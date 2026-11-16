# frege-theorem — rule-substitution（supplement）

> （《frege-theorem》词条补充材料，源：plato.stanford.edu/entries/frege-theorem/rule-substitution.html）

#### Supplement to Frege’s Theorem and Foundations for Arithmetic

## Frege’s Rule of Substitution

In this supplement, we briefly discuss the connection between Frege’s Rule of Substitution and the comprehension principles discussed in the main text. But understanding this connection is not necessary for understanding Frege’s Theorem. The Rule of Substitution is notoriously difficult to formulate correctly. Though we will formulate the rule correctly towards the end, a simplified, though incorrect, formulation of the rule will serve the purpose of getting the main idea across.

**Rule of Substitution** (Simplified Version): In any statement of the form $\ldots Fx\ldots$ (in which the variable $F$ is free) which is derivable as a theorem of logic, we may substitute any open formula $\phi(x)$ (with the free variable $x$) for all the occurrences of the atomic formula $Fx$ in $\ldots Fx\ldots$ .

To see the intent of this rule, first consider the following theorem of (Frege’s) second-order predicate logic:

$$\tag{A} \forall x(Fx \equiv Fx)$$

Now Frege’s Rule of Substitution is intended to allow us to substitute complex formulas with a free variable x for ‘ $Fx$’. So, for example, we are allowed substitute the formula ‘ $Ox \amp x > 5$’ (‘ $x$ is odd and $x$ is greater than $5$’) for ‘ $Fx$’ in (A) to derive the following from (A):

$$\tag{B} \forall x[(Ox \amp x > 5)\equiv (Ox \amp x > 5)]$$

Inferences such as this will be valid no matter what complex formula with $x$ free we substitute for $Fx$ in our universal claim (A). This is the idea behind Frege’s Rule of Substitution.

In what follows, we will assume that the Rule of Substitution can be generalized to relations, so that we can uniformly replace the formula $Rxy$ (in a theorem of logic with $R$ free) by a complex formula $\phi(x,y)$ (in which both $x$ and $y$ are free).

The Rule of Substitution has rather powerful consequences. It implies the Comprehension Principle for Concepts discussed in the main text. To see that this is a consequence of the rule, note that it follows from (A) by existential generalization that:

$\exists G\forall x(Gx\equiv Fx)$

Frege’s Rule of Substitution now allows us to substitute any formula with free variable $x$ for $Fx$. This, in effect, is the Comprehension Principle for Concepts discussed in the main text.

The same facts apply to relations. The following is a theorem of logic, where $S$ is any 2-place relation:

$\forall x\forall y(Sxy \equiv Sxy)$

From this theorem, on can generalize to obtain:

$\exists R\forall x\forall y(Rxy \equiv Sxy)$

From this theorem, Frege could use the Rule of Substitution to derive, for any formula *φ* with free variables $x$ and $y$, the existence of a relation $R$ such that any objects $x$ and $y$ stand in $R$ if and only if *φ*.

In effect, Frege’s Rule of Substitution allows us to instantiate $\phi(x)$ for the free variable $F$ in theorems of logic as if $\phi(x)$ were a *λ*-expression and constituted a name of a concept. Indeed, *λ*-notation helps us to develop a more precise formulation of the Rule of Substitution; the precise formulation of the rule for concepts is:

**Rule of Substitution** (1-place case): In any theorem of logic *ψ* in which $F$ is free, one may uniformly substitute the *λ*-expression $[\lambda x \, \phi(x)]$ for $F$, and then convert all the resulting formulas using *λ*-Conversion, provided $[\lambda x \, \phi(x)]$ is substitutable for $F$ (i.e., provided no variable free in $[\lambda x \, \phi(x)]$ is captured by a quantifier binding that variable in *ψ* when the substitution is made).

(The formulation for relations is similar.) Moreover, the principle of *λ*-Conversion simplifies the strict proof of the equivalence of Frege’s Rule of Substitution and the Comprehension Principle for Concepts. As it turns out, not only does Frege’s Rule of Substitution imply the Comprehension Principle for Concepts, but the converse also holds: the Comprehension Principle for Concepts implies the Rule of Substitution. [For a proof sketch, see Boolos (1985) pp. 161–162. Note that instead of $[\lambda x \, \phi(x)]$, Boolos uses the notation $\{a : Aa\}$; elsewhere, in (1987) for example, Boolos uses the notation $[x : A(x)]$ to denote concepts.]
