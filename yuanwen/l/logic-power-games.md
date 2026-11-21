# Reasoning About Power in Games
**First published Wed Jun 14, 2017; substantive revision Mon Dec 4, 2023**

*Turrini, Paolo, Ågotnes, Thomas*

This entry discusses the use of mathematical languages to express and analyze the formal properties of power in games. The mathematical languages discussed in this entry will be referred to as **logics**, and classified according to their ability to express game-related concepts.

The material in this entry will be limited to the logical analysis of strategies and preferences of (groups of) individuals in cooperative and non-cooperative normal form games. It will not cover the use of game theory to study logical languages nor the role of epistemic concepts in strategic decisions. It will also not cover aspects of sequential decisions-making, typical of strategic reasoning in extensive games. An account of those can be found in the related entries logic and games, epistemic foundations of game theory (see also van Benthem, Pacuit, & Roy 2011 and van Benthem 2014)[^benthem-2014][^benthem-2011].

## 1. The Logic Underneath Games

A **game** is a mathematical description of the relation between a set of **individuals** (or groups of individuals) and a set of potential **outcomes**. Individuals choose, **independently and concurrently**, a subset of the outcomes, with the final outcome being selected from the combination of each choice. *Independently* means that individuals’ choices do not influence one another. *Concurrently* means that each individual’s choices are taken not knowing the other players’ choices. Each individual is assumed to have a preference over the set of outcomes, i.e., he or she likes some outcomes more than others, and typically assumed to know the other individuals’ potential choices and preferences, adjusting their decisions accordingly.

Games are used to model all sorts of situations, ranging from animal behavior to international conflict resolution (Osborne & Rubinstein 1994)[^osborne-1994]. A useful application for the purpose of this entry is collective decision-making, an instance of which is going to be the working example throughout.

**Example 1 (The treaty of Rome).** The treaty of Rome (1958–1973) established the European Economic Community. According to Article 148 of the Treaty, acts of the Council (one of the main legislative institutions) required for their adoption:

- 12 votes (if the act was proposed by the Commission), or
- 12 votes by at least 4 member states (if the act was not proposed by the Commission).

The values above refer to the EU-6, the founding member states. The treaty allocated the votes as follows:

- 4 votes: France, Germany, Italy;
- 2 votes: Belgium, The Netherlands;
- 1 vote: Luxembourg.

This scenario can be described as a game.

There are six players, the Countries: France, Germany, Italy, Belgium, The Netherlands and Luxembourg.

They vote on one issue at the time. Issues can be binary, e.g., the adoption of a border-protection scheme, or multi-valued, e.g., how many millions should be spent on the adoption of a border-protection scheme.

Countries might have *preferences* over the outcome of the vote or even over the other Countries’ specific vote, and they usually vote without *knowing* how the others have voted.

Often times, these games are such that no participant is, alone, capable of deciding the final outcome, but, in some cases, they could cooperate and agree on a *joint strategy*.

Depending on players’ preferences, knowledge and capabilities some outcomes will be more likely to be chosen. In order to understand which ones, game theory has devised solution concepts, formally functions from the set of games to the set of outcomes in each of these games, which describe players’ rationality in mathematical terms. Solution concepts, as we will see later, can be succinctly expressed in simple and well-behaved logics.

Next we describe games as mathematical structures, emphasizing various key ingredients (e.g., the possibility of forming coalitions, the possibility to take decisions in time etc.) and the best suited languages to express them.

## 2. The Basic Ingredients

Formally, games consist of a finite set of players $N=\{1,2, \ldots, n\}$ and a possibly infinite set of outcomes $W=\{w_1, w_2, \ldots, w_k, \ldots \}$.

**Example 2.** In the example above the set of players *N* is {France, Germany, Italy, Belgium, The Netherlands, Luxembourg}. If we consider the issue adoption of border-protection scheme, there are two outcomes: yes and no, i.e., $W = \{\mbox{yes, no}\}$. If we instead consider the issue millions spent on border-protection scheme there is a potentially infinite outcome space, i.e., $W = \{\textrm{0M}, \textrm{1M}, \textrm{2M}, \ldots \}$. It is possible to have a set of outcomes that is even refined further, for instance specifying the way players have voted. In this case the outcome in which France votes yes, the others vote no, and the result is no, would be different from the outcome in which Italy votes yes, the others vote no, and the result is no, although the result of the vote is the same. What is important to emphasize is that each set of outcomes comes with a *level of description* of what is happening in the underlying interaction. There is no a priori right or wrong level of description, the choice depends on the properties of the game that one is interested in.

On top of players and outcomes, games come with two more relations:

- a **preference relation**, denoted $\succeq$, describing players’ preferences over outcomes;
- an **action relation**, denoted $E$, describing the outcomes that players or groups of players are able to impose or, conversely, rule out;

An important relation in games is knowledge, which formally describes what players know of the game and their opponents. This relation is sometimes given explicitly, other times left implicit. The present entry will not make the relation explicit, but will rather incorporate it in the formalization of players’ rationality.

Both the preference and the action relations collect families of individual relations, one per player. The preference relation, for instance, is broken down into a family $\{\succeq_i\}_{i\in N}$, describing the preference over outcomes for each of the individuals, while the action relation collects a family $\{E_C\}_{C\subseteq N}$ each describing what a specific group of players can achieve.

Overall, a game can be seen as a mathematical structure

$$(\mathcal{N}, W, \succeq, E)$$

where $\mathcal{N}$ is the set of players, typically finite, $W$ the set of outcomes, $\succeq$ the preference relation and $E$ the action relation.

This mathematical structure is also known as a **relational structure** (Blackburn, Rijke, & Venema 2001)[^blackburn-2001], which (in a certain sense) is a set-theoretic equivalent of a so-called **modal logic** (Blackburn *et al*. 2001)[^blackburn-2001], a mathematical language that is well-suited to express the mathematical properties of relations. A relational structure will henceforth be denoted $F$, which stands for **frame**.

The last ingredient that we need, in order to link relational structures and modal logics, is the specification of a set of atomic propositions Atoms, which expresses the relevant properties of the outcomes we are interested in. This set is usually taken to be countable[^note-1] and is associated to outcomes by means of a **valuation function**, i.e., a function of the form

$$V: W \to 2^\texttt{Atoms}$$

associating to each outcome the set of propositional atoms that are true at that outcome.

A tuple $(F,V)$ will be referred to as **model**, which will be denoted $M$.

The relations in a game structure, which are relative to individual players (and groups), will formally be described in connection with the main modal logics used to express their properties, at different levels of description and granularity.

The following paragraph collects the background technical notions needed to interpret the modal languages used in this entry. The reader already acquainted with modal logic can skip it. For a more in depth exploration one can consult the related entry on modal logic. Well-known classic textbooks are *Modal Logic: An Introduction* (Chellas 1980)[^chellas-1980], which focuses on non-normal modal logics, and *Modal Logic* (Blackburn *et al*. 2001)[^blackburn-2001], which focuses instead on a more mathematical treatment of normal modal logics.[^note-2]

**Modal Logic: background notions:** The language of a **modal logic** is an extension of the language of propositional logic with a set of modal operators $\Box_1,\ldots , \Box_n, \ldots$, defined on a countable set of atomic propositions $\texttt{Atoms}=\{p_1,p_2, \ldots \}$, over which the set of *well-formed formulas* is inductively built (for a mathematical treatment of logic and induction see for instance Dalen 1980)[^dalen-1980]. Each well-formed formula *φ* of a modal language $\mathcal{L}$, henceforth simply called *formula*, is constructed using the following grammar:

$$\varphi ::= p \mid \lnot\varphi\mid\varphi \wedge \varphi \mid \Box_i \varphi$$

where $\Box_i \in \{\Box_1, \ldots, \Box_n, \ldots\}$ and $p \in \texttt{Atoms}$.

A model for this language is a structure $M = ((W, R_1, \ldots, R_n, \ldots), V)$, consisting of a set of **worlds** or **states** or **outcomes** $W$; an **accessibility relation** $R_i$ for each modal operator $\Box_i$which we here assume are so-called neighborhood functions (Chellas 1980)[^chellas-1980], i.e., functions $R_i: W \to 2^{2^{W}}$; and a **valuation function** $V: \texttt{Atoms} \to 2^{W}$, which assigns to each atomic proposition a subset of $W$, with the idea that each atomic proposition is assigned to the set of worlds at which this proposition is true.

As a general convention, a multimodal language with modalities $\Box_1$, …, $\Box_n$, … will be denoted by $\mathcal{L}^{f(\Box_1),\ldots, f(\Box_n),\ldots}$, where the function $f$ associates to each modality its intuitive shorthand. Let $\Delta$ be a modal language with modalities $\Box_1$, …, $\Box_n$, … and let $M = ((W, R_1, \ldots, R_n, \ldots), V )$ be a model for this language. The **satisfaction relation** of a formula $\varphi \in \Delta$ with respect to a pair $(M,w)$, where $w \in W$, is defined according to the following truth conditions:

$$\begin{align*} M,w&\models p &\mbox{ if and only if }& w \in V(p)\\ M,w&\models \neg\varphi &\mbox{ if and only if }& M,w\not\models\varphi \\ M,w&\models \varphi\land\psi &\mbox{ if and only if }& M,w\models\varphi \mbox{ and } M,w\models\psi \\ M,w&\models \Box_i \varphi &\mbox{ if and only if }& \varphi^M\in R_i(w) \\ \end{align*} $$

where $\varphi^{M}=\{w \in W \mid M,w \models \varphi\}$ is called the **truth set** or the **extension** of *φ*.

A formula *φ* of a modal language: **holds at a state** $w$ of model $M$ whenever $M,w \models \varphi$; is **valid in a model** $M$, denoted $\models_{M} \varphi$, if and only if $M,w \models \varphi$ for every $w \in W$, where $W$ is the domain of $M$; is **valid in a class of models** $\mathcal{M}$, denoted $\models_{\mathcal{M}} \varphi$, if and only if it is valid in every $M \in \mathcal{M}$; is **valid in a frame** ${F}$ (a model without a valuation function), denoted $\models_{{F}} \varphi$, if and only if for every valuation $V$ we have that $\models_{(F,V)} \varphi$; is **valid in a class of frames** $\mathcal{F}$, denoted $\models_{\mathcal{F}} \varphi$, if and only if it is valid in every $F \in \mathcal{F}$.

We can view a *modal logic* as the set of formulas $\Delta_{\mathcal{M}}$($\Delta_{\mathcal{F}}$) that are valid in a given class of models $\mathcal{M}$ (frames $\mathcal{F}$). For a set of formulas $\Sigma$, we write $M,w \models \Sigma$ to say that $M,w \models \sigma$, for all $\sigma\in \Sigma$. We say that a set of formulas (globally) **semantically entails** a formula *φ* in a class of models $\mathcal{M}$, denoted $\Sigma \models_{\mathcal{M}} \varphi$, if for every $M \in \mathcal{M}$we have that $\models_{M} \Sigma$ implies $\models_{M} \varphi$. When $\mathcal{F}$ is a class of frames, $\Sigma \models_{\mathcal{F}} \phi$ means that $\Sigma \models_{\mathcal{M}} \phi$ where $\mathcal{M}$ is the set of models based on frames in $\mathcal{F}$.

A modal rule

$$\frac{\varphi_1,\ldots ,\varphi_n }{\psi}$$

is **sound** in a class of models $\mathcal{M}$ if $\varphi_1,\ldots ,\varphi_n \models_{\mathcal{M}} \psi$.

Recall, following Chellas (1980)[^chellas-1980], that a modal logic $\Delta$ is called **classical** if it is closed under the rule of equivalence, i.e., for each $\Box$ in the language we have:

$$\frac{\varphi \leftrightarrow \psi}{\Box \varphi \leftrightarrow \Box \psi}$$

It is called **monotonic** if it is classical and it is moreover closed under the rule of monotonicity, i.e., for each $\Box$ in the language we have:

$$\frac{\varphi \rightarrow \psi}{\Box \varphi \rightarrow \Box \psi}$$

It is called **normal** if it is monotonic, it is closed under the rule of generalization and contains the $K$ axiom, i.e., for each $\Box$ we have

$$\frac{\varphi}{\Box \varphi}$$

and $\Delta$ contains all instances of $\Box(\varphi \to \psi) \to (\Box \varphi \to \Box \psi)$.

When $ R_i$ is a principal filter[^note-3], we say that we say that the modality $\Box_i$ is *normal*. In that case $R_i$can equivalently be represented as a relation of the form $R_i: W \to 2^{W}$, and then we have that $M,w \models \Box_i \phi$ if and only if $M,v \models \phi$ for all $v \in W$ such that $wR_iv$. A *normal modal logic* can be interpreted in structures of the form $M = ((W, R'_1, \ldots, R'_n, \ldots), V)$where every $R'_i$ is a principal filter.

### 2.1 Preferences

Recall the relational structure $(\mathcal{N},W, \succeq, E)$ and consider the relation $\succeq$. This relation compactly represents a family $\{\succeq_i\}_{i\in N}$ of individual preference relations each indexed with a player.

Formally, a **preference** for player $i$ is a relation

$$\succeq_i \subseteq W \times W$$

The idea is that if two outcomes $w$ and $w'$ are such that $(w,w')\in \succeq_i$ then player $i$ considers outcome $w$ at least as good as outcome $w'$. The fact that $(w,w')\in \succeq_i$ will be abbreviated $w \succeq_i w'$. Its inverse is the relation $\preceq_i$,which holds for $(w,w')$ whenever $w' \succeq_i w$. Its strict counterpart is the relation $\succ_i$, which holds for $(w,w')$ whenever $w \succeq_i w'$ and it is not the case that $w' \succeq_i w$. Moreover $w \sim_i w'$ denotes the fact that $w \succeq_i w'$ and $w' \succeq_i w$, meaning that $i$ is indifferent between $w$ and $w'$.

**Example 3.** Let us go back to our main example. Typically Countries have preferences over the outcome of the decision, e.g., Italy think we should spend between 5 and 10 million euros for the scheme, Germany think we should spend between 1 and 2, Belgium between 4 and 5, Luxembourg, The Netherlands and France exactly 5. This means, for instance, that Italy’s preference relation is such that $w \succ_{\textrm{Italy}} w'$ whenever $\textrm{5M} \leq w \leq \textrm{10M}$ and either $w'>\textrm{10M}$ or $0\leq w'<\textrm{5M}$. What about all other couples of outcomes? In the simplest case Italy are indifferent between them. So $w \sim_{\textrm{Italy}} w'$, otherwise. However, we could also assume a more complex preference. For instance, Italy would like to spend as much money as possible within their desired budget. In this case the preference relation is: $w \succ_{\textrm{Italy}} w'$ whenever $\textrm{5M} \leq w \leq \textrm{10M}$ and either $w'>\textrm{10M}$ or $0\leq w'<\textrm{5M}$, $w \succ_{\textrm{Italy}} w'$ whenever $\textrm{5M} \leq w' < w \leq \textrm{10M}$ while $w \sim_{\textrm{Italy}} w'$, otherwise. Not all outcomes of a vote are going to reach an agreement. We then, for technical purposes, define an auxiliary outcome $w^{*}$, interpreted as a disagreement outcome. The idea is that this is an outcome of the vote that does not reach any consensus. We assume that any agreement is strictly better for any player than disagreement, i.e., $w \succ_{{i}} w'$ whenever $w'=w^{*}$ and $w\neq w^{*}$, for each $i\in N$.

Properties of these relations can be expressed by means of modal logics. To do so we introduce modal operators $\Diamond^{\preceq}_i$, $\Diamond^{\prec}_i$ and $\Diamond^{\sim}_i$ for each of the corresponding relations, and we can view a relational structure as a modal logic frame with the relation $\preceq_i$ interpreting $\Diamond^{\preceq}_i$ and so on.

The interpretation in a model $M$ based on such a frame, for $R \in \{\preceq, \prec, \sim\}$, is then as follows (note that these modalities are normal):

$$ M,w \models \Diamond^{R}_i \varphi\enskip \mbox{ if and only if }\enskip M,w^{\prime} \models \varphi, \mbox{ for some } w^{\prime} \mbox{ with } w R_i w^{\prime}$$

The relations in question often come with extra properties. For instance, $\preceq_i$ is usually taken to satisfy the following:

- **reflexivity**: i.e., $\forall w\in W, i \in N,$ we have that: $w \preceq_i w$;
- **transitivity**: i.e., $\forall w_1, w_2, w_3 \in W, i \in N,$ we have that: ($w_1 \preceq_i w_2$ and $w_2 \preceq_i w_3$) implies that $w_1 \preceq_i w_3$.
- **connectedness**: i.e., $\forall w_1, w_2 \in W, i \in N,$ we have that: either $w_1 \preceq_1 w_2$ or $w_2 \preceq_i w_1$.

The first two properties can be characterized by means of the following axioms and validities.

**Proposition 1.** $$\begin{align*} \models_F \varphi &\rightarrow \Diamond^{\preceq}_i \varphi &\mbox{ if and only if }& \preceq_i \mbox{ is reflexive} \\ \models_F \Diamond^{\preceq}_i\Diamond^{\preceq}_i\varphi &\rightarrow \Diamond^{\preceq}_i \varphi &\mbox{ if and only if }& \preceq_i \mbox{ is transitive} \end{align*}$$

However this is not the case for connectedness, as modal languages such as this one can only talk about *local* properties of relations (Blackburn *et al*. 2001)[^blackburn-2001].

To characterize connectedness we need to introduce a special type of operator: the universal (or global) modality (Goranko & Passy 1992)[^goranko-1992]. This modality expresses properties of all the states in a domain $W$ of a model $M$ and it is interpreted as follows.

$$ M,w \models A\varphi \enskip\mbox{ if and only if }\enskip M,w^{\prime} \models \varphi, \mbox{ for all } w^{\prime} \in W$$

The formula $\neg A \neg \varphi$ will be abbreviated $E\varphi$. The symbol $E$ is the existential dual of $A$ and it indicates that a certain formula holds at some state in the model. With the global modality we have a genuine addition of expressivity (together with further costs and further gains, as shown in Goranko & Passy 1992)[^goranko-1992], therefore we can express validity in a model by means of expressing truth in a world, witness the fact that $M,w \models A \varphi$ holds if and only if $ \models_M \varphi$ does.

Recall that a relation $R$ is trichotomous if and only if for all $x,y\in W$ it is either the case that $xRy, yRx$ or $y=x$. We can use a combination of preference and global modalities to obtain the following frame correspondence.

**Proposition 2.** Let $F$ be a frame. We have that:

$\models_F (\varphi \wedge \Box^{\preceq}_i \psi) \to A(\psi \vee \varphi \vee \Diamond^{\preceq}_i \varphi)$ if and only if $\preceq_i$ is trichotomous

An alternative and possibly more intuitive formula that can be used instead is, for $p,q$ being atomic propositions:

$$E p \land E q \to E(p \land q) \lor E(p \land \Diamond^{\preceq}_i q) \lor E(q \land \Diamond^{\preceq}_i p)$$

Trichotomy, transitivity and reflexivity of $\preceq_i$ are equivalent to the relation being a weak linear order, and thus being connected.

The relation $\prec_i$, i.e., the relation of strict preference, can be defined in terms of $\preceq_i$. But $\prec_i$ satisfies the following property:

- **irreflexivity**: i.e., $\forall w\in W, i \in N,$ we have that: it is not the case that $w \prec_i w$;

Irreflexivity is not definable in basic modal logic (Blackburn *et al*. 2001)[^blackburn-2001]. However if the atomic propositions are powerful enough to tell each outcome apart, then irreflexivity becomes definable. For instance let $w_k$ be a variable identifying world $w_k$.[^note-4] We have the following.

**Proposition 3.** $$\models_F w_k \to \neg \Diamond^\prec_i w_k \enskip\mbox{ if and only if }\enskip \prec_i \mbox{ is irreflexive} $$

Finally, the indifference relation $\sim$ satisfies the properties of reflexivity, transitivity and symmetry. While reflexivity and transitivity are defined analogously to the previous modalities, symmetry is defined as follows.

- **symmetry**: i.e., $\forall w_1, w_2 \in W, i \in N,$ we have that: $w_1 \sim_i w_2$ implies that $w_2 \sim_i w_1$.

While the axioms for the first two are similar to the ones for $\preceq_i$, symmetry is characterized as follows

**Proposition 4.** $$\models_F (\psi \to \Box^{\sim}_i \Diamond^{\sim}_i\psi) \enskip\mbox{ if and only if }\enskip \sim_i \mbox{ is symmetric} $$

The three properties above say, together, that each $\sim_i$ is mathematically an **equivalence relation**, i.e., a relation such that

$$\bigcup_{w \in W} \{[w] \mid w' \in [w] \mbox{ whenever } w \sim_i w' \}$$

is a partition of $W$. Each element of this partition is an **indifference class** for player $i$, i.e., a set of outcomes he or she is indifferent to.

The logic of equivalence relations, such as $\sim_i$, is also known as the ${\bf S5}$ system.

**Preferences and utilities**: Because of their widespread use in game theory, an important class of preference relations are those that *correspond* to numerical values, or utility functions.

A **utility function** is a function

$$u_i: W \rightarrow \mathbb{R}$$

mapping outcomes to real numbers, representing *how much* a player values a certain state.

Utility functions naturally induce preference relations, in the following sense.

**Definition 5.** Let $u$ be a utility function. We say that $\succeq^*_i$ **corresponds to** $u$ if the following holds:

$$w \succeq^*_i w' \enskip\textrm{ if and only if }\enskip u_i(w) \geq u_i(w')$$

Notice how every weak linear order over a finite set of outcomes corresponds to some utility function.

We refer to the related entries on preferences and decision-theory for a more detailed analysis on the role of preferences in philosophy and decision theory.

### 2.2 Choices

A game is also a description of what players can achieve, on their own or within coalitions. To formalize this we use effectivity functions, an abstract model of power introduced to study voting strategies in committees (Moulin & Peleg 1982)[^moulin-1982].

An **effectivity function** (Moulin & Peleg 1982)[^moulin-1982] is a function

$$E:2^{N} \to 2^{2^{W}}$$

associating to each group of players a set of sets of outcomes.

The idea is that, whenever it is the case that $X\in E(C)$, then coalition $C$ is able to decide that the outcome of the game lies inside the set $X$, and can therefore rule out the outcomes $W \setminus X$ from being eventually chosen. In other words $X$ is *within the power* of coalition $C$.

Effectivity functions of games are **closed under supersets**, i.e., we have that $X\in E(C)$ and $X\subseteq Y \subseteq W$ imply that $Y \in E(C)$. In other words, if $X$ is within the power of coalition $C$ then so is each of $X$’s supersets. From this, notice, it follows that if an effectivity function of a certain coalition is not empty then it always contains the set of all outcomes. For $\mathcal{X} \subseteq {2^{W}}$ we denote $\mathcal{X}^{+}$ its superset closure.

**Example 4.** Going back to the main example, consider the power of each individual country. Because of the rules of the game, no country is alone in position to rule out any outcome.

Resorting to effectivity functions: for each $i\in N$, we have that $E(\{i\}) = \{W\}$.

This is however also the case for coalitions that are not big enough. For instance, take all coalitions of at least two Countries that can be formed between The Netherlands, Belgium and Luxembourg.

$$\begin{align*} E(\{\mbox{Luxembourg, Belgium}\}) &= \\ E(\{\mbox{Luxembourg, The Netherlands}\}) &= \\ E(\{\mbox{Belgium, The Netherlands}\}) &= \\ E(\{\mbox{Luxembourg, Belgium, The Netherlands}\}) &= \{W\}. \end{align*} $$

Because their total weight sums to at most to 5 votes, they are not, on their own, able to settle for or rule out any possible agreement. In fact, for acts proposed by the Commission, each coalition $C$ whose voting weight is not at least 12 has the same effectivity function $E(C) = \{W\}$.

For the other coalitions, the situation is different. Consider for instance the coalition made by France, Germany and Italy, which, together, have a voting weight of 12. For them we have that:

$$E(\{\textrm{France, Germany, Italy}\}) = \{\{w\} \mid w \in W\}^{+}$$

This means that the three members can, on their own, decide the outcome of the vote. This is true for every coalition of voting weight 12 or more.

What about the acts not proposed by the Commission? For them let us use a different effectivity function, which we label $E^{*}$.

In this case the winning coalition has to consist of at least four members.

So $E^{*}(\{\mbox{France, Germany, Italy}\}) = \{W\}$ while $E^{*}(\{$France, Germany, Belgium, The Netherlands$\}) = \{\{w\} \mid w \in W\}^{+}$.

In general, it holds that $E(C)=E^{*}(C)$ whenever $|C|\geq 4$. Because of the properties of the voting game, we also have that $E(C)=E^{*}(C)$ whenever $|C|\leq 2$. The difference is made by coalitions of size 3: with $E^{*}$, they can never achieve more than $\{W\}$, while with $E$ they can achieve $\{\{w\} \mid w \in W\}^{+}$, if their voting power is at least 12. Notice that Luxembourg is irrelevant when it comes to bills proposed by the Commission, i.e., $E(C) = E(C \cup \textrm{ Luxembourg})$. This is not the case for the other bills, as we have observed.

Properties of effectivity functions can be expressed in modal logic. To do so it is important to observe that a *dynamic* effectivity function, essentially an effectivity function in each state of the model, corresponds to a (non-normal) relation in a relational structure. So what effectivity functions do is to induce a special kind of neighborhood structure, which we refer to as *Coalition Model*.

**Definition 6 [Coalition Models].** A *Coalition Model* is a triple $(W,E, V)$ where:

- $W$ is a nonempty set of states;
- $E: W \longrightarrow (2^{N} \longrightarrow 2^{2^W})$ is a *dynamic* effectivity function;
- $V: W \longrightarrow 2^{\texttt{Atoms}}$ is a valuation function.

A *coalition frame* is a model without the valuation function. Coalition models are, of course, relational game structures in disguise. As the reader will notice, dynamic effectivity functions allow each state to possibly have different power distributions among coalitions. This is *strictu sensu* irrelevant for the treatment of power in games (Section 3), where the effectivity functions associated to outcomes could as well be taken to be equivalent everywhere in the model, but the model is general enough to treat extensive and repeated interaction, where the sequential structure of the interaction is defined explicitly. We will usually abbreviate $E(w)(C)$ as $E_w(C)$ or even $E(C)$ when clear from the context.

The language used to talk about Coalition Models is **Coalition Logic** (Pauly 2001)[^pauly-2001], a non-normal modal logic to express choices of groups of players. Coalition Logic is an extension of propositional logic with $|2^{N}|$ modalities of the form $[C]$, so a modal operator each indexed with a coalition.

The satisfaction relation of the formulas of the form $[C]\varphi$ with respect to a pair $M,w$ is defined as follows:

$$M,w\models [C]\varphi \enskip\textrm{if and only if}\enskip \varphi^M\in E_w(C) $$

where, $\varphi^M = \{w\in W \mid M,w\models\varphi\}$.

Intuitively $\varphi^M\in E_w(C)$ means that coalition $C$ is able to achieve property *φ*.

As closure under superset, or **outcome monotonicity**, is taken to be a property of all effectivity functions, the rule of monotonicity is valid in Coalition Logic, which is therefore a monotonic modal logic (Hansen 2003)[^hansen-2003].

The rule of monotonicity takes this form for each $C\subseteq N$:

$$\frac{\varphi \to \psi}{[C]\varphi \to [C]\psi}$$

Intuitively, if $C$ is able to achieve *φ* and we have that *φ* implies *ψ*, then $C$ is also able to achieve *ψ*.

**Mathematical properties of power** Apart from outcome monotonicity, many other properties can be deemed necessary to model coalitional power in games. For instance an effectivity function typically has the following properties:

- **liveness**: i.e., $\emptyset \not\in E(C)$, for each $C\subseteq N$;
- **safety**: i.e., $W \in E(C)$, for each $C\subseteq N$;
- **regularity**: i.e., $X \in E(C)$ implies that $\overline{X} \not\in E(\overline{C})$, for each $C\subseteq N, X \subseteq W$;
- ***N*-maximality**: i.e., $\overline{X} \in E(\emptyset)$ implies that ${X} \in E(N)$ and $X \subseteq W$;
- **superadditivity**: i.e., $X\in E(C)$ and $Y \in E(D)$ implies that $X\cap Y \in E(C \cup D)$, for each $C$, $D \subseteq N$, $C \cap D = \emptyset$, $X,Y \subseteq W$;
- **coalition monotonicity**: i.e., $X \in E(C)$ implies that $X \in E(D)$, for each $C\subseteq D \subseteq N$, $X \subseteq W$;
- **well-foundedness**: i.e., $X \in E(N)$ implies that $\{x\} \in E(N)$, for some $x \in X$, for each $X \subseteq W$.

An effectivity function is called **playable** (Pauly 2001)[^pauly-2001] if it has liveness, safety, *N*-maximality and superadditivity. It is called **truly playable** (Goranko, Jamroga, & Turrini 2013)[^goranko-2013] if it is playable and well-founded. Observe that if $W$ is finite, an effectivity function is playable if and only if it is truly playable (Goranko *et al*. 2013)[^goranko-2013].

True playability is a fundamental property of effectivity functions of games, and connects one-shot coalitional games to one-shot non-cooperative games, as will be clear later.

**Example 5.** The effectivity functions of our working example are all truly playable.

In neighborhood structures, relations between set-theoretical and logical properties are often immediate and standard correspondence results between class of frames and neighborhood functions (Chellas 1980)[^chellas-1980] can be automatically used for Coalition Logic.

Coalition Logic is in fact expressive enough to characterize all the constraints mentioned so far, except the last one.

**Proposition 7.** Let $F=(W,E)$ be a Coalition Frame, and $C,C^{\prime}, C''$ be coalitions, such that $C \cap C'=\emptyset$ and $C \subseteq C''$. The following results hold:

- $\models_F [C] \varphi \to \neg [\overline{C}]\neg \varphi$ if and only if $E$ is regular;
- $\models_F [C]\top$ if and only if $E$ has safety;
- $\models_F [C] \varphi \to [C'']\varphi$ if and only if $E$ is coalition monotonic;
- $\models_F \neg [C] \bot$ if and only if $E$ has liveness;
- $\models_F \neg [\emptyset] \neg \varphi \to [N]\varphi$ if and only if $E$ is *N*-maximal;
- $\models_F [C^{\prime}] \varphi \wedge [C]\psi \to [C^{\prime} \cup C](\varphi \wedge \psi)$ if and only if $E$ is superadditive;
- $\varphi \to \psi \models_F [C]\varphi \to [C]\psi$ if and only if $E$ is outcome monotonic.

In fact, the axioms and deduction rule above are, in addition to propositional logic, sound and complete with respect to the class of all models with playable effectivity functions. For proofs, consult Pauly 2001.

Correspondence results allow us to distinguish by modal means a number of classes of frames. However expressivity of the modal operators strongly limit the capacity of the language to discern classes of structures. To this extent the reader should notice that the logics of both playable and truly playable effectivity frames share the fact that $\models_F [\emptyset]\top$. However this proposition, whose interpretation is that for each $w\in W, \{W\} \in E_w(\emptyset)$, is not sufficient to make a formal distinction between $E_w(\emptyset)$ in the two different classes of effectivity functions.

Along these lines, the following result tells us that Coalition Logic is also strong enough to reason about (or, if you prefer, too weak to distinguish) truly playable effectivity functions.

**Theorem 8.** (Goranko *et al*. 2013)[^goranko-2013] Let $\mathcal{P}$ be the class of playable frames and $\mathcal{P}^{*}$ the class of truly playable ones. Then, for every formula of Coalition Logic *φ*

$$\models_\mathcal{P} \varphi \textrm{ if and only if } \models_{\mathcal{P}^{*}} \varphi$$

This follows from the fact that Playable Coalition Logic has the finite model property (Pauly 2001)[^pauly-2001] and, in finite models, playable effectivity functions are truly playable.[^note-5]

As pointed out earlier on, this entry will only mention how knowledge is implicit in game structures but will not delve into the study of epistemic preconditions of rational play. Related entries devoted to epistemic logic, dynamic epistemic logic, and in particular epistemic game theory explore in depth the role of knowledge in decision-making. A treatment of modal logics for games which focuses instead on the role of information is Hoek & Pauly 2006.

## 3. Analyzing Power

This section looks at games in which individuals or groups take their choices independently and concurrently, and, we stress once more, abstracting away from how the interaction evolves in time. It pays particular attention to the relation between players’ choices and preferences, mentioning the role of knowledge, and most importantly it deals with how to express solution concepts in a logical language.

The section first describes the general setting of cooperative games, then it considers the more restricted and possibly better-known class of non-cooperative games.

### 3.1 Cooperative Games and Their Logic

The description of the game given in a relational structure of the form $(\mathcal{N}, W, \succeq, E)$ is not enough to understand which exact outcome *will be* chosen in the end. For that we need a solution concept, i.e., a mapping that associates to a game a set of outcomes of that game (Abdou & Keiding 1991)[^abdou-1991]. We here consider the general setting of *cooperative* or *coalitional* games, where $E: W \rightarrow (2^N \rightarrow 2^{2^W})$is a (not necessarily playable) dynamic effectivity function (again, strictly speaking a dynamic effectivity function assigns a coalitional game to each state/outcome).

A number of solution concepts have been introduced for coalitional games (see for instance Osborne & Rubinstein 1994, and Apt 2009 (Other Internet Resources)). For the present purposes we are only going to discuss what is possibly the best-known: the core. The core is a collection of stable outcomes, i.e., outcomes for which no coalition exists whose members are both able and willing to deviate from it. It can be seen as the set of outcomes to which *there is no effective opposition* (Abdou & Keiding 1991)[^abdou-1991].

Formally, given a relational structure $F=(\mathcal{N}, W, \succeq, E)$, an outcome $w\in W$ is said to be **stable** (in $v$) if there is no coalition $C$ and set of outcomes $X\subseteq W$ such that both of the following conditions are satisfied:

1. $X \in E_v(C)$
2. $y \in X$ and $i\in C$ implies that $y \succ_i w$

In words, an outcome is stable if there is no group of individuals that can achieve an alternative that they all strictly prefer.

The **core** is the collection of all stable outcomes.

**Example 6.** Consider the outcome 1M, which is the only outcome that Germany reckons acceptable. Germany, as already observed, have an effectivity function of $E(\{\textrm{Germany}\})=\{W\}$ so, on their own, are not able to turn their preference into an outcome. However, together with other Countries, they are able to do so. Suppose their allies are Belgium, France and The Netherlands. Is 1M then a *good* outcome? If we look at the preferences of the other players in the coalition, i.e., Belgium, France, The Netherlands, we observe the following. Belgium had rather an outcome between 4M and 5M, France and The Netherlands exactly 5M. These Countries could get together and select 5M, which is an outcome that is acceptable to them. However the effectivity function of $\{$Belgium, France, The Netherlands$\}$ is $E(\{$Belgium, France, The Netherlands$\})=\{W\}$, which means that the three Countries are not enough to pass the 5M bill. But the coalition made by Belgium, France, Italy and The Netherlands would be. Notice moreover that 5M is one of Italy’s preferred outcomes. 5M is in fact the only stable outcome of the game: there is no coalition that is together willing and capable of deviating from it.

Modal logic can be used to represent the core, with $E_w(C)$interpreting $[C]$as before. Consider first the formula

$$p \rightarrow \bigvee_{C\subseteq N} [C]\left(\bigwedge_{i\in C}\Diamond^\succ_i p\right)$$

This says that if $p$ is true then members of some coalition can improve upon *some* $p$ world, which does not seem the right formula to express stability in logic. However we can prove the following results, which utilizes the correspondence between the formula and a specific class of frames.

Let $E$ be an (outcome monotonic) effectivity function and let $\succeq_i$ be a weak linear order. Then:

$$(F,V'), w \models p \rightarrow \bigvee_{C\subseteq N} [C]\left(\bigwedge_{i\in C}\Diamond^\succ_i p\right)$$

holds at $w$ for *every* $V'$ if and only there exists a $C\subseteq N$ and $X \in E_w(C)$ such that, for all $i\in C$, $x\in X$ we have that $x \succ_i w$.

So the formula holds at $w$ for every valuation if and only if $w$ does not belong to the core. Clearly, if the formula is false at an outcome and some valuation, then this means that the outcome does belong to the core.

Notice that, since effectivity functions are outcome monotonic, if we have that if $X \in E_w(C)$ and

$$X \subseteq \left(\bigwedge_{i\in C} \Diamond^\succ_i p\right)^{(F,V')},$$

then

$$\left(\bigwedge_{i\in C} \Diamond^\succ_i p\right)^{(F,V')} \in E_w(C).$$

Also notice that the result above allows for the case of

$$\emptyset=\left(\bigwedge_{i\in C}\Diamond^\succ_i p\right)^{M} \in E_w(C),$$

which might be counterintuitive. Requiring $E$ to have liveness takes care of this.

Notice also how we had to impose a universal quantification on the set of valuations. Without this explicit quantification, the formula would only hold for one specific model, which would not be an appropriate solution. If instead we are only interested in knowing whether *there exists* some outcome that is stable or, conversely, whether the core is empty, it is sufficient to require the formula above to be valid. This would amount to say that *no* outcome is stable, i.e., that the core is empty.

**Proposition 10.** Let $F$ be a frame with $E_w = E_v$for every $w,v \in W$. We have that

$$\models_F p \rightarrow \bigvee_{C\subseteq N} [C]\left(\bigwedge_{i\in C}\Diamond^\succ_i p\right)$$

if and only if no outcome in $F$ belongs to the core.

Again, liveness would take care of the trivial case in which

$$\left(\bigwedge_{i\in C}\Diamond^\succ_i p\right)^{(F,V)}=\emptyset.$$

An alternative approach is to identify each outcome with a name (or, in the language of hybrid logic, a *nominal*) in the language. Then we have the following.

**Proposition 11.** Let $w_k$ an atomic proposition be true at outcome $w_k$ and only at outcome $w_k$.

$$(F,V), w_k \models w_k \rightarrow \bigvee_{C\subseteq N} [C]\left(\bigwedge_{i\in C}\Diamond^\succ_i w_k\right)$$

if and only if $w_k$ does not belong to the core.

Yet another alternative is to have atoms for coalitional power (Ågotnes, van der Hoek and Wooldridge 2009)[^ågotnes-2009]: $(F,V), w \models p_C$ iff $w \in E_w(C)$. Then:

**Proposition 12.** Let $w_k$ an atomic proposition be true at outcome $w_k$ and only at outcome $w_k$.

$$((F,V), w \models \bigvee_{C \subseteq N} \diamond^\succ p_C$$

if and only if $w$ does not belong to the core in $E_w$.

Emptyness of the core of $E_w$can then furthermore be expressed using the universal modality $A$ from Section 2.1: $(F,V), w \models A(\bigvee_{C \subseteq N} \diamond^\succ p_C)$.

So depending on the properties we are interested in, different extensions of basic modal logic combined with different forms of validity (at a world vs model vs frame) are best-suited to express them.

### 3.2 Non-cooperative Games and Their Logic

Non-cooperative games are a representation of what individuals, rather than coalitions, can achieve, and what their preferences are.

Formally, a *strategic game form* is a tuple

$$(N, W, \{\Sigma_i\}_{i\in N}, o)$$

where *N* is a finite set of players, $W$ a set of outcomes, $\{\Sigma_i\}_{i\in N}$ a collection of strategies, one for each player $i$, $o: \prod_{i\in N} \Sigma_i \to W$ an outcome function, associating a tuple of strategies to an outcome.

A non-cooperative game is a tuple $(S,\{\succeq_i\}_{i\in N})$, where $S$ is a strategic game form and $\{\succeq_i\}_{i\in N}$ a collection of preference relations, one for each player $i$.

**Example 7.** If we think of the Countries in our previous example as individual players and their votes as individual strategies, we can model the Treaty of Rome game as a non-cooperative game, where each individual can vote an amount of money to dedicate to border protection and preferences are as above.

The outcome function will take care to associate to each individual player’s vote the final outcome of the collective decision, e.g., selecting an outcome voted by a set of Countries with voting weight of at least 12, or resulting in no decision if no consensus is reached.

For instance:

- France vote 0M
- Belgium vote 2M
- Italy vote 10M
- Germany vote 0M
- The Netherlands vote 0M
- Luxembourg vote 0M

This round results in no decision, because no outcome has collected voting weight of at least 12.

However, suppose that the second round is such that everyone but Belgium stick to their vote, and assume Belgium switches to voting 0M. Now 0M has an aggregate of 13, which means it is chosen as the final decision.

Looking at the unified treatment of our example, there seem to be relationship between non-cooperative games and cooperative games. This relationship can be specified formally.

Let us first consider what a group of players can do in a game. To do so we define the **α-effectivity function**, a mathematical description of coalitional strategies in a game in terms of the sets outcomes that they can force.

**Definition 12.** [*α*-effectivity function] Let $S$ be a non-cooperative game. We define the *α* effectivity function of $S$, $E^{\alpha}_S(C)$, where $\overline{C}$ is the complement of $C$:

$E^{\alpha}_S(C)= \{X\ \mid$ there exists $\sigma_C$ such that for all $\sigma'_{\overline{C}}$ we have that $o(\sigma_C,\sigma'_{\overline{C}})\in X \}$

Intuitively the *α*-effectivity function of $S$ collects, for every group of players, the set of outcomes that they can achieve by fixing a strategy of theirs, no matter how their opponents play.

The following result shows the relationship between strategies and effectivity functions.

**Theorem 13** (Goranko *et al*. 2013)[^goranko-2013]. An effectivity function is truly playable if and only if it is the *α*-effectivity function of some non-cooperative game.

This is a generalization of the result in Peleg 1998 for finite games, starting from models of non-cooperative games first defined in Pauly 2001. In a nutshell what these results imply is the following.

**Proposition 14.** Let $F$ be a relational game structure. Then $E_w$ is the *α*-effectivity function of some non-cooperative game, for each $w \in W$, if and only if the following formulas are valid in $F$ for disjoint $C,C^{\prime}$:

- $\varphi \to \psi \models_F [C]\varphi \to [C]\psi$
- $\models_F [C] \top$
- $\models_F \neg [C] \bot$
- $\models_F \neg [\emptyset] \varphi \to [N]\varphi$
- $\models_F [C^{\prime}] \varphi \wedge [C]\psi \to [C^{\prime} \cup C](\varphi \wedge \psi)$

In the same way we did for cooperative games, we can ask ourselves whether an outcome is stable, or rational, in a strategic situation.

**Nash equilibrium and definability** The main solution concept to analyze non-cooperative games is Nash equilibrium. Informally a Nash equilibrium is a collection of strategies, one per player, such that no player is interested to change his or her strategy, given the others stick to theirs. Formally, a strategy profile *σ* is a (pure strategy) **Nash equilibrium** if for all players $i\in N$ and for all $\sigma'_i\in \Sigma_i$ we have that

$$o(\sigma_i,\sigma_{-i}) \succeq_i o(\sigma'_i,\sigma_{-i})$$

**Example 8.** Consider the following vote

- France vote 5M
- Belgium vote 5M
- Italy vote 10M
- Germany vote 1M
- The Netherlands vote 5M
- Luxembourg vote 5M

In this game there is no consensus on any budget. The situation might look like a deadlock, as everyone has voted according to their preference. However the outcome is disagreement, which no player prefers to any agreement. The only way that players can converge to an agreement is that Italy change their vote to 5M. If this happens 5M is achieved as an outcome.

Notice that the modified game, in which Italy vote 5M is a Nash equilibrium.

Consider now a modification of the game above, in which Italy and The Netherlands vote 10M, while the others stick to their vote. Surprisingly, despite the disagreement, this is Nash equilibrium, because no player is simultaneously able to get to some agreement, although being willing to do so.

How to express Nash equilibria in logic? Recall how the formula

$$p\to \bigvee_{C\subseteq N} [C]\left(\bigwedge_{i\in C}\Diamond^\succ_i p\right)$$

holds at a frame $F$ if and only if the core is empty, and a hybrid logic extension can tell us whether a specific outcome belongs to the core. If $F$ is based on a truly playable effectivity function we already have a non-cooperative form game version of the core: an outcome such that no coalition is together able and willing to deviate from, *not taking into account* what the others do. However Nash Equilibrium fixes a profile of strategies, such that no player is able and willing to deviate from there. In other words it requires the notion of best response for a player with respect to a given profile.

Formalisms such as Coalition Logic are too weak to express Nash equilibria. However, they can express the fact that certain effectivity functions allow for the possibility of a Nash equilibrium. This is what in Hansen & Pauly 2002 is called Nash-consistent Coalition Logic. Nash Equilibrium is in fact not definable in basic modal logic (van Benthem *et al*. 2011)[^benthem-2011], but it can be done with a modality that *intersects* both the preference and the choice relations (van Benthem *et al*. 2011)[^benthem-2011] (for choice relations see Section 3.2.2 below).

$(F,V),w\models \langle \approx_i \cap \succ_i \rangle \varphi$ if and only if $w(\approx_i \cap \succ_i)w'$ implies that $w'\models \varphi $

Then the best response for $i$ is defined as $ \langle \approx_i \cap \succ_i \rangle \top$, as there is no alternative that is at the same time achievable and preferable to $i$. Alternatively a hybrid logic that mentions strategy profiles in the language can provide a solution, similarly to the case of the core.

#### 3.2.1 Injective Games and PDL with Intersection

The general definition of non-cooperative games given above allows games where two different strategy profiles lead to the same outcome, i.e., where $o(\sigma) = o(\sigma')$ for $\sigma \neq \sigma'$- where the outcome function is not *injective*. However in game theory injectivity is very often implicitly or explicitly assumed. Indeed, outcomes are often identified with strategy profiles.

It is thus a natural question what happens to Coalition Logic when we restrict non-cooperative games to be injective. The answer is that, first, not much: the language of Coalition Logic cannot discern between injective and non-injective games (Goranko *et al*. 2006)[^goranko-2006]. But, second, the class of effectivity functions changes: not all truly playable effectivity functions are *α*-effectivity functions of injective games.

Recall the *well-foundedness* property of effectivity functions: if $X \in E(N)$then $\{x\} \in E(N)$ for some $x \in X$. This is in fact equivalent (Goranko *et al*. 2013)[^goranko-2013] to the property that $E(\emptyset)$ has a *complete non-monotonic core*. The non-monotonic core $E^{nc}(C)$of $E(C)$ its minimal elements: $E^{nc}(C) = \{X \in E(C) : \neg \exists Y (Y \in E(C) \text{ and } Y \subset X\}$. The non-monotonic core is *complete* if and only if for every $X \in E(C)$ there is a $Y \in E^{nc}(C)$ such that $Y \subseteq X$. While true playability implies that the non-monotonic core for the empty coalition is complete, that is not the case for arbitrary coalitions.

It is, however, for injective games: in addition to the true playability properties, the *α*-effectivity functions of injective games have a complete non-monotonic core for *all coalitions*. In addition, the non-monotonic core has some structural properties. In more detail, we say that an effectivity function $E$ is *injectively playable* (Ågotnes and Alechina 2015)[^ågotnes-2015] iff it is truly playable and has the following additional properties, for all $C, i, j, X, Y$:

- $E(C)$ has a complete non-monotonic core;
- $E^{nc}(C) = \{\bigcap_{i \in C} X_i : X_i \in E^{nc}(\{i\})\}$ when $C \neq \emptyset$;
- if $X, Y \in E^{nc}(\{i\})$ and $X \neq Y$ then $X \cap Y = \emptyset$;
- if $X \in E^{nc}(j)$ and $x \in X$ then $\exists Y \in E^{nc}(i), x \in Y$.

It follows that $E(C)$ is completely determined by its non-monotonic core.

**Theorem 15.** (Ågotnes and Alechina 2015)[^ågotnes-2015] An effectivity function is injectively playable if and only if it is the *α*-effectivity function of some injective non-cooperative game.

*Intersection* plays a key role in the effectivity of coalitions in games: intuitively, the power of a coalition is the intersection of the power of the individuals in the coalition. A natural idea then, due to van Benthem 2012, is that coalitional power could perhaps be expressed by using *intersection* *modalities*. This is indeed the case, in the following precise sense (Ågotnes and Alechina 2015)[^ågotnes-2015]: there is a satsifiability preserving translation from Coalition Logic to Propositional Dynamic Logic with Intersection (Gargov *et al*. 1988)[^gargov-1988]. This translation relies on the fact that for every non-injective game there is a (Coalition Logic) equivalent injective game.

#### 3.2.2 Non-monotonic Action Logics

Some logics exploit a more compact representation of those relational structures that correspond to non-cooperative games.

Rather than using effectivity functions, each player $i$ is associated with an equivalence relation $\approx_i \subseteq W\times W$, whose induced partition represent the choices he or she can perform. These equivalence relations describe the exact set of choices that a group of players can perform and the originating models are referred to as *consequentialist* in the literature (see for instance Belnap, Perloff, & Ming 2001)[^belnap-2001].

Now define an effectivity function $E^{*}$ for which it holds that

$$E^{*}(i)= \{[x] \mid x' \in [x] \mbox{ whenever } x \approx_i x' \}^{+}$$

Intuitively $E^{*}(i)$ collects what *exactly* the individuals can achieve and all their supersets.

$E^{*}$ is called **consequentialist** if holds that:

- $E^{*}(C)= \{\bigcap_{i\in C} X_i \mid \mbox{for some } X_i \in E^{*}(i)\}$
- $\emptyset\not\in E^{*}(C)$ for each $C\neq N$
- $E^{*}(N) = \{\{x\} \mid x \in W\}^{+}$

Notice that $E^*$ is a truly playable effectivity function.

The last property is well-foundedness, as in the case of arbitrary effectivity functions. This is not a property that is assumed in all variants, e.g., the choice structures in Kooi & Tamminga 2008 and its temporal variant STIT (Belnap *et al*. 2001)[^belnap-2001] do not. However, as observed in Turrini 2012 and Tamminga 2013, well-founded consequentialist models correspond to non-cooperative games and the effectivity function $E$ can be effectively simulated by the equivalence relation $\approx_i$ for each player. Intuitively $E^{*}(i)$ is the set of sets of outcomes that $i$ can choose without being able to refine further.

To reason about consequentialist models, we use so-called consequentialist logics, i.e., propositional logic extended with modalities of the form $[C]\varphi$, interpreted as follows:

$M,w \models [C]\varphi$ if and only if $M,w'\models \varphi$ for all $w'$ such that $w (\bigcap_{i \in C} \approx_i)w'$

Consequentialist logics have been developed to reason about action and consequence, and have interesting applications in deontic logic, such as Kooi & Tamminga 2008; Tamminga 2013; Turrini 2012. They are moreover the basis of temporal logics of strategy such as STIT and strategic STIT, discussed later. A special case are the logics of propositional control (Hoek & Wooldridge 2005; Troquard, Hoek, & Wooldridge 2009)[^hoek-2005][^troquard-2009].

#### 3.2.3 Quantified and Higher-order Coalition Logic

Many interesting properties of power in games involve quantifying over coalitions, for example the notion of agent $i$ being a *weak veto player* (Wooldridge and Dunne 2004)[^dunne-2004][^wooldridge-2004] with respect to *φ*, in the sense that any coalition that can enforce *φ* must include $i$, or, in some first or higher-order extension of Coalition Logic: $\forall C ([C]\phi \rightarrow i \in C)$. *Quantified Coalition Logic (QCL)* (Ågotnes *et al*. 2008)[^ågotnes-2008] extends Coalition Logic with a limited form of quantification over coalitions, without making the resulting logic undecidable or indeed increasing the computational complexity of the satisfiability problem. In QCL coalitions inside modalities are replaced with coalition predicates. Intuitively, $[P]\phi$ ($\langle P \rangle \phi$) means that any (some) coalition satisfying the predicate $P$ has the ability to enforce *φ*. As an example, $i$ is a weak veto player for *φ*:

$$ \neg \langle \neg supseteq(\{i\})\rangle \phi $$

– it is not the case that any coalition that is not a superset of $\{i\}$ has the power to enforce *φ*. Or that $i$ is a *dictator* for *φ*: $\neg \langle \neg supseteq(\{i\})\rangle \phi \wedge [supseteq(\{i\})]\phi$*.* Such properties, and indeed all properties that can be expressed in QCL, can already be expressed in Coalition Logic, by using disjunction and conjunction to quantify over coalitions, but those expressions would typically be exponentially long in the number of agents. QCL can express such properties concisely, and indeed is exponentially more succinct than Coalition Logic. QCL can also be further extended with Belief-Intention-Desire (BDI) logic (Chen *et al*. 2014)[^chen-2014] without increasing complexity.

*Higher-order Coalition Logic (HCL)* (Boella *et al*. 2010)[^boella-2010] extends QCL with to a monadic second-order language, unifying the languages for describing coalitions and for describing their power and significantly extending the expressive power. Expressive tractable fragments of HCL exist (Doherty *et al*. 2011)[^doherty-2011].

#### 3.2.4 Probabilities and Resource Bounds

As we have seen, the (truly playable) effectivity functions of Coalition Logic correspond to games where a joint strategy profile for the set of all agents uniquely determines the outcome. Colition Logic can be modified in several ways (Naumov *et al*. 2021)[^naumov-2021] to deal with *stochastic games*, i.e., where such a profile only determines a probability distribution over the set of possible outcomes. Having modalities $[C]_p \phi$ interpreted as "$C$ can enforce *φ* with probability $p$" leads to interesting and non-trivial (in)valid properties, such as the following variant of superadditivity $(C \cap C' = \emptyset)$

$$ [C]_p(\phi\rightarrow \psi) \rightarrow ([C']_q \phi \rightarrow [C \cup C']_{max\{p,q\}} \psi) $$

not being valid, while

$$ [N]_{p+q+r}(\phi \vee \psi\vee \sigma) \rightarrow [N]_{2p}(\phi \vee \psi) \vee [N]_{2q}(\psi \vee \sigma) \vee [N]_{2r} (\phi \vee \sigma) $$

(where $N$ is the set of all agents) is valid.

As an alternative to stochastic transitions, games with stochastic *failures* can be considerered, which from a logical viewpoint are somewhat easier to deal with (Naumov *et al*. 2021)[^naumov-2021]. Interpreting $[C]_p \phi$ as "$C$ can has a joint strategy to ensure that *φ* is true in each outcome and which is guaranteed not to fail with probability at least $p$ no matter what the other agents do", we get, e.g., that the variant of the superadditivity axiom mentioned above holds.

*Resource bounds* have also been added to coalitional modalities, interpreted in coalition models corresponding to games with costs on performing joint actions (Alechina *et al*. 2009). Here, $[C^b]\phi$ means that $C$ can force *φ* to be true under resource bound $b$, i.e., that they can chose a joint action costing at most $b$ that will ensure that *φ* is true. These modalities satisfy the following variant of superadditivity $(C \cap D = \emptyset, C \neq \emptyset, D \neq \emptyset)$:

$$ [C^b]\phi \wedge [D^d]\psi \rightarrow [(C \cup D)^{b+d}](\phi \wedge \psi). $$

#### 3.2.5 Conditional Power and Coordination

From the viewpoints of truly playable effectivity functions and Coalition Logic, two games are equivalent if coalitions have the same power as defined by *α*-effectivity. Van Benthem *et al*. 2019 point out, however, that there are meaningful differences between games with same *α*-effectivity, due to *monotonicity*: $\{w,v\} \in E(C)$ might be the case for two different reasons. First, it might be that there is a joint action by $C$ such that there is a joint action by the other agents such that the outcome will be $w$ *and* there is another joint action by the other agents such that the outcome will be $v$, or, second, it might be that that is true for only $w$ *or* $v$ (in which case $\{w\} \in E(C)$ or $\{v\} \in E(C)$). The first kind of power is called *basic* power by van Benthem *et al*. 2019, who characterise the properties of effectivity functions of basic power in the two-agent case and gives a sound and complete axiomatisation using a variant of Instantial Neighbourhood Logic (INL) (van Benthem *et al*. 2010) which again is an extension of standard modal logic with neighborhood semantics. One significance of basic power is that it captures all the outcome sets in which the other players are free to chose any state, given the choice of one of those outcome states for some coalition.

Several extensions of the Coalition Logic language have also been developed to reason about conditional and inter-related power between agents and coalitions, typically combining existential and universal quantification over choices. Goranko and Enqvist 2018 introduce extended coalition operators of the form

$$ [C](\phi; \psi_1, \ldots, \psi_k) $$

with the intuitive meaning that $C$ has the power to make *φ* true while at the same time making it possible that the other agents at the same time can achieve any of the objectives $\psi_1,\ldots, \psi_k$. The resulting logic can also be seen as a multi-agent extension of INL. Goranko and Enqvist 2018 also introduce operators of the form

$$ [C_1\triangleright\phi_1, \ldots, C_n\triangleright \phi_n] $$

with the intuitive meaning that the coalition $C = C_1 \cup \cdots C_n$ has a joint strategy such that, for each $i$, the restriction of that joint strategy to coalition $C_i$ enforces objective $\phi_i$.

Goranko and Ju 2022 notice that the latter type of operator can be used to express a certain kind of *conditional* power, namely $[A \triangleright \phi, A \cup B \triangleright \psi]$, intuitively saying that $A$ have a joint action that enforces *φ* while at the same time enables $B$ to apply a joint action that will enforce *ψ*. They also introduce two additional conditional power modalities:

$$ [A]_\alpha(\phi; \langle B\rangle\psi) \text{ and } [A]_\beta(\phi; \langle B\rangle\psi) $$

where the former says that $B \setminus A$ have a joint strategy such that if $A$ applies any action that ensures *φ*, then that joint strategy (by $B\setminus A$) at the same time ensures *ψ*, and the latter that for any joint action by $A$ that enforces *φ* there is a consistent joint action by $B$ that at the same time enforces *ψ*. These notions of power correspond to *α*- and *β*- effectivity, respectively.

Coordination is an issue not only between different coalitions, but also between the agents in the coalition $C$ in the interpretation of $[C]\phi$. In Coalition Logic it is implicitly assumed, like it often is (Schelling 1960)[^schelling-1960], that the agents in $C$ somehow can coordinate their actions to achieve the outcome *φ*. Hawke 2017 introduces a new variant of the coalition modalities that captures a stronger notion of coalitional ability, relaxes the assumption about coordination (in the case of two agents). Contrary to $[C],$ these new modalities $((C))$ are not monotonic.

#### 3.2.6 Dynamic Coalition Logic

Inspired by the model update semantics of dynamic epistemic logic, Coalition Logic has been extended in several ways with dynamic modalities modeling changes in the ability of coalitions in different ways. Broersen, Meyer and Turrini 2009 add expressions of the form $[C \downarrow \psi]\phi$ with the intuitive meaning that after $C$ chooses *ψ*, *φ* holds. Ågotnes and Galimullin 2021 add modalities for adding and removing actions and ability, inspired by arrow update logic: $[(\phi,a,\psi)^+]\gamma$ intuitively means that after the coalition model is updated by, in each *φ*-state, adding a new action for agent $a$ such that no matter what the other agents do that action will guarantee *ψ*, then *γ* holds. There are similar modalities for removing ability. Ågotnes and Galimullin 2023 extend Coalition Logic with more general and expressive modalities for *coalitional action models*, inspired by epistemic action models.

#### 3.2.7 Logic-Based Games

In many situations agents have control over certain propositional variables (Hoek & Wooldridge 2005)[^hoek-2005], for instance they can be responsible for traffic flow or they can veto a certain issue. Variables can also be shared (Gerbrandy 2006)[^gerbrandy-2006], an example being voting, where players share control over a variable whose realization is determined by a certain aggregation function, e.g., majority (Troquard, Hoek, & Wooldridge 2011)[^troquard-2011]. These logics of *propositional control* specify what propositions agents have in their effectivity function. For instance, if agent $i$ controls $p$, then both $p^{M}$ and $\neg p^{M}$ are in his or her effectivity function. In a way these models are very special types of effectivity function, and what agents control can be seen as a choice, or a strategy, available to them.

Logics for propositional control have modalities of the type $[[i]]\varphi$, meaning that player $i$ has a “control” strategy to see to it that, no matter how the other agents choose their control strategies, then *φ* holds in the end. But they also have modalities of the type $[[C]]\varphi$, meaning that players in $C$ have a joint control strategy ensuring *φ* in the end. A strategy profile is thus equivalent to a valuation function, which assigns a truth value of every proposition available. In turn, a strategy of a player $i$ can thus be seen as a partial valuation function, that assigns a truth value only to the propositions controlled by $i$.

Slightly abusing notation, we say that a valuation $V$ satisfies a formula *φ*, denoted $V \models \varphi$, whenever it makes *φ* true under the current assignment of propositions. In other words, propositional control games are played in one single world, and the individual assignments determine what propositions are true are that world. Denoting $\mathcal{V}$ the set of all valuations and $\mathcal{V}_i$ to the partial ones under the control of $i$ we have the following.

$(F,V) \models [[C]]\varphi$ if and only if for all $i \in C$, there exists $V'_i \in \mathcal{V}_i$ such that, for all $k \in \overline{C}, V'_{k}\in \mathcal{V}_k$, we have that $(F,V')\models \varphi$

So when $[[C]]\varphi$ holds, coalition $C$ can play a control strategy in such a way that no matter what the control strategy is that their opponents play, the resulting outcome satisfies *φ*.

Logics for propositional control can be extended to goal-based formalisms, the so called Boolean games (Harrenstein, van der Hoek, Meyer, & Witteveen 2001)[^harrenstein-2001]: propositions are partitioned among the players, with each player controlling the set of propositions he or she is assigned to. On top of that each player is also assigned a formula of propositional logic which is meant to be his or her goal and whose realization might not only depend upon the choices he or she is able to make.

Boolean games have been extensively studied in the field of multi-agent systems, as simple and compact models to represent strategic interaction in a logic-based setting (Dunne & Hoek 2004; Dunne & Wooldridge 2012; Dunne, Hoek, Kraus, & Wooldridge 2008)[^dunne-2004][^dunne-2012][^dunne-2008].

In their most general variants they are an extension of logics with propositional control, where each agent is assigned a goal formula. The goal formula is a satisfiable formula of the language and the important feature is that the goal of each agent does not need to be under his or her control.

For instance, agent $i$ may be assigned the control of proposition $p$ only, but might have the goal that $p \leftrightarrow q$. So whether $i$’s goal is satisfied depends not only on $i$ setting proposition $p$ to be true, but also some other agent, say $j$, setting proposition $q$ to be true. Agent $j$, on the other hand, might or might not be interested in having $q$ set to true. For instance he or she may want proposition $r$ to be true, and therefore being indifferent to whether $q$ or $\overline{q}$ is realized in the end. Or might even have the goal that $\overline{q}$.

In Boolean games some objectives can be realized all together, for instance agents might all want $p \vee \neg q$ to be true, or it might be the case that certain valuations do not realize the objectives of all agents, but no unhappy agent is able to improve his or her own situation by changing the assignment to the propositional variables he or she controls. This situation is a very simple form of Nash equilibrium that can be expressed in Boolean games.

So, for $\gamma_i$ being the objective of player $i$ and $v_i$ a partial valuation that is under control of player $i$, we say that valuation $v$ is a Nash equilibrium if we have that for each $i$ and each $v'_i$.

$$(v_i,v_{-i}) \not\models\gamma_i \mbox{ implies that } (v'_i,v_{-i}) \not\models\gamma_i$$

So if $v$ does not satisfy $i$’s goal, there is nothing $i$ can do to satisfy it.

The analysis of Nash equilibria in Boolean game shows a close correspondence between these games and propositional logic: using a reduction to the satisfiability problem of propositional logic formulas, the problem of checking whether an outcome $v$ is a Nash equilibrium of a Boolean game is co-NP complete (Wooldridge, Endriss, Kraus, & Lang 2013)[^wooldridge-2013].

Another common approach to concisely representing certain classes of games, in addition to representing payoffs qualitatively, is to impose restrictions on the payoff functions. An approach combining the two is found in Das *et al*. 2023, in which Monadic Least Fixed Point logic is used to express the existence of pure strategy Nash equilibria for games with pairwise separable payoff functions.

## 4. Conclusions: On the Right Level of Analysis

Recall the very first example, in which the set of outcomes of a voting game could be described only considering the overall outcome of the vote or by explicitly describing what each of the Countries had voted.

Often times, when describing mathematical structures by succinct languages we are confronted with the question of which one is the most suitable language. Some are able to express preferences, knowledge and coalitional ability all together, some others only two of these, some others only one. Finally some languages might only be able to express what individuals, and not coalitions, can achieve.

Again, there is no right answer to this question. It all depends on what the fundamental characteristics are that one is trying to model. To express Nash equilibria in a coordination game, there is no need for a temporal logic-based formalism. On the contrary, if one wants to express backwards induction, then a language that does not make the sequential structure of the decision problem explicit is probably not the right one.

Going back to our example, some Countries might have preferences over how other Countries vote, and this might affect their decision-making, changing the overall equilibrium points of the game. If this is the case then the richer language matters. Otherwise, if we can safely rule out this possibility, the more succinct language seems to be the appropriate choice.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=logic-power-games). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/logic-power-games/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=logic-power-games&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/logic-power-games/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- Apt, Krzysztof, 2009, “[Cooperative Games](http://homepages.cwi.nl/~apt/coop/10.pdf)”, Course Notes, Centrum Wiskunde & Informatica, Amsterdam.
- [Logic in Action](http://www.logicinaction.org/)

## Related Entries

decision theory | game theory: epistemic foundations of | logic: and games | logic: dynamic epistemic | logic: epistemic | logic: modal | preferences

### Acknowledgments

The author wishes to thank the anonymous reviewers and Valentin Goranko for the very constructive comments on earlier versions of the manuscript.

## Notes（原文脚注）

[^note-1]: This property is typically used when proving completeness via canonical model construction.

[^note-2]: This entry will take neighborhood semantics and non-normal modal logics as the reference formalisms. The reason for this simply lies in the intuitive and straightforward connection between coalitional choices and subsets of outcomes in a relational structures. Everything in this entry could be done only using normal modal logics (and Kripke models) however we felt that the neighborhood approach could offer an added value in terms of clarity. For a mathematical treatment of the connection between the two approaches see for instance Hansen, Kupke, & Pacuit 2009 or the classic Kracht & Wolter 1999.

[^note-3]: Let $A$ be a set. A **filter** on $A$ is a set $X\subseteq 2^A$, such that:

1. $\emptyset \not\in X$
2. $A_1 \in X$ and $A_2 \in X$ imply that $A_1 \cap A_2 \in X$
3. $A_1 \in X$ implies that $A_2\in X$ whenever $A_1\subseteq A_2$.

A **principal filter** is a filter with a least element.

[^note-4]: We adopt a rough version of hybrid logic here, starting from the assumption that there exists an atomic proposition *naming* each world. For a technical discussion on hybrid logic see Blackburn et al. 2001.

[^note-5]: Using the same argument one can show that Playable Coalition Logic is sound and complete with respect to Truly Playable Coalition Models (see Blackburn et al. 2001 for the definition of soundness and completeness of a set of axioms with respect to a class of frames/models)[^blackburn-2001].

[^abdou-1991]: Abdou, Joseph and Hans Keiding, 1991, *Effectivity Functions in Social Choice*, (Theory and Decision Library 8), Dordrecht: Springer Netherlands, doi:10.1007/978-94-011-3448-4

[^ågotnes-2015]: Ågotnes, Thomas, Alechina, Natasha, 2015, “Embedding Coalition Logic in the Minimal Normal Multimodal Logic with Intersection”, in S. Ju, H. Liu, and H. Ono (eds.), *Modality, Semantics and Interpretations* (Logic in Asia: Studia Logica Library), Berlin, Heidelberg: Springer.

[^ågotnes-2008]: Ågotnes, Thomas, van der Hoek, W., & Wooldridge, M., 2008, “Quantified Coalition Logic”, *Synthese*, 165(2): 269–294. [[Ågotnes *et al*. 2008 available online](https://www.jstor.org/stable/40271103)]

[^ågotnes-2009]: –––, 2009, “Reasoning about coalitional games”, 2009, *Artificial Intelligence*, 173: 45–79.

[^alechina-2011]: Alechina, Natasha, Brian Logan, Hoang Nga Nguyen, Abdur Rakib, 2011, “Logic for coalitions with bounded resources”, *Journal of Logic and Computation*, 21(6): 907–937. doi:10.1093/logcom/exq032

[^baltag-2016]: Baltag, Alexandru and Bryan Renne, 2016, “Dynamic Epistemic Logic”, in *Stanford Encyclopedia of Philosophy*, (Winter 2016 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/win2016/entries/dynamic-epistemic/](https://plato.stanford.edu/archives/win2016/entries/dynamic-epistemic/)>

[^belnap-2001]: Belnap, Nuel, Michael Perloff, and Ming Xu, 2001, *Facing the Future: Agents and Choices in Our Indeterminist World*, Oxford: Oxford University Press.

[^benthem-2012]: Benthem, Johan van, 2012, “In praise of strategies”, in J. van Eijck, R. Verbrugge (eds.), *Games, Actions and Social Software* (Lecture Notes in Computer Science: Volume 7010), Berlin, Heidelberg: Springer, pp. 96–116.

[^benthem-2014]: –––, 2014, *Logic in Games*, Cambridge, MA: MIT Press.

[^benthem-2017]: Benthem, J. van, Bezhanishvili, N., Enqvist, S., and Yu, J., 2017, “Instantial Neighbourhood Logic”, *The Review of Symbolic Logic*, 10(1): 116–144. doi:10.1017/S1755020316000447

[^benthem-2011]: Benthem, Johan van, Eric Pacuit, and Olivier Roy, 2011, “Toward a Theory of Play: A Logical Perspective on Games and Interaction”, *Games*, 2(1): 52–86. doi:10.3390/g2010052

[^blackburn-2001]: Blackburn, Patrick, Maarten de Rijke, and Yde Venema, 2001, *Modal Logic*, Cambridge: Cambridge University Press. doi:10.1017/CBO9781107050884

[^boella-2010]: Boella, Guido, Dov M. Gabbay, Valerio Genovese, and Leendert van der Torre, 2010, “Higher-Order Coalition Logic”, in *Proceedings of the 2010 conference on ECAI 2010: 19th European Conference on Artificial Intelligence*, IOS Press, NLD, 555–560.

[^broersen-2009]: Broersen, J., Mastop, R., Ch.Meyer, J. J. and Turrini, P., 2009, “Strategic Ability Update: A Modal Logic Account”, in *2009 IEEE/WIC/ACM International Joint Conference on Web Intelligence and Intelligent Agent Technology*, Milan, Italy, 2009, pp. 470–473. doi: 10.1109/WI-IAT.2009.328

[^chellas-1980]: Chellas, Brian, 1980, *Modal Logic: An Introduction*, Cambridge: Cambridge University Press.

[^chen-2014]: Chen, Q., Li, Q., Su, K., Luo, X., 2014, “Quantified Coalition Logic for BDI-Agents: Completeness and Complexity”, in DN. Pham and SB. Park (eds.), *PRICAI 2014: Trends in Artificial Intelligence* (Lecture Notes in Computer Science: Volume 8862), Cham: Springer. doi:10.1007/978-3-319-13560-1_72

[^chen-2023]: Chen, Q., Shi, C., and Wang, Y., 2023, “Reasoning about Dependence, Preference and Coalitional Power”, *Journal of Philosophical Logic*, first online 28 November 2023. doi:10.1007/s10992-023-09727-2

[^dalen-1980]: Dalen, Dirk van, 1980, *Logic and Structure*, Berlin: Springer-Verlag. doi:10.1007/978-3-662-02962-6

[^das-2023]: Das, R., Ramanujam, R., Simon, S., 2023, “A Logical Description of Priority Separable Games”, in N. Alechina, A. Herzig, and F. Liang (eds.), *Logic, Rationality, and Interaction*: LORI 2023 (Lecture Notes in Computer Science: Volume 14329), Cham: Springer. doi:10.1007/978-3-031-45558-2_3

[^doherty-2011]: Doherty, Patrick, Barbara Dunin-Keplicz, and Andrzej Szałas, 2011, “Tractable model checking for fragments of higher-order coalition logic”, in *The 10th International Conference on Autonomous Agents and Multiagent Systems – Volume 2* (AAMAS ’11), International Foundation for Autonomous Agents and Multiagent Systems, Richland, SC, 743–750.

[^dunne-2004]: Dunne, Paul E. and Wiebe van der Hoek, 2004, “Representation and Complexity in Boolean Games”, in José Júlio Alferes & João Alexandre Leite (eds.), *Logics in Artificial Intelligence, 9th European Conference, JELIA 2004, Lisbon, Portugal, September 27–30, 2004, Proceedings*, Berlin, Heidelberg: Springer, 3229: 347–359. doi:10.1007/978-3-540-30227-8_30

[^dunne-2012]: Dunne, Paul E. and Michael Wooldridge, 2012, “Towards Tractable Boolean Games”, in Wiebe van der Hoek, Lin Padgham, Vincent Conitzer, & Michael Winikoff (eds.), *Proceedings of the 11th International Conference on Autonomous Agents and Multiagent Systems*, (AAMAS 2012), Valencia, Spain, June 4–8, 2012, Richland, SC: International Foundation for Autonomous Agents and Multiagent Systems, vol. 2, pp. 939–946.

[^dunne-2008]: Dunne, Paul E., Wiebe van der Hoek, Sarit Kraus, and Michael Wooldridge, 2008, “Cooperative Boolean Games”, in Lin Padgham, David C. Parkes, Jörg P. Müller, & Simon Parsons (eds.), *Proceedings of the 7th International Joint Conference on Autonomous Agents and Multiagent Systems*, (AAMAS 2008), Estoril, Portugal, May 12–16, 2008, Richland, SC: International Foundation for Autonomous Agents and Multiagent System, vol. 2, pp. 1015–1022.

[^enqvist-2019]: Enqvist, Sebastian, Nick Bezhanishvili & Johan van Benthem, 2019, “A New Game Equivalence, its Logic and Algebra”, *Journal of Philosophical Logic*, 48(4): 649–684

[^galimullin-2021]: Galimullin, R. and Ågotnes, T., 2021, “Dynamic Coalition Logic: Granting and Revoking Dictatorial Powers”, in *Logic, Rationality, and Interaction*: LORI 2021 (Proceedings of the 8th International Workshop), Xi’an, China, October 16-18, Berlin, Heidelberg: Springer-Verlag, pp. 88–101. doi:10.1007/978-3-030-88708-7_7

[^galimullin-2023]: Galimullin, R., Ågotnes, T., 2023, “Action Models for Coalition Logic”, in C. Areces and D. Costa (eds.), *Dynamic Logic. New Trends and Applications*: DaLí 2022 (Lecture Notes in Computer Science: Volume 13780), Cham: Springer. doi:10.1007/978-3-031-26622-5_5

[^gargov-1988]: Gargov, G., Passy, S., 1988, “A note on boolean modal logic”, in *Mathematical Logic* (Proceedings of The Summer School and Conference on Mathematical Logic, Heyting’88), New York: Plenum Press, pp. 311–321.

[^garson-2014]: Garson, James, 2014, “Modal Logic”, in *Stanford Encyclopedia of Philosophy*, (Spring 2016 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/spr2016/entries/logic-modal/](https://plato.stanford.edu/archives/spr2016/entries/logic-modal/)>.

[^gerbrandy-2006]: Gerbrandy, Jelle, 2006, “Logics of Propositional Control”, in Hideyuki Nakashima, Michael P. Wellman, Gerhard Weiss, & Peter Stone (eds.), *Proceedings of the 5th International Joint Conference on Autonomous Agents and Multiagent Systems*, (AAMAS 2006), Hakodate, Japan, May 8–12, 2006, New York: ACM, pp. 193–200. doi:10.1145/1160633.1160664

[^goranko-1992]: Goranko, Valentin and Salomon Passy, 1992, “Using the Universal Modality: Gains and Questions”, *Journal of Logic and Computation*, 2(1): 5–30. doi:10.1093/logcom/2.1.5

[^goranko-2006]: Goranko, V., van Drimmelen, G., 2006, “Complete axiomatization and decidability of alternating-time temporal logic”, *Theoretical Computer Science*, 353(1–3): 93–117 (2006)

[^goranko-2013]: Goranko, Valentin, Wojciech Jamroga, and Paolo Turrini, 2013, “Strategic Games and Truly Playable Effectivity Functions”, *Autonomous Agents and Multi-Agent Systems*, 26(2): 288–314. doi:10.1007/s10458-012-9192-y

[^goranko-2018]: Goranko, Valentin and Enqvist, Sebastian, 2018, “Socially Friendly and Group Protecting Coalition Logics”, in *Proceedings.of the 17th International Conference on Autonomous Agents and Multiagent Systems* (AAMAS 2018), M. Dastani, G. Sukthankar, E. André, S. Koenig (eds.), July 10–15, 2018, Stockholm, Sweden. International Foundation for Autonomous Agents and Multiagent Systems.

[^goranko-2022]: Goranko, Vanetin and Ju, Fengkui, 2022, “A Logic for Conditional Local Strategic Reasoning”, *Journal of Logic, Language and Information*, 31: 167–188.

[^hansen-2003]: Hansen, Helle Hvid, 2003, *Monotonic Modal Logics*, Masters Thesis, University of Amsterdam.

[^hansen-2002]: Hansen, Helle Hvid and Marc Pauly, 2002, “Axiomatising Nash-Consistent Coalition Logic”, in Sergio Flesca, Sergio Greco, Nicola Leone, & Giovambattista Ianni (eds.), *Logics in Artificial Intelligence*, Berlin: Springer, 2424: 394–406. doi:10.1007/3-540-45757-7_33

[^hansen-2009]: Hansen, Helle Hvid, Clemens Kupke, and Eric Pacuit, 2009, “Neighbourhood Structures: Bisimilarity and Basic Model Theory”, *Logical Methods in Computer Science*, 5(2): lmcs:1167. [[Hansen, Kupke, & Pacuit 2009 available online](https://lmcs.episciences.org/1167)]

[^hansson-2011]: Hansson, Sven Ove and Till Grune-Yanoff, 2011, “Preferences”, in *Stanford Encyclopedia of Philosophy*, (Fall 2011 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/fall2011/entries/preferences/](https://plato.stanford.edu/archives/fall2011/entries/preferences/)>

[^harrenstein-2001]: Harrenstein, Paul, Wiebe van der Hoek, John-Jules Meyer, and Cees Witteveen, 2001, “Boolean Games”, in Johan van Benthem (ed.), *Proceedings of the 8th Conference on Theoretical Aspects of Rationality and Knowledge*, (Tark ’01), San Francisco: Morgan Kaufmann, pp. 287–298.

[^hawke-2017]: Hawke, Peter, 2017, “The Logic of Joint Ability in Two-Player Tacit Games” *Review of Symbolic Logic*, 10(3): 481–508.

[^hendricks-2006]: Hendricks, Vincent and John Symons, 2006, “Epistemic Logic”, in *Stanford Encyclopedia of Philosophy*, (Spring 2006 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/spr2006/entries/logic-epistemic/](https://plato.stanford.edu/archives/spr2006/entries/logic-epistemic/)>

[^hodges-2013]: Hodges, Wilfrid, 2013, “Logic and Games”, in *Stanford Encyclopedia of Philosophy*, (Spring 2013 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/spr2013/entries/logic-games/](https://plato.stanford.edu/archives/spr2013/entries/logic-games/)>.

[^hoek-2006]: Hoek, Wiebe van der and Marc Pauly, 2006, “Modal Logic for Games and Information”, in Patrick Blackburn, Johan van Benthem, & Frank Wolter (eds.), *Handbook of Modal Logic*, pp. 1077–1148, Elsevier.

[^hoek-2005]: Hoek, Wiebe van der and Michael Wooldridge, 2005, “On the Logic of Cooperation and Propositional Control”, *Artificial Intelligence*, 164(1–2): 81–119. doi:10.1016/j.artint.2005.01.003

[^kooi-2008]: Kooi, Barteld and Allard Tamminga, 2008, “Moral Conflicts Between Groups of Agents”, *Journal of Philosophical Logic*, 37(1): 1–21. doi:10.1007/s10992-007-9049-z

[^kracht-1999]: Kracht, Marcus and Frank Wolter, 1999, “Normal Monomodal Logics Can Simulate All Others”, *Journal of Symbolic Logic*, 64(1): 99–138. doi:10.2307/2586754

[^moulin-1982]: Moulin, Herve and Bezalel Peleg, 1982, “Cores of Effectivity Functions and Implementation Theory”, *Journal of Mathematical Economics*, 10(1): 115–145. doi:10.1016/0304-4068(82)90009-X

[^naumov-2021]: Naumov, Pavel and Kevin Ros, 2021, “Strategic coalitions in stochastic games”, *Journal of Logic and Computation*, 31(7): 1845–1867. doi:10.1093/logcom/exab032

[^osborne-1994]: Osborne, Martin and Ariel Rubinstein, 1994, *A Course in Game Theory*, Cambridge, MA: MIT Press.

[^pacuit-2015]: Pacuit, Eric and Olivier Roy, 2015, “Epistemic Foundations of Game Theory”, in *Stanford Encyclopedia of Philosophy*, (Spring 2015 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/spr2015/entries/epistemic-game/](https://plato.stanford.edu/archives/spr2015/entries/epistemic-game/)>

[^pauly-2001]: Pauly, Marc, 2001, *Logic for Social Software*, Ph.D. thesis, University of Amsterdam. [[Pauly 2001 available online](http://hdl.handle.net/11245/1.194561)]

[^peleg-1998]: Peleg, Bezalel, 1998, “Effectivity Functions, Game Forms, Games and Rights”, *Social Choice and Welfare*, 15(1): 67–80. doi:10.1007/s003550050092

[^schelling-1960]: Schelling, T., 1960, *The Strategy of Conflict*, Cambridge, MA: Harvard University Press.

[^steele-2015]: Steele, Katie and Orri Stefansson, 2015, “Decision Theory”, in *Stanford Encyclopedia of Philosophy*, (Winter 2015 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/win2015/entries/decision-theory/](https://plato.stanford.edu/archives/win2015/entries/decision-theory/)>

[^tamminga-2013]: Tamminga, Allard, 2013, “Deontic Logic for Strategic Games”, *Erkenntnis*, 78(1): 183–200. doi:10.1007/s10670-011-9349-0

[^troquard-2009]: Troquard, Nicolas, Wiebe van der Hoek, and Michael Wooldridge, 2009, “A Logic of Games and Propositional Control”, in Carles Sierra, Cristiano Castelfranchi, Keith S. Decker, & Jaime Simão Sichman (eds.), *Proceedings of the 8th International Joint Conference on Autonomous Agents and Multiagent Systems*, (AAMAS 2009), Budapest, Hungary, May 10–15, 2009, Volume 2, Richland, SC: International Foundation for Autonomous Agents and Multiagent Systems, pp. 961–968.

[^troquard-2011]: –––, 2011, “Reasoning About Social Choice Functions”, *Journal of Philosophical Logic*, 40(4): 473–498. doi:10.1007/s10992-011-9189-z

[^turrini-2012]: Turrini, Paolo, 2012, “Agreements as Norms”, in Thomas Ågotnes, Jan Broersen, & Dag Elgesem (eds.), *Deontic Logic in Computer Science: 11th International Conference* (DEON 2012), Bergen, Norway, July 16–18, 2012, Berlin: Springer, 31–45. doi:10.1007/978-3-642-31570-1_3

[^wooldridge-2004]: Wooldridge, Michael, & Dunne, P. E., 2004, “On the computational complexity of qualitative coalitional games”, *Artificial Intelligence*, 158(1): 27–73.

[^wooldridge-2013]: Wooldridge, Michael, Ulle Endriss, Sarit Kraus, and Jérôme Lang, 2013, “Incentive Engineering for Boolean Games”, *Artificial Intelligence*, 195: 418–439. doi:10.1016/j.artint.2012.11.003
