# church-turing — decision-problem（supplement）

> （《church-turing》词条补充材料，源：plato.stanford.edu/entries/church-turing/decision-problem.html）

#### Supplement to The Church-Turing Thesis

## The Rise and Fall of the *Entscheidungsproblem*

- A. Stating the *Entscheidungsproblem*
- B. Why the problem mattered
- B.1 A “philosophers’ stone”
- B.2 The consistency of mathematics
- C. Partial solutions
- D. Negative vibes
- E. The Church-Turing result
- F. Aftermath

### A. Stating the *Entscheidungsproblem*

Turing gave two formulations of what he called “the Hilbert *Entscheidungsproblem*” (1936 [2004: 84, 87]):

> [Is there a] general process [and a few paragraphs later, he emphasizes “general (mechanical) process”] for determining whether a given formula $A$ of the functional calculus K is provable

and:

> [Is there a] machine [Turing machine] which, supplied with any one $A$ of these formulae, will eventually say whether $A$ is provable.

Given Turing’s thesis, the two formulations are equivalent.

Church stated the *Entscheidungsproblem* more generally:

> By the *Entscheidungsproblem* of a system of symbolic logic is here understood the problem to find an effective method by which, given any expression *Q* in the notation of the system, it can be determined whether or not *Q* is provable in the system. (Church 1936b: 41)

While Turing and Church both formulated the *Entscheidungsproblem* in terms of determining whether or not a formula is *provable*, Hilbert and Ackermann had formulated it in terms of *universal validity* (“*allgemeingültigkeit*”):

> The *Entscheidungsproblem* is solved once we know a procedure that allows us to decide, by means of finitely many operations, whether a given logical expression is universally valid or, alternatively, satisfiable. (Hilbert & Ackermann 1928: 73)

A universally valid formula of the functional calculus (e.g., $(x)(Fx \lor \neg Fx)$ or, in modern notation, $\forall x(Fx \lor \neg Fx)$) must contain neither free variables nor individual constants, and is such that a true assertion results no matter which replacements (of suitable adicity) are made for the formula’s predicate symbols, and no matter which objects are allocated to its variables (Hilbert & Ackermann 1928: 72–73). In the case of a satisfiable formula (e.g., $(Ex)Fx$ or, in modern notation, $\exists xFx$) there must be *at least one* way of replacing its predicate symbols and of allocating objects to its variables so that a true assertion results. Universal validity and satisfiability are related as follows: $A$ is universally valid if and only if $\neg A$ is not satisfiable (1928: 73). In the above quotation, therefore, Hilbert and Ackermann are presenting two different but equivalent forms of the *Entscheidungsproblem*, one employing the concept of universal validity (or simply validity, as we would say today) and the other the closely related concept of satisfiability. The hunt was on for what they called “a determinate, finite procedure” (1928: 17) for deciding, of any given formula $A$ of the functional calculus, whether or not $A$ is universally valid, or, equivalently, for deciding whether or not $\neg A$ is satisfiable.

Turing’s and Church’s provability formulation of the *Entscheidungsproblem* and the Hilbert-Ackermann formulation in terms of validity are in fact logically equivalent, as Church noted in 1936 (1936b: 41). This equivalence is a consequence of Gödel’s proof that (where $A$ is any formula of the functional calculus) if $A$ is universally valid then $A$ is provable in the calculus. (The proof was presented originally in Gödel’s 1929 doctoral dissertation and then published as Gödel 1930.) Nevertheless, the provability version of the *Entscheidungsproblem* is arguably superior, since it asks a question about a specific axiom system, as do the allied problems of consistency and completeness. In modern treatments, the problems of consistency, completeness and decidability for an axiom system lie at the heart of proof theory, the area of modern logic founded by Hilbert.

In 1928, Hilbert and Ackermann were certainly aware of the provability formulation (1928: 86, and see below) but they gave the validity formulation the starring role. It was von Neumann who emphasized the provability formulation, calling the process of proof the “real heart of mathematics” (von Neumann 1927: 10).

### B. Why the problem mattered

Why was it that the *Entscheidungsproblem* was regarded as “the main problem of mathematical logic” and “the most general problem of mathematics”? There were fundamentally two reasons.

#### B.1 A “philosophers’ stone”

In his turn-of-the-century Paris lecture, Hilbert explained the idea of *axiomatizing* a subject-matter and using provability from the axioms as the touchstone of truth:

> When we are engaged in investigating the foundations of a science, we must set up a system of axioms which contains an exact and complete description of the relations subsisting between the elementary ideas of that science…. [N]o statement within the realm of the science whose foundation we are testing is held to be correct unless it can be derived from those axioms by means of a finite number of logical steps. (Hilbert 1900: 264 [trans. 1902: 447])

He also famously said in his lecture that there is “no *ignorabimus*” in mathematics—there is nothing that we shall not know (Hilbert 1900: 262). It was a phrase he would often use to express his “conviction of the solvability of every mathematical problem” (Hilbert 1900: 262 [trans. 1902: 445]). Thirty years later he reiterated the same standpoint, in a valedictory lecture in Königsberg:

> [I]n my opinion, there is no such thing as an unsolvable problem. On the contrary, instead of foolish ignorabimus, our slogan is: We must know, We will know. (Hilbert 1930b: 963)

It was Hilbert’s great invention, proof theory, that would, he thought, supply the basis for answering all “meaningful questions”:

> [O]n the basis of the proof theory I have outlined, every fundamental question can be answered in a way that is unambiguous and mathematically precise. (Hilbert 1930a: 8, 9)

However, proving a statement in an axiom system can be a tricky matter. Suppose the mathematician fails to discover a derivation of the statement from the axioms, what follows then? The failure could be because the statement is indeed not provable—but, on the other hand, there might be a way to prove it that escaped the mathematician’s attention. Success in finding a proof brings certainty, whereas failure leaves us uncertain. That is why a decision method is so desirable. The method enables the mathematician to determine whether or not the statement is provable. Thinking up proofs is a serendipitous activity that involves, as Behmann put it, “inventive insight”, “creative thought”, and searching “in every direction of the compass” (Behmann 1921: 2–3 [trans. 2015: 174]). Whereas a decision method is a purely mechanical process that is guaranteed to produce a definite answer.

Herbrand wrote of the “present great ambition, the solution of the *Entscheidungsproblem*”, saying this “would provide a general method in mathematics” and enable us to “to decide with certainty whether a proposition is true in a given theory” (Herbrand 1930b: 254–255). In his 1921 lecture, Behmann had referred to this desired general method as a “philosophers’ stone” (“*Stein der Weisen*”), by means of which mathematicians “would be able to *solve every problem posed*”—or even “delegate the work of proving mathematical theorems to mathematical laborers” (Behmann 1921: 3–4 [trans. 2015: 175], emphasis added). Turing’s mentor Newman, familiar of course with the work of the Hilbert group, also referred to the solution of the *Entscheidungsproblem* as a philosophers’ stone. Hilbert and Ackermann themselves said, in 1928:

> Solving this general *Entscheidungsproblem* [for the second-order functional calculus] would … enable us to decide on the provability or unprovability of *any mathematical proposition*, at least in principle. (Hilbert & Ackermann 1928: 86, emphasis added)

Schönfinkel went even further. He was another member of the Göttingen group who praised “Leibniz’s bold conjectures” (Schönfinkel 192?: 2). (For an excellent biographical article on Schönfinkel, see Wolfram 2021.) In an early draft of what would become Bernays and Schönfinkel (1928), Schönfinkel wrote of “the great *Entscheidungsproblem* of mathematical logic” which, thanks to Hilbert, mathematicians now had “the courage and the boldness to dare to touch”. He described the *Entscheidungsproblem* as “the problem of ‘solving all problems’”—not just all mathematical problems but *all* problems. Because once there is a method for solving all mathematical problems:

> thereafter everything else is indeed lightweight, once this “Gordian knot” is undone (since “the world is written in mathematical characters”). (Schönfinkel 192?: 1–2)

#### B.2 The consistency of mathematics

The second reason the *Entscheidungsproblem* was regarded as so important was its connection with the quest for proofs of the *consistency* of mathematical systems. A system is said to be inconsistent if there is some statement $A$ such that both $A$ and $\neg A$ are provable from the axioms. The system is consistent if (and only if) there is no statement for which this sorry situation is the case.

By the early twentieth century, mathematics—until then a “paragon of reliability and truth”, Hilbert said—was in trouble (Hilbert 1926: 170, trans. in van Heijenoort 1967: 375). Its reputation had been “lost due to the paradoxes of set theory” (Hilbert 1922: 160). Hilbert explained:

> [C]ontradictions appeared, sporadically at first, then ever more severely and ominously…. In particular, a contradiction discovered by Zermelo and Russell [“Russell’s paradox”] had, when it became known, a downright catastrophic effect in the world of mathematics. (Hilbert 1926: 169 [trans. 1967: 375])

Herbrand takes up the story:

> One must take great care … Set theory has produced famous examples [of inconsistencies] … But there is nothing to show us that similar issues do not arise for the theories that seem to us the most finished, like arithmetic. Could it be that arithmetic is inconsistent? (Herbrand 1930b: 250–251)

“[P]roofs of consistency would be very useful to dispel lingering doubts”, wrote Herbrand (1930b: 251). Hilbert put it even more forcefully:

> [T]he situation in which we presently find ourselves with respect to the paradoxes is in the long run intolerable. (Hilbert 1926: 170 [trans. 1967: 375])

Proving “the consistency of the arithmetic axioms” is “urgent”, he said—“a burning question” (Hilbert 1926: 179 [trans. 1967: 383]; Hilbert 1930a: 3). Hilbert’s overarching concern was to “re-establish mathematics’ old reputation for incontestable truth” (Hilbert 1922: 160), and he was “convinced that it must be possible to find a direct proof of the consistency of the arithmetical axioms” (Hilbert 1900: 265).

A solution to the *Entscheidungsproblem* would furnish a route to establishing consistency: “By means of the decision method, issues of consistency would also be able to be resolved” (Hilbert & Ackermann 1928: 76). This is because the decision method could be used to establish whether or not $A$ and $\neg A$ are both provable—so gaining a definite answer to the question “Is the system consistent?”. Hilbert believed that, following the discovery of the decision method, arithmetic and analysis would be proved consistent, thereby “establish[ing] that mathematical propositions are indeed incontestable and absolute truths” (Hilbert 1922: 162). Mathematics’ reputation would be regained.

### C. Partial solutions

By the time Turing and Church engaged with the *Entscheidungsproblem*, a number of decision methods were known for *parts* of the functional calculus.

Besides the previously mentioned Hilbert-Bernays decision method for the propositional calculus (and Peirce’s much less well-known method), and also the Löwenheim method for the monadic fragment of the functional calculus (later improved by Behmann in his 1922 paper, where it was additionally proved that the monadic fragment of the second-order functional calculus is decidable), there were various decision methods that succeeded providing the functional calculus was restricted in one way or another. Bernays and Schönfinkel (1928) showed there is a decision method when formulae containing at most two individual variables are considered. At Cambridge, Ramsey devised a method that worked provided existential quantifiers were omitted from the calculus, and any universal quantifiers were stacked one after another at the very beginning of a formula (with no negation sign preceding any of them, and with their scope extending to the end of the formula). Such formulae are interesting, Ramsey pointed out, since they represent “general laws” (Ramsey 1930: 272; Langford 1926b: 115–116). Ackermann, Bernays, Schönfinkel, Gödel, Kálmar, and Herbrand devised methods for other fragments of the calculus, in which only certain patterns of quantifiers were permitted. Gödel’s 1933 paper on the *Entscheidungsproblem* gave a summary of some of the developments.

Despite all this attention to the decision problem, no method had been found for the full functional calculus. But according to Hilbert it was just a matter of time. He and Ackermann emphasized that “finding a general decision process is an as yet unsolved and difficult problem” (1928: 77). They exuded optimism, writing buoyantly of moving “closer to the solution of the *Entscheidungsproblem*” (1928: 81).

### D. Negative vibes

Even in the 1920s, however, negative opinion on the solvability of the *Entscheidungsproblem* was building. Behmann had pointed out in his 1921 lecture that, once the “philosophers’ stone” was found, “the entirety of mathematics would indeed be transformed into one *enormous triviality*” (Behmann 1921: 5 [trans. 2015: 175]). Some found this consequence highly unpalatable. In 1927, Hilbert’s student Weyl insisted that “such a philosopher’s stone has not been discovered and never will be discovered”, and a good job too, Weyl thought, since if it were, “Mathematics would thereby be trivialized” (Weyl 1927: 20 [trans. Weyl 1949: 24]). Then a year later, in 1928, Hardy announced to the Cambridge mathematicians, assembled at his Rouse Ball Lecture, that he expected no “system of rules which enable us to say whether any given formula [is] demonstrable or not” (Hardy 1929: 16). “[T]his is very fortunate”, he continued, since if there were such a system,

> we should have a mechanical set of rules for the solution of all mathematical problems, and our activities as mathematicians would come to an end. (ibid.)

Hardy explained that his description of Hilbert’s ideas was “based upon that of v. Neumann, a pupil of Hilbert’s”, saying that he found von Neumann’s exposition “sharper and more sympathetic than Hilbert’s own” (Hardy 1929: 13–14). Hardy was referring to von Neumann’s “Zur Hilbertschen Beweistheorie” (*On Hilbert’s Proof Theory*), published in 1927 but completed by the middle of 1925. Von Neumann said:

> So it *seems* that there is no way to find the general decision criterion for whether a given normal formula [i.e., a well-formed formula with no free variables] is provable. (von Neumann 1927: 11, emphasis added)

Also:

> The day that undecidability lets up, mathematics in its current sense would cease to exist; into its place would step a perfectly mechanical rule, by means of which anyone could decide, of any given proposition, whether this can be proved or not. (von Neumann 1927: 12)

But how to *prove* that there is no general decision criterion? Von Neumann confessed he did not know:

> At present, of course, we cannot demonstrate this. Moreover, no clue whatsoever exists how such an undecidability proof would have to be conducted. (von Neumann 1927: 11)

Nor did he find a proof. With a hint of resignation he said in 1931 that the *Entscheidungsproblem* was “far too difficult” (1931: 121). Four years later, in 1935, he visited Cambridge for a term (arriving in April, a few weeks after Newman had lectured on the *Entscheidungsproblem*) and he struck up an acquaintance with a young mathematician who admired his work (Copeland & Fan 2023). The young man was of course Alan Turing, who within a few months would devise his groundbreaking proof that—just as von Neumann had hypothesized—“It is generally undecidable whether a given normal formula is provable or not” (von Neumann 1927: 12). Was there discussion, during the spring of 1935, between von Neumann and Turing (the latter already primed by Newman’s lecture) about the *Entscheidungsproblem*—which was, after all, the main problem of mathematical logic? Did von Neumann perhaps play a role in Turing’s decision to take on this fundamental problem and prove it unsolvable? These are tantalizing questions, and we may never know for sure.

### E. The Church-Turing result

Gödel’s famous incompleteness theorems of 1931 placed unexpected new obstacles in the way of Hilbert’s desired consistency proof for arithmetic (Gödel 1931). Suspicion also began to build that Gödel’s incompleteness results might further imply the unsolvability of the *Entscheidungsproblem*. Herbrand said cautiously:

> [A]lthough at present the possibility of a solution to the *Entscheidungsproblem* seems unlikely, its impossibility has not yet been proved. (Herbrand 1931a: 56)

Carnap, who took a close interest in Hilbert’s Göttingen group and had worked with Behmann (Schiemer, Zach, & Reck 2017) wrote the following about the Hilbertian idea of a “definite criterion of validity” or “decision procedure for mathematics”, using which “we could so to speak calculate the truth or falsity of every given proposition”:

> [B]ased on Gödel’s latest results, the search for a definite criterion of validity for the entire system of mathematics appears hopeless. (Carnap 1935: 163–4)

But, as Herbrand noted, nobody had *proved* the *Entscheidungsproblem* to be unsolvable. That was where Turing and Church entered the story. Newman later summed up matters as they had appeared at the time, before Church and Turing published their transformational papers in 1936:

> A first blow was dealt [to the “Hilbert decision-programme”] by Gödel’s incompleteness theorem (1931), which made it clear that truth or falsehood of $A$ could not be equated to provability of $A$ or not-$A$ in any finitely based logic, chosen once for all; but there still remained in principle the possibility of finding a mechanical process for deciding whether $A$, or $\neg A$, or neither, was formally provable in a given system. (Newman 1955: 256)

Turing summed up his show-stopping result in his usual terse way: he had shown, he said, that “the Hilbert *Entscheidungsproblem* can have no solution” (Turing 1936 [2004: 84]). Church, also not one to waste words, compressed his proof into a paper barely two pages long, and concluded pithily:

> The general case of the *Entscheidungsproblem* of the engere Funktionenkalkül is unsolvable. (Church 1936b: 41)

In establishing this, Turing and Church showed moreover that there can be no decision method for the second-order functional calculus (where quantification is permitted over not just individuals but also over properties and relations), since the second-order calculus contains the first-order calculus as a fragment. The same applies to every other mathematical system containing the first-order calculus, such as arithmetic.

However, it is one of the great ironies of the history of logic that, all along, Gödel’s first incompleteness theorem of 1931 did in fact suffice to establish the undecidability of the functional calculus—although this was certainly not apparent at the time. More than three decades passed after the publication of Gödel’s paper before this corollary of his theorem was noted, by Davis (Davis 1965: 109; Kleene 1986: 136).

Naturally, this unnoticed implication of Gödel’s theorem does not diminish Turing’s and Church’s great achievement, which at the time broke new ground. However, in recent times their work is sometimes regarded as amounting to merely a smallish development of Gödel’s previously published results, on which Church’s and Turing’s work was supposedly based. This is particularly true of Turing. Turing, it is said, “merely reformulated Gödel’s work in an elegant way” (Schmidhuber 2012: 1638) and “recast” Gödel’s findings “in the guise of the Halting Problem” (Dawson 2006: 133). (For further discussion of these and similar views, see Copeland & Fan 2022.) In this connection, it is worth remembering the words of Kleene, who worked closely with Church and played a leading part in the development of computability theory in the 1930s. Kleene noted that

> One sometimes encounters statements asserting that Gödel’s work laid the foundation for Church’s and Turing’s results

and commented:

> Whether or not one judges that Church would have proceeded from his thesis to these [undecidability] results without his having been exposed to Gödel numbering, it seems clear that Turing in [“On Computable Numbers”] had his own train of thought, quite unalloyed by any input from Gödel. One is impressed by this in reading Turing [“On Computable Numbers”] in detail. (Kleene 1987: 491–2)

### F. Aftermath

What became of the *Entscheidungsproblem* after the Church-Turing negative result?

In letters written in the wake of the result, Turing and Newman discussed the idea Newman had presented in his 1935 lecture, a machine that is able to decide mathematical problems. Turing wrote “I think you take a much more radically Hilbertian attitude about mathematics than I do”, responding to Newman’s statement that

> If all this whole formal outfit is not about finding proofs which can be checked on a machine it’s difficult to know what it is about. (Turing c.1940 [2004: 215])

Turing noted that he saw no essential difference between a proof-checking machine and a proof-finding machine. He challenged Newman:

> When you say “on a machine” do you have in mind that there is (or should be or could be, but has not been actually described anywhere) some fixed machine on which proofs are to be checked, and that the formal outfit is, as it were about this machine?

Turing called this an “extreme Hilbertian” position, and said:

> If you take this attitude … there is little more to be said: we simply have to get used to the technique of this machine and resign ourselves to the fact that there are some problems to which we can never get the answer.

Turing rejected this attitude to mathematics, because, he said, “there is a fairly definite idea of a true formula which is quite different from the idea of a provable one”—mathematicians’ judgements about whether formulae are true can outrun the pronouncements of the Hilbertian machine. Turing continued in his letter:

> If you think of various machines I don’t see your difficulty. One imagines different machines allowing different sets of proofs, and by choosing a suitable machine one can approximate “truth” by “provability” better than with a less suitable machine … (Turing c.1940 [2004: 215])

In Turing’s opinion, that was how the debate on the *Entscheidungsproblem* had panned out. The Hilbertians had wanted a single decision method for the whole of mathematics—a single computing machine or algorithm—whereas Turing showed there can be no such thing; but he emphasized that there are, nevertheless, different decision methods (machines) for different areas of mathematics (see further Copeland & Shagrir 2013). In place of the one great unsolvable decision problem, there are many lesser, but often solvable, decision problems.

In the long aftermath of the Church-Turing result, as those rough pioneering days gave way to modern computer science, Turing’s opinion became the mainstream view: Today, computer science makes use of a multiplicity of algorithms for deciding different parts of the functional calculus and other mathematical systems.
