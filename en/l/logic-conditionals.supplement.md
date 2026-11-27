# logic-conditionals — supplement（supplement）

> （《logic-conditionals》词条补充材料，源：plato.stanford.edu/entries/logic-conditionals/supplement.html）

#### Supplement to The Logic of Conditionals

## Appendix: Proof of condition $(*)$ in Section 4 of Logic of Conditionals

For the sake of simplicity, we prove the version for *acceptance of conditionals* with respect to a premise set *Γ*, which uses the following condition: $$\tag{PS\(_{acc}\)} \Gamma \Vdash_{acc} A>C \text{ iff for each } X \in \Gamma\bot |A|, \ \bigcap (X\cup |A|) \subseteq |C|. $$ The version for *truth at $w$* and with respect to $\Gamma_w$ (the premise set assigned to a world $w$) is analogous.

In the following, we assume that every proposition (subset of $W$) is expressible in our language.

Suppose that *Γ* is a (possibly infinite) set of premises (propositions). We denote by $\Gamma\bot\lvert A\rvert$ the set of all subsets $X$ of *Γ* that are maximally consistent with $A$, i.e., are maximal in having a non-empty intersection $(\bigcap X) \cap \lvert A\rvert.$

In the following, we suppose that $\lvert A\rvert$ and $\lvert B\rvert$ are non-empty.

Now suppose that $(A\vee B) >C$ is accepted w.r.t. *Γ*, i.e., for all elements $X$ of $\Gamma\bot|A\vee B|$, it holds that $(\bigcap X)\cap |A\vee B| \subseteq \lvert C\rvert.$ Equivalently,

$$\tag{1} \left(\bigcup_{X\in \Gamma\bot|A\vee B|}\bigcap X\right)\cap |A\vee B| \subseteq \lvert C\rvert. $$

We first show that

$$\tag{2} \left(\bigcup_{Y\in \Gamma\bot|A|\\ Z\in \Gamma\bot|B|} \bigcap (Y \cup Z)\right) \cap |A|\cap|B| \ \subseteq \ \bigcup_{X\in \Gamma\bot|A\vee B|}\bigcap X. $$

Take two arbitrary sets $Y\in \Gamma\bot |A|$ and $Z\in \Gamma\bot |B|$ and form the union $Y\cup Z$. Every subset of *Γ* which is a superset of $Y\cup Z$ is inconsistent both with $A$ and with $B$, so it is inconsistent with $A\vee B$. Now if $Y\cup Z$ is consistent with $A\vee B$, then $Y\cup Z$ is itself an element of $\Gamma\bot |A\vee B|$, so it appears as an $X$ on the right-hand side of (2). If, on the other hand, $Y\cup Z$ is inconsistent with $A\vee B$ (which may well be the case), then the intersection of $\bigcap (Y \cup Z)$ with $|A|\cap|B|$ will leave only the empty set. This proves (2).

From (1) and (2), we can infer

$$\tag{3} \left(\bigcup_{Y\in \Gamma\bot|A|\\ Z\in \Gamma\bot|B|} \bigcap (Y \cup Z)\right) \cap |A|\cap|B| \ \subseteq \ |C|. $$

Now we make use of the following series of equations:

$$\begin{align}\tag{4} &\left(\bigcup_{Y\in \Gamma\bot|A|\\ Z\in \Gamma\bot|B|} \bigcap (Y \cup Z)\right) \cap |A|\cap|B| \\ &\qquad= \left(\bigcup_{Y\in \Gamma\bot |A|\\ Z\in \Gamma\bot |B|} \left(\bigcap Y \cap \bigcap Z\right)\right) \cap |A|\cap|B| \\ &\qquad= \left(\bigcup_{Y\in \Gamma\bot |A|} \bigcap Y\right) \cap \left(\bigcup_{Z\in \Gamma\bot |B|} \bigcap Z\right) \cap |A|\cap|B| \notag \\ &\qquad= \left(\bigcup_{Y\in \Gamma\bot |A|} \left(\bigcap Y \cap |A|\right)\right) \cap \left(\bigcup_{Z\in \Gamma\bot |B|} \left(\bigcap Z \cap |B|\right)\right)\notag \end{align}$$

From (3) and (4), it follows that

$$\tag{5} \left(\bigcup_{Y\in \Gamma\bot |A|} \left(\bigcap Y \cap |A|\right)\right) \cap \left(\bigcup_{Z\in \Gamma\bot |B|} \left(\bigcap Z \cap |B|\right)\right) \subseteq |C|. $$

Since we assume that every proposition is expressible in our language, we can choose two sentences $D$ and $E$ such that

$$\lvert D\rvert = \bigcup_{Y\in \Gamma\bot\lvert A\rvert} \left(\bigcap Y \cap \lvert A\rvert\right)$$

and

$$\lvert E\rvert = \bigcup_{Z\in \Gamma\bot\lvert B\rvert} \left(\bigcap Z \cap \lvert B\rvert\right).$$

(5) says that $D$ and $E$ together entail $C$. By the acceptance condition (PS$_{acc}$) for conditionals, we also know that $A>D$ and $B>E$ are accepted with respect to *Γ*. This proves $(*)$. $\Box$
