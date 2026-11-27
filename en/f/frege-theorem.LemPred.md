# frege-theorem — LemPred（supplement）

> （《frege-theorem》词条补充材料，源：plato.stanford.edu/entries/frege-theorem/LemPred.html）

#### Supplement to Frege’s Theorem and Foundations for Arithmetic

## Proof of the Lemma on Predecessor$^{+}$

We wish to prove the Lemma on Predecessor$^{+}$, which asserts:

**Lemma on *Predecessor*$^{+}$**: $$\begin{align*} &Nx\amp \mathit{Precedes}(y,x) \rightarrow \\ &\quad \#[\lambda z \,\mathit{Precedes}^{+}(z,y)] = \#[\lambda z \,\mathit{Precedes}^{+}(z,x)\amp z \neq x] \end{align*}$$

Now this Lemma can be proved with the help of the following Lemma:

**Lemma: No Number Ancestrally Precedes Itself** $\forall x[Nx\rightarrow\neg\mathit{Precedes}^{*}(x,x)]$

([Proof of the Lemma that No Number Ancestrally Precedes Itself](frege-theorem.PredNoRefl.md))

Now to prove the Lemma on Predecessor$^{+}\!$, assume that $Nn$ and $\mathit{Precedes}(m,n)$. We want to show:

$\#[\lambda z \, \mathit{Precedes}^{+}(z,m)] = \#[\lambda z \, \mathit{Precedes}^{+}(z,n)\amp z \neq n]$

By Hume's Principle, it suffices to show:

$[\lambda z \, \mathit{Precedes}^{+}(z,m)]\approx [\lambda z \, \mathit{Precedes}^{+}(z,n)\amp z \neq n]$

Now it is a fact about equinumerosity (Fact 1, Facts About Equinumerosity, §3) that if two concepts are materially equivalent, then they are equinumerous. It therefore suffices to show that

$\forall x([\lambda z \, \mathit{Precedes}^{+}(z,m)]x\equivwide [\lambda z \, \mathit{Precedes}^{+}(z,n)\amp z \neq n]x)$

And by *λ*-Conversion, it suffices to show:

$\forall x[\mathit{Precedes}^{+}(x,m) \equivwide \mathit{Precedes}^{+}(x,n)\amp x \neq n]$

So let us pick an arbitrary object, say $a$, and show:

$\mathit{Precedes}^{+}(a,m) \equivwide (\mathit{Precedes}^{+}(a,n)\amp a \neq n)$

$(\rightarrow)$ Assume $\mathit{Precedes}^{+}(a,m)$. Then from our assumption that $\mathit{Precedes}(m,n)$ and a Fact about $R^{+}$ (Fact 3, Facts About $R^{+}\!$, §4, Weak Ancestral), it follows that $\mathit{Precedes}^{*}(a,n)$. *A fortiori*, then, $\mathit{Precedes}^{+}(a,n)$. Now by the Lemma mentioned at the outset of this proof, namely, No Natural Number Ancestrally Precedes Itself, we know that $\neg \mathit{Precedes}^{*}(n,n)$. Since $a$ ancestrally precedes $n$ and $n$ does not, it follows that $a\neq n$. We have therefore proved what we were after, namely:

$\mathit{Precedes}^{+}(a,n)\amp a\neq n$

$(\leftarrow)$ Assume $\mathit{Precedes}^{+}(a,n)$ and $a\neq n$. By definition, the first conjunct tells us that either $\mathit{Precedes}^{*}(a,n)$ or $a = n$. Since we know by assumption that the latter disjunct is not true, we know $\mathit{Precedes}^{*}(a,n)$. But from this fact, the fact that Predecessor is 1-1, and our assumption that $\mathit{Precedes}(m,n)$, it follows from a fact about $R^{+}$ (Fact 8, Facts About $R^{+}$, §4, Weak Ancestral), that $\mathit{Precedes}^{+}(a,m)$, which is what we had to show.

Return to Proof that *Q* is Hereditary on the Natural Numbers
