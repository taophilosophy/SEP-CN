# Paraconsistent Logic
**First published Tue Sep 24, 1996; substantive revision Fri Apr 17, 2026**

*Priest, Graham, Tanaka, Koji, Weber, Zach*

A logical consequence relation is *explosive* if according to it any arbitrary contradiction $A$, $\neg A$ entails any arbitrary conclusion $B$ (*ex contradictione quodlibet* (ECQ)). Classical logic, and most standard non-classical logics too such as intuitionist logic, are explosive. Inconsistency, according to a standard view about logic, cannot be coherently reasoned about.

Paraconsistent logic challenges this standard view. A logical consequence relation is said to be *paraconsistent* if it is not explosive. Thus, if a consequence relation is paraconsistent, then even in circumstances where the available information is inconsistent, the consequence relation does not explode into *triviality*. Thus, paraconsistent logic accommodates inconsistency in a controlled way that treats inconsistent information as potentially informative.

The prefix ‘para’ in English has two meanings: ‘quasi’ (or ‘similar to, modelled on’) or ‘beyond’. When the term ‘paraconsistent’ was coined by Miró Quesada at the Third Latin American Conference on Mathematical Logic in 1976, he seems to have had the first meaning in mind. Many paraconsistent logicians, however, have taken it to mean the second, which provided different reasons for the development of paraconsistent logic as we will see below.

Paraconsistent logic is defined negatively: any logic is paraconsistent as long as it is not explosive. This means there is no single set of open problems or programs in paraconsistent logic. As such, this entry is not a complete survey of paraconsistent logic. The aim is to describe some philosophically salient features of a diverse field.

## 1. Paraconsistency

A logic is *paraconsistent* iff its logical consequence relation $(\vDash$, either semantic or proof theoretic) is not explosive. Paraconsistency is a property of a consequence relation. The argument *ex contradictione quodlibet* (ECQ) is paraconsistently invalid: in general, it is not the case that $A$, $\neg A \vDash B$.

The role often played by the notion of consistency in logics, namely, the most basic requirement that any theory must meet, is relaxed to the notion of *coherence*: no theory can include every sentence whatsoever if it is to be considered tenable. Simple consistency of a theory (no contradictions) is a special case of absolute consistency, or *non-triviality* (not every sentence is a part of the theory). As we will see below, many paraconsistent logics do validate the Law of Non-Contradiction (LNC), $\vDash \neg(A \wedge \neg A)$, even though they invalidate ECQ.

Beyond the basic, definitional requirement that a paraconsistent consequence relation be non-explosive, there is a huge divergence of paraconsistent logics. At this stage of development, well into the twenty-first century, it seems fair to say that ‘paraconsistency’ does not single out one particular approach to logic, but is rather a property that some logics have and others do not (like, say, compactness, or multiple conclusions).

### 1.1 Dialetheism

In the literature, especially in the part of it that contains objections to paraconsistent logic, there has been some tendency to confuse paraconsistency with *dialetheism*, the view that there are true contradictions (see the entry on dialetheism). The view that a consequence relation should be paraconsistent does not entail the view that there are true contradictions. Paraconsistency is a property of a consequence relation whereas dialetheism is a view about truth. The fact that one can define a non-explosive consequence relation does not mean that some sentences are true. The fact that one can construct a model where a contradiction holds but not every sentence of the language holds (or where this is the case at some world) does not mean that the contradiction is true per se. Hence paraconsistency must be distinguished from dialetheism. This has been argued by Barrio and Da Ré (2018), and an explicitly non-dialetheic interpretation of paraconsistency is given by Carnielli and Rodrigues (2021). For reasons that paraconsistency may lead to dialetheism after all, see Asmus (2012).

Dialetheism is the view that some contradiction is true, which is a distinct thesis from ‘trivialism’, the view that everything whatsoever (including every contradiction) is true; if dialetheism is to be coherent, then it seems a dialethiest’s preferred logic must be paraconsistent (though even this has been challenged by Barrio and Da Ré, based on work by Ripley and others e.g. Ripley 2012)[^ripley-2012]. A paraconsistent logician may feel some pull towards dialetheism, but most paraconsistent logics are not dialetheic. In a discussion of paraconsistent logic, the primary focus is not the obtainability of contradictions but the explosive nature of a consequence relation.

### 1.2 A Brief History of *ex contradictione quodlibet*

It is now standard to view *ex contradictione quodlibet* as valid. This contemporary view, however, should be put in a historical perspective. It was towards the end of the nineteenth century, when the study of logic achieved mathematical articulation, that an explosive logical theory became the standard. With the work of logicians such as Boole, Frege, Russell and Hilbert, classical logic became the orthodox logical account.

In antiquity, however, no one seems to have endorsed the validity of ECQ. Aristotle presented what is sometimes called the *connexive principle*: “it is impossible that the same thing should be necessitated by the being and by the not-being of the same thing” (*Prior Analytic* II 4 57b3). (Connexive logic has recently been reinvigorated by Wansing, e.g. Omori and Wansing (2019); see the entry on connexive logic that has been developed based on this principle.) This principle became a topic of debates in the Middle Ages or Medieval time. Though the medieval debates seem to have been carried out in the context of conditionals, we can also see it as debates about consequences. The principle was taken up by Boethius (480–524 or 525) and Abelard (1079–1142), who considered two accounts of consequences. The first one is a familiar one: it is impossible for the premises to be true but the conclusion false. The first account is thus similar to the contemporary notion of truth-preservation. The second one is less accepted recently: the sense of the premises contains that of the conclusion. This account, as in some relevant logics (like Brady’s logic of meaning containment (Brady 2006)[^brady-2006]), does not permit an inference whose conclusion is arbitrary. Abelard held that the first account fails to meet the connexive principle and that the second account (the account of containment) captured Aristotle’s principle.

Abelard’s position was shown to face a difficulty by Alberic of Paris in the 1130s. Most medieval logicians didn’t, however, abandon the account of validity based on containment or something similar (see, for example, Martin 1987)[^martin-1987]. But one way to handle the difficulty is to reject the connexive principle. This approach, which has become most influential, was accepted by the followers of Adam Balsham or Parvipontanus (or sometimes known as Adam of The Little Bridge [12ᵗʰ century]). The Parvipontanians embraced the truth-preservation account of consequences and the paradoxes that are associated with it. In fact, it was a member of the Parvipontanians, William of Soissons, who discovered in the twelfth century what we now call the C.I. Lewis (independent) argument for ECQ (see Martin 1986)[^martin-1986].

The containment account, however, did not disappear. John Duns Scotus (1266–1308) and his followers accepted the containment account (see Martin 1996)[^martin-1996]. The Cologne School of the late fifteenth century argued against ECQ by rejecting *disjunctive syllogism* (see Sylvan 2000)[^sylvan-2000].

In the history of logic in Asia, we can discern the beginnings of a formalisation of argumentative moves in Tibetan debate logic; see Tillemans (2022). Logics developed by Dignāga (5ᵗʰ century) and Dharmakīrti (7ᵗʰ century) do not embrace ECQ. But it is difficult to make categorical statements about formal principles such as ECQ in this context. In general, logical studies in Asia are conducted in relation to argumentation or reasoning, especially in China, India, and the regions influenced by their cultural and intellectual traditions. Contradictions may need to be avoided; yet arguing or reasoning to an arbitrary conclusion from a contradiction does not seem to have received endorsement.

### 1.3 Modern History of Paraconsistent Logic

In the twentieth century, alternatives to an explosive account of logical consequence occurred to different people at different times and places independently of each other. They were often motivated by different considerations. The earliest paraconsistent logics in the contemporary era seem to have been given by two Russians. Starting about 1910, Vasil’év proposed a modified Aristotelian syllogistic including statements of the form: $S$ is both $P$ and not $P$. In 1929, Orlov gave the first axiomatisation of the relevant logic $R$ which is paraconsistent. (On Vasil’év, see Arruda 1977 and Arruda 1989: 102f; on Orlov, see Anderson, Belnap, & Dunn 1992: xvii.)[^arruda-1977][^arruda-1989][^arruda-1977-2]

The work of Vasil’év or Orlov did not make any impact at the time. The first (formal) logician to have developed paraconsistent logic was Jaśkowski in Poland, who was a student of Łukasiewicz, who himself had envisaged paraconsistent logic in his critique of Aristotle on the LNC (Łukasiewicz 1951). Almost at the same time, Halldén (1949) presented work on the logic of nonsense, but again this went mostly unnoticed.

Paraconsistent logics were developed independently in South America by Florencio Asenjo and especially Newton da Costa in their doctoral dissertations, in 1954 and 1963 respectively, with an emphasis on mathematical applications (see Asenjo 1966, da Costa 1974)[^asenjo-1966][^costa-1974]. An active group of logicians has been researching paraconsistent logic continuously ever since, especially in Campinas and São Paulo, Brazil, with a focus on logics of formal inconsistency. Carnielli and Coniglio (2016) give a comprehensive account to date of this work.

Paraconsistent logics in the forms of relevant logics were proposed in England by Smiley in 1959 and also at about the same time, in a much more developed form, in the United States by Anderson and Belnap. An active group of relevant logicians grew up in Pittsburgh including Dunn, Meyer, and Urquhart. The development of paraconsistent logics (in the form of relevant logics) was transported to Australia. R. Routley (later Sylvan) and V. Routley (later Plumwood) discovered an intensional semantics for some of Anderson-Belnap relevant logics. A school developed around them in Canberra which included Brady and Mortensen, and later Priest who, together with R. Routley, incorporated dialetheism into the development.

Since the 1970s, the development of paraconsistent logic has been international. Some of the major schools of thought are canvassed below, including adaptive logic (as in Batens 2001)[^batens-2001] and preservationism (as in Schotch, Brown, & Jennings 2009). There is work being done in Argentina, Australia, Belgium, Brazil, Canada, China, Czechia, England, Germany, India, Israel, Italy, Japan, Mexico, New Zealand, Poland, Scotland, Spain, the United States, and more. There has been a series of major international conferences about paraconsistent logic. In 1997, the First World Congress on Paraconsistency was held at the University of Ghent in Belgium. The Second World Congress was held in São Sebastião (São Paulo, Brazil) in 2000, the Third in Toulous in France in 2003 and the Fourth in Melbourne (Australia) in 2008. A Fifth World Congress was held in Kolkata, India in 2013. Another major paraconsistency conference in 2014 was held in Munich (Andreas & Verdée 2016)[^andreas-2016]. In 2022 the Sixth World Congress was in Toruń, Poland, and in 2024 the Seventh World Congress was in Oaxaca, Mexico. See the bibliography section on World Congress Proceedings and links in other internet resources below.

## 2. Motivations

The reasons for paraconsistency that have been put forward are specific to the development of the particular formal systems of paraconsistent logic. However, there are several general reasons for thinking that logic should be paraconsistent. Before we summarise the systems of paraconsistent logic, we present some motivations for paraconsistent logic.

### 2.1 Inconsistency without Triviality

A most telling reason for paraconsistent logic is, prima facie, the fact that there are theories which are inconsistent but non-trivial. If we admit the existence of such theories, their underlying logics must be paraconsistent (though see Michael 2016)[^michael-2016].

#### 2.1.1 Non-Trivial Theories

Examples of apparently inconsistent but non-trivial theories are easy to produce. One example can be derived from the history of science. Consider Bohr’s theory of the atom. According to this, an electron orbits the nucleus of the atom without radiating energy. However, according to Maxwell’s equations, which formed an integral part of the theory, an electron which is accelerating in orbit must radiate energy. Hence Bohr’s account of the behaviour of the atom was inconsistent. Yet, patently, not everything concerning the behavior of electrons was inferred from it, nor should it have been. Hence, whatever inference mechanism it was that underlay it, arguably this must have been paraconsistent (Brown & Priest 2015)[^brown-2015].

#### 2.1.2 True Contradictions

Despite the fact that dialetheism and paraconsistency must be distinguished, dialetheism can be a motivation for paraconsistent logic. One candidate for a dialetheia (a true contradiction) is the *liar paradox*. Consider the sentence: ‘This sentence is not true’. There are two options: either the sentence is true or it is not. Suppose it is true. Then what it says is the case. Hence the sentence is not true. Suppose, on the other hand, it is not true. This is what it says. Hence the sentence is true. In either case it is both true and not true. (See the entry on dialetheism.)

#### 2.1.3 Linguistics

Natural languages are another possible site of non-trivial inconsistency. In linguistics, it has been observed that normal lexical features are preserved even in inconsistent contexts. For example, words like ‘near’ have spatial connotations that are not disturbed even when dealing with impossible objects (McGinnis 2013)[^mcginnis-2013]:

> If I tell you that I painted a spherical cube brown, you take its exterior to be brown …, and if I am inside it, you know I am not near it. (Chomsky 1995: 20)[^chomsky-1995]

Hence if natural language can be said to have a logic, paraconsistent logics could be a candidate for formalizing it.

### 2.2 Automated Reasoning and Belief Revision

Paraconsistent logic is motivated not only by philosophical considerations, but also by its applications and implications.

#### 2.2.1 Automated Reasoning

One of the applications is *automated reasoning* (*information processing*). Consider a computer which stores a large amount of information, as in Belnap (1992). While the computer stores the information, it is also used to operate on it, and, crucially, to infer from it. Now it is quite common for the computer to contain inconsistent information, because of mistakes by the data entry operators or because of multiple sourcing. This is certainly a problem for database operations with theorem-provers, and so has drawn much attention from computer scientists. Techniques for removing inconsistent information have been investigated. Yet all have limited applicability, and, in any case, are not guaranteed to produce consistency. (There is no general algorithm for logical falsehood.) Hence, even if steps are taken to get rid of contradictions when they are found, an underlying paraconsistent logic is desirable if hidden contradictions are not to generate spurious answers to queries.

Nelson’s paraconsistent (four-valued) logic N4 has been specifically studied for applications in computer science (Kamide & Wansing 2012)[^kamide-2012]. Annotated logics were proposed by Subrahmanian (1987) and then by da Costa, Subrahmanian, and Vago (1991); these tools are extended to robotics, expert systems for medical diagnosis, and engineering, with work gathered in the volumes edited by Abe, Akama, and Nakamatsu (2015) and Akama (2016). Recent work picking up from Belnap’s original suggestion includes Bimbó (2019), Sedlár (2019), and a model of paraconsistent logic gates and circuits by Cano-Jorge (2025).

#### 2.2.2 Belief Revision

*Belief revision* is the study of rationally revising bodies of belief in the light of new evidence. Notoriously, people have inconsistent beliefs. They may even be rational in doing so. For example, there may be apparently overwhelming evidence for both something and its negation. There may even be cases where it is in principle impossible to eliminate such inconsistency. For example, consider the ‘paradox of the preface’. A rational person, after thorough research, writes a book in which they claim $A_1$,…, $A_n$. But they are also aware that no book of any complexity contains only truths. So they rationally believe $\neg(A_1 \wedge \ldots \wedge A_n)$ too. Hence, principles of rational belief revision must work on inconsistent sets of beliefs. Standard accounts of belief revision, e.g. the AGM theory (see the logic of belief revision), all fail to do this, since they are based on classical logic (Tanaka 2005)[^tanaka-2005]. A more adequate account may be based on a paraconsistent logic; see Girard and Tanaka 2016.

### 2.3 Formal Semantics and Set Theory

Paraconsistency can be taken as a response to *logical paradoxes* in formal semantics and set theory.

#### 2.3.1 Truth Theory

Semantics is the study that aims to spell out a theoretical understanding of meaning. Most accounts of semantics insist that to spell out the meaning of a sentence is, in some sense, to spell out its truth-conditions. Now, *prima facie* at least, truth is a predicate characterised by the Tarski T-scheme:

$$ T(\boldsymbol{A}) \leftrightarrow A $$

where $A$ is a sentence and $\boldsymbol{A}$ is its name. But given any standard means of self-reference, e.g., arithmetisation, one can construct a sentence, $B$, which says that $\neg T(\boldsymbol{B})$. The T-scheme gives that $T(\boldsymbol{B}) \leftrightarrow \neg T(\boldsymbol{B})$. It then follows that $T(\boldsymbol{B}) \wedge \neg T(\boldsymbol{B})$. (This is, of course, just the liar paradox.) A full development of a theory of truth in paraconsistent logic is given by Beall (2009); for more general details see Beall et al. (2018).

#### 2.3.2 Set Theory

The situation is similar in set theory. The naive, and arguably intuitively correct, axioms of set theory are the *Comprehension Schema* and *Extensionality Principle*:

$$ \begin{align*} & \exists y\forall x(x \in y \leftrightarrow A) \\ & \forall x(x \in y \leftrightarrow x \in z) \rightarrow y = z \end{align*} $$

As was discovered by Russell, any theory that contains the Comprehension Schema is inconsistent. For putting ‘$y \not\in y$’ for $A$ in the Comprehension Schema and instantiating the existential quantifier to an arbitrary such object ‘$r$’ gives:

$$ \forall y(y \in r \leftrightarrow y \not\in y) $$

So, instantiating the universal quantifier to ‘$r$’ gives:

$$ r \in r \leftrightarrow r \not\in r $$

It then follows that $r \in r \wedge r \not\in r$.

The standard approaches to these problems of inconsistency are, by and large, ones of expedience. A paraconsistent approach makes it possible to have theories of truth and sethood in which the mathematically fundamental intuitions about these notions are respected. For example, as Brady (1989; 2006) has shown, contradictions may be allowed to arise in a paraconsistent set theory, but these need not infect the whole theory.

There are several approaches to set theory with naive comprehension via paraconsistent logic. Models for paraconsistent set theory are described by Libert (2005). The theories of ordinal and cardinal numbers are developed axiomatically using relevant logic in Weber (2010b, 2012). The possibility of adding a consistency operator to track non-paradoxical fragments of the theory is considered in Omori (2015), taking a cue from the tradition of da Costa. Naive set theory using adaptive logic is presented by Verdée (2013); see Batens (2020) for current developments in adaptive Fregean Set Theory.

Incurvati (2020, chapter 4) gives a detailed critique of the paraconsistent approach to naive set theory. Recent work in algebra-valued models of paraconsistent set theory gets away from naive set theory and is about placing the axioms of standard Zermelo-Fraenkel Set Theory (ZF) in a paraconsistent framework. Algebraic models along these lines are being vigorously investigated by Tarafder, Venturi, and Jockwich (see Jockwich and Venturi 2021)[^jockwich-2021], following Löwe and Tarafder (2015). A different approach to ZF set theory in a paraconsistent logic is in Khomskii and Oddsson (2024).

#### 2.3.3 Mathematics in general

According to da Costa (1974: 498),

> It would be as interesting to study the inconsistent systems as, for instance, the non-euclidean geometries: we would obtain a better idea of the nature of paradoxes, could have a better insight on the connections amongst the various logical principles necessary to obtain determinate results, etc. … It is not our aim to eliminate the inconsistencies, but to analyze and study them.

A recent step in this direction is in Weber (2021). For further developments of mathematics in paraconsistent logics, see entry on *inconsistent mathematics*.

### 2.4 Arithmetic and Gödel’s Theorem

Unlike formal semantics and set theory, there may not be any obvious arithmetical principles that give rise to contradiction. Nonetheless, just like the classical non-standard models of arithmetic, there is a class of *inconsistent models of arithmetic* (or more accurately *models of inconsistent arithmetic*) which have an interesting and important mathematical structure.

One interesting implication of the existence of inconsistent models of arithmetic is that some of them are finite (unlike the classical non-standard models). This means that there are some significant applications in the metamathematical theorems. For example, the classical Löwenheim-Skolem theorem states that $Q$ (Robinson’s arithmetic which is a fragment of Peano arithmetic) has models of every infinite cardinality but has no finite models. But, $Q$ can be shown to have models of finite size too by referring to the inconsistent models of arithmetic; see Dunn (1979).

It is not only the Löwenheim-Skolem theorem but also other metamathematical theorems can be given a paraconsistent treatment. In the case of other theorems, however, the negative results that are often shown by the limitative theorems of metamathematics may no longer hold. One important such theorem is Gödel’s theorem.

One version of Gödel’s first incompleteness theorem states that for any consistent axiomatic theory of arithmetic, which can be recognised to be sound, there will be an arithmetic truth—viz., its Gödel sentence—not provable in it, but which can be established as true by intuitively correct reasoning. The heart of Gödel’s theorem is, in fact, a paradox that concerns the sentence, $G$, ‘This sentence is not provable’. If $G$ is provable, then it is true and so not provable. Thus $G$ is proved. Hence $G$ is true and so unprovable. If an underlying paraconsistent logic is used to formalise the arithmetic, and the theory therefore allowed to be inconsistent, the Gödel sentence may well be provable in the theory (essentially by the above reasoning). So a paraconsistent approach to arithmetic may overcome the limitations that are supposed (by many) to follow from Gödel’s theorem. For other ‘limitative’ theorems of metamathematics, see Priest (2002). For some of the original work by Meyer applying paraconsistent logic to arithmetic, and new commentaries and developments, see the collection Ferguson and Priest (2021).

### 2.5 Vagueness

From the start, paraconsistent logics were intended in part to deal with problems of vagueness and the Sorites paradox (Jaśkowski 1948 [1969])[^jaśkowski-1948]. Some empirical evidence suggest that vagueness in natural language is a good candidate for paraconsistent treatment (Ripley 2011)[^ripley-2011].

A few different paraconsistent approaches to vagueness have been suggested. *Subvaluationism* is the logical dual to supervaluationism: if a claim is true on *some* acceptable sharpening of a vague predicate, then it is true. Where the supervaluationist sees indeterminacy, or truth-value gaps, the subvaluationist sees overdeterminacy, truth-value gluts. A subvaluation logic will, like its supervaluational dual, preserve all classical tautologies, as long as the definition of validity is restricted to the non-glutty cases. Because it is so structurally similar to supervaluationism, subvaluationism is also subject to most of the same criticisms (Hyde 1997)[^hyde-1997].

More broadly, (dialetheic) paraconsistency has been used in straightforward three-valued truth-functional approaches to vagueness. The aim is to preserve both of the following intuitive claims:

1. *Tolerance*: For vague $F$, it is not the case that $x$ is $F$ but some very $F$-similar $x$ is not $F$
2. *Cutoffs*: For all $F$, if some $x$ is $F$ and some $y$ is not, and there is an ordered $F$-progression from $x$ to $y$, then there is some last $F$ and some first non-$F$

Again, the key to the analysis is to take cutoffs as sites for inconsistency, for objects both F and not F. Then all tolerance claims (about vague F) are taken as true; but since, paraconsistently, the inference of disjunctive syllogism is not generally valid, these claims do not imply absurdities like ‘everyone is bald’. Paraconsistent models place a great deal of emphasis on cutoff points of vague predicates, attributing much of the trouble with the Sorites paradox to underlying inconsistency of vague predicates (Weber 2010a)[^weber-2010a].

There is debate as to whether the Sorites paradox is of a kind with the other well-known semantic and set theoretic paradoxes, like Russell’s and the liar. If it is, then a paraconsistent approach to one would be as natural as to the other.

## 3. Systems of Paraconsistent Logic

A number of formal techniques to invalidate ECQ have been devised. As the interest in paraconsistent logic grew, different techniques developed in different parts of the world. As a result, the development of the techniques has somewhat a regional flavour (though there are, of course, exceptions, and the regional differences can be over-exaggerated; see Tanaka 2003)[^tanaka-2003]. Some of these have been summarised in Brown (2002) and Priest (2002). The list of systems canvassed here is by no means exhaustive.

Most paraconsistent logicians do not propose a wholesale rejection of classical logic. They usually accept the validity of classical inferences in consistent contexts. It is the need to isolate an inconsistency without spreading everywhere that motivates the rejection of ECQ. Depending on how much revision one thinks is needed, we have a technique for paraconsistency. The taxonomy given here is based on the degree of revision to classical logic. (On comparing paraconsistent logics based on proximity to classical logic, see Arieli, Avron and Zamansky (2011) and for more methodological concerns Wansing and Odinstov (2016).) Since the logical novelty can be seen at the propositional level, we will concentrate on the propositional paraconsistent logics.

### 3.1 Discussive Logic

The first formal paraconsistent logic to have been developed was *discussive* (or *discursive*) *logic* by the Polish logician Jaśkowski (1948). The thought behind discussive logic is that, in a discourse, each participant puts forward some information, beliefs or opinions. Each assertion is true according to the participant who puts it forward in a discourse. But what is true in a discourse on whole is the sum of assertions put forward by participants. Each participant’s opinions may be self-consistent, yet may be inconsistent with those of others. Jaśkowski formalised this idea in the form of discussive logic.

A formalisation of discussive logic is by means of modelling a discourse in a modal logic. For simplicity, Jaśkowski chose *S*5. We think of each participant’s belief set as the set of sentences true at a world in an *S*5 model $M$. Thus, a sentence $A$ asserted by a participant in a discourse is interpreted as “it is possible that $A$” or a sentence $\Diamond A$ of *S*5. Then $A$ holds in a discourse iff $A$ is true at some world in $M$. Since $A$ may hold in one world but not in another, both $A$ and $\neg A$ may hold in a discourse. Indeed, one should expect that participants disagree on some issue in a rational discourse. The idea, then, is that $B$ is a discussive consequence of $A_1, \ldots, A_n$ iff $\Diamond B$ is an *S*5 consequence of $\Diamond A_{1}, \ldots, \Diamond A_{n}$.

To see that discussive logic is paraconsistent, consider an *S*5 model, $M$, such that $A$ holds at $w_1$, $\neg A$ holds at a different world $w_2$, but $B$ does not hold at any world for some $B$. Then both $A$ and $\neg A$ hold, yet $B$ does not hold in $M$. Hence discussive logic invalidates ECQ.

However, there is no *S*5 model where $A \wedge \neg A$ holds at some world. So an inference of the form $\{A \wedge \neg A\} \vDash B$ is valid in discussive logic. This means that, in discussive logic, *adjunction* $(\{A, \neg A\} \vDash A \wedge \neg A)$ fails. But one can define a discussive conjunction, $\wedge_d$, as $A \wedge \Diamond B$ (or $\Diamond A \wedge B)$. Then adjunction holds for $\wedge_d$ (Jaśkowski 1949)[^jaśkowski-1949].

One difficulty is a formulation of a conditional. In *S*5, the inference from $\Diamond p$ and $\Diamond(p \supset q)$ to $\Diamond q$ fails. Jaśkowski chose to introduce a connective which he called *discussive implication*, $\supset_d$, defined as $\Diamond A \supset B$. This connective can be understood to mean that “if some participant states that $A$, then $B$”. As the inference from $\Diamond A \supset B$ and $\Diamond A$ to $\Diamond B$ is valid in *S*5, *modus ponens* for $\supset_d$ holds in discussive logic. A discussive bi-implication, $\equiv_d$, can also be defined as $(\Diamond A \supset B) \wedge \Diamond(\Diamond B \supset A)$ (or $\Diamond(\Diamond A \supset B) \wedge (\Diamond B \supset A))$. For some history of work on Jaśkowski’s logic and axiomatizations thereof, see Omori and Alama (2018).

### 3.2 Non-Adjunctive Systems

A non-adjunctive system is a system that does not validate adjunction (i.e., $\{A, B\} \not\vDash A \wedge B)$. As we saw above, discussive logic without a discussive conjunction is non-adjunctive. Another non-adjunctive strategy was suggested by Rescher and Manor (1970). In effect, we can conjoin premises, but only up to maximal consistency. Specifically, if $\Sigma$ is a set of premises, a maximally consistent subset is any consistent subset $\Sigma '$ such that if $A \in \Sigma - \Sigma '$ then $\Sigma ' \cup \{A\}$ is inconsistent. Then we say that $A$ is a consequence of $\Sigma$ iff $A$ is a classical consequence of $\Sigma '$ for some maximally consistent subset $\Sigma '$. Then $\{p, q\} \vDash p \wedge q$ but $\{p, \neg p\} \not\vDash p \wedge \neg p$.

### 3.3 Preservationism

In the non-adjunctive system of Rescher and Manor, a consequence relation is defined over some maximally consistent subset of the premises. This can be seen as a way to measure the *level* of consistency in the premise set. The level of $\{p, q\}$ is 1 since the maximally consistent subset is the set itself. The level of $\{p, \neg p\}$, however, is 2: $\{p\}$ and $\{\neg p\}$.

If we define a consequence relation over some maximally consistent subset, then the relation can be thought of as preserving the level of consistent fragments. This is the approach which has come to be called *preservationism*. It was first developed by the Canadian logicians Ray Jennings and Peter Schotch; see Schotch et al. (2009).

To be more precise, a (finite) set of formulas, $\Sigma$, can be partitioned into classically consistent fragments whose union is $\Sigma$. Let $\vdash$ be the classical consequence relation. A *covering* of $\Sigma$ is a set $\{\Sigma_i : i \in I\}$, where each member is consistent, and $\Sigma = \bigcup_{i \in I} \Sigma_i$. The *level* of $\Sigma$, $l(\Sigma)$, is the least $n$ such that $\Sigma$ can be partitioned into $n$ sets if there is such $n$, or $\infty$ if there is no such $n$. A consequence relation, called *forcing*, $\Vdash$, is defined as follows. $\Sigma\Vdash A$ iff $l(\Sigma) = \infty$, or $l(\Sigma) = n$ and for every covering of size $n$ there is a $j \in I$ such that $\Sigma_j \vdash A$. If $l(\Sigma) = 1$ or $\infty$ then the forcing relation coincides with classical consequence relation. In case where $l(\Sigma) = \infty$, there must be a sentence of the form $A \wedge \neg A$ and so the forcing relation explodes.

A chunking strategy has also been applied to capture the inferential mechanism underlying some theories in science and mathematics. In mathematics, the best available theory concerning infinitesimals was inconsistent. In the original calculus of Leibniz, in the calculation of a derivative infinitesimals had to be both zero and non-zero. (Cf. Colyvan 2012, chapter 7. Newton used what he called ‘fluxions’, which play a similar role.)[^colyvan-2012] In order to capture the inference mechanism underlying this (and Bohr’s theory of the atom), we need to add to the chunking a mechanism that allows a limited amount of information to flow between the consistent fragments of these inconsistent but non-trivial theories. That is, certain information from one chunk may permeate into other chunks. The inference procedure underlying the theories must be *Chunk and Permeate*.

Let $C = \{\Sigma_i : i \in I\}$ and $\varrho$ a permeability relation on $C$ such that $\varrho$ is a map from $I \times I$ to subsets of formulas of the language. If $i_0 \in I$, then any structure $\langle C, \varrho , i_0\rangle$ is called a C&P structure on $\Sigma$. If $\mathcal{B}$ is a C&P structure on $\Sigma$, we define the C&P consequences of $\Sigma$ with respect to $\mathcal{B}$, as follows. For each $i \in I$, a set of sentences, $\Sigma_i^n$, is defined by recursion on $n$:

$$ \begin{align*} \Sigma_i^{0} & = \Sigma_i^{\vdash} \\ \Sigma_i^{n+1} & = \left( \Sigma_i^n \cup \bigcup_{j \in I} \left(\Sigma_j^n \cap \rho(j,i)\right) \right)^{\vdash} \\ \end{align*} $$

That is, $\Sigma_i^{n+1}$ comprises the consequences from $\Sigma_i^n$ together with the information that permeates into chunk $i$ from the other chunk at level $n$. We then collect up all finite stages:

$$ \Sigma_i^{\omega} = \bigcup_{n \lt \omega} \Sigma_i^n $$

The C&P consequences of $\Sigma$ can be defined in terms of the sentences that can be inferred in the designated chunk $i_0$ when all appropriate information has been allowed to flow along the permeability relations (see Brown & Priest 2004, 2015.)[^brown-2004][^priest-2004]

### 3.4 Adaptive Logics

One may think not only that an inconsistency needs to be isolated but also that a serious need for the consideration of inconsistencies is a rare occurrence. The thought may be that consistency is the norm until proven otherwise: we should treat a sentence or a theory as consistently as possible. This is essentially the motivation for *adaptive logics*, pioneered by Diderik Batens in Belgium.

An adaptive logic is a logic that adapts itself to the situation at the time of application of inference rules. It models the dynamics of our reasoning. There are two senses in which reasoning is dynamic: external and internal. Reasoning is *externally* dynamic if as new information becomes available expanding the premise set, consequences inferred previously may have to be withdrawn. The external dynamics is thus the *non-monotonic* character of some consequence relations: $\Gamma \vdash A$ and $\Gamma \cup \Delta \not\vdash A$ for some $\Gamma , \Delta$ and $A$. However, even if the premise-set remains constant, some previously inferred conclusion may be considered as not derivable at a later stage. As our reasoning proceeds from a premise set, we may encounter a situation where we infer a consequence provided that no abnormality, in particular no contradiction, obtains at some stage of the reasoning process. If we are forced to infer a contradiction at a later stage, our reasoning has to adapt itself so that an application of the previously used inference rule is withdrawn. In such a case, reasoning is *internally* dynamic. Our reasoning may be internally dynamic if the set of valid inferences is not recursively enumerable (i.e., there is no decision procedure that leads to ‘yes’ after finitely many steps if the inference is indeed valid). It is the internal dynamics that adaptive logics are devised to capture.

In order to illustrate the idea behind adaptive logics, consider the premise set $\Gamma = \{p, \neg p \vee r, \neg r \vee s, \neg s, s \vee t\}$. One may start reasoning with $\neg s$ and $s \vee t$, using the Disjunctive Syllogism (DS) to infer $t$, given that $s \wedge \neg s$ does not obtain. We then reason with $p$ and $\neg p \vee r$, to infer $r$ with the DS, given that $p \wedge \neg p$ does not obtain. Now, we can apply the DS to $\neg r \vee s$ and $r$ to derive $s$, provided that $r \wedge \neg r$ does not obtain. However, by conjoining $s$ and $\neg s$, we can obtain $s \wedge \neg s$. Hence we must withdraw the first application of DS, and so the proof of $t$ lapses. A consequence of this reasoning is what cannot be defeated at any stage of the process.

A system of adaptive logic can generally be characterised as consisting of three elements:

1. A lower limit logic (LLL)
2. A set of abnormalities
3. An adaptive strategy

LLL is the part of an adaptive logic that is not subject to adaptation. It consists essentially of a number of inferential rules (and/or axioms) that one is happy to accept regardless of the situation in a reasoning process. A set of abnormalities is a set of formulas that are presupposed as not holding (or as absurd) at the beginning of reasoning until they are shown to be otherwise. For many adaptive logics, a formula in this set is of the form $A \wedge \neg A$. An adaptive strategy specifies a strategy of handling the applications of inference rules based on the set of abnormalities. If LLL is extended with the requirement that no abnormality is logically possible, one obtains the upper limit logic (ULL). ULL essentially contains not only the inferential rules (and/or axioms) of LLL but also supplementary rules (and/or axioms) that can be applied in the absence of abnormality, such as DS. By specifying these three elements, one obtains a system of adaptive logic.

### 3.5 Logics of Formal Inconsistency

The approaches taken for motivating the systems of paraconsistent logic which we have so far seen isolate inconsistency from consistent parts of the given theory. The aim is to retain as much classical machinery as possible in developing a system of paraconsistent logic which, nonetheless, avoids explosion when faced with a contradiction. One way to make this aim explicit is to extend the expressive power of our language by encoding the metatheoretical notions of consistency (and inconsistency) in the object language. The *Logics of Formal Inconsistency* (*LFIs*) are a family of paraconsistent logics that constitute consistent fragments of classical logic yet which reject the explosion principle where a contradiction is present. The investigation of this family of logics was initiated by Newton da Costa in Brazil.

An effect of encoding consistency (and inconsistency) in the object language is that we can explicitly separate inconsistency from triviality. With a language rich enough to express inconsistency (and consistency), we can study inconsistent theories without assuming that they are necessarily trivial. This makes it explicit that the presence of a contradiction is a separate issue from the non-trivial nature of paraconsistent inferences.

The thought behind *LFIs* is that we should respect classical logic as much as possible. It is only when there is a contradiction that logic should deviate from it. This means that we can admit the validity of ECQ in the absence of contradictions. In order to do so, we encode ‘consistency’ into our object language by $\circ$. Then $\vdash$ is a consequence relation of an *LFI* iff

1. $\exists \Gamma \exists A\exists B(\Gamma , A, \neg A \not\vdash B)$ and
2. $\forall \Gamma \forall A\forall B(\Gamma, \circ A, A, \neg A \vdash B)$.

Let $\vdash_C$ be the classical consequence (or derivability) relation and $\circ (\Gamma)$ express the consistency of the set of formulas $\Gamma$ such that if $\circ A$ and $\circ B$ then $\circ (A * B)$ where $*$ is any two place logical connective. Then we can capture derivability in the consistent context in terms of the equivalence: $\forall \Gamma \forall B\exists \Delta(\Gamma \vdash_C B$ iff $\circ (\Delta), \Gamma \vdash B)$.

Now take the positive fragment of classical logic with *modus ponens* plus double negation elimination $(\neg \neg A \rightarrow A)$ as an axiom and some axioms governing $\circ$:

$$ \begin{align*} \circ A & \rightarrow(A \rightarrow(\neg A \rightarrow B)) \\ (\circ A \wedge \circ B) &\rightarrow \circ (A \wedge B) \\ (\circ A \rightarrow \circ B) &\rightarrow \circ (A \rightarrow B) \end{align*} $$

Then $\vdash$ provides da Costa’s system $C_1$. If we let $A^1$ abbreviate the formula $\neg(A \wedge \neg A)$ and $A^{n+1}$ the formula $(\neg(A^n \wedge \neg A^n ))^1$, then we obtain $C_i$ for each natural number $i$ greater than 1.

To obtain da Costa’s system $C_{\omega}$, instead of the positive fragment of classical logic, we start with positive intuitionist logic. $C_i$ systems for finite $i$ do not rule out $(A^n \wedge \neg A^n \wedge A^{n+1})$ from holding in a theory. By going up the hierarchy to $\omega$, $C_{\omega}$ rules out this possibility. Note, however, that $C_{\omega}$ is not a *LFC* as it does not contain classical positive logic. For the semantics for da Costa’s $C$-systems, see for example da Costa and Alves (1977) and Loparic (1977).

The LFIs are a powerful expansion of these ideas. A comprehensive overview and further work in this tradition is in Carnielli and Coniglio (2016). Further work on looking for consistency or recovery operators is in Barrio and Carnielli (2020).

### 3.6 Many-Valued Logics

Perhaps the simplest way of generating a paraconsistent logic, first proposed by Asenjo in his PhD dissertation, is to use a many-valued logic. Classically, there are exactly two truth values. The many-valued approach is to drop this classical assumption and allow more than two truth values. The simplest strategy is to use three truth values: *true (only)*, *false (only)* and *both (true and false)* for the evaluations of formulas. The truth tables for logical connectives, except conditional, can be given as follows:

| $\neg$ |   |
| --- | --- |
| $t$ | $f$ |
| $b$ | $b$ |
| $f$ | $t$ |

| $\wedge$ | $t$ | $b$ | $f$ |
| --- | --- | --- | --- |
| $t$ | $t$ | $b$ | $f$ |
| $b$ | $b$ | $b$ | $f$ |
| $f$ | $f$ | $f$ | $f$ |

| $\vee$ | $t$ | $b$ | $f$ |
| --- | --- | --- | --- |
| $t$ | $t$ | $t$ | $t$ |
| $b$ | $t$ | $b$ | $b$ |
| $f$ | $t$ | $b$ | $f$ |

These tables are essentially those of Łukasiewicz’s and Kleene’s strong three valued logics where the middle value is thought of as *indeterminate* or *neither (true nor false)*.

For a conditional $\supset$, following Kleene’s strong three valued logic, we might specify a truth table as follows:

| $\supset$ | $t$ | $b$ | $f$ |
| --- | --- | --- | --- |
| $t$ | $t$ | $b$ | $f$ |
| $b$ | $t$ | $b$ | $b$ |
| $f$ | $t$ | $t$ | $t$ |

Let $t$ and $b$ be the *designated* values. These are the values that are preserved in valid inferences. If we define a consequence relation in terms of preservation of these designated values, then we have the paraconsistent logic *LP* (Priest 1979)[^priest-1979]. In *LP*, ECQ is invalid. To see this, we assign $b$ to $p$ and $f$ to $q$. Then $\neg p$ is also evaluated as $b$ and so both $p$ and $\neg p$ are designated. Yet $q$ is not evaluated as having a designated value. Hence ECQ is invalid in *LP*.

As we can see, *LP* invalidates ECQ by assigning a designated value, *both true and false*, to a contradiction. Thus, *LP* departs from classical logic more so than the systems that we have seen previously, and is often aligned with dialetheism. However, we can interpret truth values not in an aletheic sense but in an epistemic sense: truth values (or designated values) express epistemic or doxastic commitments (see for example Belnap 1992)[^belnap-1992]. Or we might think that the value *both* is needed for a semantic reason: we might be required to express the contradictory nature of some of our beliefs, assertions and so on (see Dunn 1976: 157)[^dunn-1976]. If this interpretative strategy is successful, we can separate *LP* from necessarily falling under dialetheism.

One feature of *LP* which requires some attention is that in *LP* *modus ponens* comes out to be invalid. For if $p$ is both true and false but $q$ false (only), then $p \supset q$ is both true and false and hence is designated. So both $p$ and $p \supset q$ are designated, yet the conclusion $q$ is not. Hence *modus ponens* for $\supset$ is invalid in *LP*. (One way to rectify the problem is to add an appropriate conditional connective as we will see in the section on relevant logics.)

Another way to develop a many-valued paraconsistent logic is to think of an assignment of a truth value not as a function but as a *relation*. Let $P$ be the set of propositional parameters. Then an evaluation, $\eta$, is a subset of $P \times \{0, 1\}$. A proposition may only relate to 1 (true), it may only relate to 0 (false), it may relate to both 1 and 0 or it may relate to neither 1 nor 0. The evaluation is extended to a relation for all formulas by the following recursive clauses:

$$ \begin{align*} \neg A\eta 1 & \textrm{ iff }A\eta 0\\ \neg A\eta 0 & \textrm{ iff }A\eta 1\\ A \wedge B\eta 1 & \textrm{ iff }A\eta 1\textrm{ and }B\eta 1\\ A \wedge B\eta 0 & \textrm{ iff }A\eta 0\textrm{ or }B\eta 0\\ A \vee B\eta 1 & \textrm{ iff }A\eta 1\textrm{ or }B\eta 1\\ A \vee B\eta 0 & \textrm{ iff }A\eta 0\textrm{ and }B\eta 0\\ \end{align*} $$

If we define validity in terms of truth preservation under all relational evaluations then we obtain *First Degree Entailment* (*FDE*) which is a fragment of relevant logics. These relational semantics for *FDE* are due to Dunn (1976), from his 1966 PhD dissertation, with precedents in 1957 by Białynicki-Birula and Rasiowa. (For recent work see also Omori and Wansing (2017).) A different approach is explored through the idea of non-deterministic matrices, studied by Avron and his collaborators (for example, Avron & Lev 2005)[^avron-2005].

### 3.7 Relevant Logics

The approaches to paraconsistency we have examined above all focus on the inevitable presence or the truth of some contradictions. A rejection of ECQ, in these approaches, depends on an analysis of the premises containing a contradiction. One might think that the real problem with ECQ is not to do with the contradictory premises but to do with the lack of connection between the premises and the conclusion. The thought is that the conclusion must be *relevant* to the premises in a valid inference.

Relevant logics were pioneered in order to study the relevance of the conclusion with respect to the premises by Anderson and Belnap (1975) in Pittsburgh, following work by Ackermann in 1956. Anderson and Belnap motivated the development of relevant logics using natural deduction systems; yet they developed a family of relevant logics in axiomatic systems. As development proceeded and was carried out also in Australia, more focus was given to the semantics.

The semantics for relevant logics were developed by Routley and Routley (1972), Routley and Meyer (1972), Urquhart (1972), Maksimova (1973), and Fine (1974). (There are also algebraic semantics; see for example Dunn & Restall 2002: 48ff and references therein.)[^dunn-2002] Routley-Meyer semantics is based on possible-world semantics, which is the most studied semantics for relevant logics, especially in Australasia. In this semantics, conjunction and disjunction behave in the usual way. But each world, $w$, has an associate world, $w^*$, and negation is evaluated in terms of $w^*: \neg A$ is true at $w$ iff $A$ is false, not at $w$, but at $w^*$. Thus, if $A$ is true at $w$, but false at $w^*$, then $A \wedge \neg A$ is true at $w$. To obtain the standard relevant logics, one needs to add the constraint that $w^{**} = w$. As is clear, negation in these semantics is an intensional operator.

The primary concern with relevant logics is not so much with negation as with relevant implication $\rightarrow$ (satisfying *modus ponens*). In relevant logics, if $A \rightarrow B$ is a logical truth, then $A$ is relevant to $B$, in the sense that $A$ and $B$ share at least one propositional variable.

Semantics for the relevant conditional are obtained by furnishing each Routley-Meyer model with a *ternary* relation. In the simplified semantics of Priest and Sylvan (1992) and Restall (1993, 1995), worlds are divided into normal and non-normal. If $w$ is a normal world, $A \rightarrow B$ is true at $w$ iff at all worlds where $A$ is true, $B$ is true. If $w$ is non-normal, $A \rightarrow B$ is true at $w$ iff for all $x, y$, such that $Rwxy$, if $A$ is true at $x, B$ is true at $y$. If $B$ is true at $x$ but not at $y$ where $Rwxy$, then $B \rightarrow B$ is not true at $w$. Then one can show that $A \rightarrow (B \rightarrow B)$ is not a logical truth. (Validity is defined as truth preservation over *normal* worlds.) This gives the basic relevant logic, $B$. Stronger logics, such as the logic $R$, are obtained by adding constraints on the ternary relation.

There are also versions of world-semantics for relevant logics based on Dunn’s relational semantics for *FDE*. Then negation is extensional. A conditional connective now needs to be given both truth and falsity conditions. So we have: $A \rightarrow B$ is true at $w$ iff for all $x, y$, such that $Rwxy$, if $A$ is true at $x, B$ is true at $y$; and $A \rightarrow B$ is false at $w$ iff for some $x, y$, such that $Rwxy$, if $A$ is true at $x, B$ is false at $y$. Adding various constraints on the ternary relation provides stronger logics. However, these logics are not the standard relevant logics developed by Anderson and Belnap. To obtain the standard family of relevant logics, one needs neighbourhood frames (see Mares 2004)[^mares-2004]. Further details can be found in the entry on relevant logics.

## 4. Further Work

Work on paraconsistent logic in the 21st century continues to develop and spread in many directions: technically, philosophically, and geographically. Here we briefly mention only a few examples.

*Contradictory Logics.* Recent research projects have focused on systems with inconsistencies at the level of logic. For example, a connexive logic with Boethius’ Thesis $(A \rightarrow B) \rightarrow \neg(A \rightarrow \neg B)$ and conjunctive simplification $(A \wedge B) \rightarrow A $, $(A \wedge B) \rightarrow B $ will yield a contradiction: $$ \begin{align*} & (A \wedge \neg A) \rightarrow \neg A \\ & \neg((A \wedge \neg A) \rightarrow \neg A) \\ \end{align*} $$ where the first line is an instance of simplification, and the second line is from applying Boetheius to another instance of simplification, $ (A \wedge \neg A) \rightarrow A $. Such a logic will have contradictory tautologies. These systems are often studied in tandem with connexive logics but there are other examples too. This has been developed especially by the Bochum Logic Group; see Wansing et al. (2025) and Wansing (2026).

*Metainferences.* From substructural logics (see entry on substructural logic) comes the thought that logics are made up of distinct entities: standard inferences, and then inferences between inferences. And then (perhaps) there are distinct inferences between metainferences, and so on, leading to investigations of a hierarchy of metainferences, with some potentially arresting philosophical implications about how to characterize a logic. Many of the logics studied in this work are paraconsistent, connecting back to ideas from Ripley (2012). This has been developed especially by the Buenos Aires Logic Group; see Teijeiro and Barrio (2026).

*Natural language indicative conditionals.* Research by Égré, Rossi, and Sprenger on the natural language indicative conditional has led to fruitful developments of trivalent semantics, with natural links to probabilistic reasoning and connexive logic; see for example Égré et al. (2025).

Further work is actively underway.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

### References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

### World Congress of Paraconsistency Volumes

- [First Congress] Batens, Diderik, Chris Mortensen, Graham Priest, and Jean-Paul van Bendegem (eds.), 2000, *Frontiers of Paraconsistent Logic* (Studies in Logic and Computation 8), Baldock, England: Research Studies Press.
- [Second Congress] Carnielli, Walter A., M. Coniglio, and Itala Maria Lof D’ottaviano (eds.), 2002, *Paraconsistency: the Logical Way to the Inconsistent* (Lecture Notes in Pure and Applied Mathematics: Volume 228), Boca Raton: CRC Press.
- [Third Congress] Beziau, Jean-Yves, Walter A. Carnielli, and Dov M. Gabbay (eds.), 2007, *Handbook of Paraconsistency* (Studies in Logic 9), London: College Publications.
- [Fourth Congress] Tanaka, Koji, Francesco Berto, Edwin Mares, and Francesco Paoli (eds.), 2013, *Paraconsistency: Logic and Applications* (Logic, Epistemology, and the Unity of Science 26), Dordrecht: Springer. doi:10.1007/978-94-007-4438-7
- [Fifth Congress] Beziau, Jean-Yves, Mihir Chakraborty, and Soma Dutta (eds.), 2015, *New Directions in Paraconsistent Logic*, Dordrecht: Springer. doi:10.1007/978-81-322-2719-9

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=logic-paraconsistent). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/logic-paraconsistent/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=logic-paraconsistent&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/logic-paraconsistent/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- [First World Congress on Paraconsistency](http://logica.ugent.be/centrum/events/WCP97/)
- [Second World Congress on Paraconsistency](http://www.cle.unicamp.br/index.php/?q=node/335)
- [Third World Congress on Paraconsistency](http://www.cle.unicamp.br/wcp3/index.htm)
- [Fourth World Congress on Paraconsistency](http://citeseerx.ist.psu.edu/viewdoc/download?rep=rep1&type=pdf&doi=10.1.1.183.3575)
- [Fifth World Congress on Paraconsistency](http://www.paraconsistency.org/wcp5.html)
- [Sixth World Congress of Paraconsistency](http://wcp6.umk.pl)
- [Seventh World Congress of Paraconsistency](https://sites.google.com/view/wcp7)

## Related Entries

Abelard [Abailard], Peter | Boethius, Anicius Manlius Severinus | dialetheism | Duns Scotus, John | liar paradox | logic: connexive | logic: many-valued | logic: of belief revision | logic: relevance | logic: substructural | mathematics: inconsistent | paradoxes: and contemporary logic | self-reference | Sorites paradox

### Acknowledgments

The editors and authors would like to thank Joy Britten for noticing an error in the example of adaptive logic reasoning in Section 3.4, and to Hitoshi Omori for identification and discussion of an error in the section on discussive logic Section 3.1.

[^abe-2015]: Abe, Jair Minoro, Seiki Akama, and Kazumi Nakamatsu (eds.), 2015, *Introduction to Annotated Logics: Foundations for Paracomplete and Paraconsistent Reasoning* (Intelligent Systems Reference Library 88), Dordrecht: Springer. doi:10.1007/978-3-319-17912-4

[^akama-2016]: Akama, Seiki (ed.), 2016, *Towards Paraconsistent Engineering* (Intelligent Systems Reference Library 110), Dordrecht: Springer. doi:10.1007/978-3-319-40418-9

[^anderson-1975]: Anderson, Alan Ross and Nuel D. Belnap, 1975, *Entailment: The Logic of Relevance and Necessity*, Volume 1, Princeton: Princeton University Press.

[^anderson-1992]: Anderson, Alan Ross, Nuel D. Belnap, and J. Michael Dunn, 1992, *Entailment: The Logic of Relevance and Necessity*, Volume 2, Princeton: Princeton University Press.

[^andreas-2016]: Andreas, Holger and Peter Verdée, 2016, *Logical Studies of Paraconsistent Reasoning in Science and Mathematics* (Trends in Logic 45), Dordrecht: Springer. doi:10.1007/978-3-319-40220-8

[^arieli-2011]: Arieli, Ofer and Arnon Arnon and Anna Zamansky, 2011, “Ideal Paraconsistent Logics”, *Studia Logica*, 99(1–3): 31–60.

[^arruda-1977]: Arruda, Ayda I., 1977, “On the Imaginary Logic of N.A. Vasil’év”, in Arruda et al. 1977: 3–24. doi:10.1016/S0049-237X(08)70642-6

[^arruda-1989]: –––, 1989, “Aspects of the Historical Development of Paraconsistent Logic”, in Priest et al. 1989: 99–130.

[^arruda-1977-2]: Arruda, Ayda I., Newton da Costa and R. Chuaqui (eds.), 1977, *Non-Classical Logic, Model Theory and Computability* (Studies in Logic and the Foundations of Mathematics 89), Amsterdam: North Holland.

[^asenjo-1966]: Asenjo, F.G., 1966, “A Calculus of Antinomies”, *Notre Dame Journal of Formal Logic*, 7(1): 103–105. doi:10.1305/ndjfl/1093958482

[^asmus-2012]: Asmus, Conrad, 2012, “Paraconsistency on the Rocks of Dialetheism”, *Logique et Analyse*, 55(217): 3–21. [[Asmus 2012 available online](http://virthost.vub.ac.be/lnaweb/ojs/index.php/LogiqueEtAnalyse/article/view/1812)]

[^avron-2005]: Avron, Arnon and Iddo Lev, 2005, “Non-deterministic Multi-valued Structures”, *Journal of Logic and Computation*, 15(3): 241–261.

[^barrio-2018]: Barrio, Eduardo and Bruno Da Ré, 2018, “Paraconsistency and its philosophical interpretations”, *Australasian Journal of Logic*, 15(2): 151–170.

[^barrio-2020]: Barrio, Eduardo and Walter Carnielli (eds.), 2020, *Recovery Operators in Logics of formal inconsistency*, special issue of the *Logic Journal of the IGPL*, 28(5).

[^batens-2001]: Batens, Diderik, 2001, “A General Characterization of Adaptive Logics”, *Logique et Analyse*, 44(173–175): 45–68. [[Batens 2001 available online](http://virthost.vub.ac.be/lnaweb/ojs/index.php/LogiqueEtAnalyse/article/view/1521)]

[^batens-2007]: –––, 2007, “A Universal Logic Approach to Adaptive Logics”, *Logica Universalis*, 1(1): 221–242. doi:10.1007/s11787-006-0012-5

[^batens-2020]: –––, 2020, “Adaptive Fregean Set Theory”, *Studia Logica*, 108: 903–939.

[^batens-2000]: Batens, Diderik, Chris Mortensen, Graham Priest, and Jean-Paul van Bendegem (eds.), 2000, *Frontiers of Paraconsistent Logic* (Studies in Logic and Computation 8), Baldock, England: Research Studies Press. [First World Congress proceedings]; see also [*Logique & Analyse*, Volume 41, Numbers 161–163.](http://virthost.vub.ac.be/lnaweb/ojs/index.php/LogiqueEtAnalyse/issue/view/150)

[^beall-2009]: Beall, Jc, 2009, *Spandrels of Truth*, Oxford: Oxford University Press. doi:10.1093/acprof:oso/9780199268733.001.0001

[^beall-2018]: Beall, Jc, Michael Glanzberg and Ellie Ripley, 2018, *Formal Theories of Truth*, Oxford: Oxford University Press.

[^belnap-1992]: Belnap, Nuel D., Jr., 1992, “A Useful Four-valued Logic: How a computer should think”, *Entailment: The Logic of Relevance and Necessity*, Volume II, Alan Ross Anderson, Nuel D. Belnap, Jr, and J. Michael Dunn, Princeton: Princeton University Press; first appeared as “A Useful Four-valued Logic”, *Modern Use of Multiple-valued Logic*, J. Michael Dunn and George Epstein (eds.), Dordrecht: D. Reidel, 1977: 5–37, and “How a Computer Should Think”, *Contemporary Aspects of Philosophy*, Gilbert Ryle (ed.), Oriel Press, 1977: 30–; reprinted in Omori and Wansing (2019a). doi:10.1007/978-94-010-1161-7_2

[^besnard-1998]: Besnard, Philippe and Anthony Hunter (eds.), 1998, *Reasoning with Actual and Potential Contradictions*, (Handbook of Defeasible Reasoning and Uncertainty Management Systems, volume 2), Dordrecht: Kluwer Academic Publishers. doi:10.1007/978-94-017-1739-7

[^beziau-2007]: Beziau, Jean-Yves, Walter A. Carnielli, and Dov M. Gabbay (eds.), 2007, *Handbook of Paraconsistency* (Studies in Logic 9), London: College Publications. [Third World Congress proceedings]

[^beziau-2015]: Beziau, Jean-Yves, Mihir Chakraborty, and Soma Dutta (eds.), 2015, *New Directions in Paraconsistent Logic*, Dordrecht: Springer. doi:10.1007/978-81-322-2719-9 [Fifth World Congress proceedings]

[^bimbó-2019]: Bimbó, Katalin, 2019, “Default Rules in the Logic of First-Degree Entailments”, in Omori and Wansing 2019a: 147–154.

[^brady-1989]: Brady, Ross T., 1989, “The Non-Triviality of Dialectical Set Theory”, in Priest et al. 1989: 437–471.

[^brady-2003]: ––– (ed.), 2003, *Relevant Logics and Their Rivals*, Volume 2, Aldershot: Ashgate.

[^brady-2006]: –––, 2006, *Universal Logic*, Stanford, CA: CSLI Publications.

[^brown-2002]: Brown, Bryson, 2002, “On Paraconsistency”, in *A Companion to Philosophical Logic*, Dale Jacquette (ed.), Oxford: Blackwell, pp. 628–650. doI:10.1002/9780470996751.

[^brown-2004]: Brown, Bryson and Graham Priest, 2004, “Chunk and Permeate: A Paraconsistent Inference Strategy. Part 1: The Infinitesimal Calculus”, *Journal of Philosophical Logic*, 33(4): 379–388. doi:10.1023/B:LOGI.0000036831.48866.12

[^brown-2015]: –––, 2015, “Chunk and Permeate II: Bohr’s Hydrogen Atom”, *European Journal for Philosophy of Science*, 5(3): 297–314.

[^cano-jorge-2025]: Cano-Jorge, Fernando, 2025, “Gates and circuits via Dunn semantics”, *Journal of Logic and Computation,*35(4).

[^carnielli-2016]: Carnielli, Walter A. and Marcelo Esteban Coniglio, 2016, *Paraconsistent Logic: Consistency, Contradiction and Negation*, Dordrecht: Springer. doi:10.1007/978-3-319-33205-5

[^carnielli-2007]: Carnielli, Walter A., Marcelo E. Coniglio, and João Marcos, 2007, “Logics of Formal Inconsistency”, in *Handbook of Philosophical Logic*, Volume 14 (Second Edition), Dov M. Gabbay and Franz Guenthner (eds.), Berlin: Springer, pp. 15–107. doi:10.1007/978-1-4020-6324-4_1

[^carnielli-2002]: Carnielli, Walter A., M. Coniglio, and Itala Maria Lof D’ottaviano (eds.), 2002, *Paraconsistency: the Logical Way to the Inconsistent* (Lecture Notes in Pure and Applied Mathematics: Volume 228), Boca Raton: CRC Press. [Second World Congress proceedings]

[^carnielli-2021]: Carnielli, Walter and Abilio Rodrigues, 2021, “On Epistemic and Ontological Interpretations of Intuitionistic and Paraconsistent Paradigms”, *Logic Journal of the IGPL*, 29(4): 569–584.

[^chomsky-1995]: Chomsky, Noam, 1995, *The Minimalist Program*, Cambridge, MA: MIT Press.

[^colyvan-2012]: Colyvan, Mark, 2012, *An Introduction to the Philosophy of Mathematics*, Cambridge: Cambridge University Press.

[^costa-1974]: da Costa, Newton C.A., 1974, “On the Theory of Inconsistent Formal Systems”, *Notre Dame Journal of Formal Logic*, 15(4): 497–510. doi:10.1305/ndjfl/1093891487

[^costa-1977]: da Costa, Newton C.A. and E.H. Alves, 1977, “Semantical Analysis of the Calculi ${\bf C}_{n}$”, *Notre Dame Journal of Formal Logic*, 18(4): 621–630. doi:10.1305/ndjfl/1093888132

[^costa-1977-2]: da Costa, Newton C.A. and L. Dubikajtis, 1977, “On Jaśkowski’s Discussive Logic”, in Arruda et al. 1977: 37–56. doi:10.1016/S0049-237X(08)70644-X

[^costa-1991]: da Costa, Newton C.A., V.S. Subrahmanian, and Carlo Vago, 1991, “The Paraconsistent Logics $\mathrm{P}\mathcal{T}$”, *Zeitschrift für Mathematische Logic und Grundlangen der Mathematik*, 37(9–12): 139–148. doi:10.1002/malq.19910370903

[^dunn-1976]: Dunn, J. Michael, 1976, “Intuitive Semantics for First Degree Entailment and ‘Coupled Trees’”, *Philosophical Studies*, 29(3): 149–68. doi:10.1007/BF00373152

[^dunn-1979]: –––, 1979, “A Theorem in 3-valued Model Theory with Connections to Number Theory, Type Theory, and Relevant Logic’”, *Studia Logica*, 38(2): 149–169. doi:10.1007/BF00373152

[^dunn-2002]: Dunn, J. Michael and Greg Restall, 2002, “Relevance Logic”, *Handbook of Philosophical Logic*, Volume 6, second edition, Dov M. Gabbay and Franz Guenthner (eds.), Dordrecht: Kluwer Academic Publishers, pp. 1–136.

[^égré-2025]: Égré, Paul and Lorenzo Rossi and Jan Sprenger, 2025, “Certain and Uncertain Inference with Indicative Conditionals”. *Australasian Journal of Philosophy*, 103(3):569–596.

[^ferguson-2021]: Ferguson, Thomas Macaulay and Graham Priest (eds.), 2021, *Robert Meyer and Relevant Arithmetic*, special issue of the *Australasian Journal of Logic*, 18(5).

[^fine-1974]: Fine, Kit, 1974, “Models for Entailment”, *Journal of Philosophical Logic*, 3(4): 347–372. doi:10.1007/BF00257480

[^girard-2016]: Girard, Patrick and Koji Tanaka, 2016, “Paraconsistent Dynamics”, *Synthese*, 193(1): 1–14. doi:10.1007/s11229-015-0740-2

[^halldén-1949]: Halldén, Sören, 1949, *The Logic of Nonsense*, Uppsala: A.-B. Lundequistska Bokhandeln.

[^hyde-1997]: Hyde, Dominic, 1997, “From Heaps and Gaps to Heaps of Gluts”, *Mind*, 106(424): 641–660. doi:10.1093/mind/106.424.641

[^incurvati-2020]: Incurvati, Luca, 2020, *Conceptions of Set and the Foundations of Mathematics*, Cambridge: Cambridge University Press.

[^jaśkowski-1948]: Jaśkowski, Stanisław, 1948 [1969], “Rachunek zdań dla systemów dedukcyjnych sprzecznych”, *Studia Societatis Scientiarum Torunensi* (Sectio A), 1(5): 55–77; an English translation appeared as “Propositional Calculus for Contradictory Deductive Systems”, *Studia Logica*, 24(1969): 143–157. (An updated translation by J. Perzanowski appeared in 1999 as “A Propositional Calculus for Inconsistent Deductive Systems”, *Logic and Logical Philosophy*, 7: 35–56.

[^jaśkowski-1949]: –––, 1949 [1999], “O koniunkcji dyskusyjnej w rachunku zdań dla systemów dedukcyjnych sprzecznych”, *Studia Societatis Scientiarum Torunensis* (Sectio A), 1(8): 171–172; an English translation appeared as “On the Discussive Conjunction in the Propositional Calculus for Inconsistent Deductive Systems”, *Logic and Logical Philosophy*, 7(1999): 57–59.

[^jockwich-2021]: Jockwich, Santiago and Giorgio Venturi, 2021, “Non-classical models of ZF”, *Studia Logica*, 109: 509–537.

[^kamide-2012]: Kamide, Norihiro and Heinrich Wansing, 2012, “Proof Theory of Nelson’s Paraconsistent Logic: A Uniform Perspective”, *Theoretical Computer Science*, 415: 1–38. doi:10.1016/j.tcs.2011.11.001

[^khomskii-2024]: Khomskii, Yuri and Hrafn Oddsson, 2024, “Paraconsistent and Paracomplete Zermelo-Fraenkel Set Theory”, *Review of Symbolic Logic* 17(4):965–995.

[^libert-2005]: Libert, Thiery, 2005, “Models for a Paraconsistent Set Theory”, *Journal of Applied Logic*, 3(1): 15–41. doi:10.1016/j.jal.2004.07.010

[^loparic-1977]: Loparic, A., 1977, “Une étude semantique de quelques calculs propositionnels”, *Comptes Rendus Hebdomadaires des Séances de l’Academie des Sciences*, 284: 835–838.

[^löwe-2015]: Löwe, Benedikt and Sourav Tarafder, 2015, “Generalized Algebra-Valued Models of Set Theory”, *Review of Symbolic Logic*, 8(1): 209–225.

[^jan-1951]: Łukasiewicz, Jan, 1951, *Aristotle’s Syllogistic: From the Standpoint of Modern Formal Logic*, Oxford: Oxford University Press.

[^maksimova-1973]: Maksimova, Larisa, 1973, “Structures with Implication”, *Algebra i logika*, 12(4): 445–467.

[^mares-2004]: Mares, Edwin D., 2004, “‘Four-Valued’ Semantics for the Relevant Logic R”, *Journal of Philosophical Logic*, 33(3): 327–341. doi:10.1023/B:LOGI.0000031375.18295.30

[^martin-1986]: Martin, Christopher J., 1986, “William’s Machine”, *Journal of Philosophy*, 83(10): 564–572. doi:10.2307/2026432

[^martin-1987]: –––, 1987, “Embarrassing Arguments and Surprising Conclusions in the Development Theories of the Conditional in the Twelfth Century”, *Gilbert De Poitiers Et Ses Contemporains*, J. Jolivet, A. De Libera (eds.), Naples: Bibliopolis, pp. 377–401.

[^martin-1996]: –––, 1996, “Impossible Positio as the Foundation of Metaphysics or, Logic on the Scotist Plan?”, *Vestigia, Imagines, Verba: Semiotics and Logic in Medieval Theological Texts*, C. Marmo (ed.), Turnhout: Brepols, pp. 255–276.

[^mcginnis-2013]: McGinnis, Nicholas D., 2013, “The Unexpected Applicability of Paraconsistent Logic: A Chomskyan Route to Dialetheism”, *Foundations of Science*, 18(4): 625–640. doi:10.1007/s10699-012-9294-7

[^michael-2016]: Michael, Michaelis, 2016, “On a ‘most telling’ Argument for Paraconsistent Logic”, *Synthese*, 193(10): 3347–3362. doi:10.1007/s11229-015-0935-6

[^mortensen-1995]: Mortensen, Chris, 1995, *Inconsistent Mathematics*, Dordrecht: Kluwer Academic Publishers.

[^omori-2015]: Omori, Hitoshi, 2015, “Remarks on Naive Set Theory Based on LP”, *Review of Symbolic Logic*, 8(2): 279–295. doi:10.1017/S1755020314000525

[^omori-2018]: Omori, Hitoshi, and Jesse Alama, 2018, “Axiomatizing Jaśkowski’s Discussive Logic D2”, *Studia Logica*, 106(6):1163–1180. doi: 10.1007/s1122.

[^omori-2017]: Omori, Hitoshi, and Heinrich Wansing (eds.), 2017, *40 Years of FDE*, special issue of *Studia Logica*, 105(6).

[^omori-2019]: ––– (eds.), 2019, *Advances in Connexive Logic*, special issue of *Logic and Logical Philosophy*, 28(3).

[^omori-2019a]: ––– (eds.), 2019a, *New Essays on Belnap-Dunn Logic*, Cham: Springer.

[^priest-1979]: Priest, Graham, 1979, “The Logic of Paradox”, *Journal of Philosophical Logic*, 8(1): 219–241. doi:10.1007/BF00258428

[^priest-1987]: –––, 1987, *In Contradiction: A Study of the Transconsistent*, Dordrecht: Martinus Nijhoff; second edition, Oxford: Oxford University Press, 2006.

[^priest-2001]: –––, 2001, “Paraconsistent Belief Revision”, *Theoria*, 67(3): 214–228. doi:10.1111/j.1755-2567.2001.tb00204.x

[^priest-2002]: –––, 2002, “Paraconsistent Logic”, in *Handbook of Philosophical Logic*, second edition, volume 6, Dov M. Gabbay and Franz Guenthner (eds.), Dordrecht: Kluwer Academic Publishers, pp. 287–393.

[^priest-2003]: –––, 2003, “Inconsistent Arithmetic: Issues Technical and Philosophical”, in *Trends in Logic: 50 Years of Studia Logica* (Studia Logica Library, volume 21), V.F. Hendricks and J. Malinowski (eds.), Dordrecht: Kluwer Academic Publishers, pp. 273–99.

[^priest-2007]: –––, 2007, “Paraconsistency and Dialetheism”, in *Handbook of the History of Logic*, Volume 8, D. Gabbay and J. Woods (eds.), Amsterdam: North Holland, pp. 129–204.

[^priest-2004]: Priest, Graham, J.C. Beall and Bradley Armour-Garb (eds.), 2004, *The Law of Non-Contradiction*, Oxford: Oxford University Press. doi:10.1093/acprof:oso/9780199265176.001.0001

[^priest-1989]: Priest, Graham, Richard Routley, and Jean Norman (eds.), 1989, *Paraconsistent Logic: Essays on the Inconsistent*, München: Philosophia Verlag.

[^priest-1992]: Priest, Graham and Richard Sylvan, 1992, “Simplified Semantics for Basic Relevant Logics”, *Journal of Philosophical Logic*, 21(2): 217–232. doi:10.1007/BF00248640

[^rescher-1970]: Rescher, Nicholas and Ruth Manor, 1970, “On Inference from Inconsistent Premises”, *Theory and Decision*, 1(2): 179–217. doi:10.1007/BF00154005

[^restall-1993]: Restall, Greg, 1993, “Simplified Semantics for Relevant Logics (and some of their rivals)”, *Journal of Philosophical Logic*, 22(5): 481–511. doi:10.1007/BF01349561

[^restall-1995]: –––, 1995, “Four-Valued Semantics for Relevant Logics (and some of their rivals)”, *Journal of Philosophical Logic*, 24(2): 139–160. doi:10.1007/BF01048529

[^restall-1995-2]: Restall, Greg and John Slaney, 1995, “Realistic Belief Revision”, *Proceedings of the Second World Conference in the Fundamentals of Artificial Intelligence*, M. De Glas and Z. Pawlak (eds.), Paris: Angkor, pp. 367–378.

[^ripley-2011]: Ripley, Ellie, 2011, “Contradictions at the Borders”, in R. Nouwen, R. van Rooij, U. Sauerland & H.-C. Schmitz (eds.), *Vagueness in Communication*, Dordrecht: Springer, pp. 169–188. doi:10.1007/978-3-642-18446-8_10

[^ripley-2012]: –––, 2012, “Conservatively extending classical logic with transparent truth”, *Review of Symbolic Logic*, 5(2): 354–378.

[^routley-1972]: Routley, Richard and Robert K. Meyer, 1972, “Semantics of Entailment (II)”, *Journal of Philosophical Logic*, 1: 192–208.

[^routley-1972-2]: Routley, Richard and Val Routley, 1972, “Semantics of First Degree Entailment”, *Noûs*, 6(4): 335–359. doi:10.2307/2214309

[^routley-1982]: Routley, Richard, Val Plumwood, Robert K. Meyer, and Ross T. Brady, 1982, *Relevant Logics and Their Rivals*, Volume 1, Ridgeview: Atascadero.

[^sedlár-2019]: Sedlár, Igor and Ondrej Majer, 2019, “Modelling Sources of Inconsistent Information in Paraconsistent Modal Logic ”, in Omori and Wansing 2019a: 293–310.

[^schotch-1980]: Schotch, P.K. and R.E. Jennings, 1980, “Inference and Necessity”, *Journal of Philosophical Logic*, 9(3): 327–340. doi:10.1007/BF00248398

[^schotch-2009]: Schotch, Peter, Bryson Brown, and Raymond Jennings (eds.), 2009, *On Preserving: Essays on Preservationism and Paraconsistent Logic*, Toronto: University of Toronto Press.

[^smiley-1959]: Smiley T.J., 1959, “Entailment and Deducibility”, *Proceedings of the Aristotelian Society*, 59: 233–254.

[^subrahmanian-1987]: Subrahmanian, V.S., 1987, “On the Semantics of Qualitative Logic Programs”, *Proc. 4th IEEE Symp. Logic Programming*, San Francisco, CA: IEEE Computer Society Press, 178–182.

[^sylvan-2000]: Sylvan, Richard, 2000, “A Preliminary Western History of Sociative Logics”, in *Sociative Logics and Their Applications: Essays by the late Richard Sylvan*, Dominic Hyde and Graham Priest (eds.), Aldershot: Ashgate Publishers, pp. 53–138.

[^teijeiro-2026]: Teijeiro, Paula and Eduardo Alejandro Barrio (eds), 2026, *Metainferences in Substructural Logics*. Springer.

[^tanaka-2003]: Tanaka, Koji, 2003, “Three Schools of Paraconsistency”, *The Australasian Journal of Logic*, 1: 28–42.

[^tanaka-2005]: –––, 2005, “The AGM Theory and Inconsistent Belief Change”, *Logique et Analyse*, 48(189–192): 113–150. [[Tanaka 2005 available online](http://virthost.vub.ac.be/lnaweb/ojs/index.php/LogiqueEtAnalyse/article/view/1614)]

[^tanaka-2013]: Tanaka, Koji, Francesco Berto, Edwin Mares, and Francesco Paoli (eds.), 2013, *Paraconsistency: Logic and Applications* (Logic, Epistemology, and the Unity of Science 26), Dordrecht: Springer. doi:10.1007/978-94-007-4438-7 [Fourth World Congress proceedings]

[^tillemans-2022]: Tillemans, Tom J.F., 2022, *Views from Tibet*, Vienna: Austrian Academy of Sciences.

[^tillemans-2016]: –––, 2016, *How Do Mādhyamikas Think?*, Somerville MA: Wisdom Publications.

[^urquhart-1972]: Urquhart, Alasdair, 1972, “Semantics for Relevant Logics”, *Journal of Symbolic Logic*, 37(1): 159–169. doi:10.2307/2272559

[^verdée-2013]: Verdée, Peter, 2013, “Strong, Universal and Provably Non-trivial Set Theory by Means of Adaptive Logic”, *Logic Journal of the IGPL*, 21(1): 108–125. doi:10.1093/jigpal/jzs025

[^wansing-2016]: Wansing, Heinrich and Sergei Odinstov, 2016, “On the Methodology of Paraconsistent Logic”, in Andreas and Verdée 2016: 175–204.

[^wansing-2025]: Wansing, Heinrich and Satoru Niki and Sergey Drobyshevich, 2025, “Bi-connexive logic, bilateralism, and negation inconsistency”, *Review of Symbolic Logic*, 18: 859–899.

[^wansing-2026]: Wansing, Heinrich, 2026, “Beyond paraconsistency: a plea for a radical breach with the Aristotelian orthodoxy in logic”, in A Rodrigues et al (ed), *Walter Carnielli on Reasoning, Paraconsistency, and Probability*. Springer.

[^weber-2010a]: Weber, Zach, 2010a, “A Paraconsistent Model of Vagueness”, *Mind*, 119(476): 1025–1045. doi:10.1093/mind/fzq071

[^weber-2010b]: –––, 2010b, “Transfinite Numbers in Paraconsistent Set Theory”, *Review of Symbolic Logic*, 3(1): 71–92. doi:10.1017/S1755020309990281

[^weber-2012]: –––, 2012, “Transfinite Cardinals in Paraconsistent Set Theory”, *Review of Symbolic Logic*, 5(2): 269–293. doi:10.1017/S1755020312000019

[^weber-2021]: –––, 2021, *Paradoxes and Inconsistent Mathematics*, Cambridge: Cambridge University Press.
