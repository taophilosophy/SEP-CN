# intuitionistic-logic-development — objections（supplement）

> （《intuitionistic-logic-development》词条补充材料，源：plato.stanford.edu/entries/intuitionistic-logic-development/objections.html）

#### Supplement to The Development of Intuitionistic Logic

## Objections to the Proof Interpretation

As the Proof Interpretation became known, through personal exchanges and in print, a number of objections were made to it:

1. Its explanation of implication is not strict enough (Johansson)
2. Its explanation of implication depends on hypothetical constructions, which are not in intuition (Freudenthal, Griss)
3. Its explanation of implication is circular (Gentzen)
4. Its explanation of implication is impredicative (Gödel, Kuroda, Kreisel)

These criticisms also targeted the universal quantifier and negation, which are both closely related to implication. Whether the criticisms are justified or not, they inspired important innovations:

1. Normalization for first-order intuitionistic predicate logic (Gentzen)
2. Minimal logic (Johansson)
3. Functional interpretations (Gödel)
4. Negationless mathematics (Griss)

Thematically, the objections of Johansson, Freudenthal, and Griss are closely related, as are those of Gentzen and Gödel, Kuroda, and Kreisel. In a discussion of the Proof Interpretation as a codification of Brouwer’s explanation of logic, the former three are potentially the strongest ones as they were formulated from a point of view that was either avowedly intuitionistic (Freudenthal, Griss), or close enough to be interpreted that way (Johansson). That was less the case for Gentzen, and certainly less for Gödel; on the other hand, their objections have had a much wider influence, corresponding to the fact that intuitionism has remained a minority view. For the moment, we will discuss the first group.

- 1. Implication is Not Strict Enough (Johansson 1935–1937)
- 2. Hypothetical Constructions Are Not in Intuition (Freudenthal 1937, Griss 1941–1951)
- 2.1 Freudenthal 1937
- 2.2 Griss 1941–1951

### 1. Implication is Not Strict Enough (Johansson 1935–1937)

As mentioned in section 4.4 above, Heyting’s axiomatization of implication was soon questioned by Johansson. Ingebrigt Johansson (1904–1987) was a Norwegian mathematician working mostly in geometry and topology. He had found a reference to Heyting’s “Die formalen Regeln” (Heyting 1930) by accident.[^note-35] “Having studied it carefully, I have become able to understand works by Brouwer to some extent; before, that was impossible for me” (Johansson to Heyting, August 29, 1935; translation mine). His concern over the acceptability of *Ex Falso* (Heyting’s Axiom 10) led to a short correspondence from later 1935 to early 1936,[^note-36] and resulted in the publication of “Der Minimalkalkül, ein reduzierter intuitionistischer Formalismus” (Johansson 1937) in Brouwer’s journal *Compositio Mathematica*. Here I will only discuss Johansson’s direct criticism of the Proof Interpretation; evidently, this does not do much justice to his ideas that allowed him not only to criticize the Proof Interpretation but to turn that criticism into the positive development of Minimal Logic.

Johansson announces his disapproval of the inclusion of *Ex Falso* in the opening letter but first formulates a precise criticism in his second:

> I have not been able to make my peace with Axiom 4.1. You say that when $a \rightarrow b$ has been proved, and later $\neg a$ is proved, then $a \rightarrow b$ should *remain* correct. Indeed; but $\vdash \neg a \rightarrow \cdot a \rightarrow b$ means that when $\neg a$ has been proved, $b$ at once *becomes* derivable from $a$, even when this had not been proved before. And that contradicts my intuition in the most violent way. (Johansson to Heyting, September 23, 1935; translation mine)

And later that year:

> My being unwilling to accept 4.1 is in the end simply based on the circumstance that I prefer to work with a more *strict* implication. My Minimal Logic shows, however, that a more strict implication really is possible. (November 15, 1935; translation mine):

(The phrase “strict implication” is a reference to Lewis 1914, which Johansson will cite in his article of 1937.)

In a note for his reply (and presumably also in the letter actually sent) Heyting explained:

> I interpret $a \rightarrow b$ as “to reduce the solution of $b$ to that of $a$, or to show the impossibility of solving $a$”. This interpretation is appropriate. (Note by Heyting to Johansson’s letter of September 23, 1935; translation mine)[^note-37]

This of course is Kolmogorov’s interpretation of 1932 (see section 5.3 above).

In 1955, in the French translation of his book *Grundlagenforschung* of 1934, Heyting adds a note saying that Johansson’s interpretation of the implication is different from his own (Heyting 1955: 19). But the discussion seems to have had an effect on Heyting. The second thoughts that Heyting seems to have developed about Kolmogorov’s interpretation as applied to *Ex Falso* are probably related to Johansson’s insistence that $\neg a \rightarrow \cdot a \rightarrow b$ can only be accepted if a construction can be indicated that, on the assumption that $\neg a$ has been proved, transforms proofs of $a$ into proofs of $b$. For in the justification of *Ex Falso* that Heyting went on to give in his book of 1956, *Intuitionism. An introduction*, he tried to make the case that there indeed is a construction that will do just that; see the discussion in section 5.4 above.

Formalized intuitionistic logic with *Ex Falso* is interpretable in Minimal Logic (Prawitz & Malmnäs 1968: 219, 221, 224–225). In this translation, $\bot$ is replaced by an arbitrary proposition letter that does not occur in the original proof. From a contentual point of view, the problem of finding an acceptable meaning for the formulas containing that proposition letter would of course remain.

However, for the specific systems of formalized primitive recursive arithmetic (PRA) and Heyting Arithmetic (HA) there is a result that is more satisfying from the contentual point of view. Defining $\bot$ as $0=1$ enables one formally to derive $\bot \rightarrow A$ for any $A$ in the language of the system. The demonstration of this fact (Troelstra & van Dalen 1988: 126–127) does not depend on knowing that there is no proof of $0=1$, and the demonstration makes it easy to see how in these systems from a formal proof of $0=1$ one would obtain a formal proof of any given $A$.

For a discussion of other logical aspects of the Heyting-Johansson correspondence, see van der Molen 2016. On negation in Minimal Logic, see Hazen 1995. Relations between the logic of Kolmogorov 1925 and Minimal Logic are discussed in Plisko 1988. Proof-theoretical aspects of Minimal Logic are treated in Prawitz 1965 and Prawitz & Malmnäs 1968; model-theory in Fitting 1969: 40, Georgacarakos 1982, and Mendez 1988; an algebraic approach in Rasiowa 1974: chapter 11. Weakenings of Minimal Logic are the subject of Colacito, de Jongh, & Vargas 2017.

### 2. Hypothetical Constructions Are Not in Intuition (Freudenthal 1937, Griss 1941–1951)

To have a genuine implication (and hence also a genuine universal quantification) it must be possible to make hypotheses; that this is possible in intuitionism was contested by the intuitionists Freudenthal and Griss, presumably independently. They did not comment directly on the passage in Brouwer’s dissertation discussed above in section section 2.2, in which Brouwer argues that arguments that seem to involve hypothetical constructions in reality do not. Both Freudenthal and Griss must have known that argument. Conversely, although Brouwer did react in print to both (see below), this regrettably did not include an explicit philosophical engagement with their views. He did express himself at a meeting of the Dutch Mathematical Society at the Krasnapolsky Hotel in Amsterdam in 1947, as remembered by Korevaar:

> That day G.F.C. Griss (mathematics teacher in Gouda) spoke about what he called his negationless mathematics. That was even more strict than Brouwer’s intuitionism. […] Afterwards there was an extended discussion at the blackboard. First between Griss and, among others, van Dantzig, who evoked his affirmative mathematics. I think that Freudenthal was there, too. Then it was Heyting’s turn; he tried to explain what Brouwer had meant. Finally, and unexpectedly, Brouwer himself appeared, from the back of the room; no one had noticed that he had arrived. Brouwer came forward running, his coat-tails flapping. And he cried: “You have all misunderstood!” (Korevaar 2016: 248; translation mine)

Unfortunately, no report seems to exist on the content of the discussion.

Two years later the Belgian philosopher S.I. Dockx hoped to organize a meeting on negationless logic with Brouwer, Griss, Freudenthal, Heyting, and van Dantzig. Brouwer made it clear, however, that he did not want to participate in an event together with Freudenthal (letter of Beth to Dockx of July 8, 1949, in van Dalen 2011: Online Supplement, 2446; for Brouwer’s conflict with Freudenthal see van Dalen 2005: 721–728, 753–757, and 794–799). In the end, a colloquium was indeed held in Brussels in 1949, with as speakers Beth, Destouches-Février, Feys, Freudenthal, Griss and van Dantzig (Chronique générale 1949: 435).[^note-38] As is the case for the meeting in Amsterdam in 1947, there seems to exist no report on the content of the discussions; and Heyting’s absence from the list of speakers is as yet unaccounted for.

#### 2.1 Freudenthal 1937

Hans Freudenthal (1905–1990) was an intellectually omnivorous German-Dutch mathematician, who took his PhD in Berlin in 1930 with a thesis in topology directed by Brouwer’s friends Hopf and Bieberbach. He came to know Brouwer when the latter lectured in Berlin in 1927, and made a favorable impression on him because of the good questions he asked (van Dalen 2005: 546). In 1930 he moved to Amsterdam to become one of Brouwer’s assistants and, from 1931, also lecturer. At the same time he continued his research in avant-garde topology. After the Second World War, Freudenthal became full professor in Utrecht, and mostly did important work in the history and didactics of mathematics. (In the preface to *Mathematics as an Educational Task* he wrote “My educational interpretation of mathematics betrays the influence of L.E.J. Brouwer’s view on mathematics (though not on education)”, Freudenthal 1973, ix.) He also edited the second volume of Brouwer’s *Collected Works*, which contains in particular the papers on topology (Brouwer 1977).

In 1937 Freudenthal formulated two objections to explanations of implication such as Heyting’s and Kolmogorov’s. One is that a hypothetical construction of the antecedent provides no actual construction material at all, so that, if the idea of a construction that proves $a \supset b$ is to make intuitionistic sense, this could only be done by giving a proof of $b$ *via* a proof of $a$. The second objection is that, moreover, the antecedent $a$ cannot even be given a definite meaning without thereby proving it; so that

> in the Heyting-Kolmogorov explanation the value of implication becomes illusory, as the hypothesis, in its quality as hypothesis, immediately eliminates itself. (Freudenthal 1937b: 115)

Freudenthal arrives at this point because of his view that, more generally, a proof is precisely what gives a statement its definite meaning:

> It lies close to hand to explain a statement as the establishing of a fact, of the obtaining of which one has convinced oneself by a *proof*, i.e., by bringing about the relation expressed in the statement. But this explanation can only be given cautiously, because once a statement is the establishing of a fact, there is no justification anymore of the separation of statement and proof. When I say, for example, that the sequence $a_{\nu}$ converges positively to $a$, this is only an abbreviated way of stating the fact that for every $n$ an $N$ can be determined such that $a-a_{\nu}$ ≤ 1/$n$ for *ν* ≥ $N$. That for every $n$ an $N$ with this property can be determined, is a statement that has intuitionistic sense only if one has a computation method that generates the $N$ from each $n$, a computation method that can roughly be represented by a formula into which $a_{\nu}$ and $a$ enter in some way. This example shows that each statement, once one formulates it in an intuitionistically unobjectionable way, automatically contains its full proof. (Freudenthal 1937b: 112; translation mine)

Behind the example Freudenthal gives here is the general intuitionistic idea that mathematical facts can only consist in the existence of constructions and proofs (which are themselves special constructions), so that spelling out a mathematical fact amounts to specifying the constructions that bring it about; but that is also, Freudenthal points out, what a proof is. Absent a proof, a statement has at most a heuristic or provisional meaning.

Negative statements are no exception according to Freudenthal, because their meaning is that all attempts at a construction with certain properties fail to achieve their aim, and a survey of these failings (which may depend on complete induction) constitutes the proof of the negative statement. Note that, as a consequence, meaning would not be compositional: The unnegated statement has no non-heuristic meaning of its own. This notion of heuristic meaning, which is the only kind of meaning an unnegated statement can have until the survey of attempts at constructions for it has been completed, must still be sufficiently precise if it is to serve as the basis of a mathematical proof of a negated statement. This goes in the direction of reading *β* of implications in section 2.2 above; perhaps the difference with Brouwer is not so great on this point.

Freudenthal accepts a special but important case of implication, the kind that is implicit in general statements such as “A total function on [0,1] is uniformly continuous”. In general statements

> the subject is the function, finitary set, number (as element of a set), understood in their wholly free growth. Neither specific nor all specific elements of a whole are meant, but *the* function, *the* finitary set, *the* element of a set, an individual therefore, albeit a peculiar individual, a true Proteus, very peculiar in this respect, that it may arrive that one is considering two different exemplars of this individual. (Freudenthal 1937b: 115; translation mine)

The assertion then is understood as of a relation between two predications of one specific subject, The example is then understood as the subject being *the* function and the predicates “being restricted in its free growth to being total on [0,1]” and “being restricted in its free growth to being uniformly continuous” (Freudenthal 1937b: 115).

Freudenthal acknowledges the alternative of reading it as asserting the containment of the species of total functions in the species of uniformly continuous ones, but finds a reading in terms of a freely growing object “intuitionistically more sympathetic” (Freudenthal 1937b: 116). He comments without further explanation that this is “so to speak a cataloguing of the species” (Freudenthal 1937b: 116). This remark in fact draws on his other publication in that issue of *Compositio Mathematica*, on intuitionistic topology. There he gives a definition of which the relevant part is this: [^note-39]

> A sequence of things $A_n (n=1,2,\ldots)$ is called *catalogued*, if to every $A_n$ is assigned the expression $\ne 0$ and to each $A_{\mu_1}A_{\mu_2} \ldots A_{\mu_k}$ the expression $= 0$ or $\ne 0$ (but never both expressions) (Freudenthal 1937a: 84; translation mine)

In a footnote, it is added that the sequence of things $A_n$ need not be lawlike, but may be growing in more or less freedom. Among the conditions on these assignments is specified that of extensibility:

> If $A_{\mu_1}A_{\mu_2}\ldots A_{\mu_{ k} } \ne 0$, an $m \ne \mu_1, \mu_2,\ldots,\mu_k$ can be indicated such that $A_{\mu_1}A_{\mu_2}\ldots A_{\mu_{ k} }A_{\mu_m} \ne 0$ (Freudenthal 1937a: 84; translation mine)

In these terms, the content of the example theorem, “A total function on [0,1] is uniformly continuous”, may be stated as follows. To a species one assigns the expression $\ne 0$ if a freely growing object can be restricted so as to have the corresponding property; and to a sequence of species the expression $\ne 0$ if a freely growing object can be restricted to have all the corresponding properties, and 0 if it cannot. Then a sequence of species $\ne 0$ containing the species of functions that are total on [0,1] may always be extended with the species of functions that are uniformly continuous.

That Freudenthal finds this reading “intuitionistically more sympathetic” is probably because it is more transparently related to the intuitionistic idea that, on the one hand, when we set out to construct an object we set out to construct an object of a certain type, and on the other hand that object will acquire properties in acts of construction over time. Freudenthal’s Protean individuals are rather suggestive of the later idea, from computer science, of generic prototype objects in certain programming languages (on the latter see e.g., Blaschek 1994). These can indeed be treated as individuals that have multiple instantiations, and properties can be added to them over time.

Freudenthal acknowledges that it remains to be seen whether his proposal can be carried out. De Iongh (1949) comments that Freudenthal in effect accepts Russell’s notion of formal implication (Russell 1903: section 12) as a primitive (Freudenthal does not mention Russell). In fact, Russell does not merely find the understanding of general implication as a containment relation less sympathetic, but mistaken (Russell 1903: section 77). On the other hand, Russell’s formal implication is construed as a relation between two propositional functions, and owes its generality to the fact that these take as arguments any value in the domain, whereas Freudenthal’s implication is a relation between two predications of an individual, and owes its generality to the fact that the individual in question is not any specific function but “the function in its free growth”.

As on this construal a proof of a general statement is in fact a proof for one peculiar individual, each instantiation of the general statement for another, normal individual needs its own proof (which will proceed along the exact same lines). Freudenthal accepts this:

> The general proof, given once, serves us no more than a map, which indeed facilitates the ascent of a mountain for us, but does not spare it. (Freudenthal 1937b: 116; translation mine)

This is also the case when an appeal is made to lemmas that are stated schematically, such as $m+n = n+m$. Freudenthal readily acknowledges that in linguistic representations of proof one will not do this, but considers this a way in which a linguistic representation fails to capture what a proof is.

Freudenthal’s paper was followed by comments from Heyting.[^note-40] Heyting agrees with Freudenthal’s thesis that if a mathematical statement is explained as the linguistic expression of a fact, then the meaning of the statement is given by its proof.[^note-41]

But at the same time he holds that posing a mathematical problem is not the same as making a mathematical assertion, and that this difference allows for an understanding of implications whose antecedent has not been established. An example he gives is that it is obviously correct to say that if *π* contains the sequence 0123456789, then it contains the sequence 012345678 (Heyting 1937: 117). (At the time there was no proof of the antecedent. In 1997 a computer program calculated that at the 17,387,594,880th digit after the decimal point in *π*, a sequence 0123456789 begins (Borwein 1998). One easily modifies Heyting’s example appropriately.) This is so, because we know how to turn solutions of the problem of finding a sequence 0123456789 into solutions of the problem of finding a sequence 012345678.

Furthermore, Heyting doubts that Freudenthal’s notion of an individual of which there may exist different exemplars clarifies matters. In his view, one would have to represent the collection of proper individuals by elements of a spread, so as to be able to explain universal quantification over these individuals in terms of the continuity principle for choice sequences applied to the sequences in the representing spread. But he observes that in that case Brouwer’s theorem that all total functions on the unit continuum are continuous cannot be reconstructed: The continuity of these functions is in fact a condition of the possibility of their representation in a spread. Brouwer published the proof of this representation theorem in his 1942B, to which the reader is referred for further details. That publication was clearly occasioned by a renewed interest on Brouwer’s part in the Freudenthal-Heyting exchange (see the opening lines of Brouwer 1942A).

Freudenthal (1937c) replied to Heyting in turn, but most briefly. He denies that with a reading in terms of problems and solutions the proper intuitionistic meaning, that is, one that does not depend on language and is not heuristic, has been found; and he considers it improbable that intuitionistic predicate calculus applies only to spreads, not to species.

The referee for *Compositio Mathematica*, in which this exchange between Freudenthal and Heyting appeared, was Brouwer. His report read:

> Interesting discussion on the sense of one sentence being implied by another, when nothing is known about the correctness of the latter sentence. (As quoted and translated in Sundholm & van Atten 2008: 70.)

One would have hoped to see Brouwer’s actual thoughts on the matter. On the other hand, as pointed out by van Dalen and Remmert (2007: 183), Brouwer was here playing both the role of referee and of editor in chief, so the only person meant actually to read this report was he.

To the extent that Freudenthal’s rejection of implication implies a rejection of negation defined as $A \rightarrow \bot$, whatever momentum Freudenthal’s objection may have had was taken over a few years later by the work of Griss; it seems that Griss was not aware of Freudenthal’s paper of 1937. Freudenthal’s proposed explanation of universal quantification seems not to have been developed any further within the tradition.

#### 2.2 Griss 1941–1951

Starting in 1941, Georg François Cornelis Griss argued that negation, and hence a whole class of implications, should be banished from intuitionism. Griss (1898–1953) had received his PhD in Amsterdam in 1925 for a thesis in differential geometry supervised by Weitzenböck, but had attended courses by Brouwer and was very sympathetic to intuitionism. (Most biographical details in this section come from van Rootselaar 1953–1954 and Pos 1953–1954.)

In a letter to Brouwer of April 19, 1941, he stated the point of departure for his negationless mathematics as follows:

> Showing that something is not true, i.e., showing the incorrectness of a hypothesis, is not an intuitively clear act. Of a hypothesis, which later turns out to be even wrong, one cannot possibly have an intuitively clear representation. One must maintain the demand that only building things up from the foundations makes sense in intuitionistic mathematics. (van Dalen 2011: Online Supplement, 2142; translation mine)

Insisting on intuitively clear representations throughout, Griss also holds that “to define is to construct” (Griss 1947: 69): a definition is meaningful only if it specifies a construction of the object defined.

Thus the notion of negation, understood as implication of a falsehood, is rejected. In *Idealistische Filosofie* (1947: 24), Griss repeats the above passage and points out this is in accord with criticism of negation by Bergson in *L’Évolution créatrice* (Bergson, 298–322); a rare occasion on which a Brouwerian intuitionist refers to the French philosopher of intuition. (Brouwer never discussed Bergson; see van Stigt 1990: 152–153 and 324 for differences between their conceptions, and also Hesseling 2003: sections 6.3.1–6.3.6.)

The fundamental point of agreement Griss finds with Bergson is that the only meaningful construal of negation consists in the positive notion of distinguishability. For example, the distinguishability of 1 and 2 is not defined as pure negation of their identity, but is an intuitive given based on their generation from the basic intuition of two-ity. For other objects, such as rational numbers and real numbers, the notion of distinguishability may be defined in terms of that of the natural numbers. With the rejection of negation also came a rejection of empty species, so that the intersection of two species exists only if they have an element in common. Griss is surprised to report that he has encountered more opposition against the rejection of empty species than against the avoidance of negation. (Griss 1951a: 45)

Griss acknowledges a role for problems and solutions in research (in terms of which Kolmogorov and Heyting understood logic, including negation); but he does not consider these to belong to mathematics proper:

> To negationless intuitionistic mathematics belong only constructions and properties in relation to those constructions. Posing problems and asking for solutions are premathematical activities. It goes without saying that in those premathematical investigations negation may be used just as well as all kinds of other means, like the principle of the excluded middle or even a physical experiment. (Griss 1948a: 72; translation mine)

Presumably, then, this would have determined his reply if Heyting had leveled the same objection to Griss’ position as he had done to Freudenthal’s, the objection that it is obviously correct to say that if *π* contains the sequence 0123456789, then it contains the sequence 012345678.

Indeed, it is clear that Griss’ conception has much in common with that of Freudenthal. At the same time, Griss’ notion of the “premathematical” seems to be much wider than Freudenthal’s of the “heuristic”. After all, for Freudenthal it was possible mathematically to prove a negative statement by showing that all ways to make the unnegated statement true by supplying an appropriate construction must fail. For Griss this is clearly excluded. (It seems Freudenthal and Griss never commented in print on each other’s positions. Note also that Griss, in his long letter to Brouwer of 1941 mentioned above that launched his program, does not refer to Freudenthal.)

Since negationless mathematics accepts only true propositions, its propositional logic contains only conjunction &, with implication as a special case: “The implication $p \rightarrow q$ will have its natural meaning: $q$ follows from $p$, $p$ is true, so $q$ is also true” (Griss 1951a: 41). However, an interpretation of Heyting’s propositional logic in this logic of & and $\rightarrow$ becomes possible by construing it as a logic of classes or species (Griss 1948b, 1951a). A basic species, for example that of the natural numbers, is taken as given, and all others will be constructed as subspecies of it. Then $\neg a$ can be defined as the complement of a relative to the basic species and $a \vee b$ is the union of $a$ and $b$. Thus, Griss (1951a) applied the strategy Heyting had used in 1928 to Heyting’s own formalization and deleted the parts that are not acceptable in negationless mathematics (while adding axioms and conditions to ensure that species be inhabited).

Axioms for an interpretation of predicate logic are obtained from those for propositional logic (Griss 1951a: 48). One substitutes $a(x)$ for $p$ everywhere, and prefixes all axioms in which $x$ occurs with $\forall x$. The meaning of $a(x)$ is that $x$ is an element of the species $a$, and $\forall x(a(x) \rightarrow b(x))$, is defined as $a \subset b$. (See below for a further remark on this in relation to a criticism voiced by Heyting in 1955.)

Treating intuitionistic mathematics according to Griss’ principles requires a substantial reconstruction. After a first mathematical sketch of his project in Dutch (Griss 1944), Griss made an informal start with parts of intuitionistic arithmetic, the theory of real numbers, and projective geometry in a series of papers published between 1946 and 1951 (Griss 1946, 1950, 1951b,c,d).

Griss was not able to continue that series, as in 1951 an illness began that would lead to his early death in 1953. However, he was able to act as the unofficial adviser of Nicolle Dequoy, who defended a doctoral thesis on negationless projective geometry at the Université de Paris in 1952 (supervised by Albert Châtelet, and published as Dequoy 1955). Formal work on negationless logic in Griss’ sense was done by Destouches-Février (1948),[^note-42] Gilmore 1953a, 1953b, and 1953c, Vredenduin 1953, Valpola 1955, Nelson 1966. This line of work culminated in Krivtsov 2000a, 2000b, 2000c, which give a comprehensive modern treatment of negationless predicate logic, arithmetic, analysis, and higher-order arithmetic.

When Griss began to elaborate the negationless intuitionistic mathematics that he proposed, Brouwer and Heyting supported his career in two ways. From 1944 to 1951, they communicated Griss’ papers to the Royal Dutch Academy of Sciences;[^note-43] and in 1949 they used their influence to reduce Griss’ teaching load at the high school in Gouda where he worked (van Rootselaar 1953–1954: 43).

But while supporting the publication of Griss’ papers, Brouwer at the same time presented a counterargument to one of Griss’ examples that implied that he did not support Griss’ philosophical claim.[^note-44] In his letter to Brouwer of 1941, Griss had remarked that

> No real number is known about which it has been proved that it cannot possibly be equal to 0 $(a \ne 0)$ while at the same time it has not been proven that the number differs positively from 0 ($a \mathbin{\#} 0$). (van Dalen 2011: 405)

($a \mathbin{\#} b$, the apartness relation, is defined as $\exists n(|a-b| \gt (1/2)^n)$.) Brouwer went on to publish a construction of a real number with just that property in “Essentially negative properties” (1948A). Brouwer’s argument, while suggestive, is perhaps not wholly conclusive: although it does show that the most obvious candidate for a positive equivalent fails, it does not show that there can be no such equivalent (Krivtsov 2000a: 167). Moreover, Brouwer did not make explicit how his own philosophical understanding of negation differed from that of Griss.

In 1949, David van Dantzig argued that the method that Brouwer had used in devising his example of an essentially negative property, which has become known as the method of the creating subject (section 3.3), depended on the untenable thesis “that there will ‘always’ be a human being willing and capable” of working on open problems (van Dantzig 1949: 951). Brouwer replied, in personal correspondence, that any psychological interpretation of intuitionism is incorrect (van Dalen 2011: 439; van Atten 2004b: chapter 6 for discussion). Note that, whether correct or not, this objection does not hinge on the possibility of negation as such.

Van Dantzig also pointed out that Brouwer’s construction cannot be used as an argument against Griss’ position, on pain of circularity:

> In any case it seems impossible to define Brouwer’s use of the term “absurd” without using another negative term (like “contradiction”), in other words it seems to be unavoidable to consider Brouwer’s general form of the negation as an “*entité primitive*”, irreducible to affirmative concepts. Therefore Brouwer’s theorem can not invalidate the attempts of other mathematicians (in particular G.F.C. Griss, Mrs. P. Destouches-Février and the present author) to do without the concept of negation. On the contrary, it shows again, how unclear the concept of “absurdity” is, and makes its avoidance appear more desirable. (van Dantzig 1949: 952)

On the other hand, while it is clear that Brouwer himself did not share these objections to absurdity, he had opened his article not by saying that he wrote it to refute but “to estimate the significance of affirmative or negationless mathematics, the development of which is sometimes advocated” (Brouwer 1948A: 963).

The “affirmative mathematics” mentioned in these quotations from van Dantzig and Brouwer was proposed by van Dantzig as a formal system for classical mathematicians to reason about numerical calculations and empirical problems (van Dantzig 1947b, 1951). It contains neither negation nor disjunction, although in certain contexts weak versions of these can be defined, and existential quantifiers must be bounded.[^note-45] Presented as “intuitionistic mathematics from a formal standpoint”, it does not aim to be a philosophical foundation of a logic for intuitionistic mathematics.[^note-46]

In 1955, Heyting objected to Griss’ position that it made it impossible to express generality:

> If we say, “For all real numbers $a$ and $b$, $a+b = b+a$”, this means the same as “If we construct two real numbers $a$ and $b$, then $a+b = b+a$”, but we have not actually constructed them. (Heyting 1953–1955: 95)

Taking this line further, a proof of the general statement would require the actual construction of all pairs of real numbers (and then showing that for each pair the equality holds), which is impossible. But in a review of Heyting’s paper, Vredenduin replied that the Grissian meaning is this:

> As soon as you have realized two real numbers $a$ and $b$, you can be certain that $a + b = b + a$. This would be meaningless only if real numbers were unrealizable. (Vredenduin 1956: 91)

Accordingly, what a general statement expresses directly is not a property of actual constructions, nor of unactual ones, but the correctness of a rule that applies to actual constructions. The premisse of the rule then means no more than “Let $a$ and $b$ be any two real numbers that we have constructed”. Griss would accept that as meaningful because he supplied a notion of real number and a construction method that shows that the species of real numbers thus construed is inhabited. Compare:

> The well-known turn in mathematics: “Suppose ABC to be rectangular” seems to be a supposition, but mostly means: “Consider a rectangular triangle ABC”. (Griss 1950: 456)

For further philosophical discussion of affirmative and negationless mathematics, see Apostel 1972; Beth 1966: 436–439; Fraenkel et al. 1973: 249–251; Franchella 1994b; Franchella 2008: 57–68; Heyting 1953–55; Heyting 1956: section 8.2. For an algebraic study of negationless logic see Imai & Iseki 1966 and Arruda1978; the latter also compares Griss’ and Vredenduin’s systems with one another. Modern formalizations of negationless systems are given in Krivtsov 2000a,b,c.

Griss’ negationless logic has been connected to the Curry-Howard isomorphism (e.g., Colson & Michel 2007, 2008, 2009; Michel 2008) and to the Calculus of Constructions (Demange 2015). These authors speak of “pedagogical logic”, as it reflects the pedagogical ideal that newly introduced hypotheses and definitions be motivated by examples.

An example of recent mathematical work that finds inspiration in the negationless approach is Veldman 2008.


## Notes（原文脚注，引自主文）

[^note-35]: 35. The reference was in Carnaps’s *Logische Syntax der Sprache* (Johansson to Heyting, November 15, 1935.)

[^note-36]: 36. As Heyting recalls in his letter of November 5, 1935 (page 3), they had in fact met, briefly, in Zürich in 1932; see also Johansson’s letter of November 15, 1935 (page 3). The latter letter is also informative about Johansson’s intellectual background. The Heyting-Johansson correspondence as kept in Heyting’s archive ends with a postcard from Johansson of January 28, 1936. The Heyting papers are at the Noord-Hollands Archief, Haarlem.

[^note-37]: 37. “Appropriate” here translates the Dutch “*doelmatig*”. Other translations of that term are “suitable”, “efficient”, “practical” (*Groot Woordenboek Nederlands-Engels*, Utrecht: van Dale 2008). The latter two may suggest a pragmatic criterion. But that can hardly be what Heyting had in mind, given that he thought of logical theorems as highly general mathematical ones, and thus, intuitionistically, certain.

[^note-38]: 38. This emends van Atten et al. 2014: 273 and van Atten & Sundholm 2016: 36, who stated that “to the best of our knowledge, the meeting never took place”.

[^note-39]: 39. The term “*Katalogisierung*” in this context is sometimes translated as “cataloguing” and more often as “locating”; the former seems to fit better here. Freudenthal’s definition is in fact proposed as an alternative to one that Brouwer made in a topological context (Brouwer 1926B2: 855). Freudenthal (1937a: 110) proves that the two definitions are equivalent.

[^note-40]: 40. A technical mistake in Heyting’s manuscript had been corrected by Brouwer. See van Dalen 2011: 393 for the letter, and also the extract and related remarks in Brouwer 1942A.

[^note-41]: 41. Also in later publications, e.g.,

> If mathematics consists of mental constructions, then every mathematical theorem is the expression of a result of a successful construction. The proof of the theorem consists in this construction itself, and the steps of the proof are the same as the steps of the mathematical construction. (Heyting 1958C: 107)

[^note-42]: 42. In 1947 Paulette Destouches-Février proposed a middle position between Griss’ logic, which she found too extreme, and that of Brouwer and Heyting by adding to the former the definition of $\neg p$ as $p \rightarrow(1=2)$, but no axioms for it (Destouches-Février 1947b: 1243). However, she does not motivate this philosophically. Destouches-Février (1914–2013) published (among many other things) a number of short technical notes on intuitionistic logic, Griss’ logic, and Johansson’s logic (1945a,b, 1947a,b, 1948, 1949, 1951). She was also the French translator of Heyting’s manuscript for Heyting 1955.

[^note-43]: 43. Brouwer presented Griss 1944, 1946, 1950, 1951a, and 1951b; Heyting presented Griss 1951c and 1951d, which dealt with intuitionistic axiomatic geometry.

[^note-44]: 44. Brouwer himself has published mathematical papers that he, without mentioning it at the time, did not sanction philosophically, namely, his papers in classical topology from the period 1909–1913, in which he used the classical reasoning that philosophically he had already rejected in Brouwer 1908C. Looking back on that period, Brouwer once called those papers “free of philosophy” (*philosophiefrei*; Brouwer 1919D: 204).

[^note-45]: 45. Heyting (1958C: 111) remarks that “from the intuitionistic point of view this restriction is difficult to account for”, and seems to overlook that Van Dantzig addresses the classical mathematician (van Dantzig 1947b: 1092).

[^note-46]: 46. Another development by Van Dantzig was ‘stable mathematics’ (1947a, 1951), an ecumenical attempt, inspired by Gödel’s double negation translation of classical into intuitionistic arithmetic (see section 4.5.1), to develop a fragment of classical mathematics in which all theorems are equivalent to their double negations also by intuitionistic standards. Gilmore (1956) pointed out in his review of van Dantzig 1951 that the greater problem for that project is not the occurrence in classical mathematics of the principle of the excluded middle but of impredicative definitions (see on this point also Gödel \*1933o and \*1941).