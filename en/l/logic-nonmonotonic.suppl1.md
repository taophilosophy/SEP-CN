# logic-nonmonotonic — suppl1（supplement）

> （《logic-nonmonotonic》词条补充材料，源：plato.stanford.edu/entries/logic-nonmonotonic/suppl1.html）

#### Supplement to Non-monotonic Logic

## Robert Stalnaker’s Counter-Example to Rational Monotony

Given a set of initial beliefs *Γ*, Stalnaker adopts the reading of “$\alpha \dproves \beta$” as “Given our initial set of beliefs *Γ*, if we learn *α* then (non-monotonically) infer *β*.” proposed in Makinson and Gärdenfors (1991).

Consider the three composers: Verdi $(v)$, Bizet $(b)$, and Satie $(s)$, and suppose that according to our initial set of beliefs Verdi is Italian $(I(v))$, while Bizet and Satie are French $(F(b), F(s))$. Suppose now that we learn that Verdi and Bizet are compatriots $(C(v,b))$. This leads us no longer to endorse either the proposition that Verdi is Italian (because he could be French), or that Bizet is French (because he could be Italian); but we would still draw the defeasible consequence that Satie is French, since nothing that we have learned conflicts with it. Thus,

> $C(v,b) \dproves F(s)$

Now consider the proposition $C(v,s)$ that Verdi and Satie are compatriots. Before learning that $C(v,b)$ we would be inclined to reject the proposition $C(v,s)$ because we endorse $I(v)$ and $F(s)$, but after learning that Verdi and Bizet are compatriots, we can no longer endorse $I(v)$, and therefore no longer reject $C(v,s)$. Then the following *fails*:

> $C(v,b) \dproves \neg C(v,s)$.

However, if we also added $C(v,s)$ to our stock of beliefs, we would lose the inference to $F(s)$: in the context of $C(v,b)$, the proposition $C(v,s)$ is equivalent to the statement that all three composers have the same nationality. This leads us to suspend our assent to the proposition $F(s)$. In other words, and contrary to Rational Monotony, the following also *fails*:

> $C(v,b), C(v,s) \dproves F(s)$.
