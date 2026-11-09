# Hybrid Logic
**First published Tue Jun 13, 2006; substantive revision Wed Dec 22, 2021**

*Braüner, Torben*

Hybrid logics are logics that result by adding further expressive power to ordinary modal logic. The most basic hybrid logic is obtained by adding so-called nominals which are propositional symbols of a new sort, each being true at exactly one possible world. The history of hybrid logic goes back to Arthur N. Prior’s work in the 1960s.

## 1. Motivations for hybrid logic

In the standard Kripke semantics for modal logic, truth is relative to points in a set. Thus, a propositional symbol might have different truth-values relative to different points. Usually, these points are taken to represent possible worlds, times, epistemic states, states in a computer, or something else. This allows us to formalize natural language statements whose truth-values are relative to for example times, like the statement

> It is raining.

which clearly has different truth-values at different times. Now, certain natural language statements are true at exactly one time, possible world, or something else. An example is the statement

> It is five o’clock 15 November 2021.

which is true at the time five o’clock 15 November 2021, but false at all other times. The first kind of natural language statements can be formalized in ordinary modal logic, but the second kind cannot.

A major motivation for hybrid logic is to add further expressive power to ordinary modal logic with the aim of being able to formalize the second kind of statements. This is obtained by adding to ordinary modal logic a second sort of propositional symbols called *nominals* such that in the Kripke semantics each nominal is true relative to exactly one point. A natural language statement of the second kind (like the example statement with the time five o’clock 15 November 2021) is then formalized using a nominal, not an ordinary propositional symbol (which would be used to formalize the example statement with rainy weather). The fact that a nominal is true relative to exactly one point implies that a nominal can be considered a term referring to a point, for example, if $\mathtt{a}$ is a nominal that stands for “it is five o’clock 15 November 2021”, then this nominal can be considered a term referring to the time five o’clock 15 November 2021. Thus, in hybrid logic a term is a specific sort of propositional symbol whereas in first-order logic it is an argument to a predicate.

Most hybrid logics involve further additional machinery than nominals. There is a number of options for such additions; here we shall consider what are called *satisfaction operators*. The motivation for adding satisfaction operators is to be able to formalize a statement being true at a particular time, possible world, or something else. For example, we want to be able to formalize that the statement “it is raining” is true at the time five o’clock 15 November 2021, that is, that

> At five o’clock 15 November 2021, it is raining.

This is formalized by the formula $\mathtt{@_a p}$ where the nominal $\mathtt{a}$ stands for “it is five o’clock 15 November 2021” as above and where $\mathtt{p}$ is an ordinary propositional symbol that stands for “it is raining”. It is the part $\mathtt{@_a}$ of the formula $\mathtt{@_a p}$ that is called a satisfaction operator. In general, if $\mathtt{a}$ is a nominal and $\mathtt{\phi}$ is an arbitrary formula, then a new formula $\mathtt{@_a\phi}$ called a *satisfaction statement* can be built. The satisfaction statement $\mathtt{@_a\phi}$ expresses that the formula $\mathtt{\phi}$ is true relative to one particular point, namely the point to which the nominal $\mathtt{a}$ refers.

To sum up, we have now added further expressive power to ordinary modal logic in the form of nominals and satisfaction operators. Informally, the nominal $\mathtt{a}$ has the truth-condition

> $\mathtt{a}$ is true relative to a point $w$     if and only if the reference of $\mathtt{a}$ is identical to $w$.

and the satisfaction statement $\mathtt{@_a\phi}$ has the truth-condition

> $\mathtt{@_a\phi}$ is true relative to a point $w$     if and only if $\mathtt{\phi}$ is true relative to the reference of $\mathtt{a}$.

Note that actually the point $w$ does not matter in the truth-condition for $\mathtt{@_a\phi}$ since the satisfaction operator $\mathtt{@_a}$ moves the point of evaluation to the reference of $\mathtt{a}$ whatever $w$ is.

It is remarkable that nominals together with satisfaction operators allow us to express that two points are identical: If the nominals $\mathtt{a}$ and $\mathtt{b}$ refer to the points $w$ and $v$, then the formula $\mathtt{@_a b}$ expresses that $w$ and $v$ are identical. The following line of reasoning shows why.

> $\mathtt{@_a b}$ is true relative to a point $w$     if and only if $\mathtt{b}$ is true relative to the reference of $\mathtt{a}$     if and only if $\mathtt{b}$ is true relative to $w$     if and only if the reference of $\mathtt{b}$ is identical to $w$     if and only if $v$ is identical to $w$.

The identity relation on a set has the well-known properties reflexivity, symmetry, and transitivity, which is reflected in the fact that the formulas

$$\begin{align*} & \mathtt{@_a a} \\ & \mathtt{@_a b \rightarrow @_b a} \\ &(\mathtt{@_a b \amp @_b c) \rightarrow @_a c} \end{align*}$$

are valid formulas of hybrid logic. Also the formula

$$ (\mathtt{@_ab \amp @_a\phi) \rightarrow @_b\phi} $$

is valid. This is the rule of replacement. Note the similarity to the formula $\mathtt{(a=b \amp \phi(a)) \rightarrow \phi(b)}$ in first-order logic with equality (commonly called Leibniz’ Law).

Beside nominals and satisfaction operators, in what follows we shall consider the so-called *binders* $\mathtt{\forall}$ and $\mathtt{\downarrow}$ allowing us to build formulas $\mathtt{\forall a \phi}$ and $\mathtt{{\downarrow} a \phi}$. The binders bind nominals to points in two different ways: The $\mathtt{\forall}$ binder quantifies over points analogous to the standard first-order universal quantifier, that is, $\mathtt{\forall a \phi}$ is true relative to $w$ if and only if whatever point the nominal $\mathtt{a}$ refers to, it is the case that $\mathtt{\phi}$ is true relative to $w$. The $\mathtt{\downarrow}$ binder binds a nominal to the point of evaluation, that is, $\mathtt{{\downarrow} a \phi}$ is true relative to $w$ if and only if $\mathtt{\phi}$ is true relative to $w$ when $\mathtt{a}$ refers to $w$. It turns out that the $\mathtt{\downarrow}$ binder is definable in terms of $\mathtt{\forall}$ (as shown below).

## 2. Formal semantics

The language we consider is the language of ordinary modal logic built over ordinary propositional symbols $\mathtt{p}, \mathtt{q}, \mathtt{r}, …$ as well as nominals $\mathtt{a}, \mathtt{b}, \mathtt{c}, …$ and extended with satisfaction operators and binders. We take the propositional connectives $\mathtt{\wedge}$ and $\mathtt{\neg}$ to be primitive; other propositional connectives are defined as usual. Similarly, we take the modal operator $\mathtt{\Box}$ to be primitive and define the modal operator $\mathtt{\Diamond}$ as $\mathtt{\neg \Box \neg}$. As the name suggests, binders bind nominals and the notions of free and bound occurrences of nominals are defined analogously to first-order logic. Satisfaction operators do not bind nominals, that is, the free nominal occurrences in a formula $\mathtt{@_a \phi}$ are the free nominal occurrences in $\mathtt{\phi}$ together with the occurrence of $\mathtt{a}$. We let $\mathtt{\phi[c/a]}$ be the formula $\mathtt{\phi}$ where the nominal $\mathtt{c}$ has been substituted for all free occurrences of the nominal $\mathtt{a}$. If the nominal $\mathtt{a}$ occurs free in $\mathtt{\phi}$ within the scope of $\mathtt{\forall c}$ or $\mathtt{{\downarrow} c}$, then the bound nominal $\mathtt{c}$ in $\mathtt{\phi}$ is renamed as appropriate.

We now define models and frames. A *model* for hybrid logic is a triple $(W, R, V)$ where $W$ is a non-empty set, $R$ is a binary relation on $W$, and $V$ is a function that assigns an element of the set $\{0,1\}$ to each pair consisting of an element of $W$ and an ordinary propositional symbol. The pair $(W, R)$ is called a *frame*. Thus, models and frames are the same as in ordinary modal logic. The elements of $W$ are called *worlds* and the relation $R$ is called the *accessibility relation*. The model $(W, R, V)$ is said to be *based* on the frame $(W, R)$.

An *assignment* for a model $M = (W, R, V)$ is a function $g$ that assigns an element of $W$ to each nominal. An assignment $g'$ is an $\mathtt{a}$*-variant* of $g$ if $g'$ agrees with $g$ on all nominals save possibly $\mathtt{a}$. The relation $M, g, w \vDash \phi$ is defined by induction, where $g$ is an assignment, $w$ is an element of $W$, and $\mathtt{\phi}$ is a formula.

> $M, g, w \vDash \mathtt{p}$ iff $V(w, \mathtt{p})=1$ $M, g, w \vDash \mathtt{a}$ iff $w = g(\mathtt{a})$ $M, g, w \vDash \mathtt{\phi \wedge \psi}$ iff $M, g, w \vDash \mathtt{\phi}$ and $M, g, w \vDash \mathtt{\psi}$ $M, g, w \vDash \mathtt{\neg \phi}$ iff not $M, g, w \vDash \mathtt{\phi}$ $M, g, w \vDash \mathtt{\Box} \phi$ iff for any element $v$ of $W$ such that $wRv$, it is the case that $M, g, v \vDash \mathtt{\phi}$ $M, g, w \vDash \mathtt{@_a \phi}$ iff $M, g, g(\mathtt{a}) \vDash \mathtt{\phi}$ $M, g, w \vDash \mathtt{\forall a\phi}$ iff for any $\mathtt{a}$-variant $g'$ of $g$, it is the case that $M, g', w \vDash \mathtt{\phi}$ $M, g, w \vDash \mathtt{{\downarrow} a\phi}$ iff $M, g', w \vDash \mathtt{\phi}$ where $g'$ is the $\mathtt{a}$-variant of $g$ such that $g'(\mathtt{a}) = w$.

A formula $\mathtt{\phi}$ is said to be *true* at $w$ if $M, g, w \vDash \mathtt{\phi}$; otherwise it is said to be *false* at $w$. By convention $M, g \vDash \mathtt{\phi}$ means $M, g, w \vDash \mathtt{\phi}$ for every element $w$ of $W$ and $M \vDash \mathtt{\phi}$ means $M, g \vDash \mathtt{\phi}$ for every assignment $g$. A formula $\mathtt{\phi}$ is *valid* in a frame if and only if $M \vDash \mathtt{\phi}$ for any model $M$ that is based on the frame in question. A formula $\mathtt{\phi}$ is *valid* in a class of frames $F$ if and only if $ \mathtt{\phi}$ is valid in any frame in $F$. A formula $\mathtt{\phi}$ is *valid* if and only if $\mathtt{\phi}$ is valid in the class of all frames. The definition of satisfiability is left to the reader.

Note that the binder $\mathtt{\downarrow}$ is definable in terms of $\mathtt{\forall}$ as the formula $\mathtt{{\downarrow} a\phi \leftrightarrow \forall a(a \rightarrow \phi)}$ is valid in any frame.

The fact that hybridizing ordinary modal logic actually does give more expressive power can, for example, be seen by considering the formula $\mathtt{{\downarrow} c\Box \neg c}$. It is straightforward to check that this formula is valid in a frame if and only if the frame is irreflexive. Thus, irreflexivity can be expressed by a hybrid-logical formula, but it is well known that it cannot be expressed by any formula of ordinary modal logic. Irreflexivity can actually be expressed just by adding nominals to ordinary modal logic, namely by the formula $\mathtt{c\rightarrow \Box \neg c}$. Other examples of properties expressible in hybrid logic, but not in ordinary modal logic, are asymmetry (expressed by $\mathtt{c \rightarrow \Box \neg \Diamond c }$), antisymmetry (expressed by $\mathtt{c\rightarrow \Box(\Diamond c \rightarrow c)}$), and universality (expressed by $\mathtt{\Diamond c}$).

See the handbook chapter Areces and ten Cate (2006) for a detailed account of the syntax and semantics of hybrid logic, as well as many other basic definitions. The syntax and semantics above can be extended in a number of ways, in particular, first-order quantification can be added (of course, an equivalent way to obtain first-order hybrid logic is by adding hybrid-logical machinery to first-order modal logic). See Braüner (2014) for an overview of first-order hybrid logic, see Chapter 6 of Braüner (2011a) for a more detailed account, and see Chapter 7 of Braüner (2011a) for an account of intensional first-order hybrid logic.

## 3. Translations

Hybrid logic can be translated into first-order logic with equality, and (a fragment of) first-order logic with equality can be translated back into (a fragment of) hybrid logic. The first-order language under consideration has a 1-place predicate symbol $\mathtt{p^*}$ corresponding to each ordinary propositional symbol $\mathtt{p}$ of modal logic, a 2-place predicate symbol $\mathtt{R}$, and a 2-place predicate symbol $\mathtt{=}$. Of course, the predicate symbol $\mathtt{p^*}$ will be interpreted such that it relativises the interpretation of the corresponding modal propositional symbol $\mathtt{p}$ to worlds, the predicate symbol $\mathtt{R}$ will be interpreted using the accessibility relation, and the predicate symbol $\mathtt{=}$ will be interpreted using the identity relation on worlds. We let $\mathtt{a}, \mathtt{b}, \mathtt{c},\ldots$ range over first-order variables. The language does not have constant or function symbols. We shall identify first-order variables with nominals of hybrid logic.

We first translate hybrid logic into first-order logic with equality. Given two new first-order variables $\mathtt{a}$ and $\mathtt{b}$, the translations $\mathrm{ST}_\mathtt{a}$ and $\mathrm{ST}_\mathtt{b}$ are defined by mutual recursion. We just give the translation $\mathrm{ST}_\mathtt{a}$.

$$\begin{align*} \mathrm{ST}_\mathtt{a} (\mathtt{p}) &= \mathtt{p^*(a)} \\ \mathrm{ST}_\mathtt{a} (\mathtt{c}) &= \mathtt{a=c} \\ \mathrm{ST}_\mathtt{a} (\mathtt{\phi \wedge \psi}) &= \mathrm{ST}_\mathtt{a} (\mathtt{\phi}) \mathtt{\wedge} \mathrm{ST}_\mathtt{a} (\mathtt{\psi}) \\ \mathrm{ST}_\mathtt{a} (\mathtt{\neg \phi}) &= \mathtt{\neg} \mathrm{ST}_\mathtt{a}(\phi) \\ \mathrm{ST}_\mathtt{a} (\mathtt{\Box \phi}) &= \mathtt{\forall b(R(a, b) \rightarrow} \mathrm{ST}_\mathtt{b} (\mathtt{\phi})\mathtt{)} \\ \mathrm{ST}_\mathtt{a} (\mathtt{@_c \phi}) &= \mathrm{ST}_\mathtt{a} (\mathtt{\phi})[\mathtt{c}/\mathtt{a}] \\ \mathrm{ST}_\mathtt{a} (\mathtt{{\downarrow} c\phi}) &= \mathrm{ST}_\mathtt{a} (\mathtt{\phi})[\mathtt{a}/\mathtt{c}] \\ \mathrm{ST}_\mathtt{a} (\mathtt{\forall c\phi}) &= \mathtt{\forall c }\mathrm{ST}_\mathtt{a} (\mathtt{\phi}) \end{align*}$$

The definition of $\mathrm{ST}_\mathtt{b}$ is obtained by exchanging $\mathtt{a}$ and $\mathtt{b}$. The translation is an extension of the well-known *standard translation* from modal logic into first-order logic. As an example, we demonstrate step by step how the hybrid-logical formula $\mathtt{{\downarrow} c\Box \neg c}$ is translated into a first-order formula:

$$\begin{align*} \mathrm{ST}_\mathtt{a} (\mathtt{{\downarrow} c\Box \neg c}) &= \mathrm{ST}_\mathtt{a} (\mathtt{\Box \neg c})[\mathtt{a}/\mathtt{c}] \\ &= \mathtt{\forall b(R(a, b) \rightarrow } \mathrm{ST}_\mathtt{b} (\mathtt{\neg c})\mathtt{)}[\mathtt{a}/\mathtt{c}] \\ &= \mathtt{\forall b(R(a, b) \rightarrow \neg } \mathrm{ST}_\mathtt{b} (\mathtt{c})\mathtt{)}[\mathtt{a}/\mathtt{c}] \\ &= \mathtt{\forall b(R(a, b) \rightarrow \neg b=c)}[\mathtt{a}/\mathtt{c}] \\ &= \mathtt{\forall b(R(a, b) \rightarrow \neg b=a)}. \end{align*}$$

The resulting first-order formula is equivalent to $\mathtt{\neg R(a, a)}$ which shows that $\mathtt{{\downarrow} c\Box \neg c}$ indeed does correspond to the accessibility relation being irreflexive, cf. above.

First-order logic with equality can be translated back into hybrid logic by the translation HT given below.

$$\begin{align*} \mathrm{HT}(\mathtt{p^*(a)}) &= \mathtt{@_a p} \\ \mathrm{HT}(\mathtt{R(a, c)}) &= \mathtt{@_a \Diamond c} \\ \mathrm{HT}(\mathtt{a=c}) &= \mathtt{@_a c} \\ \mathrm{HT}(\mathtt{\phi \wedge \psi}) &= \mathrm{HT}(\mathtt{\phi}) \mathtt{\wedge} \mathrm{HT}(\mathtt{\psi}) \\ \mathrm{HT}(\mathtt{\neg \phi}) &= \mathtt{\neg} \mathrm{HT}(\mathtt{\phi}) \\ \mathrm{HT}(\mathtt{\forall a\phi}) &= \mathtt{\forall a} \mathrm{HT}(\mathtt{\phi}) \end{align*}$$

Note that the hybrid-logical binder $\mathtt{\forall}$ is needed. The history of the above mentioned observations goes back to the work of Arthur N. Prior, we shall return to that later.

Similarly, what is called the *bounded fragment* of first-order logic can be translated into the hybrid logic but here only the binder $\mathtt{\downarrow}$ is needed, as pointed out in the paper Areces, Blackburn, and Marx (2001). The bounded fragment is the fragment of first-order logic with the property that quantifiers only occur as in the formula $\mathtt{\forall c(R(a, c) \rightarrow \phi)}$, where it is required that the variables $\mathtt{a}$ and $\mathtt{c}$ are different. A translation from the bounded fragment to the hybrid logic without the $\mathtt{\forall}$ binder can be obtained by replacing the last clause in the translation HT above by

$$ \mathrm{HT}(\mathtt{\forall c(R(a, c) \rightarrow \phi)}) = \mathtt{@_a \Box {\downarrow} c}\mathrm{HT}(\mathtt{\phi}). $$

In Areces, Blackburn, and Marx (2001) a number of independent semantic characterisations of the bounded fragment are given.

The translations given above are truth-preserving. To state this formally, one makes use of the well-known observation that models and assignments for hybrid logic can be considered as models and assignments for first-order logic and vice versa. These truth-preservation results are straightforward to formulate and we leave the details to the reader. Thus, the hybrid logic with the binder $\mathtt{\forall}$ has the same expressive power as first-order logic with equality and the hybrid logic without the binder $\mathtt{\forall}$ (but with the binder $\mathtt{\downarrow}$) has the same expressive power as the bounded fragment of first-order logic (note that the translation $\mathrm{ST}_\mathtt{a} (\mathtt{\phi})$ of any formula $\mathtt{\phi}$ without the binder $\mathtt{\forall}$ is in the bounded fragment).

The translations above can be extended to first-order hybrid logic, in which case the relevant target logic is two-sorted first-order logic with equality, one sort for worlds and one sort for individuals, see Chapter 6 of Braüner (2011a). In the case of intensional first-order hybrid logic, three sorts are employed, the third sort being for intensions, see Chapter 7 of Braüner (2011a).

## 4. Arthur N. Prior and hybrid logic

The history of hybrid logic goes back to Arthur N. Prior’s hybrid tense logic, which is a hybridized version of ordinary tense logic. With the aim of investigating this further, we shall give a formal definition of hybrid tense logic. The language of hybrid tense logic is simply the language of hybrid logic defined above except that there are two modal operators, namely $\mathtt{G}$ and $\mathtt{H}$, instead of the single modal operator $\mathtt{\Box}$. The two new modal operators are called *tense operators*. The semantics of hybrid tense logic is the semantics of hybrid logic, cf. earlier, with the clause for $\mathtt{\Box}$ replaced by clauses for the tense operators $\mathtt{G}$ and $\mathtt{H}$.

> $M, g, w \vDash \mathtt{G \phi}$ iff for any element $v$ of $W$ such that $wRv$, it is the case that $M, g, v \vDash \mathtt{\phi}$ $M, g, w \vDash \mathtt{H \phi}$ iff for any element $v$ of $W$ such that $vRw$, it is the case that $M, g, v \vDash \mathtt{\phi}$

Thus, there are now two modal operators, namely one that “looks forwards” along the accessibility relation and one that “looks backwards”. In tense logic the elements of the set $W$ are called *moments* or *instants* and the relation $R$ is called the *earlier-later relation*.

Of course, it is straightforward to modify the translations $\mathrm{ST}_a$ and $\mathrm{HT}$ above such that translations are obtained between hybrid tense logic (including the $\mathtt{\forall}$ binder) and first-order logic with equality. The first-order logic under consideration is what Prior called *first-order earlier-later logic*. Given the translations, it follows that Prior’s first-order earlier-later logic has the same expressive power as hybrid tense logic.

Now, Prior introduced hybrid tense logic in connection with what he called four grades of tense-logical involvement. The motivation for his four grades of tense-logical involvement was philosophical. The four grades were presented in the book Prior (1968), Chapter XI (also Chapter XI in the new edition Prior (2003)). Moreover, see Prior (1967), Chapter V.6 and Appendix B.3-4. For a more general discussion, see the posthumously published book Prior and Fine (1977). The stages progress from what can be regarded as pure first-order earlier-later logic to what can be regarded as pure tense logic; the goal being to be able to consider the tense logic of the fourth stage as encompassing the earlier-later logic of the first stage. In other words, the goal was to be able to translate the first-order logic of the earlier-later relation into tense logic. It was with this goal in mind Prior introduced so-called instant-propositions:

> What I shall call the third grade of tense-logical involvement consists in treating the instant-variables $a, b, c$, etc. as also representing propositions. (Prior 2003, p. 124)[^prior-2003]

In the context of modal logic, Prior called such propositions possible-world-propositions. Of course, this is what we here call nominals. Prior also introduced the binder $\mathtt{\forall}$ and what we here call satisfaction operators (he used the notation $\mathtt{T(a, \phi)}$ instead of $\mathtt{@_a \phi}$ for satisfaction operators). In fact, Prior’s third grade tense logic is identical to the hybrid tense logic as defined above. The $\mathtt{\downarrow}$ binder was introduced much later. Thus, Prior obtained the expressive power of his first-order earlier-later logic by adding to ordinary tense logic further expressive power in the form of nominals, satisfaction operators, and the binder $\mathtt{\forall}$. So from a technical point of view he clearly reached his goal.

However, from a philosophical point of view it has been debated whether or not the ontological import of his third grade tense logic is the same as the ontological import of the first-order earlier-later logic. For example, the $\mathtt{\forall}$ binder is by some authors considered a direct analogy to the first-order $\mathtt{\forall}$ quantifier, and therefore suspect; see for example the paper Sylvan (1996) in the collection Copeland (1996). See Braüner (2002) for a discussion of Prior’s fourth grade tense logic. See also Øhrstrøm and Hasle (1993), Øhrstrøm and Hasle (2006), Müller (2007), and Blackburn (2006). Finally, see the discussion of Prior’s four grades in Chapter 1 of Braüner (2011a).

The paper Hasle (2020) points out traces of hybrid-logical ideas in Prior’s works before the publication of Prior (1967) and Prior (1968) (new edition Prior (2003)). The above mentioned paper Øhrstrøm and Hasle (2006) gives a detailed account of Prior’s logical work. For a comprehensive account of Prior’s life and work, see the book Øhrstrøm and Hasle (1995). The paper Hasle and Øhrstrøm (2016) describes Prior’s methodological approach, in particular, his view on formalisation and the role of symbolic logic in conceptual studies.

## 5. The development of hybrid logic since Prior

The first completely rigorous definition of hybrid logic was given in Bull (1970), which appeared in a special issue of the journal *Theoria* in memory of Prior. Bull introduces a third sort of propositional symbols where a propositional symbol is assumed to be true exactly at one branch (“course of events”) in a branching time model. This idea of sorting propositional symbols according to restrictions on their interpretations has been developed further by a number of authors, see Section 5 of the paper Blackburn and Tzakova (1999) and also Blackburn and Goranko (2001).

The hybrid logical approach originally invented by Prior in the late 1960s was reinvented in the 1980s by Solomon Passy and Tinko Tinchev from Bulgaria, see Passy and Tinchev (1985) as well as Passy and Tinchev (1991). Rather than ordinary modal logic, this work took place in connection with the much more expressive Propositional Dynamic Logic.

A major contribution in the 1990s was the introduction of the $\mathtt{\downarrow}$ binder. An early version of the downarrow binder was introduced by Valentin Goranko in the papers Goranko (1994) and Goranko (1996). The version of the present paper was introduced in Blackburn and Seligman (1995). Since then, hybrid logic with the $\mathtt{\downarrow}$ binder has been extensively studied, see for example the paper Areces, Blackburn, and Marx (2001) on model-theoretic aspects of this logic. A comprehensive study of the model-theory of hybrid logic is the PhD thesis of ten Cate (2004). The paper Areces, Fervari, Hoffmann, and Martel (2018) considers the relationship between strong hybrid logics with the $\mathtt{\downarrow}$ binder and what are called relation-changing modal logics.

Also the weaker hybrid logic obtained by omitting both of the binders $\mathtt{\downarrow}$ and $\mathtt{\forall}$ has been the subject of extensive exploration. It turns out that this binder-free logic and a number of variants of it are decidable. In the paper Areces, Blackburn, and Marx (1999), a number of complexity results are given for hybrid modal and tense logics over various classes of frames, for example arbitrary, transitive, linear, and branching. It is remarkable that the satisfiability problem of the binder-free hybrid logic over arbitrary frames is decidable in PSPACE, which is the same as the complexity of deciding satisfiability in ordinary modal logic. Thus, hybridizing ordinary modal logic gives more expressive power, but the complexity stays the same. Some work has been carried out on simulating nominals inside modal logic, see Kracht and Wolter (1997).

Any ordinary modal formula expresses a monadic second-order property on frames, and it is well-known that for some modal formulas, including what are called Sahlqvist formulas, the second-order property is equivalent to a first-order property. In the paper Goranko and Vakarelov (2006) this is shown to hold also for a class of hybrid-logical formulas, including nominals. Several algorithms exists for calculating first-order equivalents of ordinary modal formulas. One such algorithm, SQEMA, is in the paper Conradie, Goranko, and Vakarelov (2006) extended to encompass the hybrid-logical formulas considered in Goranko and Vakarelov (2006).

As described in the previous section, Prior introduced hybrid tense logic to deal with a particular issue in the philosophy of time, but in Prior (1968), Chapter XIV (also Chapter XIV in the new edition Prior (2003)), he also showed that hybrid tense logic can replace a two-dimensional temporal logic introduced by Hans Kamp in unpublished material circulated in 1967, and later included in Kamp (1971). The dimension is simply the number of instants a formula is evaluated relative to, so adding hybrid-logical machinery enables two dimensions to be replaced by one. This work has recently been followed up in a number of papers by Blackburn and Jørgensen, see Blackburn and Jørgensen (2016a) for an overview. We now give a brief sketch of this line of work, adapted to the terminology of the present entry. The version of hybrid logic in question has a designated nominal $\mathtt{now}$ and each model comes with a designated time $ t_0 $ such that i) any stand-alone formula is evaluated relative to $ t_0 $ and ii) the nominal $\mathtt{now}$ refers to $ t_0 $. More formally, we adopt the convention that $(M,t_0), g \vDash \mathtt{\phi}$ means $M, g, t_0 \vDash \mathtt{\phi}$ and we only consider assignments $g$ where $g(\mathtt{now})=t_0$. Note that the nominal $\mathtt{now}$, considered as a stand-alone formula, is valid in this semantics, but this is not the case for any other nominal. This new notion of validity is by Blackburn and Jørgensen called *contextual validity*. The paper Blackburn and Jørgensen (2013) gives an axiom system which is complete wrt. this notion of contextual validity. The paper Blackburn and Jørgensen (2012) gives a complete tableau system, but the semantics of this paper is in line with Kamp’s original two-dimensional semantics. Both papers also consider further indexicals like $\mathtt{yesterday}$, $\mathtt{today}$ and $\mathtt{tomorrow}$.

The paper Blackburn and Jørgensen (2016b) uses hybrid tense logic to combine ideas of Prior with those of Hans Reichenbach on how to represent natural language tenses. Prior preferred the well-known tense operators described above, whereas Reichenbach preferred temporal references, that is, references to specific times, Reichenbach (1947). It turns out that the two approaches can be combined, which was not the route taken by Prior himself––see the account given in Blackburn and Jørgensen (2016b),

Hybrid-logical notions have been applied in many different places, for example, the paper Areces and Fervari (2021) adds hybrid operators to XPath, which is a widely used query language for XML, a markup language for describing digital text. Hybrid-logical has also been used to add expressive power to specification logics to capture certain properties of computational systems, see Neves, Madeira, Martins, Barbosa (2016). It should, moreover, be mentioned that logics similar to hybrid logics play a central role within the area of description logic, which is a family of logics used for knowledge representation in Artificial Intelligence, see the paper Blackburn and Tzakova (1998) and Carlos Areces’ PhD thesis (2000).

## 6. Axioms for hybrid logic

A number of papers have dealt with axioms for hybrid logic, for example Gargov and Goranko (1993), Blackburn (1993), and Blackburn and Tzakova (1999). In the paper Gargov and Goranko (1993) an axiom system for hybrid logic is given, and it is shown that if the system is extended with a set of additional axioms which are *pure* formulas (that is, formulas where all propositional symbols are nominals), then the extended axiom system is complete with respect to the class of frames validating the axioms in question. Pure formulas correspond to first-order conditions on the accessibility relation (cf. the translation $\mathrm{ST}_\mathtt{a}$ above), so axiom systems for new hybrid logics with first-order conditions on the accessibility relation can be obtained in a uniform way simply by adding axioms as appropriate. So, if, for example, the formula $\mathtt{c\rightarrow \Box \neg c}$ is added as an axiom, then the resulting system is complete with respect to irreflexive frames, as we mentioned earlier. See the discussion of such rules in Section 4 of the paper Blackburn (2000).

The proof­ system in Gargov and Goranko (1993) makes use of a complex rule (called COV) where the formula schema containing the active part of the rule can be arbitrarily large; in fact, the active part is embedded under arbitrarily deep nestings of modal operators. Blackburn and Tzakova (1999) shows that satisfaction operators can be used to formulate an axiom system in a more standard format, using a simpler rule called PASTE, such that the system is still complete when extended with pure axions.

The paper Blackburn and ten Cate (2006) investigates *orthodox* proof-rules, which are proof-rules without side-conditions, and it is shown that if one requires extended completeness using pure formulas, then unorthodox proof-rules are indispensable in axiom systems for binder-free hybrid logic. However, in the case of the stronger hybrid logic including the $\mathtt{\downarrow}$ binder, an axiom system can be given that only involves orthodox proof-rules. See also the book Braüner (2011a) for another axiom system for hybrid logic as well as axiom systems for intuitionistic hybrid logic and a hybridization of Nelson’s paraconsistent logic N4 (compare to Costa and Martins (2017) where another paraconsistent hybrid logic is considered). A survey of intuitionistic hybrid logic can be found in Braüner (2011b).

## 7. Analytic proof methods for hybrid logic

Tableau, Gentzen, and natural deduction style proof-theory for hybrid logic work very well compared to ordinary modal logic. Usually, when a modal tableau, Gentzen, or natural deduction system is given, it is for one particular modal logic and it has turned out to be problematic to formulate such systems for modal logics in a uniform way without introducing metalinguistic machinery. This can be remedied by hybridization, that is, hybridization of modal logics enables the formulation of uniform tableau, Gentzen, and natural deduction systems for wide classes of logics. The paper Blackburn (2000) introduces a tableau system for hybrid logic that has this desirable feature: Analogous to the axiom system of Blackburn and Tzakova (1999), completeness is preserved if the tableau system is extended with a set of pure axioms, that is, a set of pure formulas that are allowed to be added to a tableau during the tableau construction. The tableau system of Blackburn (2000) is the basis for a decision procedure for the binder-free fragment of hybrid logic given in Bolander and Braüner (2006). This line of work has been continued in the papers Bolander and Blackburn (2007) and Bolander and Blackburn (2009). The paper Cerrito and Cialdea (2010) presents another tableau-based decision procedure for hybrid logic. Other decision procedures for hybrid logics, which also are based on proof-theory, are given in the paper Kaminski and Smolka (2009). The procedures of the latter paper are based on a higher-order formulation of hybrid logic involving the simply typed lambda calculus.

The article Hansen, Bolander, and Braüner (2018) gives a tableau-based decision procedure for many-valued hybrid logic, that is, hybrid logic where the two-valued classical logic basis has been generalized to a many-valued logic basis involving a truth-value space having the structure of a finite Heyting algebra. Hansen (2010) gives a tableau-based decision procedure for a hybridized version of a dynamic epistemic logic called public annoucement logic. This is also a major issue of the PhD thesis Hansen (2011).

Natural deduction style proof-theory of hybrid logic has been explored in the book Braüner (2011a). This book also gives a cut-free Gentzen sequent system for hybrid logic. Cut-freeness is proved via a normalizing natural deduction system, but such a result can also be proved directly, see Indrzejczak (2016). The natural deduction and Gentzen systems of Braüner (2011a) can be extended with additional proof-rules corresponding to first-order conditions on the accessibility relations expressed by so-called *geometric theories* (this is of course analogous to extending tableau and axiom systems with pure axioms). See also Braüner and de Paiva (2006) where a natural deduction system is given for intuitionistic hybrid logic (Chapter 8 of Braüner (2011a)).

Gentzen and natural deduction systems for logics similar to hybrid logics were explored already in the 1990s by Jerry Seligman, see the overview in Seligman (2001). In particular, Seligman developed proof-systems that work with arbitrary formulas, not just satisfaction statements, the latter being the case for most proof-systems for hybrid logic, where satisfaction operators are used to access information hidden behind modalities. A natural deduction system in this style was introduced in Seligman (1997) and this system has been further developed in Chapter 4 of the book Braüner (2011a). A tableau systems in Seligman’s proof-style has been considered in Blackburn, Bolander, Braüner, and Jørgensen (2017) where a syntactic completeness proof is given. A semantic completenes proof of the tableau system is given in Jørgensen, Blackburn, Bolander, Braüner (2016). Reasoning in these systems does not directly rely on the global encodings that satisfaction operators make possible, hence, these systems can be considered more in line with the local character of the standard Kripke semantics for modal logic. In fact, this more local reasoning style makes these systems suitable for formalizing the perspectival reasoning taking place in certain psychological reasoning tasks, see Braüner (2014b) as well as Braüner, Blackburn, and Polyanskaya (2016).

As mentioned above, the papers Blackburn, Bolander, Braüner, and Jørgensen (2017) and Jørgensen, Blackburn, Bolander, Braüner (2016) gave completenes proofs for Seligman-style tableau systems for hybrid logic. Based on these results, completeness for these systems have in From (2021) and From, Blackburn, and Villadsen (2020) been fully formalised using the proof assistant Isabelle/HOL.

Some work in resolution calculi and model checking has been carried out, see Areces, de Rijke, and de Nivelle (2001) as well as Areces and Gorin (2011) for resolution calculi and see as Franceschet and de Rijke (2006) as well as Lange (2009) for results on model checking.

## 8. Quantified Hybrid Logics

We treat quantified hybrid logics separately. First-order modal logic comes in many different versions, which also is the case with first-order hybrid logic. Tableau systems for first-order hybrid logic can be found in the paper Blackburn and Marx (2002). Natural deduction and axiom systems for first-order hybrid logic can be found in Chapter 6 of the book Braüner (2011a) and Chapter 7 of the book deals with natural deduction for intensional first-order hybrid logic. The paper Indrzejczak (2020) gives a Gentzen-style sequent calculus for first-order hybrid logic with lambda operators as well as existence and definedness predicates. The paper Barbosa, Martins, and Carreteiro (2014) gives an axiomatization of a fragment of first-order hybrid logic called equational first-order hybrid logic.

It is remarkable that first-order hybrid logic offers precisely the features needed to prove interpolation theorems: While interpolation fails in a number of well-known first-order modal logics, their hybridized counterparts have this property, see Areces, Blackburn, and Marx (2003) as well as Blackburn and Marx (2003). The first paper gives a model-theoretic proof of interpolation whereas the second paper gives an algorithm for calculating interpolants based on a tableau system.

The paper Areces, Blackburn, Huertas, and Manzano (2014) deals with a hybrid-logical version of higher-order modal logic (that is, modal logic built over Church’s simple theory of types). Axiom systems are given and completeness is proved wrt. Henkin-type semantics. The paper Blackburn, Huertas, Manzano, and Jørgensen (2014) extends these results to encompass the downarrow binder and gives translations to and from the bounded fragment of first-order logic (see above).

Rather than introducing nominals as a second kind of propositional symbol, Prior sometimes created them using propositional quantifiers together with the $\mathtt{Q}$ operator, defined as follows:

> $\mathtt{ Qp = \Diamond p \wedge \forall q (\Box (p \rightarrow q) \vee \Box (p \rightarrow \neg q)) }$

Here the $\mathtt{\Box}$ and $\mathtt{\Diamond}$ are the box and diamond forms of the universal modality. The result of prefixing the ordinary propositional symbol $\mathtt{p}$ by the $\mathtt{Q}$ operator, converts $\mathtt{p}$ to a nominal. To be more precise, taking the propositional quantifier $\mathtt{\forall q}$ to range over all sets of worlds, $\mathtt{Qp}$ says that $\mathtt{p}$ denotes a singleton set, that is, $\mathtt{p}$ is a standard nominal. But there is another approach to interpreting propositional quantifiers, called the general (or Henkin) approach, where propositional quantifiers range over a *preselected* set of subsets of worlds. Interpreted these two different ways, the $\mathtt{Q}$ operator gives rise to two different ‘species’ of nominals, and it turns out that these two species behave differently with respect to the rule of universal instantiation. This is investigated in the paper Blackburn, Braüner, and Kofod (2020), which gives a tableau system for a hybrid logic with Henkin-style propositional quantifiers, containing both species of nominals. The paper moreover describes how this formally-defined ‘species division’ corresponds rather well with two intuitions about nominals that can be detected in Prior’s writings.

Since the mid 1990s, the work on hybrid logic has flourished. We refer the reader to the publications in the bibliography for further references. Moreover, see the internet resources below.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=logic-hybrid). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/logic-hybrid/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=logic-hybrid&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/logic-hybrid/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- [A.N. Prior—The Founding Father of Temporal Logic](http://www.priorstudies.org/)

## Related Entries

future contingents | logic: modal | logic: temporal | possibilism-actualism debate | Prior, Arthur

[^areces-2000]: Areces, C., 2000. *Logic Engineering. The Case of Description and Hybrid Logics*, Ph.D. thesis, Institute for Logic, Language and Computation, University of Amsterdam.

[^areces-1999]: Areces, C., Blackburn, P., and Marx, M., 1999. “The Computational Complexity of Hybrid Temporal Logics”, *The Logic Journal of the IGPL*, 8: 653–679.

[^areces-2001]: –––, 2001. “Hybrid Logics: Characterization, Interpolation and Complexity”, *Journal of Symbolic Logic*, 66: 977–1010.

[^areces-2003]: –––, 2003. “Repairing the Interpolation Theorem in Quantified Modal Logic”, *Annals of Pure and Applied Logic*, 124: 287–299.

[^areces-2014]: Areces, C., Blackburn, P., Huertas, A., and Manzano, M., 2014. “Completeness in Hybrid Type Theory”, *Journal of Philosophical Logic*, 43: 209–238.

[^areces-2001-2]: Areces, C., de Rijke, M., and de Nivelle, H., 2001. “Resolution in Modal, Description and Hybrid Logic”, *Journal of Logic and Computation*, 11: 717–736.

[^areces-2021]: Areces, C. and Fervari, R., 2021. “Axiomatizing Hybrid XPath with Data”, *Logical Methods in Computer Science*, 17:5:1–5:37.

[^areces-2018]: Areces, C., Fervari, R., Hoffmann, G., and Martel, M., 2018. “Satisfiability for Relation-Changing Logics”, *Journal of Logic and Computation*, 28: 1443–1470.

[^areces-2011]: Areces, C. and Gorin, D., 2011. “Resolution with Order and Selection for Hybrid Logics”, *Journal of Automated Reasoning*, 46: 1–42.

[^areces-2006]: Areces, C. and ten Cate, B., 2006. “Hybrid Logics”, in Blackburn, van Benthem, and Wolter (eds.) (2006): 821–868.

[^barbosa-2014]: Barbosa, L.S., Martins, M.A., and Carreteiro, M., 2014. “A Hilbert-Style Axiomatisation for Equational Hybrid Logic”, *Journal of Logic, Language and Information*, 23: 31–52.

[^blackburn-1993]: Blackburn, P., 1993. “Nominal Tense Logic”, *Notre Dame Journal of Formal Logic*, 14: 56–83.

[^blackburn-2000]: –––, 2000. “Internalizing Labelled Deduction”, *Journal of Logic and Computation*, 10: 137–168.

[^blackburn-2006]: –––, 2006. “Arthur Prior and Hybrid Logic”, *Synthese*, 150: 329–372.

[^blackburn-2017]: Blackburn, P., Bolander, T., Braüner, T., and Jørgensen, K.F., 2017. “Completeness and Termination for a Seligman-style Tableau System”, *Journal of Logic and Computation*, 27: 81–107.

[^blackburn-2020]: Blackburn, P., Braüner, T., and Kofod, J.L., 2020. “Remarks on Hybrid Modal Logic with Propositional Quantfiers”, in *The Metaphysics of Time: Themes from Prior* (*Logic and Philosophy of Time*, No. 4), pp. 401–426, Aalborg Universitetsforlag.

[^blackburn-2001]: Blackburn, P. and Goranko, V., 2001. “Hybrid Ockhamist Temporal Logic”, in *Proc. of the Eighth International Symposium on Temporal Representation and Reasoning (TIME-01)*, pp. 183–188, IEEE Computer Society Press.

[^blackburn-2014]: Blackburn, P., Huertas, A., Manzano, M., and Jørgensen, K.F., 2014. “Henkin and Hybrid Logic”, in *The Life and Work of Leon Henkin: Essays on His Contributions* (Studies in Universal Logic), pp. 279–306, Birkhäuser.

[^blackburn-2012]: Blackburn, P. and Jørgensen, K.F., 2012. “Indexical hybrid tense logic”, in *Advances in Modal Logic* (Volume 9), pp. 144–160, London: College Publications.

[^blackburn-2013]: –––, 2013. “Contextual validity in hybrid logic”, in *Modeling Using Context* (Lecture Notes in Computer Science: Volume 8177), pp. 185–198, Heidelberg: Springer.

[^blackburn-2016a]: –––, 2016a. “Arthur Prior and ‘now’”, *Synthese*, 193: 3665–3676.

[^blackburn-2016b]: –––, 2016b. “Reichenbach, Prior and hybrid tense logic”, *Synthese*, 193: 3677–3689.

[^blackburn-2002]: Blackburn, P. and Marx, M., 2002. “Tableaux for Quantified Hybrid Logic”, in *Automated Reasoning with Analytic Tableaux and Related Methods, TABLEAUX* (Lecture Notes in Artificial Intelligence: Volume 2381), pp. 38–52, Heidelberg: Springer.

[^blackburn-2003]: –––, 2003. “Constructive Interpolation in Hybrid Logic”, *Journal of Symbolic Logic*, 68: 463–480.

[^blackburn-1995]: Blackburn, P. and Seligman, J., 1995. “Hybrid Languages”, *Journal of Logic, Language and Information*, 4: 251–271.

[^blackburn-2006-2]: Blackburn, P. and ten Cate, B., 2006. “Pure Extensions, Proof Rules, and Hybrid Axiomatics”, *Studia Logica*, 84: 277–322.

[^blackburn-1998]: Blackburn, P. and Tzakova, M., 1998. “Hybridizing Concept Languages”, *Annals of Mathematics and Artificial Intelligence*, 24: 23–49.

[^blackburn-1999]: –––, 1999. “Hybrid Languages and Temporal Logic”, *Logic Journal of the IGPL*, 7: 27–54.

[^blackburn-2006-3]: Blackburn, P., van Benthem, J., and Wolter, F. (eds.), 2006. *Handbook of Modal logic*, Amsterdam: Elsevier.

[^bolander-2007]: Bolander, T. and Blackburn, P., 2007. “Termination for Hybrid Tableaus”, *Journal of Logic and Computation*, 17: 517–554.

[^bolander-2009]: –––, 2009. “Terminating Tableau Calculi for Hybrid Logics Extending K”, in *Proceedings of Methods for Modalities 5* (Electronic Notes in Theoretical Computer Science: Volume 231), pp. 21–39, Amsterdam: Elsevier.

[^bolander-2006]: Bolander, T. and Braüner, T., 2006. “Tableau-Based Decision procedures for Hybrid Logic”, *Journal of Logic and Computation*, 16: 737–763.

[^braüner-2002]: Braüner, T., 2002. “Modal logic, Truth, and the Master Modality”, *Journal of Philosophical Logic*, 31: 359–386.

[^braüner-2011a]: –––, 2011a. *Hybrid Logic and its Proof-Theory* (Applied Logic Series: Volume 37), Dordrecht-Heidelberg-Berlin-New York: Springer.

[^braüner-2011b]: –––, 2011b. “Intuitionistic Hybrid Logic: Introduction and Survey”, *Information and Computation*, 209: 1437–1446.

[^braüner-2014a]: –––, 2014a. “First-order Hybrid Logic: Introduction and Survey”, *Logic Journal of the IGPL*, 22: 155–165.

[^braüner-2014b]: –––, 2014b. “Hybrid-Logical Reasoning in the Smarties and Sally-Anne Tasks”, *Journal of Logic, Language and Information*, 23: 415–439.

[^braüner-2016]: Braüner, T., Blackburn, P., and Polyanskaya, I., 2016. “Second-order false-belief tasks: Analysis and formalization”, in *Logic, Language, Information, and Computation : 23rd International Workshop, WoLLIC* (Lecture Notes in Computer Science: Volume 9803), pp. 125–144, Heidelberg: Springer.

[^braüner-2006]: Braüner, T. and de Paiva, V., 2006. “Intuitionistic Hybrid Logic”, *Journal of Applied Logic*, 4: 231–255.

[^bull-1970]: Bull, R., 1970. “An Approach to Tense Logic”, *Theoria*, 36: 282–300.

[^cerrito-2010]: Cerrito, S. and Cialdea, M., 2010. “Nominal Substitution at Work with the Global and Converse Modalities”, in *Advances in Modal Logic* (Volume 8), pp. 57–74, London: College Publications.

[^conradie-2006]: Conradie, W., Goranko, V., and Vakarelov, D., 2006. “Algorithmic Correspondence and Completeness in Modal Logic II. Polyadic and Hybrid Extensions of the Algorithm SQEMA”, *Journal of Logic and Computation*, 16: 579–612.

[^copeland-1996]: Copeland, J. (ed.), 1996. *Logic and Reality: Essays in the Legacy of Arthur Prior*, Oxford: Clarendon Press.

[^costa-2017]: Costa, D. and Martins, M.A., 2017. “Paraconsistency in Hybrid Logic”, *Journal of Logic and Computation*, 27: 1825–1852

[^franceschet-2006]: Franceschet, M. and de Rijke, M., 2006. “Model Checking Hybrid Logics (With An Application to Semistructured Data)”, *Journal of Applied Logic*, 4: 279–304.

[^from-2021]: From, A.H., 2021. “Completeness for a Terminating Seligman-Style Tableau System”, in *26th International Conference on Types for Proofs and Programs* (TYPES 2020), Leibniz International Proceedings in Informatics (LIPIcs): Volume 188, Schloss Dagstuhl–Leibniz-Zentrum für Informatik, pp. 5:1–5:17.

[^from-2020]: From, A.H., Blackburn, P., and Villadsen, J., 2020. “Formalizing a Seligman-Style Tableau System for Hybrid Logic”, in: *Proceedings of 10th International Joint Conference on Automated Reasoning* (IJCAR), Lecture Notes in Computer Science (Voume 12166), pp. 474–482, Cham: Springer-Verlag.

[^gabbay-2006]: Gabbay, D. and Woods, J. (eds.), 2006. *Logic and the Modalities in the Twentieth Century. The Handbook of the History of Logic* (Volume 7), Amsterdam: Elsevier.

[^gargov-1993]: Gargov, G. and Goranko, V., 1993. “Modal Logic with Names”, *Journal of Philosophical Logic*, 22: 607–636.

[^goranko-1994]: Goranko, V., 1994. “Temporal Logic with Reference Pointers”, in *Proceedings of the 1st International Conference on Temporal Logic* (Lecture Notes in Artificial Intelligence: Volume 827), pp. 133–148, Berlin: Springer.

[^goranko-1996]: –––, 1996. “Hierarchies of Modal and Temporal Logics with Reference Pointers”, *Journal of Logic, Language, and Information*, 5: 1–24.

[^goranko-2001]: Goranko, V. and Vakarelov, D., 2001. “Sahlqvist Formulas in Hybrid Polyadic Modal Logics”, *Journal of Logic and Computation*, 11: 737–754.

[^hansen-2010]: Hansen, J.U., 2010. “Terminating Tableaux for Dynamic Epistemic Logics”, in *Proceedings of the 6th Workshop on Methods for Modalities (M4M-6 2009)* (Electronic Notes in Theoretical Computer Science: Volume 262), pp. 141–156.

[^hansen-2011]: –––, 2011. *A Logic Toolbox for Modeling Knowledge and Information in Multi-Agent Systems and Social Epistemology*, Ph.D. thesis, Roskilde University.

[^hansen-2018]: Hansen, J.U., Bolander, T., and Braüner, T., 2018. “Many-Valued Hybrid Logic”, *Journal of Logic and Computation*, 28: 883–908.

[^hasle-2020]: Hasle, P., 2020. “The Beginnings of Hybrid Logic: Meredith, Prior and the Contingent Constant n”, in *The Metaphysics of Time: Themes from Prior* (Logic and Philosophy of Time No. 4), pp. 145–163, Aalborg Universitetsforlag.

[^hasle-2016]: Hasle, P. and Øhrstrøm, P., 2016. “Prior’s Paradigm for the Study of Time and its Methodological Motivation”, *Synthese*, 193: 3401–3416.

[^indrzejczak-2016]: Indrzejczak, A., 2016. “Simple cut elimination proof for hybrid logic”, *Logic and Logical Philosophy*, 25: 129–141.

[^indrzejczak-2020]: Indrzejczak, A., 2020. “Existence, Definedness and Definite Descriptions in Hybrid Modal Logic”, in *Advances in Modal Logic* (Volume 13), pp. 349–368, London: College Publications.

[^jørgensen-2016]: Jørgensen, K.F., Blackburn, P., Bolander, B., and Braüner, T., 2016. “Synthetic Completeness Proofs for Seligman-style Tableau Systems”, in *Advances in Modal Logic* (Volume 11), pp. 302–321, London: College Publications.

[^kaminski-2009]: Kaminski, M. and Smolka, G., 2009. “Terminating Tableau Systems for Hybrid Logic with Difference and Converse”, *Journal of Logic, Language and Information*, 18: 437–464.

[^kamp-1971]: Kamp, H., 1971. “Formal properties of ‘now’”, *Theoria*, 37: 237–273.

[^kracht-1997]: Kracht, M. and Wolter, F., 1997. “Simulation and Transfer Results in Modal Logic — A Survey”, *Studia Logica*, 59: 149–177.

[^lange-2009]: Lange, M., 2009. “Model Checking for Hybrid Logic”, *Journal of Logic, Language and Information*, 18: 465–491.

[^müller-2007]: Müller, T., 2007. “Prior’s Tense-Logical Universalism”, *Logique et Analyse*, 50: 223–252.

[^neves-2016]: Neves, R., Madeira, A., Martins, M.A., Barbosa, L.S., 2016. “Proof theory for hybrid(ised) logics”, *Science of Computer Programming*, 126: 73–93.

[^øhrstrøm-1993]: Øhrstrøm, P. and Hasle, P., 1993. “A.N. Prior’s Rediscovery of Tense Logic”, *Erkenntnis*, 39: 23–50.

[^øhrstrøm-1995]: –––, 1995. *Temporal Logic. From Ancient Ideas to Artificial Intelligence*, Dordrecht: Kluwer.

[^øhrstrøm-2006]: –––, 2006. “A.N. Prior’s Logic”, in Gabbay and Woods (2006), pp. 399–446.

[^passy-1985]: Passy, S. and Tinchev, T., 1985. “Quantifiers in Combinatory PDL: Completeness, Definability, Incompleteness”, in *Fundamentals of Computation Theory FCT 85* (Lecture Notes in Computer Science: Volume 199), pp. 512–519, Berlin: Springer.

[^passy-1991]: Passy, S. and Tinchev, T., 1991. “An Essay in Combinatory Dynamic Logic”, *Information and Computation*, 93: 263–332.

[^prior-1967]: Prior, A.N., 1967. *Past, Present and Future*, Oxford: Clarendon Press.

[^prior-1968]: –––, 1968. *Papers on Time and Tense*, Oxford: Clarendon Press.

[^prior-2003]: –––, 2003. *Papers on Time and Tense*, second revised and expanded edition of Prior 1968, edited by P. Hasle, P. Øhrstrøm, T. Braüner, and J. Copeland, Oxford: Oxford University Press.

[^prior-1977]: Prior, A.N. and Fine, K., 1977. *Worlds, Times and Selves*, London: Duckworth; based on manuscripts by Prior with a preface and a postscript by K. Fine.

[^reichenbach-1947]: Reichenbach, H., 1947. *Elements of Symbolic Logic*, New York: Free Press.

[^seligman-1997]: Seligman, J., 1997. “The logic of correct description”, in *Advances in Intensional Logic* (Applied Logic Series: Volume 7), pp. 107–135, Dordrecht: Kluwer.

[^seligman-2001]: Seligman, J., 2001. “Internalisation: The Case of Hybrid Logics”, *Journal of Logic and Computation*, 11: 671–689.

[^sylvan-1996]: Sylvan, R., 1996. “Other Withered Stumps of Time”, in Copeland (1996), pp. 111–130.

[^cate-2004]: ten Cate, B., 2004. *Model Theory for Extended Modal Languages*, PhD thesis, Institute for Logic, Language and Computation, University of Amsterdam.
