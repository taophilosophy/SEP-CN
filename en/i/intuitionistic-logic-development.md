# The Development of Intuitionistic Logic
**First published Thu Jul 10, 2008; substantive revision Wed May 4, 2022**

*van Atten, Mark*

> “Intuitionistic logic” is a term that unfortunately gains ever greater currency; it conveys a wholly false view on intuitionistic mathematics. —Freudenthal 1937

Intuitionistic logic is an offshoot of L.E.J. Brouwer’s intuitionistic mathematics. A widespread misconception has it that intuitionistic logic is the logic *underlying* Brouwer’s intuitionism; instead, the intuitionism underlies the logic, which is construed as an application of intuitionistic mathematics to language. Intuitionistic mathematics consists in the act of effecting mental constructions of a certain kind. These are themselves not linguistic in nature, but when acts of construction and their results are described in a language, the descriptions may come to exhibit linguistic patterns. Intuitionistic logic is the mathematical study of these patterns, and in particular of those that characterize valid inferences. An inference rule is valid if, whenever the statements in the premises describe truths of intuitionistic mathematics, a construction can be found that makes true the statement that is obtained by applying the rule. What the principles of logic need to preserve is therefore not, as in classical logic, mind-independent truth, but mental constructibility. Various principles of classical logic, most notably the Principle of the Excluded Middle, then become insufficiently grounded, and certain classical theorems even contradictory. The theorems in intuitionistic logic that formally contradict classical theorems depend on elements of intuitionistic mathematics that are incompatible with classical mathematics; this illustrates how in intuitionism logic is based on mathematics and not the other way around.

The systematic explanation and formalization of intuitionistic logic was begun by Brouwer’s student Arend Heyting in 1928. An “explanation” here is an account of what one knows when one understands and correctly uses the logical connectives. Since the 1970s Heyting’s explanation and its variants are known as “the Proof Interpretation”, as the role played by mind-independent truth in explanations of classical logic is here played by proof. For Heyting, a proof was primarily a mathematical construction in Brouwer’s sense, and, secondarily, a linguistic description of it. But it turned out that a Proof Interpretation can also be based on other notions of proof. The Proof Interpretation understood in a more general sense has found many applications outside its historical origin, notably in other constructive but non-intuitionistic forms of mathematics, philosophy, computer science, and linguistics. This widening of the range of application was possible because the original Proof Interpretation depends mostly on the fact that the intuitionistic notion of mathematical truth is of a verificationist nature, so that broadly verificationist theories in other domains allow for an analogous explanation of their logic.

In this article, the principal concern is with the development of the Proof Interpretation within its original context of intuitionistic mathematics. Section 1 comments on terminology. Section 2 examines the basis of Brouwer’s conception of logic in his early writings. Section 3 presents his later refinements and also his views on Hilbert’s Program, Gödel’s incompleteness theorems, and the debate in the foundations of mathematics in the 1920s. Section 4 discusses formalizations of intuitionistic logic, which had begun even before the Proof Interpretation had been made explicit, and briefly looks at mathematical interpretations of the formalisms obtained. The explanation of the Proof Interpretation in Heyting’s writings from 1930 to 1956 is treated in section 5. The sensitivity of intuitionistic logic to the exact conception of mathematical construction was at the root of strong objections to parts of the Proof Interpretation that arose from within intuitionism. These are discussed in section 6. At the end, a short list is given of topics that will be added in future updates.

## 1. Introduction

### 1.1 The Proof Interpretation

The standard explanation of intuitionistic logic today is the BHK-Interpretation (for “Brouwer, Heyting, Kolmogorov”) or Proof Interpretation as given by Troelstra and van Dalen in *Constructivism in Mathematics* (Troelstra & van Dalen 1988: 9)[^troelstra-1988]:

- (H1)A proof of $A \wedge B$ is given by presenting a proof of $A$ and a proof of $B$.
- (H2)A proof of $A \vee B$ is given by presenting either a proof of $A$ or a proof of $B$ (plus the stipulation that we want to regard the proof presented as evidence for $A \vee B$).
- (H3)A proof of $A \rightarrow B$ is a construction which permits us to transform any proof of $A$ into a proof of $B$.
- (H4)Absurdity $\bot$ (contradiction) has no proof; a proof of $\neg A$ is a construction which transforms any hypothetical proof of $A$ into a proof of a contradiction.
- (H5)A proof of $\forall xA(x)$ is a construction which transforms a proof of $d \in D$ ($D$ the intended range of the variable $x)$ into a proof of $A(d)$.
- (H6)A proof of $\exists xA(x)$ is given by providing $d \in D$, and a proof of $A(d)$.

Notions such as “construction”, “presenting” and “transformation” can be understood in different ways, and indeed they have been. Similarly, there have been different ideas as to how one may justify that concrete instances of clauses H3 and H4 indeed work for any (possibly hypothetical) proof of the antecedent. Logical principles that are valid on one understanding of these notions may not be valid on another. As Troelstra and van Dalen indicate, it is even possible to understand these clauses in such a way that they validate the principles of classical logic (Troelstra & van Dalen 1988: 9, 32–33; see also Sundholm 2004 and Sato 1997)[^sato-1997][^sundholm-2004][^troelstra-1988]. In the context of the foundational programs of intuitionism and constructivism, all notions are of course understood to be effective; but even then there is room for differences of understanding. Such differences can have mathematical consequences. On some understandings, intuitionistic logic turns out formally to be a subsystem of classical logic (namely, classical logic without the Principle of the Excluded Middle). But that is not the understanding of intuitionistic mathematicians, who, in analysis, have constructed intuitionistically valid instances of the schema $\neg \forall x(Px \vee \neg Px)$, while classically there can be none (see the section on Strong counterexamples and the Creating Subject (3.3), below).

Troelstra and van Dalen specify that the clauses H1–H6 go back to Heyting’s explanation from 1934 (hence “H”). Heyting’s aim had been to clarify the conception of logic in Brouwer’s foundational program in mathematics, which would motivate adding the following clause:

- (H0) A proof of an atomic proposition $A$ is given by presenting a mathematical construction in Brouwer’s sense that makes $A$ true.

Indeed, as we will see, a version of the Proof Interpretation is implicit already in Brouwer’s early writings from 1907 and 1908, and was notably used by him in his proofs of the bar theorem from 1924 and 1927, which predate Heyting’s papers on logic. We will therefore begin our account of the historical development of intuitionistic logic with Brouwer’s ideas, and then show how, via Heyting and others, the modern Proof Interpretation was arrived at.

### 1.2 Interpretation, Explanation, and Names

As Sundholm (1983: 159)[^sundholm-1983] points out, in the terms “BHK-Interpretation” and “Proof Interpretation” it would be appropriate to replace “Interpretation” by “Explanation”. For in a logical-mathematical context, “interpretation” has come to refer to the interpretation of one formal theory in another.[^note-1] An interpretation of a formal system $U$ in a formal system $V$ is given by a translation $'$ of formulas of $U$ to formulas of $V$ that preserves provability:[^note-2]

$$ \textrm{If } U \vdash A \textrm{ then } V \vdash A' $$

For the moment, we note that the BHK-Interpretation or Proof Interpretation is not an interpretation in this mathematical sense, but is rather a meaning explanation; we will come back to such interpretations and their difference from explanations in Section 2 of the supplementary document The Turn to Heyting’s Formalized Logic and Arithmetic.

While accepting Sundholm’s point, we keep the terms themselves, considering that they have perhaps become too common to change. Section 5.3 below is the appropriate place to explain our preference for “Proof Interpretation” over “BHK-Interpretation”.

The name “Proof Interpretation” for the explanation that Heyting published in the 1930s and later seems to have made its first appearance in print only in 1973, in papers by van Dalen and Kleene, presented at the same conference (van Dalen 1973a; Kleene 1973)[^kleene-1973]. Heyting himself spoke simply of the “interpretation” (1958A: 107; 1974: 87) or “the intuitionistic interpretation” (1958A: 110) of logic.

The name “BHK-Interpretation” was coined by Troelstra (1977: 977)[^troelstra-1977], where “K” initially stood for “Kreisel” (because of Kreisel 1962)[^kreisel-1962], later for “Kolmogorov”, e.g., in Troelstra 1990: 6; this replacement is, in keeping with Sundholm’s point, a correction.

## 2. Brouwer’s Views on Logic in 1907 and 1908

### 2.1 Mathematics, Language, and Logic

In his dissertation (1907), Brouwer presents his conception of the relations between mathematics, language, and logic. Both the intuitionistic view of logic as essentially sterile, and the existence of results in intuitionistic logic that are incompatible with classical logic, depend essentially on that conception.

For Brouwer, pure mathematics consists primarily in the act of making certain mental constructions (Brouwer 1907: 99n.1 [1975: 61n.1])[^brouwer-1907].[^note-3] The point of departure for these constructions is the intuition of the flow of time.[^note-4] This intuition, when divested from all sensuous content, allows us to perceive the form “one thing and again a thing, and a continuum in between”. Brouwer calls this form, which unites the discrete and the continuous, “the empty two-ity”. It is the basic intuition of mathematics; the discrete cannot be reduced to the continuous, nor the continuous to the discrete (Brouwer 1907: 8 [1975: 17])[^brouwer-1907].

As time flows on, an empty two-ity can be taken as one part of a new two-ity, and so on. The development of intuitionistic mathematics consists in the exploration which specific constructions the empty two-ity and its self-unfolding or iteration allows and which not:

> The only possible foundation of mathematics must be sought in this construction under the obligation carefully to watch which constructions intuition allows and which not. (Brouwer 1907: 77 [1975: 52])[^brouwer-1907]

or, in Heyting’s words,

> [Brouwer’s] construction of intuitionist mathematics is nothing more nor less than an investigation of the utmost limits which the intellect can attain in its self-unfolding. (Heyting 1968A: 314)

Brouwer and other intuitionists have shown how on this basis arithmetic, real analysis, and topology can be constructed. Moreover, Brouwer considers any exact thought that is not itself mathematics an application of mathematics. For whenever we consciously think of two things in an exact manner, that is, think them together while keeping them separate, we do so, according to Brouwer, by projecting the discrete parts of an empty two-ity onto them (Brouwer 1907: 179n.1 [1975: 97n.1])[^brouwer-1907].

Brouwer takes the intuition of time to belong to pre-linguistic consciousness. Mathematics, therefore, is essentially languageless. It is the activity of effecting non-linguistic constructions out of something that is not of a linguistic nature. Using language we can describe our mathematical activities, but these activities themselves do not depend on linguistic elements, and nothing that is true about mathematical constructional activities owes its truth to some linguistic fact. Linguistic objects such as axioms may serve to describe a mental construction, but they cannot bring it into being. For this reason, certain axioms from classical mathematics are rejected by intuitionists, such as the completeness axiom for real numbers, which says that if a non-empty set of real numbers has an upper bound, then it has a least upper bound: we know of no general method that would allow us to construct mentally the least upper bound whose existence the axiom claims.

As Brouwer later put it, “Formal language accompanies mathematics as a score accompanies a symphony by Bach or an oratorio by Handel”. (Brouwer et al. 1937: 262; translation mine)[^brouwer-1937].[^note-5] Correspondingly, establishing properties of formal systems may have many uses, but ultimately has no foundational significance for mathematics. In a lecture from 1923, Brouwer expresses optimism about Hilbert’s proof theory, but denies that it would have significance for mathematics:

> We need by no means despair of reaching this goal [of a consistency proof for formalized mathematics], but nothing of mathematical value will thus be gained: an incorrect theory, even if it cannot be inhibited by any contradiction that would refute it, is none the less incorrect, just as a criminal policy is none the less criminal even if it cannot be inhibited by any court that would curb it. (Brouwer 1924N: 3 [van Heijenoort 1967: 336])[^heijenoort-1967]

At the same time, Brouwer was well aware of the practical need for language, both in order to communicate mathematical results to others and to help ourselves in remembering and reconstructing our previous results (Brouwer 1907: 169 [1975: 92])[^brouwer-1907]. Only an ideal mathematician with perfect and unlimited memory would be able to practice pure mathematics without recourse to language (Brouwer 1933A2: 58 [van Stigt 1990: 427])[^stigt-1990]. Clearly, given these two practical functions of language, the more precise the language is, the better.

Logic, in this framework, seeks and systematizes certain patterns in the linguistic recordings of our activities of mathematical construction. It is an application of mathematics to the language of mathematics. Specifically, logic studies the patterns that characterize valid inference. The aim is to establish general rules operating on statements about mathematical constructions such that, if the original statements (the premises) convey a mathematical truth, so will the statement obtained by applying the rule (the conclusion; Brouwer 1949C: 1243). What is preserved in an inference from given premises to a conclusion is therefore not, as in classical logic, a kind of possibly evidence-transcendent truth, but constructibility. This view is quite explicit already in Brouwer’s dissertation (Brouwer 1907: 125–132, 159–160 [1975: 72–75, 88])[^brouwer-1907], but a more memorable passage is in the paper from 1908:

> Can one, in the case of purely mathematical constructions and transformations, temporarily neglect the presentation of the mathematical system that has been erected, and move in the accompanying linguistic building, guided by the principles of the syllogism, of contradiction, and of tertium exclusum, always confident that, by momentary evocation of the presentation of the mathematical constructions suggested by this reasoning, each part of the discourse could be justified? (Brouwer 1908C: 4 [van Atten & Sundholm 2017: 40])[^atten-2017]

(He then goes on to argue that the answer is “yes” for the principles of the syllogism and of contradiction, but, in general, “no” for the Principle of the Excluded Middle (PEM); more on this below, section 2.4.)

But if a certain mathematical construction can be constructed out of another one, this is a purely mathematical fact, and as such independent of logic. Logic therefore is descriptive but not creative: by the use of logic, one will never obtain mathematical truths that are not obtainable by a direct mathematical construction (Brouwer 1949C: 1243). Hence, in the development of intuitionistic mathematics, logic can never play an essential role. It follows from Brouwer’s view that logic is subordinate to mathematics. The classical view that mathematics is subordinate to logic is closely related to the view that pure logic has no particular subject matter or domain, and is prior to all. From that perspective, Brouwer’s conception of logic as dependent on mathematics will seem too restrictive. But for Brouwer logic always presupposes mathematics, because in his view it is, like any exact thought, an application of mathematics.

The resulting linguistic system of logic may in turn be studied mathematically, even independently of the mathematical activities and their recordings that it was originally abstracted from. Iterating the process, an infinite hierarchy arises of mathematical activities, their linguistic recordings, and the mathematical study of these recordings as linguistic objects independently of their original meaning. Brouwer describes this hierarchy (in more detail than we have done here) at the end of his dissertation (Brouwer 1907: 173ff)[^brouwer-1907], and criticizes Hilbert for not respecting it. Of particular interest is the distinction Brouwer makes between mathematics and “mathematics of the second order” (Brouwer 1907: 99n.1, 173 [1975: 61n.1, 94])[^brouwer-1907], where one instance of the latter is the mathematical study of the language of the former in abstraction from its original meaning; this way, Brouwer made fully explicit the distinction between mathematics and (what became known as) metamathematics (e.g., Hilbert 1923: 153)[^hilbert-1923]. Later, Brouwer claimed priority for this distinction, adding in a footnote that he had explained it to Hilbert in a series of conversations in 1909 (Brouwer 1928A2: 375 [Mancosu 1998: 44n.1])[^mancosu-1998].

### 2.2 The Hypothetical Judgement

Brouwer realized (1907: 125–128 [1975: 72–73]) that the hypothetical judgement seems to pose a problem for his view on logic as described above. For what is peculiar to the hypothetical judgement, Brouwer says, is that there the priority of mathematics over logic seems to be reversed. Among the examples he refers to are the proofs found in elementary geometry of the problems of Apollonius. Here is one of them: Given three circles, defined by their centers and their radii, construct a fourth circle that is tangent to each of the given three. The way this is usually solved is first to assume that such a fourth circle exists, then to set up equations that express how it is related to the three given circles, and then, via algebraic manipulations and logic, arrive at explicit definitions of the center and radius of the required circle, and, from there, at corresponding mathematical constructions. So it seems that here one first has to assume the existence of the required circle, then use logic to make various judgements about it, and only thereby arrives at a mathematical construction for it.

However, Brouwer argues, this is not what really happens. His general interpretation of such cases is as follows. Having first remarked that logical reasoning accompanies or mirrors mathematical activity which is at least conceptually prior to that reasoning, Brouwer then says:

> There is a special case […] which really seems to presuppose the hypothetical judgment from logic. This occurs where a structure in a structure is defined by some relation, without it being immediately clear how to effect its construction. Here one seems to *assume* to have effected the required construction, and to deduce from this hypothesis a chain of hypothetical judgments. But this is no more than apparent; what one is really doing in this case is the following: one starts by constructing a system that fulfills part of the required relations, and tries to deduce from these relations, by means of tautologies, other relations, in such a way that in the end the deduced relations, combined with those that have not yet been used, yield a system of conditions, suitable as a starting-point for the construction of the required system. Only by this construction will it then have been proved that the original conditions can indeed be satisfied. (Brouwer 1907: 126–127 [1975: 72; translation modified])[^brouwer-1907]

Different readings of this concise passage have been proposed. According to one, Brouwer’s passage bears on $A \rightarrow B$ in the following way:

- $(\alpha)$ Brouwer points out in the above lines that if the conditions and specifications for $A$ are given, then we try to add more information in such a way that, after a certain amount of constructional activity, we can really carry out a construction of $A$ which respects the specifications. Once this is accomplished, we can turn to the “implication” construction for $B$, which yields the construction for $B$ and to the required embedding of the structure for $A$ into the structure for $B$. (van Dalen 2004: 250–251)[^dalen-2004]

According to interpretation *α*, $A \rightarrow B$ just means $A \wedge B$ with the extra information that the construction for $B$ was obtained from that for $A$. On this reading $A \rightarrow B$ can be asserted only after a construction for $A$ has been found. The idea is clear: namely, to avoid hypothetical constructions, and the use of logic they require, by insisting that a construction be supplied that proves the antecedent. (As will be explained in Section 2.1 of the supplementary document Objections to the Proof Interpretation, Freudenthal (1937b)[^freudenthal-1937b] too has suggested this strategy, albeit with a different motivation than this passage in Brouwer’s dissertation.) But, as van Dalen also notices, it is also in effect a rejection of the hypothetical judgement in the general case where one does not know whether there is a construction for $A$.

An alternative reading is *β*:

- $(\beta)$ In order to establish $A \rightarrow B$, one has to conceive of $A$ and $B$ as conditions on constructions, and to show that from the conditions specified by $A$ one obtains the conditions specified by $B$, according to transformations whose composition preserves mathematical constructibility: if, by hypothesis, a construction for $A$ has been made, then we can make a construction for $B$ (van Atten 2009: 128)[^atten-2009].

On this reading, Brouwer’s explanation of the hypothetical judgement avoids hypothetical constructions and the concomitant use of logic by considering conditions on constructions instead of constructions themselves. Instead of a “chain of hypothetical judgements” that one seems to make, one is really making a chain of transformations in which from required relations (i.e., given conditions) further relations are derived. It is, of course, a requirement that these transformations preserve mathematical constructibility, and that this preservation is itself intuitively known. The role of conditions is explicit in a statement Brouwer made at the other end of his publishing career:

> [T]he wording of a mathematical theorem has no sense unless it indicates the construction either of an actual mathematical entity or of an incompatibility (e.g., the identity of the empty two-ity with an empty unity) out of some constructional condition imposed on a hypothetical mathematical system. (Brouwer 1954A: 3)

Brouwer speaks not of an incompatibility constructed out of a hypothetical mathematical system, but out of some condition on its construction.

Be that as it may, the preservation of constructibility from $A$ to $B$ is essential to both reading *α* and reading *β*, so on either it is clear that Brouwer had the Proof Interpretation of the implication in mind already in 1907. For further discussion of Brouwer’s passage on the hypothetical judgement and the two readings of it mentioned here, see Kuiper 2004, van Dalen 2004, van Dalen 2008, and van Atten 2009.

### 2.3 Negation

Intuitionistically, to say that a proposition $A$ is true is primarily to say that we have effected a construction that is correctly described by $A$; the proposition $A$ is made true by the construction. Idealizing to a certain extent, we say that $A$ is true if we possess a construction method that, when effected, will yield a construction that is correctly described by $A$. According to Brouwer, to say that a proposition $A$ is false then must mean that it is impossible to effect an appropriate construction; notation $\neg A$. Such an impossibility is recognized either immediately (e.g., the impossibility to identify 1 unit and 2 units) or mediately. In the former case, one observes directly that an intended construction is blocked; it “does not go through” (Brouwer 1907: 127 [1975: 73])[^brouwer-1907]. In the latter case, one shows that a proposition $A$ is contradictory by reducing $A$ to a known falsehood, e.g., one shows that $A \rightarrow 1=2$ (Brouwer 1954A: 3). In practice, one defines $\neg A := A \rightarrow 1=2$ (and hence $\neg 1=2$ is seen as a particular case of $A \rightarrow A)$.

The notion of “negation as impossibility” is known as “strong negation”. One speaks of the “weak negation” of $A$ to express that so far no proof of $A$ has been found. This excludes neither finding a proof of $A$ nor finding a proof of $\neg A$ later. Clearly, then, to assert the weak negation of $A$ is not to assign a truth value besides true and false to it; Barzin and Errera’s claim (see section 4.3 below) that its treatment of negation turns Brouwer’s logic into a three-valued one is groundless. The distinction between weak and strong negation is important for the so-called “weak counterexamples”.

### 2.4 Weak Counterexamples (“unreliability”) and Excluded Middle

As the rules of logic operate on linguistic objects, and these linguistic objects may be considered separately from the precise mathematical context in which they described a truth, it is possible to apply the rules of logic and obtain new linguistic objects without providing a precise mathematical context for the latter. In other words, the logical principles, which can be stated without specifying the context in which they are applied, and thereby suggest context-independence, are for their correctness sensitive to the context. There is no general guarantee that logical principles which are valid in one context, will be equally valid in a different one. This is what Brouwer means when he speaks of “the unreliability of the logical principles”, the title and theme of his seminal paper Brouwer 1908C; see also Brouwer 1949A: 1243.

In the 1908 paper, Brouwer draws a consequence of his general view on logic that he had overlooked in his dissertation: PEM, $A \vee \neg A$, is not valid. Its constructive validity would mean that we have a method that, for any $A$, either gives us a construction for $A$, or shows that such a construction is impossible. But we do not have such a general decision method, and there are many open problems in mathematics. Brouwer states “Every number is finite or infinite” as an example of a general proposition for which so far no constructive proof has been found. As a consequence, he says, it is at present uncertain whether problems such as the following are solvable:

> Is there in the decimal expansion of *π* a digit which occurs more often than any other one?
>
> Do there occur in the decimal expansion of *π* infinitely many pairs of equal consecutive digits? (Brouwer 1908C: 7 [van Atten & Sundholm 2017: 44])[^atten-2017]

In effect, Brouwer is saying that we can assert the weak negations of the propositions expressed in these questions; hence, these propositions are so-called “Brouwerian counterexamples” or “weak counterexamples” to PEM. On the constructive reading of PEM, of course any as yet unsolved problem is a weak counterexample to PEM. Brouwer began to publish weak counterexamples to PEM in international journals only much later (1921A, 1924N, 1925E).

Brouwer remarks in the 1908 paper that the fact that PEM is not valid does not mean that it is false: $\neg(A \vee \neg A)$ implies $\neg A \wedge \neg \neg A$, a contradiction. In other words, $\neg \neg(A \vee \neg A)$ is correct. Brouwer concludes that it is always consistent to use PEM but that it does not always lead to truths. In the latter case, the argument that appeals to PEM establishes not the truth, but the consistency of its conclusion. Brouwer proposes to divide the theorems that are usually considered as proved into the true and the non-contradictory ones (Brouwer 1908C: 7n.2 [van Atten & Sundholm 2017: 44n.14])[^atten-2017]. That is not a suggestion that there are three truth values, true, non-contradictory, false; for a non-contradictory proposition might be proved one day and thereby become true.

A mathematical context in which PEM is valid, Brouwer points out, is that of the question whether a given construction of finite character is possible in a given finite domain. In such a context there are only finitely many possible attempts at that construction, and each will succeed or fail in finitely many steps (for clarity, the phrasing here is not that of Brouwer 1908C but that of Brouwer 1955)[^brouwer-1955]. So on these grounds $A \vee \neg A$ holds, where $A$ is the proposition stating that the construction exists.

Brouwer ascribed the belief in the general validity of PEM to an unwarranted projection from such finite cases (in particular, those arising from the application of finite mathematics to everyday phenomena) to the infinite.[^note-6]

In his dissertation of 1907, Brouwer still accepted PEM as a tautology, (mis)understanding $A \vee \neg A$ as $\neg A \rightarrow \neg A$ (Brouwer 1907: 131, 160 [1975: 75, 88])[^brouwer-1907].[^note-7] Curiously, he did realize at the same time that there is no evidence for the principle that every mathematical proposition is either provable or refutable (Brouwer 1907: 142n.3 [1975: 101])[^brouwer-1907]; this principle is the constructively correct reading of PEM. In the paper from 1908, he corrected his earlier understanding of PEM:

> Now the principium tertii exclusi: this demands that every supposition is either correct or incorrect, mathematically: that of every supposed fitting in a certain way of systems in one another, either the termination or the blockage by impossibility, can be constructed. (Brouwer 1908C: 5 [van Atten & Sundholm 2017: 42])[^atten-2017]

### 2.5 There Are No Absolutely Undecidable Propositions

Brouwer continues this last quotation as follows:

> It follows that the question of the validity of the principium tertii exclusi is equivalent to the question whether unsolvable mathematical problems can exist. There is not a shred of proof for the conviction, which has sometimes been put forward [here Brouwer refers in a footnote to Hilbert 1900][^hilbert-1900] that there exist no unsolvable mathematical problems.

Here he seems to overlook that, constructively, there is a difference between the claim that every mathematical problem is solvable and the weaker claim that there are no absolutely unsolvable problems. The former is equivalent to $A \vee \neg A$, the latter to $\neg \neg(A \vee \neg A)$; and Brouwer had demonstrated the intuitionistic validity of the latter in the same paper. Indeed, in the Brouwer archive there is a note from about the same period 1907–1908 in which the point is made explicitly:

> Can one ever demonstrate of a proposition, that it can never be decided? No, because one would have to so by *reductio ad absurdum*. So one would have to say: assume that the proposition has been decided in sense $a$, and from that deduce a contradiction. But then it would have been proved that not-$a$ is true, and the proposition is decided after all. (van Dalen 2001b: 174n.a; translation mine)[^dalen-2001b]

Brouwer never published this note. Wavre in 1926 gave the argument for a particular case, clearly seeing the general point:

> It suffices to give an example of a number of which one does not know whether it is algebraic or transcendent in order to give at the same time an example of a number that, until further information comes in, could be neither the one nor the other. But, on the other hand, it would be in vain, it seems to me, to want to define a number that indeed is neither algebraic nor transcendent, as the only way to show that it is not algebraic consists in showing that it is absurd that it would be, and then the number would be transcendent. (Wavre 1926: 66; translation mine)[^wavre-1926]

The explicit observation that $\neg \neg(A \vee \neg A)$ means that no absolutely unsolvable problem can be indicated was made in Heyting 1934: 16.

## 3. Brouwer’s Later Refinements and Applications, 1921–1955

### 3.1 The Implicit Proof Interpretation

Three examples can be given that show that by the mid-1920s, Brouwer in practice worked with the hypothetical judgement and with the clause for implication in the Proof Interpretation (which was published later): an equivalence in propositional logic, the proof of the bar theorem, and his reading of ordering axioms.

#### 3.1.1 An equivalence in propositional logic

In a lecture in 1923, Brouwer presented a proof of $\neg \neg \neg A \leftrightarrow \neg A$ (Brouwer 1925E: 253 [Mancosu 1998: 291])[^mancosu-1998].[^note-8] This equivalence is the one theorem in propositional logic that Brouwer ever published. The argument begins by pointing out that $A \rightarrow B$ implies that $\neg B \rightarrow \neg A$ (because $\neg B$ is $B \rightarrow \bot$ and the two implications can be composed because the consequent of the one is the antecedent of the other). It would not have been possible for Brouwer to make this inference if at the time it would have been among his proof conditions of an implication to have a proof of the antecedent, as then a proof of $A \rightarrow B$ would lead to a proof of $B$ and thereby make it impossible to begin establishing the second implication by proving its antecedent $\neg B$.

Later, Brouwer pointed out the following consequence of the validity of $\neg \neg \neg A \leftrightarrow \neg A$: the proof method of *reductio ad absurdum* can be used to establish negative propositions $\neg A$ (Brouwer 1929A: 163 [Mancosu 1998: 52])[^mancosu-1998]. For if the assumption of $\neg \neg A$ leads to a contradiction, that is, to $\neg \neg \neg A$, the equivalence allows one to simplify that to $\neg A$. On the other hand, *reductio ad absurdum* in general cannot be used to establish positive propositions $A$; the derivation of a contradiction from the assumption $\neg A$ only leads to $\neg \neg A$, which intuitionistically is weaker than $A.$

#### 3.1.2 The proof of the bar theorem

Brouwer’s bar theorem is crucial to intuitionistic analysis; for a detailed explanation of the notions involved and of Brouwer’s proof, see Heyting 1956 (Ch. 3), Parsons 1967, and van Atten 2004b (Ch. 4). Here we will rather be concerned with the logical aspects.

Brouwer’s proof of the bar theorem from 1924 (later versions of the proof appeared in 1927 and in 1954) proves a statement of the form “If $A$ has been demonstrated, then $B$ is demonstrable” (Brouwer 1924D1, 1927B, 1954A). This would evidently not be an implication $A \rightarrow B$ if the latter were understood as a transformation of the *proof conditions* of $A$ into those of $B$, because in the former case there is the additional information that, by hypothesis, $A$ has been demonstrated. In other words, we have, by hypothesis, a concrete proof of $A$ at hand. (However, both are hypothetical judgements in the sense that neither requires that we actually have demonstrated $A$.) It may be possible to exploit this extra information, and below it will be indicated how Brouwer did this. (Heyting in 1956 also chose to understand implication in this stronger sense, that is, in terms of *assertion conditions*; see section 5.4 below.)[^heyting-1956]

A simple but relevant version of the bar theorem (for the universal tree over the natural numbers, *T*) would be:

> If it has been demonstrated that every path through $T$ intersects a given set of nodes $B$, then it can be demonstrated that every path through $T$ has a node in common with a set of nodes $B′$ that can be well-ordered.[^note-9]

Sets like $B$ and $B′$ are called bars. Brouwer first formulates a condition for any demonstration that may be found of the proposition “Tree $T$ contains a bar”. This condition is that any demonstration of that proposition must be analyzable into a certain canonical form. Brouwer then gives a method to transform any such demonstration, when analyzed into that canonical form, into a mathematical construction that makes the proposition “$T$ contains a well-ordered bar”, true, thereby establishing the consequent. This strategy clearly shows that Brouwer’s operative explanation of the meaning of $A \rightarrow B$ was a version of clause (H3) of the Proof Interpretation as formulated in the Introduction, if we understand “proof” in that clause as “demonstration”.

A demonstration or concrete proof of the antecedent, be it an actual or a hypothetical one, is required to obtain a canonical form. The reason is that the existence of a canonical proof of a proposition $A$ cannot be logically derived from the mere proof conditions of $A$, as the form such a canonical proof takes may well depend on specific non-logical details of mathematical constructions for $A$.

In Brouwer’s proof of the bar theorem, the applicability of the transformation method to any demonstration of the antecedent is guaranteed by the fact that the condition on such demonstrations that he formulates is a necessary condition. Brouwer obtained this necessary condition by exploiting the fact that on his conception, mathematical objects, so in particular trees and bars, are mental objects; this opens the possibility that reflection on the way these objects and their properties are constructed in mental acts provides information on them that can be put to mathematical use, in particular if this information consists in constraints on these acts of construction. This is how Brouwer arrived at his canonical form. In effect, Brouwer’s argument for the bar theorem is a transcendental argument. On other conceptions of mathematics such considerations need not be acceptable, and indeed no proofs of the (classically valid) bar theorem are known in other varieties of constructive mathematics (where bar induction is either accepted as an axiom, a possibility that Brouwer had also suggested (Brouwer 1927B: 63n.7 [van Heijenoort 1967: 460n.7])[^heijenoort-1967], or not accepted, as in the Markov School).

For a more detailed discussion of this matter, see Sundholm and van Atten 2008.

#### 3.1.3 Ordering axioms

Around 1925, Brouwer introduced the notion of “virtual ordering”. A (partial) ordering $\lt$ is virtual if it satisfies the following axioms (Brouwer 1926A: 453):

1. The relations $r = s, r \lt s$ and $r \gt s$ are mutually exclusive.
2. From $r = u, s = v$ and $r \lt s$ follows $u \lt v$.
3. From the simultaneous failure of the relations $r \gt s$ and $r = s$ follows $r \lt s$.
4. From the simultaneous failure of the relations $r \gt s$ and $r \lt s$ follows $r = s$.
5. From $r \lt s$ and $s \lt t$ follows $r \lt t$.

In a lecture course on Order Types in 1925, of which David van Dantzig’s notes are preserved in the Brouwer Archive, Brouwer commented:

> The axioms II through V are to be understood in the constructive sense: if the premisses of the axiom are satisfied, the virtually ordered set should provide a construction for the order condition in the conclusion. (van Dalen 2008: 19)[^dalen-2008]

This is a clear instance of the clause for implication in the Proof Interpretation. Note that Brouwer did not include this elucidation in the published paper (1926A), nor in later presentations.

### 3.2 Widening the Scope of the Weak Counterexamples

As we saw above, in the paper from 1908 Brouwer had given weak counterexamples to PEM. In the 1920s Brouwer developed a general technique for constructing weak counterexamples which also made it possible to widen their scope and include principles of analysis. The development began in 1921, when Brouwer gave a weak counterexample to the proposition that every real number has a decimal expansion (Brouwer 1921A). The argument proceeded by defining real numbers whose decimal developments are dependent on specific open problems concerning the decimal development of *π*. Brouwer closed by observing that, should these open problems be solved, then other real numbers without decimal expansion can be defined (Brouwer 1921A: 210 [Mancosu 1998: 34])[^mancosu-1998]. The general technique was made explicit in a lecture from 1923 (Brouwer 1924N: 3 and footnote 4 [van Heijenoort 1967: 337 and footnote 5])[^heijenoort-1967] and reached its perfection with the “oscillatory number” method in the first Vienna lecture in 1928 (Brouwer 1929A: 161 [Mancosu 1998: 51])[^mancosu-1998]. The method involves the reduction of the validity of a mathematical principle to the solvability of an open problem of the following type: we have a decidable property $P$ (defined on the natural numbers) for which we have as yet shown neither $\exists xP(x)$ nor $\forall x\neg P(x)$. This reduction is carried out in such a way that it only uses the fact that $P$ induces an open problem of this type, and does not depend on the exact definition of $P$; that is, if the open problem is solved, one can simply replace it by another one of the same type, and exactly the same reduction still works. This uniformity means that, as long as there are open problems of this type at all (and this is practically certain at any time), there is no intuitionistic proof of the general mathematical principle in question. In the 1920s, Brouwer constructed weak counterexamples to the following general mathematical propositions, among others (where $\mathbf{R}$ stands for the set of intuitionistic real numbers, and $\mathbf{Q}$ for the set of rationals):

1. The continuum is totally ordered (Brouwer 1924N)
2. Every set is either finite or infinite (Brouwer 1924N)
3. The Heine-Borel theorem (Brouwer 1924N)
4. $\forall x \in \mathbf{R}(x \in \mathbf{Q} \vee x \not\in \mathbf{Q})$ (Brouwer 1925E)
5. Any two straight lines in the Euclidean plane are either parallel, or coincide, or intersect (Brouwer 1929A)
6. Every infinite sequence of positive numbers either converges or diverges (Brouwer 1929A)

### 3.3 Strong Counterexamples and the Creating Subject

A weak counterexample shows that we cannot at present prove some proposition, but it does not actually refute it; in that sense, it is not a counterexample proper. From 1928 on, Brouwer devised a number of strong counterexamples to classically valid propositions, that is, he showed that these propositions were contradictory. This should be understood as follows: if one keeps to the letter of the classical principle but in its interpretation substitutes intuitionistic notions for their classical counterparts, one arrives intuitionistically at a contradiction. So Brouwer’s strong counterexamples are no more counterexamples in the strict sense of the word than his weak counterexamples are (but for a different reason). One way of looking at strong counterexamples is that they are non-interpretability results.

That strong counterexamples to classical principles are possible at all is explained as follows. As mentioned, on the intuitionistic understanding, logic is subordinate to mathematics, whereas classically it is the other way around. Hence, if intuitionistic mathematics contains objects and principles that do not figure in classical mathematics, it may come about that intuitionistic logic, which then depends also on these non-classical elements, is no proper part of classical logic.

Brouwer’s first strong counterexample was published in Brouwer 1928A2, where he showed:

$$ \neg \forall x\in \mathbf{R}(x \in \mathbf{Q} \vee x \not\in \mathbf{Q}) $$

This is a strengthening of the corresponding weak counterexample from 1923, but the argument is entirely different. The strong counterexample depends on the theorem in intuitionistic analysis, obtained in 1924 and improved in 1927, that all total functions $[0,1] \rightarrow \mathbf{R}$ are uniformly continuous. The non-classical elements in that theorem are the conception of the continuum as a spread of choice sequences, and the bar theorem based on it (for further explanations of this conception, see Heyting 1956 (Ch.3) and van Atten 2004b (Chs.3 and 4)).[^note-10]

From 1948 on, Brouwer also published counterexamples that are based on so-called “creating subject methods”. (He mentions in Brouwer 1948A that he has been using this method in lectures since 1927.) Their characteristic property is that they make explicit reference to the subject who carries out the mathematical constructions, to the temporal structure of its activities, and the relation of this structure to the intuitionistic notion of truth. These methods can be used to generate weak as well as strong counterexamples. (In the earlier “oscillatory number” method for generating weak counterexamples, the creating subject is not explicitly referred to.)

Using creating subject methods, Brouwer showed, for instance,

$$ \begin{align*} \neg \forall x & \in \mathbf{R}(\neg \neg x \gt 0 \rightarrow x \gt 0) & \textrm{(Brouwer 1949A)}\\ \neg \forall x & \in \mathbf{R}(x \ne 0 \rightarrow x \lt 0 \vee x \gt 0) & \textrm{(Brouwer 1949B)} \end{align*} $$

The actual arguments using these methods introduce no new logical phenomena as such—weak and strong counterexamples can also be given by other means. For the moment, we refer to the literature for further details: Brouwer 1949A, 1949B, 1954F; Heyting 1956: 117–120; Myhill 1966; Dummett 2000: 244–245; van Atten 2018. But we do note here one particular aspect of this method. It seems to introduce a further notion of negation, by accepting that, if it is known that the creating subject will never prove $A$, then $A$ is false. But this is actually no different from the notion of negation as impossibility. Heuristically, this can be seen as follows: given the freedom the creating subject has to construct whatever it can, the only way to show that there can be no moment at which the subject demonstrates $A$ is to show that a demonstration of $A$ itself is impossible. An actual justification of the principle is this: If the creating subject demonstrates a proposition $A$, it does so at a particular moment $n$; so, by contraposition, if it is contradictory that there exists a moment $n$ at which the subject demonstrates $A$, then $A$ is contradictory.[^note-11]

### 3.4 The Classification of Propositions

In Brouwer 1955, the four possible cases a proposition *α* may be in at any particular moment are made explicit:

1. *α* has been proved to be true;
2. *α* has been proved to be false, i.e., absurd;
3. *α* has neither been proved to be true nor to be absurd, but an algorithm is known leading to a decision either that *α* is true or that *α* is absurd;
4. *α* has neither been proved to be true nor to be absurd, nor do we know an algorithm leading to the statement either that *α* is true or that *α* is absurd.

In a lecture from 1951, Brouwer lists only cases 1, 2, and 4 from the above list, adding that case 3 “obviously is reducible to the first and second cases” (Brouwer 1981A: 92). That remark emphasizes an important idealization permitted in intuitionistic mathematics: we may make the idealization that, once we have obtained a decision method for a specific proposition, we also know its outcome.

Brouwer also adds that a proposition for which case 4 holds may at some point pass to another case, either because we have in the meantime found a decision method, or because the objects involved in proposition *α* in the meantime have acquired further properties that permit to make the decision (as may happen for propositions about choice sequences).

### 3.5 Brouwer’s View on the Formalist Program and Gödel’s Incompleteness Theorems

In 1908, Brouwer had shown that $\neg \neg(A \vee \neg A)$; in 1923, when Hilbert’s program was in full swing, this result inspired Brouwer to say that “We need by no means despair of reaching this goal [of a consistency proof for formalized mathematics]”; see section 2.1 above for the full quotation. (At the time, Brouwer suspected that $\neg \neg A \rightarrow A$ was weaker than PEM; Bernays quickly corrected this impression in a letter to Brouwer (Brouwer 1925E: 252n.4 [Mancosu 1998: 292n.4])[^mancosu-1998].)

In 1928, he added to this the consistency of finite conjunctions of instances of PEM, and considered these results to “offer some encouragement” for the formalist project of a consistency proof (Brouwer 1928A2: 377 [Mancosu 1998: 43])[^mancosu-1998].[^note-12] The strongest statement based on these results he made at the end of the first Vienna lecture from 1928:

> An appropriate mechanization of the language of this intuitionistically non-contradictory mathematics should therefore deliver precisely what the formalist school has set as its goal. (Brouwer 1929A: 164; translation mine)

But, for reasons explained above, such a consistency proof would have no mathematical value for Brouwer; and the best a classical mathematician can be said to be doing, according to the view Brouwer sketches, is to be giving relative consistency proofs.

Gödel’s incompleteness theorems showed that Hilbert’s Program, in its most ambitious form, cannot succeed. Brouwer’s assistant Hurewicz discussed the incompleteness theorem in a seminar (van Dalen 2005: 674n.7)[^dalen-2005]. There is no comment from Brouwer on Gödel’s first theorem in print; on the other hand, he clearly had the second theorem in mind when he wrote, in 1952, that

> The hope originally fostered by the Old Formalists that mathematical science erected according to their principles would be crowned one day with a proof of non-contradictority, was never fulfilled, and, nowadays, in view of the results of certain investigations of the last few decades, has, I think, been relinquished. (Brouwer 1952B: 508)

Hao Wang reports:

> In the spring of 1961 I visited Brouwer at his home. He discoursed widely on many subjects. Among other things he said that he did not think G’s incompleteness results are as important as Heyting’s formalization of intuitionistic reasoning, because to him G’s results are obvious (obviously true). (Wang 1987: 88)[^wang-1987][^note-13]

With respect to the first incompleteness theorem, Brouwer’s reaction is readily understandable. Already in his dissertation, he had noted that the totality of all possible mathematical constructions is “denumerably unfinished”; by this he meant that

> we can never construct in a well-defined way more than a denumerable subset of it, but when we have constructed such a subset, we can immediately deduce from it, following some previously defined mathematical process, new elements which are counted to the original set. (Brouwer 1907: 148 [1975: 82])[^brouwer-1907]

And in one of the notebooks leading up to his dissertation, he stated that “The totality of mathematical theorems is, among other things, also a set which is denumerable but never finished”.[^note-14]

Indeed, according to Carnap, it had been an argument of Brouwer’s that had stimulated Gödel in finding the first theorem. In a diary note for December 12, 1929, Carnap states that Gödel talked to him that day

> about the inexhaustibility of mathematics (see separate sheet). He was stimulated to this idea by Brouwer’s Vienna lecture. Mathematics is not completely formalizable. He appears to be right. (Wang 1987: 84)[^wang-1987]

On the “separate sheet”, Carnap wrote down what Gödel had told him:

> We admit as legitimate mathematics certain reflections on the grammar of a language that concerns the empirical. If one seeks to formalize such a mathematics, then with each formalization there are problems, which one can understand and express in ordinary language, but cannot express in the given formalized language. It follows (Brouwer) that mathematics is inexhaustible: one must always again draw afresh from the “fountain of intuition”. There is, therefore, no characteristica universalis for the *whole* mathematics, and no decision procedure for the whole mathematics. In each and every *closed language* there are only countably many expressions. The *continuum* appears only in “the whole of mathematics” … If we have *only one language*, and can only make “elucidations” about it, then these elucidations are inexhaustible, they always require some new intuition again. (As quoted, in translation, in Wang 1987: 50)[^wang-1987]

This record contains in particular elements from the second of Brouwer’s two lectures in Vienna, in which one finds the argument that Gödel refers to: on the one hand, the full continuum is given in a priori intuition, while on the other hand, it cannot be exhausted by a language with countably many expressions (Brouwer 1930A: 3, 6 [Mancosu 1998: 56, 58])[^mancosu-1998].

The second incompleteness theorem, on the other hand, must have surprised Brouwer, given his optimism in the 1920s about the formalist school achieving its aim of proving the consistency of formalized classical mathematics (see the quotation at the beginning of this subsection).

In his final original published paper (1955), Brouwer was, in his own way, quite positive about the study of classical logic. After showing that various principles from the algebraic tradition in logic (e.g., Boole, Schröder) are intuitionistically contradictory, he continues:

> Fortunately classical algebra of logic has its merits quite apart from the question of its applicability to mathematics. Not only as a formal image of the technique of common-sensical thinking has it reached a high degree of perfection, but also in itself, as an edifice of thought, it is a thing of exceptional harmony and beauty. Indeed, its successor, the sumptuous symbolic logic of the twentieth century which at present is continually raising the most captivating problems and making the most surprising and penetrating discoveries, likewise is for a great part cultivated for its own sake. (Brouwer 1955: 116)[^brouwer-1955]

### 3.6 Brouwer’s Logic and the Grundlagenstreit

Brouwer’s logic has played a role in the Grundlagenstreit (the Foundational Debate) only to the extent that this logic could be seen as a fragment of classical logic. Constructive logic in that sense was a success, and (with a different meaning) it became fundamental to Hilbert’s Program as well. On the other hand, phenomena specific to Brouwer’s full conception of logic, in particular the strong counterexamples, played no role in the Foundational Debate whatsoever. The main reason for this may be that, in their dependence on choice sequences, they use objects that are not acceptable in classical mathematics. (A more subtle matter is whether they are acceptable in Hilbert’s finitary mathematics. According to Bernays, Hilbert never took a position on choice sequences (Gödel 2003a: 279)[^gödel-2003a], and more generally never read Brouwer’s papers (van Dalen 2005: 637)[^dalen-2005].[^note-15]) In addition, Brouwer did not announce the existence of strong counterexamples in a loud or polemical way; and when in 1954 he finally did publish (in English) a paper with a polemical title—“An example of contradictority in classical theory of functions”—the Foundational Debate was, in the social sense, long over. Intuitionistic logic and mathematics had been widely accepted to the extent that they could be seen as the constructive part of classical mathematics, while the typically intuitionistic innovations were ignored. It is not surprising, then, that the presentation of the strong counterexamples in the 1950s did not at all lead to a reopening of the debate. For further discussion of this matter, see Hesseling 2003 and van Atten 2004a.

## 4. Early Partial Formalizations and Metamathematics

As Brouwer was more interested in developing pure mathematics than in developing logic, which for him was a form of applied mathematics, he never made an extensive study of the latter. In particular, he never made a systematic comparison of intuitionistic logic and classical logic as formalized, for example, in *Principia Mathematica* (Whitehead & Russell 1910)[^whitehead-1910] or by the Hilbert school (Hilbert 1923; Hilbert & Ackermann 1928)[^hilbert-1923][^hilbert-1928]. What motivated others to make such comparisons was the publication by Brouwer in international journals of weak counterexamples that showed how these also affected very general mathematical principles such as trichotomy for real numbers (see above, section 3.2).

Clearly, to make a systematic comparison possible, one needs a codification of intuitionistic logic in a formal system. On the intuitionistic view that cannot exist, as logic is as open-ended as the mathematics it depends on. But one may formalize fragments of intuitionistic logic. The relevant papers here are Kolmogorov 1925, Heyting 1928 (unpublished), Glivenko 1928, Glivenko 1929, and Heyting 1930.[^note-16] But perhaps the first to give systematic thought to the matter was Paul Bernays. In a letter to Heyting of November 5, 1930, he wrote:

> The lectures that Prof. Brouwer at the time held in Göttingen (for the first time) [1924 (van Dalen 2001: 305)], led me to the question how a Brouwerian propositional logic could be separated out, and I arrived at the result that this can be done by leaving out the single formula $\neg \neg a \supset a$ (in your symbolism). I then also wrote to Prof. Brouwer [correcting Brouwer’s impression at the time that this formula is weaker than PEM]. (Troelstra 1990: 8)[^troelstra-1990][^note-17]

(Bernays’ correction was included, at the proof stage, in Brouwer’s paper (1925E: 252n.4 [Mancosu 1998: 292n.4])[^mancosu-1998].) However, Bernays did not publish his idea for a Brouwerian logic. (Kolmogorov would publish the same idea in 1925; see below.)[^kolmogorov-1925]

In setting up a formal system to capture, albeit necessarily only in part, logic as it figures in Brouwer’s foundations, naturally some priorly obtained meaning explanation is needed to serve as the criterion for intuitionistic validity. Yet none of the papers by Kolmogorov, Heyting, and Glivenko just mentioned made an explicit contribution to the meaning explanation of intuitionistic logic. As we will see, the explanations as given in the papers (which is not necessarily all their respective authors had in mind) were too vague for that. It is perhaps not surprising, then, that the systems were not equivalent; notably, Kolmogorov rejected *Ex Falso*, while Heyting and Glivenko accepted it. We will now discuss these papers in turn.

### 4.1 Kolmogorov 1925

In 1925, Andrei Kolmogorov, at the age of 22, published the first (partial) formalization of intuitionistic logic, and also made an extensive comparison with formalized classical logic, in a paper called “On the principle of the excluded middle”. As van Dalen has suggested (Hesseling 2003: 237)[^hesseling-2003], Kolmogorov probably had come into contact with intuitionism through Alexandrov or Urysohn, who were close friends of Brouwer’s. Kolmogorov was in any case remarkably well-informed, citing even papers that had only appeared in the Dutch-language “Verhandelingen” of the Dutch Academy of Sciences (Brouwer 1918B, 1919A, 1921A).

The task Kolmogorov set himself in the paper is to explain why “the illegitimate use of the principle of the excluded middle” as revealed in Brouwer’s writings “has not yet led to contradictions and also why the very illegitimacy has often gone unnoticed” (van Heijenoort 1967: 416)[^heijenoort-1967]. In effect, as other passages make clear (van Heijenoort 1967: 429–430)[^heijenoort-1967], the (unachieved) aim is to show that classical mathematics is translatable into intuitionistic mathematics, and thereby give a consistency proof of classical mathematics relative to intuitionistic mathematics.

The technical result established in the paper is: Classical propositional logic is interpretable in an intuitionistically acceptable fragment of it. The intuitionistic fragment, called $\mathbf{B}$ (presumably for “Brouwer”) is:

$$ \begin{align} \tag{1} A & \rightarrow(B \rightarrow A)\\ \tag{2} (A \rightarrow(A \rightarrow B)) & \rightarrow (A \rightarrow B)\\ \tag{3} (A \rightarrow(B \rightarrow C)) & \rightarrow (B \rightarrow(A \rightarrow C))\\ \tag{4} (B \rightarrow C) & \rightarrow((A \rightarrow B) \rightarrow(A \rightarrow C))\\ \tag{5} (A \rightarrow B) & \rightarrow((A \rightarrow \neg B) \rightarrow \neg A)\\ \end{align} $$

The system $\mathbf{H}$ (presumably for “Hilbert”) consists of $\mathbf{B}$ and the additional axiom

$$\tag{6} \neg \neg A \rightarrow A $$

In both systems, the rules are modus ponens and substitution.

Kolmogorov then indicates and partially carries out a proof that $\mathbf{H}$ is equivalent to the system for classical propositional logic presented by Hilbert in Hilbert 1923. Then Kolmogorov devises the following translation $^*$:

$$ \begin{align*} A^* & = \neg \neg A & \textrm{for atomic } A\\ F(\phi_1, \phi_2 ,\ldots ,\phi_k)^* & = \neg \neg F(\phi_{1}^*, \phi_{2}^*,\ldots ,\phi_{k}^*) & \textrm{ for composed formulas} \end{align*} $$

and proves this interpretability result:

$$ \textrm{If } U \vdash_{\mathbf{H}} \phi \textrm{ then } U^* \vdash_{\mathbf{B}} \phi^* $$

where $U$ is a set of axioms of $\mathbf{H}$, and $U^*$ the set of its translations (which Kolmogorov shows to be derivable in $\mathbf{B})$.

Kolmogorov’s technical result anticipated Gödel’s and Gentzen’s “double negation translations” for arithmetic (see below), all the more so since he also made quite concrete suggestions how to treat predicate logic. As Hesseling (2003: 239)[^hesseling-2003] points out, however, to see Kolmogorov’s result as a translation into intuitionistic mathematics is slightly different from his own way of seeing it. Kolmogorov saw it as a translation into a domain of “pseudomathematics”; but although he did not explicitly identify that as part of intuitionistic mathematics, he could have done so.

Kolmogorov’s strategy to obtain a (fragment) of formalized intuitionistic logic was to start with a classical system and isolate an intuitionistically acceptable system from it. (Note that, although Kolmogorov refers to *Principia Mathematica*, he did not take it as his point of departure.) This might (roughly) be described as the method of crossing out, which is also what Heyting would do in 1928 (see below). Given the task Kolmogorov set himself, it is a natural approach. Kolmogorov’s criterion whether to keep an axiom was whether a proposition has an “intuitive foundation” or “possesses intuitive obviousness” (van Heijenoort 1967: 421, 422)[^heijenoort-1967]; on implication he said,

> The meaning of the symbol $A \rightarrow B$ is exhausted by the fact that, once convinced of the truth of $A$, we have to accept the truth of $B$ too. (van Heijenoort 1967: 420)[^heijenoort-1967]

No more precise indications are given, so in that sense the paper did little to explain the meaning of intuitionistic logic.

*Ex Falso* was excluded from this fragment: Kolmogorov said that, just like PEM, *Ex Falso* “has no intuitive foundation” (van Heijenoort 1967: 419)[^heijenoort-1967]. In particular, he says that *Ex Falso* is unacceptable for the reason that it asserts something about the consequences of something impossible (van Heijenoort 1967: 421)[^heijenoort-1967]. Note that that is a very strong rejection: it not only rules out *Ex Falso* in its full generality, but also specific instances such as “If 3.15 is an initial segment of *π*, then 3.1 is an initial segment of *π*”. It also indicates an incoherence in Kolmogorov’s position: one cannot at the same time accept $A \rightarrow (B \rightarrow A)$ as an axiom and deny that anything can be asserted about the consequences of an impossible $B$.

As van Dalen notes, it is not known whether Kolmogorov sent his paper to Brouwer (van Dalen 2005: 555)[^dalen-2005]. The contents of the paper seem to have remained largely unknown outside the Soviet Union for years. Glivenko mentioned the paper in a letter to Heyting of October 13, 1928, as did Kolmogorov in an undated letter to Heyting of 1933 or later (Troelstra 1990: 16)[^troelstra-1990]; but in Heyting 1934 it is, unlike Kolmogorov’s later paper from 1932, neither discussed nor included in the bibliography. The volume of the *Jahrbuch über die Fortschritte der Mathematik* covering 1925, which included a very short notice on Kolmogorov 1925 by V. Smirnov (Leningrad), wasn’t actually published until 1932 (Smirnov 1925)[^smirnov-1925].

### 4.2 Heyting 1928

While Kolmogorov’s work remained unknown in the West, an independent initiative towards the formalization of intuitionistic logic and mathematics was taken in 1927, when the Dutch Mathematical Society chose to pose the following problem for its annual contest:

> By its very nature, Brouwer’s set theory cannot be identified with the conclusions formally derivable in a certain pasigraphic system [i.e., universal notation system]. Nevertheless certain regularities may be observed in the language which Brouwer uses to give expression to his mathematical intuition; these regularities may be codified in a formal mathematical system. It is asked to
>
> 1. construct such a system and to indicate its deviations from Brouwer’s theories;
> 2. to investigate whether from the system to be constructed a dual system may be obtained by (formally) interchanging the *principium tertii exclusi* and the *principium contradictionis*. (Troelstra 1990: 4)[^troelstra-1990]

The question had been formulated by Brouwer’s friend, colleague, and former teacher Gerrit Mannoury, who asked Brouwer’s opinion on it beforehand in a letter (Brouwer was in Berlin);[^note-18] unfortunately, no reply from Brouwer has been found, but the final formulation was the same as in Mannoury’s letter.

Brouwer’s former student Arend Heyting, who had graduated (cum laude) in 1925 with a dissertation on intuitionistic projective geometry, wrote what turned out to be the one submission (Hesseling 2003: 274)[^hesseling-2003]. The original manuscript seems no longer to exist, but it is known that its telling motto was “Stones for bread”.[^note-19] In 1928, the jury crowned Heyting’s work,[^note-20] stating that it was “a formalization carried out in a most knowledgeable way and with admirable perseverance” (Hesseling 2003: 274; translation modified)[^hesseling-2003].

Heyting’s essay covered propositional logic, predicate logic, arithmetic, and Brouwerian set theory or analysis. One would think that, to be able to achieve this, Heyting must have had quite precise ideas on how to explain the logical connectives intuitionistically. However, Heyting’s correspondence with Freudenthal in 1930 shows that before 1930, Heyting had not yet arrived at the explicit requirement of a transformation procedure in the explanation of implication (see the quotation in section 5.1 below).

Since the original manuscript seems not to have survived, a discussion of Heyting’s work must take the revised and published version from 1930 as its point of departure; see below.

Heyting sent his manuscript to Brouwer, who replied in a letter of July 17, 1928, that he had found it “extraordinarily interesting”, and continued:

> By now I have already begun to appreciate your work so much, that I should like to request that you revise it in German for the Mathematische Annalen (preferably somewhat extended rather than shortened).[^note-21]

Interestingly, Brouwer also suggested (with an eye on the formalization of the theory of choice sequences)

> And, with an eye on §13, perhaps also the notion of “law” can be formalized.

It seems, however, that Heyting made no effort in that direction.

Heyting’s paper would indeed be published soon after, in 1930; not in the *Mathematische Annalen*, as Brouwer by then was no longer on its editorial board, but in the proceedings of the Prussian Academy of Sciences. However, Heyting’s work became known already before its publication. Heyting mentioned it in correspondence with Glivenko in 1928 (see below), Tarski and Łukasiewicz talked about it to Bernays at the Bologna conference in 1928, and Church mentioned it in a letter to Errera in 1929 (Hesseling 2003: 274)[^hesseling-2003].

### 4.3 Glivenko 1928 and 1929

In reaction to Barzin and Errera, who had argued that Brouwer’s logic was three-valued and moreover that this led to it being inconsistent, Valerii Glivenko[^note-22] in 1928 set out to prove them wrong by formal means. He gave the following list of axioms for intuitionistic propositional logic:

$$ \begin{align} \tag{1} p &\rightarrow p\\ \tag{2} (p \rightarrow q) &\rightarrow((q \rightarrow r) \rightarrow(p \rightarrow r))\\ \tag{3} (p \wedge q) &\rightarrow p\\ \tag{4} (p \wedge q) &\rightarrow q\\ \tag{5} (r \rightarrow p) &\rightarrow((r \rightarrow q) \rightarrow(r \rightarrow(p \wedge q)))\\ \tag{6} p &\rightarrow(p \vee q)\\ \tag{7} q &\rightarrow(p \vee q)\\ \tag{8} \label{GlivAxiom8} (p \rightarrow r) &\rightarrow ((q \rightarrow r) \rightarrow((p \vee q) \rightarrow r))\\ \tag{9} (p \rightarrow q) &\rightarrow((p \rightarrow \neg q) \rightarrow \neg p)\\ \end{align} $$

From these axioms, he then proved

$$ \begin{align} \tag{1} \neg \neg(p \vee \neg p)\\ \tag{2} \neg \neg \neg p & \rightarrow \neg p\\ \tag{3} ((\neg p \vee p) \rightarrow \neg q) & \rightarrow \neg q\\ \end{align} $$

The first two had already informally been argued for by Brouwer (1908C, 1925E); the third was new. Now suppose that in intuitionistic logic, a proposition may be true $(p$ holds), false $(\neg p$ holds), or have a third truth value $(p'$ holds). Clearly, $p \rightarrow \neg p'$ and $\neg p \rightarrow \neg p'$, and therefore $(\neg p \vee p) \rightarrow \neg p'$; but then, by the third of the lemmata above and axiom \\ref{GlivAxiom8} in the list, $\neg p'$. As $p$ is arbitrary, this means no proposition has the third truth value. (In 1932, Gödel would show that, more generally, intuitionistic propositional logic is no $n$-valued logic for any natural number $n$; see Section 1 of the supplementary document The Turn to Heyting’s Formalized Logic and Arithmetic.)

Like Kolmogorov in 1925 and, as we will see, Heyting in 1930, Glivenko provided no detailed explanation of the intuitionistic validity of these axioms.

Glivenko immediately continued this line of work with a second short paper, Glivenko 1929, in which he showed, for a richer system of intuitionistic propositional logic:

1. If $p$ is provable in classical propositional logic, then $\neg \neg p$ is provable in intuitionistic propositional logic;
2. If $\neg p$ is provable in classical propositional logic, then it is also provable in intuitionistic propositional logic.

The first theorem is not a translation in the usual sense (as Kolmogorov’s is), as it does not translate subformulas of $p$; but it is strong enough to show that the classical and intuitionistic systems in question are equiconsistent.

The system of intuitionistic propositional logic is richer than in Glivenko’s previous paper, because to its axioms have now been added the following four:

$$ \begin{align} \tag{A} (p \rightarrow(q \rightarrow r)) & \rightarrow (q \rightarrow(p \rightarrow r))\\ \tag{B} (p \rightarrow(p \rightarrow r)) & \rightarrow (p \rightarrow r)\\ \tag{C} p & \rightarrow(q \rightarrow p)\\ \tag{D} \neg q & \rightarrow(q \rightarrow p)\\ \end{align} $$

Interestingly, Glivenko mentions in his paper that “It is Mr. A. Heyting who first made me see the appropriateness of the two axioms C and D in the Brouwerian logic” (Mancosu 1998: 304–305n.3)[^mancosu-1998]. The two had come into correspondence when, upon the publication of Glivenko 1928, Heyting sent Glivenko a letter (Troelstra 1990: 11)[^troelstra-1990]. Kolmogorov in 1925 had explicitly rejected *Ex Falso* for having no “intuitive foundation”. From Glivenko’s letter to Heyting of October 13, 1928, we know that Glivenko was aware of this (Troelstra 1990: 12)[^troelstra-1990]. In his paper, however, which he finished later, he does not mention Kolmogorov at all. Instead, he makes the remark on Heyting just quoted and then justifies D by saying that it is a consequence of the principle $(p \vee \neg q) \rightarrow (q \rightarrow p)$, the admissibility of which he considers “quite evident”.[^note-23] From a Brouwerian point of view, however, the principle is as objectionable as *Ex Falso*.[^note-24] It is worth noting that, when Heyting gave his justification for *Ex Falso* in Heyting 1956: 102, he did not appeal to the principle Glivenko had used (nor did Kolmogorov in 1932)[^kolmogorov-1932]. From Glivenko’s letter of October 18, 1928, one gets the impression that this principle had not been the argument Heyting had actually given to convince him:

> I am now convinced by your reasons that intuitionistic mathematics need not reject that axiom, so that all considerations against that axiom might lead beyond the limits of our present subject matter. (Troelstra 1990: 12; translation mine)[^troelstra-1990]

Heyting had informed Glivenko of the planned publication of his (revised and translated) prize essay from 1928 in the *Mathematische Annalen*. On October 30, 1928, Glivenko asked Heyting if he also was going to include the result that if $p$ is provable in classical propositional logic, then $\neg\neg p$ is provable in intuitionistic propositional logic; for if he would, then there would be no point for Glivenko in publishing his own manuscript. Two weeks later, Glivenko had changed his mind, writing to Heyting on November 13 that, even though this result “is but an almost trivial remark”, “its rigorous demonstration is a bit long” and he wants to publish it independently of Heyting’s paper. Indeed, Glivenko’s paper was published first, and in it the publication of Heyting’s formalization was announced; and when Heyting published his paper in 1930, he included a reference to Glivenko 1929, stating its two theorems, and he also acknowledged the use of results from Glivenko 1928. Heyting’s note “On intuitionistic logic”, also from 1930, begins with a reference to Glivenko’s “two excellent articles” from 1928 and 1929.

### 4.4 Heyting 1930

Heyting’s (partial) formalization of intuitionistic logic and mathematics in Heyting 1930, Heyting 1930A, and Heyting 1930B, is perhaps, as far as the parts on logic are concerned, the most influential intuitionistic publication ever, together with his book *Intuitionism: An Introduction* from 1956.

Heyting’s formalization comprised intuitionistic propositional and predicate logic, arithmetic, and analysis, all together in one big system (with only variables for arbitrary objects). The part concerned with analysis was, not only in its intended interpretation (involving choice sequences) but also formally, no subsystem of its classical counterpart; this explains why it sparked no general interest at the time. (A consequence we noted above is that Brouwer’s strong counterexamples never affected the debate.) Therefore this part of Heyting’s formalization was left out of consideration by the other participants in the Foundational Debate.[^note-25] This was different for the parts concerned with logic and arithmetic. Formally speaking and disregarding their intended interpretations, from these one could distill subsystems of their classical counterparts, from which only PEM (or double negation elimination) is missing. No doubt this encouraged many to accord to these systems a definitive character, which, as Heyting had remarked at the beginning of his paper, on the intuitionistic conception of logic they cannot have:

> Intuitionistic mathematics is a mental activity [“*Denktätigkeit*”], and for it every language, including the formalistic one, is only a tool for communication. It is in principle impossible to set up a system of formulas that would be equivalent to intuitionistic mathematics, for the possibilities of thought cannot be reduced to a finite number of rules set up in advance. Because of this, the attempt to reproduce the most important parts of formal language is justified exclusively by the greater conciseness and determinateness of the latter vis-à-vis ordinary language; and these are properties that facilitate the penetration into the intuitionistic concepts and the use of these concepts in research. (Heyting 1930: 42 [Mancosu 1998: 311])[^heyting-1930][^mancosu-1998]

However, Heyting himself, however, wrote some five decades later,

> I regret that my name is known to-day mainly in connection with these papers [Heyting 1930, 1930A, 1930B][^heyting-1930], which were very imperfect and contained many mistakes. They were of little help in the struggle to which I devoted my life, namely a better understanding and appreciation of Brouwer’s ideas. They diverted the attention from the underlying ideas to the formal system itself. (Heyting 1978: 15)[^heyting-1978]

The fear that the attention might be thus diverted had indeed been expressed in the first of the three papers themselves:

> Section 4 [on negation] departs substantially from classical logic. Here I could not avoid giving the impression that the differences that come to the fore in this section constitute the most important point of conflict between intuitionists and formalists (a claim that is already refuted by the remark made at the beginning [quoted above]); this impression arises because the formalism is unfit to express the more fundamental points of conflict. (Heyting 1930: 44 [Mancosu 1998: 313])[^heyting-1930][^mancosu-1998]

For the full system, including predicate logic and analysis, the reader is referred to Heyting’s original papers. Heyting’s axioms for intuitionistic propositional logic were:

$$\begin{align} \tag{1} a &\rightarrow(a \wedge a)\\ \tag{2} (a \wedge b) &\rightarrow(b \wedge a)\\ \tag{3} (a \rightarrow b) &\rightarrow((a \wedge c)\rightarrow(b \wedge c))\\ \tag{4} ((a \rightarrow b) \wedge(b \rightarrow c)) &\rightarrow(a \rightarrow c)\\ \tag{5} \label{HeytingAxiom5} b &\rightarrow(a \rightarrow b)\\ \tag{6} (a \wedge(a \rightarrow b)) &\rightarrow b\\ \tag{7} a &\rightarrow(a \vee b)\\ \tag{8} (a \vee b) &\rightarrow(b \vee a)\\ \tag{9} ((a \rightarrow c) \wedge(b \rightarrow c)) &\rightarrow((a \vee b) \rightarrow c)\\ \tag{10} \label{HeytingAxiom10} \neg a &\rightarrow(a \rightarrow b)\\ \tag{11} ((a \rightarrow b) \wedge(a \rightarrow \neg b)) &\rightarrow \neg a\\ \end{align} $$

In a letter to Oskar Becker, Heyting described the approach used to obtain these axioms, as well as those for predicate logic, as follows:

> I sifted the axioms *and theorems* of Principia Mathematica and, on the basis of those that were found to be admissible, looked for a system of independent axioms. Given the relative completeness of Principia, this to my mind ensures the completeness of my system in the best possible way. Indeed, as a matter of principle, it is impossible to be certain that one has captured *all* admissible modes of inference in one formal system. (Heyting to Becker, September 23, 1933 (draft) [van Atten 2005: 129][^atten-2005], original italics, translation mine)

As Heyting emphasizes here, the theorems of *Principia Mathematica* also had to be looked at, for a theorem might be intuitionistically acceptable even when a classical proof given for it is not.[^note-26] It is worth noting that Heyting used this method of crossing out, as also Kolmogorov had, instead of determining the logic directly from general considerations on mathematical constructions in Brouwer’s sense. (To some extent, Kreisel tried to do that systematically in the 1960s.) In his dissertation on intuitionistic axiomatization of projective geometry, Heyting had already gained experience with developing an intuitionistic system by taking a classical axiomatic system as guideline and then adjusting it.[^note-27]

In Mints 2006 (section 2) it has been observed that Russell 1903 (section 18) anticipated intuitionistic propositional logic by identifying Peirce’s law and using it to separate out the principles that imply PEM. It seems that Heyting did not realize this at the time; among the references given in Heyting 1930, Russell’s book does not appear.

Heyting shows the independence of his axioms using a method given by Bernays (1926)[^bernays-1926]; this use of a non-intended interpretation for metamathematical purposes Heyting accepted without hesitation, but he remarked that such metamathematics is “less important for us [intuitionists]” than the approach where all formulas are considered to be meaningful propositions (Heyting 1930: 43 [Mancosu 1998: 312])[^heyting-1930][^mancosu-1998].

Heyting states Glivenko’s two theorems from 1929, without giving proofs.

Unlike Kolmogorov, but like Glivenko (who had been convinced by Heyting), Heyting accepted *Ex Falso* (axiom \\ref{HeytingAxiom10} above). He was somewhat more elaborate on this point than they had been:

> The formula $a \rightarrow b$ generally means: “If $a$ is correct, then $b$ is correct too”. This proposition is meaningful if $a$ and $b$ are constant propositions about whose correctness nothing need be known … The case if conceivable that after the statement $a \rightarrow b$ has been proved in the sense specified, it turns out that $b$ is always correct. Once accepted, the formula $a \rightarrow b$ then has to remain correct; that is, we must attribute a meaning to the sign $\rightarrow$ such that $a \rightarrow b$ still holds. The same can be remarked in the case where it later turns out that $a$ is always false. For these reasons, the formulas [\\ref{HeytingAxiom5}] and [\\ref{HeytingAxiom10}] are accepted. (Heyting 1930: 44 [Mancosu 1998: 313])[^heyting-1930][^mancosu-1998]

The argument is, however, incomplete. It is uncontroversial that, once $a \rightarrow b$ has been proved, it should remain so when afterward $\neg a$ is proved. But why should $a \rightarrow b$, if it has not yet been proved, become provable just by establishing $\neg a$? (Johansson asked this in a letter to Heyting in 1935;[^note-28] see Section 1 of the supplementary document Objections to the Proof Interpretation). Clearly, then, further work needed to be done on the explanation of intuitionistic logic.

After the publication of Heyting’s series of papers, three roads could be taken, and indeed were (cf. Posy 1992)[^posy-1992]:

1. to explicate and develop the meaning explanation that had given rise to Heyting’s system;
2. to engage in metamathematical study of the formal systems distilled from Heyting’s system;
3. to find alternative motivations for (parts of) Heyting’s system that are independent from the intuitionists’, yet also in some sense constructive (e.g., Lorenzen’s dialogue semantics)

By and large, these three roads lead to very different areas, with correspondingly divergent histories, of which no unified account can be expected. (However, in the Dialectica Interpretation, as proposed and understood by Gödel [1958, 1970, 1972], they came close to one another.) Following the main theme of the present account, our topic will remain the intuitionistic meaning explanation of logic. But a number of early highlights of the formal turn are presented in this supplementary document:

> [The Turn to Heyting’s Formalized Logic and Arithmetic](intuitionistic-logic-development.heyting-logic.md)

## 5. The Proof Interpretation Made Explicit

### 5.1 Heyting 1930, 1931

Heyting told van Dalen that he had the notion of (intuitionistic) construction in mind to guide him in devising his formalization of intuitionistic logic and mathematics in 1927. In the published version of his formalization, he did not elaborate much on the meaning of the connectives; all he explained there about the general meaning of $a \rightarrow b$ was that “If $a$ is correct, then $b$ is correct too” (Heyting 1930: 44 [Mancosu 1998: 313])[^heyting-1930][^mancosu-1998]. Correspondence between Heyting and Freudenthal in 1930 shows that Heyting up till then did not have a more refined explanation at hand; we will come back to this later in this section.

Heyting began to expound on the meaning of the connectives in print in two papers written in 1930. The first, Heyting 1930C, was published that same year, the second, the text of his lecture at Königsberg in September 1930, was published the next year (Heyting 1931)[^heyting-1931].

The first paper was a reaction to Barzin and Errera’s claim that Brouwer’s logic is three-valued (Barzin & Errera 1927)[^barzin-1927]. The relevant points for the explanation of the meaning of the connectives in Heyting’s paper are the following. First, an explanation is given of assertion:

> Here, then, is the *Brouwerian assertion* of $p$: *It is known how to prove p*. We will denote this by $\vdash p$. The words “to prove” must be taken in the sense of “to prove by construction”. [original italics] (Heyting 1930C: 959 [Mancosu 1998: 307])[^mancosu-1998]

And then of intuitionistic negation:

> $\vdash \neg p$ will mean: “It is known how to reduce $p$ to a contradiction”. (Heyting 1930C: 960 [Mancosu 1998: 307])[^mancosu-1998]

Heyting goes on to explain that, although on these explanations there is a third case beside $\vdash p$ and $\vdash \neg p$, namely the case where one knows neither how to prove $p$ nor how to refute it, this does not mean there is a third truth value:

> This case could be denoted by $p'$, but it must be realized that $p'$ will hardly ever be a definitive statement, since it is necessary to take into account the possibility that the proof of either $p$ or $\neg p$ might one day succeed. If one does not wish to risk having to retract what one has said, in the case $p'$ one should not state anything at all. (Heyting 1930C: 960 [Mancosu 1998: 307])[^mancosu-1998]

This refutes the contention of Barzin and Errera. Note that these points are all in Brouwer’s writings, too. Indeed, Heyting (1932: 121)[^heyting-1932] objects to Barzin and Errera’s term “Heyting’s logic”, saying that “all the fundamental ideas of that logic come from Brouwer” (translation mine). But Heyting’s papers will have found a wider audience than Brouwer’s. Brouwer, in turn, was very positive about the paper Heyting 1930C, and wrote to the editor of the journal in which it appeared (Brouwer to de Donder, October 9, 1930):

> While preparing a note on intuitionism for the Bulletin de l’Académie Royale de Belgique,[^note-29] I was pleasantly surprised to see the publication of a note by my student Mr. Heyting, which elucidates in a magisterial manner the points that I wanted to shed light upon myself. I believe that after Heyting’s note little remains to be said. (van Dalen 2005: 676)[^dalen-2005]

Heyting also proposes a provability operator +, where $+p$ means “$p$ is provable”. The distinction between $p$ and $+p$ is relevant if one believes that (at least some) propositions are true or false independently of our mathematical activity. In that case one can go on and develop a provability logic, as for example Gödel did (see Section 1 of the supplementary document The Turn to Heyting’s Formalized Logic and Arithmetic.) That is not the intuitionistic conception, and Heyting remarks that, if the fulfillment of $p$ requires a construction, then there is no difference between $p$ and $+p$. He adds that, on the intuitionistic explanation of negation, there is indeed no difference between $\neg p$ and $+\neg p$, as a proof of $\neg p$ is defined as a construction that reduces $p$ to a contradiction. But Heyting does not generalize this remark to all of intuitionistic logic. The final section of the paper is a further discussion of the logic of the provability operator, in particular its interaction with negation (e.g., $\vdash \neg +p$ is the assertion that $p$ is unprovable). But Heyting ends by saying that, as the intuitionists’ task is the reconstruction of all mathematics, while at the same time no examples of propositions have been found so far for which this provability operator would be necessary to express their status (e.g., to express absolute undecidability), it cannot be asked of intuitionists that they develop this logic (Heyting 1930C: 963 [Mancosu 1998: 309–310])[^mancosu-1998]

The Königsberg lecture, given in 1930 and published in 1931, specifies the meanings of $p, \neg p$, and $p \vee q$. This time Heyting makes an explicit connection to phenomenology:

> We here distinguish between propositions [*Aussagen*] and assertions [*Sätze*]. An assertion is the affirmation of a proposition. A mathematical proposition expresses a certain expectation. For example, the proposition, “Euler’s constant $C$ is rational”, expresses the expectation that we could find two integers $a$ and $b$ such that $C = a / b$. Perhaps the word “intention”, coined by the phenomenologists, expresses even better what is meant here … The affirmation of a proposition means the fulfillment of an intention. (Heyting 1931: 113 [Benacerraf & Putnam 1983: 58–59])[^benacerraf-1983][^heyting-1931]

Compared to the earlier paper written in 1930, the point about the provability operator is amplified:

> The distinction between $p$ and $+p$ vanishes as soon a construction is intended in $p$ itself, for the possibility of a construction can be proved only by its actual execution. If we limit ourselves to those propositions which require a construction, the logical function of provability does not arise at all. We can impose this restriction by treating only propositions of the form “$p$ is provable”, or, to put it another way, by regarding every intention as having the intention of a construction for its fulfillment added to it. It is in this sense that intuitionistic logic, insofar as it has been developed up to now without using the function +, must be understood. (Heyting 1931: 115 [Benacerraf & Putnam 1983: 60; translation modified])[^benacerraf-1983][^heyting-1931]

The explanation of disjunction in the Königsberg lecture is:

> “$p \vee q$” signifies that intention which is fulfilled if and only if at least one of the intentions $p$ and $q$ is fulfilled. (Heyting 1931: 114 [Benacerraf & Putnam 1983: 59])[^benacerraf-1983][^heyting-1931]

And of negation:

> Becker, following Husserl, has described its meaning very clearly. For him negation is something thoroughly positive, viz., the intention of a contradiction contained in the original intention. The proposition “$C$ is not rational”, therefore, signifies the expectation that one can derive a contradiction from the assumption [*Annahme*] that $C$ is rational. It is important to note that the negation of a proposition always refers to a proof procedure which leads to the contradiction, even if the original proposition mentions no proof procedure. (Heyting 1931: 113 [Benacerraf & Putnam 1983: 59])[^benacerraf-1983][^heyting-1931]

Heyting pointed out that these explanations for disjunction and negation, taken together, are an immediate argument against the acceptability of PEM, for which a general method would be needed that, applied to any given proposition $p$, produces either a proof of $p$ or a proof of $\neg p$. What Heyting did not do here was to generalize this explanation of negation to one for implication. Also, note that the procedure does not operate on proofs of $p$, but starts from merely the assumption that $p$, which in general gives less information. Both points were taken care of shortly afterward. In a letter to Freudenthal dated October 25, 1930, shortly after the Königsberg lecture, Heyting wrote:

> From your remarks it has become clear to me that the simple explanation of $a \rightarrow b$ by “When I think $a$, I must think $b$” is untenable; this idea is in any case too indeterminate to be able to serve as the foundation for a logic. But also your formulation: “When $a$ has been proved, so has $b$”, is not wholly satisfactory to me; when I ask myself what you may mean by that, I believe that also $a \rightarrow b$, like the negation, should refer to a proof procedure: “I possess a construction that derives from every proof of $a$ a proof of $b$”. In the following, I will keep to this interpretation. There is therefore no difference between $a \rightarrow b$ and $+a \rightarrow +b$. (Troelstra 1983: 206–207; translation mine)[^troelstra-1983]

This explanation of implication, which is the one that became standard, would be introduced in print only in Heyting 1934: 14; in his paper 1932C, Heyting used the explanation given in Kolmogorov 1932 instead (see below).

Neither of these two papers by Heyting contained an argument for the validity of *Ex Falso*.

### 5.2 Influences on Heyting

A number of influences (or possible influences) on Heyting’s arriving at the Proof Interpretation can be suggested. The following are publications Heyting had all seen by 1927, for he refers to them in his dissertation (1925: 93–94):

- Brouwer 1907 (Ch. 3) and Brouwer 1908C, which forcefully made the point that intuitionistic logic is concerned with the preservation of constructibility. (See section 2.1 above.)
- Brouwer’s proof of the bar theorem from 1924, handed in on March 29, 1924 (Brouwer 1924D1: 189 [Mancosu 1998: 36])[^mancosu-1998], and perhaps also the later version from 1927, of which the manuscript was handed in on April 28, 1926 (Brouwer 1927B: 75 [van Heijenoort 1967: 446])[^heijenoort-1967]; both show how to operate mathematically on demonstrations as objects. (See section 3.1.2 above.)
- Weyl 1921, where universal and existential theorems are considered to be not genuine judgements at all, but “*Urteilsanweisungen*” (judgement instructions) and “*Urteilsabstrakte*” (judgement abstracts), thus emphasizing that such theorems for their justification need to be backed up by a construction method. Brouwer, in a note on Weyl’s paper, agreed, saying “This is only a matter of name and certainly does not reflect any lacking insight on my part” (Mancosu 1998: 122)[^mancosu-1998].

A further likely influence is Brouwer’s unpublished elucidation of the virtual ordering axioms (see section 3.1.3 above). Dirk van Dalen (personal communication) suspects that, although Heyting was probably not present at this lecture course, he heard Brouwer make a similar comment on another occasion (for example during the years 1922–1925, when Heyting was working on his dissertation under Brouwer, for that work also considers intuitionistic orderings).

### 5.3 Kolmogorov 1932 and Heyting 1934

In 1932, Kolmogorov presented a logic of problems and their solutions, and pointed out that the logic this explanation validates is formally equivalent to the intuitionistic propositional and predicate logic presented by Heyting in 1930. Moreover, he suggests that this provides a better interpretation than Heyting’s.

Kolmogorov’s idea is this:

> If $a$ and $b$ are two problems, then $a \wedge b$ designates the problem “to solve both problems $a$ and $b$”, while $a \vee b$ designates the problem “to solve at least one of the problems $a$ and $b$”. Furthermore, $a \supset b$ is the problem “to solve $b$ provided that the solution for $a$ is given” or, equivalently, “to reduce the solution of $b$ to the solution of $a$” $\ldots \neg a$ designates the problem “to obtain a contradiction provided that the solution of $a$ is given” $\ldots(x)a(x)$ stands in general for the problem “to give a general method for the solution of $a(x)$ for every single value of $x$”. (Kolmogorov 1932: 59 [Mancosu 1998: 329])[^kolmogorov-1932][^mancosu-1998]

He then lists Heyting’s axioms for propositional logic (with Heyting’s numbering) and, by discussing an example, makes it clear that these all hold when interpreted as statements about problems and their solutions. He also points out that $a \vee \neg a$ is the problem

> to give a general method that allows, for every problem $a$, either to find a solution for $a$, or to infer a contradiction from the existence of a solution for $a$!
>
> In particular, if the problem $a$ consists in the proof of a proposition, then one must possess a general method either to prove or to reduce to a contradiction any proposition. (Kolmogorov 1932: 63 [Mancosu 1998: 332])[^kolmogorov-1932][^mancosu-1998].

In the second part of his paper, Kolmogorov argues that, given the epistemological tenets of intuitionism,

> intuitionistic logic should be replaced by the calculus of problems, for its objects are in reality not theoretical propositions but rather problems. (Kolmogorov 1932: 58 [Mancosu 1998: 328])[^kolmogorov-1932][^mancosu-1998]

That he considers his interpretation an alternative to Heyting’s, and a preferable one, is again emphasized in a note added in proof:

> This interpretation of intuitionistic logic is closely connected with the ideas Mr. Heyting has developed in the last volume of *Erkenntnis* 2, 1931: 106 [Heyting 1931][^heyting-1931]; yet in Heyting a clear distinction between propositions and problems is missing. (Kolmogorov 1932: 65 [Mancosu 1998: 334])[^kolmogorov-1932][^mancosu-1998]

But it is not at all clear that Heyting would want to make that distinction. If the notion of proposition is understood in such a way that a proposition is true or false independently of our knowledge of this fact, then Heyting would readily agree with Kolmogorov that a proposition is different from a problem; but as soon as one adopts the view that propositions express intentions that are fulfilled (and the proposition made true) or disappointed (and the proposition made false) by our mathematical constructions, which is the view that Heyting actually held, then there would seem to be no essential difference between propositions and problems. Kolmogorov himself had already indicated that a problem may consist in finding the proof of a proposition; exploiting this, one can argue that the following two notions of proposition coincide:

1. propositions express intentions towards constructions
2. propositions pose problems which are solved by carrying out constructions

The basic idea is that a proposition in sense 1 gives rise to the problem of finding a construction that fulfills the expressed intention, and that a solution to a problem posed in a proposition in sense 2 also serves to fulfill the intention towards constructions that solve that problem; this is made fully explicit in a little argument due to Martin-Löf, given in detail in Sundholm 1983: 158–159.

In a letter to Heyting of October 12, 1931, Kolmogorov in effect agrees that the difference between Heyting and him is mainly a terminological matter (Troelstra 1990: 15)[^troelstra-1990].

Heyting later claimed that Kolmogorov’s meaning explanation and his own amounted to the same (Heyting 1958C: 107). By 1937, Kolmogorov seems to have come to believe the same, as in a review in the *Zentralblatt* of an exchange between Freudenthal and Heyting (discussed in Section 1 of the supplementary document Objections to the Proof Interpretation), he consistently speaks of “intention or problem” (Kolmogorov 1937)[^kolmogorov-1937]. In that exchange itself, Freudenthal (1937: 114) had said that between Heyting’s and Kolmogorov’s explanations there was “no essential difference”. Finally, Oskar Becker, in a letter to Heyting of September 1934, had remarked that Heyting’s interpretation is a generalization of Kolmogorov’s, as a “problem” and its “solution” are special cases of an intention and its fulfillment. “Intuitionistic logic is therefore a ‘calculus of intentions’”.[^note-30]

However, a complication for the identification of Heyting’s and Kolmogorov’s explanations of logic is introduced by Kolmogorov’s also accepting, in a particular case, solutions that do not consist in a carrying out a concrete construction. Kolmogorov said that “As soon as $\neg a$ is solved, then the solution of $a$ is impossible and the problem $a \rightarrow b$ is without content” (Kolmogorov 1932: 62 [Mancosu 1998: 331])[^kolmogorov-1932][^mancosu-1998], and proposed that “The proof that a problem is without content [owing to an impossible assumption] will always be considered as its solution” (Kolmogorov 1932: 59: [Mancosu 1998: 329])[^kolmogorov-1932][^mancosu-1998]. Taken together, this yields a justification of *Ex Falso*, $\neg a \rightarrow(a \rightarrow b)$.

It seems not altogether unreasonable to extend the meaning of the term “solution” this way, for, just like a concrete solution, an impossibility proof also provides what might be called “epistemic closure”: like a concrete solution, it provides a completely convincing reason to stop working on a certain problem. (This kind of “higher-order” solution is also familiar from Hilbert’s Program, e.g., Hilbert 1900: 51.)[^hilbert-1900] Note that this justification of *Ex Falso* makes no attempt to describe a counterfactual mathematical construction process; thus, Kolmogorov’s justification in 1932 is not really incompatible with the ground for his rejection of *Ex Falso* in 1925, namely, that one cannot constructively assert consequences of something impossible. Rather, the solution from 1932 introduces a stipulation to achieve completion of the logical theory for its own sake.

On the other hand, although Kolmogorov’s stipulation is neither unreasonable nor unmotivated, on Brouwer’s descriptive conception of logic there is of course no place for stipulation. For this reason, “Proof Interpretation” seems to be a more appropriate name for an explanation of Brouwerian logic than “BHK Interpretation”.

On Heyting’s explanation, however, a justification of *Ex Falso* parallel to Kolmogorov’s would seem to be impossible: while a problem may find a “higher-order” solution when it is shown that a solution is impossible, it makes no sense to say that an intention finds “higher-order” fulfillment when it is shown that it cannot be fulfilled. The notion of a solution seems to permit a reasonable extension that the notion of fulfillment does not. In his book from 1934, Heyting explains *Ex Falso* in Kolmogorov’s terms, not his own. After stating the axiom $\neg a \supset (a \supset b)$, he says:

> It is appropriate to interpret the notion of “reducing” in such a way, that the proof of the impossibility of solving $a$ at the same time reduces the solution of any problem whatsoever to that of $a$. (Heyting 1934: 15; translation mine)[^heyting-1934]

Clearly there is a difference between Kolmogorov’s own explanation and Heyting’s explanation in Kolmogorov’s terms. Where Heyting says that a proof of $\neg a$ establishes a reduction of the solution of any problem to that of $a$, Kolmogorov had said that it established that the problem of reducing the solution of any problem to that of $a$ has become without content. One has the impression that Heyting in his explanation of *Ex Falso* tries to approximate as closely as possible the explanation for ordinary implications in terms of a concrete constructive connection between antecedent and consequent; this is even clearer in the explanation he would give of *Ex Falso* in 1956 (see section 5.4 below). (Note that neither Heyting nor Kolmogorov ever justified *Ex Falso* by giving the traditional argument (based on the disjunctive syllogism) also stated in Glivenko’s paper from 1929; see section 4.3 above.)

More generally, the explanation of logic in Heyting 1934 is for the most part given Kolmogorov style, and not Heyting’s own in terms of intentions and their fulfillment. (The latter is only mentioned for its explanation of the implication (Heyting 1934: 14)[^heyting-1934].) Perhaps the reason for this is that Heyting (1934: 14)[^heyting-1934] agrees with Kolmogorov (1932: 58)[^kolmogorov-1932] that the interpretation in terms of problems and solutions provides a useful interpretation Heyting’s formal system also for non-intuitionists (while for intuitionists they come to the same thing). In his short note 1932C, titled “The application of intuitionistic logic to the definition of completeness of a logical calculus”, Heyting uses Kolmogorov’s interpretation instead of his own. Given the subject matter, that is what one might expect.

### 5.4 Heyting 1956

In his influential book *Intuitionism. An introduction* from 1956, Heyting explains the logical connectives as follows (97–98, 102):

1. “A mathematical proposition $p$ always demands a mathematical construction with certain given properties; it can be asserted as soon as such a construction has been carried out”.
2. “$p \wedge q$ can be asserted if and only if both $p$ and $q$ can be asserted”.
3. “$p \vee q$ can be asserted if and only if at least one of the propositions $p$ and $q$ can be asserted”.
4. “$\neg p$ can be asserted if and only if we possess a construction which from the supposition that a construction $p$ were carried out, leads to a contradiction”.
5. “The implication $p \rightarrow q$ can be asserted, if and only if we possess a construction $r$, which, joined to any construction proving $p$ (supposing that the latter be effected), would automatically effect a construction proving $q$”.
6. “$\vdash(\forall x)p(x)$ means that $p(x)$ is true for every $x$ in $Q$ [over which $x$ ranges]; in other words, we possess a general method of construction which, if any element $a$ of $Q$ is chosen, yields by specialization the construction $p(a)$”.
7. “$(\exists x)p(x)$ will be true if and only if an element $a$ of $Q$ for which $p(a)$ is true has actually been constructed”.

Note that these explanations are not in terms of *proof* conditions, but of *assertion* conditions. This may make a difference in particular for the explanation of implication, where, instead of only the information under what condition something counts as a proof of $p$, we now can also take into consideration that, by hypothesis, a concrete construction for $p$ has been effected. As we saw in section 3.1.2, the possibility to do so is crucial for Brouwer’s proof of the Bar Theorem.

In the same pages, Heyting also gave the following justification of *Ex Falso*:

> Axiom X [$\neg p \rightarrow(p \rightarrow q)$] may not seem intuitively clear. As a matter of fact, it adds to the precision of the definition of implication. You remember that $p \rightarrow q$ can be asserted if and only if we possess a construction which, joined to the construction $p$, would prove $q$. Now suppose that $\vdash \neg p$, that is, we have deduced a contradiction from the supposition that $p$ were carried out. Then, in a sense, this can be considered as a construction, which, joined to a proof of $p$ (which cannot exist) leads to a proof of $q$. (Heyting 1956: 102)[^heyting-1956]

One easily recognizes Heyting’s effort to explain *Ex Falso* as much as possible along the same lines as other implications, namely, by providing a concrete construction that leads from the antecedent to the consequent. In its attempt to provide, “in a sense”, a construction, the explanation is clearly not of the same kind as Kolmogorov’s stipulation from 1932. But it does not fit into Heyting’s original interpretation of logic in terms of intentions directed at constructions and the fulfillment of such intentions either. For to fulfill an intention directed toward a particular construction we will have to exhibit that construction; we will have to exhibit a construction that transforms any proof of $p$ into one of $q$. But how can a construction that from the assumption $p$ arrives at a contradiction, and therefore generally speaking not at $q$, lead to $q$? It will not do to say that such a construction exists “in a sense”. A construction that is a construction “in a sense”, which Heyting helps himself to here, is no construction.

Even within the intuitionistic movement, not everyone agreed with Heyting’s explanation of logic. This is discussed in a supplementary document:

> [Objections to the Proof Interpretation](intuitionistic-logic-development.objections.md)

Finally, this entry has not, as yet, discussed precursors to Brouwer, more intricate aspects of Brouwer’s “strong counterexamples”, the objections to the Proof Interpretation of circularity and impredicativity, or the later developments around the Proof Interpretation. These will be subject of future updates.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=intuitionistic-logic-development). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/intuitionistic-logic-development/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=intuitionistic-logic-development&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/intuitionistic-logic-development/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- [Review of Hesseling’s *Gnomes in the Fog* in the *Bulletin of Symbolic Logic*](http://www.math.ucla.edu/%7Easl/bsl/1003/1003-005.ps) (Postscript).
- [Dirk van Dalen’s Brouwer bibliography](https://dspace.library.uu.nl/bitstream/handle/1874/26868/preprint175.pdf).

## Related Entries

Brouwer, Luitzen Egbertus Jan | Gödel, Kurt | Hilbert, David | Hilbert, David: program in the foundations of mathematics | logic: classical | logic: intuitionistic | logic: provability | logic: relevance | mathematics, philosophy of: formalism | mathematics, philosophy of: intuitionism | mathematics: constructive | *Principia Mathematica* | proof theory | proof theory: development of | set theory: constructive and intuitionistic ZF | Wittgenstein, Ludwig: philosophy of mathematics

### Acknowledgments

I am grateful to Dirk van Dalen and Göran Sundholm for discussions of some of the issues involved. Helpful comments by the editors and Rosalie Iemhoff led to various improved formulations, corrections, and clarifications. Van Dalen kindly granted permission to quote from materials in the Brouwer Archive (at Utrecht at the time, now at the Noord-Hollands Archief in Haarlem). Thanks also to van Dalen and Eckhart Menzler-Trott for their search for Bernays’ letter to Brouwer, and to Sundholm and Michael Hegarty for a copy of de Iongh 1949. In section 3.6 I have drawn on van Atten 2004a; I thank the Association for Symbolic Logic for granting permission to do so.

## Notes（原文脚注）

[^note-1]: The *locus classicus* here is Tarski 1953. A recent treatment of formalized interpretability is Joosten 2004.

[^note-2]: One will want to impose various (structural) constraints on the interpretation, to avoid trivial ones that map for example all formulas of *U* to an axiom of *V*.

[^note-3]: Whenever a specific page is referred to of a text that is originally not in English, a reference to the corresponding page of an English translation, if available, is given as well.

[^note-4]: This is subjective time (one may think here of Husserl’s notion of inner time consciousness) rather than objective or scientific time (time as it figures in physics and that one measures with a clock); the latter, according to Brouwer, presupposes mathematics (Brouwer 1907: 99n.2 [1975: 61n.2])[^brouwer-1907].

[^note-5]: The *Collected Works* have “Formal language accompanies mathematics as the weather-map accompanies the atmospheric processes” instead (Brouwer 1975: 451)[^brouwer-1975], but that translation was based on the book version of the so-called signific dialogues (Brouwer et al. 1939)[^brouwer-1939], not on the original publication in the journal *Synthese* (Brouwer et al. 1937)[^brouwer-1937]. The book was edited by Mannoury, but it is not clear who changed the simile. To my mind, the original is better, because a symphony is also a construction.

[^note-6]: See Brouwer 1924N: 2 [van Heijenoort 1967: 336][^heijenoort-1967]; 1929A: 423–424 [Mancosu 1998: 49–50][^mancosu-1998]; 1949C: 492; 1952B: 510–511.

[^note-7]: According to Van Dalen (1999: 106–107)[^dalen-1999], it is likely that Brouwer (who entered university in 1897) learned this interpretation of PEM directly or indirectly from the teacher of logic at Amsterdam University at the time, C. Bellaar-Spruyt (1842–1901), who gave as example:

> If you deny that Alexander was a great man, well, then you have to acknowledge that he was not a great man. Both opposite judgements, A. was a great man and A. was not a great man, cannot both be false.

[^note-8]: Strictly speaking, Brouwer there considers not correctness and absurdity of propositions as such but of properties of a mathematical system; later (1949C: 1245; 1981A: 12), he gives the argument directly in terms of what he there calls “assertions”. But for example Wavre (1926)[^wavre-1926] already adopted this direct reading, as did Heyting (1930C).

[^note-9]: Brouwer’s actual theorem is about spreads, which are constructed from trees over natural numbers and in certain cases reduce to them. Also, a condition not mentioned by Brouwer is that the bar be decidable. This condition is implicitly fulfilled in the context in which the proofs of 1924 and 1927 are presented, because there the bar is defined by application of the weak continuity principle for choice sequences. This is not the case in the presentation of 1954, which is defective. See Kleene and Vesley 1965: 87–88, and Brouwer 1981A: 102.

[^note-10]: Veldman (1982)[^veldman-1982] has shown that for the continuity (as distinct from the uniform continuity) of these functions, the bar theorem is not needed. Continuity of course suffices for Brouwer’s strong counterexample.

[^note-11]: Dummett (2000: 32)[^dummett-2000] emphasizes that the conviction that there will always be open problems does not suffice to turn weak counterexamples constructed by the oscillatory number technique into strong ones. For that conviction is, he says, itself not a theorem or even a mathematical proposition.

[^note-12]: , the infinite form $\forall x\in \mathbf{R}(P(x) \vee \neg P(x))$ is contradictory for certain *P*; but that is, as Brouwer remarks, not relevant to the project of devising finitary consistency proofs (Brouwer 1928A2: 378 [Mancosu 1998: 43])[^mancosu-1998].

[^note-13]: For a similar report by Freudenthal, see van Dalen 2001a: 359.

[^note-14]: Brouwer, Notebook VIII, 44. Brouwer Archive, Noord-Hollands Archief, Haarlem; translation mine.

[^note-15]: “*Er hat die Sachen überhaupt nicht gelesen*”, Bernays in an interview by Dirk van Dalen, 1977.

[^note-16]: In a historical account that would emphasize the influence of ideas rather than their development, someone who would be given more attention to than is done here is Rolin Wavre (Hesseling 2003; Mancosu 1998)[^hesseling-2003][^mancosu-1998]. In the West, a prelude to systematical work on the formalization of intuitionistic logic was his paper “Logique formelle et logique empiriste” (Wavre 1926)[^wavre-1926]. Besides discussing differences between the classical and intuitionistic conceptions of logic, it gives a list of some propositional principles that are intuitionistically valid, as well as a list of some propositional principles that are classically valid but not intuitionistically. In this sense, it may be seen as an expanded version of Brouwer 1908C, which the otherwise well-informed Wavre however does not seem to have known. (Although the paper does not contain references, these are included in Wavre’s earlier paper of 1924, to which he refers in footnote 1. The “Bibliographie” there mentions a number of papers that appeared between 1901 and 1924 by Brouwer (including his dissertation in Dutch), Weyl, Hilbert, and Bernays.) Wavre’s 1926 paper, which was mainly expository and general in character, in effect served more to emphasize to a philosophical audience the urgency of systematic comparison than to develop one. Indeed, it sparked the Barzin-Errera episode (Hesseling 2003; Mancosu 1998)[^hesseling-2003][^mancosu-1998]. But it stopped short of presenting formalizations of either intuitionistic or classical logic. Kolmogorov published his formalization before Wavre’s paper, and Heyting’s paper from 1930 doesn’t mention it. Heyting surely knew Wavre’s 1924 paper, which he cites in his dissertation (Heyting 1925: 93)[^heyting-1925]; the 1926 paper was published in the same journal. There may well have been an indirect influence from Wavre on Heyting if the article played a role when Mannoury wrote his proposal for the 1927 prize question that would be successfully answered by Heyting; but that is only speculation.

[^note-17]: The letter to Brouwer that Bernays mentions here seems to be lost: neither in the Brouwer Archive in Utrecht (now at the Noord-Hollands Archief, Haarlem), nor in the Bernays papers at the ETH in Zürich the letter, a draft, or a carbon copy is to be found. I am thankful to Dirk van Dalen and Eckhart Menzler-Trott for verifying this for me.

[^note-18]: Letter Mannoury to Brouwer of January 26, 1927; Brouwer Archive, Noord-Hollands Archief, Haarlem.

[^note-19]: By tradition, the contest was anonymous, and a motto was required to identify the winner. Heyting’s motto is from the Bible, see Matthew 7:9 and (in many but not all translations) Luke 11:11.

[^note-20]: The members of the jury were, besides Mannoury, F. Schuh (professor of mathematics and mechanics in Delft) and J. Wolff (professor of mathematics at Utrecht university); like Brouwer, they had been students of Korteweg, and they had defended their theses around the same time as Brouwer, in 1905 and 1907, respectively.

[^note-21]: Brouwer to Heyting, July 17, 1928; Brouwer Archive, Noord-Hollands Archief, Haarlem. Translation from the Dutch mine.

[^note-22]: 1897–1940; his PhD adviser at Moscow State University was Lusin, who had worked on effective set theory, and who there had also advised Alexandrov and Urysohn (topologists who had become close friends of Brouwer’s), Khinchin (who had organized a seminar on intuitionism in Moscow in 1926), and Kolmogorov (who had published on intuitionistic logic in 1925). In such an environment, it is not surprising that Glivenko became acquainted with and interested in Brouwer’s intuitionism.

[^note-23]: That way of justifying *Ex Falso* was already known in the 13th century.

[^note-24]: In relevant logics it is objectionable as well, and this is no coincidence. See van Atten 2009.

[^note-25]: In the 1950s, the formalization of intuitionistic analysis was taken up again by Kleene, which led to the influential monograph Kleene and Vesley 1965; his system was not inspired by Heyting’s, see Kleene 1973. Later attempts are Myhill 1966 and Vesley 1980.

[^note-26]: As Göran Sundholm emphasized in conversation, the “relative completeness” that Heyting mentions, i.e., the richness of the presentation of logic in *Principia Mathematica*, must have been his reason for not taking Hilbert 1923 as his point of departure.

[^note-27]: The classical system was that of Whitehead 1906, where the axioms are taken from Pieri 1898.

[^note-28]: The Heyting papers are kept at the Noord-Hollands Archief, Haarlem.

[^note-29]: No manuscript of such a note seems to have survived.

[^note-30]: In his letter, Becker does not give the exact date. The Becker-Heyting correspondence, to the extent to which it seems to have been preserved, is kept with the Heyting papers at the Noord-Hollands Archief, Haarlem; it has been published in van Atten 2005.

[^note-31]: 31\. In a letter to Heyting of May 16, 1933, Gödel says he had found the translation in June 1932 (Gödel 2003a: 71)[^gödel-2003a]. In an earlier letter to Heyting, dated November 15, 1932 and concerning their projected joint book, Gödel asked Heyting to

> say something about the relation of Hilbert’s finitism (as he advocated it in his earlier works) and intuitionism. The former might perhaps recognize even fewer inference rules and concept formations than the latter. (Gödel 2003a: 63)[^gödel-2003a]

Note that Gödel did not take this earlier opportunity to announce his translation to Heyting.

[^note-32]: 32\. A translation of intuitionistic propositional logic into a modal logic (anticipating $\mathbf{S4})$ had been given before Gödel, and before the earlier (failed) attempt Becker 1930 (cited by Gödel), by the Russian logician I.E. Orlov. See Došen 1992 and Bazhanov 2003. It seems that Gödel and Becker were unaware of this precursor.

[^note-33]: 33\. One has the impression that Gödel (1933f: 39n.1 [1986: 301n.1]) misses this point when he comments

> Kolmogorov (1932)[^kolmogorov-1932] has given a somewhat different interpretation of the intuitionistic propositional calculus, without, to be sure, specifying a precise formalism.

[^note-34]: 34\. Examples of interpretations of intuitionistic predicate logic in intuitionistically acceptable systems are Veldman 1976 and de Swart 1976, 1977. Veldman (1976: 159)[^veldman-1976] is explicit that his construction does not clarify the concept “intuitionistically true sentence” but is a technical device.

[^note-35]: 35\. The reference was in Carnaps’s *Logische Syntax der Sprache* (Johansson to Heyting, November 15, 1935.)

[^note-36]: 36\. As Heyting recalls in his letter of November 5, 1935 (page 3), they had in fact met, briefly, in Zürich in 1932; see also Johansson’s letter of November 15, 1935 (page 3). The latter letter is also informative about Johansson’s intellectual background. The Heyting-Johansson correspondence as kept in Heyting’s archive ends with a postcard from Johansson of January 28, 1936. The Heyting papers are at the Noord-Hollands Archief, Haarlem.

[^note-37]: 37\. “Appropriate” here translates the Dutch “*doelmatig*”. Other translations of that term are “suitable”, “efficient”, “practical” (*Groot Woordenboek Nederlands-Engels*, Utrecht: van Dale 2008). The latter two may suggest a pragmatic criterion. But that can hardly be what Heyting had in mind, given that he thought of logical theorems as highly general mathematical ones, and thus, intuitionistically, certain.

[^note-38]: 38\. This emends van Atten et al. 2014: 273 and van Atten & Sundholm 2016: 36, who stated that “to the best of our knowledge, the meeting never took place”.

[^note-39]: 39\. The term “*Katalogisierung*” in this context is sometimes translated as “cataloguing” and more often as “locating”; the former seems to fit better here. Freudenthal’s definition is in fact proposed as an alternative to one that Brouwer made in a topological context (Brouwer 1926B2: 855). Freudenthal (1937a: 110)[^freudenthal-1937a] proves that the two definitions are equivalent.

[^note-40]: 40\. A technical mistake in Heyting’s manuscript had been corrected by Brouwer. See van Dalen 2011: 393 for the letter, and also the extract and related remarks in Brouwer 1942A.

[^note-41]: 41\. Also in later publications, e.g.,

> If mathematics consists of mental constructions, then every mathematical theorem is the expression of a result of a successful construction. The proof of the theorem consists in this construction itself, and the steps of the proof are the same as the steps of the mathematical construction. (Heyting 1958C: 107)

[^note-42]: 42\. In 1947 Paulette Destouches-Février proposed a middle position between Griss’ logic, which she found too extreme, and that of Brouwer and Heyting by adding to the former the definition of $\neg p$ as $p \rightarrow(1=2)$, but no axioms for it (Destouches-Février 1947b: 1243)[^destouches-février-1947b]. However, she does not motivate this philosophically. Destouches-Février (1914–2013) published (among many other things) a number of short technical notes on intuitionistic logic, Griss’ logic, and Johansson’s logic (1945a,b, 1947a,b, 1948, 1949, 1951). She was also the French translator of Heyting’s manuscript for Heyting 1955.

[^note-43]: 43\. Brouwer presented Griss 1944, 1946, 1950, 1951a, and 1951b; Heyting presented Griss 1951c and 1951d, which dealt with intuitionistic axiomatic geometry.

[^note-44]: 44\. Brouwer himself has published mathematical papers that he, without mentioning it at the time, did not sanction philosophically, namely, his papers in classical topology from the period 1909–1913, in which he used the classical reasoning that philosophically he had already rejected in Brouwer 1908C. Looking back on that period, Brouwer once called those papers “free of philosophy” (*philosophiefrei*; Brouwer 1919D: 204).

[^note-45]: 45\. Heyting (1958C: 111) remarks that “from the intuitionistic point of view this restriction is difficult to account for”, and seems to overlook that Van Dantzig addresses the classical mathematician (van Dantzig 1947b: 1092)[^dantzig-1947b].

[^note-46]: 46\. Another development by Van Dantzig was ‘stable mathematics’ (1947a, 1951), an ecumenical attempt, inspired by Gödel’s double negation translation of classical into intuitionistic arithmetic (see section 4.5.1), to develop a fragment of classical mathematics in which all theorems are equivalent to their double negations also by intuitionistic standards. Gilmore (1956)[^gilmore-1956] pointed out in his review of van Dantzig 1951 that the greater problem for that project is not the occurrence in classical mathematics of the principle of the excluded middle but of impredicative definitions (see on this point also Gödel \*1933o and \*1941)[^gödel-1941].

[^brouwer’s-1997a]: Brouwer’s writings are referred to according to the scheme in the bibliography van Dalen 1997a; Gödel’s, according to the bibliography in Gödel 1986, Gödel 1990, Gödel 1995 (except for Gödel 1970); Heyting’s, according to the bibliography Troelstra et al. 1981 (except for Heyting 1928).

[^apostel-1972]: Apostel, L., 1972, “Negation: The tension between ontological positivity (negationless positivity) and anthropological negativity (positively described)”, *Logique et Analyse*, 15(57–58): 209–317. [[Apostel 1972 available online](http://virthost.vub.ac.be/lnaweb/ojs/index.php/LogiqueEtAnalyse/article/view/591)]

[^artemov-2001]: Artemov, Sergei N., 2001, “Explicit provability and constructive semantics”, *Bulletin of Symbolic Logic*, 7(1): 1–36. doi:10.2307/2687821

[^arruda-1978]: Arruda, Ayda Ignez, 1978, “Some remarks on Griss’ logic of negationless intuitionistic mathematics”, in *Mathematical Logic, Proceedings of the 1st Brazilian Conference on Mathematical Logic, Campinas 1977* (Lecture Notes in Pure and Applied Mathematics 39), A.I. Arruda, N.C.A. da Costa, R. Chuaqui (eds.), 9–29.

[^atten-2004a]: van Atten, Mark, 2004a, “Review of Dennis E. Hesseling, *Gnomes in the Fog. The Reception of Brouwer’s Intuitionism in the 1920s*”, *Bulletin of Symbolic Logic*, 10(3): 423–427. doi:10.2307/3185194

[^atten-2004b]: –––, 2004b, *On Brouwer*, Belmont, CA: Wadsworth.

[^atten-2005]: –––, 2005, “The correspondence between Oskar Becker and Arend Heyting”, in *Oskar Becker und die Philosophie der Mathematik*, V. Peckhaus (ed.), München: Wilhelm Fink, 119–142.

[^atten-2009]: –––, 2009, “The hypothetical judgement in the history of intuitionistic logic”, in *Logic, Methodology, and Philosophy of Science 13: Proceedings of the 2007 International Congress in Beijing*, C. Glymour, W. Wang, and D. Westerståhl, eds., London: King’s College Publications, 122–136.

[^atten-2018]: –––, 2018, “The Creating Subject, the Brouwer-Kripke Schema, and infinite proofs”, *Indagationes Mathematicae*, 29: 1565–1636. doi: 10.1016/j.indag.2018.06.005

[^atten-2014]: van Atten, Mark, Göran Sundholm, Michel Bourdeau, and Vanessa van Atten, 2014, “‘Que les principes de la logique ne sont pas fiables.’ Nouvelle traduction française annotée et commentée de l’article de 1908 de L.E.J. Brouwer”, *Revue d’Histoire des Sciences*, 67(2): 257–281. doi:10.3917/rhs.672.0257

[^atten-2008]: van Atten, Mark, Pascal Boldini, Michel Bourdeau, and Gerhard Heinzmann (eds.), 2008, *One Hundred Years of Intuitionism (1907–2007). The Cerisy Conference*, Basel: Birkhäuser. doi:10.1007/978-3-7643-8653-5

[^atten-2017]: van Atten, Mark and Göran Sundholm, 2017, “L.E.J. Brouwer’s ‘Unreliability of the logical principles’: A new translation, with an introduction”, *History and Philosophy of Logic*, 38(1): 24–47. doi:10.1080/01445340.2016.1210986

[^barzin-1927]: Barzin, M. and A. Errera, 1927, “Sur la logique de M. Brouwer”, *Académie Royale de Belgique, Bulletin de la classe des sciences*, 13: 56–71.

[^bazhanov-2003]: Bazhanov, Valentin A., 2003, “The Scholar and the ‘Wolfhound Era’: The Fate of Ivan E. Orlov’s Ideas in Logic, Philosophy, and Science”, *Science in Context*, 16(4): 535–550. doi:10.1017/S0269889703000954

[^becker-1927]: Becker, Oskar, 1927, “Mathematische Existenz. Untersuchungen zur Logik und Ontologie mathematischer Phänomene”, *Jahrbuch für Philosophie und phänomenologische Forschung*, 8: 439–809.

[^becker-1930]: –––, 1930, “Zur Logik der Modalitäten”, *Jahrbuch für Philosophie und phänomenologische Forschung*, 11: 497–548.

[^benacerraf-1983]: Benacerraf, Paul and Hilary Putnam (eds.), 1983, *Philosophy of Mathematics: Selected Readings*, second edition, Cambridge: Cambridge University Press. doi:10.1017/CBO9781139171519

[^bergson-1907]: Bergson, Henri, 1907, *L’Évolution Créatrice*, Paris: Félix Alcan.

[^bernays-1926]: Bernays, Paul, 1926, “Axiomatische Untersuchung des Aussagen-Kalküls der ‘Principia Mathematica’”, *Mathematische Zeitschrift*, 25: 305–320. doi:10.1007/BF01283841

[^bernays-1967]: –––, 1967, “Hilbert, David”, in *The Encyclopedia of Philosophy*, vol. 3, Paul Edwards (ed.), New York: Macmillan.

[^beth-1956]: Beth, Evert W., 1956, “Semantic Construction of Intuitionistic Logic”, *Mededelingen der Koninklijke Nederlandse Akademie van Wetenschappen. Afdeling Letterkunde*, 19(11): 357–388.

[^beth-1966]: –––, 1966, *The Foundations of Mathematics: A Study in the Philosophy of Science*, second revised edition, New York: Harper & Row.

[^blaschek-1994]: Blaschek, Günther, 1994, *Object-Oriented Programming: with Prototypes*, Berlin: Springer. doi:10.1007/978-3-642-78077-6

[^borwein-1998]: Borwein, Jonathan M., 1998, “Brouwer-Heyting Sequences Converge”, *Mathematical Intelligencer*, 20(1): 14–15. doi:10.1007/BF03024393

[^brouwer-1907]: Brouwer, L.E.J., 1907, *Over de Grondslagen der Wiskunde* (On the Foundations of Mathematics), Ph.D. thesis, Universiteit van Amsterdam. English translation in Brouwer 1975: 11–101.

[^brouwer-1908c]: –––, 1908C, “De onbetrouwbaarheid der logische principes” (The Unreliability of the Logical Principles), *Tijdschrift voor Wijsbegeerte*, 2: 152–158. English translation in Van Atten and Sundholm 2017. An older English translation is in Brouwer 1975: 107–111. doi:10.1016/B978-0-7204-2076-0.50009-X

[^brouwer-1918b]: –––, 1918B, “Begründung der Mengenlehre unabhängig vom logischen Satz vom ausgeschlossenen Dritten. Erster Teil, Allgemeine Mengenlehre”, *KNAW Verhandelingen*, 5: 1–43. Also in Brouwer 1975: 150–190 (in German). doi:10.1016/B978-0-7204-2076-0.50015-5

[^brouwer-1919a]: –––, 1919A, “Begründung der Mengenlehre unabhängig vom logischen Satz vom ausgeschlossenen Dritten. Zweiter Teil, Theorie der Punktmengen”, *KNAW Verhandelingen*, 7: 1–33. Also in Brouwer 1975: 191–221 (in German). doi:10.1016/B978-0-7204-2076-0.50016-7

[^brouwer-1919d]: –––, 1919D, “Intuitionistische Mengenlehre”, *Jahresbericht D.M.V.*, 28: 203–208. English translation in Mancosu 1998: 23–27.

[^brouwer-1921a]: –––, 1921A, “Besitzt jede reelle Zahl eine Dezimalbruchentwicklung?”, *Mathematische Annalen*, 83(3–4): 201–210. English translation in Mancosu 1998: 28–35. doi:10.1007/BF01458382

[^brouwer-1998]: –––, 1924D1, “Bewijs dat iedere volle functie gelijkmatig continu is”, *KNAW verslagen*, 33: 189–193. English translation in Mancosu 1998: 36–39.

[^brouwer-1967]: –––, 1924N, “Über die Bedeutung des Satzes vom ausgeschlossenen Dritten in der Mathematik, insbesondere in der Funktionentheorie”, *Journal für die reine und angewandte Mathematik*, 154: 1–7. English translation in van Heijenoort 1967: 335–341.

[^brouwer-1925e]: –––, 1925E, “Intuitionistische Zerlegung mathematischer Grundbegriffe”, *Jahresbericht D.M.V.*, 33: 251–256. English translation in Mancosu 1998: 287–289 (sections 2–4), 290–292 (section 1).

[^brouwer-1926a]: –––, 1926A, “Zur Begründung der intuitionistischen Mathematik, II”, *Mathematische Annalen*, 95: 453–472. doi:10.1007/BF01206621

[^brouwer-nd]: –––, 1926B2, “Intuitionistische Einführung des Dimensionsbegriffes”, *Proceedings Koninklijke Akademie van Wetenschappen Amsterdam*, 29: 855–873.

[^brouwer-1927b]: –––, 1927B, “Über Definitionsbereiche von Funktionen”, *Mathematische Annalen*, 97: 60–75. English translation of sections 1–3 in van Heijenoort 1967: 457–463. doi:10.1007/BF01447860

[^brouwer-1998-2]: –––, 1928A2, “Intuitionistische Betrachtungen über den Formalismus”, *Proceedings Koninklijke Akademie van Wetenschappen Amsterdam*, 31: 374–379. English translation in Mancosu 1998: 40–44. [[Brouwer 1928A2 available online](http://www.dwc.knaw.nl/DL/publications/PU00015590.pdf)]

[^brouwer-1929a]: –––, 1929A, “Mathematik, Wissenschaft und Sprache”, *Monatshefte für Mathematik und Physik*, 36: 153–164. English translation in Mancosu 1998: 45–53. doi:10.1007/BF02307611

[^brouwer-1930a]: –––, 1930A, *Die Struktur des Kontinuums*, Wien: Komitee zur Veranstaltung von Gastvorträgen ausländischer Gelehrter der exakten Wissenschaften. English translation in Mancosu 1998: 54–63.

[^brouwer-1990]: –––, 1933A2, “Willen, weten, spreken” (Volition, Knowledge, Language), in *De Uitdrukkingswijze der Wetenschap*, L.E.J. Brouwer et al., Groningen: Noordhoff, 45–63. English translation in van Stigt 1990: 418–431. Partial English translation in Brouwer 1975: 443–446.

[^brouwer-1942a]: –––, 1942A, “Zum freien Werden von Mengen und Funktionen”, *Proceedings Nederlandse Akademie van Wetenschappen Amsterdam*, 45: 322–323. Also *Indagationes Mathematicae*, 4 (1942): 107–108.

[^brouwer-1942b]: –––, 1942B, “Die repräsentierende Menge der stetigen Funktionen des Einheitskontinuums”, *Proceedings Nederlandse Akademie van Wetenschappen Amsterdam*, 45: 443. Also *Indagationes Mathematicae*, 4 (1942): 154.

[^brouwer-1948a]: –––, 1948A, “Essentieel negatieve eigenschappen” (Essentially Negative Properties), *Proceedings Koninklijke Nederlandse Akademie van Wetenschappen Amsterdam*, 51: 963–964. Also *Indagationes Mathematicae*, 10 (1948): 322–323. English translation in Brouwer 1975: 478–479. doi:10.1016/B978-0-7204-2076-0.50053-2

[^brouwer-1949a]: –––, 1949A, “De non-aequivalentie van de constructieve en de negatieve orderelatie in het continuum” (The Non-Equivalence of the Constructive and the Negative Order Relation on the Continuum), *Proceedings Koninklijke Nederlandse Akademie van Wetenschappen Amsterdam*, 52:122–124. Also *Indagationes Mathematicae*, 11 (1949): 37–39. English translation in Brouwer 1975: 495–496. doi:10.1016/B978-0-7204-2076-0.50055-6

[^brouwer-1949b]: –––, 1949B, “Contradictoriteit der elementaire meetkunde” (Contradictority of Elementary Geometry), *Proceedings Koninklijke Nederlandse Akademie van Wetenschappen Amsterdam*, 52: 315–316. Also *Indagationes Mathematicae*, 11 (1949): 89–90. English translation in Brouwer 1975: 497–498. doi:10.1016/B978-0-7204-2076-0.50056-8

[^brouwer-1949c]: –––, 1949C, “Consciousness, Philosophy and Mathematics”, *Proceedings of the 10th International Congress of Philosophy, Amsterdam 1948*, Amsterdam: North-Holland, 3: 1235–1249.

[^brouwer-1952b]: –––, 1952B, “Historical Background, Principles and Methods of Intuitionism”, *South African Journal of Science*, 49: 139–146.

[^brouwer-1954a]: –––, 1954A, “Points and Spaces”, *Canadian Journal of Mathematics*, 6: 1–17. doi:10.4153/CJM-1954-001-9

[^brouwer-1954]: –––, 1954F, “An Example of Contradictority in Classical Theory of Functions”, *Proceedings Koninklijke Nederlandse Akademie van Wetenschappen Amsterdam*, 57: 204–205. Also *Indagationes Mathematicae*, 16 (1954): 204–205. doi:10.1016/S1385-7258(54)50030-2

[^brouwer-1955]: –––, 1955, “The Effect of Intuitionism on Classical Algebra of Logic”, *Proceedings of the Royal Irish Academy*, 57: 113–116.

[^brouwer-1975]: –––, 1975, *Collected Works. I: Philosophy and Foundations of Mathematics*, Arend Heyting (ed.), Amsterdam: North-Holland.

[^brouwer-1977]: –––, 1977, *Collected Works. II: Geometry, Analysis, Topology and Mechanics*, H. Freudenthal (ed.), Amsterdam: North-Holland.

[^brouwer-1981a]: –––, 1981A, *Brouwer’s Cambridge Lectures on Intuitionism*, Cambridge: Cambridge University Press.

[^brouwer-1937]: Brouwer, L.E.J., Fred. van Eeden, J. van Ginneken, and S.J.G. Mannoury, 1937, “Signifiese dialogen”, *Synthese*, 2: 168–174, 261–268, 316–324. doi:10.1007/BF00880415 doi:10.1007/BF00880431 doi:10.1007/BF00880440

[^brouwer-1939]: –––, 1939, *Signifische dialogen*, Utrecht: Erven J. Bijleveld. Partial English translation in Brouwer 1975: pp. 447–452.

[^chronique-1949]: Chronique générale, 1949. “Chronique générale”, *Revue Philosophique de Louvain*, 47(15): 432–436. [[Chronique générale 1949 available online](http://www.persee.fr/doc/phlou_0035-3841_1949_num_47_15_4211)]

[^colacito-2017]: Colacito, Almudena, Dick de Jongh, and Ana Lucia Vargas, 2017, “Subminimal Negation”, *Soft Computing*, 2(1): 165–174. doi:10.1007/s00500-016-2391-8

[^colson-2007]: Colson, Loïc, and David Michel, 2007, “Pedagogical Natural Deduction Systems: the Propositional Case”, *Journal of Universal Computer Science*, 13(10): 1396–1410. [[Colson & Michel 2007 available online](http://www.jucs.org/doi?doi=10.3217/jucs-013-10-1396)]

[^colson-2008]: –––, 2008, “Pedagogical Second-order Propositional Calculi”, *Journal of Logic and Computation*, 18(4): 669–695. doi:10.1093/logcom/exn001

[^colson-2009]: –––, 2009, “Pedagogical Second-order *λ*-calculus”, *Theoretical Computer Science*, 410(42): 4190–4203. doi:10.1016/j.tcs.2009.04.020

[^dalen-1973]: van Dalen, Dirk, 1973, “Lectures on intuitionism”, in Mathias & Rodgers 1973: 1–94. doi:10.1007/BFb0066771

[^dalen-1997]: –––, 1997, “A Bibliography of L.E.J. Brouwer”, Utrecht Logic Group Preprint Series, no. 175 [[van Dalen 1997 updated preprint available from Universiteit Utrecht]](https://dspace.library.uu.nl/handle/1874/26868). Updated version in van Atten et al. 2008: 343–390. doi:10.1007/978-3-7643-8653-5_22

[^dalen-1999]: –––, 1999, *Mystic, Geometer, and Intuitionist. The Life of L.E.J. Brouwer. 1: The Dawning Revolution*, Oxford: Clarendon Press.

[^dalen-2001a]: –––, 2001a, *L.E.J. Brouwer 1881–1966. Een Biografie. Het Heldere Licht van de Wiskunde*, Amsterdam: Bert Bakker.

[^dalen-2001b]: –––, 2001b, *L.E.J. Brouwer en de Grondslagen van de Wiskunde*, Utrecht: Epsilon.

[^dalen-2004]: –––, 2004, “Kolmogorov and Brouwer on constructive implication and the Ex Falso rule”, *Russian Mathematical Surveys*, 59(2): 247–257. doi:10.1070/RM2004v059n02ABEH000717

[^dalen-2005]: –––, 2005, *Mystic, Geometer, and Intuitionist. The Life of L.E.J. Brouwer. 2: Hope and Disillusion*, Oxford: Clarendon Press.

[^dalen-2008]: –––, 2008, “Another look at Brouwer’s dissertation”, in van Atten et al. 2008: 3–20. doi:10.1007/978-3-7643-8653-5_1

[^dalen-2011]: ––– (ed.), 2011, *The Selected Correspondence of L.E.J. Brouwer*, London: Springer. An online supplement (link and password on the copyright page of the book) presents most of the extant correspondence, but without English translations. doi:10.1007/978-0-85729-537-8

[^dalen-2007]: van Dalen, Dirk and Volker R. Remmert, 2007, “Ce périodique foncièrement international: the birth and youth of Compositio Mathematica”, *Nieuw Archief voor Wiskunde* 5th series, 8(3): 178–189. [[van Dalen & Remmert 2007 available online](http://www.nieuwarchief.nl/serie5/pdf/naw5-2007-08-3-178.pdf)]

[^dantzig-1947a]: van Dantzig, D., 1947a, “On the principles of intuitionistic and affirmative mathematics. I”, *Proceedings Koninklijke Nederlandse Akademie van Wetenschappen Amsterdam*, 50: 918–929. Also *Indagationes Mathematicae*, 9: 429–440.

[^dantzig-1947b]: –––, 1947b, “On the principles of intuitionistic and affirmative mathematics. II”, *Proceedings Koninklijke Nederlandse Akademie van Wetenschappen Amsterdam*, 50:1092–1103. Also *Indagationes Mathematicae*, 9: 506–517.

[^dantzig-1949]: –––, 1949, “Comments on Brouwer’s Theorem on Essentially-negative predicates”, *Proceedings Koninklijke Nederlandse Akademie van Wetenschappen Amsterdam*, 52: 949–957. Also *Indagationes Mathematicae*, 11: 347–355.

[^dantzig-1951]: –––, 1951, “Mathématique stable et mathématique affirmative”, *Congrès International de Philosophie des Sciences, 1949, II Logique* (Actualités scientifiques et industrielles 1134), Paris: Hermann & Cie, pp. 123–135.

[^demange-2015]: Demange, Vincent, 2015, “Pedagogical lambda-cube: the λ² case”, *Journal of Logic and Computation*, 25(3): 743–779. doi: 10.1093/logcom/exu049

[^dequoy-1952]: Dequoy, Nicolle, 1952 [1955], *Axiomatique intuitionniste sans négation de la géométrie projective*, PhD thesis, Université de Paris. Published in 1955, Paris:Gauthier-Villars (Collection de logique mathématique ; sér. A, 6).

[^destouches-février-1945a]: Destouches-Février, Paulette, 1945a, “Rapports entre le calcul des problèmes et le calcul des propositions”, *Comptes Rendus de l’Académie des sciences*, 220: 484–486. [[Destouches-Février 1945a available online](https://gallica.bnf.fr/ark:/12148/bpt6k3172c/f484)]

[^destouches-février-1945b]: –––, 1945b, “Logique adaptee aux théories quantiques”, *Comptes Rendus de l’Académie des sciences*, 221: 287–288. [[Destouches-Février 1945b available online](https://gallica.bnf.fr/ark:/12148/bpt6k3173p/f287)]

[^destouches-février-1947a]: –––, 1947a, “Sur la notion d’adequation et le calcul minimal de Johannsson”, *Comptes Rendus de l’Académie des sciences*, 224: 545–547. [[Destouches-Février 1947a available online](https://gallica.bnf.fr/ark:/12148/bpt6k3176m/f545)]

[^destouches-février-1947b]: –––, 1947b, “Esquisse d’une mathématique intuitioniste positive”, *Comptes Rendus de l’Académie des sciences*, 225: 1241–1243. [[Destouches-Février 1947b available online](https://gallica.bnf.fr/ark:/12148/bpt6k3177x/f1243)]

[^destouches-février-1948]: –––, 1948, “Logique de l’intuitionisme sans négation et logique de l’intuitionisme positif”, *Comptes Rendus de l’Académie des sciences*, 226: 38–39. [[Destouches-Février 1948 available online](https://gallica.bnf.fr/ark:/12148/bpt6k31787/f38)]

[^destouches-février-1949]: –––, 1949, “Connexions entre les calculs des constructions, des problèmes, des propositions”, *Comptes Rendus de l’Académie des sciences*, 228: 31–33. [[Destouches-Février 1949 available online](https://gallica.bnf.fr/ark:/12148/bpt6k31801/f31)]

[^destouches-février-1951]: –––, 1951, “Sur l’intuitionnisme et la conception strictement constructive”, *Proceedings Koninklijke Nederlandse Akademie van Wetenschappen Amsterdam*, 54: 80–86. doi:10.1016/S1385-7258(51)50012-4

[^došen-1992]: Došen, Kosta, 1992, “The First Axiomatization of Relevant Logic”, *Journal of Philosophical Logic*, 21(4): 339–356. doi:10.1007/BF00260740

[^dummett-1973]: Dummett, Michael A.E., 1973, “The Justification of Deduction”, British Academy, London. Page references to reprint in Dummett 1978: 290–318. [[Dummett 1973 available online](https://www.britac.ac.uk/pubs/proc/files/59p201.pdf)]

[^dummett-1978]: –––, 1978, *Truth and Other Enigmas*, Cambridge MA: Harvard University Press.

[^dummett-2000]: –––, 2000, *Elements of Intuitionism*, second revised edition, Oxford: Clarendon Press.

[^ewald-1996]: Ewald, William Bragg, 1996, *From Kant to Hilbert: A Source Book in the Foundations of Mathematics*, 2 vols, Oxford: Oxford University Press.

[^fitting-1969]: Fitting, Melvin Chris, 1969, *Intuitionistic Logic, Model Theory and Forcing*, (Studies in Logic and the Foundations of Mathematics, 54), Amsterdam: North-Holland.

[^fraenkel-1973]: Fraenkel, Abraham A., Yehoshua Bar-Hillel, and Azriel Levy, 1973, *Foundations of Set Theory*, second revised edition, (Studies in Logic and the Foundations of Mathematics, 67), Amsterdam: North-Holland. The revision of the chapter on intuitionism (4) was done by Dirk van Dalen.

[^franchella-1994a]: Franchella, Miriam, 1994a, “Heyting’s contribution to the change in research into the foundations of mathematics”, *History and Philosophy of Logic*, 15(2): 149–172. doi:10.1080/01445349408837229

[^franchella-1994b]: –––, 1994b, “Brouwer and Griss on intuitionistic negation”, *Modern Logic*, 4(3): 256–265. [[Franchella 1994b available online](https://projecteuclid.org/euclid.rml/1204835277)]

[^franchella-1995]: –––, 1995, “L.E.J. Brouwer towards intuitionistic logic”, *Historia Mathematica*, 22(3): 304–322. doi:10.1006/hmat.1995.1026

[^franchella-2008]: –––, 2008, *Con gli occhi negli occhi di Brouwer*, Monza: Polimetrica.

[^freudenthal-1937a]: Freudenthal, Hans, 1937a, “Zum intuitionistischen Raumbegriff”, *Compositio Mathematica*, 4: 82–111. [[Freudenthal 1937a available online](http://www.numdam.org/item?id=CM_1937__4__82_0)]

[^freudenthal-1937b]: –––, 1937b, “Zur intuitionistischen Deutung logischer Formeln”, *Compositio Mathematica*, 4: 112–116. [[Freudenthal 1937b available online](http://www.numdam.org/item?id=CM_1937__4__112_0)]

[^freudenthal-1937c]: –––, 1937c, “Nachwort”, *Compositio Mathematica*, 4: 118. [[Freudenthal 1937c available online](http://www.numdam.org/item?id=CM_1937__4__117_0)]

[^freudenthal-1973]: –––, 1973, *Mathematics as an Educational Task*, Dordrecht:Reidel.

[^gentzen-1934]: Gentzen, Gerhard, 1934, “Untersuchungen über das logische Schliessen”, *Mathematische Zeitschrift*, 39: 176–210, 405–431. English translation in Gentzen 1969: 68–131. doi:10.1007/BF01201353

[^gentzen-1969]: –––, 1969, *The Collected Papers of Gerhard Gentzen*, M.E. Szabo (ed. and trans.), Amsterdam: North-Holland.

[^georgacarakos-1982]: Georgacarakos, G.N., 1982, “The Semantics of Minimal Intuitionism”, *Logique et Analyse*, 25(100): 383–397. [[Georgacarakos 1982 available online](http://virthost.vub.ac.be/lnaweb/ojs/index.php/LogiqueEtAnalyse/article/view/959)]

[^gilmore-1953a]: Gilmore, P.C., 1953a, “The effect of Griss’ criticism of the intuitionistic logic on deductive theories formalized within the intuitionistic logic. I”, *Proceedings Koninklijke Nederlandse Akademie van Wetenschappen Amsterdam*, 56: 162–174. Also *Indagationes Mathematicae*, 15: 162–174. doi:10.1016/S1385-7258(53)50022-8

[^gilmore-1953b]: –––, 1953b, “The effect of Griss’ criticism of the intuitionistic logic on deductive theories formalized within the intuitionistic logic. II”, *Proceedings Koninklijke Nederlandse Akademie van Wetenschappen Amsterdam*, 56: 175–186. Also *Indagationes Mathematicae*, 15: 175–186. doi:10.1016/S1385-7258(53)50023-X

[^gilmore-1953c]: –––, 1953c, “Griss’ criticism of the intuitionistic logic and the theory of order”, *Proceedings of the 11th International Congress of Philosophy, Brussels 1953*, Amsterdam: North-Holland, 5: 98–104.

[^gilmore-1956]: –––, 1956, “Mathématique stable et Mathématique affirmative, by D. van Dantzig”, *Journal of Symbolic Logic*, 21(3): 323–324. doi:10.2307/2269134

[^glivenko-1928]: Glivenko, V., 1928, “Sur la logique de M. Brouwer”, *Académie Royale de Belgique, Bulletin de la classe des sciences*, 14: 225–228.

[^glivenko-1929]: –––, 1929, “Sur quelques points de la logique de M. Brouwer”, *Académie Royale de Belgique, Bulletin de la classe des sciences*, 5(15): 183–188. English translation in Mancosu 1998: 301–305.

[^gödel-1932]: Gödel, Kurt, 1932, “Zum intuitionistischen Aussagenkalkül”, *Anzeiger der Akademie der Wissenschaften in Wien*, 69: 65–66. Also, with English translation, in Gödel 1986: 222–225.

[^gödel-1986]: –––, 1932f, “Heyting, Arend: Die intuitionistische Grundlegung der Mathematik”, *Zentralblatt für Mathematik und ihre Grenzgebiete*, 2: 321–322. Also, with English translation, in Gödel 1986: 246–247.

[^gödel-1933e]: –––, 1933e, “Zur intuitionistischen Arithmetik und Zahlentheorie”, *Ergebnisse eines mathematischen Kolloquiums*, 4: 34–38. Also, with English translation, in Gödel 1986: 286–295.

[^gödel-1986-2]: –––, 1933f, “Eine Interpretation des intuitionistischen Aussagenkalküls”, *Ergebnisse eines mathematischen Kolloquiums*, 4: 39–40. Also, with English translation, in Gödel 1986: 300–303.

[^gödel-1995]: –––, \*1933o, “The present situation in the foundations of mathematics”, text of a lecture in Cambridge, MA, in Gödel 1995: 45–53.

[^gödel-1941]: –––, \*1941, “In what sense is intuitionistic logic constructive?”, text of a lecture at Yale, in Gödel 1995: 189–200.

[^gödel-1958]: –––, 1958, “Über eine bisher noch nicht benutzte Erweiterung des finiten Standpunktes”, *Dialectica*, 12(3–4): 280–287. Also, with English translation, in Gödel 1990: 240–251. doi:10.1111/j.1746-8361.1958.tb01464.x

[^gödel-1970]: –––, 1970, “On an extension of finitary mathematics which has not yet been used”, Circulated earlier version of Gödel 1972.

[^gödel-1972]: –––, 1972, “On an extension of finitary mathematics which has not yet been used”, Revised and expanded translation of Gödel 1958, first published in Gödel 1990: 271–280.

[^gödel-1986-3]: –––, 1986–, *Collected Works*, Solomon Feferman et al. (eds.), Oxford: Oxford University Press.

[^gödel-1986-4]: –––, 1986, *I: Publications 1929–1936*

[^gödel-1990]: –––, 1990, *II: Publications 1938–1974*

[^gödel-1995-2]: –––, 1995, *III: Unpublished Essays and Lectures*

[^gödel-2003a]: –––, 2003a, *IV: Correspondence A–G*

[^gödel-2003b]: –––, 2003b, *V: Correspondence H–Z*

[^griss-1944]: Griss, G.F.C., 1944, “Negatieloze intuitïonistische wiskunde”, *Verslagen Nederlandse Akademie van Wetenschappen Amsterdam*, 53: 261–268.

[^griss-1946]: –––, 1946, “Negationless intuitionistic mathematics”, *Proceedings Koninklijke Nederlandse Akademie van Wetenschappen Amsterdam*, 49: 1127–1133. Also *Indagationes Mathematicae*, 8: 675–681.

[^griss-1947]: –––, 1947, *Idealistische Filosofie*, Arnhem: Van Loghum Slaterus.

[^griss-1948a]: –––, 1948a, “Sur la négation (dans les mathématiques et la logique)”, *Synthese*, 7(1/2): 71–74.

[^griss-1948b]: –––, 1948b, “Logique des mathématiques intuitionistes sans négation”, *Comptes Rendus de l’Académie des sciences*, 227: 946–948. [[Griss 1948b available online](https://gallica.bnf.fr/ark:/12148/bpt6k3179j/f938)]

[^griss-1950]: –––, 1950, “Negationless intuitionistic mathematics. II”, *Proceedings Koninklijke Nederlandse Akademie van Wetenschappen Amsterdam*, 53: 456–463. Also *Indagationes Mathematicae*, 12: 108–115.

[^griss-1951a]: –––, 1951a, “Negationless Intuitionistic Mathematics. III”, *Proceedings Koninklijke Nederlandse Akademie van Wetenschappen Amsterdam*, 54: 193–199. Also *Indagationes Mathematicae*, 13: 193–199. doi:10.1016/S1385-7258(51)50027-6

[^griss-1951b]: –––, 1951b, “Negationless Intuitionistic Mathematics. IVa”, *Proceedings Koninklijke Nederlandse Akademie van Wetenschappen Amsterdam*, 54: 452–462. Also *Indagationes Mathematicae*, 13: 452–462. doi:10.1016/S1385-7258(51)50064-1

[^griss-1951c]: –––, 1951c, “Negationless Intuitionistic Mathematics. IVb”, *Proceedings Koninklijke Nederlandse Akademie van Wetenschappen Amsterdam*, 54: 463–471. Also *Indagationes Mathematicae*, 13: 463–471. doi:10.1016/S1385-7258(51)50065-3

[^griss-1951d]: –––, 1951d, “Logic of Negationless Intuitionistic Mathematics”, *Proceedings Koninklijke Nederlandse Akademie van Wetenschappen Amsterdam*, 54: 41–49. Also *Indagationes Mathematicae*, 13: 41–49. doi:10.1016/S1385-7258(51)50007-0

[^heijenoort-1967]: van Heijenoort, Jean (ed.), 1967, *From Frege to Gödel: A Sourcebook in Mathematical Logic, 1879–1931*, Cambridge, MA: Harvard University Press.

[^hazen-1995]: Hazen, A.P., 1995, “Is Even Minimal Negation Constructive?”, *Analysis*, 55(2): 105–107. doi:10.1093/analys/55.2.105

[^herbrand-1931]: Herbrand, Jacques, 1931, “Sur la non-contradiction de l’arithmétique”, *Journal für die reine und angewandte Mathematik*, 166: 1–8. Also Herbrand 1968: 221–232. English translation in van Heijenoort 1967: 620–628, reprint in Herbrand 1971: 284–297.

[^herbrand-1968]: –––, 1968, *Écrits logiques*, Jean van Heijenoort (ed.), Paris: Presses Unversitaires de France.

[^herbrand-1971]: –––, 1971, *Logical Writings*, Warren D. Goldfarb (ed.), Cambridge, MA: Harvard University Press.

[^hesseling-2003]: Hesseling, Dennis E., 2003, *Gnomes in the Fog. The Reception of Brouwer’s Intuitionism in the 1920s*, Basel: Birkhäuser.

[^heyting-1925]: Heyting, Arend, 1925, *Intuïtionistische axiomatiek der projectieve meetkunde*, Ph.D. thesis, Universiteit van Amsterdam.

[^heyting-1928]: –––, 1928, [Prize essay on the formalization of intuitionistic logic]. Expanded and revised version published as Heyting 1930, Heyting 1930A, Heyting 1930B.

[^heyting-1930]: –––, 1930, “Die formalen Regeln der intuitionistischen Logik I”, *Sitzungsberichte der Preussischen Akademie der Wissenschaften*, 42–56. English translation in Mancosu 1998: 311–327.

[^heyting-1930a]: –––, 1930A, “Die formalen Regeln der intuitionistischen Logik II”, *Sitzungsberichte der Preussischen Akademie der Wissenschaften*, 57–71.

[^heyting-1930b]: –––, 1930B, “Die formalen Regeln der intuitionistischen Logik III”, *Sitzungsberichte der Preussischen Akademie der Wissenschaften*, 158–169.

[^heyting-1930c]: –––, 1930C, “Sur la logique intuitionniste”, *Académie Royale de Belgique, Bulletin de la Classe des Sciences*, 16: 957–963. English translation in Mancosu 1998: 306–310.

[^heyting-1931]: –––, 1931, “Die intuitionistische Grundlegung der Mathematik” (The Intuitionist Foundations of Mathematics), *Erkenntnis*, 2: 106–115. English translation in Benacerraf & Putnam 1983: 52–61. doi:10.1017/CBO9781139171519.003 and doi:10.1007/BF02028143

[^heyting-1932]: –––, 1932, “A propos d’un article de MM. Barzin et Errera”, *Enseignement Mathématique*, 31: 121–122.

[^heyting-1932c]: –––, 1932C, “Anwendung der intuitionistischen Logik auf die Definition der Vollständigkeit eines Kalküls”, in *Verhandlungen des Internationalen Mathematikerkongresses Zürich 1932*, W. Saxer (ed.), Zürich: Orell Füssli, vol. 2, 344–345.

[^heyting-1934]: –––, 1934, *Mathematische Grundlagenforschung, Intuitionismus, Beweistheorie*, Berlin: Springer.

[^heyting-1937]: –––, 1937, “Bemerkungen zu dem Aufsatz von Herrn Freudenthal ‘Zur intuitionistischen Deutung logischer Formeln’”, *Compositio Mathematica*, 4: 117–118. [[Heyting 1937c available online](http://www.numdam.org/item?id=CM_1937__4__117_0)]

[^heyting-1955]: –––, 1955, *Les fondements des mathématiques. Intuitionnisme. Théorie de la démonstration*, Paris: Gauthier-Villars. Updated version of Heyting 1934, translated into French by P. Destouches-Février.

[^heyting-1953]: –––, 1953–1955, “G. F. C. Griss and His Negationless Intuitionistic Mathematics” *Synthese*, 9: 91–96. doi:10.1007/BF00567395

[^heyting-1956]: –––, 1956, *Intuitionism, an Introduction*, Amsterdam: North–Holland.

[^heyting-1958a]: –––, 1958A, “Blick von der intuitionistischen Warte”, *Dialectica*, 12(3–4): 332–345. doi:10.1111/j.1746-8361.1958.tb01468.x

[^heyting-1958c]: –––, 1958C, “Intuitionism in Mathematics”, in *La philosophie au milieu du vingtième siècle*, Raymond Klibansky (ed.), Firenze: La nuova Italia, vol. 1, 101–115.

[^heyting-1968a]: –––, 1968A, “L.E.J. Brouwer”, in *Logic and Foundations of Mathematics*, (Contemporary Philosophy. A Survey, Vol.1), Raymond Klibansky (ed.), Firenze: La Nuova Italia editrice, 308–315.

[^heyting-1974]: –––, 1974, “Intuitionistic views on the nature of mathematics”, *Synthese*, 27(1–2): 79–91. doi:10.1007/BF00660890

[^heyting-1978]: –––, 1978, “History of the Foundations of Mathematics”, *Nieuw Archief voor Wiskunde*, 3rd series, 26(3): 1–21.

[^hilbert-1900]: Hilbert, David, 1900, “Mathematische Probleme. Vortrag, gehalten auf dem internationalen Mathematiker-Kongress zu Paris 1900” (Mathematical Problems), *Archiv der Mathematik und Physik (3)*, 1: 44–63,213–237. English translation in the *Bulletin of the American Mathematical Society*, 8(10): 437–479, 1902. doi:10.1090/S0002-9904-1902-00923-3

[^hilbert-1922]: –––, 1922, “Neubegründung der Mathematik (Erste Mitteilung)”, *Abhandlungen aus dem Mathematischen Seminar der Hamburgischen Universität*, 1: 157–177. English translation in Mancosu 1998: 198–214.

[^hilbert-1923]: –––, 1923, “Die logischen Grundlagen der Mathematik”, *Mathematische Annalen*, 88(1–2): 151–165. English translation in Ewald 1996: 1134–1148. doi:10.1007/BF01448445

[^hilbert-1928]: Hilbert, D. and W. Ackermann, 1928, *Grundzüge der theoretischen Logik*, Berlin: Springer. doi:10.1007/978-3-642-52789-0

[^imai-1966]: Imai, Yasuyuki and Kiyoshi Iseki, 1966, “On Griss Algebra. I”, *Proceedings of the Japan Academy*, 42(3): 213–216. doi:10.3792/pja/1195522077

[^iongh-1949]: de Iongh, J.J., 1949, “Restricted Forms of Intuitionistic Mathematics”, *Proceedings of the 10th International Congress of Philosophy, Amsterdam 1948*, Amsterdam: North-Holland, 2: 744–748. doi:10.5840/wcp1019492207

[^johansson-1937]: Johansson, Ingebrigt, 1937, “Der Minimalkalkül, ein reduzierter intuitionistischer Formalismus”, *Compositio Mathematica*, 4: 119–136. [[Johansson 1937 available online](http://www.numdam.org/item?id=CM_1937__4__119_0)]

[^joosten-2004]: Joosten, Joost Johannes, 2004, *Interpretability Formalized*, Ph.D. thesis, Utrecht University. Quaestiones Infinitae vol. XLIX, [[Joosten 2004 available from Universiteit Utrecht/Universiteitsbibliotheek](http://www.joostjjoosten.nl/papers/setup.pdf)].

[^kennedy-2007]: Kennedy, Juliette, 2007, “Kurt Gödel”, in *The Stanford Encyclopedia of Philosophy*, Winter 2007 Edition, Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/win2007/entries/goedel/](https://plato.stanford.edu/archives/win2007/entries/goedel/)>.

[^kleene-1945]: Kleene, Stephen Cole, 1945, “On the Interpretation of Intuitionistic Number Theory”, *Journal of Symbolic Logic*, 10(4): 109–124. doi:10.2307/2269016

[^kleene-1952]: –––, 1952, *Introduction to Metamathematics*, Amsterdam: North-Holland.

[^kleene-1973]: –––, 1973, “Realisability: A Retrospective Survey”, in Mathias & Rodgers 1973: 95–112. doi:10.1007/BFb0066772

[^kleene-1965]: Kleene, Stephen Cole and Richard Eugene Vesley, 1965, *The Foundations of Intuitionistic Mathematics, Especially in Relation to Recursive Functions*, (Studies in logic and the foundations of mathematics, 39), Amsterdam: North-Holland.

[^kolmogorov-1925]: Kolmogorov, A., 1925, “O principe tertium non datur”, *Matematiceskij Sbornik*, 32: 646–667. English translation in van Heijenoort 1967: 416–437.

[^kolmogorov-1932]: –––, 1932, “Zur Deutung der Intuitionistischen Logik”, *Mathematische Zeitschrift*, 35: 58–65. English translation in Mancosu 1998: 328–334. doi:10.1007/BF01186549

[^kolmogorov-1937]: –––, 1937, “Freudenthal, Hans: Zur intuitionistischen Deutung logischer Formeln. Heyting, A.: Bemerkungen zu dem Aufsatz von Herrn Freudenthal ‘Zur intuitionistischen Deutung logischer Formeln’”, *Zentralblatt für Mathematik und ihre Grenzgebiete*, 0015.24201.

[^korevaar-2016]: Korevaar, Jaap., 2016, “Enkele persoonlijke herinneringen aan L.E.J. Brouwer”, (“Some personal memories of L.E.J. Brouwer”), *Nieuw Archief voor Wiskunde*, 5th series, 17(4): 247–249. [[Korevaar 2016 available online](http://www.nieuwarchief.nl/serie5/pdf/naw5-2016-17-4-247.pdf)]

[^kreisel-1962]: Kreisel, G., 1962, “Foundations of Intuitionistic Logic”, in *Logic, Methodology and Philosophy of Science: Proceedings of the 1960 International Congress*, Ernst Nagel, Patrick Suppes, and Alfred Tarski (eds.), Stanford: Stanford University Press, 198–210. doi:10.1016/S0049-237X(09)70587-7

[^kreisel-1987]: –––, 1987, “Gödel’s Excursions into Intuitionistic Logic”, in *Gödel Remembered*, P. Weingartner and L. Schmetterer (eds.), Napoli: Bibliopolis, 67–179.

[^kripke-1965]: Kripke, Saul A., 1965, “Semantical Analysis of Intuitionistic Logic I”, in *Formal Systems and Recursive Functions*, (Studies in Logic and the Foundations of Mathematics, 40), J.N. Crossley and M. Dummett (eds.), Amsterdam: North-Holland, 92–130. doi:10.1016/S0049-237X(08)71685-9

[^krivtsov-2000a]: Krivtsov, Victor N., 2000a, “A Negationless Interpretation of Intuitionistic Theories”, *Erkenntnis*, 53(1–2): 155–172. doi:10.1023/A:1005618302941

[^krivtsov-2000b]: –––, 2000b, “A Negationless Interpretation of Intuitionistic Theories. I”, *Studia Logica*, 64(3): 323–344. doi:10.1023/A:1005233526469

[^krivtsov-2000c]: –––, 2000c, “A Negationless Interpretation of Intuitionistic Theories. II”, *Studia Logica*, 65(2): 155–179. doi:10.1023/A:1005207512630

[^kuiper-2004]: Kuiper, Johannes John Carel, 2004, *Ideas and Explorations. Brouwer’s Road to Intuitionism*, Ph.D. thesis, Utrecht University. Quaestiones Infinitae vol. XLVI [[Kuiper 2004 available from Universiteit Utrecht/Universiteitsbibliotheek](https://dspace.library.uu.nl/handle/1874/90)].

[^lewis-1914]: Lewis, C.I., 1914, “The Calculus of Strict Implication”, *Mind*, New Series, 23(90): 240–247. doi:10.1093/mind/XXIII.1.240

[^mancosu-1998]: Mancosu, Paolo (ed.), 1998, *From Brouwer to Hilbert. The Debate on the Foundations of Mathematics in the 1920s*, Oxford: Oxford University Press.

[^mathias-1973]: Mathias, A.R.D. and H. Rodgers (eds.), 1973, *Cambridge Summer School in Mathematical Logic 1971*, (Lecture Notes in Mathematics, 337), Heidelberg: Springer. doi:10.1007/BFb0066770

[^mckinsey-1939]: McKinsey, J.C.C., 1939, “Proof of the Independence of the Primitive Symbols of Heyting’s Calculus of Propositions”, *Journal of Symbolic Logic*, 4(4): 155–158. doi:10.2307/2268715

[^mendez-1988]: Mendez, José M., 1988, “A Note on the Semantics of Minimal Intuitionism”, *Logique et Analyse*, 31(123–124): 371–377. [[Mendez 1988 available online](http://virthost.vub.ac.be/lnaweb/ojs/index.php/LogiqueEtAnalyse/article/view/1207)]

[^michel-2008]: Michel, David, 2008, *Systèmes formels et systèmes fonctionnels pédagogiques*, Ph.D. thesis, Université Metz. [[Michel 2008 available from Université de Lorraine](http://docnum.univ-lorraine.fr/public/UPV-M/Theses/2008/Michel.David.SMZ0824.pdf)].

[^mints-2006]: Mints, Grigori, 2006, “Notes on Constructive Negation”, *Synthese*, 148(3): 701–717. doi:10.1007/s11229-004-6294-3

[^molen-2016]: van der Molen, Tim, 2016, “The Johansson/Heyting letters and the birth of minimal logic”, *ILLC Publications, Technical Notes Series*, X-2016-04 [[van der Molen 2016 available online from ILLC](https://www.illc.uva.nl/Research/Publications/Reports/X-2016-04.text.pdf)].

[^moschovakis-2007]: Moschovakis, Joan, 2007, “Intuitionistic Logic”, in *The Stanford Encyclopedia of Philosophy*, Spring 2007 Edition, Edward N. Zalta (ed.), URL=<[https://plato.stanford.edu/archives/spr2007/entries/logic-intuitionistic/](https://plato.stanford.edu/archives/spr2007/entries/logic-intuitionistic/)>.

[^myhill-1966]: Myhill, John, 1966, “Notes Towards An Axiomatization of Intuitionistic Analysis”, *Logique et Analyse*, 9(35–36): 280–297. [[Myhill 1966 available online](http://virthost.vub.ac.be/lnaweb/ojs/index.php/LogiqueEtAnalyse/article/view/316)]

[^nelson-1966]: Nelson, David, 1966, “Non-Null Implication”, *Journal of Symbolic Logic*, 31(4): 562–572. doi:10.2307/2269691

[^parsons-1967]: Parsons, Charles, 1967, [Introduction to the translation of sections 1–3 of Brouwer 1927B], in van Heijenoort 1967: 446–457.

[^pieri-1898]: Pieri, Mario, 1898, “I principii della geometria di posizione composti in sistema logico deduttivo”, *Memorie della Reale Accademia delle Scienze di Torino, series II*, 48: 1–62.

[^plisko-1988]: Plisko, V.E., 1988, “The Kolmogorov calculus as a part of minimal calculus”, *Russian Mathematical Surveys*, 43(6): 95–110. doi:10.1070/RM1988v043n06ABEH001993

[^pos-1953]: Pos, H.J., 1953–1954, “G.F.C. Griss als wijsgerig humanist en als mens”, *De Nieuwe Stem*, 8: 654–663.

[^posy-1992]: Posy, Carl J., 1992, “Review: Dirk van Dalen, *Intuitionistic Logic*; Walter Felscher, *Dialogues as a Foundation for Intuitionistic Logic*”, *Journal of Symbolic Logic*, 57(2): 754–756. doi:10.2307/2275309

[^prawitz-1965]: Prawitz, Dag, 1965, *Natural Deduction. A Proof-Theoretical Study*, Stockholm: Almqvist & Wiksell.

[^prawitz-1968]: Prawitz, D. and P.-E. Malmnäs, 1968, “A Survey of Some Connections Between Classical, Intuitionistic and Minimal Logic”, in *Contributions to Mathematical Logic*, (Studies in Logic and the Foundations of Mathematics, 50), H. Arnold Schmidt, K. Schütte, and H.-J. Thiele (eds.), Amsterdam: North-Holland, pp. 215–229. doi:10.1016/S0049-237X(08)70527-5

[^rasiowa-1974]: Rasiowa, Helena, 1974, *An Algebraic Approach to Non-Classical Logics*, (Studies in logic and the foundations of mathematics, 78), Amsterdam: North-Holland/

[^ruitenburg-1991]: Ruitenburg, Wim, 1991, “The Unintended Interpretations of Intuitionistic Logic”, in *Perspectives on the History of Mathematical Logic*, Thomas Drucker (ed.), Basel: Birkhäuser, 134–160. doi:10.1007/978-0-8176-4769-8_10

[^rootselaar-1953]: van Rootselaar, B., 1953–1954, “In memoriam Dr. G.F.C. Griss”, *Euclides*, 29(1): 42–45.

[^russell-1903]: Russell, Bertrand, 1903, *The Principles of Mathematics*, London: Allen & Unwin.

[^sato-1997]: Sato, Masahiko, 1997, “Classical Brouwer-Heyting-Kolmogorov interpretation”, *RIMS Kokyuroku*, 1021: 28–47.

[^smirnov-1925]: Smirnov, V.J., 1925 [published 1932], “Kolmogorov, A.N.: Über das Prinzip tertium non datur”, *Jahrbuch über die Fortschritte der Mathematik* 51.0048.01.

[^stigt-1990]: van Stigt, Walter P., 1990, *Brouwer’s Intuitionism*, (Studies in the history and philosophy of mathematics, 2), Amsterdam: North-Holland.

[^stone-1937]: Stone, Marshall Harvey, 1937, “Topological Representations of Distributive Lattices and Brouwerian Logics”, *Časopis pro pěstování matematiky a fysiky*, 67(1): 1–25.

[^sundholm-1983]: Sundholm, Göran, 1983, “Constructions, Proofs and the Meaning of Logical Constants”, *Journal of Philosophical Logic*, 12(2): 151–172. doi:10.1007/BF00247187

[^sundholm-2004]: –––, 2004, “The Proof-Explanation of Logical Constants is Logically Neutral”, *Revue Internationale de Philosophie*, 58(4): 401–410.

[^sundholm-2008]: Sundholm, Göran and Mark van Atten, 2008, “The proper explanation of intuitionistic logic: on Brouwer’s proof of the Bar Theorem”, in van Atten et al. 2008: 60–77. doi:10.1007/978-3-7643-8653-5_5

[^swart-1976]: de Swart, H.C.M., 1976, “Another Intuitionistic Completeness Proof”, *Journal of Symbolic Logic*, 41(3): 644–662. doi:10.1017/S0022481200051215

[^swart-1977]: –––, 1977, “An Intuitionistically Plausible Interpretation of Intuitionistic Logic”, *Journal of Symbolic Logic*, 42(4): 564–578. doi:10.2307/2271877

[^tarski-1938]: Tarski, Alfred, 1938, “Der Aussagenkalkül und die Topologie”, *Fundamentae Mathematicae*, 31: 103–134. English translation in Tarski 1956, pp. 421–454.

[^tarski-1953]: –––, 1953, “A General Method in Proofs of Undecidability”, in *Undecidable Theories*, A. Tarski, A. Mostowski, and R. Robinson (eds.), Amsterdam: North-Holland, 3–35.

[^tarski-1956]: –––, 1956, *Logic, Semantics, Metamathematics. Papers from 1923 to 1938*, J.H. Woodger (trl.), Clarendon Press.

[^troelstra-1977]: Troelstra, A.S., 1977, “Aspects of constructive mathematics”, in *Handbook of Mathematical Logic*, (Studies in Logic and the Foundations of Mathematics, 90), Jon Barwise (ed.), Amsterdam: North-Holland, 973–1052. doi:10.1016/S0049-237X(08)71127-3

[^troelstra-1983]: –––, 1983, “Logic in the Writings of Brouwer and Heyting”, in *Atti del Convegne Internazionaledi Storia della Logica. San Gimignano, 4–8 dicembre 1982*, V. Abrusci, E. Casari, and M. Mugnai, eds., Bologna: CLUEB, 193–210.

[^troelstra-1990]: –––, 1990, “On the Early History of Intuitionistic Logic”, in *Mathematical Logic*, Petio P. Petkov (ed.), New York: Plenum Press, 3–17.

[^troelstra-1981]: Troelstra, A.S., J. Niekus, and H. van Riemsdijk, 1981, “Bibliography of A. Heyting”, *Nieuw Archief voor Wiskunde*, 3rd series, 29: 24–35.

[^troelstra-1988]: Troelstra, A.S. and D. van Dalen, 1988, *Constructivism in Mathematics*, 2 vols., (Studies in Logic and the Foundations of Mathematics, 121 & 123), Amsterdam: North-Holland.

[^valpola-1955]: Valpola, Veli, 1955, “Ein system der negationlosen Logik mit ausschliesslich realisierbaren Prädicaten”, *Acta Philosophica Fennica*, 9: 1–247.

[^veldman-1976]: Veldman, Wim, 1976, “An Intuitionstic Completeness Theorem for Intuitionistic Predicate Logic”, *Journal of Symbolic Logic*, 41(1): 159–166. doi:10.1017/S0022481200051859

[^veldman-1982]: –––, 1982, “On the Continuity of Functions in Intuitionistic Real Analysis. Some Remarks on Brouwer’s Paper: ‘Ueber Definitionsbereiche von Funktionen’”, Tech. Rep. 8210, Mathematisch Instituut, Katholieke Universiteit Nijmegen.

[^veldman-2008]: –––, 2008, “The Borel Hierarchy Theorem from Brouwer’s Intuitionistic Perspective”, *Journal of Symbolic Logic*, 73(1): 1–64. doi:10.2178/jsl/1208358742

[^vesley-1980]: Vesley, Richard, 1980, “Intuitionistic Analysis: the Search for Axiomatization and Understanding”, in *The Kleene Symposium*, (Studies in Logic and the Foundations of Mathematics, 101), J. Barwise, H. J. Keisler, and K. Kunen (eds.), Amsterdam: North-Holland, 317–331. doi:10.1016/S0049-237X(08)71265-5

[^vredenduin-1953]: Vredenduin, P.G.J., 1953, “The Logic of Negationless Mathematics”, *Compositio Mathematica*, 11: 204–277. [[Vredenduin 1953 available online](http://www.numdam.org/item?id=CM_1953__11__204_0)]

[^vredenduin-1956]: –––, 1956, “G.F.C. Griss and his Negationaless Intuitionistic Mathematics, by A. Heyting”, *Journal of Symbolic Logic*, 21(1): 91. doi:10.2307/2268511

[^wajsberg-1938]: Wajsberg, Mordchaj, 1938, “Untersuchungen über den Aussagenkalkül [von A. Heyting]”, *Wiadomosci Matematyczne*, (old series) 46: 45–101.

[^wang-1987]: Wang, Hao, 1987, *Reflections on Kurt Gödel*, Cambridge MA: MIT Press.

[^wavre-1924]: Wavre, Rolin, 1924, “Y a-t-il une crise des mathématiques? A propos de la notion d’existence et d’une application suspecte du principe du tiers exclu”, *Revue de Métaphysique et de Morale*, 31(3) 435–470.

[^wavre-1926]: –––, 1926, “Logique formelle et logique empirique”, *Revue de Métaphysique et de Morale*, 33(1): 65–75.

[^weyl-1921]: Weyl, Hermann, 1921, “Über die neue Grundlagenkrise der Mathematik”, *Mathematische Zeitschrift*, 10(1–2): 39–79. English translation in Mancosu 1998: 86–118. doi:10.1007/BF02102305

[^whitehead-1906]: Whitehead, Alfred North, 1906, *The Axioms of Projective Geometry*, Cambridge: Cambridge University Press.

[^whitehead-1910]: Whitehead, Alfred North and Bertrand Russell, 1910, *Principia Mathematica*, vol. 1, Cambridge: Cambridge University Press.
