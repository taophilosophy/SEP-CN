# frege-theorem — example（supplement）

> （《frege-theorem》词条补充材料，源：plato.stanford.edu/entries/frege-theorem/example.html）

#### Supplement to Frege’s Theorem and Foundations for Arithmetic

## A More Complex Example

If given the premise that

$1+2^{2}=5$

one can prove that

$1\in \epsilon[\lambda z \, z+2^{2} =5]$

For it follows from our premise (by *λ*-Abstraction) that:

$[\lambda z \, z+2^{2}=5]1$

Independently, by the logic of identity, we know:

$\epsilon[\lambda z \, z+2^{2}=5] = \epsilon[\lambda z \, z+2^{2}=5]$

So we may conjoin this fact and the result of *λ*-Abstraction to produce:

$\epsilon[\lambda z \, z+2^{2}=5] \eqclose \epsilon[\lambda z \, z+2^{2}=5] \amp [\lambda z \, z+2^{2}=5]1$

Then, by existential generalization on the concept $[\lambda z \, z+2^{2}=5]$, it follows that:

$\exists G[\epsilon[\lambda z \, z+2^{2}=5] \eqclose \epsilon G \amp G1]$

And, finally, by the definition of membership, we obtain:

$1\in\epsilon[\lambda z \, z+2^{2}=5]$,

which is what we were trying to prove.

Return to Frege's Theorem and Foundations for Arithmetic
