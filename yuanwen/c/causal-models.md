# Causal Models
**First published Tue Aug 7, 2018**

*Hitchcock, Christopher*

Causal models are mathematical models representing causal relationships within an individual system or population. They facilitate inferences about causal relationships from statistical data. They can teach us a good deal about the epistemology of causation, and about the relationship between causation and probability. They have also been applied to topics of interest to philosophers, such as the logic of counterfactuals, decision theory, and the analysis of actual causation.

## 1. Introduction

Causal modeling is an interdisciplinary field that has its origin in the statistical revolution of the 1920s, especially in the work of the American biologist and statistician Sewall Wright (1921)[^wright-1921]. Important contributions have come from computer science, econometrics, epidemiology, philosophy, statistics, and other disciplines. Given the importance of causation to many areas of philosophy, there has been growing philosophical interest in the use of mathematical causal models. Two major works—Spirtes, Glymour, and Scheines 2000 (abbreviated SGS), and Pearl 2009—have been particularly influential.

A causal model makes predictions about the behavior of a system. In particular, a causal model entails the truth value, or the probability, of counterfactual claims about the system; it predicts the effects of interventions; and it entails the probabilistic dependence or independence of variables included in the model. Causal models also facilitate the inverse of these inferences: if we have observed probabilistic correlations among variables, or the outcomes of experimental interventions, we can determine which causal models are consistent with these observations. The discussion will focus on what it is possible to do in “in principle”. For example, we will consider the extent to which we can infer the correct causal structure of a system, given perfect information about the probability distribution over the variables in the system. This ignores the very real problem of inferring the true probabilities from finite sample data. In addition, the entry will discuss the application of causal models to the logic of counterfactuals, the analysis of causation, and decision theory.

## 2. Basic Tools

This section introduces some of the basic formal tools used in causal modeling, as well as terminology and notational conventions.

### 2.1 Variables, Logic, and Language

*Variables* are the basic building blocks of causal models. They will be represented by italicized upper case letters. A variable is a function that can take a variety of values. The values of a variable can represent the occurrence or non-occurrence of an event, a range of incompatible events, a property of an individual or of a population of individuals, or a quantitative value. For instance, we might want to model a situation in which Suzy throws a stone and a window breaks, and have variables *S* and *W* such that:

- $S = 1$ represents Suzy throwing a rock; $S = 0$ represents her not throwing
- $W = 1$ represents the window breaking; $W = 0$ represents the window remaining intact.

If we are modeling the influence of education on income in the United States, we might use variables *E* and *I* such that:

- $E(i) = 0$ if individual *i* has no high school education; 1 if an individual has completed high school; 2 if an individual has had some college education; 3 if an individual has a bachelor’s degree; 4 if an individual has a master’s degree; and 5 if an individual as a doctorate (including the highest degrees in law and medicine).
- $I(i) = x$ if individual *i* has a pre-tax income of \$*x* per year.

The set of possible values of a variable is the *range* of that variable. We will usually assume that variables have finitely many possible values, as this will keep the mathematics and the exposition simpler. However, causal models can also feature continuous variables, and in some cases this makes an important difference.

A *world* is a complete specification of a causal model; the details will depend upon the type of model. For now, we note that a world will include, *inter alia*, an assignment of values to all of the variables in the model. If the variables represent the properties of individuals in a population, a world will include an assignment of values to every variable, for every individual in the population. A variable can then be understood as a function whose domain is a set of worlds, or a set of worlds and individuals.

If *X* is a variable in a causal model, and *x* is a particular value in the range of *X*, then $X = x$ is an *atomic proposition*. The logical operations of negation (“not”), conjunction (“and”), disjunction (“or”), the material conditional (“if…then…”), and the biconditional (“if and only if”) are represented by “${\sim}$”, “&”, “$\lor$”, “$\supset$”, and “$\equiv$” respectively. Any proposition built out of atomic propositions and these logical operators will be called a *Boolean* proposition. Note that when the variables are defined over individuals in a population, reference to an individual is *not* included in a proposition; rather, the proposition as a whole is true or false of the various individuals in the population.

We will use basic notation from set theory. Sets will appear in boldface.

- $\mathbf{\varnothing}$ is the empty set (the set that has no members or elements).
- $x \in \bX$ means that *x* is a member or element of the set $\bX$.
- $\bX \subseteq \bY$ means that $\bX$ is a subset of $\bY$; i.e., every member of $\bX$ is also a member of $\bY$. Note that both $\mathbf{\varnothing}$ and $\bY$ are subsets of $\bY$.
- $\bX \setminus \bY$ is the set that results from removing the members of $\bY$ from $\bX$.
- $\forall$ and $\exists$ are the universal and existential quantifiers, respectively.

If $\bS = \{x_1 , \ldots ,x_n\}$ is a set of values in the range of *X*, then $X \in \bS$ is used as shorthand for the disjunction of propositions of the form $X = x_i$, for $i = 1,\ldots$, n. Boldface represents *ordered sets* or *vectors*. If $\bX = \{X_1 , \ldots ,X_n\}$ is a vector of variables, and $\bx = \{x_1 , \ldots ,x_n\}$ is a vector of values, with each value $x_i$ in the range of the corresponding variable $X_i$, then $\bX = \bx$ is the conjunction of propositions of the form $X_i = x_i$.

### 2.2 Probability

In section 4, we will consider causal models that include probability. Probability is a function, P, that assigns values between zero and one, inclusive. The domain of a probability function is a set of propositions that will include all of the Boolean propositions described above, but perhaps others as well.

Some standard properties of probability are the following:

- If *A* is a contradiction, then $\Pr(A) = 0$.
- If *A* is a tautology, then $\Pr(A) = 1$.
- If $\Pr(A \amp B) = 0$, then $\Pr(A \lor B) = \Pr(A) + \Pr(B)$.
- $\Pr({\sim}A) = 1 - \Pr(A)$.

Some further definitions:

- The *conditional probability of A given B,* written $\Pr(A \mid B)$ is standardly defined as follows: $$ \Pr(A \mid B) = \frac{\Pr(A \amp B)}{\Pr(B)}. $$ We will ignore problems that might arise when $\Pr(B) = 0$.
- *A* and *B* are *probabilistically independent* (with respect to $\Pr$) just in case $\Pr(A \amp B) = \Pr(A) \times \Pr(B). A$ and *B* are *probabilistically dependent* or *correlated* otherwise. If $\Pr(B) \gt 0$, then *A* and *B* will be independent just in case $\Pr(A \mid B) = \Pr(A)$.
- Variables *X* and *Y* are probabilistically independent just in case all propositions of the form $X = x$ and $Y = y$ are probabilistically independent.
- *A* and *B* are *probabilistically independent conditional on* *C* just in case $\Pr(A \amp B \mid C) = \Pr(A \mid C) \times \Pr(B \mid C)$. If $\Pr(B \amp C) \gt 0$, this is equivalent to $\Pr(A \mid B \amp C) = \Pr(A \mid C)$. Following the terminology of Reichenbach (1956)[^reichenbach-1956], we will also say that *C screens off B from A* when these equalities hold. Conditional independence among variables is defined analogously.

As a convenient shorthand, a probabilistic statement that contains only a variable or set of variables, but no values, will be understood as having a universal quantification over all possible values of the variable(s). Thus if $\bX = \{X_1 ,\ldots ,X_m\}$ and $\bY = \{Y_1 ,\ldots ,Y_n\}$, we may write

$$ \Pr(\bX \mid \bY) = \Pr(\bX) $$

as shorthand for

$$\begin{aligned} \forall x_1 \ldots \forall x_m\forall y_1 \ldots \forall y_n [\Pr(X_1\! =\! x_1 ,\ldots ,X_m\! =\! x_m \mid Y_1\! =\! y_1 ,\ldots ,Y_n\! =\! y_n ) \\ = \Pr(X_1\! =\! x_1 ,\ldots ,X_m\! =\! x_m ) ] \end{aligned}$$

where the domain of quantification for each variable will be the range of the relevant variable.

We will not presuppose any particular interpretation of probability (see the entry on interpretations of probability), but we will assume that frequencies in appropriately chosen samples provide evidence about the underlying probabilities. For instance, suppose there is a causal model including the variables *E* and *I* described above, with $\Pr(E = 3) = .25$. Then we expect that if we survey a large, randomly chosen sample of American adults, we will find that approximately a quarter of them have a Bachelor’s degree, but no higher degree. If the survey produces a sample frequency that substantially differs from this, we have evidence that the model is inaccurate.

### 2.3 Graphs

If $\bV$ is the set of variables included in a causal model, one way to represent the causal relationships among the variables in $\bV$ is by a *graph*. Although we will introduce and use graphs in section 3, they will play a more prominent role in section 4. We will discuss two types of graphs. The first is the *directed acyclic graph* (DAG). A *directed graph* $\bG$ on variable set $\bV$ is a set of ordered pairs of variables in $\bV$. We represent this visually by drawing an arrow from *X* to *Y* just in case $\langle X, Y\rangle$ is in $\bG$. Figure 1 shows a directed graph on variable set $\bV = \{S, T, W, X, Y, Z\}$.

![a diagram where S has an arrow pointing north to T; T has an arrow pointing northwest to X and northeast to Y; Y has an arrow pointing northeast to Z; W has an arrow pointing north to Z and northwest to Y](../assets/causal-models/fig1.svg)

\*Figure 1\*

A *path* in a directed graph is a non-repeating sequence of arrows that have endpoints in common. For example, in Figure 1 there is a path from *X* to *Z*, which we can write as $X \leftarrow T \rightarrow Y \rightarrow Z$. A *directed path* is a path in which all the arrows point in the same direction; for example, there is a directed path $S \rightarrow T \rightarrow Y \rightarrow Z$. A directed graph is *acyclic,* and hence a DAG, if there is no directed path from a variable to itself. Such a directed path is called a *cycle*. The graph in Figure 1 contains no cycles, and hence is a DAG.

The relationships in the graph are often described using the language of genealogy. The variable *X* is a *parent* of *Y* just in case there is an arrow from *X* to *Y*. $\bPA(Y)$ will denote the set of all parents of *Y*. In Figure 1, $\bPA(Y) = \{T, W\}$. *X* is an *ancestor* of *Y* (and *Y* is a *descendant* of $X)$ just in case there is a directed path from *X* to *Y*. However, it will be convenient to deviate slightly from the genealogical analogy and define “descendant” so that every variable is a descendant of itself. $\bDE(X)$ denotes the set of all descendants of *X*. In Figure 1, $\bDE(T) = \{T,X, Y, Z\}$.

An arrow from *Y* to *Z* in a DAG represents that *Y* is a *direct cause* of $Z.$ Roughly, this means that the value of *Y* makes some causal difference for the value of *Z*, and that *Y* influences *Z* through some process that is not mediated by any other variable in $\bV$. Directness is relative to a variable set: *Y* may be a direct cause of *Z* relative to variable set $\bV$, but not relative to variable set $\bV'$ that includes some additional variable(s) that mediate the influence of *Y* on $Z.$ As we develop our account of graphical causal models in more detail, we will be able to say more precisely what it means for one variable to be a direct cause of another. While we will not define “cause”, causal models presuppose a broadly *difference-making* notion of causation, rather than a causal process notion (Salmon 1984, Dowe 2000)[^dowe-2000][^salmon-1984] or a mechanistic notion (Machamer, Darden, & Craver 2000; Glennan 2017)[^glennan-2017][^machamer-2000]. We will call the system of direct causal relations represented in a DAG such as Figure 1 the *causal structure* on the variable set $\bV$.

A second type of graph that we will consider is an *acyclic directed mixed graph* (ADMG). An ADMG will contain double-headed arrows, as well as single-headed arrows. A double-headed arrow represents a *latent* common cause. A latent common cause of variables *X* and *Y* is a common cause that is not included in the variable set $\bV$. For example, suppose that *X* and *Y* share a common cause *L* (Figure 2(a)). An ADMG on the variable set $\bV = \{X, Y\}$ will look like Figure 2(b).

![diagram with L having an arrow pointing northwest to X and northeast to Y](../assets/causal-models/fig2a.svg)

(a)

![X is to the right of Y and a double-headed curved arrow connects the two](../assets/causal-models/fig2b.svg)

(b)

\*Figure 2\*

We can be a bit more precise. We only need to represent missing common causes in this way when they are *closest* common causes. That is, a graph on $\bV$ should contain a double-headed arrow between *X* and *Y* when there is a variable *L* that is omitted from $\bV$, such that if *L* were added to $\bV$ it would be a *direct cause* of *X* and *Y*.

In an ADMG, we expand the definition of a *path* to include double-headed arrows. Thus, $X \leftrightarrow Y$ is a path in the ADMG shown in Figure 2(b). *Directed path* retains the same meaning, and a directed path cannot contain double-headed arrows.

We will adopt the convention that both DAGs and ADMGs represent the presence *and absence* of both direct causal relationships and latent common causes. For example the DAG in Figure 1 represents that *W* is a direct cause of *Y*, that *X* is not a direct cause of *Y*, and that *there are no latent common causes*. The absence of double-headed arrows from Figure 1 does not show merely that we have chosen not to include latent common causes in our representation; it shows that there are no latent common causes.

## 3. Deterministic Structural Equation Models

In this section, we introduce deterministic *structural equation models* (SEMs), postponing discussion of probability until Section 4. We will consider two applications of deterministic SEMs: the logic of counterfactuals, and the analysis of actual causation.

### 3.1 Introduction to SEMs

A SEM characterizes a causal system with a set of variables, and a set of equations describing how each variable depends upon its immediate causal predecessors. Consider a gas grill, used to cook meat. We can describe the operations of the grill using the following variables:

- *Gas connected* (1 if yes, 0 if no)
- *Gas knob* (0 for off, 1 for low, 2 for medium, 3 for high)
- *Gas level* (0 for off, 1 for low, 2 for medium, 3 for high)
- *Igniter* (1 if pressed, 0 if not)
- *Flame* (0 for off, 1 for low, 2 for medium, 3 for high)
- *Meat on* (0 for no, 1 for yes)
- *Meat cooked* (0 for raw, 1 for rare, 2 for medium, 3 for well done)

Thus, for example, *Gas knob* = 1 means that the gas knob is set to low; *Igniter* = 1 means that the igniter is pressed, and so on. Then the equations might be:

- *Gas level* = *Gas connected* $\times$ *Gas knob*
- *Flame* = *Gas level* $\times$ *Igniter*
- *Meat cooked* = *Flame* $\times$ *Meat on*

The last equation, for example, tells us that if the meat is not put on the grill, it will remain raw (*Meat cooked* = 0). If the meat is put on the grill, then it will get cooked according to the level of the flame: if the flame is low (*Flame* = 1), the meat will be rare (*Meat cooked* = 1), and so on.

By convention each equation has one effect variable on the left hand side, and one or more cause variables on the right hand side. We also exclude from each equation any variable that makes no difference to the value of the effect variable. For example, the equation for *Gas level* could be written as *Gas level* = (*Gas connected* $\times$ *Gas knob*) $+$ (0 $\times$ *Meat cooked*); but since the value of *Meat cooked* makes no difference to the value of *Gas level* in this equation, we omit the variable *Meat cooked*. A SEM is *acyclic* if the variables can be ordered so that variables never appear on the left hand side of an equation after they have appeared on the right. Our example is acyclic, as shown by the ordering of variables given above. In what follows, we will assume that SEMs are acyclic, unless stated otherwise.

We can represent this system of equations as a DAG (Figure 3):

![diagram: 'Gas connected' has an arrow pointing northeast to 'Gas level'; 'Gas knob' has an arrow pointing northwest to the same 'Gas level'; 'Gas level' has an arrow pointing northeast to 'Flame'; 'Igniter' has an arrow pointing northwest to the same 'Flame'; 'Flame' has an arrow pointing northeast to 'Meat cooked'; 'Meat on' has an arrow pointing northwest to the same 'Meat cooked'](../assets/causal-models/fig3.svg)

\*Figure 3\*

An arrow is drawn from variable *X* to variable *Y* just in case *X* figures as an argument in the equation for *Y*. The graph contains strictly less information than the set of equations; in particular, the DAG gives us qualitative information about which variables depend upon which others, but it does not tell us anything about the functional form of the dependence.

The variables in a model will typically depend upon further variables that are not explicitly included in the model. For instance, the level of the flame will also depend upon the presence of oxygen. Variables that are not explicitly represented in the model are assumed to be fixed at values that make the equations appropriate. For example, in our model of the gas grill, oxygen is assumed to be present in sufficient quantity to sustain a flame ranging in intensity from low to high.

In our example, the variables *Gas level*, *Flame,* and *Meat cooked* are *endogenous*, meaning that their values are determined by other variables in the model. *Gas connected, Gas knob, Igniter,* and *Meat on* are *exogenous*, meaning that their values are determined outside of the system. In all of the models that we will consider in section 3, the values of the exogenous variables are given or otherwise known.

Following Halpern (2016)[^halpern-2016], we will call an assignment of values to the exogenous variables a *context*. In an acyclic SEM, a context uniquely determines the values of all the variables in the model. An acyclic SEM together with a context is a *world* (what Halpern 2016 calls a “causal setting”)[^halpern-2016]. For instance, if we add the setting

- *Gas connected* = 1
- *Gas knob* = 3
- *Igniter* = 1
- *Meat on* = 1

to our three equations above, we get a world in which *Gas level* = 3, *Flame* = 3, and *Meat cooked* = 3.

The distinctively causal or “structural” content of a SEM derives from the way in which *interventions* are represented. To intervene on a variable is to set the value of that variable by a process that overrides the usual causal structure, without interfering with the causal processes governing the other variables. More precisely, an intervention on a variable *X* overrides the normal equation for *X*, while leaving the other equations unchanged. For example, to intervene on the variable *Flame* in our example would be to set the flame to a specified level regardless of whether the igniter is pressed or what the gas level is. (Perhaps, for example, one could pour kerosene into the grill and light it with a match.) Woodward (2003)[^woodward-2003] proposes that we think of an intervention as a causal process that operates independently of the other variables in the model. Randomized controlled trials aim to intervene in this sense. For example, a randomized controlled trial to test the efficacy of a drug for hypertension aims to determine whether each subject takes the drug (rather than a placebo) by a random process such as a coin flip. Factors such as education and health insurance that normally influence whether someone takes the drug no longer play this role for subjects in the trial population. Alternately, we could follow the approach of Lewis (1979)[^lewis-1979] and think of an intervention setting the value of a variable by a minor “miracle”.

To represent an intervention on a variable, we *replace* the equation for that variable with a new equation stating the value to which the variable is set. For example, if we intervene to set the level of flame at *low*, we would represent this by replacing the equation *Flame* = *Gas level* $\times$ *Igniter* with *Flame* = 1. This creates a new causal structure in which *Flame* is an exogenous variable; graphically, we can think of the intervention as “breaking the arrows” pointing into *Flame*. The new system of equations can then be solved to discover what values the other variables would take as a result of the intervention. In the world described above, our intervention would produce the following set of equations:

- *Gas connected* = 1
- *Gas knob* = 3
- *Igniter* = 1
- *Meat on* = 1
- *Gas level* = *Gas connected* × *Gas knob*
- *Flame* = *Gas level* × *Igniter*
- *Flame* = 1
- *Meat cooked* = *Flame* × *Meat on*

We have struck through the original equation for *Flame* to show that it is no longer operative. The result is a new world with a modified causal structure, with *Gas level* = 3, *Flame* = 1, and *Meat cooked* = 1. Since the equation connecting *Flame* to its causes is removed, any changes introduced by setting *Flame* to 1 will only propagate forward through the model to the descendants of *Flame*. The intervention changes the values of *Flame* and *Meat cooked*, but it does not affect the values of the other variables. We can represent interventions on multiple variables in the same way, replacing the equations for all of the variables intervened on.

Interventions help to give content to the arrows in the corresponding DAG. If variable $X_i$ is a parent of $X_j$, this means that there exists some setting for all of the other variables in the model, such that when we set those variables to those values by means of an intervention, intervening on $X_i$ can still make a difference for the value of $X_j$. For example, in our original model, *Gas level* is a parent of *Flame*. If we set the value of *Igniter* to 1 by means of an intervention, and set *Gas knob, Gas connected, Meat on,* and *Meat cooked* to any values at all, then intervening on the value of *Gas level* makes a difference for the value of *Flame*. Setting the value of *Gas level* to 1 would yield a value of 1 for *Flame*; setting *Gas level* to 2 yields a *Flame* of 2; and so on.

### 3.2 Structural Counterfactuals

A counterfactual is a proposition in the form of a subjunctive conditional. The antecedent posits some circumstance, typically one that is contrary to fact. For example, in our gas grill world, the flame was high, and the meat was well done. We might reason: “if the flame had been set to low, the meat would have been rare”. The antecedent posits a hypothetical state of affairs, and the consequent describes what would have happened in that hypothetical situation.

Deterministic SEMs naturally give rise to a logic of counterfactuals. These counterfactuals are called *structural* counterfactuals or *interventionist* counterfactuals. Structural counterfactuals are similar in some ways to what Lewis (1979)[^lewis-1979] calls *non-backtracking* counterfactuals. In a non-backtracking counterfactual, one does not reason backwards from a counterfactual supposition to draw conclusions about the causes of the hypothetical situation. For instance, one would not reason “If the meat had been cooked rare, then the flame would have been set to low”. Lewis (1979)[^lewis-1979] proposes that we think of the antecedent of a counterfactual as coming about through a minor “miracle”. The formalism for representing interventions described in the previous section prevents backtracking from effects to causes.

The logic of structural counterfactuals has been developed by Galles and Pearl (1998), Halpern (2000)[^halpern-2000], Briggs (2012)[^briggs-2012], and Zhang (2013a)[^zhang-2013a]. This section will focus on Briggs’ formulation; it has the richest language, but unlike the other approaches it can not be applied to causal models with cycles. Despite a shared concern with non-backtracking counterfactuals, Briggs’ logic differs in a number of ways from the more familiar logic of counterfactuals developed by Stalnaker (1968)[^stalnaker-1968] and Lewis (1973b)[^lewis-1973b].

We interpret the counterfactual conditional $A \boxright B$ as saying that *B* would be true, if *A* were made true by an intervention. The language of structural counterfactuals does not allow the connective ‘$A \boxright B$’ to appear in the antecedents of counterfactuals. More precisely, we define well-formed formulas (*wff*s) for the language inductively:

- Boolean propositions are *wff*s
- If *A* is a Boolean proposition, and *B* is a *wff*, then $A \boxright B$ is a *wff*

This means, for example, that $A \boxright (B\boxright (C\boxright D))$ is a *wff*, but $A\boxright ((B\boxright C)\boxright D)$ is not, since the embedded counterfactual in the consequent does not have a Boolean proposition as an antecedent.

Consider the world of the gas grill, described in the previous section:

- *Gas connected* = 1
- *Gas knob* = 3
- *Igniter* = 1
- *Meat on* = 1
- *Gas level* = *Gas connected* $\times$ *Gas knob*
- *Flame* = *Gas level* $\times$ *Igniter*
- *Meat cooked* = *Flame* $\times$ *Meat on*

To evaluate the counterfactual ${\textit{Flame} = 1} \boxright {\textit{Meat cooked} = 1}$ (if the flame had been set to *low*, the meat would have been cooked rare), we replace the equation for *Flame* with the assignment *Flame* = 1. We can then compute that *Meat cooked* = 1; the counterfactual is true. If the antecedent is a conjunction of atomic propositions, such as *Flame* = 1 and *Igniter* = 0, we replace all of the relevant equations. A special case occurs when the antecedent conjoins atomic propositions that assign different values to the same variable, such as *Flame* = 1 and *Flame* = 2. In this case, the antecedent is a contradiction, and the counterfactual is considered trivially true.

If the antecedent is a disjunction of atomic propositions, or a disjunction of conjunctions of atomic propositions, then the consequent must be true when *every* possible intervention or set of interventions described by the antecedent is performed. Consider, for instance,

$$ \begin{aligned} (({\textit{Flame}= 1} \amp {\textit{Gas level}= 0}) \lor ({\textit{Flame}= 2} \amp {\textit{Meat on}= 0}))\\ {} \boxright ({\textit{Meat cooked}= 1} \lor {\textit{Meat cooked}= 2}). \end{aligned} $$

If we perform the first intervention, we compute that *Meat cooked* = 1, so the consequent is true. However, if we perform the second intervention, we compute that *Meat cooked* = 0. Hence the counterfactual comes out false. Some negations are treated as disjunctions for this purpose. For example, ${\sim}(\textit{Flame} = 1)$ would be treated in the same way as the disjunction

$${\textit{Flame} = 0} \lor {\textit{Flame} = 2} \lor {\textit{Flame} = 3}.$$

If the consequent contains a counterfactual, we iterate the procedure. Consider the counterfactual:

$$\begin{align} {\textit{Flame} = 1}&\ \boxright\ ({\textit{Gas level} = 0}\ \boxright \\ & ({\textit{Flame} = 2} \boxright {\textit{Meat cooked} = 1})). \end{align}$$

To evaluate this counterfactual, we first change the equation for *Flame* to *Flame* = 1. Then we change the equation for *Gas level* to *Gas level* = 0. Then we change the equation for *Flame* again, from *Flame* = 1, to *Flame* = 2. Finally, we compute that *Meat cooked* = 2, so the counterfactual comes out false. Unlike the case where *Flame* = 1 and *Flame* = 2 are conjoined in the antecedent, the two different assignments for *Flame* do not generate an impossible antecedent. In this case, the interventions are performed in a specified order: *Flame* is first set to 1, and *then* set to 2.

The differences between structural counterfactuals and Stalnaker-Lewis counterfactuals stem from the following two features of structural counterfactuals:

1. The antecedent of a counterfactual is always thought of as being realized by an intervention, even if the antecedent is already true in a given world. For instance, in our gas grill world, *Flame* = 3. Nonetheless, if we evaluate a counterfactual with antecedent *Flame* = 3 in this world, we replace the equation for *Flame* with *Flame* = 3.
2. The truth values of counterfactuals are determined solely by the causal structures of worlds, together with the interventions specified in the their antecedents. No further considerations of *similarity* play a role. For example, the counterfactual $$ {\textit{Flame}= 1} \lor {\textit{Flame} = 2} \boxright {\textit{Flame}= 2} $$ would be false in our gas grill world (and indeed in all possible worlds). We do not reason that a world in which *Flame* = 2 is *closer* to our world (in which *Flame* = 3) than a world in which *Flame* = 1.

These features of structural counterfactuals lead to some unusual properties in the full language developed by Briggs (2012)[^briggs-2012]:

1. The analog of *modus ponens* fails for the structural conditional; i.e., from *A* and $A\boxright B$ we cannot infer *B*. For example, in our gas grill world, *Flame* = 3 and $$ {\textit{Flame} = 3} \boxright {({\textit{Gas level} = 2} \boxright {\textit{Meat cooked} = 3})} $$ are both true, but $$ {\textit{Gas level} = 2} \boxright {\textit{Meat cooked} = 3} $$ is false. To evaluate the last counterfactual, we replace the equation for *Gas level* with *Gas level* = 2. This results in *Flame* = 2 and *Meat cooked* = 2. To evaluate the prior counterfactual, we first substitute in the equation *Flame* = 3. Now, the value of *Flame* no longer depends upon the value of *Gas level*, so when we substitute in *Gas level* = 2, we get *Meat cooked* = 3. Even though the actual value of *Flame* is 3, we evaluate the counterfactual by intervening on *Flame* to set it to 3. With this intervention in place, a further intervention on *Gas level* makes no difference to *Flame* or *Meat cooked.*
2. The substitution of logically equivalent propositions into the antecedent of a counterfactual does not always preserve truth value. For example, $$ {\textit{Gas level} = 2} \boxright {\textit{Meat cooked} = 2} $$ is true, but $$\begin{align} & ({\textit{Gas level} = 2} \amp ({\textit{Flame} = 2} \lor {{\sim}(\textit{Flame} =2))}\\ & \qquad \boxright\, {\textit{Meat cooked} = 2} \end{align}$$ is false. The first counterfactual does not require us to intervene on the value of *Flame*, but the second counterfactual requires us to consider interventions that set *Flame* to all of its possible values.

To handle the second kind of case, Briggs (2012)[^briggs-2012] defines a relation of *exact* *equivalence* among Boolean propositions using the state space semantics of Fine (2012)[^fine-2012]. Within a world, the state that makes a proposition true is the collection of values of variables that contribute to the truth of the proposition. In our example world, the state that makes *Gas level* = 3 true is the valuation *Gas level* = 3. By contrast, the state that makes

$$\textit{Gas level} = 3 \amp (\textit{Flame} = 2 \lor {\sim}(\textit{Flame} = 2))$$

true includes both *Gas level* = 3 and *Flame* = 3. Propositions are exactly equivalent if they are made true by the same states in all possible worlds. The truth value of a counterfactual is preserved when exactly equivalent propositions are substituted into the antecedent.

Briggs (2012)[^briggs-2012] provides a sound and complete axiomatization for structural counterfactuals in acyclic SEMs. The axioms and inference rules of this system are presented in [Supplement on Briggs’ Axiomatization](causal-models.axiomatization.md).

### 3.3 Actual Causation

Many philosophers and legal theorists have been interested in the relation of *actual causation*. This concerns the assignment of causal responsibility for some event that occurs, based on how events actually play out. For example, suppose that Billy and Suzy are both holding rocks. Suzy throws her rock at a window, but Billy does not. Suzy’s rock hits the window, which breaks. Then Suzy’s throw was the actual cause of the window breaking.

We can represent this story easily enough with a structural equation model. For variables, we choose:

- $B = 1$ if Billy throws, 0 if he doesn’t
- $S = 1$ if Suzy throws, 0 if she doesn’t
- $W = 1$ if the window shatters, 0 if it doesn’t

Our context and equation will then be:

- $B = 0$
- $S = 1$
- $W = \max(B, S)$

The equation for *W* tells us that the window would shatter if either Billy or Suzy throws their rock. The corresponding DAG is shown in Figure 4

![diagram: B has an arrow pointing northeast to W and S has an arrow pointing northwest to the same W](../assets/causal-models/fig4.svg)

\*Figure 4\*

But we cannot simply read off the relation of actual causation from the graph or from the equations. For example, the arrow from *B* to *W* in Figure 4 cannot be interpreted as saying that Billy’s (in)action is an actual cause of the window breaking. Note that while it is common to distinguish between singular or token causation, and general or type-level causation (see, e.g., Eells 1991, Introduction)[^eells-1991], that is not what is at issue here. Our causal model does not represent any kind of causal generalization: it represents the actual and possible actions of Billy and Suzy at one particular place and time. Actual causation is not just causal structure of the single case. A further criterion for actual causation, defined in terms of the causal structure together with the actual values of the variables, is needed.

Following Lewis (1973a)[^lewis-1973a], it is natural to try to analyze the relation of actual causation in terms of *counterfactual dependence.* In our model, the following propositions are all true:

- $S = 1$
- $W = 1$
- ${S = 0}\boxright {W = 0}$

In words: Suzy threw her rock, the window shattered, and if Suzy hadn’t thrown her rock, the window wouldn’t have shattered. In general, we might attempt to analyze actual causation as follows:

$X = x$ is an actual cause of $Y = y$ in world *w* just in case:

- *X* and *Y* are different variables
- $X = x$ and $Y = y$ in *w*
- There exist $x' \ne x$ and $y' \ne y$ such that ${X = x'} \boxright {Y = y'}$ is true in *w*

Unfortunately, this simple analysis will not work, for familiar reasons involving *preemption* and *overdetermination*. Here is an illustration of each:

*Preemption:* Billy decides that he will give Suzy the opportunity to throw first. If Suzy throws her rock, he will not throw, but if she doesn’t throw, he will throw and his rock will shatter the window. In fact, Suzy throws her rock, which shatters the window. Billy does not throw.

*Overdetermination:* Billy and Suzy throw their rocks simultaneously. Their rocks hit the window at the same time, shattering it. Either rock by itself would have been sufficient to shatter the window.

In both of these cases, Suzy’s throw is an actual cause of the window’s shattering, but the shattering does not counterfactually depend upon her throw: if Suzy hadn’t thrown her rock, Billy’s rock would have shattered the window. Much of the work on counterfactual theories of causation since 1973 has been devoted to addressing these problems.

A number of authors have used SEMs to try to formulate adequate analyses of actual causation in terms of counterfactuals, including Beckers & Vennekens (2018), Glymour & Wimberly (2007), Halpern (2016)[^halpern-2016], Halpern & Pearl (2001, 2005), Hitchcock (2001)[^hitchcock-2001], Pearl (2009: Chapter 10), Weslake (forthcoming), and Woodward (2003: Chapter 2). As an illustration, consider one analysis based closely on a proposal presented in Halpern (2016)[^halpern-2016]:

(**AC**) $X = x$ is an actual cause of $Y = y$ in world *w* just in case:

1. *X* and *Y* are different variables
2. $X = x$ and $Y = y$ in *w*
3. There exist disjoint sets of variables $\bX$ and $\bZ$ with $X \in \bX$, with values $\bX = \bx$ and $\bZ = \bz$ in *w*, such that:
4. There exists $\bx' \ne \bx$ such that $$({\bX = \bx'} \amp {\bZ = \bz}) \boxright {Y \ne y}$$ is true in *w*
5. No subset of $\bX$ satisfies (3a)

That is, *X* belongs to a minimal set of variables $\bX$, such that when we intervene to hold the variables in $\bZ$ fixed at the values they actually take in *w*, *Y* counterfactually depends upon the values of the variables in $\bX.$ We will illustrate this account with our examples of preemption and overdetermination.

In *Preemption*, let the variables *B*, *S*, and *W* be defined as above. Our context and equations are:

- $S = 1$
- $B = 1 - S$
- $W = \max(B, S)$

That is: Suzy throws her rock; Billy will throw his rock if Suzy doesn’t; and the window will shatter if either throws their rock. The DAG is shown in Figure 5.

![diagram: B has an arrow pointing northeast to W and S has an arrow pointing northwest to the same W. S also has an arrow pointing west to the same B.](../assets/causal-models/fig5.svg)

\*Figure 5\*

We want to show that $S = 1$ is an actual cause of $W = 1$. Conditions AC(1) and AC(2) are clearly satisfied. For condition AC(3), we choose $\bX = \{S\}$ and $\bZ = \{B\}$. Since $B = 0$ in *Preemption*, we want to fix $B = 0$ while varying *S*. We can see easily that ${S = 0} \amp {B = 0} \boxright {W = 0}$: replacing the two equations for *B* and *S* with $B = 0$ and $S = 0$, the solution yields $W = 0$. In words, this counterfactual says that if neither Billy nor Suzy had thrown their rock, the window would not have shattered. Thus condition AC(3a) is satisfied. AC(3b) is satisfied trivially, since $\bX = \{S\}$ is a singleton set.

Here is how AC works in this example. *S* influences *W* along two different paths: the direct path $S \rightarrow W$ and the indirect path $S \rightarrow B \rightarrow W$. These two paths interact in such a way that they cancel each other out, and the value of *S* makes no net difference to the value of *W*. However, by holding *B* fixed at its actual value of 0, we eliminate the influence of *S* on *W* along that path. The result is that we isolate the contribution that *S* made to *W* along the direct path. AC defines actual causation as a particular kind of *path-specific* effect.

To treat *Overdetermination*, let *B*, *S*, and *W* keep the same meanings. Our setting and equation will be:

- $B = 1$
- $S = 1$
- $W = \max(B, S)$

The graph is the same as that shown in Figure 4 above. Again, we want to show that $S = 1$ is an actual cause of $W = 1$. Conditions AC(1) and AC(2) are obviously satisfied. For AC(3), we choose $\bX = \{B, S\}$ and $\bZ = \varnothing$. For condition AC(3a), we choose for our alternate setting $\bX = \bx'$ $B = 0$ and $S = 0$. Once again, the counterfactual ${S = 0} \amp {B = 0} \boxright {W = 0}$ is true. Now, for AC(3b) we must show that $\bX = \{B, S\}$ is minimal. It is easy to check that $\{B\}$ alone won’t satisfy AC(3a). Whether we take $\bZ = \varnothing$ or $\bZ = \{S\}$, changing *B* to 0 (perhaps while also setting *S* to 1) will not change the value of *W*. A parallel argument shows that $\{S\}$ alone won’t satisfy AC(3a) either. The key idea here is that *S* is a member of a minimal set of variables that need to be changed in order to change the value of *W*.

Despite these successes, none of the analyses of actual causation developed so far perfectly captures our pre-theoretic intuitions in every case. One strategy that has been pursued by a number of authors is to incorporate some distinction between *default* and *deviant* values of variables, or between *normal* and *abnormal* conditions. See, e.g., Hall (2007)[^hall-2007], Halpern (2008; 2016: Chapter 3), Halpern & Hitchcock (2015), Hitchcock (2007)[^hitchcock-2007], and Menzies (2004)[^menzies-2004]. Blanchard & Schaffer (2017) present arguments against this approach. Glymour et al. (2010) raise a number of problems for the project of trying to analyze actual causation.

## 4. Probabilistic Causal Models

In this section, we will discuss causal models that incorporate probability in some way. Probability may be used to represent our uncertainty about the value of unobserved variables in a particular case, or the distribution of variable values in a population. Often we are interested in when some feature of the causal structure of a system can be *identified* from the probability distribution over values of variables, perhaps in conjunction with background assumptions and other observations. For example, we may know the probability distribution over a set of variables $\bV$, and want to know which causal structures over the variables in $\bV$ are compatible with the distribution. In realistic scientific cases, we never directly observe the true probability distribution P over a set of variables. Rather, we observe finite data that approximate the true probability when sample sizes are large enough and observation protocols are well-designed. We will not address these important practical concerns here. Rather, our focus will be on what it is possible to infer from probabilities, in principle if not in practice. We will also consider the application of probabilistic causal models to decision theory and counterfactuals.

### 4.1 Structural Equation Models with Random Errors

We can introduce probability into a SEM by means of a probability distribution over the exogenous variables.

Let $\bV = \{X_1, X_2 ,\ldots ,X_n\}$ be a set of endogenous variables, and $\bU = \{U_1, U_2 ,\ldots ,U_n\}$ a corresponding set of exogenous variables. Suppose that each endogenous variable $X_i$ is a function of its parents in $\bV$ together with $U_i$, that is:

$$X_i = f_i (\bPA(X_i), U_i).$$

As a general rule, our graphical representation of this SEM will include only the endogenous variables $\bV$, and we use $\bPA(X_i)$ to denote the set of *endogenous* parents of $X_i . U_i$ is sometimes called an *error* variable for $X_i$: it is responsible for any difference between the actual value of $X_i$ and the value predicted on the basis of $\bPA(X_i)$ alone. We may think of $U_i$ as encapsulating all of the causes of $X_i$ that are not included in $\bV$. The assumption that each endogenous variable has exactly one error variable is innocuous. If necessary, $U_i$ can be a vector of variables. For example, if $Y_1$, $Y_2$, and $Y_3$ are all causes of $X_i$ that are not included in $\bV$, we can let $U_i = \langle Y_1, Y_2, Y_3\rangle$. Moreover, the error variables need not be distinct or independent from one another.

Assuming that the system of equations is acyclic, an assignment of values to the exogenous variables $U_1$, $U_2$,… ,$U_n$ uniquely determines the values of all the variables in the model. Then, if we have a probability distribution $\Pr'$ over the values of variables in $\bU$, this will induce a unique probability distribution P on $\bV$.

### 4.2 The Markov Condition

Suppose we have a SEM with endogenous variables $\bV$, exogenous variables $\bU$, probability distribution P on $\bU$ and $\bV$ as described in the previous section, and DAG $\bG$ representing the causal structure on $\bV$. Pearl and Verma (1991) prove that if the error variables $U_i$ are probabilistically independent in P, then the probability distribution on $\bV$ will satisfy the *Markov Condition* (MC) with respect to $\bG$. The Markov Condition has several formulations, which are equivalent when $\bG$ is a a DAG (Pearl 1988)[^pearl-1988]:

| (MC_{Screening_off}) | For every variable *X* in $\bV$, and every set of variables $\bY \subseteq \bV \setminus \bDE(X)$, $\Pr(X \mid \bPA(X) \amp \bY) = \Pr(X \mid \bPA(X))$. |
| --- | --- |
| (MC_{Factorization}) | Let $\bV = \{X_1, X_2 , \ldots ,X_n\}$. Then $\Pr(X_1, X_2 , \ldots ,X_n) = \prod_i \Pr(X_i \mid \bPA(X_i))$. |
| (MC_{*d*-separation}) | Let $X, Y \in \bV, \bZ \subseteq \bV \setminus \{X, Y\}$. Then $\Pr(X, Y \mid \bZ) = \Pr(X \mid \bZ) \times \Pr(Y \mid \bZ)$ if $\bZ$ *d*-separates *X* and *Y* in $\bG$ (explained below). |

Let us take some time to explain each of these formulations.

MC_{Screening_off} says that the parents of variable *X* screen *X* off from all other variables, except for the descendants of *X*. Given the values of the variables that are parents of *X*, the values of the variables in $\bY$ (which includes no descendants of $X)$, make no further difference to the probability that *X* will take on any given value.

MC_{Factorization} tells us that once we know the conditional probability distribution of each variable given its parents, $\Pr(X_i \mid \bPA(X_i))$, we can compute the complete joint distribution over all of the variables. It is relatively easy to see that MC_{Factorization} follows from MC_{Screening_off}. Since $\bG$ is acyclic, we may re-label the subscripts on the variables so that they are ordered from ‘earlier’ to ‘later’, with only earlier variables being ancestors of later ones. It follows from the probability calculus that $$\begin{align} \Pr(X_1, X_2 , &\ldots ,X_n)\ = \\ &\Pr(X_1) \times \Pr(X_2 \mid X_1) \times \ldots \times \Pr(X_n \mid X_1, X_2 , \ldots ,X_{n-1}) \end{align}$$ (this is a version of the theorem of total probability). For each term $\Pr(X_i \mid X_1, X_2 , \ldots ,X_{i-1})$, our ordering ensures that all of the parents of $X_i$ will be included on the right hand side, and none of its descendants will. MC_{Screening_off} then tells us that we can eliminate all of the terms from the right hand side except for the parents of $X_i$.

MC_{*d*-separation} introduces the graphical notion of *d*-separation. As noted above, a path from *X* to *Y* is a sequence of variables $\langle X = X_1 , \ldots ,X_k = Y\rangle$ such that for each $X_i$, $X_{i+1}$, there is either an arrow from $X_i$ to $X_{i+1}$or an arrow from $X_{i+1}$ to $X_i$ in $\bG$. A variable $X_i , 1 \lt i \lt k$ is a *collider* on the path just in case there is an arrow from $X_{i-1}$ to $X_i$ and from $X_{i+1}$ to $X_i$. In other words, $X_i$ is a collider just in case the arrows converge on $X_i$ in the path. Let $\bX, \bY$, and $\bZ$ be disjoint subsets of $\bV$. $\bZ$ *d*-separates $\bX$ and $\bY$ just in case every path $\langle X_1 , \ldots ,X_k\rangle$ from a variable in $\bX$ to a variable in $\bY$ contains at least one variable $X_i$ such that either: (i) $X_i$ is a collider, and no descendant of $X_i$ (including $X_i$ itself) is in $\bZ$; or (ii) $X_i$ is not a collider, and $X_i$ is in $\bZ$. Any path that meets this condition is said to be *blocked* by $\bZ$. If $\bZ$ does not *d*-separate $\bX$ and $\bY$, then $\bX$ and $\bY$ are *d-connected* by $\bZ$.

Note that MC provides sufficient conditions for variables to be probabilistically independent, conditional on others, but no necessary condition.

Here are some illustrations:

![diagram: T has an arrow pointing north to W; W has a long arrow pointing northeast to Z; W also has an arrow pointing northwest to X; X has an arrow pointing northwest to Y](../assets/causal-models/fig6.svg)

\*Figure 6\*

In Figure 6, MC implies that *X* screens *Y* off from all of the other variables, and *W* screens *Z* off from all of the other variables. This is most easily seen from MC_{Screening_off}. *W* also screens *T* off from all of the other variables, which is most easily seen from MC_{*d*-separation}. *T* does not necessarily screen *Y* off from *Z* (or indeed anything from anything).

![diagram: X has an arrow pointing northeast to Y and Z has an arrow pointing northwest to the same Y.](../assets/causal-models/fig7.svg)

\*Figure 7\*

In Figure 7, MC entails that *X* and *Z* will be unconditionally independent, but not that they will be independent conditional on *Y*. This is most easily seen from MC_{*d*-separation}.

Let $V_i$ and $V_j$ be two distinct variables in $\bV$, with corresponding exogenous error variables $U_i$ and $U_j$, representing causes of $V_i$ and $V_j$ that are excluded from the $\bV$. Suppose $V_i$ and $V_j$ share at least one common cause that is excluded from $\bV$. In this case, we would not expect $U_i$ and $U_j$ to be probabilistically independent, and the theorem of Pearl and Verma (1991) would not apply. In this case, the causal relationship among the variables in $\bV$ would not be appropriately represented by a DAG, but would require an acyclic directed mixed graph (ADMG) with a double-headed arrow connecting $V_i$ and $V_j$. We will discuss this kind of case in more detail in Section 4.6 below.

MC is not expected to hold for arbitrary sets of variables $\bV$, even when the DAG $\bG$ accurately represents the causal relations among those variables. For example, (MC) will typically fail in the following kinds of case:

1. In an EPR (Einstein-Podolski-Rosen) set-up, we have two particles prepared in the singlet state. If *X* represents a spin measurement on one particle, *Y* a spin measurement (in the same direction) on the other, then *X* and *Y* are perfectly anti-correlated. (One particle will be spin-up just in case the other is spin-down.) The measurements can be conducted sufficiently far away from each other that it is impossible for one outcome to causally influence the other. However, it can be shown that there is no (local) common cause *Z* that screens off the two measurement outcomes.
2. The variables in $\bV$ are not appropriately distinct. For example, suppose that *X*, *Y*, and *Z* are variables that are probabilistically independent and causally unrelated. Now define $U = X + Y$ and $W = Y + Z$, and let $\bV = \{U, W\}$. Then *U* and *W* will be probabilistically dependent, even though there is no causal relation between them.
3. MC may fail if the variables are too coarsely grained. Suppose *X*, *Y*, and *Z* are quantitative variables. *Z* is a common cause of *X* and *Y*, and neither *X* nor *Y* causes the other. Suppose we replace *Z* with a coarser variable, $Z'$ indicating only whether *Z* is high or low. Then we would not expect $Z'$ to screen *X* off from *Y*. The value of *X* may well contain information about the value of *Z* beyond what is given by $Z'$, and this may affect the probability of *Y*.

Both SGS (2000) and Pearl (2009)[^pearl-2009] contain statements of a principle called the *Causal Markov Condition* (CMC). The statements are in fact quite different from one another. In Pearl’s formulation, (CMC) is just a statement of the mathematical theorem described above: If each variable in $\bV$ is a deterministic product of its parents in $\bV$, together with an error term; and the errors are probabilistically independent of each other; then the probability distribution on $\bV$ will satisfy (MC) with respect to the DAG $\bG$ representing the functional dependence relations among the variables in $\bV$. Pearl interprets this result in the following way: Macroscopic systems, he believes, are deterministic. In practice, however, we never have access to all of the causally relevant variables affecting a macroscopic system. But if we include enough variables in our model so that the excluded variables are probabilistically independent of one another, then our model will satisfy the MC, and we will have a powerful set of analytic tools for studying the system. Thus MC characterizes a point at which we have constructed a useful approximation of the complete system.

In SGS (2000), the (CMC) has more the status of an empirical posit. If $\bV$ is set of macroscopic variables that are well-chosen, meaning that they are free from the sorts of defects described above; $\bG$ is a DAG representing the causal structure on $\bV$; and P is the empirical probability distribution resulting from this causal structure; then P can be expected to satisfy MC relative to $\bG$. They defend this assumption in (at least) two ways:

1. Empirically, it seems that a great many systems do in fact satisfy MC.
2. Many of the methods that are in fact used to detect causal relationships tacitly presuppose the MC. In particular, the use of randomized trials presupposes a special case of the MC. Suppose that an experimenter determines randomly which subjects will receive treatment with a drug $(D = 1)$ and which will receive a placebo $(D = 0)$, and that under this regimen, treatment is probabilistically correlated with recovery $(R)$. The effect of randomization is to eliminate all of the parents of *D*, so MC tells us that if *R* is not a descendant of *D*, then *R* and *D* should be probabilistically independent. If we do not make this assumption, how can we infer from the experiment that *D* is a cause of *R*?

Cartwright (1993, 2007: chapter 8) has argued that MC need not hold for genuinely indeterministic systems. Hausman and Woodward (1999, 2004) attempt to defend MC for indeterministic systems.

A causal model that comprises a DAG and a probability distribution that satisfies MC is called a *causal Bayes net.*

### 4.3 The Minimality and Faithfulness Conditions

The MC states a sufficient condition but not a necessary condition for conditional probabilistic independence. As such, the MC by itself can never entail that two variables are conditionally or unconditionally dependent. The Minimality and Faithfulness Conditions are two conditions that give necessary conditions for probabilistic independence. (This is employing the terminology of Spirtes et al. (SGS 2000). Pearl (2009)[^pearl-2009] contains a “Minimality Condition” that is slightly different from the one described here.)

(i) *The Minimality Condition*. Suppose that the DAG $\bG$ on variable set $\bV$ satisfies MC with respect to the probability distribution P. The Minimality Condition asserts that no sub-graph of $\bG$ over $\bV$ also satisfies the Markov Condition with respect to P. As an illustration, consider the variable set $\{X, Y\}$, let there be an arrow from *X* to *Y*, and suppose that *X* and *Y* are probabilistically independent of each other. This graph would satisfy the MC with respect to P: none of the independence relations mandated by the MC are absent (in fact, the MC mandates no independence relations). But this graph would violate the Minimality Condition with respect to P, since the subgraph that omits the arrow from *X* to *Y* would also satisfy the MC. The Minimality Condition implies that if there is an arrow from *X* to *Y*, then *X* makes a probabilistic difference for *Y*, conditional on the other parents of *Y*. In other words, if $\bZ = \bPA(Y) \setminus \{X\}$, there exist $\bz$, *y*, *x*, $x'$ such that $\Pr(Y = y \mid X = x \amp \bZ = \bz) \ne \Pr(Y = y \mid X = x' \amp \bZ = \bz)$.

(ii) *The Faithfulness Condition*. The Faithfulness Condition (FC) is the converse of the Markov Condition: it says that all of the (conditional and unconditional) probabilistic independencies that exist among the variables in $\bV$ are *required* by the MC. For example, suppose that $\bV = \{X, Y, Z\}$. Suppose also that *X* and *Z* are unconditionally independent of one another, but dependent, conditional upon *Y*. (The other two variable pairs are dependent, both conditionally and unconditionally.) The graph shown in Figure 8 does not satisfy FC with respect to this distribution (colloquially, the graph is not faithful to the distribution). MC, when applied to the graph of Figure 8, does not imply the independence of *X* and *Z*. This can be seen by noting that *X* and *Z* are *d*-connected (by the empty set): neither the path $X \rightarrow Z$ nor $X \rightarrow Y\rightarrow Z$ is blocked (by the empty set). By contrast, the graph shown in Figure 7 above is faithful to the described distribution. Note that Figure 8 does satisfy the Minimality Condition with respect to the distribution; no subgraph satisfies MC with respect to the described distribution. In fact, FC is strictly stronger than the Minimality Condition.

![diagram: X has an arrow pointing northeast to Y and another arrow pointing east to Z; Y has an arrow pointing southeast to Z.](../assets/causal-models/fig8.svg)

\*Figure 8\*

Here are some other examples: In Figure 6 above, there is a path $W\rightarrow X\rightarrow Y$; FC implies that *W* and *Y* should be probabilistically dependent. In Figure 7, FC implies that *X* and *Z* should be dependent, conditional on *Y*.

FC can fail if the probabilistic parameters in a causal model are just so. In Figure 8, for example, *X* influences *Z* along two different directed paths. If the effect of one path is to exactly undo the influence along the other path, then *X* and *Z* will be probabilistically independent. If the underlying SEM is linear, Spirtes et al. (SGS 2000: Theorem 3.2) prove that the set of parameters for which Faithfulness is violated has Lebesgue measure 0. Nonetheless, parameter values leading to violations of FC are *possible*, so FC does not seem plausible as a metaphysical or conceptual constraint upon the connection between causation and probabilities. It is, rather, a *methodological* principle: Given a distribution on $\{X, Y, Z\}$ in which *X* and *Z* are independent, we should prefer the causal structure depicted in Figure 7 to the one in Figure 8. This is not because Figure 8 is conclusively ruled out by the distribution, but rather because it is preferable to postulate a causal structure that *implies* the independence of *X* and *Z* rather than one that is merely *consistent* with independence. See Zhang and Spirtes 2016 for comprehensive discussion of the role of FC.

Violations of FC are often detectable in principle. For example, suppose that the true causal structure is that shown in Figure 7, and that the probability distribution over *X*, *Y*, and *Z* exhibits all of the conditional independence relations required by MC. Suppose, moreover, that *X* and *Z* are independent, conditional upon *Y*. This conditional independence relation is not entailed by MC, so it constitutes a violation of FC. It turns out that there is no DAG that is faithful to this probability distribution. This tips us off that there is a violation of FC. While we will not be able to infer the correct causal structure, we will at least avoid inferring an incorrect one in this case. For details, see Steel 2006, Zhang & Spirtes 2008, and Zhang 2013b.

Researchers have explored the consequences of adopting a variety of assumptions that are weaker than FC; see for example Ramsey et al. 2006, Spirtes & Zhang 2014, and Zhalama et al. 2016.

### 4.4 Identifiability of Causal Structure

If we have a set of variables $\bV$ and know the probability distribution P on $\bV$, what can we infer about the causal structure on $\bV$? This epistemological question is closely related to the metaphysical question of whether it is possible to *reduce* causation to probability (as, e.g., Reichenbach 1956 and Suppes 1970 proposed)[^reichenbach-1956][^suppes-1970].

Pearl (1988: Chapter 3) proves the following theorem:

(**Identifiability with time-order**) If

1. the variables in $\bV$ are time-indexed, such that only earlier variables can cause later ones;
2. the probability P assigns positive probability to every possible assignment of values of the variables in $\bV$;
3. there are no latent variables, so that the correct causal graph $\bG$ is a DAG;
4. and the probability measure P satisfies the Markov and Minimality Conditions with respect to $\bG$;

then it will be possible to uniquely identify $\bG$ on the basis of P.

It is relatively easy to see why this holds. For each variable $X_i$, its parents must come from among the variables with lower time indices, call them $X_1 ,\ldots ,X_{i-1}$. Any variables in this group that are not parents of $X_i$ will be nondescendants of $X_i$; hence they will be screened off from $X_i$ by its parents (from MC_{Screening_off}). Thus we can start with the distributions $\Pr(X_i\mid X_1 ,\ldots ,X_{i-1})$, and then weed out any variables from the right hand side that make no difference to the probability distribution over $X_i$. By the Minimality Condition, we know that the variables so weeded are not parents of $X_i$. Those variables that remain are the parents of $X_i$ in $\bG$.

If we don’t have information about time ordering, or other substantive assumptions restricting the possible causal structures among the variables in $\bV$, then it will not always be possible to identify the causal structure from probability alone. In general, given a probability distribution P on $\bV$, it is only possible to identify a *Markov equivalence class* of causal structures. This will be the set of all DAGs on $\bV$ that (together with MC) imply all and only the conditional independence relations contained in P. In other words, it will be the set of all DAGs $\bG$ such that P satisfies MC and FC with respect to $\bG$. The PC algorithm described by SGS (2000: 84–85) is one algorithm that generates the Markov equivalence class for any probability distribution with a non-empty Markov equivalence class.

Consider two simple examples involving three variables $\{X, Y, Z\}$. Suppose our probability distribution has the following properties:

- *X* and *Y* are dependent unconditionally, and conditional on *Z*
- *Y* and *Z* are dependent unconditionally, and conditional on *X*
- *X* and *Z* are dependent unconditionally, but independent conditional on *Y*

Then the Markov equivalence class is:

$$ X \rightarrow Y \rightarrow Z\\ X \leftarrow Y \leftarrow Z\\ X \leftarrow Y \rightarrow Z $$

We cannot determine from the probability distribution, together with MC and FC, which of these structures is correct.

On the other hand, suppose the probability distribution is as follows:

- *X* and *Y* are dependent unconditionally, and conditional on *Z*
- *Y* and *Z* are dependent unconditionally, and conditional on *X*
- *X* and *Z* are independent unconditionally, but dependent conditional on *Y*

Then the Markov equivalence class is:

$$ X \rightarrow Y \leftarrow Z $$

This is the only DAG relative to which the given probability distribution satisfies MC and FC.

### 4.5 Identifiability with Assumptions about Functional Form

Suppose we have a SEM with endogenous variables $\bV$ and exogenous variables $\bU$, where each variable in $\bV$ is determined by an equation of the form:

$$X_i = f_i (\bPA(X_i), U_i).$$

Suppose, moreover, that we have a probability distribution $\Pr'$ on $\bU$ in which all of the $U_i$s are independent. This will induce a probability distribution P on $\bV$ that satisfies MC relative to the correct causal DAG on $\bV$. In other words, our probabilistic SEM will generate a unique causal Bayes net. The methods described in the previous section attempt to infer the underlying graph $\bG$ from relations of probabilistic dependence and independence. These methods can do no better than identifying the Markov equivalence class. Can we do better by making use of additional information about the probability distribution P, beyond relations of dependence and independence?

There is good news and there is bad news. First the bad news. If the variables in $\bV$ are discrete, and we make no assumptions about the form of the functions $f_i$, then we can infer no more about the SEM than the Markov equivalence to which the graph belongs (Meek 1995)[^meek-1995].

More bad news: If the variables in $\bV$ are continuous, the simplest assumption, and the one that has been studied in most detail, is that the equations are *linear* with *Gaussian* (normal, or bell-shaped) errors. That is:

- $X_i = \sum_j c_j X_j + U_i$, where *j* ranges over the indices of $\bPA(X_i)$ and the $c_j$s are constants
- $Pr'$ assigns a Gaussian distribution to each $U_i$

It turns out that with these assumptions, we can do no better than inferring the Markov equivalence class of the causal graph on $\bV$ from probabilistic dependence and independence (Geiger & Pearl 1988)[^geiger-1988][^pearl-1988].

Now for the good news. There are fairly general assumptions that allow us to infer a good deal more. Here are some fairly simple cases:

(**LiNGaM**) (Shimizu et al. 2006)[^shimizu-2006] If:

1. The variables in $\bV$ are continuous;
2. The functions $f_i$ are linear;
3. The probability distributions on the error variables $U_i$ are not Gaussian (or at most one is Gaussian);
4. The error variables $U_i$ are probabilistically independent in $\Pr'$;

then the correct DAG on $\bV$ can be uniquely determined by the induced probability distribution P on $\bV$.

(**Non-linear additive**) (Hoyer et al. 2009)[^hoyer-2009] Almost all functions of the following form allow the correct DAG on $\bV$ to be uniquely determined by the induced probability distribution P on $\bV$.:

1. The functions $f_i$ are nonlinear and the errors are additive (so $X_i = f_i (\bPA(X_i)) + U_i$, with $f_i$ nonlinear);
2. The error variables $U_i$ are probabilistically independent in $\Pr'$;

In fact, this case can be generalized considerably:

(**Post non-linear**) (Zhang & Hyvärinen 2009)[^zhang-2009] With the exception of five specific cases that can be fully specified, all functions of the following form allow the correct DAG on $\bV$ to be uniquely determined by the induced probability distribution P on $\bV$.:

1. The functions have the form $X_i = g_i (f_i (\bPA(X_i)) + U_i)$ with $f_i$ and $g_i$ nonlinear, and $g_i$ invertible;
2. The error variables $U_i$ are probabilistically independent in $\Pr'$;

See also Peters et al. (2017) for discussion.

While there are specific assumptions behind these results, they are nonetheless remarkable. They entail, for example, that (given the assumptions of the theorems) knowing only the probability distribution on two variables *X* and *Y*, we can infer whether *X* causes *Y* or *Y* causes *X*.

### 4.6 Latent Common Causes

The discussion so far has focused on the case where there are no latent common causes of the variables in $\bV$, and the error variables $U_i$ can be expected to be probabilistically independent. As we noted in Section 2.3 above, we represent a latent common cause with a double-headed arrow. For example, the acyclic directed mixed graph in Figure 9 represents a latent common cause of *X* and *Z*. More generally, we can use an ADMG like Figure 9 to represent that the error variables for *X* and *Z* are not probabilistically independent.

![diagram: X has an arrow pointing east to Y which in turn has an arrow pointing east to Z; X and Z are connected by a curved double-headed arrow](../assets/causal-models/fig9.svg)

\*Figure 9\*

If there are latent common causes, we expect MC_{Screening_off} and MC_{Factorization} to fail if we apply them in a naïve way. In Figure 9, *Y* is the only parent of *Z* shown in the graph, and if we try to apply MC_{Screening_off}, it tells us that *Y* should screen *X* off from *Z*. However, we would expect *X* and *Z* to be correlated, even when we condition on *Y*, due to the latent common cause. The problem is that the graph is missing a relevant parent of *Z*, namely the omitted common cause. However, suppose that the probability distribution on $\{L, X, Y, Z\}$ satisfies MC with respect to the DAG that includes *L* as a common cause of *X* and *Z*. Then it turns out that the probability distribution will *still* satisfy MC_{*d*-separation} with respect to the ADMG of Figure 9. A causal model incorporating an ADMG and probability distribution satisfying MC_{*d*-separation} is called a *semi-Markov causal model* (SMCM).

If we allow that the correct causal graph may be an ADMG, we can still apply MC_{*d*-separation}, and ask which graphs imply the same sets of conditional independence relations. The Markov equivalence class will be larger than it was when we did not allow for latent variables. For instance, suppose that the probability distribution on $\{X, Y, Z\}$ has the following features:

- *X* and *Y* are dependent unconditionally, and conditional on *Z*
- *Y* and *Z* are dependent unconditionally, and conditional on *X*
- *X* and *Z* are independent unconditionally, but dependent conditional on *Y*

We saw in Section 4.4 that the only DAG that implies just these (in)dependencies is:

$$ X \rightarrow Y \leftarrow Z $$

But if we allow for the possibility of latent common causes, there will be additional ADMGs that also imply just these (in)dependencies. For example, the structure

$$ X \leftrightarrow Y \leftrightarrow Z $$

is also in the Markov equivalence class, as are several others.

Latent variables present a further complication. Unlike the case where the error variables $U_i$ are probabilistically independent, a SEM with correlated error terms may imply probabilistic constraints in addition to conditional (in)dependence relations, even in the absence of further assumptions about functional form. This means that we may be able to rule out some of the ADMGs in the Markov equivalence class using different kinds of probabilistic constraints.

### 4.7 Interventions

A conditional probability such as $\Pr(Y = y \mid X = x)$ gives us the probability that *Y* will take the value *y*, given that *X* has been *observed* to take the value *x*. Often, however, we are interested in predicting the value of *Y* that will result if we *intervene* to set the value of *X* equal to some particular value *x*. Pearl (2009)[^pearl-2009] writes $\Pr(Y = y \mid \ido(X = x))$ to characterize this probability. The notation is misleading, since $\ido(X = x)$ is not an event in the original probability space. It might be more accurate to write $\Pr_{\ido(X = x)} (Y = y)$, but we will use Pearl’s notation here. What is the difference between observation and intervention? When we merely observe the value that a variable takes, we are learning about the value of the variable when it is caused in the normal way, as represented in our causal model. Information about the value of the variable will also provide us with information about its causes, and about other effects of those causes. However, when we intervene, we override the normal causal structure, forcing a variable to take a value it might not have taken if the system were left alone. Graphically, we can represent the effect of this intervention by eliminating the arrows directed into the variable intervened upon. Such an intervention is sometimes described as “breaking” those arrows. As we saw in Section 3.1, in the context of a SEM, we represent an intervention that sets *X* to *x* by replacing the equation for *X* with a new one specifying that $X = x$.

As we saw in Section 3.2, there is a close connection between interventions and counterfactuals; in particular, the antecedents of structural counterfactuals are thought of as being realized by interventions. Nonetheless, Pearl (2009)[^pearl-2009] distinguishes claims about interventions represented by the *do* operator from counterfactuals. The former are understood in the indicative mood; they concern interventions that are actually performed. Counterfactuals are in the subjunctive mood, and concern hypothetical interventions. This leads to an important epistemological difference between ordinary interventions and counterfactuals: they behave differently in the way that they interact with observations of the values of variables. In the case of interventions, we are concerned with evaluating probabilities such as

$$\Pr(\bY = \by \mid \bX =\bx, \ido(\bZ = \bz)).$$

We assume that the intervention $\ido(\bZ = \bz)$ is being performed in the actual world, and hence that we are observing the values that other variables take $(\bX =\bx)$ in the same world where the intervention takes place. In the case of counterfactuals, we observe the value of various variables in the actual world, in which there is no intervention. We then ask what *would* have happened if an intervention *had been* performed. The variables whose values we observed may well take on *different* values in the hypothetical world where the intervention takes place. Here is a simple illustration of the difference. Suppose that we have a causal model in which treatment with a drug causes recovery from a disease. There may be other variables and causal relations among them as well.

Intervention:

- An intervention was performed to treat a particular patient with the drug, and it was observed that she did not recover.
- Question: What is the probability that she recovered, given the intervention and the observed evidence?
- Answer: Zero, trivially.

Counterfactual:

- It was observed that a patient did not recover from the disease.
- Question: What is the probability that she would have recovered, had she been treated with the drug?
- Answer: Nontrivial. The answer is not necessarily zero, nor is it necessarily P(*recovery* | *treatment*). If we know that she was in fact treated, then we could infer that she would not have recovered if treated. But we do not know whether she was treated. The fact that she did not recover gives us partial information: it makes it less likely that she was in fact treated; it also makes it more likely that she has a weak immune system, and so on. We must make use of all of this information in trying to determine the probability that she would have recovered if treated.

We will discuss interventions in the present section, and counterfactuals in Section 4.10 below.

Suppose that we have an acyclic structural equation model with exogenous variables $\bU$ and endogenous variables $\bV$. We have equations of the form

$$X_i = f_i (\bPA(X_i), U_i),$$

and a probability distribution $\Pr'$ on the exogenous variables $\bU$. $\Pr'$ then induces a probability distribution P on $\bV$. To represent an intervention that sets $X_k$ to $x_k$, we replace the equation for $X_k$ with $X_k = x_k$. Now $\Pr'$ induces a new probability distribution P\* on $\bV$ (since settings of the exogenous variables $\bU$ give rise to different values of the variables in $\bV$ after the intervention). P\* is the new probability distribution that Pearl writes as $\Pr(• \mid \ido(X_k = x_k))$.

But even if we do not have a complete SEM, we can often compute the effect of interventions. Suppose we have a causal model in which the probability distribution P satisfies MC on the causal DAG $\bG$ over the variable set $\bV = \{X_1, X_2 ,\ldots ,X_n\}$. The most useful version of MC for thinking about interventions is MC_{Factorization} (see Section 4.2), which tells us:

$$\Pr(X_1, X_2 , \ldots ,X_n) = \prod_i \Pr(X_i \mid \bPA(X_i)).$$

Now suppose that we intervene by setting the value of $X_k$ to $x_k$. The post-intervention probability P\* is the result of altering the factorization as follows:

$$ \Pr^*(X_1, X_2 , \ldots ,X_n) = \Pr'(X_k) \times \prod_{i \ne k} \Pr(X_i \mid \bPA(X_i)), $$

where $\Pr'(X_k = x_k) = 1$. The conditional probabilities of the form $\Pr(X_i \mid \bPA(X_i))$ for $i \ne k$ remain unchanged by the intervention. This gives the same result as computing the result of an intervention using a SEM, when the latter is available. This result can be generalized to the case where the intervention imposes a probability distribution $\Pr^{\dagger}$ on some subset of the variables in $\bV$. For simplicity, let’s re-label the variables so that $\{X_1, X_2 ,\ldots ,X_k\}$ is the set of variables that we intervene on. Then, the post-intervention probability distribution is:

$$ \Pr^*(X_1, X_2 , \ldots ,X_n) = \Pr^{\dagger}( X_1, X_2 ,\ldots ,X_k) \times \prod_{k \lt i \le n} \Pr(X_i \mid \bPA(X_i)). $$

The *Manipulation Theorem* of SGS (2000: theorem 3.6) generalizes this formula to cover a much broader class of interventions, including ones that don’t break all the arrows into the variables that are intervened on.

Pearl (2009: Chapter 3) develops an axiomatic system he calls the *do-calculus* for computing post-intervention probabilities that can be applied to systems with latent variables, where the causal structure on $\bV$ is represented by an ADMG (including double-headed arrows) instead of a DAG. The axioms of this system are presented in [Supplement on the *do*-calculus](causal-models.do-calculus.md). One useful special case is given by the

*Back-Door Criterion*. Let *X* and *Y* be variables in $\bV$, and $\bZ \subseteq \bV \setminus \{X, Y\}$ such that:

1. no member of $\bZ$ is a descendant of *X*; and
2. every path between *X* and *Y* that terminates with an arrow into *X* either (a) includes a non-collider in $\bZ$, or (b) includes a collider that has no descendants in $\bZ$;

then $\Pr(Y \mid \ido(X), \bZ) = \Pr(Y \mid X, \bZ)$.

That is, if we can find an appropriate conditioning set $\bZ$, the probability resulting from an intervention on *X* will be the same as the conditional probability corresponding to an observation of *X*.

### 4.8. Interventionist Decision Theory

Evidential Decision Theory of the sort developed by Jeffrey (1983)[^jeffrey-1983], runs into well-known problems in variants of *Newcomb’s problem* (Nozick 1969)[^nozick-1969]. For example, suppose Cheryl believes the following: She periodically suffers from a potassium deficiency. This state produces two effects with high probability: It causes her to eat bananas, which she enjoys; and it causes her to suffer debilitating migraines. On days when she suffers from the potassium deficiency, she has no introspective access to this state. In particular, she is not aware of any banana cravings. Perhaps she rushes to work every morning, grabbing whatever is at hand to eat on her commute. Cheryl’s causal model is represented by the DAG in Figure 10.

![diagram with K having an arrow pointing northwest to B and northeast to M](../assets/causal-models/fig10.svg)

\*Figure 10\*

$K = 1$ represents potassium deficiency, $B = 1$ eating a banana, and $M = 1$ migraine. Her probabilities are as follows:

$$ \begin{aligned} \Pr(K = 1) & = .2\\ \Pr(B = 1 \mid K = 1) & = .9, &\Pr(B = 1 \mid K = 0) & = .1\\ \Pr(M = 1 \mid K = 1) & = .9, & \Pr(M = 1 \mid K = 0) & = .1 \end{aligned} $$

Her utility for the state of the world $w \equiv \{K = k, B = b, M = m\}$ is $\Ur(w) = b - 20m$. That is, she gains one unit of utility for eating a banana, but loses 20 units for suffering a migraine. She assigns no intrinsic value to the potassium deficiency.

Cheryl is about to leave for work. Should she eat a banana? According to *Evidential Decision Theory* (EDT), Cheryl should maximize *Evidential Expected Utility*, where

$$\EEU(B = b) = \sum_w \Pr(w \mid B = b)\Ur(w)$$

From the probabilities given, we can compute that:

$$ \begin{aligned} \Pr(M = 1 \mid B = 1) & \approx .65\\ \Pr(M = 1 \mid B = 0) & \approx .12 \end{aligned} $$

Eating a banana is strongly correlated with migraine, due to the common cause. Thus

$$\begin{aligned} \EEU(B = 1) &\approx {-12}\\ \EEU(B = 0) & \approx {-2.4} \end{aligned} $$

So EDT, at least in its simplest form, recommends abstaining from bananas. Although Cheryl enjoys them, they provide strong evidence that she will suffer from a migraine.

Many think that this is bad advice. Eating a banana does not *cause* Cheryl to get a migraine; it is a harmless pleasure. A number of authors have formulated versions of *Causal Decision Theory* (CDT) that aim to incorporate explicitly causal considerations (e.g., Gibbard & Harper 1978; Joyce 1999; Lewis 1981; Skyrms 1980)[^gibbard-1978][^joyce-1999][^lewis-1981][^skyrms-1980]. Causal models provide a natural setting for CDT, an idea proposed by Meek and Glymour (1994) and developed by Hitchcock (2016)[^hitchcock-2016], Pearl (2009: Chapter 4) and Stern (2017)[^stern-2017]. The central idea is that the agent should treat her action as an *intervention.* This means that Cheryl should maximize her *Causal Expected Utility*:

$$\CEU(B = b) = \sum_w \Pr(w \mid \ido(B = b))\Ur(w)$$

Now we can compute

$$ \begin{aligned} \Pr(M = 1 \mid \ido(B = 1)) & = .26\\ \Pr(M = 1 \mid \ido(B = 0)) & = .26 \end{aligned} $$

So that now

$$ \begin{aligned} \CEU(B = 1) &= {-4.2}\\ \CEU(B = 0) & = {-5.2} \end{aligned} $$

This yields the plausible result that eating a banana gives Cheryl a free unit of utility. By intervening, Cheryl breaks the arrow from *K* to *B* and destroys the correlation between eating a banana and suffering a migraine.

More generally, one can use the methods for calculating the effects of interventions described in the previous section to compute the probabilities needed to calculate Causal Expected Utility. Stern (2017)[^stern-2017] expands this approach to allow for agents who distribute their credence over multiple causal models. Hitchcock (2016)[^hitchcock-2016] shows how the distinction between interventions and counterfactuals, discussed in more detail in Section 4.10 below, can be used to deflect a number of alleged counterexamples to CDT.

There is much more that can be said about the debate between EDT and CDT. For instance, if Cheryl knows that she is intervening, then she will not believe herself to be accurately described by the causal structure in Figure 10. Instead, she will believe herself to instantiate a causal structure in which the arrow from *K* to *B* is removed. In this causal structure, if P satisfies MC, we will have $\Pr(w \mid B = b) = \Pr(w \mid \ido(B = b))$, and the difference between EDT and CDT collapses. If there is a principled reason why a deliberating agent will always believe herself to be intervening, then EDT will yield the same normative recommendations as CDT, and will avoid counterexamples like the one described above. Price’s defense of EDT (Price 1986)[^price-1986] might be plausibly reconstructed along these lines. So the moral is not necessarily that CDT is normatively correct, but rather that causal models may be fruitfully employed to clarify issues in decision theory connected with causation.

### 4.9 Causal Discovery with Interventions

In the previous section, we discussed how to use knowledge (or assumptions) about the structure of a causal graph $\bG$ to make inferences about the results of interventions. In this section, we explore the converse problem. If we can intervene on variables and observe the post-intervention probability distribution, what can we infer about the underlying causal structure? This topic has been explored extensively in the work of Eberhardt and his collaborators. (See, for example, Eberhardt & Scheines 2007 and Hyttinen et al. 2013a.)[^eberhardt-2007][^hyttinen-2013a] Unsurprisingly, we can learn more about causal structure if we can perform interventions than if we can only make passive observations. However, just how much we can infer depends upon what kinds of interventions we can perform, and on what background assumptions we make.

If there are no latent common causes, so that the true causal structure on $\bV$ is represented by a DAG $\bG$, then it will always be possible to discover the complete causal structure using interventions. If we can only intervene on one variable at a time, we may need to separately intervene on all but one of the variables before the causal structure is uniquely identified. If we can intervene on multiple variables at the same time, we can discover the true causal structure more quickly.

If there are latent common causes, so that the true causal structure on $\bV$ is represented by an ADMG, then it may not be possible to discover the true causal structure using only single-variable interventions. (Although we can do this in the special case where the functions in the underlying structural equation model are all linear.) However, if we can intervene on multiple variables at the same time, then it is possible to discover the true causal graph.

Eberhardt and collaborators have also explored causal discovery using *soft* interventions. A soft intervention influences the value of a variable without breaking the arrows into that variable. For instance, suppose we want to know whether increasing the income of parolees will lead to decreased recidivism. We randomly divide subjects into treatment and control conditions, and give regular cash payments to those in the treatment condition. This is not an intervention on income *per se*, since income will still be influenced by usual factors: savings and investments, job training, help from family members, and so on. Soft interventions facilitate causal inference because they create colliders, and as we have seen, colliders have a distinct probabilistic signature. Counterintuitively, this means that if we want to determine whether *X* causes *Y* it is desirable to perform a soft intervention on *Y* (rather than *X*), to see if we can create a collider $I\rightarrow Y\leftarrow X$ (where *I* is the intervention). Soft interventions are closely related to *instrumental variables.* If there are no latent common causes, we can infer the true causal structure using soft interventions. Indeed, if we can intervene on every variable at once, we can determine the correct causal structure from this one intervention. However, if there are latent common causes, it is not in general possible to discover the complete causal structure using soft interventions. (Although this can be done if we assume linearity.)

### 4.10 Counterfactuals

Section 3.3 above discussed counterfactuals in the context of deterministic causal models. The introduction of probability adds a number of complications. In particular, we can now talk meaningfully about the probability of a counterfactual being true. Counterfactuals play a central role in the *potential outcome* framework for causal models pioneered by Neyman (1923)[^neyman-1923], and developed by Rubin (1974)[^rubin-1974] and Robins (1986)[^robins-1986], among others.

Counterfactuals in the potential outcome framework interact with probability differently than counterfactuals in Lewis’s (1973b)[^lewis-1973b] framework. Suppose that Ted was exposed to asbestos and developed lung cancer. We are interested in the counterfactual: “If Ted had not been exposed to asbestos, he would not have developed lung cancer”. Suppose that the processes by which cancer develops are genuinely indeterministic. Then, it seems wrong to say that if Ted had not been exposed to asbestos, he definitely would have developed lung cancer; and it seems equally wrong to say that he definitely would not have developed lung cancer. In this case, Lewis would say that the counterfactual “If Ted had not been exposed to asbestos, he would not have developed lung cancer” is determinately *false*. As a result, the objective probability of this counterfactual being true is zero. On the other hand, a counterfactual with objective probability *in the consequent* may be true: “If Ted had not been exposed to asbestos, his objective chance of developing lung cancer would have been .06”. By contrast, in the potential outcome framework, probability may be pulled out of the consequent and applied to the counterfactual as a whole: The probability of the counterfactual “If Ted had not been exposed to asbestos, he would have developed lung cancer” can be .06.

If we have a complete structural equation model, we can assign probabilities to counterfactuals, in light of observations. Let $\bV = \{X_1, X_2 ,\ldots ,X_n\}$ be a set of endogenous variables, and $\bU = \{U_1, U_2 ,\ldots ,U_n\}$ a set of exogenous variables. Our structural equations have the form:

$$X_i = f_i (\bPA(X_i), U_i)$$

We have a probability distribution $\Pr'$ on $\bU$, which induces a probability distribution P on $\bU \cup \bV$. Suppose that we observe the value of some of the variables: $X_j = x_j$ for all $j \in \bS \subseteq \{1,\ldots ,n\}$. We now want to assess the counterfactual “if $X_k$ had been $x_k$, then $X_l$ would have been $x_l$”, where *k* and *l* may be in $\bS$ but need not be. We can evaluate the probability of this counterfactual using this three-step process:

1. Update the probability P by conditioning on the observations, to get a new probability distribution $\Pr(• \mid \cap_{j \in \bS} X_j = x_j)$. Call the restriction of this probability function to $\bU$ $\Pr''$.
2. Replace the equation for $X_k$ with $X_k = x_k$.
3. Use the distribution $\Pr''$ on $\bU$ together with the modified set of equations to induce a new probability distribution P\* on $\bV$. $\Pr^*( X_l = x_l)$ is then the probability of the counterfactual.

This procedure differs from the procedure for interventions (discussed in Section 4.7) in that steps 1 and 2 have been reversed. We first update the probability distribution, then perform the intervention. This reflects the fact that the observations tell us about the actual world, in which the intervention did not (necessarily) occur.

If we do not have a complete SEM, it is not generally possible to identify the probability of a counterfactual, but only to set upper and lower bounds. For example, suppose that we believe that asbestos exposure causes lung cancer, so that we posit a simple DAG:

$$A \rightarrow L.$$

Suppose also that we have data for people similar to Ted which yields the following probabilities:

$$\begin{aligned} \Pr(L = 1 \mid A = 1) & = .11,\\ \Pr(L = 1 \mid A = 0) & = .06. \end{aligned}$$

(We are oversimplifying, and treating asbestos and lung cancer as binary variables.) We observe that Ted was in fact exposed to asbestos and did in fact develop lung cancer. What is the probability of the counterfactual: “If Ted had not been exposed to asbestos, he would not have developed lung cancer”? Pearl (2009)[^pearl-2009] calls a probability of this form a *probability of necessity.* It is often called the *probability of causation*, although this terminology is misleading for reasons discussed by Greenland and Robins (1988). This quantity is often of interest in tort law. Suppose that Ted sues his employer for damages related to his lung cancer. He would have to persuade a jury that his exposure to asbestos caused his lung cancer. American civil law requires a “more probable than not” standard of proof, and it employs a “but for” or counterfactual definition of causation. Hence Ted must convince the jury that it is more probable than not that he would not have developed lung cancer if he had not been exposed.

We may divide the members of the population into four categories, depending upon which counterfactuals are true of them:

- *doomed* individuals will develop lung cancer no matter what
- *immune* individuals will avoid lung cancer no matter what
- *sensitive* individuals will develop lung cancer just in case they are exposed to asbestos
- *reverse sensitive* individuals will develop lung cancer just in case they are not exposed to asbestos

It is easiest to think of the population as being divided into four categories, with each person being one of these four types. However, we do not need to assume that the process is deterministic; it may be the case that each person only has a certain probability of falling into one of these categories.

Mathematically, this is equivalent to the following. Let $U_L$ be the error variable for $L. U_L$ takes values of the form $(u_1, u_2)$ with each $u_i$ being 0 or 1. $(1, 1)$ corresponds to *doomed*, $(0, 0)$ to *immune*, $(1, 0)$ to *sensitive*, and $(0, 1)$ to *reverse*. That is, the first element tells us what value *L* will take if an individual is exposed to asbestos, and the second element what value *L* will take if an individual is not exposed. The equation for *L* will be $L = (A \times u_1) + ((1 - A) \times u_2)$.

Let us assume that the distribution of the error variable $U_L$ is independent of asbestos exposure *A*. The observed probability of lung cancer is compatible with both of the following probability distributions over our four counterfactual categories:

$$ \begin{aligned} \Pr_1(\textit{doomed}) & = .06, &\Pr_2(\textit{doomed}) &= 0,\\ \Pr_1(\textit{immune}) & = .89, & \Pr_2(\textit{immune}) & = .83,\\ \Pr_1(\textit{sensitive}) & = .05, & \Pr_2(\textit{sensitive}) & = .11, \\ \Pr_1(\textit{reverse}) & = 0 & \Pr_2(\textit{reverse}) & = .06 \end{aligned} $$

More generally, the observed probability is compatible with any probability $\Pr'$ satisfying:

$$ \begin{aligned} \Pr'(\textit{doomed}) + \Pr'(\textit{senstive}) & = \Pr(L \mid A) & = .11;\\ \Pr'(\textit{immune}) + \Pr'(\textit{reverse}) & = \Pr({\sim}L \mid A) & = .89;\\ \Pr'(\textit{doomed}) + \Pr'(\textit{reverse}) & = \Pr(L \mid {\sim}A) & = .06;\\ \Pr'(\textit{immune}) + \Pr'(\textit{senstive}) & = \Pr({\sim}L \mid {\sim}A) & = .94.\\ \end{aligned} $$

$\Pr_1$ and $\Pr_2$ are just the most extreme cases. From the fact that Ted was exposed to asbestos and developed lung cancer, we know that he is either *sensitive* or *doomed*. The counterfactual of interest will be true just in case he is *sensitive*. Hence the probability of the counterfactual, given the available evidence, is P(*sensitive* | *sensitive* or *doomed*). However, using $\Pr_1$ yields a conditional probability of .45 (5/11), while $\Pr_2$ yields a conditional probability of 1. Given the information available to us, all we can conclude is that the probability of necessity is between .45 and 1. To determine the probability more precisely, we would need to know the probability distribution of the error variable.

A closely related counterfactual quantity is what Pearl (2009)[^pearl-2009] calls the *probability of sufficiency.* Suppose that Teresa, unlike Ted, was not exposed to asbestos, and did not develop lung cancer. The probability of sufficiency is the probability that she *would* have suffered lung cancer if she *had been* exposed. That is, the probability of sufficiency is the probability that if the cause were added to a situation in which it and the effect was absent, it would have resulted in the effect occurring. The probability of sufficiency is closely related to the quantity that Sheps (1958)[^sheps-1958] called the *relative difference*, and that Cheng (1997)[^cheng-1997] calls the *causal power.* Cheng’s terminology reflects the idea that the probability of sufficiency of *C* for *E* is the power of *C* to bring about *E* in cases where *E* is absent. As in the case of the probability of necessity, if one does not have a complete structural equation model, but only a Causal Bayes Net or Semi-Markov Causal Model, it is usually only possible to put upper and lower bounds on the probability of sufficiency. Using the probabilities from the previous example, the probability of sufficiency of asbestos for lung cancer would be between .05 (5/94) and .12 (11/94).

Determining the probabilities of counterfactuals, even just upper and lower bounds, is computationally demanding. Balke and Pearl’s twin network method (Balke and Pearl (1994a), (1994b); Pearl (2009, pp. 213 - 215)) and Richardson and Robins’ split-node method (Richardson and Robins (2016)) are two methods that have been proposed for solving this kind of problem.

## 5. Further Reading

The most important works surveyed in this entry are Pearl 2009 and Spirtes, Glymour, & Scheines 2000. Pearl 2010, Pearl et al. 2016, and Pearl & Mackenzie 2018 are three overviews of Pearl’s program. Pearl 2010 is the shortest, but the most technical. Pearl & Mackenzie 2018 is the least technical. Scheines 1997 and the “Introduction” of Glymour & Cooper 1999 are accessible introductions to the SGS program. Eberhardt 2009, Hausman 1999, Glymour 2009, and Hitchcock 2009 are short overviews that cover some of the topics raised in this entry.

The entry on causation and manipulability contains extensive discussion of interventions, and some discussion of causal models.

Halpern (2016)[^halpern-2016] engages with many of the topics in Section 3. See also the entry for counterfactual theories of causation.

The entry on probabilistic causation contains some overlap with the present entry. Some of the material from Section 4 of this entry is also presented in Section 3 of that entry. That entry contains in addition some discussion of the connection between probabilistic causal models and earlier probabilistic theories of causation.

Eberhardt 2017 is a short survey that provides a clear introduction to many of the topics covered in Sections 4.2 through 4.6, as well as Section 4.9. Spirtes and Zhang 2016 is a longer and more technical overview that covers much of the same ground. It has particularly good coverage on the issues raised in Section 4.5.

The entries on decision theory and causal decision theory present more detailed background information about some of the issues raised in Section 4.8.

This entry has focused on topics that are likely to be of most interest to philosophers. There are a number of important technical issues that have been largely ignored. Many of these address problems that arise when various simplifying assumptions made here (such as acyclicity, and knowledge of the true probabilities) are rejected. Some of these issues are briefly surveyed along with references in [Supplement on Further Topics in Causal Inference](causal-models.topics.md).

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=causal-models). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/causal-models/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=causal-models&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](http://philpapers.org/sep/causal-models/) at [PhilPapers](http://philpapers.org/), with links to its database. |

## Other Internet Resources

- [Causal Analysis and Theory in Practice](http://causality.cs.ucla.edu/blog/)
- [*Causality*, 2nd Edition, 2009](http://bayes.cs.ucla.edu/BOOK-2K/), Judea Pearl's web page on his book.
- [The Tetrad Project](http://www.phil.cmu.edu/tetrad/).
- [Causal and Statistical Reasoning](http://www.phil.cmu.edu/projects/csr/), The Carnegie Mellon Curriculum, Core Site Materials.

## Related Entries

causation: and manipulability | causation: counterfactual theories of | causation: probabilistic | causation: the metaphysics of | conditionals: counterfactual | decision theory | decision theory: causal | logic: conditionals | probability, interpretations of | quantum theory: the Einstein-Podolsky-Rosen argument in | rational choice, normative: expected utility | Reichenbach, Hans: common cause principle

### Acknowledgments

Thanks to Frederick Eberhardt, Clark Glymour, Joseph Halpern, Judea Pearl, Peter Spirtes, Reuben Stern, Jiji Zhang, and Kun Zhang for detailed comments, corrections, and discussion.

Portions of this entry are taken, with minimal adaptation, from the author’s separate entry on probabilistic causation so that readers do not need to consult that entry for background material before reading this entry.

[^balke-1994a]: Balke, Alexander and Judea Pearl, 1994a, “Probabilistic Evaluation of Counterfactual Queries”, in Barbara Hayes-Roth and Richard E Korf (eds.), *Proceedings of the Twelfth National Conference on Artificial Intelligence*, Volume I, Menlo Park CA: AAAI Press, pp. 230–237. [[Balke & Pearl 1994a available online](https://www.aaai.org/Papers/AAAI/1994/AAAI94-035.pdf)]

[^balke-1994b]: –––, 1994b, “Counterfactual Probabilities: Computational Methods, Bounds, and Applications”, in Ramon Lopez de Mantaras and David Poole (eds.), *Proceedings of the Tenth Conference on Uncertainty in Artificial Intelligence*, San Francisco: Morgan Kaufmann, pp. 46–54. [[Balke & Pearl 1994b available online](https://arxiv.org/abs/1302.6784)]

[^bareinboim-2013]: Bareinboim, Elias, and Judea Pearl, 2013, “A General Algorithm for Deciding Transportability of Experimental Results”, *Journal of Causal Inference*, 1(1): 107–134. doi:10.1515/jci-2012-0004

[^bareinboim-2014]: –––, 2014, “Transportability from Multiple Environments with Limited Experiments: Completeness Results”, in Zoubin Ghahramani, Max Welling, Corinna Cortes, and Neil Lawrence and Kilian Weinberger (eds.), *Advances of Neural Information Processing 27 (NIPS Proceedings)*, 280–288. [[Bareinboim & Pearl 2014 available online](http://papers.nips.cc/paper/5536-transportability-from-multiple-environments-with-limited-experiments-completeness-results.pdf)]

[^bareinboim-2015]: –––, 2015, “Causal Inference and the Data-Fusion Problem”, *Proceedings of the National Academy of Sciences*, 113(27): 7345–7352. doi:10.1073/pnas.1510507113

[^beckers-2018]: Beckers, Sander and Joost Vennekens, 2018, “A Principled Approach to Defining Actual Causation”, *Synthese*, 195(2): 835–862. doi:10.1007/s11229-016-1247-1

[^beebee-2009]: Beebee, Helen, Christopher Hitchcock, and Peter Menzies (eds.), 2009, *The Oxford Handbook of Causation*, Oxford: Oxford University Press.

[^blanchard-2017]: Blanchard, Thomas, and Jonathan Schaffer, 2017,“Cause without Default”, in Helen Beebee, Christopher Hitchcock, and Huw Price (eds.). *Making a Difference*, Oxford: Oxford University Press, pp. 175–214.

[^briggs-2012]: Briggs, Rachael, 2012, “Interventionist Counterfactuals”, *Philosophical Studies*160(1): 139–166. doi:10.1007/s11098-012-9908-5

[^cartwright-1993]: Cartwright, Nancy, 1993, “Marks and Probabilities: Two Ways to Find Causal Structure”, in Fritz Stadler (ed.), *Scientific Philosophy: Origins and Development*, Dordrecht: Kluwer, 113–119. doi:10.1007/978-94-017-2964-2_7

[^cartwright-2007]: –––, 2007, *Hunting Causes and Using Them*, Cambridge: Cambridge University Press. doi:10.1017/CBO9780511618758

[^chalupka-2017]: Chalupka, Krzysztof, Frederick Eberhardt, and Pietro Perona, 2017, “Causal Feature Learning: an Overview”, *Behaviormetrika*, 44(1): 137–167. doi:10.1007/s41237-016-0008-2

[^cheng-1997]: Cheng, Patricia, 1997, “From Covariation to Causation: A Causal Power Theory”, *Psychological Review*, 104(2): 367– 405. doi:10.1037/0033-295X.104.2.367

[^claassen-2012]: Claassen, Tom and Tom Heskes, 2012, “A Bayesian Approach to Constraint Based Causal Inference”, in Nando de Freitas and Kevin Murphy (eds.) *Proceedings of the Twenty-Eighth Conference on Uncertainty in Artificial Intelligence*, Corvallis, OR: AUAI Press, pp. 207–216. [[Claassen & Heskes 2012 available online](http://arxiv.org/abs/1210.4866)]

[^cooper-1992]: Cooper, G. F. and Herskovits, E. 1992, “A Bayesian Method for the Induction of Probabilistic Networks from Data”, *Machine Learning*, 9(4): 309–347. doi:10.1007/BF00994110

[^danks-2014]: Danks, David, and Sergey Plis, 2014, “Learning Causal Structure from Undersampled Time Series”, *JMLR Workshop and Conference Proceedings (NIPS Workshop on Causality)*. [[Danks & Plis 2014 available online](https://doi.org/10.1184/R1/6492101.v1)]

[^dash-2001]: Dash, Denver and Marek Druzdzel, 2001, “Caveats For Causal Reasoning With Equilibrium Models”, in Salem Benferhat and Philippe Besnard (eds.) *Symbolic and Quantitative Approaches to Reasoning with Uncertainty, 6th European Conference, Proceedings. Lecture Notes in Computer Science 2143*, Berlin and Heidelberg: Springer, pp. 92–103. doi:10.1007/3-540-44652-4\\_18

[^dechter-2006]: Dechter, Rina and Thomas Richardson (eds.), 2006, *Proceedings of the Twenty-Second Conference on Uncertainty in Artificial Intelligence*, Corvallis, OR: AUAI Press.

[^dowe-2000]: Dowe, Phil, 2000, *Physical Causation*, Cambridge: University of Cambridge Press. doi:10.1017/CBO9780511570650

[^eberhardt-2009]: Eberhardt, Frederick, 2009, “Introduction to the Epistemology of Causation”, *Philosophy Compass*, 4(6): 913–925. doi:10.1111/j.1747-9991.2009.00243.x

[^eberhardt-2017]: –––, 2017, “Introduction to the Foundations of Causal Discovery”, *International Journal of Data Science and Analytics*, 3(2): 81–91. doi:10.1007/s41060-016-0038-6

[^eberhardt-2007]: Eberhardt, Frederick and Richard Scheines, 2007, “Interventions and Causal Inference”, *Philosophy of Science*, 74(5): 981–995. doi:10.1086/525638

[^eells-1991]: Eells, Ellery, 1991, *Probabilistic Causality*, Cambridge: Cambridge University Press. doi:10.1017/CBO9780511570667

[^eichler-2012]: Eichler, Michael, 2012, “Causal Inference in Time Series Analysis”, in Carlo Berzuini, Philip Dawid, and Luisa Bernardinelli (eds.), *Causality: Statistical Perspectives and Applications*, Chichester, UK: Wiley, pp. 327–354. doi:10.1002/9781119945710.ch22

[^fine-2012]: Fine, Kit, 2012, “Counterfactuals without Possible Worlds”, *Journal of Philosophy*, 109(3): 221–246. doi:10.5840/jphil201210938

[^galles-1998]: Galles, David, and Judea Pearl, 1998, “An Axiomatic Characterization of Causal Counterfactuals”, *Foundations of Science*, 3(1): 151–182. doi:10.1023/A:1009602825894

[^geiger-1994]: Geiger, Dan and David Heckerman, 1994, “Learning Gaussian Networks”, Technical Report MSR-TR-94-10, Microsoft Research.

[^geiger-1988]: Geiger, Dan and Judea Pearl, 1988, “On the Logic of Causal Models”, in Ross Shachter, Tod Levitt, Laveen Kanal, and John Lemmer (eds.), *Proceedings of the Fourth Conference on Uncertainty in Artificial Intelligence*, Corvallis, OR: AUAI Press, pp. 136–147.

[^gibbard-1978]: Gibbard, Alan, and William Harper, 1978, “Counterfactuals and Two Kinds of Expected Utility”, in Clifford Hooker, James Leach, and Edward McClennen (eds.), *Foundations and Applications of Decision Theory*, Dordrecht: Reidel, pp. 125–62.

[^glennan-2017]: Glennan, Stuart, 2017, *The New Mechanical Philosophy*, Oxford: Oxford University Press.

[^glymour-2009]: Glymour, Clark, 2009, “Causality and Statistics”, in Beebee, Hitchcock, and Menzies 2009: 498–522.

[^glymour-1999]: Glymour, Clark and Gregory Cooper, 1999, *Computation, Causation, and Discovery*, Cambridge, MA: MIT Press.

[^glymour-2010]: Glymour, Clark, David Danks, Bruce Glymour, Frederick Eberhardt, Joseph Ramsey, Richard Scheines, Peter Spirtes, Choh Man Teng, and Jiji Zhang, 2010, “Actual Causation: a Stone Soup Essay”, *Synthese*, 175(2): 169–192. doi:10.1007/s11229-009-9497-9

[^glymour-2007]: Glymour, Clark and Frank Wimberly, 2007, “Actual Causes and Thought Experiments”, in Joseph Campbell, Michael O’Rourke, and Harry Silverstein (eds.), *Causation and Explanation*, Cambridge, MA: MIT Press, pp. 43–68.

[^gong-2015]: Gong, Mingming, Kun Zhang, Bernhard Schölkopf, Dacheng Tao, and Philipp Geiger, 2015, “Discovering Temporal Causal Relations from Subsampled Data”, in Francis Bach and David Blei (eds.), *Proceeding of the 32ⁿᵈ International Conference on Machine Learning*, 37: 1898–1906. [[Gong et al. 2015 available online](http://proceedings.mlr.press/v37/gongb15.html)]

[^gong-2017]: Gong, Mingming, Kun Zhang, Bernhard Schölkopf, Clark Glymour, and Dacheng Tao, 2017, “Causal Discovery from Temporally Aggregated Time Series”, in Gal Elidan and Kristian Kersting (eds.), *Proceedings of the Thirty-Third Conference on Uncertainty in Artificial Intelligence*, Corvallis, OR: AUAI Press. [[Gong et al. 2017 available online](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5995575/)]

[^greenland-1988]: Greenland, Sander, and James Robins, 1988, “Conceptual Problems in the Definition and Interpretation of Attributable Fractions”, *American Journal of Epidemiology*, 128(6): 1185–1197. doi:10.1093/oxfordjournals.aje.a115073

[^hall-2007]: Hall, Ned, 2007, “Structural Equations and Causation”, *Philosophical Studies*, 132(1): 109–136. doi:10.1007/s11098-006-9057-9

[^halpern-2000]: Halpern, Joseph Y., 2000, “Axiomatizing Causal Reasoning”, *Journal of Artificial Intelligence Research*, 12: 317–337. [[Halpern 2000 available online](https://www.jair.org/index.php/jair/article/view/10257)]

[^halpern-2008]: –––, 2008, “Defaults and Normality in Causal Structures”, in Gerhard Brewka and Jérôme Lang (eds.), *Principles of Knowledge Representation and Reasoning: Proceedings of the Eleventh International Conference*, Menlo Park, CA: AAAI Press, pp. 198–208.

[^halpern-2016]: –––, 2016, *Actual Causality*, Cambridge, MA: MIT Press.

[^halpern-2015]: Halpern, Joseph Y. and Christopher Hitchcock, 2015, “Graded Causation and Defaults”, *British Journal for Philosophy of Science*, 66(2): 413–57. doi:10.1093/bjps/axt050

[^halpern-2001]: Halpern, Joseph and Judea Pearl, 2001, “Causes and Explanations: A Structural-Model Approach. Part I: Causes”, in John Breese and Daphne Koller (eds.), *Proceedings of the Seventeenth Conference on Uncertainty in Artificial Intelligence*, San Francisco: Morgan Kaufmann, pp. 194–202

[^halpern-2005]: –––, 2005, “Causes and Explanations: A Structural-Model Approach. Part I: Causes”, *British Journal for the Philosophy of Science*, 56(4): 843–887. doi:10.1093/bjps/axi147

[^hausman-1999]: Hausman, Daniel M., 1999, “The Mathematical Theory of Causation”, *British Journal for the Philosophy of Science*, 50(1): 151–162. doi:10.1093/bjps/50.1.151

[^hausman-1999-2]: Hausman, Daniel M. and James Woodward, 1999, “Independence, Invariance, and the Causal Markov Condition”, *British Journal for the Philosophy of Science*, 50(4): 521–583. doi:10.1093/bjps/50.4.521

[^hausman-2004]: –––, 2004, “Modularity and the Causal Markov Condition: a Restatement”, *British Journal for the Philosophy of Science*, 55(1): 147–161. doi:10.1093/bjps/55.1.147

[^hitchcock-2001]: Hitchcock, Christopher, 2001, “The Intransitivity of Causation Revealed in Equations and Graphs”, *Journal of Philosophy*, 98(6): 273–299. doi:10.2307/2678432

[^hitchcock-2007]: –––, 2007, “Prevention, Preemption, and the Principle of Sufficient Reason”, *Philosophical Review*, 116(4): 495–532. doi:10.1215/00318108-2007-012

[^hitchcock-2009]: –––, 2009, “Causal Models”, in Beebee, Hitchcock, and Menzies 2009: 299–314.

[^hitchcock-2016]: –––, 2016, “Conditioning, Intervening, and Decision”, *Synthese*, 193(4): 1157–1176. doi:10.1007/s11229-015-0710-8

[^hoyer-2009]: Hoyer, Patrik O., Dominik Janzing, Joris Mooij, Jonas Peters, and Bernhard Schölkopf, 2009, “Nonlinear Causal Discovery with Additive Noise Models”, *Advances in Neural Information Processing Systems*, 21: 689–696. [[Hoyer et al. 2009 available online](https://papers.nips.cc/paper/3548-nonlinear-causal-discovery-with-additive-noise-models)]

[^huang-2006]: Huang, Yimin and Marco Valtorta, 2006, “Pearl’s Calculus of Intervention Is Complete”, in Dechter and Richardson 2006: 217–224. [[Huang & Valtorta 2006 available online](http://arxiv.org/abs/1206.6831)]

[^hyttinen-2013a]: Hyttinen, Antti, Frederick Eberhardt, and Patrik O. Hoyer, 2013a, “Experiment Selection for Causal Discovery”, *Journal of Machine Learning Research*, 14: 3041–3071. [[Hyttinen, Eberhardt, & Hoyer 2013a available online](http://www.jmlr.org/papers/v14/hyttinen13a.html)]

[^hyttinen-2014]: Hyttinen, Antti, Frederick Eberhardt, and Matti Järvisalo, 2014, “Constraint-based Causal Discovery: Conflict Resolution with Answer Set Programming”, in Nevin Zhang and Jin Tian (eds.), *Proceedings of the Thirtieth Conference on Uncertainty in Artificial Intelligence*, Corvallis, OR: AUAI Press, pp. 340–349.

[^hyttinen-2015]: –––, 2015, “Do-calculus When the True Graph is Unknown”, in Marina Meila and Tom Heskes (eds.), *Uncertainty in Artificial Intelligence: Proceedings of the Thirty-First Conference*, Corvallis, OR: AUAI Press, pp. 395–404.

[^hyttinen-2013b]: Hyttinen, Antti, Patrik O. Hoyer, Frederick Eberhardt, and Matti Järvisalo, 2013b, “Discovering Cyclic Causal Models with Latent Variables: A General SAT-Based Procedure”, in Nichols and Smyth 2013: 301–310.

[^hyttinen-2016]: Hyttinen, Antti, Sergey Plis, Matti Järvisalo, Frederick Eberhardt, and David Danks, 2016, “Causal Discovery from Subsampled Time Series Data by Constraint Optimization”, in Alessandro Antonucci, Giorgio Corani, Cassio Polpo Campos (eds.) *Proceedings of the Eighth International Conference on Probabilistic Graphical Models*, pp. 216–227.

[^jeffrey-1983]: Jeffrey, Richard, 1983, *The Logic of Decision*, Second Edition, Chicago: University of Chicago Press.

[^joyce-1999]: Joyce, James M., 1999, *The Foundations of Causal Decision Theory*, Cambridge: Cambridge University Press. doi:10.1017/CBO9780511498497

[^lewis-1973a]: Lewis, David, 1973a, “Causation”, *Journal of Philosophy*, 70(17): 556–567. doi:10.2307/2025310

[^lewis-1973b]: –––, 1973b, *Counterfactuals*, Oxford: Blackwell.

[^lewis-1979]: –––, 1979, “Counterfactual Dependence and Time’s Arrow”, *Noûs*, 13(4): 455–476. doi:10.2307/2215339

[^lewis-1981]: –––, 1981, “Causal Decision Theory”, *Australasian Journal of Philosophy*, 59(1): 5–30. doi:10.1080/00048408112340011

[^machamer-2000]: Machamer, Peter, Lindley Darden, and Carl Craver, 2000, “Thinking about Mechanisms”, *Philosophy of Science*, 67(1): 1–25. doi:10.1086/392759

[^maier-2013]: Maier, Marc, Katerina Marazopoulou, David Arbour, and David Jensen, 2013, “A Sound and Complete Algorithm for Learning Causal Models from Relational Data”, in Nichols and Smyth 2013: 371–380. [[Maier et al. 2013 available online](http://arxiv.org/abs/1309.6843)]

[^maier-2010]: Maier, Marc, Brian Taylor, Hüseyin Oktay, and David Jensen, 2010, “Learning Causal Models of Relational Domains”, in Maria Fox and David Poole (eds.), *Proceedings of the Twenty-Fourth AAAI Conference on Artificial Intelligence*, (Menlo Park CA: AAAI Press), pp. 531–538. [[Maier et al. 2010 available online](https://www.aaai.org/ocs/index.php/AAAI/AAAI10/paper/view/1919)]

[^meek-1995]: Meek, Christopher, 1995, “Strong Completeness and Faithfulness in Bayesian Networks”, in Philippe Besnard and Steve Hanks (eds.) *Proceedings of the Eleventh Conference Conference on Uncertainty in Artificial Intelligence*, San Francisco: Morgan Kaufmann, pp. 411–418.

[^meek-1994]: Meek, Christopher and Clark Glymour, 1994, “Conditioning and Intervening”, *British Journal for Philosophy of Science,*, 45(4): 1001–1024. doi:10.1093/bjps/45.4.1001

[^menzies-2004]: Menzies, Peter, 2004, “Causal Models, Token Causation, and Processes”, *Philosophy of Science*, 71(5): 820–832. doi:10.1086/425057

[^mooij-2013]: Mooij, Joris, Dominik Janzing, and Bernhard Schölkopf, 2013, “From Ordinary Differential Equations to Structural Causal Models: the Deterministic Case”, in Nichols and Smyth 2013: 440–448.

[^neal-2000]: Neal, Radford M., 2000, “On Deducing Conditional Independence from d-separation in Causal Graphs with Feedback”, *Journal of Artificial Intelligence Research*, 12: 87–91. [[Neal 2000 available online](https://www.jair.org/index.php/jair/article/view/10250)]

[^neapolitan-2004]: Neapolitan, Richard, 2004, *Learning Bayesian Networks*, Upper Saddle River, NJ: Prentice Hall.

[^neapolitan-2016]: Neapolitan, Richard and Xia Jiang, 2016, “The Bayesian Network Story”, in Alan Hájek and Christopher Hitchcock (eds.), *The Oxford Handbook of Probability and Philosophy*, Oxford: Oxford University Press, pp. 183–99.

[^neyman-1923]: Neyman, Jerzy, 1923 [1990], “Sur les Applications de la Théorie des Probabilités aux Experiences Agricoles: Essai des Principes”) *Roczniki Nauk Rolniczych, Tom*, X: 1–51. Excerpts translated into English by D. M. Dabrowska and Terrence Speed, 1990, “On the Application of Probability Theory to Agricultural Experiments. Essay on Principles”, *Statistical Science*, 5(4): 465–80. doi:10.1214/ss/1177012031

[^ann-2013]: Ann Nichols and Padhraic Smyth (eds), 2013, *Proceedings of the Twenty-Ninth Conference on Uncertainty in Artificial Intelligence*, Corvallis, OR: AUAI Press.

[^nozick-1969]: Nozick, Robert, 1969, “Newcomb’s Problem and Two Principles of Choice”, in Nicholas Rescher (ed.), *Essays in Honor of Carl G. Hempel*, Dordrecht: Reidel, pp. 114–146. doi:10.1007/978-94-017-1466-2_7

[^pearl-1988]: Pearl, Judea, 1988, *Probabilistic Reasoning in Intelligent Systems*, San Francisco: Morgan Kaufmann.

[^pearl-1995]: –––, 1995, “Causal Diagrams for Empirical Research”, *Biometrika*, 82(4): 669–688. doi:10.1093/biomet/82.4.669

[^pearl-2009]: –––, 2009, *Causality: Models, Reasoning, and Inference*, Second Edition, Cambridge: Cambridge University Press.

[^pearl-2010]: –––, 2010, “An Introduction to Causal Inference”, *The International Journal of Biostatistics*, 6(2): article 7, pp. 1–59. doi:10.2202/1557-4679.1203

[^pearl-1996]: Pearl, Judea and Rina Dechter, 1996, “Identifying Independencies in Causal Graphs with Feedback”, in Eric Horvitz and Finn Jensen (eds.) *Proceedings of the Twelfth Conference on Uncertainty in Artificial Intelligence*, San Francisco: Morgan Kaufmann, pages 420–426.

[^pearl-2016]: Pearl, Judea, Madelyn Glymour, and Nicholas P. Jewell, 2016, *Causal Inference in Statistics: A Primer*, Chichester, UK: Wiley.

[^pearl-2018]: Pearl, Judea and Mackenzie, Dana, 2018, *The Book of Why: The New Science of Cause and Effect.*, New York: Basic Books.

[^pearl-1991]: Pearl, Judea and Verma, Thomas, 1991, “A Theory of Inferred Causation”, in James Allen, Richard Fiskes, and Erik Sandewall (eds.), *Principles of Knowledge Representation and Reasoning: Proceedings of the Second International Conference*, San Mateo, CA: Morgan Kaufmann, pp. 441–52.

[^peters-2017]: Peters, Jonas, Dominik Janzing, and Bernhard Schölkopf, 2017, *Elements of Causal Inference: Foundations and Learning Algorithms.*, Cambridge, MA: MIT Press.

[^price-1986]: Price, Huw, 1986, “Against Causal Decision Theory”, *Synthese*, 67(2): 195–212. doi:10.1007/BF00540068

[^ramsey-2006]: Ramsey, Joseph, Peter Spirtes, and Jiji Zhang, 2006, “Adjacency Faithfulness and Conservative Causal Inference”, in Dechter and Richardson 2006: 401–408. [[Ramsey, Spirtes, & Zhang 2006 available online](http://arxiv.org/abs/1206.6843)]

[^reichenbach-1956]: Reichenbach, Hans, 1956, *The Direction of Time*, Berkeley and Los Angeles: University of California Press.

[^richardson-2016]: Richardson, Thomas, and James Robins, 2016, *Single World Intervention Graphs (SWIGs): A Unification of the Counterfactual and Graphical Approaches to Causality*, Hanover, MA: Now Publishers.

[^robins-1986]: Robins, James, 1986, “A New Approach to Causal Inference in Mortality Studies with a Sustained Exposure Period: Applications to Control of the Healthy Workers Survivor Effect”, *Mathematical Modeling*, 7(9–12): 1393–1512. doi:10.1016/0270-0255(86)90088-6

[^rubin-1974]: Rubin, Donald, 1974, “Estimating Causal Effects of Treatments in Randomized and Nonrandomized Studies”, *Journal of Educational Psychology*, 66(5): 688–701. doi:10.1037/h0037350

[^salmon-1984]: Salmon, Wesley, 1984, *Scientific Explanation and the Causal Structure of the World*, Princeton: Princeton University Press.

[^scheines-1997]: Scheines, Richard, 1997, “An Introduction to Causal Inference” in V. McKim and S. Turner (eds.), *Causality in Crisis?*, Notre Dame: University of Notre Dame Press, pp. 185–199.

[^schulte-2012]: Schulte, Oliver and Hassan Khosravi, 2012, “Learning Graphical Models for Relational Data via Lattice Search”, *Machine Learning*, 88(3): 331–368. doi:10.1007/s10994-012-5289-4

[^schulte-2010]: Schulte, Oliver, Wei Luo, and Russell Greiner, 2010, “Mind Change Optimal Learning of Bayes Net Structure from Dependency and Independency Data”, *Information and Computation*, 208(1): 63–82. doi:10.1016/j.ic.2009.03.009

[^shalizi-2011]: Shalizi, Cosma Rohilla, and Andrew C. Thomas, 2011, “Homophily and Contagion are Generically Confounded in Observational Social Studies”, *Sociological Methods and Research*, 40(2): 211–239. doi:10.1177/0049124111404820

[^sheps-1958]: Sheps, Mindel C., 1958, “Shall We Count the Living or the Dead?” *New England Journal of Medicine*, 259(12): 210–4. doi:10.1056/NEJM195812182592505

[^shimizu-2006]: Shimizu, Shohei, Patrik O. Hoyer, Aapo Hyvärinen, and Antti Kermine, 2006, “A Linear Non-Gaussian Acyclic Model for Causal Discovery”, *Journal of Machine Learning Research*, 7: 2003–2030. [[Shimizu et al. 2006 available online](http://www.jmlr.org/papers/v7/shimizu06a.html)]

[^shpitser-2006]: Shpitser, Ilya and Judea Pearl, 2006, “Identification of Conditional Interventional Distributions”, in Dechter and Richardson 2006: 437–444. [[Shpister & Pearl 2006 available online](http://arxiv.org/abs/1206.6876)]

[^skyrms-1980]: Skyrms, Brian, 1980, *Causal Necessity*, New Haven and London: Yale University Press.

[^spirtes-1995]: Spirtes, Peter, 1995, “Directed Cyclic Graphical Representation of Feedback Models”, in Philippe Besnard and Steve Hanks (eds.), *Proceedings of the Eleventh Conference on Uncertainty in Artificial Intelligence*, San Francisco: Morgan Kaufmann, pp. 491–498.

[^spirtes-2000]: Spirtes, Peter, Clark Glymour, and Richard Scheines, [SGS] 2000, *Causation, Prediction and Search*, Second Edition, Cambridge, MA: MIT Press.

[^spirtes-2014]: Spirtes, Peter and Jiji Zhang, 2014, “A Uniformly Consistent Estimator of Causal Effects under the *k*-Triangle-Faithfulness Assumption”, *Statistical Science*, 29(4): 662–678. doi:10.1214/13-STS429

[^spirtes-2016]: Spirtes, Peter and Kun Zhang, 2016, “Causal Discovery and Inference: Concepts and Recent Methodological Advances”, *Applied Informatics*, 3: 3. doi:10.1186/s40535-016-0018-x

[^stalnaker-1968]: Stalnaker, Robert, 1968, “A Theory of Conditionals”, in Nicholas Rescher (ed.) *Studies in Logical Theory*, Blackwell: Oxford, pp. 98–112.

[^steel-2006]: Steel, Daniel, 2006, “Homogeneity, Selection, and the Faithfulness Condition”. *Minds and Machines*, 16(3): 303–317. doi:10.1007/s11023-006-9032-4

[^stern-2017]: Stern, Reuben, 2017, “Interventionist Decision Theory”, *Synthese*, 194(10): 4133–4153. doi:10.1007/s11229-016-1133-x

[^suppes-1970]: Suppes, Patrick, 1970, *A Probabilistic Theory of Causality*, Amsterdam: North-Holland Publishing Company.

[^tillman-2014]: Tillman, Robert E., and Frederick Eberhardt, 2014, “Learning Causal Structure from Multiple Datasets with Similar Variable Sets”, *Behaviormetrika*, 41(1): 41–64. doi:10.2333/bhmk.41.41

[^triantafillou-2015]: Triantafillou, Sofia, and Ioannis Tsamardinos, 2015, “Constraint-based Causal Discovery from Multiple Interventions over Overlapping Variable Sets”, *Journal of Machine Learning Research*, 16: 2147–2205. [[Triantafillou & Tsamardinos 2015 available online](http://www.jmlr.org/papers/v16/triantafillou15a.html)]

[^weslake-nd]: Weslake, Brad, forthcoming, “A Partial Theory of Actual Causation”, *British Journal for the Philosophy of Science.*

[^woodward-2003]: Woodward, James, 2003, *Making Things Happen: A Theory of Causal Explanation*, Oxford: Oxford University Press. doi:10.1093/0195155270.001.0001

[^wright-1921]: Wright, Sewall, 1921, “Correlation and Causation”, *Journal of Agricultural Research*, 20: 557–85.

[^zhalama-2016]: Zhalama, Jiji Zhang, and Wolfgang Mayer, 2016, “Weakening Faithfulness: Some Heuristic Causal Discovery Algorithms”, *International Journal of Data Science and Analytics*, 3(2): 93–104. doi:10.1007/s41060-016-0033-y

[^zhang-2008]: Zhang, Jiji, 2008, “Causal Reasoning with Ancestral Graphs”, *Journal of Machine Learning Research*, 9: 1437–1474. [[Zhang 2008 available online](http://www.jmlr.org/papers/v9/zhang08a.html)]

[^zhang-2013a]: –––, 2013a, “A Lewisian Logic of Counterfactuals”, *Minds and Machines*, 23(1): 77–93. doi:10.1007/s11023-011-9261-z

[^zhang-2013b]: –––, 2013b, “A Comparison of Three Occam’s Razors for Markovian Causal Models”, *British Journal for Philosophy of Science*, 64(2): 423–448. doi:10.1093/bjps/axs005

[^zhang-2008-2]: Zhang, Jiji and Peter Spirtes 2008, “Detection of Unfaithfulness and Robust Causal Inference”, *Minds and Machines*, 18(2): 239–271. doi:10.1007/s11023-008-9096-4

[^zhang-2016]: –––, 2016, “The Three Faces of Faithfulness”, *Synthese*, 193(4): 1011–1027. doi:10.1007/s11229-015-0673-9

[^zhang-2009]: Zhang, Kun, and Aapo Hyvärinen, 2009, “On the Identifiability of the Post-nonlinear Causal Model”, in Jeff Bilmes and Andrew Ng (eds.), *Proceeding of the Twenty-Fifth Conference on Uncertainty in Artificial Intelligence*, (Corvallis, OR: AUAI Press), pp. 647–655.
