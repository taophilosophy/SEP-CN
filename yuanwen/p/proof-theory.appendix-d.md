# proof-theory — appendix-d（supplement）

> （《proof-theory》词条补充材料，源：plato.stanford.edu/entries/proof-theory/appendix-d.html）

#### Supplement to Proof Theory

## D. Proof Theory of Set Theories

Clever coding allows one to express an enormous amount of ordinary mathematics in the language of second order arithmetic. Still, many statements of mathematics can only be captured in a circumscribed way in this language. More natural languages for developing mathematics are provided type theory and in its most general form by set theory. With the work of Jäger and Pohlers (1982) the forum of ordinal analysis switched from the realm of second-order arithmetic to set theory, shaping what is now called *admissible proof theory*, after the models of *Kripke-Platek set theory*, **KP**. Their work culminated in the analysis of the system $(\Delta^1_2\Hy\bCA)+\BI$.

By and large, ordinal analyses for set theories are more uniform and transparent than for subsystems of $\bZ_2$. The axiom systems for set theories considered in this paper are formulated in the usual language of set theory (called $\cL_\in$ hereafter) containing $\in$ as the only non-logical symbol besides $=$. Formulae are built from prime formulae $a\in b$ and $a=b$ by use of propositional connectives and quantifiers $\forall x,\exists x$. Quantifiers of the forms $\forall x\in a$, $\exists x\in a$ are called *bounded*. *Bounded* or *$\Delta_0$-formulae* are the formulae wherein all quantifiers are bounded; $\Sigma_1$-formulae are those of the form $\exists x\varphi (x)$ where $\varphi(a)$ is a $\Delta_0$-formula. For $n>0$, $\Pi_n$-formulae ($\Sigma_n$-formulae) are the formulae with a prefix of *n* alternating unbounded quantifiers starting with a universal (existential) one followed by a $\Delta_0$-formula. The class of $\Sigma$-formulae is the smallest class of formulae containing the $\Delta_0$-formulae which is closed under $\land$, $\lor$, bounded quantification and unbounded existential quantification.

One of the set theories which is amenable to ordinal analysis is Kripke-Platek set theory, **KP**. Its standard models are called *admissible sets*. One of the reasons that this is an important theory is that a great deal of set theory requires only the axioms of **KP**. An even more important reason is that admissible sets have been a major source of interaction between model theory, recursion theory and set theory (cf. Barwise 1975). **KP** arises from **ZF** by completely omitting the power set axiom and restricting Separation and Collection to bounded formulae. These alterations are suggested by the informal notion of “predicative”. To be more precise, the axioms of **KP** consist of *Extensionality, Pair, Union, Infinity, Bounded Separation*

$$\exists x\,\forall u\left[u\in x\leftrightarrow(u\in a\land F(u))\right]$$

for all bounded formulae $F(u)$, *Bounded Collection*

$$\forall x\in a\,\exists y\,G(x,y)\,\to\,\exists z\,\forall x\in a\,\exists y\in z\,G(x,y)$$

for all bounded formulae $G(x,y)$, and *Set Induction*

$$\forall x\,\left[(\forall y\in x\,H(y))\to H(x)\right],\to\,\forall x\,H(x)$$

for all formulae $H(x)$.

A transitive set *A* such that $(A,{\in})$ is a model of **KP** is called an *admissible set*. Of particular interest are the models of **KP** formed by segments of Gödel’s *constructible hierarchy* $\zL$. The constructible hierarchy is obtained by iterating the definable powerset operation through the ordinals

$$\begin{align} \zL_0 & =\emptyset,\\ \zL_{\lambda} & = \bigcup\{\zL_{\beta}:\beta < \lambda\}\quad {\lambda \textrm{ limit}}\\ \zL_{\beta+1} &= \big\{ X :\; X \subseteq \zL_{\beta};\;X \textrm{ definable over }\;\langle\zL_{\beta}, {\in}\rangle \big\}. \end{align}$$

So any element of $\zL$ of level *α* is definable from elements of $\zL$ with levels $<\alpha$ and the parameter $\zL_{\alpha}$. An ordinal *α* is *admissible* if the structure $(\zL_{\alpha},{\in})$ is a model of **KP**.

Formulae of $\cL_2$ can be easily translated into the language of set theory. Some of the subtheories of $\bZ_2$ considered above have set-theoretic counterparts, characterized by extensions of **KP**. **KPi** is an extension of **KP** via the axiom

$$\tag{\(\textit{Lim}\)} \forall x\exists y[x\in y\land y \textrm{ is an admissible set}].$$

**KPI** denotes the system **KPi** without Bounded Collection. It turns out that $(\Delta^1_2\Hy\bCA)+\BI$ proves the same $\cL_2$-formulae as **KPi**, while $(\bPi^1_1\Hy\bCA)$ proves the same $\cL_2$-formulae as **KPl** (see Jäger 1986).

### D.1 Admissible proof theory.

**KP** is the weakest in a line of theories that were analyzed by proof theorists of the Munich school in the late 1970s and 1980s. It can be viewed as a set-theoretic version of other well known theories.

Theorem D.1 $\lvert \KP\rvert=\lvert \bID_1\rvert=\lvert (\BI)\rvert=\psi_{\Omega_1}(\varepsilon_{\Omega_1+1})$.

In many respects, **KP** is a very special case. Several fascinating aspects of ordinal analysis do not yet exhibit themselves at the level of **KP**.

Recall that **KPI** is the set-theoretic version of $(\bPi^1_1\Hy\bCA)+\BI$, while **KPi** is the set-theoretic counterpart to $(\Delta^1_2\Hy\bCA)+\BI$. The main axiom of **KPI** says that every set is contained in an admissible set (one also says that the admissible sets are cofinal in the universe) without requiring the universe to be admissible, too. To get a sense of scale for comparing **KP**, **KPI**, and **KPi** it is perhaps best to relate the large cardinal assumptions that give rise to the pertinent ordinal representation systems. In the case of **KPI** the assumption is that there are infinitely many large ordinals $\Omega_1,\Omega_2,\Omega_3,\ldots$ (where $\Omega_n$ can be taken to be $\aleph_n$) each equipped with their own “collapsing” function $\alpha\mapsto\psi_{\Omega_n}(\alpha)$ as we saw in section 5.3.1. The ordinal system sufficient for **KPi** is built using the much bolder assumption that there is an inaccessible cardinal *I*.

As the above set theories are based on the notion of admissible set it is suitable to call the proof theory concerned with them “admissible proof theory”. The salient feature of admissible sets is that they are models of Bounded Collection and that that principle is equivalent to $\Sigma$-Reflection on the basis of the other axioms of **KP** (see Barwise 1975). Furthermore, admissible sets of the form $\zL_{\kappa}$ also satisfy $\Pi_2$-reflection, i.e., if $\zL_{\kappa}\models \forall x\,\exists y\,C(x,y,\vec{a})$ with $C(x,y)$ bounded and $\vec{a}\in\zL_{\kappa}$, then there exists $\rho<\kappa$ such that $\vec{a}\in\zL_{\rho}$ and $\zL_{\rho}\models \forall x\,\exists y\,C(x,y,\vec{a})$.

In essence, admissible proof theory is a gathering of cut-elimination and collapsing techniques that can handle infinitary calculi of set theory with $\Sigma$ and/or $\Pi_2$ reflection rules, and thus lends itself to ordinal analyses of theories of the form **KP**+ “there are *x* many admissibles” or **KP**+ “there are many admissibles”.

A theory on the verge of admissible proof theory is **KPM**, designed to axiomatize essential features of a recursively Mahlo universe of sets. An admissible ordinal *κ* is said to be *recursively Mahlo* if it satisfies $\Pi_2$-reflection in the above sense but with the extra condition that the reflecting set $\zL_{\rho}$ be admissible as well. The ordinal representation (Rathjen 1990) for **KPM** is built on the assumption that there exists a (weakly) Mahlo cardinal. The novel feature over previous work is that there are two layers of collapsing functions. In all of the ordinal representation systems for admissible proof theory, collapsed ordinals $\psi_{\pi}(\alpha)$ are intrinsically singular, i.e., they can be approached from below by a definable sequence $(\beta_{\xi})_{\xi<\lambda}$ of ordinals $\beta_{\xi}$ with $\xi<\lambda< \psi_{\pi}(\alpha)$. In the representation system for **KPM** this is no longer the case. One needs a collapsing function $\psi_{\ssM}$ whose values $\psi_{\ssM}(\delta)$ are regular ordinals themselves, meaning that they are furnished with their own collapsing function $\xi\mapsto \psi_{\lower{.8ex}{\psi_{M} (\delta)}} (\xi)$. The ordinal analysis for **KPM** was carried out in Rathjen 1991. A different approach to **KPM** using ordinal diagrams is due to Arai (2003).

### D.2 Beyond admissible proof theory

Gentzen fostered hopes that with sufficiently large constructive ordinals one could establish the consistency of analysis, i.e., $\bZ_2$. The purpose of this section is to report on the next major step in analyzing fragments of $\bZ_2$. This is obviously the ordinal analysis of the system $(\bPi^1_2\Hy\bCA)$.[^note-55] The strength of $(\bPi^1_2\Hy\bCA)$ dwarfs that of $(\Delta^1_2\Hy\bCA)+\BI$. The treatment of $\Pi^1_2$-comprehension posed formidable technical challenges (see Rathjen 1995, 2005a,b). Other approaches to ordinal analysis of systems above $(\Delta^1_2\Hy\bCA)$ are due to Arai (2003, 2004) who uses ordinal diagrams and finite deductions.

The means of admissible proof theory are certainly too weak to deal with the next level of reflection having three alternations of quantifiers, i.e., $\Pi_3$-reflection.

Definition D.2 $\alpha>0$ is said to be $\Pi_n$-*reflecting* if $\zL_{\alpha} \models \Pi_n$-reflection. By $\Pi_n$-reflection we mean the scheme

$$ {C}\to \exists z [\iTran(z) \land z \not= \emptyset\land {C}^{z}],$$

where *C* is $\Pi_n$, $\iTran(z)$ expresses that *z* is a transitive set and $C^z$ is the formula resulting from *C* by restricting all unbounded quantifiers in *C* to *z*.

An ordinal representation, $\cT(\cK)$, for dealing with $\Pi_3$-reflection was developed in Rathjen 1994b, utilizing the notion of a weakly compact cardinal. That such a cardinal notion played a role is not a mere accident. Indeed, in Richter & Aczel 1973 the recursively large analogue of a weakly compact cardinal was equated with a $\Pi_3$-reflecting ordinal. The levels of collapsing functions in $\cT(\cK)$ now become transfinite. They mirror a transfinite hierarchy of Mahloness. Moreover, the proof-theoretic treatment of $\KP+\Pi_3\textrm{-Reflection}$ features a new technique for collapsing families of proofs, called “stationary collapsing”.

Climbing up in the hierarchy of $\Pi_n$-reflection, stronger cardinal notions are required to develop the pertaining representation systems. Another description of a weakly compact cardinal is that it is $\Pi^1_1$-indescribable. As a rule of thumb, one can develop a representation system sufficient for analyzing $\Pi_{n+3}$-reflection by making use of a $\Pi^1_n$-indescribable cardinals (see Rathjen 2005a). Already at that level things become very involved. At this point the reader might ask whether the theories with $\Pi_n$-reflection carry us anywhere near the level of $\Pi^1_2$-comprehension. The answer is, unfortunately, “no” by a wide margin. To make this more visible, we need a few more preparations. On the set-theoretic side, $\Pi^{1}_{2}$-comprehension corresponds to $\Sigma_1$-separation, i.e., the scheme of axioms

$$\exists z (z = \{ {x \in a} : \phi(x) \})$$

for all $\Sigma_1$-formulas *φ*. The precise relationship is as follows:

Theorem D.3 $\KP+ \Sigma_1$-separation and $(\Pi^{1}_{2}\Hy\bCA) + \BI$ prove the same sentences of second order arithmetic.

The ordinals *κ* such that $\zL_{\kappa} \models \KP+ \Sigma_1$-*Separation* are familiar from ordinal recursion theory.

Definition D.4 An admissible ordinal *κ* is said to be *nonprojectible* if there is no total *κ*-recursive function mapping *κ* one-one into some $\beta < \kappa$, where a function $g : \zL_{\kappa} \to \zL_{\kappa}$ is called *κ*-*recursive* if it is $\Sigma$ definable in $\zL_{\kappa}$.

The key to the “largeness” properties of nonprojectible ordinals is that for any nonprojectible ordinal *κ*, $\zL_{\kappa}$ is a limit of $\Sigma_1$-elementary substructures, i.e., for every $\beta< \kappa$ there exists a $\beta < \rho < \kappa$ such that $\zL_{\rho}$ is a $\Sigma_1$-elementary substructure of $\zL_{\kappa}$, written $\zL_{\rho}\prec_1 \zL_{\kappa}$.

Such ordinals satisfying $\zL_{\rho} \prec_{1} \zL_{\kappa}$ have strong reflecting properties. For instance, if $\zL_{\rho} \models {C}$ for some set-theoretic sentence *C* (containing parameters from $\zL_{\rho}$), then there exists a $\gamma < \rho$ such that $\zL_{\gamma} \models {C}$. This is because $\zL_{\rho} \models {C}$ implies $\zL_{\kappa} \models \exists \gamma\, {C}^{\zL_{\gamma}}$, hence $\zL_{\rho} \models \exists \gamma\, {C}^{\zL_{\gamma}}$ using $\zL_{\rho} \prec_{1} \zL_{\kappa}$.

The last result makes it clear that an ordinal analysis of $\Pi^{1}_{2}$-comprehension would necessarily involve a proof-theoretic treatment of reflections beyond those surfacing in admissible proof theory. The notion of stability will be instrumental.

Definition D.5 *α* is *δ*-*stable* if $\zL_{\alpha}{\prec_1}\zL_{\alpha+\delta}$.

For our purposes we need refinements of this notion, the simplest being provided by $\Pi_n$-reflection for all *n* which suffices to express one step in the $\prec_1$ relation; cf. Richter & Aczel 1973: 1.18.

Lemma D.6 $\zL_{\kappa}\prec_1\zL_{\kappa+1}$ iff *κ* is $\Pi_n$-reflecting for all *n*.

In the following, we will gradually slice $\Pi^1_2$-comprehension into degrees of reflection to achieve a sense of scale. A further refinement of the notion of *δ*-stability will be addressed next.

Definition D.7 *κ* is said to be *δ*-$\Pi_{n}$-reflecting if whenever ${C}(u,\vec{x})$ is a set-theoretic $\Pi_n$ formula, $a_1,\ldots,a_r{{\in}}\zL_{\kappa}$ and $\zL_{\kappa+\delta}\models {C}[\kappa,a_1,\ldots,a_n]$, then there exists $\kappa_0,\delta_0<\kappa$ such that $a_1,\ldots,a_r{{\in}}\zL_{\kappa_0}$ and $\zL_{\kappa_0+\delta_0}\models {C}[\kappa_0,a_1,\ldots,a_n]$. The notion of *κ* being *δ*-$\Sigma_{n}$-reflecting is defined in the same vein.

Putting the previous definition to work, one gets:

Corollary D.8 If *κ* is $\delta+1$-$\Sigma_{1}$-reflecting, then, for all *n*, *κ* is *δ*-$\Pi_{n}$-reflecting.

At this point let us return to proof theory to explain the need for even further refinements of the preceding notions. Recall that the first nonprojectible ordinal *ρ* is a limit of smaller ordinals $\rho_n$ such that $\zL_{\rho_n}\prec_1 \zL_{\rho}$. In the ordinal representation system for $({\Pi^1_2\Hy{\bCA}})$, there will be symbols ${\fE}_n$ and ${\fE}_{\omega}$ for $\rho_n$ and *ρ*, respectively. They are proof-theoretic analogues of cardinals with very high degrees of indescribability. They were called “reducible cardinals” in Rathjen 2005b.

The associated infinitary proof system will have rules

$$\tag{\(\iRef_{\Sigma(\zL_{\fE_n+\delta})}\)} \quad\quad\frac{\Gamma\Rightarrow \Delta, C(\vec{s})^{\zL_{\fE_n+\delta}}} {\Gamma \Rightarrow \Delta, (\exists z \in \zL_{\fE_n}) (\exists \vec{x} \in \zL_{\fE_n}) [\iTran(z) \land C(\vec{x})^{z}]}, $$

where ${C}(\vec{x})$ is a $\Sigma$ formula, $\vec{s}$ are set terms of levels $<{\fE}_n+\delta$, and $\delta<{\fE}_{\omega}$. These rules suffice to bring about the embedding $\KP+\Sigma_1$-Separation into the infinitary proof system, but other reflection rules galore will be needed to carry out cut-elimination. For example, there will be “many” ordinals in the pertaining representation system that play the role of *δ*-$\Pi_{n+1}$-reflecting ordinals by virtue of corresponding reflection rules in the infinitary calculus. The corresponding collapsing functions also have new features. Instead of collapsing a single ordinal they will have to collapse intervals. In that way they are reminiscent of inverses of elementary embeddings, with the latter being associated with very large cardinals in classical set theory.


## Notes（原文脚注，引自主文）

[^note-55]: 55\. For more background information see Takeuti 1985: 259; Feferman 1989: 362, and Pohlers 1991: 374.

### Notes to Appendix E