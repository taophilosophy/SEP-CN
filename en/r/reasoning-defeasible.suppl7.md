# reasoning-defeasible — suppl7（supplement）

> （《reasoning-defeasible》词条补充材料，源：plato.stanford.edu/entries/reasoning-defeasible/suppl7.html）

#### Supplement to Defeasible Reasoning

## Social-Choice-Inspired Postulates (Lindström 2022)

Let C = nonmonotonic consequence (defined over sets of formulas), Cn = classical (monotonic) consequence, S be a selection function (defined over the powerset of worlds), where S(X) are the preferred worlds in set X.

The first group of postulates are:

- **Chernoff** S(X) ∩ Y ⊆ S(X ∩ Y) This semantic condition corresponds to the following syntactic rule: C(Γ ∪ Δ ) ⊆ Cn(C(Γ) ∪ Δ)
- **Path Independence** S(S(X) ∪ S(Y)) = S(X ∪ Y) C(C(Γ) ∩ C(Δ)) = C(Cn(Γ) ∩ Cn(Δ))
- **Gamma** Let F be a nonempty set of sets of worlds. Then ⋂_{(X∈F)}S(X) ⊆ S(⋃_{(X∈F)}X). I.e., if *x* is a best choice in every set *X* in a family of sets, then *x* is also a best choice in their union. ∩_{(Γ∈F)} Cn(Γ) ⊆ Cn(∪_{Γ∈F} C(Γ)) where F is any non-empty family of sets of sentences.

Gamma has a simple finitary consequence: S(X) ∩ S(Y) ⊆ S(X ∪ Y). This corresponds to C((Cn(Γ)) ∩ Cn(Δ)) ⊆ Cn(C(Γ) ∪ C(Δ)).

The next postulate is:

- **Sen** If S(X) ∩ S(Y) ≠ ∅, then S(X ∩ Y) ⊆ S(X) ∩ S(Y) If C(Γ) ∪ C(Δ) is consistent, then C(Γ) ∪ C(Δ) ⊆ C(Γ ∪ Δ)

This is Sen’s property β. It can also be formulated as if X ⊆ Y and S(X) ∩ Y ≠ ∅, then S(X) ∩ Y = S(Y).

The final group of postulates is:

- **Arrow (independence of irrelevant alternatives)** If S(X) ∩ Y ≠ ∅, then S(X ∩ Y) = S(X) ∩ Y If C(Γ) ∪ Δ is consistent, then C(Γ ∪ Δ) = Cn(C(Γ ∪ Δ))
- **Consistency preservation** If X ≠ ∅, then S(X) ≠ ∅ If ⊥ ∉ Cn(Γ), then ⊥ ∉ C(Γ)

Arrow is equivalent to Chernoff plus Sen. Consistency preservation plus Arrow imply Chernoff, Cautious monotonicity and Gamma.
