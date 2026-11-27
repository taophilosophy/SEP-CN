# Liar Paradox
**First published Thu Jan 20, 2011; substantive revision Sun Jul 26, 2026**

*Beall, Jc, Glanzberg, Michael, Ripley, Ellie, Rossi, Lorenzo*

The first sentence in this essay is a lie. There is something odd about saying so, as has been known since ancient times. To see why, remember that all lies are untrue. Is the first sentence true? If it is, then it is a lie, and so it is not true. Conversely, suppose that it is not true. We (viz., the authors) have said it, and normally things are said with the intention of being believed. Saying something that way when it is untrue is a lie. But then, given what the sentence says, it is true after all!

That there is some sort of puzzle to be found with sentences like the first one of this essay has been noted frequently throughout the history of philosophy. It was discussed in classical times, notably by the Megarians, but it was also mentioned by Aristotle and by Cicero. As one of the insolubilia, it was the subject of extensive investigation by medieval logicians such as Buridan. More recently, work on this problem has been an integral part of the development of modern mathematical logic, and it has become a subject of extensive research in its own right. The paradox is sometimes called the ‘Epimenides paradox’ as the tradition attributes a sentence like the first one in this essay to Epimenides of Crete, who is reputed to have said that all Cretans are always liars. That some Cretan has said so winds up in no less a source than New Testament![^note-1]

Lying is a complicated matter, but what’s puzzling about sentences like the first one of this essay isn’t essentially tied to intentions, social norms, or anything like that. Rather, it seems to have something to do with truth, or at least, some semantic notion related to truth. The puzzle is usually named ‘the Liar paradox’, though this really names a family of paradoxes that are associated with our type of puzzling sentence. The family is aptly named one of *paradoxes*, as they seem to lead to incoherent conclusions, such as: “everything is true”. Indeed, the Liar seems to allow us to reach such conclusions on the basis of logic, basic syntax, and some very obvious semantic principles that have sometimes been counted as principles of logic. Thus, we have the rather surprising situation of something near or like logic alone leading us to incoherence. This is perhaps the most virulent strain of paradox, and dealing with it has been an important task in logic for about as long as there has been logic.

In this essay, we will review the important members of the family of Liar paradoxes, and some of the important ideas about how these paradoxes might be resolved. The past few thousand years have yielded a great number of proposals, and we will not be able to examine all of them; instead, we will focus on a few that have, in recent discussions, proved to be important.

## 1. The Paradox and the Broader Phenomenon

### 1.1 Simple-falsity Liar

Consider a sentence named ‘FLiar’, which says of itself (i.e., says of FLiar) that it is false.

**FLiar**:

FLiar is false.

This seems to lead to contradiction as follows. If the sentence ‘FLiar is false’ is true, then given what it says, FLiar is false. But FLiar just is the sentence ‘FLiar is false’, so we can conclude that if FLiar is true, then FLiar is false. Conversely, if FLiar is false, then the sentence ‘FLiar is false’ is true. Again, FLiar just is the sentence ‘FLiar is false’, so we can conclude that if FLiar is false, then FLiar is true. We have thus shown that FLiar is false if and only if FLiar is true. But, now, if every sentence is true or false, FLiar itself is either true or false, in which case—given our reasoning above—it is both true and false. This is a contradiction. Contradictions, according to many logical theories (e.g., classical logic, intuitionistic logic, and many others) imply triviality, that is, that every sentence is true.

An obvious response is to deny that every sentence is true or false, i.e., to deny the principle of bivalence. As we will discuss in §4, some descendants of this idea remain important in current work on the Liar. Even so, a simple variant Liar sentence shows that this immediate answer is not all there is to the story.

### 1.2 Simple-untruth Liar

Rather than work with falsehood, we can construct a Liar sentence with the complex predicate ‘not true’.[^note-2] Consider a sentence named ‘ULiar’ (for ‘un-true’), which says of itself that it is not true.

**ULiar**:

ULiar is not true.

The argument towards contradiction is similar to the FLiar case. In short: if ULiar is true, then it is not true; and if it is not true, then it is true. But, now, if every sentence is true or not true, ULiar itself is true or not true, in which case it is both true and not true. This is a contradiction. According to many logical theories, a contradiction implies triviality. The main difference between FLiar and ULiar is that, unlike FLiar, ULiar gives rise to a paradox even if one rejects bivalence. Suppose one rejects the assumption that every sentence is true or false (but not both), and accepts that some sentences are neither true nor false. Even so, every sentence is either true or something other than true, i.e. not true. In this way, ‘not true’ encompasses everything that fails to qualify as true: both false sentences and those that are neither true nor false. As a result, blocking ULiar in a way that is analogous to the rejection of bivalence requires logical assumptions concerning negation.

We also briefly note that simply giving up the Law of Excluded Middle is not enough to deal with the ULiar, since there are versions of the reasoning to triviality via the ULiar that do not rely on Excluded Middle, but rather on Reductio (also called Negation Introduction). Suppose that ULiar is true. Since it is true, we can conclude ULiar. But, given what ULiar says, ULiar is not true. This contradicts our assumption, so, by Reductio, we conclude from no premises that ULiar is not true. But this is what ULiar says, so we conclude ULiar, from which we infer that ULiar is true, which is a contradiction.

The two forms of the Liar paradox we have so far reviewed rely on some explicit self-reference—sentences talking directly about themselves. Such explicit self-reference can be avoided, as is shown by our next family of Liar paradoxes.

### 1.3 Liar cycles

Consider a very concise (viz., one-sentence-each) dialog between siblings Max and Agnes.

**Max**:

Agnes’ claim is true.

**Agnes**:

Max’s claim is not true.

What Max said is true if and only if what Agnes said is true. But what Agnes said (viz., ‘Max’s claim is not true’) is true if and only if what Max said is not true. Hence, what Max said is true if and only if what Max said is not true. But, now, if what Max said is true or not true, then it is both true and not true. And this, as in the FLiar and ULiar cases, is a contradiction, implying, according to many logical theories, absurdity.

Liar paradoxes can also be formed using more complex sentence structures, rather than complex modes of reference. One that has been important involves Boolean compounds.

### 1.4 Boolean compounds

Boolean compounds (i.e., constructions using conjunction and disjunction, in addition to negation) can enter into Liar sentences in many ways. One relatively simple one is as follows. Consider the following sentence named ‘DLiar’ (for ‘Disjunctive’).

**DLiar**:

Either DLiar is not true or $1 = 0$.

First, observe that if DLiar is not true, then it must be true. If DLiar is not true, then by similar reasoning to what we saw above, we have that the left disjunct of DLiar is true. But a disjunction is true if one of its disjuncts is, so DLiar is true. Thus, if DLiar is not true, it is true and not true, and we have a contradiction. By Classical Reductio, then, it must be true; so one of its disjuncts must be true. If it’s the first one, we have a contradiction, so it must be the second one; we can conclude that $1 = 0$. We have thus proved that $1 = 0$. Moreover, the sentence ‘$1 = 0$’ played no real role in the above reasoning. We could replace it with any other sentence to get a proof of that sentence.

We pause to mention DLiar as it is connected with another important paradox: Curry’s paradox, which involves conditionals that say of themselves only that if they (the conditional itself) are true, so too is some absurdity (e.g., ‘if this sentence is true, then $1 = 0$’ or ‘if this sentence is true, everything is true’ or so on). At least in languages where the conditional is the material conditional, and so $A \supset B$ is equivalent to $\neg A \vee B$, DLiar is equivalent to the Curry sentence ‘DLiar is true $\supset$ $1 = 0$’. Though this may set up some relations between the Liar and Curry’s paradox, we pause to note an important difference. For the Curry paradox is most important where the conditional is more than the material conditional (or some modalized variant of it). In such settings, the Curry paradox does not wear negation on its sleeve, as DLiar does, since we cannot assume that the conditional is equivalent to the material conditional, or that it involves negation at all. For more information, consult the entry on Curry’s paradox.

### 1.5 Infinite sequences

The question of whether the Liar paradox really requires some sort of circularity has been the subject of extensive debate. Liar cycles (e.g., the Max–Agnes dialog) show that explicit self-reference is not necessary, but it is clear that such cycles themselves involve circular reference. Yablo (1993b)[^yablo-1993b] has argued that a more complicated kind of multi-sentence paradox produces a Liar without circularity. (Similar paradoxical constructions had already been discussed in Visser (1984)[^visser-1984] and Yablo (1985)[^yablo-1985].)

Yablo’s paradox relies on an infinite sequence of claims $A_0$, $A_1$, $A_2$, …, where each $A_i$ says that all of the ‘greater’ $A_k$ (i.e., the $A_k$ such that $k \gt i)$ are untrue. (In other words, each claim says of the rest that they’re all untrue.) Since we have an infinite sequence, this version of the Liar paradox appears to avoid the sort of circularity apparent in the previous examples; however, contradiction still seems to emerge. If $A_0$ is true, then all of the ‘greater’ $A_k$ are untrue, and *a fortiori* $A_1$ is untrue. But, then, there is at least one true $A_k$ with $k > 1$, which contradicts $A_0$. Conversely, if $A_0$ is untrue, then there’s at least one true $A_k$ greater than $A_0$. Letting $A_m$ be such a one (i.e., a truth greater than $A_0)$, we have it that $A_{m+1}$ is untrue, in which case there’s some truth greater than $A_{m+1}$. But this contradicts $A_m$. What we have, then, is that if $A_0$ (the first claim in the infinite sequence) is true or untrue, then it is both. And this, as in the other cases, is a contradiction.

Whether Yablo’s paradox really avoids self-reference is much-debated. See, for instance, Barrio (2012)[^barrio-2012], Beall (2001)[^beall-2001], Cook (2006, 2014)[^cook-2006][^cook-2014], Ojea (2012)[^ojea-2012], Picollo (2012)[^picollo-2012], Priest (1997)[^priest-1997], Sorensen (1998)[^sorensen-1998], and Teijeiro (2012)[^teijeiro-2012].

## 2. Basic Ingredients

We have already seen a kind of characteristic reasoning that goes with the Liar. We have also seen some common structure across all our example Liar paradoxes, such as the presence of truth predicates, and something like negation (note that the falsity of a sentence is typically defined as the truth of its negation). We pause here to discuss these ingredients of the paradox, focusing on the *basic* Liars. Just what creates the Liar paradox, and just which of the puzzles we just surveyed is ‘basic’, is a contentious matter; different approaches to solving the Liar view these matters differently. Hence, our goal is merely to illuminate some common themes across different Liars, not to offer a full diagnosis of the source of the paradox.

We highlight three aspects of the Liar: the role of truth predicates, the kinds of principles for reasoning about truth that are needed, and the way that a paradox can be derived given these resources.

### 2.1 Truth predicate

The first ingredient in building a Liar is a truth predicate, which we write here as $\Tr$. Since the truth predicate is a predicate, it applies to terms. However, we are mostly interested in terms that denote formulas and, most of the time, closed formulas, i.e. sentences. In natural language, such terms can be obtained by placing a sentence within quotation marks, as in ‘snow is white’. In suitable formal languages and theories, one can likewise define terms that simulate the role of quotation: they denote objects that encode formulas. Accordingly, we assume that, alongside the truth predicate, the language contains appropriate names of formulas. For a given formula *A*, we let $\left\ulcorner A\right\urcorner$ be a name for it. A predication of truth to *A* then looks like $\Tr(\left\ulcorner A\right\urcorner)$. Since *A* is a formula, and $\ulcorner A \urcorner$ is a term, $\Tr\ulcorner A \urcorner$ is a well-formed formula of our language. Before proceeding, however, and especially as we come to consider some ways of resolving the Liar, we should note that this treatment of truth ascriptions is adopted for convenience in exposition, and does not presuppose any particular view about what the primary bearers of truth are.

We typically expect $\Tr$ to obey some principles governing its behavior on sentences of a given language. It is to those we now turn.[^note-3]

### 2.2 Principles of truth

The tradition, going back to Tarski (1935)[^tarski-1935], is that the behavior of the truth predicate $\Tr$ is described by the following biconditional.

$$\Tr(\left\ulcorner A\right\urcorner) \leftrightarrow A.$$

Indeed, Tarski took the biconditional here to be the material biconditional of classical logic. However, nothing in the above principle forces $\leftrightarrow$ to be the classical biconditional, and the principle is still intelligible for a variety of non-classical options. This principle is usually called the *T-schema*. For more on the T-schema, and Tarski’s views of truth, see the entries on Alfred Tarski and Tarski’s truth definitions.

The Liar paradox has been a locus of thinking about non-classical logics (as we already saw a taste of, for instance, in the idea that bivalence might be rejected as part of a solution to the Liar). Thus, we should stop to consider what principles should govern the truth predicate $\Tr$ if classical logic is not to hold.

The leading idea for what might replace the T-schema points to two sorts of ‘rules’ (e.g., two sorts of ‘inference rules’ in some sense) or principles that are characteristic of the truth predicate. If you have a sentence *A*, you can infer $\Tr(\left\ulcorner A\right\urcorner)$, that is, you can ‘capture’*A* with the truth predicate. Conversely, if you have $\Tr(\left\ulcorner A\right\urcorner)$, you can infer *A*, that is, you can ‘release’*A* from the truth predicate. In some logics, capture and release wind up being equivalent to the T-schema, but it is often helpful to break these up:

**Capture**

*A* implies $\Tr(\left\ulcorner A\right\urcorner)$. (We also write this as $A \vdash \Tr(\left\ulcorner A\right\urcorner)$.)

**Release**

$\Tr(\left\ulcorner A\right\urcorner)$ implies *A*. (We also write this as $\Tr(\left\ulcorner A\right\urcorner) \vdash A$.)

*Implies* here is a logical notion, though just which one, and what the options are, depends on what background logic is assumed. For our discussion, we think of it in so-called rule form: that the argument from *A* to *B* is valid, which we record (as above) via the turnstile. In some logical settings (e.g., classical logic, in which the so-called Deduction Theorem holds), this is equivalent to the provability of a conditional, but in some settings, it is not. Either way, capture and release jointly make *A* and $\Tr(\left\ulcorner A\right\urcorner)$ logically equivalent in the sense of being interderivable. In strong forms, capture and release can lead to the full intersubstitutability of *A* and $\Tr(\left\ulcorner A\right\urcorner)$ in extensional contexts. As we discuss more in section 4.1, this is important to some views of the nature of truth. Thus, $\vdash$ is being used here as a schematic placeholder for a range of different logical notions, each of which will provide some notion of valid inference in some logical theory.

(There are a number of logical subtleties here that we will not pursue, especially about how to formulate rules, and which rules are consistent. Different formulations of rules vary significantly in logical strength as well.[^note-4] See the entry on axiomatic theories of truth for more on how consistent forms of capture and release can be formulated in classical logic. In the terminology of Friedman and Sheard (1987), the rule forms of capture and release are called ‘T-Intro’ and ‘T-Elim’, and the conditional forms ‘T-In’ and ‘T-Out’. We prefer the broader terminology, since it highlights a general form of behavior common to a great variety of predicates and operators, e.g., *knowledge* releases but doesn’t capture; *possibility* captures but doesn’t release; and so on; and truth is special in doing both.)

### 2.3 The Liar in short

The Liar paradox begins with a language containing a truth predicate, which obeys some form of capture and release. We now explore more carefully how a paradox results from these assumptions.

#### 2.3.1 Existence of Liar-like sentences

Putting aside Yablo-type paradoxes, the Liar relies on some form of self-reference, either direct, as in the simple Liars above, or indirect, as in Liar cycles. Most natural languages have little trouble generating self-reference. The first sentence of this essay is one example. Self-reference can be accidental, as in the case where someone writes ‘The only sentence on the blackboard in room 101 is not true’, by chance writing this in room 101 itself (as C. Parsons (1974)[^parsons-1974] noted).

In formal languages, self-reference is also very easy to come by. Any language capable of expressing some basic syntax can generate self-referential sentences via so-called diagonalization (or more properly, any language together with an appropriate theory of syntax or arithmetic).[^note-5] A language containing a truth predicate and this basic syntax will thus have a sentence *L* such that *L* implies $\neg \Tr(\left\ulcorner L\right\urcorner)$ and *vice versa*:

$$L \dashv \vdash \neg \Tr(\left\ulcorner L\right\urcorner).$$

This is a ‘fixed point’ of (the compound predicate) $\neg\Tr$, and is, in effect, our simple-untruth Liar.

(Technically, it is simplest to put the fixed point property in terms of implications, as we have done here. But intuitively, the idea is that somehow *L* ‘just is’ $\neg \Tr(\left\ulcorner L\right\urcorner)$. This can be made more precise, if we think of the Liar sentence *L* arising from a *name* *c* that denotes the sentence $\neg \Tr(c)$. In this way, we can think of the existence of the Liar as being reflected in the identity $c = \left\ulcorner \neg \Tr(c)\right\urcorner$. For more on the details of this approach, see Heck 2012, 2026.)

#### 2.3.2 Other logical ‘laws’

Other conspicuous ingredients in common Liar paradoxes concern logical behavior of basic connectives or features of implication. A few of the relevant principles are:

- Excluded middle (LEM): $\vdash A \vee \neg A$.
- Explosion (EFQ):[^note-6] $A,\neg A \vdash B$.
- Disjunction principle (DP):[^note-7] If $A \vdash C$ and $B \vdash C$ then $A \vee B \vdash C$.
- Adjunction: If $A \vdash B$ and $A \vdash C$ then $A \vdash B \wedge C$.

(This is not to suggest that these are the *only* logical features involved in common Liar paradoxes, but they’re arguably the most important of the salient ones.)

#### 2.3.3 The Liar in abstract

Given the foregoing ingredients, we can now give a slightly more abstract form of the paradox. (Our hope is to use this abstract form to highlight different responses to the paradox.) We suppose that we have a language $\mathcal{L}$ with a truth predicate $\Tr$, and that $\mathcal{L}$ allows enough syntax to construct a sentence *L* such that $L \dashv \vdash \neg \Tr(\left\ulcorner L\right\urcorner)$. We also suppose that the logic of $\mathcal{L}$ enjoys LEM and EFQ and satisfies DP and adjunction.

An argument that our Liar sentence *L* implies a contradiction runs as follows.

1. $\Tr(\left\ulcorner L\right\urcorner) \vee \neg \Tr(\left\ulcorner L\right\urcorner)$ [LEM]
2. Case One:
3. $\Tr(\left\ulcorner L\right\urcorner)$
4. *L* [2a: release]
5. $\neg \Tr(\left\ulcorner L\right\urcorner)$ [2b: definition of *L*]
6. $\neg \Tr(\left\ulcorner L\right\urcorner) \wedge \Tr(\left\ulcorner L\right\urcorner)$ [2a, 2c: adjunction]
7. Case Two:
8. $\neg \Tr(\left\ulcorner L\right\urcorner)$
9. *L* [3a: definition of *L*]
10. $\Tr(\left\ulcorner L)\right\urcorner)$ [3b: capture]
11. $\neg \Tr(\left\ulcorner L\right\urcorner) \wedge \Tr(\left\ulcorner L\right\urcorner)$ [3a, 3c: adjunction]
12. $\neg \Tr(\left\ulcorner L\right\urcorner) \wedge \Tr(\left\ulcorner L\right\urcorner)$ [1–3: DP]

This version of the Liar is one of many. With a little more complexity, for instance, either capture or release can be avoided in favor of some other background assumptions. Intuitionistic variants of the Liar are also available, though we shall not explore intuitionistic logic here.[^note-8]

We have so far shown that with the given ingredients our Liar sentence *L* implies a contradiction (thus formalizing the reasoning in ULiar). From here, it is one short step to all-out absurdity—if the lone contradiction weren’t already absurd enough. We invoke EFQ to finish the proof. (Well, we also assume that $A \wedge B$ implies *A* and *B*, i.e., that simplification is valid in $\mathcal{L}$; but in fact this assumption is not really necessary.)

1. *B* [4: EFQ]

*B*, here, may be any—every—sentence that you like (or don’t like, as the case may be)! EFQ is the principle that every sentence follows from a contradiction; it sanctions the step from a single contradiction to outright triviality of logic.

In the face of such absurdity (triviality), we conclude that something is wrong in the foregoing Liar reasoning. The question is: what? This, in the end, is the question that the Liar paradox raises.

## 3. Significance

We have now seen that with some elementary assumptions about truth and logic, a logical disaster ensues. What is the wider significance of such a result?

From time to time, the Liar has been argued to show us something far-reaching about philosophy. For instance, Grim (1991)[^grim-1991] has argued that it shows the world to be essentially ‘incomplete’ in some sense, and that there can be no omniscient being. McGee (1991)[^mcgee-1991] and others suggest that the Liar shows the notion of truth to be a vague notion. Glanzberg (2001)[^glanzberg-2001] holds that the Liar shows us something important about the nature of context dependence in language, while Eklund (2002)[^eklund-2002] holds that it shows us something important about the nature of semantic competence and the languages we speak. Gupta and Belnap (1993) claim that it reveals important properties of the general notion of definition. And there are other lessons, and variations on such lessons, that have been drawn.

Of more immediate concern, at least for our purposes here, is what the Liar shows us about the basic principles governing truth, and about logic. In a skeptical vein, Tarski himself (1935, 1944) seems to have thought the Liar shows the ordinary notion of truth to be incoherent, and in need of replacement with a more scientifically respectable one. (For more on Tarski, see the entries on Tarski and Tarski’s truth definitions. For more on Tarski’s aims and purposes, see Heck 1997.)[^heck-1997] More common, and perhaps the dominant thread in the solutions to the Liar, is the idea that the basic principles governing truth are more subtle than the T-schema reflects.

The Liar has also formed the core of arguments against classical logic, as it is some key features of classical logic that allow capture and release to result in absurdity. Notable among these are the arguments for logics that are paracomplete (e.g., Kripke 1975; Field 2008)[^field-2008][^kripke-1975] or paraconsistent (e.g., Asenjo 1966; Priest 1984, 2006)[^asenjo-1966][^priest-1984][^priest-2006]. However, Ripley (2013b)[^ripley-2013b] argues that classical logic can be maintained while shedding the features in question.

In many cases inspired by wider views of the significance of the paradox, there have been a number of attempts to one way or another resolve the paradox. It is to these proposed solutions that we now turn.

## 4. Some Families of Solutions

In this section, we briefly survey some approaches to resolving the Liar paradox. We group proposed solutions into families, and try to explain the basic ideas behind them. In many cases, a full exposition would involve a great deal of technical material that we will not go into here. Interested readers are encouraged to follow the references we provide for each basic idea.

### 4.1 Paracomplete and paraconsistent logics

One of the leading ideas for how to resolve the Liar paradox is that it shows us something about logic, in fact, something far-reaching about logic. The main idea is that the principles of capture and release are the fundamental conceptual principles governing truth, and cannot be modified. Instead, basic logic must be non-classical, to avoid a logical disaster of the kind we reviewed in §2.

One important way to motivate non-classical solutions is to appeal to a form of *deflationism* about truth. Such views take something akin to the T-schema to be the defining characteristic of truth, and as such, not open to modification (see, e.g., Horwich 1998)[^horwich-1998]. Most strictly, so-called transparency or ‘see-through’ or ‘pure disquotational’ conceptions of truth (e.g., Field 1994, 2008; Beall 2005)[^beall-2005][^beall-2005-2][^field-1994][^field-2008] take the defining property of truth to be *intersubstitutability* of *A* and $\Tr(\left\ulcorner A\right\urcorner)$ in all non-opaque contexts. This makes capture and release, in unrestricted form applying to all sentences of a language, a requirement for truth (at least where we have $A \vdash A$ or, more strongly, $\vdash A \rightarrow A)$.[^note-9] We note that, more recently, some deflationists have shifted the emphasis from the minimal principles traditionally taken to characterize truth (such as the T-schema) to the function truth serves in enabling generalizations (a role that has been highlighted at least since Quine). To see this, suppose a theory *S* is accepted: how can one state their agreement with all of *S*’s infinitely many consequences? Truth-theoretical generalizations offer a natural way to express such an agreement: ‘Everything that follows from *S* is true.’ Deflationists who emphasize such an expressive role of truth need not endorse the thesis that truth is uniquely or primarily characterized by minimal principles such as the T-schema (or its variants); rather, these versions of deflationism can be compatible with, or even support, other truth-theoretical principles (such as those discussed in §§4.3.3–4.3.4) insofar as they are essential to the expressive role of truth (see e.g. Picollo and Schindler 2018, 2021)[^picollo-2018][^picollo-2021]. See the entry on [truth](https://plato.stanford.edu/entries/truth/) for further discussion.

Assuming capture and release, and applying them to all sentences without restriction, yields triviality unless the logic is non-classical. There are two main sub-families of non-classical (transparency) truth theories: *paracomplete* and *paraconsistent*. We sketch the main ideas of each.

#### 4.1.1 Paracomplete

According to paracomplete approaches to the Liar, the main lesson of the Liar is that LEM ‘fails’ in some sense. In other words: the Liar teaches us that some sentences (notably, Liars!) ‘neither hold nor do not hold’ (in some sense), and so are neither true nor false. As a result, the logic of truth is non-classical.

This idea is perhaps most natural in response to the simple-falsity Liar. There, it is tempting to say that there is some status other than truth and falsity, and the Liar sentence *L* has it. But this will not suffice, for instance, for the simple-untruth Liar. This says nothing about falsity. Rather, in some way the basic reasoning reviewed in §2.3 must fail, and the culprit, in the paracomplete view, is LEM. Liar-instances of LEM ‘fail’ (in some sense) according to the paracomplete approach; such sentences fall into the ‘gap’ between truth and falsity (to use a common metaphor).

There have been many proposals for using such non-classical logics to address the Liar. An early example is van Fraassen (1968, 1970)[^fraassen-1968][^fraassen-1970]. But Kripke’s work has been the most influential in recent times, not only for approaches to the Liar based on non-classical logic, but also for a range of other approaches we will survey in §4.2. Thus, we pause to describe at least a little of Kripke’s framework.

##### Kripke’s theory

Logics where LEM fails are not themselves hard to come by. Among many such logics are a number of three-valued logics that allow sentences to take a third value over and above true and false. Sentences like Liar sentences take the third value. One of the most commonly applied logics is the Strong Kleene logic $K_3$. We do not go into the details of $K_3$ here, but only note the properties of $K_3$ we need. (For more details, see the entry on many-valued logic, or Priest 2008.)[^priest-2008] First and foremost, we have: $$\not\vdash_{K3} A \vee \neg A.$$ LEM fails. In fact, there are no logical truths (or valid sentences) according to $K_3$, even though there are valid inferences in it. (We return to this on the topic of a ‘suitable conditional’ below.)

The challenge to using $K_3$ to flesh out a paracomplete theory is to explain how anything like (even rule-form) capture and release hold, and if you follow the deflationist line, how full unrestricted capture and release hold. One way of understanding the important work of Kripke (1975)[^kripke-1975] (and related work of Martin and Woodruff 1975)[^martin-1975] is as a way of achieving just that.

Kripke begins with a fully classical language $\mathcal{L}_0$ containing no truth predicate (or more generally, no semantic terms). (Recall, we are assuming a language comes equipped with a valuation scheme. For $\mathcal{L}_0$ it is classical.) He then considers extending it to a language $\mathcal{L}^{+}_0$ which contains a truth predicate $\Tr$. The predicate $\Tr$ is taken to be applicable to every sentence of the expanded language $\mathcal{L}^{+}_0$, including those of the original $\mathcal{L}_0$. Thus, it is a self-applicative truth predicate (as the deflationist-inspired picture we mentioned must require), even though we begin with a language without a truth predicate.

We can think of $\mathcal{L}_0$ as interpreted by a classical model $\mathcal{M}_0$. Kripke shows us how to build an interpretation $\mathcal{M}^{+}_0$ for the expanded language. The main innovation is to see the truth predicate as *partial*. Rather than simply having an extension, it has an extension (set of things of which it is true), and an anti-extension (set of things of which it is false). The extension and anti-extension are mutually exclusive, but they need not jointly exhaust the domain of $\mathcal{M}_0$. Pathological sentences like *L* fall into neither the extension nor the anti-extension of $\Tr$. (Actually, we could have interpreted the base language $\mathcal{L}_0$ by a partial model as well, but the intended application sees partiality as only arising with semantic predicates like $\Tr.)$

Falling into neither the extension nor the anti-extension of $\Tr$ acts like having a third value, and we can interpret $\mathcal{L}^{+}_0$ as acting like a language with a $K_3$ valuation scheme. Treating the language this way, Kripke shows how to build up a very plausible extension and anti-extension for $\Tr$, typically written $\mathcal{E}$ and $\mathcal{A}$. The important property of the new extended model $\langle \mathcal{M}_0,\langle \mathcal{E},\mathcal{A}\rangle \rangle$ is that the truth value of *A* and $\Tr(\left\ulcorner A\right\urcorner)$ are exactly the same, for any sentence $A$. *A* is true, false, or neither, just in case $\Tr(\left\ulcorner A\right\urcorner)$ is. Furthermore, interpreting the expanded language $\mathcal{L}^{+}_0$ as a $K_3$ language, we have for $K_3$ consequence $A \dashv \vdash \Tr(\left\ulcorner A\right\urcorner)$, just as we desired.

Kripke shows how to build up $\mathcal{E}$ and $\mathcal{A}$ by an inductive process. One starts with an ‘approximation’ of the extension and anti-extension of $\Tr$, and successively improves it until the improvement process ceases to be productive (it reaches a ‘fixed point’). In fact, for the $K_3$-based solution, the natural thing to do is start with an empty extension and anti-extension, and add true sentences to the extension and false sentences to the anti-extension at successive stages of the process.

Kripke’s construction can be applied to a number of different logics, including other many-valued logics such as the ‘Weak Kleene’ logic, and supervaluation logics. See, for instance, Burgess 1986 and McGee 1991 for discussion. Kripke-style constructions engage a fair bit of mathematical subtlety. For an accessible overview of more of the details, see Soames 1999. For a more mathematically rich exposition, see McGee 1991.

##### Suitable conditionals

Logics like $K_3$ suffer from the lack of a natural or ‘suitable’ conditional (in particular, one that satisfies $A,A \rightarrow B \vdash B$ and $\vdash A \rightarrow A)$. This reveals a limitation of the Kripkean approach to the Liar. The language $\mathcal{L}^{+}_0$ cannot report the capture and release properties of truth itself in conditional form (i.e., T-biconditionals): $\Tr$ is transparent on this picture, and so $\Tr(\left\ulcorner A\right\urcorner)$ and *A* are fully intersubstitutable. We don’t have $\neg A \vee A$ true for all sentences *A* in this theory, and hence don’t have $\neg \Tr(\left\ulcorner A\right\urcorner) \vee$ A for all *A*. But $\neg \Tr(\left\ulcorner A\right\urcorner) \vee A$ is equivalent to $\Tr(\left\ulcorner A\right\urcorner) \rightarrow A$ in the theory, since (in the theory) $\rightarrow$ is just the material conditional. The Kripke construction at hand, then, thus fails to enjoy all T-biconditionals—the natural candidates for expressing in the theory the basic capture and release features of truth.

A recent, major step towards supplementing Kripke’s framework with a suitable conditional is that of Field (2008)[^field-2008]. Field’s theory is a major advance, but complex enough to be beyond the scope of this (very basic) introduction. Readers should consult Field’s own discussion for a taste of how such a modification might proceed. See Field (2008)[^field-2008], further discussion in Beall (2009)[^beall-2009], as well as subsequent developments in Field (2021, 2022, 2026)[^field-2021][^field-2022][^field-2026].

One important use for conditionals in logic is in formalizing *restricted universal quantification*, expressing the connection between *A* and *B* in ‘All *A*s are *B*s’. This has recently played a key role in a number of discussions of conditionals and paradoxes; see for example Beall et al. (2006); Beall (2011)[^beall-2011]; Field (2014)[^field-2014]; Ripley (2015)[^ripley-2015]; Field (2016)[^field-2016].

#### 4.1.2 Paraconsistent

As we mentioned, two important approaches to the Liar paradox that focus on non-classical logics are paracomplete and paraconsistent approaches. We sketched a paracomplete option above. We now turn to a paraconsistent option. Here, the basic idea is to allow the contradiction (e.g., up to and including step 4 of the derivation in §2.3.3), but alter the logic by rejecting EFQ—and, hence, avoid the absurdity involved in step 5.

Like the paracomplete approach we just surveyed, paraconsistent approaches to the Liar find easy, natural motivation in transparency or otherwise suitably ‘minimalist’ views of truth that require full intersubstitutability of *A* and $\Tr(\left\ulcorner A\right\urcorner)$, and thus cannot restrict capture and release. But paraconsistent approaches have also found motivation in a Dummett-inspired anti-deflationist view, which takes the role of truth as the aim of assertion seriously (cf. Dummett 1959)[^dummett-1959]. Indeed, Priest (2006)[^priest-2006] argues that this (non-transparency) view of truth motivates both the T-schema and LEM, and that this implies that the Liar sentence *L* is both true and not true. Hence, according to any such dialetheic line (according to which at least one sentence is both true and not true), the only option is to reject EFQ.

##### Dialetheism

Priest (1984, 2006)[^priest-1984][^priest-2006] has been one of the leading voices in advocating a paraconsistent approach to solving the Liar paradox. He has proposed a paraconsistent (and non-paracomplete) logic now known as *LP* (for *L*ogic of *P*aradox), which retains LEM, but not EFQ.[^note-10] It has the distinctive feature of allowing true contradictions. This is what Priest calls the dialetheic approach to truth. (See the entry on dialetheism for a more extensive discussion.)

Formally, *LP* can be seen as a three-valued logic; but where $K_3$ has truth-value gaps, *LP* has truth-value *gluts*. Thus, sentences in *LP* can be both true and false. However, as we discuss further in section 4.1.3, just how to describe both gaps and gluts is a delicate matter. For now, we only make the rough observation that in the same sense that $K_3$, in virtue of having a third truth value, can be said to have gaps, *LP* correspondingly has gluts.

Likewise, Kripke-style techniques can be applied to produce an interpretation for a truth predicate, starting with a classical language $\mathcal{L}_0$ not containing a truth predicate. Again, an extension and anti-extension are assigned to $\Tr$. Whereas Kripke’s original construction had the extension and anti-extension disjoint but not exhausting the domain, in this case we allow the extension and anti-extension to overlap, but suppose that the two together exhaust the domain of the model. This implements the idea of gluts, as the earlier version implemented the idea of gaps. Related techniques to Kripke’s can then be used to build an extension and anti-extension for $\Tr$. The result is again an interpretation where *A* and $\Tr(\left\ulcorner A\right\urcorner)$ get the same truth value in the model.

This construction was not given by Kripke himself, but variants have been pursued by a number of authors, including Dowden (1984)[^dowden-1984], Leitgeb (1999)[^leitgeb-1999], Priest (1984, 2006)[^priest-1984][^priest-2006], Visser (1984)[^visser-1984], and Woodruff (1984)[^woodruff-1984].

##### Combining paracompleteness and paraconsistency

Though we have identified paracomplete and paraconsistent approaches to the Liar as two distinct options, they are not incompatible. Indeed, seen as theories of negation (if one wants), one might think that negation is neither exhaustive nor ‘explosive’ – i.e., satisfies neither LEM nor EFQ. An approach like this is the *FDE*-based (transparent) truth theory discussed in Dunn 1969 (see Other Internet Resources); Gupta and Belnap 1993; Leitgeb 1999; Visser 1984; Woodruff 1984; Yablo 1993a; and—in effect—Brady 1989.

(The *LP*-based theories and $K_3$-based theories are—at least on one (standard-first-order) level—simply strengthened logics of the broader *FDE* logic. For general discussion of such frameworks, see, e.g. Priest 2008.)

#### 4.1.3 Expressive power and ‘revenge’

Working in classical logic, Tarski (1935)[^tarski-1935] famously concluded from the Liar paradox that a language cannot define its own truth predicate. More generally, he took the lesson of the Liar to be that languages cannot express the full range of semantic concepts that describe their own workings. One of the main goals of the non-classical approaches to the Liar we have surveyed here is to avoid this conclusion, which many have seen as far too drastic. However, how successful these approaches have been in this regard remains a highly contentious issue.

In one sense, both the paracomplete and paraconsistent approaches achieve the desired result: they present languages which contain truth predicates applying to sentences of those very languages, and in which  *A* and $\Tr(\left\ulcorner A\right\urcorner)$ have the same truth value. In this respect, they both present languages which contain their own truth predicate.

In the paracomplete case, the issue of whether this suffices has been much debated. The paracomplete view holds that the Liar sentence *L* is neither true nor false, and this is key to retaining consistency. But note that the paracomplete approach we discussed above cannot state this fact, as it cannot come out true that $\neg \Tr(\left\ulcorner L\right\urcorner)$. If this were true, then *L* would be true, and then $\Tr(\left\ulcorner L\right\urcorner)$ would be true, bringing us back to contradiction.

Sometimes, paracomplete and paraconsistent views are contrasted by saying that paracomplete views take paradoxical sentences to be neither true nor false, while paraconsistent views take paradoxical sentences to be both true and false. That is sometimes the way these positions are stated, but the matter is more complicated than this. Consider the claim that the Liar is neither true nor false. This claim can be formalized in our object language as $\neg(\Tr \ulcorner \lambda \urcorner \vee \Tr \ulcorner \neg\lambda \urcorner)$. A quick calculation (relying on double negation elimination, the De Morgan equivalences, the definition of *λ*, and the equivalence between *λ* and $\Tr\ulcorner\lambda\urcorner$) shows this to be *equivalent* to $\Tr \ulcorner \lambda \urcorner \wedge \Tr \ulcorner \neg\lambda \urcorner$. This is a formalized version of the claim that the Liar is both true and false. So, formally, the claims that the Liar is neither true nor false and that it is both true and false are equivalent. (All of this reasoning goes through in both $K_3$ and $LP$). Any paracomplete or paraconsistent view must thus be careful how they state their positions. For instance, a paracomplete theorist might reject both the claim that the Liar is neither true nor false and the claim that it is both true and false (note that rejection is *not* to be understood as accepting the negation), while a paraconsistent theorist might accept both claims. Indeed, a central problem for the paracomplete approach is that it cannot accurately state its own solution to the Liar. Just what to make of this has been debated. It is certainly the case that the set of true sentences in the kind of model Kripke constructs does not include $\neg \Tr(\left\ulcorner L\right\urcorner)$. Because of this, some authors, such as McGee (1991)[^mcgee-1991], T. Parsons (1984)[^parsons-1984], and Soames (1999)[^soames-1999], have in effect maintained that the Liar sentence failing to be true is a further fact that goes beyond what the truth predicate needs to express, and so is immaterial to the success of the solution to the Liar. (Actually, McGee’s view has another aspect, which we discuss in §4.3.5.)

But nonetheless, it does appear that there is an important semantic fact about truth in the paracomplete language, closely related to, if not identical to, a fact about truth *per se*, which the language cannot express. It thus has been argued to fail to achieve a fully adequate theory of truth. Kripke himself notes that there are some semantic concepts that cannot be expressed, and the argument has been pressed by C. Parsons (1974)[^parsons-1974].

One way of spelling out what is missing in the paracomplete language is to introduce a new notion of *determinateness*, so that the status of the Liar is that of not being determinately true. If so, then the Kripke paracomplete language cannot express this concept of determinateness. Some approaches taking paracomplete ideas on board have sought to supplement the Kripke approach by adding notions of determinate truth. McGee (1991)[^mcgee-1991] does so in a basically classical setting. In a non-classical, paracomplete setting, Field (2008)[^field-2008] supplements the basic paracomplete approach with infinitely many different ‘determinately’ operators, each defined in terms of Field’s ‘suitable conditional’, and each giving a different (stronger) notion of ‘truth’. (See also some of the papers in Beall (ed.) 2007.)

It is often argued in favor of paraconsistent approaches that they have no trouble ‘characterizing’ the status of Liars: they’re true and false (i.e., they are true and their negations are true). *LP* theories can state this. On the other hand, some authors, such as Littmann and Simmons (2004) and S. Shapiro (2004)[^shapiro-2004], have thought that there is a dual problem: namely, characterizing ‘normal’ sentences, those that are not both true and false. (Some put this alleged problem as the problem of characterizing being *just true*.) Whether this is a problem is something we leave open. (For some discussion, see Field 2008 and Priest 2006.)[^field-2008][^priest-2006]

These issues are often discussed under the heading of so-called ‘revenge paradoxes’ (see Murzi and Scambler 2026 for an introductory overview)[^murzi-2026]. We can illustrate this with the simple-falsity Liar. Suppose one starts with this as the benchmark Liar paradox, and proposes a simple solution that rejects bivalence. In response one is shown the simple-untruth Liar, which undercuts the simple solution. This is the pattern of ‘revenge’, where a solution to the paradox is rejected on the basis of what might be taken to be a slightly modified form of the paradox. In slightly more detail: in some widely discussed examples, a revenge paradox occurs when the notions introduced (perhaps implicitly) to provide a solution to the Liar can themselves be used to introduce a new (and equally hard) version of the Liar. When this happens, the theory that is the target of revenge is argued either not to have solved the paradox or to suffer from expressive limitations because of the notions it cannot express on pain of triviality.

Revenge paradoxes for paracomplete solutions are often proposed: many points where the paracomplete language fails to express some semantic concept offer ways to construct a revenge problem. Failing to correctly state the status of the simple-untruth Liar is one example. Another example involves the notion of determinateness discussed above. If we take the determinateness route, and assign the Liar sentence the status of not being determinately true, then one can construct a revenge problem via a sentence which says of itself that it is not determinately true.

In a similar vein, it is sometimes argued that paraconsistent approaches face a kind of revenge problem, as they have to treat the Curry paradox we discussed in §1.4 separately from the Liar. This is a somewhat difficult technical issue, as it depends on the nature of the conditional used to formulate the Curry sentence. If that conditional obeys the detachment property, then it cannot be a glut, as the Liar is in paraconsistent settings. But whether that is the correct approach to the conditional has been controversial. For more discussion, see Beall (2014, 2015)[^beall-2014][^beall-2015].

We have seen at least some approaches (e.g., McGee 1991; in some respects, T. Parsons 1984 and Soames 1999)[^mcgee-1991][^parsons-1984][^soames-1999] reject the revenge problem, while some seek to solve it by additional apparatus (e.g., Field 2008)[^field-2008]. As we discuss further in §4.4, contextualist views such as those of Burge (1979)[^burge-1979], Glanzberg (2004a)[^glanzberg-2004a], and C. Parsons (1974)[^parsons-1974] tend to see revenge not as a separate problem, but as the core Liar phenomenon. For more discussion about revenge and its nature, see the papers in Beall (ed.) (2007) and L. Shapiro (2006)[^shapiro-2006]. In recent years, the notion of semantic paradox has been broadened beyond the traditional cases of the Liar, Curry, and their variants (see, e.g., Beall and Murzi 2013)[^beall-2013]. The phenomenon of revenge has also received increased attention, across a variety of semantic notions and theories. Partially in response to this richer landscape, Murzi and Rossi (2020) proposed a general template for revenge paradoxes, arguing that non-classical theories from the main families considered here fail to characterize either paradoxical or unparadoxical sentences. For recent discussions of such generalized revenge, see Incurvati and Schlöder (2023, ch. 7) and Rosenblatt (2023)[^rosenblatt-2023].

### 4.2 Substructural logics

There is another way to see the paradox as arising from mistaken assumptions built into standard logics. This way doesn’t see the trouble as attaching to any particular connective or piece of vocabulary, but instead as attaching to some of the *structural rules* that govern the consequence relation in question. These approaches, based on so-called *substructural logics*, fall into three main camps: the noncontractive, the nontransitive, and the nonreflexive. (There is a great deal more diversity among substructural logics than this suggests; in particular, many do not fall into any of these camps, or fall into more than one. But these are the three that seem to be best-suited for addressing the paradoxes we are concerned with here.)

#### 4.2.1 Noncontractive logics

An influential substructural approach to paradoxes works by attacking the structural rule of *contraction*. Contraction is the principle that tells us that whenever $\Gamma , A, A \vdash B$, then $\Gamma , A \vdash B$; that is, it is the principle that tells us that if a conclusion $B$ follows from premiss $A$ taken twice (plus extra premises *Γ*), then it also follows from premiss $A$ taken once (plus the same extra premises). Returning to the argument given in section 2, we can see that in two cases, an assumption is used twice in reaching a conclusion: assumption 2a is used twice on the way to 2d, and assumption 3a is used twice on the way to 3d. As we presented the argument, we did not call attention to this feature, but it is one place a noncontractive approach will focus.

The details of the response will depend on how the connectives we have written as ‘$\vee$’ and ‘$\wedge$’ are interpreted; in the absence of contraction, each of conjunction and disjunction comes in ‘additive’ and ‘multiplicative’ flavors, and different proponents of noncontractive views differ in which of these they acknowledge. The difference between additive and multiplicative conjunction is this: an additive conjunction can do the work that *either* of its conjuncts can do, while a multiplicative conjunction can do the work that *both* of its conjuncts can do together. In the presence of contraction, the additive conjunction suffices for the multiplicative: it can be used once to fill the role of the first conjunct and again to fill the role of the second conjunct. Contraction allows these two uses to count as one. Without contraction, though, the additive conjunction need not suffice for the multiplicative. (The multiplicative conjunction suffices for the additive in the presence of a structural rule called weakening, not otherwise discussed in this article.) The situation for disjunction is dual: in the presence of contraction, the additive disjunction suffices for the multiplicative, but it need not otherwise.

The double use pointed to above will loom largest if these connectives are read multiplicatively: if 2d really is to do the work of $\neg \Tr(\left\ulcorner L\right\urcorner)$ and $\Tr(\left\ulcorner L\right\urcorner)$ *together*, then it really does use two copies of 2a, one for each conjunct. On an additive reading of 2d and 3d, this seeming double use need not be troubling, since 2d itself only needs to do the work of one of its conjuncts. Although this can be either one, whichever conjunct it is, a single use of 2a will suffice. On this additive reading, it is the principles LEM and EFQ that come into question; for example, with $\wedge$ read additively it takes *two* occurrences of the same contradiction to entail an arbitrary sentence (since both conjuncts must be used), while the derivation above only yields one. (The situation for 3d and 3a is similar, in either case.) We do not here consider further details; for more on these choices and noncontractive approaches in general, see Beall and Murzi (2013), Cantini (2003)[^cantini-2003], Grishin (1982)[^grishin-1982], Petersen (2000)[^petersen-2000], Restall (1994)[^restall-1994], Ripley (2015)[^ripley-2015], L. Shapiro (2011a, 2015)[^shapiro-2011a][^shapiro-2015], and Zardini (2011, 2013)[^zardini-2011][^zardini-2013]. (Some of these focus on set-theoretic paradoxes rather than truth-theoretic paradoxes, but many of the issues are parallel. See also the entry on Russell’s paradox.)

#### 4.2.2 Nontransitive logics

Another kind of substructural approach works by attacking various structural rules associated with the *transitivity* of consequence. In its simplest form, transitivity states that if $B$ follows from $A$ and $C$ follows from $B$, then $C$ follows from $A$, in symbols: if $A \vdash B$ and $B \vdash C$, then $A \vdash C$(this property is called *simple transitivity* in Weir 2015)[^weir-2015]. The best-known generalization of simple transitivity is the rule of *cut*, which allows us to move from $\Gamma \vdash B$ and $\Delta , B \vdash C$ to $\Delta , \Gamma \vdash C$.

Some nontransitive approaches can be understood through the same three-valued models as are used for K$_3$ and LP (again, we refer you to the entry on many-valued logic for details). The difference is in how consequence is defined on these models. In all cases, consequence amounts to the absence of a countermodel, but there are different understandings available of what a model has to be like to be a countermodel to an argument. Depending on what understanding of countermodel is adopted, the very same three-valued models can give rise to the paracomplete logic K$_3$, the paraconsistent logic LP, a paracomplete and paraconsistent logic sometimes called S$_3$ or FDRM, or—our present topic—two different logics that include counterexamples to the rule of cut, and have come to be known as *nontransitive*.

One kind of approach without cut is developed and defended in Weir 2005, 2015 (and for naive set theory in Weir 1998, 1999)[^weir-1998][^weir-1999], and is there dubbed ‘neoclassical’. On this approach, the third value in the models is taken to be neither true nor false, and a countermodel to an argument from *Γ* to *B* must either: make every sentence in *Γ* true and *B* untrue, or else make *B* false and every sentence *but one* in *Γ* true, while making that remaining sentence in *Γ* unfalse. The motivating idea is that valid arguments must preserve truth, and must also preserve falsity backwards in a certain sense: if a valid argument has all its premises but one true and its conclusion false, then the remaining premise must be false. This allows for counterexamples to cut, but not to simple transitivity, and allows for consistency to be maintained. The resulting logic is weaker than classical logic. In our version of the Liar paradox, the trouble is at LEM: Weir’s approach allows for counterexamples to excluded middle.

A different kind of approach without cut is developed and explored in Barrio et al. 2015; Cobreros et al. 2013, 2015; Fjellstad 2016; and Ripley 2013a, 2015. On this approach, a countermodel to an argument cannot assign the third value to any sentence that occurs in the argument. That is, a countermodel to an argument from *Γ* to *B* must do just what a classical countermodel does with regards to the argument. If it assigns the third value to any sentence at all, that sentence cannot be in *Γ* and it cannot be *B*. This allows for counterexamples to cut, and unlike Weir’s approach, it also allows for counterexamples to simple transitivity. It also has the curious feature that every argument valid in classical logic remains valid. That is, all the counterexamples to cut and simple transitivity involve appeal to capture, release, or some other special behavior of the truth predicate. Despite this classical flavor, these approaches are also dialetheist; the claim that the Liar sentence is both true and not true turns out to be a theorem. Such a claim is forced to take the third value, and so there can be no countermodel to any argument involving it.

Perhaps because of the importance of the rule of cut in proof theory, nontransitive approaches are often studied via proof systems rather than via models. The essential use of transitivity properties in paradoxical derivations was noted in Tennant 1982; an approach to paradoxes that rejects both cut and simple transitivity in a general setting can be found in Hallnäs 1991; Hallnäs and Schroeder-Heister 1991; and Schroeder-Heister 2004. There are helpful philosophical remarks on cut in Schroeder-Heister 1992, which also notes some relations between noncontractive and nontransitive approaches.

#### 4.2.3 Nonreflexive logics

A third possibility for a substructural approach to paradoxes comes from attacking *reflexivity*, the principle that every sentence entails itself. There is a close analogy between reflexivity and transitivity, as explained in Frankowski 2004; Girard et al. 1989 (p.28); and Ripley 2012, so this kind of approach ends up having commonalities with the nontransitive family. Nonreflexive approaches to paradoxes have so far been less-explored, but seem to be a promising direction for further work; see French (2016)[^french-2016], Meadows (2014)[^meadows-2014], Nicolai and Rossi (2018, 2023)[^rossi-2023] for more. See also Malinowski (1990)[^malinowski-1990] for general work on nonreflexive logics.

### 4.3 Classical logic

We have now seen a range of options for responding to the Liar paradox by reconsidering basic logic. There are also a number of approaches that leave classical logic unchanged, and try to find other ways of defusing the paradox.

One hallmark of most of these approaches is a willingness to somehow *restrict* the range of application of capture and release, to block the paradoxical reasoning. This is antithetical to the kind of deflationist view of truth we discussed in §4.1, but it is consistent with another view of truth. This other view takes the main feature of truth to be that it reports a non-trivial semantic property of sentences (e.g., corresponding with a fact in the world, or having a value in a model), and that it performs an irreplaceable semantic function (notably, determining the truth-conditions, and ultimately the meaning, of a large class of sentences). Many approaches within classical logic embody the idea that a proper understanding of this feature allows for restricted forms of capture and release, and this in turn allows the paradox to be blocked, without any departure from classical logic. Other approaches seek alternatives to capture and release altogether, and primarily characterize truth via compositional principles.

We will consider a number of important approaches to the paradox within classical logic, most of which embody one of these two guiding ideas.

#### 4.3.1 Typed restrictionist approaches

Classical solutions to the Liar must give up at least one of unrestricted capture and unrestricted release. Indeed, many classical solutions are characterized precisely via how such principles are restricted. Call such approaches *restrictionist*. The simplest restrictionist approach is known as *typing*. Although details vary, the basic idea (in its simplest version) is that the notion of truth, or truth-theoretic principles, should apply only to truth-free formulas.

The oldest typed restrictionist approach is Tarski (1936). Two features of Tarski’s approach set it apart from contemporary solutions to the Liar. First, Tarski sought a *definition* of truth, i.e. a formula which would qualify as defining the notion of truth. What would it take for a formula to define truth? First and foremost, for Tarski, the definition should be ‘materially adequate’. This means that, if $Ax$is the truth-defining formula, then all instances of $A\ulcorner B \urcorner \leftrightarrow B$should hold. This is essentially the T-schema. In fact, Tarski notices that, if the language in which *A* is defined could define truth for itself, then a paradox – the Liar paradox – would immediately ensue.

This brings us to the second feature of Tarski’s approach, namely that he considers two (interpreted) languages: an object language $\mathcal{L}_0$ and a meta-language $\mathcal{L}_1$. The object language $\mathcal{L}_0$is the language for which truth should be defined. In order to avoid the paradoxes, $\mathcal{L}_0$is to be impoverished enough that it does not contain, nor can it define, a materially adequate notion of truth for itself. The meta-language $\mathcal{L}_1$, on the other hand, is the essentially richer language that contains $\mathcal{L}_0$, and in which truth for $\mathcal{L}_0$ is defined. This means that, in the above schema, $Ax$ should belong to $\mathcal{L}_1$, and *B* to $\mathcal{L}_0$. With this restriction, it is easy enough to define a truth predicate which accurately states the truth values of every sentence in $\mathcal{L}_0$, obeys capture and release, and yields no paradox. Why is there no Liar paradox in Tarski’s treatment? Because of the syntactic restriction that the object language $\mathcal{L}_0$cannot include or define a self-applicable truth predicate (so, there is no Liar sentence in $\mathcal{L}_0$), and because no truth-theoretical principles apply to $\mathcal{L}_1$-formulas. See the entries on Tarski and Tarski’s truth definitions for more on Tarski’s views of truth.

Few contemporary restrictionists endorse Tarski’s syntactic ban Liar sentences. Contemporary restrictionists employ one (uninterpreted) formal language which includes a truth predicate, in which self-referential sentences can be defined. Such sentences, however, are inert, since truth-theoretical principles do not apply to them. The simplest restrictionist proposal consists in only accepting those instances of the T-schema $\Tr\ulcorner A \urcorner \leftrightarrow A$ in which *A* does not include the truth predicate. Such instances are known as *Tarski biconditionals*.

Typed restrictionism has faced significant criticism. To begin with, Tarski-style typing is very drastic: cases of self-reference unproblematically occur in natural languages, so declaring Liar sentences ill-formed seems unmotivated. Though Tarski aimed mainly at formal languages, his solution looks implausible for ordinary uses of ‘true’. Secondly, typed restrictionist theories are very weak: not even a platitude such as ‘it is true that it is true that $2+2=4$’ can hold in them. One way to ameliorate the situation is to iterate the typed construction. For example, in a Tarskian vein, if we want to describe truth in $\mathcal{L}_1$, we need to step up to $\mathcal{L}_2$ to get a truth predicate for $\mathcal{L}_1$. At this point one can express “it is true that it is true that $2+2=4$” with two distinct truth predicates: $\Tr_2\ulcorner \Tr_1 \ulcorner 2+2=4\urcorner \urcorner$. The process goes on indefinitely. At each stage, a new notion of truth is produced, which expresses truth for languages below it. (For more on the mathematics of this sort of hierarchy of languages, see Halbach (1997)[^halbach-1997].) However, it is unclear why one cannot just define truth for the meta-language, or for the whole hierarchy by quantifying over levels. We would thus have a predicate like ‘true at some level’. If such predicates are allowed, we are back in paradox, so defenders of the Tarskian hierarchy must say they are not possible. Explaining why is a problem for all hierarchical views. (See Glanzberg (2015)[^glanzberg-2015] and Sher (2023)[^sher-2023] for further discussion.)

Another important problem was highlighted by Kripke (1975)[^kripke-1975]. As Kripke notes, any syntactically specified set of levels will make it extremely hard, if not impossible, to place various non-paradoxical claims within the hierarchy. For instance, if Jc says *that everything Michael says is true*, the claim has to be made from a level of the hierarchy higher than everything Michael says. But if among the things Michael says is *that everything Jc says is true,* Michael’s claims must be at a higher level than all of Jc’s claims. Thus, some of Michael’s claims must be higher than some of Jc’s, and *vice versa*. This is impossible. It is also difficult to explain what level of the hierarchy an utterance winds up at when it can be coherently assigned a level. What makes it such that it involves truth at one level rather than another? For reasons such as these, many conclude that typed restrictionist strategies resolve the Liar at an excessive cost.

#### 4.3.2 Type-free restrictionism

Typing is confining. It is no surprise, then, that *type-free* restrictionist approaches have been pursued. Such approaches proceed by placing limits on the T-schema (or on capture and release). At a minimum, they must secure all Tarski biconditionals, while avoiding unnecessary constraints. The guiding question then becomes: how are the acceptable instances of the T-schema selected?

Horwich (1998)[^horwich-1998] proposed an influential criterion: we should accept all and only those instances which spell no Liar-induced trouble, no more and no less, and it should be possible to constructively specify the criterion to include the desired instances. However, Horwich’s proposal was shown to be unreachable by McGee (1992)[^mcgee-1992]. McGee explicates Horwich’s criterion as the requirement that there be a maximal consistent (i.e., consistent and not consistently extendable) and recursive set of instances of the T-schema. He then showed that there are uncountably many such sets, none of which is recursive (not even recursively enumerable).

In the last two decades, many restrictionist approaches have been proposed, typically by abandoning either the ideal of maximal consistency or the demand for simplicity. Horwich (2003)[^horwich-2003] and Leitgeb (2005)[^leitgeb-2005] pursue the latter option, restricting the T-schema to ‘grounded’ sentences (see Schindler 2014, 2020 for further discussion)[^schindler-2014][^schindler-2020]. Though details vary, a sentence is grounded if its truth value ultimately depends on the truth-free fragment of the language (see §4.3.5 for more on grounded sentences, and Kripke’s influential proposal for this notion). For instance, ‘It is true that Sarah is home’ depends only on whether Sarah is home, whereas a Liar sentence, when unpacked, just loops back on itself. Let *L* be equivalent to $\neg\Tr\ulcorner L \urcorner$. Then *L* depends on $\Tr\ulcorner L \urcorner$, which in turn depends on *L* again, and so on without end. If circular dependence is at the source of paradox, restricting the T-schema to grounded sentences seems motivated. In a similar vein, Picollo (2020a,b) allows only sentences with ‘safe reference patterns’, thereby excluding the Liar and its kin. Halbach (2009)[^halbach-2009], by contrast, proposes a simple syntactic criterion: the T-schema applies only where the truth predicate does not occur under an odd number of negations. We noted earlier that paradoxical reasoning often involves negative connectives. If unsafe negative connectives are the culprits of the paradox, confining the T-schema to ‘safe’ negations is well motivated. Finally, Warren (2024)[^warren-2024] offers another syntactic proposal: just as imperatives and interrogatives do not instantiate logical laws, so too paradoxical sentences should not instantiate the T-schema. The Tarskian aspiration for syntactic regimentation of truth remains alive.

Type-free restrictionism also faces serious objections. Tarski himself noted a difficulty for (classical) theories that rely solely on the T-schema (or capture and release), or restrictions thereof. To illustrate the point, consider a theory consisting only of all Tarski biconditionals (but the problem generalizes). Such a theory, Tarski observed, ‘would be a highly incomplete system, which would lack the most important and most fruitful general theorems’ (Tarski 1936: 257). For example, such a theory can prove that for any specific truth-free sentence *A*, $\Tr\ulcorner A \urcorner \vee \Tr\ulcorner \neg A \urcorner$holds, but not the quantified claim that *every* (truth-free) sentence is either true or false (i.e. the principle of bivalence). More generally, a theory based solely on schematic principles that permit adding or removing truth (like the Tarski biconditionals) can prove all *instances* of truth-theoretic generalizations, but not the generalizations themselves. Even simple principles such as ‘a conjunction is true if and only if both its conjuncts are’ cannot be derived. Yet such generalizations are central to those who view truth as a substantive semantic property, crucial for determining meaning via truth-conditions. This objection extends, *mutatis mutandis*, to stronger type-free restrictionist views. Partly in response to these concerns, several contemporary restrictionists develop deductively strong theories that can interpret or otherwise reproduce non-restrictionist theories, thereby recovering such generalizations (see e.g. Halbach (2009)[^halbach-2009] and, more recently, Horsten and Leigh (2017), for different strategies to pursue this objective). Critiques of restrictionist approaches along these lines provide part of the motivation for compositional approaches, to which we now turn.

#### 4.3.3 Classical compositionality

In light of the criticisms reviewed above, a number of approaches to the Liar have sought to preserve classical logic, while characterizing truth via different principles than just a set of instances of the T-schema. Compositional approaches take the need to express generalizations seriously, and seek to characterize truth directly via such generalizations. An early compositional theory was proposed by Friedman and Sheard (1987), known as $\mathsf{FSN}$. It comprises all Tarski biconditionals together with formalizations of:

- A negation is true if and only if its negand is not true
- A conjunction is true if and only if both its conjuncts are true
- A universally quantified formula is true if and only if all its instances are true

Note that the last clause treats the quantifiers substitutionally: while technically convenient, the substitutional reading is not, strictly speaking, required for compositional approaches.

These principles are formalized as *quantified axioms*, not schemata. This allows $\mathsf{FSN}$to overcome the generalization problem faced by restrictionist theories. $\mathsf{FSN}$thus stands at the opposite end of a spectrum from restrictionist theories: the latter emphasize recovering capture and release as much as is consistent with classical logic, and can be motivated by the inferential role of truth, whereas the former emphasizes truth-theoretic generalizations, in line with the semantically explanatory role of truth. By itself, however, $\mathsf{FSN}$ is weak: it proves no claims involving iterated truth. Once $\mathsf{FSN}$ is supplemented with even very weak principles permitting such iterations, variants of the Liar re-emerge. Suppose we add two rules stating that whenever *A* is provable from no premises, one may conclude $\Tr\ulcorner A \urcorner$, and conversely. These are significant weakenings of capture and release. The resulting theory, $\mathsf{FS}$, was shown by McGee (1985)[^mcgee-1985] to be *ω*-inconsistent (let’s assume for simplicity that we are working in the language of arithmetic expanded by the truth predicate): there is a formula $Bx$ such that, for every closed term t of the language, $\mathsf{FS}$ proves $Bt$, yet $\mathsf{FS}$ also proves $\neg \forall x Bx$. McGee’s formula is an infinitary Liar: in effect, $\mathsf{FS}$ proves ‘it is not the case that every iteration of the truth predicate in front of this very formula is true’, while also proving that for any given number of iterations, the corresponding sentence is true. Thus the Liar reappears, in new guises, for compositional theories as well.

#### 4.3.4 Quasi-classical compositionality: the closed-off Kripke construction

What is probably the most influential classical approach has been inspired by Kripke himself. Rather than see the Kripke apparatus we reviewed briefly in §4.1.1 as part of a non-classical logical approach, one can see it as an intermediate step towards building a classical interpretation of a self-applicative $\Tr$.

Recall that the Kripke construction starts with a classical language $\mathcal{L}_0$ with no truth predicate. It passes to an expanded language $\mathcal{L}^{+}_0$, but unlike a Tarskian metalanguage, this language contains a truth predicate $\Tr$ that applies to all of $\mathcal{L}^{+}_0$. Kripke shows how to build a partial interpretation of $\Tr$, providing an extension $\mathcal{E}$ and an anti-extension $\mathcal{A}$. But one can then simply consider the *classical* model $\langle \mathcal{M}_0,\mathcal{E}\rangle$, using only the extension. This is the ‘closed-off’ construction, as the gap between extension and anti-extension is closed off by throwing everything in the gap into the false category of a classical model.

We know this interpretation cannot make true all of capture and release (nor the full intersubstitutability of *A* and $\Tr(\left\ulcorner A\right\urcorner)$). But it does make a restricted form true. The following holds in the closed-off model: $$ [\Tr(\left\ulcorner A\right\urcorner) \vee \Tr(\left\ulcorner \neg A\right\urcorner)] \rightarrow[\Tr(\left\ulcorner A\right\urcorner) \leftrightarrow A].$$ This tells us that capture and release (in the form of the T-schema) hold for sentences that are well-behaved, in the sense of satisfying $\Tr(\left\ulcorner A\right\urcorner) \vee \Tr(\left\ulcorner \neg A\right\urcorner)$.

What happens to the Liar sentence on this approach? As in the three-valued case, the Liar is interpreted as falling within the gap. *L* is neither in $\mathcal{E}$ nor $\mathcal{A}. L$ thus falls outside of the domain where $\Tr$ is interpreted as well-behaved. Because the situation is classical, and $\left\ulcorner L\right\urcorner\not\in \mathcal{E}$, we know that $\neg \Tr(\left\ulcorner L\right\urcorner)$ is true in the closed-off model; likewise, so is $\neg \Tr(\left\ulcorner \neg L\right\urcorner)$.

On well-behaved sentences, we have the fixed point property that *A* and $\Tr(\left\ulcorner A\right\urcorner)$ have the same truth value, and so the semantics of $\mathcal{L}^{+}_0$ and the semantics it assigns to $\Tr$ correspond exactly. On pathological sentences like *L*, they do not, and indeed, cannot, on pain of triviality.

In a point related to the closed-off construction, it was observed by Feferman (1984)[^feferman-1984] that if we are careful about negation, we can dispense with $\mathcal{A}$ altogether in the Kripke construction. Thus, the construction can be done without any implicit appeal to many-valued logic. Related ways of thinking about Kripke’s construction are discussed by McGee (1991)[^mcgee-1991].

Kripke’s approach was given a classical axiomatization in Feferman (1991)[^feferman-1991] (today, a slightly more general version admitting both gaps and gluts is typically presented as the default version; see Visser (1984)[^visser-1984] and Halbach (2014)[^halbach-2014]). The resulting theory, called $\mathsf{KF}$, adopts the clauses used to build $\mathcal{E}$, and thus partly diverges from classical compositional principles. While a conjunction is still true iff both conjuncts are, it is no longer the case that a negation is true iff its negand is not true. This reflects Kripke’s construction: it is not the case that $\neg A \in \mathcal{E}$ if and only if $A \notin \mathcal{E}$. For instance, a Liar sentence *L* is not in $\mathcal{E}$, yet this does not place $\neg L$ in $\mathcal{E}$. Although KF departs from the elegant simplicity of $\mathsf{FSN}$, it includes a desirable axiom for truth-iteration: ‘it is true that *A* is true iff *A* is true’. In this way, $\mathsf{KF}$ captures the fixed-point behavior of truth while avoiding the *ω*-inconsistency of $\mathsf{FS}$. $\mathsf{KF}$ lacks principles for freely introducing or eliminating the truth predicate, i.e. approximations to the T-schema or to capture and release. However, $\mathsf{KF}$ can be consistently (and *ω*-consistently) strengthened with either direction of the T-schema (clearly, not both). Such strengthenings are essentially asymmetrical: if release is added, even very weak principles cannot be added to approximate capture, and vice versa. These asymmetrical strengthenings are especially interesting in relation to the Liar.

- Suppose one adds release. Over $\mathsf{KF}$, release is equivalent to a consistency statement: no sentence is both true and false. The resulting theory rules out fixed points where extension and anti-extension overlap, yielding $K_3$ fixed points, where they have a non-empty gap. With this axiom, the theory proves $\neg\Tr\ulcorner L \urcorner$, which is equivalent to *L* itself, so the Liar is proved.
- Suppose one adds capture. Over $\mathsf{KF}$, capture is equivalent to a completeness statement: every sentence is either true or false. The resulting theory rules out incomplete fixed points, and yields $LP$ fixed points, where extension and anti-extension overlap. With this axiom, the theory proves $\Tr \ulcorner L \urcorner$, i.e. $\neg L$, thereby refuting the Liar.

Thus, while $\mathsf{KF}$ itself remains ‘silent’ about the Liar, its extensions treat it in opposite ways: either proving it while declaring it untrue, or refuting it while declaring it true. This ambivalence has drawn criticism (Field 2008, Horsten 2011)[^field-2008][^horsten-2011]. Whether these objections succeed depends on one’s conception of truth. Silence about the Liar is common to many paracomplete theories (and is defended in Horsten 2009)[^horsten-2009], while declaring L untrue accords with a grounded conception of truth, according to which the extension of truth is ultimately determined by truth-free sentences, leaving the Liar outside it.

Theories such as $\mathsf{FS}(\mathsf{N})$ and $\mathsf{KF}$ have been central to axiomatic approaches to self-applicable truth; see Cantini (1996)[^cantini-1996], Feferman (1984, 1991)[^feferman-1984][^feferman-1991], Friedman & Sheard (1987), Horsten (2011)[^horsten-2011], and Halbach (2014)[^halbach-2014] for comprehensive treatments. For an overview, see the entry on [axiomatic theories of truth](https://plato.stanford.edu/entries/truth-axiomatic/).

#### 4.3.5 Determinateness revisited

In §4.1.3 we noted that paracomplete approaches to the paradox can be vulnerable to ‘revenge paradoxes’ based on some idea of indeterminate truth or lacking a truth value. Related issue arise in the classical case. We will discuss a few in turn.

##### Grounded sentences

The closed-off Kripke construction can help fill in the idea of *determinateness* discussed in §4.1.3. Instead of an operator, it allows us to define a predicate $D(\left\ulcorner A\right\urcorner)$ by $\Tr(\left\ulcorner A\right\urcorner) \vee \Tr(\left\ulcorner \neg A\right\urcorner).$ *D* represents ‘determinately’ in the sense of applying to sentences that have a truth value according to $\Tr$, as it were, ‘determined’ by the model produced by the Kripke construction. It also, as we observed, applies to all the sentences which are well-behaved in the sense of obeying the T-schema (or capture and release).

Formally, the sentences to which *D* applies in the model generated by the Kripke construction are those which fall in $\mathcal{E}$ or have their negations fall in $\mathcal{E}$ (equivalently fall in $\mathcal{A})$. Kripke labeled this being *grounded*.[^note-11]

It has often been noted that there is also a more informal notion of determinateness or grounding, to which the formal notion expressed by *D* at least roughly corresponds (cf. Herzberger 1970)[^herzberger-1970]. The idea is that the determinate sentences are the ones with well-defined semantic properties. Where we have no such well-defined semantic properties, we should not expect the truth predicate to report anything well-behaved, nor should we expect properties like capture and release to hold. Kripke’s construction builds up $\mathcal{E}$ in stages, starting with sentences with no semantic terms, and adding semantic complexity at each stage. One reaches $\mathcal{E}$ at the limit of this process, which allows us to think of $\mathcal{E}$ as indicating the limit of where semantic values are assigned by a well-defined process. (The well-defined process is, technically, that of an inductive definition: see Moschovakis (1974)[^moschovakis-1974], Aczel (1980)[^aczel-1980], Burgess (1986)[^burgess-1986], and McGee (1991)[^mcgee-1991] for more on this). Thus, the formal notion of grounding provided by *D* is sometimes suggested to reflect the extent to which sentences have well-defined semantic properties. This is also why, as noted above, grounded sentences receive their truth value in virtue of the values of truth-free sentences.

The notion of grounding has spawned its own literature, with Leitgeb (2005)[^leitgeb-2005] a key impetus. See also Bonnay and van Vugt (2015), Meadows (2013)[^meadows-2013], and Schindler (2014)[^schindler-2014].

##### Definite truth

Another view which makes use of a form of determinateness is advocated by McGee (1991)[^mcgee-1991]. McGee’s theory, like many we have surveyed here, is rich in complexity to which we cannot do justice. The theory has many components, including a mathematically sophisticated approach to truth related to the Kripkean ideas we have been discussing, in a setting which holds to classical logic.

McGee relies on two notions: truth and definite truth. Definite truth is a form of the idea we glossed as determinateness. But, McGee describes this idea using some very sophisticated logical techniques. We will mention them briefly, for those familiar with the technical background. Formally, for McGee, definite truth is identified with provability in a partially interpreted language, using an extension of classical logic which takes in facts about the partial interpretation known as $\mathcal{A}$-logic. It is thus different from the grounding notion we just discussed. McGee treats ‘definitely’ as a *predicate*, on par with the truth predicate, and not as an operator on sentences as some developments do. With the right notion of definite truth, McGee shows that a partially interpreted language containing its own truth predicate can meet restricted forms of capture and release put in terms of definite truth. Where $\Def$ is the definiteness predicate, McGee shows how to link truth and definite truth, by showing how to validate:

$$ \begin{align} \Def (\left\ulcorner A\right\urcorner) & \textrm{ iff } \Def (\left\ulcorner \Tr(\left\ulcorner A\right\urcorner)\right\urcorner)\\ \Def (\left\ulcorner \neg A\right\urcorner) & \textrm{ iff } \Def (\left\ulcorner \neg \Tr(\left\ulcorner A\right\urcorner)\right\urcorner) \end{align} $$

Indeed, McGee shows that these conditions can be met within a theory of both truth and definite truth, where truth satisfies appropriate forms of capture and release, and also where a formal statement of bivalence for truth comes out definitely true. McGee thus provides a theory which has strongly self-applicative truth and definite truth, within a classical setting.

Though truth may satisfy the formal property of bivalence, it is crucial to McGee’s approach that definite truth is an open-ended notion, which may be strengthened (formally, by strengthening a partially interpreted language). Thus, definite truth satisfies weaker forms of capture and release than truth itself. (Some instances of $\Def(\left\ulcorner A\right\urcorner) \rightarrow A$ fail to be definitely true, according to McGee.) Furthermore, McGee suggests that this behavior of truth and definite truth makes truth a *vague* predicate. It remains disputed whether McGee’s theory avoids the kind of revenge problems that plague other Kripkean approaches.

##### Determinateness and truth in a classical context

More recently, theories of truth and determinateness have been developed which overcome some of the difficulties of compositional approaches. More specifically, they improve on the classification of the Liar and related paradoxical sentences, or on certain features of the compositional principles themselves (such as the asymmetries we observed in $\mathsf{KF}$).

As we briefly noted, a notion of determinateness is implicit in classical implementations of Kripke’s construction. However, this does not allow such approaches to classify a Liar sentence as indeterminate, since this would require showing that *L* is neither true nor false, which $\mathsf{KF}$ (by itself) does not do.

Feferman (2008)[^feferman-2008] introduces the theory $\mathsf{DT}$ (‘Determinate Truth’), which features a primitive determinateness predicate alongside truth. Principles for determinateness are quite obviously distinct from those for truth. For example, plausibly, a sentence is determinate if and only if its negation is, whereas the same principle would be absurd for truth. For Feferman, determinateness serves to restrict the classical compositional principles: if a sentence is determinate, then the principles of $\mathsf{FSN}$ apply to it. A primitive determinateness predicate also plays a central role in the recent theory $\mathsf{CD}$ (‘Classical Determinateness’, Fujimoto and Halbach 2024)[^fujimoto-2024]. In $\mathsf{CD}$, determinateness restricts the application of truth-iteration principles, while truth itself is classically compositional over connectives and quantifiers.

These sophisticated theories are interesting in their own right but we cannot analyze them in detail here: we limit ourselves to the insights they offer into the treatment of the Liar and related paradoxes. On the one hand, they prove that Liar sentences are not determinate, thereby expressing their paradoxical status and overcoming one of the expressive limitations of $\mathsf{KF}$. On the other hand, they face a form of revenge. Reinhardt (1986)[^reinhardt-1986] and more recently Bacon (2015)[^bacon-2015] have observed that, insofar as classical theories validate a schema expressing that the T-schema holds restrictedly, i.e. of the form

$H\ulcorner A \urcorner \to (\Tr \ulcorner A \urcorner \leftrightarrow A)$

for some predicate *H*, a diagonalization argument shows that they prove the formula $C \wedge \neg H\ulcorner C \urcorner$ for a sentence *C*. Since $\mathsf{KF}$, $\mathsf{DT}$, and $\mathsf{CD}$ all validate a version of the schema (with *H* replaced by their determinateness predicate), they are all vulnerable to this kind of revenge. How serious is this difficulty? That depends. The Reinhardt/Bacon observation shows that classical theories cannot adopt a general rule to the effect that whenever a sentence is proved, it is determinate, for otherwise $C \wedge \neg H \ulcorner C \urcorner$would yield immediate inconsistency. This is familiar. It is essentially the situation of $\mathsf{KF}$ (augmented with the consistency principle) in the case of the Liar, where it proves $L \wedge \neg \Tr \ulcorner L \urcorner$but cannot be closed under the principle that whatever is proven is true. Whatever one makes of this, it is striking that the behavior of $\mathsf{KF}$ + consistency is mirrored in classical theories that articulate restrictions of the T-schema. For some, it might be a revenge paradox. For others, it might be the defining feature of their treatment of the Liar. Indeed, many contextualist accounts begin here. We now turn to them.

### 4.4 Contextualist approaches

Another family of proposed solutions to the Liar consists of *contextualist solutions*. These also make use of classical logic, but base their solutions primarily on some ideas from the philosophy of language (for more on semantic paradoxes and natural languages, see Glanzberg (2026)[^glanzberg-2026]). They take the basic lesson of the Liar to be that truth ascriptions show some form of *context dependence*, even in otherwise non-context-dependent fragments of a language. They seek to explain how this can be so, and rely on it to resolve the problems faced by the Liar.

Contextualist theories share with a number of approaches we have already seen the idea that there is something indeterminate or semantically not well-formed about our Liar sentence *L*. But, contextualist views give a special role to issues of ‘revenge’ and lack of expressive power.

#### 4.4.1 Instability and revenge

One way of thinking about why the truth predicate is not well-behaved on the Liar sentence is that there is not really a well-defined truth bearer provided by the Liar sentence. To make this vivid (as discussed by C. Parsons (1974)[^parsons-1974]), suppose that truth bearers are propositions expressed by sentences in contexts, and that the Liar sentence (which, in this case, we might formulate as ‘this sentence does not express a true proposition’) fails to express a proposition. This is the beginnings of an account of how the Liar winds up ungrounded or in some sense indeterminate. At least, we should not expect $\Tr$ to be well-behaved where sentences fail to express propositions.

As it stands, however, this is an unstable proposal. We can reason that if the Liar sentence fails to express a proposition, it fails to express a true proposition. In the manner of a revenge paradox, if our Liar sentence had originally said ‘this sentence does not express a true proposition’, then we would have our Liar sentence back. And, we have shown that this sentence says something true, and so expresses a true proposition. Thus, from the assumption that the Liar sentence is indeterminate or lacks semantic status, we reason that it must have proper semantic status, and indeed say something true. We are hence back in paradox.

Contextualists do not see this as a new ‘revenge’ paradox, but the basic problem posed by the Liar. First of all, in a setting where sentences are context dependent, the natural formulation of a truth claim is always in terms of expressing a true proposition, or some related semantically careful application of the truth predicate. But more importantly, to the contextualist, the main issue behind the Liar is embodied in the reasoning on display here. It involves two key steps. First, assigning the Liar semantically defective status—failing to express a proposition or being somehow indeterminate. Second, concluding from the first step that the Liar must be true—and so not indeterminate or failing to express a proposition—after all. Both steps appear to be the result of sound reasoning, and so the conclusions reached at both must be true. The main problem of the Liar, according to a contextualist, is to explain how this can be, and how the second step can be non-paradoxical. (Such reasoning is explored by Glanzberg (2004c)[^glanzberg-2004c] and C. Parsons (1974)[^parsons-1974]. For a critical discussion, see Gauker (2006)[^gauker-2006].)

Thus, contextualists seek to explain how the Liar sentence can have unstable semantic status, switching from defective to non-defective in the course of this sort of inference. They do so by appealing to the role of *context* in determining the semantic status of sentences. Sentences can have different semantic status in different contexts. Thus, to contextualists, there must be some non-trivial effect of context, often referred to as a *context shift*, involved in the Liar sentence, and more generally, in predication of truth. On all such views, the context shift is the engine that turns a would-be revenge into change of semantic status rather than a contradiction. Contextualists have debated extensively on such a context shift: what triggers it, where it occurs in the course of a Liar reasoning, and how it is best modeled. For more on this, see Glanzberg (2001, 2004a)[^glanzberg-2001][^glanzberg-2004a], Gauker (2006)[^gauker-2006], Murzi and Rossi (2018), and Mankowitz (2023a, 2023b, 2026)[^mankowitz-2023a][^mankowitz-2023b][^mankowitz-2026].

#### 4.4.2 Contextual parameters on truth predicates

One prominent contextualist approach, advocated by Burge (1979)[^burge-1979] and developed by Koons (1992)[^koons-1992] and Simmons (2009)[^simmons-2009], starts with the idea that the Tarskian hierarchy itself offers a way to see the truth predicate as context dependent. Tarski’s hierarchy postulates a hierarchy of truth predicates $\Tr_i$. What if *i* is not merely a marker of level in a hierarchy, but a genuine contextual parameter? If so, then the Liar sentence is in fact context-dependent: it has the form $\neg \Tr_i (\left\ulcorner L\right\urcorner)$, where *i* is set by context. Context then sets the level of the truth predicate.

This idea can be seen as an improvement on the original Tarskian approach in several respects. First, once we have a contextual parameter, the need to insist that Liar sentences are never well-formed disappears. Hence, we can think of each $\Tr_i$ as including some limited range of applicability to sentences of its own language. Using the Kripkean techniques like the closed-off construction we reviewed above, predicates like $\Tr_i$ can be constructed which have as much self-applicability as Kripke’s own. (Burge 1979 and the postscript to C. Parsons 1974 consider briefly how Kripkean techniques could be applied in this setting. Though he works in a very different setting, ideas of Gaifman (1988, 1992)[^gaifman-1988][^gaifman-1992] can be construed as showing how even more subtle ways of interpreting a context-dependent truth predicate can be developed.)

With suitable care, other problems for the Tarskian hierarchy can be avoided as well. Burge proposes that the parameter *i* in $\Tr_i$ is set by a Gricean pragmatic process. In effect, speakers implicate that *i* is to be set to a level for which the discourse they are in can be coherently interpreted (with a maximal coherent extension for $\Tr_i)$. Thus, truth does indeed find its own level, and so Kripke’s objection about how to specify levels for non-paradoxical sentences may be countered.

This approach gives substance to the idea that the Liar sentence is context dependent. Any sentence containing $\Tr_i$ will be context dependent, inheriting a contextual parameter along the way. This offers a way to make sense of the arguments for the instability of the semantic status of *L* that motivated contextualism. In an initial context, we specify some level *i*. This is the level at which *L* is interpreted. Call this interpretation $L_i . L_i$ says $\neg \Tr_i (\left\ulcorner L_{i}\right\urcorner)$. By the usual Liar reasoning, we show that $L_i$ must lack determinate semantic status—or fail to express a proposition. As we discussed, we then reason that *L* must come out true. According to the contextualist view at hand, this is the claim that $L_i$ is true according to some other context, where a wider truth predicate is in play. This amounts to being true at some higher level of the hierarchy. We can conclude, for instance, that the Liar sentence as it was used at level *i* is true according to a wider level $k \gt i$. Hence, $\Tr_k (\left\ulcorner L_{i}\right\urcorner)$, where $k \gt i$.

This form of contextualism thus maintains that once we see the context-dependent behavior of $\Tr_i$, we can make good sense of the instability of *L*. This can be seen as an improvement on the Tarskian view, and embodying some of the techniques of classical logic we reviewed in §4.3. Depending how the Burge view is spelled out technically, it will either have full capture and release at each level, or capture and release with the same restrictions as the closed-off Kripke construction.

The view that posits contextual parameters on the truth predicate does face a number of questions. For instance, it is fair to ask why we think the truth predicate really has a contextual parameter, especially if we mean a truth predicate like the one we use in natural language. Merely noting that such a parameter would avoid paradox does not show that it is present in natural language. Furthermore, whether it is acceptable to see truth as coming in levels at all, context-based or not, remains disputed. (Not all those who advocate contextual parameters on the truth predicate agree about the role of hierarchy. In particular, Simmons (2009)[^simmons-2009] advocates a view he labels the ‘singularity theory’ which he proposes avoids outright hierarchical structures.) Finally, the Burgean appeal to Gricean mechanisms to set levels of truth has been challenged. (For instance, Gaifman (1992)[^gaifman-1992] asks if the Gricean process does any substantial work in Burge’s account.)

Contextualist approaches come in many varieties, each of which makes use of slightly different apparatus. With contextualist theories the choice often turns on issues in philosophy of language as well as logic. We already noted a different way of developing contextualist ideas from Gaifman (1988, 1992)[^gaifman-1988][^gaifman-1992]. We will now briefly review a few more alternatives.

#### 4.4.3 Contextual effects on quantifier domains

Another contextualist approach, stemming from work of C. Parsons (1974)[^parsons-1974], seeks to build up the context dependence of the Liar sentence, and ultimately the context dependence of the truth predicate, from more basic components. The key is to see the context dependence of the Liar sentence as derived from the context dependence of quantifier domains.

Quantification enters the picture when we think about how to account for predication of truth when sentences display context dependence. In such an environment, it does not make good sense to predicate truth of sentences directly. Not all sentences will have the right kind of determinate semantic properties to be truth bearers; or, as we have been putting it, not all sentences will express propositions. But then, to say that a sentence *S* is true in context *c* is to say that *there is* a proposition *p* expressed by *S* in *c*, and that proposition *p* is true. Therefore truth predications, properly spelled out, involve a quantification over propositions.

The current contextualist proposal starts with the observation that quantifiers in natural language typically have context-dependent domains of quantification. When we say ‘Everyone is here’, we do not mean everyone in the world, but everyone in some contextually provided subdomain. Context dependence enters the Liar, according to this contextualist view, in the contextual effects on the domain of the propositional quantifier $\exists p$.

In particular, this domain must *expand* in the course of the reasoning about the semantic status of the Liar. In the initial context, $\exists p$ must range over a small enough domain that there is no proposition for *L* to express. In the subsequent context, the domain expands to allow *L* to express some true proposition. Proposals for how this expansion happens, and how to model the truth predicate and the relation of expressing a proposition in the presence of the Liar, have been explored by Glanzberg (2001, 2004a)[^glanzberg-2001][^glanzberg-2004a], building on work of C. Parsons (1974)[^parsons-1974]. Defenders of this approach argue that it does better in locating the locus of context dependence than the parameters on truth predicates view.

#### 4.4.4 Situation theory

Another variant on the contextualist strategy for resolving the Liar, developed by Barwise and Etchemendy (1987) and Groeneveld (1994)[^groeneveld-1994], relies on *situation theory* rather than quantifier domains to provide the locus of context dependence. Situation theory is a highly developed part of philosophy of language, so we shall again give only the roughest sketch of how their view works.

A situation is a partial state the world might be in: something like *a* being *F*. Situations are classified by what are called situation types. A proposition involves classifying a situation as being of a situation type. Thus, a proposition $\{s$; [$\sigma]\}$ tells us that situation *s* is of type *σ*. The situation *s* here plays a number of roles, including that of providing a context.

When it comes to the Liar, Barwise and Etchemendy construe Liar propositions as having the form $f_s = \{s$; [$\Tr,f_s$; 0]$\}$, relative to an initial situation *s*. This is a proposition $f_s$ which says of itself that its falsity is a fact that holds in *s*. (In Barwise and Etchemendy’s notation, the 0 indicates falsity, so the situation type is that the state of affairs of the proposition being false holds. The proposition says this is a fact that holds in *s*.) There is a sense in which this proposition cannot be expressed. In particular, the state of affairs $\langle \Tr,f_s$; $0\rangle$ cannot be in *s*. (Actually, Barwise and Etchemendy say that the proposition is expressible, but give up on what they call the *F*-closure of *s*. But there is a core observation in common between these two points, and the details do not matter for our purposes here.) There is then a distinct situation $s' = s \cup \{\langle \Tr,f_s$; $0\rangle \}$, and the proposition $\{s'$; [$\Tr,f_s$; 0]$\}$ relative to this new situation—this new ‘context’—is true.

This idea clearly has a lot in common with the restriction on quantifier domains view. In particular, both approaches seek to show how the domain of contents expressible in contexts can expand, to account for the instability of the Liar sentence. For discussion of relations between the situation-theoretic and quantifier domain approaches, see Glanzberg (2004a)[^glanzberg-2004a]. Barwise and Etchemendy discuss relations between their situation-based and a more traditional approach in 1987 (Ch. 11). For a detailed match-up between the Barwise and Etchemendy framework and a Burgean framework of indexed truth predicates, see Koons (1992)[^koons-1992].

#### 4.4.5 Issues for contextualism

It is a key challenge to contextualists to provide a full and well-motivated account of the source and nature of the context shift involved in the Liar, though of course, many contextualists believe they have met this challenge. In favor of the contextualist approach is that it takes the revenge phenomenon to be the basic problem, and so is largely immune to the kinds of revenge issues that affect other approaches we have considered. But, it may be that there is another form of revenge which might be applied. To retain consistency, contextualists must apply restrictions on quantifiers to such quantifiers as ‘all contexts’. To achieve this, it must presumably be denied that there are any absolutely unrestricted quantifiers. Glanzberg (2004b, 2006)[^glanzberg-2004b][^glanzberg-2006] argues this is the correct conclusion, while Rossi (2023)[^rossi-2023] argues that contextualism about truth is broadly compatible with absolute generality, i.e. the possibility of quantifying over absolutely everything. For more on this issue, see Bacon (2015)[^bacon-2015] and the papers in Rayo and Uzquiano (2006).

### 4.5 The revision theory

Another approach to the Liar, advocated by Gupta (1982)[^gupta-1982], Herzberger (1982)[^herzberger-1982], Gupta and Belnap (1993), and a number of others, is the *revision theory of truth*. This approach shares some features with the views we surveyed in §4.3, in that it takes classical logic for granted. We also believe it has an affinity with the views discussed in §4.4, as it rethinks some basic aspects of semantics. But it is a distinctive approach. We will sketch some of the fundamentals of this view. For a discussion of the foundations of the revision theory, and its relations to contextualism, see L. Shapiro (2006)[^shapiro-2006]. More details, and more references, may be found in the entry on the revision theory of truth.

The revision theory of truth starts with the idea that we may take the T-schema at face value. Indeed, Gupta and Belnap (1993) take up a suggestion from Tarski (1944)[^tarski-1944], that the instances of the T-schema can be seen as partial definitions of truth (presumably with all the instances together, for the right language or family of languages, constituting a complete definition). At the same time, the revision theory holds fast to classical logic. Thus, we already know, we have the Liar paradox for any language with enough expressive resources to produce Liar sentences.

In response, the revision theory proposes a different way of approaching the semantic properties of the truth predicate. In keeping with our practices here, we may begin with a classical model $\mathcal{M}_0$ for a language $\mathcal{L}_0$ without a truth predicate, and consider what happens when we add a truth predicate $\Tr$ to form the extended language $\mathcal{L}^{+}_0$. This language has a full self-applicative truth predicate, and so can generate the Liar sentence *L*.

To build a classical model for $\mathcal{L}^{+}_0$, we need an extension for $\Tr$. Let us pick a set: call it *H* for a *hypothesis* about what the extension of $\Tr$ might be. *H* may be $\varnothing$, it may be the entire domain of $\mathcal{M}_0$, or it may be anything else. It need not be a particularly good approximation of the semantic properties of $\Tr$.

Even if it is not, $\langle \mathcal{M}_0,H\rangle$ still provides a classical model, in which we can interpret $\mathcal{L}^{+}_0$. With that, we can in effect apply the T-schema, relative to our hypothesis *H*, and see what we get. More precisely, we can let $\tau(H) = \{\left\ulcorner A\right\urcorner | A$ is true in $\langle \mathcal{M}_0,H\rangle \}. \tau(H)$ is generally a better hypothesis about what is true in our language than *H* might have been. At least, clearly, if *H* made foolish guesses about the truth of sentence of the truth-free fragment $\mathcal{L}_0$, they are corrected in $\tau(H)$, which contains everything from $\mathcal{L}_0$ true in $\mathcal{M}_0$. Thus, $\langle \mathcal{M}_0,\tau(H)\rangle$ is generally a better model of $\mathcal{L}^{+}_0$ then $\langle \mathcal{M}_0,H\rangle$.

Better in many respects. But when it comes to paradoxical sentences like *L*, we see something different. As a starting hypothesis, let us consider $H = \varnothing$. Consider what happens to the truth of *L* as we apply *τ*:

| *n* | truth value of *L* in $\langle \mathcal{M}_0,\tau^n (\varnothing)\rangle$ |
| --- | --- |
| 0 | true |
| 1 | false |
| 2 | true |
| 3 | false |
| 4 | true |
| $\vdots$ | $\vdots$ |

The Liar sentence never stabilizes under this process. We reach an alternation of truth values which will go on for ever. This shows, according to the revision theory, that truth is a circular concept. As such, it does not have an extension in the ordinary sense. Rather, it has a rule for revising extensions, which never stabilizes.

In the terminology of the revision theory, *τ* is a *revision rule*. It takes us from one hypothesis about the interpretation of $\Tr$ to another. Sequences of values we generate by such revision rules, starting with a given initial hypothesis, are *revision sequences*. We leave to a more full presentation the important issue of the right way to define *transfinite* revision sequences. (See the entry on revision theories of truth.)

The characteristic property of paradoxical sentences like the Liar sentence is that they are unstable in revision sequences: there is no point in the sequence at which they reach a stable truth value. This classifies sentences as stably true, stably false, and unstable. The revision theory develops notions of consequence based on these, and related notions. See the entry on revision theories of truth for further exposition of this rich theory.

### 4.6 Inconsistency views

In §2.3.3 we saw that the Liar paradox, in the presence of unrestricted capture and release and classical logic, leads to contradiction. So long as we have EFQ (as classical logic does), this results in triviality. Most of the proposed solutions we have considered (with the exception of the revision theory) try to avoid this result somehow, either by restricting capture and release or departing from classical logic. But there is another idea that has occasionally been defended, that the Liar paradox simply shows that the kinds of languages we speak, which contain their own truth predicates, are *inconsistent*.

This is not an easy view to formulate. Though Tarski himself seemed to suggest something along these lines (for natural languages, specifically), it was argued by Herzberger (1967)[^herzberger-1967] that it is impossible to have an inconsistent language.

In contrast, Eklund (2002)[^eklund-2002] takes seriously the idea that our semantic intuitions, expressed, for instance, by unrestricted capture and release, really are inconsistent. Eklund grants that this does not make sense if these intuitions have their source simply in our grasp of the truth conditions of sentences. But he suggests an alternative picture of semantic competence which does make sense of it (closely related to conceptual role views of meaning). He suggests that we think of semantic competence in terms of a range of principles speakers are disposed to accept in virtue of knowing a language. Those principles may be inconsistent. But even so, they determine semantic values. Semantic values will be whatever comes closest to satisfying the principles—whatever makes them maximally correct—even if nothing can satisfy all of them due to an underlying inconsistency.

Eklund thus supports an idea suggested by Chihara (1979)[^chihara-1979]. Chihara’s main aim is to provide what he calls a *diagnosis* of the paradox, which should explain why the paradox arises and why it appears compelling. But along the way, he suggests that the source of the paradox is our acceptance of the T-schema (by convention, he suggests), in spite of its inconsistency.

A related, though distinct, view is defended by Patterson (2007, 2009)[^patterson-2007][^patterson-2009]. Patterson argues that competence with a language puts one in a cognitive state relating to an inconsistent theory—one including the unrestricted T-schema and governed by classical logic. He goes on to explore how such a cognitive state could allow us to successfully communicate, in spite of relating us to a false theory.

A different sort of inconsistency theory is advocated by Scharp (2013)[^scharp-2013]. Scharp argues that truth is an inconsistent concept, like the pre-relativistic concept of mass. As such, it is unsuitable for careful theorizing. What we need to do, according to Scharp, is replace the inconsistent concept of truth with a family of consistent concepts that work better. Scharp develops just such a family of concepts, and offers a theory of them.

### 4.7 Theories of paradoxicality

Having surveyed specific solutions to the Liar, we briefly turn to work that studies *paradoxicality itself*, that is, what makes a sentence or argument paradoxical.

Many solutions to the Liar come with their own characterizations (e.g., why classical logic or capture/release must be restricted to deal with Liar sentences). By contrast, theories of paradoxicality aim for a theory-independent account of what makes a paradox a paradox. They typically take the Liar as a paradigm and generalize its paradox-defining features. These accounts complement, rather than replace, the solution-oriented characterizations reviewed above.

Gallovich and Rosenblatt (2026) survey several conceptions explicitly discussed or implicitly used in the literature. On the naive conception, a sentence is paradoxical when absurdity follows from applying seemingly innocuous principles (such as capture and release, or LEM) to it. Examples of this conception are found, or critically discussed, in Bacon (2015)[^bacon-2015], Cook (2011)[^cook-2011], Hsiung (2021)[^hsiung-2021], Incurvati and Schlöder (2023), ch. 7, and Murzi and Rossi (2020).

The Inclosure conception, famously advocated by Priest (1994)[^priest-1994], seeks to derive semantic (and non-semantic) paradoxes from a single Russellian scheme. If many paradoxes share a common structure, Priest argues, they should also share a common solution (this is known as the Principle of Uniform Solution). While this idea has gained some acceptance, it is controversial whether the Inclosure scheme really uncovers such a common structure; see Beall (2014)[^beall-2014], Smith (2000)[^smith-2000], and Weber (2019)[^weber-2019] for criticism.

Proof-theoretic characterizations also exist. Building on Prawitz’s (1965)[^prawitz-1965] suggestion that set-theoretic paradoxes can be blocked by restricting derivations in natural deduction so that they must be ‘normal’ (i.e., derivations with no immediate introduction-elimination detours), Tennant (1982, 2021)[^tennant-1982][^tennant-2021] and Schroeder-Heister and Tranchini (2017, 2021) extend this idea to Liar-like paradoxes (see Rosenblatt 2024 for critical discussion)[^rosenblatt-2024].

A different line uses graph-theoretic tools to model referential patterns and valuation constraints of paradoxical sentences, and to classify them. See Barwise and Etchemendy (1987), Gaifman (1992)[^gaifman-1992], Walicki (2009)[^walicki-2009], Rabern et al. (2013), Beringer and Schindler (2017), Cook (2014)[^cook-2014], Rossi (2019)[^rossi-2019].

Finally, Kripke-style fixed-point theories offer characterizations that accommodate different logics; the same holds for more recent revision-theoretic approaches (e.g., Field 2008, 2014, 2016, 2021)[^field-2008][^field-2014][^field-2016][^field-2021].

## 5. Concluding Remarks

There is much more to say about the Liar paradox than we have covered here: there are more approaches to the Liar variants we have mentioned, and more related paradoxes like those of denotation, properties, etc. There are also more important technical results, and more important philosophical implications and applications. Our goal here has been to be more suggestive than exhaustive, and we hope to have given the reader an indication of what the Liar paradox is, and what its consequences might be.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=liar-paradox). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/liar-paradox/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=liar-paradox&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/liar-paradox/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- Dunn, J. Michael, 1969, “[Natural language versus formal language](http://www.indiana.edu/~phil/people/papers/natvsformal.pdf),” (PDF of unpublished manuscript), presented at the joint APA–ASL Symposium, New York, NY, December 27, 1969.

[Please contact the authors with other suggestions.]

## Related Entries

Curry’s paradox | dialetheism | Gödel, Kurt | Gödel, Kurt: incompleteness theorems | logic: many-valued | logic: provability | self-reference | Tarski, Alfred | Tarski, Alfred: truth definitions | truth | truth: axiomatic theories of | truth: revision theory of | vagueness

### Acknowledgments

The authors would like to thank the referee for helpful comments.

## Notes（原文脚注）

[^note-1]: Thus, a paradox nearly occurs in the New Testament. For a delightful discussion, see Anderson (1970)[^anderson-1970]. For a more thorough discussion of the history of the Liar, see Sorensen (2003)[^sorensen-2003]. There has been some important recent work on medieval theories of the Liar, and their relevance to current approaches. See the papers in Rahman, Tulenheimo, and Genot (2008), and, for instance, Read (2002, 2006)[^read-2002][^read-2006]; Restall (2008)[^restall-2008]; and Simmons (1993).

[^note-2]: Terminology here is not uniform. Van Fraassen (1968)[^fraassen-1968] introduced the term ‘strengthened Liar’ to name what we are calling the simple-untruth Liar. Van Fraassen’s term, however, has been more often used for a ‘revenge-like’ paradox in the manner of C. Parsons (1974)[^parsons-1974], as we discuss in §4.1.3.

[^note-3]: A note on terminology: when talking about a language, we mean an *interpreted language*, including a syntax, an interpretation or model (containing a domain of objects and interpretations for non-logical vocabulary), and a valuation scheme which determines truth in the model for complex formulas. Simplifying for exposition, we shall often speak loosely and blur the distinction between a logic and a language (thinking, in a not strictly accurate fashion, of the valuation scheme as the relevant bit of ‘logical consequence’ for the language). Moreover, at some points, it is a *theory* rather than a language that is at issue. We note when such distinctions become important. Given the wide range of ideas in logic that we survey in rather brief form in this essay, we leave many such subtleties to more leisurely presentations.

[^note-4]: Hence, our terminology of ‘rule forms’ may not be ideal. For our limited purposes here, were use it merely to mark the difference between a valid argument, recorded as a ‘rule form’, and the provability of a conditional, reported as a ‘conditional form’. Though this is not the only logical distinction to be drawn, it is the one which will be of most importance as our discussion progresses.

[^note-5]: The situation with formal languages is actually somewhat subtler than our brief discussion indicates. In most cases, corner quotes really indicate formal terms for Gödel numbers of sentences, and are not genuine quotation marks in the usual sense (e.g., denoting the expression ‘inside’ them). Hence, the sense in which such languages have *reference* to sentences is delicate. Yet with very minimal resources, syntax can be *represented* and diagonal sentences constructed. Hence, there is a sense, albeit subtle, in which such languages can express self-reference. See the entries on provability logic and Gödel (the section on the incompleteness theorems), as well as Heck (2007, 2026)[^heck-2007][^heck-2026].

[^note-6]: It is this principle or rule that we repeated above by saying that by the lights of many logical theories an arbitrary contradiction implies absurdity or triviality, in the sense of implying all sentences. The principle is often labeled by its classical title ‘ex falso quodlibet’, and hence its customary abbreviation is ‘EFQ’ in spite of the name ‘explosion’.

[^note-7]: This is often called ‘$\vee$-Out’ or ‘$\vee$-Elim’ or, more suggestively, ‘reasoning by cases’.

[^note-8]: Again for the classical case, Friedman and Sheard (1987) provide an exhaustive list of inconsistent theories relative to a fairly weak base theory. They show that either of the classical conditional forms of capture or release are inconsistent by themselves, over the base theory supplemented by the right choice of principles providing for completeness $(\Tr(\left\ulcorner A\right\urcorner) \vee \Tr (\left\ulcorner\neg A\right\urcorner))$ or consistency $(\neg(\Tr (\left\ulcorner A\right\urcorner) \wedge \Tr (\left\ulcorner\neg A\right\urcorner)))$ of truth.

[^note-9]: Beall and Glanzberg (2008) have argued for a close connection between general views on the nature of truth and available avenues for resolving the paradox.

[^note-10]: The logic was first advanced by Asenjo (1966)[^asenjo-1966], though has come to be popularized by Priest’s work. The name ‘*LP*’ is due to Priest, while the term ‘dialetheism’ was coined by Priest and Routley.

[^note-11]: A technical note: Kripke defined being grounded as appearing in the *minimal* fixed point. We have not discussed other fixed points here, but there are many, and a sentence can appear in them without appearing in the minimal one.

[^achourioti-2015]: Achourioti, Theodora, Henri Galinon, José Martinez Fernández, and Kentaro Fujimoto (eds), 2015, *Unifying the Philosophy of Truth*, Berlin: Springer.

[^aczel-1980]: Aczel, Peter, 1980, “Frege structures and the notions of proposition, truth and set”, in *The Kleene Symposium*, J. Barwise, H.J. Keisler, and K. Kunen (eds), Amsterdam: North-Holland, 31–59.

[^anderson-1970]: Anderson, Alan Ross, 1970, “St. Paul’s epistle to Titus”, in Martin 1970: 1–11.

[^asenjo-1966]: Asenjo, F.G., 1966, “A calculus of antinomies”, *Notre Dame Journal of Formal Logic*, 7(1): 103–105. doi:10.1305/ndjfl/1093958482

[^bacon-2015]: Bacon, Andrew, 2015, “Can the classical logician avoid the revenge paradoxes?”, *The Philosophical Review*, 124(3): 299–352. doi:10.1215/00318108-2895327

[^barrio-2012]: Barrio, Eduardo, 2012, “The Yablo paradox and circularity”, *Análisis Filosófico*, 32(1): 7–20.

[^barrio-2015]: Barrio, Eduardo, Lucas Rosenblatt, and Diego Tajer, 2015, “The logics of strict-tolerant logic”, *Journal of Philosophical Logic*, 44(5): 551–571. doi:10.1007/s10992-014-9342-6

[^barwise-1987]: Barwise, Jon and John Etchemendy, 1987, *The Liar*, Oxford: Oxford University Press.

[^başkent-2019]: Başkent, Can and Thomas Macaulay Ferguson (eds.), 2019, *Graham Priest on Dialetheism and Paraconsistency*, Cham: Springer.

[^beall-2001]: Beall, Jc, 2001, “Is Yablo’s paradox non-circular?”, *Analysis*, 61(3): 176–187. doi:10.1111/1467-8284.00292

[^beall-2005]: –––, 2005, “Transparent disquotationalism”, in Beall and Armour-Garb 2005: 7–22.

[^beall-2007]: ––– (ed.), 2007, *Revenge of the Liar*, Oxford: Oxford University Press.

[^beall-2009]: –––, 2009, *Spandrels of Truth*, Oxford: Oxford University Press.

[^beall-2011]: –––, 2011, “Adding to relevant restricted quantification”, *Australasian Journal of Logic*, 10: 36–44. [[Beall 2011 available online](https://ojs.victoria.ac.nz/ajl/article/view/1823)]

[^beall-2014]: –––, 2014, “End of inclosure”, *Mind*, 123(491): 829–849. doi:10.1093/mind/fzu075

[^beall-2015]: –––, 2015, “Free of detachment: logic, rationality, and gluts”, *Noûs*, 49: 410–423. doi:10.1111/nous.12029

[^beall-2005-2]: Beall, Jc and Bradley Armour-Garb (eds), 2005, *Deflationism and Paradox*, Oxford: Oxford University Press.

[^beall-2006]: Beall, Jc, Ross T. Brady, Allen P. Hazen, Graham Priest, and Greg Restall, 2006, “Relevant restricted quantification”, *Journal of Philosophical Logic*, 35(6): 587–598. doi:10.1007/s10992-005-9008-5

[^beall-2008]: Beall, Jc and Michael Glanzberg, 2008, “Where the paths meet: Remarks on truth and paradox”, in *Midwest Studies in Philosophy Volume XXXII: Truth and its Deformities*, P.A. French and H.K. Wettstein (eds), Boston: Wiley-Blackwell: 169–198.

[^beall-2013]: Beall, Jc and Julien Murzi, 2013, “Two flavors of Curry’s paradox”, *Journal of Philosophy*, 110(3): 143–165. doi:10.5840/jphil2013110336

[^beringer-2017]: Beringer, Timo and Thomas Schindler, 2017, “A graph-theoretic analysis of the semantic paradoxes”, *Bulletin of Symbolic Logic*, 23(4): 442–492. doi:10.1017/bsl.2017.37

[^bonnay-2015]: Bonnay, Denis, and Floris Tijmen van Vugt, 2015, “Groundedness, truth, and dependence”, in Achourioti et al. 2015: 355–368. doi:10.1007/978-94-017-9673-6_18

[^brady-1989]: Brady, Ross T., 1989, “The non-triviality of dialectical set theory”, in *Paraconsistent Logic: Essays on the Inconsistent*, G. Priest, R. Routley, and J. Norman (eds), Munich: Philosophia Verlag, 437–470.

[^burge-1979]: Burge, Tyler, 1979, “Semantical paradox”, *Journal of Philosophy*, 76(4): 169–198. doi:10.2307/2025724 Reprinted in Martin 1984: 83–117.

[^burgess-1986]: Burgess, John P., 1986, “The truth is never simple”, *Journal of Symbolic Logic*, 51(3): 663–681. doi:10.2307/2274021

[^cantini-1996]: Cantini, Andrea, 1996, *Logical Frameworks for Truth and Abstraction: An Axiomatic Study*, Amsterdam: Elsevier.

[^cantini-2003]: –––, 2003, “The undecidability of Grišin’s set theory”, *Studia Logica*, 74(3): 345–368. doi:10.1023/A:1025159016268

[^chihara-1979]: Chihara, Charles, 1979, “The semantic paradoxes: A diagnostic investigation”, *Philosophical Review*, 88(4): 590–618. doi:10.2307/2184846

[^cobreros-2013]: Cobreros, Pablo, Paul Egré, Ellie Ripley, and Robert van Rooij, 2013, “Reaching transparent truth”, *Mind*, 122(488): 841–866. doi:10.1093/mind/fzt110

[^cobreros-2015]: –––, 2015, “Vagueness, truth, and permissive consequence”, in Achourioti et al. 2015: 409–430. doi:10.1007/978-94-017-9673-6_21

[^cook-2006]: Cook, Roy, 2006, “There are non-circular paradoxes (but Yablo’s isn’t one of them)”, *The Monist*, 89(1): 118–149. doi:10.5840/monist200689137

[^cook-2011]: –––, 2011, “The no-no paradox is a paradox”, *Australasian Journal of Philosophy*, 89(3): 467–482. doi: 10.1080/00048402.2010.500671

[^cook-2014]: –––, 2014, *The Yablo Paradox*, Oxford: Oxford University Press.

[^dowden-1984]: Dowden, Bradley H., 1984, “Accepting inconsistencies from the paradoxes”, *Journal of Philosophical Logic*, 13: 125–130. doi:10.1007/BF00453017

[^dummett-1959]: Dummett, Michael, 1959, “Truth”, *Proceedings of the Aristotelian Society*, 59(1): 141–162. doi:10.1093/aristotelian/59.1.141 Reprinted in his 1978, *Truth and Other Enigmas*, Cambridge: Harvard University Press, 1–24.

[^eklund-2002]: Eklund, Matti, 2002, “Inconsistent languages”, *Philosophy and Phenomenological Research*, 64(2): 251–275. doi:10.1111/j.1933-1592.2002.tb00001.x

[^feferman-1984]: Feferman, Solomon, 1984, “Toward useful type-free theories, I”, *Journal of Symbolic Logic*, 49(1): 75–111. doi:10.2307/2274093 Reprinted in Martin 1984: 237–287.

[^feferman-1991]: –––, 1991, “Reflecting on incompleteness”, *Journal of Symbolic Logic*, 56(1): 1–49. doi:10.2307/2274902

[^feferman-2008]: –––, 2008, “Axioms for determinateness and truth”, *The Review of Symbolic Logic*, 1(2): 204–217. doi:10.1017/S1755020308080209

[^field-1994]: Field, Hartry, 1994, “Deflationist views of meaning and content”, *Mind*, 103(411): 249–285. doi:10.1093/mind/103.411.249

[^field-2008]: –––, 2008, *Saving Truth from Paradox*, Oxford: Oxford University Press.

[^field-2014]: –––, 2014, “Naive truth and restricted quantification: Saving truth a whole lot better”, *The Review of Symbolic Logic*, 7(1): 147–191. doi:10.1017/S1755020313000312

[^field-2016]: –––, 2016, “Indicative conditionals, restricted quantification, and naive truth”, *The Review of Symbolic Logic*, 9(1): 181–208. doi:10.1017/S1755020315000301

[^field-2021]: –––, 2021, “Properties, propositions, and conditionals”, *Australasian Philosophical Review*, 4(2): 112–146. doi:10.1080/24740500.2021.1886687

[^field-2022]: –––, 2022, “The power of naïve truth”, *The Review of Symbolic Logic*, 15(1): 225–258. doi:10.1017/S1755020320000167

[^field-2026]: –––, 2026, “Revisionism revisited”, *The Review of Symbolic Logic*, 19(1): 81–109. doi:10.1017/S1755020325100919

[^fjellstad-2016]: Fjellstad, Andreas, 2016, “Naive modus ponens and failures of transitivity”, *Journal of Philosophical Logic*, 45(1): 65–72. doi:10.1007/s10992-015-9351-0

[^frankowski-2004]: Frankowski, Szymon, 2004, “Formalization of a plausible inference”, *Bulletin of the Section of Logic*, 33(1): 41–52.

[^friedman-1987]: Friedman, Harvey and Michael Sheard, 1987, “An axiomatic approach to self-referential truth”, *Annals of Pure and Applied Logic*, 33: 1–21. doi:10.1016/0168-0072(87)90073-X

[^french-2016]: French, Rohan, 2016, “Structural reflexivity and the paradoxes of self-reference”, *Ergo*, 3(5): 113–131. doi:10.3998/ergo.12405314.0003.005

[^fujimoto-2024]: Fujimoto, Kentaro and Volker Halbach, 2024, “Classical Determinate Truth I”, *Journal of Symbolic Logic*, 89(1): 218–261. doi:10.1017/jsl.2023.49

[^gaifman-1988]: Gaifman, Haim, 1988, “Operational pointer semantics: Solution to self-referential puzzles I”, in *Proceedings of the Second Conference on Theoretical Aspects of Reasoning about Knowledge*, M.Y. Vardi (ed.), Los Altos: Morgan Kaufmann, 43–59.

[^gaifman-1992]: –––, 1992, “Pointers to truth”, *Journal of Philosophy*, 89(5): 223–261. doi:10.2307/2027167

[^gallovich-2026]: Gallovich, Camila and Lucas Rosenblatt, 2026, “Conceptions of Paradoxicality”, in Rossi 2026: 103–132.

[^gauker-2006]: Gauker, Christopher, 2006, “Against stepping back: A critique of contextualist approaches to the semantic paradoxes”, *Journal of Philosophical Logic*, 35(4): 393–422. doi:10.1007/s10992-006-9026-y

[^girard-1989]: Girard, Jean-Yves, Paul Taylor, and Yves Lafont, 1989, *Proofs and Types*, Cambridge: Cambridge University Press.

[^glanzberg-2001]: Glanzberg, Michael, 2001, “The Liar in context”, *Philosophical Studies*, 103(3): 217–251. doi:10.1023/A:1010314719817

[^glanzberg-2004a]: –––, 2004a, “A contextual-hierarchical approach to truth and the Liar paradox”, *Journal of Philosophical Logic*, 33(1): 27–88. doi:10.1023/B:LOGI.0000019227.09236.f5

[^glanzberg-2004b]: –––, 2004b, “Quantification and realism”, *Philosophy and Phenomenological Research*, 69(3): 541–572. doi:10.1111/j.1933-1592.2004.tb00518.x

[^glanzberg-2004c]: –––, 2004c, “Truth, reflection, and hierarchies”, *Synthese*, 142(3): 289–315. doi:10.1007/s11229-005-3718-7

[^glanzberg-2006]: –––, 2006, “Context and unrestricted quantification”, in Rayo and Uzquiano 2006: 45–74.

[^glanzberg-2015]: –––, 2015, “Complexity and hierarchy in truth predicates”, in Achourioti et al. 2015: 211–243. doi:10.1007/978-94-017-9673-6_10

[^glanzberg-2026]: –––, 2026, “The Liar paradox in natural languages”, in Rossi 2026: 278–299.

[^grim-1991]: Grim, Patrick, 1991, *The Incomplete Universe*, Cambridge: MIT Press.

[^grishin-1982]: Grishin, Viacheslav Nikolaevich, 1982, “Predicate and set-theoretic calculi based on logic without contractions”, *Mathematics of the USSR—Izvestiya*, 18(1): 41–59. doi:10.1070/IM1982v018n01ABEH001382

[^groeneveld-1994]: Groeneveld, Willem, 1994, “Dynamic semantics and circular propositions”, *Journal of Philosophical Logic*, 23(3): 267–306. doi:10.1007/BF01048483

[^gupta-1982]: Gupta, Anil, 1982, “Truth and paradox”, *Journal of Philosophical Logic*, 11(1): 1–60. doi:10.1007/BF00302338 Reprinted in Martin 1984: 175–235.

[^gupta-1993]: Gupta, Anil and Nuel Belnap, 1993, *The Revision Theory of Truth*, Cambridge: MIT Press.

[^halbach-1997]: Halbach, Volker, 1997, “Tarskian and Kripkean truth”, *Journal of Philosophical Logic*, 26(1): 69–80. doi:10.1023/A:1017977304199

[^halbach-2009]: –––, 2009, “Reducing compositional to disquotational truth”, *The Review of Symbolic Logic*, 2(4): 786–798. doi:10.1017/S1755020309990220

[^halbach-2014]: –––, 2014, *Axiomatic Theories of Truth*, Cambridge: Cambridge University Press, second edition.

[^hallnäs-1991]: Hallnäs, Lars, 1991, “Partial inductive definitions”, *Theoretical Computer Science*, 87(1): 115–142. doi:10.1016/S0304-3975(06)80007-1

[^hallnäs-1991-2]: Hallnäs, Lars and Peter Schroeder-Heister, 1991, “A proof-theoretic approach to logic programming II: Programs as definitions”, *Journal of Logic and Computation*, 1(5): 635–660. doi:10.1093/logcom/1.5.635

[^heck-1997]: Heck, Richard Kimberly, 1997, “Tarski, truth, and semantics”, *Philosophical Review*, 106(4): 533–554 (originally published under the name ‘Richard G. Heck, Jr’). doi:10.2307/2998511

[^heck-2007]: –––, 2007, “Self-reference and the languages of arithmetic”, *Philosophia Mathematica*, 15(1): 1–29 (originally published under the name ‘Richard G. Heck, Jr’). doi:10.1093/philmat/nkl028

[^heck-2012]: –––, 2012, “A Liar paradox”, *Thought*, 1(1): 36–40 (originally published under the name ‘Richard G. Heck, Jr’). doi:10.1002/tht3.5

[^heck-2026]: –––, 2026, “The Liar paradox and meta-mathematics”, in Rossi 2026: 160–190.

[^herzberger-1967]: Herzberger, Hans G., 1967, “The truth-conditional consistency of natural language”, *Journal of Philosophy*, 64(2): 29–35. doi:10.2307/2023768

[^herzberger-1970]: –––, 1970, “Paradoxes of grounding in semantics”, *Journal of Philosophy*, 67(6): 145–167. doi:10.2307/2023885

[^herzberger-1982]: –––, 1982, “Notes on naive semantics”, *Journal of Philosophical Logic*, 11(1): 61–102. doi:10.1007/BF00302339 Reprinted in Martin 1984: 133–174.

[^horsten-2009]: Horsten, Leon, 2009, “Levity”, *Mind*, 118(471): 555–581. doi:10.1093/mind/fzp096.

[^horsten-2011]: –––, 2011, *The Tarskian Turn: Deflationism and Axiomatic Truth*, Cambridge: MIT Press.

[^horsten-2017]: Horsten, Leon and Graham E. Leigh, 2017, “Truth is simple”, *Mind*, 126(501): 195–232. doi:10.1093/mind/fzv184

[^horwich-1998]: Horwich, Paul, 1998, *Truth*, Oxford: Basil Blackwell, second edition.

[^horwich-2003]: –––, 2003, “A minimalist critique of Tarski on truth”, in Jaakko Hintikka, Tommi Kauppinen, Ilkka Niiniluoto and Risto Pitkänen (eds.), Philosophy and Logic in Search of the Polish Tradition, Dordrecht, Springer: 3–12.

[^hsiung-2021]: Hsiung, Ming, 2021, “In what sense is the no-no paradox a paradox?”, *Philosophical Studies*, 179(6): 1915–1937. doi:10.1007/s11098-021-01738-6

[^incurvati-2023]: Incurvati, Luca and Julian Schlöder, 2023, *Reasoning with Attitude: Foundations and Applications of Inferential Expressivism*, Oxford: Oxford University Press.

[^koons-1992]: Koons, Robert C., 1992, *Paradoxes of Belief and Strategic Rationality*, Cambridge: Cambridge University Press.

[^kripke-1975]: Kripke, Saul, 1975, “Outline of a theory of truth”, *Journal of Philosophy*, 72(19): 690–716. doi:10.2307/2024634 Reprinted in Martin 1984: 54–81.

[^leitgeb-1999]: Leitgeb, Hannes, 1999, “Truth and the Liar in De Morgan-valued models”, *Notre Dame Journal of Formal Logic*, 40(4): 496–514. doi:10.1305/ndjfl/1012429715

[^leitgeb-2005]: –––, 2005, “What truth depends on”, *Journal of Philosophical Logic*, 34(2): 155–192. doi:10.1007/s10992-004-3758-3

[^littmann-2004]: Littmann, Greg and Keith Simmons, 2004, “A critique of dialetheism”, in Priest, Beall, and Armour-Garb 2004: 314–335.

[^malinowski-1990]: Malinowski, Grzegorz, 1990, “Q-consequence operation”, *Reports on Mathematical Logic*, 24: 49–59.

[^mankowitz-2023a]: Mankowitz, Poppy, 2023a, “The Liar without relativism”, *Erkenntnis*, 88: 267–288. doi:10.1007/s10670-020-00350-0

[^mankowitz-2023b]: –––, 2023b, “Paradox and context shift”, *Philosophical Studies*, 180(5): 1539–1557. doi:10.1007/s11098-022-01841-2

[^mankowitz-2026]: –––, 2026, “The Liar Paradox, Quantifiers, and Contexts”, in Rossi 2026: 260–277.

[^martin-1970]: Martin, Robert L. (ed.), 1970, *The Paradox of the Liar*, Atascadero: Ridgeview.

[^martin-1984]: ––– (ed.), 1984, *Recent Essays on Truth and the Liar Paradox*, Oxford: Oxford University Press.

[^martin-1975]: Martin, Robert L. and Peter W. Woodruff, 1975, “On representing ‘true-in-L’ in L”, *Philosophia*, 5: 213–217. Reprinted in Martin 1984: 47–51.

[^mcgee-1985]: McGee, Vann, 1985, “How truthlike can a predicate be? A negative result”, *Journal of Philosophical Logic*, 14(4): 399–410. doi:10.1007/BF00649483

[^mcgee-1991]: –––, 1991, *Truth, Vagueness, and Paradox*, Indianapolis: Hackett.

[^mcgee-1992]: –––, 1992, “Maximal consistent sets of instances of Tarski’s schema (T)”, *Journal of Philosophical Logic*, 21(3): 235–241. doi:10.1007/BF00260929

[^meadows-2013]: Meadows, Toby, 2013, “Truth, dependence and supervaluation: Living with the ghost”, *Journal of Philosophical Logic*, 42(2): 221–240. doi:10.1007/s10992-011-9219-x

[^meadows-2014]: –––, 2014, “Fixed points for consequence relations”, *Logique et Analyse*, 57(227): 333–357.

[^moschovakis-1974]: Moschovakis, Yiannis N., 1974, *Elementary Induction on Abstract Structures* (Studies in Logic and the Foundations of Mathematics: Volume 77), Amsterdam: North-Holland.

[^murzi-2018]: Murzi, Julien and Lorenzo Rossi, 2018, “Reflection principles and the Liar in context”, *Philosophers’ Imprint*, 18(15): 1–18.

[^murzi-2020]: –––, 2020, “Generalized revenge”, *Australasian Journal of Philosophy*, 98(1): 153–177. doi:10.1080/00048402.2019.1640323

[^murzi-2026]: Murzi, Julien and Chris Scambler, 2026, “The Liar Paradox and the Revenge Paradoxes”, in Rossi 2026: 133–159.

[^ojea-2012]: Ojea, Ignacio, 2012, “The structural collapse approach reconsidered”, *Análisis Filosófico*, 32(1): 61–68.

[^nicolai-2018]: Nicolai, Carlo and Lorenzo Rossi, 2018, “Principles for object-linguistic consequence: from logical to irreflexive”, *Journal of Philosophical Logic*, 47(3): 549–577. doi:10.1007/s10992-017-9438-x

[^nicolai-2023]: –––, 2023, “Systems for non-reflexive consequence”, *Studia Logica*, 111: 947–977. doi:10.1007/s11225-023-10049-2

[^nicolai-2021]: Nicolai, Carlo and Johannes Stern (eds.), 2021, *Modes of Truth*, London: Routledge.

[^parsons-1974]: Parsons, Charles, 1974, “The Liar Paradox”, *Journal of Philosophical Logic*, 3(4): 381–412; reprinted in, C. Parsons, *Mathematics in Philosophy*, Ithaca: Cornell University Press, 1983, 221–250. doi:10.1007/BF00257482

[^parsons-1984]: Parsons, Terence, 1984, “Assertion, denial, and the Liar Paradox”, *Journal of Philosophical Logic*, 13(2): 137–152. doi:10.1007/BF00453019

[^patterson-2007]: Patterson, Douglas, 2007, “Understanding the Liar”, in Beall 2007: 197–224.

[^patterson-2009]: –––, 2009, “Inconsistency theories of semantic paradox”, *Philosophy and Phenomenological Research*, 79(2): 387–422. doi:10.1111/j.1933-1592.2009.00283.x

[^petersen-2000]: Petersen, Uwe, 2000, “Logic without contraction as based on inclusion and unrestricted abstraction”, *Studia Logica*, 64(3): 365–403. doi:10.1023/A:1005293713265

[^picollo-2012]: Picollo, Lavinia, 2012, “The old-fashioned Yablo paradox”, *Análisis Filosófico*, 32(1): 21–29.

[^picollo-2020a]: –––, 2020a, “Alethic reference”, *Journal of Philosophical Logic*, 49(3): 417–438. doi:10.1007/s10992-019-09524-w

[^picollo-2020b]: –––, 2020b, “Reference and truth”, *Journal of Philosophical Logic*, 49(3): 439–474. doi:10.1007/s10992-019-09525-9

[^picollo-2018]: Picollo, Lavinia and Thomas Schindler, 2018, “Deflationism and the function of truth”, *Philosophical Perspectives*, 32(1): 326–351.

[^picollo-2021]: –––, 2021, “Is deflationism compatible with compositional and Tarskian truth theories?”, in Nicolai and Stern 2021: 41–68.

[^prawitz-1965]: Prawitz, Dag, 1965, *Natural Deduction. A Proof-Theoretical Study*, Stockholm: Almqvist and Wiksell.

[^priest-1984]: Priest, Graham, 1984, “Logic of paradox revisited”, *Journal of Philosophical Logic*, 13(2): 153–179. doi:10.1007/BF00453020

[^priest-1994]: –––, 1994, “The structure of the paradoxes of self-reference”, *Mind*, 103(409): 25–34. doi:10.1093/mind/103.409.25

[^priest-1997]: –––, 1997, “Yablo’s paradox”, *Analysis*, 57(4): 236–242. doi:10.1111/1467-8284.00081

[^priest-2006]: –––, 2006, *In Contradiction*, second edition, Oxford: Oxford University Press.

[^priest-2008]: –––, 2008, *An Introduction to Non-Classical Logic*: *From If to Is*, second edition, Cambridge: Cambridge University Press.

[^priest-2004]: Priest, Graham, Jc Beall, and Bradley Armour-Garb (eds.), 2004, *The Law of Non-Contradiction*, Oxford: Oxford University Press.

[^rahman-2008]: Rahman, Shahid, Tero Tulenheimo, and Emmanuel Genot (eds.), 2008, *Unity, Truth and the Liar: The Modern Relevance of Medieval Solutions to the Liar Paradox*, Berlin: Springer Verlag.

[^rabern-2013]: Rabern, Landon, Brian Rabern, and Matthew Macauley, 2013, “Dangerous reference graphs and semantic paradoxes”, *Journal of Philosophical Logic*, 42(5): 727–765. doi:10.1007/s10992-012-9246-2

[^rayo-2006]: Rayo, Agustín and Gabriel Uzquiano (eds.), 2006, *Absolute Generality*, Oxford: Oxford University Press.

[^read-2002]: Read, Stephen, 2002, “The Liar Paradox from John Buridan back to Thomas Bradwardine”, *Vivarium*, 40(2): 189–218. doi:10.1163/156853402320901812

[^read-2006]: –––, 2006, “Symmetry and paradox”, *History and Philosophy of Logic*, 27(4): 307–318. doi:10.1080/01445340600593942

[^reinhardt-1986]: Reinhardt, William N., 1986, “Some remarks on extending and interpreting theories with a partial predicate for truth”, *Journal of Philosophical Logic*, 15(2): 219–251. doi:10.1007/BF00305492

[^restall-1994]: Restall, Greg, 1994, *On Logics Without Contraction*, Ph.D. Thesis, University of Queensland.

[^restall-2008]: –––, 2008, “Modal models for Bradwardine’s theory of truth”, *Review of Symbolic Logic*, 1(2): 225–240. doi:10.1017/S1755020308080180

[^ripley-2012]: Ripley, Ellie, 2012, “Conservatively extending classical logic with transparent truth”, *Review of Symbolic Logic*, 5(2): 354–378. doi:10.1017/S1755020312000056

[^ripley-2013a]: –––, 2013a, “Paradoxes and failures of cut”, *Australasian Journal of Philosophy*, 91(1): 139–164. doi:10.1080/00048402.2011.630010

[^ripley-2013b]: –––, 2013b, “Revising up: Strengthening classical logic in the face of paradox”, *Philosophers’ Imprint*, 13(5): 1–13. [[Ripley 2013b available online](http://hdl.handle.net/2027/spo.3521354.0013.005)]

[^ripley-2015]: –––, 2015, “Comparing substructural theories of truth”, *Ergo*, 2(13): 299–328. doi:10.3998/ergo.12405314.0002.013

[^rosenblatt-2023]: Rosenblatt, Lucas, 2023, “Paradoxicality without Paradox”, *Erkenntnis*, 88: 1347–1366. doi:10.1007/s10670-021-00405-w

[^rosenblatt-2024]: –––, 2024, “A normal paradox”, *Analysis*, 84(3): 534–546. doi:10.1093/analys/anad087

[^rossi-2019]: Rossi, Lorenzo, 2019, “A unified theory of truth and paradox”, *The Review of Symbolic Logic*, 12(2): 209–254. doi:10.1017/S1755020319000078

[^rossi-2023]: –––, 2023, “Bicontextualism”, *Notre Dame Journal of Formal Logic*, 64(1): 95–127. doi:10.1215/00294527-2023-0004

[^rossi-2026]: ––– (ed.), 2026, *The Liar Paradox*. Cambridge: Cambridge University Press.

[^scharp-2013]: Scharp, Kevin, 2013, *Replacing Truth*, Oxford: Oxford University Press.

[^schindler-2014]: Schindler, Thomas, 2014, “Axioms for grounded truth”, *Review of Symbolic Logic*, 7(1): 73–83. doi:10.1017/S1755020313000282

[^schindler-2020]: –––, 2020, “A note on Horwich’s notion of grounding”, *Synthese*, 197(5): 2029–2038. doi:10.1007/s11229-018-1780-1

[^schroeder-heister-1992]: Schroeder-Heister, Peter, 1992, “Cut-elimination in logics with definitional reflection”, in *Nonclassical Logics and Information Processing*, D. Pearce and H. Wansing (eds.), Berlin: Springer, 146–171.

[^schroeder-heister-2004]: –––, 2004, “On the notion of assumption in logical systems”, in *Selected Papers Contributed to the Sessions of GAP5*, R. Bluhm and C. Nimtz (eds.), Paderborn: Mentis, 27–48.

[^schroeder-heister-2017]: Schroeder-Heister, Peter and Luca Tranchini, 2017, “Ekman’s Paradox”, *Notre Dame Journal of Formal Logic*, 58(4): 567–581. doi:10.1215/00294527-2017-0017

[^schroeder-heister-2021]: –––, 2021, “How to Ekman a Crabbé-Tennant”, *Synthese*, 199: 617–639.

[^shapiro-2006]: Shapiro, Lionel, 2006, “The rationale behind the revision theory”, *Philosophical Studies*, 129(3): 477–515. doi:10.1007/s11098-004-2497-1

[^shapiro-2011a]: –––, 2011a, “Deflating logical consequence”, *Philosophical Quarterly*, 61(243): 320–342. doi:10.1111/j.1467-9213.2010.678.x

[^shapiro-2011b]: –––, 2011b, “Expressibility and the Liar’s revenge”, *Australasian Journal of Philosophy*, 89(2): 297–314. doi:10.1080/00048401003695156

[^shapiro-2015]: –––, 2015, “Naive structure, contraction, and paradox”, *Topoi*, 34(1): 75–87. doi:10.1007/s11245-014-9235-x

[^shapiro-2004]: Shapiro, Stewart, 2004, “Simple truth, contradiction, and consistency”, in Priest, Beall, and Armour-Garb 2004: 336–354.

[^sher-2023]: Sher, Gila, 2023, “A new defense of Tarski’s solution to the Liar Paradox”, *Philosophical Studies*, 180(5–6): 1441–1466.

[^simmons-2009]: Simmons, Keith, 2009, *Universality and the Liar*, Cambridge: Cambridge University Press.

[^smith-2000]: Smith, Nicholas J. J., 2000, “The Principle of Uniform Solution (of the Paradoxes of Self-Reference)”, *Mind*, 109(433): 117–122. doi:10.1093/mind/109.433.117

[^soames-1999]: Soames, Scott, 1999, *Understanding Truth*, Oxford: Oxford University Press.

[^sorensen-1998]: Sorensen, Roy A., 1998, “Yablo’s paradox and kindred infinite Liars”, *Mind*, 107(425): 137–155. doi:10.1093/mind/107.425.137

[^sorensen-2003]: –––, 2003, *A Brief History of Paradox*, Oxford: Oxford University Press.

[^tarski-1935]: Tarski, Alfred, 1935, “Der Wahrheitsbegriff in den formalisierten Sprachen”, *Studia Philosophica*, 1: 261–405; references are to the translation “The concept of truth in formalized languages”, in J. Corcoran (ed.), J.H. Woodger (trans.), *Logic, Semantics, Metamathematics*, 2nd edition, Indianapolis: Hackett, 1983, 152–278.

[^tarski-1944]: –––, 1944, “The semantic conception of truth: and the foundations of semantics”, *Philosophy and Phenomenological Research*, 4(3): 341–375. doi:10.2307/2102968

[^teijeiro-2012]: Teijeiro, Paula, 2012, “Circularity is still scary”, *Análisis Filosófico*, 32(1): 31–35.

[^tennant-1982]: Tennant, Neil, 1982, “Proof and paradox”, *Dialectica*, 36(2–3): 265–296. doi:10.1111/j.1746-8361.1982.tb00820.x

[^tennant-2021]: –––, 2021, “Normalizability, Cut Eliminability and Paradox”, *Synthese*, 199: 597–616.

[^fraassen-1968]: van Fraassen, Bas C., 1968, “Presupposition, implication, and self-reference”, *Journal of Philosophy*, 65(5): 136–152. doi:10.2307/2024557

[^fraassen-1970]: –––, 1970, “Truth and paradoxical consequence”, in Martin 1970: 13–23.

[^visser-1984]: Visser, Albert, 1984, “Four valued semantics and the Liar”, *Journal of Philosophical Logic*, 13(2): 181–212. doi:10.1007/BF00453021

[^walicki-2009]: Walicki, Michał, 2009, “Reference, paradoxes and truth”, *Synthese*, 171(1): 195–226. doi:10.1007/s11229-008-9392-9

[^warren-2024]: Warren, Jared, 2024, “Restricting the T-schema to solve the Liar”, *Philosophy and Phenomenological Research*, 108(1): 238–258. doi:10.1111/phpr.12963

[^weber-2019]: Weber, Zach, 2019, “At the limits of thought”, in Başkent and Ferguson (2019): 555–574.

[^weir-1998]: Weir, Alan, 1998, “Naive set theory, paraconsistency, and indeterminacy: Part I”, *Logique et Analyse*, 41(161–163): 219–266.

[^weir-1999]: –––, 1999, “Naive set theory, paraconsistency, and indeterminacy: Part II”, *Logique et Analyse*, 42(167–168): 283–340.

[^weir-2005]: –––, 2005, “Naive truth and sophisticated logic”, in Beall and Armour-Garb 2005: 218–249.

[^weir-2015]: –––, 2015, “A robust non-transitive logic”, *Topoi*, 34(1): 99–107. doi:10.1007/s11245-013-9176-9

[^woodruff-1984]: Woodruff, Peter W., 1984, “Paradox, truth, and logic part 1: Paradox and truth”, *Journal of Philosophical Logic*, 13(2): 213–232. doi:10.1007/BF00453022

[^yablo-1985]: Yablo, Stephen, 1985, “Truth and reflection”, *Journal of Philosophical Logic*, 14(3): 297–349. doi:10.1007/BF00249368

[^yablo-1993a]: –––, 1993a, “Hop, skip, and jump: The agonistic conception of truth”, *Philosophical Perspectives*, 7: 371–396. doi:10.2307/2214130

[^yablo-1993b]: –––, 1993b, “Paradox without self-reference”, *Analysis*, 53(4): 251–252. doi:10.2307/3328245

[^zardini-2011]: Zardini, Elia, 2011, “Truth without contra(di)ction”, *Review of Symbolic Logic*, 4(4): 498–535. doi:10.1017/S1755020311000177

[^zardini-2013]: –––, 2013, “Naive *modus ponens*”, *Journal of Philosophical Logic*, 42(4): 575–593. doi:10.1007/s10992-012-9239-1
