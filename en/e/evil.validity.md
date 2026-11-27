# evil — validity（supplement）

> （《evil》词条补充材料，源：plato.stanford.edu/entries/evil/validity.html）

#### Supplement to The Problem of Evil

## The Validity of the Argument

That the argument is deductively valid can be seen as follows. First, let us introduce the following abbreviations:

- $\textit{State}(x)$: $x$ is a state of affairs
- $\textit{Dying}(x)$: $x$ is a state of affairs in which an animal dies an agonizing death in a forest fire
- $\textit{Suffering}(x)$: $x$ is a state of affairs in which a child undergoes lingering suffering and eventual death due to cancer
- $\textit{Bad}(x)$: $x$ is intrinsically bad or undesirable
- $\textit{Omnipotent}(x)$: $x$ is omnipotent
- $\textit{Omniscient}(x)$: $x$ is omniscient
- $\textit{MorallyPerfect}(x)$: $x$ is morally perfect
- $\textit{PreventsExistence}(x,y)$: $x$ prevents the existence $y$
- $\textit{God}(x)$: $x$ is God
- $\textit{HasPowerToPreventWithout}(x,y)$: $x$ has the power to prevent the existence of $y$ without hereby either allowing an equal or greater evil, or preventing an equal or greater good

The argument just set out can then be formulated as follows:

- (1) $\exists x [ \textit{State}(x) \,\wedge$ $ ( \textit{Dying}(x) \vee \textit{Suffering}(x) ) \,\wedge$ $ \textit{Bad}(x) \,\wedge $ $ \forall y ( \textit{Omnipotent}(y) \rightarrow \textit{HasPowerToPreventWithout}(y,x) ) ]$
- (2) $\forall x [ \textit{State}(x) \rightarrow \forall z \neg \textit{PreventsExistence}(z,x) ]$
- (3) $\forall x \forall y [ ( \textit{Bad}(x) \,\wedge$ $ \textit{HasPowerToPreventWithout}(y,x) \,\wedge$ $ \neg \textit{PreventsExistence}(y,x) ) \rightarrow \neg ( \textit{Omniscient}(y) \,\wedge$ $ \textit{MorallyPerfect}(y) ) ]$

Therefore, from (1), (2), and (3),

- (4) $\forall x \neg [ \textit{Omnipotent}(x) \,\wedge$ $ \textit{Omniscient}(x) \,\wedge$ $ \textit{MorallyPerfect(x)}]$
- (5) $\forall x [ \textit{God}(x) \,\rightarrow$ $ (\textit{Omnipotent}(x) \wedge \textit{Omniscient}(x) \wedge \textit{MorallyPerfect}(x) )]$

Therefore,

- (6) $\neg \exists x [God(x)]$

The premises here are (1), (2), (3), and (5), and they can be shown to entail the conclusion, (6), as follows.

### The Inference from (1), (2), and (3) to (4)

- (i) $\textit{State}(A) \wedge (\textit{Dying}(A) \vee \textit{Suffering}(A)) \,\wedge$ $ \textit{Bad}(a) \,\wedge$ $ \forall y (\textit{Omnipotent}(y) \rightarrow \textit{HasPowerToPreventWithout}(y,A))$ From (1), via EE (Existential Elimination).
- (ii) $\forall z \neg \textit{PreventsExistence}(z,A)$ From (2) and 1st conjunct of (i) by UE and MP.
- (iii) $\textit{Omnipotent}(G)$ Assumption for conditional proof (‘$G$’ arbitrary)
- (iv) $\textit{HasPowerToPreventWithout}(G,A)$ From 4th conjunct of (i), by instantiating ‘$G$’ and using MP.
- (v) $\neg \textit{PreventsExistence}(G,A)$ From (ii), by UE.
- (vi) $\textit{Bad}(A) \wedge \textit{HasPowerToPreventWithout}(G,A) \,\wedge$ $ \neg \textit{PreventsExistence}(G,A))$ Conjoin 3rd conjunct of (i) with (iv) and (v).
- (vii) $\neg(\textit{Omniscient}(y) \wedge \textit{MorallyPerfect}(G))$ From (3) and (6), by UE and MP.
- (viii) $\textit{Omnipotent}(G) \rightarrow \neg(\textit{Omniscient}(G) \wedge \textit{MorallyPerfect}(G))$ Conditional Proof, (iii)–(vii).
- (ix) $\neg(\textit{Omnipotent}(G) \wedge \textit{Omniscient}(G) \wedge \textit{MorallyPerfect}(G))$ From (viii), by the equivalence of $A \rightarrow B$ with $\neg(A \wedge \neg B)$, double negation elimination, and associativity of conjunctions.
- (x) $\forall x \neg(\textit{Omnipotent}(x) \wedge \textit{Omniscient}(x) \wedge \textit{MorallyPerfect}(x))$ From (ix), via UI (Universal Introduction), since ‘$G$’ was arbitrary.

### The Inference from (4) and (5) to (6)

- (i) $\neg(\textit{Omnipotent}(G) \wedge \textit{Omniscient}(G) \wedge \textit{MorallyPerfect}(G))$ From (4), via universal insantiation, and where ‘$G$’ is arbitrary.
- (ii) $\textit{God}(G) \,\rightarrow$ $(\textit{Omnipotent}(G) \wedge \textit{Omniscient}(G) \wedge \textit{MorallyPerfect}(G))$ From (5) by universal instantiation.
- (iii) $\neg \textit{God}(G)$ From (i) and (ii) by modus tollens.
- (iv) $\forall x \neg(\textit{God}(x))$ From (iii) by universal generalization, since ‘$G$’ was arbitrary.
- (v) $\neg \exists x (\textit{God}(x))$ From (iv), by interdefinability of quantifiers.

Return to The Problem of Evil
