# logic-temporal — axiomatic-ctl（supplement）

> （《logic-temporal》词条补充材料，源：plato.stanford.edu/entries/logic-temporal/axiomatic-ctl.html）

#### Supplement to Temporal Logic

## Supplement: An Axiomatic System for CTL

To obtain a complete axiomatization of CTL it suffices to replace the axioms of the linear time temporal logic LTL by their path-quantified versions. For instance, the axioms characterizing the temporal operators $G$ and $U$ as fixed points now become:

- $\exists G \varphi \leftrightarrow (\varphi \wedge \exists X\exists G \varphi)$;
- $\forall G \varphi \leftrightarrow (\varphi \wedge \forall X\forall G \varphi)$;
- $\exists(\varphi U\psi) \leftrightarrow (\psi \vee (\varphi \wedge \exists X\exists(\varphi U\psi)))$;
- $\forall (\varphi U\psi) \leftrightarrow (\psi \vee (\varphi \wedge \forall X\forall (\varphi U\psi)))$.

The inference rules are *modus ponens* and the $\forall G$-necessitation rule: if $\vdash \varphi$, then $\vdash \forall G \varphi$.
