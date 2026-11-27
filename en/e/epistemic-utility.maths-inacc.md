# epistemic-utility — maths-inacc（supplement）

> （《epistemic-utility》词条补充材料，源：plato.stanford.edu/entries/epistemic-utility/maths-inacc.html）

#### Supplement to Epistemic Utility Arguments for Epistemic Norms

## Agendas, States of the World, and Probability Functions

- A finite set of propositions forms an *algebra* if (i) it contains a tautology and a contradiction, and (ii) it is closed under negation, conjunction, and disjunction.
- Given a set of propositions $\mathcal{F}$ a world relative to $\mathcal{F}$ is a function $w : \mathcal{F} \rightarrow \{\mathsf{true}, \mathsf{false}\}$ such that
- $w(\top) = \mathsf{true}$ if $\top$ is a tautology; $w(\bot) = \mathsf{false}$ if $\bot$ is a contradiction;
- $w(\neg X) = \mathsf{true}$ iff $w(X) = \mathsf{false}$;
- $w(X \vee Y) = \mathsf{true}$ iff $w(X) = \mathsf{true}$ or $w(Y) = \mathsf{true} $;
- $w(X\ \&\ Y) = \mathsf{true}$ iff $w(X) = \mathsf{true}$ and $w(Y) = \mathsf{true} $; We write $\mathcal{W}_\mathcal{F}$ for the set of all worlds relative to $\mathcal{F}$.
- A function $P : \mathcal{F} \rightarrow [0, 1]$ is a probability function if (i) $P(\top) = 1$ and $P(\bot) = 0$, and (ii) $P(X \vee Y) = P(X) + P(Y)$ whenever $X$ and $Y$ are mutually exclusive.

## Epistemic Utility Arguments concerning Outright Beliefs

An individual’s belief set $\mathbf{B}$ is a subset of their agenda $\mathcal{F}$.

An epistemic utility function $EU$ for belief sets on agenda $\mathcal{F}$ is *Jamesian* if, for each $X$ in $\mathcal{F}$, there are $R_X, W_X \gt 0$ such that: $$ EU(\mathbf{B}, w) = \sum_{X \in \mathbf{B}\ \&\ w(X) = \mathsf{true}} R_X - \sum_{X \in \mathbf{B}\ \&\ w(X) = \mathsf{false}} W_X $$

A Jamesian epistemic utility function on $\mathcal{F}$ has *uniform ratio $t$* if $\frac{W_X}{R_X+W_X} = t$, for all $X$ in $\mathcal{F}$.

Then the Expectation Theorem for the Lockean Thesis follows from this lemma:

> **Expectation Lemma for the Lockean Thesis**. Suppose $P$ is a probability function on $\mathcal{F}$, $X$ is a proposition in $\mathcal{X}$, and $0 \lt R, W$. Then:
>
> 1. If $P(X) \gt \frac{W}{R+W}$, then $P(X) \times R + P(\neg X) \times (-W) \gt 0$.
> 2. If $P(X) = \frac{W}{R+W}$, then $P(X) \times R + P(\neg X) \times (-W) = 0$.

> **Dominance Theorem for Almost Lockean Completeness**. Suppose $\mathbf{B}$ is a belief set and $0 \leq t \leq 1$ is a threshold. Then the following are equivalent:
>
> 1. Relative to any Jamesian epistemic utility function with uniform ratio $t$, $\mathbf{B}$ is not strictly dominated;
> 2. $\mathbf{B}$ satisfies Almost Lockean Completeness with threshold $t$.

*Proof sketch for the Dominance Theorem for Almost Lockean Completeness*. First, we define a matrix. Suppose $\mathcal{F} = \{X_1, \ldots, X_n\}$ and $\mathcal{W}_\mathcal{F} = \{w_1, \ldots, w_m\}$. Then define the following matrix:

$$ \mathbf{D}_t = \left [ \begin{array}{ccc} d_{11} & \ldots & d_{1n} \\ \ldots & \ldots & \ldots \\ d_{m1} & \ldots & d_{mn} \end{array} \right ] $$

so that:

$$ d_{ij} = \left \{ \begin{array}{rl} 1-t & w_i(X_j) = \mathsf{true}\ &\ X_j \in \mathbf{B} \\ -(1-t) & w_i(X_j) = \mathsf{true}\ &\ X_j \not \in \mathbf{B} \\ -t & w_i(X_j) = \mathsf{false}\ &\ X_j \in \mathbf{B} \\ t & w_i(X_j) = \mathsf{false}\ &\ X_j \not \in \mathbf{B} \end{array} \right. $$

Then, second, we note that:

- $\mathbf{B}$ is not strictly dominated for any epistemic utility function with uniform ratio $t$ iff there is no vector $\mathbf{x}$ such that $\mathbf{x} \geq 0$ and $\mathbf{D}_t \cdot \mathbf{x} \lt 0$.
- $\mathbf{B}$ is Almost Lockean Complete with threshold $t$ iff there is a vector $\mathbf{y}$ such that $\mathbf{y} \geq 0$ and $\mathbf{y} \neq 0$ and $\mathbf{y} \cdot \mathbf{D}_t \geq 0$.

And finally we note the following theorem, known as Farkas’ Lemma, which says that the following are equivalent:

1. There is no vector $\mathbf{x}$ such that $\mathbf{x} \geq 0$ and $\mathbf{D}_t \cdot \mathbf{x} \lt 0$.
2. There is a vector $\mathbf{y}$ such that $\mathbf{y} \geq 0$ and $\mathbf{y} \neq 0$ and $\mathbf{y} \cdot \mathbf{D}_t \geq 0$.

QED.

The proof of the Dominance Theorem for Almost Lockean Completeness for Plans proceeds in a similar way.

## Epistemic Utility Arguments concerning Precise Credences

A credence function on $\mathcal{F}$ is a function $C : \mathcal{F} \rightarrow [0, 1]$.

$\mathcal{C}_\mathcal{F}$ is the set of credence functions on $\mathcal{F}$.

$\mathcal{P}_\mathcal{F} \subseteq \mathcal{C}_\mathcal{F}$ is the set of probabilistic credence functions on $\mathcal{F}$.

An epistemic utility function for credence functions on $\mathcal{F}$ is a function $EU : \mathcal{C}_\mathcal{F} \rightarrow [-\infty, 0]$.

### Probabilism and the Chance-Credence Norms

The Dominance Theorem for Probabilism and the Chance Dominance Theorem for the General Chance-Credence Norm both follow from the same fact about strictly proper epistemic utility functions, so we state that now:

> **Dominance Lemma for Convex Hulls**. Suppose $EU$ is continuous and strictly proper. And suppose $\mathcal{X} \subseteq \mathcal{P}$. Then:
>
> 1. For every $C$ that is not in in $\mathrm{cl}(\mathcal{X}^+)$, there is $C^*$ in $\mathrm{cl}(\mathcal{X}^+)$ such that, for all $P$ in $\mathcal{X}$, $$ \sum_{w \in \mathcal{W}} P(w)EU(C, w) \lt \sum_{w \in \mathcal{W}} P(w)EU(C^*, w) $$
> 2. For every $C$ in $\mathrm{cl}(\mathcal{X}^+)$ and any $C^* \neq C$ there is $P$ in $\mathcal{X}$ such that, $$ \sum_{w \in \mathcal{W}} P(w)EU(C^*, w) \lt \sum_{w \in \mathcal{W}} P(w)EU(C, w) $$

*Proof sketch for the Dominance Theorem for Convex Hulls*. The trick is to use the epistemic utility function to define something like a measure of distance from any probabilistic credence function to any other credence function. Given $EU$ and credence functions $P$, $C$, where $P$ is probabilistic, define $D_{EU}(P, C)$ to be the difference between the expected epistemic utility of $C$ from the point of view of $P$ and the expected epistemic utility of $P$ from the point of view of $P$: that is,

$$ D_{EU}(P, C) = \mathrm{Exp}_P(EU(P)) - \mathrm{Exp}_P(EU(C)) $$

We can then show that, for any set $\mathcal{X}$ of probabilistic credence functions, if $C$ lies outside $\mathrm{cl}(\mathcal{X}^+)$, then the function $D_{EU}(-, C)$ takes a minimum value on $\mathrm{cl}(\mathcal{X}^+)$. And we can show that, if $C^*$ is the credence function at which it takes that minimum value, then, for all $P$ in $\mathcal{X}$,

$$ D_{EU}(P, C^*) \lt D_{EU}(P, C) $$

And so, unpacking the definition of $D_{EU}$,

$$ \mathrm{Exp}_P(EU(C)) \lt \mathrm{Exp}_P(EU(C^*)) $$

as required.

Then:

- the Dominance Theorem for Probabilism follows from this if we let $\mathcal{X}$ be the set of omniscient credence functions, $V_w$ for $w$ in $\mathcal{W}$, since $\mathcal{P}$ is the closed convex hull of that set;
- the Chance Dominance Theorem for the General Chance-Credence Norm follows if we let $\mathcal{X}$ be the set of possible chance functions.

### Conditionalization

1. An *evidential situation* is a function $\mathcal{E}$ that takes a possible world $w$ and returns the proposition $\mathcal{E}(w)$ learned at that possible world in that evidential situation.
2. An *updating rule* is a function $R$ that takes a possible world $w$ and returns the credence function $R_w$ endorsed by that plan at that world.
3. An updating rule $R$ is *available* at an evidential situation $\mathcal{E}$ if, whenever $\mathcal{E}(w) = \mathcal{E}(w')$, we have $R_w = R_{w'}$.
4. An evidential situation is *factive* if, for every world $w$, $\mathcal{E}(w)$ is true at $w$.
5. An evidential situation is *partitional* if $\{\mathcal{E}(w) : w \in \mathcal{W}\}$ forms a partition.
6. An updating rule $R$ is a *conditionalizing rule for prior credence function $C$ and evidential situation $\mathcal{E}$* if, for every world $w$, if $C(\mathcal{E}(w)) \lt 0$, then $R_w(-) = C(- \mid \mathcal{E}(w))$.

> **Expectation Theorem for Partitional Plan Conditionalization**. Suppose $EU$ is strictly proper, $\mathcal{E}$ is a factive and partitional evidential situation, and $C$ is a probabilistic credence function. Then:
>
> 1. For any updating rules $R, R'$, if $R$ and $R'$ are both conditionalizing rules for $C$ and $\mathcal{E}$, $$ \sum_{w \in \mathcal{W}} C(w)EU(R_w, w) = \sum_{w \in \mathcal{W}} C(w)EU({R'}_w, w) $$
> 2. For any available updating rules $R, R'$, if $R$ is a conditionalizing rule for $C$ and $\mathcal{E}$, but $R'$ is not, then $$ \sum_{w \in \mathcal{W}} C(w)EU(R'_w, w) \lt \sum_{w \in \mathcal{W}} C(w)EU(R'_w, w) $$

*Proof sketch for the Expectation Theorem for Partitional Plan Conditionalization*. We prove (ii). Since $\mathcal{E}$ is partitional, let $\{\mathcal{E}(w) : w \in \mathcal{W}\} = \{E_1, \ldots, E_n\}$, write $R_i$ for the credence function that $R$ recommends at each world at which $E_i$ is true and write $R'_i$ for the credence function that $R'$ recommends at each world at which $E_i$ is true. Then, for each $E_i$ with $C(E_i) \gt 0$, since $EU$ is strictly proper and $R_i$ is a probabilistic credence function,

$$ \sum_{w \in \mathcal{W}} R_i(w)EU(R'_i, w) \leq \sum_{w \in \mathcal{W}} R_i(w)EU(R_i, w) $$

with strict inequality if $R_i \neq R'_i$. But $R_i(-) = C(-\mid E_i)$, so

$$ \sum_{w \in \mathcal{W}} C(w\mid E_i)EU(R'_i, w) \leq \sum_{w \in \mathcal{W}} C(w \mid E_i)EU(R_i, w) $$

again with strict inequality if $R_i \neq R'_i$. And so

$$ \sum_{w \in E_i} C(w)EU(R'_i, w) \leq \sum_{w \in E_i} C(w)EU(R_i, w) $$

again with strict inequality if $R_i \neq R'_i$. Since $R_i$ is conditionalizing and $R'_i$ is not, there is some $E_i$ such that $R_i \neq R'_i$, and so

$$ \sum_{E_i}\sum_{w \in E_i} C(w)EU(R'_i, w) \lt \sum_{E_i}\sum_{w \in E_i} C(w)EU(R_i, w) $$

And so

$$ \sum_{w \in \mathcal{W}} C(w)EU(R'_w, w) \lt \sum_{w \in \mathcal{W}} C(w)EU(R_w, w) $$

as required.

**Dominance Theorem for Partitional Plan Conditionalization**. Suppose $EU$ is additive, continuous, and strictly proper, $\mathcal{E}$ is a factive and partitional evidential situation, $C$ is a probabilistic credence function, and $R$ is an available updating plan in $\mathcal{E}$. Then:

1. If $R$ is not a conditionalizing plan for $C$ and $\mathcal{E}$, there is a credence function $C^*$ and an updating plan $R^*$ that is available in $\mathcal{E}$ such that, for all $w$ in $\mathcal{W}$, $$ EU(C, w) + EU(R_w, w) \lt EU(C^*, w) + EU(R^*_w, w) $$
2. If $R$ is a conditionalizing plan for $C$ and $\mathcal{E}$, then there is no credence function $C^*$ and updating plan $R^*$ that is available in $\mathcal{E}$ such that, for all $w$ in $\mathcal{W}$, $$ EU(C, w) + EU(R_w, w) \lt EU(C^*, w) + EU(R^*_w, w) $$

*Proof sketch for the Dominance Theorem for Partitional Plan Conditionalization*. We'll sketch the proof of (i). Suppose $EU(C, w) = \sum_{X \in \mathcal{F}} s(V_w(X), C(X))$. Then we define a measure of distance from one credence function to another as follows:

- First, given two credences, $p$ and $q$, define $d_s(p, q) = (ps(1, p) - (1-p)s(0,p)) - (ps(1, q) - (1-p)s(0,q))$.
- Second, given two credence functions, $C, C'$, define $D_s(C, C') = \sum_{X \in \mathcal{F}} d_s(C(X), C'(X))$.

Next, since $\mathcal{E}$ is partitional, let $\{E(w) : w \in \mathcal{W}\} = \{E_1, \ldots, E_n\}$. Now suppose $R$ is an available updating plan in $\mathcal{E}$, and write $R_i$ for the credence function it endorses at any world at which $E_i$ is true. Next, write $\mathcal{F} = \{X_1, \ldots, X_m\}$, represent a credence function $C$ by the vector $(C(X_1), \ldots, C(X_m))$, write $C \frown C'$ for the concatenation of $C$ and $C'$, which is $(C(X_1), \ldots, C(X_m), C'(X_1), \ldots, C'(X_m))$, and define

> $ \overline{R} = \{V_w \frown R_1 \frown \ldots \frown R_{i-1} \frown V_w \frown R_{i+1} \frown \ldots \frown R_n : $
>     $ i = 1, \ldots, n\ \&\ w \in E_i\} $

Then, if $R$ is not a conditionalizing plan for $C$,

$$ C \frown R_1 \frown \ldots \frown R_n \not \in \overline{R}^+ $$

It then follows that there is a credence function $C^*$ and an updating rule $R^*$ that is available in $\mathcal{E}$ such that

$$ C^* \frown R^*_1 \frown \ldots \frown R^*_n \in \overline{R}^+ $$

such that, for all $i = 1, \ldots, n$ and all $w$ in $E_i$,

> $ D_s(V_w, C) + D_s(R_1, R_1) + \ldots + D_s(R_{i-1}, R_{i-1})\ + $
>     $ D_s(V_w, R_i) + D_s(R_{i+1}, R_{i+1}) + \ldots + D_s(R_n, R_n)\ \gt $
> $ D_s(V_w, C^*) + D_s(R_1, R^*_1) + \ldots + D_s(R_{i-1}, R^*_{i-1})\ + $
>     $D_s(V_w, R^*_i) + D_s(R_{i+1}, R^*_{i+1}) + \ldots + D_s(R_n, R^*_n) $

But then, since $D_s(C, C) = 0$, $D_s(R_i, R_i) = 0$, and $D_s(R_i, R^*_i) \geq 0$,

$$ D_s(V_w, C) + D_s(V_w, R_i) \gt D_s(V_w, C^*) + D_s(V_w, R^*_i) $$

And so

$$ EU(C, w) + EU(R_i, w) \lt EU(C^*, w) + EU(R^*_i, w) $$

as required.
