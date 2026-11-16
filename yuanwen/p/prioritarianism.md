# Prioritarianism as a Theory of Value
**First published Mon Mar 24, 2025**

*Adler, Matthew, Holtug, Nils*

Prioritarianism is generally understood as a kind of *moral axiology*. An axiology provides an account of what makes items, in this case outcomes, good or bad, better or worse. A *moral* axiology focuses on *moral* value: on what makes outcomes *morally* good or bad, *morally* better or worse. Prioritarianism, specifically, posits that the moral-betterness ranking of outcomes gives extra weight (“priority”) to well-being gains and losses affecting those at lower levels of well-being. It differs from utilitarianism, which is indifferent to the well-being levels of those affected by gains and losses.[^note-1]

Although it is possible to construe prioritarianism as a non-axiological moral view, this entry follows the prevailing approach and trains its attention on axiological prioritarianism. We use the terms “good,” “bad,” “better,” and “worse,” applied to outcomes, as shorthand for *morally* good, bad, better, and worse. By an “outcome,” we mean a possible world—but our analysis transposes to “outcome” understood in related senses, e.g., as a simplified model of a possible world, or as a partial specification of a possible world sufficient to determine each person’s well-being.

The debate between prioritarians and their critics has generally concerned outcome betterness/worseness (what makes it the case that one outcome is better than, worse than, or equally good as a second) rather than outcome goodness/badness (what makes it the case that a given outcome is good or bad). This entry’s focus is the former. We will speak of prioritarianism as providing a “betterness ranking” of outcomes and contrast it with the betterness ranking offered by utilitarianism, egalitarianism, and sufficientism.

What is the relation between prioritarianism and consequentialism? Consequentialism is the class of moral views which stipulate that the moral status of choices (actions) is determined by moral axiology. More concretely: in a given choice situation, a *right* choice is a choice with an outcome that is at least as good as that of any other available choice; all other choices are *wrong*. Prioritarianism might be joined with consequentialism; if so, we have a moral theory which posits that the right choice in a given situation is the choice with the best outcome as per a prioritarian axiology. But it need not be thus joined. The moral status of choices might be determined *both* by the betterness ranking of outcomes *and* by other moral factors, such as deontological constraints. We bracket consequentialism, and in exploring prioritarianism assume only that axiology has *some* role in determining the moral status of choices.

The entry is organized as follows. Section 1 addresses the definition of prioritarianism. The definition employed here is: prioritarianism ranks outcomes according to the sum of *transformed* individual (lifetime) well-being: transformed by a strictly increasing and strictly concave function. Section 1 presents this definition and discusses alternatives. Section 2 discusses Derek Parfit’s 1991 Lindley Lecture (Parfit 2000)[^parfit-2000]—the scholarly work that drew significant philosophical attention to prioritarianism and thereby triggered intensive debates and analysis about the view. Section 3 reviews arguments in favor of prioritarianism. Section 4 discusses prioritarianism under uncertainty. Sections 5, 6, and 7 review challenges to prioritarianism by, respectively, utilitarians, egalitarians, and sufficientists.

The entry proceeds on the premise that the population of concern (those individuals whose well-being drives the betterness ranking) is: all human persons. This premise is generally adopted by the literature on prioritarianism, but—of course—is problematic in excluding non-human animals. How to extend prioritarianism to non-human animals is a topic of great importance for future research (cf. Vallentyne 2005, discussing egalitarianism and animals, and Holtug 2007b, discussing prioritarianism and animals)[^holtug-2007b][^vallentyne-2005], one that is not addressed here.

The “membership” of a given outcome is the subset of the population that exists in that outcome. The fixed-population component of a particular axiology specifies the betterness ranking of any group of outcomes all of which have the same membership. In presenting prioritarianism and considering alternatives (Sections 1 through 7), the entry simplifies matters by focusing on the fixed-population components of prioritarianism and competing axiologies. Section 8 addresses variable-population problems: how does prioritarianism rank outcomes with varying membership?[^note-2]

## 1. What is Prioritarianism?

### 1.1 Prioritarianism as a Betterness Ranking

Consider a set of outcomes $\mathbf{O}$, with a fixed membership: the very same human persons exist in all of the outcomes. Thus this is a fixed-population case. We’ll assume that there are $N$ such human persons in total. We’ll use “individual” to mean one of these human persons.

As is standard, we assume that the betterness ranking of $\mathbf{O}$ is transitive: if one outcome is at least as good as a second, and the second is at least as good as a third, then the first is at least as good as the third. To simplify the presentation, we also assume that this ranking is complete: as between any two outcomes, either the first is better than the second, or the second is better than the first, or the two are equally good.

Finally, lifetime well-being is measurable. In each outcome, each individual has a well-being number: $w_i (x)$ is the well-being number of individual $i$ in outcome $x$. These numbers represent intra- and interpersonal comparisons of lifetime well-being. Moreover, since neither utilitarianism nor prioritariansm is well-defined absent information about well-being differences, we’ll also assume that the numbers represent intra- and interpersonal comparisons of differences in lifetime well-being.[^note-3] (For the remainder of the entry, we use “well-being” as shorthand for “lifetime well-being.”)

Given well-being measurability, each outcome corresponds to a list of well-being numbers, one for each of the $N$ individuals.

A “welfarist” betterness ranking conforms to the axioms of *Pareto Indifference, Strong Pareto*, and *Anonymity*. *Pareto Indifference*: If each person is unaffected as between $x$ and $y$, the two outcomes are equally good. (An individual is “unaffected” as between two outcomes if equally well off in the two.) *Strong Pareto*. If each person is at least as well off in $x$ as in $y$, and at least one person is better off in $x$, then $x$ is better than $y$. *Anonymity*: If the list of individuals’ well-being levels in $x$ is a permutation of the list in $y, x$ and $y$ are equally good.

Pareto Indifference says: two outcomes don’t differ morally unless they differ with respect to at least one person’s well-being. Strong Pareto says: well-being makes a positive contribution to moral betterness. Anonymity says: it is the pattern of well-being in an outcome, impartially described, and not the identities of the individuals at particular levels, that matters for moral betterness. (See Adler 2022a for formal statements of these axioms and the Pigou-Dalton, Separability, and Continuity axioms discussed below.)[^adler-2022a][^adler-2022a-2]

Welfarism is controversial, to be sure, but for present purposes we take it as given. Both utilitarianism and prioritarianism (in its standard formulation) are welfarist. What prioritarianism puts on the table is the possibility of significant debate *within* the space of welfarist axiology.

The utilitarian betterness ranking assigns each outcome a score

$$ m^\textit{util}(x) = w_1 (x) + \ldots + w_N (x) $$

and ranks outcomes according to these scores. By contrast, a prioritarian betterness ranking assigns each outcome a score

$$m^\textit{prior}(x) = g(w_1 (x)) + \ldots + g(w_N (x)),$$

with $g(\cdot)$ a strictly increasing and strictly concave function (see Figure 1), and ranks outcomes according to *these* scores. To say that this function is “strictly increasing” means that it assigns greater values to greater inputs. To say that it is “strictly concave” means that it bends over: more precisely, that the $g(\cdot)$ value it assigns to any mixture of input values exceeds the mixture of their $g(\cdot)$ values.[^note-4]

![A graph of Transformed well-being g(w) in the y-axis against Well-being w in the x-axis. There is a solid concave curve beginning at (0,0) and arcing up. Four points on the curve are distinguished, given here in increasing order of x-axis value: (w_L, g(w_L)), (w_L+Delta_w, g(w_L+Delta_w), (w_H-Delta_w,g(w_H-Delta_w), (w_H,g(w_H)). The x-axis distance between w_L and w_L+Delta_w is the same as the x-axis distance between w_H-Delta_w and w_H. But the transformed well-being distance on the y-axis between the first pair g(w_L) and g(w_L+Delta_w) is greater than that between g(w_H-Delta_w) and g(w_H).](../assets/prioritarianism/figure1.png)

*Figure 1*

In a nutshell, utilitarian betterness is the sum of well-being, while prioritarian betterness is the sum of concavely transformed well-being. It is the concave transformation function, $g(\cdot)$, that allows prioritarianism to give priority to the worse off. (We use “concave” in reference to this transformation function as shorthand for strictly increasing and strictly concave.) Utilitarianism is a single ranking, while prioritarianism is a whole *family* of rankings—each member of this family defined by a specific transformation function. (See Adler 2022a regarding the choice of function.)[^adler-2022a][^adler-2022a-2]

Welfarist rankings that are neither utilitarian nor prioritarian are certainly available. The following possibilities are frequently discussed in the literature. (See Adler 2019 for formal statements of these rankings.)[^adler-2019][^adler-2019-2]

*A generalized-Gini ranking*: There are fixed positive weights $k_1 , \ldots ,k_N$, each larger than the next. A given outcome $x$ is assigned a score equaling $k_1$ times the lowest well-being number in $x$ plus $k_2$ times the second-lowest well-being number in $x$ plus … plus $k_N$ times the highest well-being number in $x$. Outcomes are ranked according to these scores. (Blackorby, Bossert, and Donaldson 2005, ch. 4; Buchak 2017, 2023)[^blackorby-2005][^buchak-2017][^buchak-2023].

*The leximin ranking*: Two outcomes are compared according to the well-being levels of the worst-off individuals, with $x$ better than $y$ if the worst-off individual in $x$ is better off than the worst-off individual in $y$; if the worst off are equally well off in the two outcomes, then they are compared according to the well-being levels of the second-worst-off individuals; etc. (Blackorby, Bossert and Donaldson 2005, ch. 4)[^blackorby-2005]

*A sufficientist ranking*. This ranking uses some threshold level of well-being $w^\textit{Thresh}$. An individual’s “capped” well-being equals her well-being, if less than $w^\textit{Thresh}$, otherwise $w^\textit{Thresh}$. An individual’s “bottomed” well-being equals her well-being, if greater than $w^\textit{Thresh}$, otherwise $w^\textit{Thresh}$. Each outcome is assigned two scores: a primary score equaling the sum of individuals’ concavely transformed capped well-being; and a secondary score equaling the sum of individuals’ bottomed well-being. Each pair of outcomes is ranked according to their primary scores; and, if those are equal, according to their secondary scores.

Via this formula, sufficientism gives absolute priority to the well-being of below-threshold individuals, over the well-being of above-threshold individuals; it converges with prioritarianism in comparing two outcomes such that all affected individuals are below the threshold; and it converges with utilitarianism in comparing two outcomes such that all affected individuals are above the threshold. (On sufficientism, see sources cited below, Section 7).

*Prioritarianism with a lexical threshold (PLT)*. The same formula as sufficientism, except that the secondary score for an outcome equals the sum of individuals’ concavely transformed bottomed well-being. (Like sufficientism, PLT gives absolute priority to the well-being of below-threshold individuals, over the well-being of above-threshold individuals. Unlike sufficientism, it converges with prioritarianism not only in comparing two outcomes such that all affected individuals are below the threshold, but also in comparing two outcomes such that all affected individuals are above the threshold.) (Brown 2005)[^brown-2005].

The distinctive features of prioritarianism, as compared both with utilitarianism and with welfarist rankings that are neither utilitarian nor prioritarian, are clarified by three axioms: *Pigou-Dalton*, *Separability*, and *Continuity*.

*Pigou-Dalton*. A pure transfer of well-being from a better-off to a worse-off person that shrinks the gap between their well-being levels and leaves everyone else unaffected is a moral improvement. (By “pure transfer,” we mean that the loss of well-being for the transferor equals the gain of well-being for the transferee.)

*Separability*. The ranking of two outcomes is independent of the well-being levels of unaffected individuals.

*Continuity*. If $x$ is better/worse than $y$, then $x^*$ is also better/worse than $y$ as long as everyone’s well-being in $x^*$ is sufficiently close to their well-being in $x$.

To illustrate, assume a population of four individuals. Let a list of four numbers, e.g. (3, 9, 1, 7), indicate the well-being levels of the four individuals in a given outcome. *Pigou-Dalton* requires that (10, 2, 25, 5) be worse than (7, 5, 25, 5), since we get from the first to the second outcome by transferring 3 units of well-being from the first to the second individual, affecting no one else and shrinking the gap between them. *Separability* requires that if (5, 5, 5, 5) is better than (10, 3, 5, 5), then (5, 5, 80, 30) is better than (10, 3, 80, 30). (Note that the third and fourth individuals are unaffected in the first pair of outcomes and that the second pair of outcomes is identical to the first except for those individuals’ well-being levels.) *Continuity* requires that if (1, 9, 12, 15) is better than (1, 7, 50, 100), then $(1 - \varepsilon,$ $9 - \varepsilon,$ $12 - \varepsilon,$ $15 - \varepsilon)$ is also better than (1, 7, 50, 100) for *ε* sufficiently small.

Table 1 states how the various betterness rankings fare with respect to these three axioms.

|   | *Pigou-Dalton* | *Separability* | *Continuity* |
| --- | --- | --- | --- |
| Utilitarianism | No | Yes | Yes |
| Prioritarianism | Yes | Yes | Yes |
| Generalized-Gini | Yes | No | Yes |
| Leximin | Yes | Yes | No |
| Sufficientism | No^{†} | Yes | No |
| PLT | Yes | Yes | No |

*Table 1.* ^{†} Pigou-Dalton not satisfied for transfers between above-threshold individuals

Several important points emerge from Table 1. First, Pigou-Dalton is the axiom that differentiates utilitarianism and prioritarianism. Utilitarianism fails Pigou-Dalton: if we reduce a better-off person’s well-being by $\Delta w$, and increase a worse-off person’s well-being by the same amount, the sum total of well-being is unchanged—and thus utilitarianism sees the transfer as a matter of moral indifference. Figure 1 illustrates why prioritarianism *satisfies* Pigou-Dalton: the increase in *concavely transformed* well-being of the worse-off individual (at well-being level $w_L)$ exceeds the loss in concavely transformed well-being of the better-off one (at $w_H)$.

Pigou-Dalton makes precise the sense in which prioritarianism gives “priority to the worse off” while utilitarianism does not.

Second, prioritarianism is the only one of these rankings that satisfies the trio of Pigou-Dalton, Separability, and Continuity. This is not because we’ve been selective in our choice of alternatives to prioritarianism. It can be shown that *if* a welfarist ranking satisfies this trio, it must be prioritarian (Adler 2022a, pp. 65–66)[^adler-2022a][^adler-2022a-2].

### 1.2 Prioritarianism as a Mode of Justification

We use “prioritarianism” to mean a particular family of betterness rankings: those that rank outcomes according to the sum of concavely transformed well-being. However, “prioritarianism” is sometimes used in a different way—to name a type of *justification* for a given ranking. In particular, debates between egalitarians and prioritarians are often (at least in part) debates about the mode of justification. (See Sections 2, 6.) In these debates, the term “egalitarianism” is often used to mean a mode of justification which gives intrinsic value to equality, and “prioritarianism” to mean a mode of justification that, inter alia, does not give intrinsic value to equality.

The following illustrates the difference between modes of justification and betterness rankings. Imagine that we adopt an egalitarian mode of justification. In order to operationalize this approach, we will need to specify how to measure the degree of well-being inequality in an outcome. Let $I(\cdot)$ be the inequality metric we adopt; $I(x)$ is the inequality score we assign to outcome $x$, with $I(x) \gt I(y)$ indicating that there is more well-being inequality in $x$ than $y$ (according to our chosen metric). If reducing inequality is *all* that we care about, we will violate the Strong Pareto axiom. So let’s assume that we care both about the degree of well-being inequality *and* about overall well-being. We justify the comparative betterness of a given pair of outcomes as a function of these *two* factors.

An important mathematical theorem, the “Decomposition Theorem,” shows the following (Adler 2022a, p. 100, n. 63)[^adler-2022a][^adler-2022a-2]. *Any* welfarist betterness ranking that satisfies the Pigou-Dalton and Continuity axioms can be expressed as ranking outcomes using the score $(w_1 (x) + \ldots + w_N (x)) - I(x)$ where $I(\cdot)$ is some inequality metric. The Decomposition Theorem applies to prioritarian rankings. While the standard formula for prioritarianism is to score outcomes using the score $m^\textit{prior}(x) = g(w_1 (x)) + \ldots + g(w_N (x)),$ the Decomposition Theorem shows that the very same ranking (for any given transformation function) can be achieved using a different scoring method, namely $(w_1 (x) + \ldots + w_N (x)) - I(x)$, for some inequality metric $I(\cdot)$.

The Decomposition Theorem crisply illustrates the possibility of an *egalitarian* justification for a *prioritarian* ranking. *Whatever* the transformation function $g(\cdot)$, there is some inequality metric such that the prioritarian ranking using that transformation function is exactly the ranking that would emerge via an egalitarian mode of reasoning: balancing overall well-being against inequality as measured by $I(\cdot)$. On this topic, see Fleurbaey (2015)[^fleurbaey-2015]; Jensen (2003)[^jensen-2003].

To avoid confusion, we will explicitly use the term “mode of justification” or a similar term whenever “egalitarian” and “prioritarian” are used to designate one or another such mode.

### 1.3 A Risk-Based Definition of Prioritarianism

Unlike much of the literature, David McCarthy (2013, 2017)[^mccarthy-2013][^mccarthy-2017] defines prioritarianism neither as a type of betterness ranking of outcomes, nor as a mode of justification, but instead as a cluster of axioms for ranking lotteries. Space constraints preclude a discussion of McCarthy’s view here; see Adler and Holtug (2019)[^holtug-2019].

## 2. Parfit

Prioritarianism comes to prominence in the philosophical literature with Derek Parfit’s 1991 Lindley Lecture (Parfit 2000)[^parfit-2000]. Although some philosophers (McKerlie 1984; Temkin 1983; Weirich 1983)[^mckerlie-1984][^temkin-1983][^weirich-1983] and also some economists had discussed prioritarianism (not using that terminology; see Adler and Norheim 2022b for a survey)[^adler-2022b][^adler-2022b-2] prior to the Lindley Lecture, this is the scholarly work that triggered intensive philosophical debate about the view.

In the lecture, Parfit introduces prioritarianism by discussing a hypothetical case previously described by the philosopher Thomas Nagel (1979, pp. 123-24). In this case, Nagel has to choose between living in the suburb, which is better for one of his children, who is healthy; and living in the city, thereby providing access to treatment for a second child, who has a serious health condition. The gain to the first child from living in the suburb is greater than the gain to the second child from living in the city. Parfit represents the interests of the two children using the numbers displayed in Table 2 (everyone else is unaffected).

|   | *First Child* | *Second Child* |
| --- | --- | --- |
| Move to the city | 20 | 10 |
| Move to the suburb | 25 | 9 |

*Table 2.*

Utilitarianism recommends moving to the suburb. The sum total of the children’s well-being in the suburb $(25 + 9)$ is greater than the sum total of their well-being in the city $(20 + 10)$. Nagel supposes that, if he decides instead to move to the city, “it would be an egalitarian decision” (Parfit 2000, p. 81)[^parfit-2000]. Parfit uses the case to explore the content of egalitarianism and to propose an alternative rationale for moving to the city: “the Priority View” (or, as it’s come to be known, “prioritarianism”). Parfit discusses both axiological (“Telic”) and deontic egalitarianism. Because our interest here is axiology, we leave aside Parfit’s analysis of deontic egalitarianism and focus on the contrast he draws between axiological egalitarianism and prioritarianism. In what follows, “axiological” is implicit.

The version of egalitarianism that Parfit explores is “pluralist” egalitarianism, which endorses two principles: a “principle of equality” (“It is in itself bad if some people are worse off than others”) and a “principle of utility” (“It is in itself better if people are better off”) (p. 84). Pure egalitarianism, consisting only of the first principle, would be indifferent between everyone being equally well off at a given level of well-being, and everyone being equally well off at a higher level of well-being. Pluralism is needed to avoid this result. Pluralist egalitarianism, in turn, can take a “strong” or “moderate” form. To see the contrast between the two, consider two outcomes $x$ and $y$ such that some are worse off in $y$ and no one is better off, but well-being is more equally distributed in $y$ than $x$. Strong pluralist egalitarians recognize some such cases in which, on balance, $y$ is better than $x$. Moderate pluralist egalitarians insist that, in every such case, $y$ is on balance worse than $x$. In short, moderate pluralist egalitarians endorse an all-things-considered betterness ranking (taking account of both the principle of equality and the principle of utility) that satisfies the Strong Pareto axiom, while strong pluralist egalitarians endorse an all-things-considered betterness ranking that violates the Strong Pareto axiom.

Parfit notes that egalitarianism is subject to what he calls the “Levelling Down Objection.”

> If inequality is bad, its disappearance must be in one way a change for the better, *however this change occurs*. Suppose that those who are better off suffer some misfortune, so that they become as badly off as everyone else. Since these events would remove the inequality, they must be in one way welcome [for egalitarians], even though they would be worse for some people, and better for no one. This implication seems to many to be quite absurd. I call this *the* *Levelling Down Objection*. (p. 98)

Pure egalitarianism and strong pluralist egalitarianism are clearly subject to the Levelling Down Objection. What’s critical to recognize is that *moderate* pluralist egalitarianism is *also* subject to this objection. Return again to the case in which some are worse off in $y$ than $x$, none are better off, but well-being is more equally distributed in $y$. Even *moderate* pluralist egalitarians agree that $y$ is better than $x$ *in one respect*. Pure, strong pluralist, and moderate pluralist egalitarians *all* endorse the principle of equality. Well-being is more equally distributed in $y$ and so—on any view that endorses this principle—$y$ is better in one respect than $x$.

Egalitarians may well not be bothered by the Levelling Down Objection. Our aim, here, is not to consider the persuasiveness of that objection, but rather to see how it figures in Parfit’s distinction *between* egalitarianism and prioritarianism (but for further discussion of the objection, see Section 6.1).

Having discussed egalitarianism, Parfit turns to an alternative rationale for departing from utilitarianism in the two-child case: “*The Priority View*: Benefitting people matters more the worse off these people are” (p. 101).

> For Utilitarians, the moral importance of each benefit depends only on how great this benefit would be. For *Prioritarians*, it also depends on how well off the person is to whom this benefit comes. We should not give equal weight to equal benefits, whoever receives them. Benefits to the worse off should be given more weight. (p. 101)

Although Parfit does not say so explicitly, he uses “prioritarianism” (“the Priority View”) to mean both a mode of justification and a betterness ranking. A careful reading of the Lindley Lecture allows us to unpack these two strands.

(1) *Mode of Justification*. “Egalitarianism,” for Parfit, clearly is a mode of justification, a way to think about moral betterness: one that justifies the outcome ranking at least in part by appeal to the principle of equality. Prioritarianism, by contrast, appeals to a different idea, namely that “benefitting people matters more the worse off these people are.” Parfit’s view of egalitarianism and prioritarianism as distinct modes of justification is made clear, for example, when he writes: “On [the Priority View], we do *not* believe in equality. We give priority to the worse off, not because this will reduce inequality, but for other reasons” (p. 103). Parfit, here, is distinguishing between egalitarian *reasons* for channeling well-being improvements to the worse-off rather than the better-off (namely, that doing so reduces well-being inequality) and prioritarian *reasons* for doing that (namely, that well-being increments have greater moral weight if received by those who are worse off). Parfit is also thinking of egalitarianism and prioritarianism as distinct modes of justification when he states that prioritarianism avoids the Levelling Down Objection. In the $x/y$ case above, both prioritarians and moderate pluralist egalitarians would agree that $x$ is better. The ranking of the two outcomes is the same. And yet (as Parfit sees it) prioritarianism avoids the Levelling Down Objection because the *reason* it gives for $x$ being better is that an increase in someone’s well-being always makes a positive moral contribution, while moderate pluralist egalitarianism runs afoul of that Objection because it gives a different *reason* for $x$ being better (namely, that equality and overall well-being balance against each other so as to result in that ranking).

(2) *Betterness Ranking*. Parfit does not explicitly articulate the prioritarian betterness ranking in the standard form now adopted in the philosophical literature, namely as the sum of concavely transformed well-being (see Section 1) or, equivalently, as a ranking that satisfies Pareto Indifference, Strong Pareto, Anonymity, Pigou-Dalton, Separability, and Continuity. But Parfit describes the commitments of prioritarianism, as regards moral betterness, so as to suggest that it endorses all of these axioms. Pareto Indifference and Anonymity are implicit in his treatment of both egalitarian and prioritarian axiology; in both cases, what matters is the pattern of well-being, impartially considered. As for Strong Pareto, Parfit writes: the Priority View “contains the idea that benefits are good” (pp. 103–04). As for Pigou–Dalton: “benefits matter more the worse off the people are who receive them” (p. 104). (This statement and similar statements are Parfit’s summary of prioritarian *reasoning*, but they also directly support Pigou-Dalton.)

As for Separability, the Lindley Lecture stresses that prioritarians do not care about “relativities.”

> [O]n the Priority View, we do not believe in equality. We do not think it in itself bad, or unjust, that some people are worse off than others. This claim can be misunderstood. We do of course think it bad that some people are worse off. But what is bad is not that these people are worse off than *others*. It is rather that they are worse off than *they* might have been.
>
> Consider next the central claim of the Priority View: benefits to the worse off matter more. … On this view, if I am worse off than you, benefits to me are more important. Is this *because* I am worse off than you? In one sense, yes. But this has nothing to do with my relation to you.
>
> It may help to use this analogy. People at higher altitudes find it harder to breathe. Is this because they are higher up than other people? In one sense, yes. But they would find it just as hard to breathe even if there were no other people who were lower down. In the same way, on the Priority View, benefits to the worse off matter more, but that is only because these people are at a lower *absolute* level. It is irrelevant that these people are worse off *than others*. …
>
> The chief difference is, then, this. Egalitarians are concerned with *relativities*: with how each person’s level compares with the level of other people. On the Priority View, we are concerned only with people’s absolute levels. (p. 104)

Separability is a crisp axiomatic expression of an absence of concern with relativities. Finally, Parfit writes that, for prioritarians, “utility [well-being] has diminishing marginal *moral importance*” (p. 105). This statement supports not only the Pigou-Dalton axiom but also (for technical reasons) the Continuity axiom, since to speak of the “marginal moral importance” of well-being assumes that there is a differentiable and, hence, continuous function mapping the array of individual well-being numbers in an outcome onto its moral value.

## 3. Arguments for Prioritarianism

The arguments that follow work within welfarism, i.e., take as given Pareto Indifference, Strong Pareto, and Anonymity. Pigou-Dalton is the axiom that distingishes prioritarianism from utilitarianism, and that encapsulates the sense in which prioritarianism accords priority to the worse off. Betterness rankings that respect Pigou-Dalton might be termed “extended prioritarian.” These include not merely prioritarianism proper, but also generalized-Gini rankings, leximin, and PLT rankings.

We consider, first, arguments for Pigou-Dalton—that is, for the wide class of *extended-prioritarian* betterness rankings—and then, within that class, for Separability and for Continuity.

### 3.1 Defending Extended Prioritarianism: Arguments for Pigou-Dalton

A variety of arguments for Pigou-Dalton can be gleaned from the literature. In what follows, by “Pigou-Dalton transfer,” we mean a change in individuals’ well-being that meets the condition for the Pigou-Dalton axiom: a better-off individual’s well-being decreases by $\Delta w$, a worse-off individual’s well-being increases by the same amount, the gap between them shrinks, and everyone else is unaffected.

(1) *Egalitarian Reasoning*. An egalitarian mode of justification, to be consistent with the Strong Pareto axiom, needs to be pluralist (as explained by Parfit in the Lindley Lecture). Most simply, pluralist egalitarianism considers two factors: overall well-being and the degree of well-being inequality. A standard inequality metric $I(\cdot)$ is such that, if $y$ is reached from $x$ via a Pigou-Dalton transfer, then $I(y) \lt I(x)$. (Cowell 2016)[^cowell-2016]. Further, in the case of a Pigou-Dalton transfer, overall well-being remains constant. Thus we have a straightforward *egalitarian* argument for why $y$ is better than $x$: one factor (the degree of inequality) is improved with $y$, and the second factor (overall well-being) remains constant. (See Weirich 1983, justifying a Pigou-Dalton respecting betterness ranking via pluralist egalitarianism.)[^weirich-1983]

(2) *Parfit*. Although Parfit (2000)[^parfit-2000] does not cleanly define the axiomatic commitments of prioritarianism (let alone use the term “Pigou-Dalton”), one can distill an argument for Pigou-Dalton from his text. The core of the argument is the distinction between *benefits* and the *moral weight of benefits*. Imagine that Ada is better off in outcome $y$ than $x$, and that Barry is better off in outcome $y^*$ than $x^*$. Assume that the well-being differences are the same; each benefits by the same amount, in well-being terms. The moral weight of the benefits need not be the same. In particular, positing that the moral weight of benefits *decreases* as individuals become better off is intuitively plausible. This supposition explains intuitively plausible departures from utilitarianism (e.g., in Nagel’s two-child case, the decision to benefit the worse-off child); *and* it does so without relying on egalitarian reasoning (and thus running afoul of the Levelling Down Objection).

(3) *Claims Across Outcomes*. Matthew Adler (2025)[^adler-2025] introduces the claims-across-outcomes framework for arriving at the betterness ranking. As between any two outcomes, a given individual has a claim in favor of the outcome in which they are better off (and a null claim if equally well off). In two-person cases, where one person has a claim to $x$ over $y$, the other to $y$ over $x$, and everyone else is unaffected, the better outcome is the one favored by the person with the stronger claim. Adler argues that this framework offers a joint justification of Strong Pareto, Pareto Indifference, Anonymity and Pigou-Dalton. To see how it argues for Pigou-Dalton, note that a Pigou-Dalton transfer is a two-person case. Let $x$ be the pre-transfer outcome, and $y$ the post-transfer outcome. The better-off individual (Iris) in $x$ has a claim to $x$ over $y$, the worse-off individual (Juan) to $y$ over $x$, with everyone else having null claims. The strength of an individual’s claim may reflect their well-being difference, their starting point well-being level, or both. In the case at hand, the well-being differences are the same. If well-being level has *any* role in determining claim strength, then it comes into play in this case; and it does so, specifically, by giving Juan (not Iris) the stronger claim.

(4) *The Moral Value of Compound States of Affairs*. Nils Holtug (2010, p. 204) has proposed an axiological account, according to which compound states of affairs, each consisting of the state that an increase in well-being befalls an individual and the state that this individual is at a particular well-being level, hold moral value. The larger the increase in well-being, and the lower the level at which it falls, the larger this value. In a Pigou-Dalton transfer, where a fixed sum of well-being is shifted from a better-off person to a worse-off person, shrinking the distance between them, this well-being falls at a lower level in the post-transfer outcome than in the pre-transfer outcome, resulting in an overall increase in moral value.

(5) *Risk-Weighted Expected Utility Theory*. Lara Buchak (2017)[^buchak-2017] proposes that distributions of well-being across a fixed population of $N$ individuals be evaluated using an equiprobability veil of ignorance. The evaluator conceptualizes a given distribution as giving them (the evaluator) a $1/N$ probability of the well-being of each of the $N$ individuals. The veil-of-ignorance construct has a long history in ethics, dating back to Harsanyi (1953, 1955, 1977)[^harsanyi-1953][^harsanyi-1955][^harsanyi-1977] and Rawls (1999)[^rawls-1999]. Buchak’s twist is to argue that the evaluator should employ risk-weighted expected utility theory (REU) to evaluate well-being lotteries, rather than expected utility theory (the standard normative theory of choice under uncertainty). REU differs from expected-utility theory by incorporating what Buchak terms a “risk function,” which reflects whether the decisionmaker is “risk-avoidant” (giving more weight to the possibility of bad outcomes), “risk-seeking,” or risk-neutral.

Buchak argues that the evaluator behind the veil of ignorance should be risk-avoidant. Given the formal structure of REU, this means that the evaluator ranks distributions according to a generalized-Gini rule. Note that the generalized-Gini rule satisfies Pigou-Dalton. Less formally: a risk-avoidant evaluator, behind the veil of ignorance, gives greater weight to the possibility of low well-being levels, and thus favors distribution $D^*$ over distribution $D$ if $D^*$ is reached from $D$ by a Pigou-Dalton transfer.

(6) *Retaining Expected Utility Theory but Dropping Bernoulli*. The Bernoulli axiom (see below, Sections 4.2–4.3) posits that the ranking of prospects in light of a given person’s well-being conforms to the expected value of that person’s well-being. Although widely adopted in the literature, the Bernoulli axiom might be dropped. If expected utility theory is retained as the normative theory of choice under uncertainty (pace Buchak) but Bernoulli is dropped, two new arguments for extended prioritarianism emerge. Indeed, these are arguments for *prioritarianism* specifically rather than merely for extended prioritarianism. One argument appeals to John Harsanyi’s “Aggregation Theorem”; this argument is discussed below in Section 4.3. A second argument appeals to the veil of ignorance, but in a different manner than Buchak; this argument is discussed below in Section 5.3.

Arguments (3), (4), (5) and (6) for the Pigou-Dalton principle, like argument (2), never assign pro tanto moral value to a reduction in individuals’ well-being, and thus also avoid the Levelling Down Objection.

### 3.2 From Extended Prioritarianism to Prioritarianism: Arguments for Separability and Continuity

The prioritarian betterness ranking satisfies Pigou-Dalton *and* Separability *and* Continuity. The arguments above for Pigou-Dalton are generally *consistent* with Separability and Continuity. (The one exception is Buchak’s argument, argument (5), which supports Pigou-Dalton by way of a defense of generalized-Gini moral betterness, thereby rejecting Separability.) However, arguments (1), (2), (3), and (4) do not themselves show why Separability and Continuity should be adopted. To arrive at prioritarianism using one of these arguments, additional considerations need to be provided to support Separability and Continuity.

#### 3.2.1 Separability

(1) *Egyptology*. Parfit, in *Reasons and Persons* (1987), famously offers the following argument against average utilitarianism (a variable-population extension of utilitarianism, which violates Separability in the variable-population context).

> Whether [the birth of a child] would be bad [according to average utilitarianism] depends on facts about all previous lives. If the Ancient Egyptians had a very high quality of life, it is more likely to be bad to have a child now. It is more likely that this child’s birth will lower the average quality of the lives that are ever lived. But research in Egyptology cannot be relevant to our decision whether to have children. (p. 420)

This has come to be known as the “Egyptology” argument for Separability. It also applies in the fixed-population context. In a nutshell, the argument is this. Let $x$ and $y$ differ with respect to the well-being of one or more individuals, the affected individuals. If the betterness ranking violates Separability, it is possible that how $x$ morally compares to $y$ depends upon the well-being levels of unaffected individuals who are temporally remote from all of the affected individuals (e.g., some unaffected individuals lived in ancient Egypt, while the affected individuals were born after 1900), or spatially remote from all of the affected individuals (some unaffected individuals live on Mars, while the affected individuals live on Earth). And this is counterintuitive. See Table 3, showing specifically how generalized-Gini moral betterness (which violates Separability) runs afoul of the Egyptology objection.

|   | *Outcome $x$* | *Outcome $y$* | *Outcome $x^*$* | *Outcome $y^*$* |
| --- | --- | --- | --- | --- |
| Able | 50 | 54 | 50 | 54 |
| Baker | 100 | 90 | 100 | 90 |
| Rick | 70 | 70 | 10 | 10 |
| Generalized-Gini outcome score (integer weights) | 390 | 392 | 230 | 228 |

*Table 3.* *Explanation*: Assume that Rick is remote from Able and Baker. Rick’s well-being is the same in each outcome pair $(x/y)$ and $(x^*/y^*)$, i.e. only Able and Baker are affected in each outcome pair. However, because Rick’s position relative to Able and Baker is different in the two pairs, the generalized-Gini ranking of the first pair is not the same as its ranking of the second, in violation of Separability.

(2) *Tractability*. A betterness ranking of outcomes is (plausibly) associated with a betterness ranking of *prospects*. This prospect ranking encapsulates how the outcome ranking provides guidance with respect to moral deliberation. Separability at the level of the outcome ranking is a necessary condition for the prospect ranking to satisfy the axiom of *Prospect Separability*. (See Section 4.2.) Prospect Separability, in turn, substantially facilitates moral deliberation. It means that the decisionmaker can ignore individuals who are *sure to be unaffected* by the decisionmaker’s choice.

(3) *Claims Across Outcomes*. Adler (2012, ch. 5) argues that the claims-across-outcomes framework supports not only Pigou-Dalton, but also Separability. Imagine that Jia is better off in outcome $y$ than outcome $x$, and thus has a claim to $y$ over $x$. Rejecting Separability means that the strength of Jia’s claim depends not merely upon her starting-point well-being level (in $x)$ and her well-being difference between the two outcomes, but a *further* factor: how her well-being compares to the well-being of unaffected individuals. An affirmative argument for this relational determinant of claim strength is hard to muster. Granted, the well-being of unaffected individuals may affect Jia’s *well-being*. But that impact will be reflected in Jia’s own well-being in the two outcomes. Why unaffected individuals should determine the *claim strength* of affected individuals, on top of (potentially) determining their well-being, is hard to see.

#### 3.2.2 Continuity

The discussion of the Continuity axiom in the literature on prioritarianism has focused, not on the axiom as such (which is a technical axiom that doesn’t elicit strong favorable or unfavorable intuitions on its own), but on the properties of the betterness rankings that satisfy or fail this axiom. Within the space of extended-prioritarian rankings, the main alternatives to prioritarianism that fail Continuity and that have been considered thus far in the literature are leximin and PLT. Note that both satisfy Pigou-Dalton and Separability; the axiomatic difference between these rankings and prioritarianism is *just* a matter of the Continuity axiom.

Leximin gives absolute priority to every worse-off individual over every group of better-off individuals. Imagine that Darsh in outcome $x$ is worse off than everyone in some group of individuals. In outcome $y$, Darsh is worse off than he is in $x$; everyone in the group is better off than they are in $x$; all others are unaffected. Then leximin *necessarily* counts $y$ as worse than $x$—even if Darsh in $x$ is only slightly worse off than those in the group; regardless of how small Darsh’s well-being loss, and how large their gains; and regardless of the size of the group. This seems implausibly extreme. To make the example more concrete: imagine that Darsh and everyone in the group suffers a chronic serious, health condition; Darsh also suffers from intermittent tension headaches. A pill can be used to prevent Darsh’s headaches from becoming slightly more severe, or to cure everyone in the group of the health condition. Leximin prefers to use the pill to prevent Darsh’s headaches from becoming slightly more severe—which seems implausible enough if there is just one person in the group, let alone if there are dozens, hundreds, or thousands.

PLT does not give absolute priority to a worse-off individual over a group of better-off individuals if all the individuals are on the same side of the threshold. But it does do so if the worse-off individual is below the threshold and the group is above. Again, this may seem implausible. For example, consider a PLT betterness ranking that sets the threshold $w^{\textit{Thresh}}$ at the level of need-satisfaction: the well-being level of an individual whose basic needs are satisfied, but has no other positive sources of well-being in her life. Imagine, now, that Darsh is needy in $x$. Darsh is worse off in $y$ than $x$; some group of non-needy persons are better off in $y$ than $x.$ PLT necessarily prefers $x$ to $y$—even if Darsh is only slightly worse off than those in the group in $x$; regardless of how small Darsh’s well-being loss, and how large their gains; and regardless of the size of the group.

That said, the absolutism of both leximin and PLT is not a logical implication of dropping Continuity. More precisely, there are extended-prioritarian betterness rankings that, like leximin and PLT, satisfy Separability; that, like them, fail Continuity; but do not give absolute priority to any individual over a sufficiently large group of better-off individuals. For example, consider the following multi-step rule: (1) $x$ is better than $y$ if the sum of transformed well-being in $x$ is greater than the sum of transformed well-being in $y$, using strictly increasing and strictly concave transformation function $g(\cdot)$; (2) if $x$ and $y$ have equal sums of $g(\cdot)$-transformed well-being, then $x$ is better than $y$ if the sum of transformed well-being in $x$ is greater than the sum of transformed well-being in $y$, using a *different* strictly increasing and strictly concave transformation function $f(\cdot)$: and (3) if $x$ and $y$ are ranked equally good at both step 1 and step 2, then they are equally good.

The substantive attractiveness of such non-absolutist extended-prioritarian rankings that differ from prioritarianism only in failing Continuity remains to be investigated.

## 4. Prioritarianism under Uncertainty

In decision theory, a standard set-up for representing choice under uncertainty is the *prospect* framework. There is a collection of mutually exclusive “states of nature,” each assigned a fixed probability. A given prospect $P$ associates each state-of-nature with some outcome. See Table 4.

|   | A prospect $P$ |   |   |   |
| --- | --- | --- | --- | --- |
| State | $s^*$ | $s^{**}$ | $s^{***}$ | $s^{****}$ |
| Probability | $\pi(s^*)$ | $\pi(s^{**})$ | $\pi(s^{***})$ | $\pi(s^{****})$ |
| Outcome | $x$ | $y$ | $z$ | $zz$ |

*Table 4.* *Explanation*: $\pi(s)$ is the probability of a given state *s.*

The set of prospects (for a given group of states-of-nature) is an abstract representation of a decisionmaker’s choice situation. The decisionmaker (Dolores) is *uncertain* about the features of the world that determine which outcome would result, for any given choice available to her. Dolores’ uncertainty is represented in the assignment of probabilities to the states-of-nature; the probability of a state-of-nature represents her degree of belief that this is the actual state-of-nature. Each choice available to Dolores corresponds to one or another prospect; the prospect says what the outcome would be, for each of the states-of-nature to which Dolores assigns some (nonzero) degree of belief.

The prospect framework has many applications. The one of interest here concerns moral axiology. The *choice guidance* given by a moral axiology can be systematized in how it ranks prospects. A particular axiology (betterness ranking of outcomes) does not uniquely determine a betterness ranking of prospects, but rather is associated with a plurality of prospect-ranking rules. In selecting between these rules, we specify what the axiology says to a non-omniscient (e.g., human) decisionmaker. Economists and philosophers have used the prospect framework to clarify the choice guidance of various axiologies, including utilitarianism, prioritarianism, and others. (See, e.g., Adler 2022a; Fleurbaey 2010; Mongin and Pivato 2016)[^adler-2022a][^adler-2022a-2][^fleurbaey-2010][^mongin-2016].

Momentarily, we’ll discuss the various prospect-ranking rules for a prioritarian axiology. First, however, we consider the proposal that prioritarian axiology fixes prospect rankings only indirectly.

### 4.1 Factualism

A basic distinction, when theorizing choices under uncertainty, is that between factualism and probabilism. According to factualism, choices should be morally assessed on the basis of the outcomes to which they will *in fact* lead. According to probabilism, on the other hand, choices should be morally assessed on the basis of the outcomes to which they *can* lead and their probabilities (that is, on the basis of the associated prospects). Probabilist forms of prioritarianism will be discussed in Section 4.2. Prioritarian factualism has been defended by Holtug (2019)[^holtug-2019], and essentially claims that the ranking of choices is determined by the value of the outcomes to which they will actually lead, where this value is assessed on the basis of the prioritarian betterness ranking. Thus, if a choice, $C$, leads to outcome $x$, and another choice, $C^*$, leads to outcome $y, C$ is better than $C^*$ if and only if $x$ is better than $y$ according to that outcome ranking.

Factualist prioritarianism does not directly inform a decisionmaker how to make choices under uncertainty, as she will then not know what the actual outcomes of the available choices are. But factualists argue that the question of how to make decisions is separate from the question of the moral rightness of choices, and that the former question needs to be addressed in terms of a decision procedure (Bales 1971; Hare 1981, ch. 2)[^bales-1971][^hare-1981]. The decision procedure we have most reason to adopt, according to factualist prioritarians, is the procedure that, if adopted, would best promote the aim of realizing the outcomes that are highest in the prioritarian ranking. This procedure will include information about how best to make choices under uncertainty. Once the prioritarian outcome betterness ranking is fully settled, specifying the content of the decision procedure will largely rely on empirical considerations about the aptness of different procedures as regards realizing the prioritarian aim. Perhaps this procedure implies that the decisionmaker should sometimes make a choice that maximizes *expected* prioritarian value (see the discussion of ex post prioritarianism below). But, if so, the only reason to maximize expected value is that we want the value that is *in fact* realized to be maximized (Carlson 1995, pp. 20–25)[^carlson-1995]. Thus, aiming to maximize expected prioritarian value is only an indirect strategy to realize what ultimately matters, namely the prioritarian value that is in fact realized. (For critical discussion of factualist prioritarianism, see Arneson 2022: 60–62)[^arneson-2022]

### 4.2 Prioritarian Prospect-Ranking Rules

As stated, there are also probabilist prioritarian theories. Consider a prioritarian betterness ranking (for short, $R)$: the ranking of a set $\mathbf{O}$ of outcomes using some strictly increasing and strictly concave transformation function. For any collection of states-of-nature (representing a decisionmaker’s uncertainty about the conditions in the world that determine which outcome would result for each of the choices available to the decisionmaker), there is a set $\mathbf{P}$ of prospects. Each prospect $P$ associates a state-of-nature with some outcome in $\mathbf{O}. R$ has a variety of associated prospect-ranking rules: rules for ranking $\mathbf{P}$.

In what follows, we present prioritarian prospect-ranking rules; we set forth prospect axioms; and we evaluate the rules in light of the axioms. For purposes of this discussion, we adopt the following premise.

*Bernoulli*: The ranking of prospects in light of a given person’s well-being tracks that person’s expected well-being. Let Leila be some person and $P, P^*$ two prospects. (1) If Leila’s expected well-being with $P$ equals her expected well-being with $P^*$, then $P$ is equally good for Leila as $P^*$. (2) If Leila’s expected well-being with $P$ is greater than her expected well-being with $P^*$, then $P$ is better for Leila than $P^*$.

The Bernoulli assumption is regularly adopted in the literature on moral choice under uncertainty, but is also controverted. The possibility of dropping Bernoulli is discussed below, in Section 4.3.

Turn, then, to prioritarian prospect-ranking rules. Three possibilities are prominent in the literature: “ex post prioritarianism” (EPP), “ex ante prioritarianism” (EAP), and “expected equally distributed equivalent prioritarianism” (EEDEP). (Formal statements of these rules and the axioms below are given in Adler 2022a; on prioritarianism under uncertainty, see also Bovens 2015; Fleurbaey 2010; Greaves 2015; McCarthy 2006, 2008; Otsuka and Voorhoeve 2009, 2018; Parfit 2012; Rabinowicz 2001)[^adler-2022a][^adler-2022a-2][^bovens-2015][^fleurbaey-2010][^greaves-2015][^mccarthy-2006][^mccarthy-2008][^otsuka-2009][^otsuka-2018][^parfit-2012][^rabinowicz-2001]. Each approach assigns a score to a given prospect in a distinctive manner, and ranks $\mathbf{P}$ according to these scores:

EPP (*ex post prioritarianism*). The outcome in each state-of-nature is assigned a “moral utility” number equaling the sum of concavely transformed well-being in that outcome. The prospect is assigned a score equaling its expected outcome utility (the sum of the outcome utilities, each discounted by the state’s probability). In short, EPP’s scoring formula is the *expected sum of concavely transformed well-being*.

EAP (*ex ante prioritarianism*). For each individual, their expected well-being with the prospect is calculated. These expected well-being values are plugged into the transformation function and summed. In short, EAP’s scoring formula is the *sum of concavely transformed expected well-being*.

EEDEP (*expected equally distributed equivalent prioritarianism*). EEDEP works the same way as EPP, except that the outcome in each state-of-nature is assigned a different moral utility: its “equally distributed equivalent.” The equally distributed equivalent of an outcome $x$ is that single well-being level $w^*$ which, if had by everyone, has the same prioritarian value as $x$. Formally, $w^*$ is such that $N \times g(w^*) = g(w_1 (x)) + \ldots + g(w_N (x))$. In short, EEDEP’s scoring formula is the *expected equally distributed equivalent*.

Prospect-ranking rules can be evaluated by means of prospect axioms. The following axioms bring into view the pros and cons of EPP, EAP, and EEDEP.

*Expected Utility Decisionmaking*. Each outcome should be assigned a moral utility that is *consistent* with the prioritarian betterness ranking $R$ (higher utility to better outcomes, equal utility for equally good outcomes). The score of a prospect is its expected utility, and prospects are ranked according to these scores.

*State Dominance*. Assume prospects $P^*$ and $P$ are such that, in each state-of-nature, the outcome of $P^*$ is ranked better by $R$ than the outcome of $P$. If so, $P^*$ is better than $P$.

*Ex Ante Pareto*. (i) *Ex Ante Pareto Indifference*. Assume that prospect $P^*$ is equally good for each person as prospect $P$. (Given Bernoulli, this condition can be restated as: each person’s expected well-being with $P^*$ is equal to their expected well-being with $P$.) If so, $P^*$ and $P$ are equally good. (ii) *Ex Ante Strong Pareto*. Assume that prospect $P^*$ is at least as good for each person as prospect $P$, and strictly better than $P$ for at least one person. (Given Bernoulli, this condition can be restated as: each person’s expected well-being with $P^*$ is greater than or equal to their expected well-being with $P$, and at least one person has strictly greater expected well-being with $P^*$.) If so, $P^*$ is better than $P$.

*Prospect Separability*. Assume that one or more persons are “sure to be unaffected” as between prospects $P$ and $P^*$. That is, in each state-of-nature, each person’s well-being with $P$ is the same as their well-being with $P^*$. If so, the $P/P^*$ ranking is independent of what these state-by-state levels are.

Each of these axioms seems quite plausible. In brief, the case for each is as follows. (1) *Expected Utility Decisionmaking*. Expected-utility theory posits axioms sufficient to demonstrate the existence of a utility function, which conforms to the betterness ranking of outcomes (one outcome is at least as good as a second if and only if the utility of the first outcome is at least as large as the utility of the second outcome), and which is such that the expectation of outcome-utility tracks choiceworthiness (one choice is at least as good as a second if and only if the expected utility of the first choice is at least as large as the expected utility of the second). (Briggs 2023; Kreps 1998; Gilboa 2009)[^briggs-2023][^gilboa-2009]. The axiom on hand, here, applies expected utility theory to the problem of ranking choices in light of the *moral* betterness of outcomes, as per the prioritarian betterness ranking $R$. (2) *State Dominance*. If one prospect is better than another, whatever the state-of-nature may be, then surely it is better. (State Dominance is a logically weaker axiom than Expected Utility Decisionmaking: if a prospect-ranking rule satisfies the latter, it necessarily satisfies the former.) (3) *Ex Ante Pareto*. These axioms can be defended by appeal to individuals’ prudential viewpoints (a given individual’s “prudential viewpoint” is focused on the well-being of that person). If two prospects $P^*$ and $P$ meet the antecedent condition for Ex Ante Pareto Indifference, then they are equally good from each individual’s prudential viewpoint. If $P^*$ and $P$ meet the antecedent condition for Ex Ante Strong Pareto, then $P^*$ is better from at least one individual’s prudential viewpoint, and no worse from anyone’s. Whatever our prospect ranking when prudential viewpoints conflict, shouldn’t we respect those viewpoints *at least* in the cases described by these axioms? (4) *Prospect Separability*. Assume that some individuals are causally remote from the decisionmaker. Dolores, the decisionmaker, is confident that, whatever the state-of-nature, her choice will not change the well-being of these individuals. This would be true, for example, of individuals who were born in the past and are already dead; and perhaps of individuals in sufficiently distant locations (distant planets). $\mathbf{P}$ is the set of prospects corresponding to Dolores’ choice situation. Each causally remote individual is sure-to-be-unaffected for all of the prospects in $\mathbf{P}$; the individual’s well-being in a given state does not vary with the prospects in $\mathbf{P}$. *If* the prospect-ranking rule satisfies Prospect Separability, the ranking of the prospects in $\mathbf{P}$ is the same regardless of the state-by-state well-being levels of each causally remote individual. Dolores can therefore ignore the well-being levels of these individuals in thinking about her choices. This provides a substantial tractability benefit in decisionmaking.

A betterness ranking of outcomes has a corresponding prospect-ranking rule that satisfies Prospect Separability *only if* the outcome-ranking rule satisfies Separability. The tractability argument for Separability (an axiom regarding the outcome ranking) is this: if the outcome-ranking rule satisfies that axiom, then it can be implemented under uncertainty via prospect-ranking rules that satisfy Prospect Separability, with the attendant tractability benefits.

Table 5 shows how EPP, EAP, and EEDEP fare with respect to these axioms. As the table shows, none of these three approaches satisfy all of the axioms.

|   | Expected Utility Decisionmaking | State Dominance | Ex Ante Pareto | Prospect Separability |
| --- | --- | --- | --- | --- |
| EPP | Yes | Yes | No | Yes |
| EAP | No | No | Yes | Yes |
| EEDEP | Yes | Yes | No^{†} | No |

*Table 5.* ^{†}No, but yes if individuals are identically situated: in each state, all individuals have the same well-being level.

One striking pattern in Table 5 is that none of these three approaches satisfy both State Dominance and Ex Ante Pareto. EPP and EEDEP satisfy State Dominance, at the expense of Ex Ante Pareto; EAP satisfies Ex Ante Pareto, at the expense of State Dominance. This is not a coincidence. As Table 6 illustrates, no prospect-ranking rule for prioritarianism can satisfy both State Dominance and Ex Ante Pareto.

| Prospect | $P$ |   | $P^+$ |   |   |   |   |
| --- | --- | --- | --- | --- | --- | --- | --- |
| State | $s$ | $s^*$ | Exp. wb |   | $s$ | $s^*$ | Exp. wb |
| Carlie | $80$ | $20$ | $50$ |   | $50$ | $50$ | $50$ |
| Dave | $20$ | $80$ | $50$ |   | $50$ | $50$ | $50$ |

(a)

| Prospect | $P'$ |   | $P''$ |   |   |   |   |
| --- | --- | --- | --- | --- | --- | --- | --- |
| State | $s$ | $s^*$ | Exp. wb |   | $s$ | $s^*$ | Exp. wb |
| Carlie | $80$ | $20$ | $50$ |   | $50 - \epsilon$ | $50 - \epsilon$ | $50 - \epsilon$ |
| Dave | $20$ | $80$ | $50$ |   | $50 - \epsilon$ | $50 - \epsilon$ | $50 - \epsilon$ |

(b)

*Table 6.* *Explanation*: In both Table 6a and 6b, the probability of state *s* and of state *s\** is .5.

Table 6a shows the conflict between State Dominance and Ex Ante Pareto Indifference given prioritarian outcome betterness. By Pigou-Dalton, the outcome in which both individuals receive 50 is better than an outcome in which one receives 80 and the other 20. Thus, by State Dominance, prospect $P+$ is better than prospect $P$. But Ex Ante Pareto Indifference requires that the prospects be ranked equally good.

Table 6b shows the conflict between State Dominance and Ex Ante Strong Pareto given prioritarian outcome betterness. For any transformation function, there is some $\varepsilon \gt 0$ such that an outcome in which both individuals receive 50 – *ε* is ranked better than an outcome in which one receives 80 and the other 20. (This is the result of Pigou-Dalton plus Continuity.) Thus, by State Dominance, prospect $P''$ is better than prospect $P'$. But this violates Ex Ante Strong Pareto.

As already noted, a prospect ranking rule that satisfies Expected Utility Decisionmaking automatically satisfies State Dominance. It therefore follows from Table 6 that no prospect-ranking rule for prioritarianism can satisfy both Expected Utility Decisionmaking and Ex Ante Pareto. EPP and EEDEP satisfy the former axiom but not the latter; EAP satisfies the latter but not the former.

In short, in using prioritarianism to provide choice guidance for decisionmakers operating under uncertainty—that is, in constructing a prospect-ranking rule to be paired with the prioritarian outcome-ranking rule—there is a tradeoff between, on the one hand, State Dominance and Expected Utility Decisionmaking; and, on the other hand, Ex Ante Pareto.

### 4.3 Dropping Bernoulli?

The Bernoulli premise—that the ranking of prospects in light of a given person’s well-being conforms to the expected value of that person’s well-being—is widely adopted in the literature on moral choice under uncertainty. See Adler (2019)[^adler-2019][^adler-2019-2]; Broome (1991)[^broome-1991]; Fleurbaey (2010)[^fleurbaey-2010]; Greaves (2017b)[^greaves-2017b]; Harsanyi (1953, 1955, 1977)[^harsanyi-1953][^harsanyi-1955][^harsanyi-1977]; McCarthy (2008)[^mccarthy-2008]; Ord (2015)[^ord-2015]; see additional sources cited in McCarthy (2008, p. 20). But it has also been challenged. See Sen (1976)[^sen-1976], Weymark (1991)[^weymark-1991].

In understanding Bernoulli, it is important to keep in mind that we’re working with well-being numbers that represent well-being levels and differences. Bernoulli says that the numbers play a *third* role: they also expectationally represent well-being comparisons of prospects. For example, assume that, with prospect $P$, Leila gets well-being level $w$ for certain. With prospect $P^*$, she has a 50% chance of getting $w^+$, and a 50% chance of getting $w^-$. Assume that $w^+ \gt w \gt w^-$. Moreover, $w^+ - w = w - w^- = \Delta w$. That is, with $P^*$ Leila gets a 50% chance of doing better than well-being level $w$ by amount $\Delta w$, and a 50% chance of doing worse than well-being level $w$ by the same amount $\Delta w$.

If Bernoulli holds true, the two prospects are equally good for Leila: the well-being she gets from $P$ is $w$, and her expected well-being from $P^*$ equals .$5(w + \Delta w) + .5(w - \Delta w) = w$. But why suppose that the prospects *are* equally good for Leila? Perhaps the prospect ranking in light of Leila’s well-being is such that: a chance of gaining $\Delta w$ counts for less than an equal chance of losing $\Delta w$. If so, $P^*$ is worse than $P$ for Leila, not equally good. Alternatively, perhaps the prospect ranking in light of Leila’s well-being is such that: a chance of gaining $\Delta w$ counts for more than an equal chance of losing $\Delta w$. If so, $P^*$ is better than $P$ for Leila, not equally good.

The debate about Bernoulli implicates difficult and contested issues in well-being measurement. We lack space to engage those issues here. What we *will* point out is how dropping Bernoulli changes the axiomatic comparison of EPP, EAP, and EEDEP. We’ll assume that the ranking of prospects in light of individual $i$’s well-being conforms to the expected value of some function $h(\cdot)$ of individual $i$’s well-being, with $h(\cdot)$ strictly increasing. Bernoulli supposes that $h(\cdot)$ is the identity function or any other linear function; with Bernoulli dropped, $h(\cdot)$ is non-linear, e.g., strictly concave, strictly convex, or some other non-linear form.[^note-5]

Now let us suppose that Bernoulli is dropped *and*, more specifically, that $h(\cdot)$ is the very same function as the prioritarian transformation function $g(\cdot)$. If so, EPP satisfies *all* of the prospect axioms discussed above: Expected Utility Decisionmaking *and* State Dominance *and* Ex Ante Pareto *and* Prospect Separability. EAP has the same axiomatic properties as with Bernoulli.[^note-6] EEDEP continues to satisfy Expected Utility Decisionmaking and State Dominance, but no longer satisfies Ex Ante Pareto even with individuals identically situated.

Note that, if prioritarianism is justified by way of Harsanyi’s Aggregation Theorem plus the rejection of Bernoulli, $h(\cdot)$ and $g(\cdot)$ will indeed be the same.[^note-7]

Alternatively, if Bernoulli is dropped but $h(\cdot)$ is different from $g(\cdot)$, the axiomatic properties of EPP remain as stated in Table 5 (which assumes Bernoulli), as do the axiomatic properties of EAP. EEDEP satisfies Expected Utility Decisionmaking and State Dominance but not Ex Ante Pareto even with individuals identically situated.

In short, dropping Bernoulli strengthens the axiomatic case for EPP as against EEDEP, and strengthens the axiomatic case for EPP as against EAP if $g(\cdot)$ is the same as $h(\cdot)$.

## 5. Utilitarian Challenges to Prioritarianism

### 5.1 Are Utilitarianism and Prioritarianism Distinct?

It has been questioned whether prioritarianism is genuinely distinct from utilitarianism (Broome 1991, ch. 10; 2015)[^broome-1991]. Unlike the utilitarian arguments described below—which concede that prioritarianism and utilitarianism are different, but contend that prioritarianism is flawed—this line of argument denies that prioritarianism is a genuine alternative to utilitarianism in the first place.

The argument runs as follows. For a given set of outcomes $\mathbf{O}$, using well-being measure $w(\cdot)$, utilitarianism assigns each outcome $x$ a score equaling $w_1 (x) + \ldots + w_N (x)$, and ranks outcomes according to these scores. Prioritarianism selects a concave transformation function $g(\cdot)$; assigns each outcome $x$ a score equaling $g(w_1 (x)) + \ldots + g(w_N (x))$; and ranks outcomes according to *these* scores. At this point, we can construct a new well-being measure $w^*(\cdot)$, which assigns well-being numbers to individuals in outcomes as follows: for each individual $i$ and outcome $x$, $w_i^*(x) = g(w_i (x))$. In short, the well-being number for each individual-outcome pair using this new well-being measure, $w^*(\cdot)$, is equal to its concavely transformed well-being number using the old well-being measure, $w(\cdot)$.

But it follows that the “prioritarian” ranking of outcomes according to the score $g(w_1 (x)) + \ldots + g(w_N (x))$ is identical to the utilitarian ranking using the score $w_1^*(x)) + \ldots + w_N^*(x)$. Thus prioritarianism is nothing other than a kind of utilitarianism.

The prioritarian can answer this argument as follows: the original well-being measure $w(\cdot)$ and the new well-being measure $w^*(\cdot)$ are *distinct.* In particular, they disagree in how they make intra- and interpersonal comparisons of well-being differences (Adler 2022a, pp. 81–83)[^adler-2022a][^adler-2022a-2]. A welfarist ranking of outcomes with respect to moral betterness—whether the ranking is utilitarian, prioritarian, sufficientist, generalized-Gini, etc.—builds *upon* an account of well-being and an accompanying well-being measure. The account of well-being and well-being measure should not be “rigged” to match the moral ranking (as is occurring with $w^*(\cdot)$ above), but should be specified independently of the moral ranking. Indeed, it should be independently plausible as a measure of *well-being*. Relative to any such independently specified measure $w(\cdot)$, utilitarianism and prioritarianism *are* different: the moral-betterness ranking produced with the score $w_1 (x) + \ldots + w_N (x)$ need *not* be the same as the ranking produced with the score $g(w_1 (x)) + \ldots + g(w_N (x))$.

### 5.2 Ex Ante Pareto

A powerful utilitarian argument against prioritarianism, with intellectual roots in Harsanyi’s Aggregation Theorem (Harsanyi 1955; Blackorby, Bossert, and Donaldson 2005, ch. 7; Broome 1991; Mongin and Pivato 2016; Weymark 1991)[^blackorby-2005][^broome-1991][^harsanyi-1955][^mongin-2016][^weymark-1991], is that prioritarianism under uncertainty runs afoul of the Ex Ante Pareto axiom (Ex Ante Pareto Indifference and Ex Ante Strong Pareto), while utilitarianism does not. Or, more precisely, among prioritarian theories, factualism, EPP, and EEDEP run afoul of it, whereas EAP does not. (See Broome 1991 for a defense of utilitarianism grounded in the Ex Ante Pareto axiom.)[^broome-1991]

To see the issues here, consider prospect-ranking rules associated with utilitarian outcome betterness. Various possibilities exist, but one is dominant in the literature: For short, let’s call this “simple utilitarianism” (SU). SU: The outcome in each state-of-nature is assigned a “moral utility” number equaling the sum of well-being in that outcome. The prospect is assigned a score equaling its expected outcome utility (the sum of the outcome utilities, each discounted by the state’s probability). In short, SU’s scoring formula is the *expected sum of well-being*.

We’ll assume, for now, that the Bernoulli premise is adopted: the ranking of prospects in light of a given person’s well-being tracks that person’s expected well-being. (See Sections 4.2–4.3.) What happens if Bernoulli is dropped is discussed at the end of this section (six paragraphs below). The analysis until then presupposes Bernoulli.

The axiomatic properties of SU are stated in Table 7. This table (a companion to Table 5) clarifies why SU is the dominant prospect-ranking rule for utilitarianism. It satisfies *all* of the uncertainty axioms mentioned above, while EPP, EAP, and EEDEP each succeed in only satisfying some of them.

|   | Expected Utility Decisionmaking | State Dominance | Ex Ante Pareto | Prospect Separability |
| --- | --- | --- | --- | --- |
| SU | Yes | Yes | Yes | Yes |

*Table 7.*

The reader may be puzzled that SU satisfies both State Dominance and Ex Ante Pareto. Didn’t Table 6 demonstrate that these axioms can’t both be satisfied by a prospect-ranking rule? The answer is that what State Dominance requires *depends* on the outcome-ranking rule. Imagine that there are two states-of-nature and two individuals, Ya and Zeke. In one state, prospect $P$ leads to an outcome in which Ya has well-being 81 and Zeke 25; in the other state, prospect $P$ leads to an outcome in which Ya has well-being 25 and Zeke 81. The outcome of prospect $P^*$ in both states is an outcome in which Ya has well-being 50 and Zeke has well-being 50. State Dominance given the utilitarian outcome-ranking rule requires that $P$ be preferred to $P^* (81 + 25 = 25 + 81 \gt 50 + 50)$. By contrast, consider a prioritarian outcome-ranking rule using the square root transformation function. State Dominance given this *prioritarian* outcome-ranking rule requires that $P^*$ be preferred to $P$ $(\sqrt{81} + \sqrt{25} \lt \sqrt{50} + \sqrt{50})$.

In short, a prospect-ranking rule *for prioritarian outcome betterness* can’t satisfy both State Dominance and Ex Ante Pareto, or both Expected Utility Decisionmaking and Ex Ante Pareto, as shown by Table 6. By contrast, a prospect-ranking rule *for utilitarian outcome betterness can* satisfy Expected Utility Decisionmaking *and* State Dominance *and* Ex Ante Pareto. This fact in turn fuels the utilitarian critique of prioritarianism. For those who are generally attracted to expected utility theory as a normative framework for decision, Expected Utility Decisionmaking (which, again, applies that framework to the specific case of moral choice-guidance) will seem quite plausible. Even if one rejects expected utility theory, State Dominance is surely compelling. But Ex Ante Pareto also has strong normative force. Prioritarian outcome-betterness forces a tradeoff between these uncertainty axioms; utilitarian outcome-betterness does not.

How prioritarianism responds to this critique depends upon whether factualism is adopted. In their ranking of choices, factualist prioritarians reject both Expected Utility Decisionmaking and Ex Ante Pareto (but not State Dominance). As regards Ex Ante Pareto, its force derives from the fact that it seems to respect the prudential viewpoints of individuals. Here, betterness from a given prudential viewpoint is measured in terms of the individual’s expected well-being. However, factualists argue that just as what ultimately matters in the case of moral value is the moral value that is in fact realized, what ultimately matters in the case of prudential value is the prudential value that is in fact realized. Therefore, Ex Ante Pareto misconstrues the prudential viewpoints of individuals.

If factualism is not adopted, the prioritarian can respond as follows. First, the tradeoff between Expected Utility Decisionmaking/State Dominance and Ex Ante Pareto is not limited to prioritarian outcome rankings. Harsanyi’s Aggregation Theorem shows that *every non-utilitarian outcome ranking* faces a tradeoff between Expected Utility Decisionmaking and Ex Ante Pareto; no such outcome ranking has a prospect ranking that satisfies both. Further, it can be shown (indeed, can be seen from Table 6) that *every Pigou-Dalton-respecting outcome ranking* faces a tradeoff between State Dominance and Ex Ante Pareto; no such outcome ranking has a prospect ranking that satisfies both. (See Adler 2019 for more detail.)[^adler-2019][^adler-2019-2] In a nutshell, the tradeoffs here are the inevitable result of injecting a concern for equity into outcome betterness (in the form of Pigou-Dalton). Utilitarianism avoids the tradeoffs, but at the cost of violating *this* very plausible axiom at the outcome level.

What happens, now, if Bernoulli is dropped? The ranking of prospects in light of individual $i$’s well-being conforms to the expected value of some function $h(\cdot)$ of individual $i$’s well-being, with $h(\cdot)$ strictly increasing but non-linear. *If* $h(\cdot)$ is identical to the prioritarian transformation function $g(\cdot)$, the axiomatic comparison of SU relative to EPP changes dramatically. SU still satisfies Expected Utility Decisionmaking, State Dominance, and Prospect Separability, but now violates Ex Ante Pareto; EPP satisfies all four of the prospect axioms, including Ex Ante Pareto. If $h(\cdot)$ is different from $g(\cdot)$, EPP fares the same way as SU vis a vis those prospect axioms, i.e., they both satisfy Expected Utility Decisionmaking, State Dominance, and Prospect Separability, but not Ex Ante Pareto.

In short, dropping Bernoulli neutralizes the case for utilitarianism based on Ex Ante Pareto.

### 5.3 Veil of Ignorance

Harsanyi famously made two distinct arguments in favor of utilitarianism. One is the Aggregation Theorem, mentioned above. The second is his veil-of-ignorance argument (Harsanyi 1953, 1955, 1977; Weymark 1991)[^harsanyi-1953][^harsanyi-1955][^harsanyi-1977][^weymark-1991]. Let each outcome be conceptualized as an equiprobability lottery over the well-being levels of the $N$ individuals in the outcome. If the evaluator complies with expected utility theory and if the Bernoulli premise holds true, then the “veil of ignorance” value assigned to a given outcome $x$—the value assigned to $x$ conceptualized as this equiprobability lottery—is just $(1/N) w_1 (x) +\ldots (1/N) w_i (x) + \ldots + (1/N) w_N (x)$. But the ranking of outcomes according to these veil-of-ignorance values is, obviously, the same as the utilitarian ranking.

One response to Harsanyi’s defense of utilitarianism, pressed by Buchak (2017)[^buchak-2017], is to argue that outcomes conceptualized as equiprobability lotteries should be valued using risk-weighed expected utility theory (REU), not expected utility theory. See Section 3.1. However this response does not offer a defense of prioritarianism (assuming Buchak is correct that REU plus the veil of ignorance leads to generalized-Gini betterness).

A second response is to agree with Harsansyi in conceptualizing outcomes as equiprobability lotteries over well-being levels, and to agree with him in adopting expected utility theory, but to reject Bernoulli. This will yield prioritarianism *if* the $h(\cdot)$ function is not merely strictly increasing but strictly concave. With Bernoulli dropped, the veil-of-ignorance value assigned to a given outcome $x$ becomes: $(1/N) h(w_1 (x)) + \ldots + (1/N) h(w_N (x))$. Clearly, this is the same as a prioritarian ranking if, but only if, $h(\cdot)$ is both strictly increasing and strictly concave.

The third and most emphatic response, which is consistent with both expected utility theory and Bernoulli, is simply to deny that the veil of ignorance is the appropriate mode of justification for outcome betterness. (Moreno-Ternero and Roemer 2008)[^moreno-ternero-2008]. Note that arguments (1), (2), (3), and (4) in Section 3.1 each defend a non-utilitarian betterness ranking by appealing to some mode of justification other than the veil of ignorance.

### 5.4 Difference Comparison

Consider the following transfer axiom (“Difference Comparison”): In any two-person case such that one person is better off in $x$ than $y$ by $\Delta w$, and the other in $y$ than $x$ by $\Delta w^*$, with everyone else unaffected, $x$ is at least as good as $y$ if and only if $\Delta w \ge$ $\Delta w^*$. This is a competing transfer axiom to Pigou-Dalton. It can be shown that a welfarist outcome ranking that satisfies Difference Comparison must be utilitarian. (Blackorby, Bossert and Donaldson 2002, p. 568)[^blackorby-2002]. For those who find this axiom more intuitive than Pigou-Dalton, it provides a direct argument for utilitarianism.

## 6. Egalitarian Challenges to Prioritarianism

### 6.1 Comparative Fairness and Levelling Down

Larry Temkin has posed a number of challenges to prioritarianism. Some of these challenges involve a rejection of welfarism, but for present purposes, the welfarist framework is taken for granted and so the focus is on challenges that can be raised within this framework. Temkin provides an account of egalitarianism that is based on individual claims (or, in Temkin’s terminology, “complaints”). This is a claims-within-outcomes account that differs from the claims-across-outcomes account presented above in Section 3.1, in that it construes claims as being internal to individual outcomes. Outcomes are to be ranked in terms of how individuals fare vis-à-vis each other in each of them, more specifically as regards their claims to an equal share of well-being (Temkin 1993, ch. 2)[^temkin-1993]. Claims thus construed express a concern with what Temkin calls “comparative fairness” (Temkin 2003, p. 62)[^temkin-2003]. Unlike prioritarianism, Temkin’s egalitarianism is comparative in the sense that it allows individual claims to depend on the well-being of others. This also means that Temkin rejects Separability.

Nevertheless, Temkin does not consider the rejection of Separability objectionable. Consider his two cases of space travelers who are in a position to divert a mineral-rich asteroid to a planet where the inhabitants will benefit from the minerals (Temkin 2003, pp. 69–70)[^temkin-2003]. In the first case, these inhabitants are much better off than people on other planets. In the second case, they are much worse off than people on other planets. People on the receiving planet are equally well off in the two cases and the increase in well-being due to the asteroid is also the same. Since prioritarianism satisfies Separability, it implies that the well-being of people on other planets is irrelevant, as these will not be affected, when determining the moral value of diverting the asteroid. However, Temkin argues that this is implausible and that, indeed, the space travelers should be willing to make a larger personal sacrifice to divert the asteroid insofar as the inhabitants on the receiving planet are worse off than everyone else in the universe.

One way for prioritarians to respond is to agree that there is a difference between the two cases but insist that it does not pertain to a difference in the moral value of benefiting people on the receiving planet (who are equally well off and benefit equally in the two cases). Rather, prioritarians may believe there is reason to regret that, in the first case, it is not possible to divert the asteroid towards another planet where the benefits will accrue to people who are at lower absolute levels of well-being.

Temkin also challenges a particular reason prioritarians sometimes invoke for preferring prioritarianism to egalitarianism, namely the Levelling Down Objection (see Section 2). Temkin (1993, ch. 9) argues that this objection relies for its plausibility on a person-affecting account of moral value. In one version, which endorses what might be called the “narrow person-affecting principle”, it is claimed that an outcome, $x$, cannot be in any respect better (or worse) than another outcome, $y$, unless there is someone for whom $x$ is better (or worse) than $y$. Thus, the reason we may be tempted to think that a levelled down outcome cannot be in any respect better is that it is better for no one.

However, Temkin thinks we should reject the narrow person-affecting principle. He offers several reasons for rejecting that principle, including one that is consistent with welfarism: the non-identity problem. Suppose that, for whatever reason, a woman may now conceive a child whose life will be fairly bad (indeed, only barely worth living). If she waits a couple of months, she will instead conceive another child, who will have a happy life. No one else, including the woman, will have their well-being impacted by her choice. According to the narrow person-affecting principle, we cannot claim that the outcome in which she has the unhappy child is worse than the outcome in which she has the happy child, because the former outcome is not worse for the unhappy child (who has a positive, although low level of well-being), nor is it worse for the happy child (who then does not exist). But this implication of the narrow person-affecting principle seems wrong.

Here are two responses prioritarians can make to Temkin’s challenge (Holtug 2010, pp. 181–200)[^holtug-2010]. First, they can deny that the Levelling Down Objection is based on a person-affecting account of moral value. Even if such an account is rejected, levelling-down cases reveal that our distributive concerns are not well captured by egalitarianism—or so it may be argued. For example, are those concerns well captured by the supposition that outcome $x$ in which well-being levels are (1, 1, 5, 5) is in one respect better than outcome $y$ in which the levels are (3, 7, 10, 15)? Counting $x$ as better in one respect seems to ignore the plight of the worse off, surely the core of distributive justice, who are much worse off in $x$ than $y$.

Second, prioritarians may endorse a person-affecting account of moral value but argue that it should be expressed in the form of a wide rather than a narrow person-affecting principle (for the distinction between wide and narrow person-affecting principles, see Parfit 1987, pp. 393–401)[^parfit-1987]. According to a particular wide person–affecting principle, an outcome, $x$, cannot be in any respect better (or worse) than another outcome, $y$, if, were $x$ to obtain, there would be no one for whom $x$ was better (or worse) than $y$ and, were $y$ to obtain, there would be no one for whom $y$ was worse (or better) than $x$. On the assumption that it can be better (or worse) for an individual to exist than never to exist, this principle implies that in the non-identity problem, it may well be worse for the woman to have the unhappy child because, were she to have the happy child instead, that would be better for *this* child (for defenses of this assumption, see Arrhenius and Rabinowicz 2015; Bradley 2013; Holtug 2015a; Johansson 2010; Persson 1997, and for criticism, Broome 1993; Bykvist 2007; McMahan 2013; Parfit 1987)[^arrhenius-2015][^bradley-2013][^broome-1993][^bykvist-2007][^holtug-2015a][^johansson-2010][^mcmahan-2013][^parfit-1987][^persson-1997]. Like the narrow principle, the wide principle implies that it cannot be in any respect better to level down.

Note also that the claims-across-outcomes framework (see Section 3.1) aims to make precise a person-affecting account of moral value.

### 6.2 Prudential Justification and Competing Claims

A further egalitarian challenge to prioritarianism is due to Michael Otsuka and Alex Voorhoeve (Otsuka and Voorhoeve 2009, 2018; Otsuka 2015)[^otsuka-2015][^otsuka-2009][^otsuka-2018]. More specifically, they raise two objections, namely the prudential justification objection and the competing claims objection. Consider first the prudential justification objection. Suppose Anandi will (equiprobably) develop a slight or a severe impairment and she needs to be treated before we know which. The treatment for the slight impairment is a bit more efficient as regards Anandi’s well-being, where her well-being levels are represented in Table 8.

|   | Anandi develops severe impairment | Anandi develops slight impairment |
| --- | --- | --- |
| A. Treatment for severe impairment | 4 | 7 |
| B. Treatment for slight impairment | 2 | 10 |

*Table 8.*

Assume again square root as the prioritarian transformation function. Then, according to EPP, we should ascribe the following values to the two possible treatments:

$$\begin{align} \tag*{A.} (0.5 \times \sqrt{4}) + (0.5 \times \sqrt{7}) &= 2.323 \\ \tag*{B.} (0.5 \times \sqrt{2}) + (0.5 \times \sqrt{10}) &= 2.288 \end{align}$$

Therefore, it is better to treat for the severe than for the slight impairment. However, according to Otsuka and Voorhoeve, this ignores that there is a prudential justification for treating for the slight impairment, namely that this would maximize Anandi’s expected well-being (see also McCarthy 2008, pp. 19–22; Ord 2015)[^mccarthy-2008][^ord-2015]. In fact, the claim that Anandi should be treated for the severe impairment violates Ex Ante Pareto (assuming Bernoulli, see Section 4.2; our discussion in this section assumes Bernoulli). Otsuka and Voorhoeve suggest that prioritarianism applies to single-person cases a principle that is appropriate only for multi-person cases.

Next, consider the competing claims objection. Compare the case of Anandi to the case of Bernard and Chimwala. Unlike the former case, the latter does not involve uncertainty. Rather, Bernard will develop the severe impairment and Chimwala the slight impairment. Furthermore, a treatment for the severe impairment will raise Bernard’s well-being from 2 to 4, and a treatment for the slight impairment will raise Chimwala’s well-being from 7 to 10 (thus, their well-being levels match those of Anandi regarding the two different impairments she may develop). The prioritarian outcome ranking implies that it is better to treat Bernard for his severe impairment than to treat Chimwala for her slight impairment. Indeed, EPP implies ‘symmetrical balancing’ in these two cases in the sense that it is better to treat Bernard than to treat Chimwala if and only if it is better to treat Anandi for the severe than for the slight impairment. However, this means that prioritarians do not assign any independent significance to the fact that Bernard and Chimwala have *competing claims*. On this basis, Otsuka and Voorhoeve argue that prioritarianism violates the separateness of persons.

Egalitarianism, on the other hand, is not vulnerable to either the prudential justification or the competing claims objection. Since it applies only to relations between individuals, it is silent on the ranking of prospects in single-person cases, such as the case of Anandi. Thus, it allows that single-person cases should be settled on the basis of the relevant person’s expected well-being. This also means that in the case of Bernard and Chimwala, egalitarianism implies that a moral concern enters the picture that is not present in the case of Anandi, which is due to the fact that Bernard is *worse off than* Chimwala and therefore has a stronger claim to being treated for his impairment.

The prudential justification objection applies only to EPP, not to EAP, EEDEP, or factualist prioritarianism. Since EAP applies the prioritarian transformation function to individual expected well-being and renders moral value an increasing function of such well-being, it implies that in single-person cases the moral ranking will always coincide with the prudential ranking that is based on the person’s expected well-being. EEDEP also coincides with the prudential ranking in single-person cases. As regards factualist prioritarianism, it implies that Anandi should be treated for the impairment she will in fact develop, which is also what is implied by factualist prudence. More generally, there is no gap in single-person cases between factualist prioritarianism and factualist prudence (which, according to factualists, is the form of prudence that ultimately matters). (For further discussion, including of whether and if so how the prudential justification objection applies to a factualist prioritarian decision-procedure, see Holtug 2019.)[^holtug-2019]

Various prioritarian responses to the prudential justification objection to EPP have been proposed (for discussion, see Bognar 2012; Crisp 2011; Holtug 2019; Hyams 2015; O’Neill 2012; Ord 2015; Parfit 2012; Porter 2012; Rendall 2013; Segall 2015; Williams 2012)[^bognar-2012][^crisp-2011][^holtug-2019][^hyams-2015][^o’neill-2012][^ord-2015][^parfit-2012][^porter-2012][^rendall-2013][^segall-2015][^williams-2012]. Here, we mention four. First, it has been argued that EPP should be seen as a conflict resolution principle, which applies only to interpersonal conflicts in well-being, and so not to single-person cases (Adler and Holtug 2019, p. 21; Williams 2012, p. 324)[^adler-2019][^adler-2019-2][^holtug-2019][^williams-2012]. Second, Parfit (2012)[^parfit-2012] proposed a hybrid principle, which includes both EPP and EAP, in response to the challenges posed by Otsuka and Voorhoeve. Third, it has been proposed that the implications of EPP in single-person cases simply do not serve to undermine this principle. Otsuka and Voorhoeve suggest that the prioritarian transformation function is inappropriate in single-person cases, but prioritarians may argue otherwise. To illustrate, consider a particular child, Friedrich, who might have either of two possible futures. In one possible outcome, $x$, Friedrich will be quite badly off, but nevertheless enjoys a particular benefit, $B$ (which improves his well-being by, say, 5 units of well-being). In another possible outcome, $y$, Friedrich will be quite well off and also enjoys this particular benefit, $B$ (again, increasing his well-being by 5 units). Prioritarians may suggest that it is both intuitive and quite appropriate to apply the prioritarian transformation function to this single-person case and on this basis claim that $B$ contributes more moral value in $x$ than in $y$, because in the outcome in which he is worse off, it is morally more urgent to benefit Friedrich (Holtug 2021, pp. 396–399)[^holtug-2021]. Finally, to the extent reservations about the claim that Anandi should be treated for the severe impairment are due to Ex Ante Pareto, it is worth pointing out that ex post egalitarianism likewise violates this principle (although not in single-person cases). And so Ex Ante Pareto does not, as such, provide a reason to favor egalitarianism over prioritarianism.

Regarding the competing claims objection, there are different ways in which prioritarians may respond. If they consider prioritarianism a conflict resolution principle, they can argue that there is a particular moral concern that applies only to the case of Bernard and Chimwala, not to the case of Anandi, and it involves weighing up their competing claims. In other words, with this revision, the prioritarian only applies the prioritarian transformation function to multi-person cases. Alternatively, or in addition, prioritarians may invoke the claims-across-outcomes framework outlined above (Section 3.1). They can then argue that Bernard has a stronger claim to being treated than Chimwala because, although Chimwala would benefit more, the benefit to Bernard falls at a lower level of well-being. On this line of reasoning, prioritarianism will not be insensitive to competing claims—rather, it will be built upon them. Of course, the prioritarian account of competing claims is different from an egalitarian account, because the prioritarian account satisfies Separability. This means that the size of each individual’s claim is independent of the well-being of others (where these independent claims are then balanced against each other to arrive at the overall prioritarian ranking). As we have seen above, prioritarians tend to consider Separability an independently attractive condition for a distributive principle to satisfy.

## 7. Sufficientist Challenges to Prioritarianism

Sufficientism was expressed as a betterness ranking in Section 1.1. This statement of sufficientism, which will be our focus here, is based upon Crisp (2003)[^crisp-2003]. See Shields (2020)[^shields-2020]; Bossert, Cato, and Kamaga (2022), for a survey of alternative versions.

Sufficientism differs from prioritarianism in two respects. Both arise from its use of a well-being threshold. First, sufficientism accords absolute priority to those below the threshold, over those above. PLT has the very same feature. Section 3.2.2 described and criticized this feature of PLT; the same criticisms apply to sufficientism.

Second, above the threshold, equal increases in well-being have equal moral value (and so above the threshold, sufficientism coincides with utilitarianism). Sufficientists argue that when a certain level of well-being has been reached, priority gives out. For example, assuming for simplicity that their well-being matches their wealth, we should not care about inequalities between the rich and the super-rich (Crisp 2003; Frankfurt 1987)[^crisp-2003][^frankfurt-1987]. Above the threshold, as long as the sum of well-being remains constant, we should be indifferent to how it is distributed.

Axiomatically, this second feature of sufficientism corresponds to a violation of the Pigou-Dalton axiom with respect to above-threshold transfers. Consider a sufficientist betterness ranking with $w^\textit{Thresh}$ as its well-being threshold, as compared to a PLT ranking with the very same threshold and to prioritarianism. Assume that in $x$ Fei and Gerry are both better off than $w^\textit{Thresh}$, with Fei better off than Gerry. In $y$ Fei’s well-being has decreased by $\Delta w$, Gerry’s has increased by $\Delta w$, the gap between them has decreased (thus both remain above $w^\textit{Thresh}$), and no one else is affected. Then Pigou-Dalton requires that $y$ be ranked better than $x$; PLT and prioritarianism will do so, while sufficientism considers the two outcomes to be equally good.

There are different ways in which the sufficientist can motivate the rejection of Pigou-Dalton above the sufficiency threshold. Crisp (2003, p. 758) makes a proposal that simultaneously fixes the threshold *and* provides an explanation of why Pigou-Dalton no longer applies once it has been met. Thus, according to Crisp, $w^\textit{Thresh}$ is the level at which compassion sets out. Along such lines, we feel compassion for the poor, giving them priority over the rich, but we do not feel compassion for the rich and so do not feel inclined to give them priority over the super-rich.

Prioritarians can respond to this argument in either of two ways. They can argue that compassion is not a reliable guide to distributive justice. Or they can argue that, even on the assumption that compassion is a reliable guide, there is no level at which compassion gives out, motivating a departure from Pigou-Dalton. Let us assume that the sufficientist will want to set $w^\textit{Thresh}$ at a relatively high level, such as to render plausible the claim that compassion gives out above that level. And assume, for simplicity, that well-being is directly proportional to life-length and that, at any given point in time at which they are alive, everyone will have the same level of well-being. Now compare two outcomes, $x$ and $y$. In $x$, half the population lives three times as long as the other half of the population (say, respectively, 300 years and 100 years) and the first half of the population obtains a well-being level of $3w^\textit{Thresh}$ whereas the second half obtains only a level of $w^\textit{Thresh}$. In $y$, life-length and therefore well-being is distributed equally between the groups, such that everyone lives 200 years and obtains a well-being level of $2w^\textit{Thresh}$. Thus, we can move from $x$ to $y$ through a series of Pigou-Dalton transfers. Prioritarians can now argue that, intuitively, $y$ is better than $x$ (Holtug 2010, pp. 233–235)[^holtug-2010]. And that, indeed, everything else being equal, we would have reason to choose $y$ over $x$, if for example we were able to distribute some life-prolonging drug equally $(y)$ rather than unequally $(x)$. This may suggest that compassion does not give out and that there is no threshold above which Pigou-Dalton ceases to apply. (For further critical discussion of sufficientism, see for example Casal 2007.)[^casal-2007]

## 8. Variable Population

Outcomes can vary regarding both the identities and the number of individuals that exist in them. Since the most complex and troubling problems in population ethics concern different-number comparisons, these will also be in focus here. Prioritarians might claim that prioritarianism applies only to same-number comparisons. Along such lines, Parfit (2004, p. 257) at one point suggested “quarantining” different-number comparisons, because of the sort of problems that arise for distributive principles when applied to such comparisons. Specifically with respect to prioritarianism he said that it “cannot be applied to cases in which, in the different possible outcomes, different people would exist. When we consider these cases, we need other principles” (Parfit 2012, p. 440; for criticism, see Otsuka 2022; Segall 2022)[^otsuka-2022][^parfit-2012][^segall-2022]. In this Section, however, the focus will be on the implications of prioritarianism insofar as it is applied to different-number comparisons.

Various distributive principles, including total utilitarianism, imply what Parfit dubbed the Repugnant Conclusion: “For any possible population of at least ten billion people, all with a very high quality of life, there must be some much larger imaginable population whose existence, if other things are equal, would be better, even though its members have lives that are barely worth living” (Parfit 1987, p. 388)[^parfit-1987]. Call the outcome with the former (happier) population $x$ and the latter (more populous) outcome $y$. Total utilitarianism implies the Repugnant Conclusion because: if there are enough individuals with a positive but very low level of well-being in $y$, its total well-being will exceed that of $x$. Prioritarianism likewise implies the Repugnant Conclusion. In fact, it even implies the Super-repugnant Conclusion, according to which $y$ can be better, even if it holds a smaller total of well-being than $x$ (Holtug 2010, p. 254)[^holtug-2010]. This is because the well-being units in $y$ mostly fall at lower levels of well-being than the units in $x$ and so they have more weight, given the prioritarian transformation function.

Both total utilitarianism and prioritarianism also imply the Negative Repugnant Conclusion, according to which an outcome, $x^*$, in which people have lives that are barely worth not living is worse than an outcome, $y^*$, in which 10 billion people have extremely miserable lives (very much worth not living), if the former outcome is sufficiently populous. But whereas total utilitarianism has this implication if $x^*$ holds a higher total of negative well-being than $y^*$, prioritarianism implies that it takes more people in $x^*$ to make this outcome worse. This is because, in $y^*$, the units of well-being will in general fall at lower (more negative) levels than in $x^*$. Therefore, relative to total utilitarianism, prioritarianism may seem less plausible regarding the Repugnant Conclusion, but more plausible regarding the Negative Repugnant Conclusion. (For a challenge to applying prioritarianism to both positive and negative levels of well-being in variable populations, see Brown 2007.)[^brown-2007]

Another aspect of prioritarianism, which some find attractive, is that it implies a weaker version of the Asymmetry. According to the Asymmetry, adding people with negative well-being to an outcome detracts from its value, whereas adding people with positive well-being does not increase its value (Narveson 1967, pp. 69–71)[^narveson-1967]. An implication of this view, which many find compelling, is that concerns about their well-being do not ground an obligation to have children (Heyd 1992; Narveson 1967; Roberts 1998; Wolf 1997)[^heyd-1992][^narveson-1967][^roberts-1998][^wolf-1997]. Nevertheless, some have argued that the Asymmetry is too strong. For example, it seems to suggest that, everything else being equal, it would be better if people ceased to have children, because on the assumption that a few of these children will have lives with net negative well-being, this negative well-being cannot be counterbalanced by the (presumably) many more future children who will have lives with net positive well-being (Sikora 1978, pp. 136–140)[^sikora-1978]. In a weaker version, which does not have this counterintuitive implication, but does prioritize the non-existence of miserable children over the existence of happy ones, the Asymmetry claims that for a given level of well-being, $w$, adding an individual with level –$w$ detracts more from the value of an outcome than adding an individual with level $w$ increases such value (Holtug 2022, pp. 49–50)[^holtug-2022].

There are various ways in which population ethicists have tried to avoid repugnant conclusions and other difficulties regarding variable populations. See generally Blackorby, Bossert and Donaldson (2005) and Greaves (2017a)[^greaves-2017a]. This is not the place to assess these proposals (and serious objections have been raised against all of them), but merely to point out how many of them are also available to prioritarians (2022). Modal proposals involve delimiting the class of individuals whose well-being counts when ranking outcomes. Thus, it has been suggested that this class includes only actual people, that is, people who exist in the actual history of the world (see Feinberg 1980, p. 180; Steinbock 1992, p. 72)[^feinberg-1980][^steinbock-1992], or only necessary people, that is, people who exist in all the outcomes compared (see Heyd 1992)[^heyd-1992]. Prioritarians can delimit the scope of their principle in this manner if they so desire.

Another proposal involves tinkering with the functions on which distributive principles rely. For example, just as total utilitarianism could be replaced with average utilitarianism, prioritarianism (as it has been defined above) could be replaced with average prioritarianism (where the outcome ranking is based on the sum of concavely transformed individual well-being, divided by the number of individuals in the outcome). Average prioritarianism implies that, as regards the Repugnant Conclusion, $x$ is better than $y$. Similarly, there is a prioritarian version of critical level theory. Critical level theories claim that there is a certain level of well-being, $l$, which is above zero, such that only lives above $l$ positively contribute to the value of an outcome (Blackorby, Bossert, and Donaldson 1997)[^blackorby-1997]. According to a prioritarian critical level theory, the outcome ordering is based on the following function (Adler 2009, p. 1510)[^adler-2009]: $m^\textit{prior-crit}(x) = [g(w_1 (x)) - g(l)] + \ldots + [g(w_N (x)) - g(l)]$. Applied to the Repugnant Conclusion, this principle implies that individuals with lives only barely worth living do not contribute positively to the value of an outcome, and so irrespective of the number of individuals in $y$, it cannot be better than $x$.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

### Work Cited

### Other Work

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=prioritarianism). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/prioritarianism/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=prioritarianism&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/prioritarianism/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

[Please contact the authors with suggestions.]

## Related Entries

common good | consequentialism | consequentialism: rule | economics [normative] and economic justice | egalitarianism | equality | justice | luck: justice and bad luck | moral decision-making under uncertainty | rational choice, normative: expected utility | rational choice, normative: rivals to expected utility | redistribution | repugnant conclusion, the

## Notes（原文脚注）

[^note-1]: Defenses of prioritarianism include Adler (2012, 2019, 2022a)[^adler-2012][^adler-2019][^adler-2022a][^adler-2019-2][^adler-2022a-2]; Adler and Holtug (2019)[^holtug-2019]; Arneson (2000, 2007, 2022)[^arneson-2000][^arneson-2007][^arneson-2022]; Holtug (2010)[^holtug-2010]; Hooker (2000)[^hooker-2000]; Hyams (2015)[^hyams-2015]; McKerlie (2007)[^mckerlie-2007]; Nebel (2017)[^nebel-2017]; O’Neill (2012)[^o’neill-2012]; Parfit (2000, 2012)[^parfit-2000][^parfit-2012]; Porter (2011, 2012)[^porter-2011][^porter-2012]; Segall (2015)[^segall-2015]; Weirich (1983)[^weirich-1983]; and Williams (2012)[^williams-2012]. See also Adler and Norheim (2022a) for a survey of prioritarianism’s implications for public policy.

[^note-2]: Space constraints preclude addressing a number of topics: picking a specific transformation function within the class of such functions (Adler 2022a)[^adler-2022a][^adler-2022a-2]; shifting from lifetime to time-slice well-being (Adler 2012; Andrić and Herlitz 2022; Holtug 2010; McKerlie 1997, 2001a, 2001b, 2007, 2013)[^adler-2012][^andrić-2022][^holtug-2010][^mckerlie-1997][^mckerlie-2001a][^mckerlie-2001b][^mckerlie-2007][^mckerlie-2013]; adjusting well-being to take account of individual desert or opportunity (Adler 2018; Arneson 2007, 2022; Brunori, Ferreira, and Peragine 2022)[^adler-2018][^arneson-2007][^arneson-2022][^brunori-2022]; shifting to a “local” prioritarianism that regulates distribution only within societies, rather than globally (Nagel 1991; cf. Holtug 2009)[^holtug-2009][^nagel-1991]; specifying prioritarianism as a deontic rather than axiological view (Nebel 2017; Williams 2012)[^nebel-2017][^williams-2012]; and, as mentioned, including non-human animals within the population of concern.

[^note-3]: To be precise: (1) $w_i (x) \ge w_j (y)$ if and only if $i$ in $x$ is at least as well off as $j$ in $y$, with $i$ and $j$ either the same individual (intrapersonal case) or distinct individuals (interpersonal case). (2) $w_i (x) - w_j (y) \ge w_k (z) - w_l (zz)$ if and only if the difference between $i$’s well-being in $x$ and $j$’s well-being in $y$ is at least as large as the difference between $k$’s well-being in $z$ and $l$’s well-being in $zz$, with either $i = j = k = l$ (intrapersonal case) or not $i = j = k = l$ (interpersonal case).

[^note-4]: Here are formal definitions. To say that $g(\cdot)$ is strictly increasing means: if $w$* $\gt w$, then $g(w^*) \gt g(w)$. To say that $g(\cdot)$ is strictly concave means: for all *α*, $0 \lt \alpha \lt 1$, and for all $w, w^*$ with $w \ne w$*, $\alpha g(w) + (1-\alpha)g(w^*) \lt g(\alpha w + (1-\alpha)w^*)$. Strict concavity, thus defined, is equivalent to requiring that $g(\cdot)$ have diminishing slope: if $w \lt w^* \lt w^{**}$,

$$ \frac{g(w^{**}) - g(w^*)}{w^{**} - w^*} \lt \frac{g(w^*) - g(w)}{w^* - w}.$$

[^note-5]: If $P$ leads for sure to a higher well-being level for individual $i$ than $P^*, P$ is surely a better prospect in light of $i$’s well-being. Requiring $h(\cdot)$ to be strictly increasing ensures that the expected value of $h(w_i)$ is greater for $P$ than $P^*$ in this kind of case.

Having $h(\cdot)$ vary among individuals creates difficulties, see Adler (2019, pp. 271–72), and we will therefore assume that $h(\cdot)$ is a single function.

[^note-6]: With Bernoulli dropped, the definition of EAP should presumably change to: the sum of $g(\cdot)$ applied to individuals’ expected $h(\cdot)$-transformed well-being. (The idea behind EAP is to use a measure of the well-being value of each individual’s prospect as the input into $g(\cdot)$.) The text accompanying this footnote describes the axiomatic properties of EAP thus reformulated.

[^note-7]: We lack space to discuss Harsanyi’s Aggregation Theorem in detail here. (On the theorem, see generally Harsanyi 1955; Blackorby, Bossert, and Donaldson 2005, ch. 7; Broome 1991; Mongin and Pivato 2016; Weymark 1991)[^blackorby-2005][^broome-1991][^harsanyi-1955][^mongin-2016][^weymark-1991]. Roughly, it appeals both to the Ex Ante Pareto axiom and to expected utility theory as applied to the moral ranking of lotteries over outcomes, or of prospects, to characterize the moral-betterness ranking of outcomes. Harsanyi supposed the Aggregation Theorem to provide a defense of utilitarianism. That itself is disputed. What *is* true is that, with additional premises, including Bernoulli, the Aggregation Theorem supports utilitarianism. See Adler (2019, pp. 282–83) for a simple explanation, using outcome lotteries rather than prospects; the premises here are Expected Utility Decisionmaking; the existence of a measure of well-being $w(\cdot)$ that represents intra- and interpersonal comparisons of well-being levels and differences; Bernoulli; Ex Ante Pareto; and Anonymity. If these premises are retained except for Bernoulli, now supposing instead that the ranking of prospects in light of individual $i$’s well-being conforms to the expected value of some function $h(\cdot)$, with $h(\cdot)$ strictly increasing and strictly concave, it follows that: the betterness ranking is prioritarian with $h(\cdot)$ as the transformation function.

[^adler-2009]: Adler, Matthew D., 2009, “Future Generations: A Prioritarian View”, *George Washington Law Review*, 77: 1478–1520.

[^adler-2012]: –––, 2012, *Well-Being and Fair Distribution: Beyond Cost-Benefit Analysis*, New York: Oxford University Press.

[^adler-2018]: –––, 2018, “Prioritarianism: Room for Desert?”, *Utilitas*, 30(2): 172–197.

[^adler-2019]: –––, 2019, *Measuring Social Welfare: An Introduction*, New York: Oxford University Press.

[^adler-2022a]: –––, 2022a, “Theory of Prioritarianism,” in Matthew D. Adler and Ole F. Norheim (eds.), *Prioritarianism in Practice*, Cambridge: Cambridge University Press, pp. 37–127.

[^adler-2022b]: –––, 2022b, “Claims Across Outcomes and Population Ethics,” in Gustaf Arrhenius, Krister Bykvist, Tim Campbell, and Elizabeth Finneron-Burns (eds.), *The Oxford Handbook of Population Ethics*, New York: Oxford University Press, pp. 320–49.

[^adler-2025]: –––, 2025, “Narrowly Person-Affecting Axiology: A Reconsideration,” *Economics and Philosophy*, 41(1): 119–160.

[^adler-2019-2]: Adler, Matthew D., and Nils Holtug, 2019, “Prioritarianism: A Response to Critics”, *Politics, Philosophy and Economics*, 18(2): 101–144.

[^adler-2022a-2]: Adler, Matthew D., and Ole F. Norheim (eds.), 2022a, *Prioritarianism in Practice*, Cambridge: Cambridge University Press.

[^adler-2022b-2]: –––, 2022b, “Introduction,” in Matthew D. and Ole F. Norheim (eds.), *Prioritarianism in Practice*, Cambridge: Cambridge University Press, pp. 1–36.

[^andrić-2022]: Andrić, Vuko, and Anders Herlitz, 2022, “Prioritarianism, Timeslices, and Prudential Value”, *Australasian Journal of Philosophy*, 100(3): 595–604.

[^arneson-2000]: Arneson, Richard J., 2000, “Luck Egalitarianism and Prioritarianism”, *Ethics*, 110(2): 338–349.

[^arneson-2007]: –––, 2007, “Desert and Equality”, in Nils Holtug and Kasper Lippert-Rasmussen (eds.), *Egalitarianism. New Essays on the Nature and Value of Equality*, Oxford: Clarendon Press, pp. 262–293.

[^arneson-2022]: –––, 2022, *Prioritarianism*, Cambridge: Cambridge University Press.

[^arrhenius-2015]: Arrhenius, Gustaf and Wlodek Rabinowicz, 2015, “The Value of Existence”, in Iwao Hirose and Jonas Olson (eds.), *Oxford Handbook of Value Theory*, Oxford: Oxford University Press, pp. 424–443.

[^bales-1971]: Bales, Eugene, 1971, “Act-utilitarianism: Account of Right-making Characteristics or Decision-making Procedure?”, *American Philosophical Quarterly*, 8(3): 257–265.

[^blackorby-1997]: Blackorby, Charles, Walter Bossert and David Donaldson, 1997, “Critical Level Utilitarianism and the Population-ethics Dilemma”, *Economics and Philosophy*, 13(2): 197–230.

[^blackorby-2002]: –––, 2002, “Utilitarianism and the Theory of Justice,” in Kenneth J. Arrow, Amartya K. Sen, and Kotaro Suzumura (eds.), *Handbook of Social Choice and Welfare*, Amsterdam: Elsevier, vol. 1, pp. 543–596.

[^blackorby-2005]: –––, 2005, *Population Issues in Social Choice Theory, Welfare Economics, and Ethics*, Cambridge: Cambridge University Press.

[^bognar-2012]: Bognar, Greg, 2012, “Empirical and Armchair Ethics”, *Utilitas*, 24(4): 467–82.

[^bossert-2022]: Bossert, Walter, Susumu Cato, and Kohei Kamaga, 2022, “Critical-level Sufficientarianism”, *Journal of Political Philosophy*, 30(4): 434–461.

[^bovens-2015]: Bovens, Luc, 2015, “Concerns for the Poorly Off in Ordering Risky Prospects”, *Economics and Philosophy*, 31(3): 397–429.

[^bradley-2013]: Bradley, Ben, 2013, “Asymmetries in Benefiting, Harming and Creating”, *Journal of Ethics*, 17(1/2): 37–49.

[^briggs-2023]: Briggs, R.A., 2023, “Normative Theories of Rational Choice: Expected Utility,” *Stanford Encyclopedia of Philosophy* (Winter 2023 Edition), Edward N. Zalta and Uri Nodelman (eds.), URL = <https://plato.stanford.edu/archives/win2023/entries/rationality-normative-utility/>

[^broome-1991]: Broome, John, 1991, *Weighing Goods: Equality, Uncertainty, and Time*, Oxford: Basil Blackwell.

[^broome-1993]: –––, 1993, “Goodness is Reducible to Betterness: The Evil of Death is the Value of Life”, in Peter Koslowski and Yuichi Shionoya (eds.), *The Good and the Economical*, Berlin: Springer-Verlag, pp. 70–84.

[^broome-2015]: –––, 2015, “Equality versus Priority: A Useful Distinction”, *Economics and Philosophy*, 31(2): 219–228.

[^brown-2005]: Brown, Campbell, 2005, “Priority or Sufficiency … or both?”, *Economics and Philosophy*, 21(2): 199–220.

[^brown-2007]: –––, 2007, “Prioritarianism for Variable Populations”, *Philosophical Studies*, 134(3): 325–361.

[^brunori-2022]: Brunori, Paolo, Francisco H.G. Ferreira, and Vito Peragine, 2022, “Prioritarianism and Equality of Opportunity”, in Matthew D. Adler and Ole F. Norheim (eds.), *Prioritarianism in Practice*, Cambridge: Cambridge University Press, pp. 518–571.

[^buchak-2017]: Buchak, Lara, 2017, “Taking Risks Behind the Veil of Ignorance”, *Ethics*, 127(3): 610–644.

[^buchak-2023]: –––, 2023, “Relative Priority”, *Economics and Philosophy*, 39(2): 199–229.

[^bykvist-2007]: Bykvist, Krister, 2007, “The Benefits of Coming into Existence”, *Philosophical Studies*, 135: 335–62.

[^carlson-1995]: Carlson, Erik, 1995, *Consequentialism Reconsidered*, Dordrecht: Kluwer Academic Publishers.

[^casal-2007]: Casal, Paula, 2007, “Why Sufficiency is Not Enough”, *Ethics*, 177(2): 296–326.

[^cowell-2016]: Cowell, Frank, 2016, “Inequality and Poverty Measures”, in Matthew D. Adler and Marc Fleurbaey (eds.), *The Oxford Handbook of Well-Being and Public Policy*, Oxford: Oxford University Press, pp. 82–125.

[^crisp-2003]: Crisp, Roger, 2003, “Equality, Priority, and Compassion”, *Ethics*, 113(4): 745–763.

[^crisp-2011]: Crisp, Roger, 2011, “In Defence of the Priority View: A Response to Otsuka and Voorhoeve”, *Utilitas*, 23(1): 99–108.

[^eyal-2023]: Eyal, Nir, and Anders Herlitz, 2023, “Input and Output in Distributive Theory”, *Nous*, 57(1): 3–25.

[^feinberg-1980]: Feinberg, Joel, 1980, “The Rights of Animals and Unborn Generations”, in Joel Feinberg, *Rights, Justice, and the Bounds of Liberty*, Princeton: Princeton University Press, pp. 159–84.

[^fleurbaey-2010]: Fleurbaey, Marc, 2010, “Assessing Risky Social Situations”, *Journal of Political Economy*, 118(4): 649–680.

[^fleurbaey-2015]: –––, 2015, “Equality versus Priority: How Relevant is the Distinction?”, *Economics and Philosophy*, 31(2): 203–217.

[^frankfurt-1987]: Frankfurt, Harry, 1987, “Equality as a Moral Ideal”, *Ethics*, 98(1): 21–43.

[^gilboa-2009]: Gilboa, Itzhak, 2009, *Theory of Decision under Uncertainty*, Cambridge: Cambridge University Press.

[^greaves-2015]: Greaves, Hilary, 2015, “Antiprioritarianism”, *Utilitas*, 27(1): 1–42.

[^greaves-2017a]: –––, 2017a, “Population Axiology”, *Philosophy Compass*, 12(11), e12442.

[^greaves-2017b]: –––, 2017b, “A Reconsideration of the Harsanyi-Sen-Weymark Debate on Utilitarianism,” *Utilitas*, 29(2): 175–213.

[^hare-1981]: Hare, Richard M., 1981, *Moral Thinking*, Oxford: Clarendon Press.

[^harsanyi-1953]: Harsanyi, John C., 1953, “Cardinal Utility in Welfare Economics and in the Theory of Risk-Taking”, *Journal of Political Economy*, 61(5): 434–435.

[^harsanyi-1955]: –––, 1955, “Cardinal Welfare, Individualistic Ethics, and Interpersonal Comparisons of Utility”, *Journal of Political Economy*, 63(4): 309–321.

[^harsanyi-1977]: –––, 1977, *Rational Behavior and Bargaining Equilibrium in Games and Social Situations* Cambridge: Cambridge University Press.

[^heyd-1992]: Heyd, David, 1992, *Genethics. Moral Issues in the Creation of People*, Berkeley: University of California Press.

[^holtug-1999]: Holtug, Nils, 1999, “Utility, Priority, and Possible People”, *Utilitas*, 11(1): 16–36.

[^holtug-2007a]: –––, 2007a, “Prioritarianism,” in Nils Holtug and Kasper Lippert-Rasmussen (eds.), *Egalitarianism. New Essays on the Nature and Value of Equality*, Oxford: Clarendon Press, pp. 125–156.

[^holtug-2007b]: –––, 2007b, “Animals: Equality for Animals”, in Jesper Ryberg, Thomas S. Petersen, and Clark Wolf (eds.), *New Waves in Applied Ethics*, Basingstoke: Palgrave Macmillan, pp. 1–24.

[^holtug-2009]: –––, 2009, “Equality, Priority, and Global Justice”, *Journal of Global Ethics*, 5(3): 173–179.

[^holtug-2010]: –––, 2010, *Persons, Interests, and Justice*, Oxford: Oxford University Press.

[^holtug-2015a]: –––, 2015a, “The Value of Coming into Existence”, in Tatjana Visak and Robert Garner (eds.), *The Ethics of Killing Animals*, Oxford: Oxford University Press, pp. 101–14.

[^holtug-2019]: –––, 2019, “Prioritarianism: Ex Ante, Ex Post, or Factualist Criterion of Rightness?”, *Journal of Political Philosophy*, 27(2): 207–228.

[^holtug-2021]: –––, 2021, “Prioritarianism, Risk, and the Gap Between Prudence and Morality”, in Jeff McMahan, Tim Campbell, James Goodrich, and Ketan Ramakrishnan (eds.), *Principles and Persons. The Legacy of Derek Parfit*, Oxford: Oxford University Press, pp. 393–411.

[^holtug-2022]: –––, 2022, “Prioritarianism and Population Ethics”, in Gustaf Arrhenius, Krister Bykvist, Tim Campbell, and Elizabeth Finneron-Burns (eds.), *The Oxford Handbook of Population Ethics*, Oxford: Oxford University Press, pp. 38–62.

[^hooker-2000]: Hooker, Brad, 2000, *Ideal Code, Real World*, Oxford: Clarendon Press.

[^hyams-2015]: Hyams, Keith, 2015, “Hypothetical Choice, Egalitarianism and the Separateness of Persons”, *Utilitas*, 27(2): 217–239.

[^jensen-2003]: Jensen, Karsten Klint, 2003, “What is the Difference between (Moderate) Egalitarianism and Prioritarianism?”, *Economics and Philosophy*, 19(1): 89–109.

[^johansson-2010]: Johansson, Jens, 2010, “Being and Betterness”, *Utilitas*, 22(3): 285–302.

[^kreps-1988]: Kreps, David M., 1988, *Notes on the Theory of Choice*, Boulder: Westview Press.

[^mccarthy-2006]: McCarthy, David, 2006, “Utilitarianism and Prioritarianism I”, *Economics and Philosophy*, 22(3): 335–363.

[^mccarthy-2008]: –––, 2008, “Utilitarianism and Prioritarianism II”, *Economics and Philosophy*, 24(1): 1–33.

[^mccarthy-2013]: –––, 2013, “Risk-Free Approaches to the Priority View”, *Erkenntnis*, 78: 421–449.

[^mccarthy-2017]: –––, 2017, “The Priority View”, *Economics and Philosophy*, 33(2): 215–257.

[^mckerlie-1984]: McKerlie, Dennis, 1984, “Egalitarianism”, *Dialogue*, 23(2): 223–237.

[^mckerlie-1997]: –––, 1997, “Priority and Time”, *Canadian Journal of Philosophy*, 27(3): 287–309.

[^mckerlie-2001a]: –––, 2001a, “Dimensions of Equality”, *Utilitas*, 13(3): 263–288.

[^mckerlie-2001b]: –––, 2001b, “Justice Between the Young and the Old”, *Philosophy and Public Affairs*, 30(2): 152–177.

[^mckerlie-2007]: –––, 2007, “Egalitarianism and the Difference between Interpersonal and Intrapersonal Judgments”, in Nils Holtug and Kasper Lippert-Rasmussen (eds.), *Egalitarianism: New Essays on the Nature and Value of Equality*, Oxford: Clarendon Press, pp. 157–173.

[^mckerlie-2013]: –––, 2013, *Justice between the Young and the Old*, New York: Oxford University Press.

[^mcmahan-2013]: McMahan, Jeff, 2013, “Causing People to Exist and Saving People’s Lives”, *Journal of Ethics*, 17(1/2): 5–35.

[^mongin-2016]: Mongin, Philippe, and Marcus Pivato, 2016, “Social Evaluation under Risk and Uncertainty”, in Matthew D. Adler and Marc Fleurbaey (eds.), *Oxford Handbook of Well-Being and Public Policy*, Oxford: Oxford University Press, pp. 65–85.

[^moreno-ternero-2008]: Moreno-Ternero, Juan D., and John E. Roemer, 2008, “The Veil of Ignorance Violates Priority”, *Economics and Philosophy*, 24(2): 233–257.

[^nagel-1979]: Nagel, Thomas, 1979, *Mortal Questions*, Cambridge: Cambridge University Press.

[^nagel-1991]: –––, 1991, *Equality and Priority*, New York: Oxford University Press.

[^narveson-1967]: Narveson, Jan, 1967, “Utilitarianism and New Generations”, *Mind*, 76(301): 62–72.

[^nebel-2017]: Nebel, Jacob M., 2017, “Priority, Not Equality, for Possible People”, *Ethics*, 127(4): 896–911.

[^o’neill-2012]: O’Neill, Martin, 2012, “Priority, Preference and Value”, *Utilitas*, 24(3): 332–48

[^ord-2015]: Ord, Toby, 2015, “A New Counterexample to Prioritarianism”, *Utilitas*, 27(3): 298–302

[^otsuka-2015]: Otsuka, Michael, 2015, “Prioritarianism and the Measure of Utility”, *Journal of Political Philosophy*, 23(1): 1–22.

[^otsuka-2022]: –––, 2022, “Prioritarianism, Population Ethics, and Competing Claims,”, in Jeff McMahan, Tim Campbell, James Goodrich, and Ketan Ramakrishnan (eds.), *Ethics and Existence. The Legacy of Derek Parfit*, Oxford: Oxford University Press, pp. 527–551.

[^otsuka-2009]: Otsuka, Michael and Alex Voorhoeve, 2009, “Why it Matters that Some are Worse off than Others: An Argument Against the Priority View”, *Philosophy and Public Affairs*, 37(2): 171–99.

[^otsuka-2018]: –––, 2018, “Equality versus Priority”, in Serena Olsaretti (ed.), *Oxford Handbook of Distributive Justice*, Oxford: Oxford University Press, pp. 65–85.

[^parfit-1987]: Parfit, Derek, 1987, *Reasons and Persons*, Oxford: Clarendon Press. Revised and corrected edition, first published in 1984.

[^parfit-2000]: –––, 2000, “Equality or Priority,” in Matthew Clayton and Andrew Williams (eds.), *The Ideal of Equality*, Houndmills: Palgrave, pp. 81–125. Delivered as the Lindley Lecture at the University of Kansas in 1991.

[^parfit-2004]: –––, 2004, “Postscript”, in Jesper Ryberg and Torbjörn Tännsjö (eds.), *The Repugnant Conclusion. Essays on Population Ethics*, Dordrecht: Kluwer Academic Publishers, p. 257.

[^parfit-2012]: –––, 2012, “Another Defence of the Priority View”, *Utilitas*, 24(3): 399–440

[^persson-1997]: Persson, Ingmar, 1997, “Person-affecting Principles and Beyond”, in Nick Fotion and Jan C. Heller (eds.), *Contingent Future Persons*, Dordrecht: Kluwer Academic Publishers, pp. 41–56.

[^porter-2011]: Porter, Thomas, 2011, “Prioritarianism and the Levelling Down Objection”, *Ethical Theory and Moral Practice*, 14(2): 197–206.

[^porter-2012]: –––, 2012, “In Defence of the Priority View”, *Utilitas*, 24(3): 349–64.

[^rabinowicz-2001]: Rabinowicz, Wlodek, 2001, “Prioritarianism and Uncertainty: On the Interpersonal Addition Theorem and the Priority View”, in Dan Egonsson et al. (eds.), *Exploring Practical Philosophy: From Action to Values*, Adlershot: Ashgate, pp. 139–165.

[^rawls-1999]: Rawls, John, 1999, *A Theory of Justice*, Revised Edition, Cambridge, MA: Belknap Press of Harvard University Press. First published in 1971.

[^rendall-2013]: Rendall, Matthew, 2013, “Priority and Desert”, *Ethical Theory and Moral Practice*, 16(5): 939–51.

[^roberts-1998]: Roberts, Melinda A., 1998, *Child versus Childmaker: Future Persons and Present Duties in Ethics and the Law*, Lanham, MD: Rowman & Littlefield.

[^segall-2015]: Segall, Shlomi, 2015, “In Defence of Priority (and Equality)”, *Politics, Philosophy and Economics*, 14(4): 343–64.

[^segall-2022]: –––, 2022, “Quarantined Prioritarianism”, in Jeff McMahan, Tim Campbell, James Goodrich, and Ketan Ramakrishnan (eds.), *Ethics and Existence. The Legacy of Derek Parfit*, Oxford: Oxford University Press, pp. 552–576.

[^sen-1976]: Sen, Amartya, 1976, “Welfare Inequalities and Rawlsian Axiomatics,” *Theory and Decision* 7(4): 243–62.

[^shields-2020]: Shields, Liam, 2020, “Sufficientarianism”, *Philosophy Compass*, 15(11), e12704.

[^sikora-1978]: Sikora, Richard I., 1978, “Is It Wrong to Prevent the Existence of Future Generations?”, in Richard I. Sikora and Brian Barry (eds.), *Obligations to Future Generations*, Philadelphia: The White Horse Press, pp. 112–166.

[^steinbock-1992]: Steinbock, Bonnie, 1992, *Life Before Birth*, Oxford: Oxford University Press.

[^temkin-1983]: Temkin, Larry S., 1983, *Inequality*, Ph.D. Thesis, Princeton University.

[^temkin-1993]: –––, 1993, *Inequality*, New York: Oxford University Press.

[^temkin-2003]: –––, 2003, “Equality, Priority or What?”, *Economics and Philosophy*, 19(1): 61–87.

[^vallentyne-2005]: Vallentyne, Peter, 2005, “Of Mice and Men: Equality and Animals”, *Journal of Ethics*, 9(9): 403–433.

[^weirich-1983]: Weirich, Paul, 1983, “Utility Tempered with Equality”, *Nous*, 17(3): 423–439.

[^weymark-1991]: Weymark, John, 1991, “A Reconsideration of the Harsanyi-Sen Debate on Utilitarianism”, in Jon Elster and John E. Roemer (eds.), *Interpersonal Comparisons of Well-Being*, Cambridge: Cambridge University Press, pp. 255–320.

[^williams-2012]: Williams, Andrew, 2012, “The Priority View Bites the Dust?”, *Utilitas*, 24(3): 315–331.

[^wolf-1997]: Wolf, Clark, 1997, “Person-affecting Utilitarianism and Population Policy; Or, Sissy Jupe’s Theory of Social Choice”, in Nick Fotion and Jan C. Heller (eds.), *Contingent Future Persons*, Dordrecht: Kluwer Academic Publishers, pp. 99–122.

[^agmon-2019]: Agmon, Shai S.Y., and Matt Hitchens, 2019, “Prioritarianism: A (Pluralist) Defence”, *Journal of Ethics and Social Philosophy*, 15(1): 19–42.

[^shalit-2023]: de-Shalit, Avner, 2023, “Do the Current Poor Owe Anything to Future Persons? The Transgenerational Community Principle and Prioritarianism”, *The Monist*, 106(2): 105–118.

[^dorsey-2014]: Dorsey, Dale, 2014, “Equality-tempered Prioritarianism”, *Politics, Philosophy and Economics*, 13(1): 45–61.

[^enflo-2022]: Enflo, Karin, 2022, “The Equivalence of Egalitarianism and Prioritarianism”, *Journal of Ethics and Social Philosophy*, 22(1): 74–108.

[^francis-2024]: Francis, Tomi, 2024, “The Welfare Diffusion Objection to Prioritarianism”, *Economics and Philosophy*, 40(1): 55–76.

[^gustafsson-2022]: Gustafsson, Johan E., 2022, “Ex-Ante Prioritarianism Violates Sequential Ex-Ante Pareto”, *Utilitas*, 34(2): 167–177.

[^hanisch-2020]: Hanisch, Christoph, 2020, “Telic Priority: Prioritarianism’s Impersonal Value”, *Moral Philosophy and Politics*, 7(1): 169–189.

[^herlitz-2018]: Herlitz, Anders, 2018, “Against Lifetime QALY Prioritarianism”, *Journal of Medical Ethics*, 44(2): 109–113.

[^hirose-2014]: Hirose, Iwao, 2014, *Egalitarianism*, New York: Routledge.

[^holtug-2015b]: Holtug, Nils, 2015b, “Theories of Value Aggregation: Utilitarianism, Egalitarianism, Prioritarianism”, in Iwao Hirose and Jonas Olson (eds.), *The Oxford Handbook of Value Theory*, Oxford: Oxford University Press, pp. 267–284.

[^inoue-2024]: Inoue, Akira, Kazumi Shimizu, Daisuke Udagawa, and Yoshiki Wakamatsu, 2024, “Reflective Equilibrium in Practice and Model Selection: A Methodological Proposal from a Survey Experiment on the Theories of Distributive Justice”, *Synthese*, 203(5): 1–31.

[^lange-2017]: Lange, Benjamin, 2017, “Restricted Prioritarianism or Competing Claims?”, *Utilitas*, 29(2): 137–152.

[^lumer-2021]: Lumer, Christoph, 2021, “From Utilitarianism to Prioritarianism: An Empathy-Based Internalist Foundation of Welfare Ethics,” in Michael Schefczyk and Christoph Schmidt-Petri (eds.), *Utility, Progress, and Technology*, Karlsruhe: KIT Scientific Publishing, pp. 139–151.

[^mckerlie-1994]: McKerlie, Dennis, 1994, “Equality and Priority”, *Utilitas*, 6(1): 25–42.

[^nebel-2023]: Nebel, Jacob M., and Orri Stefánsson, 2023, “Calibration Dilemmas in the Ethics of Distribution”, *Economics and Philosophy*, 39(1): 67–98.

[^nielsen-2022]: Nielsen, Lasse, 2022, “Pandemic Prioritarianism”, *Journal of Medical Ethics*, 48(4): 236–239.

[^otsuka-2012]: Otsuka, Michael, 2012, “Prioritarianism and the Separateness of Persons”, *Utilitas*, 24(3): 365–380.

[^persson-2001]: Persson, Ingmar, 2001, “Equality, Priority and Person-affecting Value”, *Ethical Theory and Moral Practice*, 4(1): 23–39.

[^persson-2008]: –––, 2008, “Why Levelling Down Could be Worse for Prioritarianism than for Egalitarianism”, *Ethical Theory and Moral Practice*, 11(3), 295–303.

[^persson-2011]: –––, 2011, “Prioritarianism, Levelling Down and Welfare Diffusion”, *Ethical Theory and Moral Practice*, 14(3): 307–311.

[^persson-2012]: –––, 2012, “Prioritarianism and Welfare Reductions”, *Journal of Applied Philosophy*, 29(3): 289–301.

[^peterson-2010]: Peterson, Martin, 2010, “Can Consequentialists Honour the Special Moral Status of Persons?”, *Utilitas*, 22(4): 434–446.

[^peterson-2005]: Peterson, Martin and Sven Ove Hansson, 2005, “Equality and Priority”, *Utilitas*, 17(3): 299–309.

[^rabinowicz-2002]: Rabinowicz, Wlodek, 2002, “Prioritarianism for Prospects”, *Utilitas*, 14(1): 2–21.

[^raz-1986]: Raz, Joseph, 1986, *The Morality of Freedom*, Oxford: Clarendon Press.

[^segall-2024]: Segall, Shlomi, 2024, “To Be (Disadvantaged) or Not to Be? An Egalitarian Guide for Creating New People”, *Politics, Philosophy and Economics*, 23(2): 154–180.

[^sharp-2018]: Sharp, Daniel, and Joseph Millum, 2018, “Prioritarianism for Global Health Investments: Identifying the Worst Off”, *Journal of Applied Philosophy*, 35(1): 112–132.

[^soto-2024]: Soto, Carlos, 2024, “Three Kinds of Prioritarianism”, *Journal of Ethics and Social Philosophy*, 28(1): 110–140.

[^stefánsson-2021]: Stefánsson, Orri, 2021, “Ambiguity Aversion behind the Veil of Ignorance”, *Synthese*, 198(7): 6159–6182.

[^ta-2015]: Tännsjö, Torbjörn, 2015, “Utilitarianism or Prioritarianism?”, *Utilitas*, 27(2): 240–250.

[^temkin-2000]: Temkin, Larry, 2000, “Equality, Priority, and the Levelling Down Objection”, in Matthew Clayton and Andrew Williams (eds.), *The Ideal of Equality*, London: MacMillan Press Ltd, pp. 126–161.

[^weber-2014]: Weber, Michael, 2014, “Prioritarianism”, *Philosophy Compass* 9(11): 756–768.

[^winters-2020]: Winters, Niall, Sridhar Venkatapuram, Anne Geniets, and Emma Wynne-Bannister, 2020, “Prioritarian Principles for Digital Health in Low Resource Settings”, *Journal of Medical Ethics*, 46(4): 259–264.
