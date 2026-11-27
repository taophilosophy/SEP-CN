# goedel-incompleteness — sup2（supplement）

> （《goedel-incompleteness》词条补充材料，源：plato.stanford.edu/entries/goedel-incompleteness/sup2.html）

#### Supplement to Gödel’s Incompleteness Theorems

## Supplement: The Diagonalization Lemma

The proof of the Diagonalization Lemma centers on *the operation of substitution* (of a numeral for a variable in a formula): If a formula with one free variable, $A(x)$, and a number $\boldsymbol{n}$ are given, the operation of constructing the formula where the numeral for $\boldsymbol{n}$ has been substituted for the (free occurrences of the) variable $x$, that is, $A(\underline{n})$, is purely mechanical. So is the analogous arithmetical operation which produces, given the Gödel number of a formula (with one free variable) $\ulcorner A(x)\urcorner$ and of a number $\boldsymbol{n}$, the Gödel number of the formula in which the numeral $\underline{n}$ has been substituted for the variable in the original formula, that is, $\ulcorner A(\underline{n})\urcorner$. The latter operation can be expressed in the language of arithmetic. Note, in particular, that nothing prevents $\boldsymbol{n}$ from being the Gödel number of $A(x)$ itself, that is, $\ulcorner A(x)\urcorner$ (in the usual coding schemes, though, $\boldsymbol{n}$ cannot be $\ulcorner A(\underline{n})\urcorner)$. This operation of substitution is applied here again and again.

Let us refer to the arithmetized substitution function as $\textit{substn}(\ulcorner A(x)\urcorner , \boldsymbol{n}) = \ulcorner A(\underline{n})\urcorner$, and let $S(x, y, z)$ be a formula which strongly represents this operation, as a relation, in the language of our theory $F$. In other words, $S$ is true of $x, y$, and $z$, if and only if:

$$ x = \ulcorner A(x)\urcorner , y = \boldsymbol{n}, \text{ and } z = \ulcorner A(\underline{n})\urcorner. $$

Again, nothing prevents us from considering $\textit{substn}(\ulcorner A(x)\urcorner , \ulcorner A(x)\urcorner)$, or, analogously, $S(x, x, y)$.

Given any formula $A(x)$, we can now construct another formula $\exists y[A(y) \wedge S(x, x, y)$] with one free variable $x$. Let us abbreviate it as $B(x)$.

This formula has a Gödel number, say, $\boldsymbol{k} = \ulcorner B(x)\urcorner$. By substituting the numeral $\underline{k}$ denoting it for $x$ in $B(x)$, we get $B(\underline{k})$; let us call this sentence $D$. Looking back the chain definitions, we see that:

$$ D := B(\underline{k}) := \exists y[A(y) \wedge S(\underline{k}, \underline{k}, y)]. $$

If $\boldsymbol{m} = \ulcorner B(\underline{k})\urcorner$, then $\textit{substn}(\boldsymbol{k}, \boldsymbol{k}) = \boldsymbol{m}$, and (assuming $F$ contains a sufficient amount of arithmetic; $F$ can then also prove that the result of the arithmetized substitution function is unique)

$$ F \vdash \forall y[S(\underline{k},\underline{k}, y) \leftrightarrow y = \underline{m}] $$

As $\boldsymbol{k}$ was the Gödel number of the formula $B(x)$ and $\boldsymbol{m}$ is the Gödel number of the sentence which results when $\underline{k}$ is substituted for $x$ in $B(x)$, i.e., $\boldsymbol{m} = \ulcorner B(\underline{k})\urcorner$, we can write this as:

$$ F \vdash \forall y[S(\underline{k},\underline{k}, y) \leftrightarrow y = \ulcorner B(\underline{k})\urcorner] $$

By a little logic, we have

$$\begin{align} F &\vdash D \leftrightarrow \exists y[A(y) \wedge y = \ulcorner B(\underline{k})\urcorner], \text{ and from this } \\ F &\vdash D \leftrightarrow A(\ulcorner B(\underline{k})\urcorner), \text{ i.e.,} \\ F &\vdash D \leftrightarrow A(\ulcorner D\urcorner). \end{align}$$

This completes the proof.

For the relations of the Gödelian Diagonalization Lemma to Cantor’s method of diagonalization in set theory, see Gaifman 2006.
