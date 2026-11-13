# Epistemic Utility Arguments for Epistemic Norms
**First published Fri Sep 23, 2011; substantive revision Wed Oct 11, 2023**

*Pettigrew, Richard*

If I believe George Eliot wrote more than six novels and also believe she wrote fewer than four, you will no doubt judge my beliefs irrational. After all, if she did write more than six, she didn’t write fewer than four. And similarly, if my degree of belief that Eliot wrote more than six novels is greater than my degree of belief that she wrote more than five, then again you will think me irrational. After all, if she did write more than six, she also wrote more than five. In both cases, there is a general norm I fail to satisfy. In the first, it might be this:

> **Consistency$_2$** If two propositions cannot both be true together, you should not believe both.

In the second case, it might be this:

> **No Drop** If one proposition entails another, then your degree of belief in the first should not exceed your degree of belief in the second.

This entry is concerned with norms like these. More specifically, it is concerned with how we might establish these norms. More specifically still, it is concerned with what epistemologists have come to call *epistemic utility arguments* in their favor. The norms we seek to establish primarily govern *epistemic states*; that is, they say what rationality requires of your beliefs, degrees of belief, and any other attitudes whose role it is to represent the way the world is. But, as we will see, they also govern the activities by which we acquire those states, such as gathering and responding to evidence.

Epistemic utility arguments are inspired by traditional utility-based arguments in decision theory, so let’s begin with a quick summary of those. Traditional decision theory explores a particular strategy for establishing the norms that govern which choices it is rational for an individual to make in a particular situation (see entry on normative theories of rational choice: expected utility). Given such a situation, the framework for the theory includes: *states of the world* described in as much detail as required; *actions* that are available to the individual in the situation, and the individual’s *utility function*, which takes a state of the world and an action and returns a measure of the extent to which she values the outcome of performing that action at that world. We call this measure the *utility* of the outcome at the world. For example, there might be just two relevant states of the world: one in which it rains and one in which it doesn’t. And there might be just two relevant actions from which to choose: take an umbrella when you leave the house or don’t. Then your utility function will measure how much you value the outcomes of each action at each state of the world: that is, it will give the value of being in the rain without an umbrella, being in the rain with an umbrella, being with an umbrella when there is no rain, and being without an umbrella when there is no rain. With this framework in hand, we can state certain very general norms of action in terms of it. For instance, if one action has strictly greater utility than another in every possible state of the world, we say the first *strongly dominates* the second, and the norm of Dominance says that you should not choose a strongly dominated action.

In epistemic utility theory, the states of the world remain the same, but the possible actions an individual might perform are replaced by the possible *epistemic states* she might be in, and the utility function is replaced by an *epistemic utility function*, which takes a state of the world and an epistemic state and returns a measure of the purely epistemic value of that epistemic state at that state of the world. So, in epistemic utility theory, we appeal to epistemic utility to ask which of a range of possible epistemic states it is rational to be in, just as in traditional utility theory we appeal to non-epistemic, pragmatic utility to ask which of a range of possible actions it is rational to perform. (In fact, we will often talk of epistemic *dis*utility rather than epistemic utility in this entry. But it is easy to translate between them: the negative of an epistemic utility function is an epistemic disutility function, and *vice versa*.)

Again, certain very general norms may be stated, such as the obvious analogue of Dominance from above: if one epistemic state has greater epistemic utility than another in every possible state of the world, then it is irrational to be in the latter. And we might use them to establish norms for epistemic states. For instance, consider Consistency$_2$ from the introduction. Let’s say the epistemic utility of believing a truth is some positive number $R$, while the epistemic utility of believing a falsehood is some negative number $-W$ ($R$ for *R*ight, $W$ for *W*rong). And let’s say the epistemic utility of a set of beliefs is just the sum of the epistemic utilities of the individual beliefs that belong to it, so that if you believe two truths and a falsehood, for instance, your epistemic utility is $2R - W$. Now suppose that $W$ is greater than $R$; that is, the badness of believing falsely is greater than the goodness of believing truly; that is, we more strongly wish to avoid false belief than we want to achieve true belief; that is, our epistemic utilities encode a sort of epistemic conservatism. Then, if I believe each of two propositions that cannot both be true together, my total epistemic utility is either $R-W$, if one is true and the other false, or $-2W$ if neither is true. And each of these is less than zero. So suspending judgment on both is guaranteed to be better than believing both. And so, by Dominance, believing both is irrational and we have an epistemic utility argument for Consistency$_2$. This is the style of argument we will consider in this entry. As we’ll see in Section 5.2, there is an argument from Dominance to No Drop as well.

Because we appeal to the purely *epistemic* utility of the epistemic states we consider, rather than the *pragmatic* or *practical* utility of the outcomes of the choices they lead us to make, the arguments of epistemic utility theory are different from betting arguments or dutch book arguments for epistemic norms (Ramsey 1926 [1931]; de Finetti 1937 [1980]; see entry on dutch book arguments)[^finetti-1937][^ramsey-1926]. They are also different from the sort of axiomatic justification exemplified by Cox's theorem (Cox 1946, 1961; Paris 1994)[^cox-1946][^paris-1994] as well as the sort of structural justification given by R. I. G. Hughes and Bas van Fraassen (1984) and Hannes Leitgeb (2021).

## 1. Modelling Epistemic States

Let’s begin by listing the different ways in which we might represent an individual’s epistemic state at a given time (see entry on formal representations of belief). We might represent them using any of the following:

- the set of propositions she believes at the time (we might call this the *outright belief model*; it is the object of study in much traditional epistemology and in doxastic and epistemic logic; outright beliefs are those we report when we say ‘I think I switched off the gas’ or ‘I believe it will rain tomorrow’; we’ll consider them in Section 4);
- a credence function, which takes each proposition about which she has an opinion and returns her credence in that proposition at the time, where her credence in a proposition measures how confident she is in it as a number at least 0 and at most 1 (this is the *precise credence* or *standard Bayesian model*; it is the object of study in much formal and Bayesian epistemology; credences are the states we report when we say ‘I’m 70% sure I switched off the gas’ or ‘I’m 50-50 whether it will rain tomorrow’; we’ll consider them in Section 5);
- a comparative confidence ordering, which takes each pair of propositions about which she has an opinion and says whether she is more confident in one than the other, equally confident in both, or neither more confident in one nor equally confident in both (this is the *comparative confidence model*; we report comparative confidences when we say ‘I’m more confident I switched off the gas than the electricity’ or ‘I’m more confident than not that it will rain tomorrow’; we’ll consider them in Section 6);
- a set of credence functions, each of which is a precisification of her otherwise vague or imprecise or indeterminate credences at the time (this is the *imprecise credence model*; we report imprecise credences when we say ‘I’m 50%–70% sure I switched off the gas’ or ‘I’m less than 60% sure it will rain tomorrow’; we’ll consider them in Section 7);

Epistemic utility theory may be applied to any one of these ways of representing an individual’s epistemic state. Whichever we choose, we define an epistemic (dis)utility function to be a function that takes a set of epistemic states modelled in this way, together with a state of the world, to a real number, or (positive or) negative infinity, and we take this number to measure the epistemic (dis)utility of those epistemic attitudes at that world.

## 2. The Form of Arguments in Epistemic Utility Theory

We begin by highlighting the form that epistemic utility arguments take, regardless of which sorts of epistemic states concern us. Recall the argument for Consistency$_2$ from the introduction. It had two premises: first, we placed conditions on the measure of epistemic utility; second, we stated a norm from standard utility theory. From those, we deduced the norm on belief. This is the structure of nearly all epistemic utility arguments. In general, in epistemic utility theory, we argue for an epistemic norm N using the following two ingredients:

- **E** A set of conditions that a legitimate measure of epistemic utility must satisfy.
- **Q** A norm of standard utility theory (or decision theory), which is to be applied, using an epistemic utility function, to discover what rationality requires of an agent in a given situation.

Typically, the inference from E and Q to N appeals to a mathematical theorem, which shows that, applied to any epistemic utility function that satisfies the conditions E, the norm Q entails the norm N.

## 3. Agendas and States of the World

One final piece of general stage-setting will be useful before we can embark on our journey through the arguments. On each of the models of belief listed in Section 1, there is a set of propositions with which our individual’s epistemic states are concerned: the ones to which they assign credences in the precise credence model, for instance. We call this set their *agenda* and often denote it $\mathcal{F}$.

For the most part, we’ll assume this agenda is a finite algebra of propositions. That is, (i) it contains finitely many propositions; (ii) it contains a necessarily true proposition and a necessarily false proposition; (iii) and it is closed under taking negations, conjunctions, and disjunctions—that is, if it contains a proposition, it also contains its negation, and if it contains two propositions, it also contains their conjunction and their disjunction. (But see Section 5.2.5, where we lift assumption (i).)

The epistemic utility of an individual’s set of epistemic attitudes depends on the way the world is. For instance, a belief is epistemically valuable if it’s true, but disvaluable if it’s false. So we’d better say how we represent these states of the world formally. For the most part, we’ll assume the logic that governs the propositions in our individual’s agenda is classical (but see Section 5.2.6, where we drop that assumption). In that case, a state of the world relative to an agenda is just a classically consistent assignment of the classical truth values, True and False, to the propositions in that agenda. We often write $\mathcal{W}_\mathcal{F}$ for the set of states of the world relative to the agenda $\mathcal{F}$.

Since $\mathcal{F}$ is a finite algebra, for each state of the world $w$ relative to $\mathcal{F}$, there is a proposition in $\mathcal{F}$ that is true at that state of the world and only at that state of the world. We will abuse notation and also write $w$ for this proposition.

## 4. Epistemic Utility Arguments concerning Outright Beliefs

In the outright belief model, our individual’s epistemic state is represented by their *belief set*, which contains each proposition in their agenda that they believe; on the rest, we say that they suspend judgment.

Following Kenny Easwaran (2016) and Kevin Dorst (2017), who in turn generalize Carl Hempel’s (1962) approach, we define the epistemic utility of a belief set at a state of the world as follows: the epistemic utility of a belief in a true proposition is $R$, while the epistemic utility of a belief in a false proposition is $-W$, where $0 \lt R, W$; and the epistemic utility of a belief set is the sum of the epistemic utilities of the beliefs it contains. I’ll call this the Jamesian Epistemic Utility assumption, since it allows for different ways of scoring the goodness of believing a truth and the badness of believing a falsehood, which goes some way to explicating the view in William James’ ‘The Will to Believe’ (1897).

Easwaran and Dorst impose no constraints on $R$ and $W$ except $-W \lt 0 \lt R$. Hempel assumes $R, W = 1$.

### 4.1 Dominance and Consistency

So, with all this in hand, the argument for Consistency$_2$ runs as follows:

> **Epistemic Conservatism** $W \gt R \gt 0$.
>
> **Dominance** If one option strongly dominates another, rationality requires you not to choose the second.
>
> Therefore,
>
> **Consistency$_2$** If two propositions cannot both be true together, rationality requires that you should not believe both.

### 4.2 Expected Epistemic Utility and the Lockean Thesis

Dominance is a very weak norm of rational choice, but there are stronger ones. Among them is one of the most popular norms of decision theory, which says you should maximize expected utility from the point of view of your credences.

> **Maximize Subjective Expected Utility** If one option has greater expected utility than another from the point of view of your credences, then rationality requires that you should not choose the second.

The expected utility of an option relative to your credences is obtained by taking its utility at each state, weighting that by your credence in that state, and summing up these credence-weighted utilities. For instance, suppose $p$ is your credence in a proposition and $1-p$ is your credence in its negation. Then the expected epistemic utility of believing that proposition from the point of view of your credences is

> $p \times \text{epistemic utility of believing a truth} + (1-p)\ \times$
> $ \text{epistemic utility of believing a falsehood} = pR + (1-p)(-W)$

Now we can ask when believing a proposition maximizes expected utility from the point of view of your credences.

> **Expectation Theorem for the Lockean Thesis (Hempel 1962; Easwaran 2016; Dorst 2017)[^dorst-2017][^easwaran-2016][^hempel-1962]** Suppose your credence in $X$ is $p$. Then:
>
> - If $p \gt \frac{W}{R+W}$, then believing $X$ uniquely maximizes expected epistemic utility. (That is, believing has strictly greater expected utility than suspending.)
> - If $p = \frac{W}{R+W}$, then believing $X$ and suspending judgment on $X$ both maximize expected epistemic utility. (That is, believing has the same expected utility as suspending.)
> - If $p \lt \frac{W}{R + W}$, then suspending judgment on $X$ uniquely maximizes expected epistemic utility. (That is, believing has strictly less expected utility than suspending.)

Easwaran and Dorst both appeal to this result to argue for the Lockean Thesis, which is the most well-known norm that connects credences and outright beliefs. It takes its name from passages in John Locke’s (1689 [1975]) *An Essay on Human Understanding* in which he suggests that belief is nothing more than sufficiently high credence, but it was formulated explicitly by Richard Foley (1992). In fact, the Lockean Thesis is a family of putative norms: each member of the family is distinguished by the threshold above which it demands belief, below which it demands suspension, and at which it permits either.

> **The Lockean Thesis with threshold $t$**
>
> Suppose your credence in $X$ is $p$. Then
>
> - If $p \gt t$, you are rationally required to believe $X$;
> - If $p = t$, you are rationally permitted to believe $X$ and rationally permitted to suspend on $X$;
> - If $p \lt t$, you are rationally required to suspend on $X$.

Then we have the following argument:

> **Jamesian Epistemic Utility** $0 \lt R, W$.
>
> **Maximize Subjective Expected Utility**
>
> Therefore,
>
> **The Lockean Thesis with threshold $\frac{W}{R+W}$**

#### 4.2.1 Expected Epistemic Utility, the Uniqueness Thesis, and Epistemic Permissivism

Thomas Kelly (2014) has pointed out that this argument has an interesting consequence for the debate in epistemology between those who argue for the Uniqueness Thesis and those who side with Epistemic Permissivism. Given a sort of epistemic state, the Uniqueness Thesis for that sort of state runs as follows:

> **The Uniqueness Thesis** Given an agenda, the following holds: for any body of evidence, there is a unique epistemic state of the given sort concerning the propositions in that agenda that rationality requires you to have if that body of evidence is your total evidence.

Epistemic Permissivism is simply the negation of the Uniqueness Thesis. So, for instance, the Uniqueness Thesis for credences says that, for any agenda and any body of evidence, there is a unique credence function over that agenda that rationality requires you to have in response to that evidence, while Epistemic Permissivism says that there is at least one body of evidence for which there is more than one credence function it is rational to have in response to that evidence.

Now, suppose you subscribe to the Uniqueness Thesis about credences. But you also think that rationality permits different ways in which you might set the utility $R$ of believing a truth and the utility $-W$ of believing a falsehood. For instance, you might think $R = 1, W = 2$ is permitted, but so is $R = 2, W = 3$. And suppose the unique rational credence in proposition $X$ is 0.65. Maximizing expected epistemic utility with $R = 2, W = 3$ entails the Lockean Thesis with threshold $\frac{3}{2+3}$, and this requires that you believe $X$, since $0.65 \gt \frac{3}{2+3}$; but maximizing expected epistemic utility with $R = 1, W = 2$ entails the Lockean Thesis with threshold $\frac{2}{1+2}$, and this requires that you suspend on $X$, since $0.65 \lt \frac{2}{1+2}$. And so we have Epistemic Permissivism about outright beliefs, even though we have the Uniqueness Thesis for credences. Which beliefs rationality requires you to have depends not only on your evidence, but also on your epistemic utilities. In general, the smaller the ratio of $R$ to $W$, the higher your credence in a proposition must be for you to believe it.

#### 4.2.2 Expected Epistemic Utility and Consistency

Another interesting consequence of the Expectation Theorem for the Lockean Thesis is that it shows that we can’t give an argument from Dominance to the natural generalization of Consistency$_2$ to arbitrarily many propositions; and we can only give the generalizations to $n$ propositions, for some given $n$, by becoming increasingly conservative in our epistemic utilities (Fitelson & Easwaran 2015; Easwaran 2016)[^easwaran-2015][^easwaran-2016][^fitelson-2015].

Say that a set of propositions is inconsistent if the propositions in it cannot all be true together. Then we have the following two norms:

> **Consistency$_n$** If **A** is an inconsistent set of $n$ or fewer propositions, then rationality requires that you should not believe each proposition in **A**.

> **Consistency** If **A** is an inconsistent set of finitely many propositions, then rationality requires that you should not believe each proposition in **A**.

Take any $n$ and suppose there is a lottery with $n$ tickets in which each ticket is equally likely to be the winner. Let $L_i$ be the proposition that says the $i^\mathrm{th}$ ticket will lose. Then the set of propositions $\{L_1, \ldots, L_n\}$ is inconsistent. Nonetheless, if my credence in each $L_i$ is $1 - \frac{1}{n}$, as it should be, and the Lockean threshold $t$ is below $1 - \frac{1}{n}$, then the Lockean Thesis with threshold $t$ says I must believe each member of this incoherent set. What’s more, we know that believing each maximizes expected epistemic utility from the point of view of those credences, providing $\frac{W}{R + W}$ is less than $1 - \frac{1}{n}$. And we also know that no strongly dominated option can ever maximize expected utility. So, if $W \lt (n-1)R$, and therefore $\frac{W}{R + W} \lt 1 - \frac{1}{n}$, then it’s possible to have an inconsistent set of beliefs in $n$ propositions that is not dominated. And this shows in turn that there can be no argument from Dominance to Consistency. For any $W \gt R \gt 0$, there is some $n$ such that $\frac{W}{R+W} \lt 1 - \frac{1}{n}$. On the other hand, if $n \lt \frac{R+W}{R}$, then we can at least argue from Dominance to Consistency$_n$, since the maximum epistemic utility of believing each of $n$ inconsistent propositions is $(n-1)R - W$, which is always less than zero if $n \lt \frac{R+W}{R}$.

### 4.3 Dominance and Almost Lockean Completeness

Daniel Rothschild (2021) gives an argument from Dominance to a norm he calls Almost Lockean Completeness for Belief Sets at a threshold, which says:

> **Almost Lockean Completeness for Belief Sets with threshold $t$** Rationality requires that there there is some probabilistic credence function such that your beliefs satisfy the Lockean Thesis with threshold $t$ with respect to that credence function.

It’s worth noting that the Lockean Thesis and Almost Lockean Completeness for Belief Sets are quite different norms. The first governs a relationship between your credences and your beliefs; the second does not even assume you have any credences, and instead governs only your beliefs—it says that your beliefs should be *as they would be if* you were to have credences and they were to be related to your beliefs as the Lockean Thesis says they should be.

Here is Rothschild’s argument. Above, we assumed that the epistemic utilities of true beliefs in different propositions are the same, and similarly for false beliefs. But we might score attitudes to different propositions differently: $R_X$ for a true belief in $X$, $-W_X$ for a false belief in $X$; $R_Y$ for a true belief in $Y$, $-W_Y$ for a false belief in $Y$; and so on. For instance, if $X$ concerns the correct fundamental theory of physics, I might set $R_X = 10, W_X = 20$, while if $Y$ concerns the number of blades of grass in Hyde Park, I might set $R_Y = 1, W_Y = 2$. This might reflect the greater importance of $X$ than $Y$. Now, if $\frac{W_X}{R_X} = \frac{W_Y}{R_Y}$, for any two propositions $X, Y$, we say that the epistemic utilities have *uniform ratio*. And in that case the Lockean threshold is the same for each proposition if we maximize expected utility. But what about Dominance? Rothschild proves the following result:

> **Dominance Theorem for Almost Lockean Completeness for Belief Sets (Rothschild 2021)[^rothschild-2021]** A belief set satisfies Almost Lockean Completeness iff there is no set of epistemic utilities with uniform ratio under which the pair is strongly dominated.

I sketch the proof in the supplementary materials.

One issue with this argument: To extract Almost Lockean Completeness from the Dominance Theorem for Almost Lockean Completeness, a decision-theoretic norm is needed. It would say that it’s irrational to be dominated relative to *any* set of epistemic utilities that have uniform ratio. But this norm is not compelling. Why care about being dominated relative to epistemic utilities that are not your own?

### 4.4 Updating your beliefs when you receive evidence

All the norms we have considered so far in this entry have been synchronic: that is, they say what rationality requires of your beliefs at a given time. In this section, we turn to diachronic norms: these say what rationality requires of the relationship between your beliefs at one time and your beliefs at another, typically when you learn some evidence between those times. We’ll look at two sets of norms for belief updating: AGM belief revision (Section 4.4.1) and Plan Lockean Revision (Section 4.4.2).

#### 4.4.1 AGM belief revision

AGM belief revision is a set of putative norms that govern full beliefs introduced by Carlos Alchourrón, Peter Gärdenfors, and David Makinson (1985); it includes both synchronic and diachronic norms (see entry on the logic of belief revision). The synchronic norms are these, and they apply both before and after you acquire new evidence:

> **Consistency** If $\mathbf{A}$ is an inconsistent set of finitely many propositions, then you should not believe each proposition in $\mathbf{A}$.
>
> **Closure** If $X$ is a logical consequence of the propositions in $\mathbf{A}$, then you should not believe each proposition in $\mathbf{A}$ while not believing $X$.

We’ve already seen that we cannot give an argument for either of these from the point of view of epistemic utility. But perhaps we can do better with the diachronic norms. These norms govern a belief updating operator $\star$, which takes your belief set $\mathbf{B}$, together with a proposition $E$ that gives the evidence you learn, and returns $\mathbf{B} \star E$, which is your new belief set after you learn $E$. The AGM postulates state that the following are required by rationality:

> **Success** $E$ is in $\mathbf{B} \star E$. That is, after learning a proposition, you should believe it.
>
> **Inclusion** $\mathbf{B} \star E \subseteq \mathsf{Cn}(\mathbf{B} \cup \{E\})$, where $\mathsf{Cn}$ takes a set of propositions and returns its logical closure. That is, you should believe a proposition after learning only if it is a logical consequence of what previously believed and the proposition you learn.
>
> **Preservation** If $\mathbf{B}$ and $E$ are consistent, then $\mathbf{B} \subseteq \mathbf{B} \star E$. That is, if what you learn is consistent with what you previously believed, you shouldn’t drop your belief in anything you previously believed when you learn.
>
> **Extensionality** If $E$ and $F$ are logically equivalent, then $\mathbf{B} \star E = \mathbf{B} \star F$. That is, learning either of two logically equivalent propositions should change your beliefs in the same way.

As Shear and Fitelson (2019) show, we can justify Success, Inclusion, and Extensionality by appealing to Maximize Expected Epistemic Utility. To do this, we note that, as we’ll justify in Section 5.3, there is a standard norm that is taken to govern how we should update our credences in response to new evidence. It’s called Conditionalization and it says that, if you assign positive credence to a proposition $E$ and then learn $E$ for sure as evidence, then your new credence in a proposition $X$ should be your old conditional credence in $X$ given $E$, where that is defined to be the ratio of your credence in the conjunction of $X$ and $E$ to your credence in $E$ alone; or, in other words, it’s the proportion of your old credence in $E$ that you also assigned to $X$. So you might think that (i) you should set your original credences by maximising expected utility with respect to your original credences, and (ii) set your new credences after learning evidence by maximising expected utility with respect to your new credences, which are obtained from your old ones by updating on your evidence in line with Conditionalization. Doing this secures Success, Inclusion, and Extensionality. It doesn’t secure Preservation because learning a new proposition that is consistent with all the propositions to which you assigned credence higher than some threshold can lead you to drop your credence in one of those propositions below that threshold.

#### 4.4.2 Almost Lockean Completeness for Updating Plans

Patrick Rooyakkers (ms) has extended Rothschild’s argument for the Lockean Thesis so that it establishes a version of Almost Lockean Completeness but for combinations of belief sets and updating plans. The idea is this: Suppose you’re about to learn some new evidence. You don’t know what it is, but you know it will be one of the propositions $E_1, \ldots, E_k$, which together form a partition—that is, the propositions are exhaustive and mutually exclusive. Then, as well as your prior belief set, which we’ll call $\mathbf{B}$, you should have an updating plan in place for how you’ll respond to each of the possible pieces of evidence you might receive; for each $E_i$, this should give the belief set $\beta_{E_i}$ you plan to have if $E_i$ is the proposition you learn. Then the following norm governs this plan:

> **Almost Lockean Completeness for Plans with threshold $t$** Rationality requires that there is a probabilistic credence function such that:
>
> 1. If the unconditional credence it assigns to $X$ is greater than $t$, then $X$ is in $\mathbf{B}$; if it is less than $t$, then $X$ is not in $\mathbf{B}$;
> 2. For each $E_i$, if the conditional credence it assigns to $X$ given $E_i$ is greater than $t$, then $X$ is in $\beta_{E_i}$; if it is less than $t$, then $X$ is not in $\beta_{E_i}$.

That is, you are required to obey the Lockean Thesis with a particular threshold and some probabilistic credence function before you acquire the new evidence, and obey it with respect to some unconditional credences; and you are required to plan to obey it with the same threshold after you’ve received the evidence, and obey it then with respect to the conditional credences given the evidence you learn.

Rooyakkers’ argument has the same form as Rothschild’s. He proves the following on the assumption that the epistemic utility at a world of a pair consisting of a prior belief set and a belief plan should be the sum of the epistemic utility of the prior belief set at that world and the epistemic utility of the posterior belief set that the plan endorses if you learn the proposition in the partition that is true at that world:

> **Dominance Theorem for Almost Lockean Completeness for Plans (Rooyakkers ms)** A prior belief set and a belief plan together satisfy Almost Lockean Completeness for Plans iff there is no set of epistemic utilities with uniform ratio under which the pair is strongly dominated.

## 5. Epistemic Utility Arguments for Precise Credences

In the precise credence model, we represent an individual’s epistemic state by their *credence function*, which takes each proposition in their agenda and returns a real number at least 0 and at most 1, which measures the strength of their belief, or their degree of confidence, in that proposition. In mathematical notation, $C : \mathcal{F} \rightarrow [0, 1]$.

We’ll meet the norm of Probabilism below, but it will be helpful to say here what it means for a credence function to be probabilistic, so that we can use that notion in the coming section. Suppose $C$ is a credence function defined on the agenda $\mathcal{F}$. Then, if $\mathcal{F}$ is an algebra, *$C$ is probabilistic* if

- Normality: $C(\top) = 1$, if $\top$ is a tautology; and $C(\bot) = 0$, if $\bot$ is a contradiction.
- Finite Additivity: $C(X \vee Y) = C(X) + C(Y)$, for all mutually exclusive $X$ and $Y$ in $\mathcal{F}$.

Another piece of terminology that will be useful below. A *mixture* of a sequence of credence functions is a weighted sum of them. That is, given a sequence of credence functions, $C_1, \ldots, C_n$ and a sequence of weights $0 \leq \lambda_1, \ldots, \lambda_n \leq 1$ that sum to 1, we define the mixture of these credence functions with these weights to be $\lambda_1C_1 + \ldots + \lambda_nC_n$, where, for each $X$, $$(\lambda_1C_1 + \ldots + \lambda_nC_n)(X) = \lambda_1C_1(X) + \ldots + \lambda_nC_n(X)$$ The *straight mixture* of $C_1, \ldots, C_n$ is the mixture in which each receives the same weight. If each of a sequence of credence functions is probabilistic, so is any mixture of them.

### 5.1 Epistemic utility functions for precise credences

An epistemic utility function for the states considered in the precise credence model takes a credence function on an agenda and a state of the world relative to that same agenda, and returns a real number or $-\infty$ or $\infty$ that measures the epistemic utility of that credence function at that state of the world. One of the most popular epistemic utility functions is the *Brier score*. To define it, we first define a measure of the epistemic utility of a single credence in a single proposition, and then use that to generate a measure of the epistemic utility of an entire credence function on an agenda. Measures of the epistemic utility of a single credence are known as *scoring rules*. Suppose $s$ is a scoring rule. Then, given a credence $p$:

- $s(1, p)$ gives the epistemic utility of having credence $p$ in a true proposition;
- $s(0, p)$ gives the epistemic utility of having credence $p$ in a false proposition.

Here’s the *quadratic scoring rule*:

- $q(1, p) = -(1-p)^2$
- $q(0, p) = -p^2$

One way to understand this: If a proposition is true, then credence 1 is the ideal credence in it; if it’s false, then credence 0 is the ideal. The quadratic scoring rule says that the epistemic *dis*utility of a credence is the square of the difference between it and the ideal, and the epistemic utility is the negative of that. So the epistemic utility of a credence is its proximity to the ideal credence for a particular way of measuring distance.

The *Brier score* of an entire credence function is then defined to be the sum of the quadratic scores of the credences it assigns. So: $$ B(C, w) = \sum_{X \in \mathcal{F}} q(V_w(X), C(X)) = -\sum_{X \in \mathcal{F}} (V_w(X) - C(X))^2 $$ where $V_w(X) = 1$ if $X$ is true at $w$, and $V_w(X) = 0$ if $X$ is false at $w$. We might think of $V_w$ as the ideal or omniscient credence function at world $w$.

The quadratic score and the Brier score have certain properties that are important in epistemic utility arguments concerning precise credences:

First, properties of scoring rules:

> **Continuity (for scoring rules)** We say that a scoring rule $s$ is *continuous* if $s(1, p)$ and $s(0, p)$ are both continuous functions of $p$ on $[0, 1]$.
>
> **Strict Propriety (for scoring rules)** We say that a scoring rule $s$ is *strictly proper* if, for any $0 \leq p \leq 1$, $$ ps(1, x) + (1-p)s(0, p) $$ is maximized uniquely at $x = p$. (That is, each probability expects itself to be best, epistemically speaking.)

Second, properties of epistemic utility functions:

> **Continuity (for epistemic utility functions)** We say that an epistemic utility measure $EU$ is *continuous* if $EU(C, w)$ is a continuous function of $C$ on the set of credence functions defined on the same agenda.
>
> **Strict Propriety (for epistemic utility functions)** We say that an epistemic utility measure $EU$ is *strictly proper* if, for any probabilistic credence function $P$ defined on $\mathcal{F}$, $$ \sum_{w \in \mathcal{W}_\mathcal{F}} P(w)EU(C, w) $$ is maximized uniquely, among credence functions defined on $\mathcal{F}$, at $C = P$. (That is, each probabilistic credence function expects itself to be best, epistemically speaking.)
>
> **Extensionality (for epistemic utility functions)** We say that an epistemic utility measure $EU$ is *extensional* if, whenever $C$ is a probability function on $\mathcal{F}$, and $\pi$ is a permutation of the worlds in $\mathcal{W}_\mathcal{F}$, then $EU(C, w) = EU(\pi(C), \pi(w))$, where $\pi(C)(w) = C(\pi(w))$.
>
> **Additivity (for epistemic utility functions)** We say that an epistemic utility measure $EU$ is *additive* if, for each $X$ in $\mathcal{F}$, there is a scoring rule $s_X$ such that
>
> $$ EU(C, w) = \sum_{X \in \mathcal{F}} s_X(V_w(X), C(X)) $$
>
> (That is, the epistemic utility of an entire credence function is the sum of the epistemic utilities of the individual credences, where these can be given by different scoring rules for each proposition in the agenda.)

Suppose $EU$ is additive. Then (i) $EU$ is continuous iff each $s_X$ is continuous; and (ii) $EU$ is strictly proper iff each $s_X$ is strictly proper.

A detailed discussion of the various arguments for using scoring rules and epistemic utility functions that have these properties claims can be found in the [supplementary materials](epistemic-utility.char-ep-ut-cred.md). They roughly divide into two sorts:

The first sort of argument is based on a veritist account of epistemic value, which says that the sole fundamental source of epistemic value is what Joyce (1998) calls *gradational accuracy*. The idea is that a credence in a true proposition is more accurate, and therefore more valuable, epistemically speaking, the higher it is, while a credence in a false proposition is more accurate, and thus epistemically more valuable, the lower it is. Put another way, the ideal credence function to have at a world is the omniscient credence function at that world, which assigns maximal credence to all the truths and minimal credence to all the falsehoods; and your credence function is more accurate, and therefore epistemically more valuable, the closer it lies to this ideal. So, for veritists, epistemic utility functions measure the accuracy of a credence function, and characterizing the legitimate epistemic utility functions is characterizing the legitimate ways of measuring accuracy.

Joyce (1998) offers one such characterization, based on a series of axioms he justifies individually. Leitgeb and Pettigrew (2010) offer an argument for the Brier score based on the requirement to avoid a certain sort of rational dilemma. D’Agostino and Sinigaglia (2010) offer another argument for that epistemic utility function based on the idea that accuracy is proximity to the ideal credence function. Pettigrew (2016) also thinks of accuracy that way, but offers an argument for additive and continuous strictly proper epistemic utility functions, based on a suggestion by Frank P. Ramsey (1926 [1931]) that connects accuracy and calibration, and Williams and Pettigrew (2023) improve on that characterization. Based on a pragmatic understanding of accuracy, where the utility of a credence is the pragmatic utility it obtains for you through the practical decisions it leads you to make, Levinstein (2017) builds on technical results by Mark J. Schervish (1989) to characterize the additive and continuous strictly proper scoring rules. And building on a suggestion by Sophie Horowitz (2017) that the epistemic value of a credence function is the quality of the educated guesses that it would license you to make were you faced with a forced choice between guessing various propositions, Gabrielle Kerbel (ms.) takes the accuracy of a credence to be the average quality of the guesses your credence licenses across a large range of forced choices it might be used to make, and shows that this generates an additive and continuous strictly proper epistemic utility function.

The second sort of argument does not commit to a particular account of epistemic value. Rather, it argues directly that, whatever is the source of epistemic value, measures of it should have certain properties. For instance, Joyce (2009) argues that measures of epistemic value should be strictly proper as follows: If a measure of epistemic utility is not strictly proper, then there is a probabilistic credence function that doesn’t expect itself to be best, epistemically speaking. Because of this, that credence function cannot be the unique rational response to any evidence, because it thinks of an alternative as equally good, and so someone with that credence function could rationally move to the alternative. But, for any probabilistic credence function, there is a body of evidence to which it is the unique rational response. So we have a contradiction. Therefore, every legitimate measure of epistemic utility is strictly proper. Hájek (2008) criticizes this argument and Pettigrew (2016) defends Joyce.

We now move to some general objections to these characterizations of epistemic utility functions.

#### 5.1.1 The Varying Importance Objection

According to Additivity, which is assumed by many of the accounts of epistemic utility, the epistemic utility of a whole credence function is the sum of the epistemic utilities of the individual credences it comprises; and which scoring rule measures the epistemic utility of a credence in a proposition at a world can depend on the proposition, but not on the world. This allows the veritist, for instance, to accommodate the fact that the accuracy of some propositions is more important to us than the accuracy of others: I might take the accuracy of a proposition about how many blades of grass there are on my lawn to be less important than a proposition about the fundamental constants of the universe. In such a case, I can simply take the accuracy of a credence function to be a weighted sum of the epistemic utilities of the individual credences, with greater weight given to the propositions whose accuracy is more important to me. But Ben Levinstein (2018) argues that the importance of a proposition does sometimes depend on which world we inhabit: in worlds where I meet a particular person and fall in love with them, propositions that concern their well-being have great importance to me, and the epistemic utility of my credences in those propositions should contribute greatly to the epistemic utility of my whole credence function; in worlds where I never meet that person, on the other hand, the importance of these propositions is much diminished, as is the contribution of the epistemic utility of my credences in them to my total epistemic utility. And so the weights we assign to the scores of the individual credences must also depend on the worlds; something that Additivity rules out. And Levinstein shows further that, if we do allow the weights to vary with the worlds, the resulting measure of epistemic utility is no longer strictly proper, and indeed the argument from Dominance to Probabilism that we’ll discuss in Section 5.2 fails if we use it.

#### 5.1.2 The Verisimilitude Objection

Graham Oddie (2019) has argued that there is a source of epistemic value that cannot be captured by any of the epistemic utility functions that satisfy the conditions described above; this is the virtue of *verisimilitude* (see entry on truthlikeness). His point is most easily introduced by an example. Suppose I am interested in how many stars there are on the flag of Suriname. I have credences in three propositions: *One*, *Two*, and *Three*. In fact, there is exactly one star on the flag, so *One* is true at the actual world, while *Two* and *Three* are false. Now consider two different credence functions on these three propositions:

$$ \begin{array}{r|ccc} & \textit{One} & \textit{Two} & \textit{Three} \\ \hline C & 0 & 0.5 & 0.5 \\ C' & 0 & 1 & 0 \end{array} $$

So, $C$ and $C'$ both assign credence 0 to the true proposition, *One*; they are certain that there are either two or three stars on the flag, but while $C$ spreads its credence equally over these two false options, $C'$ is certain of the first. According to Oddie, $C'$ has greater truthlikeness than $C$ at the actual world because it assigns a higher credence to a proposition that, while false, is more truthlike, namely, *Two*, and it assigns a lower credence to a proposition that is, while also false, less truthlike, namely, *Three*. On this basis, he argues that any measure of epistemic disutility must judge $C$ to be worse than $C'$. However, he notes, nearly all measures of gradational accuracy endorsed in epistemic utility theory will not judge in that way: they will judge $C'$ worse than $C$. And indeed those that do so judge will fail to respect truthlikeness in other ways. Jeffrey Dunn (2018) and Miriam Schoenfield (2019) respond to Oddie’s arguments.

#### 5.1.3 The Numerical Representability Objection

We have considered a number of different characterizations of the legitimate ways of measuring epistemic utility. Each has assumed that the measures of these quantities are numerically representable; that is, each assumes it makes sense to use real numbers to measure these quantities. Conor Mayo-Wilson and Greg Wheeler call this assumption into question (Mayo-Wilson & Wheeler, ms.). They argue that, in order to represent a quantity numerically, you need to prove a representation theorem for it in measurement theory. And, if you wish to use that quantity as a measure of utility, or as a component of a measure of utility, you need to prove a representation theorem not only for the quantity itself, but for its use in expected utility calculations. They note that this was the purpose of the representation theorems of von Neumann & Morgenstern as well as Savage and Jeffrey (see entry on normative theories of rational choice: expected utility). And they argue that the methods that these authors use are not available to the proponent of epistemic utility arguments.

### 5.2 Epistemic utility arguments for Probabilism

Following the structure of epistemic utility arguments described in Section 2, the arguments for Probabilism have three components: an account of epistemic utility, which specifies a range of legitimate measures of that quantity; a decision-theoretic norm; and a mathematical theorem that derives the epistemic norm from the decision-theoretic norm when the options are credence functions and utility is epistemic utility.

> **Probabilism** Rationality requires that your credence function at any given time is probabilistic.

Probabilism is one of a handful of norms that characterize the Bayesian view in credal epistemology. The epistemic utility arguments in its favor appeal to a slight weakening of the Dominance norm to which we appealed above. We say that one option *strongly dominates* another if it is better at all possible states of the world, and we say it *weakly dominates* if it is at least as good at all states of the world and better at some.

> **Undominated Dominance** If one option is strongly dominated by another that isn’t itself even weakly dominated, then rationality requires that you should not adopt the first.

As before, we also appeal to a mathematical theorem to derive Probabilism from the account of epistemic utility and the decision-theoretic norm. The strongest theorem in the area is this:

> **Dominance Theorem for Probabilism (de Finetti 1974; Savage 1971; Predd, et al. 2009; Pettigrew 2022; Nielsen 2022)[^finetti-1974][^nielsen-2022][^pettigrew-2022]** Suppose our epistemic utility function is continuous and strictly proper. Then
>
> 1. Every non-probabilistic credence function defined on a particular agenda is strongly dominated by a probabilistic credence function defined on that agenda.
> 2. No probabilistic credence function defined on a particular agenda is even weakly dominated by any credence function defined on that agenda.

See the supplementary materials for a sketch of how the proof of (i) follows from the Dominance Theorem for Convex Hulls.

So, we have the following argument for Probabilism:

> **Continuity** + **Strict Propriety (for epistemic utility functions)**
>
> **Undominated Dominance**
>
> Therefore,
>
> **Probabilism**

We now turn to objections to this argument.

#### 5.2.1 The Different Dominators Objection

Many of the existing characterizations of the legitimate epistemic utility functions characterize a family of such measures; they do not narrow the field to a single epistemic utility function. But, for all that the Dominance Theorem for Probabilism tells us, it may well be that, for a given non-probabilistic credence function, different epistemic utility functions in such a family give different sets of credence functions that dominate it. Thus, an agent with a non-probabilistic credence function might be faced with a range of alternative credence functions, each of which dominates theirs relative to a different legitimate epistemic utility function. Moreover, it may be that any credence function that dominates their credence function relative to one epistemic utility function does not dominate it relative to another; indeed, it may be that any credence function that dominates theirs relative to the first risks very high epistemic disutility at some world relative to the second, and *vice versa*. In this situation, it is plausible that the agent is rationally permitted to stick with her non-probabilistic credence function. This objection was originally raised by Aaron Bronfman in unpublished work, and it has been discussed by Hájek (2008) and Pettigrew (2010, 2013b)

#### 5.2.2 Evidence and Accuracy

According to Undominated Dominance, a dominated option is only ruled irrational in virtue of being dominated if at least one of the options that dominate it is not itself dominated. But there may be other features that a credence function might have besides itself being dominated such that being dominated by that credence function does not entail irrationality. Kenny Easwaran and Branden Fitelson (2012) suggest such a feature. Suppose that your credence function is non-probabilistic, but it matches the evidence that you have: that is, the credence it assigns to a proposition matches the extent to which your evidence supports that proposition. And suppose that none of the credence functions that dominate your credence function have that feature. Then, we might say, the fact that your credence function is dominated does not rule it irrational. For instance, suppose that a trick coin is about to be tossed. Your evidence tells you that the chance of it landing heads is 0.7. Your credence that it will lands heads is 0.7 and your credence that it will land tails is 0.6. Then you might think that your credences match your evidence, because you have evidence only about it landing heads and your credence that it will land heads equals the known chance that it will land heads. However, it turns out that all of the credence functions that dominate your credence function fail to match this evidence, when epistemic utility is measured by the Brier score: that is, they assign credence other than 0.7 to the coin landing heads. Pettigrew (2014a) and Joyce (2018) respond to this objection on behalf of the dominance argument for Probabilism.

#### 5.2.3 Dominance and Act-State Dependence

The final objection to the argument begins with the following sort of case (Greaves 2013; Caie 2013; Campbell-Moore 2015)[^caie-2013][^campbell-moore-2015][^greaves-2013]:

> **Thwarted Accuracy** Suppose I can read your mind. You have opinions only about two propositions, $X$ and $\neg X$. And suppose that I have control over the truth of $X$ and $\neg X$. I decide to do the following. First, define the non-probabilistic credence function $C^\dag(X) = 0.8$ and $C^\dag(\neg X) = 0.1$. Then:
>
> 1. If your credence function is $C^\dag$, I will make $X$ true (and thereby make your credence function very accurate);
> 2. If your credence function is not $C^\dag$ and your credence in $X$ is greater than 0.5, I will make $X$ false (and thereby make your credence function rather inaccurate);
> 3. If your credence function is not $C^\dag$ and your credence in $X$ is at most 0.5, I will make $X$ true (and thereby make your credence function rather inaccurate).

Now $C^\dag$ is not probabilistic, so there are credence functions that are more accurate than $C^\dag$ whether $X$ is true or false. However, because of the way I will manipulate the world in response to your credences about it, if you adopt anything other than $C^\dag$, you’ll end up less accurate. In such a case, it seems rationality doesn’t require us to have probabilistic credences. The culprit here is Undominated Dominance. It is only plausible in cases in which the options between which the agent is choosing will not influence the way the world is if they are adopted. Such situations are sometimes called situations of *act-state independence*.

There are three responses available here: the first is to bite the bullet, accept the restriction to Undominated Dominance, and therefore accept a restriction on the cases in which Probabilism holds; the second is to argue that the practical case and the epistemic case are different, with different decision-theoretic principles applying to each; the third, of course, is to abandon the accuracy argument for Probabilism. Joyce (2018) and Pettigrew (2018a) argue for the first response. They advocate different decision-theoretic principles to replace Undominated Dominance in the epistemic case: Joyce advocates standard causal decision theory together with a Ratifiability condition (Jeffrey 1983)[^jeffrey-1983]; Pettigrew omits the ratifiability condition. But they both agree that these principles will agree with Undominated Dominance in cases of act-state independence; and they agree with the verdict that $C^\dag$ is the only credence function that isn’t ruled out as irrational in Thwarted Accuracy. Konek and Levinstein (2019) argue for the second response, claiming that, since doxastic states and actions have different directions of fit, different decision-theoretic principles will govern them; and Kurt Sylvan (2020) can be read as arguing for the same conclusion on the basis of his claim that, while accuracy is the fundamental source of value for epistemic states like credences, it is a value to which the appropriate response is *respect*, not *promotion*. They hold that Undominated Dominance is the correct principle when the options are credence functions, even though it is not the correct principle when the options are actions. Caie (2013) and Berker (2013a,b), on the other hand, argue for the third option.

#### 5.2.4 Epistemic expansions

The Dominance Theorem for Probabilism states: for epistemic utility functions of a particular sort, every non-probabilistic credence function defined on a particular agenda is dominated by an alternative probabilistic credence function, *defined on that same agenda*, that is itself not dominated by a further alternative *defined again on the same agenda*. But you might think that this is still not sufficient to establish Probabilism. After all, while the dominating credence function is not itself dominated by an alternative credence function defined on the same agenda, it might be dominated by an alternative credence function defined on a different agenda. For instance, take the non-probabilistic credence function $C^*$ defined on $\mathcal{F} = \{X, \neg X\}$, where $C^*(X) = 0.6 = C^*(\neg X)$. Relative to the Brier score, it is dominated by $C'(X) = 0.5 = C'(\neg X)$. But $C'$ is Brier dominated by $C^\dag$ defined on $\mathcal{F}^\dag = \{X\}$, where $C^\dag(X) = 0.5$.

A natural reaction to this is to define the epistemic utility of a credence function to be the average epistemic utility of the credences it assigns, rather than the total epistemic utility. For instance, just as the Brier score is the total quadratic score of the credences it assigns, we can define the *average Brier score* of a credence function to be the average quadratic score of the credences it assigns. Now, relative to the average Brier score, $C^*$ is indeed dominated by $C'$ and $C'$ is not dominated by $C^\dag$. But $C'$ is dominated by $C^+$ defined on $\mathcal{F}^+ = \{\top\}$, where $C^+(\top) = 1$. Jennifer Carr (2015) initiated the investigation into how epistemic utility arguments for Probabilism might work when we start to compare credence functions defined on different agendas. She notes the analogy with population axiology in ethics (see entry on the repugnant conclusion). Pettigrew (2018b) takes this analogy further, proving an impossibility result analogous to those prevalent in that part of ethics, and Brian Talbot (2022) presses the objection based on this problem further.

#### 5.2.5 Infinite probability spaces

In the final two parts of this section, we ask what happens to the argument for Probabilism when (i) we allow for infinite agendas and (ii) we allow the logic of the propositions in those agendas to be non-classical.

We have assumed throughout that the set of propositions on which an agent’s credence function is defined is finite. What happens when we lift this restriction? The first problem is that we need to say how to measure the epistemic utility of a credence function defined over an infinite set of propositions. Then, having done that, we need to say which such credence functions are dominated relative to these measures, and which aren’t.

Sean Walsh has described an extension of the Brier score to the case in which the set of propositions to which we assign credences is countably infinite; and he has shown that non-probabilistic credence functions on such sets are dominated relative to that measure, while probabilistic ones are not. (For a description of Walsh’s unpublished work, see Kelley 2019)[^kelley-2019]. Mikayla Kelley (2019) has then gone considerably further and generalized Walsh’s results significantly by describing a wide range of possible epistemic utility functions and characterizing the undominated credence functions defined on sets of propositions of different varieties; and Michael Nielsen (2023) has generalized them in a different direction.

#### 5.2.6 Non-classical logic

In all of the arguments we’ve surveyed above, we have assumed that classical logic governs the propositions to which our agent assigns credences. This secures Probabilism, which demands, among other things, that an agent assign maximal credence to every classical tautology. But what happens if we drop this assumption? What if, instead, the propositions are governed by a three-valued logic, such as strong Kleene logic or the Logic of Paradox (see entry on many-valued logic)? In a series of papers, Robbie Williams (2012a,b, 2018) has built on mathematical results by Jeff Paris (2001) and Jean-Yves Jaffray (1989) to understand what norms of credence the epistemic utility arguments establish in this case. I’ll give a single example here to illustrate.

Strong Kleene logic has three truth values: True, False, and Neither. Our first question is this: what is the ideal credence in a proposition that is neither true nor false? Williams argues that it should be zero. And then he shows that, if the epistemic utility of a credence at a world is its proximity to the ideal credence at that world, and we measure the distance of one credence to another as the square of the difference between them, as we do to generate the quadratic scoring rule in the classical case, then the credence functions that are not dominated are precisely those that satisfy the norm of Generalized Probabilism:

> **Generalized Probabilism** Suppose $\models$ is the logical consequence relation of the correct logic. Rationality requires that your credence function $C$ at a given time should be a generalized probability function for that logic. That is:
>
> 1. If $\bot \models$, then $C(\bot) = 0$.
> 2. If $\models \top$, then $C(\top) = 1$.
> 3. If $X \models Y$, then $C(X)\leq C(Y)$.
> 4. $C(X \vee Y) = C(X) + C(Y) - C(X \wedge Y)$.

Note that, if $\models$ is classical, then Generalized Probabilism is equivalent to Probabilism.

Williams (2018) also considers the case in which you are uncertain which logic governs the propositions you consider, and Pettigrew (2021) draws on a suggestion by Ian Hacking (1967) in a different context to explore the case in which you know that the logic is classical, but you don’t know all the logical facts.

### 5.3 Epistemic utility arguments for chance-credence norms

In this section, we consider epistemic utility arguments for norms that govern the relationship between the credences you assign to propositions concerning objective chances and credences you assign to propositions to which the objective chances assign probabilities: so, for instance, the relationship between your credence in the proposition that the chance of rain tomorrow is 76% and the proposition that it will rain tomorrow (see entry on chance and randomness). The most well-known principle of this kind is the one that David Lewis calls the Principal Principle (1980). To state it, we use the following notation: if $ch$ is a probability function, we write $\rho_{ch}$ for the proposition that says that $ch$ gives the objective chances. Then:

> **The Principal Principle** Rationality requires that, if $C(\rho_{ch}) \gt 0$, and $E$ is your total evidence, then $C(X \mid \rho_{ch}) = ch(X \mid E)$, for all $X$ in your agenda.

So, for instance, your credence that it should rain tomorrow conditional on the chance of rain tomorrow given all your evidence being 76% should be 0.76.

Now, as Lewis pointed out, this norm has implausible consequences if the objective chance function might be *modest in the presence of the body of evidence $E$*: that is, if the true chances might be uncertain, given $E$, that they give the true chances; that is, if there is a probability function $ch$ that might give the chances for which $ch(\rho_{ch} \mid E) \lt 1$. After all, by the Principal Principle, if $C(\rho_{ch}) \gt 0$, then $C(\rho_{ch} \mid \rho_{ch}) = ch(\rho_{ch} \mid E) \lt 1$, but by the definition of conditional probability, $C(\rho_{ch} \mid \rho_{ch}) = 1$. Contradiction. So $C(\rho_{ch}) = 0$. That is, if some of the possible chance functions are modest in the presence of our evidence, we must give them zero credence. And, as Lewis argued, the chances posited by his account, which is known as Humeanism, will indeed be modest in this sense, because they will give some positive probability to the world being so different that its chances are also different (Lewis 1980; see Section 3.6 of the entry on Interpretations of Probability)[^lewis-1980].

Nonetheless, if we assume that the chances are not modest, which is a natural consequence of many non-Humean theories of chance, then we can give an epistemic utility argument for the Principal Principle (Pettigrew 2013, 2022). In the first premise, we assume Continuity and Strict Propriety (for epistemic utility functions)—either because credal veritism is true and the legitimate measures of accuracy are continuous and strictly proper, or for other reasons. For the second premise, we assume the following decision-theoretic norm, where we say that one option *strongly chance dominates another in the presence of $E$* if every possible chance function, conditional on $E$, gives higher expected utility to the first than to the second, and we say that one option *weakly chance dominates another in the presence of $E$* if every possible chance function, conditional on $E$, gives at least as high expected utility to the first than to the second, and at least one possible chance function, conditional on $E$ gives strictly higher expected utility to the first than to the second:

> **Undominated Chance Dominance** If one option is strongly chance dominated by an alternative in the presence of your total evidence, and that alternative is not weakly chance dominated by anything in the presence of your total evidence, then rationality requires you not to choose the first.

And then we appeal to the following corollary of the Chance Dominance Theorem for the General Chance-Credence Norm, which we state below, to derive the Principal Principle:

> **Chance Dominance Corollary for the Principal Principle** Suppose your epistemic utility function is continuous and strictly proper. And suppose no possible chance function is modest in the presence of your evidence. Then:
>
> 1. If a credence function does not satisfy Probabilism + Principal Principle, there is an alternative credence function that does satisfy Probabilism + Principal Principle such that the latter strongly chance dominates the former in the presence of your total evidence;
> 2. If a credence function does satisfy Probabilism + Principal Principle, there is no alternative credence function that even weakly chance dominates it in the presence of your total evidence.

So, we have:

> **Continuity + Strict Propriety (for epistemic utility functions)**
>
> **Undominated Chance Dominance**
>
> Therefore,
>
> **Probabilism + Principal Principle**

Now, this argument does not fully justify the Principal Principle. A full justification would also justify Undominated Chance Dominance by explaining why chances are so special that rationality requires us to reject an option when the possible chance functions unanimously reject it. But what the justification does tell us is how we should respond rationally to this deference we owe to the chances. After all, there are alternative ways we might respond: we might say, for instance, that your credence in $X$ conditional on the chance of $X$ being greater than the chance of $Y$ should be greater than your credence in $Y$ conditional on that same chance fact. So the argument does give us something.

So far, we’ve assumed that chances are not modest. But in fact we can still say something if they are. To state the next result, we need to introduce a little terminology:

- a set of credence functions is *convex* if, whenever two credences functions are in it, so is any mixture of them;
- a set of credence functions is *closed* if, whenever there is an infinite sequence of credence functions in it and they approach arbitrarily close to another credence function in the limit, then the credence function they approach is also in the set;
- the *closed convex hull* of a set of credence functions is the smallest closed and convex set that contains it; that is, for any other set of credence functions that is closed and convex and contains that set, the closed convex hull is a subset of it.

> **Chance Dominance Theorem for Chance-Credence Norms (Pettigrew 2022, Nielsen 2022)[^nielsen-2022][^pettigrew-2022]** Suppose your epistemic utility function is continuous and strictly proper. Then:
>
> 1. If your credence function does not lie in the closed convex hull of the set of possible chance functions conditional on your evidence, then there is an alternative credence function that does lie in that closed convex hull such that the latter strongly chance dominates the former;
> 2. If your credence function does lie in the closed convex hull of the set of possible chance functions conditional on your evidence, then there is no alternative credence function that weakly chance dominates it.

See the supplementary materials for a sketch of how the proof of (i) follows from the Dominance Theorem for Convex Hulls.

Together with Continuity + Strict Propriety (for epistemic utility functions) and Undominated Chance Dominance, this tells us that rationality requires us to have a credence function that lies in the closed convex hull of the possible chance functions. Now of course that isn’t a terribly intuitive condition. However, for various properties weaker than immodesty that chance functions might all have, this does entail that your credence function should also have that property as well: all that is required is that, whenever two credence functions have the property, any mixture of them does as well. Here are two such properties:

- $C$ is *chance expectational in the presence of $E$* if, for all $X$ in $\mathcal{F}$, $$ C(X) = \sum_{ch} C(\rho_{ch})ch(X \mid E) $$
- $C$ *trusts the chances in the presence of $E$* if, for all $X$ in $\mathcal{F}$, $$ C(X \mid ch(X \mid E) \geq x) \geq x $$

Both are preserved under taking mixtures and so the Chance Dominance Theorem for Chance-Credence Norms gives arguments for the following two chance-credence principles, if the chances have the appropriate properties:

- **General Recipe (Ismael 2008)[^ismael-2008]** Rationality requires you to have a credence function that is chance expectational in the presence of your total evidence.
- **Chance Trust Principle (Levinstein 2023)[^levinstein-2023]** Rationality requires you to trust the chances in the presence of your total evidence.

However, Levinstein and Spencer (ms.) argue that the sort of Humean account of chance that posits modest chance functions will also posit chance functions that are neither chance-expectational nor trusting of themselves as chances. So, for such accounts, these arguments for the weaker chance-credence principles will not work.

Levinstein (2023) offers a different epistemic utility argument for the Chance Trust Principle. Undominated Chance Dominance is intended to capture the claim that rationality requires us to defer to the chances, and proposes a precise formulation of that demand. Levinstein offers a different formulation. To defer to the chances epistemically is to expect them to have greater expected epistemic utility than you expect yourself to have (unless you are certain your credences match the chances, in which case you expect them to have exactly as much epistemic utility as you expect yourself to have). And, what’s more, you expect this regardless of the epistemic utility function you use: provided it satisfies Additivity, Continuity, and Strict Propriety, if you’re uncertain what the chances are, you should expect them to do better than you expect your own credences to do. And, Levinstein shows, if you do defer in this way, then you satisfy the Chance Trust Principle.

### 5.4 Epistemic utility arguments for Conditionalization

So far, we have been concerned with the so-called synchronic norms of credence, that is, those that govern your credences at a particular time. In this section, we turn to what are at least apparently diachronic norms, that is, those that govern the relationship between your credences at different times. The most well-known such norm is Conditionalization, or Bayes’ Rule, which roughly tells you how you should update your credences upon receiving some new evidence, when that new evidence comes in the form of a proposition learned with certainty.

> **Diachronic Conditionalization** Suppose $C$ is your credence function at an earlier time $t$ and $C'$ is your credence function at a later time $t'$ and suppose that, between $t$ and $t'$ the strongest proposition you learn is $E$, then rationality requires that, if $C(E) \gt 0$, then for all $X$ in $\mathcal{F}$, $$ C'(X) = C(X \mid E) = \frac{C(X\ \& \ E)}{C(E)} $$ That is, at the later time, your unconditional credence in a proposition should be equal to your earlier credence in it conditional on the strongest proposition you learned in the interim. If it is, we say that your posterior is obtained from your prior by conditioning on your new evidence.

In fact, however, the original epistemic utility arguments in this area did not attempt to establish Diachronic Conditionalization directly. Rather, they attempted to establish that, when you know at the earlier time that the evidence you’ll receive will come from a particular partition, then you should plan to update as Diachronic Conditionalization demands. There are in fact two versions of the resulting norm, depending on the scope of the rationality operator (Greaves & Wallace 2006; Briggs & Pettigrew 2020)[^briggs-2020][^greaves-2006].

> **Partitional Plan Conditionalization (narrow scope)** If
>
> - $C$ is your credence function at an earlier time $t$,
> - the propositions $E_1, \ldots, E_n$ form a partition,
> - between $t$ and $t'$, you’ll learn which $E_i$ is true, and nothing more,
> - you plan to update as follows: if you learn $E_i$, then you’ll adopt $R_{E_i}$ as your credence function at $t'$,
>
> then rationality requires that, if $C(E_i) \gt 0$, then for all $X$ in $\mathcal{F}$,
>
> $$ R_{E_i}(X) = C(X \mid E_i) = \frac{C(X\ \& \ E_i)}{C(E_i)} $$

This says that, if $C$ is your prior, rationality requires you to plan to update upon receipt of new evidence by conditioning $C$ on that evidence.

> **Partitional Plan Conditionalization (wide scope)** Rationality requires that: if
>
> - $C$ is your credence function at an earlier time $t$,
> - the propositions $E_1, \ldots, E_n$ form a partition,
> - between $t$ and $t'$, you’ll learn which $E_i$ is true, and nothing more,
> - you plan to update as follows: if you learn $E_i$, then you’ll adopt $R_{E_i}$ as your credence function at $t'$,
>
> then, if $C(E_i) \gt 0$, then for all $X$ in $\mathcal{F}$,
>
> $$ R_{E_i}(X) = C(X \mid E_i) = \frac{C(X\ \& \ E_i)}{C(E_i)} $$

This says that rationality requires you not to have prior $C$ and yet plan to update upon receipt of new evidence in some way other than by conditioning $C$ on that new evidence.

#### 5.4.1 Epistemic utility arguments for Partitional Plan Conditionalization

We begin with arguments for Partitional Plan Conditionalization.

The first is due to Hilary Greaves and David Wallace (2008), building on techniques from Peter M. Brown (1976) and Graham Oddie (1997). Some terminology:

- An *updating plan* is a function from states of the world to credence functions.
- An updating plan is *available* if it takes the same values at any two worlds at which your evidence will be the same.
- An updating plan is a *conditionalizing plan for a prior credence function* if, whenever you give positive credence to the evidence you’ll learn at a world, the plan tells you to update at that world by conditioning the prior on that evidence.

> **Expectation Theorem for Partitional Plan Conditionalization (narrow scope) (Greaves & Wallace 2008)** Suppose your epistemic utility function is strictly proper, and suppose your evidence will tell you which member of a particular partition is true. Then the updating plans that maximize expected epistemic utility from the point of view of your prior credence function among those available are exactly the conditionalizing plans for that prior.

I sketch the proof in the supplementary materials.

So, we have:

> **Strict Propriety**
>
> **Maximize Expected Utility**
>
> Therefore,
>
> **Partitional Plan Conditionalization (narrow scope)**

By asking about local updating plans, which say not which credence function you plan to adopt upon receiving new evidence, but just what credence you plan to assign to a particular proposition, Kenny Easwaran (2013) extends this argument to establish a version of van Fraassen’s (1999) Reflection Principle and a norm known as Conglomerability, which says that your unconditional credence in a proposition should lie in the range spanned by your conditional credences in it given different elements of a partition.

Maximize Expected Utility is a well-known norm of decision theory, but it is not universally accepted. Some decision theorists think that it is rationally permissible to take risk into account in ways that expected utility theory rules out. Building on a proposal by John Quiggin (1982), Lara Buchak (2013) has provided a popular alternative norm, Maximize Risk-Weighted Expected Utility, which allows you to take risk into account. Catrin Campbell-Moore and Bernhard Salow (2022) have explored an analogue of Greaves and Wallace’s argument that replaces Strict Propriety with its appropriately risk-sensitive analogue and replaces Maximize Expected Utility with Buchak’s risk-sensitive version. They show that these do not entail Partitional Plan Conditionalization, but rather an alternative updating norm.

The second argument for Partitional Plan Conditionalization is due to Ray Briggs and Richard Pettigrew (2020), with an improvement by Michael Nielsen (2021). They show that, assuming Additivity + Continuity + Strict Propriety, if you look not only at the epistemic utility of your updating plan, but at the sum of the epistemic utility of your prior and the epistemic utility of your updating plan, then if you violate Partitional Plan Conditionalization (wide scope), there is an alternative prior and updating plan you might have had instead that dominates yours.

> **Dominance Theorem for Partitional Plan Conditionalization (wide scope) (Briggs & Pettigrew 2020; Nielsen 2021)[^briggs-2020][^nielsen-2021]** Suppose your epistemic utility function is additive, continuous, and strictly proper measure. Then:
>
> 1. If your updating plan is available but it is not a conditionalizing plan for your prior, then there is an alternative prior and alternative available updating plan such that, at every state of the world, the sum of the epistemic utility of your prior and the epistemic utility of your updating plan is less than the sum of the epistemic utility of the alternative prior and the epistemic utility of the alternative updating plan.
> 2. If your updating plan is a conditionalizing plan for your prior, then there is no alternative prior and alternative updating plan such that, at every state of the world, the sum of the epistemic utility of your prior and the epistemic utility of your updating plan is less than the sum of the epistemic utility of the alternative prior and the epistemic utility of the alternative updating plan.

I sketch the proof in the supplementary materials.

So, we have:

> **Additivity + Continuity + Strict Propriety (for epistemic utility functions)**
>
> **Undominated Dominance**
>
> Therefore,
>
> **Partitional Plan Conditionalization (wide scope)**

#### 5.4.2 Epistemic utility arguments for Diachronic Conditionalization

We turn now to two arguments for Diachronic Conditionalization. Both take the same approach. You begin with your prior credence function at the earlier time. Between the earlier and later time you learn a proposition with certainty. Then, at the later time, you use your prior credence function to decide what your new posterior credence function should be. They differ in how they think that decision should be made.

According to Hannes Leitgeb and Richard Pettigrew (2010), you should pick the posterior credence function that maximizes expected epistemic utility from the point of view of your prior credence function, but where the expectation is taken over only those worlds at which the evidence is true. If your epistemic utility function is strictly proper, and if your prior assigns positive credence to the proposition you learn, then the unique posterior credence function that maximizes this is the one demanded by Diachronic Conditionalization.

Campbell-Moore and Salow (2022) also consider an analogue of this argument in the case of Buchak’s risk-sensitive decision theory and they show that, in this case, it does establish Diachronic Conditionalization.

According to Dmitri Gallow (2019), on the other hand, you should maximize epistemic utility in the usual way, where the expectation is taken over all worlds, but you should change the epistemic utility function you use, so that it assigns the same neutral value to every credence function at every world at which the evidence you’ve learned is false. Again it turns out that, if the epistemic utility function you begin with is strictly proper, and if your prior assigns positive credence to the proposition you learn, the credence function that maximizes this is the one demanded by Diachronic Conditionalization.

#### 5.4.3 Other updating situations

The updating norms we have considered so far and the arguments in their favor make a number of assumptions. First, they assume that your evidence will come in the form of a proposition learned with certainty—we might call this assumption *Certainty*. Second, they assume that proposition will be true—we might call this assumption *Factivity*. Third, they assume that proposition will come from a partition that can be specified in advance—we might call this *Partitionality*. We'll treat these three in turn.

First, Certainty. Richard Jeffrey (1965) points out that our evidence often doesn’t come in the form of a proposition learned with certainty, because there is often no proposition in our agenda that perfectly captures what we learn. In such cases, he suggests, the evidence places specific constraints on our posterior credences. He considers the case in which it specifies which posterior credences you must have in the propositions in a particular partition, and he formulated a rule, known as Probability Kinematics or Jeffrey Conditionalization, which tells you how to set your posterior credences in other propositions that lie outside that partition. Inspired by a suggestion by Diaconis and Zabell (1982), Leitgeb and Pettigrew (2010) argue that, when your evidence places constraints on your posterior credence function, you should update by adopting whichever credence function maximizes expected epistemic utility from the point of view of your prior credence function *among those credence functions that satisfy the constraint*. Leitgeb and Pettigrew show that the Brier score gives a different updating rule from the one that Jeffrey proposed. Levinstein (2012) argues that this is a reason to reject the Brier score, and Pettigrew (Theorem 12, Section 8.5, 2021) shows that no additive strictly proper scoring rule gives Jeffrey’s rule via this approach.

Jason Konek (2022) offers an alternative approach to the situations that Jeffrey identified. He notes that, while there might be no proposition in the agenda of your prior credence function that you come to learn with certainty, there is a proposition that expresses your experience, and you become able to entertain it when you have the learning experience, because you can simply point to the learning experience and say ‘I learned that’. So, after the learning experience, you can add this proposition to your agenda and retrospectively set your conditional credences in having that learning experience, given different ways the world might be; and that is sufficient to allow you to set your new credences given that you did have that learning experience. He provides an epistemic utility argument for a particular way of doing this.

Second, Factivity. There are two ways to approach this, but the second is also the way to approach Partitionality, so we’ll leave that for the moment. The first approach is suggested by Michael Rescorla (2022), who asks not what you should plan to do when you learn which proposition from a particular partition is true, but what you should plan to do when you become certain of a proposition in a partition, leaving open whether the proposition of which you’ll become certain will be true. Pettigrew (2023) shows that you should plan to update by conditioning on what you learned with certainty by giving a dominance argument for the following norm, due to Bas van Fraassen (1999) (see also (Staffel & de Bona forthcoming)):

> **Weak General Reflection Principle** Rationality requires that your prior credence function should be a mixture of your possible future credence functions.

Pettigrew proves the following theorem:

> **Dominance Theorem for Weak General Reflection (Pettigrew 2023)[^pettigrew-2023]** Suppose your epistemic utility function is additive, continuous, and strictly proper measure. Then:
>
> 1. If your prior credence function is not a mixture of your possible posterior credence functions, then there is an alternative prior and, for each possible posterior credence function, an alternative posterior such that, at every state of the world and for every possible posterior, the sum of the epistemic utility of your prior and the epistemic utility of that posterior is less than the sum of the epistemic utility of the alternative prior and the epistemic utility of the alternative posterior.
> 2. If your prior credence function is a mixture of your possible posterior credence functions, then there is no alternative prior and, for each possible posterior credence function, an alternative posterior such that, at every state of the world and for every possible posterior, the sum of the epistemic utility of your prior and the epistemic utility of that posterior is less than the sum of the epistemic utility of the alternative prior and the epistemic utility of the alternative posterior.

As van Fraassen (1999) shows, if we assume that (i) for each element of a given partition, there is a unique possible posterior that is certain of it, and (ii) for each possible posterior, there is a unique element of the partition of which it is certain, then the Weak General Reflection Principle entails that each possible posterior is obtained from your prior by conditioning on the relevant element of the partition.

Third, Partitionality. To represent situations in which your evidence does come in the form of a proposition learned with certainty, but in which we assume neither that the proposition is true nor that it comes from a partition that can be specified in advance, we follow Nilanjan Das (2023) in defining an *evidence function* to be a function that takes a state of the world and returns the proposition you’ll learn with certainty at that state of the world. As before, an updating plan takes a state of the world to the posterior you plan to adopt when you learn the evidence you’ll receive at that state of the world; and, as before, an updating plan is available if it gives the same recommendation for any two states of the world at which you receive the same evidence. Then Miriam Schoenfield (2016) shows that you maximize expected epistemic utility not by planning to conditionalize on your evidence, but by planning to conditionalize on the fact that you received that evidence. Gallow (2021) worries that the plans Schoenfield considers available are not genuinely available to individuals in situations in which their evidence fails to rule out that their evidence is different from how it actually is, and he suggests a framework in which to represent genuinely available plans and describes the updating plan that maximizes expected epistemic utility in that framework.

#### 5.4.4 Updating in social situations

So far, we have only considered an individual’s credences and their relationship to one another. But we also learn from others who investigate the world and share the credences they come to have on that basis. So our epistemic situation affects and is affected by the epistemic situation of others. Igor Douven and Sylvia Wenmackers (2017) have explored a situation like this. They ask whether epistemic utility considerations make different demands for updating from those they make in the individual case. They suppose that the members of a group all begin with the same prior credence function. Each holds a coin and all the coins have the same bias towards landing heads, but they are uncertain what that bias is to begin with. Each individual tosses their coin some number of times and updates their own credences on the basis of what they observe; then they share their evidence with some of the other members of the group; then they repeat this process a number of times. After each iteration, we measure their epistemic utility, and then we look at the expected average epistemic utility across all members and all times in the process. Douven and Wenmackers treat updating on the private evidence from your own coin tosses and updating on public evidence from the credences of others differently. They assume each member updates on the public evidence of others’ credences by taking the average (arithmetic mean) of their credences and those of the other members. And then they ask which updating rule for the private evidence will lead to the greatest expected average epistemic utility, and they use computer simulation to show that it is not Bayesian conditionalization. Indeed, they show that an updating rule introduced by van Fraassen (Chapter 6, 1989) to give a crude model of inference to the best explanation outperforms Bayesian conditionalization (though we don’t know whether some other rule outperforms that). However as Pettigrew (2021b) points out, this only shows that, when you update on the evidence of your peers by taking averages, rather than by conditionalizing on it, you should compensate for the suboptimality of that choice by doing something other than conditionalizing on your private evidence. But of course the results we’ve considered in this section say you shouldn’t do that. You should update on the evidence of your peers and the evidence of your private coin tosses as you should update on everything, namely, by conditionalizing.

#### 5.4.4 The epistemology of inquiry

As we saw above, when Greaves and Wallace argue for Partitional Plan Conditionalization (narrow scope), they hold fixed the partition from which our evidence will come and ask which updating plan maximizes expected epistemic utility. However, we don’t simply receive evidence passively. We also go out and seek it, and in those cases we have to pick from which partition we want our evidence to come: Should the scientist perform this experiment or another? Should the detective interview this suspect or that? Adapting an insight due to I. J. Good (1967) to the epistemic setting, Wayne Myrvold (2012) and Alejandro Pérez Carballo (2018) show that we can use epistemic utilities to tell which evidence we should collect from the epistemic point of view.

Given a partition, we know that an updating plan that maximizes expected epistemic utility is a conditionalizing plan. So let’s hold fixed that, for any given partition, we plan to condition on whichever proposition in it we learn with certainty. And now suppose there are two partitions, and we must choose which one to investigate; that is, we must choose from which one our evidence will come, always assuming that, whichever we choose, we’ll respond to the evidence we receive by conditioning on it. Then we can simply compare the expected epistemic utility of conditioning on whichever element of the first partition we learn and the expected epistemic utility of conditioning on whichever element of the second partition we learn, and then do whichever is greater. One result is that, if one partition is a fine-graining of the other, so that each proposition in the latter is a disjunction of propositions in the former, we should always choose the finer-grained one.

As well as providing epistemic norms for choosing between the partitions we might investigate, epistemic utilities can also give norms for when to investigate at all and when to consider an issue settled for the time being. To obtain these norms, we simply treat the option of conducting no further investigations as the case in which we investigate the trivial partition that consists only of a tautology. If our epistemic utility function is strictly proper, and if you assign any probability to investigating a given partition changing your credences, then investigating must have greater expected epistemic utility than not investigating, giving a epistemic analogue to Good’s value of information theorem (Good 1967; Myrvold 2012)[^good-1967][^myrvold-2012]. But of course such investigations are not cost-free, and so the question will always arise whether the cost is worth it for the expected epistemic gain.

Campbell-Moore and Salow (2020) show that, for risk-sensitive individuals, investigating isn’t always demanded, even when it’s free. It has long been known that such individuals are sometimes pragmatically required not to investigate; Campbell-Moore and Salow show that they are also sometimes epistemically required not to.

So epistemic utilities give epistemic norms that govern our choices between different inquiries and our choice whether to investigate at all, at least when other aspects are equal. But of course, things are rarely equal. There are also pragmatic reasons for investigating one partition rather than other, and so some reasons for inquiry are pragmatic: for instance, investigating one partition might have greater expected epistemic utility than investigating another, but it might be more costly, or it might not help as much to inform a pressing decision we must soon make. But Myrvold’s and Pérez Carballo’s approach does at least tell us the epistemic value of an investigation at a state of the world, which can then be weighted against its pragmatic value and perhaps also moral value to give the all-things-considered verdict on what to do. Furthermore, this approach shows that there can be purely epistemic reasons for gathering evidence for a particular investigation, answering a question that has been raised in the literature on the epistemology of inquiry (e.g. Woodard & Flores forthcoming). And Filippo Vindrola and Vincenzo Crupi (forthcoming) have recently applied the approach to the Wason Selection Task to vindicate Wason’s original contention that people tend to choose how to investigate irrationally in that case.

### 5.5 Epistemic utility arguments for and against the Uniqueness Thesis

In this section, we consider epistemic utility arguments for and against the Uniqueness Thesis about credences. Recall that this says that, for any body of evidence and any agenda, there is a unique credence function on that agenda that it is rational for an individual with that total evidence to have. And recall that epistemic permissivism about credences is the negation of this claim. There are three sorts of argument. The first appeals to norms of decision theory that encode attitudes to risk to answer questions about which prior credence functions are rationally permissible. The second appeals to the notions of probabilistic knowledge and epistemic luck. The third appeals to the value of rationality.

#### 5.5.1 Epistemic risk and the Uniqueness Thesis

Minimax (sometimes called Maximin) is the most well-known norm of decision theory that encodes an attitude to risk (Wald 1945)[^wald-1945]. This says that you should pick an option that *min*imizes your worst-case or *max*imal disutility (equivalently, you should pick an option that *maxi*mizes your worst-case or *min*imal utility). If we say that someone is more risk-averse the more weight they give to worst-case scenarios in their decision-making and the less they give to best-case scenarios, Minimax is maximally risk-averse.

Pettigrew (2016) proves that, if we assume your agenda is an algebra and our epistemic utility function is extensional and strictly proper, then Minimax entails the Principle of Indifference:

> **Principle of Indifference** Rationality requires that you assign the same credence to every possible state of the world.

Given an agenda, Probabilism and the Principle of Indifference pick out a unique prior credence function, namely, the uniform credence function, $c^\dag$, where $c^\dag(w) = \frac{1}{n}$, for all $w$ in $\mathcal{W}$, and $n$ is the number of worlds in $\mathcal{W}$.

However, Minimax is often thought too extreme. It might be rationally permissible to be risk-averse, but it is not rationally permissible to place *all* of your weight on the worst-case scenario and pay *no* attention to anything else: you would surely prefer an option that pays £1 if the number of stars is even and £1,000,000 if it’s odd to an option that pays £2 either way, and yet Minimax rules out the first.

Alternative risk-sensitive norms of decision theory have been proposed. Pettigrew considers the Hurwicz Criterion (Hurwicz 1952; Pettigrew 2016)[^hurwicz-1952] and formulates the Generalized Hurwicz Criterion (Pettigrew 2022)[^pettigrew-2022]. In the former, you consider not only the worst-case scenario but also the best, and you assign a weight to each to give the Hurwicz score. He shows that, if we are permissive enough about the weightings, we obtain permissivism about rational priors. In the latter, we give weights to all scenarios, best, second-best, and so on down to second-worst, worst; and that gives us the generalized Hurwicz score. Again, if we are permissive enough about weightings, we obtain an even broader permissivism about priors.

#### 5.5.2 Epistemic luck, probabilistic knowledge, and the Uniqueness Thesis

Jason Konek (2017) argues for a norm that’s slightly weaker than the Uniqueness Thesis. He appeals not to best and worst cases but to best and worst expectations by the lights of different possible chance functions. He is not so interested in what they think of the prior you pick, but what they think of the possible posteriors you might obtain from the prior when you learn new information. He thinks you should pick a prior so that the difference between the maximum expected epistemic utility of your posterior and the minimum is minimized: he calls this principle MaxSen.

Why do this? Because, Konek argues, this gives you the best chance of forming credences that constitute probabilistic knowledge of the sort Sarah Moss (2018) has described. One putative necessary condition on knowledge is that the success you have forming an accurate belief or credence is due to your own ability, rather than to luck. Konek argues that, if you pick the prior he recommends, whatever accuracy you obtain after you learn the new evidence and update accordingly is due to your own cognitive ability as much as possible and to luck as little as possible. The relationship of Konek’s MaxSen to the Uniqueness Thesis is a bit subtle. For someone with no evidence, a fixed agenda, and a partition from which their future evidence will come, there is a unique credence function it demands; but which it demands does depend on the partition from which the future evidence will come, and the Uniqueness Thesis does not strictly permit that.

#### 5.5.3 Propriety, epistemic permissivism, and the Uniqueness Thesis

Sophie Horowitz (2019) appeals to epistemic utility theory to raise two problems for epistemic permissivism.

First, take a strictly proper epistemic utility function. Then, Horowitz points out, whichever set of prior credence functions the epistemic permissivist takes to be rationally permissible, for many of those permissible credence functions, there will be impermissible ones they expect to have greater epistemic utility than many of the other permissible ones. For instance, perhaps rationality doesn’t require that your prior credence in a proposition is a particular number, but it does require that it lies within a certain range—say, between 0.3 and 0.6. Then, if your credence is near one end of this range but still within it (say, 0.31), then it is rationally permitted, but it will expect something a little beyond that end of the range (say, 0.29), which is thereby not rationally permitted, to have greater epistemic utility than something within the range, and therefore rationally permitted, but at the other end (say, 0.59).

Second, Horowitz notes that, if our epistemic utility function is strictly proper, then each permissible credence function expects itself to be best. And this causes problems for what Horowitz calls “acknowledged permissive cases”. These are cases in which rationality is permissive, and moreover the individual knows this is so. In such cases, they adopt their particular prior, and they know that this prior is merely one among many rationally permissible priors; but, because our epistemic utility function is strictly proper, they expect it to have greater epistemic utility than any alternative, including the alternatives they take to be rationally permissible. So, Horowitz asks, in what sense do they really consider those alternatives permissible? Horowitz considers a response by Miriam Schoenfield (2014) and finds it wanting.

### 5.6 Epistemic utility arguments in social epistemology

So far, we have considered only norms that govern an individual’s credences. But many epistemological questions arise when we consider groups of individuals and their interactions. Here are two such questions for which we have epistemic utility arguments: Does the group itself have a credence function, just as its individual members do, and if so how does relate to the credence functions of the members? (Section 5.6.1) How do we maximize the total epistemic utility across the group, and does this place constraints on the individuals? (Section 5.6.2).

#### 5.6.1 The epistemic utility of group credences

In everyday talk, we often ascribe beliefs and credences to groups of individuals as well as to their members: the Intergovernmental Panel on Climate Change is 70% confident in such-and-such; the parliamentary subcommittee believes so-and-so. And we often think that the credences of the individuals at least partly determine the credences of the group. So suppose I must come up with precise credences to ascribe to a group of individuals. The literature on probabilistic judgment aggregation or opinion pooling offers a range of possibilities. For instance:

> **Linear Pooling** A group’s credence function should be a mixture of the members’ credence functions.

Sarah Moss (2011) offers an epistemic utility argument for Linear Pooling. She says that the group’s credence function should be the one that maximizes the group’s expected epistemic utility, and she defines the group’s expected epistemic utility to be a weighted arithmetic mean of the members’ individual expected epistemic utilities. And then she proves that, providing our epistemic utility function is strictly proper, it is the mixture of the members’ credence functions with these same weights that maximizes this quantity.

One concern about this argument is that it assumes something too close to what it attempts to establish. It assumes that the members’ individual *expectations* should be combined by weighted arithmetic averaging and attempts to show that members’ individual *credence functions* should be so combined. Pettigrew (2017) offers a related argument that improves on Moss’s in some ways, though makes very slightly stronger assumptions. The idea is that, whatever the group’s credence function is, there had better not be an alternative that every member of the group expects to be better, epistemically speaking. He then shows that, if your epistemic utility function is continuous and strictly proper, and if the group’s credence function is not a mixture of the individuals’ credence functions, then there is such an alternative.

#### 5.6.2 Maximizing total epistemic utility across the group's members

As well as asking about the epistemic utility of the group’s credences, we can also ask about the total accuracy of the members’ credences. And this gives an argument for a surprisingly strong norm (Kopec 2012)[^kopec-2012]:

> **Consensus** Rationality requires that all members of a group have the same credence function.

The argument is based on the fact that, if a group violates Consensus, so that at least two members disagree about some of their credences, then there is a single credence function such that, if all members of the group were to have it, their total epistemic utility would be greater for sure.

We should take this argument with a pinch of salt. After all, one thing that people do is to investigate the world and collect evidence and then share their findings. They decide which evidence to collect by consulting their credences and asking which will maximize expected epistemic or pragmatic utility, as we saw in Section 5.3.4. And so the individuals in a group that satisfies Consensus will conduct the same sorts of investigations and acquire similar evidence, while a group with more diverse credences will conduct more diverse investigations and end up with more diverse evidence. And it might well be that the benefits a group gets in the long run from collecting diverse evidence might outweigh the disadvantage they get from lacking consensus at the start (Zollman 2010)[^zollman-2010].

## 6. Comparative confidence

In the comparative confidence model, we represent an individual’s epistemic state by their *comparative confidence ordering*, which is an ordering or binary relation $\prec, \sim$ on their agenda. For any two propositions, $X$ and $Y$ in their agenda, we say $X \prec Y$ if they are less confident in $X$ than in $Y$ and we say $X \sim Y$ if they are exactly as confident in $X$ as in $Y$.

Our first job is to say how to measure the epistemic utility of such an ordering. Fitelson and McCarthy (2014) suggest the following. A comparative confidence ordering is a set of pairwise comparisons. Fitelson and McCarthy assume that it is complete, so that, for any $X$, $Y$ in the individual’s agenda, $X \prec Y$ or $X \sim Y$ or $Y \prec X$. So we first say how to score these individual comparisons:

$$ \begin{array}{c|c||c|c} X & Y & X \prec Y & X \sim Y \\ \hline T & T & \alpha & 1 \\ T & F & \beta & \gamma \\ F & T & 1 & \gamma \\ F & F & \alpha & 1 \end{array} $$

The idea is that, if $X \prec Y$ and $X$ is false and $Y$ is true, then you’ve ordered the propositions as the omniscient agent would, so you get maximal epistemic utility, which we’ll take to be 1; and similarly if $X \sim Y$ and $X$ and $Y$ have the same truth value. Then there are three potential mistakes whose score we need to determine, and we've marked those scores as $\alpha, \beta, \gamma$.

Now, we could simply permit any different values for these, but Fitelson and McCarthy give an argument that we should set: $\alpha = 1$, $\beta = 0$, $\gamma = 1/2$ (or any positive linear transformation of these). Only for these scores does Fitelson and McCarthy’s account deliver a strictly proper way of measuring epistemic utility, in the following sense:

1. If $C$ is a probabilistic credence function and $C(X) \lt C(Y)$, then $C$ expects $X \prec Y$ to be better than $X \sim Y$ and to be better than $Y \prec X$.
2. If $C$ is a probabilistic credence function and $C(X) = C(Y)$, then $C$ expects $X \sim Y$ to be better than $X \prec Y$ and to be better than $Y \prec X$.

So the only strictly proper measure of inaccuracy for comparative confidence orderings is this (up to positive linear transformation): $$ \begin{array}{c|c||c|c} X & Y & X \prec Y & X \sim Y \\ \hline T & T & 1 & 1 \\ T & F & 0 & 1/2 \\ F & T & 1 & 1/2 \\ F & F & 1 & 1 \end{array} $$

We can now ask: for which norms can we provide epistemic utility arguments using this measure of epistemic utility? Here is one, where we say that one proposition is strictly stronger than another if the first entails the second, but the second does not entail the first:

> **Strict Quasi-Additivity**
>
> - If $X$ is strictly stronger than $Y$, $X$ and $Z$ are mutually exclusive, and $Y$ and $Z$ are mutually exclusive, then $X \vee Z \prec Y \vee Z$.
> - If $X$ is equivalent to $Y$, $X$ and $Z$ are mutually exclusive, and $Y$ and $Z$ are mutually exclusive, then $X \vee Z \sim Y \vee Z$.

From this, we can derive a number of further norms:

> **Non-Triviality** $\bot \prec \top$, if $\bot$ is a contradiction and $\top$ is a tautology.
>
> **Regularity** $\bot \prec X \prec \top$, if $\bot$ is a contradiction, $\top$ is a tautology, and $X$ is contingent.
>
> **Strict Monotonicity**
>
> - If $X$ is strictly stronger than $Y$, then rationality requires that $X \prec Y$.
> - If $X$ is equivalent to $Y$, then rationality requires that $X \sim Y$.

Now, we have already assumed that the ordering is complete. If we add Transitivity to Completeness and Strict Quasi-Additivity, then it is guaranteed that there is a particular way to represent this ordering: there is a Dempster-Shafer belief function $b$ on $\mathcal{F}$ such that $b(X) \lt b(Y)$ iff $X \prec Y$ and $b(X) = b(Y)$ iff $X \sim Y$ (Wong, et al. 1991).

Eric Raidl and Wolfgang Spohn (2020) offer a slightly different way of measuring the accuracy of a comparative confidence ordering and offer an argument for the norms of Spohn’s ranking theory (Spohn 2012)[^spohn-2012].

## 7. Imprecise credences

In the imprecise credence model, we typically represent an individual’s epistemic state not as a single credence function, but as a set of credence functions, and we assume those credence functions are probabilistic. There are various related representations, some of which are more powerful, some less, such as upper and lower previsions, sets of desirable gambles, and probability filters. I’ll focus here on sets of probability functions.

The central result in this area is that there are no measures of epistemic utility for imprecise credences that have the property analogous to the property of strict propriety in the precise case. There are three versions of these results, starting with a theorem due to Seidenfeld, Schervish, and Kadane (2012), and including adaptations by Miriam Schoenfield (2017) and Conor Mayo-Wilson and Gregory Wheeler (2016). I'll present Schoenfield’s, since it’s the most straightforward.

Schoenfield considers the simplest sort of case, where our individual only has opinions about a proposition and its negation. And she assumes that any measure of epistemic utility for imprecise credences has the following properties:

> **Extension** When restricted to precise probabilities over those two propositions, the measure of epistemic utility is maximized at the omniscient credence function and it is continuous.
>
> **Boundedness** Epistemic utilities are measured by real numbers.
>
> **Probabilistic Admissibility** For any precise credal state, there is no imprecise credal state that is at least as good as that precise state at all worlds.

Then Schoenfield shows that, if Extension, Boundedness, and Probabilistic Admissibility hold, then for any imprecise set, there is a precise probabilistic credence function that has equal epistemic utility at every world. This seems problematic, because it suggests that it can never be rationally required to have imprecise credences, and their proponents typically think it can be.

Jason Konek (2019) has proposed a way to avoid this concern. He argues that, in fact, we should not expect a single measure of epistemic utility to work for every situation. The idea is that our measure of epistemic utility for imprecise credences encodes not only our attitude to accuracy, but also our attitude to epistemic risk, and for each legitimate way of measuring epistemic utility, there is a family of imprecise credences that are endorsed by it. So all that is really required is that, for any coherent imprecise credences, there is a legitimate way of measuring epistemic utility that endorses them: that is, where they consider themselves best from that point of view.

## 8. Future directions

We have seen that epistemic utility arguments provide a fruitful approach to epistemic norms. We conclude in this section by highlighting some possible avenues for future research, though this list is by no means exhaustive:

- One attraction of the epistemic utility approach is that it does not only provide us with a means by which to establish norms that we have already formulated; it also allows provides a process by which to formulate new norms governing different situations that we can then use it justify. The recipe is straightforward: specify the situation; specify your measure of epistemic utility; ask what properties an epistemic state must have if it is to optimize that measure of epistemic utility in that situation. For instance, it is this approach that lead from Joyce’s argument for Probabilism, to Greaves & Wallace’s argument for Conditionalization, to Myrvold’s approach to the value of learning new evidence. Increasingly, epistemologists are considering less and less idealized epistemic situations: situations in which you have evidence, but you don’t know what that evidence is (Williamson 2000)[^williamson-2000]; situations in which you have higher-order evidence that casts doubt on your first-order reasoning (Feldman 2005)[^feldman-2005]; and so on. The epistemic utility approach is ideally situated to help formulate norms to govern these non-ideal situations.
- While there is some work on how to choose between different ways of measuring epistemic utility, more could be done (Pettigrew 2016, Levinstein 2017)[^levinstein-2017]. What reason do we have for using one strictly proper scoring rule rather than another?
- While much work on epistemic utility assumes, along with the veritist, that the sole fundamental source of epistemic value is truth or gradational accuracy, other parts of epistemology talk of further or alternative sources, such as explanatory power or being formed by an epistemically virtuous process. How would we measure epistemic utility if these are among its sources?
- A final, rather obvious suggestion is that there are substantial objections to the approach that must still be addressed. We have met many of them over the course of this survey, from Levinstein’s Varying Importance Objection in Section 5.1.1 to the Act-State Dependence worry in Section 5.2.3 to Jennifer Carr’s epistemic expansions concern in Section 5.2.4. These three, as well as others detailed above, still lack truly compelling responses.

There is still much to be done.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=epistemic-utility). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/epistemic-utility/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=epistemic-utility&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/epistemic-utility/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- Pettigrew, Richard, [The webpage for Pettigrew’s *Accuracy and the Laws of Credence*](https://richardpettigrew.com/books/accuracy/). This includes video tutorials that work through some of the central results in accuracy-first epistemology.
- Weisberg, Jonathan, [A series of blogposts](https://jonathanweisberg.org/tags/accuracy-for-dummies/) that walk slowly through the technical side of accuracy-first epistemology.

## Related Entries

belief, formal representations of | epistemology | epistemology: Bayesian | probability, interpretations of

[^alchourrón-1985]: Alchourrón, C.E., P. Gärdenfors, & D. Makinson, 1985, “On the Logic of Theory Change: Partial Meet Contraction and Revision Functions”, *Journal of Symbolic Logic*, 50: 510–530.

[^berker-2013a]: Berker, S., 2013a, “Epistemic Teleology and the Separateness of Propositions”, *Philosophical Review*, 122(3): 337–393.

[^berker-2013b]: –––, 2013b, “The Rejection of Epistemic Consequentialism”, *Philosophical Issues (Supp. Noûs)*, 23(1): 363–387.

[^bonjour-1985]: BonJour, L., 1985, *The Structure of Empirical Knowledge*, Cambridge, MA: Harvard University Press.

[^briggs-2020]: Briggs, R. A. & R. Pettigrew, 2020, “An Accuracy-Dominance Argument for Conditionalization”, *Noûs*, 54(1): 162–181.

[^brown-1976]: Brown, P. M., 1976, “Conditionalization and expected utility” *Philosophy of Science*, 43(3): 415–419.

[^buchak-2013]: Buchak, L., 2013, *Risk and Rationality*, Oxford: Oxford University Press.

[^caie-2013]: Caie, M., 2013, “Rational Probabilistic Incoherence”, *Philosophical Review*, 122(4): 527–575.

[^campbell-moore-2015]: Campbell-Moore, C., 2015, “Rational Probabilistic Incoherence? A Reply to Michael Caie”, *Philosophical Review* 124(3): 393–406.

[^campbell-moore-2020]: –––, & B. Salow 2020, “Avoiding Risk and Avoiding Evidence”, *Australasian Journal of Philosophy*, 98(3): 495–515.

[^campbell-moore-2022]: –––, & B. Salow 2022, “Accurate Updating for the Risk–Sensitive”, *The British Journal for the Philosophy of Science*, 73(3): 751–776.

[^carr-2015]: Carr, J., 2015, “Epistemic Expansions”, *Res Philosophica*, 92(2): 217–236.

[^carr-2017]: –––, 2017, “Epistemic Utility Theory and the Aim of Belief”, *Philosophy and Phenomenological Research*, 95(3): 511–534.

[^carr-2019]: –––, 2019, “A Modesty Proposal”, *Synthese*. doi:10.1007/s11229-019-02301-x

[^cox-1946]: Cox, R. T., 1946, “Probability, Frequency and Reasonable Expectation”, *American Journal of Physics*, 14: 1–13.

[^cox-1961]: –––, 1961, *The Algebra of Probable Inference*, Baltimore: Johns Hopkins University Press.

[^d’agostino-2010]: D’Agostino, M. & C. Sinigaglia, 2010, “Epistemic Accuracy and Subjective Probability”, in M. Dorato & M. Suàrez (eds.), *EPSA Epistemology and Methodology of Science*, Springer.

[^das-nd]: Das, N., “The Value of Biased Information”, *The British Journal for the Philosophy of Science*, 74(1): 25–55.

[^finetti-1937]: de Finetti, B., 1937 [1980], “Foresight: Its Logical Laws, Its Subjective Sources”, in H. E. Kyburg & H. E. K. Smokler (eds.), *Studies in Subjective Probability*, Huntington, NY: Robert E. Kreiger Publishing Co., 1980

[^finetti-1974]: –––, 1974, *Theory of Probability* Vol. 1, New York: Wiley.

[^diaconis-1982]: Diaconis, P. & S. Zabell, 1982, “Updating Subjective Probability” *Journal of the American Statistical Association*, 77(380): 822–830.

[^dorst-2017]: Dorst, K., 2017, “Lockeans Maximize Expected Accuracy”, *Mind*, 128(509): 175–211.

[^douven-2017]: Douven, I. & S. Wenmackers, 2017, “Inference to the Best Explanation versus Bayes???s Rule in a Social Setting”, *British Journal for the Philosophy of Science*, 68(2): 535–570.

[^dunn-2018]: Dunn, J., 2018, “Accuracy, Verisimilitude, and Scoring Rules”, *Australasian Journal of Philosophy*, 97(1): 151–166.

[^easwaran-2013]: Easwaran, K., 2013, “Expected Accuracy Supports Conditionalization—and Conglomerability and Reflection”, *Philosophy of Science*, 80(1): 119–142.

[^easwaran-2015]: –––, 2015, “Accuracy, Coherence, and Evidence”, *Oxford Studies in Epistemology*, 5, 61–96.

[^easwaran-2016]: –––, 2016, “Dr Truthlove, Or: How I Learned to Stop Worrying and Love Bayesian Probabilities”, *Noûs*, 50(4): 816–853

[^easwaran-2012]: ––– & B. Fitelson, 2012, “An ‘evidentialist’ worry about Joyce’s argument for Probabilism”, *Dialectica*, 66(3): 425–433.

[^feldman-2005]: Feldman, R., 2005, “Respecting the Evidence”, *Philosophical Perspectives*, 19(1): 95–119.

[^fitelson-2015]: Fitelson, B. & K. Easwaran, 2015, “Accuracy, Coherence and Evidence”, *Oxford Studies in Epistemology*, 5: 61–96.

[^fitelson-2014]: Fitelson B. & D. McCarthy, 2014, “Toward an epistemic foundation for comparative confidence”, Presentation, University of Wisconsin-Madison. [[Online version available here]](http://fitelson.org/cc_handout.pdf).

[^flores-nd]: Flores, C. & E. Woodard, forthcoming, “Epistemic Norms on Evidence–Gathering”, *Philosophical Studies*.

[^foley-1992]: Foley, R., 1992, “The Epistemology of Belief and the Epistemology of Degrees of Belief”, *American Philosophical Quarterly*, 29(2): 111–121.

[^fraassen-1983]: Fraassen, B.C. van, 1983, “Calibration: Frequency Justification for Personal Probability”, in R.S. Cohen & L. Laudan (eds.), *Physics, Philosophy, and Psychoanalysis*, Dordrecht: Springer.

[^gallow-2019]: Gallow, J. D., 2019, “Learning and Value Change”, *Philosophers’ Imprint*, 19: 1–22.

[^gallow-2021]: –––, 2021, “Updating for Externalists”, *Noûs*, 55(3): 487–516.

[^goldman-1999]: Goldman, A.I., 1999, *Knowledge in a Social World*, New York: Oxford University Press.

[^good-1967]: Good, I. J., 1967, “On the Principle of Total Evidence”, *The British Journal for the Philosophy of Science*, 17(4):319–321.

[^greaves-2013]: Greaves, H., 2013, “Epistemic Decision Theory”, *Mind*, 122(488): 915–952.

[^greaves-2006]: Greaves, H. & D. Wallace, 2006, “Justifying Conditionalization: Conditionalization Maximizes Expected Epistemic Utility”, *Mind*, 115(459): 607–632.

[^hacking-1967]: Hacking, I., 1967, “Slightly More Realistic Personal Probability”, *Philosophy of Science*, 34(4): 311–325.

[^harman-1973]: Harman, G., 1973, *Thought*, Princeton, NJ: Princeton University Press.

[^hájek-2008]: Hájek, A., 2008, “Arguments For—Or Against—Probabilism?”, *The British Journal for the Philosophy of Science*, 59(4): 793–819.

[^hájek-2009]: –––, 2009, “Fifteen Arguments against Hypothetical Frequentism”, *Erkenntnis*, 70: 211–235.

[^hempel-1962]: Hempel, C., 1962, “Deductive–Nomological vs. Statistical Explanation”, in H. Feigl and & G. Maxwell (eds.) *Minnesota Studies in the Philosophy of Science (vol. III)*, Minneapolis:University of Minnesota Press.

[^horowitz-2014]: Horowitz, S., 2014, “Immoderately rational”, *Philosophical Studies*, 167: 41–56.

[^horowitz-2017]: –––, 2017, “Accuracy and Educated Guesses” in T. Szabó Gendler & J. Hawthorne (eds.) *Oxford Studies in Epistemology, volume 6* Oxford: Oxford University Press.

[^horowitz-2019]: –––, 2019, “The Truth Problem for Permissivism”, *Journal of Philosophy* 116(5): 237–262.

[^hughes-1984]: Hughes, R. I. G. & B. C. van Fraassen, 1984, “Symmetry arguments in probability kinematics”, in *PSA: Proceedings of the Biennial Meeting of the Philosophy of Science Association* (Issue 2/Volume Two: Symposia and Invited Papers), pp. 851–869 doi:10.1086/psaprocbienmeetp.1984.2.192543

[^hurwicz-1952]: Hurwicz, L., 1952, “A criterion for decision making under uncertainty”, Cowles Commission Technical Report 355.

[^huttegger-2013]: Huttegger, S.M., 2013, “In Defense of Reflection”, *Philosophy of Science*, 80(3): 413–433.

[^ismael-2008]: Ismael, J., 2008, “Raid! Dissolving the Big, Bad Bug”, *Noûs*, 42(2): 292–307.

[^jaffray-1989]: Jaffray, J-Y., 1989, “Coherent bets under partially resolving uncertainty and belief functions”, *Theory and Decision*, 26: 90–105.

[^james-1897]: James, W., 1897, “The Will to Believe’, in *The Will to Believe, and Other Essays in Popular Philosophy*, New York: Longmans Green.

[^jeffrey-1965]: Jeffrey, R., 1965, *The Logic of Decision*, New York: McGraw-Hill.

[^jeffrey-1983]: Jeffrey, R., 1983, *The Logic of Decision* (2ⁿᵈ). Chicago; London: University of Chicago Press.

[^jenkins-2007]: Jenkins, C.S., 2007, “Entitlement and Rationality”, *Synthese*, 157: 25–45.

[^joyce-1998]: Joyce, J.M., 1998, “A Nonpragmatic Vindication of Probabilism”, *Philosophy of Science*, 65(4): 575–603.

[^joyce-2009]: –––, 2009, “Accuracy and Coherence: Prospects for an Alethic Epistemology of Partial Belief”, in F. Huber & C. Schmidt-Petri (eds.), *Degrees of Belief*, Springer.

[^joyce-2018]: –––, 2018, “The True Consequences of Epistemic Consequentialism”, in Ahlstrom-Vij & Dunn 2018.

[^kelley-2019]: Kelley, M., 2019, *Accuracy Dominance on Infinite Opinion Sets*, MA Thesis, UC Berkeley. [[Online version available here]](https://digicoll.lib.berkeley.edu/record/140157?v=pdf).

[^kelly-2014]: Kelly, T., 2014, “Evidence Can Be Permissive”, in M. Steup, J. Turri, & E. Sosa (eds.) *Contemporary Debates in Epistemology*, Oxford: Wiley-Blackwell.

[^kerbel-nd]: Kerbel, G., ms, “A New Approach to Scoring on the Educated Guessing Framework”, Unpublished manuscript.

[^konek-2016]: Konek, J., 2016, “Probabilistic Knowledge and Cognitive Ability”, *Philosophical Review*, 125(4): 509–587.

[^konek-2019]: –––, 2019, “IP Scoring Rules: Foundations and Applications”, *Proceedings of Machine Learning Research*, 103: 256–264.

[^konek-2022]: –––, 2022, “The Art of Learning” in T. Szabó Gendler & J. Hawthorne (eds.) *Oxford Studies in Epistemology, volume 7* Oxford: Oxford University Press.

[^konek-2019-2]: Konek, J. & B.A. Levinstein, 2019, “The Foundations of Epistemic Decision Theory”, *Mind*, 128(509): 69–107.

[^kopec-2012]: Kopec, M., 2012, “We Ought to Agree: A Consequence of Repairing Goldman’s Group Scoring Rule”, *Episteme*, 9: 101–14.

[^leitgeb-2021]: Leitgeb, H., 2021, “A Structural Justification of Probabilism: From Partition Invariance to Subjective Probability”, *Philosophy of Science*, 88(2): 341–365.

[^leitgeb-2010a]: Leitgeb, H. & R. Pettigrew, 2010a, “An Objective Justification of Bayesianism I: Measuring Inaccuracy”, *Philosophy of Science*, 77: 201–235.

[^leitgeb-2010b]: –––, 2010b, “An Objective Justification of Bayesianism II: The Consequences of Minimizing Inaccuracy”, *Philosophy of Science*, 77: 236–272.

[^levinstein-2012]: Levinstein, B. A., 2012, “Leitgeb and Pettigrew on Accuracy and Updating”, *Philosophy of Science*, 79(3): 413–424.

[^levinstein-2015]: –––, 2015, “With All Due Respect: The Macro-Epistemology of Disagreement”, *Philosophers’ Imprint*, 15(3): 1–20.

[^levinstein-2017]: –––, 2017, “A Pragmatist’s Guide to Epistemic Utility”, *Philosophy of Science* 84(4): 613–638.

[^levinstein-2018]: –––, 2018, “An Objection of Varying Importance to Epistemic Utility Theory”, *Philosophical Studies*. doi:10.1007/s11098-018-1157-9

[^levinstein-2023]: –––, 2023, “Accuracy, Deference, and Chance” *Philosophical Review* 132(1): 43–87.

[^lewis-1980]: Lewis, D., 1980, “A Subjectivist’s Guide to Objective Chance”, in R.C. Jeffrey (ed.), *Studies in Inductive Logic and Probability* (Vol. II). Berkeley: University of California Press.

[^locke-1689]: Locke, J., 1689 [1975] *An Essay Concerning Human Understanding*, P.H. Nidditch (ed.) Oxford: Clarendon Press.

[^maher-1993]: Maher, P., 1993, *Betting on Theories*, Cambridge: Cambridge University Press.

[^maher-2002]: –––, 2002, “Joyce’s Argument for Probabilism”, *Philosophy of Science*, 69(1): 73–81.

[^mayo-wilson-2016]: Mayo-Wilson, C. & G. Wheeler, 2016, “Scoring Imprecise Credences: A Mildly Immodest Proposal”, *Philosophy and Phenomenological Research*, 92(1): 55–78.

[^mayo-wilson-nd]: –––, ms., “Epistemic Decision Theory’s Reckoning”. Unpublished manuscript. [[Online version available here]](http://philsci-archive.pitt.edu/16374/).

[^meacham-2018]: Meacham, C. J. G., 2018, “Can All-Accuracy Accounts Justify Evidential Norms”, in Ahlstrom-Vij & Dunn 2018.

[^moss-2011]: Moss, S., 2011, “Scoring Rules and Epistemic Compromise”, *Mind*, 120(480): 1053–1069.

[^moss-2018]: –––, 2018, “Probabilistic Knowledge”, Oxford: Oxford University Press.

[^myrvold-2012]: Myrvold, W., 2012, “Epistemic values and the value of learning”, *Synthese*, 187: 547–568.

[^nielsen-2021]: Nielsen, M., 2021, “Accuracy-dominance and conditionalization”, *Philosophical Studies*, 178(10): 3217–3236.

[^nielsen-2022]: –––, 2022, “On the Best Accuracy Arguments for Probabilism”, *Philosophy of Science*, 89(3): 621–630.

[^nielsen-2023]: –––, 2023, “Accuracy and Probabilism in Infinite Domains” *Mind*, 132(526): 402–427.

[^oddie-1997]: Oddie, G., 1997, “Conditionalization, cogency, and cognitive value”, *British Journal for the Philosophy of Science*, 48(4): 533–541.

[^oddie-2019]: –––, 2019, “What Accuracy Could Not Be”, *The British Journal for the Philosophy of Science*, 70(2): 551–580.

[^paris-1994]: Paris, J. B., 1994, *The Uncertain Reasoner’s Companion: A Mathematical Perspective*, Cambridge: Cambridge University Press.

[^paris-2001]: –––, 2001, “A Note on the Dutch Book Method”, *Proceedings of the Second International Symposium on Imprecise Probabilities and their Applications* Ithaca, NY: Shaker.

[^pérez-2018]: Pérez Carballo, A., 2018, “Good Questions”, in J. Dunn & K. Ahlstrom-Vij (eds.), *Epistemic Consequentialism*, Oxford: Oxford University Press.

[^pettigrew-2010]: Pettigrew, R., 2010, “Modelling uncertainty”, *Grazer Philosophische Studien*, 80.

[^pettigrew-2013a]: –––, 2013a, “A New Epistemic Utility Argument for the Principal Principle”, *Episteme*, 10(1): 19–35.

[^pettigrew-2013b]: –––, 2013b, “Epistemic Utility and Norms for Credence”, *Philosophy Compass*, 8(10): 897–908.

[^pettigrew-2014a]: –––, 2014a, “Accuracy and Evidence”, *Dialectica*.

[^pettigrew-2014b]: –––, 2014b, “Accuracy, Risk, and the Principle of Indifference”, *Philosophy and Phenomenological Research*.

[^pettigrew-2016a]: –––, 2016a, *Accuracy and the Laws of Credence*, Oxford: Oxford University Press.

[^pettigrew-2016b]: –––, 2016b, “Jamesian epistemology formalised: An explication of ‘The Will to Believe’” *Episteme* 13(3): 253–268.

[^pettigrew-2017]: –––, 2017, “On the Accuracy of Group Credences” in T. Szabó Gendler & J. Hawthorne (eds.) *Oxford Studies in Epistemology, volume 6* Oxford: Oxford University Press.

[^pettigrew-2018a]: –––, 2018a, “Making Things Right: the true consequences of decision theory in epistemology”, in Ahlstrom-Vij & Dunn 2018.

[^pettigrew-2018b]: –––, 2018b, “The Population Ethics of Belief: In Search of an Epistemic Theory X”, *Noûs*, 52(2): 336–372.

[^pettigrew-2018c]: –––, 2018c, “Accuracy-First Epistemology Without Additivity”, *Philosophy of Science*, 89(1): 128–151.

[^pettigrew-2021a]: –––, 2021a, “Logical ignorance and logical learning”, *Synthese*, 198(10): 9991–10020.

[^pettigrew-2021b]: –––, 2021b, “On the pragmatic and epistemic virtues of inference to the best explanation”, *Synthese* 199(5–6): 12407–12438.

[^pettigrew-2022]: –––, 2022, *Epistemic Risk and the Demands of Rationality*, Oxford: Oxford University Press.

[^pettigrew-2023]: –––, 2023, “Bayesian updating when what you learn might be false”, *Erkenntnis* 88(1): 309–324.

[^predd-2009]: Predd, J., et al., 2009, “Probabilistic Coherence and Proper Scoring Rules”, *IEEE Transactions on Information Theory* 55(10): 4786–4792.

[^quiggin-1982]: Quiggin, J., 1982, “A theory of anticipated utility”, *Journal of Economic Behavior and Organization* 3(4): 323–43.

[^raidl-2020]: Raidl, E. & W. Spohn, 2020, “An Accuracy Argument in Favor of Ranking Theory”, *Journal of Philosophical Logic* 49(2): 283–313.

[^ramsey-1926]: Ramsey, F. P., 1926 [1931], “Truth and Probability”, in R. B. Braithwaite (ed.) *The Foundations of Mathematics and other Logical Essays*, London: Routledge & Kegan Paul Ltd.

[^rescorla-2022]: Rescorla, M., 2022, “An Improved Dutch Book Theorem for Conditionalization”, *Erkenntnis*, 87(3): 1013–1041.

[^rosenkrantz-1981]: Rosenkrantz, R.D., 1981, *Foundations and Applications of Inductive Probability*, Atascadero, CA: Ridgeview Press.

[^rothschild-2021]: Rothschild, D., 2021, ‘Lockean Beliefs, Dutch Books, and Scoring Systems’, *Erkenntnis*, 88(5): 1979–1995.

[^schervish-1989]: Schervish, M. J., 1989, “A General Method for Comparing Probability Assessors“ *The Annals of Statistics*, 17(4): 1856–1879.

[^schoenfield-2014]: Schoenfield, M., 2014, “Permission to Believe: Why Permissivism Is True and What It Tells Us About Irrelevant Influences on Belief”, *Noûs*, 48(2): 193–218.

[^schoenfield-2016]: –––, 2016, “Conditionalization does not (in general) Maximize Expected Accuracy”, *Mind*, 126(504): 1155–1187

[^schoenfield-2017]: –––, 2017, “The Accuracy and Rationality of Imprecise Credences”, *Noûs*, 51(4): 667–685.

[^schoenfield-2019]: –––, 2019, “Accuracy and Verisimilitude: The Good, The Bad, and The Ugly”, *The British Journal for the Philosophy of Science*. doi:10.1093/bjps/axz032

[^seidenfeld-1985]: Seidenfeld, T., 1985, “Calibration, Coherence, and Scoring Rules”, *Philosophy of Science*, 52(2): 274–294.

[^seidenfeld-2012]: Seidenfeld, T., M.J. Schervish, & J.B. Kadane, 2012, “Forecasting with imprecise probabilities”, *International Journal of Approximate Reasoning*, 53: 1248–1261.

[^shear-2019]: Shear, T. & B. Fitelson, 2019, “Two Approaches to Belief Revision” *Erkenntnis* 84(3): 487–518.

[^spohn-2012]: Spohn, W., 2012, *The Laws of Belief: Ranking Theory & its Philosophical Applications*, New York: Oxford University Press.

[^staffel-nd]: Staffel, J. & G. de Bona, Forthcoming, “An Improved Argument for Superconditionalization”, *Erkenntnis*.

[^sylvan-2020]: Sylvan, K., 2020, “An Epistemic Non-Consequentialism”, *The Philosophical Review*, 129(1): 1–51.

[^talbot-2022]: Talbot, B., 2022, I “Headaches for Epistemologists”, *Philosophy and Phenomenological Research*, 104(2): 408–433.

[^fraassen-1999]: van Fraassen, B. C., 1999, “Conditionalization, A New Argument For”, *Topoi*, 18(2): 93–96.

[^vindrola-nd]: Vindrola, F. & V. Crupi, forthcoming, “Bayesians Too Should Follow Wason: A Comprehensive Accuracy–Based Analysis of the Selection Task”, *The British Journal for the Philosophy of Science*.

[^wald-1945]: Wald, A., 1945, “Statistical decision functions which minimize the maximum risk”, *The Annals of Mathematics*, 46(2): 265–280.

[^walsh-nd]: Walsh, S., ms., “Probabilism in Infinite Dimensions”. Unpublished manuscript.

[^white-2009]: White, R., 2009, “Evidential Symmetry and Mushy Credence”, *Oxford Studies in Epistemology*, 3: 161–186.

[^williams-2012a]: Williams, J. R. G., 2012a, “Gradational accuracy and nonclassical semantics”, *Review of Symbolic Logic*, 5(4):513–537.

[^williams-2012b]: –––, 2012b, “Generalized Probabilism: Dutch Books and accuracy domination”, *Journal of Philosophical Logic*, 41(5):811–840.

[^williams-2018]: –––, 2018, “Rational Illogicality”, *Australasian Journal of Philosophy*, 96(1): 127–141.

[^williams-2023]: Williams, J. R. G. & R. Pettigrew, 2023, ‘Consequences of Calibration’, *The British Journal for the Philosophy of Science*.

[^williamson-2000]: Williamson, T., 2000, *Knowledge and its Limits*, Oxford: Oxford University Press.

[^wong-1991]: Wong, S.K.M., Yao, Y.Y., Bollmann, P., & Bürger, H.C., 1991, “Axiomatization of qualitative belief structure”, *IEEE Transactions on System, Man, and Cybernetics*, 21: 726–734.

[^zollman-2010]: Zollman, K. J. S., 2010, “The Epistemic Benefit of Transient Diversity”, *Erkenntnis* 72(1): 17–35.
