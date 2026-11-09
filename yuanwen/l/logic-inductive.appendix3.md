# logic-inductive — appendix3（supplement）

> （《logic-inductive》词条补充材料，源：plato.stanford.edu/entries/logic-inductive/appendix3.html）

#### Supplement to Inductive Logic

## Appendix 3: Derivations of the Two Bayesian Estimation Rules, *Rule BE-D* and *Rule BE-C*

We restate each rule, *BE-D* and *BE-C*, and provide proofs of their claims along the way.

### Rule BE-D: Bayesian Estimation for Disjunctions of Alternative Hypotheses

Let $H$ be a collection of $z$ alternative hypotheses, $z \ge 2$, where the conjunction of any two of them is logically inconsistent. Let $c$ be observational or experimental conditions for which $e$ describes one of the possible outcomes. And suppose $b$ is a conjunction of relevant auxiliary hypotheses and plausibility considerations. For each hypothesis $h$ in $H$, let its prior probability be non-zero: $P[h \mid c \cdot b] \gt 0$.

Choose any $k$ hypotheses from collection $H$, where each one of them, $h$, has a likelihood value $P[e \mid h \cdot c \cdot b] > 0$. Label these $k$ hypotheses (in whatever order you wish) as $\lsq h_1\rsq$, $\lsq h_2\rsq$, …, $\lsq h_k\rsq$. Then label all the remaining hypotheses in $H$ (in whatever order you wish) as $\lsq h_{k+1}\rsq$, $\lsq h_{k+2}\rsq$, …, $\lsq h_z\rsq$.

Given these labelings of hypotheses in $H$, let $(h_1 \vee \ldots \vee h_k)$ represent the disjunction of the first $k$ hypotheses chosen from $H$, and $(h_{k+1} \vee \ldots \vee h_z)$ represent the disjunction of the remaining hypotheses from $H$. The expression $(h_1 \vee \ldots \vee h_z)$ represents the disjunction of all hypotheses in $H$. Furthermore, let $b$ logically entail this disjunction of all alternative hypotheses in $H$: $b \vDash (h_1 \vee \ldots \vee h_z)$. So, both $P[(h_1 \vee \ldots \vee h_z) \mid c \cdot b] = 1$ and $P[(h_1 \vee \ldots \vee h_z) \mid c \cdot e \cdot b] = 1$.

Then, the posterior probability of $(h_1 \vee \ldots \vee h_k)$ satisfies the following form of Bayes’ Theorem:

$$ P[(h_1 \vee \ldots \vee h_k) \mid c \cdot e \cdot b] \; \; = \; \; \frac{\sum_{j = 1}^k P[e \mid h_j \cdot c \cdot b] \times P[h_j \mid c \cdot b]}{\sum_{i = 1}^z P[e \mid h_i \cdot c \cdot b] \times P[h_i \mid c \cdot b]}. $$

*Proof*:

Since $P[(h_1 \vee \ldots \vee h_z) \mid c \cdot e \cdot b] = 1$, we have

$$\begin{align} &P[(h_1 \vee \ldots \vee h_k) \mid c \cdot e \cdot b] \\ &\qquad = \frac{P[(h_1 \vee \ldots \vee h_k) \mid c \cdot e \cdot b]}{P[(h_1 \vee \ldots \vee h_z) \mid c \cdot e \cdot b]} \\ &\qquad = \frac{\sum_{j = 1}^k P[h_j \mid c \cdot e \cdot b]}{\sum_{i = 1}^z P[h_i \mid c \cdot e \cdot b]} \\ &\qquad = \frac{\sum_{j = 1}^k P[h_j \mid c \cdot e \cdot b] \times P[e \mid c \cdot b]}{\sum_{i = 1}^z P[h_i \mid c \cdot e \cdot b] \times P[e \mid c \cdot b]} \\ &\qquad = \frac{\sum_{j = 1}^k P[h_j \cdot e \mid c \cdot b]}{\sum_{i = 1}^z P[h_i \cdot e \mid c \cdot b]} \\ &\qquad = \frac{\sum_{j = 1}^k P[e \mid h_j \cdot c \cdot b] \times P[h_j \mid c \cdot b]}{\sum_{i = 1}^z P[e \mid h_i \cdot c \cdot b] \times P[h_i \mid c \cdot b]}. \end{align}$$

In cases where the values of all the prior probabilities, $P[h_i \mid c \cdot b]$, are known, or can be closely approximated, this equation suffices to provide values for the argument strengths $r$ of the posterior probabilities, $P[(h_1 \vee \ldots \vee h_k) \mid c \cdot e \cdot b] = r$. But when no precise values of the priors are available, a useful estimate of bounds on the posterior probabilities may be derived as follows.

Let $K$ be (your best estimate of) an upper bound on the ratios of prior probabilities, $P[h_i \mid c \cdot b] / P[h_j \mid c \cdot b]$ for all $h_j$ in $\{h_1, h_2, \ldots, h_k\}$ and all $h_i$ in $\{h_{k+1}, h_{k+2}, \ldots, h_z\}$. That is, for whichever $h_j$ in $\{h_1, h_2, \ldots, h_k\}$ has the smallest value of $P[h_j \mid c \cdot b]$, and for whichever $h_i$ in $\{h_{k+1}, h_{k+2}, \ldots, h_z\}$ has the largest value of $P[h_i \mid c \cdot b]$, let $K$ be a real number that is large enough that $K \ge P[h_i \mid c \cdot b] / P[h_j \mid c \cdot b]$.

Then, $$ \Omega[\neg (h_1 \vee \ldots \vee h_k) \mid c \cdot e \cdot b] \; \; \le \; \; K \times \left[\frac{1}{\frac{\sum_{j = 1}^k P[e \;\mid\; h_j \cdot c \cdot b]}{\sum_{i = 1}^z P[e \;\mid\; h_i \cdot c \cdot b]}} - 1 \right]. $$

*Proof*:

$$\begin{align} &\Omega[\neg (h_1 \vee \ldots \vee h_k) \mid c \cdot e \cdot b] \\ &\quad = \frac{P[(h_{k+1} \vee \ldots \vee h_z) \mid c \cdot e \cdot b]}{P[(h_1 \vee \ldots \vee h_k) \mid c \cdot e \cdot b]} \\ &\quad = \frac{\sum_{i = k+1}^z P[e \mid h_i \cdot c \cdot b] \times P[h_i \mid c \cdot b]}{\sum_{j = 1}^k P[e \mid h_j \cdot c \cdot b] \times P[h_j \mid c \cdot b]} \\ &\quad \le K \times \frac{\sum_{i = k+1}^z P[e \mid h_i \cdot c \cdot b]}{\sum_{j = 1}^k P[e \mid h_j \cdot c \cdot b]} \\ &\quad = K \times \left[\frac{\sum_{i = k+1}^z P[e \mid h_i \cdot c \cdot b] + \sum_{j = 1}^k P[e \mid h_j \cdot c \cdot b]}{\sum_{j = 1}^k P[e \mid h_j \cdot c \cdot b]} - 1\right] \\ &\quad = K \times \left[\frac{\sum_{i = 1}^z P[e \mid h_i \cdot c \cdot b]}{\sum_{j = 1}^k P[e \mid h_j \cdot c \cdot b]} - 1\right] \\ &\quad = K \times \left[\frac{1}{\frac{\sum_{j = 1}^k P[e \;\mid\; h_j \cdot c \cdot b]}{\sum_{i = 1}^z P[e \;\mid\; h_i \cdot c \cdot b]}} - 1 \right]. \end{align}$$ Thus, a lower bound on the associated posterior probability of $(h_1 \vee \ldots \vee h_k)$ is given by the formula $$\begin{align} P[(h_1 \vee \ldots \vee h_k) \mid c \cdot e \cdot b] \; \; &= \; \; \frac{1}{1 + \Omega[\neg (h_1 \vee \ldots \vee h_k) \mid c \cdot e \cdot b]} \\ &\ge \; \; \frac{1}{1 + K \times \left[\frac{1}{\frac{\sum_{j = 1}^k P[e \;\mid\; h_j \cdot c \cdot b]}{\sum_{i = 1}^z P[e \;\mid\; h_i \cdot c \cdot b]}} - 1 \right]}. \end{align}$$

### Rule BE-C: Bayesian Estimation for a Continuous Range of Alternative Hypotheses

Let $H$ be a continuous region of alternative hypotheses $h_q$, where $q$ is a real number, and where the conjunction of any two of these hypotheses is logically inconsistent. Let $c$ be observational or experimental conditions for which $e$ describes one of the possible outcomes. And suppose $b$ is a conjunction of relevant auxiliary hypotheses and plausibility considerations. For each point hypothesis $h_q$ in $H$, we take $p[e \mid h_q \cdot c \cdot b]$ to be an appropriate likelihood.

Let $p[h_q \mid c \cdot b]$ and $p[h_q \mid c \cdot e \cdot b]$ be probability density functions on $H$, where these two density functions are related as follows: $$p[h_q \mid c \cdot e \cdot b] \times P[e \mid c \cdot b] \;=\; p[e \mid h_q \cdot c \cdot b] \times p[h_q \mid c \cdot b].$$

We suppose throughout that prior probability density $p[h_q \mid c \cdot b] > 0$ for all values of $q$.

The prior probability that the true point hypothesis $h_r$ lies within measurable region $R$ is given by

$$\begin{align} P[h_R \mid c \cdot b] \; &= \; \int_R p[h_r \mid c \cdot b] \; dr,\;\; \text{where} \\ P[h_H \mid c \cdot b] \; &= \; \int_H p[h_q \mid c \cdot b] \; dq \: =\: 1. \end{align}$$

The posterior probability that the true point hypothesis $h_r$ lies within measurable region $R$ is given by

$$\begin{align} P[h_R \mid c \cdot e \cdot b] \; &= \; \int_R p[h_r \mid c \cdot e \cdot b] \; dr, \;\; \text{where} \\ P[h_H \mid c \cdot e \cdot b] \; &= \; \int_H p[h_q \mid c \cdot e \cdot b] \; dq \: =\: 1. \end{align}$$

Then, the posterior probability satisfies the following equation for each measurable region $R$: $$ P[h_R \mid c \cdot e \cdot b] = \frac{\int_R p[e \mid h_r \cdot c \cdot b] \times p[h_r \mid c \cdot b] \; \; dr}{\int_H p[e \mid h_q \cdot c \cdot b] \times p[h_q \mid c \cdot b] \; \; dq}. $$

*Proof*:

Since $P[h_H \mid c \cdot e \cdot b] = 1$, we have

$$\begin{align} P[h_R \mid c \cdot e \cdot b] \; &= \; \frac{P[h_R \mid c \cdot e \cdot b]}{P[h_H \mid c \cdot e \cdot b]} \\ &= \; \frac{\int_R p[h_R \mid c \cdot e \cdot b] \; \; dr}{\int_H p[h_q \mid c \cdot e \cdot b] \; \; dq} \\ &= \; \frac{\int_R p[h_R \mid c \cdot e \cdot b] \times P[e \mid c \cdot b] \; \; dr}{\int_H p[h_q \mid c \cdot e \cdot b] \times P[e \mid c \cdot b] \; \; dq} \\ &= \; \frac{\int_R p[e \mid h_r \cdot c \cdot b] \times p[h_r \mid c \cdot b] \; \; dr}{\int_H p[e \mid h_q \cdot c \cdot b] \times p[h_q \mid c \cdot b] \; \; dq} \end{align}$$

In cases where a precise model of the prior probability density, $p[h_q \mid c \cdot b]$, is available, this equation suffices to provide values for the posterior probabilities, $P[h_R \mid c \cdot e \cdot b]$. However, when no precise model of the priors is available, bounds on the values of posterior probabilities may be evaluated in the following way.

Let $K$ be (your best estimate of) an upper bound on the ratios of the probability density values, $p[h_q \mid c \cdot b] / p[h_r \mid c \cdot b]$, for each $h_r$ in region $R$ and $h_q$ in $(H-R)$. That is, for whichever $h_r$ in $R$ has the smallest value of $p[h_r \mid c \cdot b]$, and for whichever $h_q$ in $(H-R)$ has the largest value of $p[h_q \mid c \cdot b]$, let $K$ be a real number such that $K \ge p[h_q \mid c \cdot b] / p[h_r \mid c \cdot b]$.

Then, $$ \Omega[\neg h_R \mid c \cdot e \cdot b] \; \; \le \; \; K \times \left[\frac{1}{\frac{\int_{R} p[e \;\mid\; h_r \cdot c \cdot b] \; \; dr}{\int_{H} p[e \;\mid\; h_q \cdot c \cdot b] \; \; dq}} - 1 \right]. $$

*Proof*:

$$\begin{align} &\Omega[\neg h_R \mid c \cdot e \cdot b] \\ &\quad = \frac{P[h_{H-R} \mid c \cdot e \cdot b]}{P[h_R \mid c \cdot e \cdot b]} \\ &\quad = \frac{\int_{H-R} p[h_q \mid c \cdot e \cdot b] \; \; dq}{\int_{R} p[h_r \mid c \cdot e \cdot b] \; \; dr} \\ &\quad = \frac{\int_{H-R} p[h_q \mid c \cdot e \cdot b] \times P[e \mid c \cdot b] \; \; dq}{\int_{R} p[h_r \mid c \cdot e \cdot b] \times P[e \mid c \cdot b] \; \; dr}\\ &\quad = \frac{\int_{H-R} p[e \mid h_q \cdot c \cdot b] \times p[h_q \mid c \cdot b] \; \; dq}{\int_{R} p[e \mid h_r \cdot c \cdot b] \times p[h_r \mid c \cdot b] \; \; dr}\\ &\quad \le K \times \frac{\int_{H-R} p[e \mid h_q \cdot c \cdot b] \; \; dq}{\int_{R} p[e \mid h_r \cdot c \cdot b] \; \; dr} \\ &\quad = K \times \left[\frac{\int_{H-R} p[e \mid h_q \cdot c \cdot b] \; \; dq \;\; + \;\; \int_{R} p[e \mid h_r \cdot c \cdot b] \; \; dr}{\int_{R} p[e \mid h_r \cdot c \cdot b] \; \; dr} - 1 \right] \\ &\quad = K \times \left[\frac{\int_{H} p[e \mid h_q \cdot c \cdot b] \; \; dq}{\int_{R} p[e \mid h_r \cdot c \cdot b] \; \; dr} - 1 \right] \\ &\quad = K \times \left[\frac{1}{\frac{\int_{R} p[e \;\mid\; h_r \cdot c \cdot b] \; \; dr}{\int_{H} p[e \;\mid\; h_q \cdot c \cdot b] \; \; dq}} - 1 \right]. \end{align}$$

Thus, a lower bound on the associated posterior probability of $h_R$ is given by the formula

$$\begin{align} P[h_R \mid c \cdot e \cdot b] \;\; &= \;\; \frac{1}{1 + \Omega[\neg h_R \mid c \cdot e \cdot b]} \\ &\ge \; \; \frac{1}{1 + K \times \left[\frac{1}{\frac{\int_{R} \; p[e \;\mid\; h_r \;\cdot\; c \cdot b] \; \; dr}{\int_{H} \; p[e \;\mid\; h_q \cdot c \cdot b] \; \; dq}} - 1 \right]}. \end{align}$$
