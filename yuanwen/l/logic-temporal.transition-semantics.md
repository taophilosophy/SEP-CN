# logic-temporal — transition-semantics（supplement）

> （《logic-temporal》词条补充材料，源：plato.stanford.edu/entries/logic-temporal/transition-semantics.html）

#### Supplement to Temporal Logic

## Supplement: Transition Semantics

Transition semantics, introduced in Rumberg (2016), defines a branching time temporal logic in which possible courses of events are modeled by chains of transitions rather than histories. Whereas histories represent complete possible courses of events, sets of transitions can represent incomplete possible courses of events as well, which can then be extended towards the future, thereby enabling a dynamic picture of the interrelation of actuality, possibility, and time (for an intuitive introduction to transition semantics along these lines, see Rumberg 2019).

The notion of a *transition* employed here generalizes the notion of a transition prevalent in computer science. Intuitively, a transition captures one of the immediate future possibilities at a branching point in a tree $\mathcal{T} = \langle T,\prec\rangle$ and is formally defined as a pair $\langle t,H\rangle$ consisting of a branching point $t\in T$ and a set $H \subseteq \mathcal{H}(t)$ of locally undivided histories (where two histories $h,h'\in \mathcal{H}(t)$ are said to be undivided at $t$ iff there is some time instant $t' \in h \cap h'$ such that $t\prec t'$). A backward-linear strict partial ordering between transitions is defined ($\langle t,H\rangle$ precedes $\langle t',H'\rangle$ iff $t\prec t'$ and $H'\subset H$), and a *possible course of events* $C$ is taken to be a possibly non-maximal, downward-closed chain in that ordering. To every possible course of events $C$, there naturally corresponds a non-empty set of histories, namely, the *set of histories allowed by $C$*, defined by $\mathcal{H}(C) := \bigcap_{\langle t,H\rangle\in C} H$.

The transition language contains, in addition to temporal and modal operators, a so-called stability operator $S$, which is interpreted as a universal quantifier over the possible future extensions of the relevant transition set. Given a set of atomic propositions ${PROP}$, the set of formulae of the transition language can be recursively defined as follows:

$$\varphi := p \in {PROP} \mid \neg\varphi \mid (\varphi \wedge \varphi) \mid P\varphi \mid F\varphi \mid G\varphi \mid \Diamond\varphi \mid S\varphi.$$

In transition semantics, these formulae will be evaluated in a model on a tree $\mathcal{T} = \langle T,\prec\rangle$ at pairs $(t,C)$ consisting of a time instant $t\in T$ and a possible course of events $C$ compatible with that instant, i.e. $\mathcal{H}(C) \cap \mathcal{H}(t) \neq \emptyset$. A *transition tree model* is a triple $\mathcal{M} = \langle T,\prec,V\rangle$ where $\mathcal{T} = \langle T,\prec\rangle$ is a tree and $V$ is a valuation that assigns to every atomic proposition $p \in {PROP}$ the set of admissible pairs $(t,C)$ at which $p$ is considered true. The *truth of an arbitrary formula φ at a pair $(t,C)$ in a transition tree model $\mathcal{M}$* is defined inductively as follows:

- $\mathcal{M},(t,C) \vDash p$   iff   $(t,C) \in V(p)$, for $p\in {PROP}$;
- $\mathcal{M},(t,C) \vDash \neg\varphi$   iff   $\mathcal{M},(t,C)\not\vDash\varphi$;
- $\mathcal{M},(t,C) \vDash \varphi \wedge \psi$   iff   $\mathcal{M},(t,C) \vDash \varphi$ and $\mathcal{M},(t,C) \vDash \psi$;
- $\mathcal{M},(t,C) \vDash P\varphi$   iff   $\mathcal{M},(t',C) \vDash\varphi$ for some time instant $t'$ such that $t'\prec t$;
- $\mathcal{M},(t,C) \vDash F\varphi$   iff   for all histories $h\in \mathcal{H}(C) \cap \mathcal{H}(t)$, there is some time instant $t' \in h$ such that $t \prec t'$ and $\mathcal{M},(t',C) \vDash \varphi$;
- $\mathcal{M},(t,C) \vDash G\varphi$   iff   for all histories $h\in \mathcal{H}(C) \cap \mathcal{H}(t)$ and for all time instants $t' \in h$ such that $t \prec t'$, $\mathcal{M},(t',C) \vDash \varphi$;
- $\mathcal{M},(t,C) \vDash \Diamond\varphi$   iff   $\mathcal{M},(t,C') \vDash \varphi$ for some possible course of events $C'$ such that $\mathcal{H}(C') \cap \mathcal{H}(t) \neq \emptyset$;
- $\mathcal{M},(t,C) \vDash S\varphi$   iff   $\mathcal{M},(t,C') \vDash \varphi$ for all possible courses of events $C' \supseteq C$ such that $\mathcal{H}(C') \cap \mathcal{H}(t) \neq \emptyset$.

Thus, a formula of the form $F\varphi$ is true at an instant $t$ with respect to a possible course of events $C$ iff every history that passes through $t$ and is allowed by $C$ contains some later instant $t'$ at which *φ* is true relative to $C$. The truth values of formulae about the future at an instant can change under extensions of the given transition set, and the stability operator $S$ captures this behavior. A formula *φ* is said to be *stably true* (*stably false*) at $(t,C)$ if it remains true (false) at $t$ with respect to all possible extensions of $C$. Formulae that are neither stably true nor stably false are *contingent*.

A formula of the transition language is *valid* iff it is true at all admissible pairs $(t,C)$ in all transition tree models. While transition semantics validates the principle of excluded middle $\varphi \vee \neg \varphi$, it invalidates the principle of future excluded middle $F\varphi \vee F\neg\varphi$. However, the latter disjunction can be false only contingently: the scheme $\neg S\neg (F\varphi \vee F\neg\varphi)$ is generally valid.

The Peircean and the Ockhamist branching time temporal logics can be obtained as limiting cases by restricting the range of admissible courses of events to the empty set of transitions and maximal chains, respectively. To spell this out formally, we need to equip trees $\mathcal{T} = \langle T,\prec\rangle$ with a primitive set of transition sets $\mathit{TS}$ such that every time instant in $\mathcal{T}$ belongs to a history allowed by some set of transitions in $\mathit{TS}$. Peirceanism amounts to the case where $\mathit{TS} = \{\emptyset\}$, whereas Ockhamism results if $\mathit{TS} = \{C\mid C \text{ is maximal linear}\}$. The corresponding classes of frames are definable by the formulae $\varphi \leftrightarrow \Box \varphi$ and $F\varphi \vee F\neg\varphi$, respectively.

Transition semantics makes use of a second, defined parameter of truth, and the transition sets employed as that second parameter are set-theoretically rather complex. In Rumberg and Zanardo (2019), it is shown that the set-theoretic complexity can be evaded: based on a one-to-one correspondence between transition sets and certain tree substructures, called *prunings*, a class of first-order definable Kripke structures is provided that preserves validity, which naturally leads to axiomatizability results.
