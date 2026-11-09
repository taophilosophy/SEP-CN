# frege-theorem — Gl-Hume（supplement）

> （《frege-theorem》词条补充材料，源：plato.stanford.edu/entries/frege-theorem/Gl-Hume.html）

#### Supplement to Frege’s Theorem and Foundations for Arithmetic

## Reconstruction of the *Grundlagen* Derivation of Hume’s Principle

The derivation of Hume’s Principle in **Gl**, §73, appeals to the following principle, which is a higher-order version of the Law of Extensions:

*Principle*: $G$ is a member of the extension of the second-order concept *equinumerous to F* iff $G$ is equinumerous to $F$

Now Hume’s Principle is that the number of $F$s is identical to the number of $G$s iff $F$ and $G$ are equinumerous. We prove the biconditional in stages.

($\rightarrow$) Assume that the number of $P$s is identical to the number of $Q$s. Then, by the definitions of ‘the number of $P$s’ and ‘the number of $Q$s’, we know that the extension of the concept *equinumerous to P* is identical with the extension of the concept *equinumerous to* Q. But it is a fact about equinumerosity that $P$ is equinumerous to $P$. So by the above Principle, the extension of the concept *equinumerous to P* has $P$ as a member. So, by substitution of identicals, the extension of the concept *equinumerous to Q* has P as a member. So $P$ is equinumerous to $Q$, by the above Principle.

($\leftarrow$) Assume $P$ is equinumerous with $Q$. We want to show that the number of $P$s is identical to the number of $Q$s. So, by definition, we have to show that the extension of the concept *equinumerous to P* is identical to the extension of the concept *equinumerous to Q*. By the Principle of Extensionality, then, we have to show that these two extensions have the same members! So we pick an arbitrary concept $S$ and show that $S$ is a member of the extension of the concept *equinumerous to P* iff $S$ is a member of the extension of the concept *equinumerous to Q*.

($\rightarrow$) Assume $S$ is a member of the extension of the concept *equinumerous to P* (to show: $S$ is a member of the extension of the concept *equinumerous to Q*). Then, by the above Principle, $S$ is equinumerous to $P$. So by the transitivity of equinumerosity (this is Fact 4 in the subsection on Equinumerosity in the main portion of the entry), $S$ is equinumerous to $Q$. So, by the above Principle, $S$ is in the extension of the concept *equinumerous to Q*

($\leftarrow$) Assume S is a member of the extension of the concept *equinumerous to Q* (to show: $S$ is a member of the extension of the concept *equinumerous to P*). Then $S$ is equinumerous to $Q$, by the above Principle. By the symmetry of equinumerosity (Fact 3 in the subsection on Equinumerosity), it follows that $Q$ is equinumerous to $S$. So, given our hypothesis that $P$ is equinumerous to $Q$, it follows by the transitivity of equinumerosity, that $P$ is equinumerous to $S$. So, again by symmetry, we have: $S$ is equinumerous to $P$. And, by the above Principle, it follows $S$ is in the extension of the concept *equinumerous to P*.

Return to Frege’s Theorem and Foundations for Arithmetic
