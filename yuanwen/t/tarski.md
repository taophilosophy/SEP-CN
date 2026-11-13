# Alfred Tarski
**First published Mon Oct 30, 2006; substantive revision Sat Jan 28, 2023**

*Gómez-Torrente, Mario*

Alfred Tarski (1901–1983) described himself as “a mathematician (as well as a logician, and perhaps a philosopher of a sort)” (1944, p. 369). He is widely considered as one of the greatest logicians of the twentieth century (often regarded as second only to Gödel), and thus as one of the greatest logicians of all time. Among philosophers he is especially known for his mathematical characterizations of the concepts of truth and logical consequence for sentences of classical formalized languages, and to a lesser extent for his mathematical characterization of the concept of a logical constant for expressions of those same languages. Among logicians and mathematicians he is in addition famous for his work on set theory, model theory and algebra, which includes results and developments such as the Banach-Tarski paradox, the theorem on the indefinability of truth (see section 2 below), the completeness and decidability of elementary algebra and geometry, and the notions of cardinal, ordinal, relation and cylindric algebras. After a biographical sketch, this entry offers a condensed exposition of the parts of Tarski’s work that are most relevant to philosophy, his theories of truth, logical consequence and logical constants. In this exposition we have attempted to remain as close as possible to Tarski’s original presentations, reducing to a minimum the number of claims that might be controversial philosophically or exegetically. The final section on further reading refers the reader to other entries and works on critical and exegetical aspects of Tarski’s work not touched upon in this entry.

## 1. Biographical sketch

Tarski was born on January 14, 1901 in Warsaw, then a part of the Russian Empire. His family name at birth was Tajtelbaum, changed to Tarski in 1923. He studied mathematics and philosophy at the University of Warsaw from 1918 to 1924, taking courses with Kotarbiński, Leśniewski, Łukasiewicz, Mazurkiewicz and Sierpiński among others. (See Lvov-Warsaw School.) He got a doctoral degree, under Leśniewski’s supervision, in 1924. From then until 1939 he taught mathematics at a high school and held minor teaching positions at the University of Warsaw. In this period he published prolifically on logic and set theory, building a strong international reputation for himself. Yet he failed in his attempt to obtain a professorship at the University of Lvov (now Lviv) in 1939. In 1929 he married Maria Witkowska, with whom he soon had two children, Ina and Jan.

In August 1939 Tarski traveled to the United States to attend a congress of the Unity of Science movement (see Vienna Circle). World War II broke out soon after that, leaving Tarski no option but to stay in the States. He spent the war years separated from his family, forced to remain in Poland. In this period he held several temporary university positions, at Harvard University, the City College of New York, the Institute for Advanced Study at Princeton, and the University of California at Berkeley, where he was eventually given tenure in 1945 and a professorship in mathematics in 1948. Maria, Ina and Jan were able to join him in Berkeley in 1946.

In Berkeley Tarski built a prominent school of research in logic and the foundations of mathematics and science, centered around the prestigious graduate program in logic and methodology of science, which he was also instrumental in creating. He received many academic honors, such as the membership in the National Academy of Sciences of the USA and the election as Corresponding Fellow of the British Academy. Tarski remained affiliated to Berkeley until his death, on October 27, 1983.

## 2. Truth

In a logic seminar he gave at the University of Warsaw between 1927 and 1929, Tarski proved several results that made reference to notions that later would be called “semantical”, in particular results about the notions of definability and of truth in a structure (see Vaught 1974 and 1986)[^vaught-1974][^vaught-1986]. Vaught informs us that Tarski found certain difficulties when trying to give a mathematically satisfactory form to the results presented in the seminar, and that this led him to look for a precise theory of the semantical notions (cf. Vaught 1974, pp. 160ff. and 1986, pp. 870ff.)[^vaught-1974][^vaught-1986]. Such a theory did not exist at the time. In particular, there were no definitions of these notions in terms of concepts accepted in the foundational systems designed for the reconstruction of classical mathematics (for example, Russell and Whitehead’s theory of types or Zermelo’s set theory). Because of this, the existing results in which these notions appeared could not be reconstructed in the accepted foundational systems. And there was no rigorous axiomatic theory of the semantical notions in which these were taken as primitive, either.

In spite of this, the results about semantical notions were important and even moderately abundant by 1930. Among these Tarski himself would mention Gödel’s completeness theorem and several versions of the Löwenheim-Skolem theorem (cf. Tarski 1983b, pp. 240–1, sp. p. 240 n.1, and p. 241 n. 2)[^tarski-1983b]. All these results use the notion of truth in a structure, or functionally equivalent notions. And Tarski says that

> it is evident that all these results only receive a clear content and can only then be exactly proved, if a concrete and precisely formulated definition of [true] sentence is accepted as a basis for the investigation (Tarski 1983b, p. 241)[^tarski-1983b].

Tarski’s aim in a series of works on semantical notions was precisely to propose mathematically acceptable definitions of those notions, and in particular acceptable in some one of the chief foundational systems (the system chosen by Tarski will change with time; see below). With appropriate definitions of those notions, the theorems about them would be susceptible of being reformulated making use of the defined notions, and the uneasiness described by Tarski in the text just quoted would be alleviated. The alternative of taking the semantical notions as primitive is also considered by Tarski in several places, but he clearly prefers to avoid it if possible. The reason is that in the axiomatic alternative there is no negligible risk that there remain ways of generating the semantical antinomies for the semantical primitives of the system (cf. Tarski 1983b, p. 255)[^tarski-1983b]. With the definitional procedure, however, the consistency of the definition would depend exclusively on the consistency of the theory in which it is formulated, and this will be a theory we have reasons to think is consistent.

The first work containing a mathematical definition of one of the semantical notions is Tarski (1931) (English version, Tarski 1983d)[^tarski-1983d], where Tarski examines a language *L* in which it is possible to formalize the arithmetic of the real numbers, and gives a recursive definition of the notion “set of real numbers definable in *L*” (cf. Def. 9 in Tarski 1983d, p. 128)[^tarski-1983d]. The definition depends on others that are a bit cumbersome; today we would define a similar notion in a simpler way with the help of the definition of truth that Tarski himself would publish two years later. But the essence of the Tarskian definition of truth is already here. In the 1931 paper we find also, as was to be expected, the Tarskian concern with matters of precision and foundational rigor, and a revealing statement about the attitude of mathematicians toward the notion of definability, that could be extended to other semantical notions:

> The distrust of mathematicians towards the notion in question is reinforced by the current opinion that this notion is outside the proper limits of mathematics altogether. The problems of making its meaning more precise, of removing the confusions and misunderstandings connected with it, and of establishing its fundamental properties belong to another branch of science—metamathematics (Tarski 1983d, p. 110)[^tarski-1983d].

In his classic monograph on the concept of truth “The Concept of Truth in Formalized Languages” (Polish original version, Tarski 1933; German translation with an added postscript, Tarski 1935; English version of the German text, Tarski 1983b)[^tarski-1933][^tarski-1935][^tarski-1983b][^tarski-1935-2], Tarski will present a method for constructing definitions of truth for classical quantificational formal languages. When one succeeds in applying this method to a particular formal language, the end result will be the construction of a predicate in a metalanguage for that language whose essential properties will be that it will be constructed out of non-suspicious mathematical vocabulary and that it will be intuitively satisfied precisely by the intuitively true sentences of the object language. At the same time, Tarski shows how, in terms of the defined notion of truth, one can give intuitively adequate definitions of the semantical notions of definability and denotation, and he indicates how it is possible to define the notion of truth in a structure in a way analogous to the one used to define truth.[^note-1] That allows him to conclude that the acceptability and rigor of the “recent methodological studies” (of Löwenheim, Skolem, Gödel and Tarski himself, among others), have been vindicated (cf. Tarski 1983b, p. 266)[^tarski-1983b].

Languages, both object languages and metalanguages, are in the monograph not just interpreted grammars; a language also includes a deductive system. A Tarskian metalanguage always includes its object language as a part, both its grammar (perhaps under some translation) and its deductive system. And besides, it will always contain a few more things if these things are not already in the object language. Specifically, it will always contain a sub-language and sub-theory that can be used to say a great deal of things about the syntax of the object language; and it will always contain all the mathematics (both concepts and methods of proof) that “may be taken from any sufficiently developed system of mathematical logic” (Tarski 1983b, p. 211)[^tarski-1983b].

Tarski doesn’t give a general formulation of his method. Such a general formulation would not be too illuminating. Instead he helpfully chooses to illustrate his method as it would work for a few languages. The most basic example he uses, to which about half of his monograph is devoted, is what he calls “the language of the calculus of classes” (LCC). Here is a quick description in more current notation (Tarski uses Łukasiewicz’s Polish notation):

1. primitive signs of LCC: ∀, ∨, ¬, (, ), I (a binary predicate), *x*, _{′} (a subindex accent to generate variables by suffixing to “*x*”; let’s use the notation *x*_{*n*} for the *x* followed by *n* accents).
2. grammar of LCC: Atomic formulae are of the form I*x*_{*k*}*x*_{*l*}. Complex formulae are obtained by negation, disjunction and universal quantification.
3. interpretation of LCC: The range of the variables is the class of all subclasses of individuals (of the universe). I stands for the relation of inclusion among these subclasses. The other signs mean what you would expect.

Besides all this, Tarski gives a deductive system for LCC, as required of every language.

Tarski’s most basic idea about how to construct a truth predicate, a predicate which will be intuitively satisfied exactly by the intuitively true sentences of LCC, is that such a predicate should verify what he calls “convention **T**”. This convention imposes a condition on defined truth predicates ((a) in the example immediately below) that Tarski often talks about as grasping the intuitions behind the “classical Aristotelian conception of truth” (cf. Tarski 1983b, p. 155; 1944, pp. 342–3)[^tarski-1983b]. Convention **T** is here spelled out for the case of LCC:

**Convention T.** A formally correct definition of the symbol “Tr”, formulated in the metalanguage, will be called an *adequate definition of truth* if the deductive system of the metatheory proves the following:

1. all sentences which are obtained from the expression “Tr(*x*) if and only if *p*” by substituting for the symbol “*x*” a structural-descriptive name of any sentence of the language in question and for the symbol “*p*” the expression which forms the translation of this sentence into the metalanguage;
2. the sentence “for any *x*, if Tr(*x*) then *x* is a sentence of LCC” (cf. Tarski 1983b, pp. 187–8)[^tarski-1983b].

That a definition is “formally correct” means, roughly, that it will be constructed out of non-suspicious vocabulary following non-controversial rules for defining new expressions. But why should one think that a predicate verifying convention **T** should be, besides, coextensional with the intuitive predicate of truth for LCC? The reason can be given by an intuitive argument relating both predicates, such as the following (cf. Tarski 1944, pp. 353–4)[^tarski-1944]:

(⇒) Suppose that “*p*” is a sentence of LCC such that Tr(“*p*”). By assumption, “Tr(”*p*“) if and only if *p*” is provable in the metalanguage. So Tr(“*p*”) if and only if *p* (the metalanguage must only prove truths). So *p*. So “*p*” is true.

(⇐) Suppose that “*p*” is true. Then *p*. And then, as before, Tr(“*p*”).

Tarski defines truth in terms of the notion of the satisfaction of a formula of LCC by an infinite sequence of assignments (of appropriate objects: subclasses of the universe of individuals in the case of LCC). He gives first a recursive definition and immediately indicates how to transform it into a normal or explicit definition. The recursive definition is this: an infinite sequence of classes *f* satisfies formula *F* if and only if *f* and *F* are such that

1. there are natural numbers *k* and *l* such that *F* = I*x*_{*k*}*x*_{*l*} and *f*(*k*)⊆*f*(*l*); or
2. there is a formula *G* such that *F*=¬*G* and *f* does not satisfy *G*; or
3. there are formulae *G* and *H* such that *F*=(*G*∨*H*) and *f* satisfies *G* or *f* satisfies *H*; or finally,
4. there is a natural number *k* and a formula *G* such that *F*=∀*x*_{*k*}*G* and every infinite sequence of subclasses that differs from *f* at most in the *k*th place satisfies *G* (cf. Tarski 1983b, p. 193)[^tarski-1983b].

The normal definition is this:

An infinite sequence of subclasses *f* satisfies a formula *F* if and only if *f* and *F* stand in every relation *R* among sequences and formulae such that, for any *g* and *G*, *g* and *G* stand in *R* if and only if *g* is an infinite sequence of subclasses, *F* is a formula and either

1. there are natural numbers *k* and *l* such that *G* = I*x*_{*k*}*x*_{*l*} and *g*(*k*)⊆*g*(*l*); or
2. there is a formula *H* such that *G* is ¬*H* and *g* and *H* don’t stand in *R*; or
3. there are formulae *H* and *I* such that *G* is (*H*∨*I*) and *g* and *H* stand in *R* or *g* and *I* stand in *R*; or
4. there is a natural number *k* and a formula *H* such that *G* is ∀*x*_{*k*}*H* and, for every infinite sequence of subclasses *h* that differs from *g* at most in the *k*th place, *h* and *H* stand in *R* (cf. Tarski 1983b, p. 193, n. 1)[^tarski-1983b].

Tarski then defines the truth predicate as follows:

> For all *x*, Tr(*x*) if and only if *x* is a sentence of LCC and every infinite sequence of subclasses satisfies *x* (cf. Tarski 1983b, p. 195)[^tarski-1983b].

Given the way the definition has been constructed, it is intuitively clear that the metalanguage will prove all biconditionals of the convention **T** for LCC. Tarski does not prove this cumbersome fact in a metametalanguage, and he helpfully contents himself with showing how a few of the biconditionals would be established in the metalanguage.

The usual reasonings leading to the semantical antinomies cannot be reproduced for the Tarskian defined semantical concepts. In particular, the antinomy of the liar cannot be reproduced using the defined predicate Tr. Consider the version of the antinomy offered by Tarski (due to Łukasiewicz). Abbreviate the expression “the first underlined sentence of this entry” with the letter “*c*”. Now consider the sentence:

*c* is not a true sentence.

Given what “*c*” abbreviates, we get

(a) “*c* is not a true sentence” = *c*

And the following is intuitively true:

(b) “*c* is not a true sentence” is a true sentence if and only if *c* is not a true sentence.

From (a) and (b) follows the contradiction

*c* is a true sentence if and only if *c* is not a true sentence.

The reason why this cannot be reproduced for Tr is that this predicate is always a predicate of a language (the metalanguage) different from the language of the sentences to which it applies (the object language). It is not possible to form a sentence of the language for which one defines Tr that says of itself that it is (not) Tr, since Tr is not a predicate of that language. On the other hand, it is certainly possible in some cases to form a sentence *S* of the metalanguage that says of itself that it is not Tr, but since *S* is a sentence of the metalanguage it is simply true and (presumably) not paradoxical, since there is no reason why a biconditional like (b) should hold for it; biconditionals of this kind hold only for sentences of the language for which Tr has been defined, not for sentences of the metalanguage.

LCC has the property of being what Tarski calls a “language of finite order”. The idea of order is familiar. Variables for individuals (non-existent in LCC) are of order 1. Variables for classes of individuals (all the variables of LCC) are of order 2. Variables for classes of classes of individuals are of order 3, and so on. The order of a language of this series is the greatest positive integer *n* with variables of order *n*. (Thus, although LCC looks grammatically just like a first-order language, semantically it can be seen as a fragment of what under present conventions would be called a second-order language.)

But there are also languages of infinite order. In these the order of the available variables is not bounded above. Tarski gives an example, which he calls “the language of the general theory of classes” (LGTC). Here again is a quick description in more current notation:

1. primitive signs of LGTC: ∀, ∨, ¬, (, ), X, _{′}, ′ (The last two are a subindex accent and a superindex accent to generate variables by suffixing to “*X*”; let’s use the notation *X*_{*n*}^{*m*} for the *X* followed by *n* subindex accents and *m* superindex accents. The superindex must be positive.)
2. grammar of LGTC: Atomic formulae are of the form *X*_{*n*}^{*m*+1}*X*_{*p*}^{*m*}. Complex formulae are obtained by negation, disjunction and universal quantification with respect to the variables of all orders.
3. interpretation of LGTC: A variable of the form *X*_{*n*}¹ takes as values individuals, a variable of the form *X*_{*n*}² takes as values classes of individuals, a variable of the form *X*_{*n*}³ takes as values classes of classes of individuals, etc. *X*_{*n*}^{*m*+1}*X*_{*p*}^{*m*} “means” that the object assigned to *X*_{*n*}^{*m*+1} “contains” the object assigned to *X*_{*p*}^{*m*}. The other signs mean what you would expect.

Besides all this, Tarski gives a deductive system for LGTC, as required of every language. Suffice it to say that it is a version of a typical simple theory of finite types, with axioms and rules for the connectives and quantifiers, axioms of comprehension and extensionality for all orders, and an axiom of infinity. Tarski observes that LGTC suffices, with the help of some tricks, to develop all the mathematics that can be developed in the simple theory of finite types, even though it has formally fewer types of variables.

In the 1933 original Polish version of his monograph Tarski says that his method for constructing truth predicates cannot be applied to the construction of a truth predicate for LGTC. The problem is that in 1933 Tarski adopts as the mathematical apparatus of his metalanguages the simple theory of finite types, or equivalently, LGTC. In this language, supplemented (and even unsupplemented) by a theory of syntax for LCC, Tarski has everything he needs to give his definition of satisfaction for LCC. In particular, the relation of satisfaction for LCC is a relation that can be found in the hierarchy of finite types. (Full set theory is not needed.) And the form in which Tarski defines it quantifies only over sequences of classes and over relations among sequences of classes and formulae (as we may check above), and these are objects quantifiable over in finite type theory.

But the construction of a Tarskian truth predicate for LGTC could not be carried out in finite type theory. The relation of satisfaction for LGTC is intuitively a relation among formulae and sequences of: sequences of individuals, sequences of classes of individuals, sequences of classes of classes of individuals, etc. And this relation is not a relation in the hierarchy of finite types. Much less can one quantify in finite type theory over the objects necessary to apply the Tarskian method. One cannot quantify over sequences of: sequences of individuals, sequences of classes of individuals, sequences of classes of classes of individuals, etc.; and one cannot quantify over relations among formulae and sequences of: sequences of individuals, sequences of classes of individuals, sequences of classes of classes of individuals, etc.

It is this situation that leads Tarski to wonder

> whether our failure is accidental and in some way connected with defects in the methods actually used, or whether obstacles of a fundamental kind play a part which are connected with the nature of the concepts we wish to define, or of those with the help of which we have tried to construct the required definitions (Tarski 1983b, p. 246)[^tarski-1983b].

There is a problem even in formulating the question precisely, for, as Tarski notes,

> if the second supposition [of the preceding quotation] is the correct one all efforts intended to improve the methods of construction would clearly be fruitless (Tarski 1983b, p. 246)[^tarski-1983b].

But

> it will be remembered that in the convention **T** of §3 the conditions which decide the material correctness of any definition of true sentence are exactly stipulated. The construction of a definition which satisfies these conditions forms in fact the principal object of our investigation. From this standpoint the problem we are now considering takes on a precise form: it is a question of *whether on the basis of the metatheory of the language we are considering the construction of a correct definition of truth in the sense of convention* **T** *is in principle possible*. As we shall see, the problem in this form can be definitively solved, but in a *negative sense* (Tarski 1983b, p. 246)[^tarski-1983b].

The negative answer is provided by a version of Tarski’s theorem of the indefinability of truth. The weakest Tarskian metalanguage for LGTC will consist in expanding LGTC by means of concepts and a theory of the syntax of LGTC. But the mathematical part of the metalanguage will be the same, for that’s the “sufficiently developed system of mathematical logic” of which Tarski spoke. Further, the metalanguage will obviously contain its object language as part, both its grammar (under no translation) and its deductive system, because LGTC will appear both in the object language and in the metalanguage (cf. Tarski 1983b, p. 247)[^tarski-1983b].

In a word, the metalanguage, which we may call “LGTC+”, is LGTC plus a theory of the syntax of LGTC. The question that Tarski poses is, then, whether there is a predicate constructible in LGTC+ which verifies the convention **T** for sentences of LGTC. Tarski solves it negatively by proving the following theorem:

**Theorem I.** (a) In whatever way the symbol “Tr”, denoting a class of expressions, is defined in LGTC+, it will be possible to derive from it the negation of one of the sentences which were described in the condition (a) of the convention **T**;

(b) assuming that the class of all provable sentences of the metatheory is consistent, it is impossible to construct an adequate definition of truth in the sense of convention **T** on the basis of LGTC+ (cf. Tarski 1983b, p. 247)[^tarski-1983b].

Part (b) of Theorem I is a trivial consequence of part (a), since it is the mark of a consistent system that it doesn’t contain a sentence and its negation. The proof of part (a) is an application of Gödel’s technique of diagonalization. The following are the basic steps described using the anachronistic recourse to a more familiar case and to a modern, streamlined notation.

View LGTC as if it were a standard language L for first-order arithmetic. Suppose we extend it with a theory for talking about the syntax of L (this would not be a Tarskian metalanguage, since it would not include a “sufficiently developed system of mathematical logic”, but all this is just for purposes of illustration). Call the extension L+. Then L+ can be “interpreted” in L using Gödelian techniques, by which Tarski means, roughly, that one can translate L+ into L arithmetizing it in such a way that the translations of theorems of L+ will be theorems of L. Now suppose that φ(*n*) is the *n*th expression of L (and that this function is definable in L+), that *d*(*x*) is a diagonal function for expressions of L (which is definable in L+; here I have in mind one involving substitution of numerals for free variables), and let **n** be the numeral of *n*. Then for every predicate *E*(*x*) of expressions of L defined in L+ one can prove in L+ a general sentence of the form ∀*n*[¬*E*(*d*(φ(*n*)))↔ψ(*n*)], where ψ(*n*) is a formula with one free variable entirely constructed in L (through the arithmetization of the L+ predicate “¬*E*(*d*(φ(*n*)))”). Then one can also prove the sentence ¬*E*(*d*(φ(**k**)))↔ψ(**k**), where *k* is the Gödel number of ψ(*n*). *d*(φ(**k**)) is the sentence ψ(**k**), so ψ(**k**) is a “fixed point” of the predicate ¬*E*(x): it “says of itself” that it has the property expressed by ¬*E*(x). The sentence ¬E(*d*(φ(**k**)))↔ψ(**k**) is already equivalent to the sentence ¬[*E*(*d*(φ(**k**)))↔ψ(**k**)], and part (a) of Theorem I is proved.

In the postscript to the 1935 German translation of the monograph on truth, Tarski abandons the 1933 requirement that the apparatus of the metatheory be formalizable in finite type theory, and accepts the use of a more powerful theory of transfinite types, where the transfinite objects are classes of the objects of lower types, or the use of set theory. Tarski notes that the relation of satisfaction and a truth predicate for LGTC (and LGTC+) are definable in these more powerful metatheories (cf. Tarski 1983b, pp. 271–2)[^tarski-1983b]. But he also says that the proof of the indefinability theorem can be adapted to show that, in general, one cannot define a truth predicate “if the order of the metalanguage is at most equal to that of the language itself” (Tarski 1983b, p. 273)[^tarski-1983b].

## 3. Logical consequence

Tarski presents his theory of logical consequence in Tarski (1936a) (German version, Tarski 1936b; English translation of the Polish, Tarski 2002; English translation of the German, Tarski 1983c)[^tarski-1936b][^tarski-1983c][^tarski-2002]. This classic paper begins with some general remarks on the possibility of a precise definition of the concept of consequence. The essence of these remarks is that since the common concept is vague, it seems certainly difficult, and perhaps impossible, to reconcile all features of its use in the definition of a corresponding precise concept. Nevertheless, Tarski says, logicians had thought until recently that they had managed to define a precise concept that coincided exactly in extension with the intuitive concept of consequence. Tarski mentions the extraordinary development of mathematical logic in recent decades, which had shown “how to present mathematical disciplines in the shape of formalized deductive theories” (Tarski 1983c, p. 409)[^tarski-1983c]. In these theories, consequences are extracted from axioms and theorems by rules of inference, “such as the rules of substitution and detachment” (Tarski 1983c, p. 410)[^tarski-1983c], of a purely syntactical (or “structural”, in Tarski’s word) nature. “Whenever a sentence follows from others, it can be obtained from them—so it was thought—by means of the transformations prescribed by the rules” (Tarski 1983c, p. 410)[^tarski-1983c]. According to Tarski, this belief of the logicians was justified by “the fact that they had actually succeeded in reproducing in the shape of formalized proofs all the exact reasonings which had ever been carried out in mathematics” (Tarski 1983c, p. 410)[^tarski-1983c].

But Tarski goes on to claim that that belief of the logicians was wrong. There are some non-vague cases in which a certain sentence of a higher-order language follows in the intuitive sense from a set of other sentences of that language but cannot be derived from them using the accepted axioms and rules. These cases are provided by some ω-incomplete theories, theories in which for some predicate *P* the sentences

*A*₀. 0 possesses the given property *P*,

*A*₁. 1 possesses the given property *P*,

and, in general, all sentences of the form *A*_{*n*} can be proved, but the universal sentence

*A*. Every natural number possesses the given property *P*,

cannot be proved on the basis of the accepted axioms and rules of inference. (LGTC provides an example of such a theory.) “Yet intuitively it seems certain that the universal sentence *A* follows in the usual sense from the totality of particular sentences *A*₀, *A*₁, …, *A*_{*n*}, …. Provided all these sentences are true, the sentence *A* must also be true” (Tarski 1983c, p. 411)[^tarski-1983c].

Tarski considers the possibility of adding an ω-rule to the accepted rules of inference, that is, a rule which allows us to deduce a universal sentence of the form of *A* from the set of sentences *A*₀, *A*₁, etc. However, he says that such a rule would differ in very essential respects from the old rules: it is not a finitary rule, while all the accepted rules in common deductive systems are finitary. Also, Tarski immediately takes importance away from the further suggestion of supplementing the old system of rules by means of a formalized finitary ω-rule. He points out that in view of Gödel’s incompleteness results, no matter how many new finitary rules or axioms we add to certain higher-order theories, they will still remain incomplete theories, in fact ω-incomplete theories. This discussion is enough to show that “in order to obtain the proper concept of consequence, which is close in essentials to the common concept, we must resort to quite different methods and apply quite different conceptual apparatus in defining it” (Tarski 1983c, p. 413)[^tarski-1983c]. The different methods and the different conceptual apparatus that Tarski has in mind are going to be “the methods which have been developed in recent years for the establishment of scientific semantics, and the concepts defined with their aid” (Tarski 1983c, p. 414; a footnote refers us to Tarski’s monograph on truth)[^tarski-1983c].

The best way of appreciating the nature of Tarski’s theory of logical consequence and how it constitutes an application of the methods of Tarskian semantics is to see how it applies to a particular formal language of a simple structure, of a kind that Tarski seems to have primarily in mind in his paper of 1936. We will choose a simple language of this kind for a fragment of elementary arithmetic. This language, LAr, can be given this quick description:

1. primitive signs of LAr: ∀, →, ¬, (, ), x, _{′} (a subindex accent to generate variables by suffixing to “*x*”; let’s use again the notation *x*_{*n*} for the *x* followed by *n* accents), 0 (an individual constant), N (a monadic predicate), M (a dyadic predicate).
2. grammar of LAr: Atomic formulae are of the forms N*t*₁ and M*t*₁*t*₂, where *t*₁ and *t*₂ are either variables or the constant 0. Complex formulae are obtained by negation, conditionalization and universal quantification relativized to “N”.
3. interpretation of LAr: The range of the variables is the set of all natural numbers. N stands for the set of natural numbers and M for the relation of being less than among natural numbers. The other signs mean what you would expect.

In the 1936 paper Tarski seems to be thinking paradigmatically of languages in which (as in LAr) there is a predicate (“N” in the case of LAr) that applies exactly to the individuals in the domain of the intended interpretation of the language. He says elsewhere that the variables of such a language range exclusively over the individuals of that set (cf. Tarski 1937, p. 84)[^tarski-1937]. (This is not to say that Tarski adopts these conventions with all the languages he considers. For example, he does not adopt them with languages which, like LGTC, are used to talk about arbitrary individuals, as opposed to specific sets of them).[^note-2]

In the considerations preliminary to the presentation of his theory, Tarski says that when a sentence *X* of a formal language (e.g., LAr) is a logical consequence of a set *K* of sentences of that language, the argument with premises *K* and conclusion *X* has the following property, that Tarski calls “condition (F)”:

> (F) If, in the sentences of the class *K* and in the sentence *X*, the constants—apart from purely logical constants—are replaced by any other constants (like signs being everywhere replaced by like signs), and if we denote the class of sentences thus obtained from *K* by “*K*′”, and the sentence obtained from *X* by “*X*′”, then the sentence *X*′ must be true provided only that all sentences of the class *K*′ are true (Tarski 1983c, p. 415)[^tarski-1983c].

Let’s clarify the sense of condition (F) with an example. Consider a language LAr+ which is like LAr but has besides another individual constant, “2”, and another dyadic predicate, “Pd”, whose desired interpretations are the number 2 and the relation of being the immediate predecessor of, respectively. Let *K* be the following set of sentences of LAr+: {“∀*x*(N*x*→¬M*x*0)”, “N0”} (these sentences are true); and let *X* be the sentence “¬M00”. The argument with premises *K* and conclusion *X* is intuitively logically correct; thus, according to Tarski, it must verify condition (F). This means that *any* argument obtained from it by uniform replacement of non-logical constants by non-logical constants must be an argument where *it is not the case that the premises are true and the conclusion false*. Let’s suppose that the non-logical constants of LAr+ are “0”, “N”, “M”, “2”, and “Pd”. Replace “0” with “2” and “M” with “Pd” in the argument with premises *K* and conclusion *X* and call the resulting set of premises and conclusion “*K*′” and “*X*′”. That is, *K*′ is {“∀*x*(N*x*→¬Pd*x*2)”, “N2”} and *X*′ is “¬Pd22”. In virtue of condition (F), the argument with premises *K*′ and conclusion *X*′ must be an argument where it is not the case that the premises are true and the conclusion false; and that’s in fact the case: the first premise is false, and the second premise and the conclusion are true.

Tarski wonders if it is possible to offer condition (F) as a *definition* of the relation of logical consequence, that is, if we can take (F) not only as a necessary but also a sufficient condition for an argument to be an instance of logical consequence. His answer is that we cannot. The reason is that condition (F)

> may in fact be satisfied only because the language we are dealing with does not possess a sufficient stock of extra-logical constants. The condition (F) could be regarded as sufficient for the sentence *X* to follow from the class *K* only if the designations of all possible objects occurred in the language in question. This assumption, however, is fictitious and can never be realized (Tarski 1983b, pp. 415–6)[^tarski-1983b].

Tarski notes that in order for an argument to be an instance of logical consequence it need not be sufficient that all arguments of the same form be arguments where it is not the case that the premises are true and the conclusion false. It is conceivable that one may interpret the non-logical constants of the argument by means of certain objects (individuals, sets, etc.) in such a way that the premises thus reinterpreted become true and the conclusion becomes false, and that nevertheless (some of) those objects not be denoted by non-logical constants of the language that is being considered; in such a case we would not say that the argument is an instance of logical consequence, in spite of the fact that it would satisfy condition (F).

To give an example, suppose that the language we are considering is LAr+. Since both the relation of being less than and the relation of being the immediate predecessor of are irreflexive over the domain of the natural numbers, the sentence “∀x(N*x*→¬M*xx*)” would be a logical consequence of every set of premises on criterion (F): no replacement of the non-logical constants “N” and “M” by other non-logical constants of LAr+ turns that sentence into a falsehood. But clearly “∀*x*(N*x*→¬M*xx*)” is not a logical consequence of, say, “N0”. This can be justified, e.g., keeping fixed the usual interpretation of “0” and “N” but observing that “M” can be interpreted by means of the reflexive relation of being less than or equal to; under this interpretation, “∀*x*(N*x*→¬M*xx*)” is false, although “N0” is true. (Tarski’s remark that the supposition that all objects have names in the language can never be realized can be justified, for example, by observing that there are non-denumerably many sets of natural numbers, but in the languages he considers there are only denumerably many constants.)

Tarski’s proposal consists in making tighter the requirement expressed by condition (F), so as to incorporate the idea that a logically correct argument cannot be *reinterpreted* in such a way that the premises become true and the conclusion false; in other words, the idea that a sentence *X* is a logical consequence of a set of sentences *K* when *every interpretation on which all the sentences of K are true is an interpretation on which X is true* (or, to use a common terminology, when every interpretation *preserves* the truth of the premises in the conclusion).

As Tarski says, the idea of understanding the notion of logical consequence by means of the notion of truth preservation on all interpretations is not an original idea of his, but one implicit in the logical and mathematical practice of his time (especially among mathematicians interested in offering independence proofs). What is new to Tarski’s proposal is that he makes precise the idea using the apparatus he had developed for the mathematical characterization of satisfaction and truth. He does not give a detailed example, but it seems reasonably clear how he would proceed from the indications he gives in (1936a), (1936b) and (1937).

Tarski uses a certain precise notion of interpretation for a formal language. In our example, an *interpretation* of LAr is a sequence <*A*, *a*, *R*> that assigns appropriate objects to the non-logical constants of LAr: a set of individuals *A* to “N”, an individual *a* to “0” and a binary relation among individuals *R* to “M”. Besides, he always requires that the objects assigned by an interpretation to the other non-logical constants of a language be drawn from the set assigned to the non-logical predicate that restricts the range of quantification to a specific set of individuals (“N” in the case of LAr) (cf. Tarski 1937, §34)[^tarski-1937]; so in the case of LAr the individual assigned to “0” must belong to the set assigned to “N” and the relation assigned to “M” must be a relation among objects in the set assigned to “N”.

Tarski introduces the notion of a *sentential function*. A sentential function *S*′ of a sentence *S* is the result of uniformly replacing the non-logical constants appearing in *S* with corresponding variables of suitable types (and different from the variables already existing in the language). For example, the sentential function determined by the sentence “∀*x*(N*x*→¬M*x*0)” is the expression “∀*x*(*Px*→¬*Yxy*)” (in which “*P*”, “*Y*” and “*y*” are new variables). It is equally possible to define the more general notion of a *formula function*, in an analogous way, except that now *S* may be an open formula. The sentential functions of sentences of LAr will not in general be sentences, and so will not always be either true or false by themselves. But they will always be either true or false *with respect to interpretations of LAr*; or, as Tarski says, they will be *satisfied* or not by interpretations of LAr.

The concept of satisfaction of a sentential function by an interpretation can be defined using the Tarskian method for defining satisfaction. Say that *an interpretation <A, a, R> of LAr satisfies the formula function X with respect to a sequence f* (that assigns values from *A* to the original variables of LAr) if and only if:

1. (i) *X* is *Px*_{*n*} (for some *n*); or *X* is *Py*; or (ii) *X* is *Yx*_{*n*}*x*_{*m*} (for some *m* and *n*) and <*f*(*x*_{*n*}),*f*(*x*_{*m*})>∈*R*; or *X* is *Yyx*_{*n*} (for some *n*) and <*a*,*f*(*x*_{*n*})>∈*R*; or *X* is *Yx*_{*n*}*y* (for some *n*) and <*f*(*x*_{*n*}),*a*>∈*R*; or *X* is *Yyy* and <*a*,*a*>∈*R*; or
2. there is a formula function *Y* such that *X* is ¬*Y* and <*A*, *a*, *R*> does not satisfy *Y* with respect to sequence *f*; or
3. there are formula functions *Y* and *Z* such that *X* is (*Y*→*Z*) and either <*A*, *a*, *R*> does not satisfy *Y* with respect to sequence *f* or <*A*, *a*, *R*> satisfies *Z* with respect to sequence *f*; or, finally,
4. there is a formula function *Z* and a number *n* such that *X* is ∀*x*_{*n*}(*Px*_{*n*}→*Z*) and every sequence *g* that assigns values from *A* to the (original) variables of LAr and that differs from *f* at most in what it assigns to *x*_{*n*} is such that <*A*, *a*, *R*> satisfies *Z* with respect to *g*.[^note-3]

This is a recursive definition, entirely parallel to the definition of satisfaction of formulae by sequences in the definition of satisfaction for LCC in Tarski’s monograph on truth, that we saw in section 1 above. In the same way that that definition, the one just given can be turned into an explicit one by the same method.

The notion of satisfaction of a sentential function is easy to characterize in terms of the defined notion of satisfaction of a formula function. Say that *an interpretation* <*A*, *a*, *R*> *satisfies sentential function X* if and only if <*A*, *a*, *R*> satisfies formula function *X* with respect to every sequence. This definition is analogous to the Tarskian definition of truth.

In terms of the defined notion of satisfaction, Tarski introduces the notion of a *model* of a sentence. A model of a sentence *S* is an interpretation that satisfies the sentential function *S*′ determined by *S*; more generally, a model of a set of sentences *K* is an interpretation that satisfies all the sentential functions determined by sentences of *K*. And in terms of the defined notion of model Tarski proposes his defined notion of logical consequence. A sentence *X* is a (Tarskian) logical consequence of the sentences in set *K* if and only if every model of the set *K* is also a model of sentence *X* (cf. Tarski 1983c, p. 417)[^tarski-1983c]. Tarski proposes also a defined notion of logical truth (he uses the expression “analytic truth”) using the same apparatus: a sentence *S* is a (Tarskian) logical truth if and only if every interpretation of *S* is a model of *S*. Analogous notions of Tarskian logical consequence and logical truth can be defined for other languages using the same method we have followed with LAr, just making the obvious changes.

After presenting his definition of logical consequence, Tarski immediately adds that condition (F) can be shown to hold of arguments falling under the defined notion:

> it can be proved, on the basis of this definition, that every consequence of true sentences must be true, and also that the consequence relation which holds between given sentences is completely independent of the sense of the extra-logical constants which occur in these sentences. In brief, it can be shown that the condition (F) formulated above is necessary if the sentence *X* is to follow from the sentences of the class *K* (Tarski 1983c, p. 417)[^tarski-1983c].

(The proof that Tarski seems to have in mind is this: suppose that *X* is a Tarskian logical consequence of *K*; then there is no model of *K* which is not a model of *X*; so there is no substitution instance <*K*′, *X*′> of <*K*, *X*> such that the sentences in *K*′ are true and *X*′ is false; for if there was one such, it would readily provide an interpretation—constituted by the extensions of the extra-logical constants of <*K*′, *X*′>—which would constitute a model of *K* that would not be a model of *X*. But whether this is the proof Tarski had in mind is a disputed exegetical question.)

Hence, as was to be desired, if the defined relation of logical consequence holds for a given pair <*K*, *X*>, then also condition (F) holds for it. (Although this can be shown, the converse cannot; that is, it cannot be shown that if *X* and *K* satisfy (F) then *X* follows from *K* according to Tarski’s definition. But this is all right, since, as Tarski has already pointed out, (F) is not a sufficient condition for the ordinary notion of consequence.)

## 4. Logical constants

Tarski did not think that the construction of section 3 completely solved the problem of offering “a materially adequate definition of the concept of consequence” (Tarski 1983c, p. 418)[^tarski-1983c]. According to Tarski, perhaps the most important difficulty that remained toward solving that problem is created by the fact that “underlying our whole construction is the division of all terms of the language discussed into logical and extra-logical” (Tarski 1983c, p. 418)[^tarski-1983c]. This situation is tolerable because, as Tarski says in a letter of 1944, “it is clear that for all languages which are familiar to us such definitions [of ‘logical term’ and ‘logical truth’] can be given (or rather: have been given); moreover, they prove fruitful, and this is really the most important. We can define ‘logical terms’, e.g., by enumeration” (Tarski 1987, p. 29)[^tarski-1987][^tarski-1987-2]. But since the division is not based on a previous characterization of logical terms generally applicable to arbitrary languages, to that extent the definition of logical consequence is not fully general, and hence unsatisfactory. In the final paragraph of the consequence paper Tarski says that a positive solution to the problem would “enable us to justify the traditional boundary between logical and extra-logical expressions” (Tarski 1983c, p. 420)[^tarski-1983c]. In fact, this is the boundary which for Tarski is “underlying our whole discussion”.

Tarski says that the distinction between logical and extra-logical terms is not entirely arbitrary, because if we were to include signs like the implication sign or the universal quantifier among the extra-logical terms, “our definition of the concept of consequence would lead to results which obviously contradict ordinary usage” (Tarski 1983c, p. 418)[^tarski-1983c]. This is so because in this case the definition would not declare logical consequences many instances of the relation consecrated by the common usage of logicians. However, Tarski does not seem to worry that the opposite problem may arise. The possibility exists, according to him, of extending the set of logical terms without making the definition of logical consequence useless. Even if all terms of the language are considered logical, the definition results in a characterization of a special concept of consequence, that of material consequence.

When he speaks of extending liberally the set of logical terms, Tarski is perhaps thinking of the phenomenon of what he calls the “disciplines preceding a given discipline” in Tarski (1937) (see p. 80). He speaks of logic as preceding every discipline, in the sense that logical constants and logical laws are presupposed by and form part of every science. But similarly, in developing a certain theory, not only logic but other theories may be taken for granted; thus Tarski speaks of logic and arithmetic as a conveniently presupposed basis of theories for the development of geometry. This would account naturally for the fact that Tarski was skeptical about the possibility of finding a sharp distinction between logical and extra-logical terms, for it might very well depend on the context of investigation what terms and what laws are considered as forming part of the “logic” of the investigation.

An example which we know Tarski had in mind is the sign for the membership relation. We find him saying: “sometimes it seems to me convenient to include mathematical terms, like the ∈-relation, in the class of logical ones, and sometimes I prefer to restrict myself to terms of ‘elementary logic’. Is any problem involved here?” (Tarski 1987, p. 29)[^tarski-1987][^tarski-1987-2]. We may take the sign for membership as a logical sign in some formalizations of the theory of types (which can in turn be used to formalize theories with arbitrary universes of individuals). But when doing set theory for its own sake, the appropriate thing is not to take membership as a logical notion, and not to assume principles about membership as forming part of the “logic” of the theory, but as postulates thereof. Tarski’s final remarks in the paper on logical consequence again put forward the view that the notion of logical constant may be of a relative character. In different contexts different terms may be taken as logical and therefore so may vary the extension of the relation of logical consequence. He says that “the fluctuation in the common usage of the concept of consequence would—in part at least—be quite naturally reflected in such a compulsory situation” of relativity (Tarski 1983c, p. 420)[^tarski-1983c].

But this does not mean that no desiderata could or should be imposed on a definition of the concept of a logical constant. Many years after writing his paper on logical consequence, Tarski returned to the problem of the definition of the concept of a logical term, advancing an attempt at a positive solution. Tarski thought that this solution accommodated his conviction that the notion of a logical term is not an absolute, but a relative one.

The basis for the proposed solution appears in Tarski’s 1966 lecture “What are Logical Notions?” (published posthumously as Tarski 1986a)[^tarski-1986a]. Here Tarski first makes some remarks about the general nature of his proposal. He says that an answer to a question like the one that gives title to the lecture may take several forms. It may give an account of the prevailing usage of the term “logical notion”, or of the prevailing usage of the term among people who are qualified to use it. It may be a normative proposal, a suggestion that the term be used in a certain way, independently of its actual use. As a third possibility, some other answers

> seem to aim at something very different (…); people speak of catching the proper, true meaning of a notion, something independent of actual usage, and independent of any normative proposals, something like the platonic idea behind the notion. This last approach is so foreign and strange to me that I shall simply ignore it for I cannot say anything intelligent on such matters (Tarski 1986a, p. 145)[^tarski-1986a].

Immediately Tarski makes it clear that he is also not concerned with developing a normative proposal, but an account which captures a certain common use of the concept of logical notion: “in answering the question ‘What are logical notions?’ what I shall do is make a suggestion or proposal about a possible use of the term ‘logical notion’. This suggestion seems to me to be in agreement, if not with a prevailing usage of the term ‘logical notion’, at least with one usage which actually is encountered in practice” (Tarski 1986a, p. 145)[^tarski-1986a].

What are notions? Tarski says:

> I use the term “notion” in a rather loose and general sense, to mean, roughly speaking, objects of all possible types in some hierarchy of types like that in *Principia mathematica*. Thus notions include individuals (…), classes of individuals, relations of individuals, classes of classes of individuals, and so on (Tarski 1986a, p. 147)[^tarski-1986a].

He then proposes to define logical notions as those notions invariant under all one-one transformations of the universe of discourse onto itself:

> consider the class of *all* one-one transformations of the space, or universe of discourse, or “world”, onto itself. What will be the science which deals with the notions invariant under this widest class of transformations? Here we will have very few notions, all of a very general character. I suggest that they are the logical notions, that we call a notion “logical” if it is invariant under all possible one-one transformations of the world onto itself (Tarski 1986a, p. 149)[^tarski-1986a].

A one-one transformation of a class onto itself, also called a permutation, induces permutations of all the types in the hierarchy of types of “notions” determined by the class. Thus, a permutation *P* of a domain of individuals *D* induces a permutation of the class of *n*-ary relations of elements of *D*, a permutation of the class of functions with n arguments with domain *D*^{*n*} and range included in *D*, a permutation of the class of *n*-ary relations among relations of elements of *D*, etc. A notion or object *O* of a certain type *t* is invariant under all permutations of the universe of discourse if, for every permutation *P* of this universe, the permutation *P̃* induced by *P* in the class of notions of type *t* is such that *P̃*(*O*)=*O*.

There is no straightforward way in which the truth-functions and the quantifiers (over any type of objects) are identifiable with notions in the sense of Tarski. According to John Corcoran (see footnote 6 in Tarski 1986a, p. 150)[^tarski-1986a], in one version of the lecture Tarski indicated that the truth-functions and classical quantifiers can be constructed as certain objects in the type hierarchy that are invariant under all permutations, and, in this sense, are logical notions. (Clearly, Tarski took the logicality of these notions almost for granted, and was concerned with a definition which gave some account of the status of other more substantive notions in various mathematical languages.) For example, the truth-values “true” and “false” can be identified with the universe of individuals and the null set, respectively, and the truth-functions in turn with functions having (tuples of) these classes as arguments and values; and the classical universal and existential quantifiers over a type of objects *t* can be identified with certain functions from the class of sets of objects of type *t* into the class of truth-values—identifying “true” with the universal set of objects of type *t* and “false” with the empty set of that type. (A universal quantifier will assign “true” to the set of all objects of type *t*, and “false” to all other subsets of *t*; and the existential quantifier will assign “true” to the non-empty subsets, and “false” to the empty subset.)

In 1966 Tarski does not propose a definition of the concept of logical constant. One such definition, based on the 1966 idea, appears in a book Tarski wrote in collaboration with Steven Givant, published in 1987, four years after Tarski’s death. The main concern of Tarski and Givant (1987) is to indicate how to develop set theory in several different languages and to compare their expressive power. They define the concept of logical constant for constants in the vocabulary of a certain class of languages—all of which are in a certain sense extensions of a basic language in which they are particularly interested, weaker than the languages in which set theory is usually developed in means of expression, and yet sufficiently powerful for many purposes. The vocabulary of the basic language is composed of three two-place predicate constants of the second type and four two-place function constants of the third type; the vocabulary of the extensions considered by Tarski and Givant can only include constants of those two kinds. (However, as we will see, there does not seem to be any problem in extending the range of applicability of their definition to wider classes of languages.) They then prove several results about that class of languages, results that involve the defined concept of logical constant.

Tarski and Givant introduce informally the concept of a derivative universe of a given basic universe *U*. A derivative universe *Ũ* of a given basic universe *U* is what we have been calling the class of all objects of a certain type, generated from that basic universe *U*. Thus, the class of *n*-ary relations of elements of *U* (for any given *n*), the class of *n*-ary relations among relations of elements of *U*, etc., are derivative universes of *U*. After introducing in the same way as above the concepts of a permutation of the universe and of invariance of a member of a derivative universe under every permutation of the basic universe, Tarski and Givant give the following definitions:

1. Given a basic universe *U*, a member *M* of any derivative universe *Ũ* is said to be logical, or a logical object, if it is invariant under every permutation *P* of *U*. (Strictly speaking, since an object *M* can be a member of many derivative universes, we should use in (i) the phrase “is said to be logical, or a logical object, as a member of *Ũ*”.)
2. A symbol *S* of [a language in the class considered by Tarski and Givant] is said to be logical, or a logical constant, if, for every given realization **U** of this [language] with the universe *U*, *S* denotes a logical object in some derivative universe *Ũ* (Tarski and Givant 1987, p. 57)[^tarski-1987][^tarski-1987-2].

(i) and the parenthetical comment that comes after it embody fairly accurately the basic idea behind the (relativized) definition of a logical notion offered in Tarski (1986a), and (ii) offers the (absolute) definition of the concept of logical constant. There is no apparent obstacle to applying (ii) to wider classes of languages than the class considered for special purposes of their investigation by Tarski and Givant. It seems safe to assume that the definition can be applied to a large class of languages in the classical hierarchy of quantificational languages. Tarski and Givant themselves say that the usual logical constants of languages not in the class considered by them, like the symbols for the truth-functional connectives and quantifiers, “can also be subsumed under logical constants in the sense of (ii)” (Tarski and Givant 1987, p. 57)[^tarski-1987][^tarski-1987-2], presumably through some artifice in the style of the one discussed above. (As we will soon see, at the very least Tarski clearly would want his definition to be applicable to some languages whose set of sentences is that of some formulations of the simple theory of types.)

In Tarski and Lindenbaum (1935) the authors had proved that given a basic universe *U*, all the notions in derivative universes of *U* which can be defined in the language of the simple theory of types are invariant under all permutations of *U*. In general the Tarski-Lindenbaum theorem guarantees that all mathematical notions definable in the logicist fashion in the simple theory of types are logical notions no matter what the universe of individuals is taken to be (Tarski says that “we may interpret [the universe of the intended interpretation of the language of the theory of types] as the universe of physical objects, although there is nothing in *Principia mathematica* which compels us to accept such an interpretation” (Tarski 1986a, p. 152)[^tarski-1986a]). Since the theorem applies to every universe *U* supplying an interpretation of the language of the theory of types, the definition of the concept of logical constant in Tarski and Givant (1987) implies that all primitive symbols denoting notions in that language (e.g. quantifiers of all orders) are Tarskian logical constants; also, if the definition were applicable to defined symbols, all these symbols would be Tarskian logical constants. Such results agree well with a “usage actually encountered in practice” (for example, the practice of the logicists, but of others as well) according to which the constants of the language of the theory of types are logical constants.

When the Tarski-Givant definition is applied to interpreted languages of mathematical theories with undefined mathematical primitives, it will generally yield the result that the notions denoted by these primitives are not Tarskian logical constants. Tarski’s example is set theory formalized in first-order with a single primitive predicate for membership as a relation among elements of the universe (see Tarski 1986a, p. 153)[^tarski-1986a]. Obviously membership as a relation over a domain of individuals and sets is not invariant under all permutations of that domain, so it is not declared a logical notion of the language of set theory by Tarski’s proposed definition. Similarly, the class of all sets will be declared non-logical provided the class of individuals that are not sets is not empty. A predicate whose intended meaning is membership (among elements of the universe) is not a Tarskian logical constant, simply because there is a universe in which it denotes a non-logical object (with respect to that universe); similarly, a predicate “*S*” whose intended meaning is “is a set” (such as is used in some formalizations of set theory suitable for contemplating individuals other than sets in the universe) is not a Tarskian logical constant, for there is a universe in which “*S*” denotes a non-logical object (in such a universe, the class of objects that are not sets must be non-empty). These results are again in agreement with actual usage, for example in the model theory of first-order set theory, where the membership predicate is taken as a non-logical constant.

From the consideration of the examples provided by the theory of types and first-order set theory, Tarski extracts a conclusion that he welcomed. This is the conclusion that, in a certain sense, the distinction between logical and non-logical constants is relative to a context of investigation. Recall Tarski’s remarks about the sign for membership in a letter of 1944. In the 1966 lecture Tarski says that membership is a logical notion in some formalizations of the theory of types. He says:

> Using this method [of *Principia Mathematica*], it is clear that the membership relation is certainly a logical notion. It occurs in several types, for individuals are elements of classes of individuals, classes of individuals are elements of classes of classes of individuals, and so on. And by the very definition of an induced transformation it is invariant under every transformation of the world onto itself (Tarski 1986a, pp. 152–3)[^tarski-1986a].

It is a bit unclear that the “notions” of membership that Tarski talks about are notions in the sense introduced by him earlier in the lecture. They do not “occur” in any type, given the standard formulations of the theory of types (even in formulations in which a sign for membership is used), for they are relations among objects of different types, which do not occur in a non-cumulative hierarchy. But Tarski is perhaps thinking of some non-standard, cumulative type hierarchy. Under a suitable expansion of the concept of a notion, the notions of membership Tarski has in mind will indeed be invariant under permutations of any universe, and hence logical; and the sign or signs for these notions of membership will be Tarskian logical constants. On the other hand, as pointed out above, membership as a relation over the domain of individuals and sets will not be a logical notion in that domain, and hence the sign for this concept of membership will not be a Tarskian logical constant. Thus, interestingly, Tarski’s definition of the concept of logical constant respects in a sense his early relativistic view in the paper on logical consequence. Tarski describes the situation in the following passage:

> Since it is now well known that the whole of mathematics can be constructed within set theory, or the theory of classes, the problem [of whether mathematical notions are logical notions] reduces to the following one: Are set-theoretical notions logical notions or not? Again, since it is known that all usual set-theoretical notions can be defined in terms of one, the notion of belonging, or the membership relation, the final form of our question is whether the membership relation is a logical one in the sense of my suggestion. The answer will seem disappointing. For we can develop set theory, the theory of the membership relation, in such a way that the answer to this question is affirmative, or we can proceed in such a way that the answer is negative (Tarski 1986a, pp. 151–2)[^tarski-1986a].

## 5. Further reading

Tarski’s papers are reprinted and collected in Tarski 1986b. The volume Tarski 1983a contains widely used English translations of his main papers of the 1920s and 1930s. Givant (1986) gives a complete bibliography of Tarski’s publications until 1986. Feferman and Feferman 2004 is a biography of Tarski that also contains a very valuable introduction to his logical and mathematical work, including descriptions of all the results and developments mentioned in the initial paragraph of this entry. On Tarski’s logical work see also Simmons 2009 and Eastaugh 2017. McFarland, McFarland & Smith 2014 contains a wealth of biographical and historical information about Tarski, as well as updates to Givant’s bibliography and translations into English of a number of previously untranslated early texts by Tarski. Also of much biographical interest are the letters from Tarski to J. H. Woodger included in Mancosu 2021.

Collections of articles devoted to (parts of) Tarski’s work include: vols. 51 (1986) and 53 (1988) of the *Journal of Symbolic Logic*; Woleński and Köhler (1999); vols. 126 (2001) and 142 (2004) of *Synthese*; vols. 126 and 127 of the *Annals of Pure and Applied Logic* (2004); Patterson 2008a; and Sagi and Woods 2021. Patterson 2012 is a book-length historical and philosophical study of many of Tarski’s philosophical ideas, focusing on truth and logical consequence. Gruber 2016 is a book-length commentary of Tarski’s monograph on truth, “The Concept of Truth in Formalized Languages”, which compares the Polish original version, the German translation, and the English version of the German text.

There is a considerable bibliography on critical and exegetical aspects of Tarski’s philosophical work. The bibliography on truth is especially extensive. It includes the chapters on Tarski’s theory of truth in Coffa 1991; Kirkham 1992; Soames 1999, 2010, and 2018; Künne 2003; Burgess and Burgess 2011; and Blackburn 2018; many chapters of Woleński 1999 and 2019; the papers Field 1972; Davidson 1973, 1990; Kripke 1975, 2019; Church 1976; Soames 1984; Putnam 1985; Hodges 1985/6, 2004, and 2008; McGee 1993; García-Carpintero 1996; Heck 1997; Murawski 1998; DeVidi and Solomon 1999; Ketland 1999; Milne 1999; Sher 1999; Gómez-Torrente 2001, 2004, and 2019; Eklund 2002; Gupta 2002; Rojszczak 2002; Raatikainen 2003, 2008; Ray 2003, 2005, 2018; Sundholm 2003; Feferman 2004a; Frost-Arnold 2004; Hintikka 2004; Patterson 2004, 2008b; Azzouni 2005, 2008; Horwich 2005; Burgess 2008; David 2008; Mancosu 2008; Simons 2008; Asay 2013; Schiemer and Reck 2013; Loeb 2014; Barnard and Ulatowski 2016; Smith 2017; Simchen 2020; and the entries on the liar paradox, model theory, Tarski: truth definitions, and truth.

The critical and exegetical bibliography on Tarski on logical consequence includes Kneale and Kneale 1962; Etchemendy 1988, 1990, and 2008; McGee 1992, 2004; Gómez-Torrente 1996, 1998/9, 2008, and 2009; Ray 1996;, Sher 1996, 2022; Hanson 1997; Sagüillo 1997; Chihara 1998; Shapiro 1998; Schurz 1999; Blanchette 2000; Bays 2001; Edwards 2003; Jané 2006; Mancosu 2006, 2010; Park 2018; Zinke 2018; Griffiths and Paseau 2022; and the entries on logical consequence and logical truth.

The Tarskian ideas on logical constants are discussed, among other places, in Simons 1987; Sher 1991, 2008, and 2021; Feferman 1999; Gómez-Torrente 2002, 2021; Bellotti 2003; Casanovas 2007; Bonnay 2008, 2014; Dutilh Novaes 2014; Sagi 2015, 2018, and 2021; Bonnay and Speitel 2021; Kennedy 2021; Kennedy and Väänänen 2021; and the entry on logical constants.

The literature on general philosophical aspects of Tarski’s work and opinions includes Suppes 1988; Woleński 1993; Sinaceur 2001; Feferman 2004b; Mycielski 2004; Mancosu 2005, 2009; Betti 2008; and Frost-Arnold 2008, 2013.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

### Primary Sources: Works by Tarski

### Secondary Sources

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=tarski). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/tarski/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=tarski&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/tarski/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- [Tarski, Alfred](https://mathshistory.st-andrews.ac.uk/Biographies/Tarski/). (Entry in the MacTutor History of Mathematics archive.)
- [Tarski’s Revolution: A New History](http://www.axiom.humanities.uva.nl/content.html). (A research project at the Vrije Universiteit Amsterdam.)
- [Finding Aid to the Alfred Tarski papers](http://www.oac.cdlib.org/findaid/ark:/13030/c8cr5txf/). (A guide to the Tarski papers archived at the Bancroft Library of the University of California at Berkeley.)

## Related Entries

algebra | Carnap, Rudolf | Gödel, Kurt | Leśniewski, Stanisław | liar paradox | logic: classical | logic: second-order and higher-order | logical consequence | logical constants | logical truth | Lvov-Warsaw School | model theory | reference | Russell, Bertrand | set theory | Tarski, Alfred: truth definitions | truth | type theory | Vienna Circle | Whitehead, Alfred North

### Acknowledgments

I thank Paolo Mancosu and Richard Zach for helpful comments on an earlier version of this entry.

## Notes（原文脚注）

[^note-1]: Hodges (1985/6) claims that no notion defined by Tarski in the monograph on truth possesses all the crucial features of the notion of truth in a structure, and thus that this notion is not really defined by Tarski at this time. (See also Milne 1999. Gómez-Torrente 2001 contains a critique of Hodges’s claim.)[^gómez-torrente-2001][^milne-1999]

[^note-2]: The claim that in the 1936 paper Tarski is primarily thinking of languages with the conventions of LAr is controversial. It is defended in Gómez-Torrente (1996), (2009) and disputed e.g. in Mancosu (2006), (2010). According to Mancosu, Tarski is paradigmatically thinking of languages like LAr*: LAr* is like LAr except that quantifications need not be relativized to “*N*”, and the range of the variables is the set of all individuals of some underlying type theory. See the next footnote.

[^note-3]: A very similar definition can be given for languages like LAr* (see the preceding footnote): *an interpretation <A, a, R> of LAr* satisfies the formula function X with respect to a sequence f* (that assigns arbitrary values from the set of individuals of an underlying type theory to the original variables of LAr*) if and only if:

1. (i) *X* is *P**x*ₙ (for some *n*) and *f*(*x*_{*n*})∈*A*; or *X* is *P**y* and *a*∈*A*; or (ii) *X* is *Y**x*_{*n*}*x*_{*m*} (for some *m* and *n*) and <*f*(*x*_{*n*}),*f*(*x*_{*m*})>∈*R*; or *X* is *Y**y**x*_{*n*} (for some *n*) and <*a*,*f*(*x*_{*n*})>∈*R*; or *X* is *Y**x*_{*n*}*y* (for some *n*) and <*f*(*x*_{*n*}),*a*>∈*R*; or *X* is *Y**y**y* and <*a*,*a*>∈*R*; or
2. there is a formula function *Y* such that *X* is ¬*Y* and <*A*, *a*, *R*> does not satisfy *Y* with respect to sequence *f*; or
3. there are formula functions *Y* and *Z* such that *X* is (*Y*→*Z*) and either <*A*, *a*, *R*> does not satisfy *Y* with respect to sequence *f* or <*A*, *a*, *R*> satisfies *Z* with respect to sequence *f*; or, finally,
4. there is a formula function *Z* and a number *n* such that *X* is ∀*x*_{*n*}*Z* and every sequence *g* that assigns arbitrary values to the (original) variables of LAr and that differs from *f* at most in what it assigns to *x*_{*n*} is such that <*A*, *a*, *R*> satisfies *Z* with respect to *g*.

[^tarski-1931]: Tarski, A., 1931. “Sur les ensembles définissables de nombres réels. I.”, *Fundamenta Mathematicae*, 17: 210–239.

[^tarski-1933]: –––, 1933. *Pojęcie prawdy w językach nauk dedukcyjnych*, Warsaw: Nakładem Towarzystwa Naukowego Warszawskiego.

[^tarski-1935]: –––, 1935. “Der Wahrheitsbegriff in den formalisierten Sprachen”, *Studia Philosophica*, 1: 261–405. Translation of Tarski 1933 by L. Blaustein, with a postscript added.

[^tarski-1936a]: –––, 1936a. “O pojęciu wynikania logicznego”, *Przegląd Filozoficzny*, 39: 58–68.

[^tarski-1936b]: –––, 1936b. “Über den Begriff der logischen Folgerung”, in *Actes du Congrès International de Philosophie Scientifique,* fasc. 7 (Actualités Scientifiques et Industrielles, vol. 394), Paris: Hermann et Cie, pp. 1–11.

[^tarski-1937]: –––, 1937. *Einführung in die mathematische Logik und in die Methodologie der Mathematik.* Vienna: Julius Springer. (Translated with additions as Tarski 1941.)

[^tarski-1941]: –––, 1941. *Introduction to Logic and to the Methodology of Deductive Science*, translation of Tarski 1937 by O. Helmer, with additions. New York: Oxford University Press.

[^tarski-1944]: –––, 1944. “The Semantic Conception of Truth: And the Foundations of Semantics”, *Philosophy and Phenomenological Research*, 4: 341–376.

[^tarski-1983a]: –––, 1983a. *Logic, Semantics, Metamathematics,* second edition, ed. by J. Corcoran. Indianapolis: Hackett.

[^tarski-1983b]: –––, 1983b. “The Concept of Truth in Formalized Languages”, translation of Tarski 1935 by J.H. Woodger in Tarski 1983a, pp. 152–278.

[^tarski-1983c]: –––, 1983c. “On the Concept of Logical Consequence”, translation of Tarski 1936b by J.H. Woodger in Tarski 1983a, pp. 409–20.

[^tarski-1983d]: –––, 1983d. “On Definable Sets of Real Numbers”, translation of Tarski 1931 by J.H. Woodger in Tarski 1983a, pp. 110–142.

[^tarski-1986a]: –––, 1986a. “What Are Logical Notions?”, ed. by J. Corcoran. *History and Philosophy of Logic*, 7: 143–54.

[^tarski-1986b]: –––, 1986b. *Collected Papers*, four volumes, ed. by S. Givant and R. McKenzie. Basel: Birkhäuser.

[^tarski-1987]: –––, 1987. “A Philosophical Letter of Alfred Tarski”, *Journal of Philosophy*, 84: 28–32. A 1944 letter of Tarski to Morton White, published with a preface of the latter.

[^tarski-2002]: –––, 2002. “On the Concept of Following Logically”, translation of Tarski 1936a by M. Stroińska and D. Hitchcock. *History and Philosophy of Logic*, 23: 155–96.

[^tarski-1987-2]: –––, and S. Givant, 1987. *A Formalization of Set Theory without Variables*, Providence, RI: American Mathematical Society.

[^tarski-1935-2]: –––, and A. Lindenbaum, 1935. “Über die Beschränktheit der Ausdrucksmittel deduktiver Theorien”, in *Ergebnisse eines mathematischen Kolloquiums,* fasc. 7, 1934–1935, pp. 15–22. (Translated as Tarski and Lindenbaum 1983.)

[^tarski-1983]: –––, and A. Lindenbaum, 1983. “On the Limitations of the Means of Expression of Deductive Theories”, translation of Tarski and Lindenbaum 1935 by J.H. Woodger in Tarski 1983a, pp. 384–392.

[^asay-2013]: Asay, J., 2013. “Tarski and Primitivism about Truth”, *Philosophers’ Imprint*, 13: 1–18.

[^azzouni-2005]: Azzouni, J., 2005. “Tarski, Quine, and the Transcendence of the Vernacular ‘True’”, *Synthese*, 142: 273–88.

[^azzouni-2008]: –––, 2008. “Alternative Logics and the Role of Truth in the Interpretation of Languages”, in Patterson 2008a, pp. 390–429.

[^barnard-2016]: Barnard, R. and J. Ulatowski, 2016. “Tarski’s 1944 Polemical Remarks and Naess’ ‘Experimental Philosophy’”, *Erkenntnis*, 81: 457–477.

[^bays-2001]: Bays, T., 2001. “On Tarski on Models”, *Journal of Symbolic Logic*, 66: 1701–26.

[^bellotti-2003]: Bellotti, L., 2003. “Tarski on Logical Notions”, *Synthese*, 135: 401–13.

[^betti-2008]: Betti, A., 2008. “Polish Axiomatics and its Truth: On Tarski’s Leśniewskian Background and the Ajdukiewicz Connection”, in Patterson 2008a, pp. 44–71.

[^blackburn-2018]: Blackburn, S., 2018. *Truth*, Oxford: Oxford University Press.

[^blanchette-2000]: Blanchette, P., 2000. “Models and Modality”, *Synthese*, 124: 45–72.

[^bonnay-2008]: Bonnay, D., 2008. “Logicality and Invariance”, *Bulletin of Symbolic Logic*, 14: 29–68.

[^bonnay-2014]: –––, 2014. “Logical Constants, or How to Use Invariance in Order to Complete the Explication of Logical Consequence”, *Philosophy Compass*, 9: 54–65.

[^bonnay-2021]: Bonnay, D. and S. Speitel, 2021. “The Ways of Logicality: Invariance and Categoricity”, in Sagi and Woods 2021, pp. 55–79.

[^burgess-2008]: Burgess, J.P., 2008. “Tarski’s Tort”, in Burgess, *Mathematics, Models, and Modality. Selected Philosophical Essays*, Cambridge: Cambridge University Press, pp. 149–68.

[^burgess-2011]: Burgess, A.G. and J.P. Burgess, 2011. *Truth*, Princeton, NJ: Princeton University Press.

[^casanovas-2007]: Casanovas, E., 2007. “Logical Operations and Invariance”, *Journal of Philosophical Logic*, 36: 33–60.

[^chihara-1998]: Chihara, C., 1998. “Tarski’s Thesis and the Ontology of Mathematics”, in M. Schirn (ed.), *The Philosophy of Mathematics Today*, Oxford: Clarendon Press, pp. 157–72.

[^church-1976]: Church, A., 1976. “Comparison of Russell’s Resolution of the Semantical Antinomies with That of Tarski”, *Journal of Symbolic Logic*, 41: 747–60.

[^coffa-1991]: Coffa, J.A., 1991. *The Semantic Tradition from Kant to Carnap*, Cambridge: Cambridge University Press.

[^david-2008]: David, M., 2008. “Tarski’s Convention T and the Concept of Truth”, in Patterson 2008a, pp. 133–56.

[^davidson-1973]: Davidson, D., 1973. “In Defence of Convention T”, reprinted in Davidson, *Inquiries into Truth and Interpretation*, New York: Oxford University Press, 1984, pp. 65–75.

[^davidson-1990]: –––, 1990. “The Structure and Content of Truth”, *Journal of Philosophy*, 87: 279–328.

[^devidi-1999]: DeVidi, D. and G. Solomon, 1999. “Tarski on ‘Essentially Richer’ Metalanguages”, *Journal of Philosophical Logic*, 28: 1–28.

[^dutilh-2014]: Dutilh Novaes, C., 2014. “The Undergeneration of Permutation Invariance as a Criterion for Logicality”, *Erkenntnis*, 79: 81–97.

[^eastaugh-2017]: Eastaugh, B., 2017. “Tarski”, in A. Malpass and M. Antonutti Marfori (eds.), *The History of Philosophical and Formal Logic: From Aristotle to Tarski*, London: Bloomsbury, pp. 293–313.

[^edwards-2003]: Edwards, J., 2003. “Reduction and Tarski’s Definition of Logical Consequence”, *Notre Dame Journal of Formal Logic*, 44: 49–62.

[^eklund-2002]: Eklund, M., 2002. “A Vindication of Tarski’s Claims about the Liar Paradox”, in T. Childers (ed.), *The Logica Yearbook 2001*, Prague: Filosofia, pp. 49–55.

[^etchemendy-1988]: Etchemendy, J., 1988. “Tarski on Truth and Logical Consequence”, *Journal of Symbolic Logic*, 53: 51–79.

[^etchemendy-1990]: –––, 1990. *The Concept of Logical Consequence*, Cambridge, MA: Harvard University Press.

[^etchemendy-2008]: –––, 2008. “Reflections on Consequence”, in Patterson 2008a, pp. 263–99.

[^feferman-1999]: Feferman, S., 1999. “Logic, Logics, and Logicism”, *Notre Dame Journal of Formal Logic*, 40: 31–54.

[^feferman-2004a]: –––, 2004a. “Tarski’s Conceptual Analysis of Semantical Notions”, in A. Benmakhlouf (ed.), *Sémantique et Épistemologie*, Casablanca-Paris: Le Fennec-Vrin, pp. 79–108. Reprinted in Patterson 2008a, pp. 72–93.

[^feferman-2004b]: –––, 2004b. “Tarski’s Conception of Logic”, *Annals of Pure and Applied Logic*, 126: 5–13.

[^feferman-2004]: Feferman, A.B. and S. Feferman, 2004. *Alfred Tarski. Life and Logic*, Cambridge: Cambridge University Press.

[^field-1972]: Field, H., 1972. “Tarski’s Theory of Truth”, reprinted in Field, *Truth and the Absence of Fact*, New York: Oxford University Press, 2001, pp. 3–26.

[^frost-arnold-2004]: Frost-Arnold, G., 2004. “Was Tarski’s Theory of Truth Motivated by Physicalism?”, *History and Philosophy of Logic*, 25: 265–80.

[^frost-arnold-2008]: –––, 2008. “Tarski’s Nominalism”, in Patterson 2008a, pp. 225–46.

[^frost-arnold-2013]: –––, 2013. *Carnap, Tarski, and Quine at Harvard. Conversations on Logic, Mathematics, and Science*, Chicago: Open Court.

[^garcía-carpintero-1996]: García-Carpintero, M., 1996. “What Is a Tarskian Definition of Truth?”, *Philosophical Studies*, 82: 113–44.

[^givant-1986]: Givant, S., 1986. “Bibliography of Alfred Tarski”, *Journal of Symbolic Logic*, 51: 913–41.

[^gómez-torrente-1996]: Gómez-Torrente, M., 1996. “Tarski on Logical Consequence”, *Notre Dame Journal of Formal Logic*, 37: 125–51.

[^gómez-torrente-1998]: –––, 1998/9. “Logical Truth and Tarskian Logical Truth”, *Synthese*, 117: 375–408.

[^gómez-torrente-2001]: –––, 2001. “Notas sobre el *Wahrheitsbegriff*”, parts I and II. *Análisis Filosófico*, 21: 5–41, 149–85.

[^gómez-torrente-2002]: –––, 2002. “The Problem of Logical Constants”, *Bulletin of Symbolic Logic*, 8: 1–37.

[^gómez-torrente-2004]: –––, 2004. “The Indefinability of Truth in the ‘Wahrheitsbegriff’”, *Annals of Pure and Applied Logic*, 126: 27–37.

[^gómez-torrente-2008]: –––, 2008. “Are There Model-Theoretic Logical Truths that are not Logically True?”, in Patterson 2008a, pp. 340–68.

[^gómez-torrente-2009]: –––, 2009. “Rereading Tarski on Logical Consequence”, *Review of Symbolic Logic*, 2: 249–97.

[^gómez-torrente-2019]: –––, 2019. “Soames on the Logical Empiricists on Truth, Meaning, Convention, and Logical Truth”, *Philosophical Studies*, 176: 1357–65.

[^gómez-torrente-2021]: –––, 2021. “The Problem of Logical Constants and the Semantic Tradition: From Invariantist Views to a Pragmatic Account”, in Sagi and Woods 2021, pp. 35–54.

[^griffiths-2022]: Griffiths, O. and A.C. Paseau, 2022. *One True Logic: A Monist Manifesto*, Oxford: Oxford University Press.

[^gruber-2016]: Gruber, M., 2016. *Alfred Tarski and the “Concept of Truth in Formalized Languages”. A Running Commentary with Consideration of the Polish Original and the German Translation*, Cham: Springer.

[^gupta-2002]: Gupta, A., 2002. “An Argument against Tarski’s Convention T”, in R. Schantz (ed.), *What Is Truth?*, Berlin: De Gruyter, pp. 225–37.

[^hanson-1997]: Hanson, W., 1997. “The Concept of Logical Consequence”, *Philosophical Review*, 106: 365–409.

[^heck-1997]: Heck, R., 1997. “Tarski, Truth, and Semantics”, *Philosophical Review*, 106: 533–54.

[^hintikka-2004]: Hintikka, J., 2004. “On Tarski’s Assumptions”, *Synthese*, 142: 353–69.

[^hodges-1985]: Hodges, W., 1985/6. “Truth in a Structure”, *Proceedings of the Aristotelian Society*, 86: 135–51.

[^hodges-2004]: –––, 2004. “What Languages Have Tarski Truth Definitions?”, *Annals of Pure and Applied Logic*, 126: 93–113.

[^hodges-2008]: –––, 2008. “Tarski’s Theory of Definition”, in Patterson 2008a, pp. 94–132.

[^horwich-2005]: Horwich, P., 2005. “A Minimalist Critique of Tarski on Truth”, in JC Beall (ed.), *Deflationism and Paradox*, Oxford: Clarendon Press, pp. 75–84.

[^jané-2006]: Jané, I., 2006. “What Is Tarski’s *Common* Concept of Consequence?”, *Bulletin of Symbolic Logic*, 12: 1–42.

[^kennedy-2021]: Kennedy, J., 2021. *Gödel, Tarski and the Lure of Natural Language. Logical Entanglement, Formalism Freeness*, Cambridge: Cambridge University Press.

[^kennedy-2021-2]: Kennedy, J. and J. Väänänen, 2021. “Logicality and Model Classes”, *Bulletin of Symbolic Logic*, 27: 385–414.

[^ketland-1999]: Ketland, J., 1999. “Deflationism and Tarski’s Paradise”, *Mind*, 108: 69–94.

[^kirkham-1992]: Kirkham, R., 1992. *Theories of Truth*, Cambridge, MA: MIT Press.

[^kneale-1962]: Kneale, W. and M. Kneale, 1962. *The Development of Logic*, Oxford: Clarendon Press.

[^kripke-1975]: Kripke, S., 1975. “Outline of a Theory of Truth”, *Journal of Philosophy*, 72: 690–716.

[^kripke-2019]: –––, 2019. “Ungroundedness in Tarskian Languages”, *Journal of Philosophical Logic*, 48: 603–9.

[^künne-2003]: Künne, W., 2003. *Conceptions of Truth*, Oxford: Clarendon Press.

[^loeb-2014]: Loeb, I., 2014. “Towards Transfinite Type Theory: Rereading Tarski’s Wahrheitsbegriff”, *Synthese*, 191: 2281–99.

[^mcfarland-2014]: McFarland, A., J. McFarland, and J. T. Smith (eds.), 2014. *Alfred Tarski. Early Work in Poland – Geometry and Teaching*, New York: Birkhäuser.

[^mcgee-1992]: McGee, V., 1992. “Two Problems with Tarski’s Theory of Consequence”, *Proceedings of the Aristotelian Society*, 92: 273–92.

[^mcgee-1993]: –––, 1993. “A Semantic Conception of Truth?”, *Philosophical Topics*, 21: 83–111.

[^mcgee-2004]: –––, 2004. “Tarski’s Staggering Existential Assumptions”, *Synthese*, 142: 371–87.

[^mancosu-2005]: Mancosu, P., 2005. “Harvard 1940–1941: Tarski, Carnap and Quine on a Finitistic Language of Mathematics for Science”, *History and Philosophy of Logic*, 26: 327–57.

[^mancosu-2006]: –––, 2006. “Tarski on Models and Logical Consequence”, in J. Ferreirós and J. J. Gray (eds.), *The Architecture of Modern Mathematics*, Oxford: Oxford University Press, pp. 209–37.

[^mancosu-2008]: –––, 2008. “Tarski, Neurath, and Kokoszyńska on the Semantic Conception of Truth”, in Patterson 2008a, pp. 192–224.

[^mancosu-2009]: –––, 2009. “Tarski’s Engagement with Philosophy”, in S. Lapointe *et al*, (eds.), *The Golden Age of Polish Philosophy*, Dordrecht: Springer, pp. 131–53.

[^mancosu-2010]: –––, 2010. “Fixed- Versus Variable-Domain Interpretations of Tarski’s Account of Logical Consequence”, *Philosophy Compass*, 5: 745–759.

[^mancosu-2021]: –––, 2021. “Logic and Biology: The Correspondence Between Alfred Tarski and Joseph H. Woodger”, *Journal of Humanistic Mathematics*, 11: 18–105. doi:10.5642/jhummath.202102.04

[^milne-1999]: Milne, P., 1999. “Tarski, Truth and Model Theory”, *Proceedings of the Aristotelian Society*, 99: 141–67.

[^murawski-1998]: Murawski, R., 1998. “Undefinability of Truth. The Problem of Priority: Tarski vs. Gödel”, *History and Philosophy of Logic*, 19: 153–60.

[^mycielski-2004]: Mycielski, J., 2004. “On the Tension between Tarski’s Nominalism and His Model Theory”, *Annals of Pure and Applied Logic*, 126: 215–24.

[^park-2018]: Park, W., 2018. *Philosophy’s Loss of Logic to Mathematics. An Inadequately Understood Take-Over*, Cham: Springer.

[^patterson-2004]: Patterson, D., 2004. “The Status of Convention T”, in L. Běhounek (ed.), *The Logica Yearbook 2003*, Prague: Filosofia, pp. 195–207.

[^patterson-2008a]: ––– (ed.), 2008a. *New Essays on Tarski and Philosophy*, Oxford: Oxford University Press.

[^patterson-2008b]: –––, 2008b. “Tarski’s Conception of Meaning”, in Patterson 2008a, pp. 157–91.

[^patterson-2012]: –––, 2012. *Alfred Tarski: Philosophy of Language and Logic*, New York: Palgrave Macmillan.

[^putnam-1985]: Putnam, H., 1985. “A Comparison of Something with Something Else”, reprinted in Putnam, *Words and Life*, Cambridge, MA: Harvard University Press, 1994, pp. 330–50.

[^raatikainen-2003]: Raatikainen, P., 2003. “More on Putnam and Tarski”, *Synthese*, 135: 37–47.

[^raatikainen-2008]: –––, 2008. “Truth, Meaning, and Translation”, in Patterson 2008a, pp. 247–62.

[^ray-1996]: Ray, G., 1996. “Logical Consequence: a Defense of Tarski”, *Journal of Philosophical Logic*, 25: 617–77.

[^ray-2003]: –––, 2003. “Tarski and the Metalinguistic Liar”, *Philosophical Studies*, 115: 55–80.

[^ray-2005]: –––, 2005. “On the Matter of Essential Richness”, *Journal of Philosophical Logic*, 34: 433–57.

[^ray-2018]: –––, 2018. “Tarski on the Concept of Truth”, in M. Glanzberg (ed.), *The Oxford Handbook of Truth*, Oxford: Oxford University Press, pp. 695–717.

[^rojszczak-2002]: Rojszczak, A., 2002. “Philosophical Background and Philosophical Content of the Semantic Definition of Truth”, *Erkenntnis*, 56: 29–62.

[^sagi-2015]: Sagi, G., 2015. “The Modal and Epistemic Arguments against the Invariance Criterion for Logical Terms”, *Journal of Philosophy*, 112: 159–67.

[^sagi-2018]: –––, 2018. “Logicality and Meaning”, *Review of Symbolic Logic*, 11: 133–59.

[^sagi-2021]: –––, 2021. “Extensionality and Logicality”, *Synthese*, 198: 1095–1119.

[^sagi-2021-2]: Sagi, G. and J. Woods (eds.), 2021. *The Semantic Conception of Logic. Essays on Consequence, Invariance, and Meaning*, Cambridge: Cambridge University Press.

[^sagüillo-1997]: Sagüillo, J.M., 1997. “Logical Consequence Revisited”, *Bulletin of Symbolic Logic*, 3: 216–241.

[^schiemer-2013]: Schiemer, G. and E. Reck, 2013. “Logic in the 1930s: Type Theory and Model Theory”, *Bulletin of Symbolic Logic*, 19: 433–72.

[^schurz-1999]: Schurz, G., 1999. “Tarski and Carnap on Logical Truth. Or: What is Genuine Logic?”, in Woleński and Köhler 1999, pp. 77–94.

[^shapiro-1998]: Shapiro, S., 1998. “Logical Consequence: Models and Modality”, in M. Schirn (ed.), *The Philosophy of Mathematics Today*, Oxford: Clarendon Press, pp. 131–56.

[^sher-1991]: Sher, G., 1991. *The Bounds of Logic*, Cambridge, MA: MIT Press.

[^sher-1996]: –––, 1996. “Did Tarski Commit ‘Tarski’s Fallacy’?”, *Journal of Symbolic Logic*, 61: 653–86.

[^sher-1999]: –––, 1999. “What Is Tarski’s Theory of Truth?”, *Topoi*, 59: 149–66.

[^sher-2008]: –––, 2008. “Tarski’s Thesis”, in Patterson 2008a, pp. 300–39.

[^sher-2021]: –––, 2021. “Invariance and Logicality in Perspective”, in Sagi and Woods 2021, pp. 13–34.

[^sher-2022]: –––, 2022. *Logical Consequence*, Cambridge: Cambridge University Press.

[^simchen-2020]: Simchen, O., 2020. “Modeling Truth for Semantics”, *Analytic Philosophy*, 61: 28–36.

[^simmons-2009]: Simmons, K., 2009. “Tarski’s Logic”, in D. M. Gabbay and J. Woods (eds.), *Handbook of the History of Logic. Volume 5. Logic from Russell to Church*, Amsterdam: Elsevier, pp. 511–616.

[^simons-1987]: Simons, P., 1987. “Bolzano, Tarski and the Limits of Logic”, *Philosophia Naturalis*, 24: 378–405.

[^simons-2008]: –––, 2008. “Truth on a Tight Budget: Tarski and Nominalism”, in Patterson 2008a, pp. 369–89.

[^sinaceur-2001]: Sinaceur, H., 2001. “Alfred Tarski: Semantic Shift, Heuristic Shift in Metamathematics”, *Synthese*, 126: 49–65.

[^smith-2017]: Smith, N. J. J., 2017. “Truth via Satisfaction?”, in P. Arazim and T. Lávička (eds.), *The Logica Yearbook 2016*, London: College Publications, pp. 273–287.

[^soames-1984]: Soames, S., 1984. “What Is a Theory of Truth?”, *Journal of Philosophy*, 81: 411–29.

[^soames-1999]: –––, 1999. *Understanding Truth*, New York: Oxford University Press.

[^soames-2010]: –––, 2010. *Philosophy of Language*, Princeton, NJ: Princeton University Press.

[^soames-2018]: –––, 2018. *The Analytic Tradition in Philosophy. Volume 2. A New Vision*, Princeton, NJ: Princeton University Press.

[^sundholm-2003]: Sundholm, G., 2003. “Tarski and Leśniewski on Languages with Meaning versus Languages without Use”, in J. Hintikka *et al.* (eds.), *Philosophy and Logic. In Search of the Polish Tradition*, Dordrecht: Kluwer, pp. 109–28.

[^suppes-1988]: Suppes, P., 1988. “Philosophical Implications of Tarski’s Work”, *Journal of Symbolic Logic*, 53: 80–91.

[^vaught-1974]: Vaught, R. L., 1974. “Model Theory before 1945”, in L. Henkin *et al.* (eds.), *Proceedings of the Tarski Symposium*, Proceedings of Symposia in Pure Mathematics, vol. XXV, Providence, RI: American Mathematical Society, pp. 153–72.

[^vaught-1986]: –––, 1986. “Tarski’s Work in Model Theory”, *Journal of Symbolic Logic*, 51: 869–82.

[^woleński-1993]: Woleński, J., 1993. “Tarski as a Philosopher”, in F. Coniglione *et al.* (eds.), *Polish Scientific Philosophy: The Lvov-Warsaw School*, Amsterdam: Rodopi, pp. 319–38.

[^woleński-1999]: –––, 1999. *Essays in the History of Logic and Logical Philosophy*, Cracow: Jagiellonian University Press.

[^woleński-2019]: –––, 2019. *Semantics and Truth*, Cham: Springer.

[^woleński-1999-2]: Woleński, J. and E. Köhler (eds.), 1999. *Alfred Tarski and the Vienna Circle*, Dordrecht: Kluwer.

[^zinke-2018]: Zinke, A., 2018. *The Metaphysics of Logical Consequence*, Frankfurt: Klostermann.
