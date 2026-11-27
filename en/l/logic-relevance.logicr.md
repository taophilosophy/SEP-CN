# logic-relevance — logicr（supplement）

> （《logic-relevance》词条补充材料，源：plato.stanford.edu/entries/logic-relevance/logicr.html）

#### Supplement to Relevance Logic

## The Logic R

Here is a Hilbert-style axiomatisation of the logic $\mathbf{R}$.

Our language contains propositional variables, parentheses, negation, conjunction, and implication. In addition, we use the following defined connectives:

$$\begin{align} A\vee B &=_{df} \neg(\neg A \amp \neg B) \\ A \leftrightarrow B &=_{df} (A \rightarrow B) \amp(B \rightarrow A) \end{align}$$

|   | *Axiom Scheme* | *Axiom Name* |
| --- | --- | --- |
| 1. | $A \rightarrow A$ | Identity |
| 2. | $(A \rightarrow B) \rightarrow((B \rightarrow C) \rightarrow(A \rightarrow C))$ | Suffixing |
| 3. | $A \rightarrow((A \rightarrow B) \rightarrow B)$ | Assertion |
| 4. | $(A \rightarrow(A \rightarrow B)) \rightarrow(A \rightarrow B)$ | Contraction |
| 5. | $(A \amp B) \rightarrow A,(A \amp B) \rightarrow B$ | & -Elimination |
| 6. | $A \rightarrow(A\vee B), B \rightarrow(A\vee B)$ | $\vee$-Introduction |
| 7. | $((A \rightarrow B) \amp(A \rightarrow C)) \rightarrow(A \rightarrow(B \amp C))$ | & -Introduction |
| 8. | $((A\vee B) \rightarrow C)\leftrightarrow((A \rightarrow C) \amp(B \rightarrow C))$ | $\vee$-Elimination |
| 9. | $(A \amp(B\vee C)) \rightarrow((A \amp B)\vee(A \amp C))$ | Distribution |
| 10. | $(A \rightarrow \neg B) \rightarrow(B \rightarrow \neg A)$ | Contraposition |
| 11. | $\neg \neg A \rightarrow A$ | Double Negation |

|   | *Rule* | *Name* |
| --- | --- | --- |
| 1. | $A \rightarrow B, A\vdash B$ | Modus Ponens |
| 2. | $A, B\vdash A \amp B$ | Adjunction |
