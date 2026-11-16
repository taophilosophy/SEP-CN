# Inductive Logic
**First published Mon Sep 6, 2004; substantive revision Mon Feb 24, 2025**

*Hawthorne, James*

An inductive logic is a system of reasoning that articulates how evidence claims bear on the truth of hypotheses. As with any logic, it does this via the evaluation of arguments. Each argument consists of premise statements and a conclusion statement. A logic employs principles and rules to evaluate the extent to which the truth of an argument’s premise statements support the truth of its conclusion statement.

In a deductive logic the truth of the premises of a *good* argument guarantees the truth of its conclusion. *Good* deductive arguments are called *deductively valid*; their premises are said to *logically entail* their conclusions, where *logical entailment* means that every logically possible state of affairs that makes the premises true also makes the conclusion true. In an inductive logic the truth of the premises of a *good* argument supports the truth of its conclusion to some appropriate degree. That is, the truth of the argument’s premises provides an appropriate *degree-of-support* for the truth of its conclusion. These *degrees-of-support* are typically measured on a numerical scale. By analogy with the notion of deductive logical entailment, the notion of an appropriate inductive degree-of-support may be taken to mean something like this: among the logically possible states of affairs that make the premises true, the conclusion is true in proportion *r* of them.

This article explicates the inductive logic most widely studied by logicians and epistemologists in recent years. The logic employs conditional probability functions to represent the degree to which an argument’s premises support its conclusion. This approach is often called a *Bayesian* inductive logic, because a theorem of probability theory called Bayes’ Theorem plays a central role in articulating how evidence claims inductively support hypotheses.

Ultimately, any adequate inductive logic should provide a mechanism whereby evidence may legitimately refute false hypotheses and endorse true ones. That is, any legitimate inductive logic should provide at least a modest version of the most famous epistemological remark attributed to Sherlock Holmes:

> When you have eliminated all which is impossible, then whatever remains, however improbable, must be the truth.

Although this remark overstates what an inductive logic can usually accomplish, the underlying idea is basically right. That is, a logic of evidential support aspires to endorse the following more modest principle:

> When a rigorous body of evidence shows that all of the credible alternatives to a hypothesis are highly unlikely by comparison, then the remaining hypothesis, however initially implausible, must very probably be true.

This idea, that evidence comes to support the truth of a hypothesis by undermining its competitors, is central to the workings of a Bayesian logic of evidential support. This article will describe in some detail how this Bayesian inductive logic works.

Section 1 explicates the most important inference rules for a Bayesian inductive logic. These rules articulate how some probabilistic arguments may be combined to determine the degree to which evidence weighs for or against hypotheses (as expressed by other probabilistic arguments). Section 2 provides examples of the application of these inference rules.

## 1. Principal Inference Rules for the Logic of Evidential Support

This section lays out the fundamental elements of a probabilistic (Bayesian) inductive logic. We first develop appropriate notation and specify the logical axioms for the conditional probability functions. These conditional probability functions will be used to represent inductive arguments. Next we briefly describe the two most fundamental component arguments in the inference rules for Bayesian inductive inferences: (1) the *evidential likelihoods*, and (2) the *prior plausibility assessments* of hypotheses. Then we explicate four of the most important inference rules for this kind of inductive logic, rules that employ the probability values from likelihood arguments and the prior plausibility arguments to determine the probability values for arguments from evidential premises to hypotheses.

In the main body of this article we will forgo a discussion of the historical origins of probabilistic inductive logic. See the appendix [Historical Origins and Interpretations of Probabilistic Inductive Logic](logic-inductive.appendix1.md) for an overview of the origins, and for a brief summary of views about the nature of probabilistic inductive logic.

### 1.1 Logical Notation

In a probabilistic argument, the degree to which a premise statement $D$ supports the truth or falsehood of a conclusion statement $C$ is expressed in terms of a conditional probability function $P$. A formula of form $P[C \mid D] = r$ expresses the claim that premise $D$ supports conclusion $C$ to degree $r$, where $r$ is a real number between 0 and 1. Notice that the conclusion $C$ is placed on the left-hand side of the conditional probability expression, followed by the premise $D$ on the right-hand side. This reverses the order of premise and conclusion employed in the standard expressions for deductive logical entailment, where the logical entailment of a conclusion $C$ by premise $D$ is usually represented by an expression of form $D \vDash C$.

In applications of deductive logic the main challenge is to determine whether or not a logical entailment, $D \vDash C$, holds for arguments consisting of premises $D$ and conclusions $C$. Similarly, the main challenge in a probabilistic inductive logic is to determine the appropriate values of $r$ such that $P[C \mid D] = r$ holds for arguments consisting of premises $D$ and conclusions $C$. The probabilistic formula $P[C \mid D] = r$ may be read in either of two ways: literally *the probability of $C$ given $D$ is $r$*; but also, *apropos* the application of probability functions *P* to represent argument strengths, *the degree to which $C$ is supported by $D$ is $r$*.

Throughout our discussion we use common logical notation for conjunctions, disjunctions, and negations. We use a *dot* between sentences, $(A \cdot B)$, to represent their conjunction, ($A$ *and* $B$); and we use a *wedge* between sentences, $(A \vee B)$, to represent their disjunction, ($A$ *or* $B$). Disjunction is taken to be inclusive: $(A \vee B)$ means that *at least one* of $A$ or $B$ is true. We use the *not* symbol $\neg$ in front of a sentence to represent its negation: $\neg C$ means *it’s not the case that* $C$.

### 1.2 Logical Axioms for Conditional Probability Functions

Here are standard logical axioms for conditional probabilities. They supply minimal rules for probabilistic support functions. That is, support functions should satisfy at least these axioms, and perhaps some additional rules as well.

Let $L$ be a language of interest — i.e. any bit of language in which the inductive arguments of interest may be expressed — and let $\vDash$ be the logical entailment relation for this language. A conditional probability function (i.e. a probabilistic support function) is a function $P$ from pairs of statements of $L$ to real numbers that satisfies (at least) the following axioms.

1. There are statements $U$, $V$, $X$, and $Y$ such that $P[U \mid V] \neq P[X \mid Y]$ this *nontrivality axiom* rules out the function $P$ that assigns probability value 1 to every argument;

For all statements $A$, $B$, and $C$ in $L$:

1. $0 \le P[A \mid B] \le 1$ premises support conclusions to some degree measured by real numbers between 0 and 1;
2. If $B \vDash A$, then $P[A \mid B] = 1$ the premises of a logical entailment support its conclusion to degree 1;
3. If $C \vDash B$ and $B \vDash C$, then $P[A \mid B] = P[A \mid C]$ logically equivalent premises support a conclusion to the same degree;
4. If $C \vDash \neg(A \cdot B)$, then $P[(A \vee B) \mid C] = P[A \mid C] + P[B \mid C]$, unless $P[D \mid C] = 1$ for every statement $D$;
5. $P[(A \cdot B) \mid C] = P[A \mid (B \cdot C)] \times P[B \mid C]$.

These axioms do not presuppose that logically equivalent statements have the same probability. Rather, that can be proved from these axioms.

Axioms 1-4 should be clear enough as stated. Axiom 5 says that when $C \vDash \neg(A \cdot B)$ (i.e. when $C$ logically entails that $A$ and $B$ cannot both be true), the support-strength of $C$ for their disjunction, $(A \vee B)$, must equal the sum of its support-strengths for each of them individually. The only exception to this additivity condition occurs when $C$ supports every statement $D$ to degree 1. That can happen, for example, when $C$ is logically inconsistent, since (according to standard deductive logic) logically inconsistent statements must logically entail every statement $D$.

The following four rules follow easily from axioms 2, 3, and 5:

1. $P[\neg A \mid C] = 1 - P[A \mid C]$, unless $P[D \mid C] = 1$ for every statement $D$.
2. If $(C \cdot B) \vDash A$, then $P[A \mid C] \ge P[B \mid C]$.
3. If $(C \cdot B) \vDash A$ and $(C \cdot A) \vDash B$, then $P[A \mid C] = P[B \mid C]$.
4. Let $A_1$, $A_2$, …, $A_n$ be $n$ statements such that, for each pair of them $A_i$ and $A_j$, $C \vDash \neg(A_i \cdot A_j)$. Then $P[(A_1 \vee A_2 \vee \ldots \vee A_n) \mid C]\ =$ $P[A_1 \mid C] + P[A_2 \mid C] + \ldots + P[A_n \mid C]$, unless $P[D \mid C] = 1$ for every statement $D$.

These results are derived in the appendix, [Axioms and Some Theorems for Conditional Probability](logic-inductive.appendix2.md). This appendix also includes an alternative way to axiomatize conditional probability, which draws on much weaker axioms to arrive at the same results (i.e. all the above axioms and theorems are derivable from these weaker axioms).

Axiom 6 expresses a fundamental relationship between conditional probabilities. Think of it like this. Call the collection of logically possible states of affairs where a statement $C$ is true *the $C$ states*. Consider the proportion $p$ of $C$ states that are also $B$ states: $P[B \mid C] = p$. A certain fraction $f$ of those $(B \cdot C)$ states are also $A$ states: $P[A \mid (B \cdot C)] = f$. Then, the proportion of the $C$ states that are $(A \cdot B)$ states, $P[(A \cdot B) \mid C]$, *should be* the fraction $f$ of proportion $p$, which is given by $f \times p$. That is, the proportion of the $C$ states that are $(A \cdot B)$ states *should be* the fraction of $(B \cdot C)$ states that are also $A$ states, $f$, of the proportion of $C$ states that are $B$ states, $p$:

$$P[(A \cdot B) \mid C] = f \times p = P[A \mid (B \cdot C)] \times P[B \mid C].$$

From axiom 6, together with axioms 3 and 5, a simple form of Bayes’ Theorem follows: if $P[B \mid C] \gt 0$, then

$$P[A \mid (B \cdot C)] = \dfrac{P[B \mid (A \cdot C)] \times P[A \mid C]}{P[B \mid C]}.$$

To see how Bayes’ Theorem can represent an inference rule governing the evidential support for a hypothesis, replace $A$ by some hypothesis $h$, replace $B$ by some relevant body of evidence $e$, and let $c$ represent some appropriate conjunction of background and auxiliary conditions, including whatever experimental or observational conditions (a.k.a. *initial conditions*) may be required to link $h$ to $e$ (more about this below). Then, the appropriate version of Bayes’ Theorem takes the following form: if $P[e \mid c] \gt 0$, then

$$P[h \mid (e \cdot c)] = \dfrac{P[e \mid (h \cdot c)] \times P[h \mid c]}{P[e \mid c]}.$$

Thus, Bayes’ Theorem represents the way in which the strength of the evidential support for a hypothesis, $P[h \mid (e \cdot c)]$, can be calculated from the strengths of three other probabilistic arguments: $P[e \mid (h \cdot c)]$, $P[h \mid c]$, and $P[e \mid c]$. Stated this way, Bayes’ Theorem may not look much like an inference rule. So, let’s articulate more precisely how an equation like this may be construed as an inference rule. It represents a rule that draws on the strengths of three probabilistic arguments to infer the strength of a further argument. Thus, as an inference rule, Bayes’ Theorem may be expressed as follows:

**if**:

the strength of the argument from $c$ to $e$ is $q$, for $q \gt 0$   (i.e. $P[e \mid c] = q \gt 0$), and the strength of the argument from $(h \cdot c)$ to $e$ is $r$   (i.e. $P[e \mid (h \cdot c)] = r$), and the strength of the argument from $c$ to $h$ is $s$   (i.e. $P[h \mid c] = s$),

**then**:

the strength of the argument from $(e \cdot c)$ to $h$ is $t = r \times s / q$   (i.e. then $P[h \mid (e \cdot c)] = t$, where $t = r \times s / q$).

Each of the inference rules for the inductive logic of evidential support presented in this article is based on this basic Bayesian idea. However, it usually turns out that the numerical value $q$ of the strength of the argument $P[e \mid c] = q$ is especially difficult to evaluate. So, the Bayesian inference rules provided throughout the remainder of this article will not depend on probabilistic arguments of the form $P[e \mid c] = q$. Furthermore, the strengths $s$ of arguments of form $P[h \mid c] = s$ are often quite vague or indeterminate. This issue will receive special attention as we proceed.

We now proceed to consider four basic rules of Bayesian inference for an inductive logic. Each of these rules follows from the above axioms. However, before getting into the rules themselves, we need to first investigate more carefully the two kinds of argumentative components that will be employed by each of these rules: $P[e \mid (h \cdot c)] = r$ and $P[h \mid c] = s$.

### 1.3 Components of the Inference Rules for Inductive Logic

In nearly all applications of probabilistic inductive logic, the arguments of interest involve an assessment of the degree to which observable or detectable evidence $e$ tells for or against a hypothesis and its competing alternatives. Let $h_1$, $h_2$, $h_3$, …, etc., represent a collection of two or more competing alternative hypotheses. Hypotheses count as *competing alternatives* when they address the same subject matter, but disagree with regard to at least some claims about that subject matter. Thus, we take any two alternative hypotheses from the collection, $h_i$ and $h_j$, to be logically incompatible: $\vDash \neg (h_i \cdot h_j)$ — i.e. it is logically true that $\neg (h_i \cdot h_j)$.

The bearing of evidence on the probable truth or falsehood of a hypothesis can seldom, if ever, be assessed on the basis of evidential results alone. For one thing, the bearing of evidential results $e$ on hypothesis $h_j$ depends on the conditions under which the observations were made, or on how the experiment was set up and conducted. Let $c$ represent (a conjunction of) statements that describe the observational or experimental conditions (sometimes called the *initial conditions*) that give rise to evidential results described by (conjunction of) statements $e$.

Furthermore, the bearing of evidential conditions and their outcomes, $(c \cdot e)$, on a hypothesis $h_j$ will often depend on auxiliary hypotheses — e.g. auxiliary claims about how measuring devices produce outcomes relevant to $h_j$ under conditions like $c$. Let $b$ represent the conjunction of all such auxiliary claims that connect each competing hypothesis, $h_i$, $h_j$, etc. to outcomes $e$ of conditions $c$. For example, suppose the various hypotheses propose alternative medical disorders that may be afflicting a particular patient. Conditions $c$ may describe a body of medical tests performed on the patient (e.g. blood drawn and submitted to various specific tests), and $e$ may state the precise outcomes of those tests (e.g. precise values for white cell count, blood sugar level, AFP level, etc.). However, descriptions of medical tests and their outcomes can only weigh for or against the presence of a disorder in light of auxiliary hypotheses about the ways in which each disorder $h_j$ is likely to influence those test outcomes (e.g. how each possible medical disorder is likely to influence white cell counts, blood sugar levels, AFP levels, etc.). The expression $b$, for *b*ackground claims, represents the conjunction of such auxiliaries. (Many of the claims in $b$ should themselves be subject to evidential support in contexts where they compete with alternative claims about their own subject matters. More on this later.)

A comprehensive assessment of the probable truth of a hypothesis should also depend on some body of plausibility considerations — on how much more (or less) plausible $h_j$ is than alternatives $h_i$, based on considerations *prior* to bringing the evidence to bear. A reasonable inductive logic should reflect the idea that *extraordinary claims require extraordinarily evidence*. That is, a hypothesis that makes extraordinary claims requires exceptionally strong evidence to overcome its initial implausibility. So, it makes good sense that the logic should have a way to accommodate how much more or less plausible one hypothesis is than an alternative, prior to taking the evidence into account. For example, in diagnosing a medical disorder, it makes good sense to take into account how commonly (or rarely) each alternative disorder occurs within the most relevant sub-population to which the patient belongs. This is called the *base rates* of disorders in the relevant sub-population. We’ll soon see how such considerations figure into the inference rules of inductive logic. For the purpose of describing the logic, we also let symbol $b$ represent the conjunction of whatever relevant plausibility considerations are brought to bear on the initial plausibilities of hypotheses, along with whatever relevant auxiliary hypotheses are employed.

Expressed in these terms, a primary objective of a probabilistic inductive logic is to assess the degree-of-support for (or against) each competing hypothesis $h_j$ by a premise of form $(c \cdot e\cdot b)$, consisting of evidential condition $c$ together with its observable outcome $e$, in conjunction with relevant auxiliary hypotheses and plausibility claims $b$. That is, the objective is to determine the numerical value $t$ for a probabilistic argument of form $P[h_j \mid c \cdot e\cdot b] = t$. This expression is usually called the *posterior probability* of hypothesis $h_j$ on evidence $(c \cdot e)$, given background $b$. Thus, the primary objective of the logic is to assess the values $t$ of the *posterior probabilities* of such evidential arguments.

The most basic inference rule for the Bayesian logic of evidential support is comparative in nature. That is, this most basic rule does not directly provide values for individual posterior probabilities. Rather, it provides *ratio comparisons* of the posterior probabilities (the argument weights) for competing hypotheses.

Let $h_i$ and $h_j$ be any two distinct hypotheses from a list of competing alternatives. The *comparative degrees-of-support* for these two hypotheses is given by a numerical value $q$ for the ratio of their posterior probabilities: $P[h_i \mid c \cdot e\cdot b] / P[h_j \mid c \cdot e\cdot b] = q$. This ratio measures how much more (or less) strongly the premise $(c \cdot e \cdot b)$ supports $h_i$ than it supports $h_j$. The most basic rule for the logic states a direct way to calculate the values $q$ for such ratios; and it does this without providing values for the individual posterior probabilities, $P[h_i \mid c \cdot e \cdot b]$ and $P[h_j \mid c \cdot e \cdot b]$, themselves. We’ll see how this works when we introduce the relevant inference rule, in the next subsection.

The inference rule for determining the value $q$ of a posterior probability ratio draws on only two distinct kinds of probabilistic arguments:

1. The *likelihoods* of the evidence according to various hypotheses: A *likelihood* is a probabilistic argument of form $P[e \mid h_k \cdot c \cdot b] = r$. It is a probabilistic argument from premises $(h_k \cdot c \cdot b)$ to a conclusion $e$. This argument expresses what hypothesis $h_k$ *says* about *how likely it is* that evidence claim $e$ should be true when evidential conditions $c$ and auxiliary claims stated within $b$ are also true. Likelihoods express the empirical content of a hypothesis, what it *says* an observable part of the world is probably like. In order for two hypotheses, $h_i$ and $h_j$, to differ in empirical content (given $b$), there must be some *possible* evidential conditions $c$ that have possible outcomes $e$ on which the likelihoods for the two hypotheses disagree:

> $P[e \mid h_i \cdot c \cdot b] = r \neq s = P[e \mid h_j \cdot c \cdot b].$

It turns out that Bayesian inductive inference rules don’t depend directly on the individual values of likelihoods, but only on the values $v$ of *ratios of likelihoods*:

> $v = P[e \mid h_i \cdot c \cdot b] / P[e \mid h_j \cdot c \cdot b]$.

These *likelihood ratios* (a.k.a. *Bayes Factors*) represent how much more (or less) likely the evidential outcome $e$ should be if hypothesis $h_i$ is true than if alternative hypothesis $h_j$ is true. They embody the means by which empirical content evidentially distinguishes between two competing hypotheses.

In many scientific contexts the exact values of individual likelihoods are calculable, often via some explicit statistical model on which the hypothesis together with auxiliaries, $(h_k \cdot b)$, draws. Clearly, in contexts where the exact values of likelihoods are calculable, exact values of these likelihood ratios are calculable as well. However, even in cases where the individual hypotheses, $h_i$ and $h_j$, provide somewhat vague or imprecise information regarding the values for individual likelihoods, it may be possible to assess reasonable estimates of upper and lower bounds on their likelihood ratios. We will see how such bounds on likelihood ratios may provide important evidential inputs for the inductive inference rules.

When the evidence consists of a collection of $m$ distinct experiments or observations and their outcomes, $(c_1 \cdot e_1)$, $(c_2 \cdot e_2)$, …, $(c_m \cdot e_m)$, we use the term $c$ to represent the conjunction of these experimental or observational conditions, $(c_1 \cdot c_2 \cdot \ldots \cdot c_m)$, and we use the term $e$ to represent the conjunction of their respective outcomes, $(e_1 \cdot e_2 \cdot \ldots \cdot e_m)$. For notational convenience we may employ the term $c^m$ to abbreviate the conjunction of the $m$ experimental conditions, and we use the term $e^m$ to abbreviate the corresponding conjunction of their outcomes. Given a specific hypothesis $h_k$ together with relevant auxiliaries $b$, the evidential outcomes of these distinct experiments or observations will usually be probabilistically independent of one another, and will also be independent of the experimental conditions for one another’s outcomes. In that case the likelihood $P[e \mid h_k \cdot c \cdot b]$ decomposes into the following terms:

$$\begin{align} &P[e \mid h_k \cdot c \cdot b] = P[e^m \mid h_k \cdot c^m \cdot b] \\ &~ = P[e_1 \mid h_k \cdot c_1 \cdot b] \times P[e_2 \mid h_k \cdot c_2 \cdot b] \times \cdots \times P[e_m \mid h_k \cdot c_m \cdot b]. \end{align}$$

Thus, when the likelihoods represent evidence that consists of a collection of $m$ distinct probabilistically independent experiments (or observations) and their respective outcomes, the likelihood ratios may take the following form:

$$\begin{align} &\frac{P[e \mid h_i \cdot c \cdot b]}{P[e \mid h_j \cdot c \cdot b]} = \frac{P[e^m \mid h_i \cdot c^m \cdot b]}{P[e^m \mid h_j \cdot c^m \cdot b]} \\ &~ = \frac{P[e_1 \mid h_i \cdot c_1 \cdot b]}{P[e_1 \mid h_j \cdot c_1 \cdot b]} \times \frac{P[e_2 \mid h_i \cdot c_2 \cdot b]}{P[e_2 \mid h_j \cdot c_2 \cdot b]} \times \ldots \times \frac{P[e_m \mid h_i \cdot c_m \cdot b]}{P[e_m \mid h_j \cdot c_m \cdot b]}. \end{align}$$

2. The *prior plausibilities* of hypotheses: A *prior probability* is a probabilistic argument for or against a hypothesis of form $P[h_k \mid b]$ or $P[h_k \mid c \cdot b]$, where the information carried by $b$ or $(c \cdot b)$ does *not* contain the kinds of evidential outcomes $e$ for which the $h_k$ expresses likelihoods. These probabilistic arguments need not be *a prior* arguments for hypothesis $h_k$, as some have suggested. Nor need they merely express the subjective opinions of individual persons. Rather, the values for these arguments should represent an assessment of the plausibility of hypotheses based on a range of relevant considerations, including broadly empirical facts not captured by evidential likelihoods. For instance, such plausibility arguments may involve considerations of the *simplicity* of the hypothesis, whether it is overly *ad hoc*, whether it provides (or is at least consistent with) a reasonable causal mechanism, etc. Such considerations may be explicitly stated within statement $b$. (This view on the nature of Bayesian probabilities, and especially the prior probabilities, most closely follows in the tradition of such Bayesians as Keynes, Jeffreys, and Jaynes. Alternatively, many Bayesians, in the tradition of Ramsey, de Finetti, and Savage, take all Bayesian probabilities, including the priors, to express individual subjective degrees of belief. However, the mathematical rules of the Bayesian logic itself do not in any way depend on the resolution of this issue regarding conceptual nature of Bayesian probabilities. So we can set this issue aside here.)

In many contexts such initial plausibility assessments will not be well-represented by precise numerical values. However, it turns out that the inductive inference rules presented below need only draw on the values $u$ for *ratios of priors*:

$$ u = P[h_i \mid c \cdot b] / P[h_j \mid c \cdot b]. $$

These ratios represent how much more (or less) plausible hypothesis $h_i$ is taken to be than alternative hypothesis $h_j$, given their comparative *simplicity*, *ad hocness*, *causal viability*, etc., and including whatever broadly empirical factors are relevant to the specific field of inquiry to which these hypotheses are relevant.

Furthermore, such comparative plausibility assessments may often be too vague to be represented by precise numerical values. Rather, they will often be best represented by numerical intervals:

$$ u \ge P[h_i \mid c \cdot b] / P[h_j \mid c \cdot b] \ge v,$$

for real numbers $u$ and $v$.

One more point. Although the description of the observational/experimental conditions, embodied by $c$, will not usually be relevant to the prior probability values (in the absence of outcome $e$), the probabilistic logic itself doesn’t automatically permit the dismissal of information that may be contained in $c$. Rather, the logic requires that the relevance of $c$ be specifically addressed. However, if absent outcome $e$, conditions $c$ are equally relevant to $h_i$ and $h_j$, then the probabilistic logic permits $c$ to be dropped, yielding comparative plausibility ratios of the following form:

$$ u \ge P[h_i \mid b] / P[h_j \mid b] = P[h_i \mid c \cdot b] / P[h_j \mid c \cdot b] \ge v. $$

So, although the rules for inductive inferences described below will continue to include statements $c$ within the prior probability arguments, the reader should keep in mind that $c$ is usually not relevant to these arguments, and can be dropped from them.

The logic of evidential support combines the numerical values of these two kinds of factors to produce an assessment of the degree of support, $P[h_k \mid c \cdot e \cdot b]$, for hypotheses. To see how this works, first return to following form of Bayes’ Theorem, applied to each hypothesis $h_k$: $$P[h_k \mid c \cdot e \cdot b] = \frac{P[e \mid h_k \cdot c \cdot b] \times P[h_k \mid c \cdot b]}{P[e \mid c \cdot b]}.$$ The value of the term $P[e \mid c \cdot b]$, which occurs in the denominator of this form of Bayes’ Theorem, is usually difficult (even impossible) to assess. So it is generally more useful to consider the *comparative support* of pairs of competing hypotheses by the evidence. Applying Bayes’ Theorem to each of a pair of hypotheses, $h_i$ and $h_j$, and then taking their ratio, produces the following formula for assessing their comparative support, via the ratio of their posterior probabilities: $$\frac{P[h_i \mid c \cdot e \cdot b]}{P[h_j \mid c \cdot e \cdot b]} = \frac{P[e \mid h_i \cdot c \cdot b] \times P[h_i \mid c \cdot b]}{P[e \mid h_j \cdot c \cdot b] \times P[h_j \mid c \cdot b]}.$$ The following two sections explicate this Ratio Form of Bayes’ Theorem, and show how it captures the essential features of Bayesian inductive inference.

### 1.4 Inference Rule *RB*: the Ratio Form of Bayes’ Theorem

In this section and the next we look at two closely related versions of Bayes’ Theorem as it applies to competing hypotheses. The present section is devoted to the most elementary version, the *Ratio Form of Bayes’ Theorem*. Here it is.

**Rule RB: Ratio Form of Bayes’ Theorem**

Let $h_1$, $h_2$, …, be a list of two or more alternative hypotheses, *alternatives* in the sense that the conjunction of any two of them, $(h_i \cdot h_j)$, is logically inconsistent (i.e. no two of them can both be true): $\vDash \neg (h_i \cdot h_j)$. Let $c$ be observational or experimental conditions for which $e$ is among the possible outcomes. And suppose $b$ is a conjunction of relevant auxiliary hypotheses and plausibility considerations.

Let $h_j$ be any hypothesis from the list for which both $P[e \mid h_j \cdot c \cdot b] > 0$ and $P[h_j \mid c \cdot b] > 0$.

> Then $P[h_j \mid c \cdot e \cdot b] > 0$, *and* for each $h_i$ among the alternatives to $h_j$,

$$ \frac{P[h_i \mid c \cdot e \cdot b]}{P[h_j \mid c \cdot e \cdot b]} = \frac{P[e \mid h_i \cdot c \cdot b]}{P[e \mid h_j \cdot c \cdot b]} \times \frac{P[h_i \mid c \cdot b]}{P[h_j \mid c \cdot b]}. $$

> This ratio also provides an upper bound on $P[h_i \mid c \cdot e \cdot b]$, since

$$ P[h_i \mid c \cdot e \cdot b] \le \frac{P[h_i \mid c \cdot e \cdot b]}{P[h_j \mid c \cdot e \cdot b]}. $$

This *Ratio Form of Bayes’ Theorem* is straightforwardly derivable from the above axioms for conditional probability functions.

In any application of *Rule RB*, the *likelihood ratios* carry the full import of the evidence $(c \cdot e)$. The evidence influences the evaluation of hypotheses in no other way. In many scientific contexts, each hypothesis (together with auxiliaries) provides a precise value for the likelihoods of evidence claims. In such cases the exact values for *likelihood ratios* can be calculated. Indeed, in any given epistemic context, *RB* is useful as a *rule of inference* for inductive logic only if, for each pair of hypothesis $h_i$ and $h_j$ in the context, the values of (or at least reasonable bounds on) their *likelihood ratios* are determinable or calculable.

In *Rule RB*, the only other factor that influences the value of the *ratio of posterior probabilities* is the ratio of their associated prior probabilities. And these *ratios of priors* play a central role. So, for *Rule RB* to be useful as a rule of inference for inductive logic, the values of these *ratios of priors* must be estimable or calculable — or, at least credible upper and lower bounds on them must be assessable.

For some kinds of hypotheses, reasonably precise values for the individual prior probabilities may be available, so the numerical value for the *ratio of priors* may be calculated. However, in many epistemic contexts the prior probability values for individual hypotheses are vague and difficult to determine. In these contexts it will often be easier to assess the *ratio of priors* directly, since it represents an assessment of how much more (or less) plausible one hypothesis is than another. Indeed, an assessment of credible upper and lower bounds on *comparative plausibilities* suffices for the kinds of inductive inferences supplied by *Rule RB*. For, given a significant body of evidence, the associated *likelihood ratios* applied to wide bounds on the *comparative prior plausibilities* will often produce quite narrow bounds on the resulting ratios of *posterior probabilities*.

Notice that *Rule RB* implies that if either $P[e \mid h_i \cdot c \cdot b] = 0$ or $P[h_i \mid c \cdot b] = 0$, then $P[h_i \mid c \cdot e \cdot b] = 0$.

When $P[h_i \mid c \cdot e \cdot b] = 0$ is due to $P[e \mid h_i \cdot c \cdot b] = 0$, we have an extended version of the notion of the *falsification* of a hypothesis. *Falsification* is usually associated with the deductive refutation of a hypothesis by evidence. That is, when $(h_i \cdot c \cdot b) \vDash e^*$, but the actual outcome $e$ is logically incompatible with $e^*$, it follows that $(h_i \cdot c \cdot b) \vDash \neg e$. Then, deductively, it also follows that $(c \cdot e \cdot b) \vDash \neg h_i$, and $h_i$ is said to be *falsified* by $(c \cdot e)$, given $b$.

*Rule RB* captures this idea, since when $(h_i \cdot c \cdot b) \vDash \neg e$, probability theory yields $P[\neg e \mid h_i \cdot c \cdot b] = 1$, so $P[e \mid h_i \cdot c \cdot b] = 0$, in which case rule *RB* yields $P[h_i \mid c \cdot e \cdot b] = 0$. And, according to *RB*, $P[e \mid h_i \cdot c \cdot b] = 0$ suffices for $P[h_i \mid c \cdot e \cdot b] = 0$, from which it follows that $P[\neg h_i \mid c \cdot e \cdot b] = 1$.

*Rule RB* goes further by showing how evidence may come to *strongly refute* a hypothesis $h_i$, without fully falsifying it. Suppose now that both $P[h_j \mid c \cdot b] > 0$ and $P[h_i \mid c \cdot b] > 0$. Then, regardless of how plausible or implausible $h_i$ is taken to be as compared to $h_j$, provided that $h_j$ isn’t *way too implausible*, if the body of evidence $e$ is sufficiently unlikely on $h_i$ as compared to $h_j$, then *Rule RB* says that the posterior probability of $h_i$ on that evidence must also be extremely close to 0.

More formally, suppose that $P[h_i \mid c \cdot b] / P[h_j \mid c \cdot b] \le K$, where $K$ may be some very large number. This represents the idea that $h_i$ is initially considered to be up to $K$ times more plausible than $h_j$. Let *ε* be some extremely small number, as close to 0 as you wish. Then, according to *Rule RB*, to get the value of $P[h_i \mid c \cdot e \cdot b]$ within *ε* of 0, it suffices for the body of evidence to favor $h_j$ over $h_i$ strongly enough that $P[e \mid h_i \cdot c \cdot b] \lt (\epsilon / K) \times P[e \mid h_j \cdot c \cdot b]$. That is, via *Rule RB*:

$$\begin{align} &\text{When }~ \frac{P[h_i \mid c \cdot b]}{P[h_j \mid c \cdot b]} \le K, ~\text{ if }~ \frac{P[e \mid h_i \cdot c \cdot b]}{P[e \mid h_j \cdot c \cdot b]} \lt \frac{\epsilon}{K}, \\ &\text{then }~ P[h_i \mid c \cdot e \cdot b] \lt \epsilon. \end{align}$$

If all but the most extremely implausible alternatives to hypothesis $h_j$ become *strongly refuted* in this way by a body of evidence $(c \cdot e)$, then the posterior probability of $h_j$, $P[h_j \mid c \cdot e \cdot b]$, should approach 1. Thus, may $h_j$ become strongly supported by the evidence. The next rule will endorse this idea more fully.

### 1.5 Inference Rule *OB*: the Odds Form of Bayes’ Theorem

*Rule RB* contributes to a more comprehensive inference rule, one that applies to collections of competing hypotheses. This more comprehensive rule employs the well-known probabilistic concept of *odds*. By definition, the *odds of $A$ given $B$*, written $\Omega[A \mid B]$, is related to the *probability of $A$ given $B$* by the formula: $$\Omega[A \mid B] = \frac{P[A \mid B]}{P[\neg A \mid B]}.$$ However, for our purposes it will be more useful to employ the inverse ratio of the *odds*, the *odds against $A$ given $B$*: $$\Omega[\neg A \mid B] = \frac{P[\neg A \mid B]}{P[A \mid B]} = \frac{1 - P[A \mid B]}{P[A \mid B]}.$$ From the definition of *odds against*, it follows that: $$P[A \mid B] = \frac{1}{1 + \Omega[\neg A \mid B]}.$$

Here is how odds comes into play in Bayesian inductive logic. Sum the ratio versions of Bayes’ Theorem, as given by *Rule RB*, over a range of alternatives to hypothesis $h_j$. This yields the *Odds Form of Bayes’ Theorem*. And from that we can calculate the individual values of posterior probabilities.

**Rule OB: Odds Form of Bayes’ Theorem**

Let $H$ = {$h_1$, $h_2$, …, $h_n$} be a collection of two or more alternative hypotheses (i.e. $n \ge 2$), where the conjunction of any two of them is logically inconsistent, $\vDash \neg (h_i \cdot h_j)$. Let $c$ be observational or experimental conditions for which $e$ is among the possible outcomes. And suppose $b$ is a conjunction of relevant auxiliary hypotheses and plausibility considerations.

Let $h_j$ be any hypothesis from the list for which both $P[h_j \mid c \cdot b] > 0$ and $P[e \mid h_j \cdot c \cdot b] > 0$.

Then $P[h_j \mid c \cdot e \cdot b] > 0$ *and* for each $h_i$ an alternative to $h_j$,

$$\begin{align} \Omega[\neg h_j \mid c \cdot e \cdot b \cdot (h_i \vee h_j)] &= \frac{P[h_i \mid c \cdot e \cdot b]}{P[h_j \mid c \cdot e \cdot b]} \\ &= \frac{P[e \mid h_i \cdot c \cdot b]}{P[e \mid h_j \cdot c \cdot b]} \times \frac{P[h_i \mid c \cdot b]}{P[h_j \mid c \cdot b]}. \end{align}$$

Furthermore,

$$\begin{align} \Omega[\neg h_j \mid& c \cdot e \cdot b \cdot (h_1 \vee h_2 \vee \ldots \vee h_n)] \\ &= \sum_{i = 1, i \ne j}^n \Omega[\neg h_j \mid c \cdot e \cdot b \cdot (h_i \vee h_j)] \\ &= \sum_{i = 1, i \ne j}^n \frac{P[e \mid h_i \cdot c \cdot b]}{P[e \mid h_j \cdot c \cdot b]} \times \frac{P[h_i \mid c \cdot b]}{P[h_j \mid c \cdot b]}. \end{align}$$

Finally, the associated posterior probability of $h_j$, the degree to which premise $(c \cdot e \cdot b \cdot (h_1 \vee h_2 \vee \ldots \vee h_n))$ supports conclusion $h_j$, is given by the formula

$$\begin{align} &P[h_j \mid c \cdot e \cdot b \cdot (h_1 \vee h_2 \vee \ldots \vee h_n)] \\ &\quad = \frac{1}{1 + \Omega[\neg h_j \mid c \cdot e \cdot b \cdot (h_1 \vee h_2 \vee \ldots \vee h_n)]}. \end{align}$$

Thus, *Rule OB* shows that the *odds against a hypothesis*, assessed against a finite collection of alternatives, depends only on the values of *ratios of posterior probabilities*, where each of these ratios entirely derives from the *Ratio Form of Bayes’ Theorem*, stated by *Rule RB*. The same goes for the *posterior probability of a hypothesis*, since its value entirely derives from the odds against it. Thus, the *Ratio Form of Bayes’ Theorem* captures the essential features of the Bayesian evaluation of hypotheses. It shows how the impact of evidence, captured by *likelihood ratios*, combine with comparative plausibility assessments of hypotheses, captured by *ratios of prior probabilities*, to provide a net assessment of the extent to which hypotheses are refuted or supported in a contest with their rivals.

We conclude this section with a comment about why the posterior odds and posterior probabilities provided by *Rule OB* usually need to be relativised to finite disjunctions of alternative hypotheses, $(h_1 \vee h_2 \vee \ldots \vee h_n)$.

First notice that in any specific epistemic context where the collection of $n$ alternative hypotheses, $\{h_1, h_2, \ldots, h_n\},$ consists of *all possible* alternatives about the subject matter at issue, and if background statement $b$ says so (i.e. if $b \vDash (h_1 \vee h_2 \vee \ldots \vee h_n)$), then the explicit use of disjunctions of hypotheses can be dropped from the equations in *Rule OB*. For, in that context,

$$\Omega[\neg h_j \mid c \cdot e \cdot b] = \Omega[\neg h_j \mid c \cdot e \cdot b \cdot (h_1 \vee h_2 \vee \ldots \vee h_n)]. $$

However, in many epistemic contexts an investigator may not be aware of *all possible* alternative hypotheses or theories about the subject at issue. For instance, the medical community may not have identified every possible disorder or disease that may afflict a patient. Furthermore, in some contexts it may not even be possible to formulate *all possible* alternative hypotheses or theories — e.g. all possible alternative theories about the fundamental nature of space-time and the origin of the universe. In such cases, the best we can do is evaluate evidential support for (and against) those hypotheses we’ve formulated thus far, always keeping in mind that the list of alternatives might well be expanded to additional alternatives.

Now, just one further point. Suppose that the list of $n$ alternatives contains all alternative hypotheses that the relevant epistemic community has formulated so far, but other unidentified alternatives remain possible. Can we not appeal to the following Bayesian result to bypass the need to relativise to the disjunction of presently formulated alternative hypotheses? After all, this result is also a theorem of probability theory.

For $P[e \mid h_j \cdot c \cdot b] > 0$ and $P[h_j \mid c \cdot e\cdot b] > 0$,

$$\begin{align} &\Omega[\neg h_j \mid c \cdot e \cdot b] \\ &~ = \sum_{i = 1, i \ne j}^n \frac{P[h_i \mid c \cdot e \cdot b]}{P[h_j \mid c \cdot e\cdot b]} + \frac{P[(\neg h_1 \cdot \neg h_2 \cdot \ldots \cdot \neg h_n) \mid c \cdot e \cdot b]}{P[h_j \mid c \cdot e\cdot b]} \\ &~ = \Omega[\neg h_j \mid c \cdot e \cdot b \cdot (h_1 \vee h_2 \vee \ldots \vee h_n)] + \frac{P[(\neg h_1 \cdot \neg h_2 \cdot \ldots \cdot \neg h_n) \mid c \cdot e \cdot b]} {P[h_j \mid c \cdot e\cdot b]}, \end{align}$$

where the final term is given by the equation,

$$\begin{align} &\frac{P[(\neg h_1 \cdot \neg h_2 \cdot \ldots \cdot \neg h_n) \mid c \cdot e \cdot b]}{P[h_j \mid c \cdot e\cdot b]} \\ &\quad= \frac{P[e \mid (\neg h_1 \cdot \neg h_2 \cdot \ldots \cdot \neg h_n) \cdot c \cdot b]}{P[e \mid h_j \cdot c \cdot b]} \times \frac{P[(\neg h_1 \cdot \neg h_2 \cdot \ldots \cdot \neg h_n) \mid c \cdot b]}{P[h_j \mid c \cdot b]}. \end{align}$$

The problem with this idea is that it draws on likelihoods of form $P[e \mid (\neg h_1 \cdot \neg h_2 \cdot \ldots \cdot \neg h_n) \cdot c \cdot b]$. Such likelihoods will almost never have explicitly determinable or calculable values. So, the values of $\Omega[\neg h_j \mid c \cdot e \cdot b]$ and $P[h_j \mid c \cdot e \cdot b]$ that derive from formulas that draw on this kind of likelihood must also fail to be determinable or calculable. So, this approach to sidestepping the relativization to $(h_1 \vee h_2 \vee \ldots \vee h_n)$ is at cross-purposes with the idea that an inductive logic should be couched in terms of *usable rules* of inductive inference.

Nevertheless, the calculable values of $\Omega[\neg h_j \mid c \cdot e \cdot b \cdot (h_1 \vee h_2 \vee \ldots \vee h_n)]$ provided by *Rule OB* do entail explicit *bounds* on the values for the non-disjunctively-relativized posterior odds and posterior probabilities. For, the probabilistic logic entails the following relationships:

$$\Omega[\neg h_j \mid c \cdot e \cdot b] \ge \Omega[\neg h_j \mid c \cdot e \cdot b \cdot (h_1 \vee h_2 \vee \ldots \vee h_n)],$$

and so

$$P[h_j \mid c \cdot e \cdot b] \le P[h_j \mid c \cdot e \cdot b \cdot (h_1 \vee h_2 \vee \ldots \vee h_n)].$$

Thus, if the evidence pushes $P[h_j \mid c \cdot e \cdot b \cdot (h_1 \vee h_2 \vee \ldots \vee h_n)]$ close to 0, then it also must push $P[h_j \mid c \cdot e \cdot b]$ close to 0. However, although pushing $P[h_i \mid c \cdot e \cdot b \cdot (h_1 \vee h_2 \vee \ldots \vee h_n)]$ close to 0 for all $(n-1)$ competitors of $h_j$ results in the approach of $P[h_j \mid c \cdot e \cdot b \cdot (h_1 \vee h_2 \vee \ldots \vee h_n)]$ to 1, it need not result in the the approach of the non-disjunctively-relativized posterior $P[h_j \mid c \cdot e \cdot b]$ to 1. For, some as yet unconsidered alternative hypothesis may well be able to do better than $h_j$ on the currently available evidence $(c \cdot e \cdot b)$. The logic of Bayesian inference does not rule out this possibility.

### 1.6 Inference Rules for Bayesian Interval Estimation

This section specifies two additional inference rules for Bayesian inductive logic. They are specialized versions of Bayes’ Theorem — basically extended versions of rule *OB*. These two rules are especially useful in cases of interval estimation, where the evidence bears on whether the true hypothesis lies within some specific interval of alternative claims. The first of these two rules will be stated in terms of evidential support for disjunctions of hypotheses. The precise statement of this rule does not presuppose that the hypotheses it addresses lie within some interval of values; rather, it applies to the support for any finite disjunction of hypotheses. However, one of its important applications is to the evidential support of a *disjunctive interval* of alternative hypotheses. An example application to a disjunctive interval of alternative hypotheses is provided in Section 2.4.

The second rule applies to the support of competing hypotheses that range over continuous intervals of real numbers. For example, consider each hypothesis of form, “the chance of *heads* on tosses of this particular (possibly biased) coin is $r$”, where $r$ must have some real number value between 0 and 1. Perhaps the true value of $r$ for this particular coin is .72. However, the evidence won’t usually single out this exact chance hypothesis. Rather, the best we can usually do is use evidence to narrow down the interval within which the true value of $r$ very probably resides (e.g. show that the posterior probability that $r$ lies between .67 and .77 is .95, based on the evidence). The statement of this second interval estimation rule will closely resemble the statement of the first rule, but modifies it to apply to continuous intervals of values. An example is provided in Section 2.5.

#### 1.6.1 Inference Rule *BE-D*: Bayesian Estimation for Disjunctions of Hypotheses

The following rule provides lower bounds on the posterior probability of disjunctions of alternative hypotheses. It derives from the above axioms for conditional probabilities, with no additional suppositions beyond those explicitly stated in the rule itself. Although the statement of this rules is quite general, its most common application is to disjunctions of hypotheses about closely spaced numerical quantities.

**Rule BE-D: Bayesian Estimation for Disjunctions of Alternative Hypotheses**

Let $H$ be a collection of $z$ alternative hypotheses, $z \ge 2$, where the conjunction of any two of them is logically inconsistent. Let $c$ be observational or experimental conditions for which $e$ describes one of the possible outcomes. And suppose $b$ is a conjunction of relevant auxiliary hypotheses and plausibility considerations. For each hypothesis $h_i$ in $H$, let its prior probability be non-zero: $P[h_i \mid c \cdot b] \gt 0$.

Choose any $k$ hypotheses from collection $H$, where each one of them, $h_i$, has a likelihood value $P[e \mid h_i \cdot c \cdot b] > 0$. Label these $k$ hypotheses (in whatever order you wish) as $\lsq h_1\rsq$, $\lsq h_2\rsq$, $\ldots$, $\lsq h_k\rsq$. Then label all the remaining hypotheses in $H$ (in whatever order you wish) as $\lsq h_{k+1}\rsq$, $\lsq h_{k+2}\rsq$, $\ldots$, $\lsq h_z\rsq$.

Given these labelings of hypotheses in $H$, let $(h_1 \vee \ldots \vee h_k)$ represent the disjunction of the first $k$ hypotheses chosen from $H$, and $(h_{k+1} \vee \ldots \vee h_z)$ represent the disjunction of the remaining hypotheses from $H$. The expression $(h_1 \vee \ldots \vee h_z)$ represents the disjunction of all hypotheses in $H$. Furthermore, let’s take $b$ to logically entail that one of the hypotheses in $H$ is true — i.e. $b$ logically entails the disjunction of all alternative hypotheses in $H$: $b \vDash (h_1 \vee \ldots \vee h_z)$. So, both $P[(h_1 \vee \ldots \vee h_z) \mid c \cdot b] = 1$ and $P[(h_1 \vee \ldots \vee h_z) \mid c \cdot e \cdot b] = 1$.

Then, the posterior probability of $(h_1 \vee \ldots \vee h_k)$ satisfies the following form of Bayes’ Theorem:

$$ P[(h_1 \vee \ldots \vee h_k) \mid c \cdot e \cdot b] \; \; = \; \; \frac{\sum_{j = 1}^k P[e \mid h_j \cdot c \cdot b] \times P[h_j \mid c \cdot b]}{\sum_{i = 1}^z P[e \mid h_i \cdot c \cdot b] \times P[h_i \mid c \cdot b]}. $$

In cases where the values of all the prior probabilities, $P[h_i \mid c \cdot b]$, are known, or can be closely approximated, this equation suffices to provide values for the argument strengths $r$ of the posterior probabilities, $P[(h_1 \vee \ldots \vee h_k) \mid c \cdot e \cdot b] = r$. But when no precise values of the priors are available, a useful estimate of bounds on the posterior probabilities may be derived as follows.

Let $K$ be (your best estimate of) an upper bound on the ratios of prior probabilities, $P[h_i \mid c \cdot b] / P[h_j \mid c \cdot b]$ for all $h_j$ in $\{h_1, h_2, \ldots, h_k\}$ and all $h_i$ in $\{h_{k+1}, h_{k+2}, \ldots, h_z\}$. That is, for whichever $h_j$ in $\{h_1, h_2, \ldots, h_k\}$ has the smallest value of $P[h_j \mid c \cdot b]$, and for whichever $h_i$ in $\{h_{k+1}, h_{k+2}, \ldots, h_z\}$ has the largest value of $P[h_i \mid c \cdot b]$, let $K$ be a real number that is large enough that $K \ge P[h_i \mid c \cdot b] / P[h_j \mid c \cdot b]$.

Then, $$ \Omega[\neg (h_1 \vee \ldots \vee h_k) \mid c \cdot e \cdot b] \; \; \le \; \; K \times \left[\frac{1}{\frac{\sum_{j = 1}^k P[e \; \mid \; h_j \cdot c \cdot b]}{\sum_{i = 1}^z P[e \; \mid \; h_i \cdot c \cdot b]}} - 1 \right]. $$

Thus, a lower bound on the associated posterior probability of $(h_1 \vee \ldots \vee h_k)$ is given by the formula $$ P[(h_1 \vee \ldots \vee h_k) \mid c \cdot e \cdot b] \; \; \ge \; \; \frac{1}{1 + K \times \left[\frac{1}{\frac{\sum_{j = 1}^k P[e \; \mid \; h_j \cdot c \cdot b]}{\sum_{i = 1}^z P[e \; \mid \; h_i \cdot c \cdot b]}} - 1 \right]}. $$

A few points about this rule are worth noting. First, notice that the term $\sum_{j = 1}^k P[e \mid h_j \cdot c \cdot b] / \sum_{i = 1}^z P[e \mid h_i \cdot c \cdot b]$ is the ratio of the sum of the first $k$ likelihoods to the sum of all the likelihoods for hypotheses in $H$. So, although this rule applies to any collection $H$ consisting of $z$ alternative hypotheses, it is most usefully applied when each hypothesis $h_j$ contained in the disjunction $(h_1 \vee h_2 \vee \ldots \vee h_k)$ has a greater likelihood value, $P[e \mid h_j \cdot c \cdot b]$, than any of the other hypotheses in $H$. This is usually the most interesting case in which a lower bound on the posterior probability, $P[(h_1 \vee \ldots \vee h_k) \mid c \cdot e \cdot b]$, is assessed. For, when these $k$ likelihoods yield a sum much greater than likelihoods for the other hypotheses in $H$, then this ratio term may approach 1, which in turn drives the lower bound on the posterior probability, $P[(h_1 \vee \ldots \vee h_k) \mid c \cdot e \cdot b]$, close to 1. We will see how this can happen in an example in Section 2.4.

Notice that when all the prior probabilities are equal, the value of $K$ will be 1. In that case the final formula can be replaced by the equality, $$ P[(h_1 \vee \ldots \vee h_k) \mid c \cdot e \cdot b] \; \; = \; \; \frac{\sum_{j = 1}^k P[e \mid h_j \cdot c \cdot b]}{\sum_{i = 1}^z P[e \mid h_i \cdot c \cdot b]}. $$

When each of the prior probabilities for the first $k$ hypotheses is at least as large as any of the prior probabilities for the remaining $z-k$ hypotheses, the value of $K$ must be less than or equal to 1. In that case, the following version of the final formula holds: $$\begin{align} P[(h_1 \vee \ldots \vee h_k) \mid c \cdot e \cdot b] &\ge \frac{1}{1 + K \times \left[\frac{1}{\frac{\sum_{j = 1}^k P[e \; \mid \; h_j \cdot c \cdot b]}{\sum_{i = 1}^z P[e \; \mid \; h_i \cdot c \cdot b]}} - 1 \right]} \\ &\ge \frac{\sum_{j = 1}^k P[e \mid h_j \cdot c \cdot b]}{\sum_{i = 1}^z P[e \mid h_i \cdot c \cdot b]}. \end{align}$$

Derivations of the two Bayesian Estimation Rules, *Rule BE-D*, and *Rule BE-C* (which will be described in the next subsection) are provided in the following appendix: [Derivations of the Two Bayesian Estimation Rules, *Rule BE-D* and *Rule BE-C*.](logic-inductive.appendix3.md)

#### 1.6.2 Inference Rule *BE-C*: Bayesian Estimation for a Continuous Range of Alternative Hypotheses

A rule similar to *BE-D* applies to a continuous range of competing hypotheses. For example, the claim that “the chance *r* of *heads* on tosses of this coin lies between .63 and point .81” consists of a continuous (disjunctive) interval of competing hypotheses. So,the statement of the following rule closely parallels the statement of *Rule BE-D*. An example of its application is provided in Section 2.5.

**Rule BE-C: Bayesian Estimation for a Continuous Range of Alternative Hypotheses**

Let $H$ be a continuous region of alternative hypotheses $h_q$, where $q$ is a real number, and where the conjunction of any two of these hypotheses is logically inconsistent. Let $c$ be observational or experimental conditions for which $e$ describes one of the possible outcomes. And suppose $b$ is a conjunction of relevant auxiliary hypotheses and plausibility considerations. For each point hypothesis $h_q$ in $H$, we take $p[e \mid h_q \cdot c \cdot b]$ to be an appropriate likelihood.

Let $p[h_q \mid c \cdot b]$ and $p[h_q \mid c \cdot e \cdot b]$ be probability density functions on $H$, where these two density functions are related as follows: $$p[h_q \mid c \cdot e \cdot b] \times P[e \mid c \cdot b] \;=\; p[e \mid h_q \cdot c \cdot b] \times p[h_q \mid c \cdot b].$$

We suppose throughout that prior probability density $p[h_q \mid c \cdot b] > 0$ for all values of $q$.

The prior probability that the true point hypothesis $h_r$ lies within measurable region $R$ is given by

$P[h_R \mid c \cdot b] \; = \; \int_R p[h_r \mid c \cdot b] \; dr,\;\;$ where $\; P[h_H \mid c \cdot b] \; = \; \int_H p[h_q \mid c \cdot b] \; dq \: =\: 1$.

The posterior probability that the true point hypothesis $h_r$ lies within measurable region $R$ is given by

$P[h_R \mid c \cdot e \cdot b] \; = \; \int_R p[h_r \mid c \cdot e \cdot b] \; dr, \;\;$ where $\;P[h_H \mid c \cdot e \cdot b] \; = \; \int_H p[h_q \mid c \cdot e \cdot b] \; dq \: =\: 1$.

Then, the posterior probability satisfies the following equation for each measurable region $R$: $$\begin{align} P[h_R \mid c \cdot e \cdot b] &= \frac{\int_R p[e \mid h_r \cdot c \cdot b] \times p[h_r \mid c \cdot b] \; \; dr}{\int_H p[e \mid h_q \cdot c \cdot b] \times p[h_q \mid c \cdot b] \; \; dq}. \end{align}$$

In cases where a precise model of the prior probability density, $p[h_q \mid c \cdot b]$, is available, this equation suffices to provide values for the posterior probabilities, $P[h_R \mid c \cdot e \cdot b]$. However, when no precise model of the priors is available, bounds on the values of posterior probabilities may be evaluated in the following way.

Let $K$ be (your best estimate of) an upper bound on the ratios of the probability density values, $p[h_q \mid c \cdot b] / p[h_r \mid c \cdot b]$, for each $h_r$ in region $R$ and $h_q$ in $(H-R)$. That is, for whichever $h_r$ in $R$ has the smallest value of $p[h_r \mid c \cdot b]$, and for whichever $h_q$ in $(H-R)$ has the largest value of $p[h_q \mid c \cdot b]$, let $K$ be a real number such that $K \ge p[h_q \mid c \cdot b] / p[h_r \mid c \cdot b]$.

Then, $$\begin{align} \Omega[\neg h_R \mid c \cdot e \cdot b] & \; \le \; K \times \left[\frac{1}{\frac{\int_{R} \; p[e \:\mid\; h_r \cdot c \cdot b] \; \; dr}{\int_{H} \; p[e \;\mid\; h_q \cdot c \cdot b] \; \; dq}} - 1 \right]. \end{align}$$ Thus, a lower bound on the associated posterior probability of $h_R$ is given by the formula $$ P[h_R \mid c \cdot e \cdot b] \; \; \ge \; \; \frac{1}{1 + K \times \left[\frac{1}{\frac{\int_{R} \; p[e \;\mid\; h_r \cdot c \cdot b] \; \; dr}{\int_{H} \; p[e \;\mid\; h_q \cdot c \cdot b] \; \; dq}} - 1 \right]}. $$

In Bayesian statistics, interval hypotheses of this kind on which posterior probabilities are assessed are called *credible intervals*. The posterior probabilities of such intervals are usually calculated from prior probability distributions governed by explicitly known (or assumed) prior probability density functions. Often the assumed density function is given by $p[h_q \mid c \cdot b] = 1$ over all $h_q$ in $H$, in which case the prior is said to have a flat distribution. When the prior is flat, the value of $K=1$, and the precise value of the posterior probability for region (interval) $R$ is given by the formula, $$P[h_R \mid c \cdot e \cdot b] \; \; = \; \; \frac{\int_R p[e \mid h_q \cdot c \cdot b] \; \; dr}{\int_H p[e \mid h_q \cdot c \cdot b] \; \; dq}.$$

*Rule BE-C* is closely related to the Bayesian *Principle of Stable Estimation* (Edwards, Lindman, Savage, 1963)[^edwards-1963], but somewhat simpler and easier to apply. An example of its application is supplied in Section 2.5.

### 1.7 On the Epistemic Status of Auxiliary Hypotheses

As already noted, the logical connection between hypotheses and the evidence expressed by the *likelihoods* often requires the mediation of auxiliary hypotheses. When competing hypotheses, $h_i$ and $h_j$ draw on distinct, incompatible auxiliary hypotheses, $a_i$ and $a_j$, respectively, these auxiliaries cannot be collected into a common background claim $b$. Rather, they must be evidentially evaluated along with (in conjunction with) the hypotheses that draw on them. In that case *Rule RB* applies as follows: $$ \frac{P[(h_i \cdot a_i) \mid c \cdot e \cdot b]}{P[(h_j \cdot a_j) \mid c \cdot e \cdot b]} = \frac{P[e \mid (h_i \cdot a_i) \cdot c \cdot b]}{P[e \mid (h_j \cdot a_j) \cdot c \cdot b]} \times \frac{P[(h_i \cdot a_i) \mid c \cdot b]}{P[(h_j \cdot a_j) \mid c \cdot b]}. $$

But when two competing hypotheses draw on the same auxiliaries $a$, the logic treats them as “given” with regard to the comparative support of those hypotheses. To see how the probabilistic logic endorses this treatment, consider how *Rule RB* applies to a pair of hypotheses when each is conjoined to the same auxiliary (or conjunction of auxiliaries), $a$. First notice that *Rule RB* applies to the comparative support for $(h_i \cdot a)$ verses $(h_j \cdot a)$ as expressed above. (Here we let $d$ contain background and auxiliaries other than $a$, so that the previous background claim $b$ now consists of the conjunction ($a \cdot d)$): $$ \frac{P[(h_i \cdot a) \mid c \cdot e \cdot d]}{P[(h_j \cdot a) \mid c \cdot e \cdot d]} = \frac{P[e \mid (h_i \cdot a) \cdot c \cdot d]}{P[e \mid (h_j \cdot a) \cdot c \cdot d]} \times \frac{P[(h_i \cdot a) \mid c \cdot d]}{P[(h_j \cdot a) \mid c \cdot d]}. $$

Consider the following probabilistically valid rule — Axiom 5 of the axioms for conditional probabilities:

$$P[(A \cdot B) \mid C] = P[A \mid B \cdot C] \times P[B \mid C].$$

Applying this rule to each posterior probability in the previous ratio of posteriors yields

$$\begin{align} \frac{P[(h_i \cdot a) \mid c \cdot e \cdot d]}{P[(h_j \cdot a) \mid c \cdot e \cdot d]} &= \frac{P[h_i \mid a \cdot c \cdot e \cdot d] \times P[a \mid c \cdot e \cdot d]}{P[h_j \mid a \cdot c \cdot e \cdot d] \times P[a \mid c \cdot e \cdot d]} \\ &= \frac{P[h_i \mid c \cdot e \cdot (a \cdot d)]}{P[h_j \mid c \cdot e \cdot (a \cdot d)]} \end{align}$$

Similarly, applying this rule to each prior probability in the previous ratio of priors yields

$$ \frac{P[(h_i \cdot a) \mid c \cdot d]}{P[(h_j \cdot a) \mid c \cdot d]} = \frac{P[h_i \mid a \cdot c \cdot d] \times P[a \mid c \cdot d]}{P[h_j \mid a \cdot c \cdot d] \times P[a \mid c \cdot d]} = \frac{P[h_i \mid c \cdot (a \cdot d)]}{P[h_j \mid c \cdot (a \cdot d)]}.$$

Now, substituting these equal posterior ratios and equal prior ratios into the previous version of *RB* for $(h_i \cdot a)$ and $(h_i \cdot a)$ yields

$$ \frac{P[h_i \mid c \cdot e \cdot (a \cdot d)]}{P[h_j \mid c \cdot e \cdot (a \cdot d)]} = \frac{P[e \mid h_i \cdot c \cdot (a \cdot d)]}{P[e \mid h_j \cdot c \cdot (a \cdot d)]} \times \frac{P[h_i \mid c \cdot (a \cdot d)]}{P[h_j \mid c \cdot (a \cdot d)]}. $$

Thus, when auxiliaries $a$ are employed in common by competing hypotheses, they may be swept into a common collection of background claims $b$ (i.e., becoming $(a \cdot d)$ in this example).

As with any logic, the logic of inductive support only tells us what a given collection of premises implies about various conclusions. It may well happen that auxiliary $a$ together the body of evidence $(c \cdot e)$ implies, via likelihood ratios, that hypothesis $h_j$ is strongly supported over $h_i$, $$ \frac{P[e \mid h_i \cdot c \cdot (a \cdot d)]}{P[e \mid h_j \cdot c \cdot (a \cdot d)]} \ll 1, $$ whereas, rival auxiliary $a_r$ together with the same body of evidence may tell us, via likelihood ratios, that $h_i$ is strongly supported over $h_j$, $$ \frac{P[e \mid h_i \cdot c \cdot (a_r \cdot d)]}{P[e \mid h_j \cdot c \cdot (a_r \cdot d)]} \gg 1. $$

This ability to switch between auxiliaries to the benefit of one hypothesis over another seems epistemically dubious. Does the logic permit epistemic agents to simply employ whatever auxiliaries may best help support their own favorite hypotheses?

No, not exactly. As with any logic, only arguments that have true premises warrant their conclusions as true, or, for an inductive logic, as more or less probably true. So, if we can determine which of the alternative auxiliaries, $a$ or $a_r$, is true, then, provided the body of evidence $(c \cdot e)$ is also true, the problem would be solved. Our best assessment of which alternative hypothesis, $h_j$ or $h_i$, is most probably true should draw on premises (evidence and auxiliaries) that are themselves true. But how are we to determine which auxiliaries are true? By assessing *their* probable truth based on the body of evidence for and against *them*.

That is, the auxiliary hypotheses themselves are subject to evidence that may strongly support (the truth of) one of them over its rivals. Furthermore, this evidential support for the auxiliaries can, in turn, impact the support of hypotheses that draw on them. To see how this happens, consider again the two alternative auxiliaries (or alternative conjunctions auxiliaries) $a$ and $a_r$. Suppose that a large body of evidence, $(c^* \cdot e^*)$, bears on $a$ and its rivals, and that this body of evidence strongly supports $a$ over each of them. In particular, suppose that according to *Rule RB* this body of evidence supplies very strong support for $a$ over rival $a_r$:

$$ \frac{P[a_r \mid c^* \cdot e^* \cdot d]}{P[a \mid c^* \cdot e^* \cdot d]} = \frac{P[e^* \mid a_r \cdot c^* \cdot d]}{P[e^* \mid a \cdot c^* \cdot d]} \times \frac{P[a_r \mid c^* \cdot d]}{P[a \mid c^* \cdot d]} = \epsilon,$$

for some extremely small value of *ε*.

So, according to this body of evidence, $a$ is much more likely to be true than $a_r$. Intuitively, this provides good epistemic reason to employ $a$ rather than $a_r$ as premises in the evaluation of hypotheses $h_j$ verses $h_i$. When the evidence strongly supports one auxiliary hypothesis over an alternative, it makes good epistemic sense to draw on the most strongly supported auxiliary. Indeed, the Bayesian logic can be shown to reinforce this intuition in a sensible way. The following appendix works through the technical details of a theorem that establishes this claim.

[An Epistemic Advantage of Drawing on Well-Supported Auxiliary Hypotheses](logic-inductive.appendix4.md)

## 2. Examples

Bayesian inductive logic captures the structure of evidential support for all sorts of scientific hypotheses, ranging from simple diagnostic claims (e.g., “the patient is infected by the SARS-CoV-2 virus”) to complex scientific theories about the fundamental nature of the world, such as quantum theories and the theory of relativity. As we’ve seen, the logic is essentially comparative. The evaluation of a hypothesis depends on how strongly evidence supports it over rival hypotheses. In this section we consider several applications of this logic to the evidential evaluation of scientific hypotheses and theories.

We have seen that comparisons among the *posterior probabilities* of hypotheses depend on just two kinds of factors: (1) the *likelihoods* of evidential outcomes $e$ according to each hypothesis $h_k$, when conjoined with auxiliaries $b$ and evidential initial conditions $c$, $P[e \mid h_k\cdot c \cdot b]$; and (2) the *prior probability* of each hypotheses, $P[h_k \mid c \cdot b]$. The likelihoods capture what a hypothesis *says* about how evidential aspects of the world should turn out (if the hypothesis is true). The prior probabilities represent assessments of how plausible a hypothesis is assessed to be on grounds not captured by evidential likelihoods.

Plausibility assessments of hypotheses and theories always play an important, legitimate role in the sciences. Plausibility assessments are often backed by extensive arguments that may draw on forceful conceptual considerations together with broadly empirical claims not captured by the evidential likelihoods. Scientists often bring plausibility arguments to bear in assessing competing views. Although such arguments are usually far from decisive, they may bring the scientific community into widely shared agreement with regard to the *im*plausibility of some logically possible alternatives. This seems to be the primary epistemic role of thought experiments. Consider, for example, the kinds of plausibility arguments that have been brought to bear on the various interpretations of quantum theory (e.g., those related to the measurement problem). These arguments go to the heart of conceptual issues that were central to the original development of the theory. Many of these issues were first raised by those scientists who made the greatest contributions to the development of quantum theory, in their attempts to get a conceptual hold on the theory and its implications.

Furthermore, given any body of evidence, it is easy enough to cook up *logically possible* alternative hypotheses that completely account for the evidence. These cooked up, *ad hoc* hypotheses may be constructed so as to logically entail all the known evidence, providing likelihood values equal to 1 for the totality of the available evidence. Although most of these cooked up hypotheses will be laughably implausible, and no scientist would give them a moments notice, the evidential likelihoods are unable to rule them out. Only plausibility considerations, represented via prior probabilities, provide a place for the inductive logic to bring such *im*plausibility considerations to bear.

Among those hypotheses that are not laughably implausible, the contributions of prior plausibility assessments may be substantially “washed out” as a sufficiently strong body of evidence becomes available. Thus, provided the prior probability of a true hypothesis isn’t assessed to be too close to zero, the influence of the values of the prior probabilities will *very probably* fade away as evidence accumulates. Various Bayesian *convergence results* establish reasonable conditions for this to occur. So, it turns out that prior plausibility assessments play their most important role when the distinguishing evidence represented by the likelihoods remains weak. Some of the following examples illustrate this idea.

### 2.1. Testing Scientific Hypotheses with Statistical Evidence

Newtonian Gravitation Theory (NGT) accounts for the “falling together” of massive bodies in terms of an attractive force between them, the force of gravity produced by those massive bodies. According to the General Theory of Relativity (GTR) there is no gravitational force between bodies as such. Rather, in the vicinity of massive bodies space-time is curved. That curvature in space-time causes the distance between massive objects to decrease as they follow these curved paths through space-time. One result of this difference between GTR and NGT is that they entail different paths for beams of light that pass near the surface of the Sun on their way to Earth.

GTR entails that the light of distant stars that passes very close to the surface of the Sun is deflected from a straight-line path. This deflection will make the star, as viewed from Earth, appear to be in a slightly different location than usual with respect to background stars whose light does not pass so close to the Sun’s surface. According to GTR, the predicted angle of deflection for a beam passing near the Sun’s surface is 1.75 arcsec (where 1 arcsec is an angle of 1/3600 of a degree).

If light has gravitational mass, then Newtonian Gravitation Theory also entails that the path of a light beam near the Sun’s surface will be deflected. But the predicted gravitational deflection is only .875 arcsec, half as much as predicted by General Relativity. On the other hand, if light has no gravitational mass, NGT entails that it will not be deflected at all by gravity near the Sun’s surface.

Einstein realized these differences in the predicted paths of light by GTR vs. NGT. His publication of GTR in 1915 predicted this kind of empirical distinction between GTR and NGT. In order to test this prediction, Arthur Eddington and Andrew Crommelin lead two separate expeditions to observe the positions of stars near the edge of the Sun during a solar eclipse in 1919. Their measurements involved taking photographs of stars that appear near the Sun’s surface during the eclipse, and then measuring their apparent positions in those photographs as compared to other stars that appear further away from the Sun’s surface. The relative positions of those same stars were also photographed and measured in the night sky at another time of year, when the paths of their light was not influenced by travel near the surface of the Sun.

The hypotheses being tested by the evidence in this case are not themselves statistical in nature. However, the evidential likelihoods turn out to be probabilistic due to statistical error characteristics of the measuring devices.

The Eddington group measured a deflection of 1.61 arcsec, with an error of plus or minus .31 arcsec. The Crommelin group measured a deflection of 1.98 arcsec, with an error of plus or minus .12 arcsec. These error terms are due to inaccuracies in the measuring devices, such as irregularities in the photographic emulsions, and differences in the cameras and telescopes during the eclipse measurements as compared to the non-eclipse reference measurements of star positions at other times (e.g. due to temperature and configuration changes).

Let’s employ the following abbreviations:

**$h_G$**

the General Theory of Relativity

**$h_N$**

Newtonian Gravitation Theory together with the hypothesis that light has gravitational mass

**$h_{N_0}$**

Newtonian Gravitation Theory together with the hypothesis that light has no gravitational mass

**$c_1$**

the conditions under which the Eddington group measurements are made (type of telescope, camera, photographic plates, whether conditions, etc.), both for the eclipse measurements and for the non-eclipse reference measurements; this information includes the inferred error intervals due to the measurement conditions and the resulting states of the developed photographic plates: $\pm .31$ arcsec

**$e_1$**

the outcome of the Eddington group measurements; mean measured deflection among all stars photographed near the Sun’s rim = 1.61 arcsec

**$c_2$**

the conditions under which the Crommelin group measurements are made (type of telescope, camera, photographic plates, whether conditions, etc.), both for the eclipse measurements and for the non-eclipse reference measurements; this information includes the inferred error intervals due to the measurement conditions and the resulting states of the developed photographic plates = $\pm .12$ arcsec

**$e_2$**

the outcome of the Crommelin group measurements: mean measured deflection among all stars photographed near the Sun’s rim = 1.98 arcsec

**$b$**

includes the supposition that measurement errors of the kind involved in such measurements tend to be approximately *normally distributed* about the true value, where the *inferred measurement error* approximates the *standard deviation* of this *normal distribution*.

In cases like this, the statistical error in the measurement outcome is taken to be normally distributed around the true value of the light deflection, expressed by the hypothesis. That is, the likelihood of the evidential outcome $e$ for a hypothesis $h_j$, given $c \cdot b$, is calculated in terms of how far away, in terms of *standard deviations* for a normal distribution, the measured outcome lies from the value predicted by that hypothesis.

A well-know spreadsheet program can be used to calculate these values. It uses the following syntax to calculate the probability value due to a normal distribution for the region under the normal curve extending from the left of the curve up to point *x*, given the *mean* of the normal distribution and its standard deviation, *standard_dev*:

$$\text{NORM.DIST}(x, mean, standard\_dev, \textit{TRUE})$$ where the term $\textit{TRUE}$ tells the function to calculate the cumulative distribution up to $x$, instead of only calculating the value of the density function at $x$. Using this spreadsheet program, the probability of getting a measured outcome value between $m-v$ and $m+v$ is calculated via the following formula: $$\begin{align} &\text{NORM.DIST}(m+v, mean, standard\_dev, \textit{TRUE}) \\ &\quad - \text{NORM.DIST}(m-v, mean, standard\_dev, \textit{TRUE}). \end{align}$$

For the experiment conducted by the Eddington group, the evidence consists of a measured deflection value of 1.61, accurate to no more that two decimal places. Thus, the measurement result lies in the interval between $(1.61-.005)$ and $(1.61+.005)$. This is the evidential outcome $e_1$. Thus, the relevant evidential likelihoods may be calculated as follow:

$$\begin{align} &P[e_1 \mid h_G \cdot c_1 \cdot b]\ = \\ &\qquad \text{NORM.DIST}(1.61 + 0.005, 1.75, .31, \textit{TRUE}) \\ &\qquad\quad - \text{NORM.DIST}(1.61 - 0.005, 1.75, .31, \textit{TRUE}) \\ &~=\ 1.16 \times 10^{-2} \end{align}$$ $$\begin{align} &P[e_1 \mid h_N \cdot c_1 \cdot b] = \\ &\qquad \text{NORM.DIST}(1.61 + 0.005, .875, .31, \textit{TRUE}) \\ &\qquad\quad - \text{NORM.DIST}(1.61 - 0.005, .875, .31, \textit{TRUE}) \\ &= 7.74 \times 10^{-4} \end{align}$$ $$\begin{align} &P[e_1 \mid h_{N_0} \cdot c_1 \cdot b] = \\ &\qquad \text{NORM.DIST}(1.61 + 0.005, 0, .31, \textit{TRUE}) \\ &\qquad\quad - \text{NORM.DIST}(1.61 - 0.005, 0, .31, \textit{TRUE}) \\ &= 1.79 \times 10^{-8}. \end{align}$$

The likelihoods for the evidence from the Crommelin group, $(c_2 \cdot e_2)$, may be calculated in a similar way.

The following table provides the likelihoods due to each hypothesis for each experiment. And it provides the resulting values for the corresponding likelihood ratios.

| $e_k$ | $e_1$ | $e_2$ |
| --- | --- | --- |
| $P[e_k \mid h_G \cdot c_k \cdot b]$ | $1.16 \times 10^{-2}$ | $5.30\times 10^{-3}$ |
| $P[e_k \mid h_N \cdot c_k \cdot b]$ | $7.74 \times 10^{-4}$ | $1.29 \times 10^{-20}$ |
| $P[e_k \mid h_{N_0} \cdot c_k \cdot b]$ | $1.79 \times 10^{-8}$ | $2.53 \times 10^{-61}$ |
| $$\frac{P[e_k \mid h_N \cdot c_k \cdot b]}{P[e_k \mid h_G \cdot c_k \cdot b]}$$ | $$6.67 \times 10^{-2}$$ | $$2.43 \times 10^{-18}$$ |
| $$\frac{P[e_k \mid h_{N_0} \cdot c_k \cdot b]}{P[e_k \mid h_G \cdot c_k \cdot b]}$$ | $$1.54 \times 10^{-6}$$ | $$4.77 \times 10^{-59}$$ |
|   |   |   |
| $$\frac{P[e_k \mid h_G \cdot c_k \cdot b]}{P[e_k \mid h_N \cdot c_k \cdot b]}$$ | $$1.50 \times 10^{1}$$ | $$4.11 \times 10^{17}$$ |
| $$\frac{P[e_k \mid h_G \cdot c_k \cdot b]}{P[e_k \mid h_{N_0} \cdot c_k \cdot b]}$$ | $$6.48 \times 10^{5}$$ | $$2.09 \times 10^{58}$$ |

Table: Likelihoods and Likelihood Ratios

Clearly, $(c_1 \cdot e_1)$ provides overwhelming evidence against $h_{N_0}$ as compared to $h_G$, and strong evidence against $h_N$ as compared to $h_G$. And, $(c_2 \cdot e_2)$ also provides overwhelming evidence against both $h_{N_0}$ and $h_N$ as compared to $h_G$.

### 2.2. An Application to Medical Tests: Covid-19 Self-Tests

As an illustration of how evidential support works in a medical setting, let’s consider the kind of evidence supplied by over-the-counter COVID-19 self-tests. Let $h$ be the hypothesis that the subject of the test *has COVID-19 on the day of testing*; the alternative hypothesis, $\neg h$, says that the subject does not have COVID-19 on the day of testing. Background/auxiliary conditions $b$ state the *sensitivity* of the test (chance of a positive test result when disease is present) and the *specificity* of the test (chance of a negative test result when disease is not present). Most home-tests report *sensitivity* and *specificity* for test subjects who are already symptomatic — i.e. who already show any of the following symptoms: fever, fatigue, chills, myalgia (i.e. muscle pain), congestion, cough, loss of smell, shortness of breath, sore throat, nausea, diarrhea. In addition, a home-test is “administered appropriately” when the nasal swab is used as the test instructions specify, and the result is deposited on the supplied test strip as per instructions. For our purposes, all of this information is included in the background/auxiliary information, $b$.

Consider a home-test with the following characteristics for *symptomatic* subjects: *sensitivity* = .94, *specificity* = .98. The *sensitivity* is the *true positive rate* (the chance of a positive test result when disease is present); so the *false negative rate* (the chance of a negative test result when disease is present) for this test is .06 = (1 - *sensitivity*). The *specificity* is the *true negative rate* (the chance of a negative test result when disease is not present); so the *false positive rate* (the chance of a positive test result when disease is not present) for this test is .02 = (1 - *specificity*).

Now, let’s suppose that an individual subject is tested. Condition $c$ says that this subject is *symptomatic* and that the test is administered to the subject in the appropriate way (as specified in the instructions for the test). Let $e$ say that the *test result is positive* (i.e. the test shows that a significant amount of the target antigen of the SARS-CoV-2 virus is detected); and let $\neg e$ say that the *test result is negative* (i.e. the test shows that no significant amount of the target antigen of the SARS-CoV-2 virus is detected). What the test subject wants to know is the value of the posterior probabilities, $P[h \mid c\cdot e \cdot b]$ and $P[h \mid c \cdot \neg e\cdot b]$, that the subject has COVID-19, given the evidence of the positive result, $(c\cdot e)$, or the negative test result, $(c\cdot \neg e)$, taken together with the error rates of these tests as described in $b$.

The values of these posterior probabilities depend on the following likelihoods, which come from applying the *sensitivity* and *specificity* statistics for the test to this individual test subject:

$$P[e \mid h \cdot c \cdot b] = .94, \text{ due to the }\textit{sensitivity}, $$ $$P[\neg e \mid \neg h \cdot c \cdot b] = .98, \text{ due to the }\textit{specificity}.$$

As a result, we also have the following values:

$$(P[\neg e \mid h \cdot c \cdot b] = .06, \text{ for the }\textit{false negative rate}, $$ $$P[e \mid \neg h \cdot c \cdot b] = .02, \text{ for the }\textit{false positive rate}. $$

This provides the following likelihood ratios against disease (against $h$) for this test subject when the test result is positive, or negative, respectively: $$\frac{P[e \mid \neg h\cdot c\cdot b]}{P[e \mid h \cdot c\cdot b]} = .02/.94 = .0213$$ $$\frac{P[\neg e \mid \neg h\cdot c\cdot b]}{P[\neg e \mid h\cdot c\cdot b]} = .98/.06 = 16.34.$$

The value of the posterior probability that the subject has COVID-19, given the evidence, depends on how plausible it is that the patient has COVID-19 on the day of the test prior to taking the test results into account, $P[h \mid c \cdot b]$. In the context of medical diagnosis, this prior probability is usually assessed on the basis of the *base rate* for the disease in the patient’s risk group. Such information may be stated within the background information $b$. *Rule OB* shows how to calculate the posterior probabilities from these values.

$$\begin{align} &\Omega[\neg h \mid c \cdot e \cdot b \cdot (h \vee \neg h)] = \frac{P[\neg h \mid c \cdot e \cdot b]}{P[h \mid c \cdot e \cdot b]} \\ &\qquad = \frac{P[e \mid \neg h \cdot c \cdot b]}{P[e \mid h \cdot c \cdot b]} \times \frac{P[\neg h \mid c \cdot b]}{P[h \mid c \cdot b]}. \end{align}$$ $$\begin{align} P[h \mid c \cdot e \cdot b] &= P[h \mid c \cdot e \cdot b \cdot (h \vee \neg h)] \\ &= \frac{1}{1 + \Omega[\neg h \mid c \cdot e \cdot b \cdot (h \vee \neg h)]}. \end{align}$$

And similarly for $P[h \mid c \cdot \neg e \cdot b]$.

The table below shows how these posterior probabilities depend on the values of prior probabilities. The columns under “Test Brand 1” shows the posterior probabilities for the test described above, the test that has *sensitivity* = .94 and *specificity* = .98. The columns under “Test Brand 2” shows the posterior probabilities for a different, lower sensitivity test, a test that has *sensitivity* = .84 and *specificity* = .98.

|   | Test Brand 1 Sensitivity = .94 Specificity = .98 | Test Brand 2 Sensitivity = .84 Specificity = .98 |   |   |
| --- | --- | --- | --- | --- |
| $P[h \mid c \cdot b]$ | $P[h \mid c \cdot e \cdot b]$ | $P[h \mid c \cdot \neg e \cdot b]$ | $P[h \mid c \cdot e \cdot b]$ | $P[h \mid c \cdot \neg e \cdot b]$ |
| .01 | .322 | .001 | .298 | .002 |
| .02 | .490 | .001 | .462 | .003 |
| .03 | .592 | .002 | .565 | .005 |
| .04 | .662 | .003 | .636 | .007 |
| .05 | .712 | .003 | .689 | .009 |
| .06 | .750 | .004 | .728 | .010 |
| .07 | .780 | .005 | .760 | .012 |
| .08 | .803 | .005 | .785 | .014 |
| .09 | .823 | .006 | .806 | .016 |
| .10 | .839 | .007 | .824 | .018 |
| .20 | .922 | .015 | .913 | .039 |
| .30 | .953 | .026 | .947 | .065 |
| .40 | .969 | .039 | .966 | .098 |
| .50 | .979 | .058 | .977 | .140 |
| .60 | .986 | .084 | .984 | .197 |
| .70 | .991 | .125 | .990 | .276 |
| .80 | .995 | .197 | .994 | .395 |
| .90 | .998 | .355 | .997 | .595 |

Table: Posterior Probabilities for COVID-19 Home Test Results $h$ = *disease present*    $e$ = *test result positive*

When the precise values of the prior probabilities are unknown, but a reasonable range can be estimated, a resulting range of posterior probabilities may be calculated. Suppose we can be confident that the base-rate for COVID-19 among symptomatic members of the relevant population for the test subject is between .05 and .09. Then, when the subject is tested with Test Brand 1, the posterior probability that the subject has COVID-19, given a positive result is, according to the table, $.713 \le P[h \mid c\cdot e \cdot b] \le .823$. And the posterior probability that the subject has COVID-19, given a negative result, is $.003 \le P[h \mid c \cdot \neg e \cdot b] \le .006$.

### 2.3. When Likelihoods are Vague or Imprecise: Evidence for Continental Drift.

In many contexts the values of likelihoods may be vague or imprecise. Nevertheless, the evidence may still be capable of strongly supporting one hypothesis over another in a reasonably objective way. Here is an example.

Consider the following simple version of the continental drift hypothesis. $h_2$: The land masses of Africa and South America were once joined, then split apart and have drifted to there current positions on Earth over the eons. Let’s compare this hypothesis to the older *contractionist* theory: $h_1$: The continents have fixed positions on Earth, which they acquired when the Earth first formed, cooled, and contracted into its present configuration.

The evidence available for the drift hypothesis over the contractionist hypothesis during the first half of the 20ᵗʰ century included the following observations: (1) Upon careful examination, the east coast of South America fits the shape of the west coast of Africa extremely well. (2) When the coasts of South America and Africa are aligned as closely as possible, and the geology of the two continents is carefully examined, a number of geologic features align across the two continents (e.g. the Ghana mountain ranges align with mountain ranges in Brazil; the rock strata of the Karroo system of South Africa matches precisely with the Santa Catarina system in Brazil; etc.). (3) When the fossil record on both continents is carefully examined, a number fossils of identical species have been discovered to have lived at the same time on both continents (e.g. Mesosaurus (land reptile, 286-258 million yrs. ago), Cynognathus (fresh water reptile 250-240 million yrs. ago), Glossopteris (tree-sized fern, 299 million yrs. ago)); and none of these species could have crossed the Atlantic Ocean under their own power.

Let $c$ represent the conjunction of all the specific methods used to collect the above evidence, and let $e$ represent a detailed description of the precise results of all these investigations. (Here $b$ expresses relevant scientific background knowledge, including the relevant knowledge of geology and evolutionary biology.) Consider the evidential likelihoods, $P[e \mid h_1 \cdot c \cdot b]$ and $P[e \mid h_2 \cdot c \cdot b]$. Although experts may be unable to specify anything like precise numerical values for these likelihoods, experts may readily agree that each of the above cited evidential observations is much more likely on the drift hypothesis than on the contraction hypothesis, and that they jointly constitute extremely strong evidence in favor of *drift* over *contraction*. On a Bayesian analysis this is due to the fact that, although these likelihoods do not have precise values, it is obvious to experts that the ratio of the likelihoods is pretty extreme, strongly favoring drift over contraction. That is,

> $P[e \mid h_2 \cdot c \cdot b] / P[e \mid h_1 \cdot c \cdot b]$ is very large, and its inverse, $P[e \mid h_1 \cdot c \cdot b] / P[e \mid h_2 \cdot c \cdot b]$, is very nearly zero.

Thus, according to the Ratio Form of Bayes’ Theorem,

$$P[h_1 \mid c \cdot e \cdot b] \; \lt \; P[h_1 \mid c \cdot e \cdot b] / P[h_2 \mid c \cdot e \cdot b]$$

should be very close to 0, strongly supporting $h_2$ over $h_1$, *unless* the *drift* hypothesis is taken to be extremely implausible as compared to *contraction* on other grounds — i.e. unless $P[h_1 \mid c \cdot b] / P[h_2 \mid c \cdot b]$ is extremely large due to other information (which may be listed within $b$).

Historically, the evidence described above was well-known during the first half of the 20ᵗʰ century. Nevertheless, most geologists largely dismissed the *drift* hypothesis until the 1960s. Apparently the strength of this evidence did not suffice to overcome non-evidential (though broadly empirical) considerations that made the drift hypothesis seem much less plausible than the traditional *contractionist* view. The chief difficulty was the apparent absence of a plausible mechanism for moving continents across the ocean floor. This difficulty was overcome when a plausible enough convection mechanism was articulated, and evidence favoring it was acquired.

### 2.4. Bayesian Estimation for Disjunctions of Discrete Statistical Hypotheses

We now turn to an example application of *Rule BE-D*.

Let ‘*B*’ represent the collection of all households in the United States during July, 2020. Let ‘*A*’ represent those households among them in which one or more dogs reside. What proportion of the *B*s are *A*s? Symbolically, for real number $r$ between 0 and 1, let $F(A,B)= r$ say that the frequency (i.e. proportion) of $A$s among $B$s is $r$. So, we want to know, for what value of $r$ does $F(A,B)= r$ hold. Given that the number of households in the United States during July of 2020 was a little under $z$ = 129 million (stated within the background and auxiliaries, $b$), there are in principle that many alternative hypotheses: $F(A,B)=k/z$ for each integer $k$ between 0 and 129 million.

Suppose a sample *S* consisting of $n = 400$ of these households is randomly drawn from *B* (households present in the United States during July 20, 2020) with respect to whether or not they are *A* (households with dogs). This is the experimental condition, $c$. And suppose that within sample *S*, $m = 248$ households report being in *A* (having one or more dogs in residence). So, $F(A,S)= m/n = 248/400=.62$. This is the evidence $e$.

The posterior probability of any specific hypothesis, $P[F(A,B)=k/z \mid c \cdot F[A,S]=248/400 \cdot b]$, will be extremely small, even for $F(A,B)=248/400=.62$. And in any case, we shouldn’t expect the value of $F[A,B]$ to be exactly the value of $F(A,S)$. Rather, what we may reasonably hope to determine is that some interval of values below and above the sample value .62 has a fairly high probability: e.g. $$P[.57 \le F(A,B) \le .67 \mid c \cdot F(A,S)=248/400 \cdot b] \ge .95.$$ We will see how to determine such posterior probabilities via *Rule BE-D*.

Before proceeding, let’s settle on a few convenient notational conventions. To facilitate the statement of rule *BE-D* we pulled a particular list of hypotheses to the front of the queue, and listed them as $h_1$ through $h_k$. In the present example we diverge from this way of labeling hypotheses. Instead, we employ a notation that is more natural for the present example. We let each hypothesis in the set of alternatives $H$ take the form $F(A,B)=r_k$, where $k$ now ranges from 0 through $z$, and where we now define each $r_k$ to abbreviate proportion $k/z$ of the population $B$. Furthermore, the main disjunction of hypotheses of interest now consists of those frequencies within some interval $[v,u]$ centered around the sample frequency $F(A,S)=m/n$. Thus, the expression $v \le F[A,B] \le u$ (for some specific values of $v$ and $u$) represents the disjunction of hypotheses, $(F[A,B]=v \;\vee \ldots $ $\vee\; F[A,B]=m/n \;\vee \ldots $ $\vee\; F[A,B]=u)$, whose posterior probability we want to evaluate.

When a hypothesis states that the proportion of $A$s among $B$s is $r_k$, the associated likelihood of drawing a sample proportion $F(A,S)=m/n$ is given by the binomial distribution formula:

$$\begin{align} &P[F(A,S)=m/n \mid c \cdot F(A,B)=r_k \cdot b] \\ &\qquad = \frac{n!}{m!(n-m)!}\; r_k^m\; (1-r_k)^{n-m}. \end{align}$$

Now, we apply the Bayesian Estimation rule *BE-D* as follows:

$$\begin{align} &P[v \le F[A,B] \le q \mid c \cdot F[A,S]=m/n \cdot b] \\ &\qquad \ge \frac{1}{1 + K \times \left[\frac{1}{\frac{\sum_{j = v\cdot z}^{u\cdot z} P[e \; \mid \; h_j \cdot c \cdot b]}{\sum_{i = 1}^z P[e \; \mid \; h_i \cdot c \cdot b]}} - 1 \right]}, \end{align}$$

where the ratio of sums in the denominator is given by the formula, $$\frac{\sum_{j = v\cdot z}^{u\cdot z} P[e \mid h_j \cdot c \cdot b]}{\sum_{i = 1}^z P[e \mid h_i \cdot c \cdot b]} \; = \; \frac{\sum_{j = v\cdot z}^{u\cdot z}\; r_j^m\; (1-r_j)^{n-m}}{\sum_{i = 1}^z\; r_i^m\; (1-r_i)^{n-m}},$$ where $(v\cdot z)$ and $(u\cdot z)$ are the appropriate integers for the endpoints of the interval $[v, u]$ (i.e. $(v\cdot z) /z = v$ and $(u\cdot z)/z = u$).

These large sums of binomial factors are difficult to calculate directly. Fortunately, they are closely approximated by a more easily calculable formula, that for the normalized Beta distribution. That is,

$$\begin{align} \frac{\sum_{j = v\cdot z}^{u\cdot z}\; r_j^m\; (1-r_j)^{n-m}}{\sum_{i = 1}^z\; s_i^k\; (1-s_i)^{n-m}} \; &\approxeq \; Beta[v,u \;:\; m+1,\; (n-m)+1] \\ &=\; \frac{\int_{v}^u r^{m} (1-r)^{n-m} \; dr}{\int_{0}^1 s^m (1-s)^{n-m} \; ds}. \end{align}$$

The values of this normalized Beta-distribution function may easily be computed using well-know mathematics and spreadsheet programs. For example, the version of this function supplied by one such spreadsheet program takes the form BETA.DIST($x$, *α*, *β*, TRUE). It computes the value of the normalized beta distribution from 0 up to to $x$, where for our purposes $\alpha = m+1$, $\beta = (n-m) +1$. The input value TRUE tells the program to calculate the integral from 0 to $x$ (whereas FALSE would tell the program to calculate the value of the density function at point $x$). Using this spreadsheet version of the function, we calculate the value of the normalized Beta-distribution between $v$ and $u$ by inputing the following formula:

$$\begin{align} \tag{$BD$} &\text{BETA.DIST}[u,\; m+1,\; (n-m)+1,\; \textit{TRUE}] \\ &\quad - \text{BETA.DIST}[v,\; m+1,\; (n-m)+1,\; \textit{TRUE}]. \end{align}$$

For simplicity, we refer to the above formula as $BD(u,v,m,n)$. So, to have the spreadsheet program compute a lower bound on the value of $P[v\le F[A,B]\le u \mid c \cdot F[A,S]=m/n \cdot b]$ for specific values of $m$, $n$, $v$, and $u$, we need only input this formula with those values, together with a value for the upper bound $K$ on ratios of prior probabities:

$$ \frac{1}{1 + K\times\left(\frac{1}{ BD(u,v,m,n)} - 1\right)} $$

In many real cases it will be at least as initially plausible that the true frequency value lies within of the *region of interest* between *v* and *u* as that it lies outside that that region. In such cases the value of *K* must be less than or equal to 1. However, even when the upper bound *K* on the ratio of these priors is quite large, any moderately large sample size *n* will drive the posterior probability $P[v \le F[A,B] \le q \mid c \cdot F[A,S]=m/n \cdot b]$ close to 1, for fairly narrow bounds *v* and *u*. The following table, calculated via the Beta-distribution, illustrates this for both

$$P[F(A,B)=.62\pm .05\mid c \cdot F(A,S)=m/n=.62 \cdot b]$$

and

$$P[F(A,B)=.62\pm .025\mid c \cdot F(A,S)=m/n=.62 \cdot b]$$

over a range of different samples sizes $n$, and over a wide range of values of $K$.

| Size of sample *S* from *B* $= n$, Number of *A*s in sample *S* $= m$: $m/n = .62$ throughout table |   | Where $\frac{P[F(A,B)=s \mid c \cdot b]}{P[F(A,B)=r \mid c \cdot b]} \: \le \: K$ for all $r$, $s$ such that $.62-q \le r \le .62+q$ *and* either $s \lt .62-q$ or $s \gt .62+q$, $P[F(A,B)=.62\pm q\mid c \cdot F(A,S)=m/n \cdot b] \;\; \ge$ |   |   |   |   |   |   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Prior Ratio *K* $\downarrow$ | *n* $\rightarrow$ (*m*) $\rightarrow$ |   | 400 (248) | 800 (496) | 1600 (992) | 3200 (1984) | 6400 (3968) | 12800 (7936) |
|   |   |   |   |   |   |   |   |   |
| 1 | *q* = .05 $\rightarrow$ *q* = .025 $\rightarrow$ |   | 0.9614 0.6982 | 0.9965 0.8554 | 1.0000 0.9608 | 1.0000 0.9964 | 1.0000 1.0000 | 1.0000 1.0000 |
| 2 | *q* = .05 $\rightarrow$ *q* = .025 $\rightarrow$ |   | 0.9256 0.5364 | 0.9930 0.7474 | 0.9999 0.9246 | 1.0000 0.9929 | 1.0000 0.9999 | 1.0000 1.0000 |
| 5 | *q* = .05 $\rightarrow$ *q* = .025 $\rightarrow$ |   | 0.8327 0.3163 | 0.9827 0.5420 | 0.9998 0.8306 | 1.0000 0.9825 | 1.0000 0.9998 | 1.0000 1.0000 |
| 10 | *q* = .05 $\rightarrow$ *q* =.025 $\rightarrow$ |   | 0.7133 0.1879 | 0.9661 0.3717 | 0.9996 0.7103 | 1.0000 0.9656 | 1.0000 0.9996 | 1.0000 1.0000 |
| 100 | *q* = .05 $\rightarrow$ *q* = .025 $\rightarrow$ |   | 0.1992 0.0226 | 0.7402 0.0559 | 0.9963 0.1969 | 1.0000 0.7371 | 1.0000 0.9962 | 1.0000 1.0000 |
| 1,000 | *q* = .05 $\rightarrow$ *q* = .025 $\rightarrow$ |   | 0.0243 0.0023 | 0.2217 0.0059 | 0.9639 0.0239 | 1.0000 0.2190 | 1.0000 0.9637 | 1.0000 1.0000 |
| 10,000 | *q* = .05 $\rightarrow$ *q* = .025 $\rightarrow$ |   | 0.0025 0.0002 | 0.0277 0.0006 | 0.7277 0.0024 | 0.9999 0.0273 | 1.0000 0.7261 | 1.0000 0.9999 |
| 100,000 | *q* = .05 $\rightarrow$ *q* = .025 $\rightarrow$ |   | 0.0002 0.0000 | 0.0028 0.0001 | 0.2109 0.0002 | 0.9994 0.0028 | 1.0000 0.2096 | 1.0000 0.9994 |
| 1,000,000 | *q* = .05 $\rightarrow$ *q* = .025 $\rightarrow$ |   | 0.0000 0.0000 | 0.0003 0.0000 | 0.0260 0.0000 | 0.9940 0.0003 | 1.0000 0.0258 | 1.0000 0.9943 |
| 10,000,000 | *q* = .05 $\rightarrow$ *q* = .025 $\rightarrow$ |   | 0.0000 0.0000 | 0.0000 0.0000 | 0.0027 0.0000 | 0.9433 0.0000 | 1.0000 0.0026 | 1.0000 0.9457 |

Table: Lower Bounds on Posterior Probability $P[F(A,B)=.62\pm q\mid c \cdot F(A,S)=m/n=.62 \cdot b]$, for Sample *S* of Size *n* Randomly Drawn from *B*.

All probability entries in this table are accurate to four decimal places. Those entries of form ‘1.0000’ actually represent probability values that are a tiny bit less than 1.0000.

Notice that even when the bound of ratios of prior probabilities, $K$, is extremely large, a sufficiently large sample size overcomes this disparity between prior probabilities. To illustrate the point, let’s focus on those hypotheses that lie in the interval $F(A,B)=.62\pm .025$ (i.e. the interval $.595 \le F(A,B) \le .645$). In this context K is an an upper bound on the ratios of all the prior probabilities, $$K \;\ge\; P[F(A,B)=r_i \mid c \cdot b] / P[F(A,B)=r_j \mid c \cdot b],$$ such that $r_j$ lies within the interval $.62\pm .025$ and $r_i$ lies outside the interval $.62\pm .025$. For $K = 1,000$ this means that some of the specific frequency hypotheses $F(A,B)=k/z$ outside this interval (i.e. some hypotheses that either have $k/z \lt .62-.025$ or have $k/z \gt .62+.025$) may have prior probabilities *up to* 1000 times larger than the priors of specific hypotheses within this interval. But no specific hypotheses outside the interval has a prior *more than* 1000 times larger than any hypothesis inside the interval. The table shows that even when the upper bound on these ratios of priors is this extreme, a large enough sample size, $n = 6400$, results in a reasonably good lower bound on the posterior probability: $$P[F(A,B)=.62\pm .025\mid c \cdot F(A,S)=3968/6400 \cdot b] \; \ge \; .9637.$$ And even for a really extreme value of this ratio of priors, $K = 10,000,000$, a sample size of $n = 12800$ results in a decent lower bound on the posterior: $$P[F(A,B)=.62\pm .025\mid c \cdot F(A,S)=7936/12800 \cdot b] \; \ge \; .9457.$$

### 2.5. Bayesian Estimation for a Continuous Range of Alternative Hypotheses

Let’s consider a simple example of a statistical hypothesis about a collection of independent evidential outcomes. Suppose we possess a warped coin and want to determine its propensity for turning up *heads* when tossed in a standard unbiased way. Consider two hypotheses, $h_{q}$ and $h_{r}$, which say that the chances (or propensities) for the coin to come up *heads* when tossed are $q$ and $r$, respectively. Let $c$ report that the coin is tossed $n$ times in the normal way, and let $e$ say that precisely $m$ occurrences of *heads* result. Supposing that the outcomes of such tosses are probabilistically independent (asserted by $b$). So, the respective likelihoods take the usually binomial form $$ P[e \mid h_{r}\cdot c \cdot b] = \frac{n!}{m! \times(n-m)!} \times r^m (1-r)^{n-m}, $$

Then, *Rule RB* yields the following formula, where the likelihood ratio is the ratio of the respective binomial terms:

$$ \frac{P[h_{q} \mid c\cdot e \cdot b]} {P[h_{r} \mid c\cdot e \cdot b]} = \frac{q^m (1-q)^{n-m}} {r^m (1-r)^{n-m}} \times \frac{P[h_{q} \mid c \cdot b]} {P[h_{r} \mid c \cdot b]} $$

When, for instance, the coin is tossed $n = 100$ times and comes up *heads* $m = 72$ times, the evidence for hypothesis $h_{1/2}$ as compared to $h_{3/4}$ is given by the likelihood ratio

$$\frac{P [e \mid h_{1/2}\cdot c \cdot b]} {P [e \mid h_{3/4}\cdot c \cdot b]} = \frac{[(1/2)^{72}(1/2)^{28}]}{[(3/4)^{72}(1/4)^{28}]} = .000056269. $$

Such evidence *strongly refutes* the $h_{1/2}$ (*fair-coin*) hypothesis with respect to the $h_{3/4}$ (*bias-coin* towards 3/4-*heads*) hypothesis, provided that the assessment of prior plausibilities for these two hypotheses doesn’t make the latter hypothesis *too extremely implausible* to begin with. In this case, provided that $h_{1/2}$ is initially no more that 100 times more plausible than the $h_{3/4}$ — i.e. provided that $P[h_{1/2} \mid b] / P[h_{3/4} \mid b] \le 100$ — the resulting ratio of posterior probabilities must be less than or equal to .0056269: $$ \frac{P[h_{1/2} \mid c^{n}\cdot e^{n} \cdot b]} {P[h_{3/4} \mid c^{n}\cdot e^{n} \cdot b]} \le .000056269 \times 100 = .0056269 $$ Notice, however, that this *strong refutation* of $h_{1/2}$ is not *absolute refutation*. Additional evidence could reverse the total proportion of *heads* outcomes that favor it.

In cases like this, where all the competing hypotheses lie within a continuous region, the Bayesian Estimation Rule *BE-C* provides another useful way to assess the evidential support for hypotheses. In the coin-tossing case, the relevant region of alternative hypotheses $H$ is the class of all hypotheses of form $h_{r}$, where each such hypothesis says that the chance of *heads* on each coin-toss is $r$. So, when $c$ says the coin is tossed $n$ times, and e says these tosses produce precisely $m$ occurrences of *heads* (and $b$ says the tosses are independent and identically distributed), the individual likelihoods continue to take the binomial form: $$P[e \mid h_{r} \cdot c \cdot b] = \frac{n!}{m! \times(n-m)!} \times r^m (1-r)^{n-m}.$$

Let $h[v,u]$ express the hypothesis that the propensity for tosses to land *heads* is some real number in the interval between $v$ and $u$. Then, applying *Rule BE-C* to this problem, our goal is to evaluate posterior probabilities of form $$\begin{align} P[h[v,u] \mid c \cdot e \cdot b] &= \int_v^u p[h_q \mid c \cdot e \cdot b] \; \; dq \\ &\ge \frac{1}{1 + K \times \left[\frac{1}{\frac{\int_v^u r^m (1-r)^{n-m} \; \; dr}{\int_0^1 q^m (1-q)^{n-m} \; \; dq}} - 1 \right]}, \end{align}$$ where K is an an upper bound on the ratios of values of the prior probability density functions, $$K \;\ge\; p[h_q \mid c \cdot b] / p[h_r \mid c \cdot b],$$ when $r$ lies within the interval between $v$ and $u$, and $q$ lies outside this interval.

It turns out that the ratio $\frac{\int_v^u r^m (1-r)^{n-m} \; \; dr}{\int_0^1 q^m (1-q)^{n-m} \; \; dq}$ in this equation is the very definition of the normalized Beta-distribution function (discussed earlier) applied to $m$ positive outcomes in $n$ trials. We can employ a well-known spreadsheet application to calculate values of the normalized Beta-distribution between specific values of *v* and *u*, using the previously-defined formula $BD(u,v,m,n)$.

Thus, we have the following formula for the lower bound on the posterior probability that the propensity for *heads* lies within an interval between bounds $v$ and $u$.

$$P[h[v,u] \mid c \cdot e \cdot b] \; \; \ge \frac{1}{1 + K\times\left(\frac{1}{BD(u,v,m,n)}\right)}. $$

Here are a few examples calculated via this formula. In each case, the values of $v$ and $u$ have been chosen to lie equal distances below and above .72, which we assume to be the proportion found in the sample, $m/n = .72$. Each of the following posterior probabilities draws on specified values of m and n, and a specified value for $K$.

| $K$ | $n$ | $m$ | *posterior probabilities* |
| --- | --- | --- | --- |
| 1 | 100 | 72 | $P[h[.63,.81] \mid c \cdot e \cdot b] \; \; \gt .956$ $P[h[.60,.84] \mid c \cdot e \cdot b] \; \; \gt .992$ |
| 10 | 100 | 72 | $P[h[.59,.85] \mid c \cdot e \cdot b] \; \; \gt .959$ $P[h[.56,.88] \mid c \cdot e \cdot b] \; \; \gt .994$ |
| 100 | 100 | 72 | $P[h[.56,.88] \mid c \cdot e \cdot b] \; \; \gt .946$ $P[h[.53,.91] \mid c \cdot e \cdot b] \; \; \gt .994$ |
| 1 | 1000 | 720 | $P[h[.69,.75] \mid c \cdot e \cdot b] \; \; \gt .965$ $P[h[.68,.76] \mid c \cdot e \cdot b] \; \; \gt .995$ |
| 10 | 1000 | 720 | $P[h[.68,.76] \mid c \cdot e \cdot b] \; \; \gt .953$ $P[h[.67,.77] \mid c \cdot e \cdot b] \; \; \gt .995$ |
| 100 | 1000 | 720 | $P[h[.67,.77] \mid c \cdot e \cdot b] \; \; \gt .956$ $P[h[.66,.78] \mid c \cdot e \cdot b] \; \; \gt .997$ |

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=logic-inductive). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/logic-inductive/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=logic-inductive&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/logic-inductive/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- [Confirmation and Induction](http://www.iep.utm.edu/c/conf-ind.htm). Really nice overview by Franz Huber in the *Internet Encyclopedia of Philosophy*.
- [Inductive Logic](http://fitelson.org/il.pdf), (in PDF), by Branden Fitelson, *Philosophy of Science: An Encyclopedia*, (J. Pfeifer and S. Sarkar, eds.), Routledge. An extensive encyclopedia article on inductive logic.
- [Teaching Theory of Knowledge: Probability and Induction](http://www.ditext.com/clay/armendt2.html). A very extensive outline of issues in Probability and Induction, each topic accompanied by a list of relevant books and articles (without links), compiled by Brad Armendt and Martin Curd.
- [Probabilistic Confirmation Theory and Bayesian Reasoning](https://timothymcgrew.com/wp-content/uploads/2020/06/ConfirmationTheoryAnnBib.pdf). An annotated bibliography of influential works compiled by Timothy McGrew.
- [Bayesian Networks Without Tears](http://www.cs.ubc.ca/~murphyk/Bayes/Charniak_91.pdf), (in PDF), by Eugene Charniak (Computer Science and Cognitive Science, Brown University). An introductory article on Bayesian inference.
- [Miscellany of Works on Probabilistic Thinking](http://www.princeton.edu/~bayesway/). A collection of on-line articles on Subjective Probability and probabilistic reasoning by Richard Jeffrey and by several other philosophers writing on related issues.
- [Fitelson’s course on Confirmation Theory](http://fitelson.org/confirmation/). Main page of Branden Fitelson’s course on Confirmation Theory. The [Syllabus](http://fitelson.org/confirmation/syllabus.html) provides an extensive list of links to readings. The [Notes, Handouts, & Links](http://fitelson.org/confirmation/notes.html) page has Fitelson’s weekly course notes and some links to useful internet resources on confirmation theory.
- [Fitelson’s course on Probability and Induction](http://fitelson.org/probability/). Main page of Branden Fitelson’s course on Probability and Induction. The [Syllabus](http://fitelson.org/probability/syllabus.html) provides an extensive list of links to readings on the subject. The [Notes & Handouts](http://fitelson.org/probability/notes.html) page has Fitelson’s powerpoint slides for each of his lectures and some links to handouts for the course. The [Links](http://fitelson.org/probability/links.html) page contains links to some useful internet resources.

## Related Entries

Bayes’ Theorem | belief, formal representations of | Carnap, Rudolf | confirmation | epistemology: Bayesian | probability, interpretations of | statistics, philosophy of

### Acknowledgments

Thanks to Alan Hájek, Jim Joyce, and Edward Zalta for many valuable comments and suggestions. The editors and author also thank Greg Stokley and Philippe van Basshuysen for carefully reading an earlier version of the entry and identifying a number of typographical errors.

[^bovens-2003]: Bovens, Luc and Stephan Hartmann, 2003, *Bayesian Epistemology*, Oxford: Oxford University Press. doi:10.1093/0199269750.001.0001

[^carnap-1950]: Carnap, Rudolf, 1950, *Logical Foundations of Probability*, Chicago: University of Chicago Press.

[^carnap-1952]: –––, 1952, *The Continuum of Inductive Methods*, Chicago: University of Chicago Press.

[^carnap-1963]: –––, 1963, “Replies and Systematic Expositions”, in *The Philosophy of Rudolf Carnap*, Paul Arthur Schilpp (ed.),La Salle, IL: Open Court.

[^chihara-1987]: Chihara, Charles S., 1987, “Some Problems for Bayesian Confirmation Theory”, *British Journal for the Philosophy of Science*, 38(4): 551–560. doi:10.1093/bjps/38.4.551

[^christensen-1999]: Christensen, David, 1999, “Measuring Confirmation”, *Journal of Philosophy*, 96(9): 437–61. doi:10.2307/2564707

[^christensen-2004]: –––, 2004, *Putting Logic in its Place: Formal Constraints on Rational Belief*, Oxford: Oxford University Press. doi:10.1093/0199263256.001.0001

[^de-1937]: De Finetti, Bruno, 1937, “La Prévision: Ses Lois Logiques, Ses Sources Subjectives”, *Annales de l’Institut Henri Poincaré*, 7: 1–68; translated by Henry E. Kyburg, Jr. as “Foresight. Its Logical Laws, Its Subjective Sources”, in *Studies in Subjective Probability*, Henry E. Kyburg, Jr. and H.E. Smokler (eds.), Robert E. Krieger Publishing Company, 1980.

[^dowe-2007]: Dowe, David L., Steve Gardner, and Graham Oppy, 2007, “Bayes, Not Bust! Why Simplicity is No Problem for Bayesians”, *British Journal for the Philosophy of Science*, 58(4): 709–754. doi:10.1093/bjps/axm033

[^dubois-1980]: Dubois, Didier J. and Henri Prade, 1980, *Fuzzy Sets and Systems*, (Mathematics in Science and Engineering, 144), New York: Academic Press.

[^dubois-1990]: –––, 1990, “An Introduction to Possibilistic and Fuzzy Logics”, in Glenn Shafer and Judea Pearl (eds.), *Readings in Uncertain Reasoning*, San Mateo, CA: Morgan Kaufmann, 742–761.

[^duhem-1906]: Duhem, P., 1906, *La theorie physique. Son objet et sa structure*, Paris: Chevalier et Riviere; translated by P.P. Wiener, *The Aim and Structure of Physical Theory*, Princeton, NJ: Princeton University Press, 1954.

[^earman-1992]: Earman, John, 1992, *Bayes or Bust? A Critical Examination of Bayesian Confirmation Theory*, Cambridge, MA: MIT Press.

[^edwards-1972]: Edwards, A.W.F., 1972, *Likelihood: an account of the statistical concept of likelihood and its application to scientific inference*, Cambridge: Cambridge University Press.

[^edwards-1963]: Edwards, Ward, Harold Lindman, and Leonard J. Savage, 1963, “Bayesian Statistical Inference for Psychological Research”, *Psychological Review*, 70(3): 193–242. doi:10.1037/h0044139

[^eells-1985]: Eells, Ellery, 1985, “Problems of Old Evidence”, *Pacific Philosophical Quarterly*, 66(3–4): 283–302. doi:10.1111/j.1468-0114.1985.tb00254.x

[^eells-2006]: –––, 2006, “Confirmation Theory”, Sarkar and Pfeifer 2006..

[^eells-2000]: Eells, Ellery and Branden Fitelson, 2000, “Measuring Confirmation and Evidence”, *Journal of Philosophy*, 97(12): 663–672. doi:10.2307/2678462

[^field-1977]: Field, Hartry H., 1977, “Logic, Meaning, and Conceptual Role”, *Journal of Philosophy*, 74(7): 379–409. doi:10.2307/2025580

[^fisher-1922]: Fisher, R.A., 1922, “On the Mathematical Foundations of Theoretical Statistics”, *Philosophical Transactions of the Royal Society, series A* , 222(594–604): 309–368. doi:10.1098/rsta.1922.0009

[^fitelson-1999]: Fitelson, Branden, 1999, “The Plurality of Bayesian Measures of Confirmation and the Problem of Measure Sensitivity”, *Philosophy of Science*, 66: S362–S378. doi:10.1086/392738

[^fitelson-2001]: –––, 2001, “A Bayesian Account of Independent Evidence with Applications”, *Philosophy of Science*, 68(S3): S123–S140. doi:10.1086/392903

[^fitelson-2002]: –––, 2002, “Putting the Irrelevance Back Into the Problem of Irrelevant Conjunction”, *Philosophy of Science*, 69(4): 611–622. doi:10.1086/344624

[^fitelson-2006]: –––, 2006, “Inductive Logic”, Sarkar and Pfeifer 2006..

[^fitelson-2006-2]: –––, 2006, “Logical Foundations of Evidential Support”, *Philosophy of Science*, 73(5): 500–512. doi:10.1086/518320

[^fitelson-2007]: –––, 2007, “Likelihoodism, Bayesianism, and Relational Confirmation”, *Synthese*, 156(3): 473–489. doi:10.1007/s11229-006-9134-9

[^fitelson-2010]: Fitelson, Branden and James Hawthorne, 2010, “How Bayesian Confirmation Theory Handles the Paradox of the Ravens”, in Eells and Fetzer (eds.), *The Place of Probability in Science*, Open Court. [[Fitelson & Hawthorne 2010 preprint available from the author (PDF)](https://fitelson.org/ravens.pdf)]

[^forster-2004]: Forster, Malcolm and Elliott Sober, 2004, “Why Likelihood”, in Mark L. Taper and Subhash R. Lele (eds.), *The Nature of Scientific Evidence*, Chicago: University of Chicago Press.

[^friedman-1995]: Friedman, Nir and Joseph Y. Halpern, 1995, “Plausibility Measures: A User’s Guide”, in *UAI 95: Proceedings of the Eleventh Conference on Uncertainty in Artificial Intelligence*, 175–184.

[^gaifman-1982]: Gaifman, Haim and Marc Snir, 1982, “Probabilities Over Rich Languages, Testing and Randomness”, *Journal of Symbolic Logic*, 47(3): 495–548. doi:10.2307/2273587

[^gillies-2000]: Gillies, Donald, 2000, *Philosophical Theories of Probability*, London: Routledge.

[^glymour-1980]: Glymour, Clark N., 1980, *Theory and Evidence*, Princeton, NJ: Princeton University Press.

[^goodman-1983]: Goodman, Nelson, 1983, *Fact, Fiction, and Forecast*, 4ᵗʰ edition, Cambridge, MA: Harvard University Press.

[^hacking-1965]: Hacking, Ian, 1965, *Logic of Statistical Inference*, Cambridge: Cambridge University Press.

[^hacking-1975]: –––, 1975, *The Emergence of Probability: a Philosophical Study of Early Ideas about Probability, Induction and Statistical Inference*, Cambridge: Cambridge University Press. doi:10.1017/CBO9780511817557

[^hacking-2001]: –––, 2001, *An Introduction to Probability and Inductive Logic*, Cambridge: Cambridge University Press. doi:10.1017/CBO9780511801297

[^hájek-2003a]: Hájek, Alan, 2003a, “What Conditional Probability Could Not Be”, *Synthese*, 137(3):, 273–323. doi:10.1023/B:SYNT.0000004904.91112.16

[^hájek-2003b]: –––, 2003b, “Interpretations of the Probability Calculus”, in the *Stanford Encyclopedia of Philosophy*, (Summer 2003 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/sum2003/entries/probability-interpret/](https://plato.stanford.edu/archives/sum2003/entries/probability-interpret/)>

[^hájek-2005]: –––, 2005, “Scotching Dutch Books?” *Philosophical Perspectives*, 19 (Epistemology): 139–151. doi:10.1111/j.1520-8583.2005.00057.x

[^hájek-2007]: –––, 2007, “The Reference Class Problem is Your Problem Too”, *Synthese*, 156(3): 563–585. doi:10.1007/s11229-006-9138-5

[^halpern-2003]: Halpern, Joseph Y., 2003, *Reasoning About Uncertainty*, Cambridge, MA: MIT Press.

[^harper-1976]: Harper, William L., 1976, “Rational Belief Change, Popper Functions and Counterfactuals”, in Harper and Hooker 1976: 73–115. doi:10.1007/978-94-010-1853-1_5

[^harper-1976-2]: Harper, William L. and Clifford Alan Hooker (eds.), 1976, *Foundations of Probability Theory, Statistical Inference, and Statistical Theories of Science, volume I Foundations and Philosophy of Epistemic Applications of Probability Theory*, (The Western Ontario Series in Philosophy of Science, 6a), Dordrecht: Reidel. doi:10.1007/978-94-010-1853-1

[^hawthorne-1993]: Hawthorne, James, 1993, “Bayesian Induction *is* Eliminative Induction”, *Philosophical Topics*, 21(1): 99–138. doi:10.5840/philtopics19932117

[^hawthorne-1994]: –––, 1994,“On the Nature of Bayesian Convergence”, *PSA: Proceedings of the Biennial Meeting of the Philosophy of Science Association 1994*, 1: 241–249. doi:10.1086/psaprocbienmeetp.1994.1.193029

[^hawthorne-2005]: –––, 2005, “*Degree-of-Belief* and *Degree-of-Support*: Why Bayesians Need Both Notions”, *Mind*, 114(454): 277–320. doi:10.1093/mind/fzi277

[^hawthorne-2009]: –––, 2009, “The Lockean Thesis and the Logic of Belief”, in Franz Huber and Christoph Schmidt-Petri (eds.), *Degrees of Belief*, (Synthese Library, 342), Dordrecht: Springer, pp. 49–74. doi:10.1007/978-1-4020-9198-8_3

[^hawthorne-1999]: Hawthorne, James and Luc Bovens, 1999, “The Preface, the Lottery, and the Logic of Belief”, *Mind*, 108(430): 241–264. doi:10.1093/mind/108.430.241

[^hawthorne-2004]: Hawthorne, James and Branden Fitelson, 2004, “Discussion: Re-solving Irrelevant Conjunction With Probabilistic Independence”, *Philosophy of Science*, 71(4): 505–514. doi:10.1086/423626

[^hellman-1997]: Hellman, Geoffrey, 1997, “Bayes and Beyond”, *Philosophy of Science*, 64(2): 191–221. doi:10.1086/392548

[^hempel-1945]: Hempel, Carl G., 1945, “Studies in the Logic of Confirmation”, *Mind*, 54(213): 1–26, 54(214):97–121. doi:10.1093/mind/LIV.213.1 doi:10.1093/mind/LIV.214.97

[^horwich-1982]: Horwich, Paul, 1982, *Probability and Evidence*, Cambridge: Cambridge University Press. doi:10.1017/CBO9781316494219

[^howson-1997]: Howson, Colin, 1997, “A Logic of Induction”, *Philosophy of Science*, 64(2): 268–290. doi:10.1086/392551

[^howson-2000]: –––, 2000, *Hume’s Problem: Induction and the Justification of Belief*, Oxford: Oxford University Press. doi:10.1093/0198250371.001.0001

[^howson-2002]: –––, 2002, “Bayesianism in Statistics“, in Swinburne 2002: 39–71. doi:10.5871/bacad/9780197263419.003.0003

[^howson-2007]: –––, 2007, “Logic With Numbers”, *Synthese*, 156(3): 491–512. doi:10.1007/s11229-006-9135-8

[^howson-1993]: Howson, Colin and Peter Urbach, 1993, *Scientific Reasoning: The Bayesian Approach*, La Salle, IL: Open Court. [3rd edition, 2005.]

[^huber-2005a]: Huber, Franz, 2005a, “Subjective Probabilities as Basis for Scientific Reasoning?” *British Journal for the Philosophy of Science*, 56(1): 101–116. doi:10.1093/phisci/axi105

[^huber-2005b]: –––, 2005b, “What Is the Point of Confirmation?” *Philosophy of Science*, 72(5): 1146–1159. doi:10.1086/508961

[^jaynes-2003]: Jaynes, Edwin T., 2003, *Probability Theory: the Logic of Science*, Cambridge: Cambridge University Press.

[^jeffrey-1983]: Jeffrey, Richard C., 1983, *The Logic of Decision*, 2nd edition, Chicago: University of Chicago Press.

[^jeffrey-1987]: –––, 1987, “Alias Smith and Jones: The Testimony of the Senses”, *Erkenntnis*, 26(3): 391–399. doi:10.1007/BF00167725

[^jeffrey-1992]: –––, 1992, *Probability and the Art of Judgment*, New York: Cambridge University Press. doi:10.1017/CBO9781139172394

[^jeffrey-2004]: –––, 2004, *Subjective Probability: The Real Thing*, Cambridge: Cambridge University Press. doi:10.1017/CBO9780511816161

[^jeffreys-1939]: Jeffreys, Harold, 1939, *Theory of Probability*, Oxford: Oxford University Press.

[^joyce-1998]: Joyce, James M., 1998, “A Nonpragmatic Vindication of Probabilism”, *Philosophy of Science*, 65(4): 575–603. doi:10.1086/392661

[^joyce-1999]: –––, 1999, *The Foundations of Causal Decision Theory*, New York: Cambridge University Press. doi:10.1017/CBO9780511498497

[^joyce-2003]: –––, 2003, “Bayes’ Theorem”, in the *Stanford Encyclopedia of Philosophy*, (Summer 2003 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/win2003/entries/bayes-theorem/](https://plato.stanford.edu/archives/win2003/entries/bayes-theorem/)>

[^joyce-2004]: –––, 2004, “Bayesianism”, in Alfred R. Mele and Piers Rawling (eds.), *The Oxford Handbook of Rationality*, Oxford: Oxford University Press, pp. 132–153. doi:10.1093/0195145399.003.0008

[^joyce-2005]: –––, 2005, “How Probabilities Reflect Evidence”, *Philosophical Perspectives*, 19: 153–179. doi:10.1111/j.1520-8583.2005.00058.x

[^kaplan-1996]: Kaplan, Mark, 1996, *Decision Theory as Philosophy*, Cambridge: Cambridge University Press.

[^kelly-1997]: Kelly, Kevin T., Oliver Schulte, and Cory Juhl, 1997, “Learning Theory and the Philosophy of Science”, *Philosophy of Science*, 64(2): 245–267. doi:10.1086/392550

[^keynes-1921]: Keynes, John Maynard, 1921, *A Treatise on Probability*, London: Macmillan and Co.

[^kolmogorov-1956]: Kolmogorov, A.N., 1956, *Foundations of the Theory of Probability* (*Grundbegriffe der Wahrscheinlichkeitsrechnung*, 2ⁿᵈ edition, New York: Chelsea Publishing Company.

[^koopman-1940]: Koopman, B.O., 1940, “The Bases of Probability”, *Bulletin of the American Mathematical Society*, 46(10): 763–774. Reprinted in H. Kyburg and H. Smokler (eds.), 1980, *Studies in Subjective Probability*, 2nd edition, Huntington, NY: Krieger Publ. Co. [[Koopman 1940 available online](https://projecteuclid.org/euclid.bams/1183503229)]

[^kyburg-1974]: Kyburg, Henry E., Jr., 1974, *The Logical Foundations of Statistical Inference*, Dordrecht: Reidel. doi:10.1007/978-94-010-2175-3

[^kyburg-1977]: –––, 1977, “Randomness and the Right Reference Class”, *Journal of Philosophy*, 74(9): 501–520. doi:10.2307/2025794

[^kyburg-1978]: –––, 1978, “An Interpolation Theorem for Inductive Relations”, *Journal of Philosophy*, 75:93–98.

[^kyburg-2006]: –––, 2006, “Belief, Evidence, and Conditioning”, *Philosophy of Science*, 73(1): 42–65. doi:10.1086/510174

[^lange-1999]: Lange, Marc, 1999, “Calibration and the Epistemological Role of Bayesian Conditionalization”, *Journal of Philosophy*, 96(6): 294–324. doi:10.2307/2564680

[^lange-2002]: –––, 2002, “Okasha on Inductive Scepticism”, *The Philosophical Quarterly*, 52(207): 226–232. doi:10.1111/1467-9213.00264

[^laudan-1997]: Laudan, Larry, 1997, “How About Bust? Factoring Explanatory Power Back into Theory Evaluation”, *Philosophy of Science*, 64(2): 206–216. doi:10.1086/392553

[^lenhard-2006]: Lenhard Johannes, 2006, “Models and Statistical Inference: The Controversy Between Fisher and Neyman-Pearson”, *British Journal for the Philosophy of Science*, 57(1): 69–91. doi:10.1093/bjps/axi152

[^levi-1967]: Levi, Isaac, 1967, *Gambling with Truth: An Essay on Induction and the Aims of Science*, New York: Knopf.

[^levi-1977]: –––, 1977, “Direct Inference”, *Journal of Philosophy*, 74(1): 5–29. doi:10.2307/2025732

[^levi-1978]: –––, 1978, “Confirmational Conditionalization”, *Journal of Philosophy*, 75(12): 730–737. doi:10.2307/2025516

[^levi-1980]: –––, 1980, *The Enterprise of Knowledge: An Essay on Knowledge, Credal Probability, and Chance*, Cambridge, MA: MIT Press.

[^lewis-1980]: Lewis, David, 1980, “A Subjectivist’s Guide to Objective Chance”, in Richard C. Jeffrey, (ed.), *Studies in Inductive Logic and Probability*, vol. 2, Berkeley: University of California Press, 263–293.

[^maher-1993]: Maher, Patrick, 1993, *Betting on Theories*, Cambridge: Cambridge University Press.

[^maher-1996]: –––, 1996, “Subjective and Objective Confirmation”, *Philosophy of Science*, 63(2): 149–174. doi:10.1086/289906

[^maher-1997]: –––, 1997, “Depragmatized Dutch Book Arguments”, *Philosophy of Science*, 64(2): 291–305. doi:10.1086/392552

[^maher-1999]: –––, 1999, “Inductive Logic and the Ravens Paradox”, *Philosophy of Science*, 66(1): 50–70. doi:10.1086/392676

[^maher-2004]: –––, 2004, “Probability Captures the Logic of Scientific Confirmation”, in Christopher Hitchcock (ed.), *Contemporary Debates in Philosophy of Science*, Oxford: Blackwell, 69–93.

[^maher-2005]: –––, 2005, “Confirmation Theory”, *The Encyclopedia of Philosophy*, 2nd edition, Donald M. Borchert (ed.), Detroit: Macmillan.

[^maher-2006a]: –––, 2006a, “The Concept of Inductive Probability”, *Erkenntnis*, 65(2): 185–206. doi:10.1007/s10670-005-5087-5

[^maher-2006b]: –––, 2006b, “A Conception of Inductive Logic”, *Philosophy of Science*, 73(5): 513–523. doi:10.1086/518321

[^maher-2010]: –––, 2010, “Bayesian Probability”, *Synthese*, 172(1): 119–127. doi:10.1007/s11229-009-9471-6

[^mayo-1996]: Mayo, Deborah G., 1996, *Error and the Growth of Experimental Knowledge*, Chicago: University of Chicago Press.

[^mayo-1997]: –––, 1997, “Duhem’s Problem, the Bayesian Way, and Error Statistics, or ‘What’s Belief Got to do with It?’”, *Philosophy of Science*, 64(2): 222–244. doi:10.1086/392549

[^mayo-2006]: Mayo Deborah and Aris Spanos, 2006, “Severe Testing as a Basic Concept in a Neyman-Pearson Philosophy of Induction“, *British Journal for the Philosophy of Science*, 57(2): 323–357. doi:10.1093/bjps/axl003

[^mcgee-1994]: McGee, Vann, 1994, “Learning the Impossible”, in E. Eells and B. Skyrms (eds.), *Probability and Conditionals: Belief Revision and Rational Decision*, New York: Cambridge University Press, 179–200.

[^mcgrew-2003]: McGrew, Timothy J., 2003, “Confirmation, Heuristics, and Explanatory Reasoning”, *British Journal for the Philosophy of Science*, 54: 553–567.

[^mcgrew-2008]: McGrew, Lydia and Timothy McGrew, 2008, “Foundationalism, Probability, and Mutual Support”, *Erkenntnis*, 68(1): 55–77. doi:10.1007/s10670-007-9062-1

[^neyman-1967]: Neyman, Jerzy and E.S. Pearson, 1967, *Joint Statistical Papers*, Cambridge: Cambridge University Press.

[^norton-2003]: Norton, John D., 2003, “A Material Theory of Induction”, *Philosophy of Science*, 70(4): 647–670. doi:10.1086/378858

[^norton-2007]: –––, 2007, “Probability Disassembled”, *British Journal for the Philosophy of Science*, 58(2): 141–171. doi:10.1093/bjps/axm009

[^okasha-2001]: Okasha, Samir, 2001, “What Did Hume Really Show About Induction?”, *The Philosophical Quarterly*, 51(204): 307–327. doi:10.1111/1467-9213.00231

[^popper-1968]: Popper, Karl, 1968, *The Logic of Scientific Discovery*, 3ʳᵈ edition, London: Hutchinson.

[^quine-1953]: Quine, W.V., 1953, “Two Dogmas of Empiricism”, in *From a Logical Point of View*, New York: Harper Torchbooks. Routledge Encyclopedia of Philosophy, Version 1.0, London: Routledge

[^ramsey-1926]: Ramsey, F.P., 1926, “Truth and Probability”, in *Foundations of Mathematics and other Essays*, R.B. Braithwaite (ed.), Routledge & P. Kegan,1931, 156–198. Reprinted in *Studies in Subjective Probability*, H. Kyburg and H. Smokler (eds.), 2ⁿᵈ ed., R.E. Krieger Publishing Company, 1980, 23–52. Reprinted in *Philosophical Papers*, D.H. Mellor (ed.), Cambridge: University Press, Cambridge, 1990,

[^reichenbach-1938]: Reichenbach, Hans, 1938, *Experience and Prediction: An Analysis of the Foundations and the Structure of Knowledge*, Chicago: University of Chicago Press.

[^rényi-1970]: Rényi, Alfred, 1970, *Foundations of Probability*, San Francisco, CA: Holden-Day.

[^rosenkrantz-1981]: Rosenkrantz, R.D., 1981, *Foundations and Applications of Inductive Probability*, Atascadero, CA: Ridgeview Publishing.

[^roush-2004]: Roush, Sherrilyn , 2004, “Discussion Note: Positive Relevance Defended”, *Philosophy of Science*, 71(1): 110–116. doi:10.1086/381416

[^roush-2006]: –––, 2006, “Induction, Problem of”, Sarkar and Pfeifer 2006..

[^roush-2006-2]: –––, 2006, *Tracking Truth: Knowledge, Evidence, and Science*, Oxford: Oxford University Press.

[^royall-1997]: Royall, Richard M., 1997, *Statistical Evidence: A Likelihood Paradigm*, New York: Chapman & Hall/CRC.

[^salmon-1966]: Salmon, Wesley C., 1966, *The Foundations of Scientific Inference*, Pittsburgh, PA: University of Pittsburgh Press.

[^salmon-1975]: –––, 1975, “Confirmation and Relevance”, in H. Feigl and G. Maxwell (eds.), *Induction, Probability, and Confirmation*, (Minnesota Studies in the Philosophy of Science, 6), Minneapolis: University of Minnesota Press, 3–36.

[^sarkar-2006]: Sarkar, Sahotra and Jessica Pfeifer (eds.), 2006, *The Philosophy of Science: An Encyclopedia*, 2 volumes, New York: Routledge.

[^savage-1954]: Savage, Leonard J., 1954, *The Foundations of Statistics*, John Wiley (2nd ed., New York: Dover 1972).

[^savage-1962]: Savage, Leonard J., et al., 1962, *The Foundations of Statistical Inference*, London: Methuen.

[^schlesinger-1991]: Schlesinger, George N., 1991, *The Sweep of Probability*, Notre Dame, IN: Notre Dame University Press.

[^seidenfeld-1978]: Seidenfeld, Teddy, 1978, “Direct Inference and Inverse Inference”, *Journal of Philosophy*, 75(12): 709–730. doi:10.2307/2025515

[^seidenfeld-1992]: –––, 1992, “R.A. Fisher’s Fiducial Argument and Bayes’ Theorem”, *Statistical Science*, 7(3): 358–368. doi:10.1214/ss/1177011232

[^shafer-1976]: Shafer, Glenn, 1976, *A Mathematical Theory of Evidence*, Princeton, NJ: Princeton University Press.

[^shafer-1990]: –––, 1990, “Perspectives on the Theory and Practice of Belief Functions”, *International Journal of Approximate Reasoning*, 4(5–6): 323–362. doi:10.1016/0888-613X(90)90012-Q

[^skyrms-1984]: Skyrms, Brian, 1984, *Pragmatics and Empiricism*, New Haven, CT: Yale University Press.

[^skyrms-1990]: –––, 1990, *The Dynamics of Rational Deliberation*, Cambridge, MA: Harvard University Press.

[^skyrms-2000]: –––, 2000, *Choice and Chance: An Introduction to Inductive Logic*, 4ᵗʰ edition, Belmont, CA: Wadsworth, Inc.

[^sober-2002]: Sober, Elliott, 2002, “Bayesianism—Its Scope and Limits”, in Swinburne 2002: 21–38. doi:10.5871/bacad/9780197263419.003.0002

[^spohn-1988]: Spohn, Wolfgang, 1988, “Ordinal Conditional Functions: A Dynamic Theory of Epistemic States”, in William L. Harper and Brian Skyrms (eds.), *Causation in Decision, Belief Change, and Statistics*, vol. 2, Dordrecht: Reidel, 105–134. doi:10.1007/978-94-009-2865-7_6

[^strevens-2004]: Strevens, Michael, 2004, “Bayesian Confirmation Theory: Inductive Logic, or Mere Inductive Framework?” *Synthese*, 141(3): 365–379. doi:10.1023/B:SYNT.0000044991.73791.f7

[^suppes-2007]: Suppes, Patrick, 2007, “Where do Bayesian Priors Come From?” *Synthese*, 156(3): 441–471. doi:10.1007/s11229-006-9133-x

[^swinburne-2002]: Swinburne, Richard, 2002, *Bayes’ Theorem*, Oxford: Oxford University Press. doi:10.5871/bacad/9780197263419.001.0001

[^talbot-2001]: Talbot, W., 2001, “Bayesian Epistemology”, in the *Stanford Encyclopedia of Philosophy*, (Fall 2001 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/fall2001/entries/epistemology-bayesian/](https://plato.stanford.edu/archives/fall2001/entries/epistemology-bayesian/)>

[^teller-1976]: Teller, Paul, 1976, “Conditionalization, Observation, and Change of Preference”, in Harper and Hooker 1976: 205–259. doi:10.1007/978-94-010-1853-1_9

[^van-1983]: Van Fraassen, Bas C., 1983, “Calibration: A Frequency Justification for Personal Probability ”, in R.S. Cohen and L. Laudan (eds.), *Physics, Philosophy, and Psychoanalysis: Essays in Honor of Adolf Grunbaum*, Dordrecht: Reidel. doi:10.1007/978-94-009-7055-7_15

[^venn-1876]: Venn, John, 1876, *The Logic of Chance*, 2ⁿᵈ ed., Macmillan and co; reprinted, New York, 1962.

[^vineberg-2006]: Vineberg, Susan, 2006, “Dutch Book Argument”, Sarkar and Pfeifer 2006..

[^vranas-2004]: Vranas, Peter B.M., 2004, “Hempel’s Raven Paradox: A Lacuna in the Standard Bayesian Solution”, *British Journal for the Philosophy of Science*, 55(3): 545–560. doi:10.1093/bjps/55.3.545

[^weatherson-1999]: Weatherson, Brian, 1999, “Begging the Question and Bayesianism”, *Studies in History and Philosophy of Science [Part A]*, 30(4): 687–697. doi:10.1016/S0039-3681(99)00020-5

[^williamson-2007]: Williamson, Jon, 2007, “Inductive Influence”, *British Journal for Philosophy of Science*, 58(4): 689–708. doi:10.1093/bjps/axm032
