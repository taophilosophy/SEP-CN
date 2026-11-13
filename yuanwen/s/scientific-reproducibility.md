# Reproducibility of Scientific Results
**First published Mon Dec 3, 2018**

*Fidler, Fiona, Wilcox, John*

The terms “reproducibility crisis” and “replication crisis” gained currency in conversation and in print over the last decade (e.g., Pashler & Wagenmakers 2012)[^pashler-2012][^wagenmakers-2012], as disappointing results emerged from large scale reproducibility projects in various medical, life and behavioural sciences (e.g., Open Science Collaboration, OSC 2015)[^open-2015]. In 2016, a poll conducted by the journal *Nature* reported that more than half (52%) of scientists surveyed believed science was facing a “replication crisis” (Baker 2016)[^baker-2016]. More recently, some authors have moved to more positive terms for describing this episode in science; for example, Vazire (2018) refers instead to a “credibility revolution” highlighting the improved methods and open science practices it has motivated.

The crisis often refers collectively to at least the following things:

1. the virtual absence of replication studies in the published literature in many scientific fields (e.g., Makel, Plucker, & Hegarty 2012)[^makel-2012],
2. widespread failure to reproduce results of published studies in large systematic replication projects (e.g., OSC 2015; Begley & Ellis 2012)[^begley-2012],
3. evidence of publication bias (Fanelli 2010a)[^fanelli-2010a],
4. a high prevalence of “questionable research practices”, which inflate the rate of false positives in the literature (Simmons, Nelson, & Simonsohn 2011; John, Loewenstein, & Prelec 2012; Agnoli et al. 2017; Fraser et al. 2018)[^agnoli-2017][^fraser-2018][^john-2012][^simmons-2011], and
5. the documented lack of transparency and completeness in the reporting of methods, data and analysis in scientific publication (Bakker & Wicherts 2011; Nuijten et al. 2016)[^bakker-2011][^nuijten-2016].

The associated open science reform movement aims to rectify conditions that led to the crisis. This is done by promoting activities such as data sharing and public pre-registration of studies, and by advocating stricter editorial policies around statistical reporting including publishing replication studies and statistically non-significant results.

This review consists of four distinct parts. First, we look at the term “reproducibility” and related terms like “repeatability” and “replication”, presenting some definitions and conceptual discussion about the epistemic function of different types of replication studies. Second, we describe the meta-science research that has established and characterised the reproducibility crisis, including large scale replication projects and surveys of questionable research practices in various scientific communities. Third, we look at attempts to address epistemological questions about the limitations of replication, and what value it holds for scientific inquiry and the accumulation of knowledge. The fourth and final part describes some of the many initiatives the open science reform movement has proposed (and in many cases implemented) to improve reproducibility in science. In addition, we reflect there on the values and norms which those reforms embody, noting their relevance to the debate about the role of values in the philosophy of science.

## 1. Replicating, Repeating, and Reproducing Scientific Results

A starting point in any philosophical exploration of reproducibility and related notions is to consider the conceptual question of what such notions mean. According to some (e.g., Cartwright 1991)[^cartwright-1991], the terms “replication”, “reproduction” and “repetition” denote distinct concepts, while others use these terms interchangeably (e.g., Atmanspacher & Maasen 2016a)[^atmanspacher-2016a]. Different disciplines can have different understandings of these terms too. In computational disciplines, for example, *reproducibility* often refers to the ability to reproduce computations alone, that is, it relates exclusively to sharing and sufficiently annotating data and code (e.g., Peng 2011, 2015)[^peng-2011][^peng-2015]. In those disciplines, *replication* describes the redoing of whole experiments (Barba 2017, Other Internet Resources). In psychology and other social and life sciences, however, *reproducibility* may refer to either the redoing of computations, or the redoing of experiments. The Reproducibility Projects, coordinated by the Center for Open Science, redo entire studies, data collection and analysis. A recent funding program announcement by DARPA (US Defense Advanced Research Programs Agency) distinguished between reproducibility and replicability, where the former refers to computational reproducibility and the latter to the redoing of experiments. Here we use all three terms—“replication”, “reproduction” and “repetition”—interchangeably, unless explicitly describing the distinctions of other authors.

When describing a study as “replicable”, people could have in mind either of at least two different things. The first is that the study is replicable *in principle* the sense that it can be carried out again, particularly when its methods, procedures and analysis are described in a sufficiently detailed and transparent way. The second is that the study is replicable in that sense that it can be carried out again and, when this happens, the replication study will *successfully* produce *the same or sufficiently similar results* as the original. A study may be replicable in the former sense but not in the second sense: one might be able to replicate the methods, procedures and analysis of a study, but fail to successfully replicate the results of the original study. Similarly, when people talk of a “replication”, they could also have in mind two different things: the replication of the methods, procedures and analysis of a study (irrespective of the results) or, alternatively, the replication of such methods, procedures and analysis *as well as* the results.

Arguably, most typologies of replication make more or less fine-grained distinctions between *direct replication* (which closely follow the original study to verify results) and *conceptual replications* (which deliberately alter important features of the study to generalize findings or to test the underlying hypothesis in a new way). As suggested, this distinction may not always be known by these terms. For example, roughly the same distinction is referred to as *exact* and *inexact replication* by Keppel (1982); *concrete* and *conceptual replication* by Sargent (1981), and *literal, operational and constructive replication* by Lykken (1968). Computational reproducibility is most often direct (reproducing particular analysis outcomes from the same data set using the same code and software), but it can also be conceptual (analysing the same raw data set with alternative approaches, different models or statistical frameworks). For an example of a conceptual computational reproducibility study, see Silberzahn and Uhlmann 2015.

We do not attempt to resolve these disciplinary differences or to create a new typology of replication, and instead we will provide a limited snapshot of the conceptual terrain by surveying three existing typologies—from Stefan Schmidt (2009), from Omar Gómez, Natalia Juristo, and Sira Vegas (2010) and from Hans Radder. Schmidt’s account has been influential and widely-cited in psychology and social sciences, where the replication crisis literature is heavily concentrated. Gómez, Juristo, and Vegas’s (2010) typology of replication is based on a multidisciplinary survey of over 18 scholarly classifications of replication studies which collectively contain more than 79 types of replication. Finally, Radder’s (1996, 2003, 2006, 2009, 2012) typology is perhaps best known within philosophy of science itself.

### 1.1 An Account from the Social Sciences

Schmidt outlines five functions of replication studies in the social sciences:

- *Function 1.* Controlling for sampling error—that is, to verify that previous results in a sample were not obtained purely by chance outcomes which paint a distorted picture of reality
- *Function 2.* Controlling for artifacts (internal validity)—that is, ensuring that experimental results are a proper test of the hypothesis (i.e., have internal validity) and do not reflect unintended flaws in the study design (such as when a measurement result is, say, an artifact of a faulty thermometer rather than an actual change in a substance’s temperature)
- *Function 3.* Controlling for fraud,
- *Function 4.* Enabling generalizability,
- *Function 5.* Enabling verification of the underlying hypothesis.

Modifying Hendrik’s (1991) classes of variables that define a research space, Schmidt (2009) presents four classes of variables which may be altered or held constant in order for a given replication study to fulfil one of the above functions. The four classes are:

- *Class 1.* Information conveyed to participants (for example, their task instructions).
- *Class 2.* Context and background. This is a large class of variables, and it includes: participant characteristics (e.g., age, gender, specific history); the physical setting of the research; characteristics of the experimenter; incidental characteristics of materials (e.g., type of font, colour of the room),
- *Class 3.* Participant recruitment, including selection of participants and allocation to conditions (such as experimental or control conditions),
- *Class 4.* Dependent variable measures (or in Schmidt’s terms “procedures for the constitution of the dependent variable”, 2009: 93)

Schmidt then systematically works through examples of how each function can be achieved by altering and/or holding a different class or classes of variable constant. For example, to fulfil the function of controlling for sampling error (Function 1), one should alter only variables regarding participant recruitment (Class 3), attempting to keep variables in all other classes as close to the original study as possible. To control for artefacts (Function 2), one should alter variables concerning the context and dependent variable measures (variables in Classes 2 and 4 respectively), but keep variables in 1 and 3 (information conveyed to participants and participant recruitment) as close to the original as possible. Schmidt, like most other authors in this area, acknowledges the practical limits of being able to hold all else constant. Controlling for fraud (Function 3) is served by the same arrangements as controlling for artefacts (Function 2). In Schmidt’s account, controlling for sampling error, artefacts and fraud (Functions 1 to 3) are connected by a theme of confirming the results of the original study. Functions 4 and 5 go beyond this—generalizing to new populations (Function 4) which is served by changes to participant recruitment (Class 3) and confirming the underlying hypothesis (Function 5), which served by changes to the information conveyed, the context and dependant variable measures (Classes 1, 2 and 4 respectively) but not changes to participant recruitment (Class 3, although Schmidt acknowledges that holding the latter class of variables constant whilst varying everything else is often practically impossible). Attempts to enable verification of the underlying research hypothesis (i.e., to fulfil Function 5) alone are what Schmidt classifies as *conceptual* replications, following Rosenthal (1991). Attempts to fulfil the other four functions are considered variants of *direct* replications.

In summary, for Schmidt, direct replications control for sampling error, artifacts, and fraud, and provide information about the reliability and validity of prior empirical work. Conceptual replications help corroborate the underlying theory or substantive (as opposed to statistical) hypothesis in question and the extent to which they generalize in new circumstances and situations. In practice, direct and conceptual replications lie on a continuum, with replication studies varying more or less compared to the original on potentially a great number of dimensions.

### 1.2 An Interdisciplinary Account

Gómez, Juristo, and Vega’s (2010) survey of the literature in 18 disciplines identified 79 types of replication, not all of which they considered entirely distinct. They identify five main ways in which a replication study may diverge from an initial study. With some similarities to Schimdt’s four classes above:

1. The *site* or spatial location of the replication experiment: replication experiments may be conducted in a location that is or is not the same as the site of the initial study.
2. The *experimenters* conducting a replication may be exclusively the same as the original, exclusively different, or a combination of new and original experimenters
3. The *apparatus*, including the design, materials, instruments and other important experimental objects and/or procedures may vary between original and replication studies.
4. The *operationalisations* employed may differ, where operationalisation refers to measurement of variables. For example, in psychology this might include using two different scales measuring for depression (as a dependent variable).
5. Finally, studies may vary on *population properties*.

A change in any one or combination of these elements in a replication study corresponds to different purposes underlying the study, and thereby establishes a different kind of validity. Like Schmidt et al. then systematically work through how changes to each of the above work to fulfil different epistemic functions.

- Function 1. *Conclusion Validity and Controlling for Sampling Error*: If each of the five elements above are unchanged in a replication study, then the purpose of the replication is to control for *sampling error*, that is, to verify that previous results in a sample were not obtained purely by chance outcomes which make the sample misleading or unrepresentative. This provides a safeguard against what is known as a *type I error*: incorrectly failing to reject the *null* hypothesis (that is, the hypothesis that there is no relationship between two phenomena under investigation). These studies establish *conclusion validity*, that is, the credibility or believability of an observed relationship or phenomenon.
- Function 2. *Internal Validity and Controlling for Artefactual Results*: If a replication study differs with respect to the site, experimenters or apparatus, then its purpose is to establish that previously observed results are not an artefact of a particular apparatus, lab or so on. These studies establish *internal validity*, that is, the extent to which results can be attributed to the experimental manipulation itself rather than to extraneous variables.
- Function 3. *Construct Validity and Determining Limits for Operationalizations*: If a replication study differs with respect to operationalisations, then its purpose is to determine the extent to which the effect generalizes across measures of manipulated or dependent variables (e.g., the extent to which the effect does not depend on the particular psychometric test one uses to evaluate depression or IQ). Such studies fulfil the function of establishing *construct validity* in that they provide evidence that the effect holds across different ways of measuring the constructs.
- Function 4. *External Validity and Determining Limits in the Population Properties*: If a replication study differs with respect to its population properties, then its purpose is to ascertain the extent to which the results are generalizable to different populations, populations which, in Gómez, Juristo, and Vegas’s view, concern subjects and experimental objects such as programs. Such studies reinforce *external validity*—the extent to which the results are generalizable to different populations.

### 1.3 A Philosophical Account

Radder (1996, 2003, 2006, 2009, 2012) distinguishes three types of reproducibility. One is the reproducibility of what Radder calls an experiment’s *material realization*. Using one of Radder’s own examples as an illustration, two people may carry out the same actions to measure the mass of an object. Despite doing the same actions, person *A* regards themselves as measuring the object’s Newtonian mass while person *B* regards themselves as measuring the object’s Einsteinian mass. Here, then, the actions or material realization of the experimental procedure can be reproduced, but the theoretical descriptions of their significance differ. Radder, however, does not specify what is required for one material realisation to be a reproduction of another, a pertinent question, especially since, as Radder himself affirms, no reproduction will be exactly the same as any other reproduction (1996: 82–83).

A second type of reproducibility is the reproducibility of an experiment, given a *fixed theoretical description*. For example, a social scientist might conduct two experiments to examine social conformity. In one experiment, a young child might be instructed to give an answer to a question before a group of other children who are, unknown to the former child, instructed to give wrong answers to the same question. In another experiment, an adult might be instructed to give an answer to a question before a group of other adults who are, unknown to the former adult, instructed to give wrong answers to the same question. If the child and the adult give a wrong answer that conforms to the answers of others, then the social scientist might interpret the result as exemplifying social conformity. For Radder, the theoretical description of the experiment might be fixed, specifying that if some people in a participant’s surroundings give intentionally false answers to the question, then the genuine participant will conform to the behaviour of their peers. However, the material realization of these experiments differs insofar as one concerns children and the other adults. It is difficult to see how, in this example at least, this differs from what either Schmidt or Gómez, Juristo, and Vegas would refer to as establishing generalizability to a different population (Schmidt’s [2009] Class 3 and Function 5; Gómez, Juristo, and Vegas’s [2010] way 5 and Function 4).

The third kind of reproducibility is what Radder calls *replicability*. This is where experimental procedures differ to produce the same experimental result (otherwise known as a successful replication). For example, Radder notes that multiple experiments might obtain the result “a fluid of type *f* has a boiling point *b*”, despite having different kinds of thermometers by which to measure this boiling point (2006: 113–114).

Schmidt (2009) points out that the difference between Radder’s second and third types of reproducibility is small in comparison to their differences to the first type. He consequently suggests his alternative distinction between direct and conceptual replication, presumably intending a conceptual replication to cover Radder’s second and third types.

In summary, whilst Gómez, Juristo, and Vegas’s typology draws distinctions in slightly different places to Schmidt’s, its purpose is arguably the same—to explain what types of alterations in replication studies fulfil different scientific goals, such as establishing internal validity or the extent of generalization and so on. With the exception of his discussion of reproducing the material realization, Radder’s other two categories can perhaps be seen as fitting within the larger range of functions described by Schmidt and Gómez et al., who both acknowledge that in practice, direct and conceptual replications lie on a noisy continuum.

## 2. Meta-Science: Establishing, Monitoring, and Evaluating the Reproducibility Crisis

In psychology, the origin of the reproducibility crisis is often linked to Daryl Bem’s (2011) paper which reported empirical evidence for the existence of “psi”, otherwise known as Extra Sensory Perception (ESP). This paper passed through the standard peer review process and was published in the high impact *Journal of Personality and Social Psychology.* The controversial nature of the findings inspired three independent replication studies, each of which failed to reproduce Bem’s results. However, these replication studies were rejected from four different journals, including the journal that had originally published Bem’s study, on the grounds that the replications were not original or novel research. They were eventually published in *PLoS ONE* (Ritchie, Wiseman, & French 2012)[^ritchie-2012]. This created controversy in the field, and was interpreted by many as demonstrating how publication bias impeded science’s self-correction mechanism. In medicine, the origin of the crisis is often attributed to Ioannidis’ (2005) paper “Why most published findings are false”. The paper offered formal arguments about inflated rates of false positives in the literature—where a “false positive” result claims a relationship exists between phenomena when it in fact does not (e.g., a claim that consuming a drug is correlated with symptom relief when it in fact is not). Ioannidis’ (2005) also reported very low (11%) empirical reproducibility rates from a set of pre-clinical trial replications at Amgen, later independently published by Begley and Ellis (2012). In all disciplines, the replication crisis is also more generally linked to earlier criticisms of Null Hypothesis Significance Testing (e.g., Szucs & Ioannidis 2017)[^szucs-2017], which pointed out the neglect of statistical power (e.g., Cohen 1962, 1994)[^cohen-1962][^cohen-1994] and a failure to adequately distinguish statistical and substantive hypotheses (e.g., Meehl 1967, 1978)[^meehl-1967][^meehl-1978]. This is discussed further below.

In response to the events above, a new field identifying as *meta-science* (or *meta-research*) has become established over the last decade (Munafò et al. 2017)[^munafò-2017]. Munafò et al. define meta-science as “the scientific study of science itself” (2017: 1). In October 2015, Ioannidis, Fanelli, Dunne, and Goodman identified over 800 meta-science papers published in the five-month period from January to May that year, and estimated that the relevant literature was accruing at the rate of approximately 2,000 papers each year. Referring to the same bodies of work with slightly different terms, Ioannidis et al. define “meta-research” as

> an evolving scientific discipline that aims to evaluate and improve research practices. It includes thematic areas of methods, reporting, reproducibility, evaluation, and incentives (how to do, report, verify, correct, and reward science). (2015: 1)

Multiple research centres dedicated to this work now exist, including, for example, the Tilburg University Meta-Research Center in psychology, the Meta-Research Innovation Center at Stanford (METRICS), and others listed in Ioannidis et al. 2015 (see Other Internet Resources). Relevant research in medical fields is also covered in Stegenga 2018.

Projects that self-identify as meta-science or meta-research include:

- Large, crowd-sourced, direct (or close) replication projects such as The Reproducibility Projects in Psychology (OSC 2015) and Cancer Biology (Errington et al. 2014)[^errington-2014] and the Many Labs projects in psychology (e.g., Klein et al. 2014)[^klein-2014];
- Computational reproducibility projects, that is, redoing analysis using the same original data set (e.g., Chang & Li 2015)[^chang-2015];
- Bibliographic studies documenting the extent of publication bias in different scientific fields and changes over time (e.g., Fanelli 2010a, 2010b, 2012)[^fanelli-2010a][^fanelli-2010b][^fanelli-2012];
- Surveys of the use of Questionable Research Practices (QRPs) amongst researchers and their impact on the publication literature (e.g., John, Loewenstein, & Prelec 2012; Fiedler & Schwarz 2016; Agnoli et al. 2017; Fraser et al. 2018)[^agnoli-2017][^fiedler-2016][^fraser-2018][^john-2012];
- Surveys of the completeness, correctness and transparency of methods and analysis reporting in scientific journals (e.g., Nuijten et al. 2016; Bakker & Wicherts 2011; Cumming et al. 2007; Fidler et al. 2006)[^bakker-2011][^cumming-2007][^fidler-2006][^nuijten-2016];
- Survey and interview studies of researchers’ understanding of core methodological and statistical concepts, and real and perceived obstacles to improving practices (Bakker et al. 2016; Washburn et al. 2018; Allen, Dorozenko, & Roberts 2016)[^allen-2016][^bakker-2016][^washburn-2018];
- Evaluation of incentives to change behaviour, thereby improving reproducibility and encouraging more open practices (e.g., Kidwell et al. 2016)[^kidwell-2016].

### 2.1 Reproducibility Projects

The most well known of these projects is undoubtedly the Reproducibility Project: Psychology, coordinated by the now Center for Open Science in Charlottesville, VA (then the Open Science Collaboration). It involved 270 crowd sourced researchers in 64 different institutions in 11 different countries. Researchers attempted direct replications of 100 studies published in three leading psychology journals in the year 2008. Each study was replicated only once. Replications attempted to follow original protocols as closely as possible, though some differences were unavoidable (e.g., some replication studies were done with European samples when the original studies used US samples). In almost all cases, replication studies used larger sample sizes that the original studies and therefore had greater statistical power—that is, a greater probability of correctly rejecting the null hypothesis (i.e., that no relationship exists) when the hypothesis is false. A number of measures of reproducibility were reported:

1. The proportion of studies in which there was a match in the statistical significance between original and replication. (Here, the statistical significance of a result is the probability that it would occur given the null hypothesis, and *p* values are common measures of such probabilities. A replication study and an original study would have a match in statistical significance if, for example, they both specified that the probability of the original and replication results occurring given the null hypothesis is less than 5%—i.e., if the *p* values for results in both studies are below 0.05.) Thirty nine percent (36%) of results were successful reproduced according to this measure.
2. The proportion of studies in which the Effect Size (ES) of the replication study fell within the 95% Confidence Interval (CI) of the original. (Here, an ES represents the strength of a relationship between phenomena—a toy example of which is how strongly consumption of a drug is correlated with symptom relief—and a Confidence Interval provides some indication of the probability that the ES of the replication study is close to the ES of the original study.) Forty seven percent (47%) of results were successfully reproduced according to this measure.
3. The correlation between original ES and replication ES. Replication study ESs were roughly half the size of original ESs.
4. The proportion of studies for which subjective ratings by independent researchers indicated a match between the replication and the original. Thirty nine percent (39%) were considered successful reproductions according to this measure. The closeness of this figure to measure 1 suggests that raters relied very heavily on *p* values in making their judgements.

There have been objections to the implementation and interpretation of this project, most notably by Gilbert et al. (2016), who took issue with the extent to which the replications studies were indeed direct replications. For example, Gilbert et al. highlighted 6 specific examples of “low fidelity protocols”, that is, where replication studies differed in their view substantially from the original (in one case, using a European sample rather than a US sample of participants). However, Anderson et al. (2016) explained in a reply that in half of those cases, the authors of the original study had endorsed the replication as being direct or close to on relevant dimensions and that furthermore, that independently rated similarity between original and replication studies failed to predict replication success. Others (e.g., Etz & Vandekerckhove 2016)[^etz-2016] have applied Bayesian reanalysis to the OSC’s (2015) data and conclude that up to 75% (as opposed to the OSC’s 36–47%) of replications could be considered successful. However, they do note that in many cases this is only with very weak evidence (i.e., Bayes factors of <10). They too conclude that the failure to reproduce many effects is indeed explained by the overestimation of effect sizes, itself a product of publication bias. A Reproducibility Project: Cancer Biology (also coordinated by the Center for Open Science) is currently underway (Errington et al. 2014)[^errington-2014], originally attempting to replicate 50 of the highest impact studies in Cancer Biology published between 2010–2012. This project has recently announced it will complete with only 18 replication studies, as too few originals reported enough information to proceed with full replications (Kaiser 2018)[^kaiser-2018]. Results of the first 10 studies are reportedly mixed, with only 5 being considered “mostly repeatable” (Kaiser 2018)[^kaiser-2018].

The Many Labs project (Klein et al. 2014)[^klein-2014] coordinated 36 independent replications of 13 classic psychology phenomena (from 12 studies, that is, one study tested two effects), including anchoring, sunk cost bias and priming, amongst other well-known effects in psychology. In terms of matching statistical significance, the project demonstrated that 11 out of 13 effects could be successful replicated. It also showed great variation in many of the effect sizes across the 36 replications.

In biomedical research, there have also been a number of large scale reproducibility projects. An early one by Begley and Ellis (2012, but discussed earlier in Ioannidis 2005)[^ioannidis-2005] attempted to replicate 56 landmark pre-clinical trials and reported an alarming reproducibility rate of only 11%, that is, only 6 of the 56 results could be successfully reproduced. Subsequent attempts at large scale replications in this field have produced more optimistic estimates, but routinely failed to successfully reproduce more than half of the published results. Freedman et al. (2015) report five replication projects by independent groups of researchers which produce reproducibility estimates ranging from 22% to 49%. They estimate the cost of irreproducible research in US biomedical science alone to be in the order of USD$28 billion per year. A reproducibility project in Experimental Philosophy is an exception to the general trend, reporting reproducibility rates of 70% (Cova et al. forthcoming).

Finally, the Social Science Replication Project (SSRP) redid 21 experimental social science studies published in the journals *Nature* and *Science* between 2010 and 2015. Depending on the measure taken, the replication success rate was 57–67% (Camerer et al. 2018)[^camerer-2018].

### 2.2 Publication Bias, Low Statistical Power and Inflated False Positive Rates

The causes of irreproducible results are largely the same across disciplines we have mentioned. This is not surprising given that they stem from problems with statistical methods, publishing practices and the incentive structures created in a “publish or perish” research culture, all of which are largely shared, at least in the life and behavioral sciences.

Whilst replication is often casually referred to as a cornerstone of the scientific method, direct replication studies (as they might be understood from Schmidt or Gómez, Juristo, and Vegas’s typologies above) are a rare event in the published literature of some scientific disciplines, most notably the life and social sciences. For example, such replication attempts constitute roughly 1% of the published psychology literature (Makel, Plucker, & Hegarty 2012)[^makel-2012].

This virtual absence of replication studies in the literature can explained by the fact that many scientific journals have historically had explicit policies against publishing replication studies (Mahoney 1985)[^mahoney-1985]—thus giving rise to a “publication bias”. Over 70% of editors from 79 social science journals said they preferred new studies over replications and over 90% said they would did not encourage the submission of replication studies (Neuliep & Crandall 1990)[^neuliep-1990]. In addition, many science funding bodies also fund only “novel”, “original” and/or “groundbreaking” research (Schmidt 2009)[^schmidt-2009].

A second type of publication bias has also played a substantial role in the reproducibility crisis, namely a bias towards “statistically significant” or “positive” results. Unlike the bias against replication studies, this is rarely an explicitly stated policy of a journal. Publication bias towards statistically significant findings has a long history, and was first documented in psychology by Sterling (1959). Developments in text mining techniques have led to more comprehensive estimates. For example, Fanelli’s work has demonstrated the extent of publication bias in various disciplines, and the proportions of statistically significant results given below are from his 2010a paper. He has also documented the increase of this bias over time (2012) and explored the causes of the bias, including the relationship between publication bias and a publish or perish research culture (2010b).

In many disciplines (e.g., psychology, psychiatry, materials science, pharmacology and toxicology, clinical medicine, biology and biochemistry, economics and business, microbiology and genetics) the proportion of statistically significant results is very high, close to or exceeding 90% (Fanelli 2010a)[^fanelli-2010a]. This is despite the fact that in many of these fields, the average statistical power is low—that is, the average probability that a study will correctly reject the null hypothesis is low. For example, in psychology the proportion of published results that are statistically significant is 92% despite the fact that the average power of studies in this field to detect medium effect sizes (arguably typical of the discipline) is roughly 44% (Szucs & Ioannidis 2017)[^szucs-2017]. If there was no bias towards publishing statistically significant results, the proportion of significant results should roughly match the average statistical power of the discipline. The excess in statistical significance (in this case, the difference between 92% and 44%) is therefore an indicator the strength of the bias. For a second example, in ecology, environment and plant and animal sciences the proportion of statistically significant results is 74% and 78% respectively, admittedly lower than in psychology. However, the most recent estimate of the statistical power, again of medium effect sizes, of ecology and animal behaviour is 23–26% (Smith, Hardy, & Gammell 2011)[^smith-2011] (An earlier more optimistic assessment was 40–47%, Jennions & Møller, 2003.)[^jennions-2003] For a third example, the proportion of statistically significant results in neuroscience and behaviour is 85%. Our best estimate of the statistical power in neuroscience is at best 31%, with a lower bound estimate of 8% (Button et al. 2013)[^button-2013]. The associated *file-drawer problem* (Rosenthal 1979)[^rosenthal-1979]—where researchers relegate failed statistically non-significant studies to their file drawers, hidden from public view—has long been established in psychology and others disciplines, and is known to lead to distortions in meta-analysis (where a “meta-analysis” is a study which analyses results across multiple other studies).

### 2.3 Questionable Research Practices

In addition to creating the file-drawer problem described above, publication bias has been held at least partially responsible for the high prevalence of Questionable Research Practices (QRPs) uncovered in both self-report survey research (John, Loewenstein, & Prelec 2012; Agnoli 2017 et al. 2017; Fraser et al. 2018)[^agnoli-2017][^fraser-2018][^john-2012] and in journal studies that have detected, for example, unusual distributions of *p* values (Masicampo & Lalande 2012; Hartgerink et al. 2016)[^hartgerink-2016][^masicampo-2012]. Pressure to publish, now ubiquitous across academic institutions, means that researchers often cannot afford to simply assign “failed” or statistically non-significant studies to the file drawer, so instead they *p* hack and cherry-pick results (as discussed below) back to significance, and back into the published literature. Simmons, Nelson, and Simonsohn (2011) explained and demonstrated with simulated results how engaging in such practices inflates the false positive error rate of the published literature, leading to a lower rate of reproducible results.

“*P* hacking” refers to a set of practices which include: checking the statistical significance of results before deciding whether to collect more data; stopping data collection early because results have reached statistical significance; deciding whether to exclude data points (e.g., outliers) only after checking the impact on statistical significance and not reporting the impact of the data exclusion; adjusting statistical models, for instance by including or excluding covariates based on the resulting strength of the main effect of interest; and rounding of a *p* value to meet a statistical significance threshold (e.g., presenting 0.053 as *P* < .05). “Cherry picking” includes failing to report dependent or response variables or relationships that did not reach statistical significance or other threshold and/or failing to report conditions or treatments that did not reach statistical significance or other threshold. “HARKing” (Hypothesising After Results are Known) includes presenting ad hoc and/or unexpected findings as though they had been predicted all along (Kerr 1998)[^kerr-1998]; and presenting exploratory work as though it was confirmatory hypothesis testing (Wagenmakers et al. 2012)[^wagenmakers-2012]. Five of the most widespread QRPs are listed below in Table 1 (from Fraser et al. 2018)[^fraser-2018], with associated survey measures of prevalence.

*Table 1:*

Table 1: The prevalence of some common Questionable Research Practices. Percentage (with 95% confidence intervals) of researches who reported having used the QRP at least once (adapted from Fraser et al. 2018)[^fraser-2018]

| **Questionable Research Practice** | **Psychology Italy** (Agnoli et al. 2017)[^agnoli-2017] | **Psychology USA** (John, Loewenstein, & Prelec 2012)[^john-2012] | **Ecology** (Fraser et al. 2018)[^fraser-2018] | **Evolution** (Fraser et al. 2018)[^fraser-2018] |
| --- | --- | --- | --- | --- |
| Not reporting response (outcome) variables that failed to reach statistical significance^{#} | 47.9 *(41.3–54.6)* | 63.4 *(59.1–67.7)* | 64.1 *(59.1–68.9)* | 63.7 *(57.2–69.7)* |
| Collecting more data after inspecting whether the results are statistically significant^{*} | 53.2 *(46.6–59.7)* | 55.9 *(51.5–60.3)* | 36.9 *(32.4–42.0)* | 50.7 *(43.9–57.6)* |
| Rounding-off a *p* value or other quantity to meet a pre-specified threshold^{*} | 22.2 *(16.7–27.7)* | 22.0 *(18.4–25.7)* | 27.3 *(23.1–32.0)* | 17.5 *(13.1–23.0)* |
| Deciding to exclude data points after first checking the impact on statistical significance^{*} | 39.7 *(33.3–46.2)* | 38.2 *(33.9–42.6)* | 24.0 *(19.9–28.6)* | 23.9 *(18.5–30.2)* |
| Reporting an unexpected finding as having been predicted from the start^{^} | 37.4 *(31.0–43.9)* | 27.0 *(23.1–30.9)* | 48.5 *(43.6–53.6)* | 54.2 *(47.7–60.6)* |

^{#}cherry picking, ^{*}*p* hacking, ^{^}HARKing

### 2.4 Over-Reliance on Null Hypothesis Significance Testing

Null Hypothesis Significance Testing (NHST)—discussed above—is a commonly diagnosed cause of the current replication crisis (see Szucs & Ioannidis 2017)[^szucs-2017]. The ubiquitous nature of NHST in life and behavioural sciences is well documented, most recently by Cristea and Ioannidis (2018). This is important pre-condition for establishing its role as a cause, since it could not be a cause if its actual use was rare. The dichotomous nature of NHST facilitates publication bias (Meehl 1967, 1978)[^meehl-1967][^meehl-1978]. For example, the language of accept and reject in hypothesis testing maps conveniently on to acceptance and rejection of manuscripts, a fact that led Rosnow and Rosenthal (1989) to decry that “surely God loves the .06 nearly as much as the .05” (1989: 1277). Techniques that failed to enshrine a dichotomous threshold would be harder to employ in service of publication bias. For example, a case has been made that estimation using effect sizes and confidence intervals (introduced above) would be less prone to being used in service of publication bias (Cumming 2012, Cumming and Calin-Jageman 2017.

As already mentioned, the average statistical power in various disciplines is low. Not only is power often low, but it is virtually never reported; less than 10% of published studies in psychology report statistical power and even fewer in ecology do (Fidler et al. 2006)[^fidler-2006]. Explanations for the widespread neglect of statistical power often highlight the many common misconceptions and fallacies associated with *p* values (e.g., Haller & Krauss 2002; Gigerenzer 2018)[^gigerenzer-2018][^haller-2002]. For example, the inverse probability fallacy[^note-1] has been used to explain why so many researchers fail to calculate and report statistical power (Oakes 1986)[^oakes-1986].

In 2017, a group of 72 authors proposed in a *Nature Human Behaviour* paper that alpha level in statistical significance testing be lowered to 0.005 (as opposed to the current standard of 0.05) to improve the reproducibility rate of published research (Benjamin et al. 2018)[^benjamin-2018]. A reply from a different set of 88 authors was published in the same journal, arguing against this proposal and stating instead that researchers should justify their alpha level based on context (Lakens et al. 2018)[^lakens-2018]. Several other replies have followed, including a call from Andrew Gelman and colleagues to abandon statistical significance altogether (McShane et al. 2018, Other Internet Resources). The exchange has become known on social media as the *Alpha Wars* (e.g., in the Barely Significant blog, Other Internet Resources)). Independently, the American Statistical Association released a statement on the use of *p* values for the first time in its history, cautioning against their overinterpretation and pointing out the limits of the information they offer about replication (Wasserman & Lazar 2016) and devoted their association’s 2017 annual convention to the theme “Scientific Method for the 21ˢᵗ Century: A World Beyond $p <0.05$” (see Other Internet Resources).

### 2.5 Scientific Fraud

A number of recent high-profile cases of scientific fraud have contributed considerably to the amount of press around the reproducibility crisis in science. Often these cases (e.g., Diederik Stapel in psychology) are used as a hook for media coverage, even though the crisis itself has very little to do with scientific fraud. (Note also that the Questionable Research Practices above are not typically counted as “fraud” or even “scientific misconduct” despite their ethically dubious status.) For example, Fang, Grant Steen, and Casadevall (2012) estimated that 43% of retracted articles in biomedical research are withdrawn because of fraud. However, roughly half a million biomedical articles are published annually and only 400 of those are retracted (Oransky 2016, founder of the website RetractionWatch)[^oransky-2016], so this amounts to a very small proportion of the literature (approximately 0.1%). There are, of course, many cases of pharmaceutical companies exercising financial pressure on scientists and the publishing industry that raise speculation about how many undetected (or unretracted) cases there may still be in the literature. Having said that, there is widespread consensus amongst scientists in the field that the main cause of the current reproducibility crisis is the current incentive structure in science (publication bias, publish or perish, non-transparent statistical reporting, lack of rewards for data sharing). Whilst this incentive structure can push some to scientific fraud, it appears to be a very small proportion.

## 3. Epistemological Issues Related to Replication

Many scientists believe that replication is epistemically valuable in some way, that is to say, that replication serves a useful function in enhancing our knowledge, understanding or beliefs about reality. This section first discusses a problem about the epistemic value of replication studies—called the “experimenters regress”—and it then considers the claim that replication plays an epistemically valuable role in distinguishing scientific inquiry. It lastly examines a recent attempt to formalise the logic of replication in a Bayesian framework.

### 3.1 The Experimenters’ Regress

Collins (1985) articulated a widely discussed problem that is now known as the *experimenters’ regress*. He initially lays out the problem in the context of measurement (Collins 1985: 84)[^collins-1985]. Suppose a scientist is trying to determine the accuracy of a measurement device and also the accuracy of a measurement result. Perhaps, for example, a scientist is using a thermometer to measure the temperature of a liquid, and it delivers a particular measurement result, say, 12 degrees Celsius.

The problem arises because of the interdependence of the accuracy of the measurement result and the accuracy of the measurement device: to know whether a particular measurement result is accurate, we need to test it against a measurement result that is previously known to be accurate, but to know that the result is accurate, we need to know that it has been obtained via an accurate measuring device, and so on. This, according to Collins, creates a “circle” which he refers to as the “experimenters’ regress”.

Collins extends the problem to scientific replication more generally. Suppose that an experiment *B* is a replication study of an initial experiment *A*, and that *B*’s result apparently conflicts with *A*’s result. This seeming conflict may have one of two interpretations:

- The results of *A* and *B* deliver genuinely conflicting verdicts over the truth of the hypothesis under investigation
- Experiment *B* was not in fact a proper replication of experiment *A*.

The regress poses a problem about how to choose between these interpretations, a problem which threatens the epistemic value of replication studies if there are no rational grounds for choosing in a particular way. Determining whether one experiment is a proper replication of another is complicated by the facts that scientific writing conventions often omit precise details of experimental methodology (Collins 2016)[^collins-2016], and, furthermore, much of the knowledge that scientists require to execute experiments is tacit and “cannot be fully explicated or absolutely established” (Collins 1985: 73)[^collins-1985].

In the context of experimental methodology, Collins wrote:

> To know an experiment has been well conducted, one needs to know whether it gives rise to the correct outcome. But to know what the correct outcome is, one needs to do a well-conducted experiment. But to know whether the experiment has been well conducted…! (2016: 66; ellipses original)

Collins holds that in such cases where a conflict of results arises, scientists tend to fraction into two groups, each holding opposing interpretations of the results. According to Collins, where such groups are “determined” and the “controversy runs deep” (Collins 2016: 67)[^collins-2016], the dispute between the groups cannot be resolved via further experimentation, for each additional result is subject to the problem posed by the experimenters’ regress.[^note-2] In such cases, Collins claims that particular non-epistemic factors will partly determine which interpretation becomes the lasting view:

> the career, social, and cognitive interests of the scientists, their reputations and that of their institutions, and the perceived utility for future work. (Franklin & Collins 2016: 99)[^collins-2016][^franklin-2016]

Franklin was the most vociferous opponent of Collins, although recent collaboration between the two has fostered some agreement (Collins 2016)[^collins-2016]. Franklin presented a set of strategies for validating experimental results, all of which relate to “rational argument” on epistemic grounds (Franklin 1989: 459; 1994)[^franklin-1989]. Examples include, for instance, appealing to experimental checks on measurement devices or eliminating potential sources of error in the experiment (Franklin & Collins 2016)[^collins-2016][^franklin-2016]. He claimed that the fact that such strategies were evidenced in scientific practice “argues against those who believe that rational arguments plays little, if any, role” in such validation (Franklin 1989: 459)[^franklin-1989], with Collins being an example. He interprets Collins as suggesting that the strategies for resolving debates of the validation of results are social factors or “culturally accepted practices” (Franklin, 1989: 459)[^franklin-1989] which do not provide reasons to underpin rational belief about results. Franklin (1994) further claims that Collins conflates the difficulty in successfully *executing* experiments with the difficulty of *demonstrating* that experiments have been executed, with Feest (2016) interpreting him to say that although such execution requires tacit knowledge, one can nevertheless appeal to strategies to demonstrate the validity of experimental findings.

Feest (2016) examines a case study involving debates about the Mozart effect in psychology (which, roughly speaking, is the effect whereby listening to Mozart beneficially affects some aspect of intelligence or brain structure). Like Collins, she agrees that there is a problem in determining whether conflicting results suggest a putative replication experiment is not a proper replication attempt, in part because there is uncertainty about whether scientific concepts such as the Mozart effect have been appropriately operationalised in earlier or later experimental contexts. Unlike Collins (on her interpretation), however, she does not think that this uncertainty arises because scientists have inescapably tacit knowledge of the linguistic rules about the meaning and application of concepts like the Mozart effect. Rather the uncertainty arises because such concepts are still themselves developing and because of assumptions about the world that are required to successfully draw inferences from it. Experimental methodology then serves to reveal the previously tacit assumptions about the application of concepts and the legitimacy of inferences, assumptions which are then susceptible to scrutiny.

For example, in her study of the Mozart effect, she notes that replication studies of the Mozart effect failed to find that Mozart music had a beneficial influence on spatial abilities. Rauscher, who was the first to report results supporting the Mozart effect, suggested that the later studies were not proper replications of her study (Rauscher, Shaw, and Ky 1993, 1995)[^rauscher-1993][^rauscher-1995]. She clarified that the Mozart effect applied *only* to a *particular* category of spatial abilities (spatio-temporal processes) and that the later studies operationalised the Mozart effect in terms of different spatial abilities (spatial recognition). Here, then, there was a difficulty in determining whether to interpret failed replication results as evidence against the initial results or rather as an indication that the replication studies were not proper replications. Feest claims this difficulty arose because of tacit knowledge or assumptions: assumptions about the application of the Mozart effect concept to different kinds of spatial abilities, about whether the world is such that Mozart music has an effect on such abilities and about whether the failure of Mozart to impact other kinds of spatial abilities warrants the inference that the Mozart effect does not exist. Contra Collins, however, experimental methodology enabled the explication and testing of these assumptions, thus allowing scientists to overcome the interpretive impasse.

Against this background, her overall argument is that scientists often are and should be sceptical towards each other’s results. However, this is not because of inescapably tacit knowledge and the inevitable failure of epistemic strategies for validating results. Rather, it is at least in part because of varying tacit assumptions that researchers have about the meaning of concepts, about the world and about what to draw inferences from it. Progressive experimentation serves to reveal these tacit assumptions which can then be scrutinised, leading to the accumulation of knowledge.

There is also other philosophical literature on the experimenters’ regress, including Teira’s (2013) paper arguing that particular experimental debiasing procedures are defensible against the regress from a contractualist perspective, according to which self-interested scientists have reason to adopt good methodological standards.

### 3.2 Replication as a Distinguishing Feature of Science

There is a widespread belief that science is distinct from other knowledge accumulation endeavours, and some have suggested that replication distinguishes (or is at least essential to) science in this respect. (See also the entry on science and pseudo-science.). According to the Open Science Collaboration, “Reproducible research practices are at the heart of sound research and integral to the scientific method.” (OSC 2015: 7). Schmidt echoes this theme: “To confirm results or hypotheses by a repetition procedure is at the basis of any scientific conception” (2009: 90). Braude (1979) goes so far as to say that reproducibility is a “demarcation criterion between science and nonscience” (1979: 2). Similarly, Nosek, Spies, and Motyl state that:

> [T]he scientific method differentiates itself from other approaches by publicly disclosing the basis of evidence for a claim…. In principle, open sharing of methodology means that the entire body of scientific knowledge can be reproduced by anyone. (2012: 618)

If replication played such an essential or distinguishing role in science, we might expect it to be a prominent theme in the history of science. Steinle (2016) considers the extent to which it is such a theme. He presents a variety of cases from the history of science where replication played very different roles, although he understands “replication” narrowly to refer to when an experiment is re-run *by different researchers*. He claims that the role and value of replication in experimental replication is “much more complex than easy textbook accounts make us believe” (2016: 60), particularly since each scientific inquiry is always tied to a variety of contextual considerations that can affect the importance of replication. Such considerations include the relationship between experimental results and the background of accepted theory at the time, the practical and resource constraints on pursuing replication and the perceived credibility of the researchers. These contextual factors, he claims, mean that replication was a key or even overriding determinant of acceptance of research claims in some cases, but not in others.

For example, sometimes replication was sufficient to embrace a research claim, even if it conflicted with the background of accepted theory and left theoretical questions unresolved. A case of this is high-temperature superconductivity, the effect whereby an electric current can pass with zero resistance through a conductor at relatively high temperatures. In 1986, physicists Georg Bednorz and Alex Müller reported finding a material which acted as a superconductor at 35 kelvin (−238 degrees Celsius). Scientists around the world successfully replicated the effect, and Bednorz and Muller were then awarded with a Nobel Prize in Physics a year after their announcement. This case is remarkable since not only did their effect contradict the accepted physical theory at the time, but there is still no extant theory that adequately explains the effects which they reported (Di Bucchianico, 2014).

As a contrasting example, however, sometimes claims were accepted without any replication. In the 1650s, German scientist Otto von Guericke designed and operated the world’s first vacuum pump that would visibly suck air out of a larger space. He performed experiments with his device to various audiences. Yet the replication of his experiments by others would have been very difficult, if not impossible: not only was Guericke’s pump both expensive and complicated to build, but it was also unlikely that his descriptions of it sufficed to enable anyone to build the pump and to consequently replicate his findings. Despite this, Steinle claims that “no doubts were raised about his results”, probably as a results of his “public performances that could be witnessed by a large number of participants” (2016: 55).

Steinle takes such historical cases to provide normative guidance for understanding the epistemic value as replication as context-sensitive: whether replication is necessary or sufficient for establishing a research claim will depend on a variety of considerations, such as those mentioned earlier. He consequently eschews wide-reaching claims, such as those that “it’s all about replicability” or that “replicability does not decide anything” (2016: 60).

### 3.3 Formalising the Logic of Replication

Earp and Trafimow (2015) attempt to formalise the way in which replication is epistemically valuable, and they do this using a Bayesian framework to explicate the inferences drawn from replication studies. They present the framework in a context similar to that of Collins (1985), noting that “it is well-nigh impossible to say conclusively what [replication results] mean” (Earp & Trafimow, 2015: 3)[^earp-2015]. But while replication studies are often not conclusive, they do believe that such studies can be *informative*, and their Bayesian framework depicts how this is so.

The framework is set out with an example. Suppose an aficionado of Researcher *A* is highly confident that anything said by Researcher *A* is true. Some other researcher, Researcher *B*, then attempts to replicate an experiment by Researcher *A*, and Researcher *B* find results that conflict with those of Researcher *A*. Earp and Trafimow claim that the aficionado might continue to be confident in Researcher *A*’s findings, but the aficionado’s confidence is likely to slightly decrease. As the number of failed replication attempts increases, the aficionado’s confidence accordingly decreases, eventually falling below 50% and thereby placing more confidence in the replication failures than in the findings initially reported by Researcher *A*.

Here, then, suppose we are interested in the probability that the original result reported by Researcher *A* is true given Researcher *B*’s first replication failure. Earp and Trafimow represent this probability with the notation $p(T\mid F)$ where *p* is a probability function, *T* represents the proposition that the original result is true and *F* represents Researcher *B*’s replication failure. According to Bayes’s theorem below, this probability is calculable from the aficionado’s degree of confidence that the original result is true *prior* to learning of the replication failure $p(T)$, their degree of expectation of the replication failure on the condition that the original result is true $p(F\mid T)$, and the degree to which they would unconditionally expect a replication failure prior to learning of the replication failure $p(F)$:

$$\tag{1} p(T\mid F) = \frac{p(T)p(F\mid T)}{p(F)} $$

Relatedly, we could instead be interested in the confidence ratio that the original result is true or false given the failure to replicate. This ratio is representable as $\frac{p(T\mid F)}{p(\nneg T\mid F)}$ where $\nneg T$ represents the proposition that the original result is false. According to the standard Bayesian probability calculus, this ratio in turn is related to a product of ratios concerning

1. the confidence that the original result is true $\frac{p(T)}{p(\nneg T)}$ and
2. the expectation of a replication failure on the condition that the result is true or false $\frac{p(F\mid T)}{p(F\mid \nneg T)}$.

This relation is expressed in the equation:

$$\tag{2} \frac{p(T\mid F)}{p(\nneg T\mid F)} = \frac{p(T)}{p(\nneg T)} \frac{p(F\mid T)}{p(F\mid \nneg T)} $$

Now Earp and Trafimow assign some values to the terms on the right-hand of the equation for (2). Supposing that the aficionado is confident in the original results, they set the ratio $\frac{p(T)}{p(\nneg T)}$ to 50, meaning that the aficionado is initially fifty times more confident that the results are true than that the results are false.

They also set the ratio $\frac{p(F\mid T)}{p(F\mid \nneg T)}$. about the conditional expectation of a replication failure to 0.5, meaning that the aficionado is considerably less confident that there will be a replication failure if the original result is true than if it is false. They point out that the extent to which the aficionado is less confident depends on the quality of so-called *auxiliary assumptions* about the replication experiment. Here, auxiliary assumptions are assumptions which enable one to infer that particular things should be observable if the theory under test is true. The intuitive idea is that the higher the quality of the assumptions about a replication study, the more one would expect to observe a successful replication if the original result was true. While they do not specify precisely what makes such auxiliary assumptions have high “quality” in this context, presumably this quality concerns the extent to which the assumptions are probably true and the extent to which the replication experiment is an appropriate test of the veracity of the original results if the assumptions are true.

Once the ratios on the right-hand of equation (2) are set as such, one can see that a replication failure would reduce one’s confidence in the original results:

$$\tag{3} \begin{align} \frac{p(T\mid F)}{p(\nneg T\mid F)} & = \frac{p(T)}{p(\nneg T)} \frac{p(F\mid T)}{p(F\mid \nneg T)} \\ & = (50)(0.5) \\ & = 25\\ \end{align} $$

Here, then, a replication failure would reduce the aficionado’s confidence that the original result was true so that the aficionado would be only 25 times more confident that the result is true given a failure (as per $\frac{p(T\mid F)}{p(\nneg T\mid F)}$) rather than 50 times more confident that it is true (as per $\frac{p(T)}{p(\nneg T)}$).

Nevertheless, the aficionado may still be confident that the original result is true, but we can see how such confidence would decrease with successive replication failures. More formally, let $F_N$ be the last replication failure in a sequence of *N* replication failures $\langle F_1,F_2,\ldots,F_N\rangle$. Then, the aficionado’s confidence in the original result given the *N*th replication failure is expressible in the equation:[^note-3]

$$\tag{4} \frac{p(T\mid F_N)}{p(\nneg T\mid F_N)} = \frac{p(T)}{p(\nneg T)} \frac{p(F_1\mid T)}{p(F_1\mid \nneg T)} \frac{p(F_2\mid T)}{p(F_2\mid \nneg T)} \cdots \frac{p(F_N\mid T)}{p(F_N\mid \nneg T)} $$

For example, suppose there are 10 replication failures, and so $N=10$. Suppose further that the confidence ratios for the replication failures are set such that:

$$\tag{5} \begin{multline} \phantom{ab}\frac{p(F_1\mid T)}{p(F_1\mid \nneg T)} \frac{p(F_2\mid T)}{p(F_2\mid \nneg T)} \cdots \frac{p(F_{10}\mid T)}{p(F_{10}\mid \nneg T)}\\ \phantom{ab} = (0.5)(0.8) (0.7)(0.65) (0.75)(0.56) (0.69)(0.54) (0.73)(0.52) \end{multline} $$

Then,

$$\tag{6} \begin{align} \frac{p(T \mid F_{10})}{p(\nneg T \mid F_{10})} & = 0.54 \\ & = \frac{p(T)}{p(\nneg T)} \frac{p(F_1\mid T)}{p(F_1\mid \nneg T)} \frac{p(F_2\mid T)}{p(F_2\mid \nneg T)} \cdots \frac{p(F_{10}\mid T)}{p(F_{10}\mid \nneg T)} \\ & = (50)(0.5)(0.8)\ldots(0.52) \end{align} $$

Here, then, the aficionado’s confidence in the original result decreases so that they are more confident that it was false than that it was true. Hence, on Earp and Trafimow’s Bayesian account, successive replication failures can progressively erode one’s confidence that an original result is true, even if one was initially highly confident in the original result and even if no single replication failure by itself was conclusive.[^note-4]

Some putative merits of Earp and Trafimow’s account, then, are that it provides a formalisation whereby replication attempts are informative even if they are not conclusive, and furthermore, the formalisation provides a role for both quantity of replication attempts as well as auxiliary assumptions about the replications.

## 4. Open Science Reforms: Values, Tone, and Scientific Norms

The aforementioned meta-science has unearthed a range of problems which give rise to the reproducibility crisis, and the open science movement has proposed or promoted various solutions—or reforms—for these problems. These reforms can be grouped into four categories: (a) methods and training, (b) reporting and dissemination, (c) peer review processes, and (d) evaluating new incentive structures (loosely following the categories used by Munafò et al. 2017 and Ioannidis et al. 2015)[^ioannidis-2015][^munafò-2017]. In subsections 4.1–4.4 below, we present a non-exhaustive list of initiatives in each of the above categories. These initiatives are reflections of various values and norms that are at the heart of the open science movement, and we discuss these values and norms in 4.5.

### 4.1 Methods and Training

- *Combating bias.* The development of methods for combating bias, for example, masked or blind analysis techniques to combat confirmation bias (e.g., MacCoun & Perlmutter 2017)[^maccoun-2017].
- *Support.* Providing methodological support for researchers, including published guidelines and statistical consultancy (for example, as offered by the Center for Open Science) and large online courses such as that developed by Daniel Lakens (see Other Internet Resources).
- *Collaboration.* Promoting collaboration and team/crowd sourced science to combat low power and other methodological limitations of single studies. The Reproducibility Projects themselves are an example of this, but there are other initiatives too such StudySwap in psychology and the Collective Replication and Education Project (CREP, see Other Internet Resources for both of these , see also Munafò et al. for a more detailed description) which aims to increase the prevalence of replications through undergraduate education.

### 4.2 Reporting and Dissemination

- *The TOP Guidelines.* The Transparency and Openness Promotion (TOP) guidelines (Nosek et al. 2015)[^nosek-2015] have, as at the end of May, 2018, almost 5,000 journals and organizations as signatories. Developed within psychology, TOP guidelines have formed the basis of other disciplinary specific guidelines, such as the Tools for Transparency in Ecology and Evolution (TTEE). As the name suggests, these guidelines promote more complete and transparent reporting of methodological and statistical practices. This in turn enables authors, reviewers and editors to consider detailed aspects of their sample size planning and design decisions, and to clearly distinguish between confirmatory (planned) analysis and exploratory (post hoc) analysis.
- *Pre-registration*. In its simplest form, pre-registration involves making a public, date-stamped statement of predictions and/or hypotheses, either before data is collected, viewed or analysed. The purpose is to distinguish prediction from postdiction (Nosek et al. 2018)[^nosek-2018], or what is elsewhere referred to as confirmatory research from exploratory research (Wagenmakers et al. 2012)[^wagenmakers-2012] and a distinction perhaps more commonly known as hypothesis testing versus hypothesis generating research. Pre-registration of predictive research helps control for HARKing (Kerr 1998)[^kerr-1998] and hindsight bias, and within the frequentist Null Hypothesis Significance Testing, helps contain the false positive error rate to the set alpha level. There are several platforms that host pre-registrations, such as the Open Science Framework (osf.io) and As Predicted (aspredicted.org). The Open Science Framework also hosts a “pre-registration challenge” offering monetary rewards for publishing pre-registered work.
- *Specific Journal Initiatives*. Some high impact journals, having been singled out in the science media as having particularly problematic publishing practices (e.g., Schekman 2013)[^schekman-2013], have taken exceptional steps to improve the completeness, transparency and reproducibility of the research they publish. For example, since 2013, *Nature* and Nature research journals have engaged in a range of editorial activities aimed at improving reproducibility of research published in their journals (see the [editorial announcement](https://www.nature.com/news/announcement-reducing-our-irreproducibility-1.12852), *Nature* 496, 398, 25 April 2013, doi:10.1038/496398a). In 2017, they introduced checklists and reporting summaries (published alongside articles) in an effort to improve transparency and reproducibility. In 2018, they produced discipline specific versions for *Nature Human Behaviour* and *Nature Ecology & Evolution*. Within psychology, the journal *Psychological Science* (flagship journal of the Association of Psychological Science) was the first to adopt open science practices, such the COS Open Science badges described below. Following a meeting of ecology and evolution journal editors in 2015, a number of journals in these fields have run editorials on this topic, often committing to TTEE guidelines (discussed above). *Conservation Biology* has in addition adopted a checklist for associate editors (Parker et al. 2016)[^parker-2016].

### 4.3 Peer Review

- *Registered reports*. Registered reports shift the point at which peer review occurs in the research process, in an effort to combat publication bias against null (negative) results. Manuscripts are submitted, reviewed and a publication decision made on the basis of the introduction, methods and planned analysis alone. If accepted, authors then have a defined period of time to carry out the planned research and submit the results. Assuming authors followed their original plans (or adequately justified deviations from them), the journal will honour its decision to publish, regardless of the result outcomes. In psychology, the Registered Report format has been championed by Chris Chambers, with the journal *Cortex* being the first to adopt the format under Chambers’ editorship (Chambers 2013, 2017; Nosek & Lakens 2014)[^chambers-2013][^chambers-2017][^nosek-2014]. Currently (end of May 2018), 108 journals in a range of biomedical, psychology and neuroscience fields, offer the format (see Registered Reports in Other Internet Resources).
- *Pre-prints.* Well-established in some sciences like physics, the use of pre-print servers is relatively new in biological and social sciences.

### 4.4 Incentives and Evaluations

- *Open Science badges.* A recent review of initiatives for improving data sharing identified the awarding of open data and open materials badges as the most effective scheme (Rowhani-Farid, Allen, & Barnett 2017)[^rowhani-farid-2017]. One such badge scheme is coordinated by the Center for Open Science who currently award three badges: Open Data, Open Materials and Pre-Registration. Badges are attached to articles that follow a specific set of criteria to engage in these activities. Kidwell et al. (2016) evaluated the effectiveness of badges in the journal *Psychological Science* and found substantial increases (from 3 to 39%) in data sharing over a less than two-year period. Such increases were not found in similar journals without badge schemes over the same period.

### 4.5 Values, Tone, and Scientific Norms in Open Science Reform

There has long been philosophical debate about what role values do and should play in science (Churchman 1948; Rudner 1953; Douglas 2016)[^churchman-1948][^douglas-2016][^rudner-1953], and the reproducibility crisis is intimately connected to questions about the operations of, and interconnections between, such values. In particular, Nosek et al. (2017) argue that there is a tension between truth and publishability. More specifically, for reasons discussed in section 2 above, the accuracy of scientific results are compromised by the value which journals place on novel and positive results and, consequently, by scientists who value career success to seek to exclusively publish such results in these journals. Many others in addition to Nosek et al. (Hackett 2005; Martin 1992; Sovacool 2008)[^hackett-2005][^martin-1992][^sovacool-2008] have taken also take issue with the value which journals and funding bodies have placed on novelty.

Some might interpret the tension as a manifestation of how epistemic values (such as truth and replicability) can be compromised by (arguably) non-epistemic values, such the value of novel, interesting or surprising results. Epistemic values are typically taken to be values that, in the words of Steel “promote the acquisition of true beliefs” (2010: 18; see also Goldman 1999)[^goldman-1999]. Canonical examples of epistemic values include the predictive accuracy and internal consistency of a theory. Epistemic values are often contrasted with putative non-epistemic or non-cognitive values, which include ethical or social values like, for example, the novelty of a theory or its ability to improve well-being by lessening power inequalities (Longino 1996)[^longino-1996]. Of course, there is no complete consensus as to precisely what counts as an epistemic or non-epistemic value (Rooney 1992; Longino 1996)[^longino-1996][^rooney-1992]. Longino, for example, claims that, other things being equal, novelty counts in favour of accepting a theory, and convincingly argues that, in some contexts, it can serve as a “protection against unconscious perpetuation of the sexism and androcentrism” in traditional science (1997: 22). However, she does not discuss novelty specifically in the context of the reproducibility crisis.

Giner-Sorolla (2012), however, does discuss novelty in the context of the crisis, and he offers another perspective on its value. He claims that one reason novelty has been used to define what is publishable or fundable is that it is relatively easy for researchers to establish and for reviewers and editors to detect. Yet, Giner-Sorolla argues, novelty for its own sake perhaps should not be valued, and should in fact be recognized as merely an operationalisation of a deeper concept, such as “ability to advance the field” (567). Giner-Sorolla goes on to point out how such shallow operationalisations of important concepts often lead to problems, for example, using statistical significance to measure the importance of results, or measuring the quality of research by how well outcomes fit with experimenters’ prior expectations.

Values are closely connected to discussions about norms in the open science movement. Vazire (2018) and others invoke norms of science—*communality, universalism, disinterestedness and organised skepticism*—in setting the goals for open science, norms originally articulated by Robert Merton (1942). Each such norm arguably reflects a value which Merton advocated, and each norm may be opposed by a counternorm which denotes behaviour that is in conflict with the norm. For example, the norm of communality (which Merton called “communism”) reflects the value of collaboration and the common ownership of scientific goods since the norm recommends such collaboration and common ownership. Advocates of open science see such norms, and the values which they reflect, as an aim for open science. For example, the norm of communality is reflected in sharing and making data open, and in open access publishing. In contrast, the counternorm of secrecy is associated with a closed, for profit publishing system (Anderson et al. 2010)[^anderson-2010]. Likewise, assessing scientific work on its merits upholds the norm of universalism—that the evaluation of research claims should not depend on the socio-demographic characteristics of the proponents of such claims. In contrast, assessing work by the age, the status, the institution or the metrics of the journal it is published in reflects a counternorm of particularism.

Vazire (2018) and others have argued that, at the moment, scientific practice is dominated by counternorms and that a move to Mertonian norms is a goal of the open science reform movement. In particular, self-interestedness, as opposed to the norm of disinterestedness, motivates *p*-hacking and other Questionable Research Practices. Similarly, a desire to protect one’s professional reputation motivates resistance to having one’s work replicated by others (Vazire 2018)[^vazire-2018]. This in turn reinforces a counternorm of organized dogmatism rather than organized skepticism which, according to Merton, involves the “temporary suspension of judgment and the detached scrutiny of beliefs” (Merton, 1973).

Anderson et al.’s (2010) focus groups and surveys of scientists suggest that scientists do want to adhere to Merton’s norms but that the current incentive structure of science makes this difficult. Changing the structure of penalty and reward systems within science to promote communality, universalism, disinterestedness and organized skepticism instead of their counternorms is an ongoing challenge for the open science reform movement. As Pashler and Wagenmakers (2012) have said:

> replicability problems will not be so easily overcome, as they reflect deep-seated human biases and well-entrenched incentives that shape the behavior of individuals and institutions. (2012: 529)

The effort to promote such values and norms has generated heated controversy. Some early responses to the Reproducibility Project: Psychology and Many Labs projects were highly critical, not just of the substance of the nature and process of the work. Calls for openness were interpreted as reflecting mistrust, and attempts to replicate others’ work as personal attacks (e.g., Schnail 2014 in Other Internet Resources). Nosek, Spies, & Motyl (2012) argue that calls for openness should not be interepreted as mistrust:

> Opening our research process will make us feel accountable to do our best to get it right; and, if we do not get it right, to increase the opportunities for others to detect the problems and correct them. Openness is not needed because we are untrustworthy; it is needed because we are human. (2012: 626)

Exchanges related to this have become known as the *tone debate*.[^note-5]

## 5. Conclusion

The subject of reproducibility is associated with a turbulent period in contemporary science. This period has called for a re-evaluation of the values, incentives, practices and structures which underpin scientific inquiry. While the meta-science has painted a bleak picture of reproducibility in some fields, it has also inspired a parallel movement to strengthen the foundations of science. However, more progress is to be made, especially in understanding the solutions to the reproducibility crisis. In this regard, there are fruitful avenues for future research, including a deeper exploration of the role that epistemic and non-epistemic values can or should play in scientific inquiry.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=scientific-reproducibility). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/scientific-reproducibility/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=scientific-reproducibility&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](http://philpapers.org/sep/scientific-reproducibility/) at [PhilPapers](http://philpapers.org/), with links to its database. |

## Other Internet Resources

- Barba, Lorena A., 2017, “[Science Reproducibility Taxonomy](https://figshare.com/articles/Science_Reproducibility_Taxonomy/5248273)”, Presentation slides for the *2017 Workshop on Reproducibility Taxonomies for Computing and Computational Science*.
- McShane, Blakeley B., David Gal, Andrew Gelman, Christian Robert, and Jennifer L. Tackett, 2018, “[Abandon Statistical Significance](http://arxiv.org/abs/1709.07588)”, arXiv.org, first version 22 September 2017; latest revision, 8 September 2018.
- Schnall, Simone, 2014, “[Social Media and the Crowd-Sourcing of Social Psychology](https://www.psychol.cam.ac.uk/cece/blog)”, Blog *Department of Psychology, Cambridge University*, November 18.
- [Tilburg University Meta-Research Center](https://metaresearch.nl/)
- [Meta-Research Innovation Center at Stanford (METRICS)](https://metrics.stanford.edu/)
- [The saga of the summer 2017, a.k.a. ‘the alpha wars’](http://www.barelysignificant.com/post/summersaga/), Barely Significant blog by Ladislas Nalborczyk.
- [2017 American Statistical Association Symposium on Statistical Inference: Scientific Method for the 21ˢᵗ Century: A World Beyond $p <0.05$](http://ww2.amstat.org/meetings/ssi/2017/conferenceinfo.cfm)
- [Improving Your Statistical Inferences,](https://www.coursera.org/learn/statistical-inferences) David Lakens, 2018, Coursera,
- [StudySwap: A Platform for Interlab Replication, Collaboration, and Research Resource Exchange](https://osf.io/view/StudySwap/), Open Science Framework
- [Collaborative Replications and Education Project (CREP)](https://osf.io/wfc6u/), Open Science Framework
- [Registered Reports: Peer review before results are known to align scientific values and practices](https://cos.io/rr/), Center for Open Science

## Related Entries

Bayes’ Theorem | epistemology: Bayesian | measurement: in science | operationalism | science: theory and observation in | scientific knowledge: social dimensions of | scientific method | scientific research and big data

## Notes（原文脚注）

[^note-1]: Here, the inverse probability fallacy occurs when someone mistakes the probability of proposition *p* given proposition *q* for the probability of proposition *q* given proposition *p*. Consider the difference between the probability that someone is a human given that they are a female human (a probability of 100%) versus the probability that someone is a female human given that they are a human (a probability of around 50%). In this sense, someone would commit the fallacy if they believed that the *p* value specifies that probability that the null hypothesis is true given the results instead of it specifying the probability of obtaining the results if the null hypothesis were true. Consequently, if someone believes that the *p* value specifies the probability of the null hypothesis given the evidence, then why would they worry about the statistical power—the *a priori* probability of correctly rejecting the null hypothesis and detecting an effect when it is really present?

[^note-2]: Like Feest (2016), other philosophers of science may recognize a resemblance between the experimenter’s regress and the Duhem-Quine problem: both problems concern the limitations of evidence insofar as it putatively underdetermines which propositions to accept.

[^note-3]: Technically, the term $p(T \mid F_N)$ should instead be $p(T \mid F_1 \amp F_2 \amp \ldots \amp F_N)$ since $p(T \mid F_N)$ is the probability of *T* conditional on only the last replication failure $F_N$ and not the other failures (unless, of course, by $p(T \mid F_N)$, they really mean some other probability function $p\prime$ which has conditionalized on the other failures and would thus be a different probability function than the one used for $ p(T))$. The other replications failures would ideally feature in the antecedent conditions of particular other conditional probabilities too. Regardless, we have reproduced Earp and Trafimow’s presentation of the Bayesian framework here despite these technical details.

[^note-4]: Technically, this is only given an additional principle not discussed explicitly by Earp and Trafimow. This is the principle of conditionalisation whereby one’s so-called *posterior* degree of belief in a proposition *P* *after* the receipt of some evidence *E* should be equal to their *prior* degree of belief in *P* given *E* *before* the receipt of evidence *E*. Earp and Trafimow only explicitly discuss the relations between degrees of belief at a given time (synchronic relations), rather than the relations between degrees of belief at two different points in time (diachronic relations).

[^note-5]: For example, critics have referred to replication and open science advocates as “replication police” and “shameless little bullies” ([Gilbert 2014 online post](https://twitter.com/dantgilbert/status/470199929626193921?lang=en)) and accused “angry mobs” of conducting an “inquisition” ([Bohannon 2014 online post](https://www.sciencemag.org/news/2014/05/replication-effort-provokes-praise-and-bullying-charges)). High profile replication studies, such as that of Amy Cuddie’s power poses, have been used in attempts to establish bullying charges (Dominus 2017)[^dominus-2017]. In a publicly released draft of a guest column for the Association of Psychological Science (APS) *Observer*, past APS president Susan Fiske referred to those involved in replication and meta-science work as “methodological terrorists” ([Fiske 2016 draft](https://www.dropbox.com/s/9zubbn9fyi1xjcu/Fiske%20presidential%20guest%20column_APS%20Observer_copy-edited.pdf)). She was especially scathing of “public shaming and blaming” by “online vigilantes” and “destructo-critics”. In the final published version of this column (Fiske 2016)[^fiske-2016], she retracted some of these phrases, but the draft had already sparked many social media responses from open science advocates who largely view the tone debate as a distraction from their key issues (e.g., [Chambers 2017 online post](http://neurochambers.blogspot.com/2017/08/why-i-hate-tone-debate-in-psychology.html), and Sutton 2018).

[^agnoli-2017]: Agnoli, Franca, Jelte M. Wicherts, Coosje L. S. Veldkamp, Paolo Albiero, and Roberto Cubelli, 2017, “Questionable Research Practices among Italian Research Psychologists”, Jakob Pietschnig (ed.), *PLoS ONE*, 12(3): e0172792. doi:10.1371/journal.pone.0172792

[^allen-2016]: Allen, Peter J., Kate P. Dorozenko, and Lynne D. Roberts, 2016, “Difficult Decisions: A Qualitative Exploration of the Statistical Decision Making Process from the Perspectives of Psychology Students and Academics”, *Frontiers in Psychology*, 7(February): 188. doi:10.3389/fpsyg.2016.00188

[^anderson-2016]: Anderson, Christopher J., Štěpán Bahnik, Michael Barnett-Cowan, Frank A. Bosco, Jesse Chandler, C. R. Chartier, F. Cheung, et al., 2016, “Response to Comment on ‘Estimating the Reproducibility of Psychological Science’”, *Science*, 351(6277): 1037. doi:10.1126/science.aad9163

[^anderson-2010]: Anderson, Melissa S., Emily A. Ronning, Raymond De Vries, and Brian C. Martinson, 2010, “Extending the Mertonian Norms: Scientists’ Subscription to Norms of Research”, *The Journal of Higher Education*, 81(3): 366–393. doi:10.1353/jhe.0.0095

[^atmanspacher-2016a]: Atmanspacher, Harald and Sabine Maasen, 2016a, “Introduction”, in Atmanspacher and Maasen 2016b: 1–8. doi:10.1002/9781118865064.ch0

[^atmanspacher-2016b]: ––– (eds.), 2016b, *Reproducibility: Principles, Problems, Practices, and Prospects*, Hoboken, NJ: John Wiley & Sons. doi:10.1002/9781118865064

[^baker-2016]: Baker, Monya, 2016, “1,500 Scientists Lift the Lid on Reproducibility”, *Nature*, 533(7604): 452–454. doi:10.1038/533452a

[^bakker-2016]: Bakker, Marjan, Chris H. J. Hartgerink, Jelte M. Wicherts, and Han L. J. van der Maas, 2016, “Researchers’ Intuitions About Power in Psychological Research”, *Psychological Science*, 27(8): 1069–1077. doi:10.1177/0956797616647519

[^bakker-2011]: Bakker, Marjan and Jelte M. Wicherts, 2011, “The (Mis)Reporting of Statistical Results in Psychology Journals”, *Behavior Research Methods*, 43(3): 666–678. doi:10.3758/s13428-011-0089-5

[^begley-2012]: Begley, C. Glenn and Lee M. Ellis, 2012, “Raise Standards for Preclinical Cancer Research: Drug Development”, *Nature*, 483(7391): 531–533. doi:10.1038/483531a

[^bem-2011]: Bem, Daryl J., 2011, “Feeling the Future: Experimental Evidence for Anomalous Retroactive Influences on Cognition and Affect”, *Journal of Personality and Social Psychology*, 100(3): 407–425.

[^benjamin-2018]: Benjamin, Daniel J., James O. Berger, Magnus Johannesson, Brian A. Nosek, Eric-Jan Wagenmakers, Richard Berk, Kenneth A. Bollen, et al., 2018, “Redefine Statistical Significance”, *Nature Human Behaviour*, 2(1): 6–10. doi:10.1038/s41562-017-0189-z

[^braude-1979]: Braude, Stephen E., 1979, *ESP and Psychokinesis. A Philosophical Examination*, Philadelphia: Temple University Press.

[^button-2013]: Button, Katherine S., John P. A. Ioannidis, Claire Mokrysz, Brian A. Nosek, Jonathan Flint, Emma S. J. Robinson, and Marcus R. Munafò, 2013, “Power Failure: Why Small Sample Size Undermines the Reliability of Neuroscience”, *Nature Reviews Neuroscience*, 14(5): 365–376. doi:10.1038/nrn3475

[^camerer-2018]: Camerer C.F., et al., 2018, “Evaluating the replicability of social science experiments in *Nature* and *Science* between 2010 and 2015”, *Nature Human Behaviour*, 2: 637–644. doi: 10.1038/s41562-018-0399-z

[^cartwright-1991]: Cartwright, Nancy, 1991, “Replicability, Reproducibility and Robustness: Comments on Harry Collins”, *History of Political Economy*, 23(1): 143–155.

[^chambers-2013]: Chambers, Christopher D., 2013, “Registered Reports: A New Publishing Initiative at Cortex”, *Cortex*, 49(3): 609–610. doi:10.1016/j.cortex.2012.12.016

[^chambers-2017]: –––, 2017, *The Seven Deadly Sins of Psychology A Manifesto for Reforming the Culture of Scientific Practice*, Princeton: Princeton University Press.

[^chang-2015]: Chang, Andrew C. and Phillip Li, 2015, “Is Economics Research Replicable? Sixty Published Papers from Thirteen Journals Say ‘Usually Not’”, *Finance and Economics Discussion Series*, 2015(83): 1–26. doi:10.17016/FEDS.2015.083

[^churchman-1948]: Churchman, C. West, 1948, “Statistics, Pragmatics, Induction”, *Philosophy of Science*, 15(3): 249–268. doi:10.1086/286991

[^collins-1985]: Collins, Harry M., 1985, *Changing Order: Replication and Induction in Scientific Practice*, London; Beverly Hills: Sage Publications.

[^collins-2016]: –––, 2016, “Reproducibility of experiments: experiments’ regress, statistical uncertainty principle, and the replication imperative” in Atmanspacher and Maasen 2016b: 65–82. doi:10.1002/9781118865064.ch4

[^cohen-1962]: Cohen, Jacob, 1962, “The Statistical Power of Abnormal-Social Psychological Research: A Review”,, *The Journal of Abnormal and Social Psychology*, 65(3): 145–153. doi:10.1037/h0045186

[^cohen-1994]: –––, 1994, “The Earth Is Round ($p < .05$)”, *American Psychologist*, 49(12): 997–1003, doi:10.1037/0003-066X.49.12.997

[^cova-2018]: Cova, Florian, Brent Strickland, Angela Abatista, Aurélien Allard, James Andow, Mario Attie, James Beebe, et al., forthcoming, “Estimating the Reproducibility of Experimental Philosophy”, *Review of Philosophy and Psychology*, early online: 14 June 2018. doi:10.1007/s13164-018-0400-9

[^cristea-2018]: Cristea, Ioana Alina and John P. A. Ioannidis, 2018, “P Values in Display Items Are Ubiquitous and Almost Invariably Significant: A Survey of Top Science Journals”, Christos A. Ouzounis (ed.), *PLoS ONE*, 13(5): e0197440. doi:10.1371/journal.pone.0197440

[^cumming-2012]: Cumming, Geoff, 2012, *Understanding the New Statistics: Effect Sizes, Confidence Intervals, and Meta-Analysis*. New York: Routledge.

[^cumming-2017]: Cumming, Geoff and Robert Calin-Jageman, 2017, *Introduction to the New Statistics: Estimation, Open Science and Beyond*, New York: Routledge.

[^cumming-2007]: Cumming, Geoff, Fiona Fidler, Martine Leonard, Pavel Kalinowski, Ashton Christiansen, Anita Kleinig, Jessica Lo, Natalie McMenamin, and Sarah Wilson, 2007, “Statistical Reform in Psychology: Is Anything Changing?”, *Psychological Science*, 18(3): 230–232. doi:10.1111/j.1467-9280.2007.01881.x

[^di-2014]: Di Bucchianico, Marilena, 2014, “A Matter of Phronesis: Experiment and Virtue in Physics, A Case Study”, in *Virtue Epistemology Naturalized*, Abrol Fairweather (ed.), Cham: Springer International Publishing, 291–312. doi:10.1007/978-3-319-04672-3_17

[^dominus-2017]: Dominus, Susan, 2017, “When the Revolution Came for Amy Cuddy”, *The New York Times*, October 21, Sunday Magazine, page 29.

[^douglas-2016]: Douglas, Heather, 2016, “Values in Science”, in Paul Humphreys, *The Oxford Handbook of Philosophy of Science*, New York: Oxford University Press, pp. 609–630.

[^earp-2015]: Earp, Brian D. and David Trafimow, 2015, “Replication, Falsification, and the Crisis of Confidence in Social Psychology”, *Frontiers in Psychology*, 6(May): 621. doi:10.3389/fpsyg.2015.00621

[^errington-2014]: Errington, Timothy M., Elizabeth Iorns, William Gunn, Fraser Elisabeth Tan, Joelle Lomax, and Brian A Nosek, 2014, “An Open Investigation of the Reproducibility of Cancer Biology Research”, *ELife*, 3(December): e043333. doi:10.7554/eLife.04333

[^etz-2016]: Etz, Alexander and Joachim Vandekerckhove, 2016, “A Bayesian Perspective on the Reproducibility Project: Psychology”, Daniele Marinazzo (ed.), *PLoS ONE*, 11(2): e0149794. doi:10.1371/journal.pone.0149794

[^fanelli-2010a]: Fanelli, Daniele, 2010a, “Do Pressures to Publish Increase Scientists’ Bias? An Empirical Support from US States Data”, Enrico Scalas (ed.), *PLoS ONE*, 5(4): e10271. doi:10.1371/journal.pone.0010271

[^fanelli-2010b]: –––, 2010b, “‘Positive’ Results Increase Down the Hierarchy of the Sciences”, Enrico Scalas (ed.), *PLoS ONE*, 5(4): e10068. doi:10.1371/journal.pone.0010068

[^fanelli-2012]: –––, 2012, “Negative Results Are Disappearing from Most Disciplines and Countries”, *Scientometrics*, 90(3): 891–904. doi:10.1007/s11192-011-0494-7

[^fang-2012]: Fang, Ferric C., R. Grant Steen, and Arturo Casadevall, 2012, “Misconduct Accounts for the Majority of Retracted Scientific Publications”, *Proceedings of the National Academy of Sciences*, 109(42): 17028–17033. doi:10.1073/pnas.1212247109

[^feest-2016]: Feest, Uljana, 2016, “The Experimenters’ Regress Reconsidered: Replication, Tacit Knowledge, and the Dynamics of Knowledge Generation”, *Studies in History and Philosophy of Science Part A*, 58(August): 34–45. doi:10.1016/j.shpsa.2016.04.003

[^fidler-2006]: Fidler, Fiona, Mark A. Burgman, Geoff Cumming, Robert Buttrose, and Neil Thomason, 2006, “Impact of Criticism of Null-Hypothesis Significance Testing on Statistical Reporting Practices in Conservation Biology”, *Conservation Biology*, 20(5): 1539–1544. doi:10.1111/j.1523-1739.2006.00525.x

[^fidler-2017]: Fidler, Fiona, Yung En Chee, Bonnie C. Wintle, Mark A. Burgman, Michael A. McCarthy, and Ascelin Gordon, 2017, “Metaresearch for Evaluating Reproducibility in Ecology and Evolution”, *BioScience*, 67(3): 282–289. doi:10.1093/biosci/biw159

[^fiedler-2016]: Fiedler, Klaus and Norbert Schwarz, 2016, “Questionable Research Practices Revisited”, *Social Psychological and Personality Science*, 7(1): 45–52. doi:10.1177/1948550615612150

[^fiske-2016]: Fiske, Susan T., 2016, “A Call to Change Science’s Culture of Shaming”, *Association for Psychological Science Observer*, 29(9). [[Fiske 2016 available online](https://www.psychologicalscience.org/observer/a-call-to-change-sciences-culture-of-shaming)]

[^franklin-1989]: Franklin, Allan, 1989, “The Epistemology of Experiment”, in David Gooding, Trevor Pinch, and Simon Schaffer (eds.), *The Uses of Experiment: Studies in the Natural Sciences*, Cambridge: Cambridge University Press, pp. 437–460.

[^franklin-1994]: –––, 1994, “How to Avoid the Experimenters’ Regress”, *Studies in History and Philosophy of Science Part A*, 25(3): 463–491. doi:10.1016/0039-3681(94)90062-0

[^franklin-2016]: Franklin, Allan and Harry Collins, 2016, “Two Kinds of Case Study and a New Agreement”, in *The Philosophy of Historical Case Studies*, Tilman Sauer and Raphael Scholl (eds.), Cham: Springer International Publishing, 319: 95–121. doi:10.1007/978-3-319-30229-4_6

[^fraser-2018]: Fraser, Hannah, Tim Parker, Shinichi Nakagawa, Ashley Barnett, and Fiona Fidler, 2018, “Questionable Research Practices in Ecology and Evolution”, Jelte M. Wicherts (ed.), *PLoS ONE*, 13(7): e0200303. doi:10.1371/journal.pone.0200303

[^freedman-2015]: Freedman, Leonard P., Iain M. Cockburn, and Timothy S. Simcoe, 2015, “The Economics of Reproducibility in Preclinical Research”, *PLoS Biology*, 13(6): e1002165. doi:10.1371/journal.pbio.1002165

[^giner-sorolla-2012]: Giner-Sorolla, Roger, 2012, “Science or Art? How Aesthetic Standards Grease the Way Through the Publication Bottleneck but Undermine Science”, *Perspectives on Psychological Science*, 7(6): 562–571. doi:10.1177/1745691612457576

[^gigerenzer-2018]: Gigerenzer, Gerd, 2018, “Statistical Rituals: The Replication Delusion and How We Got There”, *Advances in Methods and Practices in Psychological Science*, 1(2): 198–218. doi:10.1177/2515245918771329

[^gilbert-2016]: Gilbert, Daniel T., Gary King, Stephen Pettigrew, and Timothy D. Wilson, 2016, “Comment on ‘Estimating the Reproducibility of Psychological Science’”, *Science*, 351(6277): 1037–1037. doi:10.1126/science.aad7243

[^goldman-1999]: Goldman, Alvin I., 1999, *Knowledge in a Social World*, Oxford: Clarendon. doi:10.1093/0198238207.001.0001

[^gómez-2010]: Gómez, Omar S., Natalia Juristo, and Sira Vegas, 2010, “Replications Types in Experimental Disciplines”, in *Proceedings of the 2010 ACM-IEEE International Symposium on Empirical Software Engineering and Measurement - ESEM ’10*, Bolzano-Bozen, Italy: ACM Press. doi:10.1145/1852786.1852790

[^hackett-2005]: Hackett, B., 2005, “Essential tensions: Identity, control, and risk in research”, *Social Studies of Science*, 35(5): 787–826. doi:10.1177/0306312705056045

[^haller-2002]: Haller, Heiko, and Stefan Krauss, 2002, “Misinterpretations of Significance: a Problem Students Share with Their Teachers?” *Methods of Psychological Research—Online*, 7(1): 1–20. [[Haller & Kraus 2002 available online](https://www.researchgate.net/publication/27262211_Misinterpretations_of_Significance_A_Problem_Students_Share_with_Their_Teachers)]

[^hartgerink-2016]: Hartgerink, Chris H.J., Robbie C.M. van Aert, Michèle B. Nuijten, Jelte M. Wicherts, and Marcel A.L.M. van Assen, 2016, “Distributions of *p*-Values Smaller than .05 in Psychology: What Is Going On?”, *PeerJ*, 4(April): e1935. doi:10.7717/peerj.1935

[^hendrick-1991]: Hendrick, Clyde, 1991. “Replication, Strict Replications, and Conceptual Replications: Are They Important?”, in Neuliep 1991: 41–49.

[^ioannidis-2005]: Ioannidis, John P. A., 2005, “Why Most Published Research Findings Are False”, *PLoS Medicine*, 2(8): e124. doi:10.1371/journal.pmed.0020124

[^ioannidis-2015]: Ioannidis, John P. A., Daniele Fanelli, Debbie Drake Dunne, and Steven N. Goodman, 2015, “Meta-Research: Evaluation and Improvement of Research Methods and Practices”, *PLOS Biology*, 13(10): e1002264. doi:10.1371/journal.pbio.1002264

[^jennions-2003]: Jennions, Michael D. and Anders Pape Møller, 2003, “A Survey of the Statistical Power of Research in Behavioral Ecology and Animal Behavior”, *Behavioral Ecology*, 14(3): 438–445. doi:10.1093/beheco/14.3.438

[^john-2012]: John, Leslie K., George Loewenstein, and Drazen Prelec, 2012, “Measuring the Prevalence of Questionable Research Practices With Incentives for Truth Telling”, *Psychological Science*, 23(5): 524–532. doi:10.1177/0956797611430953

[^kaiser-2018]: Kaiser, Jocelyn, 2018, “Plan to Replicate 50 High-Impact Cancer Papers Shrinks to Just 18”, *Science*, 31 July 2018. doi:10.1126/science.aau9619

[^keppel-1982]: Keppel, Geoffrey, 1982, *Design and Analysis. A Researcher’s Handbook*, second edition, Englewood Cliffs, NJ: Prentice-Hall.

[^kerr-1998]: Kerr, Norbert L., 1998, “HARKing: Hypothesizing After the Results Are Known”, *Personality and Social Psychology Review*, 2(3): 196–217. doi:10.1207/s15327957pspr0203_4

[^kidwell-2016]: Kidwell, Mallory C., Ljiljana B. Lazarević, Erica Baranski, Tom E. Hardwicke, Sarah Piechowski, Lina-Sophia Falkenberg, Curtis Kennett, et al., 2016, “Badges to Acknowledge Open Practices: A Simple, Low-Cost, Effective Method for Increasing Transparency”, Malcolm R Macleod (ed.), *PLOS Biology*, 14(5): e1002456. doi:10.1371/journal.pbio.1002456

[^klein-2014]: Klein, Richard A., Kate A. Ratliff, Michelangelo Vianello, Reginald B. Adams, Štěpán Bahník, Michael J. Bernstein, Konrad Bocian, et al., 2014, “Investigating Variation in Replicability: A ‘Many Labs’ Replication Project”, *Social Psychology*, 45(3): 142–152. doi:10.1027/1864-9335/a000178

[^lakens-2018]: Lakens, Daniel, Federico G. Adolfi, Casper J. Albers, Farid Anvari, Matthew A. J. Apps, Shlomo E. Argamon, Thom Baguley, et al., 2018, “Justify Your Alpha”, *Nature Human Behaviour*, 2(3): 168–171. doi:10.1038/s41562-018-0311-x

[^longino-1990]: Longino, Helen E., 1990, *Science as Social Knowledge: Values and Objectivity in Scientific Inquiry*, Princeton: Princeton University Press.

[^longino-1996]: –––, 1996, “Cognitive and Non-Cognitive Values in Science: Rethinking the Dichotomy”, in *Feminism, Science, and the Philosophy of Science*, Lynn Hankinson Nelson and Jack Nelson (eds.), Dordrecht: Springer Netherlands, 39–58. doi:10.1007/978-94-009-1742-2_3

[^longino-1997]: –––, 1997, “Feminist Epistemology as a Local Epistemology: Helen E. Longino”, *Aristotelian Society Supplementary Volume*, 71(1): 19–35. doi:10.1111/1467-8349.00017

[^lykken-1968]: Lykken, David T., 1968, “Statistical Significance in Psychological Research”, *Psychological Bulletin*, 70(3, Pt.1): 151–159. doi:10.1037/h0026141

[^madden-1995]: Madden, Charles S., Richard W. Easley, and Mark G. Dunn, 1995, “How Journal Editors View Replication Research”, *Journal of Advertising*, 24(December): 77–87. doi:10.1080/00913367.1995.10673490

[^makel-2012]: Makel, Matthew C., Jonathan A. Plucker, and Boyd Hegarty, 2012, “Replications in Psychology Research: How Often Do They Really Occur?”, *Perspectives on Psychological Science*, 7(6): 537–542. doi:10.1177/1745691612460688

[^maccoun-2017]: MacCoun, Robert J. and Saul Perlmutter, 2017, “Blind Analysis as a Correction for Confirmatory Bias in Physics and in Psychology”, in *Psychological Science Under Scrutiny*, Scott O. Lilienfeld and Irwin D. Waldman (eds.), Hoboken, NJ: John Wiley & Sons, pp. 295–322. doi:10.1002/9781119095910.ch15

[^martin-1992]: Martin, B., 1992, “Scientific fraud and the power structure of science”, *Prometheus*, 10(1): 83–98. doi:10.1080/08109029208629515

[^masicampo-2012]: Masicampo, E.J. and Daniel R. Lalande, 2012, “A Peculiar Prevalence of *p* Values Just below .05”, *Quarterly Journal of Experimental Psychology*, 65(11): 2271–2279. doi:10.1080/17470218.2012.711335

[^mahoney-1985]: Mahoney, Michael J., 1985, “Open Exchange and Epistemic Progress”,, *American Psychologist*, 40(1): 29–39. doi:10.1037/0003-066X.40.1.29

[^meehl-1967]: Meehl, Paul E., 1967, “Theory-Testing in Psychology and Physics: A Methodological Paradox”, *Philosophy of Science*, 34(2): 103–115. doi:10.1086/288135

[^meehl-1978]: –––, 1978, “Theoretical Risks and Tabular Asterisks: Sir Karl, Sir Ronald, and the Slow Progress of Soft Psychology”, *Journal of Consulting and Clinical Psychology*, 46(4): 806–834. doi:10.1037/0022-006X.46.4.806

[^merton-1942]: Merton, Robert K., 1942 [1973], “A Note on Science and Technology in a Democratic Order”, *Journal of Legal and Political Sociology*, 1(1–2): 115–126; reprinted as “The Normative Structure of Science”, in Robert K. Merton (ed.) *The Sociology of Science: Theoretical and Empirical Investigations*, Chicago, IL: University of Chicago Press.

[^munafò-2017]: Munafò, Marcus R., Brian A. Nosek, Dorothy V. M. Bishop, Katherine S. Button, Christopher D. Chambers, Nathalie Percie du Sert, Uri Simonsohn, Eric-Jan Wagenmakers, Jennifer J. Ware, and John P. A. Ioannidis, 2017, “A Manifesto for Reproducible Science”, *Nature Human Behaviour*, 1(1): 0021. doi:10.1038/s41562-016-0021

[^neuliep-1991]: Neuliep, James William (ed.), 1991, *Replication Research in the Social Sciences*, (Journal of social behavior and personality; 8: 6), Newbury Park, CA: Sage Publications.

[^neuliep-1990]: Neuliep, James W. and Rick Crandall, 1990, “Editorial Bias Against Replication Research”, *Journal of Social Behavior and Personality*, 5(4): 85–90

[^nosek-2014]: Nosek, Brian A. and Daniël Lakens, 2014, “Registered Reports: A Method to Increase the Credibility of Published Results”, *Social Psychology*, 45(3): 137–141. doi:10.1027/1864-9335/a000192

[^nosek-2012]: Nosek, Brian A., Jeffrey R. Spies, and Matt Motyl, 2012, “Scientific Utopia: II. Restructuring Incentives and Practices to Promote Truth Over Publishability”, *Perspectives on Psychological Science*, 7(6): 615–631. doi:10.1177/1745691612459058

[^nosek-2015]: Nosek, B. A., G. Alter, G. C. Banks, D. Borsboom, S. D. Bowman, S. J. Breckler, S. Buck, et al., 2015, “Promoting an Open Research Culture”, *Science*, 348(6242): 1422–1425. doi:10.1126/science.aab2374,

[^nosek-2018]: Nosek, Brian A., Charles R. Ebersole, Alexander C. DeHaven, and David T. Mellor, 2018, “The Preregistration Revolution”, *Proceedings of the National Academy of Sciences*, 115(11): 2600–2606. doi:10.1073/pnas.1708274114

[^nuijten-2016]: Nuijten, Michèle B., Chris H. J. Hartgerink, Marcel A. L. M. van Assen, Sacha Epskamp, and Jelte M. Wicherts, 2016, “The Prevalence of Statistical Reporting Errors in Psychology (1985–2013)”, *Behavior Research Methods*, 48(4): 1205–1226. doi:10.3758/s13428-015-0664-2

[^oakes-1986]: Oakes, Michael, 1986, *Statistical Inference: A Commentary for the Social and Behavioral Sciences*, New York: Wiley.

[^open-2015]: Open Science Collaboration (OSC), 2015, “Estimating the Reproducibility of Psychological Science”, *Science*, 349(6251): 943–951. doi:10.1126/science.aac4716

[^oransky-2016]: Oransky, Ivan, 2016, “Half of Biomedical Studies Don’t Stand up to Scrutiny and What We Need to Do about That”, *The Conversation*, 11 November 2016. [[Oransky 2016 available online](http://theconversation.com/half-of-biomedical-research-studies-dont-stand-up-to-scrutiny-and-what-we-need-to-do-about-that-45149)]

[^parker-2016]: Parker, T.H., E. Main, S. Nakagawa, J. Gurevitch, F. Jarrad, and M. Burgman, 2016, “Promoting Transparency in Conservation Science: Editorial”, *Conservation Biology*, 30(6): 1149–1150. doi:10.1111/cobi.12760

[^pashler-2012]: Pashler, Harold and Eric-Jan Wagenmakers, 2012, “Editors’ Introduction to the Special Section on Replicability in Psychological Science: A Crisis of Confidence?”, *Perspectives on Psychological Science*, 7(6): 528–530. doi:10.1177/1745691612465253

[^peng-2011]: Peng, Roger D., 2011, “Reproducible Research in Computational Science”, *Science*, 334(6060): 1226–1227. doi:10.1126/science.1213847

[^peng-2015]: –––, 2015, “The Reproducibility Crisis in Science: A Statistical Counterattack”, *Significance*, 12(3): 30–32. doi:10.1111/j.1740-9713.2015.00827.x

[^radder-1996]: Radder, Hans, 1996, *In And About The World: Philosophical Studies Of Science And Technology*, Albany, NY: State University of New York Press.

[^radder-2003]: –––, 2003, “Technology and Theory in Experimental Science”, in Hans Radder (ed.), *The Philosophy of Scientific Experimentation*, Pittsburgh: University of Pittsburgh Press, pp. 152–173.

[^radder-2006]: –––, 2006, *The World Observed/The World Conceived*, Pittsburgh, PA: University of Pittsburgh Press.

[^radder-2009]: –––, 2009, “Science, Technology and the Science-Technology Relationship”, in Anthonie Meijers (ed.), *Philosophy of Technology and Engineering Sciences*, Amsterdam: Elsevier, pp. 65–91. doi:10.1016/B978-0-444-51667-1.50007-0

[^radder-2012]: –––, 2012, *The Material Realization of Science: From Habermas to Experimentation and Referential Realism*, Boston: Springer. doi:10.1007/978-94-007-4107-2

[^rauscher-1993]: Rauscher, Frances H., Gordon L. Shaw, and Catherine N. Ky, 1993, “Music and Spatial Task Performance”, *Nature*, 365(6447): 611–611. doi:10.1038/365611a0

[^rauscher-1995]: Rauscher, Frances H., Gordon L. Shaw, and Katherine N. Ky, 1995, “Listening to Mozart Enhances Spatial-Temporal Reasoning: Towards a Neurophysiological Basis”, *Neuroscience Letters*, 185(1): 44–47. doi:10.1016/0304-3940(94)11221-4

[^ritchie-2012]: Ritchie, Stuart J., Richard Wiseman, and Christopher C. French, 2012, “Failing the Future: Three Unsuccessful Attempts to Replicate Bem’s ‘Retroactive Facilitation of Recall’ Effect”, Sam Gilbert (ed.), *PLoS ONE*, 7(3): e33423. doi:10.1371/journal.pone.0033423

[^rooney-1992]: Rooney, Phyllis, 1992, “On Values in Science: Is the Epistemic/Non-Epistemic Distinction Useful?”, *PSA: Proceedings of the Biennial Meeting of the Philosophy of Science Association*, 1992(1): 13–22. doi:10.1086/psaprocbienmeetp.1992.1.192740

[^rosenthal-1979]: Rosenthal, Robert, 1979, “The File Drawer Problem and Tolerance for Null Results”, *Psychological Bulletin*, 86(3): 638–641. doi:10.1037/0033-2909.86.3.638

[^rosenthal-1991]: –––, 1991, “Replication in Behavioral Research”, in Neuliep 1991: 1–39.

[^rosnow-1989]: Rosnow, Ralph L. and Robert Rosenthal, 1989, “Statistical Procedures and the Justification of Knowledge in Psychological Science”,, *American Psychologist*, 44(10): 1276–1284. doi:10.1037/0003-066X.44.10.1276

[^rowhani-farid-2017]: Rowhani-Farid, Anisa, Michelle Allen, and Adrian G. Barnett, 2017, “What Incentives Increase Data Sharing in Health and Medical Research? A Systematic Review”, *Research Integrity and Peer Review*, 2: 4. doi:10.1186/s41073-017-0028-9

[^rudner-1953]: Rudner, Richard, 1953, “The Scientist Qua Scientist Makes Value Judgments”, *Philosophy of Science*, 20(1): 1–6. doi:10.1086/287231

[^sargent-1981]: Sargent, C.L., 1981, “The Repeatability Of Significance And The Significance Of Repeatability”, *European Journal of Parapsychology*, 3: 423–433.

[^schekman-2013]: Schekman, Randy, 2013, “How Journals like Nature, Cell and Science Are Damaging Science | Randy Schekman”, *The Guardian*, December 9, sec. Opinion, [[Schekman 2013 available online](https://www.theguardian.com/commentisfree/2013/dec/09/how-journals-nature-science-cell-damage-science)]

[^schmidt-2009]: Schmidt, Stefan, 2009, “Shall We Really Do It Again? The Powerful Concept of Replication Is Neglected in the Social Sciences”, *Review of General Psychology*, 13(2): 90–100. doi:10.1037/a0015108

[^silberzahn-2015]: Silberzahn, Raphael,and Uhlmann, Eric L., 2015, “Many hands make tight work: crowdsourcing research can balance discussions, validate findings and better inform policy”, *Nature*, 526(7572): 189–192.

[^simmons-2011]: Simmons, Joseph P., Leif D. Nelson, and Uri Simonsohn, 2011, “False-Positive Psychology: Undisclosed Flexibility in Data Collection and Analysis Allows Presenting Anything as Significant”, *Psychological Science*, 22(11): 1359–1366. doi:10.1177/0956797611417632

[^smith-2011]: Smith, Daniel R., Ian C.W. Hardy, and Martin P. Gammell, 2011, “Power Rangers: No Improvement in the Statistical Power of Analyses Published in Animal Behaviour”, *Animal Behaviour*, 81(1): 347–352. doi:10.1016/j.anbehav.2010.09.026

[^sovacool-2008]: Sovacool, B. K., 2008, “Exploring scientific misconduct: Isolated individuals, impure institutions, or an inevitable idiom of modern science?” *Journal of Bioethical Inquiry*, 5: 271–282. doi: 10.1007/s11673-008-9113-6

[^steel-2010]: Steel, Daniel, 2010, “Epistemic Values and the Argument from Inductive Risk*”, *Philosophy of Science*, 77(1): 14–34. doi:10.1086/650206

[^stegenga-2018]: Stegenga, Jacob, 2018, *Medical Nihilism*, Oxford: Oxford University Press.

[^steinle-2016]: Steinle, Friedrich, 2016, “Stability and Replication of Experimental Results: A Historical Perspective”, in Atmanspacher and Maasen 2016b: 39–68. doi:10.1002/9781118865064.ch3

[^sterling-1959]: Sterling, Theodore D., 1959, “Publication Decisions and Their Possible Effects on Inferences Drawn from Tests of Significance – or Vice Versa”, *Journal of the American Statistical Association*, 54(285): 30–34. doi:10.1080/01621459.1959.10501497

[^sutton-2018]: Sutton, Jon, 2018, “Tone Deaf?”, *The Psychologist*, 31: 12–13. [[Sutton 2018 available online](https://thepsychologist.bps.org.uk/volume-31/march-2018/tone-deaf)]

[^szucs-2017]: Szucs, Denes and John P. A. Ioannidis, 2017, “Empirical Assessment of Published Effect Sizes and Power in the Recent Cognitive Neuroscience and Psychology Literature”, Eric-Jan Wagenmakers (ed.), *PLoS Biology*, 15(3): e2000797. doi:10.1371/journal.pbio.2000797

[^teira-2013]: Teira, David, 2013, “A Contractarian Solution to the Experimenter’s Regress”, *Philosophy of Science*, 80(5): 709–720. doi:10.1086/673717

[^vazire-2018]: Vazire, Simine, 2018, “Implications of the Credibility Revolution for Productivity, Creativity, and Progress”, *Perspectives on Psychological Science*, 13(4): 411–417. doi:10.1177/1745691617751884

[^wagenmakers-2012]: Wagenmakers, Eric-Jan, Ruud Wetzels, Denny Borsboom, Han L. J. van der Maas, and Rogier A. Kievit, 2012, “An Agenda for Purely Confirmatory Research”, *Perspectives on Psychological Science*, 7(6): 632–638. doi:10.1177/1745691612463078

[^washburn-2018]: Washburn, Anthony N., Brittany E. Hanson, Matt Motyl, Linda J. Skitka, Caitlyn Yantis, Kendal M. Wong, Jiaqing Sun, et al., 2018, “Why Do Some Psychology Researchers Resist Adopting Proposed Reforms to Research Practices? A Description of Researchers’ Rationales”, *Advances in Methods and Practices in Psychological Science*, 1(2): 166–173. doi:10.1177/2515245918757427

[^wasserstein-2016]: Wasserstein, Ronald L. and Nicole A. Lazar, 2016, “The ASA’s Statement on p-Values: Context, Process, and Purpose”, *The American Statistician*, 70(2): 129–133. doi:10.1080/00031305.2016.1154108
