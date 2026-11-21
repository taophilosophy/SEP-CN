# bayes-theorem — supplement（supplement）

> （《bayes-theorem》词条补充材料，源：plato.stanford.edu/entries/bayes-theorem/supplement.html）

#### Supplement to Bayes’ Theorem

## Examples, Tables, and Proof Sketches

### Example 1: Random Drug Testing

Joe is a randomly chosen member of a large population in which 3% are heroin users. Joe tests positive for heroin in a drug test that correctly identifies users 95% of the time and correctly identifies nonusers 90% of the time. To determine the probability that Joe uses heroin (= *H*) given the positive test result (= *E*), we apply Bayes' Theorem using the values

- Sensitivity = **P***_{H}*(*E*) = 0.95
- Specificity = 1 − **P**_{~*H*}(*E*) = 0.90
- Baseline "prior" probability = **P**(*H*) = 0.03.

Calculation then shows that **P***_{E}*(*H*) = 0.03×0.95**/**[0.03×0.95 + 0.97×0.1] = 0.227. So, even though the post-test probability of Joe being a user is more than seven times greater than that of the population at large, it still remains fairly unlikely that Joe is a user. (Notice how a positive result on a fairly reliable test can leave *H*'s probability quite small when its initial baseline probability starts out small!)

[Back to Text]

### Example 2: Random Drug Testing, Again

Recall that Joe, a random member of a population in which 3% use heroin, tests positive for heroin in a test of sensitivity 0.95 and specificity 0.90. Since **P***_{E}*(*H*) = 0.227 exceeds **P**(*H*) = 0.03, this result provides strong *incremental* evidence for thinking that Joe uses heroin. Nevertheless, the *total* evidence for this conclusion remains weak. Since heroin use is so rare in the population at large it is far more likely that the test is wrong in this instance than that Joe is a user.

Notice how incremental and total evidence make different uses of information about the base rate of heroin use in the population. When asking questions about incremental confirmation one ignores the base rate entirely because it is incorporated into *both* **P**(*H*) and **P***_{E}*(*H*). But, when asking questions about total evidence one must attend closely to the base rate, which almost always provides evidentially relevant information about the hypothesis. In Joe's case, for example, the low base rate swamps the positive test result. People often commit the "base rate fallacy" (Kahneman & Tversky 1973, 237-251) by mistaking incremental evidence for total evidence. They treat the result of a highly, but not completely, reliable test as though it provides conclusive evidence for the truth of some hypothesis even though the antecedent improbability of the hypothesis should lead them to question the accuracy of the test result in the case at hand.

[Back to text]

### Table 3: Measures related to total evidence

**P**(*H*) as total evidence for *H*

|   | **Multiplicative** | **Additive** |
| --- | --- | --- |
| NET | **P**(*H*)**/P**(~ *H*) = **O**(*H*) | **P**(*H*) − **P**(~*H*) = 2[**P**(*H*) − 1/2] |
| BALANCE | **P**(*H*)**/P**(*H*\*) = **B**(*H*, *H*\*) | **P**(*H*) − **P**(*H*\*) = **P**(*H* & ~*H*\*) − **P**(~*H* & *H*\*) |

**O**(*H*) as total evidence for *H*

|   | **Multiplicative** | **Additive** |
| --- | --- | --- |
| NET | **O**(*H*)**/O**(~ *H*) = **O**(*H*)² | **O**(*H*) − **O**(~*H*) = [**P**(*H*) − **P**(~*H*)]**/P**(~ *H*)**P**(*H*) |
| BALANCE | **O**(*H*)**/O**(*H*\*) = **B**(*H*, *H*\*)**/B**(~*H*, ~*H*\*) | **O**(*H*) − **O**(*H*\*) = [**P**(*H*) − **P**(*H*\*)]**/P**(~ *H*)**P**(~*H*\*) |

[Back to Text]

### Table 4: Measures of incremental evidence for fixed *H* and variable *E*

**P**(*H*) as total evidence for *H*

|   | **Ratio** | **Difference** |
| --- | --- | --- |
| Effective | ***PR***(*H*, *E*)**/*PR***(*H*, ~*E*) = **P**_{*E*}(*H*)**/** **P**_{~*E*}(*H*) = ***LR***(*E*, *H*) | ***PD***(*H*, *E*) − ***PD***(*H*, ~*E*) = **P**_{*E*}(*H*) − **P**_{~*E*}(*H*) |
| Differential | ***PR***(*H*, *E*)**/*PR***(*H*, *E*\*) = **P**_{*E*}(*H*)**/** **P**_{*E*\*}(*H*) = ***LR***(*E*, *E*\*; *H*) | ***PD***(*H*, *E*) − ***PD***(*H*, *E*\*) = **P**_{*E*}(*H*) − **P**_{*E*\*}(*H*) |

**O**(*H*) as total evidence for *H*

|   | **Ratio** | **Difference** |
| --- | --- | --- |
| Effective | ***OR***(*H*, *E*)**/*OR***(*H*, ~*E*) = **O**_{*E*}(*H*)**/** **O**_{~*E*}(*H*) = [**P**(*E* & *H*)**P**(~*E* & ~*H*)]**/**[**P**(*E* & ~*H*)**P**(~*E* & *H*)] | ***OD***(*H*, *E*) − ***OD***(*H*, ~*E*) = [**P**(*E* & *H*)**/**[**P**(*E* & ~*H*)] − [**P**(~*E* & *H*)**/P**(~*E* & ~*H*)] |
| Differential | ***OR***(*H*, *E*)**/*OR***(*H*, *E*\*) = **O**_{*E*}(*H*)**/** **O**_{*E*\*}(*H*) = [**P**(*E* & *H*)**P**(*E*\* & ~*H*)]**/**[**P**(*E* & ~*H*)**P**(*E*\* & *H*)] | ***PD***(*H*, *E*) − ***PD***(*H*, *E*\*) = [**P**(*E* & *H*)**/**[**P**(*E* & ~*H*)] − [**P**(*E*\* & *H*)**/P**(*E*\* & ~*H*)] |

[Back to Text]

### Example 3: An illustration of the difference between ***PR*** and ***OR***

The probability ratio and odds ratio yield different verdicts about the relative degree to which *E* incrementally confirms *H* and *H*\* when (a) *H* predicts *E* somewhat more strongly than *H*\* does, but (b) ~*H* predicts *E* *much* more strongly than ~*H*\* does. The general condition is this:

> | ***PR***(*H*, *E*) >***OR***(*H*, *E*) and ***OR***(*H*\*, *E*) < ***PR***(*H*\*, *E*) |
> | --- |
> | if and only if |
> | 1 < ***LR***(*H*, *H*\*; *E*) < ***LR***(~*H*, ~*H*\*; *E*) |

To illustrate, suppose that an exam that tests for knowledge of elementary mathematics is given to high-school students at the end of their sophomore year. Each student who takes the exam will have had a course in geometry (= *H*), a course in algebra (= *H*\*), courses in both subjects, or no math course at all. Reliable statistics from a large population show that students tend to pass the exam in the following proportions:

> |   | *H* & *H*\* | *H* & ~*H*\* | ~*H* & *H*\* | ~*H* & ~*H*\* |
> | --- | --- | --- | --- | --- |
> | *E* = PASS | 0.12 | 0.001 | 0.378 | 0.001 |
> | ~*E* = FAIL | 0.003 | 0.005 | 0.2 | 0.292 |

About 12% of students take both courses, and they pass 97.5% of the time. The minuscule proportion of students (0.6%) who take geometry but not algebra pass only one time in six. About 58% of students take algebra but not geometry, and they pass at a 65% rate. Finally, a bit less than 30% of students take neither class, and they pass less than 0.4% of the time. In general, algebra alone is a moderately strong indicator of passing, geometry alone does little to promote passing (but it is better than nothing), and adding geometry to algebra makes passing almost certain. Given these numbers, learning that a student has passed the exam will incrementally confirm both the hypothesis that she has taken algebra and the hypothesis that she has taken geometry. ***PR*** and ***OR*** disagree about which of the two hypotheses receives *more* incremental support.

- ***PR***(*H*, *E*) = 1.88 > ***PR***(*H*\*, *E*) = 1.42
- ***OR***(*H*, *E*) = 2.16 < ***OR***(*H*\*, *E*) = 106.2

A comparison of probability ratios tells us that *E* provides slightly more incremental evidence for *H* than for *H*\*, whereas a comparison of odds ratios indicates that *E* provides much more incremental evidence for *H*\* than for *H*. The probability ratio comparison reflects the fact that a course in geometry is a far better than one in algebra at indicating that a student has taken *both* courses. In contrast, the great, oppositely directed disparity in odds ratios is due to the fact that students have a decent chance of passing (44%) without geometry because they are likely to have had algebra, but they have almost no chance (0.7%) of passing without algebra because they will probably have had no math at all.

[Back to Text]

### Example 4: An illustration of the difference between ***PR*** and ***PD***

The probability ratio and probability difference disagree about the relative degree to which *E* incrementally confirms *H* and *H*\* when (a) *H* predicts *E* somewhat more strongly than *H*\* does, but (b) *H*\* is much more probable than *H*. Here is the general condition:

> | ***PR***(*H*, *E*) > ***PR***(*H*, *E*) and ***PD***(*H*, *E*) < ***PD***(*H*, *E*) |
> | --- |
> | if and only if |
> | 1 < (***PR***(*H*, *E*) − 1)**/**(***PR***(*H*\*, *E*) − 1) < **P**(*H*\*)**/P**( *H*) |

To illustrate, suppose that a patient shows up in an emergency room with a severe headache, muscle aches and fatigue. These symptoms are consistent with both Lyme disease (= *H*), which is rare in the area, and influenza (= *H*\*), which is more common. We are about to learn whether the patient has a fever (= *E*). The known statistics for people exhibiting the patient's symptoms are as follows:

> |   | *H* & *H*\* | *H* & ~*H*\* | ~*H* & *H*\* | ~*H* & ~*H*\* |
> | --- | --- | --- | --- | --- |
> | *E* = fever | 0.007 | 0.020 | 0.184 | 0.004 |
> | ~*E* = no fever | 0.001 | 0.002 | 0.080 | 0.702 |

While only 3% of people have Lyme disease, this illness is accompanied by fever 90% of the time. The much larger group of patients (about 27%) who have the flu are feverish only 70% of the time. Somewhat paradoxically, patients with both the flu and Lyme disease present with fevers slightly *less* often than patients with Lyme disease alone (perhaps because flu-induced fevers tend to show up more rapidly than those caused by Lyme disease). Given these statistics, learning that the patient has a fever incrementally confirms both the hypothesis that she has Lyme disease and the hypothesis that she has the flu. ***PR*** and ***PD***, disagree about which of the two hypotheses receives the greater increment of support.

- ***PR***(*H*, *E*) = 4.19 > ***PR***(*H*\*, *E*) = 3.27
- ***PD***(*H*, *E*) = 0.09 < ***PD***(*H*\*, *E*) = 0.61

According to the ratio measure, a fever provides more incremental evidence for Lyme disease than it does for the flu simply because fever accompanies the former more often than it accompanies the latter. According to the ratio measure, however, a fever incrementally confirms a diagnosis of influenza more than a diagnosis of Lyme disease. Since so many more patients suffer from the flu than from Lyme disease, and since both illnesses produce fevers at a high rate, *H*\*'s probability ends up being increased by a larger absolute amount than *H*'s probability is increased. In general, when two hypotheses have similar predictive power with respect to some item of evidence, the probability difference measure has a larger increment of confirmation accruing to the hypothesis that is antecedently more probable.

[Back to Text]

### Example 5: An illustration of the difference between ***OR*** and ***PD***

The odds ratio and probability difference yield disparate verdicts about the relative degree to which *E* incrementally confirms *H* and *H*\* under the following conditions:

> | ***PD***(*H*, *E*) >***PD***(*H*, *E*) and ***OR***(*H*, *E*) < ***OR***(*H*, *E*) |
> | --- |
> | if and only if |
> | [**P**(~*H* & *E*)**P**(*H*)]**/**[**P**(~ *H*\* & *E*)**P**(*H*\*)] >[**P**(*H* & *E*) − **P**(*H*)**P**(*E*)]**/**[ **P**(*H*\* & *E*) − **P**(*H*\*)**P**(*E*)] >1 |

To get a sense of what this involves, imagine a corporation in which employees may or may not be highly paid (= *H*), and may or may not hold cushy jobs (= *H*\*). The distribution of jobs among men (= *E*) and women on the payroll is as follows:

> |   | *H* & *H*\* | *H* & ~*H*\* | ~*H* & *H*\* | ~*H* & ~*H*\* |
> | --- | --- | --- | --- | --- |
> | *E = man* | 0.018 | 0.102 | 0.019 | 0.162 |
> | ~*E* = woman | 0.002 | 0.098 | 0.001 | 0.598 |

In this sexist firm, only 2% of employees have well-paid cushy jobs, and 90% of them are men. Well-paid but difficult jobs held by 20% of the staff, and these are almost evenly split among men (51%) and women (49%). Another 2% of employees have low-wage cushy jobs, and 95% of these are men. Most workers (76%) are poorly paid and have difficult jobs. These assignments go overwhelmingly (79%) to women. Given these statistics, learning that an employee is a man will incrementally confirm both the hypothesis that he is well-paid and the hypothesis that he has a cushy job. ***PD*** and ***OR*** disagree about which of the two hypotheses receives the greater increment of support from the evidence.

- ***PD***(*H*, *E*) = 0.18 > ***PD***(*H*\*, *E*) = 0.08
- ***OR***(*H*, *E*) = 2.36 < ***OR***(*H*\*, *E*) = 3.37

The probability difference measure has *H* garnering a (slightly) greater increment of confirmation than *H*\*. This is largely because (i) the number of men in well-paid, difficult jobs is so much greater than the number men in of low-wage, cushy jobs, and (ii) the number of men in low-wage, difficult jobs is large relative to the total number of men. The odds ratio measure has *H*\* receiving a (slightly) greater increment of confirmation than *H* because (i\*) low-wage jobs or difficult jobs are about equally good as counter indicators of *E*, but (ii) cushy jobs are much better than well-paid jobs as positive indicators of *E*.

[Back to Text]

### Table 5A: Measures of incremental evidence for fixed *E* and variable *H*

**Four measures of incremental change in NET evidence**

|   | **Ratio** | **Difference** |
| --- | --- | --- |
| **P** as total | ***PR***(*H*, *E*)**/*PR***(~*H*, *E*) = ***LR***(*H*, *E*) | ***PD***(*H*, *E*) − ***PD***(~*H*, *E*) = 2***PD***(*H*, *E*) |
| **O** as total | ***OR***(*H*, *E*)**/*OR***(~*H*, *E*) = ***LR***(*H*, *E*)² | ***OD***(*H*, *E*) − ***OD***(~*H*, *E*) = [**P**(*H*) − **P**(~*H*)]**/**[**P**( *H*)**P**(~*H*)**O**(*E*)] |

**Four measures of incremental change in the BALANCE of TOTAL evidence**

|   | **Ratio** | **Difference** |
| --- | --- | --- |
| **P** as total | ***PR***(*H*, *E*)**/*PR***(*H*\*, *E*) = ***LR***(*H*, *H*\*; *E*) | ***PD***(*H*, *E*) − ***PD***(*H*\*, *E*) = [**P**_{*E*}(*H*) − **P**_{*E*}(*H*\*)] − [**P**(*H*) − **P**(*H*\*)] |
| **O** as total | ***OR***(*H*, *E*)**/*OR***(*H*\*, *E*) = ***LR***(*H*, *H*\*; *E*)**/*LR***(~*H*, ~*H*\*; *E*) | ***OD***(*H*, *E*) − ***OD***(~*H*, *E*) = [**P**(*H*) − **P**(*H*\*)]**/**[**P**(~ *H*)**P**(~*H*\*)**O**(*E*)] |

[Back to Text]

### Proof Sketch: 3.5 Lemma

| **(3.5) Lemma**: | If *H* and *H*\* both entail *E* and if **P**(*H*) >**P**(*H*\*), then ***LR***(*H*, *H*\*; *E*) = 1 and ***LR***(~*H*, ~*H*\*; ~*E*) >1. |
| --- | --- |

**Sketch of Proof**: If *H* and *H*\* both entail *E*, then

1. **P**_{*H*}(*E*) = **P**_{*H*\*}(*E*) = 1
2. **P**_{~*H*}(~*E*) = **P**(~*E*)**/P**(~ *H*)
3. **P**_{~*H*\*}(~*E*) = **P**(~*E*)**/P**(~ *H*\*)

(a) entails that ***LR***(*H*, *H*\*; *E*) = 1. (b) and (c) entail that ***LR***(~*H*, ~*H*\*; ~*E*) >1 if and only if **P**(~*H*\*)**/P**(~ *H*) >1, which will always be so when **P**(*H*) >**P**(*H*\*).

[Back to Text]

### Proof Sketch: 3.6 Lemma

| **(3.6) Lemma**: | Simple conditioning on *E* is the only rule for revising subjective probabilities that yields a posterior **Q** with the following properties for *any* prior such that **P**(*E*) >0: |
| --- | --- |
|   | **Q**(*E*) = 1. *Ordinal Similarity*. If *H* and *H*\* entail *E*, then **P**(*H*) ≥ **P**(*H*\*) if and only if **Q**(*H*) ≥ **Q**(*H*\*). |

**Sketch of proof**: Conditioning on *E* obviously satisfies (i)-(ii) for any **P**. To see why it is the *only* revision rule that has these properties for *all* probabilities, notice that **P** might be *atomless* in the sense that any hypothesis to which it assigns a positive probability can be subdivided into disjoint hypotheses that also have positive probability. For an atomless **P** with **P**(*E*) >0, **P**_{*E*} will also be atomless. Since **Q** is defined over the same set of propositions as **P**, clauses (i)-(ii) ensure that **Q** is atomless and ordinally similar to **P**_{*E*}. It turns out that atomless probability functions defined over the same set of propositions can only be ordinally similar if they are identical (Joyce 1999, 134-135). Thus, **Q** = **P**_{*E*}, which means that (i)-(ii) can only hold in full generality if the revision rule in question is conditioning.

[Back to Text]
