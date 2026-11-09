# dynamic-epistemic — appendix-D-normal-ML（supplement）

> （《dynamic-epistemic》词条补充材料，源：plato.stanford.edu/entries/dynamic-epistemic/appendix-D-normal-ML.html）

#### Supplement to Dynamic Epistemic Logic

## Appendix D: Normal modal logic

Given a finite nonempty set $\sA$ of “agents,’ a *normal multi-modal logic with modals $[a]$ for each $a\in\sA$* is a theory that contains each of the following axiom schemes and rules:

- CL. Axiom schemes for classical propositional logic
- K. $[a](F\to G)\to([a]F\to[a]G)$ for each $a\in\sA$
- *Modus Ponens*: from $F\to G$ and *F*, infer *G*
- Modal Necessitation Rule: from *F*, infer $[a]F$ for any $a\in\sA$

and may also include one or more of the following optional axiom schemes for one or more $a\in\sA$:

- T. $[a]F\to F$
- D. $\lnot[a]\bot$
- 4. $[a]F\to[a][a]F$
- 5. $\lnot[a]F\to[a]\lnot[a]F$

The basic normal multi-modal logic $\mathsf{K}$ is the minimal normal modal logic; in particular, it contains none of the optional rules. Each of the optional schemes corresponds to a specific property of the corresponding binary relation of a Kripke model; see Blackburn et al. (2002) for technical definitions and details. Scheme T corresponds to reflexivity of $R_a$, Scheme D corresponds to seriality of $R_a$, Scheme 4 corresponds to transitivity of $R_a$, and Scheme 5 corresponds to Euclideanness of $R_a$. The traditional “logic of knowledge” is $\mathsf{S5}$ (i.e., $\mathsf{K}$ plus optional schemes T, 4, and 5), while the traditional “logic of belief” is $\mathsf{KD45}$ (i.e., $\mathsf{K}$ plus optional schemes D, 4, and 5). Other common normal modal logics include $\mathsf{S4}$ (i.e., $\mathsf{K}$ plus optional schemes T and 4) and $\mathsf{T}$ (i.e., $\mathsf{K}$ plus optional scheme T). See [Appendix C](dynamic-epistemic.appendix-C-relations.md) for definitions of the aforementioned relational properties.

For more on normal modal logics, we refer the reader to Blackburn et al. (2002) or the *Stanford of Encyclopedia Entry* entry on Modern Origins of Modal Logic.

← beginning of main article
