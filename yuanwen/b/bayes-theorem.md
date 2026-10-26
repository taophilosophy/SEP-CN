# Bayes’ Theorem
**First published Sat Jun 28, 2003; substantive revision Tue Sep 30, 2003**

*Joyce, James*

## 1. Conditional Probabilities and Bayes' Theorem

The probability of a hypothesis *H* conditional on a given body of data *E* is the ratio of the unconditional probability of the conjunction of the hypothesis with the data to the unconditional probability of the data alone.

> | **(1.1)** | **Definition**. |
> | --- | --- |
> |   | The probability of *H* conditional on *E* is defined as **P***<sub>E</sub>*(*H*) = **P**(*H* & *E*)**/P**(*E*), provided that both terms of this ratio exist and **P**(*E*) > 0.[^note-1] |

To illustrate, suppose J. Doe is a randomly chosen American who was alive on January 1, 2000. According to the United States Center for Disease Control, roughly 2.4 million of the 275 million Americans alive on that date died during the 2000 calendar year. Among the approximately 16.6 million senior citizens (age 75 or greater) about 1.36 million died. The unconditional probability of the hypothesis that our J. Doe died during 2000, *H*, is just the population-wide mortality rate **P**(*H*) = 2.4M/275M = 0.00873. To find the probability of J. Doe's death conditional on the information, *E*, that he or she was a senior citizen, we divide the probability that he or she was a senior who died, **P**(*H* & *E*) = 1.36M/275M = 0.00495, by the probability that he or she was a senior citizen, **P**(*E*) = 16.6M/275M = 0.06036. Thus, the probability of J. Doe's death given that he or she was a senior is **P**<sub><em>E</em></sub>(*H*) = **P**(*H* & *E*)/**P**(*E*) = 0.00495/0.06036 = 0.082. Notice how the size of the *total* population factors out of this equation, so that **P**<sub><em>E</em></sub>(*H*) is just the proportion of seniors who died. One should contrast this quantity, which gives the mortality rate among senior citizens, with the "inverse" probability of *E* conditional on *H*, **P**<sub><em>H</em></sub>(*E*) = **P**(*H* & *E*)/**P**(*H*) = 0.00495/0.00873 = 0.57, which is the proportion of deaths *in the total population* that occurred among seniors.

Here are some straightforward consequences of (1.1):

- *Probability*. **P**<sub><em>E</em></sub> is a probability function.[^note-2]
- *Logical Consequence*. If *E* entails *H*, then **P**<sub><em>E</em></sub>(*H*) = 1.
- *Preservation of Certainties*. If **P**(*H*) = 1, then **P**<sub><em>E</em></sub>(*H*) = 1.
- *Mixing*. **P**(*H*) = **P**(*E*)**P**<sub><em>E</em></sub>(*H*) + **P**(~*E*)**P<sub>~</sub>**<sub><em>E</em></sub>(*H*).[^note-3]

The most important fact about conditional probabilities is undoubtedly *Bayes' Theorem*, whose significance was first appreciated by the British cleric Thomas Bayes in his posthumously published masterwork, "An Essay Toward Solving a Problem in the Doctrine of Chances" (Bayes 1764)[^bayes-1764]. Bayes' Theorem relates the "direct" probability of a hypothesis conditional on a given body of data, **P**<sub><em>E</em></sub>(*H*), to the "inverse" probability of the data conditional on the hypothesis, **P**<sub><em>H</em></sub>(*E*).

> | **(1.2)** | **Bayes' Theorem**. |
> | --- | --- |
> |   | **P**<sub><em>E</em></sub>(*H*) = [**P**(*H*)**/P**(*E*)] **P**<sub><em>H</em></sub>(*E*) |

In an unfortunate, but now unavoidable, choice of terminology, statisticians refer to the inverse probability **P**<sub><em>H</em></sub>(*E*) as the "likelihood" of *H* on *E*. It expresses the degree to which the hypothesis *predicts* the data given the background information codified in the probability **P**.

In the example discussed above, the condition that J. Doe died during 2000 is a fairly strong predictor of senior citizenship. Indeed, the equation **P**<sub><em>H</em></sub>(*E*) = 0.57 tells us that 57% of the total deaths occurred among seniors that year. Bayes' theorem lets us use this information to compute the "direct" probability of J. Doe dying given that he or she was a senior citizen. We do this by multiplying the "prediction term" **P**<sub><em>H</em></sub>(*E*) by the ratio of the total number of deaths in the population to the number of senior citizens in the population, **P**(*H*)/**P**(*E*) = 2.4M/16.6M = 0.144. The result is **P**<sub><em>E</em></sub>(*H*) = 0.57 × 0.144 = 0.082, just as expected.

Though a mathematical triviality, Bayes' Theorem is of great value in calculating conditional probabilities because inverse probabilities are typically both easier to ascertain and less subjective than direct probabilities. People with different views about the unconditional probabilities of *E* and *H* often disagree about *E*'s value as an indicator of *H*. Even so, they can agree about the degree to which the hypothesis predicts the data if they know any of the following intersubjectively available facts: (a) *E*'s *objective* probability given *H*, (b) the frequency with which events like *E* will occur if *H* is true, or (c) the fact that *H* logically entails *E*. Scientists often design experiments so that likelihoods can be known in one of these "objective" ways. Bayes' Theorem then ensures that any dispute about the significance of the experimental results can be traced to "subjective" disagreements about the unconditional probabilities of *H* and *E*.

When both **P**<sub><em>H</em></sub>(*E*) and **P**<sub>~<em>H</em></sub>(*E*) are known an experimenter need not even know *E*'s probability to determine a value for **P**<sub><em>E</em></sub>(*H*) using Bayes' Theorem.

> | **(1.3)** | **Bayes' Theorem** (2nd form).[^note-4] |
> | --- | --- |
> |   | **P**<sub><em>E</em></sub>(*H*) = **P**(*H*)**P**<sub><em>H</em></sub>(*E*) **/** [**P**(*H*)**P**<sub><em>H</em></sub>(*E*) + **P**(~*H*)**P**<sub>~<em>H</em></sub>(*E*)] |

In this guise Bayes' theorem is particularly useful for inferring causes from their effects since it is often fairly easy to discern the probability of an effect given the presence or absence of a putative cause. For instance, physicians often screen for diseases of known prevalence using diagnostic tests of recognized *sensitivity* and *specificity*. The sensitivity of a test, its "true positive" rate, is the fraction of times that patients with the disease test positive for it. The test's specificity, its "true negative" rate, is the proportion of healthy patients who test negative. If we let *H* be the event of a given patient having the disease, and *E* be the event of her testing positive for it, then the test's sensitivity and specificity are given by the likelihoods **P**<sub><em>H</em></sub>(*E*) and **P<sub>~</sub>**<sub><em>H</em></sub>(*~E*), respectively, and the "baseline" prevalence of the disease in the population is **P**(*H*). Given these inputs about the effects of the disease on the outcome of the test, one can use (1.3) to determine the probability of disease given a positive test. For a more detailed illustration of this process, see Example 1 in the Supplementary Document "Examples, Tables, and Proof Sketches".

## 2. Special Forms of Bayes' Theorem

Bayes' Theorem can be expressed in a variety of forms that are useful for different purposes. One version employs what Rudolf Carnap called the *relevance quotient* or *probability ratio* (Carnap 1962, 466)[^carnap-1962]. This is the factor ***PR***(*H*, *E*) = **P**<sub><em>E</em></sub>(*H*)**/P**(*H*) by which *H*'s unconditional probability must be multiplied to get its probability conditional on *E*. Bayes' Theorem is equivalent to a simple symmetry principle for probability ratios.

> | **(1.4)** | **Probability Ratio Rule**. |
> | --- | --- |
> |   | ***PR***(*H*, *E*) = ***PR***(*E*, *H*) |

The term on the right provides one measure of the degree to which *H predicts E*. If we think of **P**(*E*) as expressing the "baseline" predictability of *E* given the background information codified in **P**, and of **P**<sub><em>H</em></sub>(*E*) as *E*'s predictability when *H* is added to this background, then ***PR***(*E*, *H*) captures the degree to which knowing *H* makes *E* more or less predictable relative to the baseline: ***PR***(*E*, *H*) = 0 means that *H* categorically predicts ~*E*; ***PR***(*E*, *H*) = 1 means that adding *H* does not alter the baseline prediction at all; ***PR***(*E*, *H*) = 1**/P**(*E*) means that *H* categorically predicts *E*. Since **P**(*E*)) = **P**<sub><b><em>T</em></b></sub>(*E*)) where ***T*** is any truth of logic, we can think of (1.4) as telling us that

> *The probability of a hypothesis conditional on a body of data is equal to the unconditional probability of the hypothesis multiplied by the degree to which the hypothesis surpasses a tautology as a predictor of the data.*

In our J. Doe example, ***PR***(*H*, *E*) is obtained by comparing the predictability of senior status given that J. Doe died in 2000 to its predictability given no information whatever about his or her mortality. Dividing the former "prediction term" by the latter yields ***PR***(*H*, *E*) = **P**<sub><em>H</em></sub>(*E*)/**P**(*E*) = 0.57/0.06036 = 9.44. Thus, as a predictor of senior status in 2000, knowing that J. Doe died is more than nine times better than not knowing whether she lived or died.

Another useful form of Bayes' Theorem is the *Odds Rule*. In the jargon of bookies, the "odds" of a hypothesis is its probability divided by the probability of its negation: **O**(*H*) = **P**(*H*)**/P**(~*H*). So, for example, a racehorse whose odds of winning a particular race are 7-to-5 has a 7**/**12 chance of winning and a 5**/**12 chance of losing. To understand the difference between odds and probabilities it helps to think of probabilities as *fractions* of the distance between the probability of a contradiction and that of a tautology, so that **P**(*H*) = *p* means that *H* is *p* times as likely to be true as a tautology. In contrast, writing **O**(*H*) = [**P**(*H*) − **P**(***F***)]**/**[**P**(***T***) − **P**(*H*)] (where ***F*** is some logical contradiction) makes it clear that **O**(*H*) expresses this same quantity as the ratio of the amount by which *H*'s probability exceeds that of a contradiction to the amount by which it is exceeded by that of a tautology. Thus, the difference between "probability talk" and "odds talk" corresponds to the difference between saying "we are two thirds of the way there" and saying "we have gone twice as far as we have yet to go."

The analogue of the probability ratio is the *odds ratio* ***OR***(*H*, *E*) = **O**<sub><em>E</em></sub>(*H*)**/O**(*H*), the factor by which *H*'s unconditional odds must be multiplied to obtain its odds conditional on *E*. Bayes' Theorem is equivalent to the following fact about odds ratios:

> | **(1.5)** | **Odds Ratio Rule**. |
> | --- | --- |
> |   | ***OR***(*H*, *E*) = **P**<sub><em>H</em></sub>(*E*)**/P**<sub><em>~H</em></sub>(*E*) |

Notice the similarity between (1.4) and (1.5). While each employs a different way of *expressing* probabilities, each shows how *its* expression for *H*'s probability conditional on *E* can be obtained by multiplying *its* expression for *H*'s unconditional probability by a factor involving inverse probabilities.

The quantity ***LR***(*H*, *E*) = **P**<sub><em>H</em></sub>(*E*)**/P**<sub>~<em>H</em></sub>(*E*) that appears in (1.5) is the *likelihood ratio* of *H* given *E*. In testing situations like the one described in Example 1, the likelihood ratio is the test's true positive rate divided by its false positive rate: ***LR*** = sensitivity**/**(1 − specificity). As with the probability ratio, we can construe the likelihood ratio as a measure of the degree to which *H* predicts *E*. Instead of comparing *E*'s probability given *H* with its unconditional probability, however, we now compare it with its probability conditional on ~*H*. ***LR***(*H*, *E*) is thus the degree to which the hypothesis surpasses its negation as a predictor of the data. Once more, Bayes' Theorem tells us how to factor conditional probabilities into unconditional probabilities and measures of predictive power.

> *The odds of a hypothesis conditional on a body of data is equal to the unconditional odds of the hypothesis multiplied by the degree to which it surpasses its negation as a predictor of the data.*

In our running J. Doe example, ***LR***(*H*, *E*) is obtained by comparing the predictability of senior status given that J. Doe died in 2000 to its predictability given that he or she lived out the year. Dividing the former "prediction term" by the latter yields ***LR***(*H*, *E*) = **P**<sub><em>H</em></sub>(*E*)/**P**<sub>~<em>H</em></sub>(*E*) = 0.57/0.056 = 10.12. Thus, as a predictor of senior status in 2000, knowing that J. Doe died is more than ten times better than knowing that he or she lived.

The similarities between the "probability ratio" and "odds ratio" versions of Bayes' Theorem can be developed further if we express *H*'s probability as a multiple of the probability of some other hypothesis *H** using the *relative probability* function **B**(*H*, *H**) = **P**(*H*)**/P**(*H**). It should be clear that **B** generalizes both **P** and **O** since **P**(*H*) = **B**(*H*, ***T***) and **O**(*H*) = **B**(*H*, ~*H*). By comparing the conditional and unconditional values of **B** we obtain the *Bayes' Factor*:

> ***BR***(*H*, *H**; *E*) = **B**<sub><em>E</em></sub>(*H*, *H**)**/B**(*H*, *H**) = [**P**<sub><em>E</em></sub>(*H*)**/P**<sub><em>E</em></sub>(*H**)]**/** [**P**(*H*)**/P**(*H**)].

We can also generalize the likelihood ratio by setting ***LR***(*H*, *H**; *E*) = **P**<sub><em>H</em></sub>(*E*)**/P**<sub><em>H</em>*</sub>(*E*). This compares *E*'s predictability on the basis of *H* with its predictability on the basis of *H**. We can use these two quantities to formulate an even more general form of Bayes' Theorem.

> | **(1.6)** | **Bayes' Theorem** (General Form) |
> | --- | --- |
> |   | ***BR***(*H*, *H**; *E*) = ***LR***(*H*, *H**; *E*) |

The message of (1.6) is this:

> *The ratio of probabilities for two hypotheses conditional on a body of data is equal to the ratio their unconditional probabilities multiplied by the degree to which the first hypothesis surpasses the second as a predictor of the data.*

The various versions of Bayes' Theorem differ only with respect to the functions used to express unconditional probabilities (**P**(*H*), **O**(*H*), **B**(*H*)) and in the likelihood term used to represent predictive power (***PR***(*E*, *H*), ***LR***(*H*, *E*), ***LR***(*H*, *H**; *E*)). In each case, though, the underlying message is the same:

> *conditional probability = unconditional probability × predictive power*

(1.2) – (1.6) are multiplicative forms of Bayes' Theorem that use division to compare the disparities between unconditional and conditional probabilities. Sometimes these comparisons are best expressed additively by replacing ratios with *differences*. The following table gives the additive analogue of each ratio measure.

| **Ratio** | **Difference** |
| --- | --- |
| *Probability Ratio*  ***PR***(*H*, *E*) = **P**<sub><em>E</em></sub>(*H*)**/P**(*H*) | *Probability Difference* ***PD***(*H*, *E*) = **P**<sub><em>E</em></sub>(*H*) −** P**(*H*) |
| *Odds Ratio*  ***OR***(*H*, *E*) = **O**<sub><em>E</em></sub>(*H*)**/O**(*H*) | *Odds Difference*  ***OD***(*H*, *E*) = **O**<sub><em>E</em></sub>(*H*) − **O**(*H*) |
| *Bayes' Factor*  ***BR***(*H*, *H**; *E*) = **B**<sub><em>E</em></sub>(*H*, *H**)**/B**(*H*, *H**) | *Bayes' Difference*  ***BD***(*H*, *H**; *E*) = **B**<sub><em>E</em></sub>(*H*, *H**) − **B**(*H*, *H**) |

We can use Bayes' theorem to obtain additive analogues of (1.4) – (1.6), which are here displayed along with their multiplicative counterparts:

|   | **Ratio** | **Difference** |
| --- | --- | --- |
| (1.4) | ***PR***(*H*, *E*) = ***PR***(*E*, *H*) = **P**<sub><em>H</em></sub>(*E*)**/P**(*E*) | ***PD***(*H*, *E*) = **P**(*H*) [***PR***(*E*, *H*) − 1] |
| (1.5) | ***OR***(*H*, *E*) = ***LR***(*H*, *E*) = **P**<sub><em>H</em></sub>(*E*)**/P**<sub><em>~H</em></sub>(*E*) | ***OD***(*H*, *E*) = **O**(*H*) [***OR***(*H*, *E*) − 1] |
| (1.6) | ***BR***(*H*, *H**; *E*) = ***LR***(*H*, *H**; *E*) = **P**<sub><em>H</em></sub>(*E*)**/P**<sub><em>H*</em></sub>(*E*) | ***BD***(*H*, *H**; *E*) = **B**(*H*, *H**) [***BR***(*H*, *H**; *E*) − 1] |

Notice how each additive measure is obtained by multiplying *H*'s unconditional probability, expressed on the relevant scale, **P**, **O** or **B**, by the associated multiplicative measure diminished by 1.

While the results of this section are useful to anyone who employs the probability calculus, they have a special relevance for *subjectivist* or "Bayesian" approaches to statistics, epistemology, and inductive inference.[^note-5] Subjectivists lean heavily on conditional probabilities in their theory of evidential support and their account of empirical learning. Given that Bayes' Theorem is the single most important fact about conditional probabilities, it is not at all surprising that it should figure prominently in subjectivist methodology.

## 3. The Role of Bayes' Theorem in Subjectivist Accounts of Evidence

Subjectivists maintain that beliefs come in varying gradations of strength, and that an ideally rational person's graded beliefs can be represented by a *subjective probability function* **P**. For each hypothesis *H* about which the person has a firm opinion, **P**(*H*) measures her level of confidence (or "degree of belief") in *H*'s truth.[^note-6] Conditional beliefs are represented by conditional probabilities, so that **P**<sub><em>E</em></sub>(*H*) measures the person's confidence in *H on the supposition that E is a fact*.[^note-7]

One of the most influential features of the subjectivist program is its account of *evidential support*. The guiding ideas of this *Bayesian confirmation theory* are these:

- *Confirmational Relativity*. Evidential relationships must be relativized to individuals and their degrees of belief.
- *Evidence Proportionism.*[^note-8] A rational believer will proportion her confidence in a hypothesis *H* to her *total evidence* for *H*, so that her subjective probability for *H* reflects the overall balance of her reasons for or against its truth.
- *Incremental Confirmation.*[^note-9] A body of data provides *incremental* evidence for *H* to the extent that conditioning on the data raises *H*'s probability.

The first principle says that statements about evidentiary relationships always make implicit reference to people and their degrees of belief, so that, e.g., "*E* is evidence for *H*" should really be read as "*E* is evidence for *H* relative to the information encoded in the subjective probability **P**".

According to evidence proportionism, a subject's level of confidence in *H* should vary directly with the strength of her evidence in favor of *H*'s truth. Likewise, her level of confidence in *H* conditional on *E* should vary directly with the strength of her evidence for *H*'s truth when this evidence is augmented by the supposition of *E*. It is a matter of some delicacy to say precisely what constitutes a person's evidence,[^note-10] and to explain how her beliefs should be "proportioned" to it. Nevertheless, the idea that incremental evidence is reflected in disparities between conditional and unconditional probabilities only makes sense if differences in subjective probability mirror differences in *total* evidence.

An item of data provides a subject with *incremental* evidence for or against a hypothesis to the extent that receiving the data increases or decreases her total evidence for the truth of the hypothesis. When probabilities measure total evidence, the increment of evidence that *E* provides for *H* is a matter of the disparity between **P**<sub><em>E</em></sub>(*H*) and **P**(*H*). When odds are used it is a matter of the disparity between **O**<sub><em>E</em></sub>(*H*) and **O**(*H*). See Example 2 in the supplementary document "Examples, Tables, and Proof Sketches", which illustrates the difference between total and incremental evidence, and explains the "baserate fallacy" that can result from failing to properly distinguish the two.

It will be useful to distinguish two subsidiary concepts related to total evidence.

- The *net evidence in favor of H* is the degree to which a subject's total evidence in favor of *H* exceeds her total evidence in favor of ~*H*.
- The *balance of total evidence for H over H** is the degree to which a subject's total evidence in favor of *H* exceeds her total evidence in favor of *H**.

The precise content of these notions will depend on how total evidence is understood and measured, and on how disparities in total evidence are characterized. For example, if total evidence is given in terms of probabilities and disparities are treated as ratios, then the net evidence for *H* is **P**(*H*)**/P**(~*H*). If total evidence is expressed in terms of odds and differences are used to express disparities, then the net evidence for *H* will be **O**(*H*) − **O**(~*H*). Readers may consult Table 3 (in the supplementary document) for a complete list of the possibilities.

As these remarks make clear, one can interpret **O**(*H*) either as a measure of net evidence or as a measure of total evidence. To see the difference, imagine that 750 red balls and 250 black balls have been drawn at random and with replacement from an urn known to contain 10,000 red or black balls. Assuming that this is our only evidence about the urn's contents, it is reasonable to set **P**(*Red*) = 0.75 and **P**(~*Red*) = 0.25. On a probability-as-total-evidence reading, these assignments reflect both the fact that we have a great deal of evidence in favor of *Red* (namely, that 750 of 1,000 draws were red) and the fact that we have also have some evidence against it (namely, that 250 of the draws were black). The *net* evidence for *Red* is then the disparity between our total evidence for *Red* and our total evidence against *Red*. This can be expressed multiplicatively by saying that we have seen three times as many red draws as black draws, which is just to say that **O**(*Red*) = 3. Alternatively, we can use **O**(*Red*) as a measure of the total evidence by taking our evidence for *Red* to be the ratio of red to black draws, rather than the total number of red draws, and our evidence for ~*Red* to be the ratio of black balls to red balls, rather than the total number of black draws. While the decision whether to use **O** as a measure total or net evidence makes little difference to questions about the *absolute* amount of total evidence for a hypothesis (since **O**(*H*) is an increasing function of **P**(*H*)), it can make a major difference when one is considering the incremental *changes* in total evidence brought about by conditioning on new information.

Philosophers interested in characterizing correct patterns of inductive reasoning and in providing "rational reconstructions" of scientific methodology have tended to focus on incremental evidence as crucial to their enterprise. When scientists (or ordinary folk) say that *E* supports or confirms *H* what they generally mean is that learning of *E*'s truth will increase the total amount of evidence for *H*'s truth. Since subjectivists characterize total evidence in terms of subjective probabilities or odds, they analyze incremental evidence in terms of changes in these quantities. On such views, the simplest way to characterize the strength of incremental evidence is by making ordinal comparisons of conditional and unconditional probabilities or odds.

> | **(2.1)** | **A Comparative Account of Incremental Evidence**. |
> | --- | --- |
> |   | Relative to a subjective probability function **P**, *E* incrementally confirms (disconfirms, is irrelevant to) *H* if and only if **P**<sub><em>E</em></sub>(*H*) is greater than (less than, equal to) **P**(*H*). *H* receives a greater increment (or lesser decrement) of evidential support from *E* than from *E** if and only if **P**<sub><em>E</em></sub>(*H*) exceeds **P**<sub><em>E*</em></sub>(*H*). |

Both these equivalences continue to hold with probabilities replaced by odds. So, this part of the subjectivist theory of evidence does not depend on how total evidence is measured.

Bayes' Theorem helps to illuminate the content of (2.1) by making it clear that *E*'s status as incremental evidence for *H* is enhanced to the extent that *H* predicts *E*. This observation serves as the basis for the following conclusions about incremental confirmation (which hold so long as 1 > **P**(*H*), **P**(*E*) > 0).

> | **(2.1a)** | If *E* incrementally confirms *H*, then *H* incrementally confirms *E*. |
> | --- | --- |
> | **(2.1b)** | If *E* incrementally confirms *H*, then *E* incrementally disconfirms ~*H*. |
> | **(2.1c)** | If *H* entails *E*, then *E* incrementally confirms *H*. |
> | **(2.1d)** | If **P**<sub><em>H</em></sub>(*E*) = **P**<sub><em>H</em></sub>(*E**), then *H* receives more incremental support from *E* than from *E** if and only if *E* is unconditionally less probable than *E**. |
> | **(2.1e)** | *Weak Likelihood Principle*. *E* provides incremental evidence for *H* if and only if **P**<sub><em>H</em></sub>(*E*) > **P**<sub>~<em>H</em></sub>(*E*). More generally, if **P**<sub><em>H</em></sub>(*E*) > **P**<sub><em>H</em>*</sub>(*E*) and **P**<sub>~<em>H</em></sub>(~*E*) ≥ **P**<sub>~<em>H</em>*</sub>(~*E*), then *E* provides more incremental evidence for *H* than for *H**. |

(2.1a) tells us that incremental confirmation is a matter of *mutual reinforcement*: a person who sees *E* as evidence for *H* invests more confidence in the possibility that both propositions are true than in either possibility in which only one obtains.

(2.1b) says that relevant evidence must be capable of discriminating between the truth and falsity of the hypothesis under test.

(2.1c) provides a subjectivist rationale for the *hypothetico-deductive model of confirmation*. According to this model, hypotheses are incrementally confirmed by any evidence they entail. While subjectivists reject the idea that evidentiary relations can be characterized in a belief-independent manner — Bayesian confirmation is *always* relativized to a person and her subjective probabilities — they seek to preserve the basic insight of the H-D model by pointing out that hypotheses are incrementally supported by evidence they entail *for anyone who has not already made up her mind about the hypothesis or the evidence*. More precisely, if *H* entails *E*, then **P**<sub><em>E</em></sub>(*H*) = **P**(*H*)**/P**(*E*), which exceeds **P**(*H*) whenever 1 > **P**(*E*), **P**(*H*) > 0. This explains why scientists so often seek to design experiments that fit the H-D paradigm. Even when evidentiary relations are relativized to subjective probabilities, experiments in which the hypothesis under test entails the data will be regarded as evidentially relevant by *anyone* who has not yet made up his mind about the hypothesis or the data. The *degree* of incremental confirmation will vary among people depending on their prior levels of confidence in *H* and *E* , but everyone will agree that the data incrementally supports the hypothesis to at least some degree.

Subjectivists invoke (2.1d) to explain why scientists so often regard improbable or surprising evidence as having more confirmatory potential than evidence that is antecedently known. While it is not true *in general* that improbable evidence has more confirming potential, it is true that *E*'s incremental confirming power relative to *H* varies inversely with *E*'s unconditional probability *when the value of the inverse probability* **P**<sub><em>H</em></sub>(*E*) *is held fixed*. If *H* entails both *E* and *E**, say, then Bayes' Theorem entails that the least probable of the two supports *H* more strongly. For example, even if heart attacks are invariably accompanied by severe chest pain and shortness of breath, the former symptom is far better evidence for a heart attack than the latter simply because severe chest pain is so much less common than shortness of breath.

(2.1e) captures one core message of Bayes' Theorem for theories of confirmation. Let's say that *H* is *uniformly better* than *H** as predictor of *E*'s truth-value when (a) *H* predicts *E* more strongly than *H** does, and (b) ~*H* predicts ~*E* more strongly than ~*H** does. According to the weak likelihood principle, hypotheses that are uniformly better predictors of the data are better supported by the data. For example, the fact that little Johnny is a Christian is better evidence for thinking that his parents are Christian than for thinking that they are Hindu because (a) a far higher proportion of Christian parents than Hindu have Christian children, and (b) a far higher proportion of non-Christian parents than non-Hindu parents have non-Christian children.

Bayes' Theorem can also be used as the basis for developing and evaluating *quantitative* measures of evidential support. The results listed in Table 2 entail that all four of the functions ***PR***, ***OR***, ***PD*** and ***OD*** agree with one another on the simplest question of confirmation: Does *E* provide incremental evidence for *H*?

> | **(2.2)** | **Corollary**. |
> | --- | --- |
> |   | Each of the following is equivalent to the assertion that *E* provides incremental evidence in favor of *H*: ***PR***(*H*, *E*) > 1, ***OR***(*H*, *E*) > 1, ***PD***(*H*, *E*) > 0, ***OD***(*H*, *E*) > 0. |

Thus, all four measures agree with the comparative account of incremental evidence given in (2.1).

Given all this agreement it should not be surprising that ***PR***(*H*, *E*), ***OR***(*H*, *E*) and ***PD***(*H*, *E*), have all been proposed as measures of the *degree* of incremental support that *E* provides for *H*.[^note-11] While ***OD***(*H*, *E*) has not been suggested for this purpose, we will consider it for reasons of symmetry. Some authors maintain that one or another of these functions is the unique correct measure of incremental evidence; others think it best to use a variety of measures that capture different evidential relationships. While this is not the place to adjudicate these issues, we can look to Bayes' Theorem for help in understanding what the various functions measure and in characterizing the formal relationships among them.

All four measures agree in their conclusions about the *comparative* amount of incremental evidence that different items of data provide for a *fixed* hypothesis. In particular, they agree ordinally about the following concepts derived from incremental evidence:

- The *effective increment of evidence*[^note-12] that *E* provides for *H* is the amount by which the incremental evidence that *E* provides for *H* exceeds the incremental evidence that ~*E* provides for *H*.
- The *differential* in the incremental evidence that *E* and *E** provide for *H* is the amount by which the incremental evidence that *E* provides for *H* exceeds the incremental evidence that *E** provides for *H*.

Effective evidence is a matter of the degree to which a person's total evidence for *H* depends on her opinion about *E*. When **P**<sub><em>E</em></sub>(*H*) and **P**<sub>~<em>E</em></sub>(*H*) (or **O**<sub><em>E</em></sub>(*H*) and **O**<sub>~<em>E</em></sub>(*H*)) are far apart the person's belief about *E* has a great effect on her belief about *H*: from her point of view, a great deal hangs on *E*'s truth-value when it comes to questions about *H*'s truth-value. A large differential in incremental evidence between *E* and *E** tells us that learning *E* increases the subject's total evidence for *H* by a larger amount than learning *E** does. Readers may consult Table 4 (in the supplement) for quantitative measures of effective and differential evidence.

The second clause of (2.1) tells us that *E* provides more incremental evidence than *E** does for *H* just in case the probability of *H* conditional on *E* exceeds the probability of *H* conditional on *E**. It is then a simple step to show that all four measures of incremental support agree ordinally on questions of effective evidence and of differentials in incremental evidence.

> | **(2.3)** | **Corollary**. |
> | --- | --- |
> |   | For any *H*, *E** and *E* with positive probability, the following are equivalent: *E* provides more incremental evidence than *E** does for *H* ***PR***(*H*, *E*) > ***PR***(*H*, *E**) ***OR***(*H*, *E*) > ***OR***(*H*, *E**) ***PD***(*H*, *E*) > ***PD***(*H*, *E**) ***OD***(*H*, *E*) > ***OD***(*H*, *E**) |

The four measures of incremental support can disagree over the *comparative* degree to which a single item of data incrementally confirms two distinct hypotheses. Example 3, Example 4, and Example 5 (in the supplement) show the various ways in which this can happen.

All the differences between the measures have ultimately to do with (a) whether the *total* evidence in favor of a hypothesis should be measured in terms of probabilities or in terms of odds, and (b) whether *disparities* in total evidence are best captured as ratios or as differences. Rows in the following table correspond to different measures of total evidence. Columns correspond to different ways of treating disparities.

|   | **Ratio** | **Difference** |
| --- | --- | --- |
| **P** = Total | ***PR***(*H*, *E*) = **P**<sub><em>E</em></sub>(*H*)**/P**(*H*) | ***PD***(*H*, *E*) = **P**<sub><em>E</em></sub>(*H*) −** P**(*H*) |
| **O** = Total | ***OR***(*H*, *E*) = **O**<sub><em>E</em></sub>(*H*)**/O**(*H*) | ***OD***(*H*, *E*) = **O**<sub><em>E</em></sub>(*H*) −** O**(*H*) |

Similar tables can be constructed for measures of net evidence and measures of balances in total evidence. See Table 5A in the supplement.

We can use the various forms of Bayes' Theorem to clarify the similarities and differences among these measures by rewriting each of them in terms of likelihood ratios.

|   | **Ratio** | **Difference** |
| --- | --- | --- |
| **P** = Total | ***PR***(*H*, *E*) = ***LR***(*H*, ***T***; *E*) | ***PD***(*H*, *E*) = **P**(*H*)[***LR***(*H*, ***T***; *E*) − 1] |
| **O** = Total | ***OR***(*H*, *E*) = ***LR***(*H*, ~*H*; *E*) | ***OD***(*H*, *E*)= **O**(*H*)[***LR***(*H*, ~*H*; *E*) − 1] |

This table shows that there are two differences between each multiplicative measure and its additive counterpart. First, the likelihood term that appears in a given multiplicative measure is diminished by 1 in its associated additive measure. Second, in each additive measure the diminished likelihood term is multiplied by an expression for *H*'s probability: **P**(*H*) or **O**(*H*), as the case may be. The first difference marks no distinction; it is due solely to the fact that the multiplicative and additive measures employ a different zero point from which to measure evidence. If we settle on the point of probabilistic independence **P**<sub><em>E</em></sub>(*H*) = **P**(*H*) as a natural common zero, and so subtract 1 from each multiplicative measure,[^note-13] then equivalent likelihood terms appear in both columns.

The real difference between the measures in a given row concerns the effect of unconditional probabilities on relations of incremental confirmation. Down the right column, the degree to which *E* provides incremental evidence for *H* is directly proportional to *H*'s probability expressed in units of **P**(***T***) or **P**(~*H*). In the left column, *H*'s probability makes no difference to the amount of incremental evidence that *E* provides for *H* once **P**<sub><em>H</em></sub>(*E*) and either **P**(*E*) or **P**<sub>~<em>H</em></sub>(*E*) are fixed.[^note-14] In light of Bayes' Theorem, then, the difference between the ratio measures and then difference measures boils down to one question:

> *Does a given piece of data provide a greater increment of evidential support for a more probable hypothesis than it does for a less probable hypothesis when both hypotheses predict the data equally well?*

The difference measures answer yes, the ratio measures answer no.

Bayes' Theorem can also help us understand the difference between rows. The measures within a given row agree about the role of *predictability* in incremental confirmation. In the top row the incremental evidence that *E* provides for *H* increases linearly with **P**<sub><em>H</em></sub>(*E*)**/P**(*E*), whereas in the bottom row it increases linearly with **P**<sub><em>H</em></sub>(*E*)**/P**<sub><em>~H</em></sub>(*E*). Thus, when probabilities measure total evidence what matters is the degree to which *H* exceeds ***T*** as a predictor of *E*, but when odds measure total evidence it is the degree to which *H* exceeds ~*H* as a predictor of *E* that matters.

The central issue here concerns the status of the likelihood ratio. While everyone agrees that it should play a leading role in any quantitative theory of evidence, there are conflicting views about precisely what evidential relationship it captures. There are three possible interpretations.

| Probability as total evidence reading | ***PR***(*H*, *E*) measures incremental change in total evidence. ***LR***(*H*, *E*) measures incremental change in *net* evidence. ***LR***(*H*, *H**, *E*) measures incremental change in the balance of evidence that *E* provides for *H* over *H** |
| --- | --- |
| Odds as total evidence reading | ***LR***(*H*, *E*) measures incremental changes in total evidence. ***LR***(*H*, *E*)<sup>2</sup> measures incremental change in net evidence. ***LR***(*H*, *H**; *E*)**/*LR***(~*H*, ~*H**; *E*) measures incremental change in the balance of evidence that *E* provides for *H* over *H**. |
| "Likelihoodist" reading | Neither **P** nor **O** measures total evidence because evidential relations are essentially *comparative*; they always involve the balance of evidence. ***LR***(*H*, *E*) measures the balance of evidence that *E* provides for *H* over *H**. ***LR***(*H*, *H**; *E*) measures the balance of evidence that *E* provides for *H* over *H**. |

On the first reading there is no conflict whatsoever between using probability ratios and using likelihood ratios to measure evidence. Once we get clear on the distinctions between total evidence, net evidence and the balance of evidence, we see that each of ***PR***(*H*, *E*), ***LR***(*H*, *E*) and ***LR***(*H*, *H**; *E*) measures an important evidential relationship, but that the relationships they measure are importantly different.

When odds measure total evidence neither ***PR***(*H*, *E*) nor ***LR***(*H*, *H**; *E*) plays a fundamental role in the theory of evidence. Changes in the probability ratio for *H* given *E* only indicate changes in incremental evidence in the presence of information about changes in the probability ratio for ~*H* given *E*. Likewise, changes in the likelihood ratio for *H* and *H** given *E* only indicate changes in the balance of evidence in light of information about changes in the likelihood ratio for ~*H* and ~*H** given *E*. Thus, while each of the two functions can figure as one component in a meaningful measure of confirmation, neither tells us anything about incremental evidence when taken by itself.

The third view, "likelihoodism," is popular among non-Bayesian statisticians. Its proponents deny evidence proportionism. They maintain that a person's subjective probability for a hypothesis merely reflects her degree of uncertainty about its truth; it need not be tied in any way to the amount of evidence she has in its favor.[^note-15] It is likelihood ratios, not subjective probabilities, which capture the "scientifically meaningful" evidential relations. Here are two classic statements of the position.

> The ‘evidential meaning’ of experimental results is characterized fully by the likelihood function… Reports of experimental results in scientific journals should in principle be descriptions of likelihood functions. (Brinbaum 1962, 272)

On this view, everything that can be said about the evidential import of *E* for *H* is embodied in the following generalization of the weak likelihood principle:

> *The* "*Law of Likelihood*". If *H* implies that the probability of *E* is *x*, while *H** implies that the probability of *E* is *x**, then *E* is evidence supporting *H* over *H** if and only if *x* exceeds *x**, and the likelihood ratio, *x***/***x**, measures the strength of this support. (Hacking 1965, 106-109)[^hacking-1965], (Royall 1997, 3)[^royall-1997]

The biostatistician Richard Royall is a particularly lucid defender of likelihoodism (Royall 1997)[^royall-1997]. He maintains that any scientifically respectable concept of evidence must analyze the evidential impact of *E* on *H* solely in terms of likelihoods; it should not advert to anyone's unconditional probabilities for *E* or *H*. This is supposed to be because likelihoods are both better known and more objective than unconditional probabilities. Royall argues strenuously against the idea that incremental evidence can be measured in terms of the disparity between unconditional and conditional probabilities. Here is the gist of his complaint:

> Whereas [***LR***(*H*, *H**; *E*)] measures the support for one hypothesis *H* relative to a specific alternative *H**, without regard either to the prior probabilities of the two hypotheses or to what other hypotheses might also be considered, the law of changing probability [as measured by ***PR***(*H*, *E*)] measures support for *H* relative to a specific prior distribution over *H* and its alternatives... The law of changing probability is of limited usefulness in scientific discourse because of its dependence on the prior probability distribution, which is generally unknown and/or personal. Although you and I agree (on the basis of the law of likelihood) that given evidence supports *H* over *H**, and *H*** over both *H* and *H**, we might disagree about whether it is evidence supporting *H* (on the basis of the law of changing probability) purely on the basis of our different judgments of the priori probability of *H*, *H**, and *H***. (Royall 1997, 10-11, with slight changes in notation)[^royall-1997]

Royall's point is that neither the probability ratio nor probability difference will capture the sort of objective evidence required by science because their values depend on the "subjective" terms **P**(*E*) and **P**(*H*), and not just on the "objective" likelihoods **P**<sub><em>H</em></sub>(*E*) and **P**<sub>~<em>H</em></sub>(*E*).

Whether one agrees with this assessment will be a matter of philosophical temperament, in particular of one's willingness to tolerate subjective probabilities in one's account of evidential relations. It will also depend crucially on the extent to which one is convinced that likelihoods are better known and more objective than ordinary subjective probabilities. Cases like the one envisioned in the law of likelihood, where hypotheses *deductively entails* a definite probability for the data, are relatively rare. So, unless one is willing to adopt a theory of evidence with a very restricted range of application, a great deal will turn on how easy it is to determine objective likelihoods in situations where the predictive connection from hypothesis to data is itself the result of *inductive* inferences. However one comes down on these issues, though, there is no denying that likelihood ratios will play a central role in any probabilistic account of evidence.

In fact, the weak likelihood principle (2.1e) encapsulates a minimal form of Bayesianism to which all parties can agree. This is clearest when it is restated in terms of likelihoods.

> | **(2.1e)** | **The Weak Likelihood Principle**. (expressed in terms of likelihood ratios) |
> | --- | --- |
> |   | If ***LR***(*H*, *H**; *E*) ≥ 1 and ***LR***(~*H*, ~*H**; ~*E*) ≥ 1, with one inequality strict, then *E* provides more incremental evidence for *H* than for *H** and ~*E* provides more incremental evidence for ~*H* than for ~*H**. |

Likelihoodists will endorse (2.1e) because the relationships described in its antecedent depend only on inverse probabilities. Proponents of both the "probability" and "odds" interpretations of total evidence will accept (2.1e) because satisfaction of its antecedent ensures that conditioning on *E* increases *H*'s probability and its odds strictly more than those of *H**. Indeed, the weak likelihood principle must be an integral part of any account of evidential relevance that deserves the title "Bayesian". To deny it is to misunderstand the central message of Bayes' Theorem for questions of evidence: namely, that hypotheses are confirmed by data they predict. As we shall see in the next section, this "minimal" form of Bayesianism figures importantly into subjectivist models of learning from experience.

## 4. The Role of Bayes' Theorem in Subjectivist Models of Learning

Subjectivists think of learning as a process of *belief revision* in which a "prior" subjective probability **P** is replaced by a "posterior" probability **Q** that incorporates newly acquired information. This process proceeds in two stages. First, some of the subject's probabilities are *directly altered* by experience, intuition, memory, or some other *non-inferential* learning process. Second, the subject "updates" the rest of her opinions to bring them into line with her newly acquired knowledge.

Many subjectivists are content to regard the initial belief changes as *sui generis* and independent of the believer's prior state of opinion. However, as long as the first phase of the learning process is understood to be non-inferential, subjectivism can be made compatible with an "externalist" epistemology that allows for criticism of belief changes in terms the reliability of the causal processes that generate them. It can even accommodate the thought that the direct effect of experience might depend causally on the believer's prior probability.

Subjectivists have studied the second, inferential phase of the learning process in great detail. Here immediate belief changes are seen as imposing constraints of the form "the posterior probability **Q** has such-and-such properties." The objective is to discover what sorts of constraints experience tends to impose, and to explain how the person's *prior* opinions can be used to justify the choice of a posterior probability from among the many that might satisfy a given constraint. Subjectivists approach the latter problem by assuming that the agent is justified in adopting whatever eligible posterior *departs minimally* from her prior opinions. This is a kind of "no jumping to conclusions" requirement. We explain it here as a natural result of the idea that rational learners should proportion their beliefs to the strength of the evidence they acquire.

The simplest learning experiences are those in which the learner becomes certain of the truth of some proposition *E* about which she was previously uncertain. Here the constraint is that all hypotheses inconsistent with *E* must be assigned probability zero. Subjectivists model this sort of learning as *simple conditioning*, the process in which the prior probability of each proposition *H* is replaced by a posterior that coincides with the prior probability of *H* conditional on *E*.

> | **(3.1)** | **Simple Conditioning** |
> | --- | --- |
> |   | If a person with a "prior" such that 0 < **P**(*E*) < 1 has a learning experience whose sole immediate effect is to raise her subjective probability for *E* to 1, then her post-learning "posterior" for any proposition *H* should be **Q**(*H*) = **P**<sub><em>E</em></sub>(*H*). |

In short, a rational believer who learns for certain that *E* is true should factor this information into her doxastic system by conditioning on it.

Though useful as an ideal, simple conditioning is not widely applicable because it requires the learner to become absolutely *certain* of *E*'s truth. As Richard Jeffrey has argued (Jeffrey 1987)[^jeffrey-1987], the evidence we receive is often too vague or ambiguous to justify such "dogmatism." On more realistic models, the direct effect of a learning experience will be to *alter* the subjective probability of some proposition without raising it to 1 or lowering it to 0. Experiences of this sort are appropriately modeled by what has come to be called *Jeffrey conditioning* (though Jeffrey's preferred term is "probability kinematics").

> | **(3.2)** | **Jeffrey Conditioning** |
> | --- | --- |
> |   | If a person with a prior such that 0 < **P**(*E*) < 1 has a learning experience whose sole immediate effect is to change her subjective probability for *E* to *q*, then her post-learning posterior for any *H* should be **Q**(*H*) = *q***P**<sub><em>E</em></sub>(*H*) + (1 − *q*)**P**<sub>~<em>E</em></sub>(*H*). |

Obviously, Jeffrey conditioning reduces to simple conditioning when *q* = 1.

A variety of arguments for conditioning (simple or Jeffrey-style) can be found in the literature, but we cannot consider them here.[^note-16] There is, however, one sort of justification in which Bayes' Theorem figures prominently. It exploits connections between belief revision and the notion of incremental evidence to show that conditioning is the *only* belief revision rule that allows learners to correctly proportion their posterior beliefs to the new evidence they receive.

The key to the argument lies in marrying the "minimal" version of Bayesian expressed in the (2.1e) to a very modest "proportioning" requirement for belief revision rules.

> | **(3.3)** | **The Weak Evidence Principle** |
> | --- | --- |
> |   | If, relative to a prior **P**, *E* provides at least as much incremental evidence for *H* as for *H**, and if *H* is antecedently more probable than *H**, then *H* should remain more probable than *H** after any learning experience whose sole immediate effect is to increase the probability of *E*. |

This requires an agent to retain his views about the relative probability of two hypotheses when he acquires evidence that supports the more probable hypothesis more strongly. It rules out obviously irrational belief revisions such as this: George is more confident that the New York Yankees will win the American League Pennant than he is that the Boston Rex Sox will win it, but he reverses himself when he learns (only) that the Yankees beat the Red Sox in last night's game.

Combining (3.3) with minimal Bayesianism yields the following:

> | **(3.4)** | **Consequence** |
> | --- | --- |
> |   | If a person's prior is such that ***LR***(*H*, *H**; *E*) ≥ 1, ***LR***(~*H*, ~*H**; ~*E*) ≥ 1, and **P**(*H*) > **P**(*H**), then any learning experience whose sole immediate effect is to raise her subjective probability for *E* should result in a posterior such that **Q**(*H*) > **Q**(*H**). |

On the reasonable assumption that **Q** is defined on the same set of propositions over which **P** is defined, this condition suffices to pick out simple conditioning as the *unique* correct method of belief revision for learning experiences that make *E* certain. It picks out Jeffrey conditioning as the *unique* correct method when learning merely alters one's subjective probability for *E*. The argument for these conclusions makes use of the following two facts about probabilities.

> | **(3.5)** | **Lemma** |
> | --- | --- |
> |   | If *H* and *H** both entail *E* when **P**(*H*) > **P**(*H**), then ***LR***(*H*, *H**; *E*) = 1 and ***LR***(~*H*, ~*H**; ~*E*) > 1. |
> |   | Proof Sketch |
> **(3.6)** **Lemma** Simple conditioning on *E* is the only rule for revising subjective probabilities that yields a posterior with the following properties for *any* prior such that **P**(*E*) > 0: **Q**(*E*) = 1. *Ordinal Similarity*. If *H* and *H** both entail *E*, then **P**(*H*) ≥ **P**(*H**) if and only if **Q**(*H*) ≥ **Q**(*H**). Proof Sketch

From here the argument for simple conditioning is a matter of using (3.4) and (3.5) to establish ordinal similarity. Suppose that *H* and *H** entail *E* and that **P**(*H*) > **P**(*H**). It follows from (3.5) that ***LR***(*H*, *H**; *E*) = 1 and ***LR***(~*H*, ~*H**; ~*E*) > 1. (3.4) then entails that any learning experience that raises *E*'s probability must result in a posterior with **Q**(*H*) > **Q**(*H**). Thus, **Q** and **P** are ordinally similar with respect to hypotheses that entail *H*. If we go on to suppose that the learning experience raises *E*'s probability to 1, then (3.6) then guarantees that **Q** arises from **P** by simple conditioning on *E*.

The case for Jeffrey conditioning is similarly direct. Since the argument for ordinal similarity did not depend at all on the assumption that **Q**(*E*) = 1, we have really established

> | **(3.7)** | **Corollary** |
> | --- | --- |
> |   | • If *H* and *H** entail *E*, then **P**(*H*) > **P**(*H**) if and only if **Q**(*H*) > **Q**(*H**). |
> |   | • If *H* and *H** entail ~*E*, then **P**(*H*) > **P**(*H**) if and only if **Q**(*H*) > **Q**(*H**). |

So, **Q** is ordinally similar to **P** both when restricted to hypotheses that entail *E* and when restricted to hypotheses than entail ~*E*. Moreover, since dividing by positive numbers does not disturb ordinal relationships, it also follows that that **Q**<sub><em>E</em></sub> is ordinally similar to **P** when restricted to hypotheses that entail *E*, and that **Q**<sub>~<em>E</em></sub> is ordinally similar to **P** when restricted to hypotheses than entail ~*E*. Since **Q**<sub><em>E</em></sub>(*E*) = 1 = **Q**<sub>~<em>E</em></sub>(*E*), (3.6) then entails:

> | **(3.8)** | **Consequence** |
> | --- | --- |
> |   | For every proposition *H*, **Q**<sub><em>E</em></sub>(*H*) = **P**<sub><em>E</em></sub>(*H*) and **Q**<sub>~<em>E</em></sub>(*H*) = **P**<sub>~<em>E</em></sub>(*H*) |

It is easy to show that (3.8) is necessary and sufficient for **Q** to arise from **P** by Jeffrey conditioning on *E*. Subject to the constraint **Q**(*E*) = *q*, it guarantees that **Q**(*H*) = *q***P**<sub><em>E</em></sub>(*H*) + (1 −*q*)**P**<sub>~<em>E</em></sub>(*H*).

The general moral is clear.

> *The basic Bayesian insight embodied in the weak likelihood principle (2.1e) entails that simple and Jeffrey conditioning on E* are the only* rational ways to revise beliefs in response to a learning experience whose sole immediate effect is to alter E*'s probability.

While much more can be said about simple conditioning, Jeffrey conditioning and other forms of belief revision, these remarks should give the reader a sense of the importance of Bayes' Theorem in subjectivist accounts of learning and evidential support. Though a mathematical triviality, the Theorem's central insight — that a hypothesis is supported by any body of data it renders probable — lies at the heart of all subjectivist approaches to epistemology, statistics, and inductive logic.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=bayes-theorem). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/bayes-theorem/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=bayes-theorem&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](http://philpapers.org/sep/bayes-theorem/) at [PhilPapers](http://philpapers.org), with links to its database. |

## Other Internet Resources

## Related Entries

## Notes（原文脚注）

[^note-1]: Though one can view conditional probabilities as basic, and even make sense of them when the conditioning event has probability zero, we stick to the standard definition here. Whenever **P***<sub>E</sub>* appears it is assumed that *E*'s probabilty is positive. For discussion of generalized conditional probabilities and useful references see (Renyi, 1955), (Harper, 1976), (Sphon, 1986), (Hammond, 1994), (McGee, 1994) and (Joyce 1999, 201-213)[^joyce-1999].

[^note-2]: **P***<sub>E</sub>* must be a real-valued function, bounded between zero and one, that satisfies:

[^note-3]: More generally, if {*E*<sub>1</sub>, *E*<sub>2</sub>, *E*<sub>3</sub>,…} is a countable *partition* of evidence propositions, mixing entails that **P**(*H*) = Σ<sub>i</sub>**P**(*E*<sub><em>i</em></sub>)** P**<sub><em>E</em></sub>*i*(*H*). One can think of the *E*<sub><em>i</em></sub> as a set of mutually exclusive and collectively exhaustive results for some experiment. Mixing then says that *H*'s unconditional probability is the *expectation* of it probability conditional on the results of the experiment.

[^note-4]: If *H*<sub>1</sub>, *H*<sub>2</sub>, *H*<sub>3</sub>,…, *H<sub>n</sub>* is a partition for which each of the inverse probabilities **P***<sub>H</sub>*i(*E*) is known, then one can express the direct probability as **P***<sub>E</sub>*(*H<sub><em>i</em></sub>*) = **P**(*H<sub><em>i</em></sub>*)**P*** <sub>H</sub>*i(*E*)**/**[Σ<sub><em>j</em></sub> **P**(*H<sub>j</sub>*)**P***<sub>H</sub>j*(* E*)].

[^note-5]: For an excellent general discussion of subjectivism see the entry interpretations of probability in this *Encyclopedia*.

[^note-6]: When the person's opinions about *H* are not sufficiently definite to be measured by a single number, her belief state is represented by a family of probability functions. For useful discussions of indeterminate belief states see (Levi, 1985), (Jeffrey, 1987) and (Kaplan 1996, pp. 23-31)[^kaplan-1996].

[^note-7]: One can have a determinate subjective probability for *H* conditional on *E* even when one lacks determinate probabilities for *H* & *E* and *E*. Statistical evidence often justifies assignments of conditional probability without providing any information about underlying unconditional probabilities. For example, careful study of actuarial tables might convince me that my chances of living past eighty given that I have a serious heart attack in my fifties are between 0.04 and 0.02, but the same table might give me no information whatever about the chances that I will suffer a serious heart attack in my fifties, and so no information about my unconditional chances of living to eighty.

[^note-8]: I take this term from Alvin Goldman, who argues *against* the view (Goldman 1986, 89-93). While not all Bayesians accept evidence proportionism, the account of incremental evidence as change in subjective probability really only makes sense if one supposes that a subject's level of confidence in a proposition varies directly with the strenght of her evidence for its truth.

[^note-9]: The distinction between the total and incremental evidence is essentially the same as Carnap's distinction between "confirmation as firmness" and "confirmation as increase in firmness" (Carnap 1962, new preface)[^carnap-1962]. Compare (Maher 1996, 162)[^maher-1996].

[^note-10]: On a pure subjectivist conception, a person's total evidence for a hypothesis derives from her own "subjective" views about the intrinsic plausibilities of propositions and from information she acquires via learning. The person begins with a subjective probability **P**<sub>0</sub> that encapsulates her "prior" judgments about the plausibilities of propositions (or, more accurately, her initial epistemic prejudices). She subsequently revises these probabilities in light of experience, thereby incorporating new information into her doxastic system. Her subjective probabilities at any time are thus the result of augmenting her "prior" opinions about the intuitive plausibilities of propositions with information acquired via learning. While some subjecivists speak as if each person starts her epistemic life with a kind of "ur-prior" that captures the state of her opinions before any empirical information comes it, such talk is misleading. Talk of "prior" and "posterior" probabilities only makes sense relative to a specific prospective sequence of learning experiences. The "prior" is nothing more than the probability function that reflects the person's beliefs, however arrived at, before learning commences. As Elliot Sober puts it, "the prior probability is properly so called, not because it is *a priori* (it is not), but because it is in place prior to taking the new evidence into account." (Sober 2002, 24)[^sober-2002]. Some probabilists, less inclined to subjective approaches, adopt less permissive conceptions of evidence. See, for example, (Williamson 2000, 184-208)[^williamson-2000] and (Maher 1996)[^maher-1996].

[^note-11]: For a thorough survey of the literature in this area, with penetrating commentary, see Fitelson 2001, chapters 1 and 2, a link to which can be found in the Other Internet Resources section of this entry. Other functions have been proposed as measures of evidential support as well, among them **P**(*H* & *E*) − **P**(*H*)**P**(*E*) see (Carnap 1962, 360)[^carnap-1962], **P**<sub><em>H</em></sub>(*E*) − **P**<sub>~<em>H</em></sub>(*E*) see (Nozick 1981, 252)[^nozick-1981], and **P**<sub><em>H</em></sub>(*E*) − **P**(*E*) see (Halina 1988), and **P**<sub><em>E</em></sub>(*H*) − **P**<sub>~<em>E</em></sub>(*H*) see (Joyce 1999)[^joyce-1999] and (Christensen 1999)[^christensen-1999]. As Fitelson shows, none of these measures satisfies the second clause of (2.1), which means than none captures the notion of *incremental* evidnece we are after.

[^note-12]: While the term "effective evidence" is not standard, the idea that the disparity between **P**<sub><em>E</em></sub>(*H*) and **P**<sub>~<em>E</em></sub>(*H*) captures an important evidential relationship is defended in (Joyce 1999, 203-213)[^joyce-1999] and (Christensen 1999)[^christensen-1999]. Both authors argue that this measure helps Bayesians circumvent the so-called "old evidence" problem described in (Glymour 1980)[^glymour-1980].

[^note-13]: An alternative would be to take the *logarithm* of each measure. Logarithmic scales are quite different from additive scales, however, since they express quantities in terms of multiples of a common base rather than distances from a common zero. Thus, on a logarithmic scale equal distances represent equal *ratios* of increases in evidence, not equal *increments* of evidence. To compare apples and apples, we must express the multiplicative measures on an additive scale (or the additive ones on a multiplicative scale).

[^note-14]: Consider, for example, two probabilities, **P** and **Q**, related by the following transformation:

[^note-15]: For a clear statement of this position see (Royall 1997, 8-11)[^royall-1997].

[^note-16]: See, for example, (Teller 1976)[^teller-1976], (Armendt 1980)[^armendt-1980], (Skyrms 1987)[^skyrms-1987] and (van Fraassen 1999).

[^armendt-1980]: Armendt, B. 1980. "Is There a Dutch Book Argument for Probability Kinematics?", *Philosophy of Science* **47**, 583-588.

[^bayes-1764]: Bayes, T. 1764. "An Essay Toward Solving a Problem in the Doctrine of Chances", *Philosophical Transactions of the Royal Society of London* **53**, 370-418. [[Fascimile available online](https://web.archive.org/web/20190126111142/http://www.stat.ucla.edu/history/essay.pdf): the original essay with an introduction by his friend Richard Price]

[^birnbaum-1962]: Birnbaum A. 1962. "On the Foundations of Statistical Inference", *Journal of the American Statistical Association* **53**, 259-326.

[^carnap-1962]: Carnap, R. 1962. *Logical Foundations of Probability*, 2nd edition. Chicago: University of Chicago Press.

[^chihara-1987]: Chihara, C. 1987. "Some Problems for Bayesian Confirmation Theory", *British Journal for the Philosophy of Science* **38**, 551-560.

[^christensen-1999]: Christensen, D. 1999. "Measuring Evidence", *Journal of Philosophy* **96**, 437-61.

[^dale-1989]: Dale, A. I. 1989. "Thomas Bayes: A Memorial", *The Mathematical Intelligencer* **11**, 18-19.

[^dale-1999]: ----- 1999. *A History of Inverse Probability*, 2nd edition. New York: Springer-Verlag.

[^earman-1992]: Earman, J. 1992. *Bayes or Bust?* Cambridge, MA: MIT Press.

[^edwards-1972]: Edwards, A. W. F. 1972. *Likelihood*. Cambridge: Cambridge University Press.

[^glymour-1980]: Glymour, Clark. 1980. *Theory and Evidence*. Princeton: Princeton University Press.

[^hacking-1965]: Hacking, Ian. 1965. *Logic of Statistical Inference*. Cambridge: Cambridge University Press.

[^hájek-2003]: Hájek, A. 2003. "Interpretations of the Probability Calculus", in the *Stanford Encyclopedia of Philosophy*, (Summer 2003 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/sum2003/entries/probability-interpret/](https://plato.stanford.edu/archives/sum2003/entries/probability-interpret/)>

[^hammond-1994]: Hammond, P. 1994. "Elementary non-Archimedean Representations for of Probability for Decision Theory and Games," in P. Humphreys, ed., *Patrick Suppes: Scientific Philosopher, vol. 1*., Dordrecht: Kluwer Publishers, 25-62.

[^harper-1976]: Harper, W. 1976. "Rational Belief Change, Popper Functions and Counterfactuals," in W. Harper and C. Hooker, eds., *Foundations of Probability Theory, Statistical Inference, and Statistical Theories of Science, vol. I*. Dordrecht: Reidel, 73-115.

[^hartigan-1983]: Hartigan, J. A. 1983. *Bayes Theory*. New York: Springer-Verlag.

[^howson-1985]: Howson, Colin. 1985. "Some Recent Objections to the Bayesian Theory of Support", *British Journal for the Philosophy of Science*, **36**, 305-309.

[^jeffrey-1987]: Jeffrey, R. 1987. "Alias Smith and Jones: The Testimony of the Senses", *Erkenntnis* **26**, 391-399.

[^jeffrey-1992]: ----- 1992. *Probability and the Art of Judgment*. New York: Cambridge University Press.

[^joyce-1999]: Joyce, J. M. 1999. *The Foundations of Causal Decision Theory*. New York: Cambridge University Press.

[^kahneman-1973]: Kahneman, D. and Tversky, A. 1973. "On the psychology of prediction", *Psychological Review* **80**, 237-251.

[^kaplan-1996]: Kaplan, M. 1996. *Decision Theory as Philosophy*. Cambridge: Cambridge University Press.

[^levi-1985]: Levi, I. 1985. "Imprecision and Indeterminacy in Probability Judgment", *Philosophy of Science* **53**, 390-409.

[^maher-1996]: Maher, P. 1996. "Subjective and Objective Confirmation", *Philosophy of Science* **63**, 149-174.

[^mcgee-1994]: McGee, V. 1994. "Learning the Impossible," in E. Eells and B. Skyrms, eds., *Probability and Conditionals*. New York: Cambridge University Press, 179-200.

[^mortimer-1988]: Mortimer, Halina. 1988. *The logic of induction*, Ellis Horwood Series in Artificial Intelligence, New York; Halsted Press.

[^nozick-1981]: Nozick, R. 1981. *Philosophical Explanations*. Cambridge: Harvard University Press.

[^renyi-1955]: Renyi, A. 1955. "On a New Axiomatic Theory of Probability", *Acta Mathematica Academiae Scientiarium Hungaricae* **6**, 285-335.

[^royall-1997]: Royall, R. 1997. *Statistical Evidence: A Likelihood Paradigm*. New York: Chapman & Hall/CRC.

[^skyrms-1987]: Skyrms, B. 1987. "Dynamic Coherence and Probability Kinematics". *Philosophy of Science* **54**, 1-20.

[^sober-2002]: Sober, E. 2002. "Bayesianism — its Scope and Limits", in Swinburne (2002), 21-38.

[^sphon-1986]: Sphon, W. 1986. "The Representation of Popper Measures", *Topoi* **5**, 69-74.

[^stigler-1982]: Stigler, S. M. 1982. "Thomas Bayes' Bayesian Inference", *Journal of the Royal Statistical Society, series A* **145**, 250-258.

[^swinburne-2002]: Swinburne, R. 2002. *Bayes' Theorem*. Oxford: Oxford University Press (published for the British Academy).

[^talbot-2001]: Talbot, W. 2001. "Bayesian Epistemology", *Stanford Encyclopedia of Philosophy* (Fall 2001 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/fall2001/entries/epistemology-bayesian/](https://plato.stanford.edu/archives/fall2001/entries/epistemology-bayesian/)>

[^teller-1976]: Teller, P. 1976. "Conditionalization, Observation, and Change of Preference", in W. Harper and C.A. Hooker, eds., *Foundations of Probability Theory, Statistical Inference, and Statistical Theories of Science*. Dordrecht: D. Reidel.

[^williamson-2000]: Williamson, T. 2000. *Knowledge and its Limits*. Oxford: Oxford University Press.

[^van-1999]: Van Fraassen, B. 1999. "A New Argument for Conditionalization". *Topoi* **18**, 93-96.

[^fitelson-2001]: Fitelson, B. 2001. *Studies in Bayesian Confirmation Theory*, Ph.D. Dissertation, University of Wisconsin. [[Preprint in PDF available online](http://fitelson.org/thesis.pdf)] (750K download) <!--LINK CHECKER COMMENTED OUT (Wed May 1 14:29:06 PDT 2019)

[^bayes'-2008]: [Bayes' Original Essay](http://www.stat.ucla.edu/history/essay.pdf) (in PDF) (UCLA Statistics Department/[History of Statistics](http://www.stat.ucla.edu/history/)) LINK CHECKER--> <!-- COMMENTED OUT BY LINK CHECKER (Thu Oct 9 04:49:17 2008)

[^portrait-2007]: [A Portrait, perhaps of Thomas Bayes](http://www.stat.ucla.edu/history/people/bayes.gif) (UCLA Statistics Department/[History of Statistics](http://www.stat.ucla.edu/history/)) --> <!-- COMMENTED OUT BY LINK CHECKER (Thu Oct 25 08:26:11 2007)

[^bayesian-2005]: [Bayesian Inference for the Physical Sciences](http://astrosun.tn.cornell.edu/staff/loredo/bayes/) (Tom Loredo, Astronomy, Cornell) --> <!-- COMMENTED OUT BY LINK CHECKER (Tue Feb 1 03:35:22 2005)
