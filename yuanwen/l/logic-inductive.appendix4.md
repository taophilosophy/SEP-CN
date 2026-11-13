# logic-inductive — appendix4（supplement）

> （《logic-inductive》词条补充材料，源：plato.stanford.edu/entries/logic-inductive/appendix4.html）

#### Supplement to Inductive Logic

## Appendix 4

## An Epistemic Advantage of Drawing on Well-Supported Auxiliary Hypotheses

Suppose that hypothesis $h_i$ does very poorly as compared to $h_j$ on evidence $(c \cdot e)$ relative to the best supported (conjunction of) auxiliaries $a$ — i.e. $P[h_i \mid (c \cdot e) \cdot (a \cdot d)] / P[h_j \mid (c \cdot e) \cdot (a \cdot d)]$ is quite small, due to the very small size of the likelihood ratio $P[e \mid h_i \cdot c \cdot (a \cdot d)] / P[e \mid h_j \cdot c \cdot (a \cdot d)]$. And suppose that for an alternative (conjunction of) auxiliaries, $a_r$, hypothesis $h_i$ does much better on the same evidence — i.e. the likelihood ratio $P[e \mid h_i \cdot c \cdot (a_r \cdot d)] / P[e \mid h_j \cdot c \cdot (a \cdot d)]$ is much larger than 1. (Here $h_j$ continues to draw on the best supported auxiliary, $a$.) This situation clearly calls for testing $(h_i \cdot a_r)$, the conjunction of $h_i$ with its assisting auxiliary $a_r$, against $(h_j \cdot a)$, the conjunction of $h_j$ with the best supported auxiliary $a$. Via *Rule RB* we have, $$ \frac{P[(h_i \cdot a_r) \mid c \cdot e \cdot d]}{P[(h_j \cdot a) \mid c \cdot e \cdot d]} = \frac{P[e \mid (h_i \cdot a_r) \cdot c \cdot d]}{P[e \mid (h_j \cdot a) \cdot c \cdot d]} \times \frac{P[(h_i \cdot a_r) \mid c \cdot d]}{P[(h_j \cdot a) \mid c \cdot d]}. $$ This may *apparently* rehabilitate $h_i$ by making the corresponding likelihood ratio, $P[e \mid (h_i \cdot a_r) \cdot c \cdot d] / P[e \mid (h_j \cdot a) \cdot c \cdot d]$, quite large. So, has bringing $a_r$ to bear succeeded in overcoming the challenge to $h_i$, even though $a_r$ is evidentially inferior to $a$ on the body of evidence $(c^* \cdot e^*)$ directly relevant to these auxiliaries?

Perhaps not at all. For, when we test $(h_i \cdot a_r)$ against $(h_j \cdot a)$, it is important to include the *total body of evidence*, including the evidence $(c^* \cdot e^*)$ that bears on $a_r$ versus $a$. Via several applications of *Rule RB* together with three reasonable suppositions about probabilistic independence, we obtain the following two results, where

$$ \epsilon = \frac{P[a_r \mid c^* \cdot e^* \cdot d]}{P[a \mid c^* \cdot e^* \cdot d]} = \frac{P[e^* \mid a_r \cdot c^* \cdot d]}{P[e^* \mid a \cdot c^* \cdot d]} \times \frac{P[a_r \mid c^* \cdot d]}{P[a \mid c^* \cdot d]}$$

for some very small value of $\epsilon$.

**Alternative Auxiliary Formula 1**

$$\begin{align} &\frac{P[(h_i \cdot a_r) \mid (c \cdot e) \cdot (c^* \cdot e^*) \cdot d]}{P[(h_j \cdot a) \mid (c \cdot e) \cdot (c^* \cdot e^*) \cdot d]} \\ &\qquad = \left(\frac{P[e \mid (h_i \cdot a_r) \cdot c \cdot d]}{P[e \mid (h_j \cdot a) \cdot c \cdot d]} \times \frac{P[a_r \mid (c^* \cdot e^*) \cdot d]}{P[a \mid (c^* \cdot e^*) \cdot d]} \right) \times \frac{P[h_i \mid c \cdot (a_r \cdot d)]}{P[h_j \mid c \cdot (a \cdot d)]} \\ &\qquad = \frac{(P[e \mid (h_i \cdot a_r) \cdot c \cdot d] \times \epsilon)}{P[e \mid (h_j \cdot a) \cdot c \cdot d]} \times \frac{P[h_i \mid c \cdot (a_r \cdot d)]}{P[h_j \mid c \cdot (a \cdot d)]}. \end{align}$$

Furthermore,

**Alternative Auxiliary Formula 2**

If $P[e \mid (h_i \cdot a) \cdot c \cdot d] > 0$, then

$$\begin{align} &\frac{P[(h_i \cdot a_r) \mid (c \cdot e) \cdot (c^* \cdot e^*) \cdot d]}{P[(h_j \cdot a) \mid (c \cdot e) \cdot (c^* \cdot e^*) \cdot d]} \\ &\quad = \frac{P[h_i \mid (c \cdot e) \cdot (a \cdot d)]}{P[h_j \mid (c \cdot e) \cdot (a \cdot d)]} \times \left( \frac{P[e \mid (h_i \cdot a_r) \cdot c \cdot d]}{P[e \mid (h_i \cdot a) \cdot c \cdot d]} \times \frac{P[a_r \mid (c^* \cdot e^*) \cdot d]}{P[a \mid (c^* \cdot e^*) \cdot d]} \right)\\ & \qquad\qquad \times \frac{P[h_i \mid c \cdot (a_r \cdot d)]}{P[h_i \mid c \cdot (a \cdot d)]} \\ &\quad = \frac{P[h_i \mid (c \cdot e) \cdot (a \cdot d)]}{P[h_j \mid (c \cdot e) \cdot (a \cdot d)]} \times \left( \frac{P[e \mid (h_i \cdot a_r) \cdot c \cdot d] \times \epsilon}{P[e \mid (h_i \cdot a) \cdot c \cdot d]}\right) \times \frac{P[h_i \mid c \cdot (a_r \cdot d)]}{P[h_i \mid c \cdot (a \cdot d)]}. \end{align}$$

To see what these formulae tell us, let’s begin with **AAF2**, which may be a bit easier to comprehend than **AAF1**. To apply **AAF2**, we consider cases where the $a$ based likelihood for the evidence according to $h_i$ is non-zero, $P[e \mid (h_i \cdot a) \cdot c \cdot d] > 0.$

Let us assume, as seems reasonable, that $P[h_i \mid a_r \cdot c \cdot d]$ is more or less the same size as (or at least not much larger than) $P[h_i \mid a \cdot c \cdot d]$. That is, let’s assume that auxiliary $a_r$ doesn’t provide notably stronger evidence for $h_i$ than does $a$: $P[h_i \mid a_r \cdot c \cdot d] \lessapprox P[h_i \mid a \cdot c \cdot d].$

Now, *suppose* that auxiliary hypothesis $a$ is very much more strongly supported by the body of evidence $(c^* \cdot e^*)$ than alternative hypothesis $a_r$. So strongly that the comparative support value for $P[a_r \mid (c^* \cdot e^*) \cdot d] / P[a \mid (c^* \cdot e^*) \cdot d] = \epsilon$ is small enough to neutralize whatever increase the auxiliary $a_r$ might provide to the likelihood value $P[e \mid (h_i \cdot a_r) \cdot c \cdot d]$ over the $a$ based likelihood value $P[e \mid (h_i \cdot a) \cdot c \cdot d]$. That is, suppose that the evidence $(c^* \cdot e^*)$ is strong enough to make $$\frac{P[a_r \mid (c^* \cdot e^*) \cdot d]}{P[a \mid (c^* \cdot e^*) \cdot d]} = \; \epsilon \; \; \lessapprox \; \; \frac{P[e \mid (h_i \cdot a) \cdot c \cdot d]}{P[e \mid (h_i \cdot a_r) \cdot c \cdot d]}. $$

Then, according to the **Alternative Auxiliary Formula 2** we must have, $$ \frac{P[(h_i \cdot a_r) \mid (c \cdot e) \cdot (c^* \cdot e^*) \cdot d]}{P[(h_j \cdot a) \mid (c \cdot e) \cdot (c^* \cdot e^*) \cdot d]} \; \; \lessapprox \; \; \frac{P[h_i \mid (c \cdot e) \cdot (a \cdot d)]}{P[h_j \mid (c \cdot e) \cdot (a \cdot d)]}. $$

Thus, when $h_i$ is already doing poorly as compared to $h_j$ on evidence $(c \cdot e)$ relative to the best supported (conjunction of) auxiliaries $a$ — i.e. when $P[h_i \mid (c \cdot e) \cdot (a \cdot d)] / P[h_j \mid (c \cdot e) \cdot (a \cdot d)]$ is quite small — allying $h_i$ with an “evidentially more congenial”, but less well-supported, auxiliary $a_r$ will not usually be much help. The alliance of $h_i$ with such an auxiliary $a_r$ can only significantly improve its comparative support when $\epsilon,$ the strength of the evidence against $a_r$, is weak enough to permit $P[e \mid (h_i \cdot a_r) \cdot c \cdot d] \times \epsilon$ to be significantly greater than $P[e \mid (h_i \cdot a) \cdot c \cdot d] > 0$.

When $P[e \mid (h_i \cdot a) \cdot c \cdot d] = 0$, *Rule RB* guarantees that the $a$ based posterior probability of $h_i$ must be 0: $P[h_i \mid (c \cdot e) \cdot (a \cdot d)] = 0.$ In that case, the $a_r$ based likelihood, $P[e \mid (h_i \cdot a_r) \cdot c \cdot d] > 0$, supplies significant help to $h_i$ by providing it a posterior probability greater than 0. However, due to the evidence against $a_r$ as compared to $a$, this posterior probability may still remain significantly smaller than the $a$ based posterior probability of $h_j$. **Alternative Auxiliary Formula 1** shows precisely how these considerations apply.

*Suppose* that auxiliary hypothesis $a$ is very much more strongly supported by the body of evidence $(c^* \cdot e^*)$ than alternative hypothesis $a_r$. So strongly that the comparative support value for $P[a_r \mid (c^* \cdot e^*) \cdot d] / P[a \mid (c^* \cdot e^*) \cdot d] = \epsilon$ is small enough to overwhelm whatever advantage the auxiliary $a_r$ might provide to increase the likelihood value $P[e \mid (h_i \cdot a_r) \cdot c \cdot d]$ over the value $P[e \mid (h_j \cdot a) \cdot c \cdot d]$. That is, suppose that the evidence $(c^* \cdot e^*)$ is strong enough to make

$$\frac{P[a_r \mid (c^* \cdot e^*) \cdot d]}{P[a \mid (c^* \cdot e^*) \cdot d]} = \; \epsilon \; \; \ll \; \; \frac{P[e \mid (h_j \cdot a) \cdot c \cdot d]}{P[e \mid (h_i \cdot a_r) \cdot c \cdot d]}. $$

Then, according to the **AAF1** we must have,

$$ \frac{P[(h_i \cdot a_r) \mid (c \cdot e) \cdot (c^* \cdot e^*) \cdot d]}{P[(h_j \cdot a) \mid (c \cdot e) \cdot (c^* \cdot e^*) \cdot d]} \; \; \ll \; \; \frac{P[h_i \mid c \cdot (a_r \cdot d)]}{P[h_j \mid c \cdot (a \cdot d)]}. $$

Furthermore, if $\epsilon$ is small enough that

$$\frac{P[a_r \mid (c^* \cdot e^*) \cdot d]}{P[a \mid (c^* \cdot e^*) \cdot d]} = \; \epsilon \; \; \ll \; \; \frac{P[e \mid (h_j \cdot a) \cdot c \cdot d]}{P[e \mid (h_i \cdot a_r) \cdot c \cdot d]} \times \frac{P[h_j \mid c \cdot (a \cdot d)]}{P[h_i \mid c \cdot (a_r \cdot d)]}. $$

Then **AFF1** tells us that

$$ \frac{P[(h_i \cdot a_r) \mid (c \cdot e) \cdot (c^* \cdot e^*) \cdot d]}{P[(h_j \cdot a) \mid (c \cdot e) \cdot (c^* \cdot e^*) \cdot d]} \; \ll \; 1. $$

Thus, strong evidence against alternative auxiliary hypothesis $a_r$ as compared to $a$ can result in strong evidence against $(h_i \cdot a_r)$ as compared to $(h_j \cdot a)$.

Here are the only assumptions needed to prove the **Alternative Auxiliary Formulae**. Each of them is a reasonable probabilistic independence assumption, given the nature of the evidential context.

1. The likelihood of $e$ is independent of $(c^* \cdot e^*)$, given what $(h_i \cdot a_r \cdot c \cdot d)$ probabilistically implies about $e$. The same goes for $h_j$ and $a$ in place of $h_i$ and $a_r$, respectively.

$$\begin{align} P[e \mid (h_i \cdot a_r) \cdot c \cdot (c^* \cdot e^*) \cdot d] &= P[e \mid (h_i \cdot a_r) \cdot c \cdot d] \\ P[e \mid (h_j \cdot a) \cdot c \cdot (c^* \cdot e^*) \cdot d] &= P[e \mid (h_j \cdot a) \cdot c \cdot d] \end{align}$$

2. The likelihood of $e^*$ is independent of both $h_i$ and $c$, given what $(a_r \cdot c^* \cdot d)$ probabilistically implies about $e^*$. The same goes for $h_j$ and $a$ in place of $h_i$ and $a_r$, respectively.

$$\begin{align} P[e^* \mid (h_i \cdot a_r) \cdot c \cdot c^* \cdot d] &= P[e^* \mid a_r \cdot c^* \cdot d] \\ P[e^* \mid (h_j \cdot a) \cdot c \cdot c^* \cdot d] &= P[e^* \mid a \cdot c^* \cdot d] \end{align}$$

3. $a_r$ is independent of $c$, given $(c^* \cdot d)$. The same goes for $a$, given $(c^* \cdot d)$.

$$\begin{align} P[a_r \mid c \cdot c^* \cdot d] &= P[a_r \mid c^* \cdot d] \\ P[a \mid c \cdot c^* \cdot d] &= P[a \mid c^* \cdot d] \end{align}$$

4. $h_i$ is independent of $c^*$, given $(a_r \cdot c \cdot d)$. The same goes for $h_j$, given $(a \cdot c \cdot d)$.

$$\begin{align} P[h_i \mid a_r \cdot c \cdot c^* \cdot d] &= P[h_i \mid a_r \cdot c \cdot d] \\ P[h_j \mid a \cdot c \cdot c^* \cdot d] &= P[h_j \mid a \cdot c \cdot d] \end{align}$$ proof of the **Alternative Auxiliaries Formula**:

$$\begin{align} &\frac{P[(h_i \cdot a_r) \mid (c \cdot e) \cdot (c^* \cdot e^*) \cdot d]}{P[(h_j \cdot a) \mid (c \cdot e) \cdot (c^* \cdot e^*) \cdot d]} \\ &\quad = \frac{P[e \mid (h_i \cdot a_r) \cdot c \cdot (c^* \cdot e^*) \cdot d]}{P[e \mid (h_j \cdot a) \cdot c \cdot (c^* \cdot e^*) \cdot d]} \times \frac{P[(h_i \cdot a_r) \mid c \cdot (c^* \cdot e^*) \cdot d]}{P[(h_j \cdot a) \mid c \cdot (c^* \cdot e^*) \cdot d]} \\ &\quad = \frac{P[e \mid (h_i \cdot a_r) \cdot c \cdot (c^* \cdot e^*) \cdot d]}{P[e \mid (h_j \cdot a) \cdot c \cdot (c^* \cdot e^*) \cdot d]} \times \frac{P[e^* \mid (h_i \cdot a_r) \cdot c \cdot c^* \cdot d]}{P[e^* \mid (h_j \cdot a) \cdot c \cdot c^* \cdot d]} \\ &\qquad\quad \times \frac{P[(h_i \cdot a_r) \mid c \cdot c^* \cdot d]}{P[(h_j \cdot a) \mid c \cdot c^* \cdot d]} \\ &\quad = \frac{P[e \mid (h_i \cdot a_r) \cdot c \cdot d]}{P[e \mid (h_j \cdot a) \cdot c \cdot d]} \times \frac{P[e^* \mid a_r \cdot c^* \cdot d]}{P[e^* \mid a \cdot c^* \cdot d]} \times \frac{P[h_i \mid a_r \cdot c \cdot c^* \cdot d]}{P[h_j \mid a \cdot c \cdot c^* \cdot d]} \\ &\qquad\quad \times \frac{P[a_r \mid c \cdot c^* \cdot d]}{P[a \mid c \cdot c^* \cdot d]}\\ &\quad = \frac{P[e \mid (h_i \cdot a_r) \cdot c \cdot d]}{P[e \mid (h_j \cdot a) \cdot c \cdot d]} \times \frac{P[e^* \mid a_r \cdot c^* \cdot d]}{P[e^* \mid a \cdot c^* \cdot d]} \times \frac{P[h_i \mid a_r \cdot c \cdot d]}{P[h_j \mid a \cdot c \cdot d]} \\ &\qquad\quad \times \frac{P[a_r \mid c^* \cdot d]}{P[a \mid c^* \cdot d]}\\ &\quad = \frac{P[e \mid (h_i \cdot a_r) \cdot c \cdot d]}{P[e \mid (h_j \cdot a) \cdot c \cdot d]} \times \frac{P[a_r \mid (c^* \cdot e^*) \cdot d]}{P[a \mid (c^* \cdot e^*) \cdot d]} \times \frac{P[h_i \mid c \cdot (a_r \cdot d)]}{P[h_j \mid c \cdot (a \cdot d)]}\\ \end{align}$$ The derivation up to this point yields **AAF1**. Continuing from there, and assuming hereafter that $P[e \mid (h_i \cdot a) \cdot c \cdot d] > 0$, we derive **AAF2** as follows.

$$\begin{align} &\frac{P[(h_i \cdot a_r) \mid (c \cdot e) \cdot (c^* \cdot e^*) \cdot d]}{P[(h_j \cdot a) \mid (c \cdot e) \cdot (c^* \cdot e^*) \cdot d]} \\ &\quad = \left( \frac{P[e \mid (h_i \cdot a) \cdot c \cdot d]}{P[e \mid (h_j \cdot a) \cdot c \cdot d]} \times \frac{P[e \mid (h_i \cdot a_r) \cdot c \cdot d]}{P[e \mid (h_i \cdot a) \cdot c \cdot d]} \right) \times \frac{P[a_r \mid (c^* \cdot e^*) \cdot d]}{P[a \mid (c^* \cdot e^*) \cdot d]} \\ &\qquad\quad \times \left( \frac{P[h_i \mid c \cdot (a \cdot d)]}{P[h_j \mid c \cdot (a \cdot d)]} \times \frac{P[h_i \mid c \cdot (a_r \cdot d)]}{P[h_i \mid c \cdot (a \cdot d)]} \right) \\ &\quad = \left( \frac{P[e \mid h_i \cdot c \cdot (a \cdot d)]}{P[e \mid h_j \cdot c \cdot (a \cdot d)]} \times \frac{P[h_i \mid c \cdot (a \cdot d)]}{P[h_j \mid c \cdot (a \cdot d)]} \right) \\ &\qquad\quad \times \left( \frac{P[e \mid (h_i \cdot a_r) \cdot c \cdot d]}{P[e \mid (h_i \cdot a) \cdot c \cdot d]} \times \frac{P[a_r \mid (c^* \cdot e^*) \cdot d]}{P[a \mid (c^* \cdot e^*) \cdot d]} \right) \times \frac{P[h_i \mid c \cdot (a_r \cdot d)]}{P[h_i \mid c \cdot (a \cdot d)]}\\ &\quad = \frac{P[h_i \mid (c \cdot e) \cdot (a \cdot d)]}{P[h_j \mid (c \cdot e) \cdot (a \cdot d)]} \times \left( \frac{P[e \mid (h_i \cdot a_r) \cdot c \cdot d]}{P[e \mid (h_i \cdot a) \cdot c \cdot d]} \times \frac{P[a_r \mid (c^* \cdot e^*) \cdot d]}{P[a \mid (c^* \cdot e^*) \cdot d]} \right) \\ &\qquad\quad \times \frac{P[h_i \mid c \cdot (a_r \cdot d)]}{P[h_i \mid c \cdot (a \cdot d)]}. \end{align}$$
