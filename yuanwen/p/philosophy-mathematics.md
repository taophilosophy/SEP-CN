# Philosophy of Mathematics
**First published Tue Sep 25, 2007; substantive revision Tue Jan 25, 2022**

*Horsten, Leon*

If mathematics is regarded as a science, then the philosophy of mathematics can be regarded as a branch of the philosophy of science, next to disciplines such as the philosophy of physics and the philosophy of biology. However, because of its subject matter, the philosophy of mathematics occupies a special place in the philosophy of science. Whereas the natural sciences investigate entities that are located in space and time, it is not at all obvious that this is also the case for the objects that are studied in mathematics. In addition to that, the methods of investigation of mathematics differ markedly from the methods of investigation in the natural sciences. Whereas the latter acquire general knowledge using inductive methods, mathematical knowledge appears to be acquired in a different way: by deduction from basic principles. The status of mathematical knowledge also appears to differ from the status of knowledge in the natural sciences. The theories of the natural sciences appear to be less certain and more open to revision than mathematical theories. For these reasons mathematics poses problems of a quite distinctive kind for philosophy. Therefore philosophers have accorded special attention to ontological and epistemological questions concerning mathematics.

## 1. Philosophy of Mathematics, Logic, and the Foundations of Mathematics

On the one hand, philosophy of mathematics is concerned with problems that are closely related to central problems of metaphysics and epistemology. At first blush, mathematics appears to study abstract entities. This makes one wonder what the nature of mathematical entities consists in and how we can have knowledge of mathematical entities. If these problems are regarded as intractable, then one might try to see if mathematical objects can somehow belong to the concrete world after all.

On the other hand, it has turned out that to some extent it is possible to bring mathematical methods to bear on philosophical questions concerning mathematics. The setting in which this has been done is that of *mathematical logic* when it is broadly conceived as comprising proof theory, model theory, set theory, and computability theory as subfields. Thus the twentieth century has witnessed the mathematical investigation of the consequences of what are at bottom philosophical theories concerning the nature of mathematics.

When professional mathematicians are concerned with the foundations of their subject, they are said to be engaged in foundational research. When professional philosophers investigate philosophical questions concerning mathematics, they are said to contribute to the philosophy of mathematics. Of course the distinction between the philosophy of mathematics and the foundations of mathematics is vague, and the more interaction there is between philosophers and mathematicians working on questions pertaining to the nature of mathematics, the better.

## 2. Four schools

The general philosophical and scientific outlook in the nineteenth century tended toward the empirical: platonistic aspects of rationalistic theories of mathematics were rapidly losing support. Especially the once highly praised faculty of rational intuition of ideas was regarded with suspicion. Thus it became a challenge to formulate a philosophical theory of mathematics that was free of platonistic elements. In the first decades of the twentieth century, three non-platonistic accounts of mathematics were developed: logicism, formalism, and intuitionism. There emerged in the beginning of the twentieth century also a fourth program: predicativism. Due to contingent historical circumstances, its true potential was not brought out until the 1960s. However it deserves a place beside the three traditional schools that are discussed in most standard contemporary introductions to philosophy of mathematics, such as (Shapiro 2000)[^shapiro-2000] and (Linnebo 2017)[^linnebo-2017].

### 2.1 Logicism

The logicist project consists in attempting to reduce mathematics to logic. Since logic is supposed to be neutral about matters ontological, this project seemed to harmonize with the anti-platonistic atmosphere of the time.

The idea that mathematics is logic in disguise goes back to Leibniz. But an earnest attempt to carry out the logicist program in detail could be made only when in the nineteenth century the basic principles of central mathematical theories were articulated (by Dedekind and Peano) and the principles of logic were uncovered (by Frege).

Frege devoted much of his career to trying to show how mathematics can be reduced to logic (Frege 1884)[^frege-1884]. He managed to derive the principles of (second-order) Peano arithmetic from the basic laws of a system of second-order logic. His derivation was flawless. However, he relied on one principle which turned out not to be a logical principle after all. Even worse, it is untenable. The principle in question is Frege’s *Basic Law V*:

$$ \{x|Fx\}=\{x|Gx\} \text{ if and only if } \forall x(Fx \equiv Gx), $$

In words: the set of the *F*s is identical with the set of the *G*s iff the *F*s are precisely the *G*s.

In a famous letter to Frege, Russell showed that Frege’s Basic Law V entails a contradiction (Russell 1902)[^russell-1902]. This argument has come to be known as *Russell’s paradox* (see section 2.4).

Russell himself then tried to reduce mathematics to logic in another way. Frege’s Basic Law V entails that corresponding to every property of mathematical entities, there exists a class of mathematical entities having that property. This was evidently too strong, for it was exactly this consequence which led to Russell’s paradox. So Russell postulated that only properties of mathematical objects that have already been shown to exist, determine classes. Predicates that implicitly refer to the class that they were to determine if such a class existed, do not determine a class. Thus a typed structure of properties is obtained: properties of ground objects, properties of ground objects and classes of ground objects, and so on. This typed structure of properties determines a layered universe of mathematical objects, starting from ground objects, proceeding to classes of ground objects, then to classes of ground objects and classes of ground objects, and so on.

Unfortunately, Russell found that the principles of his typed logic did not suffice for deducing even the basic laws of arithmetic. He needed, among other things, to lay down as a basic principle that there exists an infinite collection of ground objects. This could hardly be regarded as a logical principle. Thus the second attempt to reduce mathematics to logic also faltered.

And there matters stood for more than fifty years. In 1983, Crispin Wright’s book on Frege’s theory of the natural numbers appeared (Wright 1983)[^wright-1983]. In it, Wright breathes new life into the logicist project. He observes that Frege’s derivation of second-order Peano Arithmetic can be broken down in two stages. In a first stage, Frege uses the inconsistent Basic Law V to derive what has come to be known as *Hume’s Principle*:

The number of the *F*s = the number of the *G*s if and only if $F\approx G$,

where $F \approx G$ means that the *F*s and the *G*s stand in one-to-one correspondence with each other. (This relation of one-to-one correspondence can be expressed in second-order logic.) Then, in a second stage, the principles of second-order Peano Arithmetic are derived from Hume’s Principle and the accepted principles of second-order logic. In particular, Basic Law V is *not* needed in the second part of the derivation. Moreover, Wright conjectured that in contrast to Frege’s Basic Law V, Hume’s Principle is consistent. George Boolos and others observed that Hume’s Principle is indeed consistent (Boolos 1987)[^boolos-1987].

Wright went on to claim that Hume’s Principle can be regarded as a truth of logic. If that is so, then at least second-order Peano arithmetic is reducible to logic alone. Thus a new form of logicism was born; today this view is known as *neo-logicism* (Hale & Wright 2001)[^hale-2001]. Most philosophers of mathematics today doubt that Hume’s Principle is a principle of *logic*. Indeed, even Wright later sought to qualify this claim. Nonetheless, many philosophers of mathematics feel that the introduction of natural numbers through Hume’s Principle is attractive from an ontological and from an epistemological point of view. Linnebo argues that because the left-hand-side of Hume’s Principle merely *re-carves* the content of its right-hand-side, not much is needed from the world to make Hume’s Principle true. For this reason, he calls natural numbers and mathematical objects that can be introduced in a similar way *light* mathematical objects (Linnebo 2018)[^linnebo-2018].

Wright’s work has drawn the attention of philosophers of mathematics to the *kind* of principles of which Basic Law V and Hume’s Principle are examples. These principles are called *abstraction principles*. At present, philosophers of mathematics attempt to construct general theories of abstraction principles that explain which abstraction principles are acceptable and which are not, and why (Weir 2003; Fine 2002)[^fine-2002][^weir-2003]. Also, it has emerged that in the context of weakened versions of second-order logic, Frege’s Basic Law V is consistent. But these weak background theories only allow very weak arithmetical theories to be derived from Basic Law V (Burgess 2005)[^burgess-2005].

### 2.2 Intuitionism

Intuitionism originates in the work of the mathematician L.E.J. Brouwer (van Atten 2004)[^atten-2004], and it is inspired by Kantian views of what objects are (Parsons 2008, chapter 1)[^parsons-2008]. According to intuitionism, mathematics is essentially an activity of construction. The natural numbers are mental constructions, the real numbers are mental constructions, proofs and theorems are mental constructions, mathematical meaning is a mental construction… Mathematical constructions are produced by the *ideal* mathematician, i.e., abstraction is made from contingent, physical limitations of the real life mathematician. But even the ideal mathematician remains a finite being. She can never complete an infinite construction, even though she can complete arbitrarily large finite initial parts of it. This entails that intuitionism resolutely rejects the existence of the actual (or completed) infinite; only potentially infinite collections are given in the activity of construction. A basic example is the successive construction in time of the individual natural numbers.

From these general considerations about the nature of mathematics, based on the condition of the human mind (Moore 2001)[^moore-2001], intuitionists infer to a revisionist stance in logic and mathematics. They find non-constructive existence proofs unacceptable. Non-constructive existence proofs are proofs that purport to demonstrate the existence of a mathematical entity having a certain property without even implicitly containing a method for generating an example of such an entity. Intuitionism rejects non-constructive existence proofs as ‘theological’ and ‘metaphysical’. The characteristic feature of non-constructive existence proofs is that they make essential use of the *principle of excluded third*

$$ \phi \vee \neg \phi, $$

or one of its equivalents, such as the principle of double negation

$$ \neg \neg \phi \rightarrow \phi $$

In classical logic, these principles are valid. The logic of intuitionistic mathematics is obtained by removing the principle of excluded third (and its equivalents) from classical logic. This of course leads to a revision of mathematical knowledge. For instance, the classical theory of elementary arithmetic, *Peano Arithmetic*, can no longer be accepted. Instead, an intuitionistic theory of arithmetic (called *Heyting Arithmetic*) is proposed which does not contain the principle of excluded third. Although intuitionistic elementary arithmetic is weaker than classical elementary arithmetic, the difference is not all that great. There exists a simple syntactical translation which translates all classical theorems of arithmetic into theorems which are intuitionistically provable.

In the first decades of the twentieth century, parts of the mathematical community were sympathetic to the intuitionistic critique of classical mathematics and to the alternative that it proposed. This situation changed when it became clear that in higher mathematics, the intuitionistic alternative differs rather drastically from the classical theory. For instance, intuitionistic mathematical analysis is a fairly complicated theory, and it is very different from classical mathematical analysis. This dampened the enthusiasm of the mathematical community for the intuitionistic project. Nevertheless, followers of Brouwer have continued to develop intuitionistic mathematics onto the present day (Troelstra & van Dalen 1988)[^troelstra-1988].

### 2.3 Formalism

David Hilbert agreed with the intuitionists that there is a sense in which the natural numbers are basic in mathematics. But unlike the intuitionists, Hilbert did not take the natural numbers to be mental constructions. Instead, he argued that the natural numbers can be taken to be *symbols*. Symbols are strictly speaking abstract objects. Nonetheless, it is essential to symbols that they can be embodied by concrete objects, so we may call them *quasi-concrete* objects (Parsons 2008, chapter 1)[^parsons-2008]. Perhaps physical entities could play the role of the natural numbers. For instance, we may take a concrete ink trace of the form | to be the number 0, a concretely realized ink trace || to be the number 1, and so on. Hilbert thought it doubtful at best that higher mathematics could be directly interpreted in a similarly straightforward and perhaps even concrete manner.

Unlike the intuitionists, Hilbert was not prepared to take a revisionist stance toward the existing body of mathematical knowledge. Instead, he adopted an instrumentalist stance with respect to higher mathematics. He thought that higher mathematics is no more than a formal game. The statements of higher-order mathematics are uninterpreted strings of symbols. Proving such statements is no more than a game in which symbols are manipulated according to fixed rules. The point of the ‘game of higher mathematics’ consists, in Hilbert’s view, in proving statements of elementary arithmetic, which do have a direct interpretation (Hilbert 1925)[^hilbert-1925].

Hilbert thought that there can be no reasonable doubt about the soundness of classical Peano Arithmetic — or at least about the soundness of a subsystem of it that is called *Primitive Recursive Arithmetic* (Tait 1981)[^tait-1981]. And he thought that every arithmetical statement that can be proved by making a detour through higher mathematics, can also be proved directly in Peano Arithmetic. In fact, he strongly suspected that *every* problem of elementary arithmetic can be decided from the axioms of Peano Arithmetic. Of course solving arithmetical problems in arithmetic is in some cases practically impossible. The history of mathematics has shown that making a “detour” through higher mathematics can sometimes lead to a proof of an arithmetical statement that is much shorter and that provides more insight than any purely arithmetical proof of the same statement.

Hilbert realized, albeit somewhat dimly, that some of his convictions can actually be considered to be mathematical conjectures. For a proof in a formal system of higher mathematics or of elementary arithmetic is a finite combinatorial object which can, modulo coding, be considered to be a natural number. But in the 1920s the details of coding proofs as natural numbers were not yet completely understood.

On the formalist view, a minimal requirement of formal systems of higher mathematics is that they are at least consistent. Otherwise *every* statement of elementary arithmetic can be proved in them. Hilbert also saw (again, dimly) that the consistency of a system of higher mathematics entails that this system is at least partially arithmetically sound. So Hilbert and his students set out to prove statements such as the consistency of the standard postulates of mathematical analysis. Of course such statements would have to be proved in a ‘safe’ part of mathematics, such as elementary arithmetic. Otherwise the proof does not increase our conviction in the consistency of mathematical analysis. And, fortunately, it seemed possible in principle to do this, for in the final analysis consistency statements are, again modulo coding, arithmetical statements. So, to be precise, Hilbert and his students set out to prove the consistency of, e.g., the axioms of mathematical analysis in classical Peano arithmetic. This project was known as *Hilbert’s program* (Zach 2006)[^zach-2006]. It turned out to be more difficult than they had expected. In fact, they did not even succeed in proving the consistency of the axioms of Peano Arithmetic in Peano Arithmetic.

Then Kurt Gödel proved that there exist arithmetical statements that are undecidable in Peano Arithmetic (Gödel 1931)[^gödel-1931]. This has become known as Gödel’s *first incompleteness theorem*. This did not bode well for Hilbert’s program, but it left open the possibility that the consistency of higher mathematics is not one of these undecidable statements. Unfortunately, Gödel then quickly realized that, unless (God forbid!) Peano Arithmetic is inconsistent, the consistency of Peano Arithmetic is independent of Peano Arithmetic. This is Gödel’s *second incompleteness theorem*. Gödel’s incompleteness theorems turn out to be generally applicable to all sufficiently strong but consistent recursively axiomatizable theories. Together, they entail that Hilbert’s program fails. It turns out that higher mathematics cannot be interpreted in a purely instrumental way. Higher mathematics can prove arithmetical sentences, such as consistency statements, that are beyond the reach of Peano Arithmetic.

All this does not spell the end of formalism. Even in the face of the incompleteness theorems, it is coherent to maintain that mathematics is the science of formal systems.

One version of this view was proposed by Curry (Curry 1958)[^curry-1958]. On this view, mathematics consists of a collection of formal systems which have no interpretation or subject matter. (Curry here makes an exception for metamathematics.) Relative to a formal system, one can say that a statement is true if and only if it is derivable in the system. But on a fundamental level, *all* mathematical systems are on a par. There can be at most pragmatical reasons for preferring one system over another. Inconsistent systems can prove all statements and therefore are pretty useless. So when a system is found to be inconsistent, it must be modified. It is simply a lesson from Gödel’s incompleteness theorems that a sufficiently strong consistent system cannot prove its own consistency.

There is a canonical objection against Curry’s formalist position. Mathematicians do not in fact treat all apparently consistent formal systems as being on a par. Most of them are unwilling to admit that the preference of arithmetical systems in which the arithmetical sentence expressing the consistency of Peano Arithmetic are derivable over those in which its negation is derivable, for instance, can ultimately be explained in purely pragmatical terms. Many mathematicians want to maintain that the perceived correctness (incorrectness) of certain formal systems must ultimately be explained by the fact that they correctly (incorrectly) describe certain subject matters.

Detlefsen has emphasized that the incompleteness theorems do not preclude that the consistency of *parts* of higher mathematics that are in practice used for solving arithmetical problems that mathematicians are interested in can be arithmetically established (Detlefsen 1986)[^detlefsen-1986]. In this sense, something can perhaps be rescued from the flames even if Hilbert’s instrumentalist stance towards all of higher mathematics is ultimately untenable.

Another attempt to salvage a part of Hilbert’s program was made by Isaacson (Isaacson 1987)[^isaacson-1987]. He defends the view that *in some sense*, Peano Arithmetic may be complete after all (Isaacson 1987)[^isaacson-1987]. He argues that true sentences undecidable in Peano Arithmetic can only be proved by means of *higher-order concepts*. For instance, the consistency of Peano Arithmetic can be proved by induction up to a transfinite ordinal number (Gentzen 1938)[^gentzen-1938]. But the notion of an ordinal number is a set-theoretic, and hence non-arithmetical, concept. If the only ways of proving the consistency of arithmetic make essential use of notions which arguably belong to higher-order mathematics, then the consistency of arithmetic, even though it can be expressed in the language of Peano Arithmetic, is a non-arithmetical problem. And generalizing from this, one can wonder whether Hilbert’s conjecture that *every* problem of arithmetic can be decided from the axioms of Peano Arithmetic might not still be true.

### 2.4 Predicativism

As was mentioned earlier, predicativism is not ordinarily described as one of the schools. But it is only for contingent reasons that before the advent of the second world war predicativism did not rise to the level of prominence of the other schools.

The origin of predicativism lies in the work of Russell. On a cue of Poincaré, he arrived at the following diagnosis of the Russell paradox. The argument of the Russell paradox defines the collection C of all mathematical entities that satisfy $\neg x\in x$. The argument then proceeds by asking whether C itself meets this condition, and derives a contradiction.

The Poincaré-Russell diagnosis of this argument states that this definition does not pick out a collection at all: it is impossible to define a collection S by a condition that implicitly refers to S itself. This is called the *vicious circle principle*. Definitions that violate the vicious circle principle are called *impredicative*. A sound definition of a collection only refers to entities that exist independently from the defined collection. Such definitions are called *predicative*. As Gödel later pointed out, a platonist would find this line of reasoning unconvincing. If mathematical collections exist independently of the act of defining, then it is not immediately clear why there could not be collections that can *only* be defined impredicatively (Gödel 1944)[^gödel-1944].

All this led Russell to develop the simple and the ramified theory of types, in which syntactical restrictions were built in that make impredicative definitions ill-formed. In simple type theory, the free variables in defining formulas range over entities to which the collection to be defined do not belong. In ramified type theory, it is required in addition that the range of the bound variables in defining formulas do not include the collection to be defined. It was pointed out in section 2.1 that Russell’s type theory cannot be seen as a reduction of mathematics to logic. But even aside from that, it was observed early on that especially in ramified type theory it is too cumbersome to formalize ordinary mathematical arguments.

When Russell turned to other areas of analytical philosophy, Hermann Weyl took up the predicativist cause (Weyl 1918)[^weyl-1918]. Like Poincaré, Weyl did not share Russell’s desire to reduce mathematics to logic. And right from the start he saw that it would be in practice impossible to work in a ramified type theory. Weyl developed a philosophical stance that is in a sense intermediate between intuitionism and platonism. He took the collection of natural numbers as unproblematically given. But the concept of an arbitrary subset of the natural numbers was not taken to be immediately given in mathematical intuition. Only those subsets which are determined by arithmetical (i.e., first-order) predicates are taken to be predicatively acceptable.

On the one hand, it emerged that many of the standard definitions in mathematical analysis are impredicative. For instance, the minimal closure of an operation on a set is ordinarily defined as the intersection of all sets that are closed under applications of the operation. But the minimal closure itself is one of the sets that are closed under applications of the operation. Thus, the definition is impredicative. In this way, attention gradually shifted away from concern about the set-theoretical paradoxes to the role of impredicativity in mainstream mathematics. On the other hand, Weyl showed that it is often possible to bypass impredicative notions. It even emerged that most of mainstream nineteenth century mathematical analysis can be vindicated on a predicative basis (Feferman 1988)[^feferman-1988].

In the 1920s, History intervened. Weyl was won over to Brouwer’s more radical intuitionistic project. In the meantime, mathematicians became convinced that the highly impredicative transfinite set theory developed by Cantor and Zermelo was less acutely threatened by Russell’s paradox than previously suspected. These factors caused predicativism to lapse into a dormant state for several decades.

Building on work in generalized recursion theory, Solomon Feferman extended the predicativist project in the 1960s (Feferman 2005)[^feferman-2005]. He realized that Weyl’s strategy could be iterated into the transfinite. Also those sets of numbers that can be defined by using quantification over the sets that Weyl regarded as predicatively justified, should be counted as predicatively acceptable, and so on. This process can be propagated along an ordinal path. This ordinal path stretches as far into the transfinite as the *predicative ordinals* reach, where an ordinal is predicative if it measures the length of a provable well-ordering of the natural numbers. This calibration of the strength of predicative mathematics, which is due to Feferman and (independently) Schütte, is nowadays fairly generally accepted. Feferman then investigated how much of standard mathematical analysis can be carried out within a predicativist framework. The research of Feferman and others (most notably Harvey Friedman) shows that most of twentieth century analysis is acceptable from a predicativist point of view. But it is also clear that not all of contemporary mathematics that is generally accepted by the mathematical community is acceptable from a predicativist standpoint: transfinite set theory is a case in point.

## 3. Platonism

In the years before the second world war it became clear that weighty objections had been raised against each of the three anti-platonist programs in the philosophy of mathematics. Predicativism was perhaps an exception, but it was at the time a program without defenders. Thus room was created for a renewed interest in the prospects of platonistic views about the nature of mathematics. On the platonistic conception, the subject matter of mathematics consists of *abstract entities*.

### 3.1 Gödel’s Platonism

Gödel was a platonist with respect to mathematical objects and with respect to mathematical concepts (Gödel 1944; Gödel 1964)[^gödel-1944]. But his platonistic view was more sophisticated than that of the mathematician in the street.

Gödel held that there is a strong parallelism between plausible theories of mathematical objects and concepts on the one hand, and plausible theories of physical objects and properties on the other hand. Like physical objects and properties, mathematical objects and concepts are not constructed by humans. Like physical objects and properties, mathematical objects and concepts are not reducible to mental entities. Mathematical objects and concepts are as objective as physical objects and properties. Mathematical objects and concepts are, like physical objects and properties, postulated in order to obtain a good satisfactory theory of our experience. Indeed, in a way that is analogous to our perceptual relation to physical objects and properties, through *mathematical intuition* we stand in a quasi-perceptual relation with mathematical objects and concepts. Our perception of physical objects and concepts is fallible and can be corrected. In the same way, mathematical intuition is not fool-proof — as the history of Frege’s Basic Law V shows— but it can be trained and improved. Unlike physical objects and properties, mathematical objects do not exist in space and time, and mathematical concepts are not instantiated in space or time.

Our mathematical intuition provides *intrinsic evidence* for mathematical principles. Virtually all of our mathematical knowledge can be deduced from the axioms of *Zermelo-Fraenkel set theory with the Axiom of Choice* (ZFC). In Gödel’s view, we have compelling intrinsic evidence for the truth of these axioms. But he also worried that mathematical intuition might not be strong enough to provide compelling evidence for axioms that significantly exceed the strength of ZFC.

Aside from intrinsic evidence, it is in Gödel’s view also possible to obtain *extrinsic evidence* for mathematical principles. If mathematical principles are successful, then, even if we are unable to obtain intuitive evidence for them, they may be regarded as probably true. Gödel says that:

> … success here means fruitfulness in consequences, particularly in ‘verifiable’ consequences, i.e. consequences verifiable without the new axiom, whose proof with the help of the new axiom, however, are considerably simpler and easier to discover, and which make it possible to contract into one proof many different proofs […] There might exist axioms so abundant in their verifiable consequences, shedding so much light on a whole field, yielding such powerful methods for solving problems […] that, no matter whether or not they are intrinsically necessary, they would have to be accepted at least in the same sense as any well-established physical theory. (Gödel 1947, p. 477)[^gödel-1947]

This inspired Gödel to search for new axioms which can be extrinsically motivated and which can decide questions such as the *continuum hypothesis* which are highly independent of ZFC (cf. section 5.1).

Gödel shared Hilbert’s conviction that all mathematical questions have definite answers. But platonism in the philosophy of mathematics should not be taken to be ipso facto committed to holding that all set-theoretical propositions have determinate truth values. There are versions of platonism that maintain, for instance, that all theorems of ZFC are made true by determinate set-theoretical facts, but that there are no set-theoretical facts that make certain statements that are highly independent of ZFC truth-determinate. It seems that the famous set theorist Paul Cohen held some such view (Cohen 1971)[^cohen-1971].

### 3.2 Naturalism and Indispensability

Quine formulated a methodological critique of traditional philosophy. He suggested a different philosophical methodology instead, which has become known as *naturalism* (Quine 1969)[^quine-1969]. According to naturalism, our best theories are our best *scientific* theories. If we want to obtain the best available answer to philosophical questions such as *What* *do we know?* and *Which kinds of entities exist?*, we should not appeal to traditional epistemological and metaphysical theories. We should also refrain from embarking on a fundamental epistemological or metaphysical inquiry starting from first principles. Rather, we should consult and analyze our best scientific theories. They contain, albeit often implicitly, our currently best account of what exists, what we know, and how we know it.

Putnam applied Quine’s naturalistic stance to mathematical ontology (Putnam 1972)[^putnam-1972]. At least since Galilei, our best theories from the natural sciences are mathematically expressed. Newton’s theory of gravitation, for instance, relies heavily on the classical theory of the real numbers. Thus an ontological commitment to mathematical entities seems inherent to our best scientific theories. This line of reasoning can be strengthened by appealing to the Quinean thesis of confirmational holism. Empirical evidence does not bestow its confirmatory power on any one individual hypothesis. Rather, experience globally confirms the theory in which the individual hypothesis is embedded. Since mathematical theories are part and parcel of scientific theories, they too are confirmed by experience. Thus, we have empirical confirmation for mathematical theories. Even more appears true. It seems that mathematics is indispensable to our best scientific theories: it is not at all obvious how we *could* express them without using mathematical vocabulary. Hence the naturalist stance commands us to accept mathematical entities as part of our philosophical ontology. This line of argumentation is called an *indispensability argument* (Colyvan 2001)[^colyvan-2001].

If we take the mathematics that is involved in our best scientific theories at face value, then we appear to be committed to a form of platonism. But it is a more modest form of platonism than Gödel’s platonism. For it appears that the natural sciences can get by with (roughly) function spaces on the real numbers. The higher regions of transfinite set theory appear to be largely irrelevant to even our most advanced theories in the natural sciences. Nevertheless, Quine thought (at some point) that the sets that are postulated by ZFC are acceptable from a naturalistic point of view; they can be regarded as a generous rounding off of the mathematics that is involved in our scientific theories. Quine’s judgement on this matter is not universally accepted. Feferman, for instance, argues that all the mathematical theories that are essentially used in our currently best scientific theories are predicatively reducible (Feferman 2005)[^feferman-2005]. Maddy even argues that naturalism in the philosophy of mathematics is perfectly compatible with a non-realist view about sets (Maddy 2007, part IV)[^maddy-2007].

In Quine’s philosophy, the natural sciences are the ultimate arbiters concerning mathematical existence and mathematical truth. This has led Charles Parsons to object that this picture makes the obviousness of elementary mathematics somewhat mysterious (Parsons 1980)[^parsons-1980]. For instance, the question whether every natural number has a successor ultimately depends, in Quine’s view, on our best empirical theories; however, somehow this fact appears more immediate than that. In a kindred spirit, Maddy notes that mathematicians do not take themselves to be in any way restricted in their activity by the natural sciences. Indeed, one might wonder whether mathematics should not be regarded as a science in its own right, and whether the ontological commitments of mathematics should not be judged rather on the basis of the rational methods that are implicit in mathematical practice.

Motivated by these considerations, Maddy set out to inquire into the standards of existence implicit in mathematical practice, and into the implicit ontological commitments of mathematics that follow from these standards (Maddy 1990)[^maddy-1990]. She focussed on set theory, and on the methodological considerations that are brought to bear by the mathematical community on the question which large cardinal axioms can be taken to be true. Thus her view is closer to that of Gödel than to that of Quine. In more recent work, she isolates two maxims that seem to be guiding set theorists when contemplating the acceptability of new set theoretic principles: *unify* and *maximize* (Maddy 1997)[^maddy-1997]. The maxim “unify” is an instigation for set theory to provide a single system in which all mathematical objects and structures of mathematics can be instantiated or modelled. The maxim “maximize” means that set theory should adopt set theoretic principles that are as powerful and mathematically fruitful as possible.

### 3.3 Deflating Platonism

Bernays observed that when a mathematician is at work she “naively” treats the objects she is dealing with in a platonistic way. Every working mathematician, he says, is a platonist (Bernays 1935)[^bernays-1935]. But when the mathematician is caught off duty by a philosopher who quizzes her about her ontological commitments, she is apt to shuffle her feet and withdraw to a vaguely non-platonistic position. This has been taken by some to indicate that there is something wrong with philosophical questions about the nature of mathematical objects and of mathematical knowledge.

Carnap introduced a distinction between questions that are internal to a framework and questions that are external to a framework (Carnap 1950)[^carnap-1950]. It has been argued that Carnap’s distinction in some guise survives the demise of the logical empiricist framework in which it was first articulated (Burgess 2004b)[^burgess-2004b]. Tait has attempted to work out in detail how the resulting distinction can be applied to mathematics (Tait 2005)[^tait-2005]. This has resulted in what might be regarded as a deflationary versions of platonism.

According to Tait, questions of existence of mathematical entities can only be sensibly asked and reasonably answered from within (axiomatic) mathematical frameworks. If one is working in number theory, for instance, then one can ask whether there are prime numbers that have a given property. Such questions are then to be decided on purely mathematical grounds. Philosophers have a tendency to step outside the framework of mathematics and ask “from the outside” whether mathematical objects *really* exist and whether mathematical propositions are *really* true. In this question they are asking for supra-mathematical or metaphysical grounds for mathematical truth and existence claims. Tait argues that it is hard to see how any sense can be made of such external questions. He attempts to deflate them, and bring them back to where they belong: to mathematical practice itself. Of course not everyone agrees with Tait on this point. Linsky and Zalta have developed a systematic way of answering precisely the sort of external questions that Tait approaches with disdain (Linsky & Zalta 1995)[^linsky-1995].

It comes as no surprise that Tait has little use for Gödelian appeals to mathematical intuition in the philosophy of mathematics, or for the philosophical thesis that mathematical objects exist “outside space and time”. More generally, Tait believes that mathematics is not in need of a philosophical foundation; he wants to let mathematics speak for itself. In this sense, his position is reminiscent of the (in some sense Wittgensteinian) *natural ontological attitude* that is advocated by Arthur Fine in the realism debate in the philosophy of science.

### 3.4 Benacerraf’s Epistemological Problem

Benacerraf formulated an epistemological problem for a variety of platonistic positions in the philosophy of science (Benacerraf 1973)[^benacerraf-1973]. The argument is specifically directed against accounts of mathematical intuition such as that of Gödel. Benacerraf’s argument starts from the premise that our best theory of knowledge is the causal theory of knowledge. It is then noted that according to platonism, abstract objects are not spatially or temporally localized, whereas flesh and blood mathematicians are spatially and temporally localized. Our best epistemological theory then tells us that knowledge of mathematical entities should result from causal interaction with these entities. But it is difficult to imagine how this could be the case.

Today few epistemologists hold that the causal theory of knowledge is our best theory of knowledge. But it turns out that Benacerraf’s problem is remarkably robust under variation of epistemological theory. For instance, let us assume for the sake of argument that reliabilism is our best theory of knowledge. Then the problem becomes to explain how we succeed in obtaining reliable beliefs about mathematical entities.

Hodes has formulated a semantical variant of Benacerraf’s epistemological problem (Hodes 1984)[^hodes-1984][^hodes-1984-2]. According to our currently best semantic theory, causal-historical connections between humans and the world of concreta enable our words to refer to physical entities and properties. According to platonism, mathematics refers to abstract entities. The platonist therefore owes us a plausible account of how we (physically embodied humans) are able to refer to them. On the face of it, it appears that the causal theory of reference will be unable to supply us with the required account of the ‘microstructure of reference’ of mathematical discourse.

### 3.5 Plenitudinous Platonism

A version of platonism has been developed which is intended to provide a solution to Benacerraf’s epistemological problem (Linsky & Zalta 1995; Balaguer 1998)[^balaguer-1998][^linsky-1995]. This position is known as *plenitudinous platonism*. The central thesis of this theory is that every logically consistent mathematical theory *necessarily* refers to an abstract entity. Whether the mathematician who formulated the theory knows that it refers or does not know this, is largely immaterial. By entertaining a consistent mathematical theory, a mathematician automatically acquires knowledge about the subject matter of the theory. So, on this view, there is no epistemological problem to solve anymore.

In Balaguer’s version, plenitudinous platonism postulates a multiplicity of mathematical universes, each corresponding to a consistent mathematical theory. Thus, in particular a question such as the continuum problem (cf. section 5.1) does not receive a unique answer: in some set-theoretical universes the continuum hypothesis holds, in others it fails to hold. However, not everyone agrees that this picture can be maintained. Martin has developed an argument to show that multiple universes can always to a large extent be “accumulated” into a single universe (Martin 2001)[^martin-2001].

In Linsky and Zalta’s version of plenitudinous platonism, the mathematical entity that is postulated by a consistent mathematical theory has exactly the mathematical properties which are attributed to it by the theory. The abstract entity corresponding to ZFC, for instance, is *partial* in the sense that it neither makes the continuum hypothesis true nor false. The reason is that ZFC neither entails the continuum hypothesis nor its negation. This does not entail that all ways of consistently extending ZFC are on a par. Some ways may be fruitful and powerful, others less so. But the view does deny that certain consistent ways of extending ZFC are preferable because they consist of true principles, whereas others contain false principles.

## 4. Structuralism and Nominalism

Benacerraf’s work motivated philosophers to develop both structuralist and nominalist theories in the philosophy of mathematics (Reck & Price 2000)[^reck-2000]. And since the late 1980s, combinations of structuralism and nominalism have also been developed.

### 4.1 What Numbers Could Not Be

As if saddling platonism with one difficult problem were not enough (section 3.4), Benacerraf formulated a challenge for set-theoretic platonism (Benacerraf 1965)[^benacerraf-1965]. The challenge takes the following form.

There exist infinitely many ways of identifying the natural numbers with pure sets. Let us restrict, without essential loss of generality, our discussion to two such ways:

$$\begin{align*} \mathrm{I}{:} & \\ 0 &= \varnothing \\ 1 &= \{\varnothing\} \\ 2 &= \{\{\varnothing\}\} \\ 3 &= \{\{\{\varnothing\}\}\} \\ \vdots&\\ &\\ \mathrm{II}{:} & \\ 0 &= \varnothing \\ 1 &= \{\varnothing \} \\ 2 &= \{\varnothing , \{ \varnothing \}\}\\ 3 &= \{\varnothing , \{\varnothing \}, \{\varnothing , \{\varnothing \}\}\} \\ \vdots& \end{align*}$$

The simple question that Benacerraf asks is:

Which of these consists solely of true identity statements: I or II?

It seems very difficult to answer this question. It is not hard to see how a successor function and addition and multiplication operations can be defined on the number-candidates of I and on the number-candidates of II so that all the arithmetical statements that we take to be true come out true. Indeed, if this is done in the natural way, then we arrive at *isomorphic* structures (in the set-theoretic sense of the word), and isomorphic structures make the same sentences true (they are *elementarily equivalent*). It is only when we ask extra-arithmetical questions, such as ‘$1 \in 3$?’ that the two accounts of the natural numbers yield diverging answers. So it is impossible that both accounts are correct. According to story I, $3 = \{\{\{\varnothing \}\}\}$, whereas according to story II, $3 = \{\varnothing , \{\varnothing \}, \{\varnothing , \{\varnothing \}\}\}$. If both accounts were correct, then the transitivity of identity would yield a purely set theoretic falsehood.

Summing up, we arrive at the following situation. On the one hand, there appear to be no reasons why one account is superior to the other. On the other hand, the accounts cannot both be correct. This predicament is sometimes called labelled Benacerraf’s *identification problem*.

The proper conclusion to draw from this conundrum appears to be that neither account I nor account II is correct. Since similar considerations would emerge from comparing other reasonable-looking attempts to reduce natural numbers to sets, it appears that natural numbers are not sets after all. It is clear, moreover, that a similar argument can be formulated for the rational numbers, the real numbers… Benacerraf concludes that they, too, are not sets at all.

It is not at all clear whether Gödel, for instance, is committed to reducing the natural numbers to pure sets. A platonist can uphold the claim that the natural numbers can be embedded into the set-theoretic universe while maintaining that the embedding should not be seen as an ontological reduction. Indeed, on Linsky and Zalta’s plenitudinous platonist account, the natural numbers have no properties beyond those that are attributed to them by our theory of the natural numbers (Peano Arithmetic). But then it seems that platonists would have to take a similar line with respect to the rational numbers, the complex numbers, …. Whereas maintaining that the natural numbers are sui generis admittedly has some appeal, it is perhaps less natural to maintain that the complex numbers, for instance, are also sui generis. And, anyway, even if the natural numbers, the complex numbers, … are in some sense not reducible to anything else, one may wonder if there may not be another way to elucidate their nature.

### 4.2 *Ante Rem* Structuralism

Shapiro draws a useful distinction between *algebraic* and *non-algebraic mathematical theories* (Shapiro 1997)[^shapiro-1997]. Roughly, non-algebraic theories are theories which appear at first sight to be about a unique model: the *intended* model of the theory. We have seen examples of such theories: arithmetic, mathematical analysis… Algebraic theories, in contrast, do not carry a prima facie claim to be about a unique model. Examples are group theory, topology, graph theory…

Benacerraf’s challenge can be mounted for the objects that non-algebraic theories appear to describe. But his challenge does not apply to algebraic theories. Algebraic theories are not interested in mathematical objects per se; they are interested in structural aspects of mathematical objects. This led Benacerraf to speculate whether the same could not be true also of non-algebraic theories. Perhaps the lesson to be drawn from Benacerraf’s identification problem is that even arithmetic does not describe specific mathematical objects, but instead only describes structural relations?

Shapiro and Resnik hold that all mathematical theories, even non-algebraic ones, describe *structures*. This position is known as structuralism (Shapiro 1997; Resnik 1997)[^resnik-1997][^shapiro-1997]. Structures consists of places that stand in structural relations to each other. Thus, derivatively, mathematical theories describe places or positions in structures. But they do not describe objects. The number three, for instance, will on this view not be an object but a place in the structure of the natural numbers.

*Systems* are instantiations of structures. The systems that instantiate the structure that is described by a non-algebraic theory are isomorphic with each other, and thus, for the purposes of the theory, equally good. The systems I and II that were described in section 4.1 can be seen as instantiations of the natural number structure. $\{\{\{\varnothing \}\}\}$ and $\{\varnothing , \{\varnothing \}, \{\varnothing , \{\varnothing \}\}\}$ are equally suitable for playing the role of the number three. But neither *are* the number three. For the number three is an open place in the natural number structure, and this open place does not have any internal structure. Systems typically contain structural properties over and above those that are relevant for the structures that they are taken to instantiate.

Sensible identity questions are those that can be asked from within a structure. They are those questions that can be answered on the basis of structural aspects of the structure. Identity questions that go beyond a structure do not make sense. One can pose the question whether $3 \in 4$, but not cogently: this question involves a category mistake. The question mixes two different structures: $\in$ is a set-theoretical notion, whereas 3 and 4 are places in the structure of the natural numbers. This seems to constitute a satisfactory answer to Benacerraf’s challenge.

In Shapiro’s view, structures are not ontologically dependent on the existence of systems that instantiate them. Even if there were no infinite systems to be found in Nature, the structure of the natural numbers would exist. Thus structures as Shapiro understands them are abstract, platonic entities. Shapiro’s brand of structuralism is often labeled *ante rem* structuralism.

In textbooks on set theory we also find a notion of structure. Roughly, the set theoretic definition says that a structure is an ordered $n+1$-tuple consisting of a set, a number of relations on this set, and a number of distinguished elements of this set. But this cannot be the notion of structure that structuralism in the philosophy of mathematics has in mind. For the set theoretic notion of structure presupposes the concept of set, which, according to structuralism, should itself be explained in structural terms. Or, to put the point differently, a set-theoretical structure is merely a *system* that instantiates a structure that is ontologically prior to it.

Nonetheless, the motivation for extending ante rem structuralism even to the most encompassing mathematical discipline (set theory) is not entirely evident (Burgess 2015)[^burgess-2015]. Recall that the main motivation for arriving at a structuralist understanding of a mathematical discipline lies in Benacerraf’s identification problem. For set theory, it seems hard to mount an identification challenge: sets are not usually defined in terms of more primitive concepts.

It appears that *ante rem* structuralism describes the notion of a structure in a somewhat circular manner. A structure is described as places that stand in relation to each other, but a place cannot be described independently of the structure to which it belongs. Yet this is not necessarily a problem. For the *ante rem* structuralist, the notion of structure is a primitive concept, which cannot be defined in other more basic terms. At best, we can construct an axiomatic theory of mathematical structures.

But Benacerraf’s epistemological problem still appears to be urgent. Structures and places in structures may not be objects, but they are abstract. So it is natural to wonder how we succeed in obtaining knowledge of them. This problem has been taken by certain philosophers as a reason for developing a nominalist theory of mathematics and then to reconcile this theory with basic tenets of structuralism.

### 4.3 Mathematics Without Abstract Entities

Goodman and Quine tried early on to bite the bullet: they embarked on a project to reformulate theories from natural science without making use of abstract entities (Goodman & Quine 1947)[^goodman-1947]. The nominalistic reconstruction of scientific theories proved to be a difficult task. Quine, for one, abandoned it after this initial attempt. In the past decades many theories have been proposed that purport to give a nominalistic reconstruction of mathematics. (Burgess & Rosen 1997)[^burgess-1997] contains a good critical discussion of such views.

In a nominalist reconstruction of mathematics, concrete entities will have to play the role that abstract entities play in platonistic accounts of mathematics, and concrete relations (such as the part-whole relation) have to be used to simulate mathematical relations between mathematical objects. But here problems arise. First, already Hilbert observed that, given the discretization of nature in quantum mechanics, the natural sciences may in the end claim that there are only finitely many concrete entities (Hilbert 1925)[^hilbert-1925]. Yet it seems that we would need infinitely many of them to play the role of the natural numbers — never mind the real numbers. Where does the nominalist find the required collection of concrete entities? Secondly, even if the existence of infinitely many concrete objects is assumed, it is not clear that even elementary mathematical theories such as Primitive Recursive Arithmetic can be “simulated” by means of nominalistic relations (Niebergall 2000)[^niebergall-2000].

Field made an earnest attempt to carry out a nominalistic reconstruction of Newtonian mechanics (Field 1980)[^field-1980]. The basic idea is this. Field wanted to use concrete surrogates of the real numbers and functions on them. He adopted a realist stance toward the spatial continuum, and took regions of space to be as physically real as chairs and tables. And he took regions of space to be concrete (after all, they are spatially located). If we also count the very disconnected ones, then there are as many regions of Newtonian space as there are subsets of the real numbers. And then there are enough concrete entities to play the role of the natural numbers, the real numbers, and functions on the real numbers. And the theory of the real numbers and functions on them is all that is needed to formulate Newtonian mechanics. Of course it would be even more interesting to have a nominalistic reconstruction of a truly contemporary scientific theory such as Quantum Mechanics. But given that the project can be carried out for Newtonian mechanics, some degree of initial optimism seems justified.

This project clearly has its limitations. It may be possible nominalistically to interpret theories of function spaces on the real numbers, say. But it seems far-fetched to think that along Fieldian lines a nominalistic interpretation of set theory can be found. Nevertheless, if it is successful within its confines, then Field’s program has really achieved something. For it would mean that, to some extent at least, mathematical entities appear to be dispensable after all. He would thereby have taken an important step towards undermining the indispensability argument for Quinean modest platonism in mathematics, for, to some extent, mathematical entities appear to be dispensable after all.

Field’s strategy only has a chance of working if Hilbert’s fear that in a very fundamental sense our best scientific theories may entail that there are only finitely many concrete entities, is ill-founded. If one sympathizes with Hilbert’s concern but does not believe in the existence of abstract entities, then one might bite the bullet and claim that there are only finitely many *mathematical* entities, thus contradicting the basic principles of elementary arithmetic. This leads to a position that has been called *ultra-finitism* (Essenin-Volpin 1961)[^essenin-volpin-1961].

On most accounts, ultra-finitism leads, like intuitionism, to revisionism in mathematics. For it would seem that one would then have to say that there is a largest natural number, for instance. From the outside, a theory postulating only a finite mathematical universe appears proof-theoretically weak, and therefore very likely to be consistent. But Woodin has developed an argument that purports to show that from the ultra-finitist perspective, there are no grounds for asserting that the ultra-finitist theory is likely to be consistent (Woodin 2011)[^woodin-2011].

Regardless of this argument (the details of which are not discussed here), many already find the assertion that there is a largest number hard to swallow. But Lavine has articulated a sophisticated form of set-theoretical ultra-finitism which is mathematically non-revisionist (Lavine 1994)[^lavine-1994]. He has developed a detailed account of how the principles of ZFC can be taken to be principles that describe determinately finite sets, if these are taken to include indefinitely large ones.

### 4.4 *In Rebus* structuralism

Field’s physicalist interpretation of arithmetic and analysis not only undermines the Quine-Putnam indispensability argument. It also partially provides an answer to Benacerraf’s epistemological challenge. Admittedly it is not a simple task to give an account of how humans obtain knowledge of spacetime regions. But at least according to many (but not all) philosophers spacetime regions are physically real. So we are no longer required to explicate how flesh and blood mathematicians stand in contact with non-physical entities. But Benacerraf’s identification problem remains. One may wonder why one spacetime point or region rather than another plays the role of the number *π*, for instance.

In response to the identification problem, it seems attractive to combine a structuralist approach with Field’s nominalism. This leads to versions of *nominalist structuralism*, which can be outlined as follows. Let us focus on mathematical analysis. The nominalist structuralist denies that any concrete physical system is the unique intended interpretation of analysis. All concrete physical systems that satisfy the basic principles of Real Analysis (RA) would do equally well. So the content of a sentence *φ* of the language of analysis is (roughly) given by:

Every concrete system S that makes RA true, also makes *φ* true.

This entails that, as with *ante rem* structuralism, only structural aspects are relevant to the truth or falsehood of mathematical statements. But unlike *ante rem* structuralism, no *abstract* structure is postulated above and beyond concrete systems.

According to *in rebus* structuralism, no abstract structures exist over and above the systems that instantiate them; structures exist only *in* the systems that instantiate them. For this reason nominalist *in rebus* structuralism is sometimes described as “structuralism without structures”. Nominalist structuralism is a form of *in rebus* structuralism. But *in rebus* structuralism is not exhausted by nominalist structuralism. Even the version of platonism that takes mathematics to be about structures in the set-theoretic sense of the word can be viewed as a form of *in rebus* structuralism.

In mathematical discourse, non-algebraic structures (such as ‘the’ natural numbers) and mathematical objects (such as ‘the’ number 1) are referred to by definite descriptions. This strongly suggests that mathematical symbols (N, 1) have a unique reference rather than a ‘distributed’ one as *in rebus* structuralism would have it. But *in rebus* structuralists argue that such mathematical symbols function as *dedicated variables* in much the same way as in ‘Tommy needs his letters from home’, a world war II slogan, the name ‘Tommy’ is chosen to stand for some arbitrary concrete soldier, and re-used on many occasions without changing its reference (Pettigrew 2008)[^pettigrew-2008].

If Hilbert’s worry is wellfounded in the sense that there are no concrete physical systems that make the postulates of mathematical analysis true, then the above nominalist structuralist rendering of the content of a sentence *φ* of the language of analysis gets the truth conditions of such sentences wrong. For then for *every* universally quantified sentence *φ*, its paraphrase will come out vacuously true. So an existential assumption to the effect that there exist concrete physical systems that can serve as a model for RA is needed to back up the above analysis of the content of mathematical statements. Perhaps something like Field’s construction fits the bill.

Putnam noticed early on that if the above explication of the content of mathematical sentences is modified somewhat, a substantially weaker background assumption is sufficient to obtain the correct truth conditions (Putnam 1967)[^putnam-1967]. Putnam proposed the following *modal* rendering of the content of a sentence *φ* of the language of analysis:

*Necessarily*, every concrete system S that makes RA true, also makes *φ* true.

This is a stronger statement than the nonmodal rendering that was presented earlier. But it seems equally plausible. And an advantage of this rendering is that the following modal existential background assumption is sufficient to make the truth conditions of mathematical statements come out right:

*It is possible* that there exists a concrete physical system that can serve as a model for RA.

(‘It is possible that’ here means ‘It is or might have been the case that’.) Now Hilbert’s concern seems adequately addressed. For on Putnam’s account, the truth of mathematical sentences no longer depends on physical assumptions about the actual world.

It is admittedly not easy to give a satisfying account of how we *know* that this modal existential assumption is fulfilled. But it may be hoped that the task is less daunting than the task of explaining how we succeed in knowing facts about abstract entities. And it should not be forgotten that the structuralist aspect of this (modal) nominalist position keeps Benacerraf’s identification challenge at bay.

Putnam’s strategy also has its limitations. Chihara sought to apply Putnam’s strategy not only to arithmetic and analysis but also to set theory (Chihara 1973)[^chihara-1973]. Then a crude version of the relevant modal existential assumption becomes:

*It is possible* that there exist concrete physical systems that can serve as a model for ZFC.

Parsons has noted that when possible worlds are needed which contain collections of physical entities that have large transfinite cardinalities or perhaps are even too large to have a cardinal number, it becomes hard to see these as possible concrete or physical systems (Parsons 1990a)[^parsons-1990a]. We seem to have no reason to believe that there could be *physical* worlds that contain highly transfinitely many entities.

### 4.5 Fictionalism

According to the previous proposals, the statements of ordinary mathematics are true when suitably, i.e., nominalistically, interpreted. The nominalistic account of mathematics that will now be discussed holds that all existential mathematical statements are false simply because there are no mathematical entities. (For the same reason all universal mathematical statements will be trivially true.)

Fictionalism holds that mathematical theories are like fiction stories such as fairy tales and novels. Mathematical theories describe fictional entities, in the same way that literary fiction describes fictional characters. This position was first articulated in the introductory chapter of (Field 1989)[^field-1989], and has in recent years been gaining in popularity.

This crude description of the fictionalist position immediately opens up the question what sort of entities fictional entities are. This appears to be a deep metaphysical ontological problem. One way to avoid this question altogether is to deny that there exist fictional entities. Mathematical theories should be viewed as invitations to participate in games of pretence, in which we act as if certain mathematical entities exist. Pretence or make-believe operators shield their propositional objects from existential exportation (Leng 2010)[^leng-2010].

Anyway, as said above, on the fictionalist view, a mathematical theory isn’t literally true. Nonetheless, mathematics is used to get truths across. So we must *subtract* something from what is literally said when we assert a physical theory that involves mathematics, if we want to get at the truth. But this requires a *theory* of how this subtraction of content works. Such a theory has been developed in (Yablo, 2014)[^yablo-2014].

If the fictionalist thesis is correct, then one demand that must be imposed on mathematical theories is surely consistency. Yet Field adds to this a second requirement: mathematics must be *conservative* over natural science. This means, roughly, that whenever a statement of an empirical theory can be derived using mathematics, it can in principle also be derived without using any mathematical theories. If this were not the case, then an indispensability argument could be played out against fictionalism. Whether mathematics is in fact conservative over physics, for instance, is currently a matter of controversy. Shapiro has formulated an incompleteness argument that intends to refute Field’s claim (Shapiro 1983)[^shapiro-1983].

If there are indeed no mathematical (fictional) entities, as one form of fictionalism has it, then Benacerraf’s epistemological problem does not arise. Fictionalism then shares this advantage over most forms of platonism with nominalistic reconstructions of mathematics. But the appeal to pretence operators entails that the logical form of mathematical sentences then differs somewhat from their surface form. If there are fictional objects, then the surface form of mathematical sentences can be taken to coincide with their logical form. But if they exist as abstract entities, then Benacerraf’s epistemological problem reappears.

Whether Benacerraf’s identification problem is solved is not completely clear. In general, fictionalism is a non-reductionist account. Whether an entity in one mathematical theory is identical with an entity that occurs in another theory is usually left indeterminate by mathematical “stories”. Yet Burgess has rightly emphasized that mathematics differs from literary fiction in the fact that fictional characters are usually confined to one work of fiction, whereas the same mathematical entities turn up in diverse mathematical theories (Burgess 2004)[^burgess-2004]. After all, entities with the same *name* (such as $\pi)$ turn up in different theories. Perhaps the fictionalist can maintain that when mathematicians develop a new theory in which an “old” mathematical entity occurs, the entity in question is made more precise. More determinate properties are ascribed to it than before, and this is all right as long as overall consistency is maintained.

The canonical objection to formalism seems also applicable to fictionalism. The fictionalists should find some explanation of the fact that extending a mathematical theory in one way, is often considered preferable over continuing it in a another way that is incompatible with the first. There is often at least an appearance that there is a right way to extend a mathematical theory.

## 5. Special Topics

In recent years, subdisciplines of the philosophy of mathematics have started to arise. They evolve in a way that is not completely determined by the “big debates” about the nature of mathematics. In this section, we look at a few of these disciplines.

### 5.1 Foundations and Set Theory

Many regard set theory as in some sense the foundation of mathematics. It seems that just about any piece of mathematics can be carried out in set theory, even though it is sometimes an awkward setting for doing so. In recent years, the philosophy of set theory is emerging as a philosophical discipline of its own. This is not to say that in specific debates in the philosophy of set theory it cannot make an enormous difference whether one approaches it from a formalistic point of view or from a platonistic point of view, for instance.

The thesis that set theory is most suitable for serving as the foundations of mathematics is by no means uncontroversial. Over the past decades, *category theory* has presented itself as a rival for this role. Category theory is a mathematical theory that was developed in the middle of the twentieth century. Unlike in set theory, in category theory mathematical objects are *only* defined up to isomorphism. This means that Benacerraf’s identification problem cannot be raised for category theoretical concepts and ‘objects’. At the same time, (roughly) everything that can be done in set theory can be done in category theory (but not always in a natural manner), and vice versa (again not always in a natural manner). This means that for a structuralist perspective, category theory is an attractive candidate for providing the foundations of mathematics (McLarty 2004)[^mclarty-2004].

One question that has been important from the beginning of set theory concerns the difference between sets and proper classes. (This question has a natural counterpart for category theory: the difference between small and large categories.) Cantor’s diagonal argument forces us to recognize that the set-theoretical universe as a whole cannot be regarded as a set. Cantor’s Theorem shows that the power set (i.e., the set of all subsets) of any given set has a larger cardinality than the given set itself. Now suppose that the set-theoretical universe forms a set: the set of all sets. Then the power set of the set of all sets would have to be a subset of the set of all sets. This would contradict the fact that the power set of the set of all sets would have a larger cardinality than the set of all sets. So we must conclude that the set-theoretical universe cannot form a set.

Cantor called pluralities that are too large to be considered as a set *inconsistent multiplicities* (Cantor 1932)[^cantor-1932]. Today, Cantor’s inconsistent multiplicities are called *proper classes*. Some philosophers of mathematics hold that proper classes still constitute unities, and hence can be seen as a sort of collection. They are, in a Cantorian spirit, just collections that are too large to be sets. Nevertheless, there are problems with this view. Just as there can be no set of all sets, there can for diagonalization reasons also not be a proper class of all proper classes. So the proper class view seems compelled to recognize in addition a realm of super-proper classes, and so on. For this reason, Zermelo claimed that proper classes simply do not exist. This position is less strange than it looks at first sight. On close inspection, one sees that in ZFC one never needs to quantify over entities that are too large to be sets (although there exist systems of set theory that do quantify over proper classes). On this view, the set-theoretical universe is potentially infinite in an absolute sense of the word. It never exists as a completed whole, but is forever growing, and hence forever unfinished (Zermelo 1930)[^zermelo-1930]. This way of speaking indicates that in our attempts to understand this notion of potential infinity, we are drawn to temporal metaphors. It is not surprising that these temporal metaphors cause some philosophers of mathematics acute discomfort. For this reason, contemporary philosophers of mathematics who are sympathetic to Zermelo’s potentialist interpretation of the set theoretic universe, tend to regard the modality involved in this interpretation as a non-temporal one: the nature of this modality is hotly debated (Linnebo 2013, Studd 2019)[^linnebo-2013][^studd-2019].

A second subject in the philosophy of set theory concerns the justification of the accepted basic principles of mathematics, i.e., the axioms of ZFC. An important historical case study is the process by which the Axiom of Choice came to be accepted by the mathematical community in the early decades of the twentieth century (Moore 1982)[^moore-1982]. The importance of this case study is largely due to the fact that an open and explicit discussion of its acceptability was held in the mathematical community. In this discussion, general reasons for accepting or refusing to accept a principle as a basic axiom came to the surface. On the systematic side, two conceptions of the notion of set have been elaborated which aim to justify all axioms of ZFC in one fell swoop. On the one hand, there is the *iterative conception* of sets, which describes how the set-theoretical universe can be thought of as generated from the empty set by means of the power set operation (Boolos 1971, Linnebo 2013)[^boolos-1971][^linnebo-2013]. On the other hand, there is the *limitation of size* conception of sets, which states that every collection which is not too big to be a set, is a set (Hallett 1984)[^hallett-1984]. The iterative conception motivates some axioms of ZFC very well (the power set axiom, for instance), but fares less well with respect to other axioms, such as the replacement axiom (Potter 2004, Part IV)[^potter-2004]. The limitation of size conception motivates other axioms better (such as the restricted comprehension axiom). It seems fair to say that there is no *uniform* conception that clearly justifies all axioms of ZFC.

The motivation of putative axioms that go beyond ZFC constitutes a third concern of the philosophy of set theory (Maddy 1988; Martin 1998)[^maddy-1988][^martin-1998]. One such class of principles is constituted by the *large cardinal axioms*. Nowadays, large cardinal hypotheses are really taken to mean some kind of embedding properties between the set theoretic universe and inner models of set theory (Kanamori 2009)[^kanamori-2009]. Most of the time, large cardinal principles entail the existence of sets that are larger than any sets which can be guaranteed by ZFC to exist.

The weaker of the large cardinal principles are supported by intrinsic evidence (see section 3.1). They follow from what are called *reflection principles*. These are principles that state that the set theoretic universe as a whole is so rich that it is very similar to some set-sized initial segment of it. The stronger of the large cardinal principles hitherto only enjoy extrinsic support. Many researchers are skeptical about the possibility that reflection principles, for instance, can be found that support them (Koellner 2009)[^koellner-2009]; others, however, disagree (Welch & Horsten 2016)[^horsten-2016][^welch-2016].

Gödel hoped that on the basis of such large cardinal axioms, the most important open question of set theory could eventually be settled. This is the *continuum problem*. The *continuum hypothesis* was proposed by Cantor in the late nineteenth century. It states that there are no sets S which are too large for there to be a one-to-one correspondence between S and the natural numbers, but too small for there to exist a one-to-one correspondence between S and the real numbers. Despite strenuous efforts, all attempts to settle the continuum problem failed. Gödel came to suspect that the continuum hypothesis is independent of the accepted principles of set theory (ZFC). Around 1940, he managed to show that the continuum hypothesis is consistent with ZFC. A few decades later, Paul Cohen proved that the negation of the continuum hypothesis is also consistent with ZFC. Thus Gödel’s conjecture of the independence of the continuum hypothesis was eventually confirmed.

But Gödel’s hope that large cardinal axioms could solve the continuum problem turned out to be unfounded. The continuum hypothesis is independent of ZFC even in the context of large cardinal axioms. Nevertheless, large cardinal principles have manage to settle restricted versions of the continuum hypothesis (in the affirmative). The existence of so-called Woodin cardinals ensures that sets definable in analysis are either countable or the size of the continuum. Thus the *definable continuum problem* is settled.

In recent years, attempts have been focused on finding principles of a different kind which might be justifiable and which might yet decide the continuum hypothesis (Woodin 2001a, Woodin 2001b)[^woodin-2001a][^woodin-2001b]. One of the more general philosophical questions that have emerged from this research is the following: which conditions have to be satisfied in order for a principle to be a putative basic axiom of mathematics?

Some of the researchers who seek to decide the continuum hypothesis think that it is true; others think that it is false. But there are also many set theorists and philosophers of mathematics who believe that the continuum hypothesis not just undecidable in ZFC but *absolutely undecidable*, i.e. that it is neither provable (in the informal sense of the word) nor disprovable (in the informal sense of the word) because it is neither true nor false. If the mathematical universe is a *set theoretic multiverse*, for instance, then there are equally models that make the continuum hypothesis true and equally good models that make it false, and there is no more to be said (Hamkins, 2015)[^hamkins-2015].

### 5.2 Categoricity and Pluralism

In the second half of the nineteenth century Dedekind proved that the basic axioms of arithmetic have, up to isomorphism, exactly one model, and that the same holds for the basic axioms of Real Analysis. If a theory has, up to isomorphism, exactly one model, then it is said to be *categorical*. So modulo isomorphisms, arithmetic and analysis each have exactly one intended model. Half a century later Zermelo proved that the principles of set theory are “almost” categorical or *quasi-categorical*: for any two models $M_1$ and $M_2$ of the principles of set theory, either $M_1$ is isomorphic to $M_2$, or $M_1$ is isomorphic to a strongly inaccessible rank of $M_2$, or $M_2$ is isomorphic to a strongly inaccessible rank of $M_1$ (Zermelo 1930)[^zermelo-1930]. In recent years, attempts have been made to develop arguments to the effect that Zermelo’s conclusion can be strengthened to a full categoricity assertion (McGee 1997; Martin 2001)[^martin-2001][^mcgee-1997], but we will not discuss these arguments here.

At the same time, the Löwenheim-Skolem theorem says that every first-order formal theory that has at least one model with an infinite domain, must have models with domains of all infinite cardinalities. Since the principles of arithmetic, analysis and set theory had better possess at least one infinite model, the Löwenheim-Skolem theorem appears to apply to them. Is this not in tension with Dedekind’s categoricity theorems?

The solution of this conundrum lies in the fact that Dedekind did not even implicitly work with first-order formalizations of the basic principles of arithmetic and analysis. Instead, he informally worked with *second-order* formalizations.

Let us focus on arithmetic to see what this amounts to. The basic postulates of arithmetic contain the induction axiom. In first-order formalizations of arithmetic, this is formulated as a scheme: for each first-order arithmetical formula of the language of arithmetic with one free variable, one instance of the induction principle is included in the formalization of arithmetic. Elementary cardinality considerations reveal that there are infinitely many properties of natural numbers that are not expressed by a first-order formula. But intuitively, it seems that the induction principle holds for *all* properties of natural numbers. So in a first-order language, the full force of the principle of mathematical induction cannot be expressed. For this reason, a number of philosophers of mathematics insist that the postulates of arithmetic should be formulated in a *second-order language* (Shapiro 1991)[^shapiro-1991]. Second-order languages contain not just first-order quantifiers that range over elements of the domain, but also second-order quantifiers that range over properties (or subsets) of the domain. In *full* second-order logic, it is insisted that these second-order quantifiers range over *all* subsets of the domain. If the principles of arithmetic are formulated in a second-order language, then Dedekind’s argument goes through and we have a categorical theory. For similar reasons, we also obtain a categorical theory if we formulate the basic principles of real analysis in a second-order language, and the second-order formulation of set theory turns out to be quasi-categorical.

*Ante rem* structuralism, as well as the modal nominalist structuralist interpretation of mathematics, could benefit from a second-order formulation. If the *ante rem* structuralist wants to insists that the natural number structure is fixed up to isomorphism by the Peano axioms, then she will want to formulate the Peano axioms in second-order logic. And the modal nominalist structuralist will want to insist that the relevant concrete systems for arithmetic are those that make the *second-order* Peano axioms true (Hellman 1989)[^hellman-1989]. Similarly for real analysis and set theory. Thus the appeal to second-order logic appears as the final step in the structuralist project of isolating the intended models of mathematics.

Yet appeal to second-order logic in the philosophy of mathematics is by no means uncontroversial. A first objection is that the ontological commitment of second-order logic is higher than the ontological commitment of first-order logic. After all, use of second-order logic seems to commit us to the existence of abstract objects: classes. In response to this problem, Boolos has articulated an interpretation of second-order logic which avoids this commitment to abstract entities (Boolos 1985)[^boolos-1985]. His interpretation spells out the truth clauses for the second-order quantifiers in terms of plural expressions, without invoking classes. For instance, an second-order expression of the form $\exists x F(x)$ is interpreted as: “there are some (*first-order* objects) *x* such that they have the property *F*”. This interpretation is called the *plural interpretation* of second-order logic. It is controversial whether there is a real difference between the mathematical use of pluralities and of sets (Linnebo 2003)[^linnebo-2003]. Nevertheless it is clear that an appeal to the plural interpretation of second-order logic will be tempting for nominalist versions of structuralism.

A second objection against second-order logic can be traced back to Quine (Quine 1970)[^quine-1970]. This objection states that the interpretation of full second-order logic is connected with set-theoretical questions. This is already indicated by the fact that most regimentations of second-order logic adopt a version of the axiom of choice as one of its axioms. But more worrisome is the fact that second-order logic is inextricably intertwined with deep problems in set theory, such as the continuum hypothesis. For theories such as arithmetic that intend to describe an infinite collection of objects, even a matter as elementary as the question of the cardinality of the range of the second-order quantifiers, is equivalent to the continuum problem. Also, it turns out that there exists a sentence which is a second-order logical truth if and only if the continuum hypothesis holds (Boolos 1975)[^boolos-1975]. We have seen that the continuum problem is independent of the currently accepted principles of set theory. And many researchers believe it to be absolutely truth-valueless. If this is so, then there is an inherent indeterminacy in the very notion of second-order infinite model. And many contemporary philosophers of mathematics take the latter not to have a determinate truth value. Thus, it is argued, the very notion of an (infinite) model of full second-order logic is inherently indeterminate.

If one does not want to appeal to full second-order logic, then there are other ways to ensure categoricity of mathematical theories. One idea would be to make use of quantifiers which are somehow intermediate between first-order and second-order quantifiers. For instance, one might treat “there are finitely many *x*” as a primitive quantifier. This will allow one to, for instance, construct a categorical axiomatization of arithmetic.

But ensuring categoricity of mathematical theories does not require introducing stronger quantifiers. Another option would be to take the informal concept of algorithmic computability as a primitive notion (Halbach & Horsten 2005; Horsten 2012)[^halbach-2005][^horsten-2012]. A theorem of Tennenbaum states that all first-order models of Peano Arithmetic in which addition and multiplication are computable functions, are isomorphic to each other. Now *our* operations of addition and multiplication are computable: otherwise we could never have learned these operations. This, then, is another way in which we may be able to isolate the intended models of our principles of arithmetic. Against this account, however, it may be pointed out that it seems that the categoricity of intended models for real analysis, for instance, cannot be ensured in this manner. For computation on models of the principles of real analysis, we do not have a theorem that plays the role of Tennenbaum’s theorem.

If one accepts a certain open-endedness of the collection of arithmetical predicates, then a categoricity theorem of sorts for arithmetic can be obtained without overstepping the bounds of first-order logic and without appealing to an informal concept of computability. Suppose that there are two mathematicians, A and B, who both assert the first-order Peano-axioms in their own idiolect. Suppose furthermore that A and B regard the collection of predicates for which mathematical induction is permissible as open-ended, and are both willing to accept the other’s induction scheme as true. Then A and B have the wherewithal to convince themselves that both idiolects describe isomorphic structures (Parsons 1990b)[^parsons-1990b]. Such arguments are called internal categoricity arguments. They are widely debated in contempory philosophy of mathematics: see for instance (Button & Walsh 2019).

Many of those who are sceptical of the philosophical use of categoricity argments in the philosophy of mathematics take all of our consistent mathematical theories to have many structurally different models, and take all or many of those models to be on a par with one another. As we saw in the previous sub-section, the set theoretic multiverse view is a case in point, and so is set theoretic potentialism. But one can go further, and defend the thesis that any consistent mathematical theory describes a free-standing mathematical universe, and that no such theory is more true than any other (Linsky & Zalta 1995, Bueno 2011)[^bueno-2011][^linsky-1995].

These theories belong to a family of views that is called *mathematical pluralism*, which is an increasingly prominent theme in the philosophy of mathematics. Historically, this constellation of views has roots in the work of Hilbert and of Carnap. In a debate with Frege, Hilbert insisted that consistency suffices for a mathematical theory to have a subject matter (Resnik 1974)[^resnik-1974]; Carnap argued that choice between alternative large-scale theories (frameworks) is ultimately never more than a *pragmatic* matter (Carnap 1950)[^carnap-1950].

As is everywhere the case in philosophy, there is disagreement here: for a critique of the doctrine that mathematical truth is an irrevocably use-relative notion, see (Koellner 2009b)[^koellner-2009b], and for a retort, see (Warren 2015)[^warren-2015]. Some react to mathematical pluralism by taking it one step further still, and argue that also all inconsistent mathematical theories should be regarded as true (in a relativised sense). Moreover, some mathematical theories that are trivial in the sense of being inconsistent, are commonly taken to be just as *valuable* as many venerable consistent ones: “Historically, there are three [to the author’s knowledge] mathematical theories which had a profound impact on mathematics and logic, and were found to be trivial. There are Cantor’s naive set theory, Frege’s formal theory of logic and the first version of Church’s formal theory of mathematical logic. All three had profound reprecussions on subsequent mathematics” (Friend 2013, p. 294)[^friend-2013].

### 5.3 Computation

Until fairly recently, the subject of computation did not receive much attention in the philosophy of mathematics. This may be due in part to the fact that in Hilbert-style axiomatizations of number theory, computation is reduced to proof in Peano Arithmetic. But this situation has changed in recent years. It seems that along with the increased importance of computation in mathematical practice, philosophical reflections on the notion of computation will occupy a more prominent place in the philosophy of mathematics in the years to come.

Church’s Thesis occupies a central place in computability theory. It says that every algorithmically computable function on the natural numbers can be computed by a Turing machine.

As a principle, Church’s Thesis has a somewhat curious status. It appears to be a *basic* principle. On the one hand, the principle is almost universally held to be true. On the other hand, it is hard to see how it can be mathematically proved. The reason is that its antecedent contains an informal notion (algorithmic computability) whereas its consequent contains a purely mathematical notion (Turing machine computability). Mathematical proofs can only connect purely mathematical notions—or so it seems. The received view was that our evidence for Church’s Thesis is quasi-empirical. Attempts to find convincing counterexamples to Church’s Thesis have come to naught. Independently, various proposals have been made to mathematically capture the algorithmically computable functions on the natural numbers. Instead of Turing machine computability, the notions of general recursiveness, Herbrand-Gödel computability, lambda-definability… have been proposed. But these mathematical notions all turn out to be equivalent. Thus, to use Gödelian terminology, we have accumulated extrinsic evidence for the truth of Church’s Thesis.

Kreisel pointed out long ago that even if a thesis cannot be formally proved, it may still be possible to obtain intrinsic evidence for it from a rigorous but informal analysis of intuitive notions (Kreisel 1967)[^kreisel-1967]. Kreisel calls these exercises in *informal rigour*. Detailed scholarship by Sieg revealed that the seminal article (Turing 1936)[^turing-1936] constitutes an exquisite example of just this sort of analysis of the intuitive concept of algorithmic computability (Sieg 1994)[^sieg-1994].

Currently, the most active subjects of investigation in the domain of foundations and philosophy of computation appear to be the following. First, energy has been invested in developing theories of algorithmic computation on structures other than the natural numbers. In particular, efforts have been made to obtain analogues of Church’s Thesis for algorithmic computation on various structures. In this context, substantial progress has been made in recent decades in developing a theory of effective computation on the real numbers (Pour-El 1999)[^pour-el-1999]. Second, attempts have been made to explicate notions of computability other than algorithmic computability by humans. One area of particular interest here is the area of *quantum computation* (Deutsch *et al*. 2000)[^deutsch-2000].

### 5.4 Mathematical Proof

We know much about the concepts of *formal proof* and *formal provability*, their connection with algorithmic computability, and the principles by which these concepts are governed. We know, for instance, that the proofs of a formal system are computably enumerable, and that provability in a sound (strong enough) formal system is subject to Gödel’s incompleteness theorems. But a mathematical proof as you find it in a mathematical journal is not a formal proof in the sense of the logicians: it is a (rigorous) *informal proof* (Myhill 1960, Detlefsen 1992, Antonutti 2010)[^antonutti-2010][^myhill-1960].

First, whereas the collection of sentences provable in a formal system is always computably enumerable, we know much less about the *extension* of the concept of informal provability. Lucas (Lucas 1961)[^lucas-1961], and later Penrose (Penrose 1989, 1994)[^penrose-1989][^penrose-1994], have argued that informal mathematical provability outstrips provability in any given formal system. But their arguments are widely regarded as unpersuasive. Benacerraf has argued against Lucas and Penrose that it cannot be excluded that there is a formal system $T$ such that in fact mathematical provability extensionally coincides with provability in $T$, even though we cannot know that it does (Benacerraf 1967)[^benacerraf-1967]. Others have argued that the concept of informal mathematical provability is not even clear enough for the question whether its extension is computably enumerable to have a definite answer (Horsten & Welch 2016)[^horsten-2016][^welch-2016].

Second, there is no agreement about what the *standard* is for an argument to qualify as a mathematical proof. According to what may be called the received view, a mathematical argument for a statement $p$ constitutes an informal mathematical proof if the argument allows a competent mathematician to transform it into a *formal deduction* of $p$ from generally accepted mathematical axioms (Avigad 2021)[^avigad-2021]. An informal mathematical proof can then be taken to be a *derivation-indicator* for $p$ (Azzouni 2004)[^azzouni-2004]. But the received view of the standard of mathematical proof has come under attack in recent years. It has been argued, for instance, that the interpolations of reasons in an informal mathematical proof until a logically correct and non-elliptical first-order derivation is reached, can be an *infinite* process (Rav 1999, p.14-15)[^rav-1999]. Others are mounting a defence of the received view, so that there is a lively debate about these issues at the moment (Tatton-Brown forthcoming, Di Toffoli 2021)[^di-2021].

The past decades have witnessed the first occurrences of mathematical proofs in which computers appear to play an essential role. The four-colour theorem is one example. It says that for every map, only four colours are needed to colour countries in such a way that no two countries that have a common border receive the same color. This theorem was proved in 1976 (Appel et al. 1977)[^appel-1977]. But the proof distinguishes many cases which were verified by a computer. These computer verifications are too long to be double-checked by humans. The proof of the four colour theorem gave rise to a debate about the question to what extent computer-assisted proofs count as proofs in the true sense of the word.

The received view has it that mathematical proofs yield a priori knowledge. Yet when we rely on a computer to generate part of a proof, we appear to rely on the proper functioning of computer hardware and on the correctness of a computer program. These appear to be empirical factors. Thus one is tempted to conclude that computer proofs yield *quasi-empirical* knowledge (Tymoczko 1979)[^tymoczko-1979]. In other words, through the advent of computer proofs the notion of proof has lost its purely a priori character. Burge, in contrast, held the view that because the empirical factors on which we rely when we accept computer proofs do not appear as premises in the argument, computer proofs can yield a priori knowledge after all (Burge 1998)[^burge-1998]. (Burge later retracted this claim: see (Burge 2013, p.31)[^burge-2013].)

## 6. The Future

In the twentieth century, research in the philosophy of mathematics revolved mostly around the nature of mathematical objects, the fundamental laws that govern them, and how we acquire mathematical knowledge about them. These are *foundational concerns* that are intimately connected with traditional metaphysical and epistemological questions.

In the second half of the twentieth century, research in the philosophy of science to a significant extent moved away from foundational concerns. Instead, philosophical questions relating to the growth of scientific knowledge and of scientific understanding became more central. As early as the 1970s, there were voices that argued that a similar shift of attention should take place in the philosophy of mathematics. Lakatos initiated the philosophical *investigation of the evolution of mathematical concepts* (Lakatos 1976)[^lakatos-1976]. He argued that the content of a mathematical concept evolves in roughly the following way. A mathematician formulates a deep conjecture, but is unable to prove it. Then counterexamples against the conjecture are found. In response, the definition of one or more central concepts in the conjecture is changed in such a way that the counterexamples are at least eliminated. Still the thus revised conjecture cannot be proved, and gradually new counterexamples appear. The procedure of revising the definition of one or more central concepts is applied again and again, until a proof of the conjecture is found. Lakatos calls this procedure *concept stretchin*g. In recent decades, Lakatos’ model of concept change in mathematics has been revised and refined (Mormann 2002)[^mormann-2002].

For some decades, the view that the philosophy of mathematics should take a historical and sociological turn remained restricted to a somewhat marginal school of thought in the philosophy of mathematics. However, in recent years the opposition between this new movement of mathematical practice on the one hand, and ‘mainstream’ philosophy of mathematics on the other hand, is softening. Philosophical questions relating to mathematical practice, the evolution of mathematical theories, and mathematical explanation and understanding have become more prominent, and have been related to more traditional themes from the philosophy of mathematics (Mancosu 2008)[^mancosu-2008]. This trend will doubtlessly continue in the years to come.

For an example, let us briefy return to the subject of computer proofs (see section 5.3). The source of the discomfort that mathematicians experience when confronted with computer proofs appears to be the following. A “good” mathematical proof should do more than to convince us that a certain statement is true. It should also explain *why* the statement in question holds. And this is done by referring to deep relations between deep mathematical concepts that often link different mathematical domains (Manders 1989)[^manders-1989]. Until now, computer proofs typically only employ fairly low level mathematical concepts. They are notoriously weak at developing deep concepts on their own, and have difficulties with linking concepts in from different mathematical fields. All this leads us to a philosophical question which is just now beginning to receive the attention that it deserves: what is mathematical understanding?

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=philosophy-mathematics). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/philosophy-mathematics/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=philosophy-mathematics&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/philosophy-mathematics/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- [Mathematics, Foundations of](https://www.rep.routledge.com/articles/overview/mathematics-foundations-of/v-1), by Detlefsen, M., Routledge Encyclopedia of Philosophy
- [Category Archives: Philosophy of Mathematics](http://www.iep.utm.edu/category/s-l-m/math/), *Internet Encyclopedia of Philosophy*
- [The Infinite](http://www.iep.utm.edu/infinite/), entry by Bradley Dowden, *Internet Encyclopedia of Philosophy*
- [FOM – Foundations Of Mathematics](https://mathweb.ucsd.edu/~sbuss/FOM/), e-mail discussion forum

## Related Entries

Aristotle, Special Topics: mathematics | Brouwer, Luitzen Egbertus Jan | choice, axiom of | Church-Turing Thesis | Frege, Gottlob: theorem and foundations for arithmetic | Gödel, Kurt | Hilbert, David: program in the foundations of mathematics | infinity | Kant, Immanuel: philosophy of mathematics | logic, history of: intuitionistic logic | logic: intuitionistic | mathematical: explanation | mathematics, philosophy of: fictionalism | mathematics, philosophy of: formalism | mathematics, philosophy of: indispensability arguments in the | mathematics, philosophy of: intuitionism | mathematics, philosophy of: nominalism | mathematics, philosophy of: Platonism | mathematics, philosophy of: structuralism | mathematics: constructive | model theory: first-order | plural quantification | Russell’s paradox | set theory | set theory: continuum hypothesis | set theory: independence and large cardinals | style: in mathematics | Turing, Alan | type theory | Whitehead, Alfred North | Wittgenstein, Ludwig: philosophy of mathematics

[^antonutti-2010]: Antonutti Marfori, M., 2010. ‘Informal Rigour and Mathematical Practice’, *Studia Logica*, 102: 567–576.

[^appel-1977]: Appel, K., Haken, W. & Koch, J., 1977. ‘Every Planar Map is Four Colorable’, *Illinois Journal of Mathematics*, 21: 429–567.

[^avigad-2021]: Avigad, J., 2021. ‘Reliability of Mathematical Inference’, *Synthese*, 198: 7377–7399.

[^azzouni-2004]: Azzouni, J., 2004. ‘The Derivation-Indicator View of Mathematical Practice’, *Philosophia Mathematica*, 12: 81-105.

[^balaguer-1998]: Balaguer, M., 1998. *Platonism and Anti-Platonism in Mathematics*, Oxford: Oxford University Press.

[^benacerraf-1965]: Benacerraf, P., 1965. ‘What Numbers Could Not Be’, in Benacerraf & Putnam 1983, pp. 272–294.

[^benacerraf-1967]: –––, 1967. ‘God, the Devil, and Gödel’, *The Monist*, 51: 9–32.

[^benacerraf-1973]: –––, 1973. ‘Mathematical Truth’, in Benacerraf & Putnam 1983, 403–420.

[^benacerraf-1983]: Benacerraf, P. & Putnam, H. (eds.), 1983. *Philosophy of Mathematics: Selected Readings*, Cambridge: Cambridge University Press, 2nd edition.

[^bernays-1935]: Bernays, P., 1935. ‘On Platonism in Mathematics’, in Benacerraf & Putnam 1983, pp. 258–271.

[^boolos-1971]: Boolos, G., 1971. ‘The Iterative Conception of Set’, in Boolos 1998, pp. 13–29.

[^boolos-1975]: –––, 1975. ‘On Second-Order Logic’, in Boolos 1998, pp. 37–53.

[^boolos-1985]: –––, 1985. ‘Nominalist Platonism’, in Boolos 1998, pp. 73–87.

[^boolos-1987]: –––, 1987. ‘The Consistency of Frege’s Foundations of Arithmetic’, in Boolos 1998, pp. 183–201.

[^boolos-1998]: –––, 1998. *Logic, Logic, and Logic*, Cambridge: Harvard University Press.

[^bueno-2011]: Bueno, O. , 2011. ‘Relativism in Set Theory and Mathematics’, in S. Hales (ed.), *A Companion to Relativism*, Oxford: Wiley-Blackwell, pp. 553–568.

[^burge-1998]: Burge, T., 1998. ‘Computer Proofs, A Priori Knowledge, and Other Minds’, *Noûs*, 32: 1–37.

[^burge-2013]: –––, 2013. *Cognition Through Understanding. Self-Knowledge, Interlocution, Reasoning, Reflection. Philosophical Essays, Volume 3*, Oxford: Oxford University Press.

[^burgess-2004]: Burgess, J., 2004. ‘Mathematics and Bleak House’, *Philosophia Mathematica*, 12: 37–53.

[^burgess-2004b]: –––, 2004b, ‘Quine, Analyticity and Philosophy of Mathematics’, *Philosophical Quarterly*, 54: 38–55.

[^burgess-2005]: –––, 2005, *Fixing Frege*, Princeton: Princeton University Press.

[^burgess-2015]: –––, 2015. *Rigor and Structure*, Oxford: Oxford University Press.

[^burgess-1997]: Burgess, J. & Rosen, G., 1997. *A Subject with No Object: Strategies for Nominalistic Interpretation of Mathematics*, Oxford: Clarendon Press.

[^button-2018]: Button, T. & Walsh, S., 2018. *Philosophy and Model Theory*, Oxford: Oxford University Press.

[^cantor-1932]: Cantor, G., 1932. *Abhandlungen mathematischen und philosophischen Inhalts*, E. Zermelo (ed.), Berlin: Julius Springer.

[^carnap-1950]: Carnap, R., 1950. ‘Empiricism, Semantics and Ontology’, in Benacerraf & Putnam 1983, pp. 241–257.

[^chihara-1973]: Chihara, C., 1973. *Ontology and the Vicious Circle Principle*, Ithaca: Cornell University Press.

[^cohen-1971]: Cohen, P., 1971. ‘Comments on the Foundations of Set Theory’, in D. Scott (ed.) *Axiomatic Set Theory* (Proceedings of Symposia in Pure Mathematics, Volume XIII, Part 1), American Mathematical Society, pp. 9–15.

[^colyvan-2001]: Colyvan, M., 2001. *The Indispensability of Mathematics*, Oxford: Oxford University Press.

[^curry-1958]: Curry, H., 1958. *Outlines of a Formalist Philosophy of Mathematics*, Amsterdam: North-Holland.

[^detlefsen-1986]: Detlefsen, M., 1986. *Hilbert’s Program*, Dordrecht: Reidel.

[^philosophy-mathematics-1992]: –– (ed), 1992. *Proof, logic and formalisation*, London: Routledge.

[^deutsch-2000]: Deutsch, D., Ekert, A. & Luppacchini, R., 2000. ‘Machines, Logic and Quantum Physics’, *Bulletin of Symbolic Logic*, 6: 265–283.

[^di-2021]: Di Toffoli, S., 2021. ‘Reconciling Rigor and Intuition’. *Erkenntnis*, 86: 1783–1802.

[^essenin-volpin-1961]: Essenin-Volpin, A., 1961. ‘Le Programme Ultra-intuitionniste des fondements des mathématiques’, in *Infinistic Methods*, New York: Pergamon Press, pp. 201-223.

[^feferman-1988]: Feferman, S., 1988. ‘Weyl Vindicated: Das Kontinuum seventy years later’, reprinted in S. Feferman, *In the Light of Logic*, New York: Oxford University Press, 1998, pp. 249–283.

[^feferman-2005]: –––, 2005. ‘Predicativity’, in S. Shapiro (ed.), *The Oxford Handbook of Philosophy of Mathematics and Logic*, Oxford: Oxford University Press, pp. 590–624.

[^field-1980]: Field, H., 1980. *Science without Numbers: a defense of nominalism*, Oxford: Blackwell.

[^field-1989]: –––, 1989. *Realism, Mathematics & Modality*, Oxford: Blackwell.

[^fine-2002]: Fine, K., 2002. *The Limits of Abstraction*, Oxford: Oxford University Press.

[^frege-1884]: Frege, G., 1884. *The Foundations of Arithmetic. A Logico-mathematical Enquiry into the Concept of Number*, J.L. Austin (trans.), Evanston: Northwestern University Press, 1980.

[^friend-2013]: Friend, M. 2013. ‘Pluralism and “Bad” Mathematical Theories: Challenging our Prejudices’, in K. Tanaka, et al. (eds.), *Paraconsistency: Logic and Application*, Dordrecht: Springer, pp. 277–307.

[^gentzen-1938]: Gentzen, G., 1938. ‘Die gegenwärtige Lage in der mathematischen Grundlagenforschung. Neue Fassung des Widerspruchsfreiheitsbeweises für die reine Zahlentheorie’, in *Forschungen zur Logik und zur Grundlegung der exakten Wissenschaften* (Neue Folge/Heft 4), Leipzig: Hirzel.

[^gödel-1931]: Gödel, K., 1931. ‘On Formally Undecidable Propositions in Principia Mathematica and Related Systems I’, in van Heijenoort 1967, pp. 596–616.

[^gödel-1944]: –––, 1944. ‘Russell’s Mathematical Logic’, in Benacerraf & Putnam 1983, pp. 447–469.

[^gödel-1947]: –––, 1947. ‘What is Cantor’s Continuum Problem?’, in Benacerraf & Putnam 1983, pp. 470–485.

[^goodman-1947]: Goodman, N. & Quine, W., 1947. ‘Steps Towards a Constructive Nominalism’, *Journal of Symbolic Logic*, 12: 97–122.

[^halbach-2005]: Halbach, V. & Horsten, L., 2005. ‘Computational Structuralism’, *Philosophia Mathematica*, 13: 174–186.

[^hale-2001]: Hale, B. & Wright, C., 2001. *The Reason’s Proper Study: Essays Towards a Neo-Fregean Philosophy of Mathematics*, Oxford: Oxford University Press.

[^hallett-1984]: Hallett, M., 1984. *Cantorian Set Theory and Limitation of Size*, Oxford: Clarendon Press.

[^hodes-1984]: Hodes, H., 1984. ‘Logicism and the Ontological Commitments of Arithmetic’, *Journal of Philosophy*, 3: 123–149.

[^hamkins-2015]: Hamkins, J., 2015. ‘Is the dream solution of the continuum hypothesis attainable?’, *Notre Dame Journal of Formal Logic*, 56: 135–145.

[^hellman-1989]: Hellman, G., 1989. *Mathematics without Numbers*, Oxford: Clarendon Press.

[^hilbert-1925]: Hilbert, D., 1925. ‘On the Infinite’, in Benacerraf & Putnam 1983, pp. 183–201.

[^hodes-1984-2]: Hodes, H., 1984. ‘Logicism and the Ontological Commitments of Arithmetic’, *Journal of Philosophy*, 3: 123–149.

[^horsten-2012]: Horsten, L., 2012. ‘Vom Zählen zu den Zahlen: on the relation between computation and mathematical structuralism’, *Philosophia Mathematica*, 20: 275–288.

[^horsten-2016]: Horsten, L. & Welch, P. (eds.), 2016. *Gödel’s disjunction: the scope and limits of mathematical knowledge*, Oxford: Oxford University Press.

[^isaacson-1987]: Isaacson, D., 1987. ‘Arithmetical Truth and Hidden Higher-Order Concepts’, in The Paris Logic Group (eds.), *Logic Colloquium ‘85*, Amsterdam: North-Holland, pp. 147–169.

[^kanamori-2009]: Kanamori, A., 2009. *The Higher Infinite. Large cardinals from their beginnings*, Berlin: Springer.

[^koellner-2009]: Koellner, P., 2009. ‘On Reflection Principles’, *Annals of Pure and Applied Logic*, 157: 206–219.

[^koellner-2009b]: –––, 2009b. ‘Truth in Mathematics: The Question of Pluralism’, in O. Bueno & Ø. Linnebo (eds.), *New Waves in Philosophy of Mathematics*, Basingstoke: Palgrave Macmillan, 80–116.

[^kreisel-1967]: Kreisel, G., 1967. ‘Informal Rigour and Completeness Proofs’, in I. Lakatos (ed.), *Problems in the Philosophy of Mathematics*, Amsterdam: North-Holland.

[^lakatos-1976]: Lakatos, I., 1976. *Proofs and Refutations*, New York: Cambridge University Press.

[^lavine-1994]: Lavine, S., 1994. *Understanding the Infinite*, Cambridge, MA: Harvard University Press.

[^leng-2010]: Leng, M., 2010. *Mathematics and Reality*, Oxford: Oxford University Press.

[^linnebo-2003]: Linnebo, Ø., 2003. ‘Plural Quantification Exposed’, *Noûs*, 37: 71–92.

[^linnebo-2013]: –––, 2013. ‘The Potential Hierarchy of Sets’, *Review of Symbolic Logic*, 6: 205–228.

[^linnebo-2017]: –––, 2017. *Philosophy of Mathematics*, Princeton: Princeton University Press.

[^linnebo-2018]: –––, 2018. *Thin Objects: an abstractionist account*, Oxford: Oxford University Press.

[^linsky-1995]: Linsky, B. & Zalta, E., 1995. ‘Naturalized Platonism vs. Platonized Naturalism’, *Journal of Philosophy*, 92: 525–555.

[^lucas-1961]: Lucas, J.R., 1961. ‘Minds, Machines, and Gödel’, *Philosophy*, 36: 112–127.

[^maddy-1988]: Maddy, P., 1988. ‘Believing the Axioms I, II’, *Journal of Symbolic Logic*, 53: 481–511, 736–764.

[^maddy-1990]: –––, 1990. *Realism in Mathematics*, Oxford: Clarendon Press.

[^maddy-1997]: –––, 1997. *Naturalism in Mathematics*, Oxford: Clarendon Press.

[^maddy-2007]: –––, 2007. *Second Philosophy: a Naturalistic Method*, Oxford: Oxford University Press.

[^mancosu-2008]: Mancosu, P., 2008. *The Philosophy of Mathematical Practice*, Oxford: Oxford University Press.

[^manders-1989]: Manders, K., 1989. ‘Domain Extensions and the Philosophy of Mathematics’, *Journal of Philosophy*, 86: 553–562.

[^martin-1998]: Martin, D.A., 1998. ‘Mathematical Evidence’, in H. Dales & G. Oliveri (eds.), *Truth in Mathematics*, Oxford: Clarendon Press, pp. 215–231.

[^martin-2001]: –––, 2001. ‘Multiple Universes of Sets and Indeterminate Truth Values’ *Topoi*, 20: 5–16.

[^mcgee-1997]: McGee, V., 1997. ‘How we Learn Mathematical Language’, *Philosophical Review*, 106: 35–68.

[^mclarty-2004]: McLarty, C., 2004. ‘Exploring Categorical Structuralism’, *Philosophia Mathematica*, 12: 37–53.

[^moore-2001]: Moore, A., 2001. *The Infinite*, second edition, New York: Routledge.

[^moore-1982]: Moore, G., 1982. *Zermelo’s Axiom of Choice: Its Origins, Development, and Influence*, New York: Springer Verlag.

[^mormann-2002]: Mormann, T., 2002. ‘Towards an evolutionary account of conceptual change in mathematics’, in G. Kampis et al (eds.), *Appraising Lakatos: Mathematics, Methodology and the Man*, Dordrecht: Kluwer, pp. 139–156.

[^myhill-1960]: Myhill, J., 1960. ‘Some Remarks on the Notion of Proof’, *Journal of Philosophy*, 57: 461–471.

[^niebergall-2000]: Niebergall, K., 2000. ‘On the Logic of Reducibility: axioms and examples’, *Erkenntnis*, 53: 27–62.

[^parsons-1980]: Parsons, C., 1980. ‘Mathematical Intuition’, *Proceedings of the Aristotelian Society*, 80: 145–168.

[^parsons-1983]: –––, 1983. *Mathematics in Philosophy: Selected Essays*, Ithaca: Cornell University Press.

[^parsons-1990a]: –––, 1990a. ‘The Structuralist View of Mathematical Objects’, *Synthese*, 84: 303–346.

[^parsons-1990b]: –––, 1990b. ‘The Uniqueness of the Natural Numbers’, *Iyyun* 13: 13–44.

[^parsons-2008]: –––, 2008. *Mathematical Thought and Its Objects*, Cambridge: Cambridge University Press.

[^penrose-1989]: Penrose, R., 1989. *The Emperor’s New Mind.* Oxford: Oxford University Press.

[^penrose-1994]: –––, 1994. *Shadows of the Mind.* Oxford: Oxford University Press.

[^pettigrew-2008]: Pettigrew, R., 2008. ‘Platonism and Aristotelianism in Mathematics’, Philosophia Mathematica 16: 310–332.

[^potter-2004]: Potter, M., 2004. *Set Theory and Its Philosophy: a Critical Introduction*, Oxford: Oxford University Press.

[^pour-el-1999]: Pour-El, M., 1999. ‘The Structure of Computability in Analysis and Physical Theory’, in E. Griffor (ed.), *Handbook of Computability Theory*, Amsterdam: Elsevier, pp. 449–471.

[^putnam-1967]: Putnam, H., 1967. ‘Mathematics without Foundations’, in Benacerraf & Putnam 1983, 295–311.

[^putnam-1972]: –––, 1972. *Philosophy of Logic*, London: George Allen & Unwin.

[^quine-1969]: Quine, W.V.O., 1969. ‘Epistemology Naturalized’, in W.V.O. Quine, *Ontological Relativity and Other Essays*, New York: Columbia University Press, pp. 69–90.

[^quine-1970]: –––, 1970. *Philosophy of Logic*, Cambridge, MA: Harvard University Press, 2nd edition.

[^rav-1999]: Rav, Y., 1999. ‘Why do we prove theorems?’, *Philosophia Mathematica*, 9: 5–41.

[^reck-2000]: Reck, E. & Price, M., 2000. ‘Structures and Structuralism in Contemporary Philosophy of Mathematics’, *Synthese*, 125: 341–383.

[^resnik-1974]: Resnik, M., 1974. ‘The Frege-Hilbert Controversy’, *Philosophy and Phenomenological Research*, 34: 386–403.

[^resnik-1997]: –––, 1997. *Mathematics as a Science of Patterns*, Oxford: Clarendon Press.

[^russell-1902]: Russell, B., 1902. ‘Letter to Frege’, in van Heijenoort 1967, 124–125.

[^shapiro-1983]: Shapiro, S., 1983. ‘Conservativeness and Incompleteness’, *Journal of Philosophy*, 80: 521–531.

[^shapiro-1991]: –––, 1991. *Foundations without Foundationalism: A Case for Second-order Logic*, Oxford: Clarendon Press.

[^shapiro-1997]: –––, 1997. *Philosophy of Mathematics: Structure and Ontology*, Oxford: Oxford University Press.

[^shapiro-2000]: –––, 2000. *Thinking about Mathematics*, Oxford: Oxford University Press.

[^sieg-1994]: Sieg, W., 1994. ‘Mechanical Procedures and Mathematical Experience’, in A. George (ed.), *Mathematics and Mind*, Oxford: Oxford University Press.

[^studd-2019]: Studd, J., 2019. Everything, more or less. A defence of generality relativism. Oxford: Oxford University Press.

[^tait-1981]: Tait, W., 1981. ‘Finitism’, reprinted in Tait 2005, pp. 21–42.

[^tait-2005]: –––, 2005. *The Provenance of Pure Reason: Essays in the Philosophy of Mathematics and its History*, Oxford: Oxford University Press.

[^tatton-brown-2020]: Tatton-Brown, O., forthcoming. ‘Rigour and Proof’, *Review of Symbolic Logic*, first online 21 October 2020. doi:10.1017/S1755020320000398

[^troelstra-1988]: Troelstra, A. & van Dalen, D., 1988. *Constructivism in Mathematics: An Introduction* (Volumes I and II), Amsterdam: North-Holland.

[^turing-1936]: Turing, A., 1936. ‘On Computable Numbers, with an Application to the Entscheidungsproblem’, reprinted in M. Davis (ed.), *The Undecidable: Basic Papers on Undecidable Propositions and Uncomputable Functions*, Hewlett: Raven Press, 1965, pp. 116–151.

[^tymoczko-1979]: Tymoczko, T., 1979. ‘The Four-Color Problem and its Philosophical Significance’, *Journal of Philosophy*, 76: 57–83.

[^atten-2004]: van Atten, M., 2004. *On Brouwer*, London: Wadsworth.

[^heijenoort-1967]: van Heijenoort, J., 1967. *From Frege to Gödel: A Source Book in Mathematical Logic (1879–1931)*, Cambridge, MA: Harvard University Press.

[^warren-2015]: Warren, J., 2015. ‘Conventionalism, Consistency, and Consistency Sentences’, *Synthese*, 192: 1351–1371.

[^weir-2003]: Weir, A., 2003. ‘Neo-Fregeanism: An Embarrassment of Riches’, *Notre Dame Journal of Formal Logic*, 44: 13–48.

[^welch-2016]: Welch, P. & Horsten, L. 2016. ‘Reflecting on Absolute Infinity.’, *Journal of Philosophy*, 113: 89–111.

[^weyl-1918]: Weyl, H., 1918. *The Continuum: A Critical Examination of the Foundation of Analysis*, S. Pollard and T. Bole (trans.), Mineola: Dover, 1994.

[^woodin-2001a]: Woodin, H., 2001a. ‘The Continuum Hypothesis. Part I’, *Notices of the American Mathematical Society*, 48: 567–578.

[^woodin-2001b]: –––, 2001b. ‘The Continuum Hypothesis. Part II’, *Notices of the American Mathematical Society*, 48: 681–690.

[^woodin-2011]: –––, 2011. ‘The Realm of the Infinite’, in H. Woodin & M. Heller (eds.), *Infinity: New Research Frontiers*, New York: Cambridge University Press, pp. 89–118.

[^wright-1983]: Wright, C., 1983. *Frege’s Conception of Numbers as Objects* (Scots Philosophical Monographs, Volume 2), Aberdeen: Aberdeen University Press.

[^yablo-2014]: Yablo, S. 2014. *Aboutness* Princeton: Princeton University Press.

[^zach-2006]: Zach, R., 2006. ‘Hilbert’s Program Then and Now’, in D. Jacquette (ed.), *Philosophy of Logic* (Handbook of the Philosophy of Science, Volume 5), Amsterdam: Elsevier, pp. 411–447.

[^zermelo-1930]: Zermelo, E., 1930. ‘On Boundard Numbers and Domains of Sets’, translated by M. Hallett, in W. Ewald (ed.), *From Kant to Hilbert: A Source Book in Mathematics* (Volume 2), Oxford: Oxford University Press, 1996, pp. 1208–1233.
