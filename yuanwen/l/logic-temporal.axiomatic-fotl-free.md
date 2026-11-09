# logic-temporal — axiomatic-fotl-free（supplement）

> （《logic-temporal》词条补充材料，源：plato.stanford.edu/entries/logic-temporal/axiomatic-fotl-free.html）

#### Supplement to Temporal Logic

## Supplement: Axioms for the Minimal FOTL with $E$: the Free Logic Version

Here we abandon the classical rules for the quantifiers and adopt the rules of Free Logic instead, which is a logic that allows for terms that do not refer to any existing entity (cf. the entry on [free logic](https://plato.stanford.edu/entries/logic-free)). The application of the rule of Universal Instantiation is restricted by adding the predicate $E$ for ‘existence at the current time instant’ and the rule of Universal Generalization is modified accordingly:

- *Universal Instantiation* ($\forall$-Elimination): $\vdash \forall x \varphi(x) \to (E(y) \to \varphi[y/x])$, where $y$ does not occur free in $\varphi$.
- *Universal Generalization* ($\forall$-Introduction): If $\vdash \psi \to (E(x) \to \varphi(x))$, then $\vdash \psi \to \forall x \varphi(x)$, where $x$ does not occur free in $\psi$.

Thus, formulae like $\exists x G (x=\tau)$, $G \exists x(x=\tau)$, and $\forall y G \exists x G (x=y)$ are no longer derivable.
