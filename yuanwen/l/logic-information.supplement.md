# logic-information — supplement（supplement）

> （《logic-information》词条补充材料，源：plato.stanford.edu/entries/logic-information/supplement.html）

#### Supplement to Logic and Information

## Abstract Approaches to Information Structure

The material in the section constitutes some major instances very abstract approaches to information structure. The abstractness means that many connections with topics from the previous sections can be made, with no one connection being exclusive enough to warrant the material be placed in any one section as apposed to some other.

### Intuitionistic logic, Beth and Kripke models

Consider again the waiter-at-the-cafe example from section 1. We noted that it was the verbal interaction between several agents that facilitated the information flow that enabled the logical reasoning to be undertaken. Along with verbal interactions, there was another type of epistemic action crucial for execution of the dynamic reasoning procedure undertaken by the waiter, *observation*. Simply put, the waiter observed the coffees in his possession (and presumable the ticket with the table number and so forth), and these observations facilitated information flow between the waiter and the waiter’s physical environment, and this information flow too played a necessary role in enabling the waiter’s actions.

Beth models for constructive logic are needed when modelling the information update from observations in order that the primeness of disjunction be circumvented (see the following paragraph for an example of why it is that we should want to circumvent it). A disjunction operation is said to be *prime* when it obeys the conditions specified by (23) below. To see why this is a problem, consider the standard Kripke models for constructive logic:

$$\begin{align} \tag{21} x \Vdash A \rightarrow B &\text{ iff for all } y \in \mathbf{F}, \text{ s.t. } x \sqsubseteq y, \text{ if } y \Vdash A \text{ then } y \Vdash B \\ \tag{22} x \Vdash A \wedge B &\text{ iff } x \Vdash A \text{ and } x \Vdash B \\ \tag{23} x \Vdash A \vee B &\text{ iff } x \Vdash A \text{ or } x \Vdash B \end{align}$$

Take the states of $S$ to be stages of a scientific research project. Now consider (21). (21) makes sense on this interpretation. It means simply that $A \rightarrow B$ has been established at a particular stage $x$ in a research project iff at any future stage $y$ in our project, if *α* has established $A$, then *α* has established $B$. (22) makes sense under this interpretation, however (23) does not. (23) does not make sense because knowledge is not *prime* in the sense of (23). Clearly, $K_{\alpha}(A \vee B)$ does *not* imply that *either* $K_{\alpha}A$ *or* $K_{\alpha}B$ (see Beal and Restall 2006). In order to take care of this, we need a frame construction with different disjunction conditions.

The original (and arguably most straightforward) way to take care of this is via *Beth frames* (Beth 1955, 1956). The conceptual motivation behind Beth’s disjunction condition is straightforward. Beth’s disjunction condition states that $x \Vdash A \vee B$ iff either $A$ or $B$ *will* be established at some stage, where this stage is an informational development of $x$. In other words, if $K_{\alpha}(A \vee B)$, then *α* will establish $A$ or establish $B$ at a future stage of the research project. Note that this assumes logical omniscience on behalf of *α*. To get off the ground formally, we need to introduce (information-)*chains* and (information-)*bars*:

- **Chains:** Take an information frame $\mathbf{F} := \langle S, \sqsubseteq \rangle$. A subset $s$ of this partial order $\sqsubseteq$ will be *totally ordered* iff for all $x, y \in s$, either $x \sqsubseteq y$ or $y \sqsubseteq x. s$ will be *maximally totally ordered* iff $s$ is totally ordered, and there is no $y \in \mathbf{F}$ such that $y \not\in s$ and $s \cup \{y\}$ is a total order also. $s$ is a **chain** when $s$ is a maximal total order.
- **Bars:** $A$ subset $s' \subset S \mathbf{bars}$ an information state $x$ iff every chain $s$ through $x$ intersects $s'$.

The Beth model for disjunction (where $\llbracket{.}\rrbracket$ is an evaluation function) is as follows:

$$\tag{24} x \Vdash A \vee B \text{ iff } \llbracket A\rrbracket \cup \llbracket B\rrbracket \text{ bars } x $$

That is, for any possible course of research through $x$ (i.e., on any chain through $x)$ either $A$ will be established or $B$ will be established. The other connectives remain the same, with the caveat the propositions are closed under barring. That is, we get $x \in$ $\llbracket$$A$$\rrbracket$ whenever we have it for some $x$ that $\llbracket$$A$$\rrbracket$ bars $x$. This makes sense on our interpretation, since if *α* knows that $A$ will be established at *any* stage of research extending the present stage, then *α* will have established $A$ at the present stage.

Considerable work has been done in order to reveal the connections between modal information theory and constructive logic systems by van Benthem (2009). van Benthem begins by taking an informationalised model condition for the universal modality to be the following:

$$\tag{25} x \Vdash \Box \phi \text{ iff } \phi \text{ is true at all future states } y \sqsupseteq x $$

From here van Benthem may define constructive implication with the informationalised universal modal operator as $\Box(\phi \rightarrow \psi)$. Atomic propositions are upwardly preserved due to the addition of the atomic persistence law $p \rightarrow \Box p$. The existential modal operator $\Diamond$ is not persistent however, as facts higher up the information ordering may negate any proposition falling within the scope of $\Diamond$. Hence there is no constructive counterpart to the existential modality, and “Modulo a few technicalities, the intuitionistic language is the ‘persistent fragment’ of the modal one….”, van Benthem (2009: 257). In this case, we have a single constructive logic/modal logic framework that contains multiple views of informational processes.

### Algebraic and Other Approaches to Modal Information Theory and Related Areas.

Sadrzadeh (2009) develops algebraically an expressively rich modal logic for multi-agent information flow that rejects the necessity of positive introspection, negative introspection, and the T-axiom:

$$\begin{align} \tag{26} K_{\alpha}\phi &\Rightarrow K_{\alpha}K_{\alpha}\phi \\ \tag{27} \neg K_{\alpha}\phi &\Rightarrow K_{\alpha}\neg K_{\alpha}\phi \\ \tag{28} K_{\alpha}\phi &\Rightarrow \phi \end{align}$$

Although the rejection of the $T$-axiom seems odd at first, owing to the factive nature of knowledge, Sadrzadeh is not working with knowledge and belief, but with their weaker relatives, *appearance* (things appear to *α* to be thus and so) and *information* $(\alpha$ receives the possible false information) from which knowledge and belief may be gotten respectively if certain extra conditions are imposed.

Sadrzadeh’s motivation is to identify the minimal logical structures which allow for a compositional analysis of the epistemic actions (observations and announcements) which underpin the information flow at work. This is accomplished by the actions being understood as functions that take an agent (or groups of agents or parts of groups of agents) from one state (or certain states) of information to another (or others). Hence action composition is understood as an instance of function composition, and the algebraic semantics is lifted to the powerful compositional framework provided by *category theory* (see section 4.2 for further connections between category theory and the situation theory expounded in section 2). Sadrzadeh’s work is extended in Dyckhoff and Sadrzadeh (2010). Related work on an algebraic analysis of information update via epistemic actions, where such epistemic actions are understood as *resources* may be found in Baltag, Coeke, and Sadrzadeh (2007). For still further connections between modal logical and category theoretical notions such as coalgebras, fixpoint theory, and bisimulation with information flow. For an extension of the logical approach to the analysis of information flow via the logical apparatus of channel theory, see Seligman (2009).

A related modal informational framework for *being informed* is developed by Floridi (2006). Like Sadrzadeh and Dyckhoff, Floridi rejects the introspection axioms, however he retains an informational version of the $T$-axiom. This is due to Floridi working with his veridical notion of strongly semantic information, expounded in section 1.3. Floridi’s full logic of being informed is the modal logic KTB, which, reading $I_{\alpha}\phi$ as *α* *is informed that* $A$, takes as informationalised axioms the following:

$$\begin{align} \tag{29} &I\phi \rightarrow \phi \\ \tag{30} &I(\phi \rightarrow \psi) \rightarrow(I\phi \rightarrow I\psi) \\ \tag{31} &NI\phi \rightarrow \phi \\ \tag{32} &\vdash \phi , \vdash \phi \rightarrow \psi \Rightarrow \vdash \psi \\ \tag{33} &\vdash \phi \Rightarrow \vdash I\phi \end{align}$$

$U$ is the dual existential modality to $I$, that is, $N_{\alpha}\phi := \neg I_{\alpha}\neg \phi$, read as *α* *is uninformed*, or *for all* \(\alpha\)*’s information, it is possible that* *φ*.^{[[^note-s1]]} (Note that $NI\phi \rightarrow \phi$ is the derivable-in-KTB dual to the usual KTB axiom: $\phi \rightarrow NI\phi$.)

Floridi’s logic of being informed is a static system. It models the results of cognitive procedures rather than the properties of the cognitive procedures that bring these results about. However, Floridi is aware of the connections between KTB and constructive logics, and Primiero (2006, 2008) extends Floridi’s work into a type-theoretical constructive framework for *becoming* informed.

Another type-theoretical approach is Duzi’s (2010) type-theoretical approach. Duzi distinguishes between what she calls *empirical* and *analytic* information. As one would expect, empirical information is that which is gotten *a posteriori*, and analytic information is that which is gotten *a priori*. Logically true sentences and logical inferences convey the same empirical information, but their analytic information may differ. Analytic information is procedural information in the sense that it is individuated via the constructive procedures which take the reasoner to the truths in question. Duzi’s work is extended extensively in Duzi, Jespersen, and Materna 2010.


## Notes（原文脚注，引自主文）

[^note-s1]: S1. Floridi uses $U$ instead of $N$, but we have changed the notations here so as to guard against confusion with regard to the universal modality in situation semantics.