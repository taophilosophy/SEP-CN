# Dynamic Semantics
**First published Mon Aug 23, 2010; substantive revision Tue Jul 12, 2016**

*Nouwen, Rick, Brasoveanu, Adrian, van Eijck, Jan, Visser, Albert*

Dynamic semantics is a perspective on natural language semantics that emphasizes the growth of information in time. It is an approach to meaning representation where pieces of text or discourse are viewed as instructions to update an existing context with new information, the result of which is an updated context. In a slogan: meaning is context change potential.

It is important to be aware of the abstractness of this perspective so as to guard against various non sequiturs. For one thing, one could easily think that dynamic semantics or update semantics is committed at least in part to an internalist idea of semantics since the information states are “internal”—in the sense that they are wholly contained in the individual mind/brain. In other words, one might think that the information states of dynamic semantics are what Putnam (1975)[^putnam-1975] calls “states in the sense of methodological solipsism”. See the entries on scientific realism, computational theory of mind, externalism about mental content, and narrow mental content. However, the general framework says nothing about what the states are. The state could very well include the environment in which the interpreter is embedded and thus contain an “external” component.

A second possible misunderstanding is that dynamic semantics or update semantics is in complete opposition to classical truth conditional semantics (compare the entries on classical logic and first-order model theory). In fact, as this entry will soon make clear, what dynamic semantics provides is a generalization of truth conditional semantics rather than a radically different alternative. The classical meanings become the *preconditions* for success of the discourse actions. Dynamic semanticists claim that *compositional meanings* have the nature of functions or relations and the classical meanings are recoverable from the relational dynamic meanings as *projections* onto their “input” coordinate.

The point of the use of an abstract framework is not to give empirical predictions. This is the task of specific realizations inside the framework. The framework of dynamic semantics (i) provides a direction of thinking and (ii) allows us to import methods from the mathematical study of the framework. It follows that the question whether natural language meaning is intrinsically dynamic does not have an empirical answer. Still, what can be said is that the study of interpretation as a linearly-ordered process has proven quite fruitful and rewarding.

Since dynamic semantics focuses on the discourse actions of sender and receiver, it is in a sense close to use-oriented approaches to meaning in philosophy such as the work of Wittgenstein and Dummett. However, easy identifications between dynamic semantics and these approaches are to be avoided. Dynamic semantics as an abstract framework is compatible with many philosophical ways of viewing meaning and interpretation. Dynamic semantics aims to *model* meaning and interpretation. You can do that without answering broader philosophical questions such as the question of what it is that makes it possible for the subject to be related to these meanings at all. For example, in dynamic predicate logic we take the meaning of *horse* as given without making any substantial claim about what it means for a subject to have the concept of *horse*; we just stipulate the subject has it. This is not to say such questions—which are at the center of the work of Wittgenstein and Dummett—should not ultimately be answered: it’s just that a model can be of interest even if it does not answer them. (Note that dynamic semantics tries to give a systematic and compositional account of meaning, which makes it markedly different in spirit from Wittgenstein’s later philosophy.)

One approach to dynamic semantics is *discourse representation theory* (DRT, Kamp 1981)[^kamp-1981]. (Closely related to Kamp’s approach is Irene Heim’s *file change semantics* (FCS, Heim 1983a)[^heim-1983a] and the discourse semantics of Seuren 1985). Meanings in DRT are so-called *discourse representation structures* (DRSs). These structures are a type of database that contains specific pieces of information. In and of itself a DRS is a static object, but DRT can be said to be a dynamic semantic framework because it allows us to understand the process of composing meanings as a process of *merging* discourse representation structures. In this way, information change becomes an integral part of the interpretation process.

Our main focus in this entry is a second approach to dynamic semantics, although we will compare things to DRT along the way. In this second approach, dynamic meanings are types of actions, things that are individuated by the changes they effect. This is the approach associated with *dynamic predicate logic* (DPL, Groenendijk and Stokhof 1991a)[^groenendijk-1991a]. According to this dynamic semantic tradition, a meaning is a specification of how a receiver’s information state would be modified. It could for instance be a function that maps an old information state to one which has been *updated* with the information that the meaning embodies. Alternatively, it could be a relation that expresses the kind of information change that the meaning brings about. (For early work in this tradition, see Groenendijk and Stokhof 1991a,b; Muskens 1991; Dekker 1993; Vermeulen 1993; van Eijck 1994; Vermeulen 1994; Krahmer 1995; van den Berg 1996; Groenendijk et al. 1996; Aloni 1997; Muskens et al. 1997)[^aloni-1997][^berg-1996][^dekker-1993][^eijck-1994][^groenendijk-1991a][^groenendijk-1996][^krahmer-1995][^muskens-1991][^muskens-1997][^vermeulen-1993][^vermeulen-1994].

## 1. Interpretation as a Process

Interpretation of declarative sentences can be viewed as a product or as a process. In the product perspective, one focuses on the notion of truth in a given situation. In the process perspective, interpretation of a proposition is viewed as an information updating step that allows us to replace a given state of knowledge by a new, more accurate knowledge state. Dynamic semantics focuses on interpretation as a process.

### 1.1 Update Semantics

Update semantics is a particular way in which the interpretation-as-process idea can be implemented. The central idea behind update semantics is very simple. We start with a simple model of a hearer/receiver who receives items of information sequentially. At every moment the hearer is in a certain state: she possesses certain information. This state is modified by the incoming information in a systematic way. We now analyze the meaning of the incoming items as their contribution to the change of the information state of the receiver. Thus, meanings are seen as actions, or, more precisely, as *action types*: They are not the concrete changes of some given state into another, but what such concrete changes have in common.

### 1.2 Propositional Logic as an Update Logic

Propositional logic (the logic of negation, disjunction and conjunction) can be viewed as an update logic as follows. Consider the case where we have three basic propositions $p, q$ and $r$, and we know nothing about their truth. Then there are eight possibilities: $\{ \bar{p} \bar{q} \bar{r}, p \bar{q} \bar{r}, \bar{p} q \bar{r}, \bar{p} \bar{q} r, pq \bar{r}, p \bar{q} r, \bar{p} qr, pqr \}$ Here $\bar{p} \bar{q} \bar{r}$ should be read as: none of $p, q, r$ is true, $p \bar{q} \bar{r}$ as: $p$ is true but $q$ and $r$ are false, and so on. If now $\neg p$ (“not $p$”) is announced, four of these disappear, and we are left with $\{\bar{p} \bar{q} \bar{r}, \bar{p} q \bar{r}, \bar{p} \bar{q} r, \bar{p} qr\}$. If next $q \vee \neg r$ (“$q$ or not $r$”) is announced, the possibility $\bar{p} \bar{q} r$ gets ruled out, and we are left with $\{ \bar{p} \bar{q} \bar{r}, \bar{p} q \bar{r}, \bar{p} qr \}$. And so on. We can view the meaning of propositions like $\neg p$ and $q \vee \neg r$ as mappings from sets of possibilities to subsets thereof.

Sets of possibilities represent states of knowledge. In the example, $\{ \bar{p} \bar{q} \bar{r}, p \bar{q} \bar{r}, \bar{p} q \bar{r}, \bar{p} \bar{q} r, pq \bar{r}, p \bar{q} r, \bar{p} qr, pqr \}$ represents the state of complete ignorance about propositions $p, q, r$. Singleton sets like $\{ pq \bar{r} \}$ represent states of full knowledge about these propositions, and the empty set $\varnothing$ represents the inconsistent state that results from processing incompatible statements about $p, q$ and $r$. Here we spell out the dynamic meanings of the statements of our propositional language:

- *Atomic statements*. These are $p, q, r$. The corresponding update action is to select those possibilities from the current context where the letter is not struck out (overlined).
- *Negated statements*. These are of the form $\neg \phi$. The corresponding update action is to select those possibilities from the current context that form the complement of the set of possibilities selected by the $\phi$ statement.
- *Conjunctions of statements*. These are of the form $\phi \wedge \psi$. The corresponding update action is to select those possibilities from the current context that form the intersection of the selections from the current context made by the $\phi$ and the $\psi$ statements.
- *Disjunctions of statements*. These are of the form $\phi \vee \psi$. The corresponding update action is to select those possibilities from the current context that form the union of the selections made by the $\phi$ and the $\psi$ statements.

This gives the meanings of the propositional connectives as operations from an old context representing a state of knowledge to a new context representing the state of knowledge that results from processing the propositional information.

### 1.3 Programming Statements and their Execution

It is instructive to compare the actions of update semantics to programming statements and their execution. Such a comparison provides a first glimpse into how quantification works within a dynamic setting. Programming statements of imperative languages are interpreted (or “executed”) in the context of a machine state, where machine states can be viewed as allocations of values to registers. Assume the registers are named by variables $x, y, z$, and that the contents of the registers are natural numbers. Then the following is a machine state:

$$ \begin{array}{|c|c|}\hline x & 12 \\\hline y & 117 \\\hline z & 3 \\\hline \end{array} $$

If the statement $z := x$ is executed, i.e., “interpreted”, in this state (in C syntax, this statement would have the simpler form $z = x)$, the result is a new machine state:

$$ \begin{array}{|c|c|}\hline x & 12 \\\hline y & 117 \\\hline z & 12 \\\hline \end{array} $$

If the sequence of statements $x := y$; $y := z$ is executed in this state, the result is:

$$ \begin{array}{|c|c|}\hline x & 117 \\\hline y & 12 \\\hline z & 12 \\\hline \end{array} $$

This illustrates that the result of the sequence $z := x$; $x := y$; $y := z$ is that the values of $x$ and $y$ are swapped, with the side effect that the old value of $z$ gets lost. In other words, the meaning of the program $z := x$; $x := y$; $y := z$ can be viewed as a mapping from an input machine state $s$ to an output machine state $s'$ that differs from $s$ in several respects: $s'(x) = s(y)$ and $s'(y) = s(x)$ (that is, the input values of $x$ and $y$ are swapped in the output state), and $s'(z) = s'(y)$.

Now consider the existential quantifier “there exists an $x$ such that $A$”. Suppose we add this quantifier to an imperative programming language. What would be its meaning? It would be an instruction to replace the old value of $x$ by a new value, where the new value has property $A$. We can decompose this into a part “there exists $x$” and a test “$A$”. A formula/instruction is a *test* if the update contributed by it takes the states in the input context one at a time and tests that they satisfy a particular condition. If they do, they are included in the output context; if they don’t, they are discarded. That is, a test is an update that takes an input context and outputs a context that is a subset of the input context. All the formulas of propositional logic in the Propositional logic as an update logic section above are tests.

The two parts “there exists $x$” and the test “$A$” are glued together by sequential composition: “$\exists x$; $A$”. Focusing on the part “$\exists x$”, what would be its natural meaning? An instruction to replace the old value of $x$ by some arbitrary new value. This is again a relation between input states and output states, but the difference with definite assignments like $x := y$ is that now the relation is not a function. In fact, this relational meaning of quantifiers shows up in the well known Tarski-style truth definition for first order logic (compare the entry on Tarski’s truth definitions):

> $\exists x\phi$ is true in a model $M$ relative to a variable assignment $\alpha$ iff (if and only if) there is some variable assignment $\beta$ such that $\beta$ differs from $\alpha$ at most with respect to the value it assigns to $x$ and such that $\phi$ is true in $M$ relative to assignment $\beta$.

Implicit in the Tarskian definition is a relation that holds between assignment $\alpha$ and assignment $\beta$ iff for all variables $y$ that are different from $x$, it is the case that $\alpha(y) = \beta(y)$. This relation is often called a *random reset of x* and is written as [$x$]. For any variable $x$, the binary relation between total assignments [$x$] is an equivalence relation between assignments, i.e., it is a reflexive, symmetric and transitive binary relation. Below, we see how such relations are put to work in a dynamicised version of first order predicate logic.

Adopting [$x$] as the meaning of “$\exists x$”, note that its meaning is quite different in nature from that of a test in that it creates new values in the output context. In contrast, the output context resulting from an update with a test is always a subset of the input context and can therefore never contain anything new relative to the input context.

### 1.4 The notion of *context* in dynamic semantics

Information states are often called *contexts*, since the state is a precondition for the “interpretation”, i.e., semantic evaluation, of expressions in a formal or natural language. The use of the word “context” also makes it clear that we are not interested in the total state of the receiver but only in aspects of it relevant to the interpretation of the expressions/informational items we are focusing on. Thus, meanings are often called *context change potentials* in the dynamic tradition.

Although it is broadly speaking true that the changes brought about by meanings in dynamic semantics concern aspects of *context*, it is important to note that semanticists may mean various things when they talk about context (compare the entries on epistemic contextualism and indexicals), and these different views engender varieties of dynamic semantics that deal with a variety of issues. Some of these issues are: constructing an appropriate mechanism for pronominal reference (compare the entries on anaphora and reference), explaining the semantics of conditionals (compare the entries on conditionals and the logic of conditionals), giving a semantic treatment of the distinction between assertion and presupposition (compare the entries on assertion, speech acts, implicature, pragmatics) and developing a theory of “presupposition projection”, explaining how the interpretation of discourse is influenced and guided by the common ground that exists between speaker and hearer, and developing a theory of how this common ground develops as the discourse proceeds (compare the entries on pragmatics and implicature).

Context plays a role in two separate distinctions. The first distinction is between context and that which modifies the context. Here the context is the information state or a suitable abstraction thereof (compare the entry on semantic conceptions of information). The context modifier is (the meaning of) the received informational item. The information cannot be received without the correct kind of presupposed information state. The proper analogues in classical static predicate logic (compare the entries on classical logic and first-order model theory) are as follows: the information state is an assignment (environment) or a set of assignments, and the received information is a set of assignments. The second distinction is between context and content. Here the context is something like the storage capacity of the receiver and various other features that could influence how new expressions/informational items are interpreted. The content is the (factual, truth conditional) information that is stored. Thus, e.g., the context in this sense could be a set of registers/variables or in DRT/FCS terms, discourse referents or files. The content would then be some set of assignments or, perhaps, world/assignment pairs constraining the values of these discourse referents and the set of worlds that are live candidates for the actual world.

Here is an example to illustrate the distinctions. Suppose we view an information state as a pair of a finite set of discourse referents and a set of world/assignment pairs, where the assignments have as domain the given finite set of discourse referents. Such a state would be a context-in-the-first-sense and the set of discourse referents would be a context-in-the-second-sense. One basic kind of update would be update of content: here we constrain the set of world/assignment pairs, and leave the set of referents constant. A second basic kind of update would be extension of the set of referents: we extend our allocated storage capacity. We modify the given world/assignments pairs to pairs of worlds and extended assignments, where our extended assignments are constrained by the old ones, but take all possible values on the new referents. Thus, the update process in our example is two-dimensional: we have both update of content and update of context-in-the-second-sense.

## 2. Dynamic Predicate Logic

### 2.1. Conceptual Underpinnings

The motivation for a dynamic semantic framework for natural language comes first and foremost from potential dependencies between the reference of a personal pronoun and that of an indefinite noun phrase. The simplest example of such a dependency is that of coreferential discourse anaphora, as in:

- (1) *Mary met a student yesterday. He needed help.*

The observation is that this sequence of sentences has the same meaning as the single sentence:

- (2) *Yesterday, Mary met a student who needed help.*

If we assume that indefinites are existential quantifiers, then the analysis of (2) is easy. It simply says that there exists an $x$ that is a student, that met Mary yesterday and that needed her help then. In predicate logic:

- (3) $\exists x(\texttt{student}(x)\wedge\texttt{met}(m,x)\wedge\texttt{need-help}(x))$

However, a similar analysis is unavailable for the equivalent two-sentence example in (1). This is because interpretation is *compositional* (see the entry on compositionality for discussion) and in our compositional analysis, we will first come to an analysis of *Mary met a student yesterday*, which will have the form $\exists x(\texttt{student}(x)\wedge\texttt{met}(m,x))$. Likewise, the second sentence will correspond to $\texttt{need-help}(x)$. Assuming that the default mode of combining multiple sentences is to conjoin them, we now arrive at:

- (4) $\exists x(\texttt{student}(x)\wedge\texttt{met}(m,x))\wedge\texttt{need-help}(x)$

The final occurrence of $x$ is not bound and so in classical predicate logic, we have not arrived at an equivalent translation for (1) and (2). The upshot is that if we want to account for the equivalence between (1) and (2) within a static semantic framework, we will not be able to maintain a compositional interpretation for individual sentences. We will have to assume that the discourse in (1) is interpreted as a whole.

This is counter-intuitive. We know what the individual sentences in (1) mean and we would like to capture the potential these meanings have in combining with other meanings to form a meaningful whole, one which corresponds to a sequence of sentences. Dynamic semantics allows us to deliver a fully compositional analysis of meaning at the sentential and supra-sentential level. It does so by guaranteeing that in contrast to classical predicate logic, (3) and (4) *are* equivalent in a *dynamic* interpretation of classical predicate logic syntax. In particular, the following is valid in dynamic predicate logic:

$$\exists x(\psi \wedge \phi) \textrm{ iff } \exists x(\psi)\wedge \phi$$

In this kind of dynamic semantics for natural language, the meaning of a sentence does not correspond to a set of truth-conditions, but rather to an action performed on a context. There are two kinds of actions. Predications like $\texttt{need-help}(x)$ or $\texttt{met}(m,x)$ are *tests*. They merely check if every state/assignment in the current context assigns a value to $x$ that satisfies the relevant predicate; if (and only if) this is the case, the test passes the unaltered assignment on to the output context. In contrast, the existential quantifier is not a test. It has the potential to alter the context by randomly resetting the value of its associated variable. So, $\exists x(\psi)$ takes a context, randomly changes the value of $x$ in each assignment in the context and passes these changed assignments on to the output context if they also satisfy the condition contributed by the test $\psi$.

One of the main consequences of this semantics is that the scope of the existential quantifier is in principle limitless. It changes the value of some variable and until a further change to that variable occurs, any subsequent test accesses the particular value that was set. This also means that the semantics of existential quantification can be given without reference to any scope: the meaning of $\exists x$ is the action that takes a context and returns the same context with at most the value of $x$ randomly replaced by another value. (We will work this out in detail below.)

Right now, two senses of the term dynamic semantics (as applied to natural language) emerge. First and foremost, dynamic semantics is the general idea that logical statements do not express truth-conditions but rather actions on contexts (where contexts can be conceptualized in various ways). A second understanding of the term dynamic semantics is a set of theoretical positions taken within debates concerning the semantics of certain natural language phenomena, most notably pronominal anaphora. (See below for a similar take on dynamic semantics with respect to *presupposition*). For the case of anaphora, this theoretical understanding embodies the combination of two hypotheses: (i) pronouns correspond to variables; (ii) indefinites are non-quantificational, they simply contribute a dynamic variable assignment update. As is clear from the second hypothesis, this theoretical use of the term dynamic semantics presupposes the more general view that meanings are actions on contexts.

Before we turn to defining dynamic predicate logic, we should note that the route dynamic semantics takes to account for anaphora is by no means the only one to be found in the literature. We could also choose to give up the idea that pronouns are correspond to variables and instead assign them a more intricate meaning, one akin to that of definite descriptions. In the contemporary tradition, such ideas emerge as early as Quine 1960 and Geach 1962, before being brought to maturity by (especially) Evans (1977, 1980)[^evans-1977][^evans-1980], Parsons (1978, Other Internet Resources), Heim (1990)[^heim-1990], and Elbourne (2001, 2005)[^elbourne-2001][^elbourne-2005]. See Nouwen (forthcoming) for discussion.

### 2.2 Specifying Dynamic Predicate Logic

The previous subsection gave a first glimpse into the basic aim of a dynamic semantic framework, which is to define a logical semantics in which statements express actions and specifically, in which existential quantification has the potential to reset variables, thus *changing* the context. We get our clue about how to do this by examining the definition of existential quantification in ordinary predicate logic. Suppose we work with total assignments on a fixed set of variables $\textsf{VAR}$ over a fixed domain $D$. The set of total assignments $\textsf{ASSIGN}$ is therefore the set of all (total) functions from $\textsf{VAR}$ to $D$.

Let the meaning of atomic formulas like $P(x)$ be the set $F$ of all assignments $\alpha$ such that $\alpha(x)$ is an object satisfying $P$.

Now define: $$ \alpha[x]\beta := \forall v \in \textsf{VAR}\setminus\{x\}\ (\alpha(v) = \beta(v)). $$ So [$x$] is the binary relation “assignment $\beta$ is a result of (at most) resetting the value of the variable $x$ in assignment $\alpha$”. As already mentioned, this is an equivalence relation over variable assignments. Now the meaning $G$ of $\exists x P(x)$, will be: $$ G := \{\alpha \in \textsf{ASSIGN } \mid \exists \beta \in F \alpha[x]\beta \}. $$ Thus, $G$ is the set of assignments that can be successfully reset with respect to $x$ and obtain an assignment in $F$ as a result of this resetting. Viewed differently, $G$ is *the domain of* the relation $R$ given by $$\alpha R\beta := \alpha[x]\beta \textrm{ and } \beta \in F. $$

We could say that $G$ is the precondition for the resetting action $R$. Now the idea of $\textsf{DPL}$ is to take the meaning of $\exists x P(x)$ to be not the precondition $G$ (as in classical static first order logic) but the resetting action $R$. In this way we do not lose information since $G$ can always be obtained from $R$. Moreover, the range of the relation $R$ consists of assignments $\beta$ that differ from assignments in the precondition $G$ at most with respect to the value of $x$ and that are also in $F$ (i.e., $\beta(x)$ is in the interpretation of $P)$. The $x$ values stored in the range of the binary relation $R$ are precisely the $x$ values that satisfy $P$, i.e., the values we were looking for.

More generally, we take as $\textsf{DPL}$-meanings *binary relations* between assignments. Such relations can be seen as (modeling) *resetting actions*. This is an instance of an admittedly simplistic but well-known and useful way of modeling actions: an action is viewed as a relation between the states of the world before the action and the corresponding states after the action.

Here is the full definition. Assume a non-empty domain $D$, a set of variables $\textsf{VAR}$ and a model $\mathcal{M}=\langle D, I\rangle$ of signature $\Sigma$. Atomic conditions $\pi$ are of the form $P(x_0 , \ldots ,x_{n-1})$, where $P\in \Sigma$ is of arity $n$. Atomic resets $\varepsilon$ are of the form $\exists v$, where $v$ is a variable. The language of predicate logic for $\Sigma$ is given below ($\cdot$ is conjunction and ${\sim}$ is negation):

$$ \phi ::= \bot \mid \top \mid \pi \mid \varepsilon \mid \phi \cdot \phi \mid {\sim}(\phi). $$

Assignments are elements $\alpha , \beta ,\ldots$, of $\textsf{ASSIGN} := D^{\textsf{VAR}}$. We define the dynamic/relational semantics for this language as follows:

- $\alpha[\bot]\beta := \alpha \ne \alpha$.
- $\alpha[\top]\beta := \alpha = \beta$.
- $\alpha[P(x_0 , \ldots ,x_{n-1})]\beta := \alpha = \beta$ and $\langle \alpha(x_0), \ldots ,\alpha(x_{n-1})\rangle \in I(P)$, where $P\in \Sigma$ has arity $n$.
- $\alpha[\exists v]\beta := \alpha[v]\beta$
- $\alpha[\phi \cdot \psi]\beta :=$ there is a $\gamma$ such that $\alpha[\phi]\gamma$ and $\gamma[\psi]\beta$, or $\alpha[\phi]\gamma[\psi]\beta$ for short.
- $\alpha[{\sim}(\phi)]\beta := \alpha = \beta$ and there is no $\gamma$ such that $\alpha[\phi]\gamma$.

Note that conjunction $\cdot$ is interpreted as relation composition, and negation ${\sim}$ is basically interpreted as complementation with respect to the domain of the relation denoted by the negated formula.

Truth is defined in terms of relational meanings; we basically project the binary relations between assignments onto their first coordinate:

$$\alpha \vDash \phi := \exists \beta\ \alpha[\phi]\beta.$$

We can define implication $\phi \rightarrow \psi$ as ${\sim}(\phi \cdot {\sim}\psi)$. Applying the truth definition to this gives:

> $\alpha \vDash \phi \rightarrow \psi \textrm{ iff } \forall \beta(\alpha[\phi]\beta \Rightarrow \beta \vDash \psi)$, i.e., any assignment $\beta$ that results from updating $\alpha$ with the antecedent $\phi$ satisfies the consequent $\psi$.

Relational meanings also yield the following beautiful definition of dynamic entailment:

$$\phi \vDash \psi := \forall \alpha , \beta(\alpha[\phi]\beta \Rightarrow \exists \gamma \beta[\psi]\gamma).$$

This definition was first introduced by Hans Kamp in his pioneering paper Kamp 1981. Informally, it says that any assignment $\beta$ that has incorporated the update contributed by $\phi$ is guaranteed to support/satisfy $\psi$.

Note that ${\sim}\phi$ is equivalent to $(\phi \rightarrow \bot)$, and that $(\phi \rightarrow \psi)$ is true iff $\phi \vDash \psi$. Equally importantly, we can define $\forall x (\phi)$ as $(\exists x \rightarrow \phi)$.

A possible alternative notation for $\exists v$ would be [$v := ?$] (random reset). This emphasizes the connection with random assignment in programming languages.

The interpretations of predicate symbols are *conditions*. They are subsets of the diagonal $\{\langle \alpha , \alpha \rangle \mid \alpha \in \textsf{ASSIGN}\}$ (which is the meaning of $\top)$. Subsets of the diagonal are tests: they modify nothing and simply pass on what is OK (satisfies the condition) and throw away what is not. The mapping $\textsf{diag}$ that sends a set $F$ of assignments to a condition $\{\langle \alpha , \alpha \rangle \mid \alpha \in F\}$ is the link between the classical static and the dynamic world. For example, the relational composition of $\textsf{diag}(F)$ and $\textsf{diag}(G)$ is $\textsf{diag}(F\cap G)$.

Classical first-order logic (FOL) can be interpreted in $\textsf{DPL}$ as follows. We assume that the FOL language has the following connectives and quantifiers: $\top , \bot , \wedge , \rightarrow , \exists x$. We translate as follows:

- $( )^*$ commutes with atomic formulas and with $\rightarrow$
- $(\phi \wedge \psi)^* := \phi^* \cdot \psi^*$
- $(\exists x(\phi))^* := \neg \neg(\exists x \cdot \phi^*)$

We get that $[\phi^*]$ is the diagonal of the classical interpretation of $\phi$. Our translation is compositional. It shows that FOL can be taken as a *fragment* of $\textsf{DPL}$.

It is, conversely, possible to translate any $\textsf{DPL}$-formula $\phi$ to a predicate logical formula $\phi$°, such that the domain of $[\phi]$ is the classical interpretation of $\phi$°. One of the ways to define this translation is by means of a precondition calculus, with Floyd-Hoare rules (Eijck and de Vries 1992)[^eijck-1992]. The following is a variation on this. Take the language of standard predicate logic, with diamond modalities $\langle \psi \rangle \phi$ added, where $\psi$ ranges over DPL formulas and $\alpha \vDash \langle \psi \rangle \phi$ iff there is an assignment $\beta$ with $\alpha[\psi]\beta$, and $\beta \vDash \phi$. Then the following equivalences show that this extension does not increase expressive power.

- $\langle \bot \rangle \phi \leftrightarrow \bot$.
- $\langle \top \rangle \phi \leftrightarrow \phi$.
- $\langle P(x_1 \ldots x_n)\rangle \phi \leftrightarrow (P(x_1 \ldots x_n) \wedge \phi)$.
- $\langle \exists v\rangle \phi \leftrightarrow \exists v\phi$.
- $\langle \psi_1 \cdot \psi_2\rangle \phi \leftrightarrow \langle \psi_1\rangle \langle \psi_2\rangle \phi$.
- $\langle{\sim}(\psi)\rangle \phi \leftrightarrow(\neg(\langle \psi \rangle \top) \wedge \phi)$.

So in a weak sense “nothing new happens in $\textsf{DPL}$”. We cannot define a set that we cannot also define in FOL. The equivalences for the modalities fix a translation ( )° that yields the weakest precondition for achieving a given postcondition; see the next section for an illustration of such a translation.

### 2.3 Example: donkey sentences

An example of the merits of dynamic predicate logic is that it allows for a straightforward compositional analysis of donkey sentences (Geach 1962; see the entry on anaphora)[^geach-1962].

- (5) If a farmer owns a donkey, he beats it.

There is obviously a dependency between the pronouns $he$ and $it$ and the indefinites *a farmer* and *a donkey*, respectively. In a nutshell, the problem for (5) in a classical analysis is that such an analysis gives us two choices, which taken together do not cover the possible meanings of (5). If we treat the indefinites as referring to a particular farmer and a particular donkey and the pronouns as simply picking up that same entities, then we get a possible yet not very salient reading for (5). The most prominent reading describes a co-variation between the owning relation and the beating relation: any farmer-donkey pair that stands in the *own* relation also stands in the *beat* relation. Clearly, we will need to interpret the indefinites as quantifiers. Yet if we do so, they won’t be able to bind the variables in the consequent of the conditional since a compositional analysis will place the variables contributed by the pronouns outside the classical scope of the existential quantifiers in the antecedent of the conditional. That is, (6) does not yield the correct truth-conditions for (5).

- (6) $(\exists x(\textrm{farmer}(x)\wedge \exists y(\textrm{donkey}(y)\wedge\textrm{own}(x,y))))\rightarrow\textrm{beat}(x,y)$

The dynamic version of (6) is (7), which yields the correct truth conditions: any random reset of $x$ and $y$ such that $x$ is a farmer and $y$ is a donkey owned by $x$ is also such that $x$ beats $y$.

- (7) $\exists x\cdot \textrm{farmer}(x)\cdot \exists y\cdot \textrm{donkey}(y)\cdot \textrm{own}(x,y)\rightarrow \textrm{beat}(x,y)$

Interestingly, the translation ( )° of (7) into predicate logic is not (6) but (8). So the problem is not that predicate logic cannot express the truth-conditions of donkey conditionals but that sentences like (8) are unlikely to be the end product of a compositional interpretation process (but see Barker and Shan 2008)[^barker-2008].

- (8) $\neg \exists x (\textrm{farmer} (x) \wedge \exists y (\textrm{donkey} (y) \wedge \textrm{own}(x,y) \wedge \neg \textrm{beat}(x,y))).$

This is how (8) is derived from (6):

$$ \begin{array}{l} (\langle(\exists x \cdot Fx \cdot \exists y \cdot Dy \cdot Hxy ) \rightarrow Bxy \rangle \top) ° \\ = (\langle{\sim}((\exists x \cdot Fx \cdot \exists y \cdot Dy \cdot Hxy ) \cdot {\sim} Bxy ) \rangle \top) ° \\ = \neg(\langle(\exists x \cdot Fx \cdot \exists y \cdot Dy \cdot Hxy ) \cdot {\sim} Bxy \rangle \top) ° \\ =\ldots \\ = \neg \exists x (Fx \wedge \exists y (Dy \wedge Hxy \wedge \neg Bxy ))).\\ \end{array} $$

### 2.4 Dynamic generalized quantification

The successful application of dynamic predicate logic to the interaction of quantification and anaphora in natural languages hinges on the fact that in DPL, existential quantification is dynamic whereas universal quantification is not. What would happen if universal quantification were dynamic too? Note first of all, that it makes no sense to define a universal quantification action $\forall x$ in parallel to the random reset action $\exists x$. This is because universal quantification only makes sense on a given domain (the *restrictor*) and with respect to some given property (the *scope*). Second, if we give $\forall x(\phi)(\psi)$ a dynamic interpretation, it predicts that universal quantifiers can stand in anaphoric relations to singular pronouns across clausal boundaries, just as existential quantifiers can. For cases like (9), this is clearly undesirable.

- (9) Every boy wrote an essay. #He wrote a research proposal too.

However, as soon as one looks at *plural anaphora* it becomes apparent that the static nature of universal quantification (and, in fact, that of other non-indefinite generalized quantifiers) should not be taken for granted. For example, (10) allows a reading in which *they* is anaphorically linked to *every boy*.

- (10) Every boy wrote an essay. They wrote a research proposal too.

On the assumption that examples like (10) should receive a dynamic treatment (see the earlier remark on alternative explanations and Nouwen, forthcoming, for discussion), the conclusion can only be that universal quantifiers should not be given a static interpretation. The next question is then what kind of interpretation is appropriate, and how this interpretation can distinguish the infelicitous case of anaphora in (9) from the case in (10). One option would be to distinguish between the values assigned to the variables that are bound by the quantifier in its scope and the value assigned to that variable outside the scope of the quantifier. (See, for instance, Kamp and Reyle 1993 for such a strategy and Nouwen 2007 for discussion.)[^kamp-1993][^nouwen-2007] In order to account for (10), one would have the variable occurrences bound by the quantifier in the first sentence of (10) range over individual boys, while that variable gets assigned the plurality of all boys outside the quantifier’s scope (i.e. in the second sentence). As van den Berg (1996)[^berg-1996] was the first to show, however, such a solution only gets there half-way. In discourse, pronouns do not just have access to pluralities associated to quantifiers, but also to the relations such quantifiers are engaged in. For instance, in the second sentence of (11) the pronoun $it$ covaries with the quantification over the boys in the subject in such a way that the second sentence is understood to mean that each boy submitted the paper that $he$ wrote (cf. van den Berg 1996; Krifka 1996; Nouwen 2003; Brasoveanu 2007, 2008)[^berg-1996][^brasoveanu-2007][^brasoveanu-2008][^krifka-1996][^nouwen-2003].

- (11) Every boy wrote an essay. Each of them submitted it to a journal.

The leading idea in dynamic treatments of generalized quantification and plural anaphora is to represent plural values not by assigning pluralities to variables, but rather to adopt a notion of context that allows for pluralities (e.g., sets) of assignment functions. Say that the first sentence in (11) is translated into dynamic predicate logic with dynamic quantifiers as follows: $\forall x(\textrm{boy}(x))(\exists y\cdot \textrm{essay}(y)\cdot \textrm{wrote}(x,y))$. The interpretation of such formulas requires collecting assignment functions in which the value of $x$ is a boy and the value of $y$ is an essay written by this boy. The universal quantifier requires such collections to include all possible values for the predicate *boy*. In the subsequent discourse, we now have access to the set of all $x$ values, i.e., the set of all boys, the set of all $y$ values, i.e., the set of essays written by the boys, as well as the individual boy-essay pairs: each atomic assignment $f$ in the set of contextual assignments following the first sentence of (11) is such that $f(y)$ is an essay written by boy $f(x)$. All that is now needed to account for the case of anaphora in (11) is the assumption that the universal quantification there involves universal quantification over assignment functions, rather than just quantification over values. See van den Berg (1996)[^berg-1996], Nouwen (2007, forthcoming), Brasoveanu (2007, 2008, 2013)[^brasoveanu-2007][^brasoveanu-2008][^brasoveanu-2013] for various ways of implementing this idea.

The upshot is that given a suitably structured notion of context, quantifiers can be given dynamic interpretations generally. An important consequence is that this kind of analysis extends to non-nominal quantifiers (Brasoveanu 2007)[^brasoveanu-2007]. Cases like (11) could be described as cases of quantificational subordination, and the structured context approach can be seen as designed to offer a window into the mechanism behind subordination. Cases of modal subordination (Roberts 1987, 1989)[^roberts-1987][^roberts-1989], like the famous (12), can receive a parallel treatment.

- (12) A wolf might come in. It may eat you.

The modal *might* introduces a quantifier over possible worlds that takes scope over the indefinite *a wolf*, in the same way that *every boy* takes scope over *an essay* in (11) above. The set of assignment functions that is the output of the update contributed by the first sentence in (12) will therefore store a set of possible worlds contributed by *might* that are epistemically possible relative to the actual world, and a set of wolves that come in in these epistemically accessible worlds. The second sentence in (12) can then further elaborate on the dependency between worlds and wolves requiring at least some of the epistemic possibilities to be such that the corresponding wolf not only comes in but also eats you.

### 2.5 Dynamics beyond anaphora

Although anaphora and presuppositions (see below) are the central linguistic phenomena that may be thought to require a dynamic semantic analysis, in principle any aspect of the context could be the target of a phenomenon that warrants a dynamic analysis of interpretation. Barker’s 2002 treatment of the information provided by vague statements is illustrative. Barker assumes that contexts contain precise standards for vague adjectives like *tall*. A sentence like (19) can then be used in two distinct ways. (19) John is tall. If the information state contains precise (enough) information about what counts as *tall*, then an utterance of (19) may be used to provide information about John’s height. If, however, the hearer has no idea about the appropriate precisification of an expression like *tall* (say, s/he is an alien or a foreigner), but s/he does have information about John’s height, then (19) can be used to provide information about the standard.

## 3. Presupposition

### 3.1 Presupposition and dynamic semantics of connectives

Context plays an important role in presupposition. A sentence like (13) presupposes that John is late. But put this sentence in a context providing this very information, as in (14), and the presupposition disappears. That John is late is *asserted* in (14), not presupposed.

- (13) Mary knows that John is late
- (14) John is late and Mary knows that he is late.

Stalnaker 1973 takes presupposition to be based on presumed common knowledge. Uttering a sentence like (13) *takes for granted* that it is common knowledge that John is late. In this sense, (13) requires the context of utterance to be such that this common knowledge is in place. In contrast, (14) lacks such a requirement simply because the first conjunct in (14) asserts what the second conjunct takes for granted. The crucial assumption made by Stalnaker is that interpretation is incremental in the following sense: for a sentence of the form [$S$1 and $S$2], the interpretation of $S$2 occurs in a context which is already updated with $S$1. Schematically:

- (15) ${C}[{S1 \textrm{ and } S2}] = ({C}[{S1}])({S2})$

Stalnaker’s interpretation of the scheme in (15) is pragmatic: when we encounter a series of clauses in discourse, we interpret these clauses *in light of* a context that is already informed by the interpretation of previous clauses. This idea of incremental interpretation is simple yet powerful and it makes perfect sense for complex discourses with conjunctive interpretations (for instance, coordinations with *and* and simple sequences of declarative sentences). Since the conjuncts in a conjunction have assertoric force, they can be used to update the context in order to create a new local context. The problem is though that presuppositions do not just disappear in conjunctive environments. Just like (14), (16) also lacks the requirement that it should be common knowledge that John is late. But here the first disjunct does not have assertoric force (see, for instance, Schlenker 2009 for discussion)[^schlenker-2009]. It is not obvious what kind of pragmatic rule could account for the lack of a presupposition in (16).

- (16) Either John is not late or Mary does not know that he is late.

Examples like (16) call into question the value of an incremental interpretation schema like (15). On top of that, (15) is rather presumptuous in its assumptions of how interpretation proceeds. Asserting a clause with propositional content $p$ does not automatically make it common knowledge that $p$. Rather, such an assertion should be regarded as a *proposal* to make $p$ common knowledge. Whether or not $p$ becomes common ground is dependent on the willingness of the other interlocutors to accept the proposition (for instance, by not objecting against the assertion). In other words, (15) seems ill-suited for capturing the pragmatics of (the dynamics of) information flow.

A possible way out is to regard (15) not as a pragmatic rule, but rather as a semantic rule, couched in a dynamic notion of interpretation. This was most prominently proposed in Heim 1983b, following Karttunen 1973. Karttunen distinguishes *global contexts*, which are contexts relative to which the current sentence is evaluated, from *local contexts*, which are contexts relative to which the current clause (or potentially some sub-clausal entity) is interpreted. The idea now is that a rule like (15) can express the semantics of *and*. In (15), $C$ is the global context. A crucial part of the semantics of conjunction is that the local context for $S$2 is the update of the global context with $S$1. Thus, there is no presupposition in (14) simply because of the dynamic *semantics* of *and*. All we need to account for the lack of presupposition in (16) is to come up with a semantics for disjunction in which the local context for the second disjunct has already been updated with the negation of the first disjunct; see Krahmer and Muskens 1996 for such an account that also captures interactions between (double) negation and anaphora.

To make things more concrete let us assume that contexts are sets of possible worlds and that an update $C[S]$ of $C$ with a simple clause $S$ is $C\cap p$, where $p$ is the propositional content of $S$: updating $C$ with a clause outputs the $C$ worlds in which the clause is true. The rules in (18) show a Heimian fragment of a dynamic interpretation of the main propositional operators in English.

- (17) ${C}[{\textrm{not } S1}] = {C} \backslash {C}[{S1}]$ ${C}[{S1 \textrm{ and } S2}] = ({C}[{S1}])[{S2}]$ ${C}[{\textrm{If }S1, \textrm{ then } S2}] = ({C}[{\textrm{not }S1}]) \cup ({C}[{S1}])[{S2}]$ ${C}[{S1 \textrm{ or } S2}] = {C}[{S1}] \cup ({C}[{\textrm{not }S1}])[{S2}]$

Some question the explanatory value of such a dynamic interpretation in the sense that the framework fails to account for why there appear to be no natural language expressions that encode a minimal variation of (17), where the local context of the second disjunct $S$2 is $C[S1]$ instead of $C[\textrm{not }S1]$, or where the local context of $S$1 is based on an update with $S$2, or where there are no local contexts at all as in (18) (see, for instance, Soames 1989)[^soames-1989].

- (18) ${C}[{S1 \textrm{ or } S2}] = {C}[{S1}] \cup {C}[{S2}]$

In light of such criticisms, there has been a recent resurgence of static approaches to presupposition projection, such as the pragmatic approaches of Schlenker (2008, 2009)[^schlenker-2008][^schlenker-2009], Chemla (2008, Other Internet Resources) and the semantic (trivalent) approaches of George (2008)[^george-2008] and Fox (2008)[^fox-2008]. As Rothschild points out though, there is a route to making a semantics along the lines of (17) explanatory. To do so, one has to show that permissible dynamic interpretations of connectives share certain properties. As Rothschild (2011)[^rothschild-2011] shows, an explanatory and empirically adequate dynamic treatment of presupposition is possible if we assume that context change potentials adhere to certain principles of definedness. Let us assume that $C[S]$ (for a simple clause $S$) is only defined if and only if any presupposition of $S$ is true in all the worlds in $C$. The rules in (17) determine the definedness conditions for complex statements. For instance, according to (17) [not S] is only undefined in $C$ if $S$ is undefined in $C$. Rothschild’s insight is that we can constrain dynamic interpretation by constraining the resulting definedness conditions.

### 3.2 Presuppositions and Dynamic Epistemic Logic

Epistemic logic, the logic of knowledge, is a branch of modal logic where the modality “$i$ knows that” is studied (compare the entries: epistemic logic, logic of belief revision). The dynamic turn in epistemic logic, which took place around 2000, introduced a focus on change of state, but now with states taken to be representations of the knowledge of a set of agents.

If we fix a set of basic propositions $P$ and a set of agents $I$, then a knowledge state for $P$ and $I$ consists of a set $W$ of possible worlds, together with a valuation function $V$ that assigns a subset of $P$ to each $w$ in $W$ (if $w \in W$, then $V(w)$ lists the basic propositions that are true in $w)$ and for each agent $i \in I$, a relation $R_i$ stating the epistemic similarities for $i$ (if $wR_i w'$, this means that agent $i$ cannot distinguish world $w$ from world *w$'$*). Epistemic models $M = (W, V, \{R_i \mid i \in I\})$ are known as multimodal Kripke models. Pointed epistemic models are epistemic models with a designated world $w_0$ representing the actual world.

What happens to a given epistemic state $(M, w_0) = ((W, V, \{ R_i \mid i \in I\}), w_0)$ if a public announcement $\phi$ is made? Intuitively, the world set $W$ of $M$ is restricted to those worlds $w \in W$ where $\phi$ holds, and the valuation function $V$ and epistemic relations $R_i$ are restricted accordingly. Call the new model $M\mid\phi$. In case $\phi$ is true in $w_0$, the meaning of the public announcement $\phi$ can be viewed as a map from $(M, w_0)$ to $(M\mid\phi , w_0)$. In case $\phi$ is false in $w_0$, no update is possible.

Veltman’s update logic can be accommodated in public announcement logic (compare the entry on common knowledge) by allowing public announcements of the form $\Diamond \phi$, where the modality is read as reachability under common knowledge. If an $S$5 knowledge state for a set of agents (compare the entry on epistemic logic) is updated with the public announcement $\Diamond \phi$, then in case $\phi$ is true somewhere in the model, the update changes nothing (for in this case $M\mid\Diamond \phi$ equals $M)$, and otherwise the update yields inconsistency (since public announcements are assumed to be true). This is in accordance with the update logic definition.

The logical toolbox for epistemic logic with communicative updates is called dynamic epistemic logic or DEL. DEL started out from the analysis of the epistemic and doxastic effects of public announcements (Plaza 1989; Gerbrandy 1999)[^gerbrandy-1999][^plaza-1989]. Public announcement is interesting because it creates common knowledge. There is a variety of other kinds of announcements—private announcements, group announcements, secret sharing, lies, and so on—that also have well-defined epistemic effects. A general framework for a wide class of update actions was proposed in Baltag et al. 1999 and Baltag and Moss 2004. A further generalization to a complete logic of communication and change, with enriched actions that allow changing the facts of the world, is provided in Benthem et al. 2006. A textbook treatment of dynamic epistemic logic is given in Ditmarsch et al. 2006.

Within an epistemic logic setting, one may represent the communicative situation of an utterance with presuppositions as follows. First, we need to represent what a speaker assumes about what her audience knows or believes in a multi-agent belief (or knowledge) state, then we need to model the effect of the communicative action on the belief state. A simple way to handle presupposing utterances in dynamic epistemic logic is by modeling a presupposition $P$ as a public announcement “it is common knowledge that $P$”. In cases where it is indeed common knowledge that $P$, an update with this information changes nothing. In cases where $P$ is not common knowledge, however, the utterance is false, and public announcements of falsehoods yield an inconsistent knowledge state.

### 3.3. Beyond presupposition

Dynamic semantics is particularly suitable to describe how different types of linguistic material affect different aspects of the information state. In particular, dynamic semantics allows one to efficiently model the difference between *at-issue* content, e.g., the content that is asserted by the utterance of a declarative sentence and *non-at issue* content, content that plays some secondary role. For instance, the at-issue content of (19) is that John’s neighbor was arrested yesterday: it is the message the speaker intends to assert. The appositive *who I have never met* is not at issue. One way to see this is that an interlocutor can only respond to (19) with *No! That’s not true!* if s/he intends to challenge the fact that the neighbor was arrested, not if s/he merely wishes to express their disbelief in the speaker’s claim of never having met the neighbor.

- (19) John’s neighbour, who I have never met, was arrested yesterday.

Dynamic semantics is a suitable framework for analyzing what goes on when such sentences are interpreted, since it naturally allows the modeling of separate streams of information. For instance, AnderBois et al. 2015 provide an account of sentences like (19) where the matrix sentence updates a local set of possible worlds. The updated set can be seen as a potential candidate for updating the common ground with. In contrast, the appositive directly updates the common ground. Rather than a *proposed* common ground update, it can be seen as an *imposed* update (see Nouwen 2007 for an alternative dynamic logic)[^nouwen-2007]. The ideas of AnderBois et al. 2015 are partly inspired by similar ideas that were successfully applied in the realm of evidentials; see in particular Murray 2014.

## 4. Encoding Dynamics in Typed Logic

Compositionality has always been an important concern in the use of logical systems in natural language semantics (see the entry on compositionality). Through the use of higher order logics (see the entries on second-order and higher-order logics and Church’s type theory), a thoroughly compositional account of, e.g., the quantificational system of natural language can be achieved, as is demonstrated in classical Montague grammar (Montague 1974a,b, 1973; compare the entry on logical form)[^montague-1973][^montague-1974a]. We will review how the dynamic approach can be extended to higher order systems. The link between dynamic semantics and type theory is more like a liaison than a stable marriage: there is no intrinsic need for the connection. The connection is treated here to explain the historical influence of Montague grammar on dynamic semantics.

Most proposals for dynamic versions of Montague grammar develop what are in fact higher order versions of dynamic predicate logic (DPL). This holds for Groenendijk and Stokhof 1990; Chierchia 1992, 1995; Muskens 1994, 1995, 1996; Eijck 1997; Eijck and Kamp 1997; Kohlhase et al. 1996; and Kuschert 2000. These systems all inherit a feature (or bug) from the DPL approach: they make re-assignment destructive. DRT does not suffer from this problem: the discourse representation construction algorithms of Kamp 1981 and Kamp and Reyle 1993 are stated in terms of functions with finite domains, and carefully talk about “taking a fresh discourse referent” to extend the domain of a verifying function, for each new noun phrase to be processed.

In extensional Montague grammar “a man” translates as:

$$\lambda P\exists x(\textrm{man } x \wedge Px).$$

Here $P$, of type $e \rightarrow t$, is the variable for the VP slot: it is assumed that VPs denote sets of entities.

In Dynamic Montague Grammar (DMG) of Groenendijk and Stokhof 1990, the translation of an indefinite NP introduces an anaphoric index. The translation of “a man” is

$$\lambda P\lambda a\lambda a' \cdot \exists x(\textrm{man }x \wedge Pu_i (u_i \mid x) aa').$$

Instead of the basic types e and t of classical extensional Montague grammar, DMG has basic types $e, t$ and $m (m$ for marker). States pick out entities for markers, so they can be viewed as objects of type $m \rightarrow e$. Abbreviating $m \rightarrow e$ as $s$ (for “state”), we call objects of type $s \rightarrow s \rightarrow t$ state transitions. The variable $P$ in the DMG translation of “a man” has type $m \rightarrow s \rightarrow s \rightarrow t$, so VP meanings have been lifted from type $e \rightarrow t$ to this type. Note that $\rightarrow$ associates to the right, so $m \rightarrow s \rightarrow s \rightarrow t$ is shorthand for $m \rightarrow(s \rightarrow(s \rightarrow t))$. Indeed, DMG can be viewed as the result of systematic replacement of entities by markers and of truth values by state transitions. A VP meaning for “is happy” is a function that maps a marker to a state transition. The state transition for marker $u_i$ will check whether the input state maps $u_i$ to a happy entity, and whether the output context equals the input context. The variables $a$, *a$'$* range over states, and the expression $(u_i \mid x)a$ denotes the result of resetting the value of $u_i$ in $a$ to $x$, so the old value of $u_i$ gets destroyed (destructive assignment). The anaphoric index $i$ on reference marker $u_i$ is introduced by the translation. In fact, the translation starts from the indexed indefinite noun phrase “a man$_i$”. The connection between Montagovian compositionality and dynamic semantics as well as the basic Montagovian and dynamic ingredients are much more transparent and streamlined in the typed Logic of Change proposed in Muskens 1991, 1995, 1996. Because of this, Muskens’s Compositional DRT is probably the *de facto* standard and starting point for current research in compositional dynamic semantics. An alternative treatment is given in Incremental Typed Logic (ITL), an extension to typed logic of a “stack semantics” that is based on variable free indexing and that avoids the destructive assignment problem. The basic idea of the stack semantics for DPL, developed in Vermeulen 1993, is to replace the destructive assignment of ordinary DPL, which throws away old values when resetting, by a stack-valued one that allows old values to be reused. Stack-valued assignments assign to each variable a stack of values, the top of the stack being the current value. Existential quantification pushes a new value on the stack, but there is also the possibility of popping the stack to reuse a previously assigned value. Eijck’s 2000 ITL is in fact a typed version of stack semantics, using a single stack.

Assuming a domain of entities, contexts are finite lists of entities. If $c$ is a context of length $n$, then we refer to its elements as $c[0]$, $\ldots ,c[n-1]$, and to its length as $\lvert c\rvert$. We will refer to the type of contexts of length $i$ as $[e]^i$. If $c$ is a context in $[e]^i$, then objects of type $\{0, \ldots ,i-1\}$ can serve as indices into $c$. If $c \in[e]^i$ and $j \in \{0, \ldots ,i-1\}$, then $c[j]$ is the object of type e that occurs at position $j$ in the context. A key operation on contexts is extension with an element. If $c :: [e]^i$ and $x :: e$ ($c$ is a context of length $i$ and $x$ is an entity) then $c\mcaret x$ is the context of length $i+1$ that has elements $c$[0], $\ldots ,c[i-1], x$. Thus $\mcaret$ is an operator of type $[e]^i \rightarrow e \rightarrow[e]^{i+1}$. Also note that types like $[e]^i$ are in fact polymorphic types, with $i$ acting as a type variable. See Milner 1978.

In ITL there is no destructive assignment, and indefinite noun phrases do not carry indexes in the syntax. The ITL translation of “a man” picks up an index from context, as follows:

$$\lambda P\lambda c\lambda c' \cdot \exists x (\textrm{man } x \mcaret P\lvert c\rvert (c^x)c').$$

Here $P$ is a variable of type $\{0, \ldots ,i\} \rightarrow[e]^{i+1} \rightarrow [e]^j \rightarrow t$, while $c$ is a variable of type [$e]^i$ representing the input context of length $i$, and $c'$ is a variable of type [$e]^j$ representing the output context. Note that the type $\{0, \ldots ,i\} \rightarrow [e]^{i+1} \rightarrow [e]^j \rightarrow t$ for $P$ indicates that $P$ first takes an index in the range $\{0, \ldots ,i\}$, next a context fitting this range (a context of length $i+1)$, next a context of a yet unknown length, and then gives a truth value. $P$ is the type of unary predicates, lifted to the level of context changers, as follows. Instead of using a variable to range over objects to form an expression of type $e$, a lifted predicate uses a variable ranging over the size of an input context to form an expression that denotes a changer for that context.

The ITL translation of “a man” has type $$(\{0, \ldots ,i\} \rightarrow[e]^{i+1} \rightarrow [e]^j \rightarrow t) \rightarrow [e]^i \rightarrow [e]^j \rightarrow t.$$ In $P\lvert c\rvert (c\mcaret x)c'$, the $P$ variable marks the slot for the VP interpretation; $\lvert c\rvert$ gives the length of the input context to $P$; it picks up the value $i$, which is the position of the next available slot when the context is extended. This slot is filled by an object $x$ denoting a man. Note that $c\mcaret x[\lvert c\rvert ] = c\mcaret x[i] = x$, so the index $i$ serves to pick out that man from the context.

To see that a dynamic higher order system is expressible in ITL, it is enough to show how to define the appropriate dynamic operations. Assume $\phi$ and $\psi$ have the type of context transitions, i.e. type [$e] \rightarrow[e] \rightarrow t$ (using [$e$] for arbitrary contexts), and that $c, c', c''$ have type [$e$]. Then we can define the dynamic existential quantifier, dynamic negation and dynamic composition as follows:

$$ \begin{align*} \cal{E} & := \lambda cc'\cdot \exists x(c \mcaret x = c') \\ {\sim}\phi & := \lambda cc'\cdot (c = c' \mcaret \neg \exists c'' \phi cc'') \\ \phi ; \psi & := \lambda cc'\cdot \exists c''(\phi cc'' \mcaret \psi cc') \end{align*} $$

Dynamic implication $\Rightarrow$ is defined in the usual way by means of ${\sim}(\phi; {\sim}\psi)$.

ITL and Muskens style Compositional DRT are not incompatible; see Bittner 2014 for example. We will end this section by noting that the range of systems integrating Montagovian compositionality and dynamic semantics is far from being completely charted. A recent series of contributions integrating continuation-based and dynamic semantics is exploring new ways of integrating and generalizing them; see de Groote 2006, Bumford and Barker 2013, Charlow 2014, Bumford 2015, and Martin 2016.

## 5. Conclusion

Hopefully, the above has given the reader a sense of Dynamic Semantics as a fruitful and flexible approach to meaning and information processing. Dynamic semantics comes with a set of flexible tools, and with a collection of “killer applications”, such as the compositional treatment of donkey sentences, the account of anaphoric linking, the account of presupposition projection, the account of epistemic updating and fine-grained distinctions between different kinds of (non-at-issue) updates. Dynamic semantics is a very lively subfield of formal semantics and the cross-linguistic range of phenomena for which dynamic approaches are being pursued is expanding at an increasing pace.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=dynamic-semantics). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/dynamic-semantics/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=dynamic-semantics&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](http://philpapers.org/sep/dynamic-semantics/) at [PhilPapers](http://philpapers.org/), with links to its database. |

## Other Internet Resources

- Chemla, Emmanuel, 2008, “[Similarity: Towards a Unified Account of Scalar Implicatures, Free Choice Permission and Presupposition Projection](http://semanticsarchive.net/Archive/WI1ZTU3N/Chemla-SIandPres.html),” unpublished manuscript, Ecole Normale Superieur.
- Parsons, Terence, 1978, “[Pronouns as Paraphrases](http://www.philosophy.ucla.edu/people/faculty/tparsons/Pronouns%20as%20Paraphrases/Pronouns%20as%20Paraphrases.pdf),”, unpublished manuscript, University of Massachusetts/Amherst.

## Related Entries

anaphora | assertion | common knowledge | compositionality | conditionals | contextualism, epistemic | discourse representation theory | externalism about the mind | implicature | indexicals | information: semantic conceptions of | logic: classical | logic: conditionals | logic: epistemic | logic: of belief revision | logic: second-order and higher-order | logical form | mental content: narrow | mind: computational theory of | model theory: first-order | pragmatics | reference | scientific realism | speech acts | Tarski, Alfred: truth definitions | type theory: Church’s type theory

[^anderbois-2015]: AnderBois, Scott, Adrian Brasoveanu, and Robert Henderson, 2015, “At-issue Proposals and Appositive Impositions in Discourse”, *Journal of Semantics*, 32: 93–138. doi:10.1093/jos/fft014

[^aloni-1997]: Aloni, Maria, 1997, “Quantification in Dynamic Semantics”, in *Proceedings of the Eleventh Amsterdam Colloquium*, P. Dekker (ed.), 73–78.

[^baltag-2004]: Baltag, Alexandru and Lawrence S. Moss, 2004, “Logics for Epistemic Programs”, *Synthese*, 139(2): 165–224. doi:10.1023/B:SYNT.0000024912.56773.5e

[^baltag-1999]: Baltag, Alexandru, Lawrence S. Moss, and Slawomir Solecki, 1999, “The Logic of Public Announcements, Common Knowledge, and Private Suspicions”, Technical Report SEN-R9922, CWI, Amsterdam. [[Baltag et al. 1999 available online](http://www.cs.indiana.edu/cgi-bin/techreports/TRNNN.cgi?trnum=TR534)]

[^barker-2002]: Barker, Chris, 2002, “The Dynamics of Vagueness”, *Linguistics and Philosophy*, 25(1): 1–36.

[^barker-2008]: Barker, Chris and Chung-chieh Shan, 2008, “Donkey Anaphora is In-scope Binding”, *Semantics and Pragmatics*, 1: 1–46. doi:10.3765/sp.1.1

[^beaver-1997]: Beaver, David, 1997, “Presupposition”, in van Benthem and ter Meulen 1997: 939–1008.

[^beaver-2001]: –––, 2001, *Presupposition and Assertion in Dynamic Semantics*, Stanford: CSLI Publications.

[^benthem-1989]: Benthem, Johan van, 1989, “Semantic Parallels in Natural Language and Computation”, in *Logic Colloquium, Granada, 1987*, Heinz-Dieter Ebbinghaus et al. (eds.), Amsterdam: Elsevier, 331–375.

[^benthem-1996]: –––, 1996, *Exploring Logical Dynamics*, Stanford: CSLI & Folli.

[^benthem-1997]: Benthem, Johan van and Alice ter Meulen (eds.), 1997, *Handbook of Logic and Language*, Amsterdam: Elsevier.

[^benthem-2006]: Benthem, Johan van, Jan van Eijck, and Barteld Kooi, 2006, “Logics of Communication and Change”, *Information and Computation*, 204(11): 1620–1662. doi:10.1016/j.ic.2006.04.006

[^berg-1996]: van den Berg, Martin H., 1996, *The Internal Structure of Discourse*, Ph.D. Thesis, ILLC Dissertation Series 1996–3, Amsterdam: ILLC Publications.

[^bittner-2014]: Bittner, Maria, 2014, *Temporality: Universals and Variation*, Hoboken, NJ: Wiley-Blackwell.

[^brasoveanu-2007]: Brasoveanu, Adrian, 2007, *Structured Nominal and Modal reference*, Ph.D. Thesis, Rutgers University.

[^brasoveanu-2008]: –––, 2008, “Donkey Pluralities: Plural Information States Versus Non-Atomic Individuals”, *Linguistics and Philosophy*, 31 (2): 129–209. doi:10.1007/s10988-008-9035-0

[^brasoveanu-2013]: –––, 2013, “The Grammar of Quantification and the Fine Structure of Interpretation Contexts”, *Synthese*, 190(15): 3001–3051. doi:10.1007/s11229-012-0118-7

[^bumford-2015]: Bumford, Dylan, 2015, “Incremental Quantification and the Dynamics of Pair-list Phenomena”, *Semantics and Pragmatics*, 8(9): 1–70. doi:10.3765/sp.8.9

[^bumford-2013]: Bumford, Dylan and Chris Barker, 2013, “Association with Distributivity and the Problem of Multiple Antecedents for Singular Different”, in *Linguistics and Philosophy*, 36(5): 355–369. doi:10.1007/s10988-013-9139-z

[^charlow-2014]: Charlow, Simon, 2014, *On the Semantics of Exceptional Scope*, Ph.D. Thesis, New York University.

[^chierchia-1992]: Chierchia, Gennaro, 1992, “Anaphora and Dynamic Binding”, *Linguistics and Philosophy*, 15(2): 111–183. [[Chierchia 1992 available online](http://scholar.harvard.edu/chierchia/publications/anaphora-and-dynamic-binding)]

[^chierchia-1995]: –––, 1995, *Dynamics of Meaning: Anaphora, Presupposition, and the Theory of Grammar*, Chicago: University of Chicago Press.

[^dekker-1993]: Dekker, Paul Jacques Edgar, 1993, *Transsentential Meditations, ups and downs in dynamic semantics*, Ph.D. Thesis, University of Amsterdam, ILLC. [[Dekker 1993 available online](http://hdl.handle.net/11245/1.392554)]

[^ditmarsch-2006]: Ditmarsch, Hans van, Wiebe van der Hoek, and Barteld Kooi, 2006, *Dynamic Epistemic Logic* (Synthese Library: Volume 337), Dordrecht: Springer.

[^eijck-1994]: Eijck, Jan van, 1994, “Presupposition Failure—a Comedy of Errors”, *Formal Aspects of Computing*, 6(supplement 1): 766–787. doi:10.1007/BF01213602

[^eijck-1997]: –––, 1997, “Typed Logics with States”, *Logic Journal of the IGPL*, 5(5): 623–645. doi:10.1093/jigpal/5.5.623

[^eijck-2000]: –––, 2000, “On the Proper Treatment of Context in NL”, in *Computational Linguistics in the Netherlands 1999; Selected Papers from the Tenth CLIN Meeting*, Paola Monachesi (ed.), Utrecht Institute of Linguistics OTS, 41–51.

[^eijck-1992]: Eijck, Jan van and Fer-Jan de Vries, 1992, “Dynamic Interpretation and Hoare Deduction”, *Journal of Logic, Language, and Information*, (1)1: 1–44. doi:10.1007/BF00203385

[^eijck-1997-2]: Eijck, Jan van and Hans Kamp, 1997, “Representing Discourse in Context”, in van Benthem and ter Meulen 1997: 179–237.

[^elbourne-2001]: Elbourne, Paul, 2001, “E-Type Anaphora as NP-Deletion”, *Natural Language Semantics*, 9(3): 241–288. doi:10.1023/A:1014290323028

[^elbourne-2005]: –––, 2005, *Situations and Individuals*, Cambridge, MA: MIT Press.

[^evans-1977]: Evans, Gareth, 1977, “Pronouns, Quantifiers and Relative Clauses (I)”, *Canadian Journal of Philosophy*, 7(3): 467–536.

[^evans-1980]: –––, 1980, “Pronouns”, *Linguistic Inquiry*, 11(2): 337–362.

[^fox-2008]: Fox, Danny, 2008, “Two Short Notes on Schlenker’s theory of Presupposition Projection”, *Theoretical Linguistics*, 34(3): 237–252. doi:10.1515/THLI.2008.016

[^geach-1962]: Geach, Peter Thomas, 1962 [1980], *Reference and Generality: An Examination of Some Medieval and Modern Theories*, Ithaca, NY: Cornell University Press. Third revised edition: 1980.

[^george-2008]: George, Benjamin Ross, 2008, *Presupposition Repairs: a Static, Trivalent Approach to Predicting Projection*, M.A. Thesis, UCLA.

[^gerbrandy-1999]: Gerbrandy, Jelle, 1999, “Dynamic Epistemic Logic”, in *Logic, Language and Computation, Vol. 2*, Lawrence S. Moss, Jonathan Ginzburg, and Maarten de Rijke (eds.), Stanford: CSLI Publications.

[^groenendijk-1990]: Groenendijk, Jeroen and Martin Stokhof, 1990, “Dynamic Montague Grammar”, in *Papers from the Second Symposium on Logic and Language*, L. Kalman and L. Polos (eds.), Budapest: Akademiai Kiadoo, 3–48.

[^groenendijk-1991a]: –––, 1991a, “Dynamic Predicate logic”, *Linguistics and Philosophy*, 14(1): 39–100. doi:10.1007/BF00628304

[^groenendijk-1991b]: –––, 1991b, “Two Theories of Dynamic Semantics”, in *JELIA ‘90, European Workshop on Logics in AI* (Lecture Notes in Computer Science: Volume 478), Jan van Eijck (ed.), Berlin: Springer, 55–64. doi:10.1007/BFb0018433

[^groenendijk-1996]: Groenendijk, Jeroen, Martin Stokhof, and Frank Veltman, 1996, “Coreference and Modality”, in *Handbook of Contemporary Semantic Theory*, Shalom Lappin (ed.), Oxford: Blackwell, 179–213.

[^groeneveld-1995]: Groeneveld, Willem, 1995, *Logical Investigations into Dynamic Semantics*, Ph.D. Thesis, University of Amsterdam.

[^groote-2006]: de Groote, Philippe, 2006, “Towards a Montagovian Account of Dynamics”, in *Proceedings of Semantics and Linguistic Theory (SALT) 16*, Masayuki Gibson and Jonathan Howell (eds.), 1–16. doi:10.3765/salt.v16i0.2952

[^heim-1983a]: Heim, Irene, 1983a, “File Change Semantics and the Familiarity Theory of Definiteness”, in *Meaning, Use and Interpretation of Language*, Rainer Bäuerle, Christoph Schwarze, and Arnim von Stechow (eds.), Berlin: De Gruyter, 164–189.

[^heim-1983b]: –––, 1983b, “On the Projection Problem for Presuppositions”, *Proceedings of the Second West Coast Conference on Formal Linguistics*, Michael Barlow, Dan P. Flickinger and MIchael T. Wescoat (eds.), Stanford, CA: Stanford University Department of Lingustics, 114–126.

[^heim-1990]: –––, 1990, “E-Type Pronouns and Donkey Anaphora”, *Linguistics and Philosophy*, 13(2): 137–138.

[^hollenberg-1996]: Hollenberg, Marco and Kees Vermeulen, 1996, “Counting Variables in a Dynamic Setting”, *Journal of Logic and Computation*, 6(5): 725–744. doi:10.1093/logcom/6.5.725

[^kamp-1981]: Kamp, Hans, 1981, “A Theory of Truth and Semantic Representation”, in *Formal Methods in the Study of Language*, Jeroen Groenendijk, Theo Janssen, and Martin Stokhof (eds.), Amsterdam: Mathematisch Centrum, 277–322.

[^kamp-1993]: Kamp, Hans and Uwe Reyle, 1993, *From Discourse to Logic*, Dordrecht: Kluwer.

[^karttunen-1973]: Karttunen, Lauri, 1973, “Presuppositions of Compound Sentences”, *Linguistic Inquiry*, 4(2): 169–193.

[^karttunen-1974]: –––, 1974, “Presupposition and Linguistic Context”, *Theoretical Linguistics*, 1: 181–194.

[^kohlhase-1996]: Kohlhase, Michael, Susanna Kuschert, and Manfred Pinkal, 1996, “A Type-Theoretic Semantics for $\lambda$-DRT”, in *Proceedings of the Tenth Amsterdam Colloquium*, Paul Dekker and Martin Stokhof (eds.), Amsterdam: ILLC Publications.

[^krahmer-1995]: Krahmer, Emiel, 1995, *Discourse and Presupposition*, Ph.D. Thesis, Tilburg University; revised and published under the title *Presupposition and Anaphora*, Stanford: CSLI Publications, 1998.

[^krahmer-1996]: Krahmer, Emiel and Reinhard Muskens, 1996, “Negation and Disjunction in Discourse Representation Theory” *Journal of Semantics*, 12: 357–376. doi: 10.1093/jos/12.4.357

[^krifka-1996]: Krifka, Manfred, 1996, “Parametrized Sum Individuals for Plural Reference and Partitive Quantification” *Linguistics and Philosophy*, 19: 555–598. [[Krifka 1996 available online (pdf)](http://amor.cms.hu-berlin.de/~h2816i3x/Publications/Krifka%201996%20Plural%20Anaphora.PDF)]

[^kuschert-2000]: Kuschert, Susanna, 2000, *Dynamic Meaning and Accommodation*, Ph.D. Thesis, Universität des Saarlandes.

[^martin-2016]: Martin, Scott, 2016, “Supplemental Update”, *Semantics and Pragmatics*, 9(5). doi:10.3765/sp.9.5

[^milner-1978]: Milner, Robin, 1978, “A Theory of Type Polymorphism in Programming”, *Journal of Computer and System Sciences*, 17: 348–375.

[^montague-1973]: Montague, Richard, 1973, “The Proper Treatment of Quantification in Ordinary English”, in *Approaches to Natural Language*, Jaakko Hintikka, Julius Moravcsik, and Patrick Suppes (eds.), Dordrecht: Reidel, 221–242.

[^montague-1974a]: –––, 1974a, “English as a Formal Language”, in Montague 1974c: 188–221.

[^montague-1974b]: –––, 1974b, “Universal Grammar”, in Montague 1974c: 222–246.

[^montague-1974c]: –––, 1974c, *Formal Philosophy; Selected Papers of Richard Montague*, R.H. Thomason (ed.), New Haven and London: Yale University Press.

[^murray-2014]: Murray, Sarah E., 2014, “Varieties of Update”, *Semantics and Pragmatics*, 7: 1–53. doi:10.3765/sp.7.2

[^muskens-1991]: Muskens, Reinhard, 1991, “Anaphora and the Logic of Change”, in *JELIA ‘90, European Workshop on Logics in AI* (Lecture Notes in Computer Science: Volume 478), Jan van Eijck (ed.), Berlin and New York, 414–430. doi:10.1007/BFb0018456

[^muskens-1994]: –––, 1994, “A Compositional Discourse Representation Theory”, in *Proceedings 9ᵗʰ Amsterdam Colloquium*, Paul Dekker and Martin Stokhof (eds.), Amsterdam: ILLC Publications, 467–486.

[^muskens-1995]: –––, 1995, “Tense and the Logic of Change”, in *Lexical Knowledge in the Organization of Language*, U. Egli et al. (ed.), Amsterdam: John Benjamins, 147–183.

[^muskens-1996]: –––, 1996, “Combining Montague Semantics and Discourse Representation”, *Linguistics and Philosophy*, 19: 143–186.

[^muskens-1997]: Muskens, Reinhard, Johan van Benthem, and Albert Visser, 1997, “Dynamics”, in van Benthem and ter Meulen 1997: 587–648.

[^nouwen-2003]: Nouwen, Rick, 2003, “Complement Anaphora and Interpretation”, *Journal of Semantics*, 20: 73–113.

[^nouwen-2007]: –––, 2007, “On Dependent Pronouns and Dynamic Semantics”, *Journal of Philosophical Logic*, 36(2): 123–154.

[^nouwen-nd]: –––, forthcoming, “E-type Pronouns: Congressmen, Sheep and Paychecks”, in L. Matthewson, C. Meier, H. Rullmann, and T.E. Zimmerman (eds.), *The Blackwell Companion to Semantics*, Oxford: Wiley.

[^plaza-1989]: Plaza, Jan A., 1989, “Logics of Public Communications”, in *Proceedings of the 4ᵗʰ International Symposium on Methodologies for Intelligent Systems*, M.L. Emrich, M.S. Pfeifer, M. Hadzikadic, and Z.W. Ras (eds.), Amsterdam: North Holland, 201–216.

[^putnam-1975]: Putnam, Hilary, 1975, “The Meaning of ‘Meaning’”, in *Philosophical Papers* (Volume 2), Cambridge: Cambridge University Press.

[^quine-1960]: Quine, Willard van Orman, 1960, *Word and Object*, Cambridge, MA: MIT Press.

[^roberts-1987]: Roberts, Craige, 1987, *Modal Subordination, Anaphora and Distributivity*, Ph.D. Thesis, University of Massachusetts/Amherst; New York: Garland, 1990.

[^roberts-1989]: –––, 1989, “Modal Subordination and Pronominal Anaphora in Discourse”, *Linguistics and Philosophy*, 12: 683–721.

[^rothschild-2011]: Rothschild, Daniel, 2011, “Explaining Presupposition Projection with Dynamic Semantics”, *Semantics and Pragmatics*, 4(3): 1“43.

[^sandt-1992]: Sandt, Rob A. van der, 1992, “Presupposition Projection as Anaphora Resolution”, *Journal of Semantics* (Special Issue: Presupposition, Part 2), 9: 333–377. doi:10.1093/jos/9.4.333

[^schlenker-2007]: Schlenker, Philippe, 2007, “Anti-dynamics: Presupposition Projection without Dynamic Semantics”, *Journal of Logic, Language and Information*, 16(3): 325–356.

[^schlenker-2008]: –––, 2008, “Be Articulate: A Pragmatic Theory of Presupposition Projection”, *Theoretical Linguistics*, 34(3): 157–212.

[^schlenker-2009]: –––, 2009, “Local Contexts”, *Semantics and Pragmatics*, 2(3): 1–78.

[^seuren-1985]: Seuren, Pieter, 1985, *Discourse Semantics*, Oxford: Blackwell.

[^soames-1989]: Soames, Scott, 1989, “Presuppositions”, in Dov M. Gabbay & Franz Guenther (eds.), *Handbook of Philosophical Logic*, vol. IV, 553–616. Dordrecht. doi:10.1007/978-94-009-1171-0_9

[^stalnaker-1972]: Stalnaker, Robert C., 1972, “Pragmatics”, in *Semantics of Natural Language*, Donald Davidson and Gilbert Harman (eds.), Dordrecht: Reidel, 380–397. doi:10.1007/978-94-010-2557-7_11

[^stalnaker-1973]: –––, 1973, “Presuppositions”, *Journal of Philosophical Logic*, 2: 447–457.

[^stalnaker-1974]: –––, 1974, “Pragmatic Presuppositions”, in *Semantics and Philosophy*, Milton K. Munitz and Peter K. Unger (eds.), New York: New York University Press, 197–213.

[^veltman-1991]: Veltman, Frank, 1991, “Defaults in Update Semantics”, in *Conditionals, Defaults and Belief Revision*, Hans Kamp (ed.), Edinburgh: Dyana Deliverable R2.5A.

[^veltman-1996]: –––, 1996, “Defaults in Update Semantics”, *Journal of Philosophical Logic*, 25: 221–261.

[^vermeulen-1993]: Vermeulen, C.F.M., 1993, “Sequence Semantics for Dynamic Predicate Logic”, *Journal of Logic, Language and Information*, 2: 217–254. doi:10.1007/BF01050788

[^vermeulen-1994]: –––, 1994, *Explorations of the Dynamic Environment*, Ph.D. thesis, Utrecht University.

[^vermeulen-1995]: –––, 1995, “Merging without Mystery, Variables in Dynamic Semantics”, *Journal of Philosophical Logic*, 24: 405–450.

[^werth-2000]: Werth, Paul, 2000, *Text Worlds: Representing Conceptual Space in Discourse*, London: Pearson Education/Longman.

[^zeevat-1989]: Zeevat, Hank, 1989, “A Compositional Approach to Discourse Representation Theory”, *Linguistics and Philosophy*, 12(1): 95–131. doi:10.1007/BF00627399
