# logic-temporal — burgess-xu（supplement）

> （《logic-temporal》词条补充材料，源：plato.stanford.edu/entries/logic-temporal/burgess-xu.html）

#### Supplement to Temporal Logic

## Supplement: Burgess-Xu Axiomatic System for *Since* and *Until* and Some Extensions

The axiomatic system of Burgess-Xu for the reflexive versions of $S$ and $U$ extends classical propositional logic with the following axiom schemata and their mirror images (where $G$ and $H$ as well as $U$ and $S$ are swapped):

- $G\varphi \rightarrow \varphi$
- $G(\varphi \rightarrow \psi)\rightarrow \varphi U\chi \rightarrow \psi U\chi$
- $G(\varphi \rightarrow \psi)\rightarrow \chi U\varphi \rightarrow \chi U\psi$
- $\varphi \wedge \chi U\psi \rightarrow \chi U(\psi \wedge \chi S\varphi)$
- $\varphi U\psi \rightarrow (\varphi \wedge \varphi U\psi)U\psi$
- $\varphi U(\varphi \wedge \varphi U\psi)\rightarrow \varphi U\psi$
- $\varphi U\psi \wedge \chi U\theta \rightarrow (\varphi \wedge \chi)U(\psi \wedge \theta)\vee (\varphi \wedge \chi)U(\psi \wedge \chi)\vee (\varphi \wedge \chi)U(\varphi \wedge \theta)$

and the inference rules NEC$_G$ and NEC$_H$. The translation of this axiomatization for the strict versions of $S$ and $U$ was extended by Venema (1993) to complete axiomatic systems for:

- all *discrete linear orderings*: by adding $F\top \rightarrow \bot U\top$ and its dual $P\top \rightarrow \bot S\top$;
- all *well-orderings*: by further adding $H\bot \vee PH\bot$ and $F\varphi \rightarrow (\lnot \varphi)U\varphi$;
- $\left\langle \mathbf{N,\lt}\right\rangle$: by further adding $F\top$.
