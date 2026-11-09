# brouwer — strongcounterex（supplement）

> （《brouwer》词条补充材料，源：plato.stanford.edu/entries/brouwer/strongcounterex.html）

#### Supplement to Luitzen Egbertus Jan Brouwer

## Strong Counterexamples

Here is the argument for Brouwer’s strong counterexample to one form of PEM that he mentions in his paper “Reflections on Formalism” (1928A2). We will show that

$$ \neg \forall x\in \mathbb{R}(Px \vee \neg Px) $$

where $Px =$ “$x$ is rational” and $\mathbb{R}$ is the intuitionistic continuum. Accordingly, in this context real numbers are to be understood intuitionistically (namely, as convergent choice sequences).

We first show that the continuum cannot be split, that is, there are no non-empty spreads $A$ and $B$ such that $A\cup B = \mathbb{R}$ and $A\cap B = \varnothing$. For assume there are; then the function $f:\mathbb{R} \rightarrow \mathbb{R}$ defined by

$$ f(x) = \begin{cases} 0 \text{ if } x \in A \\ 1 \text{ if } x \in B \end{cases} $$

is total and therefore, by Brouwer’s continuity theorem (generalised from [0,1] to $\mathbb{R})$, continuous. But then $f$ must be constant, so either $A$ or $B$ is equal to $\mathbb{R}$, and the other spread must be empty. This, however, contradicts the assumption that both $A$ and $B$ are non-empty.

From the fact that the continuum cannot be split it follows that $\forall x\in \mathbb{R}(P(x) \vee \neg P(x))$ is false. For if it were true, we could obtain a splitting of the continuum by letting $f$ assign 0 to the rational real numbers $(A)$, and 1 to the irrational ones $(B)$; but this is impossible, as just shown. Hence, $\neg \forall x\in \mathbb{R}(P(x) \vee \neg P(x))$.

Brouwer established that $\mathbb{R}$ can’t be split in 1927, in footnote 10 of “On the Domains of Definition of Functions”.

Other strong counterexamples that Brouwer devised are

1. $\neg \forall x\in \mathbb{R}(\neg \neg x \lt 0 \rightarrow x \lt 0)$ (Brouwer, 1949A)
2. $\neg \forall x\in \mathbb{R}(x \ne 0 \rightarrow x \lt 0 \vee x \gt 0)$ (Brouwer, 1949B)

Here Brouwer used “creating subject” arguments (Heyting, 1956, ch. VIII; van Atten, 2003, ch.5; van Atten, 2018).
