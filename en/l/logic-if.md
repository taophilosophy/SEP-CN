# Independence Friendly Logic
**First published Mon Feb 9, 2009; substantive revision Thu Sep 15, 2022**

*Tulenheimo, Tero*

Independence friendly logic (IF logic, IF first-order logic) is an extension of first-order logic. In it, more quantifier dependencies and independencies can be expressed than in first-order logic. Its quantifiers range over individuals only; semantically IF first-order logic, however, has the same expressive power as existential second-order logic. IF logic lacks certain metaproperties that first-order logic has (axiomatizability, Tarski-type semantics). On the other hand, IF logic admits a self-applied truth-predicate – a property that first-order logic notoriously does not enjoy. Philosophical issues discussed in connection with IF logic include reformulating the logicist program, the question of truth in axiomatic set theory, and the nature of negation. Work in IF logic has also inspired alternative generalizations of first-order logic: slash logic and dependence logic.

## 1. Introduction: Quantifier Dependence

In mathematical prose, one can say things such as ‘for all real numbers $a$ and for all positive real numbers *ε*, there exists a positive real number *δ* depending on *ε* but not on $a$, such that…’ What is important here is quantifier dependence. The existential quantifier ‘there exists *δ*’ is said to depend on the universal quantifier ‘for all *ε*’ but not on the universal quantifier ‘for all $a$.’ It was an essential part of Karl Weierstrass’s (1815–1897) work in the foundations of analysis that he defined the notions of limit, continuity, and derivative in terms of quantifier dependence.[^note-1] For a concrete example, a function $f : D \rightarrow \mathbf{R}$ is *continuous*, if for all $a$ in the set $D$ and for all $\varepsilon \gt 0$ there exists $\delta \gt 0$ such that for all $x$ in $D$, if $|x - a| \lt \delta$, then $|f(x) - f(a)| \lt \varepsilon$. The definition of *uniform continuity* is obtained from that of continuity by specifying that the quantifier ‘there exists *δ*’ depends only on the quantifier ‘for all *ε*,’ not on the quantifier ‘for all $a$.’[^note-2]

*Independence friendly first-order logic* (a.k.a. *IF first-order logic*, *IF logic*) was introduced by Jaakko Hintikka and Gabriel Sandu in their article ‘Informational Independence as a Semantical Phenomenon’ (1989); other early sources are Hintikka’s booklet *Defining Truth, the Whole Truth, and Nothing but the Truth* (1991) and Sandu’s Ph.D. thesis (1991).[^note-3] IF first-order logic is an extension of first-order logic, involving a specific syntactic device ‘/’ (slash, independence indicator), which has at the object language level the same effect as the meta-level modifier ‘but does not depend on’ has in the example just considered. In the notation of IF logic, the logical form of the statement that a function $f$ is uniformly continuous would be $(\forall a)(\forall \varepsilon)(\exists \delta /\forall a)(\forall x) R$, to be contrasted with the form of the statement that $f$ merely is continuous, $(\forall a)(\forall \varepsilon)(\exists \delta)(\forall x) R$.

In the introductory examples in the present and the following section, let us confine attention to formulas in *prenex form*: a string of quantifiers followed by a quantifier-free first-order formula. If in a first-order sentence of such a form an existential quantifier $\exists y$ lies in the syntactic scope of a universal quantifier $\forall x$, then by the semantics $\exists y$ automatically depends on $\forall x$. This is so *e.g.* with the sentence $(\forall x)(\exists y) R(x, y)$. The dependence of $\exists y$ on $\forall x$ means that the *witness* of $\exists y$ may vary with the value interpreting $\forall x$. In order for the sentence to be true in a model $M$, it suffices that there be a function $f$ such that $R(a, f(a))$ holds in $M$, for any $a$ interpreting $\forall x$. Such functions, spelling out the dependencies of witnesses for existential quantifiers on interpretations of universal quantifiers, are known in logical literature as *Skolem functions*.[^note-4] For comparison, in the sentence $(\exists y)(\forall x) R(x, y)$ the quantifier $\exists y$ does not depend on the quantifier $\forall x.$ For this sentence to be true in $M$, one and the same witness $c$ for $\exists y$ must be good against any interpretation $a$ of $\forall x$, so that $R(a, c)$ holds in $M$. The corresponding Skolem function is a constant.[^note-5]

In IF first-order logic, syntactic scopes no longer determine the semantic relation of dependence. In the sentence $(\forall x)(\forall y)(\exists z/\forall y) R(x, y, z)$, for instance, $\exists z$ is syntactically subordinate to both $\forall x$ and $\forall y$, but is marked as independent of $\forall y$, and is hence dependent only on $\forall x$. Semantically this means that the witness of $\exists z$ must be given by a function taking as an argument the interpretation of $\forall x$, but not that of $\forall y$. In order for $(\forall x)(\forall y)(\exists z/\forall y) R(x, y, z)$ to be true in $M$, there must be a function $f$ of one argument such that $R(a, b, f(a))$ holds in $M$, for any $a$ interpreting $\forall x$ and any $b$ interpreting $\forall y$.

What is gained with the slash notation? After all, clearly *e.g.* $(\forall x)(\forall y)(\exists z/\forall y) R(x, y, z)$ is true in a model $M$ iff[^note-6] the first-order sentence $(\forall x)(\exists z)(\forall y) R(x, y, z)$ is true therein. As a matter of fact, the expressive power of IF logic exceeds that of first-order logic. Consider the sentence $(\forall x)(\exists y)(\forall z)(\exists w/\forall x) R(x, y, z, w)$. Its truth-condition is of the following form: there are one-argument functions $f$ and $g$ such that $R(a, f(a), b, g(b))$ holds in $M$, for any $a$ interpreting $\forall x$ and $b$ interpreting $\forall z$.[^note-7] So the sentence is true iff the following sentence (\*) containing a *finite partially ordered quantifier* is true:

$$\tag{*} \begin{matrix} \forall x \exists y \\ \forall z \exists w \end{matrix} R(x,y,z,w) $$

For, by definition (\*) is true in a model $M$ iff the second-order sentence $(\exists f)(\exists g)(\forall x)(\forall z) R(x, f(x), z, g(z))$ is true therein. The latter may be termed the *Skolem normal form* of (\*). It says that Skolem functions providing witnesses for the quantifiers $\exists y$ and $\exists w$ in (\*) exist. Finite partially ordered quantifiers – a.k.a. *Henkin quantifiers* or *branching quantifiers* – were proposed by Leon Henkin (1961)[^henkin-1961] and have been subsequently studied extensively.[^note-8] They are two-dimensional syntactic objects

$$\begin{matrix} Q_{11} \ldots Q_{1n} \\ \vdots \\ Q_{m1} \ldots Q_{mn} \end{matrix}$$

where each $Q_{ij}$ is either $\exists x_{ij}$ or $\forall x_{ij}$. They are naturally interpreted by making systematic use of Skolem functions.

Let us denote by $\mathbf{FPO}$ the logic of finite partially ordered quantifiers obtained from first-order logic as follows: if *φ* is a first-order formula and $\mathbf{Q}$ is a finite partially ordered quantifier, then $\mathbf{Q}\phi$ is a formula of $\mathbf{FPO}$.[^note-9] With $\mathbf{FPO}$ it is possible to express properties that are not definable in first-order logic. The first example was provided by Andrzej Ehrenfeucht (cf. Henkin 1961)[^henkin-1961]: a sentence that is true in a model iff the size of its domain is infinite. It turns out that $\mathbf{FPO}$ can be translated into IF logic (see *Subsect*. 4.1). Therefore IF logic is more expressive than first-order logic.

The deepest reason for IF logic, as Hintikka saw it, is that the relations of dependence and independence between *quantifiers* are the only way of expressing relations of dependence and independence between *variables* on the first-order level (Hintikka 1996: 34–35, 73–74; 2002a: 404–405; 2006a: 71, 515)[^hintikka-1996][^hintikka-1996-2]. To understand this remark properly, recall that relations of quantifier (in)dependence are *semantic* relations, but *syntactically expressed*. More precisely, in IF logic the (in)dependence relations are syntactically expressed by the interplay of two factors: syntactic scope and the independence indicator ‘/’. In a given sentence, an existential quantifier $\exists x$, say, depends on precisely those universal quantifiers within whose scope $\exists x$ lies, but of which $\exists x$ is not marked as independent using the slash sign. What Hintikka means when he speaks of (in)dependence relations between variables, are *functional dependencies* between quantities in a model. The kinetic energy of a material body depends on its mass and its speed, but does not depend on the particular material body being considered. This fact can be expressed in IF logic by the sentence

$(\forall b)(\forall m)(\forall v)(\exists e/\forall b)$(if $b$ is a material body which moves at the velocity $v$ and has the mass $m$, then the kinetic energy $e$ of $b$ equals $\frac{1}{2} mv^2 )$.

That this sentence states the existence of a functional dependence of kinetic energy on mass and speed is particularly clearly seen from the fact that if the sentence is true, the unique Skolem function for the quantifier $\exists e$ actually *is* the physical law connecting masses, speeds and kinetic energies (cf. Hintikka 1996: 34–35)[^hintikka-1996][^hintikka-1996-2].

While first-order logic can only express some relations between variables, IF first-order logic with its greater expressive power can express more. Actually, IF logic is calculated to capture all such relations (Hintikka 1996: 75–77; 2002a: 404–405; 2002b: 197; 2006a: 72)[^hintikka-1996][^hintikka-1996-2]. This idea must, in its full generality, be seen as programmatic. For a more general framework, cf. Hintikka (2006a: 515, 536, 752; 2008), Sandu & Sevenster (2010), Sandu (2013)[^sandu-2013], Sandu (2014)[^sandu-2014].

Among philosophical issues that have been addressed in connection with IF logic are the reconstruction of mathematical reasoning on the first-order level (Hintikka 1996, 1997)[^hintikka-1996][^hintikka-1997][^hintikka-1997-2][^hintikka-1996-2][^hintikka-1997-3], definability of a self-applied truth predicate (Hintikka 1991, 1996, 2001; Sandu 1998)[^hintikka-1991][^hintikka-1996][^hintikka-2001][^hintikka-1991-2][^hintikka-1996-2][^sandu-1998], truth and axiomatic set theory (Hintikka 1996, 2004a)[^hintikka-1996][^hintikka-2004a][^hintikka-1996-2], and insights into the nature of negation (Hintikka 1991, 1996, 2002; Hintikka & Sandu 1989; Sandu 1994)[^hintikka-1991][^hintikka-1996][^hintikka-1989][^hintikka-1991-2][^hintikka-1996-2][^sandu-1994]. These issues will be discussed in *Sections* 4 and 5.

## 2. The Background of IF Logic: Game-theoretical Semantics

### 2.1. Semantic games

Inspired by Ludwig Wittgenstein’s idea of a language-game, Hintikka (1968)[^hintikka-1968] introduced the basic framework of what came to be known as *game-theoretical semantics* (a.k.a. GTS). The basic lesson Hintikka adopts from Wittgenstein is that words – in particular quantifiers – are associated with activities that render them meaningful: words often have meaning only in the context of certain types of action (Hintikka 1968: 55–56)[^hintikka-1968]. Wittgenstein said that by ‘language-game’ he means ‘the whole, consisting of language and the actions into which it is woven’ (Wittgenstein 1953: I, *Sect.* 7)[^wittgenstein-1953].

It becomes natural to ask which are the activities that go together with quantifiers. As Hintikka explains (see Hintikka 2006a: 41, 67)[^hintikka-2006a], Wittgenstein had taken it as a criterion for something to be an object that it can be looked for and found. Applying this idea to quantifiers with such objects as values, Hintikka was led to formulate *semantic games* for quantifiers. Crucially, these semantic games can be formulated as games in the strict sense of game theory; but at the same time they are exact codifications of language-games in Wittgenstein’s sense, at least if one accepts that the activities associated with quantifiers are ‘looking for’ and ‘finding.’[^note-10]

Semantic games $G(\phi , M)$ for first-order sentences *φ* are two-player zero-sum games of perfect information, played on a given model $M$. Let us call the two players simply player 1 and player 2.[^note-11] The games are most easily explained for sentences in prenex form. Universal quantifiers mark a move of player 1, while existential quantifiers prompt a move by player 2. In both cases, the relevant player must choose an individual from the domain $\rM$ of $M$.[^note-12] If

$$ \phi = (\forall x)(\exists y)(\forall z)(\exists w) R(x, y, z, w), $$

the game is played as follows. First, player 1 picks out an individual $a$, whereafter player 2 chooses an individual $b$. Then player 1 proceeds to choose a further individual $c$, to which player 2 responds by picking out an individual $d$. Thereby a play of the game has come to an end. The tuple $(a, b, c, d)$ of individuals chosen determines the winner of the play. If the quantifier-free formula $R(a, b, c, d)$ holds in $M$, player 2 wins, if not, player 1 wins.

The fact that one of the players wins a single play of game $G(\phi , M)$ does not yet tell us anything about the truth-value of the sentence *φ*. Truth and falsity are characterized in terms of the notion of *winning strategy*. The sentence $(\forall x)(\exists y)(\forall z)(\exists w) R(x, y, z, w)$ is *true* in $M$ if there is a winning strategy for player 2 in the game just described: a recipe telling player 2 what to do, when (a specified amount of) information about the opponent’s earlier moves is given. Technically, the requirement is that there be *strategy functions* $f$ and $g$, such that for any choices $a$ and $c$ by player $1, R(a, f(a), c, g(a, c))$ holds in $M$. Observe that strategy function $f$ is a Skolem function for the quantifier $\exists y$ in *φ*, and similarly $g$ is a Skolem function for the quantifier $\exists w$. The sentence *φ* is *false* in $M$ if there is a winning strategy (set of strategy functions) for player 1 in the corresponding game: a constant $c$ and a function $h$ such that for any choices $b$ and $d$ by player $2, R(c, b, h(b), d)$ fails to hold in $M$.

Game-theoretical interpretation of quantifiers was already suggested by Henkin (1961; cf. Hintikka 1968: 64)[^hintikka-1968]. Henkin also pointed out, in effect, the connection between a full set of Skolem functions and a winning strategy for player 2. Hintikka (1968)[^hintikka-1968] noted that conjunctions are naturally interpreted by a choice between the two conjuncts, made by player 1; similarly, disjunctions can be interpreted by a choice by player 2 between the two disjuncts.[^note-13] Further, Hintikka proposed to interpret negation as a transposition of the roles of ‘verifier’ and ‘falsifier’ (for more details, see *Subsect.* 3.2).

The game-theoretical description of semantic games does not mention the activities of searching and finding; for such an abstract description it suffices to speak of the players making a move. Also, the characterization of truth and falsity as the existence of a winning strategy for player 2 and player 1, respectively, does not refer to efforts on the part of the players – say efforts to establish truth or to find witnesses. The truth or falsity of a sentence is a matter of ‘combinatorics’: it is an issue of the existence of a set of functions with certain properties (cf. Hintikka 1968, 1996; Hodges 2013)[^hintikka-1968][^hintikka-1996][^hintikka-1996-2][^hodges-2013]. So what happened to the original philosophical conception according to which the meanings of quantifiers are tied to the activities of searching and finding? Hintikka’s idea is that asserting a sentence involving quantifiers is to make a claim about what can and what cannot happen when a certain language-game is played; using language involving quantifiers requires mastering the rules of the corresponding semantic games (Hintikka 1968: *Sect.* 8, 1996: 128, 2006a: 538)[^hintikka-1968][^hintikka-1996][^hintikka-2006a][^hintikka-1996-2]. What is the content of such a claim in connection with the sentence $\forall x\exists y R(x, y)$? That whichever individual player 1 chooses from the domain for $\forall x$, player 2 can find a witness individual for $\exists y$. In other words, given a value for $\forall x$ (which itself can be seen as the result of the search by player 1), if player 2 is allowed to search free from any practical constraints, she will find a value for $\exists y$ so that player 2 wins the resulting play. Even though semantic games themselves can be defined without recourse to activities such as looking for or finding, these activities play an important conceptual role when the language user reasons *about* these games.

Hintikka (1973a)[^hintikka-1973a] initiated the application of GTS to the study of natural language. This work was continued notably by Hintikka & Kulas (1983, 1985), where game-theoretical rules for such items as negation, anaphoric pronouns, genitives, tenses, intensional verbs, certain prepositional constructions, and proper names were given, and the distinction between abstract meaning and strategic meaning drawn.[^note-14]

### 2.2. Imperfect information

The framework of GTS enables asking questions of a game-theoretical nature about semantic evaluation. Hintikka (1973a)[^hintikka-1973a] observed that semantic games with imperfect information are devised without any difficulty. As logical examples he used $\mathbf{FPO}$ sentences. (For examples related to natural languages, see *Subsect*. 5.4.)

From the vantage point of GTS, independence friendly first-order logic differs from first-order logic in that semantic games correlated with formulas of the former are, in general, games of imperfect information, while any game associated with a first-order formula is a game of perfect information. Consider the game for $\forall x\exists y\forall z(\exists w/\forall x) R(x, y, z, w)$, played on a model $M$. A play of this game proceeds exactly as plays of the game corresponding to $\forall x\exists y\forall z\exists w R(x, y, z, w)$. First, player 1 chooses an individual $a$, whereafter player 2 chooses an individual $b$. Then player 1 proceeds to pick out a further individual $c$, to which player 2 responds by choosing an individual $d$. So a play of the game has come to an end. The play is won by player 2, if indeed $R(a, b,c, d)$ holds in $M$; otherwise it is won by player 1. But $\exists w$ was marked as independent of $\forall x$ – why does not this fact show in any way in the course of a play?

One might be tempted to add to the description of a play: ‘player 2 chooses a value for $\exists w$ in ignorance of the value for $\forall x$.’ However, such a paraphrase would not clarify the conceptual situation. It makes no sense to speak of the independence of a move from other given moves with reference to a single play; this can only be done with reference to a multitude of plays. Quantifier independence can be conceptualized in game-theoretical terms making use of the notion of *strategy*. In the example, a strategy of player 2 is a set $\{f, g\}$ of strategy functions, function $f$ providing a value for $\exists y$ depending on the value of $\forall x$, and function $g$ providing a value for $\exists w$ depending on the value chosen for $\forall z$ but not on the value chosen for $\forall x$. The strategy $\{f, g\}$ is, then, a winning strategy for player 2, iff $R(a, f(a), c, g(c))$ holds in $M$, for all values $a$ chosen for $\forall x$ and $c$ chosen for $\forall z$. One precise way of implementing the idea that player 2 is ‘ignorant’ of the move player 1 made for $\forall x$ is to say that **(a)** strategy functions always only take as arguments the opponent’s moves, and **(b)** the strategy function corresponding to $\exists w$ may not take as its argument the move player 1 made for $\forall x$.

A sentence of IF first-order logic is by definition true in a model $M$ iff there is a winning strategy for player 2 in the correlated game, and false iff there is a winning strategy for player 1 in the correlated game. There are sentences which under these criteria are neither true nor false; they are called *non-determined* (see *Subsect.* 3.3).

In Hintikka’s judgement, the game-theoretical semantics of quantifiers can be taken to have the same rationale that was mentioned as the deepest reason for IF first-order logic at the end of *Section* 1: GTS is a method of representing, on the first-order level, the (in)dependence relations between variables by means of informational (in)dependence in the sense of game theory (Hintikka 1991: 12–13, 2006a: 535)[^hintikka-1991][^hintikka-2006a][^hintikka-1991-2].

## 3. The Syntax and Semantics of IF First-order Logic

In the literature one can find essentially different formulations of ‘IF first-order logic.’ The differences are not restricted to syntax – examples of applying different semantic ideas can be found as well.

As already noted, there is a systematic connection between the Skolem functions and strategy functions of player 2. In connection with formulas in prenex form, a Skolem function for an existential quantifier is a function of the values assigned to the preceding *universal* quantifiers, but *not* a function of the values assigned to the preceding existential quantifiers.[^note-15] Skolem functions are strategy functions taking as arguments exclusively moves made by player 1. Generally a strategy for a player in a two-player game *can* perfectly well make use of the previous choices of either player. Hodges (2007)[^hodges-2007] stresses that it makes a difference on which notion – Skolem function or strategy function – the semantics of imperfect information is based. Hodges (1997a)[^hodges-1997a] adopted the notational convention of writing, say, $(\exists y/x)$ where Hintikka writes $(\exists y/\forall x)$, hence marking the difference between semantic games formulated in terms of arbitrary strategy functions and those whose strategy functions are in effect Skolem functions; the variable $x$ in $(\exists y/x)$ can be ‘bound’ by any syntactically preceding quantifier carrying the variable $x$. Hodges proposed to employ the former formulation, while in Hintikka (1991, 1995, 1996, 2002)[^hintikka-1991][^hintikka-1995][^hintikka-1996][^hintikka-1991-2][^hintikka-1996-2] and Sandu (1993, 1994)[^sandu-1993][^sandu-1994] the latter formulation is employed. Hodges (2007: 119)[^hodges-2007] writes:

> [W]e refer to the logic with my notation and the general game semantics as *slash logic*. During recent years many writers in this area (but never Hintikka himself) have transferred the name ‘IF logic’ to slash logic, often without realising the difference. Until the terminology settles down, we have to beware of examples and proofs that don’t make clear which semantics they intend.

The distinction that Hodges makes between slash logic and IF logic serves to bring order to the mishmash of different formulations of IF first-order logic to be found in the literature.[^note-16]

### 3.1. Syntax

IF first-order logic is an extension of first-order logic. Now, any first-order formula is equivalent to a first-order formula in which no variable occurs both free and bound, and in which no two nested quantifiers carry the same variable. Formulas meeting these two syntactic conditions will be termed *regular*. Henceforth we systematically restrict attention to regular first-order formulas.[^note-17] A *vocabulary* (signature, non-logical terminology) is any countable set *τ* of relation symbols (each of which carries a fixed arity), function symbols (again each with a fixed arity), and constant symbols. The first-order logic of vocabulary *τ* will be referred to as $\mathbf{FO}[\tau]$. It is assumed here that among the logical symbols of first-order logic there is the *identity symbol* (=). The identity symbol is syntactically a binary relation symbol, but its semantic interpretation is fixed in a way that the interpretations of the items in the non-logical terminology are not.

A formula of $\mathbf{FO}[\tau]$ is in *negation normal form*, if all occurrences of the negation symbol ${\sim}$ immediately precede an atomic formula. The set of *formulas* of IF first-order logic of vocabulary *τ* (or $\mathbf{IFL}[\tau])$ can be defined as the smallest set such that:

1. If *φ* is a formula of $\mathbf{FO}[\tau]$ in negation normal form, *φ* is a formula.
2. If *φ* is a formula and in *φ* a token of $(\exists x)$ occurs in the syntactic scope of a number of universal quantifiers which include $(\forall y_1),\ldots ,(\forall y_n)$, the result of replacing in *φ* that token of $(\exists x)$ by $(\exists x/\forall y_1 ,\ldots ,\forall y_n)$ is a formula.
3. If *φ* is a formula and in *φ* a token of $\vee$ occurs in the syntactic scope of a number of universal quantifiers which include $(\forall y_1),\ldots ,(\forall y_n)$, the result of replacing in *φ* that token of $\vee$ by $(\vee /\forall y_1 ,\ldots ,\forall y_n)$ is a formula.
4. If *φ* is a formula and in *φ* a token of $(\forall x)$ occurs in the syntactic scope of a number of existential quantifiers which include $(\exists y_1),\ldots ,(\exists y_n)$, the result of replacing in *φ* that token of $(\forall x)$ by $(\forall x/\exists y_1 ,\ldots ,\exists y_n)$ is a formula.
5. If *φ* is a formula and in *φ* a token of $\wedge$ occurs in the syntactic scope of a number of existential quantifiers which include $(\exists y_1),\ldots ,(\exists y_n)$, the result of replacing in *φ* that token of $\wedge$ by $(\wedge /\exists y_1 ,\ldots ,\exists y_n)$ is a formula.

Clauses (2) and (3) allow the degenerate case that the list of universal quantifiers is empty $(n = 0)$. The resulting expressions $(\exists x$/) and $(\vee$/) are identified with the usual existential quantifier $(\exists x)$ and the usual disjunction $\vee$, respectively. Similar stipulations are made about clauses (4) and (5).

In a suitable vocabulary, each of the following is a formula:

- $(\forall x)(\forall y)(\exists z/\forall x) R(x, y, z, v)$,
- $(\forall x)(\forall y)(x = y \; (\vee /\forall x) \; Q(x, y))$,
- $(\exists x)(S(x) \; (\wedge /\exists x) \; T(x))$,
- $(\forall x)(\exists y)(\forall z/\exists y)(\exists v/\forall x) R(x, y, z, v)$.

By contrast, none of the following sequences of symbols is a formula:

- $(\exists y/\forall x) P(x, y)$,
- $(\exists x)(\exists y/\exists x) P(x, y)$,
- $(\forall x)(\forall y/\forall x) P(x, y)$,
- $(\forall x)(S(x) \; (\vee /\exists y) \; T(x))$.

If *φ* is an $\mathbf{IFL}$ formula, generated by the above clauses from some $\mathbf{FO}$ formula $\phi^*$, the *free variables* of *φ* are simply the free variables of $\phi^*$. $\mathbf{IFL}$ formulas without free variables are $\mathbf{IFL}$ *sentences*.[^note-18]

### 3.2. Semantics

Defining the semantics of a logic using GTS is a two-step process. The first step is to define the relevant *semantic games*. The second step is to define the notions of ‘true’ and ‘false’ in terms of the semantic games; this happens by reference to the notion of *winning strategy*. Semantic games may be defined by specifying recursively the alternative ways in which a game associated with a given formula *φ* can be begun.[^note-19]

For every vocabulary *τ*, $\mathbf{IFL}[\tau]$ formula *φ*, model $(\tau$ structure) $M$, and variable assignment $g$, a two-player zero-sum game $G(\phi , M, g)$ between player 1 and player 2 is associated.[^note-20] If $g$ is a variable assignment, $g[x/a]$ is the variable assignment which is otherwise like $g$ but maps the variable $x$ to the object $a$.

1. If $\phi = R(t_1 ,\ldots ,t_n)$ and $M, g \vDash R(t_1 ,\ldots ,t_n)$, player 2 wins (and player 1 loses); otherwise player 1 wins (and player 2 loses).
2. If $\phi = t_1 = t_2$ and $M, g \vDash t_1 = t_2$, player 2 wins (and player 1 loses); otherwise player 1 wins (and player 2 loses).
3. If $\phi = {\sim}R(t_1 ,\ldots ,t_n)$ and $M, g \not\vDash R(t_1 ,\ldots ,t_n)$, player 2 wins (and player 1 loses); otherwise player 1 wins (and player 2 loses).
4. If $\phi = {\sim}t_1 = t_2$ and $M, g \not\vDash t_1 = t_2$, player 2 wins (and player 1 loses); otherwise player 1 wins (and player 2 loses).
5. If $\phi = (\psi \; (\wedge /\exists y_1 ,\ldots ,\exists y_n) \; \chi)$, player 1 chooses $\theta \in \{\psi ,\chi \}$ and the rest of the game is as in $G(\theta , M, g)$.
6. If $\phi = (\psi \; (\vee /\forall y_1 ,\ldots ,\forall y_n) \; \chi)$, player 2 chooses $\theta \in \{\psi ,\chi \}$ and the rest of the game is as in $G(\theta , M, g)$.
7. If $\phi = (\forall x/\exists y_1 ,\ldots ,\exists y_n)\psi$, player 1 chooses an element $a$ from $\rM$, and the rest of the game is as in $G(\psi , M, g[x/a]$).
8. If $\phi = (\exists x/\forall y_1 ,\ldots ,\forall y_n)\psi$, player 2 chooses an element $a$ from $\rM$, and the rest of the game is as in $G(\psi , M, g[x/a]$).

Observe that the independence indications play no role in the game rules. Indeed, quantifier independence will be implemented on the level of strategies.

If a token of $(\vee /\forall y_1 ,\ldots ,\forall y_n)$ or $(\exists x/\forall y_1 ,\ldots ,\forall y_n)$ appears in the formula *φ* in the scope of the universal quantifiers $\forall y_1 ,\ldots ,\forall y_n,\forall z_1 ,\ldots ,\forall z_m$ (and only these universal quantifiers), a *strategy function* of player 2 for this token in game $G(\phi , M, g)$ is any function $f$ satisfying the following:

The arguments of $f$ are the elements $a_1 ,\ldots ,a_m$ that player 1 has chosen so as to interpret the quantifiers $\forall z_1 ,\ldots ,\forall z_m$. The value $f(a_1 ,\ldots ,a_m)$ is the left or the right disjunct when the token is a disjunction; and an element of the domain when the token is an existential quantifier.

The notion of the strategy function of player 1 for tokens of $(\wedge /\exists y_1 ,\ldots ,\exists y_n)$ and $(\forall x/\exists y_1 ,\ldots ,\exists y_n)$ can be defined dually. Strategy functions are construed as Skolem functions – the more general notion of strategy function operative in slash logic is not considered here (cf. the beginning of *Sect.* 3 and *Subsect.* 6.1). Quantifier independence will be implemented directly in terms of the *arguments* of the strategy functions.

A *strategy* of player 2 in game $G(\phi , M, g)$ is a set $F$ of her strategy functions, one function for each token of $(\vee /\forall y_1 ,\ldots ,\forall y_n)$ and $(\exists x/\forall y_1 ,\ldots ,\forall y_n)$ appearing in *φ*. Player 2 is said to *follow* the strategy $F$, if for each token of $(\vee /\forall y_1 ,\ldots ,\forall y_n)$ and $(\exists x/\forall y_1 ,\ldots ,\forall y_n)$ for which she must make a move when game $G(\phi , M, g)$ is played, she makes the move determined by the corresponding strategy function. A *winning strategy* for player 2 in $G(\phi , M, g)$ is a strategy $F$ such that against any sequence of moves by player 1, following strategy $F$ yields a win for player 2. The notions of strategy and winning strategy can be similarly defined for player 1.[^note-21]

The *satisfaction* and *dissatisfaction* of the $\mathbf{IFL}$ formula *φ* in the model $M$ under the assignment $g$ are then *defined* as follows:[^note-22]

- **(Satisfaction)** *φ* is satisfied in $M$ under $g$ iff there is a winning strategy for player 2 in game $G(\phi , M, g)$.
- **(Dissatisfaction)** *φ* is dissatisfied in $M$ under $g$ iff there is a winning strategy for player 1 in game $G(\phi , M, g)$.

As with $\mathbf{FO}$, variable assignments do not affect the (dis)satisfaction of sentences, *i.e.*, formulas containing no free variables. Indeed, we may define:[^note-23]

- **(Truth)** *φ* is true in $M$ iff there is a winning strategy for player 2 in game $G(\phi , M)$.
- **(Falsity)** *φ* is false in $M$ iff there is a winning strategy for player 1 in game $G(\phi , M)$.

The fact that *φ* is true in $M$ will be denoted by ‘$M \vDash \phi$.’ Writing $M \not\vDash \phi$ indicates, then, that *φ* is not true in $M$. This does *not* mean that *φ* would in the above-defined sense be false in $M$. As mentioned in the end of *Section* 2, there are semantic games in which neither player has a winning strategy.

The syntax of $\mathbf{IFL}$ can be generalized by removing the restriction according to which the negation sign may only appear as prefixed to an atomic formula.[^note-24]. In order to interpret negation in GTS, two *roles* are added as a new ingredient in the specification of the games: those of ‘verifier’ and ‘falsifier.’ Initially, player 1 has the role of ‘falsifier’ and player 2 that of ‘verifier.’ The roles may get switched, but only for one reason: when an occurrence of the negation symbol is encountered. All clauses defining semantic games must be rephrased in terms of roles instead of players. It is the player whose role is ‘verifier’ who makes a move for disjunctions and existential quantifiers, and similarly the player whose role is ‘falsifier’ who moves for conjunctions and universal quantifiers. When a formula ${\sim}\psi$ is encountered, the players change roles and the game continues with *ψ*. Finally, if the encountered atomic formula is true, ‘verifier’ wins and ‘falsifier’ loses, otherwise the payoffs are reversed. The negation ${\sim}$ is variably referred to as *strong negation*, *dual negation*, or *game-theoretical negation*.[^note-25] It works as one would expect: *φ* is false in $M$ iff its negation ${\sim}\phi$ is true therein (cf. Sandu 1993)[^sandu-1993].

### 3.3. Basic properties and notions

**Failure of bivalence.** There are sentences *φ* of $\mathbf{IFL}$ and models $M$ such that *φ* is neither true nor false in $M$. Consider evaluating the sentence $(\forall x)(\exists y/\forall x) x = y$ on a model whose domain has exactly two elements, $a$ and $b$. Player 1 has no winning strategy. If he chooses $a$ to interpret $\forall x$, he loses the play in which player 2 chooses $a$ to interpret $(\exists y/\forall x)$. Similarly, if player 1 chooses $b$, he loses the play in which player 2 likewise chooses $b$. Neither does player 2 have a winning strategy. Her strategy functions for $(\exists y/\forall x)$ are constants (zero-place functions). There are two such constants available: $a$ and $b$. Whichever one of these strategy functions player 2 assumes, there is a move by player 1 defeating it. If player 2 opts for $a$, player 1 wins the play in which he chooses $b$; and if player 2 applies $b$, player 1 wins the play in which he chooses $a$. Game $G(\phi , M)$ is *non-determined*: neither player has a winning strategy.[^note-26] The notion of non-determinacy may be extended to formulas as well:

- **(Non-determinacy)** *φ* is non-determined in $M$ under $g$ iff there is no winning strategy for player 1, nor for player 2, in game $G(\phi , M, g)$.

In $\mathbf{IFL}$, falsity does not ensue from non-truth. That is, bivalence fails in $\mathbf{IFL}$. However, it should be noted that it does not fail due to the postulation of a third truth-value or a truth-value gap (cf. Hintikka 1991: 20, 55)[^hintikka-1991][^hintikka-1991-2].[^note-27] Rather, the failure is a consequence of the basic assumptions of the entire semantic theory (GTS). Non-determinacy corresponds to a structural property: the fact that certain kinds of functions do not exist on the model considered.

Due to the failure of bivalence, the logical law of excluded middle fails for the dual negation ${\sim}$. Actually, *φ* is non-determined in $M$ iff $M \not\vDash(\phi \vee{\sim}\phi)$.

**Logical equivalence.** Sentences *ψ* and *χ* of $\mathbf{IFL}$ are *truth equivalent* if they are true in precisely the same models, and *falsity equivalent* if they are false in precisely the same models. Sentences *ψ* and *χ* are *logically equivalent* if they are both truth equivalent and falsity equivalent.[^note-28] Due to the failure of bivalence, in $\mathbf{IFL}$ truth equivalence does not guarantee logical equivalence.

**Truth, falsity, and independence indications.** The syntax of $\mathbf{IFL}$ allows formulas in which both universal and existential quantifiers appear slashed, *e.g.*,

$$ \phi : (\forall x)(\exists y/\forall x)(\forall z/\exists y) R(x, y, z). $$

On the other hand, quantifier independence is implemented at the level of strategies. Consequently independence indications following a universal quantifier are vacuous, when the satisfaction of a formula (truth of a sentence) is considered. Similarly, independence indications following an existential quantifier are vacuous when the dissatisfaction of a formula (falsity of a sentence) is at stake. The sentence *φ* is true in the model $M$ iff player 2 has a winning strategy $F=\{c\}$ in game $G(\phi , M)$. This, again, means that whichever elements $a$ and $b$ player 1 chooses to interpret $(\forall x)$ and $(\forall z/\exists y)$, respectively, the constant interpretation $c$ of $(\exists y/\forall x)$ given by the (zero-place) strategy function $c$ satisfies $R(a, c, b)$ in $M$. But this amounts to the same as requiring that whichever elements $a$ and $b$ player 1 chooses to interpret $(\forall x)$ and $(\forall z)$, respectively, the constant interpretation $c$ of $(\exists y/\forall x)$ satisfies $R(a, c, b)$ in $M$. Indeed, *φ* is truth equivalent to a sentence containing no slashed universal quantifiers:

*φ* is true in a model $M$ iff the sentence $(\forall x)(\exists y/\forall x)(\forall z) R(x, y, z)$ is true in $M$.

Similarly, *φ* is falsity equivalent to a sentence containing no slashed existential quantifiers: *φ* is false in a model $M$ iff the sentence $(\forall x)(\exists y)(\forall z/\exists y) R(x, y, z)$ is false therein.

### 3.4. Extended IF first-order logic

If *φ* is a sentence of $\mathbf{FO}$, *φ* is false in a model $M$ iff ${\sim}\phi$ is true in $M$ iff *φ* is not true in $M$. By contrast, in $\mathbf{IFL}$ falsity and non-truth do not coincide. An extension of $\mathbf{IFL}$ can be introduced, where it is possible to speak of the non-truth of sentences. To this end, let us introduce a new negation symbol, $\neg$, referred to as *weak negation*, *contradictory negation* or *classical negation*.[^note-29] The set of formulas of *extended IF first-order logic* (to be denoted $\mathbf{EIFL})$ is obtained from the set of formulas of $\mathbf{IFL}$ by closing it under the operations $\neg$, $\wedge$, and $\vee$:[^note-30]

- All formulas of $\mathbf{IFL}$ are formulas of $\mathbf{EIFL}$.
- If *φ* and *ψ* are formulas of $\mathbf{EIFL}$, then so are $\neg \phi , (\phi \wedge \psi)$ and $(\phi \vee \psi)$.

So if *φ* and *ψ* are $\mathbf{IFL}$ formulas, *e.g.* $\neg \phi$ and $(\neg \phi \vee \psi)$ are $\mathbf{EIFL}$ formulas; by contrast $(\forall x)\neg \phi$ is not. For the crucial restriction that $\neg$ may not occur in the scope of a quantifier, see Hintikka (1991: 49; 1996: 148). For counterexamples to this restriction see, however, Hintikka (1996: 148; 2002c) and especially Hintikka (2006b)[^hintikka-2006b] in which the so-called *fully extended IF first-order logic* (**FEIFL**) is considered. In **FEIFL**, any occurrences of $\neg$ are allowed which are subject to the following syntactic condition: if (Q$x/W)$ is a quantifier in the syntactic scope of an occurrence of $\neg$, then all quantifiers listed in $W$ are likewise in the syntactic scope of that occurrence of $\neg$.

The semantics of an $\mathbf{EIFL}$ formula formed by contradictory negation is simply this:

$$ M, g \vDash \neg \phi \text{ iff } M, g \not\vDash \phi. $$

From the viewpoint of GTS, the connective $\neg$ behaves in an unusual way. For all connectives of $\mathbf{IFL}$, there is a game rule (which can be seen as specifying the meaning of the connective). For contradictory negation there is no game rule, and its semantics is not explained in terms of plays of semantic games. A formula $\neg \phi$ serves to say, globally, something about an entire game $G(\phi , M, g)$. If *φ* is a sentence, to say that $\neg \phi$ is true in $M$ is to say that player 2 does *not* have a winning strategy in game $G(\phi , M)$. If, again, there is indeed a winning strategy for player 2 in $G(\phi , M)$, by stipulation $\neg \phi$ is false in $M$.[^note-31]

Not only is $\neg \phi$ not itself a formula of $\mathbf{IFL}$, but it cannot in general even be expressed in $\mathbf{IFL}$ (see *Subsect.* 4.2). The law of excluded middle holds for the contradictory negation: for all sentences *φ* and all models $M$, indeed $M \vDash(\phi \vee \neg \phi)$. In *Section* 5 it will be seen how Hintikka has proposed to make use of $\mathbf{EIFL}$ when discussing issues in the philosophy of mathematics.

## 4. Metalogical Properties of IF First-order Logic

The metalogical properties of $\mathbf{IFL}$ have been discussed in several publications, by Hintikka as well as Sandu.[^note-32] When presenting them, reference will be made to *existential second-order logic* $(\mathbf{ESO})$;[^note-33] further important notions are those of the *skolemization* and *Skolem normal form* of an $\mathbf{IFL}$ formula. For precise definitions of these notions, [the supplementary document](logic-if.supplement.md) can be consulted. In brief, $\mathbf{ESO}$ is obtained from $\mathbf{FO}$ by allowing existential quantification over relation and function symbols in a first-order formula. The skolemization $\mathrm{sk}[\phi]$ of an $\mathbf{IFL}$ formula *φ* is a *first-order* formula of a larger vocabulary. It explicates in terms of function symbols how existential quantifiers and disjunction symbols of *φ* depend on preceding universal quantifiers. For example, a skolemization of the $\mathbf{IFL}$ sentence $\phi = (\forall x)(\exists y)(\forall z)(\exists v/\forall x)R(x, y, z, v)$ of vocabulary $\{R\}$ is the $\mathbf{FO}$ sentence $\mathrm{sk}[\phi] = (\forall x)(\forall z)R(x, f(x), z, h(z))$ of vocabulary $\{R, f, h\}$. Its Skolem normal form, again, is the $\mathbf{ESO}$ sentence $\mathrm{SK}[\phi] = (\exists f)(\exists h)(\forall x)(\forall z)R(x, f(x), z, h(z))$. The first-order sentence $\mathrm{sk}[\phi]$ must not be confused with the second-order sentence $\mathrm{SK}[\phi]$.

### 4.1. First-order logic and existential second-order logic

**Game-theoretical vs. Tarskian semantics of FO.** The set of formulas of $\mathbf{FO}$ is a proper subset of the set of $\mathbf{IFL}$ formulas. The standard semantics of $\mathbf{FO}$ is not the one provided by GTS, but the Tarskian semantics specifying recursively the satisfaction relation $M, g \vDash \phi$. If the *Axiom of Choice* is assumed,[^note-34] the two semantics of $\mathbf{FO}$ coincide:

**Theorem (assuming AC).** (Hodges 1983: 94, Hintikka & Kulas 1985: 6–7)[^hintikka-1985][^hodges-1983] Let *τ* be any vocabulary, $M$ any *τ* structure, $g$ any variable assignment and *φ* any $\mathbf{FO}[\tau]$ formula. Then $M, g \vDash \phi$ holds in the standard sense iff there is a winning strategy for player 2 in game $G(\phi , M, g)$.[^note-35]

**Relation to ESO.** $\mathbf{IFL}$ and $\mathbf{ESO}$ are intertranslatable:[^note-36]

**Theorem** **(assuming AC)** $\mathbf{ESO}$ and $\mathbf{IFL}$ have the same expressive power.

That is, (1) for every $\mathbf{IFL}[\tau]$ formula *φ* there is an $\mathbf{ESO}[\tau]$ formula $\phi'$ such that for all *τ* structures $M$ and variable assignments $g$, we have: $M, g \vDash \phi$ iff $M, g \vDash \phi'$. Actually, $\mathrm{SK}[\phi]$ is a suitable $\mathbf{ESO}$ formula. And (2) for every $\mathbf{ESO}[\tau]$ formula *ψ* there is an $\mathbf{IFL}[\tau]$ formula $\psi'$ such that $M, g \vDash \psi$ iff $M, g \vDash \psi'$, for all *τ* structures $M$ and variable assignments $g$. This follows from the fact that $\mathbf{ESO}$ can be translated into $\mathbf{FPO}$ (Enderton 1970, Walkoe 1970)[^enderton-1970][^walkoe-1970], which again can be translated into $\mathbf{IFL}$.

Hintikka suggests that $\mathbf{IFL}$ is, substantially speaking, a *first-order* logic: the entities its quantified variables range over are *individuals*, and so are all entities with which the players of the semantic games operate. (See *Subsect.* 5.1 for a discussion of this idea.) A part of the interest of the intertranslatability theorem lies in the fact that if Hintikka’s controversial claim is accepted, this would mean that the expressive power of $\mathbf{ESO}$ can actually be achieved on the first-order level.

**IFL is more expressive than FO.** The following are examples of properties expressible in $\mathbf{ESO}$ – and therefore in $\mathbf{IFL}$ – but not in $\mathbf{FO}$: Dedekind-infinity of the domain, non-completeness of a linear order, ill-foundedness of a binary relation, disconnectedness of a graph, equicardinality of the extensions of two first-order formulas $\phi(x)$ and $\psi(x)$, infinity of the extension of a first-order formula $\phi(x)$, and the topological notion of open set (see, *e.g.*, Hintikka 1996, Väänänen 2007)[^hintikka-1996][^hintikka-1996-2][^väänänen-2007].

As an example, the Dedekind-infinity of the domain may be considered. A set $S$ is Dedekind-infinite precisely when there exists an injective function from $S$ to its proper subset. Let $\phi_{inf}$ be the following sentence of $\mathbf{IFL}$:[^note-37]

$$ (\exists t)(\forall x)(\exists z)(\forall y)(\exists v/\forall x)((x = y \leftrightarrow z = v) \wedge z \ne t). $$

The Skolem normal form of $\phi_{inf}$ is

$$ (\exists f)(\exists g)(\exists t)(\forall x)(\forall y)((x = y \leftrightarrow f(x) = g(y)) \wedge f(x) \ne t). $$

Relative to a model $M$, this $\mathbf{ESO}$ sentence asserts the existence of functions $f$ and $g$ and an element $t$ such that $f = g$ (implication from left to right), this function is injective (implication from right to left), and its domain is the whole domain of $M$ but the element $t$ does not appear in its range. Consequently the range is a proper subset of the domain of $M$. In other words, the sentence $\phi_{inf}$ is true in a model $M$ iff the domain of $M$ is infinite.

Be it still noted that when attention is restricted to *finite* models, Ronald Fagin’s famous theorem (1974) connects $\mathbf{ESO}$ and the complexity class $\mathbf{NP}$: a computational problem is solvable by an algorithm running in non-deterministic polynomial time iff it is definable in $\mathbf{ESO}$ relative to the class of all finite structures. The following are $\mathbf{NP}$-complete properties and hence expressible in $\mathbf{IFL}$, over the class of all finite models: evenness of the domain, oddness of the domain, 3-colorability of a graph, and the existence of a Hamiltonian path on a graph.[^note-38]

**Properties in common with FO.** IF first-order logic shares many metalogical properties with first-order logic.[^note-39]

**Compactness.** A set of $\mathbf{IFL}$ sentences has a model iff all its finite subsets have a model.

**Löwenheim-Skolem property.** Suppose *φ* is an $\mathbf{IFL}$ sentence that has an infinite model, or arbitrarily large finite models. Then *φ* has models of all infinite cardinalities.

The separation theorem holds in $\mathbf{IFL}$ in a strengthened form; the ‘separation sentence’ *θ* is in particular a sentence of $\mathbf{FO}$.

**Separation theorem.** Suppose *φ* is an $\mathbf{IFL}$ sentence of vocabulary *τ*, and *ψ* an $\mathbf{IFL}$ sentence of vocabulary $\tau'$. Suppose further that *φ* and *ψ* have no models in common. Then there is a *first-order* sentence *θ* of vocabulary $\tau \cap \tau'$ such that every model of *φ* is a model of *θ*, but *θ* and *ψ* have no models in common.

It is well known that for $\mathbf{FO}$ there is a sound and complete proof procedure. Because a first-order sentence *φ* is inconsistent (non-satisfiable) iff its negation ${\sim}\phi$ is valid (true in all models), trivially $\mathbf{FO}$ also has a sound and complete disproof procedure.[^note-40] The latter property extends to $\mathbf{IFL}$ (while the former does not, see *Subsect.* 4.3):

**Existence of a complete disproof procedure.** (Hintikka 1996: 68–70, 82)[^hintikka-1996][^hintikka-1996-2] The set of inconsistent $\mathbf{IFL}$ sentences is recursively enumerable.

### 4.2. Intricacies of negation

In *Subsection* 3.4, the contradictory negation $\neg$ was distinguished from the strong negation ${\sim}$. In $\mathbf{FO}$ the two coincide: for any first-order sentence *φ*, we have $M \vDash{\sim}\phi$ iff $M \vDash \neg \phi$.

**Strong negation fails as a semantic operation.** Let us write $[\phi]$ for the set of models of sentence *φ*. In the special case of $\mathbf{FO}$, the strong negation ${\sim}$ clearly defines a semantic operation: whenever *χ* and *θ* are sentences such that $[\chi] = [\theta]$, we have $[{\sim}\chi] = [{\sim}\theta]$. Burgess (2003)[^burgess-2003] observed that in the context of IF logic this property is lost in a very strong sense. In fact there are IF sentences *χ* and *θ* such that while $[\chi] = [\theta]$, the sets $[{\sim}\chi]$ and $[{\sim}\theta]$ are not only distinct but even disjoint.

**Inexpressibility of contradictory negation.** In $\mathbf{IFL}$ the strong negation ${\sim}$ and the contradictory negation $\neg$ do *not* coincide: we may have $M \vDash \neg \phi$ without having $M \vDash{\sim}\phi$. This fact by itself still leaves open the possibility that the contradictory negation of every sentence *φ* of $\mathbf{IFL}$ could be defined in $\mathbf{IFL}$, *i.e.*, that there was a sentence $neg(\phi)$ of $\mathbf{IFL}$ such that $M \vDash$ $neg(\phi)$ iff $M \not\vDash \phi$, for all models $M$. All we know by the failure of the law of excluded middle is that not in all cases can $neg(\phi)$ be chosen to be ${\sim}\phi$. However, as a matter of fact contradictory negation is inexpressible in $\mathbf{IFL}$. There are sentences *φ* of $\mathbf{IFL}$ such that $\neg \phi$ (which is a sentence of $\mathbf{EIFL})$ is not truth equivalent to any sentence of $\mathbf{IFL}$. This follows from the well-known fact that $\mathbf{ESO}$ is not closed under negation and $\mathbf{IFL}$ has the same expressive power as $\mathbf{ESO}$.[^note-41]

**Strong inexpressibility of contradictory negation.** As a corollary to the separation theorem, the result holds in a much stronger form. If *φ* and *ψ* are sentences of $\mathbf{IFL}$ such that $M \vDash \phi$ iff $M \not\vDash \psi$, then each of *φ* and *ψ* is truth equivalent to a sentence of $\mathbf{FO}$. Hence the contradictory negation $\neg \phi$ is only expressible in $\mathbf{IFL}$ for those $\mathbf{IFL}$ sentences *φ* that are truth equivalent to an $\mathbf{FO}$ sentence.[^note-42]

**Determined fragment.** Let us say that an $\mathbf{IFL}$ sentence *φ* is *determined* if it satisfies: $M \vDash(\phi \vee{\sim}\phi)$, for all models $M$. The *determined fragment* of $\mathbf{IFL}$ is the set of determined $\mathbf{IFL}$ sentences. In the determined fragment contradictory negation *is* syntactically expressible by the strong negation. By the strong inexpressibility of contradictory negation, the determined fragment of $\mathbf{IFL}$ has the same expressive power as $\mathbf{FO}$. Membership in the determined fragment is a sufficient but not necessary condition for an $\mathbf{IFL}$ sentence to have its contradictory negation expressible in $\mathbf{IFL}$. The sentence $(\forall y)(\exists x/\forall y) x = y$ is not determined;[^note-43] yet its contradictory negation $(\forall x)(\exists y) x \ne y$ is expressible in $\mathbf{IFL}$.

**Contradictory negation and GTS.** The truth-conditions that GTS yields are of the form ‘there are strategy functions $f_1 ,\ldots ,f_n$ such that —,’ *i.e.*, it gives rise to truth-conditions expressible in $\mathbf{ESO}$. By the strong inexpressibility of contradictory negation, there is no single $\mathbf{IFL}$ sentence, not translatable into $\mathbf{FO}$, whose contradictory negation has a truth-condition of that form. This fact makes it understandable why contradictory negation should not be expected to admit of a game-theoretical interpretation along the same lines in which the other logical operators are interpreted. Different ways of assigning a game-theoretical interpretation to contradictory negation can, however, be developed. To this end, in the context of *fully extended IF first-order logic* (**FEIFL**, cf. Subsect. 3.4), Hintikka has proposed to use semantic games with *subgames*. (See Hintikka 2002c, 2006b; for subgames, see Carlson & Hintikka 1979, Hintikka & Kulas 1983.)[^carlson-1979][^carlson-1979-2][^hintikka-1979][^hintikka-2002c][^hintikka-2006b][^hintikka-1983] This approach leads to mixing the play level with the strategy level: choices of individuals made in a subgame may depend on strategy functions chosen in earlier subgames. In Tulenheimo (2014)[^tulenheimo-2014], a game-theoretical semantics is formulated for the fragment of **FEIFL** that consists of formulas in prenex form. Plays of the correlated games do not involve choosing any second-order objects, such as strategy functions. Contradictory negation $(\neg)$ is interpreted by introducing an additional component in game positions: a *mode*. At the play level, the negation $\neg$ triggers not only a role switch (like the dual negation ${\sim})$, but it also involves changing the mode from positive to negative or vice versa. The semantic effect of modes becomes visible at the strategy level: modes regulate the way in which the truth condition of a sentence involves existentially or universally quantifying over strategy functions. Like independence indications, also occurrences of $\neg$ are, then, interpreted in terms of conditions that act on the strategy level. For related research, see Figueira *et al.* (2011, 2014).

**Contradictory negation and finite models.** Certain major open questions in logic and theoretical computer science can be formulated in terms of $\mathbf{IFL}$. It is an open question in complexity theory whether $\mathbf{NP} = \mathbf{coNP}$, that is, whether the class of $\mathbf{NP}$-solvable problems is the same as the class of problems whose complement is solvable in $\mathbf{NP}$. By Fagin’s theorem (1974), this open problem can be equivalently formulated as follows: Is $\mathbf{IFL}$ closed under negation *over finite models*? That is, is there for every IF sentence *φ* another IF sentence $neg(\phi)$ such that for any finite model $M$, $neg(\phi)$ is true in $M$ iff *φ* is not true in $M$? Proving that the answer is negative would settle the notorious $\mathbf{P} = \mathbf{NP}$ problem, i.e., establish that there are computational problems for which one can efficiently *verify* whether a proposed solution is correct although one cannot efficiently *find* a solution.[^note-44]

### 4.3 Failure of axiomatizability

As is well known, $\mathbf{FO}$ admits of a sound and complete proof procedure: there is a mechanical way of generating precisely those first-order sentences that are valid (true in all models). This fact can also be expressed by saying that $\mathbf{FO}$ is axiomatizable, or that the set of valid sentences of $\mathbf{FO}$ is recursively enumerable.[^note-45] Due to its greater expressive power, axiomatizability *fails* for $\mathbf{IFL}$. In other words, $\mathbf{IFL}$ is semantically incomplete.[^note-46]

One way to show this is as follows. Suppose for the sake of contradiction that the set of valid $\mathbf{IFL}$ sentences is recursively enumerable. Recall that the sentence $\phi_{inf}$ discussed in *Subsection* 4.1 is true in all and only infinite models. Note, then, that an $\mathbf{FO}$ sentence *χ* is true in all *finite* models iff the $\mathbf{IFL}$ sentence $(\phi_{inf} \vee \chi)$ is valid. Given a valid $\mathbf{IFL}$ sentence, it can be effectively checked whether the sentence is syntactically of the form $(\phi_{inf} \vee \chi)$, where *χ* is a first-order sentence. Hence the recursive enumeration of all valid $\mathbf{IFL}$ sentences yields a recursive enumeration of first-order sentences *χ* true in all finite models. But this contradicts Trakhtenbrot’s theorem, according to which the set of $\mathbf{FO}$ sentences true in all finite models is *not* recursively enumerable.[^note-47]

What is the relevance of the failure of axiomatizability of $\mathbf{IFL}$? Discussing finite partially ordered quantifiers, Quine (1970: 89–91)[^quine-1970] suggests that we should refuse to give the status of logic to any generalization of $\mathbf{FO}$ which does not have a sound and complete proof procedure *both* for validity *and* for inconsistency. For Quine, any such generalization belongs to mathematics rather than logic. Since $\mathbf{FPO}$ is not axiomatizable, it falls outside the realm of logic, thus delineated.[^note-48]

Hintikka finds this type of allegation unfounded. First, $\mathbf{IFL}$ shares many of the important metalogical results with $\mathbf{FO}$ (cf. *Subsect.* 4.1). Second, just like $\mathbf{IFL}$, also $\mathbf{FO}$ can be translated into second-order logic. The only difference is that in the former case a larger variety of quantifier (in)dependencies must be encoded by Skolem functions than in the latter. Why would the former translation render $\mathbf{IFL}$ a part of mathematics while the latter would allow $\mathbf{FO}$ to remain a logic (Hintikka 1991: 26–27)[^hintikka-1991][^hintikka-1991-2]? Third, one must make a distinction between what is needed to understand an $\mathbf{IFL}$ sentence, and what is needed to mechanically deal with the validities (logical truths) of $\mathbf{IFL}$. Due to its non-axiomatizability, there are no mechanical rules for generating the set of all validities of $\mathbf{IFL}$. However, to understand a sentence is to know what things are like when it is *true*, not to know what things are like when it is *logically true* (Hintikka 1995: 13–14)[^hintikka-1995]. Fourth, because of non-axiomatizability, the valid inference patterns in $\mathbf{IFL}$ cannot be exhausted by any recursive enumeration. Insofar as important mathematical problems can be reduced to questions about the validity of $\mathbf{IFL}$ formulas (*Subsect.* 5.3), progress in mathematics can be seen to consist (not of the discovery of stronger set-theoretical axioms but) of ever more powerful rules for establishing validity in $\mathbf{IFL}$ (Hintikka 1996: 100; 2000: 135–136)[^hintikka-1996][^hintikka-1996-2].

### 4.4 Compositionality and the failure of Tarski-type semantics

The principle of compositionality (a.k.a. Frege principle) states that semantic attributes of a complex expression $E$ are determined by the semantic attributes of its constituent expressions and the structure of $E$. In particular, the semantic attribute of interest (*e.g.*, truth) may be determined in terms of one or more auxiliary semantic attributes (*e.g.*, satisfaction).[^note-49] Hintikka has argued that compositionality amounts to *semantic context-independence*: semantic attributes of a complex expression depend *only* on the semantic attributes of its constituent expressions, plus its structure – they do *not* depend on the sentential context in which the expression is embedded. Semantic context-independence makes it possible to carry out semantic analysis from *inside out* – from simpler expressions to more complex ones.[^note-50] This is what is needed for recursive definitions of semantic attributes – such as Tarski-type definitions of truth and satisfiability – to be possible.[^note-51] By contrast, the GTS analysis of sentences is an *outside in* process: a semantic game starts with an entire sentence, and stepwise analyzes the sentence into simpler and simpler components, eventually reaching an atomic formula (together with an appropriate variable assignment). Therefore GTS allows accounting for semantic context-dependencies that violate the principle of compositionality.[^note-52]

In $\mathbf{IFL}$ an existential quantifier may depend only on *some* of the universal quantifiers in whose scope it lies. Accordingly, its interpretation depends on its relation to quantifiers outside its own scope. Such an existential quantifier is context-dependent.[^note-53] On the face of it, then, $\mathbf{IFL}$ cannot but violate the principle of compositionality and does not admit of a Tarski-type truth-definition.

Hodges (1997a,b) showed, however, that $\mathbf{IFL}$ can be given a compositional semantics.[^note-54] The semantics is given by recursively defining the satisfaction relation ‘$M \vDash_X \phi$’ (read: *φ* is satisfied in $M$ by $X)$, where $X$ is a *set* of variable assignments. While the Tarskian semantics for $\mathbf{FO}$ is in terms of single variable assignments, Hodges’s semantics employs sets of variable assignments. The game-theoretical semantics of $\mathbf{IFL}$ is captured by this compositional semantics: for every formula *φ* of $\mathbf{IFL}$, player 2 has a winning strategy in $G(\phi , M, g)$ iff the condition $M \vDash_{\{g\}} \phi$ holds. Due to Hodges’s semantic clauses for existential quantifiers and disjunctions involving independence indications, the evaluation of *φ* relative to the singleton set $\{g\}$ generally leads to evaluating syntactic components of *φ* relative to sets of (possibly infinitely) many variable assignments. Hintikka remarks (2006a: 65) that if one is sufficiently ruthless, one can always save compositionality by building the laws of semantic interaction of different expressions into the respective meanings of those expressions.[^note-55]

It is methodologically worth pointing out that compositionality is not *needed* for defining $\mathbf{IFL}$. The very existence of $\mathbf{IFL}$ proves that rejecting compositionality is no obstacle for the formulation of a powerful logic (Hintikka 1995)[^hintikka-1995]. It should also be noted that what makes Hodges’s result work is its type-theoretical ascent. Let us say that a *Tarski-type* compositional semantics is a compositional semantics which interprets each formula $\phi(x_1 ,\ldots ,x_n)$ of $n$ free variables in terms of an $n$-tuple of elements of the domain. Hence the standard semantics of $\mathbf{FO}$ is Tarski-type, but Hodges’s semantics employing the satisfaction relation ‘$M \vDash_X \phi$’ is not, because the latter evaluates a formula $\phi(x_1 ,\ldots ,x_n)$ of $n$ free variables relative to an entire *set* of $n$-tuples of elements. Cameron & Hodges (2001) proved that actually there is $no$ Tarski-type compositional semantics for $\mathbf{IFL}$.

The notion of compositionality can be refined by imposing constraints on the auxiliary semantic attributes. Sandu and Hintikka (2001: 60)[^hintikka-2001] suggested, by analogy with $\mathbf{FO}$, that ‘satisfaction by a single variable assignment’ would be a natural auxiliary attribute in connection with $\mathbf{IFL}$. By the result of Cameron and Hodges, no semantics for $\mathbf{IFL}$ exists that would be compositional in this restricted sense.

### 4.5 Defining truth

The definability of truth can only be discussed in connection with languages capable of speaking of themselves. Let us consider an arithmetical vocabulary *τ* and restrict attention to the standard model $N$ of Peano’s axioms. Each sentence *φ* of vocabulary *τ* can then be represented by a natural number $\ulcorner \phi \urcorner$, its Gödel number. It is assumed that *τ* contains a numeral $\boldsymbol{{}^\ulcorner \phi {}^\urcorner}$ for each number $\ulcorner \phi \urcorner$. If $L$ and $L'$ are abstract logics of vocabulary *τ*, such as $\mathbf{FO}$ or $\mathbf{IFL}$, and $\TRUE(x)$ is a formula of $L'$ such that every sentence *φ* of $L$ satisfies:

$$ N \vDash \phi \text{ iff } N \vDash \TRUE(\boldsymbol{{}^\ulcorner \phi {}^\urcorner}), $$

then $\TRUE(x)$ is said to be a *truth-predicate* (*explicit truth-definition*) of logic $L$ in logic $L'$ for the model $N$. By Alfred Tarski’s famous theorem of the *undefinability of truth* (Tarski 1933)[^tarski-1933], there is no truth-predicate for $\mathbf{FO}$ in $\mathbf{FO}$ itself for the model $N$. More generally, Tarski showed that under certain assumptions, a truth-definition for a logic $L$ can only be given in a metalanguage which is essentially stronger than $L$. One of the assumptions is that the negation used behaves like contradictory negation. On the other hand, Tarski also pointed out that an implicit truth-definition for $\mathbf{FO}$ in $\mathbf{FO}$ itself *is* possible. Let *τ* be an arithmetical vocabulary, and let us stay with the standard model $N$ of Peano’s axioms. Let ‘$\TRUE$’ be a unary predicate not appearing in *τ*. An $\mathbf{FO}$ formula $\psi(x)$ of vocabulary $\tau \cup \{\TRUE\}$ is an *implicit truth-definition* for $\mathbf{FO}[\tau]$ in $\mathbf{FO}[\tau \cup \{\TRUE\}]$ for $N$, if for every $\mathbf{FO}[\tau]$ sentence *φ*, the following holds:

$N \vDash \phi$ iff there is an interpretation $\TRUE^N$ of the unary predicate $\TRUE$ such that $(N, \TRUE^N ) \vDash \psi(\boldsymbol{{}^\ulcorner \phi {}^\urcorner})$.[^note-56]

Intuitively, $\TRUE^N$ is the set of those natural numbers that are Gödel numbers of true arithmetic sentences of vocabulary *τ*; and $\psi(x)$ says that $x$ is a Gödel number in the extension of the predicate $\TRUE$. The formula $\psi(x)$ is a conjunction including clauses that mimic, on the object-language level, the metalogical recursive clauses of the Tarski-type truth-definition for $\mathbf{FO}$. *E.g.*, one of the conjuncts is

$$\begin{align*} (\forall y)(\forall z)(y = \boldsymbol{{}^\ulcorner \chi {}^\urcorner} &\wedge z = \boldsymbol{{}^\ulcorner \theta {}^\urcorner} \wedge x = \boldsymbol{{}^\ulcorner (\chi \wedge \theta) {}^\urcorner} \rightarrow \\ &[\TRUE(x) \leftrightarrow (\TRUE(y) \wedge \TRUE(z))]). \end{align*}$$

The implicit nature of the truth-definition is seen from the fact that the predicate $\TRUE$ appears on both sides of the equivalence sign in these clauses.[^note-57] The above implicit truth-definition of $\mathbf{FO}$ for $N$ is of the form ‘there is a set $S$ interpreting the predicate $\TRUE$ such that $\psi(x)$.’ Thus the implicit truth-definition of $\mathbf{FO}$ in $\mathbf{FO}$ gives rise to the explicit truth-definition $\exists \TRUE\, \psi(x)$ of $\mathbf{FO}[\tau]$ in $\mathbf{ESO}[\tau]$ for $N$. Since $\mathbf{ESO}$ and $\mathbf{IFL}$ have the same expressive power, a truth-predicate of $\mathbf{FO}$ for $N$ can be formulated in $\mathbf{IFL}$.

The same reasoning can be applied to $\mathbf{ESO}$ itself, and thereby to $\mathbf{IFL}$ (Hintikka 1991, 1996; Hyttinen & Sandu 2000; Sandu 1996, 1998)[^hintikka-1991][^hintikka-1996][^hintikka-1991-2][^hintikka-1996-2][^hyttinen-2000][^sandu-1996][^sandu-1998]. Namely, an $\mathbf{ESO}$ formula $\chi(x)$ of vocabulary $\tau \cup \{\TRUE\}$ can be formulated which is an *implicit* truth-definition of $\mathbf{ESO}[\tau]$ for $N$. Therefore the $\mathbf{ESO}[\tau]$ formula $\exists \TRUE\, \chi(x)$ is an *explicit* truth-definition of $\mathbf{ESO}[\tau]$ for $N$. Here the truth-predicate is formulated in the very same language whose notion of truth is being defined: $\mathbf{ESO}$. Hence $\mathbf{ESO}$, and thereby $\mathbf{IFL}$, is capable of explicitly defining its own truth-predicate relative to $N$.[^note-58] This result does not contradict Tarski’s undefinability result, because here non-determined sentences are possible; the negation used is not contradictory negation.[^note-59]

Tarski (1983)[^tarski-1983] adopted a view according to which truth cannot be defined for natural languages. It has been argued in Hintikka & Sandu (1999) that this was due to Tarski’s belief that compositionality fails in natural languages.[^note-60] $\mathbf{IFL}$ does not have a Tarski-type compositional semantics, but it admits of formulating a self-applied truth-predicate. The proposed reason why Tarski believed it not to be possible to discuss the notion of truth in natural languages themselves cannot, then, be entertained from the viewpoint of $\mathbf{IFL}$. For, the case of $\mathbf{IFL}$ shows that the failure of Tarski-type compositionality for a language does not entail the impossibility for the language to define its own truth-predicate.[^note-61]

### 4.6 Properties of extended IF first-order logic

**Expressive power.** Since $\mathbf{IFL}$ is not closed under contradictory negation, $\mathbf{EIFL}$ is strictly more expressive than $\mathbf{IFL}$ (cf. *Subsect.* 4.2).[^note-62] The following properties are expressible in $\mathbf{EIFL}$ but not in $\mathbf{IFL}$ (Hintikka 1996: 188–190)[^hintikka-1996][^hintikka-1996-2]: finiteness of the domain, well-foundedness of a binary relation, connectedness of a graph, principle of mathematical induction, Bolzano-Weierstrass theorem, and the topological notion of continuity.

**Metalogical properties.** The nice metatheorems that $\mathbf{IFL}$ shares with $\mathbf{FO}$ are lost: Compactness, Löwenheim-Skolem property, separation theorem, and the existence of a complete disproof procedure all fail for $\mathbf{EIFL}$ (Hintikka 1991: 49, 1996: 189)[^hintikka-1991][^hintikka-1996][^hintikka-1991-2][^hintikka-1996-2]. No self-applied truth-predictate is possible for $\mathbf{EIFL}$. The definition of such a truth-predicate would have to contain the clause

$$\begin{align*} (\forall y)(y = \boldsymbol{{}^\ulcorner \theta {}^\urcorner} &\wedge x = \boldsymbol{{}^\ulcorner \neg \theta {}^\urcorner} \rightarrow \\ &[\TRUE(x) \leftrightarrow \neg \TRUE(y)]). \end{align*}$$

But this clause is not a well-formed formula of $\mathbf{EIFL}$, since $\neg$ appears in the scope of the universal quantifier $(\forall y)$ (cf. Hintikka 1996: 151)[^hintikka-1996][^hintikka-1996-2].

The validity and satisfiability problems of the full second-order can be effectively reduced to the corresponding problems concerning $\mathbf{EIFL}$. Namely, why cannot a second-order sentence simply be thought of as a two-sorted first-order sentence? Because in order to capture the standard interpretation of second-order logic,[^note-63] it must be said that for every extensionally possible set of $n$-tuples of elements of sort 1 there exists a member of sort 2 having those and only those elements as members, for all arities $n$ such that the second-order sentence contains a quantifier $(\exists R)$ where $R$ is $n$-ary.[^note-64] Now, such additional conditions can be expressed by a finite conjunction $X$ of $\mathbf{USO}$ sentences, where $\mathbf{USO}$ (*universal second-order logic*) is obtained from $\mathbf{FO}$ by allowing universal quantification over relation and function symbols in a first-order formula. Each of these $\mathbf{USO}$ sentences can be expressed as the contradictory negation of an $\mathbf{ESO}$ sentence and therefore as the contradictory negation of an $\mathbf{IFL}$ sentence. Consequently, there is an $\mathbf{IFL}$ sentence $Y$ such that $X$ itself is logically equivalent to $\neg Y$. And here $\neg Y$ is a sentence of $\mathbf{EIFL}$. Therefore, if *φ* is a second-order sentence and $\phi^*$ its reconstruction in two-sorted first-order logic, we have: *φ* is satisfiable iff $(X \wedge \phi^*)$ is satisfiable iff $(\neg Y \wedge \phi^*)$ is satisfiable. And: *φ* is valid iff $\phi^*$ is a logical consequence of $X$ iff $(\neg X \vee \phi^*)$ is valid iff $(Y \vee \phi^*)$ is valid. Here, both $(\neg Y \wedge \phi^*)$ and $(Y \vee \phi^*)$ are sentences of $\mathbf{EIFL}$, the latter even a sentence of $\mathbf{IFL}$. It follows that the satisfiability (validity) of any second-order sentence can be expressed as the satisfiability (respectively, validity) of a sentence of $\mathbf{EIFL}$.[^note-65]

**Algebraic structure.** The two negations available in $\mathbf{EIFL}, \neg$ and ${\sim}$, agree on true sentences, as well as on false ones: if *φ* is true (false) in $M$, then both ${\sim}\phi$ and $\neg \phi$ are false (true) in $M$. By contrast, if *φ* is non-determined in $M$, then ${\sim}\phi$ is non-determined as well, but $\neg \phi$ is true. The combination $\neg{\sim}$ of the two negations applied to a sentence *φ* asserts that *φ* is not false.[^note-66]

The propositional part of $\mathbf{EIFL}$ involves the four operators $\neg , {\sim}, \wedge$, and $\vee$. Hintikka (2004b)[^hintikka-2004b] raises the question of the algebraic structure induced by these operators, when any two truth equivalent sentences are identified. The operators $\neg , \wedge$, and $\vee$ give rise to a Boolean algebra – but what does the strong negation ${\sim}$ add to this structure?

Restricting attention to truth equivalence, ${\sim}$ is definable from the operators $\neg$ and $\neg{\sim}$. For, ${\sim}\phi$ is true in $M$ iff $\neg(\neg{\sim}\phi)$ is true in $M$. Instead of ${\sim}$, the operator $\neg{\sim}$ may then be considered. Hintikka points out that the propositional part of $\mathbf{EIFL}$ (formulated in terms of the operators $\vee , \wedge , \neg$ and $\neg{\sim})$ is a Boolean algebra with an operator in the sense of Jónsson & Tarski (1951). The additional operator $\neg{\sim}$ is a closure operator.

Jónsson and Tarski (1951, Thm. 3.14) showed that any closure algebra is isomorphic to an algebraic system formed by a set equipped with a reflexive and transitive relation.[^note-67] As a matter of fact, the relevant algebraic structure is precisely that of the propositional modal logic $\mathbf{S4}$. Hence the propositional part of $\mathbf{EIFL}$ has the same algebraic structure as $\mathbf{S4}$. By a well-known result due to Gödel (1933)[^gödel-1933] and McKinsey & Tarski (1948), intuitionistic propositional logic can be interpreted in $\mathbf{S4}$, via a translation $t$ such that *φ* is intuitionistically provable iff $t(\phi)$ is a valid $\mathbf{S4}$ formula. Thus, intuitionistic propositional logic is interpretable in $\mathbf{EIFL}$.[^note-68]

## 5. Philosophical Consequences

Hintikka (2006a: 73–77)[^hintikka-2006a] takes the following to be among consequences of the novel insights made possible by (extended) IF first-order logic: reconstruction of normal mathematical reasoning on the first-order level, a novel perspective on the notion of truth in axiomatic set theory, insights into the nature of negation, and the formulation of a self-applied truth-predicate. A related topic of general interest is the phenomenon of informational independence in natural languages. The ideas related to negation and definability of truth have been discussed in *Subsections* 4.2 and 4.5, respectively. Let us consider here the remaining issues.

### 5.1 Place in type hierarchy

Hintikka maintains that the only reasonable way of making a distinction between first-order logic and higher-order logic is by reference to the entities that one’s quantified variables range over. A first-order logic is, then, a logic in which all quantifiers range over individuals, in contrast to higher-order entities (*e.g.*, subsets of the domain). On this basis Hintikka holds that substantially speaking, $\mathbf{IFL}$ and even $\mathbf{EIFL}$ are *first-order* logics.[^note-69] Solomon Feferman (2006: 457–461)[^feferman-2006] criticizes the criterion that Hintikka employs for judging the first-order status of a logic. Feferman makes use of generalized quantifiers in his argument.[^note-70] The formulas

$$ Q[z_1] \ldots [z_k] (\phi_1 ,\ldots ,\phi_k) $$

involving generalized quantifiers are *syntactically first-order*, insofar as the quantified variables $z_{i1},\ldots ,z_{in_i} = [z_i]$ are first-order $(1 \le i \le k)$. The semantics of a generalized quantifier $Q$ is formulated by associating with each domain M a $k$-ary relation $Q_M$ on M, with $Q_M \subseteq$ M$^{n_1} \times \ldots \times$ M$^{n_k}$. *E.g.*, for any infinite cardinal *κ*, there is a generalized quantifier $Q_{\ge \kappa}$ such that $Q_{\ge \kappa}z P(z)$ is true in a model $M$ iff there are at least *κ* elements that satisfy the predicate $P$. Hence generalized quantifiers can be *semantically higher-order*. (The notion of cardinality is a higher-order notion.) The fact that the variables in a formula range over individuals only, does not offer a reliable criterion for the logic’s first-order status.

Hintikka’s criterion could be reformulated by saying that a logic is of first order, if any *play* of a semantic game associated with a formula of this logic only involves (in addition to choices interpreting conjunctions and disjunctions) choices of individuals, as opposed to choices of higher-order entities. By this criterion $\mathbf{IFL}$ (and even $\mathbf{EIFL})$ are first-order logics, but the logic of generalized quantifiers such as $Q_{\ge \kappa}$ is not.[^note-71] Feferman (2006: 461)[^feferman-2006] anticipates the possibility of such a reply, but finds it unconvincing.

By a result of Hintikka (1955)[^hintikka-1955], the problem of deciding whether a sentence of second-order logic is valid can be effectively reduced to the validity problem of $\mathbf{IFL}$.[^note-72] Väänänen (2001)[^väänänen-2001] has shown that the set of valid sentences of $\mathbf{IFL}$ has the same very high complexity as the set of validities of the full second-order logic.[^note-73] Väänänen (2001)[^väänänen-2001] and Feferman (2006)[^feferman-2006] conclude that speaking of validity in $\mathbf{IFL}$ leads to a strong commitment to full second-order logic. Hintikka (2006a: 476–477)[^hintikka-2006a] looks at these results from the opposite direction: for him they mean that indeed one can speak of validity in full second-order logic in terms of validity in $\mathbf{IFL}$. What is more, Hintikka (1997)[^hintikka-1997][^hintikka-1997-2][^hintikka-1997-3] affirms that even $\mathbf{EIFL}$ is a first-order logic. If so, any mathematical theory that can be expressed by the truth of an $\mathbf{EIFL}$ sentence is likewise free from problems of set existence.

Hintikka’s position leads to a puzzle. If *φ* is a sentence of $\mathbf{IFL}$ not truth equivalent to any $\mathbf{FO}$ sentence, the truth-condition of the sentence $\neg \phi$ of $\mathbf{EIFL}$ cannot be formulated without recourse to the set of all strategies of player 2: $\neg \phi$ is true in model $M$ iff for *all* strategies of player 2 in game $G(\phi , M)$, there is a sequence of moves by player 1 such that player 1 wins the resulting play. The set of all strategies of player 2 is undeniably a higher-order entity. How can commitment to entities other than individuals be said to have been avoided here? Can the meaning of the sentence $\neg \phi$ be well understood without presupposing the genuinely second-order idea of all strategies of a given player?[^note-74] Rather than being nominalistic, Hintikka’s position appears to be a variant of *universalia in rebus*. While rules of semantic games pertain to actions performed on first-order objects, combinatorial properties of sets of plays can only be formulated in second-order terms. As soon as game rules are defined for a language fragment, also the corresponding combinatorial properties are fully determined, among them the properties labeled as truth and falsity.

### 5.2 Philosophy of set theory

According to Hintikka, our pretheoretical idea of the truth of a quantified sentence *φ* (in negation normal form) is that there exist ‘witness individuals’ for the existential quantifiers, usually depending on values corresponding to the preceding universal quantifiers.[^note-75] It is the existence of such witnesses that constitutes the truth of *φ*. Providing witnesses is precisely what Skolem functions for *φ* do.[^note-76] The truth of a quantified sentence *φ* amounts to the existence of a full set of Skolem functions for *φ*. In Hintikka’s view, then, our ordinary notion of first-order truth is conceptualized in terms of (existential) second-order logic. What happens when this idea is applied to axiomatic set theory, say Zermelo-Fraenkel set theory with the Axiom of Choice $(\mathbf{ZFC})$? It should be borne in mind that the very idea of axiomatic set theory is to dispense with higher-order logic; its underlying logic is taken to be $\mathbf{FO}$. Hintikka argues as follows.[^note-77]

For each sentence *φ* of $\mathbf{ZFC}$, there is another sentence $\phi^* = (\exists f_1)\ldots(\exists f_n)\psi^*$ of $\mathbf{ZFC}$ which says, intuitively, that ‘Skolem functions’ for *φ* exist. These ‘Skolem functions’ are certain individuals of the domain of a model of $\mathbf{ZFC}$. Here both $\phi^*$ and *φ* are first-order sentences. But if for every sentence *φ* of $\mathbf{ZFC}$ we have *φ* and $\phi^*$ being logically equivalent, why could the sentences $\phi^*$ not be used for formulating a truth-predicate for $\mathbf{ZFC}$ in $\mathbf{ZFC}$ itself? However, by Tarski’s undefinability result, no such truth-predicate exists.[^note-78] So there must be a model of $\mathbf{ZFC}$ and a sentence *φ* true in that model such that $\phi^*$ is false: not all ‘Skolem functions’ asserted to exist by $\phi^*$ actually exist in the model.

This reasoning shows that $\mathbf{ZFC}$ does not fully capture the idea of truth according to which the truth of a sentence *φ* means that the Skolem functions for *φ* exist. Furthermore, it also shows that the standard interpretation of higher-order logic is not fully captured by $\mathbf{ZFC}$. To see this, observe that for every sentence *φ* there is a logically equivalent *second-order* sentence $\phi^{**} = (\exists F_1)\ldots(\exists F_n)\psi^{**}$ actually asserting the existence of Skolem functions for *φ*. The *first-order* sentence $\phi^* = (\exists f_1)\ldots(\exists f_n)\psi^*$ must not be confused with the second-order sentence $\phi^{**} = (\exists F_1)\ldots(\exists F_n)\psi^{**}$. The Skolem functions $F_i$ of which the sentence $\phi^{**}$ speaks are *sets* built out of individuals of the set-theoretical universe, while the ‘Skolem functions’ $f_i$ spoken of by $\phi^*$ are *individuals*.[^note-79]

The conclusion of Hintikka’s argument is that our ordinary notion of truth is misrepresented by $\mathbf{ZFC}$. Furthermore, by Tarski’s undefinability result the situation cannot be improved by adding further axioms to $\mathbf{ZFC}$. In Hintikka’s judgment, axiomatic set theory is a systematic but futile attempt to capture on the first-order level truths of standardly interpreted second-order logic. Like Gödel (1947)[^gödel-1947], also Hintikka holds that the concepts needed to state, say, the continuum hypothesis are sufficiently well-defined to determine the truth-value of this conjecture. The continuum hypothesis does not receive its meaning from phrasing it in $\mathbf{ZFC}$. Gödel and Hintikka agree that the independence results due to Gödel himself and Paul Cohen do not by themselves show anything about the truth or falsity of the continuum hypothesis. But unlike Gödel, Hintikka finds the derivability of any conjecture whatever in $\mathbf{ZFC}$ (or in any of its extensions) simply irrelevant for the truth of the conjecture. For Hintikka, it is a ‘combinatorial’ question whether every infinite subset of the reals is either countable or else has the cardinality of the set of all reals – a question properly conceptualized within second-order logic. This is what Hintikka takes to be the pretheoretical sense of the truth of the continuum hypothesis, and that is not captured by $\mathbf{ZFC}$.[^note-80]

### 5.3 Extended IF first-order logic and mathematical theorizing

Hintikka sees $\mathbf{EIFL}$ as allowing to reconstruct all normal mathematical reasoning on the first-order level. This result is essentially dependent on the acceptability of Hintikka’s claim that $\mathbf{EIFL}$ is ontologically committed to individuals only (*Subsect.* 5.1). But how would $\mathbf{EIFL}$ serve to reconstruct an important part of all mathematical reasoning?

Hintikka (1996: 194–210)[^hintikka-1996][^hintikka-1996-2] discusses mathematical *theories* (or mathematical axiomatizations) and mathematical *problems* (or questions of logical consequence) separately.

Any higher-order *mathematical theory* $T$ gives rise to a many-sorted first-order theory $T^*$. If the theory is finite, there is a finite conjunction $J$ formulated in $\mathbf{EIFL}$ – equivalent to a sentence of $\mathbf{USO}$ and therefore equivalent to the contradictory negation of an $\mathbf{ESO}$ sentence and so indeed equivalent to the contradictory negation of an $\mathbf{IFL}$ sentence – expressing the requirement that the standard interpretation of higher-order logic is respected. The question of the truth of the higher-order theory $T$ is thus reduced to the truth of the sentence $(J \wedge T^*)$ of $\mathbf{EIFL}$ (cf. *Subsect.* 4.6).

The *mathematical problem* of whether a given sentence $C$ is a logical consequence of a finite higher-order theory $T$ coincides with the problem of whether the second-order sentence $(\neg(J \wedge T^*) \vee C^*)$ is valid. Recalling that there is a sentence *χ* of $\mathbf{IFL}$ such that $J$ is equivalent to $\neg \chi$, it follows that $\neg(J \wedge T^*)$ is equivalent to a sentence of $\mathbf{IFL}$. Consequently there is a sentence of $\mathbf{IFL}$ which is valid iff the sentence $(\neg(J \wedge T^*) \vee C^*)$ is valid (cf. *Subsect.* 4.6). Mathematical problems can be understood as questions of the *validity* of an $\mathbf{IFL}$ sentence. Among mathematical problems thus reconstructible using $\mathbf{IFL}$ are the continuum hypothesis, Goldbach’s conjecture, Souslin’s conjecture, the existence of an inaccessible cardinal, and the existence of a measurable cardinal.[^note-81]

As conceptualizations apparently transcending the proposed framework – not expressible in a higher-order logic – Hintikka considers the maximality assumption expressed by David Hilbert’s so-called axiom of completeness. The axiom says that no mathematical objects can be added to the intended models without violating the other axioms.[^note-82]

If indeed problems related to the idea of *all subsets* are avoided in $\mathbf{EIFL}$ (Hintikka 1997)[^hintikka-1997][^hintikka-1997-2][^hintikka-1997-3], it offers a way of defending a certain form logicism. Unlike in historical logicism, the idea is not to consider logic as an axiom system on the same level as mathematical axiom systems (Hintikka 1996: 183)[^hintikka-1996][^hintikka-1996-2],[^note-83] and to attempt to reduce mathematics to logic. Rather, Hintikka (1996: 184)[^hintikka-1996][^hintikka-1996-2] proposes to ask: **(a)** Can the crucial mathematical concepts be defined in logical terms? **(b)** Can the modes of semantically valid logical inferences used in mathematics be expressed in logical terms? The idea is not to concentrate on deductive rules of logic: no complete set of deductive rules exist anyway for $\mathbf{IFL}$. Because the status of higher-order logic is potentially dubious – due to the problems associated with the notion of powerset – a positive solution to questions (a) and (b) calls for a first-order logic more powerful than $\mathbf{FO}$.

The suggested reduction of all mathematics expressible in higher-order logic to the first-order level would be philosophically significant in showing that mathematics is not a study of general concepts, but of structures consisting of particulars (Hintikka 1996: 207)[^hintikka-1996][^hintikka-1996-2]. This is not to say that actual mathematics would be best carried out in terms of $\mathbf{IFL}$, only that it could in principle be so carried out (Hintikka 1996: 205, 2006a: 477)[^hintikka-1996][^hintikka-2006a][^hintikka-1996-2]. For a critique of Hintikka’s conclusions, see Väänänen (2001)[^väänänen-2001], Feferman (2006)[^feferman-2006], and Bazzoni (2015)[^bazzoni-2015].

### 5.4 Informational independence in natural languages

When Hintikka began to apply GTS to the study of natural language (Hintikka 1973a)[^hintikka-1973a], he took up the question of whether branching quantifiers occur in natural languages. He was led to ask whether there are semantic games with imperfect information. He detected various types of grammatical constructions in English that involve informational independence.[^note-84] An often cited example is the sentence

*Some relative of each villager and some relative of each townsman hate each other*,

true under its relevant reading when the choice of a relative of each townsman can be made independently of the individual chosen for ‘each villager.’[^note-85] Hintikka (1973a)[^hintikka-1973a] sketched an argument to the effect that actually every $\mathbf{FPO}$ sentence can be reproduced as a representation of an English sentence. From this it would follow that the logic of idiomatic English quantifiers is much stronger than $\mathbf{FO}$, and that no effective procedure exists for classifying sentences as analytical or nonanalytical, synonymous or nonsynonymous.[^note-86] This would be methodologically a very important result, showing that syntactic methods are even in principle insufficient in linguistic theorizing. Jon Barwise (1979)[^barwise-1979] suggested that particularly convincing examples supporting Hintikka’s thesis can be given in terms of generalized quantifiers.

Lauri Carlson and Alice ter Meulen (1979) were the first to observe cases of informational independence between quantifiers and intensional operators. Consider the question[^note-87]

*Who does everybody admire?*

Under one of its readings, the presupposition of this question is $(\forall x)(\exists y)$ admires$(x, y)$. The desideratum of this question is

*I know who everybody admires.*

Writing ‘$K_I$’ for ‘I know,’[^note-88] the desideratum has a reading whose logical form is

$K_I (\forall x)(\exists y/K_I)$ admires$(x, y)$.

This desideratum is satisfied by an answer pointing out a function $f$ which yields for each person a suitable admired person. Such a function can be *his or her father*. Importantly, the value $f(b)$ of this function only depends on the person $b$ interpreting ‘everybody,’ but does not depend on the scenario $w$, compatible with the questioner’s knowledge, that interprets the construction ‘I know.’ Interestingly, the desideratum $K_I (\forall x)(\exists y/K_I)$ admires$(x, y)$ is not expressible without an explicit independence indicator. It is also worth noting that this case cannot be represented in the notation of $\mathbf{FPO}$. This is because several types of semantic interactions are possible among quantifiers and intensional operators, and blocking interactions of one type does not automatically block interactions of other types. In the example, the witness of $\exists y$ must not vary with the scenario $w$ interpreting the operator $K_I$, but still the values of both variables $x$ and $y$ must belong to the domain of the particular scenario $w$ chosen to interpret $K_I$.[^note-89]

Hintikka’s ideas on desiderata of wh-questions were influenced by his exchange with the linguist Elisabet Engdahl.[^note-90] These wh-questions, again, functioned as important test cases for the appearance of informational independence in natural languages.

Hintikka and Sandu (1989) took up the task of formulating an explicit unified formal treatment for the different varieties of informational independence in natural language semantics. They posed the question of which are the mechanisms that allow English to exceed the expressive power of $\mathbf{FO}$. For, natural languages typically do not resort to higher-order quantifiers. Hintikka and Sandu suggested that informational independence plays a key role in increasing the expressive power of natural languages.[^note-91]

In GTS as developed for English in Hintikka & Kulas (1983, 1985), game rules are associated with a great variety of linguistic expressions (cf. *Subsect.* 2.1). As Hintikka (1990)[^hintikka-1990] has stressed, informational independence is a cross-categorical phenomenon: it can occur in connection with expressions of widely different grammatical categories. Hintikka and Sandu (1989) propose several examples from English calculated to show that there is an abundance of instances of informational independence in natural languages. Among examples are wh-questions of the kind discussed above, and the distinction between the *de dicto* and *de re* readings of certain English sentences. Hintikka and Sandu suggest that representing such readings in terms of IF logic is more truthful to the syntax of English than the alternative, non-IF representations are.

In connection with knowledge, a *de dicto* attribution such as

$K_{\textit{Ralph}} (\exists x) (x$ is a spy)

can be turned into a *de re* attribution by marking the existential quantifier as independent of the knowledge-operator (cf. Hintikka and Sandu 1989)[^hintikka-1989]:

$K_{\textit{Ralph}} (\exists x/K_{\textit{Ralph}}) (x$ is a spy).

Because knowledge is a factive attitude (the actual world is among Ralph’s epistemic alternatives), this amounts indeed to the same as the condition

$(\exists x) K_{\textit{Ralph}} (x$ is a spy).

Rebuschi & Tulenheimo (2011) observed that independent quantifiers are of special interest in connection with non-factive attitudes such as belief. The logical form of a statement ascribing to Ralph a belief pertaining to a specific but non-existent object is

$B_{\textit{Ralph}} (\exists x/B_{\textit{Ralph}}) (x$ is a spy),

where ‘$B_{\textit{Ralph}}$’ stands for ‘Ralph believes that.’[^note-92]

Attitudes of this form were dubbed *de objecto* attitudes. Since the (intentional) object of such an attitude need not exist actually, the *de objecto* attitude is weaker than the *de re* attitude

$(\exists x) B_{\textit{Ralph}} (x$ is a spy).

On the other hand, the pattern of operators $B_{\textit{Ralph}} (\exists x/B_{\textit{Ralph}})$ requires that the witness of the existential quantifier $\exists x$ be the same relative to all doxastic alternatives of Ralph, so the *de objecto* attitude is stronger than the *de dicto* attitude

$B_{\textit{Ralph}} (\exists x) (x$ is a spy).

Janssen (2013)[^janssen-2013] discusses the possibility of providing in terms of $\mathbf{IFL}$ a compositional analysis of the *de re* / *de dicto* ambiguity in natural languages. Brasoveanu and Farkas (2011) argue that scopal properties of natural language indefinites are best elucidated in terms of a semantics inspired by $\mathbf{IFL}$, more precisely by formulating the semantics relative to sets of variable assignments as done in Hodges’s compositional semantics for slash logic.

As a rule, informational independence is not indicated syntactically in English.[^note-93] Methodological consequences of this fact are discussed in Hintikka (1990)[^hintikka-1990], where he tentatively puts forward the *Syntactic Silence Thesis*, according to which sufficiently radical cross-categorical phenomena are not likely to be marked syntactically in natural languages. Evidence for this thesis would, for its part, be evidence against the sufficiency of syntax-oriented approaches to semantics.

## 6. Related logics

### 6.1 Slash logic

Syntactically slash logic uses quantifiers like $(\exists x/y)$ instead of quantifiers such as $(\exists x/\forall y)$. Semantically slash logic is otherwise like $\mathbf{IFL}$ except that its game-theoretical semantics is based on the idea that a player’s strategy functions may utilize as their arguments *any* preceding moves made in the current play, save for those whose use is, by the slash notation, explicitly indicated as forbidden (cf. *Sect.* 3). That is, also a player’s own earlier moves may appear as arguments of a strategy function. This can make a difference in the presence of imperfect information. For example, consider evaluating the slash-logic sentence $(\forall x)(\exists y)(\exists z/x) x = z$ containing the vacuous quantifier $\exists y$. This sentence is true on a two-element domain, since player 2 can copy as the value of $y$ the value that player 1 has chosen for $x$, and then select the value of $z$ using a strategy function whose only argument is the value of $y$. (For this phenomenon of ‘signaling,’ see Hodges 1997a, Sandu 2001, Janssen & Dechesne 2006, Barbero 2013.)[^barbero-2013][^hodges-1997a][^hodges-2006][^hodges-2013][^janssen-2013][^janssen-2006][^sandu-2001][^sandu-2013][^sandu-2001-2][^sandu-2001-3] By contrast, the IF sentence $(\forall x)(\exists y)(\exists z/\forall x) x = z$ fails to be true on such a domain, since there a strategy function for $(\exists z/\forall x)$ must be a constant, and no such strategy function can guarantee a win for player 2 against both possible values that player 1 can choose for $x$. As mentioned in *Subsection* 4.4, Hodges (1997a,b) showed that slash logic admits of an alternative, compositional semantics. This requires evaluating formulas relative to sets of variable assignments, instead of single assignments as in connection with $\mathbf{FO}$.

All authors having studied slash logic, apart from Hodges himself, have opted for not following Hodges’s terminological recommendation mentioned at the beginning of Section 3: they have referred to slash logic as ‘IF logic.’

Kuusisto (2013)[^kuusisto-2013] studies the expressive power of fragments of slash logic whose formulas are formed without employing the identity symbol. Kontinen *et al.* (2014) investigate the complexity-theoretic properties of the two-variable fragment of slash logic and compare this fragment to the corresponding fragment of dependence logic. Hodges (1997a,b) and Figueira *et al.* (2009, 2011, 2014) discuss an extension of slash logic in which the contradictory negation of slash-logic sentences can be expressed.

In Sevenster (2014)[^sevenster-2014], patterns of quantifier dependence and independence in quantifier prefixes of slash-logical formulas are systematically studied in order to determine which quantifier prefixes allow slash logic to gain the expressive power of $\mathbf{ESO}$. Sevenster identifies two such patterns – the *signaling* pattern and the *Henkin* pattern – and proves that they are able to express $\mathbf{NP}$-hard decision problems. He further shows that these two are the only patterns allowing slash logic to exceed the expressive power of $\mathbf{FO}$ insofar as attention is confined to formulas in prenex form. An example of the signaling pattern would be $ (\forall u)(\exists v)(\exists w/u) $ and of the Henkin pattern $ (\forall x)(\exists u)(\forall y)(\exists v/x,u) $.[^note-94]

Barbero (2021)[^barbero-2021][^barbero-2021-2] and Barbero *et al.* (2021) take up the task of investigating fragments of the general syntax of slash logic (not all of whose formulas are in prenex form). Thereby these authors wish to study systematically those expressive resources of slash logic that allow it to exceed the expressive power of $\mathbf{FO}$ and that do not simply derive from its capacity to mimick Henkin quantifiers. While many of the features studied in these two papers depend on the *Eigenart* of slash logic, the phenomenon of *signaling by disjunction* occurs in IF logic, as well. In Section 3.3, it was seen that the IF-logical sentence $(\forall x)(\exists y/\forall x) x = y$ is non-determined in any model whose domain has exactly two elements. The slash-logical sentence $(\forall x)(\exists y/ x) x = y$ is likewise non-determined in such a model. Now, consider the result of replacing in the latter sentence the expression $(\exists y/ x) x = y$ by the disjunction $((\exists y/x) x = y \vee (\exists y/ x) x = y))$, with a token of the initial expression in both disjuncts: $$ (\forall x)((\exists y/ x) x = y \vee (\exists y/x) x = y). $$ The sentence that has been thus obtained is actually *true* in a model whose domain consists of the objects $a$ and $b$. Let $f$, $g$, and $h$ be respectively the strategy functions of player 2 for the unique token of the disjunction symbol, the left token of the existential quantifier, and the right token of the existential quantifier – defined as follows. First, $f$ selects the left disjunct if player 1 has chosen $a$ as a value of $x$, selecting the right disjunct otherwise. Further, $g$ and $h$ are constants (zero-place functions): $g= a$ and $h= b$. The set $\{f, g, h\}$ is clearly a winning strategy for player 2. Either of the tokens of the existential quantifier occur in a specific disjunct. Using the strategy function $f$ to arrive at such a disjunct makes sure that the disjunct arrived at reveals the choice that player 1 has made to interpret $\forall x$. The constants $g$ and $h$ are selected so as to render this information explicit. Thus, the resulting values of $x$ and $y$ indeed satisfy the formula $x= y$. By the same reasoning it is seen that the sentence $(\forall x)((\exists y/ \forall x) x = y \vee (\exists y/\forall x) x = y)$ of $\mathbf{IFL}$ is true in the model considered.

### 6.2 Dependence logic

Jouko Väänänen (2007)[^väänänen-2007] formulated a new approach to IF logic that he dubbed *dependence logic* $(\mathbf{DL})$; for further work on $\mathbf{DL}$, see *e.g.* Kontinen *et al.* (2013). The syntax of $\mathbf{DL}$ is obtained from that of $\mathbf{FO}$ by allowing atomic formulas of the following special form:

$$ =(x_1 ,\ldots ,x_n; x_{n+1}). $$

Intuitively such a formula means that the value of $x_{n+1}$ depends only on the values of $x_1 ,\ldots ,x_n$. The semantics of $\mathbf{DL}$ cannot be formulated relative to single variable assignments like that of $\mathbf{FO}$: we cannot explicate what it means for the value of $x_{n+1}$ to depend on those of $x_1 ,\ldots ,x_n$ with reference to a single assignment on the variables $x_1 ,\ldots ,x_{n+1}$. For example, consider the assignment described below:

| $x_1$ | $x_2$ | $x_3$ |
| --- | --- | --- |
| 7 | 5 | 8 |

Relative to this assignment, all of the following claims hold: whenever the value of $x_1$ equals 7, the value of $x_3$ equals 8; whenever the value of $x_2$ equals 5, the value of $x_3$ equals 8; whenever the value of $x_1$ equals 7 and the value of $x_2$ equals 5, the value of $x_3$ equals 8; irrespective of the values of $x_1$ and $x_2$, the value of $x_3$ equals 8. The question of dependence only becomes interesting and non-vacuous relative to a set of assignments:

| $x_1$ | $x_2$ | $x_3$ |
| --- | --- | --- |
| 7 | 5 | 8 |
| 9 | 5 | 6 |
| 7 | 11 | 8 |
| 7 | 3 | 8 |
| 9 | 19 | 6 |

The set $X$ consisting of the above five assignments satisfies the formula $=(x_1$; $x_3)$: the value of $x_3$ depends only on the value of $x_1$. As is readily observed, any two assignments in $X$ which assign the same value to $x_1$ assign also the same value to $x_3$. The interesting novelty of $\mathbf{DL}$ is that claims about variable dependencies are made at the atomic level. Quantifiers of $\mathbf{IFL}$ and those of slash logic with their independence indications easily lead to somewhat messy formulas, whereas $\mathbf{DL}$ looks exactly like $\mathbf{FO}$, apart from its greater flexibility in forms of atomic formulas.

## 7. Conclusion

In this entry IF first-order logic and extended IF first-order logic have been surveyed. Their metalogical properties have been explained and the philosophical relevance of these properties has been discussed. The suggested consequences of these logics for philosophical issues such as the existence of a self-applied truth-predicate, the logicist program, the philosophical relevance of axiomatic set theory, and informational independence in natural languages have been covered as well. Slash logic and dependence logic – both closely related to $\mathbf{IFL}$ and inspired by it – were also briefly considered.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=logic-if). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/logic-if/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=logic-if&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/logic-if/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

[Please contact the author with suggestions.]

## Related Entries

compositionality | game theory | generalized quantifiers | logic: and games | logic: classical | logic: dependence | logic: dialogical | logic: epistemic | logic: intensional | logic: intuitionistic | logic: modal | logic: second-order and higher-order | model theory | reasoning: automated | set theory | Tarski, Alfred: truth definitions

## Notes（原文脚注）

[^note-1]: The work of providing solid foundations to analysis was initiated by Augustin Cauchy (1789–1857).

[^note-2]: For references to uses of the device ‘depends on…but not on…’ in actual mathematical literature, see Dechesne (2005)[^dechesne-2005], Hintikka (1996)[^hintikka-1996][^hintikka-1996-2], Hintikka & Kulas (1983), Hodges (1997a, 1997b)[^hodges-1997a][^hodges-1997b], Mann *et al.* (2011), Mostowski & Krynicki (1995)[^krynicki-1995], Pietarinen (2001)[^pietarinen-2001]; for dependent quantifiers, see also Quine (1970)[^quine-1970]. Bazzoni (2015)[^bazzoni-2015] criticizes Hintikka’s remarks about the expressibility of uniformity concepts in IF logic, arguing that such remarks cannot show the relevance of IF logic to mathematical theorizing.

[^note-3]: In order to properly assess the origins of IF first-order logic in light of available documents, also the following should be noted. Hintikka writes (1991: 7): “IF first-order languages are introduced and studied in my paper, ‘What is Elementary Logic?’ (forthcoming).” This paper appeared as Hintikka (1995)[^hintikka-1995]. Hintikka (1991: 8,67) refers to the papers published in Sandu’s Ph.D. thesis, saying that in them Sandu has also studied independence friendly languages; he mentions specifically Sandu’s study of informationally independent connectives in Sandu & Väänänen (1992), as well as Hintikka & Sandu (1989). In Hintikka & Sandu (1997: 368) it is stated that IF languages were introduced in Hintikka & Sandu (1989) – contradicting what is said in Hintikka (1991)[^hintikka-1991][^hintikka-1991-2]. Hintikka (1996: 52)[^hintikka-1996][^hintikka-1996-2] mentions Sandu (1993)[^sandu-1993] and Hintikka (1995)[^hintikka-1995] as sources for earlier discussions on IF first-order logic; Hintikka & Sandu (1989) is not mentioned. In Sandu & Hyttinen (2001: 37) it is said that IF first-order languages were introduced in Hintikka (1996)[^hintikka-1996][^hintikka-1996-2], but on the next page it is affirmed that these languages were introduced in Hintikka & Sandu (1989).

The slash notation used for indicating quantifier independence appears already in Hintikka (1988: 22)[^hintikka-1988]. A general notation for separately indicating those preceding operators of which a given one is independent – more general than the notation of partially ordered quantifiers – was proposed in connection with epistemic logic even earlier, in Hintikka (1982: 164)[^hintikka-1982].

[^note-4]: Thoralf Skolem (1887–1963) introduced Skolem functions in Skolem (1920)[^skolem-1920]. For uses of Skolem functions in model theory, see *e.g.* Hodges (1993)[^hodges-1993]. They have also found use in automated theorem proving; cf. the entry on automated reasoning. On how they are employed in linguistics, cf. footnote 90.

[^note-5]: *I.e.*, a function with zero arguments.

[^note-6]: Here and henceforth, ‘iff’ abbreviates ‘if and only if.’

[^note-7]: The function $f$ yields a witness for $\exists y$ depending on the interpretation of $\forall x$, and similarly $g$ provides a witness for $\exists w$ depending on the interpretation of $\forall z$.

[^note-8]: Henkin introduced the general idea of *dependent quantifier* $Q_{m, n, d}$, which in effect leads to the notion of (arbitrary) partially ordered quantifier (p.o.q.) with $m$ universal quantifiers and $n$ existential quantifiers, where $d$ is a function that determines for each existential quantifier on which universal quantifiers it depends; $m$ and $n$ may be any cardinal numbers. The notion of finite p.o.q. results by letting $m$ and $n$ be finite. Well-known papers on finite p.o.q.s include Enderton (1970)[^enderton-1970], Walkoe (1970)[^walkoe-1970], Barwise (1979)[^barwise-1979], Krynicki & Lachlan (1979), Blass & Gurevich (1986), Krynicki (1993)[^krynicki-1993]; for an overview, see Krynicki & Mostowski (1995). In Barwise (1979)[^barwise-1979] *generalized* partially ordered quantifiers were also studied.

[^note-9]: $\mathbf{FPO}$ is *not* syntactically closed under negation, conjunction, or disjunction.

[^note-10]: For a critique, see Hodges (2013)[^hodges-2013], Marion (2009)[^marion-2009].

[^note-11]: Let us agree that player 1 is male (‘he’) and player 2 female (‘she’). In the literature, the players have been called by many names: *Myself* (or $I)$ and *Nature*, $\exists$ and $\forall$, *Eloise* and *Abelard*, as well as the *initial Verifier* and the *initial Falsifier* (by reference to the players’ initial roles).

[^note-12]: Henceforth, whenever $M$ is a model, M is its domain.

[^note-13]: Note that while quantifier moves pertain to ‘objects out there’ (elements of the domain), moves for conjunction and disjunction concern syntactic items (conjuncts and disjuncts).

[^note-14]: For abstract and strategic meaning, cf. also Hintikka & Sandu (1997: 397–398). For research on GTS and natural language, see Saarinen (1979), Hintikka & Sandu (1991)[^sandu-1991], Sandu (1991)[^sandu-1991], Pietarinen (2001)[^pietarinen-2001], Clark (2012)[^clark-2012]; Hintikka & Sandu (1997) offers an overview. Cf. also Janssen (2013)[^janssen-2013].

[^note-15]: In any event, this is the way in which Hintikka uses the word ‘Skolem function,’ see, *e.g.*, Hintikka (1996: 31; 2002). Cf. Sandu (2001)[^sandu-2001][^sandu-2001-2][^sandu-2001-3], where ‘two ways of Skolemizing’ are discussed. One of the two ways corresponds to Hintikka’s notion of Skolem function, the other corresponding to a generalized notion of strategy function. What results from the latter choice is, in Hodges’s terminology, a slash logic, not an IF logic; cf. the quote below.

[^note-16]: Excluding slash logic still underdetermines the choice between several proposed formulations of IF first-order logic. Apart from formulations that use in their semantics Skolem functions, or strategy functions all of whose arguments are moves by the opponent, even different ‘epistemic interpretations’ can be considered; see Barbero (2017)[^barbero-2017]. Publications in which a slash logic is actually formulated – yet referred to as an IF logic – include Hyttinen & Sandu (2000), Pietarinen (2001)[^pietarinen-2001], Väänänen (2002)[^väänänen-2002], Sandu (2007)[^sandu-2007], Caicedo *et al.* (2009), Mann *et al.* (2011), Barbero (2013)[^barbero-2013], Kontinen *et al.* (2014), Sevenster (2014)[^sevenster-2014], Barbero *et al.* (2021), and Barbero (2021)[^barbero-2021][^barbero-2021-2].

[^note-17]: For the term ‘regular formula,’ see Caicedo *et al.* (2009). The logical symbols of first-order logic considered here are negation $({\sim})$, disjunction $(\vee)$, conjunction $(\wedge)$, existential quantifier $(\exists)$, universal quantifier $(\forall)$, identity symbol $(=)$, and parentheses. See the entry on classical logic for a detailed presentation of first-order logic.

Note that implication is not among the logical symbols of IF first-order logic. Material implication $(\phi \rightarrow \psi)$ can be defined in the so-called extended $\mathbf{IFL}$ (*Subsect*. 3.4) by the formula $(\neg \phi \vee \psi)$. In the special case that *φ* is ‘truth equivalent’ to a first-order formula (see *Subsect.* 4.2), it is possible to express $(\phi \rightarrow \psi)$ in $\mathbf{IFL}$ by the formula $({\sim}\phi \vee \psi)$. For different ways of treating conditionals in GTS, including conditionals in natural language, see *e.g.* Hintikka & Kulas (1983; *Ch.* 3), Hintikka & Sandu (1991)[^sandu-1991].

[^note-18]: In the literature, the syntax of $\mathbf{IFL}$ is invariably given for *formulas*. By contrast, the semantics is often formulated for *sentences* only (see Hintikka 1991, 1995, 1996; Hintikka & Sandu 1996, 1997; Sandu 1993, 1994)[^hintikka-1991][^hintikka-1995][^hintikka-1996][^hintikka-1997][^hintikka-1997-2][^hintikka-1991-2][^hintikka-1996-2][^hintikka-1997-3][^sandu-1993][^sandu-1994][^sandu-1996]. In Sandu (1996, 1998)[^sandu-1996][^sandu-1998], the semantics is given for arbitrary formulas.

[^note-19]: See, *e.g.*, Hintikka (1991, 1995, 1996)[^hintikka-1991][^hintikka-1995][^hintikka-1996][^hintikka-1991-2][^hintikka-1996-2], Sandu (1993, 1994)[^sandu-1993][^sandu-1994]; for defining GTS for $\mathbf{FO}$ in this way, see *e.g.* Hintikka & Kulas (1983), cf. Hintikka (1968, 1973a)[^hintikka-1968][^hintikka-1973a]. The semantics of $\mathbf{IFL}$ to be presented will be its game-theoretical semantics, sketched in Hintikka & Sandu (1989) and Hintikka (1991)[^hintikka-1991][^hintikka-1991-2] and presented in a more detailed fashion *e.g.* in Hintikka (1995, 1996)[^hintikka-1995][^hintikka-1996][^hintikka-1996-2], Sandu (1993, 1994)[^sandu-1993][^sandu-1994]. The semantics is defined explicitly to arbitrary formulas and variable assignments in Sandu (1996, 1998)[^sandu-1996][^sandu-1998]. The original approach to the GTS of first-order logic in Hintikka (1968)[^hintikka-1968] avoided variable assignments by letting the players name the objects they had chosen; this approach could be adapted to $\mathbf{IFL}$ as well. Janssen (2002)[^janssen-2002] and Janssen & Dechesne (2006) address the issue of whether the game-theoretical semantics of $\mathbf{IFL}$ does justice to the idea of ‘informational independence’ among logical operators.

[^note-20]: A model of vocabulary *τ* is a structure comprising two components: a non-empty set $D$ of objects termed ‘individuals’ (the *domain* of the model) and an *interpretation function* that associates each element of the vocabulary *τ* with a suitable entity based on the domain (each constant symbol is mapped to an element of $D$, each $n$-ary relation symbol is mapped to a subset of $D^n$, and each $n$-ary function symbol is mapped to a function of type of $D^n \rightarrow D$). A variable assignment is a function whose domain is a given set of variables and whose values are elements of the domain of the model being considered. Models themselves are termed *interpretations* in the entry on classical logic. Recall that in the degenerate case that $n = 0$, the expression $(\exists x/\forall y_1 ,\ldots ,\forall y_n)$ equals by stipulation $(\exists x)$, and similarly in the case of the other connectives followed by a slash. This is why we need not give separate clauses for $(\exists x), \vee , (\forall x)$, and $\wedge$.

[^note-21]: The notion of the strategy of a player must not be confused with the game-theoretical notion of *strategy profile*. The latter means a set of strategies, one strategy for each player. For semantic games, a strategy profile would be a set $\{F_1, F_2\}$, where each $F_i$ itself is a set, namely a set of strategy functions of player $i$.

[^note-22]: The term ‘dissatisfaction’ is used as a dual of ‘satisfaction.’ The distinction between these notions generalizes the distinction between ‘truth’ and ‘falsity.’ Hodges (1997a)[^hodges-1997a] conceptualizes a related distinction in his compositional framework by speaking of ‘trumps’ and ‘cotrumps.’ Hintikka (1996, *Ch.* 10) proposed that a ‘constructive’ interpretation could be given to IF logic by requiring that winning strategies be composed of *recursive* strategy functions. This idea is developed in detail in Odintsov *et al.* (2018).

[^note-23]: To be precise, below game $G(\phi , M)$ equals by definition game $G(\phi , M, g_0)$, where $g_0$ is an arbitrarily chosen variable assignment.

[^note-24]: When negation symbol is allowed to appear in arbitrary syntactic positions in $\mathbf{FO}$ formulas, it is no longer the case that universal quantifiers and conjunction symbols are automatically of *universal force* while existential quantifiers and disjunction symbols are of *existential force*. The force of an operator depends on the number of negation signs in whose syntactic scope it lies. If we wish to retain in the general setting the characteristic feature distinguishing $\mathbf{IFL}$ from slash logic – namely the requirement that strategy functions of a player only take as arguments moves made by the adversary – the syntax must be formulated paying attention to the force that each quantifier has (cf. however Sandu 1993, 1994; Hintikka & Sandu 1997: 373)[^hintikka-1997][^hintikka-1997-2][^hintikka-1997-3][^sandu-1993][^sandu-1994]. In the general formulation of $\mathbf{IFL}$, hence formulated, an operator O can be marked as independent from any preceding quantifiers of the *opposite force*, but not from any preceding quantifier having the same force as O. For example $(\forall x){\sim}(\exists y)(\forall z/\forall x,\exists y) S(x, y, z)$ would be well formed, unlike ${\sim}(\forall x){\sim}(\exists y/\forall x) R(x, y)$.

[^note-25]: See *e.g.* Hintikka (1991: 147, 2002: 409), Hodges (1997a: 546)[^hodges-1997a], Sandu (1993, 1994)[^sandu-1993][^sandu-1994].

[^note-26]: For non-determinacy and IF logic, see Hintikka (1996)[^hintikka-1996][^hintikka-1996-2], Burgess (2003)[^burgess-2003], Väänänen (2006)[^väänänen-2006].

[^note-27]: No third truth-value is stipulated in the semantics of $\mathbf{IFL}$. Truth-value gaps may arise when neither truth nor falsity can be meaningfully ascribed to a sentence (because a presupposition of the sentence is not satisfied). This is not what non-determinacy means. Non-determinacy is a model-relative complex negative property, which can be ascribed to a sentence. A sentence has this property iff neither of the simple positive properties of truth and falsity can be correctly ascribed to the sentence. An ascription of non-determinacy is correct or incorrect depending exclusively on the model relative to which the ascription is effected.

[^note-28]: For ‘truth equivalence’ Hintikka uses the term ‘weak equivalence’ and for ‘logical equivalence’ the term ‘strong equivalence’ (cf. Hintikka 1996: 150)[^hintikka-1996][^hintikka-1996-2]. He characterizes strong equivalence as the preservation of truth and falsity. Thus if *ψ* and *χ* are strongly equivalent, nothing prevents *ψ* from being non-determined in a model, as long as *χ* also is. (On other occasions, *e.g.* in Hintikka 1991: 20, Hintikka defines ‘strong equivalence’ differently, by the requirement that either *ψ* and *χ* are both true or both false; this precludes the possibility that one or both of two strongly equivalent sentences would be non-determined.)[^hintikka-1991][^hintikka-1991-2] The term ‘truth equivalence’ used by Dechesne (2005: 32)[^dechesne-2005] is more descriptive. The term ‘falsity equivalence’ also stems from Dechesne. She follows Hintikka in terming ‘strong equivalence’ what is here for simplicity referred to as ‘logical equivalence’.

[^note-29]: Cf. Hintikka (1996: 147)[^hintikka-1996][^hintikka-1996-2], Hodges (1997a: 546)[^hodges-1997a], Sandu (1993, 1994)[^sandu-1993][^sandu-1994].

[^note-30]: In Hintikka (1996: 149)[^hintikka-1996][^hintikka-1996-2] this logic is termed *truth-functionally extended IF first-order logic* – in contradistinction to ‘extended IF first-order logic,’ which in Hintikka (1991: 47, 1996: 149) and Hintikka & Sandu (1997) is defined as containing, in addition to $\mathbf{IFL}$ formulas, only formulas $\neg \phi$, where *φ* is an $\mathbf{IFL}$ formula (or sentence). The considerations that motivate the introduction of $\neg$ in the first place, actually call for the more general syntax (witness Hintikka 1996: 149, 195–196)[^hintikka-1996][^hintikka-1996-2], which is why it is natural to define extended IF first-order logic as it is done here. For extended IF first-order logic, see also Hintikka (1991: 49; 1997; 2004).

[^note-31]: Cf. Hintikka (1991: 49; 1996: 147–149; 2002), Hintikka & Sandu (1997: 375), Sandu (1993, 1994)[^sandu-1993][^sandu-1994].

[^note-32]: Cf. Hintikka (1991, 1995, 1996, 1997)[^hintikka-1991][^hintikka-1995][^hintikka-1996][^hintikka-1997][^hintikka-1997-2][^hintikka-1991-2][^hintikka-1996-2][^hintikka-1997-3], Hintikka & Sandu (1996)[^sandu-1996], Sandu (1993, 1996, 1998)[^sandu-1993][^sandu-1996][^sandu-1998]. Analogous properties of (what on substantial criteria is) slash logic are discussed in Sandu (2007)[^sandu-2007] and Mann *et al.* (2011); recall Hodges’s distinction between independence friendly logic and slash logic (see the beginning of *Sect.* 3). Properties of another related logic, Väänänen’s dependence logic, are in a mathematically detailed fashion covered in Väänänen (2007)[^väänänen-2007]. For more information on dependence logic, see the entry on dependence logic.

[^note-33]: For (existential) second-order logic, see the entry on second-order and higher-order Logic. See also van Benthem and Doets (2001).

[^note-34]: Cf. the entry on the axiom of choice.

[^note-35]: In Hodges (2006: 527; 2013), it is pointed out that a strengthened version of this theorem can be proven if a weakened notion of strategy is applied (cf. also Hintikka 2006a: 536)[^hintikka-2006a]. Related observations are made in Forster (2006)[^forster-2006]. Namely, the standard notion of strategy employed in GTS is that of *deterministic* strategy: a set of single-valued functions yielding for any given tuple of arguments a unique move. A *nondeterministic* strategy of player 2 consists of a set of instructions, each instruction yielding a *set* of moves for any tuple of earlier moves by player 1. A nondeterministic strategy of player 2 is *winning* if it guarantees a win for player 2, regardless of which move, among those given by the strategy, player 2 makes in each case when it is her turn to move.

> **Theorem (without AC).** (Hodges 2013)[^hodges-2013] Let *τ* be any vocabulary, $M$ any *τ* structure, $g$ any variable assignment and *φ* any $\mathbf{FO}[\tau$] formula. Then $M, g \vDash \phi$ holds in the standard sense iff there is a nondeterministic winning strategy for player 2 in game $G(\phi , M, g)$.

For finite partially ordered quantifiers and AC, see Krynicki & Mostowski (1995; *Sect.* 2).

[^note-36]: The intertranslatability of the two logics is discussed in Hintikka (1991, 1996, 1997)[^hintikka-1991][^hintikka-1996][^hintikka-1997][^hintikka-1997-2][^hintikka-1991-2][^hintikka-1996-2][^hintikka-1997-3], Hintikka & Sandu (1997), Sandu (1998)[^sandu-1998].

[^note-37]: If *φ* and *ψ* are atomic $\mathbf{IFL}$ formulas, let us write $(\phi \rightarrow \psi)$ for $({\sim}\phi \vee \psi)$, and $(\phi \leftrightarrow \psi)$ for $((\phi \rightarrow \psi) \wedge(\psi \rightarrow \phi))$; cf. footnote 17. Further, $x \ne y$ is used as an abbreviation of ${\sim}x=y$.

[^note-38]: A Hamiltonian path on a graph is a path visiting every node exactly once. For Fagin’s theorem and references to $\mathbf{NP}$-complete problems, see *e.g.* Ebbinghaus & Flum (1999), Grädel *et al.* (2007), Papadimitriou (1994)[^papadimitriou-1994]. For partially ordered quantifiers, partially ordered connectives, and $\mathbf{NP}$-complete problems, see Blass & Gurevich (1986), Hella & Sandu (1995).

[^note-39]: For a discussion, see Hintikka (1991, 1995, 1996)[^hintikka-1991][^hintikka-1995][^hintikka-1996][^hintikka-1991-2][^hintikka-1996-2], Hintikka & Sandu (1997), Sandu (1993)[^sandu-1993]. Paying due attention to Hodges’s warning against confusing slash logic and IF logic, one may reconstruct proofs for various properties of $\mathbf{IFL}$ on the basis of Väänänen’s results concerning his dependence logic (Väänänen 2007)[^väänänen-2007]. The results pertaining to (what in substance is) slash logic discussed in (Sandu 2007)[^sandu-2007] and in (Mann *et al.* 2011)[^mann-2011] can likewise be compared with the analogous results concerning $\mathbf{IFL}$.

[^note-40]: A complete disproof procedure is a procedure for recursively enumerating all inconsistent sentences. The term ‘complete proof procedure for inconsistency’ might involve a smaller risk of being misunderstood (cf., *e.g.*, Quine 1970: 90)[^quine-1970]. In any event, disproving must be understood as ‘establishing inconsistent,’ not as ‘establishing not provable’ (or ‘establishing not valid’).

[^note-41]: For the fact that $\mathbf{ESO}$ is not closed under negation, cf. *e.g.* Hinman (1978: 82)[^hinman-1978].

[^note-42]: For a proof phrased in terms of $\mathbf{FPO}$, see Barwise (1979: 56, 73–74).

[^note-43]: Actually, it is non-determined in all domains with at least two elements.

[^note-44]: Fragments of $\mathbf{ESO}$ have been subject to lively interest in finite model theory and complexity theory, see *e.g.* Ebbinghaus & Flum (1999), Grädel *et al.* (2007), Papadimitriou (1994)[^papadimitriou-1994]. For related work on partially ordered quantifiers and connectives, see Blass & Gurevich (1986), Hella & Sandu (1995), Hella, Sevenster & Tulenheimo (2008). For the $\mathbf{P} = \mathbf{NP}$ problem, see *e.g.* Fortnow (2009)[^fortnow-2009].

[^note-45]: That there is a sound and complete proof procedure for $\mathbf{FO}$ was first proven by Kurt Gödel (1930)[^gödel-1930]. There are different variants of axiomatizability. Let $L$ be a logic, $A$ a set of sentences of $L$, and $P$ a proof procedure for $L$. Then $A$ is an *axiomatization* of $L$ relative to $P$, if the sentences of $L$ provable in $P$ from the sentences of $A$ are precisely the valid sentences of $L$. The logic $L$ is *finitely axiomatizable* (resp. *recursively axiomatizable,* resp. *axiomatizable*) relative to $P$, if it has a finite (*resp.* recursive, *resp.* recursively enumerable) axiomatization $A$ relative to $P$.

[^note-46]: See Hintikka (1991, 1995, 1996, 2000)[^hintikka-1991][^hintikka-1995][^hintikka-1996][^hintikka-2000][^hintikka-1991-2][^hintikka-1996-2].

[^note-47]: The theorem was proven by Boris Trakhtenbrot (1950)[^trakhtenbrot-1950]. For Trakhtenbrot’s theorem, see Ebbinghaus, Flum & Thomas (1984). Andrzej Mostowski (1957)[^mostowski-1957] proved, without recourse to Trakhtenbrot’s theorem, that extending $\mathbf{FO}$ with a quantifier capable of saying that a formula of one free variable is satisfied by finitely many elements only, results in a logic that is not axiomatizable.

[^note-48]: The fact that $\mathbf{FPO}$ fails to have a sound and complete proof procedure can be seen by reference to Trakhtenbrot’s theorem. In 1958 Ehrenfeucht showed that $\phi_{inf}$ can be expressed in $\mathbf{FPO}$; see Henkin (1961)[^henkin-1961]. From this he concluded – making use of Mostowski’s result mentioned in footnote 47 – that the Boolean closure of $\mathbf{FPO}$ (*i.e.*, its closure under the operations $\neg , \wedge$, and $\vee)$ is not axiomatizable. From Mostowski’s result the non-axiomatizability of $\mathbf{FPO}$ itself does *not* follow (since the finiteness of an extension is not expressible in $\mathbf{FPO})$.

[^note-49]: See *e.g.* Hintikka (2006a: 65)[^hintikka-2006a], Sandu & Hintikka (2001: 49)[^hintikka-2001]. For compositionality and GTS, see Hintikka & Kulas (1983), Hintikka & Sandu (1997). For a discussion on different senses of compositionality and $\mathbf{IFL}$, see Hintikka (1996)[^hintikka-1996][^hintikka-1996-2], Sandu & Hintikka (2001)[^hintikka-2001]. Cf. also the entry on compositionality.

[^note-50]: See *e.g.* Hintikka & Kulas (1983), Hintikka (1988, 1996, 2000, 2006a)[^hintikka-1988][^hintikka-1996][^hintikka-2000][^hintikka-2006a][^hintikka-1996-2].

[^note-51]: See *e.g.* Hintikka & Kulas (1983), Hintikka (1988, 1996, 2000)[^hintikka-1988][^hintikka-1996][^hintikka-2000][^hintikka-1996-2].

[^note-52]: See *e.g.* Hintikka & Kulas (1983), Hintikka (1988, 1996, 2000)[^hintikka-1988][^hintikka-1996][^hintikka-2000][^hintikka-1996-2], Hintikka & Sandu (1997).

[^note-53]: See *e.g.* Hintikka & Kulas (1983), Hintikka (1988, 1995, 1996)[^hintikka-1988][^hintikka-1995][^hintikka-1996][^hintikka-1996-2].

[^note-54]: Barwise (1979)[^barwise-1979] suggested that a compositional semantics must satisfy the condition that the relation ‘$M \vDash \phi$’ be an inductive verifiability relation in the sense of Barwise & Moschovakis (1978). He proved that $\mathbf{FPO}$ does not admit of a compositional semantics subject to this condition. Hodges (1997a)[^hodges-1997a] finds the condition suggested by Barwise unmotivated. It rather begs the question: in order for a relation to be an inductive verifiability relation, the relevant inductive clauses must be first-order. That they cannot be first-order in connection with $\mathbf{FPO}$ is hardly surprising; cf. Hodges (2007: 118)[^hodges-2007]. Hintikka had on many occasions stated that there is no realistic hope of formulating compositional truth-conditions for $\mathbf{IFL}$ sentences (Hintikka 1991, 1995, 1996; see also Hintikka & Sandu 1997)[^hintikka-1991][^hintikka-1995][^hintikka-1996][^hintikka-1997][^hintikka-1997-2][^hintikka-1991-2][^hintikka-1996-2][^hintikka-1997-3]. Hodges (1997a,b) wanted to prove Hintikka’s statement wrong. The syntax Hodges opted for is that of slash logic (cf. *Sect*. 3 and *Subsect*. 6.1). Since Hodges considers variants of slash logic, his results are not, strictly speaking, about $\mathbf{IFL}$. However, it is clear that the framework of Hodges (1997b)[^hodges-1997b] can be adapted to the syntax of $\mathbf{IFL}$ proper.

[^note-55]: It was pointed out already in Hintikka & Kulas (1983: 20) that at least in some cases compositionality can be restored by resorting to higher-order entities, specifically to functions embodying strategies of player 2. In the same connection it was noted that such higher-order entities are much less realistic philosophically and psycholinguistically than the original individuals. See also Zadrozny (1995), Janssen (1997)[^janssen-1997], Hodges (1998)[^hodges-1998]; cf. Westerståhl (1998)[^westerståhl-1998], Sandu & Hintikka (2001)[^hintikka-2001].

[^note-56]: Note that $(N, \TRUE^N)$ is an expansion of $N$ to the vocabulary $\tau \cup \{\TRUE\}$. For the notion of expansion, see [the supplementary document](logic-if.supplement.md).

[^note-57]: For details about truth-definitions of $\mathbf{FO}$, see the entry on Tarski’s truth definitions; further, see e.g., Kaye (1991)[^kaye-1991], Sandu (1998)[^sandu-1998], Väänänen (2007)[^väänänen-2007].

[^note-58]: The proof of this result is sketched in Hintikka (1991, 1996)[^hintikka-1991][^hintikka-1996][^hintikka-1991-2][^hintikka-1996-2], and later in more detail in Sandu (1998)[^sandu-1998]. See also Hintikka (1998, 2001)[^hintikka-1998][^hintikka-2001], Hyttinen & Sandu (2000), Sandu & Hyttinen (2001), Väänänen (2007)[^väänänen-2007]. For a technically analogous result, see Hodges’s comments about self-applied truth-predicates for $\Sigma_n$ formulas in Azriel Levy’s set-theoretical hierarchy (the entry on Tarski’s truth definitions); see also de Rouilhan and Bozon’s (2006: 700) comments about John Myhill’s and Craig Smorynski’s similar results.

[^note-59]: If one attempts to construct Liar’s paradox for $\mathbf{IFL}$, the assertion that the Liar sentence is true will itself be non-determined (Hintikka 1991: 44–51, 1996: 142; cf. Väänänen 2007: 108–109)[^hintikka-1991][^hintikka-1996][^hintikka-1991-2][^hintikka-1996-2][^väänänen-2007].

[^note-60]: See also Hintikka (1996: 106–108; 2001: 23–24; 2006a: 65–66).

[^note-61]: See Hintikka (1996: 123–125; 2001), Hintikka & Sandu (1997).

[^note-62]: Enderton (1970)[^enderton-1970] proved that the logic $L^*$ obtained from $\mathbf{FO}$ by closing it under arbitrary Henkin quantifiers, as well as under the operations $\neg , \wedge$, and $\vee$, can be translated into the so-called $\Delta^1_2$ fragment of second-order logic. (For this fragment, see, *e.g.*, Hinman 1978.)[^hinman-1978] Marcin Mostowski (1991)[^mostowski-1991] showed that in fact $L^*$ does not suffice to cover $\Delta^1_2$; cf. Krynicki & Mostowski (1995: 217). Now, (1) $\mathbf{EIFL}$ has the same expressive power as the Boolean closure of $\mathbf{ESO}$ (*i.e.*, its closure under $\neg , \wedge$, and $\vee)$, (2) the Boolean closure of $\mathbf{ESO}$ has the same expressive power as the Boolean closure of $\mathbf{FPO}$, and (3) the Boolean closure of $\mathbf{FPO}$ is a fragment of $L^*$. Therefore we may conclude that $\mathbf{EIFL}$ is strictly weaker than the $\Delta^1_2$ fragment of second-order logic.

[^note-63]: The standard interpretation in the sense of Henkin (1950)[^henkin-1950] construes second-order quantifiers as follows. If $R$ is an $n$-ary relation symbol, $f$ is an $n$-ary function symbol, and $\rM$ is a domain, then under the standard interpretation of second-order logic, the second-order quantifiers $(\exists R)$ and $(\forall R)$ range over all (extensionally possible) subsets of $\rM^n$, and the second-order quantifiers $(\exists f)$ and $(\forall f)$ range over all (extensionally possible) functions from $\rM^n$ to $\rM$.

[^note-64]: Similar requirements need be expressed concerning eventual second-order quantifiers $(\exists f)$.

[^note-65]: See Hintikka (1955; 1991: 47–48; 1995: 12–13; 2006a: 476–477), and especially Hintikka (1996: 194–195)[^hintikka-1996][^hintikka-1996-2]. For details about the reduction of the validity problem of full second-order logic to that of $\mathbf{ESO}$, see *e.g.* Leivant (1994: *Subsect.* 5.6).

[^note-66]: For an algebraic study of slash logic, see Mann (2007)[^mann-2007].

[^note-67]: For the relation of Jónsson and Tarski’s Theorem 3.14 to modal logic, cf. the entry on Arthur Prior.

[^note-68]: For these observations relating the propositional part of $\mathbf{EIFL}$, the modal logic $\mathbf{S4}$, and intuitionistic propositional logic, see Hintikka (2004b; 2006a: 471)[^hintikka-2004b][^hintikka-2006a].

[^note-69]: See Hintikka (1991; 1995; 1996: 129,190,198,201,205; 2000: 133; 2002a: 409; 2006a: 472). It may be of interest to note that Quine (1970: 90)[^quine-1970] affirms without hesitation that $\mathbf{FPO}$ formulas are not ontologically committed to higher-order entities (even if their expressive power goes beyond $\mathbf{FO})$. On the same basis Quine would, no doubt, have accepted that $\mathbf{IFL}$ is only committed to first-order entities. (Quine’s reasons for not considering $\mathbf{FPO}$ as a logic were related to its non-axiomatizability; cf. *Subsect*. 4.3.) For ontological commitments of $\mathbf{FPO}$ formulas, see also Patton (1991)[^patton-1991]. For the status of $\mathbf{FPO}$ as a first-order logic, cf. Hintikka & Kulas (1983: 50).

[^note-70]: See the entry on generalized quantifiers.

[^note-71]: For, in a play of the semantic game for the formula $Q_{\ge \kappa}z P(z)$ and the model $M$, player 2 would choose a function $f : \kappa \rightarrow$ M, whereafter player 1 would choose ordinals *α* and *β* with $\alpha \lt \beta \lt \kappa$. Player 2 would win iff $f(\alpha) \ne f(\beta)$ and the individuals $f(\alpha)$ and $f(\beta)$ satisfy the predicate $P$. (In order to win, player 2 must select an injective function whose all values satisfy $P$.)

[^note-72]: Cf. *Subsect.* 4.6. For details, see *e.g.* Leivant (1994: *Subsect.* 5.6).

[^note-73]: Both sets are $\Pi_2$ complete; for $\Pi_2$ completeness, see *e.g.* Väänänen (2007; *Ch.* 7).

[^note-74]: Cf. Feferman (2006: 461,463), Hintikka (1996: 129,193,198).

[^note-75]: Cf., *e.g.*, Hintikka (1991; 1995; 2002: 407; 2006a: 40–41).

[^note-76]: Together with witnesses for disjunction symbols, likewise depending in general on the values chosen for the preceding universal quantifiers.

[^note-77]: For the argument, see Hintikka (1996; 1998; 2004a; 2006a: 74)[^hintikka-1996][^hintikka-1998][^hintikka-2004a][^hintikka-2006a][^hintikka-1996-2].

[^note-78]: For *limited* formal truth definitions for set theory, see the entry on Tarski’s truth definitions.

[^note-79]: These individuals are ‘sets’ only in the sense that they belong to a domain of a model of an axiomatic *set* theory; they are not sets in the sense in which the entities over which second-order quantifiers range are sets (namely sets of individuals of the domain considered).

[^note-80]: See *e.g.* Hintikka (1996: 172–177; 1998: 319–323, 326–32; 2006a: 74). For the continuum hypothesis, and Gödel’s and Cohen’s independence results, see the entry on set theory.

[^note-81]: See Hintikka (1991: 47–48; 1996: 192–193); see also Väänänen (2007: 139–141)[^väänänen-2007].

[^note-82]: See Hintikka (1986; 1993; 1996: 208–209)[^hintikka-1986][^hintikka-1993][^hintikka-1996][^hintikka-1996-2]. The axiom of completeness appears in the second edition (1903) of Hilbert (1898). Saying that a model $M$ is maximal requires, at least on the face of it, quantification over individuals (or sets) outside the domain of $M.$

[^note-83]: Actually, Hintikka sees it as a conceptual confusion to speak of ‘axiomatizations’ in connection with logic as well as mathematical theories. In the former case, when possible, an axiomatization is simply a recursive enumeration of validities of the logic considered. By contrast, one can view an axiomatization of a mathematical theory as a way of compressing all the truths (not logical truths or validities) about the subject matter of the theory into a finite or recursively enumerable set of axioms (Hintikka 1996: 1–4)[^hintikka-1996][^hintikka-1996-2].

[^note-84]: Quantifiers occurring in conjoint constituents, quantifiers occurring in different nested $of$ phrases, and relative clauses with several antecedents; see Hintikka (1973a, 1976a, 1979)[^hintikka-1973a][^hintikka-1976a][^hintikka-1979].

[^note-85]: For a discussion, see *e.g.* Peters & Westerståhl (2006: 66–72) and the literature referred to there.

[^note-86]: This is because the set of valid $\mathbf{FPO}$ sentences is not recursively enumerable. As Hintikka himself recognizes, to produce a rigorous argument, it would be necessary to show for an arbitrary $\mathbf{FPO}$ sentence $Q\phi$, not only that there is an English sentence that is naturally represented using the prefix $Q$, but also that the grammatical constructions used allow an English counterpart of *φ*: whether the formula $Q\phi$ can be translated to $\mathbf{FO}$ crucially depends on the matrix *φ*.

[^note-87]: The example is from Hintikka (1982)[^hintikka-1982]; in this paper Hintikka does not use the slash sign. By reference to Hintikka’s theory of the semantics of questions (Hintikka 1976b)[^hintikka-1976b], Carlson and ter Meulen (1979) called attention to wh-questions formed out of suitable sentences with a branching quantifier reading, and argued that the desideratum of such a question will involve informational independence of the usual quantifiers from the intensional *know*-construction.

[^note-88]: In epistemic logic, the knowledge operator $K_a$ is construed as a universal modal operator ranging over scenarios compatible with the knowledge of the agent $a$ considered. For further information, see the entry on epistemic logic.

[^note-89]: The impossibility to express the condition $K_I (\forall x)(\exists y/K_I)$ admires$(x, y)$ in $\mathbf{FPO}$ is pointed out in both Carlson & ter Meulen (1979) and Hintikka (1982)[^hintikka-1982]. Here the existential quantifier depends on the universal quantifier but not on the knowledge operator, while the knowledge operator must precede the universal quantifier in order for the formula to imply the presupposed *de dicto* sentence ‘I know that everybody admires someone.’ According to the formula $(\forall x) K_I (\exists y/K_I)$ admires$(x, y)$, the agent’s knowledge would pertain to all *actual* individuals and it would merely imply that the agent knows of all actually existing individuals that each of them admires someone. If it is compatible with the agent’s knowledge that there are further individuals beside those which happen to exist actually, this would not guarantee the truth of the *de dicto* sentence.

[^note-90]: Cf. Hintikka (1982, 1987, 1990)[^hintikka-1982][^hintikka-1987][^hintikka-1990], Engdahl (1986)[^engdahl-1986]. For the uses of Skolem functions and related ideas in linguistics – notably the so-called *choice functions* – see *e.g.* Reinhart (1997)[^reinhart-1997], von Heusinger (2004)[^heusinger-2004], Steedman (2012)[^steedman-2012]. In logical terms, a choice function is a function taking a formula of one free variable as its argument and returning as its value an individual that satisfies this formula – if at least one such individual exists.

[^note-91]: In Hintikka & Sandu (1989: 575–576) it is said that informational independence is a relation between *applications of game rules*, but also that it is a relation that a *move prompted by an expression* in a semantic game bears to a number of earlier moves prompted by further expressions (cf. also Hintikka & Sandu 1997: 367)[^hintikka-1997][^hintikka-1997-2][^hintikka-1997-3]. The latter construal complies with the way informational independence is understood in game theory, while the former led to some confused examples in Hintikka and Sandu’s paper (examples about neg-raising, pp. 577–580, see also Hintikka 1990, Sandu 1993)[^hintikka-1990][^hintikka-1993][^sandu-1993].

[^note-92]: The belief operator $B_a$ is a universal modal operator, just like the knowledge operator $K_a$; its range is the set of scenarios compatible with all that the agent $a$ believes in the scenario relative to which the sentence is evaluated (cf. footnote 88).

[^note-93]: Cf. Hintikka & Sandu (1989: 584–585, 587–589), Hintikka (1990)[^hintikka-1990]. Some exceptions were noted in Hintikka (1973a)[^hintikka-1973a], cf. footnote 84. However, even when informational independence can be syntactically indicated, the indicators are different from case to case.

[^note-94]: Note that the slash-logical prefix $ (\forall x)(\exists u)(\forall y)(\exists v/x,u) $ can be expressed in IF logic simply by $ (\forall x)(\exists u)(\forall y)(\exists v/\forall x) $. By contrast, the identity symbol is needed to translate the slash-logical prefix $ (\forall u)(\exists v)(\exists w/u) $ into IF logic: a construction such as $ (\forall u)(\exists v)(\forall t)(\exists w/\forall u) (t=v \rightarrow \ldots)$ can be used.

[^auxier-2006]: Auxier, R. E. and Hahn, L. E. (eds.), 2006, *The Philosophy of Jaakko Hintikka*, (Library of Living Philosophers, Volume 30), Chicago: Open Court.

[^barbero-2013]: Barbero, F., 2013, “On Existential Declarations of Independence in IF Logic,” *Review of Symbolic Logic*, 6(2): 254–280.

[^barbero-2017]: –––, 2017, “Cooperation in Games and Epistemic Readings of Independence-Friendly Sentences,” *Journal of Logic, Language, and Information*, 26(3): 221–260.

[^barbero-2021]: –––, 2021, “Complexity of Syntactical Tree Fragments of Independence-Friendly Logic,” *Annals of Pure and Applied Logic*, 172(1): article 102859 (43 pages).

[^barbero-2021-2]: Barbero, F., Hella, L., and Rönnholm, R., 2021, “Independence-Friendly Logic Without Henkin Quantification,” *Archive for Mathematical Logic*, 60: 547–597.

[^barwise-1979]: Barwise, J., 1979, “On Branching Quantifiers in English,” *Journal of Philosophical Logic*, 8: 47–80.

[^barwise-1978]: Barwise, J., and Moschovakis, Y. N., 1978, “Global Inductive Definability,” *Journal of Symbolic Logic*, 43(3): 521–534.

[^bazzoni-2015]: Bazzoni, A., 2015, “Hintikka on the Foundations of Mathematics: IF Logic and Uniformity Concepts,” *Journal of Philosophical Logic*, 44(5): 507–516.

[^benthem-2001]: van Benthem, J., and Doets, K., 2001, “Higher-Order Logic,” in *Handbook of Philosophical Logic*, (2nd edition, Vol. 1), D. M. Gabbay, and F. Guenthner (eds.), Berlin: Springer, pp. 189–244.

[^blass-1986]: Blass, A., and Gurevich, Y., 1986, “Henkin Quantifiers and Complete Problems,” *Annals of Pure and Applied Logic*, 32: 1–16.

[^brasoveanu-2011]: Brasoveanu, A., and Farkas, D. F., 2011, “How Indefinites Choose Their Scope,” *Linguistics and Philosophy*, 34(1): 1–55.

[^burgess-2003]: Burgess, J. P., 2003, “A Remark on Henkin Sentences and Their Contraries,” *Notre Dame Journal of Formal Logic*, 44: 185–188.

[^caicedo-2009]: Caicedo X., Dechesne, F., and Janssen, T. M. V., 2009, “Equivalence and Quantifier Rules for Logic with Imperfect Information,” *Logic Journal of the IGPL*, 17(1): 91–129.

[^cameron-2001]: Cameron, P., and Hodges, W., 2001, “Some Combinatorics of Imperfect Information,” *Journal of Symbolic Logic*, 66: 673–684.

[^carlson-1979]: Carlson, L., and Hintikka, J., 1979, “Conditionals, Generic Quantifiers, and Other Applications of Subgames,” in *Game-Theoretical Semantics*, E. Saarinen (ed.), Dordrecht: Reidel, pp. 179–214.

[^carlson-1979-2]: Carlson, L., and ter Meulen, A., 1979, “Informational Independence in Intensional Contexts,” in *Essays in Honour of Jaakko Hintikka*, E. Saarinen, I. Niiniluoto, R. Hilpinen, and M. Provence (eds.), Dordrecht: Reidel, pp. 61–72.

[^clark-2012]: Clark, R., 2012, *Meaningful Games: Exploring Language with Game Theory*, Cambridge, MA: The MIT Press.

[^dechesne-2005]: Dechesne, F., 2005, *Game, Set, Math: Formal Investigations into Logic with Imperfect Information*, Ph.D. Thesis, Eindhoven: University of Tilburg.

[^ebbinghaus-1999]: Ebbinghaus, H.-D., and Flum, J., 1999, *Finite Model Theory*, Berlin: Springer, 2nd edition.

[^ebbinghaus-1994]: Ebbinghaus, H.-D., Flum, J., and Thomas, W., 1994, *Mathematical Logic*, New York: Springer, 2nd edition.

[^enderton-1970]: Enderton, H. B., 1970, “Finite Partially-Ordered Quantifiers,” *Zeitschrift für matematische Logik und Grundlagen der Mathematik*, 16: 393–397.

[^engdahl-1986]: Engdahl, E., 1986, *Constituent Questions: The Syntax and Semantics of Questions with Special Reference to Swedish*, Dordrecht: Reidel.

[^fagin-1974]: Fagin, R., 1974, “Generalized First-Order Spectra and Polynomial-Time Recognizable Sets,” in *Complexity of Computation*, (SIAM-AMS Proceedings, Volume 7), R. M. Karp (ed.), pp. 43–73.

[^feferman-2006]: Feferman, S., 2006, “What Kind of Logic is ‘Independence-Friendly’ Logic?,” in Auxier & Hahn (2006), pp. 453–469.

[^figueira-2009]: Figueira, S., Gorín, D., and Grimson, R., 2009, “On the Formal Semantics of IF-like Logics,” *Journal of Computer and System Sciences*, 76: 333–346.

[^figueira-2011]: –––, 2011, “On the Expressive Power of IF-Logic with Classical Negation” in *Logic, Language, Information, and Computation*, L. Beklemishev and R. de Queiroz (eds.), Berlin: Springer, pp. 135–145.

[^figueira-2014]: –––, 2014, “Independence Friendly Logic with Classical Negation via Flattening is a Second-Order Logic with Weak Dependencies,” *Journal of Computer and System Sciences*, 80: 1102–1118.

[^forster-2006]: Forster, T., 2006, “Deterministic and Nondeterministic Strategies for Hintikka Games in First-Order and Branching-Quantifier Logic,” *Logique et Analyse*, 195: 265–269.

[^fortnow-2009]: Fortnow, L., 2009, “The Status of the P versus NP Problem,” *Communications of the ACM*, 52(9): 78–86.

[^gödel-1930]: Gödel, K., 1930, “Die Vollständigkeit der Axiome des logisch Funktionenkalküls,” *Monatshefte für Mathematik und Physik*, 37: 349–360.

[^gödel-1933]: –––, 1933, “Eine Interpretation des intuitionistischen Aussagenkalkuls,” *Ergebnisse eines mathematischen Kolloquiums*, 4: 39–40.

[^gödel-1947]: –––, 1947, “What is Cantor’s Continuum Problem?,” *The American Mathematical Monthly*, 54: 515–525.

[^grädel-2007]: Grädel E., Kolaitis, P. G., Libkin, L., Marx, M., Spencer, J., Vardi, M. Y., Venema, Y., and Weinstein, S., 2007, *Finite Model Theory and Its Applications*, Berlin: Springer.

[^hella-1995]: Hella, L., and Sandu, G., 1995, “Partially Ordered Connectives and Finite Graphs,” in *Quantifiers: Logics, Models and Computation*, Vol. 2, M. Krynicki, M. Mostowski, and L. W. Szczerba (eds.), Dordrecht: Kluwer, pp. 79–88.

[^hella-2008]: Hella, L., Sevenster, M., and Tulenheimo, T., 2008, “Partially Ordered Connectives and Monadic Monotone Strict NP,” *Journal of Logic, Language and Information*, 17(3): 323–344.

[^henkin-1950]: Henkin, L., 1950, “Completeness in the Theory of Types,” *Journal of Symbolic Logic*, 15: 81–91.

[^henkin-1961]: –––, 1961, “Some Remarks on Infinitely Long Formulas,” in *Infinitistic Methods* (no ed. given), New York: Pergamon Press, pp. 167–183.

[^hilbert-1903]: Hilbert, D., 1903, *Grundlagen der Geometrie*, Leipzig: Teubner, 2nd edition. (1st edition: “Grundlagen der Geometrie,” in *Festschrift zur Feier der Enthüllung des Gauss-Weber-Denkmals in Göttingen* 3–92, Leipzig: Teubner, 1899.)

[^hinman-1978]: Hinman, P. G., 1978, *Recursion-Theoretic Hierarchies*, Berlin: Springer, 1978.

[^hintikka-1955]: Hintikka, J., 1955, “Reductions in the Theory of Types,” Acta Philosophica Fennica, 8, pp. 61–115.

[^hintikka-1968]: –––, 1968, “Language-Games for Quantifiers,” in *American Philosophical Quarterly Monograph Series 2: Studies in Logical Theory*, Oxford: Basil Blackwell, pp. 46–72; reprinted in Hintikka 1973b, *Ch.* III.

[^hintikka-1973a]: –––, 1973a, “Quantifiers vs. Quantification Theory,” *Dialectica*, 27: 329–358; reprinted in 1974 in *Linguistic Inquiry*, 5: 153–177.

[^hintikka-1973b]: –––, 1973b, *Logic, Language-Games and Information: Kantian Themes in the Philosophy of Logic*, Oxford: Clarendon Press.

[^hintikka-1976a]: –––, 1976a, “Quantifiers in Logic and Quantifiers in Natural Languages,” in *Philosophy of Logic*, S. Körner (ed.), Oxford: Basil Blackwell, pp. 208–232.

[^hintikka-1976b]: –––, 1976b, *The Semantics of Questions and the Questions of Semantics*, Acta Philosophica Fennica, 28(4).

[^hintikka-1979]: –––, 1979, “Quantifiers in Natural Languages: Some Logical Problems,” in *Game-Theoretical Semantics*, E. Saarinen (ed.), Dordrecht: Reidel, pp. 81–117.

[^hintikka-1982]: –––, 1982, “On Games, Questions, and Strange Quantifiers,” in *Philosophical Essays Dedicated to Lennart Åqvist on his Fiftieth Birthday*, T. Pauli (ed.), Department of Philosophy, Uppsala: University of Uppsala, pp. 159–169.

[^hintikka-1986]: –––, 1986, “Extremality Assumptions in the Foundations of Mathematics,” *Proceedings of the Biennial Meeting of the Philosophy of Science Association 1986, Vol. 2*, pp. 247–252.

[^hintikka-1987]: –––, 1987, “Is Scope a Viable Concept in Semantics?,” in *ESCOL ‘86. Proceedings of the Third Eastern States Conference on Linguistics*, A. Miller, and Z.-S. Zhang (eds.), pp. 259–270.

[^hintikka-1988]: –––, 1988, “On the Development of the Model-Theoretic Viewpoint in Logical Theory,” *Synthese*, 77: 1–36.

[^hintikka-1990]: –––, 1990, “Paradigms for Language Theory” in *Language, Knowledge and Intentionality: Perspectives on the Philosophy of Jaakko Hintikka*, L. Haaparanta, M. Kusch, and I. Niiniluoto (eds.): Acta Philosophia Fennica, 49, pp. 181–209; reprinted in Hintikka, J., 1998, *Paradigms for Language Theory and Other Essays* (Jaakko Hintikka: Selected Papers, Volume 4), Dordrecht: Kluwer, pp. 146–174.

[^hintikka-1991]: –––, 1991, *Defining Truth, the Whole Truth and Nothing but the Truth*, Reports from the Department of Philosophy, no. 2, Helsinki: University of Helsinki; a revised version reprinted in Hintikka, J., 1997, *Lingua Universalis vs. Calculus Ratiocinator: An Ultimate Presupposition of Twentieth-Century Philosophy* (Jaakko Hintikka: Selected Papers, Volume 2), Dordrecht: Kluwer, pp. 46–103.

[^hintikka-1993]: –––, 1993, “New Foundations for Mathematical Theories,” in *Logic Colloquium ‘90*, *Lecture Notes in Logic* 2, J. Väänänen, and J. Oikkonen (eds.), Berlin: Springer, pp. 122–144; reprinted in Hintikka, J., 1998, *Language, Truth and Logic in Mathematics* (Jaakko Hintikka: Selected Papers, Volume 3), Dordrecht: Kluwer, pp. 225–247.

[^hintikka-1995]: –––, 1995, “What is Elementary Logic? Independence-Friendly Logic as the True Core Area of Logic,” in *Physics, Philosophy and the Scientific Community*, K. Gavroglu, J. J. Stachel, and M. W. Wartofsky (eds.), Dordrecht: Kluwer, pp. 301–326; page reference is to the reprint in Hintikka, J., 1998, *Language, Truth and Logic in Mathematics* (Jaakko Hintikka: Selected Papers, Volume 3), Dordrecht: Kluwer, 1998, pp. 1–26.

[^hintikka-1996]: –––, 1996, *The Principles of Mathematics Revisited*, Cambridge: Cambridge University Press.

[^hintikka-1997]: –––, 1997, “No Scope for Scope?,” *Linguistics and Philosophy*, 20: 515–544; reprinted in Hintikka, J., 1998, *Paradigms for Language Theory and Other Essays* (Jaakko Hintikka: Selected Papers, Volume 4), Dordrecht: Kluwer, pp. 22–51.

[^hintikka-1997-2]: –––, 1997, “A Revolution in the Foundations of Mathematics?,” *Synthese*, 111: 155–170; reprinted in Hintikka, J., 1998, *Language, Truth and Logic in Mathematics* (Jaakko Hintikka: Selected Papers, Volume 3), Dordrecht: Kluwer, pp. 45–61.

[^hintikka-1998]: –––, 1998, “Truth Definitions, Skolem Functions and Axiomatic Set Theory,” *Bulletin of Symbolic Logic*, 4: 303–337.

[^hintikka-1999]: –––, 1999, *Inquiry as Inquiry: A Logic of Scientific Discovery* (Jaakko Hintikka: Selected Papers, Volume 5), Dordrecht: Kluwer.

[^hintikka-2000]: –––, 2000, “Game-Theoretical Semantics as a Challenge to Proof Theory,” *Nordic Journal of Philosophical Logic*, 4(2): 127–141.

[^hintikka-2001]: –––, 2001, “Post-Tarskian Truth,” *Synthese*, 126: 17–36.

[^hintikka-2002a]: –––, 2002a, “Hyperclassical Logic (a.k.a. IF Logic) and its Implications for Logical Theory,” *Bulletin of Symbolic Logic*, 8: 404–423.

[^hintikka-2002b]: –––, 2002b, “Quantum Logic is a Fragment of Independence-Friendly Logic,” *Journal of Philosophical Logic*, 31: 197–209.

[^hintikka-2002c]: –––, 2002c, “Negation in Logic and in Natural Language,” *Linguistics and Philosophy*, 25: 585–600.

[^hintikka-2003]: –––, 2003, “A Second-Generation Epistemic Logic and Its General Significance,” in *Knowledge Contributors*, V. F. Hendricks, K. F. Jørgensen, and S. A. Pedersen (eds.), Dordrecht: Kluwer, pp. 33–55; reprinted in Hintikka, J., 2007, *Socratic Epistemology*, New York: Cambridge University Press, pp. 61–82.

[^hintikka-2004a]: –––, 2004a, “Independence-Friendly Logic and Axiomatic Set Theory,” *Annals of Pure and Applied Logic*, 126: 313–333.

[^hintikka-2004b]: –––, 2004b, “What is the True Algebra of Logic,” in *First-Order Logic Revisited*, V. F. Hendricks, F. Neuhaus, S. A. Pedersen, U. Scheffler, and H. Wansing (eds.), Berlin: Logos Verlag, pp. 117–128.

[^hintikka-2006a]: –––, 2006a, “Intellectual Autobiography” and Hintikka’s replies to the contributors in Auxier & Hahn (2006).

[^hintikka-2006b]: –––, 2006b, “Truth, Negation and Other Basic Notions of Logic” in *The Age of Alternative Logics*, J. van Benthem, G. Heinzmann, M. Rebuschi, and H. Visser (eds.), Berlin: Springer, pp. 195–219.

[^hintikka-2008]: –––, 2008, “IF Logic in a Wider Setting: Probability and Mutual Dependence,” in *Dialogues, Logics and Other Strange Things*, C. Dégremont, L. Keiff, and H. Rückert (eds.), London: College Publications, pp. 195–211.

[^hintikka-1983]: Hintikka, J., and Kulas, J., 1983, *The Game of Language: Studies in Game-Theoretical Semantics and Its Applications*, Dordrecht: Reidel.

[^hintikka-1985]: –––, 1985, *Anaphora and Definite Descriptions: Two Applications of Game-Theoretical Semantics*, Dordrecht: Reidel.

[^hintikka-1989]: Hintikka, J., and Sandu, G., 1989, “Informational Independence as a Semantical Phenomenon,” in *Logic, Methodology and Philosophy of Science*, Vol. 8, J. E. Fenstad, I. T. Frolov, and R. Hilpinen (eds.), Amsterdam: Elsevier, pp. 571–589; reprinted in Hintikka, J., 1998, *Paradigms for Language Theory and Other Essays* (Jaakko Hintikka: Selected Papers, Volume 4), Dordrecht: Kluwer, pp. 52–70.

[^hintikka-1991-2]: –––, 1991, *On the Methodology of Linguistics: A Case Study*, Oxford: Basic Blackwell.

[^hintikka-1996-2]: –––, 1996, “A Revolution in Logic?,” *Nordic Journal of Philosophical Logic*, 1(2): 169–183; reprinted in Hintikka, J., 1998, *Language, Truth and Logic in Mathematics* (Jaakko Hintikka: Selected Papers, Volume 3), Dordrecht: Kluwer, 1998, pp. 27–44.

[^hintikka-1997-3]: –––, 1997, “Game-Theoretical Semantics,” in *Handbook of Logic and Language*, J. van Benthem, and A. ter Meulen (eds.), Amsterdam: Elsevier, pp. 361–410.

[^hintikka-1999-2]: –––, 1999, “Tarski’s Guilty Secret: Compositionality,” in *Alfred Tarski and the Vienna Circle*, J. Wolenski, and E. Köhler (eds.), Dordrecht: Kluwer, pp. 217–230.

[^hodges-1983]: Hodges, W., 1983, “Elementary Predicate Logic,” in *Handbook of Philosophical Logic*, Vol. 1, D. M. Gabbay, and F. Guenthner (eds.), Dordrecht: Reidel, pp. 1–131.

[^hodges-1993]: –––, 1993, *Model Theory*, in *Encyclopedia of Mathematics and its Applications* (Volume 42), Cambridge: Cambridge University Press.

[^hodges-1997a]: –––, 1997a, “Compositional Semantics for a Language of Imperfect Information,” *Logic Journal of the IGPL*, 5: 539–563.

[^hodges-1997b]: –––, 1997b, “Some Strange Quantifiers,” in *Structures in Logic and Computer Science: A Selection of Essays in Honor of A. Ehrenfeucht*, (Lecture Notes in Computer Science, Volume 1261) J. Mycielski, G. Rozenberg, and A. Salomaa (eds.), London: Springer, pp. 51–65.

[^hodges-1998]: –––, 1998, “Compositionality Is Not the Problem,” *Logic and Logical Philosophy*, 6: 7–33.

[^hodges-2006]: –––, 2006, “The Logic of Quantifiers,” in Auxier & Hahn (2006), pp. 521–534.

[^hodges-2007]: –––, 2007, “Logics of Imperfect Information: Why Sets of Assignments?,” in *Interactive Logic*, J. van Benthem, D. M. Gabbay, and B. Löwe (eds.), Amsterdam: Amsterdam University Press, pp. 117–133.

[^hodges-2013]: –––, 2013, “Logic and Games,” in *The Stanford Encyclopedia of Philosophy* (Spring 2013 Edition), E. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/spr2013/entries/logic-games/](https://plato.stanford.edu/archives/spr2013/entries/logic-games/)>.

[^hyttinen-2000]: Hyttinen, T., and Sandu, G., 2000, “Henkin Quantifiers and the Definability of Truth,” *Journal of Philosophical Logic*, 29: 507–527.

[^janssen-1997]: Janssen, T. M. V., 1997, “Compositionality,” in *Handbook of Logic and Language*, J. van Benthem, and A. ter Meulen (eds.), Amsterdam: Elsevier, pp. 417–473.

[^janssen-2002]: –––, 2002, “Independent Choices and the Interpretation of IF Logic,” *Journal of Logic, Language and Information*, 11: 367–387.

[^janssen-2013]: –––, 2013, “Compositional Natural Language Semantics using Independence Friendly Logic or Dependence Logic,” *Studia Logica*, 101(2): 453–466.

[^janssen-2006]: Janssen, T. M. V., and Dechesne, F., 2006, “Signaling in IF-Games: A Tricky Business,” in *The Age of Alternative Logics*, J. van Benthem, G. Heinzmann, M. Rebuschi, and H. Visser (eds.), New York: Springer, pp. 221–241.

[^jónsson-1951]: Jónsson, B., and Tarski, A., 1951, “Boolean Algebras with Operators, Part I,” *American Journal of Mathematics*, 73: 891–939.

[^kaye-1991]: Kaye, R., 1991, *Models of Peano Arithmetic*, Oxford: Clarendon Press.

[^kontinen-2014]: Kontinen, J., Kuusisto, A., Lohmann, P., and Virtema, J. (eds.), 2014, “Complexity of Two-Variable Dependence Logic and IF-Logic,” *Information and Computation*, 239: 237–253.

[^kontinen-2013]: Kontinen, J., Väänänen, J., and Westerståhl, D. (eds.), 2013, *Dependence and Independence in Logic*, special issue of *Studia Logica*, 101(2).

[^krynicki-1993]: Krynicki, M., 1993, “Hierarchies of Partially Ordered Connectives and Quantifiers,” *Mathematical Logic Quarterly*, 39: 287–294.

[^krynicki-1979]: Krynicki, M., and Lachlan, A. H., 1979, “On the Semantics of the Henkin Quantifier,” *Journal of Symbolic Logic*, 44(2): 184–200.

[^krynicki-1995]: Krynicki, M., and Mostowski, M., 1995, “Henkin Quantifiers” in *Quantifiers: Logics, Models and Computation*, Vol. 1, M. Krynicki, M. Mostowski, and L. W. Szczerba (eds.), Dordrecht: Kluwer, pp. 193–262.

[^kuusisto-2013]: Kuusisto, A., 2013. “Expressivity of Imperfect Information Logics without Identity,” *Studia Logica*, 101(2): 237–265.

[^leivant-1994]: Leivant, D., 1994, “Higher Order Logic,” in *Handbook of Logic in Artificial Intelligence and Logic Programming*, Vol. 2, D. M. Gabbay, C. J. Hogger, J. A. Robinson, and J. H. Siekmann, (eds.), Oxford: Clarendon Press, pp. 229–321.

[^mann-2007]: Mann, A. L., 2007, *Independence-Friendly Cylindric Set Algebras*, Ph.D. thesis, University of Colorado at Boulder.

[^mann-2011]: Mann, A. L., Sandu, G., and Sevenster, M., 2011, *Independence-Friendly Logic: A Game-Theoretic Approach*, Cambridge: Cambridge University Press.

[^marion-2009]: Marion, M., 2009, “Why Play Logical Games?,” in *Games: Unifying Logic, Language and Philosophy*, O. Majer, A.-V. Pietarinen, and T. Tulenheimo (eds.), New York: Springer-Verlag, pp. 3–25.

[^mckinsey-1948]: McKinsey, J. C. C., and Tarski, A., 1948, “Some Theorems About the Sentential Calculi of Lewis and Heyting,” *Journal of Symbolic Logic*, 13(1): 1–15.

[^mostowski-1957]: Mostowski, A., 1957, “On a Generalization of Quantifiers,” *Fundamenta Mathematicae*, 44: 12–36.

[^mostowski-1991]: Mostowski, M., 1991, “Arithmetic with the Henkin Quantifier and its Generalizations,” in *Séminaire du Laboratoire Logique, Algorithmique et Informatique Clermontoise*, Vol. 2, F. Gaillard, and D. Richard (eds.), pp. 1–25.

[^odintsov-2018]: Odintsov, S., Speranski, S., and Shevchenko, I., 2018. “Hintikka’s Independence-Friendly Logic Meets Nelson’s Realizability,” *Studia Logica*, 106(3): 637–670.

[^papadimitriou-1994]: Papadimitriou, C. H., 1994, *Computational Complexity*, Reading, MA: Addison-Wesley.

[^patton-1991]: Patton, T. E., 1991, “On the Ontology of Branching Quantifiers,” *Journal of Philosophical Logic*, 20: 205–223.

[^peters-2006]: Peters, S., and Westerståhl, D., 2006, *Quantifiers in Language and Logic*, Oxford: Oxford University Press.

[^pietarinen-2001]: Pietarinen, A.-V., 2001, *Semantic Games in Logic and Language*, Ph.D. thesis, Helsinki: University of Helsinki.

[^quine-1970]: Quine, W. V. O., 1970, *Philosophy of Logic*, Englewood Cliffs, NJ: Prentice-Hall.

[^rebuschi-2011]: Rebuschi, M., and Tulenheimo, T., 2011, “Between *De Dicto* and *De Re*: *De Objecto* Attitudes,” *The Philosophical Quarterly*, 61(245): 828–838.

[^reinhart-1997]: Reinhart, T., 1997, “Quantifier Scope: How Labor is Divided between QR and Choice Functions,” *Linguistics and Philosophy*, 20: 335–397.

[^rouilhan-2006]: de Rouilhan, P., and Bozon, S., 2006, “The Truth of IF: Has Hintikka Really Exorcised Tarski’s Curse?,” in Auxier & Hahn (2006), pp. 683–705.

[^sandu-1991]: Sandu, G., 1991, *Studies in Game-Theoretical Logics and Semantics*, Ph.D. thesis, Helsinki: University of Helsinki. (Includes Hintikka & Sandu 1989; Sandu 1993, 1994; Sandu & Väänänen 1992.)

[^sandu-1993]: –––, 1993, “On the Logic of Informational Independence and its Applications,” *Journal of Philosophical Logic*, 22: 29–60.

[^sandu-1994]: –––, 1994, “Some Aspects of Negation in English,” *Synthese*, 99(3): 345–360.

[^sandu-1996]: –––, 1996, Appendix to Hintikka (1996), pp. 254–270.

[^sandu-1998]: –––, 1998, “IF-Logic and Truth-Definition,” *Journal of Philosophical Logic*, 27: 143–164.

[^sandu-2001]: –––, 2001, “Signalling in Languages with Imperfect Information,” *Synthese*, 127: 21–34.

[^sandu-2007]: –––, 2007, Appendix to *Les principes des mathématiques revisités*, French transl. of Hintikka (1996) by M. Rebuschi, Paris: Vrin, pp. 285–300. (The appendix is new and the translation of the book is based on Hintikka’s revision of Hintikka 1996.)

[^sandu-2013]: –––, 2013, “Probabilistic IF Logic,” in *Logic and Its Applications*, K. Lodaya (ed.), Heidelberg: Springer, pp. 69–79.

[^sandu-2014]: –––, 2014, “Truth and Probability in Game-Theoretical Semantics,” *Teorema: Revista Internacional de Filosofía*, 33(2): 151–170.

[^sandu-2001-2]: Sandu, G., and Hintikka, J., 2001, “Aspects of Compositionality,” *Journal of Logic, Language and Information*, 10: 49–61.

[^sandu-2001-3]: Sandu, G., and Hyttinen, T., 2001, “IF logic and The Foundations of Mathematics,” *Synthese*, 126: 37–47.

[^sandu-2010]: Sandu, G., and Sevenster, M., 2010, “Equilibrium Semantics of Languages of Imperfect Information,” *Annals of Pure and Applied Logic*, 161: 618–631.

[^sandu-1992]: Sandu, G., and Väänänen, J., 1992, “Partially Ordered Connectives,” *Zeitschrift für matematische Logik und Grundlagen der Mathematik*, 38: 361–372.

[^sevenster-2006]: Sevenster, M., 2006, *Branches of Imperfect Information: Logic, Games, and Computatation*, Ph.D. thesis, Amsterdam: University of Amsterdam.

[^sevenster-2014]: –––, 2014, “Dichotomy Result for Independence-Friendly Prefixes of Generalized Quantifiers,” *Journal of Symbolic Logic*, 79(4): 1224–1246.

[^skolem-1920]: Skolem, T., 1920, “Logisch-kombinatorische Untersuchungen über die Erfüllbarkeit oder Beweisbarkeit mathematischer Sätze nebst einem Theoreme über dichte Mengen,” *Skrifter utgit av Videnskabsselskapet i Kristiania, I. Matematisk-naturvidenskabelig klasse*, no. 4, pp. 1–36; reprinted in *T. Skolem*, *Selected Works in Logic*, J. E. Fenstad (ed.), Oslo: Universitetsforlaget, 1970, pp. 103–136.

[^steedman-2012]: Steedman, M., 2012, *Taking Scope. The Natural Semantics of Quantifiers*, Cambridge, MA: The MIT Press.

[^tarski-1933]: Tarski, A., 1933, “The Concept of Truth in the Languages of the Deductive Sciences” (Polish), *Prace Towarzystwa Naukowego Warszawskiego, Wydzial III Nauk Matematyczno-Fizycznych* 34, Warsaw; expanded English translation in Tarski 1983, pp. 152–278.

[^tarski-1983]: –––, 1983, *Logic, Semantics, Metamathematics: Papers from 1923 to 1938*, 2nd and revised edition, J. Corcoran (ed.), Indianapolis: Hackett Publishing Company.

[^trakhtenbrot-1950]: Trakhtenbrot, B., 1950, “Impossibility of an Algorithm for the Decision Problem in Finite Classes” (Russian), *Doklady Akademii Nauk SSSR*, 70: 569–572. (English translation: *American Mathematical Society*, *Translation Series 2*, 23, 1963, pp. 1–5.)

[^tulenheimo-2014]: Tulenheimo, T., 2014, “Classical Negation and Game-Theoretical Semantics,” *Notre Dame Journal of Formal Logic*, 55: 469–498.

[^väänänen-2001]: Väänänen, J., 2001, “Second-Order Logic and Foundations of Mathematics,” *Bulletin of Symbolic Logic*, 7: 504–520.

[^väänänen-2002]: –––, 2002, “On the Semantics of Informational Independence,” *Logic Journal of the IGPL*, 10(3): 337–350.

[^väänänen-2006]: –––, 2006, “A Remark on Nondeterminacy in IF Logic,” Acta Philosophica Fennica, 78, pp. 71–77.

[^väänänen-2007]: –––, 2007, *Dependence Logic: A New Approach to Independence Friendly Logic*, Cambridge: Cambridge University Press.

[^heusinger-2004]: von Heusinger, K., 2004, “Choice Functions and the Anaphoric Semantics of Definite NPs,” *Research on Language and Computation*, 2: 309–329.

[^walkoe-1970]: Walkoe, W. J. Jr., 1970, “Finite Partially-Ordered Quantification,” *Journal of Symbolic Logic*, 35: 535–555.

[^westerståhl-1998]: Westerståhl, D., 1998, “On Mathematical Proofs of the Vacuity of Compositionality,” *Linguistics and Philosophy*, 21: 635–643.

[^wittgenstein-1953]: Wittgenstein, L., 1953, *Philosophische Untersuchungen* (*Philosophical Investigations*), Oxford: Basil Blackwell, transl. by G. E. M. Anscombe.

[^zadrozny-1994]: Zadrozny, W., 1994, “From Compositional to Systematic Semantics,” *Linguistics and Philosophy*, 17: 329–342.
