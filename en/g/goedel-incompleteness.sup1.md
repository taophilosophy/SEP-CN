# goedel-incompleteness — sup1（supplement）

> （《goedel-incompleteness》词条补充材料，源：plato.stanford.edu/entries/goedel-incompleteness/sup1.html）

#### Supplement to Gödel’s Incompleteness Theorems

## Gödel Numbering

A key method in the usual proofs of the first incompleteness theorem is the arithmetization of the formal language, or *Gödel numbering:* certain natural numbers are assigned to terms, formulas, and proofs of the formal theory $F$. There are different ways of doing this; one standard approach is sketched here (for a rather different method of coding, see, e.g., Boolos & Jeffrey 1989). An essential requirement is that the method is effective, that is, a purely mechanical routine.

The method proceeds in two steps:

### 1. Symbol numbers

To begin with, to each primitive symbol $s$ of the language of the formalized system $F$ at stake, a natural number $\num(s)$, called the *symbol number* of $s$, is attached. It does not matter how and in which order this is done—that is arbitrary—but once it is done, it is obviously kept fixed.

For example, in the case of the standard language of arithmetic, with symbols $0, ', +, \times , =$, (, ), $\neg , \rightarrow , \forall$ (for simplicity, let us assume that $\neg , \rightarrow$ and $\forall$ are the only primitive logical symbols, and that $\wedge , \vee , \leftrightarrow$ and $\exists$ are defined with the help of them), one might proceed, e.g., as follows:

| $\num(\lsq 0\rsq) = 1$ | $\num(\lsq {=}\rsq) = 5$ | $\num(\lsq \neg\rsq) = 9$ |
| --- | --- | --- |
| $\num(\lsq\,'\,\rsq) = 2$ | $\num(\lsq (\rsq ) = 6$ | $\num(\lsq \forall\rsq) = 10$ |
| $\num(\lsq {+}\rsq) = 3$ | $\num(\lsq )\rsq) = 7$ | $\num(\lsq x_i\rsq) = 11 + i$ |
| $\num(\lsq {\times}\rsq) = 4$ | $\num(\lsq {\rightarrow}\rsq) = 8$ |   |

### 2. Coding sequences

Some way of coding finite sequences of numbers by single numbers is also fixed. There are indefinitely many possible ways to achieve that; one common approach (used also originally by Gödel himself) is based on the products of the powers of the prime numbers.

Recall that a *prime number* is a natural number which is greater than 1 and can be divided only by 1 and the number itself (all the other numbers greater than 1 are “composite”). There are infinitely many prime numbers; the beginning of the sequence is 2, 3, 5, 7, 11, 13, 17, …

*The fundamental theorem of arithmetic* (or the unique-prime-factorization theorem) states that any natural number greater than 1 can be written as a unique product (up to ordering of the factors) of prime numbers.

Let then $p_1$ be the first prime number, $p_2$ the second prime number, and so forth. In general, $p_n$ is the $n$-th prime number, and

$$ p_1, p_2 , \ldots ,p_n $$

is the sequence of the first $n$ primes in the increasing order.

Given an arbitrary finite sequence of positive numbers (0 would cause complications) with length $k + 1$, $(n_0, n_1 , \ldots ,n_k)$, it can be uniquely coded as a product of powers of the prime numbers $p_1, p_2 , \ldots ,p_{k+1}$ as follows:

$$ c = 2^{n_0} \times 3^{n_1} \times 5^{n_2} \times \ldots \times p^{n_k}_{k+1}, $$

For example, the sequence $\langle 3, 1, 2\rangle$ is coded as $2^3 \times 3^1 \times 5^2$, that is, $8 \times 3 \times 25$, which equals 600.

#### Combining the two steps:

Given these two methods, it is possible to code an arbitrary expression of the language by a single number: first, replace each symbol $s$ by it symbol number $\num(s)$. This way a sequence of symbols becomes a sequence of numbers. Second, using the above powers of primes coding, associate to this sequence of numbers a unique single number as its code—its “Gödel number”.

For example, take the simple expression $\lsq0 = 0\rsq.$ As it was stipulated above that the symbol numbers of the symbols ‘0’ and ‘=’ are 1 and 5, respectively, the corresponding sequence of the symbol numbers is: $\langle 1, 5, 1\rangle$. The code (that is, the Gödel number) of $\lsq 0 = 0\rsq$ then is:

$$ 2^1 \times 3^5 \times 5^1 = 2 \times 243 \times 5 = 2430. $$

In general, the Gödel number of a formula (sentence, derivation) $A$ is denoted by $\ulcorner A\urcorner$. For example, $\ulcorner 0 = 0\urcorner$ refers, under the coding we have fixed, to 2430.

In this way we can assign Gödel numbers to formulas, sequences of formulas (once a method for distinguishing when one formula ends and another begins has been adopted), and most notably, proofs, or derivations.

We can also go to the other direction: It is an essential part of the method that if a code number is given (many numbers simply do not code anything, but it can be decided which ones do), it is also possible to decode it in a unique way, that is, to reconstruct the unique original expression (or derivation) that it encodes.

For example, let the Gödel number that has been given be 18. The prime factorization of it, which is unique (by the fundamental theorem of arithmetic; see above), can then be determined. It is:

$$ 2^1 \times 3^2 $$

Focusing on the powers, we see that this represents the sequence $\langle 1, 2\rangle$, and recalling the relevant symbol numbers:

$$\begin{align} 1 &= \num(\lsq 0\rsq) \\ 2 &= \num(\lsq\,'\,\rsq) \end{align}$$

it can be seen that the encoded sequence of symbols is $\langle 0, '\rangle$, that is, the expression that is coded by 18 is $\lsq 0'\rsq$.

### 3. Defining syntactical properties and operations

It is then possible to develop the key notions of exact syntax in the arithmetized form, mimicking their ordinary definitions, though the rigorous definitions tend to get a bit complicated. That is, it is possible to define, in an arithmetical language, properties such as:

| $\textit{Const}(x)$ | $x$ is (a Gödel number of) a constant. |
| --- | --- |
| $\textit{Var}(x)$ | $x$ is (a Gödel number of) a variable. |
| $\textit{Term}(x)$ | $x$ is (a Gödel number of) a term. |
| $\textit{Form}(x)$ | $x$ is (a Gödel number of) a formula. |

The following operations on (the Gödel numbers of) formulas can also be easily defined in the language of arithmetic:

$\textit{neg}(x)$   the arithmetical function that sends the Gödel number of a formula to the Gödel number of its negation: $$ \textit{neg}(\ulcorner A\urcorner) = (\ulcorner \neg A\urcorner); $$ $\textit{impl}(x, y)$   the function which maps the Gödel numbers of a pair of formulas to the Gödel number of the implication of the formulas: $$ \textit{impl}(\ulcorner A\urcorner , \ulcorner B\urcorner) = \ulcorner A \rightarrow B\urcorner; $$

Given that $y$ ($z$) is (a Gödel number of) a formula, the following syntactic relations can be also defined in arithmetic:

| $\textit{Free}(x,y)$ | $x$ is free variable in $y$. |
| --- | --- |
| $\textit{FreeFor}(x,y,z)$ | $x$ is free for $y$ in $z$. |

The following operation on Gödel numbers plays a particularly important role:

$\textit{subst}(x, y) = z$   the operation which maps the pair with the Gödel number of a formula with one free variable and the Gödel number of a numeral to the Gödel number of the closed formula which results from the original formula when the given numeral is substituted for the free variable: $$ \textit{subst}(\ulcorner A(x)\urcorner , \ulcorner \underline{n}\urcorner) = \ulcorner A(\underline{n})\urcorner $$

Once the background logic, its axioms and rules of inference have been fixed, the following can also be defined:

$\textit{LogAx}(x)$   $x$ is the Gödel number of a logical axiom.

Rules of inference also get expressed in the arithmetized form:

For example, there is an arithmetical formula $M(x, y, z)$ which is true exactly when one has an application of a standard rule of inference “Modus Ponens” at hand; i.e., for some formulas $A$ and $B,$ $x = \ulcorner A\urcorner,$ $y = \ulcorner A \rightarrow B\urcorner$ and $z = \ulcorner B\urcorner.$

When the specific formal system $F$ at stake has been fixed, the following properties and relations can also be defined:

| $\textit{Axiom}_F(x)$ | $x$ is the Gödel number of a non-logical axiom of $F$. |
| --- | --- |
| $\textit{Prf}_F(x,y)$ | $x$ is the Gödel number of a derivation (in $F)$ of the formula with the Gödel number $y$. |
| $\textit{Prov}_F(y)$ | $\exists x \textit{Prf}_F(x, y)$, i.e., the formula (with the Gödel number) $y$ is provable (derivable) in $F$. |

All the above properties and relations, except the last one, provability, are decidable and can be, not only defined but, strongly represented in any sufficiently strong $F$.
