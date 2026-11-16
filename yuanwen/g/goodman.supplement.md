# goodman — supplement（supplement）

> （《goodman》词条补充材料，源：plato.stanford.edu/entries/goodman/supplement.html）

#### Supplement to Nelson Goodman

## The Calculus of Individuals in its different versions

The Calculus of Individuals that Leonard and Goodman present in their 1940 article axiomatizes a theory of parthood based on the single primitive for the *discreteness* of two individuals. Parthood is defined using the notion of discreteness so that two individuals are discrete if and only if they share no part in common. In fact, this follows straightforwardly from Leonard and Goodman's first definition:

**I.01**

$x \lt y =_{df} \forall z\ (z \int y \supset z \int x)$

“<” is the sign for (not necessarily proper) part, and we use “$\int$ ” as the sign for discreteness, as is now common. (Leonard and Goodman use a different symbol, looking somewhat like “$\urcorner\kern-1.53pt\llcorner$”.) Definition I.01 thus stipulates that

> $x$ is a part of $y$ iff anything that is discrete from $y$ is also discrete from $x$

The next definition characterizes proper parts:

**I.011**

$x \ll y =_{df} x \lt y \land x \ne y$ $x$ is a proper part of *y* iff $x$ is a part of *y* and $x$ is not identical to *y*

Leonard and Goodman note that identity, “=”, (and dually non-identity, “≠”) could be defined in terms of parthood as “$x \lt y \land y \lt x$”, but they find it undesirable to define identity in this way; rather, they prove this equivalence as a theorem (Leonard and Goodman 1940: 47 fn. 6). Next is the definition of overlap:

**I.02**

$x \overlaps y =_{df} \exists z\ (z \lt x \land z \lt y)$ $x$ overlaps $y$ iff there is something that is both part of $x$ and part of $y$

The following are definitions of the mereological fusion (the “sum-individual”) and nucleus (the “product-individual”). Note that both definitions employ set-theoretic terminology.

**I.03**

$x \fusion \alpha =_{df} \forall z\ (z \int x \equiv \forall y\ (y \in \alpha \supset z \int y))$ $x$ is the fusion of set *α* iff: anything that is discrete from $x$ is discrete from any member of set *α*, and *vice versa*

**I.04**

$x \mathbin{\mbox{Nu}} \alpha =_{df} \forall z\ (z \lt x \equiv \forall y\ (y \in \alpha \supset z \lt y))$ $x$ is the nucleus of set *α* iff: anything that is a part of $x$ is a part from any member of set *α*, and *vice versa*

Fusion and nucleus correspond, in a way, to the set-theoretic notions of union and intersection, but note that fusions and nuclei of sets are not sets themselves but individuals. The remaining four definitions of the universe, binary mereological sum, binary mereological product, and the complement individual (Leonard and Goodman label the latter by the unhappy term “negation”), make use of fusion and nucleus, and further set-theoretic notions:

**I.05**

$ U =_{df} \mathbin{\mbox{Fu}^\prime} V $ the universe is the fusion of the set of all individuals

**I.06**

$ x + y =_{df} \mathbin{\mbox{Fu}^\prime} (\{x\}\cup \{y\}) $ the mereological sum of $x$ and $y$ is the fusion of the set containing only $x$ and $y$

**I.07**

$ xy =_{df} \mathbin{\mbox{Nu}^\prime} (\{x\}\cup \{y\}) $ the mereological product of $x$ and $y$ is the nucleus of the set containing only $x$ and $y$

**I.08**

$ -x =_{df} \mathbin{\mbox{Fu}^\prime} \hat{y}(y \int x) $ the complement individual of $x$ is the fusion of the set of all $y$ that are discrete from $x$

Note that “$V$” denotes the class of all individuals; “$\cup$” denotes the binary function of set-theoretic union; “{” and “}” are set brackets, so “{$x$}” denotes the singleton set of $x$. “($\iota x$)” is Russell's well-known definite descriptions operator (“the unique $x$ that is …”), and “$\hat{y}$” is the class abstraction operator (see also the entry on the notation in *Principia Mathematica*). “$R^\prime y$” denotes the nowadays perhaps less familiar “descriptive function” of a relation $R$ for an argument $y$, as defined in Whitehead and Russell's *Principia Mathematica* (Whitehead and Russell 1910–13):

*30.01

$R^\prime y =_{df} (\iota x)Rxy$

So, for example, if we read “$x \fusion \alpha$” as “$x$ is the fusion of *α*”, we can understand “$\mathbin{\mbox{Fu}^\prime} \alpha$” as “the fusion of *α*”, i.e., the individual that is the fusion of all members of set *α*.

With these definitions in hand, Leonard and Goodman postulate three axioms:

**I.1**

$ \exists x\ x \in \alpha \supset \exists y\ y \fusion \alpha$ if set *α* is not empty, then *α* has a fusion (i.e., unrestricted fusion)

**I.12**

$x \lt y \land y \lt x \supset x = y$ if $x$ is a part of $y$ and $y$ is a part of $x$ then $x$ and $y$ are identical (i.e., parthood is anti-symmetric)

**I.13**

$x \overlaps y \equiv \neg (x \int y)$ $x$ overlaps $y$ iff $x$ is not discrete from $y$

Leonard and Goodman do not give a full exploration of the system, but they state some informative theorems, including the transitivity and reflexivity of parthood, the transitivity and irreflexivity of proper-parthood, commutativity and reflexivity of overlap, the existence of the binary mereological sum, and its commutativity and associativity. They also observe that “[a]nalogues to DeMorgan's formula appear under interesting conditions” (Leonard and Goodman 1940: 50):

**I.85**

$(x \overlaps y \land x \ne U \land y \ne U) \supset xy = -(-x + -y)$ If $x$ and $y$ overlap, and neither is identical to the universe, then the product of $x$ and $y$ is the complement individual of the sum of the complement of $x$ and the complement of $y$ (i.e., under the given conditions, the DeMorgan equivalence holds for mereological product and sum)

The system can be shown to be equivalent to Tarski's (1929) axiomatization of Leśniewski mereology (see Ridder 2002 for the equivalence proof). Systems of this strength are now known as *classical mereology*. The distinctive features of classical mereology are *unrestricted fusion* (there is an individual that is the fusion of any collection of individuals, no matter how heterogeneous and dispersed they are—as discussed in the main text), and that various *supplementation* principles hold (see Simons 1987; see also the discussion of supplementation in the entry on mereology). Classical mereology can easily be seen to be equivalent to a complete Boolean algebra with the zero-element removed (Tarski 1935; Simons 1987: 25; Ridder 2002: ch. 3; Cotnoir and Varzi 2019; see the discussion of unrestricted composition in the entry on mereology).

The version of the Calculus of Individuals that Goodman uses in *A Study of Qualities* (SQ) is essentially the same as the one presented above: it is a minor variant of the system presented by Leonard and Goodman and equivalent to it. Like the former version, it is based on discreteness as a primitive notion and formulated using class terms. Both of these features change in the version of the calculus that Goodman presents in *The Structure of Appearance* (SA), ten years later in 1951*.* Goodman now rejects the use of class terms (see the main text, §3) and formulates a nominalistically acceptable version of the calculus. The primitive Goodman now chooses is overlap, “$\overlaps$”, instead of its discreteness. As I.13 above suggests, the relations are straightforwardly interdefinable. Indeed, Goodman defines “discrete” in SA (§II.4) in analogy to the above mentioned axiom of the previous version of the calculus:

**D2.041**

$x \int y =_{df} \neg (x \overlaps y)$ $x$ is discrete from $y$ iff $x$ does not overlap $y$

“Part” is also defined based on overlap rather than discreteness.

**D2.042**

$x \lt y =_{df} \forall z\ (z \overlaps x \supset z \overlaps y)$ $x$ is a part of $y$ iff anything that overlaps with $x$ also overlaps with $y$

The *definiens* of “proper part” does not appeal to identity:

**D2.043**

$x \ll y =_{df} x \lt y \land \neg (y \lt x)$ $x$ is a proper part of $y$ iff $x$ is a part of $y$ but $y$ is not a part of $x$

In fact, Goodman now defines identity in terms of overlap:

**D2.044**

$ x = y =_{df} \forall z\ (z \overlaps x \equiv z \overlaps y)$ $x$ is identical to $y$ iff: anything that overlaps $x$ also overlaps $y$, and *vice versa*

Further, Goodman defines the binary mereological notions of product and sum, and what we called the “complement individual” above (Goodman here chooses the phrase “negate of an individual” for it):

**D2.045**

$xy =_{df} (\iota z)\forall w\ (w \lt z \equiv (w \lt x \land w \lt y))$ the mereological product of $x$ and $y$ is the individual whose parts are all and only those individuals that are part of both $x$ and $y$

**D2.046**

$-x =_{df} (\iota z)\forall y\ (y \int x \equiv z \lt y)$ the complement individual of $x$ is the individual that is a part of all and only those individuals that are discrete from $x$

**D2.047**

$x + y =_{df} (\iota z)\forall w\ (w \overlaps z \equiv (w \overlaps x \lor w \overlaps y))$ the mereological sum of $x$ and $y$ is the individual that overlaps all and only those individual that overlap either $x$ or $y$

Goodman remarks that we cannot define the mereological sum of $x$ and $y$ as that individual that has as parts all and only those individuals that are part of either $x$ or $y$, $(\iota z)\forall w\ (w \lt z \equiv (w \lt x \lor w \lt y))$, which might be tempting in analogy to the definition of product. A given mereological sum, $z$, of a part of $x$ and a part of $y$ will be a part of $x + y$, while $z$ need not be itself a part of either summand (SA: 36).

The system has one axiom, and two axiom schemata. The axiom is formulated in terms of overlap only:

**2.41**

$x \overlaps y \equiv \exists z\forall w\ (w \overlaps z \supset (w \overlaps x \land w \overlaps y))$ “If and only if two individuals $x$ and $z$ overlap is there some individual $z$ (viz., and individual wholly contained within $x$ and within $y$), such that whatever overlaps $z$ also overlaps both $x$ and $y$” (SA: 34)

Since Goodman uses no class terms in his formulation of the Calculus of Individuals in SA, there are no definitions or axioms for fusion or nucleus. Instead, Goodman employs axiom schemata to do the work. It may be permitted to formulate these in the following way (Goodman only formalizes a definite description of the individual, but not the full axiom schema). Where *φ* can be any predicate, simple or complex:

> $\exists x\ \varphi(x) \supset \exists z\forall y\ (z \overlaps y \equiv \exists v\ (\varphi(v) \land v \overlaps y))$
>
> If there is an individual that is *φ*, then there is an individual that overlaps all and only those individuals that overlap some individual that is *φ*
>
> $\exists x\forall w\ (\varphi(w) \supset x \lt w) \supset \exists z\forall y\ (y \lt z \equiv \forall v\ (\varphi(v) \supset y \lt v))$
>
> If there is an individual that is a common part of all the individuals that are *φ*, then there is an individual “that has as parts all and only those individuals that are parts of all the individuals” that are *φ* (SA: 37)

The fact that the system of SA does not include classes does not preclude a plausible comparison with the mereologies introduced above. Since the set-theoretic formulation does not employ any iteration of the set-forming operation (i.e., sets of sets play no role) the axiom schemata above deliver exactly those individuals whose existence the corresponding fusion and nucleus axiom of the Leonard and Goodman Calculus of Individuals assert. Thus, accounting for the set-theoretic notions by open sentences accordingly, the calculus of SA is equivalent to the Leonard and Goodman calculus (Simons 1987: §2.4; Ridder 2002: 98), and hence to the other systems too.

For references, please see the Bibliography in the main entry
