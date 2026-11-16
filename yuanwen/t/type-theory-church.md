# Church’s Type Theory
**First published Fri Aug 25, 2006; substantive revision Tue Jan 16, 2024**

*Benzmüller, Christoph, Andrews, Peter*

Church’s type theory, aka simple type theory, is a formal logical language which includes classical first-order and propositional logic, but is more expressive in a practical sense. It is used, with some modifications and enhancements, in most modern applications of type theory. It is particularly well suited to the formalization of mathematics and other disciplines and to specifying and verifying hardware and software. It also plays an important role in the study of the formal semantics of natural language. And in particular, when used as a metalogic to semantically embed expressive (quantified) non-classical logics, it enables further topical applications in artificial intelligence and philosophy.

A great wealth of technical knowledge can be expressed very naturally in it. With possible enhancements, Church’s type theory constitutes an excellent formal language for representing the knowledge in automated information systems, sophisticated automated reasoning systems, systems for verifying the correctness of mathematical proofs, and a range of projects involving logic and artificial intelligence. Some examples and further references are given in Sections 1.2.2 and 5 below.

Type theories are also called higher-order logics, since they allow quantification not only over individual variables (as in first-order logic), but also over function, predicate, and even higher-order variables. Type theories characteristically assign types to entities, distinguishing, for example, between numbers, sets of numbers, functions from numbers to sets of numbers, and sets of such functions. As illustrated in Section 1.2.2 below, these distinctions allow one to discuss the conceptually rich world of sets and functions without encountering the paradoxes of naive set theory.

Church’s type theory is a formulation of type theory that was introduced by Alonzo Church in Church 1940. In certain respects, it is simpler and more general than the type theory introduced by Bertrand Russell in Russell 1908 and Whitehead & Russell 1927a. Since properties and relations can be regarded as functions from entities to truth values, the concept of a function is taken as primitive in Church’s type theory, and the λ-notation which Church introduced in Church 1932 and Church 1941 is incorporated into the formal language. Moreover, quantifiers and description operators are introduced in a way so that additional binding mechanisms can be avoided, λ-notation is reused instead. λ-notation is thus the only binding mechanism employed in Church’s type theory.

## 1. Syntax

### 1.1 Fundamental Ideas

We start with an informal description of the fundamental ideas underlying the syntax of Church’s formulation of type theory.

All entities have types, and if α and β are types, the type of functions from elements of type β to elements of type α is written as $(\alpha \beta)$. (This notation was introduced by Church, but some authors write $(\beta \rightarrow \alpha)$ instead of $(\alpha \beta)$. See, for example, Section 2 of the entry on type theory.)

As noted by Schönfinkel (1924)[^schönfinkel-1924], functions of more than one argument can be represented in terms of functions of one argument when the values of these functions can themselves be functions. For example, if $F$ is a function of two arguments, for each element $x$ of the left domain of $F$ there is a function $g$ (depending on $x$) such that $gy=Fxy$ for each element $y$ of the right domain of $F$. While we may thus regard $F$ as a function of a single argument $x$ that returns a function $g(y)$, we should (more accurately) view $g$ as the value of a new function $f$ (related to $F$) such that $g=fx$. The new $f$ is a function of a single argument, whose value for any argument $x$ in its domain is a function $fx$, whose value (in turn) for any argument $y$ in its domain is $Fxy$.

For a more explicit example, consider the function + which carries any pair of natural numbers to their sum. We may denote this function by $+_{((\sigma \sigma)\sigma)}$, where *σ* is the type of natural numbers. Given any number $x$, $[+_{((\sigma \sigma)\sigma)}x]$ is the function which, when applied to any number $y$, gives the value $[[+_{((\sigma \sigma)\sigma)}x]y]$, which is ordinarily abbreviated as $x + y$. Thus $[+_{((\sigma \sigma)\sigma)}x]$ is the function of one argument which adds $x$ to any number. When we think of $+_{((\sigma \sigma)\sigma)}$ as a function of one argument, we see that it maps any number $x$ to the function $[+_{((\sigma \sigma)\sigma)}x]$.

More generally, if $f$ is a function which maps *n*-tuples $\langle w_{\beta},x_{\gamma},\ldots ,y_{\delta},z_{\tau}\rangle$ of elements of types *β*, *γ*,…, *δ* ,*τ*, respectively, to elements of type α, we may assign to $f$ the type $((\ldots((\alpha \tau)\delta)\ldots \gamma)\beta)$. It is customary to use the convention of association to the left to omit parentheses, and write this type symbol simply as $(\alpha \tau \delta \ldots \gamma \beta)$.

A set or property can be represented by a function (often called *characteristic function*) which maps elements to truth values, so that an element is in the set, or has the property, in question iff the function representing the set or property maps that element to truth. When a statement is asserted, the speaker means that it is true, so that $s x$ means that $s x$ is true, which also expresses the assertions that *s* maps $x$ to truth and that $x \in s$. In other words, $x \in s$ iff $s x$. We take ${o}$ as the type symbol denoting the type of truth values, so we may speak of any function of type $({o}\alpha)$ as a *set* of elements of type α. A function of type $(({o}\alpha)\beta)$ is a binary relation between elements of type β and elements of type α. For example, if *σ* is the type of the natural numbers, and $<$ is the order relation between natural numbers, $<$ has type $({o}\sigma \sigma)$, and for all natural numbers $x$ and $y, {<}x y$ (which we ordinarily write as $x < y)$ has the value truth iff $x$ is less than $y$. Of course, $<$ can also be regarded as the function which maps each natural number $x$ to the set $<x$ of all natural numbers $y$ such that $x$ is less than $y$. Thus sets, properties, and relations may be regarded as particular kinds of functions. Church’s type type theory is thus a logic of functions, and, in this sense, it is in the tradition of the work of Frege’s *Begriffsschrift*. The opposite approach would be to reduce functions to relations, which was the approach taken by Whitehead and Russell (1927a) in the *Principia Mathematica*.

Expressions which denote elements of type α are called *well-formed formulas (wffs) of type* α. Thus, statements of type theory are wffs of type ${o}$.

If $\bA_{\alpha}$ is a wff of type α in which $\bu_{\alpha \beta}$ is not free, the function (associated with) $\bu_{\alpha \beta}$ such that $\forall \bv_{\beta}[\bu_{\alpha \beta}\bv_{\beta} = \bA_{\alpha}]$ is denoted by $[\lambda \bv_{\beta}\bA_{\alpha}]$. Thus $\lambda \bv_{\beta}$ is a variable-binder, like $\forall \bv_{\beta}$ or $\exists \bv_{\beta}$ (but with a quite different meaning, of course); λ is known as an *abstraction operator*. $[\lambda \bv_{\beta}\bA_{\alpha}]$ denotes the function whose value on any argument $\bv_{\beta}$ is $\bA_{\alpha}$, where $\bv_{\beta}$ may occur free in $\bA_{\alpha}$. For example, $[\lambda n_{\sigma}[4\cdot n_{\sigma}+3]]$ denotes the function whose value on any natural number *n* is $4\cdot n+3$. Hence, when we apply this function to the number 5 we obtain $[\lambda n_{\sigma}[4\cdot n_{\sigma}+3]]5 = 4\cdot 5+3 = 23$.

We use $\textsf{Sub}(\bB,\bv,\bA)$ as a notation for the result of substituting $\bB$ for $\bv$ in $\bA$, and $\textsf{SubFree}(\bB,\bv,\bA)$ as a notation for the result of substituting $\bB$ for all free occurrences of $\bv$ in $\bA$. The process of replacing $[\lambda \bv_{\beta}\bA_{\alpha}]\bB_{\beta}$ by $\textsf{SubFree}(\bB_{\beta},\bv_{\beta},\bA_{\alpha})$ (or vice-versa) is known as β-*conversion*, which is one form of λ-*conversion*. Of course, when $\bA_{{o}}$ is a wff of type ${o}$, $[\lambda \bv_{\beta}\bA_{{o}}]$ denotes the set of all elements $\bv_{\beta}$ (of type $\beta)$ of which $\bA_{{o}}$ is true; this set may also be denoted by $\{\bv_{\beta}|\bA_{{o}}\}$. For example, $[\lambda x\ x<y]$ denotes the set of $x$ such that $x$ is less than $y$ (as well as that property which a number $x$ has if it is less than $y$). In familiar set-theoretic notation,

$$[\lambda \bv_{\beta} \bA_{{o}}]\bB_{\beta} = \textsf{SubFree}(\bB_{\beta},\bv_{\beta},\bA_{{o}})$$

would be written

$$\bB_{\beta} \in \{\bv_{\beta}|\bA_{{o}}\} \equiv \textsf{SubFree}(\bB_{\beta},\bv_{\beta},\bA_{{o}}).$$

(By the Axiom of Extensionality for truth values, when $\bC_{{o}}$ and $\bD_{{o}}$ are of type ${o}, \bC_{{o}} \equiv \bD_{{o}}$ is equivalent to $\bC_{{o}} = \bD_{{o}}$.)

Propositional connectives and quantifiers can be assigned types and can be denoted by constants of these types. The negation function maps truth values to truth values, so it has type $({o}{o})$. Similarly, disjunction and conjunction (etc.) are binary functions from truth values to truth values, so they have type $({o}{o}{o})$.

The statement $\forall \bx_{\alpha}\bA_{{o}}$ is true iff the set $[\lambda \bx_{\alpha}\bA_{{o}}]$ contains all elements of type α. A constant $\Pi_{{o}({o}\alpha)}$ can be introduced (for each type symbol $\alpha)$ to denote a property of sets: a set $s_{{o}\alpha}$ has the property $\Pi_{{o}({o}\alpha)}$ iff $s_{{o}\alpha}$ contains all elements of type α. With this interpretation

$$ \forall s_{{o}\alpha}\left[\Pi_{{o}({o}\alpha)}s_{{o}\alpha} \equiv \forall x_{\alpha}\left[s_{{o}\alpha}x_{\alpha}\right]\right] $$

should be true, as well as

$$ \Pi_{{o}({o}\alpha)}[\lambda \bx_{\alpha}\bA_{{o}}] \equiv \forall \bx_{\alpha}[[\lambda \bx_{\alpha}\bA_{{o}}]\bx_{\alpha}] \label{eqPi} $$

for any wff $\bA_{{o}}$ and variable $\bx_{\alpha}$. Since by λ-conversion we have

$$ [\lambda \bx_{\alpha}\bA_{{o}}]\bx_{\alpha} \equiv \bA_{{o}} $$

this equation can be written more simply as

$$ \Pi_{{o}({o}\alpha)}[\lambda \bx_{\alpha}\bA_{{o}}] \equiv \forall \bx_{\alpha}\bA_{{o}} $$

Thus, $\forall \bx_{\alpha}$ can be defined in terms of $\Pi_{{o}({o}\alpha)}$, and λ is the only variable-binder that is needed.

### 1.2 Formulas (as certain terms)

Before we state the definition of a “formula”, a word of caution is in order. The reader may be accustomed to thinking of a formula as an expression which plays the role of an assertion in a formal language, and of a term as an expression which designates an object. Church’s terminology is somewhat different, and provides a uniform way of discussing expressions of many different types. What we call well-formed formula of type α ($\text{wff}_{\alpha}$) below would in more standard terminology be called *term* of type α, and then only certain terms, namely those with type ${o}$, would be called formulas. Anyhow, in this entry we have decided to stay with Church’s original terminology. Another remark concerns the use of some specific mathematical notation. In what follows, the entry distinguishes between the symbols $\imath$, $\iota_{(\alpha({o}\alpha))}$, and $\atoi$. The first is the symbol used for the type of individuals; the second is the symbol used for a logical constant (see Section 1.2.1 below); the third is the symbol used as a variable-binding operator that represents the definite description “the” (see Section 1.3.4). The reader should not confuse them and check to see that the browser is displaying these symbols correctly.

#### 1.2.1 Definitions

*Type symbols* are defined inductively as follows:

- $\imath$ is a type symbol (denoting the type of individuals). There may also be additional primitive type symbols which are used in formalizing disciplines where it is natural to have several sorts of individuals.
- ${o}$ is a type symbol (denoting the type of truth values).
- If α and β are type symbols, then $(\alpha \beta)$ is a type symbol (denoting the type of functions from elements of type β to elements of type α).

The *primitive symbols* are the following:

- Improper symbols: [, ], *λ*
- For each type symbol α, a denumerable list of *variables* of type $\alpha : a_{\alpha}, b_{\alpha}, c_{\alpha}\ldots$
- Logical constants: $\nsim_{({o}{o})}$, $\lor_{(({o}{o}){o})}$, $\Pi_{({o}({o}\alpha))}$ and $\iota_{(\alpha({o}\alpha))}$ (for each type symbol α). The types of these constants are indicated by their subscripts. The symbol $\nsim_{({o}{o})}$ denotes negation, $\lor_{(({o}{o}){o})}$ denotes disjunction, and $\Pi_{({o}({o}\alpha))}$ is used in defining the universal quantifier as discussed above. $\iota_{(\alpha({o}\alpha))}$ serves either as a description or selection operator as discussed in Section 1.3.4 and Section 1.3.5 below.
- In addition, there may be other constants of various types, which will be called *nonlogical constants* or *parameters*. Each choice of parameters determines a particular formulation of the system of type theory. Parameters are typically used as names for particular entities in the discipline being formalized.

A *formula* is a finite sequence of primitive symbols. Certain formulas are called *well-formed formulas* (*wff*s). We write $\textrm{wff}_{\alpha}$ as an abbreviation for *wff of type* α, and define this concept inductively as follows:

- A primitive variable or constant of type α is a wff$_{\alpha}$.
- If $\bA_{\alpha \beta}$ and $\bB_{\beta}$ are wffs of the indicated types, then $[\bA_{\alpha \beta}\bB_{\beta}]$ is a wff$_{\alpha}$.
- If $\bx_{\beta}$ is a variable of type β and $\bA_{\alpha}$ is a wff, then $[\lambda \bx_{\beta}\bA_{\alpha}]$ is a wff$_{(\alpha \beta)}$.

Note, for example, that by (a) $\nsim_{({o}{o})}$ is a wff$_{({o}{o})}$, so by (b) if $\bA_{{o}}$ is a wff$_{{o}}$, then $[\nsim_{({o}{o})}\bA_{{o}}]$ is a wff$_{{o}}$. Usually, the latter wff will simply be written as $\nsim \bA$. It is often convenient to avoid parentheses, brackets and type symbols, and use conventions for omitting them. For formulas we use the convention of association to the right, and we may write $\lor_{((oo)o)}\bA_{{o}} \bB_{{o}}$ instead of $[[\lor_{((oo)o)}\bA_{{o}}] \bB_{{o}}]$. For types the corresponding convention is analogous.

##### Abbreviations:

- $\bA_{{o}} \lor \bB_{{o}}$ stands for $\lor_{ooo}\bA_{{o}} \bB_{{o}}$.
- $\bA_{{o}} \supset \bB_{{o}}$ stands for $[\nsim_{{o}{o}}\bA_{{o}}] \lor \bB_{{o}}$.
- $\forall \bx_{\alpha}\bA_{{o}}$ stands for $\Pi_{{o}({o}\alpha)} [\lambda \bx_{\alpha}\bA_{{o}}]$.
- Other propositional connectives, and the existential quantifier, are defined in familiar ways. In particular, $$ {\bA_{{o}} \equiv \bB_{{o}} \quad \text{stands for} \quad [\bA_{{o}} \supset \bB_{{o}}] \land [\bB_{{o}} \supset \bA_{{o}}]} $$
- $\sfQ_{{o}\alpha \alpha}$ stands for $\lambda $x$_{\alpha}\lambda $y$_{\alpha}\forall f_{{o}\alpha}{[}f_{{o}\alpha} x_{\alpha} \supset f_{{o}\alpha}y_{\alpha}{]}$.
- $\bA_{\alpha} = \bB_{\alpha}$ stands for $\sfQ_{{o}\alpha \alpha}\bA_{\alpha}\bB_{\alpha}$.

The last definition is known as the Leibnizian definition of equality. It asserts that $x$ and $y$ are the same if $y$ has every property that $x$ has. Actually, Leibniz called his definition “the identity of indiscernibles” and gave it in the form of a biconditional: $x$ and $y$ are the same if $x$ and $y$ have exactly the same properties. It is not difficult to show that these two forms of the definition are logically equivalent.

#### 1.2.2 Examples

We now provide a few examples to illustrate how various assertions and concepts can be expressed in Church’s type theory.

**Example 1** To express the assertion that “Napoleon is charismatic” we introduce constants $\const{Charismatic}_{{o}\imath}$ and $\const{Napoleon}_{\imath}$, with the types indicated by their subscripts and the obvious meanings, and assert the wff

$$\const{Charismatic}_{{o}\imath} \const{Napoleon}_{\imath}$$

If we wish to express the assertion that “Napoleon has all the properties of a great general”, we might consider interpreting this to mean that “Napoleon has all the properties of some great general”, but it seems more appropriate to interpret this statement as meaning that “Napoleon has all the properties which all great generals have”. If the constant $\const{GreatGeneral}_{{o}\imath}$ is added to the formal language, this can be expressed by the wff

$$\forall p_{{o}\imath}[\forall g_{\imath}{[}\const{GreatGeneral}_{{o}\imath}g_{\imath} \supset p_{{o}\imath}g_{\imath}] \supset p_{{o}\imath} \const{Napoleon}_{\imath}]$$

As an example of such a property, we note that the sentence “Napoleon’s soldiers admire him” can be expressed in a similar way by the wff

$$\forall x_{\imath}{[}\const{Soldier}_{{o}\imath}x_{\imath} \land \const{CommanderOf}_{\imath\imath}x_{\imath} = \const{Napoleon}_{\imath} \supset \const{Admires}_{{o}\imath\imath}x_{\imath}\const{Napoleon}_{\imath}]$$

By λ-conversion, this is equivalent to

$$[\lambda n_{\imath}\forall x_{\imath}{[}\const{Soldier}_{{o}\imath}x_{\imath} \land \const{CommanderOf}_{\imath\imath}x_{\imath} = n_{\imath} \supset \const{Admires}_{{o}\imath\imath}x_{\imath}n_{\imath}]]\, \const{Napoleon}_{\imath}$$

This statement asserts that one of the properties which Napoleon has is that of being admired by his soldiers. The property itself is expressed by the wff

$$\lambda n_{\imath}\forall x_{\imath}{[}\const{Soldier}_{{o}\imath}x_{\imath} \land \const{CommanderOf}_{\imath\imath}x_{\imath} = n_{\imath} \supset \const{Admires}_{{o}\imath\imath}x_{\imath}n_{\imath}]$$

**Example 2** We illustrate some potential applications of type theory with the following fable.

> A rich and somewhat eccentric lady named Sheila has an ostrich and a cheetah as pets, and she wishes to take them from her hotel to her remote and almost inaccessible farm. Various portions of the trip may involve using elevators, boxcars, airplanes, trucks, very small boats, donkey carts, suspension bridges, etc., and she and the pets will not always be together. She knows that she must not permit the ostrich and the cheetah to be together when she is not with them.

We consider how certain aspects of this problem can be formalized so that Sheila can use an automated reasoning system to help analyze the possibilities.

There will be a set *Moments* of instants or intervals of time during the trip. She will start the trip at the location $\const{Hotel}$ and moment $\const{Start}$, and end it at the location $\const{Farm}$ and moment $\const{Finish}$. Moments will have type *τ*, and locations will have type *ϱ*. A *state* will have type *σ* and will specify the location of Sheila, the ostrich, and the cheetah at a given moment. A *plan* will specify where the entities will be at each moment according to this plan. It will be a function from moments to states, and will have type $(\sigma \tau)$. The exact representation of states need not concern us, but there will be functions from states to locations called $\const{LocationOfSheila}$, $\const{LocationOfOstrich}$, and $\const{LocationOfCheetah}$ which provide the indicated information. Thus, $\const{LocationOfSheila}_{\varrho \sigma}[p_{\sigma \tau}t_{\tau}]$ will be the location of Sheila according to plan $p_{\sigma \tau}$ at moment $t_{\tau}$. The set $\const{Proposals}_{{o}(\sigma \tau)}$ is the set of plans Sheila is considering.

We define a plan *p* to be acceptable if, according to that plan, the group starts at the hotel, finishes at the farm, and whenever the ostrich and the cheetah are together, Sheila is there too. Formally, we define $\const{Acceptable}_{{o}(\sigma \tau)}$ as

$$\begin{multline} \lambda p_{\sigma \tau} \left[ $$\begin{aligned} & \const{LocationOfSheila}_{\varrho \sigma} [p_{\sigma \tau}\const{Start}_{\tau}] = \const{Hotel}_{\varrho} \,\land\\ & \const{LocationOfOstrich}_{\varrho \sigma}[p_{\sigma \tau} \const{Start}_{\tau}] = \const{Hotel}_{\varrho} \,\land\\ & \const{LocationOfCheetah}_{\varrho \sigma}[p_{\sigma \tau} \const{Start}_{\tau}] = \const{Hotel}_{\varrho} \,\land\\ & \const{LocationOfSheila}_{\varrho \sigma}[p_{\sigma \tau} \const{Finish}_{\tau}] = \const{Farm}_{\varrho} \,\land\\ & \const{LocationOfOstrich}_{\varrho \sigma}[p_{\sigma \tau} \const{Finish}_{\tau}] = \const{Farm}_{\varrho} \,\land\\ & \const{LocationOfCheetah}_{\varrho \sigma}[p_{\sigma \tau} \const{Finish}_{\tau}] = \const{Farm}_{\varrho} \,\land\\ & \forall t_{\tau} \left [ \begin{split} & \const{Moments}_{{o}\tau}t_{\tau} \\ & \supset \left [ \begin{split} & \left[ \begin{split} & \const{LocationOfOstrich}_{\varrho \sigma}[p_{\sigma \tau}t_{\tau}] \\ & = \const{LocationOfCheetah}_{\varrho \sigma}[p_{\sigma \tau}t_{\tau}] \end{split} \right] \\ & \supset \left[ \begin{split} & \const{LocationOfSheila}_{\varrho \sigma}[p_{\sigma \tau}t_{\tau}] \\ & = \const{LocationOfCheetah}_{\varrho\sigma}[p_{\sigma\tau}t_{\tau}] \end{split} \right] \end{split} \right] \end{split} \right] \end{aligned}$$ \right] \end{multline}$$

We can express the assertion that Sheila has a way to accomplish her objective with the formula

$$\exists p_{\sigma \tau}[\const{Proposals}_{{o}(\sigma \tau)}p_{\sigma \tau} \land \const{Acceptable}_{{o}(\sigma \tau)}p_{\sigma \tau}]$$

**Example 3** We now provide a mathematical example. Mathematical ideas can be expressed in type theory without introducing any new constants. An *iterate* of a function $f$ from a set to itself is a function which applies $f$ one or more times. For example, if $g(x) = f(f(f(x)))$, then $g$ is an iterate of $f$. $[\text{ITERATE+}_{{o}(\imath\imath)(\imath\imath)}f_{\imath\imath}g_{\imath\imath}]$ means that $g_{\imath\imath}$ is an iterate of $f_{\imath\imath}$. $\text{ITERATE+}_{{o}(\imath\imath)(\imath\imath)}$ is defined (inductively) as

$$ \lambda f_{\imath\imath}\lambda g_{\imath\imath}\forall p_{{o}(\imath\imath)} \left [p_{{o}(\imath\imath)}f_{\imath\imath} \land \forall j_{\imath\imath} \left [p_{{o}(\imath\imath)}j_{\imath\imath} \supset p_{{o}(\imath\imath)} \left [\lambda x_{\imath}f_{\imath\imath} \left [j_{\imath\imath}x_{\imath} \right] \right] \right] \supset p_{{o}(\imath\imath)}g_{\imath\imath} \right] $$

Thus, $g$ is an iterate of $f$ if $g$ is in every set *p* of functions which contains $f$ and which contains the function $\lambda x_{\imath}f_{\imath\imath}[j_{\imath\imath}x_{\imath}]$ (i.e., $f$ composed with *j*) whenever it contains *j*.

A *fixed point* of $f$ is an element $y$ such that $f(y) = y$.

It can be proved that if some iterate of a function $f$ has a unique fixed point, then $f$ itself has a fixed point. This theorem can be expressed by the wff

$$\begin{aligned} \forall f_{\imath\imath} \left [ \begin{split} \exists g_{\imath\imath} & \left [ \begin{split} &\text{ITERATE+}_{{o}(\imath\imath)(\imath\imath)} f_{\imath\imath} g_{\imath\imath} \\ &{} \land \exists x_{\imath} \left [ \begin{split} & g_{\imath\imath}x_{\imath} = x_{\imath} \\ &{} \land \forall z_{\imath} \left [g_{\imath\imath} z_{\imath} = z_{\imath} \supset z_{\imath} = x_{\imath} \right] \end{split} \right] \end{split} \right]\\ & \supset { } \exists y_{\imath} [f_{\imath\imath}y_{\imath} = y_{\imath}] \end{split} \right]. \end{aligned}$$

See Andrews et al. 1996, for a discussion of how this theorem, which is called THM15B, can be proved automatically.

**Example 4** An example from philosophy is Gödel’s variant of the ontological argument for the existence of God. This example illustrates two interesting aspects:

- Church’s type theory can be employed as a meta-logic to concisely embed expressive other logics such as the higher-order modal logic assumed by Gödel. By exploiting the possible world semantics of this target logic, its syntactic elements are defined in such a way that the infrastructure of the meta-logic are reused as much as possible. In this technique, called *shallow semantical embedding*, the modal operator $\Box$, for example, is simply identified with (taken as syntactic sugar for) the λ-formula $$\lambda \varphi_{{o}\imath} \lambda w_{\imath} \forall v_{\imath} [R_{{o}\imath\imath} w_{\imath} v_{\imath} \supset \varphi_{{o}\imath} v_{\imath}]$$ where $R_{{o}\imath\imath}$ denotes the accessibility relation associated with $\Box$ and type ${\imath}$ is identified with possible worlds. Moreover, since $\forall x_{\alpha} [\bA_{{o}\alpha} x_{\alpha}]$ is shorthand in Church’s type theory for $\Pi_{{o}({o}\alpha)} [\lambda x_{\alpha} [\bA_{{o}\alpha} x_{\alpha}]]$, the modal formula $$\Box \forall x \bP x$$ is represented as $$\Box \Pi' [\lambda x_{\alpha} \lambda w_{\imath} [\bP_{{o}\imath\alpha} x_{\alpha} w_{\imath}]]$$ where $\Pi'$ stands for the λ-term $$\lambda \Phi_{{o}\imath\alpha} \lambda w_{\imath} \forall x_{\alpha} [\Phi_{{o}\imath\alpha} x_{\alpha} w_{\imath}]$$ and the $\Box$ gets resolved as described above. The above choice of $\Pi'$ realizes a possibilist notion of quantification. By introducing a binary “existence” predicate in the metalogic and by utilizing this predicate as an additional guard in the definition of $\Pi'$ an actualist notion of quantification can be obtained. Expressing that an embedded modal formula $\varphi_{{o}\imath}$ is globally valid is captured by the formula $\forall x_{\imath} [\varphi_{{o}\imath} x_{\imath}]$. Local validity (and also actuality) can be modeled as $\varphi_{{o}\imath} n_{\imath}$, where $n_{\imath}$ is a nominal (constant symbol in the meta-logic) denoting a particular possible world.
- The above technique can be exploited for a natural encoding and automated assessment of Gödel’s ontological argument in higher-order modal logic, which unfolds into formulas in Church’s type theory such that higher-order theorem provers can be applied. Further details are presented in Section 6 (Logic and Philosophy) of the SEP entry on automated reasoning and also in Section 5.2; moreover, see Benzmüller & Woltzenlogel-Paleo 2014 and Benzmüller 2019.

**Example 5** Suppose we omit the use of type symbols in the definitions of wffs. Then we can write the formula $\lambda x\nsim[xx]$, which we shall call $\textrm{R}$. It can be regarded as denoting the set of all sets $x$ such that $x$ is not in $x$. We may then consider the formula $[\textrm{R R}]$, which expresses the assertion that $\textrm{R}$ is in itself. We can clearly prove $[\textrm{R R}] \equiv [[\lambda x\nsim [xx]] \textrm{R}]$, so by λ-conversion we can derive $[\textrm{R R}] \equiv\, \nsim[\textrm{R R}]$, which is a contradiction. This is Russell’s paradox. Russell’s discovery of this paradox (Russell 1903, 101-107)[^russell-1903] played a crucial role in the development of type theory. Of course, when type symbols are present, $\textrm{R}$ is not well-formed, and the contradiction cannot be derived.

### 1.3 Axioms and Rules of Inference

#### 1.3.1 Rules of Inference

1. *Alphabetic Change of Bound Variables* $(\alpha$-*conversion*). To replace any well-formed part $\lambda \bx_{\beta}\bA_{\alpha}$ of a wff by $\lambda \by_{\beta} \textsf{Sub}(\by_{\beta},\bx_{\beta},\bA_{\alpha})$, provided that $\by_{\beta}$ does not occur in $\bA_{\alpha}$ and $\bx_{\beta}$ is not bound in $\bA_{\alpha}$.
2. β-*contraction*. To replace any well-formed part $[\lambda \bx_{\alpha}\bB_{\beta}] \bA_{\alpha}$ of a wff by $\textsf{Sub}(\bA_{\alpha},\bx_{\alpha},\bB_{\beta})$, provided that the bound variables of $\bB_{\beta}$ are distinct both from $\bx_{\alpha}$ and from the free variables of $\bA_{\alpha}$.
3. β-*expansion*. To infer $\bC$ from $\bD$ if $\bD$ can be inferred from $\bC$ by a single application of β-contraction.
4. *Substitution*. From $\bF_{({o}\alpha)}\bx_{\alpha}$, to infer $\bF_{({o}\alpha)}\bA_{\alpha}$, provided that $\bx_{\alpha}$ is not a free variable of $\bF_{({o}\alpha)}$.
5. *Modus Ponens*. From $[\bA_{{o}} \supset \bB_{{o}}]$ and $\bA_{{o}}$, to infer $\bB_{{o}}$.
6. *Generalization*. From $\bF_{({o}\alpha)}\bx_{\alpha}$ to infer $\Pi_{{o}({o}\alpha)}\bF_{({o}\alpha)}$, provided that $\bx_{\alpha}$ is not a free variable of $\bF_{({o}\alpha)}$.

#### 1.3.2 Elementary Type Theory

We start by listing the axioms for what we shall call *elementary type theory*.

$$\begin{align} [p_{{o}} \lor p_{{o}}] & \supset p_{{o}} \tag{E1}\\ p_{{o}} & \supset [p_{{o}} \lor q_{{o}}] \tag{E2}\\ [p_{{o}} \lor q_{{o}}] & \supset [q_{{o}} \lor p_{{o}}] \tag{E3}\\ [p_{{o}} \supset q_{{o}}] & \supset [[r_{{o}} \lor p_{{o}}] \supset [r_{{o}} \lor q_{{o}}]] \tag{E4}\\ \Pi_{{o}({o}\alpha)}f_{({o}\alpha)} & \supset f_{({o}\alpha)}x_{\alpha} \tag{E\(5^{\alpha}\)} \\ \forall x_{\alpha}[p_{{o}} \lor f_{({o}\alpha)}x_{\alpha}] & \supset \left[p_{{o}} \lor \Pi_{{o}({o}\alpha)}f_{({o}\alpha)}\right] \tag{E\(6^{\alpha}\)} \end{align}$$

The theorems of elementary type theory are those theorems which can be derived, using the rules of inference, from Axioms $(\rE1){-}(\rE6^{\alpha})$ (for all type symbols $\alpha)$. We shall sometimes refer to elementary type theory as $\cT$. It embodies the logic of propositional connectives, quantifiers, and λ-conversion in the context of type theory.

To illustrate the rules and axioms introduced above, we give a short and trivial proof in $\cT$. Following each wff of the proof, we indicate how it was inferred. (The proof is actually quite inefficient, since line 3 is not used later, and line 7 can be derived directly from line 5 without using line 6. The additional proof lines have been inserted to illustrate some relevant aspects. For the sake of readability, many brackets have been deleted from the formulas in this proof. The diligent reader should be able to restore them.)

$$\begin{alignat}{2} \forall x_{\imath}\left[p_{{o}} \lor f_{{o}\imath}x_{\imath}\right] \supset\left[p_{{o}} \lor \Pi_{{o}({o}\imath)} f_{{o}\imath}\right] && \text{Axiom \(6^{\imath}\)} \tag*{1.}\\ \bigg[\lambda f_{{o}\imath}\bigg[\forall x_{\imath}[p_{{o}} \lor f_{{o}\imath}x_{\imath}] \supset \bigg[p_{{o}} \lor \Pi_{{o}({o}\imath)}f_{{o}\imath}\bigg]\bigg]\bigg] f_{{o}\imath} && \text{β-expansion: 1} \tag*{2.}\\ \Pi_{{o}({o}({o}\imath))}\bigg[\lambda f_{{o}\imath}\bigg[\forall x_{\imath}[p_{{o}} \lor f_{{o}\imath}x_{\imath}] \supset \bigg[p_{{o}} \lor \Pi_{{o}({o}\imath)}f_{{o}\imath}\bigg]\bigg]\bigg] && \text{Generalization: 2} \tag*{3.}\\ \bigg[\lambda f_{{o}\imath}\bigg[\forall x_{\imath}[p_{{o}}\lor f_{{o}\imath}x_{\imath}] \supset \bigg[p_{{o}} \lor \Pi_{{o}({o}\imath)}f_{{o}\imath}\bigg]\bigg]\bigg] [\lambda x_{\imath}r_{{o}\imath}x_{\imath}] && \text{Substitution: 2} \tag*{4.}\\ \forall x_{\imath}[p_{{o}} \lor [\lambda x_{\imath}r_{{o}\imath}x_{\imath}]x_{\imath}] \supset \left[p_{{o}} \lor \Pi_{{o}({o}\imath)}\left[\lambda x_{\imath}r_{{o}\imath}x_{\imath}\right]\right] && \text{β-contraction: 4} \tag*{5.}\\ \forall x_{\imath}[p_{{o}} \lor [\lambda y_{\imath} r_{{o}\imath} y_{\imath}] x_{\imath}] \supset \left[p_{{o}} \lor \Pi_{{o}({o}\imath)}\left[\lambda x_{\imath}r_{{o}\imath}x_{\imath}\right]\right] && \text{α-conversion: 5} \tag*{6.}\\ \forall x_{\imath}\left[p_{{o}} \lor r_{{o}\imath}x_{\imath}\right] \supset \left[p_{{o}} \lor \Pi_{{o}({o}\imath)}\left[\lambda x_{\imath}r_{{o}\imath}x_{\imath}\right]\right] && \text{β-contraction: 6} \tag*{7.} \end{alignat}$$

Note that line 3 can be written as

$$ \forall f_{{o}\imath} [\forall x_{\imath} [p_{{o}} \lor f_{{o}\imath}x_{\imath}] \supset [p_{{o}} \lor [\forall x_{\imath} f_{{o}\imath} x_{\imath}] ]] \tag*{\(3'.\)} $$

and line 7 can be written as

$$ \forall x_{\imath}[p_{{o}} \lor r_{{o}\imath}x_{\imath}] \supset [p_{{o}} \lor \forall x_{\imath}r_{{o}\imath}x_{\imath}] \tag*{\(7'.\)} $$

We have thus derived a well known law of quantification theory. We illustrate one possible interpretation of the line $7'$ wff (which is closely related to Axiom E6) by considering a situation in which a rancher puts some horses in a corral and leaves for the night. Later, he cannot remember whether he closed the gate to the corral. While reflecting on the situation, he comes to a conclusion which can be expressed on line $7'$ if we take the horses to be the elements of type $\imath$, interpret $p_{{o}}$ to mean “the gate was closed”, and interpret $r_{{o}\imath}$ so that $r_{{o}\imath}x_{\imath}$ asserts “$x_{\imath}$ left the corral”. With this interpretation, line $7'$ says

> If it is true of every horse that the gate was closed or that the horse left the corral, then the gate was closed or every horse left the corral.

To the axioms listed above we add the axioms below to obtain Church’s type theory.

#### 1.3.3 Axioms of Extensionality

The axioms of boolean and functional extensionality are the following:

$$\begin{align} [x_{{o}} \equiv y_{{o}}] & \supset x_{{o}} = y_{{o}} \tag{\(7^{o}\)} \\ \forall x_{\beta}[f_{\alpha \beta}x_{\beta} = g_{\alpha \beta}x_{\beta}] & \supset f_{\alpha \beta} = g_{\alpha \beta}\tag{\(7^{\alpha \beta}\)} \end{align}$$

Church did not include Axiom $7^{{o}}$ in his list of axioms in Church 1940, but he mentioned the possibility of including it. Henkin did include it in Henkin 1950.

#### 1.3.4 Descriptions

The expression

$$\exists_1\bx_{\alpha}\bA_{{o}}$$

stands for

$$[\lambda p_{{o}\alpha}\exists y_{\alpha}[p_{{o}\alpha}y_{\alpha} \land \forall z_{\alpha}[p_{{o}\alpha}z_{\alpha} \supset z_{\alpha} = y_{\alpha}]]]\, [\lambda \bx_{\alpha}\bA_{{o}}]$$

For example,

$$\exists_1 x_{\alpha}P_{{o}\alpha}x_{\alpha}$$

stands for

$$[\lambda p_{{o}\alpha}\exists y_{\alpha}[p_{{o}\alpha}y_{\alpha} \land \forall z_{\alpha}[p_{{o}\alpha}z_{\alpha} \supset z_{\alpha} = y_{\alpha}]]]\, [\lambda x_{\alpha}P_{{o}\alpha}x_{\alpha}]$$

By λ-conversion, this is equivalent to

$$\exists y_{\alpha}[[\lambda x_{\alpha}P_{{o}\alpha}x_{\alpha}]y_{\alpha} \land \forall z_{\alpha}[[\lambda x_{\alpha}P_{{o}\alpha}x_{\alpha}] z_{\alpha} \supset z_{\alpha} = y_{\alpha}]]$$

which reduces by λ-conversion to

$$\exists y_{\alpha}[P_{{o}\alpha}y_{\alpha} \land \forall z_{\alpha}[P_{{o}\alpha}z_{\alpha} \supset z_{\alpha} = y_{\alpha}]]$$

This asserts that there is a unique element which has the property $P_{{o}\alpha}$. From this example we can see that in general, $\exists_1\bx_{\alpha}\bA_{{o}}$ expresses the assertion that “there is a unique $\bx_{\alpha}$ such that $\bA_{{o}}$”.

When there is a unique such element $\bx_{\alpha}$, it is convenient to have the notation $\atoi\bx_{\alpha}\bA_{{o}}$ to represent the expression “the $\bx_{\alpha}$ such that $\bA_{{o}}$”. Russell showed in Whitehead & Russell 1927b how to provide contextual definitions for such notations in his formulation of type theory. In Church’s type theory $\atoi\bx_{\alpha}\bA_{{o}}$ is defined as $\iota_{\alpha({o}\alpha)}[\lambda \bx_{\alpha}\bA_{{o}}]$. Thus, $\atoi$ behaves like a variable-binding operator, but it is defined in terms of λ with the aid of the logical constant $\iota_{\alpha({o}\alpha)}$. Thus, λ is still the only variable-binding operator that is needed.

Since $\bA_{{o}}$ describes $\bx_{\alpha}, \iota_{\alpha({o}\alpha)}$ is called a *description operator*. Associated with this notation is the following:

##### Axiom of Descriptions:

$$ \exists_1 x_{\alpha}[p_{{o}\alpha}x_{\alpha}] \supset p_{{o}\alpha} [\iota_{\alpha({o}\alpha)}p_{{o}\alpha}] \tag{\(8^{\alpha}\)} $$

This says that when the set $p_{{o}\alpha}$ has a unique member, then $\iota_{\alpha({o}\alpha)}p_{{o}\alpha}$ is in $p_{{o}\alpha}$, and therefore is that unique member. Thus, this axiom asserts that $\iota_{\alpha({o}\alpha)}$ maps one-element sets to their unique members.

If from certain hypotheses one can prove

$$\exists_1\bx_{\alpha}\bA_{{o}}$$

then by using Axiom $8^{\alpha}$ one can derive

$$[\lambda \bx_{\alpha}\bA_{{o}}] [\iota_{\alpha({o}\alpha)}[\lambda \bx_{\alpha}\bA_{{o}}]]$$

which can also be written as

$$[\lambda \bx_{\alpha}\bA_{{o}}] {[\atoi\bx_{\alpha}\bA_{{o}}]}$$

We illustrate the usefulness of the description operator with a small example. Suppose we have formalized the theory of real numbers, and our theory has constants $1_{\varrho}$ and $\times_{\varrho \varrho \varrho}$ to represent the number 1 and the multiplication function, respectively. (Here *ϱ* is the type of real numbers.) To represent the multiplicative inverse function, we can define the wff $\textrm{INV}_{\varrho \varrho}$ as

$${\lambda z_{\varrho} \atoi x_{\varrho} [\times_{\varrho \varrho \varrho}z_{\varrho}x_{\varrho} = 1_{\varrho}]}$$

Of course, in traditional mathematical notation we would not write the type symbols, and we would write $\times_{\varrho \varrho \varrho}z_{\varrho}x_{\varrho}$ as $z \times x$ and write $\textrm{INV}_{\varrho \varrho}z$ as $z^{-1}$. Thus $z^{-1}$ is defined to be that $x$ such that $z \times x = 1$. When *Z* is provably not 0, we will be able to prove $\exists_1 x_{\varrho}[\times_{\varrho \varrho \varrho} \textrm{Z x}_{\varrho} = 1_{\varrho}]$ and $Z \times Z^{-1} = 1$, but if we cannot establish that *Z* is not 0, nothing significant about $Z^{-1}$ will be provable.

#### 1.3.5 Axiom of Choice

The Axiom of Choice can be expressed as follows in Church’s type theory:

$$ \exists x_{\alpha}p_{{o}\alpha}x_{\alpha} \supset p_{{o}\alpha}[\iota_{\alpha({o}\alpha)}p_{{o}\alpha}] \tag{\(9^{\alpha}\)} $$

$(9^{\alpha})$ says that the choice function $\iota_{\alpha({o}\alpha)}$ chooses from every nonempty set $p_{{o}\alpha}$ an element, designated as $\iota_{\alpha({o}\alpha)}p_{{o}\alpha}$, of that set. When this form of the Axiom of Choice is included in the list of axioms, $\iota_{\alpha({o}\alpha)}$ is called a selection operator instead of a description operator, and $\atoi\bx_{\alpha} \bA_{{o}}$ means “an $\bx_{\alpha}$ such that $\bA_{{o}}$” when there is some such element $\bx_{\alpha}$. These selection operators have the same meaning as Hilbert’s *ε*-operator (Hilbert 1928)[^hilbert-1928]. However, we here provide one such operator for each type α.

It is natural to call $\atoi$ a definite description operator in contexts where $\atoi\bx_{\alpha}\bA_{{o}}$ means “the $\bx_{\alpha}$ such that $\bA_{{o}}$”, and to call it an indefinite description operator in contexts where $\atoi\bx_{\alpha}\bA_{{o}}$ means “an $\bx_{\alpha}$ such that $\bA_{{o}}$”.

Clearly the Axiom of Choice implies the Axiom of Descriptions, but sometimes formulations of type theory are used which include the Axiom of Descriptions, but not the Axiom of Choice.

Another formulation of the Axiom of Choice simply asserts the existence of a choice function without explicitly naming it:

$$ \exists j_{\alpha ({o}\alpha)}\forall p_{{o}\alpha}[\exists x_{\alpha}p_{{o}\alpha}x_{\alpha} \supset p_{{o}\alpha}[j_{\alpha({o}\alpha)}p_{{o}\alpha}]] \tag{\(\text{AC}^{\alpha}\)} $$

Normally when one assumes the Axiom of Choice in type theory, one assumes it as an axiom schema, and asserts AC$^{\alpha}$ for each type symbol α. A similar remark applies to the axioms for extensionality and description. However, modern proof systems for Church’s type theory, which are, e.g., based on resolution, do in fact avoid the addition of such axiom schemata for reasons as further explained in Sections 3.4 and 4 below. They work with more constrained, goal-directed proof rules instead.

Before proceeding, we need to introduce some terminology. $\cQ_0$ is an alternative formulation of Church’s type theory which will be described in Section 1.4 and is equivalent to the system described above using Axioms (1)–(8). A type symbol is *propositional* if the only symbols which occur in it are ${o}$ and parentheses.

Yasuhara (1975)[^yasuhara-1975] defined the relation “$\ge$” between types as the reflexive transitive closure of the minimal relation such that $(\alpha \beta) \ge \alpha$ and $(\alpha \beta) \ge \beta$. He established that:

- If $\alpha \ge \beta$, then $\cQ_0 \vdash$ AC$^{\alpha} \supset$ AC$^{\beta}$.
- Given a set *S* of types, none of which is propositional, there is a model of $\cQ_0$ in which AC$^{\alpha}$ fails if and only if $\alpha \ge \beta$ for some β in *S*.

The existence of a choice functions for “higher” types thus entails the existence of choice functions for “lower” types, the opposite is generally not the case though.

Büchi (1953)[^büchi-1953] has shown that while the schemas expressing the Axiom of Choice and Zorn’s Lemma can be derived from each other, the relationships between the particular types involved are complex.

#### 1.3.6 Axioms of Infinity

One can define the natural numbers (and therefore other basic mathematical structures such as the real and complex numbers) in type theory, but to prove that they have the required properties (such as Peano’s Postulates), one needs an Axiom of Infinity. There are many viable possibilities for such an axiom, such as those discussed in Church 1940, section 57 of Church 1956, and section 60 of Andrews 2002.

### 1.4 A Formulation Based on Equality

In Section 1.2.1, $\nsim_{({o}{o})}, \lor_{(({o}{o}){o})}$, and the $\Pi_{({o}({o}\alpha))}$’s were taken as primitive constants, and the wffs $\sfQ_{{o}\alpha \alpha}$ which denote equality relations at type α were defined in terms of these. We now present an alternative formulation $\cQ_0$ of Church’s type theory in which there are primitive constants $\sfQ_{{o}\alpha \alpha}$ denoting equality, and $\nsim_{({o}{o})}, \lor_{(({o}{o}){o})}$, and the $\Pi_{({o}({o}\alpha))}$’s are defined in terms of the $\sfQ_{{o}\alpha \alpha}$’s.

Tarski (1923)[^tarski-1923] noted that in the context of higher-order logic, one can define propositional connectives in terms of logical equivalence and quantifiers. Quine (1956)[^quine-1956] showed how both quantifiers and connectives can be defined in terms of equality and the abstraction operator λ in the context of Church’s type theory. Henkin (1963)[^henkin-1963] rediscovered these definitions, and developed a formulation of Church’s type theory based on equality in which he restricted attention to propositional types. Andrews (1963)[^andrews-1963] simplified the axioms for this system.

$\cQ_0$ is based on these ideas, and can be shown to be equivalent to a formulation of Church’s type theory using Axioms (1)–(8) of the preceding sections. This section thus provides an alternative to the material in the preceding Sections 1.2.1–1.3.4. More details about $\cQ_0$ can be found in Andrews 2002.

#### 1.4.1 Definitions

- Type symbols, improper symbols, and variables of $\cQ_0$ are defined as in Section 1.2.1.
- The logical constants of $\cQ_0$ are $\sfQ_{(({o}\alpha)\alpha)}$ and $\iota_{(\imath({o}\imath))}$ (for each type symbol α).
- Wffs of $\cQ_0$ are defined as in Section 1.2.1.

##### Abbreviations:

- $\bA_{\alpha} = \bB_{\alpha}$ stands for $\sfQ_{{o}\alpha \alpha}\bA_{\alpha}\bB_{\alpha}$
- $\bA_{{o}} \equiv \bB_{{o}}$ stands for $\sfQ_{{o}{o}{o}}$**A$_{{o}}$B**$_{{o}}$
- $T_{{o}}$ stands for $\sfQ_{{o}{o}{o}} = \sfQ_{{o}{o}{o}}$
- $F_{{o}}$ stands for $[\lambda x_{{o}}T_{{o}}] = [\lambda x_{{o}}x_{{o}}]$
- $\Pi_{{o}({o}\alpha)}$ stands for $\sfQ_{{o}({o}\alpha)({o}\alpha)}[\lambda x_{\alpha}T_{{o}}]$
- $\forall \bx_{\alpha}\bA$ stands for $\Pi_{{o}({o}\alpha)}[\lambda \bx_{\alpha}\bA]$
- $\land_{{o}{o}{o}}$ stands for $\lambda x_{{o}}\lambda y_{{o}}[[\lambda g_{{o}{o}{o}}[g_{{o}{o}{o}}T_{{o}}T_{{o}}]] = [\lambda g_{{o}{o}{o}}[g_{{o}{o}{o}}x_{{o}}y_{{o}}]]]$
- $\bA_{{o}} \land \bB_{{o}}$ stands for $\land_{{o}{o}{o}} \bA_{{o}} \bB_{{o}}$
- $\nsim_{{o}{o}}$ stands for $\sfQ_{{o}{o}{o}}F_{{o}}$

$T_{{o}}$ denotes truth. The meaning of $\Pi_{{o}({o}\alpha)}$ was discussed in Section 1.1. To see that this definition of $\Pi_{{o}({o}\alpha)}$ is appropriate, note that $\lambda x_{\alpha}T$ denotes the set of all elements of type α, and that $\Pi_{{o}({o}\alpha)}s_{{o}\alpha}$ stands for $\sfQ_{{o}({o}\alpha)({o}\alpha)}[\lambda x_{\alpha}T] s_{{o}\alpha}$, respectively for $[\lambda x_{\alpha}T] = s_{{o}\alpha}$. Therefore $\Pi_{{o}({o}\alpha)}s_{{o}\alpha}$ asserts that $s_{{o}\alpha}$ is the set of all elements of type α, so $s_{{o}\alpha}$ contains all elements of type α. It can be seen that $F_{{o}}$ can also be written as $\forall x_{{o}}x_{{o}}$, which asserts that everything is true. This is false, so $F_{{o}}$ denotes falsehood. The expression $\lambda g_{{o}{o}{o}}[g_{{o}{o}{o}}x_{{o}}y_{{o}}]$ can be used to represent the ordered pair $\langle x_{{o}},y_{{o}}\rangle$, and the conjunction $x_{{o}} \land y_{{o}}$ is true iff $x_{{o}}$ and $y_{{o}}$ are both true, i.e., iff $\langle T_{{o}},T_{{o}}\rangle = \langle x_{{o}},y_{{o}}\rangle$. Hence $x_{{o}} \land y_{{o}}$ can be expressed by the formula $[\lambda g_{{o}{o}{o}}[g_{{o}{o}{o}}T_{{o}}T_{{o}}]] = [\lambda g_{{o}{o}{o}}[g_{{o}{o}{o}}x_{{o}}y_{{o}}]]$.

Other propositional connectives, such as $\lor, \supset$, and the existential quantifier $\exists$, are easily defined. By using $\iota_{(\imath({o}\imath))}$, one can define description operators $\iota_{\alpha({o}\alpha)}$ for all types α.

#### 1.4.2 Axioms and Rules of Inference

$\cQ_0$ has a single rule of inference.

> **Rule R:** From $\bC$ and $\bA_{\alpha} = \bB_{\alpha}$, to infer the result of replacing one occurrence of $\bA_{\alpha}$ in $\bC$ by an occurrence of $\bB_{\alpha}$, provided that the occurrence of $\bA_{\alpha}$ in $\bC$ is not (an occurrence of a variable) immediately preceded by λ.

The *axioms for $\cQ_0$* are the following:

$$\begin{align} [g_{{o}{o}}T_{{o}} \land g_{{o}{o}}F_{{o}}] &= \forall x_{{o}}[g_{{o}{o}}x_{{o}}] \tag{Q1}\\ [x_{\alpha} = y_{\alpha}] & \supset [h_{{o}\alpha}x_{\alpha} = h_{{o}\alpha}y_{\alpha}] \tag{Q\(2^{\alpha}\)}\\ [f_{\alpha \beta} = g_{\alpha \beta}] & = \forall x_{\beta}[f_{\alpha \beta}x_{\beta} = g_{\alpha \beta}x_{\beta}] \tag{Q\(3^{\alpha \beta}\)}\\ [\lambda \bx_{\alpha}\bB_{\beta}]\bA_{\alpha} & = \textsf{SubFree}(\bA_{\alpha},\bx_{\alpha},\bB_{\beta}), \tag{Q4}\\ &\quad \text{ provided } \bA_{\alpha} \text{ is free for } \bx \text{ in } \bB_{\beta}\\ \iota_{\imath({o}\imath)}[\sfQ_{{o}\imath\imath}y_{\imath}] &= y_{\imath} \tag{Q5} \end{align}$$ The additional condition in axiom $(\rQ4)$ ensures that the substitution does not lead to free variables of A being bound in the result of the substitution.

## 2. Semantics

It is natural to compare the semantics of type theory with the semantics of first-order logic, where the theorems are precisely the wffs which are valid in all interpretations. From an intuitive point of view, the natural interpretations of type theory are *standard models*, which are defined below. However, it is a consequence of Gödel’s Incompleteness Theorem (Gödel 1931)[^gödel-1931] that axioms (1)–(9) do not suffice to derive all wffs which are valid in all standard models, and there is no consistent recursively axiomatized extension of these axioms which suffices for this purpose. Nevertheless, experience shows that these axioms are sufficient for most purposes, and Leon Henkin considered the problem of clarifying in what sense they are complete. The definitions and theorem below constitute Henkin’s (1950)[^henkin-1950] solution to this problem, which is often referred to as *general semantics* or *Henkin semantics*.

A *frame* is a collection $\{\cD_{\alpha}\}_{\alpha}$ of nonempty domains (sets) $\cD_{\alpha}$, one for each type symbol α, such that $\cD_{{o}} = \{\sfT,\sfF\}$ (where $\sfT$ represents truth and $\sfF$ represents falsehood), and $\cD_{\alpha \beta}$ is some collection of functions mapping $\cD_{\beta}$ into $\cD_{\alpha}$. The members of $\cD_{\imath}$ are called *individuals*.

An *interpretation* $\langle \{\cD_{\alpha}\}_{\alpha}, \frI\rangle$ consists of a frame and a function $\frI$ which maps each constant *C* of type α to an appropriate element of $\cD_{\alpha}$, which is called the *denotation of* *C*. The logical constants are given their standard denotations.

An *assignment* of values in the frame $\{\cD_{\alpha}\}_{\alpha}$ to variables is a function *φ* such that $\phi \bx_{\alpha} \in \cD_{\alpha}$ for each variable $\bx_{\alpha}$. (Notation: The assignment $\phi[a/x]$ maps variable $x$ to value *a* and it is identical with *φ* for all other variable symbols different from $x$.)

An interpretation $\cM = \langle \{\cD_{\alpha}\}_{\alpha}, \frI\rangle$ is a *general model* (aka *Henkin model*) iff there is a binary function $\cV$ such that $\cV_{\phi}\bA_{\alpha} \in \cD_{\alpha}$ for each assignment *φ* and wff $\bA_{\alpha}$, and the following conditions are satisfied for all assignments and all wffs:

- $\cV_{\phi}\bx_{\alpha} = \phi \bx_{\alpha}$ for each variable $\bx_{\alpha}$.
- $\cV_{\phi}A_{\alpha} = \frI A_{\alpha}$ if $A_{\alpha}$ is a primitive constant.
- $\cV_{\phi}[\bA_{\alpha \beta}\bB_{\beta}] = (\cV_{\phi}\bA_{\alpha \beta})(\cV_{\phi}\bB_{\beta})$ (the value of a function $\cV_{\phi}\bA_{\alpha \beta}$ at the argument $\cV_{\phi}\bB_{\beta})$.
- $\cV_{\phi}[\lambda \bx_{\alpha}\bB_{\beta}] =$ that function from $\cD_{\alpha}$ into $\cD_{\beta}$ whose value for each argument $z \in \cD_{\alpha}$ is $\cV_{\psi}\bB_{\beta}$, where *ψ* is that assignment such that $\psi \bx_{\alpha} = z$ and $\psi \by_{\beta} = \phi \by_{\beta}$ if $\by_{\beta} \ne \bx_{\alpha}$.

If an interpretation $\cM$ is a general model, the function $\cV$ is uniquely determined. $\cV_{\phi}\bA_{\alpha}$ is called the *value* of $\bA_{\alpha}$ in $\cM$ with respect to *φ*.

One can easily show that the following statements hold in all general models $\cM$ for all assignments *φ* and all wffs $\bA$ and $\bB$:

- $\cV_{\phi} T_{{o}} = \sfT$ and $\cV_{\phi} F_{{o}} = \sfF$
- $\cV_{\phi} [\nsim_{{o}{o}} \bA_{{o}}] = \sfT$ iff $\cV_{\phi} \bA_{{o}} = \sfF$
- $\cV_{\phi} [ \bA_{{o}} \lor \bB_{{o}} ] = \sfT$ iff $\cV_{\phi} \bA_{{o}} = \sfT$ or $\cV_{\phi} \bB_{{o}} = \sfT$
- $\cV_{\phi} [ \bA_{{o}} \land \bB_{{o}} ] = \sfT$ iff $\cV_{\phi} \bA_{{o}} = \sfT$ and $\cV_{\phi} \bB_{{o}} = \sfT$
- $\cV_{\phi} [ \bA_{{o}} \supset \bB_{{o}} ] = \sfT$ iff $\cV_{\phi} \bA_{{o}} = \sfF$ or $\cV_{\phi} \bB_{{o}} = \sfT$
- $\cV_{\phi} [ \bA_{{o}} \equiv \bB_{{o}} ] = \sfT$ iff $\cV_{\phi} \bA_{{o}} = \cV_{\phi} \bB_{{o}}$
- $\cV_{\phi} [\forall \bx_{\alpha}\bA] = \sfT$ iff $\cV_{\phi[a/x]} \bA= \sfT$ for all $a \in \cD_{\alpha}$
- $\cV_{\phi} [\exists \bx_{\alpha}\bA] = \sfT$ iff there exists an $a \in \cD_{\alpha}$ such that $\cV_{\phi[a/x]} \bA= \sfT$

The semantics of general models is thus as expected. However, there is a subtlety to note regarding the following condition for arbitrary types α:

- [equality] $\cV_{\phi} [ \bA_{\alpha} = \bB_{\alpha} ] = \sfT$ iff $\cV_{\phi} \bA_{\alpha} = \cV_{\phi} \bB_{\alpha}$

When the definitions of Section 1.2.1 are employed, where equality has been defined in terms of Leibniz’ principle, then this statement is not implied for all types α. It only holds if we additionally require that the domains $\cD_{{o}\alpha}$ contain all the unit sets of objects of type α, or, alternatively, that the domains $\cD_{{o}\alpha\alpha}$ contain the respective identity relations on objects of type α (which entails the former). The need for this additional requirement, which is not included in the original work of Henkin (1950)[^henkin-1950], has been demonstrated in Andrews 1972a.

When instead the alternative definitions of Section 1.4 are employed, then this requirement is obviously met due to the presence of the logical constants $\sfQ_{{o}\alpha \alpha}$ in the signature, which by definition denote the respective identity relations on the objects of type α and therefore trivially ensure their existence in each general model $\cM$. It is therefore a natural option to always assume primitive equality constants (for each type α) in a concrete choice of base system for Church’s type theory, just as realized in Andrews’ system $\cQ_0$.

An interpretation $\langle \{\cD_{\alpha}\}_{\alpha}, \frI\rangle$ is a *standard model* iff for all α and $\beta , \cD_{\alpha \beta}$ is the set of all functions from $\cD_{\beta}$ into $\cD_{\alpha}$. Clearly a standard model is a general model.

We say that a wff $\bA$ is *valid* in a model $\cM$ iff $\cV_{\phi}\bA = \sfT$ for every assignment *φ* into $\cM$. A model for a set $\cH$ of wffs is a model in which each wff of $\cH$ is valid.

A wff $\bA$ is *valid in the general* [*standard*] *sense* iff $\bA$ is valid in every general [standard] model. Clearly a wff which is valid in the general sense is valid in the standard sense, but the converse of this statement is false.

**Completeness and Soundness Theorem (Henkin 1950)[^henkin-1950]:** A wff is a theorem if and only if it is valid in the general sense.

Not all frames belong to interpretations, and not all interpretations are general models. In order to be a general model, an interpretation must have a frame satisfying certain closure conditions which are discussed further in Andrews 1972b. Basically, in a general model every wff must have a value with respect to each assignment.

A model is said to be *finite* iff its domain of individuals is finite. Every finite model for $\cQ_0$ is standard (Andrews 2002, Theorem 5404)[^andrews-2002], but every set of sentences of $\cQ_0$ which has infinite models also has nonstandard models (Andrews2002, Theorem 5506).

An understanding of the distinction between standard and nonstandard models can clarify many phenomena. For example, it can be shown that there is a model $\cM = \langle \{\cD_{\alpha}\}_{\alpha}, \frI\rangle$ in which $\cD_{\imath}$ is infinite, and all the domains $\cD_{\alpha}$ are countable. Thus $\cD_{\imath}$ and $\cD_{{o}\imath}$ are both countably infinite, so there must be a bijection *h* between them. However, Cantor’s Theorem (which is provable in type theory and therefore valid in all models) says that $\cD_{\imath}$ has more subsets than members. This seemingly paradoxical situation is called Skolem’s Paradox. It can be resolved by looking carefully at Cantor’s Theorem, i.e., $\nsim \exists g_{{o}\imath\imath}\forall f_{{o}\imath}\exists j_{\imath}[g_{{o}\imath\imath}j_{\imath} = f_{{o}\imath}]$, and considering what it means in a model. The theorem says that there is no function $g \in \cD_{{o}\imath\imath}$ from $\cD_{\imath}$ into $\cD_{{o}\imath}$ which has every set $f_{{o}\imath} \in \cD_{{o}\imath}$ in its range. The usual interpretation of the statement is that $\cD_{{o}\imath}$ is bigger (in cardinality) than $\cD_{\imath}$. However, what it actually means in this model is that *h* cannot be in $\cD_{{o}\imath\imath}$. Of course, $\cM$ must be nonstandard.

While the Axiom of Choice is presumably true in all standard models, there is a nonstandard model for $\cQ_0$ in which AC$^{\imath}$ is false (Andrews 1972b)[^andrews-1972b]. Thus, AC$^{\imath}$ is not provable in $\cQ_0$.

Thus far, investigations of model theory for Church’s type theory have been far less extensive than for first-order logic. Nevertheless, there has been some work on methods of constructing nonstandard models of type theory and models in which various forms of extensionality fail, models for theories with arbitrary (possibly incomplete) sets of logical constants, and on developing general methods of establishing completeness of various systems of axioms with respect to various classes of models. Relevant papers include Andrews 1971, 1972a,b, and Henkin 1975. Further related work can be found in Benzmüller et al. 2004, Brown 2004, 2007, and Muskens 2007.

## 3. Metatheory

### 3.1 Lambda-Conversion

The first three rules of inference in Section 1.3.1 are called rules of λ-*conversion*. If $\bD$ and $\bE$ are wffs, we write $\bD \conv \bE$ to indicate that $\bD$ can be converted to $\bE$ by applications of these rules. This is an equivalence relation between wffs. A wff $\bD$ is in β-*normal form* iff it has no well-formed parts of the form $[[\lambda \bx_{\alpha}\bB_{\beta}]\bA_{\alpha}]$. Every wff is convertible to one in β-normal form. Indeed, every sequence of contractions (applications of rule 2, combined as necessary with alphabetic changes of bound variables) of a wff is finite; obviously, if such a sequence cannot be extended, it terminates with a wff in β-normal form. (This is called the strong normalization theorem.) By the Church-Rosser Theorem, this wff in β-normal form is unique modulo alphabetic changes of bound variables. For each wff $\bA$ we denote by ${\downarrow}\bA$ the first wff (in some enumeration) in β-normal form such that $\bA \conv {\downarrow} \bA$. Then $\bD \conv \bE$ if and only if ${\downarrow} \bD = {\downarrow} \bE$.

By using the Axiom of Extensionality one can obtain the following derived rule of inference:

> *η*-*Contraction*. Replace a well-formed part $[\lambda \by_{\beta}[\bB_{\alpha \beta}\by_{\beta}]]$ of a wff by $\bB_{\alpha \beta}$, provided $\by_{\beta}$ does not occur free in $\bB_{\alpha \beta}$.

This rule and its inverse (which is called *η*-*Expansion*) are sometimes used as additional rules of λ-conversion. See Church 1941, Stenlund 1972, Barendregt 1984, and Barendregt et al. 2013 for more information about λ-conversion.

It is worth mentioning (again) that λ-abstraction replaces the need for comprehension axioms in Church’s type theory.

### 3.2 Higher-Order Unification

The challenges in higher-order unification are outlined very briefly. More details on the topic are given in Dowek 2001; its utilization in higher-order theorem provers is also discussed in Benzmüller & Miller 2014.

**Definition.** A *higher-order unifier* for a pair $\langle \bA,\bB\rangle$ of wffs is a substitution *θ* for free occurrences of variables such that $\theta \bA$ and $\theta \bB$ have the same β-normal form. A higher-order unifier for a set of pairs of wffs is a unifier for each of the pairs in the set.

Higher-order unification differs from first-order unification (Baader & Snyder 2001)[^baader-2001] in a number of important respects. In particular:

1. Even when a unifier for a pair of wffs exists, there may be no most general unifier (Gould 1966)[^gould-1966].
2. Higher-order unification is undecidable (Huet 1973b)[^huet-1973b], even in the “second-order” case (Goldfarb 1981)[^goldfarb-1981].

However, an algorithm has been devised (Huet 1975, Jensen & Pietrzykowski 1976)[^huet-1975][^jensen-1976], called *pre-unification*, which will find a unifier for a set of pairs of wffs if one exists. The pre-unifiers computed by Huet’s procedure are substitutions that can reduce the original unification problem to one involving only so called *flex-flex* unification pairs. Flex-flex pairs have variable head symbols in both terms to be unified and they are known to always have a solution. The concrete computation of these solutions can thus be postponed or omitted. Pre-unification is utilized in all the resolution based theorem provers mentioned in Section 4.

*Pattern unification* refers a small subset of unification problems, first studied by Miller 1991, whose identification has been important for the construction of practical systems. In a pattern unification problem every occurrence of an existentially quantified variable is applied to a list of arguments that are all distinct variables bound by either a λ-binder or a universal quantifier in the scope of the existential quantifier. Thus, existentially quantified variables cannot be applied to general terms but a very restricted set of bound variables. Pattern unification, like first-order unification, is decidable and most general unifiers exist for solvable problems. This is why pattern unification is preferably employed (when applicable) in some state-of-the-art theorem provers for Church’s type theory.

### 3.3 A Unifying Principle

The *Unifying Principle* was introduced in Smullyan 1963 (see also Smullyan 1995)[^smullyan-1995] as a tool for deriving a number of basic metatheorems about first-order logic in a uniform way. The principle was extended to elementary type theory by Andrews (1971)[^andrews-1971] and to extensional type theory, that is, Henkin’s general semantics without description or choice, by Benzmüller, Brown and Kohlhase (2004). We outline these extensions in some more detail below.

#### 3.3.1 Elementary Type Theory

The Unifying Principle was extended to elementary type theory (the system $\cT$ of Section 1.3.2) in Andrews 1971 by applying ideas in Takahashi 1967. This Unifying Principle for $\cT$ has been used to establish cut-elimination for $\cT$ in Andrews 1971 and completeness proofs for various systems of type theory in Huet 1973a, Kohlhase 1995, and Miller 1983. We first give a definition and then state the principle.

**Definition.** A property *Γ* of finite sets of wffs$_{{o}}$ is an *abstract consistency property* iff for all finite sets $\cS$ of wffs$_{{o}}$, the following properties hold (for all wffs **A, B**):

1. If $\Gamma(\cS)$, then there is no atom $\bA$ such that $\bA \in \cS$ and $[\nsim \bA] \in \cS$.
2. If $\Gamma(\cS \cup \{\bA\})$, then $\Gamma(\cS \cup {\downarrow} \bA\})$.
3. If $\Gamma(\cS \cup \{\nsim \nsim \bA\})$, then $\Gamma(\cS \cup \{\bA\})$.
4. If $\Gamma(\cS \cup \{\bA \lor \bB\})$, then $\Gamma(\cS \cup \{\bA\})$ or $\Gamma(\cS \cup \{\bB\})$.
5. If $\Gamma(\cS \cup \{\nsim[\bA \lor \bB]\})$, then $\Gamma(\cS \cup \{\nsim \bA,\nsim \bB\})$.
6. If $\Gamma(\cS \cup \{\Pi_{{o}({o}\alpha)}\bA_{{o}\alpha}\})$, then $\Gamma(\cS \cup \{\Pi_{{o}({o}\alpha)}\bA_{{o}\alpha}, \bA_{{o}\alpha}\bB_{\alpha}\})$ for each wff $\bB_{\alpha}$.
7. If $\Gamma(\cS \cup \{\nsim \Pi_{{o}({o}\alpha)}\bA_{{o}\alpha}\})$, then $\Gamma(\cS \cup \{\nsim \bA_{{o}\alpha}\bc_{\alpha}\})$, for any variable or parameter $\bc_{\alpha}$ which does not occur free in $\bA_{{o}\alpha}$ or any wff in $\cS$.

Note that *consistency* is an abstract consistency property.

**Unifying Principle for $\cT$.** If *Γ* is an abstract consistency property and $\Gamma(\cS)$, then $\cS$ is consistent in $\cT$.

Here is a typical application of the Unifying Principle. Suppose there is a procedure $\cM$ which can be used to refute sets of sentences, and we wish to show it is complete for $\cT$. For any set of sentences, let $\Gamma(\cS)$ mean that $\cS$ is not refutable by $\cM$, and show that *Γ* is an abstract consistency property. Now suppose that $\bA$ is a theorem of $\cT$. Then $\{\nsim \bA\}$ is inconsistent in $\cT$, so by the Unifying Principle not $\Gamma(\{\nsim \bA\})$, so $\{\nsim \bA\}$ is refutable by $\cM$.

#### 3.3.2 Extensional Type Theory

Extensions of the above Unifying principle towards Church’s type theory with general semantics were studied since the mid nineties. A primary motivation was to support (refutational) completeness investigations for the proof calculi underlying the emerging higher-order automated theorem provers (see Section 4 below). The initial interest was on a fragment of Church’s type theory, called *extensional type theory*, that includes the extensionality axioms, but excludes $\iota_{(\alpha({o}\alpha))}$ and the axioms for it (description and choice were largely neglected in the automated theorem provers at the time). Analogous to before, a distinction has been made between extensional type theory with *defined equality* (as in Section 1.2.1, where equality is defined via Leibniz’ principle) and extensional type theory with *primitive equality* (e.g., system $\cQ_0$ as in Section 1.4, or, alternatively, a system based on logical constants $\nsim_{({o}{o})}, \lor_{(({o}{o}){o})}$, and the $\Pi_{({o}({o}\alpha))}$’s as in Section 1.2.1, but with additional primitive logical constants $=_{{o}\alpha\alpha}$ added).

A first attempt towards a Unifying Principle for extensional type theory with primitive equality is presented in Kohlhase 1993. The conditions given there, which are still incomplete[^note-1], were subsequently modified and complemented as follows:

- To obtain a Unifying Principle for extensional type theory with defined equality, Benzmüller & Kohlhase 1997 added the following conditions for boolean extensionality, functional extensionality and saturation to the above conditions 1.-7. for $\cT$ (their presentation has been adapted here; for technical reasons, they also employ a slightly stronger variant for condition 2. based on β-conversion rather than β-normalization):
- If $\Gamma(\cS \cup \{ \bA_{{o}} = \bB_{{o}} \})$, then $\Gamma(\cS \cup \{ \bA_{{o}}, \bB_{{o}} \})$ or $\Gamma(\cS \cup \{ \nsim \bA_{{o}}, \nsim \bB_{{o}} \})$
- If $\Gamma(\cS \cup \{ \bA_{\alpha\beta} = \bB_{\alpha\beta} \})$, then $\Gamma(\cS \cup \{ \bA_{\alpha\beta} \bc_\beta = \bB_{\alpha\beta} \bc_\beta \})$ for any parameter $\bc_{\beta}$ which does not occur free in $\cS$.
- $\Gamma(\cS \cup \{ \bA_{{o}} \})$ or $\Gamma(\cS \cup \{ \nsim \bA_{{o}} \})$ The saturation condition 10. was required to properly establish the principle. However, since this condition is related to the proof theoretic notion of cut-elimination, it limits the utility of the principle in completeness proofs for machine-oriented calculi. The principle was nevertheless used in Benzmüller & Kohlhase 1998a and Benzmüller 1999a,b to obtain a completeness proof for a system of extensional higher-order resolution. The principle was also applied in Kohlhase 1998 to study completeness for a related extensional higher-order tableau calculus,[^note-2] in which the extensionality rules for Leibniz equality were adapted from Benzmüller & Kohlhase 1998a, respectively Benzmüller 1997.
- Different options for achieving a Unifying Principle for extensional type theory with primitive equality are presented in Benzmüller 1999a (in this work primitive logical constants $=_{{o}\alpha\alpha}$ were used in addition to $\nsim_{({o}{o})}, \lor_{(({o}{o}){o})}$, and the $\Pi_{({o}({o}\alpha))}$’s; such a redundant choice of logical constants is not rare in higher-order theorem provers). One option is to introduce a reflexivity and substitutivity condition. An alternative is to combine a reflexivity condition with a condition connecting primitive with defined equality, so that the substitutivity condition follows. Note that introducing a defined notion of equality based on the Leibniz principle is, of course, still possible in this context (defined equality is denoted in the remainder of this section by $\doteq$ to properly distinguish it from primitive equality $=$):
- Not $\Gamma(\cS \cup \{ \nsim [\bA_{\alpha} = \bA_{\alpha}] \})$
- If $\Gamma(\cS \cup \{ \bA_{\alpha} = \bA_{\alpha} \})$, then $\Gamma(\cS \cup \{ \bA_{\alpha} \doteq \bA_{\alpha} \})$
- $\Gamma(\cS \cup \{ \bA_{{o}} \})$ or $\Gamma(\cS \cup \{ \nsim \bA_{{o}} \})$ The saturation condition 10. still has to be added independent of which option is considered. The principle was applied in Benzmüller 1999a,b to prove completeness for the extensional higher-order RUE-resolution[^note-3] calculus underlying the higher-order automated theorem prover LEO and its successor LEO-II.
- In Benzmüller et al. 2004 the principle is presented in a very general way which allows for various possibilities concerning the treatment of extensionality and equality in the range between elementary type theory and extensional type theory. The principle is applied to obtain completeness proofs for an associated range of natural deduction calculi. The saturation condition is still used in this work.
- Based on insights from Brown’s (2004, 2007)[^brown-2004][^brown-2007] thesis, a solution for replacing the undesirable saturation condition by two weaker conditions is presented in Benzmüller, Brown, and Kohlhase 2009; this work also further studies the relation between saturation and cut-elimination. The two weaker conditions, termed mating and decomposition, are easier to demonstrate than saturation in completeness proofs for machine-oriented calculi. They are (omitting some type information in the second one and abusing notation):
- If $\Gamma(\cS \cup \{ \nsim \bA_{{o}}, \bB_{{o}} \})$ for atoms $\bA_{{o}}$ and $\bB_{{o}}$, then $\Gamma(\cS \cup \{ \nsim [\bA_{{o}} \doteq \bB_{{o}}] \})$
- If $\Gamma(\cS \cup \{ \nsim [h \overline{\bA^n_{\alpha^n}} \doteq h \overline{\bB^n_{\alpha^n}} ] \})$, where head symbol $h_{\beta\overline{\alpha^n}}$ is a parameter, then there is an $i\ (1 \leq i \leq n)$ such that $\Gamma(\cS \cup \{ \nsim [\bA^i_{\alpha^i} \doteq \bB^i_{\alpha^i}] \})$. The modified principle is applied in Benzmüller et al. 2009 to show completeness for a sequent calculus for extensional type theory with defined equality.
- A further extended Unifying Principle for extensional type theory with primitive equality is presented and used in Backes & Brown 2011 to prove the completeness of a tableau calculus for type theory which incorporates the axiom of choice.
- A closely related and further simplified principle has also been presented and studied in Steen 2018, where it was applied for showing completeness of the paramodulation calculus that is underlying the theorem prover Leo-III (Steen & Benzmüller 2018, 2021)[^steen-2018][^steen-2018-2][^steen-2021].

### 3.4 Cut-Elimination and Cut-Simulation

Cut-elimination proofs (see also the SEP entry on proof theory) for Church’s type theory, which are often closely related to such proofs (Takahashi 1967, 1970; Prawitz 1968; Mints 1999)[^mints-1999][^prawitz-1968][^takahashi-1967][^takahashi-1970] for other formulations of type theory, may be found in Andrews 1971, Dowek & Werner 2003, and Brown 2004. In Benzmüller et al. 2009 it is shown how certain wffs$_{{o}}$, such as axioms of extensionality, descriptions, choice (see Sections 1.3.3 to 1.3.5), and induction, can be used to justify cuts in cut-free sequent calculi for elementary type theory. Moreover, the notions of *cut-simulation* and *cut-strong axioms* are introduced in this work, and the need for omitting defined equality and for eliminating *cut-strong axioms* such as extensionality, description, choice and induction in machine-oriented calculi (e.g., by replacing them with more constrained, goal-directed rules) in order to reduce *cut-simulation* effects are discussed as a major challenge for higher-order automated theorem proving. In other words, including cut-strong axioms in a machine-oriented proof calculus for Church’s type theory is essentially as bad as including a cut rule, since the cut rule can be mimicked by them.

### 3.5 Expansion Proofs

An *expansion proof* is a generalization of the notion of a Herbrand expansion of a theorem of first-order logic; it provides a very elegant, concise, and nonredundant representation of the relationship between the theorem and a tautology which can be obtained from it by appropriate instantiations of quantifiers and which underlies various proofs of the theorem. Miller (1987)[^miller-1987] proved that a wff $\bA$ is a theorem of elementary type theory if and only if $\bA$ has an expansion proof.

In Brown 2004 and 2007, this concept is generalized to that of an *extensional expansion proof* to obtain an analogous theorem involving type theory with extensionality.

### 3.6 The Decision Problem

Since type theory includes first-order logic, it is no surprise that most systems of type theory are undecidable. However, one may look for solvable special cases of the decision problem. For example, the system $\cQ_{0}^1$ obtained by adding to $\cQ_0$ the additional axiom $\forall x_{\imath}\forall y_{\imath}[x_{\imath}=y_{\imath}]$ is decidable.

Although the system $\cT$ of elementary type theory is analogous to first-order logic in certain respects, it is a considerably more complex language, and special cases of the decision problem for provability in $\cT$ seem rather intractable for the most part. Information about some very special cases of this decision problem may be found in Andrews 1974, and we now summarize this.

A wff of the form $\exists \bx^1 \ldots \exists \bx^n [\bA=\bB]$ is a theorem of $\cT$ iff there is a substitution *θ* such that $\theta \bA \conv \theta \bB$. In particular, $\vdash \bA=\bB$ iff $\bA \conv \bB$, which solves the decision problem for wffs of the form $[\bA=\bB]$. Naturally, the circumstance that only trivial equality formulas are provable in $\cT$ changes drastically when axioms of extensionality are added to $\cT$. $\vdash \exists \bx_{\beta}[\bA=\bB]$ iff there is a wff $\bE_{\beta}$ such that $\vdash[\lambda \bx_{\beta}[\bA=\bB]]\bE_{\beta}$, but the decision problem for the class of wffs of the form $\exists \bx_{\beta}[\bA=\bB]$ is unsolvable.

A wff of the form $\forall \bx^1 \ldots \forall \bx^n\bC$, where $\bC$ is quantifier-free, is provable in $\cT$ iff ${\downarrow} \bC$ is tautologous. On the other hand, the decision problem for wffs of the form $\exists \bz\bC$, where $\bC$ is quantifier-free, is unsolvable. (By contrast, the corresponding decision problem in first-order logic with function symbols is known to be solvable (Maslov 1967)[^maslov-1967].) Since irrelevant or vacuous quantifiers can always be introduced, this shows that the only solvable classes of wffs of $\cT$ in prenex normal form defined solely by the structure of the prefix are those in which no existential quantifiers occur.

## 4. Automation

### 4.1 Machine-Oriented Proof Calculi

The development, respectively improvement, of machine-oriented proof calculi for Church’s type theory has made good progress in recent years; see, e.g., the references on superposition based calculi given below. The challenges are obviously much bigger than in first-order logic. The practically way more expressive nature of the term-language of Church’s type theory causes a larger, bushier and more difficult to traverse proof search space than in first-order logic. Moreover, remember that unification, which constitutes a very important control and filter mechanism in first-order theorem proving, is undecidable (in general) in type theory; see Section 3.2. On the positive side, however, there is a chance to find significantly shorter proofs than in first-order logic. This is well illustrated with a small, concrete example in Boolos 1987, for which a fully automated proof seems now in reach (Benzmüller et al. 2023)[^benzmüller-2023].

Clearly, further progress is needed to further leverage the practical relevance of existing calculi for Church’s type theory and their implementations (see Section 4.3). The challenges include

- an appropriate handling of the impredicative nature of Church’s type theory (some form of blind guessing cannot generally be avoided in a complete proof procedure, but must be intelligently guided),
- the elimination/reduction of cut-simulation effects (see Section 3.4) caused by defined equality or cut-strong axioms (e.g., extensionality, description, choice, induction) in the search space,
- the general undecidability of unification, rendering it a rather problematic filter mechanism for controlling proof search,
- the invention of suitable heuristics for traversing the search space,
- the provision of suitable term-orderings and their effective exploitation in term rewriting procedures,
- and efficient data structures in combination with strong technical support for essential operations such λ-conversion, substitution and rewriting.

It is planned that future editions of this article further elaborate on machine-oriented proof calculi for Church’s type theory. For the time being, however, we provide only a selection of historical and more recent references for the interested reader (see also Section 5 below):

- **Sequent calculi:** Schütte 1960; Takahashi 1970; Takeuti 1987; Mints 1999; Brown 2004, 2007; Benzmüller et al. 2009.
- **Mating method:** Andrews 1981; Bibel 1981; Bishop 1999.
- **Resolution calculi:** Andrews 1971; Huet 1973a; Jensen & Pietrzykowski 1976; Benzmüller 1997, 1999a; Benzmüller & Kohlhase 1998a.
- **Tableau method:** Kohlhase[^note-4] 1995, 1998; Brown & Smolka 2010; Backes & Brown 2011.
- **Paramodulation calculi:** Benzmüller 1999a,b; Steen 2018, Steen & Benzmüller 2018, 2021.
- **Superposition calculi:** Bentkamp et al. 2018, Bentkamp et al. 2021, Bentkamp et al. 2023a,c
- **Combinator-based superposition calculi:** Bhayat & Reger 2020

### 4.2 Proof Assistants

Early computer systems for proving theorems of Church’s type theory (or extensions of it) include HOL (Gordon 1988; Gordon & Melham 1993)[^gordon-1988][^gordon-1993], TPS (Andrews et al. 1996; Andrews & Brown 2006)[^andrews-1996][^andrews-2006], Isabelle (Paulson 1988, 1990)[^paulson-1988][^paulson-1990], PVS (Owre et al. 1996; Shankar 2001)[^owre-1996][^shankar-2001], IMPS (Farmer et al. 1993)[^farmer-1993], HOL Light (Harrison 1996)[^harrison-1996], OMEGA (Siekmann et al. 2006)[^siekmann-2006], and λClam (Richardson et al. 1998)[^richardson-1998]. Prominent proof assistents that support more powerful dependent type theory include Coq (Bertot & Castéran 2004)[^bertot-2004] and the recent Lean system (de Moura & Ullrich 2021). See Other Internet References section below for links to further info on these and other provers mentioned later.

Most of the early systems mentioned above focused (at least initially) on interactive proof. However, the TPS project in particular had been working since the mid-1980s on the integration of ND-style interactive proof and automated theorem proving using the mating method, and had investigated proof transformation techniques between the two. This research was further intensified in the 1990s, when other projects investigated various solutions such as proof planning and bridges to external theorem provers using so-called hammer tools. The hammers developed at that time were early precursors of todays very successful hammer tools such as Sledgehammer, HolyHammer and related systems (Blanchette et al. 2013, Kaliszyk & Urban 2015 and Czaika & Kaliszyk 2018)[^blanchette-2013][^kaliszyk-2015].

While, triggered by the mentioned dynamics, some first initial progress was made in the late 80s and during the 90s with regards to the automation of Church’s type theory, the resource investments and achievements at the time were lacking much behind those seen, for example, in first-order theorem proving. Good progress was fostered only later, in particular, through the development of a commonly supported syntax for Church’s type theory, called TPTP THF (Sutcliffe & Benzmüller 2010, Sutcliffe 2022)[^sutcliffe-2010], and the inclusion, from 2009 onwards, of a TPTP THF division in the yearly CASC competitions (kind of world championships for automated theorem proving; see Sutcliffe 2016 for further details)[^sutcliffe-2016]. These competitions, in combination with further factors, triggered an increasing interest in the full automation of Church’s type theory. Particularly successful was recently the exploration of equality based theorem proving using the superposition approach and the adaptation of SMT techniques to HOL.

### 4.3 Automated Theorem Provers

A selection of theorem provers for Church's type theory is presented. The focus is on systems that have successfully participated in TPTP THF CASC competitions in the past, and the order of presentation is motivated by their first-time CASC participation. The latest editions of most mentioned systems can be accessed online via the SystemOnTPTP infrastructure (Sutcliffe 2017)[^sutcliffe-2017]. Nearly all mentioned systems produce verifiable proof certificates in the TPTP TSTP syntax.

The TPS prover (Andrews et al. 1996, Andrews & Brown 2006)[^andrews-1996][^andrews-2006] can be used to prove theorems of elementary type theory or extensional type theory automatically, interactively, or semi-automatically. When searching for a proof automatically, TPS first searches for an expansion proof (Miller 1987)[^miller-1987] or an extensional expansion proof (Brown 2004, 2007)[^brown-2004][^brown-2007] of the theorem. Part of this process involves searching for acceptable matings (Andrews 1981, Bishop 1999)[^andrews-1981][^bishop-1999]. The behavior of TPS is controlled by sets of flags, also called modes. A simple scheduling mechanism is employed in the latest versions of TPS to sequentially run a about fifty modes for a limited amount of time. TPS was the winner of the first THF CASC competition in 2009.

The LEO-II prover (Benzmüller et al. 2015)[^benzmüller-2015] is the successor of LEO (Benzmüller & Kohlhase 1998b, which was hardwired with the OMEGA proof assistant (LEO stands for Logical Engine of OMEGA). The provers are based on the RUE-resolution calculi developed in Benzmüller 1999a,b. LEO was the first prover to implement calculus rules for extensionality to avoid cut-simulation effects. LEO-II inherits and adapts them, and provides additional calculus rules for description and choice. The prover, which internally collaborates with first-order provers (preferably E) and SAT solvers, has pioneered cooperative higher-order/first-order proof automation. Since the prover is often too weak to find a refutation among the steadily growing set of clauses on its own, some of the clauses in LEO-II’s search space attain a special status: they are first-order clauses modulo the application of an appropriate transformation function. Therefore, LEO-II progressively launches time limited calls with these clauses to a first-order theorem prover, and when the first-order prover reports a refutation, LEO-II also terminates. Parts of these ideas were already implemented in the predecessor LEO. Communication between LEO-II and the cooperating first-order theorem provers uses the TPTP language and standards. LEO-II was the winner of the second THF CASC competition in 2010.

The Satallax prover (Brown 2012)[^brown-2012] is based on a complete ground tableau calculus for Church’s type theory with choice (Backes & Brown 2011)[^backes-2011]. An initial tableau branch is formed from the assumptions of a conjecture and negation of its conclusion. From that point on, Satallax tries to determine unsatisfiability or satisfiability of this branch. Satallax progressively generates higher-order formulas and corresponding propositional clauses. Satallax uses the SAT solver MiniSat as an engine to test the current set of propositional clauses for unsatisfiability. If the clauses are unsatisfiable, the original branch is unsatisfiable. Satallax provides calculus rules for extensionality, description and choice. If there are no quantifiers at function types, the generation of higher-order formulas and corresponding clauses may terminate. In that case, if MiniSat reports the final set of clauses as satisfiable, then the original set of higher-order formulas is satisfiable (by a standard model in which all types are interpreted as finite sets). Satallax was the winner of the THF CASC competition in 2011 and from 2013 to 2019

The Isabelle/HOL system (Nipkow, Wenzel, & Paulson 2002)[^nipkow-2002] has originally been designed as an interactive prover. However, in order to ease user interaction several automatic proof tactics have been added over the years. By appropriately scheduling a subset of these proof tactics, some of which are quite powerful, Isabelle/HOL has since about 2011 been turned also into an automatic theorem prover for TPTP THF (and other TPTP syntax formats), that can be run from a command shell like other provers. The most powerful proof tactics that are scheduled by Isabelle/HOL include the Sledgehammer tool (Blanchette et al. 2013)[^blanchette-2013], which invokes a sequence of external first-order and higher-order theorem provers, the model finder *Nitpick* (Blanchette & Nipkow 2010)[^blanchette-2010], the equational reasoner *simp*, the untyped tableau prover *blast*, the simplifier and classical reasoners *auto*, *force*, and *fast*, and the best-first search procedure *best*. In contrast to all other automated theorem provers mentioned above, the TPTP incarnation of Isabelle/HOL does not output proof certificates. Isabelle/HOL was the winner of the THF CASC competition in 2012.

The agsyHOL prover is based on a generic lazy narrowing proof search algorithm. Backtracking is employed and a comparably small search state is maintained. The prover outputs proof terms in sequent style which can be verified in the Agda system.

coqATP implements (the non-inductive) part of the calculus of constructions (Bertot & Castéran 2004)[^bertot-2004]. The system outputs proof terms which are accepted as proofs (after the addition of a few definitions) by the Coq proof assistant. The prover employs axioms for functional extensionality, choice, and excluded middle. Boolean extensionality is not supported. In addition to axioms, a small library of basic lemmas is employed.

The Leo-III prover implements a paramodulation calculus for Church’s type theory (Steen 2018)[^steen-2018][^steen-2018-2]. The system, which is a descendant of LEO and LEO-II, provides calculus rules for extensionality, description and choice. The system has put an emphasis on the implementation of an efficient set of underlying data structures, on simplification routines and on heuristic rewriting. In the tradition of its predecessors, Leo-III cooperates with first-order reasoning tools using translations to many-sorted first-order logic. The prover accepts every common TPTP syntax dialect and is thus very widely applicable. Recently, the prover has also been extended to natively supports almost every normal higher-order modal logic (Steen et al. 2023)[^steen-2023].

CVC4, CVC5 and Verit (Barbosa et al. 2019)[^barbosa-2019] are SMT-based automated provers with built-in support for many theories, including linear arithmetic, arrays, bit vectors, data types, finite sets and strings. These provers have been extended to support (fragments of) Church's type theory.

The Zipperposition prover (Bentkamp et al. 2018, Vukmirović et al. 2022)[^bentkamp-2018][^vukmirović-2022] focuses on the effective implementation of superposition calculi for Church's type theory. It comes with Logtk, a supporting library for manipulating terms, formulas, clauses, etc. in Church's type theory, and supports relevant extensions such as datatypes, recursive functions, and arithmetic. Zipperposition was the winner of the THF CASC competition in 2020, 2021 and 2022.

Vampire (Bhayat & Reger 2020)[^bhayat-2020], which has dominated the TPTP competitions in first-order logic for more than two decades, now also supports the automation of Church's type theory using a combinator-based superposition calculus. Vampire was the winner of the THF CASC competition in 2023.

The theorem prover E (Vukmirović et al. 2023)[^vukmirović-2023], another prominent and leading first-order automated theorem prover, has been extended for Church's type theory using a variant of the supperposition approach that is also implemented in Zipperposition.

Lash (Brown and Kaliszyk 2022) is a theorem prover for Church's type theory created as a fork of Satallax.

Duper is a superposition-based theorem prover for dependent type theory, deigned to prove theorems in the proof assistant Lean.

In recent years, there has thus been a significant shift from first-order to higher-order automated theorem proving.

### 4.4 (Counter-)Model Finding

Support for finding finite models or countermodels for formulas of Church’s type theory was implemented already in the tableau-based prover HOT (Konrad 1998)[^konrad-1998]. Restricted (counter-)model finding capabilities are also implemented in the provers Satallax, LEO-II and LEO-III. The most advanced (finite) model finding support is currently realized in the systems Nitpick, Nunchaku and Refute. These tools have been integrated with the Isabelle proof assistant. Nitpick is also available as a standalone tool that accepts TPTP THF syntax. The systems are particularly valuable for exposing errors and misconceptions in problem encodings, and for revealing bugs in the THF theorem provers.

## 5. Applications

In addition to its elegance, Church's type theory also has many practical advantages. This aspect is emphasised, for example, in the recent textbook by Farmer (2023)[^farmer-2023], which deals with various relevant and important further aspects that could not be covered in this article. Because of its good practical expressiveness, the range of applications of Church's type theory is very wide, and only a few examples can be given below (a good source for further information on practical examples are the proceedings of the conferences on Interactive Theorem Proving).

### 5.1 Semantics of Natural Language

Church’s type theory plays an important role in the study of the formal semantics of natural language. Pioneering work on this was done by Richard Montague. See his papers “English as a formal language”, “Universal grammar”, and “The proper treatment of quantification in ordinary English”, which are reprinted in Montague 1974. A crucial component of Montague’s analysis of natural language is the definition of a tensed intensional logic (Montague 1974: 256)[^montague-1974], which is an enhancement of Church’s type theory. Montague Grammar had a huge impact, and has since been developed in many further directions, not least in Typelogical/Categorical Grammar. Further related work on intensional and higher-order modal logic is presented in Gallin 1975 and Muskens 2006.

### 5.2 Mathematics and Computer Science

Proof assistants based on Church’s Type Theory, including Isabelle/HOL, HOL Light, HOL4, and PVS, have been successfully utilized in a broad range of application in computer science and mathematics.

Applications in computer science include the verification of hardware, software and security protocols. A prominent example is the L4.verified project in which Isabelle/HOL was used to formally prove that the seL4 operating system kernel implements an abstract, mathematical model specifying of what the kernel is supposed to do (Klein et al. 2018)[^klein-2018].

In mathematics proof assistants have been applied for the development of libraries mathematical theories and the verification of challenge theorems. An early example is the mathematical library that was developed since the eighties in the TPS project. A exemplary list of theorems that were proved automatically with TPS is given in Andrews et al. 1996. A very prominent recent example is Hales Flyspeck in which HOL Light was employed to develop a formal proof for Kepler’s conjecture (Hales et al. 2017)[^hales-2017]. An example that strongly exploits automation support in Isabelle/HOL with Sledgehammer and Nitpick is presented in Benzmüller & Scott 2019. In this work different axiom systems for category theory were explored and compared.

A solid overview of past and ongoing formalization projects can be obtained by consulting appropriate sources such as Isabelle's Archive of Formal Proofs, the Journal of Formalized Reasoning, or the THF entries in Sutcliffe's TPTP problem library. Relevant further information and a discussion of implications and further work can also be found in Bentkamp et al. 2023b and in Bayer et al. 2024.

Further improving proof automation within these proof assistants—based on proof hammering tools or on other forms of prover integration—is relevant for minimizing interaction effort in future applications.

### 5.3 Computational Metaphysics and Artificial Intelligence

Church’s type theory is a classical logic, but topical applications in philosophy and artificial intelligence often require expressive non-classical logics. In order to support such applications with reasoning tools for Church’s type theory, the shallow semantical embedding technique (see also Section 1.2.2) has been developed that generalizes and extends the ideas underlying the well known standard translation of modal logics to first-order logic. The technique was applied for the assessment of modern variants of the ontological argument with a range of higher-order theorem provers, including LEO-II, Satallax, Nitpick and Isabelle/HOL. In the course of experiments, LEO-II detected an inconsistency in the premises of Gödel’s argument, while the provers succeeded in automatically proving Scott’s emendation of it and to confirm the consistency of the emended premises. More details on this work are presented in a related SEP entry on automated reasoning (see Section 4.6 on Logic and Philosophy). The semantical embedding approach has been adapted and further extended for a range of other non-classical logics and related applications. In philosophy this includes the encoding and formal assessment of ambitious ethical and metaphysical theories, and in artificial intelligence this includes the mechanization of deontic logics and normative reasoning to control AI systems (Benzmüller et al. 2020)[^benzmüller-2020] as well as an automatic proof of the muddy children puzzle (see Appendix B of dynamic epistemic logic), which is a famous puzzle in epistemic reasoning, respectively dynamic epistemic reasoning.

### 5.4. Metalogical Studies

Church’s type theory is also well suited to support metalogical studies, including the encoding of other logical formalisms and formalized soundness and completeness studies (see, e.g., Schlichtkrull et al. 2020, Halkjær et al. 2023, and various further pointers given in Benzmüller 2019)[^benzmüller-2019][^benzmüller-2019-2][^halkjær-2023][^schlichtkrull-2023][^schlichtkrull-2020]. In particular, Church's type theory can be studied formally in itself, as shown, for example, by Kumar et al. (2016), Schlichtkrull (2023)[^schlichtkrull-2023], and Díaz (2023)[^díaz-2023].

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=type-theory-church). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/type-theory-church/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=type-theory-church&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/type-theory-church/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

Since several sections in the main text mention software projects, we provide links to these projects below; some are duplicated because they are cited in multiple sections of the main text.

- 4.2 Proof Assistants
- [HOL](http://www.cl.cam.ac.uk/Research/HVG/HOL/)
- [TPS](http://gtps.math.cmu.edu/tps.html)
- [Isabelle/HOL](https://isabelle.in.tum.de)
- [PVS](http://www.csl.sri.com/projects/pvs/)
- [IMPS](https://github.com/theoremprover-museum/imps)
- [OMEGA](https://github.com/theoremprover-museum/OMEGA/blob/master/prog/top/omega-top.lisp)
- [λClam](http://dream.inf.ed.ac.uk/software/lambda-clam/)
- [HOL light](https://www.cl.cam.ac.uk/~jrh13/hol-light/)
- [Coq](https://coq.inria.fr)
- [Lean](https://lean-lang.org/)
- [Agda](http://hackage.haskell.org/package/Agda)
- [Sledgehammer](https://isabelle.in.tum.de/website-Isabelle2009-1/sledgehammer.html)
- [HOL(y)Hammer](http://cl-informatik.uibk.ac.at/software/hh/)
- [SystemOnTPTP](http://www.tptp.org/cgi-bin/SystemOnTPTP) (system platform)
- [TPTP TSTP](http://www.tptp.org/TSTP/) (proof format)
- 4.3 Automated Theorem Provers and Related Tools
- [TPTP CASC](http://www.tptp.org/CASC/) (competition)
- [TPS](http://gtps.math.cmu.edu/tps.html)
- [LEO-II](http://www.leoprover.org/)
- [Satallax](http://www.ps.uni-saarland.de/~cebrown/satallax/)
- [Isabelle/HOL](https://isabelle.in.tum.de)
- [agsyHOL](https://github.com/frelindb/agsyHOL)
- [Leo-III](http://github.com/leoprover/Leo-III)
- [CVC4](https://cvc4.github.io/)
- [CVC5](https://cvc5.github.io)
- [Zipperposition](https://github.com/c-cube/zipperposition)
- [Vampire](https://vprover.github.io/)
- [E](https://wwwlehre.dhbw-stuttgart.de/~sschulz/E/E.html)
- [Lash](http://grid01.ciirc.cvut.cz/~chad/lash/)
- [Duper](https://github.com/leanprover-community/duper)
- 4.4 (Counter-)Model Finding
- [Nitpick](https://isabelle.in.tum.de/doc/nitpick.pdf)
- [Nunchaku](https://github.com/nunchaku-inria)
- 5.2 Mathematics and Computer Science
- [sel4](https://sel4.systems/)
- [Flyspeck](https://github.com/flyspeck/flyspeck)
- [Archive of Formal Proofs](https://www.isa-afp.org)
- [Journal of Formalized Reasoning](https://jfr.unibo.it/issue/view/615)
- [TPTP problem library](http://tptp.org)

## Related Entries

artificial intelligence: logic-based | category theory | choice, axiom of | descriptions | epsilon calculus | Frege, Gottlob | Gödel, Kurt: incompleteness theorems | grammar: typelogical | lambda calculus, the | logic, history of: first-order logic | logic: classical | logic: deontic | logic: dynamic epistemic | logic: modal | logic: second-order and higher-order | metaphysics | ontological arguments | paradox: Skolem’s | paradoxes: and contemporary logic | possibilism-actualism debate | possible worlds | *Principia Mathematica* | proof theory | quantifiers and quantification | Quine, Willard Van Orman | rational choice, normative: expected utility | reasoning: automated | Russell, Bertrand | semantics: Montague | Tarski, Alfred | type theory

### Acknowledgments

Portions of this material are adapted from Andrews 2002 and Andrews 2001, with permission from the author and Elsevier. Benzmüller received funding for his contribution from Volkswagen Foundation.

## Notes（原文脚注）

[^note-1]: They, e.g., do not entail the saturation and reflexivity properties given below.

[^note-2]: The calculus in Kohlhase 1998 is technically still flawed; e.g., to guarantee soundness Skolemization must be used in rule $\textit{SIM}(\textit{fun})$.

[^note-3]: RUE stands for resolution by unification and equality.

[^note-4]: Different to what is claimed, the presented rules fail to capture an exhaustive extensionality treatment, and so did their implementation in the prover HOT (Konrad 1998)[^konrad-1998]; see the respective comment on this in Benzmüller 1997; there are also some soundness issues.

[^andrews-1963]: Andrews, Peter B., 1963, “A Reduction of the Axioms for the Theory of Prepositional Types”, *Fundamenta Mathematicae*, 52(3): 345–350. doi:10.4064/fm-52-3-345-350

[^andrews-1971]: –––, 1971, “Resolution in Type Theory”, *The Journal of Symbolic Logic*, 36(3): 414–432. Reprinted in Siekmann & Wrightson 1983 and in Benzmüller et al. 2008. doi:10.2307/2269949 doi:10.1007/978-3-642-81955-1

[^andrews-1972a]: –––, 1972a, “General Models and Extensionality”, *The Journal of Symbolic Logic*, 37(2): 395–397. Reprinted in Benzmüller et al. 2008. doi:10.2307/2272982

[^andrews-1972b]: –––, 1972b, “General Models, Descriptions, and Choice in Type Theory”, *The Journal of Symbolic Logic*, 37(2): 385–394. Reprinted in Benzmüller et al. 2008. doi:10.2307/2272981

[^andrews-1974]: –––, 1974, “Provability in Elementary Type Theory”, *Zeitschrift für Mathematische Logik und Grundlagen der Mathematik*, 20(25–27): 411–418. doi:10.1002/malq.19740202506

[^andrews-1981]: –––, 1981, “Theorem Proving via General Mappings”, *Journal of the ACM*, 28(2): 193–214. doi:10.1145/322248.322249

[^andrews-2001]: –––, 2001, “Classical Type Theory”, in Robinson and Voronkov 2001, Volume 2, Chapter 15, pp. 965–1007. doi:10.1016/B978-044450813-3/50017-5

[^andrews-2002]: –––, 2002, *An Introduction to Mathematical Logic and Type Theory: To Truth Through Proof*, (Applied Logic Series 27), second edition, Dordrecht: Springer Netherlands. doi:10.1007/978-94-015-9934-4

[^andrews-1996]: Andrews, Peter B., Matthew Bishop, Sunil Issar, Dan Nesmith, Frank Pfenning, and Hongwei Xi, 1996, “TPS: A Theorem-Proving System for Classical Type Theory”, *Journal of Automated Reasoning*, 16(3): 321–353. Reprinted in Benzmüller et al. 2008. doi:10.1007/BF00252180

[^andrews-2006]: Andrews, Peter B. and Chad E. Brown, 2006, “TPS: A Hybrid Automatic-Interactive System for Developing Proofs”, *Journal of Applied Logic*, 4(4): 367–395. doi:10.1016/j.jal.2005.10.002

[^baader-2001]: Baader, Franz and Wayne Snyder, 2001, “Unification Theory”, in Robinson and Voronkov 2001, Volume 1, Chapter 8, Amsterdam: Elsevier Science, pp. 445–533. doi:10.1016/B978-044450813-3/50010-2

[^backes-2011]: Backes, Julian and Chad Edward Brown, 2011, “Analytic Tableaux for Higher-Order Logic with Choice”, *Journal of Automated Reasoning*, 47(4): 451–479. doi:10.1007/s10817-011-9233-2

[^barbosa-2019]: Barbosa, Haniel, Andrew Reynolds, Daniel El Ouraoui, Cesare Tinelli, and Clark Barret, 2019, “Extending SMT Solvers to Higher-Order Logic”, in *Automated Deduction – CADE 27,* Pascal Fontaine (ed.), (Lecture Notes in Computer Science 11716), Cham: Springer Nature Switzerland AG. doi:10.1007/978-3-030-29436-6_3

[^barendregt-1984]: Barendregt, H. P., 1984, *The Lambda Calculus: Its Syntax and Semantics*, (Studies in Logic and the Foundations of Mathematics, 103), revised edition, Amsterdam: North-Holland.

[^barendregt-2013]: Barendregt, Henk, Wil Dekkers, and Richard Statman, 2013, *Lambda Calculus with Types*, Cambridge: Cambridge University Press. doi:10.1017/CBO9781139032636

[^bayer-2024]: Bayer, Jonas, Christoph Benzmüller, Kevin Buzzard, Marco David, Leslie Lamport, Yuri Matiyasevich, Lawrence Paulson, Dierk Schleicher, Benedikt Stock, and Efim Zelmanov, 2024, “Mathematical Proof Between Generations”, *Notices of the AMS*, 71(1):80-92. doi:10.1090/noti2860

[^bentkamp-2018]: Bentkamp, Alexander, Jasmin Blanchette, Simon Cruanes, and Uwe Waldmann, 2018, “Superposition for Lambda-Free Higher-Order Logic”, in Galmiche et al. 2018: 28–46. doi:10.1007/978-3-319-94205-6_3

[^bentkamp-2023a]: Bentkamp, Alexander, Jasmin Blanchette, Visa Nummelin, Sophie Tourret, and Uwe Waldmann, 2023a, “Complete and Efficient Higher-Order Reasoning via Lambda-Superposition”. *ACM SIGLOG News* 10(4):25–40. doi:10.1145/3636362.3636367

[^bentkamp-2023b]: Bentkamp, Alexander, Jasmin Blanchette, Visa Nummelin, Sophie Tourret, Petar Vukmirovic, and Uwe Waldmann, 2023b, “Mechanical Mathematicians” *Communications of the ACM, 66*(4):80–90. doi:10.1145/3636362.3636367

[^bentkamp-2023c]: Bentkamp, Alexander, Jasmin Blanchette, Sophie Tourret, and Petar Vukmirovic, 2023c, “Superposition for Higher-Order Logic”, *Journal of Automated Reasoning*, 67(1):10. doi:10.1007/s10817-022-09649-9

[^bentkamp-2021]: Bentkamp, Alexander, Jasmin Blanchette, Sophie Tourret, Petar Vukmirovic, and Uwe Waldmann, 2021, “Superposition with Lambdas”,*Journal of Automated Reasoning*, 65, 893–940. doi:10.1007/s10817-021-09595-y

[^benzmüller-1997]: Benzmüller, Christoph, 1997, *A Calculus and a System Architecture for Extensional Higher-Order Resolution*, Technical report 97–198, Department of Mathematical Sciences, Carnegie Mellon University. doi:10.1184/r1/6476477.v1

[^benzmüller-1999a]: –––, 1999a, *Equality and Extensionality in Automated Higher-Order Theorem Proving*, Ph.D. dissertation, Computer Science Department, Universität des Saarlandes.

[^benzmüller-1999b]: –––, 1999b, “Extensional Higher-Order Paramodulation and RUE-Resolution”, in Ganzinger 1999: 399–413. doi:10.1007/3-540-48660-7_39

[^benzmüller-2019]: –––, 2019, “Universal (Meta-)Logical Reasoning: Recent Successes”, *Science of Computer Programming*, 172: 48–62. doi:10.1016/j.scico.2018.10.008

[^benzmüller-1997-2]: Benzmüller, Christoph and Michael Kohlhase, 1997, “Model Existence for Higher Order Logic”. SEKI Report SR-97-09.

[^benzmüller-1998a]: –––, 1998a, “Extensional Higher-Order Resolution”, Kirchner and Kirchner 1998: 56–71. doi:10.1007/BFb0054248

[^benzmüller-1998b]: –––, 1998b, “System Description: Leo—A Higher-Order Theorem Prover”, in Kirchner and Kirchner 1998: 139–143. doi:10.1007/BFb0054256

[^benzmüller-2004]: Benzmüller, Christoph, Chad E. Brown, and Michael Kohlhase, 2004, “Higher-Order Semantics and Extensionality”, *The Journal of Symbolic Logic*, 69(4): 1027–1088. doi:10.2178/jsl/1102022211

[^benzmüller-2009]: –––, 2009, “Cut-Simulation and Impredicativity”, *Logical Methods in Computer Science*, 5(1): 6. doi:10.2168/LMCS-5(1:6)2009

[^benzmüller-2008]: Benzmüller, Christoph, Chad E. Brown, Jörg Siekmann, and Richard Statman (eds.), 2008, *Reasoning in Simple Type Theory: Festschrift in Honour of Peter B. Andrews on His 70th Birthday*, (Studies in Logic 17), London: College Publications.

[^benzmüller-2023]: Benzmüller, Christoph, David Fuenmayor, Alexander Steen, and Geoff Sutcliffe, 2023, “Who Finds the Short Proof?”, *Logic Journal of the IGPL*. doi:10.1093/jigpal/jzac082

[^benzmüller-2014]: Benzmüller, Christoph and Dale Miller, 2014, “Automation of Higher Order Logic”, in *Computational Logic*, (Handbook of the History of Logic, 9), Dov M. Gabbay, Jörg H. Siekmann, and John Woods (eds.), Amsterdam: Elsevier, 215–254.

[^benzmüller-2020]: Benzmüller, Christoph, Xavier Parent, and Leendert van der Torre, 2020, “Designing normative theories for ethical and legal reasoning: LogiKEy framework, methodology, and tool support, *Artificial Intelligence*, 287:103348. doi:10.1016/j.artint.2020.103348

[^benzmüller-2015]: Benzmüller, Christoph, Nik Sultana, Lawrence C. Paulson, and Frank Theiß, 2015, “The Higher-Order Prover Leo-II”, *Journal of Automated Reasoning*, 55(4): 389–404. doi:10.1007/s10817-015-9348-y

[^benzmüller-2019-2]: Benzmüller, Christoph and Dana S. Scott, 2019, “Automating Free Logic in HOL, with an Experimental Application in Category Theory”, *Journal of Automated Reasoning*, 64:53–72 (2020). doi:10.1007/s10817-018-09507-7

[^benzmüller-2014-2]: Benzmüller, Christoph and Bruno Woltzenlogel Paleo, 2014, “Automating Gödel’s Ontological Proof of God’s Existence with Higher-Order Automated Theorem Provers”, in *Proceedings of the Twenty-First European Conference on Artificial Intelligence (ECAI 2014)*, T. Schaub, G. Friedrich, and B. O’Sullivan (eds.), (Frontiers in Artificial Intelligence 263), Amsterdam: IOS Press, 93–98. doi:10.3233/978-1-61499-419-0-93

[^bertot-2004]: Bertot, Yves and Pierre Castéran, 2004, *Interactive Theorem Proving and Program Development: Coq’Art: The Calculus of Inductive Constructions*, (Texts in Theoretical Computer Science An EATCS Series), Berlin, Heidelberg: Springer Berlin Heidelberg. doi:10.1007/978-3-662-07964-5

[^bhayat-2020]: Bhayat, Ahmed and Giles Reger, 2020, “A Combinator-Based Superposition Calculus for Higher-Order Logic”, in Automated Reasoning. IJCAR 2020, Nicolas Peltier and Sofronie-Stokkermans (eds.), (Lecture Notes in Computer Science 12166), Cham: Springer Nature Switzerland AG. doi:10.1007/978-3-030-51074-9_16

[^bibel-1981]: Bibel, Wolfgang, 1981, “On Matrices with Connections”, *Journal of the ACM*, 28(4): 633–645. doi:10.1145/322276.322277

[^bishop-1999]: Bishop, Matthew, 1999, “A Breadth-First Strategy for Mating Search”, in Ganzinger 1999: 359–373. doi:10.1007/3-540-48660-7_32

[^blanchette-2010]: Blanchette, Jasmin Christian and Tobias Nipkow, 2010, “Nitpick: A Counterexample Generator for Higher-Order Logic Based on a Relational Model Finder”, in *Interactive Theorem Proving*, Matt Kaufmann and Lawrence C. Paulson (eds.), (Lecture Notes in Computer Science 6172), Berlin, Heidelberg: Springer Berlin Heidelberg, 131–146. doi:10.1007/978-3-642-14052-5_11

[^blanchette-2013]: Blanchette, Jasmin Christian, Sascha Böhme, and Lawrence C. Paulson, 2013, “Extending Sledgehammer with SMT Solvers”, *Journal of Automated Reasoning*, 51(1): 109–128. doi:10.1007/s10817-013-9278-5

[^boolos-1987]: Boolos, George, 1987, “A Curious Inference”, *Journal of Philosophical Logic*, 16(1): 1–12. doi:10.1007/BF00250612

[^brown-2004]: Brown, Chad E., 2004, “Set Comprehension in Church’s Type Theory”, PhD Thesis, Department of Mathematical Sciences, Carnegie Mellon University, Pittsburgh, PA.

[^brown-2007]: –––, 2007, *Automated Reasoning in Higher-Order Logic: Set Comprehension and Extensionality in Church`s Type Theory*, (Studies in Logic Logic and Cognitive Systems 10), London: King’s College Publications.

[^brown-2012]: –––, 2012, “Satallax: An Automatic Higher-Order Prover”, in *Automated Reasoning (IJCAR 2012)*, Bernhard Gramlich, Dale Miller, and Uli Sattler (eds.) (Lecture Notes in Computer Science 7364), Berlin, Heidelberg: Springer Berlin Heidelberg, 111–117. doi:10.1007/978-3-642-31365-3_11

[^brown-2010]: Brown, Chad and Gert Smolka, 2010, “Analytic Tableaux for Simple Type Theory and Its First-Order Fragment”, *Logical Methods in Computer Science*, 6(2): 3. doi:10.2168/LMCS-6(2:3)2010

[^büchi-1953]: Büchi, J. Richard, 1953, “Investigation of the Equivalence of the Axiom of Choice and Zorn’s Lemma from the Viewpoint of the Hierarchy of Types”, *The Journal of Symbolic Logic*, 18(2): 125–135. doi:10.2307/2268945

[^church-1932]: Church, Alonzo, 1932, “A Set of Postulates for the Foundation of Logic”, *The Annals of Mathematics*, 33(2): 346–366. doi:10.2307/1968337

[^church-1940]: –––, 1940, “A Formulation of the Simple Theory of Types”, *The Journal of Symbolic Logic*, 5(2): 56–68. Reprinted in Benzmüller et al. 2008. doi:10.2307/2266170

[^church-1941]: –––, 1941, *The Calculi of Lambda Conversion*, (Annals of Mathematics Studies 6), Princeton, NJ: Princeton University Press.

[^church-1956]: –––, 1956, *Introduction to Mathematical Logic*, Princeton, NJ: Princeton University Press.

[^czajka-2018]: Czajka, Łukasz and Cezary Kaliszyk, 2018, “Hammer for Coq: Automation for Dependent Type Theory”, *Journal of Automated Reasoning*, 61(1–4): 423–453. doi:10.1007/s10817-018-9458-4

[^díaz-2023]: Díaz, Javier, 2023, “Metatheory of Q0”, *Archive of Formal Proofs*. https://www.isa-afp.org/entries/Q0_Metatheory.html

[^dowek-2001]: Dowek, Gilles, 2001, “Higher-Order Unification and Matching”, in Robinson and Voronkov 2001, Volume 2, Chapter 16, Amsterdam: Elsevier Science, pp. 1009–1062. doi:10.1016/B978-044450813-3/50018-7

[^dowek-2003]: Dowek, Gilles and Benjamin Werner, 2003, “Proof Normalization Modulo”, *The Journal of Symbolic Logic*, 68(4): 1289–1316. doi:10.2178/jsl/1067620188

[^farmer-2008]: Farmer, William M., 2008, “The Seven Virtues of Simple Type Theory”, *Journal of Applied Logic*, 6(3): 267–286. doi:10.1016/j.jal.2007.11.001

[^farmer-2023]: Farmer, William M., 2023, “Simple Type Theory - A Practical Logic for Expressing and Reasoning About Mathematical Ideas”, Cham: Birkhäuser. doi:10.1007/978-3-031-21112-6

[^farmer-1993]: Farmer, William M., Joshua D. Guttman, and F. Javier Thayer, 1993, “IMPS: An Interactive Mathematical Proof System”, *Journal of Automated Reasoning*, 11(2): 213–248. doi:10.1007/BF00881906

[^gallin-1975]: Gallin, Daniel, 1975, *Intensional and Higher-Order Modal Logic*, Amsterdam: North-Holland.

[^galmiche-2018]: Galmiche, Didier, Stephan Schulz, and Roberto Sebastiani (eds.), 2018, *Automated Reasoning (IJCAR 2018)*, (Lecture Notes in Computer Science 10900), Cham: Springer International Publishing. doi:10.1007/978-3-319-94205-6

[^ganzinger-1999]: Ganzinger, Harald (ed.), 1999, *Automated Deduction—CADE-16*, (Lecture Notes in Computer Science, 1632), Berlin, Heidelberg: Springer Berlin Heidelberg. doi:10.1007/3-540-48660-7

[^gödel-1931]: Gödel, Kurt, 1931, “Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I”, *Monatshefte für Mathematik und Physik*, 38(1): 173–198. Translated in Gödel 1986: 144–195, and in van Heijenoort 1967: 596–616.

[^gödel-1986]: –––, 1986, *Collected Works*, Volume I, Oxford: Oxford University Press.

[^goldfarb-1981]: Goldfarb, Warren D., 1981, “The Undecidability of the Second-Order Unification Problem”, *Theoretical Computer Science*, 13(2): 225–230. doi:10.1016/0304-3975(81)90040-2

[^gordon-1986]: Gordon, Michael J. C., 1986, “Why Higher-Order Logic is a Good Formalism for Specifying and Verifying Hardware”, in George J. Milne, and P. A. Subrahmanyam (eds.), *Formal Aspects of VLSI Design: Proceedings of the 1985 Edinburgh Workshop on VLSI*, Amsterdam: North-Holland, pp. 153–177.

[^gordon-1988]: –––, 1988, “HOL: A Proof Generating System for Higher-Order Logic”, in *VLSI Specification, Verification and Synthesis*, Graham Birtwistle and P. A. Subrahmanyam (eds.), (The Kluwer International Series in Engineering and Computer Science 35), Boston, MA: Springer US, 73–128. doi:10.1007/978-1-4613-2007-4_3

[^gordon-1993]: Gordon, M. J., and T. F. Melham, 1993, *Introduction to HOL: A Theorem-Proving Environment for Higher-Order Logic*, Cambridge: Cambridge University Press.

[^gould-1966]: Gould, William Eben, 1966, *A Matching Procedure for *ω*-order Logic*, Ph.D. dissertation, Mathematics Department, Princeton University. [[Gould 1966 available online](https://apps.dtic.mil/sti/citations/AD0646560)]

[^hales-2017]: Hales, Thomas, Mark Adams, Gertrud Bauer, Tat Dat Dang, John Harrison, Le Truong Hoang, Cezary Kaliszyk, et al., 2017, “A Formal Proof of the Kepler Conjecture”, *Forum of Mathematics, Pi*, 5: e2. doi:10.1017/fmp.2017.1

[^harrison-1996]: Harrison, John, 1996, “HOL Light: A Tutorial Introduction”, in *Formal Methods in Computer-Aided Design*, Mandayam Srivas and Albert Camilleri (eds.), (Lecture Notes in Computer Science 1166), Berlin, Heidelberg: Springer Berlin Heidelberg, 265–269. doi:10.1007/BFb0031814

[^halkjær-2023]: Halkjær, Asta, Anders Schlichtkrull, Jørgen Villadsen, 2023, “A sequent calculus for first-order logic formalized in Isabelle/HOL”, *Journal of Logic and Computation,* 33(4):818-836. doi: 10.1093/logcom/exad013

[^henkin-1950]: Henkin, Leon, 1950, “Completeness in the Theory of Types”, *The Journal of Symbolic Logic*, 15(2): 81–91. Reprinted in Hintikka 1969 and in Benzmüller et al. 2008. doi:10.2307/2266967

[^henkin-1963]: –––, 1963, “A Theory of Prepositional Types”, *Fundamenta Mathematicae*, 52(3): 323–344. doi:10.4064/fm-52-3-323-344

[^henkin-1975]: –––, 1975, “Identity as a Logical Primitive”, *Philosophia*, 5(1–2): 31–45. doi:10.1007/BF02380832

[^hilbert-1928]: Hilbert, David, 1928, “Die Grundlagen der Mathematik”, *Abhandlungen aus dem mathematischen Seminar der Hamburgischen Universität*, 6: 65–85; translated in van Heijenoort 1967: 464–479.

[^hintikka-1969]: Hintikka, Jaakko (ed.), 1969, *The Philosophy of Mathematics*, Oxford: Oxford University Press.

[^huet-1973a]: Huet, Gerald P., 1973a, “A Mechanization of Type Theory”, in *Proceedings of the Third International Joint Conference on Artificial Intelligence* (Stanford University), D. E. Walker and L. Norton (eds.), Los Altos, CA: William Kaufman, 139–146. [[Huet 1973a available online](https://www.ijcai.org/Proceedings/73/Papers/016.pdf)]

[^huet-1973b]: –––, 1973b, “The Undecidability of Unification in Third Order Logic”, *Information and Control*, 22(3): 257–267. doi:10.1016/S0019-9958(73)90301-X

[^huet-1975]: –––, 1975, “A Unification Algorithm for Typed λ-Calculus”, *Theoretical Computer Science*, 1(1): 27–57. doi:10.1016/0304-3975(75)90011-0

[^jensen-1976]: Jensen, D.C. and T. Pietrzykowski, 1976, “Mechanizing ω-Order Type Theory through Unification”, *Theoretical Computer Science*, 3(2): 123–171. doi:10.1016/0304-3975(76)90021-9

[^kaliszyk-2015]: Kaliszyk, Cezary and Josef Urban, 2015, “HOL(y)Hammer: Online ATP Service for HOL Light”, *Mathematics in Computer Science*, 9(1): 5–22. doi:10.1007/s11786-014-0182-0

[^kirchner-1998]: Kirchner, Claude and Hélène Kirchner (eds.), 1998, *Automated Deduction—CADE-15*, (Lecture Notes in Computer Science, 1421), Berlin, Heidelberg: Springer Berlin Heidelberg. doi:10.1007/BFb0054239

[^klein-2018]: Klein, Gerwin, June Andronick, Matthew Fernandez, Ihor Kuz, Toby Murray, and Gernot Heiser, 2018, “Formally Verified Software in the Real World”, *Communications of the ACM*, 61(10): 68–77. doi:10.1145/3230627

[^kohlhase-1993]: Kohlhase, Michael, 1993, “A Unifying Principle for Extensional Higher-Order Logic”, Technical Report 93–153, Department of Mathematics, Carnegie Mellon University.

[^kohlhase-1995]: –––, 1995, “Higher-Order Tableaux”, in *Theorem Proving with Analytic Tableaux and Related Methods*, Peter Baumgartner, Reiner Hähnle, and Joachim Possega (eds.), (Lecture Notes in Computer Science 918), Berlin, Heidelberg: Springer Berlin Heidelberg, 294–309. doi:10.1007/3-540-59338-1_43

[^kohlhase-1998]: –––, 1998, “Higher-Order Automated Theorem Proving”, in *Automated Deduction—A Basis for Applications*, Volume 1, Wolfgang Bibel and Peter H. Schmitt (eds.), Dordrecht: Kluwer, 431–462.

[^konrad-1998]: Konrad, Karsten, 1998, “Hot: A Concurrent Automated Theorem Prover Based on Higher-Order Tableaux”, in *Theorem Proving in Higher Order Logics*, Jim Grundy and Malcolm Newey (eds.), (Lecture Notes in Computer Science 1479), Berlin, Heidelberg: Springer Berlin Heidelberg, 245–261. doi:10.1007/BFb0055140

[^kumar-2016]: Kumar, Ramana, Rob Arthan, Magnus O. Myreen, and Scott Owens, 2016, “Self-Formalisation of Higher-Order Logic”, *Journal of Automated Reasoning*, **56**:221–259. doi:10.1007/s10817-015-9357-x

[^maslov-1967]: Maslov, S. Yu, 1967, “An Inverse Method for Establishing Deducibility of Nonprenex Formulas of Predicate Calculus”, *Soviet Mathematics Doklady*, 8(1): 16–19.

[^miller-1983]: Miller, Dale A., 1983, *Proofs in Higher-Order Logic*, Ph.D. dissertation, Mathematics Department, Carnegie Mellon University.

[^miller-1987]: –––, 1987, “A Compact Representation of Proofs”, *Studia Logica*, 46(4): 347–370. doi:10.1007/BF00370646

[^miller-1991]: –––, 1991, “A Logic Programming Language with Lambda-Abstraction, Function Variables, and Simple Unification”, *Journal of Logic and Computation*, 1(4): 497–536. doi:10.1093/logcom/1.4.497

[^mints-1999]: Mints, G., 1999, “Cut-Elimination for Simple Type Theory with an Axiom of Choice”, *The Journal of Symbolic Logic*, 64(2): 479–485. doi:10.2307/2586480

[^montague-1974]: Montague, Richard, 1974, *Formal Philosophy. Selected Papers Of Richard Montague*, edited and with an introduction by Richmond H. Thomason, New Haven: Yale University Press.

[^muskens-2006]: Muskens, Reinhard, 2006, “Higher Order Modal Logic”, in *Handbook of Modal Logic*, Patrick Blackburn, Johan Van Benthem, and Frank Wolter (eds.), Amsterdam: Elsevier, 621–653.

[^muskens-2007]: –––, 2007, “Intensional Models for the Theory of Types”, *The Journal of Symbolic Logic*, 72(1): 98–118. doi:10.2178/jsl/1174668386

[^nipkow-2002]: Nipkow, Tobias, Markus Wenzel, and Lawrence C. Paulson (eds.), 2002, *Isabelle/HOL: A Proof Assistant for Higher-Order Logic*, (Lecture Notes in Computer Science 2283), Berlin, Heidelberg: Springer Berlin Heidelberg. doi:10.1007/3-540-45949-9

[^owre-1996]: Owre, S., S. Rajan, J. M. Rushby, N. Shankar, and M. Srivas, 1996, “PVS: Combining Specification, Proof Checking, and Model Checking”, in *Computer Aided Verification*, Rajeev Alur and Thomas A. Henzinger (eds.), (Lecture Notes in Computer Science 1102), Berlin, Heidelberg: Springer Berlin Heidelberg, 411–414. doi:10.1007/3-540-61474-5_91

[^paulson-1988]: Paulson, Lawrence C, 1988, “Isabelle: The next Seven Hundred Theorem Provers”, in *9th International Conference on Automated Deduction*, Ewing Lusk and Ross Overbeek (eds.), (Lecture Notes in Computer Science 310), Berlin/Heidelberg: Springer-Verlag, 772–773. doi:10.1007/BFb0012891

[^paulson-1990]: –––, 1990, “A Formulation of the Simple Theory of Types (for Isabelle)”, in *COLOG-88*, Per Martin-Löf and Grigori Mints (eds.), (Lecture Notes in Computer Science 417), Berlin, Heidelberg: Springer Berlin Heidelberg, 246–274. doi:10.1007/3-540-52335-9_58

[^prawitz-1968]: Prawitz, Dag, 1968, “Hauptsatz for Higher Order Logic”, *The Journal of Symbolic Logic*, 33(3): 452–457. doi:10.2307/2270331

[^quine-1956]: Quine, W. V., 1956, “Unification of Universes in Set Theory”, *The Journal of Symbolic Logic*, 21(3): 267–279. doi:10.2307/2269102

[^richardson-1998]: Richardson, Julian, Alan Smaill, and Ian Green, 1998, “System Description: Proof Planning in Higher-Order Logic with ΛClam”, in Kirchner and Kirchner 1998: 129–133. doi:10.1007/BFb0054254

[^robinson-2001]: Robinson, Alan and Andrei Voronkov (eds.), 2001, *Handbook of Automated Reasoning*, Volumes 1 and 2, Amsterdam: Elsevier Science.

[^russell-1903]: Russell, Bertrand, 1903, *The Principles of Mathematics*, Cambridge: Cambridge University Press.

[^russell-1908]: –––, 1908, “Mathematical Logic as Based on the Theory of Types”, *American Journal of Mathematics*, 30(3): 222–262. Reprinted in van Heijenoort 1967: 150–182. doi:10.2307/2369948

[^schlichtkrull-2023]: Schlichtkrull, Anders, 2023, “Soundness of the Q0 proof system for higher-order logic”, *Archive of Formal Proofs.* https://www.isa-afp.org/entries/Q0_Soundness.html

[^schlichtkrull-2020]: Schlichtkrull, Anders, Jasmin Blanchette, Dmitriy Traytel, and Uwe Waldmann, 2020, “Formalizing Bachmair and Ganzinger's Ordered Resolution Prover.” Journal of Automated Reasoning, 64(7): 1169-1195. doi:10.1007/s10817-020-09561-0

[^schönfinkel-1924]: Schönfinkel, M., 1924, “Über die Bausteine der mathematischen Logik”, *Mathematische Annalen*, 92(3–4): 305–316. Translated in van Heijenoort 1967: 355–366. doi:10.1007/BF01448013

[^schütte-1960]: Schütte, Kurt, 1960, “Syntactical and Semantical Properties of Simple Type Theory”, *The Journal of Symbolic Logic*, 25(4): 305–326. doi:10.2307/2963525

[^shankar-2001]: Shankar, Natarajan, 2001, “Using Decision Procedures with a Higher-Order Logic”, in *Theorem Proving in Higher Order Logics*, Richard J. Boulton and Paul B. Jackson (eds.), (Lecture Notes in Computer Science 2152), Berlin, Heidelberg: Springer Berlin Heidelberg, 5–26. doi:10.1007/3-540-44755-5_3

[^siekmann-1983]: Siekmann, Jörg H. and Graham Wrightson (eds.), 1983, *Automation of Reasoning*, (Classical Papers on Computational Logic 1967–1970: Vol. 2), Berlin, Heidelberg: Springer Berlin Heidelberg. doi:10.1007/978-3-642-81955-1

[^siekmann-2006]: Siekmann, Jörg, Christoph Benzmüller, and Serge Autexier, 2006, “Computer Supported Mathematics with ΩMEGA”, *Journal of Applied Logic*, 4(4): 533–559. doi:10.1016/j.jal.2005.10.008

[^smullyan-1963]: Smullyan, Raymond M., 1963, “A Unifying Principal in Quantification Theory”, *Proceedings of the National Academy of Sciences*, 49(6): 828–832. doi:10.1073/pnas.49.6.828

[^smullyan-1995]: –––, 1995, *First-Order Logic*, New York: Dover, second corrected edition.

[^steen-2018]: Steen, Alexander, 2018, *Extensional Paramodulation for Higher-Order Logic and its Effective Implementation Leo-III*, Ph.D. dissertation, Series: Dissertations in Artificial Intelligence (DISKI), Volume 345, Berlin: AKA-Verlag (IOS Press).

[^steen-2018-2]: Steen, Alexander and Christoph Benzmüller, 2018, “The Higher-Order Prover Leo-III”, in Galmiche et al. 2018: 108–116. doi:10.1007/978-3-319-94205-6_8

[^steen-2021]: Steen, Alexander and Christoph Benzmüller, 2021, “Extensional Higher-Order Paramodulation in Leo-III”, *Journal of Automated Reasoning,* 65: 775–807. doi:10.1007/s10817-021-09588-x

[^steen-2023]: Steen, Alexander, Geoff Sutcliffe, Tobias Scholl, Christoph Benzmüller, 2023, “Solving Modal Logic Problems by Translation to Higher-Order Logic”, in *Logic and Argumentation. CLAR 2023,* Andreas Herzig, Jieting Luo, Pere Pardo (eds.), (Lecture Notes in Computer Science 14156), Cham: Springer Nature Switzerland AG. doi:10.1007/978-3-031-40875-5_3

[^stenlund-1972]: Stenlund, Sören, 1972, *Combinators, λ-Terms and Proof Theory*, (Synthese Library 42), Dordrecht: Springer Netherlands. doi:10.1007/978-94-010-2913-1

[^sutcliffe-2016]: Sutcliffe, Geoff, 2016, “The CADE ATP System Competition—CASC”, *AI Magazine*, 37(2): 99–101. doi:10.1609/aimag.v37i2.2620

[^sutcliffe-2017]: –––, 2017, “The TPTP Problem Library and Associated Infrastructure: From CNF to TH0, TPTP v6.4.0”, *Journal of Automated Reasoning*, 59(4): 483–502. doi:10.1007/s10817-017-9407-7

[^sutcliffe-2023]: –––, 2023, “The logic languages of the TPTP world”, *Logic Journal of the IGPL*, 31(6): 1153–1169. doi:10.1093/jigpal/jzac068

[^sutcliffe-2010]: Sutcliffe, Geoff and Christoph Benzmüller, 2010, “Automated Reasoning in Higher-Order Logic Using the TPTP THF Infrastructure”, *Journal of Formalized Reasoning*, 3(1): 1–27. doi:10.6092/issn.1972-5787/1710

[^takahashi-1967]: Takahashi, Moto-o, 1967, “A Proof of Cut-Elimination Theorem in Simple Type-Theory”, *Journal of the Mathematical Society of Japan*, 19(4): 399–410. doi:10.2969/jmsj/01940399

[^takahashi-1970]: –––, 1970, “A System of Simple Type Theory of Gentzen Style with Inference on Extensionality, and the Cut Elimination in It”, *Commentarii Mathematici Universitatis Sancti Pauli*, 18(2):129–147.

[^takeuti-1987]: Takeuti, Gaisi, 1987, *Proof Theory*, second edition, Amsterdam: North-Holland.

[^tarski-1923]: Tarski, Alfred [Tajtelbaum, Alfred], 1923, “Sur Le Terme Primitif de La Logistique”, *Fundamenta Mathematicae*, 4: 196–200. Translated in Tarski 1956, 1–23. doi:10.4064/fm-4-1-196-200

[^tarski-1956]: –––, 1956, *Logic, Semantics, Metamathematics: Papers from 1923 to 1938*, Oxford: Oxford University Press.

[^heijenoort-1967]: van Heijenoort, Jean, 1967, *From Frege to Gödel. A Source Book in Mathematical Logic 1879–1931*, Cambridge, MA: Harvard University Press.

[^vukmirović-2022]: Vukmirović, Petar, Alexander Bentkamp, Jasmin Blanchette, Simon Cruanes, Visa Nummelin, and Sophie Tourret, 2022, “Making Higher-Order Superposition Work”, *Journal of Automated Reasoning,* 66:541–564. doi10.1007/s10817-021-09613-z

[^vukmirović-2023]: Vukmirović, Petar, Jasmin Blanchette, and Stephan Schulz, 2023, “Extending a High-Performance Prover to Higher-Order Logic”, in *Tools and Algorithms for the Construction and Analysis of Systems. TACAS 2023*, Sankaranarayanan, S., Sharygina, N. (eds.), (Lecture Notes in Computer Science 13994), Cham: Springer Nature Switzerland AG. doi:10.1007/978-3-031-30820-8_10

[^whitehead-1927a]: Whitehead, Alfred N. and Bertrand Russell, 1927a, *Principia Mathematica*, Volume 1, Cambridge: Cambridge University Press, second edition.

[^whitehead-1927b]: –––, 1927b, “Incomplete Symbols”, in Whitehead & Russell 1927a: 66–84; reprinted in van Heijenoort 1967: 216–223.

[^yasuhara-1975]: Yasuhara, Mitsuru, 1975, “The Axiom of Choice in Church’s Type Theory” (abstract), *Notices of the American Mathematical Society*, 22(January): A34. [[Yashuhara 1975 available online](https://www.ams.org/journals/notices/197501/197501FullIssue.pdf)]
