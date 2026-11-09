# dynamic-epistemic — appendix-C-relations（supplement）

> （《dynamic-epistemic》词条补充材料，源：plato.stanford.edu/entries/dynamic-epistemic/appendix-C-relations.html）

#### Supplement to Dynamic Epistemic Logic

## Appendix C: Properties of binary relations

Below are the definitions of various adjectives that may be used to describe a binary relation *R* on a set *W* (of “worlds”): this is a set $R\subseteq W$ for which we write $wRv$ to mean that $(w,v)\in R$.

- **Reflexive**: $xRx$ for each $x\in W$. “Each world has an *R*-arrow pointing from that world right back to that world.”
- **Transitive**: $xRy$ and $yRz$ implies $xRz$ for each $x,y,z\in W$. “Every sequence of worlds connected by *R*-arrows gives rise to an *R*-arrow going directly from the first world to the last.”
- **Symmetric**: $xRy$ implies $yRx$ for each $x,y\in W$. “Every *R*-arrow going in one direction gives rise to another *R*-arrow going in the opposite direction.”
- **Equivalence relation**: *R* is reflexive, transitive, and symmetric.
- **Euclidean**: $xRy$ and $xRz$ implies $yRz$ for each $x,y,z\in W$. “Two *R*-arrows leaving from the same source world give rise to *R*-arrows going between their destinations in both directions.”
- **Serial**: for every $x\in W$, there is a $y\in W$ such that $xRy$. “Every world has a departing *R*-arrow.”
- **Connected**: for each partition of *W* into two disjoint nonempty sets *S* and *T*, there is an $x\in S$ and a $y\in T$ such that $xRy$ or $yRx$. “All worlds are linked to the same *R*-arrow network.”
- **Complete (or Total)**: for any two different elements $x\in W$ and $y\in W$, we have $xRy$ or $yRx$. “Every pair of distinct worlds is ‘*R*-comparable’.” (Think of $xRy$ as saying, “*x* is less than *y*.”)
- **Well-founded**: every nonempty set $S\subseteq W$ has an $x\in S$ such that for no $y\in S$ is it the case that $yRx$. “Every nonempty set of worlds has an ‘*R*-minimal’ element.”
- **Converse well-founded**: the converse relation $R^-$ (defined by $xR^-y$ iff $yRx$) is well-founded. “Every nonempty set of worlds has an ‘*R*-maximal’ element.”
- **Preorder**: *R* is reflexive and transitive.

For information on the role of some of these properties in modal logic, we refer to the reader to our [Appendix D](dynamic-epistemic.appendix-D-normal-ML.md) or the *Stanford Encyclopedia of Philosophy* entry on Modal Logic.

← beginning of main article
