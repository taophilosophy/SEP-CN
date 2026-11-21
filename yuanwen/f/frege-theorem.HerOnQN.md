# frege-theorem — HerOnQN（supplement）

> （《frege-theorem》词条补充材料，源：plato.stanford.edu/entries/frege-theorem/HerOnQN.html）

#### Supplement to Frege’s Theorem and Foundations for Arithmetic

## Proof that Q is Hereditary on the Natural Numbers

We want to prove the following claim:

$\mathit{HerOn}(Q,N)$

The proof of this claim appeals to the following Lemma (cf. **Gg** I, Theorem 149):

**Lemma on *Predecessor*$^+$**: $$\begin{align*} &Nx \amp \mathit{Precedes}(y,x) \rightarrow \\ &\quad \#[\lambda z \, \mathit{Precedes}^{+}(z,y)] = \#[\lambda z \, \mathit{Precedes}^{+}(z,x)\amp z\neq x] \end{align*}$$

([Proof of the Lemma on *Predecessor*$\,^{+}$](frege-theorem.LemPred.md))

Intuitively, the Lemma on Predecessor$^{+}$ tells us that if $y$ precedes a number $x$, then $\#[\lambda z \, z\leq y]$ is identical to $\#[\lambda z \, z\leq x\amp z\neq x]$.

Now to show $\mathit{HerOn}(Q,N)$, we have to show:

$\forall n\forall m[\mathit{Precedes}(n,m) \rightarrow (Qn\rightarrow Qm)]$

If we replace ‘$Q$’ with its definition and simplify the result by *λ*-Conversion, then what we have to show is:

$$\begin{align*} &\forall n\forall m(\mathit{Precedes}(n,m) \rightarrow (\mathit{Precedes}(n,\#[\lambda z \, \mathit{Precedes}^{+}(z,n)])\rightarrow \\ &\quad \mathit{Precedes}(m,\#[\lambda z \, \mathit{Precedes}^{+}(z,m)])) \end{align*}$$

(Intuitively, we have to show that if $n$ precedes $m$, then if $n$ precedes the number of numbers less than or equal to $n$, then $m$ precedes the number of numbers less than or equal to $m$.) So, let $n$ and $m$ be arbitrary numbers, so that we know $Nn$ and $Nm$ and assume both:

(A)   $\mathit{Precedes}(n,m)$ (B)   $\mathit{Precedes}(n,\#[\lambda z \, \mathit{Precedes}^{+}(z,n)])$

to show:

$\mathit{Precedes}(m,\#[\lambda z \, \mathit{Precedes}^{+}(z,m)])$

By the definition of Predecessor, we have to show that there is a concept $F$ and object $x$ such that:

(1)  $Fx$ (2)   $\#[\lambda z \, \mathit{Precedes}^{+}(z,m)] = \#F$ (3)  $m = \#[\lambda u \, Fu \amp u\neq x]$

We can demonstrate that there is an $F$ and $x$ for which (1), (2) and (3) hold if we pick $F$ to be $[\lambda z \, \mathit{Precedes}^{+}(z,m)]$ and pick $x$ to be $m$. We now establish (1), (2), and (3) for these choices.

To show that (1) holds, we have to show:

$[\lambda z \, \mathit{Precedes}^{+}(z,m)]m$

But we know, from the definition of $\mathit{Precedes}^{+}$, that $\mathit{Precedes}^{+}(m,m)$. So by abstraction using *λ*-Conversion, we are done.

To show that (2) holds, we need do no work, since our choice of $F$ requires us to show:

$\#[\lambda z \, \mathit{Precedes}^{+}(z,m)] = \#[\lambda z \, \mathit{Precedes}^{+}(z,m)]$,

which we know by the logic of identity.

To show (3) holds, we need to show:

(C)  $m = \#[\lambda u \, \mathit{Precedes}^{+}(u,m) \amp u \neq m]$

[Note that the *λ*-expression in the above has been simplified by applying *λ*-Conversion to the following (which, strictly speaking, is what results when you substitute our choice for $F$ in (3)):

$[\lambda u \, [\lambda z \, \mathit{Precedes}^{+}(z,m)]u \amp u\neq m]$

In what follows, we use the simplified version of this *λ*-expression.]

Now in virtue of (A), (B) and the functionality of Predecessor (the proof of which was left as an exercise in the subsection No Two Numbers Have the Same Successor in §5), we know $m = \#[\lambda z \, \mathit{Precedes}^{+}(z,n)]$. So, substituting for $m$ in (C), we have to show:

$\#[\lambda z \, \mathit{Precedes}^{+}(z,n)] = \#[\lambda u \, \mathit{Precedes}^{+}(u,m) \amp u \neq m]$

But we can demonstrate this by appealing to the Lemma on Predecessor$^{+}$ mentioned at the outset. We may instantiate the variables $x$ and $y$ in that Lemma to $m$ and $n$, respectively, yielding:

$$\begin{align*} &Nm \amp \mathit{Precedes}(n,m)\rightarrow \\ &\quad \#[\lambda z \, \mathit{Precedes}^{+}(z,n)] = \#[\lambda z \, \mathit{Precedes}^{+}(z,m) \amp z \neq m] \end{align*}$$

Since the consequent is what we had to show, we are done, for the conjuncts of the antecedent are things we assumed to be true at the beginning of our conditional proof.

Return to Frege’s Theorem and Foundations for Arithmetic
