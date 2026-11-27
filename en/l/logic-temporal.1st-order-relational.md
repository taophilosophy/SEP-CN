# logic-temporal — 1st-order-relational（supplement）

> （《logic-temporal》词条补充材料，源：plato.stanford.edu/entries/logic-temporal/1st-order-relational.html）

#### Supplement to Temporal Logic

## Supplement: First-order Relational Structures and Languages

A *first-order relational structure* consists of:

- a non-empty set of objects $D$, called the *domain (of discourse)*;
- designated *objects* or *individuals* in $D$ denoted by *constants*;
- designated *relations* in $D$ denoted by *predicates*;

We focus on purely relational structures here. That is, we do not consider structures with designated functions.

Here are some examples of first-order relational structures:

- the numerical structure $\mathcal{N}$ on the set of natural numbers $\mathbf{N}$ with the relations $=$ and $<$, and the designated object $0$.
- the structure $\mathcal{H}$ on the set of all humans with the unary relations (i.e. properties) *man* and *woman*, binary relations *parent of*, *child of*, and *loves*, and designated individuals *Adam*, *Eve*, *Joe*, *Mia*, etc.

The vocabulary of a relational first-order language $\mathcal{L}$ comprises:

- *Non-logical symbols*:
- *constants*: $a, b, c, \dots$
- *predicates* (of specified arities): $Q, R, \dots$
- *Individual variables*: $x, y, z, \dots$
- *Logical symbols*:
- *truth-functional connectives*: $\lnot, \land, \lor, \rightarrow, \leftrightarrow$
- *logical constants*: $\top$, $\bot$
- *equality*: $=$
- *quantifiers*: $\forall$, $\exists$
- *auxiliary symbols*: $( \ , \ )$

*Terms* in $\mathcal{L}$ are constant symbols and individual variables. *Atomic formulae* in $\mathcal{L}$ are of the form $R(\tau_{1},...,\tau_{n})$, where $\tau_{1},...,\tau_{n}$ are terms in $\mathcal{L}$ and $R$ is an $n$-ary predicate symbol in $\mathcal{L}$. In particular, $\tau_{1} = \tau_{2}$ is an atomic formula. The set of *formulae* of $\mathcal{L}$ can be recursively defined as follows: $$\varphi \ := \ R(\tau_1,\dots,\tau_n) \ | \ \tau_1 = \tau_2 \ | \ \neg \varphi \ | \ (\varphi \land \varphi) \ | \ \forall x \varphi, $$ where $R(\tau_1,\dots,\tau_n)$ and $\tau_1 = \tau_2$ are atomic formulae. The truth-functional connectives $\vee, \rightarrow$, and $\leftrightarrow$ as well as the logical constants $\top$ and $\bot$ are definable in terms of $\neg$ and $\wedge$ as usual. In addition, $\exists x\varphi := \neg \forall x \neg \varphi$. We distinguish between *free* and *bound* occurrences of variables in formulae (depending on whether the variable occurs in the scope of a quantifier or not). Closed formulae, i.e. formulae not containing any free occurrences of variables, are called *sentences*. For more background on (modal) first-order logic, see e.g. Fitting and Mendelsohn (2023).
