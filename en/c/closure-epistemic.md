# Epistemic Closure
**First published Wed Nov 4, 2026**

*Alspector-Kelly, Marc*

[*Editor’s Note: The following new entry by Marc Alspector-Kelly replaces the [former entry](https://plato.stanford.edu/archives/fall2026/entries/closure-epistemic/) on this topic by the previous author.*]

A set is *closed* under a relation when members of that set only stand in that relation to other members of that set.[^note-1] The epistemic closure debates concern whether sets of certain beliefs—primarily those that are known, justified, or warranted—are closed under relations that, in one way or another, involve valid deductive implication.

Most—but by no means all—of the discussion has centered on *knowledge closure*. As we’ll characterize it here (see §1.1 below), knowledge closure is the claim that, if you know $P$ and believe $Q$ because it’s deductively implied by $P$, then you also know $Q$.[^note-2] And how could you not? After all, as you’re well aware, $Q$ *has* to be true if $P$ is; and you *know* that $P$ is true. So of course you know that $Q$ is true as well!

The intuition expressed by the “how could you not?” exclamation above is a powerful one, as even closure deniers concede. Some advocates, indeed, view closure as an unassailable epistemological axiom, so that any theory implying closure failure is refuted thereby.[^note-3] Admittedly, a stance as dismissive of closure denial as this is not as widely endorsed nowadays. But the force of the intuition that closure is obviously true has been, and remains, the most influential consideration in its favor, as a result of which closure’s endorsement is widely regarded as the default position.

Consequently, most of the arguments for closure are really arguments against closure denial, ones that purport to show that the supposed gains that accrue to such denial can be achieved without renouncing closure. Closure deniers, meanwhile, argue that such denial is the linchpin for the resolution of a variety of epistemological quandaries, and that their stance avoids untenable commitments that are forced on the closure advocate.

Closure is central to a wide variety of epistemological issues. These include the nature of knowledge and of justification, skepticism, sensitivity and safety, transmission and transmission failure, fallibilism, contextualism and pragmatic encroachment, bootstrapping and circularity, evidence and probability, and the lottery and preface paradoxes, among others.

## 1. Defining Closure and Closure Denial

### 1.1 Defining Closure

According to the simplest version of closure—appearing primarily in studies of epistemic logic—if you know $P$, and $P$ implies $Q$, then you know $Q$. If, however, you have no idea that $P$ does imply $Q$, you wouldn’t be expected to nevertheless inevitably know $Q$, even if you do know $P$.

What might be called the *classic* version says that, if you know both $P$ and that $P$ implies $Q$, then you know $Q$. But it’s consistent with the antecedent that you don’t even believe $Q$. And, even if you do, you might not believe it because it follows from $P$ but instead from, say, wishful thinking.

A recent, now-popular alternative forgoes reference to your knowing that $P$ implies $Q$:

> If you know $P$ and competently deduce $Q$ from $P$, thereby coming to believe $Q$, while retaining your knowledge of $P$ throughout, then you know $Q$ (Hawthorne 2004, 34)[^hawthorne-2004].

Call this the *dynamic* version. The “retaining your knowledge throughout” clause is due to the fact that this is a diachronic principle: your deduction of $Q$ from $P$ takes up an interval of time, at the end of which you come to believe $Q$. Since you could lose your knowledge of $P$ during that interval, the additional clause is required. This contrasts with the classic version, which is synchronic: you know $P$, that $P$ implies $Q$, and $Q$ at the same time. The dynamic version represents the expansion of knowledge by inference, which its advocates view as the core of the intuition behind closure.[^note-4]

There are, however, reasons to prefer a synchronic version. A competent deduction could involve a number of inferential steps or just one. If it involves a number of them, then closure will need to apply to each intermediate step. But then we might as well just limit the principle to one-step inferences. But we shouldn’t treat a one-step competent deduction as requiring that you end up believing $Q$; closure is sometimes appealed to in order to explain retraction phenomena wherein, realizing that $P$ implies $Q$, you retract your belief in $P$ rather than coming to believe $Q$. But then a one-step competent deduction just seems to involve your recognition, at a time, that $P$ implies $Q$ (Alspector-Kelly 2019, 9–10)[^alspector-kelly-2019].

It’s also consistent with the antecedent of the dynamic version that, at some point during the interval taken up by the competent deduction, you lose your recognition that $P$ implies $Q$, and so arrive at your belief in $Q$ without any grip on its inferential relation to $P$. You could, then, believe $Q$ at that point from wishful thinking, and so not know it. So you need to retain throughout, and so into the moment that you believe $Q$, not only your knowledge of $P$, but also your recognition that $Q$ follows from $P$. But then we might as well just characterize closure as concerning your epistemic state at that moment from the outset.[^note-5]

We’ll work with the following synchronic version:

SPC (single-premise closure): necessarily, if you know $P$, and believe $Q$ because it’s implied by $P$, then you know $Q$.[^note-6]

The phrase “because it’s implied by $P$” does not mean merely that you know that $P$ implies $Q$ as per the classic version. You could know this solely by testimony, for example, without any comprehension of the inferential relation.[^note-7] Rather, you understand, or “see”, that $P$ implies $Q$, which understanding somehow grounds your inferential dispositions, and which dispositions are manifested by your believing $Q$. We won’t attempt to finesse such understanding further here.[^note-8]

Your believing $Q$ because it’s implied by $P$ is compatible with belief overdetermination: you could believe $Q$ for other reasons as well. You might, for example, have already believed, before arriving at the department meeting, that the minimum of ten faculty members required for a quorum are present because a colleague, already there, told you as much by phone. Upon arriving and counting twelve faculty members, you then infer that a quorum is indeed present, and believe it for that reason as well.

The “necessarily” operator is needed. If SPC were a material conditional, then it would be true if there just happen not to be cases wherein the antecedent is true and the consequent false, but where that combination is entirely possible. It’s also likely stronger than a subjunctive conditional, which still permits possible scenarios in which the antecedent is true and the consequent false (see note 11). But it’s not logical necessity: the consequent isn’t a logical consequence of the antecedent. So it’s intended as either a metaphysical necessity, reflecting the essential characteristics of knowledge, or a conceptual necessity, reflecting the contours of the concept of knowledge. We won’t try to determine which here.

SPC concerns inferences with only one premise. The multi-premise version runs as follows:

MPC: necessarily, if you know each of $P, R, S,\ldots$, and believe $Q$ because it’s implied by $P, R, S,\ldots$, then you know $Q$.

Much of the discussion below concerns SPC because what’s said of it will apply to MPC as well and, as we’ll see in §4, there are concerns about MPC that, *prima facie* at least, don’t apply to SPC.

### 1.2 Closure Denial

Closure deniers don’t deny that sometimes—indeed, most of the time—when SPC’s antecedent is satisfied, so is its consequent. But they deny that this is an exceptionless generalization: there are, the closure denier insists, cases—possible ones, if not actual—wherein the antecedent is satisfied but the consequent not.

However, there aren’t any closure deniers—at least, no sane ones—in the sense of someone who thinks that *no* closure principle is true. *Some* feature $F$ will systematically distinguish cases wherein SPC succeeds from those wherein it fails. So some version of the following closure principle is true: if you know $P,$ believe $Q$ because it follows from $P,$ *and* $F$ *is realized*, then you know $Q$. Whether one counts as a closure advocate who is finessing the closure principle or as a closure denier, then, is really a matter of degree: how much is packed into $F$, and how far does it take us from the underlying intuition motivating closure’s advocacy?[^note-9]

## 2. Sensitivity, Safety, and Skepticism

The knowledge closure debate was initially triggered, and subsequently dominated, by two closure-denying theories of knowledge: Robert Nozick’s tracking theory and Fred Dretske’s conclusive reasons account.

### 2.1 Nozick

Nozick (1981, ch. 3) initially proposed that, for you to know $P$, if $P$ were false then you wouldn’t believe it. This subjunctive (or counterfactual or modal) conditional has come to be called the “sensitivity” condition.[^note-10] Sensitivity is standardly interpreted in possible-worlds format as requiring that, in the nearest world(s) to the actual world in which $P$ is false, you don’t believe $P$.[^note-11]

The view implies closure failure. But, far from regarding this as a disadvantage, Nozick saw it as the key to countering the Cartesian Skeptical Argument (CSA).[^note-12] Consider the following version of the CSA, where “$H$” is “you have hands” and “$BIV$” is “you’re a handless brain-in-a-vat”—your brain resides in a vat where it is electrically stimulated to have precisely the same sensory experiences that you now have:

**CSA1.**

You don’t know $\neg BIV$.

**CSA2.**

If you don’t know $\neg BIV$, then you don’t know $H$.

**CSA3.**

So you don’t know $H$.

Since an argument with the same structure could be run for almost any claim about the external world by substituting that claim for $H$, the ultimate result is skepticism of the external world.[^note-13]

If you didn’t have hands, this wouldn’t be because you’re a $BIV$—a remote possibility beyond our current technological capacities—but because you lost them in, for example, a car accident. But then you would be well aware that you don’t have hands, and so wouldn’t believe that you do. So $H$ is sensitive. Assuming that you also meet whatever other conditions knowledge requires, if any, then you know $H$. However, if you were a $BIV$ then, since everything would seem to you precisely as it now does, you would still believe that you’re not a $BIV$; $\neg BIV$ is insensitive. So you don’t know $\neg BIV$. So CSA2 is false. CSA2 is the contrapositive of “if you know $H$, then you know $\neg BIV$”, which is an instance of the closure principle that, if you know $P$ (and $P$ implies $Q)$, then you know $Q$. So that principle is false.[^note-14]

Here’s a counterexample to the sensitivity condition that Nozick considered (Nozick 1981, 179)[^nozick-1981]. A grandmother is visited by her grandson, who appears well. She presumably knows, in virtue of his so appearing, that he is well. But if he were ill, other family members would prevent her from seeing him and would tell her that he is well, so as to avoid distressing her. So she would still believe that he is well. So her belief is insensitive. But she seems, nonetheless, to know that he is well.

Nozick’s response was to appeal to methods: if $P$ were false then you would not believe $P$ *by the same method you actually used to arrive at belief in $P$.* Grandma’s actual method was visual inspection of her grandson and, if he were ill and so looked it, she wouldn’t believe he was well. So her belief, although insensitive, is method-sensitive. Knowledge, Nozick suggested, requires, not sensitivity, but method-sensitivity.

### 2.2 Dretske

On Dretske 1971’s conclusive-reasons view, knowledge requires that you wouldn’t have the reason you have for your belief if that belief were false.[^note-15] In other words, Dretske requires, not that your belief is sensitive, but that your reason is. In the grandmother case, if the grandson were sick she wouldn’t have the same reason—that he looks well—that she actually has, and so his looking that way counts as a conclusive reason.[^note-16]

Dretske’s conclusive-reasons account and Nozick’s method-relative account arrive at the same judgments about who knows what in, at least, the cases we will be considering.[^note-17] So we’ll treat them as the same view for our purposes here, calling it the “basis-sensitivity” account, where “basis” is neutral between methods of belief formation and reasons for belief.

In support of his view Dretske offered the now-famous zebra case (Dretske 1970)[^dretske-1970]. You’re at the zoo, looking into the zebra paddock at a zebra. Since it looks like a zebra $(LZ)$, you believe, and presumably know, that it is a zebra $(Z). Z$ is basis-sensitive: if it weren’t a zebra it would be, say, a rhino, and so wouldn’t look like a zebra. Since zebras aren’t mules, $Z$ implies that it’s not a mule disguised to look just like a zebra $(\neg DM)$. You infer $\neg DM$ from $Z. \neg DM$ is not basis-sensitive: $DM$ implies $LZ$, so you’d still believe $Z$ and infer $\neg DM$ from it. It’s obvious, Dretske insists, that you can’t learn $\neg DM$ by so inferring. But you also don’t know $\neg DM$ by its appearance, which it would have if $DM$. Nor have you washed the animal, conducted a DNA test, or done anything else that would indicate $\neg DM$. So you know $Z$ but not $\neg DM$. Closure fails.

Skeptical hypotheses like “I’m a $BIV$”, “I’m dreaming”, and the like are *wholesale*: they are one-size-fits-all hypotheses designed to undermine virtually all external-world knowledge claims. $DM$ is, instead, a *piecemeal* skeptical hypothesis, targeting a specific ordinary knowledge claim, with the implied suggestion that similar piecemeal skeptical hypotheses can be wielded against most if not all other external-world knowledge claims.[^note-18] Skeptical hypotheses of both varieties imply that your grounds for believing the targeted ordinary claims—you seem to have hands, it looks like a zebra—remain (or, at least, seem to do so). Call such ordinary proposition/skeptical hypothesis pairs—where the former implies the denial of the latter—*Dretske cases*.

Dretske (1970)[^dretske-1970] saw the zebra case as an instance of what he called “penetration failure”: your basis, $LZ$, for believing $Z$ doesn’t constitute a basis for $\neg DM$. He thought that such penetration failures provide an argument for closure failure: if the way in which you come to know the premise isn’t inevitably available as a way to come to know the conclusion, then why think that you must end up knowing the conclusion anyway? However, your basis for the conclusion is that it follows from the premise, which inevitably *isn’t* your basis for the premise. Closure doesn’t require that the *way* you know the premise is inevitably a *way* to know the conclusion. It only requires that, if you *do* know the premise, and infer the conclusion from it, then you know the conclusion (Klein 1995, Luper 2006; see also §3.1 below)[^klein-1995][^luper-2006].

Dretske (2013)[^dretske-2013] also claimed that closure fails when $P$ is “lightweight” (an ordinary claim) and $Q$ is “heavyweight” (a much-disputed philosophical claim): you can’t learn “there are physical objects” by inference from “there are cookies in the jar”, “the past is real” from “I finished breakfast”, and so on, despite the fact that the latter implies the former. However, at least some heavyweight claims are basis-sensitive: if there weren’t any physical objects in the jar, then there wouldn’t be any cookies in there, and so it wouldn’t look to you as though there were (Hawthorne 2013)[^hawthorne-2013]. And at least some lightweight propositions are not basis-sensitive. You know that the ice cubes in the glass of lemonade that you left on the patio for four hours in 95° heat have melted. But if they hadn’t—someone put the glass in the fridge without your knowing—you would still remember having put it outside and so believe that they’ve melted (Vogel 1987)[^vogel-1987].

Others have also argued that closure fails for lightweight-to-heavyweight inferences. Yablo (2014, 2017)[^yablo-2014][^yablo-2017], for example, suggests that the heavyweight claims introduce subject-matter—whether there is a physical world, you’re a $BIV$, and so on—that aren’t included in the lightweight claims, and that closure only succeeds from $P$ to $Q$ when $Q$ doesn’t introduce subject-matter not included in $P$. And Schaffer (2004, 2007)[^schaffer-2004][^schaffer-2007] suggests that knowledge ascriptions are implicitly contrastive: you know that those are cookies rather than pickles, but not that they’re cookies rather than cookie-hallucinations. So knowing that they are cookies in the first sense doesn’t require knowing that they’re not hallucinations. Such views introduce restrictions on SPC that, their advocates hope, block lightweight-to-heavyweight inferences without blocking intuitively acceptable inferences.[^note-19]

### 2.3 Red Barn

At first glance, basis-sensitivity helps to resolve a well-known counterexample to sensitivity (Kripke 2011)[^kripke-2011]. In red-barn country there are both real barns and fake barns that look real; but only real ones are painted red. Knowing none of this, you see a red barn, believe that it’s a red barn, and infer that it’s a barn. “It’s a red barn” is sensitive: if it weren’t a red barn it wouldn’t look like one, so you wouldn’t believe that it is. But “it’s a barn” isn’t sensitive: if it weren’t a barn—and so were a non-red fake barn—it would still look like a barn. So you know that it’s a red barn but not that it’s a barn. This isn’t just an example of closure failure on the sensitivity view; it’s an embarrassing one.

However, both “it’s a red barn” and “it’s a barn” are basis-sensitive. If it weren’t a red barn it wouldn’t look red; so you wouldn’t have the same basis for “it’s a red barn”. And you wouldn’t infer that it’s a barn from “it’s a red barn”. So, since inferring from a different premise presumably constitutes a different basis, you wouldn’t have the same basis for “it’s a barn” (Adams, Barker, and Figurelli 2012)[^adams-2012].[^note-20]

But there’s a problem. Red-barn country is a version of fake-barn country (wherein the color is irrelevant), originally offered as a Gettier case: although you’re justified in believing that it’s a barn and it is, you don’t know it (Goldman 1976)[^goldman-1976]. But the fact, unbeknownst to you, that the red ones are real in red barn country doesn’t seem to matter. So you don’t know “it’s a barn” in red-barn country either; and similarly for “it’s a red barn”. Basis sensitivity preserves closure in this case, but in the wrong direction.[^note-21]

### 2.4 Abominable Conjunctions

Another objection lodged against sensitivity accounts, and one that applies to any closure-denying view, is that closure denial seems to license assertions that are intuitively infelicitous (or “abominable”), such as “I know that I have hands but I don’t know that I’m not a (handless) $BIV$”.[^note-22] According to the “knowledge rule” of assertion—that I should only assert what I know—I can assert $H$ but not $\neg BIV$ (Williamson 2000, ch. 11)[^williamson-2000]. But it would be bizarre to complacently assert the former and yet steadfastly refuse to assert the latter (Hawthorne 2013)[^hawthorne-2013]. Our commitment to closure, it is claimed, provides the best explanation for these intuitions.

An alternative explanation is, however, available to the closure denier. I initially take myself to know $H$ and then realize—not that I can’t know $H$ if I don’t know $\neg BIV$, as per closure—but that I can’t know $H$ if I *am* a $BIV$. But I can’t affirm “$\neg BIV$ but I don’t know $\neg BIV$”; that’s infelicitous.[^note-23] So I can only either take myself to know $\neg BIV$, refuse to express an opinion on the matter, or retract my claim to know $H$. But I’m convinced that I don’t know $\neg BIV$, and it would be bizarre to refuse to express an opinion when I am fully aware that I must not be a $BIV$ if, as I claim, I know $H$. So I retract my claim to know $H$.

That doesn’t mean that I don’t know $H$. I can felicitously assert of someone else that they have hands, and so aren’t a $BIV$, but don’t know that they’re not; I just can’t felicitously assert this of myself. I might nevertheless have hands, and so not be a $BIV$, despite not knowing the latter. Correspondingly, I can coherently assert of someone else that they *know* that they have hands, and so aren’t a $BIV$, but don’t know that they’re not. I just can’t felicitously assert this of myself either, and for the same reason. I might nevertheless know that I have hands, and so not be a $BIV$, but not know the latter.

It might be objected that third-person conjunctions are also infelicitous. But, when the relevant cases are carefully described, the infelicity dissipates. My wife and I note that, according to the posted schedule, the train we’re taking leaves in a half-hour. My wife goes to get coffee. While she’s gone it occurs to me that the schedule might have recently changed; I ask the ticket agent, who assures me that it hasn’t. If queried by someone whether my wife knows when the train leaves—they’re worried she won’t get back in time—I would assure them that she does. But I wouldn’t claim that she knows that the schedule hasn’t changed; *I* investigated that, not her. “Although she doesn’t know it, the schedule hasn’t changed; so she knows that the train leaves in a half-hour” doesn’t seem particularly infelicitous. *My* knowing that the schedule hasn’t changed makes all the difference (Alspector-Kelly 2019, §10.7)[^alspector-kelly-2019].

### 2.5 The Spreading Problem

Here are three closure principles that are implied by SPC:

*Addition Closure* (AC): if $S$ knows $P$, and believes $(P \vee Q)$ because it’s implied by $P$, then $S$ knows $(P \vee Q)$.

*Simplification Closure* (SC): if $S$ knows $(P \amp Q)$, and believes $P$ because it’s implied by $(P \amp Q)$, then $S$ knows $P$.

*Equivalence Closure* (EC): If $S$ knows $P, P$ is logically equivalent to $Q$, and $S$ believes $Q$ because it is implied by $P$, then $S$ knows $Q$.

It is widely claimed that renouncing *these* closure principles is *extremely* unintuitive (Hawthorne 2013, Holliday 2015, McGlynn 2014a)[^hawthorne-2013][^holliday-2015][^mcglynn-2014a]. But we can get to $\neg BIV$ from $H$ by a combination of either AC and EC or SC and EC. Here’s the first way:

1. $H$
2. So, $H \lor \neg BIV$ 1, AC
3. So, $\neg BIV$ 2, EC[^note-24]

And here’s the second:

1. $H$
2. So, $H \amp \neg BIV$ 1, EC[^note-25]
3. So, $\neg BIV$ 2, SC

So both Nozick and Dretske must either deny both SC and AC or deny EC on pain of allowing knowledge of $\neg BIV$ by inference from $H$. If a belief is basis-sensitive then so is any belief logically equivalent to it.[^note-26] So both Nozick and Dretske have to, and did, affirm EC. But Nozick, while denying SC, affirmed AC (Nozick 1981, 228)[^nozick-1981], and so is susceptible to the first way above; and Dretske affirmed both AC and SC, and so is susceptible to both ways (Dretske 1970, 1009)[^dretske-1970]. Since both claim that closure fails from $H$ to $\neg BIV$, both accounts are, as written, inconsistent.

Any closure denier who repudiates the inference from $H$ to $\neg BIV$ will also have to either deny both SC and AC or deny EC, despite the fact that they are all very intuitive principles. In response the closure denier might point out that it is also very intuitive that one can’t learn $\neg BIV$ by inference from $H$ by *any* inferential route.[^note-27]

There is a host of problems with basis sensitivity that have little to do with closure; the ice-cube case (§2.2) is one such, but there are many others.[^note-28] And there are a number of more recent sensitivity accounts that either purport to resolve at least some of these problems, or affirm closure, or both (Adams and Clarke 2005, Becker 2012, Baumann 2012, Black 2008, Murphy and Black 2012, DeRose 1995 and 2010, and Roush 2005)[^adams-2012][^adams-2005][^baumann-2012][^becker-2012][^becker-2012-2][^black-2008][^derose-1995][^derose-2010][^murphy-2005][^murphy-2012][^roush-2005]. But by far the most popular approach renounces sensitivity entirely in favor of an alternative subjunctive conditional, safety.

### 2.6 Safety

A belief $P$ is *safe* if, were you to believe $P, P$ would be true.[^note-29] This is the contrapositive of sensitivity. But it’s not equivalent to sensitivity because, unlike material conditionals, the contraposition of a subjunctive conditional isn’t equivalent to the original conditional. The safety conditional is standardly rendered in possible worlds format as requiring that, in nearby worlds in which you believe $P$, $P$ is true.[^note-30]

An oft-advertised advantage of safety over sensitivity is that it preserves closure (Sosa 1999; Luper 1984, 2006; Pritchard 2009a; Williamson 2000)[^luper-1984][^luper-2006][^pritchard-2009a][^sosa-1999][^williamson-2000]. Consider the SCA. There may well be nearby worlds in which $\neg H$; a hand-maiming car accident, after all, can be caused by the briefest ill-timed glance at your phone. But, in such worlds, you would be well aware that $\neg H$. So your belief in $H$ is safe. And your belief in $\neg BIV$ is safe as well, although for a very different reason: our technological capacities being what they currently are, there’s no nearby world in which $BIV$. For that reason alone, there’s no nearby world in which $BIV$ and you believe $\neg BIV$. So that belief is also safe. So, contrary to both the skeptic and the sensitivity theorist—and assuming that you meet whatever other conditions knowledge requires, if any—you do know $\neg BIV$, and closure is preserved.[^note-31]

### 2.7 Vacuous Safety

In the $BIV$ case your belief in $H$ is safe due to the basis that you have for it: in nearby worlds in which it’s false you don’t have the perceptual experiences you actually have that lead you to believe it. However, your belief in $\neg BIV$ is only safe because the nearest world in which it’s false is too distant to matter; it’s vacuously safe. In general, skeptical hypotheses imply that you have (or, at least, seem to have) the same basis for the ordinary proposition that you actually have. So you will believe the ordinary proposition on that basis in the nearest world in which the skeptical hypothesis is true (since you actually do so), and so in which the ordinary proposition is false. If the nearest such world is nearby, then you’ll believe the ordinary proposition in a nearby world in which it’s false; that belief will be unsafe. So, in order for it to be safe, the skeptical hypothesis must be false in nearby worlds. Your belief that it is false is, therefore, vacuously safe.

A vacuously safe belief is safe no matter what your basis for it might be. So, if you believe it because your astrologer says so, your belief will still be safe. But it’s hard to swallow the claim that you know it on that basis.[^note-32] The safety theorist can suggest in response that safety is a necessary but not sufficient condition for knowledge.[^note-33] Since $Q$ in Dretske cases is vacuously safe, however, it doesn’t matter to its safety that you inferred it from $P$. But closure enshrines the idea that your inferring $Q$ from $P$ ensures that you know $Q$. It’s odd that a defense of closure appeals to a condition—safety—that makes that inference superfluous.

### 2.8 Lottery Cases

There are also Dretske cases wherein it’s doubtful that the nearest not-$Q$ world *is* distant. The flagship example is Hawthorne 2004’s lottery case. In light of your meager bank balance, you know that you can’t afford to go on an African safari next week. That implies that you won’t win the lottery this week and so be able to afford such a trip despite that meager balance. But it’s widely agreed that you don’t know that you’ll lose the lottery before the draw, despite its being extremely likely that you will.

That agreement puts pressure on probabilist threshold theories of justification and knowledge according to which you are justified in believing $P$ when $P$ is sufficiently probable on your evidence—as is, presumably, your belief that you will lose the lottery given the astronomical odds in its favor—and know $P$ when your belief, in addition to being sufficiently probable, is also true and not a Gettier case, both of which are satisfied by your belief that you will lose the lottery.

But it doesn’t put the same pressure on modal theories, including safety theory. Although improbable, the nearest world in which you win the lottery is very nearby: just a slightly different arrangement of the balls that drop from the cage will do the trick. So the safety theorist can explain that wide agreement: you don’t know that you’ll lose because you’ll still believe that you’ll lose in the nearby world in which you win.[^note-34]

But, as per §2.7 above, if you win the lottery in a nearby world, then “you can’t afford an African safari” is unsafe. So you don’t know that either, despite intuition to the contrary. The safety theorist is a skeptic to at least this extent: if you have a lottery ticket, then you don’t know any proposition that would be false if you’ll soon have a lot of money.

Perhaps that’s an amount of skepticism we can live with. However, there are any number of analogous “lottery-esque” propositions that make trouble for a much wider swath of ordinary knowledge (Vogel 1990a, Hawthorne 2004)[^hawthorne-2004][^vogel-1990a]. For example: you remember parking your car in parking spot 3b half an hour ago, where it remains. You believe—and, presumably, know—that it’s there now. This implies that it wasn’t stolen in the last half-hour. But you don’t seem to know that it wasn’t. And you know that the Broncos won by reading that in the newspaper. Their winning implies that that report isn’t an erroneous misprint. But you don’t seem to know that it isn’t.

In response, the safety theorist will insist that, for example, if you *do* know that the car is in 3b, the nearest world in which it is stolen will be distant—the thief detests that model, say—and so, by the safety account, you do know that it isn’t stolen. This contrasts with the eponymous lottery case wherein the nearest world in which you win is nearby. Were, however, the nearest world in which it’s stolen also nearby—the thief covets that model—then you indeed don’t know that it’s in 3b (Pritchard 2007a)[^pritchard-2007a].

But our being informed that the nearest $\neg Q$ world is distant in such cases doesn’t seem to shift our intuition that you don’t know $Q$. (Note that *you’re* not so informed.) In the lottery case, suppose that a ball with one of your ticket’s numbers on it—and so one that would have to drop in order for you to win—got stuck in the cage’s wire frame, so that only if the cage were forcefully shaken would that ball drop. However, since the cage is firmly affixed to the floor, that’s not something that would easily happen. The nearest world in which you win is now distant. But, intuitively, you—knowing nothing about the ball’s being stuck—still don’t know that you’ll lose.

Instead, that intuition seems to hinge on the fact that your only available evidence in lottery cases is statistical: your case (ticket, parked car, report) is one among many, you have reason to believe that it is, or is likely to be, false in a small number of those cases (a ticket will win, a car will probably be stolen, some report will likely contain a misprint), and you have no reason to think that your case is exceptional (Vogel 1990). Such evidence seems not to deliver knowledge, however distant the nearest $\neg Q$ world might be. Recall also that, on the safety view, $Q$ propositions in Dretske cases must be vacuously safe if you know the corresponding $P$ proposition. So your basis for believing $Q$ shouldn’t matter.

Since most of our sources of information misfire on occasion, similar cases involving lottery-esque propositions can be constructed for most of our everyday knowledge. The resulting skepticism is very widespread. Such cases are not only a challenge for the safety theorist; they confront any non-skeptical closure-affirming view. Some closure advocates argue that, notwithstanding intuition, you do know that you will lose the lottery, and similarly for other lottery-esque propositions (Cohen 1988, Engel 2021)[^cohen-1988][^engel-2021]. And some, like the safety theorist, claim that there are crucial differences between the eponymous lottery proposition, which you don’t know, and lottery-esque propositions, which, it’s claimed, you do know (Nelkin 2000, Smith 2010, 2016a, and 2021)[^nelkin-2000][^smith-2010][^smith-2016a][^smith-2021].

### 2.9 Closure Failures for Safety

Although the safety account preserves closure in Dretske cases, there are other cases that seem to constitute closure failures on that account. You believe that your Lamborghini is in parking spot 3b because you’re obsessively watching it on a closed-circuit TV monitor, and infer from this that it hasn’t been stolen. Your belief that it’s in spot 3b is safe: since you’re watching it on the monitor, there’s no nearby world in which you believe that it’s in that spot when it isn’t. However, there’s a nearby world in which your friend asks to borrow the car. You agree, and complacently watch him drive off on the monitor. You still believe that your car wasn’t stolen. But it was; your friend is a thief. So your belief that your car is in 3b is safe but your belief that it hasn’t been stolen isn’t. Closure fails.

In response, the safety theorist might claim that knowledge requires, not that your belief is safe, but that your basis is: there’s no nearby world in which you believe it on that basis and it’s false (Luper 1984, Sosa 1999, Pritchard 2007b)[^luper-1984][^pritchard-2007b][^sosa-1999]. They should do this anyway, since Nozick’s grandmother case can be adjusted to count against safety too: just add that, although the grandson is actually well, there’s a nearby world in which he’s sick.[^note-35]

In the car example above, you believe that your car isn’t stolen, not by inferring this from its being in 3b, but because you thought your friend wouldn’t steal it. Any nearby world in which you believe it’s in 3b by seeing it on the monitor and infer that it’s not stolen is a world in which it is in 3b and not stolen; both beliefs are basis-safe.

However, suppose there’s a nearby world in which the monitor fails. You call your friend, who assures you, while joyriding in your car, that it’s still in 3b. You infer from this that it’s not stolen; but it is. Your belief that it’s in 3b is basis-safe, since there’s no nearby world in which the monitor shows that it’s there when it isn’t. But your belief that it’s not stolen, although still inferred from its being in 3b, is not. And closure fails again (Alspector-Kelly 2011; see also Murphy 2005 and Zhao 2022)[^alspector-kelly-2011][^murphy-2005][^zhao-2022].

At this point the safety theorist might claim that, when you infer $Q$ from $P$, your basis for believing $Q$ includes, not only that you inferred it from $P$, but also whatever your basis was for your belief in $P$ (Williamson 2009a, 2009b)[^williamson-2009a][^williamson-2009b]. In the last case above, you actually believe that it’s in 3b because you see it on the monitor, whereas in the nearby world you believe this because your friend says so. So, if that claim is right, your basis for believing that it’s not stolen in the actual world is not what it is in the nearby world after all. That belief is basis-safe, and closure is preserved once again. Whether this is a plausible and viable way to individuate bases is controversial (see Goldstein and Hawthorne 2024)[^goldstein-2024].

## 3. Closure, Transmission, and Sources of Warrant

There is a crucial distinction between closure and *transmission*, one that has come to play an increasingly important role in the closure debate.[^note-36] The consequent of SPC doesn’t say anything about *how* you come by your knowledge of Q; it just says that you know it. So it’s compatible with SPC that, although you infer $Q$ from $P$ that you know, you nevertheless can’t learn $Q$ *because* you so infer; however, in such cases, you inevitably know it by other means. If so, then, although closure is preserved, the following principle is violated:

SPT (Single Premise Transmission): if (i) you know $P$, and believe $Q$ because it’s implied by $P$, then (ii) you know $Q$ *because of (i).*

Your knowing $Q$ because of (i) is compatible with knowledge overdetermination: you could know $Q$ in other ways as well. You might, for example, have already known, before arriving at the department meeting, that the minimum of ten faculty members required for a quorum are present because a colleague, already there, told you as much by phone. Upon arriving and counting twelve faculty members, you then infer that a quorum is indeed present, and know it that way as well.[^note-37]

Call ways of knowing *warrants*.[^note-38] A warrant is not exhausted by the specific feature that prompts your belief, which we might call your basis; it also includes whatever other conditions, both within your mind and in the external environment, must be in place in order for you to know on that basis. For example, it’s not enough that your colleague told you that a quorum is present. After all, she could have been lying. And even if truthful, she could have hallucinated the twelve faculty that she “saw”, which was, coincidentally, the right number. Or you could have misheard her, thinking she said “quorum” when she actually said “forum”. In any of these cases her testimony doesn’t provide you with a way of knowing—a warrant—that a quorum is present. So having a warrant requires, in addition to whatever the basis for your belief might be, also those internal and external conditions that must be in place in order for you to know in response to that basis.

Your already having a warrant for $Q$, then, doesn’t prevent your acquiring a second warrant for $Q$ because you inferred it from $P$. So, for SPT to be true, you must *always* acquire a new warrant for $Q$ whenever its antecedent applies, whether or not you already know $Q$.

Since the antecedents of SPC and SPT are the same, and the consequent of SPT requires what the consequent of SPC requires and more, transmission implies closure, and closure failure implies transmission failure. But closure doesn’t imply transmission, and transmission failure doesn’t imply closure failure.

There are, as a result, two different kinds of closure advocate. The first endorses closure because they endorse transmission. Call them *transmissivists.* Transmissivism hews as closely as possible to the knowledge-expansion intuition behind closure advocacy referenced in §1.1 and, indeed, amounts to a formalization of that intuition. The second concedes that transmission occasionally fails but insists that, whenever it does fail, closure is nevertheless preserved. Call them *preservationists*. We’ll discuss preservationism first.

### 3.1 Preservationism: Warrant for $P$ as Warrant for $Q$

The preservationist needs to explain why transmission fails and also why, whenever it fails, an alternative warrant for $Q$ steps in to save the day. One such explanation is that your warrant for $P$ always also suffices as a warrant for $Q$ whenever $P$ implies $Q$. Another is that, when transmission fails, it does so because you can only have the warrant you have for $P$ if you are already warranted in believing $Q$.

On the first explanation, although you can’t acquire a warrant for $\neg DM$ by inference from $Z$, for example, $LZ$—your basis for $Z$—suffices on its own to warrant $\neg DM$. Probabilistic considerations encourage this idea. Since $Z$ implies $\neg DM$, the probability axioms imply that $p(\neg DM\mid LZ) \ge p(Z\mid LZ)$. On probabilistic threshold conceptions of knowledge, if $LZ$ suffices for knowing $Z$ then it also suffices for knowing $\neg DM$. So you know $\neg DM$ as well.

However, since $DM$ implies $LZ, p(\neg DM\mid LZ) \lt p(\neg DM)$: $LZ$ *lowers*, rather than raises, $\neg DM$’s initial probability.[^note-39] On a popular view, evidence only counts as such if it raises the probability of the hypothesis it supports. So, on that view, $LZ$ counts *against*, rather than for, $\neg DM$ (White 2006)[^white-2006].[^note-40] More generally, $LZ$ presumably doesn’t count *against* $DM$ when $DM$ implies, and so predicts, $LZ$. But $LZ$ can only be evidence *for* $\neg DM$ if it’s evidence *against* $DM$. So it’s not evidence for $\neg DM$.

It remains true that, since $Z$ implies $\neg DM, p(\neg DM\mid LZ) \ge p(Z\mid LZ)$. Since $p(\neg DM\mid LZ) \lt p(\neg DM), p(\neg DM) \gt p(Z\mid LZ)$: the prior probability of $\neg DM$ is higher than the probability of $Z$ given $LZ$. So, if $LZ$ confers a sufficiently high probability for knowledge on $Z$, then $\neg DM$ must already be sufficiently probable in light, presumably, of background evidence $(BE)$.[^note-41] Such evidence might, say, indicate that reputable zoos are unlikely to disguise their animals.[^note-42] So transmission fails: you don’t learn $\neg DM$ by inference from $Z$, but from $BE$. But closure is still preserved (Klein 1995)[^klein-1995].

However, since $p(Q) \ge p(P)$ whenever $P$ implies $Q$, your inferring $Q$ from $P$ is, on this approach, not only irrelevant in Dretske cases, but in *all* cases. Even if, unlike Dretske cases, your evidence $E$ for $P$ raises $Q$’s antecedent probability provided by $BE$ above the threshold required for knowledge, the warrant you have for $Q$ is still provided by the combined evidence $(E \amp BE)$. And you have that warrant as soon as you acquire $E$, and so before you infer $Q$ from $P$. That inference delivers no more evidence than you already have.

But transmission requires that you acquire a new warrant *because you infer* $Q$ *from* $P$. So transmission fails in every case. But transmission was only supposed to fail in Dretske cases (Alspector-Kelly 2019, §5.5)[^alspector-kelly-2019]. More generally, if your warrant for $P$ inevitably suffices as a warrant for $Q$ whenever $P$ implies $Q$, then this counts against, rather than in favor of, transmission: it implies that transmission always fails or, at least, that it is aways superfluous (see Moretti and Piazza 2023’s “indirectness template” for transmission failure)[^moretti-2023][^moretti-2023-2].[^note-43]^{,} [^note-44]

### 3.2 Preservationism: Frontloading

The second explanation for why you inevitably end up knowing $Q$ when transmission fails is that, in Dretske cases at least, you need to *already* know $Q$ in order to learn $P$, given the way that you learned $P$. In order to learn $Z$ on the basis of $LZ$, for example, you need to know $\neg DM$. Call this *frontloading.*[^note-45] One line of reasoning for this is that, without knowing $\neg DM$, all you’ll be in a position to learn from $LZ$ is the disjunction “$Z$ or $DM$”, since both predict $LZ$.[^note-46]

Another such line is that the inference from $Z$ to $\neg DM$ is viciously circular. That inference only delivers knowledge of $\neg DM$ if you know $Z$. But a condition of your knowing $Z$ on the basis of $LZ$ is that the animal isn’t disguised to look like a zebra and, so, isn’t a mule disguised to look that way: precisely $\neg DM$. So, if you initially don’t know $\neg DM$, then you don’t know that $LZ$ warrants $Z$, and so can’t appeal to $Z$ in support of $\neg DM$.[^note-47]

On either reasoning, the story goes, transmission fails: you can’t acquire a new warrant for the conclusion when you needed one already in order to learn the premise.[^note-48]

This last step—if frontloading is required then transmission fails—is virtually universally assumed. But it’s not clear why. True, you can’t acquire your *first* warrant by the inference from $Z$ to $\neg DM$, since the latter must be already warranted. But recall that you can have multiple warrants for the same proposition. Of course, if your *only* putative warrant for $\neg DM$ is by inference from $Z$, then transmission clearly fails: you need that warrant to start with, but won’t get it until you’ve finished. But so long as you start out with a prior warrant for $\neg DM$ that doesn’t depend on this inference, it’s not obvious why the inference can’t deliver another one (White 2006, Silins 2005, and Alspector-Kelly 2019; for possible examples of cases where frontloading is required but transmission succeeds, see the latter, §6.7.2)[^alspector-kelly-2019][^silins-2005][^white-2006].

It’s also widely assumed that, if frontloading is not required, then transmission succeeds. But there are other accounts of transmission failure that don’t require antecedent knowledge of $Q$, and so that are compatible with closure denial.

For example: $DM$ implies $LZ$. So your method for evaluating $\neg DM$—namely, determining whether $\neg DM$ by inference from what you take yourself to learn when you look in the paddock—will *inevitably* deliver $\neg DM$ whenever $DM$. You can, in fact, recognize this before you look in the paddock: knowing what you’ll do if $LZ$, and knowing that $DM$ implies $LZ$, you know that you’ll arrive at $\neg DM$ if $DM$. Moreover, if $LZ$ is false, you’ll *still* arrive at $\neg DM$, since $\neg LZ$ implies $\neg DM$. So you can know before you look that, no matter what you see, and no matter what’s there, your method will deliver $\neg DM$. It’s very plausible that no such method can deliver a warrant for $\neg DM$. But this explanation of transmission failure, while compatible with your knowing $Z$ on $LZ$, doesn’t require that you initially know $\neg DM$, and so is compatible with closure failure (White 2006 and Alspector-Kelly 2019, ch. 4)[^alspector-kelly-2019][^white-2006].[^note-49]

Since both lines of reasoning for frontloading appear to apply to any skeptical hypothesis, front-loading requires prior knowledge of the falsehood of every such hypothesis, both wholesale and piecemeal. Since knowledge is widely taken to require belief and proper basing, you would also have to believe that they are false on appropriate bases.[^note-50] But some will likely mobilize concepts—hitherto undreamt-of animal-disguising technology, for example—that you don’t even understand.

The frontloader might suggest that you don’t actually need to know the denial of skeptical hypotheses; you only need a warrant for them. But then frontloading won’t preserve SPC. SPC’s antecedent is compatible with your only believing $\neg DM$, for example, because it’s implied by $Z$. But, we’re assuming, you don’t acquire a warrant that way. So, although you do have a prior warrant for $\neg DM$, you don’t believe $\neg DM$ on the basis of that warrant, which is the only one you have. So you don’t know $\neg DM$; SPC fails (Silins 2005)[^silins-2005].

The frontloader can, however, endorse this alternative version of closure:

SPWC: if (i) you know $P$, and believe $Q$ because it’s implied by $P$, then either (ii) you know $Q$ because of (i) or (iii) you have a different warrant for $Q$.[^note-51]

But frontloading may still be too demanding. Note that the arguments for frontloading wouldn’t apply if $LZ$ implied $Z$. But, since $LZ$ is a fallible basis for $Z$—$LZ \amp \neg Z$ is possible, as in $DM$—you need an antecedent warrant for $\neg DM$. The basis, $B_2$, that delivers that warrant is itself either fallible or infallible. If the former, you also need a prior warrant for $\neg(B_2 \amp DM)$. The basis for that warrant, $B_3$, is also either fallible or not. If the former, then you also need a warrant for $\neg(B_3 \amp (B_2 \amp DM))$. And if that basis, $B_4$, is fallible…. This sequence can only terminate in infallible bases. So our beliefs are only warranted if they have infallible bases. But, arguably, the bases for almost all of our beliefs are fallible. Skepticism threatens (Alspector-Kelly 2019, §§6.4–6.6)[^alspector-kelly-2019].

### 3.3 Sources of Warrant

If frontloading is required, the Cartesian skeptical argument takes on a different cast. The second premise is “if you don’t know $\neg BIV$ then you don’t know $H$”. In §2.1 this was understood to derive from closure. But now this means “if you don’t *already* know $\neg BIV$ then you don’t know $H$”. One might indeed wonder whether the force of the argument comes from an intuition, not that ordinary knowledge would implausibly put you in a position to learn that the skeptical hypothesis is false, but instead that we need to know the denials of skeptical hypotheses in order to acquire ordinary knowledge in the first place.

To avoid this version of the skeptical argument, the frontloader needs sources of warrant against every skeptical hypothesis whose denial is implied by the mundane knowledge claims that they want to endorse. There are two possible sources.[^note-52] First, background information might provide such a warrant. Second, you might have a default warrant, or “entitlement”.

#### 3.3.1 Warrant by Background Information

One might claim that background information—we don’t yet have the technology to envat a brain, for example—provides you with a warrant for believing $\neg BIV$, as well as the denials of other wholesale skeptical hypotheses (Leite 2015, 207)[^leite-2015]. An objection is that, if you’re a $BIV$, you don’t just seem to have hands; your total experience, and so what you take to be your background information, remains in place. So if you’re in no position to infer $\neg BIV$ from $H$, you’re in no more a position to infer it from putative background information.

But the fact that it wouldn’t be information if you were a $BIV$ doesn’t imply that it isn’t information if you’re not. On certain externalist views of evidence, your evidence in the “good” $\neg BIV$ case is much richer than it is in the “bad” $BIV$ case, and the former may well provide you with the wherewithal to know $\neg BIV$.[^note-53] However, that evidence will also certainly include $H$. So you don’t need a warrant for $\neg BIV$ in order to acquire your warrant for $H$ after all; the frontloading claim is false. And that seems to allow transmission from $H$ to $\neg BIV$. Closure-preserving externalist views of evidence sit more comfortably with transmissivism than with frontloading (see §3.4 below).[^note-54]

The situation is quite different with respect to piecemeal skeptical hypotheses. $DM$, for example, doesn’t incorporate whatever background information that you might have against it (to the effect that reputable zoos aren’t likely to deceive the public, say). However, it remains intuitive, not just that you can’t learn that it’s not a disguised mule by inference from “it’s a zebra”—which intuition the frontloader endorses—but also that, given your circumstances, you don’t know it at all.

That intuition is particularly strong with respect to lottery propositions. Perhaps background evidence suffices to warrant “most people lose the lottery”, “cars aren’t often stolen”, “this report is likely not a misprint”, and the like. But you need a warrant for the specific claim that this particular ticket, car, or report isn’t one of the exceptions. And it’s difficult to see how merely statistical information—the only kind you seem to have in these cases—suffices for that purpose when you know that such exceptions exist and nothing that you’re aware of distinguishes your case from any other (Sharon and Spectre 2017a, 24–27)[^sharon-2017a].

So the frontloader needs to explain these intuitions. One popular approach is that of the contextualist.

The standards for knowledge, according to the contextualist, can vary from one context of attribution to another. In ordinary contexts, wherein the standards are relatively low, you count as knowing both the ordinary claim $P$ and the denial of the skeptical hypothesis $Q$. But when the person who attributes knowledge (who may or may not be you) contemplates $Q$, doing so typically raises the standards applicable in their context to the point where you count as knowing neither $P$ nor $Q$. So, when the attributor intuits that you don’t know $Q$, they’re right; but that’s only because they’re contemplating it. In ordinary contexts, when they’re not contemplating $Q$, you do know it. In neither context is closure false. The contextualist applies this explanation of our intuitions, not just to lottery propositions, but to all piecemeal and wholesale skeptical hypotheses (Cohen 1988, DeRose 2009, Lewis 1996; see also the entry on epistemic contextualism)[^cohen-1988][^derose-2009][^lewis-1996].

Contextualism does not, however, require that closure is true. Heller 1999 claims that, although you know neither $P$ nor $Q$ in high-standards contexts, you know $P$ but *not* $Q$ in ordinary, low-standards contexts, so that closure fails in the latter contexts. The closure-affirming contextualist needs to explain both why we need to attribute knowledge of the denials of skeptical hypotheses in ordinary cases and where that knowledge comes from.

With respect to the latter question, the contextualist isn’t likely to claim that knowledge of $Q$ in ordinary contexts is acquired by transmission since it’s wildly unlikely that people in ordinary (or any other) contexts believe $Q$ in Dretske cases because they’ve inferred it from $P$. So the closure-preserving contextualist is presumably a frontloader: even in ordinary contexts, you need to know $Q$ in order to acquire your knowledge of $P$.

But while it’s plausible that, in high-standards contexts wherein $Q$ is salient, you need to know $Q$ in order to know $P$, it’s far from clear why that would be so in ordinary contexts as well. Why, for example, would you need to know that your car isn’t stolen (as well as the denial of every other wholesale and piecemeal skeptical hypothesis), which possibility hasn’t crossed your mind (or that of the attributor, if different), in order to know that it’s in 3b where you left it, so long as, in fact, it isn’t stolen?

The obvious answer is that requiring knowledge of $Q$ preserves closure in ordinary contexts. But if the contextualist affirms closure because of, for example, the abominable conjunction objection, contextualism already addresses that objection without requiring closure.[^note-55] In my high-standards context in which I contemplate “your car is stolen”, “you know your car is in 3b but not that it’s not stolen” is infelicitous because you know neither, and so don’t know that your car is in 3b. It’s entirely compatible with this that, in low-standards contexts wherein I’m not contemplating car thefts, “you know that it’s in 3b but not that it’s not stolen” is true. And any inclination to think that the conjunction is abominable in ordinary contexts as well is explicable as an instance of the “semantic blindness” tendency to fail to notice that standards that apply in high-standards contexts don’t apply in low-standards contexts. So this objection to closure denial, at least, doesn’t discriminate between closure-affirming and closure-denying contextualism (Alspector-Kelly 2019, §§10.3–10.4)[^alspector-kelly-2019].[^note-56]

#### 3.3.2 Warrant by Entitlement

An increasingly popular view is that we possess default warrants—warrants “by entitlement”—for the denials of wholesale skeptical hypotheses, which warrants require no evidence. There are a number of variations on the theme, but the essential idea is that these “cornerstone” propositions constitute an essential backdrop against which our intellectual exchange with the world takes place; they are the “hinges” upon which empirical inquiry turns (Wittgenstein 1969)[^wittgenstein-1969]. So they can’t themselves be subject to such inquiry. But they also can’t be coherently repudiated since, without them, there would be no inquiry at all. Such cornerstones include, not only the denial of wholesale skeptical hypotheses, but also “my senses are reliable”, “the future will be like the past”, “there is a material world”, and a number of others (Wright 2004 and 2014, Pritchard 2016 and 2018, and Coliva 2014 and 2015)[^coliva-2014][^coliva-2015][^pritchard-2016][^pritchard-2018][^wright-2004][^wright-2014].

One problem with the entitlement strategy is that of *leaching* (Wright 2004)[^wright-2004]. Since $H$ implies $\neg BIV$, if $\neg BIV$ is false then so is $H$. So any risk that $\neg BIV$ is false—that you are a $BIV$—is inherited by $H$, notwithstanding your evidence for $H$. But, having no evidence for $\neg BIV$, you have no epistemic safeguards against that risk: your entitlement for $\neg BIV$ has nothing to do with whether it’s true, or likely so, but only reflects your being constrained to rely on it. So your belief in $H$ is equally at risk, and so isn’t known (or justified). See Wright 2004, 2012 and 2014, and Moretti and Wright 2023 for responses.

A related problem is that of *alchemy* (McGlynn 2014a)[^mcglynn-2014a]. Suppose that, in light of your entitlement to $\neg BIV$, it’s seeming to you as though you have hands provides you with an evidential warrant for $H$. Since $H$ implies $\neg BIV$, closure seems to require that you have, not merely an entitlement, but also an evidential warrant for $\neg BIV$.

In response Wright concedes that closure for evidential warrants fails, but insists that closure for warrants per se, which may be evidential or not, is still preserved (Wright 2004)[^wright-2004]. But the denials of wholesale skeptical hypotheses, and most other cornerstones, are contingent; and the idea that we could enjoy warrants for belief in contingent propositions without any evidence is, to many, doubtful. Wright suggests that we don’t *believe* cornerstones, but only *trust* or *accept* them. But knowledge is also standardly taken to require, not mere acceptance or trust, but also belief. And even if the attitude that knowledge requires is expanded to include acceptance or trust, knowledge is also standardly understood to require proper basing. But it’s not clear how your acceptance/trust in $Q$ can be based on a default entitlement.[^note-57]

Admittedly, the consequent of SPWC—the version of closure that the frontloader can endorse—only requires that you have a warrant for $Q$, not that you know it. But the idea that you can have a warrant—which we’ve understood here to be a way of knowing—for a proposition that you can’t know is, at least, odd.[^note-58]

The entitlement strategy won’t apply to piecemeal skeptical hypotheses since ordinary empirical evidence is obviously possible for “it’s not a disguised mule”, “I will lose the lottery”, “my car isn’t stolen”, and the like. The frontloader who mobilizes the entitlement strategy will, then, need another way to handle such hypotheses.

### 3.4 Transmissivism

Since §3.1 we’ve been pursuing the preservationist option, according to which transmission sometimes fails—in Dretske cases, at least—but, when it does fail, something ensures that the conclusion ends up being known anyway, so that closure is preserved. In this section we’ll explore the transmissivist option, according to which transmission (and, therefore, closure) succeeds, if not always, then at least in some Dretske cases.

According to *dogmatism*, its perceptually seeming to you as though $H$ suffices on its own, in the absence of defeaters, to warrant the belief that $H$ (Pryor 2000, 2004, and 2012)[^pryor-2000][^pryor-2004][^pryor-2012].[^note-59] According to *disjunctivism*, in ordinary, non-skeptical scenarios your evidence doesn’t merely consist in your *seeming* to have hands (as it would if you were a $BIV)$, but in your *seeing* that you have them, where “seeing” is factive: you can only see that you have hands if you have them (McDowell 1986 and 1995, Pritchard 2012)[^mcdowell-1986][^mcdowell-1995][^pritchard-2012]. And according to $E = K$, your evidence is all and only that which you know. Since, in the “good”, non-skeptical case, you know $H, H$ constitutes evidence that you can then wield against skeptical hypotheses (Williamson 2000)[^williamson-2000].

Frontloading is false on each of these views, at least with respect to wholesale skeptical hypotheses: you don’t need to know $\neg BIV$ in order to acquire your knowledge of $H$. As a result, it seems, nothing stands in the way of learning, in the style of G. E. Moore, $\neg BIV$ by inferring it from $H$ (Moore 1939 [1959])[^moore-1939]. Correspondingly, advocates of these views very typically endorse that Moorean inference.[^note-60]

These views confront the robust intuition that the Moorean inference doesn’t transmit. One explanation for this is that we’re confusing the question whether an argument can rationally resolve initial open-mindedness about the conclusion with whether warrant transmits. If you are, like the skeptic, initially open-minded about whether $\neg BIV$ is true, then you are indeed rationally obliged to discount your putative visual evidence for $H$ (since it isn’t probative if you are a $BIV)$, and so can’t resolve your initial open-mindedness concerning $\neg BIV$ by inferring it from $H$. Since this only applies if you are initially open-minded, that inability is a dialectical failing (even if the dialectic is, as it were, in your head) and varies depending on the audience.

Warrant transmission, however, is an epistemic, not a dialectical, matter, and doesn’t so vary. If you can acquire a warrant for $H$ solely on the basis of its seeming that $H$, as per the dogmatist, or on the basis of your *seeing* that $H$, as per the disjunctivist, then you can acquire a warrant for $\neg BIV$ by inference from $H$ whether or not doing so resolves antecedent open-mindedness about the conclusion (Pryor 2004; see also Brown 2005)[^brown-2005][^pryor-2004]. (Simion 2023 criticizes this explanation of our intuition but offers a different explanation in defense of transmissivism.)[^simion-2023]

One problem with this explanation is that virtually everyone thinks that they’re not $BIV$s, and so aren’t open-minded on the issue, but still intuit that there’s something wrong with the Moorean inference. The transmissivist can, however, respond that we’re intuiting, not that the argument doesn’t work for us, but that it would beg the question against a skeptic. (Kelp 2023, however, argues that you can’t come to know a proposition by means of a question-begging argument.)[^kelp-2023]

It’s unclear, however, what purpose the Moorean inference serves. Skeptical hypotheses are of little intrinsic interest aside from the skeptic’s wielding such hypotheses against ordinary knowledge. But, according to the transmissivist, we don’t need to know beforehand that skeptical hypotheses are false in order to acquire ordinary knowledge. So ordinary knowledge is secure whatever the fortunes of skeptical hypotheses might be; the Moorean inference can play no coherent role in the defense of that knowledge. At best, it can show that closure can also be preserved. But transmissivists are precisely those who believe in SPC because they believe in SPT. So this amounts to showing that if we endorse transmissivism we’ll preserve transmission (see Alspector-Kelly §5.1).

Two problems for transmissivism have already been canvassed above. First, it countenances knowledge acquisition through inferences from $P$ to $Q$ in Dretske cases, wherein evidence $E$ favoring $P$ lowers the probability of $Q$. It’s at least odd to think that you can nevertheless learn $Q$ by means of such an inference (see §3.1). Second, you can recognize beforehand that, in Dretske cases, your method for evaluating $Q$ will deliver $Q$ whether or not $Q$ is true (see §3.2). It’s very implausible that such inferences transmit.

A third problem is that transmissivism appears to license bootstrapping. You look at a series of colored cards. In each case you note the color the card appears to be, believe that it is that color, and conjoin these: “card 1 appears red and is red”, for example. You do the same for the rest of the 1000 cards, and infer from the 1000 propositions that $A$, your color vision has been accurate 1000 times. Finally, you inductively infer from $A$ that $R$, your color vision is reliable.

As a warrant for $R$, this is intuitively absurd. But it’s difficult for the transmissivist to say why. Only skeptics will deny that you can learn the color of something by noting the color it appears to have. And the subsequent inferences to $A$ are instances of MPC. The transmissivist could resist the inference from $A$ to $R$, which is inductive. But A seems to constitute excellent inductive grounds for $R$.[^note-61]

You can also recognize that, before you get started, you will inevitably end up endorsing $R$ (and $A)$ whether or not it is true. But, as with Dretske cases, if you know this beforehand, there’s no point in your going through the motions. (See Bergmann 2004, Cohen 2005, Markie 2005, and Pryor 2004 for closure-preserving responses to bootstrapping, and Alspector-Kelly 2019, §11.1.2. for a closure-denying response.)[^alspector-kelly-2019][^bergmann-2004][^cohen-2005][^markie-2005][^pryor-2004][^note-62]

A fourth concern is that transmissivism seems to license a pernicious resistance to evidence.[^note-63] It follows from $P$ that any future evidence against $P$ must be misleading. Suppose you know $P$ and infer the latter from it. If transmissivism is true, then you know the latter. But, surely, you shouldn’t discount future evidence against $P$ (Harman 1973, attributing the problem to Saul Kripke)[^harman-1973]. Audi 1988 argues that closure fails in light of this problem. Feldman 1995 responds to Audi’s argument; Audi replies in his 1995. Harman 1973, Sorensen 1988 and Veber 2004 offer closure-preserving responses.

Neither dogmatism nor disjunctivism will apply to many Dretske cases involving piecemeal hypotheses: it doesn’t perceptually seem as though you can’t afford an African safari, or that your car is in 3b (remember that you’re not currently looking at it); and you don’t see that these claims are true. So some other source of warrant—most plausibly, background information—will be needed for “I’ll lose the lottery”, “my car isn’t stolen”, and the like. The extent to which the $E = K$ advocate will apply the transmissivist response to piecemeal skeptical hypotheses isn’t clear, since one could know that those hypotheses are false by other means than by inference from ordinary propositions.[^note-64]

## 4. Multi-Premise Closure

The discussion to this point has entirely concerned SPC. This is because there are issues that only affect MPC (or so it seems at first glance).

Recall from §2.8 that, on the probabilistic threshold conception, you’re justified in believing $P$ when the probability of $P$ on your evidence is above some high threshold, and know $P$ when your belief, in addition to being sufficiently probable, is also true and not a Gettier case. Since the probability of your beliefs given your evidence is rarely 1, that threshold is standardly understood to be less than 1 in order to avoid skepticism. But if the probability of two or more premises is, while above that threshold, less than 1, the probability of their conjunction can drop below that threshold. And that allows the probability of the conclusion to also fall below that threshold, since its probability need only be at least as high as the probability of that conjunction. So MPC can fail on the threshold view. This doesn’t affect SPC, since if $P$ implies $Q$ then $p(Q) \ge p(P)$.

A classic illustration is the lottery paradox (Kyburg 1961)[^kyburg-1961]. It’s highly probable, of each ticket in a typical lottery, that it will lose. Suppose that—like many real lotteries—although it’s probable that there’s a winning ticket in a particular lottery, it’s not guaranteed; and, as it turns out, there isn’t a winner this time around. If you believe, of each ticket, that it will lose, those beliefs will all be true. And they don’t exhibit any of the characteristics of Gettier cases. So, on the threshold view, you know, of each ticket, that it will lose. Those propositions together imply that all the tickets will lose (equivalently, that the conjunction of the many “ticket x will lose” propositions is true).[^note-65] But you don’t know the latter, since it’s improbable. MPC fails.

One can deny, as many do, that you know, of each losing ticket, that that ticket will lose, however probable its losing might be. Perhaps, for example, knowing $P$ requires, not only that $P$ is probable on your evidence, but also that your belief in $P$ is safe, which, as per §2.8 above, these beliefs are not. But suppose that you do in fact know every one of the thousands of individual claims you’ve made in your book, each of which is, then, both safe and probable on your evidence. Those claims together imply their conjunction. However, as you modestly concede, it’s likely that at least one claim in the book is wrong. That conjunction is therefore improbable. On the view we’re considering, then, you don’t know it, and MPC fails.[^note-66] Preserving MPC in this case requires, not that high probability is not sufficient for knowledge, but that it isn’t necessary: your belief can count as known even if its probability on your evidence is very low. Even those who don’t endorse high probability as sufficient for knowledge might balk at the idea that you can know $P$ despite $P$’s being highly improbable on your evidence (but see Williamson 2009a and 2014, and Smith 2016a and 2025)[^smith-2016a][^smith-2025][^williamson-2009a][^williamson-2014][^williamson-2025].

A compromise is to endorse SPC and reject MPC. But one problem with doing so is that the intuitions supporting SPC seem to equally support MPC. A purported cost of closure denial discussed in §2.5 above is that closure deniers are forced to reject highly intuitive closure principles like addition closure, simplification closure, or equivalence closure. But many simple multi-premise closure principles—employing conjunction introduction, modus ponens, modus tollens, disjunctive syllogism, etc.—are equally highly intuitive, and are all susceptible to the risk-accrual problem. Moreover, “I know $P$ and I know $Q$, but I don’t know $P \amp Q$” (for example) seems as abominable as any single-premise version.

Another concern with the compromise is that our inferential dispositions aren’t infallible: you could believe $Q$ because, you think, it follows from $P$ when, in fact, it doesn’t. So the risk that the conclusion could be false is a function, not only of the risk that the premises are false, but also that the inference is faulty. These can combine, so that the risk that the conclusion is false is too high for it to count as known (Lasonen 2008)[^lasonen-2008].

This can happen even if there is *no* risk that the premise is false. Suppose that you perform an extremely long sequence of single-premise deductions from a certain mathematical truth. For each step there is a small chance that you’ve reasoned incorrectly. Those chances can accumulate so that your putative knowledge of the final conclusion is defeated by that accumulated risk (Lasonen 2008, Schechter 2013, and Brown 2018, chs. 5 & 6; but see Tang 2018 and Montessori 2025)[^brown-2018][^lasonen-2008][^montessori-2025][^schechter-2013][^tang-2018].[^note-67]

## 5. Justification Closure

The discussion to this point has only concerned knowledge closure. But there is also a robust debate concerning whether justification is closed.

Consider the following principle:

SPJC: If you are justified in believing $P$, and believe $Q$ because it’s implied by $P$, then you are justified in believing $Q$.

Assuming that justified false beliefs are possible, neither sensitivity nor safety (nor basis-relative versions of them) can be justification, since both are factive.[^note-68] But much of the discussion from §§3–4 above applies also to justification. If SPJC is true, is that because transmission of justification succeeds? If so, then the following is also correct:

SPJT: if (i) you are justified in believing $P$, and believe $Q$ because it’s implied by $P$, then (ii) you are justified in believing $Q$ because of (i).

It is, however, as unintuitive that SPJT is true in Dretske cases as it is that SPT is true in those cases. If, instead, SPJT is false in such cases but SPJC is preserved, then much the same questions can be posed concerning the source of justification as were asked about the source of warrant: does your justification for $P$ suffice on its own as a justification for $Q$? Or is justification for $Q$ a precondition for your justification for $P$? If the latter, is the requisite justification for $Q$ provided by background knowledge? Or is $Q$ justified by default?

In fact, a significant proportion of the literature on these issues expressly concerns either justification or, confusingly, “warrant”, but where the latter term typically means, not ways of knowing, but either justification or something similar to it (see note 48). The debate concerning knowledge and that concerning justification/warrant are not always carefully distinguished. This is unfortunate, since a view ensuring that justification is closed doesn’t thereby ensure that knowledge is closed as well. It is, for example, more plausible that purely statistical information concerning the likelihood of losing the lottery delivers justification for “I will lose” than that it delivers knowledge. It’s also at least somewhat more plausible that non-evidential entitlements can justify cornerstone propositions than that such entitlements deliver knowledge of them.

If the justification for your belief is a function of its probability on your evidence, then you would be justified in believing, for each ticket in a lottery, that it will lose—including the one that will win if there is one, assuming justification isn’t factive—but not that they all will. So, for the same reasons canvassed in §4, SPJC will succeed but the multi-premise version, MPJC, will fail. And the arguments extending those concerns to SPC still apply, thereby threatening SPJC as well.

Other conceptions of justification are not similarly threatened. If justification is knowledge then, if you are justified in believing the premises, you know them. And if $E = K$, the probability of each premise on your evidence—on, that is, that very premise—is 1. And since the premises together imply the conclusion, the probability of the conclusion is also 1.

There are other non-probabilistic accounts of justification that preserve both SPJC and MPJC without the radical identification of justification and knowledge. For example, on Martin Smith’s normic account, you have a justification for believing $P$ when $P$ is normically supported by your evidence (Smith 2010 and 2016a)[^smith-2010][^smith-2016a]. “A body of evidence $E$ normically supports a proposition $P$ just in case the circumstance in which $E$ is true and $P$ is false requires more explanation than the circumstance in which $E$ and $P$ are both true” (Smith 2016a, 40; see Goodman and Salow 2023 for a similar view)[^goodman-2023][^smith-2016a].

Although improbable, there’s nothing abnormal about your winning the lottery given your statistical evidence. So that evidence doesn’t justify your believing that you will lose the lottery (call this case $A)$. However, if you watch the draw on TV and the winning numbers you see on screen don’t match those on your ticket then, if you nevertheless won, *that* would be abnormal, and would call for explanation: your eyesight failed you, you’re hallucinating, the studio is broadcasting the wrong lottery, and so on. Since the most normal worlds wherein you have the same evidence are those in which these aberrations don’t occur, and so in which you have indeed lost, your belief that you lost is justified (case $B)$.

Since you’re not justified in believing that you will lose the lottery given only that you’re very likely to lose, Smith concedes that you’re not justified in believing that you won’t be able to afford an African safari. However, he suggests, this skepticism doesn’t extend to lottery-esque propositions: you *are* justified in believing, for example, that your car hasn’t been stolen, because its being stolen would be abnormal and so call for explanation. So you’re justified in believing both that your car is in spot 3b where you parked it and that it wasn’t stolen; and similarly for other lottery-esque cases. SPJC is preserved (Smith 2016a, 56–58)[^smith-2016a].[^note-69]

MPJC is also preserved. You’re not justified in believing, of each lottery ticket, that it loses solely on the basis of the probability of its doing so, so MPJC doesn’t imply that you’re justified in believing that they’ll all lose. And if you’re justified in believing every sentence in your book then, if one of those is in fact false, some explanation of its being so is called for. But the conjunction of those sentences is only false if one or more of them is false. So the conjunction is only false if an explanation of *its* being false is called for. So you’re justified in believing that the conjunction is true, and so *not* justified in believing its negation, that at least one of those claims is false (Smith 2016a and 2022; but see Littlejohn and Dutant 2020 and Backes 2026)[^backes-2026][^littlejohn-2020][^smith-2016a][^smith-2022].

In general, there’s much yet to explore concerning the relationship between closure and recent accounts of justification now on the market.[^note-70]

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=closure-epistemic). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/closure-epistemic/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=closure-epistemic&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/closure-epistemic/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- [Epistemic Closure Principles](https://iep.utm.edu/epis-clo/), entry by John M. Collins at *Internet Encyclopedia of Philosophy*
- Luper, Steven, “Epistemic Closure”, *Stanford Encyclopedia of Philosophy* (Fall 2026 Edition), Edward N. Zalta & Uri Nodelman (eds.), URL = <[https://plato.stanford.edu/archives/fall2026/entries/closure-epistemic/](https://plato.stanford.edu/archives/fall2026/entries/closure-epistemic/)>. [This was the previous entry on this topic in the *Stanford Encyclopedia of Philosophy* – see the [version history](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=closure-epistemic).]

## Related Entries

confirmation | contextualism, epistemic | evidence | knowledge: analysis of | skepticism | skepticism: and content externalism | transmission of justification and warrant

## Notes（原文脚注）

[^note-1]: The natural numbers, for example, are closed under multiplication: the product of any two natural numbers is also a natural number. But they are not closed under division: 1 divided by 3 is not a natural number.

[^note-2]: $P$ deductively implies $Q$ when an argument with $P$ as premise and $Q$ as conclusion is deductively valid: if the premise is true then the conclusion must, as a matter of logical necessity, be true as well. Although “implies” in ordinary language sometimes means “suggests”, “insinuates”, or the like, “imply” and “implies” are used throughout this entry (and the relevant literature) to mean valid deductive entailment. Closure principles involving inductive inference are rarely discussed in the literature.

[^note-3]: “[T]he idea that no version of [closure] is true strikes me, and many other philosophers, as one of the least plausible ideas to come down the philosophical pike in recent years” (Feldman 1995, 487)[^feldman-1995]. “[I]f a philosopher advances a view that forces us to reject closure, that should be taken as a reductio of that philosopher’s view” (Fumerton 1995, 131)[^fumerton-1995].

[^note-4]: “[Timothy] Williamson has an insightful take on the root of epistemic closure intuitions, namely, the idea that ‘deduction is a way of extending one’s knowledge’” (Hawthorne 2013, fn. 6, quoting Williamson 2000, 117; see also Pritchard 2016, 13)[^hawthorne-2013][^pritchard-2016][^williamson-2000].

[^note-5]: If, instead, we maintain that competently deducing $Q$ from $P$ itself requires that you maintain your recognition that $P$ implies $Q$ throughout the deduction then, again, we might as well just characterize closure as concerning your state at the time when the competent deduction is complete.

[^note-6]: SPC is a true closure principle: a proposition that satisfies the relation “believed because it is implied by $P$”, where $P$ is a member of the set of known propositions, is a known proposition. Since the antecedent and consequent of the dynamic version concern what you know at different times, it doesn’t express a condition on the set of known propositions at a given time, and so is not, strictly speaking, a closure principle.

[^note-7]: If you did only know that $P$ implies $Q$ by testimony, then it would function for you as a premise: you would infer $Q$ from $P$ and $(P$ implies $Q)$. But suppose you also only know that $P$ and $(P$ implies $Q)$ imply $Q$ by testimony. Then you would infer $Q$ from $P, (P$ implies $Q)$, and $((P$ and $(P$ implies $Q))$ imply $Q)$. But suppose you only know that $P$, $(P$ implies $Q)$, and $((P$ and $(P$ implies $Q))$ imply $Q)$ imply $Q$ by testimony…. We can’t model your relationship to $P$’s implying $Q$ as just another premise that you know on pain of your never being able to detach the conclusion. See Lasonen 2008, 8 for a closely related argument. A classic illustration of the detachment problem is Lewis Carroll 1895.

[^note-8]: Another condition that is sometimes imposed on closure is that you don’t have a defeater suggesting that $P$ doesn’t imply $Q$. You might, for example, actually have the requisite accurate understanding of the inferential relation between $P$ and $Q$, but also have testimony from a highly reputable logician, uncharacteristically mistaken in this one instance, that this particular inference is invalid. It’s not clear, however, that such misleading defeaters undermine your knowledge of $Q$; they might, instead, undermine your knowing, or your being justified in believing or claiming, that you know $Q$. As a result, this condition is not imposed here.

[^note-9]: Attempts to finesse the closure principle in response to counterexamples that—even closure advocates concede—need accommodation have sometimes delivered versions of closure that are baroque enough as to remind one of similarly unwieldy post-Gettier analyses of knowledge (see, for example, definition (9) of justification closure in Simpson 2021, 12352).

[^note-10]: Nozick also claimed that knowledge must satisfy an *adherence* condition: were $P$ true you would believe it. He called the combined conditions “tracking”. Unlike sensitivity (or, as Nozick called it, variation), the adherence condition is rarely endorsed. An exception is Roush (2005)[^roush-2005], who offers probabilistic versions of both sensitivity and adherence. Roush also endorses a version of closure: you know propositions that you infer from propositions that you know (Roush 2005)[^roush-2005] or, later, that you track (Roush 2012)[^roush-2012] even if you don’t track the inferred proposition. It’s an open question, however, whether the later version really counts as closure-preserving, since it allows that you could know $P$, and infer $Q$ from $P$, but not know $Q$ because, although you know $P$, you don’t track it.

[^note-11]: In general, “were $P$ true then $Q$ would be true” is standardly understood to require that $Q$ is true in the $P$-worlds nearest to the actual world (although there can be $P$-worlds further out in which $Q$ is false.) This widely endorsed interpretation of subjunctive conditionals is due to Stalnaker 1968 and Lewis 1973. Nozick’s interpretation was a bit more elaborate; see Nozick 1981, 681, fn. 8. Nozick was also somewhat noncommittal about the correct possible-worlds interpretation of sensitivity and adherence; his primary commitment was to the subjunctive conditionals themselves (Nozick 1981, 173–174)[^nozick-1981]. Williamson 2023 argues that a viable interpretation of both the sensitivity and safety conditionals (see §2.6) actually preserves closure.

[^note-12]: See section §4 of the entry on skepticism for an overview of this argument.

[^note-13]: Roush 2010 argues that it’s not as easy to extend the skeptical hypothesis to other ordinary claims as it might seem.

[^note-14]: However, as we saw in §1.1, that is not a viable version of closure. And SPC’s antecedent requires, in addition to knowing $H$, that you believe $\neg BIV$ because it’s implied by $H$. But it’s very implausible that ordinary people believe $\neg BIV$ *because* it’s implied by $H$ (or by any other piece of ordinary knowledge). As a result, Warfield and David 2008 suggest that the closure principle can’t be utilized for the skeptic’s purposes. But the skeptic can respond that you *couldn’t* know $\neg BIV$ by any means whatsoever, including by inference from $H$, even if you knew $H$. But SPC ensures that, whether or not you *did* infer $\neg BIV$ from known $H$, if you *were* to do so, you *would* know $\neg BIV$. So you must not know $H$. This does, however, highlight the skeptic’s obligations: they need to claim that, even if you knew $H$, you couldn’t learn $\neg BIV$ by inference from it—that is, transmission would fail (see §3 below)—and, moreover, that there is no other way to learn $\neg BIV$ available to you. See Alspector-Kelly 2019, ch. 3.

[^note-15]: Your reason, in Dretske’s sense, is whatever it is to which you respond by forming your belief. It’s not required that you conceive of it as a reason, or even that you are aware that it produces your belief (Dretske 1970, 13–15)[^dretske-1970].

[^note-16]: Dretske’s “official” view, in Dretske 1983, is expressed, not subjunctively, but probabilistically: $S$ knows that $P$ iff $S$’s belief that $P$ is caused (or causally sustained) by a state which manifests the information that $P$, where a state manifests that information when the probability of $P$ given that state is 1. Nevertheless, Dretske has demonstrated no clear resistance to the subjunctive formulation of his view. (The relationship between the two formulations, however, deserves exploration.)

[^note-17]: An unexplored question is whether they deliver different answers in other cases.

[^note-18]: Despite the fact that discussion of skepticism has been dominated by wholesale hypotheses, there are reasons to think that piecemeal hypotheses constitute the greater threat; see Smith 2016b.

[^note-19]: See also Lawlor 2013 and 2023’s contextualized relevant alternatives account, as well as Horn 2018. But see Thomasson 2014, according to whose “easy ontology” we can resolve seemingly heavyweight ontological issues by inference from ordinary propositions.

[^note-20]: If, however, you believe that it’s a barn, not by inference from “it’s a red barn”, but because it looks like a barn, then your belief is not basis-sensitive: it would look like a barn if it weren’t because it would be a non-red fake barn. But “it’s a red barn” would still be basis-sensitive. Whether or not this combination is unintuitive, however, it’s not a violation of SPC, whose antecedent requires that you believe “it’s a barn” by inference from “it’s a red barn”.

[^note-21]: A possible response is that you only know that it’s a red barn by its appearance if you know, by its appearance, that it’s red and, by its appearance, that it’s a barn. But the latter is false (see note 20). In general, perhaps knowledge of a conjunction (it’s red and a barn) requires knowledge of, and so sensitivity to, each of its conjuncts. See Becker 2012. See also Baumann 2012 and Murphy and Black 2012. The intuition that one doesn’t know in fake-barn style cases is also not as widely affirmed as it is with respect to more traditional Gettier cases.

[^note-22]: The objection—or, at least, the appellation “abominable”—originates in DeRose 1995. See also Veber 2013 for a variety of ways of pressing the objection.

[^note-23]: “$P$ but I don’t know $P$” is a pragmatic contradiction akin to the Moorean paradox “$P$ but I don’t believe $P$”. Although both are infelicitous to assert, their conjuncts are consistent: $P$ could, in fact, be true despite my not believing, or knowing, that it is.

[^note-24]: $H$ implies $\neg BIV$, as does $\neg BIV$. Since both disjuncts of $H \vee \neg BIV$ imply $\neg BIV$, so does the disjunction. And $\neg BIV$ implies the disjunction because it implies the $\neg BIV$ disjunct. So $H \vee \neg BIV$ and $\neg BIV$ imply each other. So they’re equivalent.

[^note-25]: $H$ implies both itself and $\neg BIV$, and so implies both conjuncts of $H \amp \neg BIV$. And the conjunction—in particular, the left conjunct—implies $H$. So $H$ and $H \amp \neg BIV$ imply each other. So they’re equivalent.

[^note-26]: This is because logically equivalent propositions are true (or false) in the same possible worlds.

[^note-27]: See also Sharon and Spectre 2017a, who argue that evidential versions of AC and SC fail despite being equally intuitive. Yablo 2017 instead denies EC, as do Sherman and Harman 2011. See also Lawlor 2005.

[^note-28]: See, for example, Vogel 2000’s “Omar’s new shoes” case. Sensitivity also has notorious problems with knowledge of necessary truths, inductive knowledge, and knowledge of the future. The essays in Luper-Foy 1987 include a variety of criticisms of Nozick, many of which would also apply to Dretske.

[^note-29]: This is the simplest version of safety. A basis-relative version will be introduced in §2.9 below. Another version only requires that $P$ is true in *most* of the nearby worlds in which you believe $P$, although it must also be true in all *very* nearby such worlds (Pritchard 2009a, 2009b)[^pritchard-2009a][^pritchard-2009b].

[^note-30]: On the Lewis/Stalnaker possible-worlds interpretation of subjunctive conditionals, “were you to believe $P$, $P$ would be true” is trivially satisfied by a true belief, since the actual world is the nearest in which you believe $P$, and in that world $P$ is true. The typical possible-worlds interpretation of the safety conditional constitutes a departure from that account.

[^note-31]: Views that endorse knowledge of the denials of skeptical hypotheses are sometimes called “neo-Moorean”.

[^note-32]: This is especially so for the denial of piecemeal skeptical hypotheses like $DM$ since, unlike wholesale hypotheses, it’s easy to imagine empirical evidence that would count against it.

[^note-33]: Perhaps, for example, evidence is also required. But then a putative advantage of the safety account—that it can explain how you know $\neg BIV$ despite not having evidence for it—no longer applies. And the safety theorist would have to come up with evidence for the denials of both wholesale and piecemeal skeptical hypotheses. Note also that your evidence for your having hands—its looking to you as though you have them—plays a crucial role in ensuring that your belief that you have hands is safe. But evidence can’t play that role for vacuously safe beliefs. So it’s unclear why a safety theorist would impose a blanket evidence requirement on knowledge.

[^note-34]: The sensitivity theorist can offer a similar explanation: in the nearest world in which you win, you still believe that you lose (and on the same basis, namely, the probability of losing).

[^note-35]: A variation of basis-safety is also designed to deal with necessarily true propositions. Such propositions are true in all possible worlds, and so in all nearby worlds wherein you believe them, no matter why you do so; necessarily true propositions are vacuously basis-safe. So your belief in necessarily true proposition $T$ is basis-safe even if you believe it because your horoscope says so. But there’s presumably a nearby world in which your horoscope says instead that necessary falsehood $F$, relevantly similar to $T$, is true. So revise basis-safety to require that there be no nearby world in which you believe a relevantly similar proposition to $T$ (including $T$ itself) on the same basis as you do in the actual world and in which that proposition is false. Your belief in $T$, on the revision, is unsafe (Pritchard 2009b)[^pritchard-2009b].

[^note-36]: See Wright 1985, 2000, 2002, 2003, 2004, 2008, 2011, 2012, 2014 and 2023, and Davies 1998, 2000 and 2003. There is now a burgeoning literature on warrant transmission, including Alspector-Kelly 2015, Brown 2004, Chandler 2010, Ebert 2005, McKinsey 2003, McLaughlin 2000 and 2003, Moretti 2012, Okasha 2004, Pryor 2004 and 2012, Silins 2005, Smith 2009, Zalabardo 2014, and many others. See also the entry on transmission of justification and warrant.

[^note-37]: Knowledge overdetermination presupposes belief overdetermination (see §1.1): since knowing $P$ requires that you believe $P$ on a suitable basis, knowing $P$ in multiple ways requires that you believe $P$ on multiple bases.

[^note-38]: This is in line with the use of “warrant” in Plantinga 1993a and 1993b as the difference between mere true belief and knowledge. See, however, note 48 below on another use of “warrant”.

[^note-39]: If $DM$ implies $LZ$, then $DM$ is logically equivalent to $(DM \amp LZ). DM$ and $(DM \amp LZ)$ are, therefore, equiprobable. $p(DM\mid LZ) = p(DM \amp LZ)/p(LZ)$, so $p(DM\mid LZ)$ also equals $p(DM)/p(LZ)$. Assuming that $0 \lt p(LZ) \lt 1$, $p(DM)/p(LZ) \gt p(DM)$. So $p(DM\mid LZ) \gt p(DM)$. Since $p(DM) = 1 - p(\neg DM)$, $p(DM\mid LZ) = 1 - p(\neg DM\mid LZ)$. So $p(\neg DM\mid LZ) \lt p(\neg DM)$.

[^note-40]: Sharon and Spectre 2017a wield this point in a general argument against closure. Although $LZ$ is evidence for $Z$, it isn’t evidence for $\neg DM$. So evidence closure is false: that $P$ implies $Q$ doesn’t ensure that evidence for $P$ is evidence for $Q$. Sharon and Spectre utilize this in a number of arguments for the openness of knowledge itself. Yablo 2017 and Comesaña 2017 critique those arguments; Sharon and Spectre 2017b respond to those critiques.

[^note-41]: $BE$ need not be required in order for $LZ$ to deliver a warrant for Z; this needn’t be a frontloading view (see §3.2 below). It could be that $LZ$ by itself warrants $Z$ while $BE$ warrants $\neg DM$.

[^note-42]: It’s less clear how background evidence could confer the requisite high prior probability on the denial of wholesale skeptical hypotheses such as $BIV$, however, since those hypotheses incorporate all putative background evidence by design. $BIV$ (suitably elaborated), for example, implies that you have all of the experiences, $BE$, that you actually have, so that you will appear to have the same background evidence that you take yourself to have on the basis of that experience. So $p(\neg BIV\mid BE) \lt p(\neg BIV)$. It seems that $\neg BIV$ would have to be sufficiently probable on a priori grounds. But see note 54 and §3.3.1 below.

[^note-43]: The term “transmission” is, unfortunately, misleading in that it suggests that the warrant for the premise is somehow transferred to the conclusion, so that the former also warrants the latter. This is, in fact, antithetical to the concept of transmission according to which the warrant for the conclusion is acquired by inferring it from the premise, since that inference is otiose if the premise’s warrant already warrants the conclusion.

[^note-44]: In response, one might offer an entirely different closure principle: if you know $P$ on the basis of evidence $E$ and, perhaps, background evidence $BE, P$ implies $Q$, and you also believe $Q$ on the basis of $E \amp BE$, then you know $Q$. (In Dretske cases $Q$ would be known solely on the basis of $BE$ and despite $E$.) Notably, this principle doesn’t require that you are aware that $P$ implies $Q$ or that you believe $Q$ because it is so implied, and so doesn’t express any intuition to the effect that inference expands knowledge. Whether such a closure principle is viable, intuitively or theoretically, is an unexplored question.

[^note-45]: Frontloading is also called “conservatism” in the literature (opposing the “dogmatism” discussed in §3.4 below). The term “conservatism” is, however, sometimes directly associated with the views of Crispin Wright, which are somewhat more specific.

[^note-46]: This is the reasoning of Wright’s “disjunctive template” (Wright 2000)[^wright-2000]. It’s also encouraged by underdetermination worries: $Z$ and $\neg DM$ appear to constitute competing hypotheses that both accommodate the evidence $LZ$, so that further grounds are required in order to favor the former hypothesis over the latter. (However, responding to underdetermination, *prima facie*, only requires favoring one hypothesis over the other; it doesn’t clearly also require knowing that the less favored hypothesis is false.)

[^note-47]: This is, at least roughly, the reasoning of Wright’s “revised template” (Wright 2011, 2012; but see note 48)[^wright-2011][^wright-2012]. On this reasoning, you also need a warrant for “it’s not a zebra disguised to look like a zebra”, since that’s another way in which the condition—that it’s not disguised—can be violated. (A likely story: the “mule” that the zoo-keepers painted to look like a zebra is, in fact, a zebra with a skin condition that removed its stripes so that, before being painted, it looked just like a mule. It was sold to the unsuspecting zoo by unscrupulous animal traffickers as a mule because nobody would want to buy a diseased zebra. As a result, the animal in the paddock is a zebra cleverly disguised to look just like a zebra.) In general, this account requires antecedent knowledge, not just of skeptical hypotheses, but also of what might be called their “Gettier variants”: although you’re only dreaming that you have hands, you do in fact have hands; although the report that the Broncos won yesterday is an accidentally posted report of last month’s game, they won that game too; and so on. These hypotheses are not inconsistent with the initial proposition $P$ (you have hands, the Broncos won), and so their denial doesn’t follow from $P$; but they are inconsistent with your knowing $P$ in the way that you purport to know it.

[^note-48]: Despite the fact that Wright is the best-known advocate of the frontloading strategy for closure preservation, the application of his view to the knowledge closure debate is problematic in at least three ways. First, although he is concerned with the transmission of “warrant”, his use of that term clearly isn’t equivalent to “ways of knowing” as we have used it here, but represents something more akin to (or even weaker than) justification: “to possess a warrant for $P$ is to be in a state wherein it is, all things considered, epistemically appropriate to believe [or trust] $P$.” (Wright 2008, 6)[^wright-2008]. Second, in Wright 2011 and 2012 he refers, not to failures of transmission of warrant, but of *claims* to warrant. He recognizes that this could accommodate a certain rapprochement with his dogmatist opponent: transmission succeeds for warrant but not for claims to warrant (Wright 2012)[^wright-2012]. Third, in his most recent work Wright is explicit: both dynamic and static knowledge closure principles fail (Wright 2023, 186)[^wright-2023]. In order to maintain the relevance of the Wrightean approach to the knowledge closure debate, the discussion in the text prescinds from these concerns.

[^note-49]: Coliva (2014 and 2015) also offers an account of transmission failure that doesn’t preserve closure: although one does need to reasonably *assume* $Q$ in the relevant cases, one need not *know* (or have a warrant for) $Q$. For similar views see Di Bello 2014 and Sherman and Harman 2011.

[^note-50]: The basing requirement avoids cases wherein you have a warrant for $P$ and believe it, but believe it on the basis of, for example, wishful thinking. You presumably don’t then know $P$. Having a warrant for $P$ vs. knowing $P$ parallels the standard distinction between having a justification for believing $P$—propositional justification—and one’s belief in $P$’s being justified—doxastic justification.

[^note-51]: This is not, however, a true closure principle, since the antecedent references propositions you know and the second disjunct of the consequent only references propositions for which you have a warrant.

[^note-52]: We’ve already discussed a possible third source, that $S$’s warrant for $P$ itself suffices to warrant $Q$, in §3.1.

[^note-53]: The externalist views of evidence are disjunctivism and “$E = K$”; see §3.4 below.

[^note-54]: An alternative attempt to wield the characteristics of your background experience against skeptical hypotheses is that of the abductivist, according to which the “real-world” hypothesis provides a better explanation for those characteristics than does, for example, the $BIV$ hypothesis—better enough, it would have to be claimed, to deliver knowledge of $\neg BIV$. See Vogel 1990b, the exchange between Vogel and Fumerton in Steup, Turri, and Sosa 2013, Beebe 2009, McCain 2019, and Carter 2024.

[^note-55]: See §2.4 above. This is an objection that DeRose (1995)[^derose-1995], a contextualist, raises against closure denial.

[^note-56]: The same reasoning applies to pragmatic encroachment views, AKA interest-relative or sensitive moderate invariantism (Hawthorne 2004, Stanley 2008, Fantl and McGrath 2009)[^fantl-2009][^hawthorne-2004][^stanley-2008]. Those views emphasize variation in the standards for knowing with the knower’s practical circumstances. But they also need to countenance such variation in virtue of salience to the knowing subject of the skeptical hypothesis in order to accommodate many Dretske cases, since often nothing of practical significance hangs on those hypotheses’ being true. (There will typically be no practical implications for the typical zoo-goer whether $Z$ or $DM$, for example.) So, contemplation of such hypotheses places the subject in a high-standards situation in which they know neither $P$ nor $Q$; the abominable conjunction is false. That’s compatible with their knowing $P$ but not $Q$ in low-standards contexts—and so in which the abominable conjunction is true—wherein $Q$, and so the conjunction, isn’t contemplated.

[^note-57]: As per note 48, Wright means by “warrant” an all-things considered license to accept, not ways of knowing; he doesn’t suggest that such a warrant delivers knowledge. But we’re now considering the view as a way of preserving knowledge closure vis-a-vis wholesale skeptical hypotheses, whether or not that is Wright’s intent. See also Jope 2023.

[^note-58]: Pritchard (2016, 2018, and 2023) suggests that, precisely because we don’t *believe* cornerstones (or hinges), neither SPWC nor any other closure principle applies to them, since the antecedent of all such principles requires that you end up believing $Q$. Since the antecedent isn’t satisfied, the conditional is trivially true, and closure preserved. Wright responds that this amounts to “creative accounting”: we don’t acquire a warrant for cornerstone $Q$ propositions by inference from ordinary known $P$ propositions just because we, conveniently, don’t count as believing those $Q$ propositions; closure “holds—except when it doesn’t” (Wright 2023, 185)[^wright-2023]. See also Jope 2021 and Zhang 2021.

[^note-59]: Similar positions include phenomenal conservativism (Huemer 2001)[^huemer-2001] and moderate foundationalism (Alston 1976a and 1976b)[^alston-1976a][^alston-1976b].

[^note-60]: This isn’t inevitable; it’s possible to be a dogmatist, disjunctivist, or $E = K$ advocate without endorsing transmission and, so, without endorsing closure (see, for example, Lawlor 2023)[^lawlor-2023]. It isn’t entirely clear, in fact, that Williamson—the primary advocate of $E = K$—is a transmissivist (although he certainly advocates closure), because it’s not clear whether he thinks our knowledge of $\neg BIV$ originates in our inferring it from $H$ (or similar ordinary claims). On the one hand, he endorses the intuition that inference always expands knowledge (see note 4 above). On the other, he advocates a version of safety and, as we saw in §2.7, $Q$ propositions in Dretske cases are inevitably vacuously safe, and so safe whether or not they are inferred from anything.

[^note-61]: The bootstrapping problem was originally presented by Vogel 2000 as a problem for reliabilism, and subsequently by Cohen 2002 and 2005 as a problem for “basic knowledge”, being putative knowledge acquired from source $K$ without prior knowledge that $K$ is reliable. But suppose that you do know beforehand that your vision is reliable. You can then know that card is red because it appears red, and so know the conjunction; and similarly for all the other cards. That again appears to provide substantial inductive evidence that $R$. You did know that to start with (we’re assuming); but that doesn’t prevent your acquiring a *second* warrant for $R$. And it still seems absurd to suggest that you do so.

[^note-62]: White 2006 presents these three concerns as problems for dogmatism. But they are really problems for the combination of dogmatism (or disjunctivism or $E = K)$ and transmissivism; indeed, they are, arguably, more directly problems for the latter than the former. See Pryor 2013 and Kung 2010 for responses to White.

[^note-63]: This is sometimes called the dogmatism problem, but it should not be confused with the dogmatist position discussed above.

[^note-64]: Klein 2004 suggests that you only need to rule out skeptical hypotheses when you have some evidence in their favor. Since you can have no evidence for $BIV$, and there is no evidence for $DM$, we need to know neither $\neg BIV$ nor $\neg DM$ in order to learn $H$ or $Z$. Transmission then succeeds from the latter to the former. But frontloading is needed for lottery propositions, since we do have some non-zero statistical evidence for them: a lottery ticket will win, cars are stolen, and so on. (In fact, a number of zoos have been caught painting, not mules, but donkeys to look like zebras—e.g., in [Armenia](https://www.upi.com/Odd_News/2026/05/01/armenia-escaped-zebra-Yerevan-Zoo-painted-donkey/3011777648902/), [China](https://www.thesun.co.uk/news/33390533/china-zoo-donkeys-black-white-zebras/), [Egypt](https://www.bbc.com/news/world-africa-44968509), and [Gaza](https://www.theguardian.com/world/2009/nov/04/gaza-zoology).)

[^note-65]: Strictly speaking, the universal generalization is only equivalent to the conjunction given that the items referenced in the conjuncts exhaust the domain of quantification, which we can assume here.

[^note-66]: This is a variation of the paradox of the preface (Makinson 1965)[^makinson-1965].

[^note-67]: Such defeat might, in fact, be realized because it’s reasonable for you to assume that you’ve made a mistake somewhere even if there’s no actual risk of your having done so.

[^note-68]: If your belief is actually false, then it is false in the nearest possible world to the actual, namely, the actual world; and it is false in a world nearby to the actual, namely, the actual world. So only true beliefs can be sensitive and safe. Sutton 2007’s and Williamson 2025’s identification of justification with knowledge is an exception to the claim that justification is fallible, knowledge being factive. See also Littlejohn 2012.

[^note-69]: One might think, however, that normic support for “my car’s not stolen” on your evidence requires, not that your car’s being stolen *itself* would call for explanation, but that its being stolen *despite* *your evidence to the contrary* would do so. In lottery case B, your winning wouldn’t itself call for explanation, as Smith recognizes (Smith 2010, 23)[^smith-2010]. Nevertheless, your winning despite the mismatch between the numbers on your ticket and those on the screen *would* call for explanation, whereas such an explanation isn’t called for when your only evidence is that losing is likely given the odds, as in case A. Similarly, whether or not your car’s being stolen itself calls for explanation, that it was stolen despite the rarity of car thefts doesn’t do so. If, however, it was stolen despite your seeing what looks for all the world like your car on closed-circuit TV, *that* would call for explanation: the thief, say, had replaced your car with a car-façade when you weren’t paying attention. Given *that* evidence, your belief that it isn’t stolen is normatively supported, and so justified. So, given only that car thefts are rare, your belief that it isn’t stolen isn’t normatively supported, and so not justified, after all, although you are justified in believing that it’s in 3b; SPJC fails. See Alspector-Kelly 2019, §§8.5.1–8.5.2, for discussion of the distinction between explaining $\neg P$ itself and explaining $\neg P$ despite one’s evidence (or basis) for $P$.

[^note-70]: Many of these are “knowledge-first” accounts of justification, which appeal to knowledge in characterizing justification rather than vice versa. (Knowledge-first epistemology was initiated primarily by Williamson 2000.)[^williamson-2000] They include Bird 2007, Ichikawa 2014, Smithies 2012, Reynolds 2013, Rosenkranz 2018, Kelp 2016, Simion 2019, and Silva 2017. See McGlynn 2014b for critique of some knowledge-first accounts of justification. Smith’s view isn’t a knowledge-first account, since it doesn’t characterize justification in terms of knowledge. But it is related in that Smith sees justification and knowledge as “normatively coincident”: one can’t aim at being justified without simultaneously aiming at knowledge (Smith 2014 and 2016a, ch. 1)[^smith-2014][^smith-2016a].

[^adams-2012]: Adams, Fred, John Barker, and Julia Figurelli, 2012, “Towards Closure on Closure”, *Synthese*, 188: 179–196.

[^adams-2005]: Adams, Fred and Murray Clarke, 2005, “Resurrecting the Tracking Theories”, *Australasian Journal of Philosophy*, 83(2): 207–221.

[^alspector-kelly-2011]: Alspector-Kelly, Marc, 2011, “Why Safety Does Not Save Closure”, *Synthese*, 183(11): 127–142.

[^alspector-kelly-2013]: –––, 2013, “Review of *The Sensitivity Principle in Epistemology*, by Kelly Becker and Tim Black”, *Notre Dame Philosophical Reviews*, 14th June 2013. [[Alspector-Kelly 2013 available online](https://ndpr.nd.edu/reviews/the-sensitivity-principle-in-epistemology/)]

[^alspector-kelly-2015]: –––, 2015, “Wright Back to Dretske, or Why You Might as Well Deny Knowledge Closure”, *Philosophy and Phenomenological Research*, 90(3): 570–611.

[^alspector-kelly-2019]: –––, 2019, *Against Knowledge Closure*, Cambridge: Cambridge University Press.

[^alston-1976a]: Alston, William, 1976a, “Two Types of Foundationalism”, *The Journal of Philosophy*, 73: 165–185.

[^alston-1976b]: –––, 1976b, “Has Foundationalism Been Refuted?”, *Philosophical Studies*, 29: 287–305.

[^audi-1988]: Audi, Robert, 1988, *Belief, Justification and Knowledge*, Belmont: Wadsworth.

[^audi-1995]: –––, 1995, “Deductive Closure, Defeasibility and Scepticism: A Reply to Feldman”, *The Philosophical Quarterly*, 45(181): 494–499.

[^backes-2026]: Backes, Marvin, 2026, “Can Closure Be Saved? The Hardest Paradoxes for Closure Revisited”, *Synthese*, 207(1): Article 5. doi:10.1007/s11229-025-05386-9

[^baumann-2012]: Baumann, Peter, 2012, “Nozick’s Defense of Closure”, in Becker and Black (eds.) 2012: 11–27.

[^becker-2012]: Becker, Kelly, 2012, “Methods and How to Individuate Them”, in Becker and Black (eds.) 2012: 81–98.

[^becker-2012-2]: Becker, Kelly and Tim Black (eds.), 2012, *The Sensitivity Principle in Epistemology*, Cambridge: Cambridge University Press.

[^beebe-2009]: Beebe, James, 2009, “The Abductivist Reply to Skepticism”, *Philosophy and Phenomenological Research*, 79: 605–636.

[^bergmann-2004]: Bergmann, Michael, 2004, “Epistemic Circularity, Malignant and Benign”, *Philosophy and Phenomenological Research*, 69(3): 709–727.

[^bird-2007]: Bird, Alexander, 2007, “Justified Judging”, *Philosophy and Phenomenological Research*, 74(1): 81–110.

[^black-2008]: Black, Tim, 2008, “Defending a Sensitive Neo-Moorean Invariantism”, in Hendricks and Pritchard (eds.) 2007: 8–27.

[^brown-2004]: Brown, Jessica, 2004, “Wright on Transmission Failure”, *Analysis*, 64(1): 57–67.

[^brown-2005]: –––, 2005, “Doubt, Circularity, and the Moorean Response to the Skeptic”, *Philosophical Perspectives*, 19: 1–14.

[^brown-2018]: –––, 2018, *Fallibilism: Evidence and Knowledge*, Oxford: Oxford University Press.

[^carroll-1895]: Carroll, Lewis, 1895, “What the Tortoise Said to Achilles”, *Mind*, 4(14): 278–280.

[^carter-2024]: Carter, J. Adam, 2024, “Abduction, Skepticism, and Indirect Realism”, *Philosophical Studies*, first online 28 August 2024. doi:10.1007/s11098-024-02206-7

[^chandler-2010]: Chandler, Jake, 2010, “The Transmission of Support: A Bayesian Re-Analysis”, *Synthese*, 176: 333–343.

[^cohen-1988]: Cohen, Stewart, 1988, “How to be a Fallibilist”, *Philosophical Perspectives*, 2: 91–123.

[^cohen-2002]: –––, 2002, “Basic Knowledge and the Problem of Easy Knowledge”, *Philosophy and Phenomenological Research*, 65(2): 309–329.

[^cohen-2005]: –––, 2005, “Why Basic Knowledge is Easy Knowledge”, *Philosophy and Phenomenological Research*, 70(2): 417–430.

[^coliva-2014]: Coliva, Annalisa, 2014, “Moderatism, Transmission Failures, Closure, and Humean Scepticism”, in Dodd and Zardini (eds.) 2014: 248–270.

[^coliva-2015]: –––, 2015, *Extended Rationality: A Hinge Epistemology*, Basingstoke: Palgrave Macmillan.

[^comesaña-2017]: Comesaña, Juan, 2017, “On Sharon and Spectre’s Argument Against Closure”, *Philosophical Studies*, 174(4): 1039–1046.

[^davies-1998]: Davies, Martin, 1998, “Externalism, Architecturalism, and Epistemic Warrant,” in Crispin Wright, Barry Smith, and Cynthia Macdonald (eds.), *Knowing Our Own Minds*, Oxford: Oxford University Press, pp. 321–361.

[^davies-2000]: –––, 2000, “Externalism and Armchair Knowledge”, in Paul Boghossian and Christopher Peacocke (eds.), *New Essays on the A Priori*, Oxford: Oxford University Press, pp. 384–414.

[^davies-2003]: –––, 2003, “The Problem of Armchair Knowledge,” in Nuccetelli (ed.) 2003: 23–56.

[^derose-1995]: DeRose, Keith, 1995, “Solving the Skeptical Problem”, *The Philosophical Review*, 104(1): 1–52.

[^derose-2009]: –––, 2009, *The Case for Contextualism: Knowledge, Skepticism and Context* (Volume 1), Oxford: Oxford University Press.

[^derose-2010]: –––, 2010, “Insensitivity is Back, Baby!”, *Philosophical Perspectives*, 24(1): 161–187.

[^di-2014]: Di Bello, Marco, 2014, “Epistemic Closure, and Topics of Inquiry”, *Synthese*, 191: 3977–4002.

[^dodd-2014]: Dodd, Dylan and Elia Zardini (eds.), 2014, *Scepticism and Perceptual Justification*, Oxford: Oxford University Press.

[^dretske-1970]: Dretske, Fred, 1970, “Epistemic Operators”, *Journal of Philosophy*, 67(24): 1007–1023.

[^dretske-1971]: –––, 1971, “Conclusive Reasons”, *Australasian Journal of Philosophy*, 49: 1–22.

[^dretske-1983]: –––, 1983, *Knowledge and the Flow of Information*, Cambridge, MA: MIT Press.

[^dretske-2013]: –––, 2013, “The Case Against Closure”, in Steup, Turri, and Sosa (eds.) 2013, pp. 13–26.

[^ebert-2005]: Ebert, Philip, 2005, “Transmission of Warrant-Failure and the Notion of Epistemic Analyticity”, *Australasian Journal of Philosophy*, 83: 505–521.

[^engel-2021]: Engel, Mylan, 2021, “Lotteries, Knowledge, and Inconsistent Belief: Why You Know Your Ticket Will Lose”, *Synthese*, 198: 7891–7921.

[^fantl-2009]: Fantl, Jeremy and Matthew McGrath, 2009, *Knowledge in an Uncertain World*, Oxford: Oxford University Press.

[^feldman-1995]: Feldman, Richard, 1995, “In Defense of Closure”, *Philosophical Quarterly*, 45: 487–494.

[^fumerton-1995]: Fumerton, Richard, 1995, *Metaepistemology and Skepticism*, Lanham: Rowman & Littlefield.

[^goldman-1976]: Goldman, Alvin, 1976, “Discrimination and Perceptual Knowledge”, *Journal of Philosophy*, 73(20): 771–791.

[^goldstein-2024]: Goldstein, Simon and John Hawthorne, 2024, “Safety, Closure, and Extended Methods”, *Journal of Philosophy*, 121(1): 26–54.

[^goodman-2023]: Goodman, Jeremy and Bernhard Salow, 2023, “Epistemology Normalized”, *Philosophical Review*, 132(1): 89–145.

[^harman-1973]: Harman, Gilbert, 1973, *Thought*, Princeton: Princeton University Press.

[^hawthorne-2004]: Hawthorne, John, 2004, *Knowledge and Lotteries*, Oxford: Oxford University Press.

[^hawthorne-2013]: –––, 2013, “The Case for Closure”, in Steup, Turri, and Sosa (eds.) 2013: 40–55.

[^heller-1999]: Heller, Mark, 1999, “Relevant Alternatives and Closure”, *Australasian Journal of Philosophy*, 77(2): 196–208.

[^hendricks-2007]: Hendricks, Vincent and Duncan Pritchard (eds.), 2007, *New Waves in Epistemology*, Aldershot: Palgrave Macmillan.

[^holliday-2015]: Holliday, Wesley, 2015, “Epistemic Closure and Epistemic Logic I: Relevant Alternatives and Subjunctivism”, *Journal of Philosophical Logic*, 44(1): 1–63.

[^horn-2018]: Horn, Walter, 2018, “Epistemic Closure, Home Truths, and Easy Philosophy”, *Journal of Philosophy*, 115: 34–51.

[^huemer-2001]: Huemer, Michael, 2001, *Skepticism and the Veil of Perception*, Lanham: Rowman & Littlefield.

[^ichikawa-2014]: Ichikawa, Jonathan, 2014, “Justification is Potential Knowledge”, *Canadian Journal of Philosophy*, 44(2): 184–206.

[^jope-2021]: Jope, Matthew, 2021, “Closure, Credence and Rationality: A Problem for Non-Belief Hinge Epistemology”, *Synthese*, 198(S15): 3565–3575. doi:10.1007/s11229-019-02153-5

[^jope-2023]: –––, 2023, “Intuitive Closure, Transmission Failure, and Doxastic Justification”, in Jope and Pritchard (eds.) 2023: 6–23.

[^jope-2023-2]: Jope, Matthew and Duncan Pritchard (eds.), 2023, *New Perspectives on Epistemic Closure*, New York: Routledge.

[^kelp-2016]: Kelp, Christoph, 2016, “Justified Belief: Knowledge First-Style”, *Philosophy and Phenomenological Research*, 93: 79–100.

[^kelp-2023]: –––, 2023, “Dogma, Defeat, and Transmission”, in Jope and Pritchard (eds.) 2023: 97–112.

[^klein-1995]: Klein, Peter, 1995, “Skepticism and Closure: Why the Evil Genius Argument Fails”, *Philosophical Topics*, 23(1): 213–236.

[^klein-2004]: –––, 2004, “Closure Matters: Academic Skepticism and Easy Knowledge”, *Philosophical Issues*, 14: 165–184.

[^kripke-2011]: Kripke, Saul, 2011, “Nozick on Knowledge”, in Saul Kripke, *Philosophical Troubles, Collected Papers* (Volume 1), Oxford: Oxford University Press, pp. 161–224. doi:10.1093/acprof:oso/9780199730155.001.0001

[^kung-2010]: Kung, Peter, 2010, “On Having No Reason: Dogmatism and Bayesian Confirmation”, *Synthese*, 177: 1–17.

[^kyburg-1961]: Kyburg, Henry, 1961, *Probability and the Logic of Rational Belief*, Dordrecht: Kluwer.

[^lasonen-2008]: Lasonen, Maria, 2008, “Single-Premise Deduction and Risk”, *Philosophical Studies*, 141(2): 157–173.

[^lawlor-2005]: Lawlor, Krista, 2005, “Living Without Closure”, *Grazer Philosophische Studien*, 69: 25–50.

[^lawlor-2013]: –––, 2013, *Assurance: An Austinian View of Knowledge and Knowledge Claims*, Oxford: Oxford University Press.

[^lawlor-2023]: –––, 2023, “Modest Foundations for Perceptual Knowledge”, in Jope and Pritchard (eds.) 2023: 24–42.

[^leite-2015]: Leite, Adam, 2015, “Why Don’t I Know I’m Not a Brain in a Vat?” *Philosophy and Phenomenological Research*, 90(1): 205–13.

[^lewis-1973]: Lewis, David, 1973, *Counterfactuals*, Cambridge: Harvard University Press.

[^lewis-1996]: –––, 1996, “Elusive Knowledge”, *Australasian Journal of Philosophy*, 74(4): 549–567.

[^littlejohn-2012]: Littlejohn, Clayton, 2012, *Justification and the Truth Connection*, Cambridge: Cambridge University Press.

[^littlejohn-2020]: Littlejohn, Clayton and Julien Dutant, 2020, “Justification, Knowledge, and Normality”, *Philosophical Studies*, 177(6): 1593–609.

[^luper-1984]: Luper, Steven, 1984, “The Epistemic Predicament: Knowledge, Nozickian Tracking, and Scepticism”, *Australasian Journal of Philosophy*, 62(1): 26–49.

[^luper-2006]: –––, 2006, “Dretske on Knowledge Closure”, *Australian Journal of Philosophy*, 84(3): 379–394. doi:10.1080/00048400600895862

[^luper-foy-1987]: Luper-Foy, Stephen (ed.), 1987, *The Possibility of Knowledge: Nozick and his Critics*, Totowa: Rowman & Littlefield.

[^makinson-1965]: Makinson, D. C., 1965, “The Paradox of the Preface”, *Analysis*, 25(6): 205–207.

[^markie-2005]: Markie, Peter, 2005, “Easy Knowledge”, *Philosophy and Phenomenological Research*, 70(2): 406–416.

[^mccain-2019]: McCain, Kevin, 2019, “In Defense of the Explanationist Response to Skepticism”, *International Journal for the Study of Skepticism*, 9(1): 38–50.

[^mcdowell-1986]: McDowell, John, 1986, “Singular Thought and the Extent of Inner Space”, in Philip Pettit and John McDowell (eds.), *Subject, Thought, and Context*, Oxford: Clarendon Press, pp. 137–168.

[^mcdowell-1995]: –––, 1995, “Knowledge and the Internal”, *Philosophy and Phenomenological Research*, 55(4): 877–893.

[^mcglynn-2014a]: McGlynn, Aidan, 2014a, “On Epistemic Alchemy”, in Dodd and Zardini (eds.) 2014: 173–188.

[^mcglynn-2014b]: –––, 2014b, *Knowledge First?* London: Palgrave Macmillan.

[^mckinsey-2003]: McKinsey, Michael, 2003, “Transmission of Warrant and Closure of Apriority”, in Nuccetelli (ed.) 2003: 97–115.

[^mclaughlin-2000]: McLaughlin, Brian, 2000, “Skepticism, Externalism, and Self-Knowledge”, *The Proceedings of the Aristotelian Society* (Supplementary Volume), 74: 93–118.

[^mclaughlin-2003]: –––, 2003, “McKinsey’s Challenge, Warrant Transmission, and Skepticism”, in Nuccetelli (ed.) 2003: 79–96.

[^montessori-2025]: Montessori, Auke, 2025, “Single Premise Deduction and Defeat”, *Erkenntnis*, first online 11 October 2025. doi:10.1007/s10670-025-01024-5

[^moore-1939]: Moore, G. E., 1939 [1959], “Proof of an External World”, *Proceedings of the British Academy*, 25: 273–300; reprinted in G. E. Moore, *Philosophical Papers*, New York, NY: Collier, pp. 144–148.

[^moretti-2012]: Moretti, Luca, 2012, “Wright, Okasha and Chandler on Transmission Failure”, *Synthese*, 184: 217–234.

[^moretti-2023]: Moretti, Luca and Tommaso Piazza, “Transmission of Justification and Warrant”, *The Stanford Encyclopedia of Philosophy* (Summer 2023 Edition), Edward N. Zalta and Uri Nodelman (eds.), URL = <[https://plato.stanford.edu/archives/sum2023/entries/transmission-justification-warrant/](https://plato.stanford.edu/archives/sum2023/entries/transmission-justification-warrant/)>.

[^moretti-2023-2]: Moretti, Luca and Crispin Wright, 2023, “Epistemic Entitlement, Epistemic Risk, and Leaching”, *Philosophy and Phenomenological Research*, 106(3): 566–580. doi:10.1111/phpr.12874

[^murphy-2005]: Murphy, Peter, 2005, “Closure Failures for Safety”, *Philosophia*, 33: 331–334.

[^murphy-2012]: Murphy, Peter and Tim Black, 2012, “Sensitivity Meets Explanation: An Improved Counterfactual Condition on Knowledge”, in Becker and Black (eds.) 2012: 28–42.

[^nelkin-2000]: Nelkin, Dana, 2000, “The Lottery Paradox, Knowledge, and Rationality”, *The Philosophical Review*, 109(3): 373–409.

[^nozick-1981]: Nozick, Robert, 1981, *Philosophical Explanations*, Cambridge: Harvard University Press.

[^nuccetelli-2003]: Nuccetelli, Susana (ed.), 2003, *New Essays on Semantic Externalism and Self-Knowledge*, Cambridge: MIT Press.

[^okasha-2004]: Okasha, Samir, 2004, “Wright on the Transmission of Support: A Bayesian Analysis”, *Analysis*, 64: 139–146.

[^plantinga-1993a]: Plantinga, Alvin, 1993a, *Warrant: The Current Debate*, Oxford: Oxford University Press.

[^plantinga-1993b]: –––, 1993b, *Warrant and Proper Function*, Oxford: Oxford University Press.

[^pritchard-2007a]: Pritchard, Duncan, 2007a, “Knowledge, Luck and Lotteries”, in Hendricks and Pritchard (eds.) 2007: 28–51.

[^pritchard-2007b]: –––, 2007b, “Anti-Luck Epistemology”, *Synthese*, 158(3): 277–297.

[^pritchard-2009a]: –––, 2009a, “Sensitivity, Safety, and Anti-Luck Epistemology”, in John Greco (ed.), *The Oxford Handbook of Scepticism*, Oxford: Oxford University Press, pp. 437–455.

[^pritchard-2009b]: –––, 2009b, “Safety-Based Epistemology: Whither Now?”, *Journal of Philosophical Research*, 34: 33–45.

[^pritchard-2012]: –––, 2012, *Epistemological Disjunctivism*, Oxford: Oxford University Press.

[^pritchard-2016]: –––, 2016, *Epistemic Angst*, Princeton: Princeton University Press.

[^pritchard-2018]: –––, 2018, “Epistemic Angst”, *Philosophical and Phenomenological Research*, 96(1): 70–90. doi:10.1111/phpr.12280

[^pritchard-2023]: –––, 2023, “In Defence of Closure”, in Jope and Pritchard (eds.) 2023: 113–130.

[^pryor-2000]: Pryor, James, 2000, “The Skeptic and the Dogmatist”, *Noûs*, 34(4): 517–549.

[^pryor-2004]: –––, 2004, “What’s Wrong with Moore’s Argument?”, *Philosophical Issues*, 14: 349–378.

[^pryor-2012]: –––, 2012, “When Warrant Transmits”, in Annalisa Coliva (ed.), *Mind, Meaning, and Knowledge: Themes from the Philosophy of Crispin Wright*, Oxford: Oxford University Press, pp. 269–303.

[^pryor-2013]: –––, 2013, “Problems for Credulism”, in Chris Tucker (ed.), *Seemings and Justification: New Essays on Dogmatism and Phenomenal Conservatism*, New York: Oxford University Press, pp. 89–131.

[^reynolds-2013]: Reynolds, Stephen, 2013, “Justification as the Appearance of Knowledge”, *Philosophical Studies*, 163: 367–383.

[^rosenkranz-2018]: Rosenkranz, Sven, 2018, “The Structure of Justification”, *Mind*, 127: 309–338.

[^roush-2005]: Roush, Sherrilyn, 2005, *Tracking Truth: Knowledge, Evidence and Science*, Oxford: Oxford University Press.

[^roush-2010]: –––, 2010, “Closure on Skepticism”, *Journal of Philosophy*, 107(5): 243–256.

[^roush-2012]: –––, 2012, “Sensitivity and Closure”, in Becker and Black (eds.) 2012: 242–268.

[^schaffer-2004]: Schaffer, Jonathan, 2004, “From Contextualism to Contrastivism”, *Philosophical Studies*, 119: 73–103.

[^schaffer-2007]: –––, 2007, “Closure, Contrast, and Answer”, *Philosophical Studies*, 133: 233–255.

[^schechter-2013]: Schechter, Joshua, 2013, “Rational Self-Doubt and the Failure of Closure”, *Philosophical Studies*, 163: 429–452.

[^sharon-2017a]: Sharon, Aasaf and Levi Spectre, 2017a, “Evidence and the Openness of Knowledge”, *Philosophical Studies*, 174: 1001–1037.

[^sharon-2017b]: –––, 2017b, “Replies to Comesaña and Yablo”, *Philosophical Studies*, 174: 1073-1090.

[^sherman-2011]: Sherman, Brett and Gilbert Harman, 2011, “Knowledge and Assumptions”, *Philosophical Studies*, 156: 131–140.

[^silins-2005]: Silins, Nicholas, 2005, “Transmission Failure Failure”, *Philosophical Studies*, 126: 71–102.

[^silva-2017]: Silva, Paul, 2017, “Knowing How to Put Knowledge First in the Theory of Justification”, *Episteme*, 14(4): 393–412.

[^simion-2019]: Simion, Mona, 2019, “Knowledge‐First Functionalism”, *Philosophical Issues*, 29(1): 254–267.

[^simion-2023]: –––, 2023, “Closure, Warrant Transmission, and Defeat”, in Jope and Pritchard (eds.) 2023: 43–57.

[^simpson-2021]: Simpson, James, 2021, “Getting a Little Closure for Closure”, *Synthese*, 199: 12331–12361.

[^smith-2009]: Smith, Martin, 2009, “Transmission Failure Explained”, *Philosophy and Phenomenological Research*, 79: 164–189.

[^smith-2010]: –––, 2010, “What Else Justification Could Be”, *Noûs*, 44: 10–31.

[^smith-2014]: –––, 2014, “Knowledge, Justification, and Normative Coincidence”, *Philosophy and Phenomenological Research*, 89: 276–295.

[^smith-2016a]: –––, 2016a, *Between Probability and Certainty: What Justifies Belief*, Oxford: Oxford University Press.

[^smith-2016b]: –––, 2016b, “Scepticism by a Thousand Cuts”, *International Journal for the Study of Skepticism*, 6(1): 44–52.

[^smith-2021]: –––, 2021, “Four Arguments for Denying that Lottery Beliefs Are Justified”, in Igor Douven (ed.), *Lotteries, Knowledge, and Rational Belief: Essays on the Lottery Paradox*, Cambridge: Cambridge University Press, pp. 95–109.

[^smith-2022]: –––, 2022, “The Hardest Paradox for Closure”, *Erkenntnis*, 87: 2003–2028.

[^smith-2025]: –––, 2025, “Justification, Normalcy, and Randomness”, *Philosophy and Phenomenological Research*, 110: 442–459.

[^smithies-2012]: Smithies, Declan, 2012, “The Normative Role of Knowledge”, *Noûs*, 46(2): 265–288.

[^sosa-1999]: Sosa, Ernest, 1999, “How to Defeat Opposition to Moore,” *Philosophical Perspectives*, 13: 141–152.

[^sorensen-1988]: Sorensen, Roy, 1988, “Dogmatism, Junk Knowledge and Conditionals,” *The Philosophical Quarterly*, 38: 433–454.

[^stalnaker-1968]: Stalnaker, Robert, 1968, “A Theory of Conditionals”, *American Philosophical Quarterly*, 2: 98–112.

[^stanley-2008]: Stanley, Jason, 2008, *Knowledge and Practical Interests*, Oxford: Clarendon Press.

[^steup-2013]: Steup, Matthew, John Turri, and Ernest Sosa (eds.), 2013, *Contemporary Debates in Epistemology*, 2nd edition, Oxford: Blackwell.

[^sutton-2007]: Sutton, Jonathan, 2007, *Without Justification*, Cambridge: MIT Press.

[^tang-2018]: Tang, Weng Hong, 2018, “In Defence of Single-Premise Closure”, *Philosophical Studies*, 175: 1887–1900.

[^thomasson-2014]: Thomasson, Amie, 2014, *Ontology Made Easy*, Oxford: Oxford University Press.

[^veber-2004]: Veber, Michael, 2004, “What Do You Do With Misleading Evidence?”, *The Philosophical Quarterly*, 54: 557–569.

[^veber-2013]: –––, 2013, “The Argument from Abomination”, *Erkenntnis*, 78: 1185–1196.

[^vogel-1987]: Vogel, Jonathan, 1987, “Tracking, Closure, and Inductive Knowledge”, in Luper-Foy (ed.) 1987: 197–215.

[^vogel-1990a]: –––, 1990a, “Are There Counterexamples to the Closure Principle?”, in Michael Roth and Glenn Ross (eds.), *Doubting: Contemporary Perspectives on Skepticism*, Dordrecht: Kluwer Academic Publishers, pp. 13–29.

[^vogel-1990b]: –––, 1990b, “Cartesian Skepticism and Inference to the Best Explanation”, *Journal of Philosophy*, 87: 658–666.

[^vogel-2000]: –––, 2000, “Reliabilism Leveled”, *Journal of Philosophy*, 97: 602–623.

[^warfield-2008]: Warfield, Ted and David Marian, 2008, “Knowledge-Closure and Skepticism”, in Quentin Smith (ed.), *Epistemology: New Essays*, Oxford: Oxford University Press, pp. 137–188.

[^white-2006]: White, Roger, 2006, “Problems for Dogmatism”, *Philosophical Studies*, 131: 525–557.

[^williamson-2000]: Williamson, Timothy, 2000, *Knowledge and its Limits*, Oxford: Oxford University Press.

[^williamson-2009a]: –––, 2009a, “Probability and Danger”, *The Amherst Lecture in Philosophy*, 4: 1–35.

[^williamson-2009b]: –––, 2009b, “Replies to Critics”, in Peter Greenough and Duncan Pritchard (eds.), *Williamson on Knowledge*, Oxford: Oxford University Press, pp. 279–384.

[^williamson-2014]: –––, 2014, “Very Improbable Knowing”, *Erkenntnis*, 79: 971–999.

[^williamson-2023]: –––, 2023, “Modal Epistemology and the Logic of Counterfactuals”, in Jope and Pritchard (eds.) 2023: 58–76.

[^williamson-2025]: –––, 2025, “Justifications, Excuses, and Skeptical Scenarios”, in Timothy Williamson, *Good as Usual: Anti-Exceptionalist Essays on Values, Norms, and Action*, Oxford: Oxford University Press, pp. 149–166.

[^wittgenstein-1969]: Wittgenstein, Ludwig, 1969, *On Certainty*, Oxford: Basil Blackwell.

[^wright-1985]: Wright, Crispin, 1985, “Facts and Certainty”, *Proceedings of the British Academy*, 71: 429–472.

[^wright-2000]: –––, 2000, “Cogency and Question-Begging: Some Reflections on McKinsey’s Paradox and Putnam’s Proof”, *Philosophical Issues*, 10: 140–63.

[^wright-2002]: –––, 2002, “(Anti-) Sceptics Simple and Subtle: G. E. Moore and John McDowell”, *Philosophy and Phenomenological Research*, 65(2): 330–348.

[^wright-2003]: –––, 2003, “Some Reflections on the Acquisition of Warrant by Inference”, in Nuccetelli (ed.) 2003: 57–78.

[^wright-2004]: –––, 2004, “*I—Crispin Wright* : Warrant for Nothing (and Foundations for Free)?”, *The Proceedings of the Aristotelian Society* (Supplementary Volume), 78(1): 167–212. doi:10.1111/j.0309-7013.2004.00121.x

[^wright-2008]: –––, 2008, “The Perils of Dogmatism,” in Susana Nuccetelli and Gary Seay (eds.), *Themes from G. E. Moore: New Essays in Epistemology and Ethics*, Oxford: Oxford University Press, pp. 25–48.

[^wright-2011]: –––, 2011, “McKinsey One More Time”, in Anthony Hatzimoysis (ed.), *Self-Knowledge*, Oxford: Oxford University Press, pp. 80–104. doi:10.1093/acprof:oso/9780199590728.003.0005

[^wright-2012]: –––, 2012, “Replies”, in Annalisa Coliva (ed.), *Mind, Meaning and Knowledge: Themes from the Philosophy of Crispin Wright*, Oxford: Oxford University Press, pp. 377–486.

[^wright-2014]: –––, 2014, “On Epistemic Entitlement (II): Welfare State Epistemology”, in Dodd and Zardini (eds.) 2014: 213–247.

[^wright-2023]: –––, 2023, “Closure and Transmission Again”, in Jope and Pritchard (eds.) 2023: 163–190.

[^yablo-2014]: Yablo, Stephen, 2014, *Aboutness*, Princeton: Princeton University Press.

[^yablo-2017]: –––, 2017, “Open Knowledge and Changing the Subject”, *Philosophical Studies*, 174: 1047–1071.

[^zalabardo-2014]: Zalabardo, José, 2014, “Inference and Skepticism”, in Dodd and Zardini (eds.) 2014: 108–126.

[^zhao-2022]: Zhao, Bin, 2022, “Sensitivity, Safety, and Epistemic Closure”, *International Journal of Philosophical Studies*, 30(1): 56–71.

[^zhang-2021]: Zhang, Xiaoxing, 2021, “Closure, Deduction and Hinge Commitments”, *Synthese*, 198(S15): 3533–3551. doi:10.1007/s11229-018-1679-x
