# Hyperintensionality
**First published Mon Feb 8, 2021; substantive revision Fri Jan 16, 2026**

*Berto, Francesco, Nolan, Daniel*

A *hyperintensional* concept draws a distinction between necessarily equivalent contents. If the concept is expressed by an operator, $H$, then $H$ is hyperintensional insofar as sentences $HA$ and $HB$ can differ in truth value in spite of $A$ and $B$’s being necessarily equivalent. Necessary equivalence is standardly understood in terms of possible worlds (ways things could be or have been): $A$ and $B$ are necessarily equivalent when true at the same worlds. This is sometimes put in terms of sentences *sharing an intension*. An *extensional* operator (e.g., Boolean negation) allows substitution *salva veritate* of sentences with the same extension, i.e., truth value: if $A$ has the same truth value as $B$, then also ${\sim}A$ has the same truth value as ${\sim}B$. An *intensional* operator (e.g., the box of necessity) allows substitution *salva veritate* of sentences that express necessarily equivalent contents: if $A$ is necessarily equivalent to $B$, then $\Box A$ has the same truth value as $\Box B$. The expression “hyperintensional” is thus for an $H$ that defies substitution *salva veritate* even of expressions with the same intension.

Cresswell (1975) introduced the expression “hyperintensional” to pick out a position in a sentence where substitution fails for logical equivalents. Nowadays the term is used more broadly, referring to unrestrictedly necessary equivalence. Candidates for unrestricted necessity often include, besides the necessity had by logical truths, mathematical and metaphysical necessity.

Hyperintensionality is pervasive. Here are your prospects of getting a job you may apply for:

**(1)**

You have 40% chances of succeeding.

**(2)**

You have 60% chances of failing.

These are necessarily equivalent. But framing effects phenomena (Tversky and Kahneman 1981; Kahneman 2011)[^kahneman-2011][^tversky-1981] show that people are more prone to believe in a positive outcome when presented with (1) than with (2). *Belief formation* seems sensitive to hyperintensional distinctions: we can come to believe different things depending on how necessarily equivalent options are presented to us (Berto and Özgün 2023)[^berto-2023][^berto-2023-2], and these framing effects have important societal impacts (Thaler and Sunstein 2008)[^thaler-2008].

On to your neighbor Mike:

**(3)**

Mike is Mike.

**(4)**

Mike is Jack the Ripper.

(3) is necessarily true. Suppose (4) is true. If “Jack the Ripper” works as a proper name, (4) is necessarily true, too (Barcan Marcus 1947; Kripke 1980)[^barcan-1947][^kripke-1980]. Thus, (3) and (4) are necessarily equivalent. But (3) is uninformative; learning (4) could save your life. *Information* displays hyperintensional features. You can know (3), not (4), *a priori*. Then the *a priori* has hyperintensional features too. Hyperintensionality pervades our intuitions on *propositional contents*, what interpreted sentences say or express (in context), independently from the invocation of belief or informativeness:

**(5)**

2+2 = 4.

**(6)**

Equilateral triangles are equiangular.

If mathematical necessity is unrestricted, (5) and (6) are true at the same possible worlds: all of them. They don’t seem to say the same because they are about different things: only one is about what two and two add up to. This happens also with contingent sentences:

**(7)**

Snow is white.

**(8)**

The proposition that snow is white is true.

(7) and (8) are true at the same worlds. They also don’t seem to say the same: only one is about a proposition.

The twentieth century witnessed an intensional revolution: *belief, information, knowledge, meaning, content, essence, explanation*, were analyzed via possible worlds and constructions out of them. Standard possible worlds semantics (SPWS) found applications in logic, linguistics, game theory, decision theory, economics, artificial intelligence: a success story of philosophy. But many of those notions are, arguably, hyperintensional (Section 1). SPWS tends to miss distinctions more fine-grained than necessary equivalence. But there are nuances, because what counts as sticking with SPWS is fuzzy: as we will see, one can still make various hyperintensional distinctions using tools available in the SPWS toolkit. Some have attempted to explain away hyperintensional intuitions (Section 2). One pressing issue, if such attempts fail, is the question of “just ‘how hyper’ hyperintensions are” (Jespersen & Duží 2015: 527)[^duží-2015][^jespersen-2015]. That is, we have to answer the question of what hyperintensional distinctions we need, and when we can associate two pieces of language with the same meaning. The structure of hyperintensionality is not well understood yet (Section 3). However, the early twenty-first century is seeing a hyperintensional revolution (Nolan 2014)[^nolan-2014], with different general approaches being developed (Section 4).

## 1. The Variety of Hyperintensional Phenomena

We divide candidate hyperintensional notions in two camps: *representational* concepts pertain to ways of representing the world (1a) in thought and (1b) in language. Sub-camp (1a) includes *believing, knowing, imagining*, *being* or *becoming informed*. (1b) includes the *meaning* and *content* of sentences, the behavior of pieces of language such as *conditionals,* the behavior of *truth in fiction*. (2) *Non-representational,* “worldly” concepts include *essence*, *grounding*, *metaphysical dependence*, and *explanation*. Some notions of philosophical interest do not fit neatly into either camp: *truthmaking,* the relationship between pieces of the world and the propositions they make true, might be representational or non-representational depending on where one draws the line, though we will include truthmaking in (2).

Even the broad outlines of this division are not uncontroversial, e.g., some claim that explanation and indicative conditionals essentially involve cognition, and so would involve mind-dependence (e.g., Lycan 2001)[^lycan-2001]. Others take explanation to be an objective, worldly matter (e.g., Kment 2014)[^kment-2014]. Some claim that there is “environmental” information (Barwise and Seligman 1997)[^barwise-1997][^barwise-1997-2], which should go into (2). We stick to what we take as mainstream views on where such concepts should go. We provide (a) a brief explanation of how they have been dealt with in SPWS; and (b) intuitive evidence of their seemingly hyperintensional nature. Theoretical approaches to hyperintensionality, described in Section 4 can be assessed in light of the range of cases covered below.

### 1.1 Hyperintensionality in Representation

#### 1.1.1 Intentional Concepts

*Intentionality* involves states of the mind directed towards contents, situations, etc. Two of the most studied of these states of mind are *knowledge* and *belief*. Since Hintikka (1962), these have been understood in epistemic logic as modals. In SPWS, they are characterized in terms of what is true throughout a set of possible worlds representing ways things could be, for all the cognitive agent knows, or given the agent’s evidence, etc. If $K$ expresses the agent’s knowledge or belief state, $w$ is a possible world, and $R$ an epistemic accessibility relation on the space of worlds $W$, Hintikka’s characterization is:

**(H)**

$KA$ is true at $w$ iff $A$ is true at all $w_1$ such that $wRw_1$.

Some mainstream epistemology follows a similar path, e.g., in *relevant alternatives* approaches knowledge is “an evidential state in which all relevant alternatives (to what is known) are eliminated” (Dretske 1981: 367)[^dretske-1981]. Uneliminated alternatives work similarly to accessible worlds.

The *problem of logical omniscience* (Fagin et al. 1995: 335–6)[^fagin-1995] was an early manifestation of hyperintensional issues for SPWS. Here is a set of closure conditions for the relevant $K$ which follow from understanding it in terms of (H), above:

**(C1)**

If $KA$ and $A$ entails $B$, then $KB$

**(C2)**

If $A$ is logically valid, then $KA$

**(C3)**

It is not the case that: $KA$ and $K{\sim}A$

(C1) is *Closure under entailment*, saying that a knower $K$s all the logical consequences of what one $K$s. $A$’s entailing $B$ standardly requires all $A$-worlds to be $B$-worlds in all models, and given that $KA$ means that $A$ is true at all the epistemically accessible worlds, $B$ will be true there, too; so $KB$ will hold. (C2), *Knowledge of /* *Belief in all validities*, has it that knowers $K$s all logical truths, and since any logical theorem $A$ is true at every possible world, it would have to be true in every accessible possible world. (C3) ensures the consistency of $K$: no possible world, thus no accessible one, will make both $A$ and ${\sim}A$ true.

All of C1 to C3 look implausible to many epistemologists. Against (C1): we know basic arithmetic truths like Peano’s axioms of arithmetic, and these entail (suppose) Goldbach’s Conjecture (Every even whole number larger than 2 is the sum of two primes); but we don’t know whether Goldbach’s Conjecture is true. (C2): “If ${\sim}{\sim}A$, then $A$” is (suppose) logically valid, but some logicians do not believe it in general, offering arguments that it faces counterexamples. (C3) is widely accepted for knowledge, but systems like Hintikka’s also have conditions (C1) to (C3) for belief, and we can have, at least implicitly, inconsistent beliefs: this is often what is going on when we are confused.

One may instead read “$KA$” in (H) as “$A$ follows logically from the agent’s knowledge”, or “The agent is committed to $A$, given what it knows/believes”. On this reading (C1) to (C3) are more plausible, but then we still lack some logical account of *knowledge* and *belief* per se, as opposed to some derivative attitude or commitment. Even this account of commitment may be questioned: are we committed to believing everything, given we have inconsistent beliefs? Why is a finite agent rationally committed to believing infinitely many things, just because there are infinitely many complex logical constructions that follow from what they believe?

In semantic accounts of *information* which originated with Bar-Hillel and Carnap (1952), the informative task of a statement $A$ is to split the totality of worlds into those where $A$ is true and those where it isn’t. An agent’s becoming informed of $A$ is about ruling out the not-$A$ worlds as contenders for actuality. But “If Rome is in Italy, Rome is in Italy” and “$x^n + y^n = z^n$ has no integer solutions for $n \gt 2$” are both true at all worlds. So one can rule out none after learning either. One easily deems the former true, while the proof of the latter (Fermat’s Last Theorem) is significant news.

Generalizing: all absolutely necessary truths and logical deductions are uninformative in a system like this. But logical deductions *are* informative (Jago 2009, 2014)[^jago-2009][^jago-2014]. Besides, we can become informed of exactly one of two necessarily equivalent claims. Of necessity, “All woodchucks are woodchucks” is true if and only if “All woodchucks are whistle-pigs” is (Ripley 2012)[^ripley-2012]. But the former is trivial; one may learn the latter from a zoologist.

*Hoping, fearing, supposing, imagining* (Wansing 2017)[^wansing-2017] display similar features. One may conclude that *thought* is hyperintensional: our intentional states can treat necessarily equivalent contents differently. We can suppose that $75 \times 12 = 900$ without supposing Fermat’s Last Theorem. Even states involving perceptual experiences, like *seeing*, seem hyperintensional: you can see that Mary is eating an ice cream without seeing that Mary is eating an ice cream and John is either eating chips or not (you may not be seeing John at all). But $A$ is logically equivalent to $A \land (B \lor {\sim}B)$ in classical logic and in many weaker logics (Barwise & Perry 1983)[^barwise-1983].

#### 1.1.2 Semantic Concepts

Propositions, the meanings of sentences, what they say or express, have often been interpreted starting from Wittgenstein’s insight that understanding a sentence is knowing what is the case if it is true (Wittgenstein 1921: 4.024)[^wittgenstein-1921]. Truth conditions have been given via sets of possible worlds in SPWS (Montague 1970; Stalnaker 1976; and many others)[^montague-1970][^stalnaker-1976]. But if a proposition is just a set of possible worlds, “If Rome is in Italy, then Rome is in Italy” and “$x^n + y^n = z^n$ has no integer solutions for $n \gt 2$” mean the same thing: the total set of worlds. However, the two sentences do not seem to say the same thing: only one is about Diophantine equations. So we may need to distinguish some necessarily equivalent propositions, like the ones corresponding to those two sentences. So for necessary falsehoods: “Rome is and is not in Italy” and “$2 + 3 = 6$” end up expressing the same proposition: the empty set. In the jargon, propositions may need to be *hyperintensionally individuated*.

Moving on to indicative conditionals, the extensional material conditional, “$\supset$”, validates inferences such as:

**(1)**

${\sim}A$, therefore $A \supset B$

**(2)**

$B$, therefore $A \supset B$

If the horseshoe captures the meaning of the indicative “if”, lots of bad-sounding conditionals come out true just because the antecedent is false or the consequent true: “If Clinton is Australian, then Mars is made of marbles”; “If Strasbourg is in Germany, then Clinton is American”. These notorious problems are known as “paradoxes of material implication”.

Perhaps “If $A$, then $B$” is only true if it cannot be the case that the antecedent is true while the consequent is false, per the so-called strict conditional: a modal, “$\prec$”, such that “$A \prec B$” is understood as “At any (accessible) possible world where $A$ is true, $B$ is true”. This has its paradoxes, too. Where “$\Box A$” means that $A$ is true at all possible worlds, and “$\Diamond A$” means that $A$ is true at some, we get:

**(3)**

${\sim}\Diamond A$, therefore $A \prec B$

**(4)**

$\Box B$, therefore $A \prec B$

When there is no way for $A$ to be true, or for $B$ to be false, “$A \prec B$” is automatically true. If the indicative “if” means “$\prec$”, “If $6 + 3 = 11$, then Clinton is Australian”, “If Clinton is American, then $6 + 3 = 9$”, come out true. These sound bad: antecedent and consequent have little to do with each other. Other logical forms that come out as validities when read with the strict conditional include:

**(5)**

$A \prec (B \prec B)$

**(6)**

$A \prec (B \lor {\sim}B)$

**(7)**

$(A \land {\sim}A) \prec B$

An example of (6) is “If Mars is made of marbles, then either ‘If Mars is made of marbles, then either St Andrews is in Scotland, or it isn’t”: the material constitution of Mars has little to do with St Andrews’ location. “If Mars is made of marbles, then either Mars is made of marbles, or it isn’t” looks much better. Since, plausibly, “Either St Andrews is in Scotland, or it isn’t” and “Either Mars is made of marbles, or it isn’t” are necessarily equivalent, an adequate account of indicative conditional sentences may have to go beyond the strict conditional, and arguably will need to make hyperintensional distinctions and not treat necessarily equivalent consequents or antecedents the same.

When it comes to counterfactuals or subjunctive conditionals, “If it were/had been the case that $A$, then it would be/have been the case that $B$”, the mainstream Stalnaker (1968)-Lewis (1973) account of their truth-conditions uses possible worlds. In a simple version: a counterfactual is true just in case at the relevantly most similar worlds where $A$ is true, $B$ is true. “If Kangaroos had no tails, they would topple over” is true when, at all worlds where kangaroos have no tails and which are as relevantly similar as it gets to the actual world, kangaroos topple over.

This analysis makes all counterfactuals with necessary consequents or impossible antecedents (*counterpossibles*) *vacuously* true, for there are no worlds to falsify the consequent, or to verify the antecedent. (This view of the behavior of counterpossibles is sometimes labelled *vacuism*.) But some counterpossibles appear to be false. An often-cited example from Nolan (1997) is the pair:

**(8)**

If Hobbes had (secretly) squared the circle, sick children in the mountains of South America at the time would have cared.

**(9)**

If Hobbes had (secretly) squared the circle, sick children in the mountains of South America at the time would not have cared.

Squaring the circle is a mathematical impossibility, in spite of Hobbes’ hopes. His achieving it would have made no difference for those sick children. (9) should come out true for this reason. For a similar reason, (8) should come out false. Some counterpossibles with same antecedent and opposite consequents should have different truth values. For a defense of the view that nevertheless, all counterpossibles are true, see Williamson (2007); for a critical discussion, see Berto et al. (2018); for retorts, see the second part of Williamson (2020). The literature on this debate has grown exponentially: Kocurek (2021) offers a masterful survey. Sendłak (2024) is a book-length survey, also presenting an original, syncretic non-vacuist account. Kocurek and Jerzak (2021) provide an original non-vacuist account of counterlogicals, i.e., counterpossibles about logical impossibilities. Güngör (2023) investigates the connections with Hurford disjunctions.

Recent papers suggest that non-trivial counterpossibles play a role in scientific inquiry: Baron et al. (2017), Jenny (2018), Tan (2019), McLoone (2021). If this is right, that is another reason to not treat all counterpossibles alike. McLoone et al. (2023) report empirical evidence that trained biologists converge in their judgements on an interesting class of counterpossible claims. But, for some scepticism about the role of counterpossibles in science, see Dohrn (2024).

Other cases where semantic hyperintensionality appears to play a role include *empty names* (Kosterec 2023)[^kosterec-2023] and especially *truth in fiction*. Some fictions describe things that could not possibly happen, or so it appears, but differ in content. Then impossibilities must be distinguished. (And we should distinguish between necessarily equivalent contingencies, and distinct necessary truths, though these receive less attention in the literature.)

One topic of debate is whether we should think that some impossibilities but not all are true according to some fictions. Authors including Routley (1979), Deutsch (1985), Priest (1997), and Kim (2025) agree that absolute impossibilities can occur in stories. Sendłak (2021) is a defence of the view that some impossible things but not others are true according to some fictions. Sendłak uses this to argue for the non-vacuity of counterpossibles. Some continue to maintain that only possibly true propositions are true according to fictions, including Hanley (2004), Bourne and Caddick Bourne (2016) and (2018). Xhignesse (2016) and (2021) argues for the weaker thesis that no contradiction is ever true in fiction. Nolan (2021a,b) surveys some options for a theory of impossible fictions.

Some defenders of impossible fictions, e.g., Deutsch (1985), claim that *any* combination of propositions can comprise a story. If this is right, Routley (1979) and Proudfoot (2018) argue, there cannot be a (non-trivial) general *logic* of fiction. Routley (1979), however, offers a logic of fiction he thinks applies to *most* fictions we deal with. Badura and Berto (2019) explore a non-monotonic logic to handle many of the impossible fictions that cause problems for traditional accounts of truth in fiction. Their idea is that reading fiction is like performing a simulated, iterated belief revision.

### 1.2 Worldly Hyperintensionality

Fine (1994) influentially argues that *essence* talk must be hyperintensional. In “$x$ is essentially $F$”, we cannot be guaranteed to preserve truth by substituting necessarily equivalent predicates, i.e., predicates whose extension coincides at all possible worlds. Socrates is (suppose) essentially human, but not essentially (human and a member of a set), although necessarily someone is human if and only if they are human and a member of a set. Fine extends this line of argument to claims of real definition in general: it is the real definition of 2 that it is the successor of 1, but not the real definition of 2 that it is $10-8$, even though “the successor of 1” and “$10-8$” necessarily have the same extension. (These examples are not in Fine 1994, but we take it he would endorse them given his discussion on pp. 4–5 and 14.)[^fine-1994] Dunn (1990b) also argues that one needs hyperintensional resources to capture essentialist claims.

According to Nolan (2014), *explanation*, metaphysical *grounding*, the distinction between *intrinsic* and *extrinsic* properties, and *dispositions*, are all hyperintensional. Nolan also mentions the analysis of *causation*, *laws of nature*, *confirmation*, objective *chance*, and *ethics*. Other hyperintensional proposals include work on *truthmakers*, *omissions*, metaphysical *dependence*, and the distinction between *qualitative* and *non-qualitative* properties. Miller (2024) argues that ontological categories are to be understood hyperintensionally if taken as modally robust. Miller (2017) also provides a general hyperintensional account of when two metaphysical theories count as equivalent. In this section we will discuss a range of examples where hyperintensionality appears to be due to the facts beyond facts about how things are represented.

In the case of counterfactuals, discussed above, it is at least arguable that hyperintensional distinctions reflect worldly differences. For example, the truth of many counterfactuals appears to depend on the world beyond our representations. (Or so Nolan 2014 argues.)[^nolan-2014] Regular platonic solids come in only a handful of sizes (the most sides one can have, in three-dimensional space, is 20.) Still, this seems true:

**(1)**

If there were a piece of steel in the shape of a 36 sided platonic solid, it would have more sides than any piece of steel in the shape of a dodecahedron.

On the other hand,

**(2)**

If there were a piece of steel in the shape of a 36 sided platonic solid, it would have fewer sides than any piece of steel in the shape of a dodecahedron.

seems false. The truth value of these is not just settled by whether the antecedent is necessary. They seem to be about pieces of steel and how they relate to each other. Which blocks of steel have which shapes is not just about our representations. It would not be even if steel could take shapes that it in fact cannot.

*Explanation* seems to be hyperintensional: “explains”, “because”, etc., can be flanked by expressions that cannot be substituted with necessary equivalents *salva veritate*. One pure mathematical truth can explain another, but not every mathematical truth explains every other (Baron et al. 2020)[^baron-2020]. Schneider (2011) argues that some, but not all, logical equivalents explain each other: ${\sim}{\sim}A$ is true because $A$ is true, not vice versa. If the correctness of explanations turns out to depend also on how the world is, rather than only on what suits our explanatory practices, these cases may be due to hyperintensional explanatory connections in the world.

*Grounding* is widely regarded as hyperintensional. That Socrates and Plato both exist grounds the existence of {Socrates, Plato} (Dunn 1990b; Fine 1994)[^dunn-1990b][^fine-1994], and not the other way around, although the two are intensionally inseparable. Perhaps complex logical truths are grounded in simpler ones. ${\sim}{\sim}A$ is grounded in $A, (A \land A)$is grounded in $A$, and not the other way around (see Poggiolesi 2018, 2020)[^poggiolesi-2018][^poggiolesi-2020].

If “grounds” is a sentential operator, as in “(Socrates and Plato both exist) grounds (The set {Socrates, Plato} exists)”, the cases discussed had best be captured hyperintensionally. But a second view takes “grounds” as a two-place predicate applying to facts: “The fact that Socrates and Plato both exist grounds the fact that {Socrates, Plato} exists” expresses a relation between two facts and we might be able to preserve the truth of this statement by substitution of any other ways of referring to each of them. One complication is that one might take expressions picking out facts to themselves sometimes have constituents designating propositions: “the fact that Socrates and Plato both exist” may have the logical form *the fact that* $A$, where *that* $A$ is the proposition that Socrates and Plato exist. Interpreted that way, the expression is functioning hyperintensionally, since the necessarily equivalent proposition that {Socrates, Plato} exists cannot be substituted *salva veritate* into that expression.

A third view is to take grounding relations as holding between objects in general: Socrates and Plato ground the set {Socrates, Plato} (Schaffer 2009)[^schaffer-2009]. Now it is natural to think that any other ways of designating those objects could be substituted *salva veritate* so that the grounding-between-objects predicate is extensional; though see Jenkins (2011) for a hyperintensional object-theoretic grounding approach that does not allow this substitution *salva veritate.* Some grounding theorists have favoured the sentential operator approach: Fine (2001: 15–16), Schneider (2011: 446–7). The other views fall on different sides of the question of the hyperintensionality of grounding. See Duncan, Miller, and Norton (2017) on which styles of grounding claims are best treated as hyperintensional.

The distinction between *intrinsic* and *extrinsic* *properties* appears to be representation-independent: if mass is intrinsic it would remain such whatever we said or thought. Say that a property is had intrinsically when had only in virtue of an object’s nature, extrinsically when it is at least partly due to relations to other objects. Necessarily coextensive properties, according to some, can differ in whether they are intrinsic or extrinsic (Dunn 1990a; Eddon 2011; Bader 2013; Marshall 2015; Hoffmann-Kloss 2015)[^bader-2013][^dunn-1990a][^eddon-2011][^marshall-2015]. *Being an instance of Barak’s actual favorite property* is plausibly extrinsic, but *having a mass* may well be intrinsic, even if mass is Barak’s favorite property, and even though, given it is actually his favorite property, anything in any possible world has the first property iff it has the second. The above-named philosophers disagree on how to characterize the intrinsic/extrinsic distinction, but they share the view that it is hyperintensional.

Azzano (2024) argues that a proper account of *dispositional properties* goes along well with worldly hyperintensionality. Jenkins and Nolan (2012) argue that disposition ascriptions are hyperintensional. Heidi the gifted mathematician may be disposed to find the proof of a given conjecture, if it has one; this can be known in advance of knowing whether the conjecture has a proof. (“Give this to Heidi: if there’s a proof to be found, she’ll find it”.) Suppose the conjecture is in fact false, though the mathematical community does not yet know that. Then the condition of the disposition ascription is impossible. Still, we cannot substitute any impossibility in the disposition ascription. It is false that Heidi is disposed to find the proof of that conjecture, on the condition that she was always both identical to the number 7 and innumerate.

We use necessarily false conditions in disposition ascriptions outside talk about agents, too. A model where the number of prey killed is a function of the number of predators might say adding half a fox to a closed ecosystem, or adding $1/\pi$ foxes to an ecosystem, produces a certain fraction of additional rabbits killed. It is impossible to have, e.g., $7+1/\pi$ foxes. Still, what the ecosystem is disposed to do on the condition $7+1/\pi$ foxes are added *and* it is idealized in various ways is very different from what it is disposed to do with $105+1/\pi$ foxes and the same idealization.

*Probability* assignments to propositions, claims such as “$\rP(A) = 0.6$”, where $A$ is, e.g., that this (biased) coin will come up heads 10 times in a row, will be hyperintensional if we cannot guarantee that we preserve truth value by substitution of necessary equivalents. If we use $\rP$ to represent credences—even of logically idealized agents—we might allow different probability assignments to necessarily equivalent propositions: a logically perfect agent may be uncertain on whether water = H₂O before investigating, in spite of certainty on the self-identity of water. If the hyperintensional probability function represented *objective chance* or *frequency*, however, hyperintensionality may also be tied to how the world is. Nolan (2016a) and Salmon (2019) both argue that objective chance ascriptions are hyperintensional.

“Ought” seems hyperintensional: perhaps you ought to call your sister, but it is not the case that you ought to call your sister and be self-identical, though the two complements are intensionally inseparable. Such obligations might be dependent on our representational practices. But perhaps they pertain to objective morality. Perhaps your moral obligation to not callously cause suffering is like this. Objective obligations might be best construed as hyperintensional: the Moral Law may enjoin you to avoid callously inflicting suffering, but it may be silent about whether you ought to avoid inflicting callous suffering while being self-identical. Faroldi (2019) has a comprehensive hyperintensional treatment of “ought”.

*Truthmaker* theories in metaphysics deal with what in the world makes true propositions true. Some are hyperintensional: $A$ and $B$ may be necessarily equivalent, yet the worldly bit that makes $A$ true is distinct from the one that makes $B$ true. As Restall (1996a) points out, this seems to follow if one also endorses the Disjunction Thesis: something is a truthmaker for (*$A$ or $B$*) iff it is a truthmaker for $A$ or a truthmaker for $B$. If we endorse this, then not every truthmaker for ($A$ or ${\sim}A$) will be a truthmaker for ($B$ or ${\sim}B$), even though those two instances of excluded middle are not just necessarily equivalent but logically equivalent. Independently of the Disjunction Thesis, a truthmaker for one necessary truth may plausibly not be a truthmaker for all others: “There are infinitely many prime numbers” should have as truthmaker (something to do with) numbers. “Anyone who eats and drinks, eats” seems not to have to do with numbers. See MacBride (2013, 2020, the SEP entry on truthmakers, section 1) for accounts where necessarily equivalent propositions need not have the same truthmaker.

Impossible *occurrences* may have explanatory and even causal consequences. A mathematical conjecture might have a counterexample that nobody has yet noticed. Still, that the conjecture is not proved may have effects: if you bet that you will prove it by a certain time you will lose; if your tenure case in the mathematics department turns on whether you managed to prove the conjecture, you will miss out on tenure. Bernstein (2016) gives a theory of omissions of impossible outcomes, arguing they play explanatory and causal roles.

Hoffmann-Kolss (2015) argues that a number of classifications of properties are hyperintensional. One is the *qualitative/non-qualitative* distinction between properties that do not require a relationship to a particular and those that do—e.g., *being square* vs. *being John’s neighbor* (see also Hoffman-Kolss 2019). The dispositional/categorical distinction is arguably hyperintensional (Hoffmann-Kolss 2015: 341–342, 346)[^hoffmann-kolss-2015]. (One controversial example: on some theories, there is a necessarily-existing God that is necessarily the only omnipotent being. Still, we might think *being omnipotent* is dispositional, concerning the powers of that being, while *being God* is categorical (2015: 346).) The one between *perfectly natural properties* that best carve at the joints, and the others, is, too (2015: 345). Hoffman-Kolss’s example here is to contrast the (supposedly) perfectly natural property of being an electron with the infinitely disjunctive identity property of *being $e_1$* or *being $e_2$* or… and so on for all possible electrons $e$. If electronhood is essential to the objects that have it, something is an electron if and only if it is one of $e_1$, $e_2$, etc., but this latter condition is not perfectly natural. Defenses of the view that properties should be individuated hyperintensionally are in Snodgrass (2024,2025). Vacek and Vacek (2025) argue that also artworks and art in general provide examples of worldly hyperintensionality. Elohim (2018) links hyperintensionality to the mind-body problem.

*Any* item on this list will be controversial. You might think that what explains what is essentially a matter of the representations we make of the world. One could try to explain away grounding’s putative hyperintensionality in terms of our cognitive structures, as Thompson (2016) suggests. Thompson and Byrne (2019) offer a general “conceptualist” alternative to taking any of the cases we discussed as requiring non-representational phenomena to be characterized in hyperintensional terms: an explanation of our use of hyperintensional language to capture these phenomena comes from an account of what it is to describe and explain in these areas (2019: 157). Lenta (2023) retorts, in defense of worldly hyperintensionality, that locating the sources of hyperintensionality should not be pre-judged by preferences about the semantics of the language we use to describe the phenomena.

## 2. Is Hyperintensionality Real?

This section discusses objections to the significance or tenability of hyperintensional distinctions. One argument has to do with a general “Boolean” challenge to formulating a semantics for hyperintensional expressions in the dominant truth-conditional framework (§2.1). Another, advanced by Stalnaker (1984) and Lewis (1982, 1986), has it that the *prima facie* hyperintensionality of knowledge, belief, or content is deceptive: SPWS can still do the job once misleading intuitions have been explained away (§2.2). Williamson (2020, 2021, 2024) targets both semantic and metaphysical hyperintensionality, arguing that unreliable heuristics produce the misleading intuitions (§2.3).

### 2.1 Hyperintensional Truth Conditions

One way to modify SPWS is to resort to sets including both possible and *impossible worlds* (ways things could *not* have been). Sentences that agree in truth value in every possible world can still be assigned distinct truth-conditions: they might be true in different impossible worlds. (See §4.3). Another way is to use *structured propositions*, whereby sentences with the same possible-worlds truth conditions can have different meanings because of the way they are built up. (See §4.5). An objection to these approaches can be generalized to any view making room for hyperintensionality in a truth-conditional framework.

The objection to hyperintensional distinctions understood in this way, presented in Cresswell (2002) against structured propositions and suggested by Stalnaker (1996) against impossible worlds, can be illustrated by focusing on negation. Given $A$, what truth-conditions can we offer for ${\sim}A$? Plausibly, they can be exhausted by specifying that ${\sim}A$ is true when $A$ is false, not otherwise. Since this exhausts the meaning of “${\sim}$”, it is tempting to identify the proposition ${\sim}A$ as being the one with this truth condition. Plausibly, also, the truth conditions for ${\sim}{\sim}A$ will just be the truth conditions for $A$. (We may even want to derive this claim from plausible principles about truth, falsehood, necessity.) Now suppose $C$ and $D$ are distinct, necessarily equivalent propositions. Then ${\sim}C$ will be the proposition that is true just in case $C$ is false, and ${\sim}D$ will be the proposition that is true just in case $D$ is false: so ${\sim}C$ and ${\sim}D$ will be the same proposition. But then there will be a unique proposition with the truth conditions for ${\sim}{\sim}C (/{\sim}{\sim}D)$, since ${\sim}{\sim}C$ is the negation of ${\sim}C$. So $C$ and $D$ must be the same proposition. This is a *reductio* of the hypothesis that there can be a hyperintensional distinction between $C$ and $D$: if necessarily equivalent, they are identical.

We might call this an objection from Booleanism, because uniqueness of truth-conditional complementation is characteristic of Boolean approaches to negation. Similar objections can be motivated by Boolean thoughts about other operations. We might hope to define conjunction so that necessarily, $(A \land B)$ is true iff $A$ is true and $B$ is true, and indeed the truth condition for the proposition that $(A \land B)$ is just that both $A$ and $B$ are true. But then, with other innocuous assumptions, any two necessarily equivalent sentences will express the same proposition.

Cresswell (1975) was one of the pioneers of structured approaches to sentence meaning to handle hyperintensionality. So it is significant that he thinks this objection refutes a contention at the heart of orthodox structured meaning projects, though Cresswell thinks we may still be interested in semantic structures for reasons other than how they might make a difference to the truth-conditions of complex embeddings.

Defenders of hyperintensional meanings need to resist the idea that for each proposition $A$ there is only one proposition true whenever, and only whenever, $A$ is false. This leaves them with a challenge: how are we to understand logical operations such as negation and conjunction once Boolean characterizations are rejected?

### 2.2 Can We Explain Away Apparently Hyperintensional Distinctions?

The *prima facie* hyperintensionality of belief, information, meaning, etc., might be resisted. One strategy invokes use/mention distinctions. We can treat apparently hyperintensional language as expressing properties of, or relations between, pieces of language. Quine (1953) suggests that modal operators are best interpreted as predicates of sentences. Quine (1956) and Davidson (1968) suggest an approach to propositional attitude ascriptions as implicitly talking about connections between people and sentences: “John believes that it is raining” is regimented as a two-place predicate holding between John and the sentence “It is raining”. For Davidson, this in effect asserts that John stands in a certain relation to a sentence that stands in the same-saying relation to the sentence “It is raining”. This supposedly accommodates how non-English speakers can believe that it is raining.

Reconstruing attitude ascriptions as reporting relations to sentences has fallen out of favor, for reasons orthogonal to hyperintensionality: see the entry on propositional attitude reports. Still, similar techniques might be extended to apparently hyperintensional language. Stalnaker (1984) tries to rescue the SPWS analysis of content via a metalinguistic approach: when we fail to see that a proposition is necessarily true, or that two propositions are necessarily equivalent, we are actually failing to see what propositions are expressed by sentences. One should distinguish (1) the proposition $P$ expressed by $A$ (in a context), and (2) the proposition $P$* that *A* expresses $P$, relating the sentence to what it expresses. Ignorance of necessary truths or equivalences is ignorance about *P\*.*

Stalnaker maintains that whenever one fails to know or believe a necessary truth, $A$, one actually fails to fully grasp the sentence $A$’s meaning: one doesn’t realize that $A$ expresses the total set of worlds. He points at the occasional distance between syntactic structure, which can be quite complex, and the expressed proposition—in SPWS, a set (Stalnaker 1984: 84)[^stalnaker-1984].

For Stalnaker’s story to work in general, all cases of ignorance of necessary truths or equivalences must be instances of meaning ignorance. But a mathematician who wonders whether Goldbach’s conjecture is true can hardly be described as mistaken about what “Every even integer larger than two is the sum of two primes” means. They know the meanings of all constituents of the sentence—they have mastered the elementary-school-math concepts *even integer*, *larger than*, *two*, *sum*, *prime number* as much as any of us. As competent speakers of English, they understand how the syntax of the sentence makes its constituents conjure for it to express the content it expresses. What they have doubts about is whether *that* content is true. See Bjerring and Tang (2023) for further criticism of the Stalnakerian strategy.

Lewis (1982) proposes a fragmentation strategy to explain away apparent failures of logical omniscience, in particular, apparent belief in inconsistencies which is not, however, belief in everything. One’s epistemic state may be split into different “frames of mind”. One may believe $A$ in one frame, ${\sim}A$ in another, but fail to put two and two together. Each fragment can be given the SPWS treatment, while trans-fragmental inconsistencies do not trivialize. But, it seems strange to say that when agents don’t follow through the logical consequences of what they believe, it’s always because they haven’t conjoined the premises whereas, when they do, they suddenly come to believe the infinitely many consequences (Jago 2014)[^jago-2014]. It’s sometimes an easy logical step from $A_1, A_2, A_3$, to $A_1 \land A_2 \land A_3$. What is often difficult is to see whether a remote $B$ follows from $A_1 \land A_2 \land A_3$.

Lewis seems more hospitable than Stalnaker to hyperintensional approaches, provided they can be ultimately explained in terms of possible worlds and individuals and set-theoretic constructions out of them. Lewis (1986: 49–50) discusses a hyperintensional “trivially” operator that would apply differently to different necessary truths. Lewis (1986: 56) conjectures a structured account to tell properties like *triangular* and *trilateral* apart even if they are co-intensional. In a posthumously published letter (Lewis 2004)[^lewis-2004] he seems to acknowledge that there is more than one distinct impossible fiction. Then “According to fiction $f, A$” is hyperintensional, since when $f$ is an impossible fiction, there will be some impossible claim that is true according to it, but in general not all impossible claims will be. Lewis’s moves in several of these cases raise and point we will meet again: one may represent various hyperintensional distinctions using tools already available, in some sense, in SPWS. Some may see this as a partial vindication of theories of hyperintensionality, while others may see it as being good news for deflationary accounts of hyperintensional distinctions.

### 2.3 Heuristics and Overfitting

Williamson (2020, 2021, 2024) argues that intuitions used to motivate semantic and metaphysical hyperintensionality depend on faulty “heuristics”: rough-and-ready cognitive procedures that can lead us astray. Mistaking such flawed intuitions for genuine data, hyperintensional theories are guilty of *overfitting*: they introduce extra parameters or distinctions, besides those of SPWS or non-hyperintensional metaphysics, to fit misleading data.

Williamson (2020) argues that the indicative conditional is the extensional material conditional; that the counterfactual is not hyperintensional, and all counterpossibles are trivially true. He does it, partly, by arguing that contrary intuitions are based on inconsistent heuristics. His “primary heuristics” are variations on the Ramsey Test (Ramsey 1990)[^ramsey-1990]: we assess conditionals primarily by supposing the antecedent and evaluating the consequent under the supposition. Williamson shows, e.g., that when taken as governing credences, the heuristics lead to paradoxes akin to Lewis’s (1976) “triviality results”, showing that the probabilities of conditionals cannot in general equate the corresponding conditional probabilities. His “secondary heuristics” concern how conditionals are passed on through speakers.

Williamson (2024) expands to other heuristics we use to ascribe mental states and answer “why?”-questions. We’ll just report one of Williamson’s many objections, invoking the “why?” heuristic: we accept (reject) “*A* because *B*” when (besides judging both *A* and *B* true) we find *B* a good (bad) reply to the question, “Why *A*?”. Some examples adapted from Williamson (2021, 2024):

**(1)**

It is essential to Socrates that he is Socrates.

**(2)**

It is essential to Socrates that he is a member of {Socrates}.

**(3)**

The proposition that snow is white is true because snow is white.

**(4)**

Snow is white because the proposition that snow is white is true.

**(5)**

Richard’s actions brought it about that Edward was a king.

**(6)**

Richard’s actions brought it about that Edward was a self-identical king.

In each pair, either comes from the other by replacement of intensional equivalents. But, we tend to accept the first item in each pair and reject the second. We are guided by intuitions like those invoked in the first section of this entry, on the hyperintensionality of “it is essential that”, “because” (truth depends on facts, not vice versa), “bringing it about” (Richard Neville, the Kingmaker, could make Edward Plantagenet into a king, but Edward was self-identical already).

But we have the same inclinations to these pairs:

**(7)**

Vera is a vixen because Vera is a female fox.

**(8)**

Vera is a female fox because Vera is a vixen.

**(9)**

Richard’s actions made Edward a king.

**(10)**

Richard’s actions made Edward a male monarch.

**(11)**

Furze is as prickly as gorse because furze is gorse.

**(12)**

Furze is as prickly as gorse because furze is furze.

These differ pairwise only by substitution of synonyms (pretend “king” and “male monarch” are; they probably aren’t). So they cannot express different propositions! So our intuitions are faulty, wich casts a shadow on all of (1)–(6).

Explanatory thinking guided by the “why?” heuristic is “sensitive to the vagaries of conversational context, background knowledge, and human psychology” (Williamson, 2024: 146)[^williamson-2024]. We invoke the more familiar (“female fox”, snow’s being white) to explain the less so (“vixen”, what makes a proposition true), not vice versa. But one shouldn’t postulate semantic or metaphysical distinctions to accommodate phenomena that pertain to the messy psychology of understanding and communication. Adding distinctions to a model just to fit spurious data is overfitting.

The heuristics-and-overfitting strategy is relatively new at the time of our writing, but has been met with criticism already. Opponents of Williamson’s approach have argued that it is insufficient to save a SPWS analysis of content (Berto 2025a)[^berto-2025a]; that Williamson’s theory of conditionals is under-developed science (Rothschild 2021)[^rothschild-2021]; that Williamson got the primary heuristic for indicatives wrong by deeming it inconsistent (Salerno 2022)[^salerno-2022]; that he got the primary heuristic for counterfactuals wrong, for the same reason (Berto 2025b)[^berto-2025b]; that he mischaracterises the secondary heuristic (Krzyżanowska and Douven 2023)[^krzyżanowska-2023]. Williamson advances his heuristics as “psychological hypothes[e]s, which in the end must live or die by psychological evidence” (Williamson, 2020: 22)[^williamson-2020]. So it has also been argued that he got such evidence wrong (van Rooij et al. 2023)[^rooij-2023]; that his views on the primary heuristics (Berto 2022b)[^berto-2022b] and on people assessing counterpossibles by comparing opposite ones (Byrne 2024)[^byrne-2024] are empirically refuted.

## 3. Granularity and the Structure of Hyperintensionality

We now investigate what is known about the general structure of hyperintensionality. The initial characterization, recall, merely tells us that a concept or operator is hyperintensional when it is more fine-grained than intensional or standard modal concepts or operators. As Jespersen and Duží reminded us, little is said on “how hyper” hyperintensions are. The tag of “granularity problems” (Barwise 1997; Jago 2014; Bjerring & Schwarz 2017; Correia 2020)[^barwise-1997][^barwise-1997-2][^bjerring-2017][^correia-2020][^jago-2014] labels a set of issues concerning the right level of fine-grainedness. Different hyperintensional concepts seem to display different degrees of fine-grainedness. This may be understood again in terms of substitution *salva veritate* for the relevant operators: $X$ is strictly more fine-grained than $Y$ when all substitutions that go through for *X* also do for *Y*, but $X$ fails some, which goes through for *Y*.

A hyperintensional account shouldn’t deliver contents as fine-grained as the syntax of the target language. If propositions were be mappable 1:1 to the sentences expressing them, we would lose one motivation for having propositions, namely that syntactically different sentences can sometimes say the same thing. It also seems intuitive that, e.g., the content of $A$ should be the same as that of $A \land A$, and that $A \land B$ should have the same content as $B \land A$: “It’s windy and rainy today” seems to say the same thing as “It’s rainy and windy today” (for further motivations for coarse-graining, see Bjerring and Schwarz 2017)[^bjerring-2017].

On the other hand, limited cognitive agents may fail to make even the simplest inference from what they know or believe: can’t one believe that $A \land B$, fail to perform Conjunction Elimination, and thus fail to believe that $A$? Psychologically realistic accounts seem to require extreme fine-grainedness, cutting more finely than same-saying. Jespersen (2010) is one example of a theory that has fine-grained meanings available for some constructions, while offering more coarse-grained meanings for traditional purposes where little or no hyperintensionality is required (see also Duží and Jespersen 2015; Jespersen 2025)[^duží-2015][^jespersen-2015].

One may hope for a total ordering of hyperintensional notions by fine-grainedness: given any $X$ and $Y$, either $X$ is at least as fine-grained as $Y$, or vice versa. But this appears to be wrong. One can provide intuitive examples (inspired by Hornischer 2017, which also includes a thorough discussion)[^hornischer-2017] of incomparable hyperintensional operators $X$ and *Y,* for which there are sentences $A$, $B$, $C$, $D$, such that *XA* and *XB* are equivalent but *YA* and *YB* are not, *YC* and *YD* are equivalent but *XC* and *XD* are not.

Take “Lois Lane knows that …” and “… because Clark Kent loves the Guggenheim Museum”. Consider the four sentences:

- $A =$ Clark Kent loves the Guggenheim Museum
- $B =$ “Clark Kent loves the Guggenheim Museum” is true
- $C =$ Clark Kent is in New York
- $D =$ Superman is in New York

Lois Lane knows that $A$ (Clark Kent loves the Guggenheim Museum) if and only if she knows that $B$ (“Clark Kent loves the Guggenheim Museum” is true) (surely Lois knows how truth works!). On the other hand, she knows that $C$ (Clark Kent is in New York), but she doesn’t know that $D$ (Superman, too, is), for she is not aware that Superman is Clark Kent. Also, it is false that $A$ (Clark Kent loves the Guggenheim Museum) because Clark Kent loves the Guggenheim Museum (facts can’t explain themselves), while it is true that $B$ (“Clark Kent loves the Guggenheim Museum” is true) because Clark Kent loves the Guggenheim Museum (assuming truth supervenes on/is grounded in facts). On the other hand, $C$ (Clark Kent is in New York) because Clark Kent loves the Guggenheim Museum if and only if $D$ (Superman is in New York) because Clark Kent loves the Guggenheim Museum, for Superman is Clark Kent.

So *knows* and *because* turn out to be incomparable. This may sustain some skepticism (ventilated, e.g., in Leitgeb 2019)[^leitgeb-2019] on the possibility of a single theory for all hyperintensional operators. It makes sense to conjecture that these can be at least partially ordered. It is then an issue worth investigating, whether concepts belonging to a single sub-family, e.g., the non-representational ones, or the representational semantic ones, can be internally totally ordered (notice that *knows* is representational; one may take *because* as belonging to “ontic” explanation). Or, vice versa, the identification of totally ordered subsets of the partially ordered set of hyperintensional concepts may group such concepts into families that carve at the joints. Taking the notion of substitution as primitive, Bacon (2019) provides one of the few mathematically sophisticated accounts to model the hyperintensional granularity of propositions and properties in a general setting.

## 4. General Approaches to Hyperintensionality

Hardly any of the approaches we survey now has been put forth as a systematic account of all putatively hyperintensional notions. We focus on frameworks that are general enough to handle a broad range of phenomena (thus we do not consider, e.g., epistemic logics that target only certain forms of logical omniscience, like justification logic). We briefly introduce the key ideas of each approach and discuss how it handles phenomena introduced in Section 1.

### 4.1 Two-Dimensional Semantics

Two-dimensional semantics builds on SPWS to handle a range of representational hyperintensional phenomena. Originating in two-dimensional modal logic (Segerberg 1973; van Fraassen 1977; Davies and Humberstone 1980)[^davies-1980][^segerberg-1973], versions have been presented by Kaplan (1989), Jackson (1994), and Chalmers (1996). (Stalnaker 1978 is a pioneer, but he applied it to pragmatics rather than semantics; see also Stalnaker 2004.)[^stalnaker-1978][^stalnaker-2004]

Sometimes what a word picks out depends on context. Indexicals (“I”, “you”, “here”, “yesterday”), demonstratives (“this”, “that”, “over there”), are obvious cases: what someone refers to using “this” depends on what they are demonstrating. Kaplan (1989) proposed that these expressions function as rigid designators on occasions of use. If on 5 March 2020 I say “Yesterday it was sunny”, I express a proposition true at a possible world iff it is sunny on 4 March 2020 in that world. Elvis says “I was born in 1935”: that is true at a possible world iff *Elvis* was born in 1935 there.

On this view, “I am Elvis”, said by Elvis, is true just in case Elvis is Elvis, thus necessarily true. Ditto for “Yesterday was 4 March 2020”, said on 5 March 2020, which is true just in case 4 March 2020 is 4 March 2020. Expressing those necessary truths can, however, be informative to hearers. To capture the difference between “I am Elvis” and “Elvis is Elvis”, when uttered by Elvis as well as by someone else—say, Aretha—we would need a story about the meaning of “I” that did not treat it as a name. Kaplan took such meaning as a function from a context of utterance to an object, selecting the speaker as the object. Similarly, the meaning of “yesterday” is a function from the day of utterance, selecting the day before. This function is called the *character* of the expression. My knowing the character (and facts about context) lets me take new information from the utterances. I know “I” picks out the speaker and that the speaker said “I am Elvis”. I can learn the speaker is Elvis, although I already knew that Elvis is Elvis.

Meanings have two components: a *character* and a *content*. The content is normally given via possible worlds. The character is a function from contexts of utterance to contents. The content of “I am Elvis”, uttered by Elvis, is the total set of worlds, since Elvis couldn’t but be Elvis. The character is a function from the context’s speaker to the content that that person is Elvis. So it is a function from Elvis to the content that Elvis is Elvis, from Aretha to the content that Aretha is Elvis, etc.

Philosophers have found it useful to represent this interaction with a two-dimensional matrix. For a small example: in *w*₁, Elvis is singing but Aretha is not; in *w*_{2,} Aretha is singing but Elvis is not; in *w*₃, neither is singing. Take “I am singing”, with possible speakers Elvis and Aretha. We get six possible scenarios:

|   | $W_1$ | $W_2$ | $W_3$ |
| --- | --- | --- | --- |
| Elvis | T | F | F |
| Aretha | F | T | F |

Each row of the matrix represents a content that can be associated with “I am singing”, with different rows representing the different contents produced by different contexts due to different speakers. The entire matrix represents facts about the character of a sentence. These two-dimensional matrices become more interesting when more complex constructions are discussed.

Some proponents of two-dimensional semantics extend this setting beyond indexicals and demonstratives, e.g., to proper names and natural kind terms. Take “Robin Hood”. Its content, suppose, is just Robin. But its character is a function from contexts to such contents. In a world where our use of “Robin Hood” derives in the right way from Robin, the character delivers our Robin as the content of “Robin Hood”. In a world where Richard leads a band of outlaws in Sherwood, uses “Robin Hood” as an alias, is famous for robbing for the rich to give to the poor, the character of “Robin Hood” picks out Richard. Similarly “water” and H₂O in our world, but XYZ in Twin Earth: the character of “water” picks out different substances in different contexts.

Character-sensitive expressions can give rise to hyperintensionality. Take “It is *a priori* that”: It is *a priori* that Hesperus is Hesperus; it is not *a priori* that Hesperus is Phosphorus. Although “Hesperus” and “Phosphorus” have the same content (planet Venus), they can differ in character. There may be contingent *a priori* cases: Elvis says “I am here now” in a context where the assigned content is that Elvis Presley is in Graceland on noon of 25 December 1975. “I am here now”, some claim, can be known *a priori* by Elvis, but he cannot know *a priori* that Elvis is in Graceland on noon of 25 December 1975.

Propositional attitude contexts make for a salient case. The Sheriff of Nottingham believes Robin Hood is a dangerous outlaw. He does not believe that Robin of Locksley is a dangerous outlaw, although Robin Hood is Locksley. We can explain this if we take “believes that” as character-sensitive. “Robin Hood is a dangerous outlaw” and “Robin of Locksley is a dangerous outlaw” are true in the same worlds. But we can assign different characters to “Robin Hood” and “Robin of Locksley” looking at differences in how they are typically acquired, or linking them to how the Sheriff sees the world. This can be generalized to intensional transitive verbs. The Sheriff can be looking for Robin Hood but not looking for Robin of Locksley if “looking for” is sensitive to character.

Two-dimensional approaches get controversial when they move beyond indexicals and demonstratives. (See the papers in García-Carpintero and Maciá 2006 for arguments for and against.)[^garcía-carpintero-2006] But they account for the hyperintensionality of “it is *a priori* that” or “believes that” without straying too far from SPWS. Contents keep being sets of possible worlds. Qua functions from contexts to contents, characters are familiar from Kaplanian treatments of context-dependent expressions.

Two-dimensional semantics also has a nice story on the behavior of indexicals in belief contexts. “I believe you are Elvis”, said addressing Elvis, appears to mean something different from “I believe Elvis is Elvis”. I would happily utter the latter but not the former if I believe I am facing an Elvis impersonator. It seems that the character of expressions like “you” (or, “yesterday”, “that car”, etc.) makes the difference.

It is hard to see how to use two-dimensional resources to handle worldly hyperintensionality. When, e.g., talk of essence is employed, and we say that Socrates is essentially human but is not essentially (human and $2 + 2 = 4)$, or not essentially (human and either bats have wings or it is not the case that bats have wings), those two alternatives to “human” both have the same two-dimensional intension as “human”. Any context will pick out the same content for the predicates “is human”, “is human and such that $2 + 2 = 4$”, and “is human and either bats have wings or it is not the case that bats have wings”.

The full range of non-trivial counterpossible conditionals are also not easily handled. Take “If Hobbes had squared the circle, Hobbes would have proved an impressive mathematical result”. This is plausibly true, whereas “If Archimedes had squared the circle, Hobbes would have proved an impressive mathematical result” is false: Archimedes lived well before Hobbes and so would have beaten him to it, and Hobbes did not otherwise prove any impressive results. The necessary falsehoods “Hobbes squared the circle” and “Archimedes squared the circle” seem to deliver different truth values as antecedents in same-consequent counterfactuals. Functions from contexts to contents taken as the usual sets of possible worlds don’t deliver the result: whichever other person a context picks out for “Hobbes”, it is hard to see how “$x$ squared the circle” could pick out a contingent proposition that would be useful. Prospects are not quite hopeless here: approaches that employ two-dimensionalism as part of the picture about *indicative* conditionals have been suggested by Weatherson (2001) and Nolan (2003). One might hope for an extension to counterfactuals. Or perhaps some other approach might work: work on counter-analytic conditionals done by Locke (2021) and Kocurek et al. (2020) is promising.

### 4.2 Aboutness, Topics, Subject Matter

Some theories of content represent a number of hyperintensional distinctions by combining SPWS with ways of splitting modal space. The main work is Yablo’s book *Aboutness* (2014; see also Yablo 2017; Plebani 2020; Osorio-Kupferblum 2016 for a critical discussion; see also Osorio-Kupferblum 2024 on historical accounts of aboutness)[^osorio-kupferblum-2016][^osorio-kupferblum-2024][^plebani-2020][^yablo-2017].

Aboutness is “the relation that meaningful items bear to whatever it is that they are *on* or *of* or that they *address* or *concern*” (Yablo 2014: 1)[^yablo-2014], also called their *subject matter*. The subject matter of a sentence in context can be seen as a *topic*, an issue, or question the sentence can be taken, in that context, as answering to. When the issue is *the number of stars*, the relevant question may be: “How many stars are there?”. As in inquisitive semantics (Ciardelli et al. 2013)[^ciardelli-2013], one can associate the question with the set of its answers: There are no stars; There is one star; There are two stars; etc. Answers are propositions in the SPWS sense: sets of possible worlds. We now call these *thin* propositions, for the full propositional contents of sentences will be richer than that. The question, thus, splits the totality of worlds into sets (the relevant thin propositions). Two worlds $w_1$ and $w_2$ end up in the same set just in case they agree on the answer—in our example: when the number of stars is the same at $w_1$ and $w_2$. When, as in the example, the question has just one correct answer, the thin propositions at issue form a partition of the set of worlds $W$: a splitting into subsets such that their union is all of $W$ and each $w$ in $W$ is in exactly one subset or cell. One cell has all the 0-star worlds, one all the 1-star worlds, one all the 2-star worlds, and so on. The account features no big departure from SPWS, in a way: we only work with sets of possible worlds.

While the idea is already in Lewis (1988) (see also Plebani and Spolaore, 2021)[^plebani-2021], Yablo proposes a generalization due to some questions’ having more than one correct answer: “Where’s a good Italian restaurant in Amsterdam?”. A world $w_1$ can be in more than one cell now: it can agree with $w_2$ by having a good Italian restaurant in Rembrandtplein, with $w_3$ by having another good Italian restaurant in Keizersgracht. Here the question determines a division of $W$: a splitting into subsets whose union is $W$, but which can overlap.

There’s an intuitive mereology of topics or subject matters: they should be capable of overlapping and of fusing into wholes, inheriting features from the parts (Yablo 2014: Section 3.2)[^yablo-2014]. The topic *philosophy* and the topic *mathematics* overlap (the overlap including, presumably, *logic*). *How things went in 1882* is included in the larger *how things went in the nineteenth century*. A larger subject matter induces smaller cells: $w_1$ and $w_2$ agree on what happened in their whole nineteenth century only if they agree on what happened in their 1882 to begin with.

Let $|A|$, a subset of $W$, be the thin proposition expressed by $A$. The *thick* proposition expressed by $A$, [$A$], is its thin proposition $|A|$ together with $A$’s subject matter, $s(A)$. How does one get *the* subject matter of $A$? Yablo suggests assigning a positive subject matter, the division corresponding to “Why is $A$ true?”; a negative subject matter, the division corresponding to “Why is $A$ false?”; and to identify the overall $s(A)$ with its positive and negative subject matters taken together. Worlds agree on the overall subject matter of $A$ when either $A$ is true, or $A$ is false, for the same reasons at them. Yablo calls the reasons for $A$’s being true (false), $A$’s *truthmakers* (*falsemakers*). He suggests not to read them in a metaphysically loaded way and advocates a “semantic” conception of truthmaking: truth/falsemakers are cells of divisions of $W$, thus, just sets of worlds again, i.e., thin propositions.

Thick propositions are hyperintensional insofar as there are $A$s and $B$s such that $s(A)$ differs from $s(B)$ even if $|A| = |B|$. To get a precise answer on which hyperintensional distinctions can be made, one needs a full-fledged truthmaker assignment to all sentences of the target language. Yablo gives two “semantic pictures”, a *reductive* and a *recursive* one, which pull in different directions. We take the recursive route, which relies on van Fraassen (1969) and is found more plausible by some (e.g., Hawke 2018; Fine 2020)[^fine-2020][^hawke-2018], and leave the details to a consultation of Yablo (2014: 56–9). In a plain sentential language: when $A$ is an atomic formula $p$ one can assign it truthmakers $\{p^+\}$ and falsemakers $\{p^-\}$. Negation flips: For $A = {\sim}B$, what truthmakes $A$ is what falsemakes $B$ and vice versa. For $A = B \land C$, what truthmakes $A$ is the union of what truthmakes $B$ and what truthmakes $C$; what falsemakes $A$ is what either falsemakes $B$ or falsemakes $C$. For $A = B \lor C$, we flip the truth- and falsemakers of $B \land C$. Then, e.g., $p \land q$ is made true by $\{p^+, q^+\}$, false by $\{p^-\}$ and by $\{q^-\}$; $p \lor q$ is made true by $\{p^+\}$ and by $\{q^+\}$; false by $\{p^-, q^-\}$.

Now $p \lor {\sim}p$ and $q \lor {\sim}q$ (“John is either a bachelor or not”, “Either 44 is the sum of two primes or not”) will express distinct thick propositions insofar as they are about different things (how things stand John-wise is a different issue from how things stand 44-wise). When, with distinct $p$ and $q$, the truthmakers of $p \lor {\sim}p$ are $\{p^+\}$ and $\{p^-\}$, those of $q \lor {\sim}q$ are $\{q^+\}$ and $\{q^-\}, s(p \lor {\sim}p)$ will differ from $s(q \lor {\sim}q)$ and so the two thick propositions [$p \lor {\sim}p$] and [$q \lor {\sim}q$] will differ although $|p \lor {\sim}p| = |q \lor {\sim}q| = W$. Also, [$p$] will differ from [$p \land (q \lor {\sim}q)$] as $p$ is truthmade by $\{p^+\}, p \land (q \lor {\sim}q)$ by $\{p^+, q^+\}$ and $\{p^+, q^-\}$, not by $\{p^+\}$. So “You see that Mary is eating an ice cream” and “You see that Mary is eating an ice cream and John is either eating chips or not” don’t say the same, despite the logical equivalence of $A$ and $A \land (B \lor {\sim}B$).

Distinct, logically atomic necessarily true or false contents may be difficult to tell apart. Take “Mike is Mike”, $m = m$, and “Mike is Jack the Ripper”, $m = j$. Given that Mike is Jack and the necessity of identity, $|m = m| = |m = j| = W$; but also the subject matters will coincide: what truthmakes both is a fact about Mike, Mike’s being Mike. Nothing falsemakes either. “Hobbes squared the circle”, $Sh$, and “Daniel Nolan squared the circle”, $Sd$, concern different issues: one is about Hobbes’ mathematical (non)achievements, the other is about Daniel’s. But $|Sh| = |Sd| = \emptyset$, and there’s no way to get truth/falsemakers as sets of possible worlds that will make $s(Sh)$ and $s(Sd)$ differ: no matter how one groups possible worlds into sets, there will be no worlds available where Hobbes squares the circle or where Nolan does to begin with. Fine (2020) imputes this to the setting being conservative: it starts with possible worlds and takes subject matters as ways of splitting and grouping them (see also Gioulatou 2016, Hawke 2018 on this)[^gioulatou-2016][^hawke-2018].

*Two-component* *(2C) semantics*, presented in works such as Berto (2022a), Hawke et al. (2024), has a Yabloesque take on content while allowing more hyperintensional distinctions. A proposition $P$ is represented as an ordered pair $\langle W_P, T_P\rangle$> , where $W_P$ is its usual truth set (a set of possible worlds), $T_P$ is its topic or subject matter. Berto (2022a, ch. 2) and Hawke et al. (2024) argue that truth conditions and topic make for two irreducible components of content. Topics get a more abstract characterization than in the Yablovian setting. 2C semantics is silent on what topics are: it just asks that they make for an algebraic semilattice with a fusion operation lumping topics together. The truth-functional connectives are *topic-transparent*, i.e., they add no subject matter to the sentences where they occur: what “Snow is not white” is about, is just what “Snow is white” is about (say, *the colour of snow*). The topic of “Arif is tall and handsome” is the same as that of “Arif is tall or handsome”: the fusion of the topics of “Arif is tall” and “Arif is handsome” (say, *Arif’s height and looks*). The account tells apart “Hobbes squared the circle” and “Daniel Nolan squared the circle” simply by assigning them different topics. That the abstract setting of 2C is uninformative on when (atomic) sentences *should* get the same topic, rather than different ones, is a criticism in Douven (2025). 2C semantics has been put to work in a number of areas, ranging from hyperintensional logics of knowledge (Hawke et al. 2020; Silva 2024a,b; Rossi and Özgün 2023)[^hawke-2020][^rossi-2023][^silva-2024a], belief (Berto 2019; Özgün and Berto 2021)[^berto-2019][^berto-2019-2][^berto-2021][^özgün-2021], justification (Rossi 2025)[^rossi-2025], imagination (Giordani 2019; Badura 2021; Canavotto et al. 2022; Badura and Wansing 2023; Özgün and Schoonen 2024; Özgün and Cotnoir 2025)[^badura-2021][^badura-2023][^canavotto-2022][^giordani-2019][^özgün-2025], to cognitive synonymy (Berto and Hornischer 2023)[^berto-2023][^berto-2023-2], modal (Ferguson 2023a,b, 2024)[^ferguson-2023a][^ferguson-2024] and probabilistic (Berto and Özgün 2021)[^berto-2021][^özgün-2021] accounts of conditionals, as well as to non-classical logical settings (Tedder 2024; Ciuni 2024; Ferguson and Logan 2025; Vigiani 2025)[^ciuni-2024][^ferguson-2025][^tedder-2024][^vigiani-2025]. Yablovian and 2C semantics have been developed initially at the propositional level, but work to extend them to predicative languages and quantifiers is well underway: see Plebani and Spolaore (2024), Silva (2025), Hawke (2025).

*Exact truthmaker semantics*, championed primarily by Kit Fine (see Fine 2012, 2016, 2017a,b; see also Fine and Jago 2019 and forthcoming; Hornischer 2020; Moltmann 2020, 2021; Krämer 2023b, 2024)[^fine-2012][^fine-2016][^fine-2017a][^fine-2019][^hornischer-2020][^krämer-2023b][^krämer-2024][^moltmann-2020][^moltmann-2021], is possibly the hyperintensional alternative to SPWS enjoying the most momentum. The approach gives truthmakers and falsemakers for sentences in a way that mirrors the Yablo’s recursive route introduced above (and thus van Fraassen’s). But, crucially, rather than using possible worlds and partitions or divisions thereof, it resorts to *states* and fusions thereof to provide the required truth/falsemakers.

Finean states remind us of the situations of Barwise and Perry’s (1983) *situation semantics:* they can be partial, truthmaking neither $A$ nor $ {\sim}A$, for some $A.$ Next, the idea of *exact* truthmaking is that a state should be wholly relevant for the truth/falsity of the sentence it truthmakes/falsemakes: the state consisting of Daniel playing Backgammon and Franz napping is an inexact truthmaker for “Franz is napping” for it exceeds what is needed. Its proper part, Franz napping, is what exactly truthmakes that sentence. Additionally, states can fail to be possible by truthmaking both $A$ and $ {\sim}A$, for some $A$. Impossible states can be constructed via the fusion operation in the semantics: one can fuse incompatibles, e.g., the state of this table being square and that of it being oval. Fine jokes: “[t]he possible worlds approach is fine but for two features: the first is that possible worlds are worlds, i.e. complete rather than partial; and the second is that they are possible” (Fine 2017b: 645)[^fine-2017b]. States act as the same time as the subject matters of sentences and as what makes them true/false.

(Exact) truthmaker semantics is vastly studied and applied: from general linguistic semantics (Moltmann 2020; Champollion 2025; Jago forthcoming)[^champollion-2025][^moltmann-2020] to modal and nonclassical logic (Jago 2020; Saitta et al. 2022; Korbmacher 2023; Knudstorp 2023; Verdée 2023; Champollion and Bernard 2024; Kim 2024)[^champollion-2024][^jago-2020][^kim-2024][^knudstorp-2023][^korbmacher-2023][^saitta-2022][^verdée-2023], to epistemic (Hawke and Özgün 2023; Saitta 2025)[^hawke-2023][^saitta-2025], doxastic (Krämer 2023a; Jago 2024)[^jago-2024][^krämer-2023a] and deontic logic (Anglberger et al. 2016)[^anglberger-2016].

### 4.3 Extended Worlds Semantics

One who starts from a possible worlds framework and comes under pressure to recognize hyperintensional distinctions may respond by adding *non-normal* or *impossible* worlds (Priest 1992; Zalta 1997; Kiourti 2010; Jago 2015; Berto and Jago 2019)[^berto-2019][^berto-2019-2][^jago-2015][^kiourti-2010][^priest-1992][^zalta-1997] taken as ways things could not have been, or worlds where some truth of logic, mathematics, or metaphysics fails. We will be very brief here, as one can consult the entry on impossible worlds. See also the excellent survey by Vacek (2023) as well as Vacek (forthcoming). A recent book-length introduction is Tanaka and Sandgren (2024); see also Sandgren and Tanaka (2020).

In impossible worlds semantics, intuitively distinct necessary truths can correspond to sets containing all possible worlds and distinct impossible ones; intuitively distinct necessary falsehoods can correspond to sets containing no possible world, but distinct impossible ones. Their introduction in modal-epistemic logic is often credited to Rantala (1982), but the idea was floated in Hintikka (1975), and Kripke (1965) had already introduced non-normal worlds for the semantics of modal systems such as C.I. Lewis’ S2 and S3: points where all formulas of the form $\Diamond A$ are true, and all those of the form $\Box A$ are false (everything is possible, nothing is necessary). Cresswell (1970) offered a logic in which beliefs were modelled with sets of both possible and impossible worlds, so as to allow someone to believe some necessary truths, or impossibilities, without believing them all.

Impossible worlds have been used in theories of attitude ascriptions (including first-person ones: Lin 2025)[^lin-2025] and of claims about meaning: see Jago (2014) for a treatment of a number of issues involving mental content and reasoning. Impossible worlds also help in theories of other kinds of representations: for use in theories of impossible fictions, see Priest (1997), Badura and Berto (2019). Mainstream epistemologists are starting to find applications for them in theories of knowledge and belief, see e.g. Melchior (2021), and Garrett and Wrublewski (2022). Logicians use them to model non-omniscient agents by combining impossible worlds semantics with algorithmic and dynamic epistemic logic (Bjerring and Skipper 2019; Solaki et al. 2021; Bozdag 2022; Soysal 2024)[^bjerring-2019][^bozdag-2022][^solaki-2021][^soysal-2024]. Probabilistic-Bayesian approaches are being developed: see Pettigrew (2021); but see Elliot (2019) for some difficulties.

Given the limitations of Lewis-Stalnaker theories of counterfactual conditionals when dealing with impossible antecedents (see §1.1.2), it is natural to extend a theory of counterfactual conditionals with impossible worlds: see Routley (1989), Mares (1997), Nolan (1997), Brogaard and Salerno (2013), and Weiss (2017). Similar theories can be offered of indicative conditionals: see Nolan (2016b).

Impossible worlds have been employed to deal with wordly hyperintensionality. One early application was *de re* necessity, in offering a theory of how it could be necessarily true that an artifact could be made of slightly different material, but not too different, without succumbing to Chisolm’s paradox (Salmon 1984)[^salmon-1984]. Impossible worlds can be used to give a hyperintensional theory of properties as sets of possible and impossible instances (Nolan 2013: 8)[^nolan-2013]. They can be used in theories of metaphysical explanation (Kment 2014)[^kment-2014], essence (Brogaard and Salerno 2013: 646–8)[^brogaard-2013]. They can play a central role in a theory of omissions of impossibilities (Bernstein 2016)[^bernstein-2016].

The literature to date has only scratched the surface of potential applications in metaphysical theorizing. Concerns with the approach, of the kind presented in a general setting in our §2, are discussed in the entry on impossible worlds, section 6, Nolan (2013), Berto and Jago (2019), Garrett and Wrublewski (2025).

We close the section by mentioning the monograph Rosenkranz (2021), which models the hyperintensionality of justification, knowledge, and derivative notions like *being in a position to know*, using non-normal modal logics but without non-normal worlds semantics. Rosenkranz defends an internalist conception of justification against dominant anti-luminosity arguments.

### 4.4 Relevance/Relevant Logic

The entry on relevance logic, also called relevant logic, gives an introduction (see Anderson and Belnap 1975; Anderson et al. 1992; Dunn and Restall 2002)[^anderson-1975][^anderson-1992][^dunn-2002]. So we just briefly discuss connections to hyperintensionality. Standefer (2023) features a precise characterization of the sense in which relevance logic counts as hyperintensional. The origins lay in the aim to develop logical systems free from the paradoxes of the material and strict conditional discussed above. Another early motivation was to construct a conditional that could represent logical deducibility within the language itself.

In this program, an agreed upon necessary (though, in general, not sufficient) condition for a conditional to be logically valid is that there be some connection between antecedent and consequent. This has often been phrased via a *Variable Sharing Property* (VSP): $A \rightarrow B$ is valid only when $A$ and $B$ share some sentential variable or parameter (Anderson and Belnap 1975: 32–3)[^anderson-1975]. VSP delivers hyperintensional distinctions: conditionals with (classically) impossible antecedents and necessary consequents are not all trivially valid or true: the infamous *ex falso quodlibet*, $(A \land \neg A) \rightarrow B$, fails; whereas $(A \land \neg A) \rightarrow A$ holds in most mainstream relevant systems: plausibly, a conjunction relevantly implies its conjuncts.

In the most developed relevant semantics, the frames of Routley and Meyer (1973), hyperintensional distinctions are achieved by featuring points of evaluation different from classical possible worlds, accessible (via a *ternary* accessibility relation, different from the binary accessibility of standard modal logic) in the evaluation of conditionals. Working out the intuitive interpretation of such points and of the ternary relation has been difficult (see e.g. Copeland 1980; Read 1988; Restall 1996b; Mares 2004; Hornischer and Berto 2025)[^copeland-1980][^hornischer-2025][^mares-2004][^read-1988][^restall-1996b]. The consensus on the points nowadays seems to be that they be understood as non-normal or logically impossible worlds (see Priest 2008, ch. 10; Berto & Jago 2019, ch. 6; however, see De 2025, against using impossible worlds in a semantics for relevance logics)[^berto-2019][^berto-2019-2][^priest-2008]. The impossible worlds of Routley-Meyer frames can be seen as situations which can be locally inconsistent (making true both $A$ and $\neg A$, for some $A$) without thereby being trivial (making true everything), and incomplete (making true neither $A$ nor $\neg A$, ditto). Leitgeb (2019) proposes HYPE, a propositional logic to deal with hyperintensional contexts, where formulas are evaluated at situations of this kind, and whose relations to relevance logic are discussed in Odintsov and Wansing (2020). Fischer (2022) presents sequent calculi for HYPE.

The conditional of most mainstream relevant systems is taken as representing implication or necessary entailment, not a *ceteris paribus* or counterfactual conditional. But some of the first theories of counterpossible conditionals, addressing the limitations of the Lewis/Stalnaker account of counterfactuals, were developed against a relevance logic background: see Routley (1989); Mares and Fuhrmann (1995) and Mares (1997).

Other applications of relevance logic to areas where hyperintensional distinctions seem needed include the theory of confirmation in science (Goddard 1977; Sylvan and Nola 1991)[^goddard-1977][^sylvan-1991]; the logic of fiction (Routley 1979)[^routley-1979]; information theory (Mares 2004; Dunn 2015)[^dunn-2015][^mares-2004]; and deontic logic (Anderson 1967; Goble 1999; Tagawa and Cheng 2002)[^anderson-1967][^goble-1999][^tagawa-2002].

Relevance logic has also been deployed to deal with worldly hyperintensionality. In a series of papers, Michael Dunn developed a theory of *relevant predication* intended to illuminate a range of traditional metaphysical distinctions, including the differences between intrinsic and extrinsic properties, essential and accidental properties, and between essential properties and properties necessarily had when an object exists (Dunn 1987, 1990a, 1990b)[^dunn-1987][^dunn-1990a][^dunn-1990b]. As mentioned above, Restall (1996a) employed relevant logic to offer a theory of truthmakers.

To date, many of these proposals have been piece-meal, with less of a general story about how these techniques could be applied to handle hyperintensional language across the board. Some general strategies have been outlined for how a theory could be constructed that handles all hyperintensional phenomena: one program was Richard Routley’s “Ultralogic as Universal”, first set out in Routley (1977). See Nolan (2018) and the essays in Routley (2019) for evaluations. We finally mention here the sophisticated logical work of Sedlár (2021), Pascucci and Sedlár (2023), although it does not fit neatly into any of the approaches singled out in this entry. Rather, they propose a general hyperintensional modal-logical framework, subsuming as special cases state-based and impossible worlds semantics, as well as structuralist views on propositional content we are about to discuss. For an application of the Sedlarian framework to handle logical omniscience, see Caret (2022).

### 4.5 Structured Propositions

After Soames’ (1987) attack against unstructured accounts of propositions as sets of truth-supporting circumstances, structured propositions (King 1995)[^king-1995] have become the main rivals to SPWS views. We will be brief here as well for one can consult the entry on structured propositions. Roughly: propositions are taken as structures, composed of the entities which are the semantic values of the corresponding sentences’ syntactic constituents. (We leave aside the metaphysical issue of what ties the constituents together: see Gaskin 2008.)[^gaskin-2008] Take “Robin loves Batman”. It’s composed of a noun, “Robin”, and a verb phrase, “loves Batman”, itself made of a verb and a noun. Let the semantic values of the lexical items be: [Robin], [Batman], [*loving*]. Then the corresponding proposition can be taken as an ordered triple $\langle$[Robin], [*loving*], [Batman]$\rangle$. Order matters: Batman may not return the feeling, so “Batman loves Robin” expresses a different proposition: $\langle$[Batman], [*loving*], [Robin]$\rangle$.

What makes for the constituents? *Russellian* structured accounts, developed by Salmon (1986), Soames (2008), are typically paired with direct reference or Millian accounts of names: thus, [Batman] is Batman and [Robin] is Robin. The semantic values of predicates and verb phrases can be taken as properties or relations. The logical vocabulary can be interpreted as denoting logical operations, e.g., [${\sim}$] can be the unary function that flips truth and falsity, [$\land$] the binary function that outputs truth only if both inputs are truths, etc.

This delivers hyperintensional distinctions, e.g., “John is either a bachelor or not” and “Either 44 is the sum of two primes or not” will express different propositions: only one will include [John], i.e., John, as a constituent. Necessarily true/false atomic sentences will also be differentiated, even when their syntactic structure is the same (“Hobbes squared the circle” and “Daniel Nolan squared the circle”: [Daniel Nolan] isn’t [Hobbes]; “$3 + 3 = 6$” and “$2 + 2 = 4$”: [3] isn’t [2]).

More challenging cases come from the necessary *a posteriori*. “Mike is Mike” and “Mike is Jack the Ripper” express the same proposition, because [Mike] = [Jack the Ripper]. Same for “All woodchucks are woodchucks”, “All woodchucks are whistlepigs”, as [woodchuck] = [whistlepig]. This will create issues in intentional contexts (Ripley 2012: 9)[^ripley-2012]. Soames (1987) proposes a pragmatic-metalinguistic strategy: one should distinguish attitudes towards sentences and towards propositions. Soames comes up with examples showing that the former can be an unreliable guide to the latter: one can sometimes believe a proposition, but only assent to one of two distinct sentences expressing it. You *do* know that Mike is Jack the Ripper by knowing that Mike is Mike. But you will assent to, or assert, only the sentence that reports your knowledge in the trivial clothing. One should not confuse belief reports with reports of linguistic practices. Ripley (2012) argues that it’s difficult to account for phenomena concerning attitude reports by throwing them in the box of pragmatics: failures of substitutivity *salva veritate* behave in systematic ways in contexts of iterated embeddings, and this calls for a systematic, compositional treatment.

Salmon resorts to a distinction between “semantically encoded” and “pragmatically imparted information” (Salmon 1986: 78)[^salmon-1986] for “Mike is Mike” vs. “Mike is Jack the Ripper” cases. He introduces different representational *guises* under which one can have attitudes to the proposition expressed by different sentences. For direct reference to work, we need [Mike] to be [Jack the Ripper], but we can allow Mike-guises to differ from Jack-the-Ripper-guises, and claim that attitudes are relations to propositions mediated by guises: Lois Lane loves Kal-El under the guise of Superman, not under the guise of Clark Kent. Guises don’t belong in semantics and don’t determine denotations. Salmon’s view can in principle account for compositional phenomena involving embeddings. It has been criticized because of this: Forbes (1987) argues that guises look too much like Fregean senses (to which we come in a second) in disguise. But Branquinho (1990) argues that the correspondence will not reduce Salmon’s account to a relabelled Fregean view.

As argued by Ripley (2012), Jago (2014), there are hyperintensional phenomena involving indicative and counterfactual conditionals structuralism doesn’t seem to handle. As Jago (2014: 76–7) has it, we can be at the 1972 Ziggy Stardust Tour and wonder if Ziggy is David Bowie. We come up with:

**(1)**

If Ziggy isn’t Bowie, then Bowie isn’t Bowie.

**(2)**

If Bowie isn’t Bowie, then Bowie isn’t Bowie.

**(3)**

If Ziggy weren’t Bowie, then Bowie wouldn’t be Bowie.

**(4)**

If Bowie weren’t Bowie, then Bowie wouldn’t be Bowie.

All of (1)–(4) have metaphysically impossible antecedents. (1) and (3) are plausibly false (unless one is a vacuist), but (2) and (4) are trivial truths. The structuralist has it that (1)–(2) and (3)–(4), respectively, express the same propositions, for [Ziggy] = [Bowie]. To the extent that conditionals don’t involve intentional constructions, guises are not supposed to come into play. However, there are treatments of conditionality along the lines of epistemic modals (Kratzer 1986; Lycan 2001; Kocurek 2020)[^kocurek-2020][^kocurek-2020-2][^kratzer-1986][^lycan-2001], and the Russellian structuralist may appeal to one of them, or come up with a new one.

Could a *Fregean* structuralist account do better? Now we don’t take the constituents as denotations, rather as Fregean senses. Much now depends on how these are understood. If they are taken à la Carnap, as functions from possible worlds to extensions, there is little hope to account for “Mike is Mike” vs. “Mike is Jack the Ripper” cases. Now [Mike] and [Jack the Ripper] are functions from possible worlds to individuals; but unless one clashes with the Kripkean criticisms of descriptivism on names (Kripke 1980)[^kripke-1980], they had better be constant functions: given that they both actually pick out Mike, they should output Mike at all possible worlds (at which Mike exists). But then [Mike] and [Jack the Ripper] cannot be told apart.

One may change the set of circumstances, admitting impossible situations where Mike is distinct from Jack the Ripper, and have the two as the outputs of [Mike] and [Jack the Ripper] there, respectively. But then, as remarked by Ripley (2012) and Jago (2014) again, it is not structuralism that does the job, rather the fact that we are not working only with standard possible worlds.

An interesting proposal to improve on the Fregean situation comes from Hawke (2018), combining a theory of subject matter with a structuralist account of propositions resorting to Fregean-senses-lookalikes. Subject matter sensitivity allows Hawke to make hyperintensional distinction unavailable to standard Fregean structuralism.

One logically sophisticated, neo-Fregean structuralist account, offering a systematic analysis of a range of hyperintensional phenomena, is the *Transparent Intensional Logic* (TIL) approach. Pioneered by Tichý (1968, 1971, 1988), this treats the meanings of expressions as given by structural procedures, called *constructions*, built out of entities that are somewhat like Fregean senses. In particular, different expressions, even if they necessarily co-designate, may be associated with different senses to the extent that they can be mapped to different constructions, which are themselves individuated hyperintensionally. This gives TIL resources to handle many hyperintensional contexts straightforwardly. In particular, TIL manages to give a powerful compositional account where other approaches have to resort to pragmatics. The approach is less popular than it should be in contemporary semantics, possibly due its resorting to a technical apparatus of typed lambda-calculus equipped with partial functions, as well as operations of functional abstraction and application. For hyperintensional applications and a comprehensive discussion of TIL, see Duží et al. (2010), Duží and Jespersen (2015).

We mention one final proposal in the Fregean camp by Schellenberg (2012), further defended and developed by Skipper and Bjerring (2020). This pivots on another Fregean notion, namely that of *cognitive equipollence*: $A$ and $B$ are cognitively equipollent when one cannot rationally regard either as true and the other as false. This gives a cognitive or epistemic notion of sentential meaning which, the authors claim, is more fine-grained than SPWS intensions, but less than extra-fine-grained impossible worlds semantics.

### 4.6 Algebraic and Object Theory Approaches

Algebraic approaches to semantics typically do not try to give an account of meaning in terms of anything else at all. They treat meanings as primitive and focus on the relationships between them. By defining in a direct way how the meanings of different parts of language go together to yield sentence meanings, these approaches are not under pressure to identify the meanings of sentences true in all the same possible circumstances, or even sentences which are logically equivalent. So an algebraic approach can make room for hyperintensional differences between parts of language. Even if sentence meanings are necessarily equivalent, if they relate differently to a “believes that” operator they do not have to be substitutable in “John believes that $A$” contexts. Bealer (1979) touts this flexibility as an advantage in dealing with puzzles like the semantics of belief attributions, as does Menzel (1993).

Some algebraic approaches do not take much advantage of this flexibility with respect to hyperintensionality puzzles. Keenan and Faltz (1984)’s algebraic approach identifies necessary equivalents. Bacon (2018) adopts a Boolean account in which the propositions associated with logical equivalents are identified with each other (e.g., the proposition that ${\sim}({\sim}A \lor {\sim}B)$ is identical to the proposition that $(A \land B))$. This leaves room for distinguishing merely necessarily equivalent propositions, e.g., that $2+2=4$ and that it rains if and only if it rains. But it does little to help when we want to discriminate between logical equivalents, e.g., if we think that $A$ explains why ${\sim}{\sim}A$ but not vice versa, or we want to capture the belief content of the confused man who believes $(A \land B)$ but does not believe ${\sim}({\sim}A \lor {\sim}B)$. So it is not the algebraic approach *per se* that yields solutions to particular puzzles about hyperintensionality, but the algebraic approach combined with choices about the structure of the algebra.

Algebraic approaches are largely silent on the question of what meanings are, and how they relate. (Or, if every structure of relations between meanings can be found somewhere in Platonic heaven, how we come to be associated with our particular structure rather than others.) Theories which say more about the nature of meanings (e.g., that they are set-theoretic constructions from worlds, or structures of objects and properties) *also* face the challenge of explaining how our concrete practices explain which structures of meanings are associated with our speech and writing. So it may be that these concerns are general, and algebraic semantics can employ the same kinds of answers as their rivals.

A close relative of algebraic theories is the object theory of Zalta (1988). It also supplies distinct fine-grained meanings to, e.g., be the suitably distinct inputs so that “John believes all triangles have internal angles that add up to 180°” and “John believes all trilaterals have internal angles that add up to 180°” express different propositions. Zalta says a little more about the identity conditions of his hyperintensionally-distinguished properties: according to Zalta, properties are identical if and only if they are *encoded* by the same objects.

There is nothing in the general motivations of algebraic theories that would rule out the hypothesis that we need hyperintensional language to best capture the non-representational aspects of reality, but nor does there appear to be anything in the general motivations that would indicate why we would, or how that might manifest in our language. This is not necessarily an objection to algebraic approaches. One might think that a theory of meaning *should* be silent on substantive questions about what the world is like. We do not want it to tell us which physics or chemical theory to adopt. Likewise, it might be good for a theory of meaning to be neutral about how to understand essences, or intrinsicness of properties, or causation. Of course, a theory of meaning may not be able to be completely neutral about metaphysical questions—it should have something to say about what meanings are, whether there are abstract representations, and so on—but perhaps algebraic theories not taking a stand on worldly hyperintensionality is an attractive feature rather than a drawback.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=hyperintensionality). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/hyperintensionality/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=hyperintensionality&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/hyperintensionality/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

[Please contact the authors with suggestions.]

## Related Entries

*a priori* justification and knowledge | belief | conditionals: counterfactual | confirmation | dispositions | grounding, metaphysical | impossible worlds | indexicals | information | intentionality | intrinsic vs. extrinsic properties | logic: epistemic | logic: justification | logic: relevance | names | natural kinds | possible worlds | properties | propositional attitude reports | propositions | propositions: structured | reasons for action: justification, motivation, explanation | semantics: two-dimensional | truthmakers | Wittgenstein, Ludwig

### Acknowledgments

Versions of this entry have been presented at the Arché Metaphysics and Logic research seminar at the University of St Andrews, at the Logic of Conceivability seminar at the University of Amsterdam, and at the 2020 Hamburg Summer School at the Institute of Philosophy of the University of Hamburg. We are grateful to the participants, as well as Sara Bernstein, Max Cresswell, Mark Jago, Greg Restall and two referees of the *Stanford Encyclopedia of Philosophy*, for their valuable feedback. Franz Berto’s research for this entry has been funded by the European Research Council (ERC CoG), Grant 681404 and by the Leverhulme Trust, Grant RPG-2023-236.

[^anderson-1967]: Anderson, Alan Ross, 1967, “Some Nasty Problems in the Formal Logic of Ethics”, *Noûs*, 1(4): 345–360. doi:10.2307/2214623

[^anderson-1975]: Anderson, Alan Ross and Nuel D. Belnap, Jr., 1975, *Entailment: The Logic of Relevance and Necessity*, Volume I, Princeton, NJ: Princeton University Press.

[^anderson-1992]: Anderson, Alan Ross, Nuel D. Belnap, and J. Michael Dunn, 1992, *Entailment: The Logic of Relevance and Necessity*, Volume II, Princeton, NJ: Princeton University Press.

[^anglberger-2016]: Anglberger, Albert J.J. and Johannes Korbmacher and Federico Faroldi, 2016, “An Exact Truthmaker Semantics for Permission and Obligation”, in Oliver Roy et al. (eds), *Deontic Logic and Normative Systems,*13th International Conference, DEON, London: College Publications, pp. 16–31.

[^azzano-2024]: Azzano, Lorenzo, 2024, “Dispositionalism as Hyperintensional Metaphysics”, *Philosophia,* 52(4):1209–1231. doi:10.1007/s11406-024-00788-4

[^bacon-2018]: Bacon, Andrew, 2018, “The Broadest Necessity”, *Journal of Philosophical Logic*, 47(5): 733–783. doi:10.1007/s10992-017-9447-9

[^bacon-2019]: –––, 2019, “Substitution Structures”, *Journal of Philosophical Logic*, 48(6): 1017–1075. doi:10.1007/s10992-019-09505-z

[^bader-2013]: Bader, Ralf M., 2013, “Towards a Hyperintensional Theory of Intrinsicality”, *Journal of Philosophy*, 110(10): 525–563. doi:10.5840/jphil2013110109

[^badura-2021]: Badura, Christopher, 2021, “More Aboutness in Imagination”, *Journal of Philosophical Logic,* 50: 523–547. doi:10.1007/s10992-020-09575-4

[^badura-2019]: Badura, Christopher and Francesco Berto, 2019, “Truth in Fiction, Impossible Worlds, and Belief Revision”, *Australasian Journal of Philosophy*, 97(1): 178–193. doi:10.1080/00048402.2018.1435698

[^badura-2023]: Badura, Christopher and Heinrich Wansing, 2023, “STIT-Logic for Imagination Episodes With Voluntary Input”, *Review of Symbolic Logic,* 16: 813–861. doi:10.1017/S1755020321000514

[^barcan-1947]: Barcan [Marcus], Ruth C., 1947, “The Identity of Individuals in a Strict Functional Calculus of Second Order”, *Journal of Symbolic Logic*, 12(1): 12–15. doi:10.2307/2267171

[^bar-hillel-1952]: Bar-Hillel, Yehoshua and Rudolf Carnap, 1952 [1964], “An Outline of a Theory of Semantic Information”, Technical Report 247, The Research Laboratory of Electronics, Massachusetts Institute of Technology. Reprinted in Yehoshua Bar-Hillel’s *Language and Information: Selected Essays on Their Theory and Application*, Reading, MA: Addison-Wesley, 1964, pp. 221–274.

[^baron-2017]: Baron, Sam, Mark Colyvan, and Ellie Ripley, 2017, “How Mathematics Can Make a Difference”, *Philosophers’ Imprint*, 17(3): 1–19

[^baron-2020]: –––, 2020, “A Counterfactual Approach to Explanation in Mathematics”, *Philosophia Mathematica*, 28(1): 1–34. doi:10.1093/philmat/nkz023

[^barwise-1997]: Barwise, Jon, 1997, “Information and Impossibilities”, *Notre Dame Journal of Formal Logic*, 38(4): 488–515. doi:10.1305/ndjfl/1039540766

[^barwise-1983]: Barwise, Jon and John Perry, 1983, *Situations and Attitudes*, Cambridge, MA: The MIT Press.

[^barwise-1997-2]: Barwise, Jon and Jerry Seligman, 1997, *Information Flow: The Logic of Distributed Systems*, Cambridge: Cambridge University Press. doi:10.1017/CBO9780511895968

[^bealer-1979]: Bealer, George, 1979, “Theories of Properties, Relations, and Propositions”, *The Journal of Philosophy*, 76(11): 634–648. doi:10.2307/2025697

[^bernstein-2016]: Bernstein, Sara, 2016, “Omission Impossible”, *Philosophical Studies*, 173(10): 2575–2589. doi:10.1007/s11098-016-0672-9

[^berto-2019]: Berto, Francesco, 2019, “Simple Hyperintensional Belief Revision”, *Erkenntnis*, 84(3): 559–575. doi:10.1007/s10670-018-9971-1

[^berto-2022a]: –––, 2022a, *Topics of Thought. The Logic of Knowledge, Belief, Imagination*, Oxford: Oxford University Press. doi:10.1093/oso/9780192857491.001.0001

[^berto-2022b]: –––, 2022b, “Williamson on Indicatives and Suppositional Heuristics”, *Synthese*, 200(8). doi:10.1007/s11229-022-03518-z

[^berto-2025a]: –––, 2025a, “Saying the Same Thing”, *Erkenntnis*, online first. doi:10.1007/s10670-025-01023-6

[^berto-2025b]: –––, 2025b, “The Ramsey Test for Counterfactuals Is a Consistent Heuristic”, *Ergo,* forthcoming. Online at: https://philpapers.org/rec/BERTRT-10

[^berto-2018]: Berto, Francesco, Rohan French, Graham Priest, and Ellie Ripley, 2018, “Williamson on Counterpossibles”, *Journal of Philosophical Logic*, 47(4): 693–713. doi:10.1007/s10992-017-9446-x

[^berto-2023]: Berto, Francesco and Levin Hornischer, 2023, “Cognitive Synonymy: a Dead Parrot?”, *Philosophical Studies*, 180: 2727–2752. doi:10.1007/s11098-023-02007-4

[^berto-2019-2]: Berto, Francesco and Mark Jago, 2019, *Impossible Worlds*, Oxford: Oxford University Press. doi:10.1093/oso/9780198812791.001.0001

[^berto-2021]: Berto, Francesco and Aybüke Özgün, 2021, “Indicative Conditionals: Probabilities and Relevance”, *Philosophical Studies*, 178: 3697–3730. doi:10.1007/s11098-021-01622-3

[^berto-2023-2]: –––, 2023, “The Logic of Framing Effects”, *Journal of Philosophical Logic*, 52: 939–962. doi:10.1007/s10992-022-09694-0

[^bjerring-2014]: Bjerring, Jens Christian, 2014, “On Counterpossibles”, *Philosophical Studies*, 168(2): 327–353. doi:10.1007/s11098-013-0133-7

[^bjerring-2017]: Bjerring, Jens Christian and Wolfgang Schwarz, 2017, “Granularity Problems”, *The Philosophical Quarterly*, 67(266): 22–37. doi:10.1093/pq/pqw028

[^bjerring-2019]: Bjerring, Jens Christian and Mattias Skipper, 2019, “A Dynamic Solution to the Problem of Logical Omniscience”, *Journal of Philosophical Logic*, 48(3): 501–521. doi:10.1007/s10992-018-9473-2

[^bjerring-2023]: Bjerring, Jens Christian and Weng Hong Tang, 2023, “Fragmentation, Metalinguistic Ignorance, and Logical Omniscience”, *Philosophical Studies*, 180(7): 2129–2151. doi:10.1007/s11098-023-01962-2

[^bourne-2016]: Bourne, Craig and Emily Caddick Bourne, 2016, *Time in Fiction*, Oxford: Oxford University Press.

[^bourne-2018]: –––, 2018, “Personification Without Impossible Content”, *British Journal of Aesthetics,* 58(2): 165–179. doi:10.1093/aesthj/ayy008

[^bozdag-2022]: Bozdag, Sena, 2022, “A Semantics for Hyperintensional Belief Revision Based on Information Bases”, *Studia Logica*, 110: 679–716. doi:10.1007/s11225-021-09973-y

[^branquinho-1990]: Branquinho, Joāo, 1990, “Are Salmon’s ‘Guises’ Disguised Fregean Senses?”, *Analysis*, 50(1): 19–24. doi:10.1093/analys/50.1.19

[^brogaard-2013]: Brogaard, Berit and Joe Salerno, 2013, “Remarks on Counterpossibles”, *Synthese*, 190(4): 639–660. doi:10.1007/s11229-012-0196-6

[^byrne-2024]: Byrne, Ruth, 2024, “How People Think About the Truth of Hypothetical Impossibilities”, *Memory and Cognition,* 52: 182–196. doi:10.3758/s13421-023-01454-y

[^canavotto-2022]: Canavotto, Ilaria, Francesco Berto and Alessandro Giordani, 2022, “Voluntary Imagination: a Fine-Grained Analysis”, *Review of Symbolic Logic*, 15: 362–387. doi:10.1017/S1755020320000039

[^caret-2022]: Caret, Colin, 2022, “Simple Semantics for Logics of Indeterminate Epistemic Closure”, in Igor Sedlár (ed.), *The Logica Yearbook 2021,* London: College Publications, pp. 37–56.

[^chalmers-1996]: Chalmers, David, 1996, *The Conscious Mind: In Search of a Fundamental Theory*, Oxford: Oxford University Press.

[^champollion-2025]: Champollion, Lucas, 2025, “Truthmaker Semantics and Natural Language Semantics”, *Language and Linguistics Compass*, 19: 1–13. doi:10.1111/lnc3.70004

[^champollion-2024]: Champollion, Lucas and Timothée Bernard, 2024, “Negation and Modality in Unilateral Truthmaker Semantics”, *Linguistics and Philosophy*, 47: 517–555. doi:10.1007/s10988-023-09407-z

[^ciardelli-2013]: Ciardelli, Ivano, Jeroen Groenendijk, and Floris Roelofsen, 2013, “Inquisitive Semantics: A New Notion of Meaning”, *Language and Linguistics Compass*, 7(9): 459–476. doi:10.1111/lnc3.12037

[^ciuni-2024]: Ciuni, Roberto, 2024, “Weak Kleene Logic and Topic-Sensitive Logics”, *Logic and Logical Philosophy*, 33: 523–554. doi:10.12775/LLP.2024.018

[^correia-2020]: Correia, Fabrice, 2020, “Granularity”, in Michael J. Raven (ed.), *The Routledge Handbook of Metaphysical Grounding,* New York: Routledge, pp. 228–243.

[^copeland-1980]: Copeland, B. J., 1980, “The Trouble Anderson and Belnap Have with Relevance”, *Philosophical Studies*, 37(4): 325–334. doi:10.1007/BF00354901

[^cresswell-1970]: Cresswell, M. J., 1970, “Classical Intensional Logics”, *Theoria*, 36(3): 347–372. doi:10.1111/j.1755-2567.1970.tb00433.x

[^cresswell-1975]: –––, 1975, “Hyperintensional Logic”, *Studia Logica*, 34(1): 25–38. doi:10.1007/BF02314421

[^cresswell-2002]: –––, 2002, “Why Propositions Have No Structure”, *Noûs*, 36(4): 643–662. doi:10.1111/1468-0068.00405

[^davidson-1968]: Davidson, Donald, 1968, “On Saying That”, *Synthese*, 19(1–2): 130–146. doi:10.1007/BF00568054

[^davies-1980]: Davies, Martin and Lloyd Humberstone, 1980, “Two Notions of Necessity”, *Philosophical Studies*, 38(1): 1–30. doi:10.1007/BF00354523

[^de-2025]: De, Michael, 2025, “Relevance Logic Without Impossibilities”, *Inquiry*, Online First 23 January 2025. doi:10.1080/0020174X.2024.2448480

[^deutsch-1985]: Deutsch, Harry, 1985, “Fiction and Fabrication”, *Philosophical Studies*, 47(2): 201–211. doi:10.1007/bf00354147

[^dohrn-2024]: Dohrn, Daniel, 2024, “The Counterpossibles of Science Versus the Science of Counterpossibles”, *The British Journal for the Philosophy of Science*, 75(4): 947–970. doi:10.1086/716769

[^douven-2025]: Douven, Igor, 2025, “Review of *Topics of Thought*”, *Mind*, 134: 524–532. doi:10.1093/mind/fzad051

[^dretske-1981]: Dretske, Fred, 1981, “The Pragmatic Dimension of Knowledge”, *Philosophical Studies*, 40(3): 363–378. doi:10.1007/BF00646423

[^duncan-2017]: Duncan, Michael, Kristie Miller, and James Norton, 2017, “Is Grounding a Hyperintensional Phenomenon?”, *Analytic Philosophy*, 58(4): 297–329. doi:10.1111/phib.12105

[^dunn-1987]: Dunn, J. Michael, 1987, “Relevant Predication 1: The Formal Theory”, *Journal of Philosophical Logic*, 16(4): 347–381. doi:10.1007/BF00431183

[^dunn-1990a]: –––, 1990a, “Relevant Predication 2: Intrinsic Properties and Internal Relations”, *Philosophical Studies*, 60(3): 177–206. doi:10.1007/BF00367469

[^dunn-1990b]: –––, 1990b, “Relevant Predication 3: Essential Properties”, in *Truth or Consequences: Essays in Honor of Nuel Belnap*, J. Michael Dunn and Anil Gupta (eds.), Dordrecht: Kluwer, pp. 77–95. doi:10.1007/978-94-009-0681-5_6

[^dunn-2015]: –––, 2015, “The Relevance of Relevance to Relevance Logic”, in *Logic and Its Applications*, Mohua Banerjee and Shankara Narayanan Krishna (eds.), (Lecture Notes in Computer Science, 8923), Berlin, Heidelberg: Springer Berlin Heidelberg, pp. 11–29. doi:10.1007/978-3-662-45824-2_2

[^dunn-2002]: Dunn, J. Michael and Greg Restall, 2002, “Relevance Logic”, in *Handbook of Philosophical Logic*, Dov M. Gabbay and F. Guenthner (eds.), second edition, Dordrecht: Springer Netherlands, Volume 6, pp. 1–128. doi:10.1007/978-94-017-0460-1_1

[^duží-2010]: Duží, Marie, Bjørn Jespersen, and Pavel Materna, 2010, *Procedural Semantics for Hyperintensional Logic: Foundations and Applications of Transparent Intensional Logic*, (Logic, Epistemology, and the Unity of Science 17), Dordrecht: Springer Netherlands. doi:10.1007/978-90-481-8812-3

[^duží-2015]: Duží, Marie and Bjørn Jespersen, 2015, “Transparent Quantification into Hyperintensional Objectual Attitudes”, *Synthese*, 192(3): 635–677. doi:10.1007/s11229-014-0578-z

[^eddon-2011]: Eddon, Maya, 2011, “Intrinsicality and Hyperintensionality”, *Philosophy and Phenomenological Research*, 82(2): 314–336. doi:10.1111/j.1933-1592.2010.00414.x

[^elliott-2019]: Elliott, Edward, 2019, “Impossible Worlds and Partial Beliefs”, *Synthese*, 196(8): 3433–3458. doi:10.1007/s11229-017-1604-8

[^elohim-2018]: Elohim, David, 2018, “Grounding, Conceivability and the Mind-Body Problem”, *Synthese*, 1195: 919–926. doi:10.1007/s11229-016-1254-2

[^fagin-1995]: Fagin, Ronald, Joseph Y. Halpern, Yoram Moses and Moshe Vardi, 1995, *Reasoning About Knowledge*, Cambridge, MA: MIT Press.

[^faroldi-2019]: Faroldi, Federico L. G., 2019, *Hyperintensionality and Normativity*, Cham: Springer International Publishing. doi:10.1007/978-3-030-03487-0

[^ferguson-2023a]: Ferguson, Thomas M., 2023a, “Subject-Matter and Intensional Operators I: Conditional-Agnostic Analytic Implication”, *Philosophical Studies*, 180: 849–1879. doi:10.1007/s11098-023-01952-4

[^ferguson-2023b]: –––, 2023b, “Subject-Matter and Intensional Operators II: Applications to the Theory of Topic-Sensitive Intentional Modals”, *Journal of Philosophical Logic*, 52: 1673–1701. doi:10.1017/S1755020323000230

[^ferguson-2024]: –––, 2024, “Subject-Matter and Intensional Operators III: State-Sensitive Subject Matter and Topic-Sufficiency”, *Review of Symbolic Logic*, 17:1070–1096. doi:10.1007/s10992-023-09722-7

[^ferguson-2025]: Ferguson, Thomas M. and Shay Allen Logan, 2025, “Topic Transparency and Variable Sharing in Weak Relevant Logics”, *Erkenntnis*, 90: 1227–1254. doi:10.1007/s10670-023-00748-6

[^fine-1994]: Fine, Kit, 1994, “Essence and Modality: The Second Philosophical Perspectives Lecture”, *Philosophical Perspectives*, 8: 1–16. doi:10.2307/2214160

[^fine-2001]: –––, 2001, “The Question of Realism”, *Philosopher’s Imprint*, 1(June): art. 2. [[Fine 2001 available online](http://hdl.handle.net/2027/spo.3521354.0001.002)]

[^fine-2012]: –––, 2012, “Counterfactuals Without Possible Worlds”, *Journal of Philosophy*, 109(3): 221–246. doi:10.5840/jphil201210938

[^fine-2016]: –––, 2016, “Angellic Content”, *Journal of Philosophical Logic*, 45(2): 199–226. doi:10.1007/s10992-015-9371-9

[^fine-2017a]: –––, 2017a, “Truthmaker Semantics”, in *A Companion to the Philosophy of Language* (Vol. 2), Bob Hale et al. (eds.), 2nd ed., Chichester, UK: Wiley Blackwell, pp. 556–577. doi:10.1002/9781118972090.ch22

[^fine-2017b]: –––, 2017b, “A Theory of Truthmaker Content I: Conjunction, Disjunction and Negation”, *Journal of Philosophical Logic*, 46: 625–674. doi:10.1007/s10992-016-9413-y

[^fine-2020]: –––, 2020, “Yablo on Subject-Matter”, *Philosophical Studies*, 177(1): 129–171. doi:10.1007/s11098-018-1183-7

[^fine-2019]: Fine, Kit and Mark Jago, 2019, “Logic for Exact Entailment”, *Review of Symbolic Logic*, 12(3): 536–556. doi:10.1017/s1755020318000151

[^fine-nd]: –––, forthcoming, *An Introduction to Truthmaker Semantics*, Oxford: Oxford University Press.

[^fischer-2022]: Fischer, Martin, 2022, “Sequent Calculi for the Propositional Logic of HYPE”, *Studia logica*, 110(3): 643–677. doi:0.1007/s11225-021-09971-0

[^forbes-1987]: Forbes, Graeme, 1987, “Review of *Frege’s Puzzle*, by Nathan Salmon”, *The Philosophical Review*, 96(3): 455–458. doi:10.2307/2185233

[^garcía-carpintero-2006]: García-Carpintero, Manuel and Josep Maciá (eds), 2006, *Two-Dimensional Semantics*. Oxford: Oxford University Press.

[^garrett-2022]: Garrett, Zack and Zacharian Wrublewski, 2022, “Impossible Worlds and the Safety of Philosophical Beliefs”, *Metaphilosophy*, 53(2–3): 344–361. doi:10.1111/meta.12550

[^garrett-2025]: –––, 2025, “Beyond Impossibility”, *Acta Analytica*, Online First 23 June 2025. doi:10.1007/s12136-025-00648-0

[^gaskin-2008]: Gaskin, Richard, 2008, *The Unity of the Proposition*, Oxford: Oxford University Press. doi:10.1093/acprof:oso/9780199239450.001.0001

[^giordani-2019]: Giordani, Alessandro, 2019, “Axomatizing the Logic of Imagination”, *Studia logica,* 107: 639–657. doi:10.1007/s11225-018-9810-z

[^gioulatou-2016]: Gioulatou, Iliana, 2016, *Hyperintensionality*, Master of Science in Logic thesis, Institute for Logic, Language and Computation (ILLC), Universiteit van Amsterdam. [[Gioulatou 2016 available online](https://eprints.illc.uva.nl/1523/)]

[^goble-1999]: Goble, Lou, 1999, “Deontic Logic with Relevance”, in P. McNamara and H. Prakken (eds.), *Norms, Logics and Information Systems: New Studies on Deontic Logic and Computer Science*, Amsterdam: IOS Press, pp. 331–345.

[^goddard-1977]: Goddard, Len, 1977, “The Paradoxes of Confirmation and the Nature of Natural Laws”, *The Philosophical Quarterly*, 27(107): 97–113. doi:10.2307/2219421

[^güngör-2023]: Güngör, Hüseyin, 2023, “Counterfactuals, Hyperintensionality and Hurford Disjunctions”, *Linguistics and Philosophy,* 46(1): 169–195. doi:10.1007/s10988-022-09360-3

[^hanley-2004]: Hanley, Richard, 2004, “As Good As It Gets: Lewis on Truth In Fiction”, *Australasian Journal of Philosophy*, 82(1): 112–128. doi:10.1080/713659790

[^hawke-2018]: Hawke, Peter, 2018, “Theories of Aboutness”, *Australasian Journal of Philosophy*, 96(4): 697–723. doi:10.1080/00048402.2017.1388826

[^hawke-2025]: –––, 2025, “Aboutness and Universal Generalization”, *Philosophy and Phenomenological Research*, 111: 325–342. doi:10.1111/phpr.70017

[^hawke-2024]: Hawke, Peter, Levin Hornischer and Francesco Berto, 2024, “Truth, Topicality and Transparency: One-Component vs Two-Component Semantics”, *Linguistics and Philosophy*, 47: 481–503. doi:10.1007/s10988-023-09408-y

[^hawke-2023]: Hawke, Peter and Aybüke Özgün, 2023, “Truthmaker Semantics for Epistemic Logic”, in Federico Faroldi and Frederik Van De Putte (eds.), *Kit Fine on Truthmakers, Relevance, and Non-classical Logic*, Dordrecht: Springer, pp. 295–335. doi:10.1007/978-3-031-29415-0_15

[^hawke-2020]: Hawke, Peter, Aybüke Özgün and Francesco Berto, 2020, “The Fundamental Problem of Logical Omniscience”, *Journal of Philosophical Logic*, 49: 727–766. doi:10.1007/s10992-019-09536-6

[^hintikka-1962]: Hintikka, Jaakko, 1962, *Knowledge and Belief*, Ithaca, NY: Cornell University Press.

[^hintikka-1975]: –––, 1975, “Impossible Possible Worlds Vindicated”, *Journal of Philosophical Logic*, 4(4): 475–484. doi:10.1007/BF00558761

[^hoffmann-kolss-2015]: Hoffmann-Kolss, Vera, 2015, “On a Sufficient Condition for Hyperintensionality”, *The Philosophical Quarterly*, 65(260): 336–354. doi:10.1093/pq/pqv021

[^hoffmann-kolss-2019]: –––, 2019, “Defining Qualitative Properties”, *Erkenntnis*, 84(5): 995–1010. doi:10.1007/s10670-018-9991-x

[^hornischer-2017]: Hornischer, Levin, 2017, *Hyperintensionality and Synonymy*, M.S. in Logic Thesis, Institute for Logic, Language and Computation (ILLC), Universiteit van Amsterdam. [[Hornischer 2017 available online](https://eprints.illc.uva.nl/1543/)]

[^hornischer-2020]: –––, 2020, “Logics of Synonymy”, *Journal of Philosophical Logic*, 49: 767–805. doi:10.1007/s10992-019-09537-5

[^hornischer-2025]: Hornischer, Levin and Francesco Berto, 2025, “The Logic of Dynamical Systems is Relevant”, *Mind*, 134: 670–706. doi:10.1093/mind/fzaf012

[^jackson-1994]: Jackson, Frank, 1994, “Armchair Metaphysics”, in *Philosophy in Mind: The Place of Philosophy in the Study of Mind*, Michaelis Michael and John O’Leary-Hawthorne (eds.), (Philosophical Studies Series 60), Dordrecht: Kluwer, pp. 23–42. doi:10.1007/978-94-011-1008-2_3

[^jago-2009]: Jago, Mark, 2009, “Logical Information and Epistemic Space”, *Synthese*, 167(2): 327–341. doi:10.1007/s11229-008-9411-x

[^jago-2014]: –––, 2014, *The Impossible: An Essay on Hyperintensionality*, Oxford: Oxford University Press. doi:10.1093/acprof:oso/9780198709008.001.0001

[^jago-2015]: –––, 2015, “Impossible Worlds”, *Noûs*, 49(4): 713–728. doi:10.1111/nous.12051

[^jago-2020]: –––, 2020, “Truthmaker Semantics for Relevant Logic”, *Journal of Philosophical Logic*, 49: 681–702. doi:10.1007/s10992-019-09533-9

[^jago-2024]: –––, 2024, “Belief in Truthmaker Semantics”, *Synthese*, 204(123). doi:10.1007/s11229-024-04748-z

[^jago-nd]: –––, forthcoming, “Truthmaker Semantics in Linguistics”, in Hilary Nesi and Petar Milin (eds.), *International Encyclopedia of Language and Linguistics*, forthcoming. [[Jago forthcoming available online](https://philpapers.org/archive/JAGTSI.pdf)]

[^jenkins-2011]: Jenkins, C.S., 2011, “Is Metaphysical Dependence Irreflexive?”, *Monist*, 94(2): 267–276. doi:10.5840/monist201194213

[^jenkins-2012]: Jenkins, C.S. and Daniel Nolan, 2012, “Disposition Impossible”, *Noûs*, 46(4): 732–753. doi:10.1111/j.1468-0068.2011.00831.x

[^jenny-2018]: Jenny, Matthias, 2018, “Counterpossibles in Science: The Case of Relative Computability”, *Noûs* 52(3): 530–560. doi:10.1111/nous.12177

[^jespersen-2010]: Jespersen, Bjørn, 2010, “How Hyper Are Hyperpropositions?”, *Language and Linguistics Compass*, 4(2): 96–106. doi:10.1111/j.1749-818X.2009.00181.x

[^jespersen-2024]: –––, 2024, “Lexical Predicates Do Substitute in Fine-Grained Attitudes”, *Synthese*, 205(1): 1–30. doi:10.1007/s11229-024-04810-w

[^jespersen-2015]: Jespersen, Bjørn and Marie Duží, 2015, “Introduction”, Special issue on Hyperintensionality, *Synthese*, 192(3): 525–534. doi:10.1007/s11229-015-0665-9

[^kahneman-2011]: Kahneman, Daniel, 2011, *Thinking, Fast and Slow*, New York: Farrar, Straus and Giroux.

[^kaplan-1989]: Kaplan, David, 1989, “Demonstratives”, in *Themes from Kaplan.*, Joseph Almog, John Perry, and Howard Wettstein (eds.), New York: Oxford University Press, pp. 481–563.

[^keenan-1984]: Keenan, Edward L. and Leonard M. Faltz, 1984, *Boolean Semantics for Natural Language*, (Synthese Language Library 23), Dordrecht: Springer Netherlands. doi:10.1007/978-94-009-6404-4

[^kim-2024]: Kim, Dongwoo, 2024, “Exact Truthmaker Semantics for Modal Logics”, *Journal of Philosophical Logic*, 53: 789–829. doi:10.1007/s10992-024-09752-9

[^kim-2025]: Kim, Hannah, 2025, “Imagination and the Permissive View of Fictional Truth”, *Australasian Journal of Philosophy,* 103(4): 1039–1060. doi:10.1080/00048402.2025.2497043

[^king-1995]: King, Jeffrey C., 1995, “Structured Propositions and Complex Predicates”, *Noûs*, 29(4): 516–535. doi:10.2307/2216285

[^kiourti-2010]: Kiourti, Ira George, 2010, *Real Impossible Worlds: The Bounds of Possibility*, Ph.D. Dissertation, University of St Andrews. [[Kiourti 2010 available online](http://hdl.handle.net/10023/924)]

[^kment-2014]: Kment, Boris, 2014, *Modality and Explanatory Reasoning*, Oxford: Oxford University Press. doi:10.1093/acprof:oso/9780199604685.001.0001

[^knudstorp-2023]: Knudstorp, Søren Brinck, 2023, “Logics of Truthmaker Semantics: Comparison, Compactness and Decidability”, *Synthese*, 202(206). doi:10.1007/s11229-023-04401-1

[^kocurek-2020]: Kocurek, Alexander W., 2020, “On the Substitution of Identicals in Counterfactual Reasoning”, *Noûs*, 54: 600–631. doi:10.1111/nous.12273

[^kocurek-2021]: –––, 2021, “Counterpossibles”, *Philosophy Compass*, e12787. doi:10.1111/phc3.12787

[^kocurek-2021-2]: Kocurek, Alexander W. and Ethan Jerzak, 2021, “Counterlogicals as Counterconventionals”, *Journal of Philosophical Logic,* 50(4): 673–704. doi:10.1007/s10992-020-09581-6

[^kocurek-2020-2]: Kocurek, Alexander W., Ethan Jerzak, and Rachel Etta Rudolph, 2020, “Against Conventional Wisdom”, *Philosopher’s Imprint*, 20: art. 22. [[Kocurek et al. 2020 available online](http://hdl.handle.net/2027/spo.3521354.0020.022)]

[^kosterec-2023]: Kosterec, Miloš, 2023, “A Hyperintensional Theory of (Empty) Names”, *Erkenntnis*, 88(2): 511–529. doi:10.1007/s10670-020-00364-8

[^korbmacher-2023]: Korbmacher, Johannes, 2023, “Proof Systems for Exact Entailment”, *Review of Symbolic Logic,* 16(4): 1260–1295. doi:10.1017/s175502032200020x

[^krämer-2023a]: Krämer, Stephan, 2023a, “Mighty Belief Revision”, *Journal of Philosophical Logic*, 51: 1175–1213. doi:10.1007/s10992-022-09663-7

[^krämer-2023b]: –––, 2023b, “The Whole Truth”, in Federico Faroldi and Frederik Van De Putte (eds.), *Kit Fine on Truthmakers, Relevance, and Non-classical Logic*, Dordrecht: Springer, pp. 521–550. doi:10.1007/978-3-031-29415-0_23

[^krämer-2024]: –––, 2024, “That’s It! Hyperintensional Total Logic”, *Journal of Philosophical Logic*, 52(4): 963–1004. doi:10.1007/s10992-022-09695-z

[^kratzer-1986]: Kratzer, Angelika, 1986, “Conditionals”, in *Papers from the Parasessions on Pragmatics and Grammatical Theory*, Anne M. Farley, Peter Farley and Karl-Erik McCollough (eds.), Chicago: Chicago Linguistics Society, pp. 115–135.

[^kripke-1965]: Kripke, Saul A., 1965, “Semantical Analysis of Modal Logic II: Non-normal Modal Propositional Calculi”, in J. W. Addison, Leon Henkin, and Alfred Tarski (eds.), 1965, *The Theory of Models*, Amsterdam: North-Holland, pp. 206–20.

[^kripke-1980]: –––, 1980, *Naming and Necessity*, Oxford: Blackwell.

[^krzyżanowska-2023]: Krzyżanowska, Karolina and Igor Douven, 2023, “Williamson on Conditionals and Testimony”, *Philosophical Studies*, 180: 121–131. doi:10.1007/s11098-022-01874-7

[^leitgeb-2019]: Leitgeb, Hannes, 2019, “HYPE: A System of Hyperintensional Logic (with an Application to Semantic Paradoxes)”, *Journal of Philosophical Logic*, 48(2): 305–405. doi:10.1007/s10992-018-9467-0

[^lenta-2023]: Lenta, Giorgio, 2023, “Sources of Hyperintensionality”, *Theoria,* 89(6): 811–822. doi:10.1111/theo.12497

[^lewis-1973]: Lewis, David, 1973, *Counterfactuals*, Oxford: Blackwell.

[^lewis-1982]: –––, 1982, “Logic for Equivocators”, *Noûs*, 16(3): 431–441. doi:10.2307/2216219

[^lewis-1976]: –––, 1976, “Probabilities of conditionals and conditional probabilities”, *Philosophical Review*, 95: 581–9. doi:10.2307/2184045

[^lewis-1986]: –––, 1986, *On the Plurality of Worlds*, Oxford: Blackwell.

[^lewis-1988]: –––, 1988, “Statements Partly about Observation”, *Philosophical Papers*, 17(1): 1–31. doi:10.1080/05568648809506282

[^lewis-2004]: –––, 2004, “Letters to Beall and Priest”, in *The Law of Non-Contradiction: New Philosophical Essays*, Graham Priest, J.C. Beall, and Bradley Armour-Garb (eds.), Oxford: Oxford University Press, pp. 176–177. doi:10.1093/acprof:oso/9780199265176.003.0011

[^lin-2025]: Lin, Lixiao, 2025, “First Person and Impossible Worlds”, *Synthese*, 205(146). doi:10.1007/s11229-025-04947-2

[^locke-2021]: Locke, Theodore D., 2021, “Counterpossibles for Modal Normativists”, *Synthese*, 198: 1235–1257. doi:10.1007/s11229-019-02103-1

[^lycan-2001]: Lycan, William G., 2001, *Real Conditionals*, Oxford: Oxford University Press.

[^macbride-2012]: MacBride, Fraser, 2012 [2020], “Truthmakers”, *The Stanford Encyclopedia of Philosophy* (Spring 2020 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/spr2020/entries/truthmakers/](https://plato.stanford.edu/archives/spr2020/entries/truthmakers/)>.

[^mcloone-2021]: McLoone, Brian, 2021, “Calculus and Counterpossibles in Science”, *Synthese*, 198(12):12153–12174. doi:10.1007/s11229-020-02855-1

[^mcloone-2023]: McLoone, Brian, Cassandra Grützner and Michael T. Stuart, 2023, “Counterpossibles in Science: an Experimental Study”, *Synthese*, 201(27): 1–20. doi:10.1007/s11229-022-04014-0

[^mares-1997]: Mares, Edwin D., 1997, “Who’s Afraid of Impossible Worlds?”, *Notre Dame Journal of Formal Logic*, 38(4): 516–526. doi:10.1305/ndjfl/1039540767

[^mares-2004]: –––, 2004, *Relevant Logic: A Philosophical Interpretation*, Cambridge: Cambridge University Press. doi:10.1017/CBO9780511520006

[^mares-1995]: Mares, Edwin D. and André Fuhrmann, 1995, “A Relevant Theory of Conditionals”, *Journal of Philosophical Logic*, 24(6): 645–665. doi:10.1007/BF01306969

[^marshall-2015]: Marshall, Dan, 2015, “Intrinsicality and Grounding”, *Philosophy and Phenomenological Research*, 90(1): 1–19. doi:10.1111/phpr.12053

[^melchior-2021]: Melchior, Guido, 2021, “Sensitivity, Safety, and Impossible Worlds”, *Philosophical Studies*, 178(3): 713–729. doi:10.1007/s11098-020-01453-8

[^menzel-1993]: Menzel, Christopher, 1993, “The Proper Treatment of Predication in Fine-Grained Intensional Logic”, *Philosophical Perspectives*, 7: 61–87. doi:10.2307/2214116

[^miller-2024]: Miller, James, 2024, “Hyperintensionality and Ontological Categories”, *Erkenntnis*, 89: 2663–2681. doi:10.1007/s10670-022-00646-3

[^miller-2017]: Miller, Kristie, 2017, “A Hyperintensional Account of Metaphysical Equivalence”, *The Philosophical Quarterly*, 67: 772–793. doi:10.1093/pq/pqx015

[^moltmann-2020]: Moltmann, Friederike, 2020, “Truthmaker Semantics for Natural Language: Attitude Verbs, Modals, and Intensional Transitive Verbs”, *Theoretical Linguistics*, 46(3–4): 159–200.

[^moltmann-2021]: –––, 2021, “Situations, Alternatives, and the Semantics of ‘Cases’”, *Linguistics and Philosophy*, 44: 153–193. doi:10.1007/s10988-019-09282-7

[^montague-1970]: Montague, Richard, 1970, “Universal Grammar”, *Theoria*, 36(3): 373–398. doi:10.1111/j.1755-2567.1970.tb00434.x

[^nolan-1997]: Nolan, Daniel, 1997, “Impossible Worlds: A Modest Approach”, *Notre Dame Journal of Formal Logic*, 38(4): 535–572. doi:10.1305/ndjfl/1039540769

[^nolan-2003]: –––, 2003, “Defending a Possible-Worlds Account of Indicative Conditionals”, *Philosophical Studies*, 116(3): 215–269. doi:10.1023/B:PHIL.0000007243.60727.d4

[^nolan-2013]: –––, 2013, “Impossible Worlds”, *Philosophy Compass*, 8(4): 360–372. doi:10.1111/phc3.12027

[^nolan-2014]: –––, 2014, “Hyperintensional Metaphysics”, *Philosophical Studies*, 171(1): 149–160. doi:10.1007/s11098-013-0251-2

[^nolan-2016a]: –––, 2016a, “Chance and Necessity”, *Philosophical Perspectives*, 30(1): 294–308. doi:10.1111/phpe.12076

[^nolan-2016b]: –––, 2016b, “Conditionals and Curry”, *Philosophical Studies*, 173(10): 2629–2647. doi:10.1007/s11098-016-0666-7

[^nolan-2018]: –––, 2018, “Reflections on Routley’s Ultralogic Program”, *The Australasian Journal of Logic*, 15(2): 407–430. doi:10.26686/ajl.v15i2.4866

[^nolan-2021a]: –––, 2021a, “Impossible Fictions Part I: Lessons for Fiction”, *Philosophy Compass,*16.2: 1–12. doi: 10.1111/phc3.12723

[^nolan-2021b]: –––, 2021b, “Impossible Fictions Part II: Lessons for Mind, Language and Epistemology”, *Philosophy Compass,* 16.2: 1–16. doi:10.1111/phc3.12725

[^odintsov-2020]: Odintsov, Sergei and Heinrich Wansing, 2020, “Routley Star and Hyperintensionality”, *Journal of Philosophical Logic*, 50(1): 33-56. doi:10.1007/s10992-020-09558-5

[^osorio-kupferblum-2016]: Osorio-Kupferblum, Naomi, 2016, “Aboutness”, *Analysis*, 76(4): 528–546. doi:10.1093/analys/anw027

[^osorio-kupferblum-2024]: –––, 2024, “Goodman’s ‘About’: the Ryle Factor”, *Journal for the History of Analytical Philosophy*, 12(5): 1–27. doi:10.15173/jhap.v12i5.5463

[^özgün-2021]: Özgün, Aybüke and Francesco Berto, 2021, “Dynamic Hyperintensional Belief Revision”, *Review of Symbolic Logic*, 14: 766–811. doi:10.1017/S1755020319000686

[^özgün-2025]: Özgün, Aybüke and Aaron Cotnoir, 2025, “Imagination, Mereotopology and Topic Expansion”, *Review of Symbolic Logic,* 18: 28–51. doi:10.1017/S1755020324000236

[^özgun-2024]: Özgun, Aybüke and Tom Schoonen, 2024, “The Logical Development of Pretense Imagination”, *Erkenntnis*, 89: 2121–2147. doi: 10.1007/s10670-021-00476-9

[^pettigrew-2021]: Pettigrew, Richard, 2021, “Logical Ignorance and Logical Learning”, *Synthese*, 198: 9991–10020. doi:10.1007/s11229-020-02699-9

[^plebani-2020]: Plebani, Matteo, 2020, “Why Aboutness Matters: Meta-Fictionalism as a Case Study”, *Philosophia*, 49(3): 1177-1186. doi:10.1007/s11406-020-00272-9

[^plebani-2021]: Plebani, Matteo and Giuseppe Spolaore, 2021, “Subject Matter: A Modest Proposal”, *The Philosophical Quarterly*, 71: 605–622. doi:10.1093/pq/pqaa054

[^plebani-2024]: –––, 2024, “Predicative Subject Matter”, *Philosophical Studies,* 181: 247–265. doi:10.1007/s11098-023-02081-8

[^poggiolesi-2018]: Poggiolesi, Francesca, 2018, “On Constructing a Logic for the Notion of Complete and Immediate Formal Grounding”, *Synthese*, 195(3): 1231–1254. doi:10.1007/s11229-016-1265-z

[^poggiolesi-2020]: –––, 2020, “Grounding Rules and (Hyper-)Isomorphic Formulas”, *The Australasian Journal of Logic*, 17(1): 70–80. doi:10.26686/ajl.v17i1.5694

[^priest-1992]: Priest, Graham, 1992, “What is a Non-Normal World?”, *Logique et Analyse*, 35: 291–302.

[^priest-1997]: –––, 1997, “Sylvan’s Box: A Short Story and Ten Morals”, *Notre Dame Journal of Formal Logic*, 38(4): 573–582. doi:10.1305/ndjfl/1039540770

[^priest-2008]: –––, 2008, *An Introduction to Non-Classical Logic: From If to Is*, second edition, Cambridge: Cambridge University Press. First edition 2001. doi:10.1017/CBO9780511801174

[^proudfoot-2018]: Proudfoot, Diane, 2018, “Sylvan’s Bottle and Other Problems”, *Australasian Journal of Logic*, 15(2), 95–122. doi:10.26686/ajl.v15i2.4858

[^quine-1953]: Quine, W. V. O., 1953, “Three Grades of Modal Involvement”, in *Proceedings of the XIth International Congress of Philosophy*, Amsterdam: North-Holland, 14:65–81. Reprinted in Quine 1966: 156–174. doi:10.5840/wcp11195314450

[^quine-1956]: –––, 1956, “Quantifiers and Propositional Attitudes”, *The Journal of Philosophy*, 53(5): 177–187. Reprinted in Quine 1966: 183–194. doi:10.2307/2022451

[^quine-1966]: –––, 1966, *The Ways of Paradox*, New York: Random House.

[^ramsey-1990]: Ramsey, Frank P., 1990, “General Propositions and Causality”, in D.H. Mellor (ed.), *Philosophical Papers,* Cambridge: Cambridge University Press, pp.145–63.

[^rantala-1982]: Rantala, Veikko., 1982, “Impossible Worlds Semantics and Logical Omniscience”, in *Intensional Logic: Theory and Application* (*Acta Philosophica Fennica*, 35), Ilkka Niiniluoto and Esa Saarinen (eds), Helsinki: Societas Philosophica Fennica, pp. 106–115.

[^read-1988]: Read, Stephen, 1988, *Relevant Logic: A Philosophical Examination of Inference*, Oxford: Blackwell.

[^restall-1996a]: Restall, Greg, 1996a, “Truthmakers, Entailment and Necessity”, *Australasian Journal of Philosophy*, 74(2): 331–340. doi:10.1080/00048409612347331

[^restall-1996b]: –––, 1996b, “Information Flow and Relevant Logics”, in Jerry Seligman and Dag Westerståhl (eds.), *Logic, Language and Computation* (Volume 1), Stanford, CA: CSLI Publications, pp. 463–78.

[^ripley-2012]: Ripley, Ellie, 2012, “Structures and Circumstances: Two Ways to Fine-Grain Propositions”, *Synthese*, 189(1): 97–118. doi:10.1007/s11229-012-0100-4

[^rosenkranz-2021]: Rosenkranz, Sven, 2021, *Justification as Ignorance: An Essay in Epistemology*, Oxford: Oxford University Press. doi:10.1093/oso/9780198865636.001.0001

[^rossi-2025]: Rossi, Niccolò, 2025, “Hyperintensional Epistemic Justification: a Ground-Theoretic Topic-Sensitive Semantics”, *Synthese*, 205(127). doi: 10.1007/s11229-024-04789-4

[^rossi-2023]: Rossi, Niccolò and Aybüke Özgün, 2023, “A Hyperintensional Approach to Positive Epistemic Possibility”, *Synthese*, 202(44). doi:10.1007/s11229-023-04219-x

[^rothschild-2021]: Rothschild, Daniel, 2021, “Living in a Material World: A Critical Notice of *Suppose and Tell: The Semantics and Heuristics of Conditionals* by Timothy Williamson”, *Mind*, 132: 208–233. doi:10.1093/mind/fzab049

[^routley-1977]: Routley, Richard, 1977, “Ultralogic as Universal?” *The Relevance Logic Newsletter*, 2(1): 50–90 and 2(2): 138–175. Reprinted in Routley 2019: 1–121. doi:10.1007/978-3-319-91974-4_1

[^routley-1979]: –––, 1979, “The Semantical Structure of Fictional Discourse”, *Poetics*, 8(1–2): 3–30. doi:10.1016/0304-422X(79)90013-5

[^routley-1989]: –––, 1989, “Philosophical and Linguistic Inroads: Multiply Intensional Relevant Logics”, in *Directions in Relevant Logic*, Jean Norman and Richard Sylvan (eds.), Dordrecht: Kluwer, pp. 269–304. doi:10.1007/978-94-009-1005-8_19

[^routley-2019]: –––, 2019, *Ultralogic as Universal? The Sylvan Jungle—Volume 4*, Zach Weber (ed.), (Synthese Library 396), Cham: Springer International Publishing. doi:10.1007/978-3-319-91974-4

[^routley-1973]: Routley, Richard and Robert K. Meyer, 1973, “The Semantics of Entailment I”, in Hugues Leblanc (ed.), *Truth, Syntax and Semantics*, Amsterdam: North-Holland, pp. 194–243.

[^saitta-2025]: Saitta, Vita, 2025, “Developing the Total Knowledge Account in Truthmaker Semantics: a Bilateral Approach”, *Synthese,* 205(171). doi:10.1007/s11229-025-04978-9

[^saitta-2022]: Saitta, Vita, Matteo Plebani and Giuliano Rosella, 2022, “Truthmakers, Incompatibility, and Modality”, *Australasian Journal of Logic*, 19(5): 214–253. doi:10.26686/ajl.v19i5.7420

[^salerno-2022]: Salerno, Joseph, 2022, “Suppositional Attitudes and the Reliability of Heuristics for Assessing Conditionals”, *Thought,* 11(3): 175–183. doi:10.5840/tht202421524

[^salmon-1984]: Salmon [Salmón], Nathan, 1984, “Impossible Worlds”, *Analysis*, 44(3): 114–117. doi:10.1093/analys/44.3.114

[^salmon-1986]: –––, 1986, *Frege’s Puzzle*, Cambridge, MA: MIT Press.

[^salmon-2019]: –––, 2019, “Impossible Odds”, *Philosophy and Phenomenological Research*, 99(3): 644–662. doi:10.1111/phpr.12517

[^sandgren-2020]: Sandgren, Alexander and Koji Tanaka, 2020, “Two Kinds of Logical Impossibility”, *Noûs*, 54(4): 795–806. doi:10.1111/nous.12281

[^schaffer-2009]: Schaffer, Jonathan, 2009, “On What Grounds What”, in David Manley, David J. Chalmers and Ryan Wasserman (eds.), *Metametaphysics: New Essays on the Foundations of Ontology*, Oxford: Oxford University Press, pp. 347–383.

[^schellenberg-2012]: Schellenberg, Susanna, 2012, “Sameness of Fregean Sense”, *Synthese*, 189(1): 163–175. doi:10.1007/s11229-012-0098-7

[^schneider-2011]: Schneider, Benjamin, 2011, “A Logic for ‘Because’”, *The Review of Symbolic Logic*, 4(3): 445–465. doi:10.1017/S1755020311000104

[^sedlár-2023]: Sedlár, Igor, 2023, “Hyperintensional Logics for Everyone”, *Synthese*, 198: 933–956. doi:10.1007/s11229-018-02076-7

[^sedlár-2023-2]: Sedlár, Igor and Matteo Pascucci, 2023, “Hyperintensional Models for Non-Congruential Modal Logics”, *Logic Journal of the IGPL,* doi:10.1093/jigpal/jzad018

[^segerberg-1973]: Segerberg, Krister, 1973, “Two-Dimensional Modal Logic”, *Journal of Philosophical Logic*, 2(1): 77–96. doi:10.1007/BF02115610

[^sendłak-2021]: Sendłak, Maciej, 2021, “Counterpossibles, Story Prefix and Trivialism”, *Synthese*, 199: 7283–7301 doi:10.1007/s11229-021-03114-7

[^sendłak-2024]: –––, 2024, *Wondering about the Impossible: On the Semantics of Counterpossibles*, Dordrecht: Springer. doi:10.1007/978-3-031-65361-2

[^silva-2024a]: Silva, Francisca, 2024a, “Epistemic Logic with Partial Grasp”, *Synthese*, 204(92). doi:10.1007/s11229-024-04738-1

[^silva-2024b]: –––, 2024b, “Question-Relative Knowledge for Minimally Rational Agents”, *Inquiry*, Online First 10 April 2024. doi:10.1080/0020174X.2024.2338794

[^silva-2025]: –––, 2025, “First-Order Aboutness Theory”, *Erkenntnis*, forthcoming: https://philpapers.org/archive/SILFAT-6.pdf

[^skipper-2020]: Skipper, Mattias and Jens Christian Bjerring, 2020, “Hyperintensional Semantics: A Fregean Approach”, *Synthese*, 197(8): 3535–3558. doi:10.1007/s11229-018-01900-4

[^snodgrass-2024]: Snodgrass, J.J., 2024, “Multiplying Co-Intensional Properties. A reply to Streumer”, *Inquiry*, Online First 22 January 2024. doi:10.1080/0020174X.2024.2305392

[^snodgrass-2025]: –––, 2025, “Co-Intensional Properties and Running Afoul of Ockham’s Razor”, *Synthese*, Online First 9 August 2025. doi:10.1007/s11229-025-05153-w

[^soames-1987]: Soames, Scott, 1987, “Direct Reference, Propositional Attitudes, and Semantic Content”, *Philosophical Topics*, 15(1): 47–87.

[^soames-2008]: –––, 2008, “Why Propositions Cannot Be Sets of Truth-Supporting Circumstances”, *Journal of Philosophical Logic*, 37(3): 267–276. doi:10.1007/s10992-007-9069-8

[^solaki-2021]: Solaki, Anthia, Francesco Berto and Sonja Smets, 2021, “The Logic of Fast and Slow Thinking”, *Erkenntnis*, 86(3): 733–762. doi:10.1007/s10670-019-00128-z

[^soysal-2024]: Soysal, Zeynep, 2024, “An Algorithmic Impossible-World Model of Belief and Knowledge”, *Review of Symbolic Logic*, 17 (2):586-610. doi:10.1017/s1755020323000059

[^stalnaker-1968]: Stalnaker, Robert C., 1968, “A Theory of Conditionals”, in Nicholas Rescher (ed.), *Studies in Logical Theory*, Oxford: Blackwell, pp. 98–112.

[^stalnaker-1976]: –––, 1976, “Propositions”, in Alfred M. MacKay and Daniel D. Merrill (eds), *Issues in the Philosophy of Language*, New Haven, CT: Yale University Press, pp. 79–91.

[^stalnaker-1978]: –––, 1978, “Assertion”, in *Pragmatics* (*Syntax and Semantics* 9), Peter Cole (ed.), New York: Academic Press, pp. 315–332.

[^stalnaker-1984]: –––, 1984, *Inquiry*, Cambridge, MA: MIT Press.

[^stalnaker-1996]: –––, 1996, “Impossibilities”, *Philosophical Topics*, 24(1): 193–204. Reprinted with additional material in his, 2003, *Ways a World Might Be: Metaphysical and Anti-Metaphysical Essays*, Oxford: Oxford University Press, pp. 55–68. doi:10.5840/philtopics199624115

[^stalnaker-2004]: –––, 2004, “Assertion Revisited: On the Interpretation of Two-Dimensional Modal Semantics”, *Philosophical Studies*, 118(1/2): 299–322. doi:10.1023/B:PHIL.0000019550.81145.34

[^standefer-2023]: Standefer, Shawn, 2023, “Hyperintensionality in Relevant Logics”, in Natasha Alechina et al. (eds.), *Logic, Rationality, and Interaction: 9th International Workshop, LORI 2023,* Cham: Springer Nature, pp. 238–250. doi:10.1007/978-3-031-45558-2_18

[^stanojevic-2009]: Stanojevic, Maja, 2009, “Cognitive Synonymy: A General Overview”, *Facta Universitatis—Linguistics and Literature*, 7: 193–200.

[^sylvan-1991]: Sylvan, Richard and R. Nola, 1991, “Confirmation Without Paradoxes” in Gerhard Schurz and Georg J. W. Dorn (eds.), *Advances in Scientific Philosophy*, Leiden: Brill, pp. 5–44.

[^tagawa-2002]: Tagawa, Takahiro and Jingde Cheng, 2002, “Deontic Relevant Logic: A Strong Relevant Logic Approach to Removing Paradoxes from Deontic Logic”, in *PRICAI 2002: Trends in Artificial Intelligence*, Mitsuru Ishizuka and Abdul Sattar (eds.), (Lecture Notes in Computer Science 2417), Berlin, Heidelberg: Springer Berlin Heidelberg, pp. 39–48. doi:10.1007/3-540-45683-X_7

[^tan-2019]: Tan, Peter, 2019, “Counterpossible Non-Vacuity in Scientific Practice”, *Journal of Philosophy*, 116(1): 32–60. doi:10.5840/jphil201911612

[^tanaka-2024]: Tanaka, Koji and Alexander Sandgren, 2024, *The Many Faces of Impossibility*, Cambridge: Cambridge University Press. doi:10.1017/9781009180573

[^tedder-2024]: Tedder, Andrew, 2024, “Topics in Relevant Logic: A Semantic Perspective”, *Erkenntnis,* Online First 19 October 2024. doi:10.1007/s10670-024-00865-w

[^tichý-1968]: Tichý, Pavel, 1968, “Smysl a procedura”, *Filosofický Casopis*, 16: 222–232, translated as “Sense and procedure” in Vladimír Svoboda et al. (eds.), 2004, *Pavel Tichý’s Collected Papers in Logic and Philosophy*, Dunedin, New Zealand: University of Otago Press, pp. 77–92.

[^tichý-1971]: –––, 1971, “An Approach to Intensional Analysis”, *Noûs*, 5(3): 273–297. doi:10.2307/2214668

[^tichý-1988]: –––, 1988, *The Foundations of Frege’s Logic*, Berlin, Boston: De Gruyter. doi:10.1515/9783110849264

[^thaler-2008]: Thaler, Richard H. and Cass R. Sunstein, 2008, *Nudge: Improving Decisions about Health, Wealth, and Happiness*, New Haven, CT: Yale University Press.

[^thompson-2016]: Thompson, Naomi, 2016, “Grounding and Metaphysical Explanation”, *Proceedings of the Aristotelian Society*, 116(3): 395–402. doi:10.1093/arisoc/aow012

[^thompson-2019]: Thompson, Naomi and Darragh Byrne, 2019, “On Hyperintensional Metaphysics”, in Tobias Hansson Wahlberg and Robin Stenwall (eds.) *Maurinian Truths: Essays in Honour of Anna-Sofia Maurin on her 50th Birthday*, Lund: Lund University, pp. 151–158.

[^tversky-1981]: Tversky, Amos and Daniel Kahneman, 1981, “The Framing of Decisions and the Psychology of Choice”, *Science*, 211(4481): 453–458. doi:10.1126/science.7455683

[^van-1969]: Van Fraassen, Bas C., 1969, “Facts and Tautological Entailments”, *Journal of Philosophy*, 66(15): 477–487. doi:10.2307/2024563

[^van-1977]: –––, 1977, “The Only Necessity Is Verbal Necessity”, *The Journal of Philosophy*, 74(2): 71–85. doi:10.2307/2025572

[^vacek-2025]: Vacek, Daniela and Martin Vacek, 2025, “The Hyperintensionality of Art”, *Synthese*, 205(2): 1–16. doi:10.1007/s11229-024-04909-0

[^vacek-2023]: Vacek, Martin, 2023, “Impossible Worlds”, *Internet Encyclopedia of Philosophy,* https://iep.utm.edu/impossible-worlds/.

[^vacek-nd]: –––, forthcoming, “Worlds, Possible and Impossible”, in Hilary Nesi and Petar Milin (eds.), *International Encyclopedia of Language and Linguistics*, forthcoming. [[Vacek forthcoming available online](https://philpapers.org/archive/VACWPA.pdf)]

[^rooij-2023]: van Rooij, Robert, Karolina Krzyżanowska and Igor Douven, 2023, “Williamson’s Abductive Case for the Material Conditional Account”, *Studia Logica*, 111: 653–685. doi:10.1007/s11225-023-10038-5

[^verdée-2023]: Verdée, Peter, 2023, “Truthmakers and Relevance for FDE, LP, K3, and CL”, in Federico Faroldi and Frederik Van De Putte (eds.), *Kit Fine on Truthmakers, Relevance, and Non-classical Logic*, Dordrecht: Springer, pp. 231–279. doi:10.1007/978-3-031-29415-0_13

[^vigiani-2025]: Vigiani, Pietro, 2025, “Relevant Epistemic Logic with State-Sensitive Topics”, *Synthese*, Online First 9 January 2025. doi:10.1007/s11229-024-04863-x

[^wansing-2017]: Wansing, Heinrich, 2017, “Remarks on the Logic of Imagination. A Step towards Understanding Doxastic Control through Imagination”, *Synthese*, 194(8): 2843–2861. doi:10.1007/s11229-015-0945-4

[^weatherson-2001]: Weatherson, Brian, 2001, “Indicative and Subjunctive Conditionals”, *The Philosophical Quarterly*, 51(203): 200–216. doi:10.1111/j.0031-8094.2001.00224.x

[^weiss-2017]: Weiss, Yale, 2017, “Semantics for Counterpossibles”, *Australasian Journal of Logic*, 14(4): 383–407. doi:10.26686/ajl.v14i4.4050

[^williamson-2007]: Williamson, Timothy, 2007, *The Philosophy of Philosophy*, Oxford: Blackwell. doi:10.1002/9780470696675

[^williamson-2020]: –––, 2020, *Suppose and Tell: The Semantics and Heuristics of Conditionals*, Oxford: Oxford University Press.

[^williamson-2021]: –––, 2021, “Degrees of Freedom: Is Good Philosophy Bad Science?”, *Disputatio,* 13: 73–91.

[^williamson-2024]: –––, 2024, *Overfitting and Heuristics in philosophy,* Oxford: Oxford University Press.

[^wittgenstein-1921]: Wittgenstein, Ludwig, 1921, *Tractatus Logico-Philosophicus*, London: Routledge & Kegan Paul.

[^xhignesse-2016]: Xhignesse, Michael, 2016, “The Trouble With Poetic License”, *British Journal of Aesthetics* 56.2: 149–161. doi:10.1093/aesthj/ayv053

[^xhignesse-2021]: –––, 2021, “Imagining Fictional Contradictions”, *Synthese*, 199: 3169–3188. doi:10.1007/s11229-020-02929-0

[^yablo-2014]: Yablo, Stephen, 2014, *Aboutness*, Princeton, NJ: Princeton University Press.

[^yablo-2017]: –––, 2017, “Open Knowledge and Changing the Subject”, *Philosophical Studies*, 174(4): 1047–1071. doi:10.1007/s11098-016-0724-1

[^zalta-1988]: Zalta, Edward N., 1988, *Intensional Logic and the Metaphysics of Intentionality*, Cambridge, MA: MIT Press.

[^zalta-1997]: –––, 1997, “A Classically-Based Theory of Impossible Worlds”, *Notre Dame Journal of Formal Logic*, 38(4): 640–660. doi:10.1305/ndjfl/1039540774
