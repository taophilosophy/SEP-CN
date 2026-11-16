# frege-theorem — proof5（supplement）

> （《frege-theorem》词条补充材料，源：plato.stanford.edu/entries/frege-theorem/proof5.html）

#### Supplement to Frege’s Theorem and Foundations for Arithmetic

## Proof of Equinumerosity Lemma

In this proof of the Equinumerosity Lemma, we utilize the following abbreviation, where $\mathrm{\phi}$ is any formula in which the variable $y$ may or may not be free and $\mathrm{\phi}^{\nu}_{\upsilon}$ is the result of replacing the free occurrences of $\upsilon$ in $\mathrm{\phi}$ by *ν*:

$x\eqclose \mathit{\iota}y\mathrm{\phi} \eqabbr \mathrm{\phi}\amp \forall z(\mathrm{\phi}^z_y \rightarrow z\eqclose x)$

We may read this as follows:

$x$ is identical to *the* object $y$ which is such that $\mathrm{\phi}$ if and only if both $x$ is such that $\mathrm{\phi}$ and everything which is such that $\mathrm{\phi}$ is identical to $x$.

This abbreviation is employed below to simplify the definition of new relations. Given this new notation, we will use only the following simple consequence of this definition:

**Principle of Descriptions**: $x\eqclose \mathit{\iota} y\mathrm{\phi}\rightarrow \mathrm{\phi}^x_y $

In other words, if $x$ is *the* object $y$ such that $\mathrm{\phi} (y)$, then $x$ is such that $\mathrm{\phi}$. The use of this principle will be obvious in what follows.

*Proof of Equinumerosity Lemma*. Assume that $P\approx Q, Pa$, and $Qb$. So there is a relation, say $R$, such that (a) $R$ maps every object falling under $P$ to a unique object falling under $Q$ and (b) for every object falling under $Q$ there is a unique object falling under $P$ which is $R$-related to it. Now we use $P^{-a}$ to designate $[\lambda z \, Pz\amp z\neq a]$, and we use $Q^{-b}$ to designate $[\lambda z \, Qz\amp z\neq b]$. We want to show that $P^{-a}\approx Q^{-b}$. By the definition of equinumerosity, we have to show that there is a *functional* relation $R'$ which is 1-1 from the objects falling under $P^{-a}$ onto the objects falling under $Q^{-b}$. We prove this by cases.

*Case 1*: Suppose $Rab$. Then we choose $R'$ to be $R$ itself. Clearly, $R$ is then a 1-1 functional relation from the objects of $P^{-a}$ to the objects of $Q^{-b}$. But the proof can be given as follows. We show: (A) that $R$ is a functional relation from the objects of $P^{-a}$ to the objects of $Q^{-b}$, and then (B) that $R$ is a 1-1 functional relation from the objects of $P^{-a}$ onto the objects of $Q^{-b}$.

(A) Pick an arbitrary object, say $c$, such that $P^{-a}c$. We want to show that there is a unique object which falls under $Q^{-b}$ and to which $c$ bears $R$. Since $P^{-a}c$, we know that $Pc\amp c\neq a$, by the definition of $P^{-a}$. But if $Pc$, then by our hypothesis that $R$ is a witness to the equinumerosity of $P$ and $Q$, it follows that there is a unique object, say $d$, such that $Qd$ and $Rcd$. But we are considering the case in which $Rab$ and so from the established facts that $Rcd$ and $c\neq a$, it follows by the 1-1 character of $R$ that $b\neq d$. So we have that $Qd$ and $d\neq b$, which establishes that $Q^{-b}d$. And we have also established that $Rcd$. So it remains to show that every other object that falls under $Q^{-b}$ to which $c$ bears $R$ just is identical to $d$. So suppose $Q^{-b}e$ and $Rce$. Then by definition of $Q^{-b}$, it follows that $Qe$. But now $e=d$, for $d$ is the unique object falling under $Q$ to which $c$ bears $R$. So there is a unique object which falls under $Q^{-b}$ and to which $c$ bears $R$.

(B) Pick an arbitrary object, say $d$, such that $Q^{-b}d$. We want to show that there is a unique object falling under $P^{-a}$that bears $R$ to $d$. Since $Q^{-b}d$, we know $Qd$ and $d\neq b$. From $Qd$ and the fact that $R$ witnesses the equinumerosity of $P$ and $Q$, we know that there is a unique object, say $c$, that falls under $P$ and which bears $R$ to $d$. Since we are considering the case in which $Rab$, and we’ve established $Rcd$ and $d\neq b$, it follows that $a\neq c$, by the fact that $R$ is a functional relation. Since we now have $Pc$ and $c\neq a$, we have established that $c$ falls under $P^{-a}$, and moreover, that $Rcd$. So it remains to prove that any other object that falls under $P^{-a}$ and which bears $R$ to $d$ just is (identical to) $c$. But if $f$, say, falls under $P^{-a}$ and bears $R$ to $d$, then $Pf$, by definition of $P^{-a}$. But recall that $c$ is the unique object falling under $P$ which bears $R$ to $d$. So $f=c$.

*Case 2*: Suppose $\neg Rab$. Then we choose $R’$ to be the relation:

$$\begin{align*} &[\lambda xy \, (x\neqclose a \amp y\neqclose b\amp Rxy)\ \lor \\ &\quad (x\eqclose \mathit{\iota}u(Pu\amp Rub)\amp y\eqclose \mathit{\iota}u(Qu\amp Rau))] \end{align*}$$

To see that there is such a relation, note that once we replace the abbreviations $x=\mathit{\iota}u(Pu\amp Rub)$ and $y=\mathit{\iota}u(Qu\amp Rau)$ by primitive notation, the matrix of the *λ*-expression is a formula of the form $\mathrm{\phi}(x,y)$ which can be used in an instance of the Comprehension Principle for Relations.

Now we want to show that $R’$ is a 1-1 functional relation from the objects of $P^{-a}$ onto the objects of $Q^{-b}$. We show (A) that $R’$ is a functional relation from the objects of $P^{-a}$ to the objects of $Q^{-b}$, and then (B) that $R’$ is a 1-1 functional relation from the objects of $P^{-a}$ onto the objects of $Q^{-b}$.

(A) To show that $R’$ is a functional relation from the objects of $P^{-a}$ to the objects of $Q^{-b}$, pick an arbitrary object, say $c$, such that $P^{-a}c$. Then by definition of $P^{-a}$, we know that $Pc$ and $c\neq a$. We need to find an object, say $d$ for which the following three things hold: (i) $Q^{-b}d$, (ii) $R’cd$, and (iii) $\forall w(Q^{-b}w \amp R’cw\rightarrow w=d)$. We find such a $d$ in each of the following, mutually exclusive subcases:

Subcase 1: $Rcb$. So, since we know that each object falling under $Q$ is such that there is a unique object falling under $P$ that is $R$-related to it, we know that $c= \mathit{\iota}u(Pu\amp Rub)$. Then, since we know R maps $a$ to a unique object falling under $Q$, we let $d$ be that object. That is, $d$ satisfies the defined condition $d=\mathit{\iota}u(Qu\amp Rau)$. So $Qd$, $Rad$, and $\forall w(Qw\amp Raw\rightarrow w=d)$. We now show that (i), (ii) and (iii) hold for $d$:

1. Since we know $Qd$, all we have to do to establish $Q^{-b}d$ is to show $d\neq b$. But we know $Rad$ and we are considering the case where $\neg Rab$. So, by the laws of identity, $d\neq b$.
2. To show $R’cd$, we need to establish: $$\begin{align*} &(c\neqclose a\amp d\neqclose b\amp Rcd)\ \lor \\ &\quad (c\eqclose \mathit{\iota}u(Pu\amp Rub)\amp d\eqclose \mathit{\iota}u(Qu\amp Rau)) \end{align*}$$ But the conjunctions of the right disjunct are true (by assumption and by definition, respectively). So $R'cd$.
3. Suppose $Q^{-b}e$ (i.e., $Qe$ and $e\neq b$) and $R'ce$. We want to show: $e=d$. Since $R'ce$, then: $$\begin{align*} &(c\neqclose a\amp e\neqclose b\amp Rce)\ \lor \\ &\quad (c\eqclose \mathit{\iota}u(Pu\amp Rub)\amp e\eqclose \mathit{\iota}u(Qu\amp Rau)) \end{align*}$$ But the left disjunct is impossible (we’re considering the subcase where $Rcb$, yet the left disjunct asserts $Rce$ and $e\neq b$, which together contradict the fact that $R$ is a functional relation). So the right disjunct must be true, in which case it follows from the fact that $e=\mathit{\iota}u(Qu\amp Rau)$ that $e=d$, by the definition of $d$.

Subcase 2: $\neg Rcb$. We are under the assumption $P^{-a}c$ (i.e., $Pc$ and $c\neq a$), and so we know by the definition of $R$ and the fact that $Pc$ that there is a unique object which falls under $Q$ and to which $c$ bears $R$. Choose $d$ to be this object. So $Qd$, $Rcd$, and $\forall w(Qw\amp Rcw\rightarrow w=d)$. We can now show that (i), (ii) and (iii) hold for $d$:

1. Since we know $Qd$, all we have to do to establish that $Q^{-b}d$ is to show $d\neq b$. We know that $Rcd$ and we are considering the subcase where $\neg Rcb$. So it follows that $d\neqclose b$, by the laws of identity. So $Q^{-b}d$.
2. To show $R’cd$, we need to establish: $$\begin{align*} &(c\neqclose a\amp d\neqclose b\amp Rcd)\ \lor \\ &\quad (c\eqclose \mathit{\iota}u(Pu\amp Rub)\amp d\eqclose \mathit{\iota}u(Qu\amp Rau)) \end{align*}$$ But the conjuncts of the left disjunct are true, for $c\neq a$ (by assumption), $d\neq b$ (we just proved this), and $Rcd$ (by the definition of $d$). So $R’cd$.
3. Suppose $Q^{-b}e$ (i.e., $Qe$ and $e\neq b)$ and $R’ce$. We want to show: $e=d$. Since $R’ce$, then: $$\begin{align*} &(c\neqclose a\amp e\neqclose b\amp Rce)\ \lor \\ &\quad (c\eqclose \mathit{\iota}u(Pu\amp Rub)\amp e\eqclose \mathit{\iota}u(Qu\amp Rau)) \end{align*}$$ But the right disjunct is impossible (we’re considering the subcase where $\neg Rcb$, yet the right disjunct asserts $c=\mathit{\iota}u(Pu\amp Rub)$, which implies $Rcb$, a contradiction). So $c\neq a\amp e\neq b \amp Rce$. Since we now know that $Qe$ and $Rce$, we know that $e=d$, since $d$ is, by definition, the unique object falling under $Q$ to which $c$ bears $R$.

(B) To show that $R’$ is a 1-1 functional relation from the objects of $P^{-a}$ onto the objects of $Q^{-b}$, pick an arbitrary object, say $d$, such that $Q^{-b}d$. Then by definition of $Q^{-b}$, we know that $Qd$ and $d\neq b$. We need to find an object, say $c$, for which the following three things hold: (i) $P^{-a}c$, (ii) $R’cd$, and (iii) $\forall w(P^{-a}w\amp R’wd\rightarrow w=c)$. We find such a $c$ in each of the following, mutually exclusive cases:

Subcase 1: $Rad$. So $d=\mathit{\iota}u(Qu\amp Rau)$. Then choose $c=\mathit{\iota}u(Pu\amp Rub)$ (we know there is such an object). So $Pc$, $Rcb$, and $\forall w(Pw\amp Rwb\rightarrow w=c)$. We now show that (i), (ii) and (iii) hold for $c$:

1. Since we know $Pc$, all we have to do to establish $P^{-a}c$ is to show $c\neq a$. But we know $Rcb$, and we are considering the case where $\neg Rab$. So, by the laws of identity, it follows that $c\neq a$.
2. To show $R’cd$, we need to establish: $$\begin{align*} &(c\neqclose a\amp d\neqclose b\amp Rcd)\ \lor \\ &\quad (c\eqclose \mathit{\iota}u(Pu\amp Rub)\amp d\eqclose \mathit{\iota}u(Qu\amp Rau)) \end{align*}$$ But the conjuncts of the right disjunct are true (by definition and by assumption, respectively). So $R’cd$.
3. Suppose $P^{-a}f$ (i.e., $Pf$ and $f\neq a)$ and $R’fd$. We want to show: $f=c$. Since $R’fd$, then: $$\begin{align*} &(f\neqclose a\amp d\neqclose b\amp Rfd)\ \lor \\ &\quad (f\eqclose \mathit{\iota}u(Pu\amp Rub)\amp d\eqclose \mathit{\iota}u(Qu\amp Rau)) \end{align*}$$ But the left disjunct is impossible (we’re considering the subcase where $Rad$, yet the left disjunct asserts $Rfd$ and $f\neq a$, which together contradict the fact that $R$ is 1-1). So the right disjunct must be true, in which case it follows from the fact that $f=\mathit{\iota}u(Pu\amp Rub)$ that $f=c$, by the definition of $c$.

Subcase 2: $\neg Rad$. We are under the assumption $Q^{-b}d$ (i.e., $Qd$ and $d\neq b)$, and so we know by the definition of $R$ and the fact that $Qd$ that there is a unique object which falls under $P$ and which bears $R$ to $d$. Choose $c$ to be this object. So $Pc$, $Rcd$, and $\forall w(Pw\amp Rwd\rightarrow w=c)$. We can now show that (i), (ii), and (iii) hold for $c$:

1. Since we know $Pc$, all we have to do to establish that $P^{-a}c$ is to show $c\neq a$. But we know that $Rcd$, and we are considering the subcase in which $\neg Rad$. So it follows that $c\neq a$, by the laws of identity. So $P^{-a}c$.
2. To show $R’cd$, we need to establish: $$\begin{align*} &(c\neqclose a\amp d\neqclose b\amp Rcd)\ \lor \\ &\quad (c\eqclose \mathit{\iota}u(Pu\amp Rub)\amp d\eqclose \mathit{\iota}u(Qu\amp Rau)) \end{align*}$$ But the conjuncts of the left disjunct are true, for $c\neq a$ (we just proved this), $d\neq b$ (by assumption), and $Rcd$ (by the definition of $c$). So $R’cd$.
3. Suppose $P^{-a}f$ (i.e., $Pf$ and $f\neq a)$ and $R’fd$. We want to show: $f=c$. Since $R’fd$, then: $$\begin{align*} &(f\neqclose a\amp d\neqclose b\amp Rfd)\ \lor \\ &\quad (f\eqclose \mathit{\iota}u(Pu\amp Rub)\amp d\eqclose \mathit{\iota}u(Qu\amp Rau)) \end{align*}$$ But the right disjunct is impossible (we’re considering the subcase where $\neg Rad$, yet the right disjunct asserts $d=\mathit{\iota}u(Qu\amp Rau)$, which implies $Rad$, a contradiction). So $f\neq a\amp d\neq b\amp Rfd$. Since we now know that $Pf$ and $Rfd$, we know that $f=c$, since $c$ is, by definition, the unique object falling under $P$ which bears $R$ to $d$.
