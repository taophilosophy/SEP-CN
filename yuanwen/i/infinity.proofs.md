# infinity — proofs（supplement）

> （《infinity》词条补充材料，源：plato.stanford.edu/entries/infinity/proofs.html）

#### Supplement to Infinity

## Proofs of Theorems

**Proof that a Dedekind-infinite set contains a set just as large as the natural numbers.**

If we let $f$ be such a bijection between a set and some proper subset of itself, and let $x$ be an element of the set that is not in that proper subset, then we can consider the sequence $x, f(x), f(f(x)), f(f(f(x))),\ldots$ We can then define a function $g$ from the natural numbers to this sequence, by letting $g(0)=x$, and for any $n, g(n+1)=f(g(n))$. This function is defined for every natural number, and is one-to-one, and so it shows that this sequence has just as many elements as the set of natural numbers. (To see that it is one-to-one, assume not, so there would be two numbers $m\lt n$ such that $g(m)=g(n)$. Since $f$ is one-to-one, if $m$ and $n$ were both non-zero, then we would have $g(m-1)=g(n-1).$ By taking the earliest such pair, we would have $g(0)=g(n-m).$ But $g(0)=x,$ and $x$ is not in the subset to which $f$ maps all elements, while if $n-m\gt 0$, then $g(n-m)$ is. So this is impossible.)

**Proof that the cardinality of the positive real numbers is strictly greater than the cardinality of the positive integers.**

This proof and the next one follow Cantor’s proofs. Suppose, as hypothesis for *reductio*, that there is a bijection between the positive integers and the real numbers between 0 and 1. Given that there is such a bijection, there is a list of the real numbers between 0 and 1 of the following form (where d$_{ij}$ is the $j$th digit in the decimal representation of the $i$th real number on our list:

1. $0.\rd_{11}\rd_{12}\rd_{13}\ldots \rd_{1k}\ldots$ 2. $0.\rd_{21}\rd_{22}\rd_{23}\ldots \rd_{2k}\ldots$ $\vdots$ $n$. $0.\rd_{n1}\rd_{n2}\rd_{n3}\ldots \rd_{nk}\ldots$ $\vdots$

By hypothesis, every real number between 0 and 1 appears exactly once on this list. But consider the real number $r = 0.\rd_1 \rd_2 \rd_3\ldots\rd_n\ldots$, where $\rd_i =\rd_{nn}+1$ if $\rd_{nn} \in \{0,1,2,3,4,5,6,7\}$ and $\rd_i =\rd_{nn} -1$ otherwise. Since $r$ differs from the $n$th number in the list in the $n$th digit, $r$ is clearly not a number on our list. So we can conclude, by *reductio*, that there is no bijection between the positive integers and the real numbers between 0 and 1.

**Proof that the cardinality of a power set is strictly greater than the cardinality of the set itself.**

Suppose, as hypothesis for *reductio*, that there is a set $N$ for which the cardinality of $P(N)$—the power set of $N$—is the same as the cardinality of $N.$ Given this assumption, there is a bijection $I$ from $P(N)$ to $N$ such that (i) for each $s \in P(N),$ there is a unique member $I(s)\in N,$ and (ii) for each $r \in N,$ there is a unique member $I^-(r) \in P(N)$ under the inverse of our bijection, $I^-.$ But we can construct a member $M \in P(N)$ that is not mapped onto by any member of $N$ under the mapping $I^-$: for each $r\in N,$ $r\in M$ iff $r\not\in I^-(r).$

So we can conclude that it is not the case that there is a set $N$ for which the cardinality of $P(N)$ is the same as the cardinality of $N$. But it is obvious that the cardinality of $P(N)$ is not smaller than the cardinality of $N$ (because $P(N)$ includes all of the unit sets of members of $N$, and more besides). So the cardinality of the power set of a set is strictly greater than the cardinality of the set itself.
