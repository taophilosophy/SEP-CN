# logic-if — supplement（supplement）

> （《logic-if》词条补充材料，源：plato.stanford.edu/entries/logic-if/supplement.html）

#### Supplement to Independence Friendly Logic

## Existential second-order logic (a.k.a. $\Sigma^{1}_1$ logic)

The set of *formulas* of existential second-order logic of vocabulary $\tau$ (formulas of $\mathbf{ESO}[\tau]$) is the smallest set containing all formulas of $\mathbf{FO}[\tau]$ and which is closed under the following two rules:

- If $\phi$ is an $\mathbf{ESO}[\tau \cup \{f\}]$ formula, then $(\exists f)\phi$ is an $\mathbf{ESO}[\tau]$ formula.
- If $\phi$ is an $\mathbf{ESO}[\tau \cup \{R\}]$ formula, then $(\exists R)\phi$ is an $\mathbf{ESO}[\tau]$ formula.

*E.g.,* since $(\forall x)R(x, f(x))$ is an $\mathbf{FO}[\{R, f\}]$ formula, we have that $(\exists f)(\forall x)R(x, f(x))$ is an $\mathbf{ESO}[\{R\}]$ formula, and $(\exists R)(\exists f)(\forall x)R(x, f(x))$ is an $\mathbf{ESO}$ formula of empty vocabulary. Observe that no second-order variables are involved in the formulation of the syntax. For instance, what is bound by the second-order quantifier $(\exists f)$ is a function symbol (not a function variable). The notion of a free individual variable can be defined exactly as in the case of $\mathbf{FO}$. An $\mathbf{ESO}[\tau]$ formula is a *sentence* if it contains no free variables. (For this syntax, see *e.g.* Väänänen 2007. For an alternative formulation, see *e.g.* Ebbinghaus & Flum 1999.)

The semantics of $\mathbf{ESO}[\tau]$ is specified by defining the *satisfaction relation* $M, g \vDash \phi$ for all $\mathbf{ESO}[\tau]$ formulas $\phi , \tau$ structures $M$ and variable assignments $g$. The semantic clauses for atomic formulas and for formulas of the forms $\vee$, $\wedge$, $\exists x$, $\forall x$ and ${\sim}$ are as in $\mathbf{FO}$. The remaining semantic clauses make use of the notion of expansion of a $\tau$ structure. A $\tau'$ structure $M'$ is an *expansion* of a $\tau$ structure $M$ (to the vocabulary $\tau')$, if $\tau \subseteq \tau'$, $\rM = \rM'$, and the structures $M$ and $M'$ agree on the interpretations of all symbols of vocabulary $\tau$. So any difference between the structures is due to the interpretations of symbols that belong to $\tau'$ but not to $\tau$.

- $M, g \vDash(\exists f)\phi$ iff there is an expansion $M'$ of the structure $M$ to the vocabulary $\tau \cup \{f\}$ such that $M', g \vDash \phi$.
- $M, g \vDash(\exists R)\phi$ iff there is an expansion $M'$ of the structure $M$ to the vocabulary $\tau \cup \{R\}$ such that $M', g \vDash \phi$.

For example, let $N_1$ be the $\{R\}$ structure whose domain is the set of natural numbers and which interprets ‘$R$’ as the relation *smaller than*. Consider evaluating the $\mathbf{ESO}[\{R\}]$ sentence $(\exists f)(\forall x)R(x, f(x))$ relative to $N_1$. We have

$$ N_1, g \vDash (\exists f)(\forall x)R(x, f(x)), $$

for any assignment $g$, because by interpreting the function symbol ‘$f$’ by the function $n \mapsto n+1,$ an expansion $N_2$ of $N_1$ to the vocabulary $\{R, f\}$ is obtained, with $N_2, g \vDash (\forall x)R(x, f(x))$. The reason why $N_2, g \vDash (\forall x)R(x, f(x))$ holds is that indeed any natural number $n$ is smaller than the natural number $n+1$. And if $N_0$ is a model of empty vocabulary with the set of natural numbers as its domain, we have $N_0, g \vDash (\exists R)(\exists f)(\forall x)R(x, f(x))$, for any assignment $g$, since $N_0$ can be expanded to $N_1$, which is a structure of vocabulary $\{R\}$, and then we have $N_1, g \vDash (\exists f)(\forall x)R(x, f(x))$, as just noted.

## Skolemizations and Skolem normal forms

Let us restrict our attention to $\mathbf{IFL}$ formulas in negation normal form. A skolemization of an $\mathbf{IFL}$ formula will be a *first-order* formula of a larger vocabulary.

In $\mathbf{FO}$, it is customary to effect skolemization only with respect to existential quantifiers; discussing $\mathbf{IFL}$, Hintikka (1991, 1996, 1997) extends skolemization to disjunctions as well. For example, a skolemization of the sentence

$$ (\forall x)(\forall y)(R(x, y) \; (\vee /\forall x) \; S(x, y)) $$

of vocabulary $\{R, S\}$ is the $\mathbf{FO}$ formula

$$ (\forall x)(\forall y)([R(x, y) \wedge d(y) = 0] \vee [S(x, y) \wedge d(y) \ne 0]). $$

of vocabulary $\{R, S, d, 0\}$. Here the function term $d(y)$ is used to explicate the dependence of the choice of a disjunct on the value interpreting the universal quantifier $(\forall y)$. ‘0’ is a fresh constant symbol, standing for some fixed element of the domain. This constant is used for forming the conjuncts $d(y) = 0$ and $d(y) \ne 0$; for those values $a$ of $y$ for which $d(a) = 0$ holds, the left disjunct is chosen, while for those values of $a$ of $y$ for which $d(a) \ne 0$ holds, it is the right disjunct that is chosen.

Let $\tau$ be a fixed vocabulary, and 0 a constant symbol not in $\tau$. If $\phi$ is an $\mathbf{IFL}[\tau]$ formula, its *skolemization* $\mathrm{sk}[\phi]$ is the formula $\mathrm{sk}_{\phi}[\phi]$ that can be computed by the following rules:

- If $\psi$ is any of the formulas $R(t_1 ,\ldots ,t_n)$ or $t_1 = t_2$ or ${\sim}R(t_1 ,\ldots ,t_n)$ or ${\sim}t_1 = t_2$, then $\mathrm{sk}_{\phi}[\psi] = \psi$.
- $\mathrm{sk}_{\phi}[(\psi \; (\vee /\forall y_1 ,\ldots ,\forall y_n) \; \chi)] = (\mathrm{sk}_{\phi}[\psi] \wedge d(z_1 ,\ldots ,z_m) = 0)$ $\vee$ $(\mathrm{sk}_{\phi}[\chi] \wedge d(z_1 ,\ldots ,z_m) \ne 0)$, where $d$ is a fresh function symbol, and $(\forall z_1),\ldots ,(\forall z_m)$ are those universal quantifiers that precede the token of the disjunction sign in $\phi$, but are not among $(\forall y_1),\ldots ,(\forall y_n)$.
- $\mathrm{sk}_{\phi}[(\psi \; (\wedge /\exists y_1 ,\ldots ,\exists y_n) \; \chi)] = (\mathrm{sk}_{\phi}[\psi] \wedge \mathrm{sk}_{\phi}[\chi]$).
- $\mathrm{sk}_{\phi}[(\exists x/\forall y_1 ,\ldots ,\forall y_n)\psi] =$ $\mathrm{sk}_{\phi}[\psi][x/f(z_1 ,\ldots ,z_m)]$, where $f$ is a fresh function symbol, and $(\forall z_1),\ldots ,(\forall z_m)$ are those universal quantifiers that precede the token of the existential quantifier in $\phi$, but are not among $(\forall y_1),\ldots ,(\forall y_n)$.
- $\mathrm{sk}_{\phi}[(\forall x/\exists y_1 ,\ldots ,\exists y_n)\psi] = (\forall x) \mathrm{sk}_{\phi}[\psi]$.

If $\phi$ is a formula, $x$ is a variable, and $t$ is a term, by stipulation $\phi[x/t]$ stands for the formula obtained from $\phi$ by replacing all free occurrences of $x$ in $\phi$ by $t$. This use of the slash sign must not be confused with its use to mark quantifier independence as in IF logic.

Observe that the skolemization $\mathrm{sk}[\phi]$ of an $\mathbf{IFL}$ formula (in negation normal form) is itself an $\mathbf{FO}$ formula in negation normal form, written in a larger vocabulary including as many function symbols as there are tokens of the disjunction sign and tokens of the existential quantifier in $\phi$ – and possibly including also the constant symbol 0. The arities of these function symbols are uniquely determined by the position of the token in the syntactic tree of the formula $\phi$. Note that the interpretations of those function symbols in $\mathrm{sk}[\phi]$ that are triggered by existential quantifiers are nothing other than Skolem functions for those existential quantifiers in the sense specified in *Section* 1.

With the help of the notion of skolemization, the notion of the Skolem normal form of an $\mathbf{IFL}$ formula can be defined. If $\phi$ is a formula of $\mathbf{IFL}[\tau]$, and $\mathrm{sk}[\phi]$ is its skolemization of vocabulary $\tau'$, with $\tau \subseteq \tau'$, the *Skolem normal form* $\mathrm{SK}[\phi]$ of $\phi$ is the $\mathbf{ESO}[\tau]$ formula $\exists f_1 \ldots \exists f_n \mathrm{sk}[\phi]$, where $\{f_1 ,\ldots ,f_n\} = \tau'$ \ $\tau$. Here the set $\{f_1 ,\ldots ,f_n\}$ consists of the function symbols introduced for tokens of the disjunction sign and tokens of the existential quantifier in $\phi$, together with the constant 0 if $\phi$ contains any disjunction tokens.
