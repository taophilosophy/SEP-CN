# mathematics-constructive — supplement1（supplement）

> （《mathematics-constructive》词条补充材料，源：plato.stanford.edu/entries/mathematics-constructive/supplement1.html）

#### Supplement to Constructive Mathematics

## Ishihara’s principle $\BDN$ and the anti-Specker Property

### Ishihara’s principle $\BDN$

We consider another principle of great significance for constructive reverse mathematics. Following Ishihara [1992], we say that an inhabited subset $S$ of the set $\mathbf{N}$ of natural numbers is *pseudobounded* if for each sequence $(s_n)_{n\ge 1}$ in $S$, $s_n/n \rightarrow 0$ as $n \rightarrow \infty$. This brings us to *Ishihara’s principle* $(\BDN)$:

Every inhabited, countable, pseudobounded subset of $\mathbf{N}$ is bounded.

This principle has the unusual property of being derivable in all three main interpretations—CLASS, INT, RUSS—of BISH but not in BISH alone: Lietz has shown that $\BDN$ fails in various realizability models of extensional Martin-Löf type theory; see Lietz [2004] and Lietz & Streicher [2011].

Ishihara [1992, Theorem 4] has shown that $\BDN$ is equivalent, over BISH, to each of the statements:

Every sequentially continuous mapping of a complete, separable metric space into a metric space is pointwise continuous;

Every sequentially continuous mapping of a separable metric space into a metric space is pointwise continuous.

He and other authors have subsequently proved that $\BDN$ is a necessary and sufficient addition to BISH to ensure the derivability of a number of results allowing us to pass from sequential to pointwise properties. One important example occurs with Banach’s inverse mapping theorem from functional analysis. The classical theorem states that the inverse of a bijective bounded linear mapping between Banach spaces is continuous; but Ishihara [1994], working with separable spaces, has shown that the best possible conclusion in BISH is the sequential continuity of the inverse map, and that to pass from that to full continuity, it is necessary and sufficient to work in BISH + $\BDN$.

### The anti-Specker Property

Is there any viable constructive substitute for the classical property of sequential compactness? This question might seem frivolous, since the sequential compactness of the two-point space $\{0,1\}$ is equivalent, constructively, to LPO. However, and perhaps to the reader’s surprise, there is a notion that is both constructively useful and classically equivalent to sequential compactness. In order to discuss it, we need some definitions, and a little motivation from RUSS.

Let $\mathbf{z} = (z_n)_{n\ge 1}$ be a sequence in a metric space $(Z,\varrho)$, and $X$ a subset of $A$. We say that $\mathbf{z}$ is

*eventually bounded away from each point of* $X$ if for each $x \in X$ there exist $\delta \gt 0$ and a positive integer $N$ such that $\varrho(z_n ,x) \ge \delta$ whenever $n \ge N$;

*eventually bounded away from the set* $X$ if there exist $\delta \gt 0$ and a positive integer $N$ such that for each $x \in X$, $\varrho(z_n ,x) \ge \delta$ whenever $n \ge N$.

We recall, from earlier in this article, the strong recursive counterexample to the sequential compactness of [0,1], Specker’s [1949] theorem in RUSS: there exists a (Specker) sequence $\mathbf{z}$ in $[0,1]$ that is eventually bounded away from each point of $[0,1]$. What would it take to rule such a counterexample out of our constructive mathematics?

By a *one-point extension* of a metric space $X$ we mean a metric space of the form $X\cup \{\omega\}$ on which the metric *ϱ* restricted to $X$, is the original one, and $\varrho(\omega ,X) \gt 0$. Here we are adopting the convention that $\varrho(\omega ,X) \gt 0$ is shorthand for

$$ \exists r \gt 0\, \forall x \in X\, (\varrho(\omega ,x) \ge r). $$

To avoid Specker sequences, we can introduce the following *anti-Specker property*, $\mathbf{AS}_X$, for X:

If $Z = X\cup \{\omega \}$ is a one-point extension of $X$, then every sequence in $Z$ that is eventually bounded away from each point of $X$ is eventually bounded away from $X$—that is, $z_n = \omega$ for all sufficiently large $n$.

This property is independent of the particular one-point extension of $X$: if it holds for one such extension, it holds for them all.

The anti-Specker property is classically equivalent to the sequential compactness of $X$. It allows us to pass from a pointwise property—being eventually bounded away from each point of the set—to a uniform one—being eventually bounded away from the set itself. One might therefore expect it to be connected with some version of the fan theorem. This is indeed the case: the anti-Specker property for $[0,1]$ is equivalent, over BISH, to the fan theorem FT$_{\mathsf{c}}$ for $\mathsf{c}$-bars (Berger & Bridges [2006]). It should therefore be no surprise that, when added to BISH, anti-Specker properties enable us to pass from pointwise to uniform properties in a number of instances. To illustrate, we sketch the proof of the following result:

BISH + AS$_X$ $\vdash$ Every pointwise continuous mapping of a metric space $X$ into a metric space is *uniformly sequentially continuous*, in the sense that for all sequences $(x_n)_{n\ge 1}$, $(x'_n)_{n\ge 1}$ in $X$, if $\varrho(x_n, x'_n) \rightarrow 0$ as $n \rightarrow \infty$, then $\varrho(f(x_n),f(x'_n)) \rightarrow 0$ as $n \rightarrow \infty$.

Let $Z \equiv X\cup \{\omega \}$ be a one-point extension of $X$, and consider sequences $(x_n)_{n\ge 1}, (x'_n)_{n\ge 1}$ in $X$ such that $\varrho(x_n,x'_n) \rightarrow \infty$ as $n\rightarrow \infty$. Given $\varepsilon \gt 0$, construct a binary sequence $(\lambda_n)_{n\ge 1}$ such that

$$\begin{align} \lambda_n &= 0 \Rightarrow \varrho(f(x_n),f(x'_n)) \lt \varepsilon ,\\ \lambda_n &= 1 \Rightarrow \varrho(f(x_n),f(x'_n)) \gt \frac{\varepsilon}{2}. \end{align}$$

If $\lambda_n = 0$, set $z_n = \omega$; if $\lambda_n = 1$, set $z_n = x_n$. Using the pointwise continuity of $f$ (we omit the details), we can show that the sequence $(z_n)_{n\ge 1}$ is eventually bounded away from each point of $X$. Hence, by the anti-Specker property of $X$, it is eventually bounded away from the set $X$. It follows that $\lambda_n = 0$, and hence that $\varrho(f(x_n),f(x'_n)) \lt \varepsilon$, for all sufficiently large values of $n$. Since *ε* is an arbitrary positive number, the proof is complete.

In our present state of knowledge, we can say that the proof-theoretic strength of AS$_{[0,1]}$ lies between that of the uniform continuity theorem (a consequence of FT$_{\Pi^0_1})$ and FT$_D$. Diener [2012] has shown that AS$_{[0,1]}$ is equivalent to every compact metric space having the anti-Specker property, and that a more general form of anti-Specker property, in which one-point extensions are replaced by arbitrary supersets, is equivalent to FT$_{\Pi^0_1})$. Further interconnections between anti-Specker properties, fan theorems, and other principles of constructive mathematics are studied in detail in Dent 2013; see also Diener 2008 (Chapter 4).
