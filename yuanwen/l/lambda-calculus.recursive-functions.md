# lambda-calculus — recursive-functions（supplement）

> （《lambda-calculus》词条补充材料，源：plato.stanford.edu/entries/lambda-calculus/recursive-functions.html）

#### Supplement to The Lambda Calculus

## Appendix on Recursive Functions

To show that all recursive functions can be represented in the $\lambda$-calculus, one reproduces the definition of recursive functions in the $\lambda$-calculus. We recall the definition.

**Definition** The class of *recursive functions* is the (smallest) class of functions from natural numbers to natural numbers that contains:

*The initial functions*

| Name | Definition | Condition |
| --- | --- | --- |
| $Z$ | $Z(n) = 0$ |   |
| $S$ | $S(x) = x + 1$ |   |
| $U_{n,k}$ | $U_{n,k}(x_1 ,\ldots x_n) = x_k$ | $n \ge 1$ and $1 \le k \le n$ |

and is closed under the operations of:

- *substitution/composition*: if $G$ and $H$ are recursive functions, and if the numeric function $F$ satisfies the relation: there is a $k$ such that for all $x_1 ,\ldots ,x_n$: $F(x_1 ,\ldots ,x_n) = H(x_1 ,\ldots x_{k-1},G(x_1 ,\ldots x_n),x_{k+1},\ldots x_m)$, then $F$ is a recursive function.
- *definition by primitive recursion*: if $G$ and $H$ are recursive functions, and if the numeric function $F$ satisfies the relations:
- for all $x_1 ,\ldots ,x_n$: $F(x_1 ,\ldots ,x_n,0) = G(x_1 ,\ldots ,x_n)$
- for all k and all $x_1 ,\ldots ,x_n$: $F(x_1 ,\ldots ,x_n,k + 1) = H(x_1 ,\ldots ,x_n,k,F(x_1 ,\ldots ,x_n,k))$ then $F$ is a recursive function.
- *minimalization*: if $G$ is a recursive function, and if the numeric function $F$ satisfies the relation
- $F(x_1 ,\ldots ,x_n) = y$ iff $G(x_1 ,\ldots ,x_n,y) = 1$ and for all $x \lt y$ we have $G(x_1 ,\ldots ,x_n,x) = 0$ then $F$ is a recursive function.

Say that a number-theoretic function $f$ of arity $n$ is **$\lambda$-definable** if there exists a $\lambda$-term $F$ with the property that for every natural number $a$ and for every $n$-tuple $(a_1 ,\ldots a_n)$ of natural numbers, we have

$$ f(a_1 ,\ldots a_n) = a \text{ iff } \lambda \vdash F\ulcorner a_1\urcorner \ldots \ulcorner a_n\urcorner = \ulcorner a\urcorner $$

To show that the class of recursive functions can be represented in the $\lambda$-calculus, one follows its definition; the step-by-step construction of an arbitrary recursive function from the initial functions can be mimicked in the $\lambda$-calculus. One shows first that all initial functions can be represented; then one shows that the operations of substitution/composition, definition by primitive recursion, and minimalization can likewise be expressed. We require, first, a representation of natural numbers in the $\lambda$-calculus. Representing the initial functions and substitution/composition will then be straightforward, but some work is required to show that definition by primitive recursion and minimalization can be adequately represented. The development that follows is standard (Barendregt, 1984).

We begin with a representation of natural numbers as $\lambda$-terms. Define $\ulcorner n\urcorner$ by recursion as:

$$\begin{align} \ulcorner 0\urcorner &= \bI \\ \ulcorner n + 1\urcorner &= \lambda x[x\bF\ulcorner n\urcorner] \end{align}$$

Intuitively, to represent primitive recursion, one ought be able to proceed by cases because one has to test whether an argument is zero (‘base case’) or non-zero (‘recursion case’). One naturally searches for an analogue in the $\lambda$-calculus for an ‘if-then-else’ term-building operation. The $\bB$ combinator accomplishes this. That is, $\bB$ (given our representation of the constant-true and constant-false by the $\lambda$-terms $\bT$ and $\bF$) has the property that

$$ \bB\bT xy = x \text{ and } \bB\bF xy = y $$

for all terms $x$ and $y$. We need, further, $\lambda$-terms representing the number-theoretic operations of successor and predecessor. In other words, we need $\lambda$-terms $\Succ$ (successor), $\Pred$ (predecessor), and $\Zero$ (test for zero) satisfying

$$\begin{align} &\Succ \ulcorner n\urcorner = \ulcorner n + 1\urcorner \\ &\Pred \ulcorner n + 1\urcorner = \ulcorner n\urcorner \\ &\Zero 0 = \bT \\ &\Zero \ulcorner n + 1\urcorner = \bF \end{align}$$

for all natural numbers $n$. With this representation of natural numbers, one can then show that the terms $\Succ, \Pred$, and $\Zero$ defined as

$$\begin{align} \Succ &:= \lambda x[\lambda y[y\bF x]] \\ \Pred &:= \lambda x[x\bF] \\ \Zero &:= \lambda x[x\bT] \end{align}$$

have properties (1)–(4).

Representation of the initial recursive functions in the $\lambda$-calculus

| Function | Representation |
| --- | --- |
| $Z$ | $\lambda$x[$\bI$] |
| $S$ | $\Succ$ |
| $U_{n,k}$ | $\lambda x_1 \ldots \lambda$x$_n$[x$_k$] |

Substitution/composition is represented straightforwardly: given that the $\lambda$-terms $G^*$ and $H^*$ represent the number-theoretic functions $G$ and $H$, the composition of $G$ and $H$ is given simply by

$$ \lambda x_1 \ldots x_n [H^* x_1 \ldots x_{k-1}(G^* x_1 \ldots x_n)x_{k+1}\ldots x_n] $$

The desired representation of definition by primitive recursion is a term $Fxy$ satisfying

$$ Fxy = \ifthenelse \Zero x, Gy, H(\Pred xy,y)) $$

The existence of such a term is settled by a *fixed-point theorem*:

**Theorem** For every term $F$, there exists a term $X$ such that $X = FX$.

(One can use Curry’s ‘paradoxical’ fixed-point combinator $\bY$ for this purpose.) The final task is to represent, in the $\lambda$-calculus, the number-theoretic minimalization operation $\mu$ defined on properties of natural numbers:

$\mu x[\phi(x)] =$ the smallest natural number $n$ for which the number-theoretic property $\phi(n)$ holds

An adequate representation of $\mu$ in the $\lambda$-calculus is defined in stages. Define, for a $\lambda$-term $P$, the two terms $H_P$ and $\mu P$ as

$$\begin{align} H_P &:= \bTheta (\lambda h[\lambda z[\ifthenelse Pz, z, h \Succ z]] \\ \mu P &:= H_P\ulcorner 0\urcorner \end{align}$$

The second clause of the definition can be intuitively understood as computing thus: Does 0 have property $P$? If so, then stop; $\mu P$ is 0. If not, does 1 have property $P$? If so, then 1 is the answer. Proceeding in this fashion, one will eventually stop and the computed value will be $\mu P$. The fixed-point operator **$\Theta$** accomplishes the ‘looping’. One can then show that if $X$ is a $\lambda$-term with the property that

- for all natural numbers $n$: either $P\ulcorner n\urcorner = \bT$ or $P\ulcorner n\urcorner = \bF$

and if there exists a natural number $n$ such that $P\ulcorner n\urcorner = \bT$, then $\mu P$ is the least natural number $m$ such that $P\ulcorner m\urcorner = \bT$. With these ingredients in place, one can then prove the following representation theorem (due to Church):

**Theorem** For every number-theoretic function $f$, we have that $f$ is recursive iff $f$ is $\lambda$-definable.

One can extend the notion of $\lambda$-definability to the wider concept of partial recursive (number-theoretic) functions and prove for that class of functions a result analogous to the preceding theorem.
