# frege-theorem — PredNoRefl（supplement）

> （《frege-theorem》词条补充材料，源：plato.stanford.edu/entries/frege-theorem/PredNoRefl.html）

#### Supplement to Frege’s Theorem and Foundations for Arithmetic

## Proof That No Number Ancestrally Precedes Itself

We wish to prove:

**Lemma: No Number Ancestrally Precedes Itself** $\forall x[Nx\rightarrow \neg\mathit{Precedes}^{*}(x,x)]$

*Proof*. Assume $Nb$, to show: $\neg \mathit{Precedes}^{*}(b,b)$. Now Fact 7 concerning $R^{+}$ is:

$[Fx\amp R^{+}(x,y) \amp \mathit{Her}(F,R)]\rightarrow Fy$

So we know the following instance of Fact 7 is true, where $x = 0$, $y$ is $b$, $F$ is $[\lambda z \, \neg\mathit{Precedes}^{*}(z,z)]$, and $R$ is *Precedes*:

$$\begin{align*} &[\lambda z \, \neg\mathit{Precedes}^{*}(z,z)]0\amp \mathit{Precedes}^{+}(0,b)\ \amp \\ &\quad \mathit{Her}([\lambda z \, \neg\mathit{Precedes}^{*}(z,z)], \mathit{Precedes}))\rightarrow [\lambda z\, \neg\mathit{Precedes}^{*}(z,z)]b \end{align*}$$

By *λ*-Conversion on various terms in the above, this reduces to:

$$\begin{align*} &[\neg\mathit{Precedes}^{*}(0,0)\amp \mathit{Precedes}^{+}(0,b)\ \amp \\ &\quad \mathit{Her}([\lambda z\, \neg\mathit{Precedes}^{*}(z,z)], \mathit{Precedes})]\rightarrow \neg\mathit{Precedes}^{*}(b,b) \end{align*}$$

So to establish $\neg\mathit{Precedes}^{*}(b,b)$, we need to show each of the following conjuncts of the antecedent:

1. $\neg\mathit{Precedes}^{*}(0,0)$
2. $\mathit{Precedes}^{+}(0,b)$
3. $\mathit{Her}([\lambda z\, \neg\mathit{Precedes}^{*}(z,z)], \mathit{Precedes})$

To prove (a), note that in the Proof of Theorem 2 (i.e., $\neg\exists x(Nx\amp \mathit{Precedes}(x,0)))$, we established that $\neg\exists x(\mathit{Precedes}(x,0)$). But it is an instance of Fact 4 concerning $R^{*}$, that

$\exists x\mathit{Precedes}^{*}(x,0) \rightarrow \exists x\mathit{Precedes}(x,0)$.

It therefore follows that $\neg\exists x(\mathit{Precedes}^{*}(x,0))$. So $\neg\mathit{Precedes}^{*}(0,0)$.

We know (b) by our assumption that $Nb$ and the definition of $N$.

To establish (c), we have to show:

$$\begin{align*} &\forall x,y(\mathit{Precedes}(x,y)\rightarrow \\ &\quad ([\lambda z\, \neg\mathit{Precedes}^{*}(z,z)]x\rightarrow [\lambda z\, \neg\mathit{Precedes}^{*}(z,z)]y)) \end{align*}$$

That is, by *λ*-Conversion, we have to show:

$\forall x,y(\mathit{Precedes}(x,y)\rightarrow (\neg\mathit{Precedes}^{*}(x,x)\rightarrow \neg\mathit{Precedes}^{*}(y,y)))$

And by contraposition, we have to show:

$\forall x,y(\mathit{Precedes}(x,y)\rightarrow (\mathit{Precedes}^{*}(y,y)\rightarrow \mathit{Precedes}^{*}(x,x)))$

So assume *Precedes* $(a,b)$ and $\mathit{Precedes}^{*}(b,b)$. If we show $\mathit{Precedes}^{*}(a,a)$, we are done. We know the following instance of Fact 8 concerning $R^{+}$, where $a$ is substituted for $z$, $b$ for $y$, $b$ for $x$, and *Precedes* for $R$:

$$\begin{align*} &\mathit{Precedes}^{*}(b,b)\amp \mathit{Precedes}(a,b)\amp \mathit{Precedes} \textrm{ is 1-1 }\rightarrow \\ &\quad \mathit{Precedes}^{+}(b,a) \end{align*}$$

Since we have assumed $\mathit{Precedes}^{*}(b,b)$ and $\mathit{Precedes}(a,b)$, and we have proven in the main text that *Predecessor* is 1-1, we can use the instance of Fact 8 to conclude $\mathit{Precedes}^{+}(b,a)$. But the following is an instance of Fact 2 concerning $R^{+}$, when $a$ is substituted for $x$, $b$ for $y$, $a$ for $z$, and $R$ is *Precedes*:

$\mathit{Precedes}(a,b)\amp \mathit{Precedes}^{+}(b,a)\rightarrow\mathit{Precedes}^{*}(a,a)$

But we know $\mathit{Precedes}(a,b)$ by assumption and we have just shown $\mathit{Precedes}^{+}(b,a)$. So $\mathit{Precedes}^{*}(a,a)$, and we are done.

Proof of the Lemma on Predecessor
