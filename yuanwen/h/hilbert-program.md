# Hilbert’s Program
**First published Thu Jul 31, 2003; substantive revision Fri Sep 29, 2023**

*Zach, Richard*

In the early 1920s, the German mathematician David Hilbert (1862–1943) put forward a new proposal for the foundation of classical mathematics which has come to be known as Hilbert’s Program. It calls for a formalization of all of mathematics in axiomatic form, together with a proof that this axiomatization of mathematics is consistent. The consistency proof itself was to be carried out using only what Hilbert called “finitary” methods. The special epistemological character of finitary reasoning then yields the required justification of classical mathematics. Although Hilbert proposed his program in this form only in 1921, various facets of it are rooted in foundational work of his going back until around 1900, when he first pointed out the necessity of giving a direct consistency proof of analysis. Work on the program progressed significantly in the 1920s with contributions from logicians such as Paul Bernays, Wilhelm Ackermann, John von Neumann, and Jacques Herbrand. It was also a great influence on Kurt Gödel, whose work on the incompleteness theorems were motivated by Hilbert’s Program. Gödel’s work is generally taken to show that Hilbert’s Program cannot be carried out. It has nevertheless continued to be an influential position in the philosophy of mathematics, and, starting with the work of Gerhard Gentzen in the 1930s, work on so-called Relativized Hilbert Programs have been central to the development of proof theory.

## 1. Historical development of Hilbert’s Program

### 1.1 Early work on foundations

Hilbert’s work on the foundations of mathematics has its roots in his work on geometry of the 1890s, culminating in his influential textbook *Foundations of Geometry* (1899) (see 19th Century Geometry). Hilbert believed that the proper way to develop any scientific subject rigorously required an axiomatic approach. In providing an axiomatic treatment, the theory would be developed independently of any need for intuition, and it would facilitate an analysis of the logical relationships between the basic concepts and the axioms. For Hilbert, the investigation of the independence and, above all, consistency of the axioms is of basic importance for an axiomatic treatment. For the axioms of geometry, consistency can be proved by providing an interpretation of the system in the real plane, and thus, the consistency of geometry is reduced to the consistency of analysis. The foundation of analysis, of course, itself requires an axiomatization and a consistency proof. Hilbert provided such an axiomatization in (1900b), but it became clear very quickly that the consistency of analysis faced significant difficulties, in particular because the favored way of providing a foundation for analysis in Dedekind’s work relied on dubious assumptions akin to to those that lead to the paradoxes of set theory and Russell’s Paradox in Frege’s foundation of arithmetic.

Hilbert thus realized that a *direct* consistency proof of analysis, i.e., one not based on reduction to another theory, was needed. He proposed the problem of finding such a proof as the second of his 23 mathematical problems in his address to the International Congress of Mathematicians in 1900 (1900a) and presented a sketch of such a proof in his Heidelberg talk (1905). Several factors delayed the further development of Hilbert’s foundational program. One was perhaps the criticism of Poincaré (1906) against what he saw as a viciously circular use of induction in Hilbert’s sketched consistency proof (see Steiner 1975, Appendix)[^steiner-1975]. Hilbert also realized that axiomatic investigations required a well worked-out logical formalism. At the time he relied on a conception of logic based on the algebraic tradition, in particular, on Schröder’s work, which was not particularly suited as a formalism for the axiomatization of mathematics. (See Peckhaus 1990 on the early development of Hilbert’s Program.)[^peckhaus-1990]

### 1.2 The influence of *Principia Mathematica*

The publication of Russell and Whitehead’s *Principia Mathematica* provided the required logical basis for a renewed attack on foundational issues. Beginning in 1914, Hilbert’s student Heinrich Behmann and others studied the system of *Principia* (see Mancosu 1999 on Behmann’s role in Hilbert’s school)[^mancosu-1999]. Hilbert himself returned to work on foundational issues in 1917. In September 1917, he delivered an address to the Swiss Mathematical Society entitled “Axiomatic Thought” (1918a). It is his first published contribution to mathematical foundations since 1905. In it, he again emphasizes the requirement of consistency proofs for axiomatic systems: “The chief requirement of the theory of axioms must go farther [than merely avoiding known paradoxes], namely, to show that within every field of knowledge contradictions based on the underlying axiom-system are *absolutely impossible*.” He poses the proof of the consistency of arithmetic (and of set theory) again as the main open problems. In both these cases, there seems to be nothing more fundamental available to which the consistency could be reduced other than logic itself. And Hilbert then thought that the problem had essentially been solved by Russell’s work in *Principia*. Nevertheless, other fundamental problems of axiomatics remained unsolved, including the problem of the “decidability of every mathematical question,” which also traces back to Hilbert’s 1900 address.

These unresolved problems of axiomatics led Hilbert to devote significant effort to work on logic in the following years. In 1917, Paul Bernays joined him as his assistant in Göttingen. In a series of courses from 1917–1921, Hilbert, with the assistance of Bernays and Behmann, made significant new contributions to formal logic. The course from 1917 (Hilbert, 1918b)[^hilbert-1918b], in particular, contains a sophisticated development of first-order logic, and forms the basis of Hilbert and Ackermann’s textbook *Principles of Theoretical Logic* (1928) (see Ewald and Sieg 2013, Sieg 1999, and Zach 1999, 2003)[^ewald-2013][^sieg-1999][^sieg-2013][^zach-1999][^zach-2003].

### 1.3 Finitism and the quest for consistency proofs

Within the next few years, however, Hilbert came to reject Russell’s logicist solution to the consistency problem for arithmetic. At the same time, Brouwer’s intuitionistic mathematics gained currency. In particular, Hilbert’s former student Hermann Weyl converted to intuitionism. Weyl’s paper “The new foundational crisis in mathematics” (1921) was answered by Hilbert in three talks in Hamburg in the Summer of 1921 (1922b). Here, Hilbert presented his own proposal for a solution to the problem of the foundation of mathematics. This proposal incorporated Hilbert’s ideas from 1904 regarding direct consistency proofs, his conception of axiomatic systems, and also the technical developments in the axiomatization of mathematics in the work of Russell as well as the further developments carried out by him and his collaborators. What was new was the way in which Hilbert wanted to imbue his consistency project with the philosophical significance necessary to answer Brouwer and Weyl’s criticisms: the finitary point of view.

According to Hilbert, there is a privileged part of mathematics, contentual elementary number theory, which relies only on a “purely intuitive basis of concrete signs.” Whereas the operating with abstract concepts was considered “inadequate and uncertain,” there is a realm of

> extra-logical discrete objects, which exist intuitively as immediate experience before all thought. If logical inference is to be certain, then these objects must be capable of being completely surveyed in all their parts, and their presentation, their difference, their succession (like the objects themselves) must exist for us immediately, intuitively, as something which cannot be reduced to something else. (Hilbert 1922b, 202; the passage is repeated almost verbatim in Hilbert 1926, 376, Hilbert 1928, 464, and Hilbert 1931b, 267)[^hilbert-1922b][^hilbert-1926][^hilbert-1928][^hilbert-1931b][^hilbert-1928-2]

These objects were, for Hilbert, *signs*. The domain of contentual number theory consists in the finitary numerals, i.e., sequences of strokes. These have no meaning, i.e., they do not stand for abstract objects, but they can be operated on (e.g., concatenated) and compared. Knowledge of their properties and relations is intuitive and unmediated by logical inference. Contentual number theory developed this way is secure, according to Hilbert: no contradictions can arise simply because there is no logical structure in the propositions of contentual number theory.

The intuitive-contentual operations with signs forms the basis of Hilbert’s metamathematics. Just as contentual number theory operates with sequences of strokes, so metamathematics operates with sequences of symbols (formulas, proofs). Formulas and proofs can be syntactically manipulated, and the properties and relationships of formulas and proofs are similarly based in a logic-free intuitive capacity which guarantees certainty of knowledge about formulas and proofs arrived at by such syntactic operations. Mathematics itself, however, operates with abstract concepts, e.g., quantifiers, sets, functions, and uses logical inference based on principles such as mathematical induction or the principle of the excluded middle. These “concept-formations” and modes of reasoning had been criticized by Brouwer and others on grounds that they presuppose infinite totalities as given, or that they involve impredicative definitions (which were considered by the critics as viciously circular). Hilbert’s aim was to justify their use. To this end, he pointed out that they can be formalized in axiomatic systems (such as that of *Principia* or those developed by Hilbert himself), and mathematical propositions and proofs thus turn into formulas and derivations from axioms according to strictly circumscribed rules of derivation. Mathematics, so Hilbert, “becomes an inventory of provable formulas.” In this way the proofs of mathematics are subject to metamathematical, contentual investigation. The goal of Hilbert’s program is then to give a contentual, metamathematical proof that there can be no derivation of a contradiction, i.e., no formal derivations of a formula $A$ and of its negation $\neg A$.

This sketch of the aims of the program was fleshed out by Hilbert and his collaborators in the following 10 years. On the conceptual side, the finite standpoint and the strategy for a consistency proof were elaborated by Hilbert (1928); Hilbert (1923); Hilbert (1926) and Bernays (1928b); Bernays (1922); Bernays (1930), of which Hilbert’s article “On the infinite” (1926) provides the most detailed elaboration of the finitary standpoint. In addition to Hilbert and Bernays, a number of other people were involved in technical work on the program. In lectures given in Göttingen (Hilbert and Bernays, 1923; Hilbert, 1922a)[^bernays-1923][^hilbert-1922a][^hilbert-1923][^hilbert-1923-2], Hilbert and Bernays developed the $\varepsilon$-calculus as their definitive formalism for axiom systems for arithmetic and analysis. Hilbert there also presented his approach to giving consistency proofs using his so-called $\varepsilon$-substitution method. Ackermann (1924) attempted to extend Hilbert’s idea to a system of analysis. The proof was, however, erroneous (see Zach 2003)[^zach-2003]. John von Neumann, then visiting Göttingen, gave a corrected consistency proof for a system of the $\varepsilon$-formalism (which, however, did not include the induction axiom) in 1925 (published in 1927). Building on von Neumann’s work, Ackermann devised a new $\varepsilon$-substitution procedure which he communicated to Bernays (see Bernays 1928b)[^bernays-1928b]. In his address “Problems of the grounding of mathematics” to the International Congress of Mathematicians in Bologna in 1928 (1929), Hilbert optimistically claimed that the work of Ackermann and von Neumann had established the consistency of number theory and that the proof for analysis had already been carried out by Ackermann “to the extent that the only remaining task consists in the proof of an elementary finiteness theorem that is purely arithmetical.”

### 1.4 The impact of Gödel’s Incompleteness Theorems

Gödel’s incompleteness theorems showed that Hilbert’s optimism was undue. In September 1930, Kurt Gödel announced his first incompleteness theorem at a conference in Königsberg. Von Neumann, who was in the audience, immediately recognized the significance of Gödel’s result for Hilbert’s program. Shortly after the conference he wrote to Gödel, telling him that he had found a corollary to Gödel’s result. Gödel had found the same result already independently: the second incompleteness theorem, asserting that the system of *Principia* does not prove the formalization of the claim that the system of *Principia* is consistent (provided it is). All the methods of finitary reasoning used in the consistency proofs up till then were believed to be formalizable in *Principia*, however. Hence, if the consistency of *Principia* were provable by the methods used in Ackermann’s proofs, it should be possible to formalize this proof in *Principia*; but this is what the second incompleteness theorem states is impossible. Bernays also realized the importance of Gödel’s results immediately after he studied Gödel’s paper in January 1931, writing to Gödel that (under the assumption that finitary reasoning can be formalized in *Principia*) the incompleteness theorem shows that a finitary consistency proof of *Principia* is impossible. Shortly thereafter, von Neumann showed that Ackermann’s consistency proof is flawed and provided a counterexample to the proposed $\varepsilon$-substitution procedure (see Zach 2003)[^zach-2003].

In (1936), Gentzen published a consistency proof of first-order Peano Arithmetic ($\PA$). As Gödel had shown was necessary, Gentzen’s proof used methods that could not be formalized in $\PA$ itself, namely, transfinite induction along the ordinal $\varepsilon_0$. Gentzen’s work marks the beginning of post-Gödelian proof theory and work on Relativized Hilbert Programs. Proof theory in the tradition of Gentzen has analyzed axiomatic systems according to what extensions of the finitary standpoint are necessary to prove their consistency. Usually, the consistency strength of systems has been measured by the system’s *proof-theoretic ordinal*, i.e., the ordinal transfinite induction along which suffices to prove consistency. In the case of $\PA$, that ordinal is $\varepsilon_0$. (For further discussion, see the entries on proof theory and the development of proof theory.)

## 2. The Finitary Point of View

The cornerstone of Hilbert’s philosophy of mathematics, and the substantially new aspect of his foundational thought from 1922b onward, consisted in what he called the finitary standpoint. This methodological standpoint consists in a restriction of mathematical thought to those objects which are “intuitively present as immediate experience prior to all thought,” and to those operations on and methods of reasoning about such objects which do not require the introduction of abstract concepts, in particular, without appeal to completed infinite totalities.

There are several basic and interrelated issues in understanding Hilbert’s finitary standpoint:

1. What are the objects of finitary reasoning?
2. What are the finitarily meaningful propositions?
3. What are the finitarily acceptable methods of construction and reasoning?

### 2.1 Finitary objects and finitist epistemology

Hilbert characterized the domain of finitary reasoning in a well-known paragraph which appears in roughly the same formulation in all of Hilbert’s more philosophical papers from the 1920s (1931b; 1922b; 1928; 1926):

> [A]s a condition for the use of logical inferences and the performance of logical operations, something must already be given to our faculty of representation, certain extralogical concrete objects that are intuitively present as immediate experience prior to all thought. If logical inference is to be reliable, it must be possible to survey these objects completely in all their parts, and the fact that they occur, that they differ from one another, and that they follow each other, or are concatenated, is immediately given intuitively, together with the objects, as something that can neither be reduced to anything else nor requires reduction. This is the basic philosophical position that I consider requisite for mathematics and, in general, for all scientific thinking, understanding, and communication. (Hilbert, 1926, 376)[^hilbert-1926]

These objects are, for Hilbert, the *signs*. For the domain of contentual number theory, the signs in question are numerals such as

> 1, 11, 111, 11111

The question of how exactly Hilbert understood the numerals is difficult to answer. They are not physical objects (actual strokes on paper, for instance), since it must always be possible to extend a numeral by adding another stroke (and, as Hilbert also argues in “On the infinite” (1926), it is doubtful that the physical universe is infinite). According to Hilbert (1922b, 202), their “shape can be generally and certainly recognized by us—independently of space and time, of the special conditions of the production of the sign, and of the insignificant differences in the finished product.” They are not mental constructions, since their properties are objective, yet their existence is dependent on their intuitive construction (see Bernays 1923, 226)[^bernays-1923]. What is clear in any case is that they are logically primitive, i.e., they are neither concepts (as Frege’s numbers are) nor sets. What is important here is not primarily their metaphysical status (abstract versus concrete in the current sense of these terms), but that they do not enter into logical relations, e.g., they cannot be predicated of anything. In Bernays’s most mature presentations of finitism (Hilbert and Bernays, 1939; Bernays, 1930)[^bernays-1930][^hilbert-1939], the objects of finitism are characterized as *formal objects* which are recursively generated by a process of repetition; the stroke symbols are then concrete representations of these formal objects.

The question of what Hilbert thought the epistemological status of the objects of finitism was is equally difficult. In order to carry out the task of providing a secure foundation for infinitistic mathematics, access to finitary objects must be immediate and certain. Hilbert’s philosophical background was broadly Kantian, as was Bernays’s, who was closely affiliated with the neo-Kantian school of philosophy around Leonard Nelson in Göttingen. Hilbert’s characterization of finitism often refers to Kantian intuition, and the objects of finitism as objects given intuitively. Indeed, in Kant’s epistemology, immediacy is a defining characteristic of intuitive knowledge. The question is, what kind of intuition is at play? Mancosu (1998b) identifies a shift in this regard. He argues that whereas the intuition involved in Hilbert’s early papers was a kind of perceptual intuition, in later writings (e.g., Bernays 1928a)[^bernays-1928a] it is identified as a form of pure intuition in the Kantian sense. However, at roughly the same time Hilbert (1928, 469) still identifies the kind of intuition at play as perceptual. In (1931b, 266–267), Hilbert sees the finite mode of thought as a separate source of *a priori* knowledge in addition to pure intuition (e.g., of space) and reason, claiming that he has “recognized and characterized the third source of knowledge that accompanies experience and logic.” Both Bernays and Hilbert justify finitary knowledge in broadly Kantian terms (without however going so far as to provide a transcendental deduction), characterizing finitary reasoning as the kind of reasoning that underlies all mathematical, and indeed, scientific, thinking, and without which such thought would be impossible. (See Kitcher 1976 and Parsons 1998 on the epistemology of finitism, Patton 2014 for historical and philosophical context of Hilbert’s theory of signs, and Eder (forthcoming) specifically on the ensuing debate with the German philosopher Aloys Müller.)

### 2.2 Finitarily meaningful propositions and finitary reasoning

The most basic judgments about finitary numerals are those about equality and inequality. In addition, the finite standpoint allows operations on finitary objects. Here the most basic is that of concatenation. The concatenation of the numerals 11 and 111 is communicated as “$2 + 3$,” and the statement that 11 concatenated with 111 results in the same numeral as 111 concatenated with 11 by “$2 + 3 = 3 + 2$.” In actual proof-theoretic practice, as well as explicitly in (Hilbert and Bernays, 1934; Bernays, 1930)[^bernays-1930][^hilbert-1934], these basic operations are generalized to operations defined by recursion, paradigmatically, primitive recursion, e.g., multiplication and exponentiation (see Parsons 1998 for philosophical difficulties in relation to exponentiation and 2007 for an extended discussion of intuitive mathematics and finitism)[^parsons-1998]. Similarly, finitary judgments may involve not just equality or inequality but also basic decidable properties, such as “is a prime.” This is finitarily acceptable as long as the characteristic function of such a property is itself finitary: For instance, the operation which transforms a numeral to 1 if it is prime and 11 otherwise can be defined by primitive recursion and is hence finitary. Such finitary propositions may be combined by the usual logical operations of conjunction, disjunction, negation, but also bounded quantification. (Hilbert, 1926)[^hilbert-1926] gives the example of the proposition that “there is a prime number between $p + 1$ and $p! + 1$” where $p$ is a certain large prime. This statement is finitarily acceptable since it “serves merely to abbreviate the proposition” that either $p + 1$ or $p + 2$ or $p + 3$ or … or $p! + 1$ is a prime.

The problematic finitary propositions are those that express general facts about numerals such as that, for any given numeral $n, 1+n = n+1$. It is problematic because, as Hilbert puts it, it “is from the finitist point of view *incapable of being negated*” (1926, 378). By this he means that the contradictory proposition that there is a numeral $n$ for which $1+n \ne n+1$ is not finitarily meaningful. “One cannot, after all, try out all numbers” (1928, 470). For the same reason, a finitary general proposition is not to be understood as an infinite conjunction but “only as a hypothetical judgment that comes to assert something when a numeral is given” (ibid.). Even though they are problematic in this sense, general finitary statements are of particular importance to Hilbert’s proof theory, since the statement of consistency of a formal system $S$ is of such a general form: for any given sequence of formulas $P, P$ is not a derivation of a contradiction in $S$.

### 2.3 Finitary operations and finitary proof

Of crucial importance to both an understanding of finitism and of Hilbert’s proof theory is the question of what operations and what principles of proof should be allowed from the finitist standpoint. That a general answer is necessary is clear from the demands of Hilbert’s proof theory, i.e., it is not to be expected that given a formal system of mathematics (or even a single sequence of formulas) one can “see” that it is consistent (or that it cannot be a genuine derivation of an inconsistency) the way we can see, e.g., that $11 + 111 = 111 + 11$. What is required for a consistency proof is an operation which, given a formal derivation, transforms such a derivation into one of a special form, plus proofs that the operation in fact does this and that proofs of the special kind cannot be proofs of an inconsistency. To count as a finitary consistency proof, the operation itself must be acceptable from the finitist standpoint, and the proofs required must use only finitarily acceptable principles.

Hilbert never gave a general account of which operations and methods of proof are acceptable from the finitist standpoint, but only examples of operations and methods of inference in contentual finitary number theory which he accepted as finitary. Contentual induction was accepted in its application to finitary statements of the hypothetical, general kind explicitly in Hilbert (1922b). He (1923, 1139) said that intuitive thought “includes recursion and intuitive induction for finite existing totalities,” and used exponentiation in an example in 1928. Bernays (1930) explained how exponentiation may be understood as a finitary operation on numerals. Hilbert and Bernays (1934) give the only general account of finitary contentual number theory; according to it, operations defined by primitive recursion and proofs using induction are finitarily acceptable. All of these methods can be formalized in a system known as primitive recursive arithmetic ($\PRA$), which allows definitions of functions by primitive recursion and induction on quantifier-free formulas (ibid.). However, neither Hilbert nor Bernays ever claimed that *only* primitive recursive operations count as finitary, and they in fact did use some non-primitive recursive methods in ostensibly finitary consistency proofs already in 1923 (see Tait 2002 and Zach 2003)[^tait-2002][^zach-2003].

The more interesting conceptual issue is which operations *should* be considered as finitary. Since Hilbert was less than completely clear on what the finitary standpoint consists in, there is some leeway in setting up the constraints, epistemological and otherwise, an analysis of finitist operation and proof must fulfill. Hilbert characterized (see above) the objects of finitary number theory as “intuitively given,” as “surveyable in all their parts,” and said that their having basic properties must “exist intuitively” for us. Bernays (1922, 216) suggests that in finitary mathematics, only “primitive intuitive cognitions come into play,” and uses the term “point of view of intuitive evidence” in connection with finitism 1930, 250. This characterization of finitism as primarily to do with *intuition* and intuitive knowledge has been emphasized in particular by (Parsons, 1998)[^parsons-1998] who argues that what can count as finitary on this understanding is not more than those arithmetical operations that can be defined from addition and multiplication using bounded recursion. In particular, according to him, exponentiation and general primitive recursion are not finitarily acceptable.

The thesis that finitism coincides with primitive recursive reasoning has received a forceful defense by (Tait 1981; see also 2002, 2005b, 2019)[^tait-1981]. Tait, in contrast to Parsons, rejects the aspect of representability in intuition as the hallmark of the finitary; instead he takes finitary reasoning to be “a minimal kind of reasoning presupposed by all non-trivial mathematical reasoning about numbers.” and analyzes finitary operations and methods of proof as those that are implicit in the very notion of number as the form of a finite sequence. This analysis of finitism is supported by Hilbert’s contention that finitary reasoning is a precondition for logical and mathematical, indeed any scientific thinking Hilbert (1931b, 267). Since finitary reasoning is that part of mathematics which is presupposed by all non-trivial reasoning about numbers, it is, so Tait, “indubitable” in a Cartesian sense, and this indubitability as all that would be required of finitary reasoning to provide the epistemological grounding of mathematics Hilbert intended it for.

Another interesting analysis of finitary proof, which, however, does not provide as detailed a philosophical justification, was proposed by Kreisel (1960). It yields the result that exactly those functions are finitary which can be proved to be total in first-order arithmetic $\PA$. It is based on the proof-theoretic concept of a reflection principle; see Zach (2006) for more detail and Dean (2015) for an analysis. Kreisel (1970, Section 3.5) provides another analysis by focusing on what is “visualizable.” The result is the same: finitary provability turns out to be coextensive with provability in $\PA$.

Tait’s technical analysis yields that the finitistic functions are exactly the primitive recursive ones, and the finitistic number-theoretic truths are exactly those provable in the theory of primitive recursive arithmetic $\PRA.$ It is important to stress that this analysis is not carried out from within the finitist viewpoint itself. Since the general notions of “function” and “proof” are not themselves finitary, the finitist is unable to make sense of Tait’s thesis that everything provable in $\PRA$ is finitistically true. According to Tait, a proper analysis of finitistic provability must not assume that finitism itself has access to such non-finitistic notions. Kreisel’s approach and some criticisms of Tait that rely on reflection principles or $\omega$-rules run afoul of this requirement (see Tait 2002, 2005b)[^tait-2002][^tait-2005b]. On the other hand, one could argue that $\PRA$ is too strong a theory to count as a formalization of what is “presupposed by all non-trivial mathematical reasoning about numbers”: there are weaker but non-trivial theories which are related to smaller classes of functions than the primitive recursive ones, such as $\PV$ and $\EA$, related to the polynomial-time and Kalmar-elementary functions respectively (see Avigad 2003 on how much mathematics can be carried out in $\EA)[^avigad-2003]$. Using an analysis along the same lines as Tait’s, Ganea (2010) has arrived at the corresponding class of Kalmar-elementary functions as those that are finitistic. See also Incurvati (2019) for further analysis of different notions of finitism.

## 3. Formalism, reductionism and instrumentalism

Weyl (1925) was a conciliatory reaction to Hilbert’s proposal in 1922b and 1923, which nevertheless contained some important criticisms. Weyl described Hilbert’s project as replacing contentual mathematics by a meaningless game of formulas. He noted that Hilbert wanted to “secure not *truth*, but the *consistency* of analysis” and suggested a criticism that echoes an earlier one by Frege: Why should we take consistency of a formal system of mathematics as a reason to believe in the truth of the pre-formal mathematics it codifies? Is Hilbert’s meaningless inventory of formulas not just “the bloodless ghost of analysis”? Weyl suggested a solution:

> [I]f mathematics is to remain a serious cultural concern, then some *sense* must be attached to Hilbert’s game of formulae, and I see only one possibility of attributing it (including its transfinite components) an independent intellectual meaning. In theoretical physics we have before us the great example of a [kind of] knowledge of completely different character than the common or phenomenal knowledge that expresses purely what is given in intuition. While in this case every judgment has its own sense that is completely realizable within intuition, this is by no means the case for the statements of theoretical physics. In that case it is rather *the system as a whole* that is in question if confronted with experience. (Weyl, 1925, 140)[^weyl-1925]

The analogy with physics is striking, and one can find similar ideas in Hilbert’s own writing—perhaps Hilbert was influenced in this by Weyl. Although Hilbert’s first proposals focused exclusively on consistency, there is a noticeable development in Hilbert’s thinking in the direction of a general reductivist project of a sort quite common in the philosophy of science at the time (as was pointed out by Giaquinto 1983)[^giaquinto-1983]. In the second half of the 1920s, Hilbert replaced the consistency program with a conservativity program: Formalized mathematics was to be considered by analogy with theoretical physics. The ultimate justification for the theoretical part lies in its conservativity over “real” mathematics: whenever theoretical, “ideal” mathematics proves a “real” proposition, that proposition is also intuitively true. This justifies the use of transfinite mathematics: it is not only internally consistent, but it proves only true intuitive propositions (and indeed all, since a formalization of intuitive mathematics is part of the formalization of all mathematics).

In 1926, Hilbert introduced a distinction between real and ideal formulas. This distinction was not present in 1922b and only hinted at in 1923. In the latter, Hilbert presents first a formal system of quantifier-free number theory about which he says that “The provable formulae we acquire in this way all have the character of the finite” (1139). Then the transfinite axioms (i.e., quantifiers) are added to simplify and complete the theory (1144). Here he draws the analogy with the method of ideal elements for the first time: “In my proof theory, the transfinite axioms and formulae are adjoined to the finite axioms, just as in the theory of complex variables the imaginary elements are adjoined to the real, and just as in geometry the ideal constructions are adjoined to the actual” (ibid). When Hilbert, in 1926 explicitly introduces the notion of an ideal proposition, and in 1928, when he first speaks of *real propositions* in addition to the ideal, he is quite clear that the real part of the theory consists only of decidable, variable-free formulas. They are supposed to be “directly capable of verification”—akin to propositions derived from laws of nature which can be checked by experiment (1928, 475). The new picture of the program was this: Classical mathematics is to be formalized in a system which includes formalizations of all the directly verifiable (by calculation) propositions of contentual finite number theory. The consistency proof should show that all real propositions which can be proved by ideal methods are true, i.e., can be directly verified by finite calculation. (Actual proofs such as the $\varepsilon$-substitution had always been of such a kind: provide finitary procedures which eliminate transfinite elements from proofs of real statements, in particular, of $0 = 1$.) Indeed, Hilbert saw that something stronger is true: not only does a consistency proof establish truth of real formulas provable by ideal methods, but it yields finitary proofs of finitary general propositions if the corresponding free-variable formula is derivable by ideal methods (1928, 474).

Hilbert suggested further restrictions on the theory in addition to conservativity: simplicity, brevity of proofs, “economy of thought” and mathematical productivity. The formal system of transfinite logic is not arbitrary: “This formula game is carried out according to certain definite rules, in which the *technique of our thinking* is expressed. […] The fundamental idea of my proof theory is none other than to describe the activity of our understanding, to make a protocol of the rules according to which our thinking actually proceeds” (Hilbert 1928, 475)[^hilbert-1928][^hilbert-1928-2]. When Weyl (1928) eventually turned away from intuitionism, he emphasized this motivation of Hilbert’s proof theory: not to turn mathematics into a meaningless game of symbols, but to turn it into a theoretical science which codifies scientific (mathematical) practice (see Mancosu and Ryckman 2002 and Kish Bar-On 2021 on Weyl’s relationship to intuitionism and Hilbert’s formalism)[^mancosu-2021][^mancosu-2002].

Hilbert’s formalism was thus quite sophisticated: It avoided two crucial objections: (1) If the formulas of the system are meaningless, how can derivability in the system generate any kind of belief? (2) Why accept the system of $\PA$ and not any other consistent system? Both objections are familiar from Frege; both questions are (in part) answered by a conservativity proof for real statements. For (2), furthermore, Hilbert has a naturalistic criterion of acceptance: we are constrained in the choice of systems by considerations of simplicity, fecundity, uniformity, and by what mathematicians actually do; Weyl would add that the ultimate test of a theory would be its usefulness in physics.

Most philosophers of mathematics writing on Hilbert have read him as an instrumentalist (including Kitcher 1976, Resnik 1980, Giaquinto 1983, Sieg 1990, and in particular Detlefsen 1986)[^detlefsen-1986][^giaquinto-1983][^kitcher-1976][^resnik-1980][^sieg-1990] in that they read Hilbert’s explanation that the ideal propositions “have no meaning in themselves” (Hilbert, 1926, 381)[^hilbert-1926] as claiming that classical mathematics is a *mere* instrument, and that statements of transfinite mathematics have no truth value. To the extent that this is accurate, it must be understood as a methodological instrumentalism: A successful execution of the proof-theoretic program would show that one could pretend *as if* mathematics was meaningless. The analogy with physics is therefore not: transfinite propositions have no meaning just as propositions involving theoretical terms have no meaning, but: transfinite propositions require no direct intuitive meaning just as one does not have to directly see electrons in order to theorize about them. Hallett (1990), taking into account the 19th century mathematical background from which Hilbert came as well as published and unpublished sources from Hilbert’s entire career (in particular Hilbert 1992, the most extensive discussion of the method of ideal elements)[^hilbert-1992] comes to the following conclusion:

> [Hilbert’s treatment of philosophical questions] is *not* meant as a kind of instrumentalist agnosticism about existence and truth and so forth. On the contrary, it is meant to provide a non-skeptical and positive solution to such problems, a solution couched in cognitively accessible terms. And, it appears, the same solution holds for both mathematical and physical theories. Once new concepts or “ideal elements” or new theoretical terms have been accepted, then they exist in the sense in which *any* theoretical entities exist. (Hallett, 1990, 239)[^hallett-1990]

## 4. Hilbert’s Program and Gödel’s incompleteness theorems

There has been some debate over the impact of Gödel’s incompleteness theorems on Hilbert’s Program, and whether it was the first or the second incompleteness theorem that delivered the *coup de grâce*. Undoubtedly the opinion of those most directly involved in the developments were convinced that the theorems did have a decisive impact. Gödel announced the second incompleteness theorem in an abstract published in October 1930: no consistency proof of systems such as *Principia*, Zermelo-Fraenkel set theory, or the systems investigated by Ackermann and von Neumann is possible by methods which can be formulated in these systems. In the full version of his paper, Gödel (1931) left open the possibility that there could be finitary methods which are not formalizable in these systems and which would yield the required consistency proofs. Bernays’s first reaction in a letter to Gödel in January 1931 was likewise that “if, as von Neumann does, one takes it as certain that any and every finitary consideration may be formalized within the system $P$—like you, I regard that in no way as settled—one comes to the conclusion that a finitary demonstration of the consistency of $P$ is impossible” (Gödel, 2003a, 87).

How do Gödel’s theorems impact Hilbert’s program? Through a careful (“Gödel”-) coding of sequences of symbols (formulas, proofs), Gödel showed that in theories $T$ which contain a sufficient amount of arithmetic, it is possible to produce a formula $Pr(x, y)$ which “says” that $x$ is (the code of) a proof of (the formula with code) $y$. Specifically, if $\ulcorner 0 = 1\urcorner$ is the code of the formula $0 = 1$, then $Con_T = \forall x \neg Pr(x,\ulcorner 0 = 1\urcorner)$ may be taken to “say” that $T$ is consistent (no number is the code of a derivation in $T$ of $0 = 1)$. The second incompleteness theorem (G2) says that under certain assumptions about $T$ and the coding apparatus, $T$ does not prove $Con_T$. Now suppose there were a finitary consistency proof of $T$. The methods used in such a proof would presumably be formalizable in $T$. (“Formalizable” means that, roughly, if the proof uses a finitary operation $f$ on derivations which transforms any derivation $D$ into a derivation $f (D)$ of a simple form; then there is a formula $F(x, y)$ so that, for all derivations $D,T \vdash F(\ulcorner D\urcorner ,\ulcorner f (D)\urcorner)$.) The consistency of $T$ would be finitarily expressed as the general hypothetical that, if $D$ is any given sequence of symbols, $D$ is not a derivation in $T$ of the formula $0 = 1$. The formalization of this proposition is the formula $\neg Pr(x,\ulcorner 0 = 1\urcorner)$ in which the variable $x$ occurs free. If there were a finitary proof of the consistency of $T$, its formalization would yield a derivation in $T$ of $\neg Pr_T (x,\ulcorner 0 = 1\urcorner),$ from which $Con_T$ can be derived in $T$ by simple universal generalization on $x$. Yet, a derivation of $Con_T$ in $T$ is ruled out by G2.

As mentioned above, initially Gödel and Bernays thought that the difficulty for the consistency proof of $\PA$ could be overcome by employing methods which, although not formalizable in $\PA$, are nonetheless finitary. Whether such methods would be considered finitary according to the original conception of finitism or constitute an extension of the original finitist viewpoint is a matter of debate. The new methods considered included a finitary version of the $\omega$-rule proposed by Hilbert (1931b; 1931a). It is fair to say, however, that after about 1934 it has been almost universally accepted that the methods of proof accepted as finitary prior to Gödel’s results are all formalizable in $\PA$. Extensions of the original finitist standpoint have been proposed and defended on broadly finitary grounds, e.g., Gentzen (1936) defended the use of transfinite induction up to $\varepsilon_0$ in his consistency proof for $\PA$ as “indisputable,” Takeuti (1987) gave another defense. Gödel (1958) presented another extension of the finitist standpoint; the work of Kreisel mentioned above may be seen as another attempt to extend finitism while retaining the spirit of Hilbert’s original conception.

A different attempt at providing a way around Gödel’s second theorem for Hilbert’s Program was proposed by Detlefsen (1986; 2001; 1979). Detlefsen presents several lines of defense, one of which is similar to the one just described: arguing that a version of the $\omega$-rule is finitarily acceptable, although not capable of formalization (however, see Ignjatovic 1994)[^ignjatovic-1994]. Detlefsen’s other argument against the common interpretation of Gödel’s second theorem focuses on the notion of formalization: That the particular formalization of “$T$ is consistent” by Gödel’s formula $Con_T$ is not provable does not imply that there couldn’t be other formulas, which *are* provable in $T$, and which have as much right to be called “formalizations of the consistency of $T$.” These rely on different formalizations of the provability predicate $Pr_T$ than the standard ones. It is known that formalized consistency statements are unprovable whenever the provability predicate obeys certain general derivability conditions. Detlefsen argues that these conditions are not necessary for a predicate to count as a genuine provability predicate, and indeed there are provability predicates which violate the provability conditions and which give rise to consistency formulas which *are* provable in their corresponding theories. These, however, depend on non-standard conceptions of provability which would likely not have been accepted by Hilbert (see also Resnik 1974, Auerbach 1992 and Steiner 1991)[^auerbach-1992][^resnik-1974][^steiner-1991].

Smorynski (1977) has argued that already the first incompleteness theorem defeats Hilbert’s Program. Hilbert’s aim was not merely to show that formalized mathematics is consistent, but to do so in a specific way by showing that ideal mathematics can never lead to conclusions not in accord with real mathematics. Thus, to succeed, ideal mathematics must be *conservative* over the real part: whenever formalized ideal mathematics proves a real formula $P, P$ itself (or the finitary proposition it expresses) must be finitarily provable. For Smorynski the real formulas include not just numerical equalities and combinations thereof, but also general formulas with free variables but without unbounded quantifiers.

Now Gödel’s first incompleteness theorem (G1) states that for any sufficiently strong, consistent formal theory $S$ there is a sentence $G_S$ which is true but not derivable in $S$. $G_S$ is a real sentence according to Smorynski’s definition. Now consider a theory $T$ which formalizes ideal mathematics and its subtheory $S$ which formalizes real mathematics. $S$ satisfies the conditions of G1 and hence $S$ does not derive $G_S$. Yet, $T$, being a formalization of all of mathematics (including what is required to see that $G_S$ is true), does derive $G_S$. Hence, we have a real statement which is provable in ideal mathematics and not in real mathematics.

Detlefsen (1986, Appendix; see also 1990) has defended Hilbert’s Program against this argument as well. Detlefsen argues that “Hilbertian” instrumentalism escapes the argument from G1 by denying that ideal mathematics must be conservative over the real part; all that is required is real-soundness. Hilbertian instrumentalism requires only that the ideal theory not prove anything which is in conflict with the real theory; it is not required that it prove *only* real statements which the real theory also proves.

Franks (2009) has provided a related defense and re-evaluation of Hilbert’s project, and McCarthy (2016) an alternative approach to the provability of consistency and G2 due to Gödel himself. Kripke (forthcoming) shows how Hilbert’s own approach to consistency proofs naturally lead to Gödelian incompleteness. Santos et al. (forthcoming), expanding on work by Artemov (2020), argue that a “partial finitism” allows for consistency proofs compatible with G2, and is in line with Hilbert’s own post-Gödelian views. See also Schirn and Niebergall (2001) and Schirn (2019) for related proposals. Zach (2004) provides historical detail on the issue of conservativity and consistency in Hilbert’s program. See the entries on Gödel and Gödel’s incompleteness theorem, as well as Cheng (2021), for further discussion on Gödel’s theorems and consistency proofs.

## 5. Revised Hilbert Programs

Even if no finitary consistency proof of arithmetic can be given, the question of finding consistency proofs is nevertheless of value: the methods used in such proofs, although they must go beyond Hilbert’s original sense of finitism, might provide genuine insight into the constructive content of arithmetic and stronger theories. What Gödel’s result showed was that there can be no absolute consistency proof of all of mathematics; hence work in proof theory after Gödel concentrated on relative results, both: relative to the system for which a consistency proof was given, and relative to the proof methods used.

Reductive proof theory in this sense has followed two traditions: the first, mainly carried out by proof theorists following Gentzen and Schütte, has pursued a program of what is called *ordinal analysis*, and is exemplified by Gentzen’s first consistency proof of $\PA$ by induction up to $\varepsilon_0 . \varepsilon_0$ is a certain transfinite (though countable) ordinal, however, “induction up to $\varepsilon_0$” in the sense used here is not a genuinely transfinite procedure. Ordinal analysis does not operate with infinite ordinal numbers, but rather with *ordinal notation systems* which themselves can be formalized in very weak (essentially, finitary) systems. An ordinal analysis of a system $T$ is given if: (a) one can produce an ordinal notation system which mimics the ordinals less than some ordinal $\alpha_T$ so that (b) it can be proved finitarily that the formalization $TI(\alpha_T)$ of the principle of induction up to $\alpha_T$ implies the consistency of $T$ (i.e., $S \vdash TI(\alpha_T)\rightarrow Con_T)$ and (c) $T$ proves $TI(\beta)$ for all $\beta \lt \alpha_T$ ($S$ is a theory formalizing finitary metamathematics and is generally a weak sub-theory of $T)$. To have any foundational significance it is also required that one can give a constructive argument for transfinite induction up to $\alpha_T$. As mentioned above, this was done for by Gentzen and Takeuti for $\varepsilon_0$, the proof theoretic ordinal of $\PA$, but becomes more difficult and of progressively questionable philosophical significance for stronger theories. See the entry on proof theory for a survey of Gentzen’s consistency proof, Mancosu et al. 2021 for an accessible textbook presentation, and Thomas-Bolduc and Darnell 2022 on Takeuti’s well-ordering proof.

A philosophically more satisfactory continuation of Hilbert’s Program in proof theoretic terms has been suggested by Kreisel (1983; 1968) and Feferman (Feferman, 1988; Feferman, 1993a)[^feferman-1988][^feferman-1993a]. This work proceeds from a wider conception of Hilbert’s Program as an attempt to justify ideal mathematics by restricted means. In this conception, the aim of Hilbert’s proof theory was to show that, at least as far as a certain class of real propositions is concerned, ideal mathematics does not go beyond real mathematics. A finitary consistency proof of the kind envisaged by Hilbert would have accomplished this: if ideal mathematics proves a real proposition, then this proposition is already provable by real (i.e., finitary) methods. In a sense this *reduces* ideal mathematics to real mathematics. A *proof-theoretic reduction* of a theory $T$ to a theory $S$ shows that, as far as a certain class of propositions is concerned, if $T$ proves a proposition, then $S$ proves it too, and the proof of this fact is itself finitary. Hilbert’s proof theoretic program can then be seen to be a search for a proof theoretic reduction of all of mathematics to finitary mathematics; in a relativized program one looks for reductions of theories weaker than all of classical mathematics to theories often stronger than finitary mathematics. Proof theorists have obtained a number of such results, including reductions of theories which on their face require a significant amount of ideal mathematics for their justification (e.g., subsystems of analysis) to finitary systems. (Feferman, 1993b)[^feferman-1993b] has used such results in combination with other results that show that most, if not all, of scientifically applicable mathematics can be carried out in systems for which such reductions are available to argue against the indispensability argument in the philosophy of mathematics. The philosophical significance of such proof theoretic reductions is currently the subject of debate (Hofweber, 2000; Feferman, 2000)[^feferman-2000][^hofweber-2000].

The program of so-called reverse mathematics developed by, in particular, Friedman and Simpson, is another continuation of Hilbert’s program. In the face of Gödel’s results showing that not all of classical mathematics can be reduced to the finitary, they seek to answer the question: how much of classical mathematics can be so reduced? Reverse mathematics seeks to give a precise answer to this question by investigating which theorems of classical mathematics are provable in weak subsystems of analysis which are reducible to finitary mathematics (in the sense discussed in the preceding paragraph). A typical result is that the Hahn-Banach theorem of functional analysis is provable in a theory known as $WKL_0$ (for “weak König lemma”); $WKL_0$ is conservative over $\PRA$ for $\Pi^{0}_2$ sentences (i.e., sentences of the form $\forall x\exists yA(x, y)$. (See Simpson 1988 for an overview and Simpson 1999 for a technical treatment.)[^simpson-1988][^simpson-1999]

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=hilbert-program). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/hilbert-program/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=hilbert-program&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/hilbert-program/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

[Please contact the author with suggestions.]

## Related Entries

Brouwer, Luitzen Egbertus Jan | epsilon calculus | Frege, Gottlob: controversy with Hilbert | Gödel, Kurt | Gödel, Kurt: incompleteness theorems | Hilbert, David | mathematics, philosophy of: formalism | mathematics, philosophy of: intuitionism | *Principia Mathematica* | proof theory | proof theory: development of | Russell, Bertrand

[^an-2006]: An extended version of the first revision of this entry can be found in Zach (2006).

[^ackermann-1924]: Ackermann, Wilhelm, 1924, “Begründung des ‘tertium non datur’ mittels der Hilbertschen Theorie der Widerspruchsfreiheit,” *Mathematische Annalen*, 93: 1–36.

[^artemov-2020]: Artemov, Sergei, 2020, “The provability of consistency,” arXiv:1902.07404.

[^auerbach-1992]: Auerbach, David, 1992, “How to say things with formalisms,” in *Proof, Logic, and Formalization*, Michael Detlefsen, ed., London: Routledge, 77–93.

[^avigad-2003]: Avigad, Jeremy, 2003, “Number theory and elementary arithmetic,” *Philosophia Mathematica*, 11: 257–284.

[^bernays-1922]: Bernays, Paul, 1922, “Über Hilberts Gedanken zur Grundlegung der Arithmetik,” *Jahresbericht der Deutschen Mathematiker-Vereinigung*, 31: 10–19. English translation in Mancosu (1998a, 215–222).

[^bernays-1923]: –––, 1923, “Erwiderung auf die Note von Herrn Aloys Müller: Über Zahlen als Zeichen,” *Mathematische Annalen*, 90: 159–63. English translation in Mancosu (1998a, 223–226).

[^bernays-1928a]: –––, 1928a, “Über Nelsons Stellungnahme in der Philosophie der Mathematik,” *Die Naturwissenschaften*, 16: 142–45.

[^bernays-1928b]: –––, 1928b,, “Zusatz zu Hilberts Vortrag über ‘Die Grundlagen der Mathematik,’” *Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg*, 6: 88–92. English translation in: van Heijenoort (1967, 485–489).

[^bernays-1930]: –––, 1930, “Die Philosophie der Mathematik und die Hilbertsche Beweistheorie,” *Blätter für deutsche Philosophie*, 4: 326–67. Reprinted in Bernays (1976, 17–61). English translation in Mancosu (1998a, 234–265).

[^bernays-1976]: –––, 1976, *Abhandlungen zur Philosophie der Mathematik*, Darmstadt: Wissenschaftliche Buchgesellschaft.

[^cheng-2021]: Cheng, Yong, 2021, “Current Research on Gödel’s Incompleteness Theorems,” *Bulletin of Symbolic Logic*, 27(2): 113–67.

[^dean-2015]: Dean, Walter, 2015, “Arithmetical reflection and the provability of soundness,” *Philosophia Mathematica*, 23: 31–64, doi:10.1093/philmat/nku026

[^detlefsen-1979]: Detlefsen, Michael, 1979, “On interpreting Gödel’s second theorem,” *Journal of Philosophical Logic*, 8: 297–313. Reprinted with a postscript in Shanker (1988, 131–154).

[^detlefsen-1986]: –––, 1986, *Hilbert’s Program*, Dordrecht: Reidel.

[^detlefsen-1990]: –––, 1990, “On an alleged refutation of Hilbert’s program using Gödel’s first incompleteness theorem,” *Journal of Philosophical Logic*, 19: 343–377.

[^detlefsen-2001]: –––, 2001, “What does Gödel’s second theorem say?,” *Philosophia Mathematica*, 9: 37–71.

[^eder-nd]: Eder, Günther, forthcoming, “The Bernays-Müller debate,” *HOPOS: The Journal of the International Society for the History of Philosophy of Science*.

[^ewald-1996]: Ewald, William Bragg (ed.), 1996, *From Kant to Hilbert. A Source Book in the Foundations of Mathematics*, vol. 2, Oxford: Oxford University Press.

[^ewald-2013]: Ewald, William Bragg and Wilfried Sieg (eds.), 2013, *David Hilbert’s Lectures on the Foundations of Arithmetic and Logic 1917–1933*, Berlin and Heidelberg: Springer.

[^feferman-1988]: Feferman, Solomon, 1988, “Hilbert’s Program relativized: Proof-theoretical and foundational reductions,” *Journal of Symbolic Logic*, 53(2): 364–284.

[^feferman-1993a]: –––, 1993a, “What rests on what? The proof-theoretic analysis of mathematics,” in *Philosophy of Mathematics. Proceedings of the Fifteenth International Wittgenstein-Symposium, Part 1*, Johannes Czermak, ed., Vienna: Hölder-Pichler-Tempsky, 147–171. Reprinted in Feferman (1998, Ch. 10, 187–208).

[^feferman-1993b]: –––, 1993b, “Why a little bit goes a long way: Logical foundations of scientifically applicable mathematics,” *PSA 1992*, 2: 442–455. Reprinted in Feferman (1998, Ch. 14, 284–298). [[Preprint available online](http://math.stanford.edu/~feferman/papers/psa1992.pdf)].

[^feferman-1998]: –––, 1998, *In the Light of Logic*, Oxford: Oxford University Press.

[^feferman-2000]: –––, 2000, “Does reductive proof theory have a viable rationale?.” *Erkenntnis*, 53: 63–96.

[^franks-2009]: Franks, Curtis, 2009, *The Autonomy of Mathematical Knowledge: Hilbert’s Program Revisited*, Cambridge: Cambridge University Press.

[^ganea-2010]: Ganea, Mihai, 2010, “Two (or three) notions of finitism,” *Review of Symbolic Logic*, 3: 119–144.

[^gentzen-1936]: Gentzen, Gerhard, 1936,, “Die Widerspruchsfreiheit der reinen Zahlentheorie,” *Mathematische Annalen*, 112: 493–565. English translation in Gentzen (1969, 132–213).

[^gentzen-1969]: –––, 1969, *The Collected Papers of Gerhard Gentzen*, Amsterdam: North-Holland.

[^giaquinto-1983]: Giaquinto, Marcus, 1983, “Hilbert’s philosophy of mathematics,” *British Journal for Philosophy of Science*, 34: 119–132.

[^gödel-1931]: Gödel, Kurt, 1931, “Über formal unentscheidbare Sätze der *Principia Mathematica* und verwandter Systeme I,” *Monatshefte für Mathematik und Physik*, 38: 173–198. Reprinted and translated in Gödel (1986, 144–195).

[^gödel-1958]: –––, 1958, “Über eine bisher noch nicht benütze Erweiterung des finiten standpunktes,” *Dialectica*, 280–287. Reprinted and translated in Gödel (1990, 217–251).

[^gödel-1986]: –––, 1986, *Collected Works*, vol. 1, Oxford: Oxford University Press.

[^gödel-1990]: –––, 1990, *Collected Works*, vol. 2, Oxford: Oxford University Press.

[^gödel-2003]: –––, 2003, *Collected Works*, vol. 4, Oxford: Oxford University Press.

[^hallett-1990]: Hallett, Michael, 1990, “Physicalism, reductionism and Hilbert,” in *Physicalism in Mathematics*, Andrew D. Irvine, ed., Dordrecht: Reidel, 183–257.

[^hilbert-1899]: Hilbert, David, 1899, “Grundlagen der Geometrie,” in *Festschrift zur Feier der Enthüllung des Gauss-Weber-Denkmals in Göttingen*, Leipzig: Teubner, 1–92, 1st ed.

[^hilbert-1900a]: –––, 1900a, “Mathematische Probleme,” *Nachrichten von der Königlichen Gesellschaft der Wissenschaften zu Göttingen, Math.-Phys. Klasse*, 253–297. Lecture given at the International Congress of Mathematicians, Paris, 1900. Partial English translation in Ewald (1996, 1096–1105).

[^hilbert-1900b]: –––, 1900b, “Über den Zahlbegriff,” *Jahresbericht der Deutschen Mathematiker-Vereinigung*, 8: 180-184. English translation in Ewald (1996, 1089–1096).

[^hilbert-1905]: –––, 1905, “Über die Grundlagen der Logik und der Arithmetik,” in *Verhandlungen des dritten Internationalen Mathematiker-Kongresses in Heidelberg vom 8. bis 13. August 1904*, A. Krazer, ed., Leipzig: Teubner, 174–85. English translation in van Heijenoort (1967, 129–138).

[^hilbert-1918a]: –––, 1918a, “Axiomatisches Denken,” *Mathematische Annalen*, 78: 405–15. Lecture given at the Swiss Society of Mathematicians, 11 September 1917. Reprinted in Hilbert (1935, 146–156). English translation in Ewald (1996, 1105–1115).

[^hilbert-1918b]: –––, 1918b, “Prinzipien der Mathematik,” Lecture notes by Paul Bernays. Winter-Semester 1917/18. Typescript. Bibliothek, Mathematisches Institut, Universität Göttingen. Edited in Ewald and Sieg (2013, 59–221)..

[^hilbert-1922a]: –––, 1922a, “Grundlagen der Mathematik,” Vorlesung, Winter-Semester 1921/22. Lecture notes by Paul Bernays. Typescript. Bibliothek, Mathematisches Institut, Universität Göttingen. Edited in Ewald and Sieg (2013, 431–527).

[^hilbert-1922b]: –––, 1922b, “Neubegründung der Mathematik: Erste Mitteilung,” *Abhandlungen aus dem Seminar der Hamburgischen Universität*, 1: 157–177. Series of talks given at the University of Hamburg, July 25–27, 1921. Reprinted with notes by Bernays in Hilbert (1935, 157–177). English translation in Mancosu (1998a, 198–214) and Ewald (1996, 1115–1134).

[^hilbert-1923]: –––, 1923, “Die logischen Grundlagen der Mathematik,” *Mathematische Annalen*, 88: 151–165. Lecture given at the Deutsche Naturforscher-Gesellschaft, September 1922. Reprinted in Hilbert (1935, 178–191). English translation in Ewald (1996, 1134–1148).

[^hilbert-1926]: –––, 1926, “Über das Unendliche,” *Mathematische Annalen*, 95: 161–190. Lecture given Münster, 4 June 1925. English translation in van Heijenoort (1967, 367–392).

[^hilbert-1928]: –––, 1928, “Die Grundlagen der Mathematik,” *Abhandlungen aus dem Seminar der Hamburgischen Universität*, 6: 65–85. Reprinted in Ewald and Sieg (2013, 917–942). English translation in van Heijenoort (1967, 464–479).

[^hilbert-1929]: –––, 1929, “Probleme der Grundlegung der Mathematik,” *Mathematische Annalen*, 102: 1–9. Lecture given at the International Congress of Mathematicians, 3 September 1928. Reprinted in Ewald and Sieg (2013, 954–966). English translation in Mancosu (1998a, 227–233).

[^hilbert-1931a]: –––, 1931a, “Beweis des Tertium non datur,” *Nachrichten der Gesellschaft der Wissenschaften zu Göttingen. Math.-phys. Klasse*, 120-125. Reprinted in Ewald and Sieg (2013, 967–982).

[^hilbert-1931b]: –––, 1931b, “Die Grundlegung der elementaren Zahlenlehre,” *Mathematische Annalen*, 104: 485–494. Reprinted in Hilbert (1935, 192–195) and Ewald and Sieg (2013, 983–990). English translation in Ewald (1996, 1148–1157).

[^hilbert-1935]: –––, 1935, *Gesammelte Abhandlungen*, vol. 3, Berlin: Springer.

[^hilbert-1992]: –––, 1992, *Natur und mathematisches Erkennen*, Basel: Birkhäuser. Vorlesungen, 1919–20.

[^hilbert-1928-2]: Hilbert, David and Ackermann, Wilhelm, 1928, *Grundzüge der theoretischen Logik*, Berlin: Springer.

[^hilbert-1923-2]: Hilbert, David and Bernays, Paul, 1923, “Logische Grundlagen der Mathematik,” Vorlesung, Winter-Semester 1922-23. Lecture notes by Paul Bernays, with handwritten notes by Hilbert. Hilbert-Nachlaß, Niedersächsische Staats- und Universitätsbibliothek, Cod. Ms. Hilbert 567.

[^hilbert-1934]: –––, 1934, *Grundlagen der Mathematik*, vol. 1, Berlin: Springer.

[^hilbert-1939]: –––, 1939, *Grundlagen der Mathematik*, vol. 2, Berlin: Springer.

[^hofweber-2000]: Hofweber, Thomas, 2000, “Proof-theoretic reduction as a philosopher’s tool,” *Erkenntnis*, 53: 127–146.

[^ignjatovic-1994]: Ignjatovic, Aleksandar, 1994, “Hilbert’s program and the omega rule,” *Journal of Symbolic Logic*, 59: 322–343.

[^incurvati-2019]: Incurvati, Luca, 2019, “On the concept of finitism,” *Synthese*, 192: 2413–2436.

[^kish-bar-on-2021]: Kish-Bar-On, Kati, 2021, “Towards a New Philosophical Perspective on Hermann Weyl’s Turn to Intuitionism,” *Science in Context*, 34: 51–68.

[^kitcher-1976]: Kitcher, Philip, 1976, “Hilbert’s epistemology,” *Philosophy of Science*, 43: 99–115.

[^kreisel-1960]: Kreisel, Georg, 1960, “Ordinal logics and the characterization of informal notions of proof,” in *Proceedings of the International Congress of Mathematicians. Edinburgh, 14–21 August 1958*, J. A. Todd, ed., Cambridge: Cambridge University Press, 289–299.

[^kreisel-1968]: –––, 1968, “A survey of proof theory,” *Journal of Symbolic Logic*, 33: 321–388.

[^kreisel-1970]: –––, 1970, “Principles of proof and ordinals implicit in given concepts,” in *Intuitionism and Proof Theory*, A. Kino, J. Myhill, and R. E. Veseley, eds., Amsterdam: North-Holland.

[^kreisel-1983]: –––, 1983, “Hilbert’s programme,” in *Philosophy of Mathematics*, Paul Benacerraf and Hilary Putnam, eds., Cambridge: Cambridge University Press, 207–238, 2nd ed.

[^kripke-nd]: Kripke, Saul A., forthcoming, “The Collapse of the Hilbert Program: A Variation on the Gödelian Theme,” *Bulletin of Symbolic Logic*.

[^mancosu-1998a]: Mancosu, Paolo (ed.), 1998a, *From Brouwer to Hilbert. The Debate on the Foundations of Mathematics in the 1920s*, Oxford: Oxford University Press.

[^mancosu-1998b]: Mancosu, Paolo, 1998b, “Hilbert and Bernays on Metamathematics,” in (Mancosu, 1998a), 149–188. Reprinted in Mancosu (2010).

[^mancosu-1999]: –––, 1999, “Between Russell and Hilbert: Behmann on the foundations of mathematics,” *Bulletin of Symbolic Logic*, 5(3): 303–330. Reprinted in Mancosu (2010).

[^mancosu-2010]: –––, 2010, *The Adventure of Reason: Interplay Between Philosophy of Mathematics and Mathematical Logic, 1900–1940*, Oxford: Oxford University Press.

[^mancosu-2021]: Mancosu, Paolo, Sergio Galvan, and Richard Zach, 2021, *An Introduction to Proof Theory: Normalization, Cut-Elimination, and Consistency Proofs*. Oxford: Oxford University Press.

[^mancosu-2002]: Mancosu, Paolo and Ryckman, Thomas, 2002, “Mathematics and phenomenology: The correspondence between O. Becker and H. Weyl,” *Philosophia Mathematica*, 10: 130–202. Reprinted in Mancosu (2010).

[^mccarthy-2016]: McCarthy, T., 2016, “Gödel’s third incompleteness theorem,” *Dialectica* 70: 87–112.

[^parsons-1998]: Parsons, Charles, 1998, “Finitism and intuitive knowledge,” in *The Philosophy of Mathematics Today*, Matthias Schirn, ed., Oxford: Oxford University Press, 249–270.

[^parsons-2007]: –––, 2007, *Mathematical Thought and its Objects*, Cambridge: Cambridge University Press.

[^patton-2014]: Patton, Lydia, 2014, “Hilbert’s objectivity,” *Historia Mathematica*, 41(2): 188–203.

[^peckhaus-1990]: Peckhaus, Volker, 1990, *Hilbertprogramm und Kritische Philosophie*, Göttingen: Vandenhoeck und Ruprecht.

[^poincaré-1906]: Poincaré, Henri, 1906, “Les mathématiques et la logique,” *Revue de métaphysique et de morale*, 14: 294–317. English translation in Ewald (1996, 1038–1052).

[^resnik-1974]: Resnik, Michael D., 1974, “On the philosophical significance of consistency proofs,” *Journal of Philosophical Logic*, 3: 133–47.

[^resnik-1980]: –––, 1980, *Frege and the Philosophy of Mathematics*, Ithaca: Cornell University Press.

[^santos-nd]: Santos, Paulo Guilherme, Wilfried Sieg, and Reinhard Kahle, forthcoming, “A New Perspective on Completeness and Finitist Consistency,” *Journal of Logic and Computation*.

[^schirn-2019]: Schirn, Matthias, 2019, “The finite and the infinite: On Hilbert’s formalist approach before and after Gödel’s incompleteness theorems,” *Logique et Analyse*, 245: 1–34.

[^schirn-2001]: Schirn, Matthias, and Karl-Georg Niebergall, 2001, “Extensions of the finitist point of view,” *History and Philosophy of Logic*, 22(3): 135–61.

[^shanker-1988]: Shanker, Stuart G., 1988, *Gödel’s Theorem in Focus*, London: Routledge.

[^sieg-1990]: Sieg, Wilfried, 1990, “Reflections on Hilbert’s program,” in *Acting and Reflecting*, Wilfried Sieg, ed., Dordrecht: Kluwer, 171–82. Reprinted in Sieg (2013).

[^sieg-1999]: –––, 1999, “Hilbert’s programs: 1917–1922,” *Bulletin of Symbolic Logic*, 5(1): 1–44. Reprinted in Sieg (2013).

[^sieg-2013]: –––, 2013, *Hilbert’s Programs and Beyond*, New York: Oxford University Press.

[^simpson-1988]: Simpson, Stephen G., 1988, “Partial realizations of Hilbert’s program,” *Journal of Symbolic Logic*, 53(2): 349–363.

[^simpson-1999]: –––, 1999, *Subsystems of Second Order Arithmetic*, Berlin: Springer.

[^smorynski-1977]: Smorynski, Craig, 1977, “The incompleteness theorems,” in *Handbook of Mathematical Logic*, Jon Barwise, ed., Amsterdam: North-Holland, 821–865.

[^steiner-1975]: Steiner, Mark, 1975, *Mathematical Knowledge*, Ithaca: Cornell University Press.

[^steiner-1991]: –––, 1991, “Review of *Hilbert’s Program: An Essay on Mathematical Instrumentalism* (Detlefsen, 1986),” *Journal of Philosophy*, 88(6): 331–336.

[^tait-1981]: Tait, W. W., 1981, “Finitism,” *Journal of Philosophy*, 78: 524–546. Reprinted in Tait (2005a, 21–42).

[^tait-2002]: –––, 2002, “Remarks on finitism,” in *Reflections on the Foundations of Mathematics. Essays in Honor of Solomon Feferman*, Wilfried Sieg, Richard Sommer, and Carolyn Talcott, eds., Association for Symbolic Logic, LNL 15. Reprinted in Tait (2005a, 43–53). [[Preprint available online](https://www.researchgate.net/publication/2391294_Remarks_On_Finitism)]

[^tait-2005a]: –––, 2005a, *The Provenance of Pure Reason: Essays in the Philosophy of Mathematics and its History*, New York: Oxford University Press.

[^tait-2005b]: –––, 2005b, “Appendix to Chapters 1 and 2,” in Tait (2005a, 54–60).

[^tait-2019]: –––, 2019, “What Hilbert and Bernays meant by ‘finitism,’” in *Philosophy of Logic and Mathematics: Proceedings of the 41st International Ludwig Wittgenstein Symposium*, Gabriele M. Mras, Paul Weingartner, and Bernhard Ritter (eds.), Berlin: De Gruyter, 249–62.

[^takeuti-1987]: Takeuti, Gaisi, 1987, *Proof Theory* (Studies in Logic: 81), Amsterdam: North-Holland, 2nd edition.

[^thomas-bolduc-2022]: Thomas-Bolduc, Aaron, and Eamon Darnell, 2022, “Takeuti’s well-ordering proof: An accessible recontruction,” *The Australasian Journal of Logic*, 19(1): 1–31.

[^heijenoort-1967]: van Heijenoort, Jean (ed.), 1967, *From Frege to Gödel. A Source Book in Mathematical Logic, 1897–1931*, Cambridge, Mass.: Harvard University Press.

[^neumann-1927]: von Neumann, Johann, 1927, “Zur Hilbertschen Beweistheorie,” *Mathematische Zeitschrift*, 26: 1–46.

[^weyl-1921]: Weyl, Hermann, 1921, “Über die neue Grundlagenkrise der Mathematik,” *Mathematische Zeitschrift*, 10: 37–79. Reprinted in Weyl (1968, 143–180). English translation in Mancosu (1998a, 86–118).

[^weyl-1925]: –––, 1925, “Die heutige Erkenntnislage in der Mathematik,” *Symposion*, 1: 1–23. Reprinted in: Weyl (1968, 511–42). English translation in: Mancosu (1998a, 123–42).

[^weyl-1928]: –––, 1928, “Diskussionsbemerkungen zu dem zweiten Hilbertschen Vortrag über die Grundlagen der Mathematik,” *Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg*, 6: 86–88. English translation in van Heijenoort (1967, 480–484).

[^weyl-1968]: –––, 1968, *Gesammelte Abhandlungen*, vol. 1, Berlin: Springer Verlag.

[^zach-1999]: Zach, Richard, 1999, “Completeness before Post: Bernays, Hilbert, and the development of propositional logic,” *Bulletin of Symbolic Logic*, 5(3): 331–366.

[^zach-2003]: –––, 2003, “The practice of finitism. Epsilon calculus and consistency proofs in Hilbert’s Program,” *Synthese*, 137: 211–259.

[^zach-2004]: –––, 2004, “Hilbert’s ‘Verunglückter Beweis,’ the first epsilon theorem, and consistency proofs,” *History and Philosophy of Logic*, 25: 79–94.

[^zach-2006]: –––, 2006, “Hilbert’s program then and now,” in: Dale Jacquette, ed., *Philosophy of Logic.* Handbook of the Philosophy of Science, vol. 5. Amsterdam: Elsevier, 411–447.
