# Semantic Conceptions of Information
**First published Wed Oct 5, 2005; substantive revision Fri Jan 14, 2022**

*Sequoiah-Grayson, Sebastian, Floridi, Luciano*

Information is a rich commodity. It is perhaps the richest of them all. It is by now almost post-truistic that interested parties, from individuals, to large-scale globalised private actors and nation states, will go to extraordinary lengths to protect and to acquire information. If we allow ourselves to engage in a little armchair etymology, then something’s being in *formation* is just for it to be non-random. Indeed this armchair etymology gets straight to the heart of how it is that we often speak of information, as a contrast to randomisation. Indeed “signal-to-noise ratio” may be restated as “information-to-noise ratio”, hence the ubiquity of the refrain “That is not information, it is just noise”.

Another way of putting this is to say that information is a non-random distinction with a difference. Information supervenes on patterned deviations, and getting information from one’s environment depends on one being able to recognise and exploit these patterns. That one part of our environment may carry information about another part of our environment depends on our environment behaving in reliable, non-randomised way. Our ability to use information at one part of our environment to access information at another part of it depends not only on our ability to recognise patterned regularities, but on our ability to recognise connections between such regularities.

For example, for us to access the distal information that there is fire from the proximal information that there is smoke, we must be aware of the correlation between smoke and fire. That we do is marked by maxims such as ”smoke means fire”. Such correlations of natural meaning between events in the world is studied by the Mathematical Theory of Communication (MTC) due to Shannon and Weaver (see the entry on information). This is the “industry standard” account of information, as analysed by communications engineers. What of the information encoded by natural language however? What of information in this more concretely semantic sense? A semantic conception of information will not investigate the mere surprise value of a signal given the likelihood of the signal itself (as does MTC). Instead, it will investigate the nature of the information carried by, or encoded by the messages transmitted themselves. Another way of approaching the issue is to understand such semantic conceptions of information to be concerned with the investigation of the *informational content of* a piece of language of some sort. Such pieces of language might be propositions, singular terms, descriptions, and so on.

The first theory of such a semantic conception of information that was articulated in detail was Bar-Hillel and Carnap’s *theory of semantic information*. It is fitting then that we start here in section 1. In section 1.1 we will see how the theory of semantic information has some consequences for certain types of statements, namely logical truths and contradictions, that many have found counterintuitive. In section 1.2 we will see how Floridi responds to these problems, as well how others have extended and responded to Floridi’s proposal that we accept the *veridicality thesis*—that information be factive. A number of such responses are motivated by realist and naturalist considerations with regard to the ontology of semantic information. In section 2 we will look at semantic conceptions of information that take naturalist metaphysics seriously. Here we will see how Fodor, Dretske, Evans, Lewis, Recanati, and Jackson propose and defend semantic conceptions of information that turn on modes of presentation, and that are broadly naturalist insofar as they attempt to subsume information within causal relations of various sorts. Any causal theory of meaning or knowledge will face the problem of accounting for the meaning of, and our epistemic access to, abstract objects.

Most of the theories of broadly semantic information outlined in section 2 appeal to information channels in one sense or another (with a channel being a relation allowing information the flow from one state to another). In section 3 we will look at theories of information channels directly. (For a detailed examination of the formal properties of the theory of information channels, as well as how it is that the theory connects with other issues in logic and information more generally, see the entry on logic and information.) We will see how the original theory of information channels due to Barwise and Perry emerged from Austin’s theory of semantic content, as well as how it is that the theory of information channels has been developed and extended in order to give a semantics for information flow itself, as well as informational semantics for natural language fragments and epistemic phenomena.

## 1. Bar-Hillel and Carnap’s Theory of Semantic Information

The most natural starting point for any overview of semantic conceptions of information is Carnap and Bar-Hillel’s “An Outline of a Theory of Semantic Information” (1952). Bar Hillel and Carnap’s theory of semantic information is a quantitative theory that emerged from more general theories of information (see section 4.2 on Shannon in the entry on information). Their theory was designed with the goal of giving us a usable framework for calculating the *amount* of semantic information encoded by a sentence in a particular language. In their case the language in question is monadic predicate logic. The philosophical details are grounded on an idea that has come to be known as the *inverse range principle* (IRP). Loosely, IRP states that the amount of information carried or encoded by a sentence is inversely proportional to something else, where this something else is something to which one can attach a precise numerical value. Once this has been done, one can use this numerical value to calculate the measure of semantic information as understood by the theory of semantic information.

For Bar-Hillel and Carnap, *the amount of semantic information encoded by a sentence is inversely proportional to the likelihood of the truth of that sentence*. So for them, the likelihood of truth is the “something else” to which we can attach a precise numerical value. To illustrate, we start with their method of calculating a qualitative individuation of semantic information, *content* or “Cont”.

Where $s$ is a sentence and $W$ is the set of all possible worlds, content is defined as follows:

$$\tCont(s) := \{x\in W : x\vdash \neg s\}$$

Given that the *intension* of a sentence $s$ is the set of all worlds in which the sentence if *true*, and that the content of a sentence is the set of all worlds in which $s$ is *false*, the intension and the content of a sentence $s$ form a partition on the set of all worlds $W$.

Bar-Hillel and Carnap define two distinct methods for *quantitative* calculations of semantic information—a *content measure* (cont), and an *information measure* (inf). They start with an *a priori* probability measure of a sentence $s$, $p(s)$, which is gotten from an *a priori distribution*. The *a priori* distribution onto $W$ sums to 1, and we assume that all assignments are equiprobable, hence the *a priori* probability measure is the value of $p(s)$ that results from this distribution. In this case, *cont* and *inf* can be defined as follows:

$$\begin{align} \tcont(s) &:= 1 - p(s)\\ \inf(s) &:= \log_2\frac{1}{1 - \tcont(s)} \end{align}$$

The two measures are required for technical reasons—in order to capture additivity on *content independence* and *inductive independence* respectively. Two sentences $s$ and $s'$ are content independent when they do not have any worlds in common. Two sentences $s$ and $s'$ are inductively independent when the conditional probability of each sentence given the other is identical to their initial unconditional probability. Additivity on inductive independence fails for cont, since it might be the case that $\tcont(s\wedge s') \neq \tcont(s) + \tcont(s')$ on account of $p(s)$ and $p(s')$ having worlds in common—that is, on account of them not being content independent in spite of their being inductively independent. For additivity to hold on cont, it is *content independence*, as opposed to inductive independence that is required. By contrast, additivity on inductive independence does not fail for inf. Bar-Hillel and Carnap’s proof is non-trivial (found on their 1952: 244–5).

### 1.1 Problems for the theory of semantic information

Technical matters aside, some philosophical issues are immediate. Firstly, how do we know in practice how many possible words there are? If we are talking about the number of possible worlds with respect to all possible sentences in English, then there will be infinitely many of them. Bar-Hillel and Carnap avoided this issue by talking exclusively about the semantic information encoded by sentences formulated in monadic predicate logic with a finite number of predicate letters. Where there are $n$ predicate letters, there will be $2^n$ possible objects, exhausting all possible predicate combinations. There will then be $2^{2^n}$ possible worlds (“state descriptions” in Bar-Hillel and Carnap’s parlance), corresponding to all possible combinations of possible objects. Hintikka (1970, 1973)[^hintikka-1970][^hintikka-1973], extended Bar-Hillel and Carnap’s theory of semantic information from monadic predicate logic to fully general predicate logic.

Thirdly and more generally, Bar-Hillel and Carnap’s theory of semantic information has give rise to two problems of strong significance philosophically.

- The Bar-Hillel and Carnap Semantic Paradox (BCP)
- The Scandal of Deduction (SOD)

BCP refers to the fact that Bar-Hillel and Carnap’s theory of semantic information assigns maximal information to contradictory sentences. Where $\perp$ is an arbitrary contradiction, given that $\perp$ will be false in all possible worlds, we have the following via (1), (2), and (3) respectively:

$$\begin{align} \tCont(\perp) &= W\; (\text{i.e., maximal content})\\ \tcont(\perp) &= 1\\ \inf(\perp) &= \infty\end{align}$$

Bar-Hillel and Carnap (1952: 229)[^carnap-1952] responded to this situation as follows:

> It might perhaps, at first, seem strange that a self-contradictory sentence, hence one which no ideal receiver would accept, is regarded as carrying with it the most inclusive information. It should, however, be emphasised that semantic information is here not meant as implying truth. A false sentence which happens to say much is thereby highly informative in our sense. Whether the information it carries is true or false, scientifically valuable or not, and so forth, does not concern us. A self-contradictory sentence asserts too much; it is too informative to be true.

There are two dimensions to this response that have caused concern in philosophical circles. The first is that their notion of semantic information is *non-factive*—semantic information does not need to be true. The second is that they are taking their notion of semantic information to underpin informativeness in some non-trivial sense.

SOD refers to the fact philosophical accounts of information are yet to give an account of the informativeness of logical truths and deductive inferences. Bar-Hillel and Carnap’s theory of semantic information assigns minimal information to logical truths (and valid deductive inferences can be transformed into logical truths by conjoining the premises into an antecedent of a conditional that takes the conclusion as its consequent). Where $\top$ is an arbitrary tautology, given that $\top$ will be false in all possible worlds, we have the following via (1), (2), and (3) respectively:

$$\begin{align} \tCont(\top) &= \varnothing\\ \tcont(\top) &= 0\\ \inf(\top) &= 0\end{align}$$

With respect to logically true sentences returning a minimal information value, Bar-Hillel and Carnap (1952: 223)[^carnap-1952] respond as follows:

> This, however, is by no means to be understood as implying that there is no good sense of ‘amount of information’ in which the amount of information of these sentences will not be zero at all, and for some people, might even be rather high. To avoid ambiguities, we shall use the adjective ‘semantic’ to differentiate both the presystematic sense of ‘information’ in which we are interested at the moment and their systematic explicata from other senses (such as “amount of psychological information for the person P”) and their explicata.

We will return to SOD briefly in section 3.2 below. Note here however that Hintikka (1970, 1973)[^hintikka-1970][^hintikka-1973] mounted a technically heroic if ultimately unsuccessful attempt to solve it (see Sequoiah-Grayson (2008)[^sequoiah-grayson-2008]), and for a properly detailed investigation, see the entry on logic and information. For now we must recognise that the response of Bar-Hillel and Carnap above brings with it some noteworthy philosophical claims of its own. Firstly, Bar-Hillel and Carnap are suggesting that the type of information which is encoded by logical truths and for which the amount encoded is non-zero, is psychological in some sense or other. Furthermore, it may vary for one person from the other even with respect to the same logical truth. Secondly, they are heeding the following advice of Claude Shannon, the originator of the mathematical theory of communication, given just two years earlier.

> The word ‘information’ has been given different meanings by various writers in the general field of information theory. It is likely that at least a number of these will prove to be useful in certain applications to deserve further study and permanent recognition. It is hardly to be expected that a single concept of information would satisfactorily account for the numerous possible applications of the general field. (1950 [1993: 180]).

Shannon is advocating a rich *informational pluralism*, for a detailed development of which see Allo (2007)[^allo-2007]. Shannon’s advice on this point was, as we are about to see, nothing if not prescient.

### 1.2 Floridi’s theory of strongly semantic information

Luciano Floridi’s theory of *strongly semantic information* (2004, 2005), is a response to BCP motivated by the belief that something has gone essentially amiss with Bar-Hillel and Carnap’s theory. The suspicion is that their theory is based on a semantic principle that is too weak, *namely that truth-values are independent of semantic information*. Floridi’s proposal is that an approach according to which semantic information is factive can avoid the paradox, and that the resulting theory is more in line with our ordinary conception of what generally counts as information. The line of argument is that a theory of strongly semantic information, based on alethic and discrepancy values rather than probabilities, can successfully avoid BCP. Relatedly, see Bremer and Cohnitz (2004: chap. 2) for an overview of Floridi’s theory to be described below, and Sequoiah-Grayson (2007)[^sequoiah-grayson-2007] for a defence of the theory of strongly semantic information against independent objections from Fetzer (2004)[^fetzer-2004] and Dodig-Crnkovic (2005)[^dodig-crnkovic-2005].

Before we expound Floridi’s approach, note that some have proposed a different alethic approach, one that uses truthlikeness, or verisimilitude, to explicate the notion of semantic information—Frické (1997)[^frické-1997], Cevolani (2011, 2014)[^cevolani-2011][^cevolani-2014], and D’Alfonso (2011)[^d’alfonso-2011]. Typically these seek to identify factual information with likeness to the complete truth about all empirical matters or about some restricted relevant domain of factual interest. These also avoid the BCP, and also do not use probabilities. However, truthlikeness is different from truth itself in as much as a truth bearer can be truth-like without actually being true, i.e., while being false, so that verisimilitude accounts of information can permit that false claims may possess information. Indeed false statements can sometimes carry more information than their true negations on this account, see Frické (1997)[^frické-1997].

By contrast, Floridi’s strongly semantic factive information is defined as well-formed, meaningful, and *truthful* data. This latter factivity constraint on semantic information has come to be known commonly as the *veridicality thesis* (VT) (prefigured in Mingers (1995, 1996a, 1996b)[^mingers-1995][^mingers-1996a][^mingers-1996b]). Importantly, versions of VT arise in debates about the ontological status of information in general, not merely with regard to semantic information in particular—see Dretske (1981)[^dretske-1981] for a classic example. Once the content is so defined, the quantity of strongly semantic information in a proposition $p$ is calculated in terms of the distance of $p$ from a situation $z$ (where situations are partial or incomplete worlds) that $p$ is supposed to model.

When $p$ is true in all cases, but also when $p$ is false in all cases, there is maximal distance (as opposed to maximal closeness) between $p$ and the situation $z$ that $p$ is supposed to model. By contrast, *maximum closeness* is equivalent to the precise modelling of $z$ at the agreed level of abstraction or descriptive adequacy. *Maximal distance* in the direction of truth will result in $p$ being true in all cases in which case $p = \mathord{\top}$ and is minimally informative. Similarly, maximal distance in the direction of falsity results in $p$ being false in all cases (all possible situations or probability 0) in which case $p = \mathord{\perp}$ and is minimally informative also. The important difference here is that any distance in this direction is distance *bereft of strongly semantic information entirely*. This is on account of distance in the direction of “the false” violating the factivity condition on strongly semantic information.

Floridi distinguishes *informativeness* from strongly semantic information itself. This is welcome, since strongly semantic information is factive, whereas false statements can still be informative. Indeed a false statement $s$ may be *more informative* than a true statement $s'$, in spite of the fact that $s'$ carries strongly semantic information whereas $s$ does not. By way of example, suppose that you are running a catering contract for an event, and that there will in fact be exactly 200 people in attendance. Suppose that $s$ is *there will be 201 people in attendance*, and $s'$ is *there will be between 100 and 200 people in attendance*. $s'$ is true whilst $s$ is false, but $s$ is more informative than $s'$ on any natural understanding of the concept informative.

Where *σ* is a piece of strongly semantic (hence true) information, and $z$ is the target situation that it describes with total accuracy, the more distant *σ* gets from $z$, the larger the number of situations to which it applies and the lower its degree of informativeness. Floridi uses ‘*Θ*’ to refer to the distance between a true *σ* and $z$ (recall that Floridi is not interested in non-factive information, and might well deny that there is any sensible such commodity). *Θ* indicates the degree of support offered by $z$ to *σ*. Given a specific *σ* and a corresponding target $z$, Floridi maps the values of *Θ* onto the x-axis of a Cartesian diagram. We now need a formula to calculate the degree of informativeness *ι* of *σ*—$\iota(\sigma)$—in relation to $\Theta(\sigma)$. Floridi’s proposal is that we calculate the value of $\iota(\sigma)$ via the complement of the distance of $\Theta(\sigma)$ squared:

$$\iota(\sigma) = 1 - \Theta(\sigma)^2$$

Values of *ι* range from 0 to 1 and are mapped along the y-axis of the Cartesian diagram. Figure 1 shows the graph generated by (10) when we include negative values for false *σ*. *Θ* ranges from $-1 = \mathord{\perp}$ to $1 = \mathord{\top}$:

![A graph with a curve starting at (-1,0), labelled necessarily false, rising to (0,1) then falling to (1,0), labelled necessarily true; the quadrant for x less than 0 is labelled inaccuracy; the quadrant for x greater than 0 is labelled vacuity. The rest is explained above](../assets/information-semantic/informativeness.svg)

\*Figure 1\*

#### Responses and extensions

Floridi (2012)[^floridi-2012] extends the theory of strongly semantic information into matters of traditional epistemology. His *network theory of account* involves an argument for the claim that should strongly semantic information be embedded within a network of questions and answers that account for it correctly, then this is necessary and sufficient for the strongly semantic information to count as *knowledge*. Floridi (2008)[^floridi-2008] develops a theory of *relevant* semantic information in order to articulate a theory of *epistemic relevance*. Here he argues that the nature of relevant semantic information is an additional vindication of the veridicality thesis. In Floridi (2011)[^floridi-2011] he further explores just what it might, or should mean for semantic information to be true. Rather than accept a correspondence, coherence, or pragmatic theory of truth, he develops what he calls a *correctness theory of truth* for the veridicality thesis, one which connects directly with his network theory of account described above.

Floridi (2006)[^floridi-2006] argues that the modal logic KTB is well placed to play the role of a logic of *being informed* (KTB is system **B** described in the entry on modal logic.) KTB itself licenses a version of the veridicality thesis within the context of being informed, $I_\alpha p\to p$ (where $I$ is a universal modal operator, on account of the axiom $\square p\to p$ being an axiom of KTB). “Being informed” is understood as a cognitive state distinct from both knowledge and belief. Allo (2011)[^allo-2011] provides a formal semantics for the logic of being informed, in both pure and applied versions. Primiero (2009)[^primiero-2009] rejects the veridicality thesis for a logic of *becoming* informed. Primiero’s logic of becoming informed is a logic of epistemic constructive information, within which the definition of information requires it to be kept distinct from truth. Epistemic constructive information understands information for propositional content in terms of proof-conditions as opposed to truth-conditions.

More broadly, Dinnen and Brauner (2015) search for a single definition of information (be it semantic or not) and find the veridicality thesis to be obstructive. By contrast, Mingers and Standing (2018) argue for a single definition of information that supports the veridicality thesis. Allo (2007)[^allo-2007] preempts such concerns with an argument for an *informational pluralism* (analogous to a logical pluralism, see the entry) via a *realist* interpretation of semantic information itself. A realist interpretation of semantic information leads naturally to the question of how it is that semantic information can emerge from and be a part of the natural world—a question that is addressed in detail in Vakarelov (2010)[^vakarelov-2010]. The question of how it might be that information could be accounted for naturalistically has a rich history in philosophy, most notably in *informational semantics* covered in the following section.

Although Floridi’s, and Bar-Hillel and Carnap’s stance on semantic information is not uncontroversial ( *sans* an informational pluralism that is), Floridi’s motivating intuition has some philosophical precedent. Firstly, it is unlikely that many are satisfied with Bar-Hillel and Carnap’s claim that “A self-contradictory sentence asserts too much; it is too informative to be true”. Secondly, with regard to logical truths having zero semantic information on Floridi’s account, recall that as Wittgenstein put it with typical bluntness—“All the propositions of logic say the same thing, viz nothing. They are tautologies” (*Tractatus*, 4.46, 6.1). One way to understand Floridi’s theory of strongly semantic information is as a theory of the information we get from and about our particular objective physical environment, as our physical environment is one about which contradictions and logical truths are typically maximally uninformative. Semantic conceptions of information designed to tell a naturalistic story about the content of our putatively referring terms have a rich history of their own in philosophy, and this is the topic to which we now turn.

## 2. Information, Modes of Presentation, and Meaning

Theories of meaning that turn on modes of presentation have been common in philosophy in one way or another since Frege’s *Sense and Reference*. The story is as follows. There must be more to the meaning of a referring term than its referent, since terms can co-refer. For example, *James Newell Osterberg Jr.* and *Iggy Pop* both refer to the same individual. In spite of this the intuition that they do not mean the same thing is strong. “Iggy Pop is Iggy Pop” and “Iggy Pop is James Newell Osterberg Jr.” do not *seem* to mean the same thing. Similarly, it seems to be the case that “Alice believes that Iggy Pop was the singer in The Stooges” might true, whilst “Alice believes that James Newell Osterberg Jr. was the singer in The Stooges” might be false, at least on one natural reading that is in line with our intuitions with regard to meanings.

Frege’s well known response is that both the referent and the sense of a referring term play a role in specifying its semantic content. But what is the sense of a term? Frege’s own way of cashing out the notion of sense is in terms of a *mode of presentation* (MOP), an idea used by many later philosophers. The MOP of a referring term is the way in which the putative referent of the term is presented to us by our phenomenology. MOPs are what we would use in an attempt to identify or locate the referent of a referring term whose meaning we grasp. Many contemporary theories of meaning that turn on information, incorporate MOPs in one way or another. The reason for this is that although reducing the meaning of a term to the information carried or transmitted by it alone is attractive, it has proven to be fraught.

The temptation to take meaning and information to amount to pretty much the same thing is a result of the following idea. The idea is that the word ‘cat’ denotes the property of being a cat, and that it means *cat* because it expresses the concept cat, and the concept cat means *cat*. The concept cat means *cat* because it carries the information $\langle$cat$\rangle$, and cat carries the information $\langle$cat$\rangle$ because its instances or tokenings are caused, by and large, by cats. This is a nice idea. By tying meaning and information together and telling a *causal* story about them, we have a naturalistic story to tell about the information that we get from our environment, and hence a naturalistic story to tell about meaning. Such information-transmitting causal relationships are *information channels*—causal connections that facilitate the flow of information between the source of information and the receiver. We should take care to note this story is telling an informationally semantic story about sub-propositionally located pieces of information such as the predicate ‘cat’ and paradigmatic uses of singular terms. As such it sits outside of the domain described by the theories of semantic and strongly semantic information described above. In spite of this, we will see that a refinement of this story turns on tracking *accuracy*, if not truth itself.

In a series of influential works on this area of informational semantics, Jerry Fodor (1990)[^fodor-1990], and Fred Dretske (1981)[^dretske-1981] proposed a theory of semantics very much like the one outlined above (see the entry on causal theories of mental content). A noted problem for such an informational semantics has come to be known commonly as the *disjunction problem*. The disjunction problem is as follows. cat tokens are not always caused by cats, they are sometimes caused by other things like small dogs for example (or by thoughts about balls of yarn or whatever). Given this fact, if the story above is correct, then why does cat mean *cat* and not *cat or dog*? Fodor’s (1990)[^fodor-1990] response is in two stages.

Firstly, Fodor’s initial proposal is that non cat-caused tokens of cat are asymmetrically dependent on cat-caused tokens of cat. That is, there would not be any non cat-caused tokens of cat had there not been any cat-caused tokens of cat. Secondly, on Fodor’s picture, meaning and information *come apart*. The *information* carried by a token of a concept covaries with its cause, whereas the *meaning* of a token is what all of the concept’s tokenings have in common—the inner vehicles of our cat tokenings, or their MOPs. Note that Fodor is not, strictly speaking, subsuming information as part of meaning, but rather teasing them apart. Our failure to appreciate that meaning and information come apart is, according to Fodor, a consequence of the fact that firstly, they are very often coextensive, and that secondly, ‘means’ is a homonym for both semantic content (meaning) and information-carrying. Consider the following two uses of “means”:

- Smoke means fire.
- ‘Smoke’ means *smoke*.

On Fodor’s view, the first use is in the sense of information-carrying only. Smoke carries the information that there is fire, but that is not what it means semantically. What ‘smoke’ means, in the semantic sense, is *smoke*, and this is captured by the latter use of “means” above. On Fodor’s story, just as with ‘cat’ above, ‘smoke’ means *smoke* because it expresses smoke, and tokenings of smoke are caused paradigmatically (but not always!) by smoke itself. The “not always” qualification is covered by the asymmetric dependence condition above. So far so good, but what about non-existent objects such as bunyips? Non bunyip-caused bunyip tokens of bunyip cannot be asymmetrically dependent on bunyip-caused bunyip tokens of bunyip because there are no bunyips around to cause anything at all.

In light of non-existent objects such as bunyips, and the meaningfulness of bunyip tokens in spite of there being no bunyips, Fodor adjusts his proposal so that meaning now rests on *asymmetrical dependences among nomological relations among properties*—the property of being a bunyip for example—as opposed to *actual* causal relations between individuals. Nomological relations are cashed out in terms of counterfactuals, so what we have now is an informational semantics along the lines of the following—bunyip means *bunyip* because if there *were* bunyips, bunyips *would be* the cause of bunyip tokens on which all other causes would depend asymmetrically.

Recall again that Fodor is teasing meaning and information apart. Gareth Evans (1982)[^evans-1982] formulates a similar informational theory of meaning, but one where information and MOPs are both subsumed within the semantic story itself. For Evans, a full story about the meaning of thoughts about particular objects that are—putatively at least—in the world, needs to take account of both the causal origins of the thought, as well as the MOP engendered by it. Evans calls such thoughts *information based particular thoughts*, and such thoughts will be *well grounded* if and only if the object satisfying the MOP and the object at the source-end of the causal route are one and the same thing.

What the Fodor/Dretske and Evans theories of informational semantics have in common, is that they recognise that the meaning or content/object of a thought is robust across causal variation:

> We want to be able to say that two informational states (states of different persons) embody the same information, provided that they result from the same initial informational event. (Evans 1982: 128–129)[^evans-1982]
>
> Informational theories…appeal to reliable covariances while quantifying over the causal mechanisms by which these covariances are sustained. By doing so, they explain why information (indeed, why the very same information ) can be transmitted over so many different kinds of channels. (Fodor 1990: 100)[^fodor-1990]

Moreover, although Evans did not put things in quite these terms, Fodor, Dretske, and Evans all recognise *information channels* as robust entities in their own right.

François Recanati (2012, 2016)[^recanati-2012][^recanati-2016], has proposed a detailed version of informational semantics, his *mental files* theory, within which information channels play a central role. Recanati’s mental files are cognitive counterparts to singular terms, and as such are referring concepts. Recanati’s view looks very similar to Evan’s information based particular thoughts at first glance. However, on Recanati’s view, metal files contain information *in the form of MOPs of an object*—be they given directly and experientially, or indirectly via descriptions—their reference is not fixed by the information that they contain/their modes of presentation. Rather, the reference of a metal file is fixed by the relations *on which* this file is based, and the referent of a mental file will be the entity or object with which we are acquainted correctly in virtue of such relations obtaining. So Recanati is allowing that MOPs contain information themselves, rather than restrict the role of information to the reference fixing relation itself (as do Evans and Fodor). The feature that identifies these relations is that they are *epistemically rewarding* (ER) relations. For Recanati, a relation is an ER relation in virtue of the fact that it is the sort of relation that makes the *flow of information possible*. In other words, ER relations are *information channels*.

Recanati’s ER relations draw heavily on Lewis’s (1983)[^lewis-1983] relations of “epistemic rapport”—causal chains that would permit information flow, or information channels under another name. Both Recanati and Lewis recognise the disjunction problem by allowing that both information and misinformation may be transmitted along information channels. Recanati’s take is that the reference of a mental file is fixed by the object that sits at the distal end of the information channel that contributes to the information that the mental file contains, irrespectively of the “fit”. Fit may of course be bad on account of noisy channels and/or misidentification on the agent’s behalf. As Recanati puts it:

> The role of a mental file based on a certain acquaintance relation is to store information acquired in virtue of that relation. The information in question need not be veridical; we can think of it in terms, simply, of a list of predicates which the subject takes the referent to satisfy. The referent need not actually satisfy the predicates in question, since the subject may be mistaken. Such mistakes are possible because what determines the reference is not the content of the file but the relevant relation to the object. The file corresponds to an information channel, and the reference is the object from which the information derives, whether that information is genuine information or misinformation. (2012: 37–38)

It reads here as though Recanati is conflating a mental file on the one hand, with the information channel that carries its informational payload. Indeed Recanati goes on to argue that there are two sensible and “distinct notions of file” (p. 82). The first notion is simply a repository of evolving information that appears to be and may be about a single distinct object. The second notion of file, what Recanati calls the “proper notion”, involves *both* a specific relevant information channel, *and* the repository of information acquired via that channel.

Along with Fodor, Dretske, Evans, Recanati, and Lewis, Frank Jackson (2010)[^jackson-2010] also articulates a semantic theory based upon information channels that supervene on causal relations, along with MOPs. Jackson’s MOPs are identified with *descriptions*. Jackson’s description theory of reference for proper names turns on information channels, which are articulated in terms of causal links that underpin information flow. Jackson’s motivating idea is that names are by and large sources of information about the entities that they name. The descriptive dimension is a function of their (the descriptions) being specified in terms of information-carrying causal connections—information channels.

For Jackson, language is, in general, a representational system that transmits information about the way that things are taken to be to those who comprehend the language. When names are used in declarative sentences, speakers are representing things as being a certain way. The use of names in such contexts is to deliver putative information about the way things are to other speakers in the language community. According to Jackson, names do this as a function of their being parts of information channels that exist between users of the language, and the world. In order for us to track the information channel itself for the purposes of getting information from it, we must understand the structured connection between linguistic items (words and sentences), and ways that the world might be. Names themselves facilitate this practice in virtue of their being elements in the information channels that exist between us and the world. These channels are created by conventions of language use and established practices of baptism.

Given the ubiquity of information channels in the theories above, it is no surprise that information channels have become a topic of study on their own terms. The theory of information channels has made contributions to information-based analysis of natural language and formal semantics.

## 3. The Theory of Information Channels

The theory of information channels, *channel theory*, emerged from situation semantics (see the entry), with the latter being motivated by the observation that meaning depends on systematic regularities in the world, and that such regularities are a necessary condition on our grasping any meanings at all (Barwise 1993)[^barwise-1993]. Jon Barwise and John Perry (1983) appealed to this observation in order to justify and motivate a naturalistic theory of meaning. Early work in situation theory concentrated on situations themselves, thought of best as *partial worlds* in modal parlance. Importantly, situation theory itself dealt with the formal side of things in terms of set theory as opposed to modally, although as we will see below, modal interpretations have come to dominate.

Situation theory focused on *constraints* early on, with constraints thought of most usefully as *conditionals*. Situation theory builds its semantic theory on an Austinian theory of truth—where an utterance $u_s$ of a declarative sentence $s$ is putting forward a claim that is about some type of situation $x$, such that $x$ is of some type *φ* (Barwise 1993: 4)[^barwise-1993]. Austin (1950)[^austin-1950] calls the type *φ* the descriptive content of $s,$ with *φ* specifying the type of situation (or event or thing etc.) in the world that is being described. He calls the situation $x$ itself the *demonstrative content of $s$*. In other words, *φ* describes the content of $s$, and $x$ is the content *demonstrated* by $s$—which is just to say that it is the part of the world about which the utterer of $u_s$ is speaking when they utter $s$.

According to Barwise, for any conditional statement *if $s_1$ then $s_2$*, such that the descriptive content of $s_1$ is of type *φ*, and the descriptive content of $s_2$ is of type *ψ*, the descriptive content of *if $s_1$ then $s_2$* is the constraint $\phi\to\psi$. Constraints are connections between types. The *demonstrative content* of *if $s_1$ then $s_2$* will be a connection between the demonstrative contents of $s_1$ and $s_2$. Supposing that $x$ is the demonstrative content of *φ*, and $y$ is the demonstrative content of *ψ*, the demonstrative content of *if $s_1$ then $s_2$* will be a connection between $x$ and $y$, with this connection being an *information channel* $c$ between $x$ and $y$, written $x\cmapsto y$. As Barwise puts it succinctly:

> By an *information channel*, let us mean one of these relations between situations, since it is these relations which allow information about one situation to be gleaned from another situation. (1993: 5)

The proposal in sum is that when we express a constraint $\phi\to\psi$ by way of uttering *if $s_1$ then $s_2$*, we are making a claim to the effect that *there is an information channel supporting the constraint*. For an information channel to support a constraint, Barwise’ proposal is the following:

$$\text{If }x\vDash\phi, \:x\cmapsto y,\text{ and } \phi\to\psi, \text{ then } y\vDash \psi$$

(11) states that if information of type *φ* is true at the situation $x$, and there is an information channel $c$ from the situation $x$ to the situation $y$, and there is a constraint from information of type *φ* to information of type *ψ*, then information of type *ψ* is true at the situation $y$.

Barwise refines the notion of a situation to that of “site”—a structured object that contains information. We now have sites $x,$ $y,$ $z,$… and types $\phi,$ $\psi,$…, where $x:\phi$ is read as *the information site $x$ is of type* *φ*. With the qualification that the channels may or may not be among the sites, and that $x\cmapsto y$ is a three-place (ternary) relation between information sites and channels. Barwise formulates the *Soundness Axiom* for channel theory as follows:

$$c: \phi\to\psi \text{ iff } \text{ for all sites } x, y, \text{ if } x\cmapsto y\text{ and } x:\phi, \text{ then } y:\psi.$$

At this stage, things are starting to look decidedly *modal* in spirit, if not in practice.

Barwise and Perry’s *situations* and Austin’s *demonstrative contents*, are simply partial worlds under a different name. That is, they are *incomplete possible worlds*. Austin’s types, the *descriptive contents* of statements, are looking very much like propositions—in particular the proposition that describes the claim being made by an utterance. With a little bit of license, we might think of Austin’s demonstrative content of a statement as that statement’s *truthmaker* in a fine-grained sense. Barwise’ notation in (11) above with respect to $x\vDash\phi$ betrays this reading. Moreover, given that $x\cmapsto y$ is a ternary relation, (12) is starting to look very much like a semantic clause for the conditional that turns on a three-place accessibility relation in something like a Kripke frame.

The semantics from Routley *et al.*’s (1982) relevance logic gives the evaluation conditions on a three-place accessibility relation, where the notion of an accessibility relation is familiar from their role in Kripke frames, used to specify the semantics of modal logic. Barwise notes the connection explicitly:

> The work presented here work also suggests a way to think about the three-place accessibility relation semantics for relevance logic of Routley and Meyer. (I have discussed this with both Gabbay and Dunn off and on over the past year. More recently, Greg Restall has observed this connection, and has begun to work out the connection in some detail.) (1993: 26)

Restall (1996)[^restall-1996] along with Mares (1996)[^mares-1996] work out this connection as follows. Restall assumes that channels *are* amongst the information sites (Mares does not). Instead of information *sites*, common terminology speaks of information *states*. Information states may be incomplete and/or inconsistent, indeed they may be sub-propositional entirely (as will be the case below when we look at fine-grained information-based semantics for natural languages based on informationalised versions of the Lambek Calculi). In Kripke/frame semantics terms, we have *ternary information frame* $\mathbf{F}:\langle S, \sqsubseteq, R\rangle$, where $S$ is a set of information states, $\sqsubseteq$ is a partial order on $S$, and $R$ is a ternary accessibility relation on members of $S$. An *information model* is an information frame $\mathbf{F}$ along with an evaluation/supports relation $\Vdash$ between members of $S$ and types/propositions $\phi, \psi\ldots$. How exactly we read $x\Vdash\phi$ is going to depend on what sort of information state $x$ happens to be, and what type of thing *φ* is. The simplest case will be when $x$ is a situation and *φ* is a proposition. In this case we may read $x\Vdash\phi$ as *φ is true at $x$*. Given this much, (12) is translated as follows:

$$x\Vdash\phi\to\psi\text{ iff }\forall y, z \text{ s.t. } Rxyz, \text{ if }y\Vdash\phi\text{ then }z\Vdash\psi.$$

In this context, the way that $Rxyz$ is read is—if you take the information that is true at $x$, and you put it together with the information that is true at $y$, then you get the information that is true at $z$. However, $Rxyz$ is not read so strictly in general. Although the $\Vdash$ relation *can* be read as a straightforward semantic relation in line with $\vDash$, it is considerably more flexible. Other readings $x\Vdash\phi$ include *$x$ carries the information that ψ*, *$x$ carries the information of type ψ*, *$x$ supports the information that/of type ψ*, *$x$ is a record of the information that/of type ψ*, and so on. As a consequence of this, the way that $Rxyz$ is read in practice will depend the applications to which the resulting information-based semantic models are being put—that is, on the domain of the information channels in question.

The domain of information channels might be anything from channels for propositionally structured environmental information along the lines Floridi is interested in (be it veridical or not), or sub-propositionally structured environmental information along the lines Fodor and Evans are interested in. Moreover, it might be linguistically focused sub-propositionally structured information from natural language semantics, or concern semantic informational phenomena familiar from issues in the philosophy of language such as attitude reports and the semantic analysis of epistemic and other attitudinal states. We will examine such approaches in some detail in the section below.

For now, note that semantic models of different information channel types will be individuated in terms of how it is that the “putting together” of $x$ and $y$ in $Rxyz$ is understood *precisely*. For example, putting $x$ together with $y$ might mean the same thing as putting $y$ together with $x$, or it might not, depending on whether or not one wants the ternary relation $R$ to be a *commutative* relation. That is, on whether or not one wants it to be the case the $\forall x\;\forall y\;\forall z(Rxyz\to Ryxz)$ Whether or not one *does* want $R$ to be a commutative relation will depend on properties of the information channels that one is trying to model (for which see the paragraph above).

By analogy, recall modal logic, where different properties of the two-place accessibility relation $R^2xy$ will generate different modal logics (for example, to get the modal logic $T$ one makes $R^2xy$ reflexive, to get the modal logic $S4$ one makes $R^2xy$ reflexive and transitive and so on). Similar decisions can be made with regard to the ternary relation $Rxyz$. For example, one might want $Rxyz$ to have the properties of *commutativity*, *associativity*, *contraction*, *monotonicity*, and others, or none at all, or subtle combinations of these and more. These decisions will generate *different logics of information channels* in the same way as do the choices on $R^2$ with regard to different modal logics. These logics are known in general as substructural logics on account of the way the properties of the ternary accessibility relation (commutation etc.), correspond to the structural rules that individuate the logics themselves. (One may think of structural rules as the syntactic/proof-theoretic counterparts to the semantic conditions being discussed presently.) As a part of the growing field of logic and information more generally, we will see in the following section that clusters of such logics have found utility across a range of informational-semantic phenomena.

### 3.1 The semantics of information flow

A group of weak substructural logics known as the *Lambek calculi* reject *all* structural rules, or else one or the other of either commutation or association, or possess both of these rules only. Designed by and named after Joachim Lambek, these logics were designed originally to model the syntax, or formal grammar, of natural languages (see the entry on typelogical grammar).

That they have found a home modelling—providing a semantics for—information flow across information channels is not as surprising as it might seem initially. Firstly, with some license we may think of a natural language lexicon as a database, and a grammar as a specification of the processing constraints on that database such that the processing constraints guarantee well-formed outputs. Secondly, one of situation and channel theory’s targets originally was natural language semantics itself, so the convergence is far from totally surprising. For example, Massimo Poesio (1993)[^poesio-1993] appeals to the formal nomenclature of situation theory in order to build a theory of definite descriptions. Ginzburg (1993)[^ginzburg-1993] uses the naturally fine-grained structures of situation theory to give a semantics for propositional attitudes. Hwang and Schubert (1993) implement natural Language Processing (NLP) controls via a situation theoretic framework. Westerhåll, Haglund and Lager (1993) appeal to situation theory to give a theory of *text meaning* where texts are treated as abstract states coding readers’ cognitive states.

Barwise, Gabbay, and Hartonas (1995, 1996), appeal to the *associative* Lambek calculus in order to model, that is to give a semantics for, *information flow itself*. They define an *information network* $\mathbf{N}$ as a quadruple such that $\mathbf{N} := \langle S, C, \mapsto, \circ\rangle$, where $S$ is a set of information states (called “sites” by the authors), $C$ is a set of information channels, $\mapsto$ is a ternary accessibility relation on $S \times C \times S$, and $\circ$ is an associative binary composition operator on $C$. For information to flow, there must be some way in which channels compose so that information can flow from one channel to another. The authors specify the following constraint on serial channel composition. For all channels $a$ and $b$:

$$\forall x\; \forall y (x \overset{a\circ b}{\longmapsto} y\: \text{ iff }\ \exists z(x\overset{a}{\mapsto} z \text{ and } z\overset{b}{\mapsto} y))$$

The author’s argue for channels associating, hence the binary composition operator on channels being associative, i.e., for all channels $a,$ $b$, and $c$, if $a\circ(b\circ c)$, then $(a\circ b)\circ c$). Those familiar with *category theory* will know the refrain “channels associate!”.

Care is needed so as to not conflate channel *composition* as specified above in (14), with the channel *application* specified above in (12) and (13). The latter involves feeding a channel its input, whereas the former involves the compositions of channels themselves. Tedder (2017)[^tedder-2017] argues elegantly for the composition and application of information channels to be treated separately, and that we should not expect the properties of both (specified via structural rules on the ternary relation $\mapsto$ to be the same. For arguments with regard to just what properties it is that we *should* expect channel composition and application to possess, see Tedder (2021)[^tedder-2021] and Sequoiah-Grayson (2021)[^sequoiah-grayson-2021]. Sequoiah-Grayson (2010)[^sequoiah-grayson-2010] argues that a basic theory of information flow with a semantics given by the Lambek calculi gives us an informational interpretation of the *dynamic predicate logic* (DPL) of Groenendijk and Stokhof (1991).

Van Benthem (2010)[^benthem-2010][^benthem-2010-2], by contrast, argues against the temptation to understand Lambek calculi in such foundational informational terms. This is not to suggest that van Benthem is opposed to extended applications of the Lambek calculi. For example, van Benthem (1996)[^benthem-1996] argues for an application of the Lambek calculi for the purpose of giving a dynamic semantics for *cognitive procedures*. Van Benthem’s use of the Lambek calculi for a dynamic semantics of cognitive procedures, *in combination with* the use of substructurally interpreted Lambek calculi as a foundational model of information flow, leads naturally to the idea that models for *dynamic epistemic phenomena* might be given in information channel-theoretic terms. We examine such information models in the following section.

### 3.2 Modelling epistemic phenomena informationally

Sedlár and Punčochář (2019) extend *propositional dynamic logic* (PDL) into the non-associative Lambek Calculus, which they call *Lambek PDL*. They give Lambek PDL three informal interpretations, one in terms of actions that modify linguistic resources, another in terms of actions that modify bodies of information, and another in terms of actions that modify the epistemic states of agents (see 2019: 358–539). In their semantics, specific readings of the ternary relation $R$ from (13) above will depend on the interpretation of the information states in their models. In particular, they are interested in threshold cases where commutation, $x\circ y = y\circ x$, breaks down for channel application. Sedlár (2020)[^sedlár-2020] extends the non-associative and non-commutative Lambek calculus with *iterative* channel operations (both applicational and compositional) under an informational interpretation.

Sedlár (2016)[^sedlár-2016] designs and explores substructural epistemic logics under an informational interpretation with the explicit goal of attending to the *Scandal of Deduction* (SoD) from section 1.1 above. The motivating idea here is that there are channels from one epistemic state of an agent to another epistemic state of that agent, and that certain epistemic actions (namely acts of reasoning) that facilitate information flow along such channels can be captured by the ternary relation $R$ that marks channel application in (13) above. Punčochář and Sedlár (2017) introduce a substructural epistemic logic for *pooling information* in a group of agents via structured communication (viz. structured information flow) between them. In this context the binary combination operator $\circ$ (‘$\cdot$’ in Sedlár and Punčochář’s notation) is a pooling operator *between* the different epistemic states of agents in a communicative group. The authors’ have several examples to suggest that both association and commutation are misguided in this context. Sedlár, Punčochář, and Tedder (2019) provide a semantics for universal and common knowledge operators via the now-familiar informational reading of the non-associative Lambek Calculus under an informational interpretation.

## 4. Summary

At this point it is clear that semantic conceptions of information cover a large amount of territory, but not one without structure of cohesion.

Carnap and Bar-Hillel’s (1952) theory of semantic information for formal languages has an intuitive starting point, one that takes intensions and semantic information to be very closely related. Whatever the shortcomings of their theory, it has motivated an entire field of research into the nature of semantic information via the systematic informational approach to semantic and related phenomena of Luciano Floridi along with an increasingly large number of closely related research programs.

The information-based semantics for natural languages and content bearing mental states due largely to Dretske, Evans, Fodor, Lewis, Jackson, Recanati, and Zalta has led to refined theories of meaning and content in terms of informational relations. Such relations—information channels that allow information to flow from one part of a system to another—have proved to be so indispensable that they are in turn an object of research in their own right.

The semantic theory of information channels due largely to Barwise has been refined in such a way as to permit its adaptation for modelling a rich range of philosophical phenomena. Logics designed originally to model linguistic artefacts on their own terms have been used to capture the properties of information flow. This has lead quickly to rigorously defined semantic models for such linguistic artefacts, as well as to models for epistemic phenomena that are given in terms of information flow itself.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=information-semantic). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/information-semantic/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=information-semantic&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/information-semantic/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

[Please contact the author with suggestions.]

## Related Entries

grammar: typelogical | information | logic: and information | logic: modal | logical pluralism | meaning, theories of | mental content: causal theories of | situations: in natural language semantics

[^aczel-1993]: Aczel, Peter, David Israel, Yasuhiro Katagin, and Stanley Peters (eds.), 1993, *Situation Theory and Its Applications, Volume 3: Proceedings of the First-Third Conference on Situation Theory and Its Applications. Third Conference Held in Kanagawa, Japan, November 1991*, (CSLI Lecture Notes 37), Stanford, CA: CSLI Publications.

[^allo-2007]: Allo, Patrick, 2007, “Logical Pluralism and Semantic Information”, *Journal of Philosophical Logic*, 36(6): 659–694. doi:10.1007/s10992-007-9054-2

[^allo-2011]: –––, 2011, “The Logic of ‘Being Informed’ Revisited and Revised”, *Philosophical Studies*, 153(3): 417–434. doi:10.1007/s11098-010-9516-1

[^austin-1950]: Austin, J. L., 1950, “Truth”, *Aristotelian Society Supplementary Volume*, 24: 111–128. doi:10.1093/aristoteliansupp/24.1.111

[^barwise-1993]: Barwise, Jon, 1993, “Constraints, Channels, and the Flow of Information”, in Aczel et al. 1993: 3–28.

[^barwise-1983]: Barwise, Jon and John Perry, 1983, *Situations and Attitudes*, Cambridge, MA: MIT Press.

[^barwise-1995]: Barwise, Jon, Dov Gabbay, and Chrysafis Hartonas, 1995, “On the Logic of Information Flow”, *Logic Journal of IGPL*, 3(1): 7–49. doi:10.1093/jigpal/3.1.7

[^barwise-1996]: –––, 1996, “Information Flow and the Lambek Calculus”, in Seligman and Westerståhl 1996: 47-62.

[^benthem-1996]: van Benthem, Johan, 1996, *Exploring Logical Dynamics*, Stanford, CA: CSLI Publications.

[^benthem-2010]: –––, 2010, “Categorial Versus Modal Information Theory”, in van Benthem and Moortgat 2010: 533–543.

[^benthem-2010-2]: van Benthem, Johan and Michael Moortgat (eds), 2010, *Festschrift for Joachim Lambek*, issue of *Linguistic Analysis*, 36(1-4).

[^bremer-2004]: Bremer, Manual and Daniel Cohnitz, 2004, *Information and Information Flow: An Introduction*, Frankfurt, Lancaster: Ontos Verlag.

[^carnap-1952]: Carnap, Rudolf and Yehoshua Bar-Hillel, 1952, “An Outline of a Theory of Semantic Information”, Technical report 247, Cambridge, MA: Research Laboratory of Electronics, Massachusetts Institute of Technology. Reprinted in *Language and Information: Selected Essays on their Theory and Application*, Y. Bar-Hillel, Addison-Wesley Series in Logic, Israel: Jerusalem Academic Press and Addison-Wesley, 1964, pp. 221–274. [[Carnap and Bar-Hillel 1952 available online](https://dspace.mit.edu/handle/1721.1/4821)]

[^cevolani-2011]: Cevolani, Gustavo, 2011, “Verisimilitude and Strongly Semantic Information”, *Etica & Politica/Ethics & Politics*, 13(2): 159–179.

[^cevolani-2014]: –––, 2014, “Strongly Semantic Information as Information About the Truth”, in *Recent Trends in Philosophical Logic*, Roberto Ciuni, Heinrich Wansing, and Caroline Willkommen (eds.), (Trends in Logic 41), Cham: Springer International Publishing, 59–74. doi:10.1007/978-3-319-06080-4_5

[^d’alfonso-2011]: D’Alfonso, Simon, 2011, “On Quantifying Semantic Information”, *Information*, 2(1): 61–101. doi:10.3390/info2010061

[^dinneen-2015]: Dinneen, Jesse David and Christian Brauner, 2015, “Practical and Philosophical Considerations for Defining Information as Well-Formed, Meaningful Data in the Information Sciences”, *Library Trends*, 63(3): 378–400. doi:10.1353/lib.2015.0012

[^dodig-crnkovic-2005]: Dodig-Crnkovic, Gordana, 2005, “System Modeling and Information Semantics”, in *Proceedings of the Fifth Promote IT Conference* (Borlänge, Sweden), Janis Bubenko, Owen Eriksson, Hans Fernlund, and Mikael Lind (eds.), Lund: Studentlitteratur.

[^dretske-1981]: Dretske, Fred I., 1981, *Knowledge and the Flow of Information*, Cambridge, MA: The MIT Press.

[^evans-1982]: Evans, Gareth, 1982, *The Varieties of Reference*, John Henry McDowell (ed.), Oxford: Clarendon Press.

[^floridi-2004]: Floridi, Luciano, 2004, “Outline of a Theory of Strongly Semantic Information”, *Minds and Machines*, 14(2): 197–221. doi:10.1023/B:MIND.0000021684.50925.c9

[^floridi-2005]: –––, 2005, “Is Semantic Information Meaningful Data?”, *Philosophy and Phenomenological Research*, 70(2): 351–370. doi:10.1111/j.1933-1592.2005.tb00531.x

[^floridi-2006]: –––, 2006, “The Logic of Being Informed”, *Logique et Analyse*, 49(196): 433–460.

[^floridi-2008]: –––, 2008, “Understanding Epistemic Relevance”, *Erkenntnis*, 69(1): 69–92. doi:10.1007/s10670-007-9087-5

[^floridi-2011]: –––, 2011, “Semantic Information and the Correctness Theory of Truth”, *Erkenntnis*, 74(2): 147–175. doi:10.1007/s10670-010-9249-8

[^floridi-2012]: –––, 2012, “Semantic Information and the Network Theory of Account”, *Synthese*, 184(3): 431–454. doi:10.1007/s11229-010-9821-4

[^fetzer-2004]: Fetzer, James H., 2004, “Information: Does It Have To Be True?”, *Minds and Machines*, 14(2): 223–229. doi:10.1023/B:MIND.0000021682.61365.56

[^fodor-1990]: Fodor, Jerry A., 1990, *A Theory of Content and Other Essays*, Cambridge, MA: MIT Press.

[^frické-1997]: Frické, Martin, 1997, “Information Using Likeness Measures”, *Journal of the American Society for Information Science*, 48(10): 882–892. doi:10.1002/(SICI)1097-4571(199710)48:10<882::AID-ASI4>3.0.CO;2-Y

[^ginzburg-1993]: Ginzburg, Jonathan, 1993, “Propositional and Non-Propositional Attitudes”, in Aczel et al. 1993: 265–302.

[^groenendijk-1991]: Groenendijk, Jeroen and Martin Stokhof, 1991, “Dynamic Predicate Logic”, *Linguistics and Philosophy*, 14(1): 39–100. doi:10.1007/BF00628304

[^hintikka-1970]: Hintikka, Jaakko, 1970, “Surface Information and Depth Information”, in *Information and Inference*, Jaakko Hintikka and Patrick Suppes (eds.), Dordrecht: Reidel, 263–297. doi:10.1007/978-94-010-3296-4_8

[^hintikka-1973]: –––, 1973, *Logic, Language Games, and Information*, Oxford: Clarendon Press.

[^hwang-1993]: Hwang, Chung Hee and Lenhart K. Schubert, 1993, “Episodic Logic: A Situational Logic for Natural Language Processing”, in Aczel et al. 1993: 303–338.

[^jackson-2010]: Jackson, Frank, 2010, *Language, Names, and Information*, Oxford, UK: Wiley-Blackwell. doi:10.1002/9781444325362

[^lewis-1983]: Lewis, David, 1983, “Individuation by Acquaintance and by Stipulation”, *The Philosophical Review*, 92(1): 3–32. doi:10.2307/2184519

[^mares-1996]: Mares, Edwin D., 1996, “Relevant Logic and the Theory of Information”, *Synthese*, 109(3): 345–360. doi:10.1007/BF00413865

[^mingers-1995]: Mingers, John C., 1995, “Information and Meaning: Foundations for an Intersubjective Account”, *Information Systems Journal*, 5(4): 285–306. doi:10.1111/j.1365-2575.1995.tb00100.x

[^mingers-1996a]: –––, 1996a, “Embodying Information Systems”, in *Information Technology and Changes in Organisational Work*, Wanda Orlikowski, Geoff Walsham, Matthew Jones, and Janice DeGross (eds), London: Chapman Hall, 272–292.

[^mingers-1996b]: –––, 1996b, “An Evaluation of Theories of Information with Regard to the Semantic and Pragmatic Aspects of Information Systems”, *Systems Practice*, 9(3): 187–209. doi:10.1007/BF02169014

[^mingers-2018]: Mingers, John C. and Craig Standing, 2018, “What Is Information? Toward a Theory of Information as Objective and Veridical”, *Journal of Information Technology*, 33(2): 85–104. doi:10.1057/s41265-017-0038-6

[^poesio-1993]: Poesio, Massimo, 1993, “A Situation-Theoretic Formalization of Definite Description Interpretation in Plan Elaboration Dialogues”, in Aczel et al. 1993: 339–374.

[^primiero-2009]: Primiero, Giuseppe, 2009, “An Epistemic Logic for Becoming Informed”, *Synthese*, 167(2): 363–389. doi:10.1007/s11229-008-9413-8

[^punčochář-2017]: Punčochář, Vít and Igor Sedlár, 2017, “Substructural Logics for Pooling Information”, in *Logic, Rationality, and Interaction: 6th International Workshop, LORI 2017*, Alexandru Baltag, Jeremy Seligman, and Tomoyuki Yamada (eds.), (Lecture Notes in Computer Science 10455), Berlin, Heidelberg: Springer Berlin Heidelberg, 407–421. doi:10.1007/978-3-662-55665-8_28

[^recanati-2012]: Recanati, François, 2012, *Mental Files*, Oxford: Oxford University Press. doi:10.1093/acprof:oso/9780199659982.001.0001

[^recanati-2016]: –––, 2016, *Mental Files in Flux*, Oxford: Oxford University Press. doi:10.1093/acprof:oso/9780198790358.001.0001

[^restall-1996]: Restall, Greg, 1996, “Information Flow and Relevant Logics”, in Seligman and Westerståhl 1996: 463–477.

[^restall-2002]: –––, 2002, *An Introduction to Substructural Logics*, London: Routledge. doi:10.4324/9780203016244

[^routley-1982]: Routley, Richard, Robert K. Meyer, Valerie Plumwood, and Ross T. Brady, 1982, *Relevant Logics and Their Rivals 1*, Atascadero, CA: Ridgeview.

[^sedlár-2016]: Sedlár, Igor, 2016, “Epistemic Extensions of Modal Distributive Substructural Logics”, *Journal of Logic and Computation*, 26(6): 1787–1813. doi:10.1093/logcom/exu034

[^sedlár-2020]: –––, 2020, “Iterative Division in the Distributive Full Non-Associative Lambek Calculus”, in *Dynamic Logic. New Trends and Applications: Second International Workshop, DaLí 2019*, Luís Soares Barbosa and Alexandru Baltag (eds.), (Lecture Notes in Computer Science 12005), Cham: Springer International Publishing, 141–154. doi:10.1007/978-3-030-38808-9_9

[^sedlár-2019]: Sedlár, Igor and Vít Punčochář, 2019, “From Positive PDL to Its Non-Classical Extensions”, *Logic Journal of the IGPL*, 27(4): 522–542. doi:10.1093/jigpal/jzz017

[^sedlár-2019-2]: Sedlár, Igor, Vít Punčochář, and Andrew Tedder, 2019, “First Degree Entailment with Group Attitudes and Information Updates”, in *Logic, Rationality, and Interaction: 7th International Workshop, LORI 2019*, Patrick Blackburn, Emiliano Lorini, and Meiyun Guo (eds.), (Lecture Notes in Computer Science 11813), Berlin, Heidelberg: Springer Berlin Heidelberg, 273–285. doi:10.1007/978-3-662-60292-8_20

[^seligman-1996]: Seligman, Jerry and Dag Westerståhl (eds.), 1996, *Logic, Language and Computation, Volume 1*, (CSLI Lecture Notes 58), Stanford, CA: CSLI Publications.

[^sequoiah-grayson-2007]: Sequoiah-Grayson, Sebastian, 2007, “The Metaphilosophy of Information”, *Minds and Machines*, 17(3): 331–344. doi:10.1007/s11023-007-9072-4

[^sequoiah-grayson-2008]: –––, 2008, “The Scandal of Deduction: Hintikka on the Information Yield of Deductive Inferences”, *Journal of Philosophical Logic*, 37(1): 67–94. doi:10.1007/s10992-007-9060-4

[^sequoiah-grayson-2010]: –––, 2010, “Lambek Calculi with 0 and Test-Failure in DPL”, in van Benthem and Moortgat 2010: 517–532.

[^sequoiah-grayson-2021]: –––, 2021 “A Logic of Affordances”, in *The Logica Yearbook 2020*, Martin Blicha and Igor Sedlár (eds), London: College Publications, 219–236.

[^shannon-1950]: Shannon, Claude E., 1950, “General Treatment of the Problem of Coding. The Lattice Theory of Information”, presented at the *Symposium on Information Theory*, London, September 1950. Printed, 1953, as two papers, “General Treatment of the Problem of Coding” and “The Lattice Theory of Information” in *Institute of Radio Engineers (IRE), Transactions on Information Theory*, 1(1): 102–104 and 105–107, respectively. Reprinted, 1993, in *Claude E. Shannon: Collected Papers*, N. J. A. Sloane and A. D. Wyner (eds), Los Alamos, CA: IEEE Press, 177–179 and 180–183. doi:10.1109/TIT.1953.1188572

[^tedder-2017]: Tedder, Andrew, 2017, “Channel Composition and Ternary Relation Semantics”, *Proceedings of the Third Workshop*, Katalin Bimbó and J. Michael Dunn (eds), special issue of *The IfCoLog Journal of Logics and their Applications*, 4(3): 731–753.

[^tedder-2021]: –––, 2021, “Information Flow in Logics in the Vicinity of BB”, *The Australasian Journal of Logic*, 18(1): 1–24. doi:10.26686/ajl.v18i1.6288

[^vakarelov-2010]: Vakarelov, Orlin, 2010, “Pre-Cognitive Semantic Information”, *Knowledge, Technology & Policy*, 23(1–2): 193–226. doi:10.1007/s12130-010-9109-5

[^westerhåll-1993]: Westerhåll, Dag, Björn Haglund, and Torbjörn Lager, 1993, “A Situation-Theoretic Representation of Text Meaning: Anaphora, Quantification, and Negation”, in Aczel et al. 1993: 375–408.

[^williamson-2007]: Williamson, Timothy (ed.), 2007, *The Philosophy of Philosophy*, Oxford, UK: Blackwell Publishing Ltd. doi:10.1002/9780470696675

[^wittgenstein-1921]: Wittgenstein. Ludwig, 1921 [1922], “Logisch-Philosophische Abhandlung”, *Annalen der Naturphilosophische*, 14(3/4): 185–262. Translated as *Tractatus Logico-Philosophicus* (TLP), C. K. Ogden (trans.), London: Routledge & Kegan Paul, 1922.
