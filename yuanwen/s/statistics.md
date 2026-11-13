# Philosophy of Statistics
**First published Tue Aug 19, 2014; substantive revision Wed Oct 1, 2025**

*Romeijn, Jan-Willem*

Statistics investigates and develops specific methods for evaluating hypotheses in the light of empirical facts. A method is called statistical, and thus the subject of study in statistics, if it relates facts and hypotheses of a particular kind: the empirical facts must be codified and structured into data sets, and the hypotheses must be formulated in terms of probability distributions over possible data sets. The philosophy of statistics concerns the foundations and the proper interpretation of statistical methods, their input, and their results. Since statistics is relied upon in almost all empirical scientific research, serving to support and communicate scientific findings, the philosophy of statistics is of key importance to the philosophy of science. It is part of the philosophical appraisal of scientific method, and it impacts the debate over the epistemic and ontological status of scientific theory.

The philosophy of statistics harbors a large variety of topics and debates. Central to these is the problem of induction, which concerns the justification of inferences or procedures that extrapolate from data to predictions and general facts. Further debates concern the interpretation of the probabilities that are used in statistics, and the wider theoretical framework that may ground and justify the correctness of statistical methods. A general introduction to these themes is given in Section 1 and Section 2. Section 3 and Section 4 provide an account of how these themes play out in the two major theories of statistical method, classical and Bayesian statistics respectively. Section 5 directs attention to the notion of a statistical model, covering model selection and simplicity, but also discussing statistical and data-scientific techniques that do not rely on statistical models. Section 6 briefly mentions relations between the philosophy of statistics and several other themes from the philosophy of science, including confirmation theory, evidence, causality, measurement, and scientific methodology in general.

## 1. Statistics and induction

Statistics is a mathematical and conceptual discipline that focuses on the relation between data and hypotheses. The data are recordings of observations or events in a scientific study, e.g., a set of measurements of individuals from a population. The data actually obtained are variously called the sample, the sample data, or simply the data, and all possible samples from a study are collected in what is called a sample space. The hypotheses, in turn, are general statements about the target system of the scientific study, e.g., expressing some general fact about all individuals in the population. A statistical hypothesis is a general statement that can be expressed by a probability distribution over sample space, i.e., it determines a probability for each of the possible samples.

Statistical methods provide the mathematical and conceptual means to evaluate statistical hypotheses in the light of a sample. To this end the methods employ probability theory, and occasionally generalizations thereof. The evaluations may determine how believable a hypothesis is, whether we may rely on the hypothesis in our decisions, how strong the support is that the sample gives to the hypothesis, and so on. Good introductions to statistics abound (e.g., Mood and Graybill 1974, Barnett 1999, Press 2002, Wasserman 2004, Gelman et al. 2013)[^barnett-1999][^gelman-2013][^gelman-2013-2][^mood-1974][^press-2002][^wasserman-2004].

We can set the stage with an example, adapted from Fisher (1935) with a nod to Student’s t-test.

> **The tea tasting student**
> Consider a student who claims that they can, by taste, determine the order in which milk and tea were poured into the cup. Now imagine that we prepare five cups of tea, tossing a fair coin to determine the order of milk and tea in each cup. We ask the student to pronounce the order, and we find that she is correct in all cases! Now if she is guessing the order blindly then, owing to the random way we prepare the cups, she will answer correctly 50% of the time. This is our statistical hypothesis, referred to as the null hypothesis. It gives a probability of $1/2$ to a correct guess and hence a probability of $1/2$ to an incorrect one. The sample space consists of all sequences of answers the student might give, i.e., all sequences of correct and incorrect guesses. But our actual data sits in a rather special corner in this space. On the assumption of our statistical hypothesis, the probability of the recorded events is a mere 3%, or $1/2^{5}$ more precisely. On this ground, we may decide to reject the hypothesis that the student is guessing: the probability of the event of five correct guesses is too low to retain it.

According to the so-called null hypothesis test, such a decision is warranted if the data actually obtained are included in a particular region within sample space, whose total probability does not exceed some specified limit, standardly set at 5%. Now consider what is achieved by the statistical test just outlined. We started with a hypothesis on the actual tea tasting abilities of the student, namely, that she did not have any. On the assumption of this hypothesis, the sample data we obtained appears to be very surprising or, more precisely, highly improbable. This motivated us to reject the hypothesis that the student has no tea tasting abilities whatsoever. The sample thus points us to a negative but general conclusion about what the student can, or cannot, do.

Notably, all individual sequences of correct and incorrect guesses are equally improbable according to the null hypothesis: they all have a probability of $1/2^5$. But when we collect the possible samples in sets that have the same total number of correct guesses, the singleton set of five correct guesses presents itself as an outlier. It contains only one sequence and it is therefore less probable than the set containing all five sequences with a total of four correct guesses, and far less probable than the sets containing two or three correct guesses, which each consist of ten sequences. Marking out the one sample of five correct guesses as the improbable event thus hinges on a specific way of labelling the samples. The function on sample space that determines this labelling is usually the so-called sufficient statistic, i.e., the function that groups sequences that are equiprobable according to the statistical hypotheses under scrutiny.

The basic pattern of a statistical analysis is familiar from inductive inference: we input the data obtained thus far, and the statistical procedure outputs a verdict or evaluation that transcends the data, i.e, a statement that is not entailed by the data alone. If the data are indeed considered to be the only input, and if the statistical procedure is understood as an inference, then statistics is concerned with ampliative inference: roughly speaking, we get out more than we have put in. And since the ampliative inferences of statistics pertain to future or general states of affairs, they are inductive. However, the association of statistics with ampliative and inductive inference is contested, both because statistics is considered to be non-inferential by some (see Section 3) and non-ampliative by others (see Section 4).

Despite such disagreements, it is insightful to view statistics as a response to the problem of induction (cf. Howson 2000 and the entry on the problem of induction)[^howson-2000]. This problem, first discussed by Hume in his *Treatise of Human Nature* (Book I, part 3, section 6) but prefigured already by ancient sceptics like Sextus Empiricus (see the entry on ancient skepticism), is that there is no proper justification for inferences that run from given experience to expectations about the future. Transposed to the context of statistics, it reads that there is no proper justification for procedures that take data as input and that return a verdict, an evaluation, or some other piece of advice that pertains to the future, or to general states of affairs. Arguably, much of the philosophy of statistics is about coping with this challenge, by providing a foundation of the procedures that statistics offers, or else by reinterpreting what statistics delivers so as to evade the challenge.

It is debatable if philosophers of statistics are ultimately concerned with the delicate, somewhat ethereal issue of the justification of induction, and statisticians generally are not. Many philosophers and scientists simply accept the fallibility of statistics, and find it more important that statistical methods are understood and applied correctly. As is so often the case, the fundamental philosophical problem serves as a catalyst: the problem of induction guides our investigations into the workings, the correctness, and the conditions of applicability of statistical methods. The philosophy of statistics, understood as the general header under which these investigations are carried out, is not, or not primarily, concerned with philosophy for its own sake. Rather it presents a concrete contribution to the scientific method, and hence to science itself. Considering the centrality of statistical methods in practically every empirical science and the ongoing debates over their validity, for instance over the reproducibility of experimental findings in social and medical science (Ioannidis 2005)[^ioannidis-2005], this kind of applied philosophical work is of vital importance.

## 2. Foundations and interpretations

While there is large variation in how statistical procedures and inferences are organized, they all agree on the use of modern measure-theoretic probability theory (Kolmogorov 1933)[^kolmogorov-1933], or a near kin, as the means to express hypotheses and relate them to data. By itself, a probability function is simply a particular kind of mathematical function, used to express the size or measure of a set (cf. Billingsley 1995)[^billingsley-1995].

Let $W$ be a set with elements $s$, and consider an initial collection of subsets of $W$, e.g., the singleton sets $\{ s \}$. Now consider the operation of taking the complement $\bar{R}$ of a given set $R$: this complement $\bar{R}$ contains exactly and all those $s$ that are not included in $R$. Next consider the join $R \cup Q$ given sets $R$ and $Q$: an element $s$ is a member of $R \cup Q$ precisely when it is a member of $R$, or of $Q$, or of both. The collection of sets generated by combining and iterating the operations of complement and join is called an algebra, denoted $S$. In statistics we interpret $S$ as the set of samples, and we can associate sets $R$ with specific events or observations. A specific sample $s$ includes a record of the event denoted with $R$ exactly when $s \in R$. We take the algebra of sets like $R$ as a language for making claims about the samples.

A probability function is defined as an additive normalized measure on the algebra: a function

$$ P: {\cal S} \rightarrow [0, 1] $$

such that $P(W) = 1$ and $P(R \cup Q) = P(R) + P(Q)$ if $R \cap Q = \emptyset$. The conditional probability $P(Q \mid R)$ is defined as

$$ P(Q \mid R) \; = \; \frac{P(Q \cap R)}{P(R)} , $$

whenever $P(R) > 0$. It determines the relative size of the set $Q$ within the set $R$. It is often read as: the probability of the event $Q$ given that the event $R$ occurs. Recall that the set $R$ consists of all samples $s$ that include a record of the event associated with $R$. By looking at $P(Q \mid R)$ we zoom in on the probability function within this set $R$, i.e., we consider the condition that the associated event occurs.

What does the probability function mean? The mathematical notion of probability does not provide a complete answer. The function $P$ may be interpreted as

1. ontic, namely the frequency or propensity of the occurrence of a state of affairs, often referred to as the chance, or else as
2. epistemic, namely the degree of belief in the occurrence of the state of affairs, the willingness to act on its assumption, a degree of support or confirmation, or similar, often referred to as the credence.

This distinction should not be confused with that between objective and subjective probability. Both ontic and epistemic probability can be given an objective and subjective character, in the sense that both can be taken as dependent on, or independent of a knowing subject and her conceptual apparatus. For more details on the interpretation of probability, the reader may consult a large literature, including Galavotti (2005), Gillies (2000), Mellor (2005), von Plato (1994), the anthology by Eagle (2010), the handbook of Hajek and Hitchcock (2016), or indeed the entry on interpretations of probability. In this context the key point is that the interpretations can all be connected to foundational programmes for statistical procedures. Although the match is far from exact, the two major types specified above can be associated with the two major theories of statistics, classical and Bayesian statistics, respectively.

### 2.1 Chance and classical statistics

In the sciences, the idea that probabilities express states of affairs, i.e., properties of chance setups or stochastic processes, is relatively prominent. The probabilities express relative frequencies in series of events or, alternatively, tendencies or propensities in the systems that realize those events. More precisely, the probability attached to the property of an event type can be understood as the frequency or tendency with which that property manifests in a series of events of that type. For instance, the probability of a coin landing heads is a half exactly when in a series of similar coin tosses, the coin lands heads half the time. Or alternatively, the probability is half if there is an even tendency towards both possible outcomes in the setup of the coin tossing. The mathematician Venn (1888) and scientists like Quetelet and Maxwell (cf. von Plato 1994)[^plato-1994] are early proponents of this way of viewing probability, although the basic conception of chance goes as far back as Huygens (1657). Philosophical theories of propensities were first coined by Peirce (1910), and developed by Popper (1959), Mellor (1971), Giere (1976), and Bigelow (1977); see Handfield (2012) for an overview. A rigourous theory of probability as frequency was first devised by von Mises (1981), also defended by Reichenbach (1938) and beautifully expounded in van Lambalgen (1987). A highly readable overview of ideas about chance is offered by Diaconis and Skyrms (2018).

This ontic conception of probability is connected to one of the major theories of statistical method, which is often called classical statistics but which, more neutrally, might be termed Bernoullian, in reference to its early appearance in Bernoulli’s *Ars Conjectandi* (1713). It was developed roughly in the first half of the 20th century, mostly by mathematicians and working scientists like Fisher (1925, 1935, 1956), Wald (1939, 1950) and Neyman and Pearson (1928, 1933, 1967), and refined by very many statisticians of the last few decades. The key characteristic of this theory of statistics aligns naturally with viewing probabilities as chances, hence pertaining to observable and repeatable events. Ontic probability cannot meaningfully be attributed to statistical hypotheses, since hypotheses do not have tendencies to occur, and hence no frequencies with which they come about: they are categorically true or false, once and for all. Attributing probability to a hypothesis entails that the probability is understood epistemically.

Classical or Bernoullian statistics is often called frequentist, owing to the centrality of frequencies of events in its procedures and the prominence of the frequentist interpretation of probability developed by von Mises. In this interpretation, chances are identified with frequencies, or proportions in a class of similar events or items. They are best thought of as analogous to other physical quantities, like mass and energy. It deserves emphasis that frequencies are thus conceptually prior to chances. In propensity theory the probability of an individual event or item is viewed as a tendency in nature, so that the frequencies, or the proportions in a class of similar events or items, manifest as a consequence of the law of large numbers. In the frequentist theory, by contrast, the proportions lay down, indeed define what the chances are. This leads to a central problem for frequentist probability, the so-called reference class problem: it is not clear what class to associate with an individual event or item (cf. Reichenbach 1949, Hajek 2007)[^reichenbach-1949]. One may argue that the class needs to be as narrow as it can be, offering a maximally precise description of the event type at issue. But in the extreme case of a singleton class of events, the chances of course trivialize to zero or one. Since classical statistics employs non-trivial probabilities that attach to the single case in its procedures, a fully frequentist understanding of statistics is arguably in need of a response to the reference class problem.

To illustrate ontic probability in classical statistics, we briefly consider the frequentist interpretation in the example of the tea tasting student.

> **Frequentist interpretation**
> We denote the null hypothesis that the student is merely guessing by $h$. Say that we follow the rule indicated in the example above: we reject the null hypothesis, i.e., deny that the student is merely guessing, whenever the sampled data $s$ is included in a particular set $R$ of possible samples, i.e., when $s \in R$. Furthermore the set of samples $R$ has a summed probability of 3% according to the null hypothesis. Now imagine that we are supposed to judge a whole population of tea tasting students, scattered in tea rooms throughout the country. Then, by running the experiment in a large number of tea rooms and adopting the rule just cited, we know that we will falsely attribute special tea tasting talents to 3% of those students for whom the null hypothesis is true, i.e., who are in fact merely guessing. Alternatively, we may imagine a single student without special tea tasting talents, being tested by a population of scientists who all use the same null hypothesis test. In that case 3% of scientists will falsely attribute special tea tasting talents to the student. Either way, the percentage pertains to a frequency within a particular set of events, which by the rule is connected to a particular error in judgment.

Say that we have found a student for whom we reject the null hypothesis, i.e., a student who passes the test. Does she have the tea tasting ability or not? Unfortunately this is not the sort of question that can be answered by the test at hand. A good answer would presumably involve the proportion of students who indeed have the special tea tasting ability among those whose scores exceeded a certain threshold, e.g., those who answered correctly on all five cups. But this latter proportion, namely of students for whom the null hypothesis is false among all those students who passed the test, cannot be determined without further assumptions. It will depend also on the proportion of students who have the ability in the population on the whole: if there are many of them around, it is more probable that one who passed the test indeed has the tea tasting talents. But the null hypothesis test only involves proportions within a group of students for whom the null hypothesis is assumed to be true. This holds in general for frequentist statistics: it only considers probabilities for events, or chances for short, under the assumption that the events are distributed in a given way, and it only involves the observable consequences of these chances, namely the frequencies.

### 2.2 Credence and statistical inference

There is an alternative way of viewing the probabilities that appear in statistical methods: they can be seen as expressions of epistemic attitudes, or *credences* for short. We are again facing several interrelated options.

#### 2.2.1 Types of credence

Credences are often taken as doxastic in the sense that they specify opinions about data and hypotheses of an idealized rational agent. They express the strength or degree of belief, for instance regarding the correctness of the next guess of the tea tasting student. Credences are often framed in a decision-theoretic way, namely as part of a more elaborate representation of the agent’s dispositions towards decisions and actions. Such a decision-theoretic representation involves credences alongside preferential attitudes and other furnishing of inner life. The norms for credences accordingly derive from requirements on how credences guide our actions, often spelled out in a specific pragmatist way. Credences are taken to express a willingness to engage in collections of bets: the credence in the occurrence of an event is given by the price of a betting contract that pays out one monetary unit if the event manifests. So-called Dutch book arguments then constrain credences: the requirement that the agent does not expose herself to sure loss entails that the credences must comply to the axioms of probability theory (cf. Jeffrey 1992)[^jeffrey-1992].

There are alternatives to this pragmatist take on doxastic credence. Doxastic credences might instead pertain to beliefs in a stand-alone fashion, separate from decisions or actions. In this case the norms for the credences can be derived from the requirement that the beliefs have to be accurate, i.e., close to the truth values for the occurence or non-occurence of the events under scrutiny. By relying on specific assumptions about proximity to truth values, we can provide so-called non-pragmatist vindications of the probability axioms for credences. An early argument of this kind can be found in de Finetti (1974) but further discussions and extensions are proposed by for instance Joyce (1999) and Leitgeb and Pettigrew (2010a and 2010b).

Within the doxastic conception of credence we can make a further subdivision into subjective and objective doxastic credences. The defining characteristic of an objective doxastic credence is that it is constrained by further rationality criteria, or else by the demand that the beliefs are calibrated to an objective fact or state of affairs. A prominent rationality criterion is that equal possibilities receive equal credence, known as the princple of indifference. A well-known calibration requirement, expressed in a variety of so-called chance-credence principles, is that the credences align with frequencies of events, or chance ascriptions to events. A subjective doxastic attitude, by contrast, is not constrained in such a way: agents are free to believe as they see fit, as long as they comply to the probability axioms.

Credences may also be taken as logical. More precisely, probability theory itself may be taken as a kind of logic, i.e., a formal structure that describes valid inference. In this logical approach probability values over data and hypotheses have a role that is comparable to the role of truth values in Boolean logic. The axioms of probability impose coherence constraints on probability values, much like the rules of logic impose constraints on truth valuations. Accordingly, we can derive the norms for credences from an independent conception of valid inference. In particular, compliance to the probability axioms can be derived from natural desiderata for graded beliefs (e.g., Cox 1961 and Howson 2000)[^cox-1961][^howson-2000]. The logical conception of credence is distinct from the doxastic one because the logical constructions do not carry any reference to a psychological reality, in the same way that logic does not represent thought.

The epistemic view on probability has a long history, starting in early work by Pascal (cf. Hacking 2006)[^hacking-2006]. It was substantially developed in the 19th and the first half of the 20th century, first by the hand of De Morgan (1847) and Boole (1854), later by Keynes (1921), Ramsey (1926) and de Finetti (1937), and by decision theorists, philosophers and inductive logicians such as Carnap (1950), Savage (1962), Levi (1980), and Jeffrey (1992). Important proponents of these views in statistics were Jeffreys (1961), Edwards (1972), Lindley (1965), Good (1983), Jaynes (2003) as well as Bayesian philosophers and statisticians of the last few decades (Dawid 2004, Berger 2006, Goldstein 2006, Kadane 2011 among many others)[^berger-2006][^dawid-2004][^dawid-2004-2][^goldstein-2006][^kadane-2011]. All of these have a view that places probabilities somewhere in the realm of the epistemic rather than the ontic, i.e., not as part of the world itself but rather as a means to model our beliefs about the world.

#### 2.2.2 Statistical inference

For present concerns the important point is that each of these epistemic interpretations of the probability calculus comes with its own set of foundational programs for statistics. On the whole, epistemic probability is most naturally associated with the second major theory of statistical methods, called Bayesian statistics (Press 2002, Berger 2006, Gelman et al 2013)[^berger-2006][^gelman-2013][^gelman-2013-2][^press-2002], in reference to its inventor Thomas Bayes. The key characteristic of Bayesian statistics flows directly from the epistemic interpretation: under this interpretation it makes sense to assign probability to a statistical hypothesis, as an expression of how strongly we believe the hypothesis. Bayesian statistics allows us to relate credences over statistical hypotheses to the chances of events, so that we can express how our credences over statistical hypotheses change under the impact of observations. The result is a formal representation of statistical inference, i.e., a framework for deriving credences over hypotheses in the light of data.

To illustrate the epistemic conception of probability in Bayesian statistics, we return to the example of the tea tasting student.

> **Bayesian inference**
> As before we denote the null hypothesis that the student is guessing randomly with $h$. The distribution $P_{h}$ assigns a probability of 1/2 to any guess made by the student. The alternative $h'$ is that the student performs better than a fair coin. To keep matters simple, we might stipulate that the distribution $P_{h'}$ gives a probability of 3/4 to a correct guess. At the outset we might find it rather improbable that the student has special tea tasting abilities. To express this we give the hypothesis of her having these abilities only half the probability that we allocate to her not having any such abilities: $P(h') = 1/3$ and $P(h) = 2/3$. Notice that we need an epistemic conception of probability to make sense of this last step: we assign a credence to the hypotheses, which themselves impose chances over the events, or over the samples representing them. Now, leaving the mathematical details to Section 4.1, after receiving the sample data $s$ that the student guessed all five cups correctly, our new credence in her special abilities, denoted $P_{s}$, has more than reversed. We now think it roughly four times more probable that the student has the special abilities than that she is merely a random guesser: $P_{s}(h') = 243/307 \approx 4/5$ and $P_{s}(h) \approx 1/5$.

We express our epistemic attitudes towards statistical hypotheses in terms of credences, and the data then impact on these credences in a regulated fashion. The process of adapting credences to data is termed Bayesian statistical inference.

It deserves emphasis that Bayesian statistics is not the sole user of an epistemic notion of probability. A frequentists understanding of probabilities assigned to statistical hypotheses seems nonsensical but it is perfectly possible to interpret the probabilities of events, or the elements in sample space that represent the events, as epistemic, quite independently of the statistical method that is being used. As further explained in the next section, several philosophical developments of classical statistics employ epistemic probability, most notably fiducial probability (Fisher 1955 and 1956; see also Seidenfeld 1992 and Zabell 1992)[^fisher-1955][^fisher-1956][^seidenfeld-1992][^zabell-1992], likelihoodism (Hacking 1965, Edwards 1972, Royall 1997)[^edwards-1972][^hacking-1965][^royall-1997], and evidential probability (Kyburg 1961)[^kyburg-1961], or else connect the procedures of classical statistics to inference and support in some other way (e.g., Mayo 1996)[^mayo-1996]. In these developments of classical statistics, probabilities and functions over sample space are to some extent read epistemically, i.e., as expressions of the strength of evidence, the degree of support, or similar.

## 3. Classical statistics

The collection of procedures that may be grouped under classical statistics is vast and diverse. By and large, classical statistical procedures share the feature that they only rely on probability assignments over sample spaces. An important motivation for this is that those probabilities can be interpreted as frequencies, or as chances expressed in frequencies, from which the term of frequentist statistics originates. Classical statistical procedures are typically defined by some function over sample space, where this function depends, often exclusively, on the distributions that the hypotheses under consideration assign to the sample space. Over the domain of samples that may be obtained, an estimation function points to one element from a range of hypotheses, or perhaps to a set of them, as being in some sense the best fit with that sample. A test function, by contrast, will point to a candidate hypothesis that renders the sample too improbable and thus a candidate for rejection.

In sum, classical procedures employ the data to narrow down a set of hypotheses. Put in such general terms, it becomes apparent that classical procedures provide a response to the problem of induction. The data are used to get from a weak general statement about the target system to a stronger one, namely from a set of candidate hypotheses to a subset of them, possibly a singleton. A central concern in the philosophy of statistics is how we are to understand such procedures, and how we might justify them. The pattern of classical statistics resembles that of eliminative induction: in view of the data we discard some of the candidate hypotheses. Indeed classical statistics is often seen in loose association with Popper’s falsificationism, but this association is somewhat misleading. In classical procedures statistical hypotheses are discarded when they render the observed sample too improbable, which of course differs from discarding hypotheses that deem the observed sample impossible.

### 3.1 Basics of classical statistics

The foregoing already provided a short example and a rough sketch of classical statistical procedures. These are now specified in more detail, on the basis of Barnett (1999) as primary source. The following focuses on two very central procedures, hypothesis testing and estimation. The first has to do with the comparison of two statistical hypotheses, and invokes theory developed by Neyman and Pearson. The second concerns the choice of a hypothesis from a set, and employs procedures devised by Fisher.

#### 3.1.1 Hypothesis testing

The procedure of Fisher’s null hypothesis test was already discussed briefly in the foregoing. Let $h$ be the hypothesis of interest and, for the sake of simplicity, let $S$ be a finite sample space. The hypothesis $h$ imposes a distribution over the sample space, denoted $P_{h}$. Every point $s$ in the space represents a possible sample of data. We now define a function $F$ on the sample space that identifies when we will reject the null hypothesis by marking the samples $s$ that lead to rejection with $F(s) = 1$, as follows:

$$ F(s) = \begin{cases} 1 \quad \text{if } P_{h}(s) < q,\\ 0 \quad \text{otherwise.} \end{cases} $$

Notice that the rejection of $h$ hinges on the probability of the data under the assumption of the hypothesis, $P_{h}(s)$. This expression is often called the likelihood of the hypothesis for the sample $s$. We can collect all samples $s$ for which the likelihood drops below the threshold $q$ in a so-called region of rejection, $R_{q} = \{ s:\: F(s) = 1 \}$. The threshold $q$ can be determined by requiring that the total probability of the region of rejection $R_{q}$ is below a given level of error, $P_{h}(R_{q}) < \alpha$. A common choice is $\alpha = 0.05$.

In standard null hypothesis testing little can be said about error rates if the null hypothesis is in fact false. In response to this Neyman and Pearson (1928, 1933, and 1967) devised the so-called likelihood ratio test, a test that compares the likelihoods of two rivaling hypotheses. Let $h$ and $h'$ be the null and the alternative hypothesis respectively. We can compare these hypotheses by the following test function $F$ over the sample space:

$$ F(s) = \begin{cases} 1 \quad \text{if } \frac{P_{h'}(s)}{P_{h}(s)} > r,\\ 0 \quad \text{otherwise,} \end{cases} $$

where $P_{h}$ and $P_{h'}$ are the probability distributions over the sample space determined by the statistical hypotheses $h$ and $h'$ respectively. If $F(s) = 1$ we decide to reject the null hypothesis $h$, else we accept $h$ for the time being and so disregard $h'$. A region of rejection $R_{r}$ can be defined analogously to $R_{q}$ above.

The decision to accept or reject a hypothesis is associated with the possibility of error. Especially Neyman has become known for interpreting this in a strictly behaviorist fashion. For further discussion on this point, see Section 3.2.2. We commit a so-called type-I error if we reject the null hypothesis when in fact it is true. So for a given test function, the probability of a type-I error, often denoted with $\alpha$, is the probability, according to the null hypothesis $h$, of obtaining data within the region of rejection, i.e., data that leads us to falsely reject this hypothesis $h$:

$$ \alpha = P_{h}(R_{r}) = \sum_{s \in S} F(s) P_{h}(s) . $$

The probability $\alpha$ is alternatively called the significance level of the test. We can also make the converse type-II error of accepting the null hypothesis when in fact the alternative is true. The probability of a type-II error, often denoted $\beta$, is the probability, according to the alternative hypothesis $h'$, of obtaining data outside of the region of rejectioni.e., data that leads us to falsely accept the null hypothesis $h$:

$$ \beta = 1 - P_{h'}(R_{r}) = \sum_{s \in S} F(s) P_{h'}(s) . $$

The probability $1 - \beta$ is alternatively called the power of the test. An optimal test is one that minimizes both the errors $\alpha$ and $\beta$, and hence minimizes significance level while maximizing power.

In their fundamental lemma, Neyman and Pearson proved that the decision has optimal significance and power for, and only for, likelihood-ratio test functions $F$. That is, an optimal test depends only on a threshold for the ratio $P_{h'}(s) / P_{h}(s)$. The example of the tea tasting student allows for an easy illustration of the likelihood ratio test.

> **Neyman-Pearson test**
> Next to the null hypothesis $h$ that the student is randomly guessing, we now consider the alternative hypothesis $h'$ that she has a chance of $3/4$ to guess the order of tea and milk correctly. The samples $s$ are binary 5-tuples that record guesses as correct and incorrect. To determine the likelihoods of the two hypotheses, and thereby the value of the test function for each sample, we only need to know the so-called sufficient statistic, in this case the number of correct guesses $k$ out of the total number $n$, independently of the order. We can collect all samples $s$ in which $k$ out of $n$ guesses are correct in a set of sequences, denoted by $S_{k/n}$. All sequences within these sets are equally probable according to the hypotheses under scrutiny. In the example we observe $n = 5$ guesses, so we have $P_{h}(S_{k/5}) = \binom{5}{k}1/2^{5}$ and $P_{h'}(S_{k/5}) = \binom{5}{k} 3^{k} / 4^{5}$. For any individual sample $s$ and for the aforementioned sets of sequences $S_{k/n}$, the likelihood ratio becomes $3^{k} / 2^{5}$. If we require that the significance level is lower than 5%, then it can be calculated that only the set of samples with $k = 5$ may be included in the region of rejection. Accordingly we may set the cut-off point $r$ at $r = 3^{4} / 2^{5}$. Upon finding that the student guesses all five cups correctly, we reject the null hypothesis with 5% significance.

Notice that the construction of a test function relies on the adoption of a specific structuring of the sample space. Samples that are equally probable according to the hypotheses under scrutiny are collected into sets that correspond to observations of a sufficient statistic, and the region of rejection is then defined in terms of this statistic. In some cases, e.g., so-called one-sided tests, the test function relies on a further structuring of the sample space.

Another expression of the error of a test, closely related to but different from the significance level, is the so-called p-value (Schervish 1996). After determining a test function and region of rejection by requiring a certain significance level $\alpha$, as in the foregoing, we might obtain data well inside this region, so that it is also included in a region of rejection that is much smaller. The p-value of a given sample and test is the lowest possible significance level of the test that warrants the rejection of the null hypothesis with that sample.

> **P-values**
> Imagine that we offer the student fifteen cups of tea. Using a significance level of 2%, and entertaining the same hypotheses as in the foregoing, we can determine a new region of rejection $R_{r}$ in this larger sample space. It includes the sequence of fifteen correct guesses, the singleton $S_{15/15}$, but also the set of all 15 sequences with one failure, $S_{14/15}$, the set of all 105 sequences with two failures, $S_{13/15}$, and the set of all 455 sequences with three failures, $S_{12/15}$. Every specific sequence has the same probability according to the null hypothesis, namely $P_{h}(S_{15/15}) = 1/2^{15}$, so their summed probability is $P_{h}(R_{r}) = 576 / 2^{15} \approx 0.0176 = 1.76 \%$. Now imagine that we find the student guesses all but one cup correctly. We can then reject the null hypothesis at 2% significance level, because the sample falls within $R_{r}$. But in retrospect we could have set our significance level much lower, by including only the sample $S_{15/15}$ and the 15 samples collected in $S_{14/15}$ in the smaller region of rejection $R_{r'}$, with a summed probability as low as $P_{h}(R_{r'}) = 16/2^{15} \approx 0.05 \%$. To express how convincingly we rejected the null hypothesis, we report the latter number as the p-value.

The p-value is unfortunately ill-understood by statistical practitioners. We briefly consider the debate over it below.

#### 3.1.2 Estimation

In this section we consider parameter estimation by maximum likelihood, as first devised by Fisher (1956). Once again we employ a finite sample space $S$. In the tea tasting example, the samples $s$ are finite sequences of guesses. A set of such sequences is denoted by an augmented capital $S$ as above, e.g., we write the set of sequences starting with five correct guesses as $S_{11111}$, and we write the set of all sequences with $k$ successes in $n$ trials with $S_{k/n}$.

Maximum likelihood estimation, or MLE for short, is a tool for determining the best fitting among a set of hypotheses, often called a statistical model. Let $M = \{h_{\theta} :\: \theta \in \Theta \}$ be the model, labeled by the parameter $\theta$ and $P_{\theta}$ the distribution associated with $h_{\theta}$. Then define the maximum likelihood estimator $\hat{\theta}$ as a function over the sample space:

$$\hat{\theta}(s) = \{ \theta :\, \forall \theta' \bigl( P_{\theta'}(s) \leq P_{\theta}(s) \bigr) \}.$$

So the estimator is a set, typically a singleton set, of values of $\theta$ for which the likelihood of $h_{\theta}$ on the data $s$ is maximal. The associated best hypothesis we denote with $h_{\hat{\theta}}$. This can be illustrated easily for the tea tasting student.

> **Maximum likelihood estimation (MLE)**
> A natural statistical model for the case of the tea tasting student consists of hypotheses $h_{\theta}$ for all possible probabilities for correctly guessing, or levels of accuracy, that the student may have, $\theta \in [0, 1]$. The number of correct guesses $k$ and the total number of guesses $n$ are the sufficient statistics: the probability of a sample only depends on those numbers. For the set of finite sequences $S_{k/n}$ the associated likelihood of $h_{\theta}$ is
>
> $$ P_{\theta}(S_{k/n}) = \binom{n}{k} \theta^{k} (1 - \theta)^{n - k} . $$
>
> The maximum likelihood estimator for a given observation $S_{k/n}$ then is $\hat{\theta} = k / n$, because among all hypotheses $h_{\theta}$ the likelihood $P_{\theta}(S_{k/n})$ for $S_{k/n}$ is maximal at that value.

We suppose that the number of cups served to the student is fixed at $n$ so that sample space is finite. Notice, finally, that $h_{\hat{\theta}}$ is the hypothesis that makes the data most probable and not the hypothesis that is most probable in the light of the data.

There are all manner of requirements that we might impose on an estimator function. One is that the estimator must be consistent, an concept defined by reference to a true value $\theta^{\star}$. An estimator function is consistent if and only if for ever larger samples $S_{n}$ the estimator function $\hat{\theta}$ converges to the true parameter value $\theta^{\star}$. We call a hypothesis $h_{\theta^{\star}}$ true if and only if the data are distributed according to the associated distribution $P_{\theta^{\star}}$ or, equivalently, if the associated distribution $P_{\theta}$ is the one from which the data are generated. Another requirement is that the estimator must be unbiased, meaning that for finite data there is no discrepancy between the true parameter value and the expected value of the estimator, where this expected value is computed on the basis of $P_{\theta^{\star}}$. The classical statistical literature on estimation discusses several other such goodmaking features of estimator functions.

MLE is not the only procedure for determining the value of a parameter of interest on the basis of statistical data. We may also maximize or minimize some other target function. In the context of curve fitting, for instance, we can minimize the sum of the squares of the distances between the prediction of the statistical hypothesis and the given data points, known as the method of least squares. However, under the assumption of a statistical model in which errors are normally distributed, this procedure comes down to MLE. A more general perspective, first developed by Wald (1950), is provided by measuring the discrepancy between the predictions of the hypothesis and the actual data in terms of a loss function. The summed squares and the likelihoods may be taken as expressions of this loss. The principle that expected loss minimization is at the core of statistics has been developed in numerous directions since. Statistical learning theory, which is briefly covered below, offers a systematic analysis of this approach to statistics that can arguably underpin the estimation procedures of classical statistics (cf. Hastie et al. 2009, James et al. 2014)[^hastie-2009][^james-2014].

#### 3.1.3 Confidence intervals

Often the estimation is coupled to a so-called confidence interval. To explain this notion, we first construct a closely related notion, the region of probable estimation. For ease of exposition, assume that $\Theta$ consists of the real numbers and that every point $s$ in the sample space is labelled with a single value of the estimation function $\hat{\theta}(s)$. We define the set $R_{\tau} = \{ s:\: \hat{\theta}(s) = \tau \}$, the set of samples for which the estimator function has the value $\tau$. We can now collate a region in sample space within which the estimator function $\hat{\theta}$ is not too far off the mark, specifically, differing by at most $\Delta$ on either side of the true parameter value $\theta^{\star}$:

$$ R_{\Delta} = \{ R_{\tau} :\: \tau \in [ \theta^{\star} - \Delta , \theta^{\star} + \Delta ] \} . $$

This so-called region of probable estimation is the union of all sets $R_{\tau}$ for which $\tau \in [ \theta^{\star} - \Delta , \theta^{\star} + \Delta ]$.

We may choose the value of $\Delta$ in such a way that the region of probable estimation $R_{\Delta}$ covers a large portion of the sample space, as measured by the true distribution $P_{\theta^{\star}}$:

$$ P_{\theta^{\star}}(R_{\Delta}) = \int_{\theta^{\star} - \Delta}^{\theta^{\star} + \Delta} P_{\theta^{\star}}(R_{\tau}) d\tau = 1 - \alpha ,$$

where $\alpha$ is a margin of error. If we fix a specific margin of error $\alpha$ , this determines size of $\Delta$, which is thereby set to $\Delta_{1 - \alpha}$. The size of the latter says something about the quality of the estimate: if $\Delta_{1-\alpha}$ is small, the estimate $\hat{\theta}$ is accurate. Notice that such regions of probable estimation carry a clear frequentist interpretation: when repeating the data collection under the assumption of the true distribution, the fraction of times in which the estimator $\hat{\theta}$ is further away from $\theta^{\star}$ than $\Delta_{1-\alpha}$, tends to $\alpha$.

We can now define the confidence interval around an estimate. The key move is that we take the estimate $\hat{\theta}$ as a stand-in for the true parameter value $\theta^{\star}$. Starting from a specific estimation $\hat{\theta}$, we can calculate a region of probable estimation $R_{\Delta}$ based on an error rate $\alpha$ by putting the estimate in the role of the true distribution, i.e., by substituting $\theta^{\star} = \hat{\theta}$ in the foregoing formulas and calculating $\Delta_{1-\alpha}$ under this assumption. The symmetric confidence interval is then defined as:

$$ C_{1 - \alpha} = [ \hat{\theta} - \Delta_{1 - \alpha} , \hat{\theta} + \Delta_{1 - \alpha} ] . $$

Statistical folklore typically sets $\alpha$ at a value of 5%, leading to the symmetric 95% confidence interval $C_{95\%}$. The confidence interval is often reported alongside an estimate to indicate the estimate’s accuracy, and thereby communicate something about the size of the effect of an intervention preceding the data collection (cf. Cumming 2012)[^cumming-2012].

We have to be very careful when interpreting confidence intervals. The suggestion is that it can carry a frequentist interpretation much like the region of probable estimation, as in: we find the true value $\theta^{\star}$ within $\Delta_{1 - \alpha}$ of our estimate $\hat{\theta}$ in a fraction of $1 - \alpha$ of all samples. But this is not right. For one, to compute $\Delta_{1 - \alpha}$ we substituted the estimate for the true value. The actual value of $\Delta_{1 - \alpha}$ may be different, depending on the location of the true parameter value and the value for $\Delta_{1 - \alpha}$ at that point. However, even if $\Delta_{1 - \alpha}$ is the same when calculated by means of the estimate and by means of the true parameter, we still cannot understand the confidence interval as the interval within which the true parameter value is included with a frequency of $1 - \alpha$. The true parameter value stays fixed, and therefore it does or does not fall within the given interval, period. It makes no sense to say that it does this with a certain frequency.

We can still make sense of confidence intervals in terms of frequencies. To do so, we have to assume that the value of $\Delta_{1 - \alpha}$ is the same for all possible values of the true parameter. In that case we can say, of the specific confidence interval calculated from the currently obtained estimate $\hat{\theta}$, that it covers all possible values of the true parameter value $\theta^{\star}$ for which, if they were the true value, the currently obtained estimate $\hat{\theta}$ would be included in the region of probable estimation, while for true parameter values outside of the specific confidence interval, the currently obtained estimate would not be. Accordingly, on repeating the data collection and repeatedly constructing a confidence interval around the newly obtained estimate $\hat{\theta}$, maintaining the assumption that $\Delta_{1-\alpha}$ is constant from one confidence interval to the next, the true parameter value is included in a fraction $1 - \alpha$ of this sequence of confidence intervals. That is, the frequentist guarantee pertains to the procedure of constructing confidence intervals, not to the specific confidence interval around any given estimate.

There are of course many more procedures for estimating a variety of statistical targets, and there are many more expressions for the quality of the estimation (e.g., bootstrapping, see Efron and Tibshirani 1993)[^efron-1993]. Theories of estimation often come equipped with a rich catalogue of situation-specific criteria for estimators, reflecting the epistemic and pragmatic goals that the estimator helps achieving. However, in itself the estimator functions do not present guidelines for beliefs about the accuracy of any given estimate and, importantly, confidence intervals do not either.

### 3.2 Problems for classical statistics

Classical statistics is widely discussed in the philosophy of statistics. In what follows two problems with the classical approach are outlined, to wit, its problematic interface with belief and the fact that it violates the so-called likelihood principle. Many more specific problems can be seen to derive from these general ones.

#### 3.2.1 Interface with belief

Consider the likelihood ratio test of Neyman and Pearson. As indicated, the significance level of a test is an error rate that will manifest if data collection and testing is repeated, assuming that the null hypothesis is in fact true. Notably, this value does not tell us how probable the truth of the null hypothesis is, and neither does the p-value calculated from a specific sample. However, many scientists do use hypothesis testing in this manner, and there is much debate over what can and cannot be derived from a p-value (cf. Berger and Sellke 1987, Casella and Berger 1987, Cohen 1994, Harlow et al 1997, Wagenmakers 2007, Ziliak and McCloskey 2008, Spanos 2007, Greco 2011, Sprenger 2016)[^berger-1987][^casella-1987][^cohen-1994][^greco-2011][^harlow-1997][^sprenger-2016][^wagenmakers-2007][^ziliak-2008]. After all, the test leads to the advice to either reject the hypothesis or accept it, and this seems conceptually very close to giving a verdict of truth or falsity. An attempt to provide it with an interpretation in terms of support has been undertaken by Cox and Mayo (2006).

While the evidential value of p-values is much debated, many admit that the probability of data according to a hypothesis cannot be used straightforwardly as an indication of how believable the hypothesis is (cf. Gillies 1971, Spielman 1974 and 1978)[^gillies-1971][^spielman-1974][^spielman-1978]. Such usage runs into the so-called *base-rate fallacy.* The example of the tea tasting student is again instructive.

> **Base-rate fallacy**
> Imagine that we travel the country to perform the tea tasting test with a large number of students, and that we find a particular student who guesses all five cups correctly. Should we conclude that the student has a special talent for tasting tea? The problem is that this depends on how many students among those tested actually have the special talent. If the ability is very rare, it is more attractive to put the five correct guesses down to a chance occurrence. By comparison, imagine that all the students enter a lottery. In analogy to a student guessing all cups correctly, consider a student who wins one of the lottery’s prizes. In a normal lottery, winning a prize is very improbable, unless one is in cahoots with the bookmaker, which is the analogon of having a special tea tasting ability. But surely if a student wins the lottery, this is by itself not a good reason to conclude that they must have committed fraud and call for their arrest. Similarly, if a student has guessed all cups correctly, we cannot simply conclude that they have special abilities.

Essentially the same problem occurs if we consider the estimations of a parameter as direct advice on what to believe, as made clear by an example of Good (1983, p. 57) that is presented here in the tea tasting context. After observing five correct guesses, we have $\hat{\theta} = 1$ as maximum likelihood estimator. But it is hardly believable that the student will in the long run be 100% accurate. The point that estimation and belief maintain complicated relations is also put forward in discussions of Lindley’s paradox (Lindley 1957, Spanos 2013, Sprenger 2013)[^lindley-1957][^sprenger-2013][^sprenger-2013-2], and in the faulty interpretation of confidence intervals as regions of probable estimation. In short, it is wrongheaded to turn the results of classical statistical procedures into beliefs simpliciter.

It is a matter of debate whether any of this can be blamed on classical statistics. Initially, Neyman was emphatic that his testing procedures could not be taken as inferences, or as in some other way pertaining to the epistemic status of the hypotheses. His own statistical philosophy was strictly behaviorist (cf. Neyman 1957)[^neyman-1957], so it may be argued that the problems disappear if only scientists abandon their faulty epistemic use of classical statistics. As explained in the foregoing, we can uncontroversially associate error rates with classical procedures, and so with the decisions that flow from these procedures. A behavioural and error-based understanding of classical statistics seems just fine. On the other hand, as further elaborated below, both statisticians and philosophers have argued that an epistemic reading of classical statistics is possible, and in fact preferable (e.g., Fisher 1955, Royall 1997)[^fisher-1955][^royall-1997]. Accordingly, many have attempted to reinterpret or develop the theory, in order to align it with the epistemically oriented statistical practice of scientists (see Mayo 1996, Mayo and Cox 2006, Mayo and Spanos 2011, Spanos 2013b)[^mayo-1996][^mayo-2006][^mayo-2011][^mayo-2006-2][^spanos-2013b].

#### 3.2.2 The nature of evidence

Hypothesis tests and estimations are sometimes criticised because their results generally depend on the probability functions over the entire sample space, and not exclusively on the probabilities of the observed sample. That is, the decision to accept or reject the null hypothesis depends not just on the probability of what has actually been observed according to the various hypotheses, but also on the probability assignments over events that could have been observed but were not. A well-known illustration of this problem concerns so-called *optional stopping* (Robbins 1952, Roberts 1967, Kadane et al 1996, Mayo 1996, Howson and Urbach 2006)[^howson-2006][^mayo-1996][^mayo-2006][^mayo-2006-2][^robbins-1952][^roberts-1967].

Optional stopping is here illustrated for the likelihood ratio test of Neyman and Pearson but a similar story can be run for Fisher’s null hypothesis test and for the determination of estimators and confidence intervals.

> **Optional stopping**
> Imagine two researchers who are both testing the same student on his ability to determine the order in which milk and tea were poured in his cup. They both entertain the null hypothesis that he is guessing at random, with a probability of $1/2$, against the alternative of his guessing correctly with a probability of $3/4$. The more diligent researcher of the two decides to record six trials. The more impatient researcher, on the other hand, records at most six trials, but decides to stop recording the first trial that the student guesses incorrectly. Now imagine that, in actual fact, the man guesses all but the last of the cups correctly. Both researchers then have the exact same data of five successes and one failure, and the likelihoods for these data are the same for the two researchers too. However, while the diligent researcher cannot reject the null hypothesis, the impatient researcher can.

This might strike us as peculiar: statistics should tell us the objective impact that the data have on a hypothesis, but here the impact seems to depend on the *sampling plan* of the researcher and not just on the data themselves. As further explained in Section 3.2.3, the results of the two researchers differ because of differences in how samples that were not observed are factored into the procedure.

Some will find this dependence unacceptable: the intentions and plans of the researcher are irrelevant to the evidential value of the data. But others argue that it is just right. They maintain that the impact of data on the hypotheses should depend on the *stopping rule* or protocol that is followed in obtaining it, and not only on the likelihoods that the hypotheses have for those data (e.g. Mayo 1996)[^mayo-1996]. The motivating intuition is that upholding the irrelevance of the stopping rule opens up the possibility for opportunistic choices in data collection. In fact, defenders of classical statistics turn the table on those who maintain that optional stopping is irrelevant. They submit that it allows us to reason to a foregone conclusion by, for example, *persistent experimentation*: as a likelihoodist or Bayesian we might decide to cease experimentation only if the preferred result is reached. However, as shown in Kadane *et al*. (1996a and 1996b) and further discussed in Steele (2012), persistent experimentation is not guaranteed to yield any desired outcome, as long as we make sure to align the procedures with the appropriate evidence conception, e.g., likelihoodist or Bayesian.

The debate over optional stopping is eventually concerned with the appropriate evidential impact of data. A central concern in this wider debate is the so-called *likelihood principle* (see Hacking 1965 and Edwards 1972)[^edwards-1972][^hacking-1965]. This principle has it that the likelihoods of hypotheses for the observed data completely fix the evidential impact of those data on the hypotheses. In the formulation of Berger and Wolpert (1984), the likelihood principle states that two samples $s$ and $s'$ are evidentially equivalent exactly when $P_{i}(s) = kP_{i}(s')$ for all hypotheses $h_{i}$ under consideration, given some constant $k$. Famously, Birnbaum (1962) offers a proof of the principle from more basic assumptions. This proof relies on the assumption of conditionality. Say that we first toss a coin to determine what experiment to run, find that it lands heads, then do the experiment associated with this outcome, to record the sample $s$. Compare this to the case where we do the experiment, without randomly picking it first, and find $s$ directly. The conditionality principle states that this second sample has the same evidential impact as the first one: what we could have found if we had randomly chosen to run another experiment, but did not find, has no impact on the evidential value of the sample that we did find. Mayo (2010, 2014) has taken issue with Birnbaum’s derivation of the likelihood principle but new defenses have been offered since (Dawid 2014, Gandenberger 2014).

The classical view sketched above entails a violation of the likelihood principle: the impact of the observed data may be different depending on the probability of other samples than the observed one, because those other samples come into play when determining regions of acceptance and rejection. The Bayesian procedures discussed in Section 4, on the other hand, uphold the likelihood principle: in determining the posterior distribution over hypotheses only the prior and the likelihood of the observed data matter. In the debate over optional stopping and in many of the other debates between classical and Bayesian statistics, the likelihood principle is the focal point.

#### 3.2.3 Excursion: optional stopping

The view that the data reveal more, or something else, than what is expressed by the likelihoods of the hypotheses at issue merits detailed attention. Here we investigate this issue further with reference to the controversy over optional stopping.

Let us consider the analyses of the two above researchers in some numerical detail by constructing the regions of rejection for both of them.

> **Determining regions of rejection**
> The diligent researcher considers all 6-tuples of success and failure as the sample space, and takes their numbers as sufficient statistic. The event of six successes, or six correct guesses, has a probability of $1 / 2^{6} = 1/64$ under the null hypothesis that the student is merely guessing, against a probability of $3^{6} / 4^{6}$ under the alternative hypothesis. If we set $r < 3^{6} / 2^{6}$, then only this sample of six successes is included in the region of rejection of the null hypothesis. Samples with five successes have a probability of $1/64$ under the null hypothesis too, against a probability of $3^5 / 4^{6}$ under the alternative. So by lowering the threshold ratio $r$ by a factor 3, we also include the six samples with five successes and one failure in the region of rejection. But this will lead to a total probability of false rejection of $7/64$, i.e., a total of seven samples with a probability of $1/64$ each, which is larger than 5%. So these additional six samples cannot be included in the region of rejection, to avoid that the test surpasses a 5% significance level. Hence the diligent researcher does not reject the null hypothesis upon finding five successes and one failure.
>
> For the impatient researcher, on the other hand, the sample space is much smaller. Apart from the sample consisting of six successes, all samples consist of a series of successes ending with a failure, differing only in the length of the series. Yet the probabilities over the two samples of length six are the same as for the diligent researcher. As before, the sample of six successes is again included in the region of rejection. Similarly, the sequence of five successes followed by one failure also has a probability of $1/64$ under the null hypothesis, against a probability of $3^5 / 4^{6}$ according to the alternative. The difference is that lowering the likelihood ratio to include this sample in the region of rejection leads to the inclusion of the sample of a failure at the end only. And if we include this single extra sample in the region of rejection, the probability of false rejection under the null hypothesis becomes $1/32$ and hence does not exceed 5%. Consequently, on the basis of these data the impatient researcher can reject the null hypothesis that the student is merely guessing.

It is instructive to consider why exactly the impatient researcher can reject the null hypothesis. In virtue of the sampling plan, the other samples with five successes, namely the ones which kept the diligent researcher from including the observed sample in the region of rejection on pain of exceeding the error probability, could not have been observed. This exemplifies that the results of a classical statistical procedure do not only depend on the likelihoods for the actual data, which are indeed the same for both researchers. They also depend on the likelihoods for data that we did not obtain.

In the above example, it may be considered confusing that the protocol used for optional stopping depends on the data that is being recorded. But the controversy over optional stopping also emerges if there is no such interdependence between stopping rule and data. For example, imagine a third researcher who samples until the diligent researcher is done, or aborts sampling before that if she starts to feel peckish. Furthermore we may suppose that with each new cup offered to the student, the probability of feeling peckish is $\frac{1}{2}$. It turns out that this peckish researcher will also be able to reject the null hypothesis if she completes a series of five successes and one failure. It certainly seems at variance with the objectivity of the statistical procedure that this rejection depends on the physiology and the state of mind of the researcher: if she had not kept open the possibility of a snack break, she would not have rejected the null hypothesis, even though she did not actually take that break. As Jeffreys (1961, p. 385) famously quipped, this is indeed a “remarkable procedure”.

Yet the case is not as clear-cut as it may seem. For one, the peckish researcher is arguably testing two hypotheses in tandem, one about the ability of the tea tasting student and another about her own peckishness. Together the combined hypotheses have a different likelihood for the actual sample than the simple hypothesis considered by the diligent researcher. The likelihood principle given above dictates that this difference does not affect the evidential impact of the actual sample, but some retain the intuition that it should. Moreover, in some cases this intuition is shared by those who uphold the likelihood principle, namely when the stopping rule depends on the process being recorded in a way not already expressed by the hypotheses at issue (cf. Robbins 1952, Howson and Urbach 2006, p. 365)[^howson-2006][^robbins-1952]. In terms of our example, if the student is merely guessing and hence gets it right only by chance, then it may be more probable that the researcher gets peckish out of sheer boredom, than if the student performs far below or above chance level. In such a case the act of stopping itself reveals something about the hypotheses at issue, and this should be reflected in the likelihoods of the hypotheses. This makes the evidential impact that the data have on the hypothesis dependent on the stopping rule after all. And so the controversy over the relevance of the stopping rule continues (cf. Steel 2003, Fletcher 2023)[^fletcher-2023].

### 3.3 Responses to criticism

There have been numerous responses to the above criticisms. Some of those responses effectively reinterpret the classical statistical procedures as pertaining only to the evidential impact of data. Other responses develop the classical statistical theory to accommodate the problems. Their common core is that they establish or at least clarify the connection between two conceptual realms: the statistical procedures refer to physical probabilities, while their results pertain to evidence and support, or else to the rejection or acceptance of hypotheses.

#### 3.3.1 Likelihoodism

Classical statistics is often presented as providing us with advice for actions. The error probabilities do not tell us what epistemic attitude to take on the basis of statistical procedures, rather they indicate the long-run frequency of error if we live by them. Specifically Neyman advocated this interpretation of classical procedures. Against this, Fisher (1935a, 1955), Pearson, and other classical statisticians have argued for more epistemic interpretations, and many more recent authors have followed suit. In applications of statistics in the sciences, the Bayes factor has become an increasingly important measure of evidential strength (cf. Morey et al. 2016)[^morey-2016].

Central to the above discussion on classical statistics is the concept of likelihood, which reflects how the data bears on the hypotheses at issue. In the works of Hacking (1965), Edwards (1972), and more recently Royall (1997), the likelihoods are taken as a cornerstone for statistical procedures and given an epistemic interpretation. They are said to express the strength of the evidence presented by the data, or the comparative degree of support that the data give to a hypothesis. Hacking formulates this idea in the so-called law of likelihood (1965, p. 59): if the sample $s$ is more probable on the condition of $h_{0}$ than on $h_{1}$, then $s$ supports $h_{0}$ more than it supports $h_{1}$.

The position of likelihoodism is based on a specific combination of views on probability. On the one hand, it only employs probabilities over sample space, and avoids putting probabilities over statistical hypotheses. It thereby avoids the use of probability that cannot be given an ontic interpretation. On the other hand, it does interpret the probabilities over sample space as components of a support relation, and thereby as pertaining to the epistemic rather than the physical realm. Notably, the likelihoodist approach fits well with a long history in formal approaches to epistemology, in particular with confirmation theory (see the entry on confirmation), in which the probability theory is used to spell out confirmation relations between data and hypotheses. Measures of confirmation invariably take the likelihoods of hypotheses as input components. They provide a quantitative expression of the support relations described by the law of likelihood.

#### 3.3.2 Error statistics and severe testing

Another epistemic approach to classical statistics is presented by Mayo (1996, 2018) and Mayo and Spanos (2011). Over the past two decades, they have done much to push the agenda of classical statistics in the philosophy of science, which had become dominated by Bayesian statistics. Countering the original behaviourist tendencies of Neyman, the error statistical approach advances an epistemic reading of classical test and estimation procedures. Mayo and Spanos argue that classical procedures are best understood as inferential: they license inductive inferences. But they readily admit that the inferences are defeasible, i.e., they can lead us astray. Classical procedures are always associated with particular error probabilities, e.g., the probability of a false rejection or acceptance, or the probability of an estimator falling within a certain range. In the theory of Mayo and Spanos, these error probabilities obtain an epistemic role, because they are taken to indicate the reliability of the inferences licensed by the procedures.

The error statistical approach of Mayo and others comprises a general philosophy of science as well as a particular viewpoint on the philosophy statistics. We briefly focus on the latter, through a discussion of the notion of a severe test (cf. Mayo and Spanos 2006)[^mayo-2006][^mayo-2006-2]. The claim is that we gain knowledge of experimental effects on the basis of, what Mayo and others call, severely testing hypotheses, a concept that can be characterized by reference to the significance and power of the statistical tests involved. In Mayo’s definition, a hypothesis passes a severe test on two conditions: the hypothesis must agree with the data, and with high probability, if the hypothesis were in fact false, then it would not agree with the data. Ignoring potential controversy over the precise interpretation of “agreeing with the data” and “low probability”, we can recognize the tests characteristics of Neyman and Pearson in these conditions: a test can be called severe if the error rates are low. More precisely, we might say that an alternative hypothesis passes a severe test if the power is high, which somewhat resembles the condition that the alternative hypothesis agrees with the data: the data fall into a region with high probability according to the alternative hypothesis. Furthermore, the test is severe if the significance level of the test is low, which resembles the condition that if the alternative hypothesis is false, and hence some null hypothesis true, the probability that this null hypothesis agrees with the data is low, in the sense that the data fall into a region with low probability according to the null hypothesis.

There are, however, some differences between the criteria of Neyman and Pearson and the criterion of test severity that merit close attention. Importantly, Neyman and Pearson are concerned with test characteristics that derive from the probability assignments over sample space, as determined by the null and alternative hypotheses, and not with specific samples and specific instances of testing. The severity condition, by contrast, pertains to the particular sample obtained for a test: one condition for calling a test severe is that the alternative hypothesis must agree with the sample actually obtained. This condition does not exactly match the criterion of Neyman and Pearson testing that the power is high, as this pertains to the probability of the entire region of rejection according to the alternative hypothesis. A similar remark applies to the second condition of severity, which is that if the alternative hypothesis is false, then with high probability the data would probably not agree with it. As suggested this condition relates to the significance level of the test but it is not captured adequately by requiring that the probability of the whole region of rejection is low according to the null hypothesis, because we want the null hypothesis to give low probability to the data actually obtained. For this reason we can say that the second condition of severity is loosely expressed in the p-value, i.e., the maximal significance level at which a test can reject the null hypothesis for a given sample.

The error statistical approach shows similarities to the likelihoodist approach, in that it focuses on the evidence presented by a sample. It thereby differs from earlier views on classical statistics that motivate the procedures by reference to the frequency of success in a series of repeated applications. However, error statistics also differs from the likelihoodist approach, especially in what may be called its falsificationist orientation. The evidence presented by a statistical test or an estimation is not merely comparative, and there is no presumption that one of the hypotheses under consideration is true, or adequate, as is sometimes claimed about Bayesian statisics (e.g., Dawid 1982)[^dawid-1982][^dawid-1982-2]. Instead the error statistical approach leaves open that the data agrees with none of the hypotheses, reflecting that the assumptions of the procedures may be falsified and are open to revision. This fundamental openness to revision has inspired scholars across the board (e.g., Gelman and Shalizi 2013)[^gelman-2013][^gelman-2013-2].

#### 3.3.2 Theoretical developments

Apart from re-interpretations of the classical statistical procedures, numerous statisticians and philosophers have developed the theory of classical statistics further in order to make good on the epistemic role of its results. We focus on four developments in particular, to wit, fiducial, evidential, and game-theoretic probability, and the use of e-values rather than p-values.

The theory of evidential probability originates in Kyburg (1961), who developed a logical system to deal consistently with the results of classical statistical analyses. Evidential probability thus falls within the attempts to establish the epistemic use of classical statistics. Haenni et al (2010) and Kyburg and Teng (2001) present insightful introductions to evidential probability. The system is based on a version default reasoning: statistical hypotheses come attached with a confidence level, and logical rules organize how such confidence levels are propagated in inference, and thus advises which hypothesis to use for predictions and decisions. Particular attention is devoted to the propagation of confidence levels in inferences that involve multiple instances of the same hypothesis tagged with different confidences, where those confidences result from diverse data sets that are each associated with a particular population. Evidential probability assists in selecting the optimal confidence level, and thus in choosing the appropriate population for the case under consideration. In other words, evidential probability helps to resolve the reference class problem alluded in the foregoing.

Fiducial probability presents another way in which classical statistics can be given an epistemic status. Fisher (1930, 1933, 1935c, 1956/1973) developed the notion of fiducial probability as a way of deriving a probability assignment over hypotheses without assuming a prior probability over statistical hypotheses at the outset. The fiducial argument is controversial, and it is generally agreed that its applicability is limited to particular statistical problems. Dempster (1964), Hacking (1965), Edwards (1972), Seidenfeld (1996) and Zabell (1996) provide insightful discussions. Seidenfeld (1979) presents a particularly detailed study and a further discussion of the restricted applicability of the argument in cases with multiple parameters. Dawid and Stone (1982) argue that in order to run the fiducial argument, one has to assume that the statistical problem can be captured in a functional model that is smoothly invertible. Dempster (1966) provides generalizations of this idea for cases in which the distribution over $\theta$ is not fixed uniquely but only constrained within upper and lower bounds (cf. Hannig 2009, Haenni et al 2011)[^haenni-2011][^hannig-2009]. Crucially, such constraints on the probability distribution over values of $\theta$ are obtained without assuming any distribution over $\theta$ at the outset.

The idea of game-theoretic probability is a comparatively recent one in the development of classical statistics (Shafer and Vovk 2001 and 2019, Shafer 2021). The basic idea of this approach is to replace the categorical verdicts of failing and passing a statistical test by a gradual expression of agreement with the data in terms of bets and their payoffs. We start by viewing the distribution of the null hypothesis, $P_{h}(S)$, as a collection of betting offers by a bookie. A gambler is allowed to choose any payoff function $F(s) > 0$, which determines what they receive when observing $s$. The fair price for the collection of bets according to the bookie, as encoded in the null hypothesis, then is the expectation value:

$$ E_{P_{h}}(F) = \sum_{s \in W} P_{h}(s)F(s) $$

Say that the gambler buys the collection of bets for the fair price according to the null, and that they subsequently observe $s$ and receive the payoff $F(s)$. If this payoff is larger than the fair price, this counts as evidence against the null.

We can give a further interpretation of this payoff function as a measure of evidence. Setting $E_{P}(F) = 1$, we see that $P_{h'}(s) = P_{h}(s) F(s)$ is another probability distribution over $W$. We can associate this distribution with the alternative hypothesis $h'$. This turns the payoff function into the likelihood ratio for the two hypotheses,

$$ F(s) = \frac{P_{h'}(s)}{P_{h}(s)}\,. $$

As Shafer (2021) argues, the likelihood ratio expresses the payoff function that a gambler who adopts the alternative hypothesis $h'$ might choose, when buying a collection of bets from a bookie who adopts the null hypothesis $h$. The reason is that this optimizes on the growth rate of the betting revenues, and thus maximizes on a certain conception of epistemic gain. The likelihood ratio thus offers a natural expression of how strong the evidence is. However, for a betting conception of testing that allows us to express evidential strength, we need not necessarily adopt any hypothesis as the alternative, nor do we need to fix a payoff function in any particular way in order to reap the conceptual benefits. The betting understanding of testing is clearly classical in that it avoids an epistemic interpretation of the procedures or the payoffs, suggesting a decision- or game-theoretic interpretation instead. But it offers major advantages over traditional conceptions of testing, especially because it facilitates the build-up of statistical results across studies, where each study may choose its own payoff function.

The desideratum that we can combine and reuse statistical results in new contexts is a leading motivation for a related and very recent development within the classical statistical approach, namely the expression of the evidential impact of the data on statistical hypotheses in terms of so-called e-values (Grunwald 2023, 2024). Following the decision-theoretical outlook of Wald (1939), a central notion in this development is the loss *L* that is associated with hypotheses, denoted $h$, and actions, labelled by numbers $a$, for instance to reject or accept some hypothesis and take further action on that basis. Such a loss function helps us to weigh up type-I and type-II errors against each other, and eventually determines the decision to reject the null hypothesis and accept the alternative, or otherwise, depending on the data obtained.

E-values offer an alternative to the p-values that are often reported alongside a decision to reject the null hypothesis. The p-values indicate that we could have rejected the null hypothesis with a lower type-I error, and often serve as an expression of the strength of evidence against the null. But e-values have several properties that make them more attractive than p-values. For one, e-values are defined for collections of distributions rather than single ones, thus leaving room for composite hypotheses. Most importantly, e-values retain their evidential meaning under post-hoc changes to the loss function $L(h, a)$, including changes in the number of available actions and in the set of hypotheses under consideration. This is particularly relevant to cases in which, because of the data obtained, we wish to reconsider our statistical analysis and our decision context, or in which the data affect what actions are considered in the first place.

Crucial in the approach is the so-called e-variable, denoted $G$, defined by the requirement that $E_{P_{h}}(G) \leq 1$, where *h* is the null hypothesis. The e-variable is comparable to the payoff function $F$ in the game-theoretical approach to classical statistics discussed above. Assuming that the actions *a* are ordered so that the loss function $L(h, a)$increases monotonically in *a*, while $L(h', a)$ decreases monotonically in *a*, the decision rule is that we choose the action $a$ with maximal value for which

$$ L( h, a) \lt G(s) r , $$

in which $G(s)$ is the e-value of the observed sample $s$ and $r$ a level of maximally acceptable risk. A large e-value $G(s)$ expresses that the sample $s$ presents strong evidence against the null, so that a more extreme action can be chosen, because we are more certain of the falsity of the null hypothesis.

For comparing two simple hypotheses, a natural choice for the e-variable is the likelihood ratio, i.e., $G(s) = F(s)$, so that we select more extreme actions when our data presents stronger evidence. But the concept of an e-variable is much more general. We can reproduce the standard Neyman-Pearson test in this framework, and expand to other, more sophisticated test functions by choosing other e-variables. And we can define the notion of an *e-posterior*, replacing the confidence intervals detailed above by a notion that stands on firmer decision-theoretic grounds. However, while these are exciting new developments, the theory of e-values and e-posteriors has not yet achieved maturity and its applicability in practice has yet to be determined.

#### 3.3.3 Excursion: the fiducial argument

To explain the fiducial argument we first set up a simple example. Say that we estimate the mean $\theta$ of a normal distribution with unit variance over a variable $X$. We collect a sample $s$ consisting of measurements $X_{1}, X_{2}, \ldots X_{n}$. The maximum likelihood estimator for $\theta$ is the average value of the $X_{i}$, that is, $\hat{\theta}(s) = \sum_{i} X_{i} / n$. Under an assumed true value $\theta^{\star}$ we then have a normal distribution over the values of the estimator $\hat{\theta}(s)$, centred on the true value and with variance $1 / \sqrt{n}$. Notably, this distribution has the same shape for all values of $\theta^{\star}$. Fisher argued that we can therefore use the distribution for the estimator $\hat{\theta}(s)$ given the sample $s$ as a stand-in for the distribution over the true value $\theta^{\star}$, and derive a probability distribution $P_{\text{Fid}}(\theta^{\star})$ on the basis of a sample $s$, seemingly without assuming a prior probability.

There are several ways to clarify this so-called fiducial argument. One way employs a so-called functional model, i.e., the specification of a statistical model by means of a particular function relating statistical parameters and samples. For the above model, the function is

$$ f(\theta, \epsilon) = \theta + \epsilon = \hat{\theta}(s). $$

It relates possible parameter values $\theta$ to a quantity based on the sample, in this case the estimator of the observations $\hat{\theta}$. The two are related through a stochastic component $\epsilon$ whose distribution is known. In the example case, it is a Gaussian with a mean at $0$ and with variance $1 / \sqrt{n}$. Importantly, the distribution of $\epsilon$ is the same for every value of $\theta$. The interpretation of the function $f$ may now be apparent: relative to the choice of a value of $\theta$, which then takes the role of the true value $\theta^{\star}$, the distribution over $\epsilon$ dictates the distribution over the estimator function $\hat{\theta}(s)$.

The idea of the fiducial argument is to project the distribution over the stochastic component $\epsilon$ back onto the possible parameter values $\theta$. The key observation is that the functional relation $f(\theta, \epsilon)$ is smoothly invertible, i.e., the function

$$ f^{-1}(\hat{\theta}(s), \epsilon) = \hat{\theta}(s) - \epsilon = \theta $$

points each combination of $\hat{\theta}(s)$ and $\epsilon$ to a unique parameter value $\theta$. Hence, we can invert the claim of the previous paragraph: relative to fixing a value for $\hat{\theta}$, the distribution over $\epsilon$ fully determines the distribution over $\theta$. In virtue of the inverted functional model, we can therefore transfer the normal distribution over $\epsilon$ to the values $\theta$ around $\hat{\theta}(s)$. This yields a so-called fiducial probability distribution over the parameter $\theta$, denoted $P_{\text{Fid}}$. The distribution is obtained because, conditional on the value of the estimator, the parameters and the stochastic terms become perfectly correlated. A distribution over the latter is then automatically applicable to the former (cf. Haenni et al, 52–55 and 119–122).

Another way of explaining the same idea invokes the notion of a pivotal quantity. Because of how the above statistical model is set up, we can construct the pivotal quantity $\hat{\theta}(s) - \theta$. We know the distribution of this quantity since it is the distribution of $\epsilon$ , namely normal and with variance $1 / \sqrt{n}$. Moreover, this distribution is independent of the sample $s$, and it is such that, after observing the sample and thus fixing the value of $\hat{\theta}(s)$, it uniquely determines a distribution over the parameter values $\theta$. In sum, the fiducial argument allows us to construct a probability distribution over the parameter values on the basis of the observed sample. The argument can be run whenever we can construct a pivotal quantity or, equivalently, whenever we can express the statistical model as a functional model.

In order to properly appreciate the precise inferential move and its wobbly conceptual basis, it will be instructive to consider the use of fiducial probability in interpreting confidence intervals. As explained in Section 3.1.3, such intervals indicate the quality of an estimation but they are often mistakenly interpreted epistemically: the 95% confidence interval is often misunderstood as the range of parameter values that includes the true value with a confidence of 95% probability, a so-called 95% credal interval:

$$ P(\theta^{\star} \in [\hat{\theta} - \Delta, \hat{\theta} + \Delta]) = 0.95. $$

The idea to assign probabilities to possible values is in direct conflict with classical statistics. But the interpretation can be motivated by an application of the fiducial argument. Once we have computed the distribution $P_{\text{Fid}}(\theta)$, it becomes possible to express a fiducial interval with it, and determine the value of $\Delta$ such that $P_{\text{Fid}}(\theta^{\star} \in [\hat{\theta} - \Delta, \hat{\theta} + \Delta])$ adds up to a chosen confidence level $1 - \alpha$ . For the example above and for others amenable to the fiducial argument, the fiducial interval coincides numerically with the confidence interval, which might explain why the misinterpretation of confidence intervals is so pervasive.

A warning is in order: the fiducial argument is controversial and its proper interpretation is a matter of debate. The probabilities appearing in classical statistical methods are normally interpreted as frequencies of events, offering guarantees of low error rates when methods are applied repeatedly, while the probability distribution over hypotheses that is generated by a fiducial argument carries an epistemic interpretation. But it is not clear that we can take the distribution $P_{\text{Fid}}$ as an expression of our beliefs, nor that we may support the epistemic interpretation of confidence intervals with it. For this reason fiducial probability is perhaps best understood as a half-way house between the classical and the Bayesian view on statistics. Several authors (e.g., Dempster 1964)[^dempster-1964] have noted that fiducial probability indeed makes most sense in a Bayesian perspective. It is to this perspective that we now turn.

## 4. Bayesian statistics

Bayesian statistical methods are often presented in the form of an inference. The inference runs from a so-called prior probability distribution over statistical hypotheses, which expresses the degree of belief in the hypotheses before data has been collected, to a posterior probability distribution over the hypotheses, which expresses the beliefs after the data have been incorporated. The posterior distribution follows, via the axioms of probability theory, from the prior distribution and the likelihoods of the hypotheses for the data obtained, i.e., the probability that the hypotheses assign to the data. Bayesian methods thus employ data to modulate our attitude towards a designated set of statistical hypotheses. Viewed abstractly, both classical and Bayesian statistics present a response to the problem of induction. But whereas classical procedures select or eliminate elements from the set of hypotheses, Bayesian methods express the impact of data in a posterior probability assignment over the set.

The defining characteristic of Bayesian statistics is that it considers probability distributions over statistical hypotheses as well as over data. It thereby embraces the epistemic interpretation of probability: probabilities over hypotheses are interpreted as degrees of belief, i.e., as expressions of epistemic uncertainty. The philosophy of Bayesian statistics is concerned with determining the appropriate interpretation of these input components, and of the mathematical formalism of probability itself, ultimately with the aim to justify the output. Notice that the general pattern of a Bayesian statistical method is that of inductivism in the cumulative sense: under the impact of data we move to more and more informed probabilistic opinions about the hypotheses. However, in the following it will appear that Bayesian methods may also be understood as deductivist in nature.

### 4.1 Basic pattern of inference

Bayesian inference always starts from a statistical model, i.e., a set of statistical hypotheses. While the general pattern of inference is the same, we treat models with a finite number and a continuum of hypotheses separately and draw parallels with hypothesis testing and estimation, respectively. The exposition is mostly based on Earman 1992, Press 2002, Howson and Urbach 2006, and Gelman et al 2013.

#### 4.1.1 Finite model

Central to Bayesian methods is a theorem from probability theory known as Bayes’ theorem. Relative to a prior probability distribution over hypotheses, and the probability distributions over sample space for each hypothesis, it tells us what the adequate posterior probability over hypotheses is. More precisely, let $s$ be the sample and $S$ be the sample space as before, and let $M = \{ h_{\theta} :\: \theta \in \Theta \}$ be the model, i.e., the space of statistical hypotheses, with $\Theta$ the space of parameter values. The function $P$ is a probability distribution over the entire space $M \times S$, meaning that every element $h_{\theta}$ is associated with its own sample space $S$, and its own probability distribution over that space. For the latter, which is fully determined by the likelihoods of the hypotheses, we write the probability of the sample conditional on the hypothesis, $P(s \mid h_{\theta})$. This differs from the expression $P_{h_{\theta}}(s)$, written in the context of classical statistics, because in contrast to classical statisticians, Bayesians accept $h_{\theta}$ as an argument for the probability distribution.

Bayesian statistics is first introduced in the context of a finite set of hypotheses, after which a generalization to the infinite case is provided. Assume the prior probability $P(h_{\theta})$ over the hypotheses $h_{\theta} \in M$. Further assume the likelihoods $P(s \mid h_{\theta})$, i.e., the probability assigned to the data $s$ conditional on the hypotheses $h_{\theta}$. Then Bayes’ theorem determines that

$$ P(h_{\theta} \mid s) \; = \; \frac{P(s \mid h_{\theta})}{P(s)} P(h_{\theta}) . $$

Bayesian statistics outputs the posterior probability assignment, $P(h_{\theta} \mid s)$. This expression gets the interpretation of an opinion concerning $h_{\theta}$ after the sample $s$ has been recorded accommodated, i.e., it is a revised opinion. Further results from a Bayesian inference can all be derived from the posterior distribution over the statistical hypotheses. For instance, we can use the posterior to determine the most probable value for the parameter, i.e., picking the hypothesis $h_{\theta}$ for which $P(h_{\theta} \mid s)$ is maximal.

In this characterization of Bayesian statistical inference the probability of the data $P(s)$ is not presupposed, because it can be computed from the prior and the likelihoods by the law of total probability,

$$ P(s) \; = \; \sum_{\theta \in \Theta} P(h_{\theta}) P(s \mid h_{\theta}) . $$

This expression is often called the marginal likelihood of the model: it expresses how probable the data is in the light of the model as a whole. The result of a Bayesian statistical inference is not always reported as a posterior probability. Often the interest is only in comparing the ratio of the posteriors of two hypotheses. By Bayes’ theorem we have

$$ \frac{P(h_{\theta} \mid s)}{P(h_{\theta'} \mid s)} \; = \; \frac{P(h_{\theta}) P(s \mid h_{\theta})}{P(h_{\theta'}) P(s \mid h_{\theta'})} , $$

and if we assume equal priors $P(h_{\theta}) = P(h_{\theta'})$, we can use the ratio of the likelihoods of the hypotheses, the so-called Bayes factor, to compare the hypotheses.

Here is a Bayesian procedure for the example of the tea tasting student.

> **Bayesian statistical analysis**
> In the tea tasting example, consider the hypotheses $h_{1/2}$ and $h_{3/4}$, which in the foregoing were used as null and alternative, $h$ and $h'$, respectively. Instead of choosing among them on the basis of the data, we assign a prior distribution over them so that the null is twice as probable as the alternative: $P(h_{1/2}) = 2/3$ and $P(h_{3/4}) = 1/3$. Denoting a particular sequence of guessing $n$ out of 5 cups correctly with $s_{n/5}$, we have that $P(s_{n/5} \mid h_{1/2}) = 1 / 2^{5}$ while $P(s_{n/5} \mid h_{3/4}) = 3^{n} / 4^{5}$. As before, the likelihood ratio of five guesses thus becomes
>
> $$ \frac{P(s_{n/5} \mid h_{3/4})}{P(s_{n/5} \mid h_{1/2})} \; = \; \frac{3^{n}}{2^{5}} . $$
>
> The posterior ratio after 5 correct guesses is thus
>
> $$ \frac{P(h_{3/4} \mid s_{n/5})}{P(h_{1/2} \mid s_{n/5})} \; = \; \frac{3^{5}}{2^{5}}\, \frac{1}{2} \approx 4 . $$
>
> This posterior is derived by the axioms of probability theory alone, in particular by Bayes’ theorem. It tells us how believable each of the hypotheses is after incorporating the sample data into our beliefs.

Notice that in the above exposition, the posterior probability is written as $P(h_{\theta} \mid s_{n/5})$. Some expositions of Bayesian inference prefer to express the revised opinion as a new probability function $P_{s}( \cdot )$, which is then equated to the old probability conditional on the sample, $P( \cdot \mid s)$. For the basic formal workings of Bayesian inference, this distinction is inessential. But we will return to it in Section 4.3.3.

#### 4.1.2 Continuous model

In many applications the model is not a finite set of hypotheses, but rather a continuum labelled by a real-valued parameter. This leads to some subtle changes in the definition of the distribution over hypotheses and the likelihoods. The prior and posterior must be written down as a so-called probability density function, denoted with the lowercase $p(h_{\theta})$, such that for any set of hypotheses $M$ we can write

$$P(M) = \int_{M} p(h_{\theta}) d\theta , $$

where $P$ is again an ordinary probability function. Accordingly, $P(h_{\theta}) = p(h_{\theta}) d\theta$ is the infinitely small probability assigned to an infinitely small patch $d\theta$ around the point $\theta$.

The likelihoods need to be defined by a limit process: the probability $P(h_{\theta})$ is infinitely small so that we cannot define $P(s \mid h_{\theta})$ in the normal manner. But other than that the Bayesian machinery works exactly the same:

$$ P(h_{\theta} \mid s) d\theta \;\; = \;\; \frac{P(s \mid h_{\theta})}{P(s)} P(h_{\theta}) d\theta. $$

Finally, summations need to be replaced by integrations:

$$ P(s) \; = \; \int_{\theta \in \Theta} P(h_{\theta}) P(s \mid h_{\theta}) d\theta . $$

This is again the marginal likelihood of the model, computed by the law of total probability.

The posterior probability density provides a basis for conclusions that one might draw from the sample $s$, and which are similar to estimations and measures for the accuracy of the estimations. For one, we can derive an expectation for the parameter $\theta$, where we assume that $\theta$ varies continuously:

$$ \bar{\theta} \;\; = \;\; \int_{\Theta}\, \theta P(h_{\theta} \mid s) d\theta. $$

If the model is parameterized by a convex set, which it typically is, then there will be a hypothesis $h_{\bar{\theta}}$ in the model. This hypothesis can serve as a Bayesian estimation. An alternative notion of estimation uses the mode of the posterior distribution, i.e., the value of $\theta$ where the posterior is maximal. In analogy to the confidence interval, we can also define the credal interval or credibility interval from the posterior probability distribution: an interval of size $2d$ around the expectation value $\bar{\theta}$, written $[\bar{\theta} - d, \bar{\theta} + d]$, such that

$$ \int_{\bar{\theta} - d}^{\bar{\theta} + d} P(h_{\theta} \mid s) d\theta = 1-\epsilon . $$

This range of values for $\theta$ is such that the posterior probability of the corresponding $h_{\theta}$ adds up to $1-\epsilon$ of the total posterior probability.

There are many other ways of defining Bayesian estimations and credal intervals for $\theta$ on the basis of the posterior density. The specific type of estimation that the Bayesian analysis offers can be determined by the demands of the scientist. Any Bayesian estimation will to some extent resemble the maximum likelihood estimator due to the central role of the likelihoods in the Bayesian formalism. However, the output will also depend on the prior probability over the hypotheses, and generally speaking it will only tend to the maximum likelihood estimator when the sample size tends to infinity. See Section 4.2.2 for more on this so-called “washing out” of the priors.

### 4.2 Problems with the Bayesian approach

Most of the controversy over the Bayesian method concerns the probability assignment over hypotheses. One important set of problems surrounds the interpretation of those probabilities as beliefs, as to do with a willingness to act, or the like. Another set of problems pertains to the determination of the prior probability assignment, and the criteria that might govern it.

#### 4.2.1 Interpretations of the probability over hypotheses

The overall question here is how we should understand the probability assigned to a statistical hypothesis. Naturally the interpretation will be epistemic: the probability expresses the strength of belief in the hypothesis. It makes little sense to attempt a physical interpretation since the hypothesis cannot be seen as a repeatable event, or as an event that might have some tendency of occurring.

This leaves open several interpretations of the probability assignment as a strength of belief. One very influential interpretation of probability as degree of belief relates probability to a willingness to bet against certain odds (cf. Ramsey 1926, De Finetti 1937/1964, Earman 1992, Jeffrey 1992, Howson 2000)[^de-1937][^earman-1992][^howson-2000][^jeffrey-1992][^ramsey-1926]. According to this interpretation, assigning a probability of $3/4$ to a proposition, for example, means that we are prepared to pay at most $0.75 for a betting contract that pays out $1 if the proposition is true, and that turns worthless if the proposition is false. The claim that degrees of belief are correctly expressed in a probability assignment is then supported by a so-called *Dutch book argument*: if an agent does not comply to the axioms of probability theory, a malign bookmaker can propose a set of bets that seems fair to the agent but that lead to a certain monetary loss, and that is therefore called Dutch, presumably owing to the Dutch’s mercantile reputation. This interpretation associates beliefs directly with their behavioral consequences: believing something is the same as having the willingness to engage in a particular activity, e.g., in a bet.

There are several problems with this interpretation of the probability assignment over hypotheses. For one, it seems to make little sense to bet on the truth of a statistical hypothesis, because such hypotheses cannot be falsified or verified. Consequently, a betting contract on them will never be cashed. More generally, it is not clear that beliefs about statistical hypotheses are properly framed by connecting them to behavior (cf. Armendt 1993)[^armendt-1993]. This way of framing probability assignments introduces pragmatic considerations on beliefs, to do with navigating the world successfully, into a setting that may be more concerned with belief as a truthful representation of the world.

A somewhat different problem is that the Bayesian formalism, in particular its use of probability assignments over statistical hypotheses, suggests a remarkable closed-mindedness on the part of the Bayesian statistician. Recall the example of the foregoing, with the model $M = \{ h_{1/2}, h_{3/4} \}$. The Bayesian formalism requires that we assign a probability distribution over these two hypotheses, and further that the probability of the model is $P(M) = 1$. It is quite a strong assumption, even of an ideally rational agent, that she is indeed equipped with a real-valued function that expresses her opinion over the hypotheses. Moreover, the probability assignment over hypotheses seems to entail that the Bayesian statistician is certain that the true hypothesis is included in the model. This is an unduly strong claim to which a Bayesian statistician will have to commit at the start of her analysis. It sits badly with broadly shared methodological insights (e.g., Popper 1934/1956)[^popper-1934], according to which scientific theory must be open to revision at all times (cf. Mayo 1996)[^mayo-1996]. In its standard form, Bayesian statistics does not do justice to the nature of scientific inquiry.

The problem just outlined obtains a mathematically more sophisticated form in the problem that Bayesians expect to be well-calibrated. This problem, as formulated in Dawid (1982), concerns a Bayesian forecaster, e.g., a weatherman who determines a daily probability for precipitation in the next day. It is then shown that such a weatherman believes of himself that in the long run he will converge onto the correct probability with certainty. Yet it seems reasonable to suppose that the weatherman realizes something could potentially be wrong with his meteorological model, and so sets his probability for correct prediction below 1. The weatherman is thus led to incoherent beliefs. It seems that Bayesian statistical analysis places unrealistic demands, even on an ideal agent.

#### 4.2.2 Determination of the prior

Assuming that we have settled on a statistical model and that we can interpret the probability over it as an expression of epistemic uncertainty, how do we determine a prior probability? Perhaps we already have an intuitive judgment on the hypotheses in the model, so that we can pin down the prior probability on that basis. Or else we might have additional criteria for choosing our prior. However, several problems attach to procedures for determining the prior.

First consider the idea that the scientist who runs the Bayesian analysis provides the prior probability herself. One obvious problem with this idea is that the opinion of the scientist might not be precise enough for a determination of a full prior distribution. It does not seem realistic to suppose that the scientist can transform her opinion into a single real-valued function over the model, especially not if the model itself consists of a continuum of hypotheses. But the more pressing problem is that different scientists will provide different prior distributions, and that these different priors will lead to different statistical results. In other words, Bayesian statistical inference introduces an inevitable subjective component into scientific method.

It is one thing that the statistical results depend on the initial opinion of the scientist. But it may so happen that the scientist has no opinion whatsoever about the hypotheses. How is she supposed to assign a prior probability to the hypotheses then? The prior will have to express her ignorance concerning the hypotheses. The leading idea in expressing such ignorance is usually the principle of indifference: ignorance means that we are indifferent between any pair of hypotheses. For a finite number of hypotheses, indifference means that every hypothesis gets equal probability. For a continuum of hypotheses, indifference means that the probability density function must be uniform.

Nevertheless, there are different ways of applying the principle of indifference and so there are different probability distributions over the hypotheses that can count as expression of ignorance. This insight is nicely illustrated in Bertrand’s paradox .

> **Bertrand’s paradox**
> Consider a circle drawn through the corners of an equilateral triangle, and imagine that a knitting needle whose length exceeds the circle’s diameter is thrown onto the circle. What is the probability that the section of the needle lying within the circle is longer than the side of the equilateral triangle? To determine the answer, we need to parameterize the ways in which the needle may be thrown, determine the subset of parameter values for which the included section is indeed longer than the triangle’s side, and express our ignorance over the exact throw of the needle in a probability distribution over the parameter, so that the probability of the said event can be derived. The problem is that we may provide any number of ways to parameterize how the needle lands in the circle. If we use the angle that the needle makes with the tangent of the circle at the intersection with one of the triangle’s corners, then the included section of the needle is only going to be longer if the angle is between $60^{\circ}$ and $120^{\circ}$. If we assume that our ignorance is expressed by a uniform distribution over these angles, which ranges from $0^{\circ}$ to $180^{\circ}$, then the probability of the event is going to be $1/3$. However, we can also parameterize the ways in which the needle lands differently, namely by the shortest distance of the needle to the centre of the circle. A uniform probability over the distances will lead to a probability of $1/2$. Finally, parameterizing the needle’s position by the location of its midpoint will lead us to assign the same event a probability of $1/4$.

Jaynes (1973 and 2003) provides a very insightful discussion of this riddle and also argues that it may be resolved by relying on invariances of the problem under certain transformations. But the general message for now is that the principle of indifference does not automaticallylead to a unique choice of priors. The point is not that ignorance concerning a parameter is hard to express in a probability distribution over those values. It is rather that in some cases, we do not even know what parameters to use to express our ignorance over.

In part the problem of the subjectivity of Bayesian analysis may be resolved by taking a different attitude to scientific theory, and by giving up the ideal of absolute objectivity. Indeed, some will argue that it is just right that the statistical methods accommodate differences of opinion among scientists. However, this response misses the mark if the prior distribution expresses ignorance rather than opinion: it seems harder to defend the rationality of differences of opinion that stem from different ways of spelling out ignorance. Now there is also a more positive answer to worries over objectivity, based on so-called convergence results (e.g., Blackwell and Dubins 1962, Gaifman and Snir 1982)[^blackwell-1962][^gaifman-1982]. It turns out that the impact of prior choice diminishes with the accumulation of data, and that in the limit the posterior distribution will converge to a set, possibly a singleton, of best hypotheses, determined by the sampled data and hence completely independent of the prior distribution. However, in the short and medium run the influence of subjective prior choice remains.

For better or worse, Bayesian statistics is sensitive to subjective input. The undeniable advantage of the classical statistical procedures is that they do not need any such input, although arguably the classical procedures are in turn sensitive to choices concerning the sample space (Lindley 2000)[^lindley-2000]. Against this, Bayesian statisticians point to the advantage of being able to incorporate evidentially relevantinitial opinions into the statistical analysis.

### 4.3 Responses to criticism

The philosophy of Bayesian statistics offers a wide range of responses to the problems outlined above. Some Bayesians bite the bullet and defend the essentially subjective character of Bayesian methods. Others attempt to remedy or compensate for the subjectivity, by providing objectively motivated means of determining the prior probability or by emphasizing the objective character of the Bayesian formalism itself.

#### 4.3.1 Strict but empirically informed subjectivism

One very influential view on Bayesian statistics buys into the subjectivity of the analysis (e.g., Goldstein 2006, Kadane 2011)[^goldstein-2006][^kadane-2011]. So-called personalists or strict subjectivists argue that it is just right that the statistical methods do not provide any objective guidelines, pointing to radically subjective sources of any form of knowledge. The problems on the interpretation and choice of the prior distribution are thus dissolved, at least in part: the Bayesian statistician may choose her prior at will, and they are an expression of her beliefs. However, it deserves emphasis that a subjectivist view on Bayesian statistics does not mean that all constraints deriving from empirical fact can be disregarded. Nobody denies that if you have further knowledge that imposes constraints on the model or the prior, then those constraints must be accommodated. For example, today’s posterior probability may be used as tomorrow’s prior, in the next statistical inference. The point is that such constraints concern the rationality of belief and not the consistency of the statistical inference per se.

Subjectivist views are most prominent among those who interpret probability assignments in a pragmatic fashion, and motivate the representation of belief with probability assignments by the afore-mentioned Dutch book arguments. Central to this approach is the work of Savage and De Finetti. Savage (1962) proposed to axiomatize statistics in tandem with decision theory, a mathematical theory about practical rationality. He argued that by themselves the probability assignments do not mean anything at all, and that they can only be interpreted in the context where an agent faces a choice between actions, i.e., a choice among a set of bets. In similar vein, De Finetti (e.g., 1974) advocated a view on statistics in which only the empirical consequences of the probabilistic beliefs, expressed in a willingness to bet, mattered, although he did not make statistical inference fully dependent on decision theory. While the approaches differ a great deal, it appears that the subjectivist view on Bayesian statistics is based on the same behaviorism and empiricism that motivated Neyman and Pearson to develop classical statistics.

Notice that all this makes one aspect of the interpretation problem of Section 4.2.1 reappear: how will the prior distribution over hypotheses make itself apparent in behavior, so that it can rightfully be interpreted in terms of belief, here understood as a willingness to act? One response to this question is to turn to different motivations for representing degrees of beliefs by means of probability assignments. Following work by De Finetti, several authors have proposed vindications of probabilistic expressions of belief that are not based on behavioral goals, but rather on the epistemic goal of holding beliefs that accurately represent the world, e.g., Rosenkrantz (1981), Joyce (1998), Leitgeb and Pettigrew (2010a and 2010b), Easwaran (2013). A strong generalization of this idea is achieved in Schervish, Seidenfeld and Kadane (2009), which builds on a longer tradition of using scoring rules for achieving statistical aims like calibration or accurate prediction. An alternative approach is that any formal representation of belief must respect certain logical constraints, e.g., Cox (1961) provides an argument for the expression of belief in terms of probability assignments on the basis of the nature of partial belief per se.

The original subjectivist response to the issue that a prior over hypotheses is hard to interpret came from De Finetti’s so-called representation theorem, which shows that every prior distribution can be associated with its own set of predictions, and hence with its own behavioral consequences. In other words, De Finetti showed how priors are indeed associated with beliefs that can carry a betting interpretation, so that the prior over the hypotheses can be understood in empiricist terms after all.

#### 4.3.2 Excursion: the representation theorem

De Finetti’s representation theorem relates rules for prediction, as functions of the given sample data, to Bayesian statistical analyses of those data, against the background of a statistical model. See Festa (1996) and Suppes (2001) for useful introductions. De Finetti considers a process that generates a series of time-indexed observations, and he then studies prediction rules that take these finite segments as input and return a probability over future events, using a statistical model that can analyze such samples and provide the predictions. The key result of De Finetti is that a particular statistical model, namely the set of all distributions in which the observations are independently and identically distributed, can be equated with the class of exchangeable prediction rules, namely the rules whose predictions do not depend on the order in which the observations come in.

Let us consider the representation theorem in some more formal detail. For simplicity, say that the process generates time-indexed binary observations, i.e., 0s and 1s. The prediction rules take such bit strings of length $t$, denoted $S_{t}$, as input, and return a probability for the event that the next bit in the string is a 1, denoted $Q^{1}_{t+1}$. So we write the prediction rules as partial probability assignments $P(Q^{1}_{t+1} \mid S_{t})$. Exchangeable prediction rules are rules that deliver the same prediction independently of the order of the bits in the string $S_{t}$. If we write the event that the string $S_{t}$ has a total of $n$ observations of 1s as $S_{n/t}$, then exchangeable prediction rules are written as $P(Q^{1}_{t+1} \mid S_{n/t})$. The crucial property is that the value of the prediction is not affected by the order in which the 0s and 1s show up in the string $S_{t}$.

De Finetti relates this particular set of exchangeable prediction rules to a Bayesian inference over a specific type of statistical model. The model that De Finetti considers comprises the so-called Bernoulli hypotheses $h_{\theta}$, i.e., hypotheses for which

$$ P(Q^{1}_{t+1} \mid h_{\theta} \cap S_{t}) = \theta . $$

This likelihood does not depend on the string $S_{t}$ that has gone before. The hypotheses are best thought of as determining a fixed bias $\theta$ for the binary process, where $\theta \in \Theta = [0, 1]$. The representation theorem states that there is a one-to-one mapping of priors over Bernoulli hypotheses and exchangeable prediction rules. That is, every prior distribution $P(h_{\theta})$ can be associated with exactly one exchangeable prediction rule $P(Q^{1}_{t+1} \mid S_{n/t})$, and conversely. Next to the original representation theorem derived by De Finetti, several other and more general representation theorems were proved, e.g., for partially exchangeable sequences and hypotheses on Markov processes (Diaconis and Freedman 1980, Skyrms 1991)[^diaconis-1980][^skyrms-1991], for clustering predictions and partitioning processes (Kingman 1975 and 1978)[^kingman-1975][^kingman-1978], and even for sequences of graphs and their generating process (Aldous 1981)[^aldous-1981].

Representation theorems equate a prior distribution over statistical hypotheses to a prediction rule, and thus to a probability assignment that can be given a subjective and behavioral interpretation. This removes the worry expressed above, that the prior distribution over hypotheses cannot be interpreted subjectively because it cannot be related to belief as a willingness to act: priors relate uniquely to particular predictions. However, for De Finetti the representation theorem provided a reason for doing away with statistical hypotheses altogether, and hence for the removal of a notion of probability as anything other than subjective opinion (cf. Hintikka 1970)[^hintikka-1970]: hypotheses whose probabilistic claims could be taken to refer to intangible chancy processes are superfluous metaphysical baggage.

Not all subjectivists are equally dismissive of the use of statistical hypotheses. Jeffrey (1992) has proposed so-called mixed Bayesianism in which subjectively interpreted distributions over the hypotheses are combined with a physical interpretation of the distributions that hypotheses define over sample space. Romeijn (2003, 2005, 2006) argues that priors over hypotheses are an efficient and intuitive way of determining inductive predictions than specifying properties of predictive systems directly. This seems in agreement with the practice of science, in which hypotheses are routinely used, and often motivated by mechanistic knowledge on the data generating process.

#### 4.3.3 Bayesian statistics as logic

Despite the arguably subjective character of the prior, there is a sense in which Bayesian statistics might lay claim to objectivity. It can be shown that the Bayesian formalism meets certain objective criteria of rationality, coherence, and calibration. Bayesian statistics thus answers to the requirement of objectivity at a meta-level: while the opinions that it deals with retain a subjective aspect, the way in which it deals with these opinions, in particular the way in which data impacts on them, is objectively correct, or so it is argued. Arguments supporting the Bayesian way of accommodating data, namely by conditionalization, have been provided in a pragmatic context by dynamic Dutch book arguments, whereby probability is interpreted as a willingness to bet (cf. Maher 1993, van Fraassen 1989)[^fraassen-1989][^maher-1993]. Similar arguments have been advanced on the grounds that our beliefs must accurately represent the world along the lines of De Finetti (1974), e.g., Greaves and Wallace (2006) and Leitgeb and Pettigrew (2010).

An important distinction must be made in arguments that support the Bayesian way of accommodating evidence, namely between the mathematical fact of Bayes’ theorem, as introduced in section 4.1.1, and the epistemic principle of Bayes’ rule, which ensures the coherence of belief states over time. The theorem is simply a relation among probability assignments, and as such not subject to debate. Arguments that support the representation of the epistemic state of an agent by means of probability assignments also provide support for Bayes’ theorem as a constraint on degrees of belief. The conditional probability $P(h \mid s)$ can be interpreted as the degree of belief attached to the hypothesis $h$ on the supposition that the sample $s$ is obtained. Bayes’ rule, by contrast, presents a constraint on probability assignments that represent epistemic states of an agent at different points in time. It is written as

$$ P_{s}(h) \; = P(h \mid s) , $$

and it determines that the new probability assignment, expressing the epistemic state of the agent after the sample has been obtained, is systematically related to the old assignment, representing the epistemic state before the sample came in. In the philosophy of statistics many Bayesians adopt Bayes’ rule implicitly, and in the philosophical debate over learning Bayes’ rule is a central tenet (cf. Huttegger 2017)[^huttegger-2017]. But in what follows we will assume that Bayesian statistical inferences rely on Bayes’ theorem only.

Whether the focus lies on Bayes’ rule or on Bayes’ theorem, the common theme in the above-mentioned arguments is that they approach Bayesian statistical inference from a logical angle, and focus on its internal coherence or consistency (cf. Howson 2003)[^howson-2003]. While its use in statistics is undeniably inductive, Bayesian inference thereby obtains a deductive, or at least non-ampliative character: everything that is concluded in the inference is somehow already present in the premises. In Bayesian statistical inference, those premises are given by the prior over the hypotheses, $P(h_{\theta})$ for $\theta \in \Theta$, and the likelihood functions, $P(s \mid h_{\theta})$, as determined for each hypothesis $h_{\theta}$ separately. These premises fix a single probability assignment over the space $M \times S$ at the outset of the inference. The conclusions, in turn, are straightforward consequences of this probability assignment. They can be derived by applying theorems of probability theory, most notably Bayes’ theorem. Bayesian statistical inference thus becomes an instance of probabilistic logic (cf. Hailperin 1986, Halpern 2003, Haenni *et al* 2011)[^haenni-2011][^halpern-2003].

Summing up, there are several arguments showing that statistical inference by Bayes’ theorem, or by Bayes’ rule, is objectively correct. These arguments invite us to consider Bayesian statistics as an instance of probabilistic logic. Appeals to the logicality of Bayesian statistical inference may provide a partial remedy for its subjective character. Moreover, a logical approach to the statistical inferences avoids the problem that the formalism places unrealistic demands on the agents, and that it presumes the agent to have certain knowledge. Much like in deductive logic, we need not assume that the inferences are psychologically realistic, nor that the agents actually believe the premises of the arguments. Rather the arguments present the agents with a normative ideal and take the conditional form of consistency constraints: if you accept the premises, then these conclusions follow.

#### 4.3.4 Excursion: inductive logic and statistics

An important instance of probabilistic logic is presented in inductive logic, as devised by Carnap, Hintikka and others (Carnap 1950 and 1952, Hintikka and Suppes 1966, Carnap and Jeffrey 1970, Kuipers 1978, Hintikka and Niiniluoto 1980, Paris 1994, Skyrms 1999, Nix and Paris 2006, Paris and Waterhouse 2009, Paris and Vencovská 2015)[^carnap-1950][^carnap-1952][^carnap-1970][^hintikka-1970][^hintikka-1980][^hintikka-1966][^kuipers-1978][^nix-2006][^paris-1994][^paris-2009][^skyrms-1999]. Historically, Carnapian inductive logic developed prior to the probabilistic logics referenced above, and more or less separately from the debates in the philosophy of statistics. But the logical systems of Carnap can quite easily be placed in the context of a logical approach to Bayesian inference, and doing this is in fact quite insightful.

For simplicity, we choose a setting that is similar to the one used in the exposition of the representation theorem, namely a binary data generating process, i.e., strings of 0s and 1s. A prediction rule determines a probability for the event, denoted $Q^{1}_{t+1}$, that the next bit in the string is a 1, on the basis of a given string of bits with length $t$, denoted by $S_{t}$. Carnap and followers designed specific exchangeable prediction rules, mostly variants of the straight rule (Reichenbach 1938)[^reichenbach-1938],

$$ P(Q^{1}_{t+1} \mid S_{n/t}) = \frac{n + 1}{t + 2} , $$

where $S_{n/t}$ denotes a string of length $t$ of which $n$ entries are 1s. Carnap derived such rules from constraints on the probability assignments over the samples. Some of these constraints boil down to the axioms of probability. Other constraints, exchangeability among them, are independently motivated, by an appeal to so-called logical interpretation of probability. Under this logical interpretation, the probability assignment must respect certain invariances under transformations of the sample space, in analogy to logical principles that constrain truth valuations over a language in a particular way.

Carnapian inductive logic is an instance of probabilistic logic, because its sequential predictions are all based on a single probability assignment at the outset, and because it relies on Bayes’ theorem to adapt the predictions to sample data (cf. Romeijn 2011)[^romeijn-2011]. One important difference with Bayesian statistical inference is that, for Carnap, the probability assignment specified at the outset only ranges over samples and not over hypotheses. However, by De Finetti’s representation theorem Carnap’s exchangeable rules can be equated to particular Bayesian statistical inferences. A further difference is that Carnapian inductive logic gives preferred status to particular exchangeable rules. In view of De Finetti’s representation theorem, this comes down to the choice for a particular set of preferred priors. As further developed below, Carnapian inductive logic is thus related to objective Bayesian statistics. It is a moot point whether further constraints on the probability assignments can be considered as logical, as Carnap and followers have it, or whether the title of logic is best reserved for the probability formalism in isolation, as De Finetti and followers argue.

#### 4.3.5 Objective priors

A further set of responses to the subjectivity of Bayesian statistical inference targets the prior distribution directly: we might provide further rationality principles, with which the choice of priors can be chosen objectively. The literature proposes several objective criteria for filling in the prior over the model. Each of these lays claim to being the correct expression of complete ignorance concerning the value of the model parameters, or of minimal information regarding the parameters. Three such criteria are discussed here.

In the context of Bertrand’s paradox we already discussed the principle of indifference, according to which probability should be distributed evenly over the available possibilities. A further development of this idea is presented by the requirement that a distribution should have maximum entropy. Notably, the use of entropy maximization for determining degrees of beliefs finds much broader application than only in statistics: similar ideas are taken up in diverse fields like epistemology (e.g., Shore and Johnson 1980, Williams 1980, Uffink 1996, and also Williamson 2010)[^shore-1980][^uffink-1996][^williams-1980][^williamson-2010], inductive logic (Paris and Vencovska 1989)[^paris-1989], statistical mechanics (Jaynes 2003)[^jaynes-2003] and decision theory (Seidenfeld 1986, Grunwald and Halpern 2004)[^seidenfeld-1986]. In *objective Bayesian statistics*, the idea is applied to the prior distribution over the model (cf. Berger 2006)[^berger-2006]. For a finite number of hypotheses the entropy of the distribution $P(h_{\theta})$ is defined as

$$ E[P] \; = \; \sum_{\theta \in \Theta} P(h_{\theta}) \log P(h_{\theta}) . $$

This requirement leads to equiprobable hypotheses. However, for continuous models the maximum entropy distribution depends crucially on the metric over the parameters in the model. The burden of subjectivity is thereby moved to the parameterization. But it may well be that we have strong reasons for preferring a particular parameterization over others (cf. Jaynes 1973)[^jaynes-1973].

There are other approaches to the objective determination of priors. In view of the above problems, a particularly attractive method for choosing a prior over a continuous model is proposed by Jeffreys (1961). The general idea of so-called Jeffreys priors is that the prior probability assigned to a small patch in the parameter space is proportional to, what may be called, the density of the distributions within that patch. Intuitively, if a lot of distributions, i.e., distributions that differ among themselves, are packed together on a small patch in the parameter space as measured by the base metric, this patch should be given a larger prior probability than a similar patch within which there is little variation among the distributions (cf. Balasubramanian 2005)[^balasubramanian-2005]. More technically, such a density is expressed by a prior distribution that is proportional to the Fisher information. A key advantage of these priors is that they are invariant under reparameterizations of the parameter space: a new parameterization naturally leads to an adjusted density of distributions.

A final method of defining priors goes under the name of reference priors (Berger et al 2009)[^berger-2009]. The proposal starts from the observation that we should minimize the subjectivity of the results of our statistical analysis, and hence that we should minimize the impact of the prior probability on the posterior. The idea of reference priors is exactly that it will allow the sample data a maximal say in the posterior distribution. But since at the outset we do not know what sample we will obtain, the prior is chosen so as to maximize the expected impact of the data. Of course this expectation must itself be taken with respect to some distribution over sample space, and some associated measure of impact.

#### 4.3.6 Generalizing or revising priors

A different response to the subjectivity of priors is to extend the Bayesian formalism, in order to leave the choice of prior to some extent open. The subjective choice of a prior is in that case generalized away from, or made subject to alteration. Three such responses will be considered.

Recall that a prior probability distribution over statistical hypotheses expresses our uncertain opinion on which of the hypotheses is right. The central idea behind hierarchical Bayesian models (Gelman et al 2013)[^gelman-2013][^gelman-2013-2] is that the same pattern of putting a prior over statistical hypotheses can be repeated on the level of priors itself. More precisely, we may be uncertain over which prior probability distribution over the hypotheses is right. If we characterize possible priors by means of a set of parameters, we can express this uncertainty about prior choice in a probability distribution over the parameters that characterize the shape of the prior. In other words, we move our uncertainty one level up in a hierarchy: we consider multiple priors over the statistical hypotheses, and compare the performance of these priors on the sample data as if the priors were themselves hypotheses.

The idea of hierarchical Bayesian modeling (Gelman et al 2013)[^gelman-2013][^gelman-2013-2] relates naturally to the Bayesian comparison of Carnapian prediction rules (e.g., Skyrms 1993 and 1996, Festa 1996)[^festa-1996][^skyrms-1993][^skyrms-1996], and also to the estimation of optimum inductive methods (Kuipers 1986, Festa 1993)[^festa-1993][^kuipers-1986]. Hierarchical Bayesian modeling can also be related to another tool for choosing a particular prior distribution over hypotheses, namely the method of empirical Bayes, which estimates the prior that leads to the maximal marginal likelihood of the model. In the philosophy of science, hierarchical Bayesian modeling has made a first appearance due to Henderson et al. (2010).

There is also a response that avoids the choice of a prior altogether. This response starts with the same idea as hierarchical models: rather than considering a single prior over the hypotheses in the model, we consider a parameterized set of them. But instead of defining a distribution over this set, proponents of interval-valued or imprecise probability claim that our epistemic state regarding the priors is better expressed by this set of distributions, and that sharp probability assignments must therefore be replaced by lower and upper bounds to the assignments. Now the idea that uncertain opinion is best captured by a set of probability assignments, or a credal set for short, has a long history and is backed by an extensive literature (e.g., De Finetti 1974, Levi 1980, Dempster 1967 and 1968, Shafer 1976, Walley 1991, Augustin et al 2014)[^de-1974][^dempster-1967][^dempster-1968][^levi-1980][^shafer-1976][^walley-1991]. In light of the main debate in the philosophy of statistics, the use of interval-valued priors indeed forms an attractive extension of Bayesian statistics: it allows us to refrain from choosing a specific prior, and thereby presents a rapprochement to the classical view on statistics.

These theoretical developments are attractive but sadly they mostly enjoy a cult status among philosophers of statistics and that they have not moved the applied statistician in the street. On the other hand, standard Bayesian statistics has seen a steep rise in popularity over the past decade or so, owing to the availability of good software and numerical approximation methods. And most of the practical use of Bayesian statistics is more or less insensitive to the potentially subjective aspects of the statistical results, employing uniform priors as a neutral starting point for the analysis and relying on the afore-mentioned convergence results to wash out the remaining subjectivity (cf. Gelman and Shalizi 2013)[^gelman-2013][^gelman-2013-2]. However, this practical attitude of scientists towards modelling should not be mistaken for a principled answer to the questions raised in the philosophy of statistics (see for example Morey et al 2013)[^morey-2013].

A final reponse adopts the more Popperian viewpoint about statistical modelling expounded in Gelman and Shalizi (2013), and makes the choice of prior subject to revision explicitly. Hierarchical Bayesian modelling goes some way towards this idea, by allowing us to consider a collection of priors and adapt it on the basis of our observations. This idea can be expanded to include the revision of the whole model, i.e., the collection of statistical hypotheses over which the prior is defined (cf. Romeijn 2005)[^romeijn-2005]. Revisions of this kind relate to changes in the language, or the conceptual scheme, by means of which we are learning from the observations (Gillies 2001, Williamson 2005). Such revisions go beyond the usual method of Bayesian updating but they can still be regimented by rationality constraints, for example by requiring approximate coherence or conservativity in some way (Morey et al. 2013, Wenmackers and Romeijn 2015)[^morey-2013]. Further rationality requirements pertain to what might motivate model revisions: predictive underperfomance, changes in salience or awareness, and so on. It is to such model evaluations that we now turn.

## 5. Statistical models

In the foregoing we have seen how classical and Bayesian statistics differ. But the two major approaches to statistics also have a lot in common. Most importantly, all statistical procedures rely on the assumption of a statistical model, here referring to any restricted set of statistical hypotheses. Moreover, they are all aimed at delivering something of a verdict over these hypotheses. For example, a classical likelihood ratio test considers two hypotheses, $h$ and $h'$, and then offers a verdict of rejection and acceptance, while a Bayesian comparison delivers a posterior probability over these two hypotheses. Whereas in Bayesian statistics the model presents a very strong assumption, classical statistics does not endow the model with a special epistemic status: they are simply the hypotheses currently entertained by the scientist. Still, the adoption of a model is absolutely central to any statistical procedure.

A natural question is whether anything can be said about the quality of the statistical model, and whether any verdict on this starting point for statistical procedures can be given. While it is hard to determine the truth or falsity of a model, some models will lead to better predictions, or be a better guide to the truth, than others, inviting the slogan that “all models are wrong but some are useful” (cf. Wit et al. 2011). The evaluation of models touches on deep issues in the philosophy of science, because the statistical model often determines how the data-generating system under investigation is conceptualized and approached (Kieseppa 2001). Model choice thus resembles the choice of a theory, a conceptual scheme, or even of a whole paradigm, and thereby might seem to transcend the formal frameworks for studying theoretical rationality (cf. Carnap 1950, Jeffrey 1980)[^carnap-1950]. Despite the fact that some considerations on model choice will seem extra-statistical, in the sense that they fall outside the scope of statistical treatment, statistics offers several methods for approaching the choice of statistical models.

### 5.1 Model comparisons

There are in fact very many methods for evaluating statistical models (Claeskens and Hjort 2008, Wagenmakers and Waldorp 2006)[^claeskens-2008][^wagenmakers-2006]. In first instance, the methods occasion the comparison of statistical models, but very often they are used for selecting one model over the others. In what follows we only review prominent techniques that have led to philosophical debate: Akaike’s information criterion, the Bayesian information criterion, and furthermore the computation of marginal likelihoods and posterior model probabilities, both associated with Bayesian model selection. We leave aside methods that use cross-validation as they have, unduly, not received as much attention in the philosophical literature. The connection of model selection to conceptions of simplicity is briefly considered.

#### 5.1.1 Akaike’s information criterion

Akaike’s information criterion, modestly termed An Information Criterion or AIC for short, is based on the classical statistical procedure of estimation (see Burnham and Anderson 2002, Kieseppa 1997)[^burnham-2002]. It starts from the idea that a model $M$ can be judged by the estimate $\hat{\theta}$ that it delivers, and more specifically by the proximity of this estimate to the distribution with which the data are actually generated, i.e., the true distribution. This proximity is often equated with the expected predictive accuracy of the estimate, because if the estimate and the true distribution are closer to each other, their predictions will be better aligned to one another as well. In the derivation of the AIC, the so-called relative entropy or Kullback-Leibler divergence of the two distributions is used as a measure of their proximity, and hence as a measure of the expected predictive accuracy of the estimate.

Naturally, the true distribution is not known to the statistician who is evaluating the model. If it were, then the whole statistical analysis would be useless. However, it turns out that we can give an unbiased estimation of the divergence between the true distribution and the distribution estimated from a particular model,

$$ \text{AIC}[M] = - 2 \log P( s \mid h_{\hat{\theta}(s)} ) + 2 d , $$

in which $s$ is the sample data, $\hat{\theta}(s)$ is the maximum likelihood estimate (MLE) of the model $M$, and $d = dim(\Theta)$ is the number of dimensions of the parameter space of the model. The MLE of the model thereby features in an expression of the model quality, i.e., in a role that is conceptually distinct from the estimator function.

As can be seen from the expression above, a model with a smaller AIC is preferable: we want the fit to be optimal at little cost in complexity. Notice that the number of dimensions, or independent parameters, in the model increases the AIC and thereby lowers the eligibility of the model: if two models achieve the same maximum likelihood for the sample, then the model with fewer parameters will be preferred. For this reason, statistical model selection by the AIC can be seen as an independent motivation for preferring simple models over more complex ones (Sober and Forster 1994)[^forster-1994]. But this result also invites some critical remarks. For one, we might impose other criteria than merely the unbiasedness on the estimation of the proximity to the truth, and this will lead to different expressions for the approximation. Moreover, it is not always clearcut what the dimensions of the model under scrutiny really are. For curve fitting this may seem simple, but for more complicated models or different conceptualizations of the space of models, things do not look so easy (cf. Myung et al 2001, Kieseppa 2001, Romeijn 2017)[^romeijn-2017]. The complexity of statistical models and its relation to learning have received more systematic attention in statistical learning theory (Vapnik 2000, Harman and Kulkarni 2007)[^harman-2007][^vapnik-2000] and there are extensive discussions connecting it up to a broader philosophical notion of simplicity (e.g., Sober 2004)[^sober-2004].

A primary example of model selection is presented in curve fitting. Given a sample $s$ consisting of a set of points in the plane $(x, y)$, we are asked to choose the curve that fits these data best. We assume that the models under consideration are of the form $y = f(x) + \epsilon$, where $\epsilon$ is a normal distribution with mean 0 and a fixed standard deviation, and where $f$ is a polynomial function. Different models are characterized by polynomials of different degrees that have different numbers of parameters. Estimations fix the parameters of these polynomials. For example, for the 0-degree polynomial $f(x) = c_{0}$ we estimate the constant $\hat{c_{0}}$ for which the probability of the data is maximal, and for the 1-degree polynomial $f(x) = c_{0} + c_{1}\, x$ we estimate the slope $\hat{c_{1}}$ and the offset $\hat{c_{0}}$. Now notice that for a total of $n+$1 points, we can always find a polynomial of degree $n$ that intersects with all points exactly, resulting in a comparatively high maximum likelihood $P(s \mid \{\hat{c_{0}}, \ldots \hat{c_{n}} \})$. Applying the AIC, however, we will typically find that some model with a polynomial of degree $k < n$ is preferable. Although $P(s \mid \{\hat{c_{0}}, \ldots \hat{c_{k}} \})$ will be somewhat lower, this is compensated for in the AIC by the smaller number of parameters.

#### 5.1.2 Bayesian model evaluation and beyond

Various other prominent model selection tools are based on methods from Bayesian statistics. They all start from the idea that the quality of a model is expressed in the performance of the model on the sample data: the model that, on the whole, makes the sampled data most probable is to be preferred. Because of this, there is a close connection with the hierarchical Bayesian modelling referred to earlier (Gelman 2013)[^gelman-2013][^gelman-2013-2]. The central notion in the Bayesian model selection tools is thus the marginal likelihood of the model, i.e., the weighted average of the likelihoods over the model, using the prior distribution as a weighing function:

$$ P(s \mid M_{i}) \; = \; \int_{\theta \in \Theta_{i}} P(h_{\theta}) P(s \mid h_{\theta}) d\theta . $$

Here $\Theta_{i}$ is the parameter space belonging to model $M_{i}$. The marginal likelihoods can be combined with a prior probability over models, $P(M_{i})$, to derive the so-called posterior model probability, using Bayes’ theorem. One way of evaluating models, known as Bayesian model selection, is by comparing the models on their marginal likelihood, or else on their posteriors (cf. Kass and Raftery 1995)[^kass-1995][^raftery-1995].

Usually the marginal likelihood cannot be computed analytically. Numerical approximations can often be obtained, but for practical purposes it has proved very useful, and quite sufficient, to employ an approximation of the marginal likelihood. This approximation has become known as the Bayesian information criterion, or BIC for short (Schwarz 1978, Raftery 1995)[^raftery-1995][^schwarz-1978]. It turns out that this approximation shows remarkable similarities to the AIC:

$$ \text{BIC}[M] \; = \; - 2 \log P(s \mid h_{\hat{\theta}(s)}) + d \log n . $$

Here $\hat{\theta}(s)$ is again the maximum likelihood estimate of the model, $d = dim(M)$ the number of independent parameters, and $n$ is the number of data points in the sample. The latter dependence is the only difference with the AIC, but it is a major difference in how the model evaluation may turn out.

The concurrence of the AIC and the BIC seems to give a further motivation for our intuitive preference for simple models over more complex ones. Indeed, other model selection tools, like the deviance information criterion (Spiegelhalter et al 2002)[^spiegelhalter-2002] and the approach based on minimum description length (Grunwald 2007), also result in expressions that feature a term that penalizes complex models. However, as intimated earlier, the dimension term that we know from the information criteria does not exhaust the notion of model complexity. There is ongoing debate in the philosophy of science concerning the merits of model selection in explications of the notion of simplicity, informativeness, and the like (see, for example, Romeijn and van de Schoot 2008, Romeijn et al 2012, Steele and Werndl 2013, Sprenger 2013, Sober 2015, Autzen 2016)[^romeijn-2008][^romeijn-2012][^sprenger-2013][^sprenger-2013-2][^sprenger-2016][^steele-2013][^steele-2013-2]. Besides the debate over the evaluation of and choice between statistical models, there is a some philosophical interest in statistical meta-analysis, i.e., the practice of combining or aggregating models (e.g., Stegenga 2011)[^stegenga-2011]. Considering the importance of meta-analyses as a means to integrate and systematize the ever growing amount of research findings, this is an area that deserves more philosophical scrutiny.

An interesting new development in philosophical discussions on induction is the use of so-called meta-induction (cf. Cesa-Bianchi and Lugosi 2006, Schurz 2019, Sterkenburg 2020)[^cesa-bianchi-2006][^schurz-2019][^sterkenburg-2020]. Its basic idea relates to ensemble methods and statistical model evaluation: rather than a single model and concomitant predictive system, we consider a collection of predictors and deploy them according to their past performance, e.g., by making predictions based on a performance-weighted average of the models. There are obvious connections between meta-induction, model evaluation and statistical meta-analysis that merit further philosophical attention.

The general idea of using a wide range of models can also be identified in a rather new field on the intersection of Bayesian statistics and machine learning, Bayesian nonparametrics (e.g., Orbanz and Teh 2010, Hjort et al 2010)[^hjort-2010][^orbanz-2010]. Rather than specifying, at the outset, a confined set of distributions from which a statistical analysis is supposed to choose on the basis of the data, the idea is that the data are confronted with a potentially infinite-dimensional space of possible distributions. The set of distributions taken into consideration is then made relative to the data obtained: the complexity of the model grows with the sample. The result is a predictive system that performs an online model selection alongside a Bayesian accommodation of the posterior over the model.

### 5.2 Statistics without models

There are also statistical methods that refrain from the use of a particular model, by focusing exclusively on the data and deploying their structure, or by generalizing away from a specific choice of model. Some of these techniques are properly localized in descriptive statistics: they do not concern an inference from data but merely serve to describe the data in a particular way; principal component analysis is a primary example of this. Other techniques do derive inductive conclusions from data without explicitly adopting a model, either by relying on other assumptions that pertain to the application domain of the techniques, or by adopting constraints in a different way. Statistical methods that do not rely on an explicit model choice have unfortunately not attracted much attention in the philosophy of statistics, while data-driven methods enjoy increased popularity in scientific research. We will briefly discuss some of these methods here.

#### 5.2.1 Data reduction techniques

One set of methods, and a quite important one for many practicing statisticians, is aimed at data reduction. Often the sample data are very rich, e.g., consisting of a set of points in a space of very many dimensions. The first step in a statistical analysis may then be to automatically cluster or label the data, or to pick out the salient variability in the data, in order to scale down the computational burden of the analysis itself.

The technique of principal component analysis (PCA) is designed for the latter purpose (Jolliffe 2002)[^jolliffe-2002]. Given a set of points in a space, it seeks out the set of vectors along which the variation in the points is large. As an example, consider two points in a plane parameterized as $(x, y)$: the points $(0, 0)$ and $(1, 1)$. In the $x$-direction and in the $y$-direction the variation is $1$, but over the diagonal the variation is maximal, namely $\sqrt{2}$. The vector on the diagonal is called the principal component of the data. In richer data structures, and using a more general measure of variation among points, we can find the first component in a similar way. Moreover, we can repeat the procedure after subtracting the variation along the last found component, by projecting the data onto the plane perpendicular to that component. This allows us to build up a set of principal components of diminishing importance.

PCA is only one item from a large collection of techniques that are aimed at keeping the data manageable and finding patterns in it, a collection that also includes kernel methods and support vector machines (e.g., Vapnik and Kotz 2006)[^vapnik-2006]. For present purposes, it is important to stress that such tools should not be confused with statistical analysis: they do not involve the testing or evaluation of distributions over sample space, even though they build up and evaluate models of the data. This sets them apart from, e.g., confirmatory and exploratory factor analysis (Bartholomew 2008)[^bartholomew-2008], which are sometimes taken to be close relatives of PCA because both sets of techniques allows us to identify salient dimensions within sample space, along which the data show large variation.

Practicing statisticians often employ data reduction tools to arrive at conclusions on the distributions from which the data were sampled. There is already a wide use for machine learning and data mining techniques in the sciences, and we may expect even mode usage of these techniques in the future, because so much data is now coming available for scientific analysis. Moreover, recent statistical research suggests that data reduction, specifically kernel methods, is at the heart of modern machine learning methods, especially deep learning neural networks (cf. Belkin 2020, Bartlett et al. 2021)[^bartlett-2021][^belkin-2021]. However, in the philosophy of statistics there is as yet relatively little debate over the epistemic status of conclusions reached by means of these techniques. Philosophers of statistics would do well to direct some attention here.

#### 5.2.2 Formal and statistical learning theory

Different approaches to induction, adjacent to and partly overlapping with statistics, are presented by formal and statistical learning. This is again a vast area of research, located between statistics, computer science and artificial intelligence. The approaches are only briefly mentioned here, as examples of how we can achieve certain statistical aims, namely the identification of stable patterns in data, while in some sense avoiding the choice of a statistical model. We leave aside how formal and statistical learning can be implemented in a computer or in some other cognitive architecture. Instead we focus, necessarily briefly, on the theory of learning algorithms.

Pioneering work on formal and statistical learning was done by Solomonoff (1964). The setting is the one of inductive logic, with the data consisting of strings of 0s and 1s, and a predictor who attempts to identify the pattern in these data. So, for example, the data may be a string of the form $0101010101\ldots$, and the challenge is to identify this strings as an alternating sequence. The central idea of Solomonoff is that, to achieve universal induction, all possible computable patterns must be considered. Solomonoff then proceeded to define a formal system in which indeed all patterns are taken into consideration, effectively using a Bayesian analysis with a cleverly constructed but non-computable prior over all computable hypotheses. A comprehensive discussion of universal prediction methods following Solomonoff’s idea is offered in Sterkenburg (2018).

In theoretical computer science, the analysis of probabilistic prediction methods developed into statistical learning theory (Vapnik 2000)[^vapnik-2000]. With the advance of machine learning as a supplement to, or even a replacement of statistical methods, philosophical attention for this theory has recently increased (e.g., Herrmann 2020, Sterkenburg and Grünwald 2021)[^herrmann-2020][^sterkenburg-2021]. A closely related research area in theoretical computer science and philosophy that holds strong ties to the philosophy of statistics is formal learning theory (e.g., Kelly 1996, Kelly et al 1997)[^kelly-1996][^kelly-1997]. The approach originally covered computable learning of non-statistical patterns and formal languages (e.g., Putnam 1963, Gold 1967)[^gold-1967][^putnam-1963]. More recently, formal learning theory has been extended to hypotheses of any kind, including the learning of statistical and causal models (cf. Genin and Kelly 2017)[^genin-2017]. What is ultimately distinctive about the learning theoretic approach is that the principal focus is on finding the truth. Other considerations, such as probabilistic coherence, are either derived from optimal learning performance (Kelly 2007)[^kelly-2007] or are viewed as secondary constraints that may even hinder the performance of computationally bounded agents (Osherson et al. 1988)[^osherson-1988].

## 6. Selected related topics

There are numerous topics in the philosophy of science that bear direct relevance to the themes covered in this lemma. A few central topics are mentioned here to direct the reader to related lemmas in the encyclopedia.

One very important topic that is immediately adjacent to the philosophy of statistics is confirmation theory, the philosophical theory that describes and justifies relations between scientific theory and empirical evidence. Arguably, the theory of statistics is a proper part of confirmation theory, as it describes and justifies the relation that obtains between statistical theory and evidence in the form of samples. It can be insightful to place statistical procedures in this wider framework of relations between evidence and theory. Zooming out further, the philosophy of statistics is part of the philosophical topic of methodology, i.e., the general theory on whether and how science acquires knowledge. Thus conceived, statistics is one component in a large collection of scientific methods comprising concept formation, experimental design, manipulation and observation, confirmation, revision, and theorizing.

While these topics have always been important within epistemology and the philosophy of science, developments in the sciences have triggered interests in them from a wider community of scientists, science policy makers, and the general public: the so-called replication crisis, i.e., the discovery that in repetitions of research executed earlier we cannot recover many of the findings from the social and medical sciences. Some have pointed to problems with the statistical analyses in these sciences, e.g., the use of error probabilities as measures of how well the findings are established, as a possible explanation for the crisis (e.g., Ioannidis 2005)[^ioannidis-2005], and this in turn has sparked broad interest into the philosophy of statistics.

There are also a fair number of specific topics from the philosophy of science that are spelled out in terms of statistics or that are located in close proximity to it. One of these topics is the process of measurement, in particular the measurement of latent variables on the basis of statistical facts about manifest variables. The so-called *representational theory of measurement* (Kranz et al. 1971) relies on statistics, in particular on factor analysis, to provide a conceptual clarification of how mathematical structures represent empirical phenomena. Another important topic form the philosophy of science is causation (see the entries on probabilistic causation and Reichenbach’s common cause principle). Philosophers have employed probability theory to capture causal relations ever since Reichenbach (1956), but more recent work in causality and statistics (e.g., Spirtes et al 2001)[^spirtes-2001] has given the theory of *probabilistic causality* an enormous impulse. Here again, statistics provides a basis for the conceptual analysis of causal relations.

And there is so much more. Several specific statistical techniques, like factor analysis and the theory of Bayesian networks, invite conceptual discussion of their own accord. Numerous topics within the philosophy of science lend themselves to statistical elucidation, e.g., the coherence, informativeness, and surprise of evidence. And in turn there is a wide range of discussions in the philosophy of science that inform a proper understanding of statistics. Among them are debates over experimentation and intervention, concepts of chance, the nature of scientific models, and theoretical terms. The reader is invited to consult the entries on these topics to find further indications of how they relate to the philosophy of statistics.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=statistics). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/statistics/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=statistics&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/statistics/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

[Please contact the author with suggestions.]

## Related Entries

belief, formal representations of | causation: probabilistic | confirmation | defaults in semantics and pragmatics | evidence | induction: problem of | learning theory, formal | logic: and probability | logic: inductive | probability, interpretations of | reasoning: defeasible | Reichenbach, Hans: common cause principle | scientific method | simplicity | skepticism: ancient

[^aldous-1981]: Aldous, D.J., 1981, “Representations for Partially Exchangeable Arrays of Random Variables”, *Journal of Multivariate Analysis*, 11: 581–598.

[^armendt-1993]: Armendt, B., 1993, “Dutch books, Additivity, and Utility Theory”, *Philosophical Topics*, 21: 1–20.

[^auxier-2006]: Auxier, R.E., and L.E. Hahn (eds.), 2006, *The Philosophy of Jaakko Hintikka*, Chicago: Open Court.

[^balasubramanian-2005]: Balasubramanian, V., 2005, “MDL, Bayesian Inference, and the Geometry of the Space of Probability Distributions”, in: Advances in Minimum Description Length: Theory and Applications, P.J. Grunwald et al (eds.), Boston: MIT Press, 81–99.

[^bandyopadhyay-2011]: Bandyopadhyay, P., and Forster, M. (eds.), 2011, Handbook for the Philosophy of Science: Philosophy of Statistics, Elsevier.

[^barnett-1999]: Barnett, V., 1999, *Comparative Statistical Inference*, Wiley Series in Probability and Statistics, New York: Wiley.

[^bartholomew-2008]: Bartholomew, D.J., F. Steele, J. Galbraith, I. Moustaki, 2008, *Analysis of Multivariate Social Science Data*, Statistics in the Social and Behavioral Sciences Series, London: Taylor and Francis, 2nd edition.

[^bartlett-2021]: Bartlett, P. L., A. Montanari, A. Rakhlin, 2021, “Deep Learning: a Statistical Viewpoint”, *Acta Numerica*, 30: 87–201.

[^belkin-2021]: Belkin, M., 2021, “Fit without Fear: Remarkable Mathematical Phenomena of Deep Learning through the Prism of Interpolation”, *Acta Numerica*, 30: 203–248.

[^berger-2006]: Berger, J. 2006, “The Case for Objective Bayesian Analysis”, *Bayesian Analysis*, 1(3): 385–402.

[^berger-2009]: Berger, J.O., J.M. Bernardo, and D. Sun, 2009, “The Formal Definition of Reference Priors”, *Annals of Statistics*, 37(2): 905–938.

[^berger-1984]: Berger, J.O., and R.L. Wolpert, 1984, *The Likelihood Principle*. Hayward (CA): Institute of Mathematical Statistics.

[^berger-1987]: Berger, J.O. and T. Sellke, 1987, “Testing a Point Null Hypothesis: The Irreconciliability of P-values and Evidence”, *Journal of the American Statistical Association*, 82: 112–139.

[^bernardo-1994]: Bernardo, J.M. and A.F.M. Smith, 1994, *Bayesian Theory*, New York: John Wiley.

[^bigelow-1977]: Bigelow, J. C., 1977, “Semantics of Probability”, *Synthese*, 36(4): 459–72.

[^billingsley-1995]: Billingsley, P., 1995, *Probability and Measure*, Wiley Series in Probability and Statistics, New York: Wiley, 3rd edition.

[^birnbaum-1962]: Birnbaum, A., 1962, “On the Foundations of Statistical Inference”, *Journal of the American Statistical Association*, 57: 269–306.

[^blackwell-1962]: Blackwell, D. and L. Dubins, 1962, “Merging of Opinions with Increasing Information”, *Annals of Mathematical Statistics*, 33(3): 882–886.

[^boole-1854]: Boole, G., 1854, *An Investigation of The Laws of Thought on Which are Founded the Mathematical Theories of Logic and Probabilities*, London: Macmillan, reprinted 1958, London: Dover.

[^burnham-2002]: Burnham, K.P. and D.R. Anderson, 2002, *Model Selection and Multimodel Inference: A Practical Information-Theoretic Approach*, New York: Springer, 2nd edition.

[^carnap-1950]: Carnap, R., 1950, *Logical Foundations of Probability*, Chicago: The University of Chicago Press.

[^carnap-1952]: –––, 1952, *The Continuum of Inductive Methods*, Chicago: University of Chicago Press.

[^carnap-1970]: Carnap, R. and Jeffrey, R.C. (eds.), 1970, *Studies in Inductive Logic and Probability*, Volume I, Berkeley: University of California Press.

[^casella-1987]: Casella, G., and R. L. Berger, 1987, “Reconciling Bayesian and Frequentist Evidence in the One-Sided Testing Problem”, *Journal of the American Statistical Association*, 82: 106–111.

[^cesa-bianchi-2006]: Cesa-Bianchi, N. and G. Lugosi, 2006. *Prediction, Learning and Games*, Cambridge: Cambridge University Press.

[^claeskens-2008]: Claeskens, G. and N. L. Hjort, 2008, *Model Selection and Model Averaging*, Cambridge: Cambridge University Press.

[^cohen-1994]: Cohen, J., 1994, “The Earth is Round (p < .05)”, *American Psychologist*, 49: 997–1001.

[^cox-1961]: Cox, R.T., 1961, *The Algebra of Probable Inference*, Baltimore: John Hopkins University Press.

[^cumming-2012]: Cumming, G., 2012, *Understanding The New Statistics: Effect Sizes, Confidence Intervals, and Meta-Analysis*, New York: Routledge.

[^dawid-1982]: Dawid, A.P., 1982, “The Well-Calibrated Bayesian”, *Journal of the American Statistical Association*, 77(379): 605–610.

[^dawid-2004]: –––, 2004, “Probability, Causality and the Empirical World: A Bayes-de Finetti-Popper-Borel Synthesis”, *Statistical Science*, 19: 44–57.

[^dawid-2004-2]: Dawid, A.P. and P. Grunwald, 2004, “Game Theory, Maximum Entropy, Minimum Discrepancy, and Robust Bayesian Decision Theory”, *Annals of Statistics*, 32: 1367–1433.

[^dawid-1982-2]: Dawid, A.P. and M. Stone, 1982, “The Functional-Model Basis of Fiducial Inference”, *Annals of Statistics*, 10: 1054–1067.

[^de-1937]: De Finetti, B., 1937, “La Prévision: ses Lois Logiques, ses Sources Subjectives”, *Annales de l’Institut Henri Poincaré*, reprinted as “Foresight: its Logical Laws, its Subjective Sources”, in: Kyburg, H. E. and H. E. Smokler (eds.), *Studies in Subjective Probability*, 1964, New York: Wiley.

[^de-1974]: –––, 1974, *Theory of Probability*, Volumes I and II, New York: Wiley, translation by A. Machi and A.F.M. Smith.

[^de-1847]: De Morgan, A., 1847, *Formal Logic or The Calculus of Inference*, London: Taylor & Walton, reprinted by London: Open Court, 1926.

[^dempster-1964]: Dempster, A.P., 1964, “On the Difficulties Inherent in Fisher’s Fiducial Argument”, *Journal of the American Statistical Association*, 59: 56–66.

[^dempster-1966]: –––, 1966, “New Methods for Reasoning Towards Posterior Distributions Based on Sample Data”, *Annals of Mathematics and Statistics*, 37(2): 355–374.

[^dempster-1967]: –––, 1967, “Upper and Lower Probabilities Induced by a Multivalued Mapping”, *The Annals of Mathematical Statistics*, 38(2): 325–339.

[^dempster-1968]: –––, 1968, “A Generalization of Bayesian Inference”, *Journal of the Royal Statistical Society*, Series B, Vol. 30: 205–247.

[^diaconis-1980]: Diaconis, P., and D. Freedman, 1980, “De Finetti’s Theorem for Markov Chains”, *Annals of Probability*, 8: 115–130.

[^diaconis-2018]: Diaconis, P. and B. Skyrms, 2018, *Ten Great Ideas about Chance*, Princeton: Princeton University Press.

[^eagle-2010]: Eagle, A. (ed.), 2010, *Philosophy of Probability: Contemporary Readings*, London: Routledge.

[^earman-1992]: Earman, J., 1992, *Bayes or Bust? A Critical Examination of Bayesian Confirmation Theory*, Cambridge (MA): MIT Press.

[^easwaran-2013]: Easwaran, K., 2013, “Expected Accuracy Supports Conditionalization—and Conglomerability and Reflection”, *Philosophy of Science*, 80(1): 119–142.

[^edwards-1972]: Edwards, A.W.F., 1972, *Likelihood*, Cambridge: Cambridge University Press.

[^efron-1993]: Efron, B. and R. Tibshirani, R., 1993, *An Introduction to the Bootstrap*, Boca Raton (FL): Chapman & Hall/CRC.

[^festa-1993]: Festa, R., 1993, *Optimum Inductive Methods*, Dordrecht: Kluwer.

[^festa-1996]: –––, 1996, “Analogy and Exchangeability in Predictive Inferences”, *Erkenntnis*, 45: 89–112.

[^fisher-1925]: Fisher, R.A., 1925, *Statistical Methods for Research Workers*, Edinburgh: Oliver and Boyd.

[^fisher-1930]: –––, 1930, “Inverse Probability”, *Proceedings of the Cambridge Philosophical Society*, 26: 528–535.

[^fisher-1933]: –––, 1933, “The Concepts of Inverse Probability and Fiducial Probability Referring to Unknown Parameters”, *Proceedings of the Royal Society*, Series A, 139: 343–348.

[^fisher-1935a]: –––, 1935a, “The logic of Inductive Inference”, *Journal of the Royal Statistical Society*, 98: 39–82.

[^fisher-1935b]: –––, 1935b, *The Design of Experiments*, Edinburgh: Oliver and Boyd.

[^fisher-1935c]: –––, 1935c, “The Fiducial Argument in Statistical Inference”, *Annals of Eugenics*, 6: 317–324.

[^fisher-1955]: –––, 1955, “Statistical Methods and Scientific Induction”, *Journal of the Royal Statistical Society*, B 17: 69–78.

[^fisher-1956]: –––, 1956, *Statistical Methods and Scientific Inference*, New York: Hafner, 3rd edition 1973.

[^fitelson-2007]: Fitelson, B., 2007, “Likelihoodism, Bayesianism, and Relational Confirmation”, *Synthese*, 156(3): 473–489.

[^fletcher-2023]: Fletcher S.C. and C. Mayo-Wilson, 2023, “Evidence in Classical Statistics”, in M. Lasonen-Aarnio and C. Littlejohn (eds.), *The Routledge Handbook of the Philosophy of Evidence*, London: Taylor and Francis, p. 515–527.

[^forster-1994]: Forster, M. and E. Sober, 1994, “How to Tell when Simpler, More Unified, or Less Ad Hoc Theories will Provide More Accurate Predictions”, *British Journal for the Philosophy of Science*, 45: 1–35.

[^fraassen-1989]: Fraassen, B. van, 1989, *Laws and Symmetry*, Oxford: Clarendon Press.

[^gaifman-1982]: Gaifman, H. and M. Snir, 1982, “Probabilities over Rich Languages”, *Journal of Symbolic Logic*, 47: 495–548.

[^galavotti-2005]: Galavotti, M. C., 2005, *Philosophical Introduction to Probability*, Stanford: CSLI Publications.

[^genin-2017]: Genin, K., 2017. “The Topology of Statistical Verifiability”, *Proceedings of the 17th Conference on Theoretical Aspects of Rationality and Knowledge (TARK 2017)*, Electronic Proceedings in Theoretical Computer Science. [[Genin 2017 available online](https://arxiv.org/html/1707.08250)]

[^gelman-2013]: Gelman, A., J. Carlin, H. Stern, D. Dunson, A. Vehtari, and D. Rubin, 2013, *Bayesian Data Analysis*, revised edition, New York: Chapman & Hall/CRC.

[^gelman-2013-2]: Gelman, A., and C. Shalizi, 2013, “Philosophy and the Practice of Bayesian Statistics (with discussion)”, *British Journal of Mathematical and Statistical Psychology*, 66: 8–18.

[^giere-1976]: Giere, R. N., 1976, “A Laplacean Formal Semantics for Single-Case Propensities”, *Journal of Philosophical Logic*, 5(3): 321–353.

[^gillies-1971]: Gillies, D., 1971, “A Falsifying Rule for Probability Statements”, *British Journal for the Philosophy of Science*, 22: 231–261.

[^gillies-2000]: –––, 2000, *Philosophical Theories of Probability*, London: Routledge.

[^gold-1967]: Gold, E., 1967, “Language Identification in the Limit”, *Information and Control*, 10: 447–474.

[^goldstein-2006]: Goldstein, M., 2006, “Subjective Bayesian Analysis: Principles and Practice”, *Bayesian Analysis*, 1(3): 403–420.

[^good-1983]: Good, I.J., 1983, *Good Thinking: The Foundations of Probability and Its Applications*, Minneapolis: University of Minnesota Press; reprinted London: Dover, 2009.

[^good-1988]: –––, 1988, “The Interface Between Statistics and Philosophy of Science”, *Statistical Science*, 3(4): 386–397.

[^goodman-1965]: Goodman, N., 1965, *Fact, Fiction and Forecast*, Indianapolis: Bobbs-Merrill.

[^greaves-2006]: Greaves, H. and D. Wallace, 2006, “Justifying Conditionalization: Conditionalization Maximizes Expected Epistemic Utility”, *Mind*, 115(459): 607–632.

[^greco-2011]: Greco, D., 2011, “Significance Testing in Theory and Practice”, *British Journal for the Philosophy of Science*, 62: 607–37.

[^grünwald-2007]: Grünwald, P.D., 2007, *The Minimum Description Length Principle*, Boston: MIT Press.

[^hacking-1965]: Hacking, I., 1965, The Logic of Statistical Inference, Cambridge: Cambridge University Press.

[^hacking-2006]: –––, 2006, *The Emergence of Probability*, Cambridge: Cambridge University Press, 2nd edition.

[^haenni-2011]: Haenni, R., Romeijn, J.-W., Wheeler, G., Andrews, J., 2011, *Probabilistic Logics and Probabilistic Networks*, Berlin: Springer.

[^hailperin-1996]: Hailperin, T., 1996, *Sentential Probability Logic*, Lehigh University Press.

[^hájek-2007]: Hájek, A., 2007, “The Reference Class Problem is Your Problem Too”, *Synthese*, 156: 563–585.

[^hájek-2013]: Hájek, A. and C. Hitchcock (eds.), 2013, *Oxford Handbook of Probability and Philosophy*, Oxford: Oxford University Press.

[^halpern-2003]: Halpern, J.Y., 2003, *Reasoning about Uncertainty*, MIT press.

[^handfield-2012]: Handfield, T., 2012, *A Philosophical Guide to Chance: Physical Probability*, Cambridge: Cambridge University Press.

[^hannig-2009]: Hannig, J., 2009, “On Generalized Fiducial Inference”, *Statistica Sinica*, 19: 491–544.

[^harlow-1997]: Harlow, L.L., S.A. Mulaik, and J.H. Steiger, (eds.), 1997, *What If There Were No Significance Tests?*, Mahwah (NJ): Erlbaum.

[^harman-2007]: Harman, G. and S. Kulkarni, 2007, *Reliable Reasoning: Induction and Statistical Learning Theory*, Cambridge, MA: The MIT Press.

[^hastie-2009]: Hastie, T., R. Tibshirani, and J. Friedman, 2009, *The Elements of Statistical Learning: Data Mining, Inference, and Prediction* (Springer Series in Statistics), second edition, New York: Springer.

[^henderson-2010]: Henderson, L., N.D. Goodman, J.B. Tenenbaum, and J.F. Woodward, 2010, “The Structure and Dynamics of Scientific Theories: A Hierarchical Bayesian Perspective”, *Philosophy of Science*, 77(2): 172–200.

[^herrmann-2020]: Herrmann, D. A., 2020, “PAC Learning and Occam’s Razor: Probably Approximately Incorrect”, *Philosophy of Science*, 87(4): 685–703.

[^hjort-2010]: Hjort, N., C. Holmes, P. Mueller, and S. Walker (eds.), 2010, *Bayesian Nonparametrics*, Cambridge Series in Statistical and Probabilistic Mathematics, nr. 28, Cambridge: Cambridge University Press.

[^howson-2000]: Howson, C., 2000, *Hume’s Problem: Induction and the Justification of Belief*, Oxford: Oxford University Press.

[^howson-2003]: –––, 2003, “Probability and Logic”, *Journal of Applied Logic*, 1(3–4): 151–165.

[^howson-2011]: –––, 2011, “Bayesianism as a Pure Logic of Inference”, in: Bandyopadhyay, P and Foster, M, (eds.), *Philosophy of statistics, Handbook of the Philosophy of Science*, Oxford: North Holland, 441–472.

[^howson-2006]: Howson, C. and P. Urbach, 2006, *Scientific Reasoning: The Bayesian Approach*, La Salle: Open Court, 3rd edition.

[^hintikka-1970]: Hintikka, J., 1970, “Unknown Probabilities, Bayesianism, and de Finetti’s Representation Theorem”, in *Proceedings of the Biennial Meeting of the Philosophy of Science Association*, Vol. 1970, Boston: Springer, 325–341.

[^hintikka-1980]: Hintikka, J. and I. Niiniluoto, 1980, “An Axiomatic Foundation for the Logic of Inductive Generalization”, in R.C. Jeffrey (ed.), *Studies in Inductive Logic and Probability*, volume II, Berkeley: University of California Press, 157–181.

[^hintikka-1966]: Hintikka, J. and P. Suppes (eds.), 1966, *Aspects of Inductive Logic*, Amsterdam: North-Holland.

[^hitchcock-2016]: Hitchcock, C. and A. Hájek (eds.), 2016, *The Oxford Handbook of Probability and Philosophy*, Oxford: Oxford University Press.

[^hume-1739]: Hume, D., 1739, *A Treatise of Human Nature*, [available online](http://www.earlymoderntexts.com/authors/hume.html).

[^huttegger-2017]: Huttegger, S., 2017, *The Probabilistic Foundations of Rational Learning*, Cambridge: Cambridge University Press.

[^huygens-1657]: Huygens, Christiaan, 1657, “De Ratiociniis in Aleæ Ludo”, in *Exercitionum Mathematicarum, libri quinque,* Francis van Schooten (ed), Leiden: Johannis Elsevirii: 517–534.

[^ioannidis-2005]: Ioannidis, J.P.A., 2005, “Why Most Published Research Findings Are False”, *PLoS Medicine*, 2(8): e124. doi:10.1371/journal.pmed.0020124

[^james-2014]: James, G., D. Witten, T. Hastie, R. Tibshirani, 2014, *An Introduction to Statistical Learning Theory*, New York: Springer.

[^jaynes-1973]: Jaynes, E.T., 1973, “The Well-Posed Problem”, *Foundations of Physics*, 3: 477–493.

[^jaynes-2003]: –––, 2003, *Probability Theory: The Logic of Science*, Cambridge: Cambridge University Press, [first 3 chapters available online](http://bayes.wustl.edu/etj/prob/book.pdf).

[^jeffrey-1992]: Jeffrey, R., 1992, *Probability and the Art of Judgment*, Cambridge: Cambridge University Press.

[^jeffreys-1961]: Jeffreys, H., 1961, *Theory of Probability*, Oxford: Clarendon Press, 3rd edition.

[^jolliffe-2002]: Jolliffe, I.T., 2002, *Principal Component Analysis*, New York: Springer, 2nd edition.

[^joyce-1998]: Joyce, J., 1998, “A Nonpragmatic Vindication of Probabilism”, *Philosophy of Science*, 65: 575–603.

[^kadane-2011]: Kadane, J.B., 2011, *Principles of Uncertainty*, London: Chapman and Hall.

[^kadane-1996a]: Kadane, J.B., M.J. Schervish, and T. Seidenfeld, 1996a, “When Several Bayesians Agree That There Will Be No Reasoning to a Foregone Conclusion”, *Philosophy of Science*, 63: S281–S289.

[^kadane-1996b]: –––, 1996b, “Reasoning to a Foregone Conclusion”, *Journal of the American Statistical Association*, 91(435): 1228–1235.

[^kass-1995]: Kass, R. and A. Raftery, 1995, “Bayes Factors”, *Journal of the American Statistical Association*, 90: 773–790.

[^kelly-1996]: Kelly, K.T., 1996, *The Logic of Reliable Inquiry*, Oxford: Oxford University Press.

[^kelly-2007]: –––, 2007, “A New Solution to the Puzzle of Simplicity”, *Philosophy of Science* 74(5): 561–573.

[^kelly-1997]: Kelly, K., O. Schulte, and C. Juhl, 1997, “Learning Theory and the Philosophy of Science”, *Philosophy of Science*, 64: 245–67.

[^keynes-1921]: Keynes, J.M., 1921, *A Treatise on Probability*, London: Macmillan.

[^kieseppä-1997]: Kieseppä, I. A., 1997, “Akaike Information Criterion, Curve-Fitting, and the Philosophical Problem of Simplicity”, *British Journal for the Philosophy of Science*, 48(1): 21–48.

[^kieseppä-2001]: –––, 2001, “Statistical Model Selection Criteria and the Philosophical Problem of Underdetermination”, *British Journal for the Philosophy of Science*, 52(4): 761–794.

[^kingman-1975]: Kingman, J.F.C., 1975, “Random Discrete Distributions”, *Journal of the Royal Statistical Society*, 37: 1–22.

[^kingman-1978]: –––, 1978, “Uses of Exchangeability”, *Annals of Probability*, 6(2): 183–197.

[^kolmogorov-1933]: Kolmogorov, A.N., 1933, *Grundbegriffe der Wahrscheinlichkeitsrechnung*, Berlin: Julius Springer.

[^krantz-1971]: Krantz, D. H., R. D. Luce, A. Tversky and P. Suppes, 1971, *Foundations of Measurement*, Volumes I and II. Mineola: Dover Publications.

[^kuipers-1978]: Kuipers, T.A.F., 1978, *Studies in Inductive Probability and Rational Expectation*, Dordrecht: Reidel.

[^kuipers-1986]: –––, 1986, “Some Estimates of the Optimum Inductive Method”, *Erkenntnis*, 24: 37–46.

[^kyburg-1961]: Kyburg, Jr., H.E., 1961, *Probability and the Logic of Rational Belief*, Middletown (CT): Wesleyan University Press.

[^kyburg-2001]: Kyburg, H.E. Jr. and C.M. Teng, 2001, *Uncertain Inference*, Cambridge: Cambridge University Press.

[^lambalgen-1987]: van Lambalgen, M., 1987, *Random Sequences*, Ph.D. dissertation, Department of Mathematics and Computer Science, University of Amsterdam, [van Lambalgen 1987 available online](https://www.illc.uva.nl/Research/Publications/Dissertations/HDS-08-Michiel-van-Lambalgen.text.pdf).

[^leitgeb-2010a]: Leitgeb, H. and Pettigrew, R., 2010a, “An Objective Justification of Bayesianism I: Measuring Inaccuracy”, *Philosophy of Science*, 77(2): 201–235.

[^leitgeb-2010b]: –––, 2010b, “An Objective Justiﬁcation of Bayesianism II: The Consequences of Minimizing Inaccuracy”, *Philosophy of Science*, 77(2): 236–272.

[^levi-1980]: Levi, I., 1980, *The Enterprise of Knowledge: An Essay on Knowledge, Credal Probability, and Chance*, Cambridge MA: MIT Press.

[^lindley-1957]: Lindley, D.V., 1957, “A Statistical Paradox”, *Biometrika*, 44: 187–192.

[^lindley-1965]: –––, 1965, *Introduction to Probability and Statistics from a Bayesian Viewpoint*, Vols. I and II, Cambridge: Cambridge University Press.

[^lindley-2000]: –––, 2000, “The Philosophy of Statistics”, *Journal of the Royal Statistical Society*, D (The Statistician), Vol. 49(3): 293–337.

[^mackay-2003]: Mackay, D.J.C., 2003, *Information Theory, Inference, and Learning Algorithms*, Cambridge: Cambridge University Press.

[^maher-1993]: Maher, P., 1993, *Betting on Theories*, Cambridge Studies in Probability, Induction and Decision Theory, Cambridge: Cambridge University Press.

[^mayo-1996]: Mayo, D.G., 1996, *Error and the Growth of Experimental Knowledge*, Chicago: The University of Chicago Press.

[^mayo-2010]: –––, 2010, An Error in the Argument from Conditionality and Sufficiency to the Likelihood Principle, in: D. Mayo, A. Spanos (eds.), Error and Inference: Recent Exchanges on Experimental Reasoning, Reliability, and the Objectivity and Rationality of Science, pp. 305–314, Cambridge: Cambridge University Press.

[^mayo-2014]: –––, 2014, “On the Birnbaum Argument for the Strong Likelihood Principle”, *Statistical Science*, 29(2): 227–239.

[^mayo-2018]: –––, 2018, *Statistical Inference as Severe Testing*, Cambridge: Cambridge University Press.

[^mayo-2006]: Mayo, D.G., and A. Spanos, 2006, “Severe Testing as a Basic Concept in a Neyman-Pearson Philosophy of Induction”, *The British Journal for the Philosophy of Science*, 57: 323–357.

[^mayo-2011]: –––, 2011, “Error Statistics”, in P.S. Bandyopadhyay and M.R. Forster, *Philosophy of Statistics, Handbook of the Philosophy of Science*, Vol. 7, Elsevier.

[^mayo-2006-2]: Mayo, D.G., and D.R. Cox, 2006, “Frequentist Statistics as a Theory of Inductive Inference”, in *IMS Lecture Notes Monograph Series* (Volume 49: 2nd Lehmann Symposium on Optimality), Institute of Mathematical Statistics, 77–97. doi:10.1214/074921706000000400

[^mellor-2005]: Mellor, D. H., 2005, *The Matter of Chance*, Cambridge: Cambridge University Press.

[^mellor-2005-2]: –––, 2005, *Probability: A Philosophical Introduction*, London: Routledge.

[^mises-1981]: von Mises, R., 1981, *Probability, Statistics and Truth*, 2nd revised English edition, New York: Dover.

[^mood-1974]: Mood, A. M., F. A. Graybill, and D. C. Boes, 1974, *Introduction to the Theory of Statistics*, Boston: McGraw-Hill.

[^morey-2013]: Morey, R., J.W. Romeijn and J. Rouder, 2013, “The Humble Bayesian”, *British Journal of Mathematical and Statistical Psychology*, 66(1): 68–75.

[^morey-2016]: Morey R.D., R. Hoekstra, J.N. Rouder, M.D. Lee and E.J. Wagenmakers, 2016, “The Fallacy of Placing Confidence in Confidence Intervals”, *Psychonomic Bulletin and Review*, 23(1): 103–23.

[^myung-2000]: Myung, J., V. Balasubramanian, and M.A. Pitt, 2000, “Counting Probability Distributions: Differential Geometry and Model Selection”, *Proceedings of the National Academy of Sciences*, 97(21): 11170–11175.

[^nagel-1939]: Nagel, T., 1939, *Principles of the Theory of Probability*, Chicago: University of Chicago Press.

[^neyman-1957]: Neyman, J., 1957, “Inductive Behavior as a Basic Concept of Philosophy of Science”, *Revue Institute Internationale De Statistique*, 25: 7–22.

[^neyman-1971]: –––, 1971, Foundations of Behavioristic Statistics, in: V. Godambe and D. Sprott (eds.), Foundations of Statistical Inference, Toronto: Holt, Rinehart and Winston of Canada, pp. 1–19.

[^neyman-1928]: Neyman, J. and K. Pearson, 1928, “On the Use and Interpretation of Certain Test Criteria for Purposes of Statistical Inference”, *Biometrika*, A20: 175–240 and 264–294.

[^neyman-1933]: Neyman, J. and E. Pearson, 1933, “On the Problem of the Most Efficient Tests of Statistical Hypotheses”, *Philosophical Transactions of the Royal Society*, A 231: 289–337

[^neyman-1967]: –––, 1967, *Joint Statistical Papers*, Cambridge: Cambridge University Press.

[^nix-2006]: Nix, C. J. and J. B. Paris, 2006, “A Continuum of Inductive Methods Arising from a Generalised Principle of Instantial Relevance”, *Journal of Philosophical Logic*, 35: 83–115.

[^osherson-1988]: Osherson, D.N., M. Stob, and S. Weinstein, 1988, “Mechanical Learners Pay a Price for Bayesianism”, *The Journal of Symbolic Logic*, 53(4): 1245–1251.

[^orbanz-2010]: Orbanz, P. and Y.W. Teh, 2010, “Bayesian Nonparametric Models”, *Encyclopedia of Machine Learning*, New York: Springer.

[^paris-1994]: Paris, J.B., 1994, *The Uncertain Reasoner’s Companion*, Cambridge: Cambridge University Press.

[^paris-1989]: Paris, J.B. and A. Vencovska, 1989, “On the Applicability of Maximum Entropy to Inexact Reasoning”, *International Journal of Approximate Reasoning*, 4(3): 183–224.

[^paris-2009]: Paris, J., and P. Waterhouse, 2009, “Atom Exchangeability and Instantial Relevance”, *Journal of Philosophical Logic*, 38(3): 313–332.

[^peirce-1910]: Peirce, C. S., 1910, “Notes on the Doctrine of Chances”, in C. Hartshorne and P. Weiss (eds.), *Collected Papers of Charles Sanders Peirce*, Vol. 2, Cambridge MA: Harvard University Press, 405–14, reprinted 1931.

[^plato-1994]: Plato, J. von, 1994, *Creating Modern Probability*, Cambridge: Cambridge University Press.

[^popper-1934]: Popper, K.R., 1934/1959, *The Logic of Scientific Discovery*, New York: Basic Books.

[^popper-1959]: –––, 1959, “The Propensity Interpretation of Probability”, *British Journal of the Philosophy of Science*, 10: 25–42.

[^predd-2009]: Predd, J.B., R. Seiringer, E.H. Lieb, D.N. Osherson, H.V. Poor, and S.R. Kulkarni, 2009, “Probabilistic Coherence and Proper Scoring Rules”, *IEEE Transactions on Information Theory*, 55(10): 4786–4792.

[^press-2002]: Press, S. J., 2002, *Bayesian Statistics: Principles, Models, and Applications* (Wiley Series in Probability and Statistics), New York: Wiley.

[^putnam-1963]: Putnam, H., 1963, “Degree of Confirmation and Inductive Logic”, in *The Philosophy of Rudolf Carnap*, P.A. Schilpp (ed.), La Salle, Ill: Open Court.

[^raftery-1995]: Raftery, A.E., 1995, “Bayesian Model Selection in Social Research”, *Sociological Methodology*, 25: 111–163.

[^ramsey-1926]: Ramsey, F.P., 1926, “Truth and Probability”, in R.B. Braithwaite (ed.), *The Foundations of Mathematics and other Logical Essays*, Ch. VII, p.156–198, printed in London: Kegan Paul, 1931.

[^reichenbach-1938]: Reichenbach, H., 1938, *Experience and prediction: an analysis of the foundations and the structure of knowledge*, Chicago: University of Chicago Press.

[^reichenbach-1949]: –––, 1949, *The theory of probability*, Berkeley: University of California Press.

[^reichenbach-1956]: –––, 1956, *The Direction of Time*, Berkeley: University of Los Angeles Press.

[^renyi-1970]: Renyi, A., 1970, *Probability Theory*, Amsterdam: North Holland.

[^robbins-1952]: Robbins, H., 1952, “Some Aspects of the Sequential Design of Experiments”, *Bulletin of the American Mathematical Society*, 58: 527–535.

[^roberts-1967]: Roberts, H.V., 1967, “Informative Stopping Rules and Inferences about Population Size”, *Journal of the American Statistical Association*, 62(319): 763–775.

[^romeijn-2004]: Romeijn, J.W., 2004, “Hypotheses and Inductive Predictions”, *Synthese*, 141(3): 333–364.

[^romeijn-2005]: –––, 2005, *Bayesian Inductive Logic*, PhD dissertation, University of Groningen.

[^romeijn-2006]: –––, 2006, “Analogical Predictions for Explicit Similarity”, *Erkenntnis*, 64: 253–280.

[^romeijn-2011]: –––, 2011, “Statistics as Inductive Logic”, in Bandyopadhyay, P. and M. Forster (eds.), *Handbook for the Philosophy of Science*, Vol. 7: Philosophy of Statistics, 751–774.

[^romeijn-2017]: –––, 2017, “Implicit Complexity”, *Philosophy of Science*, 84(5): 797–809.

[^romeijn-2008]: Romeijn, J.W. and van de Schoot, R., 2008, “A Philosophical Analysis of Bayesian model selection”, in Hoijtink, H., I. Klugkist and P. Boelen (eds.), *Null, Alternative and Informative Hypotheses*, 329–357.

[^romeijn-2012]: Romeijn, J.W., van de Schoot, R., and Hoijtink, H., 2012, “One Size Does Not Fit All: Derivation of a Prior-Adapted BIC”, in Dieks, D., W. Gonzales, S. Hartmann, F. Stadler, T. Uebel, and M. Weber (eds.), *Probabilities, Laws, and Structures*, Berlin: Springer.

[^rosenkrantz-1977]: Rosenkrantz, R.D., 1977, *Inference, Method and Decision: Towards a Bayesian Philosophy of Science*, Dordrecht: Reidel.

[^rosenkrantz-1981]: –––, 1981, *Foundations and Applications of Inductive Probability*, Ridgeview Press.

[^royall-1997]: Royall, R., 1997, *Scientific Evidence: A Likelihood Paradigm*, London: Chapman and Hall.

[^savage-1962]: Savage, L.J., 1962, *The Foundations of Statistical Inference*, London: Methuen.

[^schervish-2009]: Schervish, M.J., T. Seidenfeld, and J.B. Kadane, 2009, “Proper Scoring Rules, Dominated Forecasts, and Coherence”, *Decision Analysis*, 6(4): 202–221.

[^schurz-2019]: Schurz, G., 2019, *Hume’s Problem Solved*, Cambridge, MA: MIT press.

[^schwarz-1978]: Schwarz, G., 1978, “Estimating the Dimension of a Model”, *Annals of Statistics*, 6: 461–464.

[^seidenfeld-1979]: Seidenfeld, T., 1979, *Philosophical Problems of Statistical Inference: Learning from R.A. Fisher*, Dordrecht: Reidel.

[^seidenfeld-1986]: –––, 1986, “Entropy and Uncertainty”, *Philosophy of Science*, 53(4): 467–491.

[^seidenfeld-1992]: –––, 1992, “R.A. Fisher’s Fiducial Argument and Bayes Theorem”, *Statistical Science*, 7(3): 358–368.

[^shafer-1976]: Shafer, G., 1976, *A Mathematical Theory of Evidence*, Princeton: Princeton University Press.

[^shafer-1982]: –––, 1982, “On Lindley’s Paradox (with discussion)”, *Journal of the American Statistical Association*, 378: 325–351.

[^shore-1980]: Shore, J. and Johnson, R., 1980, “Axiomatic Derivation of the Principle of Maximum Entropy and the Principle of Minimum Cross-Entropy”, *IEEE Transactions on Information Theory*, 26(1): 26–37.

[^skyrms-1991]: Skyrms, B., 1991, “Carnapian Inductive Logic for Markov Chains”, *Erkenntnis*, 35: 439–460.

[^skyrms-1993]: –––, 1993, “Analogy by Similarity in Hypercarnapian Inductive Logic”, in Massey, G.J., J. Earman, A.I. Janis and N. Rescher (eds.), *Philosophical Problems of the Internal and External Worlds: Essays Concerning the Philosophy of Adolf Gruenbaum*, Pittsburgh: Pittsburgh University Press, 273–282.

[^skyrms-1996]: –––, 1996, “Carnapian Inductive Logic and Bayesian Statistics”, in: Ferguson, T.S., L.S. Shapley, and J.B. MacQueen (eds.), *Statistics, Probability, and Game Theory: Papers in Honour of David Blackwell*, Hayward: IMS lecture notes, 321–336.

[^skyrms-1999]: –––, 1999, *Choice and Chance: An Introduction to Inductive Logic*, Wadsworth, 4th edition.

[^sober-2004]: Sober, E., 2004, “Likelihood, Model Selection, and the Duhem-Quine Problem”, *Journal of Philosophy*, 101(5): 221–241.

[^spanos-2010]: Spanos, A., 2010, “Is Frequentist Testing Vulnerable to the Base-Rate Fallacy?”, *Philosophy of Science*, 77: 565–583.

[^spanos-2013a]: –––, 2013a, “Who Should Be Afraid of the Jeffreys-Lindley Paradox?”, *Philosophy of Science*, 80: 73–93.

[^spanos-2013b]: –––, 2013b, “A Frequentist Interpretation of Probability for Model-Based Inductive Inference”, *Synthese*, 190: 1555–1585.

[^spiegelhalter-2002]: Spiegelhalter, D.J., N.G. Best, B.P. Carlin, and A. van der Linde, 2002, “Bayesian Measures of Model Complexity and Fit”, *Journal of Royal Statistical Society*, B 64: 583–639.

[^spielman-1974]: Spielman, S., 1974, “The Logic of Significance Testing”, *Philosophy of Science*, 41: 211–225.

[^spielman-1978]: –––, 1978, “Statistical Dogma and the Logic of Significance Testing”, *Philosophy of Science*, 45: 120–135.

[^sprenger-2013]: Sprenger, J., 2013, “The Role of Bayesian Philosophy within Bayesian Model Selection”, *European Journal for Philosophy of Science*, 3(1): 101–114.

[^sprenger-2013-2]: –––, Sprenger J., 2013, “Testing a Precise Null Hypothesis: The Case of Lindley’s Paradox”, *Philosophy of Science*, 80(5): 733–744.

[^sprenger-2016]: –––, 2016, “Bayesianism vs. Frequentism in Statistical Inference”, in Alan Hájek and Chris Hitchcock (eds.), *Handbook of the Philosophy of Probability*, Oxford: Oxford University Press, 382–405.

[^spirtes-2001]: Spirtes, P., Glymour, C. and Scheines, R., 2001, *Causation, Prediction, and Search*, Boston: MIT press, 2nd edition.

[^solomonoff-1964]: Solomonoff, R.J., 1964, “A Formal Theory of Inductive Inference”, parts I and II, *Information and Control*, 7: 1–22 and 224–254.

[^stegenga-2011]: Stegenga, J., 2011, “Is Meta-Analysis the Platinum Standard of Evidence?”, *Studies in History and Philosophy of Biological and Biomedical Sciences*, 42(4): 497–507.

[^steele-2013]: Steele, K., 2013, “Persistent Experimenters, Stopping Rules, and Statistical Inference”, *Erkenntnis*, 78(4): 937–961.

[^steele-2013-2]: Steele, K. and Werndl, C., 2013, “Climate Models, Calibration, and Confirmation”, *British Journal for the Philosophy of Science*, 64: 609–635.

[^sterkenburg-2018]: Sterkenburg, T., 2018, *Universal Prediction: A Philosophical Investigation*, Ph.D. thesis, Rijksuniversiteit Groningen.

[^sterkenburg-2020]: –––, 2020. “The Meta-Inductive Justification of Induction”, *Episteme*, 17(4): 519–541.

[^sterkenburg-2021]: –––, and P.D. Grünwald, 2021. “The No-Free-Lunch Theorems of Supervised Learning”, *Synthese*, 199: 9979–10015.

[^suppes-2001]: Suppes, P., 2001, *Representation and Invariance of Scientific Structures*, Chicago: University of Chicago Press.

[^uffink-1996]: Uffink, J., 1996, “The Constraint Rule of the Maximum Entropy Principle”, *Studies in History and Philosophy of Modern Physics*, 27: 47–79.

[^vapnik-2000]: Vapnik, V. N., 2000, *The Nature of Statistical Learning Theory. Statistics for Engineering and Information Science*, 2nd edition, New York: Springer.

[^vapnik-2006]: Vapnik, V.N. and S. Kotz, 2006, *Estimation of Dependences Based on Empirical Data*, New York: Springer.

[^venn-1888]: Venn, J., 1888, *The Logic of Chance*, London: MacMillan, 3rd edition.

[^wagenmakers-2007]: Wagenmakers, E.J., 2007, “A Practical Solution to the Pervasive Problems of p-Values”, Psychonomic Bulletin and Review 14(5), 779–804.

[^wagenmakers-2006]: Wagenmakers, E.J., and L.J. Waldorp, (eds.), 2006, *Journal of Mathematical Psychology*, 50(2). Special issue on Model Selection, 99–214.

[^wald-1939]: Wald, A., 1939, “Contributions to the Theory of Statistical Estimation and Testing Hypotheses”, *Annals of Mathematical Statistics*, 10(4): 299–326.

[^wald-1950]: –––, 1950, *Statistical Decision Functions*, New York: John Wiley and Sons.

[^walley-1991]: Walley, P., 1991, *Statistical Reasoning with Imprecise Probabilities*, New York: Chapman & Hall.

[^wasserman-2004]: Wasserman, L., 2004, *All of Statistics: A Concise Course in Statistical Inference*, New York: Springer.

[^williams-1980]: Williams, P.M., 1980, “Bayesian Conditionalisation and the Principle of Minimum Information”, *British Journal for the Philosophy of Science*, 31: 131–144.

[^williamson-2010]: Williamson, J., 2010, *In Defence of Objective Bayesianism*, Oxford: Oxford University Press.

[^ziliak-2008]: Ziliak, S.T. and D.N. McCloskey, 2008, *The Cult of Statistical Significance*, Ann Arbor: University of Michigan Press.

[^zabell-1992]: Zabell, S.L., 1992, “R. A. Fisher and the Fiducial Argument”, *Statistical Science*, 7(3): 358–368.

[^zabell-1982]: –––, 1982, “W. E. Johnson’s ‘Sufficientness’ Postulate”, *Annals of Statistics*, 10(4): 1090–1099.
