# epistemic-game — supplement（supplement）

> （《epistemic-game》词条补充材料，源：plato.stanford.edu/entries/epistemic-game/supplement.html）

#### Supplement to Epistemic Foundations of Game Theory

## Supplement to Epistemic Foundations of Game Theory

### 1. Proof of Lemma 3.2

**Lemma 3.2** Suppose that $G=\langle N, (S_i)_{i\in N}, (u_i)_{i\in N}\rangle$ is a strategic game. A strategy $s_i\in S_i$ is strictly dominated (possibly by a mixed strategy) with respect to $X\subseteq S_{-i}$ iff there is no probability measure $p\in \Delta(X)$ such that $s_i$ is a best response with respect to $p$.

*Proof:* We start with some preliminary observations. Let $G=\langle \{1, 2\}, (S_1, S_2), (u_1, u_2)\rangle $ be a two-player strategic game. Recall that $\Delta(S_1)$ and $\Delta(S_2)$ denote the mixed strategies for players 1 and 2, respectively. For $p_1\in \Delta(S_1)$, $p_2\in \Delta(S_2)$, we write $U_1(p_1, p_2)$ (respectively $U_2(p_1,p_2)$) for the expected utility that player $1$ (respectively $2$) receives when $1$ uses the mixed strategy $p_1$ and $2$ uses the mixed strategy $p_2$. We assume that the players’ choices are independent, so we have the following calculation for $i=1,2$:

$$U_i(p_1, p_2)=\sum_{x\in S_1}\sum_{y\in S_2} p_1(x)p_2(y) u_i(x,y)$$

A two-player game $G=\langle S_1, S_2, u_1, u_2\rangle $ is **zero-sum** provided for each $x\in S_1$ and $y\in S_2$, $u_1(x,y)+u_2(x,y)=0$. We make use of the following fundamental theorem of von Neumann:

**Theorem S2 (von Neumann’s minimax theorem)** For every two-player zero- sum game with finite strategy sets $S_1$ and $S_2$, there is a number $v$, called the **value** of the game such that:

1. $v =\max_{p\in\Delta(S_1)}\min_{q\in \Delta(S_2)} U_1(p,q)$ $ = \min_{q\in \Delta(S_2)}\max_{p\in\Delta(S_1)} U_1(p,q)$
2. The set of mixed Nash equilibria is nonempty. A mixed strategy profile $(p,q)$ is a Nash equilibrium if and only if $$ \begin{multline} \shoveleft p\in \textrm{argmax}_{p\in\Delta(S_1)}\min_{q\in\Delta(S_2)} U_1(p,q) \\ \shoveleft q\in \textrm{argmax}_{q\in\Delta(S_2)}\min_{p\in\Delta(S_1)} U_1(p,q) \\ \end{multline} $$
3. For all mixed Nash equilibria $(p,q)$, $U_1(p,q)=v$

Now, we can proceed with the proof of the Lemma. Suppose that $G=\langle N, \{S_i, u_i\}_{i\in N}\rangle$ is a strategic game where each $S_i$ is finite.

Suppose that $s_i\in S_i$ is strictly dominated with respect to $X$. Then there is a $s_i \in S_i$ such that for all $s_{-i}\in X$,

$$u_i(s_i',s_{-i}) > u_i(s_i,s_{-i}).$$

Let $p\in\Delta(X)$ be any probability measure. Then for all $s_{-i}\in X$, $0\le p(s_{-i})\le 1$. This means that for all $s_{-i}\in X$, we have

$$p(s_{-i})\cdot u_i(s_i',s_{-i}) \ge p(s_{-i})\cdot u_i(s_i,s_{-i}),$$

and there is at least one $s_{-i}\in S_{-i}$ such that

$$p(s_{-i})\cdot u_i(s_i',s_{-i}) > p(s_{-i})\cdot u_i(s_i,s_{-i})$$

(this follows since $p$ is a probability measure on $X$, so cannot assign probability 0 to all elements of $X$). Hence,

$$\sum_{s_{-i}\in S_{-i}} p(s_{-i})\cdot u_i(s_i',s_{-i})> \sum_{s_{-i}\in S_{-i}}p(s_{-i})\cdot u_i(s_i,s_{-i})$$

So, $EU(s_i',p)> EU(s_i,p)$, which means $s_i$ is not a best response to $p$.

For the converse direction, we sketch the proof for two player games. The proof of the more general statement uses the *supporting hyperplane theorem* from convex analysis. We do not discuss this extension here (note that it is not completely trivial to extend this result to the many agent case as we must allow players to have beliefs about *correlated* choices of their opponents). Let $G=\langle S_1, S_2, u_1, u_2\rangle$ be a two-player game. Suppose that $\alpha\in \Delta(S_1)$ is not a best response to any $p\in\Delta(S_2)$. This means that for each $p\in \Delta(S_2)$ there is a $q\in\Delta(S_1)$ such that $U_1(q,p)>U_1(\alpha,p)$. We can define a function $b:\Delta(S_2)\rightarrow \Delta(S_1)$ where, for each $p\in\Delta(S_2)$, $U_1(b(p),p)>U_1(\alpha,p)$.

Consider the game $(S_1, S_2, \ou_1, \ou_2)$ where

$$\ou_1(s_1, s_2)=u_1(s_1,s_2) - U_1(\alpha, s_2)$$

and $\ou_2(s_1,s_2)=-\ou_1(s_1,s_2)$. This is a 2-person, zero-sum game, and so by the von Neumann minimax theorem, there is a mixed strategy Nash equilibrium $(p_1^*, p_2^*)$. Then, by the minimax theorem, for all $m\in\Delta(S_2)$, we have

$$\oU(p_1^*, m) \ge \oU_1(p_1^*, p_2^*) \ge \oU_1(b(p_2^*),p_2^*)$$

We now prove that $\oU_1(b(p_2^*),p_2^*)> \oU_1(\alpha,p_2^*)$:

$$ \begin{align*} \oU_1(b(p_2^*),p_2^*) &= \sum_{x\in S_1}\sum_{y\in S_2} b(p_2^*)(x)p_2^*(y)\ou_1(x,y)\\ &= \sum_{x\in S_1}\sum_{y\in S_2} b(p_2^*)(x)p_2^*(y)[u_1(x,y) - U_1(\alpha, y)]\\ &= \sum_{x\in S_1}\sum_{y\in S_2} b(p_2^*)(x)p_2^*(y)u_1(x,y) \\ &\quad\quad\quad - \sum_{x\in S_1}\sum_{y\in S_2} b(p_2^*)(x)p_2^*(y)U_1(\alpha, y)\\ &= U_1(b(p_2^*), p_2^*) - \sum_{x\in S_1}\sum_{y\in S_2} b(p_2^*)(x)p_2^*(y)U_1(\alpha, y)\\ &> U_1(\alpha,p_2^*) - \sum_{x\in S_1}\sum_{y\in S_2} b(p_2^*)(x)p_2^*(y)U_1(\alpha, y)\\ &> U_1(\alpha,p_2^*) \end{align*} $$

Since $p_2^*(y) U_1(\alpha, y)$ does not depend on $x$, we have

$$ \begin{align*} \sum_{x\in S_1}\sum_{y\in S_2} b(p_2^*)(x)p_2^*(y)U_1(\alpha, y) &= \sum_{x\in S_1} b(p_2^*)(x)\sum_{y\in S_2}p_2^*(y)U_1(\alpha,y)\\ &= \sum_{x\in S_1}b(p_2^*)(x)U_1(\alpha, p_2^*)\\ &= U_1(\alpha,p_2^*)\sum_{x\in S_1}b(p_2^*)(x)\\ &=U_1(\alpha,p_2^*) \end{align*}$$

Hence, for all $m\in\Delta(S_2)$ we have $\oU_1(s_1^*,m)>0$ which implies for all $m\in\Delta(S_2)$, $U_1(s_1^*,m) > U_1(\alpha, m)$, and so *α* is strictly dominated by $p_1^*$. QED

### 2. Proof of Theorem 2.9

**Theorem 2.9 (Brandenburger & Keisler 2006: Theorem 5.4)** There is no assumption-complete type structure for the set of conjectures that contain the first-order definable subsets.

To prove this theorem, we follow an idea from Abramsky & Zvesper (2015). Suppose that $\cC_a\subseteq\pow(T_a)$ is a set of *conjectures* about Ann states (similarly, let $\cC_b\subseteq\pow(T_b)$ be a set of conjectures about Bob states). We start with the flowing assumption:

For all $X\in \cC_a$ there is a $x_0\in T_a$ such that

1. $\lambda_a(x_0)\ne\emptyset$: “in state $x_0$, Ann has consistent beliefs”
2. $\lambda_a(x_0)\subseteq \{y \mid \lambda_b(y)=X\}$: “in state $x_0$, Ann believes that Bob assumes $X$”

To prove the theorem, we need the following lemma.

**Lemma S1** Under the above assumption, for each $X\in \cC_a$ there is an $x_0$ such that $$x_0\in X\text{ iff there is a \(y\in T_b\) such that \(y\in \lambda_a(x_0)\) and \(x_0\in\lambda_b(y)\)}$$

*Proof of Lemma S1:* Suppose that $X\in\cC_a$. Then there is an $x_0\in T_a$ satisfying 1 and 2.

Suppose that $x_0\in X$. By 1., $\lambda_a(x_0)\ne\emptyset$ so there is a $y_0\in T_b$ such that $y_0\in\lambda_a(x_0)$. We show that $x_0\in\lambda_b(y_0)$. By 2., we have $y_0\in\lambda_a(x_0)\subseteq \{y \mid \lambda_b(y)=X\}$. Hence, $x_0\in X=\lambda_b(y_0)$, as desired.

Suppose that there is a $y_0\in T_b$ such that $y_0\in\lambda_a(x_0)$ and $x_0\in \lambda_b(y_0)$. By 2., $y_0\in\lambda_a(x_0)\subseteq \{y \mid \lambda_b(y)=X\}$. Hence, $x_0\in\lambda_b(y_0)=X$, as desired. QED

Consider a first-order language $\L$ whose signature contains binary relational symbols $R_a(x,y)$ and $R_b(x,y)$ defining $\lambda_a$ and $\lambda_b$ respectively. The language $\L$ is interpreted over qualitative type structures where the interpretation of $R_a$ is the set $\{(t,s) \mid t\in T_a, s\in T_b, \text{ and }s\in\lambda_a(t)\}$.

*Proof of Theorem 2.9.* Consider the formula *φ* in $\L$: $$\phi(x):=\exists y (R_a(x,y) \wedge R_b(y,x))$$

Then, the negation of *φ* is:

$\neg\phi(x):=\forall y(R_a(x,y)\rightarrow\neg R_b(y,x))$: “all states $x$ where any state $y$ that Ann considers possible is such that Bob does not consider $x$ possible at $y$”. That is, this formulas says that “Ann believes that Bob’s assumption is *wrong*”.

Suppose that $X\in\cC_a$ is defined by the formula $\neg\phi(x)$.

Suppose that there is a $x_0\in T_a$ such that

1. $\lambda_a(x_0)\ne\emptyset$: Ann’s beliefs at $x_0$ are consistent.
2. $\lambda_a(x_0)\subseteq \{y \mid \lambda_b(y)=X\}$: At $x_0$, Ann believes that Bob assumes $X=\{x \mid \phi(x)\}$ (i.e., Ann believes that Bob assumes that Ann believes that Bob’s assumption is wrong.)

We have

$$ \begin{align} \neg\phi(x_0) \text{ is true } &\text{iff } x_0 \in X &\text{(defn of \(X\))} \\ &\text{iff } \text{there is a } y\in T_b \text{ with } y\in\lambda_a(x_0) \\ &\quad\quad\text{and } x_0\in \lambda_b(y) &\text{(Lemma S1)}\\ &\text{iff } \phi(x_0) \text{ is true}. &\text{(defn of \(\phi(x)\))} \end{align} $$

QED
