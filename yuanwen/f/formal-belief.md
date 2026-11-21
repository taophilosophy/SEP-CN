# Formal Representations of Belief
**First published Wed Oct 22, 2008; substantive revision Fri Nov 13, 2020**

*Genin, Konstantin, Huber, Franz*

Epistemologists are interested in the norms governing the structure and dynamics of systems of belief: how an individual's beliefs must cohere in order to be considered rational; how they must be reflected in decision making; and how they ought to accommodate new evidence. Formal epistemologists pursue these questions by constructing mathematical models, or “formal representations,” of belief systems that are, in some sense, epistemically exemplary. Broadly speaking, these models capture something important about how an ideally rational agent would manage her epistemic life. This entry gives an overview of the formal representations that have been proposed for this purpose.

Belief comes in a qualitative (full) form, as when Sophia believes that Vienna is the capital of Austria, and a quantitative (partial) form, as when Sophia's belief that Vienna is the capital of Austria is stronger, in some sense, than her belief that Vienna is more populous than Budapest. The question of how full and partial belief are related has received considerable attention in formal epistemology, giving rise to several subtle, elegant and, unfortunately, incompatible solutions. The debate between these alternatives is a particular focus of this entry, covered in Section 4.

## 1. Preliminaries

### 1.1 Why Formalism?

Why construct *formal* representations of belief? To a large extent, the rigours and rewards of formalism in epistemology are the same as they are in any other discipline. It requires that we state basic principles precisely, and in return it permits us to demonstrate, whether by deductive proof or computer simulation, their logical consequences and connections. Often, these consequences and connections are unexpected—sometimes *so* unexpected that it is hard to imagine how they could have been discovered without the aid of the formalism. If an attractive-looking principle has an unattractive consequence, it is easy to imagine how one might have been tempted to evade or ignore it, had it not been so clearly demonstrated. Perhaps the most common tragedy is to find that several attractive principles are mutually inconsistent and that some unpleasant sacrifice must therefore be made. After a few such experiences, the epistemologist comes to feel that formal representations forestall equivocation and self-deception and promote progress and understanding.

Of course, formal representations are not without their drawbacks. Once a formal framework is adopted, certain questions and projects become salient and others recede into the background. Some antecedently interesting questions may become impossible to express in the new formalism; insiders may be tempted to disparage these questions as senseless or uninteresting. In the worst cases, this can render formal work shallow, or evasive of important issues. These are the pitfalls of parochialism. To avoid them, it is sometimes helpful to recall what motivated the formalism in the first place. To this end, a framework's history is sometimes illuminating. It also helps to transition out of, and between, formalisms: this change of perspective combats parochialism in epistemology in the same way that immersion in a new language or culture tends to combat it more broadly.

The preceding could be said for many subjects apart from epistemology. Indeed, mathematical method may facilitate progress on questions specific to epistemology, much as it has on questions specific to physics or economics. And excessive allegiance to a particular formalism has pitfalls in physics and economics, just as it does in epistemology. If we left the matter there, however, we would not do justice to the unique ambitions that have been framed for mathematical method in epistemology in particular.

Leibniz dreamed of a *characteristica universalis*—an exact idea-calculus in which it would be possible to arbitrate scientific disputes by calculation and which would serve as a “lodestar” to those “who navigate the sea of experiments” (Leibniz 1679/1989)[^leibniz-1679]. In the last century, the Unity of Science movement hoped that a new logic would serve as a universal language in which to commensurate all of the sciences and—so united—apply their full power to the problems of the day. But, as the clash between the Copernican and Ptolemaic systems illustrates, stating two theories precisely and mathematically does not suffice to adjudicate disputes between them. To that end, a significant effort was devoted to developing a calculus in which to compute the precise bearing of evidence, and thereby arbitrate between theories. This calculus was conceived not as a boon to philosophy alone, but as a kind of common law to govern and coordinate the federated republics of science. Many of the formalisms covered in this article can be traced back to a program whose ambition may stagger our contemporary imaginations.

Pascal (ca. 1658/2004) applied the new probability calculus to intensely personal questions of faith. Indeed, many epistemologists are not particularly interested in norms for *scientific* inquirers, but in the norms governing the entire belief system of an individual: how their beliefs must cohere in order to be rational; how they must be reflected in decision making; and how they ought to accommodate new evidence. Subjective probability theory and its accompanying theory of rational decision is the most comprehensive contemporary expression of this project; for better or worse, it is by far the dominant theory of practical rationality of our day. We introduce it in Section 3.1.

We invoke our illustrious forebears here mainly to illustrate the great scope of their ambitions, with the hope that their meliorist spirit will breathe life into the material covered in this article. In the midst of mathematical detail, it is easy to forget that formal epistemology is an expression of the hope that reason can be productively turned upon itself. If this project is miscarried, we risk obstructing or artificially circumscribing the scope and power of human reason. But what if it succeeds?

### 1.2 The Objects of Belief

In the following we will see several proposed models for the structure of belief. Most of these proposals take the objects of belief to be either *propositions,* or *sentences* in a formalized language. This section reviews the basic notions required to work with propositions and sentences in a formal language. If the reader feels overwhelmed with the technicalities in this section, they should feel free to postpone them, and refer back to it on-the-fly. Readers who are accustomed to working with these objects may freely skip this section.

The received view is that the objects of belief are proposition and propositions are sets of *possible worlds*. But what are these supposed to be? This is a rather difficult question (see the entry on possible worlds). On one picturesque view, a possible world is a complete description of an alternative reality. To pick out a possible world is to specify–in a way careful to avoid contradiction–every fact that holds in some possible reality that is not necessarily our own. On this view, the set of *all* possible worlds $W$ is like a giant library that contains the complete history of every possible reality. The *actual* world picks out the volume that corresponds to our own reality.

It is not necessary–and perhaps unhelpful–to think of possible worlds as total metaphysical possibilities. At this extremely fine level of granularity, each possibility specifies an infinity of obscure and uninteresting details. But context usually determines which features of the world we can take for granted; which we are uncertain about but would prefer not to be; and which are of no interest. For example, Sophia may be interested in the identity of the next mayor of Vienna, but whether they are left or right-handed is of no importance. For our purposes, a possible world is a complete specification of all and only those features of the world that are relevant given the context. The set $W$, therefore, is the set of all contextually relevant epistemic possibilities. Narrowing down the set of possibilities to an individual $w\in W$ would completely settle some interesting question under discussion. A proposition $P\subseteq W$ is a *set* of possible worlds, i.e. it is a partial specification of the way the world is. To be certain that $P$ is true is to be certain that the actual world is among the set of worlds $\{ w : w \in P \}$ since $P$ is true in a possible world $w$ iff $w\in P$.

Propositions enjoy a set-theoretic structure. The relative complement of $P$, $\neg P = W\setminus P$, is the set of all worlds in which $P$ is false. If $P,Q$ are arbitrary propositions, then their intersection $P\cap Q$ is the set of all worlds in which $P$ and $Q$ are both true. The disjunction $P\cup Q$ is the set of worlds in which at least one of $P,Q$ is true. The material conditional $P\rightarrow Q$ is the set of worlds $\neg P \cup Q,$ in which either $P$ is false or $Q$ is true. If $P\subseteq Q$ we say that $P$ *entails* $Q$ and also that $P$ is *logically stronger* than $Q$. If $P\subseteq Q$ and $Q\subseteq P$ we write $P\equiv Q$ and say that $P$ and $Q$ are *logically equivalent*. The tautological proposition $W$ is true in all worlds and the contradictory proposition, the empty set $\varnothing$, is not true in any world. A set of propositions $\mathbf{A}$ is *consistent* iff there is a world in which all the elements of $\mathbf{A}$ are true, i.e. if $\cap \mathbf{A} \neq \varnothing.$ Otherwise, we say that $\mathbf{A}$ is *inconsistent*. A set of propositions $\mathbf{A}$ is *mutually exclusive* iff the truth of any one element implies the falsehood of all other elements. The set of logical consequences of $\mathbf{A}$, written $\Cn(\mathbf{A}),$ is the set $ \{ B \subseteq W : \cap \mathbf{A} \text{ entails } B \}$. Note that if $\mathbf{A}$ is inconsistent, then $\Cn(\mathbf{A})$ is $\mathcal{P}(W)$, the set of all propositions over $W$.

A set of propositions $\mathbf{F}$ is a *field* (sometimes *algebra*) iff $\mathbf{F}$ contains $W$ and it is closed under intersection, union and complementation. That is to say that if $A,B$ are both elements of $\mathbf{F}$ then $W,A\cup B,A\cap B$ and $\neg A$ are also elements of $\mathbf{F}.$ A set of propositions $\mathbf{F}$ is a *σ-field* (sometimes *σ-algebra*) iff it is a field that is closed under *countable* intersections, i.e. if $\mathbf{S}\subseteq \mathbf{F}$ is a countable collection of propositions, then the intersection of all its elements $\cap \mathbf{S}$ is also an element of $\mathbf{F}.$ That definition implies that a *σ*-field is also closed under countable unions. It is not difficult to prove that the intersection of *σ*-fields is also a *σ*-field. That implies that every collection of propositions $\mathbf{F}$ generates $\sigma(\mathbf{F})$, the least *σ*-field containing $\mathbf{F}$, by intersecting the set of all *σ*-fields containing $\mathbf{F}$.

Propositions, although usually expressed by sentences in a language, are not themselves sentences. That distinction is commonly drawn by saying that propositions are *semantic* objects, whereas sentences are *syntactic* objects. Semantic objects (like propositions) are meaningful, since they represent meaningful possibilities, whereas bits of syntax must be “interpreted” before they become meaningful. In a slogan: sentences are potentially meaningful, whereas propositions already are.

For our purposes, a *language* $\mathbf{L}$ is identified with the set of all grammatical sentences it contains. Sentences will be denoted by lowercase letters Greek $\alpha, \beta, \ldots$. The language $\mathbf{L}$ is assumed to contain a set of *atomic* sentences $\alpha,\beta, \ldots$ which are not built out of any other sentences, as well as all the sentences generated by combining the atomic sentences with truth-functional connectives from propositional logic. In other words: if $\alpha,\beta$ are sentences in $\mathbf{L}$ then $\neg \alpha$, $\alpha\vee \beta$, $\alpha\wedge \beta$, $\alpha\rightarrow \beta$, and $\alpha \leftrightarrow \beta$ are also sentences in $\mathbf{L}$. These are meant to be read respectively as “not *α*”, “*α* or *β*”, “*α* and *β*”, “if *α*, then *β*” and “*α* if and only if *β*”. The symbol $\bot$ (pronounced “falsum”) denotes an arbitrarily chosen contradiction (e.g. $\alpha\wedge \neg \alpha)$ and the symbol $\top$ (pronounced “top”) denotes an arbitrary tautology.

Some of the sentences in $\mathbf{L}$ follow “logically” from others. For example, under the intended interpretation of the truth-functional connectives, *α* follows from the sentence $\alpha\wedge \beta$ and also from the set of sentences $\{\beta, \beta\rightarrow \alpha \}$. To capture the essentials of deductive consequence, we introduce a *consequence relation*, $\vdash$, which holds between any two sentences $\alpha \vdash \beta$, whenever *β* is a deductive consequnce of *α* . The consequence operator is assumed to satisfy the following properties, which abstract the characteristic features of deductive logic:

$$\begin{align} \tag{Reflexivity} &\alpha \vdash \alpha;\\ \tag{Monotonicity} \alpha \vdash \gamma, &\text{ implies } \alpha \wedge \beta \vdash \gamma;\\ \tag{Cut} \alpha \vdash \beta \text{ and } \alpha \wedge \beta \vdash \gamma &\text{ implies } \alpha \vdash \gamma. \end{align}$$

Reflexivity merely expresses the triviality that any sentence *α* is a deductive consequence of itself. Monotonicity expresses the fact that adding more premises to a deductive argument allows you to derive all the same conclusions as you could with fewer. Cut says roughly that deductive conclusions are on an equal epistemic footing with their premises: there is no loss of confidence as derivations get longer. Together, these principles imply that “consequences of consequences are consequences” i.e. that $\alpha \vdash \beta$ and $\beta \vdash \gamma$ implies that $\alpha \vdash \gamma$.

We will write $\Cn(\alpha)$ for the set of all *β* such that $\alpha\vdash \beta$. If $\Delta$ is a finite set of sentences, we write $\Cn(\Delta)$ for $\Cn(\wedge_{\alpha\in\Delta}\alpha)$ the set of all deductive consequences of the conjunction of all sentences in $\Delta$. If $\Delta$ is an infinite set of sentences, it is a bit more complicated to define $\Cn(\Delta)$ since the infinite conjunction of all sentences in $\Delta$ is not a sentence of the formal language. To avoid infinite conjunctions, let $\alpha_1, \alpha_2, \ldots$ be an enumeration of the sentences in $\Delta$ and let $\beta_i = \bigwedge_{j\leq i} \alpha_j$, the conjunction of the first $i$ sentences in the enumeration. Finally, let $\Cn(\Delta) = \cup_{i=1}^\infty \Cn(\beta_i)$. It is sometimes convenient to state principles in terms of the consequence operator $\Cn(\cdot)$. For example, we assume that the deductive consequence relation satisfies the following additional property.

$$\begin{align} \tag{Deduction Theorem} \beta\in \Cn(\Delta \cup \{\alpha\}) \text{ implies that } (\alpha\rightarrow \beta)\in\Cn(\Delta). \end{align}$$

The deduction theorem expresses the fact that you can prove the conditional sentence $\alpha\rightarrow \beta$ by assuming *α* and then deriving *β*. Unsurprisingly, it is possible to prove that this property holds for most deductive logics one would encounter, including both propositional and first-order logic.

Every formal language $\mathbf{L}$ gives rise to a set of possible worlds in a canonical way. A *model* of $\mathbf{L}$ assigns a truth value to every sentence in $\mathbf{L}$ by first, assigning a truth value to ever atomic sentence and then, assigning truth values to all other sentences by respecting the intended meaning of the connectives. We write $ Mod_{\mathbf{L}} $ for the set of all models of $\mathbf{L}$. Thus, each language $\mathbf{L}$ induces a finitary field $\mathbf{A}$ over the set of all models for $\mathbf{L}$. $\mathbf{A}$ is the set of propositions over $Mod_{\mathbf{L}}$ that are expressed by the sentences in $\mathbf{L}$. $\mathbf{A}$ in turn induces a unique smallest *σ*-field $\sigma(\mathbf{A})$ that contains $\mathbf{A}$.

Once we have both a set of possibilities $W$ and a formal language $\mathbf{L}$ in context, there is a standard systematic way of connecting them. A *valuation function* $V$ maps every atomic sentence *α* in $\mathbf{L}$ to a proposition $V(\alpha)\subseteq W$, the set of worlds in which *α* is true under that interpretation of the atoms. For example, if $W=Mod_\mathbf{L}$, then atoms are mapped exactly to the models in which they are true. The valuation function also interprets the non-atomic sentences in a way that respects the intended meanings of the logical connectives, i.e. so that $V(\top)=W$, $V(\neg \alpha)=W\setminus V(\alpha)$ and $V(\alpha\wedge \beta)= V(\alpha)\cap V(\beta).$ In this fashion, each sentence in $\mathbf{L}$ is mapped to a set of possible worlds.

We write $\alpha \vDash \beta $ if for all valuations $V$, $V(\alpha) \subseteq V(\beta).$ Then, $ \alpha \vDash \beta$ expresses the fact that no matter how the non-logical vocabulary of $\mathbf{L}$ are interpreted, *β* is true in all the worlds in which all sentences in *α* are true. We say that *α* is *valid* iff $\{ \top \} \vDash \alpha$, i.e if $W\subseteq V(\alpha)$ for all valuation functions. Then, *α* is valid iff *α* is true in all possible worlds, no matter how the non-logical vocabulary are interpreted. For example, the sentence $\alpha\vee \neg \alpha$ is valid.

We assume the following property of our deductive consequence relation.

$$\begin{align} \tag{Soundness} \text{If } \alpha \vdash \beta, \text{ then } \alpha \vDash \beta. \end{align}$$

Soundness says that if the sentence *β* is a derivable consequence of *α*, then no matter how the non-logical vocabulary of $\mathbf{L}$ are interpreted, *β* is true in all the worlds in which *α* true. That is to say that from true premises, our consequence relation always derives true conclusions. Soundness also implies that every theorem is valid. Soundness is a basic requirement of any *deductive* consequence relation, and illustrates the intended connection between deductive proof and semantic entailment.

Sentences are, in a sense, capable of expressing distinctions that propositions cannot. For example, the two sentences $p$ and $\neg \neg p$ are obviously distinct. But if $p$ and $q$ are provably equivalent, i.e. if $\vdash p \leftrightarrow q,$ then $\{p\}\vdash q$ and $\{q\} \vdash p.$ By Soundness, $\{p\} \vDash q$ and $\{q\}\vDash p.$ Therefore, for any valuation function, $V(p)=V(q).$ So $p$ and $q$ must express the same proposition. Of course, an agent who is unaware of the equivalence might believe $p$ without believing $q$. What's worse, every sentence $p$ such that $\vdash p$ must express the tautological proposition $W$. Of course, ordinary agents do not always recognize theorems of propositional logic. For this reason, some argue that it is sentences, rather than propositions, that are the appropriate objects of belief. However, most of the proposed models we will study require that rational agents adopt the same belief attitude toward logically equivalent sentences. That is a very strict requirement, amounting to an assumption that every rational agents is *logically omniscient*, i.e. she finds all logical entailments to be completely transparent. So long as that is the case, there is no significant difference between taking the objects of belief to be sentences or propositions. See, however, Hacking (1967)[^hacking-1967], Garber (1983)[^garber-1983] and Pettigrew (forthcoming) for ideas on how to relax the requirement of logical omniscience. Still others are not satisfied with either sentences, or propositions. Perry (1979)[^perry-1979], Lewis (1979)[^lewis-1979] and Stalnaker (1981)[^stalnaker-1981] argue that in order to capture *essentially indexical* beliefs–beliefs that essentially involve indexicals such as *I, here,* or *now*–the objects of belief must be *centered* propositions. We will not take up this helpful suggestion here, but see Ninan (2019) or Liao (2012)[^liao-2012] for more on centered propositions.

## 2. Representations of Full Belief

A prominent tradition in epistemology takes belief to be an all-or-nothing matter. According to this view, there are three doxastic attitudes an agent can take toward a sentence or proposition: either she believes *α* but not $\neg \alpha$; she believes $\neg \alpha$ but not *α*; or she believes neither *α* nor $\neg \alpha$. In the first case we say simply that she fully believes *α*; in the second case we say she fully *disbelieves* *α* and in the third we say she *suspends judgement* with respect to *α* and $\neg \alpha$. Perhaps it is also psychologically possible for an agent to fully believe both *α* and $\neg \alpha$. Since most theorists agree that she ought not, we introduce no special terminology for this case. Any belief representation that allows for finer gradations of belief attitude we will call a *graded* representation of belief.

The frameworks we introduce in this section deal chiefly with belief attitudes of the all-or-nothing variety. Most of these represent an agent’s belief state at any particular time by the set of all sentences that she fully believes. All of the frameworks will require that, as a matter of rationality, belief states must be deductively closed and not entail any contradictions. If that were the end of the story, these frameworks would not be very interesting. The real insight of these frameworks is that an agent’s belief state is not adequately represented by a complete list of her current beliefs, but only by her dispositions to *update* those beliefs upon acquiring new information. Thus, the focus of these frameworks is developing normative principles governing the dynamics of belief states as new information is assimilated. As we shall see, although these frameworks largely agree on the static principles of rationality, they conflict over the dynamical principles of belief update.

It is often informative to see how qualitative update dynamics emerge from the finer structure of degrees of belief. We will see in this section several versions of the following kind of “representation” result: every agent satisfying a certain set of qualitative dynamical update principles can be thought of as an agent updating graded beliefs of a certain structure and, conversely, every agent with graded beliefs of that structure will satisfy the same set of qualitative dynamical principles. These results suggest bridge principles connecting full and partial representations of belief.

### 2.1 Non-monotonic logic

In Section 1.2 we introduced the notion of a deductive consequence relation. One of the characteristic features of a deductive consequence relation is that adding more premises to a deductive argument allows you to derive all the same consequences as you could with fewer. In other words, for any sentences $\alpha , \beta , \gamma$ in $\mathbf{L}$: if $\alpha \vdash \gamma,$ then $ \alpha\wedge \beta \vdash \gamma$.

Of course, all sorts of seemingly rational everyday reasoning violates Monotonicity. If Sophia is told that her thermometer reads 85° Fahrenheit, she would be justified in concluding that it is not too cold to have dinner in the garden. If she then learns that her thermometer was moved above the oven where she is boiling her pasta, she might retract her conclusion. That does not mean that her original inference was unreasonable or irrational. Non-monotonicity is simply unavoidable in ordinary human contexts. Inductive inference is famously non-monotonic. Ethical and legal reasoning is similarly shot through with non-monotonicities (Ross, 1930 and Ullman-Margalit, 1983)[^ross-1930][^ullman-margalit-1983].

Non-monotonic logic studies a defeasible consequence relation $\dproves$ between premises, on the left of the wavy turnstile, and conclusions on the right. One may think of the premise *α* on the left as a sentence expressing all the “hard evidence” that an agent may possesses, and the conclusion on the right to be the defeasible conclusions that are justified on the basis of *α*. The expression $\alpha \dproves \beta $ may be read as: if my total evidence were *α*, I would be justified in concluding *β*. Thus a particular relation of defeasible consequence represents an agent's dispositions to update her beliefs in light of new information.

Recall from Section 1.2 that a deductive consequence relation satisfies Soundness. That is to say that $ \alpha \vdash \beta$ only if $ \beta $ is true in all the worlds in which *α* is true. It is clear from the preceding examples that defeasible reasoning cannot satisfy Soundness. If $\alpha \dproves \beta$ then perhaps *β* is true in “typical” worlds in which *α* is true. We call a consequence relation *ampliative* if $\alpha \dproves \beta,$ but there are worlds in which $ \alpha $ is true, but *β* is false. The terminology derives from the Latin *ampliare*, “to enlarge”, because defeasible reasoning “extends” or “goes beyond” the premises. Ampliativity and non-monotonicity go hand in hand in all but the most contrived circumstances.

Over the past forty years, researchers in artificial intelligence have created many different logics for defeasible inference, often developed to model a specific kind of defeasible reasoning. See the entry on non-monotonic logic for an excellent overview. In view of this profusion of specialized logics, non-monotonic logic investigates which properties a logic of defeasible consequence must have in order to count as a *logic* at all. (See Gabbay (1985)[^gabbay-1985] for the origins of this abstract point of view.) Non-monotonic logic provides a crucial *lingua franca* for comparing different logics of defeasible inference. It is also extremely apt for the purposes of this article because it allows us to compare different normative theories of how beliefs ought to be updated in light of new evidence, as well as theories of how full and partial beliefs ought to relate to each other.

Before we proceed to the technical development, it will be helpful to introduce an important early critique of nonmonotonic logic due to the philosopher John Pollock. Pollock (1987)[^pollock-1987] identifies two sources of nonmonotonicity in defeasible reasoning. An agent may believe *β* because she believes *α* and takes *α* to be a defeasible *reason* for *β*. Pollock distinguishes two kinds of *defeaters* for this inference: a *rebutting* defeater is a defeasible reason to believe $\neg \beta,$ whereas an *undercutting* defeater is a reason to believe $\neg \alpha$. Either kind of defeater may induce an agent to retract her belief in *β*. Pollock's point is that since nonmonotonic logics typically do not represent the structure of an agent's reasons, they often fail to elegantly handle cases of undercutting defeat. We shall soon see several examples.

#### 2.1.1 Principles for Non-montonic Logic

Kraus, Lehmann and Magidor (1990) articulate a set of principles that any “reasonable” nonmonotonic language must satisfy. It is now common to refer to this set of principles as System P. To this day, these principles remain the uncontroversial core of nonmonotonic logic.

| (KLM1) | $\alpha \dproves \alpha$ | Reflexivity |
| --- | --- | --- |
| (KLM2) | If $\vdash \beta \leftrightarrow \gamma$ and $\alpha \dproves \beta$, then $\alpha \dproves \gamma$. | Left Logical Equivalence |
| (KLM3) | If $\vdash \alpha \rightarrow \beta$ and $\gamma \dproves \alpha$, then $\gamma \dproves \beta$. | Right Weakening |
| (KLM4) | If $\alpha \wedge \beta \dproves \gamma$ and $\alpha \dproves \beta$, then $\alpha \dproves \gamma$. | Cut |
| (KLM5) | If $\alpha \dproves \beta$ and $\alpha \dproves \gamma$, then $\alpha \wedge \beta \dproves \gamma$. | Cautious Monotonicity |
| (KLM6) | If $\alpha \dproves \gamma$ and $\beta \dproves \gamma$, then $\alpha \vee \beta \dproves \gamma$. | Or |

Reflexivity merely expresses the truism that one is entitled to infer *α* from itself. The next two principles govern how a non-monotonic consequence relation should interact with deductive consequence. Left Logical Equivalence says that if *α* and *β* are classically equivalent, then they license the exact same defeasible inferences. Right Weakening says that if *α* defeasibly licenses *β*, then it also licenses all the deductive consequences of *β*. Together, these principles say that defeasible reasoning encompasses all of deductive reasoning. This sounds unreasonable if we think of $\dproves$ as modeling the defeasible reasoning of a bounded agent. It begins to sound better if we think of $\dproves$ as modeling the ampliative conclusions that are justified on the basis of some “hard” evidence.

The remaining principles are the heart of System P. Cut says that adding conclusions defeasibly inferred from $\alpha $ to the premises does not *increase* inferential power. Cautious Monotonicity says that it does not *decrease* inferential power. Let $C(\alpha)$ be $ \{ \beta : \alpha \dproves \beta \} $, the set of conclusions licensed by *α*. If we think of the premise on the left of $\dproves$ as expressing my total “hard” evidence, and the set $C(\alpha)$ as a theory inductively inferred on the basis of *α*, then Cautious Monotonicity is an expression of hypothetico-deductivism: if I learn a consequence of my theory $C(\alpha)$, I should not retract any of my previous conclusions. Moreover, Cut says that I should not add any new conclusions. Taken together, the two principles say that if a consequence of your theory is added to your total evidence, your theory should not change, i.e. if $\alpha\dproves \beta$, then $C(\alpha)=C(\alpha\wedge \beta)$.

The final principle is best approached by way of one of its instances. Substituting $\neg \alpha$ for *β* yields the following principle:

|   | If $\alpha \dproves \gamma$ and $\neg \alpha \dproves \gamma$, then $\top\dproves \gamma$. | Case Reasoning |
| --- | --- | --- |

Any genuine consequence relation ought to enable reasoning by cases. If I would infer *γ* irrespective of what I learned about *α*, I should be able to infer *γ* before the matter of *α* has been decided. In full generality, Or says that if *γ* follows defeasibly from both *α* and *β*, it ought to follow from their disjunction. Any consequence relation that satisfies Reflexivity, Right Weakening and Or must also satisfy the following principle:

|   | If $\alpha \wedge \beta \dproves \gamma$, then $\alpha \dproves \beta \rightarrow \gamma$. | Conditionalization |
| --- | --- | --- |

Conditionalization says that upon learning new evidence, you never “jump to conclusions” that are not entailed by the deductive closure of your old beliefs with the new evidence. That is not an obviously appealing principle. An agent that starts out with only the trivial evidence $\top$ will either fail to validate Conditionalization or never make any ampliative inferences at all. Suppose that after observing 100 black ravens an agent validating Conditionalization comes to believe that all ravens are black. Then, at the outset of inquiry, she must have believed that either all ravens are black, or she will see the first non-black raven among the first hundred. Such an agent seems strangely opinionated about when the first counterexample to the inductive generalization must appear.

For a more realistic example, consider the 1887 Michelson-Morely experiment. After a null result failing to detect any significant difference between the speed of light in the prevailing direction of the presumed aether wind, and the speed at right angles to the wind, physicists turned against the aether theory. If the physicists validated Conditionalization then, before the experiments, they must have believed that either there is no luminiferous aether, or the aether wind blows quickly enough to be detected by their equipment. But why should they have been so confident that the aether wind is not too slow to be detectable?

Even if there is nothing objectionable about an agent who validates Conditionalization, there is something very anti-inductivist about the thesis that all justified defeasible inferences on the basis of new evidence can be reconstructed as deductive inferences from prior conclusions plus the new evidence. Under Conditionalization, dispositions to form inductive generalizations must be “programmed in” with material conditionals at the outset of inquiry. (See Schurz (2011)[^schurz-2011] for a similar critique, in a slightly different context.) Anyone sympathetic to this critique must reject either Or, Reflexivity, or Right Weakening. Finding such surprising consequences of seemingly unproblematic principles is one of the boons of studying non-monotonic logic.

We finish this section by introducing one more prominent and controversial principles of non-monotonic logic. Adding this principle to System P results in what is commonly referred to as System R. The position one takes on this principle will determine how one feels about many of the theories which we turn to in the following. Kraus et al. (1990) claim that any rational reasoner should validate the following strengthening of Cautious Monotonicity:

| (KLM7) | If $\alpha \dproves \beta$ and $\alpha \not\mkern-7mu\dproves \hspace{1pt} \neg\gamma $, then $\alpha \wedge \gamma \dproves \beta.$ | Rational Monotonicity |
| --- | --- | --- |

Rational Monotonicity says that so long as new evidence *γ* is logically compatible with your prior beliefs $C(\alpha)$, you should not retract any beliefs from $C(\alpha)$. Accepting both Rational Monotonicity and Conditionalization amounts to saying that when confronted with new evidence that is logically consistent with her beliefs, a rational agent responds by simply forming the deductive closure of her existing beliefs with the new evidence. On that view, deductive logic is the only necessary guide to reasoning, so long as you do not run into contradiction. Stalnaker (1994) gives the following well-known purported counterexample to Rational Monotonicity.

Suppose that Sophia believes that Verdi is Italian and that Bizet and Satie are both French. Let *α* be the sentence that Verdi and Bizet are compatriots. Let *β* be the belief that Satie is French. Let *γ* be the sentence that Bizet and Satie are compatriots. Suppose that Sophia receives the evidence *α*. As a result, she concludes that either Verdi and Bizet are both French, or they are both Italian, but she cannot say which. She retains her belief that Satie is French. So $\alpha \dproves \beta$ and $\alpha \not\mkern-7mu\dproves \neg \gamma$. Now suppose that she receives the evidence *γ*. Since *γ* is compatible with her previous conclusions, Rational Monotonicity requires her to retain belief in *β* and conclude that all three composers are French. However, it seems perfectly rational to retract *β* and conclude that the three are either all Italian, or all French.

Kelly and Lin (forthcoming) use the following example to argue against Rational Monotonicity. There are just two people in Sophia's office, named Alice and Bob. She is interested in whether one of them owns a certain Ford. Let *β* be the sentence that Alice owns the Ford. Let *γ* be the sentence that Bob has the Ford. Sophia has inconclusive evidence that Alice owns the Ford–she saw her driving one just like it. She has weaker evidence that Bob owns the Ford–his brother owns a Ford dealership. Based on her total evidence *α* she concludes $\beta \vee \gamma$, i.e. that someone in the office owns the Ford, but does not go so far as inferring *β*, or *γ*. Then, Alice says that the Ford she was driving was rented and that she doesn't own a car. That defeats Sophia's main reason for $\beta\vee\gamma$, and therefore she retracts her belief that someone in the office has a Ford. But since $ \alpha \not\mkern-7mu\dproves \neg \beta $, Rational Monotonicity requires her to retain belief in $\beta\vee\gamma$ and conclude that Bob owns the Ford. However, there does not seem to be anything irrational about she has reasoned. This seems to be an illustration of Pollock’s (1987)[^pollock-1987] point: the logic is going wrong because it is ignoring the structure of Sophia’s reasons.

Defenders of Rational Monotonicity will argue that, if we find these counterexamples plausible, it is because we are under-representing either the structure of the agents prior beliefs, or of the information that triggers the update. If we were to describe these in realistic detail, they argue, we would not be convinced by these counterexamples. For an elaboration of this line of defense, see Section 5 in Lin (2019)[^lin-2019]. Other criticisms of Rational Monotonicity do not rest essentially on the plausibility of counterexamples, but on the incompatibility of Rational Monotonicity with competing norms of inquiry. One such criticism, due to Lin and Kelly (2012), will be discussed in Section 4.2.4. For another example, see Genin and Kelly (2018).

#### 2.1.2 Preferential Semantics

So far we have considered a non-monotonic consequence relation merely as a relation between syntactic objects. We can rephrase properties of non-monotonic logic “semantically,” i.e. in terms of the possible worlds in which the sentences are true or false. In some cases, this allows us to give a very perspicuous view on defeasible logic.

Recall from Section 1.2 that a deductive consequence relation satisfies Soundness, i.e. that $\alpha\vdash \beta$ only if *β* is true in all the worlds in which *α* is true. As we have discussed, non-monotonic logics are ampliative, and therefore must violate Soundness. Shoham (1987)[^shoham-1987] inaugurated a semantics for non-monotonic logics in which $\alpha\dproves \beta$ only if *β* is true in a “preferred” set of worlds in which *α* is true. On a typical interpretation, these are the most typical, or most normal worlds in which *α* is true.

Kraus et al. (1990) first proved most of the results of this section. However, the original results are stated at a level of generality that creates too much technical fuss for our purposes here. We state a simplified, but more perspicuous, version of their results. See Makinson (1994)[^makinson-1994] and the entry on defeasible reasoning for a presentation truer to the original.

A *preferential model* is a triple $\langle W,V,\prec \rangle $ where $W$ is a set of possible worlds, $V$ is a valuation function and $\prec$ is an arbitrary relation on the elements of $W$. Recall from Section Section 1.2 that $V(\alpha)$ is the set of worlds in which *α* is true. The relation $\prec$ is *transitive* iff $x\prec z$ whenever $x\prec y$ and $y \prec z $. The relation $\prec $ is *irreflexive* iff for all $w\in W$ it is not the case that $w\prec w$. A transitive, irreflexive relation is called a *strict order*. We write $w\preceq v$ iff $w\prec v$ or $w=v$. The strict order $\prec$ is *total* iff for $w,v\in W$ either $w\prec v$ or $v\prec w$.

We say that $w$ is an *α-minimal* world iff $w\in V(\alpha)$ and there is no $v\in V(\alpha)$ such that $v\prec w$. Every preferential model gives rise to a consequence relation by setting $\alpha \dproves \beta$ whenever *β* is true in all the *α-minimal* worlds. Kraus et al. (1990) prove the following:

**Theorem**. Suppose that $\prec$ is a strict order over $W$. Define the consequence relation $\dproves$ by setting $\alpha \dproves \beta$ iff *β* is true in all the *α*-minimal worlds. Then, $\dproves$ satisfies KLM1-6. If $\prec$ is total, KLM7 is also satisfied. Conversely, suppose that the consequence relation $\dproves$ satisfies KLM1–6. Then, there is a strict order $\prec$, such that $\alpha \dproves \beta$ iff *β* is true in all the *α*-minimal worlds. If KLM7 is also satisfied, then the order can be chosen to be total.

That means that we can interpret any consequence relation $\dproves$ satisfyings the basic KLM postulates in the following way: $\dproves$ represents the belief dispositions of an agent who (1) has a strict plausibility ordering over the set of possibilities in $W$ and (2) believes whatever is entailed by the “most plausible” possibilities compatible with her hard evidence. If Rational Monotonicity is not satisfied, then some possibilities will be incommensurable in plausibility. Otherwise, all possibilities will be commensurable.

### 2.2 AGM Belief Revision Theory

Like nonmonotonic logic, the theory of belief revision is concerned with how to update one’s beliefs in light of new evidence. When the new evidence is consistent with all prior beliefs, the counsel of the theory is simple, if exacting: simply add the new evidence to your old stock of beliefs and close under deductive consequence. Things are more complicated when the new evidence is inconsistent with your prior beliefs. If you want to incorporate the new information and remain logically consistent, you will have to retract some of your original beliefs. The central problem of belief revision is that deductive logic alone cannot tell you which of your beliefs to give up–this has to be decided by some other means.

Considering a similar problem, Quine and Ullian (1970) enunciated the principle of “conservatism,” conseling that our new beliefs “may have to conflict with some of our previous beliefs; but the fewer the better.” In his (1990), Quine dubs this the “maxim of minimal mutilation.” Inspired by these suggestive principles, Alchourrón, Gärdenfors, and Makinson (1985) developed a highly influential theory of belief revision, known thereafter as AGM theory, after its three originators.

In AGM theory, an agent’s beliefs are represented by a set of sentences $\bB$ from a formal language $\mathbf{L}$. The set $\bB$ is called the *belief state* of the agent. The belief state is required to be consistent and deductively closed (Hintikka 1961 and the entry on epistemic logic)[^hintikka-1961]. Of course, this is a somewhat unrealistic idealization. Levi (1991)[^levi-1991] defends this idealization by changing the interpretation of the set $\bB$–these are the sentences that the agent is *committed* to believe, not those that she actually believes. Although we may never live up to our commitments, Levi argues that we are committed to the logical consequences of our beliefs. That may rescue the principle, but only by changing the interpretation of the theory.

AGM theory studies three different types of belief change. *Contraction* occurs when the belief state $\bB$ is replaced by $\bB\div \alpha$, a logically closed subset of $ \bB$ no longer containing *α*. *Expansion* occurs when the belief state $ \bB$ is replaced with $\bB+\alpha = \Cn(\bB\cup \{\alpha \})$, the result of simply adding *α* to $\bB$ and closing under logical consequence. *Revision* occurs when the belief state $\bB$ is replaced by the belief state $\bB*\alpha$, the result of “minimally mutilating” $\bB$ in order to accommodate *α*.

Contraction is the fundamental form of belief change studied by AGM. There is no mystery in how to define expansion, and revision is usually defined derivatively via the *Levi identity* (1977): $\bB*p = (\bB \div \neg p) + p.$ Setting the mold for future work (Gärdenfors 1988, Gärdenfors and Rott 1995)[^gärdenfors-1988][^gärdenfors-1988-2][^gärdenfors-1995], Alchourrón, Gärdenfors and Makinson (1985) proceed axiomatically: they postulate several principles that every rational contraction operation must satisfy. Fundamental to AGM theory are several representation theorems showing that certain intuitive constructions give rise to contraction operations satisfying the basic postulates and conversely, that every operation satisfying the basic postulates can be seen as the outcome of such a construction. See the entry on belief revision, Huber (2013a)[^huber-2013a], or Lin (2019)[^lin-2019] for an excellent introduction to these results.

AGM theory is unique in focusing on belief contraction. For someone concerned with maintaining a database, contraction is a fairly natural operation. Medical researchers might want to publish a data set, but make sure that it cannot be used to identify their patients. Privacy regulations may force data collectors to “forget” certain facts about you and, naturally, they would want to do this as conservatively as possible. However, a plausible argument holds that all forms of rational belief change occurring “in the wild” involve learning new information, rather than conservatively removing an old belief. All the other formalisms covered in the article focus on this form of belief change. For this reason, we focus on the AGM theory of revision and neglect contraction.

Before delving into some of the technical development, we mention some important objections and alternatives to the AGM framework. As we have mentioned, the belief state of an agent is represented by the (deductively closed) set $\bB$ of sentences the agent is committed to believe. The structure of the agent’s *reasons* is not explicitly represented: you cannot tell of any two $\alpha,\beta\in \bB$ whether one is a reason for the other. Gärdenfors (1992)[^gärdenfors-1992] distinguishes between *foundations* theories, that keep track of which beliefs justify which others, and *coherence* theories, which ignore the structure of justification and focus instead on whether beliefs are consistent with one another. Arguing for the coherence approach, he draws a stark distinction between the two:

According to the foundations theory, belief revision should consist, first, in giving up all beliefs that no longer have a *satisfactory justification* and, second, in adding new beliefs that have become justified. On the other hand, according to the coherence theory, the objectives are, first, to maintain *consistency* in the revised epistemic state, and, second, to make *minimal changes* of the old state that guarantee overall coherence.

Implicit in this passage is the idea that foundations theory are out of sympathy with the principle of minimal mutilation. Elsewhere (1988), Gärdenfors is more conciliatory, suggesting that some hybrid theory is possible and perhaps even preferable:

I admit that the postulates for contractions and revisions that have been introduced here are quite simpleminded, but they seem to capture what can be formulated for the meager structure of belief sets. In richer models of epistemic states, admitting, for example, reasons to be formulated, the corresponding conservativity postulates must be formulated much more cautiously (p. 67).

Previously, we have seen Pollock (1987)[^pollock-1987] advocating for foundationalism. In artificial intelligence, Doyle’s (1979)[^doyle-1979] *reason maintenance system* is taken to exemplify the foundations approach. Horty (2012)[^horty-2012] argues that default logic aptly represents the structure of reasons. For a defense of foundationalism, as well as a useful comparison of the two approaches, see Doyle (1992)[^doyle-1992].

Another foundationalist view advocates for *belief bases* instead of belief states. A belief base is a set of sentences that is typically not closed under logical consequence. Its elements represent “basic” beliefs that are not derived from other beliefs. This allows us to distinguish between sentences that are explicit beliefs, like “Shakespeare wrote Hamlet” and never-thought-of deductive consequences like “Either Shakespeare wrote Hamlet or Alan Turing was born on a Monday.” Revision and contraction are then redefined to operate on belief bases, rather than belief sets. That allows for finer distinctions to be articulated, since belief bases which have the same logical closure are not treated interchangeably. For an introduction to belief bases see the relevant section of the entry on the logic of belief revision, §5. For a book-length treatment, see Hansson (1999b)[^hansson-1999b].

Finally, one of the most common criticisms of AGM theory is that it does not illuminate *iterated* belief change. In the following, we shall see that the canonical revision operation takes as input an entrenchment ordering on a belief state, but outputs a belief state without an entrenchment order. That severely underdetermines the result of a subsequent revision. For more on the problem of iterated belief revision, see Huber (2013a)[^huber-2013a].

#### 2.2.1 Principles for Belief Revision

Gärdenfors (1988)[^gärdenfors-1988][^gärdenfors-1988-2] proposes the following postulates for rational belief revision. For every set of sentences $\bB \subseteq \mathbf{L}$ and any sentences $\alpha , \beta \in \mathbf{L}$:

| (AGM\*1) | $\bB * \alpha = \Cn(\bB *\alpha)$; | Closure |
| --- | --- | --- |
| (AGM\*2) | $\alpha \in \bB * \alpha$; | Success |
| (AGM\*3) | $ \bB * \alpha \subseteq \Cn(\bB \cup \{\alpha\}) $; | Inclusion |
| (AGM\*4) | If $\neg \alpha \not\in \bB $, then $ \Cn(\bB \cup \{\alpha\}) \subseteq \bB * \alpha $; | Preservation |
| (AGM\*5) | $\bB * \alpha$ is inconsistent iff $ \vdash \neg \alpha$; | Consistency |
| (AGM\*6) | If $\vdash \alpha \leftrightarrow \beta$, then $\bB * \alpha = \bB *\beta$. | Extensionality |

Closure, Success, Consistency and Extensionality all impose *synchronic* constraints on $\bB*\alpha$. They say nothing about how it must be related to the prior belief state $\bB$. Closure requires the new belief set to be deductively closed. Dropping this requirement puts you in the camp of *belief bases,* rather than belief sets (Hansson 1999a)[^hansson-1999a]. Success requires that the new information is included in the new belief state. *Non-prioritized* belief revision relaxes this requirement (Hansson 1999a)[^hansson-1999a]. Extensionality requires that the agent is sensitive only to the logical content of the evidence, and not to its mode of presentation. Consistency requires that the new belief state is logically consistent, at least when the evidence is non-contradictory.

Preservation and Inclusion are the only norms that are really about *revision*–they capture the diachronic spirit of AGM revision. Inclusion says that revision by *α* should yield *no more* new beliefs than expansion by *α*. In other words, any sentence *β* that you come to believe after revising by *α* is a deductive consequence of *α* and your prior beliefs. Consider the following principle:

|   | If $\beta \in \bB * \alpha,$ then $(\alpha \rightarrow \beta)\in\bB$. | Conditionalization |
| --- | --- | --- |

In Section 2.1.1, we considered an analogue of conditionalization for nonmonotonic logic. All the same objections apply equally well in the context of belief revision. Recall from Section 1.2 that a deductive consequence relation admits a deduction theorem iff $\Delta \cup \{ \alpha\} \vdash \beta$ implies that $\Delta \vdash \alpha\rightarrow \beta.$ So long as a deduction theorem is provable for $\Cn(\cdot),$ Inclusion and Conditionalization are equivalent. If you found any of the arguments against Conditionalization convincing, you ought to be skeptical of Inclusion.

Preservation says that, so long as the new information *α* is logically consistent with your prior beliefs, all of your prior beliefs survive revision by *α*. In the setting of non-monotonic logic, we called this principle Rational Monotony. All objections and counterexamples to Rational Monotony from Section 2.1.1 apply equally well in belief revision. As we have seen, Preservation rules out any kind of *undercutting* defeat of previously successful defeasible inferences. Accepting both Preservation (rational monotonicity) and Inclusion (conditionalization) amounts to saying that when confronted with new evidence that is logically consistent with her beliefs, a rational agent responds by simply forming the deductive closure of her existing beliefs with the new evidence. On that view, deductive logic is the only necessary guide to reasoning, so long as you do not run into contradiction.

Gärdenfors (1988)[^gärdenfors-1988][^gärdenfors-1988-2] also proposes the following two additional revision postulates, closely related to Inclusion and Preservation.

| (AGM\*7) | $ \bB * (\alpha\wedge \beta) \subseteq \Cn(\bB*\alpha \cup \{\beta\}) $; | Conjunctive Inclusion |
| --- | --- | --- |
| (AGM\*8) | If $\neg \beta \not\in \bB*\alpha $, then $ \Cn(\bB*\alpha \cup \{\beta\}) \subseteq \bB * (\alpha\wedge\beta) $. | Conjunctive Preservation |

It is possible to make the connection between belief revision and nonmonotonic logic precise. Given a belief set $\bB$ and a revision operation $*,$ we can define a defeasible consequence relation by setting $\alpha \dproves \beta \text{ iff } \beta \in \bB*\alpha.$ Similarly, given a defeasible consequence relation $\dproves$ we can define $\bB = \{ \alpha : \top \dproves \alpha \} \text{ and } \bB * \alpha = \{ \beta : \alpha\dproves \beta \}.$ Then it is possible to prove the following correspondences between AGM belief revision and the set of principles we called System R in Section 2.1.1. It follows that AGM revision can be represented in terms of a total preferential model over possible worlds.

**Theorem**. Suppose that $*$ is a revision operation for $\bB$ satisfying all eight revision postulates. Then, the non-nonmonotonic consequence relation given by $\alpha \dproves \beta \text{ iff } \beta \in \bB * \alpha$ satisfies all the principles of System R. Conversely, suppose that $\dproves$ is a consequence relation that satisfies all the principles of System R. Then, the revision operation $*$ defined letting $\bB = \{ \alpha : \top \dproves \alpha \}$ and $\bB*\alpha = \{ \beta : \alpha \dproves \beta \}$ satisfies all eight revision postulates.

#### 2.2.2 Entrenchment

Gärdenfors (1988)[^gärdenfors-1988][^gärdenfors-1988-2] introduces the notion of an *entrenchment relation* in the following way:

Even if all sentences in a … set are accepted or considered as facts …, this does not mean that all sentences are of equal value for planning or problem-solving purposes. … We will say that some sentences … have a higher degree of *epistemic entrenchment* than others. The degree of entrenchment will, intuitively, have a bearing on what is abandoned …, and what is retained, when a contraction or revision is carried out.

To model the degree of entrenchment, a relation $\preceq$ is introduced holding between sentences of the language $\mathbf{L}$. The notation $\alpha \preceq \beta$ is pronounced ‘*α* is at most as entrenched as *β*.’ Gärdenfors (1988)[^gärdenfors-1988][^gärdenfors-1988-2] requires that the relation satisfies the following postulates. For all $\alpha , \beta , \gamma$ in $\mathbf{L}$:

| $({\preccurlyeq}1)$ | If $\alpha \preccurlyeq \beta$ and $\beta \preccurlyeq \gamma$, then $\alpha \preccurlyeq \gamma$ | Transitivity |
| --- | --- | --- |
| $({\preccurlyeq}2)$ | If $\alpha \vdash \beta$, then $\alpha \preccurlyeq \beta$ | Dominance |
| $({\preccurlyeq}3)$ | $\alpha \preccurlyeq \alpha \wedge \beta$ or $\beta \preccurlyeq \alpha \wedge \beta$ | Conjunctivity |
| $({\preccurlyeq}4)$ | If $\bot \not\in \Cn(\bB)$, then $[\alpha \not\in \bB$ if and only if for all *β* in $\mathbf{L}: \alpha \preccurlyeq \beta]$ | Minimality |
| $({\preccurlyeq}5)$ | If for all *α* in $\mathbf{L}: \alpha \preccurlyeq \beta$, then $\beta \in \Cn(\varnothing)$ | Maximality |

Given a fixed set of background beliefs $\bB$ and an entrenchment ordering $\preccurlyeq$ on $\mathbf{L}$ and letting $\alpha \preccurlyneq \beta$ hold just in case $\alpha \preccurlyeq \beta$ and $\beta \not\preccurlyeq \alpha$, we can define a revision operator $*$ as follows:

$$ \bB * \alpha = \Cn(\{\beta \in \bB: \neg \alpha \preccurlyneq \beta \}\cup \{\alpha \}) $$

The idea behind this equation is that the agent revises by *α* by first clearing from her belief set anything less entrenched than $\neg \alpha,$ (by dominance, this includes everything entailing $\neg \alpha$), adding *α*, and then closing under logical consequence. Gärdenfors and Makinson (1988) prove that this definition gives rise to a revision operator satisfying AGM\*1–8 and, conversely, that every revision operator satisfying AGM\*1–8 can be seen as arising from *some* entrenchment order in this way. These results illustrate why AGM theory is not a theory of *iterated* revision: the revision operation takes as input an entrenchment order and belief state, but outputs only a belief state. That severely underdetermines the results of subsequent revisions.

Grove (1988)[^grove-1988] proves an analogous representation theorem for a systems of spheres semantics that generalizes Lewis’ (1973) semantics for counterfactuals. See the relevant section of the entry on the logic of belief revision, §4, for an introduction to Grove's possible world semantics. Segerberg (1995)[^segerberg-1995] formulates the AGM approach in the framework of dynamic doxastic logic. Lindström & Rabinowicz (1999) extend this to iterated belief revision. Of necessity, our presentation of belief revision theory has been rather compressed. For an excellent article-length introduction, see the entry on logic of belief revision, Huber (2013a)[^huber-2013a], or Lin (2019)[^lin-2019]. For a book-length treatment see Gärdenfors (1988)[^gärdenfors-1988][^gärdenfors-1988-2], Hansson (1999), or Rott (2001)[^rott-2001].

### 2.3 Epistemic Logic

The formal frameworks we have seen so far foreground dynamical principles of belief revision—they are essentially concerned with how to accommodate new information. That theoretical emphasis relegates other issues to the background. In particular, these frameworks cannot easily express principles of higher-order belief (regulating beliefs about beliefs), or about the relationship between belief and knowledge. Therefore, these frameworks are relatively silent about classical epistemological issues such as whether knowledge entails belief (see the entry on the analysis of knowledge), or why it is absurd to believe both $p$ and that you don't believe that $p$ (see the entry on epistemic paradoxes, §5.3).

Epistemic logic, which in its modern formulation is typically traced to von Wright (1951)[^wright-1951] and Hintikka (1962), is a formal framework designed to foreground these matters. For an influential introductory text, see Fagin et al. (1995). The formal language of epistemic logic extends that of propositional logic with epistemic operators ${\bf B}_a \phi$ and ${\bf K}_a \phi$, pronounced respectively as ‘agent $a$ believes that *φ*,’ and ‘agent $a$ knows that $\phi.$’ When only one agent is under discussion, the subscripts are omitted. (Readers familiar with modal logic will recognize these as analogues of other “box” operators, such as necessity and obligation.) Given this extension of the language, it is possible to express epistemic principles such as $${\bf B}(p\rightarrow q)\rightarrow ({\bf B}p\rightarrow {\bf B}q),$$ which says that your beliefs are closed under modus ponens, or $$ {\bf B}p \rightarrow {\bf B}{\bf B}p,$$ which says that if you believe $p$, then you also believe that you believe it. Note that although the first principle has natural analogues in AGM (closure) and non-monotonic logic (right weakening), the second principle cannot be straightforwardly expressed in either formalism. For example, in the AGM framework we might understand $p \in {\mathbf B}$ as saying the same thing as $ {\bf B}p,$ but it is not at all clear how to express $ {\bf BB} p$. (See however Moore (1985)[^moore-1985] and the auto-epistemology section of the entry on non-monotonic logic, §3.5.) Furthermore, epistemic logic has no difficulty expressing principles governing the interaction of knowledge and belief. For example $ {\bf K}p \rightarrow {\bf B}p$ expresses the thesis that everything that is known is also believed. AGM and non-monotonic logic cannot easily say anything about these matters.

Different choices of axioms governing belief, knowledge and their interaction give rise to different epistemic logics. A significant amount of work in epistemic logic characterizes these systems and proves various surprising consequences of the axioms. *Kripke models* are the basis of the most widely used semantics for epistemic logic. (See Goldblatt (2006) for a discussion of whether or not these models are properly attributed to Kripke.) A Kripke model equips the set of possible worlds $W$ with a binary *indistinguishibility relation* over $W$. The basic idea is that two worlds $w,w^{\prime}$ stand in the relation $w R_a w'$ if, were $w$ the actual world, agent $a$ could not rule out that the actual world is $w'$. Then, the model is connected with the formal language via the following definition: $$ w \vDash {\bf B}_a\phi \text{ iff } w'\vDash \phi \text{ for all } w' \text{ such that } w R_a w^\prime. $$ In other words: it is true in $w$ that $a$ believes *φ* iff *φ* is true in all the worlds $w'$ which $a $ cannot distinguish from $w.$ Equipped with this semantics, it is possible to prove various elegant correspondences between epistemic principles and structural properties of the indistinguishibility relation. For example, the principle $ {\bf B}\phi \rightarrow {\bf BB} \phi $ is validated whenever the indistinguishibility relation is transitive. The suspicious principle ${\bf B}\phi \rightarrow \phi$ is validated whenever the indistinguishibility relation is reflexive. A significant amount of theoretical activity is devoted to the interplay between intuitive epistemic principles expressed in the language of modal logic and elegant structural conditions on indistinguishibility relations. For an excellent introduction to this subject see the entry on epistemic logic, or the more general entry on modal logic. For more on the relationship between the logic of knowledge and belief, see the entry on philosophical aspects of multi-modal logic. More recently, alternative topological semantics for epistemic logic have seen significant theoretical activity (for example: Bjorndahl and Özgün, forthcoming).

As originally formulated in von Wright (1951)[^wright-1951] and Hintikka (1962), epistemic logic says nothing about how agents should react to new information. Segerberg introduced dynamic doxastic logic (1995, 1999) to bridge the gap between belief revision and epistemic logic. Moreover, dynamic epistemic logic was developed for the same purpose, but with an emphasis on multiagent contexts (see Plaza 1989, Baltag et al. 1998, van Ditmarsch et al. 2007)[^baltag-1998][^plaza-1989][^ditmarsch-2007]. This framework benefits from theoretical contributions from philosophers, logicians, economists and computer scientists. A proper discussion of these developments would take us too far afield. The interested reader should consult the entry on dynamic epistemic logic. For Bayesian approaches to auto-epistemology see van Fraassen (1985, 1995)[^fraassen-1985][^fraassen-1995]. For a ranking-theoretic approach, see chapter 9 in Spohn (2012)[^spohn-2012] as well as Hild (1998)[^hild-1998] and Spohn (2017b)[^spohn-2017b]. For a very different approach to combining qualitative notions from traditional epistemology with probabilistic notions see Moss (2013, 2018)[^moss-2013][^moss-2018], who defends the thesis that knowledge involves probabilistic contents.

## 3. Representations for Partial Belief

It is commonly held that belief is not just an all-or-nothing matter, but admits of degrees. Sophia may believe that Vienna is the capital of Austria to a greater degree than she believes that Vienna will be sunny tomorrow. If her degrees of belief have numerical–and not just ordinal–structure, she might be twice as sure of the former than the latter. Philosophers sufficiently impressed by examples of this sort orient their activity around the structure of “partial belief” rather than the all-or-nothing variety.

Although it is easy to generate plausible examples of partial beliefs, it is harder to say exactly what is meant by a degree of belief. An agent's degree of belief in $P$ may reflect their level of confidence in the truth of $P$, their willingness to assent to $P$ in conversation, or perhaps how much evidence is required to convince them to abandon their belief in $P.$ A venerable tradition, receiving classical expression in Ramsey (1926)[^ramsey-1926] and de Finetti (1937), holds that degrees of belief are most directly reflected in which bets regarding $P$ an agent is willing to accept. At least since Pascal (ca. 1658/2004), mainstream philosophical opinion has held that degrees of belief are well-modeled by probabilities (see Hacking (1975)[^hacking-1975] for a readable history). To this day, subjective, or ‘epistemic’, probability remains one of the dominant interpretations of the probability calculus.

A parallel tradition, though never as dominant, holds that degrees of belief are neither so precise, nor as definitely comparable as suggested by Pascal's probabilistic analysis. Keynes (1921)[^keynes-1921] famously proposed that degrees of belief may enjoy only an *ordinal* structure, which admits of qualitative, but not quantitative, comparison. Keynes even suggests that the strength of some pairs of partial beliefs cannot be compared at all.

Cohen (1980) traces another minority tradition to Francis Bacon's *Novum Organum* (1620/2000). On the usual probability scale a degree of belief of zero in some proposition implies maximal conviction in its negation. On the Baconian scale, a degree of belief of zero implies no conviction in either the proposition or its negation. Thus, the usual scale runs from “disproof to proof” whereas the Baconian runs from “no evidence, or non-proof to proof.” In the past few decades, Baconian probability has received increasing attention, resulting in theories approaching the maturity and sophistication of those in the Pascalian tradition (Spohn, 2012, Huber, 2019)[^huber-2019][^spohn-2012].

In this section we introduce several frameworks for representing partial belief, starting with what is by far the most prominent framework: subjective probability theory.

### 3.1 Subjective Probability Theory

Subjective probability theory, often going under the sobriquet ‘Bayesianism,’ is by far the dominant paradigm for modeling partial belief. The literature on the subject is by now very large. The summary provided here will, of necessity, be rather brief. For an article-length introduction see the entry on Bayesian epistemology, Easwaran (2011a, 2011b)[^easwaran-2011a][^easwaran-2011b] or Weisberg (2011)[^weisberg-2011]. For a book-length introduction see Earman (1992)[^earman-1992], Skyrms (2000)[^skyrms-2000], Hacking (2001)[^hacking-2001], Howson and Urbach (2006) or Huber (2018)[^huber-2018]. For an article-length introduction to Bayesian models of rational choice, see the entry on decision theory. For an approachable book-length introduction to the theory of rational choice see Resnik (1987)[^resnik-1987].

The heart of subjective probability theory is roughly the following:

1. There is a fundamental psychological attitude called *degree of belief*, sometimes *confidence* or *credence*, that can be represented by numbers in the $[0,1]$ interval.
2. The degrees of belief of rational agents satisfy the axioms of probability theory.
3. The degrees of belief of rational agents are *updated* by some flavor of probabilistic conditioning.

The first two principles are the synchronic requirements of Bayesian theory; the third principle concerns diachronic updating behavior. Most Bayesians would also agree to some version of the following principles, which link subjective probabilities with deliberation and action:

1. Possible states of the world (*outcomes*) are assigned a *utility*: a positive or negative real number that reflects the desirability or undesirability of that outcome.
2. Rational agents perform only those actions that maximize *expected* utility

What makes Bayesianism so formidable is that, in addition to providing an account of rational belief and its updating, it also provides an account of rational action and deliberation. No other theory can claim a developed, fine-grained account of all three of these aspects of belief. In the following we will briefly spell out some of the technical details of the Bayesian picture.

#### 3.1.1 The Formal Structure

Degrees of belief in the [0,1] interval are introduced to quantify the strength of belief attitudes. For our purposes, we will take propositions to be the objects of partial belief. It is also possible to assign degrees of belief to sentences in a formal language, but for the most part nothing hinges on the approach we choose (see Weisberg, 2011)[^weisberg-2011]. Accordingly, let $\mathbf{A}$ be a field of propositions over a set $W$ of possibilities. A function Pr: $\mathbf{A} \rightarrow \Re$ from $\mathbf{A}$ into the set of real numbers, $\Re$, is a (finitely additive and non-conditional) *probability measure* on $\mathbf{A}$ if and only if for all propositions $A, B$ in $\mathbf{A}$:

$$\begin{align} \tag{Positivity} \Pr(A) &\ge 0 \\ \tag{Unitarity} \Pr(W) &= 1 \\ \tag{Additivity} \Pr(A\cup B) &= \Pr(A) + \Pr(B) \text{ if } A\cap B = \varnothing \end{align}$$

A triple $\langle W, \mathbf{A}, \Pr\rangle$ satisfying these three principles is called a (finitely additive) *probability space*. From these principles it is possible to derive many illuminating theorems. For example, the degree of belief assigned to the contradictory proposition must equal zero. Furthermore, if $E$ entails $F,$ then $\Pr(E)\leq \Pr(F)$. Finally, for any proposition $E\in\mathbf{A}$ we have that $0\leq \Pr(E)\leq 1.$

Suppose that $\mathbf{A}$ is also closed under countable intersections (and is thus a *σ*-field). Suppose Pr additionally satisfies, for all propositions $A_{1}, \ldots A_{n}, \ldots$ in $\mathbf{A}$,

$$\begin{align} \tag{\(\sigma\)-Additivity} \Pr(\cup_{i=1}^\infty A_i) = \sum_{i=1}^\infty \Pr(A_i), \text{ if } A_{i} \cap A_{j} = \varnothing \text{ for } i \ne j. \end{align}$$

Then, Pr is a *σ*- or *countably additive* probability measure on $\mathbf{A}$ (Kolmogorov 1956, ch. 2, actually gives a different but equivalent definition; see e.g. Huber 2007a, sct. 4.1)[^kolmogorov-1956]. In this case $\langle W, \mathbf{A}, \Pr\rangle$ is a *σ*- or countably additive probability space.

Countable additivity is not as innocent as it looks: it rules out the possibility that any agent is indifferent over a countably infinite set of mutully exclusive possibilities. De Finetti (1970, 1972) famously argued that we ought to reject countable additivity since it is conceivable that God could pick out a natural number “at random” and with equal (zero) probability. For another example, suppose you assign 50% credence to the proposition $\neg B$ that not all ravens that will ever be observed are black. Let $\neg B_i$ be the proposition that the $i^{th}$ observed raven is the first non-black raven to appear. Then $\neg B = \cup_{i=1}^\infty \neg B_i.$ Countable additivity entails that for all $\epsilon>0$ there is a finite $n$ such that $p(\cup_{i=1}^n \neg B_i) = 1/2 -\epsilon.$ So you must be nearly certain that if not all ravens are black, the first non-black raven will appear among the first $n$ ravens. But is it really a requirement of *rationality* that you must be opinionated about when the first non-black raven must appear? The only way to assign equal probability to all $\neg B_i$ is to violate countable additivity by setting $p(\neg B_i)=0$ for all $i$. This solution has its own drawbacks. On all standard models of Bayesian update it will be impossible to become convinced that the $i^{th}$ raven is indeed non-black, even if you are looking at a white one. For more on countable additivity, see Chapter 13 in Kelly (1996)[^kelly-1996].

A probability measure Pr on $\mathbf{A}$ is *regular* just in case $\Pr(A) \gt 0$ for every non-empty or consistent proposition $A$ in $\mathbf{A}$. Let $\mathbf{A}^{\Pr}$ be the set of all propositions $A$ in $\mathbf{A}$ with $\Pr(A) \gt 0$. The *conditional* probability measure $\Pr(\cdot\mid -): \mathbf{A}\times \mathbf{A}^{\Pr} \rightarrow \Re$ on $\mathbf{A}$ (based on the non-conditional probability measure Pr on $\mathbf{A})$ is defined for all pairs of propositions $A$ in $\mathbf{A}$ and $B$ in $\mathbf{A}^{\Pr}$ by the ratio

$$\tag{5} \Pr(A\mid B) = \frac{\Pr(A\cap B)}{\Pr(B)}. $$

(Kolmogorov 1956, ch. 1, §4)[^kolmogorov-1956]. Conditionalization by $B$ restricts all possibilities to those compatible with $B$ and renormalizes by the probability of $B$ to ensure that unitarity holds. The domain of the second argument place of $\Pr(\cdot \mid -)$ is restricted to $\mathbf{A}^{\Pr}$, since the ratio $\Pr(A\cap B)/\Pr(B)$ is not defined if $\Pr(B) = 0$. Note that $\Pr(\cdot\mid B)$ is a probability measure on $\mathbf{A}$, for every proposition $B$ in $\mathbf{A}^{\Pr}$. Some authors take conditional probability measures $\Pr(\cdot, \text{given } -): \mathbf{A}\times(\mathbf{A}\setminus \{\varnothing \}) \rightarrow \Re$ as primitive and define (non-conditional) probability measures in terms of them as $\Pr(A) = \Pr(A$, given $W)$ for all propositions $A$ in $\mathbf{A}$ (see Hájek 2003)[^hájek-2003]. Conditional probabilities are usually assumed to be Popper-Rényi measures (Popper 1955, Rényi 1955, Rényi 1970, Stalnaker 1970, Spohn 1986)[^popper-1955][^rényi-1955][^rényi-1970][^spohn-1986][^stalnaker-1970]. Spohn (2012, 202ff) critizices Popper-Rényi measures for their lack of a complete dynamics, a feature already pointed out by Harper (1976)[^harper-1976], and for their lack of a reasonable notion of independence. Relative probabilities (Heinemann 1997, Other Internet Resources) are claimed not to suffer from these two shortcomings.

#### 3.1.2 Interpretations

What does it mean to say that Sophia’s subjective probability for the proposition that tomorrow it will be sunny in Vienna equals .55? This is a difficult question. Let us first answer a different one. How do we measure Sophia’s subjective probabilities? On one traditional account, Sophia’s subjective probability for $A$ is measured by her *betting ratio* for $A$, i.e., the highest price she is willing to pay for a bet that returns \$1 if $A$, and \$0 otherwise. On a slightly different account Sophia’s subjective probability for $A$ is measured by her *fair* betting ratio for $A$, i.e., that number $r = b/(a + b)$ such that she considers the following bet to be fair: \$$a$ if $A$, and \$$-b$ otherwise $(a, b \ge 0$ with inequality for at least one).

It need not be irrational for Sophia to be willing to bet you \$5.5 to \$4.5 that tomorrow it will be sunny in Vienna, but not be willing to bet you \$550 to \$450 that this proposition is true. She may even refuse a bet of \$200 to \$999. That is because there are other factors affecting her betting quotients than her degrees of belief. Sophia may be risk-averse, e.g. if she cannot risk blowing a \$200 dollar hole in her monthly budget. Others may be risk-prone. For example, gamblers in the casino are risk prone: they pay more for playing roulette than the fair monetary value according to reasonable subjective probabilities. That may be perfectly rational if the thrill of gambling is itself a compensation. Note that it does not help to say that Sophia’s fair betting ratio for $A$ is that number $r = b/(a + b)$ such that she considers the following bet to be fair: \$$1 - r = a/(a + b)$ if $A$, and $\$ -r = -b/(a + b)$ otherwise $(a, b \ge 0$ with inequality for at least one). Just as stakes of \$200 may be too high for the measurement to work, stakes of \$1 may be too low.

Another complication arises when the proposition itself is a matter of personal importance to the agent. Suppose Sophia would be very unhappy if the Freedom Party wins a majority in the next election, but she thinks it is very unlikely. Nevertheless, she may be willing to pay \$20 for a bet that pays \$100 if they do, and \$0 otherwise. Imagine that she is buying a kind of insurance policy against bitter disappointment. In this case, her betting ratio does not obviously reflect her degree of belief that the FPÖ will win.

Ramsey (1926)[^ramsey-1926] avoids the first difficulty by pricing bets in utility instead of money. He avoids the second difficulty by presupposing the existence of at least one “ethically neutral” proposition (a proposition whose truth or falsity is a matter of indifference) which the agent takes to be just as likely to be true as she takes it to be false. See Section 3.5 of the entry on interpretations of probability. Nevertheless, the bearing of the preceding examples is that fair betting ratios and subjective probabilities can easily come apart. Subjective probabilities are measured by, but not identical to, (fair) betting ratios. The latter are operationally defined and observable. The former are unobservable, theoretical entities that, following Eriksson & Hájek (2007), we take as primitive.

#### 3.1.3 Justifications

The theory of subjective probability does not accurately describe the behavior of actual human beings (Kahneman et. al., 1982)[^kahneman-1982]. It is a normative theory intended to tell us how we *ought* to govern our epistemic lives. *Probabilism* is the thesis that a person’s degrees of belief *ought* to satisfy the axioms of probability. But why should they?

The traditional answer is that an agent that violates the axioms of probability opens herself up, in some sense, to a system of bets that guarantee a sure loss. Answers of this flavor are called *Dutch Book* arguments. The *pragmatic* version of the argument posits a tight connection between degrees of belief and betting behavior. The argument concludes by proving a theorem to the effect that an agent would enter into a system of bets guaranteeing a sure loss iff her degrees of belief violate the probability calculus. But, as we have seen, there are reasons to doubt that the connection between degrees of belief and betting behavior is really so tight as required by the pragmatic Dutch book argument. That renders the argument less convincing. The *depragmatized* version of the argument posits a connection between degrees of belief and dispositions to consider systems of bets fair, without necessarily entering into them (Armendt 1993 Christensen 1996, Ramsey 1926, Skyrms 1984)[^armendt-1993][^christensen-1996][^ramsey-1926][^skyrms-1984]. It concludes by proving an essentially identical theorem to the effect that an agent would consider fair a system of bets guaranteeing a sure loss iff her degrees of belief violate the probability calculus. The depragmatized Dutch Book Argument is a more promising justification for probabilism. See, however, Hájek (2005; 2008)[^hájek-2005][^hájek-2008]. For a much more extensive discussion see the entry on Dutch book arguments.

Some epistemologists find Dutch book arguments to be unconvincing either because they disavow any suitable connection between degrees of belief and betting quotients, or they deny that any facts about something so pragmatic as betting could have normative epistemic force. Joyce (1998)[^joyce-1998] attempts to vindicate probabilism by considering the *accuracy* of degrees of belief. The basic idea here is that a degree of belief function is defective if there exists an alternative degree of belief function that is at least as accurate in each, and strictly more accurate in some, possible world. The accuracy of a degree of belief $b(A)$ in a proposition $A$ in a world $w$ is identified with the distance between $b(A)$ and the truth value of $A$ in $w$, where 1 represents truth and 0 represents falsity. For instance, a degree of belief up to 1 in a true proposition is more accurate, the higher it is — and perfectly accurate if it equals 1. The overall accuracy of a degree of belief function $b$ in a world $w$ is then determined by the accuracy of the individual degrees of belief $b(A)$. Joyce is able to prove that, given some conditions on how to measure distance or inaccuracy, a degree of belief function obeys the probability calculus if and only if there exists no alternative degree of belief function that is at least as accurate in each, and strictly more accurate in some, possible world (the only-if-part is not explicitly mentioned in Joyce 1998, but present in Joyce 2009)[^joyce-1998][^joyce-2009]. Therefore, degrees of belief should obey the probability calculus.

Bronfman (2006, Other Internet Resources) observes that Joyce’s conditions on measures of inaccuracy do not determine a single measure, but rather a whole family of inaccuracy measures. All of Joyce’s measures agree that an agent whose degree of belief function violates the probability axioms should adopt a probabilistic degree of belief function which is at least as accurate in each, and more accurate in some, possible world. However, these measures may differ in their recommendation as to which particular probability measure the agent should adopt. In fact, for each possible world, following the recommendation of one measure will leave the agent less accurate according to some other measure. Why, then, Bronfman objects, should the ideal doxastic agent move from her non-probabilistic degree of belief function to a probability measure in the first place? Other objections are articulated in Maher (2002)[^maher-2002] and, more recently, in Easwaran and Fitelson (2012). These are addressed by Joyce (in 2009 and in 2013 (Other Internet Resources)) and Pettigrew (2013, 2016)[^pettigrew-2013][^pettigrew-2016]. Leitgeb and Pettigrew (2010a; 2010b) present conditions that narrow down the set of measures of inaccuracy to the so-called quadratic scoring rules. This enables them to escape Bronfman’s objection. For a detailed treatment, see the entry on epistemic utility arguments for probabilism, §5.2.1.

For alternative justifications of probabilism see Cox (1946)[^cox-1946] and the representation theorem of measurement theory (Krantz et al., 1971)[^krantz-1971]. For criticism of the latter see Meacham & Weisberg (2011)[^weisberg-2011]. For a recent justification of probabilism from partition invariance see Leitgeb (forthcoming).

#### 3.1.4 Update Rules

Probabilism imposes synchronic conditions on degrees of belief. But how should subjective probabilities be updated when new information is received? Update rules are *diachronic* conditions that tell us how to revise our subjective probabilities when we receive new information. There are two standard update rules. Strict conditionalization applies when the new information receives the maximal degree of belief. Jeffrey conditionalization allows for the situation in which no proposition is upgraded to full certainty when new information is acquired. In the first case, probabilism is extended by

**Strict Conditionalization** If $\Pr(\cdot)$ is your subjective probability at time $t$, and if between $t$ and $t^\prime$ you become certain of $A \in \mathbf{A}^{\Pr}$ and no logically stronger proposition, then your subjective probability at time $t^\prime$ should be $\Pr(\cdot \mid A)$.

Strict conditionalization says that, so long as $A$ has positive prior probability, the agent’s new subjective probability for a proposition $B$ after becoming certain of $A$ should equal her old subjective probability for $B$ conditional on $A$. It is by far the most standard model of partial belief update.

The discerning reader may object that there is a suppressed *ceteris paribus* clause in our statement of strict conditionalization. On the intended interpretation, the only *external* change to your subjective belief state between $t$ and $t^\prime$ is that you become certain of $A$. Moreover, you do not forget anything, fall into doubts about prior beliefs, or acquire any new concepts. Finally, there is no time $t^{\prime\prime}$ between $t$ and $t^{\prime}$ by which your degree of belief in $A$ is promoted to 1, but before your other subjective probabilities have been able to “catch up”. If there were, you would be probabilistically incoherent between $t^{\prime\prime}$ and $t^{\prime}.$ On the intended interpretation, although you acquire the information between $t$ and $t^{\prime}$, your subjective probabilities remain unchanged until $t^{\prime}$, at which point the new information is assimilated holus-bolus. These sorts of considerations apply equally to the other forms of conditioning we discuss in this article, including those in Section 3.5. For a good discussion of the difficulties in interpreting conditionalization, see Spohn (2012, p. 186–8).

What if new information does not render any proposition certain, but merely changes the subjective probability of some propositions? Jeffrey (1983a)[^jeffrey-1983a] gives the most widely accepted answer to this question. Roughly, Jeffrey conditionalization says that the ideal doxastic agent should keep fixed her “inferential beliefs,” that is, the probabilities of all hypotheses conditional on any evidential proposition.

**Jeffrey Conditionalization** Suppose that $\Pr(\cdot)$ is your subjective probability at time $t$ and that between $t$ and $t^\prime$ your subjective probabilities in the partition $\{A_i : 1\leq i \leq n \}\subseteq \mathbf{A}^{\Pr}$ (and no finer partition) change to $p_{i} \in [0,1]$ with $\sum_{i} p_{i} = 1$. Then, your subjective probability at time $t^\prime$ should be $\Pr^\prime(\cdot) = \sum_{i} \Pr(\cdot \mid A_{i}) p_{i}$.

Jeffrey conditionalization says that the agent’s new subjective probability for $B$, after her subjective probabilities for the elements of the partition have changed to $p_{i}$, should equal the weighted sum of her old subjective probabilities for $B$ conditional on the $A_{i}$, where the weights are the new subjective probabilities $p_{i}$ for the elements of the partition.

Why should we update our subjective probabilities according to strict or Jeffrey conditionalization? Dutch-book style arguments for strict conditionalization are given in Teller (1973)[^teller-1973] and Lewis (199) and extended to Jeffrey conditionalization in Armendt (1980)[^armendt-1980]. For more, see Skyrms (1987, 2006)[^skyrms-1987][^skyrms-2006]. Leitgeb and Pettigrew (2010b) present an accuracy argument for strict conditionalization (see also Greaves and Wallace, 2006)[^greaves-2006] as well as an argument for an alternative to Jeffrey conditionalization. For an overview, see the entry on epistemic utility arguments for probabilism.

Other philosophers have provided arguments against strict (and Jeffrey) conditionalization: van Fraassen (1989)[^fraassen-1989] holds that rationality does not require the adoption of a particular update rule (but see Hájek, 1998 and Kvanvig, 1994)[^hájek-1998][^kvanvig-1994]. Arntzenius (2003)[^arntzenius-2003] uses, among others, the “shifting” nature of self-locating beliefs to argue against strict conditionalization, as well as against van Fraassen’s *reflection* principle (see van Fraassen 1995; for an illuminating discussion of the reflection principle and Dutch Book arguments see Briggs 2009a)[^briggs-2009a][^fraassen-1995]. The second feature used by Arntzenius (2003)[^arntzenius-2003], called “spreading”, is not special to self-locating beliefs. Weisberg (2009)[^weisberg-2009] argues that Jeffrey conditionalization cannot handle a phenomenon he terms *perceptual undermining*. See Huber (2014)[^huber-2014] for a defense of Jeffrey conditionalization.

For our purposes it is important to point out that conditional probability is always a lower bound for the probability of the material conditional. In other words, $$p(H|E)\leq p(E\rightarrow H),$$ whenever $p(E)>0$. We can see this as a quantitative version of the qualitative principle of Conditionalization we discussed in Section 2.1.1. However confident a Bayesian agent becomes in $H$ after updating on $E,$ she must have been at least as confident that $H$ is a material consequence of $E$. Popper and Miller (1983) took this observation to be “completely devastating to the inductive interpration of the calculus of probability.” For the history of the Popper-Miller debate see Chapter 4 in Earman (1992)[^earman-1992]. A similar property can be demonstrated for Jeffrey conditioning (Genin 2017, Other Internet Resources).

#### 3.1.5 Ignorance

Subjective probability theory models ignorance with respect to a proposition $A$ by assigning probability of .5 to $A$ and its complement $\neg A$. More generally, an agent with subjective probability Pr is said to be *ignorant* with respect to the partition $\{A_{1},\ldots,A_{n}\}$ if and only if $\Pr(A_{i}) = 1/n$. The *Principle of Indifference* requires a doxastic agent to distribute her subjective probabilities in this fashion whenever, roughly, the agent lacks evidence of the relevant kind. Leitgeb and Pettigrew (2010b) give an accuracy argument for the principle of indifference. However, the principle leads to contradictory results if the partition in question is not held fixed. For a simple example, suppose that Sophia is ignorant about the color of a certain marble. Then, she must be nearly certain that it is not Blue. In this case, ignorance about one thing entails that she is very opinionated about another. But presumably she is also ignorant about whether or not the color is Blue. For more on this, see the discussion of *Bertrand’s paradox* in Kneale (1949)[^kneale-1949] and the entry on interpretations of probability, §3.1. A more cautious version of the principle of indifference, also applicable if the partition contains a countable infinity of elements, is the *principle of maximum entropy*. It requires the agent to adopt one of those probability measures Pr as her degree of belief function over (the *σ*-field generated by) the countable partition $\{A_{i}\}$ that maximize the quantity $-\sum_{i} \Pr(A_{i}) \log \Pr(A_{i})$. The latter is known as the *entropy* of Pr with respect to the partition $\{A_{i}\}$. See Paris (1994)[^paris-1994].

Suppose Sophia does not know much about wine. By the principle of indifference, her degree of belief that an Austrian Schilcher is a white wine and her degree of belief that it is a red wine should both be .5. Contrast this with the following case. Sophia is certain that a particular coin is fair, i.e. that the objective chance of the coin landing heads and the objective chance of the coin landing tails are both exactly .5. The *principal principle* (Lewis, 1980)[^lewis-1980] requires roughly that, conditional on the objective chances, one’s subjective probability should equal the objective probability (see Briggs, 2009b)[^briggs-2009b]. By the principal principle, her degree of belief that the coin will land heads on the next spin should also be .5. Although Sophia’s subjective probabilities are alike in these two scenarios, there is an important difference. In the first case a subjective probability of .5 represents complete ignorance. In the second case it represents certainty about objective chances.

Examples like these suggest that subjective probability theory is not an adequate account of partial belief because it cannot distinguish between total ignorance and knowledge, or at least certainty, about chances. We discuss potential responses to this objection in Section 3.2

#### 3.1.6 Deliberation and Action

One of the signal advantages of the Bayesian model of partial belief is that it is ready-made to plug into a prominent model of practical deliberation. Decision theory, or rational choice theory, is too large and sprawling a subject to be effectively covered here, although it will be presented in cursory outline. For an excellent introduction, see Thoma (2019)[^thoma-2019] and the entry on decision theory. For our purposes, it is enough to note that a well-developed theory exists and that no comparable theory exists for alternative models of belief. However, recent work such as Lin (2013)[^lin-2013] and Spohn (2017a, 2019)[^spohn-2017a] may remedy that inadequacy in the case of qualitative belief.

Suppose you would like to make a six egg omelet. You’ve broken 5 fresh eggs into a mixing bowl. Rooting around your fridge, you find a loose egg of uncertain provenance. If you are feeling lucky you can break the suspect egg directly into the mixing bowl; if you are wary of the egg, you might break it into a saucer first and incur more dishwashing.

There are four essential ingredients to this sort of decision-theoretic situation. There are *outcomes*, over which we have defined *utilities* measuring the desirability of the outcome. In the case of the omelet the outcomes are a ruined omelet or a 5–6 egg omelet, with or without extra washing. There are *states*–usually unknown to and out of the control of the actor–which influence the outcome of the decision. In our case the states are exhausted by the possible states of the suspect egg: either good or rotten. Finally, there are *acts* which are under the control of the decision maker. In our case the acts include breaking the egg into the bowl or the saucer. Of course, there are other conceivable acts: you might throw the suspect egg away and make do with a 5-egg omelet; you might even flip a coin to decide what to do. We omit these for the sake of simplicity.

To fit this into the framework of partial belief we assume that the set of acts $A_1, A_2, \ldots, A_n$ partition $W$. We also assume the set of states $S_1, S_2, \ldots, S_m$ partition $W$. We assume that the subjective probability function assigns a probability to every state given every act. We assume that acts and states are logically independent, so that no state rules out the performance of any act. Finally, we assume that given a state of the world $S_j$ and an act $A_i$ there is exactly one outcome $O_{ij}$ which is assigned a utility $U(O_{ij})$. The ultimate counsel of rational choice theory is that agents ought to perform only those acts that maximize *expected* utility. The expected utility of an act is defined as:

$$ \text{EU}(A_i) = \sum_{j=1}^m \Pr_{A_i}(S_j)U(O_{ij}),$$

where $\Pr_{A_i}(S_j)$ is roughly how likely the agent considers $S_j$ given that she has performed act $A_i$. Difficulties about how this quantity should be defined give rise to the schism between evidential and causal decision theory (see Section 3.3 in Thoma, 2019)[^thoma-2019]. However, in many situations, including the dilemma of the omelet, the act chosen does not affect the probabilities with which states obtain. This is called “act-state independence” in the jargon of rational choice theory. In cases of act-state independence there is broad consensus that $\Pr_{A_i}(S_j)$ should be equal to the unconditional degree of belief $\Pr(S_j)$.

Central to the literature on decision theory are a number of representation theorems showing that every agent with qualitative preferences satisfying a set of rationality postulates can be represented as an expected utility maximizer (von Neumann and Morgenstern, 1944 and Savage, 1972)[^savage-1972][^neumann-1944]. These axioms are controversial, and are subject to intuitive counterexamples. Allais (1953)[^allais-1953] and Ellsberg (1961)[^ellsberg-1961] give examples in which seemingly rational agents violate the rationality postulates and therefore cannot, even in principle, be represented as expected utility maximizers. For more on the challenge of Ellsberg and Allais, see the entry on descriptive decision theory, §2.1, as well as Buchak (2013)[^buchak-2013].

### 3.2 Imprecise Probabilities

Consider the following modification of the two examples from section 3.1.5. In the first case, Sophia is presented with a weathered and irregularly shaped coin–it was just discovered in an archeological dig of an ancient city. By probabilism, Sophia must have a *precise* real-valued credence that it will land heads on the next spin. By the principle of indifference, her credence in *Heads* must be precisely .5. In the second case, she is presented with a Euro coin that she is certain is fair–this has been confirmed by extensive experimentation. Probabilism and the principal principle require her credence in *Heads* to be precisely .5 in this case as well. As we have already seen, there is something unsatisfactory about treating ignorance (in the first case) in the same way as certainty about chances (in the second case).

There are several different ways of spelling out what is wrong with this situation. In the case of the ancient coin, Sophia has a precise credence based only on some vague and imprecise information. In the case of the Euro, she has a precise attitude based on precise information. The basic intuition here is that it is bizzarre to require, as a matter of *rationality*, that Sophia have a precise attitude when her evidence is so imprecise. Sturgeon (2008)[^sturgeon-2008] suggests that evidence and attitude must “match in character,” i.e. sharp evidence warrants a sharp attitude and imprecise evidence warrants only an imprecise attitude. According to the “character matching” thesis, rationality requires that Sophia have an *imprecise* attitude toward the ancient coin.

Joyce (2005)[^joyce-2005] articulates the difficulty in a different way. He suggests that there is an important difference between the *weight* and the *balance* of the evidence. In the case of the ancient coin, the evidence is balanced (by symmetry) but so scanty that it has no weight. In the case of the Euro, the evidence is weighty (since there is so much of it) and balanced because it favors both heads and tails equally. Joyce criticizes precise probabilism for its inability to represent the distinction between weight and balance of evidence. Skyrms (2011)[^skyrms-2011] and Leitgeb (2014)[^leitgeb-2014] argue that this distinction *is* represented: beliefs that reflect weighty evidence are more *resilient* (Skyrms) or *stable* (Leitgeb) under update. A few trials with the ancient coin might change Sophia’ credences dramatically, but not so for the Euro.

The question takes on a different character when we consider its consequence for decision making. According to the standard theory, a utility-maximizing Bayesian must find at least one side of any bet attractive. It is straightforward to check that if a bet that costs $\$\ell$ and pays out $\$w$ has negative expected utility, then the other side of the bet, that costs $\$w$ and pays out $\$\ell$, has positive expected utility. Since her credences in both cases are the same, whatever bet Sophia accepts on the next spin of the Euro, she must also accept on the ancient coin. So even though her beliefs about the Euro are more stable, this difference is not reflected in her betting behavior. Yet intuitively, it seems reasonable to refuse to bet on the ancient coin at all. A bet on the Euro is *risky*: the outcome of the spin is uncertain, but there is no uncertainty about the chance with which each outcome occurs. A bet on the ancient coin is *ambiguous*: the outcome of the spin is uncertain and there is significant uncertainty about the chance with which each outcome occurs. Many seemingly rational people take account of this distinction in their decision making (see the discussion of Ellsberg decisions in the entry on imprecise probabilities, §2.1). However, this distinction cannot be represented in the standard theory (see Buchak 2013)[^buchak-2013].

Imprecise probabilists (van Fraasen, 1990, Levi 1974)[^levi-1974] respond to these difficulties by denying that an agent’s credences are adequately described by a single probability function. Instead, they propose that a belief state is better represented by a *set* of probability functions. This set represents a kind of “credal committee,” where each member represents a way of precisifying the probability of every proposition. When new information arrives, each member updates by conditioning in the usual way. Levi requires that the credal set be closed under convex combinations. In other words, if $p,q$ are members of your credal set then $\lambda p + (1-\lambda) q$ must also be a member of your credal set, for all $\lambda \in [0,1]$. According to Levi, convex combinations of $p,q$ are “potential resolutions of the conflict” between them and “one should not preclude potential resolutions when suspending judgement between rival systems” (Levi, 1980)[^levi-1980]. However, resolving conflicts in this way leads to some unintuitive consequence. For example, if $p,q$ agree that two events are probabilistically independent, the same is not true of their convex combinations. Furthermore, if all members of the credal committee agree that some coin is biased (because it is bent) but not on the direction of the bias, it is unintuitive to require that some committee member believe that the coin is fair. For more on how to aggregate the opinions of agents with probabilistic credences, see Dietrich and List (2016) and section 10.4 in Pettigrew (2019)[^pettigrew-2019].

Whether or not we accept Levi’s convexity requirement, sets of probability functions give us the resources to distinguish ignorance from certainty about chances. If an agent is certain of an objective chance, every element of her credal committee will assign the same probability. However, if she is ignorant with respect to some proposition, her credal set will admit values in some interval $[a, b] \subseteq$ [0,1]. In her total ignorance about the ancient coin, Sophia might admit any value in the interval [0,1] for the proposition that it will land heads on the next spin. But since she knows that the Euro is fair, every member of her credal committee assigns .5 to the corresponding proposition. If we similarly redefine expected utility, then a bet on the Euro that costs \$1 and pays out \$2 if it lands heads has positive expected utility. But a similar bet on the ancient coin has expected utility ranging from -\$1 to \$2. This distinction allows for different attitudes towards the two bets.

For a detailed exposition of imprecise probability theory, see Levi (1980)[^levi-1980], van Fraassen (1990)[^fraassen-1990], Walley (1991)[^walley-1991] and Kyburg and Teng (2001). For excellent introductions see Mahtani (2019)[^mahtani-2019], as well as the entry on imprecise probability, §2.7, and its technical and historical appendices. See Weichselberger (2000)[^weichselberger-2000] for an approach that avoids sets of probability functions by assigning credal intervals $[a,b]\subseteq[0,1]$ directly to propositions. For a sophisticated recent view on which the contents of beliefs are sets of probability functions, see Moss (2018)[^moss-2018].

### 3.3 Dempster-Shafer Theory

Dempster-Shafer (DS) belief functions (Dempster 1968, Shafer 1976)[^dempster-1968][^shafer-1976] can also be understood as an attempt to formally distinguish risk from ambiguity. Like probability functions, DS belief functions are real-valued functions $ \Bel: \mathbf{A} \rightarrow \Re$ satisfying Positivity and Unitarity. But whereas probability functions are additive, DS belief functions are only *Super-additive*, i.e., for all propositions $A, B$ in $\mathbf{A}$:

$$\tag{6} \Bel(A) + \Bel(B) \le \Bel(A\cup B) \text{ if } A\cap B = \varnothing . $$

Although $0\leq\Bel(A)\leq 1$ for all $A\in\mathbf{A}$, the agent’s degree of belief in $A$ and her degree of belief in $\neg A$ need not sum to 1.

According to one interpretation (Haenni & Lehmann 2003)[^haenni-2003], the number $\Bel(A)$ represents the strength with which $A$ is supported by the agent’s knowledge or belief base. It may well be that this base supports neither $A$ nor its complement $\neg A$. Since Sophia knows little about the ancient coin, her belief base will support neither the proposition $H_a$, that it will land heads, nor the proposition $T_a$, that it will land tails. However, Sophia may well be certain that it will not land on its edge. Hence Sophia’s DS belief function $\Bel$ will be such that $\Bel(H_a) = \Bel(T_a) = 0$ while $\Bel(H_a \cup T_a) = 1$. On the other hand, Sophia is certain that the Euro coin is fair. Therefore, if $H_e,T_e$ are the propositions that the Euro will land heads and tails respectively, her $\Bel$ will be such that $\Bel(H_e) = \Bel(T_e) = .5$ and $\Bel(H_e\cup T_e) = 1$. In this way, the theory of DS belief functions can distinguish between uncertainty and ignorance about chances. Indeed,

$$ \rI(\{A_{i}\}) = 1 - \Bel(A_{1}) - \ldots - \Bel(A_{n}) -\ldots $$

can be seen as a measure of the agent’s ignorance with respect to the countable partition $\{A_{i}\}$. On this definition, Sophia is maximally ignorant about the outcome of the next spin of the ancient coin and minimally ignorant about the Euro.

Every proposition $A$ can be seen as dividing the agent’s knowledge base into three mutually exclusive and jointly exhaustive parts: a part that speaks in favor of $A$, a part that speaks against $A$ (i.e., in favor of $\neg A $), and a part that speaks neither in favor of nor against $A$. $\Bel(A)$ quantifies the part that supports $A, \Bel( \neg A)$ quantifies the part that supports $\neg A$, and I$(\{A, \neg A\}) = 1 - \Bel(A) - \Bel(\neg A)$ quantifies the part that supports neither $A$ nor $\neg A$.

We can understand the relation to subjective probability theory in the following way. Subjective probabilities require the ideal doxastic agent to divide her knowledge base into two mutually exclusive and jointly exhaustive parts: one that speaks in favor of $A$, and one that speaks against $A$. That is, the neutral part has to be distributed among the positive and negative parts. Subjective probabilities can thus be seen as DS belief functions without ignorance. (See Pryor (2007, Other Internet Resources) for a model of doxastic states that includes probability theory and Dempster-Shafer theory as special cases.)

A DS belief function induces a *plausibility* function $\rP: \mathbf{A} \rightarrow \Re$, by setting

$$ \rP(A) = 1 - \Bel(\neg A), $$

for all $A$ in $\mathbf{A}$. Degrees of plausibility quantify that part of the agent’s knowledge or belief base which is compatible with $A$, i.e., the part that supports $A$ and the part that supports neither $A$ nor $ \neg A$. Dempster and Shafer call the plausibility of $A$ its *upper probability.* Indeed, one can interpret the interval $ [\Bel(A), P(A)]$ as the interval of probabilities that the agent assigns to the proposition $A$. In our running example, Sophia assigns the interval $[0,1]$ to the proposition that the ancient coin will land heads and $[.5,.5]$ to the proposition that the Euro will land heads.

Dempster-Shafer theory is more general than the theory of subjective probability in the sense that the latter requires additivity, whereas the former requires only super-additivity. However, most authors agree that DS theory is not as general as imprecise probability theory. The reason is that DS belief functions can be represented as convex sets of probabilities. More precisely, for every DS belief function $\Bel$ there is a convex set of probabilities $\mathcal{P}$ such that $\Bel(A)=\min \{ p(A) : p \in \mathcal{P}\}$ and $P(A) = \max \{ p(A) : p\in\mathcal{P}\} $ (Walley 1991)[^walley-1991]. As not every convex set of probabilities can be represented as a DS belief function, sets of probabilities arguably provide the most general framework we have come across so far.

How are DS belief functions reflected in decision making? One interpretation of DS theory, called the *tranferable belief model* (Smets and Kennes, 1994)[^smets-1994], distinguishes between two mental levels: the credal level, where one entertains and quantifies various beliefs, and the pignistic level, where one uses those beliefs for decision making. Its twofold thesis is that (fair) betting ratios should indeed obey the probability calculus, but that degrees of belief, being different from (fair) betting ratios, need not. It suffices that they satisfy the weaker DS principles. The idea is that whenever one is forced to bet on the pignistic level, the degrees of belief from the credal level are used to calculate (fair) betting ratios that satisfy the probability axioms. These in turn are then used to calculate the agent’s expected utility for various acts.

One of the chief novelties of Dempster-Shafer theory is its modeling of belief update, which we do not cover here. For a good introduction to this and other aspects of Dempster-Shafer theory, see Section 5.4 in Kyburg and Teng (2001). For a Dutch Book-style argument for Dempster-Shafer theory, see Paris (2001)[^paris-2001]. For an accuracy-style argument see Williams (2012)[^williams-2012].

### 3.4 Possibility and Plausibility Theory

Let us summarize the accounts we have dealt with so far. Subjective probability theory requires degrees of belief to be additive. For any disjoint $A,B$ in $\mathbf{A}$, a subjective probability function Pr: $\mathbf{A} \rightarrow \Re$ must satisfy:

$$ \Pr(A) + \Pr(B) = \Pr(A\cup B). $$

Dempster-Shafer theory only requires degrees of belief to be super-additive. For any disjoint $A,B$ in $\mathbf{A}$, a DS belief function Bel: $\mathbf{A} \rightarrow \Re$ must satisfy:

$$ \Bel(A) + \Bel(B) \le \Bel(A\cup B). $$

But there are many other ways that we could have weakened the additivity axiom. Possibility theory (Dubois and Prade, 1988)[^dubois-1988] requires degrees of belief to be *maxitive* and hence sub-additive. For any $A,B \in \mathbf{A}$, a possibility measure $\Pi : \mathbf{A} \rightarrow \Re$ must satisfy:

$$ \begin{align} \Pi(\varnothing) & = 0;\\ \Pi(W) & =1;\\ \max\{\Pi(A), \Pi(B)\} & = \Pi(A \cup B); \end{align} $$

which entails that

$$ \Pi(A)+\Pi(B) \geq \Pi(A\cup B).$$

The idea is that a proposition is at least as possible as each of the possibilities it comprises, and no more possible than the “most possible” possibility. The dual notion of a *necessity measure* $\Nu : \mathbf{A} \rightarrow \Re$ is defined for all $A$ in $\mathbf{A}$ by

$$ \Nu(A) = 1 - \Pi(\neg A), $$

which implies that

$$ \Nu(A\cap B) = \min\{\Nu(A), \Nu(B)\}. $$

Although the agent’s doxastic state in possibility theory is completely specified by either *Π* or $\Nu$, the agent’s epistemic attitude towards a particular proposition $A$ is only jointly specified by $\Pi(A)$ and $\Nu(A)$. The reason is that, in contrast to probability theory, $\Pi(W \setminus A)$ is not determined by $\Pi(A)$.

Possiblity theory is inspired by fuzzy set theory (Zadeh, 1978)[^zadeh-1978]. The latter is designed to accommodate linguistic phenomena of *vagueness* (see Égré & Barberousse 2014, Raffman 2014, Williamson 1994, Field 2016, as well as the entry on vagueness)[^égré-2014][^raffman-2014][^williamson-1994]. Vagueness arises for predicates like “tall” for which there are extreme, paradigmatic and borderline cases. We might represent this phenomenon formally by a membership function $\mu_{T}: H \rightarrow [0,1]$, where $\mu_{T}(h)$ is the degree to which person of height $h \in H$ belongs to the set of tall people $T$. Then, $\mu^{-1}(1)$ is the set of all tall heights; $\mu^{-1}(0)$ is the set of all short heights; and $\cup_{r\in(0,1)}\mu^{-1}(r)$ is the set of all borderline heights. Since many distinct heights are tall, it is clear why such membership functions should not satisfy Additivity.

Fuzzy set theory interprets $\mu_{T}(178cm)$ as the degree to which the vague statement “someone measuring 178cm is tall” is *true*. Degrees of truth belong to the philosophy of language. They do not (yet) have anything to do with degrees of belief, which belong to epistemology. The epistemological thesis of possibility theory is that your subjective degrees of possibility should reflect semantic facts about degree of membership. Suppose you learn that Sophia is tall. Then, your degree of possibility for the statement “Sophia is 178cm” should equal $\mu_{T}(178\text{cm})$. That may handle borderline heights elegantly, but it has somewhat unintuitive consequences at the extremes. Since, presumably, $\mu_T(190\text{cm})=\mu_T(210\text{cm})=1$, you must find it maximally possible that Sophia is 190 and 210cm tall.

In “chancy” situations, possibility theory can only make very course-grained distinctions. Since Sophia is certain that the Euro coin will not land on its edge $\Pi(H\cup T)=\Pi(W)$, she must have $\Pi(H)=1$ or $\Pi(T)=1.$ The most natural way to model her attitude is to set $\Pi(H)=\Pi(T)=1$. There is no way of expressing a partial attitude towards both heads and tails, since these are both maximally possible.

An even more general framework than possibility or Dempster-Shafer theory is provided by Halpern’s *plausibility measures* (Halpern 2003)[^halpern-2003]. These are functions Pl:$\mathbf{A} \rightarrow \Re$ such that for all $A, B$ in $\mathbf{A}$:

$$\begin{align} \Pl(\varnothing) &= 0; \\ \Pl(W) &= 1;\\ \Pl(A) &\le \Pl(B) \text{ if } A \subseteq B. \end{align}$$

With the exception of sets of probabilities, every model of partial belief that we have seen in this section is a special case of plausibility measures. While it is fairly uncontroversial that partial belief functions should obey Halpern’s plausibility calculus, it is questionable whether his minimal principles capture anything of epistemic interest. The resulting epistemology is, in any case, very thin. It should be noted, though, that Halpern does not intend plausibility measures to provide a complete epistemology, but rather a general framework to study more specific accounts.

For more on possibility theory see Huber (2009)[^huber-2009] and Halpern (2003)[^halpern-2003]. See the latter especially for approaches to conditional possibility measures. For a helpful taxonomy of models of partial belief see this appendix to the entry on inductive logic.

### 3.5 Ranking Theory

Ranking theory (Spohn 1988, 1990 and especially 2012)[^spohn-1988][^spohn-1990][^spohn-2012] assigns numerical degrees of *disbelief* directly to possibilities in $W$. A *pointwise ranking function* $\kappa : W \rightarrow \bN\cup \{\infty \}$ assigns a natural number (or $\infty$) to each possible world in $W$. These numbers represent the degree of disbelief you assign to each possibility. Equipped with a pointwise ranking function, we can generate a *numbered partition* of $W$:

$$ \kappa^{-1}(0), \kappa^{-1}(1), \kappa^{-1}(2), \ldots ,\kappa^{-1}(\infty). $$

The cell $\kappa^{-1}(\infty)$ is the set of possibilities which are maximally disbelieved. The cell $\kappa^{-1}(n)$ is the set of possibilities which are disbelieved to degree $n$. Finally, $\kappa^{-1}(0)$ contains the possibilities which are not disbelieved (although this does not mean that they are believed). Except for $\kappa^{-1}(0)$, the cells $\kappa^{-1}(n)$ may be empty. Since one cannot consistently disbelieve everything, the first cell must not be empty.

A pointwise ranking function *κ* induces a *ranking function* $\varrho : \mathbf{A} \rightarrow \bN\cup \{\infty \}$ on the field $\mathbf{A}$ by setting,

$$ \varrho(A) = \min\{\kappa(w): w \in A\}, $$

for each $A \in \mathbf{A}$. In other words: a set of worlds is only as disbelieved as its most plausible member. By convention, we set $\varrho(\varnothing)=\infty$. This entails that ranking functions are (finitely) *minimitive* and hence super-additive. In other words, for all $A, B$ in $\mathbf{A}$,

$$ \varrho(A\cup B) = \min\{\varrho(A), \varrho(B)\}. $$

Alternatively, we can characterize ranking functions as those functions $\varrho: \mathbf{A}\rightarrow \mathbf{N}\cup\{\infty\}$ satisfying

$$\begin{align} \varrho(W) &= 0; \\ \varrho(\varnothing) &= \infty; \\ \varrho(A\cup B) &= \min \{\varrho(A), \varrho(B)\}, \end{align}$$

for all $A,B\in \mathbf{A}.$ The first axiom says that no agent should disbelieve the tautological proposition $W$. The second says that every agent should maximally disbelieve the contradictory prosition. Intuitively, the final axiom says that a disjunction $A \cup B$ should be disbelieved just in case both disjuncts are disbelieved. However, the meaning of the final axiom is not exhausted by this gloss (see Section 4.1 in Huber, 2020)[^huber-2020].

As stated above, the third axiom is called *finite minimitivity.* Just as in probability theory, it can be strengthened to countable unions, resulting in *countably* minimitive ranking functions. Unlike probability theory, finite minimitivity can also be strenghtened to arbitrary unions, resulting in *completely* minimitive ranking functions. See Huber (2006)[^huber-2006] for conditions under which a ranking function defined on a field of propositions induces a pointwise ranking functions on the underlying set of possibilities.

The number $\varrho(A)$ represents the agent’s degree of disbelief in the proposition $A$. If $\varrho(A) \gt 0$, the agent disbelieves $A$ to a positive degree. Therefore, on pain of inconsistency, she cannot also disbelieve $\neg A$ to a positive degree. In other words, for every proposition $A$ in $\mathbf{A}$, at least one of $A, \neg A$ has to be assigned rank 0. If $\varrho(A) = 0$, the agent does not disbelieve $A$ to a positive degree. However, this does not mean that she believes $A$ to a positive degree $-$ the agent may suspend judgment and assign rank 0 to both $A$ and $\neg A$. So belief in a proposition is characterized by disbelief in its negation.

For each ranking function *ϱ* we can define a corresponding *belief function* $\beta : \mathbf{A} \rightarrow \mathbf{Z}\cup \{\pm \infty \}$ by setting $ \beta(A) = \varrho(\neg A) - \varrho(A) $ for all $A$ in $\mathbf{A}$. The belief function assigns positive numbers to those propositions that are believed, negative numbers to those propositions that are disbelieved, and 0 to those propositions with respect to which the agent suspends judgment. Each ranking function *ϱ* induces a *belief set*

$$\begin{align} \bB &= \{A \in \mathbf{A}: \beta(A) \gt 0\} \\ &= \{A \in \mathbf{A}: \varrho(\neg A) \gt \varrho(A)\} \\ &=\{A \in \mathbf{A}: \varrho(\neg A) \gt 0\}. \end{align}$$

$\bB$ is the set of all propositions the agent believes to some positive degree, or equivalently, whose complements she disbelieves to a positive degree. The belief set $\bB$ induced by a (finitely/countable/completely minimitive) ranking function *ϱ* is consistent and deductively closed (in the finite/countably/complete sense). Since any proposition with $\beta(A)>0$ is believed, ranking theory can be seen as satisfying the Lockean thesis (see Section 4.2.2) without sacrificing deductive closure. Note, however, that we could have defined $\bB$ to include all those propositions $A$ with $\beta(A) \gt t$ for some threshold $t$ greater than zero. See Raidl (2019)[^raidl-2019] for an exploration of these possibilities.

So far we have discussed the synchronic structure ranking theory imposes on belief. How should ranks be updated when new information is received? The *conditional* ranking function $\varrho(\cdot\mid \cdot):\mathbf{A}\times\mathbf{A} \rightarrow \bN\cup \{\infty \} $ based on the non-conditional ranking function *ϱ* is defined by setting

$$ \varrho(A\mid B) = \varrho(A \cap B) - \varrho(B), $$

for all $A, B$ in $\mathbf{A}$ where $A \neq \varnothing$. We adopt the convention that $\infty - \infty = 0$ and $\infty - n = \infty$ for all finite $n$. Note that this entails that $\varrho(\neg A\mid A) = \infty$. Requiring that $\varrho(\varnothing \mid B) = \infty$ for all $B$ in $\mathbf{A}$ guarantees that $\varrho(\cdot\mid B)$ is a (non-conditional) ranking function. Conditional ranking functions give rise to a ranking-theoretic counterpart of strict conditionalization:

**Plain Conditionalization**. Suppose that $\varrho(\cdot)$ is your ranking function at time $t$ and that $\varrho(A),\varrho(\neg A) \lt \infty$. Furthermore, suppose that between $t$ and $t^\prime$ you become certain of $A$ and no logically stronger proposition. Then, your ranking function at time $t^\prime$ should be $\varrho(\cdot\mid A)$.

Note that all the considerations relevant to the interpretation of Bayesian conditionalization (discussed in Section 3.1.4) apply equally to ranking-theoretic conditioning. It is clear from the definition of conditioning that, as in the Bayesian case, the rank of the material conditional is a lower bound for the conditional rank: $\beta(A\rightarrow B)\leq \beta(B|A)$. That ensures that ranking-theoretic update satisfies Conditionalization ( see Section 2.1.1). It also satisfies a version of Rational Monotony: if $\beta(\neg A)=0$ and $\beta(B)>0,$ then $\beta(B|A)>0.$ Therefore, ranking-theoretic update satisfies the “spirit” of AGM update. Note, however, that ranking theory has no trouble with iterated belief revision: a revision takes as input a ranking function and an evidential proposition and outputs a new ranking function. Moreveover, the situation changes if the threshold for belief is raised to some positive number greater than zero: in that case, Rational Monotony may no longer be satisfied (see Raidl, 2019)[^raidl-2019].

Plain conditionalization only covers the case when new evidence acquires the maximum degree of certainty. Spohn (1988)[^spohn-1988] also defines a ranking-theoretic analogue to Jeffrey conditionalization. In this case, new evidence does not acquire maximum certainty, but merely changes your ranks for various propositions. For more on ranking-theoretic notions of belief update see Huber (2014, 2019)[^huber-2014][^huber-2019]. For a comparison of probability theory and ranking theory see Spohn (2009, Section 3)

Why should grades of disbelief obey the ranking calculus? And why should ranking functions be updated according to ranking-theoretic conditionalization? Recall that in the case of subjective probability theory, analogous questions were answered by appeal either to the Dutch book arguments or considerations of epistemic accuracy. Is it possible to make similar arguments in favor of ranking theory?

The short answer is yes: Huber (2007 and 2020, Chapter 5) proves that obeying the normative constraints of the ranking calculus is a necessary and sufficient condition for maintaining consistency and deductive closure, both synchronically and in the face of new evidence. The latter end is, in turn, a necessary, but insufficient means to attaining the end of always having only true beliefs, and as many thereof as possible. Unlike the Dutch book arguments, this result requires no appeal to pragmatic considerations about betting behavior. Brössel, Eder & Huber (2013) discuss the importance of this result as well as its Bayesian role-model, Joyce’s (1998, 2009)[^joyce-1998][^joyce-2009] “non-pragmatic” vindication of probabilism.

It is fairly straightforward to see that any agent that obeys the synchronic requirements of the ranking calculus (and updates according to one of the sactioned update rules) will maintain beliefs that are mutually consistent and deductively closed, no matter what new evidence arrives. What is slightly more puzzling is why any agent who does *not* validate the ranking calculus must either have inconsistent beliefs, or fail to believe a logical consequence of some of her beliefs. In other words: it is clear that the ranking calculus is sufficient for deductive cogency, but why is it *necessary*?

To sketch the necessity argument, we must introduce a bit of terminology. An agent’s degree of *entrenchment* for a proposition $A$ is the number of “independent and minimally positively reliable” (mp-reliable) information sources saying $A$ that it would take for the agent to give up her disbelief that $A$. If the agent does not disbelieve $A$ to begin with, her degree of entrenchment for $A$ is 0. If no finite number of information sources is able to make the agent give up her disbelief that $A$, her degree of entrenchment for $A$ is $\infty$. Of course, information sources we typically encounter are rarely independent or mp-reliable. However, this is not crucial. Independent, mp-reliable sources are a theoretical construct – the connection between entrenchment and update is stated as a counterfactual because the agent need never actually encounter such information sources.

The necessity argument proceeds by stipulating that entrenchment is reflected in degrees of disbelief. This connects an agent’s updating *behavior* with her ranks for various propositions. Recall that Bayesians stipulate a similar connection between degrees of belief and acceptable betting ratios. Equipped with this connection, Huber (2007, 2020)[^huber-2007][^huber-2020] proves that if an agent fails to validate the ranking calculus then, were she to encounter independent, mp-reliable information sources of various kinds, her beliefs would fail to be deductively cogent. That completes the necessity argument.

With the possible exception of decision making (see however Giang and Shenoy, 2000 as well as Spohn 2017a, 2020)[^giang-2000][^spohn-2017a][^spohn-2020], it seems that we can do everything with ranking functions that we can do with probability measures. Ranking theory also naturally gives rise to a notion of qualitative belief that incurs no Lottery-style paradoxes (see Section 4.2.2). This may be vital if we want to stay in tune with traditional epistemology. The treatment of ranking theory in this article has been, of necessity, rather compressed. For an excellent article-length introduction see Huber (2019)[^huber-2019]. For an accessible book, see Huber (2020)[^huber-2020]. For an extensive book-length treatment, with applications to many subjects in epistemology and philosophy of science, see Spohn (2012)[^spohn-2012].

## 4. Full and Partial Belief

### 4.1 Eliminationism

There are those who deny that there are any interesting principles bridging full and partial belief. Theorists of this persuasion often want either to eliminate one of these attitudes or reduce it to a special case of the other. Jeffrey (1970)[^jeffrey-1970] suggests that talk of full belief is vestigial and will be entirely superseded by talk of partial belief and utility:

> … nor am I disturbed by the fact that our ordinary notion of *belief* is only vestigially present in the notion of degree of belief. I am inclined to think Ramsey sucked the marrow out of the ordinary notion, and used it to nourish a more adequate view. But maybe there is more there, of value. I hope so. Show me; I have not seen it at all clearly, but it may be there for all that.

Theorists such as Kaplan (1996)[^kaplan-1996] also suggests that talk of full belief is superfluous once the mechanisms of Bayesian decision theory are in place. After all, only partial beliefs and utilities play any role in the Bayesian framework of rational deliberation, whereas full belief need not be mentioned at all. Those committed to full beliefs have the burden of showing how rationality will be the poorer without recourse to full belief. Kaplan calls this the *Bayesian Challenge.* Stalnaker (1984)[^stalnaker-1984] is much more sympathetic to a qualitative notion of belief, but acknowledges the force of the Bayesian challenge.

It is true that there is no canonical qualitative analogue to the Bayesian theory of practical deliberation. However, the fact that it is the theorist of full belief that feels the challenge, and not *vice versa*, may be an accident of history: if a qualitative theory of practical deliberation had been developed first, the shoe would now be on the other foot. The situation would be even more severe if qualitative decision making, which we seem to implement as a matter of course, were less cognitively demanding than its Bayesian counterpart. Of course, this anticipates a robust theory of rational qualitative deliberation that is not immediately forthcoming. However, recent work such as Lin (2013)[^lin-2013] and Spohn (2017a, 2019)[^spohn-2017a] may remedy that inadequacy. For example, Lin (2013)[^lin-2013] proves a Savage-style representation theorem characterizing the relationship between full beliefs, desires over possible outcomes and preferences over acts. By developing a theory of rational action in terms of qualitative belief, Lin demonstrates how one might answer the Bayesian challenge.

On the other hand there are partisans of full belief that are deeply skeptical about partial beliefs. See Harman (1986)[^harman-1986], Pollock (2006)[^pollock-2006], Moon (2017)[^moon-2017], Horgan (2017)[^horgan-2017] and the “bad cop” in Hájek and Lin (2017). Many of these object that partial beliefs have no psychological reality and would be too difficult to reason with if they did. Horgan (2017)[^horgan-2017] goes so far as to say that typically “there is no such psychological state as the agent’s credence in $p$” and that Bayesian epistemology is “like alchemy and phlogiston theory: it is not about any real phenomena, and thus it also is not about any genuine norms that govern real phenomena.” Harman (1986)[^harman-1986] argues that we have very few explicit partial beliefs. A theory of reasoning, according to Harman, can concern only explicit attitudes, since these are the only ones that can figure in a reasoning process. Therefore, Bayesian epistemology, while perhaps an account of dispositions to act, is not a guide to reasoning. Nevertheless, partial beliefs may be implicit in our system of full beliefs in that they can be reconstructed from our dispositions to revise them:

> How should we account for the varying strengths of explicit beliefs? I am inclined to suppose that these varying strengths are implicit in a system of beliefs one accepts in a yes/no fashion. My guess is that they are to be explained as a kind of epiphenomenon resulting from the operation of rules of revision. For example, it may be that $P$ is believed more strongly than $Q$ if it would be harder to stop believing $P$ than to stop believing $Q$, perhaps because it would require more of a revision of one’s view to stop believing $P$ than to stop believing $Q$ (p. 22).

On this picture, almost all of our explicit beliefs are qualitative. Partial beliefs are not graded *belief attitudes* toward propositions, but rather dispositions to revise our *full* beliefs. The correct theory of partial belief, according to Harman, has more to do with entrechment orders (see Section 2.2.2) or ranking-theoretic degrees of belief (see Section 3.5) than with probabilities. Other apparently partial belief attitudes are explained as full beliefs *about* objective probabilities. So, in the case of a fair lottery with ten thousand tickets, the agent does not believe to a *high degree* that the $n^{th}$ ticket will not win, but rather fully believes that it is objectively improbable that it will win.

Frankish (2009)[^frankish-2009] objects that Harman’s view requires that an agent have a full belief in any proposition that we have a degree of belief in: “And this is surely wrong. I have some degree of confidence (less than 50%) in the proposition that it will rain tomorrow, but I do not believe flat-out that it will rain – not, at least, by the everyday standards for flat-out belief.” Harman might reply that Frankish merely has a full belief in the objective probability of rain tomorrow. Frankish claims that this escape route is closed to Harman because single events “do not have objective probabilities,” but this matter is hardly settled.

Staffel (2013)[^staffel-2013] gives an example in which a proposition with a higher degree of belief is apparently less entrenched than one with a lower degree of belief. Suppose that you will draw a sequence of two million marbles from a big jar full of red and black marbles. You do not know what proportion of the marbles are red. Consider the following cases:

| (1) | You have drawn twenty marbles, 19 black and one red. Your degree of belief that the last marble you will draw is black is $.95$. |
| --- | --- |
| (2) | You have drawn a million marbles, 900,000 of which have been black. Your degree of belief that the last marble you will draw is black is $19/20=.90$. |

Staffel argues that your degree of belief in the first case is higher than in the second, but much more entrenched in the second than in the first. Therefore, degree of belief cannot be reduced to degree of entrenchment. Nevertheless, the same gambit is open to Harman in the case of the marbles–he can claim that in both scenarios you merely have a full belief in a proposition about objective chance. See Staffel (2013)[^staffel-2013] for a much more extensive engagement with Harman (1986)[^harman-1986].

### 4.2 Bridge Theories

Anyone who allows for the existence of both full and partial belief inherits a thorny problem: how are full beliefs related to partial beliefs? That seemingly innocent question leads to a treacherous search for *bridge principles* connecting a rational agent’s partial beliefs with her full beliefs. Theorists engaged in the search for bridge principles usually take for granted some set of rationality principles governing full belief and its revision, e.g. AGM theory, or a rival system of non-monotonic reasoning. Theorists usually also take for granted that partial belief ought to be representable by probability functions obeying some flavor of Bayesian rationality. The challenge is to propose additional rationality postulates governing how a rational agent’s partial beliefs cohere with her full beliefs. In this section, we will for the most part accept received wisdom and assume that orthodox Bayesianism is the correct model of partial belief and its updating. We will be more open-minded about the modeling of full belief and its rational revision.

In this section, we will once again take propositions over the set $W$ to be the objects of belief. As before, the reader is invited to think of $W$ as a set of coarse-grained, mutually exclusive, possible ways the actual world might be. We write $\Bel$ to denote the set of *propositions* that the agent believes and use $\Bel(A)$ as shorthand for $A\in \Bel$. We will also require some notation for qualitative propositional belief change. For all $E\subseteq W$, write $\Bel_E$ for the set of propositions the agent would believe upon learning $E$ and no stronger proposition. We will also write $\Bel(A|E)$ as shorthand for $A\in \Bel_E.$ By convention, $\Bel= \Bel_W.$ If ${\bf F}$ is a set of propositions, we let $\Bel_{\bf F}$ be the set $\{ \Bel_E : E \in {\bf F} \}.$ The set $\Bel_{\bf F}$ represents an agent’s *dispositions* to update her qualitative beliefs given information from ${\bf F}$.

The following normative constraint on the set of full beliefs $\Bel$ plays a large role in what follows.

**Deductive Cogency.** The belief set $\Bel$ is consistent and $B\in\Bel$ if and only if $\cap \Bel \subseteq B.$

In other words, deductive cogency means that there is a single, non-empty proposition, $\cap \Bel$, which is the logically strongest proposition that the agent believes, entailing all her other beliefs.

All of the rationality norms that we have seen for updating qualitative beliefs have propositional analogues. The following are propositional analogues for the AGM principles from Section 2.2.1.

| (Closure) | $\Bel_E=\Cn(\Bel_E)$; |
| --- | --- |
| (Success) | $E\in\Bel_E$; |
| (Inclusion) | $\Bel_E \subseteq \Cn(\Bel \cup \{E\}) $; |
| (Preservation) | If $\neg E \not\in \Cn(\Bel) $, then $ \Bel \subseteq \Bel_E $; |
| (Consistency) | $\Bel_E$ is consistent iff $ E\neq \varnothing$; |
| (Extensionality) | If $E\equiv F$, then $\Bel_E=\Bel_F$. |
| (Conjunctive Inclusion) | $\Bel_{E\cap F} \subseteq \Cn(\Bel_{E} \cup \{F\})$; |
| (Conjunctive Preservation) | If $\neg F \notin \Cn(\Bel_E)$ then, $\Cn(\Bel_E \cup \{F\}) \subseteq \Bel_{E\cap F}.$ |

Supposing that for all $E\subseteq W$, $\Bel_E$ satisfies deductive cogency, the first six postulates reduce to the following three.

| (Success) | $\cap \Bel_E \subseteq E$; |
| --- | --- |
| (Inclusion) | $\cap \Bel \cap E \subseteq \cap \Bel_{E};$ |
| (Preservation) | If $\cap \Bel \nsubseteq \neg E,$ then $\cap \Bel_{E} \subseteq \cap \Bel \cap E.$ |

Together, Inclusion and Preservation say that whenever information $E$ is consistent with current belief $\cap \Bel,$ $$\cap \Bel_E = \cap \Bel \cap E.$$ If ${\bf F}$ is a collection of propositions and for all $E\in {\bf F},$ the belief sets $\Bel,\Bel_E$ satisfy the AGM principles, we say that $\Bel_{\bf F},$ the agent’s disposition to update her qualitative beliefs given information from ${\bf F}$, satsifies the basic AGM principles.

We will use $\Pr(\cdot)$ to denote the probability function representing the agent’s partial beliefs. Of course, $\Pr(\cdot)$ is defined on a *σ*-algebra of subsets of $W$. In the usual case, when $W$ is finite, we can take the powerset $\mathcal{P}(W)$ to be the relevant *σ*-algebra. To update partial belief, we adopt the standard probabilistic modeling. For $E\subseteq W$ such that $\Pr(E)>0,$ $\Pr(\cdot|E)$ is the partial belief function resulting from learning $E.$ We will sometimes use $\Pr_E$ as a shorthand for $\Pr(\cdot|E)$. Almost always, partial belief is updated via standard conditioning. As before, ${\bf A}^{\Pr}$ is the set of propositions with positive probability according to $\Pr$.

### 4.2.1 Belief as Extremal Probability

The first bridge principle that suggests itself is that full belief is just the maximum degree of partial belief. Expressed probabilistically, it says that at all times a rational agent’s beliefs and partial beliefs can be represented by a pair $\langle \Bel,p \rangle$ satisfying:

**Extremal Probability.** $ A\in\Bel$ if and only if $\Pr(A)=1.$

Roorda (1995) calls this the *received view* of how full and partial belief ought to interact. Gärdenfors (1986)[^gärdenfors-1986] is a representative of this view, as are van Fraasen (1995) and Arló-Costa (1999)[^arló-costa-1999], although the latter two accept a slightly non-standard probabilistic modeling for partial belief. For fans of deductive cogency, the following observations ought to count in favor of the received view.

**Theorem.** If $\langle \Bel, p \rangle$ satisfy extremal probability, then $\Bel$ is deductively cogent.

Gärdenfors (1986)[^gärdenfors-1986] proves the following.

**Theorem.** Suppose that$\langle \Bel_E, \Pr_E \rangle$ satisfy extremal probability for all $E\in {\bf A}^{\Pr}.$ Then $\Bel_{{\bf A}^{\Pr}}$ satisfies the AGM postulates.

In other words: if an agent’s partial beliefs validate the probability axioms, she updates by Bayesian conditioning and fully believes all and only those propositions with extremal probability, her qualitative update behavior will satisfy all the AGM postulates (at least whenever Bayesian conditioning is defined). Readers who take the AGM revision postulates to be a *sine qua non* of rational belief update will take this to be good news for the received view.

Roorda (1995) makes three criticisms of the received view. Consider the following three propositions.

1. Millard Fillmore was the 13th President of the United States;
2. Millard Fillmore was a U.S. President;
3. Millard Fillmore either was or was not a U.S. President.

Of course, I am not as confident that Fillmore was the 13th president as I am in the truth of the tautology expressed in (3). Yet there does not seem to be anything wrong with saying that I fully believe each of (1), (2) and (3). However, if extremal probability is right, it is irrational to fully believe each of (1), (2) and (3) and not assign them all the same degree of belief.

Roorda’s second objection appeals to the standard connection between degrees of belief and practical decision making. Suppose I fully believe (1). According to the standard interpretation of degrees of belief in terms of betting quotients, I ought to accept a bet that pays out a dollar if (1) is true, and costs me a million dollars if (1) is false. In fact, if I truly assign unit probability to (1), I ought to accept nearly any stakes whatsoever that guarantee some positive payout if (1) is true. Yet it seems perfectly rational to fully believe (1) and refrain from accepting such a bet. If we accept Bayesian decision theory, extremal probability seems to commit me to all sorts of weird and seemingly irrational betting behavior.

Roorda’s final challenge to extremal probability appeals to *corrigibility*, according to which it is reasonable to believe that at least some of my beliefs may need to be abandoned in light of new information. However, if partial beliefs are updated via Bayesian conditioning, I can never cease to believe any of my full beliefs since if $\Pr(A)=1$ it follows that $\Pr(A|E)=1$ for all $E$ such that $\Pr(E)>0$. If we believe in Bayesian conditioning, extremal probability seems to entail that I cannot revise any of my full beliefs in light of new information.

### 4.2.2 The Lockean Threshold

The natural response to the difficulties with the received view is to retreat from full certainty. Perhaps full belief corresponds to partial belief above some *threshold* falling short of certainty. Foley (1993)[^foley-1993] dubbed this view the *Lockean thesis*, after some apparently similar remarks in Book IV of Locke’s (1690/1975) *Essay Concerning Human Understanding.* So far, the Lockean thesis is actually ambiguous. There may be a single threshold that is rationally mandated for all agents and in all circumstances. Alternatively, each agent may have her own threshold that she applies in all circumstances–that threshold may characterize how “bold” or “risk-seeking” the agent is in forming qualitative beliefs. A yet weaker thesis holds that the threshold may be contextually determined. We distinguish the strong, context-independent Lockean thesis (SLT) from the weaker, context-dependent thesis (WLT). The domain of the quantifier may be taken as the set of all belief states $\langle \Bel,\Pr \rangle$ a *particular* agent may find herself in, or as the set of all belief states whatsoever.

- **(SLT)** There is a threshold $s\in (\frac{1}{2}, 1)$ such that all rational $\langle \Bel, \Pr \rangle$ satisfy $$\Bel(A) \text{ iff } \Pr(A) \geq s.$$
- **(WLT)** For every rational $\langle \Bel, \Pr \rangle$ there is a threshold $s\in(\frac{1}{2}, 1)$ such that $$\Bel(A) \text{ iff } \Pr(A) \geq s.$$

Most discussions of the Lockean thesis have in mind the strong thesis. More recent work, especially Leitgeb (2017)[^leitgeb-2017], adopts the weaker thesis. The strong thesis leaves the correct threshold unspecified. Of course, for every $s\in(\frac{1}{2},1)$ we can formulate a specific thesis $\text{SLT}^s$ in virtue of which the strong thesis is true. For example, $\text{SLT}^{.51}$ is a very permissive version of the thesis, whereas $\text{SLT}^{.95}$ and $\text{SLT}^{.99}$ are more stringent. It is also possible to further specify the weak thesis. For example, Leitgeb (2017)[^leitgeb-2017] believes that the contextually-determined threshold should be equal to the degree of belief assigned to the strongest proposition that is fully believed. In light of deductive cogency, that corresponds to the orthographically ungainly $\text{WLT}^{\Pr(\cap \Bel)}$.

The strong Lockean thesis gives rise to the well-known *Lottery paradox*, due originally to Kyburg (1961, 1997)[^kyburg-1961][^kyburg-1997]. The lesson of the Lottery is that the strong thesis is in tension with deductive cogency. Suppose that $s$ is the universally correct Lockean threshold. Now think of a fair lottery with $N$ tickets, where $N$ is chosen large enough that $1-(1/N) \geq s.$ Since the lottery is fair, it seems permissible to fully believe that *some* ticket is the winner. It also seems reasonable to assign degree of belief $1/N$ to each proposition of the form ‘The $i^{\text{th}}$ ticket is the winner.’ According to the Lockean thesis, such an agent ought to fully believe that the first ticket is a loser, the second ticket is a loser, the third is a loser, etc. Since cogency requires belief to be closed under conjunction, she ought to believe that all the tickets are losers. But now she violates cogency by believing both that every ticket is a loser and that some ticket is a winner. Since $s$ was arbitrary, we have shown that no matter how high we set the threshold, there is some Lottery for which an agent must either violate the Lockean thesis or violate deductive cogency. According to Kyburg, what the paradox teaches is that we should give up on deductive cogency: full belief should not necessarily be closed under conjunction. Many others take the lesson of the Lottery to be that the strong Lockean thesis is untenable.

Several authors (Pollock (1995)[^pollock-1995], Ryan (1996)[^ryan-1996], Douven (2002)[^douven-2002]) attempt to revise the strong Lockean thesis by placing restrictions on when a high degree of belief warrants full belief. Broadly speaking, they propose that a high degree of belief is sufficient to warrant full belief unless some defeating condition holds. For example, Douven (2002)[^douven-2002] says that it is sufficient except when the proposition is a member of a *probabilistically self-undermining* set. A set ${\bf S}$ is probabilistically self-undermining iff for all $A \in {\bf S}, \Pr(A)>s$ and $\Pr(A | B)\leq s,$ where $B=\cap( {\bf S} \setminus \{ A \}).$ It is clear that this proposal would prohibit full belief that a particular lottery ticket will lose.

All proposals of this kind are vitiated by the following sort of example due to Korb (1992)[^korb-1992]. Let $A$ be any proposition with a degree of belief above threshold but short of certainty. Let $L_i$ be the proposition that the $i^{th}$ lottery ticket (of a large lottery with $N$ tickets) will lose. Consider the set ${\bf S} = \{ \neg A \cup L_i | 1 \leq i \leq N \}.$ Each member of ${\bf S}$ is above threshold, since $L_i$ is above threshold. Furthermore, the set ${\bf S} \cup \{ A\}$ meets Douven’s (as well as Pollock’s and Ryan’s) defeating conditions. Therefore, these proposals prohibit full belief in any proposition with degree of belief short of certainty. Douven and Williamson (2006) generalize this sort of example to trivialize an entire class of similar formal proposals.

Buchak (2014)[^buchak-2014] argues that what partial beliefs count as full beliefs cannot merely be a matter of the degree of partial belief, but must also depend on the type of evidence it is based on. According to Buchak, this means there can be no merely formal answer to the question: what conditions on partial belief are necessary and sufficient for full belief? The following example, of a type going back to Thomson (1986)[^thomson-1986], illustrates the point. Your parked car was hit by a bus in the middle of the night. The bus could belong either to the blue bus company or the red bus company. Consider the following two scenarios.

- **(1)** You know that the blue company operates 90% of the buses in the area, and the red bus company operates only 10%. You have degree of belief 0.9 that a blue bus is to blame.
- **(2)** The red and blue companies operate an equal number of buses. A 90% reliable eyewitness testifies that a blue bus hit your car. You have degree of belief 0.9 that a blue bus is to blame.

Buchak (2014)[^buchak-2014] argues that it is rational to have full belief that a blue bus is to blame in the first scenario, but not in the second. You have only statistical evidence in the first scenario, whereas in the second, a causal chain of events connects your belief to the accident (see also Thomson (1986)[^thomson-1986], Nelkin (2000)[^nelkin-2000] and Schauer (2003)[^schauer-2003]). These intuitions, Buchak observes, are reflected in our legal practice: purely statistical evidence is not sufficient to convict. If you find Buchak’s point convincing, you will be unsatisfied with most of the proposed accounts for how full and partial belief ought to correspond (see Staffel (2016)[^staffel-2016]).

Despite difficulties with buses and lotteries, the dynamics of qualitative belief under the strong thesis are independently interesting to investigate. For example, van Eijk and Renne (2014, Other Internet Resources) axiomatize the logic of belief for a Lockean with threshold $\frac{1}{2}$. Makinson and Hawthorne (2015) investigate which principles of non-monotonic logic are validated by Lockean agents. Before turning to proposed solutions to the Lottery paradox, we make some observations about qualitative Lockean revision, inspired largely by Shear and Fitelson (2018).

It is a theorem of the probability calculus that $\Pr(H|E) \leq \Pr(E\rightarrow H)$. So if $H$ is assigned a high degree of belief given $E$, the material conditional $E\rightarrow H$ must have been assigned a degree of belief at least as high *ex ante*. It is easy to see that as a probabilistic analogue of the principle of Conditionalization from non-monotonic logic or, equivalently, the AGM Inclusion principle. That observation has the following consequence: any belief that the Lockean comes to have after conditioning, she could have arrived at by adding the evidence to her prior beliefs and closing under logical consequence. Therefore Lockean updating satisfies the AGM principle of Inclusion. Furthermore, it follows immediately from definitions that Lockean update satisfies Success and Extensionality.

**Theorem.** Suppose that $s\in (\frac{1}{2}, 1)$. For all $E\in{\bf A}^{\Pr}$, let $\Bel_E = \{ A : \Pr(A|E) \geq s\}$. Then, $\Bel_{{\bf A}^{\Pr}}$ satisfies Inclusion, Success and Extensionality.

In Section 2.2, we argued that Inclusion and Preservation capture the spirit of AGM revision. If Lockean revision also satsified Preservation, we would have a clean sweep of the AGM principles, with the exception of deductive cogency. However, that cannot hold in general. It is possible to construct examples where $\Pr(\neg E) \lt s,$ $\Pr(H)\geq s$ and yet $\Pr(H|E) \lt s$. For Lockean agents this means that it is possible to lose a belief, even when revising on a proposition that is not disbelieved.

Recall the example of Alice, Bob and the Ford from Section 2.1.1. Let $W=\{a, b, c\}$ corresponding to the worlds in which Alice owns the Ford, Bob own the Ford and no one in the office owns the Ford. Suppose the probability function $$\Pr(a) =\frac{6}{10}, \Pr(b)=\frac{3}{10} \text{ and } \Pr(c)=\frac{1}{10}$$ captures my partial beliefs. For Lockean thresholds in the interval $(.75,.9]$, my full beliefs are exhausted by $\Bel=\{ \{a,b\}, W\}.$ Now suppose I were to learn that Alice does not own the Ford. That is consistent with all beliefs in $\Bel$, but since $\Pr(\{a,b\} | \{b,c\}) = \frac{3}{4}$ it follows by the Lockean thesis that $\{a,b\} \notin \Bel_{\{b,c\}}$. So Lockeanism does not in general validate Preservation. The good news, at least for those sympathetic to Pollock’s critique of non-monotonic logic, is that the Lockean thesis allows for undercutting defeat of previous beliefs.

However, Shear and Fitelson (2018) also have some good news for fans of AGM and the Lockean thesis. Two quantities are in the *golden ratio* *φ* if their ratio is the same as the ratio of their sum to the larger of the two quantities, i.e. for $a>b>0$, if $\frac{a+b}{a} = \frac{a}{b}$ then $\frac{a}{b} = \phi$. The golden ratio is an irrational number approximately equal to $1.618.$ Its inverse $\phi^{-1}$ is approximately $.618.$ Shear and Fitelson prove the following intriguing result.

**Theorem.** Suppose that $s\in (\frac{1}{2}, \phi^{-1}]$. For all $E\in{\bf A}^{\Pr}$, let $\Bel_E = \{ A : \Pr(A|E) \geq s\}.$ Let ${\bf D}=\{E\in{\bf A}^{\Pr} : \Bel_E \text{ is deductively cogent} \}.$ Then $\Bel_{{\bf D}}$ satisfies the six basic AGM postulates.

That shows that for relatively low thresholds, Lockean updating satsifies all the AGM postulates–at least when we restrict to deductively cogent belief sets. For an explanation of why the golden ratio arises in this context see Section 6.2 in Genin (2019)[^genin-2019].

### 4.2.3 The Stability Theory of Belief

For many, sacrificing deductive cogency is simply too high a price to pay for a bridge principle, even one so simple and intuitive as the strong Lockean thesis. That occassions a search for bridge principles that can be reconciled with deductive cogency. One proposal, due to Leitgeb (2013, 2014, 2017)[^leitgeb-2013][^leitgeb-2014][^leitgeb-2017] and Arló-Costa (2012)[^arló-costa-2012], holds that rational full belief corresponds to a stably high degree of belief, i.e. a degree of belief that remains high even after conditioning on new information. Leitgeb calls this view the *Humean thesis*, due to Hume’s conception of belief as an idea of superior vivacity, but also of superior steadiness. See Loeb (2002, 2010)[^loeb-2002][^loeb-2010] for a detailed development of the stability theme in Hume’s conception of belief. Leitgeb (2017)[^leitgeb-2017] formalizes Hume’s definition, articulating the following version of the thesis:

- **(HT)** For all rational pairs $\langle \Bel, \Pr \rangle$ there is $s\geq 1/2$ such that $$\Bel(A) \text{ iff } \neg B \notin \Bel \text{ implies } \Pr(A|B)> s.$$

In other words: every full belief must have stably high conditional degree of belief, at least when conditioning on propositions which are not currently disbelieved. Since full belief occurs on both sides of the biconditional, it is evident that this is not a proposed *reduction* of full belief to partial belief, but rather a constraint that every rational agent must satisfy. The Humean thesis leaves the precise threshold $s$ unspecified. Of course, for every $\frac{1}{2} \lt s \lt 1,$ we can formulate a specific thesis $\text{HT}^s$ in virtue of which the thesis is true. For example, $\text{HT}^{.5}$ requires that every fully believed proposition remains more likely than its negation when conditioning on propositions not currently disbelieved.

Some form of stability is widely considered to be a necessary condition for *knowledge*. Socrates propounds such a view in the *Meno*. Paxson Jr. and Lehrer (1969) champion such a view in the epistemology literature post-Gettier (1963)[^gettier-1963]. However, stability is not usually mooted as a condition of *belief*. Raidl and Skovgaard-Olsen (2017) claim that Leitgeb’s stability condition is more appropriate in an analysis of knowledge and too stringent a condition on belief. A defender of the Humean thesis might say that every *rational* belief is possibly an instance of knowledge. Since knowledge is necessarily stable, unstable beliefs are *ipso facto* not known.

Leitgeb demonstrates the following relationships between the Humean thesis, deductive cogency and the weak Lockean thesis.

**Theorem.** Suppose that $\langle \Bel, \Pr \rangle$ satsify $\text{HT}$ and $\varnothing \notin \Bel.$ Then, $\Bel$ is deductively cogent and $\langle \Bel, \Pr\rangle$ satisfy $\text{WLT}^{\Pr(\cap \Bel)}.$

So if an agent satisfies the Humean thesis and does not “fully” believe the contradictory proposition, her qualitative beliefs are deductively cogent and furthermore, she satisfies the weak Lockean thesis, where the threshold is set by the degree of belief assigned to $\cap\Bel,$ the logically strongest proposition she believes. Leitgeb also proves the following partial converse.

**Theorem.** Suppose that $\Bel$ is deductively cogent and $\langle \Bel, \Pr \rangle$ satisfy $\text{WLT}^{\Pr(\cap \Bel)}$. Then, $\langle \Bel, \Pr \rangle$ satsify $\text{HT}^{\frac{1}{2}}$ and $\varnothing \notin \Bel$.

Together, these two theorems say that the Humean thesis (with threshold 1/2) is equivalent to deductive cogency and the weak Lockean thesis (with threshold $\Pr(\cap\Bel)$). Since it is always possible to satisfy HT$^\frac{1}{2}$, Leitgeb gives us an ingenious way to reconcile deductive cogency with a version of the Lockean thesis.

Recall the example of the lottery. Let $W=\{w_1, w_2, \ldots, w_N \},$ where $w_i$ is the world in which the $i^{\text{th}}$ ticket is the winner. No matter how many tickets are in the lottery, a Humean agent cannot believe any ticket will lose. Suppose for a contradiction that she believes $W\setminus \{w_1\}$, the proposition that the first ticket will lose. Now suppose she learns $\{w_1, w_2\}$, that all but the first and second ticket will lose. This is compatible with her initial belief, but her updated degree of belief that the first ticket will lose must be $1/2$. That contradicts the Humean thesis. So she cannot believe that any ticket will lose. In this Lottery situation the agent cannot fully believe any non-trivial proposition. This example also shows how sensitive the Humean proposal is to the fine-graining of possibilities. If we coarsen $W$ into the set of possibilities $W=\{w_1, w_2\}$, where $w_1$ is the world in which the first ticket is the winner and $w_2$ is “the” world in which some other ticket is the winner, the agent can believe that the first ticket will lose without running afoul of the Humean thesis.

If Buchak (2014)[^buchak-2014] is right, no agent should have beliefs in lottery propositions–these beliefs would necessarily be formed on the basis of purely statistical evidence. Kelly and Lin (2019)[^lin-2019] give another scenario in which Humean agents seem radically skeptical, but in situations which are evidentially unproblematic. Suppose the luckless Job goes in for a physical. On the basis of a thorough examination, the doctor forms the following dire opinion of his health: her degree of belief that Job will survive exactly $n$ months is $\frac{1}{2^n}.$ Therefore, her degree of belief that Job will not survive the year is $\frac{1}{2} + \frac{1}{4} + \cdots + \frac{1}{2^{12}} > .999.$ Shockingly, the Humean thesis prevents the doctor from forming *any* non-trivial beliefs. Let $\leq n$ be the proposition that Job survives at most $n$ months and let $\geq n$ be the proposition that he survives at least $n$ months. Let $B$ be the strongest proposition that the doctor believes. Suppose for a contradiction that $B$ entails some least upper bound for the number of Job’s remaining months, i.e for some $n$, $B$ entails $\leq n$ and does not entail $\leq n^\prime $ for any $n^\prime \lt n$. By construction, $\Pr(B| \geq n) = \frac{\Pr(n)}{\Pr(\geq n)} = \frac{1}{2}$ for all $n$. But since $\geq n$ is compatible with $B$, the Humean thesis requires that $\Pr(B| \geq n) > \frac{1}{2}.$ Contradiction.

The example of the doctor suggests that the price of Humeanism is a rather extreme form of skepticism: in many situations a Humean agent will have no non-trivial full beliefs at all. That criticism is developed extensively in Rott (2017)[^rott-2017] and Douven and Rott (2018). The doctor also illustrates how the Humean proposal allows arbitrarily small perturbations of partial beliefs to be reflected as huge differences in full beliefs. Suppose the doctor is slightly more confident that Job will not survive a month, i.e. her survival probabilities decrease as $\frac{1}{2} + \epsilon, \frac{1}{4}, \frac{1}{8} - \epsilon, \frac{1}{16}, \frac{1}{32}, \ldots.$ Now the doctor can believe that Job will be dead in two months without running afoul of the Humean thesis.

So far we have inquired only into the synchronic content of the Humean proposal. What sort principles of qualitative belief update does it underwrite? Leitgeb demonstrates an intimate relationship between the AGM revision principles and the Humean thesis: every agent that satisfies the AGM principles, as well as a weak version of the Lockean thesis, must also satisfy the Humean thesis. So if you think that AGM theory is the correct theory of rational qualitative belief update (and you believe that a high degree of partial belief is a *necessary* condition of full belief) you must also accept the Humean thesis. More precisely, Leitgeb proves the following:

**Theorem.** Suppose that $\Bel_{{\bf A}^{\Pr}}$ satisfies all AGM postulates and for all $E\in{\bf A}^{\Pr},$ $A\in \Bel_E$ only if $\Pr(A|E)>r.$ Then, for all $E\in{\bf A}^{\Pr},$ $\langle \Bel_E, \Pr_E \rangle$ satisfy $\text{HT}^r$.

So any agent that violates the Humean thesis must either fail to satisfy the AGM postulates, or the high-probability requirement. Note that the converse is not true: it is not the case that that if all pairs $\langle \Bel_E, \Pr_E \rangle$ satisfy the Humean thesis, then $\Bel_{{\bf A}^{\Pr}}$ must satisfy the AGM postulates. To prove this, suppose that $\langle \Bel, \Pr \rangle$ satisfy the Humean thesis and $\cap \Bel \subset E$ for some $E\in{\bf A}^{\Pr}.$ If we let $\Bel_E = \{E\}$, then $\langle \Bel_E, \Pr_E \rangle$ satisfy the Humean thesis. However, such an agent patently violates rational and even Cautious Monotony. For a somewhat more detailed treatment of the relationship between AGM theory and the Humean thesis, see Section 6.3 in Genin (2019)[^genin-2019]. For a full treatment, see Leitgeb (2017)[^leitgeb-2017].

### 4.2.4 The Tracking Theory of Belief

Lin and Kelly (2012) propose that qualitative belief update ought to *track* partial belief update. On their picture, partial and full beliefs are maintained and updated by parallel cognitive systems. The first system, governed by the probabilistic norms of Bayesian coherence and conditioning, is precise, slow and cognitively expensive. That system is engaged for important deliberations requiring a lot of precision and occuring without much time pressure, e.g. retirement planning. The second, which in some way maintains and updates full beliefs, is quicker and less cognitively burdensome. That system is engaged in ordinary planning: grocery shopping, or selecting a restaurant for a department event. (For an objection to the two systems view, see Staffel (2018)[^staffel-2018].) What keeps these two parallel systems in sync with each other?

Lin and Kelly (2012) study *acceptance rules* that specify a mechanism for transitioning gracefully into the qualitative and out of the probabilistic system. An acceptance rule *α* maps every partial belief state $\Pr$ to a unique qualitative belief state $\alpha(\Pr)$ with which it coheres. For example, the strong Lockean thesis determines an acceptance rule once we specify a threshold. The Humean thesis, on the other hand, underdetermines an acceptance rule, merely imposing constraints on acceptable pairs $\langle \Bel, \Pr \rangle.$ An agent’s qualitative updates *track* her probabilistic updates iff $$\alpha(\Pr)_E=\alpha(\Pr_E),$$ whenever $\Pr(E)>0$. In other words: acceptance followed by qualitative revision yields the same belief state as probabilistic revision followed by acceptance.

Here is a way to understand the tracking requirement. Suppose that, although an agent maintains a latent probabilistic belief state, most of her cognitive life is spent reasoning with and updating qualitative beliefs. A typical day will go by without having to engage the probabilistic system at all. Suppose Monday is a typical day. Let $\langle \alpha(\Pr), \Pr \rangle$ be the belief state she woke up with on Monday: her full and partial beliefs are in harmony. Let $E$ be the total information she acquired since waking up. Since qualitative beliefs are updated on the fly, she goes to sleep with the qualitative belief state $\alpha(\Pr)_E$. Overnight, her probabilistic system does the difficult work of Bayesian conditioning and computes the partial belief state $\Pr_E$, just in case she runs into any sophisticated decision problems on Tuesday. Before waking, she transitions out of her probabilistic system $\Pr_E$ and into the qualitative belief state $\alpha(\Pr_E)$. If she fails the tracking requirement, she may wake up on Tuesday morning with a qualitative belief state that is drastically different from the one she had went to sleep with on Monday night. If she tracks, then she will notice no difference at all. For such an agent, no mechanism (other than memory) is required to bring her full and partial beliefs back into harmony on Tuesday morning. Supposing that we *enter* the probabilistic system by conditioning our previous partial belief state $\Pr$ on all new information $E$, and *exit* by accepting $\alpha(\Pr_E),$ tracking ensures that transitioning in and out of the probabilistic system does not induce any drastic changes in qualitative beliefs. An agent that tracks will notice no difference at all. An agent that does not track may find her full and partial beliefs perpetually falling out of sync, requiring many expensive acceptance operations to bring them back into harmony.

Tracking may be a desirable property, but are there any architectures that exhibit it? Lin and Kelly (2012) answer this question affirmitively. Since Bayesian conditioning is taken for granted, Lin and Kelly must specify two things: a qualitative revision operation and an acceptance rule that jointly track conditioning. We turn now to the details of their proposal. As usual, let $W$ be a set of worlds. A *question* ${\bf Q}$ is a partition of $W$ into a countable collection of mutually exhaustive propositions $H_1, H_2, \ldots,$ which are the complete *answers* to ${\bf Q}.$ The partial belief function $\Pr$ is defined over the algebra of propositions ${\bf A}$ generated by ${\bf Q}.$ Let $\prec$ be a well-founded, strict partial order over the answers to ${\bf Q}$. (A strict partial order is *well-founded* iff every subset of the order has a least element.) This is interpreted as a *plausibility ordering,* where $H_i \prec H_j$ means that $H_i$ is strictly *more* plausible than $H_j$. Every plausibility order $\prec$ gives rise to a deductively cogent belief state $\Bel_\prec$ by letting $\neg H_i\in \Bel_\prec$ iff there is some $H_j$ strictly more plausible than $H_i$ and closing under logical consequence. In other words, $\cap \Bel_\prec$ is the disjunction of the minimal elements in the plausibility order.

First we specify an acceptance rule. Lin and Kelly propose the *odds threshold rule*. The degree of belief function $\Pr$ is used to determine a plausibility order by setting $$H_i \prec_p H_j \text{ if and only if } \frac{\Pr(H_i)}{\Pr(H_j)} > t,$$ where $t$ is a constant greater than $1$ and $\Pr(H_i),\Pr(H_j)>0$. This determines an acceptance rule by setting $\alpha(\Pr)= \Bel_{\prec_p}.$ Since the odds threshold rule determines a plausibility order $\prec_p$ and any plausibility order $\prec$ gives rise to a deductively cogent belief state $\Bel_\prec,$ the Lottery paradox is avoided. In other words: the bridge principle that any rational $\langle \Bel,p \rangle$ are related by $\Bel=\alpha(\Pr)$ enures that $\Bel$ is deductively cogent. Furthermore, the odds threshold rule allows non-trivial qualitative beliefs in situations where the stability theory precludes them. Recall the case of the doctor. Consider the odds threshold $2^{10} -1$. Given this threshold, the hypothesis that Job will survive exactly 1 month is strictly more plausible than the proposition that he will survive at least $n$ months for any $n\geq 10$. This threshold yields the full belief that Job will survive at most 10 months. However, in the case of the Lottery, the odds threshold rule precludes any non-trivial beliefs. (The content-dependent threshold rule proposed by Kelly and Lin (forthcoming) may allow non-trivial beliefs in the Lottery situation.) See Rott (2017)[^rott-2017] and Douven and Rott (2018) for an extensive comparison of the relative likelihood of forming non-trivial qualitative beliefs on the odds-threshold and stability proposals.

It remains to specify the qualitative revision operation. Lin and Kelly adopt an operation proposed by Shoham (1987)[^shoham-1987]. The plausibility order $\prec$ is updated on evidence $E$ by setting every answer incompatible with $E$ to be strictly less plausible than every answer compatible with $E,$ and otherwise leaving the order unchanged. Let $\prec_E$ denote the result of this update operation. We use the updated plausibility order to define a belief revision rule by setting $\Bel_E = \Bel_{\prec_E}.$ Then, for all $E,F\subseteq W$, $B_E$ is deductively cogent and satisfies:

| (Success) | $\cap \Bel_E \subseteq E$; |
| --- | --- |
| (Inclusion) | $\cap \Bel \cap E \subseteq \cap \Bel_{E};$ |
| (Cautious Monotony) | If $\cap\Bel\subseteq E$ then $\cap \Bel_E \subseteq \cap \Bel.$ |

However, it does not necessarily satisfy Preservation. To see this suppose that ${\bf Q}=\{H_1, H_2, H_3\}$ and $H_1 \prec H_2$ but $H_3$ is not ordered with $H_1$ or $H_2$. Then $\cap \Bel = H_1\cup H_3.$ However $\cap\Bel_{\neg H_1} = H_2 \cup H_3\nsubseteq \cap \Bel$ even though $\cap \Bel \cap \neg H_1 \neq \varnothing.$

Lin and Kelly prove that Shoham revision and odds-threshold based acceptance jointly track conditioning:

**Theorem.** Let $\prec$ equal $\prec_p$ and let $\Bel_E = \Bel_{\prec_E}$. Then $\Bel_{\mathcal{P}(W)}$ satisfies deductive cogency, Success, Cautious Monotony and Inclusion. Furthermore, $\Bel_E = \alpha(\Pr)_E = \alpha(\Pr_E)$ for all $E\in{\bf A}^{\Pr}$.

In other words: odds-threshold acceptance followed by Shoham revision yields the same belief state as Bayesian conditioning followed by odds-threshold acceptance. (Kelly and Lin (forthcoming) recommend a modification of the odds-threshold rule proposed in Lin and Kelly (2012).) Although the original plausibility ordering $\prec_p$ is built from the probability function $\Pr,$ subsequent qualitative update proceeds without consulting the (conditioned) probabilities. That shows that there are at least some architectures that effortlessly keep the probabilistic and qualitative reasoning systems in harmony.

Fans of AGM will regret that Shoham revision does not satisfy AGM Preservation (Rational Monotony). Lin and Kelly (2012) prove that no “sensible” acceptance rule that tracks conditioning can satisfy Inclusion and Preservation. We omit the technical definition of sensible rules here. For a summary, see Section 6.4 in Genin (2019)[^genin-2019].

### 4.2.5 Epistemic Decision Theory

All of the bridge principles we have seen so far have the following in common: whether an agent’s full and partial beliefs cohere is a matter of the full and partial beliefs *alone*. It is not necessary to mention preferences or utilities in order to evaluate a belief state. There is another tradition, originating in Hempel (1962)[^hempel-1962] and receiving classical expression in Levi (1967a)[^levi-1967a], that assimilates the problem of “deciding” what to believe to a Bayesian decision-theoretic model. Crucially, these authors are not committed to a picture on which agents literally decide what to believe–rather they claim that an agent’s beliefs are subject to the same kind of normative evaluation as their practical decision-making. Contemporary contributions to this tradition include Easwaran (2015)[^easwaran-2015], Pettigrew (2016)[^pettigrew-2016] and Dorst (2017)[^dorst-2017]. Presented here is a somewhat simplified version of Levi’s (1967a)[^levi-1967a] account taking propositions, rather than sentences, as the objects of belief.

As usual, let $W$ be a set of possible worlds. The agent is taken to be interested in answering a *question* ${\bf Q},$ which is a partition of $W$ into a finite collection of mutually exhaustive answers $\{ H_1, H_2, \ldots H_n\}.$ Levi calls situations of this sort “efforts to replace agnosticism by true belief,” echoing themes in Peirce (1877)[^peirce-1877]:

> Doubt is an uneasy and dissatisfied state from which we struggle to free ourselves and pass into the state of belief; while the latter is a calm and satisfactory state which we do not wish to avoid, or to change to a belief in anything else. On the contrary, we cling tenaciously, not merely to believing, but to believing just what we do believe.

The agent’s partial beliefs are represented by a probability function $\Pr$ that is defined, at a minimum, over the algebra ${\bf A}$ generated by the question. Levi recommends the following procedure to determine which propositions are fully believed: disjoin all those elements of ${\bf Q}$ that have *maximal* expected epistemic utility and then close under deductive consequence. The *expected epistemic utility* of a hypothesis $H\in{\bf A}$ is defined as: $$E(H) := \Pr(H)\cdot U(H) + \Pr(\neg H)\cdot u(H),$$ where $U(H)$ is the epistemic utility of accepting $H$ when it is true, and $u(H)$ is the utility of accepting $H$ when it is false. How are $u(H), U(H)$ to be determined? Levi is guided by the following principles.

1. True answers have greater epistemic utility than false answers.
2. True answers that afford a high degree of relief from agnosticism have greater epistemic utility than true answers that afford a low degree of relief from agnosticism.
3. False answers that afford a high degree of relief from agnosticism have greater epistemic utility than false answers that afford a low degree of relief from agnosticism.

It is easy to object to these principles. The first principle establishes a lexicographic preference for true beliefs. It is conceivable that, contra this principle, an informative false belief that is approximately true should have greater epistemic utility than an uninformative true belief. The first principle precludes trading content against truthlikeness. It is also conceivable that, contra the third principle, one would prefer to be wrong, but not too opinionated, than wrong and opinionated. The only unexceptionable principle seems to be the second.

To measure the degree of relief from agnosticism, a probability function $m(\cdot)$ is defined over the elements of ${\bf A}$. Crucially, $m(\cdot)$ does not measure a degree of belief, but degree of *uninformativeness*. The degree of relief from agnosticism afforded by $H\in {\bf A},$ also referred to as the *amount of content* in $H$, is defined to be the complement of uninformativeness: $cont(H_i) = m(\neg H_i).$ Levi argues that all the elements of ${\bf Q}$ ought to be assigned the same amount of content, i.e. $m(H_i)=\frac{1}{n}$ and therefore $cont(H_i)= \frac{n-1}{n}$ for each $H_i\in{\bf Q}$. The set of epistemic utility functions that Levi recommends satisfy the following conditions:

- $U(H) = 1 - q\cdot cont(\neg H);$
- $u(H) = \hspace{7pt} - q\cdot cont(\neg H),$

where $0 \lt q \lt 1.$ All such utility functions are guaranteed to satisfy Levi’s three principles. The parameter $q$ is interepreted as a “degree of caution,” representing the premium placed on truth as opposed to relief from agnosticism. When $q=1$ the epistemic utility of suspending judgement, $U(W)$, is equal to zero. This is the situation in which the premium placed on relief from doubt is the maximum. Levi proves that expected epistemic utility $E(H)$ is maximal iff $\Pr(H)> q \cdot cont(\neg H).$ Therefore, Levi’s ultimate recommendation is that the agent believe all deductive consequences of $$\cap \{ \neg H_i \in {\bf Q} : \Pr(\neg H_i)> 1 - q \cdot cont(\neg H_i) \}.$$ From this formulation it is possible to see Levi’s proposal as a question-dependent version of the Lockean thesis where the appropriate threshold is a function of content. However, Levi takes pains to make sure that the result of this operation is deductively cogent and therefore avoids Lottery-type paradoxes.

Contemporary contributions to the decision-theoretic tradition proceed differently from Levi. Most recent work does not take epistemic utility to be primarily a function of content. Most of these proposals do not refer to a question in context. Many proposals, such as Easwaran (2015)[^easwaran-2015], Dorst (2017)[^dorst-2017], are equivalent to a version of the Lockean thesis, where the threshold is determined by the utility the agent assigns to true and false beliefs. Since these are essentially Lockean proposals, they are subject to Lottery-style paradoxes.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=formal-belief). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/formal-belief/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=formal-belief&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/formal-belief/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- Genin, Konstantin (2017), “[How inductive is Bayesian conditioning?](http://kgenin.github.io/papers/conditioning_long.pdf)”, unpublished manuscript.
- Heinemann, Frank (1997), “[Relative Probabilities](http://www.macroeconomics.tu-berlin.de/fileadmin/fg124/heinemann/papers/relprob.pdf),” unpublished manuscript.
- Huber, Franz, (2007a), “[Confirmation and Induction](http://www.iep.utm.edu/c/conf-ind.htm),” in J. Fieser & B. Dowden (eds.), *The Internet Encyclopedia of Philosophy*.
- Joyce, James M. (2013), “[Why Evidentialists Need Not Worry About the Accuracy Argument for Probabilism](http://www-personal.umich.edu/~jjoyce/papers/APA201.pdf),” unpublished manuscript.
- Pryor, James (2007), “[Uncertainty and Undermining](http://www.jimpryor.net/research/papers/Uncertainty.pdf),” unpublished manuscript.
- Roorda, Jonathan (1995), “[Revenge of Wolfman: A Probabilistic Explication of Full Belief](http://www.princeton.edu/%7Ebayesway/pu/Wolfman.pdf),” unpublished manuscript.
- van Eijck, Jan and Bryan Renne (2014), “[Belief as Willingness to Bet](http://arxiv.org/abs/1412.5090),” arXiv preprint.

## Related Entries

epistemology | epistemology, formal | logic: epistemic | logic: non-monotonic | possible worlds | probability, interpretations of | propositions: structured | vagueness

### Acknowledgments

We are grateful to Liam Kofi Bright and a very gracious anonymous reviewer for their comments and suggestions. We are also grateful to Branden Fitelson, Alan Hájek, and Wolfgang Spohn for their feedback on the previous version of this entry. We have used material from Huber (2009)[^huber-2009] and Genin (2019)[^genin-2019]. Supported by the German Research Foundation through the Cluster of Excellence “Machine Learning – New Perspectives for Science”, EXC 2064/1, project number 390727645.

[^alchourrón-1985]: Alchourrón, Carlos E. & Gärdenfors, Peter & Makinson, David, 1985, “On the Logic of Theory Change: Partial Meet Contraction and Revision Functions,” *Journal of Symbolic Logic*, 50: 510–530.

[^allais-1953]: Allais, Maurice, 1953, “Le comportement de l’homme rationnel devant le risque: Critique des postulats et axiomes de l’ecole americaine,” *Econometrica*, 21(4): 503–546.

[^arló-costa-1999]: Arló-Costa, Horacio, 1999, “Qualitative and Probabilistic Models of Full Belief,” in S.R. Buss, P. Hájek and P. Pudlák (eds.), *Proceedings of Logic Colloquium* (Volume 98), pp. 25–43.

[^arló-costa-2012]: Arló-Costa, Horacio and Arthur Paul Pedersen, 2012, “Belief and Probability: A General Theory of Probability Cores,” *International Journal of Approximate Reasoning*, 53(3): 293–315.

[^armendt-1980]: Armendt, Brad, 1980, “Is There a Dutch Book Argument for Probability Kinematics?” *Philosophy of Science*, 47: 583–588.

[^armendt-1993]: –––, 1993, “Dutch Book, Additivity, and Utility Theory,” *Philosophical Topics*, 21: 1–20.

[^arntzenius-2003]: Arntzenius, Frank, 2003, “Some Problems for Conditionalization and Reflection,” *Journal of Philosophy*, 100: 356–371.

[^bacon-1620]: Bacon, Francis, 1620 [2000], *The New Organon*, L. Jardine and M. Silverthorne (eds.), Cambrdige: Cambridge University Press.

[^baltag-1998]: Baltag, Alexandru, Moss, Larry and Solecki, Stawomir, 1998, “The logic of public announcements, common knowledge, and private suspicions,” in I. Gilboa (ed.) *Proceedings of the 7th conference on the theoretical aspects of rationality and knowledge* (TARK ’98), San Francisco: Morgan Kaufmann, pp. 43–56.

[^bjorndahl-2019]: Bjorndahl, Adam and Özgün, Aybüke, forthcoming, “Logic and Topology for Knowledge, Knowability, and Belief,” *The Review of Symbolic Logic*, first online 09 October 2019. doi:10.1017/S1755020319000509

[^bostrom-2007]: Bostrom, Nick, 2007, “Sleeping Beauty and Self-Location: a Hybrid Model,” *Synthese*, 157: 59–78.

[^boutilier-1996]: Boutilier, Craig, 1996, “Iterated Revision and Minimal Change of Conditional Beliefs,” *Journal of Philosophical Logic*, 25: 263–305.

[^bradley-2012]: Bradley, Darren, 2012, “Four Problems about Self-Locating Belief,” *Philosophical Review*, 121: 149–177.

[^brössel-2013]: Brössel, Peter & Eder, Anna-Maria & Huber, Franz, 2013, “Evidential Support and Instrumental Rationality,” *Philosophy and Phenomenological Research*, 87: 279–300.

[^briggs-2009a]: Briggs, R.A., 2009a, “Distorted Reflection,” *Philosophical Review*, 118: 59–85.

[^briggs-2009b]: –––, 2009b, “The Big Bad Bug Bites Anti-Realists About Chance,” *Synthese*, 167: 81–92.

[^buchak-2013]: Buchak, Lara, 2013, *Risk and Rationality*, Oxford: Oxford University Press.

[^buchak-2014]: –––, 2014, “Belief, credence, and norms” *Philosophical Studies*, 169(2): 285–311.

[^carnap-1962]: Carnap, Rudolf, 1962, *Logical Foundations of Probability*, 2nd edition, Chicago: University of Chicago Press.

[^christensen-1996]: Christensen, David, 1996, “Dutch-Book Arguments Depragmatized: Epistemic Consistency for Partial Believers,” *Journal of Philosophy*, 93: 450–479.

[^christensen-2004]: –––, 2004, *Putting Logic in Its Place. Formal Constraints on Rational Belief*, Oxford: Oxford University Press.

[^cox-1946]: Cox, Richard T., 1946, “Probability, Frequency, and Reasonable Expectation,” *American Journal of Physics*, 14: 1–13.

[^darwiche-1997]: Darwiche, Adnan & Pearl, Judea, 1997, “On the Logic of Iterated Belief Revision,” *Artificial Intelligence*, 89: 1–29.

[^de-1937]: De Finetti, Bruno, 1937, “Le prévision: ses lois logiques, ses sources subjectives,” in *Annales de l’institut Henri Poincaré*, 7: 1–68.

[^de-1970]: –––, 1970, *Theory of Probability*, New York: Wiley.

[^de-1972]: –––, 1972, *Probability, Induction and Statistics*, New York: Wiley.

[^dempster-1968]: Dempster, Arthur P., 1968, “A Generalization of Bayesian Inference,” *Journal of the Royal Statistical Society* (Series B, Methodological), 30: 205–247.

[^dietrich-2016]: Dietrich, Franz and Christian List, 2016, “Probabilistic Opinion Pooling,” in A. Hájek and C.R. Hitchcock (eds.), *Oxford Handbook of Philosophy and Probability*, Oxford: Oxford University Press.

[^dorst-2017]: Dorst, Kevin, 2017, “Lockeans Maximize Expected Accuracy,” *Mind*, 128(509): 175– 211.

[^douven-2002]: Douven, Igor, 2002, “A New Solution to the Paradoxes of Rational Acceptability,” *British Journal for the Philosophy of Science*, 53(3): 391–401.

[^douven-2018]: Douven, Igor and Hans Rott, 2018, “From Probabilities to Categorical Beliefs: Going Beyond Toy Models,” *Journal of Logic and Computation*, 28(6): 1099–1124.

[^douven-2006]: Douven, Igor and Timothy Williamson, 2006, “Generalizing the Lottery Paradox” *British Journal for the Philosophy of Science*, 57(4): 755–779.

[^doyle-1979]: Doyle, Jon, 1979, “A Truth Maintenance System,” *Artificial Intelligence*, 12(3): 231–272.

[^doyle-1992]: –––, 1992, “Reason Maintenance and Belief Revision: Foundations vs. Coherence Theories,” in P. Gärdenfors (ed.), *Belief Revision* (Cambridge Tracts in Theoretical Computer Science), Cambridge: Cambridge University Press, 29–52.

[^dubois-1988]: Dubois, Didier & Prade, Henri, 1988, *Possibility Theory*, *An Approach to Computerized Processing of Uncertainty*, New York: Plenum.

[^dubois-2009]: –––, 2009, “Accepted Beliefs, Revision, and Bipolarity in the Possibilistic Framework,” in F. Huber & C. Schmidt-Petri (eds.), *Degrees of Belief*, Dordrecht: Springer.

[^earman-1992]: Earman, John, 1992, *Bayes or Bust?: a critical examination of Bayesian confirmation theory*, Cambridge, MA: MIT Press.

[^easwaran-2011a]: Easwaran, Kenny, 2011a, “Bayesianism I: Introduction and Arguments in Favor,” *Philosophy Compass*, 6: 312–320.

[^easwaran-2011b]: –––, 2011b, “Bayesianism II: Criticisms and Applications,” *Philosophy Compass*, 6: 321–332.

[^easwaran-2015]: –––, 2015, “Dr. Truthlove, or: How I Learned to Stop Worrying and Love Bayesian Probabilities,” *Noûs*, 50(4): 816–853.

[^easwaran-2012]: Easwaran, Kenny & Fitelson, Branden, 2012, “An ‘Evidentialist’ Worry About Joyce’s Argument for Probabilism,” *Dialectica*, 66: 425–433.

[^egan-2006]: Egan, Andy, 2006, “Secondary Qualities and Self-Location,” *Philosophy and Phenomenological Research*, 72: 97–119.

[^égré-2014]: Égré, Paul & Barberousse, Anouk, 2014, “Borel on the Heap,” *Erkenntnis*, 79: 1043–1079.

[^elga-2000]: Elga, Adam, 2000, “Self-Locating Belief and the Sleeping Beauty Problem,” *Analysis*, 60: 143–147.

[^ellsberg-1961]: Ellsberg, Daniel, 1961, “ Risk, abiguity and the Savage axioms,” *Quarterly Journal of Economics*, 75(4): 643–669.

[^eriksson-2007]: Eriksson, Lina & Hájek, Alan, 2007, “What Are Degrees of Belief?” *Studia Logica*, 86: 183–213.

[^fagin-1995]: Fagin, Ronald and Joseph Halpern, Yoram Moses, and Moshe Y. Vardi, 1995, *Reasoning about Knowledge*, Cambridge, MA: The MIT Press.

[^field-1978]: Field, Hartry, 1978, “A Note on Jeffrey Conditionalization,” *Philosophy of Science*, 45: 361–367.

[^field-nd]: Field, Hartry, forthcoming, “Vagueness, Partial Belief, and Logic”, in G. Ostertag (ed.), *Meanings and Other Things: Essays on Stephen Schiffer*, Oxford: Oxford University Press [[Preprint available online](https://as.nyu.edu/content/dam/nyu-as/philosophy/documents/faculty-documents/field/Field_Vagueness-Partial-Belief-Logic.pdf)].

[^foley-1992]: Foley, Richard, 1992, “The Epistemology of Belief and the Epistemology of Degrees of Belief,” *American Philosophical Quarterly*, 29: 111–121.

[^foley-1993]: –––, 1993, *Working without a net: A study of egocentric epistemology*, Oxford: Oxford University Press.

[^foley-2009]: –––, 2009, “Belief, Degrees of Belief, and the Lockean Thesis,” in F. Huber & C. Schmidt-Petri (eds.), *Degrees of Belief*, Dordrecht: Springer.

[^frankish-2004]: Frankish, Keith, 2004, *Mind and Supermind*, Cambridge: Cambridge University Press.

[^frankish-2009]: –––, 2009, “Partial Belief and Flat-Out Belief,” in F. Huber & C. Schmidt-Petri (eds.), *Degrees of Belief*, Dordrecht: Springer.

[^gabbay-1985]: Gabbay, Dov M., 1985, “Theoretical Foundations for Non-Monotonic Reasoning in Expert Systems,” in K.R. Apt (ed.), *Logics and Models of Concurrent Systems*, NATO ASI Series 13. Berlin: Springer, 439–457.

[^garber-1983]: Garber, Daniel, 1983, “Old Evidence and Logical Omniscience in Bayesian Confirmation Theory,” in J. Earman (ed.), *Testing Scientific Theories* (Minnesota Studies in the Philosophy of Science: Volume 10), Minneapolis: University of Minnesota Press, 99–131.

[^gärdenfors-1986]: Gärdenfors, Peter, 1986, “The dynamics of belief: Contractions and revisions of probability functions,” *Topoi*, 5(1): 29–37.

[^gärdenfors-1988]: –––, 1988, *Knowledge in Flux*, *Modeling the Dynamics of Epistemic States*, Cambridge, MA: MIT Press.

[^gärdenfors-1992]: –––, 1992, “Belief Revision: An Introduction” in Gärdenfors, P. (ed.), *Belief Revision* (Cambridge Tracts in Theoretical Computer Science), Cambridge: Cambridge University Press, 1–29.

[^gärdenfors-1988-2]: Gärdenfors, Peter and Makinson, David, 1988, “Revisions of Knowledge Systems Using Epistemic Entrenchment,” *Proceedings of the 2nd Conference on Theoretical Aspects of Reasoning and Knowledge*, San Francisco: Morgan Kauffman, 83–95.

[^gärdenfors-1995]: Gärdenfors, Peter & Rott, Hans, 1995, “Belief Revision,” in D.M. Gabbay & C.J. Hogger & J.A. Robinson (eds.), *Epistemic and Temporal Reasoning* (Handbook of Logic in Artificial Intelligence and Logic Programming: Volume 4), Oxford: Clarendon Press, 35–132.

[^genin-2019]: Genin, Konstantin, 2019, “Full and Partial Belief,” in R. Pettigrew and J. Weisberg (eds.), *The Open Handbook of Formal Epistemology*, PhilPapers Foundation, pp. 437–498; [Genin 2019 available online](https://jonathanweisberg.org/pdf/open-handbook-of-formal-epistemology.pdf).

[^genin-2018]: Genin, Konstantin and Kelly, Kevin T., 2018, “Theory Choice, Theory Change, and Inductive Truth-Conduciveness,” *Studia Logica*, 107: 949–989.

[^gettier-1963]: Gettier, Edmund L., 1963, “Is justified true belief knowledge?” *Analysis*, 23(6): 121–123.

[^giang-2000]: Giang, Phan H. & Shenoy, Prakash P., 2000, “A Qualitative Linear Utility Theory for Spohn’s Theory of Epistemic Beliefs,” in C. Boutilier & M. Goldszmidt (eds.), *Uncertainty in Artificial Intelligence* (Volume 16), San Francisco: Morgan Kaufmann, 220–229.

[^glymour-1980]: Glymour, Clark, 1980, *Theory and Evidence*, Princeton: Princeton University Press.

[^goldblatt-2005]: Goldblatt, Robert, 2005, “ Mathematical modal logic: A view of its evolution, *Handbook of the History of Logic* (Volume 6), D. Gabbay and J. Woods (eds.), Amsterdam: North-Holland, pp. 1–98.

[^greaves-2006]: Greaves, Hilary & Wallace, David, 2006, ”Justifying Conditionalization: Conditionalization Maximizes Expected Epistemic Utility,“ *Mind*, 115: 607–632.

[^grove-1988]: Grove, Adam, 1988, ”Two Modellings for Theory Change,“ *Journal of Philosophical Logic*, 17: 157–170.

[^hacking-1967]: Hacking, Ian, 1967, ”Slightly More Realistic Personal Probability,“ *Philosophy of Science*, 34(4): 311–325.

[^hacking-1975]: –––, 1975, *The Emergence of Probability*, Cambridge: Cambridge University Press.

[^hacking-2001]: –––, 2001, *An Introduction to Probability and Inductive Logic*, Cambridge: Cambridge University Press.

[^haenni-2009]: Haenni, Rolf, 2009, ”Non-Additive Degrees of Belief,“ in F. Huber & C. Schmidt-Petri (eds.), *Degrees of Belief*, Dordrecht: Springer.

[^haenni-2003]: Haenni, Rolf & Lehmann, Norbert, 2003, ”Probabilistic Argumentation Systems: A New Perspective on Dempster-Shafer Theory,“ *International Journal of Intelligent Systems*, 18: 93–106.

[^hájek-1998]: Hájek, Alan, 1998, ”Agnosticism Meets Bayesianism,“ *Analysis*, 58: 199–206.

[^hájek-2003]: –––, 2003, ”What Conditional Probability Could Not Be,“ *Synthese*, 137: 273–323.

[^hájek-2005]: –––, 2005, ”Scotching Dutch Books?“ *Philosophical Perspectives*, 19: 139–151.

[^hájek-2006]: –––, 2006, ”Interview on Formal Philosophy,“ in V.F. Hendricks & J. Symons (eds.), *Masses of Formal Philosophy*, Copenhagen: Automatic Press.

[^hájek-2008]: –––, 2008, ”Arguments for – or against – Probabilism?“ *British Journal for the Philosophy of Science*, 59: 793–819. Reprinted in F. Huber & C. Schmidt-Petri (2009, eds.), *Degrees of Belief*, Dordrecht: Springer, 229–251.

[^hájek-2017]: Hájek, Alan and Lin, Hanti, 2017, ”A tale of two epistemologies?“ *Res Philosophica*, 94(2): 207–232.

[^halpern-2003]: Halpern, Joseph Y., 2003, *Reasoning about Uncertainty*, Cambridge, MA: MIT Press.

[^halpern-2015]: –––, 2015, ”The Role of the Protocol in Anthropic Reasoning,“ *Ergo*, 2: 195–206.

[^harman-1986]: Harman, Gilbert, 1986, *Change in view: Principles of Reasoning*, Cambridge, MA: MIT Press.

[^harper-1976]: Harper, William L., 1976, ”Ramsey Test Conditionals and Iterated Belief Change,“ in W.L. Harper & C.A. Hooker (eds.), *Foundations of Probability Theory, Statistical Inference, and Statistical Theories of Science* (Volume I), Dordrecht: D. Reidel, 117–135.

[^hansson-1999a]: Hansson, Sven Ove, 1999a, ”A Survey of Non-Prioritized Belief Revision,“ *Erkenntnis*, 50: 413–427.

[^hansson-1999b]: –––, 1999b, *A Textbook of Belief Dynamics: Theory Change and Database Updating*, Dordrecht: Kluwer.

[^hansson-2005]: –––, 2005, ”Interview on Formal Epistemology,“ in V.F. Hendricks & J. Symons (eds.), *Formal Philosophy*, Copenhagen: Automatic Press.

[^hawthorne-2009]: Hawthorne, James, 2009, ”The Lockean Thesis and the Logic of Belief,“ in F. Huber & C. Schmidt-Petri (ed.), *Degrees of Belief*, Dordrecht: Springer.

[^hawthorne-1999]: Hawthorne, James & Bovens, Luc, 1999, ”The *Preface*, the *Lottery*, and the Logic of Belief,“ *Mind*, 108: 241–264.

[^hawthorne-2004]: Hawthorne, John, 2004, *Knowledge and Lotteries*, Oxford: Oxford University Press.

[^hempel-1962]: Hempel, Carl Gustav, 1962, ”Deductive-Nomological vs. Statistical Explanation,“ in H. Feigl & G. Maxwell (eds.), *Scientific Explanation, Space and Time* (Minnesota Studies in the Philosophy of Science: Volume 3), Minneapolis: University of Minnesota Press, 98–169.

[^hendricks-2006]: Hendricks, Vincent F., 2006, *Mainstream and Formal Epistemology*, New York: Cambridge University Press.

[^hild-1998]: Hild, Matthias, 1998, ”Auto-Epistemology and Updating,“ *Philosophical Studies*, 92: 321–361.

[^hild-2008]: Hild, Matthias & Spohn, Wolfgang, 2008, ”The Measurement of Ranks and the Laws of Iterated Contraction,“ *Artificial Intelligence*, 172: 1195–1218.

[^hintikka-1961]: Hintikka, Jaakko, 1961, *Knowledge and Belief*, *An Introduction to the Logic of the Two Notions*, Ithaca, NY: Cornell University Press. Reissued as J. Hintikka (2005), *Knowledge and Belief: An Introduction to the Logic of the Two Notions*, prepared by V.F. Hendricks & J. Symons, London: King’s College Publications.

[^horgan-2017]: Horgan, Terry, 2017, ”Troubles for Bayesian formal epistemology,“ *Res Philosophica*, 94(2): 223–255.

[^horty-2012]: Horty, John F., 2012, *Reasons as Defaults*, Oxford: Oxford University Press.

[^howson-2006]: Howson, Colin & Urbach, Peter, 2006, *Scientific reasoning: the Bayesian approach*, Chicago: Open Court Publishing.

[^huber-2006]: Huber, Franz, 2006, ”Ranking Functions and Rankings on Languages,“ *Artificial Intelligence*, 170: 462–471.

[^huber-2007]: –––, 2007, ”The Consistency Argument for Ranking Functions,“ *Studia Logica*, 86: 299–329.

[^huber-2009]: –––, 2009, ”Belief and Degrees of Belief,“ in F. Huber & C. Schmidt-Petri (eds.), *Degrees of Belief*, Dordrecht: Springer, 1–33.

[^huber-2013a]: –––, 2013a, ”Belief Revision I: The AGM Theory,“ *Philosophy Compass*, 8: 604–612.

[^huber-2013b]: –––, 2013b, ”Belief Revision II: Ranking Theory,“ *Philosophy Compass*, 8: 613–621.

[^huber-2014]: –––, 2014, ”For True Conditionalizers Weisberg’s Paradox is a False Alarm,“ *Symposion*, 1: 111–119.

[^huber-2018]: –––, 2018, *A Logical Introduction to Probability and Induction*, New York: Oxford University Press.

[^huber-2019]: –––, 2019, ”Ranking Theory,“ in R. Pettigrew and J. Weisberg (eds.), *The Open Handbook of Formal Epistemology*, Philpapers Foundation, 397–436; [Huber 2019 available online](https://jonathanweisberg.org/pdf/open-handbook-of-formal-epistemology.pdf).

[^huber-2020]: –––, 2020, *Belief and Counterfactuals: A Study in Means-End Philosophy*, New York: Oxford University Press.

[^jeffrey-1970]: Jeffrey, Richard C., 1970, ”Dracula Meets Wolfman: Acceptance vs. Partial Belief,“ in M. Swain (ed.), *Induction, Acceptance, and Rational Belief*, Dordrecht: D. Reidel, 157–185.

[^jeffrey-1983a]: –––, 1983a, *The Logic of Decision*, 2nd edition, Chicago: University of Chicago Press.

[^jeffrey-1983b]: –––, 1983b, ”Bayesianism with a Human Face,“ in J. Earman (ed.), *Testing Scientific Theories* (Minnesota Studies in the Philosophy of Science: Volume 10), Minneapolis: University of Minnesota Press, 133–156.

[^jeffrey-2004]: –––, 2004, *Subjective Probability. The Real Thing*, Cambridge: Cambridge University Press.

[^joyce-1998]: Joyce, James M., 1998, ”A Nonpragmatic Vindication of Probabilism,“ *Philosophy of Science*, 65: 575–603.

[^joyce-1999]: –––, 1999, *The Foundations of Causal Decision Theory*, Cambridge: Cambridge University Press.

[^joyce-2005]: –––, 2005, ”How Probabilities Reflect Evidence,“ *Philosophical Perspectives*, 19: 153–178.

[^joyce-2009]: –––, 2009, ”Accuracy and Coherence: Prospects for an Alethic Epistemology of Partial Belief,“ in F. Huber & C. Schmidt-Petri (eds.), *Degrees of Belief*, Dordrecht: Springer.

[^kahneman-1982]: Kahneman, Daniel & Slovic, Paul & Tversky, Amos (eds.), 1982, *Judgment Under Uncertainty: Heuristics and Biases*, Cambridge: Cambridge University Press.

[^kaplan-1996]: Kaplan, Mark, 1996, *Decision Theory as Philosophy*, Cambridge: Cambridge University Press.

[^kelly-1996]: Kelly, Kevin T., 1996, *The Logic of Reliable Inquiry*, Oxford: Oxford University Press.

[^kelly-nd]: –––, forthcoming, ”Beliefs, Probabilities and their Coherent Correspondence,“ in I. Douven (ed.), *Lotteries, Knowledge and Rational Belief: Essays on the Lottery Paradox*, Cambridge: Cambridge University Press.

[^keynes-1921]: Keynes, John Maynard, 1921, *A Treatise on Probability*, in *The Collected Writings of John Maynard Keynes* (Volume 8, Elizabeth Johnson and Donald Moggridge, editors), Cambridge, Cambridge University Press, 1973.

[^kneale-1949]: Kneale, William C., 1949, Probability and Induction. Oxford: Clarendon Press.

[^kolmogorov-1956]: Kolmogorov, Andrej N., 1956, *Foundations of the Theory of Probability*, 2nd edition, New York: Chelsea Publishing Company.

[^korb-1992]: Korb, Kevin B., 1992, ”The Collapse of Collective Defeat: Lessons from the Lottery paradox,“ in D. Hull, M. Forbes and K. Okruhlick (eds.) *Proceedings of the Biennial Meeting of the Philosophy of Science Association* 1992(1): 230–236.

[^krantz-1971]: Krantz, David H. & Luce, Duncan R. & Suppes, Patrick & Tversky, Amos, 1971, *Foundations of Measurement* (Volume 1), New York: Academic Press.

[^kraus-1990]: Kraus, Sarit & Lehmann, Daniel & Magidor, Menachem, 1990, ”Nonmonotonic Reasoning, Preferential Models, and Cumulative Logics,“ *Artificial Intelligence*, 40: 167–207.

[^kripke-1979]: Kripke, Saul, 1979, ”A Puzzle About Belief,“ in A. Margalit (ed.), *Meaning and Use*, Dordrecht: D. Reidel, 239–283.

[^kroedel-2012]: Kroedel, Thomas, 2012, ”The Lottery Paradox, Epistemic Justification and Permissibility,“ *Analysis*, 52: 57–60.

[^kvanvig-1994]: Kvanvig, Jonathan L., 1994, ”A Critique of van Fraassen’s Voluntaristic Epistemology,“ *Synthese*, 98: 325–348.

[^kyburg-1961]: Kyburg, Henry E. Jr., 1961, *Probability and the Logic of Rational Belief*, Middletown, CT: Wesleyan University Press.

[^kyburg-1997]: –––, 1997, ”The rule of adjunction and reasonable inference,“ *The Journal of Philosophy*, 94(3): 109–125.

[^kyburg-2001]: Kyburg, Henry E. Jr. & Teng, Choh Man, 2001, *Uncertain Inference*, Cambridge: Cambridge University Press.

[^leibniz-1679]: Leibniz, Gottfried, 1679 [1989], ”On the General Characteristic“ in L. Loemker (ed.), *Philosophical Papers and Letters*, second edition, Dordrecht: Kluwer.

[^leitgeb-2004]: Leitgeb, Hannes, 2004, *Inference on the Low Level*: *An Investigation into Deduction, Nonmonotonic Reasoning, and the Philosophy of Cognition*, Dordrecht: Kluwer.

[^leitgeb-2013]: –––, 2013, ”Reducing Belief Simpliciter to Degrees of Belief,“ *Annals of Pure and Applied Logic*, 164: 1338–1389.

[^leitgeb-2014]: –––, 2014, ”The Stability Thoery of Belief,“ *Philosophical Review*, 123: 131–171.

[^leitgeb-2017]: –––, 2017, *The Stability Theory of Belief*, Oxford: Oxford University Press.

[^leitgeb-2020]: –––, forthcoming, ”A Structural Justification of Probabilism: From Partition Invariance to Subjective Probability,“ *Philosophy of Science*, first online 24 February 2020. doi:10.1086/711570

[^leitgeb-2010a]: Leitgeb, Hannes & Pettigrew, Richard, 2010a, ”An Objective Justification of Bayesianism I: Measuring Inaccuracy,“ *Philosophy of Science*, 77: 201–235.

[^leitgeb-2010b]: –––, 2010b, ”An Objective Justification of Bayesianism II: The Consequences of Minimizing Inaccuracy,“ *Philosophy of Science*, 77: 236–272.

[^levi-1967a]: Levi, Isaac, 1967a, *Gambling With Truth. An Essay on Induction and the Aims of Science*, New York: Knopf.

[^levi-1967b]: –––, 1967b, ”Probability Kinematics,“ *British Journal for the Philosophy of Science*, 18: 197–209.

[^levi-1974]: –––, 1974, ”On Indeterminate Probabilities,“ *Journal of Philosophy*, 71: 391–418.

[^levi-1977]: –––, 1977, ”Subjunctives, Dispositions and Chances,“ *Synthese*, 34(4): 423–455.

[^levi-1978]: –––, 1978, ”Dissonance and Consistency according to Shackle and Shafer,“ *PSA: Proceedings of the Biennial Meeting od the Philosophy of Science Association* (Volume 2: Symposia and Invited Papers), 466–477.

[^levi-1980]: –––, 1980, *The Enterprise of Knowledge*, Cambridge, MA: MIT Press.

[^levi-1991]: –––, 1991, *The Fixation of Belief and its Undoing*, Cambridge: Cambridge University Press.

[^lewis-1973]: Lewis, David K., 1973, *Counterfactuals*, Oxford: Blackwell.

[^lewis-1979]: –––, 1979, ”Attitudes *De Dicto* and *De Se*,“ *The Philosophical Review*, 88: 513–543; reprinted with postscripts in D. Lewis (1983), *Philosophical Papers* (Volume I), Oxford: Oxford University Press, 133–159.

[^lewis-1980]: –––, 1980, ”A Subjectivist’s Guide to Objective Chance,“ in R.C. Jeffrey (ed.), *Studies in Inductive Logic and Probability* (Volume II), Berkeley: University of Berkeley Press, 263–293; reprinted with postscripts in D. Lewis (1986), *Philosophical Papers* (Volume II), Oxford: Oxford University Press, 83–132.

[^lewis-1986]: –––, 1986, *On the Plurality of Worlds*, Oxford: Blackwell.

[^lewis-1999]: –––, 1999, ”Why Conditionalize?“ in D. Lewis (1999), *Papers in Metaphysics and Epistemology*, Cambridge: Cambridge University Press, 403–407.

[^lewis-2001]: –––, 2001, ”Sleeping Beauty: Reply to Elga,“ *Analysis*, 61: 171–176.

[^liao-2012]: Liao, Shen–yi, 2012, ”What are centered worlds?“ *The Philosophical Quarterly*, 62(247): 294–316.

[^lin-2012]: Lin, Hanti & Kelly, Kevin T., 2012, ”Propositional Reasoning that Tracks Probabilistic Reasoning,“ *Journal of Philosophical Logic*, 41: 957–981.

[^lin-2013]: Lin, Hanti, 2013, ”Foundations of everyday practical reasoning,“ *Journal of Philosophical Logic*, 42: 831–862.

[^lin-2019]: –––, 2019, ”Belief Revision Theory,“ in R. Pettigrew & J. Weisberg (eds.), *The Open Handbook of Formal Epistemology*, PhilPapers Foundation pp. 349–396; [Lin 2019 available online](https://jonathanweisberg.org/pdf/open-handbook-of-formal-epistemology.pdf).

[^lindström-1999]: Lindström, Sten & Rabinowicz, Wlodek, 1999, ”DDL Unlimited: Dynamic Doxastic Logic for Introspective Agents,“ *Erkenntnis*, 50: 353–385.

[^locke-1690]: Locke, John, 1690 [1975], *An Essay Concerning Human Understanding*, Oxford: Clarendon Press.

[^loeb-2002]: Loeb, Louis E., 2002, *Stability and Justification in Hume’s Treatise*, Oxford: Oxford University Press.

[^loeb-2010]: –––, 2010, *Reflection and the Stability of Belief*, Oxford: Oxford University Press.

[^maher-2002]: Maher, Patrick, 2002, ”Joyce’s Argument for Probabilism,“ *Philosophy of Science*, 69: 73–81.

[^maher-2006]: –––, 2006, ”Review of David Christensen, *Putting Logic in Its Place. Formal Constraints on Rational Belief*,“ *Notre Dame Journal of Formal Logic*, 47: 133–149.

[^mahtani-2019]: Mahtani, Anna, 2019, ”Imprecise Probabilities“ in R. Pettigrew and J. Weisberg (eds.), *The Open Handbook of Formal Epistemology*, PhilPapers Foundation, pp. 107–130; [Mahtani 2019 available online](https://jonathanweisberg.org/pdf/open-handbook-of-formal-epistemology.pdf).

[^makinson-1965]: Makinson, David, 1965, ”The Paradox of the Preface,“ *Analysis*, 25: 205–207.

[^makinson-1989]: –––, 1989, ”General Theory of Cumulative Inference,“ in M. Reinfrank & J. de Kleer & M.L. Ginsberg & E. Sandewall (eds.), *Non-Monotonic Reasoning* (Lecture Notes in Artificial Intelligence: Volume 346), Berlin: Springer, 1–18.

[^makinson-1994]: –––, 1994, ”General Patterns in Nonmonotonic Reasoning,“ in D.M. Gabbay & C.J. Hogger & J.A. Robinson (eds.), *Nonmonotonic Reasoning and Uncertain Reasoning* (Handbook of Logic in Artificial Intelligence and Logic Programming: Volume 3), Oxford: Clarendon Press, 35–110.

[^makinson-2009]: –––, 2009, ”Levels of Belief in Nonmonotonic Reasoning,“ in F. Huber & C. Schmidt-Petri (eds.), *Degrees of Belief*, Dordrecht: Springer.

[^makinson-1991]: Makinson, David & Peter Gärdenfors, 1991, ”Relations between the Logic of Theory Change and Nonmonotonic Logic,“ A. Fuhrmann & M. Morreau (eds.), *The Logic of Theory Change*, Berlin: Springer, 185–205.

[^makinson-2015]: Makinson, David and James Hawthorne, 2015 ”Lossy Inference Rules and their Bounds“ in A. Koslow and A. Buchsbaum (eds.) *The Road to Universal Logic*, Cham: Springer, pp. 385–407.

[^meacham-2008]: Meacham, Christopher, 2008, ”Sleeping Beauty and the Dynamics of *De Se* Belief,“ *Philosophical Studies*, 138: 245–269.

[^meacham-2011]: Meacham, Christopher & Weisberg, Jonathan, 2011, ”Representation Theorems and the Foundations of Decision Theory,“ *Australasian Journal of Philosophy*, 89: 641–663.

[^moss-2013]: Moss, Sarah, 2013, ”Epistemology Formalized,“ *Philosophical Review*, 122: 1–43.

[^moss-2018]: –––, 2018, *Probabilistic Knowledge*, Oxford University Press.

[^moon-2017]: Moon, Andrew, 2017, ”Beliefs do not come in degrees,“ *Canadian Journal of Philosophy*, 47(6): 760–778.

[^moore-1985]: Moore, Robert C., 1985, ”Semantical considerations on nonmonotonic logic,“ *Artificial Intelligence*, 25(1): 75–94.

[^nayak-1994]: Nayak, Abhaya C., 1994, ”Iterated Belief Change Based on Epistemic Entrenchment,“ *Erkenntnis*, 41: 353–390.

[^nelkin-2000]: Nelkin, Dana K., 2000, ”The Lottery Paradox, Knowledge and Rationality,“ *The Philosophical Review*, 109(3): 373–409.

[^niiniluoto-1983]: Niiniluoto, Ilkka, 1983, ”Novel Facts and Bayesianism,“ *British Journal for the Philosophy of Science*, 34: 375–379.

[^ninan-2010]: Ninan, Dilip, 2010, ”*De Se* Attitudes: Ascription and Communication,“ *Philosophy Compass*, 5: 551–567.

[^paris-1994]: Paris, Jeff B., 1994, *The Uncertain Reasoner’s Companion — A Mathematical Perspective* (Cambridge Tracts in Theoretical Computer Science: Volume 39), Cambridge: Cambridge University Press.

[^paris-2001]: –––, 2001, ”A Note on the Dutch Book Method,“ *Proceedings of the Second International Symposium on Imprecise Probabilities and their Applications*, Ithaca, NY: Shaker.

[^pascal-1658]: Pascal, Blaise, ca. 1658 [2004], ”Discourse on the Machine“ in R. Ariew (ed. and trans.), *Pensées*, Indianapolis: Hackett.

[^paxson-1969]: Paxson Jr., Thomas and Keith Lehrer, 1969, ”Knowledge: Undefeated Justified True Belief,“ *The Journal of Philosophy*, 66(8): 373– 409.

[^percival-2002]: Percival, Philip, 2002, ”Epistemic Consequentialism,“ *Supplement to the Proceedings of the Aristotelian Society*, 76: 121–151.

[^perry-1979]: Perry, John, 1979, ”The Problem of the Essential Indexical,“ *Noûs*, 13(1): 3–21.

[^pettigrew-2013]: Pettigrew, Richard, 2013, ”Accuracy and Evidence,“ *Dialectica*, 67: 579–596.

[^pettigrew-2016]: –––, 2016, *Accuracy and the Laws of Credence*, Oxford: Oxford University Press.

[^pettigrew-2019]: –––, 2019, ”Aggregating Incoherent Agents who Disagree,“ *Synthese*, 196: 2737–2776.

[^pettigrew-2020]: –––, forthcoming, ”Logical Ignorance and Logical Learning,“ *Synthese*, first online 05 June 2020. doi:10.1007/s11229-020-02699-9

[^peirce-1877]: Peirce, Charles Sanders, 1877 [1992], ”The Fixation of Belief,“ in N. Houser and C. Kloesel (eds.), *The Essential Peirce: Selected Philosophical Writings* (Volume 1: 1867–1893), Bloomington: Indiana University Press.

[^plaza-1989]: Plaza, Jan, 1989, ”Logics of public communication,“ in M.L. Emrich, et al. (eds.) *Proceedings of the 4th international symposium on methodologies for intelligent systems*, Oak Ridge, TN: Oak Ridge National Laboratory, pp. 201–216.

[^pollock-1987]: Pollock, John L., 1987, ”Defeasible Reasoning,“ *Cognitive Science*, 11(4): 481–518.

[^pollock-1995]: –––, 1995, *Cognitive Carpentry*, Cambridge, MA: MIT Press.

[^pollock-2006]: –––, 2006, *Thinking about Acting: Logical Foundations for Rational Decision Making*, Oxford: Oxford University Press.

[^popper-1955]: Popper, Karl R., 1955, ”Two Autonomous Axiom Systems for the Calculus of Probabilities,“ *British Journal for the Philosophy of Science*, 6: 51–57.

[^popper-1983]: Popper, Karl Y. & Miller, David, 1983, ”A proof of the impossibility of inductive probability,“ *Nature*, 302(5910): 687.

[^quine-1970]: Quine, Willard V.O. & Ullian, Joseph S., 1970, *The Web of Belief*, New York: Random House.

[^quine-1990]: Quine, Willard V.O., 1990, *Pursuit of Truth*, Cambridge: Harvard University Press.

[^raffman-2014]: Raffman, Diana, 2014, *Unruly Words. A Study of Vague Language*, Oxford: Oxford University Press.

[^raidl-2019]: Raidl, Eric, 2019, ” Completenes for Counter-Doxa Conditionals Using Ranking Semantics,“ *Review of Symbolic Logic*, 12(4): 861– 891.

[^raidl-2017]: Raidl, Eric and Niels Skovgaard-Olsen, 2017, ” Bridging Ranking Theory and the Stability Theory of Belief,“ *Journal of Philosophical Logic*, 46(6): 577– 609.

[^ramsey-1926]: Ramsey, Frank P., 1926, ”Truth and Probability,“ in F.P. Ramsey, *The Foundations of Mathematics and Other Logical Essays*, R.B. Braithwaite (ed.), London: Kegan, Paul, Trench, Trubner & Co., 1931, 156–198.

[^rényi-1955]: Rényi, Alfred, 1955, ”On a New Axiomatic System for Probability,“ *Acta Mathematica Academiae Scientiarum Hungaricae*, 6: 285–335.

[^rényi-1970]: –––, 1970, *Foundations of Probability*, San Francisco: Holden-Day.

[^resnik-1987]: Resnik, Michael D., 1987, *Choices: An Introduction to Decision Theory*, Minneapolis: University of Minnesota Press.

[^ross-1930]: Ross, David, 1930, *The Right and the Good*, Oxford: Oxford University Press.

[^rott-2001]: Rott, Hans, 2001, *Change, Choice, and Inference*, *A Study of Belief Revision and Nonmonotonic Reasoning*, Oxford: Oxford University Press.

[^rott-2009a]: –––, 2009a, ”Degrees All the Way Down: Beliefs, Non-Beliefs, Disbeliefs,“ in F. Huber & C. Schmidt-Petri (eds.), *Degrees of Belief*, Dordrecht: Springer.

[^rott-2009b]: –––, 2009b, ”Shifting Priorities: Simple Representations for Twenty-seven Iterated Theory Change Operators,“ in D. Makinson & J. Malinowski & H. Wansing (eds.), *Towards Mathematical Philosophy. Trends in Logic* 28, Dordrecht: Springer, 269–296.

[^rott-2017]: –––, 2017, ”Stability and Skepticism in the Modelling of Doxastic States: Probabilities and Plain Beliefs,“ *Minds and Machines*, 27(1): 167–197.

[^ryan-1996]: Ryan, Sharon, 1996, ”The Epistemic Virtues of Consistency,“ *Synthese*, 109(2): 121–141.

[^savage-1972]: Savage, Leonard J., 1972, *The Foundations of Statistics*, 2nd edition, New York: Dover.

[^schauer-2003]: Schauer, Frederick, 2003, *Profiles, Probabilities and Stereotypes*, Cambridge, MA: Belknap.

[^schurz-2011]: Schurz, Gerhard, 2011, ”Abductive Belief Revision in Science,“ in E. Olsson & S. Enqvist (eds.) *Belief Revision Meets Philosophy of Science*, Dordrecht: Springer, 77–104.

[^segerberg-1995]: Segerberg, Krister, 1995, ”Belief Revision from the Point of View of Doxastic Logic,“ *Bulletin of the IGPL*, 3: 535–553.

[^segerberg-1999]: –––, 1999, ”Two Traditions in the Logic of Belief: Bringing them Together,“ in H.J Ohlbach and U. Reyle (eds.), *Logic, Language and Reasoning: Essays in Honor of Dov Gabbay*, Dordrecht: Kluwer Academic Plublishers, pp. 135–147.

[^shackle-1949]: Shackle, George L.S., 1949, *Expectation in Economics*, Cambridge: Cambridge University Press.

[^shackle-1969]: –––, 1969, *Decision, Order, and Time*, 2nd ed. Cambridge: Cambridge University Press.

[^shafer-1976]: Shafer, Glenn, 1976, *A Mathematical Theory of Evidence*, Princteton, NJ: Princeton University Press.

[^shear-2018]: Shear, Ted and Branden Fitelson, 2018, ”Two Approaches to Belief Revision,“ *Erkenntnis*, 84(3): 487–518.

[^shenoy-1991]: Shenoy, Prakash P., 1991, ”On Spohn’s Rule for Revision of Beliefs,“ *International Journal for Approximate Reasoning*, 5: 149–181.

[^shoham-1987]: Shoham, Yoav, 1987, ”A semantical approach to nonmonotonic logics,’ in M. Ginsberg (ed.), *Readings in Nonmonotonic Reasoning*, San Francisco: Morgan Kaufmann, 227–250.

[^skyrms-1984]: Skyrms, Brian, 1984, *Pragmatism and Empiricism*, New Haven: Yale University Press.

[^skyrms-1987]: –––, 1987, “Dynamic Coherence and Probability Kinematics,” *Philosophy of Science*, 54: 1–20.

[^skyrms-2000]: –––, 2000 *Choice and Chance: An Introduction to Inductive Logic*, Belmont, CA: Wadsworth.

[^skyrms-2006]: –––, 2006, “Diachronic Coherence and Radical Probabilism,” *Philosophy of Science*, 73: 959–968; reprinted in F. Huber & C. Schmidt-Petri (eds.), *Degrees of Belief*, Dordrecht: Springer, 2009.

[^skyrms-2011]: –––, 2011, “Resiliency, Propensities and Causal Necessity,” in A. Eagle (ed), *Philosophy of Probability: Contemporary Readings*, London: Routledge, 529–536.

[^smets-2002]: Smets, Philippe, 2002, “Showing Why Measures of Quantified Beliefs are Belief Functions,” in B. Bouchon & L. Foulloy & R.R. Yager (eds.), *Intelligent Systems for Information Processing: From Representation to Applications*, Amsterdam: Elsevier, 265–276.

[^smets-1994]: Smets, Philippe & Kennes, Robert, 1994, “The Transferable Belief Model,” *Artifical Intelligence*, 66: 191–234.

[^spohn-1986]: Spohn, Wolfgang, 1986, “On the Representation of Popper Measures,” *Topoi*, 5: 69–74.

[^spohn-1988]: –––, 1988, “Ordinal Conditional Functions: A Dynamic Theory of Epistemic States,” in W.L. Harper & B. Skyrms (eds.), *Causation in Decision, Belief Change, and Statistics* (Volume II), Dordrecht: Kluwer, 105–134.

[^spohn-1990]: –––, 1990, “A General Non-Probabilistic Theory of Inductive Reasoning,” in R.D. Shachter & T.S. Levitt & J. Lemmer & L.N. Kanal (eds.), *Uncertainty in Artificial Intelligence* (Volume 4), Amsterdam: North-Holland, 149–158.

[^spohn-1994]: –––, 1994, “On the Properties of Conditional Independence,” in P. Humphreys (ed.), *Patrick Suppes: Scientific Philosopher* (Volume 1: Probability and Probabilistic Causality), Dordrecht: Kluwer, 173–194.

[^spohn-2009]: –––, 2009, “A Survey of Ranking Theory,” in F. Huber & C. Schmidt-Petri (eds.), *Degrees of Belief*, Dordrecht: Springer.

[^spohn-2012]: –––, 2012, *The Laws of Belief: Ranking Theory and Its Philosophical Applications*, Oxford: Oxford University Press.

[^spohn-2017a]: –––, 2017a, “Knightian Uncertainty and Ranking Theory,” *Homo Oeconomicus*, 34(4): 293–311.

[^spohn-2017b]: –––, 2017b, “ The Epistemology and Auto-Epistemology of Temporal Self-Location and Forgetfulness,” *Ergo*, 4(13): 359–418

[^spohn-2020]: –––, 2020, “Defeasible Normative Reasoning,” *Synthese*, 197: 1391–1428.

[^staffel-2013]: Staffel, Julia, 2013, “Can there be reasoning with degrees of belief?” *Synthese*, 190(16): 3535–3551.

[^staffel-2016]: –––, 2016, “Beliefs, Buses and Lotteries: Why Rational Belief Can’t Be Stably High Credence,” *Philosophical Studies*, 173(7): 1721–1734.

[^staffel-2018]: –––, 2018, “How do beliefs simplify reasoning?” *Noûs*, 53(4): 937–962.

[^stalnaker-1970]: Stalnaker, Robert C., 1970, “Probability and Conditionality,” *Philosophy of Science*, 37: 64–80.

[^stalnaker-1981]: –––, 1981, “Indexical Belief,” *Synthese*, 49(1): 129–151.

[^stalnaker-1984]: –––, 1984, *Inquiry*, Cambridge, MA: MIT Press

[^stalnaker-1996]: –––, 1996, “Knowledge, Belief, and Counterfactual Reasoning in Games,” *Economics and Philosophy*, 12: 133–162.

[^stalnaker-2002]: –––, 2002, “Epistemic Consequentialism” *Supplement to the Proceedings of the Aristotelian Society*, 76: 153–168.

[^stalnaker-2003]: –––, 2003, *Ways a World Might Be*, Oxford: Oxford University Press.

[^stalnaker-2009]: –––, 2009, “Iterated Belief Revision,” *Erkenntnis*, 70: 189–209.

[^sturgeon-2008]: Sturgeon, Scott, 2008, “Reason and the Grain of Belief,” *Noûs*, 42: 139–165.

[^teller-1973]: Teller, Paul, 1973, “Conditionalization and Observation,” *Synthese*, 26: 218–258.

[^thoma-2019]: Thoma, Johanna, 2019, “Decision Theory,” in R. Pettigrew & J. Weisberg (eds.), *The Open Handbook of Formal Epistemology*, The PhilPapers Foundation, pp. 57–106; [Thoma 2019 available online](https://jonathanweisberg.org/pdf/open-handbook-of-formal-epistemology.pdf).

[^thomson-1986]: Thomson, Judith Jarvis, 1986, “Liability and Individualized Evidence,” *Law and Contemporary Problems*, 49(3): 199–219.

[^titelbaum-2013]: Titelbaum, Michael G., 2013, *Quitting Certainties: A Bayesian Framework Modeling Degrees of Belief*, Oxford: Oxford University Press.

[^ullman-margalit-1983]: Ullman-Margalit, Edna, 1983, “On Presumption,” *The Journal of Philosophy*, 80(3): 143–163.

[^ditmarsch-2007]: van Ditmarsch, Hans & van der Hoek, Wiebe and Kooi, Barteld, 2007, *Dynamic Epistemic Logic*, Dordrecht: Springer.

[^fraassen-1985]: van Fraassen, Bas C., 1985, “Belief and the Will,” *Journal of Philosophy*, 81: 235–256.

[^fraassen-1989]: –––, 1989, *Laws and Symmetry*, Oxford: Oxford University Press.

[^fraassen-1990]: –––, 1990, “Figures in a Probability Landscape,” in J.M. Dunn & A. Gupta (eds.), *Truth or Consequences*, Dordrecht: Kluwer, 345–356.

[^fraassen-1995]: –––, 1995, “Belief and the Problem of Ulysses and the Sirens,” *Philosophical Studies*, 77: 7–37.

[^neumann-1944]: von Neumann, John & Morgenstern, Oskar, 1944, *Theory of Games and Economic Behavior*, Princeton: Princeton University Press.

[^wright-1951]: von Wright, Georg Henrik, 1951, *An Essay in Modal Logic*, Amsterdam: North-Holland Publishing Company.

[^walley-1991]: Walley, Peter, 1991, *Statistical Reasoning With Imprecise Probabilities*, New York: Chapman and Hall.

[^weatherson-2005]: Weatherson, Brian, 2005, “Can We Do Without Pragmatic Encroachment?” *Philosophical Perspectives*, 19: 417–443.

[^weatherson-2007]: –––, 2007, “The Bayesian and the Dogmatist,” *Proceedings of the Aristotelian Society*, 107: 169–185.

[^weichselberger-2000]: Weichselberger, Kurt, 2000, “The Theory of Interval-probability as a Unifying Concept for Uncertainty,” *International Journal of Approximate Reasoning*, 24: 149–170.

[^weisberg-2009]: Weisberg, Jonathan, 2009, “Commutativity or Holism? A Dilemma for Jeffrey Conditionalizers,” *British Journal for the Philosophy of Science*, 60: 793–812.

[^weisberg-2011]: –––, 2011, “Varieties of Bayesianism,” in D.M. Gabbay & S. Hartmann & J. Woods (eds.), *Inductive Logic* (Handbook of the History of Logic: Volume 10), Amsterdam/New York: Elsevier, 477–551.

[^weisberg-2015]: –––, 2015, “Updating, Undermining, and Independence,” *British Journal for the Philosophy of Science*, 66: 121–159.

[^williams-2012]: Williams, Robert, 2012, “Gradational Accuracy and Nonclassical Semantics,” *Review of Symbolic Logic*, 5(4): 513–537.

[^williamson-1994]: Williamson, Timothy, 1994, *Vagueness*, New York: Routledge.

[^zadeh-1978]: Zadeh, Lotfi A., 1978, “Fuzzy Sets as a Basis for a Theory of Possibility,” *Fuzzy Sets and Systems*, 1: 3–28.
