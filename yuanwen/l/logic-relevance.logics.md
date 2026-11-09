# logic-relevance — logics（supplement）

> （《logic-relevance》词条补充材料，源：plato.stanford.edu/entries/logic-relevance/logics.html）

#### Supplement to Relevance Logic

## The Logic S

Here is a Hilbert-style axiomatisation of the logic $\mathbf{S}$ (for “syllogism”).

Our language contains propositional variables, parentheses and one connective: implication.

|   | *Axiom Scheme* | *Axiom Name* |
| --- | --- | --- |
| 1. | $(B\rightarrow C) \rightarrow((A\rightarrow B) \rightarrow(A\rightarrow C))$ | Prefixing |
| 2. | $(A\rightarrow B) \rightarrow((B\rightarrow C) \rightarrow(A\rightarrow C))$ | Suffixing |

|   | *Rule* | *Name* |
| --- | --- | --- |
| 1. | $A \rightarrow B, B \rightarrow C \vdash A \rightarrow C$ | Transitivity |
| 2. | $A \rightarrow B \vdash(B \rightarrow C) \rightarrow(A \rightarrow C)$ | Rule Suffixing |
| 3. | $B \rightarrow C \vdash(A \rightarrow B) \rightarrow(A \rightarrow C)$ | Rule Prefixing |

The logic **T-W** is $\mathbf{S}$ with the addition of the identity axiom $(A\rightarrow A)$. Martin’s theorem is that no instance of the identity axiom is a theorem of $\mathbf{S}$. It is a corollary of Martin’s theorem that in **T-W** if both $A\rightarrow B$ and $B\rightarrow A$ are provable, then $A$ and $B$ are the same formula (see Anderson, Belnap, and Dunn (1992) §66).
