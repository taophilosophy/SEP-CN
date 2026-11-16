# formal-epistemology — supplement（supplement）

> （《formal-epistemology》词条补充材料，源：plato.stanford.edu/entries/formal-epistemology/supplement.html）

#### Supplement to Formal Epistemology

## Technical Supplement

- 1. Elementary Theorems of Probability Theory
- 2. The Raven Paradox
- 3. Foundationalism
- 4. Epistemic Logic
- 5. The Meaning of ‘If …then …’

### 1. Elementary Theorems of Probability Theory

**Theorem. (No Chance for Contradictions).** When $A$ is a contradiction, $p(A) = 0$.

*Proof:* Let $A$ be any contradiction, and let $B$ be some tautology. Then $A \vee B$ is also a tautology, and by axiom (2) of probability theory: $$ p(A \vee B) = 1$$ Since $A$ and $B$ are logically incompatible, axiom (3) also tells us that: $$ p(A \vee B) = p(A) + p(B)$$ Combining these two equations: $$ p(A) + p(B) = 1$$ But axiom (2) also tells us that $p(B)=1$. So: $$ p(A) + 1 = 1$$ So $p(A)=0$. $\qed$

**Theorem (Complementarity for Contradictories).** For any $A$, $p(A) = 1 - p(\neg A)$.

*Proof:* $A \vee \neg A$ is always a tautology, so axiom (2) tells us: $$ p(A \vee \neg A) = 1$$

Since $A$ and $\neg A$ are logically incompatible, axiom (3) tells us: $$ p(A \vee \neg A) = p(A) + p(\neg A)$$

These two equations together yield: $$ p(A) + p(\neg A) = 1$$

Thus $p(A) = 1-p(\neg A)$. $\qed$

**Theorem (Equality for Equivalents).** When $A$ and $B$ are logically equivalent, $p(A) = p(B)$.

*Proof:* Suppose $A$ and $B$ are logically equivalent. Then $\neg A$ and $B$ are incompatible. So axiom (3) tells us: $$ p(\neg A \vee B) = p(\neg A) + p(B)$$

By the previous theorem this becomes: $$ p(\neg A \vee B) = 1 - p(A) + p(B)$$

But $p(\neg A \vee B)=1$, since $\neg A \vee B$ is a tautology. Thus: $$ 1 = 1 - p(A) + p(B)$$

Which, with a little algebra, yields $p(A)=p(B)$. $\qed$

**Theorem (Conditional Certainty for Logical Consequences).** When $A$ logically entails $B$, $p(B\mid A)=1$.

*Proof:* Suppose $A$ logically entails $B$. By the definition of conditional probability: $$ p(B\mid A) = \frac{p(B \wedge A)}{p(A)}$$

So we just need to show that $p(B \wedge A)=p(A)$.

For any $A$ and $B$, $A$ is logically equivalent to $(A \wedge B) \vee (A \wedge \neg B)$. By the previous theorem and axiom (3) then: $$\begin{align} p(A) &= p((A \wedge B) \vee (A \wedge \neg B))\\ &= p(A \wedge B) + p(A \wedge \neg B)\end{align}$$

Because $A$ logically entails $B$, $A \wedge \neg B$ is a contradiction, and thus: $$ p(A \wedge \neg B) = 0$$

Combining the previous two equations yields $p(A) = p(A \wedge B)$. $\qed$

**Theorem (Conjunction Costs Probability).** For any $A$ and $B$, $p(A) > p(A \wedge B)$, unless $p(A \wedge \neg B)=0$, in which case $p(A) = p(A \wedge B)$.

*Proof:* As we saw in the previous proof, for any $A$ and $B$: $$ p(A) = p(A \wedge B) + p(A \wedge \neg B)$$

Thus when $p(A \wedge \neg B)>0$, $p(A)>p(A \wedge B)$. If instead $p(A \wedge \neg B)=0$, then $p(A)=p(A \wedge B)$. $\qed$

**Theorem (The Conjunction Rule).** For any $A$ and $B$ where $p(B) \neq 0$, $p(A \wedge B) = p(A\mid B)p(B)$.

*Proof:* $$\begin{align} p(A \wedge B) &= \frac{p(A \wedge B)p(B)}{p(B)}\\ &= p(A\mid B)p(B). \end{align}$$ $\qed$

**Theorem (The Law of Total Probability).** For any $A$, and any $B$ whose probability is neither 0 nor 1 : $$ p(A) = p(A\mid B)p(B) + p(A\mid \neg B)p(\neg B).$$

*Proof:* As in the proof of Conjunction Costs Probability: $$ p(A) = p(A \wedge B) + p(A \wedge \neg B)$$

Applying the Conjunction Rule to each summand yields:

$$ p(A) = p(A\mid B)p(B) + p(A\mid \neg B)p(\neg B)$$

$\qed$

**Theorem (Bayes’ Theorem).** For any propositions $H$ and $E$ with non-zero probability, $$ p(H\mid E) = p(H)\frac{p(E\mid H)}{p(E)}.$$

*Proof:* By the definition of conditional probability: $$ p(H\mid E) = \frac{p(H \wedge E)}{p(E)}$$

Given the equivalence of $H \wedge E$ and $E \wedge H$: $$ p(H\mid E) = \frac{p(E \wedge H)}{p(E)}$$

Multiplying the right-hand side by 1 in the form of $p(H)/p(H)$: $$ p(H\mid E) = p(H)\frac{p(E \wedge H)}{p(E)p(H)}$$

Applying the definition of conditional probability again, this time for $p(E\mid H)$:

$$ p(H\mid E) = p(H)\frac{p(E\mid H)}{p(E)}$$

$\qed$

### 2. The Raven Paradox

**Theorem (The Raven Theorem).** If (i) $p(\neg R \mid \neg B)$ is very high and (ii) $p(\neg B\mid H)=p(\neg B)$, then $p(H\mid \neg R \wedge \neg B)$ is just slightly larger than $p(H)$.

*Proof:* Recall, Bayes’ theorem tells us that $p(H\mid \neg R \wedge \neg B)$ can be obtained from $p(H)$ by multiplying $p(H)$ by the factor: $$ \frac{p(\neg R \wedge \neg B)\mid H)}{p(\neg R \wedge \neg B)}$$

So we need to show that this factor is only slightly larger than 1.

We begin by applying the Conjunction Rule in the numerator: $$ \frac{p(\neg R \wedge \neg B\mid H)}{p(\neg R \wedge \neg B)} = \frac{p(\neg R \mid \neg B \wedge H)p(\neg B \mid H)}{p(\neg R \wedge \neg B)}$$

Next, notice that $H \wedge \neg B$ logically entails $\neg R$: if all ravens are black, this non-black thing must not be a raven. So, by Conditional Certainty for Logical Consequences, the left term in the numerator is just 1, and hence can be removed: $$ \frac{p(\neg R \wedge \neg B)\mid H)}{p(\neg R \wedge \neg B)} = \frac{p(\neg B \mid H)}{p(\neg R \wedge \neg B)}$$

Then we apply assumption (ii) of the theorem in the numerator: $$ \frac{p(\neg R \wedge \neg B)\mid H)}{p(\neg R \wedge \neg B)} = \frac{p(\neg B)}{p(\neg R \wedge \neg B)}$$

By the definition of conditional probability (applied upside down) then: $$ \frac{p(\neg R \wedge \neg B)\mid H)}{p(\neg R \wedge \neg B)} = \frac{1}{p(\neg R \mid \neg B)}$$

And by assumption (i) of our theorem, the denominator here is very close to 1. So the whole ratio is just slightly larger than 1, as desired. $\qed$

### 3. Foundationalism

In the main text we relied on an assumption of the form $p(B\mid A) \leq p(\neg (A \wedge \neg B))$. Since $\neg (A \wedge \neg B)$ is logically equivalent to $A \supset B$, the following theorem will suffice:

**Theorem (The Horseshoe Upper Bound Theorem).** For any $A$ and $B$ such that $p(A)>0$, $p(B\mid A) \leq p(A \supset B)$.

*Proof:* Begin by noting that $A \supset B$ is logically equivalent to $\neg A \vee (B \wedge A)$, so: $$\begin{align} p(A \supset B) &= p(\neg A \vee (B \wedge A))\\ &= p(\neg A) + p(B \wedge A)\end{align}$$

Then, because $p(B \wedge A) = p(B\mid A)p(A)$: $$ p(A \supset B) = p(\neg A) + p(B\mid A)p(A)$$

Then, because multiplying by $p(B\mid A)$ is multiplying a number that’s 1 or smaller:

$$\begin{align} p(A \supset B) &\geq p(B\mid A)p(\neg A) + p(B\mid A)p(A)\\ &= p(B\mid A)[p(\neg A) + p(A)]\\ &= p(B\mid A) \end{align}$$

$\qed$

### 4. Epistemic Logic

**Theorem ($\bwedge$-distribution).** $K(\phi \wedge \psi) \supset (K \phi \wedge K \psi).$

*Proof:* For clarity, we omit some of the more verbose steps in the derivations of lines 4, 5 and 6.

\begin{array}{rll} 1.& (\phi \wedge \psi) \supset \phi& \mathbf{P}\\ 2.& (\phi \wedge \psi) \supset \psi& \mathbf{P}\\ 3.& K[(\phi \wedge \psi) \supset \phi]& 1, \mathbf{NEC}\\ 4.& K[(\phi \wedge \psi) \supset \psi]& 2, \mathbf{NEC}\\ 5.& K(\phi \wedge \psi) \supset K\phi& 3, \mathbf{K}\\ 6.& K(\phi \wedge \psi) \supset K\psi& 4, \mathbf{K}\\ 7.& K(\phi \wedge \psi) \supset (K\phi \wedge K\psi)& 5,6, \mathbf{P}\\ \end{array}

$\qed$

**Lemma (Unknowns are Unknowable).** $\neg \Diamond K(\phi \wedge \neg K \phi).$

*Proof:* Again, we omit some of the more verbose steps:

\begin{array}{rll} 1.& K(\phi \wedge \neg K\phi) \supset (K\phi \wedge K\neg K\phi)& \bwedge\textbf{-distribution}\\ 2.& K\neg K\phi \supset \neg K \phi& \mathbf{T}\\ 3.& K(\phi \wedge \neg K\phi) \supset (K\phi \wedge \neg K\phi)& 1, 2, \mathbf{P}, \mathbf{MP}\\ 4.& \neg (K\phi \wedge \neg K\phi)& \mathbf{P}\\ 5.& \neg K(\phi \wedge \neg K\phi)& 3, 4, \mathbf{P}, \mathbf{MP}\\ 6.& \Box \neg K(\phi \wedge \neg K\phi)& 5, \mathbf{NEC}\\ 7.& \neg \neg \Box \neg K(\phi \wedge \neg K\phi)& 6, \mathbf{P}\\ 8.& \neg \Diamond K(\phi \wedge \neg K\phi)& 7, \textrm{Defn. of }\Diamond\\ \end{array}

$\qed$

### 5. The Meaning of ‘If …then …’

**Theorem (Lewis’ Triviality Theorem).** If Stalnaker’s Hypothesis is true, then $p(B\mid A)=p(B)$ for all propositions $A$ and $B$ such that $p(A) \neq 0$ and $1 \gt p(B) \gt 0$.

*Proof:* We start by applying the Law of Total Probability to the conditional $A \rightarrow B$: $$ p(A \rightarrow B) = p(A \rightarrow B\mid B)p(B) + p(A \rightarrow B\mid \neg B)p(\neg B)$$

Next let’s introduce $p_B$ as a name for the probability function we get from $p$ by conditionalizing on $B$, i.e., $p_B(A)=p(A\mid B)$ for every proposition $A$. Likewise, $p_{\neg B}$ is obtained by conditionalizing $p$ on $\neg B$. Then: $$ p(A \rightarrow B) = p_B(A \rightarrow B)p(B) + p_{\neg B}(A \rightarrow B)p(\neg B)$$

Now, assuming Stalnaker’s Hypothesis: $$ p(A \rightarrow B) = p_B(B\mid A)p(B) + p_{\neg B}(B\mid A)p(\neg B)$$

But $p_B$ automatically assigns probability 1 to $B$, while $p_{\neg B}$ assigns 0. So:

$$\begin{align} p(A \rightarrow B) &= 1 \times p(B) + 0 \times p(\neg B)\\ &= p(B) \end{align}$$

And since $p(A \rightarrow B)=p(B\mid A)$ by Stalnaker’s Hypothesis, $p(B\mid A)=p(B)$ too. $\qed$

**Theorem (Gärdenfors’ Triviality Theorem).** As long as there are two propositions $A$ and $B$ such that $K$ is agnostic about $A$, $A \supset B$, and $A \supset \neg B$, the Ramsey Test cannot hold.

*Proof:* The gist of the argument is that adding $\neg A$ to $K$ would, via the Ramsey Test, bring contradictory conditionals with it: $A \rightarrow B$ and $\neg (A \rightarrow B)$. But this would mean that $K$ wasn’t really agnostic about $A$; its contents would already contradict $\neg A$, so $K$ would have to already contain $A$, contra the stipulation that $K$ is agnostic about $A$.

Why would adding $\neg A$ to $K$ also add these contradictory conditionals, given the Ramsey Test? Let’s proceed in three steps:

First, notice that adding $A \supset B$ to $K$ would bring $A \rightarrow B$ with it via the Ramsey test, since further adding $A$ would also add $B$ via *modus ponens*. By parallel reasoning, adding $A \supset \neg B$ to $K$ would bring $\neg (A \rightarrow B)$ with it via the Ramsey Test.

Second, notice that $\neg A$ logically entails $A \supset B$ (but not *vice versa*). Similarly, $\neg A$ entails $A \supset \neg B$ (but not *vice versa*). $\neg A$ is logically stronger than both these $\supset$-statements.

Third and finally, because $\neg A$ is logically stronger, adding $\neg A$ to $K$ brings with it everything that adding either $\supset$-statement would. The logically stronger the added information, the more logically follows from it. But as we saw, adding $A \supset B$ to $K$ adds $A \rightarrow B$, and adding $A \supset \neg B$ adds $\neg (A \rightarrow B)$. So adding the stronger statement $\neg A$ adds both these contradictory sentences to $K$. $\qed$
