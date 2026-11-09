# frege-theorem — Gg-Hume（supplement）

> （《frege-theorem》词条补充材料，源：plato.stanford.edu/entries/frege-theorem/Gg-Hume.html）

#### Supplement to Frege’s Theorem and Foundations for Arithmetic

## Reconstruction of the *Grundgesetze* ‘Derivation’ of Hume’s Principle

In **Gg**, Fregean extensions do *not* contain concepts as members but rather objects. So Frege had to find another way to express the explicit definition of $\#F$. His technique was to let extensions go proxy for their corresponding concepts. We may describe Frege’s technique as follows. (What follows is an adaptation and simplification of the strategy Frege outlines in **Gg** I, §34ff.) Instead of defining the number of $F$s as the extension consisting of all those first-order concepts that are equinumerous to $F$, he defined it as the extension consisting of all the extensions of concepts equinumerous to $F$. Here is a formula which says: *$x$ is an extension of a concept that is equinumerous to $F$:*

$\exists H(x\eqclose \epsilon H \amp H\apprxclose F)$

We can name this concept using our $\lambda$-notation as follows:

$[\lambda x \, \exists H(x\eqclose \epsilon H \amp H\apprxclose F)]$

Instead of writing out this lengthy expression *being an* $x$ *which is an extension of a concept equinumerous to* $F$, let us define the concept $F^{\approx}$ as follows:

$F^{\approx} \eqdef [\lambda x \, \exists H(x\eqclose \epsilon H \amp H\apprxclose F)]$

Note that the extension of this concept, $\epsilon F^{\approx}$, contains only extensions as members.

Now Frege’s explicit definition of ‘the number of $F$s’ can be given as follows:

$\#F \eqdef \epsilon F^{\approx}$

This definition identifies the number of $F$s as the extension that contains all and only those extensions of concepts that are equinumerous to $F$.

We can complete our preliminary work for the proof of Hume’s Principle by formulating and proving the following Lemma (derived from Basic Law V), which simplifies the proof of Hume’s Principle:

**Lemma for Hume’s Principle**: $\epsilon G\in\#F \equivwide G\apprxclose F$

([Proof of the Lemma for Hume’s Principle](frege-theorem.subproof1.md))

This Lemma tells us that the extension $G$ is a member of $\#F$ just in case $G$ is equinumerous to $F$. Clearly, since $F$ is equinumerous to itself, it follows that $\#F$ contains $\epsilon F$ as a member. From these facts, one can get a sense of how Frege derived Hume’s Principle from Basic Law V in **Gg**. Here is a reconstruction of the argument.

> [Proof of Hume’s Principle from Basic Law V](frege-theorem.subproof2.md)

Return to Frege’s Theorem and Foundations for Arithmetic
