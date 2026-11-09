# logic-temporal — axiomatic-fotl-varying（supplement）

> （《logic-temporal》词条补充材料，源：plato.stanford.edu/entries/logic-temporal/axiomatic-fotl-varying.html）

#### Supplement to Temporal Logic

## Supplement: Axiomatic System **FOTL(VD)** for the Minimal FOTL with Varying Domain Semantics

The axiomatic system below is an adaptation of similar axiomatic systems that can be found in Rescher and Urquhart (1971, Chapter XX) and McArthur (1976, Chapter 4).

I. **Axiom schemes:**

1. All axioms of the minimal propositional temporal logic $\mathbf{K}_{t}$
2. Restricted Universal Instantiation ($\forall$-Elimination): $\forall y(\forall x \varphi(x) \rightarrow \varphi[y/x])$, for any $y$ free for substitution for $x$ in $\varphi$
3. Vacuous Generalization: $\forall x \varphi \leftrightarrow \varphi$, if $x$ does not occur free in $\varphi$
4. $\forall$-Distributivity: $\forall x (\varphi \rightarrow \psi) \rightarrow (\forall x \varphi \to \forall x \psi)$
5. $\forall$-Permutation: $\forall x \forall y \varphi \rightarrow \forall y \forall x \varphi$
6. Reflexivity of equality: $\forall x (x = x)$
7. Extensionality: $\forall x \forall y (x = y \rightarrow (\varphi[x/z] \rightarrow \varphi[y/z]))$
8. Necessity of non-equality: $\forall x\forall y(x \neq y \rightarrow A (x \neq y))$ (Recall that $A \varphi = H \varphi \land \varphi \land G \varphi$.)

II. **Inference rules**  (where $\vdash_{\mathrm{VD}}$ denotes derivability in **FOTL(VD)**):

1. Modus Ponens: If $\vdash_{\mathrm{VD}} \varphi \rightarrow \psi$ and $\vdash_{\mathrm{VD}} \varphi$, then $\vdash_{\mathrm{VD}} \psi$
2. $G$-Necessitation: If $\vdash_{\mathrm{VD}} \varphi$, then $\vdash_{\mathrm{VD}} G \varphi$
3. $H$-Necessitation: If $\vdash_{\mathrm{VD}} \varphi$, then $\vdash_{\mathrm{VD}} H \varphi$
