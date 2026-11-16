# reasoning-defeasible — suppl6（supplement）

> （《reasoning-defeasible》词条补充材料，源：plato.stanford.edu/entries/reasoning-defeasible/suppl6.html）

#### Supplement to Defeasible Reasoning

## David Lewis’s Conditional Logic

This is Donald Nute’s axiom system (Nute 1984, 396-399) for David K. Lewis’s preferred logic for the counterfactual conditional, $VC$ (Lewis 1973, 132):

Rules:

1. Modus ponens.
2. Deduction within the consequent of conditionals: if $\chi_1 \ldots \chi_n$ logically entails *ψ*, then the conditionals $(\phi \Rightarrow \chi_1)\ldots(\phi \Rightarrow \chi_n)$ logically entail $(\phi \Rightarrow \psi)$.
3. Interchange of logical equivalents.

Axioms:

1. All truth-functional tautologies.
2. *ID*: $(\phi \Rightarrow \phi)$
3. *MOD*: $(\neg \phi \Rightarrow \phi) \rightarrow(\psi \Rightarrow \phi)$
4. *CSO*: $[(\phi \Rightarrow \psi) \amp(\psi \Rightarrow \phi)] \rightarrow [(\phi \Rightarrow \chi) \leftrightarrow(\psi \Rightarrow \chi)]$
5. *CV*: $(\phi \Rightarrow \psi) \rightarrow[((\phi \amp \chi) \Rightarrow \psi) \vee (\phi \Rightarrow \neg \chi)]$
6. *MP*: $(\phi \Rightarrow \psi) \rightarrow(\phi \rightarrow \psi)$
7. *CS*: $(\phi \amp \psi) \rightarrow(\phi \Rightarrow \psi)$

The last two axioms, *MP* and *CS*, correspond to weak and strong centering, respectively (in effect, the stipulation that the actual world is one of the most, or uniquely the most, normal of all worlds). For nonmonotonic logic, these conditions, and these two axioms, must be dropped. The fifth axiom, *CV*, is the object-language correlate of Rational Monotony.
