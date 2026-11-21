# Preference Logic
**First published Mon Jul 28, 2025**

*Liu, Fenrong, van der Torre, Leon*

The concept of preference spans numerous research fields, resulting in diverse perspectives on the topic. Preference logic specifically focuses on reasoning about preferences when comparing objects, situations, actions, and more, by examining their formal properties. This entry surveys major developments in preference logic to date. Section 2 provides a historical overview, beginning with foundational work by Halldén and von Wright, who emphasized the syntactic aspects of preference. In Section 3, early semantic contributions by Rescher and Van Dalen are introduced. The consideration of preference relations over possible worlds naturally gives rise to modal preference logic where preference lifting enables comparisons across sets of possible worlds. Section 4 introduces von Wright’s distinction between intrinsic and extrinsic preferences and presents a two-layer structure for extrinsic (or reason-based) preferences, a major focus of development over the last two decades. This entry reviews the primary frameworks in this area. Section 5 is about preference change, which can happen for various reasons, and it explores different logical approaches to these dynamics. Section 6 discusses various interpretations of *ceteris paribus* preferences, provides a review of its underlying logic, and examines conditional preference networks (CP-nets), which are closely related to this concept. Section 7 briefly examines the connections between preference logic and other research areas. Section 8 concludes this entry.

## 1. Introduction

Preference logic is inherently interdisciplinary, with representations and analyses of preference varying across different fields. But there is a distinct common feature—preference is concerned with comparing situations, objects, or actions. The binary relations involved in such comparisons are: “*A* is better than *B*” ($>$), “*A* is equally as good as *B*” ($\equiv$), and “*A* is at least as good as *B*” ($\geq$).

Preference logic began with syntactic approaches, which focused on the formal principles governing preference relations. In contrast, semantic approaches aim to provide interpretations of these relations, which enables the identification of conditions under which such principles hold. In particular, possible world semantics offers a systematic framework for exploring preference logic from a semantic perspective. The transition from syntactic to semantic approaches is reflected in this entry.

When agents make comparisons, the resulting preferences may either reflect their own tastes, without any external justification, or they may derive from specific reasons that are externally justified. Preferences formed purely on the basis of the agent’s own tastes are called *intrinsic* preferences. In contrast, preferences that can be explained or justified by external reasons are referred to as *extrinsic* preferences. In this entry, this distinction, famously made by von Wright (1963)[^wright-1963], serves as a central theme to introduce both classic and contemporary works in preference logic.

Extrinsic preferences require additional elements in a model in order to represent both preferences and the reasons that justify them. Such reasons can include priorities, object properties, or values. Several major frameworks have been proposed in logic and rational choice theory, where preferences were traditionally treated as fixed in both disciplines. The term “two-layer structure” will be used to describe these frameworks. This richer modeling approach enables reasoning about not only the preferences themselves but also the underlying reasons. Interestingly, a parallel development can be observed in deontic logic, where norm-based semantics introduces an additional structure to deontic notions, thus aligning closely with the ideas underpinning extrinsic preference models.

Another key topic in preference logic is the study of preference change, aligning with broader trends in incorporating new information. Just as attitudes such as knowledge, belief and intention may need to be updated, preferences may evolve with new information, changes in the agent’s state, or other factors. This entry assumes familiarity with belief revision theory (see SEP entry on preferences) and dynamic epistemic logic (DEL; see entry on dynamic epistemic logic) and focuses specifically on the unique aspects of preference change.

In AI systems where decisions must be made, preferences often need to be represented concisely. One central notion in this context is *ceteris paribus* preference, which enables reasoning about preferences such as “*A* is preferable to *B*, all else being equal”. This concept has been studied extensively in logic and also forms the basis for frameworks like CP-nets (conditional preference networks) in the computer science literature. CP-nets is a well-known visual language that balances expressive power with computational efficiency. Accordingly, this entry devotes significant attention to *ceteris paribus* preferences.

## 2. Syntactic approaches to preference logic

Pioneering logicians such as Halldén (1957)[^halldén-1957] and von Wright (1963)[^wright-1963] proposed logics for preferences that focused on comparisons between situations. These logics extended propositional language with a binary connective, $>$, denoting the concept of preference or “betterness”.

### 2.1 Halldén: two theories, A and B

Halldén’s (1957)[^halldén-1957] book *On the Logic of “Better”* is often taken as the starting point for a logical analysis of preference. It is a point of reference for all other preference logics. Halldén extended the propositional logic with two new connectives—what he called “ethical connectives”: “better” ($>$) and “equally as good as” ($\equiv$). He distinguished between the positive and negative sense of $\equiv$, which then led to Theory A and Theory B. Theory A is based on the *positive* sense and is formally given by $p\equiv q$ iff for all *r*, $r>p$ iff $r>q$, and $p>r$ iff $q>r$. Theory B is based on the *negative* sense, where $p\equiv q$ simply means $\neg(p>q)\land \neg(q>p)$.

The sentences, built up from propositional variables and ordinary truth-functional connectives as well as the two new connectives, are called “A-formulas”. They follow the usual convention of leaving out brackets, with the reading then based on decreasing binding order for $\neg$, $>$, $\equiv$, $\land$, $\lor$, $\rightarrow$, $\leftrightarrow$.

**Theory A.** Theory A, presented in Figure 1, is an extension of propositional calculus. Postulates $A_1–A_5$ show that Halldén treats $>$ as an asymmetrical and transitive relation, i.e., a partial order, while “$\equiv$” is treated as a reflexive, symmetrical and transitive relation, i.e., an equivalence relation. Halldén traced these assumptions back to Menger as early as 1939 (cf. Menger 1939)[^menger-1939]. $A_6$ concerns the interrelationship between the notions of better and equal value. The expansion principles $A_7$ and $A_8$ make use of negation. They also play a central role in von Wright’s preference logic later on.

**Theory A**

All theorems of propositional calculus are postulates of Theory A.

**$R_1$**

If *φ* and $\varphi\rightarrow\psi$ are theorems of A, then *ψ* is a theorem of A (*modus ponens*)

**$R_2$**

Suppose *φ* is a theorem of A, and *ψ* is similar to *φ* in all respects except one: wherever a certain variable occurs in *φ*, an A-formula occurs in *ψ*. Then *ψ* is a theorem of A (substitution)

**$R_3$**

Suppose *φ* and $\tau_1\equiv\tau_2$ are theorems of A, *ψ* is an A-formula, and *ψ* is similar to *ψ* in all respects except one: $\tau_1$ occurs in *ψ* in one or many places where $\tau_2$ occurs in *φ*. Then *ψ* is a theorem of A (replacement)

$$\begin{align*} \tag*{\(A_1\)} p> q\rightarrow\neg (q > p)&& \textrm{(\(>\)-asymmetry)}\\ \tag*{\(A_2\)} p>q \land q >r\rightarrow p>r&& \textrm{(\(>\)-transitivity)}\\ \tag*{\(A_3\)} p\equiv p&& \textrm{(\(\equiv\)-reflexivity)}\\ \tag*{\(A_4\)} p\equiv q \rightarrow q\equiv p&& \textrm{(\(\equiv\)-symmetry)}\\ \tag*{\(A_5\)} p\equiv q \land q\equiv r \rightarrow p\equiv r&& \textrm{(\(\equiv\)-transitivity)}\\ \tag*{\(A_6\)} p>q\land q\equiv r \rightarrow p>r&& \textrm{(\(>\equiv\)-transitivity)}\\ \tag*{\(A_7\)} p>q\leftrightarrow(p\land \neg q)> (q\land \neg p)&& \textrm{(\(>\)-expansion)}\\ \tag*{\(A_8\)} p\equiv q\leftrightarrow(p\land \neg q)\equiv(q\land \neg p)&& \textrm{(\(\equiv\)-expansion)} \end{align*} $$

\*Figure 1.\*

Halldén proves that Theory A is consistent. He presents several theorems of theory A such as contraposition: $p>q \rightarrow\neg q>\neg p$. He also considers fourteen optional postulates that can be added to Theory A. For example, there is the distribution postulate, $p>(q\land r)\rightarrow p>q \land p>r$, and the connectedness postulate, $p>q \lor p\equiv q \lor q>p$.

**Theory B.** The language of Theory B is a fragment of that of Theory A containing only those sentences that do not contain nested occurrences of $>$ and $\equiv$. Also, if $\varphi>\psi$ or $\varphi\equiv\psi$ occurs in a B-formula, then *φ* and *ψ* do not contain conjunction or disjunction symbols.

Theory B consists of the rules and postulates in Figure 2. Postulates $B_1–B_5$ are identical to $A_1–A_5$, $B6$ can be derived from Theory A, and $B_7$ represents connectedness.

**Theory B**

- All theorems of propositional calculus are postulates of B.
- The inference rules $R_1, R_2$ and $R_3$ of Theory A apply also in Theory B.

$$\begin{align*} \tag*{\(B_6\)} p>q \rightarrow\neg q>\neg p&& \textrm{(contraposition)}\\ \tag*{\(B_7\)} p>q \lor p\equiv q \lor q>p && \textrm{ (connected)} \end{align*}$$

\*Figure 2.\*

Theory B has been proven to be consistent. Interestingly, a procedure is provided to decide whether a given formula is a theorem of B. It consists of two steps called *univocal* expansion and *multivocal* expansion.

In the first phase, logical principles are applied to expand the formula. For example, $p\equiv q$ is replaced by $p\equiv q \land q \equiv p$, and $p> q\land q>r$ is replaced by $p> q\land q>r\land p>r$. Consider the following sequence of replacements from Halldén (1957)[^halldén-1957] to determine whether

$$p\equiv \neg p\land q\equiv \neg q \rightarrow \neg (p>q)$$

is a theorem:

$$\begin{gather*} p\equiv \neg p\land q\equiv \neg q \land p>q\\ p\equiv \neg p\land \neg p\equiv p\land q\equiv \neg q \land p>q\\ p\equiv \neg p\land \neg p\equiv p\land q\equiv \neg q \land \neg q\equiv q \land p>q\\ p\equiv \neg p\land \neg p\equiv p\land q\equiv \neg q \land \neg q\equiv q \land p>q\land \neg q>\neg p\\ p\equiv \neg p\land \neg p\equiv p\land q\equiv \neg q \land \neg q\equiv q \land p>q\land \neg q>\neg p\land \neg q>p\\ p\equiv \neg p\land \neg p\equiv p\land q\equiv \neg q \land \neg q\equiv q \land p>q\land \neg q>\neg p\land \neg q>p\land q>\neg p\\ p\equiv \neg p\land \neg p\equiv p\land q\equiv \neg q \land \neg q\equiv q \land p>q\land \neg q>\neg p\land \neg q>p\land q>\neg p\land p>\neg q \end{gather*}$$

The last formula is contradictory, thus we can conclude that $p\equiv \neg p\land q\equiv \neg q \rightarrow \neg (p>q)$ is a theorem.

If the first phase is not decisive, each formula is expanded into a set of more complex formulas in a second phase. For example, $p>q\land \neg q> \neg p$ cannot be further expanded using univocal expansion, but it may be expanded into this set of formulas:

$$\begin{align} &p>q\land \neg q> \neg p\land p>\neg p, \\ &p>q\land \neg q> \neg p\land p\equiv \neg p, \\ &p>q\land \neg q> \neg p\land \neg p>p, \\ &p>q\land \neg q> \neg p\land \neg p\equiv p, \end{align}$$

reflecting all possible relations between *p* and $\neg p$. Interested readers can find more details on how it works in Halldén’s (1957)[^halldén-1957] book.

### 2.2 Von Wright’s logic of preference

The second point of reference is *The Logic of Preference* by von Wright (1963)[^wright-1963]. In this book, von Wright distinguishes between three groups of concepts related to preferences while also noting that there are no sharp divisions between them. The relevant concept grouping is: deontological concepts (right, duty, command, prohibition), axiological concepts (good, evil, betterness), and anthropological concepts (need, want, decision, choice). These notions are explored in deontic logic and decision theory, and they intersect with preference logic. The connection will be discussed in Section 7. Von Wright also makes key distinctions that are relevant to the later development of preference logic:

- preferences between states of affairs vs. preferences over means or methods,
- intrinsic preference (intrinsic betterness) vs. extrinsic preference (preference with reasons),
- qualitative preference vs. measurable value (e.g., utility), and
- risk-free preference vs. preference under uncertainty.

More concretely, the formal language adopted by von Wright is again a fragment of Halldén’s A-formulas, and it consists of only those sentences that do not contain nested occurrences of $>$ and $\equiv$. However, in contrast to the language of Theory B, if $\varphi>\psi$ or $\varphi\equiv\psi$ occurs in a formula, then *φ* and *ψ* may contain conjunction or disjunction symbols.

Unlike Halldén’s two theories, the logic of preference is not presented as an axiomatic calculus. Instead, it serves as a technique for determining whether a given preference expression (P-expression) represents a logically true proposition.

The logic of preference is based on five key principles, shown in Figure 3. The first two—asymmetry and transitivity—describe relations among preferences and are derived from Halldén’s systems. The other three—expansion, disjunctive distribution, and amplification—allow any P-expression to be transformed into a standard form, which enables application of the decision technique. This technique is illustrated with an example. Consider the P-expression

$$(p>\neg p)\land (\neg q>q)\rightarrow(p>q).$$

Using expansion we obtain

$$(p>\neg p)\land (\neg q>q)\rightarrow(p\land \neg q>\neg p \land q).$$

As there is no disjunction in the atomic preferences, distribution is vacuous. The third step, amplification, gives the normal form

$$ \begin{align} (p\land q>\neg p\land q) &\land (p\land \neg q>\neg p\land \neg q)\\ &\land (p\land \neg q>p\land q)\\ &\land (\neg p\land \neg q>\neg p\land q) \rightarrow(p\land \neg q>\neg p \land q). \end{align} $$

This formula is a tautology, which can be explained as follows. The formula would be false if and only if the first four constituents

$$\begin{align} &(p\land q>\neg p\land q), \\ &(p\land \neg q>\neg p\land \neg q), \\ &(p\land \neg q>p\land q) \textrm{ and} \\ &(\neg p\land \neg q>\neg p\land q) \end{align}$$

were all true and $(p\land \neg q>\neg p \land q)$ were false. But this conflicts with transitivity.

Looking at the five principles concerning preference, one has to be careful because they are not closed under substitution. The reasoning behind this limitation is explained below.

**Von Wright’s 5 preference principles**

$$\begin{align} &\tag*{\(V_1\)} (p>q) \rightarrow\neg (q>p)&& \textrm{(\(>\)-asymmetry)}\\[1em] & \tag*{\(V_2\)} (p>q) \land (q >r)\rightarrow q>r&& \textrm{(\(>\)-transitivity)}\\[1em] & \tag*{\(V_3\)} (p>q)\leftrightarrow(p\land \neg q)> (\neg p\land q)&& \textrm{(\(>\)-expansion)}\\ \end{align}$$ $$ \begin{align}\tag*{\(V_4\)}\quad (p&\lor q)>(r \lor s) \leftrightarrow \\ &(p \land \neg r \land \neg s) > (\neg p\land \neg q \land r) \\ &\land\ (p\land \neg r \land \neg s)> (\neg p\land \neg q \land s)\\ &\land\ (q\land \neg r \land \neg s)> (\neg p\land \neg q \land r)\\ &\land\ (q\land \neg r \land \neg s)> (\neg p\land \neg q \land s) \ \text{(disjunctive distribution)} \end{align} $$ $$ \begin{align}\tag*{\(V_5\)} (p&>q) \leftrightarrow \\ &((p\land r)> (q\land r)) \\ &\land\ ((p\land \neg r)>(q\land \neg r)) \qquad {\textrm{(amplification)}} \end{align} $$

\*Figure 3.\*

Another contribution by von Wright is his attempt to understand the meaning of preference in terms of “changes”. His analysis reveals a unique way of viewing preference. When can one say that one state of affairs is preferable to another? To answer this question, consider two generic preference states, *p* and *q*. There are four possible cases: $p \land q$, $p \land \neg q$, $\neg p \land q$, and $\neg p \land \neg q$. Any world must necessarily fall into one of these four possibilities. This explains not only the first three principles, which had already been adopted by Halldén, but also the principle of disjunctive distribution, illustrated by $V_4$ in the table above.

In the case of $p\land q$, “an agent prefers *p* over *q*” means that the agent would prefer to lose *q* (and keep *p*) rather than lose *p* (and keep *q*).

In the case of $p\land \neg q$, “an agent prefers *p* over *q*” means that the agent would prefer to maintain the current state than see it change into $\neg p\land q$.

In the case of $\neg p\land q$, “an agent prefers *p* over *q*” means that the agent would prefer to see the world change from $\neg p$ to *p*, and *q* into $\neg q$, rather than see no change.

In the case of $\neg p \land \neg q$, “an agent prefers *p* over *q*” means that the agent would prefer to get *p* without *q* rather than get *q* without *p*.

Principle $V_5$ is the so-called *holistic* property of preference. Let *φ* be a formula, and let $PL(\varphi)$ be the set of propositional letters that occur in *φ*, which von Wright calls the universe of discourse. Suppose $r \not\in PL(\varphi>\psi)$, then replace every formula $\varphi> \psi$ with the conjunction

$$((\varphi\land r)> (\psi\land r)) \land ((\varphi\land \neg r)>(\psi\land \neg r)).$$

This principle, also called *amplification*, is applied to every *r* in the complement of $PL(\varphi > \psi)$ with respect to the set of propositional letters. Amplification ensures that every *r* in the universe of discourse that is not directly relevant to the evaluation of a preference subformula will remain constant.

While $V_1$, $V_2$, $V_3$ and $V_4$ appear in many axiomatic preference logics, this is not the case with $V_5$. The reason is that $V_5$ cannot be combined with substitution.

Since Halldén, numerous principles have been explored in the literature. For a comprehensive review see S. O. Hansson’s (2001)[^hansson-2001] chapter on the subject, which includes the following examples:

$$\begin{align*} \tag{H1} \textrm{There is no series } p_1,\ldots, p_n \\ \textrm{such that } p_1>\ldots>p_n>p_1 && \textrm{(\(>\)-acyclic)}\\ \tag{H2} p\equiv q \land q >r \rightarrow p>r &&\textrm{(\(\equiv\)\(>\)-trans)}\\ \tag{H3} p> q \land q >r \rightarrow p>s \lor s>r && \textrm{(semi-trans)}\\ \tag{H4} p>q \land r >s \rightarrow p>s \lor r>q && \textrm{(interval order)} \end{align*} $$

\*Figure 4:\* More preference principles

Both Halldén and von Wright emphasize the generality of the preference principles by adopting a syntactic or algorithmic approach. Later researchers have often used examples to support or challenge these principles, and many preference properties remain unsettled.

## 3. Semantic approaches to preference logic

This section provides a semantic perspective on preference by introducing an earlier proposal by Rescher (1967)[^rescher-1967] and Van Dalen (1974) as well as possible world semantics, which has been central to later research in this area.

### 3.1 Rescher-Van Dalen semantics

Rescher (1966, 1967)[^rescher-1966][^rescher-1967] introduced the first semantics for preference logic where models are real-valued functions on formulas. Van Dalen (1974) generalized this to partial orders, and he showed that the preference logic of Rescher is a special case. The semantic structures directly reflect the preferences expressed in the language. We present here the semantics and axiomatizations of Van Dalen.

The language coincides with the language of von Wright, i.e., it is an extension of propositional logic with the binary connective $>$, except in this case, it lacks nested preference statements. Indifference is defined in terms of preference as $\varphi\equiv \psi = \neg (\varphi>\psi)\land \neg (\psi>\varphi)$.

In order to assign truth values to formulas of the form $\varphi>\psi$, Van Dalen prescribes an order relation between propositions. He simultaneously considers a truth valuation *v* and a measure of goodness *m*. In this framework, *m* is a mapping of the set of propositions into a partially ordered set *A*, and *v* is a mapping of propositional symbols (atoms) into $\{0,1\}$, which is extended to all formulas by the following inductive definition:

1. $v(\neg \varphi) = 1-v(\varphi)$
2. $v(\varphi\lor\psi) = \textrm{max}\{v(\varphi),v(\psi)\}$
3. $v(\varphi P\psi) = 1$ if $m(\varphi) \lt m(\psi)$ on *A*, or 0 otherwise

For a set *Γ* of formulas, the satisfaction relation is defined by:

$$\begin{align*} A, m, v \models p &\quad \textrm{ iff}\quad v(p) = 1 \textrm{ for atomic } p\\ A, m \models \varphi &\quad \textrm{ iff}\quad A, m, v \models \varphi \textrm{ for all } v\\ A, v \models \varphi &\quad \textrm{ iff}\quad A, m, v \models \varphi \textrm{ for all } m\\ A \models \varphi &\quad \textrm{ iff}\quad A, m, v\models \varphi \textrm{ for all } m \textrm{ and } v\\ \models \varphi &\quad \textrm{ iff}\quad A \models \varphi \textrm{ for all } A (\varphi \textrm{ is true})\\ A, m, v \models \Gamma &\quad \textrm{ iff}\quad A, m, v \models \Gamma \textrm{ for all } \varphi\in\Gamma\\ \Gamma\models \varphi &\quad \textrm{ iff}\quad A, m,v\models\Gamma \Rightarrow A, m,v\models \varphi\\ \end{align*}$$

Van Dalen calls the semantics described above irrational semantics, mainly because logically equivalent propositions can lead to different preferences. He therefore considers three extra conditions to the measure *m* or the partially set *A* in order to get semantics of a more restricted kind:

1. If $\varphi\equiv \psi$ is a tautology, then $m (\varphi) = m(\psi)$.
2. *A* is linearly ordered.
3. *A* is the set of reals and $m(\neg \varphi)=-m(\varphi)$.

Van Dalen presents several theories—**PREFIR**, **PREF**, **PREFL**, and **PREFR**—outlined in Figure 5. He demonstrates that **PREFIR** is complete for irrational semantics, **PREF** is complete for semantics with condition (i), **PREFL** is complete for linear semantics, and **PREFR** is complete for Rescher semantics.

Van Dalen’s preference theories **PREFIR**, **PREF**, **PREFL** and **PREFR**

- All tautologies of classical propositional logic are axioms.
- *Modus ponens* and replacement (see Halldén’s Theory A)

$$\begin{align*} \tag*{P1} \neg (\varphi> \varphi) \\ \tag*{P2} \varphi>\psi \land \psi >\chi \rightarrow \varphi> \chi\\ \tag*{P3} \varphi>\psi \land \psi \equiv\chi \rightarrow \varphi> \chi\\ \tag*{P4} \varphi>\psi \rightarrow \neg \psi > \neg \varphi\\ \end{align*}$$

We will consider a number of axiom systems, all of which have tautologies as axioms and *modus ponens* as a rule of inference. All but the first have the rule of replacement as a rule of inference.

**PREFIR**

Axioms P1, P2 (only the *modus ponens* rule is applied)

**PREF**

Axioms P1, P2

**PREFL**

Axioms P1, P2, P3

**PREFR**

Axioms P1, P2, P3, P4

\*Figure 5.\*

Moreover, Van Dalen shows that all systems have the finite model property and are decidable. He also extends the language with monadic operators for good, bad and neutral, and he considers nested preference statements. Other authors like Chisholm and Sosa (1966) consider first-order extensions of such preference logics.

### 3.2 Preference over possible worlds

In an era of rapid advancements in modal logics (see entry on modal logic), binary preference relations have been incorporated naturally into possible world semantics to enable the comparison of different situations or worlds in various contexts. This subsection and the next review modal preference logic and discuss various methods for lifting preferences in order to compare sets of possible worlds.

Dyadic modal logic has been developed since the late 1960s to model conditional obligations (B. Hansson 1969)[^hansson-1969] along with related formalisms for conditionals (Lewis 1973; Makinson 1993)[^lewis-1973][^makinson-1993]. In these frameworks, a preference structure underlying possible world semantics was employed, particularly in studies of deontic logic and conditionals.

Starting in the late 1980s, a widely adopted monadic modal approach emerged that explored preferences within non-monotonic logic and belief revision (Boutilier 1990; Lamarre 1991)[^boutilier-1990][^lamarre-1991] as well as deontic logic (Tan & Van der Torre 1996)[^tan-1996]. While the motivations behind these works vary, the monadic modal approach in some cases offers a more straightforward path to axiomatizing preference logic.

Research on preference logic has frequently been linked to understanding agent choices in dynamic environments. A central focus is how agents rank possible worlds in order to express their preferences. This allows for more nuanced models of decision-making and normative reasoning. The integration of preference orders into modal logic, inspired by earlier developments in conditional logic and belief revision, extends the expressive power of logical systems by incorporating preference structures over possible worlds.

A modal preference model $\mathcal{M}$ is a triple $(W, \succeq, V)$ where *W* is a set of possible worlds, $\succeq$ is a binary preference relation over these worlds, and *V* is a valuation assigning truth values to propositional letters in these worlds. Depending on the context, we assume the preference relation $\succeq$ has certain properties. For instance, it can be a (total) pre-order, or a partial order, etc. If we choose (total) pre-order, a strict preference relation “$w\succ v$” can then be defined as “$w\succeq v\land v \nsucceq w$”, and an indifference relation “$w\approx v$” can be defined as “$w\succeq v\land v\succeq w$”.

On the syntactic side, a modal preference language is given to express the basic preference relations and their properties. The language is an extension of propositional logic, with two new operators $\lozenge^{\geq}\varphi$ and $\lozenge^{>}\varphi$ (Van Benthem, Girard, & Roy 2009)[^van-2009]. Their truth conditions are defined below:

$\mathcal{M}$, $w \models \lozenge^{\geq} \varphi$    iff    for some *v*   with $v\succeq w$, $\mathcal{M}$, $v \models \varphi$.

$\mathcal{M}$, $w \models \lozenge^{>} \varphi$    iff    for some *v*   with $v \succ w$, $\mathcal{M}$, $v \models \varphi.$

The theory shown in Figure 6 below is an axiomatization of the modal preference logic given by Van Benthem, Girard, and Roy (2009) where $\succeq$ is a transitive and reflexive relation and E is an existential modality, interpreted as follows:

$\mathcal{M}, w \models E\varphi$    iff    for some $v, \mathcal{M}, v \models \varphi$.

**Modal preference logic**

- S4 for $\lozenge^{\geq}$, S5 for *E*, K for $\lozenge^{>}$.
- Inclusion axioms:
- $\lozenge^{>} \varphi\rightarrow\lozenge^{\geq} \varphi$
- $\lozenge^{\geq} \varphi\rightarrow\lozenge E\varphi$
- Interaction axioms between $\lozenge^{\geq}\varphi$ and $\lozenge^{>} \varphi$:
- $\lozenge^{>}\lozenge^{\geq} \varphi\rightarrow\lozenge^{>} \varphi$
- $\lozenge^{\geq}\lozenge^{>} \varphi\rightarrow\lozenge^{>} \varphi$
- $\psi\land \lozenge^{\geq}\varphi\rightarrow\lozenge^{>}\varphi\lor \lozenge^{\geq}(\varphi\land \lozenge^{\geq}\psi)$

\*Figure 6.\*

### 3.3 Preference lifting

The modal preference language described above can express the properties of preference relations between possible worlds. But addressing relationships between sets of possible worlds presents a lifting problem (Thomason & Horty 1996)[^thomason-1996] as it involves extending a property that applies to individual worlds so that it also applies to sets of worlds. There are various ways of achieving this. The three examples below use only two quantifiers.

$$\begin{align*} p\geq^{\forall\forall}q & := \forall w \models q\, \forall v\models p: v\succeq w \\ p>^{\forall\forall}q & := \forall w \models q\, \forall v\models p: v\succ w \\ \end{align*}$$ $$\begin{align*} p\geq^{\forall\exists}q & := \forall w \models q\, \exists v\models p: v\succeq w \\ p>^{\forall\exists}q & := \forall w \models q\, \exists v\models p: v\succ w \\ \end{align*}$$ $$\begin{align*} p\unrhd^{\overline{\forall\forall}}q & := \forall w \models p\, \forall v\models q: v\not\succ w \\ p\rhd^{\overline{\forall\forall}}q & := \forall w \models p\, \forall v\models q: v\not\succeq w\\ \end{align*}$$

On the syntactic side, to express the lifting, the basic modal preference language is extended with the universal modality $U\varphi$ (and its dual $E\varphi$) (Boutilier 1992)[^boutilier-1992]. The truth definition for this new modality is:

$\mathcal{M}$, $w \models U \varphi$    iff    for all *v*  , $\mathcal{M}$, $v \models \varphi$.

With this modality, the language gains greater expressive power to define generic preference notions related to the lifting problem. We provide one example:

$$\varphi\geq^{\forall\exists}\psi \coloneq U(\varphi\rightarrow\lozenge^{\geq}\psi).$$

We can read $\varphi\geq^{\forall\exists}\psi$ as “for each *φ*-world, there exists a *ψ*-world which is as good as that *φ*-world”. We can define other notions of generic preference in a similar manner. For instance, $\forall\exists$-preference and $\exists\exists$-preference can be defined in the language as follows:

1. $\varphi\geq^{\forall\exists}\psi \coloneq U(\varphi\rightarrow\langle\geq\rangle\psi)$
2. $\varphi\geq^{\exists\exists}\psi \coloneq E(\varphi\land\langle\geq\rangle\psi)$

Van Benthem, Girard, and Roy (2009) argue that $\geq^{\forall\forall}$ under *ceteris paribus* represents the notion of “preference” intended by von Wright (1963)[^wright-1963] in his seminal work on preference logic and offers an axiomatization for it. The logic of *ceteris paribus* preference will be discussed in Section 6.

Other attempts to axiomatize logics for preference relations over sets of possible worlds have emerged across various research areas. Notable contributions include the works of Van Fraassen (1973), Lewis (1973)[^lewis-1973], Spohn (1988)[^spohn-1988], Boutilier (1990)[^boutilier-1990] and Halpern (1997)[^halpern-1997] among many others. An illustrative example is provided below.

Halpern (1997)[^halpern-1997] proposed a complete axiomatization for the logic of “relative likelihood”. It was structurally similar to the logic of preference, or simply “preference” as he termed it. Unlike earlier axiomatizations, he accounted for both total and partial pre-orders. The language used is the same as that employed by von Wright—it excludes nested preference formulas—except that the atomic preference formulas $\varphi>\psi$ may include conjunctions and disjunctions.

Given a preference model $\mathcal{M}=(W, \succeq, V)$, the preference formula is interpreted as follows:

> $\mathcal{M} \models \varphi > \psi$ iff $\llbracket \varphi \rrbracket _{\mathcal{M}}$ is nonempty, $\forall v \in \llbracket \psi \rrbracket _{\mathcal{M}}\exists u \in \llbracket \varphi \rrbracket _{\mathcal{M}}$ such that $u\succ v$ and *u* dominates $\llbracket \psi \rrbracket _{\mathcal{M}}$

and *u* dominates *V* if there is no $v' \in V$ such that $v'\succ u$.

The complete axiomatization of Halpern (1997)[^halpern-1997] when $\succeq$ is a partial order consists of the axioms and rules listed in Figure 7. Axiom 2 corresponds to the reflexivity of $\succeq$, and axiom 3 corresponds to the transitivity of $\succeq$. In the case of a total preorder, the axiom $\varphi_1>\varphi_2\rightarrow (\varphi_1>\varphi_3)\lor(\varphi_3>\varphi_2)$ must be added.

**System AX**

1. All substitution instances of tautologies of propositional calculus.
2. $\neg (\varphi> \varphi)$
3. $((\varphi_1 \lor \varphi_2)> \varphi_3) \land ((\varphi_1\lor \varphi_3)> \varphi_2)\rightarrow(\varphi_1>(\varphi_2\lor \varphi_3))$
4. $U (\varphi_1\rightarrow\varphi_2) \land U(\varphi_3\rightarrow\varphi_4)\land(\varphi_1>\varphi_4) \rightarrow(\varphi_2>\varphi_3)$
5. Gen. $U\varphi,$ for all propositional tautologies.
6. MP. From *φ* and $\varphi\rightarrow\psi$ infer *ψ*.

\*Figure 7.\*

A recent paper by Shi and Sun (2021) explores an alternative method of preference lifting known as the Egli-Milner order. This bidirectional approach, formally defined below, considers both the best and worst elements across sets, aligning with the maximin principle of favorably balancing the worst outcomes:

$$\mathcal{M}, w \models \varphi \geq \psi \text{ iff } \begin{cases} (1) \ \forall x \in \llbracket\varphi\rrbracket_w \ \exists y \in \llbracket\psi\rrbracket_w : x \succeq_w y; \\ (2) \ \forall x \in \llbracket\psi\rrbracket_w \ \exists y \in \llbracket\varphi\rrbracket_w : y \succeq_w x \end{cases}$$

where $\llbracket\varphi\rrbracket_w$ denotes the set of *w*-accessible worlds that satisfy *φ*. Traditionally applied in fields like denotational semantics, Shi and Sun (2021) extend the Egli-Milner order to preference logic by developing a complete axiomatic system for the “convex order” derived from a total pre-order.

## 4. Reason-based preference

Over the last two decades, the study of the logic of reason-based preference has been a primary focus of several research efforts surveyed in this section.

### 4.1 Intrinsic vs. extrinsic preferences

The concept of reason-based preference originates from a well-known distinction between intrinsic and extrinsic preferences introduced by von Wright (1963)[^wright-1963]. This distinction hinges on whether a preference is grounded in an explicit reason or justification.

An *extrinsic preference* arises when one option is preferred over another because it is regarded as better in a specific respect. For example, in von Wright’s example, one person prefers claret over hock because it is beneficial for her health. Here, the preference for claret is extrinsic since it is based on an objective judgment about health benefits. Extrinsic preferences are thus tied to some underlying rationales, often involving external factors like health, practicalities, or expert advice.

In contrast, an *intrinsic preference* is a preference based purely on personal liking, without any need for an explicit reason or justification. For instance, one person may prefer claret to hock simply because she likes the taste. This preference is intrinsic because it is driven solely by subjective enjoyment, with no reference to any external rationale.

In formal models of extrinsic preference, a *two-layer structure* is typically adopted to account for the reason base and the preference.

### 4.2 Two-layer structures

#### 4.2.1 Priorities and preference

In the context of deciding between options, the notion of priorities was introduced (Liu 2008, 2010; De Jongh & Liu 2009)[^liu-2008][^liu-2010]. Priorities represent important properties ordered according to an individual’s considerations, which in turn determine preference among choices.

A two-layer structure consists of a priority base and preferences. A *priority base* is a set of properties ranked according to an agent’s considerations. Consider the example of Alice, who is deciding which house to buy. She evaluates each house based on three criteria—cost, quality, and neighborhood—in that order of importance. For Alice, the cost of a house is good if it fits her budget; otherwise, it is bad. Her decision is thus guided by whether the house meets her prioritized criteria and the relative importance of those criteria.

To formalize this, a first-order logic is used with constants $d_0,$ $d_1,$…, variables $x_0,$ $x_1,$…, and predicates $P,$ $Q,$ $P_0,$ $P_1,$…. For simplicity, this setup assumes a finite domain with monadic predicates and simple, usually quantifier-free formulas.

Formally, a priority base is an ordered sequence of formulas, written as

$$C_1(x) \gg C_2(x) \gg \dots \gg C_n(x) \quad (n \in \mathbb{N}),$$

where each $C_m(x)$ ($1 \leq m \leq n$) is a formula with exactly one free variable *x*. The earlier priorities are considered lexicographically more significant than later ones, creating a preference order. For example, $C_1 \land \neg C_2 \land \dots \land \neg C_m$ is preferred over $\neg C_1 \land C_2 \land \dots \land C_m$.

To illustrate this, Alice’s priority base might look like

$$C(x) \gg Q(x) \gg N(x),$$

where $C(x)$, $Q(x)$, and $N(x)$ represent that *x* has a low price (cost), high quality, and a good neighborhood, respectively. Given two houses $d_1$ and $d_2$ with properties $C(d_1),$ $C(d_2),$ $\neg Q(d_1),$ $\neg Q(d_2),$ $N(d_1)$, and $\neg N(d_2)$, Alice would prefer $d_1$ over $d_2$ according to this priority base.

The linearly-ordered priorities in the two-layer structure can also be generalized to partially ordered priority graphs (which allows certain priorities to be non-comparable) or even to unordered sets of properties (Kratzer 1981; Liu 2011b)[^kratzer-1981][^liu-2011b].

In deontic logic, the two-layer structure (where priorities establish a preference or obligation ordering) has also been widely recognized, particularly in systems that prioritize commands (see the work of Hansen 2008 and Van Benthem, Grossi, & Liu 2010)[^hansen-2008][^liu-2010][^van-2010], which will be discussed in Section 7.

##### Belief as reasons

The above method of defining preference from a priority base presupposes complete information about whether an alternative possesses the properties in the base. In cases of incomplete information, beliefs play a crucial role, and agents’ preferences depend on them. This situation requires the introduction of formulas such as $BC(x),$ $\neg BC(x),$ or $B\neg C(x),$ where $C_m$ represents priorities. This approach enables complex aspects to be considered, e.g., determining whether certain properties from the priority base apply or, more fundamentally, forming a priority base based on beliefs. Addressing such uncertainties calls for a combination of doxastic and preference languages; see the work of Liu (2011b)[^liu-2011b] for various procedures for defining preference under uncertainty. In this setting, beliefs about whether an alternative has or doesn’t have a certain priority serve as reasons for preference.

#### 4.2.2 Salient properties and preference

Rational choice theory typically assumes that agents have fixed preferences but does not explain the origin of these preferences. Dietrich and List (2013a,b) started to address this gap. They proposed a framework for modeling preference formation and change by suggesting that preferences are based on the “motivationally salient” properties of alternatives rather than the alternatives themselves. This approach allows preferences to be reason-based, evolving as different properties become salient.

To formalize this: an agent’s preference order over alternatives depends on the properties of these alternatives, which are motivationally salient in a given state.

Let *X* be a set of alternatives. Let *P* be the set of all possible properties an alternative might have. A motivational state $M \subseteq P$ includes all the properties deemed salient by the agent in a given context.

Preferences are defined by a binary relation $\succeq_M$ over *X*, where $x \succeq_M y$ means alternative *x* is weakly preferred to *y* in state *M*.

To account for varying preferences across motivational states, Dietrich and List (2013a,b) introduced the *weighing relation* $\geq$ over *property combinations*:

- Each alternative *x* can be described by the set of properties it has, denoted as $S_x$.
- For any two sets of properties, $S_x \geq S_y$ indicates that the properties in $S_x$ are preferred over those in $S_y$.
- The weighing relation thus acts as a stable underlying structure that supports the agent’s preference ordering across different motivational states.

Formally, if *x* and *y* are alternatives, then the agent’s preference $x \succeq_M y$ in state *M* can be represented as follows:

$$x \succeq_M y \iff S_x \geq S_y,$$

where $S_x = \{ P \in M : x \text{ has } P \}$ and $S_y = \{ P \in M : y \text{ has } P \}$. This relation ensures that the agent’s preferences in any motivational state *M* reflect the agent’s stable evaluation of property combinations across contexts.

The works of Dietrich and List (2013a,b) explore rationality by contrasting *structural rationality*, which focuses on internal consistency in preferences (as in traditional economics), with *substantive* rationality, which evaluates the content or worthiness of preferences. Formal rationality demands logical coherence, such as the preference of *A* over *C* if *A* is preferred over *B* and *B* over *C*. Substantive rationality, however, considers preferences to be “irrational” if they are self-destructive or harmful, even if they are consistent, as it assesses the value of the preferences, not just their coherence. An earlier discussion on these philosophical issues can be found in the work of Pettit (2002)[^pettit-2002].

#### 4.2.3 Reasons and preference

Osherson and Weinstein (2012) propose a logic of preference where preferences are not arbitrary or merely consistent but are based on identifiable reasons. This framework introduces modal connectives that allow the reasons for desiring a certain outcome to be expressed formally, which provides a way to model how various reasons combine to shape an agent’s preferences.

When choosing whether or not to install a fire alarm, a person may consider safety and cost as different reasons that support or oppose that course of action. In this example, a preference for installing a fire alarm puts great value on increasing safety, so this preference is based on a “safety reason”. If finances are tight, the cost may serve as a reason against installing the alarm.

Each reason (e.g., safety or cost) can be quantified using *utility scales* representing how much better or worse each choice is, based on a specific criterion. Formally, a “utility function” *u* is defined as a mapping

$$u: W \times S \rightarrow \mathbb{R}$$

where *W* is the set of possible worlds and *S* indexes utility scales such as safety or cost.

To evaluate a choice such as whether or not to install a fire alarm, the model uses a “selection function” *s* to identify alternative worlds that are closest to the real world for comparison purposes. For example, it compares

- world $w_1$, where a fire alarm is installed (a safer world), and
- world $w_2$, where no fire alarm is installed (the current, less safe world).

Formally, the “selection function” $s(w, A)$ selects a representative world from set *A* based on its similarity to the current world *w*:

$$s(w, A) = \text{closest world in } A \text{ to } w.$$

Finally, the preference relation can be formally defined using modal expressions. For instance, $p \succ_1 \neg p$ holds if, for safety reasons, installing an alarm (represented by *p*) is preferred over not installing one, denoted by the utility scale $u_1$ for safety. If $u_2$ (cost) is also considered, the preference relation may combine both $u_1$ and $u_2$, thereby capturing a comprehensive view that balances safety and cost.

This logic framework enables structured reasoning that incorporates specific reasons behind preferences, allowing for a nuanced representation of choices grounded in real-life decision-making contexts.

Osherson and Weinstein explore decidability issues and various conditions for subclasses of models.

Two-layer structures have become a standard approach to modeling preferences with reasons, with potential applications in various fields. A recent example is preferences that stem from underlying causal considerations—see Xie and Yan’s (2024) work on this topic. In a similar vein, Chen, Shi, and Wang (2024) integrates preference and dependence into cooperative games, providing a unified perspective on concepts like Nash equilibrium, Pareto optimality, and the Shapley core.

## 5. Dynamics of preference change

Preferences can change due to various triggers, making preference change a natural phenomenon to consider. Logical modeling has thus been proposed as a way to study reasoning about these dynamics. This section partially follows the categorization of preference change outlined by Lang and Van der Torre (2008), which is based on the type of input driving the change. Additionally, this section highlights the dynamical changes that can occur in two-layer structures. Grüne-Yanoff and Hansson (2009) discussed why preference change has been overlooked in the social sciences, particularly in economics, and the volume of essays presents various approaches to studying preference change (see also the section on preference change in the entry on [preferences](https://plato.stanford.edu/entries/preferences/#PreCha)). This section examines the primary ideas and formal frameworks within the logic tradition.

### 5.1 Intrinsic preference revision

The first type of preference change is analogous to belief change: just as belief revision incorporates newly acquired beliefs into an existing belief state, intrinsic preference revision incorporates new preferences into an existing preference state. Here, preferences are revised by other preferences to form new preferences, without beliefs intervening.

Two main methodologies are used to model preference change: the Alchourrón, Gärdenfors and Makinson (AGM) postulational framework (see the description of the AGM belief revision theory in the entry on logic of belief revision) and dynamic logic-based systems (see entry on dynamic epistemic logic). Both have been widely adopted by researchers to explore various forms of preference change.

Sven Ove Hansson (1995)[^hansson-1995] provided a detailed analysis of preference change, identifying four distinct types within the AGM framework:

- **revision**: acquiring a preference for *φ* over *ψ* with the revision statement “*φ* is preferable to *ψ*”.
- **contraction**: removing the preference that “*φ* is preferable to *ψ*”.
- **addition**: adding a new alternative to the set of options considered.
- **subtraction**: removing an option from the set of options considered.

While belief revision assigns priorities to minimize changes to prior beliefs, Hansson argues that priorities are unsuitable for preference revision. In preference revision, accommodating a new statement like $\varphi\succeq \psi$ can involve adjusting the position of either *φ* or *ψ*. He also proposes a similarity measure to keep the revised preference model as close to the original as possible, along with AGM-style postulates for these operators.

Van Benthem and Liu (2007) developed an extension of dynamic epistemic logic as a way to reason about preference change. A “suggestion” operator was introduced, denoted as $\sharp\varphi$. The formula $[\sharp\varphi]\psi$ means “After *φ* is publicly suggested, *ψ* holds”, and is defined as:

$$(\mathcal{M}, s) \models [\sharp \varphi]\psi \quad\textrm{ iff }\quad \mathcal{M}_{\sharp \varphi}, s \models \psi$$

where $\mathcal{M}_{\sharp \varphi}$ is defined with the same domain, valuation, and actual world as $(\mathcal{M}, s)$ but with the preference relations updated by subtracting the preference links from *φ*-worlds to $\neg \varphi$-worlds:

$$\leq^{*} = \leq - \{(s, t) \mid \mathfrak{M}, s \models \varphi \textrm{ and } \mathfrak{M}, t \models \neg \varphi\}.$$

More generally, in this framework, suggestion $\sharp(\varphi)$ can be understood as a relational program in propositional dynamic logic (PDL) (cf. Harel, Kozen, & Tiuryn 2000)[^harel-2000], with

$$(?\neg \varphi ; R) \cup (R ; ?\varphi)$$

indicating that all existing *R* links are retained with the exception of those links from *φ*-worlds to $\neg \varphi$-worlds. This setup allows for different types of preference change. For example, adding preference links (making every *φ*-world preferable to every $\neg \varphi$-world) can be represented as

$$R := R \cup (?\neg \varphi ; \top; ?\varphi)$$

where $\top$ denotes the universal relation. *Radical preference upgrade* is defined as

$$\Uparrow \varphi(R) := (?\varphi;R;?\varphi)\cup(?\neg \varphi; R;?\neg \varphi) \cup (?\neg \varphi;\top;?\varphi)$$

which makes all *φ*-worlds preferable to all $\neg \varphi$-worlds while preserving the original ordering within each group.

This dynamic preference logic extends DEL by supporting various relation-changing operators, and Van Benthem and Liu (2007) provide completeness theorems for these operators. Their results leverage the PDL format, which enables reduction of dynamic modalities and recursive computation of reduction axioms.

### 5.2 Preference change driven by belief update

The second type of preference change arises in response to changes in belief and reflects the dynamic interplay between what an agent believes and how they evaluate options. This topic has gained reasonable attention (see the work of Bradley 2007, Lang & Van der Torre 2008, and Liu 2011b)[^bradley-2007][^lang-2008][^liu-2011b]. For instance, following the tradition of decision theory established by Savage (1954)[^savage-1954], Bradley argues that preference change can arise from a change in beliefs where “preference change is induced by a redistribution of belief across some partition of the possibility space”. He formalizes this principle using a Bayesian approach. Consider the following example by Lang and Van der Torre (2008):

> Initially, I desire to eat sushi from this plate. Then I learn that this sushi has been made with old fish. Now I desire not to eat this sushi. (2008: 351)

Learning that the sushi was made with old fish changes my belief, which then reverses my initial preference. Here, preference change is a consequence of belief change, making belief change the key element to model.

The AGM framework addresses belief revision by establishing postulates for how a belief set should adapt to new, possibly conflicting, information. Lang and Van der Torre (2008) apply a similar approach to preference change resulting from belief updates. The formal language proposed includes: a dyadic modal operator for belief, $N(\alpha\mid\beta)$, meaning “*α* is normal (or believed) given *β*”; a preference operator, $P(\alpha\mid\beta)$, meaning “*α* is preferred given *β*”; and a dynamic operator, $[*\alpha]\beta$, read as “after learning *α*, *β* holds”. To capture the properties of preference change, they propose eight postulates. Two examples are given below:

$$\tag{P1} P\alpha \rightarrow [*\alpha]P\alpha $$

(P1) means that learning that something is already preferred does not alter the initial preference. For instance, if I desire wealth, then upon becoming wealthy, this preference remains. This persistence generally feels natural, but is debated; in Jeffrey’s decision theory, for example, once you become wealthy, the desire to become wealthy may no longer apply.

$$\tag{P5} P\alpha \land N\beta \rightarrow [*\beta]P\alpha$$

(P5) implies that learning that something that was expected is actually the case should not alter existing preferences. This principle, equivalently stated as $P\alpha \land \neg[*\beta]P\alpha \rightarrow \neg N\beta$, expresses that unexpected information is necessary for preference change to occur.

In summary, belief updates drive preference changes, which demonstrates their close relationship. Frameworks like the AGM theory and dynamic logic systems provide tools for modeling this evolution.

### 5.3 Two-layer models of preference change

In a two-layer structure, the priority base can shift due to changes in the relative importance of factors naturally leading to corresponding changes in preferences. De Jongh and Liu (2009) examined the interplay between a linear priority base and preferences and showed how priority shifts influence preference relations. In a related context, Andréka, Ryan, and Schobbens (2002) explored methods for deriving preferences from various priority orderings within a more general, non-linear graph structure. Building on these ideas, Girard (2008)[^girard-2008] and Liu (2011a)[^liu-2011a] introduced basic graph update operations that offer a formal framework for analyzing changes in priority structures. Christoff, Gratzl, and Roy (2021) studied the proof theory of priority merge in labeled sequents.

#### 5.3.1 Graph updates: basic operations

Suppose there is a priority base, denoted as $\mathscr{B}$, which is a set of prioritized propositions. When a new proposition *A* is added, there are straightforward options for incorporating it:

- **give *A* the highest priority**: *A* can be placed at the top of the priority base to make it the most important proposition.
- **give *A* the lowest priority**: *A* can be added to the bottom to give it the lowest priority.
- **side by side**: *A* can be placed alongside $\mathscr{B}$ without establishing an order between *A* and the other priorities.

The set $\alpha(\mathscr{B}, A)$ of basic graph updates is defined in a way that allows these possible changes to be captured:

$$\alpha(\mathscr{B}, A) := A \mid \mathscr{B}_1 ; \mathscr{B}_2 \mid \mathscr{B}_1 \parallel \mathscr{B}_2.$$

Here, $\mathscr{B}_1 ; \mathscr{B}_2$ represents the sequential composition of adding $\mathscr{B}_1$ on top of $\mathscr{B}_2$ so that every element in $\mathscr{B}_1$ has a higher priority than every element in $\mathscr{B}_2$. Parallel composition, ($\mathscr{B}_1 \parallel \mathscr{B}_2$), combines $\mathscr{B}_1$ and $\mathscr{B}_2$ as disjoint sets with no priority ordering between them.

A priority base can be modified not only by inserting new propositions but also with deletion operations that remove priorities. For example, top deletion removes any items from the priority base that are not “dominated” by others, i.e., those that have the highest priority level.

These basic graph updates provide simple ways to restructure a given priority base by adding or removing propositions.

#### 5.3.2 Tracking dynamics

To track changes across different levels—at the world layer and the priority layer—we define a specific technical notion. Given a priority update $\alpha: (\mathscr{B}, A) \rightarrow \mathscr{B'}$ and a world-level map $\sigma: (\preceq, A) \rightarrow \preceq'$, it is said that *α* *induces* *σ* if:

$$\sigma(\preceq_{\mathscr{B}}, A) = \preceq_{\alpha(\mathscr{B}, A).}$$

An operation *α* is a *PDL-definable operation* if it induces a *PDL*-definable relation transformer *σ* by using tests for formulas in the language, weak and strict basic preference relations *R*, and the universal relation, while allowing arbitrary unions and sequential compositions:

$$\pi:=?\varphi \mid R\mid R^{<} \mid \top\mid ;\mid \cup.$$

These are interpreted as the standard *PDL* program operations of *test* $?\varphi$, *sequential composition* $``;"$ and *choice* $``\cup"$.

In the two-layer framework, it is interesting to see how priority dynamics can mirror preference dynamics. For example, it is possible to achieve a preference change due to a “suggestion” operator either by altering the world-layer preference relation or by modifying the priority base. If a new proposition *A* is added in parallel to an existing base $\mathscr{B}$, the preference relation is updated, as shown in the following commuting diagram:

![a commuting diagram: link to extended description below](../assets/logic-preference/figxy1.svg)

\*Diagram A:\* Commutative diagram where new proposition A is added in parallel to an existing base [An extended description of Diagram A is in the supplement.]

Similarly, placing a new proposition *A* at the top of the priority graph $(\mathscr{B}, <)$ aligns with a radical upgrade at the world level:

![a diagram: link to extended description below](../assets/logic-preference/figxy2.svg)

\*Diagram B\*: Commutative diagram where new proposition A is placed at the top of the priority graph [An extended description of Diagram B is in the supplement.]

These examples illustrate cases where priority-layer transformations correspond seamlessly with world-layer relation updates.

While priority dynamics and preference dynamics will often align, there are limits. For instance, the deletion operation $\textit{del}(\mathscr{B})$ is not *PDL*-definable (Liu 2011a)[^liu-2011a]. Certain natural priority-layer modifications cannot be fully represented at the world layer.

#### 5.3.3 Belief-driven preference change in two-layer structures

In two-layer structures, it also makes sense to consider preference changes driven by belief updates. Within the framework of De Jongh and Liu (2009), various strategies are employed to derive preferences from priorities and beliefs, as illustrated in the following example:

> Alice is looking for an apartment. She regards price as more important than neighborhood. She believes that apartment $d_1$ has a low price but is in a bad neighborhood. She has *no information* about the price of apartment $d_2$ but believes it is in a good neighborhood.

In situations involving uncertainties, the “decision strategy” compares two options by prioritizing the most important criterion that each option is believed to satisfy. In this context, Alice would prefer $d_1$ over $d_2$ based on her beliefs.

However, if her beliefs change (e.g., if she learns that $d_2$ has a low price), her preference may shift so that she favors $d_2$ over $d_1$. This highlights the distinction between preference changes due to belief updates and those resulting from priority shifts, as in the previous examples.

In conclusion, priority dynamics and preference dynamics, though closely related, retain unique features, underscoring the value of modeling both intrinsic and reason-based preferences for a comprehensive understanding of agent decision-making.

## 6. *Ceteris paribus* preference and CP-nets

*Ceteris paribus* preference refers to a way of expressing preferences under the condition of “all else being equal”. It allows agents to state that one option is preferred over another while assuming that all other relevant factors remain constant. In AI systems for decision-making, a CP-net is a graphical model used to represent conditional preferences. It relies on the principle that comparisons between options are made under the assumption that other factors are unchanged, which aligns closely with the concept of *ceteris paribus*.

This section introduces results on the logic of *ceteris paribus* preferences along with the fundamentals of CP-nets.

### 6.1 Formalizing *ceteris paribus* preferences in logic

The core problem of *ceteris paribus* preference is how to interpret “all else being equal”. For example, one man may generally prefer red wine over white wine, *ceteris paribus*, but not if the red wine is poisonous and the white wine is not. So the challenge of formalizing a *ceteris paribus* proviso is how to determine whether the conditions are the same except for the color of the wine. This issue was discussed in the first studies of preference logic by Halldén (1957)[^halldén-1957] and von Wright (1963)[^wright-1963]. The difference between the equality reading of *ceteris paribus* and the normality reading “all else being normal” was also discussed by Van Benthem, Girard, and Roy (2009).

When interpreting the phrase “all else being equal”, a natural approach is to use equivalence classes of worlds. This approach has been taken by many researchers in the field. For instance, Doyle and Wellman (1994) defined context-dependent equivalence relations among individuals, which is called contextual equivalence. As a consequence, this means that the equivalence class may vary according to the context under consideration.

Formally, let $\Omega$ be a set of states, and let $\mathcal{E}(\Omega)$ denote the set of all equivalence relations on $\Omega$. The contextual equivalence is defined on a set $\Omega$ as a function *η*: $\mathcal{P}(\mathcal{P}(\Omega))\rightarrow\mathcal{E} (\Omega)$ assigning to each set of proposition $\{p, q, \ldots\}$ an equivalence relation $\eta(p, q, \ldots)$. For $w\,\eta(p,q,\ldots)\, w^{\prime}$ , we write $w\approx_{ mod\, p,q,\ldots} w^{\prime}$, meaning that with regard to $p, q, \ldots$, it is the case that *w* and $w^{\prime}$ are the same. Doyle and Wellman (1994) thus proposed dividing the space of possibilities into equivalence classes and ignoring comparison links that go across these classes.

Van Benthem, Girard, and Roy (2009) applied this idea to equivalence relations between possible worlds: truth-value equivalence for all relevant modal formulas in some specified set. In addition, they showed how this notion links up with von Wright’s work, and how it applies to game-theoretic solution concepts. They introduced new modalities of the form $\langle \Gamma \rangle\varphi$ into the language, formally defined as

$$p\mid \neg \varphi\mid \varphi\land \psi \mid\langle \Gamma \rangle^{>}\varphi\mid \langle \Gamma \rangle^{\geq}\varphi\mid \langle \Gamma \rangle\varphi,$$

where *Γ* is an arbitrary set of formulas. This way, “being equal” is part of the formal language itself. Semantically, *Γ* defines an equivalence class of possible worlds. For instance, $w \approx_{\Gamma} v$ indicates that *w* and *v* are equal w.r.t. *Γ*—they satisfy the same formulas in *Γ*.

A *ceteris paribus* preference model is a quadruple $\mathcal{M}$= $(W, \succeq, \trianglerighteq_{\Gamma}, V)$ where:

- *W* is a set of states, $\succeq$ is a binary preference relation, *V* is an evaluation
- $\trianglerighteq_{\Gamma}$ is the binary relation given by $w\trianglerighteq_{\Gamma}v$ iff $w\succeq v$ and $w \approx_{\Gamma} v$
- the strict subrelation $\trianglerighteq_{\Gamma}$ is defined by $w\succ v$ and $w \approx_{\Gamma} v$

The relation $\trianglerighteq_{\Gamma}$ is essentially an intersection of two relations over worlds: the basic preference relation and truth-value equivalence with respect to the formulas in *Γ*. The truth conditions for the new formulas that involve the equivalent classes are:

- $\mathcal{M}, w \models \langle \Gamma \rangle^{\geq}\varphi$  iff   $\exists v$ s.t. $v \trianglerighteq_{\Gamma} w$ and $\mathcal{M}, v\models \varphi$
- $\mathcal{M}, w \models \langle \Gamma \rangle^{>}\varphi$  iff   $\exists v$ s.t. $v \vartriangleright_{\Gamma} w$ and $\mathcal{M}, v\models \varphi$
- $\mathcal{M}, w \models \langle \Gamma \rangle\varphi$  iff   $\exists v$ s.t. $v \approx_{\Gamma} w$ and $\mathcal{M}, v\models \varphi$

For those cases where *Γ* is finite, Van Benthem, Girard, and Roy (2009) provide a complete axiomatization. For the features of *ceteris paribus*, the new set of axioms is found in Figure 8.

Reflexivity axioms for *ceteris paribus* sets where $\varphi\in\Gamma$:

1. $\langle \Gamma \rangle\varphi\rightarrow\varphi$
2. $\langle \Gamma \rangle\neg \varphi\rightarrow\neg\varphi$

Monotonicity axioms for *ceteris paribus* sets where $\Gamma \subseteq\Gamma^{\prime}$

1. $\langle \Gamma^{\prime} \rangle\varphi\rightarrow\langle \Gamma \rangle\varphi$
2. $\langle \Gamma^{\prime} \rangle^{\geq}\varphi\rightarrow\langle \Gamma \rangle\varphi$
3. $\langle \Gamma^{\prime} \rangle^{>}\varphi\rightarrow\langle \Gamma \rangle\varphi$

Axioms characterizing the changes to the *ceteris paribus* sets:

1. $\pm\varphi\land \langle \Gamma \rangle(\alpha\land \pm \varphi)\rightarrow\langle \Gamma \cup\{\varphi\} \rangle\alpha$
2. $\pm\varphi\land \langle \Gamma \rangle^{\geq}(\alpha\land \pm \varphi)\rightarrow\langle \Gamma \cup\{\varphi\} \rangle^{\geq}\alpha$
3. $\pm\varphi\land \langle \Gamma \rangle^{>}(\alpha\land \pm \varphi)\rightarrow\langle \Gamma \cup\{\varphi\} \rangle^{>}\alpha$

\*Figure 8:\* Axiomatization of *ceteris paribus* preferences by Van Benthem, Girard, and Roy (2009)

In the full language, *Γ* in modalities $\langle\Gamma\rangle\varphi$ can be of an arbitrary size. The follow-up work of Seligman and Girard (2011) presents an axiomatization of part of the full logic, the set of what is called “flexible” validities, and provides an alternative semantics in which all validities are flexible and so completely axiomatized. The axiomatization of infinite arbitrary sets is still an open problem.

### 6.2 Computational models of ceteris paribus preferences

CP-nets, short for “conditional preference networks”, essentially embody the concept of *ceteris paribus*, which is the core principle underlying how the networks represent preferences. This section introduces the basics of CP-nets, highlighting their compact, intuitive, and structured way of representing agent preferences under the *ceteris paribus* assumption (all else being equal).

A conditional preference network (CP-net) is a graphical model defined as follows.

Let $V = \{X_1, X_2, \ldots, X_n\}$ be a set of variables where each $X_i$ has a finite domain $\text{Dom}(X_i)$ of possible values. There is a directed graph *G* where:

- each variable $X_i$ corresponds to a node.
- the parents of $X_i$, denoted as $\text{Pa}(X_i)$, are nodes with edges directed towards $X_i$. These parents represent the variables that influence the preferences over $X_i$. An edge from $X_i$ to $X_j$ means that the preferences for $X_j$ depend on the value of $X_i$.

Instead of listing preferences for all possible outcomes (which grows exponentially with the number of variables), CP-nets use conditional preference tables (CPTs) to capture only relevant dependencies (i.e., the elements that the preference depends on). Each node $X_i$ is annotated with a CPT that specifies a total order $\succ_{u}$ over $\text{Dom}(X_i)$ for every possible instantiation *u* of $\text{Pa}(X_i)$. For example:

> if $\text{Pa}(X_i) = \{A, B\},$ then the CPT of $X_i$ specifies preferences for all combinations of *A* and *B*.

The semantics of CP-nets describe how preferences over outcomes are derived based on the structure of each network and the conditional preference tables.

An *outcome* is a complete assignment of values to all variables in the CP-net. For example, if $V = \{X_1, X_2, X_3\}$ and the domains are

$$\text{Dom}(X_1) = \{a_1, a_2\}, \quad \text{Dom}(X_2) = \{b_1, b_2\}, \quad \text{Dom}(X_3) = \{c_1, c_2\},$$

then one outcome would be $o = \{X_1 = a_1, X_2 = b_2, X_3 = c_1\}$.

Following the *ceteris paribus* assumption, which means comparing outcomes while keeping all other variables constant, if we respect the conditional preferences specified in the CPTs of each variable, we can get preferences over outcomes.

For example, if the CPT for $X_2$ specifies that $b_1 \succ b_2$ given $X_1 = a_1$, then:

$$\begin{align*} \text{if } &o_1 = \{X_1 = a_1, X_2 = b_1, X_3 = c_1\} \text{ and }\\ &o_2 = \{X_1 = a_1, X_2 = b_2, X_3 = c_1\}, \text{then } o_1 \succ o_2.\\ \end{align*}$$

An algorithm can be designed to efficiently find the optimal outcome in a CP-net—see the work of Boutilier, Brafman, and others (2004); Wilson (2004)[^wilson-2004]; and Goldsmith, Lang, and others (2008).

By capturing only relevant conditional preferences, CP-nets avoid combinatorial explosion from enumerating preferences over all possible outcomes. CP-nets have demonstrated significant value in AI-driven decision-making with applications in areas such as recommendation systems and product configuration. They have attracted considerable attention in the fields of computer science and artificial intelligence, as highlighted in the more recent work of Allen (2015)[^allen-2015] and Cai, Zhan, and Jiang (2023), among others.

## 7. Preference across research fields

### 7.1 Preference and conditional logics

It is well known that there has been a strong relationship between preference logics $p\geq^{\forall\exists}q$ and conditional logics since the end of the 1960s and the early 1970s (Lewis 1973)[^lewis-1973], as some of them are interdefinable.

For example, if I prefer fish over meat, and I prefer meat over vegetarian food, and I am in a steakhouse where they offer only steak or salad, then in that context, I prefer steak. Such reasoning about preferences and facts relates preference reasoning to conditional reasoning.

In possible world semantics, this can be explained from the fact that models of conditional logic are also preference structures. However, these preference logics developed as counterparts of conditional and deontic logics in the late 1960s and early 1970s, and they were rather different from the preference logics developed in the decade before by Halldén and von Wright.

If we write $\varphi\Rightarrow \psi$ for the conditional “if *φ* then *ψ*”, then under suitable conditions, we can define that *φ* is preferred to *ψ* if $\varphi\lor \psi$ implies *φ* and not *ψ*:

$$\varphi\geq^{\forall\exists} \psi :=\neg ((\varphi\lor \psi)\Rightarrow \neg \varphi).$$

Then we also have that the conditional “if *φ* then *ψ*” is defined as a preference of $\varphi\land \psi$ over $\varphi\land \neg \psi$:

$$\varphi\Rightarrow \psi := (\psi\land \varphi)>^{\forall\exists}(\neg \psi\land \varphi).$$

Conditional logics were more popular due to the frequent use of conditionals in natural language. We may say that some preference logics became known in the literature as conditional logics and others as deontic logics. However, it does not follow from this result that preference and conditional logics are the same thing. In general, the relationship between conditionals and comparatives is only partially understood (Makinson 1993)[^makinson-1993].

### 7.2 Preference and deontic logics

Traditional deontic logic often uses possible world semantics to interpret notions like obligation and permission, with the worlds ordered by a preference relation that ranks them by ideality. Deontic formulas are evaluated in the context of the current world based on their accessibility to these ideal worlds: an action is obligatory if it occurs in all the most preferred worlds accessible from the current world. The intricate relationship between better worlds and the best worlds has been extensively examined by Parent (2014)[^parent-2014] and Grossi, Van der Hoek, and Kuijer (2022). This ordering reflects intuitive deontic principles, but it struggles with conflicts and dilemmas because a single ordering may not fully capture multiple, potentially incompatible imperatives.

Makinson (1999)[^makinson-1999] emphasized the distinction between norms (imperatives without truth values) and deontic propositions (statements about obligations or permissions that can be true or false). He argued that this distinction has been overlooked in contemporary deontic logic and called for a “reconstruction” of deontic logic as a system grounded in explicit imperatives rather than abstract truth conditions. In his 2012 book, Horty made a notable contribution when he proposed a framework for understanding the reasons behind actions which employed default logic as its foundational structure. He elucidated how multiple reasons interact—supporting, overriding, or conflicting with one another—to determine what individuals ought to do.

These concerns with reasons led to the development of imperative-based semantics in deontic logic, which defines deontic operators in relation to explicit sets of imperatives. Standard deontic systems (e.g., monadic and dyadic systems) have been adapted to fit this model, with extensions for handling priority conflicts and dilemmas between imperatives. A two-layer structure has also been adopted for deontic logic. Notable works include those of Hansen (2008, 2014)[^hansen-2008][^hansen-2014]; Van Benthem, Grossi, and Liu (2014); and Benzmüller, Parent, and Van der Torre (2020).

### 7.3 Preference in decision theory and game theory

In decision theory and game theory, the notions of “preference” and “preference relation” are used to model choices, often with a behavioral interpretation. The formal properties of preference relations and their representation through utility functions have been studied extensively in the literature, some of which even predates preference logic. This entry primarily emphasizes the qualitative approach to preferences, which focuses on the formal properties of preference relations. By contrast, the quantitative approach typically relies on utility functions to represent preferences numerically. Decision-making under uncertainty is commonly modeled using an expected value framework, which combines the agent’s beliefs (expressed as probabilities) with utilities to capture preferences. Critical research has reexamined the foundations of preference theory. For example, Hausman (2012)[^hausman-2012] distinguishes between notions of preference as choice, welfare, and value, raising questions about whether utility functions can adequately capture well-being—especially when qualitative factors shape individual preferences. Fu (2020) proposes a novel approach that integrates both qualitative and quantitative methods to more accurately reflect the complexities of real-world decision-making. To connect this entry with decision theory, it is crucial to consider the numerical, quantitative representations of reason-based preferences derived from the richer two-layer structures presented in Section 4.

### 7.4 Preference in social choice theory

In social choice theory, the core issue is how to aggregate individual preferences into a coherent group preference. One well-known result in this area is Arrow’s (1951)[^arrow-1951] impossibility theorem, which demonstrates the limitations of creating a fair aggregation rule that meets certain desirable conditions. Further research has explored alternative assumptions, leading to new results. For instance, Andréka, Ryan, and Schobbens (2002) use graphs to represent alternative orderings of options as a method for aggregating individual preferences. List (2022)[^list-2022] (in the entry on social choice theory) provides a useful survey on this topic. In social settings, individual preferences are often not fully independent and are influenced by the views of peers. As a community, it is intriguing to consider how social preferences evolve over time and whether stable preferences can emerge. Seligman, Liu, and Girard (2011) and Liang and Seligman (2011)[^seligman-2011][^seligman-2011-2] discuss logic research on this topic. This area of study requires an exploration of community structures, mechanisms for updating individual preferences, and methods for defining social preferences. Related insights can be drawn from works on social belief, such as that of Shi (2021)[^shi-2021][^shi-2021-2]. A similar issue is investigated in evolutionary game theory, particularly in the so-called “indirect evolutionary approach” to social preference. For example, Bowles and Gintis (2011) explore how prosocial preferences such as altruism, fairness and cooperation can evolve and achieve stability.

## 8. Conclusions

Preference logic provides a versatile framework for understanding how agents compare situations and make decisions. This entry has reviewed key developments in the field, tracing its evolution from syntactic and algorithmic approaches to semantic frameworks. It has also highlighted recent research on two-layer structures, which stem from the distinction between intrinsic and extrinsic preferences, emphasizing the role of reasons in shaping preferences.

The study of preference change and the concept of *ceteris paribus* preference highlight the dynamic and practical aspects of preference logic, particularly in decision-making contexts. These frameworks will remain a foundation for addressing future challenges and advancing research in the field.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=logic-preference). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/logic-preference/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=logic-preference&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/logic-preference/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

[Please contact the author with suggestions.]

## Related Entries

logic: dynamic epistemic | logic: modal | logic: of belief revision | preferences | social choice theory

[^allen-2015]: Allen, Thomas E., 2015, “CP-Nets: From Theory to Practice”, in *Algorithmic Decision Theory* (Lecture Notes in Computer Science 9346), Toby Walsh (ed.), Cham: Springer, 555–560.

[^andréka-2002]: Andréka, Hajnal, Michael Ryan, and Philippe-Yves Schobbens, 2002, “Operators and Laws for Combining Preferential Relations”, *Journal of Logic and Computation*, 12(1): 13–53. doi:10.1093/logcom/12.1.13

[^arrow-1951]: Arrow, Kenneth J., 1951, *Social Choice and Individual Values* (Yale University. Cowles Foundation for Research in Economics 12), New York: John Wiley & Sons.

[^benzmüller-2020]: Benzmüller, Christoph, Xavier Parent, and Leendert W. N. van der Torre, 2020, “Designing Normative Theories for Ethical and Legal Reasoning: LogiKEy Framework, Methodology, and Tool Support”, *Artificial Intelligence*, 287: 103348. doi:10.1016/J.ARTINT.2020.103348

[^boutilier-1990]: Boutilier, Craig, 1990, “Conditional Logics of Normality as Modal Systems”, in *Proceedings of the Eighth National Conference on Artificial Intelligence (AAAI’90)*, volume 1, Menlo Park, CA: AAAI Press, 594–599.

[^boutilier-1992]: –––, 1992, *Toward a Logic for Qualitative Decision Theory*, Ph.D. thesis, University of Toronto.

[^boutilier-2004]: Boutilier, Craig, Ronen I. Brafman, Carmel Domshlak, Holger H. Hoos, and David Poole, 2004, “CP-Nets: A Tool for Representing and Reasoning with Conditional Ceteris Paribus Preference Statements”, *Journal of Artificial Intelligence Research*, 21: 135–191. doi:10.1613/jair.1234

[^bowles-2011]: Bowles, Samuel and Herbert Gintis, 2011, *A Cooperative Species: Human Reciprocity and Its Evolution*, Princeton/Oxford: Princeton University Press.

[^bradley-2007]: Bradley, Richard, 2007, “The Kinematics of Belief and Desire”, *Synthese*, 156(3): 513–535. doi:10.1007/s11229-006-9136-7

[^cai-2023]: Cai, Jianlong, Jieyu Zhan, and Yuncheng Jiang, 2023, “CP-Nets-Based User Preference Learning in Automated Negotiation through Completion and Correction”, *Knowledge and Information Systems*, 65(9): 3567–3590. doi:10.1007/s10115-023-01872-z

[^chen-2024]: Chen, Qian, Chenwei Shi, and Yiyan Wang, 2024, “Reasoning about Dependence, Preference and Coalitional Power”, *Journal of Philosophical Logic*, 53(1): 99–130. doi:10.1007/s10992-023-09727-2

[^chisholm-1966]: Chisholm, Roderick M. and Ernest Sosa, 1966, “On the Logic of ‘Intrinsically Better’”, *American Philosophical Quarterly*, 3(3): 244–249.

[^christoff-2022]: Christoff, Zoé, Norbert Gratzl, and Olivier Roy, 2022, “Priority Merge and Intersection Modalities”, *The Review of Symbolic Logic*, 15(1): 165–196. doi:10.1017/s1755020321000058

[^de-2009]: De Jongh, Dick and Fenrong Liu, 2009, “Preference, Priorities and Belief”, in Grüne-Yanoff and Hansson 2009: 85–107. doi:10.1007/978-90-481-2593-7_4

[^dietrich-2013a]: Dietrich, Franz and Christian List, 2013a, “A Reason-Based Theory of Rational Choice”, *Noûs*, 47(1): 104–134. doi:10.1111/j.1468-0068.2011.00840.x [[Dietrich and List 2013a preprint available online](https://eprints.lse.ac.uk/46930/)]

[^dietrich-2013b]: –––, 2013b, “Where Do Preferences Come From?”, *International Journal of Game Theory*, 42(3): 613–637. doi:10.1007/s00182-012-0333-y

[^doyle-1994]: Doyle, Jon and Michael P. Wellman, 1994, “Representing Preferences as *Ceteris Paribus* Comparatives”, in *Papers from the 1994 AAAI Spring Symposium: Decision-Theoretic Planning* (AAAI Technical Report, SS-94-06), Association for the Advancement of Artificial Intelligence, 69–75.

[^fu-2020]: Fu, Xiaoxuan, 2020, “Preference Lifting under Uncertainty”, Ph.D. thesis, Department of Philosophy, Tsinghua University.

[^girard-2008]: Girard, Patrick, 2008, *Modal Logics for Belief and Preference Change*, Ph.D. thesis, Stanford University.

[^goldsmith-2008]: Goldsmith, Judy, Jérôme Lang, Miroslaw Truszczynski, and Nic Wilson, 2008, “The Computational Complexity of Dominance and Consistency in CP-Nets”, *Journal of Artificial Intelligence Research*, 33: 403–432. doi:10.1613/JAIR.2627

[^grossi-2022]: Grossi, Davide, Wiebe van der Hoek, and Louwe B. Kuijer, 2022, “Reasoning about General Preference Relations”, *Artificial Intelligence*, 313: 103793. doi:10.1016/j.artint.2022.103793

[^grüne-yanoff-2009]: Grüne-Yanoff, Till and Sven Ove Hansson (eds), 2009, *Preference Change: Approaches from Philosophy, Economics and Psychology* (Theory and Decision Library. Series A, Philosophy and Methodology of the Social Sciences, 42), Dordrecht/London: Springer. doi:10.1007/978-90-481-2593-7

[^halldén-1957]: Halldén, Sören, 1957, *On the Logic of “Better”* (Library of Theoria 2), Lund: C.W.K. Gleerup.

[^halpern-1997]: Halpern, Joseph Y., 1997, “Defining Relative Likelihood in Partially-Ordered Preferential Structures”, *Journal of Artificial Intelligence Research*, 7: 1–24. doi:10.1613/jair.391

[^hansen-2008]: Hansen, Jörg, 2008, *Imperatives and Deontic Logic*, Ph.D. dissertation, Konstanz, Germany: University of Konstanz.

[^hansen-2014]: –––, 2014, “Reasoning about Permission and Obligation”, in *David Makinson on Classical Methods for Non-Classical Problems* (Outstanding Contributions to Logic 5), Sven Ove Hansson and David Makinson (eds), Dordrecht: Springer, 255–280. doi:10.1007/978-94-007-7759-0_14

[^hansson-1969]: Hansson, Bengt, 1969, “An Analysis of Some Deontic Logics”, *Noûs*, 3(4): 373–398. doi:10.2307/2214372

[^hansson-1995]: Hansson, Sven Ove, 1995, “Changes in Preference”, *Theory and Decision*, 38(1): 1–28. doi:10.1007/bf01083166

[^hansson-2001]: –––, 2001, “Preference Logic”, in *Handbook of Philosophical Logic*, Dov M. Gabbay and Franz Guenthner (eds), second edition, Dordrecht: Kluwer, 319–393. doi:10.1007/978-94-017-0456-4_4

[^harel-2000]: Harel, David, Dexter Kozen, and Jerzy Tiuryn, 2000, *Dynamic Logic*, Cambridge, MA: MIT Press. doi:10.7551/mitpress/2516.001.0001

[^hausman-2012]: Hausman, Daniel M., 2012, *Preference, Value, Choice, and Welfare*, Cambridge/New York: Cambridge University Press. doi:10.1017/cbo9781139058537

[^horty-2012]: Horty, John Francis, 2012, *Reasons as Defaults*, Oxford/New York: Oxford University Press. doi:10.1093/acprof:oso/9780199744077.001.0001

[^kratzer-1981]: Kratzer, Angelika, 1981, “Partition and Revision: The Semantics of Counterfactuals”, *Journal of Philosophical Logic*, 10(2): 201–216. doi:10.1007/bf00248849

[^lamarre-1991]: Lamarre, Philippe, 1991, “S4 as the Conditional Logic of Nonmonotonicity”, in *Proceedings of the Second International Conference on Principles of Knowledge Representation and Reasoning (KR’91)*, James F. Allen, Richard Fikes, and Erik Sandewall (eds), San Francisco, CA: Morgan Kaufmann, 357–367.

[^lang-2008]: Lang, Jérôme and Leendert van der Torre, 2008, “From Belief Change to Preference Change”, in *Proceedings of the 18th European Conference on Artificial Intelligence (ECAI-2008)* (Frontiers in Artificial Intelligence and Applications 178), Malik Ghallab, Constantine D. Spyropoulos, Nikos Fakotakis, Nikos Avouris (eds), IOS Press, 351–355. doi:10.3233/978-1-58603-891-5-351

[^lewis-1973]: Lewis, David, 1973, *Counterfactuals*, Oxford: Basil Blackwell.

[^liang-2011]: Liang Zhen and Jeremy Seligman, 2011, “A Logical Model of the Dynamics of Peer Pressure”, *Electronic Notes in Theoretical Computer Science*, 278: 275–288. doi:10.1016/j.entcs.2011.10.021

[^list-2022]: List, Christian, 2022, “Social Choice Theory”, in *The Stanford Encyclopedia of Philosophy* (Winter 2022), Edward N. Zalta and Uri Nodelman (eds), URL = <[https://plato.stanford.edu/archives/win2022/entries/social-choice/](https://plato.stanford.edu/archives/win2022/entries/social-choice/)>. First published 2013.

[^liu-2008]: Liu, Fenrong, 2008, *Changing for the Better: Preference Dynamics and Agent Diversity*, Ph.D. thesis, ILLC, University of Amsterdam.

[^liu-2010]: –––, 2010, “Von Wright’s ‘The Logic of Preference’ Revisited”, *Synthese*, 175(1): 69–88. doi:10.1007/s11229-009-9530-z

[^liu-2011a]: –––, 2011a, “A Two-Level Perspective on Preference”, *Journal of Philosophical Logic*, 40(3): 421–439. doi:10.1007/s10992-010-9168-9

[^liu-2011b]: –––, 2011b, *Reasoning about Preference Dynamics* (Synthese Library 354), Berlin: Springerd. doi:10.1007/978-94-007-1344-4

[^makinson-1993]: Makinson David, 1993, “Five Faces of Minimality”, *Studia Logica*, 52(3): 339–379, doi:10.1007/bf01057652

[^makinson-1999]: –––, 1999, “On a Fundamental Problem of Deontic Logic”, in *Norms, Logics and Information Systems. New Studies on Deontic Logic and Computer Science*, Paul McNamara and Henry Prakken (eds), Amsterdam: IOS Press, 29–53.

[^menger-1939]: Menger, Karl, 1939, “A Logic of the Doubtful. On Optative and Imperative Logic”, *Reports of a Mathematical Colloquium*, Notre Dame, IN, series 2, 1: 53–64.

[^osherson-2012]: Osherson, Daniel and Scott Weinstein, 2012, “Preference Based on Reasons”, *The Review of Symbolic Logic*, 5(1): 122–147. doi:10.1017/s1755020311000244

[^parent-2014]: Parent, Xavier, 2014, “Maximality vs. Optimality in Dyadic Deontic Logic”, *Journal of Philosophical Logic*, 43(6): 1101–1128. doi:10.1007/s10992-013-9308-0

[^pettit-2002]: Pettit, Philip, 2002, *Rules, Reasons, and Norms: Selected Essays*, Oxford/New York: Oxford University Press. doi:10.1093/0199251878.001.0001

[^rescher-1966]: Rescher, Nicholas, 1966, *The Logic of Commands* (Monographs in Modern Logic), London: Routledge & K. Paul.

[^rescher-1967]: –––, 1967, “Semantic Foundations for the Logic of Preference”, in *The Logic of Decision and Action*, Nicholas Rescher (ed.), Pittsburgh: University of Pittsburgh Press, 37–62.

[^savage-1954]: Savage, Leonard J., 1954, *The Foundations of Statistics* (Wiley Publications in Statistics), New York: Wiley.

[^seligman-2011]: Seligman, Jeremy and Patrick Girard, 2011, “Flexibility in Ceteris Paribus Reasoning”, *The Australasian Journal of Logic*, 10: 67–99. doi:10.26686/ajl.v10i0.1826

[^seligman-2011-2]: Seligman, Jeremy, Fenrong Liu, and Patrick Girard, 2011, “Logic in the Community”, in *Logic and Its Applications: Fourth Indian Conference (ICLA 2011)* (Lecture Notes in Computer Science 6521), Mohua Banerjee and Anil Seth (eds.), Berlin/Heidelberg: Springer, 178–188. doi:10.1007/978-3-642-18026-2_15

[^shi-2021]: Shi, Chenwei, 2021, “Collective Opinion as Tendency Towards Consensus”, *Journal of Philosophical Logic*, 50(3): 593–613. doi:10.1007/s10992-020-09579-0

[^shi-2021-2]: Shi, Chenwei and Yang Sun, 2021, “Logic of Convex Order”, *Studia Logica*, 109(5): 1019–1047. doi:10.1007/s11225-020-09940-z

[^spohn-1988]: Spohn, Wolfgang, 1988, “Ordinal Conditional Functions: A Dynamic Theory of Epistemic States”, in *Causation in Decision, Belief Change, and Statistics*, William L. Harper and Brian Skyrms (eds), Dordrecht: Kluwer, 105–134. doi:10.1007/978-94-009-2865-7_6

[^tan-1996]: Tan, Yao-Hua and Leendert W. N. van der Torre, 1996, “How to Combine Ordering and Minimizing in a Deontic Logic Based on Preferences”, in *Deontic Logic, Agency and Normative Systems: Third International Workshop on Deontic Logic in Computer Science (DEON ’96)*, Mark A. Brown and José Carmo (eds), London: Springer London, 216–232. doi:10.1007/978-1-4471-1488-8_12

[^thomason-1996]: Thomason, Richmond H. and John F. Horty, 1996, “Nondeterministic Action and Dominance: Foundations for Planning and Qualitative Decision”, in *Proceedings of the 6th Conference on Theoretical Aspects of Rationality and Knowledge (TARK ’96)*, Yoav Shoham (ed.), San Francisco, CA: Morgan Kaufmann, 229–250.

[^van-2009]: Van Benthem, Johan, Patrick Girard, and Olivier Roy, 2009, “Everything Else Being Equal: A Modal Logic for *Ceteris Paribus* Preferences”, *Journal of Philosophical Logic*, 38(1): 83–125. doi:10.1007/s10992-008-9085-3

[^van-2010]: Van Benthem, Johan, Davide Grossi, and Fenrong Liu, 2010, “Deontics = Betterness + Priority”, in *Deontic Logic in Computer Science: 10th International Conference (DEON 2010)* (Lecture Notes in Computer Science 6181), Guido Governatori and Giovanni Sartor (eds), Berlin/Heidelberg: Springer, 50–65. doi:10.1007/978-3-642-14183-6_6

[^van-2014]: –––, 2014, “Priority Structures in Deontic Logic”, *Theoria*, 80(2): 116–152. doi:10.1111/theo.12028

[^van-2007]: Van Benthem, Johan and Fenrong Liu, 2007, “Dynamic Logic of Preference Upgrade”, *Journal of Applied Non-Classical Logics*, 17(2): 157–182. doi:10.3166/jancl.17.157-182

[^van-1974]: Van Dalen, Dirk, 1974, “Variants of Rescher’s Semantics for Preference Logic and Some Completeness Theorems”, *Studia Logica*, 33(2): 163–181. doi:10.1007/BF02120492

[^van-1973]: Van Fraassen, Bas C., 1973, “Values and the Heart’s Command”, *The Journal of Philosophy*, 70(1): 5–19. doi:10.2307/2024762

[^wright-1963]: von Wright, Georg Henrik, 1963, *The Logic of Preference*, Edinburgh: Edinburgh University Press.

[^wilson-2004]: Wilson, Nic, 2004, “Extending CP-Nets with Stronger Conditional Preference Statements”, in *Proceedings of the 19th National Conference on Artificial Intelligence (AAAI’04)*, Deborah L. McGuinness and George Ferguson (eds), San Jose, CA: AAAI Press, 735–741. [[Wilson 2004 available online](https://aaai.org/papers/00735-AAAI04-116-extending-cp-nets-with-stronger-conditional-preference-statements/)]

[^xie-2024]: Xie, Kaibo and Jialiang Yan, 2024, “A Logic for Desire Based on Causal Inference”, *Journal of Logic and Computation*, 34(2): 352–371. doi:10.1093/logcom/exac060
