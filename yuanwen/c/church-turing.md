# The Church-Turing Thesis
**First published Wed Jan 8, 1997; substantive revision Mon Dec 18, 2023**

*Copeland, B. Jack*

The Church-Turing thesis (or Turing-Church thesis) is a fundamental claim in the theory of computability. It was advanced independently by Church and Turing in the mid 1930s. There are various equivalent formulations of the thesis. A common one is that every effective computation can be carried out by a Turing machine (i.e., by Turing’s abstract computing machine, which in its universal form encapsulates the fundamental logical principles of the stored-program all-purpose digital computer). Modern reimaginings of the Church-Turing thesis transform it, extending it to fundamental physics, complexity theory, exotic algorithms, and cognitive science. It is important to be aware though that some of the theses nowadays referred to as the Church-Turing thesis are at best *very* distant relatives of the thesis advanced by Church and Turing.

## 1. The 1936 Thesis and its Context

The Church-Turing thesis concerns the concept of an *effective* or *systematic* or *mechanical* method, as used in logic, mathematics and computer science. “Effective” and its synonyms “systematic” and “mechanical” are terms of art in these disciplines: they do not carry their everyday meaning. A method, or procedure, $M$, for achieving some desired result is called “effective” (or “systematic” or “mechanical”) just in case:

1. $M$ is set out in terms of a finite number of exact instructions (each instruction being expressed by means of a finite number of symbols);
2. $M$ will, if carried out without error, produce the desired result in a finite number of steps;
3. $M$ can (in practice or in principle) be carried out by a human being unaided by any machinery except paper and pencil;
4. $M$ demands no insight, intuition, or ingenuity, on the part of the human being carrying out the method.

A well-known example of an effective method is the truth-table test for tautologousness. In principle, a human being who works by rote could apply this test successfully to any formula of the propositional calculus—given sufficient time, tenacity, paper, and pencils (although in practice the test is unworkable for any formula containing more than a few propositional variables).

### 1.1 Note on terminology

Statements that there is an effective method for achieving such-and-such a result are commonly expressed by saying that there is an effective method for obtaining the values of such-and-such a mathematical *function*.

For example, that there is an effective method for determining whether or not any given formula of the propositional calculus is a tautology (such as the truth-table method) is expressed in function-speak by saying there is an effective method for obtaining the values of a function, call it $T$, whose domain is the set of formulae of the propositional calculus and whose value for any given formula $x$, written $T(x)$, is 1 or 0 according to whether $x$ is, or is not, a tautology.

### 1.2 Making the informal concept of an effective method precise

The notion of an effective method or procedure is an informal one, and attempts to characterize effectiveness, such as the above, lack rigor, for the key requirement that the method must demand no insight, intuition or ingenuity is left unexplicated.

One of Alan Turing’s achievements, in his famous paper of 1936, was to present a formally exact predicate with which the informal predicate “can be done by means of an effective method” may be replaced (Turing 1936)[^turing-1936]. Alonzo Church, working independently, did the same (Church 1936a)[^church-1936a].

The replacement predicates that Church and Turing proposed were, on the face of it, very different from one another. However, these predicates turned out to be *equivalent*, in the sense that each picks out the same set (call it $S$) of mathematical functions. The Church-Turing thesis is the assertion that this set $S$ contains *every* function whose values can be obtained by a method or procedure satisfying the above conditions for effectiveness.

Since it can also be shown that there are no functions in $S$ *other than* ones whose values can be obtained by a method satisfying the above conditions for effectiveness, the Church-Turing thesis licenses replacing the informal claim “There is an effective method for obtaining the values of function $f$” by the formal claim “$f$ is a member of $S$”—or by any other formal claim equivalent to this one.

When the Church-Turing thesis is expressed in terms of the replacement concept proposed by Turing, it is appropriate to refer to the thesis also as “Turing’s thesis”; and as “Church’s thesis” when expressed in terms of one or another of the formal replacements proposed by Church.

The formal concept proposed by Turing was that of *computability by Turing machine*. He argued for the claim—Turing’s thesis—that whenever there is an effective method for obtaining the values of a mathematical function, the function can be computed by a Turing machine.

The converse claim—amounting to the claim mentioned above, that there are no functions in $S$ *other than* ones whose values can be obtained by an effective method—is easily established, since a Turing machine program is itself a specification of an effective method. Without exercising any insight, intuition, or ingenuity, a human being can work through the instructions in the program and carry out the required operations.

If Turing’s thesis is correct, then talk about the existence and non-existence of effective methods and procedures can be replaced throughout mathematics, logic and computer science by talk about the existence or non-existence of Turing machine programs.

Turing stated his thesis in numerous places, with varying degrees of rigor. The following formulation is one of the most accessible:

> **Turing’s thesis**:
> L.C.M.s [logical computing machines: Turing’s expression for Turing machines] can do anything that could be described as “rule of thumb” or “purely mechanical”. (Turing 1948 [2004: 414])[^turing-1948]

He adds:

> This is sufficiently well established that it is now agreed amongst logicians that “calculable by means of an L.C.M.” is the correct accurate rendering of such phrases. (Ibid.)

### 1.3 Formulations of Turing’s thesis in terms of numbers

In his 1936 paper, which he titled “On Computable Numbers, with an Application to the *Entscheidungsproblem*”, Turing wrote:

> Although the subject of this paper is ostensibly the computable numbers, it is almost equally easy to define and investigate computable functions … I have chosen the computable numbers for explicit treatment as involving the least cumbrous technique. (1936 [2004: 58])

Computable numbers are (real) numbers whose decimal representation can be generated progressively, digit by digit, by a Turing machine. Examples are:

- any number whose decimal representation consists of a finite number of digits (e.g., 109, 1.142)
- all rational numbers, such as one-third, two-sevenths, etc.
- some irrational real numbers, such as π and e.

Some real numbers, though, are *un*computable, as Turing proved. Turing’s proof pointed to specific examples of uncomputable real numbers, but it is easy to see in a general way that there *must* be real numbers that cannot be computed by any Turing machine, since there are *more* real numbers than there are Turing-machine programs. There can be no more Turing-machine programs than there are whole numbers, since the programs can be counted: 1ˢᵗ program, 2ⁿᵈ program, and so on; but, as Cantor proved in 1874, there are vastly more real numbers than whole numbers (Cantor 1874)[^cantor-1874].

As Turing said, “it is almost equally easy to define and investigate computable functions”: There is, in a certain sense, little difference between a computable number and a computable function. For example, the computable number .14159… (formed of the digits following the decimal point in π, 3.14159…) corresponds to the computable function: $f(1) = 1,$ $f(2) = 4,$ $f(3) = 1,$ $f(4) = 5,$ $f(5) = 9,$… .

As well as formulations of Turing’s thesis like the one given above, Turing also formulated his thesis in terms of numbers:

> [T]he “computable numbers” include all numbers which would naturally be regarded as computable. (Turing 1936 [2004: 58])[^turing-1936]

and

> It is my contention that these operations [the operations of an L.C.M.] include all those which are used in the computation of a number. (Turing 1936 [2004: 60])[^turing-1936]

In the first of these two formulations, Turing is stating that every number which is able to be calculated by an effective method (that is, “all numbers which would naturally be regarded as computable”) is included among the numbers whose decimal representations can be written out progressively by one or another Turing machine. In the second, Turing is saying that the operations of a Turing machine include all those that a human mathematician needs to use when calculating a number by means of an effective method.

### 1.4 The meaning of “computable” and “computation” in Turing’s thesis

Turing introduced his machines with the intention of providing an idealized description of a certain human activity, the tedious one of *numerical computation*. Until the advent of automatic computing machines, this was the occupation of many thousands of people in business, government, and research establishments. These human rote-workers were in fact called “computers”. Human computers used effective methods to carry out some aspects of the work nowadays done by electronic computers. The Church-Turing thesis is about computation *as this term was used in 1936*, viz. human computation (to read more on this, turn to Section 7).

For instance, when Turing says that the operations of an L.C.M. include all those needed “in the computation of a number”, he means “in the computation of a number by a human being”, since that is what computation was in those days. Similarly, “numbers which would naturally be regarded as computable” are numbers that would be regarded as being computable by a human computer, a human being who is working solely in accordance with an effective method.

### 1.5 Church’s thesis

Where Turing used the term “purely mechanical”, Church used “effectively calculable” to indicate that there is an effective method for obtaining the values of the function; and where Turing offered an analysis in terms of computability by an L.C.M., Church gave two alternative analyses, one in terms of the concept of *recursion* and the other in terms of *lambda-definability* (λ-definability). He proposed that we

> define the notion … of an effectively calculable function of positive integers by identifying it with the notion of a recursive function of positive integers (or of a λ-definable function of positive integers). (Church 1936a: 356)[^church-1936a]

The concept of a λ-definable function was due to Church and Kleene, with contributions also by Rosser (Church 1932, 1933, 1935c, 1936a; Church & Rosser 1936; Kleene 1934, 1935a,b, 1936a,b; Kleene & Rosser 1935; Rosser 1935a,b)[^church-1932][^church-1933][^church-1935c][^church-1936a][^church-1936][^kleene-1934][^kleene-1935a][^kleene-1936a][^kleene-1935][^rosser-1935a]. A function is said to be λ-definable if the values of the function can be obtained by a certain process of repeated substitution. The concept of a recursive function had emerged over time through the work of, among others, Grassmann, Peirce, Dedekind, Peano, Skolem, Hilbert—and his “assistants” Ackermann and Bernays—Sudan, Péter (née Politzer), Herbrand, Kleene, and pre-eminently Gödel (Gödel 1931, 1934)[^gödel-1931][^gödel-1934]. The class of λ-definable functions (of positive integers) and the class of recursive functions (of positive integers) are identical; this was proved by Church and Kleene (Church 1936a; Kleene 1936a,b)[^church-1936a][^kleene-1936a].

When Turing learned of Church’s 1936 proposal to identify effectiveness with λ-definability (while preparing his own paper for publication), he quickly established that the concept of λ-definability and his concept of computability are equivalent (by proving the “theorem that all … λ-definable sequences … are computable” and its converse; Turing 1936 [2004: 88ff])[^turing-1936]. Thus, in Church’s proposal, the words “λ-definable function of positive integers” (and equally the words “recursive function of positive integers”) can be replaced by “function of positive integers that is computable by Turing machine”. What Turing proved is called an *equivalence result*. There is further discussion of equivalence results in Section 4.1.

Post referred to Church’s identification of effective calculability with recursiveness and λ-definability as a “working hypothesis”, and he quite properly criticized Church for masking this hypothesis as a *definition*:

> [T]o mask this identification under a definition … blinds us to the need of its continual verification. (Post 1936: 105)[^post-1936]

This, then, is the “working hypothesis” that, in effect, Church proposed:

> **Church’s thesis**:
> A function of positive integers is effectively calculable only if λ-definable (or, equivalently, recursive).

The reverse implication, that every λ-definable function of positive integers is effectively calculable, is commonly referred to as *the converse of Church’s thesis,* although Church himself did not so distinguish (bundling both theses together in his “definition”).

If attention is restricted to functions of positive integers, Church’s thesis and Turing’s thesis are *extensionally* equivalent. “Extensionally equivalent” means that the two theses are about one and the same class of functions: In view of the previously mentioned results by Church, Kleene and Turing, the class of λ-definable functions (of positive integers) is identical to the class of recursive functions (of positive integers) and to the class of computable functions (of positive integers). Notice, though, that while the two theses are equivalent in this sense, they nevertheless have distinct *meanings* and so are two *different* theses. One important difference between the two is that Turing’s thesis concerns *computing machines*, whereas Church’s does not.

Concerning the origin of the terms “Church’s thesis” and “Turing’s thesis”, Kleene seems to have been the first to use the word “thesis” in this connection: In 1952, he introduced the name “Church’s thesis” for the proposition that every effectively calculable function (on the natural numbers) is recursive (Kleene 1952: 300, 301, 317)[^kleene-1952]. The term “Church-Turing thesis” also seems to have originated with Kleene—with a flourish of bias in favor of his mentor Church:

> So Turing’s and Church’s theses are equivalent. We shall usually refer to them both as *Church’s thesis*, or in connection with that one of its … versions which deals with “Turing machines” as the *Church-Turing thesis*. (Kleene 1967: 232)[^kleene-1967]

Some prefer the name *Turing-Church thesis*.

### 1.6 Comparing the Turing and Church approaches

One way in which Turing’s and Church’s approaches differed was that Turing’s concerns were rather more general than Church’s, in that (as just mentioned) Church considered only functions of positive integers, whereas Turing described his work as encompassing “computable functions of an integral variable or a real or computable variable, computable predicates, and so forth” (1936 [2004: 58]). Turing intended to pursue the theory of computable functions of a real variable in a subsequent paper, but in fact did not do so.

A greater difference lay in the profound significance of Turing’s approach for the emerging science of automatic computation. Church’s approach did not mention computing machinery, whereas Turing’s introduced the “Turing machine” (as Church dubbed it in his 1937a review of Turing’s 1936 paper)[^church-1937a][^church-1936][^turing-1936]. Turing’s paper also introduced what he called the “universal computing machine”. Now known as the universal Turing machine, this is Turing’s all-purpose computing machine. The universal machine is able to emulate the behavior of any single-purpose Turing machine, i.e., any Turing machine set up to solve one particular problem. The universal machine does this by means of storing a description of the other machine on its tape, in the form of a finite list of instructions (a computer program, in modern terms). By following suitable instructions, the universal machine can carry out any and every effective procedure, assuming Turing’s thesis is true. The functional parts of the abstract universal machine are:

1. the memory in which instructions and data are stored, and
2. the instruction-reading-and-obeying control mechanism.

In that respect, the universal Turing machine is a bare-bones logical model of almost every modern electronic digital computer.

In his review of Turing’s work, Church noted an advantage of Turing’s analysis of effectiveness over his own:

> computability by a Turing machine … has the advantage of making the identification with effectiveness in the ordinary (not explicitly defined) sense evident immediately. (Church 1937a: 43)[^church-1937a]

He also said that Turing’s analysis has “a more immediate intuitive appeal” than his own (Church 1941: 41)[^church-1941].

Gödel found Turing’s analysis superior to Church’s. Kleene related that Gödel was unpersuaded by Church’s thesis until he saw Turing’s formulation:

> According to a November 29, 1935, letter from Church to me, Gödel “regarded as thoroughly unsatisfactory” Church’s proposal to use λ-definability as a definition of effective calculability. … It seems that only after Turing’s formulation appeared did Gödel accept Church’s thesis. (Kleene 1981: 59, 61)[^kleene-1981]

Gödel described Turing’s analysis of computability as “most satisfactory” and “correct … beyond any doubt” (Gödel 1951: 304 and 193?: 168)[^gödel-1951]. He remarked:

> We had not perceived the sharp concept of mechanical procedures sharply before Turing, who brought us to the right perspective. (Quoted in Wang 1974: 85)[^wang-1974]

Gödel also said:

> The resulting definition of the concept of mechanical by the sharp concept of “performable by a Turing machine” is both correct and unique. (Quoted in Wang 1996: 203)[^wang-1996]

And:

> Moreover it is absolutely impossible that anybody who understands the question and knows Turing’s definition should decide for a different concept. (Ibid.)

Even the modest young Turing agreed that his analysis was “possibly more convincing” than Church’s (Turing 1937: 153)[^turing-1937].

### 1.7 The *Entscheidungsproblem*

Both Turing and Church introduced their respective versions of the Church-Turing thesis in the course of attacking the so-called *Entscheidungsproblem*. As already mentioned, the title of Turing’s 1936 paper included “with an Application to the *Entscheidungsproblem*”, and Church went with simply “A Note on the *Entscheidungsproblem*” for the title of his 1936 paper. So—what is the *Entscheidungsproblem*?

The German word “*Entscheidungsproblem*” means *decision problem*. The *Entscheidungsproblem* for a logical calculus is the problem of devising an effective method for deciding whether or not a given formula—any formula—is provable in the calculus. (Here “provable” means that the formula can be derived, step by logical step, from the axioms and definitions of the calculus, using only the rules of the calculus.) For example, if such a method for the classical propositional calculus is used to test the formula $A \rightarrow A$ ($A$ implies $A$), the output will be “Yes, provable”, and if the contradiction $A \amp \neg A$ is tested, the output will be “Not provable”. Such a method is called a *decision method* or *decision procedure*.

Church and Turing took on the *Entscheidungsproblem* for a fundamentally important logical system called the (first-order) *functional calculus*. The functional calculus consists of standard propositional logic plus standard quantifier logic. The functional calculus is also known as the *classical predicate calculus* and as *quantification theory* (and Church sometimes used the German term *engere Funktionenkalkül*). They each arrived at the same negative result, arguing on the basis of the Church-Turing thesis that, in the case of the functional calculus, the *Entscheidungsproblem* is *unsolvable*—there can be *no* decision method for the calculus. The two discovered this result independently of one another, both publishing it in 1936 (Church a few months earlier than Turing). Church’s proof, which made no reference to computing machines, is for that reason sometimes considered to be of less interest than Turing’s.

The *Entscheidungsproblem* had attracted some of the finest minds of early twentieth-century mathematical logic, including Gödel, Herbrand, Post, Ramsey, and Hilbert and his assistants Ackermann, Behmann, Bernays, and Schönfinkel. Herbrand described the *Entscheidungsproblem* as “the most general problem of mathematics” (Herbrand 1931b: 187)[^herbrand-1931b]. But it was Hilbert who had brought the *Entscheidungsproblem* for the functional calculus into the limelight. In 1928, he and Ackermann called it “das Hauptproblem der mathematischen Logik”—“the main problem of mathematical logic” (Hilbert & Ackermann 1928: 77)[^ackermann-1928][^hilbert-1928].

Hilbert knew that the propositional calculus (which is a fragment of the functional calculus) is decidable, having found with Bernays a decision procedure based on what are called “normal forms” (Bernays 1918; Behmann 1922; Hilbert & Ackermann 1928: 9–12; Zach 1999)[^ackermann-1928][^behmann-1922][^bernays-1918][^hilbert-1928][^zach-1999], and he also knew from the work of Löwenheim that the *monadic* functional calculus is decidable (Löwenheim 1915)[^löwenheim-1915]. (The monadic functional calculus is the fragment involving only one-place predicates—i.e., no relations, such as “=” and “<”, and no higher-place predicates, such as “– is between – and –”.) He thought there must be a decision procedure for the entire functional calculus. The challenge, the main problem of mathematical logic, was to find it. As he and Ackermann wrote in 1928, in their famous book *Grundzüge der Theoretischen Logik* (Principles of Mathematical Logic):

> [I]t is to be expected that a systematic, so to speak computational treatment of the logical formulae is possible …. (Hilbert & Ackermann 1928: 72)[^ackermann-1928][^hilbert-1928]

However, their expectations were frustrated by the Church-Turing result of 1936. Hilbert and Ackermann excised the quoted statement from a revised edition of their book. Published in 1938, the new edition was considerably watered down to take account of Turing’s and Church’s monumental result.

Hilbert knew, of course, that some mathematical problems have *no* solution, for example the problem of finding a finite binary numeral $n$ (or unary numeral, in Hilbert’s version of the problem) such that $n^2 = 2$ (Hilbert 1926: 179)[^hilbert-1926]. He was nevertheless very fond of saying that *every mathematical problem can be solved*, and by this he meant that

> every definite mathematical problem must necessarily be susceptible of an exact settlement, either in the form of an actual answer to the question asked, or by the proof of the impossibility of its solution and therewith the necessary failure of all attempts. (Hilbert 1900: 261 [trans. 1902: 444])[^hilbert-1900]

It seems never to have crossed his mind that his “Hauptproblem der mathematischen Logik” falls into the second of these two categories—until, that is, Church and Turing unexpectedly proved “the impossibility of its solution”.

For more detail on the *Entscheidungsproblem*, and an outline of the stunning result that Church and Turing independently established in 1936, see the supplement on [The Rise and Fall of the *Entscheidungsproblem*](church-turing.decision-problem.md).

## 2. Backstory: Emergence of the concepts of *effective method* and *decision method*

Effective methods are the subject matter of the Church-Turing thesis. How did this subject matter evolve and how was it elaborated prior to Church and Turing? This section looks back to an earlier era, after which Section 3 turns to modern developments.

### 2.1 From simple rules-of-thumb to Siri and beyond

Effective methods are extremely helpful in carrying out many practical tasks, and their use stretches back into the mists of antiquity, although it was not until the twentieth century that interest began to build in analysing their nature. Perhaps the earliest effective methods to be utilized were rules-of-thumb (as Turing called them) for arithmetical calculations of various sorts, but whatever their humble beginnings, the scope of effective methods has widened dramatically over the centuries. In the Middle Ages, the Catalan philosopher Llull envisaged an effective method for posing and answering questions about the attributes of God, the nature of the soul, the nature of goodness, and other fundamental issues. Three hundred years later, in the seventeenth century, Hobbes was asserting that human reasoning processes amount to nothing more than (essentially arithmetical) effective procedures:

> By reasoning I understand computation. (Hobbes 1655 [1839]: ch. 1 sect. 2)[^hobbes-1655]

Nowadays, effective methods—algorithms—are the basis for every job that electronic computers do. According to some computer scientists, advances in the design of effective methods will soon usher in human-level artificial intelligence, followed by superhuman intelligence. Already, virtual assistants such as Siri, Cortana and ChatGPT implement effective methods that produce useful answers to a wide range of questions.

In its most sublimely general form, the *Entscheidungsproblem* is the problem of designing an effective general-purpose question-answerer, an effective method that is capable of giving the correct answer, yes or no, to *any* meaningful scientific question, and perhaps even ethical and metaphysical questions too. The idea of such a method is almost jaw-dropping. Llull seems to have glimpsed the concept of a general question-answering method, writing in approximately 1300 of a general art (“*ars*”), or technique, “by means of which one may know in regard to all natural things” (*Lo Desconhort*, line 8, in Llull 1986: 99)[^llull-1986]. He dreamed of an *ars generalis* (general technique) that could mechanize the “one general science, with its own general principles in which the principles of other sciences would be implicit” (Preface to *Ars Generalis Ultima*, in Llull 1645 [1970: 1])[^llull-1645]. Llull used circumscribed fields of knowledge to illustrate his idea of a mechanical question-answerer, designing small domain-specific machines consisting of superimposed discs; possibly his machines took the form of a parchment *volvelle*, a relative of the metal astrolabe.

In early modern times, Llull’s idea of the *ars generalis* received a sympathetic discussion in Leibniz’s writings.

### 2.2 Leibniz

Leibniz designed a calculating machine that he said would add, subtract, multiply and divide, and in 1673 he demonstrated a version of his machine in London and Paris (Leibniz 1710)[^leibniz-1710]. His interest in mechanical methods led him to an even grander conception, inspired in part by Llull’s unclear but provocative speculations about a general-purpose question-answering mechanism. Leibniz said that Llull “had scraped the skin off” this idea, but “did not see its inmost parts” (Leibniz 1671 [1926: 160])[^leibniz-1671]. Leibniz envisaged a method, just as mechanical as multiplication or division, whereby

> when there are disputes among persons, we can simply say: Let us calculate, without further ado, in order to see who is right. (Leibniz 1685 [1951: 51])[^leibniz-1685]

The basis of the method, Leibniz explained, was that “we can represent all sorts of truths and consequences by Numbers” and “then all the results of reasoning can be determined in numerical fashion” (Leibniz 1685 [1951: 50–51])[^leibniz-1685]. He hoped the method would apply to “Metaphysics, Physics, and Ethics” just as well as it did to mathematics (1685 [1951: 50]). This conjectured method could, he thought, be implemented by what he called a *machina combinatoria*, a combinatorial machine (Leibniz *n.d.*1; Leibniz 1666)[^leibniz-1666]. However, there was never much progress towards his dreamed-of method, and in a letter two years before his death he wrote:

> [I]f I were younger or had talented young men to help me, I should still hope to create a kind of universal symbolistic [*spécieuse générale*] in which all truths of reason would be reduced to a kind of calculus. (Leibniz 1714 [1969: 654])[^leibniz-1714]

In his theorizing Leibniz described what he called an *ars inveniendi*, a discovering or devising method. The function of an *ars inveniendi* is to produce hitherto unknown truths of science (Leibniz 1679 [1903: 37]; Leibniz *n.d.*2 [1890: 180]; Hermes 1969)[^hermes-1969][^leibniz-1679]. A mechanical *ars inveniendi* would generate true statements, and with time the awaited answer to a scientific question would arrive (Leibniz 1671 [1926: 160])[^leibniz-1671]. Blessed with a universal (i.e., complete, and consistent) *ars inveniendi*, the user could input *any* meaningful and unambiguous (scientific or mathematical) statement $S$, and the machine would eventually respond (correctly) with either “$S$ is true” or “$S$ is false”. As the groundbreaking developments in 1936 by Church and Turing made clear, if the *ars inveniendi* is supposed to work by means of an effective method, then there can be no universal *ars inveniendi*—and not even an *ars inveniendi* that is restricted to all mathematical statements, since these include statements of the form “$p$ is provable”, or even to all purely logical statements.

### 2.3 Logic machines

The modern concept of a decision method for a logical calculus did not develop until the twentieth century. But earlier logicians, including Leibniz, certainly had the concept of a method that is *mechanical* in the literal sense that it could be carried out by a machine constructed from mechanical components of the sort familiar to them—discs, pins, rods, springs, levers, pulleys, rotating shafts, gear wheels, weights, dials, mechanical switches, slotted plates, and so forth.

In 1869, Jevons designed a pioneering machine known as the “logic piano” (Jevons 1870; Barrett & Connell 2005)[^barrett-2005][^jevons-1870]. The name arose because of the machine’s piano-like keyboard for inputting logical formulae. The formulae were drawn from a syllogistic calculus involving four positive terms, such as “iron” and “metal” (Jevons 1870)[^jevons-1870]. Turing’s colleague Mays, who himself designed an influential electrical logic machine (Mays & Prinz 1950)[^mays-1950], described the logic piano as “the first working machine to perform logical inference without the intervention of human agency” (Mays & Henry 1951: 4)[^mays-1951].

The logic piano implemented a method for determining which combinations drawn from eight terms—the four positive terms and the corresponding four negated terms (“non-metal”, etc.)—were consistent with the inputted formulae and which not (although in fact not all consistent combinations were taken into account). The machine displayed the consistent formulae by means of lettered strips of wood, with upper-case letters representing positive terms and lower-case negative. Jevons exhibited the logic piano in Manchester at Owens College, now Manchester University, where he was professor of logic (Mays & Henry 1953: 503)[^mays-1953]. His piano, Jevons claimed with considerable exaggeration, made it “evident that mechanism is capable of replacing for the most part the action of thought required in the performance of logical deduction” (Jevons 1870: 517)[^jevons-1870].

A decade later, Venn published the technique we now call *Venn diagrams* (Venn 1880)[^venn-1880]. This technique satisfies the four criteria set out for an effective method in Section 1. The user first diagrams the premisses of a syllogism and then, as Quine put it, “we inspect the diagram to see whether the content of the conclusion has automatically appeared in the diagram as a result” (Quine 1950: 74)[^quine-1950]. Not all formulae of the functional calculus are Venn-diagrammable, and Venn’s original method is limited to testing syllogisms. In the twentieth century, Massey showed that Venn’s method can be stretched to give a decision procedure for the monadic functional calculus (Massey 1966)[^massey-1966].

Venn, like Jevons, was well aware of the concept of a literally mechanical method. He pointed out that diagrammatic methods such as his “readily lend themselves to mechanical performance” (Venn 1880: 15)[^venn-1880]. Venn went on to describe what he called a “logical-diagram machine”. This simple machine displayed wooden segments corresponding to the component areas of a Venn diagram; each wooden segment represented one of four terms. A finger-operated release mechanism allowed any segment selected by the user to drop downwards. This represented “the destruction of any class” (1880: 18). Venn reported that he constructed this machine, which measured “between five and six inches square and three inches deep” (1880: 17). When Venn published his description of it, Jevons quickly wrote to him saying that the logical-diagram machine “is exceedingly ingenious & seems to represent the relations of four terms very well” (Jevons 1880)[^jevons-1880]. Venn himself however was less enthusiastic, saying in his article “I have no high estimate myself of the interest or importance of what are sometimes called logical machines” (1880: 15). Baldwin, commenting on Venn’s machine in 1902, complained that it was “merely a more cumbersome diagram” (1902: 29). This is quite true—it would be at least as easy to draw the Venn diagram on paper as to set it up on the machine. But Venn’s article made it very plain that the logical-diagram machine was intended to be a hilarious send-up of Jevons’ complicated logic piano.

At around the same time, Marquand—a student of Peirce’s—designed a logic machine which a Princeton colleague then built (out of wood salvaged from “Princeton’s oldest homestead”, Marquand related in his 1885)[^marquand-1885]. Marquand knew of Jevons’ and Venn’s designs, and said he had “followed Jevons” in certain respects, and that his own machine was “somewhat similar” to Jevons’ (Marquand 1881, 1883: 16, 1885: 303)[^marquand-1881][^marquand-1883][^marquand-1885]. Peirce, with customary bluntness, called Marquand’s machine “a vastly more clear-headed contrivance than that of Jevons” (Peirce 1887: 166)[^peirce-1887]. Again limited to a syllogistic calculus involving only four positive terms, Marquand’s device, like Jevons’, displayed term-combinations consistent with the inputted formulae. A lettered plate with sixteen mechanical dials was used to display the combinations.

### 2.4 Peirce

In 1886, in a letter to Marquand, Peirce famously suggested that Marquand consider an electrical version of his machine, and he sketched simple switching circuits implementing (what we would now call) an AND-gate and an OR-gate—possibly the earliest proposal for electrical computation (Peirce 1886)[^peirce-1886]. Far-sightedly, Peirce wrote in the letter that, with the use of electricity, “it is by no means hopeless to expect to make a machine for really very difficult mathematical problems”. Much later, Church discovered a detailed diagram of an electrical relay-based form of Marquand’s machine among Marquand’s papers at Princeton (reproduced in Ketner & Stewart 1984: 200)[^ketner-1984]. Whoever worked out the design in this diagram—Marquand, Peirce, or an unknown third person—has a claim to be an important early pioneer of electromechanical computing.

Peirce, with his interest in logic machines, seems to have been the first to consider the decision problem in roughly the form in which Turing and Church tackled it. From about 1896, he developed the diagrammatic proof procedures he called “existential graphs”. These were much more advanced than Venn’s diagrams. Peirce’s system of *alpha-graphs* is a diagrammatic formulation of the propositional calculus, and his system of *beta-graphs* is a version of the first-order functional calculus (Peirce 1903a; Roberts 1973)[^peirce-1903a][^roberts-1973]. Roberts (1973)[^roberts-1973] proved that the beta-graphs system contains the axioms and rules of Quine’s 1951 formulation of the first-order functional calculus, in which only closed formulae are asserted (Quine 1951: 88)[^quine-1951].

Peirce anticipated the concept of a decision method in his extensive notes for a series of lectures he delivered in Boston in 1903. There he developed a method (Peirce 1903b,c)[^peirce-1903b] that, if applied to any given formula of the propositional calculus, would, he said, “determine” (or “positively ascertain”) whether the alpha-graphs system demonstrates that the formula is satisfiable (is “alpha-possible”, in Peirce’s terminology), or whether, on the other hand, the system demonstrates that it is unsatisfiable (“alpha-impossible”). (See the supplement on [The Rise and Fall of the *Entschedungsproblem*](church-turing.decision-problem.md) for an explanation of “satisfiable”.) Peirce said his method “is such a comprehensive routine that it would be easy to define a machine that would perform it”—although the “complexity of the case”, he continued, “renders any such procedure quite impracticable” (Peirce 1903c)[^peirce-1903c]. Perhaps he would not have been completely surprised to learn that within five or six decades, and with the use of electricity, it became far from impractical to run a decision method for the propositional calculus on a machine.

Peirce also searched—in vain, of course—for a corresponding method for his beta-graphs system (Peirce 1903b,c,d; Roberts 1997)[^peirce-1903b][^roberts-1997]. Like Hilbert after him, he seems to have entertained no doubt that full first-order predicate logic is amenable to a machine-like method.

Peirce had prescient ideas about the use of machines in mathematics more generally. Around the turn of the century, he wrote:

> [T]he whole science of higher arithmetic, with its hundreds of marvellous theorems, has in fact been deduced from six primary assumptions about number. The logical machines hitherto constructed are inadequate to the performance of mathematical deductions. There is, however, a modern Exact Logic which, although yet in its infancy, is already far enough advanced to render it a mere question of expense to construct a machine that would grind out all the known theorems of arithmetic and advance that science still more rapidly than it is now progressing. (Peirce *n.d.*, quoted in Stjernfelt 2022)[^stjernfelt-2022]

Here Peirce seems to be asserting—quite correctly—that a machine can be devised to grind out all the theorems of Dedekind’s (1888)[^dedekind-1888] axiomatisation of arithmetic (which consisted of six “primary assumptions” in the form of of four axioms and two definitions). This statement of Peirce’s, made almost four decades before Turing introduced Turing machines into mathematics, was well ahead of its time.

As to whether *all* mathematical reasoning can be performed by a machine, as Leibniz seems to have thought, Peirce was fiercely skeptical. He formulated the hypothesis that, in the future, mathematical reasoning

> might conceivably be left to a machine—some Babbage’s analytical engine or some logical machine. (Peirce 1908: 434)[^peirce-1908]

However, he placed this hypothesis alongside others he deemed “logical heresies”, calling it “malignant” (ibid.). His skeptical attitude, if perhaps not his reasons for it, was arguably vindicated by Turing’s subsequent results (Turing 1936, 1939)[^turing-1936][^turing-1939]. But before that, a quite different view of matters took root among mathematicians, under the influence of Hilbert and his group at Göttingen.

### 2.5 Hilbert and the Göttingen group

It was largely Hilbert who first drew attention to the need for a precise analysis of the idea of an effective decision method. In a lecture he gave in Zurich in 1917, to the Swiss Mathematical Society, he emphasized the need to study the concept of “decidability by a finite number of operations”, saying—accurately—that this would be “an important new field of research to develop” (Hilbert 1917: 415)[^hilbert-1917]. The lecture considered a number of what he called “most challenging epistemological problems of a specifically mathematical character” (1917: 412). Pre-eminent among these was the “problem of the decidability [*Entscheidbarkeit*] of a mathematical question” because the problem “touches profoundly upon the nature of mathematical thinking” (1917: 413).

Hilbert and his Göttingen group looked back on Leibniz as the originator of their approach to logic and the foundations of mathematics. Behmann, a prominent member of the group, said that Leibniz had anticipated modern symbolic logic (Behmann 1921: 4–5)[^behmann-1921]. Leibniz’s hypothesized “universal characteristic” or universal symbolistic was a universal symbolic language, in conception akin to languages used in mathematical logic and computer science today. Hilbert and Ackermann acknowledged Leibniz’s influence on the first page of their *Grundzüge der Theoretischen Logik*, saying “The idea of a mathematical logic was first put into a clear form by Leibniz” (Hilbert & Ackermann 1928: 1)[^ackermann-1928][^hilbert-1928]. Cassirer said that in Hilbert’s work “the fundamental idea of Leibniz’s ‘universal characteristic’ is taken up anew and attains a succinct and precise expression” (Cassirer 1929: 440)[^cassirer-1929]. It was in the writings of the Göttingen group that Leibniz’s idea of an effective method for answering any specified mathematical or scientific question found its fullest development (see further the supplement on [The Rise and Fall of the *Entscheidungsproblem*](church-turing.decision-problem.md)).

Hilbert’s earliest publication to mention what we would now call a decision problem is his 1899 book *Grundlagen der Geometrie* [Foundations of Geometry]. He said that in the course of his investigations of Euclidean geometry he was

> guided by the principle of discussing each given question in such a way that we examined both whether it can or cannot be answered by means of prescribed steps using certain limited resources. (Hilbert 1899: 89)[^hilbert-1899]

Concerning a specific example, he wrote:

> Suppose a geometrical construction problem that can be carried out with a compass is presented; we will attempt to lay down a criterion that enables us to determine [*beurteilen*] immediately, from the analytical nature of the problem and its solutions, whether the construction can also be carried out using only a ruler and a segment-transferrer. (Hilbert 1899: 85–86)[^hilbert-1899]

He described what would now be called an effective method for determining this, and his term “*beurteilen*” could, with a trace of anachronism, be translated as “decide”.

Hilbert expressed the concept of a decision method more clearly the following year, in his famous turn-of-the-century speech in Paris, to the International Congress of Mathematicians. He presented twenty-three unsolved problems, “from the discussion of which an advancement of science may be expected”. The tenth on his list (now known universally as Hilbert’s Tenth Problem) was:

> Given a diophantine equation with any number of unknown quantities and with rational integral numerical coefficients: *To devise a process according to which it can be determined by a finite number of operations whether the equation is solvable in rational integers*. (Hilbert 1900: 276 [trans. 1902: 458])[^hilbert-1900]

The *Entscheidungsproblem* was coming into even clearer focus by the time Hilbert’s student Behmann published a landmark article in 1922, “Contributions to the Algebra of Logic, in particular to the *Entscheidungsproblem*”. It was probably Behmann who coined the term “*Entscheidungsproblem*” (Mancosu & Zach 2015: 166–167)[^mancosu-2015]. In a 1921 lecture to the Göttingen group, Behmann said:

> If a logical or mathematical statement is given, the required procedure should give complete instructions for determining whether the statement is correct or false by a deterministic calculation after finitely many steps. The problem thus formulated I want to call the *allgemeine Entscheidungsproblem* [general decision problem]. (Behmann 1921: 6 [trans. 2015: 176])[^behmann-1921]

Peirce, as we saw, spoke of a procedure’s forming “such a comprehensive routine that it would be easy to define a machine that would perform it”. His work was well-known in Göttingen: Hilbert and Ackermann said that Peirce “especially”, and also Jevons, had “enriched the young science” of mathematical logic (1928: 1). Like Peirce, Behmann used the concept of a machine to clarify the nature of the *Entscheidungsproblem*. “It is essential to the character” of the problem, Behmann said, that “only entirely mechanical calculation according to given instructions” is involved. The decision whether the statement is true or false becomes “a mere exercise in computation”; there is “an elimination of thinking in favor of mechanical calculation”. Behmann continued:

> One might, if one wanted to, speak of mechanical or machine-like thinking. (Perhaps one can one day even let it be carried out by a machine.) (Behmann 1921: 6–7 [trans. 2015: 176])[^behmann-1921]

Leibniz’s Llullian idea of a machine that could calculate the truth was suddenly at the forefront of early twentieth century mathematics.

### 2.6 Newman and the Cambridge mathematicians

The connection Behmann emphasized between the decision problem and a machine that carries out an “exercise in computation” would soon prove crucial in Turing’s hands. What seems to have been Turing’s first significant brush with the *Entscheidungsproblem* was in 1935, in a Cambridge lecture given by Newman. Newman, a mathematical logician and topologist, was very familiar with the ideas emanating from Göttingen. As early as 1923 he gave a left-field discussion of some of Hilbert’s ideas, himself proposing an approach to the foundations of mathematics that, while radical and new, nevertheless had a strongly Hilbertian flavor (Newman 1923)[^newman-1923]. In 1928, Newman attended an international congress of mathematicians in the Italian city of Bologna, where Hilbert talked about the *Entscheidungsproblem* while lecturing on his proof theory (Hilbert 1930a; Zanichelli 1929)[^hilbert-1930a][^zanichelli-1929]. Hilbert’s leading works in mathematical logic—Hilbert and Ackermann (1928)[^ackermann-1928] and Hilbert and Bernays (1934)—were both recommended reading for Newman’s own lectures on the Foundations of Mathematics (Smithies 1934; Copeland and Fan 2022)[^copeland-2022][^smithies-1934].

Speaking in a tape-recorded interview about Turing’s engagement with the *Entscheidungsproblem*, Newman said “I believe it all started because he attended a lecture of mine on foundations of mathematics and logic”:

> I think I said in the course of this lecture that what is meant by saying that [a] process is constructive is that it’s a purely mechanical machine—and I may even have said, a machine can do it.
>
> And this of course led [Turing] to the next challenge, what sort of machine, and this inspired him to try and say what one would mean by a perfectly general computing machine. (Newman *c*1977)[^newman-1977]

Sadly, there seems to be no record of what else Newman said at that crucial juncture in his lecture. However, his 1923 paper “The Foundations of Mathematics from the Standpoint of Physics” does record some of his related thinking (Copeland & Fan 2023)[^copeland-2023]. There he introduced the term “process” (which he also used in the above quotation), saying “All logic and mathematics consist of certain *processes*” (1923: 12). He emphasized the requirement that a process should *terminate* with the required result (such as a theorem or number); and he gave a formal treatment of processes:

> The properties of processes are formally developed from a set of axioms, and a general method reached for attacking the problem of whether a given process terminates or not. (Newman 1923: 12)[^newman-1923]

Newman did not mention the *Entscheidungsproblem* in his 1923 paper—let alone moot its unsolvability (there is no evidence that, pre-Turing, he thought the problem unsolvable)—yet, with hindsight, he certainly laid some suggestive groundwork for an attack on the problem. He wrote:

> The information of the first importance to be obtained about a process or segment of a process is whether it is *possible* to perform it…. The statement that [process] $\Phi|\,|\alpha\rho$ is possible means that this process *terminates*: comes to a halt … (Newman 1923: 39)[^newman-1923]

Newman even proposed an “apparatus”, a “symbolic machine”, for producing numbers by means of carrying out processes of the sort he analysed, and he gave a profound discussion of real numbers from the standpoint of this proposal (1923: 130ff).

Nor was Newman the only person at Cambridge with an interest in the *Entscheidungsproblem*. The *Entscheidungsproblem* was “in the air” there during the decade leading up to Turing’s assault on it. The Sadleirian Professor of Mathematics at Cambridge, Hardy, took an interest in the problem, inspired by von Neumann’s magisterial exposition and critique of Hilbert’s ideas (von Neumann 1927)[^neumann-1927]. Ackermann himself had visited Cambridge from Göttingen for the first half of 1925 (Zach 2003: 226)[^zach-2003]. Another visitor, Langford—who worked in Cambridge on a fellowship from Harvard for the academic year 1924–25 (Frankena & Burks 1964)[^frankena-1964]—presented a series of results to the American Mathematical Society not long after his return to Harvard, in effect solving a number of special cases of the *Entscheidungsproblem* (Langford 1926a, 1927)[^langford-1926a][^langford-1927].

The Cambridge logician Ramsey, like Turing a Fellow of King’s College, also worked on the *Entscheidungsproblem* in the latter part of the 1920s. He died in 1930 (the year before Turing arrived in Cambridge as an undergraduate), but not before completing a key paper solving the *Entscheidungsproblem* in special cases (Ramsey 1930)[^ramsey-1930]. His work, too, was prominent in the recommended reading for Newman’s lecture course. Braithwaite, another Fellow of King’s College (who had a hand in Turing’s election to a junior research fellowship at King’s in 1935), was keenly interested in Ramsey’s work on the *Entscheidungsproblem* (Copeland & Fan 2022)[^copeland-2022]. Also in 1935, von Neumann visited Cambridge from Princeton, for the term following Newman’s lecture course (Copeland & Fan 2023)[^copeland-2023]. Von Neumann, a member of the Göttingen group during the mid-1920s, had called the *Entscheidungsproblem* “profound and complex”, and he voiced doubts that it was solvable (von Neumann 1927: 11; 1931: 120)[^neumann-1927].

He was not alone. Hardy gave this statement of the *Entscheidungsproblem*, in the course of a famous discussion of Hilbert’s ideas:

> Suppose, for example, that we could find a finite system of rules which enabled us to say whether any given formula was demonstrable or not. (Hardy 1929: 16)[^hardy-1929]

Hardy foresaw what Turing, and Church, would soon prove, telling his audience that such a system of rules “is not to be expected”.

What Turing showed is that there will never be, and can never be, a computing machine satisfying the following specification: When the user types in a formula—any formula—of the functional calculus, the machine carries out a finite number of steps and then outputs the correct answer, either “This formula is provable in the functional calculus” or “This formula is not provable in the functional calculus”, as the case may be. Given, therefore, Turing’s thesis that *if an effective method exists then it can be carried out by one of his machines*, it follows that there is no effective method for deciding the full first-order functional calculus.

## 3. Other Approaches to Computability

Turing and Church were certainly not the only people to tackle the problem of analyzing the concept of effectiveness. This section surveys some other important proposals made during the twentieth and twenty-first centuries.

### 3.1 Gödel

Gödel was led to the problem of analyzing effectiveness by his search for a means to *generalize* his 1931 incompleteness results (which in their original form applied specifically to the formal system set out by Whitehead and Russell in their *Principia Mathematica*). In 1934, he considered an analysis in terms of his generalized concept of recursion—about a year before Church first publicly announced his thesis that “the notion of an effectively calculable function of positive integers should be identified with that of a recursive function” (Church 1935a; Gödel 1934, fn. 3; Davis 1982)[^church-1935a][^davis-1982][^gödel-1934].

But Gödel was doubtful: “I was, at the time … not at all convinced that my concept of recursion comprises all possible recursions” (Gödel 1965b)[^gödel-1965b]. It was Turing’s analysis, Gödel emphasized, that finally enabled him to generalize his incompleteness theorems:

> due to A. M. Turing’s work, a precise and unquestionably adequate definition of the general concept of formal system can now be given. (Gödel 1965a: 71)[^gödel-1965a]

He explained:

> Turing’s work gives an analysis of the concept of “mechanical procedure” (alias “algorithm” or “computation procedure” or “finite combinatorial procedure”). This concept is shown to be equivalent with that of a “Turing machine”. A formal system can simply be defined to be any mechanical procedure for producing formulas, called provable formulas. (Gödel 1965a: 71–72)[^gödel-1965a]

Armed with this definition, incompleteness can, Gödel said, “be proved rigorously for *every* consistent formal system containing a certain amount of finitary number theory” (1965a: 71).

### 3.2 Post

By 1936, Post had arrived independently at an analysis of effectiveness that was substantially the same as Turing’s (Post 1936; Davis & Sieg 2015)[^davis-2015][^post-1936]. Post’s idealized human “worker”—or “problem solver”—operated in a “symbol space” consisting of “a two way infinite sequence of spaces or boxes”. A box admitted

> of but two possible conditions, i.e., being empty or unmarked, and having a single mark in it, say a vertical stroke. (Post 1936: 103)[^post-1936]

The problem solver worked in accordance with “a fixed unalterable set of directions” and could perform a small number of “primitive acts” (Post 1936: 103)[^post-1936], namely:

1. determine whether the box that is presently occupied is marked or not;
2. erase any mark in the box that is presently occupied;
3. mark the box that is presently occupied if it is unmarked;
4. move to the box to the right of the present position; and
5. move to the box to the left of the present position.

Post’s paper was submitted for publication in October 1936, some five months after Turing’s. It contained no analog of Turing’s universal computing machine, and nor did it anticipate Church’s and Turing’s result that the *Entscheidungsproblem* is unsolvable. Curiously, though, Post had achieved far more than he let on in his 1936 paper. In an article subtitled “Account of an Anticipation”, published in 1965 but written in about 1941, he explained that during the early 1920s he had devised a system—he called it the “complete normal system”, because “in a way, it contains all normal systems”—and this, he said, “correspond[ed]” to Turing’s universal machine (Post 1965: 412)[^post-1965]. Furthermore, he argued during the same period that the decision problem is unsolvable in the case of his “normal systems” (1965: 405ff). But it seems he did not extend this argument to anticipate the Church-Turing result that the decision problem for the predicate calculus is unsolvable (1965: 407).

Turing later generously acknowledged Post’s 1936 paper, describing Turing machines as “the logical computing machines introduced by Post and the author” (Turing 1950b: 491)[^turing-1950b].

### 3.3 Hilbert and Bernays

In 1939, in Volume II of their titanic work *Grundlagen der Mathematik* (Foundations of Mathematics), Hilbert and Bernays proposed a logic-based analysis of effectiveness. According to this analysis, effectively calculable numerical functions are numerical functions that can be evaluated in what they called a “*regelrecht*” manner (Hilbert & Bernays 1939: 392–421)[^hilbert-1939]. In this context, the German word “*regelrecht*” can be translated “rule-governed”. Hilbert and Bernays offered the concept of the *rule-governed evaluation* of a numerical function as a “sharpening of the concept of computable” (1939: 417).

The basic idea is this: To evaluate a numerical function (such as addition or multiplication) in a rule-governed way is to calculate the values of the function, step by logical step, in a suitable deductive logical system. On this approach, effective calculability is analysed as *calculability in a logic*. (Both Church and Turing had previously discussed the approach—see Section 4.4.)

The logical system Hilbert and Bernays used to flesh out this idea was an *equational calculus*, reminiscent of a calculus that Gödel had detailed in lectures he gave in Princeton in 1934 (Gödel 1934)[^gödel-1934]. The theorems of an equational calculus are (as the name says) *equations*—for example $2^3 = 8$ and $x^2 + 1 = x(x + 1) - (x - 1),$ or in general $\mathrm{f}(m) = n.$ The Hilbert-Bernays equational calculus contains no logical symbols (such as negation, conjunction, implication, or quantifiers), and every formula is simply an equation between terms. Three types of equation are permitted as the initial formulae (or premisses) of deductions in the system; and the system is required to satisfy three general conditions that Hilbert and Bernays called “recursivity conditions”. The rules of the calculus concern substitutions within equations and are very simple, allowing steps such as:

$$ a = b, f(a) \vdash f(b) $$

On the basis of this calculus (which they called $Z^0$) Hilbert and Bernays established an equivalence result: The numerical functions that are capable of rule-governed evaluation coincide with the (primitive) recursive functions (1939: 403 and 393*n*).

It is perhaps unsurprising that Hilbert, the founder of proof theory, ultimately selected an analysis of effective calculability as calculability *within a logic*, even though Church and Turing had already presented their analyses in terms of recursive functions and Turing machines respectively. Hilbert and Bernays went on to use their analysis to give a new proof of the unsolvability of the *Entscheidungsproblem* (Hilbert & Bernays 1939: 416–421)[^hilbert-1939]. This proof quietly marks what must have been an unsettling, even painful, shift of perspective for them. The idea of a decision procedure for mathematics had until the Church-Turing result been central to their thinking, and in Volume 1 of the *Grundlagen*, published in 1934, they had assumed the *Entscheidungsproblem* to be solvable.

### 3.4 Modern axiomatic analyses

Church reported a discussion he had had with Gödel at the time when it was still wide open how the intuitive concept of effective calculability should be formalized (probably during 1934). Gödel suggested that

> it might be possible, in terms of effective calculability as an undefined notion, to state a set of axioms which would embody the generally accepted properties of this notion, and to do something on that basis. (Church 1935b)[^church-1935b]

Logicians frequently analyse a concept of interest, e.g., universal quantification, not by defining it in terms of other concepts, but by stating a set of axioms that collectively embody the generally accepted properties of (say) universal quantification. To follow this approach in the case of effectiveness, we would “write down some axioms about computable functions which most people would agree are evidently true” (Shoenfield 1993: 26)[^shoenfield-1993]. Shoenfield continued, “It might be possible to prove Church’s Thesis from such axioms”, but added: “However, despite strenuous efforts, no one has succeeded in doing this”.

Moving on a few years, a meeting on *The Prospects for Mathematical Logic in the Twenty-First Century*, held at the turn of the millennium, included the following among leading open problems:

> “Prove” the Church-Turing thesis by finding intuitively obvious or at least clearly acceptable properties of computation that suffice to guarantee that any function so computed is recursive [and therefore can be computed by a Turing machine]. (Shore in Buss et al. 2001: 174–175)[^buss-2001]

The axiomatic type of approach sketched by Gödel has by now been developed in a number of quite different ways. These axiomatic frameworks go a long way toward countering Montague’s complaint of over 60 years ago that “Discussion of Church’s thesis has suffered for lack of a precise general framework within which it could be conducted” (Montague 1960: 432)[^montague-1960]. Some examples of the axiomatic approach are as follows (in chronological order):

- Gandy (Turing’s only PhD student) pointed out that Turing’s analysis of human computation does not immediately apply to computing machines strongly dissimilar from Turing machines. (See Section 4.3 below for details of Turing’s analysis.) For example, Turing’s analysis does not obviously apply to parallel machines which, unlike a Turing machine, are able to process an arbitrary number of symbols simultaneously. Seeking a generalized form of Turing’s analysis that applies equally well to Turing machines and massively parallel machines, Gandy (1980)[^gandy-1980] stated four axioms governing the behaviour of what he called *discrete deterministic mechanical devices*. (He formulated the axioms in terms of hereditarily finite sets.) Gandy was then able to prove that every device satisfying these axioms can be simulated by a Turing machine: Discrete deterministic mechanical devices, even massively parallel ones, are no more powerful than Turing machines, in the sense that whatever computations such a device is able to perform can also be done by the universal Turing machine. (For more on Gandy’s analysis, see Section 6.4.2.)
- Engeler axiomatized the concept of an algorithmic function by using *combinators* (Engeler 1983: ch. III)[^engeler-1983]. Combinators were originally introduced by Schönfinkel in 1924, in a paper that a recent book on combinators described as “presenting a formalism for universal computation for the very first time” (Schönfinkel 1924; Wolfram 2021: 214)[^schönfinkel-1924][^wolfram-2021]. Schönfinkel’s combinators were extensively developed by Curry (Curry 1929, 1930a,b, 1932; Curry & Feys 1958)[^curry-1929][^curry-1930a][^curry-1932][^curry-1958]. Examples of combinators are the “permutator” $\mathrm{C}$ and the “cancellator” $\mathrm{K}$. These produce the following effects: $\mathrm{C}xyz = xzy$ and $\mathrm{K}xy = x$.
- Sieg formalized Turing’s analysis of human computation by means of four axioms (Sieg 2008)[^sieg-2008]. The result, Sieg said, is an axiomatic characterization of “the concept ‘mechanical procedure’”, and he observed that his system “substantiates Gödel’s remarks” (above) that one should try to find a set of axioms embodying the generally accepted properties of the concept of effectiveness (Sieg 2008: 150)[^sieg-2008].
- Dershowitz and Gurevich (2008) stated three very general axioms, treating computations as discrete, deterministic, sequentially-evolving structures of states. They called these structures “state-transition systems”, and called the three axioms the “Sequential Postulates”. They also used a fourth axiom, stipulating that “Only undeniably computable operations are available in initial states” (2008: 306). From their four axioms, they proved a proposition they called Church’s thesis: “Every numeric function computed by a state-transition system satisfying the Sequential Postulates, and provided initially with only basic arithmetic, is partial recursive” (2008: 327).

Returning to the *very idea* of proving the Church-Turing thesis, it is important to note that the proposition Dershowitz and Gurevich call Church’s thesis is in fact *not* the thesis stated by Church, viz. “A function of positive integers is effectively calculable only if recursive”. Crucially, their version of Church’s thesis does not even mention the key concept of effective calculability. The entire project of trying to prove Church’s (or Turing’s) actual thesis has its share of philosophical difficulties. For example, suppose someone were to lay down some axioms expressing claims about effective calculability (as Sieg for instance has done), and suppose it is possible to prove from these axioms that a function of positive integers is effectively calculable only if recursive. Church’s thesis would have been proved from the axioms, but whether the axioms form a satisfactory account of effective calculability is a *further* question. If they do not, then this “proof” of Church’s thesis could carry no conviction. Which is to say, a proof of this sort will be convincing only to one who accepts another thesis, namely that the axioms are indeed a satisfactory account of effective calculability. This is a Churchian meta-thesis. Church’s thesis would have been proved, but only at the expense of throwing up another, unproved, thesis seemingly of the same nature.

There is further discussion of difficulties associated with the idea of proving the Church-Turing thesis in Section 4.3.5, Section 4.5, and Section 4.6.

## 4. The Case for the Church-Turing Thesis

### 4.1 The inductive and equivalence arguments

Although there have from time to time been attempts to call the Church-Turing thesis into question (for example by Kalmár in his 1959; Mendelson replied in his 1963)[^kalmár-1959][^mendelson-1963], the summary of the situation that Turing gave in 1948 is no less true today: “it is now agreed amongst logicians that ‘calculable by L.C.M.’ is the correct accurate rendering” of the informal concept of effectiveness.

In 1936, both Church and Turing gave various grounds for accepting their respective theses. Church argued:

> The fact … that two such widely different and (in the opinion of the author) equally natural definitions of effective calculability [i.e., in terms of λ-definability and recursion] turn out to be *equivalent* adds to the strength of the reasons adduced below for believing that they constitute as general a characterization of this notion as is consistent with the usual intuitive understanding of it. (Church 1936a: 346, emphasis added)[^church-1936a]

Church’s “reasons adduced below” comprised two not wholly convincing arguments. Both suffered from the same weakness, discussed in Section 4.4.4.

Turing, on the other hand, marshalled a formidable case for the thesis. Unlike Church, he offered inductive evidence for it, showing that large classes of numbers “which would naturally be regarded as computable” are computable in his sense (1936: 74–75). Turing proved, for example, that the limit of a computably convergent sequence is computable; that all real algebraic numbers are computable; that the real zeroes of the Bessel functions are computable; and that (as previously noted) π and e are computable (1936: 79–83). But most importantly of all, Turing gave profound logico-philosophical arguments for the thesis. He referred to these arguments simply as “I”, “II” and “III”. They are described in Section 4.3 and Section 4.4.

By about 1950, considerable evidence had amassed for the thesis. One of the fullest surveys of this evidence is to be found in chapters 12 and 13 of Kleene’s 1952. As well as discussing Turing’s argument I, and Church’s two arguments mentioned above, Kleene bolstered Church’s just quoted *equivalence argument*, pointing out that “Several other characterizations … have turned out to be equivalent” (1952: 320). As well as the characterizations mentioned by Church, Kleene included computability by Turing machine, Post’s canonical and normal systems (Post 1943, 1946)[^post-1943][^post-1946], and Gödel’s notion of reckonability (Gödel 1936)[^gödel-1936]. (Turing’s student and lifelong friend Robin Gandy picturesquely called Church’s equivalence argument the “argument by confluence” [Gandy 1988: 78].)[^gandy-1988]

In modern times, the equivalence argument can be presented even more forcefully: All attempts to give an exact characterization of the intuitive notion of an effectively calculable function have turned out to be *equivalent*, in the sense that each characterization offered has been proved to pick out the same class of functions, namely those that are computable by Turing machine. The equivalence argument is often considered to be very strong evidence for the thesis, because of the *diversity* of the various formal characterizations involved. Apart from the many different characterizations already mentioned in Section 1 and Section 3, there are also analyses in terms of register machines (Shepherdson & Sturgis 1963)[^shepherdson-1963], Markov algorithms (Markov 1951)[^markov-1951], and other formalisms.

The equivalence argument may be summed up by saying that the concept of effective calculability—or the concept of computability simpliciter—has turned out to be *formalism-transcendent*, or even “formalism-free” (Kennedy 2013: 362)[^kennedy-2013], in that all these different formal approaches pick out exactly the *same* class of functions.

Indeed, there is not even a need to distinguish, within any given formal approach, systems of different orders or types. Gödel noted in an abstract published in 1936 that the concept “computable” is *absolute*, in the sense that all the computable functions are specifiable in one and the same system, there being no need to introduce a hierarchy of systems of different orders—as is done, for example, in Tarskian analyses of the concept “true”, and standardly in the case of the concept “provable” (Gödel 1936: 24)[^gödel-1936]. Ten years later, commenting on Turing’s work, Gödel emphasized that “the great importance … [of] Turing’s computability” is

> largely due to the fact that with this concept one has for the first time succeeded in giving an absolute definition of an interesting epistemological notion, i.e., one not depending on the formalism chosen. In all other cases treated previously, such as demonstrability or definability, one has been able to define them only relative to a given language…. (Gödel 1946: 150)[^gödel-1946]

In his 1952 survey, Kleene also developed Turing’s inductive argument (1952: 319–320). To summarize:

- Every effectively calculable function that has been investigated in this respect has turned out to be computable by Turing machine.
- All known methods or operations for obtaining new effectively calculable functions from given effectively calculable functions are paralleled by methods for constructing new Turing machines from given Turing machines.

Inductive evidence for the thesis has continued to accumulate. For example, Gurevich points out that

> As far as the input-output relation is concerned, synchronous parallel algorithms and interactive sequential algorithms can be simulated by Turing machines. This gives additional confirmation of the Church-Turing thesis. (Gurevich 2012: 33)[^gurevich-2012]

### 4.2 Skepticism about the inductive and equivalence arguments

It is a general feature of inductive arguments that, while they may supply strong evidence, they nevertheless do not establish their conclusions with certainty. A stronger argument for the Church-Turing thesis is to be desired. Gandy said that the inductive argument

> cannot settle the philosophical (or foundational) question. It might happen that one day some genius established an entirely new sort of calculation. (Gandy 1988: 79)[^gandy-1988]

Dershowitz and Gurevich highlighted the difficulty:

> History is full of examples of delayed discoveries. Aristotelian and Newtonian mechanics lasted much longer than the seventy years that have elapsed since Church proposed identifying effectiveness with recursiveness, but still those physical theories were eventually found lacking. (Dershowitz & Gurevich 2008: 304)[^dershowitz-2008]

Dershowitz and Gurevich presented a highly relevant example of delayed discovery (following Barendregt 1997: 187)[^barendregt-1997]: Any hope that the effectively calculable functions could be identified with the *primitive* recursive functions—introduced in 1923 (Skolem 1923; Péter 1935)[^péter-1935][^skolem-1923]—evaporated a few years later, when Ackermann described an effectively calculable function that is not primitive recursive (Ackermann 1928)[^ackermann-1928].

The equivalence argument has also been deemed unsatisfactory. Dershowitz and Gurevich call it “weak” (2008: 304). After all, the fact that a number of statements are equivalent does not show the statements are true, only that if one is true, all are—and if one is false, all are. Kreisel wrote:

> The support for Church’s thesis … certainly does not consist in … the equivalence of different characterizations: what excludes the case of a *systematic* error? (Kreisel 1965: 144)[^kreisel-1965]

Mendelson put the point more mildly, saying that the equivalence argument is “not conclusive”:

> It is conceivable that all the equivalent notions define a concept that is related to, but not identical with, effective computability. (Mendelson 1990: 228)[^mendelson-1990]

Clearly, what is required is a direct argument for the thesis from first principles. Turing’s argument I fills this role.

### 4.3 Turing’s argument I

The logico-philosophical arguments that Turing gave in Section 9 of “On Computable Numbers” are outstanding among the reasons for accepting the thesis.

He introduced argument I as “only an elaboration” of remarks at the beginning of his 1936 paper—such as:

> We may compare a man in the process of computing a real number to a machine which is only capable of a finite number of conditions $q_1,$ $q_2,$…, $q_R$ which will be called “$m$-configurations”. (Turing 1936 [2004: 59, 75])[^turing-1936]

He also described argument I as a “direct appeal to intuition” (Turing 1936 [2004: 75])[^turing-1936]. The appeal he is talking about concerns our understanding of which features of human computation are the *essential* features (some examples of *in*essential features are that human computers eat, breathe, and sleep).

In outline, argument I runs as follows: Given that human computation has *these* (and only these) essential features—and here Turing supplied a list of features—then, whichever human computation is specified, a Turing machine can be designed to carry out the computation. Therefore, the Turing-machine computable numbers include all numbers that would naturally be regarded as computable (Turing’s thesis).

#### 4.3.1 Turing’s analysis

Turing’s list of the essential features of human computation is as follows (Turing 1936 [2004: 75–76])[^turing-1936]:

1. Computers write symbols on two-dimensional sheets of paper, which may be considered to be (or may actually be) divided up into squares, each square containing no more than a single individual symbol.
2. The computer is not able to recognize, or print, more than a finite number of different types of individual symbol.
3. The computer is not able to observe an unlimited number of squares all at once—if he or she wishes to observe more squares than can be taken in at one time, then successive observations must be made. (Say the maximum number of squares the computer can observe at any one moment is $B$, where $B$ is some positive integer.)
4. When the computer makes a fresh observation in order to view more squares, none of the newly observed squares will be more than a certain fixed distance away from the nearest previously observed square. (Say this fixed distance consists of $L$ squares, where $L$ is some positive integer.)
5. In order to alter a symbol (e.g., to replace it by a different symbol), the computer needs to be actually observing the square containing the symbol.
6. The computer’s behavior at any moment is determined by the symbols that he or she is observing and his or her “state of mind” at that moment. Moreover, the computer’s state of mind at any given moment, together with the symbols he or she is observing at that moment, determine the computer’s state of mind at the next moment.
7. The number of states of mind that need to be taken into account when describing the computer’s behavior is finite.
8. The operations the computer performs can be split up into elementary operations. These are so simple that no more than one symbol is altered in a single elementary operation.
9. All elementary operations are of one or other of the following forms:
10. A change of state of mind.
11. A change of observed squares, together with a possible change of state of mind.
12. A change of symbol, together with a possible change of state of mind.

#### 4.3.2 Next step: $B$-$L$-type Turing machines

The next step of argument I is to establish that if human computation has those and only those essential features, then, whatever human computation is specified, a Turing machine can be designed to perform the computation. In order to show this, Turing introduced a modified form of Turing machine, which can be called a “$B$-$L$-type” Turing machine. A $B$-$L$-type Turing machine has much in common with an ordinary Turing machine:

1. A $B$-$L$-type Turing machine consists of a scanner and a one-dimensional paper tape; the tape is divided into squares.
2. The scanner contains mechanisms that enable it to move the tape to the left or right.
3. The scanner’s mechanisms also enable it recognize, delete, and print symbols.
4. The scanner is able to recognize and print only a finite number of different types of individual symbol.
5. At any moment, the control mechanism of the scanner will be in any one of a finite number of internal states. Turing terms these “$m$-configurations”. He included an explanatory remark about $m$-configurations in a summary in French of the central ideas of “On Computable Numbers”: Inside the machine, “levers, wheels, et cetera can be arranged in several ways, called ‘$m$-configurations’”. (The complete summary is translated in Copeland & Fan 2022.)[^copeland-2022]
6. The machine’s behavior at any moment is determined by its $m$-configuration and the symbols it is observing (i.e., scanning).
7. The machine’s possible behaviors are limited to moving the tape, deleting the symbol on an observed square, and printing a symbol on an observed square. Each of these behaviors may be accompanied by a change in $m$-configuration.

Moving on now to the differences between ordinary Turing machines and $B$-$L$-type machines:

1. The scanner of a $B$-$L$-type machine can observe up to $B$ squares at once; whereas the scanner of an ordinary Turing machine can observe only a single square of the tape at any one moment. A Turing machine that is able to survey a sequence of squares all at once like this is sometimes known by the (perhaps inelegant) term “string machine”.
2. The scanner of a $B$-$L$-type machine can, in a single operation, move the tape up to $L$ squares at once (to the left or right of any one of the immediately previously observed squares); whereas the scanner of an ordinary machine can move the tape by only one square in a single elementary operation.

Returning to the argument, Turing asserted that, given his account 1–9 of the essential features of human computation, a $B$-$L$-type machine can “do the work” of any human computer (1936: 77). This is because the $B$-$L$-type machine either duplicates or can simulate each of features 1–9. Let us take these features in turn.

Feature 1 is simulated by the machine: The $B$-$L$-type machine uses its one-dimensional tape to mimic the computer’s two-dimensional sheets of paper. Turing said:

> I think it will be agreed that the two-dimensional character of paper is no essential of computation. (Turing 1936 [2004: 75])[^turing-1936]

However, some commentators note that there is room for doubt about this matter. Gandy complained that Turing here argued “much too briefly”, saying:

> It is not totally obvious that calculations carried out in two (or three) dimensions can be put on a one-dimensional tape and yet preserve the “local” properties. (Gandy 1988: 81, 82–83)[^gandy-1988]

Dershowitz and Gurevich ask:

> [H]ow certain is it that each and every elaborate data structure used during a computation can be encoded as a string, and its operations simulated by effective string manipulations? (Dershowitz & Gurevich 2008: 305)[^dershowitz-2008]

Progressing to the other features on Turing’s list: 2, 3, 4 and 5 are straightforwardly duplicated in the machine. Features 6 and 7 are simulated, by letting the machine’s $m$-configurations do duty for the computer’s states of mind (more on that below). Feature 8 is duplicated in the machine: the machine’s complex operations (such as long multiplication and division) are built up out of elementary operations. Feature 9 is simulated, again by letting the $m$-configurations to do duty for human states of mind.

#### 4.3.3 Final step

The next and final step of argument I involves the statement that any computation done by a $B$-$L$-type machine can also be done by an ordinary Turing machine. This is straightforward, since by means of a sequence of single-square moves, the ordinary machine can simulate a $B$-$L$-type machine’s tape-moves of up to $L$ squares at once; and the ordinary machine can also simulate the $B$-$L$-type machine’s scanning of up to $B$ squares at once, by means of a sequence of single-square scannings (interspersed where necessary with changes of $m$-configuration). Thus, if a $B$-$L$-type machine can “do the work” of a human computer, so can an ordinary Turing machine.

In summary, Turing has shown the following—provided his claim is accepted that “To each state of mind of the computer corresponds an ‘$m$-configuration’ of the machine”: *Given the above account of the essential features of human computation, an ordinary Turing machine is able to do the work of any human computer*. In other words: Subject to that proviso and that given, he has established his thesis that the numbers computable by an ordinary Turing machine include all numbers which would naturally be regarded as computable.

#### 4.3.4 States of mind, and argument III

But should Turing’s claim about the correspondence of states of mind and $m$-configurations be accepted? Might not human states of mind greatly surpass arrangements of levers and wheels? Might not the computer’s states of mind sometimes determine him or her to change the symbols in a way that a $B$-$L$-type machine cannot?

Turing addressed worries about the correspondence between states of mind and $m$-configurations in his supplementary argument III, which he said “may be regarded as a modification of I” (1936: 79). Here he argued that reference to the computer’s states of mind can be avoided altogether, by talking instead about what he called a “note of instructions”. A note of instructions, he said, is “a more definite and physical counterpart” of a state of mind. Each step of the human computation can be regarded as being governed by a note of instructions—by means of following the instructions in the note, the computer will know what operation to perform at that step (erase, print, or move). Turing envisaged the computer preparing new notes on the fly, as the computation progresses: “The note of instructions must enable him [the computer] to carry out one step and write the next note”. Each note is in effect a tiny computer program, which both carries out a single step of the computation and also writes the program that is to be used at the next step.

Once instruction notes are in the picture, there is no need to refer to the human computer’s states of mind:

> the state of progress of the computation at any stage is completely determined by the note of instructions and the symbols on the tape. (Turing 1936 [2004: 79])[^turing-1936]

Another—related—way of answering the worry that human states of mind might surpass the machine’s $m$-configurations is to point out that, even if this were true, it would make no essential difference to argument I. This is because of feature 3 and feature 7 (Section 4.3.1): The number of states of mind that need to be taken into account is finite, and the maximum number of squares that the computer can observe at any one moment is $B$ (a finite number).

Given feature 7, it follows that no matter how fancy a state of mind might be, the computer’s relevant behaviors when in that state of mind can be encapsulated by means of finite table. Each row of the table will be of the following form: If the observed symbols are such-and-such, then perform elementary operation so-and-so (where the elementary operations are as specified in feature 9). Since only a finite number of states of mind are in consideration (feature 3)—say $n$—all necessary information about the computer’s states of mind can be encapsulated in a list of $n$ such tables. This list consists of finitely many symbols, and therefore it can be placed on the tape of a $B$-$L$-type machine in advance of the machine beginning its emulation of the human computer. (This is akin to writing a program on the tape of a universal Turing machine.) The $B$-$L$-type machine consults the list at each step of the computation, and the machine’s behavior at every step is completely determined by the list together with the currently observed symbols.

To conclude: no matter what powers might be accorded to the human computer’s states of mind, a $B$-$L$-type machine can nevertheless “do the work” of the computer, so long as only finitely many states of mind need be taken into consideration (given, of course, the remainder of Turing’s account of the essential features of computation).

#### 4.3.5 Turing’s theorem

Now that the proviso mentioned above about states of mind has been cleared out of the way, Turing’s achievement in argument I can be summed up like this: He has, in Gandy’s phrase, “outlined a proof” of a theorem (Gandy 1980: 124)[^gandy-1980].

> **Turing’s computation theorem**:
> This account of the essential features of human computation implies Turing’s thesis.

It should by now be completely clear why Turing called argument I a “direct appeal to intuition”. If one’s intuition tells one that Turing’s account of the essential features of human computation is correct, then the theorem can be applied and Turing’s thesis is secured.

However, Turing’s account is not immune from skepticism. Some skeptical questions are: Might there be aspects of human computation that Turing has overlooked? Might a computer who is limited by 1–9 be unable to perform some calculations that *can* be done by a human computer not so restricted? Also, must the number of states of mind that need to be taken into account when describing the computer’s behavior always be finite? Gödel thought the number of Turing’s “distinguishable states of mind” may “converge toward infinity”, saying

> What Turing disregards completely is the fact that *mind, in its use, is not static, but constantly developing*. (Gödel 1972: 306)

Indeed, what are the *grounds* supposed to be for thinking that 1–9 are true? Are these claims supposed to be grounded in the nature and limitations of the human sense organs and the human mind? Or are they supposed to be grounded in some other way, e.g., in the fundamental nature of *effective methods*?

Turing’s argument I is a towering landmark and there is now a sizable literature on these and other questions concerning it. For more about this important argument see, for starters, Sieg 1994, 2008; Shagrir 2006; and Copeland & Shagrir 2013.

### 4.4 Turing’s argument II

#### 4.4.1 Calculating in a logic

Kleene, in his survey of evidence for the Church-Turing thesis, listed a type of argument based on symbolic logic (Kleene 1952: 322–3)[^kleene-1952]. (He called these category “D” arguments.) Arguments of this type commence by introducing a plausible alternative method of characterizing effectively calculable functions (or, in Turing’s case, computable functions or numbers). The alternative method involves derivability in one or another symbolic logic: The concept of effective calculability (or of computability) is characterized in terms of *calculability within the logic* (see Section 3.3). Schematically, the characterization is of the form: A function is effectively calculable (or computable) if each successive value of the function is derivable within the logic. The next step of the argument is then to establish that the new characterization (whatever it is) is equivalent to the old. In Church’s case, this amounts to arguing that the new characterization is equivalent to his characterization in terms of either recursiveness or λ-definability. Finally, the conclusion that the new and previous characterizations are equivalent is claimed as further evidence in favor of the Church-Turing thesis.

In his survey, Kleene illustrated this approach by describing an argument of Church’s (Church 1936a: 357–358)[^church-1936a]. Turing’s argument II is also of this type, but, curiously, Kleene did not mention it (despite assigning five pages of his 1952 survey to Turing’s argument I).

#### 4.4.2 Church’s “step-by-step” argument

It is instructive to examine Church’s argument—which Gandy dubbed the “step-by-step” argument (Gandy 1988: 77)[^gandy-1988]—before considering Turing’s II. Church introduced the following alternative method, describing it as among the “methods which naturally suggest themselves” in connection with defining effective calculability:

> a function $F$ (of one positive integer) [is defined] to be effectively calculable if, for every positive integer $m$, there exists a positive integer $n$ such that $F(m) = n$ is a provable theorem. (Church 1936a: 358)[^church-1936a]

Church did not specify any particular symbolic logic. He merely stipulated a number of general conditions that the logic must satisfy (1936a: 357). These included the stipulations that the list of axioms of the logic must be either finite or enumerably infinite, and that each rule of the logic must specify an “effectively calculable operation” (the latter is necessary, he said, if the logic “is to serve at all the purposes for which a system of symbolic logic is usually intended”). Having introduced this alternative method of characterizing effective calculability, Church then went on to argue that every function (of one positive integer) that is “calculable within the logic” in this way is also recursive. He concluded, in support of Church’s thesis, that the new method produces “no more general definition of effective calculability than that proposed”, i.e., in terms of recursiveness (1936a: 358).

#### 4.4.3 Turing’s variant

Turing’s prefatory remarks to argument II bring out its broad similarity to Church’s argument. Turing described II as being a “proof of the equivalence of two definitions”, adding—“in case the new definition has a greater intuitive appeal” (1936 [2004: 75]).

Turing’s argument, unlike Church’s, does involve a specific symbolic logic, namely Hilbert’s first-order predicate calculus. Argument II hinges on a proposition that can be called

> **Turing’s provability theorem**:
> Every formula provable in Hilbert’s first-order predicate calculus can be proved by the universal Turing machine. (See Turing 1936 [2004: 77].)[^turing-1936]

The alternative method considered by Turing (which is similar to Church’s) characterizes a computable number (or sequence) in terms of statements each of which supplies the next digit of the number (or sequence). The number (sequence) is said to be computable if each such statement is provable in Hilbert’s calculus (the idea being that, if this is so, then Hilbert’s calculus may be used to calculate—or compute—the digits of the number one by one). Employing the provability theorem, Turing then showed the following: Every number that is computable according to this alternative definition is also computable according to the Turing-machine definition (i.e., the digits of the number can be written out progressively by a Turing machine), and vice versa (Turing 1936 [2004: 78])[^turing-1936]. In other words, he proved the equivalence of the two definitions, as promised.

#### 4.4.4 Comparing the Church and Turing arguments

Returning to Church’s step-by-step argument, there is an air of jiggery-pokery about it. Church wished to conclude that functions “calculable within the logic” are recursive, and, in the course of arguing for this, he found it necessary to assert that each rule of the logic is a recursive operation, on the basis that each rule is required to be an effectively calculable operation. In a different context, he might have supported this assertion by appealing to Church’s thesis (which says, after all, that what is effectively calculable is recursive). But in the present context, such an appeal would naturally be question-begging.

Nor did Church make any such appeal. (Sieg described Church’s reasoning as “semi-circular”, but this seems too harsh—there is nothing circular about it; Sieg 1994: 87, 2002: 394.)[^sieg-1994][^sieg-2002] But nor did Church offer any compelling reasons in support of his assertion. He merely gave examples of systems whose rules *are* recursive operations; and also said—having stipulated that each rule of procedure must be an effectively calculable operation—that he will “*interpret this to mean* that … each rule of procedure must be a recursive operation” (1936: 357, italics added.) In short, a crucial step of Church’s argument for Church’s thesis receives inadequate support. Sieg famously dubbed this step the “stumbling block” in Church’s argument (Sieg 1994: 87)[^sieg-1994].

There is no such difficulty in Turing’s argument. Having selected a specific logic (Hilbert’s calculus), Turing was able specify a Turing machine that would “find all the provable formulae of the calculus”, so making it indubitable that functions calculable in the logic are Turing-machine computable (Turing 1936 [2004: 77])[^turing-1936]. For this reason, Turing’s argument II is to be preferred to Church’s step-by-step argument.

### 4.5 Kripke’s version of argument II

A significant recent contribution to the area has been made by Kripke (2013)[^kripke-2013]. A conventional view of the status of the Church-Turing thesis is that, while “very considerable intuitive evidence” has amassed for the thesis, the thesis is “not a precise enough issue to be itself susceptible to mathematical treatment” (Kripke 2013: 77)[^kripke-2013]. Kleene gave an early expression of this now conventional view:

> Since our original notion of effective calculability of a function … is a somewhat vague intuitive one, the thesis cannot be proved. … While we cannot prove Church’s thesis, since its role is to delimit precisely an hitherto vaguely conceived totality, we require evidence …. (Kleene 1952: 318)[^kleene-1952]

Rejecting the conventional view, Kripke suggests that, on the contrary, the Church-Turing thesis is susceptible to mathematical proof. Furthermore, he canvasses the idea that Turing himself sketched an argument that serves to prove the thesis.

Kripke attempts to build a mathematical demonstration of the Church-Turing thesis around Turing’s argument II. He claims that his demonstration is “very close” to Turing’s (Kripke 2013: 80)[^kripke-2013]. However, this is debatable, since, in its detail, the Kripke argument differs considerably from argument II. But one can at least say that Kripke’s argument was inspired by Turing’s argument II, and belongs in Kleene’s category “D” (along with II and Church’s step-by-step argument).

Kripke argues that the Church-Turing thesis is a corollary of Gödel’s completeness theorem for first-order predicate calculus with identity. Put somewhat crudely, the latter theorem states that every *valid* deduction (couched in the language of first-order predicate calculus with identity) is *provable* in the calculus. In other words, the deduction of $B$ from premises $A_{1},$ $A_{2},$ … $A_{n}$ (where statements $A_{1},$ $A_{2},$ … $A_{n},$ $B$ are all in the language of first-order predicate calculus with identity) is logically valid if and only if $B$ can be proved from $A_{1},$ $A_{2},$ … $A_{n}$ in the calculus.

The first step of the Kripke argument is his claim that (error-free, human) computation is itself a form of deduction:

> [A] computation is a special form of mathematical argument. One is given a set of instructions, and the steps in the computation are supposed to follow—follow deductively—from the instructions as given. *So a computation is just another mathematical deduction, albeit one of a very specialized form*. (Kripke 2013: 80)[^kripke-2013]

The following two-line program in pseudo-code illustrates Kripke’s claim. The symbol “$\rightarrow$” is read “becomes”, and “=” as usual means identity. The first instruction in the program is $r \rightarrow 2$. This tells the computer to place the value 2 in storage location $r$ (assumed to be initially empty). The second instruction $r \rightarrow r + 3$ tells the computer to add 3 to the content of $r$ and store the result in $r$ (over-writing the previous content of $r$). The execution of this two-line program can be represented as a deduction:

> {Execution of $r \rightarrow 2$, followed immediately by execution of $r \rightarrow r + 3$} logically entails that $r = 5$ in the immediately resulting state.

In the case of Turing-machine programs, Turing developed a detailed logical notation for expressing all such deductions (Turing 1936)[^turing-1936].

(In fact, the successful execution of *any* string of instructions can be represented deductively in this fashion—Kripke has not drawn attention to a feature special to computation. The instructions do not need to be ones that a computer can carry out.)

The second step of Kripke’s argument is to appeal to what he refers to as *Hilbert’s thesis*: this is the thesis that the steps of any mathematical argument can be expressed “in a language based on first-order logic (with identity)” (Kripke 2013: 81)[^kripke-2013]. The practice of calling this claim “Hilbert’s thesis” originated in Barwise (1977: 41)[^barwise-1977], but it should be noted that since Hilbert regarded second-order logic as indispensable (see, e.g., Hilbert & Ackermann 1928: 86)[^ackermann-1928][^hilbert-1928], the name “Hilbert’s thesis” is potentially misleading.

Applying “Hilbert’s thesis” to Kripke’s above quoted claim that “a computation is just another mathematical deduction” (2013: 80) yields:

> every (human) computation can be formalized as a valid deduction couched in the language of first-order predicate calculus with identity.

Now, applying Gödel’s completeness theorem to this yields in turn:

> every (human) computation is provable in first-order predicate calculus with identity, in the sense that, given an appropriate formalization, each step of the computation can be derived from the instructions (possibly in conjunction with ancillary premises, e.g., well-known mathematical premises, or premises concerning numbers that are supplied to the computer at the start of the computation).

Finally, applying Turing’s provability theorem to this intermediate conclusion yields the Church-Turing thesis:

> every (human) computation can be done by Turing machine.

### 4.6 Turing on the status of the thesis

As Section 3.4 mentioned, Dershowitz and Gurevich have also argued that the Church-Turing thesis is susceptible to mathematical proof (Dershowitz & Gurevich 2008)[^dershowitz-2008]. They offer “a proof of Church’s Thesis, as Gödel and others suggested may be possible” (2008: 299), and they add:

> In a similar way, but with a different set of basic operations, one can prove Turing’s Thesis, … . (Dershowitz & Gurevich 2008: 299)[^dershowitz-2008]

Yet Turing’s own view of the status of his thesis is very different from that expressed by Kripke, Dershowitz and Gurevich. According to Turing, his thesis is not susceptible to mathematical proof. He did not consider either argument I or argument II to be a mathematical demonstration of his thesis: he asserted that I and II, and indeed “[a]ll arguments which can be given” for the thesis, are

> fundamentally, appeals to intuition, and for this reason rather unsatisfactory mathematically. (Turing 1936 [2004: 74])[^turing-1936]

Indeed, Turing might have regarded “Hilbert’s thesis” as itself an example of a proposition that can be justified only by appeals to intuition.

Turing discussed a thesis closely related to Turing’s thesis, namely *for every systematic method there is a corresponding substitution-puzzle* (where “substitution-puzzle”, like “computable by Turing machine”, is a rigorously defined concept). He said:

> The statement is … one which one does not attempt to prove. Propaganda is more appropriate to it than proof, for its status is something between a theorem and a definition. (Turing 1954 [2004: 588])[^turing-1954]

Probably Turing would have taken this remark to apply equally to the thesis (Turing’s thesis) that *for every systematic method there is a corresponding Turing machine*.

Turing also said (in handwritten material published in 2004) that the phrase “systematic method”

> is a phrase which, like many others e.g., “vegetable” one understands well enough in the ordinary way. But one can have difficulties when speaking to greengrocers or microbiologists or when playing “twenty questions”. Are rhubarb and tomatoes vegetables or fruits? Is coal vegetable or mineral? What about coal gas, marrow, fossilised trees, streptococci, viruses? Has the lettuce I ate at lunch yet become animal? … The same sort of difficulty arises about question c) above [*Is there a systematic method by which I can answer such-and-such questions*?]. An ordinary sort of acquaintance with the meaning of the phrase “systematic method” won’t do, because one has got to be able to say quite clearly about any kind of method that might be proposed whether it is allowable or not. (Turing in Copeland 2004: 590)[^copeland-2004]

Here Turing is emphasizing that the term “systematic method” is not exact, and so in that respect is like the term “vegetable”, and unlike mathematically precise terms such as “λ-definable”, “Turing-machine computable”, and “substitution-puzzle”. Kleene claimed that, since terms like “systematic method” and “effectively calculable” are not exact, theses involving them cannot be proved (op. cit.). Turing however did not voice a similar argument (perhaps because he saw a difficulty). The fact that the term “systematic method” is inexact is *not* enough to show that there could be no mathematically acceptable proof of a thesis involving the term. Mendelson gave a graphic statement of this point, writing about what is called above “*the converse of Church’s thesis*” (Section 1.5):

> The assumption that a proof connecting intuitive and precise mathematical notions is impossible is patently false. In fact, half of CT (the “easier” half), the assertion that all partial-recursive functions are effectively computable, is acknowledged to be obvious in all textbooks in recursion theory. A straightforward argument can be given for it…. This simple argument is as clear a proof as I have seen in mathematics, and it is a proof in spite of the fact that it involves the intuitive notion of effective computability. (Mendelson 1990: 232–233)[^mendelson-1990]

Yet the point that the “intuitive” nature of some of its terms does not rule out the thesis’s being provable is not to say that the thesis *is* provable. If the status of the Church-Turing thesis is “something between a theorem and a definition”, then the definition is presumably Church’s proposal to “define the notion … of an effectively calculable function” (Section 1.5) and the theorem is Turing’s computation theorem (Section 4.3.5), i.e., that given Turing’s account of the essential features of human computation, Turing’s thesis is true. This theorem is demonstrable, but to prove the thesis itself from the theorem, it would be necessary to show, with mathematical certainty, that Turing’s account of the essential features of human computation is correct. So far, no one has done this. Propaganda does seem more appropriate than proof.

## 5. The Church-Turing Thesis and the Limits of Machines

### 5.1 Two distinct theses

Can the universal Turing machine perfectly simulate the behavior of *each and any* machine? The Church-Turing thesis is sometimes regarded as providing a statement of the logical limits of machinery, to the effect that the universal Turing machine is the most general machine possible (and so the answer to the question just posed is *yes*.) For example:

> That there exists a most general formulation of machine and that it leads to a unique set of input-output functions has come to be called *Church’s thesis*. (Newell 1980: 150)[^newell-1980]

Yet the Church-Turing thesis is a thesis about the extent of *effective* methods (therein lies its mathematical importance). Putting this another way, the thesis concerns what a *human being* can achieve when calculating by rote, using paper and pencil (absent contingencies such as boredom, death, or insufficiency of paper). What a human rote-worker can achieve, and what a machine can achieve, may be different.

Gandy was perhaps the first to distinguish explicitly between Turing’s thesis and the very different proposition that *whatever can be calculated by a machine can be calculated by a Turing machine* (Gandy 1980)[^gandy-1980]. Gandy called this proposition “Thesis M”. He pointed out that Thesis M is in fact false in the case of some “machines obeying Newtonian mechanics”, where “there may be rigid rods of arbitrary lengths and messengers travelling with arbitrary large velocities” (1980: 145). He also pointed out that Thesis M fails to apply to what he calls “essentially analogue machines” (1980: 125). A most interesting question is whether Thesis M is true of all *discrete* (i.e., non-analogue) machines that are consistent with the *actual laws of physics*. This question is discussed in Section 6.4.

Thesis M is imprecise, since Gandy never explicitly specified quite what he meant by “calculated by a machine”. It is useful to state a more definite proposition that captures the spirit of Thesis M. This might be called the *strong Church-Turing thesis*, but on balance it seems preferable to avoid that name, since the proposition in question is very different from the Church-Turing thesis of 1936. The proposition will be called the “maximality thesis”.

Some more terminology: A machine $m$ will be said to *generate* (borrowing this word from Turing 1937: 153)[^turing-1937] a certain function (e.g., $x$ squared) if $m$ can be set up so that, if $m$ is presented with any of the function’s arguments (e.g., 4), $m$ will carry out some sequence of processing steps, at the end of which $m$ produces the corresponding value of the function (16 in the example). *Mutatis mutandis* for functions that, like addition, demand more than one argument.

> **Maximality thesis**:
> All functions that can be generated by machine are effectively computable.

“Effectively computable” is a commonly used term: A function is said to be effectively computable if (and only if) there is an effective method for obtaining its values. When phrased in terms of effective computability, the Church-Turing thesis says: All effectively computable functions are Turing-machine computable.

Clearly the Church-Turing thesis and the maximality thesis are different theses.

### 5.2 The “equivalence fallacy”

A common argument for the maximality thesis, or an equivalent, cites the fact, noted above, that many different attempts to analyse the informal notion of computability in precise terms—attempts by Turing, Church, Post, Markov, and others—turned out to be *equivalent* to one another, in the sense that each analysis provably picks out the same class of functions, namely those functions computable by Turing machines.

As previously mentioned, this convergence of analyses is often considered strong evidence for the Church-Turing thesis (this is the equivalence argument for the thesis—Section 4.1). Some go further and take this convergence to be evidence also for the maximality thesis. Newell, for example, presented the convergence of the analyses given by Turing, Church, Post, Markov, et al., as showing that

> all attempts to … formulate … general notions of mechanism … lead to classes of machines that are equivalent in that they encompass *in toto* exactly the same set of input-output functions. (Newell 1980: 150)[^newell-1980]

The various equivalent analyses, said Newell, constitute a

> large zoo of different formulations of maximal classes of machines. (ibid.)

Arguably there is a fallacy here. The analyses Newell is discussing are of the concept of an effective method: The equivalence of the analyses bears only on the question of the extent of what is *humanly* computable, not on the further question whether functions generatable by *machines* could extend beyond what is in principle humanly computable.

### 5.3 Watching our words

It may be helpful at this point to survey some standard technical terminology that could set traps for the unwary.

#### 5.3.1 The word “computable”

As already emphasized, when Turing talks about computable numbers, he is talking about humanly computable numbers. He says: “Computing is normally done by writing certain symbols on paper” (1936 [2004: 75])—and normally done “by human clerical labour, working to fixed rules” (1945 [2005: 386]). “The computer”, he says, might proceed “in such a desultory manner that he never does more than one step at a sitting” (1936 [2004: 79]). The work of the human computer is mechanizable: “We may now construct a machine”—the Turing machine—“to do the work of this computer” (1936 [2004: 77]). See also Section 7 for more quotations relating to this crucial point.

Thus, the various results in “On Computable Numbers” to the effect that such-and-such functions are uncomputable are accordingly about human computers. Turing should not be construed as intending to state results about the limitations of machinery. Gandy wrote:

> it is by no means obvious that the limitations described in [Section 4.3 above] apply to mechanical devices; Turing does not claim this. (Gandy 1988: 84)[^gandy-1988]

#### 5.3.2 Two instructive quotations

> [C]ertain functions are uncomputable in an absolute sense: uncomputable even by [Turing machine], and, therefore, uncomputable by any past, present, or future real machine. (Boolos & Jeffrey 1974: 55)[^boolos-1974]

In the technical logical literature, the term “computable” is usually used to mean “effectively computable” (although not always—see Section 5.3.3). (“Effectively computable” was defined in Section 5.1.) Since Boolos and Jeffrey are using “computable” to mean “effectively computable”, what they are saying in this quotation comes down to the statement that the functions in question are *not effectively computable* by any past, present, or future real machine—which is true, since the functions are, *ex hypothesi*, *not* effectively computable. However, to a casual reader of the literature, this statement (and others like it) might appear to say more than it in fact does. That a function is *uncomputable* (i.e., is effectively uncomputable), by any past, present, or future real machine, does not entail *per se* that the function in question cannot be *generated* by some real machine.

The second quotation:

> FORMAL LIMITS OF MACHINE BEHAVIORS … There are certain behaviors that are “uncomputable”—behaviors for which *no* formal specification can be given for a machine that will exhibit that behavior. The classic example of this sort of limitation is Turing’s famous *Halting Problem*: can we give a formal specification for a machine which, when provided with the description of *any* other machine together with its initial state, will … determine whether or not that machine will reach its halt state? Turing proved that no such machine can be specified. (Langton 1989: 12)[^langton-1989]

What is proved is that no *Turing machine* can always determine, when provided with the description of *any* Turing machine together with its initial state, whether or not that machine will reach its halt state. Turing certainly proved nothing entailing that it is impossible to specify a machine *of some sort or other* that can do what Langton describes. Thus, the considerations Langton presents do not impose any general formal limits on machine behaviors—only on the behaviors of Turing machines. Yet the quotation gives a different impression. (In passing, it is worth pointing out that although the Halting Problem is very commonly attributed to Turing, as Langton does here, Turing did not in fact formulate it. The Halting Problem originated with Davis in the early 1950s (Davis 1958: 70)[^davis-1958].)

#### 5.3.3 Beyond effective

Some authors use phrases such as “computation in a broad sense”, or simply “computation”, to refer to computation of a type that potentially transcends effective computation (e.g., Doyle 2002; MacLennan 2003; Shagrir & Pitowsky 2003; Siegelmann 2003; Andréka, Németi, & Németi 2009; Copeland & Shagrir 2019)[^andréka-2009][^copeland-2019][^doyle-2002][^maclennan-2003][^shagrir-2003][^siegelmann-2003].

Doyle, for instance, suggested that *equilibrating systems* with discrete spectra (e.g., molecules or other quantum many-body systems) may illustrate a concept of computation that is wider than effective computation. Since “equilibrating can be so easily, reproducibly, and mindlessly accomplished”, Doyle said, we may “take the operation of equilibrating” to be a computational operation, even if the functions computable in principle using Turing-machine operations *plus* equilibrating include functions that are not computable by an unaided Turing machine (Doyle 2002: 519)[^doyle-2002].

#### 5.3.4 The word “mechanical”

There is a world of difference between the technical and everyday meanings of “mechanical”. In the technical literature, “mechanical” and “effective” are usually used interchangeably: A “mechanical” procedure is simply an effective procedure. Gandy 1988 outlines the history of this use of the word “mechanical”.

Statements like the following occur in the literature:

> Turing proposed that a certain class of abstract machines [Turing machines] could perform any “mechanical” computing procedure. (Mendelson 1964: 229)[^mendelson-1964]

This could be mistaken for Thesis M. However, “mechanical” is here being used in its technical sense, and the statement is nothing more than the Church-Turing thesis:

> Turing proposed that a certain class of abstract machines could perform any effective computing procedure.

The technical usage of “mechanical” has a tendency to obscure the conceptual possibility that not all machine-generatable functions are Turing-machine computable. The question “Can a *machine* implement a procedure that is not mechanical?” may appear self-answering—yet this is what is being asked if Thesis M and the maximality thesis are questioned.

### 5.4 The strong maximality thesis

The maximality thesis has two interpretations, depending whether the phrase “can be generated by machine” is taken in the sense of “can be generated by a machine conforming to the physical laws of the actual world” (the weak form of the thesis), or in a sense that quantifies over *all* machines, irrespective of conformity to the actual laws of physics (the strong form). (The strong-weak terminology reflects the fact that the strong form entails the weak, but not vice versa.)

The weak form will be discussed in Section 6.4. The strong form is known to be false. This can be shown by giving an example of a notional machine that is capable of generating a function that is not effectively computable. A single example will be provided here; further examples may be found in Andréka et al. 2009, Davies 2001, Hogarth 1994, Pitowsky 1990, Siegelmann 2003, and other papers mentioned below.

#### 5.4.1 Accelerating Turing machines

Accelerating Turing machines (ATMs) are exactly like standard Turing machines except that their speed of operation accelerates as the computation proceeds (Stewart 1991; Copeland 1998a,b, 2002a; Copeland & Shagrir 2011)[^copeland-1998a][^copeland-2002a][^copeland-2011][^stewart-1991]. An ATM performs the second operation called for by its program in half the time taken to perform the first, the third in half the time taken to perform the second, and so on.

If the time taken to perform the first operation is called one “moment”, then the second operation is performed in half a moment, the third operation in quarter of a moment, and so on. Since

$$ \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \ldots + \frac{1}{2^n} + \frac{1}{2^{n+1}} + \ldots \le 1, $$

an ATM is able to perform infinitely many operations in two moments of operating time. This enables ATMs to generate functions that cannot be computed by any standard Turing machine (and so, by the Church-Turing thesis, these functions are not effectively computable).

One example of such a function is the *halting function $h$*. $h(n) = 1$ if the $n$th Turing machine halts, and $h(n) = 0$ if the $n$th Turing machine runs on endlessly. It is well known that no standard Turing machine can compute this function (Davis 1958)[^davis-1958]; but an ATM can produce any of the function’s values in a finite period of time.

When computing $h(n)$, the ATM’s first step is write “0” on a square of the tape called the answer square ($A$). The ATM then proceeds to simulate the actions of the $n$th Turing machine. If the ATM finds that the $n$th machine halts, then the ATM goes on to erase the “0” it previously wrote on $A$, replacing this by “1”. If, on the other hand, the $n$th machine does not halt, the ATM never returns to square $A$ to erase the “0” originally written there. Either way, once two moments of operating time have elapsed, $A$ contains the value $h(n)$ (Copeland 1998a)[^copeland-1998a].

This notional machine is a counterexample to the strong maximality thesis.

## 6. Modern Versions of the Church-Turing Thesis

### 6.1 The algorithmic version

In modern computer science, algorithms and effective procedures are associated not primarily with humans but with machines. Accordingly, many computer science textbooks formulate the Church-Turing thesis without mentioning human computers (e.g., Hopcroft & Ullman 1979; Lewis & Papadimitriou 1981)[^hopcroft-1979][^lewis-1981]. This is despite the fact that the concept of human computation lay at the heart of Turing’s and Church’s analyses.

The variety of algorithms studied by modern computer science eclipses the field as it was in Turing’s day. There are now parallel algorithms, distributed algorithms, interactive algorithms, analog algorithms, hybrid algorithms, quantum algorithms, enzymatic algorithms, bacterial foraging algorithms, slime-mold algorithms and more (see e.g., Gurevich 2012; Copeland & Shagrir 2019)[^copeland-2019][^gurevich-2012]. The universal Turing machine cannot even perform the atomic steps of algorithms carried out by, e.g., a parallel system where every cell updates simultaneously (in contrast to the serial Turing machine), or an enzymatic system (where the atomic steps involve operations such as selective enzyme binding).

Nevertheless, the universal Turing machine is still able to *calculate* the behavior of parallel systems and enzymematic systems. The *algorithmic version of the Church-Turing thesis* states that this is true of *every* algorithmic system. Thus Lewis and Papadimitriou said: “we take the Turing machine to be a precise formal equivalent of the intuitive notion of ‘algorithm’” (1981: 223). David Harel gave the following (famous) formulation of the algorithmic version of the thesis:

> any algorithmic problem for which we can find an algorithm that can be programmed in some programming language, *any* language, … is also solvable by a Turing machine. This statement is one version of the so-called Church/Turing thesis. (Harel 1992: 233)[^harel-1992]

Given the extent to which the concept of an algorithm has evolved since the 1930s—from the step-by-step labors of human computers to the growth of slime mold—interesting questions arise. Will the concept continue to evolve? What are the limits, if any, on this evolution? Could the concept evolve in such that a way that the algorithmic version of the Church-Turing thesis is no longer universally true? Returning to Doyle’s suggestions about equilibrating systems (in Section 5.3.3), Doyle’s claim is essentially that the operation of equilibrating could reasonably be regarded as a basic step of some effective procedures or algorithms—*whether or not* the resulting algorithms satisfy the algorithmic version of the Church-Turing thesis. (See Copeland & Shagrir 2019 for further discussion.)[^copeland-2019]

In summary, the algorithmic version of the Church-Turing thesis is broader than the original thesis, in that Church and Turing considered essentially only a single type of algorithm, effective step-by-step calculations on paper. The algorithmic version is also perhaps less secure than the original thesis.

### 6.2 Computational complexity: the Extended Church-Turing thesis

The Turing machine now holds a central place not only in computability theory but also in complexity theory. Quantum computation researchers Bernstein and Vazirani say:

> Just as the theory of computability has its foundations in the Church-Turing thesis, computational complexity theory rests upon a modern strengthening of this thesis. (Bernstein & Vazirani 1997: 1411)[^bernstein-1997]

There are in fact two different complexity-theoretic versions of the Church-Turing thesis in the modern computer science literature. Both are referred to as the “Extended Church-Turing thesis”. The first was presented by Yao in 2003:

> The *Extended Church-Turing Thesis (ECT)* makes the … assertion that the Turing machine model is also as efficient as any computing device can be. That is, if a function is computable by some hardware device in time $T(n)$ for input of size $n$, then it is computable by a Turing machine in time $(T(n))^k$ for some fixed $k$ (dependent on the problem). (Yao 2003: 100–101)[^yao-2003]

Yao points out that ECT has a powerful implication:

> at least in principle, to make future computers more efficient, one only needs to focus on improving the implementation technology of present-day computer designs. (2003: 101)

Unlike the original Church-Turing thesis (whose status is “something between” a theorem and a definition) ECT is neither a logico-mathematical theorem nor a definition. If it is true, then its truth is a consequence of the laws of physics—and it might not be true. (Although it is trivial if, contrary to a standard but unproved assumption in computer science, P = NP.)

The second complexity-theoretic version of the thesis involves the concept of a *probabilistic Turing machine* (due to Rabin & Scott 1959)[^rabin-1959]. Vazirani and Aharonov state the thesis:

> [T]he extended Church-Turing thesis … asserts that any reasonable computational model can be simulated efficiently by the standard model of classical computation, namely, a probabilistic Turing machine. (Aharonov & Vazirani 2013: 329)[^aharonov-2013]

These two related theses differ considerably from the original Church-Turing thesis, not least in that both extended theses are *empirical* hypotheses. Moreover, there is ongoing debate as to whether quantum computers in fact falsify these theses. (For an introduction to this debate see Copeland & Shagrir 2019, and for a more detailed treatment see Aharonov & Vazirani 2013.)[^aharonov-2013][^copeland-2019]

### 6.3 Brain simulation and the Church-Turing thesis

It is sometimes said that the Church-Turing thesis has implications concerning the scope of computational simulation. For example, Searle writes:

> Can the operations of the brain be simulated on a digital computer? … The answer seems to me … demonstrably “Yes” … That is, naturally interpreted, the question means: Is there some description of the brain such that under that description you could do a computational simulation of the operations of the brain. But given Church’s thesis that anything that can be given a precise enough characterization as a set of steps can be simulated on a digital computer, it follows trivially that the question has an affirmative answer. (Searle 1992: 200)[^searle-1992]

Another example:

> we can depend on there being a Turing machine that captures the functional relations of the brain,

for so long as

> these relations between input and output are functionally well-behaved enough to be describable by … mathematical relationships … we know that some specific version of a Turing machine will be able to mimic them. (Guttenplan 1994: 595)[^guttenplan-1994]

Andréka, Németi and Németi state a more general thesis about the power of Turing machines to simulate other systems:

> [T]he Physical Church-Turing Thesis … is the conjecture that whatever physical computing device (in the broader sense) or physical thought-experiment will be designed by any future civilization, it will always be simulateable by a Turing machine. (Andréka, Németi, & Németi 2009: 500)[^andréka-2009]

Andréka, Németi, and Németi even say that the thesis they state here “was formulated and generally accepted in the 1930s” (ibid.).

Yet it was *not* a thesis about the simulation of physical systems that Church and Turing formulated in the 1930s, but rather a completely different thesis concerning human computation—and it was the latter thesis that became generally accepted during the 1930s and 1940s.

It certainly muddies the waters to call a thesis about simulation “Church’s thesis” or the “Church-Turing thesis”, because the arguments that Church and Turing used to support their actual theses go no way at all towards supporting the theses set out in the several quotations above. Nevertheless, what can be termed the “Simulation thesis” has its place in the present catalogue of modern forms of the Church-Turing thesis:

> **Simulation thesis**:
> Any system whose operations can be characterized as a set of steps (Searle) or whose input-output relations are describable by mathematical relationships (Guttenplan) can be simulated by a Turing machine.

If the Simulation thesis is intended to cover all possible systems then it is surely false, since Doyle’s envisaged equilibrating systems falsify it (Section 5.3.3). If, on the other hand, the thesis is intended to cover only actual physical systems, including brains, then the Simulation thesis is, like the Extended Church-Turing thesis, an *empirical* thesis—and so is very different from Turing’s thesis and Church’s thesis. The truth of the “actual physical systems” version of the Simulation thesis depends on the laws of physics.

One potential objection that any upholder of the Simulation thesis will need to confront parallels a difficulty that Gandy raised for Thesis M (Section 5.1). Physical systems that are not discrete—such as Gandy’s “essentially analogue machines”—appear to falsify the Simulation thesis, since the variables of a system with continuous dynamics take arbitrary real numbers as their values, whereas a Turing machine is restricted to *computable* real numbers, and so cannot fully simulate the continuous system.

This brings the discussion squarely to one of the most interesting topics in the area, so-called “physical versions” of the Church-Turing thesis.

### 6.4 The Church-Turing thesis and physics

#### 6.4.1 The Deutsch-Wolfram thesis

In 1985, Wolfram formulated a thesis that he described as “a physical form of the Church-Turing hypothesis”:

> [U]niversal computers are as powerful in their computational capacities as any physically realizable system can be, so that they can simulate any physical system. (Wolfram 1985: 735)[^wolfram-1985]

Deutsch (who laid the foundations of quantum computation) independently stated a similar thesis, again in 1985, and also described it as a “physical version” of the Church-Turing thesis:

> I can now state the physical version of the Church-Turing principle: “Every finitely realizable physical system can be perfectly simulated by a universal model computing machine operating by finite means”. This formulation is both better defined and more physical than Turing’s own way of expressing it. (Deutsch 1985: 99)[^deutsch-1985]

This thesis is certainly “more physical” than Turing’s thesis. It is, however, a completely *different* claim from Turing’s own, so it is potentially confusing to present it as a “better defined” version of what Turing said. As already emphasized, Turing was talking about *effective methods*, whereas the theses presented by Deutsch and Wolfram concern all (finitely realizable) physical systems—no matter whether or not the system’s activity is effective.

In the wake of this early work by Deutsch and Wolfram, the phrases “physical form of the Church-Turing thesis”, “physical version of the Church-Turing thesis”—and even “*the* physical Church-Turing thesis”—are now quite common in the current literature. However, such terms are probably better avoided, since these physical theses are very distant from Turing’s thesis and Church’s thesis.

In his 1985 paper, Deutsch went on to point out that if the description “a universal model computing machine operating by finite means” is replaced in his physical thesis by “a universal Turing machine”, then the result:

> Every finitely realizable physical system can be perfectly simulated by a universal Turing machine

is not true. His reason for saying so is the point discussed at the end of Section 6.3, concerning non-discrete physical systems. Deutsch argued that a universal Turing machine “cannot perfectly simulate any classical dynamical system”, since “[o]wing to the continuity of classical dynamics, the possible states of a classical system necessarily form a continuum”, whereas the universal Turing machine is a discrete system (Deutsch 1985: 100)[^deutsch-1985]. Deutsch then went on to introduce the important concept of a universal quantum computer, saying (but without proof) that this is “capable of perfectly simulating every finite, realizable physical system” (1985: 102).

The following formulation differs in its details from both Wolfram’s and Deutsch’s theses, but arguably captures the spirit of both. In view of the Deutsch-Gandy point about continuous systems, the idea of perfect simulation is replaced by the concept of simulation *to any desired degree of accuracy*:

> **Deutsch-Wolfram Thesis**:
> Every finite physical system can be simulated to any specified degree of accuracy by a universal Turing machine. (Copeland & Shagrir 2019)[^copeland-2019]

Related physical theses were advanced by Earman 1986, Pour-El and Richards 1989, Pitowsky 1990, Blum et al. 1998, and others. The Deutsch-Wolfram thesis is closely related to Gandy’s Thesis M, and to the weak maximality thesis (Section 5.4). In fact the Deutsch-Wolfram thesis entails the latter (but not vice versa, since the maximality thesis concerns only *machines*, whereas the Deutsch-Wolfram thesis concerns the behavior of *all* finite physical systems—although any who think that every finite physical system is a computing machine will disagree; see e.g., Pitowsky 1990).

Is the Deutsch-Wolfram thesis true? This is an open question (Copeland & Shagrir 2020)[^copeland-2020]—so too for the weak maximality thesis. One focus of debate is whether physical *randomness*, if it exists, falsifies these theses (Calude et al. 2010; Calude & Svozil 2008; Copeland 2000)[^calude-2008][^calude-2010][^copeland-2000]. But even in the case of non-random systems, speculation stretches back over at least six decades that there may be real physical processes (and so, potentially, machine-operations) whose behavior is neither computable nor approximable by a universal Turing machine. See, for example, Scarpellini 1963, Pour-El and Richards 1979, 1981, Kreisel 1967, 1974, 1982, Geroch and Hartle 1986, Pitowsky 1990, Stannett 1990, da Costa and Doria 1991, 1994, Hogarth 1994, Siegelmann and Sontag 1994, Copeland and Sylvan 1999, Kieu 2004, 2006 (see Other Internet Resources), Penrose 1994, 2011, 2016.

To select, by way of example, just one paper from this list: Pour-El and Richards showed in their 1981 article that a system evolving from computable initial conditions in accordance with the familiar three-dimensional wave equation is capable of exhibiting behavior that falsifies the Deutsch-Wolfram thesis. However, now as then, it is an open question whether these initial conditions are physically possible.

#### 6.4.2 The “Gandy argument”

Gandy (1980)[^gandy-1980] gave a profound discussion of whether there could be deterministic, discrete systems whose behavior cannot be calculated by a universal Turing machine. The now famous “Gandy argument” aims to show that, given certain reasonable physical assumptions, the behavior of *every* discrete deterministic mechanism is calculable by Turing machine. In some respects, the Gandy argument resembles and extends Turing’s argument I, and Gandy regarded it as an improved and more general alternative to Turing’s I (1980: 145). He emphasized that (unlike Turing’s argument), his argument takes “parallel working into account” (1980: 124–5); and it is this that accounts for much of the additional complexity of Gandy’s analysis as compared to Turing’s.

Gandy viewed the conclusion of his argument (that the behavior of every discrete deterministic mechanism is calculable by Turing machine) as relatively *a priori*, provable on the basis of a set-theoretic derivation that makes very general physical assumptions (namely, the four axioms mentioned in Section 3.4). These assumptions include, for instance, a lower bound on the dimensions of a mechanism’s components, and an upper bound on the speed of propagation of effects and signals. (The argument aims to cover only mechanisms obeying the principles of Relativity.) Gandy expressed his various physical assumptions set-theoretically, by means of precise axioms, which he called Principles I – IV. Principle III, for example, captures the idea that there is a bound on the number of types of basic parts (atoms) from which the states of the machine are uniquely assembled; and Principle IV—which Gandy called the “principle of local causation”—captures the idea that each state-transition must be determined by the *local environments* of the parts of the mechanism that change in the transition.

Gandy was very clear that his argument does not apply to continuous systems—analogue machines, as he called them—and non-relativistic systems. (Extracts from unpublished work by Gandy, in which he attempted to develop a companion argument for analogue machines, are included in Copeland & Shagrir 2007.)[^copeland-2007] However, the scope of the Gandy argument is also limited in other ways, not noted by Gandy himself. For example, some asynchronous algorithms fall outside the scope of Gandy’s principles (Gurevich 2012; Copeland & Shagrir 2007)[^copeland-2007][^gurevich-2012]. Gurevich concludes that Gandy has not shown “that his axioms are satisfied by all discrete mechanical devices”, and Shagrir says there is no “basis for claiming that Gandy characterized finite machine computation” (Gurevich 2012: 36, Shagrir 2002: 234)[^gurevich-2012][^shagrir-2002]. It will be useful to give some examples of discrete deterministic systems that, in one way or another, evade Gandy’s conclusion that the behavior of every such system is calculable by Turing machine.

First, it is relatively trivial that mechanisms *satisfying* Gandy’s four principles may nevertheless produce uncomputable output from computable input if embedded in a universe whose physical laws have Turing-uncomputability built into them, e.g., via a temporal variable (Copeland & Shagrir 2007)[^copeland-2007]. Moreover, some asynchronous algorithms fall outside the scope of Gandy’s principles (Gurevich 2012; Copeland & Shagrir 2007)[^copeland-2007][^gurevich-2012]. Second, certain (notional) discrete deterministic “relativistic computers” also fall outside the scope of Gandy’s principles. Relativistic computers were described in a 1987 lecture by Pitowsky (Pitowsky 1990), and in Hogarth 1994 and Etesi & Németi 2002. The idea is outlined in the entry on computation in physical systems; for further discussion see Shagrir and Pitowsky 2003, Copeland and Shagrir 2020.

The Németi relativistic computer makes use of gravitational time-dilation effects in order to compute (in a broad sense) a function that provably cannot be computed by a universal Turing machine (e.g., the halting function). Németi and his colleagues emphasize that the Németi computer is “not in conflict with presently accepted scientific principles” and that, in particular, “the principles of quantum mechanics are not violated”. They suggest moreover that humans might “even build” a relativistic computer “sometime in the future” (Andréka, Németi, & Németi 2009: 501)[^andréka-2009].

According to Gandy,

1. “A discrete deterministic mechanical device satisfies principles I-IV” (he called this “Thesis P”; Gandy 1980: 126)[^gandy-1980], and
2. “What can be calculated by a device satisfying principles I-IV is computable” (he labelled this “Theorem”).

1 and 2 together yield: *What can be calculated by a discrete deterministic mechanical device is (Turing-machine) computable*.

However, the Németi computer is a discrete, deterministic mechanical device, and yet is able to calculate functions that are not Turing-machine computable. That is to say, relativistic computers are counterexamples to Gandy’s Thesis P. In brief, the reason for this is that the sense of “deterministic” implicitly specified in Gandy’s Principles (“Gandy-deterministic”) is narrower than the intuitive sense of “deterministic”, where a deterministic system is one obeying laws that involve no randomness or stochasticity. Relativistic computers are deterministic but not Gandy-deterministic. (For a fuller discussion, see Copeland, Shagrir, & Sprevak 2018.)[^copeland-2018]

In conclusion, Gandy’s analysis has made a considerable contribution to the current understanding of machine computation. But, important and illuminating though the Gandy argument is, it certainly does not settle the question whether the Deutsch-Wolfram thesis is true.

#### 6.4.3 Quantum effects and the “Total” thesis

There is a stronger form of the Deutsch-Wolfram thesis, dubbed the “Total thesis” in Copeland and Shagrir 2019.

> **The Total Thesis**:
> Every physical aspect of the behavior of any physical system can be calculated (to any specified degree of accuracy) by a universal Turing machine.

Logically, the Total thesis is counter-exampled by the universal Turing machine itself (assuming that the universal machine, with its indefinitely long tape, is at least a notional physical system; see Copeland & Shagrir 2020 for discussion of this assumption)[^copeland-2020]. This is because there is no algorithm for calculating whether a universal Turing machine halts on every given input—i.e., there is no algorithm for calculating that aspect of the machine’s behavior. The question remains, however, whether the Total thesis is infringed by any systems that are “more physical” than the universal machine. (Notice that such systems, if any exist, do not necessarily also infringe the Deutsch-Wolfram thesis, since it is possible that, even though answers to certain physical questions about the system are uncomputable, the system is nevertheless able to be simulated by a Turing machine.)

Interestingly, recent work in condensed matter quantum physics indicates that—possibly—quantum many-body systems could infringe the Total thesis. In 2012, Eisert, Müller and Gogolin established the surprising result that

> the very natural physical problem of determining whether certain outcome sequences cannot occur in repeated quantum measurements is undecidable, even though the same problem for classical measurements is readily decidable. (Eisert, Müller & Gogolin 2012: 260501.1)[^eisert-2012]

This was a curtain-raiser to a series of dramatic results about the uncomputability of quantum phase transitions, by Cubitt and his group (Cubitt, Perez-Garcia, & Wolf 2015; Bausch, Cubitt, Lucia, & Perez-Garcia 2020; Bausch, Cubitt, & Watson 2021)[^bausch-2020][^bausch-2021][^cubitt-2015]. These results concern the “spectral gap”, an important determinant of the properties of a substance. A quantum many-body system is said to be “gapped” if the system has a well-defined next least energy-level above the system’s ground energy-level, and is said to be “gapless” otherwise (i.e., if the energy spectrum is continuous). The “spectral gap problem” is the problem of determining whether a given many-body system is gapped or gapless.

The uncomputability results of Cubitt et al. stem from their discovery that the halting problem can be encoded in the spectral gap problem. Deciding whether a model system of the type they have studied is gapped or gapless, given a description of the local interactions, is “at least as hard as solving the Halting Problem” (Bausch, Cubitt, & Watson 2021: 2)[^bausch-2021]. Moreover, this is not just a case of *uncomputability in, uncomputability out*. Uncomputability arises even though the initial conditions are computable (as with the notional system described in Pour-El and Richards 1981, mentioned in Section 6.4.1)[^pour-el-1981]. Cubitt et al. emphasize:

> the phase diagram is uncomputable even for *computable* (or even algebraic) values of its parameter $\phi$. Indeed, it is uncomputable at a countably-infinite set of computable (or algebraic) values of $\phi$. (Bausch, Cubitt, & Watson 2019: 8)[^bausch-2019]

However, Cubitt admits that the models used in the proofs are somewhat artificial:

> Whether the results can be extended to more natural models is yet to be determined. (Cubitt, Perez-Garcia & Wolf 2015: 211)[^cubitt-2015]

In short, it is an open—and fascinating—question whether there are realistic physical systems that fail to satisfy the Total thesis.

## 7. Some Key Remarks by Turing and Church

### 7.1 Turing machines

Turing prefaced his first description of a Turing machine with the words:

> We may compare a man in the process of computing a … number to a machine. (Turing 1936 [2004: 59])[^turing-1936]

The Turing machine is a model, idealized in certain respects, of a *human being* calculating in accordance with an effective method.

Wittgenstein put this point in a striking way:

> Turing’s “Machines”. These machines are *humans* who calculate. (Wittgenstein 1947 [1980: 1096])[^wittgenstein-1947]

It is a point that Turing was to emphasize, in various forms, again and again. For example:

> A man provided with paper, pencil, and rubber, and subject to strict discipline, is in effect a universal machine. (Turing 1948 [2004: 416])[^turing-1948]

In order to understand Turing’s “On Computable Numbers” and later texts, it is essential to keep in mind that when he used the words “computer”, “computable” and “computation”, he employed them not in their modern sense as pertaining to machines, but as pertaining to human calculators. For example:

> Computers always spend just as long in writing numbers down and deciding what to do next as they do in actual multiplications, and it is just the same with ACE [the Automatic Computing Engine] … [T]he ACE will do the work of about 10,000 computers … Computers will still be employed on small calculations … (Turing 1947 [2004: 387, 391])[^turing-1947]

Turing’s ACE, an early electronic stored-program digital computer, was built at the National Physical Laboratory, London; a pilot version—at the time the fastest functioning computer in the world—first ran in 1950, and a commercial model, the DEUCE, was marketed very successfully by English Electric.

### 7.2 Human computation and machine computation

The electronic stored-program digital computers for which the universal Turing machine was a blueprint are, each of them, computationally equivalent to a Turing machine, and so they too are, in a sense, models of human beings engaged in computation. Turing chose to emphasize this when explaining these electronic machines in a manner suitable for an audience of uninitiates:

> The idea behind digital computers may be explained by saying that these machines are intended to carry out any operations which could be done by a human computer. (Turing 1950a [2004: 444])[^turing-1950a]

He made the point a little more precisely in the technical document containing his design for the ACE:

> The class of problems capable of solution by the machine [the ACE] can be defined fairly specifically. They are [a subset of] those problems which can be solved by human clerical labour, working to fixed rules, and without understanding. (Turing 1945 [2005: 386])[^turing-1945]

Turing went on to *characterize* this subset in terms of the amount of paper and time available to the human clerk.

It was presumably because he considered the point to be essential for understanding the nature of the new electronic machines that he chose to begin his *Programmers’ Handbook for Manchester Electronic Computer Mark II* with this explanation:

> Electronic computers are intended to carry out any definite rule of thumb process which could have been done by a human operator working in a disciplined but unintelligent manner. (Turing *c*1950: 1)[^turing-1950]

It was not some deficiency of imagination that led Turing to model his L.C.M.s on what could be achieved by a *human* computer. The purpose for which he invented the Turing machine demanded it. The *Entscheidungsproblem* is the problem of finding a *humanly executable* method of a certain sort, and, as was explained earlier, Turing’s aim was to show that there is no such method in the case of the full first-order predicate calculus.

### 7.3 Church and the human computer

Turing placed the human computer center stage in his 1936 paper. Not so Church. Church did not mention computation or human computers explicitly in either of his two groundbreaking papers on the *Entscheidungsproblem* (Church 1936a,b)[^church-1936a]. He spoke of “effective calculability”, taking it for granted his readers would understand this term to be referring to *human* calculation. He also used the term “effective method”, again taking it for granted that readers would understand him to be speaking of a humanly executable method.

Church also used the term “algorithm”, saying

> It is clear that for any recursive function of positive integers there exists an algorithm using which any required particular value of the function can be effectively calculated. (Church 1936a: 351)[^church-1936a]

He said further that the notion of effective calculability could be spelled out as follows:

> by defining a function to be effectively calculable if there exists an algorithm for the calculation of its values. (Church 1936a: 358)[^church-1936a]

It was in Church’s review of Turing’s 1936 paper that he brought the human computer out of the shadows. He wrote:

> [A] human calculator, provided with pencil and paper and explicit instructions, can be regarded as a kind of Turing machine. It is thus immediately clear that computability, so defined [i.e., computability by a Turing machine], can be identified with (especially, is no less general than) the notion of effectiveness as it appears in certain mathematical problems … and in general any problem which concerns the discovery of an algorithm. (Church 1937a: 43)[^church-1937a]

### 7.4 Turing’s use of “machine”

It is important to note that, when Turing used the word “machine”, he often meant not machine-in-general but, as we would now say, Turing machine. At one point he explicitly drew attention to this usage:

> The expression “machine process” of course means one which could be carried out by the type of machine I was considering [in “On Computable Numbers”]. (Turing 1947 [2004: 378–9])[^turing-1947]

Thus when, a few pages later, Turing asserted that “machine processes and rule of thumb processes are synonymous” (1947 [2004: 383]), he is to be understood as advancing the Church-Turing thesis (and its converse), not a version of the maximality thesis. Unless his intended usage is borne in mind, misunderstanding could ensue. Especially liable to mislead are statements like the following, which a casual reader might mistake for a formulation of the maximality thesis:

> The importance of the universal machine is clear. We do not need to have an infinity of different machines doing different jobs. A single one will suffice. The engineering problem of producing various machines for various jobs is replaced by the office work of “programming” the universal machine to do these jobs. (Turing 1948 [2004: 414])[^turing-1948]

In context it is perfectly clear that these remarks concern machines equivalent to Turing machines; the passage is embedded in a discussion of L.C.M.s.

Whether or not Turing would, if queried, have assented to the weak maximality thesis is unknown. There is certainly no textual evidence in favor of the view that he did so assent. The same is true of the Deutsch-Wolfram thesis and its cognates: there is no textual evidence that Turing would have assented to any such thesis.

### 7.5 Church’s version of Turing’s thesis

Interestingly, the summary of Turing’s account of computability given by Church in his 1937 review was not entirely correct. Church said:

> The author [Turing] proposes as a criterion that an infinite sequence of digits 0 and 1 be “computable” that it shall be possible to devise a computing machine, occupying a finite space and with working parts of a finite size, which will write down the sequence to any desired number of terms if allowed to run for a sufficiently long time. (Church 1937a: 42)[^church-1937a]

However, there was no requirement proposed in Turing’s 1936 paper that Turing machines occupy “a finite space” or have “working parts of a finite size”. Nor did Turing couch matters in terms of the machine’s writing down “any desired number of terms” of the sequence, “if allowed to run for a sufficiently long time”. Turing said, on the contrary, that a sequence is “computable if it can be computed by a circle-free machine” (Turing 1936 [2004: 61])[^turing-1936]; where a machine is circle-free if it is *not* one that

> never writes down more than a finite number of symbols [0s and 1s]. (Turing 1936 [2004: 60])[^turing-1936]

In consequence, Church’s version of Turing’s thesis is subtly different from Turing’s own:

> **Church’s Turing’s thesis**:
> An infinite sequence of digits is “computable” if (and only if) it is possible to devise a computing machine, occupying a finite space and with working parts of a finite size, that will write down the sequence to any desired number of terms if allowed to run for a sufficiently long time.

In so far as Church includes these three finiteness requirements (i.e., that the machine occupy a finite space, have finite-sized parts, and produce finite numbers of digits), his version of Turing’s thesis can perhaps be said to be “more physical” than any of Turing’s formulations of the thesis. Church’s finiteness requirements are in some respects reminiscent of Gandy’s idea that the states of a discrete deterministic calculating machine must be built up iteratively from a bounded number of types of basic components, the dimensions of which have a lower bound (see Section 6.4.2). Although, as explained there, Gandy imposes further requirements on a discrete deterministic calculating machine, and these go far beyond Church’s finiteness requirements.

Notwithstanding Church’s efforts to inject additional physical realism into the concept of a Turing machine, it is—as in Turing’s case—unknown whether Church would, if queried, have assented to the Deutsch-Wolfram thesis or any cognate thesis. There seems to be no textual evidence either way. Church was simply silent about such matters.

> Supplementary Document: [The Rise and Fall of the *Entscheidungsproblem*](church-turing.decision-problem.md).

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=church-turing). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/church-turing/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=church-turing&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/church-turing/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- [The Turing Archive for the History of Computing](http://www.alanturing.net/)
- Kieu, Tien D., 2006, “[Reply to Andrew Hodges](https://arxiv.org/pdf/quant-ph/0602214v2.pdf)”, arXiv:quant-ph/0602214v2.

## Related Entries

Church, Alonzo | computability and complexity | computation: in physical systems | computer science, philosophy of | computing: modern history of | Gödel, Kurt: incompleteness theorems | Llull, Ramon | mind: computational theory of | Turing, Alan | Turing machines

[^ackermann-1928]: Ackermann, Wilhelm, 1928, “Zum Hilbertschen Aufbau der reellen Zahlen”, *Mathematische Annalen*, 99(1): 118–133. doi:10.1007/BF01459088

[^aharonov-2013]: Aharonov, Dorit and Umesh V. Vazirani, 2013, “Is Quantum Mechanics Falsifiable? A Computational Perspective on the Foundations of Quantum Mechanics”, in Copeland, Posy, and Shagrir 2013: 329–349 (ch. 11).

[^andréka-2009]: Andréka, Hajnal, István Németi, and Péter Németi, 2009, “General Relativistic Hypercomputing and Foundation of Mathematics”, *Natural Computing*, 8(3): 499–516. doi:10.1007/s11047-009-9114-3

[^baldwin-1902]: Baldwin, J. Mark, 1902, “Logical Machine”, in J. Mark Baldwin (ed.), *Dictionary of Philosophy and Psychology*, volume 2, New York: Macmillan, 28–30.

[^barendregt-1997]: Barendregt, Henk, 1997, “The Impact of the Lambda Calculus in Logic and Computer Science”, *Bulletin of Symbolic Logic*, 3(2): 181–215. doi:10.2307/421013

[^barrett-2005]: Barrett, Lindsay and Matthew Connell, 2005, “Jevons and the Logic ‘Piano’”, *The Rutherford Journal*, 1: article 3. [[Barrett & Connell 2005 available online](http://www.rutherfordjournal.org/article010103.html)]

[^barwise-1977]: Barwise, Jon, 1977, “An Introduction to First-Order Logic”, in Jon Barwise (ed.), *Handbook of Mathematical Logic*, Amsterdam: North-Holland, 5–46.

[^bausch-2020]: Bausch, Johannes, Toby S. Cubitt, Angelo Lucia, and David Perez-Garcia, 2020, “Undecidability of the Spectral Gap in One Dimension”, *Physical Review X*, 10(3): 031038. doi:10.1103/PhysRevX.10.031038

[^bausch-2019]: Bausch, Johannes, Toby S. Cubitt, and James D. Watson, 2019, “Uncomputability of Phase Diagrams”, arXiv:1910.01631.

[^bausch-2021]: –––, 2021, “Uncomputability of Phase Diagrams”, *Nature Communications*, 12(1): article 452. doi:10.1038/s41467-020-20504-6

[^behmann-1921]: Behmann, Heinrich, 1921 [2015], “Entscheidungsproblem und Algebra der Logik”, Lecture, 10 May 1921, to the Göttingen Mathematical Society. In Mancosu and Zach 2015: 177–187, with a partial translation by Richard Zach in the same (2015: 173–177).

[^behmann-1922]: –––, 1922, “Beiträge zur Algebra der Logik, insbesondere zum Entscheidungsproblem”, *Mathematische Annalen*, 88(1–2): 168–168. doi:10.1007/BF01448447

[^bernays-1918]: Bernays, Paul, 1918, “Beiträge zur axiomatischen Behandlung des Logik-Kalküls”, Habilitationsschrift, University of Göttingen. Bernays Papers, ETH Zurich (Hs 973.192).

[^bernays-1928]: Bernays, Paul and Moses Schönfinkel, 1928, “Zum Entscheidungsproblem der mathematischen Logik”, *Mathematische Annalen*, 99(1): 342–372. doi:10.1007/BF01459101

[^bernstein-1997]: Bernstein, Ethan and Umesh Vazirani, 1997, “Quantum Complexity Theory”, *SIAM Journal on Computing*, 26(5): 1411–1473. doi:10.1137/S0097539796300921

[^blum-1998]: Blum, Lenore, Felipe Cucker, Michael Shub, and Steve Smale, 1998, *Complexity and Real Computation*, New York: Springer. doi:10.1007/978-1-4612-0701-6

[^boolos-1974]: Boolos, George and Richard C. Jeffrey, 1974, *Computability and Logic*, New York: Cambridge University Press.

[^buss-2001]: Buss, Samuel R., Alexander S. Kechris, Anand Pillay, and Richard A. Shore, 2001, “The Prospects for Mathematical Logic in the Twenty-First Century”, *Bulletin of Symbolic Logic*, 7(2): 169–196. doi:10.2307/2687773

[^calude-2008]: Calude, Cristian S. and Karl Svozil, 2008, “Quantum Randomness and Value Indefiniteness”, *Advanced Science Letters*, 1(2): 165–168. doi:10.1166/asl.2008.016

[^calude-2010]: Calude, Cristian S., Michael J. Dinneen, Monica Dumitrescu, and Karl Svozil, 2010, “Experimental Evidence of Quantum Randomness Incomputability”, *Physical Review A*, 82(2): 022102. doi:10.1103/PhysRevA.82.022102

[^cantor-1874]: Cantor, Georg, 1874, “Ueber eine Eigenschaft des Inbegriffs aller reellen algebraischen Zahlen”, *Journal für die reine und angewandte Mathematik*, 77: 258–262. doi:10.1515/crll.1874.77.258

[^carnap-1935]: Carnap, Rudolf, 1935, “Ein Gültigkeitskriterium für die Sätze der klassischen Mathematik”, *Monatshefte für Mathematik und Physik*, 42: 163–190. doi:10.1007/BF01733289

[^cassirer-1929]: Cassirer, Ernst, 1929, *Philosophie der symbolischen Formen* (Volume 3: *Phänomenologie der Erkenntnis*), Berlin: Bruno Cassirer.

[^church-1932]: Church, Alonzo, 1932, “A Set of Postulates for the Foundation of Logic”, *Annals of Mathematics*, second series 33(2): 346–366. doi:10.2307/1968337

[^church-1933]: –––, 1933, “A Set of Postulates For the Foundation of Logic (2)”, *Annals of Mathematics*, second series 34(4): 839–864. doi:10.2307/1968702

[^church-1935a]: –––, 1935a, “An Unsolvable Problem of Elementary Number Theory, Preliminary Report” (abstract), *Bulletin of the American Mathematical Society*, 41(6): 332–333. Full paper in Church 1936b.

[^church-1935b]: –––, 1935b, letter to Kleene, 29 November 1935. Excerpt in Davis 1982: 9.

[^church-1935c]: –––, 1935c, “A Proof of Freedom from Contradiction”, *Proceedings of the National Academy of Sciences*, 21(5): 275–281. doi:10.1073/pnas.21.5.275

[^church-1936a]: –––, 1936a, “An Unsolvable Problem of Elementary Number Theory”, *American Journal of Mathematics*, 58(2): 345–363. doi:10.2307/2371045

[^church-1936b]: –––, 1936b, “A Note on the Entscheidungsproblem”, *The Journal of Symbolic Logic*, 1(1): 40–41. doi:10.2307/2269326

[^church-1937a]: –––, 1937a, Review of Turing 1936, *The Journal of Symbolic Logic*, 2(1): 42–43. doi:10.1017/S002248120003958X

[^church-1937b]: –––, 1937b, Review of Post 1936, *The Journal of Symbolic Logic*, 2(1): 43. doi:10.1017/S0022481200039591

[^church-1941]: –––, 1941, *The Calculi of Lambda-Conversion*, Princeton, NJ: Princeton University Press.

[^church-1936]: Church, Alonzo and J. Barkley Rosser, 1936, “Some Properties of Conversion”, *Transactions of the American Mathematical Society*, 39(3): 472–482. doi:10.1090/S0002-9947-1936-1501858-0

[^copeland-1998a]: Copeland, B. Jack, 1998a, “Even Turing Machines Can Compute Uncomputable Functions”, in *Unconventional Models of Computation, Proceedings of the 1st International Conference, New Zealand*, Christian S. Calude, John Casti, and Michael J. Dinneen (eds), London: Springer-Verlag, 150–164.

[^copeland-1998b]: –––, 1998b, “Super Turing-Machines”, *Complexity*, 4(1): 30–32. doi:10.1002/(SICI)1099-0526(199809/10)4:1<30::AID-CPLX9>3.0.CO;2-8

[^copeland-2000]: –––, 2000, “Narrow versus Wide Mechanism: Including a Re-Examination of Turing’s Views on the Mind-Machine Issue”, *The Journal of Philosophy*, 97(1): 5–32. doi:10.2307/2678472

[^copeland-2002a]: –––, 2002a, “Accelerating Turing Machines”, *Minds and Machines*, 12(2): 281–300. (In a special issue on the Church-Turing thesis, edited by Carol Cleland.) doi:10.1023/A:1015607401307

[^copeland-2004]: ––– (ed.), 2004, *The Essential Turing: Seminal Writings in Computing, Logic, Philosophy, Artificial Intelligence, and Artificial Life*, Oxford: Clarendon Press. doi:10.1093/oso/9780198250791.001.0001

[^copeland-2022]: Copeland, B. Jack and Zhao Fan, 2022, “Did Turing Stand on Gödel’s Shoulders?”, *The Mathematical Intelligencer*, 44: 308–319. doi:10.1007/s00283-022-10177-y

[^copeland-2023]: –––, 2023, “Turing and von Neumann: From Logic to the Computer”, *Philosophies*, 8(2): 1–30.

[^copeland-2013]: Copeland, B. Jack, Carl J. Posy, and Oron Shagrir (eds), 2013, *Computability: Turing, Gödel, Church, and Beyond*, Cambridge, MA: The MIT Press.

[^copeland-2007]: Copeland, B. Jack and Oron Shagrir, 2007, “Physical Computation: How General Are Gandy’s Principles for Mechanisms?”, *Minds and Machines*, 17(2): 217–231. doi:10.1007/s11023-007-9058-2

[^copeland-2011]: –––, 2011, “Do Accelerating Turing Machines Compute the Uncomputable?”, *Minds and Machines*, 21(2): 221–239. doi:10.1007/s11023-011-9238-y

[^copeland-2013-2]: –––, 2013, “Turing versus Gödel on Computability and the Mind”, in Copeland, Posy, and Shagrir 2013: 1–33 (ch. 1).

[^copeland-2019]: –––, 2019, “The Church-Turing Thesis: Logical Limit or Breachable Barrier?”, *Communications of the ACM*, 62(1): 66–74. doi:10.1145/3198448

[^copeland-2020]: –––, 2020, “Physical Computability Theories”, in *Quantum, Probability, Logic: The Work and Influence of Itamar Pitowsky*, Meir Hemmo and Orly Shenker (eds), Cham: Springer: 217–231.

[^copeland-2018]: Copeland, B. Jack, Oron Shagrir, and Mark Sprevak, 2018, “Zuse’s Thesis, Gandy’s Thesis, and Penrose’s Thesis”, in *Physical Perspectives on Computation, Computational Perspectives on Physics*, Michael E. Cuffaro and Samuel C. Fletcher (eds), Cambridge: Cambridge University Press, 39–59. doi:10.1017/9781316759745.003

[^copeland-1999]: Copeland, B. Jack and Richard Sylvan, 1999, “Beyond the Universal Turing Machine”, *Australasian Journal of Philosophy*, 77(1): 46–66. doi:10.1080/00048409912348801

[^couturat-1903]: Couturat, Louis (ed.), 1903, *Opuscules et Fragments Inédits de Leibniz*, Paris: Alcan. Facsimile of the 1903 edition, Hildesheim: G. Olms, 1961.

[^cubitt-2015]: Cubitt, Toby S., David Perez-Garcia, and Michael M. Wolf, 2015, “Undecidability of the Spectral Gap”, *Nature*, 528(7581): 207–211. doi:10.1038/nature16059

[^curry-1929]: Curry, Haskell B., 1929, “An Analysis of Logical Substitution”, *American Journal of Mathematics*, 51(3): 363–384. doi:10.2307/2370728

[^curry-1930a]: –––, 1930a, “Grundlagen der kombinatorischen Logik, Teil 1”, *American Journal of Mathematics*, 52(3): 509–536. doi:10.2307/2370619

[^curry-1930b]: –––, 1930b, “Grundlagen der kombinatorischen Logik, Teil 2”, *American Journal of Mathematics*, 52(4): 789–834. doi:10.2307/2370716

[^curry-1932]: –––, 1932, “Some Additions to the Theory of Combinators”, *American Journal of Mathematics*, 54(3): 551–558. doi:10.2307/2370900

[^curry-1958]: Curry, Haskell B. and Robert Feys, 1958, *Combinatory Logic*, Amsterdam: North-Holland.

[^costa-1991]: da Costa, Newton C. A. and Francisco A. Doria, 1991, “Classical Physics and Penrose’s Thesis”, *Foundations of Physics Letters*, 4(4): 363–373. doi:10.1007/BF00665895

[^costa-1994]: –––, 1994, “Undecidable Hopf Bifurcation with Undecidable Fixed Point”, *International Journal of Theoretical Physics*, 33(9): 1885–1903. doi:10.1007/BF00671031

[^davies-2001]: Davies, E. Brian, 2001, “Building Infinite Machines”, *The British Journal for the Philosophy of Science*, 52(4): 671–682. doi:10.1093/bjps/52.4.671

[^davis-1958]: Davis, Martin, 1958, *Computability and Unsolvability*, New York: McGraw-Hill.

[^davis-1965]: ––– (ed.), 1965, *The Undecidable: Basic Papers on Undecidable Propositions, Unsolvable Problems and Computable Functions*, Hewlett, NY: Raven Press.

[^davis-1982]: –––, 1982, “Why Gödel Didn’t Have Church’s Thesis”, *Information and Control*, 54(1–2): 3–24. doi:10.1016/S0019-9958(82)91226-8

[^davis-2015]: Davis, Martin and Wilfried Sieg, 2015, “Conceptual Confluence in 1936: Post and Turing”, in *Turing’s Revolution*, Giovanni Sommaruga and Thomas Strahm (eds), Cham: Birkhäuser, 3–27. doi:10.1007/978-3-319-22156-4_1

[^dawson-2006]: Dawson, John W., 2006, “Gödel and the Origins of Computer Science”, in *Logical Approaches to Computational Barriers*, Arnold Beckmann, Ulrich Berger, Benedikt Löwe, and John V. Tucker (eds), (Lecture Notes in Computer Science 3988), Berlin/Heidelberg: Springer, 133–136. doi:10.1007/11780342_14

[^dedekind-1888]: Dedekind, Richard, 1888, *Was Sind und was Sollen die Zahlen?* Braunschweig: Vieweg.

[^dershowitz-2008]: Dershowitz, Nachum and Yuri Gurevich, 2008, “A Natural Axiomatization of Computability and Proof of Church’s Thesis”, *Bulletin of Symbolic Logic*, 14(3): 299–350. doi:10.2178/bsl/1231081370

[^deutsch-1985]: Deutsch, David, 1985, “Quantum Theory, the Church–Turing Principle and the Universal Quantum Computer”, *Proceedings of the Royal Society of London. Series A. Mathematical and Physical Sciences*, 400(1818): 97–117. doi:10.1098/rspa.1985.0070

[^doyle-1982]: Doyle, Jon, 1982, “What is Church’s Thesis? An Outline”, Laboratory for Computer Science, MIT.

[^doyle-2002]: –––, 2002, “What Is Church’s Thesis? An Outline”, *Minds and Machines*, 12(4): 519–520. doi:10.1023/A:1021126521437

[^earman-1986]: Earman, John, 1986, *A Primer on Determinism*, Dordrecht: Reidel.

[^eisert-2012]: Eisert, Jens, Markus P. Müller, and Christian Gogolin, 2012, “Quantum Measurement Occurrence Is Undecidable”, *Physical Review Letters*, 108(26): 260501 (5 pages). doi:10.1103/PhysRevLett.108.260501

[^engeler-1983]: Engeler, Erwin, 1983 [1993], *Metamathematik der Elementarmathematik*, Berlin: Springer. Translated as *Foundations of Mathematics: Questions of Analysis, Geometry & Algorithmics*, Charles B. Thomas (trans.), Berlin/New York: Springer-Verlag.

[^etesi-2002]: Etesi, Gábor and István Németi, 2002, “Non-Turing Computations via Malament-Hogarth Space-Times”, *International Journal of Theoretical Physics*, 41(2): 341–370. doi:10.1023/A:1014019225365

[^frankena-1964]: Frankena, William and Arthur W. Burks, 1964, “Cooper Harold Langford 1895–1964”, *Proceedings and Addresses of the American Philosophical Association*, 38: 99–101.

[^gandy-1980]: Gandy, Robin, 1980, “Church’s Thesis and Principles for Mechanisms”, in *The Kleene Symposium*, Jon Barwise, H. Jerome Keisler, and Kenneth Kunen (eds), Amsterdam: North-Holland, 123–148. doi:10.1016/S0049-237X(08)71257-6

[^gandy-1988]: –––, 1988, “The Confluence of Ideas in 1936”, in *The Universal Turing Machine: A Half-Century Survey*, Rolf Herken (ed.), New York: Oxford University Press, 51–102.

[^geroch-1986]: Geroch, Robert and James B. Hartle, 1986, “Computability and Physical Theories”, *Foundations of Physics*, 16(6): 533–550. doi:10.1007/BF01886519

[^gödel-1930]: Gödel, Kurt, 1930, “Die Vollständigkeit der Axiome des logischen Funktionenkalküls”, *Monatshefte für Mathematik und Physik*, 37: 349–360. doi:10.1007/BF01696781

[^gödel-1931]: –––, 1931, “Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I”, *Monatshefte für Mathematik und Physik*, 38: 173–198. doi:10.1007/BF01700692

[^gödel-1933]: –––, 1933, “Zum Entscheidungsproblem des logischen Funktionenkalküls”, *Monatshefte für Mathematik und Physik*, 40: 433–443. doi:10.1007/BF01708881

[^gödel-1934]: –––, 1934 [1965], “On Undecidable Propositions of Formal Mathematical Systems”, Lecture notes taken by Stephen Kleene and J. Barkley Rosser at the Institute for Advanced Study, in Davis 1965: 39–74.

[^gödel-1936]: –––, 1936, “Über die Länge von Beweisen”, *Ergebnisse eirtes mathematischen Kolloquiums*, 7: 23–24.

[^gödel-1995]: –––, 193?, “Undecidable Diophantine Propositions”, in Gödel 1995: 164–175.

[^gödel-1946]: –––, 1946, “Remarks Before the Princeton Bicentennial Conference”, in Gödel 1990: 150–153.

[^gödel-1951]: –––, 1951, “Some Basic Theorems on the Foundations of Mathematics and Their Implications”, in Gödel 1995: 304–323.

[^gödel-1965a]: –––, 1965a, “Postscriptum” to Gödel 1934, in Davis 1965: 71–73.

[^gödel-1965b]: –––, 1965b, letter to Davis, 15 February 1965. Excerpt in Davis 1982: 8.

[^gödel-nd]: –––, *Kurt Gödel: Collected Works*, 5 volumes, Solomon Feferman et al. (eds), Oxford: Clarendon Press.

[^gödel-1986]: 1986, *Volume 1: Publications 1929–1936*

[^gödel-1990]: 1990, *Volume 2: Publications 1938–1974*

[^gödel-1995-2]: 1995, *Volume 3: Unpublished Essays and Lectures*

[^gurevich-2012]: Gurevich, Yuri, 2012, “What Is an Algorithm?”, in *SOFSEM 2012: Theory and Practice of Computer Science*, Mária Bieliková, Gerhard Friedrich, Georg Gottlob, Stefan Katzenbeisser, and György Turán (eds), (Lecture Notes in Computer Science 7147), Berlin/Heidelberg: Springer, 31–42. doi:10.1007/978-3-642-27660-6_3

[^guttenplan-1994]: Guttenplan, Samuel D. (ed.), 1994, *A Companion to the Philosophy of Mind*, Oxford/Cambridge, MA: Blackwell Reference. doi:10.1002/9781405164597.

[^hardy-1929]: Hardy, G. H., 1929, “Mathematical Proof”, *Mind*, 38(149): 1–25. doi:10.1093/mind/XXXVIII.149.1

[^harel-1992]: Harel, David, 1992, *Algorithmics: The Spirit of Computing*, second edition, Reading, MA: Addison-Wesley.

[^herbrand-1930a]: Herbrand, Jacques, 1930a, *Recherches sur la Théorie de la Démonstration*, doctoral thesis, University of Paris. In Herbrand 1968.

[^herbrand-1930b]: –––, 1930b, “Les bases de la logique Hilbertienne”, *Revue de Métaphysique et de Morale*, 37(2): 243–255.

[^herbrand-1931a]: –––, 1931a, “Sur le Problème Fondamental de la Logique Mathématique”, *Sprawozdania z Posiedzeń Towarzystwa Naukowego Warszawskiego, Wydział III*, 24: 12–56.

[^herbrand-1931b]: –––, 1931b, Precis of Herbrand 1930a, *Annales de l’Université de Paris*, 6: 186–189. In Herbrand 1968.

[^herbrand-1932]: –––, 1932, “Sur la non-contradiction de l’Arithmétique”, *Journal für die reine und angewandte Mathematik*, 166: 1–8. doi:10.1515/crll.1932.166.1

[^herbrand-1968]: –––, 1968, *Écrits Logiques*, Paris: Presses Universitaires de France.

[^hermes-1969]: Hermes, Hans, 1969, “Ideen von Leibniz zur Grundlagenforschung: Die Ars inveniendi und die Ars iudicandi”, in *Systemprinzip und Vielheit der Wissenschaften*, Udo W. Bargenda and Jürgen Blühdorn (eds), Wiesbaden: Franz Steiner: 78–88.

[^hilbert-1899]: Hilbert, David, 1899, *Grundlagen der Geometrie*, Leipzig: Teubner.

[^hilbert-1900]: –––, 1900 [1902], “Mathematische Probleme”, *Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen, Mathematisch-Physikalische Klasse*, 3: 253–297. Translated in 1902 as “Mathematical Problems”, Mary Winston Newson (trans.), *Bulletin of the American Mathematical Society*, 8(10): 437–480. doi:10.1090/S0002-9904-1902-00923-3

[^hilbert-1917]: –––, 1917, “Axiomatisches Denken”, *Mathematische Annalen*, 78(1–4): 405–415. doi:10.1007/BF01457115

[^hilbert-1922]: –––, 1922, “Neubegründung der Mathematik. Erste Mitteilung”, *Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg*, 1: 157–177. doi:10.1007/BF02940589

[^hilbert-1926]: –––, 1926 [1967], “Über das Unendliche”, *Mathematische Annalen*, 95(1): 161–190. Translated as “On the Infinite” in van Heijenoort 1967: 367–392. doi:10.1007/BF01206605

[^hilbert-1930a]: –––, 1930a, “Probleme der Grundlegung der Mathematik”, *Mathematische Annalen*, 102(1): 1–9. doi:10.1007/BF01782335

[^hilbert-1930b]: –––, 1930b, “Naturerkennen und Logik”, *Die Naturwissenschaften*, 18(47–49): 959–963. doi:10.1007/BF01492194

[^hilbert-1928]: Hilbert, David and Wilhelm Ackermann, 1928, *Grundzüge der Theoretischen Logik*, Berlin: Springer.

[^hilbert-1938]: –––, 1938, *Grundzüge der Theoretischen Logik*, Berlin: Springer. Second edition.

[^hilbert-1934]: Hilbert, David and Paul Bernays, 1934, *Grundlagen der Mathematik*, Volume 1, Berlin: Springer.

[^hilbert-1939]: –––, 1939, *Grundlagen der Mathematik*, Volume 2, Berlin: Springer.

[^hobbes-1655]: Hobbes, Thomas, 1655 [1839], *De Corpore*, in *Thomæ Hobbes Malmesburiensis: Opera Philosophica* (Volume 1), William Molesworth (ed.), London: J. Bohn, 1839.

[^hogarth-1994]: Hogarth, Mark, 1994, “Non-Turing Computers and Non-Turing Computability”, *PSA: Proceedings of the Biennial Meeting of the Philosophy of Science Association*, 1994(1): 126–138. doi:10.1086/psaprocbienmeetp.1994.1.193018

[^hogarth-2004]: –––, 2004, “Deciding Arithmetic Using *SAD* Computers”, *The British Journal for the Philosophy of Science*, 55(4): 681–691. doi:10.1093/bjps/55.4.681

[^hopcroft-1979]: Hopcroft, John E. and Jeffrey D. Ullman, 1979, *Introduction to Automata Theory, Languages, and Computation*, Reading, MA: Addison-Wesley.

[^houser-1997]: Houser, Nathan, Don D. Roberts, and James Van Evra (eds), 1997, *Studies in the Logic of Charles Sanders Peirce*, Bloomington, IN: Indiana University Press.

[^jevons-1870]: Jevons, W. Stanley, 1870, “On the Mechanical Performance of Logical Inference”, *Philosophical Transactions of the Royal Society of London*, 160: 497–518. doi:10.1098/rstl.1870.0022

[^jevons-1880]: –––, 1880, letter to Venn, 18 August 1880, Venn Collection, Gonville and Caius College, Cambridge, C 45/4 (quoted by permission of the Master and Fellows of Gonville and Caius).

[^kalmár-1959]: Kalmár, László, 1959, “An Argument Against the Plausibility of Church’s Thesis”, in *Constructivity in Mathematics: Proceedings of the colloquium held at Amsterdam 1957*, Arend Heyting (ed.), Amsterdam: North-Holland: 72–80.

[^kennedy-2013]: Kennedy, Juliette, 2013, “On Formalism Freeness: Implementing Gödel’s 1946 Princeton Bicentennial Lecture”, *Bulletin of Symbolic Logic*, 19(3): 351–393. doi:10.1017/S1079898600010684

[^ketner-1984]: Ketner, Kenneth L. and Arthur F. Stewart, 1984, “The Early History of Computer Design: Charles Sanders Peirce and Marquand’s Logical Machines”, *The Princeton University Library Chronicle*, 45(3): 187–224. doi:10.2307/26402393

[^kieu-2004]: Kieu, Tien D., 2004, “Hypercomputation with Quantum Adiabatic Processes”, *Theoretical Computer Science*, 317(1–3): 93–104. doi:10.1016/j.tcs.2003.12.006

[^kleene-1934]: Kleene, Stephen C., 1934, “Proof by Cases in Formal Logic”, *Annals of Mathematics*, second series 35(3): 529–544. doi:10.2307/1968749

[^kleene-1935a]: –––, 1935a, “A Theory of Positive Integers in Formal Logic. Part I”, *American Journal of Mathematics*, 57(1): 153–173. doi:10.2307/2372027

[^kleene-1935b]: –––, 1935b, “A Theory of Positive Integers in Formal Logic. Part II”, *American Journal of Mathematics*, 57(2): 219–244. doi:10.2307/2371199

[^kleene-1936a]: –––, 1936a, “General Recursive Functions of Natural Numbers”, *Mathematische Annalen*, 112(1): 727–742. doi:10.1007/BF01565439

[^kleene-1936b]: –––, 1936b, “λ-Definability and Recursiveness”, *Duke Mathematical Journal*, 2(2): 340–353. doi:10.1215/S0012-7094-36-00227-2

[^kleene-1952]: –––, 1952, *Introduction to Metamathematics*, Amsterdam: North-Holland.

[^kleene-1967]: –––, 1967, *Mathematical Logic*, New York: Wiley.

[^kleene-1981]: –––, 1981, “Origins of Recursive Function Theory”, *IEEE Annals of the History of Computing*, 3(1): 52–67. doi:10.1109/MAHC.1981.10004

[^kleene-1986]: –––, 1986, “Introductory Note to *1930b*, *1931* and *1932b*”, in Gödel 1986: 126–141.

[^kleene-1987]: –––, 1987, “Reflections on Church’s Thesis”, *Notre Dame Journal of Formal Logic*, 28(4): 490–498. doi:10.1305/ndjfl/1093637645

[^kleene-1935]: Kleene, Stephen C. and J. Barkley Rosser, 1935, “The Inconsistency of Certain Formal Logics”, *Annals of Mathematics*, second series 36(3): 630–636. doi:10.2307/1968646

[^kreisel-1965]: Kreisel, Georg, 1965, “Mathematical Logic”, in *Lectures on Modern Mathematics, Volume 3*, Thomas L. Saaty (ed.), New York: Wiley, 95–195.

[^kreisel-1967]: –––, 1967, “Mathematical Logic: What Has it Done For the Philosophy of Mathematics?”, in *Bertrand Russell: Philosopher of the Century*, Ralph Schoenman (ed.), London: George Allen and Unwin: 201–272.

[^kreisel-1974]: –––, 1974, “A Notion of Mechanistic Theory”, *Synthese*, 29(1–4): 11–26. doi:10.1007/BF00484949

[^kreisel-1982]: –––, 1982, Review of Pour-El and Richards 1979 and 1981, *The Journal of Symbolic Logic*, 47(4): 900–902. doi:10.2307/2273108

[^kripke-2013]: Kripke, Saul A., 2013, “The Church-Turing ‘Thesis’ as a Special Corollary of Gödel’s Completeness Theorem”, in Copeland, Posy, and Shagrir 2013: 77–104 (ch. 4).

[^langford-1926a]: Langford, C. Harold, 1926a, “Some Theorems on Deducibility”, *Annals of Mathematics*, second series 28(1/4): 16–40. doi:10.2307/1968352

[^langford-1926b]: –––, 1926b, “Analytic Completeness of Sets of Postulates”, *Proceedings of the London Mathematical Society*, second series 25: 115–142. doi:10.1112/plms/s2-25.1.115

[^langford-1927]: –––, 1927, “Theorems on Deducibility (Second Paper)”, *Annals of Mathematics*, second series 28(1/4): 459–471. doi:10.2307/1968390

[^langton-1989]: Langton, Christopher G., 1989, “Artificial Life”, in *Artificial Life: The Proceedings of An Interdisciplinary Workshop on the Synthesis and Simulation of Living Systems, Held September, 1987 in Los Alamos, New Mexico*, Christopher G. Langton (ed.), Redwood City, CA: Addison-Wesley, 1–47.

[^leibniz-1666]: Leibniz, Gottfried Wilhelm, 1666 [2020], *Dissertatio de Arte Combinatoria*, Leipzig. Translated in *Leibniz: Dissertation on Combinatorial Art*, Massimo Mugnai, Han van Ruler, and Martin Wilson (eds), Oxford: Oxford University Press, 2020.

[^leibniz-1671]: –––, 1671 [1926], letter to Herzog, October(?) 1671, in Erich Hochstetter, Willy Kabitz and Paul Ritter (eds), *Gottfried Wilhelm Leibniz: Sämtliche Schriften und Briefe,* second series: *Philosophischer Briefwechsel* (Volume 1), *1663–1685*, Darmstadt: O. Reichl, 1926: 159–165 (facsimile of the 1926 edition, Hildesheim: G. Olms, 1972).

[^leibniz-1679]: –––, 1679 [1903], “Consilium de Encyclopaedia Nova Conscribenda Methodo Inventoria”, in Couturat 1903: 30–41.

[^leibniz-1685]: –––, 1685 [1951], “L’Art d’Inventer”, in Couturat 1903. Translated as “The Art of Discovery” in Philip P. Wiener (ed.),*Leibniz Selections*, New York: Scribner, 1951: 50–58.

[^leibniz-1710]: –––, 1710, “*Brevis descriptio machinae arithmeticae, cum figura*”, in *Miscellanea Berolinensia ad incrementum scientiarum*, pp. 317–19 (and Fig. 73), Berlin: Johann Christoph Papenius.

[^leibniz-1714]: –––, 1714 [1969], letter to Remond, 10 January 1714, in Leroy E. Loemker (ed.), *Gottfried Wilhelm Leibniz: Philosophical Papers and Letters*, second edition, Dordrecht: Reidel, 1969: 654–655.

[^leibniz-1903]: –––, *n.d.*1 [1903], “De Machina Combinatoria”, in Couturat 1903: 572.

[^leibniz-1890]: –––, *n.d.*2 [1890], “Discours touchant la methode de la certitude et l’art d’inventer pour finir les disputes et pour faire en peu de temps des grands progrés”, in Carl J. Gerhardt (ed.), *Die philosophischen Schriften von Gottfried Wilhelm Leibniz* (Volume 7), Berlin, 1890: 174–183 (facsimile of the 1890 edition, Hildesheim: G. Olms, 1965).

[^lewis-1981]: Lewis, Harry R. and Christos H. Papadimitriou, 1981, *Elements of the Theory of Computation*, Englewood Cliffs, NJ: Prentice-Hall.

[^llull-1645]: Llull, Ramon, 1645 [1970], *Ars Generalis Ultima*, Palma Malorca, facsimile of the 1645 edition, Frankfurt: Minerva, 1970.

[^llull-1986]: –––, 1986, *Poesies*, Josep Romeu i Figueras (ed.), Barcelona: Enciclopèdia Catalana.

[^löwenheim-1915]: Löwenheim, Leopold, 1915, “Über Möglichkeiten im Relativkalkül”, *Mathematische Annalen*, 76(4): 447–470. doi:10.1007/BF01458217

[^maclennan-2003]: MacLennan, Bruce J., 2003, “Transcending Turing Computability”, *Minds and Machines*, 13(1): 3–22. doi:10.1023/A:1021397712328

[^mancosu-2015]: Mancosu, Paolo and Richard Zach, 2015, “Heinrich Behmann’s 1921 Lecture on the Decision Problem and the Algebra of Logic”, *Bulletin of Symbolic Logic*, 21(2): 164–187. doi:10.1017/bsl.2015.10

[^markov-1951]: Markov, Andrey A., 1951, “Теория Алгорифмов”, *Trudy Matematicheskogo Instituta imeni V. A. Steklova*, 38: 176–189. Translation by Edwin Hewitt, 1960, “The Theory of Algorithms”, *American Mathematical Society Translations*, Series 2, 15: 1–14.

[^marquand-1881]: Marquand, Allan, 1881, “On Logical Diagrams for *n* Terms”, *The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science*, fifth series, 12(75): 266–270. doi:10.1080/14786448108627104

[^marquand-1883]: –––, 1883, “A Machine for Producing Syllogistic Variations”, in *Studies in Logic*, Charles S. Peirce (ed.), Boston: Little, Brown, 12–15. doi:10.1037/12811-002

[^marquand-1885]: –––, 1885, “A New Logical Machine”, *Proceedings of the American Academy of Arts and Sciences*, 21: 303–307.

[^massey-1966]: Massey, Gerald J., 1966, “An Extension of Venn Diagrams”, *Notre Dame Journal of Formal Logic*, 7(3): 239–250. doi:10.1305/ndjfl/1093958619

[^mays-1951]: Mays, Wolfe and Desmond P. Henry, 1951, “Logical Machines: New Light on W. Stanley Jevons”, *Manchester Guardian*, no. 32677 (14 July 1951) B, 4.

[^mays-1953]: –––, 1953, “Jevons and Logic”, *Mind*, 62(248): 484–505. doi:10.1093/mind/LXII.248.484

[^mays-1950]: Mays, W. and Dietrich G. Prinz, 1950, “A Relay Machine for the Demonstration of Symbolic Logic”, *Nature*, 165(4188): 197–198. doi:10.1038/165197a0

[^mendelson-1963]: Mendelson, Elliott, 1963, “On Some Recent Criticism of Church’s Thesis.”, *Notre Dame Journal of Formal Logic*, 4(3): 201–205. doi:10.1305/ndjfl/1093957577

[^mendelson-1964]: –––, 1964, *Introduction to Mathematical Logic*, Princeton, NJ: Van Nostrand.

[^mendelson-1990]: –––, 1990, “Second Thoughts about Church’s Thesis and Mathematical Proofs”, *The Journal of Philosophy*, 87(5): 225–233. doi:10.2307/2026831

[^montague-1960]: Montague, Richard, 1960, “Towards a General Theory of Computability”, *Synthese*, 12(4): 429–438. doi:10.1007/BF00485427

[^németi-2006]: Németi, István and Gyula Dávid, 2006, “Relativistic Computers and the Turing Barrier”, *Applied Mathematics and Computation*, 178(1): 118–142. doi:10.1016/j.amc.2005.09.075

[^newell-1980]: Newell, Allen, 1980, “Physical Symbol Systems”, *Cognitive Science*, 4(2): 135–183. doi:10.1207/s15516709cog0402_2

[^newman-1923]: Newman, Maxwell H.A., 1923, “The Foundations of Mathematics from the Standpoint of Physics”, fellowship dissertation, in the Records of St John’s College, Cambridge, SJCR/SJAC/2/1/5/1 (quoted by permission of the Master and Fellows of St John’s).

[^newman-1955]: –––, 1955, “Alan Mathison Turing, 1912–1954”, *Biographical Memoirs of Fellows of the Royal Society*, 1(November): 253–263. doi:10.1098/rsbm.1955.0019

[^newman-1977]: –––, *c*1977, Newman in interview with Christopher Evans, *n.d.*, “The Pioneers of Computing: An Oral History of Computing”, London: Science Museum; transcription by Copeland in Copeland 2004: 206.

[^olszewski-2006]: Olszewski, Adam, Jan Woleński, and Robert Janusz (eds), 2006, *Church’s Thesis after 70 Years*, Frankfurt/New Brunswick, NJ: Ontos. doi:10.1515/9783110325461

[^peirce-1886]: Peirce, Charles S., 1886, letter to Marquand, 30 December 1886, in Peirce 1993: item 58, pp. 422–424.

[^peirce-1887]: –––, 1887, “Logical Machines”, *The American Journal of Psychology*, 1(1): 165–170.

[^peirce-1903a]: –––, 1903a, “The 1903 Lowell Institute Lectures I–V”, in Peirce 2021: 137–310.

[^peirce-1903b]: –––, 1903b, R S32, draft of last part of the 2nd Lowell Lecture, in Peirce 2021.

[^peirce-1903c]: –––, 1903c, R 462, 2nd draft of the 3rd Lowell Lecture, in Peirce 2021.

[^peirce-1903d]: –––, 1903d, R 464, 3rd draft of the 3rd Lowell Lecture, in Peirce 2021.

[^peirce-nd]: –––, *n.d.*, R 831, untitled, Charles S. Peirce Papers, Houghton Library, Harvard.

[^peirce-1908]: –––, 1908, “Some Amazing Mazes (conclusion)”, *Monist*, 18(3): 416–464. doi:10.5840/monist190818326

[^peirce-1993]: –––, 1993, *Writings of Charles S. Peirce: A Chronological Edition, Volume 5: 1884–1886*, Christian J.W. Kloesel (ed.), Bloomington, IN: Indiana University Press.

[^peirce-2021]: –––, 2021, *Charles S. Peirce: Logic of the Future, Writings on the Existential Graphs, Volume 2/2: The 1903 Lowell Lectures*, Ahti-Veikko Pietarinen (ed.), Berlin: de Gruyter.

[^penrose-1994]: Penrose, Roger, 1994, *Shadows of the Mind: A Search for the Missing Science of Consciousness*, Oxford/New York: Oxford University Press.

[^penrose-2011]: –––, 2011, “Gödel, the Mind, and the Laws of Physics”, in *Kurt Gödel and the Foundations of Mathematics*, Matthias Baaz, Christos H. Papadimitriou, Hilary W. Putnam, Dana S. Scott, and Charles L. Harper, Jr (eds), Cambridge: Cambridge University Press, 339–358. doi:10.1017/CBO9780511974236.019

[^penrose-2016]: –––, 2016, “On Attempting to Model the Mathematical Mind”, in *The Once and Future Turing: Computing the World*, S. Barry Cooper and Andrew Hodges (eds), Cambridge: Cambridge University Press, 361–378. doi:10.1017/CBO9780511863196.022

[^péter-1935]: Péter, Rózsa, 1935, “Über den Zusammenhang der verschiedenen Begriffe der rekursiven Funktion”, *Mathematische Annalen*, 110(1): 612–632. doi:10.1007/BF01448046

[^pitowski-1990]: Pitowski, Itamar, 1990, “The Physical Church Thesis and Physical Computational Complexity”, *Iyyun*, 39: 81–99.

[^post-1936]: Post, Emil L., 1936, “Finite Combinatory Processes—Formulation 1”, *The Journal of Symbolic Logic*, 1(3): 103–105. doi:10.2307/2269031

[^post-1943]: –––, 1943, “Formal Reductions of the General Combinatorial Decision Problem”, *American Journal of Mathematics*, 65(2): 197–215. doi:10.2307/2371809

[^post-1946]: –––, 1946, “A Variant of a Recursively Unsolvable Problem”, *Bulletin of the American Mathematical Society*, 52(4): 264–268. doi:10.1090/S0002-9904-1946-08555-9

[^post-1965]: –––, 1965, “Absolutely Unsolvable Problems and Relatively Undecidable Propositions—Account of an Anticipation”, in Davis 1965: 340–433.

[^pour-el-1979]: Pour-El, Marian Boykan and Ian Richards, 1979, “A Computable Ordinary Differential Equation Which Possesses No Computable Solution”, *Annals of Mathematical Logic*, 17(1–2): 61–90. doi:10.1016/0003-4843(79)90021-4

[^pour-el-1981]: –––, 1981, “The Wave Equation with Computable Initial Data Such That Its Unique Solution Is Not Computable”, *Advances in Mathematics*, 39(3): 215–239. doi:10.1016/0001-8708(81)90001-3

[^pour-el-1989]: –––, 1989, *Computability in Analysis and Physics*, Berlin: Springer. [[Pour-El and Richards 1989 available online](https://projecteuclid.org/eBooks/perspectives-in-logic/Computability-in-Analysis-and-Physics/toc/pl/1235422916)]

[^quine-1950]: Quine, Willard Van Orman, 1950, *Methods of Logic*, New York: Holt.

[^quine-1951]: –––, 1951, *Mathematical Logic*, revised edition, Cambridge, MA: Harvard University Press.

[^rabin-1959]: Rabin, Michael O. and Dana S. Scott, 1959, “Finite Automata and Their Decision Problems”, *IBM Journal of Research and Development*, 3(2): 114–125. doi:10.1147/rd.32.0114

[^ramsey-1930]: Ramsey, Frank P., 1930, “On a Problem of Formal Logic”, *Proceedings of the London Mathematical Society*, second series 30(1): 264–286. doi:10.1112/plms/s2-30.1.264

[^roberts-1973]: Roberts, Don D., 1973, *The Existential Graphs of Charles S. Peirce*, Hague: Mouton.

[^roberts-1997]: –––, 1997, “A Decision Method for Existential Graphs”, in Houser, Roberts, & Van Evra 1997: 387–401.

[^rosser-1935a]: Rosser, J. Barkley, 1935a, “A Mathematical Logic Without Variables. I”, *Annals of Mathematics*, second series 36(1): 127–150. doi:10.2307/1968669

[^rosser-1935b]: –––, 1935b, “A Mathematical Logic without Variables. II”, *Duke Mathematical Journal*, 1(3): 328–355. doi:10.1215/S0012-7094-35-00123-5

[^scarpellini-1963]: Scarpellini, Bruno, 1963, “Zwei Unentscheidbare Probleme Der Analysis”, *Zeitschrift für Mathematische Logik und Grundlagen der Mathematik*, 9(18–20): 265–289. doi:10.1002/malq.19630091802

[^scarpellini-2003]: –––, 2003, “Comments on ‘Two Undecidable Problems of Analysis’”, *Minds and Machines*, 13(1): 79–85. doi:10.1023/A:1021364916624

[^schiemer-2017]: Schiemer, Georg, Richard Zach, and Erich Reck, 2017, “Carnap’s Early Metatheory: Scope and Limits”, *Synthese*, 194(1): 33–65. doi:10.1007/s11229-015-0877-z

[^schmidhuber-2012]: Schmidhuber, Jürgen, 2012, “Turing in Context”, *Science*, 336(6089): 1638–1639. doi:10.1126/science.336.6089.1638-c

[^schönfinkel-nd]: Schönfinkel, Moses, 192?, “Zum Entscheidungsproblem der mathematischen Logik”, *n.d.*, Heft I, *Bernays Papers*, ETH Zurich (Hs 974.282).

[^schönfinkel-1924]: –––, 1924, “Über die Bausteine der mathematischen Logik”, *Mathematische Annalen*, 92(3–4): 305–316. doi:10.1007/BF01448013

[^searle-1992]: Searle, John R., 1992, *The Rediscovery of the Mind*, Cambridge, MA: MIT Press.

[^shagrir-2002]: Shagrir, Oron, 2002, “Effective Computation by Humans and Machines”, *Minds and Machines*, 12(2): 221–240. doi:10.1023/A:1015694932257

[^shagrir-2006]: –––, 2006, “Gödel on Turing on Computability”, in Olszewski, Wolenski, and Janusz 2006: 393–419. doi:10.1515/9783110325461.393

[^shagrir-2003]: Shagrir, Oron and Itamar Pitowsky, 2003, “Physical Hypercomputation and the Church–Turing Thesis”, *Minds and Machines*, 13(1): 87–101. doi:10.1023/A:1021365222692

[^shepherdson-1963]: Shepherdson, John C. and Howard E. Sturgis, 1963, “Computability of Recursive Functions”, *Journal of the ACM*, 10(2): 217–255. doi:10.1145/321160.321170

[^shoenfield-1993]: Shoenfield, Joseph R., 1993, *Recursion Theory*, Berlin/New York: Springer.

[^sieg-1994]: Sieg, Wilfried, 1994, “Mechanical Procedures and Mathematical Experience”, in *Mathematics and Mind*, Alexander George (ed.), Oxford: Oxford University Press: 71–117.

[^sieg-2002]: –––, 2002, “Calculations by Man and Machine: Conceptual Analysis”, in *Reflections on the Foundations of Mathematics: Essays in Honor of Solomon Feferman*, Wilfried Sieg, Richard Sommer, and Carolyn Talcott (eds), Urbana, IL: Association for Symbolic Logic, 390–409.

[^sieg-2008]: –––, 2008, “Church Without Dogma: Axioms for Computability”, in *New Computational Paradigms*, S. Barry Cooper, Benedikt Löwe, and Andrea Sorbi (eds), New York, NY: Springer New York, 139–152. doi:10.1007/978-0-387-68546-5_7

[^siegelmann-2003]: Siegelmann, Hava T., 2003, “Neural and Super-Turing Computing”, *Minds and Machines*, 13(1): 103–114. doi:10.1023/A:1021376718708

[^siegelmann-1992]: Siegelmann, Hava T. and Eduardo D. Sontag, 1992, “On the Computational Power of Neural Nets”, in *Proceedings of the Fifth Annual Workshop on Computational Learning Theory - COLT ’92*, Pittsburgh, PA: ACM Press, 440–449. doi:10.1145/130385.130432

[^siegelmann-1994]: –––, 1994, “Analog Computation via Neural Networks”, *Theoretical Computer Science*, 131(2): 331–360. doi:10.1016/0304-3975(94)90178-3

[^skolem-1923]: Skolem, Thoralf, 1923, “Begründung der elementaren Arithmetik”, *Videnskapsselskapets Skrifter, I. Matematisk-naturvidenskabelig Klasse*, 6: 3–38.

[^smithies-1934]: Smithies, Frank, 1934, “Foundations of Mathematics. Mr. Newman”, lecture notes, St John’s College Library, Cambridge, GB 275 Smithies/H/H57.

[^stannett-1990]: Stannett, Mike, 1990, “X-Machines and the Halting Problem: Building a Super-Turing Machine”, *Formal Aspects of Computing*, 2(1): 331–341. doi:10.1007/BF01888233

[^stewart-1991]: Stewart, Ian, 1991, “Deciding the Undecidable”, *Nature*, 352(6337): 664–665. doi:10.1038/352664a0

[^stjernfelt-2022]: Stjernfelt, Frederik, 2022, *Sheets, Diagrams, and Realism in Peirce*, Berlin: De Gruyter. doi:10.1515/9783110793628

[^syropoulos-2008]: Syropoulos, Apostolos, 2008, *Hypercomputation: Computing beyond the Church-Turing Barrier*, New York: Springer. doi:10.1007/978-0-387-49970-3

[^turing-1936]: Turing, Alan M., 1936 [2004], “On Computable Numbers, with an Application to the Entscheidungsproblem”, *Proceedings of the London Mathematical Society*, 1936, second series, 42(1): 230–265. Reprinted in Copeland 2004: 58–90 (ch. 1). doi:10.1112/plms/s2-42.1.230

[^turing-1937]: –––, 1937, “Computability and λ-Definability”, *The Journal of Symbolic Logic*, 2(4): 153–163. doi:10.2307/2268280

[^turing-1939]: –––, 1939 [2004], “Systems of Logic Based on Ordinals”, *Proceedings of the London Mathematical Society*, second series, 45(1): 161–228. Reprinted in Copeland 2004: 146–204 (ch. 3). doi:10.1112/plms/s2-45.1.161

[^turing-1940]: –––, c.1940 [2004], letter to Newman, n.d., in Copeland 2004: 214–216 (ch. 4).

[^turing-1945]: –––, 1945 [2005], “Proposed Electronic Calculator”, National Physical Laboratory Report, in Copeland 2005: 369–454 (ch. 20). doi:10.1093/acprof:oso/9780198565932.003.0021

[^turing-1947]: –––, 1947 [2004], “Lecture on the Automatic Computing Engine”, London Mathematical Society, in Copeland 2004: 378–394 (ch. 9).

[^turing-1948]: –––, 1948 [2004], “Intelligent Machinery”, National Physical Laboratory Report, in Copeland 2004: 410–432 (ch. 10).

[^turing-1950a]: –––, 1950a [2004], “Computing Machinery and Intelligence”, *Mind*, 59(236): 433–460. Reprinted in Copeland 2004: 441–464 (ch. 11). doi:10.1093/mind/LIX.236.433

[^turing-1950b]: –––, 1950b, “The Word Problem in Semi-Groups With Cancellation”, *Annals of Mathematics*, second series 52(2): 491–505. doi:10.2307/1969481

[^turing-1950]: –––, c.1950, *Programmers’ Handbook for Manchester Electronic Computer Mark II*, Computing Machine Laboratory, University of Manchester. [[Turing c.1950 available online](http://www.AlanTuring.net/programmers_handbook)]

[^turing-1954]: –––, 1954 [2004], “Solvable and Unsolvable Problems”, *Science News* (Penguin Books), 31: 7–23. Reprinted in Copeland 2004: 582–595 (ch. 17).

[^heijenoort-1967]: van Heijenoort, Jean, 1967, *From Frege to Gödel: A Source Book in Mathematical Logic, 1879–1931*, Cambridge, MA: Harvard University Press.

[^venn-1880]: Venn, John, 1880, “On the Diagrammatic and Mechanical Representation of Propositions and Reasonings”, *The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science*, fifth series, 10(59): 1–18. doi:10.1080/14786448008626877

[^neumann-1927]: von Neumann, John, 1927, “Zur Hilbertschen Beweistheorie”, *Mathematische Zeitschrift*, 26(1): 1–46. doi:10.1007/BF01475439

[^neumann-1931]: –––, 1931, “Die formalistische Grundlegung der Mathematik”, *Erkenntnis*, 2(1): 116–121. doi:10.1007/BF02028144

[^wang-1974]: Wang, Hao, 1974, *From Mathematics to Philosophy*, New York: Humanities Press.

[^wang-1996]: –––, 1996, *A Logical Journey: From Gödel to Philosophy*, Cambridge, MA: MIT Press.

[^weyl-1927]: Weyl, Hermann, 1927 [1949], “Philosophie der Mathematik und Naturwissenschaft”, *Handbuch der Philosophie*, Munich: Oldenbourg. Published in English as *Philosophy of Mathematics and Natural Science*, Princeton, NJ: Princeton University Press, 1949.

[^wittgenstein-1947]: Wittgenstein, Ludwig, 1947 [1980], *Bemerkungen über die Philosophie der Psychologie*. Translated as *Remarks on the Philosophy of Psychology*, Volume 1, Anscombe, G. Elizabeth M. and Georg Henrik von Wright (eds), Oxford: Blackwell, 1980.

[^wolfram-1985]: Wolfram, Stephen, 1985, “Undecidability and Intractability in Theoretical Physics”, *Physical Review Letters*, 54(8): 735–738. doi:10.1103/PhysRevLett.54.735

[^wolfram-2021]: –––, 2021, *Combinators: A Centennial View*, Champaign, IL: Wolfram Media.

[^yao-2003]: Yao, Andrew C.-C., 2003, “Classical Physics and the Church-Turing Thesis”, *Journal of the ACM*, 50(1): 100–105. doi:10.1145/602382.602411

[^zach-1999]: Zach, Richard, 1999, “Completeness Before Post: Bernays, Hilbert, and the Development of Propositional Logic”, *Bulletin of Symbolic Logic*, 5(3): 331–366. doi:10.2307/421184

[^zach-2003]: –––, 2003, “The Practice of Finitism: Epsilon Calculus and Consistency Proofs in Hilbert’s Program”, *Synthese*, 137(1/2): 211–259. doi:10.1023/A:1026247421383

[^zanichelli-1929]: Zanichelli, Nicola (ed.), 1929, *Atti del Congresso Internazionale dei Matematici, Bologna, 3–10 Settembre 1928, Volume 1: Rendiconto del Congresso Conferenze*, Bologna: Società Tipografica.
