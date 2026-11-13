# Epistemology of Artificial Intelligence
**First published Fri Oct 16, 2026**

*Beisbart, Claus*

Artificial intelligence (AI) is increasingly being used to obtain knowledge and understanding. For example, it is employed to detect objects in images, make predictions, examine mathematical conjectures, and infer causal connections. Indeed, over the last few years, many people have become accustomed to consulting chatbots powered by large language models when they have a question. However, are humans really justified in basing their beliefs on AI outputs? Can they claim to know things based on AI? If so, what is the justification? What kind of knowledge does AI yield? How do the procedures inherent in AI compare to well-known patterns of scientific inference? And how can AI contribute to a better understanding of real-world systems? Answering these questions remains a challenge because AI is a new technology that humans still struggle to understand fully. Many AI systems are considered “black boxes” or opaque, as it is often put.

The stunning achievements of AI in knowledge-related tasks, along with its opacity, motivate an epistemology of AI—a study of how much AI can truly contribute to the acquisition of knowledge and understanding. The epistemology of AI treats it both as an object of knowledge and as a tool that extends the capacities of epistemic agents, if it does not become an epistemic agent in its own right. As a branch of epistemology, the epistemology of AI parallels social epistemology in its departure from a focus on the unaided individual human being. However, the epistemology of AI has yet to become an established philosophical field. Still, since the advent of AI, authors from epistemology, the philosophy of science, and the philosophy of mind have addressed epistemological questions concerning AI. What is now called the “philosophy of AI” also touches upon epistemological questions about AI, but has traditionally been more focused on whether AI applications have mental states or properties. This article surveys and systematizes existing epistemological work on AI, covering symbolic and connectionist AI, and comparing machine learning with pre-programmed AI.

## 1. Introduction

### 1.1 Motivation for the epistemology of AI

In structural biology, predicting the three-dimensional shape of proteins (i.e., a class of molecules that perform various crucial functions in cells) represents a key challenge. Biologists compare their models’ abilities to make such predictions in a biannual competition (Dill & MacCallum 2012)[^dill-2012]. In 2018, AlphaFold, a deep learning model, won this competition. In 2020, AlphaFold 2, a new version of this model (Jumper et al. 2021)[^jumper-2021], “performed so mind-bogglingly well that it could herald a revolution in biology” (Callaway 2020, 203)[^callaway-2020]. In the meantime, AlphaFold 2 has predicted the structure of more than 200 million proteins, and comparisons with data indicate that a high fraction of the predictions is highly accurate (Varadi et al. 2024; Terwilliger et al. 2024)[^terwilliger-2024][^varadi-2024]. A successor model, AlphaFold 3, can predict the structure of a broader range of biological complexes (Abramson et al. 2024)[^abramson-2024].

This is but one example in which artificial intelligence (AI) has been successfully used to perform epistemic tasks (i.e., tasks related to rational belief, knowledge, and understanding). Given the track record of AlphaFold 2, it seems fair to say that we are justified in believing that its next prediction will be true, or at least an excellent approximation. Perhaps one could even say that AlphaFold 2 can provide an understanding of protein folding, or that it possesses such understanding.

Other examples in which AI successfully performs knowledge-related tasks abound. In medicine, so-called classifiers are used, which diagnose diseases on the basis of various types of data, such as X-ray images or magnetic resonance imaging (MRI) data (e.g., Hosny et al. 2018)[^hosny-2018]. In astrophysics, AI is used to detect and classify objects in telescope data (e.g., Hausen & Robertson 2020)[^hausen-2020]. Recently, Lemos et al. (2023, 1) presented “an approach for using machine learning to automatically discover the governing equations and unknown properties (in this case, masses) of real physical systems from observations.” Another AI application, AlphaGeometry, proves rather complicated theorems from Euclidean geometry (Trinh et al. 2024)[^trinh-2024]. In 2025, Deep Think, a development of Google’s large language model Gemini, reached the status of gold medalist (the highest distinction) at the International Mathematical Olympiads for pre-university students (Castelvecchi 2025)[^castelvecchi-2025]. And in 2026, OpenAI claimed that a system of 10’000 AI agents solved one of the millennium problems in mathematics by proving that the Navier-Stokes equations can break down due to a singularity, although disputes about the discovery remain (Castelvecchi 2026)[^castelvecchi-2026]. Last but not least, many people use ChatGPT and similar chatbots based on large language models (LLMs) to answer a wide range of questions. In all of these examples, AI systems produce outputs that many humans base their beliefs on. Thus, it is often tempting to claim knowledge based on AI outputs. The epistemic achievements of AI systems not only support humans but also enable robots, autonomous vehicles, and self-driving labs (Abolhasani & Kumacheva 2023)[^abolhasani-2023] to obtain the information required to fulfill their tasks. Arguably, AI is an epistemic technology because it is primarily used for epistemic purposes and operations (Alvarado 2023a)[^alvarado-2023a].

However, are we truly justified in believing things based on AI outputs? Is it rational to trust AI applications? Are we entitled to claim knowledge obtained from these applications? If so, what exactly is the source of the justification? Furthermore, is it possible that AI systems provide us with understanding?

These are questions for an epistemology of AI. Epistemology is the philosophical study of knowledge and related achievements, as well as their sources. Since terms such as “knowledge,” “(epistemic) justification,” and “(epistemic) rationality” are normative in that they have direct implications for what we ought to believe, epistemology is also normative to some extent. Consequently, it is part of philosophy and not only empirical science (though there are programs to naturalize epistemology).

### 1.2 Outline of the epistemology of AI

At present, the epistemic successes of AI are not (yet) fully understood. The performance of the recent wave of large language models has surprised many commentators, and even computer scientists struggle to understand why AI applications produce certain outputs for a given input, or why some AI models perform exceptionally well even when applied to new data. Accordingly, AI is often described as a black box and termed “opaque” (e.g., Burrell 2016)[^burrell-2016]. This problem has spurred research in computer science to make models more explainable or interpretable (see, e.g., Doshi-Velez and Kim 2017 [Other Internet Resources]). Notably, this research raises its own philosophical questions: What is the opacity of AI? What types of explanations are required to overcome it? In light of these questions, it seems advisable to include philosophical research on the opacity and explainability of AI in the epistemology of AI.

Accordingly, the epistemology of AI treats AI as having two roles: first, as an object of inquiry aimed at better knowing and understanding AI; second, as something on the side of the epistemic subject/agent (e.g., something that supports their inquiries, forms part of the subject, or even is a subject of its own).

Regarding the two-fold role of AI, the epistemology of AI and AI ethics resemble each other (see, e.g., the SEP entry on the ethics of AI, Müller 2025)[^müller-2025]. However, there is an important distinction between AI ethics and AI epistemology in relation to considering AI as an object: when ethicists treat an AI system as a mere object, they deny that it is a full moral agent who has moral duties, is accountable for its deeds, and possesses moral rights. By contrast, in epistemology, AI is considered an object if it is an object of inquiry, regardless of its status as an agent, and it counts as (part of the) subject if it is used to obtain knowledge and understanding.

In what follows, AI is understood broadly to encompass both symbolic AI, or “good old-fashioned AI” (GOFAI), and subsymbolic, connectionist AI. The current hype of AI is clearly due to connectionist artificial neural networks (ANNs), in particular deep neural networks (DNNs), which form the base for current large language models. ANNs are usually trained using, e.g., supervised or reinforcement learning, and thus follow the paradigm of machine learning (ML). However, in this entry, preprogrammed algorithms and GOFAI, in particular computer simulations (see, e.g., Winsberg & Alvarado 2026)[^winsberg-2026] count as AI, too. (See Bringsjord and Govindarajulu 2026 for a philosophical introduction to AI. For a short introduction to AI tailored to this entry, see the Supplementary Document at the end:AI and its Varieties from an Epistemological Perspective.)[^bringsjord-2026]

> [Supplementary Document: AI and Its Varieties From an Epistemological Perspective](epistemology-ai.supplement.md)

## 2. AI as an object of knowledge and understanding

### 2.1 Philosophical interest in the problem of opacity

Most work in the epistemology of AI as an object of knowledge is motivated by the diagnosis that many AI applications, particularly ANNs, are black boxes, opaque, or intransparent (e.g., Castelvecchi 2016; Ribeiro et al. 2016; Quinn et al. 2022)[^castelvecchi-2016][^quinn-2022][^ribeiro-2016]. As previously indicated, the rough idea is that humans have difficulties understanding AI. This is often considered problematic for various stakeholders and purposes. For instance, due to the opacity of AI, developers struggle to identify the causes of its malfunctions (Castelvecchi 2016)[^castelvecchi-2016]. The broader use of AI may be hindered because people who do not understand it and similarly believe that nobody else understands it may not trust it (see, e.g., Lipton 2018 for a discussion of this argument)[^lipton-2018]. To mitigate such problems, many authors have required AI models to be better understood or, using common buzzwords, to be transparent, explainable, or interpretable.

But what exactly is the problem with AI opacity? Why is it so difficult to understand the workings of AI, and which types of explanations may render AI more transparent? Over the last few years, epistemologists and philosophers of science have become interested in these questions. Ultimately, AI opacity implies that humans lack specific epistemic achievements concerning AI, and interpretability or explainability is closely connected to understanding and explanation, and thus key topics in epistemology and philosophy of science.

A natural entry point for philosophical work on the opacity of AI is the question of what opacity, explainability, and interpretability are. In a famous paper, computer scientist Zachary Lipton (2018) argued that interpretability and explainability are not well-defined: “[I]nterpretability is not a monolithic concept but several distinct ideas that must be disentangled before any progress can be made” (Lipton 2018, 4; cf. Carvalho et al. 2019, 10)[^carvalho-2019][^lipton-2018]. Lipton’s diagnosis invites a philosophical clarification using a definition or an explication. As it turns out, the question of how to define opacity and related concepts is connected to other questions considered below.

> Q1. Which aspects of opacity, explainability, and interpretability exist?
>
> Q2. Is there a fundamental source of the problems concerning opacity?
>
> Q3. What is the disvalue of opacity and the value of explainability or interpretability?
>
> Q4. What are promising routes to improve interpretability?
>
> Q5. What can we reasonably expect from interpretable AI?

### 2.2 Opacity, interpretability, explainability, and their aspects (Q1)

Let us first clarify the terminology. While transparency is often considered the opposite of opacity (e.g., Creel 2020)[^creel-2020], matters regarding explainability and interpretability are more complicated. The latter two terms are extensively used in the computer science literature to frame concrete ML research (e.g., Rudin et al. 2022)[^rudin-2022]. In particular, since the launch of the Explainable AI (XAI) program by the US Defense Advanced Research Projects Agency (Gunning & Aha 2019; Gunning et al. 2021)[^gunning-2019][^gunning-2021], the term “XAI” has become a buzzword (Arrieta et al. 2020, 83; cf. Molnar 2020, 419)[^arrieta-2020][^molnar-2020]. Accordingly, the terms “interpretability” and “explainability” are used to articulate practical solutions to reduce opacity or to mitigate its effects. Furthermore, some unavoidable opacity due to complexity is compatible with a significant degree of interpretability. Although some researchers treat “interpretability” and “explainability” as equivalent (Miller 2019, 8; Linardatos et al. 2020)[^linardatos-2020][^miller-2019], others (e.g., Rudin 2019)[^rudin-2019] distinguish between interpretability and explainability; for example, by taking interpretability to be a property of explanations (see Erasmus et al. 2021 for a philosophical proposal)[^erasmus-2021]. Still, in what follows, the notions of explainability and interpretability will be considered equivalent and addressed together with the concept of opacity.

Working scientists articulate the opacity of computer simulations as follows: “[I]t is not immediately obvious what is going on or why” (di Paolo et al. 2000, 497). Sociologist Jenna Burrell (2016, 1) notes that ML algorithms “are opaque in the sense that if one is a recipient of the output of the algorithm (the classiﬁcation decision), rarely does one have any concrete sense of how or why a particular classiﬁcation has been arrived at from inputs.” Thus, the general issue is that epistemic access to essential aspects of AI systems is challenging (Beisbart 2025b)[^beisbart-2025b]: humans face problems in knowing and understanding AI applications and their workings (where understanding is roughly the grasp of connections in one’s knowledge, Kvanvig 2003, 192)[^kvanvig-2003]. The problems arise because, first, most AI applications are highly complex; for instance, LLMs have billions of parameters (e.g., Mahapatra & Garain 2024 [Other Internet Resources], Table 3). Second, ML models apply rules that have not been defined by human researchers but were rather inferred from data. Third, even scientists lack informative higher-level descriptions of what the neurons in an ANN are doing. Notably, the opacity of AI does not extend to all its aspects. For instance, researchers typically understand the meaning of AI output. Additionally, programs can be printed and examined. However, this does not enable humans to anticipate AI outputs or understand what they are doing in a more qualitative manner.

Conversely, a model can be called explainable or interpretable if humans can, or do, know or understand its workings in crucial respects. The notion of understanding is indeed a natural candidate for a term that summarizes various aspects of the epistemic access to AI we may wish to have. Accordingly, Fleisher (2022) explicates transparency in terms of explanatory understanding (i.e., understanding why things are as they are), while Beisbart and Räz (2022) propose the even broader notion of objectual understanding to make sense of interpretability.

If opacity, explainability, and interpretability are understood that broadly, it is natural to distinguish between different aspects of these properties and classify them systematically (cf. Q1 above). A resulting framework may detail

1. the degrees to which epistemic access may be difficult,
2. the types of epistemic access that are difficult, and
3. the aspects of AI to which epistemic access is prohibited,

with points (a)–(c) being closely connected.

So far, a comprehensive classification of opacity’s facets remains missing; instead, philosophers offer distinctions that often mix dimensions (a)–(c) (see, e.g., Facchini & Termine 2022 and Buttaboni & Floridi 2026 for proposals)[^buttaboni-2026][^facchini-2022].

Regarding the degrees to which epistemic access is difficult (a), we can distinguish between

1. the in-principle impossibility of access to AI,
2. impossibility in practice (see Humphreys 2009 for the distinction between in principle and in practice)[^humphreys-2009],
3. mere difficulty of access, and
4. factual lack of access.

It has been observed that, in many respects, AI opacity is contingent on human practices and abilities. For instance, Burrell (2016) distinguishes between three forms of opacity, where the first two are contingent in this sense:

1. Agents such as companies do not disclose their algorithms and the parameter values of their models to protect their commercial interests.
2. Many humans cannot write and read computer code.
3. A mismatch exists between the mathematics underlying ML algorithms and how humans tend to describe reasoning.

The philosophical literature clearly focuses on the third form of opacity.

Regarding the types of epistemic access that are difficult (b), some authors list epistemic accomplishments that humans may wish to have regarding AI. Some accomplishments are merely matters of knowledge; for example, humans want to know whether a learning algorithm converges or what a particular part of the model does (Lipton 2018, 14)[^lipton-2018]. Other accomplishments relate to abilities constitutive of understanding, such as the ability to anticipate what would happen if model parameters were changed.

Regarding the different aspects to which epistemic access is hampered (c), it is useful to first distinguish between the training and application of the trained model in the case of ML; accordingly, Søgaard (2024) contrasts training opacity with inference opacity. Second, it is natural to articulate various aspects that are difficult to know or understand using questions such as “What did the model do and how does it do it?” Using these questions, Boge (2022) distinguishes between w(hat)- and h(ow)-opacity. Similarly, Zednik (2021) differentiates between “what,” “where,” “why,” and “how” questions to define a framework for thinking about explainable AI. He assigns the different types of questions to different stakeholders; for instance, people affected by AI decisions (so-called decision subjects) are most interested in “why” questions, e.g., “Why did the AI application reject my loan application?” (see Langer et al. 2021 for an empirical analysis of stakeholder interests related to explainability; cf. Preece et al. 2018 [Other Internet Resources])[^langer-2021]. Zednik further claims that the different questions and stakeholder interests can be addressed at different levels of description. He uses the distinction that Marr (1982) proposed for levels of cognition, namely the computational, algorithmic, and implementational levels (see Barberousse et al. 2009 for a slightly different definition of layers)[^barberousse-2009], and claims, for instance, that the “why” questions asked by decision subjects can be answered at the computational level. This approach assumes that the questions can be addressed at a specific level, which is difficult for ANNs. Note, too, that a classification of levels of description may be used independently of Zednik’s framework to distinguish the aspects of a model that humans may want to know. Depending on whether the questions relate to specific model outputs or the entire model, we can distinguish between local and global explainability (e.g., Erasmus et al. 2021)[^erasmus-2021].

### 2.3 Sources of opacity (Q2)

Philosophers studying AI opacity have not only attempted to distinguish among various facets of opacity but also to trace them back to one or a few fundamental sources. This is not only evident from Mann et al.’s (2023) taxonomy and Søgaard’s (2024) recent attempt to reduce the sources of opacity. Paul Humphreys’s famous philosophical explication of opacity can also be read as an attempt to pin down the basic source of opacity. It was first developed in the context of computer simulation but is also now applied to AI (e.g., Boge 2022)[^boge-2022]. The explication reads as follows:

> a process [here: the process in which a program is running on a computer] is epistemically opaque relative to a cognitive agent X at time t just in case X does not know at t all of the epistemically relevant elements of the process. (Humphreys 2009, 618; see also Humphreys 2004, 147–151)[^humphreys-2004][^humphreys-2009]

In this definition, opacity is agent-dependent and represents a factual lack of knowledge about the process. The agent- and time-dependence in the definition can be overcome by quantifying over agents and time (Boge & Grünke forthcoming). Humphreys calls the opacity essential if the lack of knowledge is necessary, given human nature. In any case, according to Humphreys, the problem is not that agents don’t know single elements of the process. Instead, the problem stems from the high complexity of the calculations, implying that too many relevant elements are unknown.

With its focus on complexity, Humphreys’s definition identifies an important obstacle to epistemic access to simulations and other AI. However, what is meant by knowledge of the “epistemically relevant elements” in the definition? In their clarification of opacity, Durán & Formanek (2018) regard the execution of a computer program as a justification or inference, and define epistemic opacity as the impossibility for an agent to check or survey the justification step by step. Opacity then coincides with so-called unsurveyability, an idea that has been used to articulate the fact that computer-aided proofs (e.g., of the Four Color Theorem) are unsurveyable because they cannot be “definitively checked by members of the mathematical community” in a reasonable time (Tymoczko 1979, 60)[^tymoczko-1979].

Understood in this manner, opacity is fairly precisely defined, yet narrow. It is doubtful whether all problems about epistemic access to simulations and other AI models are covered by it. Some authors (e.g., Imbert 2017 for computer simulation, Mann et al. 2023 for computer systems)[^imbert-2017][^mann-2023] distinguish several types or sources of opacity. Among these is the fact that large-scale computer simulations are typically developed by teams of experts from diverse backgrounds (Imbert 2017, 744)[^imbert-2017]. This makes computer simulations more difficult to understand, but it is independent of the large number of relevant elements. A more general objection is that Humphreys-style definitions miss the dimension of understanding and related inferential abilities (Beisbart 2021)[^beisbart-2021].

Regarding ML and ANNs in particular (which were not the focus of Humphreys’s work but are discussed, for instance, in Zednik 2021)[^zednik-2021], there are additional aspects that are difficult for us to access, e.g., the training data, which is not a process. Another aspect that escapes Humphreys’s definition is the fact that we currently lack informative higher-level descriptions of the inner workings of ANNs: It is challenging to describe the patterns of activations in artificial neurons using assumptions that refer to their target system (“in the air, pressure and temperature behave according to the ideal gas law”). What we can do is describe the structure of an ANN and list the mathematical functions that connect the neurons. However, these functions are not manifestly the functions that working scientists with domain knowledge use to describe the data, for example when calculating the momentum of a particle by multiplying its velocity by its mass. The operations of some ANNs are often described as mapping input data into latent spaces (see, e.g., Liu et al. 2019 for an overview)[^liu-2019], where objects have latent features that are used to achieve the epistemic tasks of interest. Other AI models, too, are known to construct new features from input features, for instance via principal component analysis. Since humans lack an understanding of the latent spaces, they cannot describe how features from these spaces are used to run inferences. In other words, they do not know the features to which the ANNs become sensitive. An additional difficulty stems from the fact that, in ANNs, objects or features need not be represented by a single neuron; instead, distributed representations exist , in which a set of neurons is used to represent a feature (Hinton 1984; Plate 2003)[^hinton-1984][^plate-2003]. Conversely, individual neurons can be polysemantic, i.e., they are activated by several distinct and unrelated features (Olah et al. 2020)[^olah-2020].

An analogous problem exists for human cognition (and to some extent for instruments such as microscopes): most humans do not fully understand how they know things (using instruments). This is particularly evident from tacit knowledge (Polanyi 1966; Collins 2010)[^collins-2010][^polanyi-1966]. For instance, we know that the person on the poster is Taylor Swift and that she looks friendly, but we cannot articulate an illuminating justification for this. More generally, a decent understanding of human perception is a fairly recent accomplishment, and we do not yet fully understand how human reasoning arises from neuronal activity—a challenge that also applies to AI. This suggests that we can know something even when the underlying processes are opaque to us.

### 2.4 Value of interpretability and explainability (Q3)

Why is the opacity of AI a problem, and why should researchers strive for interpretability? Krishnan (2020) has challenged the notion that there is a significant black box problem with AI. One reason for this is that interpretability is intended to serve multiple purposes, and many of these purposes can be achieved without it.

If the opacity of AI is a problem, the reason must be that knowledge or understanding of AI is valuable. To discuss the value of the explainability of AI (cf. Q3 above), it is helpful to distinguish between final and instrumental value. Knowledge and understanding are often considered to have final value (i.e., to be valuable for themselves). However, even if this is correct, the value of knowledge and understanding depends on their respective objects. Now, even though it seems valuable to know and understand AI in general, the same does not hold for all specific AI systems for which explainability is requested. Thus, the crucial question is which other goods are served by explainability.

One candidate for such a good is (epistemic) trust, with the main idea being that people trust AI only, or much more, if they understand AI to some measure (e.g., Lipton 2018)[^lipton-2018]. While the extent to which people trust AI is an empirical question, it is related to the normative question of when AI is trustworthy (see Section 3.4 below). Accordingly, philosophers investigate the extent to which transparency or interpretability is required to establish trust (see Section 3 below).

Knowledge and understanding of AI systems come with additional benefits (Lipton 2018)[^lipton-2018]: knowledge about an AI application helps us to

1. judge the extent to which it is generalizable and transferable to new applications, and
2. assess whether it is fair or exhibits any unacceptable bias (see Johnson 2020; Fazelpour & Danks 2021 for algorithmic bias)[^fazelpour-2021][^johnson-2020].

Explanations of AI also provide crucial information for

1. contextualizing and competently using its outcomes (cf. Rudin 2019; Hatherley et al. 2024)[^hatherley-2024][^rudin-2019].

Furthermore, transparency of AI applications is instrumental in

1. inferring causal connections in the real world and enhancing understanding of real-world phenomena.

The last point has recently become the focus of a philosophical debate about ML models that obtain classifications and predictions based on data. Sullivan (2022) argues that the limitations of existing ML models in providing understanding are not due to their opacity but instead stem from link uncertainty (i.e., the uncertainty about how the ML models relate to their target systems). One of Sullivan’s arguments is that knowledge about the implementation of a known function is useless for better understanding the target system. Furthermore, some current ML models (e.g., the Deep Patient Model) allow for some understanding of real-world phenomena, e.g., using so-called how-possibly explanations, which list factors that might have produced a specific outcome (see Knüsel & Baumberger 2020 and Jebeile et al. 2021 for case studies on how ML models can foster understanding)[^jebeile-2021][^knüsel-2020]. Critics have objected that Sullivan’s notion of understanding is too weak and that link uncertainty is usually reduced together with opacity (Räz & Beisbart 2022)[^beisbart-2022][^räz-2022][^räz-2022-2]. In any case, efforts to better understand an AI application can benefit scientific inquiry, e.g., by supporting the design of experiments to detect causes (Zednik & Boelsen 2022)[^zednik-2022].

While scientific research sets high standards for understanding, it is less clear that transparency carries significant weight in other areas. Medicine provides an interesting use case. Arguably, accuracy should be given priority over transparency because the natural comparison point for AI, human doctors are also often unable to explain judgments based on their tacit knowledge (London 2019)[^london-2019]. Additionally, medical knowledge is in part quite “superficial” because it lacks a theoretical or mechanistic basis; thus, using ML does not lower standards. However, it has been argued that AI’s opacity impedes patient-centered medicine (Bjerring & Busch 2020)[^bjerring-2020]. Moreover, higher accuracy doesn’t necessarily translate into better patient outcomes in realistic settings, and a better understanding of the AI models may help human doctors to use it more successfully (Hatherley et al. 2024)[^hatherley-2024]. Finally, the claim that there is a completely general trade-off between accuracy and interpretability has been disputed (Rudin 2019)[^rudin-2019]: more transparent classifiers need not be less accurate. Even if this is true, however, enhancing explainability comes at a cost, e.g., increased computational resources.

If interpretability has several aspects, as suggested above, there is no single question about its value (Lipton 2018; Krishnan 2020)[^krishnan-2020][^lipton-2018]. Instead, the values of various aspects of interpretability must be elucidated in a more piecemeal manner. To achieve this, a promising approach could be to formulate concrete desiderata for explainability in specific contexts and infer the type of interpretability required. In this vein, Holm (2026) argues that the justified use of AI in medical diagnosis requires explanations for why a particular diagnosis has been produced. By contrast, a mechanistic understanding of AI does not seem necessary in medical practice, because many drugs and therapies also lack mechanistic understanding, and evidence-based medicine gives mechanistic understanding a relatively minor role (London 2019; McCoy et al. 2022)[^london-2019][^mccoy-2022]. Arguments of this type often require empirical support; for instance, if more explainable AI is expected to engender trust, surveys can be conducted to determine which types of explanations lead to such trust (e.g., Tonekaboni et al., 2019)[^tonekaboni-2019].

### 2.5. Routes to greater interpretability (Q4)

As previously noted, one strand of current research in computer science aims to make AI more interpretable or explainable (see Adadi & Berrada 2018 and Hassija et al. 2024 for overviews)[^adadi-2018][^hassija-2024]. Epistemologists of AI can help classify the relevant approaches, discuss their potential, and thus contribute to their critical evaluation.

From a practical perspective, approaches that make existing AI post hoc more understandable must be distinguished from approaches that attempt to build AI that is understandable from the very beginning (note, however, that the term “post hoc” is not always used to make this distinction; e.g., Lipton 2018)[^lipton-2018]. We can, furthermore, distinguish between model-specific methods and model-agnostic methods which can be applied to all AI models (e.g., Linardatos et al. 2020)[^linardatos-2020]. Finally, the methods may be distinguished by their purposes and the aspects of interpretability they address.

Well-known techniques to make trained ML models more understandable include *second-order models*, i.e., additional models used to represent the workings of an ML model. One famous approach is known as *local interpretable model-agnostic explanations* (LIME; Ribeiro et al. 2016)[^ribeiro-2016]. The idea is to fit a simple model (e.g., a decision tree or a linear model) to the outputs of the ML model (see Garreau & von Luxburg 2020 for an evaluation)[^garreau-2020]. A slightly different method uses so-called *anchors* to make a model more understandable: simple if-then rules or sufficient conditions for classification are searched to predict the model’s behavior with high probability (Ribeiro et al. 2018)[^ribeiro-2018]. Another popular approach is *saliency maps* (Simonyan et al. 2014 [Other Internet Resources]). Given an input image and its corresponding output, a saliency map shows how critical each pixel of the input image was to that output. In a more general setting, it is investigated how sensitive the output is to specific changes of input characteristics (*sensitivity analysis*; Samek et al. 2017 [Other Internet Resources]). Rather than modifying the input, researchers can also intervene on a model’s internal components to gain a better understanding of its operations.

Using models to provide post-hoc explanations has become a matter of debate. Computer scientist Cynthia Rudin (2019) has cautioned against simplifying and idealized models because they may miss the real causes of the model behavior. By contrast, Andrés Páez (2019) has argued that true scientific explanations of AI systems and their outputs are not available to humans. This skeptical point does not exclude a more pragmatic form of understanding, which need not be factive (i.e., fully faithful to the AI model; see Zerilli 2022)[^zerilli-2022]. It may also be argued that scientists make progress with highly idealized models, which can only provide a non-factive understanding (Páez 2019)[^páez-2019]. However, even if models used for post-hoc explainability parallel scientific models, they may fail to satisfy the demands of users because explanations based on such models lack important features that everyday examples of explanations have, such as being *contrastive* (i.e., outlining why X rather than Y occurred), *selective* (i.e., focusing on the most salient causes), and *social* (i.e., being a social practice, Mittelstadt et al. 2019; see also Miller 2019)[^miller-2019][^mittelstadt-2019].

In the philosophy of science, model-based explanations represent only one form of explanation. So to what extent can other types of explanations, e.g., causal (Beckers 2022; Baron 2023)[^baron-2023][^beckers-2022] or statistical ones (Räz 2022)[^räz-2022][^räz-2022-2], be usefully applied to AI and satisfy the demands of explainability arising in various contexts? In the last few years, there has been a surge of interest in mechanistic interpretability, which aims to provide an understanding of how an ANN functions at the algorithmic level (Bereska & Gavves 2024 [Other Internet Resources]; see Millière & Buckner 2024b [Other Internet Resources] for its application to LMMs). This understanding may be obtained using causal abstraction (Geiger et al. 2021; Geiger et al. 2025)[^geiger-2025][^geiger-2021]: an ANN’s neurons are partitioned into groups, each of which is represented by a single variable in a simpler higher-order causal model. Researchers also intervene on ANNs to approach mechanistic interpretability; in the simplest case, they use ablations and deactivate specific neurons to study their effects on the outputs (Geiger et al. 2025)[^geiger-2025]. Mechanistic interpretability seems particularly important for improving ANNs and contrasts with propositional interpretability, which ascribes desires and beliefs to AI systems. Notably, propositional interpretability does not presuppose that AI can have desires and beliefs; instead, it can be considered to adopt the intentional stance (Dennett 1987)[^dennett-1987]. Zerilli (2022) and Chalmers (2025 [Other Internet Resources]) argue that propositional interpretability is sufficient for the demands of decision subjects because decisions made by humans are usually explained and justified on the same level.

### 2.6 Expectations about interpretability (Q5)

The extent to which various types of explanations yield understanding suitable for a task also depends on the broader expectations we have for interpretability (cf. Q5). In this context, a central issue stems from the suspicion that interpretability is subjective: what is interpretable to one person may not be to someone else (cf. Lipton 2018, 13; cf. Miller 2019)[^lipton-2018][^miller-2019]. This arouses fear that there are no objective standards for interpretable AI. However, philosophers have argued that interpretability can have subjective aspects without compromising objective scientific research (for a discussion on the subjectivity and objectivity of explanations, see e.g., Friedman 1974; van Fraassen 1980, chs. 4–5; de Regt 2017)[^regt-2017][^friedman-1974][^fraassen-1980]. To see this, it is first necessary to decouple understanding from the sense of understanding—if an explanation feels right, this often does not reliably indicate real understanding (Trout 2002)[^trout-2002]. Focusing on abilities that concern the AI application (e.g., answering questions about the AI) helps abstract from feelings that vary across people. Second, understanding in a broad sense allows for some subjectivity since different people are interested in different questions (as Zednik 2021 suggests)[^zednik-2021] and set different desiderata on the answers (see Watson & Floridi 2021)[^watson-2021]. This is not problematic if there are objectively correct answers to each question and if it is a matter of fact which explanations best satisfy specific desiderata.

## 3. Contribution of AI to knowledge

If AI is an interesting object of knowledge and understanding, this is largely due to its applications, particularly for epistemic purposes. The questions of to what extent, why, and how AI can contribute to knowledge and understanding form the second part of the epistemology of AI. In this section, the focus is on knowledge.

### 3.1 Preliminaries

Suppose an AI system yields a specific output, such as a label for a class (e.g., dog), the numerical value of a variable (e.g., the temperature at some place and time in degrees Celsius), or an answer to a question (e.g., that magnesium is a metal). Based on such outputs, a human user may form a belief in a proposition *p* (e.g., that an image shows a dog, that the temperature is 5 degrees Celsius, or that magnesium is a metal). A crucial epistemological question, then, is whether, or under what conditions, the human knows *p* to be the case. Of course, AI may also be used for heuristic purposes only (see, e.g., Duede 2023 and Wang et al. 2023)[^duede-2023][^wang-2023], but then questions about knowledge do not arise. Furthermore, AI, particularly LLMs, may also be used for knowledge production in a more interactive way, e.g., when humans interrogate LLMs to examine the credibility of a claim, but such AI uses are still developing and best analyzed once we’ve understood the setting in which AI yields a single output.

Users must typically interpret an AI system’s output to obtain a proposition that may then become the subject of their knowledge (Iizuka 2024)[^iizuka-2024]. This is even the case when a chatbot outputs a sentence, because the reference of indexicals must be fixed, for example. Often, several interpretations are possible. For instance, if an ANN yields “dachshund” in response to an image, this may be translated into a proposition about the image (“This photo shows a dachshund”) or about a specific event represented by the image (“There was a dachshund in the concert hall”). In the epistemology of AI, it is often useful to focus on interpretations based on minimal prior knowledge, because this helps isolate the AI system’s contribution. However, this strategy is not sensible for queries addressed to LLMs. Prompts asking a question do not provide data that can represent the world as images do. Thus, the most natural candidate for a proposition that the user may believe is the LLM’s answer in some literal interpretation (see Heersmink et al. 2024 for a general epistemological analysis of LLMs)[^heersmink-2024].

Often, things are more complicated than in the simple setting just sketched. Some algorithms yield a probability distribution over the values of the variable of interest. In other cases, it is clear that the output does not provide a literally true description of a target system; thus, users are only interested in the accuracy of the output, i.e., its closeness to the truth, where the tolerated margin of error depends on the users’ purposes. For this reason, it has been claimed that the purpose of assessing computer models is to show accuracy, not literal truth (cf., e.g., Beisbart 2019a)[^beisbart-2019a]. Other authors, such as Parker (2020), suggest that adequacy of purpose is the proper standard for computer models and their output. However, all of these complications can be considered within the confines of the simple setting described above by re-interpreting the proposition *p*, for example, by stating that a certain probability takes a specific value or that the true temperature is near the output of an AI model.

Whether the human agent knows *p* in the simple setting depends on whether they believe *p* and whether *p* is true, and thus on contingent matters that do not require epistemological analysis. The crucial epistemological question is only whether the user has sufficient justification to believe *p*, or whether an alternative remaining condition of knowledge is fulfilled, such as whether epistemic luck is excluded, whether there is an appropriate causal connection between *p* and the AI-based belief (Goldman 1967)[^goldman-1967], whether belief formation based on the AI tool forms a reliable process (e.g., Goldman 1976)[^goldman-1976], or whether AI-based belief is sensitive or safe (e.g., Gardiner & Zaharatos 2022)[^gardiner-2022]. For simplicity, this entry will focus on whether the belief is justified. This still leaves room to discuss internalist and externalist accounts of justification (see Hila 2025 for a related discussion of LLMs)[^hila-2025].

A natural strategy to answer the question about justification is to draw on familiar models of knowledge acquisition. One candidate is testimonial knowledge, where humans expand their knowledge by believing what other humans know, believe, or assert. From a phenomenological perspective, conversations with chatbots feel very similar to conversations with humans (Heersmink et al. 2024)[^heersmink-2024]. However, many authors suggest that AI systems do not know, believe, or assert anything (Fricker 2025; Herrmann & Levinstein 2024; see Butlin & Viebahn 2025 for assertions and Green & Michel 2022 for a more general discussion on AI and speech acts)[^butlin-2025][^fricker-2025][^green-2022][^herrmann-2024], implying that familiar models of testimonial knowledge do not apply to AI (but see Freiman 2024 and He & Yang 2025 for attempts to provide conditions on something like AI testimony)[^freiman-2024].

A more plausible idea is that AI systems are—or share their epistemic status with—instruments. For sure, many AI systems differ from measurement devices because they do not produce data by causally interacting with a real-world system; instead, they process information obtained through other means (Duede 2022)[^duede-2022]. Furthermore, conversational AI outputs words or sentences, whereas measurement devices output variable values. Still, AI systems that provide classifications and computer simulations are not far from pocket calculators, and computer simulations have also occasionally been called instruments (e.g., Parker 2010; Alvarado 2022)[^alvarado-2022][^parker-2010]. Freiman (2024) denies that chatbots are instruments, but his argument is focused on language-processing AI and does not generalize to other AI systems.

This suggests that the epistemology of some AI systems can be reduced to that of instruments (cf. Grindrod 2025)[^grindrod-2025]. However, this does not help much because the epistemology of instruments is underdeveloped (but see Baird 2004; Neges 2018)[^baird-2004][^neges-2018]. For many reliabilists, such as Goldman (1976), the workings of instruments cannot belong to the reliable process required for knowledge or justification (see Goldberg 2012 for discussion; see also Sosa 2006; cf. see also the discussion of computational reliabilism below in Section 3.2)[^goldberg-2012][^sosa-2006]. Instead, the question is whether the practice of forming a belief based on an instrument’s output constitutes a reliable process (cf. Fricker 2016)[^fricker-2016]. Still, this reliability condition is only satisfied if the instrument is reliable in the sense that it yields the truth with high probability across a range of cases (Sosa 2006)[^sosa-2006]. For internalists, the human subject must have reasons that justify believing in the instruments.

What, then, might be the justification for believing that *p* based on AI output? In some cases, the user can easily check whether *p* is true, for instance, by verifying that multiplying the factors identified in a factorization yields the correct result. However, in many other examples, an independent check is impossible. An alternative justification for belief in *p* may be grounded in a close understanding of what the AI application has done. However, the opacity of many AI systems prevents this; in particular, it is practically impossible to inspect the operations performed by an AI device manually.

### 3.2 Justifying AI results: Basics

Meanwhile, the justification for believing results from pre-programmed GOFAI is well understood. For instance, the justification of computer simulation results (often called their validation) draws on several sources (see, e.g., Winsberg 1999 and 2001; Winsberg & Alvardo 2026, Sect. 2.2; Oberkampf & Roy 2010)[^oberkampf-2010][^winsberg-1999][^winsberg-2001][^winsberg-2026]. One source is the fit between the simulation results and data from the target system, if available. Many simulations gain additional credibility by being built on assumptions that form prior knowledge, often as part of a theory. However, in many simulations, the equations from theories are only approximated, using, e.g., discretization techniques. Accordingly, scientists have to “verify” their simulations to control that the simulations approximate the solutions to the original equations.

To justify their simulation results in practice, scientists try to exclude or control various types of errors, such as modeling errors (the conceptual model underlying the simulations is wrong), round-off errors, discretization errors, and errors due to hardware failure (Parker 2008a and 2008b)[^parker-2008a][^parker-2008b]. Often, there are also indirect reasons to believe the results of a simulation. For instance, the simulation was built by a team that knows the relevant tricks of the trade and principles for reliable simulation-building (Winsberg 2009)[^winsberg-2009]. Simulation results are also more credible when they are robust, i.e., when the results from several simulation runs or independent models agree (e.g., Muldoon 2007; Parker 2011)[^muldoon-2007][^parker-2011].

All in all, philosophers agree with scientists that simulation results can be justified, even though simulations are opaque in Humphreys’s sense (2004). This point has been stressed by “computational reliabilists” (Durán & Formanek 2018)[^durán-2018]. A direct application of reliabilism to computer simulations would imply that a user is justified in believing the results of a specific simulation program if taking the results of this program to be true is a reliable process of belief formation; that is, if a high proportion of the simulation results in a specific domain of applications is true or sufficiently accurate. However, computational reliabilism, as defined by Durán and Formanek, deviates from standard reliabilism by requiring the user to have evidence of the process’s reliability (e.g., from validation). Importantly, this evidence is available despite a simulation’s opacity.

When we turn away from computer simulation, and thus a form of pre-programmed GOFAI, things change (*pace* Durán & Jongsma 2021, who extend computational reliabilism to ML without significant modifications)[^durán-2021]. As an example, consider ANNs trained using supervised learning. The justification of their results cannot draw on prior knowledge of the assumptions built into the model. This is not because ANNs make no assumptions; rather, typical users do not know which assumptions ANNs make unless they have deeper knowledge of the ANN.

As a consequence, the verification known from computer simulations is no longer an issue: Since humans do not implement substantive assumptions about their targets in ANNs, the question of whether such assumptions are appropriately implemented doesn’t arise. There have been attempts to verify that learned ML models satisfy specific safety properties, such as robustness to specific input perturbations. However, research in this direction has not yet advanced very far; for instance, so-called “complete methods” for ANNs can only be applied to small networks in practice (Urban & Miné 2021 [Other Internet Resources]; Krichen et al. 2022)[^krichen-2022]. Therefore, the justification of ANN results must primarily draw on experience with the device (i.e., its track record) and be based solely on “familiarity or involvement with objects and data” (Schubbach 2019, 1825)[^schubbach-2019].

More specifically, the justification can refer to the facts (a) that the ANN has been optimized to reproduce known truths and (b) that it has been tested on other data, as is typically done. For instance, in supervised learning, the available data is randomly split into training and test sets. The ANN is first optimized using the training data and then tested using the test data. Accordingly, the justification of ANN results can be roughly reconstructed using an enumerative induction or a statistical inference: If the ANN has yielded accurate results for a large proportion (or a specific fraction) of a range of inputs (partly by design, partly in a test), it will thus also yield accurate results for other inputs (with a certain probability). Section 3.3.3, which describes ML as inductive inference in more detail, will expand on this perspective.

### 3.3 Justifying ML results: More specific accounts

Thus far, our discussion on justifying ML (machine learning) results has used ANNs (artificial neural networks) as examples and assumed that ML models are highly opaque to users. However, there are several distinct types of ML models, and, at least in some cases, researchers have insights into how the models work or background knowledge of their use cases. This facilitates more informative descriptions of ML models, which can lead to more telling justifications for their results and a better understanding of how ML can help gain knowledge. In what follows, more specific descriptions of (some classes of) ML models will be considered together with the consequences for justification. Note that the descriptions can focus on the learning phase and/or the application of the trained model.

#### 3.3.1 ML models as models

The term “ML model” suggests that ML applications constitute models. This paves the way for a more detailed account of ML, as we can draw on the literature on modeling. The first point to clarify is to which class of models ML models belong. Here, we bracket the learning phase (which may be considered a model of human learning; cf. Buckner 2019; Lefrançois 2020, Ch. 11)[^buckner-2019][^lefrançois-2020] and focus on the learned model.

Some ANNs may be considered *computational models of parts of a brain* (Boge 2022, Sec. 2.1)[^boge-2022]. However, many ANNs, as well as other ML models, are quite dissimilar from parts of the human brain (see Watson 2019 for differences between the workings of ANNs and human cognition)[^watson-2019]. Also, thinking of ML models in this manner is not very productive unless we know more about how the brain works, and this knowledge is not independent of ML models .

Since ML models have been inferred from data, they may seem to be *data models/models of data* or something close (Boge 2022, Sec. 2.1; see Suppes 1962 for a classic source and Castillo Brache & Bokulich 2024 for a recent overview of data models)[^boge-2022][^castillo-2024][^suppes-1962]. Data models arise from applying data-processing techniques such as data cleaning, data conversion, and data correction. If data models are still data, then ML models are not in general such models because they do not output purified versions of the data. However, if data models can also arise from curve fitting or data binning, as is sometimes assumed (e.g., Harris 2003)[^harris-2003], then many ML models are data models. For instance, ML-based decision trees and clustering algorithms assign data points or items represented by them to groups, which is similar to data binning. An ANN classifier can also be considered a data model interpolating a function mediating between input data and labels.

Considered as data models, trained ML models stand out as being particularly complex because they have many parameters. This differs from simple data models, which fit known analytical functions (e.g., a Gaussian distribution) to some data. Consequently, trained ANNs (and other ML models) are selected from huge spaces of models. They can thus be fine-tuned to fit the training data much better than simpler models. Notably, however, the model ultimately selected through training depends significantly on the choice of optimization method and the so-called loss function. Accordingly, each trained ML model provides a unique perspective on the data.

The massive number of parameters in trained ML models may give rise to the concern that such models overfit the data: Due to their high number of parameters, the models match the training data with high accuracy (meaning low bias in statistical terms), taking noise in the data too seriously and failing to make accurate classifications for new data (high variance; see e.g., Prince 2023, Ch. 8 for technical details; a useful overview is given by Buckner 2019, 8)[^buckner-2019][^prince-2023]. It has been confirmed that ML models can overfit and effectively learn random labels (Zhang et al. 2017 [2021]. However, there are strategies to avoid overfitting, such as regularization techniques. In a narrow sense, regularization changes the optimization problem underlying learning by adding a term to the loss function: higher model complexity yields more loss. In a broader sense, regularization comprises other techniques (Prince 2023, Ch. 9; Tian & Zhang 2022)[^prince-2023][^tian-2022]. For instance, under “early stopping”, training is stopped when further training is not expected to improve model performance. In a strategy called “dropout,” some ANN nodes are deactivated so that the number of model parameters is reduced. Over the last few years, it has also been observed that, for a large class of tasks and models, overfitting automatically disappears if the number of parameters exceeds a certain threshold. The resulting phenomenon is known as “double descent” (Belkin et al. 2019; Nakkiran et al. 2021)[^belkin-2019][^nakkiran-2021]: whereas models first improve as more parameters are added (“first descent”), the trend reverses after the so-called “sweet spot,” and overfitting sets in, leading to performance deterioration. The problem at this point is that the model has so many parameters that it can interpolate the data, implying that each data point is reproduced with zero deviation. Later, however, as models become even larger, they can select among alternative interpolations, thereby improving model performance again (second descent). Accordingly, some ML models can be considered “big models” that avoid overfitting.

It is also possible to conceptualize ML models not as data models but as *representational models of phenomena* described by their inputs and outputs. Although this is difficult under a similarity view of models (Sullivan 2023; see, e.g., Weisberg 2013 for the similarity view)[^weisberg-2013], it works adequately from an inferentialist perspective (Suárez 2004)[^suárez-2004]. As required by inferentialism about models, an ML model allows scientists to infer information about a target system. More specifically, ML models may be considered mathematical models (i.e., as sets of mathematical equations) because the dependence of the output on the input can be cast as equation that approximates the relationships between variables in the natural world. Recently, Sullivan (2024) has proposed that ML models function similarly to toy models (extremely simple models, often exemplifying a type of mechanism; see Frigg & Hartmann 2026, Section 1)[^frigg-2026] because they involve heavy idealizations.

Within the class of representational models, ML models are unique because the “inference machines” or mathematical equations have been “learned” from the data. This is a marked difference from other models. Since these other models have been designed by humans, they contain assumptions that humans can understand, such as the laws of nature or descriptions of mechanisms that can help explain phenomena in the target system. It may well be that ML models also contain such assumptions; however, whether this is true will remain unknown until the black box is opened.

Regarding LLMs, it is clear that they contain a model of a language or a specific form of discourse that is encoded in the training data. However, it is debatable whether LLMs also contain world models (i.e., models that represent parts of the world). This is plausible if they can answer questions not addressed in the training data or if specific groups of neurons can be shown to trace certain real-world features (see Millière & Buckner 2024a, 2024b [Other Internet Resources] for a discussion).

#### 3.3.2 Abstraction

When ANNs identify specific types of objects in images, we can say that they apply concepts to the input. To do this, they must abstract from many aspects of the image content, and, *qua* ML models, must have learned to do this. Thus, one way to characterize the epistemic work performed by ML models is to say that they engage in abstraction. But how exactly do they do this?

Cameron Buckner (2018; see also Buckner 2023, Ch. 3)[^buckner-2023] has proposed to answer this question for certain types of ANNs using transformational abstraction: an image is repeatedly transformed by mapping it into simpler feature spaces. These spaces are spanned by properties that increasingly suppress irrelevant information contained in nuisance parameters (e.g., the angle from which a chair is observed). In a deep convolutional neural network, one step in this direction is achieved by two consecutive layers. The first layer is composed of convolutional nodes that identify line segments with a specific orientation, for example. Thus, the output of each convolutional node encodes the degree to which a certain region of the image contains a line segment with a specific orientation. The next layer of neurons applies max-pooling (i.e., the maximum activation across a few convolutional nodes is computed). Thus, the outputs of max-pooling only encode the extent to which a line segment exists in the region at all, whereas information about orientation has been suppressed. Buckner argues that such networks learn to engage in transformational abstraction by constructing a sequence of feature spaces such that the objects of interest (chairs, etc.) correspond to optimally separated regions in the very last feature space.

Buckner focuses on supervised learning and on a form of abstraction related to perception. Unsupervised learning methods can also be considered to engage in a form of abstraction (Watson 2023)[^watson-2023]. For instance, when a decision tree is created based on information about certain variables, categories and subcategories are constructed to assign data to an increasing number of abstract classes. In fact, every data analysis technique that reduces the amount of information contained in the data can be viewed as an abstraction. Thus, beliefs based on specific ML models may be justified by saying that they categorize data or items into concepts that have been optimally abstracted from data.

#### 3.3.3 Inferences

In many ML applications, such as when ML models make predictions, it is natural to say that they perform inference. But how may this inference be characterized?

Computer proofs of mathematical results can be regarded as deductive arguments (Tymoczko 1979; McEvoy 2008)[^mcevoy-2008][^tymoczko-1979]. For computer simulations, the inference has also been reconstructed as a deductive argument, where the premises comprise the input (reconstructed as propositions) and the model assumptions made by the simulation (typically dynamical equations), while the conclusion is the output, translated into a proposition once more (Beisbart 2012; cf. Bueno 2014)[^beisbart-2012][^bueno-2014]. Since many computer simulations do not evaluate the model with which scientists start but rather approximations, the model-based premises articulate this approximate model (also known as the “computerized model”; Schlesinger et al.1979)[^schlesinger-1979].

Although the workings of a trained ML model can also be considered to derive consequences from a model, a more helpful reconstruction additionally covers the training. In supervised learning, the labeled training data can be reconstructed as a set of premises that describe items using their labels. The conclusion is a general hypothesis stating that inputs are mapped to outputs using a specific function. This inference is inductive (not deductively valid) since the inferred function is not included in the training data. From the perspective of induction, implementing induction on a computer can be embedded in long-standing efforts to formalize and “mechanize” induction (see Ortner & Leitgeb 2011 for the latter)[^ortner-2011]; hence, problems about induction (e.g., Henderson 2024)[^henderson-2024] resurface in the context of ML (Lauc 2020; Li 2023)[^lauc-2020].

Since the inference just indicated involves premises about many items, the learning may be said to run an enumerative induction over the items. However, this is not precisely what is occurring. In enumerative induction, the premises characterize the items in the same way (e.g., ravens as being black), whereas ML models have been trained on inputs mapped to different labels. A more adequate way of describing the inference is that some correlations between variables are identified. Buchholz and Raidl (2025) go so far as to argue that hypotheses are rejected during training, as suggested by falsificationist methodology (see also Gillies 1996)[^gillies-1996]. Still, if the learned model is supported by the training data, the support is inductive: the trained model is compatible with, or best fitted to, the training data (Mitchell 1997, 23; Li 2023)[^mitchell-1997]. As mentioned in Section 3.1, learned models are tested using additional test data, with the fit between the model and test data adding to the inductive justification of the model.

The resulting inductive justification can be characterized statistically when the training and test data are random samples from an underlying distribution (cf. Corfield 2010)[^corfield-2010]. To see this, it is helpful to draw on statistical learning theory (Vapnik 2000)[^vapnik-2000], a formal framework that lends itself to computer implementation (e.g., Steel 2010; Schurz 2019)[^schurz-2019][^steel-2010]. In a standard setting investigated in statistical learning theory (Vapnik 2000)[^vapnik-2000], a generator produces items, each characterized by features (e.g., height and weight). Accordingly, each item can be represented as a vector **x** = (x₁, x₂, … ); e.g., an item with a height of 3 and a weight of 4 (in suitable units) is represented as (3, 4). A supervisor assigns each item another feature y (e.g., its stability). The work of the generator is described as independently choosing from the same fixed probability distribution over the features, P(**x**); likewise, the work of the supervisor is described using a conditional probability distribution, Q(y|**x**). Both probability distributions are unknown, and the task of learning is to predict the supervisor’s reaction given a finite set of data (**x**, y). In mathematical terms, a function f is sought that maps points in the feature space used by the generator into features used by the supervisor: f: **x**→y. The challenge is to minimize the expected loss, known as the risk functional. The latter can be estimated based on finite data (**x**, y) using the so-called empirical risk.

In this setting, the model’s ability to perform well on test data not used for training but drawn from the same distribution is called generalizability, and many ML models generalize well. In statistical learning theory, statistical estimates of the errors or bounds on the errors can be derived (Corfield 2010; Grote et al. 2024)[^corfield-2010][^grote-2024]. However, particularly for ANNs, the relevant results are often not very useful for current ML research, and the generalization properties of ANNs are still not fully understood (Zhang et al. 2017 [2021]; Grote et al. 2024)[^grote-2024][^zhang-2017].

Things become more difficult when the training data are not known to provide a random sample of a fixed distribution of interest, particularly when an ML model is applied to data from a different distribution. For instance, medical doctors may be interested in applying a medical diagnosis tool trained on Swiss data to populations in other countries. Such ML applications lead to out-of-distribution errors. If these errors are small, a model is often called (distributionally) robust (Freiesleben & Grote 2023)[^freiesleben-2023]. A model may produce small out-of-distribution errors if the new data are similar to the data used for training and testing, an idea that is used in transfer learning (see Weiss et al. 2016; Niu et al. 2021)[^niu-2021][^weiss-2016].

The philosophical literature on induction (see Henderson 2024 for an overview)[^henderson-2024] suggests that enumerative induction may even be justified if it is not based on a random sample from the target population. It is justified when the training data trace exemplars of the same natural kind (cf. Ellis 1998; Mizrahi 2013)[^ellis-1998][^mizrahi-2013], when the inference is based on the best explanation of the observed regular pattern that extends to new data (Harman 1965; see Mitchell et al. 1986 for an explanation-based account of generalization)[^harman-1965][^mitchell-1986], when it is underwritten by suitable facts (Norton 2021; see Spelda & Stritecky 2024 for an application to ML)[^norton-2021][^spelda-2024], or when the learning process is in a well-defined sense close to optimal (Corfield 2010)[^corfield-2010]. However, these conditions are not easily fulfilled in ML. The natural-kind condition is not satisfied in most ANN applications because the data does not (only) trace the properties of a natural kind. Nor is Harman’s explanation condition often satisfied: when ANNs work well, researchers often lack an explanation for this. Echoing Schubbach (2019), we can state that the justification of ANN results is “blind” and does not rely on an explanation of how the results have been obtained. In the spirit of the material theory of induction, it has been suggested that ML models should be grounded in suitable domain knowledge or well-established ontologies (Kulmanov et al. 2021; Li 2023)[^kulmanov-2021]. This requirement is violated for some ANNs, as so-called adversarial examples illustrate: input images that an ML model correctly classifies can be altered in ways that are imperceptible to humans yet distort the model’s classification (Szegedy 2013 [Other Internet Resources]; Goodfellow et al. 2014 [Other Internet Resources]).

Sometimes, ML-based inference can be characterized more strongly: ML engages in causal inference or variational induction (Pietsch 2016 and 2021)[^pietsch-2016][^pietsch-2021]. This is trivially true of ML models that aim to infer causal Bayesian networks (Buijsman 2023; Pearl 2009, Sec. 2.1)[^buijsman-2023][^pearl-2009], but may also hold for other models since training confronts ML models with not only positive instances of a target property. Rather, a successful classifier learns which types of properties in the input make a difference to the label. Accordingly, if the so-called homogeneity condition is fulfilled, Mill’s method of difference for identifying causes is applied. However, the homogeneity condition is often not fulfilled because variations in the value of an input variable may correlate with other aspects of the target system that are not manifested in the input data (see Harris & Dunham 2021 for a different perspective on ML and causal inference)[^harris-2021].

#### 3.3.4 Memory

The acquisition of human knowledge is also supported by memory. Here, memory is not just the ability to retain information, which has an obvious counterpart in computer memory. Rather, memory selects and integrates information obtained via perception and other means. To some extent, ML models can achieve this, too: Buckner (2023, Ch. 4) recently brought together philosophical accounts of memory and deep learning. The difficulties in effectively imitating human memory can be illustrated by “catastrophic interference” or “catastrophic forgetting” (French 1999)[^french-1999]. When some ML models were first trained on one task, and then on another, they forgot how to solve the first task. By contrast, humans typically remember the first task. Buckner discusses how the challenge can be addressed using ANNs with two modules for short- and long-term memory, respectively (see Kirkpatrick et al. 2017 for computer science solutions)[^kirkpatrick-2017].

Similarly, Buckner (2023, Ch. 5) discusses philosophical accounts of imagination in view of recent advances in generative AI. Accordingly, if AI can be shown to memorize information or imagine scenarios, this may help us construct more informative accounts of the justification of AI output. Note that imagination is also relevant when AI is used more interactively, e.g., to support brain-storming.

### 3.4 Trust and other attitudes

The question of whether we should believe things based on AI outputs is naturally rephrased as asking whether we should trust AI. Thus, it is no surprise that a growing body of literature on trust in AI and AI trustworthiness has asked questions of the following kind: do AI models represent types of entities we can (fully) trust (Ryan 2020; Ferrario et al. 2021; Starke et al. 2021)[^ferrario-2021][^ryan-2020][^starke-2021]? Under which circumstances should we trust AI models (Durán & Jongsma 2021)[^durán-2021]? What kind of explainability can help increase trust in AI (Baron 2025)[^baron-2025]?

However, only some parts of this literature are relevant to epistemology (cf. Alvarado 2023b)[^alvarado-2023b]. Trust is only a topic in epistemology if it is *epistemic* trust—trust that a trustee knows something or tells the truth (see Dormandy 2019 for a collection on epistemic trust)[^dormandy-2019]. Epistemic trust is at most appropriate vis-à-vis an AI system if the latter makes truth-apt claims. AI systems that make decisions cannot be epistemically trusted; trusting such systems means expecting that they make good decisions, which is not only a question of epistemology.

Hardwig (1991) has argued that epistemic trust in another person involves reliance on their character (similar points have been made about trust more generally; e.g., Baier 1986)[^baier-1986]. In particular, a trustor must rely on the trustee’s willingness to tell the truth. If epistemic trust involves reliance on character traits or motives, it is, strictly speaking, not applicable to AI, as long as AI does not have character or will (see, however, Ferrario et al. 2021 and Starke et al. 2021 for discussion)[^ferrario-2021][^starke-2021].

Still, even if full epistemic trust in AI is impossible, people can rely on AI (i.e., believe or accept its results) or take an unquestioning attitude to its outputs (Nguyen 2022)[^nguyen-2022]. The aforementioned justifications for believing AI results do not—and need not—refer to character traits. The reason is likely that motives become an issue for trust only if we know that the trusted person has certain intentions and can change them. Although this is not the case with (current) AI, the intentions of those people who have built, trained, or even prompted an AI model can influence whether the AI system can be epistemically trusted.

The (epistemic) trust that humans invest in AI as a matter of fact has been investigated using empirical studies (see Glikson & Woolley 2020 for an overview)[^glikson-2020]. Some of these studies report human overreliance on AI (e.g., Klingbeil et al. 2024)[^klingbeil-2024], which can negatively impact the ability and preparedness to think critically (Zhai et al. 2024)[^zhai-2024]. The epistemology of AI is crucial to determining how much we should trust AI and what overreliance is.

Notably, epistemic trust is not the only epistemologically relevant attitude that humans may have towards AI. For instance, humans may justifiably consider AI models to be experts or epistemic authorities. According to Zagzebski’s (2012) often-quoted account of epistemic authority, we take someone else to be an epistemic authority if we defer to their judgment and bracket our own reasons that bear on the case (preemption). For instance, I may defer to a doctor’s judgment that a treatment is effective even though I have some evidence that it is not. It is natural to say that current AI does not qualify as a full expert (Ferrario et al. 2024)[^ferrario-2024]. Still, it seems to approach the status of an epistemic authority on some matters (Hauswald 2025; see Mizrahi 2025 for a critique)[^hauswald-2025][^mizrahi-2025].

As indicated, AI and its use are rapidly evolving, and new patterns of use are emerging. For instance, so-called AI agents or systems of interacting AI agents can take over complex epistemic work (Barman et al. 2025, Villaescusa-Navarro et al. 2025 [Other Internet Resources])[^barman-2025]. In such applications, broader trust that AI agents do their jobs well will become an issue.

## 4. Contribution of AI to understanding

It is one thing to know something, and another to understand it. Understanding seems to be a distinct epistemic achievement that is arguably more valuable than knowledge (see Grimm 2012 for an overview)[^grimm-2012]. Therefore, the epistemology of AI should also cover understanding. Notably, AI has a rather bad press regarding understanding. For instance, Messeri and Crockett (2024) write: “The proliferation of AI tools in science risks introducing a phase of scientific enquiry in which we produce more but understand less” (see also Sanjuán 2021, 1)[^sanjuán-2021].

Now, of course, LLMs can explain all kinds of things to individual users. Still, the worry expressed by many researchers is that AI models, particularly ML models such as ANNs, do not foster scientific understanding. The most obvious reason for such claims is that the models are poorly understood, which seems to make it difficult to use them as vehicles for understanding. In more detail, according to a recent account (de Regt and Dieks 2005; de Regt 2017)[^regt-2017][^regt-2005], scientific understanding requires a theory that is intelligible to the working scientist, which is not the case for many ML models, particularly ANNs. Nevertheless, some authors (Sullivan 2022; Krenn et al. 2022)[^krenn-2022][^sullivan-2022] have suggested that ANNs can deepen human understanding.

Upon closer analysis, the contribution of AI to human understanding depends on (a) what exactly “understanding” means, (b) what exactly “contribution” means, (c) which type of AI is under consideration, and (d) how AI is used (see, e.g., Krenn et al. 2022)[^krenn-2022]. As before with knowledge, we can bracket the question of whether AI itself has an understanding of the situation because AI understanding would have to be based on mental states of the AI, which is controversial at best (but see Beckmann 2025 for an argument that SORA, a video-generating AI tool, has an understanding of the world)[^beckmann-2025].

Epistemologists distinguish between various kinds of understanding, with the most important being objectual and explanatory understanding, both of which occur in degrees (see, e.g., Baumberger et al. 2016; Grimm 2021)[^baumberger-2016][^grimm-2021]. Objectual understanding is the understanding of an object or domain of things; it is often described as having a grasp of various types of connections between items or aspects of a topic, such as logical, probabilistic, evidential, and explanatory connections (Kvanvig 2003, 192)[^kvanvig-2003]. By contrast, an agent is roughly said to have an explanatory understanding of why *p* is the case if they accept a true explanation of *p* and can *grasp* it (e.g., Hills 2016)[^hills-2016]. Here, grasp of connections or explanations is typically explicated through various abilities; for instance, the agent can infer what would happen if assumptions in the explanation were slightly modified.

As inferential tools, AI applications can establish logical, probabilistic, and evidential connections. For instance, if an AI tool predicts a patient’s susceptibility to a specific disease, given information about the patient, and scientists trust the tool, they learn that the patient is at risk of that disease. The patient information can then be used as evidence for assessing susceptibility to the disease. Thus, AI tools can contribute to objectual understanding. However, the connection between a particular input and output is often too specific to enable the human to make more of their knowledge of the connection and run additional inferences about slightly modified situations, as would be required for grasping the connection. But humans who repeatedly run the AI tool on various inputs can learn generalizable connections, which they can then use to make additional inferences (see Lenhard 2019, 100 for this mechanism)[^lenhard-2019]. If this is the case, the humans deepen their objectual understanding using the AI tool. Still, this understanding is based on intensive work with the tool, with the final understanding of connections no longer requiring the tool (cf. Lawler & Sullivan 2021)[^lawler-2021].

As indicated, many ML models represent latent features. Accordingly, ML models may aid objectual understanding by disclosing connections between latent features (and more obvious features). However, this is only possible if humans know these latent features. Such knowledge requires methods of interpretability being applied to the models (see Schut et al. 2023 [Other Internet Resources] for an interesting example in which chess grandmasters learned from AI).

Regarding explanatory understanding, AI can undoubtedly aid the discovery of explanations by suggesting hypotheses about causal connections or laws. For instance, if scientists observe that weather data indicating a specific type of thunderstorm leads to correct predictions of a drop in the temperature in the same region, they may hypothesize that the former is a cause of the latter.

AI applications provide explanatory understanding in a more thorough sense if they contain an explanation. Many computer simulations do this because they are based upon laws of nature and can thus be seen as deductively inferring the consequences of laws and antecedent conditions contained in the input, as required by the DN model of explanation (Hempel & Oppenheim 1948)[^hempel-1948]. Other computer simulations use descriptions of mechanisms to infer the consequences for higher-level phenomena and thus explain them (Sawyer 2004)[^sawyer-2004]. Accordingly, scientists can use a computer simulation to derive a yet unexplained event from potentially explanatory assumptions. Notably, however, scientists can claim to explain a phenomenon reproduced by a computer simulation only if they show that the (e.g., mechanistic) assumptions in the simulation are true and that these assumptions are decisive for the explanandum phenomenon (Grüne-Yanoff 2009)[^grüne-yanoff-2009]. Furthermore, even if this is the case, knowledge of the explanation may not confer real understanding, because scientists may not be able to work with it (e.g., to draw other inferences). In terms of de Regt’s (2017) account of understanding, an intelligible theory is missing.

That GOFAI can provide explanations in the sense just characterized is straightforward because the crucial explanatory assumptions are built into the simulation. It would be much more interesting if ML could infer new explanations without the investment of prior explanatory knowledge (see Beisbart 2025a for discussion)[^beisbart-2025a]. ML models can certainly reproduce the explanandum phenomena given suitable input data. However, due to the opacity of ML, it often remains unclear whether the relevant inference is based on a law of nature or on something else that might be explanatory. Even if there are good reasons to think that specific ML models become sensitive to causes or other explanatory-relevant information (Pietsch 2016 and 2021)[^pietsch-2016][^pietsch-2021], this does not help, because humans do not know the causes unless they learn a great deal about the ML application. However, human scientists can run Mill’s (1843 [1996, Part III]) method of difference using the AI model: input variables are systematically varied, and the consequences for the output are traced. Given certain assumptions (homogeneity and faithful representation of the target through the model), they may then infer that a certain input variable is causally relevant to a feature of the output (Knüsel & Baumberger 2020; Meskhidze 2023)[^knüsel-2020][^meskhidze-2023]. In this manner, they can obtain a causal explanation based on ML (see Buijsman 2023 for more discussion)[^buijsman-2023].

Chatbots based on LLMs can answer “why” questions and thus give explanations. To some extent, chatbots rephrase previously given explanations that are memorized by the LLM (Millière & Buckner 2024a, 2024b [Other Internet Resources]). In other cases, LLMs may provide text that looks like a plausible explanation. However, the text may contain hallucination, and even if it only provides true information, this may not constitute a correct explanation. Therefore, if a chatbot suggests an explanation by answering a “why” question, we can only accept it if there is epistemic justification for doing so. For instance, the LLM may be known to contain a faithful world model of a certain domain of things (but see Beckmann & Queloz 2026, Sec. 5 for a caveat)[^beckmann-2026].

## 5. Further philosophical issues

### 5.1 Epistemic subject

When AI systems support humans in their inquiries, it may be asked what precisely the epistemic subject is. One natural candidate is the human person; however, as an alternative, we may also claim that a human and the AI application together form the subject. This is possible if the mind can extend beyond the human skull and skin because, under certain conditions, cognitive achievements and mental states are attributable to a coupled system consisting of a human person and a tool, such as a computer running a specific program (Clark & Chalmers 1998; cf. Hutchins 2000; see Menary 2010 for a discussion)[^clark-1998][^hutchins-2000][^menary-2010]. For instance, if a human medical doctor uses an AI tool to diagnose a particular disease, this achievement may be attributed to a coupling between the human and the AI (see Beisbart 2012 for a similar proposal regarding computer simulations)[^beisbart-2012].

Whether the unaided human or a coupled system is the epistemic subject/agent matters in some discussions in the epistemology of AI. For instance, the degree to which AI applications are opaque depends on who the agent is: an unaided human cannot check all the relevant steps in a computer-assisted proof, but they can do so with the help of a computer program such as a proof checker (see Tymoczko 1979 and Teller 1980 for a discussion on this point)[^teller-1980][^tymoczko-1979].

The ambiguity in the epistemic subject just noted raises the question of how we should think of the epistemic subject, or which subject is more relevant. This is muddy terrain, and the answer depends on what “relevant” means. In one sense, this question asks how best to describe and explain inquiry. Clark and Chalmers (1998) have argued that certain cognitive achievements are more easily explained by referring to coupled systems. As far as scientific inquiry is concerned, it is often argued that scientific work, knowledge, or understanding is no longer usefully thought to belong to individuals (Giere 2002)[^giere-2002]. This is not only because a great deal of scientific work is carried out by groups; according to Humphreys (2009, 616), the computational methods “push humans away from the centre of the epistemological enterprise.” Humphreys considers current science a hybrid that is still significantly constrained by the limits of human abilities, but envisions the possibility of “automated science.” However, he still takes the perspective of unaided humans when speaking of the “anthropocentric predicament” vis-à-vis automated science (i.e., the difficulty humans face in understanding automated science; ibid., 617).

The question about the proper epistemic subject can also be understood in a normative, even moral sense that relates to our self-understanding. The question then is to what extent we should care about what humans can do without computer assistance. Worries about deskilling—that humans lose certain skills through extensive AI use (see, e.g., Krook 2025 and Lee et al. 2025 for related empirical work; see Helal et al. 2025 for a meta-analysis)[^helal-2025][^krook-2025][^lee-2025]—are premised on the assumption that humans should be able to complete certain tasks on their own. There are also concerns that the constant use of LLMs incentivizes a superficial type of knowledge and thus deteriorates our epistemic situation (Hila 2025; cf. Schneider 2025)[^hila-2025][^schneider-2025]. By contrast, if we stress that AI tools enable humans to extend themselves (Humphreys 2004)[^humphreys-2004] and to complete tasks they couldn’t before, we assume that the coupled system is the more significant epistemic subject.

### 5.2 Relationship between the epistemology and ethics of AI

This issue of the epistemic subject is but one example of how epistemological questions about AI often raise ethical questions, and vice versa, even if both fields may currently be rather disconnected (as suggested by Russo et al. 2024)[^russo-2024].

From the perspective of the *epistemology* of AI *as an object of knowledge* (and understanding), ethical demands are crucial when it comes to the question of what exactly should be known (and understood) about AI. This question is hardly avoidable because several aspects that are not (yet) known about AI may not be particularly valuable to know. The epistemology of AI can tell us which knowledge is significant in an epistemic sense (e.g., by opening fruitful avenues of research), but not which knowledge has practical significance (to use a distinction drawn by Kitcher 2001, 65)[^kitcher-2001]. For instance, if medical doctors know their AI tools well, they can better understand when these tools fail and can thus avoid mistaken diagnoses leading to bad patient outcomes, which is a matter of practical significance. Relatedly, when transparency conflicts with other demands such as precision, ethical considerations are needed to decide on the trade-off.

The epistemology of AI is less dependent on ethics if AI is considered as an epistemic tool or agent rather than the object of knowledge. The degree to which AI results are epistemically justified can then be discussed without recourse to ethics: ethics is only relevant when we need to determine the confidence level required for specific practical applications. Inductive inferences come with an inductive risk of getting things wrong, and tradeoffs between non-epistemic values are needed to decide which risks are tolerable (e.g., Johnson 2023)[^johnson-2023]. In the last few years, a particular emphasis has been placed on models for which error rates differ between different groups, often in a morally problematic way because previous patterns of discrimination are translated into software (Johnson 2020; Fazelpour & Danks 2021; Hedden 2021)[^fazelpour-2021][^hedden-2021][^johnson-2020]. Moral reasons also become crucial when we decide whether we use a specific AI tool. Even if the results of the AI tool are epistemically justified, this does not imply we are morally permitted to use AI. For instance, AI use may contribute to human deskilling or infringe others’ intellectual property rights.

From the perspective of the *ethics* of AI, the epistemology of AI is crucial. This is because AI is largely, but not exclusively, an “epistemic technology” (Alvarado 2023a, 31)[^alvarado-2023a] yielding “cognitive interventions that are aimed at improving the epistemic environment” (Grote 2025, 1221)[^grote-2025]. When this is the case, then the ethical evaluation will depend on epistemological considerations. This is evident from the fact that concerns expressed in the ethics of AI, for instance regarding inconclusive, inscrutable, and misguided evidence (Mittelstadt et al. 2016; Morley et al. 2020)[^mittelstadt-2016][^morley-2020], are epistemological. As a concrete example, consider the concern that using AI for diagnoses is dangerous because AI is prone to error, particularly with new types of data. Ultimately, this worry is rooted in the moral values of human health and well-being. Still, the extent to which the concern is justified depends on how reliable the AI tool is (for certain groups of people, maybe), and this latter question can be discussed in purely epistemological terms.

Since moral concerns about AI often lead to epistemic problems, Grote (2025) has argued for the methodological priority of the epistemology of AI over its ethics. However, this seems to go too far. One reason is that the design of ML models involves tradeoffs that cannot be decided on epistemic grounds alone. For instance, to train a classifier, designers must decide on the comparative weights they give to false positives and false negatives (Kraemer et al. 2011)[^kraemer-2011], and this decision requires recourse to non-epistemic values (Rudner 1953)[^rudner-1953]. To provide a different example, if algorithmic bias is defined as variation in performance across groups, it seems to be merely an epistemological or technical problem. However, there is an important moral question here: under which circumstances is such bias morally wrong? Accordingly, AI design must be guided by both epistemic and moral values (Russo et al. 2024)[^russo-2024].

The recent epistemic achievements due to AI are likely to impact other debates in epistemology such as the discussion on scientific realism (Chakravartty 2025)[^chakravartty-2025]. On the one hand, the extension of human capacities makes it more plausible to hold the realist view that humans can know about unobservables. One the other hand, AI may also strengthen the underdetermination argument against realism if it turns out that AI uses different latent features than humans do to make predictions about observables. It is also debated whether the no-miracles argument can be extended to AI models (e.g., Rowbottom & Curtis-Trudel 2026)[^rowbottom-2026]. Future AI applications will likely provide epistemologists with more “food for thought”.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=epistemology-ai). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/epistemology-ai/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=epistemology-ai&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/epistemology-ai/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- Bereska, Leonard, and Efstratios Gavves, 2024, “[Mechanistic Interpretability for AI Safety — A Review](https://arxiv.org/abs/2404.14082)”, *arXiv* preprint, arXiv:2404.14082.
- Chalmers, David J., 2025, “[Propositional Interpretability in Artificial Intelligence](https://arxiv.org/abs/2501.15740)”, *arXiv* preprint, arXiv:2501.15740.
- Doshi-Velez, Finale, and Been Kim, 2017, “[Towards a Rigorous Science of Interpretable Machine Learning](https://arxiv.org/abs/1702.08608)”, *arXiv* preprint, arXiv:1702.08608.
- Goodfellow, Ian J., Jonathon Shlens, and Christian Szegedy, 2014, “[Explaining and Harnessing Adversarial Examples](https://arxiv.org/abs/1412.6572)”, *arXiv* preprint, arXiv:1412.6572.
- Guo, Daya, et al., 2025, “[Deepseek-r1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948)”, *arXiv* preprint, arXiv:2501.12948.
- Mahapatra, Joy, and Utpal Garain, 2024, “[Impact of Model Size on Fine-Tuned LLM Performance](https://arxiv.org/abs/2407.14088)”, *arXiv* preprint, arXiv:2407.14088.
- Millière, Raphaël, and Cameron Buckner, 2024a, “[A Philosophical Introduction to Language Models — Part I](https://arxiv.org/abs/2401.03910)”, *arXiv* preprint, arXiv:2401.03910.
- –––, 2024b, “[A Philosophical Introduction to Language Models — Part II](https://arxiv.org/abs/2405.03207)”, *arXiv* preprint, arXiv:2405.03207.
- Preece, Alun, Dan Harborne, Dave Braines, Richard Tomsett, and Supriyo Chakraborty, 2018, “[Stakeholders in Explainable AI](https://arxiv.org/abs/1810.00184)”, *arXiv* preprint, arXiv:1810.00184.
- Samek, Wojciech, Thomas Wiegand, and Klaus-Robert Müller, 2017, “[Explainable Artificial Intelligence: Understanding, Visualizing and Interpreting Deep Learning Models](https://arxiv.org/abs/1708.08296)”, *arXiv* preprint, arXiv:1708.08296.
- Schut, Lisa, et al., 2023, “[Bridging the Human-AI Knowledge Gap: Concept Discovery and Transfer in AlphaZero](https://arxiv.org/abs/2310.16410)”, *arXiv* preprint, arXiv:2310.16410.
- Simonyan, Karen, Andrea Vedaldi, and Andrew Zisserman, 2014, “[Deep Inside Convolutional Networks: Visualising Image Classification Models and Saliency Maps](https://arxiv.org/abs/1312.6034)”, *arXiv* preprint, arXiv:1312.6034.
- Szegedy, Christian, 2013, “[Intriguing Properties of Neural Networks](https://arxiv.org/abs/1312.6199)”, *arXiv* preprint, arXiv:1312.6199.
- Urban, Caterina, and Antoine Miné, 2021, “[A Review of Formal Methods Applied to Machine Learning](https://arxiv.org/abs/2104.02466)”, *arXiv* preprint, arXiv:2104.02466.
- Villaescusa-Navarro, Francisco, et al., 2025, “[The Denario Project: Deep Knowledge AI Agents for Scientific Discovery](https://arxiv.org/abs/2510.26887)”, *arXiv* preprint, arXiv:2510.26887.
- Zhao, Wayne Xin, et al., 2023, “[A Survey of Large Language Models](https://arxiv.org/abs/2303.18223)”, *arXiv* preprint, arXiv:2303.18223.

## Related Entries

artificial intelligence | artificial intelligence: ethics of | computer science, philosophy of | connectionism | induction: problem of | reasoning: automated | scientific explanation | simulations in science | understanding

[^abolhasani-2023]: Abolhasani, Milad, and Eugenia Kumacheva, 2023, “The Rise of Self-Driving Labs in Chemical and Materials Sciences”, *Nature Synthesis*, 2: 483–492.

[^abramson-2024]: Abramson, Josh, et al., 2024, “Accurate Structure Prediction of Biomolecular Interactions with AlphaFold 3”, *Nature*, 630.8016: 493–500.

[^adadi-2018]: Adadi, Amina, and Mohammed Berrada, 2018, “Peeking Inside the Black-Box: A Survey on Explainable Artificial Intelligence (XAI)”, *IEEE Access*, 6: 52138–52160.

[^alvarado-2022]: Alvarado, Ramón, 2022, “Computer Simulations as Scientific Instruments”, *Foundations of Science*, 27(3), 1183–1205.

[^alvarado-2023a]: –––, 2023a, “AI as an Epistemic Technology”, *Science & Engineering Ethics*, 29:32.

[^alvarado-2023b]: –––, 2023b, “What Kind of Trust Does AI Deserve, If Any?”, *AI and Ethics*, 3(4): 1169–1183.

[^arrieta-2020]: Arrieta, Alejandro B., et al., 2020, “Explainable Artificial Intelligence (XAI): Concepts, Taxonomies, Opportunities and Challenges Toward Responsible AI*”, Information Fusion*, 58: 82–115.

[^baier-1986]: Baier, Annette, 1986, “Trust and Antitrust”, *Ethics*, 96(2): 231–260.

[^baird-2004]: Baird, Davis, 2004, *Thing Knowledge: A Philosophy of Scientific Instruments*, Berkeley, CA: University of California Press.

[^barberousse-2009]: Barberousse, Anouk, Sara Franceschelli, and Cyrille Imbert, 2009, “Computer Simulations as Experiments”, *Synthese*, 169: 557–574.

[^barman-2025]: Barman, Kristian G., et al., 2025, “Large Physics Models: Towards a Collaborative Approach with Large Language Models and Foundation Models”, *The European Physical Journal C*, 85.9: 1066.

[^baron-2023]: Baron, Sam, 2023, “Explainable AI and Causal Understanding: Counterfactual Approaches Considered”, *Minds and Machines*, 33(2): 347–377.

[^baron-2025]: –––, 2025, “Trust, Explainability and AI”, *Philosophy & Technology*, 38(4).

[^baumberger-2016]: Baumberger, Christoph, Claus Beisbart, and Georg Brun, 2016, “What Is Understanding? An Overview of Recent Debates in Epistemology and Philosophy of Science”, in Stephen Grimm, Christoph Baumberger, and Sabine Ammon (eds.), *Explaining Understanding. New Perspectives from Epistemology and Philosophy of Science*, New York: Routledge, pp. 1–34.

[^beckers-2022]: Beckers, Sander, 2022, “Causal Explanations and XAI”, *Proceedings of the First Conference on Causal Learning and Reasoning, Proceedings of Machine Learning Research*, 177: 90–109.

[^beckmann-2025]: Beckmann, Pierre, 2025, “New Horizons in Machine Understanding: Explanatory and Objectual Understanding in Deep Learning Video Generation Models”, *Synthese*, 206: 285.

[^beckmann-2026]: Beckmann, Pierre, and Queloz, Matthieu, 2026, “Mechanistic Indicators of Understanding in Large Language Models”, *Philosophical Studies*, 183: 1749–1792.

[^beisbart-2012]: Beisbart, Claus, 2012, “How Can Computer Simulations Produce New Knowledge?”, *European Journal for Philosophy of Science*, 2.3: 395–434.

[^beisbart-2019a]: –––, 2019a, “What is Validation of Computer Simulations? Toward a Clarification of the Concept of Validation and of Related Notions”, in Claus Beisbart and Nicole Saam (eds), *Computer Simulation Validation: Simulation Foundations, Methods and Applications*, Cham: Springer.

[^beisbart-2019b]: –––, 2019b, “Should Validation and Verification Be Separated Strictly?”, in Claus Beisbart and Nicole Saam (eds.), *Computer Simulation Validation: Simulation Foundations, Methods and Applications.* Cham: Springer.

[^beisbart-2021]: –––, 2021, “Opacity Thought Through: On the Intransparency of Computer Simulations”, *Synthese*, 199: 11643–11666.

[^beisbart-2025a]: –––, 2025a, “Digging Deeper with Deep Learning? Explanatory Understanding and Deep Neural Networks”, *European Journal for Philosophy of Science*, 50:14.

[^beisbart-2025b]: –––, 2025b, “In Which Ways Is Machine Learning Opaque?”, in: Juan M. Durán and Giorgia Pozzi (eds.), *Philosophy of Science for Machine Learning: Core Issues and New Perspectives*, Cham: Springer, pp. 3–24.

[^beisbart-2022]: Beisbart, Claus, and Tim Räz, 2022, “Philosophy of Science at Sea: Clarifying the Interpretability of Machine Learning”, *Philosophy Compass*, 17(6), e12830.

[^belkin-2019]: Belkin, Mikhail, et al., 2019, “Reconciling Modern Machine-Learning Practice and the Classical Bias–Variance Trade-off”, *Proceedings of the National Academy of Sciences*, 116.32: 15849–15854.

[^bjerring-2020]: Bjerring, Jens Christian, and Jacob Busch, 2020, “Artificial Intelligence and Patient-Centered Decision-Making”, *Philosophy and Technology*, 34(2): 349–371.

[^boden-2016]: Boden, Margaret A., 2016, *AI: Its Nature and Future*, Oxford: Oxford University Press.

[^boge-2022]: Boge, Florian J., 2022, “Two Dimensions of Opacity and the Deep Learning Predicament”, *Minds & Machines*, 32, 43–75.

[^boge-nd]: Boge, Florian J., and Paul Grünke, forthcoming, “Computer Simulations, Machine Learning and the Laplacean Demon: Opacity in the Case of High Energy Physics”, in Andreas Resch, Michael Kaminski, and Petra Gehring (eds.), *The Science and Art of Simulation II*, Cham: Springer.

[^bringsjord-2026]: Bringsjord, Selmer, and Naveen Sundar Govindarajulu, 2026, “Artificial Intelligence”, *The Stanford Encyclopedia of Philosophy* (Spring 2026 Edition), Edward N. Zalta & Uri Nodelman (eds.), URL = <[https://plato.stanford.edu/archives/spr2026/entries/artificial-intelligence/](https://plato.stanford.edu/archives/spr2026/entries/artificial-intelligence/)>.

[^buckner-2018]: Buckner, Cameron, 2018, “Empiricism without Magic: Transformational Abstraction in Deep Convolutional Neural Networks”, *Synthese*, 195, 5339–5372.

[^buckner-2019]: –––, 2019, “Deep Learning: A Philosophical Introduction”, *Philosophy Compass*, 14: e12625.

[^buckner-2023]: –––, 2023, *From Deep Learning to Rational Machines: What the History of Philosophy Can Teach Us about the Future of Artifical Intelligence*, New York, NY: Oxford University Press.

[^buchholz-2025]: Buchholz, Oliver, and Eric Raidl, 2025, “A Falsificationist Account of Artificial Neural Networks”, *The British Journal for the Philosophy of Science*, 76(4): 1011–1035.

[^bueno-2014]: Bueno, Otávio, 2014, “Computer Simulations: An Inferential Conception”, *The Monist* 97(3): 378–398.

[^buijsman-2023]: Buijsman, S., 2023, “Causal Scientific Explanations from Machine Learning”, *Synthese*, 202(202).

[^burrell-2016]: Burrell, Jenna, 2016, “How the Machine ‘Thinks’: Understanding Opacity in Machine Learning Algorithms”, *Big Data & Society*, 3(1): 2053951715622512.

[^butlin-2025]: Butlin, Patrick, and Emanuel Viebahn, 2025, “AI Assertion”, *Ergo: An Open Access Journal of Philosophy*, 12(37): 968–988.

[^buttaboni-2026]: Buttaboni, Carlotta, and Luciano Floridi, 2026, “A Regulatory Taxonomy of AI Opacity in the EU: Rethinking Transparency, Traceability, Interpretability, and Explainability”, *AI and Ethics*, 6(100).

[^callaway-2020]: Callaway, Ewen, 2020, “‘It Will Change Everything’: DeepMind’s AI makes Gigantic Leap in Solving Protein Structures,”, *Nature*, 588(7837): 203–205.

[^carvalho-2019]: Carvalho, Diogo V., Eduardo M. Pereira, and Jaime S. Cardoso, 2019, “Machine Learning Interpretability: A Survey on Methods and Metrics”, *Electronics*, 8(8): 832.

[^castelvecchi-2016]: Castelvecchi, Davide, 2016, “Can we Open the Black Box of AI?”, *Nature News*, 538(7623): 20–23.

[^castelvecchi-2025]: –––, 2025, “AI Models Solve Maths Problems at Level of Top Students”. *Nature*, 644(7): 1.

[^castelvecchi-2026]: –––, 2026, “OpenAI Claims Huge Maths Breakthrough on a Famed ‘Millennium Problem’”. *Nature*, 657: 579–580.

[^castillo-2024]: Castillo Brache, Leticia, and Alisa Bokulich, 2024, “Models, Data Models, and Big Data”, in Tarja Knuuttila, Natalia Carrillo, and Rami Koskinen (eds.), *The Routledge Handbook of Philosophy of Scientific Modeling*, Abingdon & New York: Routledge, pp. 245–255.

[^chakravartty-2025]: Chakravartty, Anjan, 2025, “Scientific Realism”, *The Stanford Encyclopedia of Philosophy* (Winter 2025 Edition), Edward N. Zalta & Uri Nodelman (eds.), URL = <[https://plato.stanford.edu/archives/win2025/entries/scientific-realism/](https://plato.stanford.edu/archives/win2025/entries/scientific-realism/)>.

[^clark-1998]: Clark, Andy, and David Chalmers, 1998, “The Extended Mind”, *Analysis*, 58(1): 7–19.

[^collins-2010]: Collins, Harry, 2010, *Tacit and Explicit Knowledge*, Chicago: Chicago University Press.

[^corfield-2010]: Corfield, David, 2010, “Varieties of Justification in Machine Learning”, *Minds & Machines*, 20: 291–301.

[^creel-2020]: Creel, Kathleen A., 2020, “Transparency in Complex Computational Systems”, *Philosophy of Science*, 87(4): 568–589.

[^cuomo-2022]: Cuomo, Salvatore, et al., 2022, “Scientific Machine Learning Through Physics–Informed Neural Networks: Where We Are and What’s Next”, *Journal of Scientific Computing*, 92.3 (2022): 88.

[^danks-2014]: Danks, David, 2014, “Learning”, in Keith Frankish and William M. Ramsey (eds.), *Cambridge Handbook of Artificial Intelligence*, Cambridge: Cambridge University Press, pp. 151–167.

[^dennett-1987]: Dennett, Daniel C., 1987, *The Intentional Stance*, Cambridge, MA: MIT Press.

[^regt-2017]: de Regt, Henk W., 2017, *Understanding Scientific Understanding*, New York: Oxford University Press.

[^regt-2020]: –––, 2020, “Understanding, Values, and the Aims of Science”, *Philosophy of Science*, 87(5): 921–932.

[^regt-2005]: de Regt, Henk W., and Dennis Dieks, 2005, “A Contextual Approach to Scientific Understanding”, *Synthese*, 144: 137–70.

[^dill-2012]: Dill, Ken A., & Justin L. MacCallum, 2012, “The Protein-Folding Problem, 50 Years On”, *Science*, 338(6110): 1042–1046.

[^di-2000]: Di Paolo, Ezequiel A., Jason Noble, and Seth Bullock, 2000, “Simulation Models as Opaque Thought Experiments”, in Mark A. Bedau et al. (eds.), *Artificial Life VII: Proceedings of the Seventh International Conference on the Synthesis and Simulation of Living Systems*, Cambridge, MA: MIT Press, pp. 497–506.

[^dormandy-2019]: Dormandy, Katherine (ed.), 2019, *Trust in Epistemology*, New York: Taylor & Francis.

[^dreyfus-1972]: Dreyfus, Hubert L., 1972, *What Computers Can’t Do: The Limits of Artificial Intelligence*, New York: Harper & Row.

[^dreyfus-1992]: –––, 1992, *What Computers Still Can’t Do: A Critique of Artificial Reason*, Cambridge, MA: MIT Press.

[^duede-2022]: Duede, Eamon, 2022, “Instruments, Agents, and Artificial Intelligence: Novel Epistemic Categories of Reliability”, *Synthese*, 200: 491.

[^duede-2023]: –––, 2023, “Deep Learning Opacity in Scientific Discovery”, *Philosophy of Science*, 90(5): 1089–1099.

[^durán-2018]: Durán, Juan M., & Nico Formanek, 2018, “Grounds for Trust: Essential Epistemic Opacity and Computational Reliabilism”, *Minds & Machines*, 28: 645–666.

[^durán-2021]: Durán, Juan M., and Karin R. Jongsma, 2021, “Who Is Afraid of Black Box Algorithms? On the Epistemological and Ethical Basis of Trust in Medical AI”, *Journal of Medical Ethics*, 47(5): 329–335.

[^ellis-1998]: Ellis, Brian, 1998, “An Essentialist Perspective on the Problem of Induction”, *Principia*, 2(1): 103–124.

[^erasmus-2021]: Erasmus, Adrian, Tyler D. P. Brunet, and Eyal Fisher, 2021, “What is Interpretability?”, *Philosophy and Technology*, 34: 833–862.

[^facchini-2022]: Facchini, Alessandro, and Alberto Termine, 2022, “Towards a Taxonomy for the Opacity of AI Systems”, in Vincent C. Müller (ed.), *Philosophy and Theory of Artificial Intelligence 2021: Studies in Applied Philosophy, Epistemology and Rational Ethics*, 63, Cham: Springer, pp. 73–89.

[^fazelpour-2021]: Fazelpour, Sina, and David Danks, 2021, “Algorithmic Bias: Senses, Sources, Solutions”, *Philosophy Compass*, 16(8): e12760.

[^ferrario-2021]: Ferrario, Andrea, Michele Loi, and Eleonora Viganò, 2021, “Trust Does Not Need to be Human: It Is Possible to Trust Medical AI”, *Journal of Medical Ethics*, 47(6): 437–438.

[^ferrario-2024]: Ferrario, Andrea, Alessandro Facchini, and Alberto Termine, 2024, “Experts or Authorities? The Strange Case of the Presumed Epistemic Superiority of Artificial Intelligence Systems”, *Minds and Machines*, 34(3): 1–27.

[^fetzer-1988]: Fetzer, James H., 1988, “Program Verification: The Very Idea”, *Communications of the ACM*, 31(9): 1048–1063.

[^fleisher-2022]: Fleisher, Will, 2022, “Understanding, Idealization, and Explainable AI”, *Episteme*, 19(4): 534–560.

[^freiesleben-2023]: Freiesleben, Timo, and Thomas Grote, 2023, “Beyond Generalization: A Theory of Robustness in Machine Learning”, *Synthese*, 202: 109.

[^freiman-2024]: Freiman, Oren, 2024, “AI-Testimony, Conversational AIs and Our Anthropocentric Theory of Testimony”, *Social Epistemology*, 38(4): 476–490.

[^french-1999]: French, Robert M., 1999, “Catastrophic Forgetting in Connectionist Networks”, *Trends in Cognitive Sciences*, 3.4: 128–135.

[^fricker-2016]: Fricker, Elizabeth, 2016, “Unreliable Testimony”, in H. Kornblith and B. McLaughlin (eds.), *Goldman and is Critics*, Malden, MA: Wiley Blackwell, pp. 88–123.

[^fricker-2025]: –––, 2025, “On the Metaphysical and Epistemic Contrasts Between Human and AI Testimony”, *Inquiry*, 1–26.

[^friedman-1974]: Friedman, Michael, 1974, “Explanation and Scientific Understanding”, *Journal of Philosophy*, 71: 5–19.

[^frigg-2026]: Frigg, Roman, and Stephan Hartmann, 2026, “Models in Science”, *The Stanford Encyclopedia of Philosophy* (Fall 2026 Edition), Edward N. Zalta & Uri Nodelman (eds.), URL = <[https://plato.stanford.edu/archives/fall2026/entries/models-science/](https://plato.stanford.edu/archives/fall2026/entries/models-science/)>.

[^gardiner-2022]: Gardiner, Georgi, and Brian Zaharatos, 2022, “The Safe, the Sensitive, and the Severely Tested: A Unified Account”, *Synthese*, 200(5): 369.

[^garreau-2020]: Garreau, Damien, and Ulrike Luxburg, 2020, “Explaining the Explainer: A First Theoretical Analysis of LIME”, in *Proceedings of the 23ʳᵈ* *International Conference on Artificial Intelligence and Statistics:* *Proceedings of Machine Learning Research*, 108.

[^geiger-2025]: Geiger, Atticus, Daniel Ibeling, Amir Zur, Mayank Chaudhary, Shreya Chauhan, Jialu Huang, Thomas Icard, and Clark Barrett, 2025, “Causal Abstraction: A Theoretical Foundation for Mechanistic Interpretability”, *Journal of Machine Learning Research*, 26(83): 1–64.

[^geiger-2021]: Geiger, Atticus, et al., 2021, “Causal Abstractions of Neural Networks”, *Advances in Neural Information Processing Systems*, 34: 9574–9586.

[^giere-2002]: Giere, Ronald, 2002, “Scientific Cognition as Distributed Cognition”, in Peter Carruthers, Stephen Stich, and Michael Siegal (eds.), *The Cognitive Basis of Science*, Cambridge: Cambridge University Press, pp. 285–299.

[^gillies-1996]: Gillies, Donald, 1996, *Artificial Intelligence and Scientific Method*, Oxford: Oxford University Press.

[^glikson-2020]: Glikson, Ella, and Anita Williams Woolley, 2020, “Human Trust in Artificial Intelligence: Review of Empirical Research”, *Academy of Management Annals*, 14(2): 627–660.

[^goldberg-2012]: Goldberg, Sanford C., 2012, “Epistemic Extendedness, Testimony, and the Epistemology of Instrument-Based Belief”, *Philosophical Explorations*, 15(2): 181–197.

[^goldman-1967]: Goldman, Alvin I., 1967, “A Causal Theory of Knowing”, *Journal of Philosophy*, 64(12): 357–372.

[^goldman-1976]: –––, 1976, “Discrimination and Perceptual Knowledge”, *Journal of Philosophy*, 73 (November): 771–791.

[^goldman-1979]: –––, 1979, “What is Justified Belief?”, in George Pappas (ed.), *Justification and Knowledge: New Studies in Epistemology*, Dordrecht: D. Reidel, pp. 1–25.

[^green-2022]: Green, Mitchell, and Jan G. Michel, 2022, “What Might Machines Mean?”, *Minds & Machines*, 32: 323–338.

[^grimm-2012]: Grimm, Stephen, 2012, “The Value of Understanding”, *Philosophy Compass*, 7(2): 103–117.

[^grimm-2021]: –––, 2021, “Understanding”, *The Stanford Encyclopedia of Philosophy* (Summer 2021 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/sum2021/entries/understanding/](https://plato.stanford.edu/archives/sum2021/entries/understanding/)>.

[^grindrod-2025]: Grindrod, Jumbly, 2025, “Computational Beliefs”, *Inquiry*, 68(10): 3169–3190.

[^grote-2025]: Grote, Thomas, 2025, “Machine Learning in Healthcare and the Methodological Priority of Epistemology over Ethics”, *Inquiry*, 68: 1218–1247.

[^grote-2020]: Grote, Thomas, and Philipp Berens, 2020, “On the Ethics of Algorithmic Decision-Making in Healthcare”, *Journal of Medical Ethics*, 46(3): 205–211.

[^grote-2024]: Grote, Thomas, Konstantin Genin, and Emily Sullivan, 2024, “Reliability in Machine Learning”, *Philosophy Compass*, 19(5): e12974.

[^grüne-yanoff-2009]: Grüne-Yanoff, T., 2009, “The Explanatory Potential of Artificial Societies”, in *Synthese* 169: 539–555.

[^gunning-2019]: Gunning, David, and David Aha, 2019, “DARPA’s Explainable Artificial Intelligence (XAI) Program”, *AI Magazine*, 40(2): 44–58.

[^gunning-2021]: Gunning, David, Eric Vorm, Yunyan Wang, and Matt Turek, 2021, “DARPA’s Explainable AI (XAI) Program: A Retrospective”, *Authorea Preprints*.

[^hardwig-1991]: Hardwig, John, 1991, “The Role of Trust in Knowledge”, *Journal of Philosophy*, 88(12): 693–708.

[^harman-1965]: Harman, Gilbert H., 1965, “The Inference to the Best Explanation”, *Philosophical Review*, 74(1): 88–95.

[^harris-2021]: Harris, Dan, and Dunham, Darin, 2021, “Induction in Machine Learning”, in *2021 IEEE Aerospace Conference*, IEEE *(50100)*, pp. 1–17.

[^harris-2003]: Harris, Todd, 2003, “Data Models and the Acquisition and Manipulation of Data”, *Philosophy of Science*, 70(5): 1508–1517.

[^hassija-2024]: Hassija, Vikas, Varun Chamola, Aniket Mahapatra, Ankit Singal, Divyansh Goel, Kun-Chih Huang, and Amir Hussain, 2024, “Interpreting Black-Box Models: A Review on Explainable Artificial Intelligence”, *Cognitive Computation*, 16(1): 45–74.

[^hatherley-2024]: Hatherley, Joshua J., Robert Sparrow, and Mark Howard, 2024, “The Virtues of Interpretable Medical Artificial Intelligence”, *Cambridge Quarterly of Healthcare Ethics*, 33(3): 323–332.

[^haugeland-1985]: Haugeland, John, 1985, *Artificial Intelligence: The Very Idea*, Cambridge, MA: MIT Press.

[^hausen-2020]: Hausen, Ryan, and Brant E. Robertson, 2020, “Morpheus: A Deep Learning Framework for the Pixel-Level Analysis of Astronomical Image Data” *The Astrophysical Journal Supplement Series*, 248(1): 20.

[^hauswald-2025]: Hauswald, Rico, 2025, “Artificial Epistemic Authorities”, *Social Epistemology*, 39(6): 716–725.

[^hedden-2021]: Hedden, Brian, 2021, “On Statistical Criteria of Algorithmic Fairness”, *Philosophy & Public Affairs*, 49(2): 209–231.

[^he-2025]: He, Jinhua, and Chen Yang, 2025, “Testimony by LLMs”, *AI & Society*, 40: 6201–6213.

[^heersmink-2024]: Heersmink, Richard, Barend de Rooij, María Jimena Clavel Vázquez, and Matteo Colombo, 2024, “A Phenomenology and Epistemology of Large Language Models: Transparency, Trust, and Trustworthiness”, *Ethics and Information Technology*, 26(3): 1–15.

[^helal-2025]: Helal, Mohamed Y. I., Ahmed E. Hassanien, Hossam A. Gaber, and Rehab F. Abdel-Kader, 2025, “The Impact of Generative AI on Critical Thinking Skills”, *Information Discovery and Delivery*.

[^hempel-1948]: Hempel, Carl G., and Paul Oppenheim, 1948, “Studies in the Logic of Explanation”, *Philosophy of Science*, 15(2): 135–175.

[^henderson-2024]: Henderson, Leah, “The Problem of Induction”, *The Stanford Encyclopedia of Philosophy* (Winter 2024 Edition), Edward N. Zalta & Uri Nodelman (eds.), URL = <[https://plato.stanford.edu/archives/win2024/entries/induction-problem/](https://plato.stanford.edu/archives/win2024/entries/induction-problem/)>.

[^herrmann-2024]: Herrmann, Daniel A., and Benjamin A. Levinstein, 2024, “Standards for Belief Representations in LLMs”, *Minds and Machines*, 35(1): 1–25.

[^hila-2025]: Hila, Angjelin, 2025, “The Epistemological Consequences of Large Language Models”, *AI & Society*: 1–19.

[^hills-2016]: Hills, Alison, 2016, “Understanding Why”*, Noûs*, 50: 661–688.

[^hinton-1984]: Hinton, Geoffrey E., 1984, “Distributed Representations”, Technical Report CMU-CS-84-157, Carnegie Mellon University.

[^holm-2026]: Holm, Sune, 2026, “On the Justified Use of AI Decision Support in Evidence-Based Medicine: Validity, Explainability, and Responsibility”, *Cambridge Quarterly of Healthcare Ethics*: 35(3): 183–189.

[^hosny-2018]: Hosny, Ahmed, et al., 2018, “Artificial Intelligence in Radiology”, *Nature Reviews Cancer*, 18(8): 500–510.

[^humphreys-2004]: Humphreys, Paul, 2004, *Extending Ourselves: Computational Science, Empiricism, and Scientific Method*, New York: Oxford University Press.

[^humphreys-2009]: –––, 2009, “The Philosophical Novelty of Computer Simulation Methods”, *Synthese*, 169: 615–626.

[^hutchins-2000]: Hutchins, Edwin, 2000, “Distributed Cognition”, in *International Encyclopedia of the Social and Behavioral Sciences*, Amsterdam: Elsevier, pp. 2068–2072.

[^iizuka-2024]: Iizuka, Shun, 2024, “Taking It Not at Face Value: A New Taxonomy for the Beliefs Acquired from Conversational AIs”, *Techné: Research in Philosophy and Technology*, 28(2): 219–235.

[^imbert-2017]: Imbert, Cyrille, 2017, “Computer Simulations and Computational Models in Science”, in Lorenzo Magnani and Tommaso Bertolotti (eds.), *Springer Handbook of Model-Based Science*. Cham: Springer, pp. 735–781.

[^jebeile-2021]: Jebeile, Julie, Vincent Lam, and Tim Räz, 2021, “Understanding Climate Change with Statistical Downscaling and Machine Learning”, *Synthese*, 199: 1877–1897.

[^johnson-2020]: Johnson, Gabbrielle M., 2020, “Algorithmic Bias: On the Implicit Biases of Social Technology”, *Synthese*, 198(10): 9941–9961.

[^johnson-2023]: –––, 2023, “Are Algorithms Value-Free?”, *Journal of Moral Philosophy*, 21(1–2): 1–35.

[^jumper-2021]: Jumper, John, et al., 2021, “Highly Accurate Protein Structure Prediction with AlphaFold.”, *Nature*, 596.7873: 583–589.

[^kaelbling-1996]: Kaelbling, Leslie P., Michael L. Littman, and Andrew W. Moore, 1996, “Reinforcement Learning: A Survey”, *Journal of Artificial Intelligence Research*, 4: 237–285.

[^khan-2022]: Khan, Salman, Mubarak Shah, and Salman Khan, 2022, “Transformers in Vision: A Survey”, *ACM Computing Surveys*, 54(10s): 1–41.

[^kirkpatrick-2017]: Kirkpatrick, James, et al., 2017, “Overcoming Catastrophic Forgetting in Neural Networks”, *Proceedings of the National Academy of Sciences*, 114(13): 3521–3526.

[^kitcher-2001]: Kitcher, Philip, 2001, *Science, Truth, and Democracy*, New York: Oxford University Press.

[^klingbeil-2024]: Klingbeil, Alexander, Christian Grützner, and Peter Schreck, 2024, “Trust and Reliance on AI: An Experimental Study on the Extent and Costs of Overreliance on AI”, *Computers in Human Behavior*, 160: 108352.

[^knüsel-2020]: Knüsel, Benedikt, and Christoph Baumberger, 2020, “Understanding Climate Phenomena with Data-Driven Models”, *Studies in History and Philosophy of Science Part A*, 84(C): 46–56.

[^kraemer-2011]: Kraemer, Felicitas, Kees Van Overveld, and Martin Peterson, 2011, “Is There an Ethics of Algorithms?”, *Ethics and Information Technology*, 13: 251–260.

[^krenn-2022]: Krenn, Mario, et al., 2022, “On Scientific Understanding with Artificial Intelligence”, *Nature Reviews Physics*, 4(12): 761–769.

[^krichen-2022]: Krichen, Moez, et al., 2022, “Are Formal Methods Applicable to Machine Learning and Artificial Intelligence?”, SMARTTECH 2022 Proceedings, IEEE.

[^krishnan-2020]: Krishnan, Maya, 2020, “Against Interpretability: A Critical Examination of the Interpretability Problem in Machine Learning”, *Philosophy & Technology*, 33: 487–502.

[^krook-2025]: Krook, Joshua, 2025, “When Autonomy Breaks: The Hidden Existential Risk of AI”, *AI & Society*, 40: 6011–6024.

[^kulmanov-2021]: Kulmanov, Maxat, et al., 2021, “Semantic Similarity and Machine Learning with Ontologies”, *Briefings in Bioinformatics*, 22.4: bbaa199.

[^kvanvig-2003]: Kvanvig, Jonathan, 2003, *The Value of Knowledge and the Pursuit of Understanding*, New York: Cambridge University Press.

[^langer-2021]: Langer, Markus, et al., 2021, “What Do We Want from Explainable Artificial Intelligence (XAI)? A Stakeholder Perspective on XAI and a Conceptual Model Guiding Interdisciplinary XAI Research,” *Artificial Intelligence*, 296: 103473.

[^lauc-2020]: Lauc, Davor, 2020, “Machine Learning and the Philosophical Problems of Induction”, in Sandro Skansi (ed.), *Guide to Deep Learning Basics*, Cham: Springer.

[^lawler-2021]: Lawler, Insa, and Emily Sullivan, 2021, “Model Explanation Versus Model-Induced Explanation”, *Foundations of Science*, 26(4): 1049–1074.

[^lee-2025]: Lee, Hyeon-Pyo, Anant Tankelevitch, Lucio Drosos, Ingrid Rintel, and Nicholas Wilson, 2025, “The Impact of Generative AI on Critical Thinking”, *Proceedings of CHI 2025*, 1–22.

[^lefrançois-2020]: Lefrançois, Guy R., 2020, *Theories of Human Learning*, Cambridge: Cambridge University Press.

[^lemos-2023]: Lemos, Pablo, Niall Jeffrey, Miles Cranmer, Shirley Ho, and Peter Battaglia, 2023, “Rediscovering Orbital Mechanics with Machine Learning”, *Machine Learning: Science and Technology*, 4(4): 045002.

[^lenhard-2019]: Lenhard, Johannes, 2019, *Calculated Surprises*, New York: Oxford University Press.

[^li-2023]: Li, Dan, 2023, “Machines Learn Better with Better Data Ontology: Lessons from Philosophy of Induction and Machine Learning Practice”, *Minds & Machines*, 33, 429–450.

[^linardatos-2020]: Linardatos, Pantelis, Vasilis Papastefanopoulos, and Sotiris Kotsiantis, 2020, “Explainable AI: A Review of Machine Learning Interpretability Methods”, *Entropy*, 23(1): 18.

[^lipton-2018]: Lipton, Zachary, 2018, “The Mythos of Model Interpretability: In Machine Learning, the Concept of Interpretability Is Both Important and Slippery”, *ACM Queue*, 16(3), July 17 2018. [[Lipton 2018 available online](https://queue.acm.org/doi/10.1145/3236386.3241340)]

[^liu-2019]: Liu, Yang, Eser Jun, Qing Li, and Jeffrey Heer, 2019, “Latent Space Cartography”, *Computer Graphics Forum*, 38(3): 67–78.

[^london-2019]: London, Alex John, 2019, “Artificial Intelligence and Black‐Box Medical Decisions: Accuracy versus Explainability”, *Hastings Center Report*, 49(1): 15–21.

[^mann-2023]: Mann, Sara, et al., 2023, “Sources of Opacity in Computer Systems: Towards a Comprehensive Taxonomy”, *2023 IEEE 31st International Requirements Engineering Conference Workshops (REW)*, Hannover, pp. 337–342.

[^marr-1982]: Marr, David, 1982, *Vision*, New York: W. H. Freeman.

[^mccoy-2022]: McCoy, Liam G., et al., 2022, “Believing in Black Boxes: Machine Learning for Healthcare Does Not Need Explainability to Be Evidence-Based”, *Journal of Clinical Epidemiology*, 142: 252–257.

[^mcevoy-2008]: McEvoy, Mark, 2008, “The Epistemological Status of Computer-Assisted Proofs”, *Philosophia Mathematica*, 16(3): 374–387.

[^menary-2010]: Menary, Richard (ed.), 2010, *The Extended Mind*, Cambridge, MA: MIT Press.

[^meskhidze-2023]: Meskhidze, Helen, 2023, “Can Machine Learning Provide Understanding? How Cosmologists Use Machine Learning to Understand Observations of the Universe”, *Erkenntnis*, 88(5): 1895–1909.

[^messeri-2024]: Messeri, Lisa, and M. J. Crockett, 2024, “Artificial Intelligence and Illusions of Understanding in Scientific Research”, *Nature*, 627(8002): 49–58.

[^mill-1843]: Mill, John Stuart, 1843 [1996], *A System of Logic: Ratiocinative and Inductive*, in J. M. Robson (ed.), *Collected Works of John Stuart Mill*, Volume VII, London and New York: Routledge.

[^miller-2019]: Miller, Tim, 2019, “Explanation in Artificial Intelligence: Insights from the Social Sciences” *Artificial Intelligence*, 267. 10.1016/j.artint.2018.07.007.

[^mitchell-1997]: Mitchell, Tom M., 1997, *Machine Learning*, New York: McGraw-Hill.

[^mitchell-1986]: Mitchell, Tom M., Richard M. Keller, and Smadar T. Kedar-Cabelli, 1986, “Explanation-Based Generalization: A Unifying View”, *Machine Learning*, 1(1): 47–80.

[^mittelstadt-2016]: Mittelstadt, Brent, Patrick Allo, Mariarosaria Taddeo, Sandra Wachter, and Luciano Floridi, 2016, “The Ethics of Algorithms: Mapping the Debate”, *Big Data and Society*, 3(2): 2053951716679679.

[^mittelstadt-2019]: Mittelstadt, Brent, Chris Russell, and Sandra Wachter, 2019, “Explaining explanations in AI”, In: FAT* ’19: Conference on Fairness, Accountability, and Transparency, January 29–31, 2019, Atlanta, GA, ACM, New York, NY, pp. 279–288.

[^mizrahi-2013]: Mizrahi, Moti, 2013, “The Pessimistic Induction: A Bad Argument Gone Too Far”, *Synthese*, 190(15): 3209–3226.

[^mizrahi-2025]: –––, 2025, “No Epistemic Respect for Bullshit Machines or LLMs”, *Social Epistemology Review and Reply Collective*, 14(9): 138–146.

[^molnar-2020]: Molnar, Christoph, Giuseppe Casalicchio, and Bernd Bischl, 2020, “Interpretable Machine Learning: A Brief History, State-of-the-Art and Challenges”, *Joint European Conference on Machine Learning and Knowledge Discovery in Databases*, Cham: Springer.

[^morley-2020]: Morley, Jessica, Caio C. V. Machado, Christopher Burr, Josh Cowls, Indra Joshi, Mariarosaria Taddeo, and Luciano Floridi, 2020, “The Ethics of AI in Health Care: A Mapping Review”, *Social Science & Medicine*, 260: 113172.

[^muldoon-2007]: Muldoon, Ryan, 2007, “Robust Simulations”, *Philosophy of Science*, 74(5): 873–883.

[^müller-2025]: Müller, Vincent C., 2025, “Ethics of Artificial Intelligence and Robotics”, *The Stanford Encyclopedia of Philosophy* (Fall 2025 Edition), Edward N. Zalta & Uri Nodelman (eds.), URL = <[https://plato.stanford.edu/archives/fall2025/entries/ethics-ai/](https://plato.stanford.edu/archives/fall2025/entries/ethics-ai/)>.

[^nakkiran-2021]: Nakkiran, Preetum, et al., 2021, “Deep Double Descent: Where Bigger Models and More Data Hurt”, *Journal of Statistical Mechanics: Theory and Experiment*, 2021.12: 124003.

[^neges-2018]: Neges, Sebastian, 2018, *Instrumentation: A Study in Social Epistemology*, PhD Dissertation, University of Vienna.

[^nguyen-2022]: Nguyen, C. Thi, 2022, “Trust as an Unquestioning Attitude”, *Oxford Studies in Epistemology*, 7: 214–244.

[^nielsen-2015]: Nielsen, Michael A., 2015, *Neural Networks and Deep Learning*, Determination Press.

[^niu-2021]: Niu, Shanshan, Yong Liu, Jian Wang, and Honggang Song, 2021, “A Decade Survey of Transfer Learning (2010–2020)”, *IEEE Transactions on Artificial Intelligence*, 1(2): 151–166.

[^norton-2021]: Norton, John D., 2021, *The Material Theory of Induction*, Calgary: University of Calgary Press.

[^oberkampf-2010]: Oberkampf, William, and Christopher Roy, 2010, *Verification and Validation in Scientific Computing*, Cambridge: Cambridge University Press.

[^olah-2020]: Olah, Chris, et al, 2020, “Zoom In: An Introduction to Circuits”, *Distill*, 5(3): e00024–001.

[^ortner-2011]: Ortner, Ronald, and Hannes Leitgeb, 2011, “Mechanizing Induction”, *Handbook of the History of Logic*, 10: Amsterdam: North-Holland, pp. 719–772.

[^páez-2019]: Páez, Andrés, 2019, “The Pragmatic Turn in Explainable Artificial Intelligence (XAI)”, *Minds and Machines*, 29(3): 441–459.

[^parker-2008a]: Parker, Wendy S., 2008a, “Computer Simulation Through an Error-Statistical Lens”, *Synthese*, 163(3): 371–384.

[^parker-2008b]: –––, 2008b, “Franklin, Holmes, and the Epistemology of Computer Simulation”, *International Studies in the Philosophy of Science*, 22(2): 165–183.

[^parker-2010]: –––, 2010, “An Instrument for What? Digital Computers, Simulation and Scientific Practice”, *Spontaneous Generations*, 4(1): 39–44.

[^parker-2011]: –––, 2011, “When Climate Models Agree: The Significance of Robust Model Predictions”, *Philosophy of Science*, 78(4): 579–600.

[^parker-2020]: –––, 2020, “Model Evaluation: An Adequacy-for-Purpose View”, *Philosophy of Science*, 87(3): 457–477.

[^pearl-2009]: Pearl, Judea, 2009, *Causality*, 2ⁿᵈ edn., Cambridge: Cambridge University Press.

[^pietsch-2016]: Pietsch, Wolfgang, 2016, “The Causal Nature of Modeling with Big Data”, *Philosophy & Technology*, 29: 137–171.

[^pietsch-2021]: –––, 2021, *Big Data*, Cambridge: Cambridge University Press.

[^plate-2003]: Plate, Tony, 2003, “Distributed Representations”, *Encyclopedia of Cognitive Science*, 1: 1002–1010.

[^polanyi-1966]: Polanyi, Michael, 1966, *The Tacit Dimension*, Gloucester, MA: Peter Smith.

[^prince-2023]: Prince, Simon J. D., 2023, *Understanding Deep Learning*, Cambridge, MA: The MIT Press.

[^quinn-2022]: Quinn, Thomas P., Stephan Jacobs, Manisha Senadeera, Vuong Le, and Simon Coghlan, 2022, “The Three Ghosts of Medical AI: Can the Black-Box Present Deliver?”, *Artificial Intelligence in Medicine*, 124: 102158.

[^räz-2022]: Räz, Tim, 2022, “Understanding Deep Learning With Statistical Relevance”, *Philosophy of Science*, 89(1): 20–41.

[^räz-2022-2]: Räz, Tim, and Claus Beisbart, 2022, “The Importance of Understanding Deep Learning”, *Erkenntnis*, 89(5).

[^ribeiro-2016]: Ribeiro, Marco Tulio, Sameer Singh, and Carlos Guestrin, 2016, “‘Why Should I Trust You?’ Explaining the Predictions of Any Classifier”, *Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining*, pp. 1135–1144.

[^ribeiro-2018]: Ribeiro, Marco Tulio, Sameer Singh, and Carlos Guestrin, 2018, “Anchors: High-Precision Model-Agnostic Explanations”, *Proceedings of the AAAI Conference on Artificial Intelligence*, 32(1).

[^rowbottom-2026]: Rowbottom, Darrell P., and André Curtis-Trudel, 2026, “Explaining AI’s Successes: A No Miracles Argument for Quasi-Representations”, *Synthese*, 207(4): 179.

[^rudin-2019]: Rudin, Cynthia, 2019, “Stop Explaining Black Box Machine Learning Models for High Stakes Decisions and Use Interpretable Models Instead”, *Nature Machine Intelligence*, 1(5): 206–215.

[^rudin-2022]: Rudin, Cynthia, et al., 2022, “Interpretable Machine Learning: Fundamental Principles and 10 Grand Challenges”, *Statistic Surveys*, 16: 1–85.

[^rudner-1953]: Rudner, Richard, 1953, “The Scientist Qua Scientist Makes Value Judgments”, *Philosophy of Science*, 20(1): 1–6.

[^russell-2016]: Russell, Stuart J., and Peter Norvig, 2016, *Artificial Intelligence: A Modern Approach*, 3rd edn., global edition, Boston: Pearson Education.

[^russo-2024]: Russo, Federica, Eric Schliesser, and Jean Wagemans, 2024, “Connecting Ethics and Epistemology of AI”, *AI & Society*, 39: 1585–1603.

[^ryan-2020]: Ryan, Mark, 2020, “In AI We Trust: Ethics, Artificial Intelligence, and Reliability”, *Science and Engineering Ethics*, 26: 2749–2767.

[^sanjuán-2021]: Sanjuán, Miguel AF, 2021, “Artificial Intelligence, Chaos, Prediction and Understanding in Science”, *International Journal of Bifurcation and Chaos*, 31(11): 2150173, preprint under [https://arxiv.org/abs/2003.01771v2](https://arxiv.org/abs/2003.01771v2)

[^sawyer-2004]: Sawyer, R. Keith, 2004, “Social Explanation and Computational Simulation”, *Philosophical Explorations*, 7(3): 219–231.

[^schlesinger-1979]: Schlesinger, S., R. E. Crosbie, R. E. Gagné, G. S. Inis, C. S. Lalwani, J. Loch, R. J. Sylvester, R. D. Wright, N. Kheir, & D. Bartos, 1979, “Terminology for Model Credibility”, *Simulation*, 32: 103–104.

[^schneider-2025]: Schneider, Susan, 2025, “Chatbot Epistemology”, *Social Epistemology*, 39(5): 570–589.

[^schubbach-2019]: Schubbach, Arno, 2019, “Judging Machines: Philosophical Aspects of Deep Learning”, *Synthese*, 198(2): 1807–1827.

[^schurz-2019]: Schurz, Gerhard, 2019, *Hume’s Problem Solved: The Optimality of Meta-Induction*, Cambridge, MA: MIT Press.

[^søgaard-2024]: Søgaard, Anders, 2024, “On the Opacity of Deep Neural Networks”, *Canadian Journal of Philosophy*, 53(3): 224–239.

[^sosa-2006]: Sosa, Ernest, 2006, “Knowledge: Instrumental and Testimonial”, in Jennifer Lackey and Ernest Sosa (eds.), *The Epistemology of Testimony*, Oxford: Oxford University Press, pp. 116–123.

[^soydaner-2022]: Soydaner, Derya, 2022, “Attention Mechanism in Neural Networks*”, Neural Computing and Applications*, 34(16): 13371–13385.

[^spelda-2024]: Spelda, Petr, and Vít Stritecky, 2024, “Why and How to Construct an Epistemic Justification of Machine Learning?”, *Synthese*, 204: 74.

[^starke-2021]: Starke, Georg, Rik van den Brule, Bernice Simone Elger, Pim Haselager, 2021, “Intentional Machines: A Defence of Trust in Medical Artificial Intelligence”, *Bioethics*, 36(2): 154–161.

[^steel-2010]: Steel, Daniel, 2010, “What If the Principle of Induction Is Normative? Formal Learning Theory and Hume’s Problem”, *International Studies in the Philosophy of Science*, 24(2): 171–185.

[^suárez-2004]: Suárez, Mauricio, 2004, “An Inferential Conception of Scientific Representation”, *Philosophy of Science*, 71: 767–779.

[^sullivan-2022]: Sullivan, Emily, 2022, “Understanding from Machine Learning Models”, *British Journal for the Philosophy of Science*, 73(1): 109–133.

[^sullivan-2024]: –––, 2024, “Do Machine Learning Models Represent Their Targets?”, *Philosophy of Science*, 91(5): 1445–1455.

[^suppes-1962]: Suppes, Patrick, 1962, “Models of Data”, in Ernest Nagel, Patrick Suppes, and Alfred Tarski (eds.), *Logic, Methodology and Philosophy of Science: Proceedings of the 1960 International Congress*, Stanford, CA: Stanford University Press, pp. 252–261.

[^symons-2020]: Symons, John, and Jack K. Horner, 2020, “Why There Is No General Solution to the Problem of Software Verification”, *Foundations of Science*, 25(3): 541–557.

[^teller-1980]: Teller, Paul, 1980, “Computer Proof”, *Journal of Philosophy*, 77(12): 797–803.

[^terwilliger-2024]: Terwilliger, Thomas, et al., 2024, “AlphaFold Predictions Are Valuable Hypotheses and Accelerate but Do Not Replace Experimental Structure Determination”, *Nature Methods*, 21(1): 110–116.

[^tian-2022]: Tian, Yu, and Yao Zhang, 2022, “A Comprehensive Survey on Regularization Strategies in Machine Learning”, *Information Fusion*, 80: 146–166.

[^tonekaboni-2019]: Tonekaboni, Sana, Shalmali Joshi, Melissa D. McCradden, and Anna Goldenberg, 2019, “What Clinicians Want: Contextualizing Explainable Machine Learning for Clinical End Use”, in *Machine Learning for Healthcare Conference, PMLR 106:* 359–380.

[^trinh-2024]: Trinh, T. H., Y. Wu, Q. V. Le, et al., 2024, “Solving Olympiad Geometry without Human Demonstrations”, *Nature*, 625: 476–482.

[^trout-2002]: Trout, J., 2002, “Scientific Explanation and the Sense of Understanding”, *Philosophy of Science*, 69: 212–233.

[^tymoczko-1979]: Tymoczko, Thomas, 1979, “The Four-Color Problem and its Philosophical Significance”, *Journal of Philosophy*, 76(2): 57–83.

[^fraassen-1980]: van Fraassen, Bas, 1980, *The Scientific Image*, Oxford: Oxford University Press.

[^vapnik-2000]: Vapnik, Vladimir, 2000, *The Nature of Statistical Learning Theory*, 2ⁿᵈ ed. New York: Springer.

[^varadi-2024]: Varadi, Mihaly, et al., 2024, “AlphaFold Protein Structure Database in 2024: Providing Structure Coverage for Over 214 Million Protein Sequences”, *Nucleic Acids Research*, 52(D1): D368-D375.

[^vaswani-2017]: Vaswani, Ashish, et al., 2017, “Attention Is All You Need”, *Advances in Neural Information Processing Systems*, 30.

[^wang-2023]: Wang, Hanchen, et al., 2023, “Scientific Discovery in the Age of Artificial Intelligence”, *Nature*, 620(7972): 47–60.

[^watson-2019]: Watson, David, 2019, “The Rhetoric and Reality of Anthropomorphism in Artificial Intelligence”, *Minds & Machines*, 29: 417–440.

[^watson-2023]: –––, 2023, “On the Philosophy of Unsupervised Learning”, *Philosophy and Technology*, 36: 28.

[^watson-2021]: Watson, David, and Luciano Floridi, 2021, “The Explanation Game: A Formal Framework for Interpretable Machine Learning”, *Synthese*, 198: 9211–9242.

[^wei-2022]: Wei, Jason, et al., 2022, “Chain-of-Thought Prompting Elicits Reasoning in Large Language Models”, *Advances in Neural Information Processing Systems*, 35: 24824–24837.

[^weisberg-2013]: Weisberg, Michael, 2013, *Simulation and Similarity: Using Models to Understand the World*, New York: Oxford University Press. [https://doi.org/10.1093/acprof:oso/9780199933662.001.0001](https://doi.org/10.1093/acprof:oso/9780199933662.001.0001)

[^weiss-2016]: Weiss, Karl, Taghi M. Khoshgoftaar, and DingDing Wang, 2016, “A Survey of Transfer Learning”, *Journal of Big Data*, 3(1): 9.

[^weizenbaum-1966]: Weizenbaum, Joseph, 1966, “ELIZA—A Computer Program for the Study of Natural Language Communication Between Man and Machine”, *Communications of the ACM*, 9(1): 36–45.

[^winsberg-1999]: Winsberg, Eric, 1999, “Sanctioning Models: The Epistemology of Simulation”, *Science in Context*, 12(2): 275–292

[^winsberg-2001]: –––, 2001, “Simulations, Models, and Theories: Complex Physical Systems and their Representations”, *Philosophy of Science*, 68: 442–454.

[^winsberg-2009]: –––, 2009, “A Tale of Two Methods”, *Synthese*, 169(3): 575–592.

[^winsberg-2018]: –––, 2018, *Philosophy of Climate Science*, Cambridge: Cambridge University Press.

[^winsberg-2026]: Winsberg, Eric, and Ramon Alvarado, 2026, “Computer Simulations in Science”, *The Stanford Encyclopedia of Philosophy*, (Spring 2026 Edition), Edward N. Zalta & Uri Nodelman (eds.), URL = <[https://plato.stanford.edu/archives/spr2026/entries/simulations-science/](https://plato.stanford.edu/archives/spr2026/entries/simulations-science/)>. .

[^wolfram-2023]: Wolfram, Stephen, 2023, *What Is ChatGPT Doing … and Why Does It Work?*, Champaign, IL: Wolfram Media, Inc.

[^zagzebski-2012]: Zagzebski, Linda Trinkaus, 2012, *Epistemic Authority: A Theory of Trust, Authority, and Autonomy in Belief*, New York: Oxford University Press.

[^zednik-2021]: Zednik, Carlos, 2021, “Solving the Black Box Problem: A Normative Framework for Explainable Artificial Intelligence”, *Philosophy & Technology*, 34: 265–288.

[^zednik-2022]: Zednik, Carlos, and Hannes Boelsen, 2022, “Scientific Exploration and Explainable Artificial Intelligence”, *Minds & Machines*, 32: 219–239.

[^zerilli-2022]: Zerilli, John, 2022, “Explaining Machine Learning Decisions”, *Philosophy of Science*, 89(1): 1–19.

[^zhai-2024]: Zhai, Chao, Samuel Wibowo, and Liyan Li, 2024, “The Effects of Over-Reliance on AI Dialogue Systems on Students’ Cognitive Abilities”, *Smart Learning Environments*, 11(1): 28.

[^zhang-2017]: Zhang, Chiyuan, Samy Bengio, Moritz Hardt, Benjamin Recht, and Oriol Vinyals, 2017 [2021], “Understanding Deep Learning Requires Rethinking Generalization”, *ArXiv*, 1611.03530 [CS], updated as “Understanding Deep Learning (Still) Requires Rethinking Generalization”, *Communications of the ACM*, 64(3): 107–115.
