# common-knowledge — proof2-11（supplement）

> （《common-knowledge》词条补充材料，源：plato.stanford.edu/entries/common-knowledge/proof2-11.html）

#### Supplement to Common Knowledge

## Proof of Proposition 2.11

**Proposition 2.11**. If $A$ holds, and if $A$ is a common reflexive indicator in the population $P$ that $x$, then there is common reason to believe in $P$ that $x$.

**Proof**. (Cubitt and Sugden 2003)

| 1. | $\mathbf{R}_i A$ | (from RCI and the assumption that $A$ holds) |
| --- | --- | --- |
| 2. | $A \indi \mathbf{R}_j A$ | (RCI2) |
| 3. | $A \indi x$ | (RCI3) |
| 4. | $\mathbf{R}_i x$ | (from 1 and 3, using CS1) |
| 5. | $\mathbf{R}_i (A \indj x)$ | (from 3, using RCI4) |
| 6. | $A \indi \mathbf{R}_j x$ | (from 2 and 5, using CS5) |
| 7. | $\mathbf{R}_i \mathbf{R}_j x$ | (from 1 and 6, using CS1) |
| 8. | $\mathbf{R}_i(A \indj \mathbf{R}_k x)$ | (from 6, using RCI4) |
| 9. | $A \indi \mathbf{R}_j (\mathbf{R}_k x)$ | (from 2 and 8, using CS5) |
| 10. | $\mathbf{R}_i (\mathbf{R}_j (\mathbf{R}_k x))$ | (from 1 and 9, using A1) |
| 11. | $\mathbf{R}_i (A \indj \mathbf{R}_k (\mathbf{R}_l x))$ | (from 9, using RCI4) |

And so on, for all $i, j, k, l$ etc. in $P$. Lines $4, 7, 10, 3n+1 (n \gt 3)$ establish the theorem.

Return to Common Knowledge
