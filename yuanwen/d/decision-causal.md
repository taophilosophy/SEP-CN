# Causal Decision Theory
**First published Sat Oct 25, 2008; substantive revision Thu Oct 24, 2024**

*Weirich, Paul*

Causal decision theory adopts principles of rational choice that attend to an act’s consequences. It maintains that an account of rational choice must use causality to identify the considerations that make a choice rational.

Given a set of options constituting a decision problem, decision theory recommends an option that maximizes utility, that is, an option whose utility equals or exceeds the utility of every other option. It evaluates an option’s utility by calculating the option’s expected utility. It uses probabilities and utilities of an option’s possible outcomes to define an option’s expected utility. The probabilities depend on the option. Causal decision theory takes the dependence to be causal rather than merely evidential.

This essay explains causal decision theory, reviews its history, describes current research in causal decision theory, and surveys the theory’s philosophical foundations. The literature on causal decision theory is vast, and this essay covers only a portion of it.

## 1. Expected Utility

Suppose that a student is considering whether to study for an exam. He reasons that if he will pass the exam, then studying is wasted effort. Also, if he will not pass the exam, then studying is wasted effort. He concludes that because whatever will happen, studying is wasted effort, it is better not to study. This reasoning errs because studying raises the probability of passing the exam. Deliberations should take account of an act’s influence on the probability of its possible outcomes.

An act’s expected utility is a probability-weighted average of its possible outcomes’ utilities. Possible states of the world that are mutually exclusive and jointly exhaustive, and so form a partition, generate an act’s possible outcomes. An act-state pair specifies an outcome. In the example, the act of studying and the state of passing form an outcome comprising the effort of studying and the benefit of passing. The expected utility of studying is the probability of passing if one studies times the utility of studying and passing plus the probability of not passing if one studies times the utility of studying and not passing. In compact notation,

$$ \textit{EU} (S) = P(P \mbox{ if } S) \util (S \amp P) + P({\sim}P \mbox{ if } S) \util (S \amp{\sim}P). $$

Each product specifies the probability and utility of a possible outcome. The sum is a probability-weighted average of the possible outcomes’ utilities.

How should decision theory interpret the probability of a state $S$ if one performs an act $A$, that is, $P(S \mbox{ if }A)$? Probability theory offers a handy suggestion. It has an account of conditional probabilities that decision theory may adopt. Decision theory may take $P(S \mbox{ if }A)$ as the probability of the state conditional on the act. Then $P(S \mbox{ if }A)$ equals $P(S\mid A)$, which probability theory defines as $P(S \amp A)/P(A)$ when $P(A) \ne 0$. Some theorists call expected utility computed using conditional probabilities conditional expected utility. I call it expected utility *tout court* because the formula using conditional probabilities generalizes a simpler formula for expected utility that uses nonconditional probabilities of states. Also, some theorists call an act’s expected utility its utility *tout court* because an act’s expected utility appraises the act and yields the act’s utility in ideal cases. I call it expected utility because a person by mistake may attach more or less utility to a bet than its expected utility warrants. The equality of an act’s utility and its expected utility is normative rather than definitional.

Expected utilities obtained from conditional probabilities steer the student’s deliberations in the right direction.

$$\textit{EU} (S) = P(P\mid S)\util (S \amp P) + P({\sim}P\mid S)\util (S \amp{\sim}P), $$

and

$$\textit{EU} ({\sim}S) = P(P\mid {\sim}S)\util ({\sim}S \amp P) + P({\sim}P\mid {\sim}S)\util ({\sim}S \amp{\sim}P). $$

Because of studying’s effect on the probability of passing, $P(P\mid S) \gt P(P\mid {\sim}S)$ and $P({\sim}P\mid S) \lt P({\sim}P\mid {\sim}S)$. So $\textit{EU} (S) \gt \textit{EU} ({\sim}S)$, assuming that studying’s increase in the probability of passing compensates for the effort of studying. Maximization of expected utility recommends studying.

The handy interpretation of the probability of a state if one performs an act, however, is not completely satisfactory. Suppose that one tosses a coin with an unknown bias and obtains heads. This result is evidence that the next toss will yield heads, although it does not causally influence the next toss’s result. An event’s probability conditional on another event indicates the evidence that the second event provides for the first. If the two events are correlated, the second may provide evidence for the first without causally influencing it. Causation entails correlation, but correlation does not entail causation. Deliberations should attend to an act’s causal influence on a state rather than an act’s evidence for a state. A good decision aims to produce a good outcome rather than evidence of a good outcome. It aims for the good and not just signs of the good. Often efficacy and auspiciousness go hand in hand. When they come apart, an agent should perform an efficacious act rather than an auspicious act.

Consider the Prisoner’s Dilemma, a stock example of game theory. Two people isolated from each other may each act either cooperatively or uncooperatively. They each do better if they each act cooperatively than if they each act uncooperatively. However, each does better if he acts uncooperatively, no matter what the other does. Acting uncooperatively dominates acting cooperatively. Suppose, in addition, that the two players are psychological twins. Each thinks as the other thinks. Moreover, they know this fact about themselves. Then if one player acts cooperatively, he concludes that his counterpart also acts cooperatively. His acting cooperatively is good evidence that his counterpart does the same. Nonetheless, his acting cooperatively does not cause his counterpart to act cooperatively. He has no contact with his counterpart. Because he is better off not acting cooperatively whatever his counterpart does, not acting cooperatively is the better course. Acting cooperatively is auspicious but not efficacious.

To make expected utility track efficacy rather than auspiciousness, causal decision theory interprets the probability of a state if one performs an act as a type of causal probability rather than as a standard conditional probability. In the Prisoner’s Dilemma with twins, consider the probability of one player’s acting cooperatively given that the other player does. This conditional probability is high. Next, consider the causal probability of one player’s acting cooperatively if the other player does. Because the players are isolated, this probability equals the probability of the first player’s acting cooperatively. It is low if that player follows dominance. Using conditional probabilities, the expected utility of acting cooperatively exceeds the expected utility of acting uncooperatively. However, using causal probabilities, the expected utility of acting uncooperatively exceeds the expected utility of acting cooperatively. Switching from conditional to causal probabilities makes expected-utility maximization yield acting uncooperatively.

Michael Titelbaum (2022) introduces the conceptual apparatus of causal decision theory, including subjective probability taken as degree of belief or credence, and devotes a chapter to decision theory. Brian Hedden (2023), following points in Christopher Hitchcock (2013), shows that the slogan characterization of causal decision theory as favoring options with good effects is not completely accurate. The theory’s guiding idea is, instead, to promote options that would have good outcomes if they were realized. Consequently, Hedden suggests renaming causal decision theory as counterfactual decision theory, but J. Dimitri Gallow (2024a) maintains that the name change is unnecessary. Some theorists argue for causal decision theory by showing that it has desirable features that distinguish it from other decision theories. Bacon (2022) shows that only following causal decision theory maximizes the expectation of actual value, the expectation he takes to be the basic action-guiding quantity. Nielsen (2024) shows that only causal decision theory respects the value of information.

## 2. History

This section tours causal decision theory’s history and along the way presents various formulations of the theory.

### 2.1 Newcomb’s Problem

Robert Nozick (1969) presented a dilemma for decision theory. He constructed an example in which the standard principle of dominance conflicts with the standard principle of expected-utility maximization. Nozick called the example Newcomb’s Problem after the physicist, William Newcomb, who first formulated the problem.

In Newcomb’s Problem an agent may choose either to take an opaque box or to take both the opaque box and a transparent box. The transparent box contains one thousand dollars that the agent plainly sees. The opaque box contains either nothing or one million dollars, depending on a prediction already made. The prediction was about the agent’s choice. If the prediction was that the agent will take both boxes, then the opaque box is empty. On the other hand, if the prediction was that the agent will take just the opaque box, then the opaque box contains a million dollars. The prediction is reliable. The agent knows all these features of his decision problem.

Figure 1 displays the agent’s options and their outcomes. A row represents an option, a column a state of the world, and a cell an option’s outcome in a state of the world.

*Figure 1.*

|   | Prediction one-boxing | Prediction two-boxing |
| --- | --- | --- |
| Take one box | $\$1{,}000{,}000$ | $\$0$ |
| Take two boxes | $\$1{,}001{,}000$ | $\$1{,}000$ |

Figure 1. Newcomb’s Problem

Because the outcome of two-boxing is better by $\$1{,}000$ than the outcome of one-boxing given each prediction, two-boxing dominates one-boxing. Two-boxing is the rational choice according to the principle of dominance. Because the prediction is reliable, a prediction of one-boxing has a high probability given one-boxing. Similarly, a prediction of two-boxing has a high probability given two-boxing. Hence, using conditional probabilities to compute expected utilities, one-boxing’s expected utility exceeds two-boxing’s expected utility. One-boxing is the rational choice according to the principle of expected-utility maximization.

Decision theory should address all possible decision problems and not just realistic decision problems. However, if Newcomb’s problem seems untroubling because unrealistic, realistic versions of the problem are plentiful. The essential feature of Newcomb’s problem is an inferior act’s correlation with a good state that it does not causally promote. In realistic, medical Newcomb problems, a medical condition and a behavioral symptom have a common cause and are correlated although neither causes the other. If the behavior is attractive, dominance recommends it although expected-utility maximization prohibits it. Also, Allan Gibbard and William Harper (1978: Sec. 12) and David Lewis (1979) observe that a Prisoner’s Dilemma with psychological twins, a case Section 1 mentions, poses a Newcomb problem for each player. For each player, the other player’s act is a state affecting the outcome. Acting cooperatively is a sign, but not a cause, of the other player’s acting cooperatively. Dominance recommends acting uncooperatively, whereas expected utility computed with conditional probabilities recommends acting cooperatively. In some realistic instances of the Prisoner’s Dilemma, the players’ anticipated similarity of thought creates a conflict between the principle of dominance and the principle of expected-utility maximization. Arif Ahmed (2018) collects essays by several authors on Newcomb’s problem, and Kenny Easwaran (2021) distinguishes Newcomb-like problems according to opportunities for causal intervention.

### 2.2 Stalnaker’s Solution

Robert Stalnaker (1968) presented truth conditions for subjunctive conditionals. A subjunctive conditional is true if and only if in the nearest antecedent-world, its consequent is true. (This analysis is understood so that a subjunctive conditional is true if its antecedent is true in no world.) Stalnaker used analysis of subjunctive conditionals to ground their role in decision theory and in a resolution of Newcomb’s problem.

In a letter to Lewis, Stalnaker (1972) proposed a way of reconciling decision principles in Newcomb’s problem. He suggested calculating an act’s expected utility using probabilities of conditionals in place of conditional probabilities. Accordingly,

$$ \textit{EU} (A) = \sum_i P(A \gt S_i)\util (A \amp S_i), $$

where $A \gt S_i$ stands for the conditional that if $A$ were performed then $S_i$ would obtain. Thus, instead of using the probability of a prediction of one-boxing given one-boxing, one should use the probability of the conditional that if the agent were to pick just one box, then the prediction would have been one-boxing. Because the agent’s act does not cause the prediction, the probability of the conditional equals the probability that the prediction is one-boxing. Also, consider the conditional that if the agent were to pick both boxes, then the prediction would have been one-boxing. Its probability similarly equals the probability that the prediction is one-boxing. The act the agent performs does not affect any prediction’s probability because the prediction occurs prior to the act. Consequently, using probabilities of conditionals to compute expected utility, two-boxing’s expected utility exceeds one-boxing’s expected utility. Therefore, the principle of expected-utility maximization makes the same recommendation as does the principle of dominance.

Gibbard and Harper (1978) elaborated and made public Stalnaker’s resolution of Newcomb’s problem. They distinguished causal decision theory, which uses probabilities of subjunctive conditionals, from evidential decision theory, which uses conditional probabilities. Because in decision problems probabilities of subjunctive conditionals track causal relations, using them to calculate an option’s expected utility makes decision theory causal.

Gibbard and Harper distinguished two types of expected utility. One type they called value and represented with $V$. It indicates news-value or auspiciousness. The other type they called utility and represented with $U$. It indicates efficacy in attainment of goals. A calculation of an act’s expected value uses conditional probabilities, and a calculation of its expected utility uses probabilities of conditionals. They argued that expected utility, calculated with probabilities of conditionals, yields genuine expected utility.

As Gibbard and Harper introduce $V$ and $U$, both rest on an assessment $D$ (for desirability) of maximally specific outcomes. Instead of adopting a formula for expected utility that uses an assessment of outcomes neutral with respect to evidential and causal decision theory, this essay follows Stalnaker (1972) in adopting a formula that uses utility to evaluate outcomes.

### 2.3 Variants

Consider a conditional asserting that if an option were adopted, then a certain state would obtain. Gibbard and Harper assume, to illustrate the main ideas of causal decision theory, that the conditional has a truth-value, and that, given its falsity, if the option were adopted, then the state would not obtain. This assumption may be unwarranted if the option is flipping a coin, and the relevant state is obtaining heads. It may be false (or indeterminate) that if the agent were to flip the coin, he would obtain heads. Similarly, the corresponding conditional about obtaining tails may be false (or indeterminate). Then probabilities of conditionals are not suitable for calculating the option’s expected utility. The relevant probabilities do not sum to one (or do not even exist). To circumvent such impasses, some theorists calculate causally-sensitive expected utilities without probabilities of subjunctive conditionals. Causal decision theory has many formulations.

Brian Skyrms (1980: Sec IIC; 1982) presented a version of causal decision theory that dispenses with probabilities of subjunctive conditionals. His theory separates factors that the agent’s act may influence from factors that the agent’s act may not influence. It lets $K_i$ stand for a possible full specification of factors that an agent may not influence and lets $C_j$ stand for a possible (but not necessarily full) specification of factors that the agent may influence. The set of $K_i$ forms a partition, and the set of $C_j$ forms a partition. The formula for an act’s expected utility first calculates its expected utility using factors the agent may influence, with respect to each possible combination of factors outside the agent’s influence. Then it computes a probability-weighted average of those conditional expected utilities. An act’s expected utility calculated this way is the act’s $K$-expectation, $\textit{EU}_k(A)$. According to Skyrms’s definition,

$$\textit{EU}_k(A) = \sum_i P(K_i)\sum_j P(C_j \mid K_i \amp A)\util (C_j \amp K_i \amp A).$$

Skyrms holds that an agent should select an act that maximizes $K$-expectation.

Lewis (1981) presented a version of causal decision theory that calculates expected utility using probabilities of dependency hypotheses instead of probabilities of subjunctive conditionals. A dependency hypothesis for an agent at a time is a maximally specific proposition about how the things the agent cares about do and do not depend causally on his present acts. An option’s expected utility is its probability-weighted average utility with respect to a partition of dependency hypotheses $K_i$. Lewis defines the expected utility of an option $A$ as

$$ \textit{EU} (A) = \sum_i P(K_i)\util (K_i \amp A) $$

and holds that to act rationally is to realize an option that maximizes expected utility. His formula for an option’s expected utility is the same as Skyrms’s assuming that $U(K_i \amp A)$ may be expanded with respect to a partition of factors the agent may influence, using the formula

$$ U(K_i \amp A) = \sum_j P(C_j\mid K_i \amp A)\util (C_j \amp K_i \amp A). $$

Skyrms’s and Lewis’s calculations of expected utility dispense with causal probabilities. They build causality into states of the world so that causal probabilities are unnecessary. In cases such as Newcomb’s problem, their calculations yield the same recommendations as calculations of expected utility employing probabilities of subjunctive conditionals. The various versions of causal decision theory make equivalent recommendations when cases meet their background assumptions. Adam Bales (2016) compares versions in special cases that do not meet the background assumptions.

### 2.4 Representation Theorems

Decision theory often introduces probability and utility with representation theorems. These theorems show that if preferences among acts meet certain constraints, such as transitivity, then there exist a probability function and a utility function (given a choice of scale) that generate expected utilities agreeing with preferences. David Krantz, R. Duncan Luce, Patrick Suppes, and Amos Tversky (1971) offer a good, general introduction to the purposes and methods of constructing representations theorems. In Section 3.1, I discuss the theorems’ function in decision theory.

Richard Jeffrey ([1965] 1983) presented a representation theorem for evidential decision theory, using its formula for expected utility. Brad Armendt (1986, 1988a) presented a representation theorem for causal decision theory, using its formula for expected utility. James Joyce (1999) constructed a very general representation theorem that yields either causal or evidential decision theory depending on the interpretation of probability that the formula for expected utility adopts.

### 2.5 Objections

The most common objection to causal decision theory is that it yields the wrong choice in Newcomb’s problem. It yields two-boxing, whereas one-boxing is correct. Terry Horgan (1981 [1985]), Paul Horwich (1987: Chap. 11), and Caspar Hare and Brian Hedden (2016) for example, promote one-boxing. The main rationale for one-boxing is that one-boxers fare better than do two-boxers. Causal decision theorists respond that Newcomb’s problem is an unusual case that rewards irrationality. One-boxing is irrational even if one-boxers prosper. Bales (2018) rejects the argument that two-boxing is irrational

Some theorists hold that one-boxing is plainly rational if the prediction is completely reliable. They maintain that if the prediction is certainly accurate, then choice reduces to taking $\$M$ or taking $\$T$. This view oversimplifies. If an agent one-boxes, then that act is certain to yield $\$M$. However, the agent still would have done better by taking both boxes. Dominance still recommends two-boxing. Making the prediction certain to be accurate does not change the character of the problem. Efficacy still trumps auspiciousness, as Howard Sobel (1994: Chap. 5) argues.

A way of reconciling the two sides of the debate about Newcomb’s problem acknowledges that a rational person should prepare for the problem by cultivating a disposition to one-box. Then whenever the problem arises, the disposition will prompt a prediction of one-boxing and afterwards the act of one-boxing (still freely chosen). Causal decision theory may acknowledge the value of this preparation. It may conclude that cultivating a disposition to one-box is rational although one-boxing itself is irrational. Hence, if in Newcomb’s problem an agent two-boxes, causal decision theory may concede that the agent did not rationally prepare for the problem. It nonetheless maintains that two-boxing itself is rational. Although two-boxing is not the act of a maximally rational agent, it is rational given the circumstances of Newcomb’s problem.

Causal decision theory may also explain that it advances a claim about the evaluation of an act given the agent’s circumstances in Newcomb’s problem. It asserts two-boxing’s conditional rationality. Conditional and nonconditional rationality treat mistakes differently. In contrast with conditional rationality, nonconditional rationality does not grant past mistakes. It evaluates an act taking account of the influence of past mistakes. However, conditional rationality accepts present circumstances as they are and does not discredit an act because it stems from past mistakes. Causal decision theory maintains that two-boxing is rational, granting the agent’s circumstances and so ignoring any mistakes leading to those circumstances, such as irrational preparation for Newcomb’s problem.

Another objection to causal decision theory concedes that two-boxing is the rational choice in Newcomb’s problem but rejects causal principles of choice that yield two-boxing. It seeks noncausal principles that yield two-boxing. Positivism is a source of aversion to decision principles incorporating causation. Some decision theorists shun causation because no positivist account specifies its nature. Without a definition of causation in terms of observable phenomena, they prefer that decision theory avoid causation. Causal decision theory’s response to this objection is both to discredit positivism and also to clarify causation so that puzzles concerning it no longer give decision theory any reason to avoid it.

Evidential decision theory has weaker metaphysical assumptions than has causal decision theory, even if causation has impeccable metaphysical credentials. Some decision theorists do not omit causation because of metaphysical scruples but for conceptual economy. Jeffrey ([1965] 1983, 2004), for the sake of parsimony, formulates decision principles that do not rely on causal relations.

Ellery Eells (1981, 1982) contends that evidential decision theory yields causal decision theory’s recommendations but, more economically, without reliance on causal apparatus. In particular, evidential decision theory yields two-boxing in Newcomb’s problem. An agent’s reflection on his evidence makes conditional probabilities support two-boxing.

A noncontentious elaboration of Newcomb’s problem posits that the agent’s choice and its prediction have a common cause. The agent’s choice is evidence of the common cause and evidence of the choice’s prediction. Once an agent acquires the probability of the common cause, he may put aside the evidence his choice provides about the prediction. That evidence is superfluous. Given the probability of the common cause, the probability of a prediction of one-boxing is constant with respect to his options. Similarly, the probability of a prediction of two-boxing is constant with respect to his options. Because the probability of a prediction is the same conditional on either option, the expected utility of two-boxing exceeds the expected utility of one-boxing according to evidential decision theory. Horgan (1981 [1985]) and Huw Price (1986) make similar points.

Suppose that an event $S$ is a sign of a cause $C$ that produces an effect $E$. For the probability of $E$, knowing whether $C$ holds makes superfluous knowing whether $S$ holds. Observation of $C$ *screens off* the evidence that $S$ provides for $E$. That is, $P(E\mid C \amp S) = P(E\mid C)$. In Newcomb’s problem, assuming that the agent is rational, his beliefs and desires are a common cause of his choice and the prediction. So his choice is a sign of the prediction’s content. For the probability of a prediction of one-boxing, knowing one’s beliefs and desires makes superfluous knowing the choice that they yield. Knowledge of the common cause screens off evidence that the choice provides about the prediction. Hence, the probability of a prediction of one-boxing is constant with respect to one’s choice, and maximization of evidential expected-utility agrees with the principle of dominance. This defense of evidential decision theory is called the tickle defense because it assumes that an introspected condition screens off the correlation between choice and prediction.

Eells’s defense of evidential decision theory assumes that an agent chooses according to beliefs and desires and knows his beliefs and desires. Some agents may not choose this way and may not have this knowledge. Decision theory should prescribe a rational choice for such agents, and evidential decision theory may not do that correctly, as Lewis (1981: 10–11) and John Pollock (2010) argue. Armendt (1988b: 326–329) and David Papineau (2001: 252–255) concur that the phenomenon of screening off does not in all cases make evidential decision theory yield the results of causal decision theory.

Horwich (1987: Chap. 11) rejects Eells’s argument because, even if an agent knows that her choice springs from her beliefs and desires, she may be unaware of the mechanism by which her beliefs and desires produce her choice. The agent may doubt that she chooses by maximizing expected utility. Then in Newcomb’s problem her choice may offer relevant evidence about the prediction. Eells (1984a) constructs a dynamic version of the tickle defense to meet this objection. Sobel (1994: Chap. 2) discusses that version of the defense. He argues that it does not yield evidential decision theory’s agreement with causal decision theory in all decision problems in which an act furnishes evidence concerning the state of the world. Moreover, it does not establish that an evidential theory of rational desire agrees with a causal theory of rational desire. He concludes that even in cases where evidential decision theory yields the right recommendation, it does not yield it for the right reasons.

Jeffrey (1981) and Eells (1984b) use tickles or metatickles to reconcile evidential and causal decision theory, and Huttegger (2023) elaborates the method of reconciliation in the case of Newcomb’s problem using deliberational dynamics in the style of Skyrms (1990). He notes, however that the reconciliation makes assumptions that some cases do not meet. The two decision theories may disagree if the predictor knows more about the agent’s decision-making than does the agent.

Price (2012) proposes a blend of evidential and causal decision theory and motivates it with an analysis of cases in which an agent has foreknowledge of an event occurring by chance. Causal decision theory on its own accommodates such cases, argue Bales (2016) and Gallow (2024b). Ahmed (2014a) champions evidential decision theory and advances several objections to causal decision theory. His objections assume some controversial points about rational choice, including a controversial principle for sequences of choices. A common view distinguishes principles for evaluating choices from principles for evaluating sequences of choices. The principle of utility maximization evaluates an agent’s choice as a resolution of a decision problem only if the agent has direct control of each option in the decision problem, that is, only if the agent can at will immediately adopt any option in the decision problem. The principle does not evaluate an agent’s sequence of multiple choices because the agent does not have direct control of such a sequence. She realizes a sequence of multiple choices only by making each choice in the sequence at the time for it; she cannot at will immediately realize the entire sequence. Rationality evaluates an option in an agent’s direct control by comparing it with alternatives but evaluates a sequence in an agent’s indirect control by evaluating the directly controlled options in the sequence; a sequence of choices is rational if the choices in the sequence are rational. Adopting this common method of evaluating sequences of choices fends off objections to causal decision theory that assume rival methods.

## 3. Current Issues

Decision theory is an active area of research. Current work addresses a number of problems. Causal decision theory’s approach to those problems arises from its nonpositivistic methodology and its attention to causation. This section mentions some topics on causal decision theory’s agenda.

### 3.1 Probability and Utility

Principles of causal decision theory use probabilities and utilities. The interpretation of probabilities and utilities is a matter of debate. One tradition defines them in terms of functions that representation theorems introduce to depict preferences. The representation theorems show that if preferences meet certain structural axioms, then if they also meet certain normative axioms, they are as if they follow expected utility. That is, preferences follow expected utility calculated using probability and utility functions constructed so that preferences follow expected utility. Expected utility calculated this way differs from expected utility calculated using probability and utility assignments grounded in attitudes toward possible outcomes. For example, a person confused about bets concerning a coin toss may have preferences among those bets that are as if he assigns probability 60% to heads, when, in fact, the evidence of past tosses leads him to assign probability 40% to heads. Consequently, when preferences meet a representation theorem’s structural axioms, the theorem’s normative axioms justify only conformity with expected utility fabricated to agree with preferences and do not justify conformity with expected utility in the traditional sense. Defining probability and utility using the representation theorems thus weakens the traditional principle of expected utility. It becomes merely a principle of coherence among preferences.

Instead of using the representation theorems to define probabilities and utilities, decision theory may use them to establish probabilities’ and utilities’ measurability when preferences meet structural and normative axioms. This employment of the representation theorems allows decision theory to advance the traditional principle of expected utility and thereby enrich its treatment of rational decisions. Decision theory may justify that traditional principle by deriving it from general principles of evaluation, as in Weirich (2001).

A broad account of probabilities and utilities takes them to indicate attitudes toward propositions. They are rational degrees of belief and rational degrees of desire, respectively. This account of probabilities and utilities recognizes their existence in cases where they are not inferable from preferences or their other effects but instead are inferable from their causes, such as an agent’s information about objective probabilities, or are not inferable at all (except perhaps by introspection). The account relies on arguments that degrees of belief and degrees of desire, if rational, conform to standard principles of probability and utility. Bolstering these arguments is work for causal decision theory.

Besides clarifying its general interpretation of probability and utility, causal decision theory searches for the particular probabilities and utilities that yield the best version of its principle to maximize expected utility. The causal probabilities in its formula for expected utility may be probabilities of subjunctive conditionals or various substitutes. Versions that use probabilities of subjunctive conditionals must settle on an analysis of those conditionals. Lewis (1973: Chap. 1) modifies Stalnaker’s analysis to count a subjunctive conditional true if and only if as antecedent worlds come closer and closer to the actual world, there is a point beyond which the consequent is true in all the worlds at least that close. Joyce (1999: 161–180) advances probability images, as Lewis (1976) introduces them, as substitutes for probabilities of subjunctive conditionals. The probability image of a state $S$ under subjunctive supposition of an act $A$ is the probability of $S$ according to an assignment that shifts the probability of ${\sim}A$-worlds to nearby $A$-worlds. Causal relations among an act and possible states guide probability’s reassignment.

A common formula for an act’s expected utility takes the utility for an act-state pair, the utility of the act’s outcome in the state, to be the utility of the act’s and the state’s conjunction:

$$ \textit{EU} (A) = \sum_i P(A \gt S_i)\util (A \amp S_i). $$

Does causal decision theory need an alternative, more causally-sensitive utility for an act-state pair? Weirich (1980) argues that it does. A person contemplating a wager that the capital of Missouri is Jefferson City entertains the consequences if he *were* to make the wager given that St. Louis *is* Missouri’s capital. A rational deliberator subjunctively supposes an act attending to causal relations and indicatively supposes a state attending to evidential relations, but can suppose an act’s and a state’s conjunction only one way. Furthermore, using the utility of an act’s and a state’s conjunction prevents an act’s expected utility from being partition-invariant. The next subsection elaborates this point.

### 3.2 Partition Invariance

An act’s expected utility is partition invariant if and only if it is the same under all partitions of states. Partition invariance is a vital property of an act’s expected utility. If acts’ expected utilities lack this property, then decision theory may use only expected utilities computed from selected partitions. Expected utility’s partition invariance makes an act’s expected utility independent of selection of a partition of states and thereby increases expected utility’s explanatory power.

Partition invariance ensures that various representations of the same decision problem yield solutions that agree. Take Newcomb’s problem with Figure 2’s representation.

*Figure 2.*

|   | Right prediction | Wrong prediction |
| --- | --- | --- |
| Take only one box | $\$1{,}000{,}000$ | $0 |
| Take two boxes | $\$1{,}000$ | $\$1{,}001{,}000$ |

Figure 2. New States for Newcomb’s Problem

Dominance does not apply to this representation. It nonetheless settles the problem’s solution because it applies to a decision problem if it applies to any accurate representation of the problem, such as Figure 1’s representation of the problem. If expected utilities are partition-sensitive, then acts that maximize expected utility may be partition-sensitive. The principle of expected utility does not yield a decision problem’s solution, however, if acts of maximum expected-utility change from one partition to another. In that case an act is not a solution to a decision problem simply because it maximizes expected utility under some accurate representation of the problem. Too many acts have the same credential.

The expected utility principle, using probabilities of conditionals, applies to Figure 2’s representation of Newcomb’s problem. Letting $P1$ stand for a prediction of one-boxing and $P2$ stand for a prediction of two-boxing, the acts’ expected utilities are:

$$ \begin{align} \textit{EU} (1) & = P(1 \gt R)\util (\$1{,}000{,}000) + P(1 \gt W)0\\ & = P(P1)\util (\$1{,}000{,}000)\\ \textit{EU} (2) & = P(2 \gt R)\util (\$1{,}000) + P(2 \gt W)\util (\$1{,}001{,}000)\\ & = P(P2)\util (\$1{,}000) + P(P1)\util (\$1{,}000{,}000)\\ \end{align} $$

Hence $\textit{EU}(1) \lt EU(2)$. This result agrees with the verdict of causal decision theory given other accurate representations of the problem. Provided that causal decision theory uses a partition-invariant formula for expected utility, its recommendations are independent of a decision problem’s representation.

Lewis (1981: 12–13) observes that the formula

$$ EU(A) = \sum_i P(S_i)\util (A \amp S_i) $$

is not partition invariant. Its results depend on the partition of states. If a state is a set of worlds with equal utilities, then with respect to a partition of such states every act has the same expected utility. An element $S_i$ of the partition obscures the effects of $A$ that the utility of an outcome should evaluate. Lewis overcomes this problem by using only partitions of dependency hypotheses. However, causal decision theory may craft a partition-invariant formula for expected utility by adopting a substitute for $U(A \amp S_i)$.

Sobel (1994: Chap. 9) investigates partition invariance. Putting his work in this essay’s notation, he proceeds as follows. First, he takes a canonical computation of an option’s expected utility to use worlds as states. His basic formula is

$$ \textit{EU} (A) = \sum_i P(A \gt W_i)\util (W_i). $$

A world $W_i$ absorbs an act performed in it. Only the worlds in which $A$ holds contribute positive probabilities and so affect the sum. Next, Sobel searches for other computations, using coarse-grained states, that are equivalent to the canonical computation. A suitable specification of utilities achieves partition invariance given his assumptions. According to a theorem he proves (1994: 185),

$$ U(A) = \sum_i P(S_i)\util (A \mbox{ given } S_i) $$

for any partition of states.

Joyce (2000: S11) also articulates for causal decision theory a partition-invariant formula for an act’s expected utility. He achieves partition invariance, assuming that

$$ \textit{EU} (A) = \sum_i P(A \gt S_i)\util (A \amp S_i), $$

by stipulating that $U(A \amp S_i)$ equals

$$ \sum_{ij} P^A(W_j\mid S_i)\util (W_j), $$

where $W_j$ is a world and $P^A$ stands for the probability image of $A$. Weirich (2001: Secs. 3.2, 4.2.2), as Sobel does, substitutes $U(A \mbox{ given }S_i)$ for $U(A \amp S_i)$ in the formula for expected utility and interprets $U(A \mbox{ given }S_i)$ as the utility of the outcome that $A$’s realization would produce if $S$ obtains. Accordingly, $U(A \mbox{ given }S_i)$ responds to $A$’s causal consequences in worlds where $S_i$ holds. Then the formula

$$ \textit{EU} (A) = \sum_i P(S_i) \util (A \mbox{ given }S_i) $$

is invariant with respect to partitions in which states are probabilistically independent of the act. A more complex formula,

$$ \textit{EU} (A) = \sum_i P(S_i \mbox{ if }A)\util (A \mbox{ given } (S_i \mbox{ if } A)), $$

assuming a causal interpretation of its probabilities, relaxes all restriction on partitions. $U(A \mbox{ given }(S_i \mbox{ if }A))$ is the utility of the outcome if $A$ were realized, given that it is the case that $S_i$ would obtain if $A$ were realized.

### 3.3 Outcomes

One issue concerning outcomes is their comprehensiveness. Are an act’s outcomes possible worlds, temporal aftermaths, or causal consequences? Gibbard and Harper ([1978] 1981: 166–168) mention the possibility of narrowing outcomes to causal consequences, as practical applicability advocates. The narrowing must be judicious, however, because the expected-utility principle requires that outcomes include every relevant consideration. For example, if an agent is averse to risk, then each of a risky act’s possible outcomes must include the risk the act generates. Its inclusion tends to lower each possible outcome’s utility.

In Sobel’s canonical formula for expected utility,

$$ \textit{EU} (A) = \sum_i P(A \gt W_i)\util (W_i). $$

The formula, from one perspective, omits states of the world because the outcomes themselves form a partition. The distinction between states and outcomes dissolves because worlds play the role of both states and outcomes. States are dispensable means of generating outcomes that are exclusive and exhaustive. According to a basic principle, an act’s expected utility is a probability-weighted average of possible outcomes that are exclusive and exhaustive, such as the worlds to which the act may lead.

Suppose that a world’s utility comes from realization of basic intrinsic desires and aversions. Granting that the utilities of their realizations are additive, the utility of a world is a sum of the utilities of their realizations. Then besides being a probability-weighted average of the utilities of worlds to which it may lead, an option’s expected utility is also a probability-weighted average of the realizations of basic intrinsic desires and aversions. In this formula for its expected utility, states play no explicit role:

$$ \textit{EU} (A) = \sum_i P(A \gt B_i)\util (B_i), $$

where $B_i$ ranges over possible realizations of basic intrinsic desires and aversions. The formula considers for each basic desire and aversion the prospect of its realization if the act were performed. It takes the act’s expected utility as the sum of the prospects’ utilities. The formula provides an economical representation of an act’s expected utility. It eliminates states and obtains expected utility directly from outcomes taken as realizations of basic desires and aversions.

To illustrate calculation of an act’s expected utility using basic intrinsic desires and aversions, suppose that an agent has no basic intrinsic aversions and just two basic intrinsic desires, one for health and the other for wisdom. The utility of health is 4, and the utility of wisdom is 8. In the formula for expected utility, a world covers only matters about which the agent cares. In the example, a world is a proposition specifying whether the agent has health and whether he has wisdom. Accordingly, there are four worlds: $$ \begin{align} H \amp W, \\ H \amp {\sim}W, \\ {\sim}H \amp W, \\ {\sim}H \amp {\sim}W.\\ \end{align} $$

Suppose that $A$ is equally likely to generate any world. Using worlds,

$$ \begin{align} \textit{EU} (A) & = P(A \gt(H \amp W))\util (H \amp W) \\ &\qquad + P(A \gt(H \amp{\sim}W))\util (H \amp{\sim}W) \\ &\qquad + P(A \gt({\sim}H \amp W))\util ({\sim}H \amp W) \\ &\qquad + P(A \gt({\sim}H \amp{\sim}W))\util ({\sim}H \amp{\sim}W) \\ & = (0.25)(12) + (0.25)(4) + (0.25)(8) + (0.25)(0) \\ & = 6.\\ \end{align} $$

Using basic intrinsic attitudes,

$$ \begin{align} \textit{EU} (A) &= P(A \gt H)\util (H) + P(A \gt W)\util (W) \\ & = (0.5)(4) + (0.5)(8) \\ & = 6. \end{align} $$

The two methods of computing an option’s utility are equivalent given that, under supposition of an act’s realization, the probability of a basic intrinsic desire’s or aversion’s realization is the sum of the probabilities of the worlds that realize it.

### 3.4 Acts

In deliberations, a first-person action proposition represents an act. The proposition has a subject-predicate structure and refers directly to the agent, its subject, without the intermediary of a concept of the agent. A centered world represents the proposition. Such a world not only specifies individuals and their properties and relations, but also specifies which individual is the agent and where and when his decision problem arises. Realization of the act is realization of a world with, at its center, the agent at the time and place of his decision problem.

Isaac Levi (2000) objects to any decision theory that attaches probabilities to acts. He holds that deliberation crowds out prediction. While deliberating, an agent does not have beliefs or degrees of belief about the act that she will perform. Levi holds that Newcomb’s problem, and evidential and causal decision theories that address it, involve mistaken assignments of probabilities to an agent’s acts. He rejects both Jeffrey’s ([1965] 1983) evidential decision theory and Joyce’s (1999) causal decision theory because they allow an agent to assign probabilities to her acts during deliberation.

In opposition to Levi’s views, Joyce (2002) argues that (1) causal decision theory need not accommodate an agent’s assigning probabilities to her acts, but (2) a deliberating agent may legitimately assign probabilities to her acts. Evidential decision theory computes an act’s expected utility using the probability of a state given the act, $P(S\mid A)$, defined as $P(S \amp A)/P(A)$. The fraction’s denominator assigns a probability to an act. Causal decision theory replaces $P(S\mid A)$ with $P(A \gt S)$ or a similar causal probability. It need not assign a probability to an act.

May an agent deliberating assign probabilities to her possible acts? Yes, a deliberator may sensibly assign probabilities to any events, including her acts. Causal decision theory may accommodate such probabilities by forgoing their measurement with betting quotients. According to that method of measurement, willingness to make bets indicates probabilities. Suppose that a person is willing to take either side of a bet in which the stake for the event is $x$ and the stake against the event is $y$. Then the probability the person assigns to the event is the betting quotient $x/(x + y)$. This method of measurement may fail when the event is an agent’s own future act. A bet on an act’s realization may influence the act’s probability, as a thermometer’s temperature may influence the temperature of a liquid it measures.

Joyce (2007: 552–561) considers whether Newcomb problems are genuine decision problems despite strong correlations between states and acts. He concludes that, yes, despite those correlations, an agent may view her decision as causing her act. An agent’s decision supports a belief about her act independently of prior correlations between states and her act. According to a principle of evidential autonomy (2007: 557),

> A deliberating agent who regards herself as free need not proportion her beliefs about her own acts to the antecedent evidence that she has for thinking that she will perform them.

She should proportion her beliefs to her total evidence, including her self-supporting beliefs about her own acts. Those beliefs provide new relevant evidence about her acts.

How should an agent deliberating about an act understand the background for her act? She should not adopt a backtracking supposition of her act. Standing on the edge of a cliff, she should not suppose that if she were to jump, she would have a parachute to break her fall. Also, she should not imagine gratuitous changes in her basic desires. She should not imagine that if she were to choose chocolate instead of vanilla, despite currently preferring vanilla, that she would then prefer chocolate. She should imagine that her basic desires are constant as she imagines the various acts she may perform, and, moreover, should adopt during deliberations the pretense that her will generates her act independently of her basic desires and aversions.

Christopher Hitchcock (1996) holds that an agent should pretend that her act is free of causal influence. Doing this makes partitions of states yielding probabilities for decisions agree with partitions of states yielding probabilities defining causal relevance. As a result, probabilities in causal decision theory may form a foundation for probabilities in the probabilistic theory of causation. Causal decision theory, in particular, the version using dependency hypotheses, grounds theories of probabilistic causation.

Ahmed (2013) argues that causal decision theory goes awry in cases in which the universe is deterministic. In response, Alexander Sandgren and Timothy Luke Williamson (2021), Adam Elga (2022), Boris Kment (2023), and Williamson and Sandgren (2023) propose amendments to causal decision theory. Joyce (2016), Melissa Fusco (2023), and Calum McNamara (2023) defend causal decision theory against Ahmed’s objection.

### 3.5 Generalizing Expected Utility

Problems such as Pascal’s Wager and the St. Petersburg paradox suggest that decision theory needs a means of handling infinite utilities and expected utilities. Suppose that an option’s possible outcomes all have finite utilities. Nonetheless, if those utilities are infinitely many and unbounded, then the option’s expected utility may be infinite. Alan Hájek and Harris Nover (2006) also show that the option may have no expected utility. The order of possible outcomes, which is arbitrary, may affect convergence of their utilities’ probability-weighted average and the value to which the average converges if it does converge. Causal decision theory should generalize its principle of expected-utility maximization to handle such cases.

Also, common principles of causal decision theory advance standards of rationality that are too demanding to apply to humans. They are standards for ideal agents in ideal circumstances (a precise formulation of the idealizations may vary from theorist to theorist). Making causal decision theory realistic requires relaxing idealizations that its principles assume. A generalization of the principle of expected-utility maximization, for example, may relax idealizations to accommodate limited cognitive abilities. Weirich (2004, 2021) and Pollock (2006) take steps in this direction. Appropriate generalizations distinguish taking maximization of expected utility as a procedure for making a decision and taking it as a standard for evaluating a decision even after the decision has been made.

### 3.6 Decision Instability

Gibbard and Harper (1978: Sec. 11) present a problem for causal decision theory using an example drawn from literature. A man in Damascus knows that he has an appointment with Death at midnight. He will escape Death if he manages at midnight not to be at the place of his appointment. He can be in either Damascus or Aleppo at midnight. As the man knows, Death is a good predictor of his whereabouts. If he stays in Damascus, he thereby has evidence that Death will look for him in Damascus. However, if he goes to Aleppo he thereby has evidence that Death will look for him in Aleppo. Wherever he decides to be at midnight, he has evidence that he would be better off at the other place. No decision is stable. Decision instability arises in cases in which a choice provides evidence for its outcome, and each choice provides evidence that another choice would have been better. Reed Richter (1984, 1986) uses cases of decision instability to argue against causal decision theory. The theory needs a resolution of the problem of decision instability. The problem does not refute causal decision theory but shows that it needs generalization to handle cases of decision instability.

A common analysis of the problem classifies options as either self-ratifying or not self-ratifying. Jeffrey ([1965] 1983) introduced ratification as a component of evidential decision theory. His version of the theory evaluates a decision according to the expected utility of the act it selects. The distinction between an act and a decision to perform the act grounds his definition of an option’s self-ratification and his principle to make self-ratifying, or ratifiable, decisions. According to his definition ([1965] 1983: 16),

> A ratifiable decision is a decision to perform an act of maximum estimated desirability relative to the probability matrix the agent thinks he would have if he finally decided to perform that act.

Estimated desirability is expected utility. An agent’s probability matrix is an array of rows and columns for acts and states, respectively, with each cell formed by the intersection of an act’s row and a state’s column containing the probability of the state given that the agent is about to perform the act. Before performing an act, an agent may assess the act in light of a decision to perform it. Information the decision carries may affect the act’s expected utility and its ranking with respect to other acts.

Jeffrey used ratification as a means of making evidential decision theory yield the same recommendations as causal decision theory. In Newcomb’s problem, for instance, two-boxing is the only self-ratifying option. However, Jeffrey (2004: 113n) concedes that evidential decision theory’s reliance on ratification does not make it agree with causal decision theory in all cases. Moreover, Joyce (2007) argues that the motivation for ratification appeals to causal relations, so that even if it yields correct recommendations using Jeffrey’s formula for expected utility, it still does not yield a purely evidential decision theory.

Causal decision theory’s account of self-ratification may put aside Jeffrey’s method of evaluating a decision by evaluating the act it selects. Because the decision and the act differ, they may have different consequences. For example, a decision may fail to generate the act it selects. Hence, the decision’s expected utility may differ from the act’s expected utility. Driving through a flooded section of highway may have high expected utility because it minimizes travel time to one’s destination. However, the decision to drive through the flooded section may have low expected utility because for all one knows the water may be deep enough to swamp the car. Using an act’s expected utility to assess a decision to perform the act leads to faulty evaluations of decisions. As, for example, Hedden (2012) maintains, it is better to evaluate a decision by comparing its expected utility to the expected utilities of rival decisions. A decision’s expected utility depends on the probability of its execution as well as the expected consequences of the act it selects.

Weirich (1985) and Harper (1986) define ratification in terms of an option’s expected utility given its realization rather than given a decision to realize it. An option is self-ratifying if and only if it maximizes expected utility given its realization. This account of ratification accommodates cases in which an option and a decision to realize it have different expected utilities. Weirich and Harper also assume causal decision theory’s formula for expected utility. In the case of Death in Damascus, causal decision theory concludes that the threatened man lacks a self-ratifying option. A self-ratifying option emerges, however, if the man may flip a coin to make his decision. Adopting the probability distribution for locations is called a mixed strategy, whereas choices of location are called pure strategies. Assuming that Death cannot predict the coin flip’s outcome, the mixed strategy is self-ratifying.

During deliberations to resolve a decision problem, an agent may revise the probabilities she assigns to pure strategies in light of computations of their expected utilities using earlier probability assignments. The process of revision may culminate in a stable probability assignment that represents a mixed strategy. Skyrms (1982, 1990) and Eells (1984b) investigate these dynamics of deliberation. Some open issues are whether adoption of a mixed strategy resolves a decision problem and whether a pure strategy arising from a mixed strategy that constitutes an equilibrium of deliberations is rational if the pure strategy itself is not self-ratifying.

Andy Egan (2007) argues that causal decision theory yields the wrong recommendation in decision problems with an option that provides evidence concerning its outcome. He entertains the case of an assassin who deliberates about pulling the trigger, knowing that the option’s realization provides evidence of a brain lesion that ruins his aim. Egan maintains that causal decision theory mistakenly ignores the evidence that the option provides. However, versions of causal decision theory that incorporate ratification are innocent of the charges. Ratification takes account of evidence an option provides concerning its outcome.

Any version of the expected utility principle, whether it uses conditional probabilities or probabilities of conditionals, must specify the information that guides assignments of probabilities and utilities. Principles of nonconditional expected-utility maximization use the same information for all options, and hence exclude information about an option’s realization. The principle of ratification uses for each option information that includes the option’s realization. It is a principle of conditional expected-utility maximization. Egan’s cases count against nonconditional expected-utility maximization, and not against causal decision theory. Conditional expected-utility maximization using causal decision theory’s formula for expected utility addresses the cases he presents.

Egan’s examples do not refute causal decision theory but present a challenge for it. Suppose that in a decision problem no self-ratifying option exists, or multiple self-ratifying options exist. How should a rational agent proceed, granting that a decision principle should take account of information that an option provides? This is an open problem in causal decision theory (and in any decision theory acknowledging that an option’s realization may constitute evidence concerning its outcome). Ratification analyzes decision instability but is not a complete response to it.

In response to Egan, Frank Arntzenius (2008) and Joyce (2012) argue that in some decision problems an agent’s rational deliberations using freely available information do not settle on a single option but instead settle on a probability distribution over options. They acknowledge that the agent may regret the option issuing from these deliberations but differ about the regret’s significance. Arntzenius holds that the regret counts against the option’s rationality, whereas Joyce denies this. Ahmed (2012) and Ralph Wedgwood (2013) reject Arntzenius’s and Joyce’s responses to Egan because they hold that deliberations should settle on an option. Wedgwood introduces a novel decision principle to accommodate Egan’s decision problems. Ahmed contends that Egan’s analysis of these decision problems has a flaw because when it is extended to some other decision problems, it declares every option irrational. Anna Kusser and Wolfgang Spohn (1992: 17–18) show that decision instability may arise because an option’s realization changes utilities, instead of probabilities, of possible outcomes.

Ahmed (2014b) and Jack Spencer (2021) criticize causal decision theory in cases of decision instability, and Spencer and Ian Wells (2019) criticize a principle of causal dominance attributed to causal decision theory. Gallow (2024c) argues that a decision theory that removes instability also rejects the sure-thing principle (a principle of dominance). Rhys Borchert and Spencer (2024) argue that solutions to problems with decision instability are hard to reconcile with two-boxing in Newcomb’s problem. To handle cases of decision instability, Benjamin Levinstein and Nate Suares (2020) advance *functional decision theory*, even though it permits one-boxing in Newcomb’s Problem. Gallow (2020) and David Barnett (2022) introduce *degrees of ratifiability*. In a decision problem with two options *A* and *B*, *A*’s degree of ratifiability is *U*(*A* given *A*) – *U*(*B* given *A*), and similarly for *B*. They propose that the rationally preferable option has the greater degree of ratifiability. Spencer (2023) argues that this proposal in some cases forbids an option that an agent will realize and that has better prospects than all other options because of the information that the option’s realization carries. Joyce (2018), Armendt (2019), Bales (2020), and Greg Lauro and Simon Huttegger (2021), and Williamson (2021) elaborate ways that causal decision theory may respond to decision instability.

Points about ratification in decision problems clarify points about equilibrium in game theory because in games of strategy a player’s choice often furnishes evidence about other players’ choices. Decision theory underlies game theory because a game’s solution identifies rational choices in the decision problems the game creates for the players. Solutions to games distinguish correlation and causation, as do decision principles. Because in simultaneous-move games two agent’s strategies may be correlated but not related as cause and effect, solutions to such games do not have the same properties as solutions to sequential games. Causal decision theory attends to distinctions on which solutions to games depend. It supports game theory’s account of interactive decisions. Joyce and Gibbard (2016) describe the role of ratification in game theory, and Stalnaker (2018) describes causal decision theory’s place in game theory.

The existence of self-ratifying mixed strategies in decision problems such as Death in Damascus suggests that ratification, as causal decision theory explains it, supports participation in a Nash equilibrium of a game. Such an equilibrium assigns a strategy to each player so that each strategy in the assignment is a best response to the others. Suppose that two people are playing Matching Pennies. Simultaneously, each displays a penny. One player tries to make the sides match, and the other player tries to prevent a match. If the first player succeeds, he gets both pennies. Otherwise, the second player gets both pennies. Suppose that each player is good at predicting the other player, and each player knows this. Then if the first player displays heads, he has reason to think that the second player displays tails. Also, if the first player displays tails, he has reason to think that the second player displays heads. Because Matching Pennies is a simultaneous-move game, neither player’s strategy influences the other player’s strategy, but each player’s strategy is evidence of the other player’s strategy. Mixed strategies help resolve decision instability in this case. If the first player flips his penny to settle the side to display, then his mixed strategy is self-ratifying. The second player’s situation is similar, and she also reaches a self-ratifying strategy by flipping her penny. The combination of self-ratifying strategies is a Nash equilibrium of the game.

Weirich (2004: Chap. 9) presents a method of selecting among multiple self-ratifying strategies, and hence a method by which a group of players may coordinate to realize a particular Nash equilibrium when several exist. Although decision instability is an open problem, causal decision theory has resources for addressing it. The theory’s eventual resolution of the problem will offer game theory a justification for participation in a Nash equilibrium of a game.

## 4. Related Topics and Concluding Remarks

Causal decision theory has foundations in various areas of philosophy. For example, it relies on metaphysics for an account of causation. It also relies on inductive logic for an account of inferences concerning causation. A comprehensive causal decision theory treats not only causal probabilities’ generation of options’ expected utilities, but also evidence’s generation of causal probabilities.

Research concerning causation contributes to the metaphysical foundations of causal decision theory. Nancy Cartwright (1979), for example, draws on ideas about causation to flesh out details of causal decision theory. Also, some accounts of causation distinguish types of causes. Both oxygen and a flame are metaphysical causes of tinder’s combustion. However, only the flame is causally responsible for, and so a normative cause of, the combustion. Causal responsibility for an event accrues to just the salient metaphysical causes of the event. Causal decision theory is interested not only in events for which an act is causally responsible, but also in other events for which an act is a metaphysical cause. Expected utilities that guide decisions are comprehensive.

Judea Pearl (2000) and also Peter Spirtes, Clark Glymour, and Richard Scheines (2000) present methods of inferring causal relations from statistical data. They use directed acyclic graphs and associated probability distributions to construct causal models. In a decision problem, a causal model yields a way of calculating an act’s effect. A causal graph and its probability distribution express a dependency hypothesis and yield each act’s causal influence given that hypothesis. They specify the causal probability of a state under supposition of an act. An act’s expected utility is a probability-weighted average of its expected utility according to the dependency hypotheses that candidate causal models represent, as Weirich (2015: 225–236) explains.

A causal model’s directed graph and probability distribution indicate causal relations among event types. As Pearl (2000: 30) and Sprites et al. (2000: 11) explain, a causal model meets the causal Markov condition if and only if with respect to its probability distribution each event type in its directed graph is independent of all the event type’s nondescendants, given its parents. Given a model meeting the condition, knowledge of all an event’s direct causes makes other information statistically irrelevant to the event’s occurrence, except for information about the event and its effects. Knowledge of an event’s direct causes screens off evidence from indirect causes and independent effects of its causes. Given a typical causal model for Newcomb’s problem, knowledge of the common cause of a decision and a prediction screens off the correlation between the decision and the prediction.

Directed acyclic graphs present causal structure clearly, and so clarify in decision theory points that depend on causal structure. For example, Eells (2000) observes that choice is not genuine unless a decision screens off an act’s correlation with states. Joyce (2007: 546) uses a causal graph to depict how this may happen in a Newcomb problem that arises in a Prisoner’s Dilemma with a psychological twin. He shows that the Newcomb problem is a genuine choice despite correlation of acts and states because a decision screens off that correlation. Spohn (2012) constructs for Newcomb’s problem a causal model that distinguishes a decision and its execution and argues that given the model causal decision theory recommends one-boxing. An act in a decision problem may constitute an intervention in the causal model for the decision problem, as Christopher Meek and Clark Glymour (1994) explain. Hitchcock (2016) and Joyce and Gibbard (2016) maintain that treating an act as an intervention enriches causal decision theory.

Timothy Williamson (2007: Chap. 5) studies the epistemology of counterfactual, or subjunctive, conditionals. He points out their role in contingency planning and decision making. According to his account, one learns a subjunctive conditional if one robustly obtains its consequent when imagining its antecedent. Experience disciplines imagination. The experience leading to a judgment that a subjunctive conditional holds may be neither strictly enabling nor strictly evidential so that knowledge of the conditional is neither purely *a priori* nor purely *a posteriori*. Williamson claims that knowledge of subjunctive conditionals is foundational so that decision theory appropriately grounds knowledge of an act’s choiceworthiness in knowledge of such conditionals.

Most texts on decision theory are consistent with causal decision theory. Many do not treat the special cases, such as Newcomb’s problem, that motivate a distinction between causal and evidential decision theory. For example, Leonard Savage (1954) analyzes only decision problems in which options do not affect probabilities of states, as his account of utility makes clear (1954: 73). Causal and evidential decision theories reach the same recommendations in these problems. Causal decision theory is the prevailing form of decision theory among those who distinguish causal and evidential decision theory.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=decision-causal). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/decision-causal/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=decision-causal&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/decision-causal/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- [MIT Course on Decision Theory](http://ocw.mit.edu/courses/linguistics-and-philosophy/24-222-decisions-games-and-rational-choice-spring-2008/), offered by Robert Stalnaker.
- [Decision Theory](http://en.wikipedia.org/wiki/Decision_theory), as of this writing (November 4, 2016), the Wikipedia site has a good overall introduction to decision theory and a list of references.

## Related Entries

causation: counterfactual theories of | causation: the metaphysics of | conditionals | conditionals: counterfactual | decision theory | game theory | prisoner’s dilemma | probability, interpretations of | rational choice, normative: expected utility

### Acknowledgments

I thank Christopher Haugen for bibliographical research and Brad Armendt, David Etlin, William Harper, Xiao Fei Liu, Calum McNamara, Brian Skyrms, Howard Sobel, and an anonymous referee for helpful comments.

[^ahmed-2012]: Ahmed, Arif, 2012, “Push the Button”, *Philosophy of Science*, 79: 386–395.

[^ahmed-2013]: –––, 2013, “Causal Decision Theory: A Counterexample”, *Philosophical Review*, 122: 289–306.

[^ahmed-2014a]: –––, 2014a, *Evidence, Decision and Causality*, Cambridge: Cambridge University Press.

[^ahmed-2014b]: –––, 2014b, “Dicing with Death,” *Analysis* 74: 587–592.

[^ahmed-2018]: ––– (ed.), 2018, *Newcomb’s Problem*, Cambridge: Cambridge University Press.

[^armendt-1986]: Armendt, Brad, 1986, “A Foundation for Causal Decision Theory”, *Topoi*, 5(1): 3–19. doi:10.1007/BF00137825

[^armendt-1988a]: –––, 1988a, “Conditional Preference and Causal Expected Utility”, in William Harper and Brian Skyrms (eds.), *Causation in Decision, Belief Change, and Statistics*, Vol. II, pp. 3–24, Dordrecht: Kluwer.

[^armendt-1988b]: –––, 1988b, “Impartiality and Causal Decision Theory”, in Arthur Fine and Jarrett Leplin (eds.), *PSA: Proceedings of Biennial Meeting of the Philosophy of Science Association 1988* (Volume I), pp. 326–336, East Lansing, MI: Philosophy of Science Association.

[^armendt-2019]: –––, 2019, “Causal Decision Theory and Decision Instability,” *Journal of Philosophy*, 116: 263–277.

[^arntzenius-2008]: Arntzenius, Frank, 2008, “No Regrets, or: Edith Piaf Revamps Decision Theory”, *Erkenntnis*, 68(2): 277–297. doi:10.1007/s10670-007-9084-8

[^bacon-2022]: Bacon, Andrew, 2022, “Actual Value in Decision Theory”, *Analysis*, 82(4): 617–629.

[^bales-2016]: Bales, Adam, 2016, “The Pauper’s Problem: Chance, Foreknowledge and Causal Decision Theory”, *Philosophical Studies*, 173(6): 1497–1516. doi:10.1007/s11098-015-0560-8

[^bales-2018]: –––, 2018, “Richness and Rationality: Causal Decision Theory and the WAR Argument,” *Synthese*, 195: 259–267.

[^bales-2020]: –––, 2020, “Intentions and Instability: A Defense of Causal Decision Theory,” *Philosophical Studies*, 177: 793–804.

[^barnett-2022]: Barnett, David, 2022, “Graded Ratifiability”, *Journal of Philosophy*, 119(2): 57–88.

[^borchert-2024]: Borchert, Rhys and Jack Spencer, 2024, “Newcomb, frustrated”, *Analysis*, 84(3): 449–456 doi:10.1093/analys/anad084

[^cartwright-1979]: Cartwright, Nancy, 1979, “Causal Laws and Effective Strategies”, *Noûs*, 13(4): 419–437. doi:10.2307/2215337

[^easwaran-2021]: Easwaran, Kenny, 2021, “A Classification of Newcomb Problems and Decision Theories,” *Synthese*, 198 (Supplement 27): S6415–S6434.

[^eells-1981]: Eells, Ellery, 1981, “Causality, Utility, and Decision”, *Synthese*, 48(2): 295–329. doi:10.1007/BF01063891

[^eells-1982]: –––, 1982, *Rational Decision and Causality*, Cambridge: Cambridge University Press.

[^eells-1984a]: –––, 1984a, “Newcomb’s Many Solutions”, *Theory and Decision*, 16(1): 59–105. doi:10.1007/BF00141675

[^eells-1984b]: –––, 1984b, “Metatickles and the Dynamics of Deliberation”, *Theory and Decision*, 17(1): 71–95. doi:10.1007/BF00140057

[^eells-2000]: –––, 2000, “Review: *The Foundations of Causal Decision Theory*, by James Joyce”, *British Journal for the Philosophy of Science*, 51(4): 893–900. doi:10.1093/bjps/51.4.893

[^egan-2007]: Egan, Andy, 2007, “Some Counterexamples to Causal Decision Theory”, *Philosophical Review*, 116(1): 93–114. 10.1215/00318108-2006-023

[^elga-2022]: Elga, Adam, 2022, “Confessions of a Causal Decision Theorist”, *Analysis*, 82(2): 203–213.

[^fusco-2023]: Fusco, Melissa, 2023, “Absolution of a Causal Decision Theorist”, *Noûs*, first online 23 June 2023. doi:10.1111/nous.12459

[^gallow-2020]: Gallow, J. Dimitri, 2020, “The Causal Decision Theorist’s Guide to Managing the Improvement News”, *Journal of Philosophy*, 117(3): 117–149.

[^gallow-2024a]: –––, 2024a, “Counterfactual Decision Theory is Causal Decision Theory,” *Pacific Philosophical Quarterly*, 105: 115–156.

[^gallow-2024b]: –––, 2024b, “Decision and Foreknowledge”, *Noûs*, 58: 77–105.

[^gallow-2024c]: –––, 2024c, “The Sure Thing Principle Leads to Instability”, *Philosophical Quarterly*, first online 10 September 2024. doi:10.1093/pq/pqae114

[^gibbard-1978]: Gibbard, Allan and William Harper, 1978 [1981], “Counterfactuals and Two Kinds of Expected Utility”, in Clifford Alan Hooker, James L. Leach, and Edward Francis McClennan (eds.), *Foundations and Applications of Decision Theory* (University of Western Ontario Series in Philosophy of Science, 13a), Dordrecht: D. Reidel, pp. 125–162, doi:10.1007/978-94-009-9789-9_5; reprinted in Harper, Stalnaker, and Pearce 1981: 153–190. doi:10.1007/978-94-009-9117-0_8

[^hájek-2006]: Hájek, Alan and Harris Nover, 2006, “Perplexing Expectations”, *Mind*, 115(459): 703–720. doi:10.1093/mind/fzl703

[^hare-2016]: Hare, Caspar and Brian Hedden, 2016, “Self-Reinforcing and Self-Frustrating Decisions,” *Noûs*, 50: 604–628.

[^harper-1986]: Harper, William, 1986, “Mixed Strategies and Ratifiability in Causal Decision Theory”, *Erkenntnis*, 24(1): 25–36. doi:10.1007/BF00183199

[^harper-1981]: Harper, William, Robert Stalnaker, and Glenn Pearce (eds.), 1981,*Ifs: Conditionals, Belief, Decision, Chance, and Time* (University of Western Ontario Series in Philosophy of Science, 15), Dordrecht: Reidel.

[^hedden-2012]: Hedden, Brian, 2012, “Options and the Subjective *Ought*,” *Philosophical Studies*, 158(2): 343–360. doi:10.1007/s11098-012-9880-0

[^hedden-2023]: –––, 2023, “Counterfactual Decision Theory”, *Mind*, 132: 730–761.

[^hitchcock-1996]: Hitchcock, Christopher Read, 1996, “Causal Decision Theory and Decision-Theoretic Causation”, *Noûs*, 30(4): 508–526. doi:10.2307/2216116

[^hitchcock-2013]: –––, 2013, “What is the ‘Cause’ in Causal Decision Theory?”, *Erkenntnis*, 78: 129–146.

[^hitchcock-2016]: –––, 2016, “Conditioning, Intervening, and Decision”, *Synthese*, 193(4): 1157–1176. doi:10.1007/s11229-015-0710-8

[^horgan-1981]: Horgan, Terry, 1981 [1985], “Counterfactuals and Newcomb’s Problem”, *The Journal of Philosophy*, 78(6): 331–356, doi:10.2307/2026128; reprinted in Richmond Campbell and Lanning Sowden (eds.), 1985, *Paradoxes of Rationality and Cooperation: Prisoner’s Dilemma and Newcomb’s Problem*, Vancouver: University of British Columbia Press, pp. 159–182.

[^horwich-1987]: Horwich, Paul, 1987, *Asymmetries in Time*, Cambridge, MA: MIT Press.

[^huttegger-2023]: Huttegger, Simon, 2023, “Reconciling Evidential and Causal Decision Theory”, *Philosopher’s Imprint*, 23(20). doi:10.3998/phimp.931

[^jeffrey-1981]: Jeffrey, Richard C., 1981, “The Logic of Decision Defended”, *Synthese*, 48(3): 473–492.

[^jeffrey-1965]: –––, [1965] 1983, *The Logic of Decision*, second edition, Chicago: University of Chicago Press. [The 1990 paperback edition includes some revisions.]

[^jeffrey-2004]: –––, 2004, *Subjective Probability: The Real Thing*, Cambridge: Cambridge University Press.

[^joyce-1999]: Joyce, James M., 1999, *The Foundations of Causal Decision Theory*, Cambridge: Cambridge University Press.

[^joyce-2000]: –––, 2000, “Why We Still Need the Logic of Decision”, *Philosophy of Science*, 67: S1–S13. doi:10.1086/392804

[^joyce-2002]: –––, 2002, “Levi on Causal Decision Theory and the Possibility of Predicting One’s Own Actions”, *Philosophical Studies*, 110(1): 69–102. doi:10.1023/A:1019839429878

[^joyce-2007]: –––, 2007, “Are Newcomb Problems Really Decisions?” *Synthese*, 156(3): 537–562. doi:10.1007/s11229-006-9137-6

[^joyce-2012]: –––, 2012, “Regret and Instability in Causal Decision Theory”, *Synthese*, 187(1): 123–145. doi:10.1007/s11229-011-0022-6

[^joyce-2016]: –––, 2016, “Review of *Evidence, Decision and Causality*, by Arif Ahmed”, *Journal of Philosophy*, 113: 224–232.

[^joyce-2018]: –––, 2018, “Deliberation and Stability in Newcomb Problems and Pseudo-Newcomb Problems,” in Arif Ahmed (ed.), *Newcomb’s Problem*, Cambridge: Cambridge University Press, pp. 138–159.

[^joyce-2016-2]: Joyce, James and Allan Gibbard, 2016, “Causal Decision Theory”, in Horacio Arlø-Costa, Vincent F. Hendricks, and Johan van Benthem (eds.), *Readings in Formal Epistemology*, Berlin: Springer, pp. 457–491.

[^kment-2023]: Kment, Boris, 2023, “Decision, Causality, and Predetermination”, *Philosophy and Phenomenological Research*, 107(3): 638–670. doi:10.1111/phpr.12935

[^krantz-1971]: Krantz, David, R., Duncan Luce, Patrick Suppes, and Amos Tversky, 1971, *The Foundations of Measurement* (Volume 1: *Additive and Polynomial Representations*), New York: Academic Press.

[^kusser-1992]: Kusser, Anna and Wolfgang Spohn, 1992, “The Utility of Pleasure is a Pain for Decision Theory”, *Journal of Philosophy*, 89(1): 10–29.

[^lauro-2022]: Lauro, Greg and Simon Huttegger, 2022, “Structural Stability in Causal Decision Theory”, *Erkenntnis*, 87: 603–621.

[^levi-2000]: Levi, Isaac, 2000, “Review Essay on *The Foundations of Causal Decision Theory*, by James Joyce”, *Journal of Philosophy*, 97(7): 387–402. doi:10.2307/2678411

[^levinstein-2020]: Levinstein, Benjamin and Nate Soares, 2020, “Cheating Death in Damascus”, *Journal of Philosophy*, 117: 237–266.

[^lewis-1973]: Lewis, David, 1973, *Counterfactuals*, Cambridge, MA: Harvard University Press.

[^lewis-1976]: –––, 1976, “Probabilities of Conditionals and Conditional Probabilities”, *Philosophical Review*, 85(3): 297–315. doi:10.2307/2184045

[^lewis-1979]: –––, 1979, “Prisoner’s Dilemma is a Newcomb Problem”, *Philosophy and Public Affairs*, 8(3): 235–240.

[^lewis-1981]: –––, 1981, “Causal Decision Theory”, *Australasian Journal of Philosophy*, 59(1): 5–30. doi:10.1080/00048408112340011

[^mcnamara-2023]: McNamara, Calum, 2023, “Causal Decision Theory, Context, and Determinism”, *Philosophy and Phenomenological Research*, 109: 226–260.

[^meek-1994]: Meek, Christopher and Clark Glymour, 1994, “Conditioning and Intervening”, *British Journal for the Philosophy of Science*, 45(4): 1001–1021. doi:10.1093/bjps/45.4.1001

[^nielsen-2024]: Nielsen, Michael, 2024, “Only CDT Values Knowledge”, *Analysis*, 84(1): 67–82.

[^nozick-1969]: Nozick, Robert, 1969, “Newcomb’s Problem and Two Principles of Choice”, in Nicholas Rescher (ed.), *Essays in Honor of Carl G. Hempel*, Dordrecht: Reidel, pp. 114–146.

[^papineau-2001]: Papineau, David, 2001, “Evidentialism Reconsidered”, *Noûs*, 35(2): 239–259.

[^pearl-2000]: Pearl, Judea, 2000, *Causality: Models, Reasoning, and Inference*, Cambridge: Cambridge University Press; second edition, 2009.

[^pollock-2006]: Pollock, John, 2006, *Thinking about Acting: Logical Foundations for Rational Decision Making*, New York: Oxford University Press.

[^pollock-2010]: –––, 2010, “A Resource-Bounded Agent Addresses the Newcomb Problem”, *Synthese*, 176(1): 57–82. doi:10.1007/s11229-009-9484-1

[^price-1986]: Price, Huw, 1986, “Against Causal Decision Theory”, *Synthese*, 67(2): 195–212. doi:10.1007/BF00540068

[^price-2012]: –––, 2012, “Causation, Chance, and the Rational Significance of Supernatural Evidence”, *Philosophical Review*, 121(4): 483–538. doi:10.1215/00318108-1630912

[^richter-1984]: Richter, Reed, 1984, “Rationality Revisited”, *Australasian Journal of Philosophy*, 62(4): 392–403. doi:10.1080/00048408412341601

[^richter-1986]: –––, 1986, “Further Comments on Decision Instability”, *Australasian Journal of Philosophy*, 64(3): 345–349. doi:10.1080/00048408612342571

[^sandgren-2021]: Sandgren, Alexander and Timothy Luke Williamson, 2021, “Determinism, Counterfactuals, and Decision”, *Australasian Journal of Philosophy*, 98(2): 286–302.

[^savage-1954]: Savage, Leonard, 1954, *The Foundations of Statistics*, New York: Wiley.

[^skyrms-1980]: Skyrms, Brian, 1980, *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*, New Haven, CT: Yale University Press.

[^skyrms-1982]: –––, 1982, “Causal Decision Theory”, *Journal of Philosophy*, 79(11): 695–711. doi:10.2307/2026547

[^skyrms-1990]: –––, 1990, *The Dynamics of Rational Deliberation*, Cambridge, MA: Harvard University Press.

[^sobel-1994]: Sobel, Jordan Howard, 1994, *Taking Chances: Essays on Rational Choice*, Cambridge: Cambridge University Press.

[^solomon-2021]: Solomon, Toby Charles Penhallurick, 2021, “Causal Decision Theory’s Predetermination Problem”, *Synthese*, 198: 5623–5654.

[^spencer-2021]: Spencer, Jack, 2021, “An Argument Against Causal Decision Theory”, *Analysis*, 81(1): 52–61.

[^spencer-2023]: –––, 2023, “Can It Be Irrational to Knowingly Choose the Best?”, *Australasian Journal of Philosophy*, 101(1): 128–139.

[^spencer-2019]: Spencer, Jack and Ian Wells, 2019, “Why Take Both Boxes?” *Philosophy and Phenomenological Research*, 99: 27–48.

[^spirtes-2000]: Spirtes, Peter, Clark Glymour, and Richard Scheines, 2000, *Causation, Prediction, and Search*, second edition, Cambridge, MA: MIT Press.

[^spohn-2012]: Spohn, Wolfgang, 2012, “Reversing 30 Years of Discussion: Why Causal Decision Theorists Should One-Box”, *Synthese*, 187(1): 95–122. doi:10.1007/s11229-011-0023-5

[^stalnaker-1968]: Stalnaker, Robert C., 1968, “A Theory of Conditionals”, in *Studies in Logical Theory* (American Philosphical Quarterly Monographs: Volume 2), Oxford: Blackwell, 98–112; reprinted in in Harper, Stalnaker, and Pearce 1981: 41–56. doi:10.1007/978-94-009-9117-0_2

[^stalnaker-1972]: –––, 1972 [1981], “Letter to David Lewis”, May 21; printed in Harper, Stalnaker, and Pearce 1981: 151–152. doi:10.1007/978-94-009-9117-0_7

[^stalnaker-2018]: –––, 2018, “Game Theory and Decision Theory (Causal and Evidential),” in Arif Ahmed (ed.), *Newcomb’s Problem*, Cambridge: Cambridge University Press, pp. 180–200.

[^titelbaum-2022]: Titelbaum, Michael, 2022, *The Fundamentals of Bayesian Epistemology*, Volume 1: *Introducing Credences*, and Volume 2: *Arguments, Challenges, Alternatives*, Oxford: Oxford University Press.

[^wedgwood-2013]: Wedgwood, Ralph, 2013, “Gandalf’s Solution to the Newcomb Problem”, *Synthese*, 190(14): 2643–2675. doi:10.1007/s11229-011-9900-1

[^weirich-1980]: Weirich, Paul, 1980, “Conditional Utility and Its Place in Decision Theory”, *Journal of Philosophy*, 77(11): 702–715.

[^weirich-1985]: –––, 1985, “Decision Instability”, *Australasian Journal of Philosophy*, 63(4): 465–472. doi:10.1080/00048408512342061

[^weirich-2001]: –––, 2001, *Decision Space: Multidimensional Utility Analysis*, Cambridge: Cambridge University Press.

[^weirich-2004]: –––, 2004, *Realistic Decision Theory: Rules for Nonideal Agents in Nonideal Circumstances*, New York: Oxford University Press.

[^weirich-2015]: –––, 2015, *Models of Decision-Making: Simplifying Choices*, Cambridge: Cambridge University Press.

[^weirich-2021]: –––, 2021, *Rational Choice Using Imprecise Probabilities and Utilities*, Cambridge: Cambridge University Press.

[^williamson-2007]: Williamson, Timothy, 2007, *The Philosophy of Philosophy*, Malden, MA: Blackwell.

[^williamson-2021]: Williamson, Timothy Luke, 2021, “Causal Decision Theory Is Safe from Psychopaths”, *Erkenntnis*, 86: 665–685.

[^williamson-2023]: Williamson, Timothy Luke and Alexander Sandgren, 2023, “Law-Abiding Causal Decision Theory”, *British Journal for the Philosophy of Science*, 74(4): 899–920.
