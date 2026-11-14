# Pascal’s Wager
**First published Sat May 2, 1998; substantive revision Sun Sep 11, 2022**

*Hájek, Alan*

“Pascal’s Wager” is the name given to an argument due to Blaise Pascal for believing, or for at least taking steps to believe, in God. The name is somewhat misleading, for in a single section of his *Pensées*, Pascal apparently presents *four* such arguments, each of which might be called a ‘wager’—it is only the third of these that is traditionally referred to as “Pascal’s Wager”. We find in it the extraordinary confluence of several important strands of thought: the justification of theism; probability theory and decision theory, used here for almost the first time in history; pragmatism; voluntarism (the thesis that belief is a matter of the will); and the use of the concept of infinity.

We will begin with some brief stage-setting: some historical background, some of the basics of decision theory, and some of the exegetical problems that the *Pensées* pose. Then we will follow the text to extract three main arguments. The bulk of the literature addresses the third of these arguments, as will the bulk of our discussion here. Some of the more technical and scholarly aspects of our discussion will be relegated to lengthy footnotes, to which there are links for the interested reader. All quotations are from §233 of *Pensées* (1910, Trotter translation), the ‘thought’ whose heading is “*Infinite—nothing*”.

## 1. Background

It is important to contrast Pascal’s argument with various putative ‘proofs’ of the existence of God that had come before it. Anselm’s ontological argument, Aquinas’ ‘five ways’, Descartes’ ontological and cosmological arguments, and so on, purport to prove that God exists. Pascal is apparently unimpressed by such attempted justifications of theism: “Endeavour … to convince yourself, not by increase of proofs of God…” Indeed, he insists that “we do not know if He is …”. Pascal’s project, then, is radically different. He aims to show that *we ought to believe* in God, rather than that *God exists*. And he seeks to provide *prudential* reasons rather than *evidential* reasons for believing in God. To put it simply, we should wager that God exists because it is the *best bet*. Ryan 1994 finds precursors to this line of reasoning in the writings of Plato, Arnobius, Lactantius, and others; we might add Ghazali to his list—see Palacios 1920. Franklin 2018 presents striking parallels to Pascal’s Wager by Sirmond and Chillingworth from 1637 and 1638 respectively, thus predating Pascal by a few years. But what is distinctive is Pascal’s explicitly decision-theoretic formulation of the reasoning. In fact, Hacking 1975 describes the Wager as “the first well-understood contribution to decision theory” (viii). Thus, we should pause briefly to review some of the basics of that theory.

In any decision problem, the way the world is, and what an agent does, together determine an outcome for the agent. We may assign *utilities* to such outcomes, numbers that represent the degree to which the agent values them. It is typical to present these numbers in a decision table, with the columns corresponding to the various relevant states of the world, and the rows corresponding to the various possible actions that the agent can perform.

In *decisions under uncertainty*, nothing more is given—in particular, the agent does not assign subjective probabilities to the states of the world. Still, sometimes rationality dictates a unique decision nonetheless. Consider, for example, a case that will be particularly relevant here. Suppose that you have two possible actions, $A_1$ and $A_2$, and the worst outcome associated with $A_1$ is at least as good as the best outcome associated with $A_2$; suppose also that in at least one state of the world, $A_1$’s outcome is strictly better than $A_2$’s. Let's say in that case that $A_1$ *superdominates* $A_2$. Then rationality seems to require you to perform $A_1$.[^note-1]

**Example**. A magician will toss a coin. You know nothing about the coin—it might be a normal coin, it might be two-headed, it might be two-tailed, and it might be biased to any degree. Suppose that in this state of complete ignorance about the coin, you do not assign any probability whatsoever to its landing heads. Suppose that you can either bet on heads or on tails; it costs nothing to bet, and you will win $1 if you bet correctly. But I will pay you an extra $1 if you bet on heads (I especially like bets on heads). Your possible total pay-offs are given by this decision table:

|   | *Coin lands heads* | *Coin lands tails* |
| --- | --- | --- |
| *Bet on heads* | 2 | 1 |
| *Bet on tails* | 0 | 1 |

Betting on heads superdominates betting on tails. The worst outcome associated with betting on heads (which pays $1)  is at least as good as the best outcome associated with betting on tails (which pays $1); and if the coin lands heads, the outcome associated with betting on heads pays *more* than that associated with tails ($2 > $0). Moreover, it seems clear that you should bet on heads.

In *decisions under risk*, the agent assigns subjective probabilities to the various states of the world. Assume that the states of the world are independent of what the agent does. A figure of merit called the *expected utility*, or the *expectation* of a given action can be calculated by a simple formula: for each state, multiply the utility that the action produces in that state by the state’s probability; then, add these numbers. According to decision theory, rationality requires you to perform the action of maximum expected utility (if there is one).

**Example**. Suppose that the utility of money is linear in number of dollars: you value money at exactly its face value. Suppose now that you know that a *fair* coin will be tossed, and so you assign probability 1/2 to heads and 1/2 to tails. It costs a dollar to play the following game. If the coin lands heads, you will win $3; if it lands tails, you will get nothing.  (Including the initial cost of playing, the total possible payoffs are $1 less than these respective amounts.) Should you play? Here is the decision table:

|   | *Coin lands heads* | *Coin lands tails* |
| --- | --- | --- |
| *Play* | 2 | –1 |
| *Do not play* | 0 | 0 |

The expectation of playing is (2 x 1/2)  + (–1 x 1/2) = 1/2. This exceeds the expectation of not playing—namely 0—so you should play.

And now suppose that the payoff if the coin lands heads is reduced by $1, so that the decision table becomes:

|   | *Coin lands heads* | *Coin lands tails* |
| --- | --- | --- |
| *Play* | 1 | –1 |
| *Do not play* | 0 | 0 |

Then consistent with decision theory, you could either play or not, for either way your expectation would be 0.

Considerations such as these will play a crucial role in Pascal’s arguments. It should be admitted that there are certain exegetical problems in presenting these arguments. Pascal never finished the *Pensées*, but rather left them in the form of notes of various sizes pinned together. Hacking 1972 describes the “Infinite—nothing” as consisting of “two pieces of paper covered on both sides by handwriting going in all directions, full of erasures, corrections, insertions, and afterthoughts” (24).[^note-2] This may explain why certain passages are notoriously difficult to interpret, as we will see. Furthermore, our formulation of the arguments in the parlance of modern Bayesian decision theory might appear somewhat anachronistic. For example, Pascal did not distinguish between what we would now call *objective* and *subjective* probability, although it is clear that it is the latter that is relevant to his arguments. To some extent, “Pascal’s Wager” now has a life of its own, and our presentation of it here is perfectly standard. Still, we will closely follow Pascal’s text, supporting our reading of his arguments as much as possible. (See also Golding 1994 for another detailed analysis of Pascal’s reasoning, broken down into more steps than the presentation here.)[^golding-1994]

There is the further problem of dividing the *Infinite-nothing* into separate arguments. We will locate three arguments that each conclude that rationality requires you to wager for God, although they interleave in the text.[^note-3] Finally, there is some disagreement over just what “wagering for God” involves—is it *believing* in God, or merely *engendering* belief? We will conclude with a discussion of what Pascal meant by this.

## 2. The Argument from Superdominance

Pascal maintains that we are incapable of knowing whether God exists or not, yet we must “wager” one way or the other. Reason cannot settle which way we should incline, but a consideration of the relevant outcomes supposedly can. Here is the first key passage:

> “God is, or He is not.” But to which side shall we incline? Reason can decide nothing here. There is an infinite chaos which separated us. A game is being played at the extremity of this infinite distance where heads or tails will turn up… Which will you choose then? Let us see. Since you must choose, let us see which interests you least. You have two things to lose, the true and the good; and two things to stake, your reason and your will, your knowledge and your happiness; and your nature has two things to shun, error and misery. Your reason is no more shocked in choosing one rather than the other, since you must of necessity choose… But your happiness? Let us weigh the gain and the loss in wagering that God is… If you gain, you gain all; if you lose, you lose nothing. Wager, then, without hesitation that He is.

There are exegetical problems already here, partly because Pascal appears to contradict himself. He speaks of “the true” as something that you can “lose”, and “error” as something “to shun”. Yet he goes on to claim that if you lose the wager that God is, then “you lose nothing”. Surely in that case you “lose the true”, which is just to say that you have made an error, and since this is something “to shun”, it is presumably a cost. Pascal believes, of course, that the existence of God is “the true”—but *that* is not something that he can appeal to in this argument. Moreover, it is not because “you must of necessity choose” that “your reason is no more shocked in choosing one rather than the other”. Rather, by Pascal’s own account, it is because “[r]eason can decide nothing here”. (If it could, then it might well be shocked—namely, if you chose in a way contrary to it.)

Following McClennen 1994, Pascal’s argument seems to be best captured as presenting the following decision table:

|   | *God exists* | *God does not exist* |
| --- | --- | --- |
| *Wager for God* | Gain all | Status quo |
| *Wager against God* | Misery | Status quo |

Wagering for God superdominates wagering against God: the worst outcome associated with wagering for God (status quo) is at least as good as the best outcome associated with wagering against God (status quo); and if God exists, the result of wagering for God is strictly better than the result of wagering against God. (The fact that the result is *much* better does not matter yet.) Pascal draws the conclusion at this point that you should wager for God.

Without any assumption about your probability assignment to God’s existence, the argument is invalid. Rationality does *not* require you to wager for God if you assign probability 0 to God existing, as a strict atheist might. And Pascal does not explicitly rule this possibility out until a later passage, when he assumes that you assign positive probability to God’s existence; yet this argument is presented as if it is self-contained. His claim that “[r]eason can decide nothing here” may suggest that Pascal regards this as a decision under uncertainty, which is to assume that you do *not* assign probability at all to God’s existence. If that is a further premise, then the argument is apparently valid; but that premise contradicts his subsequent assumption that you assign positive probability. See McClennen for a reading of this argument as a decision under uncertainty.

Pascal appears to be aware of a further objection to this argument, for he immediately imagines an opponent replying:

> “That is very fine. Yes, I must wager; but I may perhaps wager too much.”

The thought seems to be that if I wager for God, and God does not exist, then I really do lose something. In fact, Pascal himself speaks of *staking* *something* when one wagers for God, which presumably one loses if God does not exist. (We have already mentioned ‘the true’ as one such thing; Pascal also seems to regard one’s worldly life as another.) In that case, the table is mistaken in presenting the two outcomes under ‘God does not exist’ as if they were the same, and we do not have a case of superdominance after all.

Pascal addresses this at once in his second argument, which we will discuss only briefly, as it can be thought of as just a prelude to the main argument.

## 3. The Argument From Expectation

He continues:

> Let us see. Since there is an equal risk of gain and of loss, if you had only to gain two lives, instead of one, you might still wager. But if there were three lives to gain, you would have to play (since you are under the necessity of playing), and you would be imprudent, when you are forced to play, not to chance your life to gain three at a game where there is an equal risk of loss and gain. But there is an eternity of life and happiness.

Understanding “equal risk” here as “equal probability”, the probability of gain (winning the wager) and of loss (losing the wager) must each be 1/2. His hypothetically speaking of “two lives” and “three lives” may strike one as odd. It is helpful to bear in mind Pascal’s interest in gambling (which after all provided the initial motivation for his study of probability) and to take the gambling model quite seriously here. Indeed, the Wager is permeated with gambling metaphors: “game”, “stake”, “heads or tails”, “cards” and, of course, “wager”. Now, recall our calculation of the expectations of the two dollar and three dollar gambles. Pascal apparently assumes now that utility is linear in number of *lives*, that wagering for God costs “one life”, and then reasons analogously to the way we did in our expectation calculations above! This is, as it were, a warm-up. Since wagering for God is rationally required even in the hypothetical case in which one of the prizes is three lives, then all the more it is rationally required in the actual case, in which one of the prizes is an *eternity* of life (salvation).

So Pascal has now made two striking assumptions:

(1). The probability of God’s existence is 1/2.

(2). Wagering for God brings *infinite* reward if God exists.

Morris 1994 is sympathetic to (1), while Hacking 1972 finds it “a monstrous premiss” (189). One way to defend it is via the classical interpretation of probability, according to which all possibilities are given equal weight. The interpretation seems attractive for various gambling games, which by design involve an evidential symmetry with respect to their outcomes; and Pascal even likens God’s existence to a coin toss, evidentially speaking. However, unless more is said, the interpretation yields implausible, and even contradictory results. (You have a one-in-a-million chance of winning the lottery; but either you win the lottery or you don’t, so each of these possibilities has probability 1/2?!) Pascal’s argument for (1) is presumably that “[r]eason can decide nothing here”. (In the lottery ticket case, reason can decide *something*.) But it is not clear that complete ignorance should be modeled as equiprobability. Morris imagines, rather, an agent who does have evidence for and against the existence of God, but it is equally balanced. In any case, it $is$ clear that there are people in Pascal’s audience who do not assign probability 1/2 to God’s existence. This argument, then, does not speak to them.

However, Pascal realizes that the value of 1/2 actually plays no real role in the argument, thanks to (2). This brings us to the third, and by far the most important, of his arguments.

## 4. The Argument From Generalized Expectations: “Pascal’s Wager”

We continue the quotation.

> But there is an eternity of life and happiness. And this being so, if there were an infinity of chances, of which one only would be for you, you would still be right in wagering one to win two, and you would act stupidly, being obliged to play, by refusing to stake one life against three at a game in which out of an infinity of chances there is one for you, if there were an infinity of an infinitely happy life to gain. But there is here an infinity of an infinitely happy life to gain, a chance of gain against a finite number of chances of loss, and what you stake is finite. It is all divided; wherever the infinite is and there is not an infinity of chances of loss against that of gain, there is no time to hesitate, you must give all…

Again this passage is difficult to understand completely. Pascal’s talk of winning two, or three, lives is a little misleading. By his own decision theoretic lights, you would *not* act stupidly “by refusing to stake one life against three at a game in which out of an infinity of chances there is one for you”—in fact, you should not stake more than an infinitesimal amount in that case (an amount that is bigger than 0, but smaller than every positive real number). The point, rather, is that the prospective prize is “an infinity of an infinitely happy life”. In short, if God exists, then wagering for God results in infinite utility.

What about the utilities for the other possible outcomes? There is some dispute over the utility of “misery”. Hacking interprets this as “damnation” (188), and Pascal does later speak of “hell” as the outcome in this case. Martin 1983 among others assigns this a value of *negative infinity*. Sobel 1996, on the other hand, is one author who takes this value to be finite. There is some textual support for this reading: “The justice of God must be vast like His compassion. Now justice to the outcast is less vast … than mercy towards the elect”. As for the utilities of the outcomes associated with God’s non-existence, Pascal tells us that “what you stake is finite”. This suggests that whatever these values are, they are finite.

Pascal’s guiding insight is that the argument from expectation goes through equally well *whatever* your probability for God’s existence is, provided that it is non-zero and finite (non-infinitesimal)—“a chance of gain against a finite number of chances of loss”.[^note-4]

Pascal’s assumptions about utilities and probabilities are now in place. In another landmark moment in this passage, he next presents a formulation of expected utility theory. When gambling, “every player stakes a certainty to gain an uncertainty, and yet he stakes a finite certainty to gain a finite uncertainty, without transgressing against reason”. How much, then, should a player be prepared to stake without transgressing against reason? Here is Pascal’s answer: “… the uncertainty of the gain is proportioned to the certainty of the stake according to the proportion of the chances of gain and loss …” It takes some work to show that this yields expected utility theory’s answer exactly, but it is work well worth doing for its historical importance and is included in a footnote.[^note-5].)

Let us now gather together all of these points into a single argument. We can think of Pascal’s Wager as having three premises: the first concerns the decision table of rewards, the second concerns the probability that you should give to God’s existence, and the third is a maxim about rational decision-making. Specifically:

1. Either God exists or God does not exist, and you can either wager for God or wager against God. The utilities of the relevant possible outcomes are as follows, where $f_1, f_2$, and $f_3$ are numbers whose values are not specified beyond the requirement that they be finite:

   |   | *God exists* | *God does not exist* |
   | --- | --- | --- |
   | *Wager for God* | $\infty$ | $f_1$ |
   | *Wager against God* | $f_2$ | $f_3$ |
2. Rationality requires the probability that you assign to God existing to be positive (and finite).
3. Rationality requires you to perform the act of maximum expected utility (when there is one).
4. Conclusion 1. Rationality requires you to wager for God.
5. Conclusion 2. You should wager for God.

We have a decision under risk, with probabilities assigned to the ways the world could be, and utilities assigned to the outcomes. In particular, we represent the infinite utility associated with salvation as ‘$\infty$’. We assume that the real line is extended to include the element ‘$\infty$’, and that the basic arithmetical operations are extended as follows:

For all real numbers $r$: $\infty + r = \infty$. For all real numbers $r$: $\infty \times r = \infty$ if $r \gt 0$.

The first conclusion seems to follow from the usual calculations of expected utility (where $p$ is your positive (and finite) probability for God’s existence):

$$ \mathrm{E}(\text{wager for God}) = \infty \times p + f_1 \times(1 - p) = \infty $$

That is, your expected utility of belief in God is infinite—as Pascal puts it, “our proposition is of infinite force”. On the other hand, your expected utility of wagering against God is

$$ \mathrm{E}(\text{wager against God}) = f_2 \times p + f_3 \times(1 - p) $$

This is finite.[^note-6] By premise 3, rationality requires you to perform the act of maximum expected utility. Therefore, rationality requires you to wager for God.

We now survey some of the main objections to the argument.

## 5. Objections to Pascal’s Wager

### 5.1 Premise 1: The Decision Table

Here the objections are manifold. Most of them can be stated quickly, but we will give special attention to what has generally been regarded as the most important of them, ‘the many Gods objection’ (see also the link to footnote 7).

1. Different decision tables for different people. The argument assumes that the same decision table applies to everybody. However, perhaps the relevant rewards are different for different people. Perhaps, for example, there is a predestined infinite reward for the Chosen, whatever they do, and finite utility for the rest, as Mackie 1982 suggests. Or maybe the prospect of salvation appeals more to some people than to others, as Swinburne 1969 has noted.

Even granting that a single $2 \times 2$ table applies to everybody, one might dispute the values that enter into it. This brings us to the next two objections.

2. The utility of salvation could not be infinite. One might argue that the very notion of infinite utility is suspect—see for example Jeffrey 1983 and McClennen 1994.[^note-7] Hence, the objection continues, whatever the utility of salvation might be, it must be finite. Strict finitists, who are suspicious of the notion of infinity in general, will agree—see Dummett 1978 and Wright 1987. Or perhaps the notion of infinite utility makes sense, but an infinite reward could only be finitely appreciated by a human being.

3. There should be more than one infinity in the table. There are also critics of the Wager who, far from objecting to infinite utilities, want to see *more* of them in the table. For example, it might be thought that a forgiving God would bestow infinite utility upon wagerers-for and wagerers-against alike—Rescher 1985 is one author who entertains this possibility. Or it might be thought that, on the contrary, wagering against an existent God results in *negative* infinite utility. (As we have noted, some authors read Pascal himself as saying as much.) Either way, $f_2$ is not really finite at all, but $\infty$ or $-\infty$ as the case may be. And perhaps $f_1$ and $f_3$ could be $\infty$ or $-\infty$. Suppose, for instance, that God does not exist, but that we are reincarnated *ad infinitum*, and that the total utility we receive is an infinite sum that diverges to infinity or to negative infinity.

4. The table should have more rows. Perhaps there is more than one way to wager for God, and the rewards that God bestows vary accordingly. For instance, God might not reward infinitely those who strive to believe in Him only for the very mercenary reasons that Pascal gives, as James 1956 has observed. One could also imagine distinguishing belief based on faith from belief based on evidential reasons, and posit different rewards in each case.

5. The table should have more columns: the many Gods objection. If Pascal is really right that reason can decide nothing here, then it would seem that various other theistic hypotheses are also live options. Pascal presumably had in mind the Catholic conception of God—let us suppose that this is the God who either ‘exists’ or ‘does not exist’. By excluded middle, this is a partition. The objection, then, is that the partition is not sufficiently fine-grained, and the ‘(Catholic) God does not exist’ column really subdivides into various *other* theistic hypotheses. The objection could equally run that Pascal’s argument ‘proves too much’: by parallel reasoning we can ‘show’ that rationality requires believing in various incompatible theistic hypotheses. As Diderot (1746)[^diderot-1746] puts the point: “An Imam could reason just as well this way”.[^note-8]

Since then, the point has been presented again and refined in various ways. Mackie 1982 writes, “the church within which alone salvation is to be found is not necessarily the Church of Rome, but perhaps that of the Anabaptists or the Mormons or the Muslim Sunnis or the worshippers of Kali or of Odin” (203). Cargile 1966 shows just how easy it is to multiply theistic hypotheses: for each real number $x$, consider the God who prefers contemplating $x$ more than any other activity. It seems, then, that such ‘alternative gods’ are a dime a dozen—or $\aleph_1$, for that matter.

In response, some authors argue that in such a competition among various possible deities for one’s belief, some are more probable than others. Although there may be ties among the expected utilities—all infinite—for believing in various ones among them, their respective probabilities can be used as tie-breakers. Schlesinger (1994, 90)[^schlesinger-1994] offers this principle: “In cases where the mathematical expectations are infinite, the criterion for choosing the outcome to bet on is its probability”. (Note that this principle is not found in the Wager itself, although it might be regarded as a friendly addition. Askell 2018 proposes a similar principle.) Are there reasons, then, for assigning higher probability to some Gods than others? Jordan (1994a, 107)[^jordan-1994a] suggests that some outlandish theistic hypotheses may be dismissed for having “no backing of tradition”. Similarly, Schlesinger maintains that Pascal is addressing readers who “have a notion of what genuine religion is about” (88), and we might take that to suggest that Cargile’s imagined Gods, for example, may be correspondingly assigned lower probability than Pascal’s God. Franklin (2018, 41)[^franklin-2018] writes that “[Pascal's] rhetoric is addressed to real agents, namely ”men of the world“ in the Paris of 1660” for whom “the spectrum of religious theories to which they attached grounded subjective non-zero probability consisted of just Catholicism and atheism”. Saka (2018, 190–191)[^saka-2018] replies to various authors who relativise the Wager to Pascal's intended audience that “Pascal's peers knew of Greco-Roman paganism, Judaism, Islam, new-world paganism, and multiple brands of Protestantism; they knew of alleged Satanism … and they knew, from their acquaintance with the foregoing, that still other religions could readily be hypothesized.” But still there is the issue of what probabilities should be assigned to alternative deities. Lycan and Schlesinger 1989 give more theoretical reasons for favoring Pascal’s God over others in one’s probability assignments. They begin by noting the familiar problem in science of underdetermination of theory by evidence. Faced with a multiplicity of theories that all fit the observed data equally well, we favor the simplest such theory. They go on to argue that simplicity considerations similarly favor a conception of God as “absolutely perfect”, “which is theologically unique in that it implies all the other predicates traditionally ascribed to God” (104), and we may add that this conception is Pascal’s. Conceptions of rival Gods, by contrast, leave open various questions about their nature, the answering of which would detract from their simplicity, and thus their probability.

Finally, Bartha 2012 models one’s probability assignments to various theistic hypotheses as evolving over time according to a ‘deliberational dynamics’ somewhat analogous to the dynamics of evolution by natural selection. So understood, Pascal’s Wager is not a single decision, but rather a sequence of decisions in which one’s probabilities update sequentially in proportion to how choiceworthy each God appeared to be in the previous round. (This relies on a sophisticated handling of infinite utilities in terms of utility ratios given in his 2007; see below.) He argues that a given probability assignment is choiceworthy only if it is an equilibrium of this deliberational dynamics. He shows that certain assignments are choiceworthy by this criterion, thus providing a kind of vindication of Pascal against the many Gods objection.

### 5.2 Premise 2: The Probability Assigned to God’s Existence

There are four sorts of problem for this premise. The first two are straightforward; the second two are more technical, and can be found by following the link to footnote 9.

1. Undefined probability for God’s existence. Premise 1 presupposes that you should *have* a probability for God’s existence in the first place. However, perhaps you could rationally *fail* to assign it a probability—your probability that God exists could remain *undefined*. We cannot enter here into the thorny issues concerning the attribution of probabilities to agents. But there is some support for this response even in Pascal’s own text, again at the pivotal claim that “[r]eason can decide nothing here. There is an infinite chaos which separated us. A game is being played at the extremity of this infinite distance where heads or tails will turn up…” The thought could be that any probability assignment is inconsistent with a state of “epistemic nullity” (in Morris’ 1986 phrase)[^morris-1986]: to assign a probability at all—even 1/2—to God’s existence is to feign having evidence that one in fact totally lacks. For unlike a coin that we know to be fair, this metaphorical ‘coin’ is ‘infinitely far’ from us, hence apparently completely unknown to us. Perhaps, then, rationality actually requires us to *refrain* from assigning a probability to God’s existence (in which case at least the Argument from Superdominance would apparently be valid). Or perhaps rationality does not require it, but at least *permits* it. Either way, the Wager would not even get off the ground.

2. Zero probability for God’s existence. Strict atheists may insist on the rationality of a probability assignment of 0, as Oppy 1990 among others points out. For example, they may contend that reason alone *can* settle that God does not exist, perhaps by arguing that the very notion of an omniscient, omnipotent, omnibenevolent being is contradictory. Or a Bayesian might hold that rationality places no constraint on probabilistic judgments beyond coherence (or conformity to the probability calculus). Then as long as the strict atheist assigns probability 1 to God’s non-existence alongside his or her assignment of 0 to God’s existence, no norm of rationality has been violated.

Furthermore, an assignment of $p = 0$ would clearly block the route to Pascal’s conclusion, under the usual assumption that

$$ \infty \times 0 = 0 $$

For then the expectation calculations become:

$$\begin{align*} \mathrm{E}(\text{wager for God}) &= \infty \times 0 + f_1 \times(1 - 0) \\ &= f_1 \\ &\\ \mathrm{E}(\text{wager against God}) &= f_2 \times 0 + f_3 \times(1 - 0) \\ &= f_3 \end{align*}$$

And nothing in the argument implies that $f_1 \gt f_3$. (Indeed, this inequality is questionable, as even Pascal seems to allow.) In short, Pascal’s wager has no pull on strict atheists.[^note-9]

### 5.3 Premise 3: Rationality Requires Maximizing Expected Utility

Finally, one could question Pascal’s decision theoretic assumption that rationality requires one to perform the act of maximum expected utility (when there is one). Now *perhaps* this is an analytic truth, in which case we could grant it to Pascal without further discussion—perhaps it is *constitutive* of rationality to maximize expectation, as some might say. But this premise has met serious objections. The Allais 1953 and Ellsberg 1961 paradoxes, for example, are said to show that maximizing expectation can lead one to perform intuitively sub-optimal actions. So too the St. Petersburg paradox, in which it is supposedly absurd that one should be prepared to pay any finite amount to play a game with infinite expectation. (That paradox is particularly apposite here.)[^note-10]

Various refinements of expected utility theory have been suggested as a result of such problems. For example, we might consider expected *differences* between the pay-offs of options, and prefer one option to another if and only if the expected difference of the former relative to the latter is positive—see Hájek and Nover 2006, Hájek 2006, Colyvan 2008, and Colyvan & Hájek 2016. Or we might consider suitably defined utility *ratios*, and prefer one option to another if and only if the utility ratio of the former relative to the latter is greater than 1—see Bartha 2007. If we either admit refinements of traditional expected utility theory, or are pluralistic about our decision rules, then premise 3 is apparently false as it stands. Nonetheless, the door is opened to some suitable reformulation of it that might serve Pascal’s purposes. Indeed, Bartha argues that his ratio-based reformulation answers some of the most pressing objections to the Wager that turn on its invocation of infinite utility.

Finally, one might distinguish between *practical* rationality and *theoretical* rationality. One could then concede that practical rationality requires you to maximize expected utility, while insisting that theoretical rationality might require something else of you—say, proportioning belief to the amount of evidence available. This objection is especially relevant, since Pascal admits that perhaps you “must renounce reason” in order to follow his advice. But when these two sides of rationality pull in opposite directions, as they apparently can here, it is not obvious that practical rationality should take precedence. (For a discussion of pragmatic, as opposed to theoretical, reasons for belief, see Foley 1994.)[^foley-1994]

### 5.4 Is the Argument Valid?

A number of authors who have been otherwise critical of the Wager have explicitly conceded that the Wager is valid—e.g. Mackie 1982, Rescher 1985, Mougin and Sober 1994, and most emphatically, Hacking 1972. That is, these authors agree with Pascal that wagering for God really is rationally mandated by Pascal’s decision table in tandem with positive probability for God’s existence, and the decision theoretic account of rational action.

However, Duff 1986 and Hájek 2003 argue that the argument is in fact invalid. Their point is that there are strategies besides wagering for God that also have infinite expectation—namely, *mixed* strategies, whereby you do not wager for or against God outright, but rather choose which of these actions to perform on the basis of the outcome of some chance device. Consider the mixed strategy: “Toss a fair coin: heads, you wager for God; tails, you wager against God”. By Pascal’s lights, with probability 1/2 your expectation will be infinite, and with probability 1/2 it will be finite. The expectation of the entire strategy is:

$$ \frac{1}{2} \times \infty + \frac{1}{2} \times [f_2 \times p + f_3 \times(1 - p)] = \infty $$

That is, the ‘coin toss’ strategy has the same expectation as outright wagering for God. But the probability 1/2 was incidental to the result. Any mixed strategy that gives positive and finite probability to wagering for God will likewise have infinite expectation: “wager for God iff a fair die lands 6”, “wager for God iff your lottery ticket wins”, “wager for God iff a meteor quantum tunnels its way through the side of your house”, and so on.

It can be argued that the problem is still worse than this, though, for there is a sense in which *anything* that you do might be regarded as a mixed strategy between wagering for God, and wagering against God, with suitable probability weights given to each. Suppose that you choose to ignore the Wager, and to go and have a hamburger instead. Still, you may well assign positive and finite probability to your winding up wagering for God nonetheless; and this probability multiplied by infinity again gives infinity. So ignoring the Wager and having a hamburger has the same expectation as outright wagering for God. Even worse, suppose that you focus all your energy into *avoiding* belief in God. Still, you may well assign positive and finite probability to your efforts failing, with the result that you wager for God nonetheless. In that case again, your expectation is infinite again. So even if rationality requires you to perform the act of maximum expected utility when there is one, here there isn’t one. Rather, there is a many-way tie for first place, as it were. All hell breaks loose: anything you might do is maximally good by expected utility lights![^note-11]

Monton 2011 defends Pascal’s Wager against this line of objection. He argues that an atheist or agnostic has more than one opportunity to follow a mixed strategy. Returning to the first example of one, suppose that the fair coin lands tails. Monton’s thought is that your expected utility now changes; it is no longer infinite, but rather that of an atheist or agnostic who has no prospect of the infinite reward for wagering for God. You are back to where you started. But since it was rational for you to follow the mixed strategy the first time, it is rational for you to follow it again now—that is, to toss the coin again. And if it lands tails again, it is rational for you to toss the coin again … With probability 1, the coin will land heads eventually, and from that point on you will wager for God. Similar reasoning applies to wagering for God just in case an n-sided die lands 1 (say): with probability 1 the die will eventually land 1, so if you repeatedly base your mixed strategy on the die, with probability 1 you will wind up wagering for God after a finite number of rolls. Robertson 2012 replies that not all such mixed strategies are (probabilistically) guaranteed to lead to your wagering for God in the long run: not ones in which the probability of wagering for God decreases sufficiently fast on successive trials. Think, for example, of rolling a 4-sided die, then a 9-sided die, and in general an $(n+1)^2$-sided die on the $n$ᵗʰ trial …, a strategy for which the probability that you will eventually wager for God is only 1/2, as Robertson shows. However, Easwaran and Monton 2012 counter-reply that with a continuum of times at which the dice can be rolled, the sequence of rolls that Robertson proposes can be completed in an arbitrarily short period of time. In that case, what should you do next? By Monton’s argument, it seems you should roll a die again. Easwaran and Monton prove that if there are uncountably many times at which one implements a mixed strategy with non-zero probability of wagering for God, then with probability 1, one ends up wagering for God at one of these times. (And they assume, as is standard, that once one wagers for God there is no going back.) They concede that imagining uncountably rolls of a die, say, involves an idealization that is surely not physically realizable. But they maintain that you should act in the way that an idealized version of yourself would eventually act, one who *can* realize the rolls as described—that is, wager for God outright.

There is a further twist on the mixed strategies objection. To repeat, the objection’s upshot is that even granting Pascal all his premises, still wagering for God is not rationally required. But we have seen numerous reasons *not* to grant all his premises. Very well then; let’s not. Indeed, let’s suppose that you give *tiny probability p* to them all being true, where $p$ is positive and finite. So you assign probability $p$ to your decision problem being exactly as Pascal claims it to be. But if it is, according to the mixed strategies objection, all hell breaks loose. Yet again, $p$ multiplied by infinity gives infinity. Hence, it seems that each action that gets infinite expected utility according to Pascal similarly gets infinite expected utility according to *you*; but by the previous reasoning, that is anything you might do. The full force of the objection that hit Pascal now hits you too. There are some subtleties that we have elided over; for example, if you also assign positive and finite probability to a source of *negative* infinite utility, then the expected utilities instead become $\infty$ – $\infty$, which is undefined. But that is just another way for all hell to break loose for you: in that case, you cannot evaluate the choiceworthiness of your possible actions at all. Either way, you face decision-theoretic paralysis. We might call this *Pascal’s Revenge*. See Hájek (2015)[^hájek-2015] for more discussion.

Jackson and Rogers (2019), developing points in Jackson (2016)[^jackson-2016], argue that the mixed-strategies objection is a “structural, but not substantive” (61) objection to Pascal's Wager. They provide cases in which it is clearly rational to prefer one infinite good to another. They suggest a reformulation of how prospects of infinite rewards should be compared. (This also provides a response to the many Gods objection.) Hájek (2003 and especially 2018) offers many valid reformulations of the Wager with more nuanced representations of the utility of salvation, such that the lower the probability of wagering for God, the lower the expected utility. See [^note-11] for further discussion.

### 5.5 Moral Objections to Wagering for God

Let us grant Pascal’s first conclusion for the sake of the argument: rationality requires you to wager for God. The second conclusion, that you *should* wager for God, does not obviously follow. All that we have granted is that one norm—the norm of rationality—prescribes wagering for God. For all that has been said, some *other* norm might prescribe wagering against God. And unless we can show that the rationality norm trumps the others, we have not settled what you should do, all things considered.

There are several arguments to the effect that *morality* requires you to wager *against* God. Pascal himself appears to be aware of one such argument. He admits that if you do not believe in God, his recommended course of action “will deaden your acuteness” (This is Trotter’s translation. Pascal’s original French wording is “vous abêtira”, whose literal translation is even more startling: “will make you a beast”.) One way of putting the argument is that wagering for God may require you to corrupt yourself, thus violating a Kantian duty to yourself. Clifford 1877 argues that an individual’s believing something on insufficient evidence harms society by promoting credulity. Penelhum 1971 contends that the putative divine plan is itself immoral, condemning as it does honest non-believers to loss of eternal happiness, when such unbelief is in no way culpable; and that to adopt the relevant belief is to be complicit to this immoral plan. See Quinn 1994 for replies to these arguments. For example, against Penelhum he argues that as long as God treats non-believers justly, there is nothing immoral about him bestowing special favor on believers, more perhaps than they deserve. (Note, however, that Pascal leaves open in the Wager whether the payoff for non-believers $is$ just; indeed, as far as his argument goes, it may be extremely unjust.)

Finally, Voltaire protests that there is something unseemly about the whole Wager: “That article seems a bit indecent and childish; that notion of gambling, of losses and winnings, does not suit the gravity of the subject” (Voltaire 1778 [1961, 123])[^voltaire-1778]. This does not so much support wagering against God, as dismissing all talk of ‘wagerings’ altogether. Schlesinger (1994, 84)[^schlesinger-1994] canvasses a sharpened formulation of this objection: an appeal to greedy, self-interested motivations is incompatible with “the quest for piety” that is essential to religion. He replies that the pleasure of salvation that Pascal’s Wager countenances is “of the most exalted kind”, and that if seeking it counts as greed at all, then it is “the manifestation of a noble greed that is to be acclaimed” (85). Franklin (1998, 2018)[^franklin-1998][^franklin-2018] regards Voltaire as caricaturing Pascal's Wager and missing his key point that “you must wager”. Franklin argues that given that the choice Pascal presents is unavoidable, it should be made on the basis of a rational calculation, and that his conclusion concerns *action*, not the truth of theism.

## 6. A Fourth “Wager”?

We have concluded our discussion of what is traditionally known as “Pascal’s Wager”. But Pascal has one last twist in store for us. In his “End of this address” he writes regarding wagering for God:

> Now, what harm will befall you in taking this side? You will be faithful, humble, grateful, generous, a sincere friend, truthful. Certainly you will not have those poisonous pleasures, glory and luxury; but will you not have others? I will tell you that you will thereby gain in this life, and that, at each step you take on this road, you will see so great certainty of gain, so much nothingness in what you risk, that you will at last recognise that you have wagered for something certain and infinite, for which you have given nothing.

This passage makes two further striking claims regarding wagering for God: you will “gain in this life”, and “you have wagered for something certain”. The decision table can be presented as follows (with the outcomes ranked):

|   | *God exists* | *God does not exist* |
| --- | --- | --- |
| *Wager for God* | Gain all (Best) | Gain in earthly life (Second best) |
| *Wager against God* | Misery (Worst) | Earthly life (Third best) |

This is again a decision under uncertainty (in our technical sense)—it involves no considerations of probability. Indeed, “the wager” dissolves, twice over: utilities alone definitively settle that you should wager for God, and in any case it is not really a gamble at all, since your gain is certain! (That is my understanding of “you have wagered for something certain”; it is not God's existence itself that is “certain”.) The worst outcome associated with wagering for God (gain in earthly life) is *strictly better* than the best outcome associated with wagering against God (earthly life). It follows immediately that you should wager for God. Hájek (2018)[^hájek-2018] calls this an argument from *superduperdominance*. This is a valid argument for wagering for God, even if we allow that God's existence might be impossible.

Pascal has come full circle back to the first wager, and he now goes even beyond it. The solution to *this* decision problem is trivial. The status of this “wager”—the soundness or otherwise of this argument—turns on whether one's prospects are as this decision table portrays them. See Jordan (2006)[^jordan-2006] and (2018, 108–109) for further discusion.

## 7. What Does It Mean to “Wager for God”?

Let us now grant Pascal that, all things considered (rationality and morality included), you should wager for God. What exactly does this involve?

A number of authors read Pascal as arguing that you should *believe* in God—see e.g. Quinn 1994, and Jordan 1994a. But perhaps one cannot simply believe in God at will; and rationality cannot require the impossible. Pascal is well aware of this objection: “[I] am so made that I cannot believe. What, then, would you have me do?”, says his imaginary interlocutor. However, he contends that one can take steps to cultivate such belief:

> You would like to attain faith, and do not know the way; you would like to cure yourself of unbelief, and ask the remedy for it. Learn of those who have been bound like you, and who now stake all their possessions. These are people who know the way which you would follow, and who are cured of an ill of which you would be cured. Follow the way by which they began; by acting as if they believed, taking the holy water, having masses said, etc. …
>
> But to show you that this leads you there, it is this which will lessen the passions, which are your stumbling-blocks.

We find two main pieces of advice to the non-believer here: act like a believer, and suppress those passions that are obstacles to becoming a believer. And these are actions that one *can* perform at will.

Believing in God is presumably one way to wager for God. This passage suggests that even the non-believer can wager for God, by striving to become a believer. Critics may question the psychology of belief formation that Pascal presupposes, pointing out that one could strive to believe (perhaps by following exactly Pascal’s prescription), yet fail. To this, a follower of Pascal might reply that the act of genuine striving already displays a pureness of heart that God would fully reward.

According to Pascal, ‘wagering for God’ and ‘wagering against God’ are contradictories, as there is no avoiding wagering one way or another: “you must wager. It is not optional.” The decision to wager for or against God is one that you make at a time—at $t$, say. But of course Pascal does not think that you would be infinitely rewarded for wagering for God momentarily, then wagering against God thereafter; nor that you would be infinitely rewarded for wagering for God sporadically—only on the last Thursday of each month, for example. What Pascal intends by ‘wagering for God’ is an ongoing action—indeed, one that continues until your death—that involves your adopting a certain set of practices and living the kind of life that fosters belief in God. The decision problem for you at $t$, then, is whether you should embark on this course of action; to fail to do so is to wager against God at $t$.

## 8. The Continuing Influence of Pascal’s Wager

Pascal’s Wager vies with Anselm’s Ontological Argument for being the most famous argument in the philosophy of religion. Indeed, the Wager arguably has greater influence nowadays than any other such argument—not just in the service of Christian apologetics, but also in its impact on various lines of thought associated with infinity, decision theory, probability, epistemology, psychology, and even moral philosophy. It has provided a case study for attempts to develop infinite decision theories. In it, Pascal countenanced the notion of infinitesimal probability long before philosophers such as Lewis 1980 and Skyrms 1980 gave it prominence. It continues to put into sharp relief the question of whether there can be pragmatic reasons for belief, and the putative difference between theoretical and practical rationality. It raises subtle issues about the extent to which one’s beliefs can be a matter of the will, and the ethics of belief.

Reasoning reminiscent of Pascal’s Wager, often with an explicit acknowledgment of it, also informs a number of debates in moral philosophy, both theoretical and applied. Kenny 1985 suggests that nuclear Armageddon has negative infinite utility, and some might say the same for the loss of even a single human life. Stich 1978 criticizes an argument that he attributes to Mazzocchi, that there should be a total ban on recombinant DNA research, since such research could lead to the “Andromeda scenario” of creating a killer strain of bacterial culture against which humans are helpless; the ban, moreover, should be enforced if the “Andromeda scenario has even the smallest possibility of occurring” (191), in Mazzocchi’s words. This is plausibly read, then, as an assignment of negative infinite utility to the Andromeda scenario. More recently, Colyvan, Cox, and Steele 2010 discuss Pascal’s Wager-like problems for certain deontological moral theories, in which violations of duties are assigned negative infinite utility. Colyvan, Justus and Regan 2011 canvas difficulties associated with assigning infinite value to the natural environment. Bartha and DesRoches 2017 respond, with an appeal to relative utility theory. Stone 2007 argues that a version of Pascal’s Wager applies to sustaining patients who are in a persistent vegetative state; see Varelius 2013 for a dissenting view. Pascal’s Wager has even been appealed to in the medical debate over whether antibiotics should be used to prevent a certain kind of inflammation in the heart (Shaw and Conway 2010)[^shaw-2010].

Pascal’s Wager is a watershed in the philosophy of religion. As we have seen, it is also a great deal more besides.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=pascal-wager). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/pascal-wager/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=pascal-wager&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/pascal-wager/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- [Pascal's Wager: A Pragmatic Argument for Belief in God](https://1000wordphilosophy.com/2021/01/04/pascals-wager-a-pragmatic-argument-for-belief-in-god/), by Liz Jackson, at *1000 Word Philosophy*.
- [*Theistic Belief and Religious Uncertainty*](http://www.infidels.org/library/modern/jeffrey_jordan/belief.html) by Jeff Jordan.
- [Pascal’s Wager](http://www.iep.utm.edu/p/pasc-wag.htm), by Paul Saka, in the *Internet Encyclopedia of Philosophy*.
- [Pascal’s Wager](http://www.infidels.org/library/modern/theism/wager.html), maintained by Stephen R. Welch, at infidels.org.

## Related Entries

decision theory | infinity | probability, interpretations of

### Acknowledgments

I thank Bronwyn Finnigan and Liz Jackson for helpful comments.

## Notes（原文脚注）

[^note-1]: Hájek 2012 argues that in fact this is too quick. This article considers a series of increasingly strong senses of “superdominance” (the one considered here is “superdominance+”), and he argues that none of them is strong enough to confer such a requirement. This, in turn, casts doubt on the validity of the first of Pascal’s wagers. However, the details get somewhat intricate, and I have chosen not to get into them in this exposition.

[^note-2]: Those interested in the reconstruction over the years of the text itself should consult Lafuma 1954.

[^note-3]: Our demarcation of the arguments follows that of Hacking 1972, although we will differ on certain points of detail.

[^note-4]: Unfortunately, he squanders this insight when he lapses back to the assumption that the probability is 1/2 shortly thereafter: “And so our proposition is of infinite force, when there is the finite to stake in a game where there are equal risks of gain and of loss, and the infinite to gain.”

[^note-5]: Consider a gamble that pays you $W$ units (for ‘win’) if $X$, and nothing otherwise. We are seeking the fair price $f$, at which you should be indifferent between playing the gamble and not; you should be prepared to pay that much, but no more. Expected utility theory tells us that *the fair price is the gamble’s expected utility*:

$$ f = P(X)W $$

where $P(X)$ is the chance of gain (and so $1 - P(X)$ is the chance of loss).

Let’s derive this from Pascal’s answer, quoted here again:

> … the uncertainty of the gain is proportioned to the certainty of the stake according to the proportion of the chances of gain and loss …

You will pay $f$ with certainty: this is “the certainty of the stake”. It is uncertain whether you win, but if you do your gain is $W - f$: this is “the uncertainty of the gain”. This is proportioned to the certainty of the stake, $f$—that is,

$$ \frac{f}{W-f} $$

according to

$$ \frac{P(X)}{1 - P(X)} $$

That is,

$$ \frac{f}{W-f} = \frac{P(X)}{1 - P(X)} $$

Simple algebra gives

$$ f - fP(X) = P(X)W - fP(X) $$

and hence

$$ f = P(X)W $$

*The fair price is the gamble’s expected utility*!

[^note-6]: In the basic version of decision theory that we have presented, states are assumed to be independent of actions. Evidential decision theory generalizes this. It replaces in its expectation calculation for a given action the unconditional probabilities of states by the conditional probabilities of the states, given the action—see Jeffrey 1983. Now perhaps what you do is not independent of whether God exists. For instance, maybe God helps people wager for Him, so that

$$ {\scriptsize P(\text{God exists} \mid \text{you wager for God}) \gt P(\text{God exists} \mid \text{you wager against God}).} $$

Still, the expected utility calculations are as before, provided the first conditional probability is positive and finite: infinite for wagering for God, finite for wagering against God.

Causal decision theory replaces evidential decision theory’s conditional probabilities with probabilities that capture the degree of causal relevance of an action to each state. There are various versions of causal decision theory—see Lewis 1981. Using some such version would presumably not significantly affect matters here. We would just replace the assumption that your probability is positive and finite with the same assumption about whatever probability is used instead.

[^note-7]: After all, infinite utilities run afoul of the Archimedean, or continuity axiom that is commonly assumed in decision theory:

> If you prefer $A$ to $B$, and prefer $B$ to $C$, then there is a gamble between $A$ and $C$ ($A$ with probability $p$, $C$ with probability $1 - p$, for some real-valued $p$) that you regard as equally desirable as $B$ for sure.

For suppose that salvation, say, has infinite utility for you. You prefer salvation to $1, and prefer $1 to nothing; but there is no such gamble that rewards you with salvation if you win, and nothing if you lose, that you value at $1. Indeed, assuming that the probability of winning remains positive, you prefer the gamble to any finite reward; but if the probability of winning drops to 0, your preference discontinuously switches to the finite reward. The objection, then, is that infinite utilities run afoul of the underpinnings of decision theory (by violating a preference axiom), and thus of the theory itself. Yet that theory is appealed to in Premise 3 of the argument. In short, Premise 1 is in tension with Premise 3.

The issue then becomes whether continuity is a requirement on rational preference. Hájek 1997 argues that it is not, and gives further positive arguments for allowing infinite utilities into decision theory. Sorensen 1994 likewise argues for “infinite decision theory”. For presentations of ‘non-Archimedean’ decision theory, see Skalia 1975 and Pivato 2014. For related work on infinite utilities that is more philosophical, see Cain 1995, Nelson 1991, Ng 1995, Vallentyne 1993, Vallentyne 1995, Vallentyne and Kagan 1997, and van Liedekerke 1995.

[^note-8]: It should be pointed out that the rival Gods must award infinite utility for salvation in order to create a problem—otherwise they will be trumped by the ones that do. (It seems that Kali and Odin thus drop out of consideration, for example.) And to be damaging to the Wager, the alternative hypotheses about how salvation is achieved should be mutually exclusive. If there is some common core to the theistic hypotheses, and it suffices to (strive to) believe that in order to be saved, then there is no problem. For instance, it will not matter that you do not know what God’s favorite real number is, if it turns out that you are saved as long as your belief is adequate in other respects. So it is crucial that salvation hinges on getting the details of the belief right. What, then, should we believe? To settle this question, it seems we get nowhere with Pascal-style practical reasoning.

One response is that we are therefore in a position somewhat like that of Buridan’s ass, unable to settle which course of action is best; and that like the ass we are better off doing something rather than nothing, and in this case that means choosing one of the theistic hypotheses, and hoping we choose the right one. So it might still be rationally required to be a theist. See Jordan 1994a for a version of this “ecumenical” response. There are at least two counter-responses. Firstly, the assumption that there are alternative *Gods* who offer infinite rewards really plays no role in the many-Gods objection. All that matters is that there are sources of infinite reward besides Pascal’s God. These sources could even be inanimate—as it might be, supreme pleasure machines, which offer infinite utility irrespective of one’s beliefs. Secondly, one of the alternative Gods might punish those who wager for him, and reward those who don’t—see Martin’s 1983 “perverse master”.

[^note-9]: Here are the third and fourth problems for Premise 2.

> **3. Infinitesimal probability for God’s existence**:
> One might reply that you can rationally assign infinitesimal probability to God’s existence—see e.g. Oppy 1990, 2018,  Hájek 2003, Bartha 2016, and Wenmackers 2018. The argument might run, for example, that there are infinitely many possible Gods to consider (see our discussion of the many Gods objection), and for some infinite subset of them that includes Pascal’s God, rationality does not favor any one over the rest. Treating them even-handedly then requires assigning infinitesimal probability to each. Or again, a Bayesian might say that you could coherently assign to God’s existence an infinitesimal probability, provided that you also assign a probability to God’s non-existence that falls short of 1 by the same infinitesimal.
>
> It is remarkable that Pascal anticipated the notion of infinitesimal probability, when he says: “if there were an infinity of chances, of which one only would be for you, you would still be right in wagering one [life] … if there were an infinity of an infinitely happy life to gain.” But what he says here is far from obvious. If $\infty$ is a legitimate utility value, then offhand it would seem that $1/\infty$ is a legitimate probability value, and indeed it seems to be the very one that he is considering. However, then we have:
>
> $$ \mathrm{E}(\text{wager for God}) = \infty \times \frac{1}{\infty} + f_1 \times \left(1 - \frac{1}{\infty}\right) \approx 1 + f_1 $$
>
> And it is not clear that this should exceed $f_3$.
>
> All of this treats $\infty$ as if it is a number, subject to ordinary arithmetic operations, such as taking reciprocals, multiplying and adding. Perhaps, for example, $\infty \times (1/\infty)$ is not defined, much as $\infty - \infty$ is not. But that is just another way in which a probability of $(1/\infty)$ might thwart Pascal’s reasoning. We will say more below about infinite numbers for which such arithmetic operations are unproblematic.

> **4. Imprecise (vague) probability for God’s existence**:
> So far we have presupposed that probability assignments are sharp. However, Pascal’s argument is addressed to us—mere humans. And it is apparently a fact about us that our belief states are irremediably imprecise: we cannot assign probability, precise to indefinitely many decimal places, to all propositions. (Such imprecision about probabilities is also called “vagueness”.) Or perhaps even ideally rational agents may, or indeed should, assign imprecise probabilities when their relevant evidence is impoverished, as Pascal thinks that it is here. (See Joyce 2005 for more on this route to imprecise probabilities in general.)[^joyce-2005] Perhaps, then, rationality permits us to assign imprecise probability to God’s existence. If it moreover permits us to assign it probability that is imprecise over an interval that includes 0, then the Wager fails—see Hájek 2000. Indeed, Pascal’s claim that “[reason] can decide nothing here” might be thought to support a probability assignment to God’s existence that is imprecise over the entire $[0, 1]$ interval. However, Rinard 2018 argues that if it is contingent whether God exists, then rationality forbids us from assigning God's existence a probability that is imprecise over an interval that includes 0—the imprecise probability must lie entirely above 0. In that case, Pascal's Wager is just as successful when aimed at rational agents with imprecise probabilities as it is when aimed at rational agents with precise probabilities.

[^note-10]: One could also insist that rational choices must be ratifiable (à la Jeffrey 1983 or Sobel 1996)[^jeffrey-1983][^sobel-1996], and that the act of maximum expectation might not be.

A common rationale for maximizing expectation comes from the various laws of large numbers. Their content is roughly that under suitable circumstances, in the limit, one’s average reward tends to the expectation; and of course one wants to maximize one’s average reward. But the strong law of large numbers assumes that the expectation is finite, and since the expectation of wagering for God is putatively infinite, it clearly cannot be appealed to here. (See e.g. Feller 1971, 236.)[^feller-1971] Perhaps an appeal to the weak law of large numbers, which allows infinite expectation, would suffice. But being a limit theorem, it concerns infinitely long runs of trials. Far from having such a long run here, we have just a single-shot decision problem. This is a decision that you do not get to repeat. This is not so troubling, perhaps, when the variance (a measure of the spread of the distribution of possible outcomes) is small, so that getting an outcome close to the expectation is probable; but what about when the variance is large?

This brings us to yet another problem for Pascal’s third premise. To be sure, the expectation of wagering for God is infinite, if we accept Pascal’s earlier assumptions; but so too is the variance. Expectation does not seem to be such a good guide to choiceworthiness when the variance is large—for what one might end up getting can then be much worse than the expectation—let alone when the variance is infinite. (See Weirich 1984 and Sorensen 1994 for versions of this last point.)[^sorensen-1994][^weirich-1984] Indeed, the lower one makes $f_2$ (or more generally, some highly dispreferred outcome), the less compelling premise 3 seems; and the lower one makes the probability of salvation (or more generally, of some highly desired outcome), the less compelling premise 3 seems. Yet consistent with premise 1, $f_2$ could be (almost) as low as one likes, and consistent with premise 2, the probability of salvation could be (almost) as low as one likes.

[^note-11]: Recall Schlesinger’s (1994, 90)[^schlesinger-1994] tie-breaking principle: “In cases where the mathematical expectations are infinite, the criterion for choosing the outcome to bet on is its probability”. Similarly, Golding (1994, 139–140)[^golding-1994] offers this principle: “given a decision problem where an infinite value is at stake, the option that offers the highest probability of attaining the infinite value is the rational choice, regardless of what other probabilities or finite values are at stake”. This clearly rules out the coin-tossing strategy, the die-tossing strategy, and all the other mixed strategies, since these have lower probabilities of your achieving salvation than outright wagering for God does. Sorensen 1994 objects to Schlesinger’s principle as being ad hoc. One way of putting the objection is that the principle lacks the foundational support that maximizing expected utility has. Bartha 2007, 2016 provides it such support. Be that as it may, Pascal does not appeal to the principle in his argument. As it stands, the argument is apparently invalid.

The problem is that multiplying ∞ by any positive, finite probability again yields ∞. Let us call this property of ∞ *reflexivity under multiplication* (by such a probability). Such reflexivity is at once the strength of the Wager (for then Pascal does not need to say anything more about your probability of God’s existence), and its weakness (for then all the various mixed strategies get maximal expectation also). One could try to fix the weakness, while saving as much one can of the strength. This would involve finding a utility for salvation that is not reflexive under multiplication, yet which is still sufficiently large to swamp your probability, whatever it is, in the expectation calculation.

For instance, if the utility of salvation were enormous, but finite (as it is on Golding’s reading of the Wager, 1994, 130–131)[^golding-1994], then the mixed strategies would yield lower expectation than outright wagering for God. Multiplying that utility by 1/2, 1/6, etc. makes a difference. And the utility could be made enormous enough to offset any actual person’s probability assignment, however small (provided it is positive and finite), so that the expectation of outright belief is maximal for everybody. Or suppose that the utility of salvation were an infinite number that is not reflexive under multiplication. Consider, for example, the infinite ‘hyperreal’ numbers of non-standard analysis (see Robinson 1966, Nelson 1987)[^nelson-1987][^robinson-1966]. Or consider the infinite ‘surreal’ numbers of Conway 1976. Multiplication of such a utility by a positive, finite probability (less than 1) yields another, smaller infinite number. So the expectation of wagering for God again exceeds that of wagering against God, and also that of each mixed strategy, whatever your probability is (provided it is positive and finite). Hájek 2004 suggests the hyperreal and surreal approaches. Herzberg 2011 and Chen and Rubio 2020 develop them, offering valid reformulations with hyperreal and surreal utilities, respectively. See Wenmackers 2018, §2.2 for a summary of hyperreal numbers, and the entry on Infinity for summaries of both kinds of numbers.

These proposals yield valid arguments for wagering for God, where Pascal’s argument was invalid. The trouble is that they do not seem adequately to capture Pascal’s reasoning. He writes: “Unity added to infinity adds nothing to it”. Let us call this property of infinity *reflexivity under addition*. We can see why Pascal would want the utility of salvation to be reflexive under addition: salvation is supposed to be the best possible thing. But if that utility is finite, or hyperreal infinite, or surreal infinite, then adding one to it does make a difference. What is wanted, then, is the seemingly impossible: a representation of the reward of salvation that is reflexive under addition (so that it cannot be bettered), but not reflexive under multiplication by positive, finite probabilities (so that the mixed strategies can be distinguished in expectation from outright belief). Rota (2017, footnote 4) replies that one could regard salvation as the best thing possible for humans as they actually are, even if one could conceive of greater things. And Wenmackers (2018, 304)[^wenmackers-2018] points out that “it is not clear that the existence of larger numbers on the utility scale entails the existence of states or rewards corresponding to them”. But still such modern understandings of infinity, in which it is not reflexive under addition, are at odds with Pascal's own view about it, which explicitly denies this (quoted above). This provides some support for representing the infinite utility as we have, with ∞, to which unity indeed adds nothing: ∞ + 1 = ∞ in the extended reals. See Hájek 2012 and especially 2018 for further reformulations of Pascal’s Wager that appear to be valid. Moreover, one of them captures Pascal’s idea of salvation being the best thing conceivable: the utility of salvation is again ∞, which is reflexive under addition, while the utility of damnation is −∞ (the way that some authors understand the Wager in the first place).

Another approach, apparently faithful to Pascal’s theology, eschews premise 1’s numerical utilities altogether, opting instead for *comparative* judgments of value, and making suitable adjustments elsewhere in the argument. For example, Rota 2016 offers a reformulation that replaces premise 1’s values of $\infty$, $f_1$, $f_2$, $f_3$, with O1, O2, O3, O4, respectively, where O1 is much greater than O3, and O2 is either greater than, equal to, or only a small amount less than O4. Premise 2’s quantification over all positive probabilities is replaced by one over probabilities of $1/2$ or higher. The conclusion essentially is that practical rationality requires agents with such probabilities to wager for God (slightly changing Rota’s wording to conform with ours).

[^allais-1953]: Allais, Maurice, 1953. “Le Comportment de l’Homme Rationnel Devant la Risque: Critique des Postulats et Axiomes de l’École Américaine”, *Econometrica*, 21: 503–546.

[^askell-2019]: Askell, Amanda, 2019. “Prudential Objections to Atheism”, in Graham Oppy (ed.), *A Companion to Atheism and Philosophy*, Oxford: Wiley-Blackwell.

[^bartha-2007]: Bartha, Paul, 2007. “Taking Stock of Infinite Value: Pascal’s Wager and Relative Utilities,” *Synthese*, 154: 5–52.

[^bartha-2012]: –––, 2012. “Many Gods, Many Wagers: Pascal’s Wager Meets the Replicator Dynamics”, in Jake Chandler and Victoria S. Harrison (eds.), *Probability in the Philosophy of Religion*, Oxford: Oxford University Press, 187–206.

[^bartha-2016]: –––, 2016. “Probability and the Philosophy of Religion”, in Alan Hájek and Christopher Hitchcock (eds.), *The Oxford Handbook of Probability and Philosophy*, Oxford: Oxford University Press, 738–771.

[^bartha-2018]: –––, 2018. “Pascal’s Wager and the Dynamics of Rational Deliberation”, in Bartha and Pasternack (eds.) 2018, 236–259.

[^bartha-2016-2]: Bartha, Paul and C. Tyler DesRoches, 2016. “The Relatively Infinite Value of the Environment”, *Australasian Journal of Philosophy*, 95(2): 328–353.

[^bartha-2018-2]: Bartha, Paul and Lawrence Pasternack (eds.), 2018. *Pascal's Wager* (Classic Philosophical Arguments), Cambridge: Cambridge University Press.

[^brown-1984]: Brown, Geoffrey, 1984. “A Defence of Pascal’s Wager”, *Religious Studies*, 20: 465–79.

[^cain-1995]: Cain, James, 1995. “Infinite Utility”, *Australasian Journal of Philosophy*, 73(3): 401–404.

[^cargile-1966]: Cargile, James, 1966. “Pascal’s Wager”, *Philosophy*, 35: 250–7.

[^chen-2020]: Chen, Eddy, and Daniel Rubio, 2020. “Surreal Decisions”, *Philosophy and Phenomenological Research*, 100(1): 54–74.

[^clifford-1877]: Clifford, William K., 1877. “The Ethics of Belief”, in R. Madigan (ed.), *The Ethics of Belief and Other Essays*, Amherst, MA: Prometheus, 70–96.

[^colyvan-2008]: Colyvan, Mark, 2008. “Relative Expectation Theory”, *Journal of Philosophy*, 105(1): 37–54.

[^colyvan-2010]: Colyvan, Mark, Damian Cox, and Katie Steele, 2010. “Modelling the Moral Dimension of Decisions”, *Noûs*, 44(3): 503–529.

[^colyvan-2010-2]: Colyvan, M., J. Justus, and H.M. Regan, 2010. “The Natural Environment is Valuable but Not Infinitely Valuable”, *Conservation Letters*, 3(4): 224–8.

[^colyvan-2016]: Colyvan, Mark and Alan Hájek, 2016. “Making Ado Without Expectations”, *Mind*, 125(499): 829–857.

[^conway-1976]: Conway, John, 1976. *On Numbers and Games*, London: Academic Press.

[^cutland-1988]: Cutland, Nigel (ed.), 1988. *Nonstandard Analysis and its Applications*, London: London Mathematical Society, Student Texts 10.

[^diderot-1746]: Diderot, Denis, 1746. *Pensées Philosophiques*, reprinted Whitefish, MN: Kessinger Publishing, 2009.

[^duff-1986]: Duff, Antony, 1986. “Pascal’s Wager and Infinite Utilities”, *Analysis*, 46: 107–9.

[^dummett-1978]: Dummett, Michael. 1978. “Wang’s Paradox”, in *Truth and Other Enigmas*, Cambridge, MA: Harvard University Press.

[^duncan-2018]: Duncan, Craig, 2018. “The Many Gods Objection to Pascal’s Wager: A Defeat, Then a Resurrection”, in Bartha and Pasternack (eds.) 2018, 148–167.

[^easwaran-2012]: Easwaran, Kenny and Bradley Monton, 2012. “Mixed Strategies, Uncountable Times, and Pascal’s Wager: A Reply to Robertson”, *Analysis*, 72(4): 681–685.

[^ellsberg-1961]: Ellsberg, D., 1961. “Risk, Ambiguity and the Savage Axioms”, *Quarterly Journal of Economics*, 25: 643–669.

[^feller-1971]: Feller, William, 1971. *An Introduction to Probability Theory and its Applications* (Volume II), 2nd edition, London: Wiley.

[^flew-1960]: Flew, Anthony, 1960. “Is Pascal’s Wager the Only Safe Bet?”, *The Rationalist Annual*, 76: 21–25.

[^foley-1994]: Foley, Richard, 1994. “Pragmatic Reasons for Belief”, in Jordan 1994b, 27–44.

[^franklin-1998]: Franklin, James, 1998. “Two Caricatures, I: Pascal’s Wager”, *International Journal for Philosophy of Religion*, 44: 109–14.

[^franklin-2018]: –––, 2018. “Pascal’s Wager and the Origins of Decision Theory: Decision-Making by Real Decision-Makers”, in Bartha and Pasternack (eds.) 2018, 31–46.

[^golding-1994]: Golding, Joshua, 1994. “Pascal’s Wager”, *The Modern Schoolman*, 71(2): 115–143.

[^hacking-1972]: Hacking, Ian, 1972. “The Logic of Pascal’s Wager”, *American Philosophical Quarterly*, 9(2): 186–92; reprinted in Jordan (ed.) 1994b, 21–29. (Page references are to the 1972 original.)

[^hacking-1975]: –––, 1975. *The Emergence of Probability*, Cambridge: Cambridge University Press.

[^hájek-1997]: Hájek, Alan, 1997. “The Illogic of Pascal’s Wager”, *Proceedings of the 10th Logica International Symposium*, T. Childers et al. (eds.), Filosophia, The Institute of Philosophy of the Academy of Sciences of the Czech Republic, 239–249.

[^hájek-2000]: –––, 2000. “Objecting Vaguely to Pascal’s Wager”, *Philosophical Studies*, 98(1): 1–16.

[^hájek-2003]: –––, 2003. “Waging War on Pascal’s Wager”, *Philosophical Review*, 112(1): 27–56.

[^hájek-2006]: –––, 2006. “Some Reminiscences on Richard Jeffrey, and Some Reflections on *The Logic of Decision*”, *Philosophy of Science*, 73(5): 947–958.

[^hájek-2012]: –––, 2012. “Blaise and Bayes”, in Jake Chandler and Victoria S. Harrison (eds.), *Probability in the Philosophy of Religion*, Oxford: Oxford University Press, 167–186.

[^hájek-2015]: –––, 2015. “Pascal’s Ultimate Gamble”, in Alex Byrne, Joshua Cohen, Gideon Rosen, and Seana Shiffrin (eds.), *The Norton Introduction to Philosophy*, New York: Norton.

[^hájek-2018]: –––, 2018. “The (In)validity of Pascal’s Wager”, in Bartha and Pasternack (eds.) 2018, 123–147.

[^hájek-2006-2]: Hájek, Alan and Harris Nover, 2006. “Perplexing Expectations”, *Mind*, 115 (July): 703–720.

[^herzberg-2011]: Herzberg, Frederik, 2011. “Hyperreal Expected Utilities and Pascal’s Wager”, *Logique et Analyse*, 213: 69–108.

[^jackson-2016]: Jackson, Liz, 2016. “Wagering Against Divine Hiddenness”, *The European Journal for Philosophy of Religion*, 8(4): 85–109.

[^jackson-2019]: Jackson, Liz, and Andrew Rogers 2019. “Salvaging Pascal’s Wager”, *Philosophia Christi*, 21(1): 59–84.

[^james-1956]: James, William, 1956. “The Will to Believe”, in *The Will to Believe and Other Essays in Popular Philosophy*, New York: Dover Publications.

[^jeffrey-1983]: Jeffrey, Richard C., 1983. *The Logic of Decision*, 2nd edition, Chicago: University of Chicago Press.

[^jordan-1994a]: Jordan, Jeff, 1994a. “The Many Gods Objection”, in Jordan (ed.) 1994b, 101–113.

[^jordan-2006]: –––, 2006. *Pascal*’*s Wager: Pragmatic Arguments and Belief in God*, Oxford: Oxford University Press.

[^jordan-2018]: –––, 2018. “The Wager and William James”, in Bartha and Pasternack (eds.) 2018, 101–119.

[^jordan-1994b]: Jordan, Jeff (ed.), 1994b. *Gambling on God: Essays on Pascal’s Wager*, Lanham, MD: Rowman & Littlefield.

[^joyce-2005]: Joyce, James M., 2005. “How Probabilities Reflect Evidence”, *Philosophical Perspectives*, 19: 153–179.

[^lewis-1980]: Lewis, David, 1980. “A Subjectivist’s Guide to Objective Chance”, in Richard C. Jeffrey (ed.), *Studies in Inductive Logic and Probability* (Volume II), Berkeley and Los Angeles: University of California Press; reprinted in Lewis 1986.

[^lewis-1986]: –––, 1986, *Philosophical Papers: Volume II*, Oxford: Oxford University Press.

[^lindstrom-1988]: Lindstrom, Tom, 1988. “Invitation to Non-Standard Analysis”, in Cutland (ed.) 1988, 1–139.

[^lycan-1989]: Lycan, William, and George Schlesinger. 1989. “You Bet Your Life”, in Joel Feinberg (ed.), *Reason and Responsibility*, 7th edition, Belmont CA: Wadsworth; also in the 8th, 9th, 10th editions; reprinted in Tom Beauchamp, Joel Feinberg, and James M. Smith (eds.), *Philosophy and the Human Condition*, 2nd edition, Englewood Cliffs, NJ: Prentice Hall, 1989.

[^mackie-1982]: Mackie, J. L., 1982. *The Miracle of Theism*, Oxford: Oxford University Press.

[^martin-1983]: Martin, Michael 1983. “Pascal’s Wager as an Argument for Not Believing in God”, *Religious Studies*, 19: 57–64.

[^martin-1990]: –––, 1990. *Atheism: a Philosophical Justification*, Philadelphia: Temple University Press.

[^mcclennen-1994]: McClennen, Edward, 1994. “Pascal’s Wager and Finite Decision Theory”, in Jordan (ed.) 1994b, 115–137.

[^monton-2011]: Monton, Bradley, 2011. “Mixed Strategies Can’t Evade Pascal’s Wager”, *Analysis*, 71: 642–645.

[^morris-1986]: Morris, Thomas V., 1986. “Pascalian Wagering”, *Canadian Journal of Philosophy*, 16: 437–54.

[^morris-1994]: –––, 1994. “Wagering and the Evidence”, in Jordan (ed.) 1994b, 47–60.

[^mougin-1994]: Mougin, Gregory, and Elliott Sober, 1994. “Betting Against Pascal’s Wager”, *Noûs*, XXVIII: 382–395.

[^nelson-1987]: Nelson, Edward, 1987. *Radically Elementary Probability Theory* (Annals of Mathematics Studies, 117), Princeton: Princeton University Press.

[^nelson-1991]: Nelson, Mark T., 1991. “Utilitarian Eschatology”, *American Philosophical Quarterly*, 28: 339–347.

[^ng-1995]: Ng, Yew-Kwang, 1995. “Infinite Utility and Van Liedekerke’s Impossibility: A Solution”, *Australasian Journal of Philosophy*, 73: 408–411.

[^oppy-1990]: Oppy, Graham, 1990. “On Rescher on Pascal’s Wager”, *International Journal for Philosophy of Religion*, 30: 159–68.

[^oppy-2018]: –––, 2018. “Infinity in Pascal’s Wager”, in Bartha and Pasternack 2018, 260–277.

[^palacios-1920]: Palacios, M. Asin, 1920. *Los Precedentes Musulmanes del ‘Pari’ de Pascal*, Santander: Boletín de la Biblioteca Menéndez Pelayo.

[^pascal-1670]: Pascal, Blaise, 1670, *Pensées*, translated by W. F. Trotter, London: Dent, 1910.

[^penelhum-1971]: Penelhum, Terence, 1971. *Religion and Rationality*, New York: Random House.

[^pivato-2014]: Pivato, Michael, 2014. “Additive Representation of Separable Preferences over Infinite Products”, *Theory and Decision*, 77: 31–83.

[^quinn-1994]: Quinn, Philip L., 1994. “Moral Objections to Pascalian Wagering”, in Jordan (ed.) 1994b, 61–81.

[^rescher-1985]: Rescher, Nicholas, 1985. *Pascal’s Wager*, Notre Dame: South Bend, IN: Notre Dame University Press.

[^rinard-2018]: Rinard, Susanna, 2018. “Pascal’s Wager and Imprecise Probability”, in Bartha and Pasternack (eds.) 2018, 278–292.

[^robinson-1966]: Robinson, Abraham, 1966. *Non-Standard Analysis*, Amsterdam: North Holland.

[^rota-2016]: Rota, Michael, 2016. “A Better Version of Pascal’s Wager”, *American Catholic Philosophical Quarterly*, 90(3): 415–439.

[^rota-2017]: Rota, Michael, 2017. “Pascal’s Wager”, *Philosophy Compass*, 12:e12404.

[^ryan-1945]: Ryan, John, 1945. “The Wager in Pascal and Others”, *New Scholasticism*, 19(3): 233–50; reprinted in Jordan (ed.) 1994b, 11–19.

[^saka-2018]: Saka, Paul, 2018. “Rationality and the Wager”, in Bartha and Pasternack (eds.) 2018, 187–208.

[^schlesinger-1994]: Schlesinger, George, 1994. “A Central Theistic Argument”, in Jordan (ed.) 1994b, 83–99.

[^shaw-2010]: Shaw, David and David Conway, 2010. “Pascal’s Wager, Infective Endocarditis and the ‘No-Lose’ Philosophy in Medicine”, *Heart*, 96(1): 15–18.

[^skalia-1975]: Skalia, H. J., 1975. *Non-Archimedean Utility Theory*, Dordrecht: D. Reidel.

[^skyrms-1980]: Skyrms, Brian, 1980, *Causal Necessity*, New Haven: Yale University Press.

[^sobel-1996]: Sobel, Howard, 1996. “Pascalian Wagers”, *Synthese*, 108: 11–61.

[^sorensen-1994]: Sorensen, Roy, 1994. “Infinite Decision Theory”, in Jordan (ed.) 1994b, 139–159.

[^stone-2007]: Stone, Jim, 2007. “Pascal’s Wager and the Persistent Vegetative State”, *Bioethics*, 21(2): 84–92.

[^swinburne-1969]: Swinburne, R. G., 1969. “The Christian Wager”, *Religious Studies*, 4: 217–28.

[^vallentyne-1993]: Vallentyne, Peter, 1993. “Utilitarianism and Infinite Utility”, *Australasian Journal of Philosophy*, 71: 212–217.

[^vallentyne-1995]: –––, 1995. “Infinite Utility: Anonymity and Person-Centredness”, *Australasian Journal of Philosophy*, 73: 413–420.

[^vallentyne-1997]: Vallentyne, Peter and Shelly Kagan, 1997. “Infinite Value and Finitely Additive Value Theory”, *The Journal of Philosophy*, XCIV(1): 5–27

[^van-1995]: Van Liedekerke, Luc, 1995. “Should Utilitarians Be Cautious About an Infinite Future?”, *Australasian Journal of Philosophy*, 73(3): 405–407.

[^varelius-2013]: Varelius, Jukka, 2013. “Pascal’s Wager and Deciding About the Life-Sustaining Treatment of Patients in Persistent Vegetative State”, *Neuroethics*, 6: 277–285.

[^voltaire-1778]: Voltaire, F. M. A., 1778 [1961]. *Philosophical Letters (Letters Concerning the English Nation)*. Trans. E. Dilworth. Bobbs-Merrill, 17th letter, remark V.

[^weirich-1984]: Weirich, Paul, 1984. “The St. Petersburg Gamble and Risk”, *Theory and Decision*, 17: 193–202.

[^wenmackers-2018]: Wenmackers, Sylvia, 2018. “Infinitesimal Probabilities and Pascal’s Wager”, in Bartha and Pasternack (eds.) 2018, 293–314.

[^wright-1987]: Wright, Crispin, 1987. “Strict Finitism”, in *Realism, Meaning and Truth*, Oxford: Blackwell.
