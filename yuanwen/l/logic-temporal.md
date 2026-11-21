# Temporal Logic
**First published Mon Nov 29, 1999; substantive revision Fri May 3, 2024**

*Goranko, Valentin, Rumberg, Antje*

Broadly construed, *Temporal Logic* covers all formal approaches to representing and reasoning about time and temporal information. More narrowly, it usually refers to the modal-logic style approach introduced by Arthur Prior in the 1950s under the name *Tense Logic* and subsequently developed further by many logicians and computer scientists. Temporal Logic has been widely used as a formalism for clarifying philosophical issues about time, as a framework for defining the semantics of temporal expressions in natural language, as a language for encoding temporal knowledge in artificial intelligence, and as a tool for specification and verification of computer programs and systems.

Here we provide a broadly representative — yet concise and inevitably incomplete — overview of the rich variety of temporal models and logics introduced and studied over the past 70 years or so.

## 1. Temporal reasoning from antiquity to modern days

Discussions of temporality and reasoning about time go back to antiquity, and examples can even be found in the Bible (Boyd 2014)[^boyd-2014]. Zeno’s famous flying arrow paradox refers to the nature of time and challenges the notion of change. Much of the early temporal discussion, however, centered around the problem of *future contingents*, i.e. the question whether statements about future events that are neither necessary nor impossible can have definite truth values. The most widely known and probably most cited example is the sea-battle scenario discussed by Aristotle in *On Interpretation* (Chapter 9). Aristotle argued that statements such as “There will be a sea-battle tomorrow”, as well as the contrary prediction “There will not be a sea-battle tomorrow”, do not hold of necessity and hence lack definite truth values at present, while conceding that it is necessary that either there will be a sea-battle tomorrow or not. Somewhat later, the philosopher Diodorus Chronus demonstrated the problem of future contingents in his famous *Master Argument*, which led him to define the possible as “what is or will be the case”. A detailed discussion of Diodorus’ argument is provided in e.g. Rescher and Urquhart (1971, Chapter XVII) and the entry on future contingents.

Philosophical discussions concerning time and the contingency of the future continued in the Middle Ages, where the theme was taken up by writers such as Peter Aureole, William of Ockham, and Luis Molina. The central question here was how to reconcile God’s foreknowledge with the idea of human freedom. Ockham, for example, embraced the idea of a true or actual future, holding that future contingents are either true or false even though only God knows their truth values. According to Ockham, this is not to say, however, that future contingents are necessary: there are alternative possibilities for humans to choose from. Later, several philosophers and logicians engaged in the problem of relating time and modality, proposing various different solutions. C.S. Peirce objected to the idea that future contingents can have definite truth values. He advanced the view that only the present and the past are actual, whereas the future is the realm of possibility and necessity. In a similar spirit, J. Łukasiewicz devised a three-valued logic, treating the truth values of future contingents as undetermined. For a more recent philosophical discussion on the open future, indeterminism, and free will, see e.g. Belnap et al. (2001), Correia and Iacona (2013), and Müller (2014)[^müller-2014].

The modern era of formal temporal logic was initiated by the seminal work of Arthur N. Prior, with important precursors such as H. Reichenbach, J. Findlay, J. Łukasiewicz, and J. Łoś.[^note-1] From the early 1950s, Prior introduced and analyzed in detail over more than a decade several different versions of Tense Logic, many of which are discussed here. Prior’s invention of Tense Logic was largely driven by philosophical considerations. In particular, the Master Argument of Diodorus Chronus and the intricate relationship between time, (in)determinism, God’s foreknowledge, and human freedom played a pivotal role in his work. Prior was convinced that a proper logical approach could help to clarify and resolve such philosophical problems. He introduced temporal operators, studied metric tense logic, was a pioneer in hybrid logic, and devised two versions of branching time logic, which he took to reflect the views of Ockham and Peirce, respectively. His work paved the way for the development of the vast and diverse field of temporal logic, with numerous important applications not only in philosophy, but also in computer science, artificial intelligence, and linguistics. For more on Prior’s views and work, see the special issue Albretsen et al. (2016), the four volumes of the recent book series *Logic and Philosophy of Time* (Hasle et al. 2017; Blackburn et al. 2019; Jakobsen et al. 2020; Hasle et al. 2020)[^blackburn-2019][^hasle-2017][^hasle-2020][^jakobsen-2020]; and the entry on Arthur Prior. A comprehensive overview of the history of temporal reasoning and logics is provided in Øhrstrøm and Hasle (1995). See also Øhrstrøm and Hasle (2006) and Dyke and Bardon (2013, Part I).

## 2. Formal models of time

Philosophers have extensively discussed the ontological nature and properties of time. Several aspects of the debate are reflected in the rich variety of formal models of time as they have been explored in temporal logics. For example, is time instant-based or interval-based? Is it discrete, dense, or continuous? Does time have a beginning or an end? Is it linear, branching, or circular? Before we turn to the formal languages of temporal logics and their semantics, we briefly introduce below the two most basic types of formal models of time together with some of their pertinent properties: instant-based and interval-based models.

### 2.1 Instant-based models of time

In instant-based models, the primitive temporal entities are points in time, i.e. *time instants*, and the basic relationship between them is *temporal precedence*. Accordingly, the flow of time is represented by a non-empty set of time instants $T$ with a binary relation $\prec$ of precedence on it: $\mathcal{T} = \left\langle T, \prec \right\rangle.$

There are some basic properties which can naturally be imposed on instant-based flows of time. The temporal precedence relation $\prec$ is usually required to be a strict partial ordering, that is, an irreflexive, transitive, and hence asymmetric relation. In computer science, however, one often uses the reflexive closure $\preceq $ of the precedence relation, and then the asymmetry condition is replaced by antisymmetry. A list of key properties is provided below.

One fundamental distinction in the realm of instant-based models of time is the distinction between linear models, where the flow of time is depicted as a line, and backward-linear models, which allow for a tree-like representation, supporting the view that the past is fixed (and hence linear) while the future may be open (branching into multiple future possibilities). In either case, the temporal ordering may or may not contain minimal or maximal elements, corresponding to first or last instants in time, respectively.

Another important distinction is between discrete models of time, which are prevalent in computer science, and dense or continuous ones, which are more common in natural sciences and philosophy. In forward-discrete (resp. backward-discrete) models, each time instant that has a successor (resp. predecessor) has an immediate successor (resp. immediate predecessor). In dense models, by contrast, between any two subsequent time instants, there is another instant.

Many, but not all, properties that may be imposed on an instant-based model of time $\mathcal{T} = \left\langle T, \prec \right\rangle$ can be expressed by first-order sentences as follows (where $\preceq$ is an abbreviation of $x\prec y \lor x=y$):

- *reflexivity*: $\forall x (x\prec x);$
- *irreflexivity*: $\forall x\lnot (x\prec x);$
- *transitivity*: $\forall x\forall y\forall z(x\prec y\wedge y\prec z\rightarrow x\prec z);$
- *asymmetry*: $\forall x\forall y \lnot(x\prec y\wedge y\prec x);$
- *antisymmetry*: $\forall x\forall y(x\prec y\wedge y\prec x\rightarrow x=y);$
- *linearity (trichotomy)*: $\forall x\forall y(x=y\vee x\prec y\vee y\prec x);$
- *forward-linearity*: $\forall x\forall y\forall z(z\prec x\wedge z\prec y\rightarrow (x=y \vee x \prec y\vee y\prec x));$
- *backward-linearity*: $\forall x\forall y\forall z(x\prec z\wedge y\prec z\rightarrow (x=y \vee x \prec y\vee y\prec x));$
- *beginning*: $\exists x\lnot\exists y(y\prec x);$
- *end*: $\exists x\lnot\exists y(x\prec y);$
- *no beginning (backward-seriality)*: $\forall x\exists y(y\prec x);$
- *no end (forward-seriality, unboundedness)*: $\forall x\exists y(x\prec y);$
- *density*: $\forall x\forall y(x\prec y\rightarrow \exists z(x\prec z\wedge z\prec y));$
- *forward-discreteness*: $\forall x\forall y(x\prec y\rightarrow \exists z(x\prec z \wedge z\preceq y \wedge \lnot\exists u(x\prec u\wedge u\prec z)));$
- *backward-discreteness*: $\forall x\forall y(y\prec x\rightarrow \exists z(z\prec x \wedge y\preceq z \wedge \lnot\exists u(z\prec u\wedge u\prec x))).$

Note that, in linear models, the two discreteness conditions simplify to

- $\forall x\forall y(x\prec y\rightarrow \exists z(x\prec z \wedge \forall u(x\prec u \rightarrow z\preceq u)))$ and
- $\forall x\forall y(y\prec x\rightarrow \exists z(z\prec x \wedge \forall u(u\prec x \rightarrow u\preceq z))),$ respectively.

Key examples of properties that cannot be expressed by first-order sentences, but require a second-order language with quantification over sets, are *continuity*, *well-ordering*, the *finite interval property*, and *forward/backward induction*. Continuity demands that there be ‘no gaps’ in the temporal order. Not only must the temporal order be dense, it must also be *Dedekind complete* (i.e., every non-empty set of time instants that has an upper bound has a least upper bound). The ordering of the real numbers fulfills this condition, but the rational numbers do not. To see this, consider the set of all rational numbers whose square is less than 2 and note that $\sqrt{2}$ is not rational. An instant-based model of time is well-ordered if there are no infinite descending chains (i.e., every non-empty, linear set of time instants has a least element), and it has the finite interval property if between any two comparable time instants there are at most finitely many instants. The natural numbers are well-ordered and have the finite interval property, the integers are not well-ordered but have the finite interval property, and the rationals are neither well-ordered nor do they have the finite interval property. Lastly, a partial order is forward (resp. backward) inductive if there are ‘no transfinite forward (resp. backward) jumps’ (i.e., every infinite ascending (resp. descending) chain lacks a strict upper (resp. lower) bound). As we will see in Section 3.6, these second-order properties can be expressed in propositional temporal languages.

### 2.2 Interval-based models of time

In contrast to instant-based models of time, interval-based models rely on *time intervals*, i.e. periods rather than instants, as the primitive entities. They can, and have been, motivated by considerations concerning Zeno’s famous flying arrow paradox: If the flying arrow is always at an instant and if at each instant the arrow is at rest, then how is movement possible? By modelling the flight of the arrow as an event that occupies a temporal interval the paradox can arguably be avoided. Other examples that naturally invoke interval-based reasoning are: “Last night Alice cried a lot while writing the letter, and then she calmed down” and “Bill was drinking his tea when the postman came”.

Interval-based models usually presuppose linear time. But they are richer than instant-based models as there are more possible relationships between time intervals than between time instants. An interval-based model of time can, for instance, include the relations *temporal precedence* $\prec,$ *inclusion* $\sqsubseteq,$ and *overlap* $O$ over a given set of time intervals $T$: formally, $\mathcal{T}= \left\langle T,\prec,\sqsubseteq, O \right\rangle.$ Some natural properties of such interval-based relations include:

- *reflexivity of* $\sqsubseteq:$ $\forall x(x\sqsubseteq x);$
- *antisymmetry of* $\sqsubseteq:$ $\forall x\forall y(x\sqsubseteq y\wedge y\sqsubseteq x\rightarrow x=y);$
- *atomicity of* $\sqsubseteq$ (for discrete time): $\forall x\exists y(y\sqsubseteq x\wedge \forall z(z\sqsubseteq y\rightarrow z=y));$
- *downward monotonicity of $\prec$ w.r.t. $\sqsubseteq:$* $\forall x\forall y\forall z(x\prec y\wedge z\sqsubseteq x\rightarrow z\prec y);$
- *symmetry of* $O$: $\forall x\forall y(xOy\rightarrow yOx);$
- *overlapping intervals intersect in a subinterval*: $\forall x\forall y (xOy \rightarrow \exists z( z \sqsubseteq x \land z \sqsubseteq y \land \forall u ( u \sqsubseteq x \land u \sqsubseteq y \to u \sqsubseteq z)));$
- *monotonicity of $\sqsubseteq$ w.r.t. $O$:* $\forall x\forall y \forall z(x \sqsubseteq y \land xOz \rightarrow z \sqsubseteq y \lor zOy).$

In an influential early work on interval-based temporal ontology and reasoning in AI, Allen (1983)[^allen-1983] considered the family of all binary relations that can arise between two intervals in a linear order, subsequently called *Allen relations*. These 13 relations, displayed in Table 1, are mutually exclusive and jointly exhaustive, i.e., exactly one of them holds between any given pair of strict intervals (excluding point-intervals). Moreover, they turn out to be definable in terms of only two of them, viz. in terms of ‘meets’ and ‘met-by’ (Allen 1983)[^allen-1983].

| Interval relations | Allen’s notation | $\textsf{HS}$ notation |
| --- | --- | --- |
| ┣━━┫ | *equals* $\{=\}$ |   |
| ├──┤ ┣┫ | *before* $\{\lt\}$ / *after* $\{\gt\}$ | $\langle L\rangle\:/\:\langle\overline{L}\rangle$ *Later* |
| ├──╊┫ | *meets* $\{m\}$ / *met-by* $\{mi\}$ | $\langle A\rangle\:/\:\langle\overline{A}\rangle$ *After* |
| ├─╊┿━┫ | *overlaps* $\{o\}$ / *overlapped-by* $\{oi\}$ | $\langle O\rangle\:/\:\langle\overline{O}\rangle$ *Overlaps* |
| ├─╊┫ | *finished-by* $\{fi\}$ / *finishes* $\{f\}$ | $\langle E\rangle\:/\:\langle\overline{E}\rangle$ *Ends* |
| ├╊╉┤ | *contains* $\{di\}$ / *during* $\{d\}$ | $\langle D\rangle\:/\:\langle\overline{D}\rangle$ *During* |
| ┣╉─┤ | *started-by* $\{si\}$ / *starts* $\{s\}$ | $\langle B\rangle\:/\:\langle\overline{B}\rangle$ *Begins* |

*Table 1:* Allen relations between time intervals and the corresponding Halpern-Shoham modal operators (see Section 6).

More abstract questions can also be posed: assume, for example, that we are provided with a structure defined by a set of interval relations (of arbitrary arity) that are required to fulfill certain conditions. Can this structure be represented by a concrete interval-based model over linear time? Answers are provided by various representation theorems, see e.g. van Benthem (1983)[^benthem-1983]; Ladkin (1987)[^ladkin-1987]; and Venema (1990)[^venema-1990].

### 2.3 Instant-based vs. interval-based models of time

The choice between instants and intervals as the primary objects of temporal ontology has been a highly debated philosophical theme since the times of Zeno and Aristotle (Øhrstrøm and Hasle 1995)[^øhrstrøm-1995]. Technically, the two types of temporal ontologies are closely related, and they are reducible to each other: on the one hand, time intervals can be defined by pairs of time instants (beginning and end); on the other hand, a time instant can be construed as a degenerate interval, viz. as a point-interval whose beginning and end points coincide.

Still, the technical reductions do not resolve the question whether sentences are to be evaluated with respect to instants or with respect to intervals, and one may argue that both instants and intervals are needed as mutually complementary. Two-sorted point-interval models were studied in e.g. Balbiani et al. (2011), and more complex models of time have been investigated as well, including models of time granularity (Euzenat and Montanari 2005)[^euzenat-2005], which allow for different resolution levels of temporal intervals (e.g. minutes, hours, days, years, etc.), metric and layered temporal models (Montanari 1996)[^montanari-1996][^montanari-1996-2], etc.

Here we focus mainly on instant-based logics and discuss interval-based logics in somewhat less detail. For further discussion on the ontological primacy of instants versus intervals in temporal logics, see Hamblin (1972)[^hamblin-1972]; Kamp (1979)[^kamp-1979]; Humberstone (1979)[^humberstone-1979]; Galton (1996)[^galton-1996]; as well as van Benthem (1983; 1984)[^benthem-1983][^benthem-1984], who provides a detailed comparative exploration of both approaches. A more philosophical and historical overview is provided in e.g. Øhrstrøm and Hasle (1995; 2006); Dyke and Bardon (2013); Meyer (2013)[^meyer-2013]; and Goranko (2023)[^goranko-2023].

## 3. Prior’s basic tense logic TL

In this section, we discuss the language, semantics, and axiomatization of the basic tense logic TL introduced by Prior (1957; 1967; 1968)[^prior-1957][^prior-1967][^prior-1968][^prior-1968-2], who is widely regarded as the founding father of temporal logic. Prior’s motivation for inventing tense logic was largely philosophical, and his ideas were inspired by the use of tense in natural language. The innovative feature of Prior’s approach was that he treated propositions as tensed rather than tenseless. Technically, this was achieved by the introduction of temporal operators into the language, which were given a modal-logic style semantics. In view of the pivotal role that tense played in his framework, Prior himself referred to his account as *Tense Logic*, whereas nowadays the more general expression *Temporal Logic* is more prevalent.

### 3.1 Prior’s tense operators

The basic language of Prior’s Tense Logic TL extends the standard propositional language (with atomic propositions and truth-functional connectives) by four temporal operators with intended meaning as follows:

- $P$: “It was (at some point in the **P**ast) the case that …”
- $F$: “It will (at some point in the **F**uture) be the case that …”
- $H$: “It **H**as always been the case that …”
- $G$: “It is always **G**oing to be the case that …”

For example, “It will always be the case that Prior invented Tense Logic” translates in TL as $GP(\mathsf{Prior\ invents\ TL})$, which can be glossed as “It is always going to be the case that it was the case that Prior invents Tense Logic”. Formulae not containing temporal operators are considered present tensed.

The language of TL contains one pair of temporal operators for the past, $P$ and $H$, and one pair of temporal operators for the future, $F$ and $G$. The operators $P$ and $F$ are often referred to as the ‘weak’ temporal operators, while $H$ and $G$ are known as the ‘strong’ ones. The respective past and future operators are duals of each other, i.e., they are interdefinable by means of the following equivalences:

$$ P\varphi \equiv \neg H\neg \varphi, H\varphi \equiv \neg P\neg \varphi \text{ and } F\varphi \equiv \neg G\neg \varphi, G\varphi \equiv \neg F\neg \varphi. $$

In light of these equivalences, the set of formulae of TL can be recursively defined as follows, over a given set of atomic propositions $PROP$: $$ \varphi := p \in {PROP} \mid \lnot \varphi \mid (\varphi \land \varphi) \mid P\varphi \mid F\varphi. $$ The truth-functional connectives $\vee,\to,$ and $\leftrightarrow$ as well as the logical constants $\top$ and $\bot$ are definable in terms of $\lnot$ and $\land$ as usual. Besides, we can define $A\varphi =H\varphi \wedge \varphi \wedge G\varphi$ and, dually, $E\varphi =P\varphi \vee \varphi \vee F\varphi,$ which on linear flows of time mean “always” and “sometime”, respectively.

As said, Prior’s introduction of the temporal operators was motivated by the use of tense in natural language, and indeed, various tenses in natural language can, at least approximately, be captured in TL. For example:

- $P$: “Prior *(has) invented* Tense Logic”.
- $F$: “Prior *will invent* Tense Logic”.
- $PP$: “Prior *had invented* Tense Logic”.
- $FP$: “Prior *will have invented* Tense Logic”.
- $PF$: “Prior *would invent* Tense Logic”.

Hamblin and Prior showed that, in models of linear time, any sequence of temporal operators reduces to a sequence of at most two operators. In total, they identified 15 different such combinations — or *tenses*, as they called them (see Prior 1967, Chapter III.5)[^prior-1967]. These combinations seem to surpass the number of verbal tenses in e.g. English, but there are also temporal features of natural language that cannot be captured in TL: Prior’s temporal operators cannot, for instance, distinguish between the simple past and the present perfect (“I wrote a letter” vs. “I have written a letter”), a distinction that drove Reichenbach’s work. Moreover, they are not suited to model the linguistic differentiation between perfective and imperfective aspect (“I wrote a letter” vs. “I was writing a letter”), which is arguably more adequately dealt with in an interval-based framework. For details, see Kuhn and Portner (2006) and the entry on tense and aspect.

### 3.2 Semantics of TL

The standard semantics of TL is essentially a Kripke-style semantics, familiar from modal logic. In modal logic, sentences are evaluated over so-called Kripke frames consisting of a non-empty set of possible worlds and an accessibility relation between them. In temporal logic, the possible worlds are time instants, and the accessibility relation has a concrete interpretation in terms of temporal precedence. In other words, sentences are evaluated over instant-based models of time $\mathcal{T}=\left\langle T, \prec \right\rangle$, hereafter called *temporal frames*. Note that so far no conditions, like transitivity, irreflexivity, etc., are imposed on the precedence relation $\prec$.

Given a set of atomic propositions $PROP$, a *temporal model* for TL is a triple $\mathcal{M}= \left\langle T, \prec, V \right\rangle$ where $\mathcal{T} =\left\langle T, \prec \right\rangle$ is a temporal frame and $V: PROP \rightarrow \mathcal{P}(T)$ is a *valuation function* that assigns to each atomic proposition $p\in{PROP}$ the set of time instants $V(p) \subseteq T$ at which $p$ is considered true. (Equivalently, the valuation can be given by a function $I: T\times{PROP}\to \{\mathit{true},\mathit{false}\},$ which assigns a truth value to each atomic proposition at each time instant in the temporal frame, or by a *labeling* or *state description* $L: T \to \mathcal{P}({PROP})$, which assigns to each time instant the set of atomic propositions that are considered true at that instant.)

The *truth of an arbitrary formula φ of TL at a given time instant $t$ in a temporal model $\mathcal{M}$* (denoted $\mathcal{M},t \models\varphi$) is then defined inductively as follows:

- $\mathcal{M},t \models p$   iff   $t \in V(p)$, for $p \in {PROP}$;
- $\mathcal{M},t \models \neg\varphi$   iff   $\mathcal{M},t \not\models\varphi$ (i.e., it is not the case that $\mathcal{M},t \models \varphi$);
- $\mathcal{M},t \models \varphi \wedge \psi$   iff   $\mathcal{M},t \models\varphi$ and $\mathcal{M},t \models\psi$;
- $\mathcal{M},t \models P\varphi$   iff   $\mathcal{M},t'\models \varphi$ for some time instant $t'$ such that $t'\prec t{;}$
- $\mathcal{M},t \models F\varphi$   iff   $\mathcal{M},t'\models \varphi$ for some time instant $t'$ such that $t\prec t'.$

That is, a formula of the form $P\varphi$ is true at an instant $t$ iff *φ* is true at some earlier instant $t',$ while $F\varphi$ is true at $t$ iff *φ* is true at some later instant $t'.$ Accordingly, for the duals $H$ and $G$, we have that $H\varphi$ is true at $t$ iff *φ* is true at all earlier instants $t',$ and $G\varphi$ is true at $t$ iff *φ* is true at all later instants $t'.$

- $\mathcal{M},t \models H\varphi$   iff   $\mathcal{M},t'\models \varphi$ for all time instants $t'$ such that $t'\prec t$;
- $\mathcal{M},t \models G\varphi$   iff   $\mathcal{M},t'\models \varphi$ for all time instants $t'$ such that $t\prec t'$.

Note that, from the point of view of modal logic, there are two different accessibility relations involved here: an ‘earlier-relation’ in the case of the past operators and a ‘later-relation’ in the case of the future operators. In temporal logic, these two relations are covered by a single precedence relation; after all, ‘earlier’ and ‘later’ are just converses of each other (i.e., $t$ is earlier than $t'$ iff $t'$ is later than $t$).

A formula *φ* of TL is *valid in a temporal model $\mathcal{M}$* (denoted $\mathcal{M} \models \varphi$) iff it is true at every time instant in that model. Moreover, we say that *φ* is *valid in a temporal frame* $\mathcal{T}$ (denoted $\mathcal{T} \models \varphi$) iff it is valid in every model on that frame. Accordingly, a formula *φ* is *valid* (denoted $\models \varphi$) iff it is valid in all temporal frames, i.e. true at all time instants in all temporal models. A formula *φ* is *satisfiable* iff its negation is not valid, i.e. if *φ* is true at some time instant in some temporal model.

### 3.3 Standard translation of TL into first-order logic

As in the case of modal logic, the language and semantics of TL can be translated into classical first-order logic (see e.g. van Benthem 1983)[^benthem-1983].

Suppose that the set of atomic propositions of TL is given by ${PROP}=\left\{p_{0},p_{1},...\right\}$, and let $L_{1}$ be a first-order language with a denumerable set of unary predicate symbols $\mathcal{P}=\left\{P_{0},P_{1},...\right\}$, one for each atomic proposition of TL, and a binary predicate symbol $R$ for the precedence relation. The *standard translation* $ST$ of TL into $L_{1}$ is defined as follows, where $\theta[y/x]$ is the result of substituting $y$ for all free occurrences of $x$ in *θ*:

- $ST(p_{i}) = P_{i}(x);$
- $ST(\lnot\varphi) = \lnot ST(\varphi);$
- $ST(\varphi \land \psi) = ST(\varphi)\land ST(\psi);$
- $ST(P\varphi) = \exists y(yRx\wedge ST(\varphi)[y/x]),$ where $y$ is a new variable (i.e. one unused so far);
- $ST(F\varphi) = \exists y(xRy\wedge ST(\varphi)[y/x]),$ where $y$ is a new variable.

It then follows that

- $ST(H\varphi) = \forall y(yRx\rightarrow ST(\varphi)[y/x]);$
- $ST(G\varphi) = \forall y(xRy\rightarrow ST(\varphi)[y/x]).$

For example:

$$ST(Gp_{1}\lor FHp_{2})=\forall y(xRy\rightarrow P_{1}(y))\lor \exists y(xRy\wedge \forall z(zRy\rightarrow P_{2}(z))).$$

Not every first-order formula has a correspondent in TL. Actually, by carefully re-using variables, TL can be translated into the two-variable fragment FO$^{2}$ of first-order logic, which eventually implies decidability (since validity in FO$^{2}$ is decidable, as shown by Grädel and Otto 1999)[^grädel-1999]. For instance, the example above can be re-written as

$$ST(Gp_{1}\lor FHp_{2})=\forall y(xRy\rightarrow P_{1}(y))\lor \exists y(xRy\wedge \forall x(xRy\rightarrow P_{2}(x))).$$

Given the standard translation, every temporal model $\mathcal{M}=\left\langle T,\prec ,V\right\rangle$ can be regarded as an $L_{1}$-model where $R$ is interpreted by $\prec$ and each $P_{i}$ by $V(p_{i}).$ Then:

$$\begin{align} \mathcal{M},t \models \varphi \ & \text{ iff } \mathcal{M}\models ST(\varphi)[x:=t], \\ \mathcal{M} \models \varphi \ & \text{ iff } \mathcal{M}\models \forall x ST(\varphi). \end{align}$$

Thus, validity of a formula of TL in a temporal model is a first-order property. Validity in a temporal frame, on the other hand, turns out to be a second-order property as it involves universal quantification over valuations. If we treat the unary predicates from $\mathcal{P}$ as predicate *variables* of a second-order language $L_{2}$ that range over all subsets of $T$, every temporal frame $\mathcal{T} = \langle T,\prec\rangle$ can be regarded as an $L_{2}$-model. We have:

$$\begin{align} \mathcal{T}\models \varphi \ & \text{ iff }\mathcal{T}\models \forall P_0 \forall P_1\dots\forall x ST(\varphi), \\ \models \varphi \ & \text{ iff }\models \forall P_0 \forall P_1\dots\forall x ST(\varphi). \end{align}$$

The standard translation of TL into first-order logic enables a systematic treatment of various aspects of temporal logic with the tools and techniques of classical logic (see e.g. van Benthem 2001; Blackburn et al. 2007)[^benthem-2001][^blackburn-2007]. However, since TL validity is essentially second-order, when it comes to frame definability, there are also interesting divergences. As we will see in Section 3.6, not all first-order properties of temporal frames are definable by temporal formulae; and vice versa, not all properties of temporal frames that can be expressed by formulae of TL are first-order definable. A non-trivial correspondence between temporal logic and first-order logic as alternative languages for describing properties of time emerges, see e.g. van Benthem (1995)[^benthem-1995].

### 3.4 Tense logic, first-order logic, and McTaggart’s time series

The standard translation discussed in the previous section links the semantics of Prior’s basic tense logic to first-order logic. Yet, there are crucial differences between the two approaches. In fact, in the early days of temporal logic, Prior’s approach was perceived as a rival to more conventional approaches using first-order logic. The rivalry between tense logic and first-order logic can be seen as reflecting a fundamental distinction concerning the nature of time, namely the distinction between the A-series and the B-series of time introduced by McTaggart (1908)[^mctaggart-1908].

Roughly speaking, the A-series characterizes time and temporal order in terms of past, present, and future. The B-series, in contrast, is based on the notions ‘earlier’ and ‘later’. McTaggart argued that the B-series is insufficient because it lacks an appropriate notion of change, and he rejected the A-series as inconsistent because what is future now will be past, which, according to him, requires that one and the same time instant has incompatible properties. From this he concluded that time is unreal. For a detailed discussion of McTaggart’s account and its philosophical relevance, see Ingthorsson (2016)[^ingthorsson-2016] and the entry on time.

There is arguably a close correspondence between the A-series conception of time and tense logic, on the one hand, and between the B-series conception and first-order logic, on the other, as was already noted by Prior (1967, Chapter 1). Consider, for example, the sentence “It was light, it is dark, and it will be light again.” This sentence can be formalized in TL as $$P(\mathsf{light}) \wedge \mathsf{dark} \wedge F(\mathsf{light})$$ while its first-order formulation reads $$\exists t_0 (t_0 \prec t_1 \wedge \mathsf{light}(t_0)) \wedge \mathsf{dark}(t_1) \wedge \exists t_2 (t_1 \prec t_2 \wedge \mathsf{light}(t_2)).$$ The TL formula consists of tensed propositions, and it invokes the local perspective of the present. Accordingly, the truth value of the formula changes over time. The first-order formula, by contrast, is built up from tenseless propositions and has a fixed truth value once and for all. Here we are provided with predicates of time instants rather than tenses, and the perspective involved is an overarching, global one. Prior felt that not everything that can be expressed in a tensed language can likewise be expressed in a tenseless one, his classic example being: “Thank goodness, that’s over!” (Prior 1959)[^prior-1959].

### 3.5 Axiomatic system $\mathbf{K}_{t}$ for TL

Like every formal logical system, temporal logic has two major aspects: a *semantic* and a *deductive* one. In this section, we present a deductive system for TL, viz. the *minimal temporal logic $\mathbf{K}_{t}$*. The system we are providing is a Hilbert-style axiomatic one, i.e., it consists of lists of axioms and inference rules. The system was first studied by Lemmon, following earlier axiomatizations proposed by Hamblin and Prior (see Rescher and Urquhart 1971, Chapter VI)[^rescher-1971].

The list of axioms of the minimal temporal logic $\mathbf{K}_{t}$ extends classical propositional logic by the following four axiom schemata:

- $(K_H)$ $H(\varphi \rightarrow \psi)\rightarrow (H\varphi \rightarrow H\psi)$
- $(K_G)$ $G(\varphi \rightarrow \psi)\rightarrow (G\varphi \rightarrow G\psi)$
- (GP) $\varphi \rightarrow GP\varphi$
- (HF) $\varphi \rightarrow HF\varphi$

The first two axiom schemata are the temporal correspondents of the so-called *K-axiom* of modal logic, hence the terminology $\mathbf{K}_{t}$. The third and fourth axiom schemata capture the interaction of the past and future operators. They guarantee that these operators exploit converse temporal relations, viz. earlier and later, respectively.

The inference rules comprise, in addition to the classical *modus ponens*, two *necessitation rules* for the temporal operators (where $\vdash$ means “deducible”):

- (MP) If $\vdash \varphi \rightarrow \psi$ and $\vdash \varphi,$ then $\vdash \psi.$
- (NEC$_H$) If $\vdash \varphi,$ then $\vdash H\varphi.$
- (NEC$_G$) If $\vdash \varphi,$ then $\vdash G\varphi.$

The axiomatic system $\mathbf{K}_{t}$ is sound and complete for validity in TL: all and only those formulae that are valid in TL can be deduced from the axioms according to the rules. For a proof, see e.g. Rescher and Urquhart (1971); McArthur 1976; Goldblatt (1992)[^goldblatt-1992]; and Gabbay et al. (1994).

### 3.6 Expressing temporal properties in TL and extensions of $\mathbf{K}_{t}$

The minimal temporal logic $\mathbf{K}_{t}$ captures those validities of TL that do not depend on any specific assumptions concerning the properties of the temporal precedence relation. In this section, we will see that many natural properties of temporal frames can be expressed by temporal formulae, and, taken as additional axioms, these formulae can often be used to define logics on the relevant subclasses of temporal frames.

A temporal formula of TL *expresses* (*defines* or *corresponds to*) a property of temporal frames if the formula is valid in all and only those frames that have the property. The most important correspondences between properties of temporal frames (see list in Section 2.1) and TL formulae include:

| (REF) | any of $H\varphi \rightarrow \varphi,$ $G\varphi \rightarrow \varphi,$ $\varphi \rightarrow P\varphi,$ or $\varphi \rightarrow F\varphi$ (reflexivity) |
| --- | --- |
| (TRAN) | any of $H\varphi \rightarrow HH\varphi,$ $G\varphi \rightarrow GG\varphi,$ $PP\varphi \rightarrow P\varphi,$ or $FF\varphi \rightarrow F\varphi$ (transitivity) |
| (LIN-F) | $PF\varphi \rightarrow (P\varphi \vee \varphi \vee F\varphi)$ or $F\varphi \wedge F\psi \rightarrow (F(\varphi\wedge \psi) \vee F(F\varphi \wedge \psi) \vee F(\varphi \wedge F\psi))$ (forward-linearity) |
| (LIN-P) | $FP\varphi \rightarrow (P\varphi \vee \varphi \vee F\varphi)$ or $P\varphi \wedge P\psi \rightarrow (P(\varphi\wedge \psi) \vee P(P\varphi \wedge \psi) \vee P(\varphi \wedge P\psi))$ (backward-linearity) |
| (LIN) | $(PF\varphi \lor FP\varphi) \rightarrow (P\varphi \vee \varphi \vee F\varphi)$ (linearity) |
| (BEG) | $H\bot \vee PH\bot$ (time has a beginning, assuming irreflexivity and transitivity) |
| (END) | $G\bot \vee FG\bot$ (time has an end, assuming irreflexivity and transitivity) |
| (NOBEG) | $P\top$  or  $H\varphi\rightarrow P\varphi$ (time has no beginning) |
| (NOEND) | $F\top$  or  $G\varphi\rightarrow F\varphi$ (time has no end) |
| (DENSE) | any of $HH\varphi \rightarrow H\varphi,$ $GG\varphi \rightarrow G\varphi,$ $P\varphi \rightarrow PP\varphi,$ or $F\varphi \rightarrow FF\varphi$ (density) |
| (DISCR-F) | $(F\top \wedge \varphi \wedge H\varphi) \rightarrow FH\varphi$ (forward-discreteness, assuming forward-linearity) |
| (DISCR-P) | $(P\top \wedge \varphi \wedge G\varphi) \rightarrow PG\varphi$ (backward-discreteness, assuming backward-linearity) |
| (COMPL) | $(FG\lnot\varphi \wedge F\varphi) \rightarrow F(G\lnot\varphi \wedge HF\varphi)$ or $A(H\varphi \rightarrow FH\varphi)\rightarrow (H\varphi \rightarrow G\varphi)$ (Dedekind completeness, recall that $A\varphi = H\varphi \wedge \varphi \wedge G\varphi$) |
| (WELLORD) | $H(H\varphi \rightarrow \varphi)\rightarrow H\varphi$ (well-ordering with transitivity) |
| (FIN-INT) | $(G(G\varphi\rightarrow\varphi)\rightarrow (FG\varphi\rightarrow G\varphi))\ \wedge$ $(H(H\varphi\rightarrow\varphi)\rightarrow (PH\varphi\rightarrow H\varphi))$ (finite intervals) |
| (IND$_{G}$) | $F\varphi \wedge G(\varphi \rightarrow F\varphi)\rightarrow GF\varphi$ (forward induction) |
| (IND$_{H}$) | $P\varphi \wedge H(\varphi\rightarrow P\varphi)\rightarrow HP\varphi$ (backward induction) |

The principle (LIN) combines forward-linearity (LIN-F) and backward-linearity (LIN-P) in a single condition. The resulting formula is, however, not sufficient to guarantee the connectedness of the temporal frame. In other words, it cannot rule out disjoint linear time lines. Moreover, (FIN-INT) is equivalent to the conjunction of (IND$_{H}$) and (IND$_{G}$). Note that (IND$_{H}$) implies forward-discreteness and that (IND$_{G}$) implies backward-discreteness, but not conversely. For instance, a time flow consisting of a copy of the natural numbers followed by a copy of the integers is backward-discrete, but does not satisfy (IND$_{G}$). To see this, assume that *φ* is true on the copy of the natural numbers but not on the copy of the integers and evaluate at the initial point of the structure.

Recall that the last five properties mentioned above — Dedekind completeness, well-ordering, the finite interval property, and forward/backward induction — are not definable by first-order sentences. However, they can be expressed by temporal formulae. On the other hand, some very simple first-order definable properties of temporal frames, such as irreflexivity or asymmetry, are not expressible in TL. Proofs of some of the correspondence claims listed above can be found in Goranko (2023)[^goranko-2023]. For more results and details on the expressibility of properties of temporal frames, see Segerberg (1970)[^segerberg-1970]; Rescher and Urquhart (1971); Burgess (1979)[^burgess-1979]; van Benthem (1983; 1995)[^benthem-1983][^benthem-1995]; Goldblatt (1992)[^goldblatt-1992]; and Hodkinson and Reynolds (2007)[^reynolds-2007].

By extending the list of axioms of $\mathbf{K}_{t}$ with one or several of the above principles one can axiomatize the logics of various natural models of time; that is, there are axiomatic extensions that are sound and complete for validity on the relevant class of temporal frames. Some of these extensions were already studied in the early days of Temporal Logic. Prior (1967)[^prior-1967] discusses various systems resulting from different combinations of axioms. We provide some important ones below:

$$\begin{align} \mathbf{K4}_{t} = & \ \mathbf{K}_{t} + \text{(TRAN): all transitive frames.} \\ \mathbf{S4}_{t} = & \ \mathbf{K}_{t} + \text{(REF) + (TRAN): all partial orderings.} \\ \mathbf{L}_{t} = & \ \mathbf{K}_{t} + \text{(TRAN) + (LIN): all strict linear orderings.} \\ \mathbf{N}_{t} = & \ \mathbf{L}_{t} + \text{(NOEND) + (IND\(_{G}\)) + (WELLORD) or} \\ & \ \mathbf{L}_{t} + \text{(BEG) + (NOEND) + (FIN-INT): } \langle \mathbf{N,\lt}\rangle. \\ \mathbf{Z}_{t} = & \ \mathbf{L}_{t} + \text{(NOBEG) + (NOEND) + (IND\(_{H}\)) + (IND\(_{G}\)) or} \\ & \ \mathbf{L}_{t} + \text{(NOBEG) + (NOEND) + (FIN-INT): } \langle \mathbf{Z,\lt}\rangle. \\ \mathbf{Q}_{t} = & \ \mathbf{L}_{t} + \text{(NOBEG) + (NOEND) + (DENSE): } \left\langle \mathbf{Q, \lt}\right\rangle. \\ \mathbf{R}_{t} = & \ \mathbf{L}_{t} + \text{(NOBEG) + (NOEND) + (DENSE) + (COMPL): } \left\langle \mathbf{R, \lt}\right\rangle. \end{align}$$

As the axiomatizations of the number systems illustrate, the fact that (LIN) is not sufficient to guarantee connectedness, or that irreflexivity is not definable in TL, does not hamper axiomatizbility (even though it requires some manipulations in the completeness proofs, see e.g. Blackburn et al. 2001, Chapter 4)[^blackburn-2001]. Indeed, connectedness and irreflexivity do not yield any new validities.

Each of the above logics turns out *decidable* (i.e., it has a decidable set of validities). This is typically shown by proving the *finite model property*: “Every satisfiable formula is satisfiable in a finite model”. In most cases, such proofs involve non-standard models. For proofs of completeness of (variations of) these axiomatic systems as well as proofs of decidability, see Segerberg (1970)[^segerberg-1970]; Rescher and Urquhart (1971); Burgess (1979)[^burgess-1979]; Burgess and Gurevich (1985); Goldblatt (1992)[^goldblatt-1992]; and Gabbay et al. (1994).

## 4. Extensions of TL over linear time

A natural class of instant-based models of time is the class of linear models, and soon after Prior’s invention of Tense Logic several extensions of TL over linear time have been proposed. In this section, we discuss two such extensions: the *Next Time* operator and the operators *Since* and *Until*. We then introduce the linear time temporal logic LTL, which is based on those operators and has important applications in computer science.

### 4.1 Adding the *Next Time* operator

In forward-discrete, linear temporal models $\mathcal{M}= \left\langle T,\prec, V \right\rangle$ without end point, where every instant $t$ has a unique immediate successor $s(t),$ it is natural to add a new temporal operator $X$ (“*NeXt Time*” or “*Tomorrow*”) with the following semantics:[^note-2]

$$ \mathcal{M},t \models X\varphi \text{ iff } \mathcal{M},s(t) \models \varphi. $$

That is, $X\varphi$ is true at a time instant $t$ iff *φ* is true at the immediate successor $s(t)$ of $t$. The *Next Time* operator was already mentioned by Prior (1967, Chapter IV.3), but its importance was first fully appreciated in the context of LTL.

The operator $X$ satisfies the K-axiom

- (K$_{X}$) $X(\varphi \to \psi) \to (X\varphi \to X\psi);$

and the functionality axiom

- (FUNC) $X\lnot \varphi \leftrightarrow \lnot X\varphi.$

It also enables a recursive fixed point definition of $G$ and, on the ordering of the natural numbers, the operators $X$ and $G$ satisfy an induction principle. Assuming the reflexive closure of the precedence relation $\prec$, as is common in computer science, these properties can be expressed as follows:

- (FP$_G$) $G\varphi \leftrightarrow (\varphi \wedge XG\varphi);$
- (IND) $\varphi \wedge G(\varphi \rightarrow X\varphi )\rightarrow G\varphi.$

In the language with $G,H,$ and $X$, these principles can be used to provide sound and complete axiomatizations of the temporal logic of forward-discrete, linear orderings without end points and the natural numbers with successor function, respectively:

$\mathbf{L}_{t}(X) = \mathbf{L}_{t}$ + (K$_{X}$) + (FUNC) + (FP$_{G}$): all forward-discrete, linear orderings without end points. $\mathbf{N}_{t}(X) = \mathbf{N}_{t}$ + (K$_{X}$) + (FUNC) + (FP$_{G}) $ + (IND): $\left\langle \mathbf{N},s,\leq \right\rangle,$ where $s(n) = n+1.$

A past analogue of $X$, usually denoted $Y$ (“*Yesterday*”), can be defined and axiomatized likewise. For details, see Goldblatt (1992)[^goldblatt-1992] and Andréka et al. (1995).

### 4.2 Adding *Since* and *Until*

Perhaps the most important extension of Prior’s basic tense logic TL over linear time was the introduction of the binary temporal operators $S$ (“*Since*”) and $U$ (“*Until*”) by Hans Kamp in his doctoral dissertation (Kamp 1968)[^kamp-1968]. The intuitive meanings of these are[^note-3]

- $\varphi S\psi$ “*φ* has been the case since a time when *ψ* was the case.”
- $\varphi U\psi$ “*φ* will be the case until a time when *ψ* is the case.”

For instance, the sentence “I will keep trying until I succeed” can be formalized as: $\mathsf{try}\, U\,\mathsf{succeed}.$ As another example, “Ever since Mia left home, Joe has been unhappy and has been drinking until losing consciousness” translates as:

$$ (\mathsf{Joe\ unhappy} \land (\mathsf{Joe\ drinks}\ U\ \lnot(\mathsf{Joe\ conscious})))\ S\ (\mathsf{Mia\ leaves}). $$

The formal semantics of $S$ and $U$ in a temporal model $\mathcal{M} = \langle T,\prec,V\rangle$ is given by the following two clauses:

$$\begin{array}{ll} \mathcal{M},t\vDash \varphi S\psi\quad \text{ iff } &\mathcal{M},s\vDash \psi \text{ for some } s \text{ such that } s\prec t \\ & \text{ and } \mathcal{M},u\vDash \varphi \text{ for every } u \text{ such that } s\prec u\prec t; \\ \mathcal{M},t\vDash \varphi U\psi \quad \text{ iff } &\mathcal{M},s\vDash \psi \text{ for some } s \text{ such that } t\prec s \\ & \text{ and } \mathcal{M},u\vDash \varphi \text{ for every } u \text{ such that } t\prec u\prec s. \end{array}$$

These are the ‘strict’ versions of $S$ and $U$, prevalent in philosophy. In computer science, usually reflexive versions of the semantics clauses are considered.

Prior’s temporal operators $P$ and $F$ are definable in terms of $S$ and $U$:

$$ P\varphi :=\top S\varphi \ \text{ and } \ F\varphi :=\top U\varphi. $$

On irreflexive, forward-discrete, linear temporal orders without end point, $S$ and $U$ also allow for a definition of the *Next Time* operator $X$:

$$ X\varphi := \bot U \varphi. $$

This definition fails on reflexive temporal orders, which shows that the strict versions of $S$ and $U$ are more expressive than their reflexive counterparts.[^note-4] Other operators can be defined in terms of $S$ and $U$ as well, such as for instance *Before*, given by $\varphi B\psi :=\lnot ((\lnot \varphi)U\psi)$ with intuitive reading “If *ψ* will be the case in the future, *φ* will occur before *ψ*”.

Temporal languages with *Since* and *Until* afford great expressive power. Kamp (1968)[^kamp-1968] proved the following remarkable result:

*Every temporal operator on a class of continuous, strict linear orderings that is definable in first-order logic is expressible in terms of $S$ and $U$*.

The result was later extended by Stavi to all linear orders, by introducing two additional operators. However, it turns out that no finite number of new operators can make the temporal language functionally complete on all *partial* orderings, as shown by Gabbay. See Gabbay et al. (1994) for an overview of these results.

A complete axiomatic system for the Since-Until logic on the class of all reflexive linear orderings was provided by Burgess (1982a)[^burgess-1982a] and further simplified by Xu (1988). Extensions of this axiomatization for strict linear orderings were obtained by Venema (1993)[^venema-1993] and Reynolds (1994; 1996)[^reynolds-1994][^reynolds-1996]. For details and related results, see Burgess (1984)[^burgess-1984]; Zanardo (1991)[^zanardo-1991]; Gabbay et al. (1994); Finger et al. (2002); and Hodkinson and Reynolds (2007)[^reynolds-2007]. The Burgess-Xu axiomatic system and some of its extensions are presented in the supplementary document:

> [Burgess-Xu Axiomatic System for *Since* and *Until* and Some Extensions](logic-temporal.burgess-xu.md)

### 4.3 The linear time temporal logic LTL

The most popular and widely used temporal logic in computer science is the linear time temporal logic LTL, which was proposed in a seminal paper by Pnueli (1977)[^pnueli-1977] and was first explicitly axiomatized and studied in Gabbay et al. (1980). In LTL, the flow of time is viewed as a discrete, linear sequence of time instants, which are taken to represent successive states of a run of a computer system. To be more precise, LTL is interpreted over the reflexive closure of the ordering of the natural numbers $\left\langle \mathbf{N},\leq\right\rangle,$ and the language involves the operators $G,$ $X$, and $U$ (no past operators).

The logic LTL is very useful for expressing properties of infinite computations in reactive systems, such as safety, liveness, and fairness, as laid out in Section 11.1. For example, the specification “Every time when a message is sent, an acknowledgment of receipt will eventually be returned, and the message will not be marked ‘sent’ before the acknowledgment of receipt is returned” can be formalized in LTL as:

$$ G(\mathsf{Sent} \to (\lnot \mathsf{MarkedSent} \ U\ \mathsf{AckReturned})). $$

The axiomatic system for LTL extends classical propositional logic by the K-axiom for $G$, the K-axiom and the functionality axioms for $X$, as well as by axioms providing fixed point characterizations of the reflexive versions of $G$ and $U$:

- (K$_G$) $G(\varphi \rightarrow \psi)\rightarrow (G\varphi \rightarrow G\psi)$
- (K$_X$) $X(\varphi \rightarrow \psi)\rightarrow (X\varphi \rightarrow X\psi)$
- (FUNC) $X\lnot \varphi \leftrightarrow \lnot X\varphi$
- (FP$_G$) $G\varphi \leftrightarrow (\varphi \wedge XG\varphi)$
- (GFP$_G$) $\psi \land G(\psi \rightarrow (\varphi \land X\psi)) \rightarrow G\varphi$
- (FP$_U$) $\varphi U\psi \leftrightarrow (\psi \vee (\varphi \wedge X(\varphi U\psi)))$
- (LFP$_U$) $G((\psi \vee (\varphi \wedge X\theta))\rightarrow \theta)\rightarrow (\varphi U\psi \rightarrow \theta)$

The inference rules involve only *modus ponens* and the necessitation rule for $G$. In technical terms, the axiom (FP$_{G}$) says that $G\varphi$ is a *fixed point* of the operator $\Gamma_{G}$ defined by $\Gamma_{G} (\theta) = \varphi \land X\theta,$ whereas (GFP$_{G}$) says that $G\varphi$ is (in terms of its set-theoretic extension) a *greatest post-fixed point* of $\Gamma_{G}.$ Likewise, the axiom (FP$_{U}$) says that $\varphi U\psi$ is a *fixed point* of the operator $\Gamma_{U}$ defined by $\Gamma_{U}(\theta) = \psi \lor (\varphi \land X\theta),$ whereas (LFP$_{U}$) says that $\varphi U\psi$ is a *least pre-fixed point* of $\Gamma_{U}$. Some variations of this axiomatic system are presented in the supplementary document:

> [Some Variations of the Axiomatic System for LTL](logic-temporal.axiomatic-ltl.md)

Early studies of temporal logics for linear time are presented in Rescher and Urquhart (1971) and McArthur (1976)[^mcarthur-1976]. Proofs of completeness of variations of the axiomatic system given above can be found in Gabbay et al. (1980; 1994); Goldblatt (1992)[^goldblatt-1992]; and Finger et al. (2002). All logics mentioned in this section have the finite model property (usually with respect to non-standard models) and hence are decidable (see the references on completeness).

## 5. Branching time temporal logics

Much of Prior’s work on Tense Logic was motivated by the Master Argument of Diodorus Chronus and its fatalistic conclusion. Confronted with the following trilemma

1. Every true proposition concerning the past is necessary.
2. The impossible does not follow from the possible.
3. Something that neither is nor will be is possible.

Diodorus went on to define the possible as “what is or will be the case” (see Prior 1967, Chapter 3.1)[^prior-1967]. Prior set out to show that Diodorus’ argument was wrong.

Prior was interested in themes like indeterminism and the open future; one of his objectives here was to allow for human freedom. In order to analyze and clarify the assumptions underlying the Master Argument, he opted for a branching representation of the interrelation of time and modality, which was suggested to him in a letter by Kripke in 1958 (see Ploug and Øhrstrøm 2012)[^ploug-2012].[^note-5] The Diodorean conception of modality as quantification over linear time was abandoned and replaced by the picture of a tree, whose branches depict alternative possibilities for the future. Prior (1967, Chapter 7) considered two different versions of branching time temporal logic, which he associated with the historical views of Peirce and Ockham, respectively. An early formal treatment of these ideas is provided in Thomason (1970; 1984)[^thomason-1970][^thomason-1984] and Burgess (1978)[^burgess-1978]. Many technical results and further developments have been proposed since then, and we mention some of them below, including the computation tree logics CTL and CTL\*.

For Prior’s motivational views on indeterminism and human freedom, see Øhrstrøm and Hasle (1995, Chapters 2.6 and 3.2) and Øhrstrøm (2019)[^øhrstrøm-2019][^øhrstrøm-2019-2]. A detailed discussion of the philosophical aspects of the theory of branching time is contained in e.g. Belnap et al. (2001); Correia and Iacona (2013); the entry on future contingents and the entry on branching time.

### 5.1 Prior’s theory of branching time

In Prior’s theory of branching time, the interrelation of time and modality is represented as a tree that is linear towards the past and branches into multiple possible futures. Backward-linearity captures the idea that the past is fixed; forward-branching reflects the openness of the future. At each point in time, there may be more than one branch leading towards the future, and each such branch represents a future possibility.

Formally, a *tree* (or *branching time structure*) is a temporal frame $\mathcal{T} = \left\langle T, \prec \right\rangle$ where the temporal precedence relation $\prec$ is a backward-linear partial order on the set of time instants $T$ such that any two instants have a common $\prec$-predecessor in $T$. That is, every time instant in the tree has a linearly ordered set of $\prec$-predecessors, and any two instants share some common past. The former condition rules out backward-branching, while the latter ensures ‘historical connectedness’. In the philosophical literature, the temporal precedence relation $\prec$ is commonly assumed to be irreflexive, i.e. a strict partial order, whereas in the computational tree logics, its reflexive closure is exploited, as we will see in Section 5.5.

A tree $\mathcal{T} = \left\langle T, \prec \right\rangle$ depicts alternative possibilities for the future in a unified structure, and it can be carved up into multiple histories. A *history* in $\mathcal{T}$ is a maximal (i.e. non-extendable) set of time instants that is linearly ordered by $\prec$, that is, an entire path through the tree; it represents a complete possible course of events. We denote the set of all histories in $\mathcal{T}$ by $\mathcal{H}(\mathcal{T})$, and we use $\mathcal{H}(t)$ for the set of histories passing through a given time instant $t$.

Some philosophers have criticized the label ‘branching time’ as a misnomer, arguing that time does not branch but rather evolves linearly. Early criticism along these lines is found in Rescher and Urquhart (1971), and a similar point is raised in Belnap et al. (2001), who suggest the name ‘branching histories’ instead. This criticism also casts doubt on the terminology ‘time instants’ used here to refer to the primitive points of the tree. We stick to the terminology for reasons of uniformity. In the branching time literature, the more neutral expression ‘moments’ prevails, and in Belnap et al. (2001) the distinction between instants of time and moments is formally worked out: branching time structures are associated with a linearly ordered set of time instants, where an instant is defined as the set of contemporaneous moments across different histories.

### 5.2 The Peircean branching time temporal logic

Prior’s basic tense logic TL remains neutral about the structure of time. In a branching time setting with alternative future possibilities, however, the original semantics of the future operator $F$ no longer adequately captures future truth. In such a setting, the future operator $F$ merely reads “it will possibly be the case that $\dots$”. Prior (1967, Chapter 7) therefore considered two alternative semantics for the future operator, which give rise to the Peircean and Ockhamist branching time temporal logics, respectively.

In the Peircean branching time logic PBTL, the intuitive meaning of the future operator $F$ is “it will necessarily be the case that $\dots$”. That is, future truth is conceived of as truth in *all* possible futures. On this new reading, the future operator $F$ is no longer dual to the strong future operator $G$, which retains its original semantics but now needs to be included as an additional primitive operator into the language. Given a set of atomic propositions ${PROP}$, the set of formulae of PBTL can be recursively defined as follows:

$$ \varphi := p \in {PROP}\mid \neg \varphi\mid (\varphi \wedge \varphi) \mid P \varphi \mid F\varphi \mid G \varphi. $$

Formulae of PBTL are evaluated in a temporal model $\mathcal{M} = \langle T,\prec,V\rangle$ on a tree $\mathcal{T} = \langle T,\prec\rangle$, called a *Peircean tree model*. As usual, $V$ is a valuation that assigns to every atomic proposition $p \in {PROP}$ the set of time instants $V(p) \subseteq T$ at which $p$ is considered true. The *truth of an arbitrary formula φ of PBTL at a given time instant $t$ in a Peircean tree model $\mathcal{M}$* is then defined inductively. The semantic clauses for the truth-functional connectives $\neg$ and $\wedge$, the past operator $P$, and the strong future operator $G$ are as in TL (see Section 3.2), and we only provide the semantic clause for the new future operator $F$ here:

$$\begin{array}{ll} \mathcal{M},t\vDash F\varphi \quad \text{ iff } & \text{for all histories } h\in \mathcal{H}(t)\text{, there is some time } \\ & \text{instant } t'\in h \text{ such that } t\prec t' \text{ and } \mathcal{M},t'\vDash \varphi. \end{array}$$

Thus, according to the Peircean semantics, a formula of the form $F\varphi$ is true at an instant $t$ iff every history passing through $t$ contains some later instant $t'$ at which *φ* is true. The strong future operator $G$ implicitly contains universal quantification over histories and reads “it will necessarily always be the case that $\dots$”. The dual of $G$ is the original future operator of TL, which is now denoted by $f$, while the dual of the Peircean $F$ is commonly written $g$ (cf. Burgess 1980)[^burgess-1980]. Thus, all future operators involve (implicitly or explicitly) quantification over histories and are modalized: they express possibility and necessity regarding the future. There is no actual future and, accordingly, no notion of plain future truth. As this accords well with the view held by Peirce, Prior called this system ‘Peircean’.

In the Peircean temporal logic, the formula $\varphi \rightarrow HF\varphi$ is no longer valid: what is the case now need not have been necessary in the past. This blocks the Master Argument of Diodorus Chronus on Prior’s reconstruction, where the formula figures as an additional premise (see Prior 1967, Chapter 3.1)[^prior-1967]. Moreover, while Peirceanism preserves bivalence and the principle of excluded middle $\varphi \vee \neg\varphi$, it renders all formulae expressing future contingents false and hence invalidates the principle of future excluded middle $F\varphi \vee F\neg\varphi$. This principle is interpreted as saying that eventually either *φ* or $\neg\varphi$ will be the case and is usually judged intuitively valid (see e.g. Thomason 1970)[^thomason-1970].

A complete finite axiomatization of the Peircean branching time temporal logic was given by Burgess (1980)[^burgess-1980], using a version of the so-called Gabbay Irreflexivity Rule. Zanardo (1990)[^zanardo-1990] provides an alternative axiomatization, where the Gabbay Irreflexivity Rule is replaced by an infinite list of axioms. Decidability of Peirceanism was established in Burgess (1980)[^burgess-1980], too. Burgess’ (1980) axiomatization of PBTL is provided in the supplementary document:

> [Burgess’ Axiomatic System for PBTL](logic-temporal.pbtl.md)

### 5.3 The Ockhamist branching time temporal logic

While Prior favored Peirceanism, his alternative Ockhamist branching time temporal logic has become far more influential. In the Ockhamist branching time logic OBTL, truth is not only relativized to a time instant in the tree but also to one of the histories passing through that instant, and the future operator $F$ is evaluated along that given history. Thus, the intuitive meaning of $F$ becomes “*With respect to the given history*, it will be the case that $\dots$”. In addition to the temporal operators $F$ and $P$, the language of OBTL contains a modal operator $\Diamond$ and its dual $\Box$, which are interpreted as quantifiers over histories. Given a set of atomic propositions ${PROP}$, the set of formulae of OBTL can be recursively defined by

$$ \varphi := p \in {PROP}\mid \neg \varphi\mid (\varphi \wedge \varphi) \mid P\varphi \mid F\varphi \mid \Diamond\varphi. $$

In the Ockhamist semantics, these formulae will be evaluated in a model on a tree $\mathcal{T} = \langle T,\prec\rangle$ at pairs $(t,h)$ consisting of a time instant $t\in T$ and a history $h \in \mathcal{H}(t)$ containing that instant. Naturally, the question arises how to evaluate the atomic propositions in the model: do their truth values depend only on the given time instant, or do they depend on the history parameter as well? The answer to this question crucially hinges on whether atomic propositions may contain ‘traces of futurity’ or not (Prior 1967, 124)[^prior-1967]. There is no consensus on the treatment of atomic propositions in the literature (cf. Zanardo 1996)[^zanardo-1996], and Prior himself entertained the idea of a two-sorted language with two different kinds of atomic propositions that each require a different treatment (Prior 1967, Chapter 7.4)[^prior-1967]. Here we will allow the truth values of atomic propositions to depend on both the time instant and the history. The more specific case of instant-based propositions can be obtained by imposing the additional requirement that the scheme $p \leftrightarrow \Box p$ be valid for $p \in {PROP}$.

Thus, an *Ockhamist tree model* is a triple $\mathcal{M} = \left\langle T, \prec, V \right\rangle$ where $\mathcal{T} = \langle T,\prec\rangle$ is a tree and $V$ is a valuation that assigns to every atomic proposition $p\in {PROP}$ the set of admissible instant-history pairs $V(p) \subseteq T \times \mathcal{H}(\mathcal{T})$ at which $p$ is considered true. The *truth of an arbitrary formula φ of OBTL at a given instant-history pair $(t,h)$ in an Ockhamist tree model $\mathcal{M}$* is defined inductively as follows:

- $\mathcal{M},(t,h)\vDash p$   iff   $(t,h)\in V(p)$, for $p\in {PROP}$;
- $\mathcal{M},(t,h) \vDash \neg\varphi$   iff   $\mathcal{M},(t,h) \not\vDash \varphi$;
- $\mathcal{M},(t,h) \vDash \varphi \wedge \psi$   iff   $\mathcal{M},(t,h) \models \varphi$ and $\mathcal{M},(t,h) \vDash \psi$;
- $\mathcal{M},(t,h)\vDash P\varphi$   iff   $\mathcal{M},(t',h) \vDash \varphi$ for some time instant $t'\in h$ such that $t' \prec t$;
- $\mathcal{M},(t,h)\vDash F\phi$   iff   $\mathcal{M},(t',h)\models \phi$ for some time instant $t'\in h$ such that $t \prec t'$;
- $\mathcal{M},(t,h)\vDash \Diamond \varphi$   iff   $\mathcal{M},(t,h')\vDash \varphi$ for some history $h'\in \mathcal{H}(t)$.

The temporal operators are essentially interpreted as they are in linear temporal logic: the instant of evaluation is simply shifted backwards and forwards on the given history. Note that the requirement “$t'\in h$” is redundant in the semantic clause for the past operator $P$ as there is no backward branching. It is crucial, however, in the clause for the future operator $F$. As usual, the strong temporal operators $H$ and $G$ are defined as the duals of $P$ and $F$, respectively. The modal operators quantify over the set of histories passing through the current instant. The operator $\Diamond$ is an existential quantifier over that set and captures possibility, while its dual $\Box$ involves universal quantification and expresses ‘inevitability’ or ‘historical necessity’.

We say that a formula of OBTL is *Ockhamist valid* iff it is true at all admissible instant-history pairs in all Ockhamist tree models. Obviously, all temporal formulae that are valid in linear models of time are Ockhamist valid as well. Hence, Ockhamism validates the principle of future excluded middle $F\varphi \vee F \neg\varphi$ (under the assumption that time does not end) as well as the formula $\varphi \rightarrow HF\varphi$. It invalidates, however, the principle of the necessity of the past $P\varphi \rightarrow \Box P\varphi$, and thus, like Peirceanism, blocks Diodorus’ Master Argument, albeit for a different reason.

Whereas in the Peircean branching time logic PBTL future truth is modalized, in the Ockhamist branching time logic OBTL future truth and modality come apart. The Peircean formulae $F\varphi$ and $G\varphi$ are equivalent to the Ockhamist $\Box F\varphi$ and $\Box G\varphi$, respectively. In fact, PBTL can be regarded as a proper fragment of OBTL, namely the fragment that comprises all and only those formulae that are recursively built up from (instant-based) atomic propositions using truth-functional connectives and the combined modalities $\Box F$ and $\Box G$ (with their duals $\Diamond G$ and $\Diamond F$). In fact, the Peircean language is strictly less expressive than the Ockhamist one, lacking e.g. an equivalent for $\Diamond GF\varphi$ (for a proof, see Reynolds 2002)[^reynolds-2002].

By relativizing truth at an instant to a history in the tree, the Ockhamist branching time logic provides a notion of plain future truth. From a philosophical point of view, however, the relativization to a history is not entirely unproblematic. There are essentially two different ways to interpret the Ockhamist history parameter. First, one may think of it as referring to the actual course of events in the tree of possibilities, and since this idea meshes well with Ockham’s view on the future, Prior chose the label ‘Ockhamism’. This idea of an actual history has triggered a variety of so-called ‘Thin Red Line’ theories (for a discussion, see Belnap and Green 1994; Belnap et al. 2001; and Øhrstrøm 2009)[^belnap-1994][^belnap-2001][^øhrstrøm-2009]. Second, one may think of the history as an auxiliary parameter of truth that cannot be initialized in a context: the context of utterance uniquely determines the time instant of the utterance, but it cannot single out one of the histories passing through that instant if the future is genuinely open. This line of thought has given rise to ‘post-semantic’ accounts, which aim to bridge the gap between the recursive semantic machinery and a context by introducing a notion of *super-truth*, most notably Thomason’s supervaluationism (Thomason 1970)[^thomason-1970] and MacFarlane’s assessment-sensitive post-semantics (MacFarlane 2003; 2014)[^macfarlane-2003]. These accounts sacrifice bivalence, but they preserve the principles of excluded middle $\varphi \vee \neg\varphi$ and future excluded middle $F\varphi \vee F\neg\varphi$.

From a logical point of view, the Ockhamist approach to branching time strongly resembles the idea underlying the notion of a *$T\times W$ frame* and the more general notion of a *Kamp frame*, discussed in Thomason (1984)[^thomason-1984], as well as the definition of an *Ockhamist frame* introduced in Zanardo (1996)[^zanardo-1996]. These kinds of frames build on a non-empty set of possible worlds, each of which is endowed with an internal linear temporal structural, and assume a time-relative, historical accessibility relation between possible worlds. That is, overlap of histories is replaced by accessibility, and possible worlds are considered primitive elements, whereas in branching time histories are defined in terms of instants. As a consequence, if we merge a frame consisting of historically related possible worlds into a tree, new histories may emerge that do not correspond to any of the possible worlds (for the construction, see e.g. Reynolds 2002)[^reynolds-2002].

Technically, the difference between a possible worlds based approach and a branching time based approach can be overcome by equipping branching time structures with a primitive set of histories that is rich enough to cover the entire structure, a so-called *bundle*. A *bundled tree* is defined as a triple $\langle T,\prec,\mathcal{B}\rangle$ where $\mathcal{T} = \langle T,\prec\rangle$ is a tree and the bundle $\mathcal{B} \subseteq \mathcal{H}(\mathcal{T})$ is a non-empty set of histories such that every instant in $\mathcal{T}$ belongs to some history in $\mathcal{B}$ (Burgess 1978; 1980)[^burgess-1978]. The Ockhamist semantics straightforwardly generalizes to bundled trees, with the only difference being that quantification over histories is now restricted to histories from the bundle. Bundled tree validity is equivalent to Kamp validity (Zanardo 1996; Reynolds 2002)[^reynolds-2002][^zanardo-1996], but weaker than full Ockhamist validity. Reynolds (2002)[^reynolds-2002] provides the following example of a formula that is Ockhamist valid but falsifiable in bundled trees (assuming instant-based atomic propositions); further counterexamples were provided in e.g. Burgess 1978 and Nishimura 1979: $$\Box G(p \to \Diamond F p) \to \Diamond G(p \to F p).$$ Intuitively, the antecedent of this formula allows one to construct a ‘limit history’ in which $p$ always holds. Such limit histories may be omitted in bundled trees, which gave rise to philosophical discussions concerning the adequacy of those frames (see e.g. Nishimura 1979; Thomason 1984; and Belnap et al. 2001)[^belnap-2001][^nishimura-1979][^thomason-1984].

A complete axiomatization for bundled tree validity is given in Zanardo (1985)[^zanardo-1985] and Reynolds (2002; 2003)[^reynolds-2002][^reynolds-2003]. Finding a complete axiomatization for Ockhamist validity turned out to be more difficult. It has been shown that the class of Ockhamist trees is not definable in the class of bundled trees (Zanardo et al. 1999)[^zanardo-1999]. In Reynolds (2003)[^reynolds-2003], an axiomatization for Ockhamist validity is proposed and a completeness proof sketched. In this system, the problem of emergent histories is dealt with by an infinite axiom scheme based on the formula given above. The full proof, however, has never appeared in print, and so the problem appears to be still open. Moreover, bundled tree validity is known to be decidable (see Burgess 1979)[^burgess-1979]. The same holds for Ockhamist validity, under the assumption of instant-based atomic propositions (see Gurevich and Shelah 1985a; 1985b; and Reynolds 2002)[^gurevich-1985a][^reynolds-2002]. We are not aware of results establishing decidability or undecidability of Ockhamist validity with history-dependent atomic propositions. Reynolds’ (2003) axiomatization for bundled tree validity and his proposed extension to Ockhamist validity is provided in the supplementary document:

> [Reynolds’ Axiomatic System for OBTL](logic-temporal.obtl.md)

Recently, generalizations of the Ockhamist branching time logic have been proposed, replacing the Ockhamist history parameter by a *set of histories*. In Zanardo (1998)[^zanardo-1998], trees $\mathcal{T} = \langle T,\prec\rangle$ are equipped with an indistinguishability function that assigns to each time instant a partition of the set of histories passing through that instant, and truth at an instant is relativized to one such indistinguishability cell, i.e. to a set of histories. For details, see Zanardo (1998)[^zanardo-1998] and Ciuni and Zanardo (2010). An account that is similar in spirit is the *transition semantics* presented in Rumberg (2016)[^rumberg-2016]. In that framework, possible courses of events are construed as chains of local future possibilities, viz. transitions, and can be extended towards the future. Transition semantics introduces a second local perspective in time, which — unlike Zanardo’s (1998)[^zanardo-1998] indistinguishability cells — can be shifted independently of the time instant and which — unlike MacFarlane’s (2003; 2014)[^macfarlane-2003][^macfarlane-2014] postsemantic moment of assessment — is incorporated in the semantics proper. The language contains a so-called stability operator that allows one to capture how the truth value of a formula about the future at an instant changes in the course of time. For details, see Rumberg (2016; 2019)[^rumberg-2016][^rumberg-2019][^rumberg-2019-2] and Rumberg and Zanardo (2019). Both the branching time logic with indistinguishability functions and the transition approach subsume Peirceanism and Ockhamism as limiting cases, namely the cases where the set of histories taken into account in the semantic evaluation is a singleton, resp. the set of all histories passing through the given instant. A brief overview of the transition based approach is presented in the supplementary document:

> [Transition Semantics](logic-temporal.transition-semantics.md)

### 5.4 The computation tree logics CTL and CTL\*

Branching time logics are extensively used in computer science. The most popular ones are the computation tree logics CTL and CTL\*, which are variants of the Peircean and the Ockhamist branching time temporal logics, respectively. They are interpreted on the class of so-called *computation trees*, where every history has the order type of the natural numbers. These trees are naturally obtained as tree unfoldings of discrete transition systems and represent the possible infinite computations arising in such systems. As usual in computer science, they are based on the reflexive closure of the precedence relation $\prec$. While CTL historically preceded CTL\*, nowadays CTL is often viewed as a fragment of CTL\*, and we follow this convention here.

The *full computation tree logic* CTL\* is the computational variant of Ockhamism, and it was introduced by Emerson and Halpern (1985). The language of CTL\* contains (the reflexive versions of) the future operators $G$ and $U$ (*Until*) as well as the *Next Time* operator $X$ (no past operators), which are now interpreted on computation trees. As in the general Ockhamist branching time logic, the evaluation is relativized to both an instant (here called a *state*) and a history (here called a *computation path*, or just a *path*). We note that in computer science usually instant-based atomic propositions are assumed, i.e., the evaluation of the atomic propositions depends only on the state.

The *computation tree logic* CTL is the computational variant of Peirceanism, and it was introduced by Emerson and Clarke (1982). CTL is the fragment of CTL\* where each of the temporal operators $G$, $U$, and $X$ is immediately preceded by a modal operator, $\Box$ or $\Diamond$, here usually denoted by the path quantifiers $\forall$ and $\exists$. That is, the language of CTL is recursively built up using the combined modalities $\forall G\varphi$, $\forall(\varphi U\psi)$, $\forall X\varphi,$ and $\exists G\varphi$, $\exists(\varphi U\psi)$, $\exists X\varphi$. A precursor of CTL is the logic UB, introduced by Ben-Ari et al. (1983), in which $U$ does not occur.

The logic CTL became widely used owing to its good computational properties with regard to *model checking*, having linear complexity both in the size of the input formula and in the size of the input model (as finite transition system). However, CTL is not always sufficiently expressive, which led to its extension CTL\*. The logic CTL\* is much more expressive and subsumes the linear time temporal logic LTL, but it has higher complexities of model checking (PSPACE) and of deciding satisfiability (2EXPTIME). For further details and proofs of decidability, see Emerson and Sistla (1984); Emerson and Halpern (1985); Emerson (1990)[^emerson-1990]; Goldblatt (1992)[^goldblatt-1992]; Stirling (1992)[^stirling-1992]; Gabbay et al. (1994); Finger et al. (2002); and Demri et al. (2016).

A complete axiomatization of CTL can be obtained by replacing the axioms of LTL by their path-quantified versions. For proofs of completeness, see Emerson (1990)[^emerson-1990] and Goldblatt (1992)[^goldblatt-1992]. For CTL\* more axioms must be added to account for the interaction of temporal and modal operators and to enforce the limit closure property of trees. A complete axiomatization for CTL\* was obtained by Reynolds (2001)[^reynolds-2001], and a completeness result for the extension of CTL\* with past operators was established in Reynolds (2005)[^reynolds-2005]. For more on CTL and CTL\*, see Demri et al. (2016). A sketch of the axiomatic system for CTL is included in the supplementary document:

> [An Axiomatic System for CTL](logic-temporal.axiomatic-ctl.md)

## 6. Interval temporal logics

Instant-based and interval-based models of time introduce two different temporal ontologies, and even though they are technically reducible to each other, this does not solve the semantic issue: should propositions about time be interpreted as referring to time instants or to intervals?

There have been various explorations of interval-based temporal logics in the philosophical logic literature. Important early contributions include Hamblin (1972)[^hamblin-1972]; Humberstone (1979)[^humberstone-1979]; Röper (1980)[^röper-1980]; and Burgess (1982b)[^burgess-1982b]. The latter provides an axiomatization for an interval-based temporal logic with a precedence relation between intervals on the rationals and the reals. The interval-based approach to temporal reasoning has been very prominent in Artificial Intelligence. Some notable works here include Allen’s (1984)[^allen-1984] logic of planning, Kowalski and Sergot’s (1986) calculus of events, and Halpern and Shoham’s (1986) modal interval logic. It also features in some applications in computer science, such as *real-time logics* and *hardware verification*, notably Moszkowski’s (1983)[^moszkowski-1983] interval logic and Zhou, Hoare, and Ravn’s duration calculus (see Hansen and Zhou 1997)[^hansen-1997].

Here we briefly present the propositional modal-logic style approach proposed by Halpern and Shoham (1986), hereafter called $\mathsf{HS}.$ The language of $\mathsf{HS}$ includes a family of unary interval operators of the form $\langle X\rangle,$ one for each of Allen’s interval relations over linear time. The respective notations are listed in Table 1 (Section 2.2). Given a set of atomic propositions $PROP$, formulae are recursively defined by the following grammar: $$\varphi := p \in {PROP} \mid \neg \varphi \mid (\varphi \wedge \varphi) \mid \langle X\rangle\varphi.$$

The interval logic $\mathsf{HS}$ starts from instant-based models over linear time, and intervals are considered defined elements. Let $\mathcal{T} = \langle T,\prec\rangle$ be a temporal frame with a precedence relation $\prec$ that induces a strict linear order on the set of time instants $T$. An *interval* in $\mathcal{T}$ is defined as an ordered pair $[a,b]$ such that $a,b\in T$ and $a\leq b.$ The set of all intervals in $\mathcal{T}$ is denoted by $\mathbb{I}(\mathcal{T)}.$ Note that the definition allows for ‘point intervals’ whose beginning and end points coincide, following the original proposal by Halpern and Shoham (1986). Sometimes only ‘strict’ intervals are considered.

Crucially, in interval-based temporal logic, formulae are evaluated relative to time intervals rather than instants. An *interval model* is a triple $\mathcal{M} = \langle T,\prec,V\rangle$ consisting of a strict linear temporal frame $\mathcal{T} = \langle T,\prec\rangle$ and a valuation $V$ that assigns to each atomic proposition $p\in{PROP}$ the set of time intervals $V(p) \subseteq \mathbb{I}(\mathcal{T})$ at which $p$ is considered true. The *truth of an arbitrary formula φ at a given interval $[a,b]$ in an interval model $\mathcal{M}$* is defined by structural induction on formulae as follows:

- $\mathcal{M},[a,b] \models p$   iff   $[a,b]\in V(p)$, for $p \in {PROP};$
- $\mathcal{M},[a,b] \models \neg\varphi$   iff   $\mathcal{M},[a,b] \not\models \varphi;$
- $\mathcal{M},[a,b] \models \varphi \wedge \psi$   iff   $\mathcal{M},[a,b] \models \varphi$ and $\mathcal{M},[a,b] \models \psi;$
- $\mathcal{M},[a,b] \models \langle X\rangle\varphi$   iff   $\mathcal{M},[c,d] \models \varphi$ for some interval $[c,d]$ such that $[a,b]R_{X}[c,d]$, where $R_X$ is Allen’s interval relation corresponding to the modal operator $\langle X\rangle$ (cf. Table 1).

That is, the new interval operators are given a Kripke-style semantics over the associated Allen relations. E.g., for the Allen relation “meets”, we have:

$$ \mathcal{M},[t_{0},t_{1}] \models \langle A\rangle \varphi \text{ iff } \mathcal{M},[t_{1},t_{2}] \models \varphi \text{ for some interval } [t_{1},t_{2}]. $$

For each diamond modality $\langle X\rangle,$ the corresponding box modality is defined as its dual: $[X] \varphi \equiv \neg \langle X\rangle \neg \varphi.$ Sometimes it is useful to include an additional modal constant for point intervals, denoted $\pi,$ with the following truth definition:

$$ \mathcal{M},[a,b]\models\pi \ \text{ iff } \ a=b. $$

Some of the $\mathsf{HS}$ modalities are definable in terms of others, and both for the semantics with and without point intervals, minimal fragments have been identified that are expressive enough to define all other operators. Complete sets of equivalences that capture the interdefinability of some $\mathsf{HS}$ modalities are presented in the supplementary document:

> [Interdefinability of $\mathsf{HS}$ Modalities](logic-temporal.interdefine-hs.md)

The logic $\mathsf{HS}$ has over a thousand expressively non-equivalent fragments involving only some of the modal operators (see Della Monica et al. 2011 for a survey)[^della-2011]. Most of its fragments are very expressive, and the respective notions of validity are usually undecidable (under some additional assumptions even highly undecidable, viz. $\Pi^{1}_{1}$-complete). However, some non-trivial decidable fragments of HS have been identified. The probably best studied one is the *neighborhood interval logic*, which involves the operators $\langle A \rangle$ and $\langle\overline{A}\rangle$ (Goranko et al. 2003)[^goranko-2003]. An example of an axiom for $\langle A\rangle$ is $\langle A \rangle\langle A \rangle\langle A \rangle p \to \langle A \rangle\langle A \rangle p,$ saying that any two consecutive right-neighboring intervals can be joined into one right-neighboring interval.

In addition to the unary $\mathsf{HS}$ interval modalities associated with Allen’s binary interval relations, some operators of higher arity naturally arise. For instance, there is the operation of chopping an interval into two subintervals, which gives rise to the ternary interval relation ‘chop’, proposed and studied in Moszkowski (1983)[^moszkowski-1983] and extended in Venema (1991)[^venema-1991] to the logic CDT, which involves next to ‘chop’ ($C$), the two residual ‘chop’ operators $D$ and $T.$ The logic CDT was completely axiomatized in Venema (1991)[^venema-1991]; see also Goranko et al. (2004) and Konur (2013)[^konur-2013].

There is a natural spatial interpretation of interval temporal logics, based on the idea that the pairs that define an interval on a linear order $L$ can be considered coordinates of a point in the $L \times L$-plane. Relations between intervals are then interpreted as spatial relations between the relevant points. This interpretation has been fruitfully used to transfer various technical results between interval and spatial logics, such as undecidability, see e.g. Venema (1990)[^venema-1990] and Marx and Reynolds (1999).

Lastly, a few words about the relationship between interval temporal logics and first-order logic. The standard translation of Prior’s basic tense logic TL into first-order logic (presented in Section 3.3) extends naturally to interval logics, where atomic propositions are represented in the first-order language by binary relations. It turns out that some fragments of $\mathsf{HS}$ can be translated into the two-variable fragment FO$^{2}$ of first-order logic, which eventually implies their decidability. The expressively strongest such interval logic is the neighborhood interval logic, proven to be expressively complete for FO$^{2}$ (Bresolin et al. 2009)[^bresolin-2009]. Other fragments of $\mathsf{HS}$ require at least three distinct variables for the standard translation. But even the full logic $\mathsf{HS}$ is less expressive than the three-variable fragment FO$^{3}$ of first-order logic, for which Venema (1991)[^venema-1991] showed that the logic CDT is expressively complete.

For more on interval temporal logics, see Halpern and Shoham (1986); Venema (1990)[^venema-1990]; Goranko et al. (2003; 2004); Della Monica et al. (2011); the survey Konur (2013)[^konur-2013], and the references therein.

## 7. Other variants of propositional temporal logics

So far we have discussed the traditional family of propositional temporal logics, but there are numerous variations and alternative developments that provide useful formalisms for various applications. We briefly present some of them here: hybrid temporal logics, metric and real-time temporal logics, and quantified propositional logics.

### 7.1 Hybrid temporal logics

A notable family of temporal logics, enriching the traditional framework, are *hybrid temporal logics*, which combine propositional temporal logic with elements of first-order logic and thereby considerably increase the expressive power of the language.

The most important notion in hybrid temporal logics is that of a *nominal*. Nominals are special atomic symbols: they are considered to be true at exactly one instant of the temporal model. Hence, one can think of a nominal $a$ as saying “It is $a$ o’clock now”. For this reason, nominals are sometimes also called ‘clock variables’. The idea of nominals can be traced back to Prior (1967, Chapter V; 1968, Chapter XI), who considered the possibility of identifying instants with instant-propositions: an instant can be conceived of as the conjunction of all those propositions that are true at that instant. The first mathematical exploration of hybrid temporal logic was given in Bull (1970)[^bull-1970]. In addition to nominals, hybrid languages are often augmented by further syntactic mechanisms, such as satisfaction operators, quantifiers over nominals, and reference pointers, which we briefly discuss below. Satisfaction operators and quantifiers over nominals can already be found in Prior’s work (see Blackburn 2006)[^blackburn-2006] and were reinvented independently in Passy and Tinchev (1985). Reference pointers were introduced only much later in Goranko (1996)[^goranko-1996], and a similar referencing mechanism is found in Alur and Henzinger (1994).

- *Satisfaction operators*: The satisfaction operator $@_{i}$ allows one to express that a given formula is true at the time instant denoted by the nominal $i$. That is, $\mathcal{M},t\vDash @_{i}\varphi$ iff $\mathcal{M},V(i)\vDash \varphi,$ where $ V(i)$ is the unique instant where $i$ is true. The notion of truth at an instant of a temporal model is imported into the object-language.
- *Quantifiers over nominals*: The nominal quantifier $\forall i$ expresses that a formula is true at the given time instant no matter which instant the nominal $i$ denotes. More formally, $\mathcal{M},t\vDash \forall i\varphi$ iff $\mathcal{M}_{[i\rightarrow s]},t\vDash \varphi$ for any instant $s$ in $\mathcal{M},$ where $\mathcal{M}_{[i\rightarrow s]}$ is the model obtained from $\mathcal{M}$ by re-assigning the denotation of $i$ to be $s.$ The full power of first-order quantification is brought into the temporal language, while many of its propositional virtues are preserved.
- *Reference pointers*: Reference pointers $\downarrow_{i}$ (also known as ‘binders’) provide a mechanism for referring to the current time instant, i.e. saying ‘now’. A formula $\downarrow_{i}\varphi$ is true at a given instant $t$ iff *φ* is true at $t$ when all occurrences of the nominal $i$ in *φ* denote $t$. That is, $\mathcal{M},t\vDash \downarrow_{i}\varphi$ iff $\mathcal{M}_{[i\rightarrow t]},t\vDash \varphi$.

Other operators that can be considered hybrid temporal logic operators are the *universal modality*, the *difference modality*, and *propositional quantifiers*. The universal modality $A$ says that a given formula is true at every instant of the temporal model and hence captures the notion of validity in a model: $\mathcal{M},t\vDash A\varphi$ iff $\mathcal{M}\vDash\varphi$. The difference modality $D$, on the other hand, states that the given formula is true at some other instant. Note that both modalities abstract away from the underlying accessibility relation. Propositional quantifiers $\forall p$ introduce second-order quantification into the propositional language, and we discuss them in Section 7.3 below.

Hybrid languages are very expressive. Here are just two examples:

- Irreflexivity of the precedence relation, which is not expressible in TL, can be expressed in a language with nominals by $i \rightarrow \neg Fi$ or with the help of the satisfaction operator by $@_{i}\neg Fi.$
- The operators $S$ and $U$ are definable in a language with nominals and reference pointers: $\varphi U\psi :={\downarrow _{i}}F(\psi \wedge H(Pi\rightarrow \varphi))$, and likewise for $S.$

While the weaker versions of hybrid logics — with nominals, satisfaction operators, universal modality, and difference modality — are still decidable, the more expressive ones — with quantifiers over nominals or reference pointers — are usually undecidable. For details, see Goranko (1996)[^goranko-1996]; and Areces and ten Cate (2007).

Branching time versions of hybrid temporal logics have been investigated as well. For an overview of varieties of hybrid temporal logics and their historical development, see Blackburn (1993)[^blackburn-1993]; Gargov and Goranko (1993); Blackburn and Seligman (1995), Blackburn and Tzakova (1999) and the entry on hybrid logic.

### 7.2 Metric and real-time temporal logics

Metric temporal logics go back to Prior, too (see Prior 1967, Chapter VI)[^prior-1967]. He used the notation $Pn\varphi$ for “It was the case the interval $n$ ago that *φ*” (i.e. *φ* was the case $n$ time units ago) and $Fn\varphi$ for “It will be the case the interval $n$ hence that *φ*” (i.e *φ* will be the case $n$ time units hence). These operators presuppose that time has a certain metric structure and can be carved up into temporal units, which may be associated with clock times (e.g. hours, days, years, etc.). If the relevant units are days, for example, the operator $F 1$ reads ‘the following day’ (or just ‘tomorrow’).

Prior noted that $P n\varphi$ can be defined as $F(-n)\varphi.$ The case $n=0$ accordingly amounts to the present tense. The metric operators validate combination principles such as:

$$FnFm\varphi \rightarrow F(n+m)\varphi.$$

The interrelation of the metric and non-metric versions of the temporal operators is captured by the following equivalences:

$$\begin{matrix} P\varphi \equiv \exists {n}({n} \lt 0 \land Fn\varphi) & F\varphi \equiv \exists n(n \gt 0 \land Fn\varphi) \\ H\varphi \equiv \forall {n}({n} \lt 0 \rightarrow Fn\varphi) & G\varphi \equiv \forall n(n \gt 0 \rightarrow Fn\varphi). \end{matrix}$$

Instant-based temporal logics for metric time are studied in e.g. Rescher and Urquhart (1971, Chapter X); Montanari (1996)[^montanari-1996][^montanari-1996-2]; and Montanari and Policriti (1996). For metric interval logics, see Bresolin et al. (2013).

Various metric extensions of temporal logics over the structure of the real numbers have been proposed, giving rise to so-called *real-time* logics. These logics introduce additional operators, such as the following, which enable different formalizations of the sentence “whenever $p$ holds in the future, $q$ will hold within three time units later”:

- time-bounded operators, e.g.: $G(p \to F_{_{\leq 3}} q);$
- freeze quantifiers (similar to hybrid logic reference pointers), e.g.: $Gx. (p \to Fy. (q \land y\leq x+3));$
- quantifiers over time variables, e.g.: $\forall x G(p \land t=x \to F(q \land t\leq x+3)).$

Such real-time extensions are usually very expressive and often lead to logics with undecidable decision problems. A way to regain decidability is to relax “punctuality” requirements involving precise time durations by requirements involving time intervals. For details, see e.g. Koymans (1990)[^koymans-1990]; Alur and Henzinger (1992; 1993; 1994) as well as Reynolds (2010; 2014)[^reynolds-2010][^reynolds-2014] on the real-time linear temporal logic RTL, and the survey Konur (2013)[^konur-2013].

### 7.3 Quantified propositional temporal logics

Propositional temporal logics can be extended with quantifiers over atomic propositions. For example, the formula $F\forall p(p \rightarrow Fp)$ can be used to express that there is a future time such that everything that is the case then will again be the case in the future (see Rescher and Urquhart 1971, Chapter XIX)[^rescher-1971]. Set-theoretically, such quantifiers range over all valuations of the respective atomic propositions and hence are tantamount to monadic second-order quantifiers. The resulting languages are very expressive, and the respective logics are usually undecidable (often not even recursively axiomatizable). Notable extensions include the logic QPTL, the quantified propositional version of LTL (which is decidable albeit with non-elementary complexity), as well as the extension of CTL\* (see French 2001)[^french-2001]. Complete axiomatic systems and decidability results for the quantified propositional temporal logic QPTL (with and without past operators) have been presented in Kesten and Pnueli (2002) and French and Reynolds (2003)[^reynolds-2003]. See also Fritz (2024)[^fritz-2024] for a systematic study of modal logics with propositional quantification.

## 8. First-order temporal logics

Objects exist in time, and they change their properties over time. Propositional temporal logics are not expressive enough to capture this aspect of the world: all that is associated with a time instant is a set of unstructured atomic propositions that are considered true there. What is needed is a more fine-grained model of the temporal history of the world, with objects that may have certain properties and stand in certain relations. Accordingly, in addition to temporal operators, the language should contain names for objects, variables and quantifiers ranging over objects, as well as predicates for denoting properties and relations. This is what first-order temporal logics provide.

### 8.1 Existence and quantification in time

Existence in time is an important topic in the philosophy of time. Usually, objects come into being at one point in time and go out of being at some later time. But what is it for an object to exist in time? Do only present objects exist, as a *presentist* would hold, or is existence to be understood in a broader sense comprising past and future objects as well, as an *eternalist* would say? The controversy between *presentism* and *eternalism* is accompanied by a debate on *persistence*, that is, on the question how objects exist through time. Are objects wholly present at each instant at which they exist — a view known as *endurantism* — or do they persist by having different temporal stages at different instants in time — a view called *perdurantism*? For a detailed overview of these debates, see e.g. Dyke and Bardon (2013); Meyer (2013)[^meyer-2013]; Correia and Rosenkranz (2018), as well as the entries on [time](https://plato.stanford.edu/entries/time/), [temporal parts](https://plato.stanford.edu/entries/temporal-parts/), and [identity over time](https://plato.stanford.edu/entries/identity-time/).

Similar questions arise in the context of first-order temporal logics, albeit under a different guise. Issues concerning existence in and identity over time reveal themselves in the interaction of temporal operators and individual quantifiers. For example, the sentence “A philosopher will be a king” can be interpreted in several different ways:[^note-6]

- $\exists {x}(philosopher({x})\land {F} \, king({x}))$ *Someone who is now a philosopher will be a king at some future time.*
- $\exists {x}{F} (philosopher({x})\land king({x}))$ *There now exists someone who will at some future time be both a philosopher and a king.*
- ${F} \exists {x}(philosopher({x})\land {F}\, king({x}))$ *There will exist someone who is a philosopher and later will be a king.*
- ${F} \exists {x}(philosopher({x})\land king({x}))$ *There will exist someone who is at the same time both a philosopher and a king.*

All of the above readings presuppose that the domain of quantification is relative to a time instant and that the same individual may exist at multiple times. To accommodate this idea, we need to equip our models with a *local domain* of objects ${D}({t})$ at each time instant $t$, restrict the range of the individual quantifiers to that domain, and incorporate a mechanism that enables us to identify an object across different times.

Moreover, the example suggests that the local domain at a given time instant contains exactly those individuals that do in fact exist at that instant. However, there are alternative ways of understanding the local domains associated with time instants, which mirror different conceptions of existence in time. Here are four natural options:

1. The first view corresponds to the view sketched above: objects come into being at one point in time and go out of being at a later time, i.e., they exist only over a certain period of time. This idea can be captured formally by assuming that the local domains are constituted solely by the present objects. The local domains accordingly vary over time.
2. Objects actually exist only over a period of time, but they remain in the temporal history of the world once they have ceased to exist. On this account, the local domains include not only the present objects but all past objects as well; they increase as time progresses and new objects come into being.
3. Alternatively, one may hold that all objects that will ever exist are initially part of the temporal history of the world but drop out once they have ceased to exist. That is, the local domains comprise all present and future objects; they decrease as time progresses and objects go out of being.
4. Past, present, and future objects likewise exist. This is the notion of existence in an eternalist sense. One way to formally capture this idea is by stipulating that the local domains contain all objects that are part of the temporal history of the world. Hence, they are constant over time.

A conceptually different but technically closely related issue concerns the range of quantification. What do we quantify over in a temporal setting?

- Only over those objects that exist at the current time instant, as presupposed in the above example?
- Over all present, past, and future objects in the temporal history of the world?

Adopting the terminology ‘actualist quantification’ and ‘possibilist quantification’ by Fitting and Mendelsohn (2023) to the temporal case, we may refer to the first kind of quantification as *presentist quantification* and use the term *eternalist quantification* for the latter. Depending on the choice between these options, the sentence “Every human is born after 1888” comes out true or false. It is true if we quantify over only those humans that are currently alive, but it is false if we quantify over all humans in the temporal history of the world, including those that have ever lived. A further issue concerns fictitious entities, such as Santa Claus or Pippi Longstocking, which do not really exist at any time instant. Still, they may be said to exist in a broader sense, and one may want to include them in the domain of quantification. We set this issue aside here and refer the reader to the entry on free logic, which is a logic that allows reference to non-existing entities (cf. also Section 8.6).

Many of the questions concerning the interrelation of existence and quantification arising here correspond to well known problems in modal first-order logics, where an extensive discussion on these issues started already with Frege and Russell and peaked in the 1940s-1950s in the works of R. Barcan-Marcus, R. Carnap, W. Quine, R. Montague, and others (see the entry on [modal logic](https://plato.stanford.edu/entries/logic-modal)). A central theme in first-order modal logics is the validity or invalidity of the so-called Barcan formula. In a temporal setting, a version of the formula (referring to the future) can be glossed as follows: “If at some time in the future there will be something that is $Q$, then there is something now that will be $Q$ at some time in the future.” Whether this statement is guaranteed to be true crucially depends on how the local domains at the various instants in time are construed and what our quantifiers range over. Furthermore, temporal logic yields two versions of the Barcan formula, one for the future and one for the past.

### 8.2 The language and models of FOTL

A basic language of first-order temporal logic (FOTL) is an extension of a given first-order language by the operators $P$ and $F$. Whereas in propositional temporal logics atomic propositions are considered unstructured entities, in first-order temporal logics atomic formulae are built up from terms denoting individuals and predicate symbols denoting properties and relations. In addition, the language usually contains quantifiers ranging over individuals. (A brief overview of plain first-order logic is provided in the supplementary document [First-order Relational Structures and Languages](logic-temporal.1st-order-relational.md).) In what follows, we consider FOTL over a relational first-order language (no function symbols) with individual quantifiers and equality. The set of formulae is defined as follows:

$$\varphi \ \ := \ R(\tau_1,\dots,\tau_n) \ | \ \tau_1 = \tau_2 \ | \ \neg \varphi \ | \ (\varphi \land \varphi) \ | \ \forall x \varphi \ | \ P \varphi \ | \ F \varphi, $$

where $R(\tau_1,\dots,\tau_n)$ and $\tau_1 = \tau_2$ are atomic formulae. The truth functional connectives $\vee, \rightarrow$, and $\leftrightarrow$, the logical constants $\top$ and $\bot$, as well as the temporal operators $H$ and $G$ can be defined as usual. Moreover, the dual $\exists$ of $\forall$ is defined by $\exists x \varphi := \neg \forall x \neg \varphi$.

The models of FOTL are based on temporal frames, where each time instant is associated with a first-order relational structure. Formally, a *first-order temporal model* is a quintuple $\mathcal{M}= \langle T, \prec,\mathcal{U},D,\mathcal{I}\rangle$ where:

- $\mathcal{T}= \left\langle T, \prec \right\rangle$ is a temporal frame;
- $\mathcal{U}$ is the *global domain (universe)* of the model;
- $D: T \to \mathcal{P}(\mathcal{U})$ is a *domain function* that assigns to each time instant $t\in T$ a *local domain* $D_{t} \subseteq \mathcal{U}$ such that $\mathcal{U}= \bigcup_{t\in T}D_t$.[^note-7]
- $\mathcal{I}$ is an *interpretation function* that assigns for each time instant $t\in T$:
- an object $\mathcal{I}_{t}(c) \in \mathcal{U}$ to each constant symbol $c$;
- an $n$-ary relation $\mathcal{I}_{t}(R) \subseteq \mathcal{U}^{n}$ to each $n$-ary predicate symbol $R$. Note that even though the interpretations of the constant and predicate symbols are defined locally in that they are relativized to a given time instant, their extensions range over the global domain. This approach allows for reference to objects that do not currently exist and enables a proper treatment of cross-temporal relations, as, for example, in the sentence “One of my friends is a descendant of a follower of William the Conqueror”.

The quadruple $\mathcal{F} = \langle T,\prec,\mathcal{U},D\rangle$ is called the *augmented temporal frame* (or the *skeleton*) of the model $\mathcal{M}$. Since the model is supposed to represent the temporal history of the world, the local domains associated with the different time instants in the underlying augmented temporal frame must be suitably connected. There are four natural cases to be distinguished, which relate back to the four notions of existence discussed in Section 8.1 above:

1. *varying domains*: no restrictions apply;
2. *expanding (increasing) domains*: for all $t,t' \in T$, if $t \prec t',$ then $D_{t} \subseteq D_{t'}$;
3. *shrinking (decreasing) domains*: for all $t,t' \in T$, if $t \prec t',$ then $D_{t'} \subseteq D_{t}$;
4. *locally constant domains*: for all $t,t' \in T$, if $t \prec t',$ then $D_{t} = D_{t'}$.

Thus, an augmented temporal frame $\mathcal{F}$ has locally constant domains if and only if it has both expanding and shrinking domains. We say that $\mathcal{F}$ has *a constant domain* if all local domains equal the global domain. Note that, since the global domain is required to be the union of all local domains, having locally constant domains implies having a constant domain just in case the set of time instants forms a temporally connected structure.

### 8.3 Semantics of FOTL

There is a variety of semantics for first-order modal logics, which can be adapted to first-order temporal logics, including counterpart semantics, bundle semantics, metaframe semantics, admissible sets semantics, etc. We present here the temporal versions of the standard semantics for first-order modal logic as provided in Fitting and Mendelsohn (2023).

As in propositional temporal logic, formulae of FOTL are evaluated locally at time instants. However, since FOTL formulae may contain variables, their evaluation at a given time instant in a first-order temporal model depends also on a variable assignment. Let us denote the set of individual variables of FOTL by $\mathrm{VAR}$ and the set of individual terms (i.e. variables and constants) by $\mathrm{TERM}$. Given a first-order temporal model $\mathcal{M}= \langle T, \prec,\mathcal{U},D,\mathcal{I}\rangle$, a *variable assignment in $\mathcal{M}$* is a mapping $v: \mathrm{VAR} \to \mathcal{U}$ that assigns to each variable $x \in \mathrm{VAR}$ an object $v(x)$ in the global domain $\mathcal{U}$. Such an assignment can be uniquely extended to a time-relative *term valuation* as follows: $$v_{t}(x) := v(x), \ v_{t}(c) := \mathcal{I}_{t}(c). $$ While variable assignments are constant across time, the interpretation of the constant symbols depends on the respective time instant. (Versions where variables are evaluated locally as well have also been studied, see e.g. Gabbay et al. 2009.)[^gabbay-2009]

The *truth of an arbitrary formula φ of FOTL at a given time instant $t$ in a first-order temporal model $\mathcal{M}$ with respect to a variable assignment $v$* (denoted $\mathcal{M},t \models_{v} \varphi$) is now defined inductively as follows:

- $\mathcal{M},t \models_{v} R(\tau_{1},\ldots,\tau_{n})$   iff   $\langle v_{t}(\tau_{1}),\ldots,v_{t}(\tau_{n})\rangle \in \mathcal{I}_{t}(R)$, for any $n$-ary predicate symbol $R$ and terms $\tau_{1},\ldots,\tau_{n} \in \mathrm{TERM}$;
- $\mathcal{M},t \models_{v} \tau_{1}=\tau_{2}$   iff   $v_{t}(\tau_1) = v_{t}(\tau_2)$, for any terms $\tau_{1},\tau_{2} \in \mathrm{TERM}$;
- $\mathcal{M},t \models_{v} \lnot \varphi$   iff   $\mathcal{M},t\not\models_{v} \varphi$;
- $\mathcal{M},t\models_{v} \varphi \land \psi$   iff   $\mathcal{M},t\models_{v} \varphi$ and $\mathcal{M},t\models_{v} \psi$;
- $\mathcal{M},t\models_{v} P \varphi$   iff   $\mathcal{M},t'\models_{v} \varphi$ for some $t'\in T$ such that $t' \prec t$;
- $\mathcal{M},t\models_{v} F \varphi$   iff   $\mathcal{M},t'\models_{v} \varphi$ for some $t'\in T$ such that $t \prec t'$;
- $\mathcal{M},t\models_{v} \forall x \varphi$   iff   …
- *presentist quantification*: …$\mathcal{M},t\models_{v[a/x]} \varphi$ for every $a\in D_{t}$;
- *eternalist quantification*: …$\mathcal{M},t\models_{v[a/x]} \varphi$ for every $a\in \mathcal{U}$, where $v[a/x]$ is the variant of the variable assignment $v$ that assigns to the variable $x$ the object $a$, i.e. $v[a/x](x) = a$.

As we mentioned earlier, there are two natural approaches to quantification in temporal logic: *presentist quantification* and *eternalist quantification*. Technically, presentist quantification amounts to quantification over the *local* domain at the given time instant, whereas eternalist quantification is construed as quantification over the *global* domain. The respective semantic clauses for the dual $\exists$ of $\forall$ accordingly read as follows:

- $\mathcal{M},t\models_{v} \exists x \varphi$ iff …
- *presentist quantification*: …$\mathcal{M},t\models_{v[a/x]} \varphi$ for some $a\in D_t$;
- *eternalist quantification*: …$\mathcal{M},t\models_{v[a/x]} \varphi$ for some $a\in \mathcal{U}$.

Note that presentist quantification naturally suggests first-order temporal models with varying domains. In the semantics based on eternalist quantification the local domains do not play any essential role. In fact, eternalist quantification is tantamount to the assumption that the model has a constant domain, i.e., all local domains equal the global domain. In what follows, we often refer to the semantics with presentist quantification as *varying domain semantics* and to the semantics with eternalist quantification as *constant domain semantics*.

In each of these semantics, a FOTL formula *φ* is said to be *valid in a first-order temporal model $\mathcal{M}$* iff it is true in that model at each time instant with respect to every variable assignment; it is *valid in an augmented temporal frame* iff it is valid in each model based on that frame; and it is *valid* iff it is valid in every model.

Adopting one or the other approach to quantification affects the notion of validity, even for non-temporal principles. For instance, the sentence $\exists x(x= c)$ is valid in first-order logic, and it is valid in the constant domain semantics as well. However, it is no longer valid in the varying domain semantics because the object assigned to the constant $c$ may not belong to the local domain. Another principle from plain first-order logic that distinguishes the two semantics is the scheme of *Universal Instantiation* (where *τ* is any term free for substitution for $x$ in *φ*): $$\forall x \varphi(x) \to \varphi(\tau), $$ which is likewise valid in the constant domain semantics but invalid in the varying domain semantics, for analogous reasons. The main distinction between the two semantics, however, is reflected in principles involving interaction of temporal operators and individual quantifiers, such as the Barcan formula schemata and their converses. In the following two sections, we take a closer look at validity in the respective semantics.

### 8.4 Eternalist quantification and constant domain semantics

Let us consider some FOTL validities and non-validities in the constant domain semantics, that is, in the semantics with eternalist quantification. We denote validity in the constant domain semantics by $\models_{\mathrm{CD}}$.

- All FOTL instances of valid first-order formulae are CD-valid.
- In particular, the scheme of *Universal Instantiation* is CD-valid: $\models_{\mathrm{CD}} \forall x \varphi(x) \to \varphi(\tau)$, for any term *τ* free for substitution for $x$ in *φ*.
- The *Future Barcan Formula*[^note-8] scheme, $\mathsf{BF}_{G}$, is CD-valid: $\models_{\mathrm{CD}} \forall x G \varphi(x) \to G \forall x \varphi(x)$ or, equivalently, $\models_{\mathrm{CD}} F \exists x \varphi(x) \to \exists x F \varphi(x)$.
- The *Converse Future Barcan Formula* scheme, $\mathsf{CBF}_{G}$, is CD-valid: $\models_{\mathrm{CD}} G \forall x \varphi(x) \to \forall x G \varphi(x)$ or, equivalently, $\models_{\mathrm{CD}} \exists x F \varphi(x) \to F \exists x \varphi(x)$.
- Some important non-validities include: $\not\models_{\mathrm{CD}} \forall x F \varphi(x) \to F \forall x \varphi(x)$  and  $\not \models_{\mathrm{CD}} G \exists x \varphi(x) \to \exists x G \varphi(x)$.

Analogous claims hold for the past versions of the above schemata, with $H$ and $P$ instead of $G$ and $F$. An axiomatic system for the minimal FOTL with constant domain semantics as well as some important theorems of it are provided in the supplementary document:

> [Axiomatic System **FOTL(CD)** for the Minimal FOTL with Constant Domain Semantics](logic-temporal.axiomatic-fotl-constant.md)

### 8.5 Presentist quantification and varying domain semantics

In the varying domain semantics, the range of the individual quantifiers is restricted to the local domains. As a consequence, some formulae that are valid in the semantics with constant domains are no longer valid in the varying domain semantics. Most importantly, the varying domain semantics invalidates Universal Instantiation $\forall x \varphi(x) \to \varphi(\tau)$ as well as both the Future and Past Barcan Formula schemata and their converses. We denote validity in the varying domain semantics by $\models_{\mathrm{VD}}$.

It turns out that the Barcan formulae schemata $\mathsf{BF}_{G}$ and $\mathsf{BF}_{H}$ and their converses $\mathsf{CBF}_{G}$ and $\mathsf{CBF}_{H}$ define conditions on the local domains. For any augmented temporal frame $\mathcal{F}$, the following holds:

- $\mathcal{F}$ has expanding domains iff $\mathcal{F} \models_{\mathrm{VD}} \mathsf{BF}_{H}$ iff $\mathcal{F} \models_{\mathrm{VD}} \mathsf{CBF}_{G}$;
- $\mathcal{F}$ has shrinking domains iff $\mathcal{F} \models_{\mathrm{VD}} \mathsf{BF}_{G}$ iff $\mathcal{F} \models_{\mathrm{VD}} \mathsf{CBF}_{H}$.

Note that the Future Barcan scheme $\mathsf{BF}_{G}$ semantically corresponds to the converse Past Barcan scheme $\mathsf{CBF}_{H}$, and *vice versa*. From the above it follows that an augmented temporal frame $\mathcal{F}$ has locally constant domains iff either of the following formulae is VD-valid in $\mathcal{F}$: $\mathsf{BF}_{G} \wedge \mathsf{BF}_{H}$, $\mathsf{CBF}_{G} \wedge \mathsf{CBF}_{H}$, $\mathsf{BF}_{G} \wedge \mathsf{CBF}_{G}$, or $\mathsf{BF}_{H} \wedge \mathsf{CBF}_{H}$.

An axiomatic system for the minimal FOTL with varying domain semantics is provided in the supplementary document:

> [Axiomatic System **FOTL(VD)** for the Minimal FOTL with Varying Domain Semantics](logic-temporal.axiomatic-fotl-varying.md)

### 8.6 The existence predicate

Although presentism and eternalism are philosophically distinct ontologies, their technical manifestations are interreducible. On the one hand, the constant domain semantics with eternalist quantification can be obtained from the varying domain semantics with presentist quantification by imposing the constraint that the Past and Future Barcan Formula schemata and their converses be valid (provided that the temporal frame is connected). On the other hand, the varying domain semantics can be simulated in the constant domain semantics by adding to the language of FOTL an *existence predicate* $E$ for ‘existence at the current time instant’ with the following semantics: $\mathcal{M},t\vDash_v E(\tau)$ iff $v_t(\tau) \in D_t$. In the varying domain semantics, $E$ can be defined by $E(\tau) := \exists x (x=\tau)$.

The existence predicate enables an alternative formalization of the sentence “Some man exists who signed the Declaration of Independence”. Instead of writing $$\exists x(\mathsf{man}(x) \land P(\mathsf{signs}(x))), $$ we can write $$\exists x(E(x) \land \mathsf{man}(x) \land P(\mathsf{signs}(x))). $$ Assuming a constant domain semantics with eternalist quantification, the first formula is true at the present instant, whereas the second formula is presently false. It was true in 1777.

For every formula *φ* of FOTL, we can form its *$E$-relativization* by replacing every occurrence of $\forall x$ in *φ* by “$\forall x (E(x) \to ...)$” and every occurrence of $\exists x$ by “$\exists x (E(x) \land ...)$”. We then have that *φ* is valid in the varying domain semantics if and only if its $E$-relativization is valid in the constant domain semantics. The question that remains, from a philosophical point of view, is whether existence is a legitimate predicate. An axiomatic system for the minimal FOTL with existence predicate can be obtained along the lines of free logic, as outlined in the supplementary document:

> [Axioms for the Minimal FOTL with $E$: the Free Logic Version](logic-temporal.axiomatic-fotl-free.md)

### 8.7 Proper names and definite descriptions

A further issue arising in first-order temporal logics concerns the interpretation of individual terms. Depending on what kind of terms we are dealing with, we may or may not want to allow their interpretation to vary with time.

In the semantics outlined above, variable assignments are defined globally, and hence individual variables pick out the same object at all times. In other words, they are *rigid designators*. The interpretation of the constant symbols, on the other hand, is specified locally, i.e. relative to a time instant. If we wish to regard constants as proper names, it seems natural to treat them as rigid designators, too. Constant symbols can then be used to identify an object across different times. For instance, treating $a$ as a name for Aristotle, the sentence “Aristotle was sitting but now he is standing” can be formalized as $P\mathsf{sit}(a) \wedge \mathsf{stand}(a)$. Note that if constants are treated as rigid designators, the principle of the *Necessity of Identity* $\tau_1 = \tau_2 \rightarrow A(\tau_1 = \tau_2)$ is valid, for both variables and constants (recall that $A \varphi = H \varphi \land \varphi \land G\varphi$).

But there are also individual terns that are not rigid. Prime examples are *definite descriptions*, such as “the Pope”, which may pick out different objects at different times. Clearly, proper names and definite descriptions will require a different semantic treatment and are not freely inter-substitutable. For example “The Pope was born in Argentina” was false in 2012, whereas “Jorge Mario Bergoglio was born in Argentina” was true then. Moreover, in a temporal setting, the question arises how to deal with definite descriptions that refer to objects that do no longer or do not yet exist, such as “the first child to be born in South Africa in 2050”. The issues get even more intricate in a branching time setting, where time and modality are combined. Note, for instance, that some definite descriptions that are temporally rigid may be modally non-rigid. For more on definite descriptions and their challenges in the context of temporal logic, see Rescher and Urquhart (1971, Chapters XIII and XX) and Cocchiarella (2002)[^cocchiarella-2002].

One way to deal with definite descriptions is to switch from an extensional to an intensional account of individual terms. That is, rather than assigning to each term at each time instant an *extension*, i.e. an object from the domain, one may assign to each term an *intension*, i.e. a function from time instants to objects. A general framework in which individual terms are assigned both extensions and intensions is the Case Intensional First-Order Logic (CIFOL) proposed in Belnap and Müller (2014a; 2014b). In CIFOL, identity is extensional, predication is intensional, and individuals can be identified across times without making use of rigid designation. The framework also becomes interesting in the debate on persistence as it remains metaphysically neutral with respect to the precise nature of the objects included in the overall domain: it could be genuine individuals, but it could just as well be temporal stages.

### 8.8 Some technical results on first-order temporal logics

First-order temporal logics are very expressive, and this often comes with a high computational price: these logics can be deductively very complex and are typically *highly* undecidable (cf. Merz 1992; Gabbay et al. 1994; Hodkinson et al. 2002)[^gabbay-1994][^hodkinson-2002][^merz-1992]. The first-order temporal logic with constant domain semantics over the natural numbers, for example, with only two variables and unary relation symbols is not only undecidable but not even recursively axiomatizable (cf. Börger et al. 1997; Hodkinson et al. 2000)[^börger-1997][^hodkinson-2000].

Few axiomatizable — and even fewer decidable — natural fragments of first-order temporal logics have been identified and investigated so far. These include first-order temporal logics with *Since* and *Until* over the class of all linear flows of time and over the order of the rationals (Merz 1992; Reynolds 1996)[^merz-1992][^reynolds-1996], the fragment T(FOs) of FOTL, where temporal operators may not occur inside the scope of an individual quantifier (Gabbay et al. 1994, Chapter 14)[^gabbay-1994], as well as the *monodic fragment*, only allowing formulae with at most one free variable in the scope of a temporal operator (see Hodkinson et al. 2000; 2001; 2002 and Wolter and Zakharyaschev 2002)[^hodkinson-2000][^wolter-2002]. Still, as shown in the latter paper, already the monodic fragment with equality is no longer recursively axiomatizable. For further decidability results for suitably restricted fragments of FOTL, see Hodkinson et al. (2000). Additional technical references are given in Gabbay et al. (1994, Chapter 14) and Kröger and Merz (2008). For completeness results for first-order modal logics, see also Fitting and Mendelsohn (2023) and the entry on [modal logic](https://plato.stanford.edu/entries/logic-modal).

For further philosophical discussion on first-order modal and temporal logics, see Rescher and Urquhart (1971, Chapter XX); McArthur (1976)[^mcarthur-1976]; Garson (1984)[^garson-1984]: Linsky and Zalta (1994); van Benthem (1995, Section 7); Fitting and Mendelsohn (2023); Wölfl (1999)[^wölfl-1999]; Cocchiarella (2002)[^cocchiarella-2002]; as well as Lindström and Segerberg (2007).

## 9. Combining temporal and other logics

Logics are used to model various aspects of the world, including aspects that may dynamically change over time. For instance, the notion of knowledge studied in epistemic logic, the idea of an action underlying logics of agency, or the concept of space in spatial logics all bear an intimate relation to time. It is therefore natural to add a temporal dimension to these logics and equip the corresponding languages with temporal operators.

From a technical point of view, there are several ways of combining models and logical systems: products, fusions, etc. (see the entry on combining logics). These constructions provide different mechanisms for temporalizing a logic. Generic questions about transfer of logical properties, such as axiomatizability and decidability, arise: decidability, for instance, is usually preserved in fusions, while it is often lost in products of logical systems. For a general discussion of temporalizing logical systems and properties of temporalized logics, see Finger and Gabbay (1992; 1996); Finger et al. (2002); and Gabbay et al. (2003). Here we briefly discuss some of the most popular cases of temporalized logical systems.

### 9.1 Temporal-epistemic logics

Temporal-epistemic logics bring together temporal logics and (multi-agent) logics of knowledge. Some interesting properties can naturally be expressed by combining the epistemic modality $K$ (“the agent knows that”) with temporal operators. Here are just two examples: *perfect recall*: $K \varphi \to GK \varphi$ (If the agent knows *φ* now, then the agent will always know *φ* in the future) and *no learning*: $FK \varphi \to K \varphi$ (If the agent will know *φ* at some time in the future, then the agent already knows *φ* now).

Various temporal-epistemic logics were developed during the 1980s, with a unifying study by Halpern and Vardi (1989). They consider a variety of 96 temporal-epistemic logics on so-called *interpreted systems*, i.e. sets of temporal runs in a transition system with epistemic indistinguishability relations on the state space for each agent. The variety is based on several parameters: *number of agents* (one or many), *the language* (with or without common knowledge), *the formal model of time* (linear or branching time), *recall abilities* (no recall, bounded recall, or perfect recall), *learning abilities* (learning or no learning), *synchrony* (synchronous or asynchronous), *unique initial state*. Depending on the particular choice of these parameters, the computational complexity of the decision problem for these logics ranges very broadly from PSPACE-complete to highly undecidable ($\Pi^{1}_{1}$-complete). For details, see Halpern and Vardi (1989); Fagin et al. (1995); as well as the more recent van Benthem and Pacuit (2006), which surveys a number of decidability and undecidability results for temporal-epistemic logics and illustrates how the combination of time with other modalities bears on computational complexity.

### 9.2 Temporal logics and logics of agency

Temporal reasoning is an important aspect of reasoning about agents and their actions. Probably the most influential family of logics of agency in philosophy is the family of so-called *stit* logics, originating from the work of Belnap and Perloff (1988). These logics contain formulae of the form *stit*φ, reading “The agent sees to it that *φ*”, which allow one to reason about how an agent’s action choices affect the world. The original versions of *stit* logic do not involve temporal operators. Nevertheless, their semantics is based on Ockhamist tree models, where an agent’s set of choices at a given time instant is represented by a partition of the set of histories passing through that instant. Roughly, the formula *stit*φ is true at an instant $t$ with respect to a history $h$ iff the agent’s choice at the instant $t$ with respect to the history $h$ guarantees that *φ*, i.e. if *φ* is true at $t$ relative to all histories in the choice cell containing $h$. For a detailed discussion of varieties of *stit* logic and their historical development, see Segerberg (1992)[^segerberg-1992]; Belnap et al. (2001) and the entry on the logic of action. Temporal extensions of *stit* logics have first been proposed in Broersen (2011)[^broersen-2011] and Lorini (2013)[^lorini-2013]: in Broersen (2011)[^broersen-2011] the *stit* operator is combined with the *Next Time* operator $X$ into a single operator which requires that the objective be met in the next step, whereas in Lorini (2013)[^lorini-2013] the *stit* operator and the temporal operators are treated separately. Furthermore, in Broersen (2019)[^broersen-2019] a spatial dimension is added to the temporal dimension.

Another important family of temporal logics of agency are the *alternating-time logics* ATL and ATL\*, introduced in Alur et al. (2002). ATL and ATL\* are multi-agent extensions of the computation tree logics CTL and CTL\*, and they have become a popular logical framework for strategic reasoning in multi-agent systems. Alternating-time temporal logics enrich the language with strategic path quantifiers $\langle\!\langle C \rangle\!\rangle \varphi,$ intuitively saying “The coalition $C$ has a collective strategy to guarantee that the objective *φ* is met”, where the objective *φ* is a temporal formula. That is, the formula *φ* is required to be true in every path enabled by the collective strategy of $C$. While *stit* logics build on branching time, ATL and ATL\* are interpreted over so-called concurrent game structures, in which paths are viewed as sequences of states generated by collective actions of all agents. A combination of ATL and *stit* theory was developed in Broersen et al. (2006). The branching time logics CTL and CTL\* can be regarded as single-agent versions of ATL and ATL\*. Even though the latter are much more expressive, they generally preserve the good computational properties of the former. For details, see Alur et al. (2002), as well as Goranko and van Drimmelen (2006), where a complete axiomatization and decidability results for ATL are established. A general introduction to ATL from a temporal logic perspective is provided in Demri et al. (2016, Chapter 9).

### 9.3 Spatial-temporal logics

Space and time are intimately related in the physical world, and they have become inseparable in modern physical theories. While early physical theories, culminating in Newton’s classical mechanics, presuppose an absolute notion of time that is independent of space, Einstein’s relativity theory views time and space as inextricably interwoven, as modeled by Minkowski’s four-dimensional space-time manifold.

Early thoughts on space-time and special relativity theory can already be found in Prior’s work (see Kofod 2020 for a discussion of Prior’s youth ideas and Prior 1967 for his mature work.)[^kofod-2020][^prior-1967] In Goldblatt (1980)[^goldblatt-1980], the Diodorean modal logic of Minkowski space-time was studied and proved to be exactly the modal logic D4.2, as Prior had conjectured. Further results are provided in Uckelman and Uckelman (2007)[^uckelman-2007]. Logical investigations into general relativity theory have been conducted as well, see e.g. Andréka et al. (2007).

In Artificial Intelligence, space-time reasoning has been actively evolving over the past decades, particularly in the context of spatio-temporal ontologies, databases, and constraint networks. The main focus here is on the logical characterization of spatio-temporal models, computational complexity, and expressiveness (Gabelaia et al. 2005; Kontchakov et al. 2007)[^gabelaia-2005][^kontchakov-2007].

Another interesting line of research is triggered by the theory of branching space-times, initially developed in Belnap (1992)[^belnap-1992]. This theory relates to space-time just as Prior’s theory of branching time relates to linear time; that is, it combines space-time reasoning with indeterminism. An extensive presentation of branching space-times can be found in Belnap et al. (2022). For an intuitive introduction, see Belnap (2012)[^belnap-2012].

### 9.4 Temporal description logics

Description logics are essentially variations of modal logics. They involve *concepts* (unary predicates) and *roles* (binary predicates) and are used to describe various ontologies and the relations between the concepts in them (see e.g. Baader and Lutz 2007)[^baader-2007]. For example, the description logic term $\textsf{philosopher}\sqsubseteq\exists \mathsf{READ}.\textsf{book}$ says that every philosopher reads a book. Description logics can be temporalized in various ways. E.g. the temporalized version $G(\textsf{philosopher} \sqsubseteq P\, \mathsf{READ}.\textsf{book})$ allows us to express that it will always be the case that everyone who is a philosopher has read a book. For more on temporal description logics, see Artale and Franconi (2000); Wolter and Zakharyaschev (2000); and Lutz et al. (2008).

### 9.5 Temporal logics and other non-classical logics

Temporal reasoning can naturally be combined with various non-classical logical systems, resulting, for instance, in many-valued temporal logics (Rescher and Urquhart 1971, Chapter XVIII)[^rescher-1971], intuitionistic temporal logics (Ewald 1986)[^ewald-1986], constructive and paraconsistent temporal logics (Kamide and Wansing 2010; 2011)[^kamide-2010], probabilistic temporal logics (Hart and Sharir 1986; Konur 2013)[^hart-1986][^konur-2013], etc.

## 10. Logical deduction and decision methods for temporal logics

There exists a great variety of deduction systems and decision methods for the temporal logics mentioned here and many more. *Hilbert style axiomatic systems*, such as the ones provided in Section 3.5 and Section 4.3, are the most common deduction systems for temporal logics. But numerous *natural deduction systems*, *sequent calculi*, *resolution-based systems*, and *semantic tableaux systems* have been proposed as well. We briefly discuss the latter below. Some general references on deductive systems for temporal logics (in addition to the more specific references mentioned elsewhere in this text) include: Rescher and Urquhart (1971); McArthur (1976)[^mcarthur-1976]; Burgess (1984)[^burgess-1984]; Emerson (1990)[^emerson-1990]; Goldblatt (1992)[^goldblatt-1992]; Gabbay et al. (1994); van Benthem (1995)[^benthem-1995]; Bolc and Szalas (1995); Gabbay and Guenthner (2002); Gabbay et al. (2003); Fisher et al. (2005); Blackburn et al. (2007); Baier and Katoen (2008); Kröger and Merz (2008); Fisher (2011)[^fisher-2011]; Demri et al. (2016).

One of the most important logical decision problems is to determine whether a given formula is valid, respectively satisfiable. Particularly efficient and practically useful for this purpose are the *tableaux-based methods*, originating from pioneering work by Beth, Hintikka, Smullyan, and Fitting. Unlike axiomatic systems, semantic tableaux calculi are refutation-based systems: in order to prove validity, one negates the input formula and shows that the negation is not satisfiable. This is done by a systematic, tree-like search for a satisfying model, and the search is guaranteed to find such a model whenever it exists. If no model for the negation can be found, the input formula must be valid. A survey on tableaux systems for many temporal logics is provided in Goré (1999)[^goré-1999]. More specific references include: Ben-Ari et al. (1983) for the branching time logic UB; Emerson and Halpern (1985) for the computation tree logic CTL; Wolper (1985)[^wolper-1985] for the linear time temporal logic LTL; Kontchakov et al. (2004) on temporalizing tableaux; Reynolds (2007)[^reynolds-2007] for CTL with bundled tree semantics; Goranko and Shkatov (2010) for ATL; Reynolds (2011)[^reynolds-2011] for the full computation tree logic CTL\*; Reynolds (2014)[^reynolds-2014] for the real-time temporal logic RTL, etc.

In addition to the proof systems mentioned above, another computationally powerful approach for solving logical decision problems are *automata-based methods*, which have been actively developing since the early 1990s. These methods transform temporal formulae into automata on infinite words (for linear time logics) or infinite trees (for branching time logics) and represent models for the logics as input objects (infinite words or trees) for the associated automata. Thus, satisfiability of a formula becomes equivalent to the automaton accepting at least one input, i.e. the language of the automaton being non-empty. The methods are based on classical results about decidability of the monadic second-order theories of the natural numbers (by Büchi) and of the infinite binary tree (by Rabin). For instance, in Emerson and Sistla (1984), automata on infinite trees and Rabin’s theorem were used to obtain a decision procedure for CTL\*. For further details see Vardi (2007)[^vardi-2007].

Important references on decidability results and decision procedures for various temporal logics include: Burgess (1980)[^burgess-1980] and Gurevich and Shelah (1985) for branching time logics; Burgess and Gurevich (1985a; 1985b)[^gurevich-1985a][^gurevich-1985b] for linear temporal logics; Goldblatt (1992)[^goldblatt-1992] for both linear and branching time logics; Montanari and Policriti (1996) for metric and layered temporal logics; French (2001)[^french-2001] for some quantified propositional branching time logics.

While most propositional temporal logics are decidable, adding some extra syntactic or semantic features can make them explode computationally and become undecidable. The most common causes of undecidability of temporal logics, besides combinations with other expressive logics, include: grid-like models; temporal operators along multiple time-lines; products of temporal logics; interval-based logics with no locality assumptions; time reference mechanisms, such as hybrid reference pointers and freeze quantifiers; arithmetic features, such as time addition, exact time constraints, etc. Such negative results have given rise to extensive research on how to tame temporal logics and restore decidability, such as adding syntactic and parametric restrictions (e.g. on the number of propositional variables or the depth of nesting), imposing suitable semantic restrictions (e.g. locality for interval logics), identifying decidable fragments (e.g. the two-variable fragment FO$^{2}$ of classical first-order logic, guarded fragments, monodic fragments), etc.

## 11. Applications of temporal logics

Temporal logic is a field whose early development was largely driven by philosophical considerations. In a surprisingly short time, however, temporal logics were applied and further developed in various different disciplines, ranging from computer science, artificial intelligence, and linguistics, to natural, cognitive, and social sciences. In this section, we briefly discuss some applications of temporal logics in computer science, artificial intelligence, and linguistics.

### 11.1 Temporal logics in Computer Science

The idea of applying temporal reasoning to the analysis of deterministic and stochastic transition systems was already present in the theory of processes and events in Rescher and Urquhart (1971, Chapter XIV). However, it was with the seminal paper of Pnueli (1977)[^pnueli-1977] that temporal logic became important in computer science. Pnueli proposed the application of temporal logics to the specification and verification of *reactive and concurrent programs and systems*. In order to ensure correct behavior of a reactive program, in which computations are non-terminating (e.g. an operating system), it is necessary to formally specify and verify the acceptable infinite executions of that program. Moreover, to ensure correctness of a concurrent program, where two or more processors are working in parallel, it is necessary to formally specify and verify their interaction and synchronization.

Key properties of infinite computations that can be captured by temporal patterns are liveness, safety, and fairness (see Manna and Pnueli 1992)[^manna-1992]:

- *Liveness* properties or *eventualities* involve temporal patterns of the forms $F{p},$ $q \to F {p},$ or $G(q \to F {p}),$ which ensure that if a specific precondition ($q$) is initially satisfied, then a desirable state (satisfying $p$) will eventually be reached in the course of the computation. Examples are “If a message is sent, it will eventually be delivered” and “Whenever a printing job is activated, it will eventually be completed”.
- *Safety* or *invariance* properties involve temporal patterns of the forms ${G} {p},$ $q \to {G} {p},$ or $G(q \to {G} {p}),$ which ensure that if a specific precondition ($q$) is initially satisfied, then undesirable states (violating the safety condition $p$) will never occur. Examples are: “No more than one process will be in its critical section at any moment of time”, “A resource will never be used by two or more processes simultaneously”, or, to give more practical examples: “The traffic lights will never show green in both directions”, “A train will never pass a red semaphore”.
- *Fairness* properties involve combined temporal patterns of the forms ${GF} {p}$ (“infinitely often $p$”) or ${FG} {p}$ (“eventually always $p$”). Intuitively, fairness requires that whenever several processes that share resources are run concurrently, they must be treated ‘fairly’ by the operating system, scheduler, etc. A typical fairness requirement says that if a process is persistent enough in sending a request (e.g. keeps sending it over and over again), its request will eventually be granted.

An infinite computation is formally represented by a model of the linear time temporal logic LTL. Non-deterministic systems are modeled by tree structures. Thus, both LTL and the computation tree logics CTL and CTL\* have become instrumental in the specification and verification of reactive and concurrent systems.

The following example refers to a single computation and combines liveness and safety properties: “Whenever a state of alert is reached, the alarm is activated and remains activated until a safe state is eventually reached”. This property is expressible in LTL as

$$ G(\textsf{alert} \to (\textsf{alarm} \ U\ \textsf{safe})). $$

Another example, referring to all computations in the system, is: “If the process *σ* is eventually enabled on some computation starting from the current state, then on every computation starting there, whenever *σ* is enabled, it will remain enabled until the process *τ* is disabled”. This property can be formalized in CTL\* as

$$ \Diamond F\,\textsf{enabled}_{\sigma} \to \Box G(\textsf{enabled}_{\sigma} \to (\textsf{enabled}_{\sigma} \,U\, \textsf{disabled}_{\tau})). $$

A variation of LTL useful for specifying and reasoning about concurrent systems is Lamport’s (1994)[^lamport-1994] *temporal logic of actions* TLA. Other applications of temporal logics in computer science include: temporal databases, real-time processes and systems, hardware verification, etc. Further details on such applications can be found in e.g. Pnueli (1977)[^pnueli-1977]; Emerson and Clarke (1982); Moszkowski (1983)[^moszkowski-1983]; Galton (1987)[^galton-1987]; Emerson (1990)[^emerson-1990]; Alur and Henzinger (1992); Lamport (1994)[^lamport-1994]; Vardi and Wolper (1994); Bolc and Szalas (1995); Gabbay et al. (2000); Baier and Katoen (2008); Kröger and Merz (2008); Fisher (2011)[^fisher-2011]; Demri et al. (2016).

### 11.2 Temporal logics in Artificial Intelligence

Artificial Intelligence (AI) is one of the major areas of application of temporal logics. Important topics in AI which have been explored with their help include: temporal ontologies, spatial-temporal reasoning, temporal databases and constraint solving, executable temporal logics, temporal planning, temporal reasoning in agent-based systems, and natural language processing. Comprehensive overviews of a wide variety of applications may be found in e.g. Vila (1994)[^vila-1994]; Galton (1995)[^galton-1995]; Fisher et al. (2005); and Fisher (2008)[^fisher-2008]. See also the related discussion on reasoning about action and change in Section 4 of the entry on logic and artificial intelligence.

The idea of relating temporal reasoning and AI was first discussed in the late 1960s and 70s, and it flourished in the 1980s and 90s; for overviews of historical developments, see Galton (1987)[^galton-1987]; Vila (1994)[^vila-1994]; Øhrstrøm and Hasle (1995); and Pani and Bhattacharjee (2001). The combination of temporal logic and AI was suggested in the early philosophical discussion on AI by McCarthy and Hayes (1969), the theory of processes and events in Rescher and Urquhart (1971, Chapter XIV), and the period-based theories of Hamblin (1972)[^hamblin-1972]. Seminal work from the 1980s and 90s include: McDermott’s (1982)[^mcdermott-1982] temporal logic for reasoning about processes and plans, Allen’s (1984)[^allen-1984] general theory of action and time, the event calculus of Kowalski and Sergot (1986), the reified temporal logic by Shoham (1987)[^shoham-1987], the logic of time representation by Ladkin (1987)[^ladkin-1987], the work on temporal database management by Dean and McDermott (1987), the introduction of interval-based temporal logics by Halpern and Shoham (1991) and by Allen and Ferguson (1994) (with representation of actions and events), the situation calculus of Pinto and Reiter (1995), and Lamport’s (1994)[^lamport-1994] action theory.

Although it is much concerned with applications, the debate in the AI literature raises interesting philosophical issues, too. Philosophical questions naturally arise with respect to the ontological foundations of the temporal models: the choice between discrete and continuous, instant-based and interval-based temporal models is one example. Both instant-based and interval-based approaches have been developed and compared, see e.g. van Benthem (1983)[^benthem-1983]; Allen (1983)[^allen-1983]; Allen and Hayes (1989); Allen and Ferguson (1994); Galton (1090; 1995)[^galton-1995]; Vila (2005)[^vila-2005]; etc.

Furthermore, the AI literature distinguishes between different kinds of temporal phenomena, such as fluents, events, actions, and states. While fluents concern states of the world that may change over time (e.g. whether the light is on or off), events and actions represent what happens in the world and causes changes between states (e.g. the turning on of the light, the room becoming light). Theories of temporal incidence explore the structural properties of these phenomena, such as whether they are homogenous over an extended period of time (e.g. if the light is on from 2 o'clock to 4 o'clock, can we infer that it was on at 3 o'clock?). See e.g. Galton (2005)[^galton-2005]; Vila (2005)[^vila-2005]; etc.

Once we have incorporated such temporal phenomena in our models, we need to specify a logical language that allows us to express when they happen or occur. In the AI literature, different methods of temporal qualification can be found. For an overview, see Reichgelt and Vila (2005)[^vila-2005]. Traditionally, temporalized variations of first-order logic rather than Prior style temporal logics have been used. Perhaps the simplest first-order approach is the so-called *method of temporal arguments* (McCarthy and Hayes 1969; Shoham 1987; Vila 1994)[^mccarthy-1969][^shoham-1987][^vila-1994]. Here the temporal dimension is captured by augmenting propositions and predicates with ‘time stamp’ arguments; for example “Publish(A. Prior, *Time and Modality*, 1957)[^prior-1957]”. An alternative, yet closely related approach, is that of *reified temporal logics* (McDermott 1982; Allen 1984; Shoham 1987; see Ma and Knight 2001 for a survey)[^allen-1984][^mcdermott-1982][^shoham-1987]. This approach makes use of reifying meta-predicates, such as ‘TRUE’ and ‘FALSE’, but also ‘HOLDS’, ‘OCCURS’, ‘BEFORE’, ‘AFTER’, and interval relations such as ‘MEETS’, ‘OVERLAPS’, etc., which are applied to propositions of some standard logical language (e.g. classical first-order logic); for example “OCCUR(Born(A. Prior), 1914)”. Still, the modal-logic style approach has had a recent resurgence, e.g. in the context of agent-based temporal reasoning (cf. Fisher and Wooldridge 2005)[^fisher-2005][^fisher-2005-2].

However, philosophical questions arise not only with respect to traditional issues, such as the choice of the temporal models and the question about which temporal phenomena exist and how they are to be reasoned about. AI supplies novel puzzles as well. A famous example is the *frame problem*: if a change occurs, how can we keep track of what does not change as a result? This problem has been widely explored and relates to issues in philosophy and cognitive science. For a detailed discussion, see the entry on the frame problem.

### 11.3 Temporal logics in Linguistics

Tense is an important feature of natural languages. It is a linguistic device that allows one to specify the relative location of events in time, usually with respect to the speech time. In several languages, including English, tense becomes manifest in a system of different verbal tenses. English allows for a distinction between past, present, and future tense (‘will’ future), and traditionally, the respective perfect and progressive forms are referred to as tenses as well.

As laid out above, Prior’s invention of tense logic was motivated by the use of tense in natural language. An alternative early logical approach to tense was provided by Reichenbach (1947)[^reichenbach-1947], who suggested an analysis of the English verbal tenses in terms of three points in time: speech time, event time, and reference time, where the reference time is a contextually salient point in time, which, intuitively, captures the perspective from which the event is viewed. Using the notion of reference time, Reichenbach was able to distinguish, for example, between the simple past (“I wrote a letter”) and the present perfect (“I have written a letter”), which are conflated in Prior’s account. With both the simple past and the present perfect, the event time precedes the speech time; but in the former case the reference time coincides with the event time, whereas in the latter case the reference time is simultaneous with the speech time.

Neither Prior’s nor Reichenbach’s frameworks can account for the difference between, for instance, the simple past (“I wrote a letter”) and the past progressive (“I was writing a letter”). The relevant distinction here is one of aspect rather than of tense and seems to call for an interval-based or event-based setting. For accounts along these lines, see e.g. Dowty (1979)[^dowty-1979]; Parsons (1980); Galton (1984)[^galton-1984]; and van Lambalgen and Hamm (2005).

Whereas Reichenbach’s analysis makes reference to a contextually salient point in time, on Prior’s account tenses are construed as temporal operators, which are interpreted as quantifiers over instants in time. This raises the general question: are tenses in natural language to be treated as quantifiers, or do they refer to specific points in time? In an influential paper, Partee (1973)[^partee-1973] provided the following counterexample against a quantifier treatment of tenses: the sentence “I didn’t turn off the stove” means neither (1) there is an earlier time instant at which I do not turn off the stove, nor does it mean (2) there is no earlier instant at which I turn off the stove. The first requirement is too weak, the second too strong. Partee suggested an analogy between tenses and referential pronouns. According to this proposal, tenses refer to specific, contextually given points in time (e.g. 8 o’clock this morning), which are presupposed to stand in appropriate temporal relations to the speech time. Subsequently, accounts that restrict quantification to a contextually given time interval (e.g. this morning) have become popular. On these accounts, Partee’s example sentence has the intuitive meaning: there is no earlier time instant in the contextually salient time interval at which I turn off the stove. Formally, this is compatible with both quantifier and referential treatments of tense; for details see Kuhn and Portner (2002) and Ogihara (2011)[^ogihara-2011]. Moreover, the idea of combining quantificational and referential elements can be dealt with in the hybrid variants of tense logic discussed in Section 7.1 (see Blackburn and Jørgensen 2016)[^blackburn-2016]. The hybrid approach also allows for a Hans Kamp style treatment of temporal indexicals, such as “now” (Kamp 1971)[^kamp-1971], as was noticed by Prior as early as 1968 (Prior 1968)[^prior-1968][^prior-1968-2].

Other pertinent issues in linguistics relating to time concern the meaning of temporal adverbs and connectives, the interaction of tense and quantification, the interpretation of embedded tenses and sequence of tense, as well as the interrelation of tense and modality. For an overview and further discussion on the application of temporal logics in linguistics, see e.g. Steedman (1997)[^steedman-1997]; Kuhn and Portner (2002); Mani et al. (2005); ter Meulen (2005)[^meulen-2005]; Moss and Tiede (2007); Ogihara (2007; 2011)[^ogihara-2007][^ogihara-2011]; Dyke (2013)[^dyke-2013][^dyke-2013-2]; and the entry on tense and aspect.

## Further Reading

For further references on temporal logics, see the overviews in Venema (2001)[^venema-2001]; Burgess (2009)[^burgess-2009]; and Müller (2011)[^müller-2011], as well as the detailed bibliographies in Rescher and Urquhart (1971); Burgess (1984)[^burgess-1984]; Øhrstrøm and Hasle (1995); Gabbay et al. (1994); Fisher et al. (2005); Baier and Katoen (2008); Demri et al. (2016); and Goranko (2023)[^goranko-2023].

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=logic-temporal). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/logic-temporal/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=logic-temporal&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/logic-temporal/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- [A Research Site for Prior Studies and Temporal Logic](https://research.prior.aau.dk/priorstudies/)
- [TIME International Symposium on Temporal Representation and Reasoning](http://time.di.unimi.it/TIME_Home.html)
- [The Temporal Logic of Actions (TLA) Home Page](http://research.microsoft.com/en-us/um/people/lamport/tla/tla.html)
- [Galton, A., “Temporal Logic”, *The Stanford Encyclopedia of Philosophy* (Fall 2008 Edition).](https://plato.stanford.edu/archives/fall2008/entries/logic-temporal/)

## Related Entries

artificial intelligence: logic-based | branching time | Diodorus Cronus | frame problem | future contingents | identity: over time | logic: action | logic: combining | logic: free | logic: hybrid | logic: intensional | logic: modal | McTaggart, John M. E. | Ockham [Occam], William | Prior, Arthur | temporal parts | tense and aspect | time

### Acknowledgments

The first version of this entry was written by Antony Galton in 1999, later revised in Galton (2008)[^galton-2008]. In 2015 the entry was substantially re-written and extended by Valentin Goranko. The 2020 version constitutes a major revision and further extension of the 2015 version, with Antje Rumberg as a new co-author, and builds the basis of the present version. We acknowledge Galton’s contribution to the previous versions, and we are grateful to Johan van Benthem, Patrick Blackburn, Rob Goldblatt, Angelo Montanari, Yde Venema, Michael Zakharyaschev, Ed Zalta, Alberto Zanardo, as well as some attentive readers for helpful comments and suggestions on earlier versions.

## Notes（原文脚注）

[^note-1]: Tkaczyk and Jarmużek (2019) have recently stressed Łoś’s contribution to the emergence of temporal logic. Their paper was followed by a response by Øhrstrøm and Hasle (2019), clarifying Łoś’s influence on Prior.

[^note-2]: Especially in the early computer science literature, sometimes the notation $\small{\bigcirc}$ instead of $X$ is used for the *Next Time* operator.

[^note-3]: In the philosophical logic literature, often a prefix notation for $U$ and $S$ is used and the two arguments are swapped, i.e., $U\psi \varphi$ is used for $\varphi U\psi$.

[^note-4]: In fact, the reflexive versions of $S$ and $U$ can be defined in terms of the strict ones, e.g. $\varphi S_{\mathit{ref}}\psi :=\psi \vee (\varphi \land \varphi S\psi)$, but generally not *vice versa*. Still, on discrete linear frames, the strict operators are definable in terms of their reflexive counterparts by making use of $X$ and its past analogue, respectively: e.g. $\varphi U\psi := X(\varphi U_{\mathit{ref}}\psi)$.

[^note-5]: As outlined in Øhrstrøm and Gonzalez (2022), Prior toyed with the idea of branching time –– or the big Y –– already before he received Kripke’s letter, inspired by the science fiction novel *The Seeds of Time* (1956) by John Wyndham.

[^note-6]: We have adopted this example from the original entry on [Temporal Logic](https://plato.stanford.edu/archives/spr2008/entries/logic-temporal/) by Anthony Galton (Galton 2008)[^galton-2008].

[^note-7]: Note that the assumption that the global domain is the union of all local domains intuitively excludes the possibility of fictitious individuals, who do not really exist at any time instant. The problem can be resolved by allowing for temporally isolated instants or possible worlds, where such fictitious objects can reside. Alternatively, one can drop the above requirement and allow objects in the global domain which do not belong to any local domain.

[^note-8]: Here we adopt the terminology from McArthur (1976)[^mcarthur-1976].

[^albretsen-2016]: Albretsen, J., P. Hasle, and P. Øhrstrøm (eds.), 2016, *Special Issue on the Philosophy and Logic of A.N. Prior*, *Synthese*, 193(11).

[^allen-1983]: Allen, J.F., 1983, “Maintaining Knowledge about Temporal Intervals”, *Communications of the ACM*, 26(11): 832–843.

[^allen-1984]: –––, 1984, “Towards a General Theory of Action and Time”, *Artificial Intelligence*, 23: 123–154.

[^allen-1994]: Allen, J.F., and G. Ferguson, 1994, “Actions and Events in Interval Temporal Logic”, *Journal of Logic and Computation*, 4(5): 531–579.

[^allen-1989]: Allen, J.F., and P. Hayes, 1989, “Moments and Points in an Interval-Based Temporal Logic”, *Computational Intelligence*, 5(4): 225–238.

[^alur-1992]: Alur, R., and T. Henzinger, 1992, “Logics and Models of Real-Time: A Survey”, in *Real-Time: Theory in Practice*, Proceedings of the REX Workshop 1991 (Lecture Notes in Computer Science: Volume 600), Berlin: Springer, pp. 74–106.

[^alur-1993]: –––, 1993, “Real-Time Logics: Complexity and Expressiveness”, *Information and Computation*, 104: 35–77.

[^alur-1994]: –––, 1994, “A Really Temporal Logic”, *Journal of the ACM*, 41: 181–204.

[^alur-2002]: Alur, R., T. Henzinger, and O. Kupferman, 2002, “Alternating-Time Temporal Logic”, *Journal of the ACM*, 49(5): 672–713.

[^andréka-1995]: Andréka, H., V. Goranko, S. Mikulas, I. Németi, and I. Sain, 1995, “Effective First-Order Temporal Logics of Programs”, in Bolc and Szalas (1995), pp. 51–129.

[^andréka-2007]: Andréka, H., J. Madarász, and I. Németi, 2007, “Logic of Space-Time and Relativity Theory”, in M. Aiello, J. van Benthem, and I. Pratt-Hartmann (eds.), *Handbook of Spatial Logics*, Dordrecht: Springer, pp. 607–711.

[^areces-2007]: Areces, C., and B. ten Cate, 2007, “Hybrid Logics”, in Blackburn et al. (2007), pp. 821–868.

[^aristotle-nd]: Aristotle, *Organon, II — On Interpretation, Chapter 9*. See [https://archive.org/stream/AristotleOrganon/AristotleOrganoncollectedWorks](https://archive.org/stream/AristotleOrganon/AristotleOrganoncollectedWorks).

[^artale-2000]: Artale, A., and E. Franconi, 2000, “A Survey of Temporal Extensions of Description Logics”, *Annals of Mathematics and Artificial Intelligence*, 30: 171–210.

[^baader-2007]: Baader, F., and C. Lutz, 2007, “Description Logic”, in Blackburn et al. (2007), pp. 757–819.

[^baier-2008]: Baier, C., and J.P. Katoen, 2008, *Principles of Model Checking*, Cambridge, Massachusetts: MIT Press.

[^balbiani-2011]: Balbiani, P., V. Goranko, and G. Sciavicco, 2011, “Two-Sorted Point-Interval Temporal Logics”, in *Proceedings of the 7th International Workshop on Methods for Modalities* (Electronic Notes in Theoretical Computer Science: Volume 278), pp. 31–45.

[^belnap-1992]: Belnap, N., 1992, “Branching Space-Time”, *Synthese*, 92(3): 385–434.

[^belnap-2012]: –––, 2012, “Newtonian Determinism to Branching Space-Time Indeterminism in Two Moves”, *Synthese*, 188: 5–21.

[^belnap-1994]: Belnap, N., and M. Green, 1994, “Indeterminism and the Thin Red Line”, *Philosophical Perspectives*, 8: 365–388.

[^belnap-2014a]: Belnap, N., and T. Müller, 2014a, “CIFOL: Case-Intensional First Order Logic (I): Toward a Theory of Sorts”, *Journal of Philosophical Logic*, 43(2–3): 393–437.

[^belnap-2014b]: –––, 2014b, “BH-CIFOL: Case-Intensional First Order Logic (II): Branching Histories”, *Journal of Philosophical Logic*, 43(5): 835–866.

[^belnap-2022]: Belnap, N., T. Müller, and T. Placek, 2022, *Branching Space-Times: Theory and Applications*, Oxford: Oxford University Press.

[^belnap-1988]: Belnap, N., and M. Perloff, 1988, “Seeing to it that: A Canonical Form for Agentives”, *Theoria*, 54: 175–199, reprinted with corrections in H. E. Kyberg et al. (eds.), *Knowledge Representation and Defeasible Reasoning*, Dordrecht: Kluwer, 1990, pp. 167–190.

[^belnap-2001]: Belnap, N., M. Perloff, and M. Xu, 2001, *Facing the Future: Agents and Choices in Our Indeterminist World*, Oxford: Oxford University Press.

[^ben-ari-1983]: Ben-Ari, M., A. Pnueli, and Z. Manna, 1983, “The Temporal Logic of Branching Time”, *Acta Informatica*, 20(3): 207–226.

[^benthem-1983]: van Benthem, J., 1983, *The Logic of Time*, Dordrecht, Boston, and London: Kluwer Academic Publishers. [Second edition: 1991.]

[^benthem-1984]: –––, 1984, “Tense Logic and Time”, *Notre Dame Journal of Formal Logic*, 25(1): 1–16.

[^benthem-1995]: –––, 1995, “Temporal Logic”, in D.M. Gabbay, C.J. Hogger, and J.A. Robinson (eds.), *Handbook of Logic in Artificial Intelligence and Logic Programming* (Volume 4), Oxford: Clarendon Press, pp. 241–350.

[^benthem-2001]: –––, 2001, “Correspondence Theory”, in D.M. Gabbay, and F. Guenther (eds.), *Handbook of Philosophical Logic* (Volume 3), Second Edition, Dordrecht: Kluwer, pp. 325–408.

[^benthem-2006]: van Benthem, J., and E. Pacuit, 2006, “The Tree of Knowledge in Action: Towards a Common Perspective”, in *Advances in Modal Logic* (Volume 6), London: College Publications, pp. 87–106.

[^blackburn-1993]: Blackburn, P., 1993, “Nominal Tense Logic”, *Notre Dame Journal of Formal Logic*, 34: 56–83.

[^blackburn-2006]: –––, 2006, “Arthur Prior and Hybrid Logic”, *Synthese*, 150: 329–372.

[^blackburn-2007]: Blackburn, P., J. van Benthem, and F. Wolter, 2007, *Handbook of Modal Logic*, Amsterdam: Elsevier.

[^blackburn-2019]: Blackburn, P., P. Hasle, and P. Øhrstrøm (eds.), 2019, *Logic and Philosophy of Time: Further Themes from Prior* (Volume 2), Aalborg: Aalborg University Press.

[^blackburn-2016]: Blackburn, P., and K. Jørgensen , 2016, “Reichenbach, Prior, and Hybrid Tense Logic”, *Synthese*, 193(11): 3677–3689.

[^blackburn-2001]: Blackburn, P., M. de Rijke, and Y. Venema, 2001, *Modal Logic*, Cambridge: Cambridge University Press.

[^blackburn-1995]: Blackburn, P., and J. Seligman, 1995, “Hybrid Languages”, *Journal of Logic, Language and Information*, 4: 251–272.

[^blackburn-1999]: Blackburn, P., and M. Tzakova, 1999, “Hybrid Languages and Temporal Logic”, *Logic Journal of the IGPL*, 7: 27–54.

[^bolc-1995]: Bolc, L., and A. Szalas (eds.), 1995, *Time and Logic: A Computational Approach*, London: UCL Press.

[^börger-1997]: Börger, E., E. Grädel, and Y. Gurevich, 1997, *The Classical Decision Problem*, Berlin, Heidelberg: Springer.

[^boyd-2014]: Boyd, S., 2014, “Defending History: Temporal Reasoning in Genesis 2:7–3:8”, *Answers Research Journal*, 7: 215–237.

[^bresolin-2009]: Bresolin, D., V. Goranko, A. Montanari, and G. Sciavicco, 2009, “Propositional Interval Neighborhood Logics: Expressiveness, Decidability, and Undecidable Extensions”, *Annals of Pure and Applied Logic*, 161(3): 289–304.

[^bresolin-2013]: Bresolin, D., D. Della Monica, V. Goranko, A. Montanari, and G. Sciavicco, 2013, “Metric Propositional Neighborhood Logics on Natural Numbers”, *Software and Systems Modeling*, 12(2): 245–264.

[^broersen-2011]: Broersen, J., 2011, “Deontic Epistemic *Stit* Logic Distinguishing Modes of Mens Rea”, *Journal of Applied Logic*, 9: 137–152.

[^broersen-2019]: –––, 2019, “Agents Necessitating Effects in Newtonian Time and Space: From Power and Opportunity to Effectivity”, *Synthese*, 196: 31–68.

[^broersen-2006]: Broersen, J., A. Herzig, and N. Troquard, 2006, “A STIT-Extension of ATL”, in *Proceedings of JELIA 2006* (Lecture Notes in Artificial Intelligence: Volume 4160), Berlin: Springer, pp. 69–81.

[^bull-1970]: Bull, R., 1970, “An Approach to Tense Logic”, *Theoria*, 36: 282–300.

[^burgess-1978]: Burgess, J., 1978, “The Unreal Future”, *Theoria*, 44(3): 157–179.

[^burgess-1979]: –––, 1979, “Logic and Time”, *Journal of Symbolic Logic*, 44: 566–582.

[^burgess-1980]: –––, 1980, “Decidability for Branching Time”, *Studia Logica*, 39: 203–218.

[^burgess-1982a]: –––, 1982a, “Axioms for Tense Logic I: ‘Since’ and ‘Until’”, *Notre Dame Journal of Formal Logic*, 23: 367–374.

[^burgess-1982b]: –––, 1982b, “Axioms for Tense Logic II: Time Periods”, *Notre Dame Journal of Formal Logic*, 23: 375–383.

[^burgess-1984]: –––, 1984, “Basic Tense Logic”, in D.M. Gabbay, and F. Guenthner (eds.), *Handbook of Philosophical Logic* (Volume 2), Dordrecht: Reidel, pp. 89–133. [New edition in Gabbay and Guenthner (2002), pp. 1–42.]

[^burgess-2009]: –––, 2009, *Philosophical Logic*, Princeton: Princeton University Press.

[^burgess-1985]: Burgess, J., and Y. Gurevich, 1985, “The Decision Problem for Linear Temporal Logic”, *Notre Dame Journal of Formal Logic*, 26(2): 115–128.

[^ciuni-2010]: Ciuni, R., and A. Zanardo, 2010, “Completeness of a Branching-Time Logic with Possible Choices”, *Studia Logica*, 96: 393–420.

[^cocchiarella-2002]: Cocchiarella, N., 2002, “Philosophical Perspectives on Quantification in Tense and Modal Logic”, in Gabbay and Guenthner (2002), pp. 235–276.

[^correia-2013]: Correia, F., and F. Iacona (eds.), 2013, *Around the Tree: Semantic and Metaphysical Issues Concerning Branching and the Open Future* (Synthese Library: Volume 361), Dordrecht: Springer.

[^correia-2018]: Correia, F., and S. Rosenkranz, 2018, *Nothing to Come: A Defense of the Growing Block Theory of Time* (Synthese Library: Volume 395), Dordrecht: Springer.

[^dean-1987]: Dean, T., and D.V. McDermott, 1987, “Temporal Data Base Management”, *Artificial Intelligence*, 32:1–55.

[^della-2011]: Della Monica, D., V. Goranko, A. Montanari, and G. Sciavicco, 2011, “Interval Temporal Logics: A Journey”, *Bulletin of the European Association for Theoretical Computer Science*, 105: 73–99.

[^demri-2016]: Demri, S., V. Goranko, and M. Lange, 2016, *Temporal Logics in Computer Science*, Cambridge: Cambridge University Press.

[^dowty-1979]: Dowty, D., 1979, *Word Meaning and Montague Grammar*, Dordrecht: Reidel.

[^dyke-2013]: Dyke, H., 2013, “Time and Tense”, in Dyke and Bardon (2013), pp. 328–344.

[^dyke-2013-2]: Dyke, H., and A. Bardon (eds.), 2013, *A Companion to the Philosophy of Time* (Blackwell Companions to Philosophy), Oxford: Wiley-Blackwell.

[^emerson-1990]: Emerson, E.A., 1990, “Temporal and Modal Logics”, in J. van Leeuwen (ed.), *Handbook of Theoretical Computer Science* (Volume B: Formal Models and Semantics), Amsterdam: Elsevier, pp. 995–1072.

[^emerson-1982]: Emerson, E.A., and E.C. Clarke, 1982, “Using Branching Time Temporal Logic to Synthesise Synchronisation Skeletons”, *Science of Computer Programming*, 2: 241–266.

[^emerson-1985]: Emerson, E.A., and J. Halpern, 1985, “Decision Procedures and Expressiveness in the Temporal Logic of Branching Time”, *Journal of Computer and Systems Science*, 30: 1–24.

[^emerson-1984]: Emerson, E.A., and A. Sistla, 1984, “Deciding Full Branching Time Logic”, *Information and Control*, 61: 175–201.

[^euzenat-2005]: Euzenat, J., and A. Montanari, 2005, “Time Granularity”, in Fisher et al. (2005), pp. 59–118.

[^ewald-1986]: Ewald, W., 1986, “Intuitionistic Tense and Modal Logic”, *Journal of Symbolic Logic*, 51(1): 166–179.

[^fagin-1995]: Fagin, R., J. Halpern, Y. Moses, and M. Vardi, 1995, *Reasoning about Knowledge*, Boston: MIT Press.

[^finger-1992]: Finger, M., and D.M. Gabbay, 1992, “Adding a Temporal Dimension to a Logic System”, *Journal of Logic, Language and Information*, 1(3): 203–233.

[^finger-1996]: –––, 1996, “Combining Temporal Logic Systems”, *Notre Dame Journal of Formal Logic*, 37(2): 204–232.

[^finger-2002]: Finger, M., D.M. Gabbay, and M. Reynolds, 2002, “Advanced Tense Logic”, in Gabbay and Guenthner (2002), pp. 43–204.

[^fisher-2008]: Fisher, M., 2008, “Temporal Representation and Reasoning”, in F. van Harmelen, V. Lifschitz, and B. Porter (eds.), *Handbook of Knowledge Representation*, Amsterdam: Elsevier, pp. 513–550.

[^fisher-2011]: –––, 2011, *An Introduction to Practical Formal Methods Using Temporal Logic*, New York: Wiley.

[^fisher-2005]: Fisher, M., D.M. Gabbay, and L. Vila, 2005, *Handbook of Temporal Reasoning in Artificial Intelligence*, Amsterdam: Elsevier.

[^fisher-2005-2]: Fisher, M., and M. Wooldridge, 2005, “Temporal Reasoning in Agent-Based Systems”, in Fisher et al. (2005), pp. 469–495.

[^fitting-2023]: Fitting, M., and R. Mendelsohn, 2023, *First-Order Modal Logic* (Second edition), Springer.

[^french-2001]: French, T., 2001, “Decidability of Quantified Propositional Branching Time Logics”, *Advances in AI* (Lecture Notes in Computer Science: Volume 2256), Berlin: Springer, pp. 165–176.

[^french-2003]: French, T., and M. Reynolds, 2003, “A Sound and Complete Proof System for QPTL”, in Balbiani et al. (eds.), *Advances in Modal Logic* (Volume 4), London: College Publication, pp. 127–148.

[^fritz-2024]: Fritz, P., 2024 (forthcoming), *Propositional Quantifiers*, Cambridge Elements in Philosophy and Logic, Cambridge: Cambridge University Press.

[^gabbay-2002]: Gabbay, D.M., and F. Guenthner (eds.), 2002, *Handbook of Philosophical Logic* (Volume 7), Second Edition, Dordrecht: Kluwer.

[^gabbay-1994]: Gabbay, D.M., I. Hodkinson, and M. Reynolds, 1994, *Temporal Logic: Mathematical Foundations and Computational Aspects* (Volume 1), Oxford: Clarendon Press.

[^gabbay-2003]: Gabbay, D., A. Kurucz, F. Wolter, and M. Zakharyaschev, 2003, *Many-Dimensional Modal Logics: Theory and Applications*, Amsterdam: Elsevier.

[^gabbay-1980]: Gabbay, D.M., A. Pnueli, S. Shelah, and J. Stavi, 1980, “On the Temporal Basis of Fairness”, in *Proceedings of the 7th ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages*, pp. 163–173.

[^gabbay-2000]: Gabbay, D.M., M. Reynolds, and M. Finger, 2000, *Temporal Logic: Mathematical Foundations and Computational Aspects* (Volume 2), Oxford: Oxford University Press.

[^gabbay-2009]: Gabbay, D.M., D. Skvortsov, and V. Shehtman, 2009, *Quantification in Nonclassical Logic* (Studies in Logic and the Foundations of Mathematics, Volume 153), Elsevier.

[^gabelaia-2005]: Gabelaia, D., R. Kontchakov, A. Kurucz, F. Wolter, and M. Zakharyaschev, 2005, “Combining Spatial and Temporal Logics: Expressiveness vs. Complexity”, *Journal of Artificial Intelligence Research*, 23: 167–243.

[^galton-1984]: Galton, A.P., 1984, *The Logic of Aspect*, Oxford: Clarendon Press.

[^galton-1987]: –––, 1987, *Temporal Logics and their Applications*, London: Academic Press.

[^galton-1990]: –––, 1990, “A Critical Examination of Allen’s Theory of Action and Time”, *Artificial Intelligence*, 42: 159–188.

[^galton-1995]: –––, 1995, “Time and Change for AI”, in D.M. Gabbay, C.J. Hogger, and J.A. Robinson, *Handbook of Logic in Artificial Intelligence and Logic Programming* (Volume 4), Oxford: Clarendon Press, pp. 175–240.

[^galton-1996]: –––, 1996, “Time and Continuity in Philosophy, Mathematics, and Artificial Intelligence”, *Kodikas/Code*, 19 (1–2): 101–119.

[^galton-2005]: –––, 2005, “Eventualities”, in Fisher et al. (2005), pp. 25–58.

[^galton-2008]: –––, 2008, “Temporal Logic”, in E.N. Zalta (ed.), *The Stanford Encyclopedia of Philosophy* (Fall 2008 Edition), URL = <[https://plato.stanford.edu/archives/fall2008/entries/logic-temporal/](https://plato.stanford.edu/archives/fall2008/entries/logic-temporal/)>.

[^gargov-1993]: Gargov, G., and V. Goranko, 1993, “Modal Logic with Names”, *Journal of Philosophical Logic*, 22: 607–636.

[^garson-1984]: Garson, J., 1984, “Quantification in Modal Logic”, in D.M. Gabbay, and F. Guenthner (eds.), *Handbook of Philosophical Logic*, Dordrecht: Reidel, pp. 249–307.

[^goldblatt-1980]: Goldblatt, R., 1980, “Diodorean Modality in Minkowski Spacetime”, *Studia Logica*, 39: 219–236. [Reprinted in *Mathematics of Modality* (CSLI Lecture Notes 43), Stanford: CSLI Publications, 1993.]

[^goldblatt-1992]: –––, 1992, *Logics of Time and Computation* (CSLI Lecture Notes 7), Second Edition, Stanford: CSLI Publications.

[^goranko-1996]: Goranko, V., 1996, “Hierarchies of Modal and Temporal Logics with Reference Pointers”, *Journal of Logic, Language and Information*, 5(1): 1–24.

[^goranko-2023]: –––, 2023, *Temporal Logics*, Cambridge Elements in Philosophy and Logic, Cambridge: Cambridge University Press.

[^goranko-2006]: Goranko, V., and G. van Drimmelen, 2006, “Complete Axiomatization and Decidablity of the Alternating-Time Temporal Logic”, *Theoretical Computer Science*, 353: 93–117.

[^goranko-2003]: Goranko, V., A. Montanari, and G. Sciavicco, 2003, “Propositional Interval Neighborhood Logics”, *Journal of Universal Computer Science*, 9(9): 1137–1167.

[^goranko-2004]: –––, 2004, “A Road Map of Propositional Interval Temporal Logics and Duration Calculi”, *Journal of Applied Non-Classical Logics* (Special Issue on Interval Temporal Logics and Duration Calculi), 14(1–2): 11–56.

[^goranko-2010]: Goranko, V., and D. Shkatov, 2010, “Tableau-Based Decision Procedures for Logics of Strategic Ability in Multi-Agent Systems”, *ACM Transactions of Computational Logic*, 11(1): 3–51.

[^goré-1999]: Goré, R., 1999, “Tableau Methods for Modal and Temporal Logics”, in M. D’Agostino, D.M. Gabbay, R. Hahnle, and J. Posegga (eds.), *Handbook of Tableau Methods*, Dordrecht: Kluwer, pp. 297–396.

[^grädel-1999]: Grädel, E., and M. Otto, 1999, “On Logics With Two Variables”, *Theoretical Computer Science*, 224(1–2), pp. 73–113.

[^gurevich-1985a]: Gurevich, Y., and S. Shelah, 1985a, “The Decision Problem for Branching Time Logic”, *Journal of Symbolic Logic*, 50: 668–681.

[^gurevich-1985b]: –––, 1985b, “To the Decision Problem for Branching Time Logic”, in P. Weingartner, and G. Dold (eds.), *Foundations of Logic and Linguistics: Problems and their Solutions*, Plenum, pp. 181–198.

[^halpern-1986]: Halpern, J., and Y. Shoham, 1986. “A Propositional Modal Logic of Time Intervals”, in *Proceedings of the 2nd IEEE Symposium on Logic in Computer Science*, pp. 279–292. [Reprinted in *Journal of the ACM*, 38(4): 935–962, 1991.]

[^halpern-1989]: Halpern, J., and M. Vardi, 1989, “The Complexity of Reasoning about Knowledge and Time I: Lower Bounds”, *Journal of Computer and System Sciences*, 38(1): 195–237.

[^hamblin-1972]: Hamblin, C.L., 1972, “Instants and Intervals”, in J.T. Fraser, F. Haber, and G. Müller (eds.), *The Study of Time*, Berlin/Heidelberg: Springer, pp. 324–331.

[^hansen-1997]: Hansen, M.R., and C. Zhou, 1997, “Duration Calculus: Logical Foundations”, *Formal Aspects of Computing*, 9: 283–330.

[^hart-1986]: Hart, S., and M. Sharir, 1986, “Probabilistic Propositional Temporal Logics”, *Information and Control*, 70(2–3): 97–155.

[^hasle-2017]: Hasle, P., P. Blackburn, and P. Øhrstrøm (eds.), 2017, *Logic and Philosophy of Time: Themes from Prior* (Volume 1), Aalborg: Aalborg University Press.

[^hasle-2020]: Hasle, P., D. Jakobsen, and P. Øhrstrøm (eds.), 2020, *Logic and Philosophy of Time: The Metaphysics of Time* (Volume 4), Aalborg: Aalborg University Press.

[^hodkinson-2007]: Hodkinson, I., and M. Reynolds, 2007, “Temporal Logic”, in Blackburn et al. (2007), pp. 655–720.

[^hodkinson-2000]: Hodkinson, I., F. Wolter, and M. Zakharyaschev, 2000, “Decidable Fragments of First-Order Temporal Logics”, *Annals of Pure and Applied Logic*, 106(1–3): 85–134.

[^hodkinson-2001]: –––, 2001, “Monodic Fragments of First-Order Temporal Logics: 2000-2001 A.D.”, in *Logic for Programming, Artificial Intelligence, and Reasoning*, Proceedings of the 8th International Conference LPAR 2001, Springer, pp. 1–23.

[^hodkinson-2002]: –––, 2002, “Decidable and Undecidable Fragments of First-Order Branching Temporal Logics”, in *Proceedings of the 17th Annual IEEE Symposium on Logic in Computer Science*, IEEE Computer Society Press, pp. 393–402.

[^humberstone-1979]: Humberstone, I.L., 1979, “Interval Semantics for Tense Logic: Some Remarks”, *Journal of Philosophical Logic*, 8: 171–196.

[^ingthorsson-2016]: Ingthorsson, R.D., 2016, *McTaggart’s Paradox*, New York: Routledge.

[^jakobsen-2020]: Jakobsen, D., P. Øhrstrøm, M. Prior, and A. Rini (eds.), 2020, *Logic and Philosophy of Time: Three Little Essays. Arthur Prior in 1931* (Volume 3), Aalborg: Aalborg University Press.

[^kamide-2010]: Kamide, N., and H. Wansing, 2010, “Combining Linear-Time Temporal Logic with Constructiveness and Paraconsistency”, *Journal of Applied Logic*, 6: 33–61.

[^kamide-2011]: –––, 2011, “A Paraconsistent Linear-Time Temporal Logic”, *Fundamenta Informaticae*, 106: 1–23.

[^kamp-1968]: Kamp, J., 1968, *Tense Logic and the Theory of Linear Order*, PhD Thesis, University of California, Los Angeles.

[^kamp-1971]: –––, 1971, “Formal Properties of ‘Now’”, *Theoria*, 37: 227–273.

[^kamp-1979]: –––, 1979, “Events, Instants and Temporal Reference”, in R. Bäuerle, U. Egli, and A. von Stechow (eds.), *Semantics from Different Points of View*, Berlin: Springer, pp. 376–417.

[^kesten-2002]: Kesten, Y., and A. Pnueli, 2002, “Complete Proof System for QPTL”. *Journal of Logic and Computation*, 12(5): 701–745.

[^kofod-2020]: Kofod, J., 2020, “Arthur Prior’s Early Thoughts on Physics and Cosmology”, in Jakobsen et al. (2020), pp. 73–97.

[^kontchakov-2007]: Kontchakov, R., A. Kurucz, F. Wolter, and M. Zakharyaschev, 2007, “Spatial Logic + Temporal Logic = ?”, in M. Aiello, J. van Benthem, and I. Pratt-Hartmann (eds.), *Handbook of Spatial Logics*, Berlin: Springer, pp. 497–564.

[^kontchakov-2004]: Kontchakov, R., C. Lutz, F. Wolter, and M. Zakharyaschev, 2004, “Temporalising Tableaux”, *Studia Logica*, 76(1): 91–134.

[^konur-2013]: Konur, S., 2013, “A Survey on Temporal Logics for Specifying and Verifying Real-Time Systems”, *Frontiers of Computer Science*, 7(3): 370–403.

[^koymans-1990]: Koymans, R., 1990, “Specifying Real-Time Properties with Metric Temporal Logic”, *Real-Time Systems*, 2(4): 55–299.

[^kowalski-1986]: Kowalski, R.A., and M.J. Sergot, 1986, “A Logic-Based Calculus of Events”, *New Generation Computing*, 4: 67–95.

[^kröger-2008]: Kröger, F., and S. Merz, 2008, *Temporal Logic and State Systems* (EATCS Texts in Theoretical Computer Science Series), Berlin: Springer.

[^kuhn-2002]: Kuhn, S.T., and P. Portner, 2002, “Tense and Time”, in Gabbay and Guenthner (2002), pp. 277–346.

[^ladkin-1987]: Ladkin, P., 1987, *The Logic of Time Representation*, PhD Thesis, University of California, Berkeley.

[^lambalgen-2005]: van Lambalgen, M., and F. Hamm, 2005, *The Proper Treatment of Events*, Malden: Blackwell.

[^lamport-1994]: Lamport, L., 1994, “The Temporal Logic of Actions”, *ACM Transactions on Programming Languages and Systems*, 16(3): 872–923.

[^lindström-2007]: Lindström, S., and K. Segerberg, 2007, “Modal Logic and Philosophy”, in Blackburn et al. (2007), pp. 1149–1214

[^linsky-1994]: Linsky, B., and E. Zalta, 1994, “In Defense of the Simplest Quantified Modal Logic”, *Philosophical Perspectives*, 8: 431–458.

[^lorini-2013]: Lorini, E., 2013, “Temporal STIT Logic and Its Application to Normative Reasoning”, *Journal of Applied Non-Classical Logics*, 23(4): 372–399.

[^lutz-2008]: Lutz, K., F. Wolter, and M. Zakharyaschev, 2008, “Temporal Description Logics: A Survey”, *Proceedings of TIME 2008*, pp. 3–14.

[^ma-2001]: Ma, J., and B. Knight, 2001, “Reified Temporal Logics: An Overview”, *Artificial Intelligence Review*, 15(3): 189–217.

[^macfarlane-2003]: MacFarlane, J., 2003, “Future Contingents and Relative Truth”, *The Philosophical Quarterly*, 53(212): 321–336.

[^macfarlane-2014]: –––, 2014, *Assessment Sensitivity: Relative Truth and Its Applications*, Oxford: Oxford University Press.

[^manna-1992]: Manna, Z., and A. Pnueli, 1992, *The Temporal Logic of Reactive and Concurrent Systems* (Specification: Volume 1), Springer: New York.

[^mani-2005]: Mani, I., J. Pustejovsky, and R. Gaizauskas, 2005, *The Language of Time: A Reader*, Oxford: Oxford University Press.

[^marx-1999]: Marx, M., and M. Reynolds, 1999, “Undecidability of Compass Logic”, *Journal of Logic and Computation*, 9(6): 897–914.

[^mcarthur-1976]: McArthur, R., 1976, *Tense Logic*, Synthese Library, Springer.

[^mccarthy-1969]: McCarthy, J., and P.J. Hayes, 1969, “Some Philosophical Problems from the Standpoint of Artificial Intelligence”, in D. Michie, and B. Meltzer (eds.), *Machine Intelligence 4*, Edinburgh: Edinburgh University Press, pp. 463–502.

[^mcdermott-1982]: McDermott, D., 1982, “A Temporal Logic for Reasoning about Processes and Plans”, *Cognitive Science*, 6: 101–155.

[^mctaggart-1908]: McTaggart, E.J., 1908, “The Unreality of Time”, *Mind*, 17(68): 457–472.

[^merz-1992]: Merz, S., 1992, “Decidability and Incompleteness Results for First-Order Temporal Logics of Linear Time”, *Journal of Applied Non-Classical Logic*, 2(2): 139–156.

[^meulen-2005]: ter Meulen, A., 2005, “Temporal Reasoning in Natural Language”, in Fisher et al. (2005), pp. 559–585.

[^meyer-2013]: Meyer, U., 2013, *The Nature of Time*, Oxford: Oxford University Press.

[^montanari-1996]: Montanari, A., 1996, *Metric and Layered Temporal Logic for Time Granularity*, PhD Thesis (Institute for Logic, Language, and Computation Dissertation Series, Volume: 1996–02), University of Amsterdam.

[^montanari-1996-2]: Montanari, A., and A. Policriti, 1996, “Decidability Results for Metric and Layered Temporal Logics”, *Notre Dame Journal Formal Logic*, 37(2): 260–282.

[^moss-2007]: Moss, S.L., and H.J. Tiede, 2007, “Applications of Modal Logic in Linguistics”, in Blackburn et al. (2007), pp. 1003–1076.

[^moszkowski-1983]: Moszkowski, B., 1983, *Reasoning about Digital Circuits*, PhD Thesis (Technical Report STAN-CS-83–970), Department of Computer Science, Stanford University.

[^müller-2011]: Müller, T., 2011, “Tense or Temporal Logic”, in R. Pettigrew (ed.), *The Continuum Companion to Philosophical Logic*, London: Continuum, pp. 324–350.

[^müller-2014]: ––– (ed.), 2014, *Nuel Belnap on Indeterminism and Free Action* (Outstanding Contributions to Logic: Volume 2), Springer.

[^nishimura-1979]: Nishimura, H., 1979, “Is the Semantics of Branching Structures Adequate for Non-Metric Ockhamist Tense Logics?”, *Journal of Philosophical Logic*, 8: 477–478.

[^ogihara-2007]: Ogihara, T., 2007, “Tense and Aspect in Truth-Conditional Semantics”, *Lingua*, 117:392–418.

[^ogihara-2011]: –––, 2011, “Tense”, in C. Maienborn, K. von Heusinger, and P. Portner (eds.), *Semantics: An International Handbook of Natural Language Meaning*, de Gruyter, pp. 1463–1484.

[^øhrstrøm-2009]: Øhrstrøm, P., 2009, “In Defense of the Thin Red Line: A Case for Ockhamism”, *Humana Mente*, 8: 17–32.

[^øhrstrøm-2019]: –––, 2019, “A Critical Discussion of Prior’s Philosophical and Tense-Logical Analysis of the Ideas of Indeterminism and Human Freedom”, *Synthese*, 196(1): 69–85.

[^øhrstrøm-2022]: Øhrstrøm, P., and M. Gonzalez, 2022, “Prior’s Big Y and the Idea of Branching Time”, *History and Philosophy of Logic*, online first.

[^øhrstrøm-1995]: Øhrstrøm, P., and P. Hasle, 1995, *Temporal Logic: From Ancient Ideas to Artificial Intelligence*, Dordrecht: Kluwer Academic Publishers.

[^øhrstrøm-2006]: –––, 2006, “Modern Temporal Logic: The Philosophical Background”, in *Handbook of the History of Logic* (Volume 7), pp. 447–498.

[^øhrstrøm-2019-2]: –––, 2019, “The Significance of the Contributions of A.N. Prior and Jerzy Łoś in the Early History of Modern Temporal Logic”, in Blackburn et al. (2019), pp. 31–40.

[^pani-2001]: Pani, A.K., and G.P. Bhattacharjee, 2001, “Temporal Representation and Reasoning in Artificial Intelligence: A Review”, *Mathematical and Computer Modelling*, 34: 55–80.

[^parsons-1990]: Parsons, T., 1990, *Events in the Semantics of English: A Study in Subatomic Semantics*, Cambridge: MIT Press.

[^partee-1973]: Partee, B., 1973, “Some Structural Analogies between Tenses and Pronouns in English”, *The Journal of Philosophy*, 70(18): 601–609.

[^passy-1985]: Passy, S., and T. Tinchev, 1985. “Quantifiers in Combinatory PDL: Completeness, Definability, Incompleteness”, in *Fundamentals of Computation Theory FCT 85* (Lecture Notes in Computer Science: Volume 199), Berlin: Springer, pp. 512–519.

[^pinto-1995]: Pinto, J., and R. Reiter, 1995, “Reasoning about Time in the Situation Calculus”, *Annals of Mathematics and Artificial Intelligence*, 14(2–4): 251–268.

[^ploug-2012]: Ploug, T., and P. Øhrstrøm, 2012, “Branching Time, Indeterminism, and Tense Logic: Unveiling the Prior-Kripke Letters”, *Synthese*, 188(3): 367–379.

[^pnueli-1977]: Pnueli, A., 1977, “The Temporal Logic of Programs”, *Proceedings of the 18th IEEE Symposium on Foundations of Computer Science*, pp. 46–67.

[^prior-1957]: Prior, A.N., 1957, *Time and Modality*, Oxford: Oxford University Press.

[^prior-1959]: –––, 1959, “Thank Goodness that’s over”, *Philosophy*, 34(128): 12–17.

[^prior-1967]: –––, 1967, *Past, Present and Future*, Oxford: Oxford University Press.

[^prior-1968]: –––, 1968, *Papers on Time and Tense*, Oxford: Oxford University Press. [New edition: P. Hasle et al. (eds.), Oxford: Oxford University Press, 2003.]

[^prior-1968-2]: –––, 1968, “‘Now’”, *Noûs*, 2(2): 101–119.

[^reichenbach-1947]: Reichenbach, H., 1947, *Elements of Symbolic Logic*, New York: Macmillan.

[^reichgelt-2005]: Reichgelt H., and L. Vila, 2005, “Temporal Qualification in Artificial Intelligence”, in Fisher et al. (2005), pp. 167–194.

[^rescher-1971]: Rescher, N., and A. Urquhart, 1971, *Temporal Logic*, Berlin: Springer.

[^reynolds-1994]: Reynolds, M., 1994, “Axiomatizing U and S over Integer Time”, in D.M. Gabbay, and H.J. Ohlbach (eds.), *Temporal Logic*, Proceedings of the First International Conference ICTL 1994 (Lecture Notes in Artificial Intelligence: Volume 828), Berlin/Heidelberg: Springer, pp. 117–132.

[^reynolds-1996]: –––, 1996, “Axiomatising First-Order Temporal Logic: Until and Since over Linear Time”, *Studia Logica*, 57(2–3): 279–302.

[^reynolds-2001]: –––, 2001, “An Axiomatization of Full Computation Tree Logic”, *Journal of Symbolic Logic*, 66: 1011–1057.

[^reynolds-2002]: –––, 2002, “Axioms for Branching Time”. *Journal of Logic and Computation*, 12(4): 679–697.

[^reynolds-2003]: –––, 2003, “An Axiomatization of Prior’s Ockhamist Logic of Historical Necessity”, in Balbiani et al. (eds.), *Advances in Modal Logic* (Volume 4), London: College Publications, pp. 355–370.

[^reynolds-2005]: –––, 2005, “An Axiomatization of PCTL\*”, *Information and Computation*, 201(1): 72–119.

[^reynolds-2007]: –––, 2007, “A Tableau for Bundled CTL”, *Journal of Logic and Computation*, 17(1): 117–132.

[^reynolds-2010]: –––, 2010, “The Complexity of Temporal Logic over the Reals”, *Annals of Pure and Applied Logic*, 161(8): 1063–1096.

[^reynolds-2011]: –––, 2011, “A Tableau-Based Decision Procedure for CTL\*”, *Formal Aspects of Computing*, 23(6): 739–779.

[^reynolds-2014]: –––, 2014, “A Tableau for Temporal Logic over the Reals”, in Goré et al. (eds.), *Advances in Modal Logic* (Volume 10), London: College Publications, pp. 439–458.

[^röper-1980]: Röper, P., 1980, “Intervals and Tenses”, *Journal of Philosophical Logic*, 9: 451–469.

[^rumberg-2016]: Rumberg, A., 2016, “Transition Semantics for Branching Time”, *Journal of Logic, Language and Information*, 25(1): 77–108.

[^rumberg-2019]: –––, 2019, “Actuality and Possibility in Branching Time: The Roots of Transition Semantics”, in Blackburn et al. (2019), pp. 145–161.

[^rumberg-2019-2]: Rumberg, A., and A. Zanardo, 2019, “First-Order Definability of Transition Structures”, *Journal of Logic, Language and Information*, 28(3): 459–488.

[^segerberg-1970]: Segerberg, K., 1970, “Modal Logics with Linear Alternative Relations”, *Theoria*, 36: 301–322.

[^segerberg-1992]: –––, 1992, “Getting Started: Beginnings in the Logic of Action”, *Studia Logica*, 51: 347–378.

[^shoham-1987]: Shoham, Y., 1987, “Temporal Logic in AI: Semantical and Ontological Considerations”, *Artificial Intelligence*, 33: 89–104.

[^steedman-1997]: Steedman, M., 1997, “Temporality”, in J. van Benthem, and A. ter Meulen (eds.), *Handbook of Logic and Language*, Amsterdam: Elsevier, pp. 925–969.

[^stirling-1992]: Stirling, C., 1992, “Modal and Temporal Logics”, in *Handbook of Logic in Computer Science* (Computational Structures: Volume 2), Oxford, Clarendon Press, pp. 477–563.

[^thomason-1970]: Thomason, R.H., 1970, “Indeterminist Time and Truth-Value Gaps”, *Theoria*, 36(3): 264–281.

[^thomason-1984]: –––, 1984, “Combinations of Tense and Modality”, in D.M. Gabbay, and F. Guenther (eds.), *Handbook of Philosophical Logic* (Extensions of Classical Logic: Volume 2), Dordrecht: Reidel, pp. 135–165. [New edition in Gabbay and Guenthner (2002), pp. 205–234.]

[^tkaczyk-2019]: Tkaczyk, M., and T. Jarmużek, 2019, “Jerzy Łoś Positional Calculus and the Origin of Temporal Logic”, *Logic and Logical Philosophy*, (28): 259–276.

[^uckelman-2007]: Uckelman, S.L., and J. Uckelman, 2007, “Modal and Temporal Logics for Abstract Space-Time Structures”, in *Studies in History and Philosophy of Science* (Part B: Studies in History and Philosophy of Modern Physics), 38(3): 673–681.

[^vardi-2007]: Vardi, M., 2007, “Automata-Theoretic Techniques for Temporal Reasoning”, in Blackburn et al. (2007), pp. 971–989.

[^vardi-1994]: Vardi, M., and P. Wolper, 1994, “Reasoning about Infinite Computations”, *Information and Computation*, 115: 1–37.

[^venema-1990]: Venema, Y., 1990, “Expressiveness and Completeness of an Interval Tense Logic”, *Notre Dame Journal of Formal Logic*, 31: 529–547.

[^venema-1991]: –––, 1991, “A Modal Logic for Chopping Intervals”, *Journal of Logic and Computation*, 1(4): 453–476.

[^venema-1993]: –––, 1993, “Completeness via Completeness: Since and Until”, in M. de Rijke (ed.), *Diamonds and Defaults*, Dordrecht: Kluwer, pp. 279–286.

[^venema-2001]: –––, 2001, “Temporal Logic”, in L. Goble (ed.), *Blackwell Guide to Philosophical Logic*, Oxford: Blackwell Publishers.

[^vila-1994]: Vila, L., 1994, “A Survey on Temporal Reasoning in Artificial Intelligence”, *AI Communications*, 7: 4–28.

[^vila-2005]: –––, 2005, “Formal Theories of Time and Temporal Incidence”, in Fisher et al. (2005), pp. 1–24.

[^wölfl-1999]: Wölfl, S., 1999, “Combinations of Tense and Modality for Predicate Logic”, *Journal of Philosophical Logic*, 28: 371–398.

[^wolper-1985]: Wolper, P., 1985, “The Tableau Method for Temporal Logic: An Overview”, *Logique et Analyse*, 28(110–111): 119–136.

[^wolter-2000]: Wolter F., and M. Zakharyaschev, 2000, “Temporalizing Description Logics”, in D.M. Gabbay, and M. de Rijke (eds.), *Frontiers of Combining Systems II*, New York: Wiley, pp. 379–401.

[^wolter-2002]: –––, 2002, “Axiomatizing the Monodic Fragment of First-Order Temporal Logic”, *Annals of Pure and Applied Logic*, 118(1–2): 133–145.

[^xu-1988]: Xu, M., 1988, “On some U,S-Tense Logics”, *Journal of Philosophical Logic*, 17: 181–202.

[^zanardo-1985]: Zanardo, A., 1985, “A Finite Axiomatization of the Set of Strongly Valid Ockhamist Formulas”, *Journal of Philosophical Logic*, 14: 447–468.

[^zanardo-1990]: –––, 1990, “Axiomatization of ‘Peircean’ Branching-Time Logic”, *Studia Logica*, 49: 183–195.

[^zanardo-1991]: –––, 1991, “A Complete Deductive System for Since-Until Branching Time Logic”, *Journal of Philosophical Logic*, 20: 131–148.

[^zanardo-1996]: –––, 1996, “Branching-Time Logic with Quantification over Branches: The Point of View of Modal Logic”, *Journal of Symbolic Logic*, 61: 1–39.

[^zanardo-1998]: –––, 1998, “Undivided and Indistinguishable Histories in Branching-Time Logics”, *Journal of Logic, Language and Information*, 7(3): 297–315.

[^zanardo-1999]: Zanardo, A., B. Barcellan, and M. Reynolds, 1999, “Non-Definability of the Class of Complete Bundled Trees”, *Logic Journal of the IGPL* (Special Issue on Temporal Logic), 7(1): 125–136.
