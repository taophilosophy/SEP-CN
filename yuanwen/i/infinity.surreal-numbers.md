# infinity — surreal-numbers（supplement）

> （《infinity》词条补充材料，源：plato.stanford.edu/entries/infinity/surreal-numbers.html）

#### Supplement to Infinity

## Construction of Surreal Numbers

Conway’s construction of surreal numbers (1976) is summarized in the following principle: If $L$, $R$ are two sets of surreal numbers, and no member of $L$ is $\ge$ any member of $R$, then there is a surreal number $\{L|R\}$ consisting of a “left set” $L$ and a “right set” $R$. By convention, if $x = \{L|R\}$, then we let $x^L$ and $x^R$ stand for elements from $L$ and $R$ respectively. Sums and products of sets of surreal numbers are the unions of element-wise addition and multiplication.

We then make the following definitions:

1. $x \ge y$ iff no $x^R \le y$ and $x \le$ no $y^L$. (Following our convention, the right-hand side says that no element of $x$’s right set is $\le y$, and $x$ is $\le$ no element of $y$’s left set.)
2. $x \le y \text{ iff } y \ge x$
3. $x = y \text{ iff } x \ge y \text{ and } y \ge x$
4. $x \gt y \text{ iff } x \ge y \text{ and not } y \ge x$
5. $x + y = \{x^L + y, x + y^L|x^R + y, x + y^R\}$
6. $-x = \{-x^R|-x^L\}$
7. $xy = \{x^L y + xy^L - x^L y^L, x^R y + xy^R - x^R y^R |$ $x^L y + xy^R - x^L y^R, x^R y + xy^L - x^R y^L\}$
8. for any non-zero $x$, we can find $$\begin{align} y = \{0, [1 + &(x^R - x)y^L]/x^R, [1 + (x^L - x)y^R]/x^L |\\ &[1 + (x^L -x)y^L]x^L, [1 + (x^R - x)]y^R]/x^R\} \end{align}$$ such that $xy=1$

We may construct the surreal numbers in successive stages (or on successive “days”, as Conway puts it), and regard them generally as pairs of sets of previously constructed surreal numbers. This is not circular, as at the first stage (“day”) we can help ourselves to a pair of *empty* sets. Taking $L=R=\emptyset$ gives us $\{\emptyset|\emptyset\}$, abbreviated $\{|\}$. We identify this with 0. And away we go:

$\{0|\} = 1$; $\{|0\} = -1.$

$\{0,1|\} = \{1|\} = 2$; $\{0|1\} = 1/2$; $\{-1|0\} = -1/2$; $\{|-1\} = -2.$

$\{2|\} = 3$; $\{1|2\} = 3/2$; $\{1/2|1\} = 3/4$; $\{0|1/2\} = 1/4$; $\{-1/2|0\} = -1/4$; $\{-1|-1/2\} = -3/4$; $\{-2|-1\} = -3/2$; $\{|-2\} = -3$

$\vdots$

$\{1/4, 5/16, 21/64,\ldots | 1/2, 3/8, 11/32, \ldots \} = 1/3$;

$\{0, 1, 2, 3, \ldots |\} = \omega$; $\{|0, -1, -2, -3, \ldots \} = -\omega$;

$\{0|1, 1/2, 1/4, 1/8, \ldots \} = 1/\omega$; $\{1/2, 3/4, 7/8, \ldots |1\} = 1 - 1/\omega$;

$\{0, 1, 2, 3,\ldots, \omega|\} = \omega+1$; $\{|0, -1, -2, -3, \ldots, -\omega\} = -(\omega +1)$; $\{0, 1, 2, 3,\ldots|\omega\} = \omega-1$;

$\{1/\omega|1, 1/2, 1/4 \ldots \} = 2/\omega$; $\{0|1/\omega\} = 1/2\omega$;

$\{2|5/2, 9/4, 17/8, \ldots \} = 2 + 1/\omega$; $\{3/2, 7/4, 15/8, \ldots |2\} = 2 - 1/\omega$

$\vdots$

$\{\omega, \omega+1, \omega+2, \omega+3,\ldots | \} = \omega\cdot 2$; $\{0, 1, 2, 3,\ldots |\omega, \omega-1, \omega-2, \omega-3, \ldots \} = \omega/2$;

$\{0|1/\omega, 1/2\omega, 1/4\omega, \ldots \} = 1/\omega^2$

$\vdots$

$\{0, 1, 2, 3,\ldots | \omega, \omega/2, \omega/4, \omega/8, \ldots \} = \sqrt{\omega}$

$\vdots$

The resulting number system contains *gaps*. $[L|R]$ is a gap iff (1) every subset of $L$ has an upper bound within $L$ and every subset of $R$ has a lower bound within $R$; and (2) the union of $L$ and $R$ is the proper class of all of the surreal numbers. This proper class is called $No$. (Note that (2) entails that at least one of $L$ and $R$ is a proper class.) Ehrlich (2012) argues that No may be regarded as an absolute continuum. If a partition $\Xi = [L|R]$ is a gap and $x$ is a number:

$x+\Xi$ is the gap $[x+L|x+R]$;

$-\Xi$ is the gap $[-R|-L]$; and

$\omega^\Xi$ is the gap $[L'|R']$,

where $L'$ contains all numbers $\omega^l$s and $R'$ contains all numbers $\omega^r$s for $l\in L$, $r \in R$, and $s$ any positive real. $On$ is the gap $[No|]$ at the end of the number line; $1/On$ is the gap between 0 and all of the positive numbers; $\infty$ is the gap between the reals and the positive infinite numbers; and $1/\infty$ is the gap between the infinitesimals and the positive reals.

All numbers have a unique normal form expression $\sum_{\beta\lt \alpha}\omega^{y_\beta}r_\beta$, where $\alpha$ is an ordinal, the $r_\beta$ $(\beta\lt\alpha)$ are non-zero reals, and the numbers $y_\beta$ form a descending sequence. Moreover, every expression of this form is a number. All gaps have one of the following two normal forms: $\sum_{\beta\in On} \omega^{x_\beta}r_\beta$ and ($\sum_{\beta \lt \alpha}\omega^{x_\beta}r_\beta)\pm\omega^\Xi$, where in each case $x_\beta$ is a decreasing sequence and each $r_\beta$ is a non-zero real number, and, in the second case, $\Xi$ is a gap $[L'|R']$ for which $R'$ contains all the $x_\beta$ $(\beta \lt\alpha).$ It is worth emphasizing that, in Conway’s system, gaps are not numbers, since they are formed from proper classes rather than sets. For example, in Conway’s system, $\infty$ is neither an ordinal nor a cardinal.
