# Dependence Logic
**First published Thu Feb 23, 2017; substantive revision Mon May 19, 2025**

*Galliani, Pietro*

Dependence logic is an extension of first-order logic which adds to it *dependence atoms*, that is, expressions of the form $\eqord(x_1 \ldots x_n, y)$ which assert that the value of $y$ is functionally dependent on (in other words, determined by) the values of $x_1 \ldots x_n$. These atoms permit the specification of non-linearly ordered *dependency patterns* between variables, much in the same sense of IF-Logic *slashed quantifiers*; but, differently from IF-logic, dependence logic separates quantification from the specification of such dependence/independence conditions.

The principal semantics of dependence logic, called *team semantics*, generalizes Tarski’s semantics by letting expressions be satisfied or not satisfied with respect to *sets* of variable assignments rather than with respect to single assignments. This semantics pre-dates the development of dependence logic proper, and it was originally developed by Wilfrid Hodges in the context of IF-logic (Hodges 1997)[^hodges-1997]. There also exists a game-theoretic semantics for dependence logic, based on games of imperfect information and roughly analogous to the game-theoretic semantics for independence-friendly logic (Väänänen 2007a)[^väänänen-2007a]. *Sensu stricto*, the term “dependence logic” refers exclusively to the language obtained by adding the above-mentioned functional dependence atoms to the language of first-order logic; but the term is also used, in a more general sense, to refer to the area of research that studies the properties of logics obtained by adding various *notions of dependence and independence* to first order logic, such as *independence logic* (Grädel & Väänänen 2013)[^grädel-2013], *intuitionistic dependence logic* (Yang 2013)[^yang-2013] or *inclusion logic* (Galliani 2012, Galliani & Hella 2013)[^galliani-2012][^galliani-2013], or even those of logics extending *other* logical frameworks through similar atoms, as in the case of *modal dependence logic* (Väänänen 2008)[^väänänen-2008].

In this article, the term “dependence logic” will be used to refer to dependence logic proper, and the term “logics of dependence and independence” will instead be used to refer to its variants and generalizations.

## 1. Dependency patterns in first order logic and its extensions

One feature of first order logic which accounts for much of its expressivity and applicability is the fact that it allows quantifiers to be *nested*, and, hence, it permits the specification of *dependency patterns* between quantified variables. Consider, for example, the (hopefully false) statement that “every boy loves some girl that loves some other boy”. It can be straightforwardly translated into first order logic as

$$\tag{1} \label{eq:boygirl1} \begin{align} &\forall x (\boy(x) \rightarrow \exists y (\girl(y) \land \loves(x, y) \land {} \\ &\quad \exists z (\boy(z) \land x \not = z \land \loves(y, z)))) \end{align} $$

whose truth condition, according to Tarski’s usual semantics, is precisely what one would expect: the above expression is true if and only if for every boy $b$ it is possible to find a girl $g$ and a boy $b'$ such that $b$ loves $g$ and $g$ loves $b'$ and $b$ and $b'$ are not the same. The identity of the girl $g$ may of course depend on the identity of the first boy $b$—after all, for this expression to be true we do not require that all boys are in love with all girls—and, furthermore, the identity of the second boy $b'$ may depend on *both* the identity of the first boy $b$ (since $b'$ must be different from $b$) and from the identity of the girl $g$ that $b$ loves. So the *dependency pattern* between our quantified variables is as follows: $y$ depends on $x$, while $z$ depends on both $x$ and $y$. From a syntactic perspective, this is reflected by the fact that $\exists y$ is in the *scope* of $\forall x$ while $\exists z$ is in the scope of both $\forall x$ and $\exists y$.

Differences in the dependency patterns between operators can be used to formalize important distinctions, such as for example the one between the continuity of a function $f$

$$\forall x \forall \epsilon \exists \delta \forall x' (|x - x'| < \delta \rightarrow |f(x) - f(x')| < \epsilon)$$

and its uniform continuity

$$\forall \epsilon \exists \delta \forall x \forall x' (|x - x'| < \delta \rightarrow |f(x) - f(x')| < \epsilon)$$

or, in intensional extensions of first order logic, to express the difference between *De Dicto* and *De Re* readings (e.g., “It is possible for every person to be crazy” may be understood either as stating that it for every person $p$, it is possible for $p$ to be crazy, $\forall x (\person (x) \rightarrow \Diamond \crazy (x))$, or as stating that it is possible that everyone is crazy together, $\Diamond \forall x (\person (x) \rightarrow \crazy (x))$).

Dependency patterns between quantified variables in first order logic are necessarily *transitive*, as it is made evident by their connections with the scopes of the corresponding sub-expressions: if $\exists y$ is in the scope of $\forall x$ and $\exists z$ is in the scope of $\exists y$ then necessarily $\exists z$ will be in the scope of (and, therefore, dependent from) $\forall x$. Furthermore, the set of all quantifiers in whose scope some subformula *α* lies is linearly ordered: if *α* is in the scope of $Q_1 x_1$ and $Q_2 x_2$, then either $Q_1 x_1$ is in the scope of $Q_2 x_2$ or vice versa.

This limits the expressive possibilities of first order logic. For example, let us suppose that we wish to amend our previous assertion about boys and girls as follows: every boy loves some girl that loves some other boy, and this second boy can be chosen independently on the first one. What this means, intuitively speaking, is simple enough: for every boy $b$ we can find a girl $g$ such that $b$ loves $g$, and for every such girl we can find a boy $b'$ such that $g$ loves $b'$ and $b \not = b'$, and furthermore we can find the identity of the second boy $b'$ without knowing that of $b$, on the basis of the identity of the girl $g$ alone. This can still be the true in some scenarios, such as for example if two boys $b_1$ and $b_2$ love respectively two girls $g_1$ and $g_2$, who however love only $b_2$ and $b_1$ respectively. However, it is easily seen that it is not equivalent to our previous statement: for example, if our universe consists (as in (b) above) of two boys $b$ and $b'$ and a girl $g$, and $b$ and $b'$ both love $g$ who loves both of them, then our previous assertion is true but the current one is false.

![[two similar figures, both figures have the words 'Boys' and 'Girls' separated by horizontal space at the top. Figure (a) has point b1 at the upper left, g1 at the upper right, b2 at the lower left and g2 at the lower right. Arrows point from g1 to b1, from b1 to g2, from g2 to b2, and b2 to g1. Figure (b) has b1 at the upper left, b2 at the lower left, g1 at the middle right. An arrow points both from and to b1 and g1 and similarly from b2 to g1.]](../assets/logic-dependence/bg1.svg)

Two scenarios in which ($\ref{eq:boygirl1}$) is true. In (a), $z$ can be chosen independently from $x$; in (b), it cannot.

However, it is not clear how to formalize this condition in first order logic. In essence, we would need to modify ($\ref{eq:boygirl1}$) so that $z$ is not in the scope of $x$, and hence it does not depend on it; however, we would still want $z$ to depend on $y$ and $y$ on $x$. As just discussed, however, such a dependency pattern is not realizable in first-order logic. We can sidestep the issue by resorting to higher-order quantification: indeed, one can see that the expression

$$\tag{2}\label{boygirl2} \begin{align} &\exists F \forall x (\boy (x) \rightarrow \exists y(\girl (y) \land \loves (x, y) \land \boy (F(y)) \land {} \\ &\quad x \not = F(y) \land \loves (y,F(y)))) \end{align}$$

captures our intended interpretation, but only at the cost of explicit existential quantification over functions.

A possible alternative would be to expand the syntax of first order logic in order to lift the restrictions about dependency patterns between quantified variables. This is the route taken by *branching quantifier logic* (Henkin 1961)[^henkin-1961], in which the truth conditions of ($\ref{boygirl2}$) correspond to those of

$$\tag{3}\label{boygirl3} \begin{align} &\left(\begin{smallmatrix} \forall x &\exists y\\ \forall z &\exists w \end{smallmatrix} \right)(\boy (x) \rightarrow (\girl (y) \land \loves (x,y) \land {}\\ &\quad (y = z \rightarrow (\boy (w) \land x \not = w \land \loves (z,w))))), \end{align} $$

and to *independence-friendly logic*, in which ($\ref{boygirl2}$) is equivalent to

$$\tag{4}\label{boygirl4} \begin{align} &\forall x \exists y (\boy (x) \rightarrow (\girl (y) \land \loves (x,y) \land (\exists z/x) (\boy (z) \land {} \\ &\quad x \not = z \land \loves (y,z)))). \end{align} $$

We will not give here a detailed explanation of the semantics of these two formalisms; suffice to say, in ($\ref{boygirl3}$) the value of $w$ does not depend on the values of $x$ and $y$ (although it may depend on the value of $z$), as they belong to different “rows” of the complex quantifier $\left(\begin{smallmatrix} \forall x &\exists y\\ \forall z &\exists w \end{smallmatrix}\right)$, while in ($\ref{boygirl4}$) the value of $z$ does not depend on the value of $x$, because this dependency is explicitly “slashed away” by the quantifier ($\exists z / x$).

One feature common to branching quantifier logic and independence friendly logic, as we can see, is that they do not separate the quantification of variables from the specification of non-standard patterns of dependence: as in the case of first order logic, whether a quantified variable $v_1$ will or will not depend on some other quantified variable $v_2$ will be determined by the respective position and form of their quantifiers.

Dependence logic takes a different approach to the problem of extending first order logic in order to represent ($\ref{boygirl2}$). Compared to ($\ref{eq:boygirl1}$), the only novel condition is the one that states that the value of $z$ is *determined* by (that is, functionally dependent on) the value of $y$; and this corresponds to a new atomic condition $\eqord(y, z)$, called a *dependence atom*, whose intended meaning is that (the value of) $z$ is a function of the value of $y$. Differently from the cases of branching quantifier logic or independence-friendly logic, this is a condition over the values that $y$ and $z$ can take, not a condition over the behaviour of the quantifier $\exists z$: indeed, there is in general no reason to require that $z$ is a quantified variable at all—it might well be a free variable instead, or some complex term involving multiple variables.

In dependence logic, ($\ref{boygirl2}$) can be formalized as

$$\tag{5}\label{boygirl5} \begin{align} &\forall x \exists y \exists z (\eqord(y,z) \land ( \boy (x) \rightarrow (\girl (y) \land \loves (x,y) \rightarrow {}\\ &\quad (\boy (z) \land x \not = z \land \loves (y,z))))) \end{align} $$

The truth conditions of ($\ref{boygirl2}$), ($\ref{boygirl3}$), ($\ref{boygirl4}$) and ($\ref{boygirl5}$) are precisely the same: any model that satisfies one of these expressions (in the respective languages) satisfies all four. More in general, as we will see, the expressive powers of existential second-order logic, independence-friendly logic and dependence logic *with respect to definability of classes of models* are precisely the same. This is, however, not the case for formulas with free variables; and furthermore, these logics can be extended and modified along markedly different lines.

## 2. Team semantics

Team semantics, first developed by Wilfrid Hodges in the context of independence friendly logic (Hodges 1997)[^hodges-1997], is a generalization of Tarski’s semantics for first order logic to the case of multiple assignments of elements to variables. Sets of such assignments, called *teams* for historical reasons, constitute the fundamental semantic notion of team semantics, and formulas are satisfied or not satisfied with respect to them rather than with respect to single assignments. The connection between team semantics and Tarski semantics is shown by the following result, which holds in dependence logic as well as in all its first order variants:

**Conservativity:** A first order formula is satisfied by a team $X$ (in the sense of team semantics) if and only if all assignments $s \in X$ satisfy it (in the sense of Tarski semantics).

More in general, teams can be understood as *belief sets*, representing the set of all states of the world (=assignments) that some agent believes possible. Then a team $X$ will satisfy some formula *φ* if and only if *φ* holds when $X$ is the set of all possible states; and in this case, we will write $X \models \phi$ (or $M, X \models \phi$ if the choice of the model $M$ is not clear). In this section, we will examine the rules of team semantics and their interpretation in terms of this principle; then, in the next section, we will discuss how it also arises from the imperfect-information *game-theoretic semantics* for dependence logic.

The condition for the new dependence atoms $\eqord(x_1 \ldots x_n, y)$, which correspond to the statement that the value of $y$ is a function of the values of $x_1 \ldots x_n$, is easily understood:

**TS-dep:** $X \models ~\eqord(x_1 \ldots x_n, y)$ if and only if any two assignments $s_1, s_2 \in X$ which agree on the values of $x_1 \ldots x_n$ also agree on the value of $y$.

For example, suppose that $X$ is a set of assignments over the three variables $x_1$, $x_2$ and $y$, where $x_1$ represents the nationality of a candidate to a position, $x_2$ represents their score (according to a suitable evaluation method) and $y$ represents whether they were accepted or rejected. Then the atom $\eqord(x_2, y)$ corresponds to the statement that the offer is determined by the score alone: if two candidates have the same score they will receive exactly the same offer, regardless of any other factor. A special case of dependence atom is given by the *constancy atoms* $\eqord(y)$, which—as per the above semantics—are satisfied by a team if and only if all of its assignments agree over the value of $y$.

$$\begin{array}{l | c c c} \textbf{assignment}& \mathbf{x_1} & \mathbf{x_2} & \mathbf{y}\\ \hline s_0 & 0 & 0 & 0 \\ s_1 & 0 & 1 & 1 \\ s_2 & 1 & 0 & 1 \\ s_3 & 1 & 1 & 2 \end{array}$$

*Table 1:* A team $X$ in which $y = x_1 + x_2$. Here $y$ is a function of $x_1$ and $x_2$, and hence $=\!\!(x_1 x_2, y)$ holds; however, $y$ is not a function of $x_1$ alone, so $=\!\!(x_1, y)$ does not hold.

Under the same interpretation, the rules for first-order literals and conjunctions (for simplicity, we will assume that our expressions are in negation normal form; and, as is customary, we will assume that the negations of dependence atoms are never satisfied) are easy to derive:

**TS-lit:** For all first-order literals *α*, $X \models \alpha$ if and only if for all assignments $s \in X$, $s \models \alpha$ in the usual Tarski semantics sense;

**TS-$\land$:** $X \models \phi \land \psi$ if and only if $X \models \phi$ and $X \models \psi$.

It is worth pointing out that, as we can already see by these rules, the *law of the excluded middle* does not hold in dependence logic (just as it does not hold in independence friendly logic): for example, if a team $X$ contains both assignments $s$ with $s(x) = s(y)$ and assignments $s'$ with $s'(x) \not = s'(y)$ then $X \not \models x=y$ and $X \not \models x\not = y$. In this section, in any case, we will present the language of dependence logic without an explicit negation operator; then, later, we will discuss the consequences of adding it to its language.

What about universal quantification? In which circumstances should a universally quantified expression $\forall v \psi$ hold in a team? Again, we must recall the intuition according to which a team represents a set of possible states of things. If we wish to evaluate $\forall v \psi$, with respect to which possible states of things should we evaluate *ψ*? The natural answer is that we should consider all states of things that differ from ones in $X$ only with respect to the value of $v$. This justifies the following rule:

**TS-$\forall$:** $X \models \forall v \psi$ if and only if $X[M/v] \models \phi$, where $X[M/v]$ is the set $\{s' : \exists s \in X \mbox{ s.t. } s' \sim_v x\}$

where $s' \sim_v s$ means that the two assignments $s$ and $s'$ differ from each other at most with respect to the value of the variable $v$.

$$ X= \begin{array}{l | c} \textbf{assignment} & x\\ \hline s_0 & 0\\ s_1 & 1 \end{array} \Rightarrow X[M/y]= \begin{array}{l | c | c} \textbf{assignment} & x & y\\ \hline s'_0 & 0 & 0\\ s'_1 & 0 & 1\\ s'_2 & 1 & 0\\ s'_3 & 1 & 1 \end{array}$$

*Table 2:* $X$ and $X[M/y]$ in a model with two elements $0$ and $1$.

Let us now consider disjunction. When should $\phi \lor \psi$ hold? To answer this, let us recall—once again—that teams can be understood as sets of possible states of things, and that therefore the union of two teams $Y$ and $Z$ represents all states of things which may occur if $Y$ or $Z$ is the case. Therefore, if the two formulas *φ* and *ψ* are satisfied by the set of teams $\{Y_1 \ldots Y_n, \ldots\}$ and $\{Z_1 \ldots Z_n, \ldots\}$ respectively, their disjunction $\phi \lor \psi$ should be satisfied by the set of teams $\{Y_i \cup Z_j : i,j \in 1, \ldots\}$, or, equivalently,

**TS-$\lor$:** $X \models \phi \lor \psi$ if and only if $X=Y \cup Z$ for two teams $Y$ and $Z$ such that $Y \models \phi$ and $Z \models \psi$.

It is worth pointing out here that we do *not* require, in general, that $Y$ and $Z$ are disjoint. Because of the *downwards closure property*, which we will discuss soon, this additional condition would make no difference for the semantics of dependence logic proper; but in the case of certain extensions and variants of dependence logic, that additional requirement would conflict with the principle of *locality* according to which the satisfaction conditions of an expression depend only on the values of the variables which occur free in it (Galliani 2012)[^galliani-2012].

It is also important to note that, in dependence logic, disjunction is *not* idempotent: for example, $\eqord(x,y) \lor \eqord(x,y)$ is not equivalent to $\eqord(x,y)$, and it is satisfied by a team $X$ if and only if for every *three* assignments in $X$ which agree on $x$ at least *two* agree on $y$. This may appear somewhat counter-intuitive; but it is a straightforward consequence of the fact that, under our interpretation, $\eqord(x,y) \lor \eqord(x,y)$ is to be read as “every possible state of things comes from one of two sets of states of things, and in both of them $y$ is a function of $x$”. Since the union of functions is not in general a function, it comes to little surprise that disjunction in dependence logic is not idempotent.

Finally, we consider the case of existential quantification. When is the expression $\exists v \psi$ satisfied by a team? In order to answer this, we may begin by considering the interpretation of the *restriction* operator which, given any team $X$, results in the team $X_{\backslash v}$ obtained by removing the variable $v$ (if present) from all assignments $s \in X$ (and then, since $X$ is a set, by collapsing identical assignments). This could be understood as a *forgetting* operation, through which we delete all information about the value of $v$—for example, because what we believed about this value was unreliable, or because this value has been altered. Now suppose that $X_{\backslash v} = Y_{\backslash v}$: then, in our interpretation, this means that the sets of possible states of things represented by $X$ and $Y$ disagree at most with respect to the value of $v$. Thus, if $Y$ satisfies the condition *φ*, we may say that $X$ would satisfy *φ* *if not for the value of* $y$, or, equivalently, that $X$ satisfies $\exists v \psi$. This justifies the following rule:

**TS-$\exists$:** $X \models \exists v \psi$ if and only if there exists some $Y$, over the variables of $X$ and $v$, such that $X_{\backslash v} = Y_{\backslash v}$ and $Y \models \psi$.

It is straightforward to verify that this is the case if and only if $Y$ is of the form $X[F/y] = \{s[a/y] : s \in X, a \in F(s)\}$ for some function $F$ from assignments in $X$ to nonempty sets of elements of our model.

It is worth pointing out here that it is not in general required by the above definition that $X$ and $Y$ contain the same number of assignments: a single assignment in $X$ may well correspond to multiple assignments in $Y$, and—if $v$ is already a variable occurring in the assignments of $X$—a single assignment in $Y$ may also correspond to multiple assignments in $X$.

$$ X= \begin{array}{l | c} \textbf{assignment} & x\\ \hline s_0 & 0\\ s_1 & 1 \end{array} \Rightarrow X[F/y]= \begin{array}{l | c | c} \textbf{assignment} & x & y\\ \hline s'_0 & 0 & 0\\ s'_1 & 0 & 1\\ s'_2 & 1 & 0 \end{array}$$

*Table 3:* $X$ and $X[F/y]$ for $F(s_0) = \{0,1\}$, $F(s_1) = \{0\}$

We will postpone an in-depth discussion of the properties of dependence logic to after the specification of its game-theoretic semantics. However, we conclude this section with the following three important consequences of the above-given rules:

**Locality:** If the restrictions of $X$ and $Y$ to the variables occurring free in *φ* are the same then $X \models \phi$ if and only if $Y \models \phi$.

**Downwards closure:** If $X \models \phi$ and $Y \subseteq X$ then $Y \models \phi$.

**Empty set property:** If $\emptyset$ is the team containing no assignments then $\emptyset \models \phi$ for all dependence logic formulas *φ*.

The locality principle, together with the conservativity principle mentioned at the beginning of this section, constitutes an important “sanity condition” that any variant and extension of dependence logic should satisfy. The same cannot be said about downwards closure and the empty set property, which—as we will see—are violated by variants of dependence logic.

Finally, we need to define the *truth* of a dependence logic sentence with respect to a model. Since a sentence has no free variables, by the locality principle we have at once that either all nonempty teams satisfy it or no nonempty team satisfies it. This is analogous to the case of Tarski’s semantics, in which a sentence is either satisfied by all variable assignments or by none of them. Thus, we can define truth in the usual way:

**Truth in team semantics:** A sentence *φ* is true in a model $M$ if and only if $M, \{\emptyset\} \models \phi$, where $\{\emptyset\}$ is the team containing only the empty assignment. In this case, we write that $M \models \phi$.

### 2.1 Game-theoretic semantics

As mentioned, the game-theoretic semantics for dependence logic is a variant of the imperfect-information semantics for independence-friendly logic, which is itself an adaptation of the game-theoretic semantics of first-order logic. We refer the reader to (Väänänen 2007a)[^väänänen-2007a] for a formal, detailed definition of this semantics.

In game-theoretic semantics, a sentence *φ* and a model $M$ are made to correspond to a (usually two-player) game $G_M(\phi)$. Then truth is defined in terms of the existence of *winning strategies* for one of the players (who, in this work, will be called simply “Player $0$”): in other words, if $\sigma_0$ is a (possibly non-deterministic) strategy for Player $0$ and $\Pi(G_M(\phi), \sigma_0)$ is the set of all plays which are compatible with $\sigma_0$ then *φ* is true if and only if every play in $\Pi(G_M(\phi), \sigma_0)$ is winning for Player $0$. It is possible to think of the game $G_M(\phi)$ as a debate between two players, one of whom (Player $0$) wishes to demonstrate that it is the case that *φ* while the other (Player $1$) wishes to demonstrate that it is not the case that *φ*.

As in the case of first-order logic and independence-friendly logic, in the imperfect-information game for dependence logic the positions of the game are pairs $(\theta, s)$, where *θ* is an instance of a subformula of *φ* (that is, multiple occurrences of the same expression as a subformula of *φ* are to be considered separately) and $s$ is a variable assignment over the model $M$.[^note-1] The initial position is $(\phi, \emptyset)$, where $\emptyset$ is the empty assignment; and a non-deterministic strategy $\sigma_0$ for Player $0$ selects, for every disjunction and existential quantification, one or more *successors* of the current position according to the following rules:

- If the current position is of the form $(\psi \lor \theta, s)$ then its successors are $(\psi, s)$ and $(\theta, s)$;
- If the current position is of the form $(\exists v \psi, s)$ then its successors are all positions $(\psi, s')$ with $s' \sim_v s$.

Similarly, the successors of $(\psi \land \theta, s)$ are $(\psi, s)$ and $(\theta, s)$, and the successors of $(\forall v \psi, s)$ are all positions of the form $(\psi, s')$ for $s' \sim_v s$; but a strategy for Player $0$ cannot specify a successor for these positions, as it is assumed that Player $1$ chooses which position follows them.

A sequence of positions $\overline \rho = \rho_0 \rho_1 \ldots \rho_n$ is a *play* of $G_M(\phi)$ if and only if

1. $\rho_0 = (\phi, \emptyset)$;
2. For all $i = 1 \ldots n$, $\rho_{i}$ is a successor of $\rho_{i-1}$.

If furthermore $\rho_{i+1} \in \sigma_0(\rho_i)$ whenever $\rho_i$ corresponds to a disjunction or an existential quantifier, we say that $\overline \rho$ *respects* the strategy $\sigma_0$; and as mentioned, we write $\Pi(G_M(\phi), \sigma_0)$ for the set of all plays over $G_M(\phi)$ which respect $\sigma_0$.

We say that a strategy $\sigma_0$ is *winning* if every play $\overline \rho$ which ends in a position $(\alpha, s)$ where *α* is a first-order literal is such that the assignment $s$ satisfies *α* in the usual sense of Tarski’s semantics. Dependence atoms—and the plays which ends in dependence atoms—are of no relevance for deciding whether a given strategy is winning. However, they are used to specify whether a given strategy is *uniform*:

**Uniformity condition** A strategy $\sigma_0$ for $G_M(\phi)$ is uniform if any two plays $\overline \rho, \overline \gamma \in \Pi(G_M(\phi), \sigma_0)$ which end in two positions $(\eqord(x_1 \ldots x_n, y), s)$, $(\eqord(x_1 \ldots x_n, y), s')$ for the same instance of the dependence atom $\eqord(x_1 \ldots x_n, y)$ we have that

$$\textrm{If } s(x_1)\ldots s(x_n) = s'(x_1) \ldots s'(x_n) \textrm{ then } s(y) = s'(y).$$

Then we can define truth in game-theoretic semantics as follows:

**Truth in game-theoretic semantics:** A sentence *φ* is true in a model $M$ (with respect to game-theoretic semantics) if and only if Player $0$ has a uniform winning strategy in $G_M(\phi)$.

It can be shown that this notion is equivalent to the notion of truth in team semantics. In fact, we can show more than this. If, for any team $X$ and formula *φ*, the game $G_{M,X}(\phi)$ is played as $G_M(\phi)$ but with the initial position chosen randomly for every play from $\{(\phi, s) : s \in X\}$, then the following holds:

**Equivalence of GTS and team semantics:** A formula *φ* is satisfied by a team $X$ (with respect to a model $M$) if and only if Player $0$ has a uniform winning strategy in $G_{M,X}(\phi)$.

This result, as an aside, makes it clear why the team semantics of dependence logic satisfies the empty set property and the downwards closure property. Indeed, if $X = \emptyset$ then every strategy for Player $0$ in $G_{M, X}(\phi)$ is trivially winning and uniform; and if $X \subseteq Y$ then any uniform winning strategy for Player $0$ in $G_{M, X}(\phi)$ is also a uniform winning strategy for Player $0$ in $G_{M, Y}(\phi)$.

## 3. Properties

### 3.1 Expressivity

Sentence-wise, dependence logic is equivalent to the existential fragment $\Sigma_1^1$ of second-order logic. More precisely, it can be proved (Väänänen 2007a)[^väänänen-2007a] that

**Sentence-wise equivalence of dependence logic and $\Sigma_1^1$:** For every dependence logic sentence *φ* there exists a $\Sigma_1^1$ sentence $\phi^*$ such that

$$\tag{6}\label{eq:DLESO} M \models \phi \Leftrightarrow M \models \phi^* \textrm{ for all models } M. $$

Similarly, for every $\Sigma_1^1$ sentence $\phi^*$ there exists a dependence logic sentence *φ* such that ($\ref{eq:DLESO}$) holds.

Since Fagin’s Theorem (Fagin 1974)[^fagin-1974] shows that a property of finite models is definable in $\Sigma_1^1$ if and only if it is recognizable in polynomial time by a nondeterministic Turing machine (that is, if and only if it is in NPTIME), it follows at once that

**Dependence logic and NPTIME:** For any dependence logic sentence *φ*, the class of all finite models which satisfy it is in NPTIME. Furthermore,for any NPTIME class $\mathcal K$ of finite models, there exists a dependence logic sentence *φ* such that $M \models \phi$ if and only if $M \in \mathcal K$.

Another direct consequence of the equivalence between dependence logic and $\Sigma_1^1$ on the level of sentences is that the compactness theorem and the Löwenheim-Skolem theorem both hold for dependence logic too (Väänänen 2007a)[^väänänen-2007a]:

**Compactness:** If a set *Φ* of finite dependence logic sentences is not satisfiable in any model then some finite subset $\Phi_0 \subseteq_f \Phi$ of it is already not satisfiable.

**Löwenheim-Skolem theorem:** If a dependence logic sentence has an infinite model then it has models of all infinite cardinalities.

However, matters are more delicate when it comes to formulas with free variables. Then it is possible to show (Kontinen & Väänänen 2009)[^kontinen-2009][^kontinen-2009-2] that dependence logic corresponds to the *downwards-closed* fragment of existential second order logic:

**Team definability in dependence logic** A set $\mathcal X$ of teams over a model $M$ and a set $V$ of variables is of the form $\{X : M, X \models \phi\}$ for some dependence logic formula *φ*, with free variables in $V$, if and only if

1. $\mathcal X$ is nonempty;
2. $\mathcal X$ is downwards closed, that is, $Y \subseteq X \in \mathcal X \Rightarrow Y \in \mathcal X$;
3. $\mathcal X$ is $\Sigma_1^1$-definable in $M$, that is, there exists a $\Sigma_1^1$ *sentence* $\Psi(R)$, over the vocabulary of $M$ plus the new $|V|$-ary relation symbol $R$, such that $$X \in \mathcal X \textrm{ if and only if } M, \textrm{Rel}(X) \models \Psi(R)$$ where $\textrm{Rel}(X)$ is the $|V|$-ary relation $\{s(V) : s \in X\}$ which corresponds to the team $X$.

### 3.2 Hierarchies in dependence logic

In (Durand & Kontinen 2012)[^durand-2012], the effect of restricting the number of dependent variables of dependence atoms or the number of universal quantifiers was examined. It was shown that both of these ways of defining fragments of dependence logic give rise of hierarchies:

- For all $k$, let $\mathcal D(k-\forall)$ be dependence logic restricted to at most $k$ universal quantifiers and let $\mathcal D(k-dep)$ be dependence logic restricted to dependency atoms of the form $\eqord(\vec x, y)$ for $|\vec x| \leq k$. Then $$ \begin{align*} \mathcal D(k-\forall) &< \mathcal D(k+1-dep),\\ \mathcal D(k-\forall) &\leq \mathcal D(k-dep) \leq \mathcal D(k+1 - dep) \end{align*} $$ and $$ \mathcal D(k-\forall) < \mathcal D(2k + 2 - \forall) $$ with respect to the expressive power of sentences.

### 3.3 Negation in dependence logic

So far, we assumed that all dependence logic expressions are in negation normal form, and that dependence atoms are never negated. Adding an explicit negation operator to the language of dependence logic, on the other hand, is somewhat problematic, owing to the fact that existential second order logic is not closed under negation. Indeed, the “obvious” negation rule

$$X \models \sim \phi \textrm{ if and only if } X \not \models \phi$$

greatly increases the expressive power of dependence logic, extending it to *team logic* (Väänänen 2007a,b)[^väänänen-2007a], which is, in a very strong sense, equivalent to full second order logic (Kontinen & Nurmi 2009)[^kontinen-2009][^kontinen-2009-2].

A less strong, “dual” negation $\lnot$ can be defined in terms of de Morgan’s rules, $\lnot(\phi \lor [\land] \psi) \equiv (\lnot \phi) \land [\lor] (\lnot \psi)$ and $\lnot (\exists v [\forall v] \phi) \equiv \forall v [\exists v] (\lnot \phi)$, plus the law of double negation $\lnot \lnot \phi \equiv \psi$ and the rule

$$X \models {\lnot \eqord}(\vec x, y) \textrm{ if and only if } X = \emptyset$$

for negations of dependence atoms (Väänänen 2007a,b)[^väänänen-2007a]. The resulting language is expressively equivalent to negation-free dependence logic, and, in fact, the description of dependence logic of (Väänänen 2007a)[^väänänen-2007a] considers this negation as part of its language; however, as shown in (Kontinen & Väänänen 2011)[^kontinen-2011], the satisfaction conditions of a dependence logic formula and those of its negation have little connection to one another. More precisely:

**Dual negation and dependence logic:** For any two dependence logic formulas *φ* and *ψ* such that $\phi \land \psi$ is not satisfiable, there exists a dependence logic formula *θ* such that

$$M, X \models \theta \textrm{ if and only if } M, X \models \phi$$

and

$$M, X \models \lnot \theta \textrm{ if and only if } M, X \models \psi$$

for all models $M$ and teams $X$.

Thus, nothing in general can be said about the dual negation of *φ* except that it is equivalent to some dependence logic expression which is not satisfied by any team which satisfies *φ*. Since, as already mentioned, the law of the excluded middle fails in dependence logic, this is not a very informative property; in particular, it is possible to find in dependence logic (with dual negation) equivalent expressions with non-equivalent negations, like for example $x \not = x \land y \not = y$ and $\lnot\eqord(x,y)$.

### 3.4 Truth, validity and proof systems in dependence logic

Like independence friendly logic, dependence logic can define its own truth operator (Väänänen 2007a)[^väänänen-2007a], that is, if for all formulas *φ* we have that $\lceil \phi\rceil$ is the Gödel number of *φ* then we can find a formula $\tau(x)$, with $x$ as its only free variable, such that

$$M \models \phi \textrm{ if and only if } M \models \tau(\lceil \phi \rceil)$$

for all models $M$ which satisfy Peano’s axioms for natural numbers. This is not in contradiction with Tarski’s undefinability theorem, because dependence logic is not closed under contradictory negation.

The problem of deciding whether a dependence logic sentence is valid (that is, true in all models) is non-arithmetical, and in fact complete with respect to the $\Pi_2$ class of the Levy hierarchy. Nonetheless, the proof theory of dependence logic has been studied. In particular, in (Kontinen & Väänänen 2013)[^kontinen-2013], a sound and complete proof system has been developed for the problem of finding the *first order* consequences of a dependence logic theory.

## 4. Variants of dependence logic

In this section, we will briefly summarize the properties of the most studied variants of dependence logic. Many such variants exist, and much work has been done on their classification and comparison. In this work, we will only mention those variants which are of special significance because of their relationship with dependence logic proper.

### 4.1 Independence Logic

Rather than extending first order logic with dependence atoms $\eqord(\vec x, y)$, independence logic (Grädel & Väänänen 2013)[^grädel-2013] extends it with *independence atoms* $\vec x \mathop{\bot_{\vec z}} \vec y$, whose intended interpretation is “for any possible choice of $\vec z$, the possible values of $\vec x$ and $\vec y$ are independent”—in other words, given any fixed choice of $\vec z$, knowing the value taken by $\vec x$ would not convey any information about the value taken by $\vec y$. This is a notion of significant conceptual importance: for example, one may want to express that—if one does not know the encryption key—seeing the encrypted version of a message carries no information about the corresponding clear-text version. If $x$ represents the encrypted message and $y$ represents the plain-text one, then this corresponds to the condition $x \mathop{\bot} y$, where $\vec z$ in this case is empty. Similarly, if $k$ represents the key then $x \mathop{\bot} k$ represents the claim that the key cannot be inferred from the encrypted message; and the conjunction dependence atom $\eqord(k, x, y)$ (which, as we will soon see, can be represented in independence logic) represents the claim that the plain-text message can be decoded given the encrypted message and the key.

Formally, the satisfaction rule for independence atoms can be given as follows:

**TS-indep:** $M \models_X \vec x \mathop{\bot_{\vec z}} \vec y$ if and only if for all $s, s' \in X$ with $s(\vec z) = s'(\vec z)$ there exists a $s'' \in X$ with $s''(\vec z\, \vec x) = s(\vec{x}\, \vec{z})$ and $s''(\vec y) = s'(\vec y)$.

$$\begin{array}{l | c c c} \textbf{assignment}& \mathbf{x_1} & \mathbf{x_2} & \mathbf{x_3}\\ \hline s_0 & 0 & 0 & 0 \\ s_1 & 0 & 1 & 1 \\ s_2 & 1 & 0 & 1 \\ s_3 & 1 & 1 & 0 \end{array}$$

Independence logic is strictly more expressive than dependence logic: indeed, it lacks the downwards closure property, and the dependence atom $\eqord(\vec x, y)$ is equivalent to the independence atom $y \mathop{\bot_{\vec x}} y$. Furthermore, it can also be shown (Galliani & Väänänen 2014)[^galliani-2014] that conditioned independence atoms $\vec x \mathop{\bot_{\vec y}} \vec z$ can be defined in terms of *unconditional* independence atoms $\vec x \mathop{\bot} \vec y$.

Sentence-wise, independence logic is also equivalent to existential second order logic $\Sigma_1^1$; but formula-wise, it is more expressive, and it was shown in Galliani 2012 that it can capture all nonempty $\Sigma_1^1$-definable team properties.

### 4.2 Inclusion logic

Inclusion logic (Galliani 2012, Galliani & Hella 2013)[^galliani-2012][^galliani-2013] extends first-order logic with *inclusion atoms* $\vec x \subseteq \vec y$, reminiscent of the inclusion dependencies of database theory. Its semantics is:

**TS-inc:** $M \models_X \vec x \subseteq \vec y$ if and only if for all $s \in X$ there exists a $s' \in X$ such that $s(\vec x) = s'(\vec y)$.

$$\begin{array}{l | c c} \textbf{assignment}& \mathbf{x_1} & \mathbf{x_2}\\ \hline s_0 & 0 & 0 \\ s_1 & 0 & 1 \\ s_2 & 1 & 2 \\ s_3 & 2 & 3 \end{array}$$

Differently from dependence and independence logic, inclusion logic is (sentence-wise) strictly weaker than existential second order logic. In fact, it can be shown (Galliani & Hella 2013)[^galliani-2013] to be equivalent to the positive fragment of *greatest fixed point logic*, and, therefore, to capture PTIME properties of models over finite ordered models. Formula-wise, inclusion logic is strictly weaker than independence logic but incomparable with dependence logic: indeed, the satisfiability conditions of its formulas are not downwards closed, but they are *closed by unions* in the sense that

$$M, X_i \models \phi \forall i \in I \Rightarrow M, \bigcup_i X_i \models \phi.$$

### 4.3 Team Logic

Team logic (Väänänen 2007a,b; Kontinen & Nurmi 2009)[^kontinen-2009][^kontinen-2009-2][^väänänen-2007a] extends dependence logic by adding to it a *contradictory negation* $\lnot$. It is equi-expressive with full second order logic, both in terms of definability of classes of models (Väänänen 2007b)[^väänänen-2007b] and with respect to the classes of teams that team logic expressions can define with respect to a given model (Kontinen & Nurmi 2009)[^kontinen-2009][^kontinen-2009-2]. In (Lück 2019), a Hilbert-style axiomatization for Team Logic (and for its modal and propositional equivalents) was found that is complete for its dependence-free fragment (that is, for the fragment in which dependence atoms do not appear).

### 4.4 Intuitionistic Dependence Logic

Intuitionistic dependence logic (Abramsky & Väänänen 2009; Yang 2013)[^abramsky-2009][^yang-2013] extends dependence logic by adding an implication connective $\phi \rightarrow \psi$, whose satisfaction rules are given in team semantics by

**TS-$\rightarrow$:** $X \models \phi \rightarrow \psi$ if and only if for all subsets $Y$ of $X$, if $Y \models \phi$ then $Y \models \psi$.

This operator is called the “intuitionistic implication”, because of the similarity between its semantics and the one of the implication operator in Kripke’s semantics for intuitionistic logic (Kripke 1965)[^kripke-1965]. Its interpretation in terms of belief is quite straightforward: if the assignments in $X$ represent the *states of thing* that some agent believes possible, then a subset $Y$ of $X$ may represent the result of a *belief update* in which the agent rejects some previously believed possible states of thing, and $\phi \rightarrow \psi$ states than any such update that would cause *φ* to hold would also cause *ψ* to hold. From this standpoint, this is a very natural concept which permits us to describe predictions about how such an agent’s overall belief state would react to belief updates.

However, because of the second order universal quantification implicit in its semantics, this connective suffices to greatly increase the expressive complexity of the logic: in particular, as shown in (Yang 2013)[^yang-2013], any sentence of second order logic is equivalent to some sentence of intuitionistic dependence logic. Intuitionistic dependence logic retains the downwards closure property: if a team satisfies an intuitionistic dependence logic formula then so do all of its subsets.

The connections between (extensions of) Intuitionistic Dependence Logic and formal inquisitive semantics has been analyzed in (Ciardelli et al. 2020)[^ciardelli-2020].

### 4.5 Generalized Dependencies and Connectives in Team Semantics

The variants and extensions of Dependence Logic seen above are all generated from First Order Logic (with Team Semantics) by introducing new atoms or connectives. It is possible to consider *generalized dependence atoms* (Kuusisto 2015)[^kuusisto-2015], much in the same way in which generalized quantifiers are introduced in classical First Order Logic, and ask questions like:

- For which collections $\mathcal D$ of atoms or connectives is it the case that $\mathbf{FO}(\mathcal D)$ (i.e., First Order Logic augmented by the atoms and connectives in $\mathcal D$) is expressively equivalent to First Order Logic? Such collections $\mathcal D$ are said to be *strongly first order*.
- Given a collection $\mathcal D$ of atoms and connectives, for which other collections $\mathcal E$ of atoms and connectives is it the case that $\mathbf{FO}(\mathcal D, \mathcal E)$ is expressively equivalent to $\mathbf{FO}(\mathcal D)$? Such $\mathcal E$ are said to be *safe* for $\mathcal D$.

No complete answer to these questions is known at the moment. Some partial results, however, are known:

1. If $\mathcal D$ is a collection of upwards closed dependencies (that is to say, dependencies that, if true of some team $X$ in some model $M$, are also true of any superteam $Y \supseteq X$ in the same model), plus possibly the constancy atom (that is, the already-mentioned special case of the dependence atom that states that some variable is constant over a team), then $\mathcal D$ is strongly first order (Galliani 2015)[^galliani-2015][^galliani-2015-2];
2. Not all strongly first order dependencies are safe for all dependencies: in particular, the constancy atom is not safe for *unary* inclusion dependencies $x \subseteq y$, where $x$ and $y$ are single variables; the possibility operator $\diamond \phi$, which is satisfied by a team $X$ in a model $M$ if and only if there is a nonempty subset of X that satisfies *φ* in $M$, is instead safe for all collections of dependencies, as are the totality atom (that states that some variable, or tuple of variables, takes all possible values) and the non-constancy atom (that states that some variable takes at least two different values in a team) (Galliani 2021)[^galliani-2021];
3. If $\mathcal D$ is a strongly first order collection of dependencies and $\mathcal E$ is a collection of downwards closed dependencies (that is, dependencies that whenever true of some team they are also true of every subteam), then $\mathcal D$ is safe for $\mathcal E$ (Galliani 2019)[^galliani-2019];
4. If $\mathcal D$ is a collection of dependencies that are downwards closed and *relativizable* (that is to say, adding relativizations of dependencies in $\mathcal D$ to unary predicates $P$ to the language is no more expressive than adding the dependencies themselves), then $\mathcal D$ is strongly first order if and only if every dependence in it can be defined in terms of constancy atoms (Galliani 2019)[^galliani-2019].
5. (Somewhat more involved) characterizations are available for the dependencies that are relativizable and safe to add to First Order Logic *together with their contradictory negations* (Galliani 2024)[^galliani-2024] as well as for the ones that are strongly first order, closed by unions, and domain independent (Galliani 2022)[^galliani-2022].

These are all partial results, however, and the general theory of dependencies and connectives in Team Semantics is still in its infancy.

A related topic is the study of extensions of Dependence Logic via generalized quantifiers (Engström 2012)[^engström-2012]. An interesting result along these lines consists in axiomatization for the extension of Dependence Logic via the quantifier $Q$ “there exist uncountably many…”, which is sound and complete for the $\textbf{FO}(Q)$ consequences of a theory (Engström, Kontinen & Väänänen 2017)[^engström-2017][^kontinen-2017].

Also worth pointing out in this context is the work of (Kontinen & Yang 2019)[^kontinen-2019], which found a logic based on Team Semantics (with different choices of connectives than the “standard” ones of Dependence Logic) whose formulas capture precisely the first-order-definable properties of teams; and (Hella et al. 2024)[^hella-2024], in which definability hierarchies are found for generalized dependencies.

### 4.6 Propositional Dependence Logic

The dependence and independence atoms considered so far express relationships between the possible values of *variables* in a set of assignments. However, the same notions of dependence and independence can be equally naturally be applied to proposition themselves, as it happens in natural language expression such as for instance “Whether he will or will not pass the course depends only on the content of his final exam”.

Propositional Dependence Logic consider such atoms within the context of propositional logic. Propositional dependence logic teams are sets of *valuations* $v$ from propositional atoms $p_1 \ldots p_n$ to $\{T, F\}$. Its semantic rules – and their justifications – mirror very closely the ones of first order team semantics, and the rule for dependence atoms is

**PTS-dep:** $X \models \eqord(p_1 \ldots p_n, q)$ if and only if any two valuations $v_1, v_2 \in X$ which agree on the values of $p_1 \ldots p_n$ also agree on the value of $q$.

Many of the variants and generalizations of first order dependence logic can be lowered to the propositional level without any difficulty: thus, for example, it is possible to study the properties of propositional inclusion logic, propositional team logic, propositional intuitionistic dependence logic and so on.

Whereas (first order) dependence logic is strictly more expressive than first order logic, propositional dependence logic is not more expressive than propositional logic, as it follows immediately from the fact that all propositional functions are expressible in propositional logic. There exists, however, a close relation between the teams of propositional dependence logic and the *information states* of *inquisitive logic* (Groenendijk 2009; Ciardelli & Roelofsen 2011)[^ciardelli-2011][^groenendijk-2009], a semantic framework for the study of the notion of meaning and information exchange: in particular, the implication of inquisitive logic is exactly the same as the one of propositional intuitionistic dependence logic.

In (Mahmood and Meier 2020) the complexity of Propositional Dependence Logic and its variants was studied with respect to a number of parametrizations (formula-size, formula-depth, treewidth, team-size, number of variables).

Axiomatizations for propositional dependence logic and many of its extensions can be found in (Yang & Väänänen 2016)[^yang-2016]; and the analysis of the computational complexity of this formalism (and of related propositional logics based on Team Semantics) can be found in (Virtema 2017; Hannula et al. 2018)[^hannula-2018][^virtema-2017].

### 4.7 Modal Dependence Logic

Modal dependence logic (Väänänen 2008)[^väänänen-2008] and its variants extend modal logic by adding to it the same dependence atoms $\eqord(p_1 \ldots p_n, q)$ already considered in the case of propositional dependence logic.

Its satisfaction conditions can be defined through a variant of team semantics in which teams are replaced by *sets* of possible worlds.

Much research has investigated the complexity-theoretic properties of this logic, of its fragments, and its extensions (Ebbing, Lohmann, & Yang 2011; Ebbing & Lohmann 2012; Lohmann & Vollmer 2013)[^ebbing-2012][^lohmann-2013].

Modal Independence Logic has also been investigated in (Kontinen et al, 2017)[^kontinen-2017]; and a modal version of Inclusion Logic was axiomatized in (Anttila et al, 2025)[^anttila-2025].

### 4.8 Linear Temporal Logic with Team Semantics

Linear Temporal Logic may also be given a “Team Semantics” of sorts, in which formulas are evaluated with respect to sets of traces (that is to say, sets of sequences of states), representing possible computations of a system. Such a logical framework can be used for the specification and verification of *hyperproperties* (Krebs et al. 2017, Other Internet Resources; Lück 2020; Gutsfeld et al 2022)[^gutsfeld-2022][^lück-2020], that is to say, properties like “The system terminates within a bounded amount of time” whose truth cannot be ascertained by checking every possible trace of the system on its own but only by looking at the set of all possible traces as a whole.

### 4.9 Quantitative Variants of Team Semantics and Dependence Logic

As teams correspond to sets of assignments, it is natural to consider the possibility of extensions of team semantics in which satisfaction is defined instead with respect to *multiteams* (i.e., multisets of assignments) or *probability distributions* over assignments.

The first possibility has been studied in (Durand et al. 2018a), while the second has been studied in (Durand et al. 2018b). The second work, in particular, has led to interesting connections to problems of descriptive complexity over the reals and metafinite model theory (Hannula et al. 2019, Hannula et al. 2020, Hannula and Virtema 2022)[^hannula-2019][^hannula-2020][^hannula-2022].

A related approach is that of (Grädel and Wilke 2022)[^grädel-2022], in which a variant of Team Semantics over multisets of assignments is studied.

## 5. Applications of dependence logic

### 5.1 Dependence logic and database theory

There is a straightforward connection between the teams of team semantics and the relations studied in relational database theory: given a team $X$ and a tuple of variables $\vec v = v_1 \ldots v_k$ occurring in its assignments, it is possible to define the relation $X(\vec v) = \{\langle s(v_1), \ldots, s(v_n)\rangle : s \in X\}$. Furthermore, the dependency atoms studied in dependence logic and its variants are analogous to – and in many cases, derived from – dependencies considered in database theory such as *functional dependencies* (Väänänen 2007a)[^väänänen-2007a], *multivalued dependencies* (Engström 2012)[^engström-2012], and *inclusion and exclusion dependencies* (Galliani 2012)[^galliani-2012]. The relationship between dependence logic and database theory contributed not only to the further development of dependence logic, but also to that of database theory: for instance, in Hannula & Kontinen 2016 a finite axiomatization of the unrestricted implication problem for inclusion, functional, and embedded multivalued database-theoretic dependencies was found through the study of a similar problem within the context of team semantics.

### 5.2 Dependence logic and belief representation

As discussed in (Yang 2014)[^yang-2014] and (Yang & Väänänen 2016)[^yang-2016], there exists a close connection between (propositional) intuitionistic dependence logic and *inquisitive logic* (Ciardelli & Roelofsen, 2011)[^ciardelli-2011], a framework for the study of meaning and information exchange between agents. More in general, the dependency atoms and connectives of studied in team semantics admit natural interpretations in terms of *belief states* and *belief updates*, as discussed in (Galliani 2015)[^galliani-2015][^galliani-2015-2]. At this time, the exact nature of the relationship between such logics and dynamic-epistemic logic and its variants (Van Ditmarsch, van Der Hoek, & Kooi 2007)[^ditmarsch-2007] is largely unexplored, but there is ample reason to suspect further connections between these two areas of mathematical and philosophical logic.

### 5.3 Dependence logic and Arrow’s theorem

Arrow’s theorem (Arrow 1950)[^arrow-1950] is a profoundly influential result of social choice theory that, in brief, shows that no voting system (that is, no system for converting rankings of individual preferences between alternatives into a global, societal-level preference ranking) exists that can satisfy three reasonable-sounding conditions, namely

- If every voter prefers $A$ to $B$, the group as a whole prefers $A$ and $B$;
- Whether the group as a whole prefers $A$ to $B$ or vice versa depends exclusively on every voter’s preferences concerning $A$ and $B$, and *not* on their preferences concerning other possible alternatives;
- No single voter is a *dictator*, that is, the group’s preferences are not determined by the preferences of any single voter.

As the wording itself suggests, the second and third conditions admit a natural reading in terms of dependence and independence: in fact, as shown in Pacuit & Yang 2016, Arrow’s theorem can be formalized in independence logic and proved in a suitable natural deduction system.

### 5.4 Quantum team logic and Bell’s inequalities

In (Hyttinen, Paolini, & Väänänen 2015)[^hyttinen-2015] a variant of propositional team logic, called *quantum team logic*, is introduced. In this formalism, teams are replaced by *quantum teams*, which differ from the ordinary teams of propositional team logic in that they allow for the values of certain variables to be *indeterminate* with respect to certain valuations and in that they allow for multiple instances of the same valuation (thus adding a quantitative aspect to team semantics). A semantics is then defined over quantum teams for a language that allows for the specification of *inequalities* concerning the probabilities of events, and a sound and complete proof system is developed for it; and finally, it is shown that *Bell’s inequalities* admit counterexamples in this systems, as they do according to the predictions of quantum mechanics and according to experimental evidence (Einstein, Podolsky, & Rosen 1935; Bell 1964; Aspect, Grangier, & Roger 1981)[^aspect-1981][^bell-1964][^einstein-1935], while they do not so in the *classical* version of this framework.

### 5.5 Team Semantics and Counterfactual Reasoning

In (Barbero and Sandu 2021)[^barbero-2021], a generalization of Team Semantics is introduced that can be used to reason about interventionist counterfactuals and causal dependencies. In short, the chief element of this direction of research is to replace teams with *causal teams* which specify explicitly functional dependencies between variables, and then using these specifications to compute the consequences of interventions. (Barbero and Virtema 2023)[^barbero-2023] further generalizes this approach by combining it with Probabilistic Team Semantics in order to reason about probabilistic intervenionist counterfactuals; and (Barbero and Virtema 2024)[^barbero-2024] studies the expressivity capabilities of this family of logics.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=logic-dependence). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/logic-dependence/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=logic-dependence&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/logic-dependence/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- Krebs, Andreas, et al., 2017, “[Team semantics for the specification and verification of hyperproperties](https://arxiv.org/abs/1709.08510)”, manuscript at arXiv.org.
- [Dependence Logic on Wikipedia](https://en.wikipedia.org/w/index.php?title=Dependence_logic&oldid=742549065)

## Related Entries

compositionality | game-theoretic semantics and pragmatics | logic: and games | logic: classical | logic: independence friendly | logic: second-order and higher-order

## Notes（原文脚注）

[^note-1]: Since, for simplicity, we are working with expressions in negation normal form, there is no need of a third element to indicate whether the current subformula is or is not negated as a component of the sentence.

[^abramsky-2009]: Abramsky, Samson and Jouko Väänänen, 2009, “From IF to BI: A Tale of Dependence and Separation”, *Synthese*, 167(2): 207–230. doi:10.1007/s11229-008-9415-6

[^anttila-2025]: Anttila, Aleksi, Matilda Häggblom and Fan Yang, 2025, “Axiomatizing modal inclusion logic and its variants”, *Arch. Math. Logic*. https://doi.org/10.1007/s00153-024-00957-y

[^arrow-1950]: Arrow, Kenneth J., 1950, “A Difficulty in the Concept of Social Welfare”, *The Journal of Political Economy*, pp.328–346. doi:10.1086/256963

[^aspect-1981]: Aspect, Alain, Philippe Grangier and Gérard Roger, 1981, “Experimental Tests of Realistic Local Theories via Bell’s Theorem”, *Physical Review Letters*, 47(7): 460–463. doi:10.1103/PhysRevLett.47.460

[^barbero-2021]: Barbero, Fausto and Gabriel Sandu, 2021, “Team Semantics for Interventionist Counterfactuals: Observations vs. Interventions”, *Journal of Philosophical Logic*, 50: 471–521. doi:10.1007/s10992-020-09573-6

[^barbero-2023]: Barbero, Fausto and Jonni Virtema, 2023, “Strongly complete axiomatization for a logic with probabilistic interventionist counterfactuals”, *Logics in Artificial Intelligence. JELIA 2023*. doi:10.1007/978-3-031-43619-2_44

[^barbero-2024]: –––, 2024, “Expressivity landscape for logics with probabilistic interventionist counterfactuals”, *32nd EACSL Annual Conference on Computer Science Logic, CSL 2024*, Vol. 288. doi:10.4230/LIPIcs.CSL.2024.15

[^bell-1964]: Bell, J.S., 1964, “On the Einstein-Podolsky-Rosen Paradox”, *Physics*, 1(3): 195–200.

[^ciardelli-2011]: Ciardelli, Ivano and Floris Roelofsen, 2011, “Inquisitive Logic”, *Journal of Philosophical Logic*, 40(1): 55–94. doi:10.1007/s10992-010-9142-6

[^ciardelli-2020]: Ciardelli, Ivano, Iemhoff Rosalie, and Yang, Fan, 2020, “Questions and Dependency in Intuitionistic Logic”, *Notre Dame Journal of Formal Logic*, 61(1): 75– 115. doi:10.1215/00294527-2019-0033

[^ditmarsch-2007]: van Ditmarsch, Hans, Wiebe van der Hoek, and Barteld Kooi, 2007,*Dynamic Epistemic Logic*, (Synthese Library 337), Dordrecht: Springer. doi:10.1007/978-1-4020-5839-4

[^durand-2012]: Durand, Arnaud and Juha Kontinen, 2012, “Hierarchies in Dependence Logic”, *ACM Transactions on Computational Logic (TOCL)*, 13(4): 1–21. doi:10.1145/2362355.2362359

[^durand-2018]: Durand, Arnaud, et al., 2018, “Approximation and dependence via multiteam semantics”, *Annals of Mathematics and Artificial Intelligence*, 83(3): 297–320.

[^durand-2018-2]: Durand, Arnaud, et al., 2018, “Probabilistic team semantics”, *International Symposium on Foundations of Information and Knowledge Systems*, Cham: Springer.

[^ebbing-2012]: Ebbing, Johannes and Peter Lohmann, 2012, “Complexity of Model Checking for Modal Dependence Logic”, *SOFSEM 2012: International Conference on Current Trends in Theory and Practice of Computer Science*, (Lecture Notes in Computer Science, 7147), Berlin, Heidelberg: Springer, pp. 226–237. doi:10.1007/978-3-642-27660-6_19

[^ebbing-2013]: Ebbing, Johannes, Peter Lohmann, and Fan Yang, 2013, “Model Checking for Modal Intuitionistic Dependence Logic”, *International Tbilisi Symposium on Logic, Language, and Computation 2011*, (Lecture Notes in Computer Science, 7758), Berlin, Heidelberg: Springer, pp. 231–256. doi:10.1007/978-3-642-36976-6_15

[^einstein-1935]: Einstein, A., B. Podolsky and N. Rosen, 1935, “Can Quantum-Mechanical Description of Physical Reality be Considered Complete?” *Physical Review*, 47(10): 777–780. doi:10.1103/PhysRev.47.777

[^engström-2012]: Engström, Fredrik, 2012, “Generalized Quantifiers in Dependence Logic”, *Journal of Logic, Language and Information*, 21(3): 299–324. doi:10.1007/s10849-012-9162-4

[^engström-2017]: Engström, Fredrik, Juha Kontinen, and Jouko Väänänen, 2017, “Dependence logic with generalized quantifiers: Axiomatizations”, *Journal of Computer and System Sciences*, 88: 90–102.

[^fagin-1974]: Fagin, Ronald, 1974, “Generalized First-Order Spectra and Polynomial-Time Recognizable Sets”, *Complexity of Computation* (SIAM-AMS Proceedings 7), Richard M. Karp (ed.), Providence, RI: American Mathematical Society, pp. 27–41.

[^galliani-2012]: Galliani, Pietro, 2012, “Inclusion and Exclusion Dependencies in Team Semantics—On Some Logics of Imperfect Information”, *Annals of Pure and Applied Logic*, 163(1): 68–84. doi:10.1016/j.apal.2011.08.005

[^galliani-2015]: –––, 2015, “The Doxastic Interpretation of Team Semantics”, *Logic Without Borders: Essays on Set Theory, Model Theory, Philosophical Logic and Philosophy of Mathematics* (Ontos Mathematical Logic, 5), Åsa Hirvonen, Juha Kontinen, Roman Kossak, and Andrés Villaveces (eds), Berlin, Boston: De Gruyter, pp. 167–192. doi:10.1515/9781614516873.167

[^galliani-2015-2]: –––, 2015, “Upwards closed dependencies in team semantics”, *Information and Computation*, 245: 124–135.

[^galliani-2019]: –––, 2019, “Characterizing downwards closed, strongly first-order, relativizable dependencies”, *The Journal of Symbolic Logic*, 84(3): 1136–1167

[^galliani-2021]: –––, 2021, “Safe dependency atoms and possibility operators in team semantics.” *Information and Computation*, 278: 104593.

[^galliani-2022]: –––, 2022, “Strongly First Order, Domain Independent Dependencies: The Union-Closed Case.” *Logic, Language, Information, and Computation*, 263–279.

[^galliani-2024]: –––, 2024, “Doubly strongly first-order dependencies.” *Journal of Logic and Computation*, exae056.

[^galliani-2013]: Galliani, Pietro and Lauri Hella, 2013, “Inclusion Logic and Fixed Point Logic”, *Computer Science Logic 2013* (Leibniz International Proceedings in Informatics: LIPIcs 23), Dagstuhl, Germany: Schloss Dagstuhl-Leibniz-Zentrum fuer Informatik, pp. 281–295. doi:10.4230/LIPIcs.CSL.2013.281

[^galliani-2014]: Galliani, Pietro and Jouko Väänänen, 2014, “On Dependence Logic”, in *Johan van Benthem on Logic and Information Dynamics* (Outstanding contributions to logic, 5), Alexandru Baltag and Sonja Smets (eds), Cham: Springer, pp. 101–119. doi:10.1007/978-3-319-06025-5_4

[^grädel-2013]: Grädel, Erich and Jouko Väänänen, 2013, “Dependence and Independence”, *Studia Logica*, 101(2): 399–410. doi:10.1007/s11225-013-9479-2

[^grädel-2022]: Grädel, Erich and Richard Wilke, 2022, “Logics with multiteam semantics”, *ACM Transactions on Computational Logic (TOCL)*, 23(2): 1–30. doi:10.1145/3487579

[^groenendijk-2009]: Groenendijk, Jeroen, 2009, “Inquisitive Semantics: Two Possibilities for Disjunction”, in Peter Bosch, David Gabelaia, & Jérôme Lang (eds), *Seventh international Tbilisi Symposium on Language, Logic, and Computation* (Lecture Notes in Computer Science: Volume 5422), Springer-Verlag, pp. 80–94. doi:10.1007/978-3-642-00665-4_8

[^gutsfeld-2022]: Gutsfeld, Jens Oliver, Meier, Arne, Ohrem, Christoph and Virtema, Jonni, 2022, “Temporal Team Semantics Revisited”. *LICS ‘22: Proceedings of the 37th Annual ACM/IEEE Symposium on Logic in Computer Science*, 44. doi:10.1145/3531130.3533360

[^hannula-2016]: Hannula, Miika and Juha Kontinen, 2016, “A Finite Axiomatization of Conditional Independence and Inclusion Dependencies”. *Information and Computation*, 249: 121–137. doi:10.1016/j.ic.2016.04.001

[^hannula-2018]: Hannula, Miika, et al., 2018, “Complexity of propositional logics in team semantic”, *ACM Transactions on Computational Logic*, 19(1): 1–14.

[^hannula-2019]: –––, 2019, “Facets of distribution identities in probabilistic team semantics”, in F. Calimeri, N. Leone, and M. Manna (eds.), *Logics in Artificial Intelligence*, Cham: Springer.

[^hannula-2020]: –––, 2020, “Descriptive complexity of real computation and probabilistic independence logic”, *Proceedings of the 35th Annual ACM/IEEE Symposium on Logic in Computer Science*, Association for Computing Machinery, New York: 550–563.

[^hannula-2022]: Hannula, Miika and Virtema, Jonni, “Tractability frontiers in probabilistic team semantics and existential second-order logic over the reals”, *Annals of Pure and Applied Logic* 173(1): 103108. doi:10.1016/j.apal.2022.103108.

[^hella-2024]: Hella, Lauri, Kerkko Luosto and Jouko Väänänen, 2024, “Dimension in team semantics”, *Mathematical Structures in Computer Science*, 34(5): 410–454. doi:10.1017/S0960129524000021

[^henkin-1961]: Henkin, Leon, 1961, “Some Remarks on Infinitely Long Formulas”, in *Infinitistic Methods* (Proceedings of the Symposium on the Foundations of Mathematics, Warsaw, 1959), Oxford: Pergamon Press, pp. 167–183.

[^hodges-1997]: Hodges, Wilfrid, 1997, “Compositional Semantics for a Language of Imperfect Information”, *Logic Journal of the IGPL*, 5(4): 539–563. doi:10.1093/jigpal/5.4.539

[^hyttinen-2015]: Hyttinen, Tapani, Gianluca Paolini and Jouko Väänänen, 2015, “Quantum Team Logic and Bell’s Inequalities”, *The Review of Symbolic Logic*, 8(4): 722–742. doi:10.1017/S1755020315000192

[^kontinen-2009]: Kontinen, Juha and Ville Nurmi, 2009, “Team Logic and Second-Order Logic”, in *Proceedings of the 16th International Workshop on Logic, Language, Information, and Computation* (Lecture Notes in Computer Science, 5514), Berlin, Heidelberg: Springer, pp. 230–241. doi:10.1007/978-3-642-02261-6_19

[^kontinen-2009-2]: Kontinen, Juha and Jouko Väänänen, 2009, “On Definability in Dependence Logic”, *Journal of Logic, Language and Information*, 18(3): 317–332.doi:10.1007/s10849-009-9082-0

[^kontinen-2011]: –––, 2011, “A Remark on Negation in Dependence Logic”, *Notre Dame Journal of Formal Logic*, 52(1): 55–65. doi:10.1215/00294527-2010-036

[^kontinen-2013]: –––, 2013, “Axiomatizing First-Order Consequences in Dependence Logic”, *Annals of Pure and Applied Logic*, 164(11): 1101–1117. doi:10.1016/j.apal.2013.05.006

[^kontinen-2017]: Kontinen, Juha, et al., 2017, “Modal independence logic”, *Journal of Logic and Computation*, 27(5): 1333–1352.

[^kontinen-2019]: Kontinen, Juha and Fan Yang, 2019, “Logics for first-order team properties”, *International Workshop on Logic, Language, Information, and Computation*, Berlin, Heidelberg: Springer.

[^kripke-1965]: Kripke, Saul A., 1965, “Semantical Analysis of Intuitionistic Logic I”, in *Formal Systems and Recursive Functions: Proceedings of the Eighth Logic Colloquium, Oxford July 1963* (Studies in Logic and the Foundations of Mathematics, 40), John N. Crossley and Michael A. E. Dummett (eds.), North Holland, pp. 92–130. doi:10.1016/S0049–237X(08)71685-9

[^kuusisto-2015]: Kuusisto, Antti, 2015, “A double team semantics for generalized quantifiers”, *Journal of Logic, Language and Information*, 24(2): 149–191.

[^lohmann-2013]: Lohmann, Peter and Heribert Vollmer, 2013, “Complexity Results for Modal Dependence Logic”, *Studia Logica*, 101(2): 343–366. doi:10.1007/s11225-013-9483-6

[^lück-2018]: Lück, Martin, 2018, “Axiomatizations of team logics”, *Annals of Pure and Applied Logic*, 169(9): 928–969.

[^lück-2020]: –––, 2020, “On the complexity of linear temporal logic with team semantics”, *Theoretical Computer Science*, 837: 1–25.

[^pacuit-2016]: Pacuit, Eric and Fan Yang, 2016, “Dependence and Independence in Social Choice: Arrow’S Theorem”, in *Dependence Logic*, Samson Abramsky, Juha Kontinen, Jouko Väänänen, and Heribert Vollmer (eds), Dordrecht: Springer, pp. 235–260. doi:10.1007/978-3-319-31803-5_11

[^väänänen-2007a]: Väänänen, Jouko, 2007a, *Dependence Logic: A New Approach to Independence Friendly Logic*, (London Mathematical Society student texts, 70), Cambridge: Cambridge University Press. doi:10.1017/CBO9780511611193

[^väänänen-2007b]: –––, 2007b, “Team Logic”, in *Interactive Logic: Selected Papers from the 7th Augustus de Morgan Workshop*, (Texts in Logic and Games, 1), Johan van Benthem, Dov Gabbay, and Benedikt Löwe (eds.), Amsterdam: Amsterdam University Press, pp. 281–302.

[^väänänen-2008]: –––, 2008, “Modal Dependence Logic”, *New Perspectives on Games and Interaction* (Texts in Logic and Games, 4), Krzysztof R. Apt and Robert van Rooij (eds), Amsterdam: Amsterdam University Press, pp.237–254.

[^virtema-2017]: Virtema, Jonni, 2017, “Complexity of validity for propositional dependence logics”, *Information and Computation*, 253: 224–236.

[^yang-2013]: Yang, Fan, 2013, “Expressing Second-Order Sentences in Intuitionistic Dependence Logic”, *Studia Logica*, 101(2): 323–342. doi:10.1007/s11225-013-9476-5

[^yang-2014]: –––, 2014, “On Extensions and Variants of Dependence Logic: A Study of Intuitionistic Connectives in the Team Semantics Setting”. PhD Thesis, University of Helsinki.

[^yang-2016]: Yang, Fan and Jouko Väänänen, 2016, “Propositional Logics of Dependence”, *Annals of Pure and Applied Logic*, 167(7): 557–589. doi:10.1016/j.apal.2016.03.003
