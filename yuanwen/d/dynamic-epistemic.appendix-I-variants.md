# dynamic-epistemic — appendix-I-variants（supplement）

> （《dynamic-epistemic》词条补充材料，源：plato.stanford.edu/entries/dynamic-epistemic/appendix-I-variants.html）

#### Supplement to Dynamic Epistemic Logic

## Appendix I: Variants of the action model approach to Dynamic Epistemic Logic

### 1. Graph modifier logics

Aucher et al. (2009) study highly expressive extensions of (ML) that contain modalities for performing the following Kripke model-transforming operations:

- add a new world that is disconnected from all others and at which all propositional letters are false;
- add a new world as above but then consider this new world to be the “actual” one (i.e., consider it the new point of evaluation);
- given a formula *F* and a letter *p*, change the valuation of *p* by making *p* true only at those non-*F* worlds where it was true before;
- given a formula *F* and a letter *p*, change the valuation of *p* by making *p* true both where it was before and at all *F*-worlds;
- for an agent *a* and formulas *G* and $G'$, remove all *a*-arrows in the model whose source is a *G*-world and whose target is a $G'$-world; and
- for an agent *a* and formulas *G* and $G'$, add an *a*-arrow from every *G*-world to every $G'$-world.

Based on a language that extends (ML) with a universal modality, a modal operator for each of the operations listed above, and Propositional Dynamic Logic-style sequential combinations of these modalities (with test), Aucher et al. (2009) define a sound and complete logic $\GML$ of global graph modifiers. This logic extends public announcement logic. Aucher et al. (2009) also study a variant of $\GML$ that restricts the valuation-change operations so that only the valuation of the “actual world” (i.e., the point of evaluation) changes; this has natural connections with hybrid logic and is related to the work on local state assignment by Renardel de Lavalette (2004). Nevertheless, the exact connection between the Aucher et al. (2009) graph modification operations and action model-induced transformations is unknown.

Graph modifier logics may be considered part of the family of works that have grown out of van Benthem's (2005) “sabotage logic”. Other examples in this family include van Eijck and Wang (2008), Areces, Fervari, and Hoffmann (2012), and Fervari (2014).

### 2. Generalized Arrow Update Logic

Generalized Arrow Update Logic (Kooi and Renne 2011b) is a variant of Arrow Update Logic (see Appendix E) that drops the assumption that arrow updates are common knowledge. This is achieved using a product update-like operation based on the basic arrow update language (AUL) (see Appendix E). In addition to providing a complete axiomatization (based on reduction axioms to (ML)), Kooi and Renne (2011b) study the *update expressivity* of generalized arrow updates with respect to action models. Note that this notion of *update expressivity* is very different from the notion of *language expressivity*. In particular, update expressivity is concerned with identifying the Kripke model-transforming functions can be described using the model-changing modalities of the language (e.g., the generalized arrow updates or the action models). Contrast this with language expressivity, which is concerned with identifying the propositions (here meaning “sets of worlds”) that are definable using a formula of the language. Kooi and Renne (2011b) show that both the language (EAL) of Epistemic Action Logic (i.e., the logic of action models) and the language (GAUL) of Generalized Arrow Update Logic are equally language expressive and equally update expressive. However, (GAUL) may have some advantages:

- there exist generalized arrow updates whose smallest update-equivalent action models are exponentially larger; and
- generalized arrow updates are at worst poly-exponentially less succinct than action models, though this improves to being at worst polynomially less succinct if the action models have preconditions in (ML) or if generalized arrow updates are allowed to have target conditions in (EAL).

Therefore, if we restrict preconditions to (ML) or extend (GAUL) so as to allow (EAL)-formulas in target conditions—neither of which affects update expressivity because (ML), (EAL), and (GAUL) are all equally language expressive—then generalized arrow updates are exponentially more succinct than action models.

Kooi and Renne (2011a) study a relativized common knowledge-style extension of the basic arrow update language (AUL); however, this extension has not yet been brought to the generalized language (GAUL). Finally, we mention that it seems as though the arrow-deletion operations of (AUL) ought to have some natural connection with the arrow-deletion operations in the graph modifier logics of Aucher et al. (2009). However, the connection is not obvious because arrow updates of (AUL) retain arrows that simultaneously satisfy a number of arrow specifications, whereas the graph modifier operations only call for satisfaction of what is essentially a single arrow specification. It may be possible to overcome this restriction, perhaps by addition of a Propositional Dynamic Logic-like union operation, but this has yet to be investigated.

### 3. Logic of Communication and Change

Van Benthem, van Eijck, and Kooi (2006) introduced $\LCC$, the Logic of Communication and Change, as a Propositional Dynamic Logic-like language that incorporates action models with substitution (see Appendix G). The language \eqref{LCC} of the Logic of Communication and Change and the set $\AM(\LCC)_*$ of pointed action models with substitution having preconditions in the language \eqref{LCC} are together defined by the following recursive grammar:

$$\begin{align*}\taglabel{LCC} F & \ccoloneqq p \mid F\land F \mid \lnot F \mid [\pi]F \mid [A,e]F \\ \pi & \ccoloneqq a \mid {?}F \mid \pi;\pi \mid \pi\cup\pi \mid \pi* \\ & \quad \small p\in\sP,\; a\in\sA,\; (A,e)\in\AM(\LCC)_* \end{align*}$$

Expressions made using the start symbol *F* are called *formulas*, and expressions made using the start symbol $\pi$ are called *programs*. The sublanguage (EPDL) of “Epistemic Propositional Dynamic Logic” is defined by disallowing formation of action model formulas $[A,e]F$ in the grammar for \eqref{LCC}. The semantics of this language is given as follows.

- $M,w\models p$ holds if and only if $w\in V(p)$.
- $M,w\models F\land G$ holds if and only if $M,w\models F$ and $M,w\models G$.
- $M,w\models \lnot F$ holds if and only if $M,w\not\models F$.
- $M,w\models[\pi]F$ holds if and only if $M,v\models F$ for each *v* such that $w\sem{\pi}v$.
- $M,w\models[A,e]F$ holds if and only if $M,w\not\models\pre^A(e)$ or $M[A],(w,e)\models F$, where $M[A]$ is defined by the BMS product update (Baltag, Moss, and Solecki 1998).
- $x\sem{a}y$ holds if and only if $x R_a y$.
- $x\sem{{?}F}y$ holds if and only if $x=y$ and $M,w\models F$.
- $x\sem{\pi_1;\pi_2}y$ holds if and only if there exists *z* such that $x\sem{\pi_1}z$ and $z\sem{\pi_2}y$.
- $x\sem{\pi_1\cup\pi_2}y$ holds if and only if $x\sem{\pi_1}y$ or $x\sem{\pi_2}y$.
- $x\sem{\pi*}y$ holds if and only if $x(\sem{\pi}^*)y$ holds, where $\sem{\pi}^*$ is the reflexive-transitive closure of $\sem{\pi}$.

Van Benthem, van Eijck, and Kooi (2006) provide a sound and complete axiomatization for the logic $\LCC$ consisting of the validities of \eqref{LCC}. Completeness is via reduction to (EPDL). The authors also show that the language is highly expressive, including in particular relativized common knowledge among a group $\{a_1,\dots,a_n\}$ via the program

$$ (a_1\cup\cdots\cup a_n)*. $$

We refer the reader to van Benthem, van Eijck, and Kooi (2006) for details.

Van Eijck and Wang (2008) consider an extension of $\LCC$ that allows converses of agent programs *a* and apply this to consensus seeking in Dutch plenary meetings. Van Eijck (2008b) and van Eijck and Wang (2008) consider a further extension that allows for *relational change* operators; these are similar to valuation changes except that programs are used to describe Kripke model transformations that include changes in agents’ relations $R_a$ in the model. These extensions, which are extremely expressive, are applied to the study of Belief Revision in a DEL-style framework.

### 4. General Dynamic Dynamic Logic

Girard, Seligman, and Liu (2012) propose General Dynamic Dynamic Logic $\mathsf{GDDL}$, a Propositional Dynamic Logic-style language that has complex action model-like modalities that themselves contain Propositional Dynamic Logic-style instructions. The basic idea, following van Benthem and Liu (2007) and Liu (2008), is to describe relation changes using programs but then use additional “higher level” programs to describe how the “lower level” programs are to interact. The framework is mathematically complicated, so we refer the reader to Girard, Seligman, and Liu (2012) for details. We note that Girard, Seligman, and Liu (2012) argue that $\mathsf{GDDL}$ has model-transforming updates that are sufficiently expressive to express all model-changing transformations of action models, Generalized Arrow Update Logic, or $\LCC$. However, it has not been proved whether this result is strict (i.e., whether all $\mathsf{GDDL}$-transformations are expressible using, e.g., $\LCC$). Seligman, Liu, and Girard (2011, 2013) apply $\GDDL$ to a logic of “friendship” (a certain notion of social connectivity) in social networks.

← beginning of main article
