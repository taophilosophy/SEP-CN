# logic-relevance — logic-b-dj-dk（supplement）

> （《logic-relevance》词条补充材料，源：plato.stanford.edu/entries/logic-relevance/logic-b-dj-dk.html）

#### Supplement to Relevance Logic

## The Logics $\mathbf{B}, \mathbf{DJ}$, and $\mathbf{DK}$

Here is a Hilbert-style axiomatisation of the logic $\mathbf{B}$ (for “Base Logic”). The implication, conjunction, and disjunction fragment of $\mathbf{B}$ is the weakest system that can be given a Routley-Meyer semantics.

|   | *Axiom Scheme* | *Axiom Name* |
| --- | --- | --- |
| 1. | $A\rightarrow A$ | Identity |
| 2. | $A\rightarrow(A\vee B)$; $B\rightarrow(A\vee B)$ | Or-Intro. |
| 3. | $((A\rightarrow B) \amp(A\rightarrow C))\rightarrow(A\rightarrow(B \amp C))$ | And-Intro. |
| 4. | $((A\rightarrow C) \amp(B\rightarrow C))\rightarrow((A\vee B)\rightarrow C)$ | Or-Elim. |
| 5. | $(A \amp B)\rightarrow A$; $(A \amp B) \rightarrow B$ | And-Elim. |
| 6. | $(A \amp(B\vee C))\rightarrow((A \amp B)\vee(A \amp C))$ | Distribution |
| 7. | $\neg \neg A\rightarrow A$ | Double Negation-Elim. |

|   | *Rule* | *Name* |
| --- | --- | --- |
| 1. | $A \rightarrow B, A \vdash B$ | Modus Ponens |
| 2. | $A \rightarrow B \vdash(B \rightarrow C) \rightarrow(A \rightarrow C)$ | Rule Suffixing |
| 3. | $B \rightarrow C \vdash(A \rightarrow B) \rightarrow(A \rightarrow C)$ | Rule Prefixing |
| 4. | $A \rightarrow$ *$\neg$B* $\vdash B \rightarrow$ *$\neg$A* | Rule Contraposition |

The logic $\mathbf{DJ}$ is obtained from adding to $\mathbf{B}$ the conjunctive syllogism axiom: $((A\rightarrow B) \amp(B\rightarrow C))\rightarrow(A\rightarrow C)$. The logic $\mathbf{DK}$ is obtained by adding the law of excluded middle $(A\vee \neg A)$ to $\mathbf{DJ}$.

The use of “D” in the names of these logics stands for “dialectical”, and is so used because these logics are particularly useful for dealing with paradoxes and other usual sources of contradictions. Although the original intended connection with 19th Century dialectial theories has been largely disregarded in the contemporary literature, the traditional names have been retained.
