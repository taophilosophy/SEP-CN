# Free Logic
**First published Mon Apr 5, 2010; substantive revision Thu Jun 19, 2025**

*Gratzl, Norbert, Pavlović, Edi, Nolt, John*

In most general terms, free logic is concerned with names that do not denote. Classical logic requires each singular term to denote an object in the domain of quantification — which is usually understood as the set of “existing” objects. Free logic does not. Free logic is therefore useful for analyzing discourse containing singular terms that either are or might be empty. Varying conventions for calculating the truth values of atomic formulas containing empty singular terms yield three distinct forms of free logic: negative, positive and neutral, which is why we commonly refer to them as free logics (in the plural) instead.

Most free logics have been first-order, their quantifiers ranging over individuals. Recently, however, some work on higher-order free logics has appeared. Corine Besson (2009) argues that internalist theories of natural kinds require second-order free logics whose quantifiers range over kinds, and she finds precedent for this idea ranging as far back as Cocchiarella (1986). Andrew Bacon, John Hawthorne, and Gabriel Uzquiano (2016) explore the possibility of using a higher-order free logic to resolve certain intensional paradoxes, but they find that this idea faces daunting difficulties. Timothy Williamson (2016) reluctantly concurs. This article, however, focuses mainly on first-order logics.

Section 1 lays out a brief history and motivation of free logic, introduces basic definitions and explains how it differs from related logics. The semantics for the variants of free logics are surveyed in Section 2. Section 3 presents the proof systems for the three variants, briefly laying out the axiomatization and then focusing on the currently favored proof-theoretic approaches. Section 4 is critical, examining three anomalies that infect most free logics. Section 5 samples applications of free logic to theories of description, logics of partial or non-strict functions, logics with Kripke semantics, logics of fiction and logics that are in a certain sense Meinongian.

## 1. Brief History and Motivation

A consideration of one question regarding non-denoting names can be traced back to Aristotle (translation Barnes 1984)[^barnes-1984]:

> It might, indeed, very well seem that the same sort of thing does occur in the case of contraries said with combination, ‘Socrates is well’ being contrary to ‘Socrates is sick’. Yet not even with these is it necessary always for one to be true and the other false. For if Socrates exists one will be true and one false, but if he does not both will be false; neither ‘Socrates is sick’ nor ‘Socrates is well’ will be true if Socrates himself does not exist at all. (13b11–20)

While this passage possibly anticipates the issues free logics are concerned with, it was in the 20th century that the modern debate begins. In the first part of the 20th century, some inquiries were made into a logic with possibly empty domains, or *inclusive* logic (called so because it includes this possibility, Quine 1954)[^quine-1954], and thus inquiry is sometimes considered a precursor to the investigations into free logic. The section 1.2 below discusses the difference between free and inclusive logics, however.

Proper modern free logics, as a family of first-order logics, came about as a result of examining the existence assumptions of classical logics in the middle of the 20th century (Hintikka 1959; Lambert 1967, 1997, 2001)[^hintikka-1959][^lambert-1967], with the name due to Karel Lambert, which is short for “logic free of existence assumptions with respect to its terms, singular and general” (we’ll tighten up the previously loose talk of ‘names’ and focus on terms instead). But since in modern logic there are hardly any presuppositions with regard to general terms (although there are naturally some exceptions, like Besson 2009)[^besson-2009], the first point will be the focus of this exposition.

Consider then the following two arguments.

$$\frac{\text{Bucephalus is a horse.}}{\because \text{ There exists something that is a horse.}}$$

This sounds like a perfectly fine piece of elementary reasoning. But this is structurally at least *very* similar to the next argument:

$$\frac{\text{Sleipnir does not exist.}}{ \because\text{ There exists something that does not exist.}}$$

A useful, albeit artificial, assumption that pervades the standard approaches to quantified first order logic is that every singular term denotes an object. Obviously, the second inference is blocked by limiting singular terms to the denoting ones.

In opposition to this dismissive response “ intuitively, Socrates *could have* not existed ” (although, see possibilism-actualism debate), free logic chooses to alter the logical rules for Existential Generalization (and related Universal Specification) by explicitly limiting them to the existence predicate ${E!}$.

### 1.1 Definition and Variants

The definitional hallmarks of a free logic are: (1) it is free of existential presuppositions with respect to its singular terms, (2) it is free of existential presuppositions with respect to its general terms and finally (3) its quantifiers have existential import, or are more broadly limited to the predicate which delineates the denoting terms, ${E!}$ (most commonly read as *existence*, Leonard 1956; Baaz and Iemhoff 2006; Maffezioli and Orlandelli 2019, and *definedness*, Feferman 1995; Antonelli 2000)[^antonelli-2000][^baaz-2006][^feferman-1995][^leonard-1956][^maffezioli-2019].

In any case, it is crucial for the understanding of free logic that, in any of its versions, quantification is limited to the $E!$-predicate; whereas the particular interpretation of this predicate may vary and, as we shall see later, this predicate does not need to even have the time honored status of a *logical* predicate.

As stated previously, point (2) does not have any significant bearing on the discussion, while point (3) represents the limitation of quantification to ${E!}$. Focusing now on point (1), the question arises as to the status of atoms containing non-denoting terms, and what truth status is assigned to them determines the major variants of free logic.

*Positive* FL allows for some atoms with terms outside of ${E!}$ to remain true (at the very least self-identities). On the other hand *negative* FL treats all such atoms as uniformly false (as was the suggestion in Aristotle’s quote above). Finally *neutral* FL, assigns a third value to those atoms, and forms a subfamily of its own, depending on the interpretation of that third value and/or the meaning and inferential behavior of logical symbols.

### 1.2 Related Systems

#### Inclusive Logic

Another existence assumption that is frequently employed relates not to terms but to models — namely that the domain is non-empty. Logics which allow for the rejection of this assumption (i.e., allow us to include the empty domain) are called *inclusive*. While they bear a close resemblance to free logics, these two issues are orthogonal to one another and can be considered in separation. To see this, it is easy to consider *empty logic* of Hailperin (1953), which contains no singular terms and no elements of the domain. While obviously inclusive, this logic is not free, since there are no non-denoting terms. The converse case of free non-inclusive logics is easily obtained by additionally specifying this via the addition of the following rule to any of the free logics below:

$$\frac{{E!} t, \Gamma \Rightarrow \Delta}{\Gamma \Rightarrow \Delta} \text{NI, t fresh}$$

This is standardly taken to be the case with free logics, so this rule can be assumed to be added to the systems discussed below.

#### Classical/Intuitionistic Logic

While most of the presentation here centers on the free logics arising form the extension of classical propositional base, considerable work has also gone into investigation of those with intuitionistic bases. Considerations discussed below apply, *mutatis mutandis* also for those bases. In either case the simplest way of obtaining a non-free logic from a free one is simply the addition of the rule

$$\frac{{E!} t, \Gamma \Rightarrow \Delta}{\Gamma \Rightarrow \Delta}\text{NI}^+$$

Notice that in contrast to the previous version of the rule which required an *arbitrary* term be used, any term can be used here. Therefore, in effect this rule eliminates non-denoting terms (it states, read bottom up, that in any proof search we may add the assumption a term denotes). Important to note is that the intuitionistic version of the rule contains at most one formulas in $\Delta$, but is otherwise of the same form.

#### Quasi-free Logic

While the name is recent and due to Indrzejczak (2021a), the logics of these type have been considered for a while, with the most notable example the Logic of Partial Terms (Feferman 1995)[^feferman-1995]. This logic lies somewhere between classical (*mutatis mutandis*, intuitionistic) and free logics by, in effect, adding the rule NI$^+$ for singular terms, but remaining free for functional expressions. Feferman specifically discusses a negative free extension, but a useful overview of multiple versions (and their uniform cut elimination) is available in (Indrzejczak 2021a).

### 1.3 Language of Free logic

For the formal presentation of free logics we utilize the language $\mathcal{L}$, a standard first-order language (without functions), adapted from (Gratzl 2010)[^gratzl-2010], with the vocabulary defined as

**Definition 1** (Alphabet $\mathcal{L}$). *The alphabet* of the language $\mathcal{L}$ consists of:

1. Denumerable list of free individual variables (names): $a,b,c,\ldots$,
2. Denumerable list of bound individual variables: $x,y,z,\ldots$,
3. Denumerable list of $n$-ary predicate variables, including a unary predicate ${E!}$ and a binary predicate $=$,
4. $\neg$, $\wedge$, $\vee$, $\to$, $\forall$, $\exists$, $($, $)$.

A *formula* of $\mathcal{L}$ is then defined as

**Definition 2** (Formula of $\mathcal{L}$).

$$A::= P^{n}(\bar{t_{1}},...,\bar{t_{n}})\ |\ \neg A\ |\ A\circ A\ |\ \forall x A\ |\ \exists x A$$

where $\circ \in \{\wedge, \vee, \to\}$.

## 2. Formal Semantics for Free Logics

In this section we lay out common semantical approaches to free logics. We commence with a formal presentation of the three (well-studied) semantical approaches for positive and negative free logic.

### 2.1 Meinongian Semantics

The *inner-outer domain*, or *Meinongian* semantics, has been devised to study meta-theoretical properties of positive free logic. The main ingredients for it are a structure and a valuation, laid out in the following two definitions:

**Definition 3** (Meinongian structure $\mathcal{S}_{m}$). A *Meinongian structure* $\mathcal{S}_{m}$ is a triple $\langle\cD_i, \cD_o, \varphi\rangle$, where the following conditions are met:

1. $\cD_i, \cD_o$ are sets, with $\cD_i$ the inner domain, thought of as the set of existents, and ${\mathcal D}_o$ the outer domain, thought of the set of non-existents. Both $\cD_i$, and $\cD_o$ can possibly be empty, however: $\cD_i \cup \cD_o \not = \varnothing$, and $\cD_i \cap \cD_o = \varnothing$.
2. $\varphi(E!) = \cD_i$.
3. Let $\cD$ be the union of $\cD_i$ and $\cD_o$, then:
4. •  For every free individual variable $t$: $\varphi(t) \in \cD$.
5. •  For every $n$-ary predicate $P^n$: $\varphi(P^n) \subseteq \cD^n$.
6. •  Every object in $\cD$ has a name in the formal language, i.e. if $d \in \cD$, then $d^\bullet$ (the standard-name of $d$) is in the language.

**Definition 4** (Meinongian Valuation ${\mathcal V}^{m}$). *The truth-value assignment* ${\mathcal V}^{m}$ on the structure $\mathcal{S}_m$ is defined as

1. $\notag {\mathcal V}^{m}({E!} t)= \begin{cases} \top, & \text{if}\ \varphi(t) \in \cD_i\\ \bot, & \text{otherwise} \end{cases}$
2. $\notag {\mathcal V}^{m}(P^{n}(t_{1},\ldots,t_{n}))= \begin{cases} \top, & \text{if}\ \langle \varphi(t_{1}),\ldots,\varphi(t_{n})\rangle\in \varphi(P^{n})\\ \bot, & \text{otherwise} \end{cases}$
3. $\notag {\mathcal V}^{m}(s = t)= \begin{cases} \top, & \text{if}\ \varphi(s) = \varphi(t)\\ \bot, & \text{otherwise} \end{cases}$
4. $\notag {\mathcal V}^{m}(\neg A)= \begin{cases} \top, & \text{if}\ {\mathcal V}^{m}(A)=\bot\\ \bot, & \text{if}\ {\mathcal V}^{m}(A)=\top \end{cases}$
5. $\notag {\mathcal V}^{m}( A\to B)= \begin{cases} \bot, & \text{if}\ {\mathcal V}^{m}(A)=\top\ and\ {\mathcal V}^{m}(B)=\bot\\ \top, & \text{otherwise} \end{cases}$
6. $\notag {\mathcal V}^{m}( \forall x A)= \begin{cases} \top, & \text{if } \forall d\in \cD_i, {\mathcal V}^{m}(A[d^\bullet/x])=\top\\ \bot, & \text{if } \exists d\in \cD_i, {\mathcal V}^{m}(A[d^\bullet/x])=\bot \end{cases}$
7. ${\mathcal V}^{m}(A)= \top$ iff ${\mathcal V}^{m}(A) \not= \bot$

We lay out several examples of (logically) true statements, as well as one of non-entailment.

**Example 1**.

1. $\exists x(x = a)$ is not logically true (where $\exists x$ is understood in the usual way as $\neg \forall x \neg$). Let $\mathcal{S}_{m}$ be a Meinongian-structure with $\langle\cD_i, \cD_o, \varphi\rangle$, with $\cD_i = \varnothing$, and $\cD_o = \{1\}$, $\varphi(a) = 1$. While clearly ${\mathcal V}^{m}(a=a) = \top$, nonetheless ${\mathcal V}^{m}(\exists x(x=a)) = \bot$ since for no $d\in \cD_i$, ${\mathcal V}^m(d^\bullet = a)=\top$.
2. $P(a) \not \models \exists xP(x)$ is true (i.e., the entailment does not hold). Let $\mathcal{S}_{m}$ be a Meinongian-structure with $\langle\cD_i, \cD_o, \varphi\rangle$, with $\cD_i = \varnothing$, and $\cD_o = \{1\}$, $\varphi(a) = 1$, $\varphi(P) = \{1\}$, then: ${\mathcal V}^{m}(P(a)) = \top$, but nonetheless ${\mathcal V}^{m}(\exists xP(x)) = \bot$.
3. $P(a) \to \exists xP(x)$ is not logically true; using the same argument as in (1) above.
4. $\forall xE!x$ is logically true. Follows immediately from the valuation for $E!$.

### 2.2 Supervaluational Semantics

The supervaluational approach to semantics offers means for reducing three-valued semantics to a positive one. It is more involved, but has some advantages over Meinongian semantics given that it does not make use of an outer-domain, which can be viewed as ontologically dubious. The price for this is at least more formal complexity and, furthermore that meta-theoretically it is not compact in the sense of the compactness theorem; more on this in Example 2 and remark. The approach of fully retaining three-valued semantics is explored in the section on neutral free logic later in this section.

One of the goals of supervaluational semantics is to save the laws of classical logic, such as $A\vee \neg A$, $\neg(A \wedge \neg A)$ while preserving the spirit of free logic, that is allowing for empty singular terms and quantification which is tied to the $E!$-predicate. This is achieved by setting up a multi-stage process, that commences with the following definition:

**Definition 5** (Stage-1 structure $\mathcal{S}_{s1}$). *A stage-1 structure* $\mathcal{S}_{s1}$ is a pair $\langle\cD, \varphi\rangle$, where the following conditions are met:

1. $\cD$ is a possibly empty set.
2. $\varphi$ is a partial function such that:
3. •  If a free individual variable $t$ is in $D_\varphi$, the domain of $\varphi$, then for some $d \in \cD$, $\varphi(t) = d$.
4. •  $\varphi(E!) = \cD$.
5. •  For every $n$-ary predicate $P^n$: $\varphi(P^n) \subseteq \cD^n$.
6. Every object in $\cD$ has a name in the formal language, i.e. if $d \in \cD$, then $d^\bullet$ (the standard-name of $d$) is in the language.

**Definition 6** (Stage-1 Valuation ${\mathcal V}^{s1}$). *The truth-value assignment* ${\mathcal V}^{s1}$ on the structure $\mathcal{S}_{s1}$ is defined as

1. $\notag {\mathcal V}^{s1}({E!} t)= \begin{cases} \top, & \text{if}\ t \in D_\varphi \\ \bot, & \text{otherwise}\end{cases}$
2. $\notag {\mathcal V}^{s1}(P^{n}(t_{1},\ldots,t_{n}))= \begin{cases} \top, & \text{if } t_i {\scriptsize\ (1\leq i \leq n)} \in D_\varphi, \text{ and} \\ & \langle \varphi(t_1), \ldots,\varphi(t_{n})\rangle\in \varphi(P^{n})\\ \bot, & \text{if } t_i {\scriptsize\ (1\leq i \leq n)} \in D_\varphi, \text{ and}\\ & \langle \varphi(t_{1}) \ldots,\varphi(t_{n})\rangle\not\in \varphi(P^{n}) \\ \text{undefined,} & \exists t_i {\scriptsize\ (1\leq i \leq n)} \not\in D_\varphi, \end{cases}$
3. $\notag {\mathcal V}^{s1}(s = t)= \begin{cases} \top, & \text{if } s, t \in D_\varphi \text{ and } \varphi(s) = \varphi(t)\\ \bot, & \text{if } s, t \in D_\varphi \text{ and } \varphi(s) \not = \varphi(t)\\ \bot, & \text{if one of } s \text{ or } t \not\in D_\varphi\\ \text{undefined,} & \text{if both}\ s,t \not\in D_\varphi \end{cases}$

A stage-2 structure over a stage-1 structure is defined as follows:

**Definition 7** (Stage-2 structure over a stage-1 structure). *An $\mathcal{S}_{s2}$-structure with $\langle D', \varphi'\rangle$ is over an $\mathcal{S}_{s1}$-structure with $\langle D, \varphi\rangle$* (or *an $\mathcal{S}_{s2}$-structure is a completion of an $\mathcal{S}_{s1}$-structure*) iff

1. $D' \not = \varnothing$, $D \subseteq D'$,
2. for every $n$-ary predicate $P^n$, $\varphi(P^n) \subseteq \varphi'(P^n)$,
3. for every free individual variable $t$, if $t$ is in the domain of $\varphi$, then: $\varphi'(t) = \varphi(t)$,
4. for every free individual variable $t$, $\varphi(t) \in D'$.

Based on an $\mathcal{S}_{s2}$-structure which is in turn a *completion* (Morscher and Simons 2001a) of an $\mathcal{S}_{s2}$-structure, we define a valuation ${\mathcal V}^{s2}$ as follows:

**Definition 8** (Stage-2 Valuation ${\mathcal V}^{s2}$). *The truth-value assignment* ${\mathcal V}^{s2}$ is defined as

1. If $A$ is a formula such that $A$ is in the domain of ${\mathcal V}^{s1}$, then ${\mathcal V}^{s2}(A) = {\mathcal V}^{s1} = A$.
2. If $A$ is a formula such that $A$ is not in the domain of ${\mathcal V}^{s1}$, then ${\mathcal V}^{s2}$ is defined as follows:
3. $\notag {\mathcal V}^{s2}(P^{n}(t_{1},\ldots,t_{n}))= \begin{cases} \top, & \text{if } \langle \varphi'(t_1) , \ldots,\varphi'(t_{n})\rangle\in \varphi'(P^{n})\\ \bot, & \text{if } \langle \varphi'(t_{1}) \ldots,\varphi'(t_{n})\rangle\not\in \varphi'(P^{n}) \end{cases}$
4. $\notag {\mathcal V}^{s2}(s = t)= \begin{cases} \top, & \text{if}\ \varphi'(s) = \varphi'(t)\\ \bot, & \text{if} \ \varphi'(s) \not = \varphi'(t) \end{cases}$
5. $\notag {\mathcal V}^{s2}(\neg A)= \begin{cases} \top, & \text{if}\ {\mathcal V}^{s2}(A)=\bot\\ \bot, & \text{if}\ {\mathcal V}^{s2}(A)=\top \end{cases}$
6. $\notag {\mathcal V}^{s2}( A\to B)= \begin{cases} \bot, & \text{if}\ {\mathcal V}^{s2}(A)=\top\ and\ {\mathcal V}^{s2}(B)=\bot\\ \top, & \text{otherwise} \end{cases}$
7. $\notag {\mathcal V}^{s2}( \forall x A)= \begin{cases} \top, & \text{if } \forall d^\bullet: \text{if }{\mathcal V}^{s2}(E!d^\bullet) = \top, \\ & \qquad\text{then } {\mathcal V}^{s2}(A[d^\bullet/x])=\top\\ \bot, & \text{if } \exists d^\bullet, {\mathcal V}^{s2}(E!d^\bullet) = \top \text{ and } {\mathcal V}^{s2}(A[d^\bullet/x])=\bot \end{cases}$

The remaining definitional clauses for the Boolean cases and existentially quantified formulas follow as usual. Now with this at hand, we can define a *supervaluation* $\sigma$ which is based on a stage-1 structure and its stage-2 superstructures; in order to indicate the dependence of $\sigma$ with respect to ${\mathcal V}^{s1}$, we write $\sigma_{{\mathcal V}^{s1}}$, and define:

**Definition 9** (Supervaluation $\sigma_{{\mathcal V}^{s1}}$).

1. $\sigma_{{\mathcal V}^{s1}}(A) = \top$ iff ${\mathcal V}^{s2}(A) = \top$ for all stage-2 structures $\mathcal{S}_{s2}$ over stage-1 structure $\mathcal{S}_{s1}$.
2. $\sigma_{{\mathcal V}^{s1}}(A) = \bot$ iff ${\mathcal V}^{s2}(A) = \bot$ for all stage-2 structures $\mathcal{S}_{s2}$ over stage-1 structure $\mathcal{S}_{s1}$.
3. $A$ is not in the domain of $\sigma_{{\mathcal V}^{s1}}(A)$ otherwise, i.e. there is a stage-2 structure over a stage-1 structure with ${\mathcal V}^{s2}(A) = \top$, and there is a stage-2 structure over a stage-1 structure with ${\mathcal V}^{s2}(A) = \bot$.

Since this semantics is more complicated we define core semantical notions in detail and provide some examples.

**Definition 10**.

1. A formula $A$ is *logically true*, or *logically supertrue* iff for all $\mathcal{S}_{s1}$ structures with $\sigma_{\mathcal{S}^{s1}}(A) = \top$. A formula $A$ is *logically false*, or *logically superfalse* iff for all $\mathcal{S}_{s1}$ structures with $\sigma_{\mathcal{S}^{s1}}(A) = \bot$.
2. A formula $A$ is a *logical consequence* of a set of formulas $\Gamma$, or $A$ is a *logical superconsequence* of $\Gamma$ $(\Gamma \models A)$ iff for all $\mathcal{S}_{s1}$ structures: if $\sigma_{\mathcal{S}^{s1}}(B) = \top$, for all $B \in \Gamma$, then $\sigma_{\mathcal{S}^{s1}}(A) = \top$.
3. A set of formulas $\Gamma$ is *satisfiable*, or *supersatisfiable* iff there is a $\mathcal{S}_{s1}$ structure with $\sigma_{\mathcal{S}^{s1}}(A) = \top$, for all $A \in \Gamma$.
4. A formula $A$ is *contingent*, or *supercontigent* iff (1) there is a $\mathcal{S}_{s1}$ structure with $\sigma_{\mathcal{S}^{s1}}(A) = \top$ and a (2) there is a $\mathcal{S}_{s1}$ structure with $\sigma_{\mathcal{S}^{s1}}(A) = \bot$.

Next we offer several examples as a way of elaborating on these definitions.

**Example 2**.

1. $\exists x(x = a)$ is not logically true. Let there be a $\mathcal{S}_{s1}$ structure such that $a$ is not in the domain of $\varphi$; the result follows.
2. $P(a) \models \exists xP(x)$. According to our definition of logical superconsequence, $\exists xP(x)$ follows from $P(a)$ just in case for all $\mathcal{S}_{s1}$ structures: if $\sigma_{\mathcal{S}_{s1}}(P(a)) = \top$, then $\sigma_{\mathcal{S}_{s1}}(\exists xP(x)) = \top,$ now plugging in the clause 1 of Definition 9 we obtain: just in case for all $\mathcal{S}_{s1}$ structures: if ${\mathcal V}^{s2}(P(a)) = \top$ for every completion $\mathcal{S}_{s2}$ of $\mathcal{S}_{s1}$, then ${\mathcal V}^{s2}(\exists xP(x) ) = \top$ for every completion $\mathcal{S}_{s2}$ of $\mathcal{S}_{s1}$.
3. $P(a) \to \exists xP(x)$ is not logically (super-)true. Suppose that $P(a) \to \exists xP(x)$ is logically (super-)true, i.e. for all $\mathcal{S}_{s1}$ structures, $\sigma_{\mathcal{S}_{s1}}(P(a) \to \exists xP(x)) = \top$, just in case ${\mathcal V}^{s2}(P(a) \to \exists xP(x))=\top$ for all $\sigma_{\mathcal{S}_{s2}}$ over $\sigma_{\mathcal{S}_{s1}}$. There is a valuation ${\mathcal V}^{s1}$ such that ${\mathcal V}^{s1}$ is not defined for $P(a)$, so ${\mathcal V}^{s1}(E!a) = {\mathcal V}^{s1}(P(a)) = \bot$, and the desired result follows.
4. $\forall xE!x$ is logically (super-)true. ${\mathcal V}^{s2}(\forall xE!x) = \top$ for all $\mathcal{S}_{s2}$ structures over $\mathcal{S}_{s1}$, since: either ${\mathcal V}^{s2}(E!d^\bullet) = \top$ or ${\mathcal V}^{s2}(E!d^\bullet) = \bot$ for all $d^\bullet$. However, for both cases in by definition 8 clause 7: ${\mathcal V}^{s2} (\forall xE!x) = \top$.

Some remarks about the above examples are in order.

(1) Items 2 and 3 show that strong completeness is not available for logical superconsequence, and with it that compactness fails.

(2) As the previous example highlights the logical consequence relation used in supervaluational semantics is *global* as opposed to the more usual *local*. Local consequence states that $\Gamma$ entails $A$ just in case every model that makes all of $\Gamma$ true, likewise makes $A$ true — the quantifier takes the wide scope. By contrast, global consequence states that if every model makes all of $\Gamma$ true, then every model makes $A$ true -the implication takes the wide scope instead.

### 2.3 Negative Semantics

Let us now turn to a negative structure, which is defined as follows:

**Definition 11** (Negative structure $\mathcal{S}_{n}$). A *Negative structure* $\mathcal{S}_{n}$ is a pair $\langle\cD, \varphi\rangle$, where the following conditions are met:

1. $\cD$ is a possibly empty set.
2. $\varphi$ is a partial function such that:
3. •  If a free individual variable $t$ is in the domain of $\varphi$, then for some $d \in \cD$, $\varphi(t) = d$.
4. •  $\varphi(E!) = \cD_i$.
5. •  For every $n$-ary predicate $P^n$: $\varphi(P^n) \subseteq \cD^n$.
6. Every object in $\cD$ has a name in the formal language, i.e. if $d \in \cD$, then $d^\bullet$ (the standard-name of $d$) is in the language.

**Definition 12** (Negative Valuation ${\mathcal V}^{n}$). *The truth-value assignment* ${\mathcal V}^{n}$ on the structure $\mathcal{S}_n$ is defined as

1. $\notag {\mathcal V}^{n}({E!} t)= \begin{cases} \top, & \text{if}\ t \text{ is in the domain of} \ \varphi\\ \bot, & \text{otherwise} \end{cases}$
2. $\notag {\mathcal V}^{n}(P^{n}(t_{1},\ldots,t_{n}))= \begin{cases} \top, & \text{if } t_i {\scriptsize\ (1\leq i \leq n)} \in D_\varphi \text{ and} \\ & \text{and}\ \langle \varphi(t_{1}), \ldots,\varphi(t_{n})\rangle\in \varphi(P^{n})\\ \bot, & \text{otherwise} \end{cases}$
3. $\notag {\mathcal V}^{n}(s = t)= \begin{cases} \top, & \text{if } s, t \in D_\varphi, \text{ and } \varphi(s) = \varphi(t)\\ \bot, & \text{otherwise} \end{cases}$
4. $\notag {\mathcal V}^{n}(\neg A)= \begin{cases} \top, & \text{if}\ {\mathcal V}^{n}(A)=\bot\\ \bot, & \text{if}\ {\mathcal V}^{n}(A)=\top \end{cases}$
5. $\notag {\mathcal V}^{n}( A\to B)= \begin{cases} \bot, & \text{if}\ {\mathcal V}^{n}(A)=\top\ and\ {\mathcal V}^{n}(B)=\bot\\ \top, & \text{otherwise} \end{cases}$
6. $\notag {\mathcal V}^{n}( \forall x A)= \begin{cases} \top, & \text{if for every } d\in \cD_i, {\mathcal V}^{n}(A[d^\bullet/x])=\top\\ \bot, & \text{if for some } d\in \cD_i, {\mathcal V}^{n}(A[d^\bullet/x])=\bot \end{cases}$
7. *${\mathcal V}^{n}(A)= \top$ iff ${\mathcal V}^{n}(A) \not= \bot$*

**Example 3**.

1. $\exists x(x = a)$ is not logically true. Let $\mathcal{S}_n$ be a negative structure with $D = \varnothing$, so no individual variable is in the domain of $\varphi$, so ${\mathcal V}_n(a = a) = \bot$ for all free individual variable, and so ${\mathcal V}_n(\exists x(x = a)) = \bot$.
2. $P(a) \models \exists xP(x)$ is correct. Suppose it is not, then there is a $\mathcal{S}_n$ structure with ${\mathcal V}_n(P(a)) = \top$, and ${\mathcal V}_n(\exists xP(x)) = \bot$, which is impossible.
3. $P(a) \to \exists xP(x)$ is logically true, using basically the same argument as before.
4. $\forall xE!x$ is logically true. For any $\mathcal{S}_n$ with a non-empty domain the claim is obviously true; for any $\mathcal{S}_n$ structure with empty domain it is vacuously true due to clause 6 of definition 6.

### 2.4 Generalized Semantics

The approach of utilizing *generalized semantics* was introduced by Pavlović and Gratzl (2021) to facilitate meta-theory. In a nutshell, the idea of this approach is that for the proofs of soundness and completeness, a *description* of a model, rather than a full-blown model, will suffice. This allows for a simplified presentation of semantics (eschewing partial functions) and, given that it has a greater level of generality, can be applied to different particular semantic approaches. Great use of this feature of generalized semantics was made to offer a uniform picture of a variety of positive and negative free logics.

**Definition 13** (Negative structure $\mathcal{S}_{n}$). *A negative structure* $\mathcal{S}_{n}$ is a pair $\langle\cD,\varphi\rangle$, where ${\mathcal D}=a_{1},\ldots, b_{1},\ldots$ countable list of free individual variables, and $\varphi$ an *interpretation function* on $\mathcal{L}:$

- $\varphi(t)=t$, where $t \in \cD$ (to emphasize its dual role we will abuse the notation slightly and write ${\mathcal D}$ as $\varphi(\cD)$)
- $\varphi({E!})\subseteq \cD$
- $\varphi(=)=Ref \cup Id$, closed under symmetry and transitivity, where:
- •  $Ref=\{\langle t,t\rangle\ |\ t\in \varphi({E!})\}$
- •  $Id\subseteq \varphi({E!})\times \varphi({E!})$
- $\varphi(P^{n})\subseteq \varphi({E!})^{n}$ such that if $\langle s,t\rangle\in \varphi(=)$, then $\langle\ldots, s_{i},\ldots\rangle\in \varphi(P^{n})$ iff $\langle\ldots, t_{i},\ldots\rangle\in \varphi(P^{n})$, for any $n$ and any $1\leq i\leq n$.

A positive structure is defined as

**Definition 14** (Positive structure $\mathcal{S}_{p}$). *The positive structure $\mathcal{S}_{p}$ differs from $\mathcal{S}_{n}$ only in that*

- $Ref=\{\langle t,t\rangle\ |\ t\in \varphi({\mathcal D})\}$,
- $Id\subseteq \varphi(\cD)\times \varphi(\cD)$ and
- $\varphi(P^{n})\subseteq \varphi(\cD)^{n}$.

The clause $\varphi({E!})\subseteq \cD$ can be omitted, since ${E!}$ is defined like any other unary predicate by the last clause of the definition, and not specified as a logical predicate. As another consequence of this definition, if $s=t$ then ${E!} s$ iff ${E!} t$.

To create a model we attach to these structures a valuation function, propositionally classical while incorporating free quantification.

**Definition 15** (Valuation ${\mathcal V}$). *The truth-value assignment* ${\mathcal V}$ on the structure $\langle\cD,\varphi\rangle$ is defined as

- ${\mathcal V}(P^{n}(t_{1},\ldots,t_{n}))=\top$ iff $\langle t_{1},\ldots,t_{n}\rangle\in \varphi(P^{n})$, and $\bot$ otherwise.
- Standard for connectives.
- ${\mathcal V}(\forall x A)=\top$ iff for every $t\in \varphi({E!})$ it holds that ${\mathcal V}(A[t/x])=\top$, and $\bot$ otherwise.
- ${\mathcal V}(\exists x A)=\top$ iff for some $t\in \varphi({E!})$ it holds that ${\mathcal V}(A[t/x])=\top$, and $\bot$ otherwise.

By way of comparison, from these two structures we can likewise define a *classical* structure, namely a structure validating, under the valuation above, precisely all of classical first order logic:

**Definition 16** (Structure $\mathcal{S}_{c}$). A *classical structure* $\mathcal{S}_{c}$ is any structure such that it is both an $\mathcal{S}_{p}$ and an $\mathcal{S}_{n}$.

### 2.5 Neutral Semantics

A similar investigation is offered for neutral free logics based on strong (Kleene 1938)[^kleene-1938] and weak Kleene conditional. For simplicity the presentation here is limited to negation and implication, identity-free segment.

Even though there are multiple possible neutral free logics, there is good reason to see it as a single kind of logic, since the treatment of quantifiers does not vary between these interpretations, and the systems under consideration here vary only the type of implication used.

**Definition 17** (Neutral structure $\mathcal{S}_{nt}$). A *neutral structure* $\mathcal{S}_{nt}$ is a pair $\langle\cD,\varphi\rangle$, where ${\mathcal D}=a_{1},\ldots, b_{1},\ldots$ countable list of free individual variables, and $\varphi$ an *interpretation function* on $\mathcal{L}:$

- $\varphi(t)=t$, where $t \in \cD$ (to emphasize its dual role we will abuse the notation slightly and write ${\mathcal D}$ as $\varphi(\cD)$)
- $\varphi({E!})\subseteq \varphi(\cD)$,
- $\varphi(P^{n})\subseteq \varphi({E!})^{n}$.

Notice that the neutral structure here is presented as a negative structure in order to simplify the presentation of the valuations below.

**Definition 18** (Weak Valuation ${\mathcal V}^{-}$). *The truth-value assignment* ${\mathcal V}^{-}$ on the structure $\langle\cD,\varphi\rangle$ is defined as

1. $\notag {\mathcal V}^{-}({E!} t)= \begin{cases} \top, & \text{if}\ t\in \varphi({E!})\\ \bot, & \text{otherwise} \end{cases}$
2. $\notag {\mathcal V}^{-}(P^{n}(t_{1},\ldots,t_{n}))= \begin{cases} +, & \text{if for some } 1\leq i\leq n, t_i \notin \varphi({E!})\\ \top, & \text{if}\ \langle t_{1},\ldots,t_{n}\rangle\in \varphi(P^{n})\\ \bot, & \text{otherwise} \end{cases}$
3. $\notag {\mathcal V}^{-}(\neg A)= \begin{cases} \top, & \text{if}\ {\mathcal V}^{-}(A)=\bot\\ \bot, & \text{if}\ {\mathcal V}^{-}(A)=\top\\ +, & \text{otherwise} \end{cases}$
4. $\notag {\mathcal V}^{-}( A\to B)= \begin{cases} +, & \text{if}\ {\mathcal V}^{-}(A)=+\ or\ {\mathcal V}^{-}(B)=+ \\ \bot, & \text{if}\ {\mathcal V}^{-}(A)=\top\ and\ {\mathcal V}^{-}(B)=\bot\\ \top, & \text{otherwise} \end{cases}$
5. $\notag {\mathcal V}^{-}( \forall x A)= \begin{cases} \top, & \text{if for every } t\in \varphi({E!}), {\mathcal V}^{-}(A[t/x])=\top\\ \bot, & \text{if for some } t\in \varphi({E!}), {\mathcal V}^{-}(A[t/x])=\bot\\ +, & \text{otherwise} \end{cases}$

**Definition 19** (Strong Valuation ${\mathcal V}^{3}$). *The truth-value assignment* ${\mathcal V}^{3}$ on the structure $\langle\cD,\varphi\rangle$ is defined as

1. $\notag {\mathcal V}^{3}(E! t)= \begin{cases} \top, & \text{if}\ t\in \varphi(E!)\\ \bot, & \text{otherwise} \\ \end{cases}$
2. $\notag {\mathcal V}^{3}(P^{n}(t_{1},\ldots,t_{n}))= \begin{cases} +, & \text{if for some } 1\leq i\leq n, t_i \notin \varphi({E!})\\ \top, & \text{if } \langle t_{1},\ldots,t_{n}\rangle\in \varphi(P^{n})\\ \bot, & \text{otherwise} \end{cases}$
3. $\notag {\mathcal V}^{3}(\neg A)= \begin{cases} \top, & \text{if}\ {\mathcal V}^{3}(A)=\bot\\ \bot, & \text{if}\ {\mathcal V}^{3}(A)=\top\\ +, & \text{otherwise} \end{cases}$
4. $\notag {\mathcal V}^{3}( A\to B)= \begin{cases} \top, & \text{if}\ {\mathcal V}^{3}(A)=\bot \ or\ {\mathcal V}^{3}(B)=\top \\ \bot, & \text{if}\ {\mathcal V}^{3}(A)=\top\ and\ {\mathcal V}^{3}(B)=\bot\\ +, & \text{otherwise} \end{cases}$
5. $\notag {\mathcal V}^{3}( \forall x A)= \begin{cases} \top, & \text{if for every } t\in \varphi({E!}), {\mathcal V}^{3}(A[t/x])=\top\\ \bot, & \text{if for some } t\in \varphi({E!}), {\mathcal V}^{3}(A[t/x])=\bot\\ +, & \text{otherwise} \end{cases}$

When it comes to supervaluations of this generalized semantics, a completion of a neutral structure, $\varphi '$, is identical to $\varphi$ it completes, except that $\varphi'(P^n) \subseteq \varphi'(D)$ (therefore making it a positive structure) such that $\varphi(P^n) \subseteq \varphi'(P^n)$, and the valuations for atoms do not contain the case for $+$ (thus making it moot for logical symbols).

We again offer several examples, to illustrate both the functioning of the two systems, and also their differences.

**Example 4**.

1. $\forall x {E!} x$ is valid in both weak and strong models; proof, same as in Example 2, follows immediately from the valuation for ${E!}$.
2. $\forall x Px \to P(a)$ is always non-false (so *tolerantly valid*) under either valuation, although not always true (so not *strictly valid*) (for more on strict and tolerant validity, see (Cobreros et al. 2012)[^cobreros-2012]). If $P(a)$ is false, then ${E!} a$ is true, and therefore $\forall x P(x)$ is false. However, if ${E!} a$ is false, this formula is third-valued under weak valuation, and either third-valued (if $\forall x P(x)$ is true) or true (if $\forall x P(x)$ is false) under the strong evaluation.
3. $\forall x P(x) \to ({E!} a \to P(a))$ is true under the strong evaluation. ${E!} a$ is crisp, meaning it is always true or false. If false, ${E!} a \to P(a)$ is true and the whole formula is true. If true, then $P(a)$ is either true or false. In the former case ${E!} a \to P(a)$ is true and the whole formula is true. In the latter case, $\forall x P(x)$ is false and the whole formula is again true.
4. $\forall x P(x) \to ({E!} a \to P(a))$ is merely non-false under the weak evaluation. If ${E!} a$ is true, the reasoning is the same as in the previous point. But if it is false, the whole formula is third-valued.

## 3. Formal Proof Systems for Free Logics

Traditional presentation of proof-systems for free logic has more often been in Hilbert, or axiom, style and due to this historical fact we first introduce some formalizations of variants of free logic by using this style. However, further types of proof systems have been developed which facilitated fruitful research in this area; so, most of this section is devoted to these more useful proof systems. Before stating systems for Hilbert-style calculi of free logic, we recall such a system for classical logic.  It and the rest of the systems presented here are formulated in a first-order language $\bL$ without sentence letters or function symbols, whose primitive logical operators are negation (not) ‘${\neg}$’, the conditional (if-then) ‘$\rightarrow$’, the universal quantifier (for all) ‘$\forall$’, identity ‘=’ and ‘E!’, the others being defined as usual. We assume for the sake of definiteness that the formulas of $\bL$ are closed (contain no unquantified variables) and that they may be vacuously quantified (have the form $\forall xA$ or $\exists xA$, where $x$ does not occur free in $A)$. An occurrence of a variable is *quantified* if it lies within the scope of an operator such as ‘$\forall$’ or ‘$\exists$’ that binds that variable; otherwise it is *free*. Each axiom system has *modus ponens* as the sole rule of inference.

**Definition 20** (Axioms for classical logic).

$$\begin{align} \tag{H1} &\text{Classical tautologies}\\ \tag{H2} &\forall x (A \to B) \to (\forall x A \to \forall xB)\\ \tag{H3} &A \to \forall x A, x \text{ not free in }A\\ \tag{H4} &\forall xA \to A[t/x]\\ \tag{H5} &s = t \to (A \to A[t//s])\\ \tag{H6} &t = t\\ \tag{H7} &\forall xA,\text{ if } A\text{ is tautologous} \end{align} $$

### 3.1 Hilbert-style Systems of Free Logic

In contrast, the Hilbert-style systems for free logics are below, starting with one for the positive variant, PFL. Note in particular Axiom (P4).

**Definition 21** (Axioms for positive free logic).

$$\begin{align} \tag{P1} &\text{Classical tautologies}\\ \tag{P2} &\forall x (A \to B) \to (\forall x A \to \forall xB)\\ \tag{P3} &A \to \forall x A, x \text{ not free in }A\\ \tag{P4} &\forall xA \to (E!t \to A[t/x])\\ \tag{P5} &s = t \to (A \to A[t//s])\\ \tag{P6} &t = t\\ \tag{P7} &\forall xA,\text{ if } A\text{ is tautologous}\\ \tag{P8} &\forall xE! x\\ \end{align} $$

Next is a Hilbert-style calculus for negative free logic, NFL. Compared to the one for PFL, note Axiom (N6) and the added Axiom (N9).

**Definition 22** (Axioms for negative free logic).

$$\begin{align} \tag{N1} &\text{Classical tautologies}\\ \tag{N2} &\forall x (A \to B) \to (\forall x A \to \forall xB)\\ \tag{N3} &A \to \forall x A, x \text{ not free in }A\\ \tag{N4} &\forall xA \to (E!t \to A[t/x])\\ \tag{N5} &s = t \to (A \to A[t//s])\\ \tag{N6} &E!t \to t = t\\ \tag{N7} &\forall xA,\text{ if } A\text{ is tautologous}\\ \tag{N8} &\forall xE! x\\ \tag{N9} &P[t_1, ..., t_n] \to (E!t_1 \wedge ... \wedge E!t_n)\\ \end{align} $$

For definitions of *derivability, provability*, and further syntactic concepts and theorems, e.g. deduction theorem, see the entry on classical logic.

**Some theorems.** We exhibit some interesting theorems of free logic, beginning with with positive free logic and *Hintikka's Law*: $E!s \leftrightarrow \exists x(x = s)$ The proof from left to right is straightforward:

$$\begin{align} \tag*{1.} &\forall x\neg(x = t) \to (E!t \to \neg(x= t) ) &\text{[from P4]} \\ \tag*{2.} &t = t &\text{[from P6]} \\ \tag*{3.} &t = t \to (E!t \to \neg \forall x \neg (x = t)) &\text{[from 1 by logic]} \\ \tag*{4.} &E!t \to \neg \forall x \neg (x = t) &\text{[from 2,3 by MP]} \end{align}$$

On the other hand, the proof from right to left is slightly more convoluted:

$$\begin{align} \tag*{ 1.} &s=t \to (E!s \to E!t) &\text{[from P5]} \\ \tag*{ 2.} &\forall x((x = t) \to (E!x \to E!t)) &\text{[from 1, P7]} \\ \tag*{ 3.} &\forall x(\neg E!t \to (E!x \to \neg (x =t))) &\text{[from 2 by logic]} \\ \tag*{ 4.} &\forall x\neg E!t \to \forall x(E!x \to \neg (x =t)) &\text{[from 3,P2 by logic]} \\ \tag*{ 5.} &\neg E!t \to \forall x \neg E!t &\text{[from P3]} \\ \tag*{ 6.} &\neg E!t \to \forall x(E!x \to \neg (x =t)) &\text{[from 4,5 by logic]} \\ \tag*{ 7.} &\forall x (E!x \to \neg (x=t)) \\ &\qquad \to (\forall xE!x \to \forall x\neg (x=t)) &\text{[from P2]} \\ \tag*{ 8.} &\forall xE!x \to (\forall x(E!x \to \neg (x=t)) \\ &\qquad \to \forall x \neg (x=t)) &\text{[from 7,P2 by logic]} \\ \tag*{ 9.} &\forall xE!x &\text{[from P8]} \\ \tag*{ 10.} &\forall x(E!x \to \neg (x=t)) \to \forall x \neg (x=t) &\text{[from 8,9 by MP]} \\ \tag*{ 11.} &\neg E!t \to \forall x\neg x=t &\text{[from 6,10 by logic]} \\ \tag*{ 12.} &\exists x (x=t) \to E!t &\text{[from 11 by logic]} \end{align}$$

Now moving to negative free logic, we have the stronger claim of

$$ E!t \leftrightarrow t = t\tag{E!-SI equivalence} $$

as a theorem, since: $E!t \to t = t$ is an axiom of type N6, and $t= t \to E!t$ an axiom of type N9.

In contrast to positive free logic, NFL also proves the *indiscernibility of non-existents*:

$$ \neg E!s \wedge \neg E!t \to (P[s] \to P[t])\tag{Indiscernability of non-E!} $$

$$\begin{align} \tag*{1.} &P[s] \to E!s &\text{[from N9]} \\ \tag*{2.} &P[s] \wedge \neg P[t] \to E!s \vee E!t &\text{[from 1 by logic]} \\ \tag*{3.} &\neg (P[s] \to P[t]) \to \neg (\neg E!s \wedge \neg E!t) &\text{[from 2 by logic]} \\ \tag*{4.} &\neg E!s \wedge \neg E!t \to (P[s] \to P[t]) &\text{[from 3 by logic]} \end{align}$$

Moreover, indiscernibility of non-existents generalizes to $\neg E!s \wedge \neg E!t \to (A[s] \to A[t])$ by induction on the complexity of $A$.

Clearly this formula is not a theorem of PFL as an application of the soundness theorem shows: let's construct a Meinongian structure with $D_i = \varnothing,$ and $D_o = \{0, 1\}$ with $\varphi(s) = 0,$ and $\varphi(t) = 1,$ and $\varphi(P) = \{0\}.$ Then ${\mathcal V}(\neg E!s \wedge \neg E!t \to (P[s] \to P[t])) = \bot,$ and so PFL $\not \vdash \neg E!s \wedge \neg E!t \to (P[s] \to P[t]).$

Finally, that truth implies the existential claim likewise holds in negative free logic:

$$ P(s) \to \exists xP(x)\tag{TIEx}$$

$$\begin{align} \tag*{1.} &E!s \to (P(s) \to \exists xP(x)) &\text{[from N4 by logic]} \\ \tag*{2.} &P(s) \to E!s &\text{[from N9]} \\ \tag*{3.} &P(s) \to \exists xP(x) &\text{[from 1,3 by logic]} \end{align}$$

**Collapse into classical logic.** It is quite instructive to ask what happens if positive and negative free logic are combined. Semantically, given Definition 3 and Definition 11 and their respective valuations, the answer might be elusive. However, just like with the generalized semantics, syntactically the answer is straightforward. So, the axioms and rules of inference are as for PFL and NFL taken jointly.

$E!t \to (\forall x A \to A)$ follows from axiom 3 and logic, in the light of NFL-theorem $E!t \leftrightarrow t = t$, we obtain: $t=t \to (\forall x A \to A)$ so by PFL axiom P6, the desired result, i.e. $\forall x A \to A$ follows.

(This equivalence is sometimes taken as a definition of $E!t$.) Identity statements in negative free logic thus have existential implications. This may be problematic in certain contexts. According to Shapiro and Weir (2000), for example, use of such an “existential” notion of identity sullies the “epistemic innocence” of some recent efforts to base neo-logicist philosophies of mathematics on free logic.

### 3.2 Quantified Sequent Calculi

Most of the recent representations of a proof system for free logics has been in the form of sequent calculi. These approaches are favored for their transparency arising from locality — all the relevant information for evaluating an inference step is contained locally at within the point of application, as well as modularity — extensions do not alter the properties of the base system. For an overview of proof theory in general see the entry on proof theory, and for its history and the modern developments we utilize here see the entry on the development of proof theory.

The basic unit of a sequent calculus is a *sequent* $\Gamma \Rightarrow \Delta$, where $\Gamma$ and $\Delta$ are finite multisets of (closed) formulas, intuitively understood as ``if everything left of the arrow holds, then something on the right of the arrow holds''. All the formulas except $\Gamma$ and $\Delta$ in the schematic presentation below are called *active* formulas of the rule if they occur only in the upper sequent(s) and *principal* if they occur in the lower sequent of the rule.

In this section we will present the sequent calculi for the bivalent positive and negative free logics with and without identity. The base is the classical propositional calculus G3cp:

**Initial sequent:** $P,\Gamma \Rightarrow \Delta, P$, where $P$ is prime

**Propositional rules:**

$$\begin{aligned} &\frac{\Gamma \Rightarrow \Delta, A}{ \neg A, \Gamma \Rightarrow \Delta} L\neg && \frac{A, \Gamma \Rightarrow \Delta }{\Gamma \Rightarrow \Delta, \neg A} R\neg \\ & &&\\ & \frac{A, B, \Gamma \Rightarrow \Delta}{A \wedge B, \Gamma \Rightarrow \Delta}L\wedge && \frac{\Gamma \Rightarrow \Delta, A \qquad \Gamma \Rightarrow \Delta, B }{\Gamma \Rightarrow \Delta, A \wedge B } R\wedge \\ & &&\\ & \frac{A, \Gamma \Rightarrow \Delta \qquad B, \Gamma \Rightarrow \Delta }{A \vee B, \Gamma \Rightarrow \Delta} L\vee && \frac{\Gamma \Rightarrow \Delta, A, B}{\Gamma \Rightarrow \Delta, A\vee B} R\vee \\ & &&\\ & \frac{\Gamma \Rightarrow \Delta, A \qquad B, \Gamma \Rightarrow \Delta }{A \to B, \Gamma \Rightarrow \Delta} L \to && \frac{A, \Gamma \Rightarrow \Delta, B}{\Gamma \Rightarrow \Delta, A \to B} R\to \end{aligned}$$

Figure **G3cp**

To obtain the first order quantified calculus G3c, one would add the rules for quantifiers:

**Quantifier rules:**

$$\begin{aligned} \frac{A [t/x] , \forall x A , \Gamma \Rightarrow \Delta}{\forall x A , \Gamma \Rightarrow \Delta} L\forall && \frac{\Gamma \Rightarrow \Delta, A [ t/x] }{\Gamma \Rightarrow \Delta, \forall x A} R\forall^* \\ &&\\ \frac{A [ t/x], \Gamma \Rightarrow \Delta}{\exists x A , \Gamma \Rightarrow \Delta} L\exists^* && \frac{\Gamma \Rightarrow \Delta, \exists x A, A[ t/x]}{\Gamma \Rightarrow \Delta, \exists x A} R \exists \end{aligned}$$

$t$ is fresh (not occurring in the conclusion of the rule) in rules marked with ${}^*$.

Figure **Classical quantifier rules**

To add identity, we extend two more rules, for reflexivity of identity (Ref) and the replacement principle (Repl):

**Identity rules:**

$$\begin{aligned} \frac{t=t,\Gamma \Rightarrow \Delta }{\Gamma \Rightarrow \Delta} =_{Ref} && \frac{s=t, P[s], P[t], \Gamma \Rightarrow \Delta}{s=t, P[t], \Gamma \Rightarrow \Delta} =_{Repl} \end{aligned}$$

Figure **Identity rules**

The replacement rule is defined only for primes, but it suffices to prove all instances of replacement, so no generality is lost here. At the same time, the rule as presented has a geometric form, which means that its addition in the present form will be modular, not upsetting the properties of the base. All of these rules taken together constitute what is most commonly thought of as G3c.

### 3.3 Positive Free Logic

To obtain a sequent calculus G3pf for positive free logic, we replace the classical quantifier rules by free quantifier rules, which limit quantification to ${E!}$:

**Quantifier rules:**

$$\begin{aligned} \frac{ A [t/x] ,{E!} t, \forall x A , \Gamma \Rightarrow \Delta}{{E!} t,\forall x A , \Gamma \Rightarrow \Delta} L \forall && \frac{{E!} t, \Gamma \Rightarrow \Delta, A [ t/x]}{\Gamma \Rightarrow \Delta, \forall x A} R\forall^* &&\\ &&\\ \frac{{E!} t, A [ t/x], \Gamma \Rightarrow \Delta}{\exists x A , \Gamma \Rightarrow \Delta} L\exists^* && \frac{{E!} t, \Gamma \Rightarrow \Delta, \exists x A, A[ t/x]}{{E!} t,\Gamma \Rightarrow \Delta, \exists x A} R \exists \end{aligned}$$

$t$ is fresh (not occurring in the conclusion of the rule) in rules marked with ${}^*$.

Figure **Free quantifier rules**

This substitution will suffice to demonstrate two axioms which characterize free logic, of Restricted generalization (RG) and Restricted specification (RS):

$$\forall x {E!} x \tag{RG}$$

$$\forall x A \to ({E!} t \to A[t/x])\tag{RS}$$

The first of these principles corresponds to the rule R$\forall$, and the second to the rule L$\forall$. RG states that (free) quantifiers apply to all, and RS that they apply only to, the instances of ${E!}$. By contrast, the principle of Unrestricted specification holds for classical FOL, but not free logics:

$$\forall x A\to A[t/x] \tag{US}$$

One can easily see that this will not be derivable using the free rules due to the presence of the extra condition $E! t$ in the conclusion of the rule.

These observations on the functioning of the quantifier rules will hold for both positive free logic and negative free logic, but the latter needs to be distinguished by further modifications we outline in the next section.

### 3.4 Negative Free Logic

To obtain a sequent calculus G3nf for negative free logic, we extend the propositional base of G3cp with the free quantifier rules, much like in the positive case (hence the observations of the previous section still hold), but instead of the standard identity rules we add the following relational rules:

**Relational rules:**

$$ \frac{{E!} t, P[t], \Gamma\Rightarrow\Delta}{P[t], \Gamma\Rightarrow\Delta}{E!} \qquad \frac{t=t, P[t], \Gamma\Rightarrow\Delta}{P[t], \Gamma\Rightarrow\Delta} =_{Ref} $$ $$ \frac{s=t, P[s], P[t], \Gamma \Rightarrow \Delta}{s=t, P[t], \Gamma \Rightarrow \Delta}=_{Repl} $$

Notice that the rule for reflexivity of identity has been weakened, now to apply only to terms occurring within atoms. Since the rule for $E!$ is similarly restricted, we get that $E! t$ iff $t = t$. Therefore, instead of the classical reflexivity of identity, we get the restricted version (remember that free quantification is restricted):

$$\forall x (x=x) \tag{RRef}$$

All the atomic formulas (even self-identities) are restricted to $E!$. Therefore, the following principle, that truth implies ${E!}$ (TIE), is characteristic of negative free logic:

$$P[t] \to {E!} t \tag{TIE}$$

Notice that this will not hold for positive free logic when $P[t]$ is $t=t$.

Since all the relational rules once again follow the geometric rule schema, modularity is once again in effect and their additions do not alter the structural properties of the base system.

Positive free logic is the most widely used of the free logics, at least in part because it represents the least intervention into the familiar quantified first-order logic. Compared to it, negative free logic adds a rule while weakening another, meaning that neither is a proper part of the other. As one consequence, not too surprising if one observes the form of their respective rules, ${E!} t$ is equivalent to self-identity, $t=t$, making it also straightforwardly expressible in an existence-free language.

### 3.5 Neutral Free Logic

The proof-theoretic presentation of the system for neutral free logic here, due to Pavlović and Gratzl (2023) starts off from the sequent calculus for weak Kleene logics from (Fjellstad 2020)[^fjellstad-2020]. The system there is a five-sided calculus, with the fifth side introduced to account for crispness of formulas (formulas are *crisp* when they are either true or false), specifically in order to deal with the falsity conditions of the universal quantifier (in weak Kleene logics it requires all instances to be crisp).

However, in neutral free logic, quantification is limited to the extension of the predicate ${E!}$, which is itself always crisp (subsequently, $P(t_1...t_n)$ is crisp iff ${E!} t_i$ for $1\leq i\leq n$). As a result, if for some $t_i$ such that ${E!} t_i$ the instantiated formula $A[t_i/x]$ is not crisp, then for any such $t_i$ it is not crisp. Therefore, it follows from $A[t_i/x]$ being false that it is crisp for every $t_i$ s.t. ${E!} t_i$, and therefore the additional crispness condition is not required.

The basic building block of the system is a (dual-)sequent of the form

$$\Gamma\ |\ \Gamma' \Rightarrow \Delta\ |\ \Delta'$$

where $\Gamma$, $\Gamma'$, $\Delta$ and $\Delta'$ are again multisets, which is notational variation of the generalized propositional sequent calculi for weak and strong Kleene in (Indrzejczak 2021b) (see also Bochman 1998; Degauquier 2016)[^bochman-1998][^degauquier-2016], extended to quantification.

The vertical bar ‘$|$’ is a structural comma (i.e. a structural conjunction between antecedents and a structural disjunction between succedents).

In an implication format, the reading of this sequent is “if everything in $\Gamma$ is true and everything in $\Gamma'$ non-false, then either something in $\Delta$ is non-false or something in $\Delta'$ is true”, while in the negative-conjunction reading it states “it is not the case that everything in $\Gamma$ is true, everything in $\Delta$ is false, everything in $\Gamma'$ is non-false and everything in $\Delta'$ is non-true”.

**Quantifier rules:**

$$\begin{aligned} \frac{{E!} t, \forall x A, A[t/x],\Gamma\ |\ \Gamma' \Rightarrow \Delta\ |\ \Delta'}{{E!} t, \forall x A, \Gamma\ |\ \Gamma' \Rightarrow \Delta\ |\ \Delta'} L\forall &\\ &\\ \frac{{E!} t, \Gamma\ |\ \Gamma' \Rightarrow A[t/x], \Delta\ |\ \Delta'}{\Gamma\ |\ \Gamma' \Rightarrow \forall x A, \Delta\ |\ \Delta'}R\forall^* &\\ &\\ \frac{{E!} t,\Gamma \ |\ \forall x A, A[t/x], \Gamma' \Rightarrow \Delta\ |\ \Delta'}{{E!} t,\Gamma \ |\ \forall x A, \Gamma' \Rightarrow \Delta\ |\ \Delta'}L'\forall&\\ &\\ \frac{{E!} t, \Gamma\ |\ \Gamma' \Rightarrow \Delta\ |\ \Delta',A[t/x]}{ \Gamma\ |\ \Gamma' \Rightarrow \Delta\ |\ \Delta',\forall x A}R'\forall^*& \end{aligned}$$

**${E!}$ rules:**

$$\begin{aligned} &\frac{{E!} t,P[t],\Gamma\ |\ \Gamma' \Rightarrow \Delta\ |\ \Delta'}{P[t],\Gamma\ |\ \Gamma' \Rightarrow \Delta\ |\ \Delta'}L{E!} && \frac{{E!} t,\Gamma\ |\ \Gamma' \Rightarrow P[t],\Delta\ |\ \Delta'}{\Gamma\ |\ \Gamma' \Rightarrow P[t],\Delta\ |\ \Delta'}R{E!} \\ & &&\end{aligned}$$ $$\begin{aligned}& \frac{\{{E!} t_{i}\}_{1\leq i\leq n},P(t_1 ... t_n),\Gamma\ |\ \Gamma' \Rightarrow \Delta\ |\ \Delta'}{\{{E!} t_{i}\}_{1\leq i\leq n},\Gamma\ |\ \Gamma', P(t_1 ... t_n)\Rightarrow\Delta\ |\ \Delta'}L'{E!} &&\\ &&&\\ &\frac{\{{E!} t_{i}\}_{1\leq i\leq n},\Gamma\ |\ \Gamma' \Rightarrow P(t_1 ... t_n),\Delta\ |\ \Delta'}{\{{E!} t_{i}\}_{1\leq i\leq n}, \Gamma\ |\ \Gamma' \Rightarrow \Delta\ |\ \Delta', P(t_1 ... t_n)}R'{E!} &&\\ &&&\end{aligned}$$ $$\begin{aligned}& \frac{{E!} t, \Gamma\ |\ \Gamma' \Rightarrow \Delta\ |\ \Delta' }{\Gamma\ |\ \Gamma', {E!} t\Rightarrow \Delta\ |\ \Delta'}L\text{Tr}_{{E!}} && \frac{\Gamma\ |\ \Gamma' \Rightarrow {E!} t, \Delta\ |\ \Delta'}{\Gamma\ |\ \Gamma' \Rightarrow \Delta\ |\ \Delta', {E!} t}R\text{Tr}_{{E!}} \end{aligned}$$

Where $P$ is atomic; $P[t]$ is an atom other than ${E!} t$ containing $t$; $P(t_1 ... t_n)$ is an atom other than ${E!} t$ containing precisely terms $t_1 ... t_n$ and in that order; $t$ is fresh in rules marked with $*$.

Figure **Neutral free rules**

Rules L${E!}$ and R${E!}$ tell us, in parallel to the rule ${E!}$ of negative free logic, that in true atoms all terms are ${E!}$, but also that all *false* atoms likewise contain only terms that are ${E!}$. So, all crisp atoms contain only denoting terms. Conversely, rules L’${E!}$ and R’${E!}$ tell us that atoms containing only denoting terms are crisp (true or false, respectively). Finally, transfer rules L$Tr_{E!}$ and R$Tr_{E!}$ tell us that ${E!}$ atoms themselves are always crisp.

Next, we proceed with identifying the propositional base to attach these rules to. Two obvious candidates identified in the literature (Priest 2008)[^priest-2008] are weak Kleene (Bochvar and Bergmann 1981)[^bochvar-1981] and strong Kleene (Kleene 1938)[^kleene-1938] logics, of which the former tends to be more prevalent.

#### Weak Kleene base

In discussing approaches to neutral free logic(s), Lehmann (1980, 1994, 2002) argues as follows:

> The underlying semantic rationale for neutral free semantics is Frege’s functional view of reference: predicates and ‘=’ name functions from individuals to truth-values. If functions are operations, as Frege seems to have thought, then the semantic rules governing subject-predicate and identity constructions are [such that] where there is no input to an operation, there is no output either. The truth-functional connectives name truth-functions, so the same line of thought dictates the weak tables for them. (Lehmann 2002, 234)[^lehmann-2002]

Following this reasoning the first sequent calculus we observe, G3wnf, will be obtained by adding to the free quantifier and relational rules weak Kleene base. To make things more manageable, here we restrict ourselves to the negation and implication fragment of it:

**Initial sequents (is):**

$$P, \Gamma\ |\ \Gamma' \Rightarrow \Delta\ |\ \Delta', P \tag{\(is_1\)}$$ $$ \Gamma\ |\ \Gamma', P\Rightarrow P,\Delta\ |\ \Delta'\tag{\(is_2\)} $$ $$ P, \Gamma\ |\ \Gamma' \Rightarrow P, \Delta\ |\ \Delta'\tag{\(is_3\)}$$

**Propositional rules:**

$$\begin{aligned} \frac{\Gamma\ |\ \Gamma'\Rightarrow A,\Delta\ |\ \Delta'}{\neg A, \Gamma\ |\ \Gamma' \Rightarrow \Delta\ |\ \Delta'}L\neg && \frac{A, \Gamma\ |\ \Gamma' \Rightarrow \Delta\ |\ \Delta'}{\Gamma\ |\ \Gamma' \Rightarrow \neg A, \Delta\ |\ \Delta'}R\neg\\ &&\\ \frac{\Gamma\ |\ \Gamma' \Rightarrow \Delta\ |\ \Delta', A}{\Gamma\ |\ \Gamma', \neg A\Rightarrow \Delta\ |\ \Delta'}L'\neg && \frac{\Gamma\ |\ \Gamma', A \Rightarrow \Delta\ |\ \Delta'}{\Gamma\ |\ \Gamma' \Rightarrow \Delta\ |\ \Delta',\neg A}R'\neg\\ && \end{aligned}$$

$$\begin{aligned} &\small \frac{A,B, \Gamma\ |\ \Gamma' \Rightarrow \Delta\ |\ \Delta' \qquad \Gamma\ |\ \Gamma' \Rightarrow A, B, \Delta\ |\ \Delta'\qquad B, \Gamma\ |\ \Gamma' \Rightarrow A, \Delta\ |\ \Delta'}{A\to B, \Gamma\ |\ \Gamma' \Rightarrow \Delta\ |\ \Delta'}\normalsize L\to\\ &\end{aligned}$$ $$\begin{aligned}\normalsize\frac{A,\Gamma\ |\ \Gamma' \Rightarrow B, \Delta\ |\ \Delta'}{\Gamma\ |\ \Gamma' \Rightarrow A\to B,\Delta\ |\ \Delta'}R\to&\\ &\\ \frac{\Gamma\ |\ \Gamma' \Rightarrow \Delta\ |\ \Delta', A\qquad \Gamma \ |\ B, \Gamma'\Rightarrow \Delta\ |\ \Delta'}{\Gamma \ |\ A\to B, \Gamma'\Rightarrow \Delta\ |\ \Delta'}L'\to&\\ &\end{aligned}$$ $$\begin{aligned}&\small\frac{\Gamma\ |\ \Gamma', A\Rightarrow B,\Delta\ |\ \Delta'\qquad \Gamma\ |\ \Gamma', A\Rightarrow \Delta\ |\ \Delta', A\qquad \Gamma\ |\ \Gamma', B\Rightarrow \Delta\ |\ \Delta', B}{\Gamma\ |\ \Gamma' \Rightarrow \Delta\ |\ \Delta', A\to B}\normalsize R'\to\end{aligned}$$

Figure $\mathbf{G3wnf}$

Notice that adding the fourth potential initial sequent,

$$\Gamma\ |\ \Gamma',P(t_1 ... t_n)\Rightarrow \Delta\ |\ \Delta',P(t_1 ... t_n)\tag{\(is_4^*\)}$$

would collapse the system into a bivalent one, since it would state that it is not the case that an atom is neither true nor false (or, if an atom is non-false then it is true on the implicational reading), effectively blocking the third value. However, a restricted version of that possibility,

$$\{{E!} t_{i}\}_{1\leq i\leq n},\Gamma\ |\ \Gamma',P(t_1 ... t_n)\Rightarrow \Delta\ |\ \Delta',P(t_1 ... t_n)\tag{\(is_4\)}$$ is derivable in the present system. The restricted version tells us that it is not the case that an atom is neither true nor false *if all the terms therein denote*. The same reasoning will likewise hold for the next system.

#### Strong Kleene base

On the other hand, $G3_{snf}$ is obtained by selecting as the propositional base strong Kleene logic K$_3$. Note that the systems presented actually differ only in two rules, with $G3_{snf}$ present one containing no three-premise rules:

**Initial sequents (is):** $$\tag{\(is_1\)} P, \Gamma\ |\ \Gamma' \Rightarrow \Delta\ |\ \Delta', P$$ $$\tag{\(is_2\)} \Gamma\ |\ \Gamma', P\Rightarrow P,\Delta\ |\ \Delta'$$ $$ \tag{\(is_3\)} P, \Gamma\ |\ \Gamma' \Rightarrow P, \Delta\ |\ \Delta'$$

**Propositional rules:**

$$\begin{aligned} \frac{\Gamma\ |\ \Gamma'\Rightarrow A,\Delta\ |\ \Delta'}{\neg A, \Gamma\ |\ \Gamma' \Rightarrow \Delta\ |\ \Delta'}L\neg && \frac{A, \Gamma\ |\ \Gamma' \Rightarrow \Delta\ |\ \Delta'}{\Gamma\ |\ \Gamma' \Rightarrow \neg A, \Delta\ |\ \Delta'}R\neg\\ &&\\ \frac{\Gamma\ |\ \Gamma' \Rightarrow \Delta\ |\ \Delta', A}{\Gamma\ |\ \Gamma', \neg A\Rightarrow \Delta\ |\ \Delta'}L'\neg && \frac{\Gamma\ |\ \Gamma', A \Rightarrow \Delta\ |\ \Delta'}{\Gamma\ |\ \Gamma' \Rightarrow \Delta\ |\ \Delta',\neg A}R'\neg \end{aligned}$$ $$\begin{aligned} \frac{\Gamma\ |\ \Gamma' \Rightarrow A, \Delta\ |\ \Delta'\qquad B, \Gamma\ |\ \Gamma' \Rightarrow \Delta\ |\ \Delta'}{A\to B, \Gamma\ |\ \Gamma' \Rightarrow \Delta\ |\ \Delta'} L\to &&\\ &&\\ \frac{A,\Gamma\ |\ \Gamma' \Rightarrow B, \Delta\ |\ \Delta'}{\Gamma\ |\ \Gamma' \Rightarrow A\to B,\Delta\ |\ \Delta'}R\to&&\\ &&\\ \frac{\Gamma\ |\ \Gamma' \Rightarrow \Delta\ |\ \Delta', A \qquad \Gamma \ |\ B, \Gamma'\Rightarrow \Delta\ |\ \Delta'}{\Gamma \ |\ A\to B, \Gamma'\Rightarrow \Delta\ |\ \Delta'}L'\to&&\\ &&\\ \frac{\Gamma\ |\ \Gamma', A\Rightarrow \Delta\ |\ \Delta', B}{\Gamma\ |\ \Gamma' \Rightarrow \Delta\ |\ \Delta', A\to B}R'\to &&\end{aligned} $$

## 4. Generic Anomalies

While problems noted above are specific to particular forms of free logic, there are anomalies that infect all, or nearly all, forms. This section considers three: (1) a cluster of problems related to the application of primitive predicates to empty terms, (2) the failure of substitutivity *salva veritate* of co-referential expressions, and (3) the inability of free logic to express sufficient conditions for existence.

### 4.1 Problems with Primitive Predicates

In classical logic and in positive free logic any substitution instance of a valid formula (or form of inference) is itself a valid formula (or form of inference). But in negative or neutral free logic this is not the case. A *substitution instance* is the result of replacing primitive non-logical symbols by possibly more complex ones of the same semantic type—$n$-place predicates with open formulas in $n$ variables, and individual constants with singular terms—each occurrence of the same primitive symbol being replaced by the same possibly complex symbol. The replacement of an occurrence of a primitive $n$-place predicate $P$ in some formula $B$ by an open formula $A$ with free variables $x_1 ,\ldots ,x_n$ is performed as follows: where $t_1 ,\ldots ,t_n$ are the individual constants or variables immediately following $P$ in that occurrence, replace P$t_1 \ldots t_n$ in $B$ by $A(t_i /x_i)$—the result of replacing $x_i$ by $t_i$ in $A$, for each $i$, $1\le i\le n$.

Let $P$, for example, be a primitive one-place predicate. Then if the semantics is negative, $Pt \rightarrow \rE!t$ is valid. But now consider the substitution instance ${\sim}Pt \rightarrow \rE!t$, in which the open formula ${\sim}Px$ is substituted for $P$. This substitution instance is false when $t$ is empty. Hence valid formulas may have invalid substitution instances. The same holds for ordinary neutral semantics that make conditionals true whenever their consequents are true.

In a negative semantics, moreover, the truth value of an empty-termed statement depends arbitrarily on our choice of primitive predicates. Consider, for example, a negative free logic interpreted over a domain of people that takes as primitive the one-place predicate ‘$A$’, meaning “is an adult,” and defines “is a minor” by this schema:

$$ Mt \eqdf {\sim}At. $$

For any non-denoting name $t, At$ is false in this theory; hence $Mt$ is true. If we take ‘is a minor’ as primitive instead, the truth-values of $At$ and $Mt$ are reversed. But why should truth-values depend on primitiveness in this way?

Positive semantics avoid these anomalies. But, if bivalent, in application they force us to assign truth values to empty-termed formulas in some other way, often without sufficient reason. Consider, for example, these three formulas, all of which contain the empty singular term ‘$1/0$’ (where ‘$/$’ is the division sign):

$$\begin{aligned} 1/0 &= 1/0 \\ 1/0 &\gt 1/0 \\ 1/0 &\le 1/0 \end{aligned}$$

Assuming a bivalent positive semantics, which ones should we make true and which false? Since the semantics is positive, ‘$1/0 = 1/0$’ is automatically true. One might argue further that since ‘$\le$’ expresses a relationship weaker than ‘=’ and since ‘$1/0 = 1/0$’ is true, ‘$1/0 \le 1/0$’ should be true as well. But that is merely to mimic with empty terms an inference pattern that holds for denoting terms. To what extent is such mimicry justified? Suppose we do decide to make ‘$1/0 \le 1/0$’ true; should we therefore make ‘$1/0 \gt 1/0$’ false? There are no non-arbitrary criteria for answering such questions. To a large extent, of course, the answers don’t matter. There are no facts here; any consistent convention will do. But that’s just the problem. Some convention is needed, and establishing one can be a lot of bother for nothing.

### 4.2 Substitutivity Failures

Classical predicate logic has the desirable feature that co-extensive open formulas may be substituted for one another in any formula *salva veritate*—i.e., without changing that formula’s truth value. (Open formulas $A$ and $B$ in $n$ free variables $x_1 ,\ldots ,x_n$ are *coextensive* if and only if $\forall x_1 \ldots \forall x_n (A \leftrightarrow B)$ is true.) But, as Lambert noted in 1974, this principle fails for nearly all free logics with identity. Consider, for example, the formula $t=t$, where $t$ is empty, which is an instance of the open formula $x=x$. Now $x=x$ is coextensive with both $(x=x \amp \rE!x)$ and $(\rE!x \rightarrow x=x)$, since all three formulas are satisfied by all members of $\bD$. Hence if co-extensive open formulas could be exchanged *salva veritate*, $(t=t \amp \rE!t)$ and $(\rE!t \rightarrow t=t)$ would have the same truth value as $t=t$. But on nearly all free logics this is not the case. Positive free logic and supervaluations make $t=t$ true and $(t=t \amp \rE!t)$ false; negative free logic makes $t=t$ false and $(\rE!t \rightarrow t=t)$ true; and any ordinary neutral free logic whose conditionals are true whenever their antecedents are false makes $t=t$ truth-valueless and $(\rE!t \rightarrow t=t)$ true. Many find this troubling because, since Frege, it has been widely held that (1) extensions of complex linguistic expressions should be functions of the extensions of their components (so that co-extensive components should be exchangeable without affecting the extension of the whole) and (2) the extension of a formula (or statement) is a truth value.

One possible response is to reject (2). Leeb (2006) develops for a version of PFL a dual-domain semantics in which the extensions of formulas are abstract states of affairs. In this semantics, co-referential open sentences are exchangeable not *salve veritate*, but (as he puts it) *salve extensione*; that is, the exchange does not alter the state of affairs designated by the statement in which it occurs. But Leeb’s state-of-affairs semantics is so complex that it may discourage application.

Those who wish to retain (2) may be consoled by the following observation: though substitutivity *salve veritate* of co-extensive open formulas fails for nearly all free logics, a related but weaker principle, the substitutivity *salve veritate* of co-*comprehensive* open formulas, is valid for positive free logics. Open formulas $A$ and $B$ in $n$ free variables $x_1 ,\ldots ,x_n$ are *co-comprehensive* if every assignment of denotations in the outer domain $\bD_o$ to $x_1 ,\ldots ,x_n$ satisfies $A$ if and only if it satisfies $B$. Among the open formulas mentioned in the previous paragraph, for example, $x=x$ and $(\rE!x \rightarrow x=x)$ are co-comprehensive in a dual-domain positive free logic, being satisfied by all members of $\bD_o$, but $(x=x \amp \rE!x)$ is not co-comprehensive with them, since it is satisfied only by the members of $\bD$. Unlike co-extensiveness, however, co-comprehensiveness is not expressible in the language of PFL. But it becomes expressible with the introduction of quantifiers over the outer domain—a strategy considered in Section 5.5.

### 4.3 Inexpressibility of Existence Conditions

‘Whatever thinks exists,’ ‘Any necessary being exists’, ‘That which is immediately known exists’: such statements of sufficient conditions for existence are prominent in metaphysical debates. But, somewhat surprisingly, they are not expressible in free logic. Their apparent form is $\forall x(A \rightarrow \rE!x)$. But because the universal quantifier ranges just over $\bD$, which is also the extension of E!, this form is valid in free logic—as it is in classical logic with $\rE!x$ expressed as $\exists y\,y=x$. No statement of this form—not even ‘all impossible things exist’—can be false. Hence on free logic all such statements are equally devoid of content. Argument evaluation suffers as a result. Consider, for example, the obviously valid inference:

|   | I think. |
| --- | --- |
|   | Whatever thinks exists. |
| $\therefore$ | I exist. |

Its natural formalization in free logic is $Ti, \forall x(Tx \rightarrow \rE!x) \vdash \rE!i$. But this form is invalid. To obtain the conclusion, we must first deduce $Ti \rightarrow \rE!i$ by specification from the second premise and then use modus ponens with the first. But since the logic is free, specification requires the question-begging premise $\rE!i$.

Unsatisfactory entailments involving “existence hedges”—predications that entail the existence of their objects—have recently come up in discussions of neutral free logic in particular. Daniel Yeakel (2016, p. 379) argues that “on any neutral free logic either some existence hedges will entail some undesired existence claims, or they will not entail some desired existence claims.” But the example of the previous paragraph works for negative and positive free logics as well. A remedy is not to be found in free logic alone, but again quantification over the outer domain of a dual-domain semantics may help (see Section 5.5).

## 5. Some Applications

This section considers applications of free logic in theories of definite descriptions, languages that allow partial or non-strict functions, logics with Kripke semantics, logics of fiction and logics that are in a certain sense “Meinongian.” Free logic has also found application elsewhere—most prominently in theories of predication, programming languages, set theory, logics of presupposition (with neutral semantics), and definedness logics. For more on these and other applications, see Lambert 1991 and 2001b; Lehman 2002, pp. 250–253; and Nolt 2006, pp. 1039–1053.

### 5.1 Definite Descriptions

One of the driving forces for the development of free logic has been the investigation of the existence assumptions of singular terms, more specifically *definite descriptions*. Theories of definite descriptions are still both a play and a proving ground within the conceptual framework of free logic. For a more philosophical approach to definite descriptions, see the entry on descriptions].

#### Russellian approach

The most influential theory of definite descriptions of the first half of the 20th century was developed by Bertrand Russell in his “On Denoting” and was later incorporated (with more technical apparatus) into the *Principia Mathematica* (Whitehead and Russell 1910)[^whitehead-1910]. Russell thought of definite descriptions as incomplete symbols having only meaning in context and none in isolation; more on this below. This also deprived the definite descriptions of the status of singular terms.

Whether or not this is the case, there are a couple of rather basic thoughts and lessons that can be borne out: a definite description is of the form: the $A$, or the $x$, such that $A[x]$; where ‘the $x$’ is the description operator, and ‘$A[x]$’ is the basis of the description. A definite description is (uniquely) satisfied just in case the basis of the description is uniquely satisfied. Such a definite description is also called *proper*. That is, the definite description ‘the current pope’ is uniquely satisfied since there is exactly one object in the domain that satisfies ‘being a pope’, i.e. the basis of the definite description. Note that the phrase ‘the base of a definite description being uniquely satisfied’ means that there is exactly one object that satisfies it, or to be even more painstakingly precise: there is at least one object that satisfies the basis of the description and there is at most one.

In order to incorporate definite descriptions into (some) formal language some used an inverted iota, or an inverted capital I, we just use $\imath$, where $\imath$ is a variable-binding term-forming operator, such that: $\imath x A$ is a singular term, if $A$ is a formula. This admittedly is not in the spirit of Russell, but very much in the spirit of free logic that has its core the scientific goal of unification. In this particular case this means that the plethora of theories on definite descriptions can conveniently be both developed and compared within the framework of free logic. However, what is in the spirit of Russell is that definite descriptions essentially occur in two contexts: (1) the $A$ exists, and (2) the $A$ is $F$. Russell’s guiding principles, or as Russell puts it, contextual definitions, are then stated as:

$$E!\imath xA[x] \leftrightarrow \exists x(A[x] \wedge \forall y(A[y] \to x = y))\tag{R1}$$

$$F(\imath xA[x]) \leftrightarrow \exists x(A[x] \wedge \forall y(A[y] \to x = y) \wedge F[x])\tag{R2}$$

In accordance with what Russell tells us about definite descriptions with a uniquely satisfied basis, the following formulas are theorems:

$$E!\imath xA[x] \to A[\imath x A[x]]\tag{T1}$$

$$E!\imath xA[x] \to \imath xA[x] = \imath xA[x]\tag{T2}$$

However, Russell’s approach becomes less elegant if it comes to the negative side, that is, if the basis of a definite description is not uniquely satisfied. We just mention two here. First, following (R2) negation of the left-hand side is ambiguous given the right-hand side of the equivalence, it can either mean:

$$\neg(\exists x(A[x] \wedge \forall y(A[y] \to x = y) \wedge F[x]))$$

or

$$\exists x(A[x] \wedge \forall y(A[y] \to x = y) \wedge \neg F[x])$$

In order to disambiguate Russell invented *scope operators* to distinguish the two different readings, in which he did not succeed consistently; more work on the formal aspects of Russell’s theory are found e.g. (Scales 1969; Czermak 1974; Donald Kalish 1992; Lambert 1997; Gratzl 2015)[^czermak-1974][^donald-1992][^lambert-1997][^scales-1969]. The second inelegance is that, given that Russell denies definite descriptions the status of singular terms, he needs a philosophical theory about the logical structure of sentences and terms, which is interesting in itself, but also cumbersome and furthermore leads to the fact that Russell’s approach is not closed under substitution, which is not advantageous given that uniformity is a goal.

#### Hilbert and Bernays Approach

Another way that would remain in classical logic but treats definite descriptions radically different is found in Hilbert & Bernays in their *Grundlagen der Mathematik*, Vol. 1, 1934. In their approach expressions of the form $\imath xA$ are accepted as singular terms just in case it is provable in the formal system, or simply logic, that the basis of $\imath xA$, i.e. $A$, is uniquely satisfied. That is, both formulas are provable:

$$\exists xA[x], \ and \ \forall x \forall y(A[x] \wedge A[y] \to x = y)$$

If these formulas are provable, then $A[\imath xA[x]]$ is among the provable statements of the formal system in question. Now, this approach has been critiqued on occasion for e.g. mingling the formation rules of formulas and terms with provability of the formal system, for not being natural — not even for mathematics for which it has been originally developed for. The former point of critique can be lifted, see e.g. (Lambert 1999)[^lambert-1999]; others were not so impressed by the syntactic quagmire left behind by Hilbert and Bernays and developed quite elaborated results, e.g. (Schütte 1971)[^schütte-1971].

On the positive side, there are two points: (1) it does not prove $(***)$ (see below) and it proves $t = \imath x(x = t)$. The last formula is also known as *Frege’s Law*, (FL), which Frege introduced in his *Grundgesetze*; that is to say, in a different context but (FL) is what we have nowadays in classical first-order logic. Clearly, classical logic or even a free logic and (FL) alone will not result in an interesting account of definite descriptions.

#### Free Description Theories

Taking stock, there are options within classical logic to develop quite divergent theories on definite descriptions, all of which have their own merits and drawbacks. The three theories outlined have background theories, or philosophical attitudes, of their own and so, as the argument goes, are not directly comparable within one common framework. Fortunately, here free logic offers a way out.

Lambert’s Law is the minimal principle (at least up to now) all description theories based on free logic seem to agree upon:

$$\forall x(x = \imath yA[y] \leftrightarrow \forall y(A[y] \leftrightarrow x = y))\tag{LL}$$

Following Lambert (1997), it is also instructive to determine which effect (LL) has if it is combined with classical logic; where it is assumed that classical logic is closed under substitution for all singular terms. From (LL) and axiom 3 (or as is also known: universal instantiation) and tautologies, it follows that (this closely follows Lambert 1997)[^lambert-1997]:

$$t = \imath xA \to A[t/x]\tag{*}$$

The following is a theorem:

$$\imath x(P(x) \wedge \neg P(x)) = \imath x(P(x) \wedge \neg P(x)\tag{**}$$

But now contradiction follows from $(*), (**)$, and modus ponens:

$$P(\imath x(P(x) \wedge \neg P(x))) \wedge \neg P(\imath x(P(x) \wedge \neg P(x)))\tag{***}$$

Now, further inductive support for the usefulness of free logic is that free logicians drew the morals of adopting a version of free logic in which contradiction can be avoided; suffice it to say that in the face of antinomy and it appropriate error analysis, typically some routes are open for investigation, one that varies universal instantiation is at least a viable and systematic option.

We already introduced Hintikka’s Law (HL), i.e.

$$E!t \leftrightarrow \exists x(x = t)\tag{HL}$$

earlier. So, adding (HL) to PFL, Russell’s (R1), (R2), (T1), and (T2) are obtainable.

However, NFL is more in tune with Russell’s account (since definite descriptions are, in fact, treated as genuine singular terms), for this end NFL is accompanied with (LL) and a version of axiom 8 of NFL including definite descriptions, i.e.:

$$\iota xA[x] = \iota xA[x] \to E!\iota xA[x]$$

NFL enjoys the theorem of *indiscernability of non-existents*, which has the following instance (given that NFL enriched with definite descriptions is closed under substitution):

$$\neg E!\imath xA \wedge \neg E!\imath xB \to (B[\imath xA] \to B[\imath xB])$$

Free description theories leaning more towards the positive side of free logic are, for instance, theories building on (LL) and

$$\forall x(A[x] \leftrightarrow B[x]) \to \imath xA[x] = \imath xB[x]\tag{Coext}$$

In (Morscher and Simons 2001b) the truth of this principle is called self-evident. The predicates ‘having kidneys’ and ‘having a heart’ are co-extensional, which is an empirical truth, and according to (Coext) then implies that the $x$ having a lung = the $x$ having a heart — a truth of the status of being obvious might be challenged. Whereas, still having positive intuitions the predicates ‘being a Labrador full up with food’ and ‘being a Martian’ are co-extensional, both being empty, the then part: the $x$ being a Labrador full up with food = the $x$ being a Martian seems to be more in line with PFL. It is noteworthy for Hilbert and Bernays (Coext) is a theorem given that the uniquenss-conditions are provable for both $A$, and $B$.

A principle related to (Coext) and still maintaining PFL is:

$$\neg E!s \wedge \neg E!t \to s = t\tag{Negexid}$$

Both (Coext) and (Negexid) are reflections of the *chosen object*-idea which assigns empty singular terms and arbitrary object. Under this assumption one is back to the classical existence assumptions, and so classical logic. The chosen-object theory is due to Frege, the formulation used is due to Carnap (Carnap 1964)[^carnap-1964]: $$\forall x(x = \imath yA[y] \leftrightarrow$$ $$(\exists z(\forall y(A[y] \leftrightarrow y = z) \wedge z = x)$$ $$\vee \neg \exists z(\forall y(A[y] \leftrightarrow y = z) \wedge z=*))\tag{Chosob}$$

Technical investigations on the chosen object theory are found in (Donald Kalish 1992)[^donald-1992] and more recently and more proof-theoretically motivated in (Indrzejczak 2019)[^indrzejczak-2019]. After a period of lull, where logical research on definite descriptions was not so pronounced, the research into definite descriptions has lately again picked up e.g. (Kürbis 2021, 2022)[^kürbis-2021].

### 5.2 Logics with Partial or Non-Strict Functions

Some logics employ primitive *n-place function symbols*—symbols that combine with $n$ singular terms to form a complex singular term. Thus, for example, the plus sign ‘+’ is a two-place function symbol that, when placed between, say, ‘2’ and ‘3’, forms a complex singular term, ‘$2 + 3$’ that denotes the number five. Similarly, ‘$^2$’ is a one-place function symbol that, when placed after a term denoting a number, forms a complex singular term that denotes that number’s square. Semantically, the extension of a function symbol is a function whose arguments are members of the quantificational domain $\bD$, and the resulting complex term denotes the result of applying that function to the referents of the $n$ component singular terms, taken in the order listed. Since classical logic requires every singular term (including those formed by function symbols) to refer to an object in $\bD$, for each such function symbol $f$, it requires that:

$$ \forall x_1 \ldots \forall x_n\exists y(y = f(x_1, \ldots, x_n)). $$

Hence classical logic prohibits primitive function symbols whose extensions are partial functions—functions whose value is for some arguments undefined. Such, for example, is the binary division sign ‘/’, since when placed between two numerals the second of which is ‘0’, it forms an empty singular term. Similarly, the limit function symbol ‘lim’ yields an empty singular term when applied to the name of a non-coverging sequence. Classical logic can accommodate function symbols for partial functions via elaborate contextual definitions. But then (as with Russellian definite descriptions) the form in which these function symbols are usually written is not their logical form. Free logic provides a more elegant solution. Because it allows empty singular terms, symbols for partial functions may simply be taken as primitive.

In applications of free logic involving partial functions, the existence predicate ‘$\rE!$’ is often replaced by the postfix definedness predicate ‘$\downarrow$’. For any singular term $t, t\downarrow$ is true if and only if $t$ has some definite value in $\bD$. Thus, for example, the formula ‘$(1/0)\downarrow$’ is false. While some writers (e.g., Feferman (1995)) distinguish ‘$\downarrow$’ from ‘$\rE!$’, the literature as a whole does not, and ‘$\downarrow$’ is often merely a syntactic variant of ‘$\rE!$’.

In addition to partial functions, *positive* free logics can also readily handle *non-strict* functions. A non-strict function is a function that may yield a value even if not all of its arguments are defined. The binary function $f$ such that $f(x,y) = x$, for instance, can yield a value even if the $y$-term is empty. So, for example, the formula $f(1, 1/0) = 1$ can be regarded as true. Logics for non-strict functions must be positive because in a negative or neutral logic empty-termed atomic formulas, such as $f(1, 1/0) = 1$, cannot be true. Free logics involving non-strict functions find application in some programming languages (Gumb 2001, Gumb and Lambert 1991)[^gumb-2001][^gumb-1991][^lambert-1991]. Such logics may employ a dual-domain semantics in which the referents of empty functional expressions such as ‘1/0’ are regarded as *error objects*—objects that correspond in the running of a program to error messages. Thus, for example, an instruction to calculate $f(1, 1/0)$ might return the value 1, but an instruction to calculate $f(1/0, 1)$ would return an error message.

### 5.3 Logics with Kripke Semantics

Kripke semantics for quantified modal logics, tense logics, deontic logics, intuitionistic logics, and so on, are often free. This is because they index truth to certain objects that we shall call “worlds,” and usually some things that we have names for do not exist in some of these worlds. Worlds may be conceived in various ways: they may, for example, be understood as possible universes in alethic modal logic, times or moments in tense logic, permissible conditions in deontic logic, or epistemically possible states of knowledge in intuitionistic logic. Associated with each world $w$ is a domain $\bD_w$, of objects (intuitively, the set of objects that exist at $w)$. An object may exist in (or “at”) more than one world but need not exist in all. Thus, for example, Kripke semantics for tense logic represents the fact that Bertrand Russell existed at one time but exists no longer by Russell’s being a member of the domains of certain “worlds”—that is, times (specifically, portions of the last two centuries)—but not others (the present, for example, or all future times). Two natural assumptions are made here: that the same object may exist in more than one world (this is the assumption of *transworld identity*), and that some singular terms—proper names, in particular—refer not only to an object at a given world, but to that same object at every world. Such terms are called *rigid* *designators*. Any logic that combines rigid designators with quantifiers over the domains of worlds in which their referents do not exist must be free.

Kripke semantics gives predicates different extensions in different worlds. Thus, for example, the extension of the predicate ‘is a philosopher’ was empty in all worlds (times) before the dawn of civilization and more recently has varied. For rigidly designating terms, this raises the question of how to evaluate atomic formulas at worlds in which their referents do not exist. Is the predicate ‘is a philosopher’ satisfied, for example, by Russell in worlds (times) in which he does not exist—times such as the present? The general answers given to such questions determine whether a Kripke semantics is positive, negative or neutral.

For negative or neutral semantics, the extension at $w$ of an $n$-place predicate $P$ is a subset of $\bD_w^n$. An atomic formula can be true at $w$ only if all its singular terms have referents in $\bD_w$; if not, it is false (in negative semantics) or truth-valueless (in neutral semantics). In a positive semantics, atomic formulas that are empty-termed at $w$ may nevertheless be true at $w$. Predicates are usually interpreted over the union $\bU$ of domains of all the worlds, which functions as a kind of outer domain for each world, so that the extension of an $n$-place predicate $P$ at a world $w$ is a subset of $\bU^n$. Some applications, however, require predicates to be true of—and singular terms to be capable of denoting—objects that exist in no world. If so, we may collect these objects into an outer domain that is a superset of $\bU$. (They might be fictional objects, timeless Platonic objects, impossible objects, or the like.)

Quantified formulas, like all formulas, are true or false only relative to a world. Thus $\exists xA$, for example, is true at a world $w$ if and only if some object in $\bD_w$ satisfies $A$. Except in intuitionistic logic, where it has a specialized interpretation, the universal quantifier is interpreted similarly: $\forall xA$ is true at $w$ if and only if all objects in $\bD_w$ satisfy $A$. Kripke semantics often specify that for each $w, \bD_w$ is nonempty, so that the resulting free logic is non-inclusive—but we shall not do so.

Any of various free modal or tense logics can be formalized by adding to a language $\bL$ of the sort defined in Section 1.3 the sentential operator ‘$\Box$’. If $A$ is a formula, so is $\Box A$. In alethic modal logic, this operator is read “it is necessarily the case that.” More generally, it means “it is true in all accessible worlds that,” where accessibility from a given world is a different relation for different modalities: possibility for alethic logics, permissibility for deontic logics, various temporal relations for tense logics, and so on. A typical bivalent Kripke model $\bM$ for such a language consists of a set of worlds, a binary accessibility relation $\bR$ defined on that set; an assignment to each world $w$ of a domain $\bD_w$; an “outer” domain $\bD_o$ of objects (which typically is either $\bU$ or a superset thereof); and a two-place interpretation function $\bI$ that assigns denotations at worlds to individual constants and extensions at worlds to predicates. For each individual constant $t$ and world $w, \bI(t,w)\in \bD_o$. In such a model, a singular term is a rigid designator if and only if for all worlds $w_1$ and $w_2$, $\bI(t,w_1) = \bI(t,w_2)$. For every $n$-place predicate $P, \bI(P,w) \subseteq \bD_w^n$ if the semantics is negative or neutral; if it is positive, $\bI(P,w) \subseteq \bD_o^n$. Truth values at the worlds of a model $\bM$ are assigned by a two-place valuation function $\bV$ (where $\bV(A,w)$ is read “the truth value $\bV$ assigns to formula $A$ at world $w$”) as follows:

$$\begin{aligned} \bV(Pt_1 \ldots t_n,w) &= \left\{\begin{array}{l} \top, \text{ iff } \langle\bI(t_1,w),\ldots,\bI(t_n,w)\rangle \in \bI(P,w); \\ \bot, \text{ otherwise.} \end{array}\right. \\ \bV(s=t,w) &= \left\{\begin{array}{l} \top, \text{ iff } \bI(s,w)=\bI(t,w); \\ \bot, \text{ otherwise.} \end{array}\right. \\ \bV(\rE!t,w) &= \left\{\begin{array}{l} \top, \text{ iff } \bI(t,w) \in \bD_w; \\ \bot \text{ otherwise.} \end{array}\right. \\ \bV({\sim}A,w) &= \left\{\begin{array}{l} \top, \text{ iff } \bV(A,w) = \bot\\ \bot, \text{ otherwise.} \end{array}\right. \\ \bV(A\rightarrow B,w) &= \left\{\begin{array}{l} \top, \text{ iff } \bV(A,w) = \bot \text{ or } \bV(B,w) = \top; \\ \bot, \text{ otherwise.} \end{array}\right. \\ \bV(\Box A,w) &= \left\{\begin{array}{l} \top, \text{ iff for all } u \text{ such that } w\bR u, \bV(A,u) = \top\\ \bot, \text{ otherwise.} \end{array}\right. \\ \bV(\forall xA,w) &= \left\{\begin{array}{l} \top \text{ iff for all } d\in \bD_w, \bV_{(t,d)}(A(t/x),w) = \bot \\ \quad(\text{where } t \text{ is not in } A \text{ and } \bV_{(t,d)} \text{ is the}\\ \quad\text{valuation function on the model just like } \bM \\ \quad\text{except that its interpretation function } \bI^* \text{ is} \\ \quad\text{such that for each world } w, \bI^*(t,w)= d); \\ \bot, \text{ otherwise.} \end{array}\right. \end{aligned}$$

Under the stipulations that admissible models make all individual constants rigid designators and that $\bI(P,w) \subseteq \bD_o^n$, the standard free logic PFL, together with the modal axioms and rules appropriate to whatever structure we assign to $\bR$, is sound and complete on this semantics.

Modal semantics thus defined call for free logic whenever worlds are allowed to have differing domains—that is whenever we may have worlds $u$ and $w$ such that $\bD_u \ne \bD_w$. For in that case there must be an object $d$ that exists in one of these domains (let it be $\bD_w)$, but not the other, so that any singular term $t$ that rigidly designates $d$ must be empty at world $u$. Hence ${\sim}\exists x(x=t)$ (which is self-contradictory in classical logic) must be true at world $u$. Such a semantics also requires free logic when $\bD_o$ contains objects not in $\bU$, for in that case rigid designators of these objects are empty in all worlds. Finally, this semantics calls for *inclusive* logic if any world has an empty domain. Thus, given this semantics, the only way to make the resulting logic unfree is to require that domains be *fixed*—i.e., that all worlds have the same domain $\bD$, that $\bD$ be non-empty, and that $\bD_o = \bD$.

Just this trio of requirements was in effect proposed by Saul Kripke in his ground-breaking (1963) paper on modal logic as one of two strategies for retaining classical quantification. (The other, more draconian, strategy was to allow differing domains but ban individual constants and treat open formulas as if they were universally quantified.) But such fixed-domain semantics validate the implausible formula:

$$ \forall x\Box \exists y(y = x), $$

which asserts that everything exists necessarily and the equally implausible Barcan formula:

$$ \forall x\Box A \rightarrow \Box \forall xA $$

(named for Ruth Barcan, later Ruth Barcan Marcus, who discussed it as early as the late 1940s). To see its implausibility, consider this instance: ‘If everything is necessarily a product of the big bang, then necessarily everything is a product of the big bang’. It may well be true that everything (in the actual world) is necessarily a product of the big bang—i.e., that nothing in this world would have existed without it. But it does not seem necessary that everything is a product of the big bang, for other universes are possible in which things that do not exist in the actual world have other ultimate origins. Because of the restrictiveness and implausibility of fixed-domain semantics, many modal logicians loosen Kripke’s strictures and adopt free logics.

We may also drop the assumption that singular terms are rigid designators and thus allow *nonrigid designators*. On the semantics considered here, these are singular terms $t$ such that for some worlds $w_1$ and $w_2, \bI(t,w_1) \ne \bI(t,w_2)$. Definite descriptions, understood attributively, are the best examples. Thus the description “the oldest person” designates different people at different times (worlds)—and no one at times before people existed (“worlds” $w$ at which $\bI(t,w)$ is undefined).

Nonrigid designators, if empty at some worlds, require free logics even with fixed domains. (Thus classical logic with nonrigid designators is possible only if we require for each singular term $t$ that at each world $w$, $t$ denotes some object in $\bD_w$.) On some semantics for nonrigid designators, the quantifier rule must differ from that given above, and other adjustments must be made. For details, see Garson 1991, Cocchiarella 1991, Schweitzer 2001 and Simons 2001.

Intuitionistic logic, too, has a Kripke semantics, though special valuation clauses are needed for ‘${\sim}$’, ‘$\rightarrow$’ and ‘$\forall$’ in order to accommodate the special meanings these operators have for intuitionists, and ‘$\Box$’ is generally not used. The usual first-order intuitionistic logic, the Heyting predicate calculus (HPC)—also called the intuitionistic predicate calculus—has the theorem $\exists x(x=t)$ and hence is not free. But intuitionists admit the existence only of objects that can in some sense be constructed, while classical mathematicians posit a wider range of objects. Therefore users of HPC cannot legitimately name all the objects that classical mathematicians can. Worse, they cannot legitimately name objects whose constructibility has yet to be determined. Yet some Kripke-style semantics for HPC do allow use of names for such objects (semantically, names of objects that “exist” at worlds accessible from the actual world but not at the actual world itself). Some such semantics, though intended for HPC, have turned out, unexpectedly, not to be adequate for HPC. An obvious fix, advocated by Posy (1982), is to adopt a free intuitionistic logic. For more on this issue, see Nolt 2007.

### 5.4 Logics of Fiction

Because fictions use names that do not refer to literally existing things, free logic has sometimes been employed in their analysis. So long as we engage in the pretense of a story, however, there is no special need for it. It is true, for example, in Tolkien’s *The Lord of the Rings* that Gollum hates the sun, from which we can legitimately infer that *in the story* there exists something that hates the sun. Thus quantifiers may behave classically so long as we consider only what occurs and what exists “in the story.” (The general logic of fiction, however, is often regarded as *non*classical, for two reasons: (1) a story may be inconsistent and hence require a paraconsistent logic, and (2) the objects a story describes are typically (maybe always) incomplete; that is, the story does not determine for each such object $o$ and every property $P$ whether or not $o$ has $P$.)

The picture changes, however, when we distinguish what is true in the story from what is literally true. For this purpose logics of fiction often deploy a sentence operator that may be read “in the story.” Here we shall use ‘$\mathbf{S}_x$’ to mean “in the story $x$,” where ‘$x$’ is to be replaced by the name of a specific story. Anything within the scope of this operator is asserted to be true in the named story; what is outside its scope is to be understood literally. (For a summary of theories of what it means to be true in a story, see Woods 2006.)[^woods-2006]

With this operator the statement ‘In the story, *The Lord of the Rings*, Gollum hates the sun’ may be formalized as follows:

$$\tag{GHS} \mathbf{S}_{The\: Lord\: of\: the\: Rings}(\text{Gollum hates the sun}). $$

The statement that in *The Lord of the Rings* something hates the sun is:

$$ \mathbf{S}_{The\: Lord\: of\: the\: Rings}\exists x(x \text{ hates the sun}). $$

This second statement follows from the first, even though Gollum does not literally exist. But it does not follow that there exists something such that it, in *The Lord of the Rings*, hates the sun:

$$ \exists x \mathbf{S}_{The\: Lord\: of\: the\: Rings}(x \text{ hates the sun}). $$

and indeed that statement is not true, for, literally, Gollum does not exist. Since the sun, however, exists both literally and in the story, the statement:

$$ \exists x\mathbf{S}_{The\: Lord\: of\: the\: Rings}(\text{Gollum hates } x) $$

is true and follows by free existential generalization from (GHS) together with the true premise ‘$\rE!(\text{the sun})$’. Thus free logic may play a role in reasoning that mixes fictional and literal discourse.

Terms for fictional entities also occur in statements that are entirely literal, making no mention of what is true “in the story.” Consider, for example, the statement:

$$\tag{G} \text{Gollum is more famous than Gödel.} $$

Mark Sainsbury (2005, ch. 6) holds that reference failure invariably makes such statements false and hence that they are best represented in a negative free logic. Others, however—including Orlando 2008 and Dumitru and Kroon 2008—question Sainsbury’s treatment, maintaining that statements like (G) are both atomic and true. If so, they require a positive free logic. The logic must be free because it deals with an empty singular term, and it must be positive, because only on a positive semantics can empty-termed atomic statements be true. One must still decide, however, whether the name ‘Gollum’ is to be understood as having no referent or as having a referent that does not exist.

If ‘Gollum’ has no referent, then (G) might be handled by a *single-domain* positive semantics. But that semantics would have to treat atomic formulas non-standardly; it could not, as usual, stipulate that (G) is true just in case the pair $\langle$Gollum, Gödel$\rangle$ is a member of the extension of the predicate ‘is more famous than’; for if there is no Gollum, there is no such pair. On such a semantics ‘Gollum is more famous than Gödel’ would not imply that something is more famous than Gödel.

If, on the other hand, terms such as ‘Gollum’ refer to non-existent objects, then those objects could inhabit the outer domain of a dual-domain positive free logic. Dumitru (2015), for example, lays out such a dual-domain semantics for fictional discourse using free descriptions and compares it with a supervaluational approach that also uses free descriptions. In a such a dual-domain semantics, atomic formulas have their standard truth conditions: (G) is true just in case $\langle$Gollum, Gödel$\rangle$ is a member of the extension of ‘is more famous than’. Moreover, if we allow quantifiers over that outer domain, then ‘Something is more famous than Gödel’ (where the quantifier ranges over the outer domain) does follow from ‘Gollum is more famous than Gödel’, though ‘There *literally exists* something more famous than Gödel’ (where the quantifier ranges over the inner domain) does not. Meinongian logics of fiction employ this strategy.

### 5.5 Meinongian Logics

Alexius Meinong is best known for his view that some objects that do not exist nevertheless have being. His name has been associated with various developments in logic. Some free logicians use it to describe any dual-domain semantics. For others, Meinongian logic is something much more elaborate: a rich theory of all the sorts of objects we can think about—possible or impossible, abstract or concrete, literal or fictional, complete or incomplete. In this section the term is used to describe logics stronger than the first type but possibly weaker than the second: positive free logics with an extra set of quantifiers that range over the outer domain of a dual-domain semantics.

Whether such logics can legitimately be considered free is controversial. On older conceptions, free logic forbids any quantification over non-existing things (see Paśniczek 2001 and Lambert’s reply in Morscher and Hieke 2001, pp. 246–8)[^morscher-2001][^morscher-2001-2][^paśniczek-2001]. But by anybody’s definition, Meinongian logics in the sense intended here at least *contain* free logics when the inner domain is interpreted as the set of existing things. Moreover, on the strictly semantic definition, which is also that of Lehman 2002, whether the members of $\bD$ exist is irrelevant to the question of whether a logic is free. For a defense of this definition, see Nolt 2006, pp. 1054–1057.

Historically, quantification over domains containing objects that do not exist has been widely dismissed as ontologically irresponsible. Quine (1948) famously maintained that existence is just what an existential quantifier expresses. Yet nothing forces us to interpret “existential” quantification over every domain as expressing existence—or being of any sort. Semantically, an existential quantifier on a variable $x$ is just a logical operator that takes open formulas on $x$ into truth values; the value is T if and only if the open formula is satisfied by at least one object in the quantifier’s domain. That the objects in the domain have or lack any particular ontological status is a philosophical interpretation of the formal semantics. Alex Orenstein (1990) argues that “existential” is a misnomer and that we should in general call such quantifiers “particular.” That suggestion is followed in the remainder of this section.

Quantifiers ranging over the outer domain of a dual-domain semantics are called *outer quantifiers*, and those ranging over the inner domain *inner quantifiers*. If the inner particular quantifier is interpreted to mean “there exists” and the members of the outer domain are possibilia, then the outer particular quantifier may mean something like “there is possible a thing such that” or “for at least one possible thing.” We shall use the generalized product symbol ‘$\Pi$’ for the outer universal quantifier and the generalized sum symbol ‘$\Sigma$’ for its particular dual. This notation enables us to formalize, for example, the notoriously puzzling but obviously true statement ‘Some things don’t exist’ (Routley 1966)[^routley-1966] as:

$$ \Sigma x{\sim}\rE!x. $$

Since in a dual-domain semantics all singular terms denote members of the outer domain, the logic of outer quantifiers is not free but classical. With ‘E!’ as primitive, the free inner quantifiers can be defined in terms of the classical outer ones as follows:

$$\begin{aligned} \forall xA &\eqdf \Pi x(\rE!x \rightarrow A) \\ \exists xA &\eqdf \Sigma x(\rE!x \amp A). \end{aligned}$$

The outer quantifiers, however, cannot be defined in terms of the inner.

Logics with both inner and outer quantifiers have various applications. They enable us, for example, to formalize substantive sufficient conditions for existence and hence adequately express the argument of Section 4.3, as follows:

$$ Ti, \Pi x(Tx \rightarrow \rE!x) \vdash \rE!i. $$

This form is valid. The co-comprehensiveness of open formulas $A$ and $B$ in $n$ free variables $x_1 ,\ldots ,x_n$ (see Section 4.2), can likewise be formalized as:

$$ \Pi x_1 \ldots \Pi x_n (A \leftrightarrow B). $$

Richard Grandy’s (1972) theory of definite descriptions holds that $\iota xA=\iota xB$ is true if and only if $A$ and $B$ are co-comprehensive and thus is readily expressible in a Meinongian logic. Free logics with outer quantifiers have also been employed in logics that are Meinongian in the richer sense of providing a theory of objects (including, in some cases, fictional objects) that is inspired by Meinong’s work (Routley 1966 and 1980, Parsons 1980, Jacquette 1996, Paśniczek 2001, Priest 2005 and 2008, pp. 295–7)[^jacquette-1996][^paśniczek-2001][^priest-2005][^priest-2008][^routley-1966][^routley-1980].

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=logic-free). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/logic-free/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=logic-free&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/logic-free/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

[Please contact the authors with suggestions.]

## Related Entries

descriptions | fiction: fictional entities | logic: classical | logic: intuitionistic | logic: modal | logic: temporal | nonexistent objects | possible objects | proof theory | proof theory: development of

### Acknowledgments

Beginning with the 2025 update, Norbert Gratzl and Edi Pavlović have taken responsibility for updating and maintaining this entry.

[^antonelli-2000]: Antonelli, Gian Aldo, 2000, “Proto-Semantics for Positive Free Logic,” *Journal of Philosophical Logic*, 29 (3): 277–294.

[^antonelli-2007]: –––, 2007, “Free Quantification and Logical Invariance,” *Rivista de Estetica* (New Series), 33 (1): 61–73.

[^baaz-2006]: Baaz, Matthias, and Rosalie Iemhoff, 2006, “Gentzen Calculi for the Existence Predicate.” *Studia Logica* 82: 7–23.

[^bacon-2016]: Bacon, Andrew, Hawthorne, John, and Uzquiano, Gabriel, 2016, “Higher-order free logic and the Prior-Kaplan paradox,” *Canadian Journal of Philosophy* 46(4–5): 493–541.

[^barnes-1984]: Barnes, J., ed. *The Complete Works of Aristotle*, Volumes I and II, Princeton: Princeton University Press, 1984.

[^bencivenga-1981]: Bencivenga, Ermanno, 1981, “Free Semantics” in *Boston Studies in the Philosophy of Science*, 47: 38–41; revised version reprinted in Lambert 1991, pp. 98–110.

[^bencivenga-1986]: –––, 1986, “Free Logics,” in D. Gabbay and F. Guenthner (eds.), *Handbook of Philosophical Logic*, vol. III: *Alternatives to Classical Logic*, Dordrecht: D. Reidel, pp. 373–426

[^bencivenga-2002]: –––, 2002, “Free Logics,” in D. Gabbay and F. Guenthner (eds.), *Handbook of Philosophical Logic*, 2ⁿᵈ edition, vol. 5, Dordrecht: Kluwer, pp. 147–196. (This is a republication of Bencivenga 1986.)

[^bencivenga-2014]: –––, 2014, “Jaśkowski’s Universally Free Logic,” *Studia Logica* 102: 1095–1102.

[^besson-2009]: Besson, Corine, 2009, “Externalism, Internalism, and Logical Truth,” *Review of Symbolic Logic*, 2 (1): 1–29.

[^bochman-1998]: Bochman, Alexander, 1998, “Biconsequence Relations: A Four-Valued Formalism of Reasoning with Inconsistency and Incompleteness,”*Notre Dame Journal of Formal Logic* 39 (1): 47–73.

[^bochvar-1981]: Bochvar, Dmitri, and Merrie Bergmann, 1981, “On a Three-Valued Logical Calculus and Its Application to the Analysis of the Paradoxes of the Classical Extended Functional Calculus.” *History and Philosophy of Logic* 2 (1–2): 87–112.

[^burge-1974]: Burge, Tyler, 1974, “Truth and Singular Terms,” *Noûs*, 8: 309–25; reprinted in Lambert 1991, pp. 189–204.

[^carnap-1964]: Carnap, Rudolf, 1964, *Meaning and Necessity: A Study in Semantics and Modal Logic*. University of Chicago Press.

[^church-1965]: Church, Alonzo, 1965, review of Lambert 1963 in *Journal of Symbolic Logic*, 30: 103–104.

[^cobreros-2012]: Cobreros, Pablo, Paul Egré, David Ripley, and Robert Van Rooij, 2012, “Tolerant, Classical, Strict.” Journal of Philosophical Logic 41: 347–85.

[^cocchiarella-1966]: Cocchiarella, Nino B., 1966, “A Logic of Actual and Possible Objects” (abstract), *Journal of Symbolic Logic*, 31: 688–689.

[^cocchiarella-1986]: –––, 1986, *Logical Investigations of Predication Theory and the Problem of Universals*, Napoli, Italy: Bibliopolis.

[^cocchiarella-1991]: –––, 1991, “Quantification, Time and Necessity,” in Lambert 1991, pp. 242–256.

[^czermak-1974]: Czermak, Johannes, 1974, “A Logical Calculus with Descriptions.” *Journal of Philosophical Logic*, 211–28.

[^degauquier-2016]: Degauquier, Vincent, 2016, “Partial and Paraconsistent Three-Valued Logics.” *Logic and Logical Philosophy* 25 (2): 143–71.

[^donald-1992]: Donald Kalish, Gary Mar, Richard Montague, 1992, *Logic: Techniques of Formal Reasoning*. Oxford University Press.

[^dumitru-2015]: Dumitru, Mircea, 2015, “A Free Logic for Fictionalism” in Iulian D. Toader, Gabriel Sandu & Ilie Pȃrvu, eds., *Romanian Studies in Philosophy of Science*, Springer Verlag, pp. 149–163.

[^dumitru-2008]: Dumitru, Mircea and Frederick Kroon, 2008, “What to Say When There Is Nothing to Talk about (Qué decir cuando no hay nada de quehablar),” *Crítica: Revista Hispanoamericana de Filosofía*, 40 (120): 97–109.

[^feferman-1995]: Feferman, Solomon, 1995, “Definedness,” *Erkenntnis*, 43 (3): 295–320.

[^fine-1983]: Fine, Kit, 1983, “The Permutation Principle in Quantificational Logic,” *Journal of Philosophical Logic*, 12: 33–7.

[^fjellstad-2020]: Fjellstad, Andreas, 2020, “Structural Proof Theory for First-Order Weak Kleene Logics.” *Journal of Applied Non-Classical Logics* 30 (3): 272–89.

[^fodor-1996]: Fodor, Jerry A., and Ernest Lepore, 1996, “What Cannot be Evaluated Cannot be Evaluated and it Cannot be Supervalued Either,” *Journal of Philosophy*, 93 (10): 516–535.

[^garson-1991]: Garson, James W., 1991, “Applications of Free Logic to Quantified Intensional Logic,” in Lambert 1991, pp. 111–142.

[^grandy-1972]: Grandy, Richard E., 1972, “A Definition of Truth for Theories with Intensional Definite Description Operators,” *Journal of Philosophical Logic*, 1: 137–55; reprinted in Lambert 1991, pp. 171–188.

[^gratzl-2010]: Gratzl, Norbert, 2010, “A Sequent Calculus for a Negative Free Logic.” *Studia Logica* 96 (3): 331–48. ———, 2015, “Incomplete Symbols—Definite Descriptions Revisited.” *Journal of Philosophical Logic* 44 (5): 489–506.

[^gumb-2001]: Gumb, Raymond D., 2001, “Free Logic in Program Specification and Verification,” in Morscher and Hieke 2001, pp. 157–93.

[^gumb-1991]: Gumb, Raymond D., and Karel Lambert, 1991, “Definitions in Nonstrict Positive Free Logic,” *Modern Logic*, 7: 25–55 and 435–440 (errata).

[^hailperin-1953]: Hailperin, Theodore, 1953, “Quantification Theory and Empty Individual Domains,” *Journal of Symbolic Logic*, 18: 197–200.

[^hintikka-1959]: Hintikka, Jaakko, 1959, “Towards a Theory of Definite Descriptions,” *Analysis*, 19: 79–85.

[^indrzejczak-2019]: Indrzejczak, Andrzej, 2019, “Fregean Description Theory in Proof-Theoretical Setting.” *Logic and Logical Philosophy* 28 (1): 137–55. ———, 2021a, “Free Logics Are Cut-Free.” *Studia Logica* 109 (4): 859–86. ———, 2021b, *Sequents and Trees*. Springer.

[^jacquette-1996]: Jacquette, Dale, 1996, *Meinongian Logic: The Semantics of Existence and Nonexistence*, Berlin: Walter de Gruyter.

[^jacquette-2006]: –––, (ed.), 2006, *Philosophy of Logic* (Series: Volume 5 of the *Handbook of the Philosophy of Science*), Amsterdam: Elsevier.

[^jaśkowski-1934]: Jaśkowski, Stanisław, 1934, “On the Rules of Supposition in Formal Logic,” *Studia Logica* 1: 5–32. Reprinted in *Polish Logic 1920–1939*, Storrs McCall (ed.), Oxford, Clarendon Press, 1967, pp. 232–258.

[^jeffrey-1991]: Jeffrey, Richard, 1991, *Formal Logic: Its Scope and Limits*, 3ʳᵈ edition, New York: McGraw-Hill.

[^kleene-1938]: Kleene, Stephen C., 1938, “On Notation for Ordinal Numbers.” *The Journal of Symbolic Logic* 3 (4): 150–55.

[^kripke-1963]: Kripke, Saul 1963, “Semantical Considerations on Modal Logic,” *Acta Philosophical Fennica*, 16: 83–94.

[^kürbis-2021]: Kürbis, Nils, 2021, “Definite Descriptions in Intuitionist Positive Free Logic.” *Logic and Logical Philosophy* 30: 327–58. ———, 2022, “A Binary Quantifier for Definite Descriptions for Cut Free Free Logics.” *Studia Logica* 110: 219–39.

[^lambert-1958]: Lambert, Karel, 1958, “Notes on E!,” *Philosophical Studies*, 9: 60–63.

[^lambert-1960]: –––, 1960, “The Definition of E! in Free Logic,” in *Abstracts: The International Congress for Logic, Methodology and Philosophy of Science*, Stanford: Stanford University Press.

[^lambert-1962]: –––, 1962, “Notes on E! III: A Theory of Descriptions,” *Philosophical Studies*, 13(4): 51–59.

[^lambert-1963]: –––, 1963, “Existential Import Revisited,” *Notre Dame Journal of Formal Logic*, 4: 288–292.

[^lambert-1967]: –––, 1967, “Free Logic and the Concept of Existence.” *Notre Dame Journal of Formal Logic* 8 (1–2): 133–44.

[^lambert-1974]: –––, 1974, “Predication and Extensionality,” *Journal of Philosophical Logic*, 3: 255–264.

[^lambert-1991]: –––, (ed.), 1991, *Philosophical Applications of Free Logic*, New York: Oxford University Press.

[^lambert-1997]: –––, 1997, *Free Logics: Their Foundations, Character, and Some Applications Thereof*. Sankt Augustin: Academia Verlag.

[^lambert-1999]: –––, 1999, “Logically Proper Definite Descriptions* an Essay in Honor of Ruth Marcus.” *Dialectica* 53 (3–4): 271–82.

[^lambert-2001a]: –––, 2001a, “Free Logic and Definite Descriptions,” in Morscher and Hieke 2001, pp. 37–47.

[^lambert-2001b]: –––, 2001b, “Free Logics,” in Lou Goble (ed.), *The Blackwell Guide to Philosophical Logic*, Oxford: Blackwell Publishing, pp. 258–279.

[^lambert-2003a]: –––, 2003a, *Free Logic: Selected Essays*, Cambridge: Cambridge University Press.

[^lambert-2003b]: –––, 2003b, “Existential Import, E! and ‘The’” in Lambert 2003a, pp. 16–32.

[^lambert-2003c]: –––, 2003c, “Foundations of the Hierarchy of Positive Free Definite Description Theories” in Lambert 2003a, pp. 69–91.

[^lambert-2003d]: –––, 2003d, “The Hilbert-Bernays Theory of Definite Descriptions” in Lambert 2003a, pp. 44–68.

[^lambert-2003e]: –––, 2003e, “Nonextensionality” in Lambert 2003a, pp. 107–121.

[^lambert-2003a-2]: –––, 2003f, “The Philosophical Foundations of Free Logic” in Lambert 2003a, pp. 122–175.

[^lambert-2003a-3]: –––, 2003g, “Predication and Extensionality” in Lambert 2003a, pp. 92–106.

[^lambert-2003a-4]: –––, 2003h, “Russell’s Version of the Theory of Definite Descriptions” in Lambert 2003a, pp. 1–15.

[^leblanc-1971]: Leblanc, Hughes, 1971, “Truth Value Semantics for a Logic of Existence,” *Notre Dame Journal of Formal Logic*, 12: 153–68.

[^leblanc-1968]: Leblanc, Hughes and Richmond H. Thomason, 1968, “Completeness Theorems for Some Presupposition-Free Logics,” *Fundamenta Mathematicae*, 62: 125–64; reprinted in Leblanc’s *Existence, Truth and Provability*, Albany: State University of New York Press, 1982, pp. 22–57.

[^leeb-2006]: Leeb, Hans-Peter, 2006, “State-of-Affairs Semantics for Positive Free Logic,” *Journal of Philosophical Logic*, 35 (2): 183–208.

[^lehmann-1980]: Lehmann, Scott, 1980, “Slightly Non-Standard Logic.” *Logique Et Analyse* 23 (92): 379–92.

[^lehmann-1994]: –––, 1994, “Strict Fregean Free Logic,” *Journal of Philosophical Logic*, 23 (3): 307–336.

[^lehmann-2001]: –––, 2001, “No Input, No Output Logic,” in Morscher and Hieke 2001, pp. 147–54.

[^lehmann-2002]: –––, 2002, “More Free Logic,” in D. Gabbay and F. Guenthner (eds.), *Handbook of Philosophical Logic*, 2ⁿᵈ edition, vol. 5, Dordrecht: Kluwer, pp. 197–259.

[^lejewski-1954]: Lejewski, Czeslaw, 1954, “Logic and Existence,” *British Journal for the Philosophy of Science*, 5 (18): 104–19; reprinted in Dale Jacquette (ed.), *Philosophy of Logic: An Anthology*, Oxford: Blackwell, 2002, pp. 147–55.

[^leonard-1956]: Leonard, Henry S., 1956, “The Logic of Existence,” *Philosophical Studies*, 7: 49–64.

[^maffezioli-2019]: Maffezioli, Paolo, and Eugenio Orlandelli, 2019, “Full Cut Elimination and Interpolation for Intuitionistic Logic with Existence Predicate.” *Bulletin of the Section of Logic* 48 (2): 137–58.

[^mehlberg-1958]: Mehlberg, Henryk, 1958, *The Reach of Science*, Toronto: University of Toronto Press.

[^meyer-1982]: Meyer, Robert K., Ermanno Bencivenga and Karel Lambert, 1982, “The Ineliminability of E! in Free Quantification Theory without Identity,” *Journal of Philosophical Logic*, 11: 229–231.

[^meyer-1968]: Meyer, Robert K. and Karel Lambert, 1968, “Universally Free Logic and Standard Quantification Theory,” *Journal of Symbolic Logic*, 33: 8–26.

[^morscher-2001]: Morscher, Edgar and Alexander Hieke (eds.), 2001, *New Essays in Free Logic: In Honour of Karel Lambert* (Applied Logic Series, vol., 23), Dordrecht: Kluwer.

[^morscher-2001-2]: Morscher, Edgar and Peter Simons, 2001, “Free Logic: A Fifty-Year Past and an Open Future,” in Morscher and Hieke 2001, pp. 1–34.

[^mostowski-1951]: Mostowski, Andrezej, 1951, “On the Rules of Proof in the Pure Functional Calculus of the First Order,” *Journal of Symbolic Logic*, 16: 107–111.

[^nolt-2006]: Nolt, John, 2006, “Free Logics,” in Jacquette 2006, pp. 1023–1060.

[^nolt-2007]: –––, 2007, “Reference and Perspective in Intuitionistic Logic,” *Journal of Logic, Language and Information*, 16 (1): 91–115.

[^orenstein-1990]: Orenstein, Alex, 1990, “Is Existence What Existential Quantification Expresses?” in Robert B. Barrett and Roger F. Gibson (eds.), *Perspectives on Quine*, Cambridge: Blackwell, 1990, pp. 245–270.

[^orlando-2008]: Orlando, Eleonora, 2008, “Names without Fictional Objects (Ficción sin metafísica),” *Crítica: Revista Hispanoamericana de Filosofía*, 40 (120): 111–127. Parsons, Terence, 1980, *Nonexistent Objects*, New Haven: Yale University Press.

[^paśniczek-1998]: Paśniczek, Jacek, 1998, *The Logic of Intentional Objects*: *A Meinongian Version of Classical Logic*, Dordrecht: Kluwer.

[^paśniczek-2001]: –––, 2001, “Can Meinongian Logic Be Free?” in Morscher and Hieke 2001, pp. 227–36.

[^pavlović-2021]: Pavlović, Edi, and Norbert Gratzl, 2021, “A More Unified Approach to Free Logics.” *Journal of Philosophical Logic* 50 (1): 117–48.

[^pavlović-2023]: –––, 2023, “Neutral Free Logic: Motivation, Proof Theory and Models.” *Journal of Philosophical Logic* 52 (2): 519–54.

[^posy-1982]: Posy, Carl J., 1982, “A Free IPC is a Natural Logic: Strong Completeness for Some Intuitionistic Free Logics,” *Topoi*, 1: 30–43; reprinted in Lambert 1991, pp. 49–81.

[^priest-2005]: Priest, Graham, 2005, *Towards Non-Being*, Oxford: Oxford University Press.

[^priest-2008]: –––, 2008, *An Introduction to Non-Classical Logic: From If to Is*, 2ⁿᵈ edition, Cambridge: Cambridge University Press.

[^quine-1948]: Quine, W. V. O., 1948, “On What There Is,” *Review of Metaphysics*, 48: 21–38; reprinted as Chapter 1 of Quine 1963).

[^quine-1954]: –––, 1954, “Quantification and the Empty Domain,” *Journal of Symbolic Logic*, 19: 177–179.

[^quine-1963]: –––, 1963, *From a Logical Point of View*, 2ⁿᵈ edition, New York: Harper & Row.

[^routley-1966]: Routley, Richard, 1966, “Some Things Do Not Exist,” *Notre Dame Journal of Formal Logic*, 7: 251–276.

[^routley-1980]: –––, 1980, *Exploring Meinong’s Jungle and Beyond*, Canberra: Australian National University.

[^russell-1919]: Russell, Bertrand, 1919, *Introduction to Mathematical Philosophy*, New York: Simon & Schuster.

[^sainsbury-2005]: Sainsbury, R. M., 2005, *Reference without Referents*, Oxford: Clarendon Press.

[^scales-1969]: Scales, Ronald D., 1969, *Attribution and Existence*. University of California, Irvine.

[^schock-1968]: Schock, Rolf, 1968, *Logics without Existence Assumptions*, Stockholm: Almqvist & Wiskell.

[^schütte-1971]: Schütte, Kurt, 1971, *Proof Theory*. Grundlehren Der Mathematischen Wissenschaften. Springer.

[^schweitzer-2001]: Schweitzer, Paul, 2001, “Free Logic and Quantification in Syntactic Modal Contexts,” in Morscher and Hieke 2001, pp. 69–85.

[^shapiro-2000]: Shapiro, Stewart, and Alan Weir, 2000, “‘Neo-Logicist’ Logic is Not Epistemically Innocent,” *Philosophia Mathematica*, 3 (8): 160–189.

[^simons-2001]: Simons, Peter, 2001, “Calculi of Names: Free and Modal,” in Morscher, Edgar and Alexander Hieke 2001, pp. 49–65.

[^smiley-1960]: Smiley, Timothy, 1960, “Sense without Denotation,” *Analysis*, 20: 125–135.

[^fraassen-1966]: van Fraassen, Bas C., 1966, “Singular Terms, Truth Value Gaps and Free Logic,” *Journal of Philosophy*, 63: 481–95; reprinted in Lambert 1991, pp. 82–97.

[^fraassen-1991]: –––, 1991, “On (the *X*)(*X* = Lambert),”, in W. Spohn, et al. (eds.), *Existence and Explanation*: *Essays Presented in Honor of Karel Lambert*, Dordrecht: Kluwer, pp. 1–18.

[^whitehead-1910]: Whitehead, Alfred, and Bertrand Russell, 1910, *Principia Mathematica*. Vol. 1. Cambridge: Cambridge University Press.

[^williamson-1999]: Williamson, Timothy, 1999, “A Note on Truth, Satisfaction and the Empty Domain,” *Analysis*, 59(1): 3–8.

[^williamson-2016]: –––, 2016, “Reply to Bacon, Hawthorne, and Uzquiano,” *Canadian Journal of Philosophy* 46(4–5): 542–547.

[^woods-2006]: Woods, John, 2006, “Fictions and their Logic,” in Jacquette 2006, pp. 1061–1126.

[^woodruff-1984]: Woodruff, Peter W., 1984, “On Supervaluations in Free Logic,” *Journal of Symbolic Logic*, 49: 943–950.

[^yeakel-2016]: Yeakel, Daniel, 2016, “Existence Hedges and Neutral Free Logic,” *Proceedings of the Aristotelian Society*, cxvi (3): 379–386.
