# Interpretations of Probability
**First published Mon Oct 21, 2002; substantive revision Thu Nov 16, 2023**

*Hájek, Alan*

> *Probability is the most important concept in modern science, especially as nobody has the slightest notion what it means.* —Bertrand Russell, 1929 Lecture
> (cited in Bell 1945, 587)[^bell-1945]

One regularly reads and hears probabilistic claims like the following:

- The Democrats will probably win the next election.
- The coin is just as likely to land heads as tails.
- There’s a 30% chance of rain tomorrow.
- The probability that a radium atom decays in one year is roughly 0.0004.

But what do these statements mean? This may be understood as a metaphysical question about what kinds of things are probabilities, or more generally as a question about what makes probability statements true or false. At a first pass, various *interpretations of probability* answer this question, one way or another.

However, there is also a stricter usage: an ‘interpretation’ *of a formal theory* provides meanings for its primitive symbols or terms, with an eye to turning its axioms and theorems into true statements about some subject. In the case of probability, Kolmogorov’s axiomatization (which we will see shortly) is the usual formal theory, and the so-called ‘interpretations of probability’ usually interpret *it*. That axiomatization introduces a function ‘$P$’ that has certain formal properties. We may then ask ‘What is $P$?’. Several of the views that we will discuss also answer this question, one way or another.

Our topic is complicated by the fact that there are various alternative formalizations of probability. Moreover, as we will see, some of the leading ‘interpretations of probability’ do *not* obey all of Kolmogorov’s axioms, yet they have not lost their title for that. And various other quantities that have nothing to do with probability *do* satisfy Kolmogorov’s axioms, and thus are ‘interpretations’ of it in the strict sense: normalized mass, length, area, volume, and other quantities that fall under the scope of measure theory, the abstract mathematical theory that generalizes such quantities. Nobody seriously considers these to be ‘interpretations of probability’, however, because they do not play the right role in our conceptual apparatus.

Perhaps we would do better, then, to think of the interpretations as *analyses* of various concepts of probability. Or perhaps better still, we might regard them as *explications* of such concepts, refining them to be fruitful for philosophical and scientific theorizing (à la Carnap 1950, 1962)[^carnap-1950].

However we think of it, the project of finding such interpretations is an important one. Probability is virtually ubiquitous. It plays a role in almost all the sciences. It underpins much of the social sciences — witness the prevalent use of statistical testing, confidence intervals, regression methods, and so on. It finds its way, moreover, into much of philosophy. In epistemology, the philosophy of mind, and cognitive science, we see states of opinion being modeled by subjective probability functions, and learning being modeled by the updating of such functions. Since probability theory is central to decision theory and game theory, it has ramifications for ethics and political philosophy. It figures prominently in such staples of metaphysics as causation and laws of nature. It appears again in the philosophy of science in the analysis of confirmation of theories, scientific explanation, and in the philosophy of specific scientific theories, such as quantum mechanics, statistical mechanics, evolutionary biology, and genetics. It can even take center stage in the philosophy of logic, the philosophy of language, and the philosophy of religion. Thus, problems in the foundations of probability bear at least indirectly, and sometimes directly, upon central scientific, social scientific, and philosophical concerns. The interpretation of probability is one of the most important such foundational problems.

## 1. Kolmogorov’s Probability Calculus

Probability theory was a relative latecomer in intellectual history. To be sure, proto-probabilistic ideas concerning evidence and inference date back to antiquity (see Franklin 2001)[^franklin-2001]. However, probability’s mathematical treatment had to wait until the Fermat-Pascal correspondence, and their analysis of games of chance in 17ᵗʰ century France. Its axiomatization had to wait still longer, in Kolmogorov’s classic *Foundations of the Theory of Probability* (1933). Roughly, probabilities lie between 0 and 1 inclusive, and they are additive. More formally, let $\Omega$ be a non-empty set (‘the universal set’). A *field* (or *algebra*) on $\Omega$ is a set $\mathbf{F}$ of subsets of $\Omega$ that has $\Omega$ as a member, and that is closed under complementation (with respect to $\Omega)$ and union. Let $P$ be a function from $\mathbf{F}$ to the real numbers obeying:

1. (Non-negativity) $P(A) \ge 0$, for all $A \in \mathbf{F}$.
2. (Normalization) $P(\Omega) = 1$.
3. (Finite additivity) $P(A \cup B) = P(A) + P(B)$ for all $A, B \in \mathbf{F}$ such that $A \cap B = \varnothing$.

Call $P$ a *probability function*, and $(\Omega , \mathbf{F}, P)$ a *probability space*. This is Kolmogorov’s “elementary theory of probability”.

The non-negativity and normalization axioms are largely matters of convention, although it is non-trivial that probability functions take at least the two values 0 and 1, and that they have a maximal value (unlike various other measures, such as length, volume, and so on, which are unbounded). We will return to finite additivity at a number of points below.

We may now apply the theory to various familiar cases. For example, we may represent the results of tossing a single die once by the set $\Omega = \{1, 2, 3, 4, 5, 6\}$, and we could let $\mathbf{F}$ be the set of all subsets of $\Omega$. Under the natural assignment of probabilities to members of $\mathbf{F}$, we obtain such welcome results as the following:

$$\begin{align} P(\{1\}) &= \frac{1}{6}, \\ P(\text{even}) &= P(\{2\} \cup \{4\} \cup \{6\}) \\ &= \frac{3}{6}, \\ P(\text{odd or less than 4}) &= P(\text{odd}) + P(\text{less than 4}) - P(\text{odd} \cap \text{less than 4}) \\ &= \frac{1}{2} + \frac{1}{2} - \frac{2}{6} \\ &= \frac{4}{6}, \end{align}$$

and so on.

We could instead attach probabilities to members of a collection $\mathbf{S}$ of *sentences* of a formal language, closed under (countable) truth-functional combinations, with the following counterpart axiomatization:

1. $P(A) \ge 0$ for all $A \in \mathbf{S}$.
2. If $T$ is a logical truth (in classical logic), then $P(T) = 1$.
3. $P(A \vee B) = P(A) + P(B)$ for all $A \in \mathbf{S}$ and $B \in \mathbf{S}$ such that $A$ and $B$ are logically incompatible.

The bearers of probabilities are sometimes also called “events”, “outcomes”, or “propositions”, but the underlying formalism remains the same. More attention has been given to interpreting ‘$P$’ than to interpreting its bearers; we will be concerned with the former.

The elementary theory of probability suffices for most everyday applications of probability, and it will suffice for most of our discussion below. But more advanced treatments in mathematics, statistics, and science require more mathematical sophistication involving *countable* infinite extensions. (Readers less interested in the mathematical details may want to skip to "*The conditional probability ...*" three paragaphs below.) Now let us strengthen our closure assumptions regarding $\mathbf{F}$, requiring it to be closed under complementation and *countable* union; it is then called a *sigma field* (or *sigma algebra)* on $\Omega$. It is controversial whether we should strengthen finite additivity, as Kolmogorov does:

$3'$. (Countable additivity) If $A_1, A_2, A_3\ldots$ is a countably infinite sequence of (pairwise) disjoint sets, each of which is an element of $\mathbf{F}$, then $$ P(\bigcup_{n=1}^{\infty} A_n) = \sum_{n=1}^{\infty} P(A_n) $$

Kolmogorov comments that infinite probability spaces are idealized models of real random processes, and that he limits himself arbitrarily to only those models that satisfy countable additivity. This axiom is the cornerstone of the assimilation of probability theory to measure theory.

*The conditional probability of A given B* is then given by the ratio of unconditional probabilities:

$$ P(A\mid B) = \frac{P(A\cap B)}{P(B)},\text{ provided } P(B) \gt 0. $$

This is often taken to be the *definition* of conditional probability, although it should be emphasized that this is a technical usage of the term that may not align perfectly with a pretheoretical concept that we might have (see Hájek, 2003)[^hájek-2003]. We recognize it in locutions such as “the probability that the die lands 1, given that it lands odd, is 1/3”, or “the probability that it will rain tomorrow, given that there are dark clouds in the sky tomorrow morning, is high”. It is the concept of the probability of something *given* or *in the light of* some piece of evidence or information. Indeed, some authors take conditional probability to be the primitive notion, and axiomatize it directly (e.g. Popper 1959b, Rényi 1970, van Fraassen 1976, Spohn 1986, and Roeper and Leblanc 1999)[^popper-1959b][^rényi-1970][^roeper-1999][^spohn-1986].

There are other formalizations that give up normalization; that give up countable additivity, and even additivity; that allow probabilities to take infinitesimal values (positive, but smaller than every positive real number); that allow probabilities to be imprecise — interval-valued, or more generally represented with sets of precise probability functions; and that treat probabilities comparatively rather than quantitatively. (See Fine 1974, Halpern 2003, Cozman 2016, Fine 2016, Hawthorne 2016, Lyon 2016.)[^cozman-2016][^fine-2016][^halpern-2003][^hawthorne-2016][^lyon-2016] For now, however, when we speak of ‘the probability calculus’, we will mean Kolmogorov’s approach, as is standard. See Hájek and Hitchcock (2016b) for a relatively non-technical introduction to it, intended for philosophers.

Given certain probabilities as inputs, the axioms and theorems allow us to compute various further probabilities. However, apart from the assignment of 1 to the universal set and 0 to the empty set, they are silent regarding the initial assignment of probabilities.[^note-1] For guidance with that, we need to turn to the interpretations of probability. First, however, let us list some criteria of adequacy for such interpretations.

## 2. Criteria of Adequacy for the Interpretations of Probability

What criteria are appropriate for assessing the cogency of a proposed interpretation of probability? Of course, an interpretation should be precise, unambiguous, non-circular, and use well-understood primitives. But those are really prescriptions for good philosophizing generally; what do we want from our interpretations *of probability*, specifically? We begin by following Salmon (1966, 64)[^salmon-1966], although we will raise some questions about his criteria, and propose some others. He writes:

> *Admissibility.* We say that an interpretation of a formal system is admissible if the meanings assigned to the primitive terms in the interpretation transform the formal axioms, and consequently all the theorems, into true statements. A fundamental requirement for probability concepts is to satisfy the mathematical relations specified by the calculus of probability…
>
> *Ascertainability.* This criterion requires that there be some method by which, in principle at least, we can ascertain values of probabilities. It merely expresses the fact that a concept of probability will be useless if it is impossible in principle to find out what the probabilities are…
>
> *Applicability.* The force of this criterion is best expressed in Bishop Butler’s famous aphorism, “Probability is the very guide of life.”…

It might seem that the criterion of admissibility goes without saying. The word ‘interpretation’ is often used in such a way that ‘admissible interpretation’ is a pleonasm. Yet it turns out that the criterion is non-trivial, and indeed if taken seriously would rule out several of the leading interpretations of probability! As we will see, some of them fail to satisfy countable additivity; for others (certain propensity interpretations) the status of at least some of the axioms is unclear. Nevertheless, we regard them as genuine candidates. It should be remembered, moreover, that Kolmogorov’s is just one of many possible axiomatizations, and there is not universal agreement on which is ‘best’ (whatever that might mean). Indeed, Salmon’s preferred axiomatization differs from Kolmogorov’s.[^note-2] Thus, there is no such thing as admissibility *tout court*, but rather admissibility with respect to this or that axiomatization. In any case, if we found an inadmissible interpretation (with respect to Kolmogorov’s axiomatization) that did a wonderful job of meeting the criteria of ascertainability and applicability, then we should surely embrace it.

So let us turn to those criteria. It is a little unclear in the ascertainability criterion just what “in principle” amounts to – it outruns what is practical or feasible – though perhaps some latitude here is all to the good. Most of the work will be done by the applicability criterion. We must say more (as Salmon indeed does) about what *sort* of a guide to life probability is supposed to be. Mass, length, area and volume are all useful concepts, and they are ‘guides to life’ in various ways (think how critical distance judgments can be to survival); moreover, they are admissible and ascertainable, so presumably it is the applicability criterion that will rule them out. Perhaps it is best to think of applicability as a cluster of criteria, each of which is supposed to capture something of probability’s distinctive conceptual roles; moreover, we should not require that all of them be met by a given interpretation. They include:

*Non-triviality:* an interpretation should make non-extreme probabilities at least a conceptual possibility. For example, suppose that we interpret ‘$P$’ as the *truth* function: it assigns the value 1 to all true sentences, and 0 to all false sentences. Then trivially, all the axioms come out true, so this interpretation is admissible. We would hardly count it as an adequate *interpretation of* *probability*, however, and so we need to exclude it. It is essential to probability that, at least in principle, it can take *intermediate* values. All of the interpretations that we will present meet this criterion, so we will discuss it no more.

*Applicability to frequencies:* an interpretation should render perspicuous the relationship between probabilities and (long-run) frequencies. Among other things, it should make clear why, by and large, more probable events occur more frequently than less probable events.

*Applicability to rational beliefs:* an interpretation should clarify the role that probabilities play in constraining the degrees of belief, or *credences*, of rational agents. Among other things, knowing that one event is more probable than another, a rational agent will be more confident about the occurrence of the former event.

*Applicability to rational decisions*: an interpretation should make clear how probabilities figure in rational decision-making. This seems especially apposite for a ‘guide to life’.

*Applicability to ampliative inferences:* an interpretation will score bonus points if it illuminates the distinction between ‘good’ and ‘bad’ ampliative inferences, while explicating why both fall short of deductive inferences.

*Applicability to science:* an interpretation should illuminate paradigmatic uses of probability in science (for example, in quantum mechanics and statistical mechanics).

Perhaps there are further *metaphysical* desiderata that we might impose on the interpretations. For example, there appear to be connections between probability and *modality.* Events with positive probability *can* happen, even if they don’t. Some authors also insist on the converse condition that *only* events with positive probability can happen, although this is more controversial — see our discussion of ‘regularity’ in Section 3.3.4. (Indeed, in uncountable probability spaces this condition will require the employment of infinitesimals, and will thus take us beyond the standard Kolmogorov theory — ‘standard’ both in the sense of being the orthodoxy, and in its employment of standard, as opposed to ‘non-standard’ real numbers. See Skyrms 1980.) In any case, our list is already long enough to help in our assessment of the leading interpretations on the market.

## 3. The Main Interpretations

Broadly speaking, there are arguably three main concepts of probability:

1. An epistemological concept, which is meant to measure objective evidential support relations. For example, “in light of the relevant seismological and geological data, California will *probably* experience a major earthquake this decade”.
2. The concept of an agent’s degree of confidence, a graded belief. For example, “I am not sure that it will rain in Canberra this week, but it *probably* will.”
3. A physical concept that applies to various systems in the world, independently of what anyone thinks. For example, “a particular radium atom will *probably* decay within 10,000 years”.

Some philosophers will insist that not all of these concepts are intelligible; some will insist that one of them is basic, and that the others are reducible to it. Moreover, the boundaries between these concepts are somewhat permeable. After all, ‘degree of confidence’ is itself an epistemological concept, and as we will see, it is thought to be rationally constrained both by evidential support relations and by attitudes to physical probabilities in the world. And there are intramural disputes within the camps supporting each of these concepts, as we will also see. Be that as it may, it will be useful to keep these concepts in mind. Sections 3.1 and 3.2 discuss analyses of concept (1), *classical* and *logical/evidential* probability; 3.3 discusses analyses of concept (2), *subjective* probability; 3.4, 3.5, and 3.6 discuss three analyses of concept (3), *frequentist*, *propensity*, and *best-system* interpretations.

### 3.1 Classical Probability

The classical interpretation owes its name to its early and august pedigree. It was championed by de Moivre and Laplace, and inchoate versions of it may be found in the works of Pascal, Bernoulli, Huygens, and Leibniz. It assigns probabilities in the absence of any evidence, or in the presence of symmetrically balanced evidence. The guiding idea is that in such circumstances, probability is shared equally among all the possible outcomes, so that the classical probability of an event is simply the fraction of the total number of possibilities in which the event occurs. It seems especially well suited to those games of chance that by their very design create such circumstances — for example, the classical probability of a fair die landing with an even number showing up is 3/6. It is often presupposed (usually tacitly) in textbook probability puzzles.

Here is a classic statement by de Moivre:

> [I]f we constitute a fraction whereof the numerator be the number of chances whereby an event may happen, and the denominator the number of all the chances whereby it may either happen or fail, that fraction will be a proper designation of the probability of happening. (1718; 1967, 1–2)

Laplace gives the best-known but slightly different formulation:

> The theory of chances consists in reducing all events of the same kind to a certain number of equally possible cases, that is to say, to cases whose existence we are equally uncertain of, and in determining the number of cases favourable to the event whose probability is sought. The ratio of this number to that of all possible cases is the measure of this probability, which is thus only a fraction whose numerator is the number of favourable cases, and whose denominator is the number of all possible cases. (1814; 1999, 4)

We may ask a number of questions about this formulation. When are events of the same kind? Intuitively, ‘heads’ and ‘tails’ are equally likely outcomes of tossing a fair coin; but if their kind is ‘ways the coin could land’, then ‘edge’ should presumably be counted alongside them. The “certain number of equally possible cases” and “the number of all possible cases” are presumably finite numbers. What, then, of probabilities in infinite spaces? Apparently, irrational-valued probabilities such as $1/\sqrt{2}$ are automatically eliminated, and thus theories such as quantum mechanics that posit them cannot be accommodated. (We will shortly see, however, that Laplace’s theory has been refined to handle infinite spaces.)

Who are “we”, who “are equally uncertain”? Different people may be equally undecided about different things, which suggests that Laplace is offering a subjectivist interpretation in which probabilities vary from person to person depending on contingent differences in their evidence. Yet he means to characterize the objective probability assignment of a rational agent in an epistemically neutral position with respect to a set of “equally possible” cases. But then the proposal risks sounding empty: for what is it for an agent to *be* “equally uncertain” about a set of cases, other than assigning them equal probability?

This brings us to one of the key objections to Laplace’s account. The notion of “equally possible” cases faces the charge of either being a category mistake (for ‘possibility’ does not come in degrees), or circular (for what is meant is really ‘equally probable’). The notion is finessed by the so-called ‘principle of indifference’, a coinage due to Keynes (although he was no friend of the principle): “if there is no known reason for predicating of our subject one rather than another of several alternatives, then relatively to such knowledge the assertions of each of these alternatives have an equal probability” (1921, 52–53). (The ‘principle of equal probability’ would be a better name.) Thus, it might be claimed, there is no circularity in the classical interpretation after all. However, this move may only postpone the problem, for there is still a threat of circularity, albeit at a lower level. We have two cases here: outcomes for which we have *no evidence* (“reason”) *at all*, and outcomes for which we have *symmetrically balanced evidence*. There is no circularity in the first case unless the notion of ‘evidence’ is itself probabilistic; but artificial examples aside, it is doubtful that the case ever arises. For example, we have a considerable fund of evidence on coin tossing from the results of our own experiments, the testimony of others, our knowledge of some of the relevant physics, and so on. In the second case, the threat of circularity is more apparent, for it seems that some sort of *weighing* of the evidence in favor of each outcome is required, and this seems to require a reference to probability. Indeed, the most obvious characterization of symmetrically balanced evidence is in terms of equality of conditional probabilities: given evidence $E$ and possible outcomes $O_1, O_2 , \ldots ,O_n$, the evidence is symmetrically balanced iff $P(O_1\mid E) = P(O_2\mid E) = \ldots = P(O_n\mid E)$. Then it seems that probabilities reside at the base of the interpretation after all. Still, it would be an achievement if all probabilities could be reduced to cases of equal probability. See Zabell (2016)[^zabell-2016] for further discussion of the classical interpretation and the principle of indifference.

When the spaces are countably infinite, the spirit of the classical theory may be upheld by appealing to the information-theoretic principle of *maximum entropy*, a generalization of the principle of indifference championed by Jaynes (1968)[^jaynes-1968]. Entropy is a measure of the lack of ‘informativeness’ of a probability function. The more concentrated is the function, the less is its entropy; the more diffuse it is, the greater is its entropy. For a discrete assignment of probabilities $P = (p_1, p_2,\ldots)$, the entropy of $P$ is defined as:

$$ -\sum_i p_i\log p_i $$

(For more explanation of this formula see the entry on Information.)

The principle of maximum entropy enjoins us to select from the family of all probability functions consistent with our background knowledge the function that maximizes this quantity. In the special case of choosing the most uninformative probability function over a finite set of possible outcomes, this is just the familiar ‘flat’ classical assignment discussed previously. Things get more complicated in the infinite case, since there cannot be a flat assignment over denumerably many outcomes, on pain of violating the standard probability calculus (with countable additivity). Rather, the best we can have are sequences of progressively flatter assignments, none of which is truly flat. We must then impose some *further* constraint that narrows the field to a smaller family in which there *is* an assignment of maximum entropy.[^note-3] This constraint has to be imposed from outside as background knowledge, but there is no general theory of which external constraint should be applied when. See Seidenfeld (1986)[^seidenfeld-1986] for mathematical results regarding maximum entropy and a critique of it.

Let us turn now to uncountably infinite spaces. It is easy — all too easy — to assign equal probabilities to the points in such a space: each gets probability 0. Non-trivial probabilities arise when uncountably many of the points are clumped together in larger sets. If there are finitely many clumps, Laplace’s classical theory may be appealed to again: if the evidence bears symmetrically on these clumps, each gets the same share of probability.

Enter Bertrand’s paradoxes (1889). They all arise in uncountable spaces and turn on alternative parametrizations of a given problem that are non-linearly related to each other. Some presentations are needlessly arcane; length and area suffice to make the point. The following example (adapted from van Fraassen 1989)[^fraassen-1989] nicely illustrates how Bertrand-style paradoxes work. A factory produces cubes with side-length between 0 and 1 foot; what is the probability that a randomly chosen cube has side-length between 0 and 1/2 a foot? The classical intepretation’s answer is apparently 1/2, as we imagine a process of production that is uniformly distributed over side-length. But the question could have been given an equivalent restatement: A factory produces cubes with face-area between 0 and 1 square-feet; what is the probability that a randomly chosen cube has face-area between 0 and 1/4 square-feet? Now the answer is apparently 1/4, as we imagine a process of production that is uniformly distributed over face-area. This is already disastrous, as we cannot allow the same event to have two different probabilities (especially if this interpretation is to be admissible!). But there is worse to come, for the problem could have been restated equivalently again: A factory produces cubes with volume between 0 and 1 cubic feet; what is the probability that a randomly chosen cube has volume between 0 and 1/8 cubic-feet? Now the answer is apparently 1/8, as we imagine a process of production that is uniformly distributed over volume. And so on for all of the infinitely many equivalent reformulations of the problem (in terms of the fourth, fifth, … power of the length, and indeed in terms of every non-zero real-valued exponent of the length). What, then, is *the* probability of the event in question?

The paradox arises because the principle of indifference can be used in incompatible ways. We have no evidence that favors the side-length lying in the interval [0, 1/2] over its lying in [1/2, 1], or vice versa, so the principle requires us to give probability 1/2 to each. Unfortunately, we also have no evidence that favors the face-area lying in any of the four intervals [0, 1/4], [1/4, 1/2], [1/2, 3/4], and [3/4, 1] over any of the others, so we must give probability 1/4 to each. The event ‘the side-length lies in [0, 1/2]’, receives a different probability when merely redescribed. And so it goes, for all the other reformulations of the problem. We cannot meet any pair of these constraints simultaneously, let alone all of them.

Jaynes attempts to save the principle of indifference and to extend the principle of maximum entropy to the continuous case, with his *invariance condition*: in two problems where we have the same knowledge, we should assign the same probabilities. He regards this as a consistency requirement. For any problem, we have a group of admissible transformations, those that change the problem into an equivalent form. Various details are left unspecified in the problem; equivalent formulations of it fill in the details in different ways. Jaynes’ invariance condition bids us to assign equal probabilities to equivalent propositions, reformulations of one another that are arrived at by such admissible transformations of our problem. Any probability assignment that meets this condition is called an *invariant* assignment. Ideally, our problem will have a unique invariant assignment. To be sure, things will not always be ideal; but sometimes they are, in which case this is surely progress on Bertrand-style problems.

And in any case, for many garden-variety problems such technical machinery will not be needed. Suppose I tell you that a prize is behind one of three doors, and you get to choose a door. This seems to be a paradigm case in which the principle of indifference works well: the probability that you choose the right door is 1/3. It seems implausible that we should worry about some reparametrization of the problem that would yield a different answer. To be sure, Bertrand-style problems caution us that there are limits to the principle of indifference. But arguably we must just be careful not to overstate its applicability.

How does the classical theory of probability fare with respect to our criteria of adequacy? Let us begin with admissibility. (Laplacean) classical probabilities obey non-negativity and normalization, but they are only finitely additive (de Finetti 1974). So they do not obey the full Kolmogorov probability calculus, but they provide an interpretation of the elementary theory.

Classical probabilities are ascertainable, assuming that the space of possibilities can be determined in principle. They bear a relationship to the credences of rational agents; the circularity concern, as we saw above, is that the relationship is vacuous, and that rather than *constraining* the credences of a rational agent in an epistemically neutral position, they merely record them.

Without supplementation, the classical theory makes no contact with frequency information. However the coin happens to land in a sequence of trials, the possible outcomes remain the same. Indeed, even if we have strong empirical evidence that the coin is biased towards heads with probability, say, 0.6, it is hard to see how the unadorned classical theory can accommodate this fact — for what now are the ten possibilities, six of which are favorable to heads? Laplace does supplement the theory with his Rule of Succession: “Thus we find that an event having occurred successively any number of times, the probability that it will happen again the next time is equal to this number increased by unity divided by the same number, increased by two units.” (1951, 19) That is:

$$ Pr(\text{success on } N+1^{\text{st}}\text{ trial}\mid N\text{ consec. succeses}) = \frac{N+1}{N+2} $$

Thus, inductive learning is possible — though not by classical probabilities *per se*, but rather thanks to this further rule. And we must ask whether such learning can be captured once and for all by such a simple formula, the same for all domains and events. We will return to this question when we discuss the logical interpretation below.

Science apparently invokes at various points probabilities that look classical. Bose-Einstein statistics, Fermi-Dirac statistics, and Maxwell-Boltzmann statistics each arise by considering the ways in which particles can be assigned to states, and then applying the principle of indifference to different subdivisions of the set of alternatives, Bertrand-style. The trouble is that Bose-Einstein statistics apply to some particles (e.g. photons) and not to others, Fermi-Dirac statistics apply to different particles (e.g. electrons), and Maxwell-Boltzmann statistics do not apply to any known particles. None of this can be determined *a priori*, as the classical interpretation would have it. Moreover, the classical theory purports to yield probability assignments in the face of ignorance. But as Fine (1973)[^fine-1973] writes:

> If we are truly ignorant about a set of alternatives, then we are also ignorant about combinations of alternatives and about subdivisions of alternatives. However, the principle of indifference when applied to alternatives, or their combinations, or their subdivisions, yields different probability assignments (170).

This brings us to one of the chief points of controversy regarding the classical interpretation. Critics accuse the principle of indifference of extracting information from ignorance. Proponents reply that it rather codifies the way in which such ignorance should be epistemically managed — for anything other than an equal assignment of probabilities would represent the possession of some knowledge. Critics counter-reply that in a state of complete ignorance, it is better to assign imprecise probabilities (perhaps ranging over the entire [0, 1] interval), or to eschew the assignment of probabilities altogether.

### 3.2 The Logical/Evidential Interpretation

#### 3.2.1 The logical interpretation

Logical theories of probability retain the classical interpretation’s idea that probabilities can be determined a priori by an examination of the space of possibilities. However, they generalize it in two important ways: the possibilities may be assigned *unequal* weights, and probabilities can be computed whatever the evidence may be, symmetrically balanced or not. Indeed, the logical interpretation, in its various guises, seeks to encapsulate in full generality the degree of support or confirmation that a piece of evidence $e$ confers upon a given hypothesis $h$, which we may write as $c(h, e)$. In doing so, it can be regarded also as generalizing deductive logic and its notion of implication, to a complete theory of inference equipped with the notion of ‘degree of implication’ that relates $e$ to $h$. It is often called the theory of ‘inductive logic’, although this is a misnomer: there is no requirement that $e$ be in any sense ‘inductive’ evidence for $h$. ‘Non-deductive logic’ would be a better name, but this overlooks the fact that deductive logic’s relations of implication and incompatibility are also accommodated as extreme cases in which the confirmation function takes the values 1 and 0 respectively. In any case, it is significant that the logical interpretation provides a framework for induction.

Early proponents of logical probability include Johnson (1921)[^johnson-1921], Keynes (1921)[^keynes-1921], and Jeffreys (1939/1998). However, by far the most systematic study of logical probability was by Carnap. His formulation of logical probability begins with the construction of a formal language. In (1950/1962) he considers a class of very simple languages consisting of a finite number of logically independent monadic predicates (naming properties) applied to countably many individual constants (naming individuals) or variables, and the usual logical connectives. The strongest (consistent) statements that can be made in a given language describe all of the individuals in as much detail as the expressive power of the language allows. They are conjunctions of complete descriptions of each individual, each description itself a conjunction containing exactly one occurrence (negated or unnegated) of each predicate of the language. Call these strongest statements *state descriptions*.

Any probability measure $m(-)$ over the state descriptions automatically extends to a measure over all sentences, since each sentence is equivalent to a disjunction of state descriptions; m in turn induces a confirmation function $c(-, -)$:

$$ c(h,e) = \frac{m(h \amp e)}{m(e)} $$

There are infinitely many candidates for $m$, and hence $c$, even for very simple languages. Carnap argues for his favored measure “$m^*$” by insisting that the only thing that significantly distinguishes individuals from one another is some qualitative difference, not just a difference in labeling. Call a *structure description* a maximal set of state descriptions, each of which can be obtained from another by some permutation of the individual names. $m^*$ assigns each structure description equal measure, which in turn is divided equally among their constituent state descriptions. It gives greater weight to homogenous state descriptions than to heterogeneous ones, thus ‘rewarding’ uniformity among the individuals in accordance with putatively reasonable inductive practice. The induced $c^*$ allows inductive learning from experience.

Consider, for example, a language that has three names, $a$, $b$ and $c$, for individuals, and one predicate $F$. For this language, the state descriptions are:

$$\begin{array}{crcrcr} 1. & Fa &\amp& Fb &\amp& Fc \\ 2. & \neg Fa &\amp& Fb &\amp& Fc \\ 3. & Fa &\amp& \neg Fb &\amp& Fc \\ 4. & Fa &\amp& Fb &\amp& \neg Fc \\ 5. & \neg Fa &\amp& \neg Fb &\amp& Fc \\ 6. & \neg Fa &\amp& Fb &\amp& \neg Fc \\ 7. & Fa &\amp& \neg Fb &\amp& \neg Fc \\ 8. & \neg Fa &\amp& \neg Fb &\amp& \neg Fc \\ \end{array}$$

There are four structure descriptions:

$$\begin{align} \{1\}, &\text{ “Everything is }F\text{”;} \\ \{2, 3, 4\}, &\text{ “Two } F\text{s, one }\neg F\text{”;} \\ \{5, 6, 7\}, &\text{ “One } F\text{, two }\neg F\text{s”; and} \\ \{8\}, &\text{ “Everything is }\neg F\text{”;} \\ \end{align}$$

The measure $m^*$ assigns numbers to the state descriptions as follows: first, every structure description is assigned an equal weight, 1/4; then, each state description belonging to a given structure description is assigned an equal part of the weight assigned to the structure description:

$$\begin{array}{llll} \textit{State description} & \textit{Structure Description} & \textit{Weight} & \quad m^* \\ \left.\begin{array}{l} 1.\ Fa.Fb.Fc \end{array}\right. & \text{I. Everything is } F & 1/4 & \quad 1/4 \\ \left.\begin{array}{l} 2.\ \neg Fa.Fb.Fc\phantom{\neg} \\ 3.\ Fa.\neg Fb.Fc \\ 4.\ Fa.Fb.\neg Fc \end{array} \right\} & \text{II. Two } F\text{s, one }\neg F & 1/4 & \left\{\begin{array}{l} 1/12 \\ 1/12 \\ 1/12 \end{array}\right. \\ \left.\begin{array}{l} 5.\ \neg Fa.\neg Fb.Fc \\ 6.\ \neg Fa.Fb.\neg Fc \\ 7.\ Fa.\neg Fb.\neg Fc \end{array} \right\} & \text{III. One } F\text{, two }\neg F\text{s} & 1/4 & \left\{\begin{array}{l} 1/12 \\ 1/12 \\ 1/12 \end{array}\right. \\ \left.\begin{array}{l} 8.\ \neg Fa.\neg Fb.\neg Fc \end{array}\right. & \text{IV. Everything is } \neg F & 1/4 & \quad 1/4 \end{array}$$

Notice that $m^*$ gives greater weight to the homogenous state descriptions 1 and 8 than to the heterogeneous ones. This will manifest itself in the inductive support that hypotheses can gain from appropriate evidence statements. Consider the hypothesis statement $h = Fc$, true in 4 of the 8 state descriptions, with *a priori* probability $m^*(h) = 1/2$. Suppose we examine individual “$a$” and find it has property $F$ — call this evidence $e$. Intuitively, $e$ is favorable (albeit weak) inductive evidence for $h$. We have: $m^*(h \amp e) = 1/3,$ $m^*(e) = 1/2$, and hence

$$ c^*(h,e) = \frac{m^*(h \amp e)}{m^*(e)} = \frac{2}{3}. $$

This is greater than the *a priori* probability $m^*(h) = 1/2$, so the hypothesis has been confirmed. It can be shown that in general $m^*$ yields a degree of confirmation $c^*$ that allows learning from experience.

Note, however, that infinitely many confirmation functions, defined by suitable choices of the initial measure, allow learning from experience. We do not have yet a reason to think that $c^*$ is the right choice. Carnap claims nevertheless that $c^*$ stands out for being simple and natural.

He later generalizes his confirmation function to a continuum of functions $c_{\lambda}$. Define a *family* of predicates to be a set of predicates such that, for each individual, exactly one member of the set applies, and consider first-order languages containing a finite number of families. Carnap (1963)[^carnap-1963] focuses on the special case of a language containing only one-place predicates. He lays down a host of axioms concerning the confirmation function $c$, including those induced by the probability calculus itself, various axioms of symmetry (for example, that $c(h, e)$ remains unchanged under permutations of individuals, and of predicates of any family), and axioms that guarantee undogmatic inductive learning, and long-run convergence to relative frequencies. They imply that, for a family $\{P_n\},$ $n = 1, \ldots,k$ $(k \gt 2){:}$

$$\begin{align} c_{\lambda}(\text{individual } s+1 \text{ is } P_j,\ s_j \text{ of the first } &s \text{ individuals are }P_j) \\ &= \frac{(s_j + \lambda/k)}{s+ \lambda}, \end{align}$$

where *λ* is a positive real number. The higher the value of *λ*, the less impact evidence has: induction from what is observed becomes progressively more swamped by a classical-style equal assignment to each of the $k$ possibilities regarding individual $s + 1$.

I turn to various objections to Carnap’s program that have been offered in the literature, noting that this remains an area of lively debate. (See Maher (2010)[^maher-2010] for rebuttals of some of these objections and for defenses of the program; see Fitelson (2006)[^fitelson-2006] for an overall assessment of the program.) Firstly, is there a correct setting of *λ*, or said another way, how ‘inductive’ should the confirmation function be? The concern here is that any particular setting of *λ* is arbitrary in a way that compromises Carnap’s claim to be offering a *logical* notion of probability. Also, it turns out that for any such setting, a universal statement in an infinite universe always receives zero confirmation, no matter what the (finite) evidence. Many find this counterintuitive, since laws of nature with infinitely many instances can apparently be confirmed. Earman (1992)[^earman-1992] discusses the prospects for avoiding the unwelcome result.

Significantly, Carnap’s various axioms of symmetry are hardly logical truths. Moreover, Fine (1973, 202)[^fine-1973] argues that we cannot impose further symmetry constraints that are seemingly just as plausible as Carnap’s, on pain of inconsistency. Goodman (1955)[^goodman-1955] taught us: that the future will resemble the past in some respect is trivial; that it will resemble the past in all respects is contradictory. And we may continue: that a probability assignment can be made to respect some symmetry is trivial; that one can be made to respect all symmetries is contradictory. This threatens the whole program of logical probability.

Another Goodmanian lesson is that inductive logic must be sensitive to the meanings of predicates, strongly suggesting that a purely syntactic approach such as Carnap’s is doomed. Scott and Krauss (1966) use model theory in their formulation of logical probability for richer and more realistic languages than Carnap’s. Still, finding a canonical language seems to many to be a pipe dream, at least if we want to analyze the “logical probability” of any argument of real interest — either in science, or in everyday life.

Logical probabilities are admissible. It is easily shown that they satisfy finite additivity, and given that they are defined on finite sets of sentences, the extension to countable additivity is trivial. Given a choice of language, the values of a given confirmation function are ascertainable; thus, if this language is rich enough for a given application, the relevant probabilities are ascertainable. The whole point of the theory of logical probability is to explicate ampliative inference, although given the apparent arbitrariness in the choice of language and in the setting of *λ* — thus, in the choice of confirmation function — one may wonder how well it achieves this. The problem of arbitrariness of the confirmation function also hampers the extent to which the logical interpretation can truly illuminate the connection between probabilities and frequencies.

The arbitrariness problem, moreover, stymies any compelling connection between logical probabilities and rational credences. And a further problem remains even after the confirmation function has been chosen: if one’s credences are to be based on logical probabilities, they must be relativized to an evidence statement, $e$. Carnap requires that $e$ be one’s *total evidence*—the maximally specific information at one’s disposal, the strongest proposition of which one is certain. But perhaps learning does not come in the form of such ‘bedrock’ propositions, as Jeffrey (1992)[^jeffrey-1992] has argued — maybe it rather involves a shift in one’s subjective probabilities across a partition, without any cell of the partition becoming certain. Then it may be that the strongest proposition of which one is certain is expressed by a tautology $T$ — hardly an interesting notion of ‘total evidence’.[^note-4]

In connection with the ‘applicability to science’ criterion, a point due to Lakatos is telling. By Carnap’s lights, the degree of confirmation of a hypothesis depends on the language in which the hypothesis is stated and over which the confirmation function is defined. But scientific progress often brings with it a change in scientific language (for example, the addition of new predicates and the deletion of old ones), and such a change will bring with it a change in the corresponding $c$-values. Thus, the growth of science may overthrow any particular confirmation theory. There is something of the snake eating its own tail here, since logical probability was supposed to explicate the confirmation of scientific theories.

We have seen that the later Carnap relaxed his earlier aspiration to find a *unique* confirmation function, allowing a continuum of such functions displaying a wide range of inductive cautiousness. Various critics of logical probabilities believe that he did not go far enough — that even his later systems constrain inductive learning beyond what is rationally required. This recalls the classic debate earlier in the 20ᵗʰ century between Keynes, a famous proponent of logical probabilities, and Ramsey, an equally famous opponent. Ramsey (1926; 1990)[^ramsey-1926] was skeptical of there being any non-trivial relations of logical probability: he said that he could not discern them himself, and that others disagree about them. This skepticism led him to formulate his enormously influential version of the subjective interpretation of probability, to be discussed shortly.

#### 3.2.2 The evidential interpretation

One might insist, however, that there are non-trivial probabilistic *evidential* relations, even if they are not logical. It may not be a matter of *logic* that the sun will probably rise tomorrow, given our evidence, yet there still seems to be an objective sense in which it probably will, given our evidence. In a crime investigation, there may be a fact of the matter of how strongly the available evidence supports the guilt of various suspects. This does not seem to be a matter of logic—nor of physics, nor of what anyone happens to think, nor of how the facts in the actual world turn out. It seems to be a matter, rather, of *evidential* probabilities.

More generally, Timothy Williamson (2000, 209)[^williamson-2000] writes:

> Given a scientific hypothesis $h$, we can intelligibly ask: how probable is $h$ on present evidence? We are asking how much the evidence tells for or against the hypothesis. We are not asking what objective physical chance or frequency of truth $h$ has. A proposed law of nature may be quite improbable on present evidence even though its objective chance of truth is 1. That is quite consistent with the obvious point that the evidence bearing on $h$ may include evidence about objective chances or frequencies. Equally, in asking how probable $h$ is on present evidence, we are not asking about anyone’s actual degree of belief in $h$. Present evidence may tell strongly against $h$, even though everyone is irrationally certain of $h$.

Williamson identifies one’s evidence with what one knows. However, one might adopt other conceptions of evidence, and one might even take evidential probabilities to link any two propositions whatsoever. Williamson maintains that evidential probabilities are not logical—in particular, they are not syntactically definable. He assumes an initial probability distribution $P$, which “measures something like the intrinsic plausibility of hypotheses prior to investigation” (211). The evidential probability of $h$ on total evidence $e$ is then given by $P(h\mid e)$.

Are evidential probabilities admissible? Williamson says that “P will be assumed to satisfy a standard set of axioms for the probability calculus” (211). So admissibility is built into the very specification of P. Are they ascertainable? He writes:

> What, then, are probabilities on evidence? We should resist demands for an operational definition; such demands are as damaging in the philosophy of science as they are in science itself. Sometimes the best policy is to go ahead and theorize with a vague but powerful notion. One’s original intuitive understanding becomes refined as a result, although rarely to the point of a definition in precise pretheoretic terms. That policy will be pursued here. (211)

This might be understood as rejecting ascertainability as a criterion of adequacy.

However, some authors are skeptical that there are such things as evidential probabilities—e.g. Joyce (2004)[^joyce-2004]. He also argues that there is more than one sense in which evidence tells for or against a hypothesis. Bacon (2014)[^bacon-2014] allows that there are such things as evidential probabilities, but he argues that various puzzling results follow from Williamson’s account of them, in virtue of its identifying evidence with knowledge. Moreover, one may resist demands for an *operational* definition of evidential probabilities, while seeking some further understanding of them in terms of other theoretical concepts. For example, perhaps $P(h\mid e)$ is the subjective probability that a perfectly rational agent with evidence $e$ would assign to $h$? Williamson argues against this proposal; Eder (2023)[^eder-2023] defends it, and she offers several ways of interpreting evidential probabilities in terms of ideal subjective probabilities. If some such way is tenable, evidential probabilities would presumably enjoy whatever applicability that such subjective probabilities have. This brings us to our next interpretation of probability.

### 3.3 The Subjective Interpretation

#### 3.3.1 Probability as degree of belief

Nearly a century before Ramsey, De Morgan wrote: “By degree of probability, we really mean, or ought to mean, degree of belief” (1847, 172). According to the *subjective* (or *personalist* or *Bayesian*) interpretation, probabilities are degrees of confidence, or credences, or partial beliefs of suitable agents. Thus, we really have *many* interpretations of probability here— as many as there are suitable agents. What makes an agent suitable? What we might call *unconstrained subjectivism* places no constraints on the agents — anyone goes, and hence anything goes. Various studies by psychologists are taken to show that people commonly violate the usual probability calculus in spectacular ways. (See, e.g., several articles in Kahneman et al. 1982.)[^kahneman-1982] We clearly do not have here an admissible interpretation (with respect to any probability calculus), since there is no limit to what degrees of confidence agents might have.

More promising, however, is the thought that the suitable agents must be, in a strong sense, *rational*. Following Ramsey, various subjectivists have wanted to assimilate probability to logic by portraying probability as “the logic of partial belief” (1926; 1990, 53 and 55). A rational agent is required to be logically consistent, now taken in a broad sense. These subjectivists argue that this implies that the agent obeys the axioms of probability (although perhaps with only finite additivity), and that subjectivism is thus (to this extent) admissible. Before we can present this argument, we must say more about what degrees of belief are.

#### 3.3.2 The betting analysis and the Dutch Book argument

Subjective probabilities have long been analyzed in terms of betting behavior. Here is a classic statement by de Finetti (1980):

> Let us suppose that an individual is obliged to evaluate the rate $p$ at which he would be ready to exchange the possession of an arbitrary sum $S$ (positive or negative) dependent on the occurrence of a given event $E$, for the possession of the sum $pS$; we will say by definition that this number $p$ is the measure of the degree of probability attributed by the individual considered to the event $E$, or, more simply, that $p$ is the probability of $E$ (according to the individual considered; this specification can be implicit if there is no ambiguity). (62)

This boils down to the following analysis:

> Your degree of belief in $E$ is $p$ iff $p$ units of utility is the price at which you would buy or sell a bet that pays 1 unit of utility if $E$, 0 if not $E$.

The analysis presupposes that, for any $E$, there is exactly one such price — let’s call this your *fair price* for the bet on $E$. This presupposition may fail. There may be no such price — you may refuse to bet on $E$ at all (perhaps unless coerced, in which case your genuine opinion about $E$ may not be revealed), or your selling price may differ from your buying price, as may occur if your probability for $E$ is imprecise. There may be more than one fair price — you may find a range of such prices acceptable, as may also occur if your probability for $E$ is imprecise. For now, however, let us waive these concerns, and turn to an important argument that uses the betting analysis purportedly to show that rational degrees of belief must conform to the probability calculus (with at least finite additivity).

A *Dutch book* is a series of bets bought and sold at prices that collectively guarantee loss, however the world turns out. Suppose we identify your credences with your betting prices. Ramsey notes, and it can be easily proven (e.g., Skyrms 1984)[^skyrms-1984], that if your credences violate the probability calculus, then you are susceptible to a Dutch book—this is the *Dutch Book Theorem*. For example, suppose that you violate the additivity axiom by assigning $P(A \cup B) \lt P(A) + P(B)$, where $A$ and $B$ are mutually exclusive. Then a cunning bettor could buy from you a bet on $A \cup B$ for $P(A \cup B)$ units, and sell you bets on $A$ and $B$ individually for $P(A)$ and $P(B)$ units respectively. He pockets an initial profit of $P(A) + P(B) - P(A \cup B)$, and retains it whatever happens. Ramsey offers the following influential gloss: “If anyone’s mental condition violated these laws [of the probability calculus], his choice would depend on the precise form in which the options were offered him, which would be absurd.” (1990, 78) The Dutch Book argument concludes: rationality requires your credences to obey the probability calculus.

The argument is incomplete as it stands. As Hájek (2008, 2009b)[^hájek-2008][^hájek-2009b] observes, the Dutch Book Theorem leaves open the possibility that you are susceptible to a Dutch Book whether or not your credences violate the probability calculus—perhaps we are all susceptible? Equally important, and often neglected, is the converse theorem that establishes how you can avoid such a predicament. If your subjective probabilities conform to the probability calculus, then no Dutch book can be made against you (Kemeny 1955)[^kemeny-1955]; your probability assignments are then said to be *coherent*. Williamson (1999)[^williamson-1999] extends the Dutch Book argument to countable additivity: if your credences violate countable additivity, then you are susceptible to a Dutch book (with infinitely many bets). Conformity to the full probability calculus thus seems to be necessary and sufficient for coherence.[^note-5] We thus have an argument that rational credences provide an interpretation of the full probability calculus, and thus an admissible interpretation. Note, however, that de Finetti—the arch subjectivist and proponent of the Dutch Book argument—was an opponent of countable additivity (e.g. in his 1974). See Hájek (2009b)[^hájek-2009b], Pettigrew (2020)[^pettigrew-2020] and the entry on Dutch Book arguments for various objections to Dutch Book arguments for conformity to the probability calculus and for other putative norms on credences.

But let us return to the betting analysis of credences. It is an attempt to make good on Ramsey’s idea that probability “is a measurement of belief *qua* basis of action” (67). While he regards the method of measuring an agent’s credences by her betting behavior as “fundamentally sound” (68), he recognizes that it has its limitations.

The betting analysis gives an operational definition of subjective probability, and indeed it inherits some of the difficulties of operationalism in general, and of behaviorism in particular. For example, you may have reason to misrepresent your true opinion, or to feign having opinions that in fact you lack, by making the relevant bets (perhaps to exploit an incoherence in someone else’s betting prices). Moreover, as Ramsey points out, placing the very bet may alter your state of opinion. Trivially, it does so regarding matters involving the bet itself (e.g., you suddenly increase your probability that you have just placed a bet). Less trivially, placing the bet may change the world, and hence your opinions, in other ways. For example, betting at high stakes on the proposition ‘I will sleep well tonight’ may suddenly turn you into an insomniac! And then the bet may concern an event such that, were it to occur, you would no longer value the pay-off the same way. (During the August 11, 1999 solar eclipse in the UK, a man placed a bet that would have paid a million pounds if the world came to an end.)

These problems stem largely from taking literally the notion of entering into a bet on $E$, with its corresponding payoffs. The problems may be avoided by identifying your degree of belief in a proposition with the betting price you regard as fair, whether or not you enter into such a bet; it corresponds to the betting odds that you believe confer no advantage or disadvantage to either side of the bet (Howson and Urbach 1993)[^howson-1993]. At your fair price, you should be indifferent between taking either side.[^note-6]

De Finetti speaks of “an arbitrary sum” as the prize of the bet on $E$. The sum had better be potentially infinitely divisible, or else probability measurements will be precise only up to the level of ‘grain’ of the potential prizes. For example, a sum that can be divided into only 100 parts will leave probability measurements imprecise beyond the second decimal place, conflating probabilities that should be distinguished (e.g., those of a logical contradiction and of ‘a fair coin lands heads 8 times in a row’). More significantly, if utility is not a linear function of such sums, then the size of the prize will make a difference to the putative probability: winning a dollar means more to a pauper more than it does to Bill Gates, and this may be reflected in their betting behaviors in ways that have nothing to do with their genuine probability assignments. De Finetti responds to this problem by suggesting that the prizes be kept small; that, however, only creates the opposite problem that agents may be reluctant to bother about trifles, as Ramsey points out.

Better, then, to let the prizes be measured in utilities: after all, utility is infinitely divisible, and utility is a linear function of utility. While we’re at it, we should adopt a more liberal notion of betting. After all, there is a sense in which every decision is a bet, as Ramsey observed.

#### 3.3.3 Probabilities and utilities

Utilities (desirabilities) of outcomes, their probabilities, and rational preferences are all intimately linked. The *Port Royal Logic* (Arnauld, 1662)[^arnauld-1662] showed how utilities and probabilities together determine rational preferences; de Finetti’s betting analysis derives probabilities from utilities and rational preferences; von Neumann and Morgenstern (1944) derive utilities from probabilities and rational preferences. And most remarkably, Ramsey (1926)[^ramsey-1926] (and later, Savage 1954 and Jeffrey 1966)[^savage-1954] derives *both* probabilities *and* utilities from rational preferences alone.

First, he defines a proposition to be *ethically neutral* — relative to an agent — if the agent is indifferent between the proposition’s truth and falsehood. The agent doesn’t care about the ethically neutral proposition as such — it may be a means to an end that he might care about, but it has no intrinsic value. (The result of a coin toss is typically like this for most of us.) Now, there is a simple test for determining whether, for a given agent, an ethically neutral proposition $N$ has probability 1/2. Suppose that the agent prefers $A$ to $B$. Then $N$ has probability 1/2 iff the agent is indifferent between the gambles:

$$\begin{align} & A \text{ if } N, B \text{ if not } \\ & B \text{ if } N, A \text{ if not}. \\ \end{align}$$

Ramsey assumes that it does not matter what the candidates for $A$ and $B$ are. We may assign arbitrarily to $A$ and $B$ any two real numbers $u(A)$ and $u(B)$ such that $u(A) \gt u(B)$, thought of as the desirabilities of $A$ and $B$ respectively. Having done this for the one arbitrarily chosen pair $A$ and $B$, the utilities of all other propositions are determined.

Given various assumptions about the richness of the preference space, and certain ‘consistency assumptions’, he can define a real-valued utility function of the outcomes $A, B$, etc — in fact, various such functions will represent the agent’s preferences. He is then able to define equality of differences in utility for any outcomes over which the agent has preferences. It turns out that ratios of utility-differences are invariant — the same whichever representative utility function we choose. This fact allows Ramsey to define degrees of belief as ratios of such differences. For example, suppose the agent is indifferent between $A$, and the gamble “$B$ if $X, C$ otherwise”. Then it follows from considerations of expected utility that her degree of belief in $X, P(X)$, is given by:

$$ P(X) = \frac{u(A) - u(C)}{u(B) - u(C)} $$

Ramsey shows that degrees of belief so derived obey the probability calculus (with finite additivity).

Savage (1954)[^savage-1954] likewise derives probabilities and utilities from preferences among options that are constrained by certain putative ‘consistency’ axioms. For a given set of such preferences, he generates a class of utility functions, each a positive linear transformation of the other (i.e. of the form $U_1 = aU_2 + b$, where $a \gt 0)$, and a unique probability function. Together these are said to ‘represent’ the agent’s preferences, and the result that they do so is called a ‘representation theorem’. Jeffrey (1966) refines Savage’s approach. The result is a theory of decision according to which rational choice maximizes ‘expected utility’, a certain probability-weighted average of utilities. (See Buchak 2016 for more discussion.)[^buchak-2016] Some of the difficulties with the behavioristic betting analysis of degrees of belief can now be resolved by moving to an analysis of degrees of belief that is functionalist in spirit. For example, according to Lewis (1986a, 1994a)[^lewis-1986a][^lewis-1994a], an agent’s credences are represented by the probability function belonging to a utility function/probability function pair that best rationalizes her behavioral dispositions, rationality being given a decision-theoretic analysis. Representation theorems (in one form or another) underpin *representation theorem arguments* that rational agents’ credences obey the probability calculus: their preferences obey the requisite axioms, and thus their credences are representable that way. However, as well as being representable probabilistically, such agents’ credences are representable *non-probabilistically*; why should the probabilistic representation be privileged? See Zynda (2000)[^zynda-2000], Hájek (2008)[^hájek-2008], and Meacham and Weisberg (2011) for this and other objections to representation theorem arguments.

There is a deep issue that underlies all of these accounts of subjective probability. They all presuppose the existence of necessary connections between desire-like states and belief-like states, rendered explicit in the connections between preferences and probabilities. In response, one might insist that such connections are at best contingent, and indeed can be imagined to be absent. Think of an idealized Zen Buddhist monk, devoid of any preferences, who dispassionately surveys the world before him, forming beliefs but no desires. It could be replied that such an agent is not so easily imagined after all — even if the monk does not value worldly goods, he will still prefer some things to others (e.g., truth to falsehood).

Once desires enter the picture, they may also have unwanted consequences. Again, how does one separate an agent’s enjoyment or disdain for gambling from the value she places on the gamble itself? Ironically, a remark that Ramsey makes in his critique of the betting analysis seems apposite here: “The difficulty is like that of separating two different co-operating forces” (1990, 68). See Eriksson and Hájek (2007) for further criticism of preference-based accounts of credence.

The betting analysis makes subjective probabilities ascertainable to the extent that an agent’s betting dispositions are ascertainable. The derivation of them from preferences makes them ascertainable to the extent that his or her preferences are known. However, it is unclear that an agent’s full set of preferences is ascertainable even to himself or herself. Here a lot of weight may need to be placed on the ‘in principle’ qualification in the ascertainability criterion. The expected utility representation makes it virtually analytic that an agent should be guided by probabilities — after all, the probabilities are her own, and they are fed into the formula for expected utility in order to determine what it is rational for her to do. So the applicability to rational decision criterion is clearly met.

#### 3.3.4 Orthodox Bayesianism, and further constraints on rational credences

But do they function as a *good* guide? Here it is useful to distinguish different versions of subjectivism. *Orthodox Bayesians* in the style of de Finetti recognize no rational constraints on subjective probabilities beyond:

1. conformity to the probability calculus, and
2. a rule for updating probabilities in the face of new evidence, known as *conditioning* or *conditionalizing*. An agent with probability function $P_1$, who becomes certain of a piece of evidence $E$ (and nothing stronger), should shift to a new probability function $P_2$ related to $P_1$ by:

$$\tag{Conditioning} P_2(X) = P_1(X \mid E),\text{ provided }P_1(E) \gt 0. $$

This is a permissive epistemology, licensing doxastic states that we would normally call crazy. Thus, you could assign probability 1 to this sentence ruling the universe, while upholding such extreme subjectivism.

Some subjectivists impose the further rationality requirement of *regularity*: anything that is possible (in an appropriate sense) gets assigned positive probability. It is advocated by authors such as Jeffreys (1939/1998), Kemeny (1955)[^kemeny-1955], Edwards et al. (1963), Shimony (1970)[^shimony-1970], and Stalnaker (1970)[^stalnaker-1970]. It is meant to capture a form of open-mindedness and responsiveness to evidence. But then, perhaps unintuitively, someone who assigns probability 0.999 to this sentence ruling the universe can be judged rational, while someone who assigns it probability 0 is judged irrational. See, e.g., Levi (1978)[^levi-1978] for further opposition to regularity.

Probabilistic coherence plays much the same role for degrees of belief that *consistency* plays for ordinary, all-or-nothing beliefs. What an extreme subjectivist, even one who demands regularity, lacks is an analogue of *truth*, some yardstick for distinguishing the ‘veridical’ probability assignments from the rest (such as the 0.999 one above), some way in which probability assignments are answerable to the world. It seems, then, that the subjectivist needs something more.

And various subjectivists offer more. Having isolated the “logic” of partial belief as conformity to the probability calculus, Ramsey goes on to discuss what makes a degree of belief in a proposition *reasonable*. After canvassing several possible answers, he settles upon one that focuses on *habits* of opinion formation — “e.g. the habit of proceeding from the opinion that a toadstool is yellow to the opinion that it is unwholesome” (50). He then asks, for a person with this habit, what probability it would be best for him to have that a given yellow toadstool is unwholesome, and he answers that “it will in general be equal to the proportion of yellow toadstools which are in fact unwholesome” (1990, 91). This resonates with more recent proposals (e.g., van Fraassen 1984, Shimony 1988)[^shimony-1988][^fraassen-1984] for evaluating degrees of belief according to how closely they match the corresponding relative frequencies — in the jargon, how well *calibrated* they are. Since relative frequencies obey the axioms of probability (up to finite additivity), it is thought that rational credences, which strive to track them, should do so also.[^note-7]

However, rational credences may strive to track various things. For example, we are often guided by the opinions of experts. We consult our doctors on medical matters, our weather forecasters on meteorological matters, and so on. Gaifman (1988)[^gaifman-1988] coins the terms “expert assignment” and “expert probability” for a probability assignment that a given agent strives to track: “The mere knowledge of the [expert] assignment will make the agent adopt it as his subjective probability” (193). This idea may be codified as follows:

$$\begin{align} \tag{Expert} &P(A\mid pr(A)=x) = x, \\ &\text{for all } x \text{ where this is defined}. \end{align}$$

where ‘$P$’ is the agent’s subjective probability function, and ‘$pr(A)$’ is the assignment that the agent regards as expert. For example, if you regard the local weather forecaster as an expert on your local weather, and she assigns probability 0.1 to it raining tomorrow, then you may well follow suit:

$$ P(\textit{rain}\mid pr(\textit{rain}) = 0.1) = 0.1 $$

More generally, we might speak of an entire probability function as being such a guide for an agent over a specified set of propositions. Van Fraassen (1989, 198)[^fraassen-1989] gives us this definition: “If $P$ is my personal probability function, then $q$ is an *expert function for me concerning* family $F$ of propositions exactly if $P(A \mid q(A) = x) = x$ for all propositions $A$ in family $F$.”

Let us define a *universal expert function* *for* a given rational agent as one that would guide *all* of that agent’s probability assignments in this way: an expert function for the agent concerning all propositions. van Fraassen (1984, 1995a)[^fraassen-1984][^fraassen-1995a], following Goldstein (1983)[^goldstein-1983], argues that an agent’s *future probability functions* are universal expert functions for that agent. He enshrines this idea in his *Reflection Principle*, where *P* is the agent’s probability and $P_{t}$ is her function at a later time $t$:

$$\begin{align} &P (A \mid P_t(A) = x) = x, \\ &\text{for all } t, A \text{ and } x \text{ for which this is defined.} \end{align}$$

The principle encapsulates a certain demand for ‘diachronic coherence’ imposed by rationality. Van Fraassen defends it with a ‘diachronic’ Dutch Book argument (one that considers bets placed at different times), and by analogizing violations of it to the sort of pragmatic inconsistency that one finds in Moore’s paradox.

We may go still further. There may be universal expert functions for large classes of rational agents, and perhaps all of them. The *Principle of Direct Probability* regards the *relative frequency* function as a universal expert function for all rational agents; we have already seen the importance that proponents of calibration place on it. Let $A$ be an event-type, and let *relfreq*$(A)$ be the relative frequency of $A$ (in some suitable reference class). Then for any rational agent with probability function $P$, we have (cf. Hacking 1965)[^hacking-1965]:

$$\begin{align} &P(A\mid \textit{relfreq}(A) = x) = x, \\ &\text{for all } A \text{ and for all } x \text{ where this is defined.} \end{align}$$

Lewis (1980)[^lewis-1980] posits a similar expert role for the *objective chance function, ch*, for all rational *initial* credences in his *Principal Principle* (here simplified[^note-8]):

$$\begin{align} &C(A\mid \textit{ch}(A) = x) = x, \\ &\text{for all } A \text{ and for all } x \text{ where this is defined.} \end{align}$$

‘$C$’ denotes the ‘ur’ credence function of an agent at the beginning of enquiry. This is an idealization that ensures that the agent does not have any “inadmissible” evidence that bears on $A$ without bearing on the chance of $A$. For example, a rational agent who somehow knows that a particular coin toss lands heads is surely *not* required to assign

$$ C(\text{heads} \mid \textit{ch}(\text{heads}) = \frac{1}{2}) = \frac{1}{2}. $$

Rather, this conditional probability should be 1, since she has information relevant to the outcome ‘heads’ that trumps its chance. The other expert principles surely need to be suitably qualified – otherwise they face analogous counterexamples. Yet strangely, the Principal Principle is the only expert principle about which concerns about inadmissible evidence have been raised in the literature.

I will say more about relative frequencies and chance shortly.

The ultimate expert, presumably, is the *truth* function — the function that assigns 1 to all the true propositions and 0 to all the false ones. Knowledge of its values should surely trump knowledge of the values assigned by human experts (including one’s future selves), frequencies, or chances. Note that for any putative expert $q$,

$$\begin{align} &P(A\mid q(A) = x \,\cap\, A) = 1, \\ &\text{for all } A \text{ and for all } x \text{ where this is defined.} \end{align}$$

— the truth of $A$ overrides anything the expert might say. So all of the proposed expert probabilities above should really be regarded as defeasible. Joyce (1998)[^joyce-1998] portrays the rational agent as estimating truth values, seeking to minimize a measure of distance between them and her probability assignments—that is, to maximize the *accuracy* of those assignments. Generalizing a theorem of de Finetti’s (1974), he shows that for any measure of distance that satisfies certain intuitive properties, any agent who violates the probability axioms could serve this epistemic goal better by obeying them instead, however the world turns out. In short, non-probabilistic credences are *accuracy-dominated* by probabilistic credences. This provides a “non-pragmatic” argument for probabilism (in contrast to the Dutch Book and representation theorem arguments) for finite domains. Nielsen (2023)[^nielsen-2023] extends a related accuracy argument by Predd et al. (2009), with different conditions on accuracy measures, to arbitrarily large domains.

There are some unifying themes in these putative constraints on subjective probability. An agent’s degrees of belief determine her estimates of certain quantities: the values of bets, or the desirabilities of gambles more generally, or the probability assignments of various ‘experts’ — humans, relative frequencies, objective chances, or truth values. The laws of probability then are claimed to be constraints on these estimates: putative necessary conditions for minimizing her ‘losses’ in a broad sense, be they monetary, or measured by distances from the assignments of these experts.

#### 3.3.5 Objective Bayesianism

We have been gradually adding more and more constraints on rational credences, putatively demanded by rationality. Recall that Carnap first assumed that there was a unique confirmation function, and then relaxed this assumption to allow a plurality of such functions. We now seem to be heading in the opposite direction: starting with the extremely permissive orthodox Bayesianism, we are steadily reducing the class of rationally permissible credence functions. So far the constraints that we have admitted have not been especially *evidence*-driven. *Objective Bayesians* maintain that a rational agent’s credences are largely determined by her evidence.

How large is “largely”? The lines of demarcation are not sharp, and subjective Bayesianism may be regarded as a somewhat indeterminate region on a spectrum of views that morph into objective Bayesianism. At one end lies an extreme form of subjective Bayesianism, according to which rational credences are constrained only by the probability calculus (and updating by conditionalization). At the other of the spectrum lies an extreme form of objective Bayesianism, according to which rational probabilities are constrained to the point of uniqueness by one’s evidence—we may call this *the Uniqueness Thesis*. But both objective Bayesians and subjective Bayesians may adopt less extreme positions, and typically do. For example, Jon Williamson (2010) is an objective Bayesian, but not an extreme one. He adds to the probability calculus the constraints of being calibrated with evidence, and otherwise equivocating between basic outcomes, especially appealing to versions of maximum entropy. As such, his view is a descendant of the classical interpretation and its generalization due to Jaynes.

### 3.4 Frequency Interpretations

Gamblers, actuaries and scientists have long understood that relative frequencies bear an intimate relationship to probabilities. Frequency interpretations posit the most intimate relationship of all: identity. Thus, we might identify the probability of ‘heads’ on a certain coin with the number of heads in a suitable sequence of tosses of the coin, divided by the total number of tosses. A simple version of frequentism, which we will call *finite frequentism*, attaches probabilities to events or attributes in a finite reference class in such a straightforward manner:

> *the probability of an attribute A in a finite reference class B is the relative frequency of actual occurrences of A within B.*

Thus, finite frequentism bears certain structural similarities to the classical interpretation, insofar as it gives equal weight to each member of a set of events, simply counting how many of them are ‘favorable’ as a proportion of the total. The crucial difference, however, is that where the classical interpretation counted all the *possible* outcomes of a given experiment, finite frequentism counts *actual* outcomes. It is thus congenial to those with empiricist scruples. It was developed by Venn (1876)[^venn-1876], who in his discussion of the proportion of births of males and females, concludes: “probability *is* nothing but that proportion” (p. 84, his emphasis).[^note-9]) Finite frequentism is often assumed, tacitly or explicitly, in statistics and in the sciences more generally.

Finite frequentism gives an operational definition of probability, and its problems begin there. For example, just as we want to allow that our thermometers could be ill-calibrated, and could thus give misleading measurements of temperature, so we want to allow that our ‘measurements’ of probabilities via frequencies could be misleading, as when a fair coin lands heads 9 out of 10 times. More than that, it seems to be built into the very notion of probability that such misleading results can arise. Indeed, in many cases, misleading results are guaranteed. Starting with a degenerate case: according to the finite frequentist, a coin that is never tossed, and that thus yields no actual outcomes whatsoever, lacks a probability for heads altogether; yet a coin that is never measured does not thereby lack a diameter. Perhaps even more troubling, a coin that is tossed exactly once yields a relative frequency of heads of either 0 or 1, whatever its bias. Or we can imagine a unique radiocative atom whose probabilities of decaying at various times obey a continuous law (e.g. exponential); yet according to finite frequentism, with probability 1 it decays at the exact time that it *actually* does, for its relative frequency of doing so is 1/1. Famous enough to merit a name of its own, these are instances of the so-called ‘problem of the single case’. In fact, many events are most naturally regarded as not merely unrepeated, but in a strong sense *unrepeatable* — the 2020 presidential election, the final game of the 2019 NBA play-offs, the Civil War, Kennedy’s assassination, certain events in the very early history of the universe, and so on. Nonetheless, it seems natural to think of non-extreme probabilities attaching to some, and perhaps all, of them. Worse still, some cosmologists regard it as a genuinely chancy matter whether our universe is open or closed (apparently certain quantum fluctuations could, in principle, tip it one way or the other), yet whatever it is, it is ‘single-case’ in the strongest possible sense.

The problem of the single case is particularly striking, but we really have a sequence of related problems: ‘the problem of the double case’, ‘the problem of the triple case’ … Every coin that is tossed exactly twice can yield only the relative frequencies 0, 1/2 and 1, whatever its bias… According to actual frequentism, it is an analytic truth that every coin that is tossed an odd number of times is biased. A finite reference class of size $n$, however large $n$ is, can only produce relative frequencies at a certain level of ‘grain’, namely $1/n$. Among other things, this rules out irrational-valued probabilities; yet our best physical theories say otherwise. Furthermore, there is a sense in which any of these problems can be transformed into the problem of the single case. Suppose that we toss a coin a thousand times. We can regard this as a *single* trial of a thousand-tosses-of-the-coin experiment. Yet we do not want to be committed to saying that *that* experiment yields its actual result with probability 1.

The problem of the single case is that the finite frequentist fails to see intermediate probabilities in various places where others do. There is also the converse problem: the frequentist sees intermediate probabilities in various places where others do not. Our world has myriad different entities, with myriad different attributes. We can group them into still more sets of objects, and then ask with which relative frequencies various attributes occur in these sets. Many such relative frequencies will be intermediate; the finite frequentist automatically identifies them with intermediate probabilities. But it would seem that whether or not they are genuine *probabilities*, as opposed to mere tallies, depends on the case at hand. Bare ratios of attributes among sets of disparate objects may lack the sort of modal force that one might expect from probabilities. I belong to the reference class consisting of myself, the Eiffel Tower, the southernmost sandcastle on Santa Monica Beach, and Mt Everest. Two of these four objects are less than 7 feet tall, a relative frequency of 1/2; moreover, we could easily extend this class, preserving this relative frequency (or, equally easily, not). Yet it would be odd to say that my *probability* of being less than 7 feet tall, relative to this reference class, is 1/2, although it is perfectly acceptable (if uninteresting) to say that 1/2 of the objects in the reference class are less than 7 feet tall.

Some frequentists (notably Venn 1876, Reichenbach 1949, and von Mises 1957 among others)[^reichenbach-1949][^venn-1876][^mises-1957], partly in response to some of the problems above, have gone on to consider *infinite* reference classes, identifying probabilities with *limiting* relative frequencies of events or attributes therein. Thus, we require an infinite sequence of trials in order to define such probabilities. But what if the actual world does not provide an infinite sequence of trials of a given experiment? Indeed, that appears to be the norm, and perhaps even the rule. In that case, we are to identify probability with a *hypothetical* or *counterfactual* limiting relative frequency. We are to imagine hypothetical infinite extensions of an actual sequence of trials; probabilities are then what the limiting relative frequencies *would be* if the sequence were so extended. We might thus call this interpretation *hypothetical frequentism*:

> *the probability of an attribute A in a reference class B is the value the limiting relative frequency of occurrences of A within B would be if B were infinite.*

Note that at this point we have left empiricism behind. A modal element has been injected into frequentism with this invocation of a counterfactual; moreover, the counterfactual may involve a radical departure from the way things actually are, one that may even require the breaking of laws of nature. (Think what it would take for the coin in my pocket, which has only been tossed once, to be tossed infinitely many times — never wearing out, and never running short of people willing to toss it!) One may wonder, moreover, whether there is always — or ever — a fact of the matter of what such counterfactual relative frequencies are.

Limiting relative frequencies, we have seen, must be relativized to a sequence of trials. Herein lies another difficulty. Consider an infinite sequence of the results of tossing a coin, as it might be H, T, H, H, H, T, H, T, T, … Suppose for definiteness that the corresponding relative frequency sequence for heads, which begins 1/1, 1/2, 2/3, 3/4, 4/5, 4/6, 5/7, 5/8, 5/9, …, converges to 1/2. By suitably reordering these results, we can make the sequence converge to any value in [0, 1] that we like. (If this is not obvious, consider how the relative frequency of even numbers among positive integers, which intuitively ‘should’ converge to 1/2, can instead be made to converge to 1/4 by reordering the integers with the even numbers in every fourth place, as follows: 1, 3, 5, 2, 7, 9, 11, 4, 13, 15, 17, 6, …) To be sure, there may be something natural about the ordering of the tosses as given — for example, it may be their *temporal* ordering. But there may be more than one natural ordering. Imagine the tosses taking place on a train that shunts backwards and forwards on tracks that are oriented west-east. Then the *spatial* ordering of the results from west to east could look very different. Why should one ordering be privileged over others?

A well-known objection to any version of frequentism is that *relative* frequencies must be *relativised* to a reference class. Consider a probability concerning myself that I care about — say, my probability of living to age 80. I belong to the class of males, the class of non-smokers, the class of philosophy professors who have two vowels in their surname, … Presumably the relative frequency of those who live to age 80 varies across (most of) these reference classes. What, then, is my probability of living to age 80? It seems that there is no single frequentist answer. Instead, there is my probability-qua-male, my probability-qua-non-smoker, my probability-qua-male-non-smoker, and so on. This is an example of the so-called *reference class problem* for frequentism (although it can be argued that analogues of the problem arise for the other interpretations as well[^note-10]). And as we have seen in the previous paragraph, the problem is only compounded for limiting relative frequencies: probabilities must be relativized not merely to a reference class, but to a sequence within the reference class. We might call this the *reference sequence problem.*

The beginnings of a solution to this problem would be to restrict our attention to sequences of a certain kind, those with certain desirable properties. For example, there are sequences for which the limiting relative frequency of a given attribute does not exist; Reichenbach thus excludes such sequences. Von Mises (1957)[^mises-1957] gives us a more thoroughgoing restriction to what he calls *collectives* — hypothetical infinite sequences of attributes (possible outcomes) of specified experiments that meet certain requirements. Call a *place-selection* an effectively specifiable method of selecting indices of members of the sequence, such that the selection or not of the index $i$ depends at most on the first $i - 1$ attributes. Von Mises imposes these axioms:

> *Axiom of Convergence:* the limiting relative frequency of any attribute exists.
>
> *Axiom of Randomness:* the limiting relative frequency of each attribute in a collective *ω* is the same in any infinite subsequence of *ω* which is determined by a place selection.

The probability of an attribute $A$, relative to a collective *ω*, is then defined as the limiting relative frequency of $A$ in *ω*. Note that a constant sequence such as H, H, H, …, in which the limiting relative frequency is the same in *any* infinite subsequence, trivially satisfies the axiom of randomness. This puts some strain on the terminology — offhand, such sequences appear to be as *non*-random as they come — although to be sure it is desirable that probabilities be assigned even in such sequences. Be that as it may, there is a parallel between the role of the axiom of randomness in von Mises’ theory and the principle of maximum entropy in the classical theory: both attempt to capture a certain notion of disorder.

Collectives are abstract mathematical objects that are not empirically instantiated, but that are nonetheless posited by von Mises to explain the stabilities of relative frequencies in the behavior of actual sequences of outcomes of a repeatable random experiment. Church (1940)[^church-1940] renders precise the notion of a place selection as a recursive function. Nevertheless, the reference sequence problem remains: probabilities must always be relativized to a collective, and for a given attribute such as ‘heads’ there are infinitely many. Von Mises embraces this consequence, insisting that the notion of probability only makes sense relative to a collective. In particular, he regards single case probabilities as nonsense: “We can say nothing about the probability of death of an individual even if we know his condition of life and health in detail. The phrase ‘probability of death’, when it refers to a single person, has no meaning at all for us” (11). Some critics believe that rather than solving the problem of the single case, this merely ignores it. And note that von Mises drastically understates the commitments of his theory: by his lights, the phrase ‘probability of death’ also has no meaning at all when it refers to a million people, or a billion, or any finite number — after all, collectives are *infinite*. More generally, it seems that von Mises’ theory has the unwelcome consequence that probability statements never have meaning in the real world, for apparently all sequences of attributes are finite.

Let us see how the frequentist interpretations fare according to our criteria of adequacy. Finite relative frequencies of course satisfy finite additivity. In a finite reference class, only finitely many events can occur, so only finitely many events can have positive relative frequency. In that case, countable additivity is satisfied somewhat trivially: all but finitely many terms in the infinite sum will be 0. Limiting relative frequencies violate countable additivity (de Finetti 1972, §5.22)[^finetti-1972]. Indeed, the domain of definition of limiting relative frequency is not even a field, let alone a sigma field (de Finetti 1972, §5.8)[^finetti-1972]. So such relative frequencies do not provide an admissible interpretation of Kolmogorov’s axioms. Finite frequentism has no trouble meeting the ascertainability criterion, as finite relative frequencies are in principle easily determined. The same cannot be said of limiting relative frequencies. On the contrary, any finite sequence of trials (which, after all, is all we ever see) puts literally no constraint on the limit of an infinite sequence; still less does an *actual* finite sequence put any constraint on the limit of an infinite *hypothetical* sequence, however fast and loose we play with the notion of ‘in principle’ in the ascertainability criterion.

It might seem that the frequentist interpretations resoundingly meet the applicability to frequencies criterion. Finite frequentism meets it all too well, while hypothetical frequentism meets it in the wrong way. If anything, finite frequentism makes the connection between probabilities and frequencies *too* tight, as we have already observed. A fair coin that is tossed a million times is very *unlikely* to land heads *exactly* half the time; one that is tossed a million and one times is even less likely to do so! Facts about finite relative frequencies should serve as evidence, but not *conclusive* evidence, for the relevant probability assignments. Hypothetical frequentism fails to connect probabilities with finite frequencies. It connects them with limiting relative frequencies, of course, but again too tightly: for even in infinite sequences, the two can come apart. (A fair coin could land heads forever, even if it is highly unlikely to do so.) To be sure, science has much interest in finite frequencies, and indeed working with them is much of the business of statistics. Whether it has any interest in highly idealized, hypothetical extensions of actual sequences, and relative frequencies therein, is another matter. The applicability to rational beliefs and to rational decisions go much the same way. Such beliefs and decisions are guided by finite frequency information, but they are *not* guided by information about limits of hypothetical frequencies, since one never has such information. For much more extensive critiques of finite frequentism and hypothetical frequentism, see Hájek (1997)[^hájek-1997] and Hájek (2009) respectively, and La Caze (2016)[^la-2016].

### 3.5 Propensity Interpretations

Like the frequency interpretations, *propensity* interpretations regard probabilities as objective properties of entities in the real world. Probability is thought of as a physical propensity, or disposition, or tendency of a given type of physical situation to yield an outcome of a certain kind, or to yield a long run relative frequency of such an outcome.

While Popper (1957)[^popper-1957] is often credited as being the pioneer of propensity interpretations, we already find the key idea in the writings of Peirce (1910, 79–80): “I am, then, to define the meaning of the statement that the *probability*, that if a die be thrown from a dice box it will turn up a number divisible by three, is one-third. The statement means that the die has a certain ‘would-be’; and to say that the die has a ‘would-be’ is to say that it has a property, quite analogous to any *habit* that a man might have.” A man’s habit is a paradigmatic example of a disposition; according to Peirce the die’s probability of landing 3 or 6 is an analogous disposition. We might think of various habits coming in different degrees, measuring their various strengths. Analogously, the die’s propensities to land various ways measure the strength of its dispositions to do so.

Peirce continues: “Now in order that the full effect of the die’s ‘would-be’ may find expression, it is necessary that the die should undergo an endless series of throws from the dice box”, and he imagines the relative frequency of the event-type in question oscilating from one side of 1/3 to another. This again anticipates Popper’s view. But an important difference is that Peirce regards the propensity as a property of the die itself, whereas Popper attributes the propensity to the entire chance set-up of throwing the die.

Popper (1957)[^popper-1957] is motivated by the desire to make sense of single-case probability attributions that one finds in quantum mechanics—for example ‘the probability that this radium atom decays in 1600 years is 1/2’. He develops the theory further in (1959a). For him, a probability $p$ of an outcome of a certain type is a propensity of a repeatable experiment to produce outcomes of that type with limiting relative frequency $p$. For instance, when we say that a coin has probability 1/2 of landing heads when tossed, we mean that we have a repeatable experimental set-up — the tossing set-up — that has a propensity to produce a sequence of outcomes in which the limiting relative frequency of heads is 1/2. With its heavy reliance on limiting relative frequency, this position risks collapsing into von Mises-style frequentism according to some critics. Giere (1973)[^giere-1973], on the other hand, explicitly allows single-case propensities, with no mention of frequencies: probability is just a propensity of a repeatable experimental set-up to produce sequences of outcomes. This, however, creates the opposite problem to Popper’s: how, then, do we get the desired connection between probabilities and frequencies?

It is thus useful to follow Gillies (2000a, 2016)[^gillies-2000a][^gillies-2016] in distinguishing *long-run* propensity theories and *single-case* propensity theories:

> A long-run propensity theory is one in which propensities are associated with repeatable conditions, and are regarded as propensities to produce in a long series of repetitions of these conditions frequencies which are approximately equal to the probabilities. A single-case propensity theory is one in which propensities are regarded as propensities to produce a particular result on a specific occasion (2000a, 822).

Hacking (1965)[^hacking-1965] and Gillies offer long-run (though not infinitely long-run) propensity theories. Fetzer (1982, 1983)[^fetzer-1982][^fetzer-1983] and Miller (1994)[^miller-1994] offer single-case propensity theories. So does Popper in a later work (1990), in which he regards propensities as “properties of *the whole physical situation* and sometimes of the particular way in which a situation changes” (17). Note that ‘propensities’ are categorically different things depending on which sort of theory we are considering. According to the long-run theories, propensities are tendencies to produce relative frequencies with particular values, but the propensities are not measured by the probability values themselves; according to the single-case theories, the propensities *are* measured by the probability values. According to Popper’s earlier view, for example, a fair die has a propensity — an *extremely strong* tendency — to land ‘3’ with long-run relative frequency 1/6. The small value of 1/6 does *not* measure this tendency. According to Giere, on the other hand, the die has a *weak* tendency to land ‘3’. The value of 1/6 *does* measure this tendency.

It seems that those theories that tie propensities to frequencies do not provide an admissible interpretation of the (full) probability calculus, for the same reasons that relative frequencies do not. It is *prima facie* unclear whether single-case propensity theories obey the probability calculus or not. To be sure, one can *stipulate* that they do so, perhaps using that stipulation as part of the implicit definition of propensities. Still, it remains to be shown that there really are such things — stipulating what a witch is does not suffice to show that witches exist. Indeed, to claim, as Popper does, that an experimental arrangement has a tendency to produce a given limiting relative frequency of a particular outcome, presupposes a kind of stability or uniformity in the workings of that arrangement (for the limit would not exist in a suitably *unstable* arrangement). But this is the sort of ‘uniformity of nature’ presupposition that Hume argued could not be known either *a priori*, or empirically. Now, appeals can be made to limit theorems — so called ‘laws of large numbers’ — whose content is roughly that under suitable conditions, such limiting relative frequencies almost certainly exist, and equal the single case propensities. Still, these theorems make assumptions (e.g., that the trials are independent and identically distributed) whose truth again cannot be known, and must merely be postulated.

Part of the problem here, say critics, is that we do not know enough about what propensities are to adjudicate these issues. There is *some* property of this coin tossing arrangement such that this coin would land heads with a certain long-run frequency, say. But as Hitchcock (2002)[^hitchcock-2002] points out, “calling this property a ‘propensity’ of a certain strength does little to indicate just what this property is.” Said another way, propensity accounts are accused of giving empty accounts of probability, à la Molière’s ‘dormative virtue’ (Sober 2000, 64)[^sober-2000]. Similarly, Gillies objects to single-case propensities on the grounds that statements about them are untestable, and that they are “metaphysical rather than scientific” (825). Some might level the same charge even against long-run propensities, which are supposedly *distinct* *from* the testable relative frequencies.

This suggests that the propensity account has difficulty meeting the applicability to science criterion. Some propensity theorists (e.g., Giere) liken propensities to physical magnitudes such as electrical charge that are the province of science. But Hitchcock observes that the analogy is misleading. We can only determine the general properties of charge — that it comes in two varieties, that like charges repel, and so on — by empirical investigation. What investigation, however, could tell us whether or not propensities are non-negative, normalized and additive? (See also Eagle 2004.)[^eagle-2004]

More promising, perhaps, is the idea that propensities are to play certain theoretical roles, and that these place constraints on the way they must behave, and hence what they could be (in the style of the Ramsey/Lewis/‘Canberra plan’ approach to theoretical terms — see Lewis 1970 or Jackson 2000)[^lewis-1970]. The trouble here is that these roles may pull in opposite directions, *overconstraining* the problem. The first role, according to some, constrains them to obey the probability calculus (with finite additivity); the second role, according to others, constrains them to violate it.

On the one hand, propensities are said to constrain the degrees of belief, or *credences*, of a rational agent. Recall the ‘applicability to rational beliefs’ criterion: an interpretation should clarify the role that probabilities play in constraining the credences of rational agents. One such putative role for propensities is codified by Lewis’s ‘Principal Principle’. (See section 3.3.) The Principal Principle underpins an argument (Lewis 1980)[^lewis-1980] that whatever they are, propensities must obey the usual probability calculus (with finite additivity). After all, it is argued, rational credences, which are guided by them, do.

On the other hand, Humphreys (1985)[^humphreys-1985] gives an influential argument that propensities do *not* obey Kolmogorov’s probability calculus. The idea is that the probability calculus implies *Bayes’ theorem*, which allows us to reverse a conditional probability:

$$ P(A\mid B) = \frac{P(B\mid A) \cdot P(A)}{P(B)} $$

Yet propensities seem to be measures of ‘causal tendencies’, and much as the causal relation is asymmetric, so these propensities supposedly do not reverse. Suppose that we have a test for an illness that occasionally gives false positives and false negatives. A given sick patient may have a (non-trivial) propensity to give a positive test result, but it apparently makes no sense to say that a given positive test result has a (non-trivial) propensity to have come from a sick patient. Thus, we have an argument that whatever they are, propensities must *not* obey the usual probability calculus. ‘Humphreys’ paradox’, as it is known, is really an argument against any formal account of propensities that has as a theorem:

**(∗)**

if the probability of $B$, given $A$ exists, then the probability of $A$, given $B$ exists,

however one understands these conditional probabilities. The argument has prompted Fetzer and Nute (in Fetzer 1981)[^fetzer-1981] to offer a “probabilistic causal calculus” that looks quite different from Kolmogorov’s calculus.[^note-11] But one could respond more conservatively, as Lyon (2014)[^lyon-2014] points out. For example, Rényi’s axiomatization of primitive conditional probabilities does not have (∗) as a theorem, and thus propensities may conform to it despite Humphreys’ argument. Nonetheless, Lyon offers “a more general problem for the propensity interpretation. There are all sorts of pairs of events that have no propensity relations between them, and all three axiom systems—Kolmogorov’s, Popper’s, and Rényi’s—will sometimes force there to be conditional probabilities between them. This is not an argument that there is no alternative axiom system that propensity theorists can adopt, but it is an argument that the three main contenders are not viable” (124).

Or perhaps all this shows that the notion of ‘propensity’ bifurcates: on the one hand, there are propensities that bear an intimate connection to relative frequencies and rational credences, and that obey the usual probability calculus (with finite additivity); on the other hand, there are causal propensities that behave rather differently. In that case, there would be still more interpretations of probability than have previously been recognized.

### 3.6 Best-System Interpretations

Traditionally, philosophers of probability have recognized five leading interpretations of probability—classical, logical, subjectivist, frequentist, and propensity. But recently, so-called *best-system* interpretations of chance have become increasingly popular and important. While they bear some similarities to frequentist accounts, they avoid some of frequentism’s major failings; and while they are sometimes assimilated to propensity accounts, they are really quite distinct. So they deserve separate treatment.

The best-system approach was pioneered by Lewis (1994b)[^lewis-1994b]. His analysis of chance is based on his account of *laws of nature* (1973), which in turn refines an account due to Ramsey (1928/1990). According to Lewis, the laws of nature are the theorems of the *best systematization* of the universe—the *true* theory that best combines the theoretical virtues of *simplicity and* strength. These virtues trade off. It is easy for a theory to be simple but not strong, by saying very little; it is easy for a theory to be strong but not simple, by conjoining lots of disparate facts. The best theory balances simplicity and strength optimally—in short, it is the most economical true theory.

So far, there is no mention of chances. Now, we allow probabilistic theories to enter the competition. We are not yet in a position to speak of such theories as being true. Instead, let us introduce another theoretical virtue: *fit*. The more probable the actual history of the universe is by the lights of the theory, the better it fits that history. Now the theories compete according to how well they combine simplicity, strength, and fit. The theorems of the winning theory are the laws of nature. Some of these laws may be probabilistic. The chances are the probabilities that are determined by these probabilistic laws.

According to Lewis (1986b)[^lewis-1986b], intermediate chances are incompatible with determinism. Loewer (2004)[^loewer-2004] agrees that intermediate *propensities* are incompatible with determinism, understanding those to be essentially *dynamical*: “they specify the degree to which one state has a tendency to cause another” (15). But he argues that *chances* are best understood along Lewisian best-system lines, and that there is no reason to limit them to dynamical chances. In particular, best-system chances may also attach to *initial conditions*: adding to the dynamical laws a probability assignment, or *distribution*, over initial conditions may provide a substantial gain in strength with relatively little cost in simplicity. Science furnishes important examples of deterministic theories with such initial-condition probabilities. Adding the so-called micro-canonical distribution to Newton’s laws (and the assumption that the distant past had low entropy) yields all of statistical mechanics; adding the so-called quantum equilibrium distribution to Bohm’s dynamical laws yields standard quantum mechanics. Indeed, this contact with actual science is one of the selling points of best-system analyses. See Schwarz (2016)[^schwarz-2016] for further selling points.

At first blush, best-systems analyses seem to score well on our criteria of adequacy. They are admissible by definition: chances are determined by probabilistic laws (rather than by those expressed by some other formalism). One could in principle ascertain values of probabilities, since they supervene on what actually happens in the universe (though ‘in principle’ bears a heavy burden). Applicability to frequencies is secured through the role that ‘fit’ plays. Schwarz (2014)[^schwarz-2014] offers a proof of the Principal Principle, which could be taken to undergird the best-systems analyses’ applicability to rational beliefs and rational decisions. And we have just mentioned the interpretation’s applicability to science.

This approach solves, or at least eases, some of frequentism’s problems. Progress can be made on the problem of the single case. The chances of a rare atom decaying in various time intervals may be determined by a more pervasive functional law, in which decay chances are given for a far wider range of atoms by plugging in a range of settings of some other magnitude (e.g., atomic number). And simplicity may militate in favour of this functional law being continuous, so even irrational-valued probabilities may be assigned. Moreover, bare ratios of attributes among sets of disparate objects will not qualify as chances if they are not pervasive enough, for then a theory that assigns them probabilities will lose too much simplicity without sufficient gain in strength.

However, some other problems for frequentism remain, and some new ones emerge, beginning with more basic problems for the Lewisian account of lawhood itself. Some of them are partly a matter of Lewis’s specific formulation. Critics (e.g. van Fraassen 1989)[^fraassen-1989] question the rather nebulous notion of “balancing” simplicity and strength, which are themselves somewhat sketchy. But arguably some technical story (e.g. information-theoretic) could be offered to precisify them. Lewis himself worries that the exchange rate for such balancing may depend partly on our psychology, in which case there is the threat the laws themselves depend on our psychology, an unpalatable idealism about them. But he maintains that this threat is not serious as long as “nature is kind”, and one theory is so robustly the front-runner that it remains so under any reasonable standards for balancing. And again, perhaps technical tools can offer some objectivity here. (See section 4 for a gesture at such tools.)

More telling is the concern that simplicity is language-relative, and indeed that any theory can be given the simplest specification possible: simply abbreviate it as $T$! Lewis replies that a theory’s simplicity must be judged according to its specification in a canonical language, in which all of the predicates correspond to *natural* properties. Thus, ‘green’ may well be eligible, but ‘grue’ surely is not. (See Goodman 1955.)[^goodman-1955] Our abbreviation, then, has to be unpacked in terms of such a language, in which its true complexity will be revealed. But this now involves a substantial metaphysical commitment to a distinction between natural and unnatural properties, one that various empiricists (e.g. van Fraassen 1989)[^fraassen-1989] find objectionable.

Further problems arise with the refinement to handle probabilistic laws. Again, some of them may be due to Lewis’s particular formulation. Elga (2004)[^elga-2004] observes that Lewis’s notion of fit is problematic in various infinite universes—think of an infinite sequence of tosses of a coin. Offhand, it seems that the particular infinite sequence that is actualized will be assigned probability *zero* by any plausible candidate theory that regards the probability of heads as intermediate and the trials as independent. Elga argues, moreover, that there are technical difficulties with addressing this problem with infinitesimal probabilities. However, perhaps we merely need a different understanding of ‘fit’—perhaps understood as ‘typicality’ (Elga), or perhaps one closer to that employed by statisticians with ‘chi-squared’ tests of goodness of fit (Schwarz 2014)[^schwarz-2014].

Hoefer (2007)[^hoefer-2007] modifies Lewis’s best-system account in light of some of these problems. Hoefer understands “best” as “best for us”, covering regularities that are of interest to us, using the language both of science and of daily life, without any special privilege bestowed upon natural properties. Moreover, the “best system” is now one of chances directly, rather than of laws. Thus, there may be chances associated with the punctuality of trains, for example, without any presumption that there are any associated laws. Hoefer follows Elga in understanding ‘fit’ as ‘typicality’. Strength is a matter of the size of the overall domain of the best system’s probability functions. Simplicity is to be understood in terms of elegant unification, and user-friendliness to beings like us. As a result, Hoefer embraces the agent-centric nature of chances in his sense, regarding as essential the credence-guiding role for them that is captured by the Principal Principle. This is how his account meets the ‘applicability to rational beliefs’ criterion.

However, some other problems for Lewis’s account may run deeper, threatening best-system analyses more generally, and symptomatic of the ghost of frequentism that still hovers behind such analyses. One problem for frequentism that we saw strikes at the heart of any attempt to reduce chances to properties of patterns of outcomes. Such outcomes may be highly misleading regarding the true chances, *because of* their probabilistic nature. This is most vivid for events that are single-case by any reasonable typing. Whether or our universe turns out to be open or closed, plausibly that outcome is compatible with any underlying intermediate chance. The point generalizes, however pervasive the probabilistic pattern might be. Plausibly, a coin’s landing 9 heads out of 10 tosses is compatible with any underlying intermediate chance for heads; and so on. The pattern of outcomes that is instantiated may be a poor guide to the true chance. (See Hájek 2009 for further arguments against frequentism that carry over to best-system accounts.)

Another way of putting the concern is that best-system accounts mistake an idealized epistemology of chance for its metaphysics (though see Lewis’ insistence that this is not the case, in his 1994). Such accounts single out three theoretical virtues—and one may wonder why *just* those three—and reifies the probabilities of a theory that displays the virtues to the highest degree. But a probabilistic world may be recalcitrant to even the best theorizing: nature may be unkind.

## 4. Conclusion: Recent Trends, Future Prospects

It should be clear from the foregoing that there is still much work to be done regarding the interpretations of probability. Each interpretation that we have canvassed seems to capture some crucial insight into a concept of it, yet falls short of doing complete justice to this concept. Perhaps the full story about probability is something of a patchwork, with partially overlapping pieces and principles about how they ought to relate. In that sense, the above interpretations might be regarded as complementary, although to be sure each may need some further refinement. My bet, for what it is worth, is that we will retain the distinct notions of physical, logical/evidential, and subjective probability, with a rich tapestry of connections between them.

There are further signs of the rehabilitation of classical and logical probability, and in particular the principle of indifference and the principle of maximum entropy, by authors such as Paris and Vencovská (1997), Maher (2000, 2001)[^maher-2000][^maher-2001], Bartha and Johns (2001), Novack (2010), White (2010)[^white-2010], and Pettigrew (2016)[^pettigrew-2016]. However, Rinard (2014)[^rinard-2014] argues that the principle of indifference leads to incoherence even when imprecise probabilities are allowed. Eva (2019)[^eva-2019] resurrects the principle as a constraint on *comparative* probabilities of the form ‘I am more confident in *p* than in *q*’ or ‘I am equally confident in *p* and *q*’. This, in turn, showcases another recent trend: an increased interest in comparative probabilities.

Relevant here may also be advances in information theory and complexity theory. Information theory uses probabilities to define the information in a particular event, the degree of uncertainty in a random variable, and the mutual information between random variables (Shannon 1948, Shannon & Weaver 1949)[^shannon-1948][^shannon-1949]. This theory has been developed extensively to give accounts of complexity, optimal data compression and encoding (Kolmogorov 1965, Li and Vitanyi 1997, Cover and Thomas 2006; see the entry on information for more details)[^kolmogorov-1965]. It is applied across the sciences, from its natural home in computer science and communication theory, to physics and biology. Interpreting information in these areas goes hand-in-hand with interpreting the underlying probabilities: each concept of probability has a corresponding concept of information. For example, Scarantino (2015)[^scarantino-2015] offers an account of ‘natural information’ in biology that is compatible with either a logical interpretation of probability or objective Bayesian interpretation, while Kraemer (2015)[^kraemer-2015] offers one that rests on a finite frequency interpretation.

Information theory has also proved to be fruitful in the study of randomness (Kolmogorov 1965, Martin-Löf 1966)[^kolmogorov-1965][^martin-löf-1966], which obviously is intimately related to the notion of probability – see Eagle (2016)[^eagle-2016], and the entry on chance versus randomness. Refinements of our understanding of randomness, in turn, should have a bearing on the frequency interpretations (recall von Mises’ appeal to randomness in his definition of a ‘collective’), and on propensity accounts (especially those that make explicit ties to frequencies). Given the apparent connection between propensities and causation adumbrated in Section 3.5, powerful causal modelling methods should also prove fruitful here. More generally, the theory of graphical causal models (also known as Bayesian networks) uses directed acyclic graphs to represent causal relationships in a system. (See Spirtes, Glymour and Scheines 1993, Pearl 2000, Woodward 2003.)[^pearl-2000][^spirtes-1993][^woodward-2003] The graphs and the probabilities of the system’s variables harmonize in accordance with the causal Markov condition, a sophisticated version of Reichenbach’s slogan “no correlation without causation”. (See the entry on causal models for more details.) Thus again, each understanding of probability has a counterpart understanding of causal networks.

Regarding best-system interpretations of chance, I noted that it is somewhat unclear exactly what ‘simplicity’ and ‘strength’ consist in, and exactly how they are to be balanced. Perhaps insights from statistics and computer science may be helpful here: approaches to statistical model selection, and in particular the ‘curve-fitting’ problem, that attempt to characterize simplicity, and its trade-off with strength — e.g., the Akaike Information Criterion (see Forster and Sober 1994)[^forster-1994], the Bayesian Information Criterion (see Kieseppä 2001)[^kieseppä-2001], Minimum Description Length theory (see Rissanen 1999)[^rissanen-1999] and Minimum Message Length theory (see Wallace and Dowe 1999)[^wallace-1999].

Physical probabilities are becoming even more crucial to scientific inquiry. Probabilities are not just used to characterize the support given to scientific theories by evidence; they appear essentially in the content of the theories themselves. This has led to fertile philosophical ground interpreting the probabilities in such theories. For example, quantum mechanics has physical probabilities at the fundamental level. The interpretation of these probabilities is related to the interpretation of the theory itself (see the entry on philosophical issues in quantum theory). Statistical mechanics and evolutionary theory have non-fundamental objective probabilities. Are they genuine chances? How can we account for them? See Strevens (2003)[^strevens-2003] and Lyon (2011)[^lyon-2011] for discussion. However, Schwarz (2018)[^schwarz-2018] argues that these probabilities can and should be left uninterpreted. Loewer (2012, 2020)[^loewer-2012][^loewer-2020] proposes that the Lewisian best system of our world is given by “*the Mentaculus*”—a complete probability map of the universe. This is Albert’s (2000)[^albert-2000] package of:

- the fundamental dynamical laws of statistical mechanics;
- the claim that initially the universe was in a microstate $M(0)$ whose entropy was tiny (“the Past Hypothesis”);
- and a law specifying a uniform probability distribution over the micro-states that realize $M(0).$

Another ongoing debate regarding physical probabilities concerns whether chance is compatible with determinism—see, e.g., Schaffer (2007)[^schaffer-2007], who is an incompatibilist, and Ismael (2009)[^ismael-2009] and Loewer (2020)[^loewer-2020], who are compatibilists. Handfield and Wilson (2014) argue that chance ascriptions are context-sensitive, varying according to the relevant “evidence base”. This captures the thought that in a deterministic universe, there is *some* sense in which all chances are extreme, while doing justice to other compatibilist usages of chance. See Frigg (2016)[^frigg-2016] for an overview of this debate. Relatedly, an important approach to objective probability that has gained popularity involves the so-called *method of arbitrary functions*. Originating with Poincaré (1896)[^poincaré-1896], it is a mathematical technique for determining probability functions for certain systems with chaotic dynamical laws mapping input conditions to outcomes. Roughly speaking, the probabilities for the outcomes are relatively insensitive to the probabilities over the various initial conditions — think of how the probabilities of outcomes of spins of a roulette wheel apparently do not depend on how the wheel is spun, sometimes vigorously, sometimes feebly. See Strevens (2003, 2013)[^strevens-2003][^strevens-2013] for detailed treatments of this approach.

The subjectivist theory of probability is also thriving—indeed, it has been the biggest growth area among all the interpretations, thanks to the burgeoning of formal epistemology in the last couple of decades. For each of the topics that I will briefly mention, I can only cite a few representative works.

Especially since Joyce (1998)[^joyce-1998], *accuracy* arguments for various Bayesian norms have been influential. They include arguments for conditionalization (Greaves and Wallace 2006, Briggs and Pettigrew 2020)[^briggs-2020][^greaves-2006][^pettigrew-2020], the Reflection Principle (Easwaran 2013)[^easwaran-2013], and the Principal Principle (Pettigrew 2016)[^pettigrew-2016]. However, Mahtani (2021) argues that the mathematical theorems that are invoked to support the accuracy approach do not justify probabilism. These lines of research continue to develop. And these norms themselves have received further attention—e.g. Schoenfield (2017) on conditionalization, and Hall (1994, 2004)[^hall-1994][^hall-2004], Ismael (2008)[^ismael-2008], and Briggs (2009)[^briggs-2009] on the Principal Principle.

Yet for some problems, Bayesian modelling seems not to be sufficiently nuanced. A recently flourishing area has concerned modelling an agent’s *self-locating* credences, concerning who she is, or what time it is. The contents of such credences are usually taken to be richer than just propositions (thought of as sets of possible worlds); rather, they are finer-grained propositions (sets of centered worlds — see Lewis 1979)[^lewis-1979]. This in turn has ramifications for updating rules, in particular calling conditionalization into question—see Meacham (2008)[^meacham-2008]. The so-called Sleeping Beauty problem (Elga 2000)[^elga-2000] has generated much discussion in this regard. See Titelbaum (2012) for a comprehensive study and approach to such problems, Titelbaum (2016)[^titelbaum-2016], and the entry on self-locating beliefs for a survey of the literature. These continue to be fertile areas of research.

On the other hand, there is another sense in which Bayesian modelling has been regarded as *too* nuanced. It seems to be psychologically unrealistic to portray *humans* (rather than ideally rational agents) as having degrees of belief that are infinitely precise real numbers. Thus, there have been various attempts to ‘humanize’ Bayesianism, and this line of research is gaining momentum. For example, there has been a flourishing study of imprecise probability and imprecise decision theory, in which credences need not be precise numbers—for example, they could be sets of numbers, or intervals. See http://www.sipta.org/ for up-to-date research in this area. This resonates with recent work on whether imprecise probabilities are rationally required—Hájek and Smithson (2012) and Isaacs, Hájek, and Hawthorne (2022) on the pro side, Schoenfield (2017) on the con side. The debate continues.

Nor is it plausible that humans obey all the theorems of the probability calculus—we are incoherent in all sorts of ways. The last couple of decades have also seen research on degrees of incoherence—measuring the extent of departures from obedience to the probability calculus—including Zynda (1996)[^zynda-1996], Schervish, Seidenfeld and Kadane (2003), De Bona and Staffel (2017, 2018), and Staffel (2019)[^staffel-2019]. Lin (2013)[^lin-2013] sees traditional epistemology’s notion of *belief* as appropriate for humans who fall short of the Bayesian ideal, but who nevertheless may obey various doxastic norms that can be given Bayesian endorsement. He models everyday practical reasoning, with qualitative beliefs and desires, providing a qualitative decision theory and representation theorem. Easwaran (2016)[^easwaran-2016] takes humans to genuinely have all-or-nothing beliefs, but offers an *instrumentalist* justification for representing those beliefs with probabilities.

It also a fact of life that humans *disagree* with each other. How should an agent modify her credences (if at all) when she disagrees on some claim with an *epistemic peer*—someone who has the same evidence as her, and whom she regards as equally good at evaluating that evidence? The literature on this topic is huge (see Kopec and Titelbaum (2016)[^titelbaum-2016] for a survey, and the entry on disagreement), and it connects in important ways with the interpretations of probability. Intuitively, we feel that disagreement with an epistemic peer rationally calls for moving one’s opinion in the direction of theirs, since disagreement with a peer seems to be evidence that one has made a mistake in evaluating one’s initial evidence. As Kelly (2010)[^kelly-2010] argues, this ‘conciliationist’ intuition appears to commit us to the evidential interpretation of probability, with the common evidence bestowing a unique probability on the disputed claim. (See Schoenfield 2014 and Titelbaum 2016 for dissent; for a defense of the Uniqueness Thesis more generally, see Horowitz and Dogramaci 2016.)[^dogramaci-2016][^titelbaum-2016] The intuition also appears to commit us to *probabilistic enkrasia*: the view that our credences are beholden to our attitudes *about* evidential probabilities, in much the same way as the Principal Principle portrays our credences as beholden to our attitudes about chances. (See Christensen 2013 and Elga 2010 for versions of probabilistic enkrasia principles.)[^christensen-2010] Let’s grant that disagreement with a peer about some claim is evidence that one has made a mistake regarding it. This should affect one’s opinion in it only if one’s attitude about the *correct* way to evaluate the evidence constrains one’s attitude about the claim. However, probabilistic enkrasia has been criticised (see Williamson 2014; Lasonen-Aarnio 2015)[^lasonen-aarnio-2015][^williamson-2014].

We thus come back full circle to where we started. The classical and logical/evidential interpretations sought to capture an objective notion of probability that measures evidential support relations. Early proponents of the subjective interpretation gave us a highly permissive notion of rational credences, constrained only by the probability calculus. Less liberal subjectivists added further rationality constraints, with credences beholden to attitudes about physical probabilities, and to evidential probabilities—at an extreme, to the point of uniqueness. The three kinds of concepts of probability that we identified at the outset converge: epistemological, degrees of confidence, and physical. Future research will doubtless explore further the relationships between them—and how they provide guides to life.

### Suggested Further Reading

Kyburg (1970)[^kyburg-1970] contains a vast bibliography of the literature on probability and induction pre-1970. Also useful for references before 1967 is the bibliography for “Probability” in the Macmillan *Encyclopedia of Philosophy*. Earman (1992)[^earman-1992] and Howson and Urbach (1993) have large bibliographies, and give detailed presentations of the Bayesian program. Hájek and Hitchcock (2021 [Other Internet Resources]) has a more recent and extensive annotated bibliography for all the interpretations of probability discussed in this entry. Skyrms (2000)[^skyrms-2000] is an excellent introduction to the philosophy of probability. Von Plato (1994)[^plato-1994] is more technically demanding and more historically oriented, with another extensive bibliography that has references to many landmarks in the development of probability theory in the last century. Fine (1973)[^fine-1973] is still a highly sophisticated survey of and contribution to various foundational issues in probability, with an emphasis on interpretations. More recent philosophical studies of the leading interpretations include Childers (2013)[^childers-2013], Gillies (2000b)[^gillies-2000b], Galavotti (2005)[^galavotti-2005], Huber (2019), and Mellor (2005)[^mellor-2005]. Hájek and Hitchcock (2016) is a collection of original survey articles on philosophical issues related to probability. Section IV includes chapters on most of the major interpretations of probability. It also includes coverage of the history of probability, Kolmogorov’s formalism and alternatives, and applications of probability in science and philosophy. Joyce (2011)[^joyce-2011] is a thorough survey of subjective Bayesianism; Titelbaum (2022) is a wide-ranging and accessible introduction to Bayesian epistemology. Hájek and Lin (2017) canvass various respects of similarity and dissimilarity between Bayesian epistemology and traditional epistemology. Knauff and Spohn (2021) is a comprehensive open access handbook on many topics concerning rationality; the chapter by Hájek and Staffel (2021) elaborates on a number of issues raised in this entry’s discussion of subjective probability. Eagle (2010)[^eagle-2010] is a valuable anthology of many significant papers in the philosophy of probability, with detailed and incisive critical discussions. Billingsley (1995)[^billingsley-1995] and Feller (1968)[^feller-1968] are classic, rather advanced textbooks on the mathematical theory of probability. Ross (2013)[^ross-2013] is less advanced and has lots of examples.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=probability-interpret). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/probability-interpret/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=probability-interpret&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/probability-interpret/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- Bartha, Paul, [Probability](https://philosophy.ubc.ca/wp-content/uploads/sites/19/2019/09/p550wk5.pdf) (in PDF), lectures notes, University of British Columbia.
- Fitelson, Branden, 2008, “[Lecture notes on Probability and Induction](http://fitelson.org/probability/notes.html)”, University of California, Berkeley.
- Hájek, A., and C. Hitchcock, 2021, “[Interpretations of Probability](https://www.oxfordbibliographies.com/display/document/obo-9780195396577/obo-9780195396577-0416.xml)”, *Oxford Bibliographies Online*..
- Pettigrew, Richard and Jonathan Weisberg (eds.), 2019, [*The Open Handbook of Formal Epistemology*](https://jonathanweisberg.org/pdf/open-handbook-of-formal-epistemology.pdf), open access, published by PhilPapers.
- Weisberg, Jonathan, [*Odds and Ends*](https://jonathanweisberg.org/vip/), an open access, open source textbook.

## Related Entries

Carnap, Rudolf | causal models | causation: probabilistic | chance: versus randomness | decision theory | disagreement | Dutch book arguments | epistemology: Bayesian | information | Laplace, Pierre Simon | logic: inductive | Popper, Karl | probability, in medieval and Renaissance philosophy | quantum theory: philosophical issues in | Ramsey, Frank | Reichenbach, Hans | self-locating beliefs | statistics, philosophy of

### Acknowledgments

I thank Branden Fitelson, Matthias Hild, Christopher Hitchcock, Leon Leontyev, Ralph Miles, Wolfgang Schwarz, Teddy Seidenfeld, Glenn Shafer, Elliott Sober, Jeremy Strasser, and Jim Woodward for their many helpful comments, and especially Jim Joyce, who gave me very detailed and incisive feedback.

## Notes（原文脚注）

[^note-1]: Compare: apart from the assignment of ‘true’ to tautologies and ‘false’ to contradictions, deductive logic is silent regarding the assignment of truth values.

[^note-2]: It turns out that the axiomatization that Salmon gives (p. 59) is inconsistent, and thus that by his lights no interpretation could be admissible. His axiom A2 states:

> If “$A$ is a subclass of $B, P(A, B) = 1$” (read this as “the probability of $B$, given $A$, equals 1”).

Let $I$ be the empty class; then for all $B, P(I, B) = 1$. But his A3 states:

> If $B$ and $C$ are mutually exclusive, then $P(A, B \cup C) =$
>    $P(A, B) + P(A, C)$.

Then for any $X, P(I, X \cup \overline{X}) = P(I, X) + P(I, \overline{X}) = 1 + 1 = 2$, which contradicts his normalization axiom A1. Carnap (1950, 341)[^carnap-1950] notes a similar inconsistency in Jeffreys’ (1939) axiomatization. This problem is easily remedied — simply add the qualification in A2 that $A$ is non-empty — but it is instructive. It suggests that we ought not take the admissibility criterion too seriously. After all, Salmon’s subsequent discussion of the merits and demerits of the various interpretations, as judged by the ascertainability and applicability criteria, still stands, and that is where the real interest lies.

[^note-3]: For example, we might specify that our family consists of distributions over the non-negative integers with a given mean, $m$. Then it turns out that the maximum entropy distribution exists, and is geometric:

$$ P(k) = \frac{1}{1+m}\left( \frac{m}{1+m} \right)^k, k=1,2,\ldots $$

However, not just any further constraint will solve the problem. If instead our family consists of distributions over the positive integers with finite mean, then once more there is no distribution that achieves maximum entropy. (Intuitively, the larger the mean, the more diffuse we can make the distribution, and there is no bound on the mean.)

[^note-4]: Indeed, according to the requirement of regularity (to be discussed further in §3.3), one should not be certain of anything stronger than $T$, on pain of irrationality!

[^note-5]: Some authors simply *define* ‘coherence’ as conformity to the probability calculus.

[^note-6]: Still, according to some, the fair price of a bet on $E$ measures the wrong quantity: not your probability that $E$ will be the case, but rather your probability that $E$ will be the case *and* that the prize will be paid, which may be rather less — for example, if $E$ is unverifiable. Perhaps we should say that betting behavior can be used only to measure probabilities of propositions of the form ‘$E$ and it is verified that $E$’. For typical bets, the distinction between ‘$E$’ and ‘$E$ and it is verified that $E$’ will not matter. But if $E$ is unverifiable, then a bet on it cannot be used to elicit the agent’s probability for it. In that case we should think of this objection as showing that the betting interpretation is incomplete.

[^note-7]: Note, however, that some authors find calibration a poor measure for evaluating degrees of belief. One probability function can be better calibrated than another even though the latter uniformly assigns higher probabilities to truths and lower probabilities to falsehoods — see Joyce (1998)[^joyce-1998].

[^note-8]: There are subtleties that I cannot go into here, including the notion of admissibility, the relativity of chances to times, and Lewis’ (1994b) revised version of the Principle.

[^note-9]: Interestingly, Venn has a lengthy and disparaging discussion of “Gradations of Belief” long before they became established in the subjective interpretation. He writes:

> The subjective side of Probability … seems a mere appendage of the objective, and affords in itself no safe ground for a science of inference…. The conception then of the science of Probability as a science of the laws of belief seems to break down at every point. (120–121)

[^note-10]: The reference class problem is analogous to the “total evidence” problem for Carnap, discussed above. Intuitively, the right reference class is determined by all the evidence relevant to my longevity, and it is unclear what is and is not relevant evidence without appeal to probabilities.

[^note-11]: It should be noted that Gillies argues that Humphreys’ paradox does *not* force non-Kolmogorovian propensities on us.

[^albert-2000]: Albert, D., 2000, *Time and Chance*, Cambridge, MA: Harvard University Press.

[^arnauld-1662]: Arnauld, A., 1662, *Logic, or, The Art of Thinking* (“The Port Royal Logic”), tr. J. Dickoff and P. James, Indianapolis: Bobbs-Merrill, 1964.

[^bacon-2014]: Bacon, A., 2014, “Giving Your Knowledge Half A Chance”, *Philosophical Studies*, 171 (2): 373–397.

[^bartha-2001]: Bartha, P. and R. Johns, 2001, “Probability and Symmetry”, *Philosophy of Science*, 68 (Proceedings): S109–S122.

[^bell-1945]: Bell, E. T., 1945, *The Development of Mathematics*, 2nd edition, New York, McGraw-Hill Book Company.

[^bertrand-1889]: Bertrand, J., 1889, *Calcul des Probabilités* [*Calculus of Probabilities*], Paris, France: Gauthier-Villars.

[^billingsley-1995]: Billingsley, P., 1995, *Probability and Measure*, 3rd edition, New York: John Wiley & Sons.

[^briggs-2009]: Briggs, R., 2009, “The Anatomy of the Big Bad Bug”, *Noûs*, 43 (3): 428–449. doi:10.1111/nous.12258

[^briggs-2020]: Briggs, R. A., and R. Pettigrew, 2020, “An Accuracy-Dominance Argument for Conditionalization”, *Noûs* 54 (1): 162–181, doi:10.1111/nous.12258

[^buchak-2016]: Buchak, L., 2016, “Decision Theory”, in Hájek and Hitchcock (eds.) 2016, 789–815.

[^carnap-1950]: Carnap, R., 1950, *Logical Foundations of Probability*, Chicago: University of Chicago Press; 2nd edition, 1962.

[^carnap-1952]: –––, 1952, *The Continuum of Inductive Methods*, Chicago: University of Chicago Press.

[^carnap-1963]: –––, 1963, “Replies and Systematic Expositions”, in *The Philosophy of Rudolf Carnap*, P. A. Schilpp, (ed.), La Salle, IL: Open Court, 859–1013.

[^childers-2013]: Childers, T., 2013, *Philosophy and Probability*, Oxford University Press.

[^christensen-2010]: Christensen, D., 2010, “Rational Reflection”, *Philosophical Perspectives*, 24 (1): 121–140.

[^church-1940]: Church, A., 1940, “On the Concept of a Random Sequence”, *Bulletin of the American Mathematical Society*, 46: 130–135.

[^cover-1991]: Cover, T. M., and J. A. Thomas, 1991, *Elements of Information Theory*, New York: John Wiley & Sons, Inc.

[^cozman-2016]: Cozman, F. G., 2016, “Imprecise and Indeterminate Probabilities”, in Hájek and Hitchcock (eds.) 2016, 296–311.

[^de-2017]: De Bona, G., and J. Staffel, 2017, “Graded Incoherence for Accuracy Firsters”, *Philosophy of Science*, 284 (2): 189–213.

[^de-2018]: –––, 2018, “Why Be (Approximately) Coherent?”, *Analysis*, 78 (3): 405–415.

[^finetti-1937]: de Finetti, B., 1937, “La Prévision: Ses Lois Logiques, Ses Sources Subjectives”, *Annales de l’Institut Henri Poincaré*, 7: 1–68; translated as “Foresight. Its Logical Laws, Its Subjective Sources”, in *Studies in Subjective Probability*, H. E. Kyburg, Jr. and H. E. Smokler (eds.), Robert E. Krieger Publishing Company, 1980, 55–118.

[^finetti-1972]: –––, 1972, *Probability, Induction and Statistics*, New York: Wiley.

[^finetti-1990]: –––, 1990 [1974], *Theory of Probability* (Volume 1), New York: John Wiley & Sons.

[^moivre-1718]: de Moivre, A., 1718/1967, *The Doctrine of Chances: or, A Method of Calculating the Probability of Events in Play*, London: W. Pearson, 1718; 2nd edition, 1738; 3rd edition 1756; reprinted 1967, New York, NY: Chelsea.

[^de-1847]: De Morgan, A., 1847, *Formal Logic, or, The Calculus of Inference, Necessary and Probable*, London: Taylor and Walton.

[^dogramaci-2016]: Dogramaci, S., and S. Horowitz, 2016, “An Argument for Uniqueness about Evidential Support”, *Philosophical Issues* 26 (1): 130–147.

[^eagle-2010]: Eagle, A., 2010, *Philosophy of Probability: Contemporary Readings*, London: Routledge.

[^eagle-2004]: –––, 2004, “Twenty-One Arguments Against Propensity Analyses of Probability”, *Erkenntnis*, 60: 371–416.

[^eagle-2016]: –––, 2016, “Probability and Randomness”, in Hájek and Hitchcock (eds.) 2016, 440–459.

[^eagle-2018]: –––, 2018, “Chance, Determinism, and Unsettledness”, *Philosophical Studies*, 1–22.

[^earman-1992]: Earman, J., 1992, *Bayes or Bust?*, Cambridge, MA: MIT Press.

[^easwaran-2013]: Easwaran, K., 2013, “Expected Accuracy Supports Conditionalization—and Conglomerability and Reflection”, *Philosophy of Science* 80 (1): 119–142.

[^easwaran-2016]: –––, 2016, “Dr. Truthlove or: How I Learned to Stop Worrying and Love Bayesian Probabilities”, *Noûs* 50 (4): 816–853.

[^eder-2023]: Eder A. A.., 2023, “Evidential Probabilities and Credences”, *The British Journal for the Philosophy of Science* 74 (1).

[^edwards-1963]: Edwards, W., H. Lindman, and L. J. Savage, 1963, “Bayesian Statistical Inference for Psychological Research”, *Psychological Review*, 70: 193–242.

[^elga-2000]: Elga, A., 2000, “Self-Locating Belief and the Sleeping Beauty Problem”, *Analysis*, 60 (2): 143–147. Also in Eagle 2010.

[^elga-2004]: –––, 2004, “Infinitesimal Chances and the Laws of Nature”, *Australasian Journal of Philosophy*, 82 (1): 67–76.

[^elga-2013]: –––, 2013, “The Puzzle of the Unmarked Clock and the New Rational Reflection Principle”, *Philosophical Studies* 164 (1): 127–139.

[^eriksson-2007]: Eriksson, L. and A. Hájek, 2007, “What Are Degrees of Belief?”, *Studia Logica* (Special Issue, Formal Epistemology, Branden Fitelson, ed.), 86 (2): 185–215.

[^eva-2019]: Eva, B., 2019, “Principles of Indifference”, *Journal of Philosophy*, 116 (7): 390–411.

[^feller-1968]: Feller, W., 1968, *An Introduction to Probability Theory and Its Applications*, New York: John Wiley & Sons.

[^festa-1993]: Festa, R., 1993, *Optimum Inductive Methods: A Study in Inductive Probability, Bayesian Statistics, and Verisimilitude*, Dordrecht: Kluwer (Synthese Library 232).

[^fetzer-1981]: Fetzer, J. H., 1981, *Scientific Knowledge: Causation, Explanation, and Corroboration* (Boston Studies in the Philosophy of Science, Volume 69), Dordrecht: D. Reidel.

[^fetzer-1982]: –––, 1982, “Probabilistic Explanations”, *PSA: Proceedings of the Biennial Meeting of Philosophy of Science Association*, 2: 194–207.

[^fetzer-1983]: –––, 1983, “Probability and Objectivity in Deterministic and Indeterministic Situations”, *Synthese*, 57: 367–386.

[^fine-1973]: Fine, T., 1973, *Theories of Probability*, Waltham, MA: Academic Press.

[^fine-2016]: –––, 2016, “Mathematical Alternatives to Standard Probability that Provide Selectable Degrees of Precision”, in Hájek and Hitchcock (eds.) 2016, 203–247.

[^fitelson-2006]: Fitelson, B., 2006, “Inductive Logic”, in *The Philosophy of Science: An Encyclopedia* (Volume 1: A–M), S. Sarkar and J. Pfeiffer (eds.), New York: Routledge, 384–394.

[^forster-1994]: Forster, M. and E. Sober, 1994, “How to Tell when Simpler, More Unified, or Less Ad Hoc Theories will Provide More Accurate Predictions”, *The British Journal for the Philosophy of Science*, 45: 1–35.

[^franklin-2001]: Franklin, J., 2001, *The Science of Conjecture: Evidence and Probability Before Pascal*, Baltimore: Johns Hopkins University Press.

[^frigg-2016]: Frigg, R., 2016, “Chance and Determinism”, in Hájek and Hitchcock (eds.) 2016, 460–474.

[^gaifman-1988]: Gaifman, H., 1988, “A Theory of Higher Order Probabilities”, in *Causation, Chance, and Credence*, B. Skyrms and W. L. Harper (eds.), Dordrecht: Kluwer Academic Publishers, 191–219.

[^galavotti-2005]: Galavotti, M. C., 2005, *Philosophical Introduction to Probability*, Stanford: CSLI Publications.

[^giere-1973]: Giere, R. N., 1973, “Objective Single-Case Probabilities and the Foundations of Statistics”, in *Logic, Methodology and Philosophy of Science* (Volume IV), P. Suppes *et al*., (eds.), New York: North-Holland, 467–483. Also in Eagle 2010.

[^gillies-2000a]: Gillies, D., 2000a, “Varieties of Propensity”, *British Journal for the Philosophy of Science*, 51: 807–835.

[^gillies-2000b]: –––, 2000b, *Philosophical Theories of Probability*, London: Routledge.

[^gillies-2016]: –––, 2016, *The Propensity Interpretation*, in Hájek and Hitchcock (eds.) 2016, 406–422.

[^goldstein-1983]: Goldstein, M., 1983, “The Prevision of a Prevision”, *Journal of the American Statistical Association*, 78: 817–819.

[^goodman-1955]: Goodman, N., 1955, *Fact, Fiction, and Forecast*, Cambridge, MA: Harvard University Press; 2nd edition, Indianapolis: Bobbs-Merrill, 1965; 3rd edition Indianapolis: Bobbs-Merrill, 1973; 4th edition, Cambridge, MA: Harvard University Press, 1983.

[^greaves-2006]: Greaves, H., and D. Wallace, 2006, “Justifying Conditionalization: Conditionalization Maximizes Expected Epistemic Utility”, *Mind*, 115 (459): 607–632.

[^hacking-1965]: Hacking, I., 1965, *The Logic of Statistical Inference*, Cambridge: Cambridge University Press.

[^hájek-1997]: Hájek, A., 1997, “‘*Mises Redux’ — Redux*. Fifteen Arguments Against Finite Frequentism”, *Erkenntnis*, 45: 209–227. Also in Eagle 2010.

[^hájek-2003]: –––, 2003 “What Conditional Probability Could Not Be”, *Synthese*, 137 (3): 273–323.

[^hájek-2008]: –––, 2008, “Arguments for—or Against—Probabilism?”, *The British Journal for the Philosophy of Science*, 59: 793–819; reprinted in *Degrees of Belief*, F. Huber and C. Schmidt-Petri (eds.), Dordrecht: Springer, 2009, 229–251.

[^hájek-2009a]: –––, 2009a, “Fifteen Arguments Against Hypothetical Frequentism”, *Erkenntnis*, 70: 211–235. Also in Eagle 2010.

[^hájek-2009b]: –––, 2009b, “Dutch Book Arguments”, in *The Oxford Handbook of Rational and Social Choice*, P. Anand, P. Pattanaik, and C. Puppe (eds.), Oxford: Oxford University Press, 173–195.

[^hájek-2016]: Hájek, A., and C. Hitchcock, (eds.), 2016, *The Oxford Handbook of Probability and Philosophy*, Oxford: Oxford University Press.

[^hájek-2016b]: Hájek, A. and C. Hitchcock, 2016b, “Probability for Everyone—Even Philosophers”, in Hájek, A., and C. Hitchcock (eds.) 2016, pp. 5–30.

[^hájek-2017]: Hájek, A. and H. Lin, 2017, “A Tale of Two Epistemologies”, *Res Philosophica*, 94 (2): 207–232.

[^hájek-2012]: Hájek, A., and M. Smithson, 2012, “Rationality and Indeterminate Probabilities”, *Synthese*, 187 (1): 33–48.

[^hájek-2021]: Hájek, A. and J. Staffel, 2021, “Subjective Probability and Its Dynamics”, in Knauff and Spohn (eds.) 2021.

[^hall-1994]: Hall, N., 1994, “Correcting the Guide to Objective Chance” *Mind*, 103 (412): 505–518.

[^hall-2003]: –––, 2003, “Two Concepts of Causation”, in J. Collins, N. Hall, and L. Paul (eds.), *Counterfactuals and Causation*, Cambridge, MA: MIT Press, 225–276.

[^hall-2004]: –––, 2004, “Two Mistakes About Credence and Chance”, *Australasian Journal of Philosophy*, 82 (1): 93–111.

[^halpern-2003]: Halpern, J., 2003, *Reasoning About Uncertainty*, Cambridge, MA: The MIT Press.

[^handfield-2014]: Handfield, T. and A. Wilson, 2014, “Chance and Context”, in *Chance and Temporal Asymmetry*, A. Wilson (ed.), Oxford: Oxford University Press.

[^hawthorne-2016]: Hawthorne, J., 2016, “A Logic of Comparative Support: Qualitative Conditional Probability Relations Representable by Popper Functions”, in Hájek and Hitchcock (eds.) 2016, 277–295.

[^hintikka-1965]: Hintikka, J., 1965, “A Two-Dimensional Continuum of Inductive Methods”, in *Aspects of Inductive Logic*, J. Hintikka and P. Suppes (eds.), Amsterdam: North-Holland, 113–132.

[^hitchcock-2002]: Hitchcock, C., 2002, “Probability and Chance”, in the *International Encyclopedia of the Social and Behavioral Sciences* (Volume 18), London: Elsevier, 12,089–12,095.

[^hoefer-2007]: Hoefer, C., 2007, “The Third Way on Objective Probability: A Skeptic’s Guide to Objective Chance”, *Mind*, 116 (2): 549–596.

[^howson-1993]: Howson, C. and P. Urbach, 1993, *Scientific Reasoning: The Bayesian Approach*, La Salle, IL: Open Court, 2ⁿᵈ edition.

[^huber-2018]: Huber, F., 2018, *A Logical Introduction to Probability and Induction*, Oxford University Press.

[^humphreys-1985]: Humphreys, P., 1985, “Why Propensities Cannot Be Probabilities”, *Philosophical Review*, 94: 557–70. Also in Eagle 2010.

[^isaacs-2022]: Isaacs, Y., A. Hájek, and J. Hawthorne, 2022, “Non-Measurability, Imprecise Credences, and Imprecise Chances”, *Mind*, 131 (523): 894–918.

[^ismael-2008]: Ismael, J., 2008, “Raid! Dissolving the Big, Bad Bug”, *Noûs*, 42 (2): 292–307.

[^ismael-2009]: –––, 2009, “Probability in Deterministic Physics”, *The Journal of Philosophy*, 106 (2): 89–108.

[^jackson-1997]: Jackson, F., 1997, *From Metaphysics to Ethics: A Defence of Conceptual Analysis*, Oxford: Oxford University Press.

[^jaynes-1968]: Jaynes, E. T., 1968, “Prior Probabilities” *Institute of Electrical and Electronic Engineers Transactions on Systems Science and Cybernetics*, SSC-4: 227–241.

[^jeffrey-1965]: Jeffrey, R., 1965, *The Logic of Decision*, Chicago: University of Chicago Press; 2ⁿᵈ edition, 1983.

[^jeffrey-1992]: –––, 1992, *Probability and the Art of Judgment*, Cambridge: Cambridge University Press.

[^jeffreys-1939]: Jeffreys, H., 1939, *Theory of Probability*; reprinted in Oxford Classics in the Physical Sciences series, Oxford: Oxford University Press, 1998.

[^johnson-1921]: Johnson, W. E., 1921, *Logic*, Cambridge: Cambridge University Press.

[^joyce-1998]: Joyce, J., 1998, “A Nonpragmatic Vindication of Probabilism”, *Philosophy of Science*, 65 (4): 575–603; reprinted in Eagle 2010.

[^joyce-2004]: –––, 2004, “Williamson on Evidence and Knowledge”, *Philosophical Books*, 45 (4): 296–305.

[^joyce-2011]: –––, 2011, “The Development of Subjective Bayesianism”, in Gabbay, D. M., S. Hartmann, and J. Woods (eds), *Handbook of the History of Logic* (Volume 10: *Inductive Logic*), Boston: Elsevier, 415–475.

[^kahneman-1982]: Kahneman, D., P. Slovic, and A. Tversky, (eds.), 1982, *Judgment Under Uncertainty. Heuristics and Biases*, Cambridge: Cambridge University Press.

[^kelly-2010]: Kelly, T., 2010, “Peer Disagreement and Higher Order Evidence”, in In Alvin I. Goldman & Dennis Whitcomb (eds.), *Social Epistemology: Essential Readings*, Oxford: Oxford University Press, pp. 183–217.

[^kemeny-1955]: Kemeny, J., 1955, “Fair Bets and Inductive Probabilities”, *Journal of Symbolic Logic*, 20: 263–273.

[^keynes-1921]: Keynes, J. M., 1921, *A Treatise on Probability*, London: Macmillan and Co.

[^kieseppä-2001]: Kieseppä, I. A., 2001, “Statistical Model Selection Criteria and Bayesianism”, *Philosophy of Science*, 68 (Proceedings): S141-S152.

[^knauff-2021]: Knauff, Markus and Wolfgang Spohn, 2021, (eds.), *Handbook of Rationality*, Cambridge, MA: MIT Press. [[Knauff and Spohn 2021 available online](https://direct.mit.edu/books/oa-edited-volume/5525/The-Handbook-of-Rationality)].

[^kolmogorov-1933]: Kolmogorov, A. N., 1933, *Grundbegriffe der Wahrscheinlichkeitrechnung*, Ergebnisse Der Mathematik; translated as *Foundations of Probability*, New York: Chelsea Publishing Company, 1950.

[^kolmogorov-1965]: –––, 1965, “Three Approaches to the Quantitative Definition of Information”, *Problemy Perdaci Informacii*, 1: 4–7.

[^kopec-2016]: Kopec, M., and M. G. Titelbaum, 2016, “The Uniqueness Thesis”, *Philosophy Compass*, 11 (4): 189–200.

[^kraemer-2015]: Kraemer, D. M, 2015, “Natural Probabilistic Information”, *Synthese*, 192 (9): 2901–2919.

[^kyburg-1970]: Kyburg, H. E., 1970, *Probability and Inductive Logic*, New York: Macmillan.

[^kyburg-1980]: Kyburg, H. E. and Smokler, H. E., (eds.), 1980, *Studies in Subjective Probability*, 2nd edition, Huntington, New York: Robert E. Krieger Publishing Co.

[^la-2016]: La Caze, A., 2016, “Frequentism”, in Hájek and Hitchcock (eds.) 2016, 341–359.

[^laplace-1814]: Laplace, P. S., 1814/1999. *Philosophical Essay of Probabilities*, translated by Andrew Dale, New York: Springer.

[^lasonen-aarnio-2015]: Lasonen-Aarnio, M., 2015, “New Rational Reflection and Internalism about Rationality”, *Oxford Studies in Epistemology*, 5: 145–171.

[^levi-1978]: Levi, I., 1978, “Coherence, Regularity and Conditional Probability”, *Theory and Decision*, 9: 1–15.

[^lewis-1970]: Lewis, D., 1970, “How to Define Theoretical Terms”, *Journal of Philosophy*, 67: 427–446.

[^lewis-1973]: –––, 1973, *Counterfactuals*, Oxford: Blackwell.

[^lewis-1979]: –––, 1979,“Attitudes De Dicto and De Se”, *Philosophical Review*, 88: 513–543.

[^lewis-1980]: –––, 1980, “A Subjectivist’s Guide to Objective Chance”, in Richard C. Jeffrey (ed.) *Studies in Inductive Logic and Probability*, Vol II., Berkeley and Los Angeles: University of California Press; reprinted in Lewis 1986b, 263–294. Also in Eagle 2010.

[^lewis-1986a]: –––, 1986a, “Probabilities of Conditionals and Conditional Probabilities II”, *Philosophical Review*, 95: 581–589.

[^lewis-1986b]: –––, 1986b, *Philosophical Papers: Volume II*, Oxford: Oxford University Press.

[^lewis-1994a]: –––, 1994a, “Reduction of Mind”, in *A Companion to the Philosophy of Mind*, S. Guttenplan (ed.), Oxford: Blackwell, 412–431.

[^lewis-1994b]: –––, 1994b, “Humean Supervenience Debugged”, *Mind*, 103: 473–490.

[^li-1997]: Li, M. and P. Vitányi, 1997, *An Introduction to Kolmogorov Complexity* *and Its Applications*, 2ⁿᵈ ed., New York: Springer.

[^lin-2013]: Lin, Hanti, 2013, “Foundations of Everyday Practical Reasoning”, *Journal of Philosophical Logic*, 42 (6): 831–862.

[^loewer-2004]: Loewer, B., 2004, “David Lewis’s Humean Theory of Objective Chance”, *Philosophy of Science*, 71 (5): 1115–1125. Also in Eagle 2010.

[^loewer-2012]: –––, 2012, “Two Accounts of Laws and Time”, *Philosophical Studies*, 160 (1): 115–137.

[^loewer-2020]: –––, 2020, “The Mentaculus Vision”, in V. Allori (ed.) *Statistical Mechanics and Scientific Explanation: Determinism, Indeterminism, and Laws of Nature*, Singapore: World Scientific, 3–29.

[^lyon-2011]: Lyon, A., 2011, “Deterministic Probability: Neither Chance nor Credence”, *Synthese*, 182 (3): 413–32.

[^lyon-2014]: –––, 2014, “From Kolmogorov, to Popper, to Renyi: There’s No Escaping Humphreys’ Paradox (When Generalized)”, in *Chance and Temporal Asymmetry*, Oxford: Oxford University Press.

[^lyon-2016]: –––, 2016, “Kolmogorov’s Axiomatization and Its Discontents”, in Hájek and Hitchcock (eds.) 2016, 155–166.

[^maher-2000]: Maher, P., 2000, “Probabilities for Two Properties”, *Erkenntnis*, 52: 63–91.

[^maher-2001]: –––, 2001, “Probabilities for Multiple Properties: The Models of Hesse and Carnap and Kemeny”, *Erkenntnis*, 55: 183–216.

[^maher-2010]: –––, 2010, “Explication of Inductive Probability”, *Journal of Philosophical Logic*, 39: 593–616.

[^mahtani-2022]: Mahtani, A., 2022, “Dutch Book and Accuracy Theorems”, *Proceedings of the Aristotelian Society*, 120 (3): 309–327.

[^martin-löf-1966]: Martin-Löf, P., 1966, “The Definition of Random Sequences”, *Information and Control*, 9: 602–619.

[^meacham-2008]: Meacham, C. J. G., 2008, “Sleeping Beauty and the Dynamics of De Se Beliefs”, *Philosophical Studies*, 138 (2): 245–269.

[^meacham-2011]: Meacham, C. J. G., and J. Weisberg, 2011, “Representation Theorems and the Foundations of Decision Theory”, *Australasian Journal of Philosophy*, 89 (4): 641–663.

[^mellor-2005]: Mellor, D. H., 2005, *Probability: A Philosophical Introduction*, London: Routledge.

[^miller-1994]: Miller, D. W., 1994, *Critical Rationalism: A Restatement and Defence*, Lasalle, Il: Open Court.

[^nielsen-2023]: Nielsen, M., 2023, “Accuracy and Probabilism in Infinite Domains”, *Mind*, 132 (526): 402–427.

[^norton-2008]: Norton, J. D., 2008, “Ignorance and Indifference”, *Philosophy of Science*, 75 (1): 45–68.

[^paris-1997]: Paris J. and A. Vencovská, 1997, “In Defence of the Maximum Entropy Inference Process”, *International Journal of Approximate Reasoning*, 17: 77–103.

[^pearl-2000]: Pearl, J., 2000, *Causality*, Cambridge: Cambridge University Press.

[^peirce-1957]: Peirce, C. S., 1957, “Notes on the Doctrine of Chances”, in *Essays in the Philosophy of Science* (The American Heritage Series), Indianapolis and New York: Bobbs-Merrill, 74–84.

[^pettigrew-2014]: Pettigrew, R., 2014, “Accuracy, Risk, and the Principle of Indifference” *Philosophy and Phenomenological Research*, 92 (1): 35–59.

[^pettigrew-2016]: –––, 2016, *Accuracy and the Laws of Credence*, Oxford: Oxford University Press.

[^pettigrew-2020]: –––, 2020, *Dutch Book Arguments* (Elements in Decision Theory and Philosophy), Cambridge: Cambridge University Press.

[^poincaré-1896]: Poincaré, H. 1896, *Calcul des Probabilités*, Paris: Gauthier-Villars.

[^popper-1957]: Popper, K. R., 1957, “The Propensity Interpretation of the Calculus of Probability and the Quantum Theory”, in S. Körner (ed.), *The Colston Papers*, 9: 65–70.

[^popper-1959a]: –––, 1959a, “The Propensity Interpretation of Probability”, *British Journal of the Philosophy of Science*, 10: 25–42. Also in Eagle 2010.

[^popper-1959b]: –––, 1959b, *The Logic of Scientific Discovery*, New York: Basic Books; reprinted, London: Routledge, 1992.

[^popper-1990]: –––, 1990, *A World of Propensities – Two New Views on Causality*, Bristol: Thoemmes.

[^predd-2009]: Predd, J. B., R. Seiringer, E. H. Lieb, D. N. Osherson, H. V. Poor, and S. R. Kulkarni, 2009, “Probabilistic Coherence and Proper Scoring Rules”, *IEEE Transactions on Information Theory*, 55 (10): 4786–4792.

[^ramsey-1926]: Ramsey, F. P., 1926, “Truth and Probability”, in *Foundations of Mathematics and other Essays*, R. B. Braithwaite (ed.), London: Kegan, Paul, Trench, Trubner, & Co., 1931, 156–198; reprinted in *Studies in Subjective Probability*, H. E. Kyburg, Jr. and H. E. Smokler (eds.), 2ⁿᵈ edition, New York: R. E. Krieger Publishing Company, 1980, 23–52; reprinted in *Philosophical Papers*, D. H. Mellor (ed.), Cambridge: Cambridge University Press, 1990, 52–94. Also in Eagle 2010.

[^ramsey-1928]: –––, 1928/1990, “General Propositions and Causality”, *Philosophical Papers*, edited by D. H. Mellor, Cambridge: Cambridge University Press, 145–163.

[^reichenbach-1949]: Reichenbach, H., 1949, *The Theory of Probability*, Berkeley: University of California Press.

[^rényi-1970]: Rényi, A., 1970, *Foundations of Probability*, San Francisco: Holden-Day, Inc.

[^rinard-2014]: Rinard, S., 2014, “The Principle of Indifference and Imprecise Probability”, *Thought*, 3: 110–114.

[^rissanen-1999]: Rissanen, J. 1999, “Hypothesis Selection and Testing by the MDL Principle”, *Computer Journal*, 42 (4): 260–269.

[^roeper-1999]: Roeper, P. and H. Leblanc, 1999, *Probability Theory and Probability Logic*, Toronto: University of Toronto Press.

[^ross-2013]: Ross, S., 2013,*A First Course in Probability*, 9th edition, Upper Saddle River, NJ: Pearson.

[^salmon-1966]: Salmon, W., 1966, *The Foundations of Scientific Inference*, Pittsburgh: University of Pittsburgh Press.

[^savage-1954]: Savage, L. J., 1954, *The Foundations of Statistics*, New York: John Wiley.

[^scarantino-2015]: Scarantino, A., 2015, “Information as a Probabilistic Difference Maker”, *Australasian Journal of Philosophy*, 93 (3): 419–443.

[^schaffer-2007]: Schaffer, J., 2007, “Deterministic Chance?”, *The British Journal for the Philosophy of Science*, 58 (2): 113–140.

[^schervish-2003]: Schervish, M. J., T. Seidenfeld, and J. B. Kadane, 2003, “Measures of Incoherence”, in *Bayesian Statistics* (Volume 7), J.M. Bernardo, et al. (eds.), Oxford: Oxford University Press, 385–402.

[^schoenfield-2017a]: Schoenfield, M., 2017a, “Conditionalization Does Not (in General) Maximize Expected Accuracy”, *Mind*, 126 (504): 1155–1187.

[^schoenfield-2017b]: –––, 2017b, “The Accuracy and Rationality of Imprecise Credences”, *Noûs*, 51 (4): 667–685.

[^schoenfield-2019]: –––, 2019, “Permission to Believe: Why Permissivism Is True and What It Tells Us about Irrelevant Influences on Belief”, in J. Fantl, M. McGrath, and E. Sosa (eds.), *Contemporary Epistemology: An Anthology*, Hoboken: Wiley-Blackwell, 277–295.

[^schwarz-2014]: Schwarz, W., 2014, “Proving the Principal Principle”, in *Chance and Temporal Asymmetry*, A. Wilson (ed.), Oxford: Oxford University Press, 81–99.

[^schwarz-2016]: –––, 2016, “Best System Approaches to Chance”, in Hájek and Hitchock (eds.), 2016, 423–439.

[^schwarz-2018]: –––, 2018, “No Interpretation of Probability”, *Erkenntnis*, 83 (6): 1195–1212.

[^scott-1966]: Scott D., and P. Krauss, 1966, “Assigning Probabilities to Logical Formulas”, in *Aspects of Inductive Logic*, J. Hintikka and P. Suppes (eds.), Amsterdam: North-Holland, 219–264.

[^seidenfeld-1986]: Seidenfeld, T., 1986, “Entropy and Uncertainty”, *Philosophy of Science*, 53: 467–491.

[^shannon-1948]: Shannon, C. E., 1948, “A Mathematical Theory of Communication”, *Bell System Technical Journal*, 27 (3): 379–423.

[^shannon-1949]: Shannon, C. E, and W. Weaver, 1949, *The Mathematical Theory of Communication*, University of Illinois Press.

[^shimony-1970]: Shimony, A., 1970, “Scientific Inference”, in *The Nature and Function of Scientific Theories*, R. Colodny (ed.), Pittsburgh: University of Pittsburgh Press.

[^shimony-1988]: –––, 1988, “An Adamite Derivation of the Calculus of Probability”, in J.H. Fetzer (ed.), *Probability and Causality*, Dordrecht: D. Reidel.

[^skyrms-1980]: Skyrms, B., 1980, *Causal Necessity*, New Haven: Yale University Press.

[^skyrms-1984]: –––, 1984, *Pragmatics and Empiricism*, New Haven: Yale University Press.

[^skyrms-2000]: –––, 2000, *Choice and Chance*, 4ᵗʰ edition, Belmont, CA: Wadsworth, Inc.

[^sober-2000]: Sober, E., 2000, *Philosophy of Biology*, 2ⁿᵈ edition, Boulder, CO: Westview Press.

[^spirtes-1993]: Spirtes, P., C. Glymour, and R. Scheines, 1993, *Causation, Prediction, and Search*, New York: Springer-Verlag.

[^spohn-1986]: Spohn, W., 1986, “The Representation of Popper Measures”, *Topoi*, 5: 69–74.

[^staffel-2019]: Staffel, J., 2019, *Unsettled Thoughts: A Theory of Degrees of Rationality*, Oxford: Oxford University Press.

[^stalnaker-1970]: Stalnaker, R., 1970, “Probabilities and Conditionals”, *Philosophy of Science*, 37: 64–80.

[^stove-1986]: Stove, D. C., 1986, *The Rationality of Induction*, Oxford: Oxford University Press.

[^strevens-2003]: Strevens, M., 2003, *Bigger Than Chaos: Understanding Complexity through Probability*, Cambridge, MA: Harvard University Press.

[^strevens-2013]: –––, 2013, *Tychomancy*, Cambridge, MA: Harvard University Press.

[^titelbaum-2013]: Titelbaum, M. G., 2013, *Quitting Certainties: A Bayesian Framework Modeling Degrees of Belief*, Oxford University Press.

[^titelbaum-2016]: –––, 2016, “Self-Locating Credences”, in Hájek and Hitchcock (eds.) 2016, 666–680.

[^titelbaum-2017]: –––, 2017, “One’s Own Reasoning”, *Inquiry*, 60 (3): 208–232.

[^titelbaum-2017-2]: –––, 2017, *Fundamentals of Bayesian Epistemology* (Volumes 1 and 2), Oxford: Oxford University Press.

[^fraassen-1984]: van Fraassen, B., 1984, “Belief and the Will”, *Journal of Philosophy*, 81: 235–256. Also in Eagle 2010.

[^fraassen-1989]: –––, 1989, *Laws and Symmetry*, Oxford: Clarendon Press.

[^fraassen-1995a]: –––, 1995a, “Belief and the Problem of Ulysses and the Sirens”, *Philosophical Studies*, 77: 7–37.

[^fraassen-1995b]: –––, 1995b, “Fine-grained Opinion, Conditional Probability, and the Logic of Belief”, *Journal of Philosophical Logic*, 24: 349–377.

[^venn-1876]: Venn, J., 1876, *The Logic of Chance*, 2ⁿᵈ edition, London: Macmillan; reprinted, New York: Chelsea Publishing Co., 1962.

[^mises-1957]: von Mises R., 1957, *Probability, Statistics and Truth*, revised English edition, New York: Macmillan.

[^neumann-1944]: von Neumann, J. and O. Morgenstern, 1944, *Theory of Games and Economic Behavior*, Princeton: Princeton University Press; New York: John Wiley and Sons, 1964.

[^plato-1994]: von Plato J., 1994, *Creating Modern Probability*, Cambridge: Cambridge University Press.

[^wallace-1999]: Wallace, C. S. and D. L. Dowe, 1999, “Minimum Message Length and Kolmogorov Complexity”, *Computer Journal* (Special Issue: Kolmogorov Complexity), 42 (4): 270–283.

[^white-2010]: White, R., 2010, “Evidential Symmetry and Mushy Credence”, *Oxford Studies in Epistemology*, 3 (161): 20.

[^williamson-1999]: Williamson, J., 1999, “Countable Additivity and Subjective Probability”, *The British Journal for the Philosophy of Science*, 50 (3): 401–416.

[^williamson-2000]: Williamson, T., 2000, *Knowledge and Its Limits*, Oxford: Oxford University Press.

[^williamson-2014]: –––, 2014, “Very Improbable Knowing”, *Erkenntnis*, 79 (5): 971–999.

[^woodward-2003]: Woodward, J., 2003, *A Theory of Explanation: Causation, Invariance and Intervention*, Oxford: Oxford University Press.

[^zabell-2016]: Zabell, S. 2016, “Symmetry Arguments in Probability”, in Hájek and Hitchcock (eds.) 2016, 315–340.

[^zynda-1996]: Zynda, L., 1996, “Coherence as an Ideal of Rationality”, *Synthese* 109(2): 175–216.

[^zynda-2000]: –––, 2000, “Representation Theorems and Realism about Degrees of Belief”, *Philosophy of Science* 67(1): 45–69.
