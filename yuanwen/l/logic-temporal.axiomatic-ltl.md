# logic-temporal — axiomatic-ltl（supplement）

> （《logic-temporal》词条补充材料，源：plato.stanford.edu/entries/logic-temporal/axiomatic-ltl.html）

#### Supplement to Temporal Logic

## Supplement: Some Variations of the Axiomatic System for LTL

Note that (GFP$_G$) generalizes the induction axiom (IND) $\varphi \wedge G(\varphi \rightarrow X\varphi)\rightarrow G\varphi$ (which we discuss in Section 4.1). In fact, the axiom (GFP$_G$) can be replaced by the following induction rule, which is deducible in the LTL system provided in the main text:

- If $\vdash \psi \rightarrow \varphi \land X\psi$, then $\vdash \psi \rightarrow G\varphi$.

Likewise, (LFP$_U$) can be replaced by the following derivable rule:

- If $\vdash (\psi \vee (\varphi \wedge X\theta)) \rightarrow \theta$, then $\vdash \varphi U \psi \rightarrow \theta$.

Moreover, if we define $G p$ as $\lnot (\top U \lnot p)$, the axioms (FP$_G$) and (GFP$_G$) become deducible from the rest.
