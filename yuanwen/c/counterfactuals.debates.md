# counterfactuals — debates（supplement）

> （《counterfactuals》词条补充材料，源：plato.stanford.edu/entries/counterfactuals/debates.html）

#### Supplement to Counterfactuals

## Debates over Counterfactual Principles

This supplemental entry provides an overview of some of the debates over various counterfactual principles, such as:

- A.1 Centering Principles
- A.2 Uniqueness Principles and the Duality of *might* and *would*
- A.3 The Limit Assumption
- A.4 SDA and REA
- A.5 Uniformity Principles
- A.6 Import-Export

As we’ll see, many of these principles “correspond” to non-trivial constraints on world-orderings in the ordering semantics. Very roughly, a counterfactual principle P corresponds to a constraint C on world-orderings iff the class of world-orderings that satisfy C is the largest class of world-orderings over which P is valid. (For more about correspondence theory, see the entry on modal logic.)

Throughout, we minimally assume $\leq_w$ is a total preorder (see section 5.1) and that $R$ is reflexive (i.e., $w \in R(w)$). This ensures the following minimal principles hold, which we appeal to throughout:

- **Identity:** $\vDash {{A}} \mathbin{>} {{A}}$
- **Right Weakening:** if ${{B}} \vDash {{C}}$, then ${{A}} \mathbin{>} {{B}} \vDash {{A}} \mathbin{>} {{C}}$
- **Agglomeration:** ${{A}} \mathbin{>} {{B}}, {{A}} \mathbin{>} {{C}} \vDash {{A}} \mathbin{>} ({{B}} \wedge {{C}})$
- **Replacement of Equivalent Antecedents (REA):** if $\vDash {{A}} \equiv {{B}}$, then $\vDash ({{A}} \mathbin{>} {{C}}) \equiv ({{B}} \mathbin{>} {{C}})$
- **T Axiom:** $A \vDash \neg({{A}} \mathbin{>} \bot)$

Regarding the T Axiom, note that $\neg({{A}} \mathbin{>} \bot)$ is true iff there is an accessible ${{A}}$-world, i.e., ${{A}}$ is possible. Similarly, $\neg{{A}} \mathbin{>} \bot$ is true iff $\neg{{A}}$ is true at no accessible world, i.e., ${{A}}$ is necessary. This gives us a way to define $\Box$ and $\Diamond$ in terms of $\mathbin{>}$, which we implicitly use below:

- $\Box{{A}} \mathrel{\colon=} (\neg{{A}} \mathbin{>} \bot)$
- $\Diamond{{A}} \mathrel{\colon=} \neg({{A}} \mathbin{>} \bot)$

With these definitions, the statement of the T Axiom above reduces to the typical statement from modal logic (viz., ${{A}} \vDash \Diamond{{A}}$, or, equivalently, $\Box{{A}} \vDash {{A}}$).

### A.1 Centering Principles

Centering principles are motivated by the intuitive idea that nothing is closer or more similar to a world than it is to itself. Two constraints on world-orderings capture this idea:

- **weak centering:** every world is at least as close to itself as any other world if $x \in R(w)$, then $w \leq_w x$
- **(strong) centering:** every world is the unique closest world to itself if $x \in R(w)$ and $x \neq w$, then $w <_w x$

Weak centering corresponds to the following natural principle:

- **Modus Ponens**: ${{A}} \mathbin{>} {{C}}, A \vDash {{C}}$

In support of Modus Ponens, the following inference seems valid:

**(A1)**

a. If George were caught, he would face years of prison.

**b.**

Actually, George did get caught.

**c.**

In that case, he will face years of prison.

Most theorists accept Modus Ponens for logically simple counterfactuals. Complications arise, however, for “right-nested” counterfactuals whose consequent is itself a counterfactual. Briggs (2012: 150) gives the following example (cf. McGee’s (1985) counterexample to modus ponens for indicatives). Imagine a captain is deciding whether to order a soldier to execute a prisoner. The soldier is loyal and highly accurate. Ultimately, the captain gives the order, the soldier shoots, and the prisoner dies. Now consider:

**(A2)**

a. If the soldier had shot the prisoner, then (even) if the captain hadn’t given the order to shoot, the prisoner (still) would have died. ${{S}} \mathbin{>} (\neg{{O}} \mathbin{>} {{D}})$

**b.**

Actually, the soldier did shoot the prisoner. ${{S}}$

**c.**

So, if the captain hadn’t given the order to shoot, the prisoner would have died. $\neg{{O}} \mathbin{>} {{D}}$

Since the soldier is accurate, (A2a) seems true. And (A2b) is true by stipulation of the case. But since the soldier is loyal (A2c) seems false. What to make of such counterexamples is hotly debated (Kolodny and MacFarlane 2010; Yalcin 2012; Bledin 2015; Stojnić 2017; Mandelkern 2020, 2024; Stern 2021). We’ll return to this example in section A.6.

Strong centering corresponds to a stronger principle, which entails Modus Ponens (via the T Axiom):

- **And-to-If** (i.e., **True-True**): ${{A}}, {{C}} \vDash {{A}} \mathbin{>} {{C}}$

In support of this principle, the following dialogue seems felicitous:

**(A3)**

a. [You are given the option to bet on a fair coin toss. Your friend says:] If you were to bet on heads, you would win.

**b.**

[You accept the bet. The coin lands heads. Your friend says:] See, I was right!

The response in (A3b) only makes sense if And-to-If is valid. Moreover, centering seems highly plausible when thinking about the intuitive notion of similarity or closeness.

Against this, however, the following inference sounds questionable to say the least:

**(A4)**

a. A fair coin was flipped and it landed heads.

**b.**

So, if the coin had been flipped, it would have landed heads.

Theorists disagree on what to make of such cases. Both D. Lewis (1973b: §1.7) and Stalnaker (1968) defend And-to-If, offering pragmatic explanations for why examples like (A4) sound odd (cf. Leahy 2011; Zakkou 2019). Other theorists propose dropping centering in favor of weak centering (e.g., J. Bennett 1974: 387–8). However, Walters and Williams (2013) and Walters (2016) provide a very thorough defense of And-to-If and offer a helpful survey of the objections to it (see also the back-and-forth between Lee Walters and Arif Ahmed in Walters 2009, Ahmed 2011, and Walters 2011).

### A.2 Uniqueness Principles and the Duality of *might* and *would*

David Lewis and Robert Stalnaker were both prominent defenders of the variably strict analysis and made major contributions to its development. However, they fundamentally disagreed over which constraints should be imposed on world-orderings.

The first point of disagreement was over uniqueness:

- **uniqueness (linearity):** there are no ties, i.e., distinct worlds cannot be equally close if $x \equiv_w y$, then $x = y$

Assuming the limit assumption (section B.3), uniqueness corresponds to the following principles (which are provably equivalent using the minimal principles above):

- **Conditional Excluded Middle (CEM)**: $\vDash ({{A}} \mathbin{>} {{C}}) \vee ({{A}} \mathbin{>} \neg{{C}})$
- **Negation Commutativity**: $\Diamond{{A}} \vDash \neg({{A}} \mathbin{>} {{C}}) \equiv ({{A}} \mathbin{>} \neg{{C}})$
- **Disjunction Distributivity**: ${{A}} \mathbin{>} ({{B}} \vee {{C}}) \vDash ({{A}} \mathbin{>} {{B}}) \vee ({{A}} \mathbin{>} {{C}})$

Stalnaker (1968: 46, 1981) famously defended these principles. Lewis (1973b: §3.4) famously rejected them.

Against these principles, Lewis (1973b: 80) borrows an example from Quine (1950: Ch.3):

**(A5)**

a. If Bizet and Verdi were compatriots, Bizet would be Italian.

**b.**

If Bizet and Verdi were compatriots, Verdi would be French.

Neither of these counterfactuals seems true. Yet, according to the uniqueness principles, one of these counterfactuals must be true.

Here is another way to put the point. It is tempting to say both of the following are true:

**(A6)**

a. If Bizet and Verdi were compatriots, Bizet might be Italian.

**b.**

If Bizet and Verdi were compatriots, Verdi might be French.

Yet (A6a) is equivalent to the negation of (A5b), and (A6b) is equivalent to the negation of (A5a), given the following principle:

- **Duality**: $\vDash ({{A}} \mathbin{>}_m {{C}}) \equiv \neg({{A}} \mathbin{>} \neg{{C}})$, where $\mathbin{>}_m$ symbolizes *might*-counterfactuals

More generally, CEM and Duality together entail the collapse of *might*- and *would*-counterfactuals, i.e., that ${{A}} \mathbin{>}_m {{C}}$ is equivalent to $\Diamond{{A}} \wedge ({{A}} \mathbin{>} {{C}})$!

At the same time, there is linguistic support for these uniqueness principles. Many of their instances sound correct.

**(A7)**

a. It’s not the case that if you were to eat that mushroom, you would live. $\neg({{E}} \mathbin{>} {{L}})$

**b.**

So, if you were to eat that mushroom, you would not live. ${{E}} \mathbin{>} \neg{{L}}$

Relatedly, Higginbotham (1986) presents evidence for these principles given how they interact with quantifiers. For example, (A8a) and (A8b) sound equivalent, suggesting Negation Commutativity holds:

**(A8)**

a. No one would decline if they were invited. $\neg\exists x({{I}}x \mathbin{>} {{D}}x)$, or equivalently $\forall x\neg({{I}}x \mathbin{>} {{D}}x)$

**b.**

Everyone would not decline if they were invited. $\forall x({{I}}x \mathbin{>} \neg{{D}}x)$

There is also a strong probabilistic argument for these principles. Imagine a fair coin is never flipped. How likely is it that if the coin were flipped, it would land heads? Most speakers judge the answer to be 50%. This suggests (A9a) is 50% likely to be true, and likewise for (A9b).

**(A9)**

a. If the coin were flipped, it would land heads. ${{F}} \mathbin{>} {{H}}$

**b.**

If the coin were flipped, it would land tails. ${{F}} \mathbin{>} \neg{{H}}$

Now, (A9a) and (A9b) are mutually exclusive: they can’t both be true. By the law of total probability, it follows that the probability of their disjunction is the sum of the probabilities of each disjunct, which comes to 100%. This suggests every instance of CEM has probability 1, which is hard to explain unless CEM holds. (For further arguments, see Stalnaker 1981; Williams 2010; Santorio 2017; Mandelkern 2018c; Khoo 2022.)

In reply to the counterexample in (A5), Stalnaker (1980, 1984: Ch. 7) analyzes such cases as vagueness in the similarity of worlds along supervaluationist lines (cf. van Fraassen 1966; Swanson 2012; see the entries on vagueness and the sorites paradox). The basic idea is that there is indeterminacy in the notion of similarity being used. Under one resolution (A5a) is true while under another (A5b) is true. But every resolution makes one or the other true.

In reply to the Duality problem, Stalnaker (1980, 1984: Ch.7) suggests the *might* in *might*-counterfactuals takes wide scope over the entire counterfactual and generally expresses a kind of epistemic possibility (DeRose (1999) strengthens “generally” to “always”). Stalnaker (1984: 43–44) motivates this by observing that (A10a) seems equivalent to (A10b). J. Bennett (2003) alternatively suggests (A10a) is equivalent to (A10c), where *might* only scopes over the consequent (cf. Lewis 1986b).

**(A10)**

a. If John had been invited, he might have come to the party. ${{I}} \mathbin{>}_m {{C}}$

**b.**

It might be that if John had been invited, he would have come to the party. $\Diamond_m({{I}} \mathbin{>} {{C}})$

**b.**

If John had been invited, it might be that he would have come to the party. ${{I}} \mathbin{>} \Diamond_m{{C}}$

Either way, the clash between *would* and *might* is explained in the same way one explains the infelicity of epistemic contradictions (cf. DeRose 1999; Williams 2010; Moss 2013; Mandelkern 2018c; Kocurek 2022; Schultheis 2024):

**(A11)**

\#It’s raining and it might not be raining. ${{R}} \wedge \Diamond_m{{R}}$

The debates over CEM and Duality continue to attract arguments on each side (van Fraassen 1976; Higginbotham 1986, 2003; DeRose 1994, 1999; von Fintel and Iatridou 2002; J. Bennett 2003; Kaufmann 2009; Williams 2010; Klinedinst 2011; Swanson 2012; Bacon 2015; Santorio 2017; Mandelkern 2018c, 2024; Cariani and Goldstein 2020; Kocurek 2022; Schultheis 2024; Willer 2025).

### A.3 The Limit Assumption

The second point of disagreement between Lewis and Stalnaker was over the limit assumption:

- **limit assumption (well-foundedness):** there are no “infinite descending chains” of ever closer and closer worlds there are no $x_1,x_2,x_3,\dots$ where $x_1 >_w x_2 >_w x_3 > \cdots$ ad infinitum

Equivalently, this says there is always at least one closest $P$-world whenever $P$ is possible (i.e., if $\varnothing \neq P \subseteq W$, there is an $x \in P$ where $x \leq_w y$ for all $y \in P$). Stalnaker (1968, 1981) accepts this assumption. Lewis (1973b: 20) rejects it.

D. Lewis (1973b: 20) provides the following counterexample. Consider this one inch line:

$\rule{1in}{.5ex}$

Suppose, counterfactually, that this line were more than one inch long. How long would it be? Presumably, for any world where the line is $(1\frac{1}{n})''$ long, there is a closer/more similar world where the line is just a bit shorter, say $(1\frac{1}{n+1})''$. But then there is no closest/most similar world where the line is more than one inch long.

Stalnaker (1981, 1984: 141–142) replies that, in most contexts, not every minute difference counts towards similarity. In a context where “every difference in length is important”, Stalnaker says the antecedent *if the line were more than one inch long* is inappropriate. This could be construed as either a rejection of the example or an acknowledgement that the limit assumption fails in such hyper-precise contexts (Kocurek 2025). That said, Swanson (2012) shows how one can accommodate Lewis’s example without dropping the limit assumption.

Pollock (1976: 20) and Herzberger (1979) provide a more powerful defense of the limit assumption. They observe it corresponds to the following “infinitary” principle:

- **Infinite Agglomeration**: ${{A}} \mathbin{>} {{C}}_1, {{A}} \mathbin{>} {{C}}_2, {{A}} \mathbin{>} {{C}}_3,\dots \vDash {{A}} \mathbin{>} ({{C}}_1 \wedge {{C}}_2 \wedge {{C}}_3 \wedge \cdots)$

Many theorists find this principle as plausible as its finite counterpart, Agglomeration (see Fine 2012b for a thorough defense). Indeed, Infinite Agglomeration can be used to undermine Lewis’s own counterexample. Consider the following series of counterfactuals:

**(A12)**

a. If the line were more than $1''$ long, it would be less than $(1\frac{1}{2})''$ long.

**b.**

If the line were more than $1''$ long, it would be less than $(1\frac{1}{3})''$ long.

**c.**

If the line were more than $1''$ long, it would be less than $(1\frac{1}{4})''$ long. $\vdots$

Intuitively, these counterfactuals cannot all be true. After all, they seem to entail the following absurd counterfactual (as one would expect if Infinite Agglomeration holds):

**(A13)**

If the line were more than $1''$ long, it would be no more than $1''$ long.

By contrast, if Lewis is right that for every world where the line is $(1\frac{1}{n})''$ long, there is a closer world where the line is $(1\frac{1}{n+1})''$ long, the counterfactuals in (A12) are jointly consistent and do not entail (A13). Thus, Lewis’s “counterexample” to the limit assumption only highlights its indispensability.

The debates over the limit assumption are complex. Kaufmann (2017) observes that there are many versions of the limit assumption that one could endorse. Dorr and Mandelkern (2024) and Kocurek (2025) observe that depending on how the constraint is formulated, the logic of conditionals may not be fully axiomatizable.

### A.4 SDA and REA

One of the most widely discussed criticisms of the variably strict analysis concerns how it handles counterfactuals with disjunctive antecedents. Such counterfactuals are a crucial test case for the semantics of counterfactuals, as they shed light on whether the apparent non-monotonicity of counterfactuals should be explained semantically or pragmatically.

Consider the following inference (modified from (19)):

**(A14)**

a. If either the left or the right switch were flipped up, the light would be on.

**b.**

So, if the left switch were flipped up, the light would be on.



Generally, inferences of this form seem valid. This suggests the following principle holds:

- **Simplification of Disjunctive Antecedents (SDA)**: $({{A}} \vee {{B}}) \mathbin{>} {{C}} \vDash ({{A}} \mathbin{>} {{C}}) \wedge ({{B}} \mathbin{>} {{C}})$

However, SDA is not valid on the ordering semantics (see Figure 4). The closest ${{A}} \vee {{B}}$-worlds may all be ${{A}}$-worlds, while the closest ${{B}}$-worlds are strictly further. In that case, $({{A}} \vee {{B}}) \mathbin{>} {{C}}$ may fail to ensure ${{B}} \mathbin{>} {{C}}$ is true. Many theorists view this as a serious problem for variably strict analyses (Fine 1975; Nute 1975b; Loewer 1976; Ellis, Jackson, and Pargetter 1977; Warmbrōd 1981a).

One cannot address this objection by imposing a constraint on world-orderings. For SDA corresponds to the requirement that all accessible worlds be equally close (i.e., $x \equiv_w y$ for all $x,y \in R(w)$). This would collapse the variably strict analysis to the strict conditional analysis, however: given this constraint, a counterfactual is true on the ordering semantics iff its antecedent necessarily implies its consequent.

SDA poses a more general challenge for non-monotonic analyses. Assuming classical logic, SDA and REA together imply Antecedent Strengthening. For in classical propositional logic, ${{A}}$ is equivalent to $({{A}} \wedge {{B}}) \vee ({{A}} \wedge \neg{{B}})$. Thus:

$$\begin{align} \tag*{1.} &A \gt C &\text{(premise)} \\ \tag*{2.} &((A \wedge B) \vee (A \wedge \neg B)) &\text{(REA,1)} \\ \tag*{3.} &(A \wedge B) \gt C &\text{(SDA,2)} \end{align}$$

That said, SDA is not unproblematic. For one, recall that McKay and van Inwagen (1977: 354) give the following counterexample (repeated from (15)):

**(A15)**

a. If Spain had fought for the Allies or the Axis, it would have fought for the Axis. $({{L}} \vee {{X}}) \mathbin{>} {{X}}$

**b.**

\#If Spain had fought for the Allies, it would have fought for the Axis. ${{L}} \mathbin{>} {{X}}$

There is also a tension between CEM and SDA. Together, they classically entail the trivializing principle $\neg({{A}} \mathbin{>} \neg{{C}}) \vDash {{B}} \mathbin{>} {{C}}$ (Cariani and Goldstein 2020; this is an equivalent statement of the principle they call “The Interconnectivity of All Things”):

$$\begin{align} \tag*{1.} &\neg(A \gt \neg C) &\text{(premise)}\\ \tag*{2.} &\neg(A \vee B) \gt \neg C) &\text{(SDA,1)} \\ \tag*{3.} &((A \vee B) \gt C) \vee ((A \vee B) \gt \neg C) &\text{(CEM)} \\ \tag*{4.} &(A \vee B) \gt C &\text{(2, 3)} \\ \tag*{5.} &B \gt C &\text{(SDA,4)} \end{align}$$

Willer (2025: 32) gives an example to illustrate this tension. (His example involves indicatives, but it’s easily adapted to counterfactuals.) Suppose an urn has 101 coins: 90 gold, 10 silver, and 1 plastic. The gold coins are winners while the silver and plastic ones are losers. Now consider:

**(A16)**

a. If John were to draw a gold or silver coin, he would win.

**b.**

If John were to draw a gold or silver coin, he would lose.

SDA implies that both of these sentences are false. For example, (A16a) is false since John would lose if he were to draw a silver coin. By contrast, CEM implies one of these must be true (though perhaps it’s indeterminate which). Following the probabilistic argument for CEM (section A.2), one might say, for example, that (A16a) is 90% likely to be true, since it’s 90% likely that if John were to draw a gold or silver coin, he would draw a gold coin (and thus, would win).

That said, the ordering semantics validates a restricted version of SDA:

- **Limited SDA**: $\neg(({{A}} \vee {{B}}) \mathbin{>} \neg{{A}}), ({{A}} \vee {{B}}) \mathbin{>} {{C}} \vDash {{A}} \mathbin{>} {{C}}$

Ordering theorists may thus argue that in examples like (A14), where SDA seems valid, speakers are (perhaps naturally) implicitly assuming a missing premise needed to make the argument strictly valid, viz., (A17):

**(A17)**

It’s not true that if either the left switch or the right switch had been flipped, it would not have been the left one. [Simplified using Duality: If either the left or right switch had been flipped, it might have been the left one.]

By contrast, the missing premise needed to render (A15) valid is explicitly denied by (A15a), which is why the inference seems fallacious.

More sophisticated responses are also available. Lewis (1977), Nute (1980a), Alonso-Ovalle (2009), and Starr (2014a: 1049) each develop variably strict analyses where disjunction is given a non-Boolean interpretation to validate SDA without validating the other counterfactual fallacies (see Franke 2011; Lassiter 2018; Santorio 2020; Schultheis 2025 for alternative variably strict responses).

This is not the end of the story, however. Starr (2014b: 2) observes that while counterfactuals do not generally simplify, as illustrated by examples like (A15), they seem to always simplify in “double-if” constructions of the form *If A or if B, then C*. For example, (A18) sounds much worse than (A15a), suggesting that (A18) simplifies (see Starr 2014b; Khoo 2017, 2021, 2022a; Klinedinst 2024).

**(A18)**

\#If Spain had fought for the Allies or if Spain had fought for the Axis, it would have fought for the Axis.

Recent empirical work also suggests a difference between disjunctive antecedents and their Boolean equivalents. Ciardelli, Zhang, and Champollion (2018) (extending Champollion et al. 2016) present a simple yet powerful demonstration of this. Suppose there is a light connected to two switches, *A* and *B*. The light turns on iff the switches are in the same position. Right now, both switches are up, and so the light is on. Now consider:

**(A19)**

a. If either switch *A* or switch *B* were down, the light would be off. $(\neg{{A}} \vee \neg{{B}}) \mathbin{>} \neg{{L}}$

**b.**

If switch *A* and switch *B* weren’t both up, the light would be off. $\neg({{A}} \wedge {{B}}) \mathbin{>} \neg{{L}}$

By De Morgan’s laws, the antecedents of these conditionals are equivalent: $\neg{{A}} \vee \neg{{B}}$ is logically equivalent to $\neg({{A}} \wedge {{B}})$. Yet Ciardelli et al. (2018) conducted experiments showing speakers typically judge (A19a) as much more acceptable than (A19b). Intuitively, (A19a) seems to say of each switch that if it were down, the light would be off (since the other switch would still be up). By contrast, (A19b) seems to say that if one or both switches were down, the light would be off. (Caveat: this effect might subtly depend on the exact phrasing; see Rips and Edwards 2010; Romoli, Santorio, and Wittenberg 2022.) This suggests a core principle of variably strict analyses, viz., REA, fails: logically equivalent antecedents behave differently in counterfactuals (cf. section 7.2). Theorists disagree over the best way to accommodate all of this data, however (Fine 2012a,b; Starr 2014a,b; Khoo 2017, 2021, 2022a; Willer 2017, 2025; Ciardelli, Zhang, and Champollion 2018; Lassiter 2018; Santorio 2018, 2020; K. Schulz 2018; Cariani and Goldstein 2020; Romoli, Santorio, and Wittenberg 2022; Güngör 2023; Klinedinst 2024).

### A.5 Uniformity Principles

Another controversy is over principles concerning when two counterfactual antecedents may be treated in a “uniform” manner. The most widely discussed uniformity principle is what Nute (1980b: 52) (for reasons unknown to us) calls “CSO” (also called “Counterfactual Equivalence” (Bacon 2023), “Reciprocity” (McHugh and Klochowicz 2024), or “Substitution of Subjunctive Equivalents” (Starr 2019)):

- **CSO**: ${{A}} \mathbin{>} {{B}}, {{B}} \mathbin{>} {{A}} \vDash ({{A}} \mathbin{>} {{C}}) \equiv ({{B}} \mathbin{>} {{C}})$

Given the minimal counterfactual principles above, CSO is equivalent to the conjunction of two other principles:

- **Limited Antecedent Strengthening**: ${{A}} \mathbin{>} {{B}}, {{A}} \mathbin{>} {{C}} \vDash ({{A}} \wedge {{B}}) \mathbin{>} {{C}}$
- **Limited Transitivity**: ${{A}} \mathbin{>} {{B}}, ({{A}} \wedge {{B}}) \mathbin{>} {{C}} \vDash {{A}} \mathbin{>} {{C}}$

The ordering semantics validates all of these principles. In support of them, many of their instances seem reasonable. Here is an example of CSO:

**(A20)**

a. If Ann had gone to the party, Ben would have gone. ${{A}} \mathbin{>} {{B}}$

**b.**

If Ben had gone to the party, Ann would have gone. ${{B}} \mathbin{>} {{A}}$

**c.**

If Ann had gone to the party, it would have been fun. ${{A}} \mathbin{>} {{F}}$

**d.**

So, if Ben had gone to the party, [Ann would have gone, and so] it would have been fun. ${{B}} \mathbin{>} {{F}}$

Moreover, these uniformity principles would nicely explain why some instances of the counterfactual fallacies, such as (16) and (17), seem plausible: each is missing a premise, which is naturally implicitly assumed by the speakers (cf. our discussion of Limited SDA above).

Some theorists have questioned these principles, however. Pollock (1976, 1981: 254) gives a complicated counterexample to CSO (involving a circuit with three switches and two lights). Bacon (2023) and McHugh and Klochowicz (2024) give more intuitive counterexamples. To use McHugh and Klochowicz’s example, imagine a light is connected to two switches, *A* and *B*, which can be in the up, neutral, or down position. The light turns on iff switch *A* is neutral and switch *B* is either up or neutral. Right now, *A* is neutral and *B* is down, so the light is off. Now consider:

**(A21)**

a. If switch *B* were not down, neither switch would be down. $\neg{{B}} \mathbin{>} \neg({{A}} \vee {{B}})$

**b.**

If neither switch were down, switch *B* would not be down. $\neg({{A}} \vee {{B}}) \mathbin{>} \neg{{B}}$

**c.**

If switch *B* were not down, the light would be on. $\neg{{B}} \mathbin{>} {{L}}$

**d.**

If neither switch were down, the light would be on. $\neg({{A}} \vee {{B}}) \mathbin{>} {{L}}$

Here, (A21a) and (A21b) seem true. By CSO, then, (A21c) and (A21d) should be equivalent. Yet McHugh and Klochowicz (2024) ran experiments to test this, finding subjects generally found (A21c) much more acceptable than (A21d). (Interestingly, the reason seems similar to the reason why speakers seem to judge (A19a) and (A19b) differently.) Bacon (2023) and McHugh and Klochowicz (2024) both present theories that aim to explain such failures of uniformity principles. What to make of these counterexamples is very much a live debate.

### A.6 Import-Export

A final point of controversy concerns principles governing nested counterfactuals. Recall the counterexample to Modus Ponens (repeated from (A2)):

**(A22)**

a. If the soldier had shot the prisoner, then (even) if the captain hadn’t given the order to shoot, the prisoner (still) would have died. ${{S}} \mathbin{>} (\neg{{O}} \mathbin{>} {{D}})$

**b.**

Actually, the soldier did shoot the prisoner. ${{S}}$

**c.**

So, if the captain hadn’t given the order to shoot, the prisoner would have died. $\neg{{O}} \mathbin{>} {{D}}$

It is natural to interpret (A22a) as equivalent to (A23):

**(A23)**

If the soldier had shot the prisoner and the captain hadn’t given the order to shoot, the prisoner (still) would have died. $({{S}} \wedge \neg{{O}}) \mathbin{>} {{D}}$

This supports a more general principle, which states right-nested conditionals are equivalent to unnested conditionals with conjunctive antecedents:

- **Import-Export**: $\vDash ({{A}} \mathbin{>} ({{B}} \mathbin{>} {{C}})) \equiv (({{A}} \wedge {{B}}) \mathbin{>} {{C}})$

Intuitively, this says one can “import” a right-nested antecedent into the main antecedent, and one can “export” a conjunct in the main antecedent into its own nested antecedent.

Neither the strict semantics nor the ordering semantics validates this principle (though the strict analysis validates the left-to-right direction, Import, assuming $R$ is shift-reflexive: if *wRv*, then *vRv*). At first, this seems like a problem given how natural inferences like the following are:

**(A24)**

a. If Simone had drummed, then if Jean-Paul had danced, Claude would have stayed for another drink. ${{S}} \mathbin{>} ({{J}} \mathbin{>} {{C}})$

**b.**

So, if Simone had drummed and Jean-Paul had danced, Claude would have stayed for another drink. $({{S}} \wedge {{J}}) \mathbin{>} {{C}}$

Mandelkern (2021) and Santorio (2023) present counterexamples, however. To use Santorio’s case, imagine a game show host randomly selects a number between 1 and 6. They do this by first flipping a coin to determine whether they select from the low numbers (1, 2, 3) or the high numbers (4, 5, 6) and then select randomly from the chosen set. In fact, they select a 1. Now consider:

**(A25)**

a. If the host had selected 5, then if they had (instead) selected an even number, they would have selected a 4. ${{5}} \mathbin{>} ({{E}} \mathbin{>} {{4}})$

**b.**

\#If the host had selected 5 and they had (instead) selected an even number, they would have selected a 4. $({{5}} \wedge {{E}}) \mathbin{>} {{4}}$

While (A25b) is clearly defective, Santorio suggests (A25a) has a coherent reading on which it has a 50% probability: if they had selected a 5, they would have been selecting from a high number, and so if they had (instead) selected an even from that group, there would be a 50% chance of selecting 4. This suggests at least one direction of Import-Export (viz., Import) fails.

Moreover, Gibbard (1981) famously proved a triviality result that suggests Export is problematic:

- **Gibbard’s Triviality Result** If Modus Ponens, Import-Export, and Conditional Proof (if ${{A}} \vDash {{B}}$, then $\vDash {{A}} \rightarrow {{B}}$) all hold, and if $\vDash$ obeys classical logic, then $\mathbin{>}$ is equivalent to the material conditional $\supset$.
- *Proof:* By Modus Ponens, ${{A}} \mathbin{>} {{B}} \vDash {{A}} \supset {{B}}$. Conversely:

$$\begin{align} \tag*{1.} &A \supset B &\text{(premise)} \\ \tag*{2.} &((A \supset B) \wedge A) \gt B &\text{(Conditional Proof)} \\ \tag*{3.} &(A \supset B) \gt (A \gt B) &\text{(Import-Export,2)} \\ \tag*{4.} &A \gt B &\text{(Modus Ponens,1,3)} \end{align}$$

This result suggests that, realistically, counterfactuals cannot validate Modus Ponens and Import-Export. Other triviality results implicate Import-Export (Mandelkern 2018b, 2021; Mandelkern and Rothschild 2021). What to make of these results is a matter of controversy (Kratzer 1986, 2012; Gillies 2009, 2010; Khoo 2013; Mandelkern 2021, 2024; Khoo and Mandelkern 2019; Cariani 2021: Ch. 8; Willer 2025).
