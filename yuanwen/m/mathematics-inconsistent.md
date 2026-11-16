# Inconsistent Mathematics
**First published Tue Jul 2, 1996; substantive revision Wed Nov 30, 2022**

*Mortensen, Chris*

Inconsistent mathematics is the study of the mathematical theories that result when classical mathematical axioms are asserted within the framework of a (non-classical) logic which can tolerate the presence of a contradiction without turning every sentence into a theorem.

## 1. Foundations of Mathematics

Inconsistent Mathematics began historically with foundational considerations. Frege and Russell proposed to found their mathematics on the naive principle of set theory: to every predicate is a set. But the naive principle leads rapidly to a proof of the existence of the Russell set, the set of all sets not members of themselves, which both is and is not a member of itself. This and other set-theoretic paradoxes noted by Russell and others led to attempts to produce consistent set theories as a foundation for mathematics. Perhaps the best known of these was Zermelo-Fraenkel set theory ZF. But ZF and others such as NBG and the like were in various ways ad hoc, having to include multiple independent principles instead of a single simple comprehension axiom. Hence, a number of people including da Costa (1974), Brady (1971, 1989)[^brady-1971][^brady-1989], Priest, Routley, & Norman (1989, pp. 152, 498), considered it preferable to retain the full power of the natural comprehension principle, and tolerate a degree of inconsistency in set theory. Brady, in particular, has extended, streamlined and simplified these results on naive set theory in his book (2006). For a clear account see also Restall’s review (2007).

These constructions require, of course, that one dispense *at least* with that principle of Boolean logic *ex contradictione quodlibet* (ECQ) (from a contradiction every proposition may be deduced, also called explosion). In passing, C.I.Lewis showed that ECQ follows by a simple argument from the principle disjunctive syllogism (DS) (from *A*-or-*B* and not-*A* deduce *B*). So DS has to go too. Obviously, ECQ trivialises any inconsistent theory (triviality = every sentence is provable). Non-triviality should be regarded as a constraint on interesting theories: a trivial theory is useless for mathematical calculation, since a trivial theory does not distinguish principles in the theory from their negations. Similarly, considerable debate (Burgess 1981, Mortensen 1983)[^burgess-1981][^mortensen-1983], made it clear that dispensing with DS was not so counter-intuitive, especially when a plausible story emerged about the special conditions under which DS continues to hold.

It should also be noted that Brady’s construction of inconsistent naive set theory opens the door to a revival of Frege-Russell logicism (briefly, that mathematics reduces to logic.) Logicism was widely held, even by Frege himself, to have been badly damaged by the Russell Paradox. If the Russell Contradiction does not spread, then there is no obvious reason why one cannot hold that naive set theory provides an adequate foundation for mathematics, and that naive set theory is deducible from logic via the naive comprehension schema. The only change needed is a move to an inconsistency-tolerant logic. Even more radically, Weber, in related papers (2010), (2012), (2013), has taken the inconsistency to be a positive virtue, since it enables us to settle several questions that were left open by Cantor, namely, that the well-ordering theorem and the axiom of choice are provable, and that the Continuum Hypothesis is false (2012, 284). Some of these come out provably both true and false; wherein Weber is concerned to advance proofs of the *classical recapture*, which is the project of showing that traditional results remain provable (2010, 72). This is invigorating new ground. Weber also showed something essential to this project, namely, that Cantor’s Theorem continues to hold; that is, it does not depend on overly-strong logical principles which are contested by paraconsistentists. Retaining Cantor’s Theorem is important in Weber’s view, since different orders of infinity remain available in inconsistent set theory.

In addition, mathematics contains machinery for a metalanguage, that is for talking about mathematics itself. This includes the concepts: (i) names for mathematical statements and other parts of syntax, (ii) self-reference, (iii) proof and (iv) truth. Gödel’s contribution to the philosophy of mathematics was to show that the first three of these can be rigorously expressed in arithmetical theories, albeit in theories which are either inconsistent or incomplete. The possibility of a well-structured example of the former of these two alternatives, namely inconsistency, was not taken seriously, again because of belief in ECQ. However, in addition natural languages seem to have their own truth predicate. Combined with self-reference this produces the Liar paradox, “This sentence is false”, an inconsistency. Priest (1987)[^priest-1987] and Priest, Routley and Norman (1989, p. 154) argued that the Liar had to be regarded as a statement both true and false, a true contradiction. This represents another argument for studying inconsistent theories, namely the claim that some contradictions are true, also known as *dialetheism*. Kripke (1975)[^kripke-1975] proposed instead to model a truth predicate differently, in a consistent incomplete theory. We see below that incompleteness and inconsistency are closely related.

To simplify the motivation, mathematics, like many another science, encounters anomalies, puzzles and paradoxes. Paradoxes typically appear in the form of contradictions where there are grounds for accepting incompatible sides of the contradiction. Mathematics progresses at least in part by eliminating anomalies in favour of consistent reconstructions. This has typically been the method of addressing anomalies, and it is facilitated by noticing that the contradictions emerge in the foundations of mathematics. But it was noticed in the later twentieth century that there is another way, namely accept the contradiction and develop mathematical theories containing both sides of the contradiction. This would be impossible if the contradictory theory was erected on a logical foundation containing the Boolean principle Ex Contradictione Quodlibet ECQ, from a contradiction everything follows. So ECQ has to be abandoned, but fortunetely that proves possible, indeed mathematically straightforward. What remains is a rich field, of novel mathematical applications interesting in their own right, which sidestep the vexing questions of which foundational principles to adopt, by developing contradictions in areas of mathematics such as number theory or analysis which are far from foundations. This is inconsistent mathematics.

## 2. Arithmetic

But these remarks have been about foundations, and mathematics is not its foundations. Hence there is a further independent motive, to see what mathematical structure remains *wherever* the constraint of consistency is relaxed. But it would be wrong to regard this as in any way a repudiation of the structures studied in classical mathematics: inconsistent structures represent an *addition* to known structures.

Robert K. Meyer (1976)[^meyer-1976] seems to have been the first to think of an inconsistent arithmetical theory. At this point, he was more interested in the fate of a consistent theory, his relevant arithmetic R#. This amounts to the axioms for Peano arithmetic, with a base of the quantified relevant logic RQ, and Meyer hoped that the weaker base of relevant logic would allow more models. He was right. There proved to be a whole class of inconsistent arithmetical theories; see Meyer and Mortensen (1984), for example. In a parallel with the above remarks on rehabilitating logicism, Meyer argued that these arithmetical theories provide the basis for a revived Hilbert Program. Hilbert’s program was the project of rigorously formalising mathematics and proving its consistency by simple finitary/inductive procedures. It was widely held to have been seriously damaged by Gödel’s Second Incompleteness Theorem, according to which the consistency of arithmetic was unprovable within arithmetic itself. But a consequence of Meyer’s construction was that within his arithmetic R# it was demonstrable by finitary means that whatever contradictions there might happen to be, they could not adversely affect any numerical calculations. Hence Hilbert’s goal of conclusively demonstrating that mathematics is trouble-free proves largely achievable as long as inconsistency-tolerant logics are used.

The arithmetical models used by Meyer and Mortensen later proved to allow inconsistent representation of the truth predicate. They also permit representation of structures beyond natural number arithmetic, such as rings and fields, including their order properties. Axiomatisations were also provided. Recently, the finite inconsistent arithmetical collapse models, a strictly larger class than those studied by Meyer and Mortensen, have been completely characterised by Graham Priest. Collapse models are obtained from classical models by collapsing the domain down to congruence classes generated by various congruence relations. When members of the same congruence class are identified, the theories produced are inconsistent. For example, Meyer’s initial construction collapsed the integers under the congruence *modulo 2*. This puts 0 and 2 in the same congruence class, so that in a suitable three-valued logic, both 0=2 and not-(0=2) hold. Priest showed that these models take a certain general form, see Priest (1997)[^priest-1997] and (2000). Strictly speaking, Priest went a little too far in including “clique models”. This was corrected by Paris and Pathmanathan (2006), and extended into the infinite by Paris and Sirokfskich (2008). Even more recently, Tedder (2015)[^tedder-2015] obtained axiomatisations for the class of finite collapse models with a different background logic, Avron’s A3.

## 3. Analysis

One could hardly ignore the examples of analysis and its special case, the calculus. For a model-theoretic approach to these see Mortensen (1990, 1995)[^mortensen-1990][^mortensen-1995].

Now Meyer’s original approach to the natural numbers, that is R#, was axiomatic rather than model-theoretic. The axiomatic approach has also been taken in *analysis* by McKubre-Jordens and Weber (2012)[^weber-2012]. In axiomatising analysis with a base of paraconsistent logic, their paper pushes Meyer’s approach to arithmetic via R# a long way further. These same authors (2017) rework the theory of integration as it was in Archimedes’ hands, which employs the method of exhaustion, using paraconsistent reasoning. This gives a result “up to inconsistency”, which means that one is able to prove “Classical result or contradiction”. The classical result can be then seen to be recapturable by the classical move disjunctive syllogism applied to the classically-false (inconsistent) second disjunct.

It is certainly important and worthy to pursue this direction, but a mild caution is entered here: the axiomatic project is a bit different from inconsistent mathematics. As noted earlier, Meyer in this phase was consistentist – he sought a consistent theory with an inconsistency-tolerant logic. With similar motivation, he was also concerned to try to settle what he called “the gamma problem”, which was essentially the question of whether the axiomatic theory R# could be shown to contain classical Peano arithmetic as a sub-theory. If this were so, then his proof of nontriviality for R# would immediately yield a new proof of the negation consistency of classical Peano arithmetic! Note that this would not be contrary to Godel’s Second Theorem, since presumably the proof of the gamma result would not be confined to finitary techniques. (In the case of Meyer’s theory, it turned out to be not so.)

There have proved to be many places throughout analysis where there are distinctive inconsistent insights. The examples in the remainder of this section are drawn from Mortensen (1995)[^mortensen-1995]. For example: (1) Robinson’s (1974)[^robinson-1974] non-standard analysis was based on infinitesimals, quantities smaller than any real number, as well as their reciprocals, the infinite numbers. This has an inconsistent version, which has some advantages for calculation in being able to discard higher-order infinitesimals. Interestingly, the theory of differentiation turned out to have these advantages, while the theory of integration did not. A similar result, using a different background logic, was obtained by Da Costa (2000). (2) Another place to find applications of inconsistency in analysis is topology, where one readily observes the practice of cutting and pasting spaces being described as “identification” of one boundary with another. One can show that this can be described in an inconsistent theory in which the two boundaries are both identical and not identical, and it can be further argued that this is the most natural description of the practice. (3) Yet another application is the class of inconsistent continuous functions. Not all functions which are classically discontinuous are amenable of inconsistent treatment; but some are, for example *f*(*x*)=0 for all *x*<0 and *f*(*x*)=1 for all *x*≥0. The inconsistent extension replaces the first < by ≤, and has distinctive structural properties. These inconsistent functions may well have some application in dynamic systems in which there are discontinuous jumps, such as quantum measurement systems. Differentiating such functions leads to the delta functions, applied by Dirac to the study of quantum measurement. (4) Next, there is the well-known case of inconsistent systems of linear equations, such as the system (i) *x*+*y*=1, plus (ii) *x*+*y*=2. Such systems can potentially arise within the context of automated control. Little work has been done classically to solve such systems, but it can be shown that there are well-behaved solutions within inconsistent vector spaces. (5) Finally, one can note a further application in topology and dynamics. Given a supposition which seems to be conceivable, namely that whatever happens or is true, happens or is true on an open set of (spacetime) points, one has that the logic of dynamically possible paths is open set logic, that is to say intuitionist logic, which supports incomplete theories par excellence. This is because the natural account of the negation of a proposition in such a space says that it holds on the largest open set contained in the Boolean complement of the set of points on which the original proposition held, which is in general smaller than the Boolean complement. However, specifying a topological space by its closed sets is every bit as reasonable as specifying it by its open sets. Yet the logic of closed sets is known to be paraconsistent, ie. supports inconsistent nontrivial theories; see Goodman (1981)[^goodman-1981], for example. Thus given the (alternative) supposition which also seems to be conceivable, namely that whatever is true is true on a closed set of points, one has that inconsistent theories may well hold. This is because the natural account of the negation of a proposition, namely that it holds on the smallest closed set containing the Boolean negation of the proposition, means that on the overlapping boundary both the proposition and its negation hold. Thus dynamical theories determine their own logic of possible propositions, and corresponding theories which may be inconsistent, and are certainly as natural as their incomplete counterparts.

On closed set logic and boundaries as a natural setting for contradictory theories, see Mortensen (2003, 2010)[^mortensen-2003][^mortensen-2010]. Weber and Cotnoir (2015) also explore the inconsistency of boundaries, arising from the incompatibility of the three principles (i) there are boundaries, (ii) space is topologically connected, and (iii) discrete entities can be in contact (i.e., no space between them). This is a very interesting problem, as all three are plausible; in particular there do seem to be boundaries in our world. An initially surprising feature of this account is that boundaries come out as “empty”; after all, null entities are contrary to the spirit of mereology. But this is not so shocking as it turns out that they are only empty in the sense that they have members inconsistently.

Category theory throws light on many mathematical structures. It has certainly been proposed as an alternative foundation for mathematics. Such generality inevitably runs into problems similar to those of comprehension in set theory; see, e.g., Hatcher 1982 (pp. 255–260). Hence there is the same possible application of inconsistent solutions. There is also an important collection of categorial structures, the toposes, which support open set logic in exact parallel to the way sets support Boolean logic. This has been taken by many to be a vindication of the foundational point of view of mathematical intuitionism. However, it can be proved that that toposes support closed set logic as readily as they support open set logic, to date the only category-theoretic semantics for a paraconsistent logic. This should not be viewed as an objection to intuitionism, however, so much as an argument that inconsistent theories are equally reasonable as items of mathematical study. See Mortensen (1995 Chap 11, co-author Lavers). This position has now been taken up, extended and ably defended by Estrada-González (2010, 2015a, 2015b)[^estrada-gonzález-2010][^estrada-gonzález-2015a][^estrada-gonzález-2015b]. The same author (2016) undertakes to provide a category-theoretic description of trivial theories, with the aim of showing that triviality is not such an uninteresting feature for mathematical theories to have. The present author remains unconvinced, since a trivial theory is surely useless for mathematical calculation; but the ingenuity of the arguments must be conceded.

Duality between incompleteness/intuitionism and inconsistency/paraconsistency has at least two aspects. First there is the above topological (open/closed) duality. Second there is Routley * duality. The Routley Star * of a set of sentences *S*, is defined as *S*\* =_{*df*} {*A*: ~*A* is not in *S*}. Discovered by the Routleys (1972) as a semantical tool for relevant logics, the * operation dualises between inconsistent and incomplete theories of the large natural class of de Morgan logics. For example, starring Peano arithmetic gives a deductively-closed inconsistent complete non-trivial classical arithmetical theory containing all of PA, which presents an interesting challenge for the Godel incompleteness results, see Mortensen (2013)[^mortensen-2013]. Both kinds of duality interact as well, where the * gives distinctive duality and invariance theorems for open set and closed set arithmetical theories. On the basis of these results, it is fair to argue that both kinds of mathematics, intuitionist and paraconsistent, are equally reasonable.

## 4. Geometrical Inconsistency

A geometrical development is the application to explaining the phenomenon of inconsistent pictures. The best known of these are perhaps M. C. Escher’s masterpieces *Belvedere, Waterfall* and *Ascending and Descending*. In fact the tradition goes back millennia to Pompeii. Escher seems to have derived many of his intuitions from the Swedish artist Oscar Reutersvärd, who began his inconsistent work in 1934. Escher also actively collaborated with the English mathematician Roger Penrose. There have been several attempts to describe the mathematical structure of inconsistent pictures using classical consistent mathematics, by theorists such as Cowan, Francis and Penrose. As argued in Mortensen (1997)[^mortensen-1997], however, no consistent mathematical theory can capture the sense that one is seeing an impossible thing. Only an inconsistent theory can capture the content of that perception. This amounts to an appeal to a cognitive justification of paraconsistency. One can then proceed to display inconsistent theories which are candidates for such inconsistent contents. There is an analogy with classical mathematics on this point: projective geometry is a classical consistent mathematical theory which is interesting because we are creatures with an eye, since it explains why it is that things look the way they do in perspective.

Inconsistent geometrical studies are further developed in Mortensen (2002a)[^mortensen-2002a], where category theory is applied to give a general description of the relationships between the various theories and their consistent cut-downs and incomplete duals. For an informal account which highlights the difference between visual “paradoxes” and the philosophically more common paradoxes of language, such as the Liar, see Mortensen (2002b)[^mortensen-2002b].

More recently, inconsistent mathematical descriptions have been obtained for several classes of inconsistent figures, exemplified by Escher’s Cube (found in his print *Belvedere*), the Reutersvärd-Penrose triangle, and others. See Mortensen (2010)[^mortensen-2010].

This raises another interesting issue. Ever since Euclid, the method of reductio ad absurdum has been thoroughly exploited in geometrical proofs (assume he opposite of what you want to prove and deduce a contradiction). But here we have a different technique (employ a contradiction to describe how inconsistent figures look, to demonstrate that the content is genuinely contradictory). If successful, this is a demonstration that human conceptualisation exceeds the merely possible (consistent). For discussion see Mortensen (2019, 2022)[^mortensen-2019][^mortensen-2022].

One more point: do these geometrical paradoxes lend support to full dialetheism? The answer is no. If you can draw a contradictory picture then *something* exists that is inconsistent. And, distinct inconsistent figures imply distinctions between types of contradictions which ECQ does not permit. But this should not be pushed too far. Nothing says that because a picture has a content, that content must somehow be *true*: many pictures are fictional in content. For more on this theme see Mortensen (2019a)[^mortensen-2019a].

## 5. Chunk and Permeate

Recently, an alternative technique for dealing generally with contradictions has emerged. Brown and Priest (2004) have proposed a technique they call “Chunk and Permeate”, in which reasoning from inconsistent premisses proceeds by separating the assumptions into consistent theories (chunks), deriving appropriate consequences, then passing (permeating) those consequences to a different chunk for further consequences to be derived. They suggest that Newton’s original reasoning in taking derivates in the calculus, was of this form. This is an interesting and novel approach, though it must meet the objection that to believe a conclusion obtained on this basis, one should believe all the premisses equally; and so an argument of the more common form, appealing to all the premisses without fragmenting them, should be eventually forthcoming. The objection is thus that Chunk and Permeate is part of the context of discovery rather than the context of justification.

Later, Benham *et. al.* (2014) have extended these methods to the Dirac delta function. This broadens the class of applications, and so strengthens the technique. However, it also becomes clear there, that there is a close parallel between (one large class of) Chunk and Permeate applications, and (consistent) non-standard analysis: wherever Chunk and Permeate takes a derivative by shifting chunks to one where infinitesimals are zero, non-standard analysis takes a derivative by defining derivatives to be “standard parts only”. Of course, equivalence between these two techniques does not show which is explanatorily deeper. Developments are to be awaited with interest.

## 6. Conclusion

To conclude: there has been appearing lately quite a bit of philosophical material, that is sympathetic to the cause of inconsistent mathematics. Colyvan (2000)[^colyvan-2000] addresses the issue that inconsistent mathematical theories imply inconsistent mathematical objects as their subject-matters. He also takes up the important task of providing an account of how inconsistent mathematics can have a branch which is *applied* mathematics. Priest (2013)[^priest-2013], like Colyvan, notes that inconsistent mathematics adds to the platonist mix. Berto (2007)[^berto-2007] usefully surveys paradoxes and foundational issues, and sets out some of the arithmetical results that bear on important philosophical issues like the Incompleteness Theorems. Van Bendegem (2014) pursues the interesting motivation that change is always a state of anomaly, so that always changing implies always anomalous. Examples include infinitesimals, complex numbers and infinity. Caution should be adopted over thinking that inconsistency is always anomalous, however, if only because it is simply more material for mathematical study.

It should be emphasised again that these structures do not in any way challenge or repudiate existing mathematics, but rather extend our conception of what is mathematically possible. This, in turn, sharpens the issue of Mathematical Pluralism; see e.g., Davies (2005)[^davies-2005], Hellman and Bell (2006), or Priest (2013)[^priest-2013]. Various authors have different versions of mathematical pluralism, but it is something along the lines that incompatible mathematical theories can be equally true. The case for mathematical pluralism rests on the observation that there are different mathematical “universes” in which different, indeed incompatible, mathematical theorems or laws hold. Well-known examples are the incompatibility between classical mathematics and intuitionist mathematics, and the incompatibility between ZF-like universes of sets respectively with, and without, the Axiom of Choice. It seems absurd to say that ZF with Choice is true mathematics and ZF without Choice is false mathematics, if they are both legitimate examples of mathematically well-behaved theories.

The primary question for the philosophy of mathematics is surely *what is mathematics*. Duality operations like topological duality or Routley* reinforce the point that incomplete/inconsistent duals are equally reasonable as examples of mathematics. From this point of view, disputes about which of intuitionist or classical or inconsistent mathematics to accept seem pointless; they are all part of the subject matter of mathematics. This point is made effectively by Shapiro (2014, in contrast see his 2002). Shapiro’s distinctive position has other ingredients: mathematics as the science of structure, and mathematical pluralism implying logical pluralism (on logical pluralism see also Beall and Restall 2006)[^beall-2006]; but we do not take these up here.

For what it is worth, the present writer thinks that some version of mathematical pluralism is obviously true, if one takes mathematics to be firstly about mathematical theories allowing for inconsistency , and only secondly about the objects internal to those theories. There is, of course, no problem about incompatible theories co-existing, if considered as structures of propositions. The primacy of theories fits, too, with the natural observation that the epistemology of mathematics is deductive proof. It is only if one takes as a starting point the primacy of the mathematical object as the truth-maker of theories, that one has to worry about how their objects manage to co-exist.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=mathematics-inconsistent). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/mathematics-inconsistent/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=mathematics-inconsistent&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/mathematics-inconsistent/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

[Please contact the author with suggestions.]

## Related Entries

contradiction | logic: paraconsistent | mathematics, philosophy of | self-reference

[^beall-2006]: Beall, J.C. and G. Restall, 2006, *Logical Pluralism*, Oxford: The Clarendon Press.

[^benham-2014]: Benham, R., C. Mortensen and G. Priest, 2014, “Chunk and Permeate III: The Dirac Delta Function”, *Synthese*, 191(13): 3057-3062. doi:10.1007/s11229-014-0473-7

[^berto-2007]: Berto, F., 2007, *How to Sell a Contradiction*, London: College Publications.

[^brady-1971]: Brady, R., 1971, “The Consistency of the Axioms of Abstraction and Extensionality in a Three-Valued Logic”, *Notre Dame Journal of Formal Logic*, 12: 447–453.

[^brady-1989]: –––, 1989, “The Nontriviality of Dialectical Set Theory”, in G. Priest, R. Routley and J. Norman (eds.), *Paraconsistent Logic*, Munich: Philosophia Verlag.

[^brady-2006]: –––, 2006, *Universal Logic*, Stanford: CSLI Publications.

[^brown-2004]: Brown, B., and G. Priest, 2004, “Chunk and Permeate: A Paraconsistent Inference Strategy. Part I: The Infinitesimal Calculus”, *The Journal of Philosophical Logic*, 33: 379–388.

[^burgess-1981]: Burgess, J., 1981, “Relevance, a Fallacy?”, *Notre Dame Journal of Formal Logic*, 22: 97–104.

[^colyvan-2000]: Colyvan, M., 2000, “Applying Inconsistent Mathematics”, *New Waves in the Philosophy of Mathematics*, O.Bueno and O. Limmbo (eds.), London: Palgrave McMillan, 160-172.

[^da-1974]: Da Costa, Newton C.A., 1974, “On the Theory of Inconsistent Formal Systems”, *Notre Dame Journal of Formal Logic*, 15: 497–510.

[^da-2000]: –––, 2000, “Paraconsistent Mathematics”, in D. Batens *et al*. (eds.), *Frontiers of Paraconsistent Logic*, Hertfordshire: Research Studies Press, 165–180.

[^davies-2005]: Davies, E.B., 2005 “A Defence of Mathematical Pluralism ”, *Philosophia Mathematica*, 13: 252–276.

[^estrada-gonzález-2010]: Estrada-González, L., 2010, “Complement-Topoi and Dual Intuitionistic Logic”, *Australasian Journal of Logic*, 9: 26–44.

[^estrada-gonzález-2015a]: –––, 2015a, “The Evil Twin: The Basics of Complement-toposes”, in Beziau, Chakraborty and Dutta (eds.), *New Directions in Paraconsistent Logic*, Dordrecht: Springer: 375-425.

[^estrada-gonzález-2015b]: –––, 2015b, “From (paraconsistent) topos logic to Universal (topos) logic”, in Koslow and Buchsbaum (eds.), *The Road to Universal Logic: Festschrift for Jean-Yves Beziau on his Fiftieth Birthday*, Dordrecht: Springer, 263-295.

[^estrada-gonzález-2016]: –––, 2016, “Prospects for Triviality”, in H. Andreas and P. Verdee (eds.), *Logical Studies of Paraconsistent Reasoning in Science and Mathematics*, Dordrecht: Springer, 81-89.

[^goodman-1981]: Goodman, N., 1981, “The Logic of Contradictions”, *Zeitschrift fur Mathematische Logic und Grundlagen der Arithmetik*, 27: 119–126.

[^hatcher-1982]: Hatcher, W. S., 1982, *The Logical Foundations of Mathematics*, Oxford: Pergamon.

[^hellman-2006]: Hellman, G. and J. Bell, 2006, “Pluralism and the Foundations of Mathematics”, in C.K. Waters et al. (eds.), *Scientific Pluralism* (Minnesota Studies in the Philosophy of Science, Volume XIX), Minneapolis: University of Minnesota Press.

[^kripke-1975]: Kripke, S., 1975, “Outline of a Theory of Truth”, *The Journal of Philosophy*, 72: 690–716.

[^mckubre-jordens-2012]: McKubre-Jordens, M., and Zach Weber, 2012, “Real Analysis and Paraconsistent Logic”, *Journal of Philosophical Logic*, 41(5): 901–922.

[^meyer-1976]: Meyer, R. K., 1976, “Relevant Arithmetic”, *Bulletin of the Section of Logic of the Polish Academy of Sciences*, 5: 133–137.

[^meyer-1984]: Meyer, R. K. and C. Mortensen, 1984, “Inconsistent Models for Relevant Arithmetics”, *The Journal of Symbolic Logic*, 49: 917–929.

[^mortensen-1983]: Mortensen, C., 1983, “Reply to Burgess and to Read”, *Notre Dame Journal of Formal Logic*, 24: 35–40.

[^mortensen-1990]: –––, 1990, “Models for Inconsistent and Incomplete Differential Calculus”, *Notre Dame Journal of Formal Logic*, 31: 274–285.

[^mortensen-1995]: –––, 1995, *Inconsistent Mathematics*, Kluwer Mathematics and Its Applications Series, Dordrecht: Kluwer. [[Errata available online](https://www.adelaide.edu.au/directory/chris.mortensen?dsn=directory.file;field=data;id=15292;m=view).]

[^mortensen-1997]: –––, 1997, “Peeking at the Impossible”, *Notre Dame Journal of Formal Logic*, 38: 527–534.

[^mortensen-2000]: –––, 2000, “Prospects for Inconsistency”, in D. Batens *et al*. (eds.), *Frontiers of Paraconsistent Logic*, London: Research Studies Press, 203–208.

[^mortensen-2002a]: –––, 2002a, “Towards a Mathematics of Impossible Pictures”, in W. Carnielli, M. Coniglio and I. D’Ottaviano (eds.), *Paraconsistency: The Logical Way to the Infinite*, (Lecture Notes in Pure and Applied Mathematics, Volume 228), New York: Marcel Dekker, 445–454.

[^mortensen-2002b]: –––, 2002b, “Paradoxes Inside and Outside Language”, *Language and Communication*, 22: 301–311.

[^mortensen-2003]: –––, 2003, “Closed Set Logic”, in R. Brady (ed.), *Relevant Logics and Their Rivals* (Volume II), Aldershot: Ashgate, pp. 252-262 (especially 255-6).

[^mortensen-2006]: –––, 2006, “An Analysis of Inconsistent and Incomplete Necker Cubes”, *Australasian Journal of Logic*, 4: 216–225.

[^mortensen-2010]: –––, 2010, *Inconsistent Geometry* (Studies in Logic, Volume 27), London: College Publications (King’s College).

[^mortensen-2011]: –––, 2011, “Merge”, *Australasian Journal of Logic*, 9: 135–141.

[^mortensen-2013]: –––, 2013, “Arithmetic Starred”, in K. Tanaka, F. Berto, E. Mares and F. Paoli (eds.), *Paraconsistency: Logic and Applications*, Dordrecht: Springer, 309–314.

[^mortensen-2019]: –––, 2019, “Euclid's Geometry: the Case of Contradiction”, *Journal of Modern Greek Studies* (Australia and New Zealand), Special Issue, 2019, 71–83.

[^mortensen-2019a]: –––, 2019a, “Dialethism and Impossible Figures”, in A. Rieger and G. Young (eds.), *Dialetheism and Its Applications*, Cham: Springer International Publishing, 185–194.

[^mortensen-2022]: –––, 2022, *The Impossible Arises*, Bloomington, Indiana University Press.

[^paris-2006]: Paris, J., and Pathmanathan, N., 2006, “A Note on Priest’s Finite Arithmetics”, *The Journal of Philosophical Logic*, 35: 529–537.

[^paris-2008]: Paris, J., and Sirokofskich, A., 2008, “On LP-models of Arithmetic”, *The Journal of Symbolic Logic*, 73(1): 212–226.

[^priest-1987]: Priest, G., 1987, *In Contradiction*, Dordrecht: Nijhoff; second expanded edition, Oxford: The Clarendon Press, 2006.

[^priest-1997]: –––, 1997, “Inconsistent Models for Arithmetic: I, Finite Models”, *The Journal of Philosophical Logic*, 26: 223–235.

[^priest-2000]: –––, 2000, “Inconsistent Models for Arithmetic: II, The General Case”, *The Journal of Symbolic Logic*, 65: 1519–29.

[^priest-2013]: –––, 2013, “Mathematical Pluralism”, *Logic Journal of IGPL*, 21(1): 4–13: doi:10.1093/jzs018

[^priest-1989]: Priest, G., R. Routley and J. Norman (eds.), 1989, *Paraconsistent Logic*, Munich: Philosophia Verlag.

[^restall-2007]: Restall, G., 2007, “Review of Brady *Universal Logic*”, *Bulletin of Symbolic Logic*, 13(4): 544–547.

[^robinson-1974]: Robinson, A., 1974, *Non-standard Analysis*, Amsterdam: North-Holland, revised edition.

[^routley-1972]: Routley, R. and V. Routley, 1972, “The Semantics of First Degree Entailment”, *Noûs*, 6: 335–359.

[^shapiro-2002]: Shapiro, S., 2002, “Inconsistency and Incompleteness”, *Mind*, 111: 817–832.

[^shapiro-nd]: –––, “Structures and Logics: a Case for (a) Relativism”, *Erkenntnis*, 79: 309–329.

[^tedder-2015]: Tedder, A., 2015,“Axioms for Finite Collapse Models of Arithmetic”, *The Review of Symbolic Logic*, 8(3): 529-539.

[^van-2014]: Van Bendegem, J-P., 2014, “Inconsistency in Mathematics and the Mathematics of Inconsistency”, *Synthese*, 191(13), 3063-3078.

[^weber-2010]: Weber, Z., 2010, “Transfinite Numbers in Paraconsistent Set Theory”, *The Review of Symbolic Logic*, 3(1): 71-92.

[^weber-2012]: –––, 2012, “Transfinite Cardinals in Paraconsistent Set Theory”, *The Review of Symbolic Logic*, 5(2): 269–293.

[^weber-2013]: –––, 2013, “Notes on Inconsistent Set Theory”, in K. Tanaka, F. Berto, E. Mares and F. Paoli (eds.), *Paraconsistency: Logic and Applications*, Dordrecht: Springer, 315–328.

[^weber-2015]: ––– and Cotnoir, A.J., 2015, “Inconsistent Boundaries”, *Synthese*, 192: 1267–1294. doi:10.1007/511229-014-0614-2

[^weber-2017]: Weber, Z., and M. McKubre-Jordens, 2017, “Paraconsistent Measurement of the Circle”, *Australasian Journal of Logic*, 14(1): doi:10.26686/ajl.v14i1.4034
