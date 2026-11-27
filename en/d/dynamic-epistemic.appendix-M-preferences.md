# dynamic-epistemic — appendix-M-preferences（supplement）

> （《dynamic-epistemic》词条补充材料，源：plato.stanford.edu/entries/dynamic-epistemic/appendix-M-preferences.html）

#### Supplement to Dynamic Epistemic Logic

## Appendix M: Preference dynamics

DEL-style model-changing operators have been applied by a number of researchers to the study of preferences, preference change, and related notions. At the semantic core of the various DEL approaches to reasoning about preference and preference change is some variant of the *preference model*.

**Preference model.** Given a nonempty set $\sP$ of propositional letters and a finite nonempty set $\sA$ of agents, a *preference model* is a structure

$$ M=(W,\succeq,V) $$

consisting of a nonempty set *W* of *worlds* identifying the possible states of affairs that might obtain, a function $\succeq$ that assigns to each agent *a* a reflexive and transitive binary relation$\succeq_a$ on *W*, and a *propositional valuation* *V* mapping each propositional letter to the set of worlds at which that letter is true. A *pointed preference model*, sometimes called a *scenario* or a *situation*, is a pair $(M,w)$ consisting of a preference model *M* and a world *w* (called the *point*) that designates the state of affairs that we (the formal modelers) currently assume to be actual.

A preference model is just like a plausibility model except that the order $\succeq_a$ need not satisfy the property of *Plausibility*; in particular, within each nonempty set of worlds, there need not always exist a nonempty subset consisting of the “most preferred” worlds. The expression $w\succeq_a v$ is read, “agent *a* considers *w* to be at least as preferred as *v*”.

Note that the convention here is that the “larger” worlds according to $\succeq_a$ are more preferred; this is the opposite of the convention adopted for plausibility models. The converse preferential relation $\preceq_a$, the strict preferential relations $\succ_a$ and $\prec_a$, and the equi-preferential relation $\simeq_a$ are defined in terms of $\succeq_a$ in a manner analogous to our definitions of converse plausibility, strict plausibility, strict converse plausibility, and equi-plausibility in the definition of plausibility models.

Van Benthem et al. (2009) consider a single-agent version of a reflexive and irreflexive preference language we call \\eqref{RIPL}. This language consists of a universal modality $[\forall]$ (“true at all worlds in the model”), a reflexive preference modality $[\succeq_a]$ (“true at the worlds non-strictly less preferred by *a*”), the converse reflexive preference modality $[\preceq_a]$ (“true at the worlds non-strictly preferred by *a*”), an irreflexive preference modality $[\succ_a]$ (“true at the worlds strictly less preferred by *a*”), and the converse irreflexive preference modality $[\prec_a]$ (“true at the worlds strictly preferred by *a*”).

$$\begin{align*} \taglabel{RIPL} F \ccoloneqq &p \mid F\land F \mid \lnot F \mid [\forall F] \,\mid \\ &[\succeq_a]F \mid [\preceq_a]F \mid [\succ_a]F \mid [\prec_a]F \\ &\small p\in\sP,\; a\in\sA \end{align*}$$

We recall that the dual existential modality $[\exists]$ is defined by $[\exists]F\coloneqq\lnot[\forall]\lnot F$. The dual modalities for the preference relation, which are written between angled brackets, are defined similarly; for example, $\may{\succeq_a}F\coloneqq\lnot[\succeq_a]\lnot F$. The language \\eqref{RIPL} is interpreted over pointed preference models as follows.

- $M,w\models p$ holds if and only if $w\in V(p)$.
- $M,w\models F\land G$ holds if and only if both $M,w\models F$ and $M,w\models G$.
- $M,w\models\lnot F$ holds if and only if $M,w\not\models F$.
- $M,w\models[\forall]F$ holds if and only if $M,v\models F$ for each $v\in W$.
- $M,w\models[\succeq_a]F$ holds if and only if $M,v\models F$ for each $v\succeq_a w$.
- $M,w\models[\preceq_a]F$ holds if and only if $M,v\models F$ for each $v\preceq_a w$.
- $M,w\models[\succ_a]F$ holds if and only if $M,v\models F$ for each $v\succ_a w$.
- $M,w\models[\prec_a]F$ holds if and only if $M,v\models F$ for each $v\prec_a w$.

Van Benthem et al. (2009) show that \\eqref{RIPL} allows us to express eight distinct notions of “agent *a* prefers *G* to *F*”. A number of these notions arise in choosing best moves in a game-theoretic setting (van Benthem 2009).

**Theorem (van Benthem et al. 2009).** Let $(M,w)$ be a pointed preference model.

1. Define $M,w\models F\leq_a^{\exists\exists} G$ to mean that $\exists x, \exists y \succeq_a x:$ ($M,x\models F$ and $M,y\models G$). “There is an *F*-world that agent *a* non-strictly prefers to some *G*-world.” The formula $[\exists](F\land\may{\preceq_a}G)$ is equivalent to $F\leq_a^{\exists\exists} G$.
2. Define $M,w\models F\leq_a^{\forall\exists} G$ to mean that $\forall x, \exists y \succeq_a x:$ ($M,x\models F$ implies $M,y\models G$). “For every *F*-world, there is a *G*-world that agent *a* non-strictly prefers.” The formula $[\forall](F\to\may{\preceq_a} G)$ is equivalent to $F\leq_a^{\forall\exists} G$.
3. Define $M,w\models F\lt_a^{\exists\exists} G$ to mean that $\exists x, \exists y \succ_a x:$ ($M,x\models F$ and $M,y\models G$). “There is an *F*-world that agent *a* strictly prefers to some *G*-world.” The formula $[\exists](F\land\may{\prec_a}G)$ is equivalent to $F\lt_a^{\exists\exists} G$.
4. Define $M,w\models F\lt_a^{\forall\exists} G$ to mean that $\forall x, \exists y :$ (if $M,x\models F$, then $M,y\models G$ and $y\succ_a x$). “For every *F*-world, there is a *G*-world that agent *a* strictly prefers.” The formula $[\forall](F\to\may{\prec_a} G)$ is equivalent to $F\lt_a^{\forall\exists} G$.
5. Define $M,w\models F\lt_a^{\forall\forall} G$ to mean that $\forall x, \forall y :$ (if $M,x\models F$ and $M,y\models G$, then $x\prec_a y$). “Agent *a* strictly prefers every *G*-world to every *F*-world.” If the preference ordering $\succeq_a$ is total (see [Appendix C](dynamic-epistemic.appendix-C-relations.md)), then $[\forall](G\to[\preceq_a]\lnot F)$ is equivalent to $F\lt_a^{\forall\forall} G$.
6. Define $M,w\models G\gt_a^{\exists\forall} F$ to mean that $\exists y, \forall x :$ (if $M,x\models F$ and $M,y\models G$, then $x\prec_a y$). “There is a *G*-world that agent *a* strictly prefers to every *F*-world.” If the preference ordering $\succeq_a$ is total, then $[\exists](G\land[\preceq_a]\lnot F)$ is equivalent to $G\gt_a^{\exists\forall} F$.
7. Define $M,w\models F\leq_a^{\forall\forall} G$ to mean that $\forall x, \forall y :$ (if $M,x\models F$ and $M,y\models G$, then $x\preceq_a y$). “Agent *a* non-strictly prefers every *G*-world to every *F*-world.” If the preference ordering $\succeq_a$ is total, then $[\forall](G\to[\prec_a]\lnot F)$ is equivalent to $F\leq_a^{\forall\forall} G$.
8. Define $M,w\models G\geq_a^{\exists\forall} F$ to mean that $\exists y, \forall x :$ (if $M,x\models F$ and $M,y\models G$, then $x\preceq_a y$). “There is a *G*-world that agent *a* non-strictly prefers to every *F*-world.” If the preference ordering $\succeq_a$ is total, then $[\exists](G\land[\prec_a]\lnot F)$ is equivalent to $G\geq_a^{\exists\forall} F$.

To consider multi-agent preferences in conjunction with multi-agent knowledge, and to allow for DEL-style changes in preferences and knowledge, van Benthem and Liu (2007) study preference models to which epistemic relations $R_a$ are added for each agent *a*.

**Epistemic preference model.** Given a nonempty set $\sP$ of propositional letters and a finite nonempty set $\sA$ of agents, an *epistemic preference model* is a structure $$ M=(W,\succeq,R,V) $$ consisting of a nonempty set *W* of *worlds* identifying the possible states of affairs that might obtain, a function $\succeq$ that assigns to each agent $a\in\sA$ a reflexive and transitive binary relation ${\succeq_a}$ on *W*, a function *R* that assigns a binary equivalence relation $R_a$ on *W* to each agent $a\in\sA$, and a *propositional valuation* *V* mapping each propositional letter to the set of worlds at which that letter is true. A *pointed epistemic preference model*, sometimes called a *scenario* or a *situation*, is a pair $(M,w)$ consisting of an epistemic preference model *M* and a world *w* (called the *point*) that designates the state of affairs that we (the formal modelers) currently assume to be actual.

We note that van Benthem and Liu (2007) define epistemic preference models so that each $R_a$ is an equivalence relation. This is because they wish to adopt the standard logic of knowledge (multi-agent $\mathsf{S5}$) and assign formulas $[a]F$ an epistemic reading (“agent *a* knows *F*”). This restriction that the $R_a$’s be equivalence relations is not a technical necessity and could easily be varied if other normal modal logics for the modalities $[a]$ are desired.

Van Benthem and Liu (2007) define the single-agent dynamic epistemic preference language \\eqref{DEPL} that makes use of a universal modality, reflexive preference formulas $[\preceq_a]F$ (“agent *a* prefers *F*”) for each agent *a*, a knowledge modality $[a]F$ (“agent *a* knows *F*”) for each agent *a*, “link-cutting” public announcement formulas $[F!']G$ (“after the announcement of *F*, formula *G* is true”), and “preference upgrade” formulas $[\sharp F]G$ (“after eliminating preferences for $\lnot F$-worlds over *F*-worlds, *G* is true”). Here we consider a simple multi-agent extension.

$$\begin{align*} \taglabel{DEPL} F \ccoloneqq &p \mid F\land F \mid \lnot F \mid [a]F \,\mid \\ &[\forall]F \mid [\preceq_a]F \mid [F!']F \mid [\sharp F]F \\ &\small p\in\sP,\; a\in\sA \end{align*}$$

Formulas of this language are interpreted at pointed epistemic preference models using the appropriate clauses from \\eqref{RIPL} and from (ML) along with the following clauses:

- $M,w\models[a]F$ holds if and only if $M,v\models F$ for each *v* satisfying $wR_av$.
- $M,w\models[F!']G$ holds if and only if we have that $M[F!'],w\models G$, where the model $$ M[F!']=(W[F!'],{\succeq}[F!'],R[F!'],V[F!']) $$ is defined by:
- $W[F!'] \coloneqq W$ — retain all worlds,
- $x{\succeq}[F!']_a y$ if and only if $x\succeq_a y$ — leave preferences as before,
- $xR[F!']_ay$ if and only if $xR_ay$ and we have $M,x\models F$ if and only if $M,y\models F$ — delete only those epistemic connections between *F*-worlds and $\lnot F$-worlds, and
- $v\in V[F!'](p)$ holds if and only if $v\in V(p)$ — leave the valuation the same at all worlds.
- $M,w\models[\sharp F]G$ holds if and only if we have that $M[\sharp F],w\models G$, where the model $$ M[\sharp F]=(W[\sharp F],{\succeq}[\sharp F],R[\sharp F],V[\sharp F]) $$ is defined by:
- $W[\sharp F]\coloneqq W$ — retain all worlds,
- $x{\succeq}[\sharp F]_ay$ if and only if $x\succeq_a y$ and it is not the case that both $M,w\not\models F$ and $M,y\models F$ — delete only those preferences for $\lnot F$-worlds over *F*-worlds,
- $x R[\sharp F]_ay$ if and only if $x R_a y$ — leave epistemic relations as before, and
- $v\in V[\sharp F](p)$ if and only if $v\in V(p)$ — leave the valuation the same at all worlds.

Van Benthem and Liu (2007) axiomatize the \\eqref{DEPL}-validities and call the resulting logic Dynamic Epistemic Upgrade Logic $\DEUL$.

**The axiomatic theory $\DEUL$.**

- Axiom schemes and rules for classical propositional logic
- $\mathsf{S5}$ axiom schemes and rules for $[a]$
- $\mathsf{S4}$ axiom schemes and rules for $[\preceq_a]$
- Universal modality axioms:
- $\mathsf{S5}$ axiom schemes and rules for $[\forall]$
- $[\forall]F\to[a]F$
- $[\forall]F\to[\preceq_a]F$
- Link-cutting public announcements:
- $[F!']p\leftrightarrow(F\to p)$ for letters $p\in\sP$ “After a false announcement, every letter holds—a contradiction. After a true announcement, letters retain their truth values.”
- $[F!'](G\land H)\leftrightarrow([F!']G\land[F!']H)$ “A conjunction is true after an announcement iff each conjunct is.”
- $[F!']\lnot G\leftrightarrow(F\to\lnot[F!']G)$ “*G* is false after an announcement iff the announcement, whenever truthful, does not make *G* true.”
- $[F!'][a]G\leftrightarrow(F\to[a][F!']G)$ “*a* knows *G* after an announcement iff the announcement, whenever truthful, is known by *a* to make *G* true.”
- $[F!'][\preceq_a]G\leftrightarrow(F\to[\preceq_a][F!']G)$ “*a* prefers *G* after an announcement iff *a* prefers that *G* is true after the announcement is truthfully made.”
- $[F!'][\forall]G\leftrightarrow (F\to[\forall]([F!']G\land[\lnot F!']G))$ “*G* is true everywhere after an announcement of *F* iff whenever *F* is true, it is true everywhere that both the announcement of *F* and the announcement of its negation makes *G* true.”
- Link-Cutting Announcement Necessitation Rule: from *F*, infer $[G!']F$. “A validity holds after any announcement.”
- Preference upgrades:
- $[\sharp F]p\leftrightarrow p$ for letters $p\in\sP$ “*p* holds after an upgrade iff *p* held before the upgrade.”
- $[\sharp F](G\land H)\leftrightarrow ([\sharp F]G\land[\sharp F]H)$ “A conjunction is true after an upgrade iff each conjunct is.”
- $[\sharp F]\lnot G\leftrightarrow\lnot[\sharp F]G$ “A negation is true after an upgrade iff it is false before the upgrade.”
- $[\sharp F][a]G\leftrightarrow[a][\sharp F]G$ “*a* knows *G* after an upgrade iff the upgrade is known by *a* to make *G* true.”
- $[\sharp F][\preceq_a]G\leftrightarrow ([\preceq_a](F\to[\sharp F]G)\land (\lnot F\to[\preceq_a][\sharp F]G))$ “*a* prefers *G* after an upgrade by *F* iff *a* prefers that ‘the upgrade by *F* make *G* true at *F*-worlds,’ and, in case *F* is false, *a* also prefers that the upgrade of *F* make *G* true.”
- $[\sharp F][\forall]G\leftrightarrow[\forall][\sharp F]G$ “*G* is true everywhere after an upgrade of *F* iff it is true everywhere that the upgrade makes *G* true.”
- Preference Upgrade Necessitation Rule: from *F*, infer $[\sharp G]F$. “A validity holds after any upgrade.”

**$\DEUL$ Soundness and Completeness (van Benthem and Liu 2007).** $\DEUL$ is sound and complete with respect to the collection $\sC_*$ of pointed epistemic preference models. That is, for each \\eqref{DEPL}-formula *F*, we have that $\DEUL\vdash F$ if and only if $\sC_*\models F$.

The work of van Benthem and Liu (2007) has been further developed by a number of authors. Liu (2008) looks at a quantitative version of preference and preference change closely related to earlier work on belief revision by Aucher (2003). Yamada (2007a,b, 2008) examines various deontic logics of action, command, and obligation. Van Eijck (2008) looks at a generalized Propositional Dynamic Logic-style preference logic that encompasses van Benthem and Liu (2007) and allows for the study of common knowledge (or belief) along with a DEL-style notion of conditional belief and belief change. Van Eijck and Sietsma (2010) further extend this work, examining applications to judgment aggregation; this has natural connections with coalition logic and social choice theory. Van Benthem, Girard, and Roy (2009c) examine a preference logic for von Wright’s (1963) notion of *ceteris paribus* (in the distinct senses of “all things being normal” and of “all things being equal”) along with a dynamic notion of “agenda change”. A textbook on preferences and preference dynamics is Liu (2011).

← beginning of main article
