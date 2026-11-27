# logic-temporal — axiomatic-fotl-constant（supplement）

> （《logic-temporal》词条补充材料，源：plato.stanford.edu/entries/logic-temporal/axiomatic-fotl-constant.html）

#### Supplement to Temporal Logic

## Supplement: Axiomatic System **FOTL(CD)** for the Minimal FOTL with Constant Domain Semantics

The axiomatic system provided here is an adaptation of similar axiomatic systems that can be found in Rescher and Urquhart (1971, Chapter XX) and McArthur (1976, Chapter 4).

I. **Axiom schemes:**

1. All axioms of the minimal propositional temporal logic $\mathbf{K}_{t}$
2. Universal Instantiation ($\forall$-Elimination): $\forall x \varphi(x) \to \varphi(\tau)$, for any term *τ* free for substitution for $x$ in *φ*
3. Reflexivity of equality: $\forall x (x = x)$
4. Extensionality: $\forall x \forall y (x = y \to (\varphi[x/z] \to \varphi[y/z]))$
5. Future necessity of non-equality: $\forall x\forall y(x \neq y \to G (x \neq y))$

II. **Inference rules**  (where $\vdash_{\mathrm{CD}}$ denotes derivability in **FOTL(CD)**):

1. Modus Ponens: If $\vdash_{\mathrm{CD}} \varphi \rightarrow \psi$ and $\vdash_{\mathrm{CD}} \varphi$, then $\vdash_{\mathrm{CD}} \psi$
2. $G$-Necessitation: If $\vdash_{\mathrm{CD}} \varphi$, then $\vdash_{\mathrm{CD}} G \varphi$
3. $H$-Necessitation: If $\vdash_{\mathrm{CD}} \varphi$, then $\vdash_{\mathrm{CD}} H \varphi$
4. Universal Generalization ($\forall$-Introduction): If $\vdash_{\mathrm{CD}} \psi \to \varphi(x)$, then $\vdash_{\mathrm{CD}} \psi \to \forall x \varphi$, where $x$ does not occur free in *ψ*

III. **Some important theorems:**

1. Symmetry of equality: $\vdash_{\mathrm{CD}} \forall x\forall y(x = y \to y = x)$ [Derived from Extensionality, applied to $\varphi := (z=x)$.]
2. Future necessity of equality: $\vdash_{\mathrm{CD}} \forall x\forall y(x = y \to G (x = y))$ [Derived from Extensionality, applied to $\varphi := G (x=z)$.]
3. Past necessity of equality: $\vdash_{\mathrm{CD}} \forall x\forall y(x = y \to H (x = y))$. [Derived likewise.]
4. Past necessity of non-equality: $\forall x\forall y(x \neq y \to H (x \neq y))$. [Derived from the future necessity of equality.]
5. Transitivity of equality: $\vdash_{\mathrm{CD}} \forall x\forall y \forall z(x = y \land y = z \to x = z)$
6. The Converse Future Barcan formula $\mathsf{CBF}_{G}$: $\vdash_{\mathrm{CD}} G \forall x \varphi(x) \to \forall x G \varphi(x)$ Proof: (a)  $\vdash_{\mathrm{CD}} \forall x \varphi(x) \to \varphi(x)$ (Universal Instantiation) (b)  $\vdash_{\mathrm{CD}} G \forall x \varphi(x) \to G \varphi(x)$ (From (a) by NEC$_{G}$, K$_{G}$, MP) (c)  $\vdash_{\mathrm{CD}} G \forall x \varphi(x) \to \forall x G \varphi(x)$ (From (b) by Univ. Generalization)
7. The Converse Past Barcan formula $\mathsf{CBF}_{H}$: $\vdash_{\mathrm{CD}} H \forall x \varphi(x) \to \forall x H \varphi(x)$ [Derived by replacing $G$ by $H$ in the proof above.]
8. $\vdash_{\mathrm{CD}} P \forall x \varphi(x) \to \forall x P \varphi(x)$. Proof: (a)  $\vdash_{\mathrm{CD}} \forall x \varphi(x) \to \varphi(x)$ (Universal Instantiation) (b)  $\vdash_{\mathrm{CD}} H (\forall x \varphi(x) \to \varphi(x))$ (From (a) by NEC$_{H}$) (c)  $\vdash_{\mathrm{CD}} H (\forall x \varphi(x) \to \varphi(x)) \to (P \forall x \varphi(x) \to P \varphi(x))$       (Instance of a TL validity) (d)  $\vdash_{\mathrm{CD}} P \forall x \varphi(x) \to P \varphi(x)$ (From (b) and (c) by MP) (e)  $\vdash_{\mathrm{CD}} P \forall x \varphi(x) \to \forall x P \varphi(x)$ (From (d) by Univ. Generalization)
9. The Future Barcan formula $\mathsf{BF}_{G}$: $\vdash_{\mathrm{CD}} \forall x G \varphi(x) \to G \forall x \varphi(x)$ Proof sketch: (a)  $\vdash_{\mathrm{CD}} P G \varphi(x) \to \varphi(x)$ (Instance of a TL validity) (b)  $\vdash_{\mathrm{CD}} \forall x P G \varphi(x) \to P G \varphi(x)$ (Universal Instantiation) (c)  $\vdash_{\mathrm{CD}} \forall x P G \varphi(x) \to \varphi(x)$ (From (a) and (b) by prop. logic) (d)  $\vdash_{\mathrm{CD}} P \forall x G \varphi(x) \to \forall x P G \varphi(x)$ (Instance of Theorem 8 above) (e)  $\vdash_{\mathrm{CD}} P \forall x G \varphi(x) \to \varphi(x)$ (From (c) and (d) by prop. logic) (f)  $\vdash_{\mathrm{CD}} P \forall x G \varphi(x) \to \forall x \varphi(x)$ (From (e) by Univ. Generalization) (g)  $\vdash_{\mathrm{CD}} G P \forall x G \varphi(x) \to G \forall x \varphi(x)$ (From (f) by NEC$_{G}$, K$_{G}$, MP) (h)  $\vdash_{\mathrm{CD}} \forall x G \varphi(x) \to G P \forall x G \varphi(x)$ (Instance of a TL validity) (i)  $\vdash_{\mathrm{CD}} \forall x G \varphi(x) \to G \forall x \varphi(x)$ (From (g) and (h) by prop. logic)
10. The Past Barcan formula $\mathsf{BF}_{H}$: $\vdash_{\mathrm{CD}} \forall x H \varphi(x) \to H \forall x \varphi(x)$ [Derived by replacing $P$ and $G$ by $F$ and $H$ in the proof above.]
