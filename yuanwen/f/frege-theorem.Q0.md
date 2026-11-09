# frege-theorem — Q0（supplement）

> （《frege-theorem》词条补充材料，源：plato.stanford.edu/entries/frege-theorem/Q0.html）

#### Supplement to Frege’s Theorem and Foundations for Arithmetic

## Proof that 0 Falls Under Q

The proof that 0 falls under $Q$ is relatively straightforward. We want to show:

$[\lambda y \, \mathit{Precedes}(y,\#[\lambda z \, \mathit{Precedes}^{+}(z,y)])]0$

By $\lambda$-Conversion, it suffices to show:

$\mathit{Precedes}(0, \#[\lambda z \, \mathit{Precedes}^{+}(z,0)])$

So, by the definition of Predecessor, we have to show that there is a concept $F$ and object $x$ such that:

1. $Fx$
2. $\#[\lambda z \, \mathit{Precedes}^{+}(z,0)] = \#F$
3. $0 = \#[\lambda u \, Fu\amp u\neq x]$

We can demonstrate that there is an $F$ and $x$ for which (1), (2) and (3) hold if we pick $F$ to be $[\lambda z \, \mathit{Precedes}^{+}(z,0)]$ and pick $x$ to be 0. We now establish (1), (2), and (3) for these choices.

To show that (1) holds, we have to show:

$[\lambda z \, \mathit{Precedes}^{+}(z,0)]0$

But we know, from the definition of $\mathit{Precedes}^{+}$, that $\mathit{Precedes}^{+}(0,0)$, So by $\lambda$-abstraction, we are done.

To show that (2) holds, we need do no work, since our choice of $F$ requires us to show:

$\#[\lambda z \, \mathit{Precedes}^{+}(z,0)] = \#[\lambda z \, \mathit{Precedes}^{+}(z,0)],$

which we know by the logic of identity.

To show (3) holds, we need to show:

$0 = [\lambda u \, [\lambda z \, \mathit{Precedes}^{+}(z,0)]u\amp u\neq 0]$

But, by applying $\lambda$-Conversion, we have to show:

(A)  $0 = \#[\lambda u \, \mathit{Precedes}^{+}(u,0)\amp u\neq 0]$

To show (A), it suffices to show the following, in virtue of the Lemma Concerning Zero (in our subsection on The Concept *Natural Number* in §4):

$\neg\exists x ([\lambda u \, \mathit{Precedes}^{+}(u,0) \amp u\neq 0]x)$

And by $\lambda$-Conversion, it suffices to show:

(B)  $\neg\exists x (\mathit{Precedes}^{+}(x,0)\amp x\neq 0)$

We establish (B) as follows.

When we established Theorem 2 (i.e., the fact that 0 is not the successor of any number), we proved that nothing precedes 0:

$\neg\exists x \mathit{Precedes}(x,0)$

From this, and Fact (4) about $R^{*}$ (in the subsection on the Ancestral of $R$, in §4), it follows that nothing ancestrally precedes 0:

$\neg\exists x \mathit{Precedes}^{*}(x,0)$

Now suppose (for *reductio*) the negation of (B); i.e, that there is some object, say a, such that $\mathit{Precedes}^{+}(a,0)$ and $a\neq 0$. Then, by definition of $\mathit{Precedes}^{+}$, it follows that either $\mathit{Precedes}^{*}(a,0)$ or $a = 0$. But since our reductio hypthesis includes that $a\neq 0$, it must be that $\mathit{Precedes}^{*}(a,0)$, which contradicts the fact displayed immediately above.

Return to Frege's Theorem and Foundations for Arithmetic
