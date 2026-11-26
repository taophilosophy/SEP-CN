# Automated Reasoning
**First published Wed Jul 18, 2001; substantive revision Sat Feb 10, 2024**

*Portoraro, Frederic*

Reasoning is the ability to make inferences, and automated reasoning is concerned with the building of computing systems that automate this process. Although the overall goal is to mechanize different forms of reasoning, the term has largely been identified with valid deductive reasoning as practiced in mathematics and formal logic. In this respect, automated reasoning is akin to mechanical theorem proving. Building an automated reasoning program means providing an algorithmic description to a formal calculus so that it can be implemented on a computer to prove theorems of the calculus in an efficient manner. Important aspects of this exercise involve defining the class of problems the program will be required to solve, deciding what language will be used by the program to represent the information given to it as well as new information inferred by the program, specifying the mechanism that the program will use to conduct deductive inferences, and figuring out how to perform all these computations efficiently. While basic research work continues in order to provide the necessary theoretical framework, the field has reached a point where automated reasoning programs are being used by researchers to attack open questions in mathematics and logic, provide important applications in computing science, solve problems in engineering, and find novel approaches to questions in exact philosophy.

## 1. Introduction

A problem being presented to an automated reasoning program consists of two main items, namely a statement expressing the particular question being asked called the **problem’s conclusion**, and a collection of statements expressing all the relevant information available to the program—the **problem’s assumptions**. Solving a problem means proving the conclusion from the given assumptions by the systematic application of rules of deduction embedded within the reasoning program. The problem solving process ends when one such proof is found, when the program is able to detect the non-existence of a proof, or when it simply runs out of resources.

### 1.1 Problem Domain

A first important consideration in the design of an automated reasoning program is to delineate the class of problems that the program will be required to solve—the **problem domain**. The domain can be very large, as would be the case for a general-purpose theorem prover for first-order logic, or be more restricted in scope as in a special-purpose theorem prover for Tarski’s geometry, or the modal logic K. A typical approach in the design of an automated reasoning program is to provide it first with sufficient logical power (e.g., first-order logic) and then further demarcate its scope to the particular domain of interest defined by a set of **domain axioms**. To illustrate, EQP, a theorem-proving program for equational logic, was used to solve an open question in Robbins algebra (McCune 1997)[^mccune-1997]: *Are all Robbins algebras Boolean?* For this, the program was provided with the axioms defining a Robbins algebra:

$$\begin{align} \tag{A1} &x+y=y+x & \text{(commutativity)}\\ \tag{A2} (&x+y)+z = x+ (y+z) & \text{(associativity)}\\ \tag{A3} -(-(&x+y)+ -(x+-y))=x & \text{(Robbins equation)} \end{align}$$

The program was then used to show that a characterization of Boolean algebra that uses Huntington’s equation, $$-(-x + y) + -(-x + -y) = x,$$ follows from the axioms. We should remark that this problem is non-trivial since deciding whether a finite set of equations provides a basis for Boolean algebra is undecidable, that is, it does not permit an algorithmic representation; also, the problem was attacked by Robbins, Huntington, Tarski and many of his students with no success. The key step was to establish that all Robbins algebras satisfy $$\exists x\exists y(x + y = x),$$ since it was known that this formula is a sufficient condition for a Robbins algebra to be Boolean. When EQP was supplied with this piece of information, the program provided invaluable assistance by completing the proof automatically.

A special-purpose theorem prover does not draw its main benefit by restricting its attention to the domain axioms but from the fact that the domain may enjoy particular theorem-proving techniques which can be hardwired—coded—within the reasoning program itself and which may result in a more efficient logic implementation. Much of EQP’s success at settling the Robbins question can be attributed to its built-in associative-commutative inference mechanisms.

### 1.2 Language Representation

A second important consideration in the building of an automated reasoning program is to decide (1) how problems in its domain will be presented to the reasoning program; (2) how they will actually be represented internally within the program; and, (3) how the solutions found—completed proofs—will be displayed back to the user. There are several formalisms available for this, and the choice is dependent on the problem domain and the underlying deduction calculus used by the reasoning program. The most commonly used formalisms include standard first-order logic, typed *λ*-calculus, and clausal logic. We take up clausal logic here and assume that the reader is familiar with the rudiments of first-order logic; for the typed *λ*-calculus the reader may want to check Church 1940. Clausal logic is a quantifier-free variation of first-order logic and has been the most widely used notation within the automated reasoning community. Some definitions are in order: A **term** is a constant, a variable, or a function whose arguments are themselves terms. For example, $a, x, f(x)$, and $h(c,f(z),y)$ are all terms. A **literal** is either an atomic formula, e.g. $F(x)$, or the negation of an atomic formula, e.g. ${\sim}R(x,f(a))$. Two literals are **complementary** if one is the negation of the other. A **clause** is a (possibly empty) finite disjunction of literals $l_1\vee \ldots \vee l_n$ where no literal appears more than once in the clause (that is, clauses can be alternatively treated as sets of literals). **Ground** terms, ground literals, and ground clauses have no variables. The **empty clause**, [ ], is the clause having no literals and, hence, is unsatisfiable—false under any interpretation. Some examples: ${\sim}R(a,b)$, and $F(a) \vee{\sim}R(f(x),b) \vee F(z)$ are both examples of clauses but only the former is ground. The general idea is to be able to express a problem’s formulation as a set of clauses or, equivalently, as a formula in **conjunctive normal form (CNF)**, that is, as a conjunction of clauses.

For formulas already expressed in standard logic notation, there is a systematic two-step procedure for transforming them into conjunctive normal form. The first step consists in re-expressing a formula into a semantically equivalent formula in **prenex normal form**, $(\Theta x_1)\ldots(\Theta x_n)\alpha(x_1 ,\ldots ,x_n)$, consisting of a string of quantifiers $(\Theta x_1)\ldots(\Theta x_n)$ followed by a quantifier-free expression $\alpha(x_1 ,\ldots ,x_n)$ called the **matrix**. The second step in the transformation first converts the matrix into conjunctive normal form by using well-known logical equivalences such as DeMorgan’s laws, distribution, double-negation, and others; then, the quantifiers in front of the matrix, which is now in conjunctive normal form, are dropped according to certain rules. In the presence of existential quantifiers, this latter step does not always preserve equivalence and requires the introduction of **Skolem functions** whose role is to “simulate” the behaviour of existentially quantified variables. For example, applying the skolemizing process to the formula $$\forall x\exists y\forall z\exists u\forall v[R(x,y,v) \vee{\sim}K(x,z,u,v)]$$ requires the introduction of a one-place and two-place Skolem functions, $f$ and $g$ respectively, resulting in the formula $$\forall x\forall z\forall v[R(x,f(x),v) \vee{\sim}K(x,z,g(x,z),v)]$$ The universal quantifiers can then be removed to obtain the final clause, $R(x,f(x),v) \vee{\sim}K(x,z,g(x,z),v)$ in our example. The Skolemizing process may not preserve equivalence but maintains satisfiability, which is enough for clause-based automated reasoning.

Although clausal form provides a more uniform and economical notation—there are no quantifiers and all formulas are disjunctions—it has certain disadvantages. One drawback is the increase in the size of the resulting formula when transformed from standard logic notation into clausal form. The increase in size is accompanied by an increase in cognitive complexity that makes it harder for humans to read proofs written with clauses. Another disadvantage is that the syntactic structure of a formula in standard logic notation can be used to guide the construction of a proof but this information is completely lost in the transformation into clausal form.

## 2. Deduction Calculi

A third important consideration in the building of an automated reasoning program is the selection of the actual deduction calculus that will be used by the program to perform its inferences. As indicated before, the choice is highly dependent on the nature of the problem domain and there is a fair range of options available: General-purpose theorem proving and problem solving (first-order logic, simple type theory), program verification (first-order logic), distributed and concurrent systems (modal and temporal logics), program specification (intuitionistic logic), hardware verification (higher-order logic), logic programming (Horn logic), constraint satisfaction (propositional clausal logic), mathematics (higher-order logic), computational metaphysics (higher-order modal logic), and others.

A deduction calculus consists of a set of logical axioms and a collection of deduction rules for deriving new formulas from previously derived formulas. Solving a problem in the program’s problem domain then really means establishing a particular formula *α*—the problem’s conclusion—from the extended set *Γ* consisting of the logical axioms, the domain axioms, and the problem assumptions. That is, the program needs to determine if *Γ* entails $\alpha , \Gamma \vDash \alpha$. How the program goes about establishing this semantic fact depends, of course, on the calculus it implements. Some programs may take a very **direct** route and attempt to establish that $\Gamma \vDash \alpha$ by actually constructing a step-by-step proof of *α* from *Γ*. If successful, this shows of course that *Γ* derives—proves—*α*, a fact we denote by writing $\Gamma \vdash \alpha$. Other reasoning programs may instead opt for a more **indirect** approach and try to establish that $\Gamma \vDash \alpha$ by showing that $\Gamma \cup \{{\sim}\alpha \}$ is inconsistent which, in turn, is shown by deriving a contradiction, $\bot$, from the set $\Gamma \cup \{{\sim}\alpha \}$. Automated systems that implement the former approach include natural deduction systems; the latter approach is used by systems based on resolution, sequent deduction, and matrix connection methods.

Soundness and completeness are two (metatheoretical) properties of a calculus that are particularly important for automated deduction. **Soundness** states that the rules of the calculus are truth-preserving. For a direct calculus this means that if $\Gamma \vdash \alpha$ then $\Gamma \vDash \alpha$. For indirect calculi, soundness means that if $\Gamma \cup \{{\sim}\alpha \} \vdash \bot$ then $\Gamma \vDash \alpha$. **Completeness** in a direct calculus states that if $\Gamma \vDash \alpha$ then $\Gamma \vdash \alpha$. For indirect calculi, the completeness property is expressed in terms of **refutations** since one establishes that $\Gamma \vDash \alpha$ by showing the existence of a proof, not of *α* from *Γ*, but of $\bot$ from $\Gamma \cup \{{\sim}\alpha \}$. Thus, an indirect calculus is **refutation complete** if $\Gamma \vDash \alpha$ implies $\Gamma \cup \{{\sim}\alpha \} \vdash \bot$. Of the two properties, soundness is the most desirable. An incomplete calculus indicates that there are entailment relations that cannot be established within the calculus. For an automated reasoning program this means, informally, that there are true statements that the program cannot prove. Incompleteness may be an unfortunate affair but lack of soundness is a truly problematic situation since an unsound reasoning program would be able to generate false conclusions from perfectly true information.

It is important to appreciate the difference between a logical calculus and its corresponding implementation in a reasoning program. The implementation of a calculus invariably involves making some modifications to the calculus and this results, strictly speaking, in a new calculus. The most important modification to the original calculus is the “mechanization” of its deduction rules, that is, the specification of the systematic way in which the rules are to be applied. In the process of doing so, one must exercise care to preserve the metatheoretical properties of the original calculus.

Two other metatheoretical properties of importance to automated deduction are decidability and complexity. A calculus is **decidable** if it admits an algorithmic representation, that is, if there is an algorithm that, for any given *Γ* and *α*, it can determine in a finite amount of time the answer, “Yes” or “No”, to the question “Does $\Gamma \vDash \alpha$?” A calculus may be undecidable in which case one needs to determine which decidable fragment to implement. The time-space **complexity** of a calculus specifies how efficient its algorithmic representation is. Automated reasoning is made the more challenging because many calculi of interest are not decidable and have poor complexity measures forcing researchers to seek tradeoffs between deductive power versus algorithmic efficiency.

### 2.1 Resolution

Of the many calculi used in the implementation of reasoning programs, the ones based on the **resolution** principle have been the most popular. Resolution is modeled after the chain rule (of which Modus Ponens is a special case) and essentially states that from $p \vee q$ and ${\sim}q \vee r$ one can infer $p \vee r$. More formally, let $C - l$ denote the clause $C$ with the literal $l$ removed. Assume that $C_1$ and $C_2$ are ground clauses containing, respectively, a positive literal $l_1$ and a negative literal ${\sim}l_2$ such that $l_1$ and ${\sim}l_2$ are complementary. Then, the rule of **ground resolution** states that, as a result of **resolving** $C_1$ and $C_2$, one can infer $(C_1 - l_1) \vee(C_2 - {\sim}l_2)$:

$$\tag{ground resolution}\frac{C_1 C_2}{(C_1 - l_1)\vee (C_2 - \sim l_2)}$$

**Herbrand’s theorem** (Herbrand 1930)[^herbrand-1930] assures us that the non-satisfiability of *any* set of clauses, ground or not, can be established by using ground resolution. This is a very significant result for automated deduction since it tells us that if a set *Γ* is not satisfied by any of the infinitely many interpretations, this fact can be determined in *finitely* many steps. Unfortunately, a direct implementation of ground resolution using Herbrand’s theorem requires the generation of a vast number of ground terms making this approach hopelessly inefficient. This issue was effectively addressed by generalizing the ground resolution rule to **binary resolution** and by introducing the notion of unification (Robinson 1965a). Unification allows resolution proofs to be “lifted” and be conducted at a more general level; clauses only need to be instantiated at the moment where they are to be resolved. Moreover, the clauses resulting from the instantiation process do not have to be ground instances and may still contain variables. The introduction of binary resolution and unification is considered one of the most important developments in the field of automated reasoning.

#### Unification

A **unifier** of two expressions—terms or clauses—is a substitution that when applied to the expressions makes them equal. For example, the substitution *σ* given by

$$\sigma := \{x \leftarrow b, y \leftarrow b, z \leftarrow f(a,b)\}$$

is a unifier for

$$R(x,f(a,y))$$

and

$$R(b,z)$$

since when applied to both expressions it makes them equal:

$$\begin{aligned} R(x, f(a, y))\sigma & = R(b, f(a, b))\\ & = R(b, z)\sigma \end{aligned}$$

A **most general unifier** (mgu) produces the most general instance shared by two unifiable expressions. In the previous example, the substitution $\{x \leftarrow b, y \leftarrow b, z \leftarrow f(a,b)\}$ is a unifier but not an mgu; however, $\{x \leftarrow b, z \leftarrow f(a,y)\}$ is an mgu. Note that unification attempts to “match” two expressions and this fundamental process has become a central component of most automated deduction programs, resolution-based and otherwise. **Theory-unification** is an extension of the unification mechanism that includes built-in inference capabilities. For example, the clauses $R(g(a,b),x)$ and $R(g(b,a),d)$ do not unify but they AC-unify, where AC-unification is unification with built-in associative and commutative rules such as $g(a,b) = g(b,a)$. Shifting inference capabilities into the unification mechanism adds power but at a price: The existence of an mgu for two unifiable expressions may not be unique (there could actually be infinitely many), and the unification process becomes undecidable in general.

#### Binary resolution

Let $C_1$ and $C_2$ be two clauses containing, respectively, a positive literal $l_1$ and a negative literal ${\sim}l_2$ such that $l_1$ and $l_2$ unify with mgu *θ*. Then,

$$\tag{binary resolution}\frac{C_1 C_2}{(C_1 \theta - l_1 \theta)\vee (C_2 \theta - \sim l_2 \theta)}$$

by binary resolution; the clause $(C_1\theta - l_1\theta) \vee (C_2\theta - {\sim}l_2\theta)$ is called a **binary resolvent** of $C_1$ and $C_2$.

#### Factoring

If two or more literals occurring in a clause $C$ share an mgu *θ* then $C\theta$ is a **factor** of $C$. For example, in $R(x,a) \vee{\sim}K(f(x),b) \vee R(c,y)$ the literals $R(x,a)$ and $R(c,y)$ unify with mgu $\{x \leftarrow c, y \leftarrow a\}$ and, hence, $R(c,a) \vee{\sim}K(f(c),b)$ is a factor of the original clause.

#### The Resolution Principle

Let $C_1$and $C_2$ be two clauses. Then, a **resolvent** obtained by **resolution** from $C_1$ and $C_2$ is defined as: (a) a binary resolvent of $C_1$ and $C_2$; (b) a binary resolvent of $C_1$ and a factor of $C_2$; (c) a binary resolvent of a factor of $C_1$ and $C_2$; or, (d) a binary resolvent of a factor of $C_1$ and a factor of $C_2$.

Resolution proofs, more precisely refutations, are constructed by deriving the empty clause [ ] from $\Gamma \cup \{{\sim}\alpha \}$ using resolution; this will always be possible if $\Gamma \cup \{{\sim}\alpha \}$ is unsatisfiable since resolution is refutation complete (Robinson 1965a). As an example of a resolution proof, we show that the set $\{\forall x(P(x) \vee Q(x)), \forall x(P(x) \supset R(x)),\forall x(Q(x) \supset R(x))\}$, denoted by *Γ*, entails the formula $\exists xR(x)$. The first step is to find the clausal form of $\Gamma \cup \{{\sim}\exists xR(x)\}$; the resulting clause set, denoted by $S_0$, is shown in steps 1 to 4 in the refutation below. The refutation is constructed by using a level-saturation method: Compute all the resolvents of the initial set, $S_0$, add them to the set and repeat the process until the empty clause is derived. (This produces the sequence of increasingly larger sets: $S_0, S_1, S_2,\ldots)$ The only constraint that we impose is that we do not resolve the same two clauses more than once.

> | $S_0$ | 1 | $P(x) \vee Q(x)$ | Assumption |
> | --- | --- | --- | --- |
> |   | 2 | *${\sim}$P*$(x) \vee R(x)$ | Assumption |
> |   | 3 | *${\sim}$Q*$(x) \vee R(x)$ | Assumption |
> |   | 4 | ${\sim}R(a)$ | Negate conclusion |
> | $S_1$ | 5 | $Q(x) \vee R(x)$ | Res 1 2 |
> |   | 6 | $P(x) \vee R(x)$ | Res 1 3 |
> |   | 7 | ${\sim}P(a)$ | Res 2 4 |
> |   | 8 | ${\sim}Q(a)$ | Res 3 4 |
> | $S_2$ | 9 | $Q(a)$ | Res 1 7 |
> |   | 10 | $P(a)$ | Res 1 8 |
> |   | 11 | $R(x)$ | Res 2 6 |
> |   | 12 | $R(x)$ | Res 3 5 |
> |   | 13 | $Q(a)$ | Res 4 5 |
> |   | 14 | $P(a)$ | Res 4 6 |
> |   | 15 | $R(a)$ | Res 5 8 |
> |   | 16 | $R(a)$ | Res 6 7 |
> | $S_3$ | 17 | $R(a)$ | Res 2 10 |
> |   | 18 | $R(a)$ | Res 2 14 |
> |   | 19 | $R(a)$ | Res 3 9 |
> |   | 20 | $R(a)$ | Res 3 13 |
> |   | 21 | [ ] | Res 4 11 |

Although the resolution proof is successful in deriving [ ], it has some significant drawbacks. To start with, the refutation is too long as it takes 21 steps to reach the contradiction, [ ]. This is due to the naïve brute-force nature of the implementation. The approach not only generates too many formulas but some are clearly redundant. Note how $R(a)$ is derived six times; also, $R(x)$ has more “information content” than $R(a)$ and one should keep the former and disregard the latter. Resolution, like all other automated deduction methods, must be supplemented by strategies aimed at improving the efficiency of the deduction process. The above sample derivation has 21 steps but research-type problems command derivations with thousands or hundreds of thousands of steps.

#### Resolution Strategies

The successful implementation of a deduction calculus in an automated reasoning program requires the integration of search strategies that reduce the search space by pruning unnecessary deduction paths. Some strategies remove redundant clauses or tautologies as soon as they appear in a derivation. Another strategy is to remove more specific clauses in the presence of more general ones by a process known as **subsumption** (Robinson 1965a). Unrestricted subsumption, however, does not preserve the refutation completeness of resolution and, hence, there is a need to restrict its applicability (Loveland 1978)[^loveland-1978]. **Model elimination** (Loveland 1969)[^loveland-1969] can discard a sentence by showing that it is false in some model of the axioms. The subject of model generation has received much attention as a complementary process to theorem proving. The method has been used successfully by automated reasoning programs to show the independence of axioms sets and to determine the existence of discrete mathematical structures meeting some given criteria.

Instead of removing redundant clauses, some strategies prevent the generation of useless clauses in the first place. The **set-of-support strategy** (Wos, Carson & Robinson 1965)[^robinson-1965][^robinson-1965-2][^wos-1965] is one of the most powerful strategies of this kind. A subset $T$ of the set $S$, where $S$ is initially $\Gamma \cup \{{\sim}\alpha \}$, is called a **set of support** of $S$ iff $S - T$ is satisfiable. Set-of-support resolution dictates that the resolved clauses are not both from $S - T$. The motivation behind set-of-support is that since the set *Γ* is usually satisfiable it might be wise not to resolve two clauses from *Γ* against each other. **Hyperresolution** (Robinson 1965b) reduces the number of intermediate resolvents by combining several resolution steps into a single inference step.

Independently co-discovered, **linear resolution** (Loveland 1970, Luckham 1970)[^loveland-1970][^luckham-1970] always resolves a clause against the most recently derived resolvent. This gives the deduction a simple “linear” structure affording a straightforward implementation; yet, linear resolution preserves refutation completeness. Using linear resolution we can derive the empty clause in the above example in only eight steps:

> | 1 | $P(x) \vee Q(x)$ | Assumption |
> | --- | --- | --- |
> | 2 | *${\sim}$P*$(x) \vee R(x)$ | Assumption |
> | 3 | *${\sim}$Q*$(x) \vee R(x)$ | Assumption |
> | 4 | ${\sim}R(a)$ | Negated conclusion |
> | 5 | ${\sim}P(a)$ | Res 2 4 |
> | 6 | $Q(a)$ | Res 1 5 |
> | 7 | $R(a)$ | Res 3 6 |
> | 8 | [ ] | Res 4 7 |

With the exception of unrestricted subsumption, all the strategies mentioned so far preserve refutation completeness. Efficiency is an important consideration in automated reasoning and one may sometimes be willing to trade completeness for speed. **Unit resolution** and **input resolution** are two such refinements of linear resolution. In the former, one of the resolved clauses is always a literal; in the latter, one of the resolved clauses is always selected from the original set to be refuted. Albeit efficient, neither strategy is complete. Ordering strategies impose some form of partial ordering on the predicate symbols, terms, literals, or clauses occurring in the deduction. **Ordered resolution** treats clauses not as sets of literals but as sequences—linear orders—of literals. Ordered resolution is extremely efficient but, like unit and input resolution, is not refutation complete. To end, it must be noted that some strategies improve certain aspects of the deduction process at the expense of others. For instance, a strategy may reduce the size of the proof search space at the expense of increasing, say, the length of the shortest refutations. A taxonomy and detailed presentation of theorem-proving strategies can be found in Bonacina 1999; for a discussion of the relative complexity (i.e. efficiency measures) of resolution see Buresh-Oppenheim & Pitassi 2003, and Urquhart 1987.

There are several automated reasoning programs that are based on resolution, or refinements of resolution. Otter (succeeded by Prover4) was a driving force in the development of automated reasoning (Wos, Overbeek, Lusk & Boyle 1984)[^wos-1984] but it has been superseded by more capable programs like Vampire (Voronkov 1995, Kovács & Voronkov 2013)[^kovács-2013][^voronkov-1995]. Resolution also provides the underlying logico-computational mechanism for the popular logic programming language Prolog (Clocksin & Mellish 1981)[^clocksin-1981].

### 2.2 Sequent Deduction

Hilbert-style calculi (Hilbert and Ackermann 1928)[^hilbert-1928] have been traditionally used to characterize logic systems. These calculi usually consist of a few axiom schemata and a small number of rules that typically include modus ponens and the rule of substitution. Although they meet the required theoretical requisites (soundness, completeness, etc.) the approach at proof construction in these calculi is difficult and does not reflect standard practice. It was Gentzen’s goal “to set up a formalism that reflects as accurately as possible the actual logical reasoning involved in mathematical proofs” (Gentzen 1935)[^gentzen-1935]. To carry out this task, Gentzen analyzed the proof-construction process and then devised two deduction calculi for classical logic: the natural deduction calculus, $\mathbf{NK}$, and the sequent calculus, $\mathbf{LK}$. (Gentzen actually designed NK first and then introduced LK to pursue metatheoretical investigations). The calculi met his goal to a large extent while at the same time managing to secure soundness and completeness. Both calculi are characterized by a relatively larger number of deduction rules and a simple axiom schema. Of the two calculi, LK is the one that has been most widely used in implementations of automated reasoning programs, and it is the one that we will discuss first; NK will be discussed in the next section.

Although the application of the LK rules affect logic formulas, the rules are seen as manipulating not logic formulas themselves but sequents. **Sequents** are expressions of the form $\Gamma \rightarrow \Delta$, where both *Γ* and $\Delta$ are (possibly empty) sets of formulas. *Γ* is the sequent’s **antecedent** and $\Delta$ its **succedent**. Sequents can be interpreted thus: Let $\mathcal{I}$ be an interpretation. Then,

> $\mathcal{I}$ satisfies the sequent $\Gamma \rightarrow \Delta$ (written as: $\mathcal{I} \vDash \Gamma \rightarrow \Delta)$ iff
> either $\mathcal{I} \not\vDash \alpha$ (for some $\alpha \in \Gamma)$ or $\mathcal{I} \vDash \beta$ (for some $\beta \in \Delta)$.

In other words,

> $\mathcal{I} \vDash \Gamma \rightarrow \Delta$ iff $\mathcal{I} \vDash(\alpha_1~ \amp \ldots \amp ~\alpha_n) \supset (\beta_1 \vee \ldots \vee \beta_n)$, where $\alpha_1~ \amp \ldots \amp ~\alpha_n$ is the iterated conjunction of the formulas in *Γ* and $\beta_1 \vee \ldots \vee \beta_n$ is the iterated disjunction of those in $\Delta$.

If *Γ* or $\Delta$ are empty then they are respectively valid or unsatisfiable. An **axiom of LK** is a sequent $\Gamma \rightarrow \Delta$ where $\Gamma \cap \Delta \ne \varnothing$. Thus, the requirement that the same formula occurs at each side of the $\rightarrow$ sign means that the axioms of LK are valid, for no interpretation can then make all the formulas in *Γ* true and, simultaneously, make all those in $\Delta$ false. LK has two rules per logical connective, plus one extra rule: the cut rule.

| Axioms | Cut Rule |   |   |
| --- | --- | --- | --- |
| <table class="no-rules cellpad-med-dense centered"> <tr> <td style="border-bottom:1px solid black;"> &nbsp;&nbsp; </td> </tr> <tr> <td style="padding:0px;"> $\Gamma , \alpha \rightarrow \Delta , \alpha$ </td> </tr> </table> | <table class="no-rules cellpad-med-dense centered"> <tr> <td style="border-bottom:1px solid black;"> $\Gamma \rightarrow \Delta , \alpha$ </td> <td style="border-bottom:1px solid black;"> $\alpha , \lambda \rightarrow \Sigma$ </td> </tr> <tr> <td colspan="2" style="padding:0px;"> $\Gamma , \lambda \rightarrow \Delta , \Sigma$ </td> </tr> </table> |   |   |
| Antecedent Rules $(\Theta \rightarrow)$ | Succedent Rules $(\rightarrow \Theta)$ |   |   |
| $\amp\rightarrow$ | <table class="no-rules cellpad-med-dense centered"> <tr> <td style="border-bottom:1px solid black;"> $\Gamma , \alpha , \beta \rightarrow \Delta$ </td> </tr> <tr> <td style="padding:0px;"> $\Gamma , \alpha \amp \beta \rightarrow \Delta$ </td> </tr> </table> | $\rightarrow\amp$ | <table class="no-rules cellpad-med-dense centered"> <tr> <td style="border-bottom:1px solid black;"> $\Gamma \rightarrow \Delta , \alpha$ </td> <td style="border-bottom:1px solid black;"> $\Gamma \rightarrow \Delta , \beta$ </td> </tr> <tr> <td colspan="2" style="padding:0px;"> $\Gamma \rightarrow \Delta , \alpha \amp \beta$ </td> </tr> </table> |
| $\vee \rightarrow$ | <table class="no-rules cellpad-med-dense centered"> <tr> <td style="border-bottom:1px solid black;"> $\Gamma , \alpha \rightarrow \Delta$ </td> <td style="border-bottom:1px solid black;"> $\Gamma , \beta \rightarrow \Delta$ </td> </tr> <tr> <td colspan="2" style="padding:0px;"> $\Gamma , \alpha \vee \beta \rightarrow \Delta$ </td> </tr> </table> | $\rightarrow \vee$ | <table class="no-rules cellpad-med-dense centered"> <tr> <td style="border-bottom:1px solid black;"> $\Gamma \rightarrow \Delta , \alpha , \beta$ </td> </tr> <tr> <td style="padding:0px;"> $\Gamma \rightarrow \Delta , \alpha \vee \beta$ </td> </tr> </table> |
| $\supset \rightarrow$ | <table class="no-rules cellpad-med-dense centered"> <tr> <td style="border-bottom:1px solid black;"> $\Gamma \rightarrow \Delta , \alpha$ </td> <td style="border-bottom:1px solid black;"> $\Gamma , \beta \rightarrow \Delta$ </td> </tr> <tr> <td colspan="2" style="padding:0px;"> $\Gamma , \alpha \supset \beta \rightarrow \Delta$ </td> </tr> </table> | $\rightarrow \supset$ | <table class="no-rules cellpad-med-dense centered"> <tr> <td style="border-bottom:1px solid black;"> $\Gamma , \alpha \rightarrow \Delta , \beta$ </td> </tr> <tr> <td style="padding:0px;"> $\Gamma \rightarrow \Delta , \alpha \supset \beta$ </td> </tr> </table> |
| $\supset \equiv$ | <table class="no-rules cellpad-med-dense centered"> <tr> <td style="border-bottom:1px solid black;"> $\Gamma , \alpha , \beta \rightarrow \Delta$ </td> <td style="border-bottom:1px solid black;"> $\Gamma \rightarrow \Delta , \alpha , \beta$ </td> </tr> <tr> <td colspan="2" style="padding:0px;"> $\Gamma , \alpha \equiv \beta \rightarrow \Delta$ </td> </tr> </table> | $\equiv \supset$ | <table class="no-rules cellpad-med-dense centered"> <tr> <td style="border-bottom:1px solid black;"> $\Gamma , \alpha \rightarrow \Delta , \beta$ </td> <td style="border-bottom:1px solid black;"> $\Gamma , \beta , \rightarrow \Delta , \alpha$ </td> </tr> <tr> <td colspan="2" style="padding:0px;"> $\Gamma \rightarrow \Delta , \alpha \equiv \beta$ </td> </tr> </table> |
| ${\sim}\rightarrow$ | <table class="no-rules cellpad-med-dense centered"> <tr> <td style="border-bottom:1px solid black;"> $\Gamma \rightarrow \Delta , \alpha$ </td> </tr> <tr> <td style="padding:0px;"> $\Gamma , {\sim}\alpha \rightarrow \Delta$ </td> </tr> </table> | $\rightarrow{\sim}$ | <table class="no-rules cellpad-med-dense centered"> <tr> <td style="border-bottom:1px solid black;"> $\Gamma , \alpha \rightarrow \Delta$ </td> </tr> <tr> <td style="padding:0px;"> $\Gamma \rightarrow \Delta , {\sim}\alpha$ </td> </tr> </table> |
| $\exists \rightarrow$ | <table class="no-rules cellpad-med-dense centered"> <tr> <td style="border-bottom:1px solid black;"> $\Gamma , \alpha(a/x) \rightarrow \Delta$ </td> </tr> <tr> <td style="padding:0px;"> $\Gamma , \exists x\alpha(x) \rightarrow \Delta$ </td> </tr> </table> | $\rightarrow \exists$ | <table class="no-rules cellpad-med-dense centered"> <tr> <td style="border-bottom:1px solid black;"> $\Gamma \rightarrow \Delta , \alpha(t/x), \exists x\alpha(x)$ </td> </tr> <tr> <td style="padding:0px;"> $\Gamma \rightarrow \Delta , \exists x\alpha(x)$ </td> </tr> </table> |
| $\forall \rightarrow$ | <table class="no-rules cellpad-med-dense centered"> <tr> <td style="border-bottom:1px solid black;"> $\Gamma , \alpha(t/x), \forall x\alpha(x) \rightarrow \Delta$ </td> </tr> <tr> <td style="padding:0px;"> $\Gamma , \forall x\alpha(x) \rightarrow \Delta$ </td> </tr> </table> | $\rightarrow \forall$ | <table class="no-rules cellpad-med-dense centered"> <tr> <td style="border-bottom:1px solid black;"> $\Gamma \rightarrow \Delta , \alpha(a/x)$ </td> </tr> <tr> <td style="padding:0px;"> $\Gamma \rightarrow \Delta , \forall x\alpha(x)$ </td> </tr> </table> |

The sequents above a rule’s line are called the **rule’s premises** and the sequent below the line is the **rule’s conclusion**. The quantification rules $\exists \rightarrow$ and $\rightarrow \forall$ have an eigenvariable condition that restricts their applicability, namely that $a$ must not occur in $\Gamma , \Delta$ or in the quantified sentence. The purpose of this restriction is to ensure that the choice of parameter, $a$, used in the substitution process is completely “arbitrary”.

Proofs in LK are represented as trees where each node in the tree is labeled with a sequent, and where the original sequent sits at the root of the tree. The children of a node are the premises of the rule being applied at that node. The leaves of the tree are labeled with axioms. Here is the LK-proof of $\exists xR(x)$ from the set $\{\forall x(P(x) \vee Q(x)), \forall x(P(x) \supset R(x)),\forall x(Q(x) \supset R(x))\}$. In the tree below, *Γ* stands for this set:

| <table class="cellpad-med-dense" style="margin-bottom:0px;"> <tr> <td style="border-bottom:1px solid black;"> $\Gamma ,P(a) \rightarrow$ $P(a),R(a),\exists xR(x)$ </td> <td style="border-bottom:1px solid black;"> $\Gamma ,P(a),R(a) \rightarrow$ $R(a),\exists xR(x)$ </td> </tr> <tr> <td colspan="2" style="border-bottom:1px solid black;"> $\Gamma ,P(a),P(a) \supset R(a) \rightarrow R(a),\exists xR(x)$ </td> </tr> <tr> <td colspan="2"> $\Gamma ,P(a) \rightarrow R(a),\exists xR(x)$ </td> </tr> </table> | <table class="cellpad-med-dense" style="border-spacing:0px; margin-bottom:0px;"> <tr> <td style="border-bottom:1px solid black;"> $\Gamma ,Q(a) \rightarrow$ $Q(a),R(a),\exists xR(x)$ </td> <td style="border-bottom:1px solid black;"> $\Gamma ,Q(a),R(a) \rightarrow$ $R(a),\exists xR(x)$ </td> </tr> <tr> <td colspan="2" style="border-bottom:1px solid black;"> $\Gamma ,Q(a),Q(a) \supset R(a) \rightarrow R(a),\exists xR(x)$ </td> </tr> <tr> <td colspan="2"> $\Gamma ,Q(a) \rightarrow R(a),\exists xR(x)$ </td> </tr> </table> |
| --- | --- |
| <table class="centered cellpad-med-dense centercell"> <tr> <td style="border-bottom:1px solid black;"> $\Gamma ,P(a) \vee Q(a) \rightarrow R(a),\exists xR(x)$ </td> </tr> <tr> <td style="border-bottom:1px solid black;"> $\Gamma \rightarrow R(a),\exists xR(x)$ </td> </tr> <tr> <td> $\Gamma \rightarrow \exists xR(x)$ </td> </tr> </table> |   |

In our example, all the leaves in the proof tree are labeled with axioms. This establishes the validity of $\Gamma \rightarrow \exists xR(x)$ and, hence, the fact that $\Gamma \vDash \exists xR(x)$. LK takes an indirect approach at proving the conclusion and this is an important difference between LK and NK. While NK constructs an actual proof (of the conclusion from the given assumptions), LK instead constructs a proof that proves the existence of a proof (of the conclusion from the assumptions). For instance, to prove that *α* is entailed by *Γ*, NK constructs a step-by-step proof of *α* from *Γ* (assuming that one exists); in contrast, LK first constructs the sequent $\Gamma \rightarrow \alpha$ which then attempts to prove valid by showing that it cannot be made false. This is done by searching for a counterexample that makes (all the sentences in) *Γ* true and makes *α* false: If the search fails then a counterexample does not exist and the sequent is therefore valid. In this respect, proof trees in LK are actually refutation proofs. Like resolution, LK is refutation complete: If $\Gamma \vDash \alpha$ then the sequent $\Gamma \rightarrow \alpha$ has a proof tree.

As it stands, LK is unsuitable for automated deduction and there are some obstacles that must be overcome before it can be efficiently implemented. The reason is, of course, that the statement of the completeness of LK only has to assert, for each entailment relation, the existence of a proof tree but a reasoning program has the more difficult task of actually having to construct one. Some of the main obstacles: First, LK does not specify the order in which the rules must be applied in the construction of a proof tree. Second, and as a particular case of the first problem, the premises in the rules $\forall \rightarrow$ and $\rightarrow \exists$ rules inherit the quantificational formula to which the rule is applied, meaning that the rules can be applied repeatedly to the same formula sending the proof search into an endless loop. Third, LK does not indicate which formula must be selected next in the application of a rule. Fourth, the quantifier rules provide no indication as to what terms or free variables must be used in their deployment. Fifth, and as a particular case of the previous problem, the application of a quantifier rule can lead into an infinitely long tree branch because the proper term to be used in the instantiation never gets chosen. Fortunately, as we will hint at below each of these problems can be successfully addressed.

Axiom sequents in LK are valid, and the conclusion of a rule is valid iff its premises are. This fact allows us to apply the LK rules in either direction, forwards from axioms to conclusion, or backwards from conclusion to axioms. Also, with the exception of the cut rule, all the rules’ premises are subformulas of their respective conclusions. For the purposes of automated deduction this is a significant fact and we would want to dispense with the cut rule; fortunately, the cut-free version of LK preserves its refutation completeness (Gentzen 1935)[^gentzen-1935]. These results provide a strong case for constructing proof trees in a backwards fashion; indeed, by working this way a refutation in cut-free LK gets increasingly simpler as it progresses since subformulas are simpler than their parent formulas. Moreover, and as far as propositional rules go, the new subformulas entered into the tree are completely dictated by the cut-free LK rules. Furthermore, and assuming the proof tree can be brought to completion, branches eventually end up with atoms and the presence of axioms can be quickly determined. Another reason for working backwards is that the truth-functional fragment of cut-free LK is **confluent** in the sense that the order in which the non-quantifier rules are applied is irrelevant: If there is a proof, regardless of what you do, you will run into it! To bring the quantifier rules into the picture, things can be arranged so that all rules have a fair chance of being deployed: Apply, as far as possible, all the non-quantifier rules before applying any of the quantifier rules. This takes care of the first and second obstacles, and it is no too difficult to see how the third one would now be handled. The fourth and fifth obstacles can be addressed by requiring that the terms to be used in the substitutions be suitably selected from the Herbrand universe (Herbrand 1930)[^herbrand-1930].

The use of sequent-type calculi in automated theorem proving was initiated by efforts to mechanize mathematics (Wang 1960)[^wang-1960][^wang-1960-2]. At the time, resolution captured most of the attention of the automated reasoning community but during the 1970s some researchers started to further investigate non-resolution methods (Bledsoe 1977)[^bledsoe-1977], prompting a frutiful and sustained effort to develop more human-oriented theorem proving systems (Bledsoe 1975, Nevins 1974)[^bledsoe-1975]. Eventually, sequent-type deduction gained momentum again, particularly in its re-incarnation as **analytic tableaux** (Fitting 1990)[^fitting-1990]. The method of deduction used in tableaux is essentially cut-free LK’s with sets used in lieu of sequents.

### 2.3 Natural Deduction

Although LK and NK are both commonly labeled as “natural deduction” systems, it is the latter which better deserves the title due to its more natural, human-like, approach to proof construction. The rules of NK are typically presented as acting on standard logic formulas in an implicitly understood context, but they are also commonly given in the literature as acting more explicitly on “judgements”, that is, expressions of the form $\Gamma \vdash \alpha$ where *Γ* is a set of formulas and *α* is a formula. This form is typically understood as making the metastatement that there is a proof of *α* from *Γ* (Kleene 1962)[^kleene-1962]. Following Gentzen 1935 and Prawitz 1965 here we take the former approach. The system NK has no logical axioms and provides two introduction-elimination rules for each logical connective:

| Introduction Rules $(\Theta \mathbf{I})$ | Elimination Rules $(\Theta \mathbf{E})$ |   |   |
| --- | --- | --- | --- |
| $\amp$I | <table class="no-rules cellpad-med-dense centered"> <tr> <td style="padding:0px;border-bottom:1px solid black; text-align:center;"> $\alpha$ </td> <td style="padding:0px;border-bottom:1px solid black; text-align:center;"> $\beta$ </td> </tr> <tr> <td style="padding:0px; text-align:center;" colspan="2"> $\alpha \amp \beta$ </td> </tr> </table> | $\amp$E | <table class="no-rules centered" style="border-spacing:0px;"> <tr> <td style="padding:0px;border-bottom:1px solid black; text-align:center;"> $\alpha_1 \amp \alpha_2$ </td> </tr> <tr> <td style="padding:0px; text-align:center;"> $\alpha_i$ (for $i = 1,2)$ </td> </tr> </table> |
| $\vee$I | <table class="no-rules centered" style="border-spacing:0px;"> <tr> <td style="padding:0px;border-bottom:1px solid black; text-align:center;"> $\alpha_i$ (for $i = 1,2)$ </td> </tr> <tr> <td> $\alpha_1 \vee \alpha_2$ </td> </tr> </table> | $\vee$E | <table class="no-rules cellpad-med-dense centered"> <tr> <td style="border-bottom:1px solid black; text-align:center;"> $\alpha \vee \beta$ </td> <td style="border-bottom:1px solid black; text-align:center;"> [$\alpha$ &mdash; $\gamma$] </td> <td style="border-bottom:1px solid black; text-align:center;"> [$\beta$ &mdash; $\gamma$] </td> </tr> <tr> <td style="padding:0px; text-align:center;" colspan="3"> $\gamma$ </td> </tr> </table> |
| $\supset$I | <table class="no-rules cellpad-med-dense centered"> <tr> <td style="padding:0px;border-bottom:1px solid black; text-align:center;"> [$\alpha$ &mdash; $\beta$] </td> </tr> <tr> <td style="padding:0px; text-align:center;"> $\alpha \supset \beta$ </td> </tr> </table> | $\supset$E | <table class="no-rules cellpad-med-dense centered"> <tr> <td style="border-bottom:1px solid black; text-align:center;"> $\alpha$ </td> <td style="border-bottom:1px solid black; text-align:center;"> $\alpha \supset \beta$ </td> </tr> <tr> <td colspan="2"> $\beta$ </td> </tr> </table> |
| $\equiv$I | <table class="no-rules cellpad-med-dense centered"> <tr> <td style="border-bottom:1px solid black; text-align:center;"> [$\alpha$ &mdash; $\beta$] </td> <td style="border-bottom:1px solid black; text-align:center;"> [$\beta$ &mdash; $\alpha$] </td> </tr> <tr> <td colspan="2"> $\alpha \equiv \beta$ </td> </tr> </table> | $\equiv$E | <table class="no-rules cellpad-med-dense centered"> <tr> <td style="border-bottom:1px solid black; text-align:center;"> $\alpha_i (i = 0,1)$ </td> <td style="border-bottom:1px solid black; text-align:center;"> $\alpha_0 \equiv \alpha_1$ </td> </tr> <tr> <td colspan="2"> $\alpha_{1-i}$ </td> </tr> </table> |
| ${\sim}$I | <table class="no-rules cellpad-med-dense centered"> <tr> <td style="padding:0px;border-bottom:1px solid black; text-align:center;"> [$\alpha$ &mdash; $\bot$] </td> </tr> <tr> <td style="padding:0px; text-align:center;"> ${\sim}\alpha$ </td> </tr> </table> | ${\sim}$E | <table class="no-rules cellpad-med-dense centered"> <tr> <td style="padding:0px;border-bottom:1px solid black; text-align:center;"> [${\sim}\alpha$ &mdash; $\bot$] </td> </tr> <tr> <td style="padding:0px; text-align:center;"> $\alpha$ </td> </tr> </table> |
| $\exists$I | <table class="no-rules cellpad-med-dense centered"> <tr> <td style="padding:0px;border-bottom:1px solid black; text-align:center;"> $\alpha(t/x)$ </td> </tr> <tr> <td style="padding:0px; text-align:center;"> $\exists x\alpha(x)$ </td> </tr> </table> | $\exists$E | <table class="no-rules cellpad-med-dense centered"> <tr> <td style="border-bottom:1px solid black; text-align:center;"> $\exists x\alpha(x)$ </td> <td style="border-bottom:1px solid black; text-align:center;"> [$\alpha(a/x)$ &mdash; $\beta$] </td> </tr> <tr> <td colspan="2"> $\beta$ </td> </tr> </table> |
| $\forall$I | <table class="no-rules cellpad-med-dense centered"> <tr> <td style="padding:0px;border-bottom:1px solid black; text-align:center;"> $\alpha(a/x)$ </td> </tr> <tr> <td style="padding:0px; text-align:center;"> $\forall x\alpha(x)$ </td> </tr> </table> | $\forall$E | <table class="no-rules cellpad-med-dense centered"> <tr> <td style="padding:0px;border-bottom:1px solid black; text-align:center;"> $\forall x\alpha(x)$ </td> </tr> <tr> <td style="padding:0px; text-align:center;"> $\alpha(t/x)$ </td> </tr> </table> |

A few remarks: First, the expression [*α*—$ \gamma$] represents the fact that *α* is an auxiliary assumption in the proof of *γ* that eventually gets discharged, i.e. discarded. For example, $\exists$E tells us that if in the process of constructing a proof one has already derived $\exists x\alpha(x)$ and also *β* with $\alpha(a/x)$ as an auxiliary assumption then the inference to *β* is allowed. Second, the eigenparameter, $a$, in $\exists$E and $\forall$I must be foreign to the premises, undischarged—“active”—assumptions, to the rule’s conclusion and, in the case of $\exists$E, to $\exists x\alpha(x)$. Third, $\bot$ is shorthand for two contradictory formulas, *β* and ${\sim}\beta$. Finally, NK is complete: If $\Gamma \vDash \alpha$ then there is a proof of *α* from *Γ* using the rules of NK.

As in LK, proofs constructed in NK are represented as trees with the proof’s conclusion sitting at the root of the tree, and the problem’s assumptions sitting at the leaves. (Proofs are also typically given as sequences of judgements, $\Gamma \vdash \alpha$, running from the top to the bottom of the printed page.) Here is a natural deduction proof tree of $\exists xR(x)$ from $\forall x(P(x) \vee Q(x)), \forall x(P(x) \supset R(x))$ and $\forall x(Q(x) \supset R(x))$:

| <table class="cellpad-med-dense" style="margin-bottom:0px;"> <tr> <td style="border-bottom:1px solid black;"> $\forall x(P(x)\vee Q(x))$ </td> </tr> <tr> <td> $P(a)\vee Q(a)$ </td> </tr> </table> | <table class="cellpad-med-dense" style="margin-bottom:0px;"> <tr style="vertical-align:bottom;"> <td style="border-bottom:1px solid black;"> <table class="cellpad-med-dense" style="margin-bottom:0px;"> <tr> <td style="border-bottom:1px solid black;"> $\forall x(P(x)\supset R(x))$ </td> </tr> <tr> <td> $P(a)\supset R(a)$ </td> </tr> </table> </td> <td style="border-bottom:1px solid black;"> [$P(a)$&mdash;$R(a)$] </td> </tr> <tr> <td colspan="2"> $R(a)$ </td> </tr> </table> | <table class="cellpad-med-dense" style="margin-bottom:0px;"> <tr style="vertical-align:bottom;"> <td style="border-bottom:1px solid black;"> <table class="cellpad-med-dense" style="margin-bottom:0px;"> <tr> <td style="border-bottom:1px solid black;"> $\forall x(Q(x)\supset R(x))$ </td> </tr> <tr> <td> $Q(a)\supset R(a)$ </td> </tr> </table> </td> <td style="border-bottom:1px solid black;"> [$Q(a)$&mdash;$R(a)$]</td> </tr> <tr> <td colspan="2"> $R(a)$ </td> </tr> </table> |
| --- | --- | --- |
| <table class="centered cell-center" style="margin-bottom:0px"> <tr> <td style="border-bottom:1px solid black;">$R(a)$</td></tr> <tr> <td>$\exists xR(x)$ </td></tr> </table> |   |   |

As in LK, a forward-chaining strategy for proof construction is not well focused. So, although proofs are *read* forwards, that is, from leaves to root or, logically speaking, from assumptions to conclusion, that is not the way in which they are typically *constructed*. A backward-chaining strategy implemented by applying the rules in reverse order is more effective. Many of the obstacles that were discussed above in the implementation of sequent deduction are applicable to natural deduction as well. These issues can be handled in a similar way, but natural deduction introduces some issues of its own. For example, as suggested by the $\supset$-Introduction rule, to prove a goal of the form $\alpha \supset \beta$ one could attempt to prove *β* on the assumption that *α*. But note that although the goal $\alpha \supset \beta$ does not match the conclusion of any other introduction rule, it matches the conclusion of all *elimination* rules and the reasoning program would need to consider those routes too. Similarly to forward-chaining, here there is the risk of setting goals that are irrelevant to the proof and that could lead the program astray. To wit: What prevents a program from entering the never-ending process of building, say, larger and larger conjunctions? Or, what is there to prevent an uncontrolled chain of backward applications of, say, $\supset$-Elimination? Fortunately, NK enjoys the **subformula property** in the sense that each formula entering into a natural deduction proof can be restricted to being a subformula of $\Gamma \cup \Delta \cup \{\alpha \}$, where $\Delta$ is the set of auxiliary assumptions made by the ${\sim}$-Elimination rule. By exploiting the subformula property a natural deduction automated theorem prover can drastically reduce its search space and bring the backward application of the elimination rules under control (Portoraro 1998, Sieg & Byrnes 1996)[^portoraro-1998][^sieg-1996]. Further gains can be realized if one is willing to restrict the scope of NK’s logic to its intuitionistic fragment where every proof has a normal form in the sense that no formula is obtained by an introduction rule and then is eliminated by an elimination rule (Prawitz 1965)[^prawitz-1965].

Implementations of automated theorem proving systems using NK deduction have been motivated by the desire to have the program reason with precisely the same proof format and methods employed by the human user. This has been particularly true in the area of education where the student is engaged in the interactive construction of formal proofs in an NK-like calculus working under the guidance of a theorem prover ready to provide assistance when needed (Portoraro 1994, Suppes 1981)[^portoraro-1994][^suppes-1981]. Other, research-oriented, theorem provers true to the spirit of NK exist (Pelletier 1998)[^pelletier-1998] but are rare.

### 2.4 The Matrix Connection Method

The name of the matrix connection method (Bibel 1981)[^bibel-1981] is indicative of the way it operates. The term “matrix” refers to the form in which the set of logic formulas expressing the problem is represented; the term “connection” refers to the way the method operates on these formulas. To illustrate the method at work, we will use an example from propositional logic and show that $R$ is entailed by $P \vee Q, P \supset R$ and $Q \supset R$. This is done by establishing that the formula

$$(P \vee Q) \amp(P \supset R) \amp(Q \supset R) \amp{\sim}R$$

is unsatisfiable. To do this, we begin by transforming it into conjunctive normal form:

$$(P \vee Q) \amp({\sim}P \vee R) \amp({\sim}Q \vee R) \amp{\sim}R$$

This formula is then represented as a matrix, one conjunct per row and, within a row, one disjunct per column:

| $P$ | $ Q$ |
| --- | --- |
| ${\sim}P$ | $R$ |
| ${\sim}Q$ | $R$ |
| ${\sim}R$ |   |

The idea now is to explore all the possible vertical paths running through this matrix. A **vertical path** is a set of literals selected from each row in the matrix such that each literal comes from a different row. The vertical paths:

| *Path 1* | $P, {\sim}P, {\sim}Q$ and ${\sim}R$ |
| --- | --- |
| *Path 2* | $P, {\sim}P, R$ and ${\sim}R$ |
| *Path 3* | $P, R, {\sim}Q$ and ${\sim}R$ |
| *Path 4* | $P, R, R$ and ${\sim}R$ |
| *Path 5* | $Q, {\sim}P, {\sim}Q$ and ${\sim}R$ |
| *Path 6* | $Q, {\sim}P, R$ and ${\sim}R$ |
| *Path 7* | $Q, R, {\sim}Q$ and ${\sim}R$ |
| *Path 8* | $Q, R, R$ and ${\sim}R$ |

A path is **complementary** if it contains two literals which are complementary. For example, Path 2 is complementary since it has both $P$ and ${\sim}P$ but so is Path 6 since it contains both $R$ and ${\sim}R$. Note that as soon as a path includes two complementary literals there is no point in pursuing the path since it has itself become complementary. This typically allows for a large reduction in the number of paths to be inspected. In any event, all the paths in the above matrix are complementary and this fact establishes the unsatisfiability of the original formula. This is the essence of the matrix connection method. The method can be extended to predicate logic but this demands additional logical apparatus: Skolemnization, variable renaming, quantifier duplication, complementarity of paths via unification, and simultaneous substitution across all matrix paths (Bibel 1981, Andrews 1981)[^andrews-1981][^bibel-1981]. Variations of the method have been implemented in reasoning programs in higher-order logic (Andrews 1981)[^andrews-1981] and non-classical logics (Wallen 1990)[^wallen-1990].

### 2.5 Term Rewriting

Equality is an important logical relation whose behavior within automated deduction deserves its own separate treatment. **Equational logic** and, more generally, **term rewriting** treat equality-like equations as **rewrite rules**, also known as **reduction** or **demodulation rules**. An equality statement like $f(a)= a$ allows the simplification of a term like $g(c,f(a))$ to $g(c,a)$. However, the same equation also has the potential to generate an unboundedly large term: $g(c,f(a)), g(c,f(f(a))), g(c,f(f(f(a)))),\ldots$ . What distinguishes term rewriting from equational logic is that in term rewriting equations are used as unidirectional reduction rules as opposed to equality which works in both directions. Rewrite rules have the form $t_1 \Rightarrow t_2$ and the basic idea is to look for terms $t$ occurring in expressions $e$ such that $t$ unifies with $t_1$ with unifier *θ* so that the occurrence $t_1\theta$ in $e\theta$ can be replaced by $t_2\theta$. For example, the rewrite rule $x + 0 \Rightarrow x$ allows the rewriting of *succ*(*succ*(0) $+ 0)$ as *succ*(*succ*(0)).

To illustrate the main ideas in term rewriting, let us explore an example involving symbolic differentiation (the example and ensuing discussion are adapted from Chapter 1 of Baader & Nipkow 1998)[^baader-1998]. Let *der* denote the derivative respect to $x$, let $y$ be a variable different from $x$, and let $u$ and $v$ be variables ranging over expressions. We define the rewrite system:

$$\begin{align} \tag{R1} \der(x) & \Rightarrow 1\\ \tag{R2} \der(y) & \Rightarrow 0\\ \tag{R3} \der(u+v) & \Rightarrow \der(u) + \der(v)\\ \tag{R4} \der( u \times v) & \Rightarrow (u \times \der(v)) + (\der(u) \times v) \end{align}$$

Again, the symbol $\Rightarrow$ indicates that a term matching the left-hand side of a rewrite rule should be replaced by the rule’s right-hand side. To see the differentiation system at work, let us compute the derivative of $x \times x$ respect to $x$, $\der(x \times x)$:

| $\der(x \times x)$ | $\Rightarrow$ | $(x \times \der(x)) + (\der(x) \times x)$ |   | by R4 |
| --- | --- | --- | --- | --- |
|   | $\Rightarrow$ | $(x \times 1) + (\der(x) \times x)$ |   | by R1 |
|   | $\Rightarrow$ | $(x \times 1) + (1 \times x)$ |   | by R1 |

At this point, since none of the rules (R1)–(R4) applies, no further reduction is possible and the rewriting process ends. The final expression obtained is called a **normal form**, and its existence motivates the following question: Is there an expression whose reduction process will never terminate when applying the rules (R1)–(R4)? Or, more generally: Under what conditions a set of rewrite rules will always stop, for any given expression, at a normal form after finitely many applications of the rules? This fundamental question is called the **termination** problem of a rewrite system, and we state without proof that the system (R1)–(R4) meets the termination condition.

There is the possibility that when reducing an expression, the set of rules of a rewrite system could be applied in more than one way. This is actually the case in the system (R1)–(R4) where in the reduction of $\der(x \times x)$ we could have applied R1 first to the second sub-expression in $(x \times$ $\der(x)) + \der(x) \times x)$, as shown below:

| $\der(x \times x)$ | $\Rightarrow$ | $(x \times \der(x)) + (\der(x) \times x)$ |   | by R4 |
| --- | --- | --- | --- | --- |
|   | $\Rightarrow$ | $(x \times \der(x)) + (1 \times x)$ |   | by R1 |
|   | $\Rightarrow$ | $(x \times 1) + (1 \times x)$ |   | by R1 |

Following this alternative course of action, the reduction terminates with the same normal form as in the previous case. This fact, however, should not be taken for granted: A rewriting system is said to be **(globally) confluent** if and only if independently of the order in which its rules are applied every expression always ends up being reduced to its one and only normal form. It can be shown that (R1)–(R4) is confluent and, hence, we are entitled to say: “Compute *the* derivative of an expression” (as opposed to simply “$a$” derivative). Adding more rules to a system in an effort to make it more practical can have undesired consequences. For example, if we add the rule

$$\tag{R5} u+0\Rightarrow u$$

to (R1)–(R4) then we will be able to further reduce certain expressions but at the price of losing confluency. The following reductions show that $\der(x + 0)$ now has two normal forms: the computation

| $\der(x + 0)$ | $\Rightarrow$ | $\der(x) + \der(0)$ |   | by R3 |
| --- | --- | --- | --- | --- |
|   | $\Rightarrow$ | $1 + \der(0)$ |   | by R1 |

gives one normal form, and

| $\der(x + 0)$ | $\Rightarrow$ | $\der(x)$ |   | by R5 |
| --- | --- | --- | --- | --- |
|   | $\Rightarrow$ | 1 |   | by R1 |

gives another. Adding the rule

$$\tag{R6} \der(0) \Rightarrow 0$$

would allow the further reduction of $1 + \der(0)$ to $1 + 0$ and then, by R5, to 1. Although the presence of this new rule actually increases the number of alternative paths—$\der(x + 0)$ can now be reduced in four possible ways—they all end up with the same normal form, namely 1. This is no coincidence as it can be shown that (R6) actually restores confluency. This motivates another fundamental question: Under what conditions can a non-confluent system be made into an equivalent confluent one? The Knuth-Bendix **completion** algorithm (Knuth & Bendix 1970)[^knuth-1970] gives a partial answer to this question.

Term rewriting, like any other automated deduction method, needs strategies to direct its application. Rippling (Bundy, Stevens & Harmelen 1993, Basin & Walsh 1996)[^basin-1996][^bundy-1993] is a heuristic that has its origins in inductive theorem-proving that uses annotations to selectively restrict the rewriting process. The **superposition calculus** is a calculus of equational first-order logic that combines notions from first-order resolution and Knuth-Bendix ordering equality. Superposition is refutation complete (Bachmair & Ganzinger 1994)[^bachmair-1994] and is at the heart of a number of theorem provers, most notably the E equational theorem prover (Schulz 2004)[^schulz-2004] and Vampire (Voronkov 1995)[^voronkov-1995]. Superposition has been extended to higher-order logic (Bentkamp *et al*. 2021)[^bentkamp-2021].

### 2.6 Mathematical Induction

Mathematical induction is a very important technique of theorem proving in mathematics and computer science. Problems stated in terms of objects or structures that involve recursive definitions or some form of repetition invariably require mathematical induction for their solving. In particular, reasoning about the correctness of computer systems requires induction and an automated reasoning program that effectively implements induction will have important applications.

To illustrate the need for mathematical induction, assume that a property *φ* is true of the number zero and also that if true of a number then is true of its successor. Then, with our deductive systems, we can deduce that for any given number $n, \phi$ is true of it, $\phi(n)$. But we cannot deduce that *φ* is true of all numbers, $\forall x\phi(x)$; this inference step requires the rule of mathematical induction:

$$\tag{mathematical induction}\frac{\alpha(0)\quad \quad [\alpha(n)-\alpha(\textit{succ}(n))]}{\forall x \alpha(x)}$$

In other words, to prove that $\forall x\alpha(x)$ one proves that $\alpha(0)$ is the case, and that $\alpha(succ(n))$ follows from the assumption that $\alpha(n)$. The implementation of induction in a reasoning system presents very challenging search control problems. The most important of these is the ability to determine the particular way in which induction will be applied during the proof, that is, finding the appropriate induction schema. Related issues include selecting the proper variable of induction, and recognizing all the possible cases for the base and the inductive steps.

The Boyer-Moore theorem prover (Boyer & Moore 1979)[^boyer-1979] has been a most successful implementation of automated inductive theorem proving. In the spirit of Gentzen, Boyer and Moore were interested in how people prove theorems by mathematical induction. Their theorem prover is written in the functional programming language Lisp which is also the language in which theorems are represented. For instance, to express the commutativity of addition the user would enter the Lisp expression (EQUAL (PLUS X Y) (PLUS Y X)). Everything defined in the system is a functional term, including its basic “predicates”: T, F, EQUAL X Y, AND X Y, NOT X, IF X Y Z, etc. Proofs are conducted by rewriting terms that possess recursive definitions, ultimately reducing the conclusion’s statement to the T predicate. The Boyer-Moore theorem prover has been used to check the proofs of some quite deep theorems (Boyer, Kaufmann & Moore 1995)[^boyer-1995]. Lemma caching, problem statement generalization, and proof planning are techniques particularly useful in inductive theorem proving (Bundy, Harmelen & Hesketh 1991)[^bundy-1991].

ACL2 (Kaufmann & Moore 1996)[^kaufmann-1996] is a successor of, and supersedes, the Boyer-Moore prover and is intended for large-scale hardware and software verification projects. Models of computer hardware and software can be formally represented as “state machines” consisting of “states” as mathematical objects and “transitions” as functions or relations on state objects. ACL2 uses an extension of an applicative subset of Common Lisp as the natural language in which to express such notions and where models and their properties can be derived logically (Boyer & Moore 1997)[^boyer-1997]. ACL2 supports the user in the building of proofs but its primary role is to prevent logical mistakes. In a quasi-“black box” fashion, “to be a good user of ACL2 you do not have to understand how the theorem prover works. You just have to understand how to interact with it” (Kaufmann & Moore 2024 [Other Internet Resources]) but, if desired, the user can easily command ACL2 to supply its full proof output for inspection. The authors of ACL2 share the interesting insight that ACL2 users rarely read successful proofs and tend to concentrate on subgoals in failed proofs; then, they try to figure out how these goals could be proved and provide ACL2 with guidance to do so. Although ACL2 has been largely applied to the formal verification of microprocessor design (see the section *4.4 Formal Verification of Hardware*) ACL2 has found many applications in other areas of which we mention three here: the formalization of the Normalization Theorem in algebraic simplicial topology (Lambán, Martín-Mateos, Rubio & Ruiz-Reina 2012)[^lambán-2012], the formal verification of an implementation of Buchberger’s algorithm for computing Gröbner bases of polynomial ideals (Medina-Bulo, Palomo-Lozano & Ruiz-Reina 2010)[^medina-bulo-2010], and a formalization of finite group theory up to an application of the Sylow theorems (Russinoff 2023)[^russinoff-2023].

## 3. Other Logics

### 3.1 Higher-Order Logic

Higher-order logic differs from first-order logic in that quantification over functions and predicates is allowed. The statement “*Any two people are related to each other in one way or another*” can be legally expressed in higher-order logic as $\forall x\forall y\exists RR(x,y)$ but not in first-order logic. Higher-order logic is inherently more expressive than first-order logic and is closer in spirit to actual mathematical reasoning. For example, the notion of set finiteness cannot be expressed as a first-order concept. Due to its richer expressiveness, it should not come as a surprise that implementing an automated theorem prover for higher-order logic is more challenging than for first-order logic. This is largely due to the fact that unification in higher-order logic is more complex than in the first-order case: unifiable terms do not always possess a most general unifier, and higher-order unification is itself undecidable. Finally, given that higher-order logic is incomplete, there are always proofs that will be entirely out of reach for any automated reasoning program.

Methods used to automate first-order deduction can be adapted to higher-order logic. TPS (Andrews *et al*. 1996, Andrews *et al*. 2006)[^andrews-2006][^andrews-1996] is a theorem proving system for higher-order logic that uses Church’s typed *λ*-calculus as its logical representation language and is based on a connection-type deduction mechanism that incorporates Huet’s unification algorithm (Huet 1975)[^huet-1975]. As a sample of the capabilities of TPS, the program has proved automatically that a subset of a finite set is finite, the equivalence among several formulations of the Axiom of Choice, and Cantor’s Theorem that a set has more subsets than members. The latter was proved by the program by asserting that there is no onto function from individuals to sets of individuals, with the proof proceeding by a diagonal argument. HOL (Gordon & Melham 1993)[^gordon-1993] is another higher-order proof development system primarily used as an aid in the development of hardware and software safety-critical systems. HOL is based on the LCF approach to interactive theorem proving (Gordon, Milner & Wadsworth 1979)[^gordon-1979], and it is built on the strongly typed functional programming language ML. HOL, like TPS, can operate in automatic and interactive mode. Availability of the latter mode is welcomed since the most useful automated reasoning systems may well be those which place an emphasis on interactive theorem proving (Farmer, Guttman & Thayer 1993)[^farmer-1993] and can be used as assistants operating under human guidance. (Harrison 2000)[^harrison-2000] discusses the verification of floating-point algorithms and the non-trivial mathematical properties that are proved by HOL Light under the guidance of the user. Isabelle (Paulson 1994)[^paulson-1994] is a generic, higher-order, framework for rapid prototyping of deductive systems. Object logics can be formulated within Isabelle’s metalogic by using its many syntactic and deductive tools. Isabelle also provides some ready-made theorem proving environments, including Isabelle/HOL, Isabelle/ZF and Isabelle/FOL, which can be used as starting points for applications and further development by the user (Paulson 1990, Nipkow & Paulson 2002)[^nipkow-2002][^paulson-1990]. Isabelle/ZF has been used to prove equivalent formulations of the Axiom of Choice, formulations of the Well-Ordering Principle, as well as the key result about cardinal arithmetic that, for any infinite cardinal $\kappa , \kappa \cdot \kappa = \kappa$ (Paulson & Grabczewski 1996)[^paulson-1996].

To help prove higher-order theorems and discharge goals arising in interactive proofs, the user can ask Isabelle/HOL to invoke external first-order provers through Sledgehammer (Paulson 2010)[^paulson-2010], a subsystem aimed at combining the complementary capabilities of automated reasoning systems of different types, including SMT solvers (see the section on SAT Solvers; Blanchette *et al*. 2013)[^blanchette-2013]. LEO-II (Benzmüller *et al*. 2015)[^benzmüller-2015][^benzmüller-2015-2] is also a resolution-based automated theorem prover for higher-order logic that has been applied in a wide array of problems, most notably in the automation of Gödel’s ontological proof of God’s existence (see Section 4.6 Logic and Philosophy). Leo-II has been superseded by Leo-III which implements a higher-order ordered paramodulation calculus that operates within a multi-agent blackboard architecture for parallel proof search; the architecture allows to independently run agents using Leo-III’s native proof calculus as well as, in a cooperative fashion, agents for external, specialized, first- and higher-order theorem provers and model finders (Benzmüller, Steen & Wisniewski 2017, Steen and Benzmüller 2021)[^benzmüller-2017][^steen-2021].

### 3.2 Non-classical Logics

Non-classical logics (Haack 1978)[^haack-1978] such as modal logics, intuitionsitic logic, multi-valued logics, autoepistemic logics, non-monotonic reasoning, commonsense and default reasoning, relevance logic, paraconsistent logic, and so on, have been increasingly gaining the attention of the automated reasoning community. One of the reasons has been the natural desire to extend automated deduction techniques to new domains of logic. Another reason has been the need to mechanize non-classical logics as an attempt to provide a suitable foundation for artificial intelligence. A third reason has been the desire to attack some problems that are combinatorially too large to be handled by paper and pencil. Indeed, some of the work in automated non-classical logic provides a prime example of automated reasoning programs at work. To illustrate, the Ackerman Constant Problem asks for the number of non-equivalent formulas in the relevance logic R. There are actually 3,088 such formulas (Slaney 1984)[^slaney-1984] and the number was found by “sandwiching” it between a lower and an upper limit, a task that involved constraining a vast universe of $20^{400} 20$-element models in search of those models that rejected non-theorems in R. It is safe to say that this result would have been impossible to obtain without the assistance of an automated reasoning program.

There have been three basic approaches to automate the solving of problems in non-classical logic (McRobie 1991)[^mcrobie-1991]. One approach has been, of course, to try to mechanize the non-classical deductive calculi. Another has been to simply provide an equivalent formulation of the problem in first-order logic and let a classical theorem prover handle it. A third approach has been to formulate the semantics of the non-classical logic in a first-order framework where resolution or connection-matrix methods would apply. (Pelletier *et al*. 2017)[^pelletier-2017] describes an automated reasoning system for a paraconsistent logic that takes both “indirect” approaches, the translational and the truth-value approach, to prove its theorems.

#### Modal logic

Modal logics find extensive use in computing science as logics of knowledge and belief, logics of programs, and in the specification of distributed and concurrent systems. Thus, a program that automates reasoning in a modal logic such as K, K4, T, S4, or S5 would have important applications. With the exception of S5, these logics share some of the important metatheoretical results of classical logic, such as cut-elimination, and hence cut-free (modal) sequent calculi can be provided for them, along with techniques for their automation. Connection methods (Andrews 1981, Bibel 1981)[^andrews-1981][^bibel-1981] have played an important role in helping to understand the source of redundancies in the search space induced by these modal sequent calculi and have provided a unifying framework not only for modal logics but also for intuitionistic and classical logic as well (Wallen 1990)[^wallen-1990]. Current efforts to automate modal logic reasoning revolve around the translational approach mentioned above, namely to embed modal logic into classical logic and then use an existing automated reasoning system for the latter to prove theorems of the former. (Benzmüller & Paulson 2013)[^benzmüller-2013] shows how to embed quantified modal logic into simple type theory, proves the soundness and completeness of the embedding, and demonstrates with simple experiments how existing higher-order theorem provers can be used to automate proofs in modal logic. The approach can be extended to higher-order modal logic as well (Benzmüller & Paleo 2015)[^benzmüller-2015][^benzmüller-2015-2]. As a matter of fact, embeddings in classical higher-order logic can be used as a means for universal reasoning (Benzmüller 2019)[^benzmüller-2019]; that is, the embedding provides a universal logical reasoning framework that uses classical higher-order logic as a metalogic in which various other classical and non-classical logics can be represented. Further evidence to the claim of universality is provided by the semantical embedding approach to free logic and category theory (Benzmüller & Scott 2020)[^benzmüller-2020]. Embedding yields a number of practical benefits to automated deduction: universality, uniformity, expressiveness of notation and reasoning, and ready availability of existing powerful automated theorem-proving tools that are known to be sound.

#### Intuitionistic logic

There are different ways in which intuitionsitic logic can be automated. One is to directly implement the intuitionistic versions of Gentzen’s sequent and natural deduction calculi, LJ and NJ respectively. This approach inherits the stronger normalization results enjoyed by these calculi allowing for a more compact mechanization than their classical counterparts. Another approach at mechanizing intuitionistic logic is to exploit its semantic similarities with the modal logic S4 and piggy back on an automated implementation of S4. Automating intuitionistic logic has applications in software development since writing a program that meets a specification corresponds to the problem of proving the specification within an intuitionistic logic (Martin-Löf 1982)[^martin-löf-1982]. A system that automated the proof construction process would have important applications in algorithm design but also in constructive mathematics. Nuprl (Constable *et al*. 1986)[^constable-1986] is a computer system supporting a particular mathematical theory, namely constructive type theory, and whose aim is to provide assistance in the proof development process. The focus is on logic-based tools to support programming and on implementing formal computational mathematics. Over the years the scope of the Nuprl project has expanded from “proofs-as-programs” to “systems-as-theories”. Similar in spirit and based on the Curry-Howard isomorphism, the Coq system formalizes its proofs in the Calculus of Inductive Constructions, a *λ*-calculus with a rich system of types including dependent types (Coquand & Huet 1988, Coquand & Paulin-Mohring 1988)[^coquand-1988][^coquand-1988-2]. Like Nuprl, Coq is designed to assist in the development of mathematical proofs as well as computer programs from their formal specifications.

## 4. Applications

### 4.1 Logic Programming

Logic programming, particularly represented by the language **Prolog** (Colmerauer *et al*. 1973)[^colmerauer-1973], is probably the most important and widespread application of automated theorem proving. During the early 1970s, it was discovered that logic could be used as a programming language (Kowalski 1974)[^kowalski-1974]. What distinguishes logic programming from other traditional forms of programming is that logic programs, in order to solve a problem, do not explicitly state *how* a specific computation is to be performed; instead, a logic program states *what* the problem is and then delegates the task of actually solving it to an underlying theorem prover. In Prolog, the theorem prover is based on a refinement of resolution known as SLD-resolution. **SLD-resolution** is a variation of linear input resolution that incorporates a special rule for selecting the next literal to be resolved upon; SLD-resolution also takes into consideration the fact that, in the computer’s memory, the literals in a clause are actually ordered, that is, they form a sequence as opposed to a set. A Prolog **program** consists of clauses stating known facts and rules. For example, the following clauses make some assertions about flight connections:

> flight(toronto, london).
> flight(london, rome).
> flight(chicago, london).
> flight$(X, Y)$ :– flight$(X, Z)$ , flight$(Z, Y)$.

The clause flight(toronto, london) is a fact while flight$(X, Y)$ :– flight$(X, Z)$ , flight$(Z,Y)$ is a rule, written by convention as a reversed conditional (the symbol “:–” means “if”; the comma means “and”; terms starting in uppercase are variables). The former states that there is flight connection between Toronto and London; the latter states that there is a flight between cities $X$ and $Y$ if, for some city $Z$, there is a flight between $X$ and $Z$ and one between $Z$ and $Y$. Clauses in Prolog programs are a special type of Horn clauses having precisely one positive literal: **Facts** are program clauses with no negative literals while **rules** have at least one negative literal. (Note that in standard clause notation the program rule in the previous example would be written as flight$(X,Y) \vee{\sim}$flight$(X,Z) \vee{\sim}$flight$(Z,Y)$.) The specific form of the program rules is to effectively express statements of the form: “*If these conditions over here are jointly met then this other fact will follow*”. Finally, a **goal** is a Horn clause with no positive literals. The idea is that, once a Prolog program *Π* has been written, we can then try to determine if a new clause *γ*, the goal, is entailed by $\Pi , \Pi \vDash \gamma$; the Prolog prover does this by attempting to derive a contradiction from $\Pi \cup \{{\sim}\gamma \}$. We should remark that program facts and rules alone cannot produce a contradiction; a goal must enter into the process. Like input resolution, SLD-resolution is not refutation complete for first-order logic but it is complete for the Horn logic of Prolog programs. The fundamental theorem: If *Π* is a Prolog program and *γ* is the goal clause then $\Pi \vDash \gamma$ iff $\Pi \cup \{{\sim}\gamma \} \vdash [\,]$ by SLD-resolution (Lloyd 1984)[^lloyd-1984].

For instance, to find out if there is a flight from Toronto to Rome one asks the Prolog prover to see if the clause flight(toronto, rome) follows from the given program. To do this, the prover adds ${\sim}$flight(toronto,rome) to the program clauses and attempts to derive the empty clause, $[\,]$, by SLD-resolution:

| 1 | flight(toronto, london) | Program clause |
| --- | --- | --- |
| 2 | flight(london, rome) | Program clause |
| 3 | flight(chicago, london) | Program clause |
| 4 | flight$(X,Y) \vee{\sim}$flight$(X,Z) \vee{\sim}$flight$(Z,Y)$ | Program clause |
| 5 | ${\sim}$flight(toronto, rome) | Negated conclusion |
| 6 | ${\sim}$flight(toronto,$Z) \vee{\sim}$flight$(Z$, rome) | Res 5 4 |
| 7 | ${\sim}$flight(london, rome) | Res 6 1 |
| 8 | $[ \,]$ | Res 7 2 |

The conditional form of rules in Prolog programs adds to their readability and also allows reasoning about the underlying refutations in a more friendly way: To prove that there is a flight between Toronto and Rome, flight(toronto,rome), unify this clause with the consequent flight$(X,Y)$ of the fourth clause in the program which itself becomes provable if both flight(toronto,$Z)$ and flight$(Z$,rome) can be proved. This can be seen to be the case under the substitution $\{Z \leftarrow$ london$\}$ since both flight(toronto,london) and flight(london,rome) are themselves provable. Note that the theorem prover not only establishes that there is a flight between Toronto and Rome but it can also come up with an actual itinerary, Toronto-London-Rome, by extracting it from the unifications used in the proof.

There are at least two broad problems that Prolog must address in order to achieve the ideal of a logic programming language. Logic programs consist of facts and rules describing what is true; anything that is not provable from a program is deemed to be false. In regards to our previous example, *flight*(*toronto*, *boston*) is not true since this literal cannot be deduced from the program. The identification of falsity with non-provability is further exploited in most Prolog implementations by incorporating an operator, **not**, that allows programmers to explicitly express the negation of literals (or even subclauses) within a program. By definition, not $l$ succeeds if the literal $l$ itself fails to be deduced. This mechanism, known as **negation-by-failure**, has been the target of criticism. Negation-by-failure does not fully capture the standard notion of negation and there are significant logical differences between the two. Standard logic, including Horn logic, is monotonic which means that enlarging an axiom set by adding new axioms simply enlarges the set of theorems derivable from it; negation-by-failure, however, is **non-monotonic** and the addition of new program clauses to an existing Prolog program may cause some goals to cease from being theorems. A second issue is the **control problem**. Currently, programmers need to provide a fair amount of control information if a program is to achieve acceptable levels of efficiency. For example, a programmer must be careful with the order in which the clauses are listed within a program, or how the literals are ordered within a clause. Failure to do a proper job can result in an inefficient or, worse, non-terminating program. Programmers must also embed hints within the program clauses to prevent the prover from revisiting certain paths in the search space (by using the **cut** operator) or to prune them altogether (by using **fail**. Last but not least, in order to improve their efficiency, many implementations of Prolog do not implement unification fully and bypass a time-consuming yet critical test—the so-called **occurs-check**—responsible for checking the suitability of the unifiers being computed. This results in an unsound calculus and may cause a goal to be entailed by a Prolog program (from a computational point of view) when in fact it should not (from a logical point of view).

There are variations of Prolog intended to extend its scope. By implementing a model elimination procedure, the Prolog Technology Theorem Prover (PTTP) (Stickel 1992)[^stickel-1992] extends Prolog into full first-order logic. The implementation achieves both soundness and completeness. Moving beyond first-order logic, *λ*Prolog (Miller & Nadathur 1988)[^miller-1988] bases the language on higher-order constructive logic.

### 4.2 SAT Solvers

The problem of determining the satisfiability of logic formulas has received much attention by the automated reasoning community due to its important applicability in industry. A propositional formula is **satisfiable** if there is an assignment of truth-values to its variables that makes the formula true. For example, the assignment $(P \leftarrow$ true, $Q \leftarrow$ true, $R \leftarrow$ false) does not make $(P \vee R) \amp{\sim}Q$ true but $(P \leftarrow$ true, $Q \leftarrow$ false, $R \leftarrow$ false) does and, hence, the formula is satisfiable. Determining whether a formula is satisfiable or not is called the Boolean Satisfiability Problem—$\mathbf{SAT}$ for short—and for a formula with $n$ variables SAT can be settled thus: Inspect each of the $2^n$ possible assignments to see if there is at least one assignment that satisfies the formula, i.e. makes it true. This method is clearly complete: If the original formula is satisfiable then we will eventually find one such satisfying assignment; but if the formula is contradictory (i.e. non-satisfiable), we will be able to determine this too. Just as clearly, and particularly in this latter case, this search takes an exponential amount of time, and the desire to conceive more efficient algorithms is well justified particularly because many computing problems of great practical importance such as graph-theoretic problems, network design, storage and retrieval, scheduling, program optimization, and many others (Garey & Johnson 1979) can be expressed as SAT instances, i.e. as the SAT question of some propositional formula representing the problem. Given that SAT is NP-complete (Cook 1971)[^cook-1971] it is very unlikely that a polynomial algorithm exists for it; however, this does not preclude the existence of sufficiently efficient algorithms for particular cases of SAT problems.

The Davis-Putnam-Logemann-Loveland $(\mathbf{DPLL})$ algorithm was one of the first SAT search algorithms (Davis & Putnam 1960; Davis, Logemman & Loveland 1962)[^davis-1962][^davis-1960] and is still considered one of the best complete SAT solvers; many of the complete SAT procedures in existence today can be considered optimizations and generalizations of DPLL. In essence, DPLL search procedures proceed by considering ways in which assignments can be chosen to make the original formula true. For example, consider the formula in CNF $$P \amp{\sim}Q \amp({\sim}P \vee Q \vee R) \amp(P \vee{\sim}S)$$ Since $P$ is a conjunct, but also a unit clause, $P$ must be true if the entire formula is to be true. Moreover, the value of ${\sim}P$ does not contribute to the truth of ${\sim}P \vee Q \vee R$ and $P \vee{\sim}S$ is true regardless of $S$. Thus, the whole formula reduces to $${\sim}Q \amp(Q \vee R)$$ Similarly, ${\sim}Q$ must be true and the formula further reduces to $$R$$ which forces $R$ to be true. From this process we can recover the assignment $(P \leftarrow$ true, $Q \leftarrow$ false, $R \leftarrow$ true, $S \leftarrow$ false) proving that the original formula is satisfiable. A formula may cause the algorithm to branch; the search through a branch reaches a dead end the moment a clause is deemed false—a **conflicting clause**—and all variations of the assignment that has been partially constructed up to this point can be discarded. To illustrate:

| 1 | $R \amp(P \vee Q) \amp({\sim}P \vee Q) \amp({\sim}P \vee{\sim}Q)$ | Given |
| --- | --- | --- |
| 2 | $(P \vee Q) \amp({\sim}P \vee Q) \amp({\sim}P \vee{\sim}Q)$ | By letting $R \leftarrow$ true |
| 3 | $Q \amp{\sim}Q$ | By letting $P \leftarrow$ true |
| 4 | ? | Conflict: $Q$ and ${\sim}Q$ cannot both be true |
| 5 | $(P \vee Q) \amp({\sim}P \vee Q) \amp({\sim}P \vee{\sim}Q)$ | Backtrack to (2): $R \leftarrow$ true still holds |
| 6 | ${\sim}P$ | By letting $Q \leftarrow$ true |
| 7 | true | By letting ${\sim}P$ be true, i.e., $P \leftarrow$ false |

Hence, the formula is satisfiable by the existence of $(P \leftarrow$ false, $Q \leftarrow$ true, $R \leftarrow$ true). DPLL algorithms are made more efficient by strategies such as **term indexing** (ordering of the formula variables in an advantageous way), **chronological backtracking** (undoing work to a previous branching point if the process leads to a conflicting clause), and **conflict-driven learning** (determining the information to keep and where to backtrack). The combination of these strategies results in a large prune of the search space; for a more extensive discussion the interested reader is directed to Zhang & Malik 2002.

A quick back-envelope calculation reveals the staggering computing times of (algorithms for) SAT-type problems represented by formulas with as little as, say, 60 variables. To wit: A problem represented as a Boolean formula with 10 variables that affords a linear solution taking one hundredth of a second to complete would take just four hundredths and six hundredths of a second to complete if the formula had instead 40 and 60 variables respectively. In dramatic contrast, if the solution to the problem were exponential (say $2^n)$ then the times to complete the job for 10, 40 and 60 variables would be respectively one thousandth of a second, 13 days, and 365 centuries. It is a true testament to the ingenuity of the automated reasoning community and the power of current SAT-based search algorithms that real-world problems with thousands of variables can be handled with reasonable efficency. Küchlin & Sinz 2000 discuss a SAT application in the realm of industrial automotive product data management where 18,000 (elementary) Boolean formulas and 17,000 variables are used to express constraints on orders placed by customers. As another example, Massacci & Marraro 2000 discuss an application in logical cryptanalysis, that is, the verification of properties of cryptographic algorithms expressed as SAT problems. They demonstrate how finding a key with a cryptographic attack is analogous to finding a model—assignment—for a Boolean formula; the formula in their application encodes the commercial version of the U.S Data Encryption Standard (DES) with the encoding requiring 60,000 clauses and 10,000 variables.

Although SAT is conceptually very simple, its inner nature is not well understood—there are no criteria that can be generally applied to answer as to why one SAT problem is harder than another. It should then come as no surprise that algorithms that tend to do well on some SAT instances do not perform so well on others, and efforts are being spent in designing hybrid algorithmic solutions that combine the strength of complementary approaches—see Prasad, Biere & Gupta 2005 for an application of this hybrid approach in the verification of hardware design.

Recent advances in SAT hybrid strategies coupled with supercomputing power has allowed a team of three computing scientists to solve the Boolean Pythagorean Triples Problem, a long-standing open question in Ramsey Theory: Can the set $\{1, 2,...\}$ of natural numbers be divided into two parts with no part containing a triple $(a, b, c)$ such that $a^2 + b^2 = c^2$? Heule, Kullmann & Marek 2016 proved that this cannot be done by showing that the set $\{1, 2, \ldots ,n\}$ can be so partitioned for $n = 7824$ but that this is impossible for $n \ge 7825$. Expressing this deceptively simple question as a SAT problem required close to 38,000 clauses and 13,000 variables with about half of these going to represent that the problem is satisfiable when n $= 7824$ and the other half to represent that it is not when n $= 7825$; of the two, proving the latter was far more challenging since it demanded a proof of unsatisfiability, i.e. that no such partition exists. A naïve brute-force approach considering all $2^{7825}$ possible two-part partitions was clearly out of the question and the problem was attacked by using “clever” algorithms within a multi-stage SAT-based framework for solving hard problems in combinatorics, consisting of five phases: *Encode* (encoding the problem as SAT formulas), *Transform* (optimizing the encoding using clause elimination and symmetry breaking techniques), *Split* (dividing the problem effectively into subproblems using splitting heuristics), *Solve* (searching for satisfying assignments or their lack thereof using fast processing), and *Validate* (validating the results of the earlier phases). Of special importance was the application of **cube-and-conquer**, a hybrid SAT strategy particularly effective for hard combinatorial problems. The strategy combines **look-ahead** with **conflict-driven clause-learning** $(\mathbf{CDCL})$, with the former aiming to construct small binary search trees using global heuristics and the latter aiming to find short refutations using local heuristics.

After splitting the problem into $10^6$ hard subproblems (known as “cubes”), these were handed down to 800 cores working in parallel on a *Stampede* supercomputer which, after 2 days of further splitting and CDCL clause-crunching, settled the question and delivered a 200-terabyte proof validating the work. After deservedly celebrating this significant accomplishment of automated reasoning, and after entertaining all the new applications that the enhanced SAT method would afford (particularly in the areas of hardware and software verification), we should then ask some questions that are of especial importance to mathematicians: Is there a more insightful way to establish this result that would involve more traditional and intellectually satisfying mathematical proof methods? Or, as far as increasing our understanding of a given field (combinatorics in this case), what is the value of settling a question when no human can inspect the proof and hence get no insight from it? Even the team responsible for the result admits that “the proofs of unsatisfiability coming from SAT solvers are, from a human point of view, a giant heap of random information (no direct understanding is involved)”. The conjecture has been settled but we basically have no underlying idea what makes 7825 so special. Perhaps the real value to be drawn from these considerations is that they lead us to think about the deeper question: What is it about the structure of a specific problem that makes it amenable to standard mathematical treatment as opposed to requiring a mindless brute-force approach? While this question is being contemplated, SAT may provide the best line of attack on certain mathematical problems.

The DPLL search procedure has been extended to quantified logic. MACE is a popular program based on the DPLL algorithm that searches for finite models of first-order formulas with equality. As an example (McCune 2001)[^mccune-2001], to show that not all groups are commutative one can direct MACE to look for a model of the group axioms that also falsifies the commutation law or, equivalently, to look for a model of:

$$\begin{align} \tag{G1} &e\cdot x = x &\text{(left identity)} \\ \tag{G2} & i(x)\cdot x = e &\text{(left inverse)} \\ \tag{G3} & x(\cdot y)\cdot z = x \cdot(y \cdot z) &\text{(associativity)}\\ \tag{DC} & a\cdot b \neq b\cdot a & \text{(denial of commutativity)} \end{align}$$

MACE finds a six-element model of these axioms, where $\cdot$ is defined as:

| $\cdot$ | 0 | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 1 | 2 | 3 | 4 | 5 |
| 1 | 1 | 0 | 4 | 5 | 2 | 3 |
| 2 | 2 | 3 | 0 | 1 | 5 | 4 |
| 3 | 3 | 2 | 5 | 4 | 0 | 1 |
| 4 | 4 | 5 | 1 | 0 | 3 | 2 |
| 5 | 5 | 4 | 3 | 2 | 1 | 0 |

and where $i$ are defined as:

| $x$ | 0 | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- | --- |
| $i(x)$ | 0 | 1 | 2 | 3 | 4 | 5 |

This example also illustrates, once again, the benefits of using an automated deduction system: How long would have taken the human researcher to come up with the above or a similar model? For more challenging problems, the program is being used as a practical complement to the resolution-based theorem prover Prover9 (formerly Otter), with Prover9 searching for proofs and MACE jointly looking for (counter) models. To find such models, MACE converts the first-order problem into a set of "flattened" clauses which, for increasing model sizes, are instantiated into propositional clauses and solved as a SAT problem. The method has been implemented in other automated reasoning systems as well, most notably in the Paradox model finder where the MACE-style approach has been enhanced by four additional techniques resulting in some significant efficiency improvements (Claessen & Sörensson 2003)[^claessen-2003]: term definitions (to reduce the number of variables in flattened clauses), static symmetric reduction (to reduce the number of isomorphic models), sort inference (to apply symmetric reduction at a finer level) and incremental SAT (to reuse search information between consecutive model sizes). The strategy of pairing the complementary capabilities of separate automated reasoning systems has been applied to higher-order logic too as exemplified by Nitpick, a counterexample generator for Isabelle/HOL (Blanchette & Nipkow 2010)[^blanchette-2010]. Brown 2013 describes a theorem proving procedure for higher-order logic that uses SAT-solving to do most of the work; the procedure is a complete, cut-free, ground refutation calculus that incorporates restrictions on instantiations and has been implemented in the Satallax theorem prover (Brown 2012)[^brown-2012].

An approach of great interest at solving SAT problems in first-order logic is **Satisfiability Modulo Theory** $(\mathbf{SMT})$ where the interpretation of symbols in the problem’s formulation is constrained by a **background theory**. For example, in linear arithmetic the function symbols are restricted to + and $-$. As another example, in the extensional theory of arrays (McCarthy 1962)[^mccarthy-1962] the array function *read*$(a, i)$ returns the value of the array $a$ at index $i$, and *write*$(a, i, x)$ returns the array identical to $a$ but where the value of $a$ at $i$ is $x$. More formally,

**(read-write axiom 1)**

$\forall a : \textit{Array} . \forall i,j : \textit{Index} . \forall x : \textit{Value} . i = j\ \rightarrow $ $\textit{read}(write(a, i, x), j) = x$

**(read-write axiom 2)**

$\forall a : \textit{Array} . \forall i,j : \textit{Index} . \forall x : Value . i \ne j\ \rightarrow$ $\textit{read}(\textit{write}(a, i, x), j) = \textit{read}(a, j)$

**(extensionality)**

$\forall a,b : \textit{Array} . \forall i : \textit{Index} . a = b\ \rightarrow$ $\textit{read}(a, i) = \textit{read}(b, i)$

In the context of these axioms, an SMT solver would attempt to establish the satisfiability (or, dually, the validity) of a given first-order formula, or thousands of formulas for that matter, such as

$$i - j = 1 \amp f(\textit{read}(\textit{write}(a, i, 2), j + 1) = \textit{read}(\textit{write}(a, i, f(i - j + 1)), i)$$

(Ganzinger *et al*. 2004)[^ganzinger-2004] discusses an approach to SMT called $\mathbf{DPLL}(\mathbf{T})$ consisting of a general DPLL(X) engine that works in conjunction with a solver *Solver$_T$* for background theory $T$. Bofill *et al*. (2008) present the approach in the setting of the theory of arrays, where the DPLL engine is responsible for enumerating propositional models for the given formula whereas *Solver$_T$* checks whether these models are consistent with the theory of arrays. Their approach is sound and complete, and can be smoothly extended to multidimensional arrays.

SMT is particularly successful in verification applications, most notably software verification. Having improved the efficiency of SAT solvers with SMT, the effort is now on designing more efficient SMT solvers (de Moura 2007)[^moura-2007]. There is also the need to conduct a comprehensive comparison and potential consolidation of the techniques offered by the different SMT-based verification approaches, including bounded model checking, k-induction, predicate abstraction, and lazy abstraction with interpolants (Beyer, Dangl & Wendler 2018 and 2021)[^beyer-2018][^beyer-2021].

### 4.3 Deductive Computer Algebra

To prove automatically even the simplest mathematical facts requires a significant amount of domain knowledge. As a rule, automated theorem provers lack such rich knowledge and attempt to construct proofs from first principles by the application of elementary deduction rules. This approach results in very lengthy proofs (assuming a proof is found) with each step being justified at a most basic logical level. Larger inference steps and a significant improvement in mathematical reasoning capability can be obtained, however, by having a theorem prover interact with a computer algebra system, also known as a symbolic computation system. A **computer algebra system** is a computer program that assists the user with the symbolic manipulation and numeric evaluation of mathematical expressions. For example, when asked to compute the improper integral

$$\int_0^\infty e^{-a^2 t^2}\cos(2bt)\,dt$$

a competent computer algebra system would quickly reply with the answer

$$\frac{\sqrt{\pi}}{2a}{e^{-b^2/a^2}}$$

Essentially, the computer algebra system operates by taking the input expression entered by the user and successively applies to it a series of transformation rules until the result no longer changes (see the section on Term Rewriting for more details). These transformation rules encode a significant amount of domain (mathematical) knowledge making symbolic systems powerful tools in the hands of applied mathematicians, scientists, and engineers trying to attack problems in a wide variety of fields ranging from calculus and the solving of equations to combinatorics and number theory.

Problem solving in mathematics involves the interplay of deduction and calculation, with decision procedures being a reminder of the fuzzy division between the two; hence, the integration of deductive and symbolic systems, which we coin here as **Deductive Computer Algebra (DCA)**, is bound to be a fruitful combination. Analytica (Bauer, Clarke & Zhao 1998)[^bauer-1998] is a theorem prover built on top of Mathematica, a powerful and popular computer algebra system. Besides supplying the deductive engine, Analytica also extends Mathematica’s capabilities by defining a number of rewrite rules—more precisely, identities about summations and inequalities—that are missing in the system, as well as providing an implementation of Gosper’s algorithm for finding closed forms of indefinite hypergeometric summations. Equipped with this extended knowledge, Analytica can prove semi-automatically some nontrivial theorems from real analysis, including a series of lemmas directly leading to a proof of the Bernstein Approximation Theorem. Here is the statement of the theorem simply to give the reader a sense of the level of the mathematical richness we are dealing with:

> **Bernstein Approximation Theorem**.
> Let $\text{I} = [0, 1]$ be the closed unit interval, $f$ a real continuous function on I, and $B_n (x,f)$ the *nth* Bernstein polynomial for $f$ defined as $$B_n(x, f)= \sum_{k=0}^n \binom{n}{k} f(k/n)x^k(1-x)^{n-k}$$ Then, on the interval I, the sequence of Bernstein polynomials for $f$ converges uniformly to $f$.

To be frank, the program is supplied with key information to establish the lemmas that lead to this theorem but the amount and type of deductive work done by the program is certainly nontrivial. (Clarke & Zhao 1994)[^clarke-1994] provides examples of fully automated proofs using problems in Chapter 2 of *Ramanujan’s Notebooks* (Berndt 1985)[^berndt-1985] including the following example that the reader is invited to try. Show that:

$$\sum_{k=n+1}^{A_r}\frac{1}{k}=r+2\left(\sum_{k=1}^r (r-k)(\sum_{j=A_{k-1}+1}^{a_k} \frac{1}{(3j)^3 -3j})\right) + 2r\phi(3, A_0)$$

where $A_0 =1$, $A_{n+1}=3A_n +1$ and $\phi(x,n)$ is Ramanujan’s abbreviation for

$$ \phi(x, n)=_{df} \sum_{K_1}^n \frac{1}{-(kx)+ k^3x^3}$$

Analytica’s proof of this identity proceeds by simplifying both the left- and right-hand sides of the equality and showing that both sides reduce to the same expression, $-H_n +$ $H_{A_r}$. The simplification uses the added summation identities mentioned before as well as some elementary properties of the harmonic numbers,

$$ H_n=\sum_{k=1}^n\frac{1}{k} $$

The resulting proof has 28 steps (some of which are nontrivial) taking about 2 minutes to find.

Kerber, Kohlhase & Sorge 1998 use the $\Omega$mega planning system as the overall way to integrate theorem proving and symbolic computation. In Harrison & Théry 1998, we find an example of the integration of a higher-order logic theorem proving system (HOL) with a computer algebra system (Maple).

Their great power notwithstanding, symbolic algebra systems do not enforce the same level of rigor and formality that is the essence of automated deduction systems. In fact, the mathematical semantics of some of the knowledge rules in most algebra systems is not entirely clear and are, in cases, logically unsound (Harrison & Théry 1998)[^harrison-1998]. The main reason for this is an over-aggressiveness to provide the user with an answer in a timely fashion at whatever cost, bypassing the checking of required assumptions even if it means sacrificing the soundness of the calculation. (This is strongly reminiscent of most Prolog implementations that bypass the so-called “occurs-check” also abandoning logical soundness in the name of efficiency.) This serious problem opens the opportunity for a deduction system to provide a service to the computer algebra system: Use its deductive capabilities to verify that the computer algebra’s computational steps meet the required assumptions. There is a catch in this, however: For sufficiently large calculation steps, verifying is tantamount to proving and, to check these steps, the deduction system may well need the assistance of the very same system that is in need of verification! The solution to the soundness problem may then well require an extensive modification of the chosen symbolic algebra system to make it sound; an alternative approach is to develop a new system, entirely from scratch, in conjunction with the development of the automated theorem prover. In either case, the resulting combined deductive computer algebra system should display a much improved ability for automated mathematical reasoning.

### 4.4 Formal Verification of Hardware

Automated reasoning has reached the level of maturity where theorem proving systems and techniques are being used for industrial-strength applications. One such application area is the formal verification of hardware and software systems. The cost of defects in hardware can easily run into the millions. In 1994, the Pentium processor was shipped with a defect in its floating-point unit and the subsequent offer by Intel to replace the flawed chip (which was taken up only by a small fraction of all Pentium owners) cost the company close to \$500 million. To guard against situations like this, the practice of testing chip designs is now considered insufficient and more formal methods of verification have not only gained large attention in the microprocessor industry but have become a necessity. The idea behind formal verification is to rigorously prove with mathematical certainty that the system functions as specified. Common applications to hardware design include formally establish that the system functions correctly on all inputs, or that two different circuits are functionally equivalent.

Depending on the task at hand, one can draw from a number of automated formal verification techniques, including SAT solvers in propositional logic, symbolic simulation using binary decision diagrams (BDDs), model checking in temporal logic, or conducting proofs in higher-order logic. In the latter case, using an automated theorem prover like HOL—see Section 3.1—has shown to be invaluable in practice. Proof construction in a system like HOL proceeds semi-automatically with the user providing a fair amount of guidance as to how the proof should proceed: The user tries to find a proof while being assisted by the theorem prover which, on request, can either automatically fill in a proof segment or verify proof steps given to it. Although some of the techniques mentioned above provide decision procedures which higher-order logic lacks, higher-order logic has the advantage of being very expressive. The tradeoff is justified since proving facts about **floating-point arithmetic** requires the formalization of a large body of real analysis, including many elementary statements such as:

| \|- | (!x. a <= x /\\ x <= b ==> (f diffl (f' x)) x) /\\ |
| --- | --- |
|   | f(a) <= K /\\ |
|   | f(b) <= K /\\ |
|   | (!x. a <= x /\\ x <= b /\\ (f'(x) = 0) ==> f(x) <= K) ==> |
|   | (!x. a <= x /\\ x <= b ==> f(x) <= K) |

This statement from Harrison 2000 written in HOL says that if a function $f$ is differentiable with derivative $f'$ in an interval $[a, b]$ then a sufficient condition for $f(x) \le K$ throughout the interval is that $f(x) \le K$ at the endpoints $a, b$ and at all points of zero derivative. The result is used to determine error bounds when approximating transcendental functions by truncated power series. Conducting proofs in such a “painstakingly foundational system” (Harrison 2006)[^harrison-2006] has some significant benefits. First, one achieves a high degree of assurance that the proofs are valid since (admitedly lengthy) they are composed of small error-free deductive steps. Second, the formalization of these elementary statements and intermediate results can be reused in other tasks or projects. For example, a library of formal statements and proven results in floating-point division can be reused when proving other results of floating-point algorithms for square roots or transcendental functions. To further illustrate, different versions of the square root algorithm for the Intel Itanium share many similarities and the proof of correctness for one version of the algorithm can be carried over to another version after minor tweaking of the proof. A third benefit of using a prover like HOL is, of course, that such lengthy proofs are carried out mechanically and are deductively certain; the likelihood of introducing a human error if they were carried out manually would be just as certain.

Formal verification frameworks have become an indispensable part of the microprocessor design process, as exemplified by the use of the ACL2 theorem prover at Centaur Technology (Hunt, Kaufmann, Moore and Slobodova 2017)[^hunt-2017]. ACL2 is used as an integrated programming and proof environment in the formal specification of microprocessors, formal models of hardware design and their associated proofs, and to support the design of other formal analysis tools. Uses of ACL2 to prove group-theoretic properties of elliptic curves (Russinoff 2017)[^russinoff-2017] echo the aforementioned work of Harrison 2000 within abstract mathematical domains in order to serve the needs of wordly microprocessor design.

### 4.5 Formal Verification of Software

Society is becoming increasingly dependent on software systems for critical services such as safety and security. Serious adverse effects of malfunctioning software include loss of human life, threats to security, unauthorized access to sensitive information, large financial losses, denial of critical services, and risk to safety. One way to increase the quality of critical software is to supplement traditional methods of testing and validation with techniques of formal verification. The basic approach to formal verification is to generate a number of conditions that the software must meet and to verify—establish—them by mathematical proof. As with hardware, automated formal verification (simply formal verification, hereafter) is concerned with discharging these proof obligations using an automated theorem prover.

The formal verification of **security protocols** is an almost ideal application of automated theorem proving in industry. Security protocols are small distributed programs aimed at ensuring that transactions take place securely over public networks. The specification of a security protocol is relatively small and well defined but its verification is certainly non-trivial. We have already mentioned in a previous section the use of SAT-based theorem provers in the verification of the U.S Data Encryption Standard (DES). As another example, the Mondex “electronic purse” is a smart card electronic cash system that was originally developed by National Westminster Bank and subsequently sold to MasterCard International. Schmitt & Tonin 2007 describe a Java Card implementation of the Mondex protocol for which the security properties were reformulated in the Java Modeling Language (JML) following closely the original Z specification. Proof of correctness was conducted using the KeY tool (Beckert, Hanle & Schmitt 2007)[^beckert-2007][^schmitt-2007], an interactive theorem proving environment for first-order dynamic logic that allows the user to prove properties of imperative and object-oriented sequential programs. This application of automated reasoning demonstrates, in the words of the authors, that “it is possible to bridge the gap between specification and implementation ensuring a fully verified result”.

Denney, Fischer & Schumann 2004 describe a system to automate the certification of safety properties of data-analysis **aerospace software** at NASA. Using Hoare-style program verification techniques, their system generates proof obligations that are then handled by an automated theorem prover. The process is not fully automated, however, since many of the obligations must be simplified first in order to improve the ability of the theorem prover to solve the proof tasks. For example, one such class of obligations makes a statement about a matrix, $r$, that needs to remain symmetric after updates along its diagonal have been made, and has the form:

**Original form**: $\textit{symm}(r) \rightarrow\textit{symm}(\textit{diag-updates}(r))$

**Simplified form** (when $r$ is 2x2):

| $(\forall i)(\forall j)(0 \le i, j \le 1 \rightarrow \textit{sel}(r, i, j) = \textit{sel}(r, j, i)) \rightarrow$ |
| --- |
| $(\forall k)(\forall l)(0 \le k, l \le 1 \rightarrow$ |
| $\textit{sel}(\textit{upd}(\textit{upd}(r, 1, 1, r_{11}), 0, 0, r_{00}), k, l) = \textit{sel}(\textit{upd}(\textit{upd}(r, 1, 1, r_{11}), 0, 0, r_{00}), l, k)))$ |

Even after the simplification, current theorem provers find the proof task challenging. The task becomes intractable for larger matrices and number of updates (e.g. a $6\times 6$ matrix with 36 updates) and further preprocessing and simplification on the obligation is required before the task eventually falls within the reach of state-of-art theorem provers. But it is worth remarking that proofs are found without using any specific features or configuration parameters of the theorem provers which would improve their chances at completing the proofs. This is important since the everyday application of theorem provers in industry cannot presuppose such deep knowledge of the prover from their users. The formal verification of software remains a demanding task but it is difficult to see how the certification of properties could happen without the assistance of automated deduction when one faces the humanly impossible task of establishing thousands of such obligations.

In the field of **nuclear engineering**, techniques of automated reasoning are deemed mature enough to assist in the formal verification of the safety-critical software responsible for controlling a nuclear power plant’s reactor prevention systems (RPS). The RPS component of the digital control system of the APR-1400 nuclear reactor is specified using NuSCR, a formal specification language customized for nuclear applications (Yoo, Jee & Cha 2009)[^yoo-2009]. Model checking in computation tree logic is used to check the specifications for completeness and consistency. After this, nuclear engineers generate function block designs via a process of automatic synthesis and formally verify the designs also using techniques of model checking in linear temporal logic; the techniques are also used to verify the equivalence of the multiple revisions and releases of the design. These model-checking tools were implemented to make their use as easy and intuitive as possible, in a way that did not require a deep knowledge of the techniques, and used notations familiar to nuclear engineers. The use of automated reasoning tools not only helps the design engineers to establish the desired results but it also raises the confidence of the government’s regulatory personnel that need to approve the RPS software before the reactor can be certified for operation.

**Quantum computing** is an emerging field at the intersection of physics and computer science. The field is expected to bring very significant practical applications and, given the nature of the quantum world, we can rest assured there will be no shortage of philosophical implications. These applications require a firm foundation, including the formalization and verification of quantum algorithms and results in quantum information theory. Aiming to this worthwhile objective, a number of results have already been formalized in Isabelle/HOL and added to its library so they can be made available for further work. After formalizing a number of concepts in quantum computing such as qubits, quantum states, quantum gates, entanglement, measurement, matrix representation of quantum circuits, and others, the work proceeds to the formalization of theorems and algorithms (Bordg, Lachnitt & He 2021)[^bordg-2021], including:

- the no-clone theorem, which states that it is impossible to make an exact copy of an unknown quantum state (Wooters & Zurek 1982, Dieks 1982)[^dieks-1982][^wooters-1982];
- the quantum teleportation protocol, whose formalization had been done previously in the Coq system (Boender, Kammüller & Nagarajan 2015)[^boender-2015] but now it is part of Isabelle’s library as well; the protocol allows the transmission of an unknown quantum state in the absence of a quantum channel using only an entangled pair and a classical channel;
- the verification of Deutsch’s algorithm and its generalized version, the Deutsch-Jozsa’s algorithm (Deutsch 1985). Deutsch was the first to demonstrate that a quantum computer could perform a task faster than any von-Neumann—classical—computer; and,
- a number of results in quantum game theory such as the quantum prisoner’s dilemma, i.e. the quantum version of the classical dilemma, and the unfair quantum prisoner’s dilemma, where one of the prisoners abides by the laws of classical physics while the other has the quantum advantage (Eisert, Wilkens & Lewenstein 1999)[^eisert-1999].

Of notable mention is the fact that the formalization of the unfair quantum prisoner’s dilemma into Isabelle/HOL uncovered a flaw in the original “paper-and-pencil” publication and which had gone undetected for many years. Under the more formal and strict framework that Isabelle/HOL demands, the so-called quantum “miracle move” (as defined in Eisert, Wilkens & Lewenstein 1999)[^eisert-1999] was found to be of no advantage over a classical strategy. This error has now been rectified (Eisert, Wilkens & Lewenstein 2020)[^eisert-2020] thus re-establishing the advantage of a quantum strategy . Further use of Isabelle/HOL in quantum computing includes the verification of quantum cryptographic protocols and the addition to Isabelle’s library the formalization of the quantum Fourier transform which will pave the way for more advanced quantum algorithms.

### 4.6 Logic and Philosophy

In the spirit of Wos, Overbeek, Lusk & Boyle 1992, we pose the question: What do the following statements about different systems of formal logic and exact philosophy have in common?

- The implicational fragments of the modal logics S4 and S5 have been studied extensively over the years. Posed as an open question, it was eventually shown that there is a single axiom for implicational S4 as well as several new shortest axioms for implicational S5 (Ernst, Fitelson, Harris & Wos 2002)[^ernst-2002][^wos-2002].
- The $L$ combinator is defined as $(Lx)y = x(yy)$. Although it was known that the $L$-based combinator $E_{12} = ((L(LL))(L(LL)))((L(LL))(L(LL)))$ satisfies $E_{12}E_{12} = E_{12}$ the question remained whether a shorter $L$-based combinator satisfying this property existed. (Glickfeld & Overbeek 1986) showed this to be the case with $E_8 = ((LL)(L(LL)))(L(LL))$.
- Thirteen shortest single axioms of length eleven for classical equivalence had been discovered, and $XCB= e(x, e(e(e(x, y), e(z, y)), z))$ was the only remaining formula of that length whose status was undetermined—was it an axiom? For a quarter of a century this question remained open despite intense study by various researchers. It was finally settled that $XCB$ is indeed such a single axiom, thus ending the search for shortest single axioms for the equivalential calculus (Wos, Ulrich & Fitelson 2002)[^wos-2002].
- Saint Anselm of Canterbury offered in his *Proslogium* a famous argument for the existence of God. But, quite recently, a simpler proof has been discovered in the sense that it is shorter and uses fewer assumptions (Oppenheimer & Zalta 2011)[^oppenheimer-2011]. In the same tradition, Gödel produced a proof of God’s existence but (Benzmüller & Paleo 2014)[^benzmüller-2014] have recently proved the same result using a weaker logic system while simultaneously addressing a major criticism of Gödel’s proof.
- In the axioms defining a Robbins algebra, the Huntington’s equation $-(-(x + y) + -(x + -y)) = x$ can be replaced by a simpler one, namely the Robbins equation $-(-x + y) + -(-x + -y) = x$. This conjecture went unproved for more than 50 years resisting the attacks of many logicians including Tarski until it was eventually proved in (McCune 1997)[^mccune-1997].

We ask again, what do these results have in common? The answer is that each has been proved with the help of an automated reasoning program. Having disclosed the answer to this question prompts a new one: How much longer would have taken to settle these open problems without the application of such an automated reasoning tool?

#### Modal logic

The strict implicational fragments of the logical systems S4 and S5 of **modal logic** are known as C4 and C5, respectively, and their Hilbert-style axiomatizations presuppose condensed detachment as their sole rule of inference. With insight from Kripke’s work, Anderson & Belnap (1962) published the first axiomatization of C4 using the following 3-axiom basis, where the Polish notation ‘*Cpq*’ stands for ‘$p \rightarrow q$’.

**(1)**

$Cpp \quad CCpqCrCpq \quad CCpCqrCCpqCpr$

A question was posed sometime after: Is there a shorter such axiomatization for C4, using a 2-axiom basis or even a single axiom? Using the automated reasoning program Otter, the authors Ernst, Fitelson, Harris & Wos (2001)[^wos-2001] settled both questions in the affirmative. In fact, several 2-axiom bases were discovered of which the following turned out to be shortest:

**(2)**

$CpCqq \quad CCPCqrCCpqCsCpr $

Further rounds of automated reasoning work were rewarded with the discovery of a single axiom for C4; the axiom is 21 symbols long and it was also proved that it is the shortest such axiom:

**(3)**

$CCpCCqCrrCpsCCstCuCpt$

To show that each of (2) and (3) is necessary and sufficient for (1), a circle of proofs was produced using the automated reasoning tool: (1) $\Rightarrow$ (3) $\Rightarrow$ (2) $\Rightarrow$ (1). As for C5, its axiomatization was originally published in a paper by Lemmon, A. Meredith, D. Meredith, Prior & Thomas (1957) giving several 4-, 3-, 2- and 1-axiom bases for C5, including the following 3-axiom basis:

**(4)**

$CqCpp \quad CCpqCCqrCpr \quad CCCCpqrCpqCpq$

The publication also included the shortest known 2-axiom bases for C5 (actually two of them, containing 20 symbols each) but the shortest single axiom for C5 was later discovered by (Meredith and Prior 1964)[^meredith-1964] and having 21 symbols:

**(5)**

$CCCCCppqrCstCCtqCsCsq$

Applying automated reasoning strategies again, Ernst, Fitelson, Harris & Wos 2001) discovered several new bases, including the following 2-axiom basis of length 18 and six 1-axiom bases matching Meredith’s length of 21 (only one of these is given below):

**(6)**

$Cpp \quad CCpqCCCCqrsrCpr$

**(7)**

$CCCCpqrCCuuqCCqtCsCpt$

To show that each of (6) and (7) is necessary and sufficient for (4), a circle of proofs was also produced with the theorem prover: (6) $\Rightarrow$ (4) $\Rightarrow$ (7) $\Rightarrow$ (6).

#### Combinatory logic

A charming foray into **combinatory logic** is presented in Smullyan 1985 and Glickfeld & Overbeek 1986, where we learn about a certain enchanted forest inhabited by talking birds. Given any birds $A$ and $B$, if the name of bird $B$ is spoken to bird $A$ then $A$ will respond with the name of some bird in the forest, $AB$, and this response to $B$ from $A$ will always be the same. Here are some definitions about enchanted birds:

**$\mathbf{B1}$**

A *mockingbird* $M$ *mimics* any bird in the sense that $M$’s response to a bird $x$ is the same as $x$’s response to itself, $Mx = xx$.

**$\mathbf{B2}$**

A bird $C$ *composes* birds $A$ and $B$ if $A(Bx) = Cx$, for any bird $x$. In other words, $C$’s response to $x$ is the same as $A$’s response to $B$’s response to $x$.

**$\mathbf{B3}$**

A bird $A$ is fond of a bird $B$ if $A$’s response to $B$ is $B$; that is, $AB = B$.

And here are two facts about this enchanted forest:

**$\mathbf{F1}$**

For any birds $A$ and $B$ in the forest there is a bird $C$ that composes them.

**$\mathbf{F2}$**

There is a mockingbird in the forest.

There have been rumors that every bird in the forest is fond of at least one bird, and also that there is at least one bird that is not fond of any bird. The challenge to the reader now is, of course, to settle these rumors using only F1 and F2, and the given definitions (B1)–(B3). Glickfeld & Overbeek 1986 do this in mere seconds with an automated reasoning system using paramodulation, demodulation and subsumption. For a more challenging problem, consider the additional definitions:

**$\mathbf{B4}$**

A bird is egocentric if it is fond of itself: $EE = E$.

**$\mathbf{B5}$**

A bird $L$ is a lark if for any birds $x$ and $y$ the following holds: $(Lx)y = x(yy)$.

Smullyan challenges us to prove a most surprising thing about larks: Suppose we are not given any other information except that the forest contains a lark. Then, show that at least one bird in the forest must be egocentric! Below we give the salient steps in the proof found by the automated reasoning system, where ‘$S(x, y)$’ stands for ‘$xy$’ and where clauses (2) and (3) are, respectively, the definition of a lark and the denial of the theorem; numbers on the right are applications of paramodulation:

> | 1 | (x1 = x1) |   |
> | --- | --- | --- |
> | 2 | (S(S(L, x1), x2) = S(x1, S(x2, x2))) |   |
> | 3 | -(S(x1, x1) = x1) |   |
> | 6 | (S(x1, S(S(L, S(x2, x2)), x2)) = S(S(L, x1), S(x2, x2))) | 2 2 |
> | 8 | (S(x1, S(S(x2, x2), S(x2, x2))) = S(S(L, S(L, x1)), x2)) | 2 2 |
> | 9 | (S(S(S(L, L), x1), x2) = S(S(x1, x1), S(x2, x2))) | 2 2 |
> | 18 | -(S(S(L, S(S(L, S(L, L)), x1)), x1) = S(S(L, S(x1,x1)), x1)) | 6 3 6 9 8 8 |
> | 19 | [] | 18 1 |

Closer inspection of the left and right hand sides of (18) under the application of unification revealed the discovery of a $10-L$ bird, i.e. a 10-symbol bird expressed solely in terms of larks, which was a strong candidate for egocentricity. This discovery was exciting because the shortest egocentric $L$-bird known to Smullyan was of length 12. A subsequent run of the automated reasoning system produced a proof of this fact as well as another new significant bird: A possible egocentric $8-L$ bird! A few more runs of the system eventually produced a 22-line proof (with terms with as many as 50 symbols, excluding commas and parentheses) of the fact that $((LL)(L(LL)))(L(LL))$ is indeed egocentric. The natural questions to ask next are, of course, whether there are other $8-L$ egocentric birds and whether there are shorter ones. The reader may want to attempt this with paper and pencil but, given that there are 429 such birds, it may be wiser to try it instead (or in conjunction) with an automated reasoning program; both approaches are explored in Glickfeld & Overbeek 1986. For a more formal, but admittedly less colorful, introduction to combinatory logic and lambda-conversion the reader is referred to Hindley & Seldin 1986.

#### Equivalential calculus

Formulas in the classical **equivalential calculus** are written using sentential variables and a two-place function symbol, $e$, for equivalence. The calculus has two rules of inference, detachment (modus ponens) and substitution; the rules can be combined into the single rule of condensed detachment: Obtain $t\theta$ from $e(s,t)$ and $r$ where $s\theta = r\theta$ with mgu *θ*. The calculus can be axiomatized with the formulas:

$$\begin{align} \tag{E1}& e(x, x) &\text{(reflexivity)}\\ \tag{E2}& e(e(x, y), e(y, x)) & \text{(symmetry)}\\ \tag{E3}& e(e(x, y), e(e(y, z), e(x, z))) & \text{(transitivity)} \end{align}$$

We can dispense with reflexivity since it is derivable from the other two formulas. This brings the number of axioms down to two and a natural question to ask is whether there is a single axiom for the equivalential calculus. In 1933, Łukasiewicz found three formulas of length eleven that each could act as a single axiom for the calculus—here’s one of them: $e(e(x,y),e(e(z,y),e(x,z)))$—and he also showed that no shorter single axiom existed. Over time, other single axioms also of length eleven were found and the list kept growing with additions by Meredith, Kalman and Peterson to a total of 14 formulas of which 13 were known to be single axioms and one formula with a yet undetermined status: the formula $XCB= e(x, e(e(e(x, y), e(z, y)), z))$. (Actually, the list grew to 18 formulas but Wos, Winker, Veroff, Smith & Henschen 1983 reduced it to 14.)[^wos-1983] Resisting the intense study of various researchers, it remained as an open question for many years whether the 14th formula, $XCB$, was a single axiom for the equivalential calculus (Peterson 1977)[^peterson-1977]. One way to answer the question in the affirmative would be to show that at least one of the 13 known single axioms is derivable from $XCB$ alone; another approach would be to derive from $XCB$ the 3-axiom set (E1)–(E3). While Wos, Ulrich & Fitelson 2002 take shots at the former, their line of attack concentrates on the latter with the most challenging task being the proving of symmetry. Working with the assistance of a powerful automated reasoning program, Otter, they conducted a concerted, persistent and very aggressive assault on the open question. (Their article sometimes reads like a military briefing from the front lines!) For simpler problems, proofs can be found by the reasoning program automatically; deeper and more challenging ones like the one at hand require the guidance of the user. The relentless application of the reasoning tool involved much guidance in the setting of lemmas as targets and the deployment of an arsenal of strategies, including the set of support, forward and backward subsumption, lemma adjunction, formula complexity, hints strategy, ratio strategy, term avoidance, level saturation, and others. After much effort and CPU time, the open question finally succumbed to the combined effort of man and machine and a 61-step proof of symmetry was found, followed by one for transitivity after 10 more applications of condensed detachment. Subsequent runs of the theorem prover using demodulation blocking and the so-called cramming strategy delivered shorter proofs. Here are the last lines of their 25-step proof which in this case proves transitivity first followed by symmetry:

| 123 | [hyper,51,106,122] | P(e(e(e(e(x,y),e(z,y)),z),x)). |
| --- | --- | --- |
| 124 | [hyper,51,53,123] | P(e(e(e(e(e(e(e(x,y),e(z,y)), z),x),u),e(v,u)),v)). |
| 125 | [hyper,51,124,123] | P(e(e(e(x,y),x),y)). |
| 127 | [hyper,51,124,108] | P(e(e(e(e(x,e(e(e(x,y),e(z,y)) ,z)),e(e(e(e(e(u,v),e(w,v)),w),u), v6)),v7),e(v6,v7))). |
| 128 | [hyper,51,127,123] | P(e(e(x,y),e(e(y,z),e(x,z)))). |
| 130 | [hyper,51,128,125] | P(e(e(x,y),e(e(e(z,x),z),y))). |
| 131 | [hyper,51,128,130] | P(e(e(e(e(e(x,y),x),z),u), e(e(y,z),u))). |
| 132 | [hyper,51,131,123] | P(e(e(x,y),e(y,x))). |

With an effective methodology and a strategy that included the assistance of an automated reasoning program in a crucial way, the search for shortest single axioms for the equivalent calculus came to an end.

#### Computational metaphysics

Fitelson & Zalta 2007, Oppenheimer & Zalta 2011, and Alama, Oppenheimer, & Zalta 2015 describe several applications of automated reasoning in **computational metaphysics**. By representing formal metaphysical claims as axioms and premises in an automated reasoning environment using programs like Prover9, Mace4, the E-prover system and Paradox, the logical status of metaphysical arguments is investigated. After the suitable formalization of axioms and premises, the model finder program Mace4 is used to help verify their consistency. Then, using Prover9, proofs are automatically generated for a number of theorems of the Theory of Plato’s Forms, twenty five fundamental theorems of the Theory of Possible Worlds, the theorems described in Leibniz’s unpublished paper of 1690 and in his modal metaphysics, and a fully automated construction of Saint Anselm’s Ontological Argument. In the latter application, Saint Anselm is understood in Oppenheimer & Zalta 2011 as having found a way of inferring God’s existence from His mere being as opposed to inferring God’s actuality from His mere possibility. This allows for a formalization that is free of modal operators, involving an underlying logic of descriptions, three non-logical premises, and a definition of God. Here are two key definitions in the formalization, as inputted into Prover9, that helped express the concept of God:

> | Definition of none_greater: |
> | --- |
> | all x (Object(x) -> (Ex1(none_greater,x) <-> |
> | (Ex1(conceivable,x) & |
> | -(exists y (Object(y) & Ex2(greater_than,y,x) & |
> | Ex1(conceivable,y)))))). |
> |   |
> | Definition of God: |
> | Is_the(g,none_greater). |

Part of the challenge when representing in Prover9 these and other statements from axiomatic metaphysics was to circumvent some of the prover’s linguistic limitations. For example, Prover9 does not have definite descriptions so statements of this kind as well as second-order concepts had to be expressed in terms of Prover9’s existing first-order logic. But the return is worth the investment since Prover9 not only delivered a proof of Ex1(e,g)—there is one and only one God—but does so with an added bonus. A close inspection of the output provides yet another example of an automated theorem prover "outreasoning" its users, revealing that some of the logical machinery is actually redundant: The proof can be constructed only using two of the logical theorems of the theory of descriptions (called "Theorem 2" and "Theorem 3" in their article), one of the non-logical premises (called "Premise 2"), and the definition of God. We cannot help but to include here Prover9’s shorter proof, written in the more elegant notation of standard logic (from Oppenheimer & Zalta 2011)[^oppenheimer-2011]:

| 1. | ${\sim}E!\iota x\phi_1$ | Assumption, for *Reductio* |
| --- | --- | --- |
| 2. | $\exists y(Gy\iota x\phi_1 \amp Cy)$ | from (1), by Premise 2 and MP |
| 3. | $Gh\iota x\phi_1 \amp Ch$ | from (2), by $\exists$E, ‘$h$’ arbitrary |
| 4. | $Gh\iota x\phi_1$ | from (3), by &E |
| 5. | $\exists y(y = \iota x\phi_1)$ | from (4), by Theory of Descriptions, Theorem 3 |
| 6. | $C\iota x\phi_1 \amp{\sim}\exists y(Gy\iota x\phi_1 \amp Cy)$ | from (5), by Theory of Descriptions, Theorem 2 |
| 7. | ${\sim}\exists y(Gy\iota x\phi_1 \amp Cy)$ | from (6), by &E |
| 8. | $E!\iota x\phi_1$ | from (1), (2), (7), by *Reductio* |
| 9. | $E!g$ | from (8), by the definition of ‘$g$’ |

In the same tradition as St. Anselm’s, Gödel also provided an ontological proof of God’s existence (Gödel 1970, Scott 1972)[^gödel-1970][^scott-1972]. An important difference between the two is Gödel’s use of modal operators to represent metaphysical possibility and necessity and, of course, his use of symbolic logic for added reasoning precision. In his proof, Gödel begins by framing the concept of “positive property” using two axioms, and he introduces a definition stating that “A God-like being possesses all positive properties”. This is enough logical machinery to prove as a theorem the possibility of God’s existence, $\Diamond \exists xG(x)$; three more axioms and two additional definitions allow Gödel to further his proof to establish not only that God exists, $\exists xG(x)$, but that this is so by necessity, $\Box \exists xG(x)$. Gödel’s proof is in the formalism of higher-order modal logic (HOML) using modal operators and quantification over properties. Gödel never published his proof but he shared it with Dana Scott who produced the version presented below, which is taken from (Benzmüller & Paleo 2014)[^benzmüller-2014] along with its English annotation to aid the reader with its intended interpretation:

**Axiom A1**

$\forall \varphi[P({\sim}\varphi) \equiv{\sim}P(\varphi)]$   *Either a property or its negation is positive, but not both*)

**Axiom A2**

$\forall \varphi \forall \psi[(P(\varphi) \wedge \Box \forall x[\varphi(x) \rightarrow \psi(x)]) \supset P(\psi)]$   *A property necessarily implied by a positive property is positive*

**Theorem T1**

$\forall \varphi[P(\varphi) \supset \Diamond \exists x \varphi(x)]$   *Positive properties are possibly exemplified*

**Definition D1**

$G(x) \equiv \forall \varphi[P(\varphi) \supset \varphi(x)]$   *A God-like being possesses all positive properties*

**Axiom A3**

$P(G)$   *The property of being God-like is positive*

**Corollary C**

$\Diamond \exists xG(x)$   *Possibly, God exists*

**Axiom A4**

$\forall \varphi[P(\varphi) \supset \Box P(\varphi)]$   *Positive properties are necessarily positive*

**Definition D2**

$\varphi \ess x \equiv \varphi(x) \wedge \forall \psi(\psi(x) \supset \Box \forall y(\varphi(y) \supset \psi(y)))$   *An essence of an individual is a property possessed by it and   necessarily implying any of its properties*

**Theorem T2**

$\forall x[G(x) \supset G \ess x]$   *Being God-like is an essence of any God-like being*

**Definition D3**

$NE(x) \equiv \forall \varphi [\varphi \ess x \supset \Box \exists y\varphi(y)]$   *Necessary existence of an individual is the necessary    exemplification of all its essences*

**Axiom A5**

$P(NE)$   *Necessary existence is a positive property*

**Theorem T3**

$\Box \exists xG(x)$   *Necessarily, God exists*

The proof has recently been analysed to an unprecedented degree of detail and precision by Benzmüller & Paleo 2014 with the help of automated theorem provers. A major challenge faced by these authors was the lack of a HOML-based theorem prover that could carry out the work but this was circumvented by embedding the logic into the classical higher-order logic (HOL) already offered by existing theorem provers like LEO-II, Satallax and the countermodel finder Nitpick. Details of the syntactic and semantic embedding are given in their paper and it consists of encoding HOML formulas as HOL predicates via mappings, expansions, and $\beta \eta$-conversions. The mapping associates HOML types *α*, terms $s_{\alpha}$, and logical operators *θ* with corresponding HOL “raised” types $\lceil\alpha\rceil$, type-raised terms $\lceil s_{\alpha}\rceil$, and type-raised logical operators $\theta^{\bullet}$. If $\mu$ and $\omicron$ are, respectively, the types of individuals and Booleans then $\lceil\mu\rceil = \mu$ and $\lceil\omicron\rceil = \sigma$ where *σ* is shorthand for $\iota \rightarrow \omicron$ with *ι* as the type of possible worlds; as for function types, $\lceil\beta \rightarrow \gamma\rceil = \lceil\beta\rceil\rightarrow\lceil\gamma\rceil$. For type-raised terms, $\lceil s_\alpha \rceil$ is defined inductively on the structure of $s_\alpha $ as the following example illustrates:

$$\begin{align} \lceil \exists_{(\mu\rightarrow\omicron)\rightarrow\omicron}X_\mu. g_{\mu\rightarrow \omicron}X\rceil & = \lceil \exists_{(\mu\rightarrow \omicron)\rightarrow \omicron}\rceil\lceil X_\mu . g_{\mu\rightarrow \omicron}X\rceil\\ & = \lceil \exists_{(\mu\rightarrow\omicron)\rightarrow\omicron}\rceil\lceil X_\mu\rceil . \lceil g_{\mu\rightarrow \omicron}\rceil\lceil X\rceil\\ & = \exists^{\bullet}_{\lceil (\mu\rightarrow\omicron)\rightarrow\omicron\rceil}X_{\lceil \mu \rceil} . g_{\lceil\mu\rightarrow\omicron\rceil}X\\ & = \exists^{\bullet}_{(\mu\rightarrow \sigma)\rightarrow\sigma}X_\mu. g_{\mu\rightarrow \sigma} X \end{align}$$

Type-raised logical connectives, $\theta^{\bullet}$, are defined below where $r$ is a new constant symbol in HOL associated with the accessibility relation of HOML:

$$\begin{align} \sim^{\bullet}_{\sigma\rightarrow\sigma} & =\lambda s_\sigma \lambda w_\iota\sim(sw)\\ \vee^{\bullet}_{\sigma\rightarrow\sigma\rightarrow\sigma} & = \lambda s_\sigma \lambda t_\sigma \lambda w_\iota(sw\vee tv) \\ \forall^{\bullet}_{(\alpha\rightarrow\sigma)\rightarrow\sigma} & = \lambda s_{\alpha\rightarrow\sigma}\lambda w_\iota \forall x_\alpha sxw \\ \Box^\bullet_{\sigma\rightarrow\sigma} & = \lambda s_\sigma \lambda w_\iota \forall u_\iota . \sim(r_{\iota\rightarrow\iota\rightarrow\omicron} wu)\vee su) \end{align}$$

The other connectives can be defined in the usual way. Validity is expressed as a *λ*-term, $\lambda s_{\iota\rightarrow \omicron}\forall w_\iota sw$, that when applied to a term $s_{\sigma}$ we write as $[s_{\sigma}]$. For example, under the embedding, proving in HOML the possibility of God’s existence, $\Diamond_{\omicron\rightarrow \omicron}\exists_{(\mu \rightarrow \omicron)\rightarrow \omicron} X_{\mu} . g_{\mu \rightarrow\omicron} X$, is tantamount to proving its validity in HOL: $[\Diamond^{\bullet}_{\sigma \rightarrow \sigma}\exists^{\bullet}_{(\mu \rightarrow \sigma)\rightarrow \sigma} X_{\mu} . g_{\mu \rightarrow \sigma} X]_{\mu \rightarrow\omicron }$. To prove so, the type-raised HOL expression $[\Diamond^{\bullet}\exists^{\bullet}X_{\mu} . g_{\mu \rightarrow\sigma } X]$ is then encoded in the so-called THF0 syntax (Sutcliffe & Benzmüller 2010)[^sutcliffe-2010] prior to being fed, along with the above set of equality rules, to the provers that were used in completing the proof:

| thf(corC, conjecture, |
| --- |
| (v |
| @(mdia |
| @(mexists_ind |
| @^[X: mu] : |
| (g @ X)))))). |

The proof in Benzmüller & Paleo 2014 is presented here, including the axioms and definitions as well as the derivation of its four main results—T1, C, T2, T3—all written in the type-decorated type-raised higher-order logic notation resulting from the embedding. The proof steps are not fully expanded—note the presence of type-raised connectives—and the inferential moves are not broken down to lower levels of detail. Borrowing a phrase from Bertrand Russell (Urquhart 1994)[^urquhart-1994], this was done to spare the reader of the “kind of nausea” that the fully detailed automated proof would cause:

| A1 | $[\forall^{\bullet}\varphi_{\mu\rightarrow \sigma} . p_{(\mu \rightarrow \sigma)\rightarrow\sigma} (\lambda X_{\mu} . {\sim}^{\bullet}\varphi$X))$ \equiv^{\bullet} {\sim}^{\bullet}p\varphi]$ | Axiom |
| --- | --- | --- |
| A2 | $[\forall^{\bullet}\varphi_{\mu\rightarrow \sigma} .\forall^{\bullet}\psi_{\mu \rightarrow \sigma} . (p_{(\mu \rightarrow \sigma)\rightarrow\sigma} \varphi\ \wedge^{\bullet}$ $\Box^{\bullet}\forall^{\bullet}X_{\mu}.(\varphi X \supset^{\bullet}\psi X)) \supset^{\bullet}\psi]$ | Axiom |
| T1 | $[\forall^{\bullet}\varphi_{\mu\rightarrow \sigma} . p_{(\mu \rightarrow \sigma)\rightarrow\sigma} \varphi \supset^{\bullet} \Diamond^{\bullet}\exists^{\bullet}X_{\mu}. \varphi X]$ | A1, A2 (in K) |
| D1 | $g_{\mu\rightarrow\sigma} =\lambda X_{\mu} .\forall^{\bullet}\varphi_{\mu\rightarrow\sigma } . p_{(\mu\rightarrow \sigma)\rightarrow\sigma} \varphi \supset^{\bullet}\varphi X$ | Definition |
| A3 | $[p_{(\mu\rightarrow \sigma)\rightarrow \sigma} g_{\mu \rightarrow\sigma}]$ | Axiom |
| C | $[\Diamond^{\bullet}\exists^{\bullet}X_{\mu} . g_{\mu \rightarrow\sigma} X]$ | T1, D1, A3 (in K) |
| A4 | $[\forall^{\bullet}\varphi_{\mu\rightarrow \sigma} . p_{(\mu \rightarrow \sigma)\rightarrow\sigma} \varphi \supset^{\bullet} \Box^{\bullet}p\varphi]$ | Axiom |
| D2 | $\ess_{(\mu\rightarrow \sigma)\rightarrow \mu \rightarrow \sigma} = \lambda \varphi_{\mu \rightarrow\sigma} . \lambda X_{\mu}. \varphi X\ \wedge$ $\forall^{\bullet}\psi_{\mu\rightarrow\sigma}. (\psi X \supset^{\bullet} \Box^{\bullet}\forall^{\bullet}Y_{\mu}. (\varphi Y \supset^{\bullet}\psi Y))$ | Definition |
| T2 | $[\forall^{\bullet}X_{\mu} . g_{\mu \rightarrow\sigma} X \supset^{\bullet}\ess_{(\mu\rightarrow \sigma)\rightarrow \mu \rightarrow\sigma} gX]$ | A1, D1, A4, D2 (in K) |
| D3 | $\text{NE}_{\mu\rightarrow \sigma} = \lambda X_{\mu} .\forall^{\bullet}\varphi_{\mu \rightarrow\sigma}. (\ess \varphi X \supset^{\bullet} \Box^{\bullet}\exists^{\bullet}Y_{\mu}. \varphi Y)$ | Definition |
| A5 | $[p_{(\mu\rightarrow \sigma)\rightarrow\sigma}\text{NE}_{\mu\rightarrow\sigma}]$ | Axiom |
| T3 | $[\Box^{\bullet}\exists X_{\mu} . g_{\mu \rightarrow\sigma} X]$ | D1, C, T2, D3, A5 (in KB) |

Besides helping in the completion of the proof, the automated theorem provers were also very instrumental in the finding of some novel results. First, Gödel’s set of original assumptions was shown to be inconsistent by LEO-II by proving that self-difference becomes an essential property of every entity; a re-formulation of the definition of essence due to Dana Scott—this involved the addition of a missing conjunct, $\varphi X$, in the definition—was shown by Nitpick to be consistent. Second, LEO-II and Satallax managed to prove C, T1 and T2 using only the logic system K and, moreover, Nitpick found a counter-model for T3 in K thus showing that more logical power is required to complete the rest of the proof. Third, using LEO-II and Satallax, it is shown that the logic system KB (system K with the Brouwer axiom) is sufficient to establish the necessity of God’s existence, $\Box^{\bullet}\exists^{\bullet}X_{\mu} . g_{\mu \rightarrow\sigma} X$, which is a double-win for automated reasoning: a gain in logical economy, and the deeper philosophical result of having effectively dismissed a major criticism against Gödel’s proof, namely his use of the stronger logic system S5. Fourth, the authors also prove in KB that:

$$(\forall^{\bullet}\varphi_{\mu\rightarrow\sigma} .\forall^{\bullet}X_{\mu} . (g_{\mu \rightarrow \sigma} X \supset^{\bullet} ({\sim}^{\bullet}(p_{(\mu \rightarrow \sigma)\rightarrow\sigma} \varphi) \supset^{\bullet} {\sim}^{\bullet}(\varphi X)))$$

as well as:

$$\forall^{\bullet}X_{\mu} .\forall^{\bullet}Y_{\mu} . (g_{\mu \rightarrow \sigma} X \supset^{\bullet} (g_{\mu \rightarrow\sigma} Y \supset^{\bullet} X =^{\bullet} Y)),$$

that is, that God is flawless and that monotheism holds, respectively. At this point, it would be fair to say that any of these results would be enough to vindicate the application of automated reasoning in exact philosophy. Now, for the bad news followed by good news: Fifth, the formula $s_{\sigma} \supset^{\bullet} \Box^{\bullet}s_{\sigma}$ can also be formally derived which is unfortunate since it implies that there are no contingent truths and that everything is determined, i.e. there is no free will. However, the issue has been addressed by follow-up work based on Fitting’s and Anderson’s variants of the ontological argument (Fuenmayor & Benzmüller 2017, Fitting 2002, Anderson 1990)[^anderson-1990][^benzmüller-2017][^fitting-1990][^fitting-2002][^fuenmayor-2017].

**Abstract object theory** (AOT) is a metaphysical theory of abstract objects (Zalta 1983)[^zalta-1983]. Abstract objects are the objects presupposed by scientific theories: numbers, natural laws, properties, states of affairs, possibilities, etc. AOT draws a fundamental distinction between ordinary objects defined as $O!x =_{df} \Diamond E!x$ and abstract objects defined as $A!x =_{df}\lnot\Diamond E!x$. AOT also provides two distinctive modes of predication: exemplification $(Fx$, more generally $Fx_1 ...x_n)$ and encoding $(xF$, ‘$x$ encodes $F$’, and more generally $x_1 ...x_n F)$. AOT adds encoding to 2ⁿᵈ-order S5 quantified modal logic without identity, extended with definite descriptions $\iota x \phi$, lambda expressions $\lambda x_1 ...x_n \phi^*$ (where $\phi^*$ means no encoding of subformulas), and a free logic for complex terms (Zalta 1983, Zalta 1988)[^zalta-1983]. The key axioms of AOT are comprehension for abstract objects, $$\exists x(A!x \amp \forall F(xF \equiv \phi))$$ with no free $x$’s in *φ*, and classical *λ*-conversion, $$[\lambda y_1 ...y_n \phi^*]x_1 ...x_n \equiv \phi^* (x_1 /y_1,..., x_n /y_n)$$ with no descriptions in $\phi^*$. These imply comprehension for relations, $$\exists F^n \Box \forall x_1 ...x_n (F^n x_1 ...x_n \equiv \phi^*)$$ with no descriptions in $\phi^*$. Other principles include $$\begin{align} O!x &\rightarrow \Box \lnot\exists FxF\\ \Diamond xF &\rightarrow \Box xF\\ O!x \amp O!y & \rightarrow(x = y \rightarrow \Box \forall F(Fx \equiv Fy))\\ A!x \amp A!y & \rightarrow(x = y \rightarrow \Box \forall F(xF \equiv yF))\end{align}$$ and $\iota x(A!x \amp \forall F(xF \equiv \phi))$ always being well-defined. To give a sense of the expressive power and application of AOT, here are some examples of AOT’s ability to define metaphysical entities as abstract objects and derive interesting results (Zalta 2018)[^zalta-2018]:

> **Plato’s Forms (e.g. triangle)**
> $\Phi_T =_{df}\iota x(A!x \amp \forall F(xF \equiv \Box \forall x(Tx \rightarrow Fx)))$
>
> **Leibniz’s Concepts (e.g. Alexander)**
> $c_a =_{df}\iota x(A!x \amp \forall F(xF \equiv Fa))$
>
> **Frege Numbers**
> $0 =_{df}\iota x(A!x \amp \forall F(xF \equiv\lnot\exists yFy))$
> $1 =_{df}\iota x(A!x \amp \forall F(xF \equiv \exists y(Fy \amp \forall z(Fz \rightarrow z = y))))$
> etc.
>
> **Truth Values**
> $\top =_{df}\iota x(A!x \amp \forall F(xF \equiv \exists p(p \amp F = [\lambda y p])))$
> $\bot =_{df}\iota x(A!x \amp \forall F(xF \equiv \exists p(\lnot p \amp F = [\lambda y p])))$
>
> **Situations and Possible Worlds**
> $\textit{Situation}(x) =_{df} \forall F(xF \rightarrow \exists p(F = [\lambda y p]))$
> $s \vDash p =_{df} s[\lambda y p]$
> $\textit{PossibleWorld}(x) =_{df} \Diamond \forall p((s \vDash p) \equiv p)$, from which one can derive Leibniz’s Principle that $p$ is necessary if true in all worlds, $\vdash \Box p \equiv \forall w(w \vDash p)$, and also Lewis’ Principle that for every way the world might be, there is a world which is that way, $\vdash \Diamond p \equiv \exists w(w \vDash p)$
>
> **Theoretical Mathematical Objects (e.g. null set in ZF)**
> $\varnothing_{ZF} =_{df}\iota x(A!x \amp \forall F(xF \equiv ZF \vDash F\varnothing))$

AOT is under continuous development and for further details of the theory the reader is referred to one of its latest formulations (Zalta 2022)[^zalta-2022]. The computational analysis of AOT was pioneered by Fitelson and Zalta (Fitelson & Zalta 2007)[^fitelson-2007] by using the first-order system Prover9. Conducting computational investigations of a higher-order theory like AOT using a first-order prover has inherent limitations and it would be preferable to work within the computational framework of a higher-order prover. AOT, however, is based on a logical foundation that is significantly different from classical higher-order logic and, ideally, one would want to work with a theorem prover for AOT itself. The downside to this is, of course, that one would need to build such a prover and this is no trivial task. But one can “approximate” such a system to a large extent by building instead a **shallow semantic embedding** (SSE) of AOT into an existing higher-order prover like e.g. Isabelle/HOL where the researcher can faithfully represent AOT’s axioms and deductive system (Benzmüller 2019, Kirchner 2021)[^benzmüller-2019][^kirchner-2021]. In this setting, Isabelle/HOL acts as the metalogical framework for the SSE that provides the “custom” theorem prover for AOT. But there is always a trade-off, and building the embedding brings its own set of challenges. Key among these is that there are aspects of AOT which can be easily formulated in relational type theory but present a challenge when being re-formulated in the underlying functional type theory of Isabelle/HOL. For example, not every formula in AOT can be converted to a *λ*-term unless one is willing to face a contradiction! With some ingenuity, one can use Isabelle/HOL’s functional calculus to define some complex types to help build an Aczel model of AOT, and then interpret those offending *λ*-expressions in terms of the complex types all in the context of a free logic. The bottom line: Every formula of AOT can then be expressed as a *λ*-term but not all these terms denote; hence, consistency is preserved.

Key aspects of the SSE of AOT in Isabelle/HOL include the model construction of the embedding using Aczel models, reproducing the syntax of AOT, extending Isabelle’s “outer” syntax (to deal with certain challenges of reasoning in AOT), representing an abstract semantics of AOT, specifying the logic of the Hilbert *ε* operator, representing the logic of the actuality operator, representing hyperintensionality, deriving the axiom system and deductive system, and other considerations—see Kirchner 2021 for details. Salient among these is the use of **abstraction layers** (Kirchner 2017)[^kirchner-2017] which play an important role in determining the derivability of a statement from the deductive system of the target theory (AOT here). An abstraction layer is constructed by proving that the axioms and deduction rules of AOT are semantically valid in the SSE; after this, all subsequent reasoning (as conducted by e.g. sledgehammer, Isabelle/HOL’s main tool for automated reasoning) is restricted to rely on the derived axioms and deduction rules themselves and may not refer to the underlying semantics. The work took about 25,000 lines of Isabelle/HOL: About 5,000 lines to build the required model structure and semantics as well as the syntax representation of AOT, and the remaining 20,000 for the logic reasoning in AOT. Under the embedding, computational explorations of AOT can be conducted in a more “native” fashion as illustrated below in the 9-line proof in Isabelle/HOL notation that no object is both ordinary and abstract (Kirchner 2021)[^kirchner-2021]:

| 7571 | **AOT_theorem** partition: ❬ ¬∃x (O!x & A!x) ❭ |
| --- | --- |
| 7572 | **proof**(rule "raa-cor:2") |
| 7573 | **AOT_assume** ❬ ∃x (O!x & A!x) ❭ |
| 7574 | then **AOT_obtain** a **where** ❬ O!a & A!a ❭ |
| 7575 | **using** "∃E" [rotated] by blast |
| 7576 | **AOT_thus** ❬ p & ¬p ❭ for p |
| 7577 | **by** (metis "&E"(1) "Conjunction Simplification"(2) "≡E"(1) |
| 7578 | "modus-tollens:1" "oa-contingent:2" "raa-cor:3") |
| 7579 | **qed** |

An additional 1,000 lines of such computational derivations lead to the result that there are distinct abstract objects which cannot be distinguished by exemplification: $\exists x\exists y(A!x \amp A!y \amp x \ne y \amp \forall F(Fx \equiv Fy))$. A few more derivations land a significant novel discovery which provides the analytical means to determine if a *λ*-expression denotes in AOT: $[\lambda x \phi]\downarrow \equiv \Box \forall x\forall y(\forall F(Fx \equiv Fy) \rightarrow(\phi \equiv \phi(y/x))$ with $y$ not free in *φ*. And, as a corollary, $[\lambda x \phi]\downarrow \rightarrow \forall x\forall y(\forall F(Fx \equiv Fy) \rightarrow \Box(\phi \equiv \phi(y/x))$ with $y$ not free in *φ*. The proof of the latter in the context of the SSE takes the 20 lines in Isabelle/HOL given below:

| 8761 | **AOT_theorem** "kirchner-thm-cor:1": |
| --- | --- |
| 8762 | ❬ [λx φ{x}]↓ → ∀x∀y(∀F([F]x ≡ [F]y) → □(φ{x} ≡ φ{y})) ❭ |
| 8763 | **proof**(rule "→I"; rule GEN; rule GEN; rule "→I") |
| 8764 | **fix** x y |
| 8765 | **AOT_assume** ❬ [λx φ{x}]↓ ❭ |
| 8766 | **AOT_hence** ❬ □∀x∀y (∀F ([F]x ≡ [F]y) → (φ{x} ≡ φ{y})) ❭ |
| 8767 | **by** (rule "kirchner-thm:1"[THEN "≡E"(1)]) |
| 8768 | **AOT_hence** ❬ ∀x□∀y (∀F ([F]x ≡ [F]y) → (φ{x} ≡ φ{y})) ❭ |
| 8769 | **using** CBF[THEN "→E"] **by** blast |
| 8770 | **AOT_hence** ❬ □∀y (∀F ([F]x ≡ [F]y) → (φ{x} = φ{y})) ❭ |
| 8771 | **using** "∀E" **by** blast |
| 8772 | **AOT_hence** ❬ ∀y □(∀F ([F]x ≡ [F]y) → (φ{x} ≡ φ{y})) ❭ |
| 8773 | **using** CBF[THEN "→E"] **by** blast |
| 8774 | **AOT_hence** ❬ ᷑(∀F ([F]x ≡ [F]y) → (φ{x} ≡ φ{y})) ❭ |
| 8775 | **using** "∀E" **by** blast |
| 8776 | **AOT_hence** ❬ □∀F([F]x ≡ [F]y) → □(φ{x} ≡ φ{y}) ❭ |
| 8777 | **using** "qml:1"[axiom_inst] "vdash-properties:6" **by** blast |
| 8778 | **moreover AOT_assume** ❬ ∀F([F]x ≡ [F]y) ❭ |
| 8779 | **ultimately AOT_show** ❬ □(φ{x} ≡ φ{y}) ❭ **using** "→E" "ind-nec" **by** blast |
| 8780 | **qed** |

After establishing further results about basic logical objects, restricted variables, the extended relation comprehension, and possible worlds, the computational exploration can then be redirected to Dedekind-Peano arithmetic where its postulates for natural numbers are formally derived in a system free of mathematical primitive notions and mathematical axioms—Frege’s Theorem—and thereby supporting the claim that AOT can provide a philosophically grounded basis for objects of mathematics. The computational approach in Kirchner 2021 is guided by a proof outline that was previously given in Zalta 1999 but that now, being reconstructed in Isabelle/HOL, produces derivations of the postulates in full detail and formality.

> *Postulate 1*
> **AOT_theorem** "0-n": ❬ [ℕ]0 ❭
>
> *Postulate 2*
> **AOT_theorem** "0-pred": ❬ ¬∃n [ℙ]n 0 ❭
>
> *Postulate 3*
> **AOT_theorem** "no-same-succ": ❬ ∀n∀m∀k([ℙ]nk & [ℙ]mk → n = m) ❭
>
> *Postulate 4*
> **AOT_theorem** "th-succ": ❬ ∀n∃!m [ℙ]nm ❭
>
> *Postulate 5*
> **AOT_theorem** induction: ❬ ∀F([F]0 & ∀n∀m([ℙ]nm → ([F]n → [F]m)) → ∀n[F]n) ❭

The computational explorations described above were done using the second-order fragment of AOT but the SSE could be extended to the full higher-order logic AOT (Kirchner 2021)[^kirchner-2021] where it could be applied to the analysis of theoretical mathematics. It is important to stress that embedding a target theory within the higher-order logic of an existing prover results in more than just a formalization of the theory: The SSE allows for the discovery of new results within the target theory, as exemplified above, as well as the study and further development of the target theory itself such as placing the theory on firmer foundations, e.g. avoiding known paradoxes (Zalta 2018, Kirchner 2021)[^kirchner-2021][^zalta-2018]. The computational analysis of AOT described in here can also be construed as yet another test of the concept of embedding theories, simple and complex alike, within the framework of a higher-order prover. It illustrates the power and convenience of the approach, and researchers in automated reasoning may want to seriously consider using an SSE in their theorem-proving efforts (Benzmüller 2019)[^benzmüller-2019].

Leibniz’s dream was to have a *charateristica universalis* and *calculus ratiocinator* that would allow us to reason in metaphysics and morals in much the same way as we do in geometry and analysis; that is to say, to settle disputes between philosophers as accountants do: “To take pen in hand, sit down at the abacus and, having called in a friend if they want, say to each other: Let us calculate!” From the above applications of automated reasoning, one would agree with the researchers when they imply that these results achieve, to some extent, Leibniz’s goal of a computational metaphysics (Fitelson & Zalta 2007, Benzmüller & Paleo 2014)[^benzmüller-2014][^fitelson-2007].

#### Procedural epistemology

Work in computational metaphysics has implications in other areas in philosophy such as e.g. epistemology. An obvious example is our improved epistemological standing when errors in our reasoning are (computationally) detected and corrected. Also, proofs produced by automated reasoning systems can help us better understand complex arguments, and see more quickly the consequences of revising our theories by the introduction, or removal, or axioms—a sort of “what-if analysis”. To illustrate, in the desire to simplify the foundations of AOT, one can attempt the removal of constraints in the comprehension principle but it can be shown that this move leads to a paradox in a non-trivial way (Kirchner 2021)[^kirchner-2021]. Finding alternative axiom sets for a given theory can help reduce the epistemological load needed to prove meta-theoretical results such as soundness. In brief, “one of the great benefits of using computational techniques is that enables us to see exactly what the commitments of our theories are” (Zalta 2018)[^zalta-2018].

As a direct application in epistemology, a nonmonotonic theorem prover can provide the basis for a “computational laboratory” in which to explore and experiment with different models of artificial rationality; the theorem prover can be used to equip an artificial rational agent with an inference engine to reason and gain information about the world. In such **procedural epistemology**, a rational agent is defeasible (i.e. nonmonotonic) in the sense that new reasoning leads to the acceptance of new beliefs but also to the retraction of previously held beliefs in the presence of new information. At any given point in time, the agent holds a set of justified beliefs but this set is open to revision and is in a continuous set of flux as further reasoning is conducted. This model better reflects our accepted notion of rationality than a model in which all the beliefs are warranted, i.e. beliefs that once are attained are never retracted. Actually, a set of warranted beliefs can be seen as justified beliefs “in the limit”, that is, as the ultimate epistemic goal in the agent’s search for true knowledge about its world. (Pollock 1995)[^pollock-1995] offers the following definition:

A set is defeasible enumerable iff there is an effective computable function $f$ such that for each $n, f(n)$ is a recursive set and the following two conditions hold

**1.**

$(\forall x)(x \in A \rightarrow (\exists n)(\forall m \gt n) x \in f(m))$

**2.**

$(\forall x)(x \not\in A \rightarrow (\exists n)(\forall m \gt n) x \not\in f(m))$

To compare the concepts, if $A$ is recursively enumerable then there is a sequence of recursive sets $A_i$ such that each $A_i$ is a subset of $A$ with each $A_i$ growing monotonically, approaching $A$ in the limit. But if $A$ is only defeasibly enumerable then the $A_i$’s still approach $A$ in the limit but may not be subsets of $A$ and approach $A$ intermittently from above and below. The goal of the OSCAR Project (Pollock 1989)[^pollock-1989] is to construct a general theory of rationality and implement it in an artificial computer-based rational agent. As such, the system uses a defeasible automated reasoner that operates according to the maxim that the set of warranted beliefs should be defeasible enumerable. OSCAR has been in the making for some time and the application of automated nonmonotonic reasoning has also been used to extend its capabilities to reason defeasibly about perception and time, causation, and decision-theoretic planning (Pollock 2006)[^pollock-2006].

### 4.7 Mathematics

One of the main goals of automated reasoning has been the automation of mathematics. An early attempt at this was Automath (de Bruijn 1968)[^bruijn-1968] which was the first computer system used to check the correctness of proofs and whole books of mathematics, including Landau’s *Grundlagen der Analysis* (van Benthem Jutting 1977)[^benthem-1977]. Automath has been superseded by more modern and capable systems, most notably Mizar. The Mizar system (Trybulec 1979, Muzalewski 1993)[^muzalewski-1993] is based on Tarski-Grothendieck set theory and, like Automath, consists of a formal language which is used to write mathematical theorems and their proofs. Once a proof is written in the language, it can be checked automatically by Mizar for correctness. Mizar proofs are formal but quite readable, can refer to definitions and previously proved theorems and, once formally checked, can be added to the growing Mizar Mathematical Library (MML) (Bancerek & Rudnicki 2003, Bancerek *et al*. 2018)[^bancerek-2003][^bancerek-2018]. As of June 2018, MML contained about 12,000 definitions and 59,000 theorems. The Mizar language is a subset of standard English as used in mathematical texts and is highly structured to ensure the production of rigorous and semantically unambiguous texts. Here’s a sample proof in Mizar of the existence of a rational number *x$^y$* where $x$ and $y$ are irrational:

| theorem T2: |
| --- |
| ex x, y st x is irrational & y is irrational & x.^.y is rational |
| proof |
| set w = √2; |
| H1: w is irrational by INT_2:44,T1; |
| w>0 by AXIOMS:22,SQUARE_1:84; |
| then (w.^.w).^.w = w.^.(w•w) by POWER:38 |
| .= w.^.(w²) by SQUARE_1:58 |
| .= w.^.2 by SQUARE_1:88 |
| .= w² by POWER:53 |
| .= 2 by SQUARE_1:88; |
| then H2: (w.^.w).^.w is rational by RAT_1:8; |
| per cases; |
| suppose H3: w.^.w is rational; |
| take w, w; |
| thus thesis by H1,H3; |
| suppose H4: w.^.w is irrational; |
| take w.^.w, w; |
| thus thesis by H1,H2,H4; |
| end; |

Examples of proofs that have been checked by Mizar include the Hahn-Banach theorem, the Brouwer fixed-point theorem, Kőnig’s lemma, the Jordan curve theorem, and Gödel’s completeness theorem. Rudnicki (2004) discusses the challenges of formalizing Witt’s proof of the Wedderburn theorem: *Every finite division ring is commutative*. The theorem was formulated easily using the existing formalizations available in MML but the proof demanded further entries into the library to formalize notions and facts from algebra, complex numbers, integers, roots of unity, cyclotomic polynomials, and polynomials in general. It took several months of effort to supply the missing material to the MML library but, once in place, the proof was formalized and checked correct in a matter of days. Clearly, a repository of formalized mathematical facts and definitions is a prerequisite for more advanced applications. The QED Manifesto (Boyer *et al*. 1994, Wiedijk 2007)[^boyer-1994][^wiedijk-2007] has such aim in mind and there is much work to do: Mizar has the largest such repository but even after 30 years of work “it is minuscule with respect to the body of established mathematics” (Rudnicki 2004). This last remark should be construed as a call to increase the effort toward this important aspect in the automation of mathematics.

Mizar’s goal is to assist the practitioner in the formalization of proofs and to help check their correctness; other systems aim at finding the proofs themselves. Geometry has been a target of early automated proof-finding efforts. Chou (1987)[^chou-1987] proves over 500 geometry theorems using the algebraic approach offered by Wu’s method and the Gröbner basis method by representing hypotheses and conclusions as polynomial equations. Quaife (1992)[^quaife-1992] provides another early effort to find proofs in first-order mathematics: over 400 theorems in Neumann-Bernays-Gödel set theory, over 1,000 theorems in arithmetic, a number of theorems in Euclidian geometry, and Gödel’s incompleteness theorems. The approach is best described as semi-automatic or “interactive” with the user providing a significant amount of input to guide the theorem-proving effort. This is no surprise since, as one applies automated reasoning systems into richer areas of mathematics, the systems take more on the role of proof assistants than theorem provers. This is because in richer mathematical domains the systems need to reason about theories and higher-order objects which in general takes them deeper into the undecidable. **Interactive theorem proving** is arguably the “killer” application of automated reasoning in mathematics and much effort is being expended in the building of increasingly capable reasoning systems that can act as assistants to professional mathematicians. The proof assistant Isabelle/HOL provides the user with an environment in which to conduct proofs expressed in a structured, yet human-readable, higher-order logic language and which incorporates a number of facilities that increase the user’s productivity, automates proof-verification and proof-finding tasks, and provides a modular way for the user to build and manage theory hierarchies (Ballarin 2014)[^ballarin-2014]. More recently, using both automated and interactive theorem proving techniques, Quafie’s work in Tarskian geometry has been extended with the proving of additional theorems (some of which required Ph.D. level proofs), including four challenge problems left unsolved by Quaife, and the derivation of Hilbert’s 1899 axioms for geometry from Tarski’s axioms (Beeson and Wos 2017)[^beeson-2017].

Different proof assistants offer different capabilities measured by their power at automating reasoning tasks, supported logic, object typing, size of mathematical library, and readability of input and output. A “canonical” proof which is not too trivial but not too complex either can be used as a baseline for system comparison, as done in (Wiedijk 2006)[^wiedijk-2006] where the authors of seventeen reasoning systems are tasked with establishing the irrationality of $\sqrt{} 2$. The systems discussed are certainly more capable than this and some have been used to assist in the formalization of far more advanced proofs such as Erdös-Selberg’s proof of the Prime Number Theorem (about 30,000 lines in Isabelle), the formalization of the Four Color Theorem (60,000 lines in Coq), and the Jordan Curve Theorem (75,000 lines in HOL Light). A milestone in interactive theorem proving was reached in 2012 when, after six-years of effort and using the Coq proof assistant, George Gonthier and his team completed the formal verification of the 255-page proof of the Feit-Thompson theorem, also known as the Odd Order Theorem, a major step in the classification of finite simple groups. Other, more recent, successes include the resolution of Keller’s conjecture (Brakensiek *et al.* 2022)[^brakensiek-2022], the formalization of metric spaces (Maggesi 2018)[^maggesi-2018], and the formalization and classification of finite fields (Chan and Norrish 2019)[^chan-2019].

The above notwithstanding, automated reasoning has had a small impact on the practice of doing mathematics and there is a number of reasons given for this. One reason is that automated theorem provers are not sufficiently powerful to attempt the kind of problems mathematicians typically deal with; that their current power is, at best, at the level of first-year undergraduate mathematics and still far from leading edge mathematical research. While it is true that current systems cannot prove completely on their own problems at this level of difficulty we should remember that the goal is to build reasoning systems so that “eventually machines are to be an aid to mathematical research and not a substitute for it” (Wang 1960)[^wang-1960][^wang-1960-2]. With this in mind, and while the automated reasoning community continues to try to meet the grand challenge of building increasingly powerful theorem provers, mathematicians can draw now some of the benefits offered by current systems, including assistance in completing proof gaps or formalizing and checking the correctness of proposed proofs. Indeed, the latter may be an application that could help address some real issues currently being faced by the mathematical community. Consider the announcement by Daniel Goldston and Cem Yildrim of a proof of the Twin Prime Conjecture where, although experts initially agreed that the proof was correct, an insurmountable error was found shortly after. Or, think about the case of Hales’ proof of the Kepler Conjecture which asserts that no packing of congruent balls in Euclidean 3-space has density greater than the face-centered cubic packing. Hales’ proof consists of about 300 pages of text and a large number of computer calculations. After four years of hard work, the 12-person panel assigned by *Annals of Mathematics* to the task of verifying the proof still had genuine doubts about its correctness. Thomas Hales, for one, took upon himself to formalize his proof and have it checked by an automated proof assistant with the aim of convincing others of its correctness (Hales 2005b, in Other Internet Resources). His task was admittedly heavy but the outcome is potentially very significant to both the mathematical and automated reasoning communities. All eyes were on Hales and his formal proof as he announced the completion of the *Flyspeck* project (Hales 2014, in Other Internet Resources; Hales 2015)[^hales-2015] having constructed a formal proof of the conjecture using the Isabelle and HOL Light automated proof assistants: “In truth, my motivations for the project are far more complex than a simple hope of removing residual doubt from the minds of few referees. Indeed, I see formal methods as fundamental to the long-term growth of mathematics.” (Hales 2006)[^hales-2006].

Church 1936a, 1936b and Turing 1936 imply the existence of theorems whose shortest proof is very large, and the proof of the Four Color Theorem in (Appel & Haken 1977)[^appel-1977], the Classification of Simple Groups in (Gorenstein 1982)[^gorenstein-1982], and the proof of the Kepler Conjecture in (Hales 2005a)[^hales-2005a] may well be just samples of what is yet to come. As (Bundy 2011)[^bundy-2011] puts it: “As important theorems requiring larger and larger proofs emerge, mathematics faces a dilemma: either these theorems must be ignored or computers must be used to assist with their proofs.”

The above remarks also counter another argument given for not using automated theorem provers: Mathematicians enjoy proving theorems, so why let machines take away the fun? The answer to this is, of course, that mathematicians can have even more fun by letting the machine do the more tedious and menial tasks: “It is unworthy of excellent men to lose hours like slaves in the labour of calculation which could safely be relegated to anyone else if machines were used” (G. W. Leibniz, *New Essays Concerning Human Understanding*). If still not convinced, just consider the sobering prospect of having to manually check the 23,000 inequalities used in Hales’ proof!

Another reason that is given for the weak acceptance of automated reasoning by the mathematical community is that the programs are not to be trusted since they may contain bugs—software defects—and hence may produce erroneous results. Formally verifying automated reasoning programs will help ameliorate this, particularly in the case of proof checkers. Proving programs correct is no easy task but the same is true about proving theorems in advanced mathematics: Gonthier proved correct the programs used in the formalization of his proof of the Four Color Theorem, but he spent far more effort formalizing all the graph theory that was part of the proof. So ironically enough, it turns out that at least in this case, and surely there are others, “it is actually easier to verify the correctness of the program than to verify the correctness of the pen-and-paper mathematics” (Wiedijk 2006)[^wiedijk-2006]. For theorem provers and model finders, a complementary strategy would be to verify the programs’ results as opposed to the programs themselves. Paraphrasing (Slaney 1994): It does not matter to the mathematician how many defects a program may have as long as the proof (or model) it outputs is correct. So, the onus is in the verification of results, whether produced by machine or man, and checking them by independent parties (where of course the effort may well use automated checkers) should increase the confidence on the validity of the proofs.

It is often argued that automated proofs are too long and detailed. That a proof can be expressed in more elementary steps is in principle very beneficial since this allows a mathematician to request a proof assistant justify its steps in terms of simpler ones. But proof assistants should also allow the opposite, namely to abstract detail and present results and their justifications using the higher-level concepts, language, and notation mathematicians are accustomed to. Exploiting the hierarchical structure of proofs as done in (Denney 2006)[^denney-2006] is a step in this direction but more work along these lines is needed. Having the proof assistant work at the desired level of granularity provides more opportunity for insight during the proof discovery process. This is an important consideration since mathematicians are equally interested in gaining understanding from their proofs as in establishing facts—more about this below.

(Bundy 2011)[^bundy-2011] alludes to a deadlock that is preventing the wider adoption of theorem provers by the mathematical community: On the one hand, the mathematicians need to use the proof assistants to build a large formal library of mathematical results. But, on the other hand, they do not want to use the provers since there is no such library of previously proved results they can build upon. To break the impasse, a number of applications are proposed of which assisting the mathematician in the search of previously proved theorems is of particular promise. Indeed, a thoughtful reuse of library results can lead to concise proofs of non-trivial mathematical problems as exemplified in the proving of some fundamental theorems of linear algebra (Aransay and Divansón 2017)[^aransay-2017] and probability theory (Avigad, Hölzl and Serafin 2017)[^avigad-2017]. During its history, mathematics has accumulated a huge number of theorems and the number of mathematical results continues to grow dramatically. In 2010, *Zentralblatt MATH* covered about 120,000 new publications (Wegner 2011)[^wegner-2011]. Clearly, no individual researcher can be acquainted with all this mathematical knowledge and it will be increasingly difficult to cope with one’s ever-growing area of specialty unless assisted with automated theorem-proving tools that can search in intelligent ways for previously proved results of interest. An alternative approach to this problem is for mathematicians to tap into each other’s knowledge as enabled in computational social systems like *polymath* and *mathoverflow*. The integration of automated reasoning tools into such social systems would increase the effectiveness of their collective intelligence by supporting “the combination of precise formal deductions and the more informal loose interaction seen in mathematical practice” (Martin & Pease 2013, in Other Internet Resources).

Due to real pressing needs from industry, some applications of automated reasoning in pure and applied mathematics are more of necessity than choice. After having worked on the formalization of some elementary real analysis to verify hardware-based floating point trigonometric functions, (Harrison 2006, Harrison 2000)[^harrison-2000][^harrison-2006] mentions the further need to formalize *more* pure mathematics—italics are his—to extend his formalization to power series for trigonometric functions and basic theorems about Diophantine approximations. Harrison finds it surprising that “such extensive mathematical developments are used simply to verify that a floating point tangent function satisfies a certain error bound” and, from this remark, one would expect there are other industrial applications that will demand more extensive formalizations.

Albeit not at the rate originally anticipated, automated reasoning is finding applications in mathematics. Of these, formal verification of proofs is of special significance since it not only provides a viable mechanism to check proofs that humans alone could not but it also has, as a side effect, the potential to redefine what it would take for a proof to be accepted as such. As the use of automated reasoning assistants becomes more widespread one can envision their use following a certain methodical order: First, automated reasoning tools are used for theory exploration and discovery. Then, having identified some target problem, the practitioner works interactively with an automated assistant to find proofs and establish facts. Finally, an automated proof checker is used to check the correctness of all final proofs prior to being submitted for publication and being made available to the rest of the mathematical community via the creation of new entries in a repository of formalized mathematics. It is indeed a matter of time before the application of automated proof assistants becomes an everyday affair in the life of the mathematician; it is the grand challenge of the automated reasoning community to make it happen sooner than later.

Besides formal verification, or *certification*, another important aspect of a proof is the *explanation* it provides; that is, the reasons it gives as to why the given statement is actually true. This, needless to say, is an important source of insight and for many mathematicians it may be the single most valuable aspect of a proof as it allows them to gain a better understanding of the nature of the statement being established and of the mathematical theory and objects involved; moreover, the approach used in the proof has the potential of being applicable to the proving of other mathematical results. So when it comes to building theorem provers to be used by the mathematical community, perhaps there should be less emphasis on the provers as certifiers, i.e. as proof checkers, and place more emphasis on the provers as proof solvers, i.e. as assistants in helping the mathematician complete proofs and explain the steps in doing so. Assuming that a prover were to be powerful enough to successfully attack proofs in the mathematician’s area of research, it would be very desirable yet admittedly extremely challenging if the prover were to also use the very same notation, methods, and techniques of proof-solving used by the mathematician herself. One could safely bet that mathematicians would be more receptive to this type of human-oriented theorem prover because the prover would work the same way the mathematician does. More mathematicians may initially approach such a prover simply out of sheer curiosity; that is, just to see how the prover would go about proving a previously established result. This would certainly be of much interest to students of mathematics since they may need to see how a given problem (say, from their textbook) has been solved and, by inspecting the proof, want to learn how to do it on their own.

Virtually all automated theorem provers nowadays go about building their proofs in ways far more akin to machines than to humans (e.g. resolution-driven, connection methods). There are some systems that, after establishing a fact, can present the higher-level steps in the proof in a form more amenable to humans and do so by translating the machine-oriented steps into a human-readable format. The approach has merit but it has a significant limitation: How deep into the proof can one continue asking for an explanation before the translation breaks down? An alternative approach could try to address the situation head on: Why not build a system that directly proves theorems the way mathematicians actually do it? This is indeed a very tall order but the question is not new and it has been taken up in various forms by a small minority of researchers going back to the early days of automated theorem proving, including Bledsoe 1977 (investigations into non-resolution methods), Boyer and Moore 1979 (induction by recursive term rewriting), Bundy *et al*. 1991 (automated inductive theorem proving), Clarke and Zhao 1994 (integration of theorem provers with symbolic algebra systems), Portoraro 1994 (automated advice to students building symbolic logic proofs), Portoraro 1998 (strategic proof construction the way teachers of symbolic logic do and teach it), Pelletier 1998 (building proofs in the predicate calculus the way humans do it), Beeson 2001 (proof generation using mathematical methods), Buchberger *et al*. 2016 (computer-assisted natural-style mathematics), and others. More recently, Ganesalingam and Gowers 2017 describes a theorem prover that solves and presents proofs of elementary problems in metric space theory where the program’s approach is hard to distinguish from what a mathematician might prove and write. To illustrate, below is the program’s proof that the intersection of two open subsets of a metric space is itself open, and it is given as it was both solved and written by the program:

> ***Proof***. Let $x$ be an element of $A\cap B$. Then $x \in A$ and $x \in B$. Therefore, since $A$ is open, there exists $\eta > 0$ such that $u \in A$ whenever $d(x, u) \lt \eta$ and since $B$ is open, there exists $\theta > 0$ such that $v \in B$ whenever $d(x, v) \lt \theta$. We would like to find $\delta > 0$ s.t. $y \in A\cap B$ whenever $d(x, y) \lt \delta$. But $y \in A\cap B$ if and only if $y \in A$ and $y \in B$. We know that $y\cap A$ whenever $d(x, y) \lt \eta$ and that $y\cap B$ whenever $d(x, y) \lt \theta$. Assume now that $d(x, y) \lt \delta$. Then $d(x, y) \lt \eta$ if $\delta \le \eta$ and $d(x, y) \lt \theta$ if $\delta \le \theta$. We may therefore take $\delta = \text{min}\{\eta , \theta \}$ and we are done.

Impressive as it may be, the authors acknowledge a number of shortcomings and many outstanding challenges in the building and presentation of such proofs even for elementary problems in mathematics, and the reader is referred to their article for details. As we have already mentioned, building increasingly powerful provers that can attack problems in advanced areas of mathematical research and doing so in a human-oriented fashion is admittedly extremely challenging but also, we need to add, a very worthwhile, promising, and rewarding line of research. Embracing this kind of provers by mathematicians will have clear practical applications both in research and education. There will be philosophical implications too, especially the moment the provers are endowed with the additional ability to ask for assistance when getting stuck in a proof and, when this happens, we will be pressed to ask: Who is interacting with whom, the human with the machine or vice versa? The experience of interacting with a theorem prover will have been extended to a new realm, becoming truly two-sided, more intimate and richer, more of a *collaboration* than an interaction: the dawn of *collaborative theorem proving*.

### 4.8 Artificial Intelligence

Since its inception, the field of automated theorem proving has had important applications in the larger field of artificial intelligence (AI). Automated deduction is at the heart of AI applications like logic programming (see Section 4.1 Logic Programming) where computation is equated with deduction; robotics and problem solving (Green 1969)[^green-1969] where the steps to achieve goals are steps extracted from proofs; deductive databases (Minker *et al*. 2014)[^minker-2014] where factual knowledge is expressed as atomic clauses and inference rules, and new facts are inferred by deduction; expert systems (Giarratano & Riley 2004)[^giarratano-2004] where human expertise in a given domain (e.g. blood infections) is captured as a collection of IF-THEN deduction rules and where conclusions (e.g. diagnoses) are obtained by the application of the inference rules; and many others. An application of automated reasoning in AI which is bound to have deep philosophical implications is the increased use of BDI computational logics for describing the beliefs, desires, and intentions of intelligent agents and multi-agent systems (Meyer 2014)[^meyer-2014] and, in particular, endowing future intelligent systems, such as decision-support systems or robots, with legal and ethical behaviour. Deontic logic can be automated for the task (Furbach *et al*. 2014)[^furbach-2014] but given that there is no agreement on a universal system of deontic logic, ethics “code designers” need a way to experiment with the different deontic systems (i.e., to lay out axioms and see what conclusions follow from them) to help them identify the desired ethic code for the specific application at hand; (Benzmüller *et al*. 2018)[^benzmüller-2018] discusses an environment for this. If actual, physical, robots were to be used in these experiments, the term “deontic laboratory” would be quite descriptive albeit somewhat eerie.

Restricting the proof search space has always been a key consideration in the implementation of automated deduction, and traditional AI-approaches to search have been an integral part of theorem provers. The main idea is to prevent the prover from pursuing unfruitful reasoning paths. A dual aspect of search is to try to look for a previously proved result that could be useful in the completion of the current proof. Automatically identifying those results is no easy task and it becomes less easy as the size of the problem domain, and the number of already established results, grows. This is not a happy situation particularly in light of the growing trend to build large libraries of theorems such as the Mizar Problems for Theorem Proving (MPTP) (Urban *et al*. 2010, Bancerek & Rudnicki 2003)[^bancerek-2003][^urban-2010] or the Isabelle/HOL mathematical library (Meng & Paulson 2008)[^meng-2008], so developing techniques for the discovery, evaluation, and selection of existing suitable definitions, premises and lemmas in large libraries of formal mathematics as discussed in (Kühlwein *et al*. 2012)[^kühlwein-2012] is an important line of research.

Among many other methods, and in stark contrast to automated provers, mathematicians combine induction heuristics with deductive techniques when attacking a problem. The former helps them guide the proof-finding effort while the latter allows them to close proof gaps. And of course all this happens in the presence of the very large body of knowledge that the human possesses. For an automated prover, the analogous counterpart to the mathematician’s body of knowledge is a large library like MPTP. An analogous approach to using inductive heuristics would be to endow the theorem prover with inductive, data-driven, machine learning abilities. Urban & Vyskocil 2012 run a number of experiments to determine any gains that may result from such an approach. For this, they use MPTP and theorem provers like E and SPASS enhanced with symbol-based machine learning mechanisms. A detailed presentation and statistical results can be found in the above reference but in summary, and quoting the authors, “this experiment demonstrates a very real and quite unique benefit of large formal mathematical libraries for conducting novel integration of AI methods. As the machine learner is trained on previous proofs, it recommends relevant premises from the large library that (according to the past experience) should be useful for proving new conjectures.” Urban 2007 discusses MaLARea (a Machine Learner for Automated Reasoning), a meta-system that also combines inductive and deductive reasoning methods. MaLARea is intended to be used in large theories, i.e. problems with a large number of symbols, definitions, premises, lemmas, and theorems. The system works in cycles where results proved deductively in a given iteration are then used by the inductive machine-learning component to place restrictions in the search space for the next theorem-proving cycle. Albeit simple in design, the first version of MaLARea solved 142 problems out of 252 in the MPTP Challenge, outperforming the more seasoned provers E (89 problems solved) and SPASS (81 problems solved). Machine learning premise-selection methods trained on the considerable amount of mathematical knowledge encoded in Flyspeck’s library of proofs, when combined with theorem provers, provides an AI-type system capable of proving a wide range of mathematical conjectures: Almost 40% of the 14,185 theorems can be proved automatically without any guidance from the user within 30 seconds on a 14-CPU workstation (Kaliszyk & Urban 2014)[^kaliszyk-2014]. Machine learning techniques can also be applied successfully to the problem of selecting good heuristics in the building of first-order proofs (Bridge, Holden & Paulson 2014)[^bridge-2014].

The relationship between automated deduction and machine learning is reciprocal and the former has something to offer to the latter too. To mention one contribution, deep learning has become the technique of choice when it comes to applications in image recognition, language processing, and others, and there is theoretical evidence of its superiority over shallow learning. Such mathematical proofs can be formalized using theorem-proving systems like e.g. Isabelle/HOL while at the same time can contribute to the growth of their libraries with formalized results that can be used for further work aimed to secure the foundations of machine learning (Bentkamp, Blanchette & Klakow 2019)[^bentkamp-2019].

Besides using large mathematical libraries, tapping into web-based semantic ontologies is another possible source of knowledge. Pease & Sutcliffe 2007 discuss ways for making the SUMO ontology suitable for first-order theorem proving, and describes work on translating SUMO into TPTP. An added benefit of successfully reasoning over large semantic ontologies is that this promotes the application of automated reasoning into other fields of science. Tapping into its full potential, however, will require a closer alignment of methods from automated reasoning and artificial intelligence.

## 5. Conclusion

Automated reasoning is a mature yet still growing field that provides a healthy interplay between basic research and application. Automated deduction is being conducted using a multiplicity of theorem-proving methods, including resolution, sequent calculi, natural deduction, matrix connection methods, term rewriting, mathematical induction, and others. These methods are implemented using a variety of logic formalisms such as first-order logic, type theory and higher-order logic, clause and Horn logic, non-classical logics, and so on. Automated reasoning programs are being applied to solve a growing number of problems in formal logic, mathematics and computer science, logic programming, software and hardware verification, circuit design, exact philosophy, and many others. One of the results of this variety of formalisms and automated deduction methods has been the proliferation of a large number of theorem proving programs. To test the capabilities of these different programs, selections of problems have been proposed against which their performance can be measured (McCharen, Overbeek & Wos 1976, Pelletier 1986)[^mccharen-1976][^pelletier-1986]. The TPTP (Sutcliffe & Suttner 1998, Sutcliffe 2017)[^sutcliffe-2017][^sutcliffe-1998] is a library of such problems that is updated on a regular basis. There is also a competition among automated theorem provers held regularly at the CADE conference (Pelletier, Sutcliffe & Suttner 2002; Sutcliffe 2016, in Other Internet Resources)[^pelletier-2002]; the problems for the competition are selected from the TPTP library and range from problems in clause normal form (CNF), fist-order form (FOF), typed first-order form (TFF), monomorphic typed higher-order form (TH0), and others. There is a similar library and competition for SMT solvers (Barret *et al*. 2013)[^barret-2013].

Initially, computers were used to aid scientists with their complex and often tedious numerical calculations. The power of the machines was then extended from the numeric into the symbolic domain where infinite-precision computations performed by computer algebra programs have become an everyday affair. The goal of automated reasoning has been to further extend the machine’s reach into the realm of deduction where they can be used as reasoning assistants in helping their users establish truth through proof.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=reasoning-automated). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/reasoning-automated/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=reasoning-automated&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/reasoning-automated/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

### Publications

- Hales, T. C., 2005b, [*The Flyspeck Project Fact Sheet*](http://code.google.com/p/flyspeck/wiki/FlyspeckFactSheet)
- Hales, T. C., 2014, [*Flyspeck*](http://code.google.com/p/flyspeck/wiki/AnnouncingCompletion)
- Kaufman, M. and J. S. Moore, 2024, “[A Walking Tour of ACL2](https://www.cs.utexas.edu/~moore/acl2/v8-6/combined-manual/index.html?topic=ACL2____A_02Walking_02Tour_02of_02ACL2)”, *ACL2 User’s Manual*.
- Martin, U. and A. Pease, 2013, “[What does mathoverflow tell us about the production of mathematics?](http://arxiv.org/abs/1305.0904),” *Computing Research Repository*, at arxiv.org.
- Sutcliffe, G., 2014, *Proceedings of the 7th IJCAR Automated Theorem Proving System Competition (CASC-J7)*, [available online](https://dl.acm.org/doi/10.3233/AIC-150668), pp. 1–36.
- Sutcliffe, G., 2016, *Proceedings of the 8th IJCAR Automated Theorem Proving System Competition (CASC-J8)*, [available online](https://tptp.org/CASC/J8/Proceedings.pdf), pp. 1–40.

### Web Sites

- [ACL2: A Computational Logic](http://www.cs.utexas.edu/users/moore/acl2/)
- [Alfa/Agda](http://wiki.portal.chalmers.se/agda/pmwiki.php)
- [The Coq Proof Assistant (now known as the Rocq Prover)](https://rocq-prover.org/)
- [CVC4](http://cvc4.cs.stanford.edu/web/)
- [E Theorem Prover](http://wwwlehre.dhbw-stuttgart.de/~sschulz/E/E.html)
- [EQP Equational Prover](http://www.cs.unm.edu/~mccune/eqp/)
- [HOL Automated Reasoning Group](http://www.cl.cam.ac.uk/research/hvg/HOL/)
- [HOL Light](https://hol-light.github.io/)
- [IMPS: An Interactive Mathematical Proof System](http://imps.mcmaster.ca)
- [iProver](https://gitlab.com/korovin/iprover/)
- [Isabelle](http://www.cl.cam.ac.uk/research/hvg/Isabelle/)
- [leanCoP](http://www.leancop.de/)
- [LEO-II](http://www.cl.cam.ac.uk/~lp15/Grants/LEO-II/index.html)
- [LEO-III](https://github.com/leoprover/Leo-III/)
- [Metamath](http://us.metamath.org/)
- [MetiTarski](http://www.cl.cam.ac.uk/~lp15/papers/Arith/)
- [The Minlog System](http://www.minlog-system.de)
- [The Mizar Project](http://www.mizar.org/)
- [The Nuprl Project](https://nuprl-web.cs.cornell.edu/)
- [Paradox](http://vlsicad.eecs.umich.edu/BK/Slots/cache/www.cs.chalmers.se/~koen/paradox/)
- [Prover 9 and Mace 4](http://www.cs.unm.edu/~mccune/prover9/)
- [PVS Specification and Verification System](http://pvs.csl.sri.com/)
- [Satallax](http://www.ps.uni-saarland.de/~cebrown/satallax/)
- [Sledgehammer](https://isabelle.in.tum.de/website-Isabelle2009-1/sledgehammer.html)
- [SPASS](http://www.spass-prover.org/)
- [TPS Theorem Proving System](http://gtps.math.cmu.edu/tps.html)
- [Vampire](http://vprover.github.io/)
- [Yices 2](http://yices.csl.sri.com/)
- [Z3](https://github.com/Z3Prover/z3/)
- [The CADE ATP System Competition](https://tptp.org/CASC/)
- [The TPTP Problem Library for Automated Theorem Proving](https://www.tptp.org/)
- [The SMT-LIB Satisfiability Modulo Theories Library](http://smtlib.cs.uiowa.edu/)
- [The QED Manifesto](http://www.cs.ru.nl/~freek/qed/qed.html)
- [CADE: The Conference on Automated Deduction](http://www.cadeinc.org/)
- [IJAR: The International Joint Conference on Automated Reasoning](http://ijcar.org/)

## Related Entries

artificial intelligence: logic-based | logic: classical | logic: modal | reasoning: defeasible

[^alama-2015]: Alama, J., P. Oppenheimer, and E. Zalta, 2015, “Automating Leibniz’s Theory of Concepts”, *CADE 25: Proceedings of the 25th International Conference on Automated Deduction*, (Lecture Notes in Artificial Intelligence: Volume 9195), A. Felty and A. Middeldorp (eds.), Berlin: Springer, pp. 73–97.

[^anderson-1990]: Anderson, C. A., 1990, “Some Emendations of Gödel’s Ontological Proof”, *Faith and Philosophy*, 7(3): 291–303.

[^anderson-1962]: Anderson, A. R. and N. D. Belnap, 1962, “The Pure Calculus of Entailment”, *Journal of Symbolic Logic*, 27: 19–52.

[^andrews-1981]: Andrews, P. B., 1981, “Theorem-Proving via General Matings”, *Journal of the Association for Computing Machinery*, 28 (2): 193–214.

[^andrews-2006]: Andrews, P. B., M. Bishop and C. E. Brown, 2006, “TPS: A Hybrid Automatic-Interactive System for Developing Proofs”, *Journal of Applied Logic*, 4: 367–395.

[^andrews-1996]: Andrews, P. B., M. Bishop, S. Issar, D. Nesmith, F. Pfenning and H. Xi, 1996, “TPS: A Theorem-Proving System for Classical Type Theory”, *Journal of Automated Reasoning*, 16 (3): 321–353.

[^appel-1977]: Appel, K., and W. Haken, 1977, “Every Planar Map is Four Colorable Part I. Discharging”, *Illinois Journal of Mathematics*, 21: 429–490.

[^aransay-2017]: Aransay, J., J. Divansón, 2017, “A Formalization in HOL of the Fundamental Theorem of Linear Algebra and Its Application to the Solution of the Least Squares Problem”, *Journal of Automated Reasoning*, 58 (4): 509–535.

[^avigad-2014]: Avigad, J. and J. Harrison, 2014, “Formally Verified Mathematics”, *Communications of the ACM*, 57 (4): 66–75.

[^avigad-2017]: Avigad, J., J. Hölzl and L. Serafin, 2017, “A Formally Verified Proof of the Central Limit Theorem”, *Journal of Automated Reasoning*, 59 (4): 389–423.

[^baader-1998]: Baader, F. and T. Nipkow, 1998, *Term Rewriting and All That*, Cambridge: Cambridge University Press.

[^bachmair-1994]: Bachmair, L. and H. Ganzinger, 1994, “Rewrite-Based Equational Theorem Proving with Selection and Simplification”, *Journal of Logic and Computation*, 4 (3): 217–247.

[^ballarin-2014]: Ballarin, C., 2014, “Locales: A Module System for Mathematical Theories”, *Journal of Automated Reasoning*, 52 (2): 123–153.

[^bancerek-2003]: Bancerek, G. and P. Rudnicki, 2003, “Information Retrieval in MML”, *Proceedings of the Second International Conference on Mathematical Knowledge Management*, LNCS 2594, Heidelberg: Springer-Verlag, pp. 119-132

[^bancerek-2018]: Bancerek, G., C. Byliński, A. Grabowski, A. Korniłowicz, R. Matuszewski, A. Naumowicz and K. Pąk, 2018, “The Role of the Mizar Mathematical Library for Interactive Proof Development in Mizar”, *Journal of Automated Reasoning (Special Issue: Milestones in Interactive Theorem Proving)*, 61 (9): 9–31.

[^barret-2013]: Barret C., M. Deters, L. de Moura, A. Oliveras and A. Stump, 2013, “6 Years of SMT-COMP”, *Journal of Automated Reasoning*, 50 (3): 243–277.

[^basin-1996]: Basin, D. A. and T. Walsh, 1996, “A Calculus for and Termination of Rippling”, *Journal of Automated Reasoning*, 16 (1–2): 147–180.

[^bauer-1998]: Bauer, A., E. Clarke and X. Zhao, 1998, “Analytica: An Experiment in Combining Theorem Proving and Symbolic Computation”, *Journal of Automated Reasoning*, 21: 295–325.

[^beckert-2007]: Beckert, B., R. Hanle and P.H. Schmitt (eds.), 2007, “Verification of Object-Oriented Software: The KeY Approach”, *Lecture Notes in Artificial Intelligence* (Volume 4334), Berlin: Springer-Verlag.

[^beeson-2001]: Beeson M., 2001, “Automatic Derivation of the Irrationality of e”, *Journal of Symbolic Computation*, 32 (4): 333–349.

[^beeson-2017]: Beeson,M. and L. Wos, 2017, “Finding Proofs in Tarskian Geometry”, *Journal of Automated Reasoning*, 58 (1), 181–207.

[^bentkamp-2019]: Bentkamp, A., J.C. Blanchette and D. Klakow, 2019, “A Formal Proof of the Expressiveness of Deep Learning”, *Journal of Automated Reasoning*, 63 (2), 347–368.

[^bentkamp-2021]: Bentkamp, A., J. Blanchette, S. Tourret, P. Vukmirovi&cacute; and U. Waldmann, 2021, “Superposition with Lambdas”, *Journal of Automated Reasoning*, 65 (7), 893–940.

[^benzmüller-2019]: Benzmüller, C., 2019, “Universal (Meta-) Logical Reasoning: Recent Successes”, *Science of Computer Programming*, Vol. 172, 48–62.

[^benzmüller-2014]: Benzmüller, C. and B. W. Paleo, 2014, “Automating Gödel’s Ontological Proof of God’s Existence with Higher-Order Automated Theorem Provers”, *ECAI 2014: Proceedings of the 21st European Conference on Artificial Intelligence*, T. Schaub *et al*. (eds.), IOS Press, pp. 93–98.

[^benzmüller-2015]: –––, 2015, “Higher-Order Modal Logics: Automation and Applications”, *Reasoning Web 2015*, LNCS 9203, W. Faber and A. Paschke (eds.), pp. 32–74.

[^benzmüller-2018]: Benzmüller C., X. Parent and L. van der Torre, 2018, “A Deontic Logic Reasoning Infrastructure”, *CiE2018: Proceedings of the 14th Conference on Computability in Europe*, LNCS 10936, F. Manea *et al*. (eds.), pp. 60–69.

[^benzmüller-2013]: Benzmüller C. and L. C. Paulson, 2013, “Quantified Multimodal Logics in Simple Type Theory”, *Logica Universalis*, 7 (1): 7–20.

[^benzmüller-2020]: Benzmüller, C. and D. S. Scott, 2020, “Automating Free Logic in HOL, with an Experimental Application in Category Theory”, *Journal of Automated Reasoning*, 64 (1), 53–72.

[^benzmüller-2017]: Benzmüller, C., A. Steen and M. Wisniewski, 2017, “Leo-III version 1.1 (system description)”, *Logic for Programming, Artificial Intelligence, and Reasoning (LPAR)—Short Papers*, T. Eiter, D. Sands, G. Sutcliffe and A. Voronkov (eds.), Kalpa Publications in Computing, Volume 1: 11–26.

[^benzmüller-2015-2]: Benzmüller, C., N. Sultana, L. C. Paulson and F. Theiß, 2015, “The Higher-Order Prover LEO-II”, *Journal of Automated Reasoning*, 55 (4): 389–404.

[^berndt-1985]: Berndt, B., 1985, *Ramanujan’s Notebooks* (Part I), Berlin: Springer-Verlag, pp. 25-43.

[^beyer-2018]: Beyer, D., M. Dangl and P. Wendler, 2018, “A Unifying View on SMT-Based Software Verification”, *Journal of Automated Reasoning*, 60 (3): 299–335.

[^beyer-2021]: Beyer, D., M. Dangl and P. Wendler, 2021, “Correction to: A Unifying View on SMT-Based Software Verification”, *Journal of Automated Reasoning*, 65 (3): 461.

[^bibel-1981]: Bibel, W., 1981, “On Matrices with Connections”, *Journal of the Association of Computing Machinery*, 28 (4): 633–645.

[^blanchette-2013]: Blanchette, J. C., S. Böhme and L. C. Paulson, 2013, “Extending Sledgehammer with SMT Solvers”, *Journal of Automated Reasoning*, 51 (1): 109–128.

[^blanchette-2010]: Blanchette, J. C. and T. Nipkow, 2010, “Nitpick: A Counterexample Generator for Higher-Order Logic Based on a Relational Model Finder”, *ITP2010: First International Conference on Interactive Theorem Proving*, LNCS 6172, M. Kaufmann and L. C. Paulson (eds.), pp. 131–146.

[^bledsoe-1977]: Bledsoe, W. W., 1977, “Non-resolution Theorem Proving”, *Artificial Intelligence*, 9: 1–35.

[^bledsoe-1975]: Bledsoe, W. W. and M. Tyson, 1975, “The UT Interactive Prover”, *Memo ATP-17A*, Department of Mathematics, University of Texas.

[^boender-2015]: Boender, J., F. Kammüller and R. Nagarajan, 2015, “Formalization of Quantum Protocols using Coq”, in *EPTCS 195: 12th International Workshop on Quantum Physics and Logic (QPL)*, Chris Heunen, Peter Selinger, and Jamie Vicary (eds.), pp. 71–83. doi:10.4204/EPTCS.195.6

[^bofill-2008]: Bofill, M., R. Nieuwenhuis, A. Oliveras, E. Rodriguez-Carbonell and A. Rubio, 2008, “A Write-Based Solver for SAT Modulo the Theory of Arrays”, *Formal Methods in Computer-Aided Design (FMCAD’08)*, pp. 1–8.

[^bonacina-1999]: Bonacina, M. P., 1999, “A Taxonomy of Theorem-Proving Strategies”, *Artificial Intelligence Today*, (Lecture Notes in Computer Science: Volume 1600), Berlin: Springer-Verlag, pp. 43–84.

[^bordg-2021]: Bordg, A., H. Lachnitt and Y. He, 2021, “Certified Quantum Computation in Isabelle/HOL”, *Journal of Automated Reasoning*, 65 (5): 691–709.

[^boyer-1979]: Boyer, R. S. and J. S. Moore, 1979, *A Computational Logic*, New York: Academic Press.

[^boyer-1997]: –––, 1997, “Mechanized Formal Reasoning about Programs and Computing Machines”, *Automated Reasoning and Its Applications*, R. Veroff (ed.), Cambridge, MA: MIT Press, pp. 147–176.

[^boyer-1995]: Boyer, R. S., M. Kaufmann, and J. S. Moore, 1995, “The Boyer-Moore Theorem Prover and its Interactive Enhancement”, *Computers and Mathematics with Applications*, 29: 27–62.

[^boyer-1994]: Boyer R. S., *et al*., 1994, “The QED Manifesto”, *CADE-12: Proceedings of the 12th International Conference on Automated Deduction*, (Lecture Notes in Artificial Intelligence: Volume 814), A. Bundy (ed.), Berlin: Springer-Verlag, pp. 238–251.

[^brakensiek-2022]: Brakensiek, J., M. Heule, J. Mackey and D. Narváez, 2022, “The Resolution of Keller’s Conjecture”, *Journal of Automated Reasoning*, 66 (3): 277–300.

[^bridge-2014]: Bridge, J. P., S. B. Holden and L.C. Paulson, 2014, “Machine Learning for First-Order Theorem Proving”, *Journal of Automated Reasoning*, 53 (2), 141–172.

[^brown-2012]: Brown, C. E., 2012, “Satallax: An Automatic Higher-Order Prover”, *Automated Reasoning: Proceedings of the 6th International Joint Conference on Automated Reasoning (IJCAR 2012)*, LNAI 7364, B. Gramlich *et al*. (eds.), pp. 111–117, Springer-Verlag.

[^brown-2013]: –––, 2013, “Reducing Higher-Order Theorem Proving to a Sequence of SAT Problems”, *Journal of Automated Reasoning*, 51 (1): 57–77.

[^buchberger-2016]: Buchberger B., T. Jebelean, T. Kutsia, A. Maletzky and W. Windsteiger, 2016, “Theorema 2.0: Computer-Assisted Natural-Style Mathematics”, *Journal of Formalized Reasoning*, 9 (1): 149–185.

[^bundy-2011]: Bundy, A., 2011, “Automated theorem proving: a practical tool for the working mathematician?”, *Annals of Mathematics and Artificial Intelligence*, 61 (1): 3–14.

[^bundy-1991]: Bundy, A., F. van Harmelen, J. Hesketh and A. Smaill, 1991, “Experiments with Proof Plans for Induction”, *Journal of Automated Reasoning*, 7 (3): 303–324.

[^bundy-1993]: Bundy, A., A. Stevens, F. van Harmelen, A. Ireland and A. Smaill, 1993, “Rippling: A Heuristic for Guiding Inductive Proofs”, *Artificial Intelligence*, 62: 185–253.

[^buresh-oppenheim-2007]: Buresh-Oppenheim, J. and T. Pitassi, 2007, “The Complexity of Resolution Refinements”, *Journal of Symbolic Logic*, 72 (4): 1336–1352.

[^chan-2019]: Chan, HL. and M. Norrish, 2019, “Classification of Finite Fields with Applications”, *Journal of Automated Reasoning*, 63 (3): 667–693.

[^chang-1973]: Chang, C. L. and R. C. T. Lee, 1973, *Symbolic Logic and Mechanical Theorem Proving*, New York: Academic Press.

[^chou-1987]: Chou, S., 1987, *Mechanical Geometry Theorem Proving*, Dordrecht: Kluwer Academic Publishers.

[^church-1936a]: Church, A., 1936a, “An unsolvable problem of elementary number theory”, *American Journal of Mathematics*, 58 (2): 345–363.

[^church-1936b]: –––, 1936b, “A note on the Entscheidungsproblem”, *Journal of Symbolic Logic*, 1 (1): 40–41.

[^church-1940]: –––, 1940, “A Formulation of the Simple Theory of Types”, *Journal of Symbolic Logic*, 5: 56–68.

[^claessen-2003]: Claessen, K. and N. Sörensson, 2003, “New Techniques that Improve MACE-style Finite Model Finding”, *Proceedings of the CADE-19 Workshop: Model Computation – Principles, Algorithms, Applications*, P. Baumgartner and C. Fermueller (eds.)

[^clarke-1994]: Clarke, E. and X. Zhao, 1994, “Combining Symbolic Computation and Theorem Proving: Some Problems of Ramanujan”, *CADE-12: Proceedings of the 12th International Conference on Automated Deduction*, (Lecture Notes in Artificial Intelligence: Volume 814), A. Bundy (ed.), Berlin: Springer-Verlag, pp. 758-763.

[^clocksin-1981]: Clocksin, W. F. and C. S. Mellish, 1981, *Programming in Prolog*, Berlin: Springer-Verlag.

[^colmerauer-1973]: Colmerauer, A., H. Kanoui, R. Pasero and P. Roussel, 1973, *Un Système de Communication Homme-machine en Français*, Rapport, Groupe Intelligence Artificielle, Université d’Aix Marseille.

[^constable-1986]: Constable, R. L., S. F. Allen, H. M. Bromley, W.R. Cleaveland, J. F. Cremer, R. W. Harper, D. J. Howe, T. B. Knoblock, N. P. Mendler, P. Panangaden, J. T. Sasaki and S. F. Smith, 1986, *Implementing Mathematics with the Nuprl Proof Development System*, Englewood Cliffs, NJ: Prentice Hall.

[^cook-1971]: Cook, S. A., 1971, “The complexity of Theorem-Proving Procedures”, *Proceedings of the 3rd Annual ACM Symposium on Theory of Computing*, New York: Association for Computing Machinery, pp. 151–158.

[^coquand-1988]: Coquand, T. and G. Huet, 1988, “The Calculus of Constructions”, *Information and Computation - Semantics of Data Types*, A. R. Meyer (ed.), 76 (2–3): 95–120.

[^coquand-1988-2]: Coquand, T. and C. Paulin-Mohring, 1988, “Inductively Defined Types”, *COLOG88: Proceedings of the International Conference on Computer Logic*, P. Martin-Löf and G. Mints (eds.), LNCS 417, pp. 50–66.

[^davis-1962]: Davis, M., G. Logemann and D. Loveland, 1962, “A Machine Program for Theorem-Proving”, *Communications of the Association for Computing Machinery*, 5 (7): 394–397.

[^davis-1960]: Davis, M. and H. Putnam, 1960, “A Computing Procedure for Quantification Theory”, *Journal of the Association for Computing Machinery*, 7 (3): 201–215.

[^bruijn-1968]: de Bruijn, N. G., 1968, “Automath, a Language for Mathematics”, in *Automation of Reasoning (Volume 2)*, J. Siekmann and G. Wrighston (eds.), Berlin: Springer-Verlag, 1983, pp. 159–200.

[^moura-2007]: de Moura, L., 2007, “Developing Efficient SMT Solvers”, *Proceedings of the CADE-21 Workshop on Empirically Successful Automated Reasoning in Large Theories*, G. Sutcliffe, J. Urban and S. Schulz (eds.), Bremen.

[^denney-2004]: Denney, E., B. Fischer and J. Schumann, 2004, “Using Automated Theorem Provers to Certify Auto-generated Aerospace Software”, *Automated Reasoning, Second International Joint Conference (IJCAR)* (Lecture Notes in Artificial Intelligence: Volume 3097), D. Basin and M. Rusinowitch (eds.), Berlin: Springer-Verlag, pp. 198-212.

[^denney-2006]: Denney, E., J. Power and K. Tourlas, 2006, “Hiproofs: A Hierarchical Notion of Proof Tree”, *Proceedings of the 21st Annual Conference on Mathematical Foundations of Programming Semantics (MFPS XXI)* (Electronic Notes in Theoretical Computer Science, Vol. 155), pp. 341–359.

[^deutsch-1982]: Deutsch, D., 1982, “Quantum theory, the Church-Turing principle and the universal quantum computer”, *Proceedings of the Royal Society of London A*, 400: 97–117.

[^dieks-1982]: Dieks, D., 1982, “Communication by EPR devices”, *Physics Letters A*, 92: 271–272.

[^eisert-1999]: Eisert, J., M. Wilkens and M. Lewenstein, 1999, “Quantum games and quantum strategies”, *Physical Review Letters*, 83: 3077–3080.

[^eisert-2020]: –––, 2020, “Erratum: quantum games and quantum strategies”, [*Physical Review Letters*, 83: 3077–3080], *Physical Review Letters*, 124: 139901.

[^ernst-2002]: Ernst, Z., B. Fitelson, K. Harris and L. Wos, 2002, “Shortest Axiomatizations of Implicational S4 and S5”, *Notre Dame Journal of Formal Logic*, 43 (3): 169–179.

[^farmer-1993]: Farmer, W. M., J. D. Guttman and F. J. Thayer, 1993, “IMPS: An Interactive Mathematical Proof System”, *Journal of Automated Reasoning*, 11 (2): 213–248.

[^fitelson-2007]: Fitelson B. and E. Zalta, 2007, “Steps Toward a Computational Metaphysics”, *Journal of Philosophical Logic*, 36 (2): 227–247.

[^fitting-1990]: Fitting, M., 1990, *First-Order Logic and Automated Theorem Proving*, Berlin: Springer-Verlag.

[^fitting-2002]: –––, 2002, *Types, Tableaus and Gödel’s God*. Kluwer.

[^fuenmayor-2017]: Fuenmayor, D. and C. Benzmüller, 2017, “Automating Emendations of the Ontological Argument in Intensional Higher-Order Modal Logic”, *KI 2017: Advances in Artificial Intelligence - Proceedings of the 40th Annual German Conference on AI*, LNCS 10505, G. Kern-Isberner *et al*. (eds.), pp. 114-127.

[^furbach-1994]: Furbach , U., 1994, “Theory Reasoning in First Order Calculi”, *Management and Processing of Complex Data Structures*, (Lecture Notes in Computer Science Volume 777), pp. 139–156.

[^furbach-2014]: Furbach, U., C. Schon and F. Stolzenburg, 2014, “Automated Reasoning in Deontic Logic”, *MIWAI2014: Proceedings of the 8th Multi-disciplinary International Workshop on Artificial Intelligence*, LNAI 8875, M. N. Murty *et al*. (eds.), pp. 57–68.

[^ganesalingam-2017]: Ganesalingam, M. and W. T. Gowers, 2017, “A Fully Automatic Theorem Prover with Human-Style Output”, *Journal of Automated Reasoning*, 58 (2): 253–291.

[^ganzinger-2004]: Ganzinger, H., G. Hagen, R. Nieuwenhuis, A. Oliveras, C. Tinelli, 2004, “DPLL(T): Fast Decision Procedures”, *Computer Aided Verification*, (Lecture Notes in Computer Science: Volume 3114), pp. 175–188.

[^gentzen-1935]: Gentzen, G., 1935, “Investigations into Logical Deduction”, in Szabo 1969, pp. 68–131.

[^giarratano-2004]: Giarratano, J. and G. Riley, 2004, *Expert Systems: Principles and Programming*, 4th edition, Boston, MA: PWS Publishing Co.

[^gödel-1970]: Gödel, K., 1970, “Appendix A: Notes in Kurt Gödel’s Hand“, in Sobel 2004, pp. 144–145.

[^gordon-1993]: Gordon, M. J. C. and T. F. Melham, eds., 1993, *Introduction to HOL: A Theorem Proving Environment for Higher Order Logic*, Cambridge: Cambridge University Press.

[^gordon-1979]: Gordon, M. J. C., A. J. Milner and C. P. Wadsworth, 1979, *Edinburgh LCF: A Mechanised Logic of Computation* (LNCS 78), Berlin: Springer-Verlag.

[^gorenstein-1982]: Gorenstein, D., 1982, *Finite Simple Groups: An Introduction to their Classification* (University Series in Mathematics), New York: Plenum Press.

[^green-1969]: Green, C., 1969, “Application of Theorem Proving to Problem Solving”, *IJCAI’69 Proceedings of the 1st international joint conference on Artificial intelligence*, San Francisco: Morgan Kaufmann, pp. 219–239

[^haack-1978]: Haack, S., 1978, *Philosophy of Logics*, Cambridge: Cambridge University Press.

[^hales-2005a]: Hales, T. C., 2005a, “A proof of the Kepler Conjecture”, *Annals of Mathematics*, 162 (3): 1065–1185.

[^hales-2006]: –––, 2006, “Introduction to the Flyspeck Project”, *Dagstuhl Seminar Proceedings 05021: Mathematics, Algorithms, Proofs*, T. Coquand *et al*. (eds.)

[^hales-2015]: Hales, T. C. *et al*., 2015, “A Formal Proof of the Kepler Conjecture”, *arXiv:1501.02.02155 9 [mat.MG]*, Cornell University Library.

[^harrison-2000]: Harrison, J., 2000, “High-Level Verification Using Theorem Proving and Formalized Mathematics”, *CADE-17: Proceedings of the 17th International Conference on Automated Deduction*, (Lecture Notes in Artificial Intelligence: Volume 1831), D. McAllester (ed.), Berlin: Springer-Verlag, pp. 1-6.

[^harrison-2006]: –––, 2006, “Verification: Industrial Applications”, *Proof Technology and Computation*, H. Schwichtenberg and K. Spies (eds.), Amsterdam: IOS Press, pp. 161–205.

[^harrison-2009]: –––, 2009, “Formalizing an Analytic Proof of the Prime Number Theorem”, *Journal of Automated Reasoning (Special Issue: A Festschrift for Michael J. C. Gordon)*, 43 (3): 243–261.

[^harrison-1998]: Harrison, J. and L. Théry, 1998, “A Skeptic’s Approach to Combining HOL and Maple”, *Journal of Automated Reasoning*, 21: 279–294.

[^herbrand-1930]: Herbrand, J., 1930, *Recherches sur la Theorie de la Demonstration*, Travaux de la Societé des Sciences at des Lettres de Varsovie, Classe III, Science Mathématique et Physique, No. 33, 128.

[^heule-2017]: Heule, M. J. H. and O. Kullmann, 2017, “The Science of Brute Force”, *Communications of the ACM*, 60 (8): 70–79.

[^heule-2016]: Heule, M. J. H., O. Kullmann and V. W. Marek, 2016, “Solving and Verifying the Boolean Pythagorean Triples problem via Cube-and-Conquer”, *Theory and Applications of Satisfiability Testing — SAT 2016, 19th International Conference*, LNCS 9710, N. Creignou and D. Le Berre (eds.), pp. 228–245.

[^hilbert-1928]: Hilbert, D. and W. Ackermann, 1928, *Principles of Mathematical Logic*, L. Hammond, G. Leckie, and F. Steinhardt (trans.), New York: Chelsea Publishing Co., 1950.

[^huet-1975]: Huet, G. P., 1975, “A Unification Algorithm for Typed *λ*-calculus”, *Theoretical Computer Science*, 1: 27–57.

[^hunt-2017]: Hunt Jr., W. A., M. Kaufmann, J. S. Moore and A. Slobodova, 2017, “Industrial Hardware and Software Verification with ACL2”, *Philosophical Transactions of the Royal Society A*, 375: 20150399.

[^kaliszyk-2014]: Kaliszyk, C. and J. Urban, 2014, “Learning-Assisted Automated Reasoning with Flyspeck”, *Journal of Automated Reasoning*, 53 (2), 173–213.

[^kanckos-2017]: Kanckos, A., and B. W. Paleo, 2017, “Variants of Gödel’s Ontological Proof in a Natural Deduction Calculus”, *Studia Logica*, (3): 553–586.

[^kaufmann-1996]: Kaufmann, M. and J. S. Moore, 1996, “ACL2: An industrial strength version of Nqthm”, *Proceedings of the 11th Annual Conference on Computer Assurance (COMPASS-96)*, IEEE Computer Society, pp. 23–34.

[^kerber-1998]: Kerber, M., Kohlhase and V. Sorge, 1998, “Integrating Computer Algebra into Proof Planning”, *Journal of Automated Reasoning*, 21: 327–355.

[^kirchner-2017]: Kirchner, D., 2017, “Representation and Partial Automation of the Principia Logico-Metaphysica in Isabelle/HOL”, *Archive of Formal Proofs*. Formal proof development. ISSN: 2150–914x. URL: http://isa-afp.org/entries/PLM.html.

[^kirchner-2021]: –––, 2021, *Computer-Verified Foundations of Metaphysics and an Ontology of Natural Numbers in Isabelle/HOL*, Ph.D. Dissertation, Fachbereich Mathematik und Informatik, Freie Universität Berlin.

[^kirchner-2019]: Kirchner, D., C. Benzmüller and E. Zalta, 2019, “Computer Science and Metaphysics: A Cross-Fertilization”, *Open Philosophy*, 2: 230–251.

[^kirchner-2020]: –––, 2020, “Mechanizing Principia Logico-Metaphysica in Functional Type Theory", *Review of Symbolic Logic*, 13 (1): 206–18.

[^knuth-1970]: Knuth, D. and P. B. Bendix, 1970, “Simple Word Problems in Universal Algebras”, in *Computational Problems in Abstract Algebra*, J. Leech (ed.), Oxford, New York: Pergamon Press, pp. 263–297.

[^kleene-1962]: Kleene, S. C., 1962, *Introduction to Metamathematics*, Amsterdam: North-Holland.

[^kovács-2013]: Kovács, L. and A. Voronkov, 2013, “First-Order Theorem Proving and VAMPIRE”, *CAV 2013: Proceedings of the International Conference on Computer Aided Verification*, N. Sharygina and H. Veith (eds.), LNCS 8044, pp. 1–35.

[^kowalski-1974]: Kowalski, R., 1974, “Predicate Logic as a Programming Language”, *Proceedings of the International Federation for Information Processing* (Proc. IFIP ’74), Amsterdam: North Holland, pp. 569–574.

[^küchlin-2000]: Küchlin, W. and C. Sinz, 2000, “Proving Consistency Assertions for Automotive Product Data Management”, *Journal of Automated Reasoning* (Special Issue: Satisfiability in the Year 2000), I. P. Gent and T. Walsh (eds.), 24 (1–2): 145–163.

[^kühlwein-2012]: Kühlwein, D., T. van Laarhoven, E. Tsivtsivadze, J. Urban and T. Heskes, 2012, “Overview and Evaluation of Premise Selection Techniques for Large Theory Mathematics”, *Automated Reasoning: 6th International Joint Conference, IJCAR 2012*, (Lecture Notes in Computer Science: Volume 7364), B. Gramlich, D. Miller and U. Sattler (eds.), Manchester, UK: Springer-Verlag, pp. 378–392.

[^lambán-2012]: Lambán, L., F. J. Martín-Mateos, J. Rubio, and J. L. Ruiz-Reina, 2012, “Formalization of a Normalization Theorem in Simplicial Topology”, *Annals of Mathematics and Artificial Intelligence*, 64 (1): 1–37.

[^lemmon-1957]: Lemmon, E. J., C. A. Meredith, D. Meredith, A. N. Prioir and I. Thomas, 1957, *Calculi of Pure Strict Implication*, Philosophy Dept., Canterbury University, Christchurch, New Zealand.

[^lloyd-1984]: Lloyd, J. W., 1984, *Foundations of Logic Programming*, Berlin: Springer-Verlag.

[^loveland-1969]: Loveland, D. W., 1969, “A Simplified Format for the Model Elimination Procedure”, *Journal of the Association for Computing Machinery*, 16: 349–363.

[^loveland-1970]: –––, 1970, “A Linear Format for Resolution”, *Proceedings of the IRIA Symposium on Automatic Demonstration*, New York: Springer-Verlag, pp. 147-162.

[^loveland-1978]: –––, 1978, *Automated Theorem Proving: A Logical Basis*, Amsterdam: North Holland.

[^luckham-1970]: Luckham, D., 1970, “Refinements in Resolution Theory”, *Proceedings of the IRIA Symposium on Automatic Demonstration*, New York: Springer-Verlag, pp. 163-190.

[^maggesi-2018]: Maggesi, M., 2018, “A Formalization of Metric Spaces in HOL Light”, *Journal of Automated Reasoning*, 60 (2): 237–254.

[^martin-löf-1982]: Martin-Löf, P., 1982, “Constructive Mathematics and Computer Programming”, *Logic, Methodology and Philosophy of Science* (Volume IV), Amsterdam: North-Holland, pp. 153-175.

[^massacci-2000]: Massacci, F. and L. Marraro, 2000, “Logical Cryptanalysis: Encoding and Analysis of the U.S. Data Encryption Standard”, *Journal of Automated Reasoning* (Special Issue: Satisfiability in the Year 2000), I. P. Gent and T. Walsh (eds.), 24 (1–2): 165–203.

[^mccarthy-1962]: McCarthy, J., 1962, “Towards a Mathematical Science of Computation”, *International Federation for Information Processing Congress* (Munich, 1962), Amsterdam: North Holland, pp. 21–28.

[^mccharen-1976]: McCharen, J. D., R. A. Overbeek and L. A. Wos, 1976, “Problems and Experiments for and with Automated Theorem-Proving Programs”, *IEEE Transactions on Computers* 8: 773–782.

[^mccune-1997]: McCune, W., 1997, “Solution of the Robbins Problem”, *Journal of Automated Reasoning*, 19 (3): 263–276.

[^mccune-2001]: –––, 2001, *MACE 2.0 Reference Manual and Guide*, Mathematics and Computer Science Division, ANL/MSC-TM-249, Argonne National Laboratory.

[^mcrobie-1991]: McRobie, M. A., 1991, “Automated Reasoning and Nonclassical Logics: Introduction”, *Journal of Automated Reasoning*, 7 (4): 447–451.

[^medina-bulo-2010]: Medina-Bulo, I., F. Palomo-Lozano and J. Ruiz-Reina, 2010, “A Verified Common Lisp Implementation of Buchberger’s Algorithm in ACL2”, *Journal of Symbolic Computation*, 45 (1): 96–123.

[^meng-2008]: Meng, J. and L. C. Paulson, 2008, “Translating higher-order clauses to first-order clauses”, *Journal of Automated Reasoning*, 40 (1): 35–60.

[^meredith-1964]: Meredith, C. A. and A. N. Prior, 1964, “Investigations into Implicational S5”, *Z. Math. Logik Grundlagen Math.*, 10:203–220.

[^meyer-2014]: Meyer, J.-J. Ch., 2014, “Logics for Intelligent Agents and Multi-Agent Systems”, *Handbook of the History of Logic, Volume 9: Computational Logic*, J. Siekmann (ed.), pp. 629–658, Elsevier.

[^miller-1988]: Miller, D. and G. Nadathur, 1988, “An Overview of *λ*Prolog”, *Proceedings of the Fifth International Logic Programming Conference — Fifth Symposium in Logic Programming*, R. Bowen and R. Kowalski (eds.), Cambridge, MA: MIT Press.

[^minker-2014]: Minker, J., D. Seipel and C. Zaniolo, 2014, “Logic and Databases: A History of Deductive Databases”, *Handbook of the History of Logic, Volume 9: Computational Logic*, J. Siekmann (ed.), pp. 571–627, Elsevier.

[^muzalewski-1993]: Muzalewski, M., 1993, *An Outline of PC Mizar*, Fondation Philippe le Hodey, Brussels.

[^nipkow-2002]: Nipkow, T., L. C. Paulson and M. Wenzel, 2002, “Isabelle/HOL: A Proof Assistant for Higher-Order Logic“, LNCS Vol. 2283, pp. 207–208.

[^nivens-1974]: Nivens, A. J., 1974, “A Human-Oriented Logic for Automatic Theorem Proving”, *Journal of the Association of Computing Machinery*, 21 (4): 606–621.

[^oppenheimer-2011]: Oppenheimer, P. and E. Zalta, 2011, “A Computationally-Discovered Simplification of the Ontological Argument”, *Australasian Journal of Philosophy*, 89 (2): 333–349.

[^paulson-1990]: Paulson, L. C., 1990, “Isabelle: The Next 700 Theorem Provers”, *Logic and Computer Science*, P. Odifreddi (ed.), Academic Press, pp. 361–386.

[^paulson-1994]: –––, 1994, *Isabelle: A Generic Theorem Prover* (Lecture Notes in Computer Science: Volume 828), Berlin: Springer-Verlag.

[^paulson-2010]: –––, 2010. “Three Years of Experience with Sledgehammer, a Practical Link Between Automatic and Interactive Theorem Provers”, *PAAR-2010*, B. Konev *et al*. (eds.), pp. 1–10.

[^paulson-1996]: Paulson, L. C. and K. Grabczewski, 1996, “Mechanizing Set Theory”, *Journal of Automated Reasoning*, 17 (3): 291–323.

[^pease-2007]: Pease, A. and G. Sutcliffe, 2007, “First Order Reasoning on a Large Ontology”, *Proceedings of the CADE-21 Workshop on Empirically Successful Automated Reasoning in Large Theories* (Volume 257), G. Sutcliffe and J. Urban (eds.), Bremen.

[^pelletier-1986]: Pelletier, F. J., 1986, “Seventy-Five Problems for Testing Automatic Theorem Provers”, *Journal of Automated Reasoning*, 2 (2): 191–216.

[^pelletier-1998]: –––, 1998, “Natural Deduction Theorem Proving in THINKER”, *Studia Logica*, 60 (1): 3–43.

[^pelletier-2017]: Pelletier, F. J., G. Sutcliffe and A. P. Hazen, 2017, “Automated Reasoning for the Dialetheic Logic RM3”, *Proceedings of the Thirtieth International Florida Artificial Intelligence Research Society Conference*, V. Rus and Z. Markov (eds.), pp. 110–115.

[^pelletier-2002]: Pelletier, F. J., G. Sutcliffe, and C. Suttner, 2002, “The Development of CASC”, *AI Communications*, 15 (2–3): 79–90.

[^peterson-1977]: Peterson, J. G., 1977, *The Possible Shortest Single Axiom for EC-Tautologies*, Report 105, Department of Mathematics, University of Auckland.

[^pollock-1989]: Pollock, J., 1989, “OSCAR: A General Theory of Rationality”, *Journal of Experimental & Theoretical Artificial Intelligence*, 1 (3): 209–226

[^pollock-1995]: –––, 1995, *Cognitive Carpentry*, Cambridge, MA: Bradford/MIT Press.

[^pollock-2006]: –––, 2006, “Against Optimality: Logical Foundations for Decision-Theoretic Planning in Autonomous Agents”, *Computational Intelligence*, 22(1): 1–25.

[^portoraro-1994]: Portoraro, F. D., 1994, “Symlog: Automated Advice in Fitch-style Proof Construction”, *CADE-12: Proceedings of the 12th International Conference on Automated Deduction*, (Lecture Notes in Artificial Intelligence: Volume 814), A. Bundy (ed.), Berlin: Springer-Verlag, pp. 802-806.

[^portoraro-1998]: –––, 1998, “Strategic Construction of Fitch-style Proofs”, *Studia Logica*, 60 (1): 45–66.

[^prasad-2005]: Prasad, M., A. Biere and A. Gupta, 2005, “A Survey of Recent Advances in SAT-Based Formal Verification”, *International Journal on Software Tools for Technology Transfer*, 7 (2): 156–173.

[^prawitz-1965]: Prawitz, D., 1965, *Natural Deduction: A Proof Theoretical Study*, Stockholm: Almqvist & Wiksell.

[^quaife-1992]: Quaife, A., 1992, *Automated Development of Fundamental Mathematical Theories*, Kluwer Academic Publishers.

[^robinson-1965]: Robinson, J. A., 1965, “A Machine Oriented Logic Based on the Resolution Principle”, *Journal of the Association of Computing Machinery*, 12: 23–41.

[^robinson-1965-2]: –––, 1965, “Automatic Deduction with Hyper-resolution”, *Internat. J. Comput. Math.*, 1: 227–234.

[^robinson-2001]: Robinson, J. A. and A. Voronkov (eds.), 2001, *Handbook of Automated Reasoning: Volumes I and II*, Cambridge, MA: MIT Press.

[^russinoff-2017]: Russinoff, D. M., 2017, “A Computationally Surveyable Proof of the Group Properties of an Elliptic Curve”, *Proceedings of the 14th International Workshop on the ACL2 Theorem Prover and Its Applications*, W. Hunt Jr. and A. Slobodova (eds.), Open Publishing Association (EPTCS 249), pp. 30–46.

[^russinoff-2023]: –––, 2023, “A Formalization of Finite Group Theory: Part III”, *Proceedings of the 18th International Workshop on the ACL2 Theorem Prover and Its Applications*, A. Coglio and S. Swords (eds.), Open Publishing Association (EPTCS 393), pp. 33–49.

[^schmitt-2007]: Schmitt, P. and I. Tonin, 2007, “Verifying the Mondex Case Study”, *Proceedings of the Fifth IEEE International Conference on Software Engineering and Formal Methods*, IEEE Computer Society, pp. 47–58.

[^schulz-2004]: Schulz, S., 2004, “System Abstract: E 0.81”, *Proceedings of the 2nd International Joint Conference on Automated Reasoning* (Lecture Notes in Artificial Intelligence: Volume 3097), D. Basin and M. Rusinowitch (eds.), Berlin: Springer-Verlag, pp.223-228.

[^scott-1972]: Scott, D., 1972, “Appendix B: Notes in Dana Scott’s Hand”, in Sobel 2004, pp. 145–146.

[^sieg-1996]: Sieg, W. and J. Byrnes, 1996, *Normal Natural Deduction Proofs (in Classical Logic)*, Report CMU-PHIL 74, Department of Philosophy, Carnegie-Mellon University.

[^slaney-1984]: Slaney, J. K., 1984, “3,088 Varieties: A Solution to the Ackerman Constant Problem”, *Journal of Symbolic Logic*, 50: 487–501.

[^sobel-2004]: Sobel, J. H., 2004, *Logic and Theism: Arguments for and Against Beliefs in God*, Cambridge University Press.

[^steen-2021]: Steen, A. and C. Benzmüller, 2021, “Extensional Higher-Order Paramodulation in Leo-III”, *Journal of Automated Reasoning*, 65 (6): 775–807.

[^stickel-1992]: Stickel, M. E., 1992, “A Prolog Technology Theorem Prover: A New Exposition and Implementation in Prolog”, *Theoretical Computer Science*, 104: 109–128.

[^suppes-1981]: Suppes, P., *et al*., 1981, “Part I: Interactive Theorem Proving in CAI Courses”, *University-Level Computer-Assisted Instruction at Stanford: 1968–1980*, P. Suppes (ed.), Institute for the Mathematical Study of the Social Sciences, Stanford University.

[^sutcliffe-2017]: Sutcliffe, G., 2017, “The TPTP Problem Library and Associated Infrastructure”, *Journal of Automated Reasoning*, 59 (4): 483–502.

[^sutcliffe-2010]: Sutcliffe, G. and C. Benzmüller, 2010, “Automated Reasoning in Higher-Order Logic Using TPTP THF Infrastructure”, *Journal of Formalized Reasoning*, 43 (4): 337–362.

[^sutcliffe-1998]: Sutcliffe, G. and C. Suttner, 1998, “The TPTP Problem Library – CNF Release v1.2.1”, *Journal of Automated Reasoning*, 21 (2): 177–203.

[^szabo-1969]: Szabo, M. E. (ed.), 1969, *The Collected Papers of Gerhard Gentzen*, Amsterdam: North-Holland.

[^trybulec-1978]: Trybulec, A., 1978, “The Mizar Logic Information Language”, *Bulletin of the Association for Literary Linguistic Computing*, 6(2): 136–140.

[^trybulec-1985]: Trybulec, A. and H. Blair, 1985, “Computer Assisted Reasoning with Mizar”, *Proceedings of the 9th International Joint Conference on Artificial Intelligence*, (IJCAI-85: Volume 1), Los Angeles, pp. 26–28.

[^turing-1936]: Turing, A., 1936, “On computable numbers, with an application to the Entscheidungsproblem”, *Proceedings of the London Mathematical Society*, 42 (2): 230–265.

[^urban-2007]: Urban, J., 2007, “MaLARea: A Metasystem for Automated Reasoning in Large Theories”, *Proceedings of the CADE-21 Workshop on Empirically Successful Automated Reasoning in Large Theories*, J. Urban, G. Sutcliffe and S. Schulz (eds.), pp. 45–58.

[^urban-2010]: Urban, J., K. Hoder, A. Voronkov, 2010, “Evaluation of Automated Theorem Proving on the Mizar Mathematical Library”, *Mathematical Software – ICMS 2010: Proceedings of the Third International Congress on Mathematical Software*, Kobe, Japan, (Lecture Notes in Computer Science, Volume 6327), pp. 155–166.

[^urban-2012]: Urban, J. and J. Vyskocil, 2012, “Theorem Proving in Large Formal Mathematics as an Emerging AI Field”, *arXiv:1209.3914 [cs.AI]*, Report No. DPA-12271, Cornell University.

[^urquhart-1987]: Urquhart, A., 1987, “Hard Examples for Resolution”, *Journal of the ACM*, 34 (1): 209–219.

[^urquhart-1994]: –––, 1994 (ed.), *The Collected Papers of Bertrand Russell, Volume 4: Foundations of Logic, 1903-05*, Routledge, London and New York.

[^benthem-1977]: van Benthem Jutting, L. S., 1977, *Checking Landau’s “Grundlagen” in the Automath system*, Ph.D. Thesis, Eindhoven University of Technology; published in *Mathematical Centre Tracts*, Number 83, Amsterdam: Mathematisch Centrum, 1979.

[^voronkov-1995]: Voronkov, A., 1995, “The Anatomy of Vampire: Implementing Bottom-Up Procedures with Code Trees”, *Journal of Automated Reasoning*, 15 (2): 237–265.

[^wallen-1990]: Wallen, L. A., 1990, *Automated Deduction in Nonclassical Logics*, Cambridge, MA: MIT Press.

[^wang-1960]: Wang, H., 1960, “Proving Theorems by Pattern Recognition – I”, in *Automation of Reasoning (Volume 1)*, J. Siekmann and G. Wrightson (eds.), Berlin: Springer-Verlag, 1983, pp. 229–243.

[^wang-1960-2]: –––, 1960, “Toward Mechanical Mathematics”, in *Automation of Reasoning* (Volume 1), J. Siekmann and G. Wrightson (eds.), Berlin: Springer-Verlag, 1983, pp. 244-264.

[^wegner-2011]: Wegner, B., 2011, “Completeness of reference databases, old-fashioned or not?”, *Newsletter of the European Mathematical Society*, 80: 50–52.

[^wiedijk-2006]: Wiedijk, F., 2006, *The Seventeen Provers of the World*, (Lecture Notes in Artificial Intelligence: Volume 3600), F. Wiedijk (ed.), New York: Springer-Verlag.

[^wiedijk-2007]: –––, 2007, “The QED Manifesto Revisited”, *Studies in Logic, Grammar and Rhetoric*, 10 (23): 121–133.

[^wooters-1982]: Wooters, W.K. and W. H. Zurek, 1982, “A single quantum cannot be cloned”, *Nature*, 299: 802–803.

[^wos-2001]: Wos, L. (ed.), 2001, *Journal of Automated Reasoning* (Special Issue: Advances in Logic Through Automated Reasoning), 27 (2).

[^wos-1965]: Wos, L., D. Carson and G. R. Robinson, 1965, “Efficiency and Completeness of the Set of Support Strategy in Theorem Proving”, *Journal of the Association of Computing Machinery*, 12: 698–709.

[^wos-1984]: Wos, L., R. Overbeek, E. Lusk and J. Boyle, 1984, *Automated Reasoning: Introduction and Applications*, Englewood Cliffs, NJ: Prentice-Hall.

[^wos-2002]: Wos, L., D. Ulrich, and B. Fitelson, 2002, “Vanquishing the XCB Question; The Methodological Discovery of the Last Shortest Single Axiom for the Equivalential Calculus”, *Journal of Automated Reasoning*, 29 (2):107–124.

[^wos-1983]: Wos, L., S. Winker, R. Veroff, B. Smith and L. Henschen, 1983, “Questions Concerning Possible Shortest Single Axiom for the Equivalential Calculus: An Application of Automated Theorem Proving to Infinite Domains”, *Notre Dame Journal of Formal Logic*, 24: 205–223.

[^yoo-2009]: Yoo, J., E. Jee and S. Cha, 2009, “Formal Modeling and Verification of Safety-Critical Software”, *IEEE Software*, 26 (3): 42–49.

[^zalta-1983]: Zalta, E., 1983, *Abstract Objects: An Introduction to Axiomatic Metaphysics*, Synthese Library, SYLI Volume 160, Springer.

[^zalta-1999]: –––, 1999, “Natural Numbers and Natural Cardinals as Abstract Objects: A Partial Reconstruction of Frege’s Grundgesetze in Object Theory”, *Journal of Philosophical Logic*, 28 (6): 619–660.

[^zalta-2018]: –––, 2018, “How Computational Investigations Improved an Ontology”, *2018 Annual Meeting of the International Association for Computing and Philosophy*, Warsaw, Polska Akademia Nauk (PAN), Copernicus Center,

[^zalta-2022]: –––, 2022, *Principia Logico-Metaphysica*, Draft/Excerpt dated September 2, 2022, URL: https://mally.stanford.edu/principia.pdf

[^zhang-2002]: Zhang, L. and S. Malik, 2002, “The Quest for Efficient Boolean Satisfiability Solvers”, *CADE-18: Proceedings of the 18th International Conference on Automated Deduction*, (Lecture Notes in Artificial Intelligence: Volume 2392), A. Voronkov (ed.), Berlin: Springer-Verlag, pp. 295-313.
