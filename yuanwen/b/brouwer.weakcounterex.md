# brouwer — weakcounterex（supplement）

> （《brouwer》词条补充材料，源：plato.stanford.edu/entries/brouwer/weakcounterex.html）

#### Supplement to Luitzen Egbertus Jan Brouwer

## Weak Counterexamples

Here are four weak counterexamples.

Consider a still open problem in mathematics, such as Goldbach’s conjecture (the conjecture that every even number equal to or greater than 4 is the sum of two prime numbers).

Being a still open problem, Goldbach’s conjecture is by itself a weak counterexample to PEM: we have at present experienced neither its truth nor its falsity, nor do we have a decision method. So intuitionistically speaking, we cannot at present assert “Goldbach’s conjecture is true, or it is false”.

As an illustration of the technique that Brouwer used to generate weak counterexamples to other classically valid statements, we show three more weak counterexamples, adapted from the first Vienna lecture (Brouwer, 1929). They are based on a sequence of rational numbers $a(n)$, defined in terms of Goldbach’s conjecture, as follows:

$$a(n) = \begin{cases} -\left(\frac{1}{2}\right)^n &\text{ if for all } j \le n, 2j+4 \text{ is the sum of two primes} \\ -\left(\frac{1}{2}\right)^k &\text{ if for some } k \le n, 2k+4 \text{ is the not the sum of} \\ &\qquad\qquad\text{two primes} \\ \end{cases}$$

The sequence of the $a(n)$ satisfies the Cauchy condition (the condition that for every rational number $\varepsilon \gt 0$ there is a natural number N such that $|a(j) - a(k)| \lt \varepsilon$ for all $j,k\gt$N), as for every $n$, any two members of the sequence after $a(n)$ lie within $(\frac{1}{2} )^n$ of each other. Therefore the sequence converges and determines a real number $\alpha$.

From the way $\alpha$ is constructed, it is clear that we can assert that $\alpha =0$ only when we know that the first clause of the definition of $a(n)$ always applies, in other words, only when we have proved Goldbach’s conjecture; and we can assert that $\alpha \ne 0$ only when we know that for some $n$ the second clause applies, in other words, when we have found a counterexample to the conjecture. So far, we have neither. This leads to the following three weak counterexamples:

1. We cannot now assert $\forall x\in \mathbb{R} (x = 0 \vee x \ne 0)$, because we cannot, intuitionistically, assert $\alpha = 0 \vee \alpha \ne 0$ until we have a proof of one of the disjuncts.
2. Similarly, we cannot now assert $\forall x\in \mathbb{R} (x \lt 0 \vee x = 0 \vee x \gt 0)$.
3. We cannot now assert $\forall x\in \mathbb{R} (x \in \mathbb{Q} \vee x \not\in \mathbb{Q})$, for to assert that $\alpha \in \mathbb{Q}$ we have to know $m,n \in \mathbb{Z}$ such that $\alpha = m/n$, but we can’t as long as we do not know the value of $\alpha$. (By construction, $\alpha$ cannot be irrational.)

Should Goldbach’s conjecture one day be proved or disproved, the definition of $\alpha$ can easily be modified by appealing to a remaining open problem; Brouwer’s first Vienna lecture (Brouwer 1929A) shows a general way to do this.

Brouwer devised further weak counterexamples using “creating subject” arguments (Heyting, 1956, ch. VIII; van Atten, 2003, ch. 5; van Atten, 2018).
