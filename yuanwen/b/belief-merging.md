# Belief Merging and Judgment Aggregation
**First published Wed Jul 8, 2015; substantive revision Mon Jun 9, 2025**

*Pigozzi, Gabriella*

Groups often need to reach decisions and decisions can be complex, involving the assessment of several related issues. For example, in a university a hiring committee typically decides on a candidate on the basis of her teaching and research qualities. A city council confronted with the decision of building a bridge, may ask its members to state whether they are favorable or not and, at the same time, to provide reasons for their position (like economical and environmental impacts, or expenditure considerations). Lastly, jurors are required to decide on the liability of a defendant by expressing their judgments on the conditions prescribed by the relevant code of law for the case at hand. As pointed out by Kornhauser and Sager (1986) referring to real jury trials, the aggregation of individual opinions on logically interrelated propositions can lead to a paradoxical result, the so-called *doctrinal paradox*. Inspired by the doctrinal paradox in jurisprudence, the problem of judgment aggregation attracted the interest of political scientists, philosophers, logicians, economists and computer scientists. Links to social choice theory have shown that, similar to the problem of preference aggregation (Arrow 1951/1963; Sen 1970)[^arrow-1951][^sen-1970], a judgment aggregation procedure that satisfies a number of desirable properties does not exist.

The question judgment aggregation addresses is how we can define aggregation procedures that preserve individual rationality at the collective level. From a philosophical point of view, such question concerns the nature of group attitudes such as group beliefs (Roth 2011)[^roth-2011]. When the city council decides to build the bridge, the decision is taken on the basis of individual beliefs that, for example, the bridge will have a positive impact on the development of the economic activities in the area and does not represent an environmental threat. Thus, the formal approach to judgment aggregation can serve to cast light on the dependence between individual and collective beliefs (if there are any). The questions tackled by judgment aggregation are also relevant for the testimony problem investigated in social epistemology (Goldman 1999, 2004, 2010)[^goldman-1999]. How shall the diverging opinions of experts in a panel be combined and how should a rational agent respond to such disagreement?

The problem of combining potentially conflicting pieces of information does not arise only when a group of people needs to make a decision. Artificial intelligence also explores ways to aggregate conflicting sensors’ information, experts’ opinions or databases into a consistent one (Bloch et al. 2001)[^bloch-2001]. The combination of information coming from heterogeneous sensors improves the deficiencies of the individual sensors increasing the performances of a system. Examples are sensors of gesture recognition, screen rotation, and accelerometer in smart phones. Distributed databases may need to be accessed and managed at the same time to share data, for example, a hospital may need to access the data collected about patients by different units. Internet users can find ratings on products provided by people who have purchased and assessed them on different online platforms. The type of information to be combined can differ, and so its representation can be numerical or symbolic: numbers, linguistic values, statistical probability distributions, binary preferences, utility functions etc. Yet all examples mentioned above deal with the problem of merging items coming from heterogeneous sources and with the issue of managing conflicts. At a purely formal level, belief merging studies the fusion of independent and equally reliable sources of information expressed in propositional logic. As with judgment aggregation, belief merging addresses the problem of fusing several individual bases expressed in propositional logic into a consistent one. Given the structural similarity of the problems investigated by these two disciplines, exploring their connections can reveal how similar these formalisms really are. On a more practical level, the application of operators defined in belief merging to judgment aggregation problems lead to the definition of a wider class of aggregation operators for judgment aggregation, the so-called *distance-based procedures*.

The focus of this entry is to draw explicit connections between judgment aggregation and the belief merging literature. Judgment aggregation will be briefly introduced in the next section. For a more comprehensive introduction to judgment aggregation the reader is referred to (Grossi and Pigozzi 2014; Endriss 2016)[^endriss-2016][^grossi-2014].

## 1. Judgment Aggregation

The formal work on judgment aggregation stemmed from the “doctrinal paradox” in the jurisprudence literature (Kornhauser and Sager 1986, 1993, 2004; Kornhauser 1992)[^kornhauser-1992][^kornhauser-1986]. The paradox shows that judges may face a real danger of falling into collective irrationality when trying to reach a common and justified verdict. Despite the recent birth of the discipline, structurally similar problems seemed to have been first pointed out by Poisson in 1837 (as pointed out in Elster 2013)[^elster-2013], and later noted by the Italian legal theorist Vacca in 1921 (see Spector 2009)[^spector-2009].

In Kornhauser and Sager’s court example (1993), a three-member court has to reach a verdict in a breach of contract case between a plaintiff and a defendant. According to the contract law, the defendant is liable for breach of contract (proposition *r*) if and only if the contract forbid the defendant to do a certain action *X* (proposition *p*) and the defendant did action *X* (proposition *q*). Suppose that the three judges express the judgments as in Table 1.

*Table 1:*

|   | Obligation (*p*) | Action (*q*) | Defendant liable (*r*) |
| --- | --- | --- | --- |
| Judge 1 | True | True | True |
| Judge 2 | True | False | False |
| Judge 3 | False | True | False |
| Majority | True | True | False |

Table 1: The doctrinal paradox

Proposition *r* is the *conclusion*, whereas *p* and *q* are the *premises*. The legal doctrine can thus be logically expressed as $(p\land q)\leftrightarrow r$, stating that premises *p* and *q* are both necessary and sufficient for the conclusion *r*. Table 1 shows that each judge respects the given legal doctrine, by declaring the conclusion to be true if and only if she deems both premises true. If the judges aggregate their individual opinions using majority rule on the judgments on each proposition, the resulting judgment set is {*p*, *q*, not *r*}, which constitutes a violation of the legal doctrine. This is an instance of the doctrinal paradox: despite the individuals being logically consistent, the group’s judgment on the propositions is not consistent with the legal doctrine. In the example above, the judges cannot declare the defendant not liable and, at the same time, state that both conditions for her liability apply. Thus, the court faces a dilemma. Either judges are asked to express judgments on the premises only, and the court’s decision on *r* is logically derived from the majority on the premises (the *premise-based* or *issue-by-issue procedure*), or the verdict is decided by the majority judgment on *r* (the *conclusion-based* or *case-by-case procedure*) ignoring the opinions on the premises. Instances such as that in Table 1 illustrate that the two procedures may give opposite results. In the court example the issues on which the judges have to express a position are distinguished into premises and conclusion. We should note, however, that the theory of judgment aggregation does not require such a distinction. The court decision of declaring the defendant not liable (despite a majority in favour of the two criteria to declare her liability) would be inconsistent with the decision rule $(p \land q) \leftrightarrow r$ even without a distinction between premises and conclusion.

This was not the first time that the definition of a collective outcome by majority rule resulted in a paradoxical result. Already in 1785, the Marquis de Condorcet discovered what is now known as the *Condorcet paradox*. Given a set of individual preferences, if we compare each of the alternatives in pairs and apply majority voting, we may obtain an intransitive preference (or cycle) in the collective outcome, of the type that alternative *x* is preferred to *y*, *y* is preferred to *z*, and *z* to *x*, making it impossible to declare an alternative the winner. The similarities between the Condorcet paradox and the judgment aggregation paradox were promptly noticed by Kornhauser and Sager (1986) and List and Pettit (2004). The study of the aggregation of individual preferences into a social preference ordering is the focus of social choice theory (List 2013)[^list-2013]. The Nobel Prize winner Kenneth Arrow proved the landmark result by showing that the problem which Condorcet stumbled upon is more general and not limited to majority rule. Arrow’s impossibility theorem (Arrow 1951/1963; Morreau 2014)[^arrow-1951][^morreau-2014] states that, given a finite set of individual preferences over three or more alternatives, there exists *no* aggregation function that satisfies a few plausible axioms. There are a number of results similar to Arrow’s theorem that demonstrate the “impossibility” of judgment aggregation. The first impossibility theorem of judgment aggregation (List and Pettit 2002)[^list-2002][^list-2002-2] was followed by further generalizations (Pauly and van Hees 2006; Dietrich 2006; Mongin 2008)[^dietrich-2006][^mongin-2008][^pauly-2006].

Let us restrict attention to the aggregation of judgments formulated in the language *L* of propositional logic (the problem of judgment aggregation can be generalized to modal and conditional logics as well as predicate logic, see Dietrich 2007; for a more in-depth discussion of non-classical logics and judgment aggregation see Grossi 2009, Porello 2017 and Xuefeng 2018)[^dietrich-2007][^grossi-2009][^porello-2017][^xuefeng-2018]. The set of formulas on which the individuals express judgments is called *agenda* $(A\subseteq L$). The agenda does not contain double negations $(\neg \neg \varphi$ is equivalent to $\varphi$), is closed with respect to negation (i.e., if $\varphi \in A$, then also $\neg \varphi \in A$) and is generally assumed not to contain tautologies or contradictions. For example, the agenda of the court case is $A = \{p, \neg p, q, \neg q, p \wedge q, \neg (p \wedge q)\}$. Dietrich and List (2007a) showed that, when the agenda is sufficiently rich (like, for instance, the agenda of the court decision or $\{p, \neg p, q, \neg q, p \to q, \neg (p \to q)\}$), the only judgment aggregation rules satisfying the *desiderata* below are dictatorships. An aggregation function is a dictatorship when, for *any* input, the collective outcome is taken to be the individual judgment of one (and the same) individual, i.e., the dictator. In a dictatorial aggregation function all individual inputs but the dictator’s are ignored. A *judgment set* is a consistent and complete set of formulae $J \subseteq A$. A judgment set is complete if, for any element $\varphi$ of the agenda, either $\varphi\in A$ or $\neg \varphi\in A$ (that is, any item of the agenda has to be accepted of rejected). Given a group of *n* individuals, a *profile* is a *n*-tuple of individual judgment sets $\langle J_1, \ldots, J_n \rangle$. Finally, a *judgment aggregation rule F* is a function that assigns to each profile $\langle J_1, \ldots, J_n\rangle$ a collective judgment set $F(J_1, \ldots, J_{n}) \subseteq A$. The conditions imposed on *F* are the following:

**Universal Domain:** All profiles of consistent and complete (with respect to the agenda) judgment sets are accepted as input of the aggregation function. The profile of the doctrinal paradox in Table 1 is a legitimate input because the judges expressed acceptance or rejection on each issue in the agenda and their opinions respected the rule $(p \wedge q) \leftrightarrow r$.

**Collective Rationality:** Only complete and consistent collective judgments are acceptable as outputs. The collective judgment of the example in Table 1 is complete (the group accepts or rejects each agenda’s item) but is not consistent because it violates the rule $(p \wedge q) \leftrightarrow r$.

**Independence:** The collective judgment on each proposition depends only on the individual judgments on that proposition, and not on other (considered to be independent) propositions in the agenda. (This condition reformulates in the judgment aggregation framework the *independence of the irrelevant alternatives* condition in Arrow’s theorem for preference aggregation.) Proposition-wise majority rule (as in the court example in Table 1) satisfies the independence condition because the group acceptance/rejection of each agenda’s item depends on whether a majority of the individuals accepted/rejected that proposition.

**Unanimity Preservation:** If all individuals submit the same judgment on a proposition *p*$\in$ *A*, this is in the collective judgment set.

Despite the undemanding conditions, it can be shown that there exists no judgment aggregation rule *F* that jointly satisfies the above conditions that is not a dictatorship. This impossibility result is particularly meaningful because, when reformulated for a preference framework, it can be shown that Arrow’s theorem (for strict preference orderings) is obtained as a corollary (Dietrich and List 2007a)[^dietrich-2007a]. This led Dietrich and List to say that judgment aggregation can be seen as a more general problem than preference aggregation (see Grossi and Pigozzi 2014 for details on such reformulation)[^grossi-2014].

In addition to formal connections between the two types of aggregation problems, from a conceptual point of view judgment aggregation extends the problems of preference aggregation to more general decision problems. Although the models provided by social choice have improved our understanding of many familiar collective decision problems such as elections, referenda and legislative decisions, they focus primarily on collective choices between alternative outcomes such as candidates, policies or actions. They do not capture a whole class of decision problems in which a group has to form collectively endorsed beliefs or judgments on *logically interconnected* propositions. Yet, as the examples given in the introduction also show, such decision problems are common and not limited to court decisions. Pettit (2001) coined the term of *discursive dilemma* to highlight the fact that such problem can arise in all situations in which a group of individuals needs to reach a common stance on multiple propositions.

Impossibility results often bear a negative flavor. However, they also indicate possible escape routes. Consistent collective outcomes can be obtained when the universal domain condition is relaxed (considering, for example, *unidimensionally aligned* profiles (List 2002)[^list-2002][^list-2002-2], a conditions similar to Black’s single-peakedness in preference aggregation (Black 1948)[^black-1948]) or when the collective rationality condition is limited to require consistent (but not complete) collective judgments. Possibility results are also obtained when the independence condition is relaxed. The premise-based procedure seen in the court’s case is an example of an aggregation rule that violates independence. There, the collective position on the conclusion is derived by logical implication from the majority judgments on the premises. More in general, *sequential priority rules* violate independence and guarantee consistent group positions: the elements of the agenda are aggregated following a pre-fixed order, and earlier decisions constrain later ones. The reader is referred to (List and Puppe 2009; List 2013; Grossi and Pigozzi 2014; Endriss 2016)[^endriss-2016][^grossi-2014][^list-2013][^list-2009] for thorough introductions to judgment aggregation and an overview on more impossibility theorems as well as on escapes routes from such results. In the next section we introduce the problem of combining conflicting information as it has been addressed in computer science. We will see that some operators introduced in belief merging are instances of aggregation procedures that violate the independence condition and that such operators can be applied to hold concrete aggregation procedures to judgment aggregation problems.

## 2. Belief Merging

Computer scientists have studied the aggregation of several independent and potentially conflicting sources of information into a consistent one. As mentioned in the introduction, examples are the combination of conflicting sensors’ information received by an agent, the aggregation of multiple databases to build an expert system, and multi-agent systems (Borgida and Imielinski 1984; Baral et al. 1992; Chawathe et al. 1994; Elmagarmid et al. 1999; Subrahmanian 1994; Kim 1995)[^baral-1992][^borgida-1984][^chawathe-1994][^elmagarmid-1999][^kim-1995][^subrahmanian-1994]. Belief merging (or *fusion*) studies the aggregation of symbolic information (expressed in propositional logic) into a consistent base. As we shall see, the process of merging several bases has tight links with *belief change* (or *belief revision*), an active discipline since the 1980s across formal philosophy and computer science that models how human and artificial agents change their beliefs when they encounter new information. Revision, expansion and contraction are the three main types of theory change studied by Alchourrón, Gärdenfors and Makinson (the so-called AGM theory) who also provided rationality postulates for each of them (Alchourrón et al. 1985; Gärdenfors 1988)[^alchourrón-1985][^gärdenfors-1988]. In belief revision, the focus is on how one belief base changes in face of new, completely reliable information and this new piece may be conflicting with existing beliefs in the base. When I learn that a new acquaintance Rob has a child, I simply add the piece of information and eventually derive new consequences (this is expansion). The most interesting case, though, is when the new information conflicts with previously held beliefs. Suppose that from a common friend I understood that Rob had no kids. Now I learn from Rob himself that he has a child. In order to accommodate the new information, I need to perform a revision, which consists of removing the wrong belief that he had no kids (and all the other beliefs that may depend on that), add the new input that in fact he has a child, and derive possibly new consequences (see Hansson 2011 for an overview and Fermé and Hansson 2018 for a comprehensive introduction to belief change)[^fermé-2018][^hansson-2011]. As for belief revision, in merging the term “knowledge” is used in a broader sense than in the epistemological literature, such that “knowledge” refers to formulas accepted by an agent (i.e., formulas in her knowledge base), which are not necessarily true. Then, “knowledge base” and “belief base” are used interchangeably. For Grégoire and Konieczny (2006) belief merging operators can be used to aggregate also other types of information than knowledge and beliefs, such as goals, observations, and norms.

If belief revision focuses on how one base changes following the addition of a new piece of information, belief fusion studies how to aggregate several different and potentially conflicting bases (like, for instance, different experts’ opinions, several databases, information coming from different sources etc.) to obtain a consistent base. Different approaches have been proposed in the literature. Here we briefly mention *combination* and *arbitration* before moving to the merging operators as defined by Konieczny and Pino Pérez, which have been applied to judgment aggregation. The first approach to the problem of dealing with aggregating different and possibly inconsistent databases (Baral et al. 1991; Baral et al. 1992)[^baral-1991][^baral-1992] built on Ginsberg’s idea of considering maximally consistent subsets when facing an inconsistent theory (Ginsberg 1986)[^ginsberg-1986], such as the one that may result from the union of the information coming from several self-consistent (but conflicting with one another) agents. Combination operators take the union of the knowledge bases (a finite set of logical formulas) and, if the union is logically inconsistent, select some maximal consistent subsets. The logical properties of such *combination* operators have been investigated in (Konieczny 2000)[^konieczny-2000] and compared to *merging* operators as defined in (Konieczny and Pino Pérez 1998, 1999)[^konieczny-1998]. There are several differences between combining and merging knowledge bases. One difference is that the method by Baral et al. (1991, 1992) is syntax-dependent while merging operators obey the principle of irrelevance of syntax. According to the principle of irrelevance of syntax, an operation on two equivalent knowledge bases should return two equivalent knowledge bases. For instance, $K_1 = \{a, b\}$ and $K_{2}= \{a \wedge b\}$ have the same logical consequences. So, if $K_3 = \{\neg b\}$, merging $K_1$ with $K_3$ or merging $K_2$ with $K_3$ will give two equivalent knowledge bases. On the other hand, the combination of $K_1$ and $K_3$ may not be logically equivalent to the combination of $K_2$ and $K_3$. Let $E_1 = K_1 \bigsqcup K_3$ ($\bigsqcup$ is the union on multi-set) and $E_2 = K_2 \bigsqcup K_3$. The maximal consistent subsets of $E_1$ are $\{a, b\}$ and $\{a, \neg b\}$, and those of $E_2$ are $\{a \wedge b\}$ and $\{\neg b\}$. So each maximal consistent subset of $E_1$ implies $a$, but this is not the case for all maximal consistent subsets of $E_2$ (example from Konieczny 2000)[^konieczny-2000]. Another difference is that when combination operators are used, the information about the source of the knowledge bases is ignored. This means that, unlike merging, combination operators cannot take into account cardinality considerations. Suppose, for example, that four medical experts advise on the effectiveness of four vaccines for adults over 65 years old. Let the propositions $a, b, c, d$ stand for “Vaccine A (respectively, B, C, D) is effective in over-65s”. If two experts agree that vaccines A and B are effective in over-65s, one expert esteems that vaccine D (but not vaccine A) is effective and, finally, the last expert agrees with the first two that vaccine A is effective and that, if B is effective in over-65s, so is vaccine C too, we can represent the four experts opinions as four knowledge bases: $K_1 = K_{2}= \{a, b\}$, $K_{3}= \{\neg a, d\}$ and $K_4 = \{a, b\rightarrow c\}$. The union of these four bases is $\{a,\neg a, b, b\rightarrow c, d\}$, which is clearly logically inconsistent. Considering maximal consistent subsets is one way to avoid inconsistency while retaining as much information as possible. In this example, the two maximal consistent subsets are: $\{a, b,b\rightarrow c, d\}$ and $\{\neg a, b, b\rightarrow c, d\}$. This means that we cannot decide whether to accept *a* or $\neg a$. However, a majority of knowledge bases contained *a*, and only one base contained $\neg a$. It seems intuitive that *a* should be in the resulting knowledge base as long as all knowledge bases are treated equally. If, for whatever reason, $K_{3}$ is more trustworthy than the other knowledge bases, then we may prefer a combined base in which $\neg a$ is accepted.

*Arbitration* is another operator to fuse knowledge bases that has been introduced in the early Nineties (Revesz 1993, Liberatore and Schaerf 1995)[^liberatore-1995][^revesz-1993]. In belief revision, it is commonly assumed that the new information is accepted and must be included in the revised base. By contrast, arbitration addresses situations in which two sources give contradicting information but are equally reliable (examples are two equally competent experts, two equally trustworthy witnesses etc.). If we have no reason to dismiss one of the two sources, the solution is to fuse the two bases rather than revise one by the other. The operation is arbitration in the sense that, since both sources are equally reliable, the resulting base should contain as much as possible of both sources. Liberatore and Schaerf (1995) proposed axioms for arbitration between two belief bases, and the operator proposed by Revesz only satisfied some of them. Their proposal suffered from the fact of being limited to the arbitration of only two bases. This limitation is overcome in the belief merging approach, where a finite number of bases can be merged into a consistent one.

None of the above methods could take into account the popularity of a specific information item. This meant that those operators could not capture the view of the majority. The first to introduce a majority postulate for the merging of several knowledge bases were Lin and Mendelzon (1999). The idea was inspired by the majority rule in social choice theory. However, their majority postulate includes a notion of *partial support* that captures the specificity of knowledge merging with respect to voting, and is not limited to count the number of bases supporting a proposition *a vs.* the number of bases containing $\neg a$. A knowledge base was defined to partially support a literal *l* if there is a proposition *a* that contains no atoms appearing in *l*, such that the agent believes either *l* or *a* is true without knowing which one. A model-theoretic characterization of the postulates and specific merging operators are given in Lin and Mendelzon (1999). In the belief merging literature, sources of information are generally assumed to be equally reliable. One way to help to solve the conflict is to relax this assumption as, for example, in the extension to merging weighted knowledge bases given in (Lin 1996)[^lin-1996][^lin-1996-2] or in prioritized knowledge bases (Benferhat et al. 1998; Cholvy 1998; Delgrande et al. 2006)[^benferhat-1998][^cholvy-1998][^delgrande-2006].

A new set of postulates for merging operators and the distinction (in terms of axioms they satisfy) between arbitration and majority operators were introduced by Konieczny and Pino Pérez (1998). In subsequent works (Konieczny and Pino Pérez 1999, 2002)[^konieczny-1999] they extended the framework to include merging under *integrity constraints*, that is, a set of exogenously imposed conditions that have to be satisfied by the merged base (Kowalski 1978; Reiter 1988)[^kowalski-1978][^reiter-1988]. In the next section we present the formal framework introduced by Konieczny and Pino Pérez, which is now the standard framework for belief merging as it overcomes the limitations of the previous proposals.

The formal methods developed in belief merging have been exported and applied in areas of social epistemology, like elections and preference aggregation (Meyer et al. 2001)[^meyer-2001], group consensus (Gauwin et al. 2005)[^gauwin-2005], and judgment aggregation (Pigozzi 2006)[^pigozzi-2006] to which we return in Section 2.2.

### 2.1 A framework for merging under integrity constraints

Konieczny and Pino Pérez consider a propositional language *L* built up from a finite set *At* of atomic propositions and the usual connectives $(\neg, \land, \lor , \rightarrow, \leftrightarrow )$. An interpretation is a total function $At \rightarrow \{0, 1\}$ that assigns 0 (false) or 1 (true) to each atomic proposition. For example, if $At =\{p, q, r\}$, then $(1, 0, 1)$ is the interpretation that assigns true to *p* and *r* and false to *q*.[^note-1] Denote the set of all interpretations by $W = \{0, 1\}^{At}$. For any formula $\varphi \in L$, $\mymod(\varphi) = \{\omega \in W | \omega \models \varphi\}$ denotes the set of models of $\varphi$, i.e., the set of truth assignments that makes $\varphi$ true. If we take the formula that expressed the contractual law in the doctrinal example, then $\mymod((p\land q) \leftrightarrow r) = \{(1,1,1), (1, 0, 0), (0, 1, 0), (0,0,0)\}.$ As usual, a formula $\varphi$ is consistent if it has at least a model, and a formula $\varphi$ follows from a set of formulae $\Phi$ if every interpretation that makes all formulae in $\Phi$ true, makes also $\varphi$ true.

A *belief base* $K_i$ is a finite set of propositional formulas representing the explicit beliefs held by individual *i*. Each $K_{i}$ is assumed to be consistent. $\mathcal{K}$ denotes the set of all consistent belief bases. The postulates for merging consider a *multi-set* of belief bases (*belief profile*, or *belief set*, the terminology used in early papers) $E = \{K_1, \ldots , K_{n}\}$. The reason for using multi-sets is that an element can appear more than once, thus allowing the representation of the fact that two or more agents can hold the same beliefs. This is needed to take into account the popularity of a piece of information, hence to define majority operators. To mark the distinction with the usual set union $\cup$, the multi-set union is denoted by $\sqcup$ and defined as $\{\varphi\} \sqcup \{\varphi\} = \{\varphi, \varphi\}$. Two belief profiles are equivalent $(E_1\equiv E_{2})$ if and only if there exists a bijection *f* from $E_1$ to $E_{2}$ such that, for any $B\in E_1$, we have that $\models\land f(B)\leftrightarrow \land B$.

Integrity constraints represent extra conditions that should follow from the merged bases. The interest of integrity constraints is to ensure that the aggregation of individual pieces of information satisfies some problem-specific requirement. For example, suppose that members of a city council have to decide what to build in a certain area. We can have constraints on the available budget (enough to cover only some of the projects) but also constraints on the coexistence of different projects (we may not build a parking lot and a playground in that area, but we may build a playground and a public library). If the (possibly empty) set of integrity constraints is denoted by the belief base *IC*, $\Delta_{\IC}(E)$ denotes the result of merging the multi-set *E* of belief bases given *IC*. Intuitively, the result will be a consistent belief base representing the collective beliefs and implying *IC*.

Konieczny and Pino Pérez (1999, 2002) put forward the following postulates for *IC* fusion operators between equally reliable sources. Let $E$, $E_1$, $E_{2}$, be belief profiles, $K_1$, $K_{2}$ be consistent belief bases, and $\IC$, $\IC_1$, $\IC_{2}$, be integrity constraints. $\Delta$ is an *IC* fusion operator if and only if it satisfies the following rationality postulates:

**(IC0)**

$\Delta_{\IC}(E) \models \IC$

**(IC1)**

If $\IC$ is consistent, then $\Delta_{\IC}(E)$ is consistent.

**(IC2)**

If $\land E$ is consistent with *IC*, then $\Delta_{\IC}(E)\equiv \land E\land \IC$

**(IC3)**

If $E_1\equiv E_{2}$, and $\IC_1\equiv \IC_{2}$, then $\Delta_{\IC_1}(E_1)\equiv \Delta_{\IC_2}(E_{2})$

**(IC4)**

If $K_1 \models\IC$ and $K_{2} \models\IC$, then $\Delta_{\IC}(\{K_1, K_{2}\})\land K_1$ is consistent if and only if $\Delta_{\IC}(\{K_1, K_{2}\})\land K_{2}$ is consistent.

**(IC5)**

$\Delta_{\IC}(E_1) \land \Delta_{\IC}(E_{2}) \models\Delta_{\IC}(E_1\sqcup E_{2})$

**(IC6)**

If $\Delta_{\IC}(E_1) \land \Delta_{\IC}(E_{2})$ is consistent, then $\Delta_{\IC}(E_1\sqcup E_{2}) \models \Delta_{\IC}(E_1) \land \Delta_{\IC}(E_{2})$

**(IC7)**

$\Delta_{\IC_{1}}(E) \land \IC_{2} \models\Delta_{\IC_{1\land} \IC_{2}} (E)$

**(IC8)**

If $\Delta_{\IC_1}(E) \land \IC_{2}$ is consistent, then $\Delta_{\IC_{1\land}\IC_{2}} (E) \models\Delta_{\IC_1}(E)$

In order to illustrate these postulates, we consider the following example, due to (Konieczny and Pino Pérez 1999)[^konieczny-1999]. A group of flats co-owners wish to improve their condominium. At the meeting, the chairman proposes to build a tennis court, a swimming pool or a private parking. He also points out that building two of the three options will lead to a significant increase of the yearly maintenance expenses (this corresponds to the *IC*).

(IC0) ensures that the resulting merged base satisfies the integrity constraints. This is an obvious condition to impose since these are postulates for merging under integrity constraints, where the idea is to ensure that the result of the merging satisfies the integrity constraints. By employing a merging operator, the chairman knows that the group will agree on the increase of the expenses, if they decide to build at least two of the three facilities. (IC1) states that, when *IC* is consistent, then the result of the fusion operator will also be consistent. Again, given that the interpretations of the merged bases are selected among the interpretations of the integrity constraints, if *IC* is consistent, the result will also be consistent. (IC2) states that the result of the merging operator is simply the conjunction of the belief profile and the *IC*, whenever such conjunction is consistent. In our running example, if each person wishing to build two or more facilities endorses the rise of the expenses and the opinions given by the co-owners are consistent, then the merging will just return the conjunction of the *IC* and the individual opinions. (IC3) states that if two belief profiles $E_1$ and $E_{2}$ are logically equivalent and $\IC_1$ and $\IC_{2}$ are also equivalent, then merging the first belief profile with $\IC_1$ will be equivalent as merging the second belief profile with $\IC_{2}$. This postulate expresses a principle already imposed on belief revision operators (of which, as we shall see, merging operators are extensions), that is, the *principle of irrelevance of syntax*, which says that the result of a merging operator depends only on the semantical content of the merged bases and not on their syntactical expression. (IC4) is known as the *fairness postulate* because it states that when merging two belief bases $K_1$ and $K_{2}$, no priority should be given to one of them. The merging is consistent with one of them if and only if it is consistent with the other. This postulate expresses a symmetric condition that operators that give priority to one of the two bases will not satisfy. (IC5) and (IC6) were first introduced in (Revesz 1997)[^revesz-1997] and together they mean that if two groups agree on at least one item, then the result of the fusion will coincide with those items on which the two groups agreed on. So, if the group of co-owners can be split in two parties, such that one wants to build the tennis court and the swimming pool and the other wants the swimming pool and the parking, the building of the swimming pool will be selected as the final group decision. Finally, (IC7) and (IC8) guarantee that if the conjunction between the merging on $E$ under $\IC_1$ and $\IC_{2}$ is consistent, then $\IC_1$ will remain satisfied if $E$ is merged under a more restrictive condition, that is, the conjunction of $\IC_1$ and $\IC_{2}$. This is a natural requirement to impose as, less formally, (IC7) and (IC8) together state that if the swimming pool is chosen among the set of three alternatives, it will still be selected if we reduce the set of alternatives to the tennis court and swimming pool. The last two postulates are a generalization of two postulates for revision (R5 and R6) in (Katsuno and Mendelzon 1991)[^katsuno-1991], who analyzed the revision operator from a model-theoretic point of view and gave a characterization of revision operators satisfying the AGM rationality postulates (Alchourrón et al. 1985)[^alchourrón-1985] in terms of minimal change with respect to an ordering over interpretations. Like Katsuno and Mendelzon’s postulates, (IC7) and (IC8) ensure that the notion of closeness is well behaved, in the sense that if an outcome is selected by the merging operator under $\IC_1$, then that outcome will also be the closest (i.e., it will be selected) to $\IC_{2}$ within the more restrictive constraint $\IC_1 \land \IC_{2}$ (assuming $\Delta_{\IC_1}(E) \land \IC_{2}$ to be consistent). In Katsuno and Mendelzon model-theoretic approach, revision operators change the initial belief base by choosing the closest interpretation in the new information. Similarly, *IC* merging operators select the closest interpretation in the integrity constraints to the set of belief bases. Hence, belief merging can be interpreted as a generalization of belief revision to multiple belief bases (Grégoire and Konieczny 2006)[^grégoire-2006].

Two sub-classes of $\IC$ fusion operators are defined. An *IC majority fusion* operator minimizes the level of total dissatisfaction (as introduced by Lin and Mendelzon 1996)[^lin-1996][^lin-1996-2], whereas an *IC arbitration operator* aims at equally distributing the level of individual dissatisfaction among the agents. The majority operator is similar in spirit to the utilitarian approach in social choice theory, whereas the arbitration is inspired to egalitarianism.

Let, for every integer $n$, $E^n$ denote the multi-set containing *n* times *E*. An *IC majority* operator satisfies the following additional postulate:

**(Maj)**

$\exists n \Delta_{\IC} (E_1\sqcup E^{n}_{2}) \models\Delta_{\IC}(E_{2})$

Thus, (Maj) states that enough repetitions of $E_{2}$ will make $E_{2}$ the opinion of the group. The number of repetitions needed depends on the specific instance.

An *IC arbitration* operator is characterized by the following postulate, in addition to (IC0)–(IC8):

**(Arb)**

Let IC1 and IC2 be logically independent. If $$\begin{align} \Delta_{\IC_1}(K_1) &\equiv \Delta_{\IC_2}(K_{2}), \textrm{ and}\\ \Delta_{\IC_{1} \leftrightarrow \neg \IC_{2}} (\{K_1, K_{2}\}) &\equiv (\IC_1\leftrightarrow \neg \IC_{2}), \textrm{ then} \\ \Delta_{\IC_{1}\lor \IC_{2}} (\{K_1, K_{2}\}) &\equiv \Delta_{\IC_1}(K_1).\end{align}$$

Intuitively, this axiom states that the arbitration operator selects the median outcomes that are *IC*-consistent. The behavior of such operator will be clearer when expressed in a model-theoretical way, as we shall see in the next section.

An example can help to appreciate the different behavior of a majority and an arbitration operator. Suppose three friends need to decide whether to buy a birthday present for a common acquaintance. Suppose now that two of them want to buy her a book and invite her out for dinner, while the third friend does not want to contribute to either of those presents. If the group takes its decision by majority, the three friends would resolve to buy a book and to invite her out for dinner, making the third friend very unhappy. If, on the other hand, they use an arbitration operator, they would either buy her a book or invite her out to a restaurant, making the three members equally dissatisfied. Everyone has exactly one formula in their belief base that is not being satisfied, so the “amount” of dissatisfaction for each friend is the same.

The fusion operators in the literature can be divided into two classes: *syntax-based* fusion and *model-based* fusion. The first type takes the propositional formulas as the information input, and typically considers the maximally consistent subsets of the belief profile. In a model-based operator, on the other hand, it is the interpretations of the formulas that are considered as inputs to the merging process. Hence, each belief base is seen as a set of models and the syntactic representation of its formulas is irrelevant. Recall the example we used at the beginning of Section 2 to illustrate that the combination of belief bases is syntax-dependent. We had $K_1 = \{a, b\}$, $K_2 = \{a \wedge b\}$ and $K_3 = \{\neg b\}$. A syntax-based fusion would treat $a, b, a \wedge b, \neg b$ as inputs, whereas a model-based fusion would take $mod(K_1) = mod(K_2) = \{(1, 1)\}$ and $mod(K_3) = \{(1,0), (0,0)\}$. Since model-based operators have been applied to the problem of judgment aggregation, we will focus on that class of merging operators and refer to (Baral et al. 1992; Konieczny 2000; Grégoire and Konieczny 2006)[^baral-1992][^grégoire-2006][^konieczny-2000] for more on syntax-based fusion.

### 2.2 The distance-based approach

An *IC* model-based fusion operator selects, among the models of the integrity constraints *IC*, those that are preferred, where the preference relation depends on the operator that is used. Thus, the collective belief set $\Delta_{\IC}(E)$ is guaranteed to be a set of formulas that are true in all of the selected models and to satisfy the *IC*. In the example of the city council seen earlier, this means that building a playground and a parking lot will never be selected as a decision outcome. The preference information usually takes the form of a total pre-order (to recall, a pre-order is a reflexive and transitive relation) $\le$ on the interpretations induced by a notion of distance *d* between an interpretation $\omega$ and the profile *E*, denoted by $d(\omega,E)$. Intuitively, this is to select a collective outcome that is the closest (with respect to some notion of distance to be specified) to all individual belief bases while satisfying the integrity constraints. It should be noted that a distance-based fusion operator does not always guarantee a unique result. We will come back to this point when we look at the application of belief merging to judgment aggregation.

We have seen that majority operators are characterized by trying to minimize the total dissatisfaction, whereas the arbitration operators aim at minimizing the local dissatisfaction. We can thus see the distance as a way to capture the notion of dissatisfaction. Inspired by the *economy principle* employed in belief revision, the outcome in merging should keep as much as information as possible from *each* individual belief base $K_i$. In other words, since the sources of information are assumed to be equally reliable, the merge should delete as little as possible from the sources. The idea then is to select the interpretations that minimize the distance between the models of *IC* and the models of the belief profile *E*. Formally, this can be expressed as follows:

$$ \mymod(\Delta_{\IC}(E)) = \mymin (\mymod (\IC), \le_{d}) $$

A distance *d* between interpretations is a total function $d: W \times W \rightarrow R^{+}$ such that for all $\omega, \omega'\in W$:

1. $d(\omega ,\omega') = d(\omega',\omega )$
2. $d(\omega ,\omega') = 0 \textrm{ iff } \omega =\omega'$.

The first point states that the distance is symmetric. Suppose there are three belief bases: $K_1 = K_3 = \{a, b, \neg c, d\}$ and $K_2 = \{\neg a, b, c, d\}$. If we denote by $\omega_i$ the interpretation of $K_i$, we have $\omega_1 = \omega_3 = (1,1,0,1)$ and $\omega_2 = (0,1,1,1)$. The first point requires that $d(\omega_1 ,\omega_2) = d(\omega_2 ,\omega_1)$. The second point states that if two interpretations are identical, the distance is 0, so $d(\omega_1 ,\omega_3) = 0$.[^note-2]

Two steps are needed to find the models of *IC* that minimize the distances to the belief profile. In the first step, we calculate the distance between each interpretation satisfying *IC* (that is, each candidate merged base) and each individual belief base. The intuition here is to quantify how far each individual opinion is from each possible collective outcome (recall that the outcomes will be selected among the interpretations satisfying *IC*). In the second step, we need to aggregate all those individual distances to define the collective distance, that is, the distance of the belief profile to each model of *IC*. This amounts to quantify how far the group is from each possible outcome. Finally, the (possibly more than one) base that minimizes such distance is selected as an outcome.

For the first step, we need to define the distance between an interpretation $\omega$ and a belief base *K*. This is the minimal distance between $\omega$ and the models of *K*. Formally: $d(\omega, K) = \mymin_{\omega'\in \mymod(K)} d(\omega, \omega')$. If *K* has more than one model (e.g., $K_i = \{a \vee b\}$ has three models: $\{(0,1) (1,0), (1,1)\}$), $\omega'$ will be the closest to $\omega$.

We can now define the distance between an interpretation $\omega$ and a belief profile *E*, which is needed for the second step. We need an aggregation function $D: R^{+n} \rightarrow R^{+}$ that takes the distances between the models of *IC* and the belief bases $K_i$ calculated in the first step, and aggregate them into a collective distance. This is: $D(\omega, E) = D(d(\omega, K_1)$, $d(\omega, K_2)$, $\ldots$, $d(\omega, K_n))$. A total pre-order over the set *W* of all interpretations is thus obtained. The merging operator can now select all interpretations that minimize the distance to the profile *E*.

Technically, an aggregation function $D: R^{+n} \rightarrow R^{+}$ assigns a nonnegative real number to every n-ary tuple of nonnegative real numbers. For any $x_1,\ldots, x_{n}, x, y \in R^{+}, D$ satisfies the following properties:

1. if $x\ge y$, then $D(x_1,\ldots , x,\ldots , x_{n})\ge D(x_1,\ldots , y,\ldots , x_{n})$
2. $D(x_1,\ldots , x,\ldots , x_{n})=0$ if and only if $x_1=\ldots =x_{n}=0$
3. $D(x)=x$

The outcome of the merging operator clearly depends on the chosen distance functions *d* and *D*. Among the first proposals (Lin and Mendelzon 1999; Revesz 1993)[^lin-1999][^revesz-1993] it was to adopt the *Hamming distance* (defined below) for *d* and the *sum* or the *max* for *D* (denoted respectively $D_{\Sigma}$ and $D_{\mymax}$).[^note-3] When *D* is the sum, the global distance is obtained by summing the individual ones. The corresponding merging operator is a majority operator and is called *minisum* as it will select those interpretations that minimize the sum. The merging operator that uses $D_{\mymax}$ is known as *minimax* and outputs the judgment set that minimizes the maximal distance to the individual bases (Brams et al. 2007b)[^brams-2007b]. Intuitively, *minimax* aims at minimizing the disagreement with the most dissatisfied individual. Two opposite outcomes may be selected when $D_{\Sigma}$ or $D_{\mymax}$ is used (Brams et al. 2007b; Eckert and Klamler 2007)[^brams-2007b][^eckert-2007].

The Hamming distance was a commonly used distance in belief revision. The idea is simple. The Hamming distance counts the number of propositional letters on which two interpretations differ. So, for example, if $\omega = (1, 0, 0)$ and $\omega' = (0, 1, 0)$, we have that $d(\omega, \omega') = 2$ as the two interpretations differ on the assignment to the first and the second propositions. Also well known is the *drastic distance*, which assigns distance 0 if two interpretations are the same and 1 otherwise. But the choice of the distance is not restricted to those options. Other distances can be used, that still satisfy the postulates given above (Konieczny and Pino Pérez 1999, 2002)[^konieczny-1999]. The minimization of the sum of the individual distances is an example of an *IC* majority merging operator. In the next section, we will see this operator applied to the discursive dilemma.

The distance-based approach can clarify the distinction between arbitration and majority operators. *Leximax* is an example of arbitration operator. A *leximax* operator may take *d* as the Hamming distance and, for each interpretation, the distances between that interpretation and the *n* bases $K_i$ form a list. A pre-order over interpretations is defined by taking the lexicographical order between sequences of distances, fixing an order over the set of agents. Finally, $D_{\textit{leximax}}$ selects the minimum. The intuition is that, unlike a majority operator that selects the option that minimizes the *total* disagreement (by minimizing the sum of the individual distances, for example), an arbitration operator looks at the *distribution* of such disagreement and selects the option that is fairer to all individuals, that is, it aims at equally distributing the individual dissatisfaction with the chosen outcome (recall the birthday gift example above). This follows from the definition of the Hamming distance: the larger the Hamming distance, the more disagreement there is between two interpretations (here disagreement simply means that the interpretations assign different truth values to the same formula). Suppose that a belief profile *E* has three bases. Suppose as well that the distances from the two models of *IC* ($\omega$ and $\omega'$) are $D_{\Sigma} (\omega, E) = D_{\Sigma} (\omega', E) = 6$ when we take the sum of the Hamming distances, and $D_{\textit{leximax}}(\omega, E)= (2,2,2)$ and $D_{\textit{leximax}}(\omega', E)= (5,1,0)$ when we take the lexicographic order on the distances. In this example, the majority operator cannot distinguish between $\omega$ and $\omega'$ (because in both cases the sum is 6), while the arbitration operator will prefer $\omega$ to $\omega'$ as $\omega$ distributes the individual disagreement in a fairer way than $\omega'$.

As mentioned earlier, Liberatore and Schaerf were among the first to propose arbitration operators. However, their approach was limited to only two bases, and the result of the merge was one of the two bases. Such operator would give questionable results in some situations, like the one in (Konieczny and Pino Pérez 2002)[^konieczny-2002]. Suppose that two financial experts give you advice regarding four shares *a, b, c* and *d*. According to the first expert, all four shares are going to rise (denoted by $\varphi_1= \{(1, 1, 1, 1)\}$, whereas the second expert deems that all four shares will fall $(\varphi_{2}= \{(0, 0, 0, 0)\})$. According to Liberatore and Schaerf’s arbitration operator, the result will be $\{(1, 1, 1, 1), (0, 0, 0, 0)\},$ which means that either the first or the second expert is totally right. If, on the other hand, we apply an arbitration operator *à la* Konieczny and Pino Pérez, we obtain $\{(0, 0, 1, 1)$, $(0, 1, 0, 1)$, $(0, 1, 1, 0)$, $(1, 0, 0, 1)$, $(1, 0, 1, 0)$, $(1, 1, 0, 0)\}$. This result can be interpreted as that—if we assume that all sources are equally reliable—we do not have any reason to prefer one or another and, so a reasonable position is to conclude that both can be equally right. Still, Liberatore and Schaerf’s operator may be used in all situations where the result can be only one of the bases submitted by the individuals. For example, if two doctors meet in order to decide a patient’s therapy, they likely have to decide in favour of one of the two proposals as mixing therapies may not be a feasible nor a safe option.

A representation theorem (Konieczny and Pino Pérez 1999, 2002)[^konieczny-1999] ensures that to each sub-class of *IC* merging operators (majority and arbitration operators) corresponds a family of pre-orders on interpretations (mirroring a similar representation theorem that Katsuno and Mendelzon (1991) proved for belief revision operators).[^note-4]

Let us now illustrate how belief merging can be applied to judgment aggregation problems.

## 3. Belief merging applied to the discursive dilemma

The merging of individual belief bases into a collective one shares similarities to the judgment aggregation problem. In both cases, we wish to aggregate individual inputs into a group outcome, and both disciplines employ logic to formalize the bases’ contents. As we have seen in Section 1, no aggregation procedure can ensure a consistent and complete group judgment. However, the merging operators introduced in computer science ensure a consistent outcome because such operators do not satisfy independence. The collective judgment on a proposition is not only determined by the individual judgments on that proposition but also by considerations of *all* other agenda’s items. It is natural to apply the results about merging methods to the aggregation of individual judgments (Pigozzi 2006)[^pigozzi-2006].

How do impossibility results in judgment aggregation conciliate with the fact that *IC* merging operators can ensure a consistent collective outcome? The reason is that merging operators violate the independence conditions, one of the requirements imposed on aggregation functions in the impossibility theorems. Independence turned out to be an instrumentally attractive condition because it protects an aggregation function from strategic manipulation (Dietrich 2006; Dietrich and List 2007b)[^dietrich-2006][^dietrich-2007b]. This means that an individual has no interest in submitting an insincere judgment set in order to get a better outcome for her. However, independence has been criticized in the literature as a not suitable *desideratum* to aggregate propositions that are logically interconnected (Chapman 2002; Mongin 2008)[^chapman-2002][^mongin-2008]. Clearly, paradoxical results are avoided by resorting to *IC*, which blocks unacceptable outcome. However, it is worth noting that in judgment aggregation the collective rationality condition (that requires logically consistent outputs) plays an analogous role as *IC* in belief merging, that is, blocks unacceptable outcomes like inconsistent majority judgments. Moreover, judgment aggregation impossibility results persist even if we explicitly import additional integrity constraints into the judgment aggregation framework (see Dietrich and List 2008b; Grandi 2012)[^dietrich-2008b][^grandi-2012].

It has been observed (Brams et al. 2007a)[^brams-2007a] that majority voting minimizes the sum of Hamming distances. This means that, whenever proposition-wise majority voting selects a consistent judgment set, the same outcome is selected by the *minisum* rule. Majority voting has credentials for being democratic. Another reason to focus on majority distance-based procedures is that the aim of the aggregation of individual judgments should be the right decision rather than a fair distribution of individual dissatisfactions. The epistemic link between majority voting and right decisions has been pointed out in the *Condorcet Jury Theorem*. The theorem shows that, when the voters are independent and have an equal probability of being right better than random, then majority rule ensures to select the right decision and the probability for doing so approaches 1 as the voters’ group size increases (see List 2013 for this and some more formal arguments for majority rule)[^list-2013].

Let us consider the three judges example and see what we obtain when applying the *minisum* rule. The legal doctrine corresponds to $\IC= \{(p\land q) \leftrightarrow r\}$. The court is represented by the profile $E=\{K_1 , K_{2} , K_{3}\}$, which is the multi-set containing the judgment sets $K_1 , K_{2} , K_3$ of the three judges. The three judgment sets and their corresponding models are:

\begin{align} K_1 &= \{p, q, r\} \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \mymod(K_1) &= \{(1, 1, 1)\};\\ K_{2} &= \{p, \neg q, \neg r\} \ \ \ \ \ \ \ \ \ \ \ \ \mymod(K_{2}) &= \{(1, 0, 0)\};\\ K_{3} &= \{\neg p, q, \neg r\} \ \ \ \ \ \ \ \ \ \ \ \ \mymod(K_{3}) &= \{(0, 1, 0)\}.\\ \end{align}

Table 2 shows the result for the majority operator that minimizes the sum of the Hamming distances. In the first column are all the interpretations for the propositional variables *p*, *q*, and *r*. The interpretations that are not models of the *IC* have a shaded background. So, for example, $(1,0,1)$ cannot be selected as the collective outcome because it violates the legal doctrine. The numbers in the $d_H (\cdot,K_1)$, $d_H(\cdot,K_{2})$, and $d_H(\cdot,K_{3})$ columns are the Hamming distances of each $K_i$ from the corresponding interpretation. In the last column are the sums of the Hamming distances.

*Table 2*

|   | $d_{H}(\cdot,K_{1})$ | $d_{H}(\cdot,K_{2})$ | $d_{H}(\cdot,K_{3})$ | $\Sigma(d_{H} (\cdot,E))$ |
| --- | --- | --- | --- | --- |
| $(1,1,1)$ | 0 | 2 | 2 | 4 |
| $(1,1,0)$ | 1 | 1 | 1 | 3 |
| $(1,0,1)$ | 1 | 3 | 1 | 5 |
| $(1,0,0)$ | 2 | 2 | 0 | 4 |
| $(0,1,1)$ | 1 | 1 | 3 | 5 |
| $(0,1,0)$ | 2 | 0 | 2 | 4 |
| $(0,0,1)$ | 2 | 2 | 2 | 6 |
| $(0,0,0)$ | 3 | 1 | 1 | 5 |

Table 2

We see that, without *IC*, the distance-based majority operator would select the same (inconsistent) outcome as proposition-wise majority voting, that is, $(1,1,0)$. This is the outcome that is at the minimum distance from *E*. However, the merging operator cannot select $(1,1,0)$ as that outcome violates the IC. Neglecting the shaded rows, only four interpretations are candidates to be selected as collective judgment sets, that is, $(1,1,1)$, $(1,0,0)$, $(0,1,0)$, and $(0,0,0)$. Of those, three are the ones that minimize the distances. Thus, collective inconsistency is avoided when a distance-based aggregation is used. However, this method does not always guarantee a unique outcome. In the court example, this aggregation selects the three models $(1,1,1)$, $(1,0,0)$ and $(0,1,0)$ as group positions. Technically, this is said to be an *irresolute* procedure, and a tie-breaking rule needs to be combined if we wish to ensure a unique result (as common in social choice theory).

The applicability of merging techniques developed in computer science to judgment aggregation problems does not mean that the two disciplines have the same objectives. As we have seen, the original motivation of belief merging was to define ways to aggregate information coming from different sources. Since the sources can have different access to the information, no externally given agenda is assumed. This is a difference with the judgment aggregation framework, where individuals are required to submit their opinion on a given set of items. Belief merging and judgment aggregation do not only differ in the type of inputs they aggregate. They also output different results: a collective base satisfying some given integrity constraints for belief merging, and a collective judgment on the given agenda for judgment aggregation.

Another difference resides in the fact that judgment aggregation assumes that all members are rational, and so they all submit consistent judgment sets. In belief merging, this is not required. Agents can submit belief bases that are inconsistent with the *IC* (Grégoire 2004)[^grégoire-2004]. If an individual submits a judgment that violates an integrity constraint, that judgment set will not figure among the candidates to represent the group position. However, his input will not be disregarded and will be taken into account in the merging process. The possibility to abstain from expressing an opinion on a certain item is also easily taken into account in a belief merging setting. If individuals need to have their say on *p*, *q* and *r* and one agent believes *q* and *r* to be true but does not have a clear opinion on *p*, this will be represented as $\mymod(K_1)= \{(1, 1, 1),$ $(0, 1, 1)\}$ and the distances calculated accordingly. The completeness requirement on judgment sets has also been weakened in the judgment aggregation framework. List and Pettit (2002) first discussed the weakening of completeness in the context of supermajority and unanimity rules. Later, it was shown (Gärdenfors 2006; Dokow and Holzman 2010)[^dokow-2010][^gärdenfors-2006] that, when judgment sets are not assumed to be complete, any independent and unanimous aggregation function turns out to be weakly oligarchic, that is, a subset of the individuals will decide the collective outcome. Intuitively, this is a less negative result than dictatorship, though it reduces to dictatorship in the case in which only one individual belongs to that subset. Dietrich and List (2008a) independently obtained equivalent results on oligarchic rules to those in (Dokow and Holzman 2010)[^dokow-2010].

Finally, if model-based merging approach is syntax-dependent, judgment aggregation explicitly permits syntax-dependence. This can give rise to decision framing problems (Cariani et al. 2008)[^cariani-2008] or logical agenda manipulation (Dietrich 2006)[^dietrich-2006] when a judgment problem can be presented using two logically equivalent but syntactically different agendas.

A formal investigation of the relationships between belief merging and judgment aggregation can be found in (Everaere et al. 2015, 2017)[^everaere-2015]. As we have seen, belief merging takes a profile of propositional belief bases as input, where such bases represent the beliefs of a certain individual, not restraint to a given agenda. Judgment aggregation, on the other hand, asks people to submit their judgments on a specific set of issues. The analysis rests on the assumption that an individual’s beliefs allow deriving her opinion on the agenda’s items. Thus, in (Everaere et al. 2015)[^everaere-2015] a *projection function p* (assumed to be identical for all the individuals) is defined. The role of such projection function is precisely to determine the judgments of an agent (input of judgment aggregation operators) starting from her beliefs (input of belief merging). So, for example, if an individual only believes $a\land b$ and one of the agenda items is *a*, then the projection function can derive that the person submits a “yes” as judgment on *a*. However, if she believes only *a* and one of the agenda item is $a\land b$, she will probably be not able to submit a judgment on that item. For this reason, individual judgment sets in (Everaere et al. 2015)[^everaere-2015] are not necessarily complete (individuals can abstain on some agenda’s issues). Using the projection *p*, two paths along which a collective judgment can be derived from a profile of belief bases are considered. Along one path (merge-then-project), the individual belief bases are first merged using a merging operator and then the collective judgment is computed by the projection *p*. Along the other path (project-then-aggregate), starting from the individual bases, the individual judgment sets are first computed by *p* and then aggregated using a judgment aggregation procedure to determine the collective judgment on the given agenda. Thus, the question addressed is whether the two collective judgments obtained by following the two paths coincide. Two cases are considered: the general case (incomplete agendas) and the case in which the agenda is complete (i.e. it contains all possible interpretations). For example, the agenda $A= \{\neg a \land \neg b, \neg a \land b, a \land \neg b, a \land b\}$ is complete whereas the agenda $A= \{\neg a \land \neg b, \neg a \land b, a \land \neg b\}$ is not. Hence, if an individual believes $a\land b$, her judgment set will be $(0,0,0,1)$ in the first agenda and $(0,0,0)$ in the second one, which may lead to different collective outcomes depending on whether the merge-then-project or the project-then-merge path is used. The fact that by properly choosing the agenda one may manipulate the result has been investigated in the judgment aggregation literature (Dietrich 2016, Lang et al. 2016)[^dietrich-2016][^lang-2016]. In the general case, IC merging methods can give results that are inconsistent with those obtained by using judgment aggregation operators satisfying unanimity or majority preservation[^note-5]. On a more positive side, when the agenda is complete, the collective judgments obtained by following the two paths coincide for some judgment aggregation operators satisfying properties closed to some IC merging postulates.

Recently, distance-based operators have been applied to a new problem of judgment aggregation: dynamically rational judgment aggregation. Traditionally, judgment aggregation focuses on static aggregation: individuals submit their judgments, and those are aggregated using some procedure. However, in more realistic contexts, new information may become available at any time. How to aggregate judgments in the light of new information? Dietrich and List explore whether collective judgments can be dynamically rational, meaning that they change rationally in response to new information (Dietrich and List 2024)[^dietrich-2024]. A judgment aggregation rule is said to be dynamically rational with respect to a revision operator if individually revising the judgments in light of some information and then aggregating them leads to the same result as revising the old collective judgment with the new information. Distance-based revision operators, for instance, allow one to minimally change a judgment while consistently including the new information. Thus, they are rationality-preserving. Dietrich and List investigate the conditions under which judgment aggregation rules and revision operators can achieve dynamic rationality, highlighting the challenges and an impossibility theorem associated with it. Possible escape routes (obtained by relaxing the conditions on the aggregation rule or the revision operator) to the impossibility result are also examined.

### 3.1 Extensions and criticisms

The *minisum* rule applied to merge the judgment sets of the three judges in the previous section is based on the same principles as the *Kemeny rule*, a well-known preference aggregation rule (Kemeny 1959)[^kemeny-1959]. Unlike what happened in social choice, at the beginning the literature of judgment aggregation focused on the axiomatic method and only few concrete aggregation rules were proposed and studied. Arguably, the interest of researchers from computer science and multi-agent systems for judgment aggregation lead to the definition of more concrete aggregation rules and to the investigation of their relations. The same idea of minimization that plays such a crucial role in belief merging can be found as a principle in the definition of several voting rules in social choice theory. For instance, the *minisum* rule turned out to be equivalent to several other rules recently introduced in the judgment aggregation literature (Lang et al. 2017)[^lang-2017].

The interest of computer scientists for aggregation methods is witnessed by the fact that judgment aggregation is now among the topics of computational social choice, an interdisciplinary discipline that promotes exchanges and interactions between computer science and social choice theory. Computational issues of aggregation rules are among the interests of computational social choice. The intuition behind the application of complexity theory to aggregation rules is to assess the acceptability of an aggregation rule on the basis of pragmatic considerations, that is, the algorithmic feasibility of applying that rule. So, an aggregation rule is acceptable when its outcome is ‘easy’ to compute, that is, it can be solved by an algorithm in time which grows – at worst – polynomially with the size of the input (only in some pathological cases we can imagine desiring a rule that will not be able to return an outcome in a foreseeable future). On the other hand, if an aggregation rule is manipulable, then it is acceptable when it is ‘hard’ for an individual to manipulate it. Thus, the study of the computational complexity of aggregation rules may reveal that, even though a rule is manipulable, it is actually hard for an individual to act on that. The computational complexity of the distance-based procedures has been studied (Endriss et al. 2012; Endriss and de Haan 2015)[^endriss-2015][^endriss-2012]. The high computational complexity of Hamming rule in judgment aggregation mirrors a parallel result that the Kemeny rule in preference aggregation is also highly computational complex, as first shown in Bartholdi et al. (1989) and Hudry (1989). A new rule has been proposed to overcome the high computational complexity of distance-based procedures. The average-voter rule (Grandi 2012)[^grandi-2012] selects the judgment set submitted by the individuals that minimizes the sum of the distances. Hence, the outcome has to be one of the submitted judgment sets. This allows reducing the computational complexity and, at the same time, selects the most representative individual.

A generalization of distance-based methods for judgment aggregation has been given in (Miller and Osherson 2009)[^miller-2009]. Besides generalizing (by taking a general metric) the merging operator we have applied to the doctrinal paradox, they proposed three other distance-based procedures for judgment aggregation. In case proposition-wise majority collapses into an inconsistent collective judgment set, one method (*Endpoint*) selects as group outcome the closest (according to some distance metric) consistent collective judgment set. The other two methods (*Full* and *Output*) look at minimal ways to change the profile in order to output a consistent proposition-wise majority collective judgment set. The difference is that *Output* allows the individual judgment sets in the modified profile to be inconsistent.

Duddy and Piggins (2012) questioned the use of Hamming distance between judgment sets. The problem is that, when the agenda contains propositions that are logically connected, the Hamming distance may be responsible of double counting because it ignores such interdependencies. Suppose, for example, that two individuals accept propositions *q* but disagree on $p\land q$ (so, one individual accepts the conjunction, while the other rejects it). This can happen only if they disagree on *p*. The Hamming distance between the two judgment sets $K_1 = \{\neg p, q, \neg(p\land q)\}$ and $K_{2} = \{p, q, (p\land q)\}$ is 2. It is the disagreement on *p* that implies the disagreement over $p\land q$, so the distance should be just 1. The alternative distance proposed in order to address this problem is a distance that takes the smallest number of logically coherent changes needed to convert one judgment set into the other.

## 4. Other topics

Belief merging is an abstract theory that addresses the problem of aggregating symbolic inputs, without specifying whether such items are beliefs, knowledge, desires, norms etc. It is the choice of the merging operator that should best suit the type of inputs. The framework of judgment aggregation has also been extended to include the aggregation of other types of attitudes, as in (Dietrich and List 2010)[^dietrich-2010].

The literature on belief merging includes the study of the strategic manipulation problem (Evaraere et al. 2007). When an aggregation procedure is not strategy-proof, an individual who has a preference over the possible outcomes can manipulate the result by lying on her true beliefs and thus obtain an outcome closer to her true preferences. In general, merging operators are not strategy-proof when Hamming distance is used, whereas they are strategy-proof when the drastic distance is employed. For a recent survey of results on strategic behaviour in judgment aggregation, see (Baumeister et al. 2017)[^baumeister-2017].

In those situations in which we can assume that there is a fact of the matter (for example, a defendant has—or has not—committed a murder), which each agent has a (noisy) opinion about, the truth-tracking properties of belief merging operators can be investigated (Hartmann et al. 2010; Hartmann and Sprenger 2012; Cevolani 2014)[^cevolani-2014][^hartmann-2010][^hartmann-2012]. The question is then whether a certain aggregation method selects the right decision. Williamson (2009) argues that aggregating the *evidence* on which the judgments are based is best for judgment aggregation, as it would yield to the right decision. The three-step proposal he advocates distinguishes between three types of propositions: evidence, beliefs and judgments. Evidence is the support for an agent’s beliefs and judgments, and it is the right candidate for merging techniques. Judgments, on the other hand, are best dealt with decision theory that maps degrees of beliefs and utilities to judgments.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=belief-merging). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/belief-merging/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=belief-merging&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/belief-merging/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

[Please contact the author with suggestions.]

## Related Entries

Arrow’s theorem | epistemology: social | jury theorems | logic: of belief revision | social choice theory | social procedures, formal approaches

### Acknowledgments

I am indebted to Eric Pacuit and to an anonymous reviewer of the updated entry, who provided many valuable comments and suggestions that greatly improved the content and readability of this entry, and to Erman Acar who pointed out some typos in the previous version.

## Notes（原文脚注）

[^note-1]: The set *At* of atomic propositions is assumed to be ordered, i.e., an order such that *p* comes before *q* and *q* comes before *r*. Thus $(1,0,0)$ represents an interpretation that assigns true to *p* and false to *q* and *r*.

[^note-2]: Technically, *d* is a pseudo-distance as the triangular inequality $(\forall \omega, \omega', \omega'' \in W$, $d(\omega, \omega') \le d(\omega, \omega'') + d(\omega'', \omega'))$ is not required to hold. Konieczny and Pino Pérez (2002) showed that, if *d* satisfies the triangular inequality, then $D_{\Sigma}$ satisfies the *iteration* axiom:

**($\IC_{\textit{It}}$)**

If $\varphi \vdash \IC$ then $\exists n \Delta_{\IC}^{n} (E,\varphi) \vdash\varphi$

[^note-3]: Similarly as the *minimax* rules in decision theory, the *max* operators aims at selecting the outcome that minimizes the worst disagreement. Such operators do not satisfy all the postulates for merging, and hence are called *quasi-merging* operators (Konieczny and Pino Pérez 2002)[^konieczny-2002].

[^note-4]: Belief revision and belief merging have deep connections. In particular, merging operators can be seen as a generalization of revision operators (Konieczny and Pino Pérez 2002)[^konieczny-2002]. More precisely, if $\Delta$ is an *IC* merging operator, then the operator $*$ defined as $\varphi * \IC= \Delta_{\IC}(\varphi)$ is an AGM revision operator (Alchourrón *et al.* 1985)[^alchourrón-1985]. The other direction (whether an AGM revision operator defines an *IC* merging operator) has a more complex answer, which can be summarized by saying that a revision operator can define a merging *IC* operator if and only if the revision operator is defined in terms of distances.

[^note-5]: The majority preservation property ensures that, if the proposition-wise majority vote is a consistent judgment set, the judgment aggreegation procedures must select that same judgment set (Lang et al. 2017)[^lang-2017].

[^alchourrón-1985]: Alchourrón, C.E., P. Gärdenfors, and D. Makinson, 1985, “On the Logic of Theory Change: Partial Meet Functions for Contraction and Revision”, *Journal of Symbolic Logic*, 50: 510–530.

[^arrow-1951]: Arrow, K., 1951/1963, *Social Choice and Individual Values*, New York: Wiley.

[^baral-1991]: Baral, C., S. Kraus, and J. Minker, 1991, “Combining Multiple Knowledge Bases”, *IEEE Transactions on Knowledge and Data Engineering*, 3(2): 208–220.

[^baral-1992]: Baral, C., S. Kraus, J. Minker, and V. Subrahmanian, 1992, “Combining Multiple Knowledge Bases Consisting of First Order Theories”, *Computational Intelligence*, 8(1): 45–71.

[^bartholdi-1989]: Bartholdi, J., C. Tovey, and M. Trick, 1989, “The Computational Difficulty of Manipulating an Election”, *Social Choice and Welfare*, 6: 227–241.

[^baumeister-2017]: Baumeister, D., J. Rothe, and A.K. Selker, 2017, “Strategic Behavior in Judgment Aggregation”, in U. Endriss (ed.), *Trends in Computational Social Choice*, AI Access, pp. 145–168.

[^benferhat-1998]: Benferhat, S., D. Dubois, J. Lang, H. Prade, A. Saffiotti, and P. Smets, 1998, “A General Approach for Inconsistency Handling and Merging Information in Prioritized Knowledge Bases”, in *Proceedings of the Sixth International Conference on Principles of Knowledge Representation and Reasoning* (KR’98), San Francisco: Morgan Kaufmann, pp. 466–477.

[^black-1948]: Black, D., 1948, “On the Rationale of Group Decision Making”, *The Journal of Political Economy*, 56: 23–34.

[^bloch-2001]: Bloch, I., A. Hunter, A. Ayoun, S. Benferhat, P. Besnard, L. Cholvy, R. Cooke, D. Dubois and H. Fargier, 2001, “Fusion: general concepts and characteristics”, *International Journal of Intelligent Systems*, 16: 1107–1134.

[^borgida-1984]: Borgida, A. and T. Imielinski, 1984, “Decision Making in Committees: A Framework for Dealing with Inconsistency and Non-Monotonicity”, in *Proceedings of the Workshop on Non-Monotonic Reasoning*, New Paltz, NY, pp. 21–32.

[^brams-2007a]: Brams, S.J., D.M. Kilgour, and M.R. Sanver, 2007a, “A Minimax Procedure for Negotiating Multilateral Treaties”, in R. Avenhaus and I. W. Zartman (eds.), *Diplomacy Games: Formal Models and International Negotiations*, Berlin: Springer, pp 265–282.

[^brams-2007b]: –––, 2007b, “A Minimax Procedure for Electing Committees”, *Public Choice*, 132: 401–420.

[^cariani-2008]: Cariani, F., M. Pauly, and J. Snyder, 2008, “Decision Framing in Judgment Aggregation”, *Synthese*, 163(1): 1–24.

[^cevolani-2014]: Cevolani, G., 2014, “Truth Approximation, Belief Merging and Peer Disagreement”, *Synthese*, 191(11): 2383–2401.

[^chapman-2002]: Chapman, B., 2002, “Rational Aggregation”, *Politics, Philosophy, Economics*, 1(3): 337–354.

[^chawathe-1994]: Chawathe, S., H. Garcia Molina, J. Hammer, K. Ireland, Y. Papakonstantinou, J. Ullman, and J. Widom, 1994, “The TSIMMIS Project: Integration of Heterogeneous Information Sources”, in *Proceedings of IPSJ Conference*, Tokyo: Information Processing Society of Japan, pp. 7–18.

[^cholvy-1998]: Cholvy, L., 1998, “Reasoning about Merged Information”, in D.M. Gabbay, and Ph. Smets (eds.), *Handbook of Defeasible Reasoning and Uncertainty Management Systems*, Vol. 3, Dordrecht: Kluwer Academic Publishers, pp. 233–263.

[^condorcet-1785]: Condorcet, N. de, 1785, *Essai sur l’Application de l’Analyse à la Probabilité des Décisions Rendues à la Pluralité des Voix*, Paris.

[^delgrande-2006]: Delgrande, J.P., D. Dubois, and J. Lang, 2006, “Iterated Revision as Prioritized Merging”, in *Proceedings of the 10ᵗʰ International Conference on Knowledge Representation and Reasoning* (KR’06), Menlo Park, CA: AAAI Press, pp. 210–220.

[^dietrich-2006]: Dietrich, F., 2006, “Judgment Aggregation: (Im)Possibility Theorems”, *Journal of Economic Theory*, 126: 286–298.

[^dietrich-2007]: –––, 2007, “A Generalised Model of Judgment Aggregation”, *Social Choice and Welfare*, 28(4): 529–565.

[^dietrich-2016]: –––, 2016, “Judgment Aggregation and Agenda Manipulation”, *Games and Economic Behavior*, 95: 113–136.

[^dietrich-2007a]: Dietrich, F. and C. List, 2007a, “Arrow’s Theorem in Judgment Aggregation”, *Social Choice and Welfare*, 29: 19–33.

[^dietrich-2007b]: –––, 2007b, “Strategy-proof Judgment Aggregation”, *Economics and Philosophy*, 23: 269–300.

[^dietrich-2008a]: –––, 2008a, “Judgment Aggregation Without Full Rationality”, *Social Choice and Welfare*, 31: 15–39.

[^dietrich-2008b]: –––, 2008b, “Judgment Aggregation Under Constraints”, in T. Boylan and R. Gekker, eds., *Economics, Rational Choice and Normative Philosophy*, Routledge, pp. 111–123.

[^dietrich-2010]: –––, 2010, “The Aggregation of Propositional Attitudes: Towards a General Theory”, in *Oxford Studies in Epistemology* (Volume 3), Oxford: Oxford University Press, pp. 215–234.

[^dietrich-2024]: –––, 2024, “Dynamically Rational Judgment Aggregation”, *Social Choice and Welfare*, 63: 531–580.

[^dokow-2010]: Dokow, E. and R. Holzman, 2010, “Aggregation of Binary Evaluations with Abstentions”, *Journal of Economic Theory*, 145(2): 544–561.

[^duddy-2012]: Duddy, C. and A. Piggins, 2012, “A Measure of Distance Between Judgment Sets”, *Social Choice and Welfare*, 39: 855–867.

[^eckert-2007]: Eckert, D. and C. Klamler, 2007, “How puzzling is judgment aggregation? Antipodality in distance-based aggregation rules”, Working paper, University of Graz.

[^elmagarmid-1999]: Elmagarmid, A., M. Rusinliewicz, and A. Sheth (eds.), 1999, *Management of Heterogeneous and Autonomous Database Systems*, San Francisco: Morgan Kaufmann.

[^elster-2013]: Elster, J., 2013, “Excessive Ambitions (II)”, *Capitalism and Society*, 8(1): Article 1 [[Elster 2013 available online](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2207111)]

[^endriss-2016]: Endriss, U., 2016, “Judgment Aggregation”, in F. Brandt, V. Conitzer, U. Endriss, J. Lang, A. Procaccia (eds.), *Handbook of Computational Social Choice*, Cambridge: Cambridge University Press, pp. 399–426.

[^endriss-2015]: Endriss, U. and R. de Haan, 2015, “Complexity of the Winner Determination Problem in Judgment Aggregation: Kemeny, Slater, Tideman, Young”, in *Proceedings of the 14th International Conference on Autonomous Agents and Multiagent Systems*, IFAAMAS, pp. 117–125.

[^endriss-2012]: Endriss, U., U. Grandi, and D. Porello, 2012, “Complexity of Judgment Aggregation”, *Journal of Artificial Intelligence Research*, 45: 481–514.

[^everaere-2007]: Everaere, P., S. Konieczny, and P. Marquis, 2007, “The Strategy-Proofness Landscape of Merging”, *Journal of Artificial Intelligence Research (JAIR)*, 28: 49–105.

[^everaere-2015]: –––, 2015, “Belief Merging versus Judgment Aggregation”, in *Proceedings of the 14th International Conference on Autonomous Agents and Multiagent Systems* (AAMAS 15), IFAAMAS, pp. 999–1007.

[^everaere-2017]: –––, 2017, “An Introduction to Belief Merging and its Links to Judgment Aggregation”, in U. Endriss (ed.), *Trends in Computational Social Choice*, AI Access Books, pp. 123–143.

[^fermé-2018]: Fermé, E. and S.O. Hansson, 2018, *Belief Change. Introduction and Overview*, Cham: Springer.

[^gärdenfors-1988]: Gärdenfors, P., 1988, *Knowledge in Flux: Modeling the Dynamics of Epistemic States*, Cambridge, MA: MIT Press.

[^gärdenfors-2006]: –––, 2006, “A Representation Theorem for Voting with Logical Consequences”, *Economics and Philosophy*, 22: 18–190.

[^gauwin-2005]: Gauwin, O., S. Konieczny, and P. Marquis, 2005, “Conciliation and Consensus in Iterated Belief Merging”, in *Proceedings of the 8th European Conference on Symbolic and Quantitative Approaches to Reasoning with Uncertainty*, Berlin: Springer, pp. 514–526.

[^ginsberg-1986]: Ginsberg, M., 1986, “Counterfactuals”, *Artificial Intelligence*, 30(1): 35–79.

[^goldman-1999]: Goldman, A., 1999, *Knowledge in a Social World*, Oxford: Oxford University Press.

[^goldman-2004]: –––, 2004, “Group Knowledge versus Group Rationality: Two Approaches to Social Epistemology”, *Episteme: A Journal of Social Epistemology*, 1(1): 11–22.

[^goldman-2010]: –––, 2010, “Social Epistemology”, *The Stanford Encyclopedia of Philosophy* (Summer 2010 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/sum2010/entries/epistemology-social/](https://plato.stanford.edu/archives/sum2010/entries/epistemology-social/)>.

[^grégoire-2004]: Grégoire, E., 2004, “Extension of a Distance-based Fusion Framework”, in *Proceedings of the 8th International Conference on Sensor Fusion: Architectures, Algorithms and Applications*, pp. 282–286.

[^grégoire-2006]: Grégoire, E. and S. Konieczny, 2006, “Logic-based Approaches to Information Fusion”, *Information Fusion*, 7: 4–18.

[^grandi-2012]: Grandi, U., 2012, *Binary Aggregation with Integrity Constraints*, Ph.D. thesis, ILLC, University of Amsterdam [[Grandi 2012 available online](https://www.illc.uva.nl/Research/Publications/Dissertations/DS-2012-08.text.pdf)].

[^grossi-2009]: Grossi, D., 2009, “Unifying Preference and Judgment Aggregation”, in *Proceedings of the 8th International Conference on Autonomous Agents and Multiagent Systems*, pp. 217–224.

[^grossi-2014]: Grossi, D. and G. Pigozzi, 2014, *Judgment Aggregation: A Primer*, San Rafael, CA: Morgan & Claypool.

[^hansson-2011]: Hansson, S.O., 2011, “Logic of Belief Revision”, *The Stanford Encyclopedia of Philosophy* (Fall 2011 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/fall2011/entries/logic-belief-revision/](https://plato.stanford.edu/archives/fall2011/entries/logic-belief-revision/)>.

[^hartmann-2010]: Hartmann, S., G. Pigozzi, and J. Sprenger, 2010, “Reliable Methods of Judgment Aggregation”, *Journal of Logic and Computation*, 20(2): 603–617.

[^hartmann-2012]: Hartmann, S. and J. Sprenger, 2012, “Judgment Aggregation and the Problem of Tracking the Truth”, *Synthese*, 187(1): 209–221.

[^hudry-1989]: Hudry, O., 1989, *Recherches d’Ordres Médians: Complexité, Algorithmique et Problèmes Combinatoires*, Ph.D. thesis, Telecom Paris Tech.

[^katsuno-1991]: Katsuno, H. and A.O. Mendelzon, 1991, “Propositional Knowledge Base Revision and Minimal Change”, *Artificial Intelligence*, 52: 263–294.

[^kemeny-1959]: Kemeny, J., 1959, “Mathematics without numbers”, *Daedalus*, 88: 577–591.

[^kim-1995]: Kim, W. (ed.), 1995, *Modern Database Systems: The Object Model, Interoperability and Beyond*, New York: Addison Wesley.

[^konieczny-2000]: Konieczny, S., 2000, “On the Difference between Merging Knowledge Bases and Combining them”, in A.G. Cohn, F. Giunchiglia, and B. Selman, (eds.), *KR2000: Principles of Knowledge Representation and Reasoning*, San Francisco: Morgan Kaufmann, pp. 135–144.

[^konieczny-1998]: Konieczny, S. and R. Pino Pérez, 1998, “On the Logic of Merging”, in *Proceedings of the 6th International Conference on Principles of Knowledge Representation and Reasoning*, San Francisco: Morgan Kaufmann, pp. 488–498.

[^konieczny-1999]: –––, 1999, “Merging with Integrity Constraints”, in *Proceedings of the 5th European Conference on Symbolic and Quantitative Approaches to Reasoning with Uncertainty* (ECSQARU ’99), LNAI 1638, pp. 233–244.

[^konieczny-2002]: –––, 2002, “Merging Information under Constraints: A Logical Framework”, *Journal of Logic and Computation*, 12: 773–808.

[^kornhauser-1992]: Kornhauser, L.A., 1992, “Modeling Collegial Courts. II. Legal Doctrine”, *Journal of Law, Economics, and Organization*, 8: 441–470.

[^kornhauser-1986]: Kornhauser, L.A. and L.G. Sager, 1986, “Unpacking the Court”, *Yale Law Journal*, 96: 82–117.

[^kornhauser-1993]: –––, 1993, “The One and the Many: Adjudication in Collegial Courts”, *California Law Review*, 81: 1–51.

[^kornhauser-2004]: –––, 2004, “The Many as One: Integrity and Group Choice in Paradoxical Cases”, *Philosophy & Public Affairs*, 32(3): 249–276.

[^kowalski-1978]: Kowalski, R., 1978, “Logic for data description”, in H.G.J. Minker (ed.), *Logic and data bases*, New York: Plenum, pp. 77–102.

[^lang-2016]: Lang, J., M. Slavkovik, and S. Vesic, 2016, “Agenda Separability in Judgment Aggregation”, in *Proceedings of the Thirtieth Conference on Artificial Intelligence*, Palo Alto: Association for the Advancement of Artificial Intelligence (AAAI), pp. 1016–1022.

[^lang-2017]: Lang, J., G. Pigozzi, M. Slavkovik, L. van der Torre, and S. Vesic, 2017, “A Partial Taxonomy of Judgment Aggregation Rules and their Properties”, *Social Choice and Welfare*, 48(2): 327–356.

[^liberatore-1995]: Liberatore, P. and M. Schaerf, 1995, “Arbitration: a Commutative Operator for Belief Revision”, in *Proceedings of the Second World Conference on the Fundamentals of Artificial Intelligence*, pp. 217–228, Paris: Angkor Press.

[^liberatore-1998]: –––, 1998, “Arbitration (or How to Merge Knowledge Bases)”, *IEEE Transactions on Knowledge and Data Engineering*, 10(1): 76–90.

[^lin-1995]: Lin, J., 1995, *Frameworks for Dealing with Conflicting Information and Applications*, Ph.D. thesis, University of Toronto.

[^lin-1996]: –––, 1996, “Integration of Weighted Knowledge Bases”, *Artificial Intelligence*, 83: 363–378.

[^lin-1996-2]: Lin, J. and A. Mendelzon, 1996, “Merging databases under constraints”, *International Journal of Cooperative Information Systems*, 7: 55–76.

[^lin-1999]: –––, 1999, “Knowledge Base Merging by Majority”, in *Dynamic Worlds: From the Frame Problem to Knowledge Management*, R. Pareschi and B. Fronhöfer (eds), Norwell, MA: Kluwer, pp. 195–218.

[^list-2002]: List, C., 2002, “A Possibility Theorem on Aggregation over Multiple Interconnected Propositions”, *Mathematical Social Sciences*, 45(1): 1–13.

[^list-2013]: –––, 2013, “Social Choice Theory”, *The Stanford Encyclopedia of Philosophy* (Winter 2013 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/win2013/entries/social-choice/](https://plato.stanford.edu/archives/win2013/entries/social-choice/)>.

[^list-2002-2]: List, C. and P. Pettit, 2002, “Aggregating sets of judgments: an impossibility result”, *Economics and Philosophy*, 18: 89–110.

[^list-2004]: –––, 2004, “Aggregating Sets of Judgments: Two Impossibility Results Compared”, *Synthese*, 140: 207–235.

[^list-2009]: List, C. and C. Puppe, 2009, “Judgment Aggregation: A Survey”, in P. Anand, C. Puppe, and P. Pattanaik (eds.), *The Handbook of Rational and Social Choice*, Oxford: Oxford University Press, pp. 457–482.

[^meyer-2001]: Meyer, T., A. Ghose, and S. Chopra, 2001, “Social Choice, Merging and Elections”, in *Proceedings of the 6th European Conference on Symbolic and Quantitative Approaches to Reasoning with Uncertainty*, Benferhat and Besnard (eds.), Vol. 2143 of *Lecture Notes in Artificial Intelligence*, Berlin: Springer, pp. 466–477.

[^miller-2009]: Miller, M.K. and D. Osherson, 2009, “Methods for Distance-based Judgment Aggregation”, *Social Choice and Welfare*, 32(4): 575–601.

[^mongin-2008]: Mongin, P., 2008, “Factoring Out the Impossibility of Logical Aggregation”, *Journal of Economic Theory*, 141: 100–113.

[^morreau-2014]: Morreau, M., 2014, “Arrow’s Theorem”, *The Stanford Encyclopedia of Philosophy* (Winter 2014 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/win2014/entries/arrows-theorem/](https://plato.stanford.edu/archives/win2014/entries/arrows-theorem/)>.

[^pauly-2006]: Pauly, M. and M. van Hees, 2006, “Logical Constraints on Judgment Aggregation”, *Journal of Philosophical Logic*, 35: 569–585.

[^pettit-2001]: Pettit, P., 2001, “Deliberative Democracy and the Discursive Dilemma”, *Philosophical Issues*, 11: 268–299.

[^pigozzi-2006]: Pigozzi, G., 2006, “Belief merging and the discursive dilemma: an argument-based account to paradoxes of judgment aggregation”, *Synthese*, 152: 285–298.

[^poisson-1837]: Poisson, S.D., 1837, *Recherches sur la probabilité des jugements en matière criminelle et en matière civile: précédées des règles générales du calcul des probabilités*, Paris.

[^porello-2017]: Porello, D., 2017, “Judgment Aggregation in Non-Classical Logics”, *Journal of Applied Non-Classical Logics*, 27(1–2): 106–139.

[^reiter-1988]: Reiter, R., 1988, “On Integrity Constraints”, in M.Y. Vardi (ed.), *Proceedings of the Second Conference on the Theoretical Aspects of Reasoning about Knowledge*, San Francisco: Morgan Kaufmann, pp. 97–111.

[^revesz-1993]: Revesz, P., 1993, “On the Semantics of Theory Change: Arbitration between Old and New Information”, in C. Beeri (ed.), *Proceedings of the Twelfth ACM Symposium on Principles of Database Systems*, Washington D.C., pp. 71–82.

[^revesz-1997]: –––, 1997, “On the Semantics of Arbitration”, *International Journal of Algebra and Computation*, 7(2): 133–160.

[^roth-2011]: Roth, A.S., 2011, “Shared Agency”, *The Stanford Encyclopedia of Philosophy* (Spring 2011 Edition), E.N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/spr2011/entries/shared-agency](https://plato.stanford.edu/archives/spr2011/entries/shared-agency)>.

[^sen-1970]: Sen, A.K., 1970, *Collective Choice and Social Welfare*, San Francisco: Holden-Day.

[^spector-2009]: Spector, H., 2009, “The Right to a Constitutional Jury”, *Legisprudence*, 3(1): 111–123.

[^subrahmanian-1994]: Subrahmanian, V.S., 1994, “Amalgamating Knowledge Bases”, *ACM Transactions on Database Systems*, 19(2): 291–331.

[^vacca-1921]: Vacca, R., 1921, “Opinioni Individuali e Deliberazioni Collettive”, *Rivista Internazionale di Filosofia del Diritto*, 52: 52–59.

[^willamson-2009]: Willamson, J., 2009, “Aggregating Judgments by Merging Evidence”, *Journal of Logic and Computation*, 19(3): 461–473.

[^xuefeng-2018]: Xuefeng, W., 2018, “Judgment Aggregation in Nonmonotonic Logic”, *Synthese*, 195(8): 3651–3683.
