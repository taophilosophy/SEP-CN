# proof-theory — appendix-a（supplement）

> （《proof-theory》词条补充材料，源：plato.stanford.edu/entries/proof-theory/appendix-a.html）

#### Supplement to Proof Theory

## A. Formal Axiomatics: Its Evolution and Incompleteness

In this somewhat extended appendix, we are going to discuss the evolution of the formal axiomatic standpoint in Hilbert’s foundational thinking. To begin with we articulate in greater detail than we did in section 1 of the main article Dedekind’s way of defining abstract concepts, like that of a simply infinite system. Dedekind had seen very clearly that such a structural definition raises a fundamental issue: How can we ensure that such a definition does not contain internal contradictions?

- A.1 Structural definitions
- A.2 Consistency: no internal contradictions
- A.3 Formal proofs
- A.4 Gödel’s incompleteness results

### A.1 Structural definitions

In the three volumes of Dedekind’s *Gesammelte mathematische Werke*, there are exactly two occurrences of the word “Axiom”. The main substantive occurrence is found in section 3 of Dedekind 1872, where Dedekind refers to his principle of continuity as an *axiom*. The second occurrence, in the preface to the same essay, points to Cantor’s 1872, where a corresponding principle is also called an axiom. To emphasize, the word “Axiom” is neither used in his work on algebraic number theory, nor in his second foundational essay on natural numbers (Dedekind 1888). And yet, Emmy Noether is right when she asserts in her brief remark on *Stetigkeit und irrationale Zahlen* that Dedekind’s axiomatic standpoint is articulated very clearly in this essay and in his letters to Lipschitz from June and July 1876 that comment on the essay (her remarks can be found in Dedekind 1932: 334). In his letter of July 1876, Dedekind makes a striking remark concerning Euclid’s Elements and continuity:

> Let’s analyze all the assumptions, that have been made explicitly or tacitly, on which the entire edifice of Euclid’s geometry is built, let’s admit the truth of all his theorems as well as the feasibility of all his constructions …: as far as I have investigated matters, one never reaches in this way the continuity of space as a condition that is inseparably connected with Euclid’s geometry; his whole system remains valid even without continuity—a result that is certainly surprising for many and thus seemed to me to be worth mentioning. (Dedekind 1932: 479)

Where we indicated the ellipsis, Dedekind inserted a remarkable statement, in parentheses, that pertains to his theory of real numbers:

> (an absolutely reliable method of such an analysis consists for me in the replacement of all *Kunstausdrücke* [technical terms or terms of art] by arbitrary newly invented (up to now meaningless words): the edifice, if properly constructed, must not collapse, and I claim for example that my theory of real numbers passes this test).

What is Dedekind’s *theory* of real numbers?—It is best understood as the theory of *complete* (or continuous) *ordered* fields. The notion of a *field*, prominent in Dedekind’s work on algebraic number theory, was introduced in a supplement to Lejeune Dirichlet et al. 1871. It is highlighted in the 1872 essay already in section 1, entitled “Properties of rational numbers”. The system $\rR$ of rational numbers is said to have, with respect to the four fundamental operations (addition, subtraction, multiplication and division), that “completeness and closure” which he designated in the Supplement as the *characteristic property* (*Merkmal*) of a number field. In this very section, Dedekind also introduces the usual ordering between rational numbers that is compatible with the algebraic operations. Dedekind’s treatment foreshadows that of simply infinite systems in the later and methodologically sophisticated essay *Was sind und was sollen die Zahlen?* (1888). There, any system N of “things” is simply infinite just in case there is an element 1 in N and a mapping $\varphi$ of N, such that

1. $\varphi[{\bN}]$ is a subset of N,
2. N is the chain of the system $\{1\}$,
3. 1 is not an element of $\varphi[{\bN}]$, and
4. the mapping $\varphi$ is injective.[^note-35]

Using this approach, any system R of things is a *complete ordered field* just in case there is an ordering O and there are four operations on R, such that (1) R with O is a continuous ordered system (in Dedekind’s sense) and (2) R with the four operations is a field (and the operations are compatible with the ordering). Dedekind’s theory of real numbers is thus given as a “structural definition”.

Hilbert’s theory of real numbers is formulated in Hilbert 1900a also as a structural definition. It is assumed that a system exists whose elements satisfy the conditions Hilbert calls *axioms*. Hilbert points out the parallelism with the method of geometry.

> Here [in geometry] one begins customarily by assuming the existence of all the elements, i.e., one postulates at the outset three systems of things (namely, the points, lines, and planes), and then—essentially after the model of Euclid—brings these elements into relationship with one another by means of certain axioms of linking, order, congruence, and continuity. (Hilbert 1900a: 1092)

These geometric ways are taken over for arithmetic when Hilbert introduces a system of real numbers as follows:

> We think a system of things, and we call them numbers and denote them by *a*, *b*, *c*…. We think these numbers in certain mutual relations, whose precise and complete description is obtained through the following axioms. (Hilbert 1900a: 1092)

Then the axioms for an ordered field are formulated and “completed” by the requirement of continuity via the Archimedean axiom and the axiom of completeness. This formulation is in the spirit of Hilbert’s geometric ways, but how is it connected to Dedekind’s way?

The connection is illuminated through the correspondence with Frege in late 1899 when Hilbert responds to Frege’s complaint about his use of the word “axiom”; he points out that the *Erklärung* of the concept “between” provides a proper definition, as its characteristic conditions (*Merkmale*) are given by the five axioms II 1 through II 5 that involve “between”. He writes, if one wanted to take “definition” in exactly the traditional sense, then one would have to say:

> “Between” is a relation for the points of a line that satisfies the following characteristic conditions: II 1 … II 5. (Gabriel et al. 1980: 11)

He emphasizes that he has absolutely no objection, if Frege called his axioms simply characteristic conditions. He asserts most clearly:

> The renaming of “axioms” as “characteristic conditions” etc. is a pure formality and, in addition, a matter of taste—in any event, it is easily accomplished. (Gabriel et al. 1980: 12)

Let us see briefly how this perspective allows us to understand properly the completeness axiom that is frequently criticized as being metamathematical and, to boot, a statement of a peculiar sort.[^note-36]

The completeness axiom requires in both the geometric and arithmetic case that the assumed structure is maximal, i.e., any extension satisfying the remaining axioms must already be contained in it. In the case of the arithmetic of real numbers, we can proceed as follows: Call a field *continuous* when it satisfies the axioms of an ordered field and the Archimedean axiom; a system A is called *fully continuous* or *complete* if and only if A is continuous and for any system B, if A is a subfield of B and B is continuous, then B is a subfield of A. Hilbert’s arithmetic axioms are equivalent to Dedekind’s characteristic conditions for a complete ordered field and characterize the fully continuous systems up to isomorphism.

### A.2 Consistency: no internal contradictions

In the 1920s, Hilbert and Bernays called this way of proceeding, because it assumes the existence of a suitable system, *existential axiomatics*. Hilbert’s view of axioms as characterizing a system of things is complemented by the traditional one, namely, that the axioms must allow to establish, purely logically, all geometric facts and laws. It is reflected for arithmetic in the Paris lecture, where he states that the totality of real numbers is

> … a system of things whose mutual relations are governed by the axioms set up and for which all propositions, and only those, are true which can be derived from the axioms by a finite number of logical inferences. (Hilbert 1900a: 1092)

It is Hilbert’s firm view that “the concept of the continuum is strictly logically tenable in this sense only” and that the axiomatic method has to confront two fundamental problems, formulated in 1900 at first for geometry and then for arithmetic:

> The necessary task then arises of showing the consistency and the completeness of these axioms, i.e., it must be proved that the application of the given axioms can never lead to contradictions, and, further, that the system of axioms suffices to prove all geometric propositions. (Hilbert 1900a: 1092–1093)

It is not clear, whether completeness requires the proof of *all* true geometric, or arithmetic, statements or of just those that are part of the established corpus; the latter would be a *quasi-empirical* notion of completeness. Turning to the central topic of consistency, we observe that the notion was viewed as a “semantic” one not only by Dedekind, but also by logicians in the nineteenth century more generally. In the essay (1888) and his letter to Keferstein (1890), Dedekind sharply expresses a crucial requirement for a structural definition; namely, one has to logically prove the existence of a system of things falling under the notion in order to ensure that it does not contain “internal contradictions”. The considerations in 1872 that pertain to cuts of rational numbers establish that the system of cuts falls under the concept of a complete ordered field; in more modern terms, the system of cuts is a complete ordered field, as it *satisfies* the *Merkmale* of the notion. If one views these *Merkmale* as axioms formulated in an appropriate language, then the system of cuts provides a *model* of these axioms.

This is a pre-Tarskian notion of semantics introduced in Hilbert 1917/18, but rooted—via the indicated connection to satisfying the conditions of a structural definition—in the mathematical practice of the late nineteenth century. It is used in Hilbert & Ackermann 1928 and also in Gödel’s dissertation (1929) that is following, as Gödel himself emphasizes, Hilbert and Ackermann’s terminology. Of course, in Gödel’s thesis this is done only for the language of first-order logic or the “restricted function calculus”. The formulae of the latter, *logische Ausdrücke*, are built up from individual variables $(x_1, x_2, \ldots)$, function variables $(F_1, F_2, \ldots)$, and statement variables $(X_1, X_2,\ldots)$. Meaning is given to these complexes of symbols in the following way:

> Let *A* be any logical expression that contains the function variables $F_1$, $F_2$,…, $F_k$, the free individual variables $x_1$, $x_2$,…, $x_l$ and the statement variables $X_1$, $X_2$,…, $X_m$ and otherwise only bound variables. Let $f_1$, $f_2$,…, $f_k$ be functions (all defined in the same domain of thought), $a_1$, $a_2$,…, $a_l$ individuals (belonging also to the same domain of thought), and $A_1$, $A_2$,…, $A_m$ statements; of this system
>
> $$S = (f_1, f_2, \ldots, f_k; a_1, a_2,\ldots, a_l; A_1, A_2, \ldots, A_m)$$
>
> we say that it *satisfies* the logical expression, if it yields, when placed into it [the expression], a true proposition ([true] in the domain of thought under consideration). (Gödel 1929 [1986: 66–68])[^note-37]

There is no further explication of “true proposition”. Let us note that Gödel later discusses a language expanded by individual constants (names) and function constants (relation symbols). He distinguishes *logische Ausdrücke* from *Zählausdrücke*: the latter contain neither function nor statement variables and all individual variables are bound. *Zählaxiomensysteme* are defined as consisting only of *Zählausdrücke*. As an example of such an axiom system he mentions in note 10 Hilbert’s system for geometry without the continuity axioms, i.e., the Archimedean principle and the completeness axiom. For the metamathematical investigation the axioms “with a fixed interpretation” are replaced by corresponding logical expressions: Gödel solves the completeness problem for *Zählaxiomensysteme* by reducing it by this technique to the solution for the corresponding axiom system. But let us return to Hilbert’s earlier work.

In 1899 and 1900a,b, Hilbert formulated a (quasi-) syntactic notion of consistency: no finite number of logical steps lead (from given axioms) to a contradiction. That does not mean, however, he sought to prove consistency by syntactic methods. The (relative) consistency proofs in 1899 are all semantic. In 1900a, Hilbert expected to prove the consistency of arithmetic by “a suitable modification of familiar methods of inference”. In the Paris Lecture he suggests finding a *direct method* of proof; but he still thought that such a method would emerge from a suitable modification of known methods. Hilbert believed, it seems, that the genetic build-up of the real numbers could somehow be exploited to yield the blueprint for a consistency proof in Dedekind’s logicist style. That impression is supported by his treatment of arithmetic in contemporaneous lectures, but also by a more programmatic statement from the *Introduction* to the notes for the lectures *Elemente der Euklidischen Geometrie* that were given in the winter term 1898/99. He maintains there,

> It is important to fix precisely the starting-point of our investigations: as given we consider the laws of pure logic and in particular all of arithmetic. (Hilbert 1898/99: 303).

Hilbert adds then parenthetically, “On the relation between logic and arithmetic cf. Dedekind, *Was sind und was sollen die Zahlen?*” and, for Dedekind, arithmetic is clearly part of logic.

Hilbert changed his attitude only after the discovery of the elementary contradiction of Russell and Zermelo.[^note-38] That paradox convinced him that there was a deep problem, that difficulties appeared already at an earlier stage, and that the issue had to be addressed in a different way. In early 1904 Hilbert sent a letter to Adolf Hurwitz writing:

> It has been my view for a long time that exactly the most important and most interesting questions have not been settled by Dedekind and Cantor (and a fortiori not by Weierstrass and Kronecker). In order to be forced into the position to reflect on these matters systematically, I announced a seminar on the “logical foundations of mathematical thought” for next semester. (Dugac 1976: 271)

The notes from the following summer term contain complimentary remarks on Dedekind’s achievements, but insist pointedly that basic difficulties remain.

> He [Dedekind] arrived at the view that the standpoint of considering the integers as obvious [*selbstverständlich*] cannot be sustained; he recognized that the difficulties Kronecker saw in the definition of irrationals arise already for integers; furthermore, if they are removed here, they disappear there. This work [*Was sind und was sollen die Zahlen?*] was epochal, but it did not yet provide something definitive, certain difficulties remain. These difficulties are connected, as for the definition of the irrationals, above all to the concept of the infinite; … (Hilbert 1904: 166)

This set the stage for Hilbert’s Heidelberg talk in August of that year, 1904, in which he indicates a novel way of solving the consistency problem for arithmetic. The sense in which he takes arithmetic now is more restricted, namely, as dealing with just the natural numbers.

### A.3 Formal proofs

Hilbert’s Heidelberg talk takes on the consistency problem with a striking syntactic approach. The goal is still securing the existence of a suitable model, that means here “the consistent existence of the so-called smallest infinite”. The system consists of axioms for identity and Dedekind’s conditions for a *simply infinite system*; the induction principle is mentioned, but neither formulated nor treated in the consistency argument. In modern notation the axioms can be given in this way, where *W* is a “formula”:

$$\begin{align} \tag{1} &x =x\\ \tag{2} &x =y \; \land\; W(x) \rightarrow W(y)\\ \tag{3} &x' =y' \rightarrow x=y\\ \tag{4} &x' \ne 1\\ \end{align}$$

The rules, implicit in Hilbert’s description of “consequence”, are *modus ponens* and a substitution rule allowing the replacement of variables by arbitrary sign combinations. Other “modes of logical inferences” are alluded to but not stated, and they are consequently not incorporated into the consistency proof. The view that the problem for the real numbers is resolved once matters are settled for the natural numbers is strongly emphasized.

For the consistency proof Hilbert calls an equation $a=b$ *homogeneous* if *a* and *b* have the same number of symbol occurrences. It is easily seen, by induction on derivations, that all equations derivable from axioms (1)–(3) are homogeneous. A contradiction can be obtained only by establishing an unnegated instance of (4) from (1)–(3); such an instance is necessarily inhomogeneous and thus not provable. Hilbert comments:

> The considerations just sketched constitute the first case in which a direct proof of consistency has been successfully carried out for axioms, whereas the method of a suitable specialization, or of the construction of examples, which is otherwise customary for such proofs—in geometry in particular—necessarily fails here. (Hilbert 1905 [1967: 135])

Hilbert stressed the programmatic goal of developing logic and mathematics simultaneously, but the actual work has real shortcomings: as to the logical work, there is no calculus for sentential logic and there is no proper treatment of quantification; as to the mathematical work, not even the induction principle is formulated. In sum, there is an important shift from “semantic” to “syntactic” arguments, but the formal set-up is woefully inadequate as a frame for mathematics.

The foundational import of Hilbert’s considerations was challenged by Poincaré, interpreting the results in a very generous way as including the treatment of induction. As the consistency proof proceeded by induction, Poincaré raised not only the question, how it could be viewed as justifying induction, but also brought out additional *methodological shortcomings* (Poincaré 1905 [1996: 1026–7]).[^note-39] His incisive analysis shifted Hilbert’s attention not away from foundational concerns—they are documented by lectures given throughout the period from 1905 to 1921—but rather from the “proof-theoretic” approach advocated in the Heidelberg talk. Indeed, under the impact of a detailed study of *Principia Mathematica* beginning in 1913, Hilbert flirted again with logicism.[^note-40] What resulted from this study were the lectures *Prinzipien der Mathematik*. Hilbert gave them in the winter term of 1917/18 with the assistance of Paul Bernays; these lectures present modern mathematical logic and provide a comprehensive formalism for representing mathematical practice, in particular, for developing analysis in ramified type theory with the axiom of reducibility.

The programmatic logicism in Hilbert’s Zürich talk and these lectures was abandoned in the following years. A radical constructivism for developing mathematics from the ground up replaced it, but was abandoned as well, because even basic logical laws were seen not to hold, e.g., the law of the excluded middle. The finitist consistency program, as we think of it, was only formulated towards the end of lectures given in the winter term 1921/22. The elementary character of the formalisms for mathematics allowed viewing the metamathematical studies as part of *constructive mathematics*. This new, still tentative perspective was connected to Hilbert’s approach in his Heidelberg talk; indeed, that approach had been reviewed and modified in 1920/21. The broad considerations and preliminary results were presented in talks in Copenhagen and Hamburg given in the spring and summer of 1921. In his 1922 paper, based on these talks, Hilbert claimed that induction had been avoided by restructuring the consistency proof and that Poincaré’s objection had consequently been met.

In September of 1921, Bernays presented a paper at the meeting of the German Association of Mathematicians (DMV) in Jena. The paper was published as Bernays 1922 and starts out with a discussion of *existential axiomatics* that presupposes, as we saw in A.2, a system of objects satisfying the structural conditions formulated by the axioms. As the assumption of such a system contains “something so-to-speak transcendent for mathematics”, the question arises, “which principled position with respect to it should be taken”. Bernays remarks that it might be perfectly coherent to appeal to an intuitive grasp of the natural number sequence or even of the manifold of real numbers. However, that could not be an intuition in any primitive sense, and one should take seriously the tendency of the exact sciences to use only restricted means to acquire knowledge, as far as that can be done. He was led to the question,

> whether it is not possible to give a foundation to these transcendent assumptions in such a way that only primitive intuitive knowledge is used. (Bernays 1922: 11)

Contentual mathematics is to be based on primitive intuitive knowledge and includes for Bernays, at this stage, induction—both as a proof and definition principle concerning the natural numbers. In the outline (*Disposition*) for the lectures to be given in the winter term 1921/22, Bernays discusses “constructive arithmetic” (*konstruktive Arithmetik*) and then the “broader formulation of constructive thought” (*konstruktiver Gedanke*):

> Construction of the proofs, by means of which the formalization of the higher inferences is made possible and the consistency problem is becoming accessible in a general way. (Bernays 1921: 123–124)

### A.4 Gödel’s incompleteness results

On 26 August 1930, Gödel met with Rudolf Carnap and Friedrich Waismann at the Café Reichsrat; the main topic of conversation was their upcoming trip to Königsberg, from Vienna of course. Reflecting a dramatic shift away from travel preparations, Carnap noted that the discussion turned to “Gödel’s discovery: Incompleteness of the system of *Principia Mathematica*; difficulty of the consistency proof”.[^note-41] In Königsberg the three attended the *Conference for Epistemology of the Exact Sciences* that was held there from 5 to 7 September. On the very first day of the conference, Carnap and Waismann gave plenary lectures on the foundations of mathematics presenting the logicist position and Wittgenstein’s views, respectively; von Neumann and Heyting gave complementary lectures on the formalist and intuitionist standpoints. On the next day Gödel presented the results of his thesis claiming at the very end of his talk[^note-42] that the completeness result for first-order logic cannot be extended to “the higher parts of logic (the extended functional calculus)”. After all, together with the categorical characterization of natural and real numbers, such a result would imply the “solvability of every problem of arithmetic and analysis expressible in *Principia Mathematica*”. That conclusion, he argued, conflicts with a fact he had recently established, namely, that

> … there are mathematical problems which can be expressed in *Principia Mathematica* but cannot be solved by the logical devices of *Principia Mathematica*.

The latter fact, Gödel asserted, can also be expressed as follows:

> The Peano axiom system, with the logic of *Principia Mathematica* as superstructure, is not syntactically complete.

Carnap, Heyting, von Neumann, Waismann and Gödel were among the participants of a roundtable discussion “Zur Grundlegung der Mathematik” that took place on 7 September, the last day of the conference, and was chaired by Gödel’s thesis advisor Hans Hahn. At that occasion, Gödel presented his result in greater detail, but also with a different emphasis. (The stenographic notes of Gödel’s remarks were published in the 1931 issue of the journal *Erkenntnis* together with a Postscriptum (*Nachtrag*, 1931b) that summarizes the mathematical results of Gödel 1931a.) Now he connects his considerations closely with Hilbert’s program and argues, the consistency of a formal theory *A* for classical mathematics does not guarantee that all theorems of *A* are “contentually correct” (*inhaltlich richtig*). At first he views it as “quite possible” that

> … one might prove a statement of the form $(Ex)F(x)$, where *F* is a finitist property of natural numbers (the negation of Goldbach’s conjecture, e.g., has this form) by the transfinite means of classical mathematics and yet ascertain by contentual considerations that all numbers have the property *not-F*; this remains possible, and that’s what I would like to point out, even if the consistency of the formal system for classical mathematics had been proved. For of no formal system can one claim that all contentual considerations are representable in it. (Gödel 1931b: 200)

In a second remark, he strengthens the claim that “one might prove a statement” to the assertion, “one can indeed give examples of statements” that are contentually correct but unprovable in A, if the latter is consistent. He concludes: Thus, if one adjoins the negation of such a statement to the axioms of classical mathematics, then one obtains a consistent system in which a contentually false statement is provable. Let us explore now, how Gödel seems to have convinced himself of that state of mathematical affairs. This reconstruction is based on Wang 1981 and the long first section of Gödel 1931a that sketches the “main idea of the proof” and assumes the semantic soundness of classical mathematics; in the core of the paper, soundness is replaced by the weaker syntactic conditions of consistency and $\omega$-consistency.[^note-43]

Ironically, the main idea exploits two features that made Hilbert’s finitist program plausible: (1) strong formal theories *T*, like Principia Mathematica or Zermelo-Fraenkel set theory, allow the formalization of mathematics, and (2) the formal theories can be described in a very elementary part of mathematics, finitist mathematics. The latter descriptions are precise and can be involved in rigorous mathematical arguments; after all, a finitist proof of the consistency of formal theories was sought and actually given for a fragment of arithmetic. It was also clear that elementary combinatorial concepts could be defined in the formal theories. Gödel observed that metamathematical notions like FORM(ULA) and PROOF can be *provably* (in metamathematics) *represented* by formulae in the language of *T*; that amounts, say for FORM, to having a formula *form* in the language of *T* such that: If FORM($\varphi$) then $T \vdash \textit{form}({\Corner{\varphi}})$, and If NOT FORM($\varphi$) then $T\vdash \neg \textit{form}({\Corner{\varphi}})$. Here ${\Corner{\varphi}}$ is a closed term in the language of *T* that serves as a name for the formula $\varphi$.

One way of achieving such a naming scheme is to require that *T* have names for natural numbers, i.e., *numerals*, and allow for the formation of sequences (of sequences) of numerals. The numerals can be used, non-standardly, as names or *codes* for the basic symbols of *T*’s language; the numeral used, for example, as the code for the conjunction symbol $\land$ is indicated by ${\Corner{\land}}$. As a formula $\varphi$ of the language of *T* is a sequence of basic symbols, it is coded by the corresponding sequence of the codes for the basic symbols that make up $\varphi$; that sequence is denoted by ${\Corner{\varphi}}$.[^note-44] A proof *D* of $\varphi$ is similarly a sequence of formulae (having $\varphi$ as their last element) and thus can be coded by the corresponding sequence of codes for the formulae that make up *D*; ${\Corner{D}}$ is the code for *D*. For the metamathematical notion PROOF there is a formula *proof* in the language of *T* that represents it.[^note-45] Clearly, $\varphi$ is a theorem if it has a proof, i.e., FOR SOME *D*, PROOF (*D*, $\varphi$). Defining the formal notion *theorem* in the same way from *proof*, we can easily prove: If THEOREM($\varphi$) then $T\vdash \textit{theorem}({\Corner{\varphi}})$. (As we will see, the corresponding condition for NOT THEOREM($\varphi$) is not provable for sufficiently strong *T*.)

This way of “internalizing” the syntactic description of *T* in *T* allows us, in particular, to formulate a self-referential statement *G* that expresses its own unprovability in *T*.[^note-46] If *T* is sound, *G* is seen to be independent of *T* as follows. Assuming that *T* proves *G*, soundness guarantees the truth of *G* and consequently the unprovability of *G*; thus, *T* does not prove *G*. Assuming that *T* proves $\neg G$, soundness guarantees the falsity of *G*, i.e., *T* proves *G*, contradicting the consistency of *T*; thus, *T* does not prove $\neg G$. In sum then, neither *G* nor $\neg G$ is provable in *T*. In section 7 of the Princeton notes, Gödel indicates a way of obtaining *G* that he attributes to Carnap 1934. It starts with a general “self-reference lemma”: for any formula $\varphi(x)$ with the free variable *x*, one can construct a sentence *S* such that *T* proves the equivalence of *S* and $\varphi({\Corner{S}})$. This allows us to prove that an adequate notion of truth cannot be defined in *T*, as that would make possible the construction of the “liar sentence” saying of itself that it is false. As the concept of a theorem of *T* is definable in *T*, assuming again the soundness of *T*, the set of provable sentences is a proper subset of the true ones. Thus, there is some sentence *A* that is true but not provable; indeed, as $\neg A$ is false and *T* is sound, *A* is independent of *T*. Gödel emphasizes in footnote 26,

> One thus obtains a proof for the existence of undecidable propositions in that system, but no individual instance of an undecidable proposition. (1934 [1986: 363])

All of this concerns the first incompleteness theorem. At the end of the first section of his 1931a, Gödel remarks that the formally undecidable sentence *G* can be decided by metamathematical considerations and continues:

> The precise analysis of this curious situation leads to surprising results concerning the consistency proofs of formal theories, that will be presented in greater detail in section 4 (Theorem XI). (Gödel 1931a: 150)

Gödel discovered this theorem only after the Königsberg congress; it is his second incompleteness theorem, asserting that the formal statement *cons* expressing the consistency of a theory cannot be proved in the theory. For its proof, Gödel suggested formalizing the argument for the first incompleteness theorem in order to obtain the statement $(\textit{cons} \rightarrow G)$ as a theorem of *Principia Mathematica*. Then, evidently, *cons* cannot be established in the system, as that would allow a formal proof of *G*, contradicting the first theorem. Independently, von Neumann found a way of proving more directly the equivalence of *G* and *cons* to be discussed below. That came about as follows: right after the roundtable discussion von Neumann had a private conversation with Gödel, important aspects of which are reported in Wang 1981: 654–655:

> In this discussion, von Neumann asked whether number theoretical undecidable propositions could also be constructed, in view of the fact that the combinatorial objects can be mapped onto the integers, and expressed the belief that it could be done. In reply, Gödel said, “Of course undecidable propositions about integers could be so constructed, but they would contain concepts quite different from those occurring in number theory like addition and multiplication”. Shortly afterward Gödel, to his own astonishment, succeeded in turning the undecidable proposition into polynomial form preceded by quantifiers (over natural numbers).

Von Neumann was very enthusiastic about the result Gödel had found and was preoccupied with it during the following months. We get a sense of that from Herbrand’s letter to his friend Claude Chevalley, when he writes from Berlin on 3 December 1930:

> Mathematicians are a strange bunch; I have been here for two weeks, and each time I see von Neumann, we talk about a paper by a certain Gödel, who has produced quite curious statements; and all this destroys some very solidly anchored ideas.[^note-47]

This sentence opens the letter. Having sketched Gödel’s arguments, Herbrand concludes the metamathematical discussion with, “Please excuse this long beginning; but all of this haunts me, and by writing about it I can exorcise it a bit”.

Von Neumann communicated the outcome of his reflections to Gödel in a letter of 20 November 1930 announcing as a “new result” that the consistency of classical mathematics is unprovable. The reasoning for von Neumann’s result was articulated more sharply in a letter of 12 January 1931, which he wrote after having received the galleys of Gödel’s 1931a paper with its dramatic expansion of methods and results. Metamathematically von Neumann claimed—in contrast to Gödel’s sketch of a formal proof of the first incompleteness theorem—the equivalence of the sentence *G* with the consistency statement *cons* assuming general properties of the theorem predicate for formal theories. (That’s what Hilbert and Bernays would do in great detail and precisely in their 1939 through representability and derivability conditions.) Methodologically he argued—in opposition to Gödel’s conjecture—that intuitionist or, synonymously at the time, finitist proofs can be formally captured in elementary arithmetic or, if not there, then certainly in analysis or set theory.[^note-48]


## Notes（原文脚注，引自主文）

[^note-35]: 35. These four conditions correspond to the conditions $(\alpha)$ through $(\delta)$ of $\#71$ in Dedekind 1888; they are easily seen to be equivalent to the so-called Peano axioms. The *chain* of the system $\{1\}$ (with respect to the mapping $\varphi$ of N) is the intersection of all systems that contain 1 as an element and are closed under $\varphi$.

[^note-36]: 36. In Torretti 1978 [1984: 234], for example, one finds the following observation:

> … the completeness axiom is what nowadays one would call a metamathematical statement, though one of a rather peculiar sort, since the theory with which it is concerned includes Axiom V2 [i.e., the completeness axiom] itself.

[^note-37]: 37. We have modified the translation one finds in the *Collected Works*. In particular, logical expression stands for *logischer Ausdruck*, satisfy for *erfüllen*, domain of thought for *Denkbereich*, statement for *Aussage*, and proposition for *Satz*.

[^note-38]: 38. In *On the Infinite* Hilbert writes retrospectively:

> In particular, a contradiction discovered by Zermelo and Russell had, when it became known, a downright catastrophic effect in the world of mathematics. (Hilbert 1926: 375)

More can be learnt about Hilbert’s reaction at the time from various reports in 1902 and 1903 (cf. Peckhaus 1990: 57).

[^note-39]: 39. One should keep in mind that the “existence of sets” was the central issue, and it was to be guaranteed by the consistency of an appropriate axiom system, a viewpoint shared by Poincaré. The latter was, on the whole, impressed by Hilbert’s novel approach.

[^note-40]: 40. See Mancosu 1999b. Not only the details of *Principia Mathematica* were of significance; on the contrary, the broad logicist outlook had a real impact on Hilbert. Hilbert’s notes for a course on *Set Theory* (from the summer term 1917) and his talk *Axiomatisches Denken* reveal a logicist direction in his work. In the latter essay Hilbert writes:

> The examination of consistency is an unavoidable task; thus, it seems to be necessary to axiomatize logic itself and *to show that number theory as well as set theory are just parts of logic*. (Hilbert 1918: 153).

If we try to achieve such a reduction to logic, Hilbert says at the very end of the set theory notes, “… we are facing one of the most difficult problems of mathematics”. (Hilbert 1917)

[^note-41]: 41. This is reported in Dawson 1997 (p. 68) based on doc 023-73-04 in the Carnap Nachlass at the University of Pittsburgh.

[^note-42]: 42. Volume III of Gödel’s Collected Works contains a paper entitled “Vortrag über Vollständigkeit des Funktionenkalkül’s” that is taken to be the manuscript for his talk in Königsberg. However, Gödel’s talk was a contributed talk of just 20 minutes; only a small part of the paper could have been delivered.

[^note-43]: 43. The historical context and relevant details are presented in Sieg 2012.

[^note-44]: 44. More precisely, we define a function CODE by recursion on formulae that associates with each formula $\varphi$ a term in the language of $T$, which is also denoted by ${\Corner{\varphi}}$.

[^note-45]: 45. The representability conditions for PROOF are as follows: If PROOF$(D, \varphi)$ then $T \vdash \iproof(\Corner{D},\Corner{\varphi})$, and if NOT PROOF$(D,\varphi)$ then $T\vdash \neg \iproof(\Corner{D},\Corner{\varphi})$.

[^note-46]: 46. Note that *G* is, as Dawson put it (on p. 68), “an involved combinatorial statement expressed in the richer language of the system of *Principia Mathematica*” (or set theory). It is only after the “arithmetization of syntax” and the representation of the syntactic notions in elementary number theory that *G* is turned into an arithmetical statement; section 3 of Gödel 1931a. See the remarks below from Wang 1981 concerning this development after the Königsberg conference, and the further very detailed description of how *G* is equivalent to a Diophantine equation in section 8 of Gödel’s 1934 Princeton lectures and in Gödel 1938/9.

[^note-47]: 47. The letter, to the best of our knowledge, has not been published. One of the authors, Sieg, had received a copy from Chevalley’s daughter quite a few years ago.

[^note-48]: 48. As to the details of their interaction, see the Introductory Notes to Gödel’s correspondence with von Neumann and Herbrand, in volume V of the *Collected Works*. Gödel’s contrary perspective on the formalizability of finitist proofs is expressed not only at the end of his 1931 paper, but also in his letters to von Neumann and Herbrand, as well as in his contribution to the meeting of the Schlick Circle on 15 January 1931 and in the “*Nachtrag*” to his Königsberg remarks. In the latter he wrote:

> For a system in which all finitist (i.e., intuitionistically proper) forms of proof are formalized, a finitist consistency proof as sought by the formalists would be altogether impossible. However, it seems doubtful, whether one of the systems formulated up to now, say *Principia Mathematica*, is so comprehensive (or whether such a comprehensive system exists at all). (Gödel 1931b: 204).

### Notes to Appendix B