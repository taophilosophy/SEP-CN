# logic-temporal — pbtl（supplement）

> （《logic-temporal》词条补充材料，源：plato.stanford.edu/entries/logic-temporal/pbtl.html）

#### Supplement to Temporal Logic

## Supplement: Burgess’ Axiomatic System for PBTL

Burgess’ (1980) axiomatic system for PBTL extends classical propositional logic by

- the familiar axiom schemata $(K_H)$ and $(K_G)$ (see Section 3.5), as well as $G(\varphi \rightarrow \psi)\rightarrow (F\varphi \rightarrow F\psi),$
- the axiom schemata (GP) and the Peircean variant of (HF) (cf. Section 3.5): $\varphi \rightarrow H\neg G\neg\varphi,$
- the axiom schemata (NOBEG) and Peircean versions of (NOEND) (cf. Section 3.6): $G\varphi \rightarrow F\varphi$ and $G\varphi \rightarrow \neg F\neg\varphi,$
- the axiom scheme (TRANS) for *H*, *G*, and *F* (cf. Section 3.6),
- the axiom schemata $H\varphi \rightarrow (\varphi \rightarrow (G\varphi \rightarrow GHp))$ and $H\varphi \rightarrow (\varphi \rightarrow (\neg F\neg\varphi \rightarrow \neg F\neg Hp)),$ and
- the axiom scheme $FG\varphi \rightarrow GF\varphi.$

The inference rules comprise, in addition to (MP), (NEC$_H$), and (NEC$_G$) (see Section 3.5),

- a version of the so-called Gabbay Irreflexivity Rule: If $\vdash H\neg\varphi \rightarrow (\neg\varphi \rightarrow (G\varphi \rightarrow \psi)),$ then $\vdash \psi,$ provided $\varphi$ does not occur in $\psi$.
