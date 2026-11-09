# logic-temporal — obtl（supplement）

> （《logic-temporal》词条补充材料，源：plato.stanford.edu/entries/logic-temporal/obtl.html）

#### Supplement to Temporal Logic

## Supplement: Reynolds’ Axiomatic System for OBTL

Reynolds (2003) proposed complete axiomatic systems for OBTL, both for bundled tree validity and Ockhamist validity, assuming instant-based atomic propositions.

His system for bundled tree validity extends the minimal temporal logic $\mathbf{K}_{t}$ (see Section 3.5) by the axiom schemata (TRANS), (LIN-F), and (LIN-P) (see Section 3.6) as well as

- the $\mathbf{S5}$ axiom schemata for $\Box$ (i.e. $\Box(\varphi \rightarrow \psi) \rightarrow (\Box\varphi \rightarrow \Box\psi), \Box\varphi \rightarrow \varphi, \Diamond\varphi \rightarrow \Box\Diamond\varphi$),
- the axiom scheme $G \bot \to \Box G \bot$ for maximality of histories,
- the interaction axiom scheme $P \varphi \rightarrow \Box P \Diamond \varphi$, and
- the axiom scheme $p \rightarrow \Box p$ for instant-based atomic propositions.

The inference rules comprise, in addition to (MP), (NEC$_H$), and (NEC$_G$) (see Section 3.5),

- the necessitation rule for $\Box$, and
- the so-called Gabbay Irreflexivity Rule: If $\vdash (p\land H \lnot p) \to \varphi,$ then $\vdash \varphi,$ provided $p$ does not occur in $\varphi$.

To completely axiomatize Ockhamist validity, Reynolds proposed to add the following infinite axiom scheme, which is supposed to guarantee the “limit closure property”:

- $\Box G_{\leq} \bigwedge_{i=0}^{n-1} (\Diamond \varphi_{i} \to \Diamond F \Diamond \varphi_{i+1}) \to \Diamond G_{\leq} \bigwedge_{i=0}^{n-1} (\Diamond \varphi_{i} \to F \Diamond \varphi_{i+1})$

where $\varphi_{0},\ldots, \varphi_{n-1}$ are any OBTL formulae, $\varphi_{n} = \varphi_{0}$, and $G_{\leq} \theta := \theta \land G\theta$.
