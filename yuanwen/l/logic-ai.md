# Logic-Based Artificial Intelligence
**First published Wed Aug 27, 2003; substantive revision Tue Feb 27, 2024**

*Thomason, Richmond*

Artificial Intelligence (referred to hereafter by its nickname, “AI”) is the subfield of Computer Science devoted to developing programs that enable computers to display behavior that can (broadly) be characterized as intelligent.[^note-1]

Many of the most influential figures in AI’s early days had ambitious goals and views about how to obtain them. John McCarthy’s plan was to use ideas from philosophical logic to formalize commonsense reasoning. During his lifetime he and his students and associates pursued projects with a distinctly philosophical flavor. This theme has persisted, but has mostly been absorbed into work in knowledge representation. It has become more directly concerned with applications; the connections to philosophy and philosophical logic remain, but are more tenuous.

The new insights and theories that have emerged from AI are of great potential value in informing and constraining any area of philosophical inquiry where reasoning is important—reasoning about what to do, for instance, or about our own attitudes or the attitudes of others. Although logic in AI grew out of philosophical logic, in this new setting it has produced new theories and ambitious programs that could only have been nurtured by a community devoted to building working, large-scale computational models of rational agency.

This entry assumes an audience consisting primarily of philosophers who have little or no familiarity with AI. It concentrates on the issues that arise when logic is used in understanding intelligent reasoning in mechanized reasoning systems. And it provides a selective overview, without attempting to achieve anything like complete coverage. Sections 3 and 4 describe two important themes that arose early and have continued to the present: nonmonotonic logic and reasoning about action and change. The remaining sections sketch selected topics, with references to the primary literature.

## 1. Logic in Artificial Intelligence

### 1.1 The Role of Logic in Artificial Intelligence

Theoretical computer science developed out of logic, the theory of computation (if this is to be considered a different subject from logic), and related areas of mathematics.[^note-2] So most computer scientists are well informed about logic even if they aren’t logicians. They are familiar with the idea that logic provides techniques for analyzing the inferential properties of languages, and with the distinction between a high-level logical analysis of a reasoning problem and its implementations. Logic can, for instance, provide a specification for a programming language by mapping programs to the computations that they should license and enabling proofs that these computations conform to certain standards.

Often, however, the connection between logic and computer programs is looser than this. Certainly, a software application can be said to implement a logical formalization when it is provably sound and complete—but also merely when logical ideas informed parts of the software development process. A program that is said to implement a logical model can be incomplete, or even unsound.

Sometimes parts of a working system are inspired by ideas from logic while other parts seem logically problematic. These challenging features may suggest improvements to the logical theory. So logical theory informs applications, and applications challenge logical theory and can lead to theoretical innovations. Logic programming provides many examples of such interactions.

Even limited-objective reasoning systems can call for large, complex bodies of declarative information. It is generally recognized in AI that it is important to treat declarative representations, along with their retrieval and maintenance and the reasoning systems they service as separate items, each with its own research problems. The evolution of expert systems illustrates the point. The earliest expert systems were based entirely on large systems of procedural rules, with no separate representation of the background knowledge. But later generation expert systems show a greater modularity in their design. A separate knowledge representation component is useful for software engineering purposes—it is much better to have a single representation of a general fact, capable of many different uses and making the system easier to develop and to modify. This modularity is essential in enabling these systems to deliver explanations as well as mere conclusions.[^note-3]

In response to the need to design this declarative component, a subfield of AI known as *knowledge representation* emerged during the 1980s. Conferences devoted to this topic have taken place since 1989; these provide an in-depth record of research in the field. See Section 12. for a list of the proceedings.

Typical presentations at the KR and Reasoning conferences deal with the following topics.

1. Topics in logical theory and the theory of computation, including
2. Nonmonotonic logic
3. Complexity theory
4. Studies in application areas, including
5. Temporal reasoning
6. Formalisms for reasoning about planning, action and change, and causality
7. Metareasoning
8. Reasoning about context
9. Reasoning about values and desires
10. Reasoning about the mental states of other agents, and especially about knowledge and belief
11. Spatial reasoning
12. Reasoning about vagueness
13. Argumentation and argumentation theory
14. Aggregation problems of many kinds, such as the integration of conflicting knowledge sources
15. Studies in applicable techniques, including
16. Logic programming
17. Description logics
18. Theorem proving
19. Model construction
20. Studies of large-scale applications, including
21. Cognitive robotics
22. Creating, merging, updating, and correcting knowledge bases
23. Querying knowledge bases

These topics have little in common with the contents of the *Journal of Symbolic Logic*, the premier journal of record for mathematical logic. But there is substantial overlap with *The Journal of Philosophical Logic*, especially in topics such as tense logic, epistemic logic, logical approaches to practical reasoning, and belief change. Of course, there also are differences; very few *JPL* publications deal with complexity theory or with potential applications to automated reasoning.

### 1.2 Philosophical Logic

Founded in 1936, the *JSL* sought to bring together mathematicians and philosophers working in logic. Articles in the first volume were divided about equally between professional mathematicians and philosophers, and the early volumes do not show any strong differences between the two groups as to topic.

This situation changed in the 1960s. The 1969 volume of the *JSL* contained 39 articles by mathematicians, and only nine by philosophers. By the early 1970s, many philosophers felt that philosophical papers on logic were unlikely to be accepted by the *JSL*, and that those that were accepted were unlikely to be read by philosophers. At this point, the two groups had diverged markedly. Mathematicians pursued the development of an increasingly technical and complex body of methods and theorems, and many philosophers saw this trend as unilluminating and philosophically irrelevant. These divisions led to the founding of the *Journal of Philosophical Logic* in 1972. The list of sample topics in the first issue included:

1. Contributions to branches of logical theory directly related to philosophical concerns, such as inductive logic, modal logic, deontic logic, quantum logic, tense logic, free logic, logic of questions, logic of commands, logic of preference, logic of conditionals, many-valued logic, relevance logics;
2. Contributions to philosophical discussions that utilize the machinery of formal logic …;
3. Discussions of philosophical issues relating to logic and the logical structure of language, …;
4. Philosophical work relating to the special sciences, ….

The common thread here is a desire to apply the methods of mathematical logic to nonmathematical domains. Quantum logic and the logic of induction, for instance, apply logic to physics and empirical science. Other topics in the *JPL* list concern developments in logic that might be helpful in addressing nonscientific reasoning.

### 1.3 Logic in AI and Philosophical Logic

McCarthy 1959, an early contribution to logical AI, discusses the problem of figuring out how to get to the airport. Here McCarthy proposes a realistic reasoning problem. Its solution may involve many connected inferences, and though ultimately it may look like a proof—a proof that performing certain actions will produce an outcome in which someone is located at an airport—it will differ from a mathematical exercise because it draws on broader and less tractable resources. These include causal knowledge as well as goals and preferences. Contrastingly, research papers in philosophical logic use reasoning examples to *illustrate,* rather than to *motivate* logical theory and the reasoning examples they cite are simple, isolated inferences.

It would not be far wrong to characterize early work in logical AI as philosophical logic devoted to a new and ambitious application area. And in fact the first generation of AI logicists[^note-4] read the literature in philosophical logic and were influenced by it. Subsequently, however, the specialties have diverged. New logical theories have emerged in logical AI (nonmonotonic logic is the most important example) which had not occurred to philosophers. The AI community’s interest in the theoretical analysis of algorithms and—of course—in useful technology are responsible for other differences. AI researchers are often concerned with ambitious applications using unprecedentedly large bodies of data and inferential rules. Their sheer size produces new problems and new methodologies. And on the other hand, philosophical logicians are philosophers and as such are often interested in topics (metaphysical topics, for instance) that are of no interest to computer scientists.

If philosophical logic and logic in AI continue to diverge, it will probably be for such methodological reasons. But despite this, the fundamental research goals are the same—logical AI is philosophical logic constrained by an interest in large-scale formalization and in feasible, implementable reasoning.

The early influence of philosophical logic on logic in AI was profound. The bibliography of McCarthy & Hayes 1969, one of the most influential early papers in logical AI, illustrates the point well. There are 58 citations in the bibliography. Of these, 35 refer to the philosophical logic literature. (There are 17 computer science citations, one mathematical logic citation, one economics citation, and one psychology citation.) This paper was written at a time when there were hardly any references to logical AI in the computer science literature. Naturally, as logical AI has matured and developed as a branch of computer science, the proportion of cross-disciplinary citations has decreased. A sampling of articles from the first Knowledge Representation conference, Brachman *et al*. 1989, held in 1989, shows only 12 philosophical logic citations out of a total of 522 sampled citations. A sampling of articles from Cohn *et al*. 1998, shows 23 philosophical logic citations out of a total of 468 sampled.[^note-5]

Despite the dramatic decrease in quantity of explicit citations, the later literature in logical AI reflects an indirect acquaintance with philosophical logic, by citing papers in CS venues that were directly influenced by philosophical work. Of course, the influence becomes increasingly tenuous as time passes, and this trend is accelerated by the fact that new theoretical topics have been invented in logical AI that were at best only dimly prefigured in the philosophical literature. In Europe, the lines are harder to draw between professional divisions among logicians. Some European journals, especially the *Journal of Logic, Language, and Information* and *Studia Logica*, are successful in maintaining a focus in logic while attracting authors from all the disciplines in which logic is represented.

In the final analysis, logic deals with reasoning—and relatively little of the reasoning we do is mathematical, while almost all of the mathematical reasoning done by nonmathematicians is mere calculation. To have scope as well as rigor, logic needs to maintain itself as a single discipline, uniting its mathematical and philosophical side. But the needs of Computer Science have added strong unifying motives for this unification, providing a novel methodology and relations to new, rewarding applications.

## 2. John McCarthy and Commonsense Logicism

### 2.1 Logic and AI

John McCarthy was, and remains, the most influential figure in logical AI. McCarthy was one of the founders of AI, and consistently advocated logical formalization as the path to human-level AI. All but the most recent work in McCarthy’s research program can be found in Lifschitz 1990a, which also contains Lifschitz 1990b, an introduction to McCarthy’s work. For additional historical background, see Israel 1991.

McCarthy’s views were first articulated in McCarthy 1959 and elaborated and amended in McCarthy & Hayes 1969. He felt that even if AI implementations do not straightforwardly use logical reasoning techniques like theorem proving, a logical formalization will help to understand the reasoning problem itself. The claim is that without a logical account of the reasoning domain, it will not be possible to implement the reasoning itself. This is in fact controversial. Many AI researchers see no need for logical formalization in their work. For instance, the products of machine learning will typically bear no discernible relation to logic, and depend on a combination of training corpora and cumulative learning experience. There will be no obvious way to characterize or understand them at a declarative, conceptual level, and their relation to logic will be problematic.

The recommendations of McCarthy & Hayes 1969, overlap to a large extent with those of analytic philosophy, but are directed at a different goal: programmable general intelligence rather than conceptual analysis. Similar goals have occurred to a few philosophers; see, for instance, Carnap 1956 (pp. 244–247) and Pollock 1995.

Assuming that most readers of this article will be interested in the relation between logical AI and philosophical logic, the remainder of this article will ignore relations both to philosophy in general and to the feasibility of developing human-level intelligent systems.

### 2.2 The Formalization of Common Sense

McCarthy’s long-term objective was to formalize *commonsense reasoning*, the prescientific reasoning that engages human thinking about everyday problems. We have mentioned a planning problem: how to get to the airport. Other examples include:

1. *Narrative understanding.* The reasoning involved in reconstructing implicit information from narratives, such as sequencing of eventualities, and inferred causal connections.
2. *Diagnosis.* For instance, explaining faults in physical devices on the basis of observations.
3. *Spatial Reasoning.* For instance, reasoning about the parts of rigid bodies and their shapes, and their relation to the shape of the whole.
4. *Reasoning about the attitudes of other agents.* For instance, making informed guesses about the beliefs and desires of other agents, either from “keyhole observation” or from conversational clues of the sort that could be obtained in a brief, interactive interview.

McCarthy’s goal will probably seem outrageous to most philosophers, who are trained to think of common sense as elusive and incoherent. But philosophers invoke common sense in relation to philosophical disputes, where its employment is problematic. McCarthy was thinking of everyday, practical common sense. We couldn’t manage to navigate simple daily tasks if common sense were not reliable in these settings. Formalizing the reasoning that supports these tasks may turn out to be impracticable, but the project itself is neither misguided nor quixotic.

Whether or not formalization is the secret to human-level AI, it has been successful on a smaller-scale—not only in unembodied settings[^note-6] but in online robot planning and execution. It is used in some approaches to complete, autonomous agents.[^note-7]. It plays an important role in multiagent systems, where communicating and reasoning about knowledge are critical.[^note-8] And it has illuminated qualitative reasoning about the behavior of physical devices.[^note-9]

## 3. Nonmonotonic Reasoning and Nonmonotonic Logics

### 3.1 Nonmonotonicity

While a mathematical proof must cover every contingency, practical reasoning routinely closes its eyes to some possibilities. Consider a plan to get to the airport. It could be impeded by an earthquakes, a meteor strike, or a highway accident. But it’s perfectly reasonable to ignore the first two factors, and often even the third can safely be ignored. Acceptance of a plan, unlike acceptance of a proof, is risky. In fact, risk and the possibility of unpleasant surprises are features of sound commonsense reasoning. This means that the reasoning is *nonmonotonic*.

Classical logics were designed with mathematics in mind and their consequence relations are monotonic. That is, if a set $T$ of formulas implies a consequence $B$ then a larger set $T \cup \{A\}$ will also imply $B$. A logic is nonmonotonic if its consequence relation lacks this property. *Preferred models* provide a general way to induce a nonmonotonic consequence relation. Invoke a function that for each $T$ produces a subset $\mathcal{M}_T$ of the models of $T$; in general, we will expect $\mathcal{M}_T$ to be a proper subset of these models. We then say that $T$ implies $B$ if $B$ is satisfied by every model in $\mathcal{M}_T$. As long as we do not suppose that $\mathcal{M}_{T} \subseteq \mathcal{M}_{S}$ if $S \subseteq T$, the implication relation will be nonmonotonic.

Improbability is not the only reason for disregarding a contingency. Other reasons include (1) a feeling for what is normal and usual; (2) epistemic excusability—immunity from any blame that may attach to ignoring a possibility; (3) the estimated costs of further deliberation; and (4) inattention and mere cognitive laziness. Some of these may be more “rational” than others, but in fact it isn’t easy to locate a boundary between rational and irrational factors. And probably no one has succeeded in clarifying and disentangling these motivating considerations.

In the early stages of its development. many researchers hoped that nonmonotonic logic would provide a general approach to efficient reasoning about uncertainty. But by the end of the 1980s, fully quantitative probabilistic reasoning had become not only implementable but clearly preferable in many sorts of applications to methods involving nonmonotonic logic. Nonmonotonicity is no magic path to efficient reasoning. It can be useful in reasoning about uncertainty. But so can probabilities.

### 3.2 Beginnings

Three influential papers on nonmonotonic logic appeared in 1980: McDermott & Doyle 1980, Reiter 1980, and McCarthy 1980. In each case, the formalisms presented in these papers emerged from a gestation period of several years or more. To set out the historical influences accurately, it would have been necessary to interview the authors, and this has not been done. However, there seem to have been two motivating factors: strategic considerations having to do with the long-range goals of AI, and much more specific, tactical considerations arising from the analysis of the reasoning systems that were being deployed in the 1970s.

Section 3.1 explained why if was generally felt that monotonicity renders classical logics unsuitable as a vehicle for formalizing commonsense reasoning. Minsky 1974, which was widely read at the time of its publication, helped to crystalize this attitude. Minsky’s paper presents an assortment of challenges for AI, focusing at the outset on the problem of natural language understanding.[^note-10] He advocates “frame-based” knowledge representation techniques[^note-11] and (conceiving these as an alternative to logic), he throws out a number of loosely connected challenges for the logical approach, including the following problems: building large-scale representations, reasoning efficiently, representing control knowledge, and providing for the flexible revision of defeasible beliefs. In retrospect, most AI researchers would likely agree that these problems are quite general challenges to any research program (including the one Minsky himself advocated at the time) and would add that logical techniques are an important element in addressing some, perhaps all, of the issues. For instance, a well structured logical design can be a great help in scaling up any computationally useful body of knowledge.

Perhaps unintentionally, Minsky’s paper incentivized nonmonotonic logicians by identifying monotonicity as a source of the alleged shortcomings of logic. Although Minsky apparently meant to discredit logical methods in AI, McDermott & Doyle 1980 and McCarthy 1980 interpret his criticisms as a challenge to be met by developing logics that lack the monotonicity property.

The development of nonmonotonic logic also owes much to the needs of AI applications. In fact, this influence was at least as persuasive as McCarthy’s strategic considerations, and in many ways more influential on the shape of the formalisms that emerged. Here, we mention three applications that appear to have been important for some of the early nonmonotonic logicians: belief revision, closed-world reasoning, and planning.

#### 3.2.1 Belief Revision

Doyle 1979 presents a “truth maintenance system.” Doyle’s truth maintenance algorithm answered a general need, providing a mechanism for updating the “beliefs” of a knowledge repository. The idea is to keep track of the support of beliefs, and to use the record of these support dependencies when it is necessary to revise beliefs.

In a TMS, part of the support for a belief can consist in the *absence* of some other belief. This introduces nonmonotonicity. For instance, it provides for defaults: beliefs that are induced by the absence of contrary beliefs.

The TMS algorithm and its refinements had a significant impact on AI applications, and this created the need for a logical analysis. (In even fairly simple cases, it can be hard in the absence of analytic tools to see what consequences a TMS should deliver.) This presented a natural and highly specific challenge for those seeking to develop a nonmonotonic logic. The TMS also provided the idea that nonmonotonicity has to do with inferences based on unprovability; this insight was important for modal approaches to nonmonotonic logic and for default logic. And the TMS’s emphasis on interactions between arguments initiated a theme in nonmonotonic logic that remains important to this day. *Abstract argumentation* is a framework for default reasoning with connections to logic programming that continues to receive much attention. See, for instance, Besnard & Hunter 2008 and Rahwan & Simari 2009.

#### 3.2.2 Closed-world reasoning

The study of databases in computer science has a logical side; see Minker 1997 for a survey. This area has interacted with logical AI. The deductive database paradigm was taking shape at about the same time that many AI researchers were thinking through the problems of nonmonotonic logic, and provided several specific examples of nonmonotonic reasoning that called for analysis. Of these, perhaps the most important is the *closed-world assumption*. According to this assumption—at least as far as simple claims (i.e. positive or negative literals) are concerned—the system assumes that it knows all that there is to be known. It is the closed world assumption that justifies a negative answer to a query “Is there a direct flight from Detroit to Bologna?” when the system finds no such flight in its data. This is another case of inference from the absence of a proof. A negative is proved, in effect, by the failure of a systematic attempt to prove the positive. This idea, which was investigated in papers such as Reiter 1978 and Clark 1978, provided a well-defined challenge for nonmonotonic logicians, as well as suggestions about how to address the challenge.

#### 3.2.3 Planning

Rational planning is impossible without the ability to reason about the outcomes of a series of contemplated actions. Predictive reasoning of this sort is local; in a complex world with many dynamic variables, we assume that most of these will be unchanged by the performance of an action. The problem of how to formalize such “causal inertia” is known as the *frame problem*.

It is very natural to suppose that inertia holds by default—that variables are unchanged by the performance of an action unless there is a special reason to think that they will change. This suggests that nonmonotonic temporal formalisms should apply usefully to reasoning about action and change, and in particular might address the frame problem. Sandewall 1972, is an early attempt along these lines. Later work in this direction provides an especially important and instructive case study of the use of logic in AI; see Section 4.4, for further discussion.

### 3.3 The Earliest Formalisms

Section 3.2 mentioned three influential approaches to nonmonotonic logic: *circumscription* (McCarthy), *modal approaches* (Doyle & McDermott) and *default logic* (Reiter).

In McCarthy 1993a, McCarthy urged us, when considering the early history of circumscription, to take into account a group of three papers: McCarthy 1986, 1980, and 1987. The first paper connects the strategic ideas of McCarthy & Hayes 1969 with the need for a nonmonotonic logic, and sketches the logical ideas of *domain circumscription*, the simplest case of circumscription. The second paper provides more thorough logical foundations, and introduces the more general and powerful *predicate circumscription* approach. The third paper discusses challenging commonsense examples and techniques for formalizing them.

All forms of circumscription involve restricting attention to models in which certain sets are minimized; for this reason, circumscription can be grouped with the preferred models treatments of nonmonotonicity. McCarthy’s approach is conservative: it uses classical second-order logic. Therefore the circumscription literature can avoid logical foundations and concentrate on formalizations. The other varieties of nonmonotonic logic, including default logic and the modal nonmonotonic logics, raise issues that will seem familiar to philosophical logicians. These have to do with the design of new logics, the systematic investigation of questions concerning validity, and managing the proliferation of alternative logics.

It is natural to think of nonmonotonic inferences as being *hedged*. That is, a nonmonotonic inference may require not merely the presence of proved conclusions, but the *absence* of other conclusions. The general form of such a default rule is:

**$\textbf{DR}$:**

In the presence of $\{A_1 ,\ldots ,A_n\}$ and in the absence of $\{B_1 ,\ldots ,B_m\}$, conclude $C$. We write such a rule as $A_1 ,\ldots ,A_n$ ; $B_1 ,\ldots ,B_m \leadsto C$.

An important special case of $\mathbf{DR}$ is a *normal default*, a simple rule to the effect that $C$ holds by default, conditionally on assumptions $A_1 ,\ldots ,A_n$. This can be formalized by taking the negation of the conclusion itself to be what must be absent.

**$\mathbf{NDR}$:**

In the presence of $\{A_1 ,\ldots ,A_n\}$ and in the absence of $\neg C$, conclude $C$, written as $A_1 ,\ldots ,A_n \leadsto C$. The special case stipulating that a conclusion $C$ holds by default is $\top \leadsto C$ or simply $\leadsto C$.

A *default theory* consists of two components: a set of formulas taken as axioms, and a set of default rules.

At first sight, it is perplexing how to characterize proofs in default logic, because the default account of provability is circular: proofs are defined in terms of chains of correct inferences, but correct inference is defined in terms of (non)provability. Therefore provability can’t be characterized inductively,, as in the monotonic case. The early theory of Sandewall 1972 didn’t address this difficulty successfully. McDermott & Doyle 1980 and Reiter 1980 propose solutions to this problem. In both cases, the logical task is (1) to develop a formalism in which rules like $\mathbf{DR}$ can be expressed, and (2) to define the relation between a combination $DT$ of nonmonotonic axioms and rules and the theories $E$ which could count as reasonable consequences of $DT$. In the terminology that later became standard, we need to define the relation between a default theory $DT$ and its *extensions*.

This is a radical departure from classical logic, which associates a single collection of consequences with an axiomatic basis. A default theory can determine many alternative consequence sets, with the logic itself providing no way to choose between them.

In retrospect, we can identify two approaches to nonmonotonic logic: those based on *preference* and those based on *conflict*. Theories of the first sort (like circumscription) involve a relatively straightforward modification of the ordinary model-theoretic definition of logical consequence, appealing to a preference relation over models. Theories of the second sort (like default logic) require a more radical reworking of logical ideas. The possibility of multiple extensions—different possible coherent, inferentially complete conclusion sets that can be drawn from a single set of premises—means that we have to think of logical consequence not as a function taking a set of axioms into its logical closure, but as a *relation* between a set of axioms and alternative logical closures. Since logical consequence is so fundamental, this represents a major theoretical departure. With multiple extensions, we can still retrieve a consequence relation between a theory and a formula in various ways, the simplest being to say that $DT$ nonmonotonically implies $C$ if $C$ is a member of every extension of $DT$. Still, the conflict-based account of consequence provides a much richer underlying structure than the preferential one.

Reiter approaches the formalization problem conservatively. The language of default logic is the same as the language of first-order logic and its formulas cannot express defaults. But a theory may involve a set of *default rules*—rules of the form $\mathbf{DR}$. A *default theory*, then, is a pair $\text{DT}=\langle W,D\rangle$ consisting of a set $W$ of (monotonic) axioms and a set $D$ of default rules. Reiter 1980 provides a fixpoint definition of the extensions of such a theory, and develops the theoretical groundwork for the approach, proving a number of the basic theorems.

Of these theorems, we mention one in particular, which will be used in Section 4.5, in connection with the Yale Shooting Anomaly. The idea is to take a conjectured extension (which will be a set $T^*$) and to use this set for consistency checks in a proof-like process that successively applies default rules in $\langle W,D\rangle$ to stages that begin with $W$.

We define a default proof process $T_0,T_1,\ldots$ for $\langle W,D\rangle$, relative to $T^*$, as follows.

- Let $T_0 = W$.
- If no default rule in $D$ is nonvacuously applicable to $T_i$ relative to $T^*$, then $T_{i+1} = \text{Th}_{\text{\small{FOL}}}(T_i)$, the logical closure in FOL of $T_i$.
- Otherwise, choose some default rule $A$ ; $B_1 ,\ldots ,B_m\leadsto C$ that is nonvacuously applicable to $T_i$ relative to $T^*$, and let $T_{i+1} = \text{Th}_{\text{\small{FOL}}}(T_i\cup \{C\})$.

In other words, as long as we can nonvacuously close the stage we are working on under an applicable default, we do so; otherwise, we do nothing. A theorem of Reiter’s says that, under these circumstances:

> $T$ is an extension of $\langle W, D\rangle$ if and only if there is a proof process $T_0, T_1,\ldots$ for $W, D$, relative to $T$, such that $T =\bigcup\{T_i :0\le i\}$.

Thus, we can show that $T$ is an extension by (1) constructing a default reasoning process $\{T_i\}$ from $\langle W, D\rangle$ that uses $T$ for consistency checks, (2) taking the limit $T'$ of this process, and (3) verifying that in fact $T' = T.$

The modal approach invokes a modal operator $L$, informally interpreted as ‘provable’.[^note-12] The essence of McDermott and Doyle’s approach, like Reiter’s, is a fixpoint definition of the extensions of a nonmonotonic logic. Incorporating nonmonotonicity in the object language creates some additional complexities, which in the early modal approach show up mainly in proliferation of the logics and difficulties in evaluating the merits of the alternatives. As better foundations for the modal account emerged, it became possible to prove, as was expected, the equivalence of the modal and default logic approaches.[^note-13]

Unlike other early presentations of nonmonotonic logic, Reiter’s shows specific influence from earlier and independent work on nonmonotonicity in logic programming—the work seems to have been largely inspired by the need to provide logical foundations for the nonmonotonic reasoning found in deductive databases. The subsequent history of nonomonotonic logic is intimately connected with the literature on logic programming semantics.

Doyle and McDermott’s paper cites the earlier literature in logicist AI, presenting nonmonotonic logic as part of a program of formalizing commonsense rationality. But this work is also clearly influenced by the need to provide a formal account of truth maintenance.

### 3.4 Later Work in Nonmonotonic Logic

Nonmonotonic logic is a complex, robust research field. Providing a survey of the subject is made difficult by the fact that there are many different foundational paradigms for formalizing nonmonotonic reasoning, and the relations between these paradigms is not simple. An adequate account of even a significant part of the field requires a something like a book-length treatment. A number of books and handbook articles are available, including Łukaszewicz 1990, Brewka 1991, Besnard 1992, Marek & Truszczynski 1994, Gabbay *et al*. 1994, Antoniou 1997, Brewka *et al*. 1997, Schlechta 1997, Makinson 2005, Antoniou & Wang 2007, Bochman 2007, Horty 2012, Straßer 2014, and Straßer & Antonelli 2019. The collection Ginsberg 1987 is a useful source for readers interested in the early history of the subject, and has an excellent introduction.

#### 3.4.1 Preference Semantics

Section 3.1 explained how preferred models can be used to characterize a nonmonotonic consequence relation. This approach to the model theory of nonmonotonicity was clarified in Shoham 1988, five years after the work discussed in Section 3.2. Shoham’s work provides a more general and abstract approach.

Preferential semantics relies on a function $S$ taking a set $K$ of models into a subset $S(K)$ of $K$. The crucial definition of *preferential entailment* stipulates that $A$ is a (nonmonotonic) consequence of $T$ if every model $M$ of $S$(*Models*$(T))$ implies $A$. Shoham characterizes $S(K)$ in terms of a partial order $\preccurlyeq$ over models: $S(K)$ is the set of models in $K$ that are $\preccurlyeq$-minimal in $K$. To ensure that no set can preferentially entail a contradiction unless it classically entails a contradiction, infinite descending $\preccurlyeq$ chains must be disallowed.

This treatment of nonmonotonicity is similar to the earlier modal semantic theories of conditionals—the similarities are particularly evident using presentations of conditional semantics such as Chellas 1975 that associate a set of worlds with the antecedent. Of course, the consequence relation of the classical conditional logics is monotonic, and conditional semantics uses possible worlds, not models. But the *left-nonmonotonicity* of conditionals (the fact that $A\,\Box{\rightarrow}\,C$ does not imply $[A\wedge B]\,\Box{\rightarrow}\,C)$ creates issues that parallel those that arise from a nonmonotonic consequence relation. Interrelations between conditionals and nonmonotonic logic became an important theme in later work in nonmonotonic logic. See, for instance, Gärdenfors & Makinson 1994, Boutilier 1992, Pearl 1994, Gabbay 1995, Delgrande 1998, Arlo-Costa & Shapiro 1992, Alcourrón 1995, Asher 1995, Kern-Isberner 2001, Giordano & Schwind 2004, Lent & Thomason 2015, and Casini & Straccia 2022.

Preference semantics raises an opportunity for formulating and proving representation theorems relating conditions over preference relations to properties of the abstract consequence relation. This line of investigation began with Lehmann & Magidor 1992.

#### 3.4.2 Modal and epistemic theories

Neither Doyle nor McDermott pursued the modal approach much beyond the initial stages. With a helpful suggestion from Robert Stalnaker (see Stalnaker 1993)[^stalnaker-1993], however, Robert C. Moore produced a modal theory that improves in many ways on the earlier ideas. Moore gives the modal operator of his system an epistemic interpretation, based on the conception of a default rule as one that licenses a conclusion for a reasoning agent unless something that the agent knows blocks the conclusion. In Moore’s *autoepistemic logic*, an extension $E$ of a theory $T$ is a superset of $T$ that is *stable*, i.e., that is deductively closed, and that satisfies the following two rules:

1. If $A\in E$ then $\Box A\in E$.
2. If $A\not\in E$ then $\neg \Box A\in E$.

It is also usual to impose a *groundedness* condition on autoepistemic extensions of $T$, ensuring that every member of an extension has some reason tracing back to $T$. Various such conditions have been considered; the simplest one restricts extensions to those satisfying

1. $E$ is the set of nonmodal consequences of $T\cup \{A : \Box A\in E\} \cup \{\neg \Box A : A\not\in E\}$.

Autoepistemic logic remains a popular approach to nonmonotonic logic, in part because of its usefulness in providing theoretical foundations for logic programming. See Marek & Truszczynski 1991, Marek & Truszczynski 1989, Konolige 1994, Antoniou 1997, Moore 1993, and Deneker *et al*. 2003.

Epistemic logic has inspired other approaches to nonmonotonic logic. Like other modal theories of nonmonotonicity, these use modality to reflect consistency in the object language, and so allow default rules along the lines of $\mathbf{DR}$ to be expressed. But instead of consistency, these use *ignorance*. See Halpern & Moses 1985 and Levesque 1987 for variations on this idea. These theories are explained and compared to other nonmonotonic logics in Meyer & van der Hoek 1995. In more recent work, Levesque’s ideas are systematically presented and applied to the theory of knowledge bases in Levesque & Lakemeyer 2000.

## 4. Reasoning about Action and Change

### 4.1 Priorian Tense Logic

The contours of modern temporal logic were standardized by Arthur Prior during the 1950s and 1960s: see Prior 1956, 1967, 1968.[^note-14] As it was developed in philosophical logic, tense logic proved to be a species of modal logic. Thus, it relativizes the truth-values of formulas to *world-states* or temporal stages of the world; these are the tense-theoretic analogues of the timeless possible worlds of ordinary modal logic. A research program can then be borrowed from modal logic—for instance, working out the relations between axiomatic systems and the corresponding model theoretic constraints on temporal orderings. See, for instance, Burgess 1984 and van Benthem 1983.

Priorian tense logic shares with modal logic an interest in using the first-order theory of relations to explain the logical phenomena, an expectation that the important temporal operators will be quantifiers over world-states, and a rather tenuous connection to realistic, practical specimens of temporal reasoning. Of course, these temporal logics do yield validities, such as

$$A\rightarrow\textit{PFA} $$

(if $A$, then it was the case that $A$ was going to be the case), which certainly are intuitively valid. But at most, these can only play a broadly foundational role in accounting for commonsense reasoning about time. It is hard to think of realistic examples of reasoning in which they play a leading part.

### 4.2 Planning Problems and the Situation Calculus

Planning problems provide one of the most fruitful showcases for combining logical analysis with AI applications. On the one hand automated planning enjoys many applications of real practical value, and on the other logical formalizations of planning are genuinely helpful in understanding planning problems, and in designing algorithms.

The classical representation of an AI planning problem, as described in Amarel 1968, evidently originates in early work of Herbert Simon’s, published in a 1966 CMU technical report, Simon 1966. In such a problem, an agent in an initial world-state is equipped with a set of *actions*, which are thought of as partial functions transforming world-states into world-states. Actions are feasible only in world-states that meet appropriate constraints. (These constraints are now called the “preconditions” of the action.) A planning problem then becomes a search for a series of feasible actions that successively transform the initial world-state into a desired world-state.

The *Situation Calculus*, developed by John McCarthy, is the origin of most of the later work in formalizing reasoning about action and change. It was first described in 1969, the earliest generally accessible publication on the topic is McCarthy & Hayes 1969.

Apparently, Priorian tense logic had no influence on Amarel. But there is no important difference between Amarel’s world-states and those of Priorian tense logic. The “situations” of the Situation Calculus are these same world-states, under a new name.[^note-15] They resemble possible worlds in modal logic in providing abstract locations that support a consistent and complete collection of truths. As in tense logic, these locations are ordered, and change is represented by variations in truth conditions from one location to another. The differences, of course, are inspired by the intended use of the Situation Calculus: it is meant to formalize Simon’s representation of the planning problem, in which a single agent reasons about scenarios in which sequential actions are performed.[^note-16] Change in the situation calculus is dynamic, driven by the performance of actions. Therefore the fundamental model theoretic component is

$$ \sc{Result}(\ra,\rs,\rs'), $$

the relation between an action a, an input situation s in which a is performed, and an output situation $\rs'$ immediately subsequent to the performance of the action. Usually (though this is not absolutely necessary) the deterministic assumption is made that $\rs'$ is unique.

All this, of course, presupposes a discrete picture of time. As in other action-driven frameworks, such ss game theory and the theory of digital computation, such a picture appears to be indispensible.

In general, actions can be successfully performed only under certain limited circumstances. This could be modeled by allowing for cases in which there is no $\rs'$ such that $\sc{Result}(\ra,\rs,\rs')$. Often, however, it is assumed that $\sc{Result}$ is in fact a total function, but that in cases in which s does not meet the “preconditions” of a, there are no restrictions on the $\rs'$ satisfying $\sc{Result}(\ra,\rs,\rs')$. This means that the causal effects of a will be entirely unconstrained in such cases, and in the presence of inertial laws “performing” a will leave things unchanged.

A planning problem starts with a limited repertoire of actions (where preconditions and effects are associated with each action), an initial situation, and a goal (which can be treated as a formula). A planning problem is a matter of finding a sequence of actions that will achieve the goal, given the initial situation. That is, given a goal $G$ and initial situation s, the problem will consist of finding a sequence $\ra_1, \ldots,\ra_n$ of actions which will transform s into a final situation $\rs_n$ that satisfies $G$. The planning problem is in effect a search for such a sequence of actions. The success conditions for the search can be characterized in a formalism like the Situation Calculus, which allows information about the results of actions to be expressed.

Nothing has been said up till now about the actual language of the Situation Calculus. The crucial thing is how change is to be expressed. With tense logic in mind, it would be natural to invoke a modality like $[a]A$, with the truth condition

$$ \vDash_{\small{s}}[a]A \text{ iff } \vDash_{\small{\rs'}}A, \text{ where } \vDash \sc{Result}(\ra,\rs)=\rs'. $$

This formalization, in the style of dynamic logic, is in fact an attractive alternative to McCarthy’s.

But McCarthy & Hayes 1969 deploys a language that is much closer to first-order logic. (This formalization style is characteristic of McCarthy’s work; see McCarthy 1979.)[^mccarthy-1979] Actions are treated as individuals. And propositions whose truth values can change over time (propositional *fluents*) are also treated as individuals. Where $s$ denotes a situation and $f$ a fluent, $\Holds(f,\rs)$ says that $f$ is true in $\rs$.

### 4.3 Formalizing Microworlds

Since the pioneering work of the nineteenth and early twentieth century logicians, the process of formalizing mathematical domains has become routine. Although (as with set theory) there may be controversies about what axioms and logical infrastructure best serve to formalize an area of mathematics, the methods of formalization and the criteria for evaluating them are automatic and (mostly) unexamined. This methodological clarity has not been successfully extended to other domains; even the formalization of the empirical sciences presents difficult problems that have not yet been resolved.[^note-17]

The formalization of temporal reasoning, and in particular of reasoning about actions and plans, is the best-developed successful extension of modern formalization techniques to domains other than mathematical theories. This departure has required the creation of new methodologies. One methodological innovation will emerge in Section 4.5: the development of a library of scenarios for testing the adequacy of various formalisms, and the creation of specialized domains like the blocks-world domain (mentioned above, in Section 4.2) that serve a laboratories for testing ideas. For more on the blocks world, see Genesereth & Nilsson 1987; Davis 1991. McCarthy’s ideas about *elaboration tolerance* McCarthy 1999 provide one interesting attempt to provide a criterion for the adequacy of formalizations. Another idea that has emerged in the course of formalizing commonsense domains is the importance of an explicit ontology; see, for instance, Fikes 1996 and Lenat & Guha 1989. Another is the potential usefulness of explicit representations of context; see Guha, 1991. Another is the use of simulation techniques: see, for instance, Johnstone & Williamson 2007.

### 4.4 Prediction and the Frame Problem

To tell whether a plan achieves its goal, you need to see whether the goal holds in the plan’s final state. Doing this requires *predictive* reasoning, a type of reasoning that the tense-logical literature neglected. As in mechanics, prediction involves the inference of later states from earlier ones. But (in the case of simple planning problems at least) change is driven by actions rather than by differential equations. The investigation of this qualitative form of temporal reasoning, and of related sorts of reasoning (e.g., plan recognition, which seeks to infer goals from observed actions, and narrative explanation, which seeks to fill in implicit information in a temporal narrative) is one of the most impressive chapters in the brief history of commonsense logicism.

The essence of prediction is the problem of inferring what holds in the situation that ensues from performing an action, given information about the initial situation. The problem is much easier if the agent has complete knowledge about the initial situation—this assumption is often unrealistic, but was usual in the classical planning formalisms.[^note-18]

A large part of action-driven dynamics has to do with what does *not* change. Take a simple plan to type ‘cat’ using a word processor: the natural plan is to first enter ‘c’, then enter ‘a’, then enter ‘t’. Part of one’s confidence in this plan is that the actions are independent: for instance, entering ‘a’ does not also erase the ‘c’. The required inference can be thought of as a form of *inertia*. The *Frame Problem* is the problem of how to formalize the required inertial reasoning.

The Frame Problem was named and introduced in McCarthy & Hayes 1969. Unlike most of the philosophically interesting technical problems to emerge in AI, it has attracted the interest of philosophers; most of the relevant papers, and background information, can be found in Ford & Pylyshyn 1996 and Pylyshyn 1987. Both of these volumes document interactions between AI and philosophy.

The quality of these interactions is discouraging. Like any realistic commonsense reasoning problem, the Frame Problem is open-ended, and can depend on a wide variety of circumstances. If you put $20 in a wallet, put the wallet in your pocket, and go to the store, you can safely assume that the $20 will remain in the wallet. But if you leave the $20 on the counter at the store while shopping, you can’t safely expect it to be there later. This may account for the temptation that makes some philosophers[^note-19] want to construe the Frame Problem very broadly, so that very soon it becomes indiscernible from the problem of formalizing general common sense in arbitrary domains.[^note-20] Such a broad construal may serve to introduce speculative discussions concerning the nature of AI, but it loses all contact with the genuine, new logical problems in temporal reasoning that have been discovered by the AI community.

The purely logical Frame Problem can be solved using monotonic logic, by simply writing explicit axioms stating what does *not* change when an action is performed. This technique can be successfully applied to quite complex formalization problems.[^note-21] But *nonmonotonic* solutions to the framework have been extensively investigated and deployed; these lead to new and interesting lines of logical development.

Some philosophers (Fodor 1987, Lormand 1996)[^fodor-1987][^lormand-1996] have felt that contrived propositions will pose special difficulties in connection with the Frame Problem. As Shanahan points out Shanahan 1997 [p. 24]) Fodor’s “fridgeon” example is readily formalized in the Situation Calculus and poses no special problems. However, as Lormand suggests, Goodman’s examples Goodman, 1946 do create problems if they are admitted as fluents; there will be anomalous extensions in which objects change from green to blue in order to preserve their grueness.

This is one of the few points made by philosophers about the Frame Problem that raises a genuine difficulty for AI formalization. But the difficulty is peripheral, because the example is unrealistic. Closure properties (such as closure under boolean operations) are not assumed for fluents. In fact, it is generally supposed that the fluents chosen in formalizing a planning domain will represent a very limited subset of the totality of state-dependent functions; typically, it will be a relatively small finite set of variables, representing features of the domain considered to be important. In particular cases these will be chosen in much the same way that a set of variables is chosen in statistical modeling.

I don’t know of any systematic account in the AI literature of formalization methodology, or, in particular, of how to choose an appropriate set of fluents. But it would certainly be part of such an account that all fluents should correspond to projectable predicates, in Goodman’s sense.

### 4.5 Nonmonotonic Treatments of Inertia and a Package of Problems

Nonmonotonic solutions to the Frame Problem make inertia a default; changes are assumed to occur only if there is some special reason for them to occur. In action-centered accounts of change, these special reasons are found in axioms specifying the immediate effects of actions.

We can illustrate the formalization with Reiter’s default logic. Recall that in Reiter’s theory, defaults are represented as rules, not as axioms; this means that we need to use default rule schemata to formalize inertia. For each fluent, action, and situation, the inertia schema will include the following rule:

$$\tag*{\textbf{Inertia:}} \leadsto \Holds(f,s) \leftrightarrow \Holds(f, \ttResult(a, s)) $$

This way of doing things makes any change in the truth value of a fluent a *prima facie* anomaly. But it follows from Reiter’s account of extensions that such defaults are overridden when they conflict with the (monotonic) axioms giving the state dynamics. If, for instance, there is a monotonic causal axiom for the action move-P4-to-Q4 ensuring that moving a certain pawn to Q4 will locate the pawn at Q4, the instance

$$\begin{aligned} &\Holds(\mathsf{At}(\mathsf{Q2}, \mathsf{Pawn4}), \mathsf{s_0}) \\ &\quad\leftrightarrow\ \Holds(\mathsf{At}(\mathsf{Q2}, \mathsf{Pawn4}),\ttResult(\mathsf{move\text{-}P4\text{-}to\text{-}Q4}, \mathsf{s_0})) \end{aligned}$$

of $\mathbf{IR}$ will be overridden, and there will be no extension in which the pawn remains where it was after performing the move-P4-to-Q4 action. **Inertia** will then ensure that the other pieces stay put.

The frame problem that captured wider attention was taken out of context and in isolation. If one is interested in understanding the philosophically interesting problems that arise in deploying formalisms like the Situation Calculus, it is best to consider a larger range of problems. These include not only the Frame Problem itself, but also the Qualification Problem, the Ramification Problem, and an assortment of specific challenges such as the scenarios mentioned later in this section. And one has to think about how to generalize: for instance, how to deal with incomplete information, multiple agents acting concurrently, and continuous change in the environment.

The *Qualification Problem* arises in connection with the formalization of just about any commonsense generalization. Typically, these will involve an open-ended and seemingly unmanageable array of exceptions. The same phenomenon, under the label ‘the problem of *ceteris paribus* generalizations’, is familiar from analytic philosophy. It also comes up in the semantics of *generic* constructions found in natural languages.[^note-22]

Nonmonotonic logics make a contribution to this problem by enabling incremental formalization. If a commonsense generalization is formulated as a default, then further qualifications can be added nondestructively. The default axiom is retained, and an exception—which itself may be a default—is added. This is helpful, even if it doesn’t address deeper problems of a philosophical nature.

The Qualification Problem was raised in McCarthy 1986, where it was motivated chiefly by generalizations concerning the consequences of actions; McCarthy considered in some detail the generalization that turning the ignition key in an automobile will start the car. Much the same point, in fact, can be made about virtually any action, including stacking one block on another—the standard example used in the early days of the Situation Calculus. A circumscriptive approach to the Qualification Problem is presented in Lifschitz 1987; this explicitly introduces the relation between an action and its preconditions into the formalism, and circumscriptively minimizes preconditions, eliminating from preferred models any “unknown preconditions” that might render an action inefficacious.

Not every nonmonotonic logic provides graceful mechanisms for qualification. Plain default logic, for instance, does not deliver the intuitively desired conclusions because it provides no way for defaults to override other defaults. To achieve this effect, one needs a fancy version of the logic in which defaults are prioritized. This can complicate the theory considerably; see, for instance, Asher & Morreau 1991 and Horty 1994. And, as Elkan 1995 points out, the Qualification Problem raises computational issues.

Relatively little attention has been given to the Qualification Problem for characterizing actions, in comparison with other problems in temporal reasoning. In particular, the standard accounts of *unsuccessful* actions are somewhat unintuitive. In the formalization of Lifschitz 1987, for instance, actions with unsatisfied preconditions are only distinguished from actions whose preconditions all succeed in that the conventional effects of the action will only be ensured when the preconditions are met. It is as if an action of spending $1,000,000 can be performed at any moment—although if you don’t have the money, no effects in particular will be guaranteed.[^note-23] And there is no distinction between actions that cannot even be attempted (like boarding a plane in London when you are in Sydney), actions that can be attempted, but in which the attempt can be expected to go wrong (like making a withdrawal when you have insufficient funds), actions that can be attempted with reasonable hope of success, and actions that can be attempted with guaranteed success. As J.L. Austin made clear in Austin 1961, the ways in which actions can be attempted, and in which attempted actions can fail, are a well developed part of commonsense reasoning. Obviously, in contemplating a plan containing actions that may fail, one may need to reason about the consequences of failure. Formalizing the pathology of actions, providing a systematic theory of ways in which actions and the plans that contain them can go wrong, would be a useful addition to planning formalisms, and one that would illuminate important themes in philosophy.

The challenge posed by the *Ramification Problem* (characterized first in Finger 1987)[^finger-1987] is to formalize the indirect consequences of actions, where “indirect” effects are synchronous[^note-24] but causally derivative. If one walks into a room, the direct effect is that one is now in the room. There are also many indirect effects: for instance, that one’s shirt also is now in the room.

You can see from this formulation that a distinction is presupposed between direct consequences of actions (ones that attach intrinsically to an action and are ensured by its successful performance) and other consequences. This assumption is generally accepted without question in the AI literature on action formalisms. You can make a good case for its commonsense plausibility—for instance, many of our words for actions (‘to warm’, ‘to lengthen’, ‘to fill’) are derived from the effects that are conventionally associated with them. And in these cases, success is entailed: if someone has warmed something, this entails that it became warm. But there are complications. Lin 1995 discusses a simple example: a certain suitcase has two locks, and is open if and only if both locks are open. Then (assuming that actions are not performed concurrently) opening one lock will open the suitcase if and only if the other lock is open. Lin’s formalization treats opening each lock as an action, with direct consequences. But opening the suitcase is not an action, it is an indirect effect.

Obviously, the Ramification Problem is intimately connected with the Frame Problem. In approaches that adopt nonmonotonic solutions to the Frame Problem, inertial defaults will need to be overridden by ramifications in order to obtain correct results. In Lin’s example, suppose that the left lock of the suitcase is open and the action of opening the right lock is performed. Then the default conclusion that the suitcase remains closed needs somehow to be suppressed.

Some approaches to the Ramification Problem depend on the development of theories of commonsense causation and therefore are closely related to the causal approaches to reasoning about time and action mentioned in Section 4.6. See, for instance, Giunchiglia *et al*. 1997, Thielscher 1989, Lin 1995.

Philosophical logicians have been content to illustrate their ideas with relatively small-scale examples. The formalization of even large-scale mathematical theories is relatively unproblematic. Logicist AI is the first branch of logic to undertake the task of formalizing realistic and nontrivial commonsense reasoning. In doing so, the field has had to invent new methods. An important part of the methodology that has emerged in formalizing action and change is the prominence that is given to challenges, posed in the form of *scenarios*. These scenarios represent formalization problems which usually involve relatively simple, realistic examples designed to challenge the logical theories in specific ways. Typically, there will be clear commonsense intuitions about the inferences that should be drawn in these cases. The challenge is to design a logical formalism that will provide general, well-motivated solutions to these benchmark problems.

Among the many scenarios that have been discussed in the literature are the Baby Scenario, the Bus Ride Scenario, the Chess Board Scenario, the Ferryboat Connection Scenario, the Furniture Assembly Scenario, the Hiding Turkey Scenario, the Kitchen Sink Scenario, the Russian Turkey Scenario, the Stanford Murder Mystery, the Stockholm Delivery Scenario, the Stolen Car Scenario, the Stuffy Room Scenario, the Ticketed Car Scenario, the Walking Turkey Scenario, and the Yale Shooting Anomaly. Accounts of these can be found in Shanahan 1997 and Sandewall 1994; see especially Sandewall 1994[Chapters 2 and 7].

Many of these scenarios are designed to test advanced problems that will not be discussed here—for instance, challenges dealing with multiple agents, or with continuous changes. Here, we concentrate on one of the earliest, and probably the most subtle of these scenarios: the Yale Shooting Anomaly, first reported in Hanks & McDermott 1985 and published in Hanks & McDermott 1986 and Hanks & McDermott 1987.

The Yale Shooting Anomaly involves three actions: load, shoot, and wait. A propositional fluent Loaded tracks whether a certain pistol is loaded; another fluent, Alive, tracks whether a certain turkey, Fred, is alive. The load action has no preconditions; its only effect is Loaded. The shoot action has Loaded as its only precondition and Not-Alive as its only effect; the wait action has no preconditions and no effects.

Causal information regarding the axioms is formalized as follows.

| **Load:** | $\forall s(\Holds(\Loaded, \ttResult(\load, s))$ |
| --- | --- |
| **Shoot 1:** | $\forall s (\Holds(\Loaded, s)\ \rightarrow$ $\Holds(\lnot \Alive, \ttResult(\shoot, s)))$ |
| **Shoot 2:** | $\forall s (\Holds(\Loaded, s)\ \rightarrow$ $\Holds(\lnot \Loaded, \ttResult(\shoot, s)))$ |

There is no Wait Axiom.

We will formalize the inertial reasoning in this scenario using Reiter’s default logic. The set $D$ of defaults for this theory consists of all instances of the inertial schema $\mathbf{IR}$. In the initial situation, Fred is alive and the pistol is unloaded.

| **IC1:** | $\Holds(\Alive, s_0)$ |
| --- | --- |
| **IC2:** | $\lnot\Holds(\Loaded, s_0)$ |

The monotonic theory $W$ of the scenario consists of: (1) the action axioms **Load**, **Shoot 1** and **Shoot 2** and (2) the initial conditions $\mathbf{IC1}$ and $\mathbf{IC2}$.

Let $s_1=\ttResult(\load, s_0),$ $s_2=\ttResult(\mathsf{wait}, s_1)$, and $s_3=\ttResult(\shoot, s_2)$.

The Yale Shooting Anomaly involves the action sequence load; wait; shoot, passing from $\rs_0$ to $\rs_3$, as follows.

| $\rs_0$ | $\ttload$ $\rightarrow$ | $\rs_1$ | $\ttwait$ $\rightarrow$ | $\rs_2$ | $\ttshoot$ $\rightarrow$ | $\rs_3$ |
| --- | --- | --- | --- | --- | --- | --- |

It is an anomaly—a challenge to a naive theory of inertia—because default logic allows an extension according to which the pistol is unloaded and Fred is alive in the final situation $s_3$. The anomalous extension is pictured as follows.

| $\ttAlive$ $\lnot\ttLoaded$ $\rs_0$ | $\ttload$ $\rightarrow$ | $\ttAlive$ $\ttLoaded$ $\rs_1$ | $\ttwait$ $\rightarrow$ | $\ttAlive$ $\lnot\ttLoaded$ $\rs_2$ | $\ttshoot$ $\rightarrow$ | $\ttAlive$ $\lnot\ttLoaded$ $\rs_3$ |
| --- | --- | --- | --- | --- | --- | --- |

In narrative form, what happens in this extension is this. At first, Fred is alive and the pistol is unloaded. After loading, the pistol is loaded and Fred remains alive. After waiting, the pistol becomes unloaded and Fred remains alive. Shooting is then vacuous because the pistol is unloaded. So finally, after shooting, Fred remains alive and the pistol remains unloaded.

The best way to see that this is an extension is to work through the proof. Less formally, though, you can see that the expected extension in which Fred ends up dead violates just one default: the frame default for Alive is violated when Fred changes state in the last step. But the anomalous extension also violates only one default: the frame default for Loaded is violated when the pistol spontaneously becomes unloaded while waiting. If you just go by the number of defaults that are violated, both extensions are equally good.

A planning algorithm based on a straightforward default logic formalization of causal inertia will be unable to perform as expected. It will be unable to verify a perfectly reasonable commonsense plan to kill Fred and will fail similarly in all but the simplest planning scenarios. So the Yale Shooting Anomaly represents a major obstacle in developing an inertia-based theory of predictive reasoning. A plausible, well-motivated logical solution to the Frame Problem has run afoul of a simple, crisp example in which it clearly delivers the wrong results.

Naturally, the literature concerning the Yale Shooting Anomaly is extensive. Surveys of some of this work, with bibliographical references, can be found in Shanahan 1997 and Morgenstern 1996.

### 4.6 Some Emergent Frameworks

It is commonly agreed that good solutions need to perform satisfactorily over a large suite of scenarios and to be generalizable: in particular, they should be deployable even when continuous time, concurrent actions, and various kinds of ignorance are introduced. And it is agreed that they should support multiple reasoning tasks, including not only prediction and plan verification but explanation of historical information or a narrative in terms of actions performed and agent goals.

Here, we mention four approaches: (1) Features and fluents (Sandewall), (2) Motivated Action Theory (Morgenstern and Stein), (3) State Minimization in the Event Calculus (Shanahan) and (4) Causal Theories (Lifschitz and others). The fourth approach is most likely to be interesting to philosophers and to contain elements that will be of lasting importance regardless of future developments in this area, and is discussed in more detail.

#### 4.6.1 Features and fluents

This approach, described in Sandewall 1994, uses preference semantics as a way to organize nonmonotonic solutions to the problems of reasoning about action and change. Rather than introducing a single logical framework, Sandewall considers a number of temporal logics, including ones that use discrete, continuous, and branching time. The properties of the logics are systematically tested against a large suite of test scenarios.

#### 4.6.2 Motivated Action Theory

This theory grew out of direct consideration of the problems in temporal reasoning described above in Section 4.5, and especially the Yale Shooting scenario. Morgenstern & Stein 1994 seeks to find a general, intuitively motivated logical framework that solves the difficulties. Morgenstern and Stein settle on the idea that unmotivated actions are to be minimized, where an action can be motivated directly, e.g. by an axiom, or indirectly, through causal chains. The key technical idea is a (rather complicated) definition of motivation in an interval-based temporal logic.

Morgenstern 1996 presents a summary of the theory, along with reasons for rejecting its causal rivals. The most important of these is that accounts based on the Situation Calculus do not appear to generalize to cases allowing for concurrency and ignorance. She also cites the failure of early causal theories to deal with retrodiction.

#### 4.6.3 State-Based Minimization in the Event Calculus

Baker 1989 works with circumscriptive versions of the Yale Shooting Anomaly. Recall that circumscription uses preferred models in which the extensions of abnormality predicates are minimized. In the course of this minimization, certain parameters (including, of course, the predicates to be minimized) are allowed to vary; the rest are held constant. Which parameters vary and which are held constant is determined by the application.

In the earliest circumscriptive solutions to the Frame Problem, the inertial rule $\textbf{CIR}$ is stated using an abnormality predicate.

$$\tag*{\textbf{CIR}:} \forall f, s, a [\lnot \texttt{Ab}(f, a, s)\rightarrow [\Holds(f, s)\leftrightarrow \Holds(f, \ttResult(a, s))]] $$

This axiom uses a biconditional, so that it can be used for retrodiction; this is typical of the more recent formulations of commonsense inertia. An unsophisticated solution to the frame problem minimizes the abnormality predicate while allowing the Holds predicate to vary and keeping all other parameters fixed. This succumbs to the Yale Shooting Anomaly in much the same way that default logic does. Circumscription does not involve multiple extensions, so the anomaly appears as inability to conclude that Fred is dead after the shooting.

In Baker’s reformulation of the problem, separate axioms ensure the existence of a situation corresponding to each Boolean combination of fluents, and the Result function is allowed to vary, while the Holds predicate is held constant. In this setting, the Result function needs to be specified for “counterfactual”actions—in particular, for shooting and for waiting in the Yale Shooting Anomaly. It is this feature that eliminates the incorrect model for that scenario; for details, see Baker 1989 and Shanahan 1997, Chapter 6.

This idea, which Shanahan calls “State-Based Minimization,” is developed and extended in Shanahan 1997, in the context of a temporal logic deriving from the Event Calculus of Kowalski & Sergot 1986. Shanahan’s version has the advantage of being closely connected to logic programming.

#### 4.6.4 Causal Theories

Recall that in the anomalous model of the Yale Shooting scenario the gun becomes unloaded after the performance of the wait action, an action which has no conventional effects. The unloading, then, is uncaused. This suggests a solution that minimizes outcomes that have no cause.

This strategy was pursued in Geffner 1990 and 1992. A similar approach beginning with Lifschitz 1987 develops a sustained line of research along these lines, carried out not only by Lifschitz and his students and colleagues in the Texas Action Group but by some others. For this work and further references, see Thielscher 1989, Gustaffson & Doherty 1996, Baral 1995, Nakashima *et al*. 1997, Lifschitz 1997, Giunchiglia & Lifschitz 1998, Lin 1995, Haugh 1987, Lifschitz 1998b, Turner 1999, McCain & Turner 1995, Elkan 1991, McCain & Turner 1997, Thielscher 1996, and Gelfond & Lifschitz 1998.

Here, we describe the causal solution presented in Turner 1999. Turner returns to the ideas of Geffner 1992, but places them in a simpler logical setting and applies them to the formalization of more complex scenarios that illustrate the interactions of causal inertia with other considerations, especially the Ramification Problem.

Ramification is induced by the presence of *static* laws which relate the direct consequences of actions to other changes. A car-starting scenario illustrates the difficulties. There is one action, *turn-on*, which turns on the ignition; let’s suppose that this action has no preconditions. There is a fluent $Ig$ tracking whether the ignition is on, a fluent *Dead* tracking whether the battery is dead, and a fluent *Run* tracking whether the engine is running. A static law says that if the ignition is on and the battery isn’t dead, the engine is running. (Let’s suppose that every other source of failure has already been eliminated in this scenario; the only possible reason for not starting is the battery.) We want to consider a transition in which *turn-on* is performed when the ignition isn’t on, the battery is not dead, and the car isn’t running.

Of course, we want to infer in such a case that a performance of *turn-on* will result in a situation in which the ignition is on, the battery isn’t dead, and the engine is running. But contraposed causal laws frustrate this conclusion. The difficulty is this: we can conclude by contraposing our only static law that if the ignition is on and the engine isn’t running, then the battery is dead. This law not only is true in our scenario, but would be used to explain a failed attempt to start the car. But if it is used for prediction, then performing *turn-on* will produce a “Murphy’s law” outcome in which the ignition is on, the battery is dead, and the engine isn’t running. Everything has a cause in this unwanted outcome: The battery is dead because of causal inertia and the engine isn’t running because of the contraposed causal law.

Readers who want to explore in some detail the problems of embedding a nonmonotonic solution to the Frame Problem in relatively expressive action languages can look to Gelfond & Lifschitz 1998. This paper presents an increasingly powerful and sophisticated series of action languages incorporating a somewhat *ad hoc* solution to the Ramification Problem. Turner 1999 is an improvement along these lines.

Turner’s idea is to treat $\texttt{Caused}$ as a modal operator $[c]$, which is provided with a nonmonotonic preferred models interpretation. Universal causality prevails in a preferred model: the caused propositions and the true propositions must coincide. Moreover, this model must be unique; it must be the only possibility consistent with the extensional part of the language.

To understand this idea, it’s helpful to recall that in the possible worlds interpretation of $\mathbf{S5}$, worlds can be identified with *state descriptions*, i.e. with complete, consistent sets $I$ of literals (atomic formulas and their negations). This allows us to think of a model as a pair $\langle I, S\rangle$, where $S$ is a set of interpretations including $I$. The modal operator $[c]$ is given the standard semantics. Where $S$ is a set of interpretations and where $I\in S, S\vDash_I[c]A$ if and only if $S\vDash_{I'}A$ for all $I'\in S. \langle I, S\rangle$ *satisfies* a set of formulas $T$ if and only if $S\vDash_I A$ for all $A\in T$.

Turner’s preferred models of $T$ are the pairs $\langle I, S\rangle$ such that: (1) $\langle I, S\rangle$ satisfies $T$, (2) $S = \{I\}$, and (3) $\langle I, S\rangle$ is the unique interpretation $\langle$*I$'$*, *S$'$*$\rangle$ meeting conditions (1) and (2). Condition (2) guarantees the “universality of causation;” it validates $A \leftrightarrow [c]A$. Condition (3) “grounds” causality in noncausal information (in the models in which we are interested, this will be a matter of which fluents hold in which situations), in the strongest sense: it is uniquely determined by this information.

Although it is not evident, Turner’s account of preferred models turns out to be related to more general nonmonotonic logics, such as default logic. Consult Turner 1999 for details.

The axioms that specify the effects of actions treat these effects as caused; for instance, the axiom schema for loading would read as follows:

> | **Causal-Load:** | $[c]\Holds(\Loaded, \ttResult(\load, s))$[^note-25] |
> | --- | --- |

Ramifications of the immediate effects of actions are also treated as caused. And there are two nonmonotonic inertial axiom schemata:

$$\begin{aligned} ([c] \Holds(f, s)\land {}&\Holds(f, \ttResult(a, s))) \\ &\rightarrow [c]\Holds(f, \ttResult(a, s)) \end{aligned}$$

and

$$\begin{aligned} ([c] \lnot\Holds(f, s)\land {}&\lnot\Holds(f, \ttResult(a, s))) \\ &\rightarrow [c]\lnot\Holds(f, \ttResult(a, s)) \end{aligned}$$

Thus, a true proposition can be caused either because it is the direct or indirect effect of an action, or because it involves the persistence of a caused proposition. Initial conditions are also considered to be caused, by stipulation.

To illustrate the workings of this approach, consider the simplest case: a language with just one fluent-denoting constant, f, and one action-denoting constant, wait. As in the Yale shooting problem, there are no axioms for wait; the action can always be performed and has no associated effects. Let s$_1$ be the result of performing the wait action in s$_0)$.

The theory $T$ contains an initial condition

$$\Holds( \mathsf{f}, \mathsf{s}_0)$$

and a statement that the initial condition is caused,

$$[c]\Holds( \mathsf{f}, \mathsf{s}_0),$$

Two models of $T$ satisfy conditions (1) and (2):

$$ M_1 = \langle I_1,\{I_1\}\rangle \text{ and } M_2 = \langle I_2,\{I_2\}\rangle, $$

where

$$I_1=\{\Holds( \mathsf{f}, \mathsf{s}_0), \Holds( \mathsf{f}, \mathsf{s}_1)\} \text{ and }I_2=\{\Holds( \mathsf{f}, \mathsf{s}_0), \lnot\Holds( \mathsf{f}, \mathsf{s}_1)\}. $$

$M_1$ is the intended model, in which nothing changes. It satisfies Condition (3), since if $\langle I_1, S\rangle$ satisfies $T$ then it satisfies $[c]\Holds(\mathrm{f}, \mathrm{s}_1)$ by the inertial axiom

$$([c]\Holds(\mathsf{f}, \mathsf{s}_0)\land \Holds(\mathsf{f}, \mathsf{s}_1))\rightarrow [c]\Holds(\mathsf{f}, \mathsf{s}_1)$$

Therefore, $S = \{I_1\}$.

$M_2$ is an anomalous model, in which the fluent ceases spontaneously. This model does not satisfy Condition (3), since $M_3 = \langle I_2,\{I_1, I_2\}\rangle$ also satisfies $T$; in particular, it satisfies the inertial axiom for f because it fails to satisfy $\Holds(\mathsf{f}, \mathsf{s}_1)$. So, while $M_1$ is a preferred model, $M_2$ is not.

Turner’s approach avoids the problem of contraposition by giving causal relations the form

$$[\sc{Background-Conditions} \land \sc{Cause}]\rightarrow [c]\sc{Effect}$$

When contraposed, this becomes

$$[\sc{Cause}\land \lnot [c] \sc{Effect}]\rightarrow \lnot \sc{Background-Conditions}$$

which does not have the form of a causal law.

The apparent usefulness of a “principle of universal causality” in accounting for a range of problems in qualitative commonsense reasoning should be of interest to philosophers. And the causal theory, as initiated by Geffner and developed by Turner, has many interesting detailed features. For instance, while philosophical work on causality has concentrated on the causal relation, Taylor’s approach shows that much can be done with only a nonrelational causal predicate.

Action-driven dynamics can be used to construct models for conditional logics. Lent and Thomason 2015 uses Turner’s causal approach to provide such models in the restricted case where the antecedent is the conjunction of an action expression and simple nonmodal conditions. An explicit solution to the frame problem provides counterfactual predictions and automatically provides a conditional semantics.

Morgenstern 1996 offers two chief criticisms of the causal approach to reasoning about actions: that it does not give an adequate account of explanation[^note-26] and that the Situation Calculus itself is limited in scope. Neither criticism is fatal; both can be taken as challenges for future research.

For another approach to nonmonotonic causal reasoning, based on input-output logics (Makinson & van der Torre 2000), see Bochman 2004.

## 5. Causal Reasoning

Of course, causal reasoning is an important topic in its own right. For instance, it figures in qualitative reasoning about devices. Herbert Simon’s work in this area goes back to the 1950s: see Simon 1952; 1977; Iwasaki & Simon 1986. Judea Pearl and his students and associates are responsible for the most sustained and successful investigation of causal models and causal reasoning. Pearl and many of his co-authors are computer scientists, but statisticians and philosophers have also contributed to this research program. We will not discuss causal networks further here. See Halpern 2016 and Hitchcock 2022.

## 6. Spatial Reasoning

The precomputational literature in philosophical logic relating to spatial reasoning is relatively sparse. But the need to support computational reasoning about space in application areas such as motion planning and manipulation in physical space, the indexing and retrieval of images, geographic information systems, diagrammatic reasoning, and the design of high-level graphics programs has led to new interest in spatial representations and spatial reasoning. Of course, the geometrical tradition provides an exceptionally strong mathematical resource for this enterprise. But as in many other AI-related areas, it is not clear these theories are appropriate for informing these applications, and many computer scientists have felt it worthwhile to develop new foundations. Some of this work is closely related to the research in qualitative reasoning mentioned above in Section 2.2, and in some cases has been carried out by the same individuals. And of course, there also are connections to the mereology literature in philosophical logic.

The AI literature in spatial reasoning is extensive; for references to some areas not discussed here, see Stock 1997, Kapur & Mundy 1988, Hammer 1995, Wilson 1998, Osherson & Lasnik 1990, Renz & Nebel 1999, Yeap & Jeffries 1999, Chen 1990, Burger & Bhanu 1992, Allwein & Barwise 1996, Glasgow *et al*. 1995, and Kosslyn 1990. Here, we discuss only one trend, which is closely connected with parallel work in philosophical logic.

Qualitative approaches to space were introduced into the logical literature early in the twentieth century by Stanisław Leśniewski; see Leśniewski 1916, which presents the idea of a *mereology*, or qualitative theory of the part-whole relation between physical individuals. This idea of a logical theory of relations among regions remained active in philosophical logic, even though it attracted relatively few researchers. More recent work in the philosophical literature, especially Casati & Varzi 1999, Simons 1987, Casati & Varzi 1996, Clarke 1981, and Clarke 1985, has influenced the current computational work.

The Regional Connection Calculus (RCC), developed by computer scientists at the University of Leeds, is based on a primitive $C$ relating regions of space: the intended interpretation of $C(x, y)$ is that the intersection of the closures of the values of $x$ and $y$ is nonempty. See Cohn *et al*. 1997, Cohn 1996) for details and references. The extent of what can be defined with this simple primitive is surprising, but the technicalities quickly become complex; see, for instance, Gotts 1994, Gotts 1996). The work cited in Cohn *et al*. 1997 describes constraint propagation techniques and encodings in intuitionistic propositional logic as ways of supporting implemented reasoning based on RCC and some of its extensions. More recent work based on RCC addresses representation and reasoning about motion, which of course combines spatial and temporal issues; see Wolter & Zakharyaschev 2000). For more information about qualitative theories of movement, with references to other approaches, see Galton 1997.

## 7. Reasoning about Knowledge

Hintikka 1962, the classical source for epistemic logic, takes its cue from modal logic. Thus, the work concentrates on how to model the attitudes of a single agent with modal operators. Because possible-worlds semantics accommodates alternative modal operators, Hintikka discusses at length the question of exactly which alternatives are appropriate for knowledge and belief, opting for the modal logic $\mathbf{S4}$. For more background and information about later developments, see Rendsvig & Symons 2022. And Laux & Wansing 1995 discusses both the philosophical and computational traditions up to 1994.

Epistemic attitudes figure in game theory, as well as logical AI, and work in both of these application areas either parallels or was influenced by Hintikka’s modal approach. In several papers (including McCarthy 1979)[^mccarthy-1979], John McCarthy recommended an approach to formalizing knowledge that uses first-order logic, but that quantifies explicitly over such things as individual concepts. Here, however, we discuss the approach taken by most computer scientists, who—unlike McCarthy—use modal logic, but—unlike Hintikka—concentrate on the multiagent case.

Fagin *et al*. 1995 simplifies the underlying modality, using $\mathbf{S5}$ for knowledge (or deontic $\mathbf{S5}$ for belief), but concentrates on agents’ attitudes about one another’s attitudes. Such logics have direct applications in the analysis of *distributed systems*, dynamic systems in which change is effected by message actions, which modify the knowledge of agents according to rules determined by a *communications protocol*. Multi-Agent epistemic logic is another example of how the need of applications provided the inspiration for significant contributions to logic. Fagin *et al*. 1995; is essential reading for anyone seriously interested in this topic. Other applied work in epistemic logic is reported in the proceedings of a series of conferences initiated in 1986 with Halpern 1986. These conferences record one of the most successful collaborations of philosophers with logicians in Computer Science, although the group of involved philosophers has been relatively small. The focus of the conferences has gradually shifted from Computer Science to Economics.

Computer scientists are used to thinking of reasoning as the manipulation of symbolic representations. And it is mainly due to AI that limited rationality has become a topic of serious interest, providing a counterbalance to the idealizations of philosophy and economics.[^note-27] You would think, then, that closure of epistemic attitudes under logical consequence would be highly unpopular in AI. But this is not so; the possible worlds approach to attitudes is not only the leading theory in the areas discussed in Fagin *et al*. 1995, but has even been advocated in robotics applications; see Rosenschein & Kaelbling 1995; Rosenschein 1989. Nevertheless, the issue of hyperintensionality has been investigated in the AI literature; see Perlis 1985; Konolige 1986; Lakemeyer 1997; Levesque 1984). Though the work on this topic in AI provides new theories and some new results, no leading approach has yet emerged.

## 8. Towards a Formalization of Common Sense

John McCarthy’s explicit long-term goal—the formalization of commonsense knowledge—was adopted and pursued by a relatively small subcommunity of AI researchers. The work of a much larger group (those involved in knowledge representation, cognitive robotics, and qualitative physics) contributes to specialized projects that support the larger goal. Anything remotely like a formalization of common sense is so far from being accomplished that—if it is achievable at all—guessing when we could expect the task to be completed is hopeless. But at least the effort has yielded a better sense of how to develop a workable methodology for formalizing commonsense examples and domains, and of how to divide the larger problem up into more manageable parts.

The first book-length treatment of this topic, Davis 1991, divides the general problem into the following subtopics.

1. Quantities and Measurements
2. Time
3. Space
4. Physics
5. Minds
6. Plans and Goals
7. Society

The first four of these topics overlaps with qualitative physics. For more information on this related subfield, consult Weld & de Kleer 1990, Davis 2008, and Forbus 2008.

Item 6 is the most extensively studied of Davis’s seven. Section 4 discussed the early phases of this work. There is a robust subsequent history of research on planning and goal formation, with the later work blending into work on planning architectures for autonomous agents. Items 5 and 7 are underresearched. Although artificial societies and architectures for artificial minds have been intensively studied, there has been relatively little work on the formalization of commonsense psychology and commonsense interpersonal reasoning. However, see Davis 1991 and Hobbs & Gordon 2005.

For a book-length treatment of the commonsense challenge, see Mueller, 2006. More than half of the book is devoted to reasoning about actions and change. There are short chapters on space and mental states, and a longer treatment of nonmonotonic reasoning.

Research in computer science is almost entirely driven by the availability of funding. The formalization of commonsense reasoning was never heavily funded, but until John McCarthy’s death in 2011 small amounts of funding were available. There were regular meetings of the commonsense interest group in 1998, 2001, 2003, 2005, 2007, and 2009. Many of the papers presented at the 2003 conference were collected in expanded form in 2004, in Volume 153 of *Artificial Intelligence*. Davis & Morgenstern 2004, the introduction to this collection, provides a useful survey and appreciation of research in the formalization of common sense and the mechanization of commonsense reasoning. The [Common Sense Problem Page](http://www-formal.stanford.edu/leora/commonsense/) is still maintained, but activity in this field has been slow from 2010 until the present, except for related knowledge representation research.

Borrowing the idea from other areas of computer science, the commonsense community has sought to develop suites of “benchmark problems”: to publicize problems that are difficult but not impossibly difficult and to encourage the creation of solutions and their comparison. Probably the best-documented problem to date is Ernest Davis’ “egg-cracking problem.” This is formulated as follows in [the Common Sense Problem Page](http://www-formal.stanford.edu/leora/commonsense/).

> A cook is cracking a raw egg against a glass bowl. Properly performed, the impact of the egg against the edge of the bowl will crack the eggshell in half. Holding the egg over the bowl, the cook will separate the two halves of the shell with his fingers, enlarging the crack, and the contents of the egg will fall gently into the bowl. The end result is that the entire contents of the egg will be in the bowl, with the egg unbroken, and that the two halves of the shell are in the cook’s fingers.

> *Variants:* What happens if: The cook brings the egg to impact very quickly? Very slowly? The cook lays the egg in the bowl and exerts steady pressure with his hand? The cook, having cracked the egg, attempts to peel it off its contents like a hard-boiled egg? The bowl is made of looseleaf paper? Of soft clay? The bowl is smaller than the egg? The bowl is upside down? The cook tries this procedure with a hard-boiled egg? With a coconut? With an M&M?

Along with the problem itself three solutions are posted: Shanahan 2004, Lifschitz 1998a, and a version of Morgenstern 2001. Comparing the solutions is instructive—similarities outweigh differences. All the authors think of this as a planning problem, and use versions of the Situation Calculus or the Event Calculus in the formalization. Each axiomatization is modular, with, for instance, separate modules devoted to the relevant geometrical and material properties. Each author provides a “proof of concept” for the formalization by showing that the axioms support a proof of the correctness of a plan to crack the egg in the simple case. None of the authors considers all of Davis’ elaborations of the problem, but the axioms are framed with elaboration in mind and some elaborations are considered. It isn’t clear whether any of the authors actually implemented their formalization (for instance, using a theorem prover, an animation, or a robot controller).

The egg-cracking example raises the problem of how to evaluate moderately large formalizations of commonsense problems. Morgenstern and Shanahan express this issue explicitly. Morgenstern suggests that the important criteria are (1) Epistemological adequacy (correspondence to intuitive reasoning, as experienced by people who engage in it), (2) Faithfulness to the real world, (3) Reusability, and (4) Elaboration tolerance. The first two of these criteria may be too subjective to be very useful. To these, Shanahan adds (5) Usability. More important, however, in the long run, would be the automatization of testing and evaluation, by generating scenarios and testing them with real-world or simulated robotic agents.

Any even moderately successful attempt to formalize common sense will soon encounter unprecedented problems of scale, creating challenges similar to those that software engineering tries to address. Even fairly small programs and systems of axioms are difficult to comprehend and can produce unexpected results. Creating and maintaining them may require teams of developers, precipitating organizational issues, as well as issues having to do with the integration of modules, the maintenance and testing of large systems, and the generation of axioms from disparate knowledge sources. Although the need for large-scale software systems has provided best practices for enterprises of this kind it might well turn out that, even with ample funding, human expertise would be inadequate for this task.

Two ways to automate the creation of formalizations can be imagined. (1) The large-scale ontologies created by the knowledge representation community could be mined for axioms, or (2) axioms could be created directly from corpora using machine learning techniques. The first method would entail unprecedented difficulties having to do with knowledge integration. Techniques for rendering the products of machine learning explainable[^note-28] provide some hope for the second method, but the outputs of these techniques are not at all like logical axioms and the task of converting them appears to be challenging, to say the least.

All this contrasts sharply with the methodology of philosophical analysis. Analyses are far smaller in scale, are not formalized with implementations in mind, and little or no attention is paid to their integration. Philosophers have never chosen a specific domain comparable to the planning domain and mounted a sustained attempt to formalize it, along with a companion effort to develop appropriate logics.

It is easy to suspect that many of the topics that have preoccupied analytic philosophy exhibit the sort of complexity that emerged, for instance, from the attempts of AI researchers to formalize reasoning about actions and their effects. If AI researchers were able to develop and partially automate a formalization methodology for problems like those listed in [the Common Sense Problem Page](http://www-formal.stanford.edu/leora/commonsense/), this would certainly be a tremendous advance over what analytic philosophers have been able to achieve. But perhaps philosophers can congratulate themselves that this has proved to be such a difficult challenge.

## 9. Taxonomic Representation and Reasoning

### 9.1 Concept-Based Classification

Traditionally, the task of representing large amounts of domain information for general-purpose reasoning has been one of the most important areas of knowledge representation. Systems that exploit the intuitive taxonomic organization of domains are useful for this purpose; taxonomic hierarchies not only help to organize the process of knowledge acquisition, but provide a useful connection to rule-based reasoning.[^note-29]

For domains in which complex definitions are a natural way to organize information, knowledge engineering services based on definitions of concepts have been extremely successful. Like variable-free versions of first-order logic (see, for instance, Quine 1960)[^quine-1960], these systems are centered on concepts or first-order predicates, and provide a number of mechanisms for their definition. The fundamental algorithm associated with these *taxonomic logics* is a classifier which inputs a system of definitions and outputs the entailment relations between defined and primitive concepts. For background on these systems, see Woods & Schmolze 1992 and Brachman *et al*. 1991.

The simplest taxonomic logics can be regarded as subsystems of first-order logic with complex predicates. But they have been extended in many ways, and the issues raised by many of these extensions overlap in many cases with topics in philosophical logic.

### 9.2 Nonmonotonic Inheritance

Much more complex logical issues arise when the organization of a domain into hierarchies is allowed to have exceptions. One way to approach this topic is to explore how to make a taxonomic logic nonmonotonic; but *nonmonotonic inheritance* is a topic in its own right. Although there are strong affinities to nonmonotonic logic, nonmonotonic inheritance relies more heavily on graph-based representations than on traditional logical ideas, and seems to provide a much finer-grained approach to nonmonotonic reasoning that raises entirely new issues, and which quickly becomes problematic. For this reason, systems of nonmonotonic inheritance tend to be expressively weak, and their relations to the more powerful nonmonotonic logic has never been fully clarified. For background on this topic, see Thomason 1992 and Horty 1994.

## 10. Contextual Reasoning

In the tradition in philosophical logic dealing with contextual effects on the interpretation of expressions, as well as in the more recent tradition in dynamic logic, context is primarily formalized as an assignment of values to variables, and the language is designed to make explicit reasoning about context either very limited or outright impossible.

Concern in AI about the representation of large and apparently heterogeneous domains and about the integration of disparate knowledge sources, as well as interests in formalizing common sense of the sort discussed in Section 2.2, above, have led to interest in the AI community in formalizing languages that take context into account more explicitly.

In McCarthy 1993b, McCarthy recommends the study of languages containing a construct

$$\textit{ist}(c, \phi),$$

where $\textit{ist}$ is read “is-true.” This is analogous to the $\Holds$ construct of the situation calculus—but now $c$ stands for a context, and $\phi$ is a possibly complex propositional representation, which many (including McCarthy) take to refer to a sentence.

There are analogies here both to modal logic and to languages with an explicit truth predicate. But the applications that are envisioned for a logic of context create opportunities and problems that are in many ways new. Work on the logic of context subsequent to McCarthy’s original suggestion, includes McCarthy & Buvac 1998, Guha 1991, and some of the papers in the conference volumes Akman *et al*. 2001 and Bouquet *et al*. 1999. For extensions of Richard Montague’s Intensional Logic motivated by McCarthy’s suggestions, see Thomason 2003 and 2005.

For some reason, work on the explicit formalization of context hasn’t been pursued intensively by the computational community beyond this point, but for an application to information integration, see Snidaro 2019.

Philosophical interest in context, and especially in the interaction of context with propositional attitudes and modals, continues to be strong; but the very general logical frameworks for context that McCarthy envisioned have yet not been taken up by philosophers.

## 11. Prospects for a Logical Theory of Practical Reason

There is reason to hope that the combination of logical methods with planning applications in AI can enable the development of a far more comprehensive and adequate theory of practical reasoning than has heretofore been possible. As with many problems having to do with common sense reasoning, the scale and complexity of the formalizations that are required are beyond the traditional techniques of philosophical logic. However, with computational methods of implementing and testing the formalizations and with areas such as cognitive robotics providing laboratories for developing and testing ideas, we can hope to radically advance a problem that has seen little progress since it was first proposed by Aristotle: how to devise a formalization of practical reasoning that is genuinely applicable to realistic problems.

The classical work in deontic logic that was begun by von Wright (see von Wright 1983)[^wright-1983] is one source of ideas; see (Horty 2001 and van der Torre 1997)[^horty-2001][^torre-1997]. In fact, as the more recent work in deontic logic shows, nonmonotonic logic provides a natural and useful supplement to the classical deontic logic. One recent work (Horty 2012)[^horty-2012] seeks to base deontic logic on a prioritized version of Reiter’s default logic.

An even more robust account of practical reasoning begins to emerge when these ideas are supplemented with work on the foundations of planning and reasoning about action that were discussed in Section 4, above. But this development can be pursued even further, by extending the formalism to include preferences and intentions.[^note-30]

Ultimately, what is needed is a model of an intelligent reasoning and acting agent. Developing such a model need not be entirely a matter of logic, but according to one school of thought, logic has a central role to play in it; see, for instance, Baral & Gelfond 2000, Wobcke *et al*. 1998, Burkhard *et al*. 1998), Wooldridge 2000, Thielscher 2005, and Levesque & Lakemeyer 2008.

## 12. Readings

Minker 2000b is a comprehensive collection of survey papers and original contributions to the field of logic-based AI, with extensive references to the literature. Jack Minker’s introduction, Minker 2000a, is a useful orientation to the field. This volume is a good beginning point for readers who wish to pursue this topic further. Brachman & Levesque 2004 provides an introduction to the field of knowledge representation in textbook form. Davis 1991 and Mueller 2006 are book-length treatments of the challenging problem of formalizing commonsense reasoning. Straßer & Antonelli 2012 is a good entry point for readers interested in nonmonotonic logic, and Shanahan 2009 is a useful discussion of the frame problem. Wooldridge 2000 deals with logical formalizations of rational agents.

The proceedings of the Knowledge Representation and Reasoning conferences provide the best detailed record of logical research in AI from 1989 to the present: Brachman *et al*. 1989, Allen *et al*. 1991, Nebel *et al*. 1992, Doyle *et al*. 1994, Aiello *et al*. 1996, Cohn *et al*. 1998, Cohn *et al*. 2000, Fensel *et al*. 2002, Dubois *et al*. 2004, Doherty *et al*. 2006, Brewka & Lang 2008, Lin *et al*. 2010, Eiter *et al*. 2012, Baral *et al*. 2014, Baral *et al*. 2016, Thielscher *et al*. 2018, Calvanese *et al*. 2020, Bienvenu *et al*. 2021, and Kern-Isberner *et al*. 2022.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=logic-ai). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/logic-ai/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=logic-ai&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/logic-ai/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- Stanford Formal Reasoning Group, [Formal Reasoning Group Web Pages](http://www-formal.stanford.edu).
- John McCarthy, [John McCarthy’s Web Pages](http://www-formal.stanford.edu/jmc/).
- Stanford Computer Science, [John McCarthy’s Posthumous Stanford Pages](http://jmc.stanford.edu/).
- Leora Morgenstern, [Common Sense Problem Page](http://www-formal.stanford.edu/leora/commonsense/).
- Toronto Cognitive Robotics Group, [Toronto Cognitive Robotics Pages](http://www.cs.toronto.edu/cogrobo/main/).

## Related Entries

conditionals | frame problem | logic: non-monotonic | reasoning: automated

### Acknowledgments

I am grateful to John McCarthy, who read an early draft of this article and provided extensive and helpful comments.

## Notes（原文脚注）

## Notes to Logic-Based Artificial Intelligence

[^note-1]: For readers who would like an in-depth orientation to the field of AI, I recommend Russell & Norvig 2010.

[^note-2]: For some of the historical background, see Davis 1988.

[^note-3]: See Stefik 1995 for general background on expert systems. For information concerning explanation, see Moore 1995a; Clancey 1983.

[^note-4]: One might be surprised at first to hear the AI community refer to its logical advocates as logicists. On reflection, it seems reasonable to think of logicist projects this way, as proposals to apply what Alonzo Church called “the logistic method” to reasoning in various domains. One need not narrowly associate logicism with Frege, and with Russell and Whitehead, and their programs for formalizing mathematics.

[^note-5]: The submissions to the 1989 conference were unclassified as to topic; every other article was sampled, a total of 522. The 1998 conference divided its contributed articles into 26 topical sessions; the first paper in each of these sessions was sampled.

[^note-6]: Data integration is one such area. See Levy 2000. Large-scale knowledge representation is another. See Lenat & Guha 1989.

[^note-7]: See Reiter 2001 for an extended contribution to cognitive robotics, with references to some of the other literature in this area. Reiter’s book also contains self-contained chapters on the Situation Calculus and the problems of formalizing reasoning about action and change. These chapters may be useful to anyone wishing to follow up on the topics discussed in Section 4. Also see Levesque & Lakemeyer 2008.

[^note-8]: For a survey of research in multiagent systems, see Chopra 2018.

[^note-9]: Qualitative physics is an independent specialty in AI, different in many ways from logical AI. But the two specialties have certainly influenced each other.

[^note-10]: At the time, this very difficult and not particularly well-defined problem was very much on the minds of many AI researchers, but it has not proved to be a productive focus for logical AI. Natural language interpretation has developed into a separate field almost entirely concerned with specialized language technologies, such as automated speech-to-speech discourse, data mining, and text summarization.

[^note-11]: When Minsky speaks of a “frame”, he has in mind an information nexus in an object-oriented system of knowledge representation. His use of the word is unconnected to and not to be confused with the use of ‘frame’ in the *frame problem*.

[^note-12]: The analogy to modal logics of provability inspired by Gödel’s work, such as Boolos 1993, has, of course, been recognized in later work in nonmonotonic logic. But it has not been a theme of major importance.

[^note-13]: See Konolige 1988.

[^note-14]: Readers interested in the historical aspects of the material discussed in this section might wish to compare it to Ohrstrom & Hasle 1995. For additional historical background on Prior’s work, see Copeland 1996.

[^note-15]: In retrospect, the term ‘situation’ is not entirely fortunate, since it was later adopted independently and in quite a different sense by the situation semanticists. (See, for instance. Seligman & Moss 1996)[^seligman-1996]. In the AI literature, the term ‘state’ is often used interchangeably with ‘situation’—without, as far as I can see, causing any confusion. The connections with physical states, as well as with the more general states of any complex dynamic system are entirely appropriate.

[^note-16]: The early versions of the Situation Calculus were meant to be compatible with concurrent applications, with multiple planning agents, possibly acting simultaneously. But most of the logical analyses have been devoted to the single-agent case.

[^note-17]: Carnap’s attempts to formalize dispositional terms and inductive methods are classical examples of the problems that emerge in the formalization of empirical science.

[^note-18]: For information about planning under uncertainty, see, for instance, DeJong & Bennett 1989; Bacchus et al. 1999; Boutilier et al. 1996.

[^note-19]: Examples are Dennett 1987 and Fodor 1987.

[^note-20]: In the AI community, the term for a problem so difficult that solving it would involve overcoming just about every obstacle to achieving human-level intelligence is “AI-complete.” The Frame Problem is not AI-complete.

[^note-21]: See Schubert 1990, Reiter 1993, and Reiter 2001.

[^note-22]: See Carlson & Pelletier 1995.

[^note-23]: This way of putting it is a little misleading for the Situation Calculus, which has no robust notion of performance, considering only the outcomes associated with hypothetical action sequences. Nevertheless, the point remains that misexecutions were neglected in early work on planning. Later work pays more attention to the needs of embodied actors; see, for instance, Ghallab et al 2014.

[^note-24]: Effects of actions that are delayed in time are a separate problem, which, as far as the present author knows, no one has solved.

[^note-25]: Turner uses discrete temporal logic rather than the Situation Calculus. But for uniformity of presentation, the Situation Calculus is used to present the ideas.

[^note-26]: In explanation problems, one is reasoning backwards in time. Here, information is provided about a series of occurring states and the problem is to provide actions that account for the occurrences.

[^note-27]: See, for instance, Simon 1982a, 1982b, and Russell & Wefald 1991.

[^note-28]: See, for instance, Guidotti 2021.

[^note-29]: This is related to the field of Knowledge Engineering. For background, see Stefik 1995.

[^note-30]: For background on quantitative models of preference and decision, see Doyle & Thomason 1999. For work in AI on intentions, see, for instance Konolige & Pollack 1993, Cohen & Levesque 1990, Sadek 1992, and Pollack 1992.

[^aiello-1996]: Aiello, Luigia Carlucci, Doyle, Jon, and Shapiro, Stuart (eds.), 1996, *KR’96: Principles of Knowledge Representation and Reasoning*, San Francisco: Morgan Kaufmann.

[^akman-2001]: Akman, Varol, Bouquet, Paolo, Thomason, Richmond, and Young, Roger A. (eds.), 2001, *Modeling and Using Context*, Berlin: Springer-Verlag.

[^alcourrón-1995]: Alcourrón, Carlos E., 1995, “Defeasible logics: Demarcation and affinities”, in *Conditionals: From Philosophy to Computer Science*, Gabriella Crocco, Luis Fariñas del Cerro, and A. Herzig (eds.), Oxford: Oxford University Press, 67–102.

[^allen-1989]: Allen, James F., Fikes, Richard, and Sandewall, Erik (eds.), 1989, *KR’89: Principles of Knowledge Representation and Reasoning*, San Francisco: Morgan Kaufmann.

[^allen-1991]: Allen, James F., Fikes, Richard, and Sandewall, Erik (eds.), 1991, *KR’91: Principles of Knowledge Representation and Reasoning*, San Mateo, California: Morgan Kaufmann.

[^allwein-1996]: Allwein, Gerard and Barwise, Jon (eds.), 1996, *Logical Reasoning with Diagrams*, Oxford: Oxford University Press.

[^amarel-1968]: Amarel, Saul, 1968, “On representations of problems of reasoning about actions”, in *Machine Intelligence 3*, Donald Mitchie (ed.), Chichester, England: Ellis Horwood, 131–171.

[^antoniou-1997]: Antoniou, Grigoris, 1997, *Nonmonotonic Reasoning*, Cambridge, Massachusetts: The MIT Press.

[^antoniou-2007]: Antoniou, Grigoris and Wang, Kewen, 2007, “Default logic”, in *Handbook of the History of Logic, Volume 8: The Many-Valued and Nonmonotonic Turn in Logic*, Dov Gabbay and John Woods (eds.), Amsterdam: Elsevier Science Publishers, 517–555.

[^arlo-costa-1992]: Arlo-Costa, Horacio and Shapiro, Scott, 1992, “Maps between nonmonotonic logic and conditional logic”, in *KR’92. Principles of Knowledge Representation and Reasoning: Proceedings of the Third International Conference*, Bernhard Nebel, Charles Rich, and William Swartout (eds.), San Mateo, California: Morgan Kaufmann, 553–564.

[^asher-1995]: Asher, Nicholas, 1995, “Commonsense entailment: A conditional logic for some generics”, in *Conditionals: From Philosophy to Computer Science*, Gabriella Crocco, Luis Fariñas del Cerro, and A. Herzig (eds.), Oxford: Oxford University Press, 103–145.

[^asher-1991]: Asher, Nicholas and Morreau, Michael, 1991, “Commonsense entailment: a modal theory of nonmonotonic reasoning”, in *Proceedings of the Twelfth International Joint Conference on Artificial Intelligence*, J. Mylopoulos and R. Reiter (eds.), Los Altos, California: Morgan Kaufmann, 387–392.

[^austin-1961]: Austin, John L., 1961, “A plea for excuses”, in *Philosophical Papers*, J.O. Urmson and G.J. Warnock (eds.), Oxford: Oxford University Press.

[^bacchus-1999]: Bacchus, Fahiem, Halpern, Joseph Y., and Levesque, Hector J., 1999, “Reasoning about noisy sensors and effectors in the situation calculus”, *Artificial Intelligence*, 111(1–2): 171–208.

[^baker-1989]: Baker, Andrew B., 1989, “A simple solution to the Yale shooting problem”, in *KR’89: Principles of Knowledge Representation and Reasoning*, Ronald J. Brachman, Hector J. Levesque, and Raymond Reiter (eds.), San Mateo, California: Morgan Kaufmann, 11–20.

[^baral-1995]: Baral, Chitta, 1995, “Reasoning about actions: Non-deterministic effects, constraints, and qualification”, in *Proceedings of the Fourteenth International Joint Conference on Artificial Intelligence*, Chris Mellish (ed.), San Francisco: Morgan Kaufmann, 2017–2023.

[^baral-2014]: Baral, Chita, De Giacomo, Giuseppe, and Eiter, Thomas (eds.), 2014, *KR2014: Principles of Knowledge Representation and Reasoning*, Menlo Park, California: AAAI Press.

[^baral-2016]: Baral, Chita, Delgrande, James, and Wolter, Frank (eds.), 2016, *KR2016: Principles of Knowledge Representation and Reasoning*, Menlo Park, California: AAAI Press.

[^baral-2000]: Baral, Chitta and Gelfond, Michael, 2000, “Reasoning agents in dynamic domains”, in *Logic-Based Artificial Intelligence*, Jack Minker (ed.), Dordrecht: Kluwer Academic Publishers, 257–279.

[^besnard-1992]: Besnard, Philippe, 1992, *Default Logic*, Berlin: Springer-Verlag.

[^besnard-2008]: Besnard, Philippe and Hunter, Anthony, 2008, *Elements of Argumentation*, Cambridge, Massachusetts: The MIT Press.

[^bienvenu-2021]: Bienvenu, Meghyn, Lakemeyer, Gerhard, and Erdem, Esra (eds.), 2021, *KR2021: Principles of Knowledge Representation and Reasoning*, Menlo Park, California: AAAI Press.

[^bochman-2004]: Bochman, Alexander, 2004, “A causal approach to nonmonotonic reasoning”, *Artificial Intelligence*, 160(1–2): 105–143.

[^bochman-2007]: Bochman, Alexander, 2007, “Nonmonotonic reasoning”, in *Handbook of the History of Logic. Volume 8: The Many Valued and Nonmonotonic Turn in Logic*, Dov M. Gabbay and John Woods (eds.), Amsterdam: Elsevier Publishing Co., 557–622.

[^boolos-1993]: Boolos, George, 1993, *The Logic of Provability*, Cambridge, England: Cambridge Universoti Press.

[^bouquet-1999]: Bouquet, Paolo, Serafini, Luigi, Brézillon, Patrick, Benerecetti, Massimo, and Castellani, Francesca (eds.), 1999, *Modeling and Using Contexts: Proceedings of the Second International and Interdisciplinary Conference, CONTEXT’99*, Berlin: Springer-Verlag.

[^boutilier-1992]: Boutilier, Craig, 1992, “Conditional logics for default reasoning and belief revision”, Tech. Rep. KRR-TR-92-1, Computer Science Department, University of Toronto, Toronto, Ontario.

[^boutilier-1996]: Boutilier, Craig, 1996, “Iterated revision and minimal change of conditional beliefs”, *Journal of Philosophical Logic*, 25(3): 263–305.

[^boutilier-1996-2]: Boutilier, Craig, Dean, Thomas, and Hanks, Steve, 1996, “Planning under uncertainty: Structural assumptions and computational leverage”, in *New Directions in AI Planning*, Malik Ghallab and Alfredo Milani (eds.), Amsterdam: IOS Press, 157–171.

[^brachman-1989]: Brachman, Ronald J., Levesque, Hector J., and Reiter,, Raymond, 1989, *KR’89: Principles of Knowledge Representation and Reasoning*, San Mateo, Morgan Kaufmann.

[^brachman-1991]: Brachman, Ronald J., McGuinness, Deborah L., Patel-Schneider, Peter F., and Resnik, Lori A., 1991, “Living with CLASSIC: When and how to use a KL-ONE-like language”, in *Principles of Semantic Networks*, John F. Sowa (ed.), San Mateo, California: Morgan Kaufmann, 401–456.

[^brachman-2004]: Brachman, Ronald J. and Levesque, Hector J., 2004, *Knowledge Representation and Reasoning*, Amsterdam: Elsevier.

[^brewka-1991]: Brewka, Gerhard, 1991, *Nonmonotonic Reasoning: Logical Foundations of Commonsense*, Cambridge, England: Cambridge University Press.

[^brewka-1997]: Brewka, Gerhard, Dix, Jürgen, and Konolige, Kurt, 1997, *Nonmonotonic Reasoning: An Overview*, Stanford: CSLI Publications.

[^brewka-2008]: Brewka, Gerhard and Lang, Jérôme (eds.), 2008, *KR2008: Proceedings of the Eleventh National Conference*, Menlo Park, California: AAAI Press.

[^burger-1992]: Burger, Wilhelm and Bhanu, Bir, 1992, *Qualitative Motion Planning*, Dordrecht: Kluwer Academic Publishers.

[^burkhard-1998]: Burkhard, Hans-Dieter, Hannebauer, Markus, and Wendler, Jan, 1998, “Belief-desire-intention deliberation in artificial soccer”, *The AI Magazine*, 1998(3): 87–93.

[^burgess-1984]: Burgess, John P., 1984, “Basic tense logic”, in *Handbook of Philosophical Logic, Volume II: Extensions of Classical Logic*, Dov Gabbay and Franz Guenther (eds.), Dordrecht: D. Reidel Publishing Co., 89–133.

[^calvanese-2020]: Calvanese, Diego, Erdem, Esra, and Thielscher, Michael (eds.), 2020, *KR2020: Principles of Knowledge Representation and Reasoning*, Menlo Park, California: AAAI Press.

[^carlson-1995]: Carlson, Greg N. and Pelletier, Francis Jeffry (eds.), 1995, *The Generic Book*, Chicago, IL: Chicago University Press.

[^carnap-1955]: Carnap, Rudolph, 1955, “Meaning and synonymy in natural languages”, *Philosophical Studies*, 7: 33–47. Reprinted in Carnap 1956, pp. 233–247.

[^carnap-1956]: Carnap, Rudolph, 1956, *Meaning and Necessity*, Chicago: Chicago University Press, second edition (First edition published in 1947.).

[^casati-1996]: Casati, Roberto and Varzi, Achille C., 1996, *Holes and Other Superficialities*, Cambridge, Massachusetts: The MIT Press.

[^casati-1999]: Casati, Roberto and Varzi, Achille C., 1999, *Parts and Places: The Structures of Spatial Representation*, Cambridge, Massachusetts: The MIT Press.

[^casini-2022]: Casini, Giovanni and Straccia, Umberto, 2022, “A general framework for modelling conditional reasoning—Preliminary Report”, in *KR2022: Principles of Knowledge Representation and Reasoning, Proceedings of the Nineteenth International Conference*, Gabriele Kern-Isberner and Gerhard Lakemeyer and Thomas Meyer (eds.), Menlo Park, California, 575–595.

[^chellas-1975]: Chellas, Brian, 1975, “Basic conditional logic”, *Journal of Philosophical Logic*, 4(2): 133–154.

[^chen-1990]: Chen, Su-Shing (ed.), 1990, *Advances in Spatial Reasoning, Volume 1*, Norwood, New Jersey: Ablex.

[^chopra-1997]: Chopra, Amit, van der Torre, Leon, Verhagen, Harko, and Villata, Serena 1997, *Handbook of Normative Multiagent Systems*, London: College Publications.

[^clancey-1983]: Clancey, William J., 1983, “The epistemology of a rule-based expert system: a framework for explanation”, *Artificial Intelligence*, 20: 215–251.

[^clark-1978]: Clark, Keith L., 1978, “Negation as failure”, in *Logic and Data Bases*, H. Gallaire and Jack Minker (eds.), New York: Plenum Press, 293–322.

[^clarke-1981]: Clarke, Bowman L., 1981, “A calculus of individuals based on ‘connection’”, *Notre Dame Journal of Formal Logic*, 22(3): 204–218.

[^clarke-1985]: Clarke, Bowman L., 1985, “Individuals and points”, *Notre Dame Journal of Formal Logic*, 26(1): 61–75.

[^cohen-1990]: Cohen, Philip R. and Levesque, Hector J., 1990, “Intention is choice with commitment”, *Artificial Intelligence*, 42(3): 213–261.

[^cohn-1996]: Cohn, Anthony G., 1996, “Qualitative spatial representation and reasoning techniques”, in *KI-97, Advances in Artificial Intelligence*, Gerhard Brewka, Christopher Habel, and Bernhard Nebel (eds.), Berlin: Springer-Verlag, 1-30.

[^cohn-1997]: Cohn, Anthony G., Bennett, Brandon, Gooday, John, and Gotts, Nicholas M., 1997, “Representing and reasoning with qualitative spatial relations”, in *Spatial and Temporal Reasoning*, Oliviero Stock (ed.), Dordrecht: Kluwer Academic Publishers, 97–134.

[^cohn-1998]: Cohn, Anthony G., Schubert, Lenhart, and Shapiro, Stuart C. (eds.), 1998, *KR’98: Principles of Knowledge Representation and Reasoning*, San Francisco: Morgan Kaufmann.

[^cohn-2000]: Cohn, Anthony G., Giunchiglia, Fausto, and Selman, Bart (eds.), 2000, *KR2000: Principles of Knowledge Representation and Reasoning*, San Francisco: Morgan Kaufmann.

[^copeland-1996]: Copeland, B. Jack, 1996, “Arthur Prior’s life and legacy”, in *Logic and Reality: Essays on the Legacy of Arthur Prior*, Jack Copeland (ed.), Oxford: Oxford University Press, 1–40.

[^davis-1991]: Davis, Ernest, 1991, *Common Sense Reasoning*, San Francisco: Morgan Kaufmann.

[^davis-2004]: Davis, Ernest and Morgenstern, Leora, 2004, “Introduction: Progress in formal commonsense reasoning”, *Artificial Intelligence*, 153(1–2): 1–12.

[^davis-1988]: Davis, Martin, 1988, “Mathematical Logic and the Origin of Modern Computers”, in *The Universal Turing Machine: A Half-Century Survey*, Jack Copeland (ed.), Oxford: Oxford University Press, 149–174.

[^davis-2008]: Davis, Ernest, 2008, “Physical reasoning”, in *Handbook of Knowledge Representation*, van Harmelen, Frank, Lifschitz, Vladimir and Porter, Bruce (eds.), : Elsevier, 597–620.

[^dejong-1989]: DeJong, Gerald D. and Bennett, Scott W., 1989, “Permissive planning: Extending classical planning to uncertain task domains”, *Artificial Intelligence*, 89(1–2): 173–217.

[^delgrande-1998]: Delgrande, James P., 1998, “Conditional logics for defeasible logics”, in *Handbook of Defeasible Reasoning and Uncertainty Management Systems, Volume 2*, Dov M. Gabbay and Philippe Smets (eds.), Dordrecht: Kluwer Academic Publishers, 135–174.

[^deneker-1998]: Deneker, Marc, Marek, Victor W., and Truszczyński, Miroslaw 1998, “Uniform semantic treatment of default and autoepistemic logics”, *Artificial Intelligence*, 143(1): 79–122.

[^dennett-1987]: Dennett, Daniel, 1987, “Cognitive wheels: The frame problem of AI”, in *The Robot’s Dilemma: The Frame Problem in Artificial Intelligence*, Zenon Pylyshyn (ed.), Norwood, New Jersey: Ablex Publishing Co., 41–64.

[^doherty-2006]: Doherty, Patrick, Fikes, Richard, and Sandewall, Erik (eds.), 2006, *KR’2006: Proceedings, Tenth International Conference on Principles of Knowledge Representation and Reasoning*, Palo Alto: AAAI Press.

[^doyle-1995]: Doyle, Jon, 1995, “A truth maintenance system”, *Artificial Intelligence*, 12(1): 231–272.

[^doyle-1994]: Doyle, Jon, Sandewall, Erik, and Torasso, Pietro (eds.), 1994, *KR’94: Principles of Knowledge Representation and Reasoning*, San Francisco: Morgan Kaufmann.

[^doyle-1999]: Doyle, Jon and Thomason, Richmond H., 1999, “Background to qualitative decision theory”, *AI Magazine*, 20(2): 55–68.

[^dubois-2004]: Dubois, Didier, Welty, Christopher, and Williams, Mary-Anne (eds.), 2004,*KR2004: Principles of Knowledge Representation and Reasoning*, Palo Alto: AAAI Press.

[^eiter-1992]: Eiter, Tomas, McIlraith, Sheila A., and Brewka, Gerald (eds.), 1992, *KR2012: Proceedings of the Thirteenth International Conference*, Menlo Park, California: AAAI Press.

[^elkan-1991]: Elkan, Charles, 1991, “Reasoning about action in first-order logic”, in *Proceedings of the Conference of the Canadian Society for Computational Studies of Intelligence (CSCSI)*, Canadian Society for Computational Studies of Intelligence, San Francisco: Morgan Kaufman, 221–227.

[^elkan-1995]: Elkan, Charles, 1995, “On solving the qualification problem”, in *Working Notes of the AAAI Spring Symposium on Extending Theories of Action: Formal Theories and Applications*, Menlo Park, California: American Association for Artificial Intelligence.

[^fagin-1995]: Fagin, Ronald, Halpern, Joseph Y., Moses, Yoram, and Vardi, Moshe Y., 1995, *Reasoning about Knowledge*, Cambridge, Massachusetts: The MIT Press.

[^fensel-2002]: Fensel, Dieter, Giunchiglia, Fausto, McGuinness, Deborah, and Williams, Mary-Anne (eds.), 2002, *KR2002: Principles of Knowledge Representation and Reasoning*, San Francisco, California: Morgan Kaufmann.

[^fikes-1996]: Fikes, Richard, 1996, “Ontologies: What are they, and where’s the research?”, in *KR’96: Principles of Knowledge Representation and Reasoning*, Luigia Carlucci Aiello, Jon Doyle, and Stuart Shapiro (eds.), San Francisco, California: Morgan Kaufmann, 652–654.

[^finger-1987]: Finger, Jeffrey J., 1987, *Exploiting Constraints in Design Synthesis*, Ph.D. dissertation, Department of Computer Science, Stanford University, Stanford, California.

[^fodor-1987]: Fodor, Jerry A., 1987, “Modules, frames, fridgeons, sleeping dogs, and the music of the spheres”, in *The Robot’s Dilemma: The Frame Problem in Artificial Intelligence*, Zenon Pylyshyn (ed.), Norwood, New Jersey: Ablex Publishing Co., 139–149.

[^forbus-2008]: Forbus, Kenneth 2008, “Qualitative Modeling”, in *Handbook of Knowledge Representation*, van Harmelen, Frank, Lifschitz, Vladimir and Porter, Bruce (eds.), : Elsevier, 361–393.

[^ford-1996]: Ford, Kenneth M. and Pylyshyn, Zenon (eds.), 1996, *The Robot’s Dilemma Revisited: The Frame Problem in Artificial Intelligence*, Norwood, New Jersey: Ablex Publishing Co.

[^gabbay-1994]: Gabbay, Dov, Hogger, Christopher J., and Robinson, J. A. (eds.), 1994, *Handbook of Logic in Artificial Intelligence and Logic Programming, Volume 3: Nonmonotonic Reasoning and Uncertain Reasoning*, Oxford: Oxford University Press.

[^gabbay-1995]: Gabbay, Dov M., 1995, “Conditional implications and non-monotonic consequence”, in *Conditionals: From Philosophy to Computer Science*, Gabriella Crocco, Luis Fariñas del Cerro, and A. Herzig (eds.), Oxford: Oxford University Press, 337–359.

[^galton-1997]: Galton, Anthony, 1997, “Space, time, and movement”, in *Spatial and Temporal Reasoning*, Oliviero Stock (ed.), Dordrecht: Kluwer Academic Publishers, 321–352.

[^gärdenfors-1994]: Gärdenfors, Peter and Makinson, David, 1994, “Nonmonotonic inferences based on expectations”, *Artificial Intelligence*, 65(2): 197–245.

[^geffner-1990]: Geffner, Hector, 1990, “Causal theories of nonmonotonic reasoning”, in *Proceedings of the Eighth National Conference on Artificial Intelligence*, Thomas Dietterich and William Swartout (eds.), American Association for Artificial Intelligence, Menlo Park, CA: AAAI Press, 524–530.

[^geffner-1992]: Geffner, Hector, 1992, *Default Reasoning: Causal and Conditional Theories*, Cambridge, Massachusetts: MIT Press.

[^gelfond-1998]: Gelfond, Michael and Lifschitz, Vladimir, 1998, [“Action languages”](https://www.diva-portal.org/smash/get/diva2:1716299/FULLTEXT02.pdf), *Electronic Transactions on AI*, 3.

[^genesereth-1987]: Genesereth, Michael and Nilsson, Nils J., 1987, *Logical Foundations of Artificial Intelligence*, San Mateo, California: Morgan Kaufmann.

[^ghallab-2014]: Ghallab, Malik, Nau, Dana, and Traverso, Paolo, 2014, “The actor’s view of automated planning and acting: A position paper”, *Artificial Intelligence*, 208: 1–17.

[^ginsberg-1987]: Ginsberg, Matthew L. (ed.), 1987, *Readings in Nonmonotonic Reasoning*, Los Altos, California: Morgan Kaufmann. (Out of print.).

[^giordano-2004]: Giordano, Laura and Schwind, Camilla, 2004, “Conditional logic of actions and causation”, *Artificial Intelligence*, 157(1–2): 239–279.

[^giunchiglia-1997]: Giunchiglia, Enrico, Kartha, G. Neelakantan, and Lifschitz, Vladimir, 1997, “Representing action: Indeterminacy and ramifications”, *Artificial Intelligence*, 95(2): 409–438.

[^giunchiglia-1998]: Giunchiglia, Enrico and Lifschitz, Vladimir, 1998, “An action language based on causal explanation”, in *Proceedings of the Fourteenth National Conference on Artificial Intelligence and the Ninth Innovative Applications of Artificial Intelligence Conference*, Ted Senator and Bruce Buchanan (eds.), American Association for Artificial Intelligence, Menlo Park, California: AAAI Press, 623–628.

[^glasgow-1995]: Glasgow, Janice, Narayanan, N. Hari, and Chandrasekaran, B. (eds.), 1995, *Diagrammatic Reasoning*, Cambridge, Massachusetts: The MIT Press.

[^goodman-1946]: Goodman, Nelson, 1946, *Fact, Fiction and Forecast*, Cambridge, Massachusetts: Harvard University Press, fourth edition.

[^gotts-1994]: Gotts, N.M., 1994, “How far can we ‘C’? defining a doughnut using connection alone”, in *KR’94: Principles of Knowledge Representation and Reasoning*, Jon Doyle, Erik Sandewall, and Pietro Torasso (eds.), San Francisco, California: Morgan Kaufmann, 246–257.

[^gotts-1996]: Gotts, N.M., 1996, “Topology from a single primitive relation: Defining topological properties and relations in terms of connection”, Tech. Rep. 96.24, School of Computer Studies, University of Leeds, Leeds.

[^guha-1991]: Guha, Ramanathan V., 1991, “Contexts: a formalization and some applications”, Tech. Rep. STAN-CS-91-1399, Stanford Computer Science Department, Stanford, California.

[^guidotti-2018]: Guidotti, Riccardo, Monreale, Anna, Ruggieri, Salvatore, Turini, Franco, Giannotti, Fosca, and Pedreschi, Dino, 2018, “A survey of methods for explaining black box models”, *ACM Computing Surveys*, 51(5): 1–42.

[^gustaffson-1996]: Gustaffson, Joakim and Doherty, Patrick, 1996, “Embracing occlusion in specifying the indirect effects of actions”, in *KR’96: Principles of Knowledge Representation and Reasoning*, Luigia Carlucci Aiello, Jon Doyle, and Stuart Shapiro (eds.), San Francisco, California: Morgan Kaufmann, 87–98.

[^halpern-1986]: Halpern, Joseph Y. (ed.), 1986, *Theoretical Aspects of Reasoning about Knowledge: Proceedings of the First Conference (TARK 1986)*, Los Altos, California: Morgan Kaufmann Publishers, Inc.

[^halpern-2016]: Halpern, Joseph L., 2016, *Actual Causality*, Cambridge, Massachusetts: The MIT Press.

[^halpern-1985]: Halpern, Joseph Y. and Moses, Yoram, 1985, “Towards a theory of knowledge and ignorance”, in *Logics and Models of Concurrent Systems*, Krzysztof R. Apt (ed.), Berlin: Springer-Verlag, 459–476.

[^halpern-2001]: Halpern, Joseph, and Pearl, Judea, 2001, “Causes and explanations: a Structural-model approach”, in *Uncertainty in Artificial Intelligence. Proceedings of the Seventeenth Conference*, San Francisco: Morgan Kaufmann, 194–202.

[^hammer-1995]: Hammer, Eric M., 1995, *Logic and Visual Information*, Stanford, California: CSLI Publications.

[^hanks-1985]: Hanks, Steven and McDermott, Drew, 1985, “Temporal reasoning and default logics”, Tech. Rep. YALEU/CSD/RR#430, Department of Computer Science, Yale University, New Haven, Connecticut.

[^hanks-1986]: Hanks, Steven and McDermott, Drew, 1986, “Default reasoning, nonmonotonic logics and the frame problem”, in *Proceedings of the Fifth National Conference on Artificial Intelligence*, Tom Kehler and Stan Rosenschein (eds.), American Association for Artificial Intelligence, Los Altos, California: Morgan Kaufmann, 328–333.

[^hanks-1987]: Hanks, Steven and McDermott, Drew, 1987, “Non-monotonic logics and temporal projection”, *Artificial Intelligence*, 33(3): 379–412.

[^haugeland-1981]: Haugeland, John, 1981, “Semantic engines: An introduction to mind design”, in *Mind Design*, John Haugeland (ed.), Cambridge, Massachusetts: The MIT Press, 1–34.

[^haugh-1987]: Haugh, Brian, 1987, “Simple causal minimization for temporal persistence and projection”, in *Proceedings of the Seventh National Conference on Artificial Intelligence*, Kenneth Forbus and Howard Shrobe (eds.), American Association for Artificial Intelligence, Menlo Park, California: AAAI Press, 218–223.

[^hintikka-1962]: Hintikka, Jaakko, 1962, *Knowledge and Belief*, Ithaca, New York: Cornell University Press.

[^hitchcock-2022]: Hitchcock, Christopher, 2022, “Causal models”, in *The Stanford Encyclopedia of Philosophy*, Edward N. Zalta (ed.), URL $= \langle$https://plato.stanford.edu/archives/spr2022/entries/causal-models/$\rangle$.

[^hobbs-2005]: Hobbs, Jerry and Gordon, Andrew, 2005, “Encoding knowledge of commonsense psychology”, *7th International Symposium on Logical Formalizations of Commonsense Reasoning.* May 22–24, 2005, Corfu, Greece.

[^horty-1994]: Horty, John F., 1994, “Some direct theories of nonmonotonic inheritance”, in *Handbook of Logic in Artificial Intelligence and Logic Programming, Volume 3: Nonmonotonic Reasoning and Uncertain Reasoning*, Dov Gabbay, Christopher J. Hogger, and J. A. Robinson (eds.), Oxford University Press, 111–187.

[^horty-2001]: Horty, John F., 2001, *Agency and Deontic Logic*, Oxford: Oxford University Press.

[^horty-2012]: Horty, John, 2012, *Reasons as Defaults*, Oxford: Oxford University Press.

[^israel-1991]: Israel, David J., 1991, “A short sketch of the life and career of John McCarthy”, in *Artificial Intelligence and Mathematical Theory of Computation: Papers in Honor of John McCarthy*, Vladimir Lifschitz (ed.), San Diego, California: Academic Press.

[^iwasaki-1986]: Iwasaki, Yumi and Simon, Herbert, 1986, “Causality in device behavior”, *Artificial Intelligence*, 29(1): 3–32.

[^johnston-2007]: Johnston, Benjamin and Williams, Mary-Anne, “A generic framework for approximate simulation in commonsense reasoning systems”, AAAI 2007 Spring Symposium on Commonsense Reasoning, American Association for Artificial Intelligence, Menlo Park, 2007.

[^kapur-1988]: Kapur, Deepak and Mundy, Joseph L., 1988, “Geometric reasoning and artificial intelligence: Introduction to the special volume”, *Artificial Intelligence*, 37(1–3): 1–11.

[^kern-isberner-2001]: Kern-Isberner, Gabriele, 2001, *Conditionals in Nonmonotonic Reasoning and Belief Revision: Considering Conditionals as Agents*, Berlin: Springer-Verlag.

[^kern-isberner-2022]: Kern-Isberner, Gabriele, Lakemeyer, Gerhard, and Meyer, Thomas (eds.), 2022, *KR2022: Principles of Knowledge Representation and Reasoning*, Menlo Park, California: AAAI Press.

[^konolige-1986]: Konolige, Kurt, 1986, “What awareness isn’t: A sentential view of implicit and explicit belief”, in *Theoretical Aspects of Reasoning about Knowledge: Proceedings of the First Conference*, Joseph Y. Halpern (ed.), Los Altos, California: Morgan Kaufmann Publishers, Inc., 241–250.

[^konolige-1988]: Konolige, Kurt, 1988, “On the relation between default and autoepistemic logic”, *Artificial Intelligence*, 35(3): 343–382. (See also errata, Artificial Intelligence $\mathbf{41}$(1): 115.).

[^konolige-1994]: Konolige, Kurt, 1994, “Autoepistemic logic”, in *Handbook of Logic in Artificial Intelligence and Logic Programming, Volume 3: Nonmonotonic Reasoning and Uncertain Reasoning*, Dov Gabbay, Christopher J. Hogger, and J. A. Robinson (eds.), Oxford: Oxford University Press, 217–295.

[^konolige-1993]: Konolige, Kurt and Pollack, Martha, 1993, “A representationalist theory of intention”, in *Proceedings of the Thirteenth International Joint Conference on Artificial Intelligence*, Ruzena Bajcsy (ed.), San Mateo, California: Morgan Kaufmann.

[^kosslyn-1990]: Kosslyn, Stephen Michael, 1990, “Visual cognition: Introduction”, in *An Invitation to Cognitive Science. Volume 2: Visual Cognition and Action*, Daniel N. Osherson and Howard Lasnik (eds.), Cambridge, Massachusetts: The MIT Press, 3–4.

[^kowalski-1986]: Kowalski, Robert A. and Sergot, Marek J., 1986, “A logic-based calculus of events”, *New Generation Computing*, 4: 67–95.

[^lakemeyer-1997]: Lakemeyer, Gerhard, 1997, “Limited reasoning in first-order knowledge bases”, *Artificial Intelligence*, 71(2): 213–255.

[^laux-1995]: Laux, Armin and Wansing, Heinrich (eds.), 1995, *Knowledge and Belief in Philosophy and Artificial Intelligence*, Berlin: Akedemie Verlag.

[^lehmann-1992]: Lehmann, Daniel and Magidor, Menachem, 1992, “What does a conditional knowledge base entail?”, *Artificial Intelligence*, 55(1): 1–60.

[^lenat-1989]: Lenat, Douglas B. and Guha, R.V., 1989, *Building Large Knowledge-Based Systems: Representation and Inference in the CYC Project.*, Reading, Massachusetts: Addison-Wesley Publishing Company.

[^lent-2015]: Lent, Jeremy and Thomason, Richmond, 2015, “Action models for conditionals”, *Journal of Logic, Language, and Information*, 24(2): 211–231.

[^leśniewski-1916]: Leśniewski, Stanisław, 1916, “Podstawy ogólnej teorii mnogosci I”, English Title: “Foundations of a general set theory I.”, Moscow: Popławski.

[^levesque-2000]: Levesque, Hector and Lakemeyer, Gerhard, 2000, *The Logic of Knowledge Bases*, Cambridge, Massachusetts: The MIT Press.

[^levesque-1984]: Levesque, Hector J., 1984, “A logic of implicit and explicit belief”, in *Proceedings of the Fourth National Conference on Artificial Intelligence*, American Association for Artificial Intelligence, 198–202.

[^levesque-1987]: Levesque, Hector J., 1987, “Taking issue: Guest editor’s introduction”, *Computational Intelligence*, 3(3): 149–150.

[^levesque-2008]: Levesque, Hector and Lakemeyer, Gerhard, 2008, “Cognitive robotics”, in *Handbook of Knowledge Representation*, Harmelen, Frank van, Lifschitz, Vladimir, and Porter, Bruce (eds.), Amsterdam: Elsevier, 969–886.

[^levy-2000]: Levy, Alon Y., 2000, “Logic-based techniques in data integration”, in *Logic-Based Artificial Intelligence*, Jack Minker (ed.), Dordrecht: Kluwer Academic Publishers, 575–595.

[^lin-2010]: Lin, Fangshen, Sattler, Ulrike, and Truszczyński, Miroslaw (eds.), 2010, *KR2010: Principles of Knowledge Representation and Reasoning*, Menlo Park, California: AAAI Press.

[^lifschitz-1987]: Lifschitz, Vladimir, 1987, “Formal theories of action: Preliminary report”, in *Proceedings of the Tenth International Joint Conference on Artificial Intelligence*, John McDermott (ed.), Los Altos, California: Morgan Kaufmann.

[^lifschitz-1990a]: Lifschitz, Vladimir (ed.), 1990a, *Formalizing Common Sense: Papers by John McCarthy*, Norwood, New Jersey: Ablex Publishing Corporation.

[^lifschitz-1990b]: Lifschitz, Vladimir, 1990b, “Understanding common sense: McCarthy’s research in artificial intelligence”, in *Formalizing Common Sense: Papers by John McCarthy*, Vladimir Lifschitz (ed.), Norwood, New Jersey: Ablex Publishing Corporation, 1–8.

[^lifschitz-1997]: Lifschitz, Vladimir, 1997, “On the logic of causal explanation”, *Artificial Intelligence*, 96(2): 451–465.

[^lifschitz-1998a]: Lifschitz, Vladimir, 1998a, “Cracking an Egg: An Exercise in Commonsense Reasoning”, presented at the Fourth Symposium on Logical Formalizations of Commonsense Reasoning, London, January 1998. [Lifschitz 1998a available online in PostScript](https://www.cs.utexas.edu/~vl/papers/egg.ps).

[^lifschitz-1998b]: Lifschitz, Vladimir, 1998b, “Situation calculus and causal logic”, in *KR’98: Principles of Knowledge Representation and Reasoning*, Anthony G. Cohn, Lenhart Schubert, and Stuart C. Shapiro (eds.), San Francisco, California: Morgan Kaufmann, 536–546.

[^lin-1995]: Lin, Fangzhen, 1995, “Embracing causality in specifying the indirect effects of actions”, in *Proceedings of the Fourteenth International Joint Conference on Artificial Intelligence*, Chris Mellish (ed.), San Francisco: Morgan Kaufmann, 1985–1991.

[^lin-2010-2]: Lin, Fangzhen, Sattler, Ulrike, and Truszczynski, Miroslaw (eds.), 2010, *KR2010: Proceedings of the Twelfth International Conference*, Palo Alto: AAAI Press.

[^lormand-1996]: Lormand, Eric, 1996, “The holorobophobe’s dilemma”, in *The Robot’s Dilemma Revisited: The Frame Problem in Artificial Intelligence*, Kenneth M. Ford and Zenon Pylyshyn (eds.), Norwood, New Jersey: Ablex Publishing Co., 61–88.

[^witold-1990]: Łukaszewicz, Witold, 1990, *Non-Monotonic Reasoning: Formalization of Commonsense Reasoning*, New York: Ellis Horwood.

[^makinson-2005a]: Makinson, David, 2005a, “How to go non-monotonic”, in *Handbook of Philosophical Logic* (Volume 12, Second edition), Dov Gabbay and Franz Guenthner (eds.), Berlin: Springer-Verlag, 175–278.

[^makinson-2005b]: Makinson, David, 2005b, *Bridges from Classical to Nonmonotonic Logic*, London: King’s College Publications.

[^makinson-nd]: Makinson, David C. and Leendert van der Torre “Input/output logics”, *Journal of Philosophical Logic*, 29(4): 383–408.

[^marek-1991]: Marek, Victor and Truszczynski, Mirosaw, 1991, “Autoepistemic logic”, *Journal of the Association for Computing Machinery*, 38(3): 588–619.

[^marek-1989]: Marek, Wictor and Truszczynski, Mirosaw, 1989, “Relating autoepistemic and default logics”, in *KR’89: Principles of Knowledge Representation and Reasoning*, Ronald J. Brachman, Hector J. Levesque, and Raymond Reiter (eds.), San Mateo, California: Morgan Kaufmann, 276–288.

[^marek-1994]: Marek, Wictor and Truszczynski, Mirosaw, 1994, *Nonmonotonic Logic: Context-Dependent Reasoning*, Berlin: Springer-Verlag.

[^mccain-1995]: McCain, Norman and Turner, Hudson, 1995, “A causal theory of ramifications and qualifications”, in *Proceedings of the Fourteenth International Joint Conference on Artificial Intelligence*, Chris Mellish (ed.), San Francisco: Morgan Kaufmann, 1978–1984.

[^mccain-1997]: McCain, Norman and Turner, Hudson, 1997, “Causal theories of action and change”, in *Proceedings of the Thirteenth National Conference on Artificial Intelligence and the Eighth Innovative Applications of Artificial Intelligence Conference*, Howard Shrobe and Ted Senator (eds.), American Association for Artificial Intelligence, Menlo Park, California: AAAI Press, 460–465.

[^mccarthy-1959]: McCarthy, John, 1959, “Programs with common sense”, in *Proceedings of the Teddington Conference on the Mechanization of Thought Processes*, London: Her Majesty’s Stationary Office, 75–91.

[^mccarthy-1979]: McCarthy, John, 1979, “First order theories of individual concepts and propositions”, in *Machine Intelligence 9*, J.E. Hayes, D. Mitchie, and L.I. Mikulich (eds.), Chichester, England: Ellis Horwood, 129–148.

[^mccarthy-1980]: McCarthy, John, 1980, “Circumscription: A form of non-monotonic reasoning”, *Artificial Intelligence*, 13: 27–39.

[^mccarthy-1983]: McCarthy, John, 1983, “Situations, actions, and causal laws”, Tech. Rep. Memo 2, Stanford Artificial Intelligence Project, Stanford University.

[^mccarthy-1986]: McCarthy, John, 1986, “Applications of circumscription to formalizing common sense knowledge”, *Artificial Intelligence*, 13: 27–39.

[^mccarthy-1987]: McCarthy, John, 1987, “Epistemological problems of artificial intelligence”, in *Readings in Nonmonotonic Reasoning*, Matthew L. Ginsberg (ed.), Los Altos, California: Morgan Kaufmann, 46–55.

[^mccarthy-1993a]: McCarthy, John, 1993a, “History of circumscription”, *Artificial Intelligence*, 59: 23–26.

[^mccarthy-1993b]: McCarthy, John, 1993b, “Notes on formalizing contexts”, in *Proceedings of the Thirteenth International Joint Conference on Artificial Intelligence*, Ruzena Bajcsy (ed.), San Mateo, California: Morgan Kaufmann, 555–560.

[^mccarthy-1999]: McCarthy, John, 1999, [ “Elaboration tolerance” ](http://www-formal.stanford.edu/jmc/elaboration.html).

[^mccarthy-1998]: McCarthy, John and Buvac, Saša, 1998, “Formalizing context (expanded notes)”, in *Computing Natural Language*, Atocha Aliseda, Rob van Glabbeek, and Dag Westerståhl (eds.), Stanford, California: CSLI Publications, 13–50.

[^mccarthy-1969]: McCarthy, John and Hayes, Patrick J., 1969, “Some philosophical problems from the standpoint of artificial intelligence”, in *Machine Intelligence 4*, B. Meltzer and D. Michie (eds.), Edinburgh: Edinburgh University Press, 463–502.

[^mcdermott-1982]: McDermott, Drew, 1982, “Nonmonotonic logic II: Nonmonotonic modal theories”, *Journal of the Association for Computing Machinery*, 29(1): 33–57.

[^mcdermott-1980]: McDermott, Drew and Doyle, Jon, 1980, “Non-monotonic logic I”, *Artificial Intelligence*, 13: 41–72.

[^meyer-1995]: Meyer, John-Jules Ch. and van der Hoek, Wiebe, 1995, *Epistemic Logic for AI and Computer Science*, Cambridge: Cambridge University Press.

[^minker-1997]: Minker, Jack, 1997, “Logic and databases: Past, present and future”, *AI Magazine*, 18(3): 21–47.

[^minker-2000a]: Minker, Jack, 2000a, “Introduction to logic-based artificial intelligence”, in *Logic-Based Artificial Intelligence*, Jack Minker (ed.), Dordrecht: Kluwer Academic Publishers, 3–33.

[^minker-2000]: Minker, Jack (ed.), 2000, *Logic-Based Artificial Intelligence*, Dordrecht: Kluwer Academic Publishers.

[^minsky-1974]: Minsky, Marvin, 1974, “A framework for representing knowledge”, Tech. Rep. 306, Artificial Intelligence Laboratory, MIT. Republished in several places, including Haugeland 1981.

[^moore-1995]: Moore, Johanna, 1995, *Participating in Explanatory Dialogues*, The MIT Press.

[^moore-1993]: Moore, Robert C., 1993, “Autoepistemic logic revisited”, *Artificial Intelligence*, 59(1–2): 27–30.

[^moore-1995-2]: Moore, Robert C., 1995, *Logic and Representation*, Cambridge, England: Cambridge University Press.

[^morgenstern-1996]: Morgenstern, Leora, 1996, “The problem with solutions to the frame problem”, in *The Robot’s Dilemma Revisited: The Frame Problem in Artificial Intelligence*, Kenneth M. Ford and Zenon Pylyshyn (eds.), Norwood, New Jersey: Ablex Publishing Co., 99–133.

[^morgenstern-2001]: Morgenstern, Leora, 2001, “Mid-Sized Axiomatizations of Commonsense Problems: A Case Study in Egg Cracking”, *Studia Logica*, 67(3):333–384.

[^morgenstern-1994]: Morgenstern, Leora and Stein, Lynn, 1994, “Motivated action theory: a formal theory of causal reasoning”, *Artificial Intelligence*, 71(1): 1–42.

[^mueller-2006]: Mueller, Erik T., 2006, *Common Sense Reasoning*, Elsevier.

[^nakashima-1997]: Nakashima, Hideyuki, Matsubara, Hitoshi, and Osawa, Ichiro, 1997, “Causality as a key to the frame problem”, *Artificial Intelligence*, 91(1): 37–50.

[^nebel-1992]: Nebel, Bernhard, Rich, Charles, and Swartout, William (eds.), 1992, *KR’: Principles of Knowledge Representation and Reasoning*, San Francisco: Morgan Kaufmann.

[^nilsson-1991]: Nilsson, Nils J., 1991, “Logic and artificial intelligence”, *Artificial Intelligence*, 47(1–3): 31–56.

[^ohrstrom-1995]: Ohrstrom, Peter and Hasle, Per F.V., 1995, *Temporal Logic from Ancient Ideas to Artificial Intelligence*, Dordrecht: Kluwer Academic Publishers.

[^osherson-1990]: Osherson, Daniel N. and Lasnik, Howard (eds.), 1990, *An Invitation to Cognitive Science. Volume 2: Visual Cognition and Action*, Cambridge, Massachusetts: The MIT Press.

[^pearl-1994]: Pearl, Judea, 1994, “From Adams’ conditionals to default expressions, causal conditionals, and counterfactuals”, in *Probability and Conditionals: Belief Revision and Rational Decision*, Ellery Eells and Brian Skyrms (eds.), Cambridge, England: Cambridge University Press, 47–74.

[^pearl-2000]: Pearl, Judea, 2000, *Causality: Models, Reasoning, and Inference*, Cambridge, England: Cambridge University Press.

[^perlis-1985]: Perlis, Donald, 1985, “Languages with self-reference I: Foundations”, *Artificial Intelligence*, 25: 301–322.

[^pollack-1992]: Pollack, Martha, 1992, “The uses of plans”, *Artificial Intelligence*, 57(1): 43–68.

[^pollock-1995]: Pollock, John L., 1995, *Cognitive Carpentry: A Manual for How to Build a Person*, Cambridge, Massachusetts: The MIT Press.

[^prior-1956]: Prior, Arthur, 1956, *Time and Modality*, Oxford: Oxford University Press.

[^prior-1967]: Prior, Arthur, 1967, *Past, Present and Future*, Oxford: Oxford University Press.

[^prior-1968]: Prior, Arthur, 1968, *Papers on Time and Tense*, Oxford: Oxford University Press.

[^pylyshyn-1987]: Pylyshyn, Zenon (ed.), 1987, *The Robot’s Dilemma: The Frame Problem in Artificial Intelligence*, Norwood, New Jersey: Ablex Publishing Co.

[^quine-1960]: Quine, Willard V.O, 1960, “Variables explained away”, in *Selected Logic Papers*, Willard V. Quine (ed.), Cambridge, Massachusetts: Harvard University Press, 227–235.

[^rahwan-2009]: Rahwan, Iyad and Simari, Guillermo R., 2009, *Argumentation in Artificial Intelligence*, Berlin: Springer-Verlag.

[^reiter-1978]: Reiter, Raymond, 1978, “On closed world data bases”, in *Logic and Data Bases*, H. Gallaire and J. Minker (eds.), New York: Plenum Press, 55–76.

[^reiter-1980]: Reiter, Raymond, 1980, “A logic for default reasoning”, *Artificial Intelligence*, 13: 81–32.

[^reiter-1993]: Reiter, Raymond, 1993, “Proving properties of states in the situation calculus”, *Artificial Intelligence*, 64: 337–351.

[^reiter-2001]: Reiter, Raymond, 2001, *Knowledge in Action: Logical Foundations for Specifying and Implementing Dynamical Systems*, Cambridge, Massachusetts: The MIT Press.

[^rendsvig-2022]: Rendsvig, Rasmus and Symons,John 2022, “Epistemic logic”, in *The Stanford Encyclopedia of Philosophy* (Spring 2022 Edition), Edward M. Zalta (ed.), URL =[https://plato.stanford.edu/archives/spr2022/entries/logic-epistemic/“](https://plato.stanford.edu/archives/spr2022/entries/logic-epistemic/).

[^renz-1999]: Renz, Jochen and Nebel, Bernhard, 1999, ”On the complexity of qualitative spatial reasoning: A maximal tractable fragment of the region connection calculus“, *Artificial Intelligence*, 108(1–2): 69–123.

[^rosenschein-1989]: Rosenschein, Stanley J., 1989, ”Synthesizing information-tracking automata from environment descriptions“, in *KR’89: Principles of Knowledge Representation and Reasoning*, Ronald J. Brachman, Hector J. Levesque, and Raymond Reiter (eds.), San Mateo, California: Morgan Kaufmann, 386–393.

[^rosenschein-1995]: Rosenschein, Stanley J. and Kaelbling, Leslie Pack, 1995, ”A situated view of representation and control“, *Artificial Intelligence*, 73(1–2): 149–173.

[^russell-2020]: Russell, Stuart and Norvig, Peter, 2020, *Artificial Intelligence: A Modern Approach*, Englewood Cliffs, New Jersey: Prentice Hall, fourth edition.

[^russell-1991]: Russell, Stuart J. and Wefald, Eric, 1991, *Do the Right Thing*, Cambridge, Massachusetts: The MIT Press.

[^sadek-1992]: Sadek, M.D., 1992, ”A study in the logic of intention“, in *KR’92. Principles of Knowledge Representation and Reasoning: Proceedings of the Third International Conference*, Bernhard Nebel, Charles Rich, and William Swartout (eds.), San Mateo, California: Morgan Kaufmann, 462–473.

[^sandewall-1972]: Sandewall, Eric, 1972, ”An approach to the frame problem, and its implementation“, in *Machine Intelligence 7*, D. Michie and B. Meltzer (eds.), Edinburgh University Press, 195–204.

[^sandewall-1994]: Sandewall, Erik, 1994, *Features and Fluents: A Systematic Approach to the Representation of Knowledge About Dynamical Systems*, Oxford: Oxford University Press.

[^schlechta-1997]: Schlechta, Karl, 1997, *Nonmonotonic Logics*, Berlin: Springer-Verlag.

[^schlechta-2007]: Schlechta, Karl, 2007, ”Non-monotonic logics: A preferential approach“, in *Handbook of the History of Logic, Volume 8: The Many-Valued and Nonmonotonic Turn in Logic*, Dov Gabbay and John Woods (eds.), Amsterdam: Elsevier Science Publishers, 451–516.

[^schubert-1990]: Schubert, Lenhart, 1990, ”Monotonic solution of the frame problem in the situation calculus; an efficient method for worlds with fully specified actions“, in *Knowledge Representation and Defeasible Reasoning*, Henry Kyburg, Ronald Loui, and Greg Carlson (eds.), Dordrecht: Kluwer Academic Publishers, 23–67.

[^seligman-1996]: Seligman, Jerry and Moss, Lawrence S., 1996, ”Situation theory“, in *Handbook of Logic and Language*, Johan van Benthem and Alice ter Meulen (eds.), Amsterdam: Elsevier, 239–307.

[^shanahan-1997]: Shanahan, Murray, 1997, *Solving the Frame Problem*, Cambridge, Massachusetts: The MIT Press.

[^shanahan-2004]: Shanahan, Murray, 2004, ”An attempt to formalise a non-trivial benchmark problem in common sense reasoning“, *Artificial Intelligence*, 153(1–2): 141–165.

[^shanahan-2009]: Shanahan, Murray, 2009, ”The Frame Problem“, *The Stanford Encyclopedia of Philosophy* (Winter 2009 Edition), Edward N. Zalta (ed.), URL $= \langle$[https://plato.stanford.edu/archives/win2009/entries/frame-problem/](https://plato.stanford.edu/archives/win2009/entries/frame-problem/)$\rangle$.

[^shoham-1988]: Shoham, Yoav, 1988, *Reasoning About Change: Time and Causation From the Standpoint of Artificial Intelligence*, Cambridge, Massachusetts: The MIT Press.

[^simon-1952]: Simon, Herbert, 1952, ”On the definition of the causal relation“, *The Journal of Philosophy*, 49: 517–528.

[^simon-1966]: Simon, Herbert, 1966, ”On reasoning about action“, Tech. Rep. Complex Information Processing Paper #87, Carnegie Institute of Technology, Pittsburgh, Pennsylvania.

[^simon-1977]: Simon, Herbert A., 1977, *Models of Discovery*, Dordrecht: D. Reidel Publishing Co.

[^simon-1982a]: Simon, Herbert A., 1982a, *Models of Bounded Rationality, Volume 1*, Cambridge, Massachusetts: The MIT Press.

[^simon-1982b]: Simon, Herbert A., 1982b, *Models of Bounded Rationality, Volume 2*, Cambridge, Massachusetts: The MIT Press.

[^simons-1987]: Simons, Peter, 1987, *Parts: A Study in Ontology*, Oxford: Oxford University Press.

[^snidaro-2019]: Snidaro, Lauro, Herrero Jesús Garcíia, Llinas, James, and Blash, Erik, 2019, ”Recent trends in context exploitation for information fusion and AI“, *The AI Magazine*, 40(3): 14–27.

[^stalnaker-1993]: Stalnaker, Robert C., 1993, ”A note on non-monotonic modal logic“, *Artificial Intelligence*, 64(2): 183–196. Widely circulated in manuscript form, 1980 to 1992.

[^stefik-1995]: Stefik, Mark J., 1995, *An Introduction to Knowledge Systems*, San Francisco: Morgan Kaufmann.

[^stock-1997]: Stock, Oliviero (ed.), 1997, *Spatial and Temporal Reasoning*, Dordrecht: Kluwer Academic Publishers.

[^stone-1998]: Stone, Matthew, 1998, *Modality in Dialogue: Planning, Pragmatics and Computation*, Ph.D. dissertation, Computer Science Department, University of Pennsylvania, Philadelphia, Pennsylvania.

[^straßer-2014]: Straßer, Christian, 2014, *Adaptive Logic and Defeasible Reasoning: Applications in Argumentation, Normative Reasoning and Default Reasoning*, Berlin: Springer Verlag.

[^straßer-2019]: Straßer, Christian, and Antonelli, G. Aldo, 2019, ”Non-Monotonic Logic“, *The Stanford Encyclopedia of Philosophy* (Winter 2012 Edition), Edward N. Zalta (ed.), URL $= \langle$[https://plato.stanford.edu/archives/win2012/entries/logic-nonmonotonic/](https://plato.stanford.edu/archives/win2012/entries/logic-nonmonotonic/)$\rangle$.

[^thielscher-1989]: Thielscher, Michael, 1989, ”Ramification and causality“, *Artificial Intelligence*, 89(1–2): 317–364.

[^thielscher-1996]: Thielscher, Michael, 1996, ”Causality and the qualification problem“, in *KR’96: Principles of Knowledge Representation and Reasoning*, Luigia Carlucci Aiello, Jon Doyle, and Stuart Shapiro (eds.), San Francisco, California: Morgan Kaufmann, 51–62.

[^thielscher-2005]: Thielscher, Michael, 2005, *Reasoning Robots: The Art and Science of Programming Robotic Agents*, Dordrecht: Kluwer Academic Publishers.

[^thielscher-2018]: Thielscher, Michael, Toni, Francesco, and Wolter, Frank (eds.), 2018, *KR2018: Principles of Knowledge Representation and Reasoning*, Menlo Park, California: AAAI Press.

[^thomason-1992]: Thomason, Richmond H., 1992, ”NETL and subsequent path-based inheritance theories“, in *Semantic Networks in Artificial Intelligence*, Fritz Lehmann (ed.), Oxford: Pergamon Press, 179–204.

[^thomason-2003]: Thomason, Richmond, 2003, ”Dynamic contextual intensional logic: logical foundations and an application“, in *Modeling and Using Context: Fourth International and Interdisciplinary Conference*, Patrick Blackburn, Chiara Ghidini, and Roy Turner (eds.), Berlin: Springer-Verlag, 328-341.

[^thomason-2005]: Thomason, Richmond, 2005, ”Making contextual intensional logic nonmonotonic“, in *Modeling and Using Context: Fifth International and Interdisciplinary Conference*, Anind Dey, Boicho Kokinov, David Leake, and Roy Turner (eds.), Berlin: Springer-Verlag, 502–514.

[^turner-1999]: Turner, Hudson, 1999, ”A logic of universal causation“, *Artificial Intelligence*, 113(1–2): 87–123.

[^benthem-1983]: van Benthem, Johan, 1983, *The Logic of Time*, Dordrecht: D. Reidel Publishing Company.

[^torre-1997]: van der Torre, Leendert W.N., 1997, *Reasoning about Obligations: Defeasibility in Preference-Based Deontic Logic*, Amsterdam: Thesis Publishers.

[^harmelen-2008]: van Harmelen, Frank, Lifschitz, Vladimir, and Porter, Bruce (eds.) 2008,*Handbook of Knowledge Representation*, Amsterdam: Elsevier.

[^wright-1983]: von Wright, Georg Henrik, 1983, *Practical Reason: Philosophical Papers, Volume 1*, Ithaca: Cornell University Press.

[^weld-1990]: Weld, Daniel S. and de Kleer, Johan (eds.), 1990, *Qualitative Reasoning about Physical Systems*, San Mateo, California: Morgan Kaufmann.

[^wilson-1998]: Wilson, Randall H., 1998, ”Geometric reasoning about assembly tools“, *Artificial Intelligence*, 98(1–2): 237–279.

[^wobcke-1998]: Wobcke, Wayne, Pagnucco, Maurice, and Zhang, C. (eds.), 1998, *Agents and Multi-Agent Systems—Formalisms, Methodologies, and Applications*, Berlin: Springer-Verlag.

[^wolter-2000]: Wolter, Frank and Zakharyaschev, Michael, 2000, ”Spatio-temporal representation and reasoning based on RCC-8“, in *KR2000: Principles of Knowledge Representation and Reasoning*, Anthony G. Cohn, Fausto Giunchiglia, and Bart Selman (eds.), San Francisco: Morgan Kaufmann, 3–14.

[^woods-1992]: Woods, William A. and Schmolze, James G., 1992, ”The KL-ONE family“, in *Semantic Networks in Artificial Intelligence*, Fritz Lehmann (ed.), Oxford: Pergamon Press, 133–177.

[^wooldridge-2000]: Wooldridge, Michael J., 2000, *Reasoning about Rational Agents*, Cambridge, England: Cambridge University Press.

[^yeap-1999]: Yeap, Wai K. and Jeffries, Margaret E., 1999, ”Computing a representation of the local environment“, *Artificial Intelligence*, 107(2): 265–301.
