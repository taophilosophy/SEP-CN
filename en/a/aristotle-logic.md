# Aristotle’s Logic
**First published Sat Mar 18, 2000; substantive revision Tue Nov 22, 2022**

*Smith, Robin*

Aristotle’s logic, especially his theory of the syllogism, has had an unparalleled influence on the history of Western thought. It did not always hold this position: in the Hellenistic period, Stoic logic, and in particular the work of Chrysippus, took pride of place. However, in later antiquity, following the work of Aristotelian Commentators, Aristotle’s logic became dominant, and Aristotelian logic was what was transmitted to the Arabic and the Latin medieval traditions, while the works of Chrysippus have not survived.

This unique historical position has not always contributed to the understanding of Aristotle’s logical works. Kant thought that Aristotle had discovered everything there was to know about logic, and the historian of logic Prantl drew the corollary that any logician after Aristotle who said anything new was confused, stupid, or perverse. During the rise of modern formal logic following Frege and Peirce, adherents of Traditional Logic (seen as the descendant of Aristotelian Logic) and the new mathematical logic tended to see one another as rivals, with incompatible notions of logic. More recent scholarship has often applied the very techniques of mathematical logic to Aristotle’s theories, revealing (in the opinion of many) a number of similarities of approach and interest between Aristotle and modern logicians.

This article is written from the latter perspective. As such, it is about Aristotle’s logic, which is not always the same thing as what has been called “Aristotelian” logic.

## 1. Introduction

Aristotle’s logical works contain the earliest formal study of logic that we have. It is therefore all the more remarkable that together they comprise a highly developed logical theory, one that was able to command immense respect for many centuries: Kant, who was ten times more distant from Aristotle than we are from him, even held that nothing significant had been added to Aristotle’s views in the intervening two millennia.

In the last century, Aristotle’s reputation as a logician has undergone two remarkable reversals. The rise of modern formal logic following the work of Frege and Russell brought with it a recognition of the many serious limitations of Aristotle’s logic; today, very few would try to maintain that it is adequate as a basis for understanding science, mathematics, or even everyday reasoning. At the same time, scholars trained in modern formal techniques have come to view Aristotle with new respect, not so much for the correctness of his results as for the remarkable similarity in spirit between much of his work and modern logic. As Jonathan Lear has put it, “Aristotle shares with modern logicians a fundamental interest in metatheory”: his primary goal is not to offer a practical guide to argumentation but to study the properties of inferential systems themselves.

## 2. Aristotle’s Logical Works: The *Organon*

The ancient commentators grouped together several of Aristotle’s treatises under the title *Organon* (“Instrument”) and regarded them as comprising his logical works:

1. *Categories*
2. *On Interpretation*
3. *Prior Analytics*
4. *Posterior Analytics*
5. *Topics*
6. *On Sophistical Refutations*

In fact, the title *Organon* reflects a much later controversy about whether logic is a part of philosophy (as the Stoics maintained) or merely a tool used by philosophy (as the later Peripatetics thought); calling the logical works “The Instrument” is a way of taking sides on this point. Aristotle himself never uses this term, nor does he give much indication that these particular treatises form some kind of group, though there are frequent cross-references between the *Topics* and the *Analytics*. On the other hand, Aristotle treats the *Prior* and *Posterior Analytics* as one work, and *On Sophistical Refutations* is a final section, or an appendix, to the *Topics*). To these works should be added the *Rhetoric*, which explicitly declares its reliance on the *Topics*.

## 3. The Subject of Logic: “Syllogisms”

All Aristotle’s logic revolves around one notion: the **deduction** (*sullogismos*). A thorough explanation of what a deduction is, and what they are composed of, will necessarily lead us through the whole of his theory. What, then, is a deduction? Aristotle says:

> A deduction is speech (*logos*) in which, certain things having been supposed, something different from those supposed results of necessity because of their being so. (*Prior Analytics* I.2, 24b18–20)

Each of the “things supposed” is a **premise** (*protasis*) of the argument, and what “results of necessity” is the **conclusion** (*sumperasma*).

The core of this definition is the notion of “resulting of necessity” (*ex anankês sumbainein*). This corresponds to a modern notion of logical consequence: $X$ results of necessity from $Y$ and $Z$ if it would be impossible for $X$ to be false when $Y$ and $Z$ are true. We could therefore take this to be a general definition of “valid argument”.

### 3.1 Induction and Deduction

Deductions are one of two species of argument recognized by Aristotle. The other species is **induction** (*epagôgê*). He has far less to say about this than deduction, doing little more than characterize it as “argument from the particular to the universal”. However, induction (or something very much like it) plays a crucial role in the theory of scientific knowledge in the *Posterior Analytics*: it is induction, or at any rate a cognitive process that moves from particulars to their generalizations, that is the basis of knowledge of the indemonstrable first principles of sciences.

### 3.2 Aristotelian Deductions and Modern Valid Arguments

Despite its wide generality, Aristotle’s definition of deduction is not a precise match for a modern definition of validity. Some of the differences may have important consequences:

1. Aristotle explicitly says that what results of necessity must be different from what is supposed. This would rule out arguments in which the conclusion is identical to one of the premises. Modern notions of validity regard such arguments as valid, though trivially so.
2. The plural “certain things having been supposed” was taken by some ancient commentators to rule out by definition arguments with only one premise, and Aristotle himself says in some places that nothing new follows from just one premise.
3. The force of the qualification “because of their being so” has sometimes been seen as ruling out arguments in which the conclusion is not ‘relevant’ to the premises, e.g., arguments in which the premises are inconsistent, arguments with conclusions that would follow from any premises whatsoever, or arguments with superfluous premises.

Of these three possible restrictions, the most interesting would be the third. This could be (and has been) interpreted as committing Aristotle to something like a relevance logic. In fact, there are passages that appear to confirm this. However, this is too complex a matter to discuss here.

However the definition is interpreted, it is clear that Aristotle does not mean to restrict it only to a subset of the valid arguments. This is why I have translated *sullogismos* with ‘deduction’ rather than its English cognate. In modern usage, ‘syllogism’ means an argument of a very specific form. Moreover, modern usage distinguishes between valid syllogisms (the conclusions of which follow from their premises) and invalid syllogisms (the conclusions of which do not follow from their premises). The second of these is inconsistent with Aristotle’s use: since he defines a *sullogismos* as an argument in which the conclusion results of necessity from the premises, “invalid *sullogismos*” is a contradiction in terms. The first is also at least highly misleading, since Aristotle does not appear to think that the *sullogismoi* are simply an interesting subset of the valid arguments. Moreover (see below), Aristotle expends great efforts to argue that every valid argument, in a broad sense, can be “reduced” to an argument, or series of arguments, in something like one of the forms traditionally called a syllogism. If we translate *sullogismos* as “syllogism”, this becomes the trivial claim “Every syllogism is a syllogism”,

## 4. Premises: The Structures of Assertions

Syllogisms are structures of sentences each of which can meaningfully be called true or false: **assertions** (*apophanseis*), in Aristotle’s terminology. According to Aristotle, every such sentence must have the same structure: it must contain a **subject** (*hupokeimenon*) and a **predicate** and must either affirm or deny the predicate of the subject. Thus, every assertion is either the **affirmation** *kataphasis* or the **denial** (*apophasis*) of a single predicate of a single subject.

In *On Interpretation*, Aristotle argues that a single assertion must always either affirm or deny a single predicate of a single subject. Thus, he does not recognize sentential compounds, such as conjunctions and disjunctions, as single assertions. This appears to be a deliberate choice on his part: he argues, for instance, that a conjunction is simply a collection of assertions, with no more intrinsic unity than the sequence of sentences in a lengthy account (e.g. the entire *Iliad*, to take Aristotle’s own example). Since he also treats denials as one of the two basic species of assertion, he does not view negations as sentential compounds. His treatment of conditional sentences and disjunctions is more difficult to appraise, but it is at any rate clear that Aristotle made no efforts to develop a sentential logic. Some of the consequences of this for his theory of demonstration are important.

### 4.1 Terms

Subjects and predicates of assertions are **terms**. A term (*horos*) can be either individual, e.g. *Socrates*, *Plato* or universal, e.g. *human*, *horse*, *animal*, *white*. Subjects may be either individual or universal, but predicates can only be universals: *Socrates is human*, *Plato is not a horse*, *horses are animals*, *humans are not horses*.

The word **universal** (*katholou*) appears to be an Aristotelian coinage. Literally, it means “of a whole”; its opposite is therefore “of a particular” (*kath’ hekaston*). Universal terms are those which can properly serve as predicates, while particular terms are those which cannot.

This distinction is not simply a matter of grammatical function. We can readily enough construct a sentence with “Socrates” as its grammatical predicate: “The person sitting down is Socrates”. Aristotle, however, does not consider this a genuine predication. He calls it instead a merely **accidental** or **incidental** (*kata sumbebêkos*) predication. Such sentences are, for him, dependent for their truth values on other genuine predications (in this case, “Socrates is sitting down”).

Consequently, predication for Aristotle is as much a matter of metaphysics as a matter of grammar. The reason that the term *Socrates* is an individual term and not a universal is that the entity which it designates is an individual, not a universal. What makes *white* and *human* universal terms is that they designate universals.

Further discussion of these issues can be found in the entry on Aristotle’s metaphysics.

### 4.2 Affirmations, Denials, and Contradictions

Aristotle takes some pains in *On Interpretation* to argue that to every affirmation there corresponds exactly one denial such that that denial denies exactly what that affirmation affirms. The pair consisting of an affirmation and its corresponding denial is a **contradiction** (*antiphasis*). In general, Aristotle holds, exactly one member of any contradiction is true and one false: they cannot both be true, and they cannot both be false. However, he appears to make an exception for propositions about future events, though interpreters have debated extensively what this exception might be (see section 12 below). The principle that contradictories cannot both be true has fundamental importance in Aristotle’s metaphysics (see section 9 below).

### 4.3 All, Some, and None

One major difference between Aristotle’s understanding of predication and modern (i.e., post-Fregean) logic is that Aristotle treats individual predications and general predications as similar in logical form: he gives the same analysis to “Socrates is an animal” and “Humans are animals”. However, he notes that when the subject is a universal, predication takes on two forms: it can be either **universal** or **particular**. These expressions are parallel to those with which Aristotle distinguishes universal and particular terms, and Aristotle is aware of that, explicitly distinguishing between a term being a universal and a term being universally predicated of another.

|   | **Affirmations** | **Denials** |   |   |
| --- | --- | --- | --- | --- |
| **Universal** | $P$ affirmed of all of $S$ | Every $S$ is $P$, All $S$ is (are) $P$ | $P$ denied of all of $S$ | No $S$ is $P$ |
| **Particular** | $P$ affirmed of some of $S$ | Some $S$ is (are) $P$ | $P$ denied of some of $S$ | Some $S$ is not $P$, Not every $S$ is $P$ |
| **Indefinite** | $P$ affirmed of $S$ | $S$ is $P$ | $P$ denied of $S$ | $S$ is not $P$ |

Whatever is affirmed or denied of a universal subject may be affirmed or denied of it it **universally** (*katholou* or “of all”, *kata pantos*), **in part** (*kata meros*, *en merei*), or **indefinitely** (*adihoristos*).

#### 4.3.1 The “Square of Opposition”

In *On Interpretation*, Aristotle spells out the relationships of contradiction for sentences with universal subjects as follows:

|   | **Affirmation** | **Denial** |
| --- | --- | --- |
| **Universal** | Every $A$ is $B$ | No $A$ is $B$ |
| **Particular** | Some $A$ is $B$ | Not every $A$ is $B$ |

Simple as it appears, this table raises important difficulties of interpretation (for a thorough discussion, see the entry on the square of opposition).

In the *Prior Analytics*, Aristotle adopts a somewhat artificial way of expressing predications: instead of saying “$X$ is predicated of $Y$” he says “$X$ belongs (*huparchei*) to $Y$”. This should really be regarded as a technical expression. The verb *huparchein* usually means either “begin” or “exist, be present”, and Aristotle’s usage appears to be a development of this latter use.

#### 4.3.2 Some Convenient Abbreviations

For clarity and brevity, I will use the following semi-traditional abbreviations for Aristotelian categorical sentences (note that the predicate term comes *first* and the subject term *second*):

| **Abbreviation** | **Sentence** |
| --- | --- |
| $Aab$ | $a$ belongs to all $b$ (Every $b$ is $a$) |
| $Eab$ | $a$ belongs to no $b$ (No $b$ is $a$) |
| $Iab$ | $a$ belongs to some $b$ (Some $b$ is $a$) |
| $Oab$ | $a$ does not belong to all $b$ (Some $b$ is not $a$) |

## 5. The Syllogistic

Aristotle’s most famous achievement as logician is his theory of inference, traditionally called the **syllogistic** (though not by Aristotle). That theory is in fact the theory of inferences of a very specific sort: inferences with two premises, each of which is a categorical sentence, having exactly one term in common, and having as conclusion a categorical sentence the terms of which are just those two terms not shared by the premises. Aristotle calls the term shared by the premises the **middle term** (*meson*) and each of the other two terms in the premises an **extreme** (*akron*). The middle term must be either subject or predicate of each premise, and this can occur in three ways: the middle term can be the subject of one premise and the predicate of the other, the predicate of both premises, or the subject of both premises. Aristotle refers to these term arrangements as **figures** (*schêmata*):

### 5.1 The Figures

|   | **First Figure** | **Second Figure** | **Third Figure** |   |   |   |
| --- | --- | --- | --- | --- | --- | --- |
|   | **Predicate** | **Subject** | **Predicate** | **Subject** | **Predicate** | **Subject** |
| **Premise** | $a$ | $b$ | $a$ | $b$ | $a$ | $c$ |
| **Premise** | $b$ | $c$ | $a$ | $c$ | $b$ | $c$ |
| **Conclusion** | $a$ | $c$ | $b$ | $c$ | $a$ | $b$ |

Aristotle calls the term which is the predicate of the conclusion the **major** term and the term which is the subject of the conclusion the **minor** term. The premise containing the major term is the **major premise**, and the premise containing the minor term is the **minor premise**.

Aristotle then systematically investigates all possible combinations of two premises in each of the three figures. For each combination, he either demonstrates that some conclusion necessarily follows or demonstrates that no conclusion follows. The results he states are correct.

### 5.2 Methods of Proof: “Perfect” Deductions, Conversion, Reduction

Aristotle’s proofs can be divided into two categories, based on a distinction he makes between “perfect” or “complete” (*teleios*) deductions and “imperfect” or “incomplete” (*atelês*) deductions. A deduction is perfect if it “needs no external term in order to show the necessary result” (24b23–24), and it is imperfect if it “needs one or several in addition that are necessary because of the terms supposed but were not assumed through premises” (24b24–25). The precise interpretation of this distinction is debatable, but it is at any rate clear that Aristotle regards the perfect deductions as not in need of proof in some sense. For imperfect deductions, Aristotle does give proofs, which invariably depend on the perfect deductions. Thus, with some reservations, we might compare the perfect deductions to the axioms or primitive rules of a deductive system.

In the proofs for imperfect deductions, Aristotle says that he “reduces” (*anagein*) each case to one of the perfect forms and that they are thereby “completed” or “perfected”. These completions are either **probative** (*deiktikos*: a modern translation might be “direct”) or **through the impossible** (*dia to adunaton*).

A direct deduction is a series of steps leading from the premises to the conclusion, each of which is either a **conversion** of a previous step or an inference from two previous steps relying on a first-figure deduction. Conversion, in turn, is inferring from a proposition another which has the subject and predicate interchanged. Specifically, Aristotle argues that three such conversions are sound:

$$\begin{align} Eab &\rightarrow Eba \\ Iab &\rightarrow Iba \\ Aab &\rightarrow Iba \end{align}$$

He undertakes to justify these in *An. Pr.* I.2. From a modern standpoint, the third is sometimes regarded with suspicion. Using it we can get *Some monsters are chimeras* from the apparently true *All chimeras are monsters*; but the former is often construed as implying in turn *There is something which is a monster and a chimera*, and thus that there are monsters and there are chimeras. In fact, this simply points up something about Aristotle’s system: Aristotle in effect supposes that *all* terms in syllogisms are non-empty. (For further discussion of this point, see the entry on the square of opposition).

As an example of the procedure, we may take Aristotle’s proof of *Camestres*. He says:

> If $M$ belongs to every $N$ but to no $X$, then neither will $N$ belong to any $X$. For if $M$ belongs to no $X$, then neither does $X$ belong to any $M$; but $M$ belonged to every $N$; therefore, $X$ will belong to no $N$ (for the first figure has come about). And since the privative converts, neither will $N$ belong to any $X$. (*An. Pr.* I.5, 27a9–12)

From this text, we can extract an exact formal proof, as follows:

| Step | Justification | Aristotle’s Text |
| --- | --- | --- |
| 1. $MaN$ |   | *If $M$ belongs to every $N$* |
| 2. $MeX$ |   | *but to no $X$,* |
| To prove: $NeX$ |   | *then neither will $N$ belong to any $X$.* |
| 3. $MeX$ | (2, premise) | *For if $M$ belongs to no $X$,* |
| 4. $XeM$ | (3, conversion of $e$) | *then neither does $X$ belong to any $M$;* |
| 5. $MaN$ | (1, premise) | *but $M$ belonged to every $N$;* |
| 6. $XeN$ | (4, 5, *Celarent*) | *therefore, $X$ will belong to no $N$ (for the first figure has come about).* |
| 7. $NeX$ | (6, conversion of $e$) | *And since the privative converts, neither will $N$ belong to any $X$.* |

A completion or proof “through the impossible” shows that a certain conclusion follows from a pair of premises by assuming as a third premise the denial of that conclusion and giving a deduction, from it and one of the original premises, the denial (or the contrary) of the other premises. This is the deduction of an “impossible”, and Aristotle’s proof ends at that point. An example is his proof of *Baroco* in 27a36–b1:

| Step | Justification | Aristotle’s Text |
| --- | --- | --- |
| 1. $MaN$ |   | *Next, if $M$ belongs to every $N$,* |
| 2. $MoX$ |   | *but does not belong to some $X$,* |
| To prove: $NoX$ |   | *then it is necessary for $N$ not to belong to some $X$* |
| 3. $NaX$ | Contradictory of the desired conclusion | *For if it belongs to all,* |
| 4. $MaN$ | Repetition of premise 1 | *and $M$ is predicated of every $N$,* |
| 5. $MaX$ | (3, 4, Barbara) | *then it is necessary that $M$ belongs to every $X$.* |
| 6. $MoX$ | (5 is the contradictory of 2) | *But it was assumed not to belong to some.* |

### 5.3 Disproof: Counterexamples and Terms

Aristotle proves invalidity by constructing counterexamples. This is very much in the spirit of modern logical theory: all that it takes to show that a certain *form* is invalid is a single *instance* of that form with true premises and a false conclusion. However, Aristotle states his results not by saying that certain premise-conclusion combinations are invalid but by saying that certain premise pairs do not “syllogize”: that is, that, given the pair in question, examples can be constructed in which premises of that form are true and a conclusion of any of the four possible forms is false.

When possible, he does this by a clever and economical method: he gives two triplets of terms, one of which makes the premises true and a universal affirmative “conclusion” true, and the other of which makes the premises true and a universal negative “conclusion” true. The first is a counterexample for an argument with either an $E$ or an $O$ conclusion, and the second is a counterexample for an argument with either an $A$ or an $I$ conclusion.

### 5.4 The Deductions in the Figures (“Moods”)

In *Prior Analytics* I.4–6, Aristotle shows that the premise combinations given in the following table yield deductions and that all other premise combinations fail to yield a deduction. In the terminology traditional since the middle ages, each of these combinations is known as a **mood** Latin *modus*, “way”, which in turn is a translation of Greek *tropos*). Aristotle, however, does not use this expression and instead refers to “the arguments in the figures”.

In this table, “$\vdash$” separates premises from conclusion; it may be read “therefore”. The second column lists the medieval mnemonic name associated with the inference (these are still widely used, and each is actually a mnemonic for Aristotle’s proof of the mood in question). The third column briefly summarizes Aristotle’s procedure for demonstrating the deduction.

| Form | Mnemonic | Proof |
| --- | --- | --- |
| FIRST FIGURE |   |   |
| $Aab, Abc \vdash Aac$ | *Barbara* | Perfect |
| $Eab, Abc \vdash Eac$ | *Celarent* | Perfect |
| $Aab, Ibc \vdash Iac$ | *Darii* | Perfect; also by impossibility, from *Camestres* |
| $Eab, Ibc \vdash Oac$ | *Ferio* | Perfect; also by impossibility, from *Cesare* |
| SECOND FIGURE |   |   |
| $Eab, Aac \vdash Ebc$ | *Cesare* | $(Eab, Aac)\rightarrow (Eba, Aac)$ $\vdash_{Cel} Ebc$ |
| $Aab, Eac \vdash Ebc$ | *Camestres* | $(Aab, Eac) \rightarrow (Aab, Eca)= (Eca, Aab)$ $\vdash_{Cel} Ecb \rightarrow Ebc$ |
| $Eab, Iac \vdash Obc$ | *Festino* | $(Eab, Iac) \rightarrow (Eba,Iac)$ $\vdash_{Fer} Obc$ |
| $Aab, Oac \vdash Obc$ | *Baroco* | $(Aab, Oac +Abc) \vdash_{Bar} (Aac,Oac)$ $\vdash_{Imp} Obc$ |
| THIRD FIGURE |   |   |
| $Aac, Abc \vdash Iab$ | *Darapti* | $(Aac, Abc) \rightarrow (Aac,Icb)$ $\vdash_{Dar} Iab$ |
| $Eac, Abc \vdash Oab$ | *Felapton* | $(Eac, Abc) \rightarrow (Eac,Icb)$ $\vdash_{Fer} Oab$ |
| $Iac, Abc \vdash Iab$ | *Disamis* | $(Iac, Abc) \rightarrow (Ica, Abc)=(Abc,Ica)$ $\vdash_{Dar} Iba \rightarrow Iab$ |
| $Aac, Ibc \vdash Iab$ | *Datisi* | $(Aac, Ibc) \rightarrow (Aac,Icb)$ $\vdash_{Dar} Iab$ |
| $Oac, Abc \vdash Oab$ | *Bocardo* | $(Oac, +Aab, Abc) \vdash_{Bar} (Aac,Oac)$ $\vdash_{Imp} Oab$ |
| $Eac, Ibc \vdash Oab$ | *Ferison* | $(Eac, Ibc) \rightarrow (Eac, Icb)$ $\vdash_{Fer} Oab$ |

Table of the Deductions in the Figures

### 5.5 Metatheoretical Results

Having established which deductions in the figures are possible, Aristotle draws a number of metatheoretical conclusions, including:

1. No deduction has two negative premises
2. No deduction has two particular premises
3. A deduction with an affirmative conclusion must have two affirmative premises
4. A deduction with a negative conclusion must have one negative premise.
5. A deduction with a universal conclusion must have two universal premises

He also proves the following metatheorem:

> All deductions can be reduced to the two universal deductions in the first figure.

His proof of this is elegant. First, he shows that the two particular deductions of the first figure can be reduced, by proof through impossibility, to the universal deductions in the second figure:

(*Darii*)

$(Aab, Ibc, +Eac)\vdash_{Camestres} (Ebc, Ibc)\vdash_{Imp} Iac$

(*Ferio*)

$(Eab, Ibc, +Aac)\vdash_{Cesare} (Ebc, Ibc)\vdash_{Imp} Oac$

He then observes that since he has already shown how to reduce all the particular deductions in the other figures except *Baroco* and *Bocardo* to *Darii* and *Ferio*, these deductions can thus be reduced to *Barbara* and *Celarent*. This proof is strikingly similar both in structure and in subject to modern proofs of the redundancy of axioms in a system.

Many more metatheoretical results, some of them quite sophisticated, are proved in *Prior Analytics* I.45 and in *Prior Analytics* II. As noted below, some of Aristotle’s metatheoretical results are appealed to in the epistemological arguments of the *Posterior Analytics*.

### 5.6 Syllogisms with Modalities

Aristotle follows his treatment of “arguments in the figures” with a much longer, and much more problematic, discussion of what happens to these figured arguments when we add the qualifications “necessarily” and “possibly” to their premises in various ways. In contrast to the syllogistic itself (or, as commentators like to call it, the *assertoric* syllogistic), this *modal* syllogistic appears to be much less satisfactory and is certainly far more difficult to interpret. Here, I only outline Aristotle’s treatment of this subject and note some of the principal points of interpretive controversy.

#### 5.6.1 The Definitions of the Modalities

Modern modal logic treats necessity and possibility as interdefinable: “necessarily P” is equivalent to “not possibly not P”, and “possibly P” to “not necessarily not P”. Aristotle gives these same equivalences in *On Interpretation*. However, in *Prior Analytics*, he makes a distinction between two notions of possibility. On the first, which he takes as his preferred notion, “possibly P” is equivalent to “not necessarily P and not necessarily not P”. He then acknowledges an alternative definition of possibility according to the modern equivalence, but this plays only a secondary role in his system.

#### 5.6.2 Aristotle’s General Approach

Aristotle builds his treatment of modal syllogisms on his account of non-modal (**assertoric**) syllogisms: he works his way through the syllogisms he has already proved and considers the consequences of adding a modal qualification to one or both premises. Most often, then, the questions he explores have the form: “Here is an assertoric syllogism; if I add these modal qualifications to the premises, then what modally qualified form of the conclusion (if any) follows?”. A premise can have one of three modalities: it can be necessary, possible, or assertoric. Aristotle works through the combinations of these in order:

- Two necessary premises
- One necessary and one assertoric premise
- Two possible premises
- One assertoric and one possible premise
- One necessary and one possible premise

Though he generally considers only premise combinations which syllogize in their assertoric forms, he does sometimes extend this; similarly, he sometimes considers conclusions in addition to those which would follow from purely assertoric premises.

Since this is his procedure, it is convenient to describe modal syllogisms in terms of the corresponding non-modal syllogism plus a triplet of letters indicating the modalities of premises and conclusion: $N$ = “necessary”, $P$ = “possible”, $A$ = “assertoric”. Thus, “Barbara $NAN$” would mean “The form *Barbara* with necessary major premise, assertoric minor premise, and necessary conclusion”. I use the letters “$N$” and “$P$” as prefixes for premises as well; a premise with no prefix is assertoric. Thus, *Barbara* $NAN$ would be $NAab, Abc \vdash NAac$.

#### 5.6.3 Modal Conversions

As in the case of assertoric syllogisms, Aristotle makes use of conversion rules to prove validity. The conversion rules for necessary premises are exactly analogous to those for assertoric premises:

$$\begin{align} NEab &\rightarrow NEba \\ NIab &\rightarrow NIba \\ NAab &\rightarrow NIba \end{align}$$

Possible premises behave differently, however. Since he defines “possible” as “neither necessary nor impossible”, it turns out that $x$ *is possibly* $F$ entails, and is entailed by, $x$ *is possibly not* $F$. Aristotle generalizes this to the case of categorical sentences as follows:

$$\begin{align} PAab &\rightarrow PEab \\ PEab &\rightarrow PAab \\ PIab &\rightarrow POab \\ POab &\rightarrow PIab \end{align}$$

In addition, Aristotle uses the intermodal principle $N\rightarrow A$: that is, a necessary premise entails the corresponding assertoric one. However, because of his definition of possibility, the principle $A\rightarrow P$ does not generally hold: if it did, then $N\rightarrow P$ would hold, but on his definition “necessarily $P$” and “possibly $P$” are actually inconsistent (“possibly $P$” entails “possibly not $P$”).

This leads to a further complication. The denial of “possibly $P$” for Aristotle is “either necessarily $P$ or necessarily not $P$”. The denial of “necessarily $P$” is still more difficult to express in terms of a combination of modalities: “either possibly $P$ (and thus possibly not $P$) or necessarily not $P$” This is important because of Aristotle’s proof procedures, which include proof through impossibility. If we give a proof through impossibility in which we assume a necessary premise, then the conclusion we ultimately establish is simply the denial of that necessary premise, not a “possible” conclusion in Aristotle’s sense. Such propositions do occur in his system, but only in exactly this way, i.e., as conclusions established by proof through impossiblity from necessary assumptions. Somewhat confusingly, Aristotle calls such propositions “possible” but immediately adds “ not in the sense defined”: in this sense, “possibly $Oab$” is simply the denial of “necessarily $Aab$”. Such propositions appear only as premises, never as conclusions.

#### 5.6.4 Syllogisms with Necessary Premises

Aristotle holds that an assertoric syllogism remains valid if “necessarily” is added to its premises and its conclusion: the modal pattern $NNN$ is always valid. He does not treat this as a trivial consequence but instead offers proofs; in all but two cases, these are parallel to those offered for the assertoric case. The exceptions are *Baroco* and *Bocardo*, which he proved in the assertoric case through impossibility: attempting to use that method here would require him to take the denial of a necessary $O$ proposition as hypothesis, raising the complication noted above, and he uses the procedure he calls *ecthesis* instead (see Smith 1982)[^smith-1982].

#### 5.6.5 The Problem of the “Two Barbaras” and Other Problems of Interpretation

Since a necessary premise entails an assertoric premise, every $AN$ or $NA$ combination of premises will entail the corresponding $AA$ pair, and thus the corresponding $A$ conclusion. Thus, $ANA$ and $NAA$ syllogisms are always valid. However, Aristotle holds that some, but not all, $ANN$ and $NAN$ combinations are valid. Specifically, he accepts *Barbara* $NAN$ but rejects *Barbara* $ANN$. Almost from Aristotle’s own time, interpreters have found his reasons for this distinction obscure, or unpersuasive, or both, and often have not followed his view. His close associated Theophrastus, for instance, adopted the simpler rule that the modality of the conclusion of a syllogism was always the “weakest” modality found in either premise, where $N$ is stronger than $A$ and $A$ is stronger than $P$ (and where $P$ probably has to be defined as “not necessarily not”).

Beginning with Albrecht Becker, interpreters using the methods of modern formal logic to interpret Aristotle’s modal logic have seen the Two-Barbaras problem as only one of a series of difficulties in giving a coherent interpretation of the modal syllogistic. A very wide range of reconstructions has been proposed: see Becker 1933, McCall 1963, Nortmann 1996, Van Rijen 1989, Patterson 1995, Thomason 1993, Thom 1996, Rini 2012, Malink 2013. The majority of reconstructions do not attempt to reproduce every detail of Aristotle’s exposition but instead produce modified reconstructions that abandon some of those results. Malink 2013, however, offers a reconstruction that reproduces everything Aristotle says, although the resulting model introduces a high degree of complexity. (This subject quickly becomes too complex for summarizing in this brief article.

## 6. Demonstrations and Demonstrative Sciences

A **demonstration** (*apodeixis*) is “a deduction that produces knowledge”. Aristotle’s *Posterior Analytics* contains his account of demonstrations and their role in knowledge. From a modern perspective, we might think that this subject moves outside of logic to epistemology. From Aristotle’s perspective, however, the connection of the theory of *sullogismoi* with the theory of knowledge is especially close.

### 6.1 Aristotelian Sciences

The subject of the *Posterior Analytics* is *epistêmê*. This is one of several Greek words that can reasonably be translated “knowledge”, but Aristotle is concerned only with knowledge of a certain type (as will be explained below). There is a long tradition of translating *epistêmê* in this technical sense as **science**, and I shall follow that tradition here. However, readers should not be misled by the use of that word. In particular, Aristotle’s theory of science cannot be considered a counterpart to modern philosophy of science, at least not without substantial qualifications.

We have scientific knowledge, according to Aristotle, when we know:

> the cause why the thing is, that it is the cause of this, and that this cannot be otherwise. (*Posterior Analytics* I.2)

This implies two strong conditions on what can be the object of scientific knowledge:

1. Only what is necessarily the case can be known scientifically
2. Scientific knowledge is knowledge of causes

He then proceeds to consider what science so defined will consist in, beginning with the observation that at any rate one form of science consists in the possession of a **demonstration** (*apodeixis*), which he defines as a “scientific deduction”:

> by “scientific” (*epistêmonikon*), I mean that in virtue of possessing it, we have knowledge.

The remainder of *Posterior Analytics* I is largely concerned with two tasks: spelling out the nature of demonstration and demonstrative science and answering an important challenge to its very possibility. Aristotle first tells us that a demonstration is a deduction in which the premises are:

1. true
2. **primary** (*prota*)
3. **immediate** (*amesa*, “without a middle”)
4. **better known** or **more familiar** (*gnôrimôtera*) than the conclusion
5. **prior** to the conclusion
6. **causes** (*aitia*) of the conclusion

The interpretation of all these conditions except the first has been the subject of much controversy. Aristotle clearly thinks that science is knowledge of causes and that in a demonstration, knowledge of the premises is what brings about knowledge of the conclusion. The fourth condition shows that the knower of a demonstration must be in some better epistemic condition towards them, and so modern interpreters often suppose that Aristotle has defined a kind of epistemic justification here. However, as noted above, Aristotle is defining a special variety of knowledge. Comparisons with discussions of justification in modern epistemology may therefore be misleading.

The same can be said of the terms “primary”, “immediate” and “better known”. Modern interpreters sometimes take “immediate” to mean “self-evident”; Aristotle does say that an immediate proposition is one “to which no other is prior”, but (as I suggest in the next section) the notion of priority involved is likely a notion of logical priority that it is hard to detach from Aristotle’s own logical theories. “Better known” has sometimes been interpreted simply as “previously known to the knower of the demonstration” (i.e., already known in advance of the demonstration). However, Aristotle explicitly distinguishes between what is “better known for us” with what is “better known in itself” or “in nature” and says that he means the latter in his definition. In fact, he says that the process of acquiring scientific knowledge is a process of *changing* what is better known “for us”, until we arrive at that condition in which what is better known in itself is also better known for us.

### 6.2 The Regress Problem

In *Posterior Analytics* I.2, Aristotle considers two challenges to the possibility of science. One party (dubbed the “agnostics” by Jonathan Barnes) began with the following two premises:

1. Whatever is scientifically known must be demonstrated.
2. The premises of a demonstration must be scientifically known.

They then argued that demonstration is impossible with the following dilemma:

1. If the premises of a demonstration are scientifically known, then they must be demonstrated.
2. The premises from which each premise are demonstrated must be scientifically known.
3. Either this process continues forever, creating an infinite regress of premises, or it comes to a stop at some point.
4. If it continues forever, then there are no first premises from which the subsequent ones are demonstrated, and so nothing is demonstrated.
5. On the other hand, if it comes to a stop at some point, then the premises at which it comes to a stop are undemonstrated and therefore not scientifically known; consequently, neither are any of the others deduced from them.
6. Therefore, nothing can be demonstrated.

A second group accepted the agnostics’ view that scientific knowledge comes only from demonstration but rejected their conclusion by rejecting the dilemma. Instead, they maintained:

- Demonstration “in a circle” is possible, so that it is possible for all premises also to be conclusions and therefore demonstrated.

Aristotle does not give us much information about how circular demonstration was supposed to work, but the most plausible interpretation would be supposing that at least for some set of fundamental principles, each principle could be deduced from the others. (Some modern interpreters have compared this position to a coherence theory of knowledge.) However their position worked, the circular demonstrators claimed to have a third alternative avoiding the agnostics’ dilemma, since circular demonstration gives us a regress that is both unending (in the sense that we never reach premises at which it comes to a stop) and finite (because it works its way round the finite circle of premises).

### 6.3 Aristotle’s Solution: “It Eventually Comes to a Stop”

Aristotle rejects circular demonstration as an incoherent notion on the grounds that the premises of any demonstration must be prior (in an appropriate sense) to the conclusion, whereas a circular demonstration would make the same premises both prior and posterior to one another (and indeed every premise prior and posterior to itself). He agrees with the agnostics’ analysis of the regress problem: the only plausible options are that it continues indefinitely or that it “comes to a stop” at some point. However, he thinks both the agnostics and the circular demonstrators are wrong in maintaining that scientific knowledge is only possible by demonstration from premises scientifically known: instead, he claims, there is another form of knowledge possible for the first premises, and this provides the starting points for demonstrations.

To solve this problem, Aristotle needs to do something quite specific. It will not be enough for him to establish that we can have knowledge of *some propositions* without demonstrating them: unless it is in turn possible to deduce all the other propositions of a science from them, we shall not have solved the regress problem. Moreover (and obviously), it is no solution to this problem for Aristotle simply to *assert* that we have knowledge without demonstration of some appropriate starting points. He does indeed say that it is his position that we have such knowledge (*An. Post.* I.2,), but he owes us an account of why that should be so.

### 6.4 Knowledge of First Principles: *Nous*

Aristotle’s account of knowledge of the indemonstrable first premises of sciences is found in *Posterior Analytics* II.19, long regarded as a difficult text to interpret. Briefly, what he says there is that it is another cognitive state, *nous* (translated variously as “insight”, “intuition”, “intelligence”), which knows them. There is wide disagreement among commentators about the interpretation of his account of how this state is reached; I will offer one possible interpretation. First, Aristotle identifies his problem as explaining how the principles can “become familiar to us”, using the same term “familiar” (*gnôrimos*) that he used in presenting the regress problem. What he is presenting, then, is not a method of discovery but a process of becoming wise. Second, he says that in order for knowledge of immediate premises to be possible, we must have a kind of knowledge of them without having learned it, but this knowledge must not be as “precise” as the knowledge that a possessor of science must have. The kind of knowledge in question turns out to be a capacity or power (*dunamis*) which Aristotle compares to the capacity for sense-perception: since our senses are innate, i.e., develop naturally, it is in a way correct to say that we know what e.g. all the colors look like before we have seen them: we have the capacity to see them by nature, and when we first see a color we exercise this capacity without having to learn how to do so first. Likewise, Aristotle holds, our minds have by nature the capacity to recognize the starting points of the sciences.

In the case of sensation, the capacity for perception in the sense organ is actualized by the operation on it of the perceptible object. Similarly, Aristotle holds that coming to know first premises is a matter of a potentiality in the mind being actualized by experience of its proper objects: “The soul is of such a nature as to be capable of undergoing this”. So, although we cannot come to know the first premises without the necessary experience, just as we cannot see colors without the presence of colored objects, our minds are already so constituted as to be able to recognize the right objects, just as our eyes are already so constituted as to be able to perceive the colors that exist.

It is considerably less clear what these objects are and how it is that experience actualizes the relevant potentialities in the soul. Aristotle describes a series of stages of cognition. First is what is common to all animals: perception of what is present. Next is memory, which he regards as a retention of a sensation: only some animals have this capacity. Even fewer have the next capacity, the capacity to form a single experience (*empeiria*) from many repetitions of the same memory. Finally, many experiences repeated give rise to knowledge of a single universal (*katholou*). This last capacity is present only in humans.

See Section 7 of the entry on Aristotle’s psychology for more on his views about mind.

## 7. Definitions

The **definition** (*horos*, *horismos*) was an important matter for Plato and for the Early Academy. Concern with answering the question “What is so-and-so?” are at the center of the majority of Plato’s dialogues, some of which (most elaborately the *Sophist*) propound methods for finding definitions. External sources (sometimes the satirical remarks of comedians) also reflect this Academic concern with definitions. Aristotle himself traces the quest for definitions back to Socrates.

### 7.1 Definitions and Essences

For Aristotle, a definition is “an account which signifies what it is to be for something” (*logos ho to ti ên einai sêmainei*). The phrase “what it is to be” and its variants are crucial: giving a definition is saying, of some existent thing, what it is, not simply specifying the meaning of a word (Aristotle does recognize definitions of the latter sort, but he has little interest in them).

The notion of “what it is to be” for a thing is so pervasive in Aristotle that it becomes formulaic: what a definition expresses is “the what-it-is-to-be” (*to ti ên einai*), or in modern terminology, its essence.

### 7.2 Species, Genus, and Differentia

Since a definition defines an essence, only what has an essence can be defined. What has an essence, then? That is one of the central questions of Aristotle’s metaphysics; once again, we must leave the details to another article. In general, however, it is not individuals but rather **species** (*eidos*: the word is one of those Plato uses for “Form”) that have essences. A species is defined by giving its **genus** (*genos*) and its **differentia** (*diaphora*): the genus is the kind under which the species falls, and the differentia tells what characterizes the species within that genus. As an example, *human* might be defined as *animal* (the genus) *having the capacity to reason* (the differentia).

#### Essential Predication and the Predicables

Underlying Aristotle’s concept of a definition is the concept of **essential predication** (*katêgoreisthai en tôi ti esti*, predication in the what it is). In any true affirmative predication, the predicate either does or does not “say what the subject is”, i.e., the predicate either is or is not an acceptable answer to the question “What is it?” asked of the subject. Bucephalus is a horse, and a horse is an animal; so, “Bucephalus is a horse” and “Bucephalus is an animal” are essential predications. However, “Bucephalus is brown”, though true, does not state what Bucephalus is but only says something about him.

Since a thing’s definition says what it is, definitions are essentially predicated. However, not everything essentially predicated is a definition. Since Bucephalus is a horse, and horses are a kind of mammal, and mammals are a kind of animal, “horse” “mammal” and “animal” are all essential predicates of Bucephalus. Moreover, since what a horse is is a kind of mammal, “mammal” is an essential predicate of horse. When predicate $X$ is an essential predicate of $Y$ but also of other things, then $X$ is a **genus** (*genos*) of $Y$.

A definition of $X$ must not only be essentially predicated of it but must also be predicated only of it: to use a term from Aristotle’s *Topics*, a definition and what it defines must “counterpredicate” (*antikatêgoreisthai*) with one another. $X$ counterpredicates with $Y$ if $X$ applies to what $Y$ applies to and conversely. Though X’s definition must counterpredicate with $X$, not everything that counterpredicates with $X$ is its definition. “Capable of laughing”, for example, counterpredicates with “human” but fails to be its definition. Such a predicate (non-essential but counterpredicating) is a **peculiar property** or **proprium** (*idion*).

Finally, if $X$ is predicated of $Y$ but is neither essential nor counterpredicates, then $X$ is an **accident** (*sumbebêkos*) of $Y$.

Aristotle sometimes treats genus, peculiar property, definition, and accident as including all possible predications (e.g. *Topics* I). Later commentators listed these four and the differentia as the five **predicables**, and as such they were of great importance to late ancient and to medieval philosophy (e.g., Porphyry).

### 7.3 The Categories

The notion of essential predication is connected to what are traditionally called the **categories** (*katêgoriai*). In a word, Aristotle is famous for having held a “doctrine of categories”. Just what that doctrine was, and indeed just what a category is, are considerably more vexing questions. They also quickly take us outside his logic and into his metaphysics. Here, I will try to give a very general overview, beginning with the somewhat simpler question “What categories are there?”

We can answer this question by listing the categories. Here are two passages containing such lists:

> We should distinguish the kinds of predication (*ta genê tôn katêgoriôn*) in which the four predications mentioned are found. These are ten in number: what-it-is, quantity, quality, relative, where, when, being-in-a-position, having, doing, undergoing. An accident, a genus, a peculiar property and a definition will always be in one of these categories. (*Topics* I.9, 103b20–25)
>
> Of things said without any combination, each signifies either substance or quantity or quality or a relative or where or when or being-in-a-position or having or doing or undergoing. To give a rough idea, examples of substance are man, horse; of quantity: four-foot, five-foot; of quality: white, literate; of a relative: double, half, larger; of where: in the Lyceum, in the market-place; of when: yesterday, last year; of being-in-a-position: is-lying, is-sitting; of having: has-shoes-on, has-armor-on; of doing: cutting, burning; of undergoing: being-cut, being-burned. (*Categories* 4, 1b25–2a4, tr. Ackrill, slightly modified)

These two passages give ten-item lists, identical except for their first members. What are they lists $of$? Here are three ways they might be interpreted:

The word “category” (*katêgoria*) means “predication”. Aristotle holds that predications and predicates can be grouped into several largest “kinds of predication” (*genê tôn katêgoriôn*). He refers to this classification frequently, often calling the “kinds of predication” simply “the predications”, and this (by way of Latin) leads to our word “category”.

- First, the categories may be *kinds of predicate*: predicates (or, more precisely, predicate expressions) can be divided into ten separate classes, with each expression belonging to just one class. This comports well with the root meaning of the word *katêgoria* (“predication”). On this interpretation, the categories arise out of considering the most general types of question that can be asked about something: “*What* is it?”; “*How much* is it?”; “*What sort* is it?”; “*Where* is it?”; “*What* is it *doing*?” Answers appropriate to one of these questions are nonsensical in response to another (“When is it?” “A horse”). Thus, the categories may rule out certain kinds of question as ill-formed or confused. This plays an important role in Aristotle’s metaphysics.
- Second, the categories may be seen as classifications of *predications*, that is, kinds of relation that may hold between the predicate and the subject of a predication. To say of Socrates that he is human is to say what he $is$, whereas to say that he is literate is not to say what he is but rather to give a quality that he *has*. For Aristotle, the relation of predicate to subject in these two sentences is quite different (in this respect he differs both from Plato and from modern logicians). The categories may be interpreted as ten different ways in which a predicate may be related to its subject. This last division has importance for Aristotle’s logic as well as his metaphysics.
- Third, the categories may be seen as *kinds of entity*, as highest genera or kinds of thing that are. A given thing can be classified under a series of progressively wider genera: Socrates is a human, a mammal, an animal, a living being. The categories are the highest such genera. Each falls under no other genus, and each is completely separate from the others. This distinction is of critical importance to Aristotle’s metaphysics.

Which of these interpretations fits best with the two passages above? The answer appears to be different in the two cases. This is most evident if we take note of point in which they differ: the *Categories* lists **substance** (*ousia*) in first place, while the *Topics* list **what-it-is** (*ti esti*). A substance, for Aristotle, is a type of entity, suggesting that the *Categories* list is a list of types of entity.

On the other hand, the expression “what-it-is” suggests most strongly a type of predication. Indeed, the *Topics* confirms this by telling us that we can “say what it is” of an *entity* falling under any of the categories:

> an expression signifying what-it-is will sometimes signify a substance, sometimes a quantity, sometimes a quality, and sometimes one of the other categories.

As Aristotle explains, if I say that Socrates is a man, then I have said what Socrates is and signified a substance; if I say that white is a color, then I have said what white is and signified a quality; if I say that some length is a foot long, then I have said what it is and signified a quantity; and so on for the other categories. What-it-is, then, here designates a kind of predication, not a kind of entity.

This might lead us to conclude that the categories in the *Topics* are only to be interpreted as kinds of predicate or predication, those in the *Categories* as kinds of being. Even so, we would still want to ask what the relationship is between these two nearly-identical lists of terms, given these distinct interpretations. However, the situation is much more complicated. First, there are dozens of other passages in which the categories appear. Nowhere else do we find a list of ten, but we do find shorter lists containing eight, or six, or five, or four of them (with substance/what-it-is, quality, quantity, and relative the most common). Aristotle describes what these lists are lists of in different ways: they tell us “how being is divided”, or “how many ways being is said”, or “the figures of predication” (ta schêmata tês katêgorias). The designation of the first category also varies: we find not only “substance” and “what it is” but also the expressions “this” or “the this” (*tode ti*, *to tode*, *to ti*). These latter expressions are closely associated with, but not synonymous with, substance. He even combines the latter with “what-it-is” (*Metaphysics* Z 1, 1028a10: “… one sense signifies what it is and the this, one signifies quality …”).

Moreover, substances are for Aristotle fundamental for predication as well as metaphysically fundamental. He tells us that everything that exists exists because substances exist: if there were no substances, there would not be anything else. He also conceives of predication as reflecting a metaphysical relationship (or perhaps more than one, depending on the type of predication). The sentence “Socrates is pale” gets its truth from a state of affairs consisting of a substance (Socrates) and a quality (whiteness) which is in that substance. At this point we have gone far outside the realm of Aristotle’s logic into his metaphysics, the fundamental question of which, according to Aristotle, is “What is a substance?”. (For further discussion of this topic, see the entry on Aristotle’s Categories and the entry on Aristotle’s metaphysics, (Section 2).

See Frede 1981, Ebert 1985 for additional discussion of Aristotle’s lists of categories.

For convenience of reference, I include a table of the categories, along with Aristotle’s examples and the traditional names often used for them. For reasons explained above, I have treated the first item in the list quite differently, since an example of a substance and an example of a what-it-is are necessarily (as one might put it) in different categories.

| **Traditional name** | **Literally** | **Greek** | **Examples** |
| --- | --- | --- | --- |
| Substance | substance “this” what-it-is | *ousia* *tode ti* *ti esti* | man, horse Socrates “Socrates is a man” |
| Quantity | How much | *poson* | four-foot, five-foot |
| Quality | What sort | *poion* | white, literate |
| Relation | related to what | *pros ti* | double, half, greater |
| Location | Where | *pou* | in the Lyceum, in the marketplace |
| Time | when | *pote* | yesterday, last year |
| Position | being situated | *keisthai* | lies, sits |
| Habit | having, possession | *echein* | is shod, is armed |
| Action | doing | *poiein* | cuts, burns |
| Passion | undergoing | *paschein* | is cut, is burned |

### 7.4 The Method of Division

In the *Sophist*, Plato introduces a procedure of “Division” as a method for discovering definitions. To find a definition of $X$, first locate the largest kind of thing under which $X$ falls; then, divide that kind into two parts, and decide which of the two $X$ falls into. Repeat this method with the part until $X$ has been fully located.

This method is part of Aristotle’s Platonic legacy. His attitude towards it, however, is complex. He adopts a view of the proper structure of definitions that is closely allied to it: a correct definition of $X$ should give the **genus** (*genos*: kind or family) of $X$, which tells what kind of thing $X$ is, and the **differentia** (*diaphora*: difference) which uniquely identifies $X$ within that genus. Something defined in this way is a **species** (*eidos*: the term is one of Plato’s terms for “Form”), and the differentia is thus the “difference that makes a species” (*eidopoios diaphora*, “specific difference”). In *Posterior Analytics* II.13, he gives his own account of the use of Division in finding definitions.

However, Aristotle is strongly critical of the Platonic view of Division as a method for *establishing* definitions. In *Prior Analytics* I.31, he contrasts Division with the syllogistic method he has just presented, arguing that Division cannot actually prove anything but rather assumes the very thing it is supposed to be proving. He also charges that the partisans of Division failed to understand what their own method was capable of proving.

### 7.5 Definition and Demonstration

Closely related to this is the discussion, in *Posterior Analytics* II.3–10, of the question whether there can be both definition and demonstration of the same thing (that is, whether the same result can be established either by definition or by demonstration). Since the definitions Aristotle is interested in are statements of essences, knowing a definition is knowing, of some existing thing, what it is. Consequently, Aristotle’s question amounts to a question whether defining and demonstrating can be alternative ways of acquiring the same knowledge. His reply is complex:

1. Not everything demonstrable can be known by finding definitions, since all definitions are universal and affirmative whereas some demonstrable propositions are negative.
2. If a thing is demonstrable, then to know it just is to possess its demonstration; therefore, it cannot be known just by definition.
3. Nevertheless, some definitions can be understood as demonstrations differently arranged.

As an example of case 3, Aristotle considers the definition “Thunder is the extinction of fire in the clouds”. He sees this as a compressed and rearranged form of this demonstration:

- Sound accompanies the extinguishing of fire.
- Fire is extinguished in the clouds.
- Therefore, a sound occurs in the clouds.

We can see the connection by considering the answers to two questions: “What is thunder?” “The extinction of fire in the clouds” (definition). “Why does it thunder?” “Because fire is extinguished in the clouds” (demonstration).

As with his criticisms of Division, Aristotle is arguing for the superiority of his own concept of science to the Platonic concept. Knowledge is composed of demonstrations, even if it may also include definitions; the method of science is demonstrative, even if it may also include the process of defining.

## 8. Dialectical Argument and the Art of Dialectic

Aristotle often contrasts *dialectical arguments* with demonstrations. The difference, he tells us, is in the character of their premises, not in their logical structure: whether an argument is a *sullogismos* is only a matter of whether its conclusion results of necessity from its premises. The premises of demonstrations must be *true and primary*, that is, not only true but also prior to their conclusions in the way explained in the *Posterior Analytics*. The premises of dialectical deductions, by contrast, must be **accepted** (*endoxos*).

### 8.1 Dialectical Premises: The Meaning of *Endoxos*

Recent scholars have proposed different interpretations of the term *endoxos*. Aristotle often uses this adjective as a substantive: *ta endoxa*, “accepted things”, “accepted opinions”. On one understanding, descended from the work of G. E. L. Owen and developed more fully by Jonathan Barnes and especially Terence Irwin, the *endoxa* are a compilation of views held by various people with some form or other of standing: “the views of fairly reflective people after some reflection”, in Irwin’s phrase. Dialectic is then simply “a method of argument from [the] common beliefs [held by these people]”. For Irwin, then, *endoxa* are “common beliefs”. Jonathan Barnes, noting that *endoxa* are opinions with a certain standing, translates with “reputable”.

My own view is that Aristotle’s texts support a somewhat different understanding. He also tells us that dialectical premises differ from demonstrative ones in that the former are *questions*, whereas the latter are *assumptions* or *assertions*: “the demonstrator does not ask, but takes”, he says. This fits most naturally with a view of dialectic as argument directed at another person by question and answer and consequently taking as premises that other person’s concessions. Anyone arguing in this manner will, in order to be successful, have to ask for premises which the interlocutor is liable to accept, and the best way to be successful at that is to have an inventory of acceptable premises, i.e., premises that are in fact acceptable to people of different types.

In fact, we can discern in the *Topics* (and the *Rhetoric*, which Aristotle says depends on the art explained in the *Topics*) an art of dialectic for use in such arguments. My reconstruction of this art (which would not be accepted by all scholars) is as follows.

### 8.2 The Two Elements of the Art of Dialectic

Given the above picture of dialectical argument, the dialectical art will consist of two elements. One will be a method for discovering premises from which a given conclusion follows, while the other will be a method for determining which premises a given interlocutor will be likely to concede. The first task is accomplished by developing a system for classifying premises according to their logical structure. We might expect Aristotle to avail himself here of the syllogistic, but in fact he develops quite another approach, one that seems less systematic and rests on various “common” terms. The second task is accomplished by developing lists of the premises which are acceptable to various types of interlocutor. Then, once one knows what sort of person one is dealing with, one can choose premises accordingly. Aristotle stresses that, as in all arts, the dialectician must study, not what is acceptable to this or that specific person, but what is acceptable to this or that type of person, just as the doctor studies what is healthful for different types of person: “art is of the universal”.

#### 8.2.1 The “Logical System” of the *Topics*

The method presented in the *Topics* for classifying arguments relies on the presence in the conclusion of certain “common” terms (*koina*) — common in the sense that they are not peculiar to any subject matter but may play a role in arguments about anything whatever. We find enumerations of arguments involving these terms in a similar order several times. Typically, they include:

1. Opposites (*antikeimena*, *antitheseis*)
2. Contraries (*enantia*)
3. Contradictories (*apophaseis*)
4. Possession and Privation (*hexis kai sterêsis*)
5. Relatives (*pros ti*)
6. Cases (*ptôseis*)
7. “More and Less and Likewise”

The four types of **opposites** are the best represented. Each designates a type of term pair, i.e., a way two terms can be opposed to one another. **Contraries** are polar opposites or opposed extremes such as hot and cold, dry and wet, good and bad. A pair of **contradictories** consists of a term and its negation: good, not good. A **possession** (or condition) and **privation** are illustrated by sight and blindness. **Relatives** are relative terms in the modern sense: a pair consists of a term and its correlative, e.g. large and small, parent and child.

The argumentative patterns Aristotle associated with **cases** generally involve inferring a sentence containing adverbial or declined forms from another sentence containing different forms of the same word stem: “if what is useful is good, then what is done usefully is done well and the useful person is good”. In Hellenistic grammatical usage, *ptôsis* meant “case” (e.g. nominative, dative, accusative); Aristotle’s use here is obviously an early form of that.

Under the heading **more and less and likewise**, Aristotle groups a somewhat motley assortment of argument patterns all involving, in some way or other, the terms “more”, “less”, and “likewise”. Examples: “If whatever is $A$ is $B$, then whatever is more (less) $A$ is more (less) $B$”; “If $A$ is more likely $B$ than $C$ is, and $A$ is not $B$, then neither is $C$”; “If $A$ is more likely than $B$ and $B$ is the case, then $A$ is the case”.

#### 8.2.2 The *Topoi*

At the heart of the *Topics* is a collection of what Aristotle calls *topoi*, “places” or “locations”. Unfortunately, though it is clear that he intends most of the *Topics* (Books II–VI) as a collection of these, he never explicitly defines this term. Interpreters have consequently disagreed considerably about just what a *topos* is. Discussions may be found in Brunschwig 1967, Slomkowski 1996, Primavesi 1997, and Smith 1997.

### 8.3 The Uses of Dialectic and Dialectical Argument

An *art* of dialectic will be useful wherever dialectical argument is useful. Aristotle mentions three such uses; each merits some comment.

#### 8.3.1 Gymnastic Dialectic

First, there appears to have been a form of stylized argumentative exchange practiced in the Academy in Aristotle’s time. The main evidence for this is simply Aristotle’s *Topics*, especially Book VIII, which makes frequent reference to rule-governed procedures, apparently taking it for granted that the audience will understand them. In these exchanges, one participant took the role of answerer, the other the role of questioner. The answerer began by asserting some proposition (a *thesis*: “position” or “acceptance”). The questioner then asked questions of the answerer in an attempt to secure concessions from which a contradiction could be deduced: that is, to **refute** (*elenchein*) the answerer’s position. The questioner was limited to questions that could be answered by yes or no; generally, the answerer could only respond with yes or no, though in some cases answerers could object to the form of a question. Answerers might undertake to answer in accordance with the views of a particular type of person or a particular person (e.g. a famous philosopher), or they might answer according to their own beliefs. There appear to have been judges or scorekeepers for the process. Gymnastic dialectical contests were sometimes, as the name suggests, for the sake of exercise in developing argumentative skill, but they may also have been pursued as a part of a process of inquiry.

#### 8.3.2 Dialectic That Puts to the Test

Aristotle also mentions an “art of making trial”, or a variety of dialectical argument that “puts to the test” (the Greek word is the adjective *peirastikê*, in the feminine: such expressions often designate arts or skills, e.g. *rhêtorikê*, “the art of rhetoric”). Its function is to examine the claims of those who say they have some knowledge, and it can be practiced by someone who does not possess the knowledge in question. The examination is a matter of refutation, based on the principle that whoever knows a subject must have consistent beliefs about it: so, if you can show me that my beliefs about something lead to a contradiction, then you have shown that I do not have knowledge about it.

This is strongly reminiscent of Socrates’ style of interrogation, from which it is almost certainly descended. In fact, Aristotle often indicates that dialectical argument is by nature refutative.

#### 8.3.3 Dialectic and Philosophy

Dialectical refutation cannot of itself establish any proposition (except perhaps the proposition that some set of propositions is inconsistent). More to the point, though deducing a contradiction from my beliefs may show that they do not constitute knowledge, failure to deduce a contradiction from them is no proof that they are true. Not surprisingly, then, Aristotle often insists that “dialectic does not prove anything” and that the dialectical art is not some sort of universal knowledge.

In *Topics* I.2, however, Aristotle says that the art of dialectic is useful in connection with “the philosophical sciences”. One reason he gives for this follows closely on the refutative function: if we have subjected our opinions (and the opinions of our fellows, and of the wise) to a thorough refutative examination, we will be in a much better position to judge what is most likely true and false. In fact, we find just such a procedure at the start of many of Aristotle’s treatises: an enumeration of the opinions current about the subject together with a compilation of “puzzles” raised by these opinions. Aristotle has a special term for this kind of review: a *diaporia*, a “puzzling through”.

He adds a second use that is both more difficult to understand and more intriguing. The *Posterior Analytics* argues that if anything can be proved, then not everything that is known is known as a result of proof. What alternative means is there whereby the first principles of sciences are known? Aristotle’s own answer as found in *Posterior Analytics* II.19 is difficult to interpret, and recent philosophers have often found it unsatisfying since (as often construed) it appears to commit Aristotle to a form of apriorism or rationalism both indefensible in itself and not consonant with his own insistence on the indispensability of empirical inquiry in natural science.

Against this background, the following passage in *Topics* I.2 may have special importance:

> It is also useful in connection with the first things concerning each of the sciences. For it is impossible to say anything about the science under consideration on the basis of its own principles, since the principles are first of all, and we must work our way through about these by means of what is generally accepted about each. But this is peculiar, or most proper, to dialectic: for since it is examinative with respect to the principles of all the sciences, it has a way to proceed.

A number of interpreters (beginning with Owen 1961)[^owen-1961] have built on this passage and others to find dialectic at the heart of Aristotle’s philosophical method. Further discussion of this issue would take us far beyond the subject of this article (the fullest development is in Irwin 1988; see also Nussbaum 1986 and Bolton 1990; for criticism, Hamlyn 1990, Smith 1997)[^bolton-1990][^hamlyn-1990][^irwin-1988][^nussbaum-1986][^smith-1997].

## 9. Dialectic and Rhetoric

Aristotle says that rhetoric, i.e., the study of persuasive speech, is a “counterpart” (*antistrophos*) of dialectic and that the rhetorical art is a kind of “outgrowth” (*paraphues ti*) of dialectic and the study of character types. The correspondence with dialectical method is straightforward: rhetorical speeches, like dialectical arguments, seek to persuade others to accept certain conclusions on the basis of premises they already accept. Therefore, the same measures useful in dialectical contexts will, mutatis mutandis, be useful here: knowing what premises an audience of a given type is likely to believe, and knowing how to find premises from which the desired conclusion follows.

The *Rhetoric* does fit this general description: Aristotle includes both discussions of types of person or audience (with generalizations about what each type tends to believe) and a summary version (in II.23) of the argument patterns discussed in the *Topics*. For further discussion of his rhetoric see Aristotle’s rhetoric.

## 10. Sophistical Arguments

Demonstrations and dialectical arguments are both forms of valid argument, for Aristotle. However, he also studies what he calls **contentious** (*eristikos*) or **sophistical** arguments: these he defines as arguments which only apparently establish their conclusions. In fact, Aristotle defines these as apparent (but not genuine) *dialectical* *sullogismoi*. They may have this appearance in either of two ways:

1. Arguments in which the conclusion only appears to follow of necessity from the premises (apparent, but not genuine, *sullogismoi*).
2. Genuine *sullogismois* the premises of which are merely apparently, but not genuinely, acceptable.

Arguments of the first type in modern terms, appear to be valid but are really invalid. Arguments of the second type are at first more perplexing: given that acceptability is a matter of what people believe, it might seem that whatever appears to be *endoxos* must actually be *endoxos*. However, Aristotle probably has in mind arguments with premises that may at first glance *seem* to be acceptable but which, upon a moment’s reflection, we immediately realize we do not actually accept. Consider this example from Aristotle’s time:

- Whatever you have not lost, you still have.
- You have not lost horns.
- Therefore, you still have horns

This is transparently bad, but the problem is not that it is invalid: the problem is rather that the first premise, though superficially plausible, is false. In fact, anyone with a little ability to follow an argument will realize that at once upon seeing this very argument.

Aristotle’s study of sophistical arguments is contained in *On Sophistical Refutations*, which is actually a sort of appendix to the *Topics*.

To a remarkable extent, contemporary discussions of fallacies reproduce Aristotle’s own classifications. See Dorion 1995 for further discussion.

## 11. Non-Contradiction and Metaphysics

Two frequent themes of Aristotle’s account of science are (1) that the first principles of sciences are not demonstrable and (2) that there is no single universal science including all other sciences as its parts. “All things are not in a single genus”, he says, “and even if they were, all beings could not fall under the same principles” (*On Sophistical Refutations* 11). Thus, it is exactly the universal applicability of dialectic that leads him to deny it the status of a science.

In *Metaphysics* IV (Γ), however, Aristotle takes what appears to be a different view. First, he argues that there is, in a way, a science that takes being as its genus (his name for it is “first philosophy”). Second, he argues that the principles of this science will be, in a way, the first principles of all (though he does not claim that the principles of other sciences can be demonstrated from them). Third, he identifies one of its first principles as the “most secure” of all principles: the principle of non-contradiction. As he states it,

> It is impossible for the same thing to belong and not belong simultaneously to the same thing in the same respect (*Met.* )

This is the most secure of all principles, Aristotle tells us, because “it is impossible to be in error about it”. Since it is a first principle, it cannot be demonstrated; those who think otherwise are “uneducated in analytics”. However, Aristotle then proceeds to give what he calls a “refutative demonstration” (*apodeixai elenktikôs*) of this principle.

Further discussion of this principle and Aristotle’s arguments concerning it belong to a treatment of his metaphysics (see Aristotle: Metaphysics). However, it should be noted that: (1) these arguments draw on Aristotle’s views about logic to a greater extent than any treatise outside the logical works themselves; (2) in the logical works, the principle of non-contradiction is one of Aristotle’s favorite illustrations of the “common principles” (*koinai archai*) that underlie the art of dialectic.

See Aristotle’s Metaphysics, Aristotle on non-contradiction, Dancy 1975, and Code 1986 for further discussion.

## 12. Time and Necessity: The Sea-Battle

The passage in Aristotle’s logical works which has received perhaps the most intense discussion in recent decades is *On Interpretation* 9, where Aristotle discusses the question whether every proposition about the future must be either true or false. Though something of a side issue in its context, the passage raises a problem of great importance to Aristotle’s near contemporaries (and perhaps contemporaries).

A **contradiction** (*antiphasis*) is a pair of propositions one of which asserts what the other denies. A major goal of *On Interpretation* is to discuss the thesis that, of every such contradiction, one member must be true and the other false. In the course of his discussion, Aristotle allows for some exceptions. One case is what he calls **indefinite** propositions such as “A man is walking”: nothing prevents both this proposition and “A man is not walking” being simultaneously true. This exception can be explained on relatively simple grounds.

A different exception arises for more complex reasons. Consider these two propositions:

1. There will be a sea-battle tomorrow
2. There will not be a sea-battle tomorrow

It seems that exactly one of these must be true and the other false. But if (1) is *now* true, then there *must* be a sea-battle tomorrow, and there *cannot* fail to be a sea-battle tomorrow. The result, according to this puzzle, is that nothing is possible except what actually happens: there are no unactualized possibilities.

Such a conclusion is, as Aristotle is quick to note, a problem both for his own metaphysical views about potentialities and for the commonsense notion that some things are up to us. He therefore proposes another exception to the general thesis concerning contradictory pairs.

This much would probably be accepted by most interpreters. What the restriction is, however, and just what motivates it are matters of wide disagreement. It has been proposed, for instance, that Aristotle adopted, or at least flirted with, a three-valued logic for future propositions, or that he countenanced truth-value gaps, or that his solution includes still more abstruse reasoning. The literature is much too complex to summarize: see Anscombe, Hintikka, D. Frede, Whitaker, Waterlow.

Historically, at least, it is likely that Aristotle is responding to an argument originating with the Megarian philosophers. He ascribes the view that only that which happens is possible to the Megarians in *Metaphysics* IX (Θ). The puzzle with which he is concerned strongly recalls the “Master Argument” of Diodorus Cronus especially in certain further details. For instance, Aristotle imagines the statement about tomorrow’s sea battle having been uttered ten thousand years ago. If it was true, then its truth was a fact about the past; if the past is now unchangeable, then so is the truth value of that past utterance. This recalls the Master Argument’s premise that “what is past is necessary”. Diodorus Cronus was active a little after Aristotle, and he was certainly influenced by Megarian views, whether or not it is correct to call him a Megarian (David Sedley 1977 argues that he was instead a member of the Dialectical School which was in any event an offshoot of the Megarians; see Dorion 1995 and Döring 1989, Ebert 2008 and the article Dialectical School)[^döring-1989][^dorion-1995][^ebert-2008][^sedley-1977]. It is therefore likely that Aristotle’s target here is some Megarian argument, perhaps a forerunner of Diodorus’ Master Argument.

## 13. Glossary of Aristotelian Terminology

- Accept: *tithenai* (in a dialectical argument)
- Accepted: *endoxos* (also ‘reputable’ ‘common belief’)
- Accident: *sumbebêkos* (see *incidental*)
- Accidental: *kata sumbebêkos*
- Affirmation: *kataphasis*
- Affirmative: *kataphatikos*
- Assertion: *apophansis* (sentence with a truth value, declarative sentence)
- Assumption: *hupothesis*
- Belong: *huparchein*
- Category: *katêgoria* (see the discussion in Section 7.3).
- Contradict: *antiphanai*
- Contradiction: *antiphasis* (in the sense “contradictory pair of propositions” and also in the sense “denial of a proposition”)
- Contrary: *enantion*
- Deduction: *sullogismos*
- Definition: *horos*, *horismos*
- Demonstration: *apodeixis*
- Denial (of a proposition): *apophasis*
- Dialectic: *dialektikê* (the *art* of dialectic)
- Differentia: *diaphora*; specific difference, *eidopoios diaphora*
- Direct: *deiktikos* (of proofs; opposed to “through the impossible”)
- Essence: *to ti esti*, *to ti ên einai*
- Essential: *en tôi ti esti* (of predications)
- Extreme: *akron* (of the major and minor terms of a deduction)
- Figure: *schêma*
- Form: *eidos* (see also Species)
- Genus: *genos*
- Immediate: *amesos* (“without a middle”)
- Impossible: *adunaton*; “through the impossible” (*dia tou adunatou*), of some proofs.
- Incidental: see Accidental
- Induction: *epagôgê*
- Middle, middle term (of a deduction): *meson*
- Negation (of a term): *apophasis*
- Objection: *enstasis*
- Particular: *en merei*, *epi meros* (of a proposition); *kath’hekaston* (of individuals)
- Peculiar, Peculiar Property: *idios*, *idion*
- Possible: *dunaton*, *endechomenon*; *endechesthai* (verb: “be possible”)
- Predicate: *katêgorein* (verb); *katêegoroumenon* (“what is predicated”)
- Predication: *katêgoria* (act or instance of predicating, type of predication)
- Primary: *prôton*
- Principle: *archê* (starting point of a demonstration)
- Quality: *poion*
- Reduce, Reduction: *anagein*, *anagôgê*
- Refute: *elenchein*; refutation, *elenchos*
- Science: *epistêmê*
- Species: *eidos*
- Specific: *eidopoios* (of a differentia that “makes a species”, *eidopoios diaphora*)
- Subject: *hupokeimenon*
- Substance: *ousia*
- Term: *horos*
- Universal: *katholou* (both of propositions and of individuals)

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=aristotle-logic). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/aristotle-logic/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=aristotle-logic&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/aristotle-logic/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

[Please contact the author with suggestions.]

## Related Entries

Aristotle, General Topics: aesthetics | Aristotle, General Topics: metaphysics | Aristotle, General Topics: rhetoric | Aristotle, Special Topics: mathematics | Aristotle, Special Topics: on non-contradiction | Chrysippus | Diodorus Cronus | future contingents | logic: ancient | logic: relevance | Megaric School | square of opposition | Stoicism

### Acknowledgments

I am indebted to Alan Code, Marc Cohen, and Theodor Ebert for helpful criticisms of earlier versions of this article. I thank Franz Fritsche, Nikolai Biryukov, Ralph E. Kenyon, Johann Dirry, Ben Greenberg, Hasan Masoud, Marc Michael Hämmerling, James Whitely, and edward@logicmuseum.com for calling my attention to errors.

[^ackrill-1961]: Ackrill, J. L., 1961. *Aristotle’s Categories and De Interpretatione* (Clarendon Aristotle Series),Oxford: Clarendon Press.

[^barnes-1981]: Barnes, Jonathan, 1981. “Proof and the Syllogism”, 17–59 in Berti 1981.

[^barnes-1994]: ––– (trans.), 1994. *Aristotle, Posterior Analytics* (translation with commentary), 2nd edition, Oxford: Clarendon Press.

[^becker-1933]: Becker, Albrecht, 1933. *Die Aristotelische Theorie der Möglichkeitsschlüsse*, Berlin: Junker und Dunnhaupt.

[^berti-1981]: Berti, Enrico (ed.), 1981. *Aristotle on Science: The Posterior Analytics*, Padua: Antenore.

[^bolton-1990]: Bolton, Robert, 1990. “The Epistemological Basis of Aristotelian Dialectic,” 185–236 in D. Devereux and P. Pellegrin (eds.), *Biologie, logique, et metaphysique chez Aristote*, Paris: Editions du CNRS, 1990.

[^broadie-1982]: Broadie, Sarah [Waterlow], 1982. *Passage and Possibility*, Oxford: Clarendon Press.

[^brunschwig-1967]: Brunschwig, Jacques (ed. & trans.), 1967. *Aristote, Topiques I–IV*, Paris: Les Belles Lettres.

[^brunschwig-2007]: –––, 2007. *Aristote, Topiques V–VIII*, Paris: Les Belles Lettres.

[^brunschwig-1984]: –––, 1984. 31–40 in “Aristotle on Arguments without Winners or Losers”. *Wissenschaftskolleg – Jahrbuch 1984/85*, Berlin.

[^burnyeat-1981]: Burnyeat, Myles, 1981. “Aristotle on Understanding Knowledge”, 97–139 in Berti 1981.

[^bydén-2000]: Bydén, Börje (translator & commentator), 2000. *Aristoteles, De Interpretatione, Om Sofistiska Vederläggningar*, Stockholm: Thales.

[^clark-1980]: Clark, Michael, 1980. *The Place of Syllogistic in Logical Theory*, Nottingham: Nottingham University Press.

[^code-1986]: Code, Alan, 1986. “Aristotle’s Investigation of a Basic Logical Principle: Which Science Investigates the Principle of Non-Contradiction?”, *Canadian Journal of Philosophy*, 16: 341–358.

[^corcoran-1972]: Corcoran, John, 1972. “Completeness of an Ancient Logic”, *Journal of Symbolic Logic*, 37: 696–705.

[^corcoran-1973]: –––, 1973. “A Mathematical Model of Aristotle’s Syllogistic”, *Archiv für Geschichte der Philosophie*, 55: 191–219.

[^cresswell-2016]: Cresswell, Max, Adrian Rini, and Edwin Mares (eds.), 2016. *Logical Modalities from Aristotle to Carnap: The Story of Necessity*, Cambridge: Cambridge University Press.

[^crivelli-2011]: Crivelli, Paolo, 2011. “Aristotle on Syllogisms from a Hypothesis”, in Angela Longo (ed.), *Argument from Hypothesis in Ancient Philosophy*, Naples: Bibliopolis, 95–184.

[^dancy-1975]: Dancy, Russell, 1975. *Sense and Contradiction*, Dordrecht: D. Reidel,

[^döring-1989]: Döring, Klaus, 1989. “Gab es eine Dialektische Schule?” *Phronesis*, 34: 293–310.

[^dorion-1995]: Dorion, Louis-André (tr. & comm.), 1995. *Les Réfutations sophistiques*, Paris: J. Vrin.

[^duncombe-2016]: Duncombe, Matthew, and Catarina Dutilh Novaes, 2016. “Dialectic and Logic in Aristotle and His Tradition.” *History and Philosophy of Logic*, 37: 1–8.

[^ebbesen-1981]: Ebbesen, Sten, 1981. *Commentators and Commentaries on Aristotle’s Sophistici Elenchi*, 3 volumes, Leiden: E. J. Brill.

[^ebert-1985]: Ebert, Theodor, 1985. “Gattungen der Prädikate und Gattungen des Seienden bei Aristoteles: Zum Verhältnis von Kat. 4 und Top. I.9”, *Archiv für Geschichte der Philosophie*, 67: 113–138.

[^ebert-2008]: –––, 2008. “In Defence of the Dialectical School”, in F. Alesse, et al. (eds.), *Anthropine Sophia*, Naples: Bibliopolis, 275–293.

[^ebert-2015]: –––, 2015. “What Is a Perfect Syllogismi in Aristotle’s Syllogistic?” *Ancient Philosophy*, 35: 351–374.

[^ebert-2007]: ––– and Nortmann, Ulrich, 2007. *Aristoteles, Analytica Priora, Buch I*, German translation with commentary, Berlin: Akademie Verlag.

[^ebrey-2015]: Ebrey, David, 2015. “Why Are There No Conditionals in Aristotle’s Logic?” *Journal of the History of Philosophy*, 53: 185–205.

[^evans-1977]: Evans, J. D. G., 1977. *Aristotle’s Concept of Dialectic*, Cambridge: Cambridge University Press.

[^fait-2007]: Fait, Paolo (tr. & comm.), 2007. *Aristotele, Le confutazione sofistiche*, Rome-Bari: Edizione Laterza.

[^fait-2013]: –––, 2013. “The ‘False Validating Premiss’ in Aristotle’s Doctrine of Fallacies. An Interpretation of *Sophistical Refutations* 8”, in Rapp and Hasper 2013, 238–267.

[^ferejohn-1980]: Ferejohn, Michael, 1980. *The Origins of Aristotelian Science*, New Haven: Yale University Press.

[^frede-1970]: Frede, Dorothea, 1970. *Aristoteles und die Seeschlacht*, Goettingen.

[^frede-2012]: –––, 2012. “The *Endoxon* Mystique: What *Endoxa* Are and What They Are Not”, *Oxford Studies in Ancient Philosophy*, 43: 185–215.

[^frede-1974]: Frede, Michael, 1974. “Stoic vs. Peripatetic Syllogistic”, *Archiv für Geschichte der Philosophie*, 56 (1): 1–32.

[^frede-1981]: –––, 1981. “Categories in Aristotle”, reprinted in M. Frede, *Essays in Ancient Philosophy*, Minneapolis: University of Minnesota Press, 1987, 29–48.

[^hambruch-1904]: Hambruch, Ernst, 1904. *Logische Regeln der Platonischen Schule in der Aristotelischen Topik*, Berlin: Weidemann.

[^hamlyn-1990]: Hamlyn, D. W., 1990. “Aristotle on Dialectic”, *Philosophy*, 65: 465–476.

[^hasper-2013]: Hasper, Pieter Sjoerd, 2013. “Aristotle’s *Sophistical Refutations*. A Translation”, in Rapp and Hasper 2013, 13–53.

[^hecquet-2019]: Hecquet, Myriam (tr. & comm.), 2019. *Aristote, Les réfutations sophistiques*, Paris: Libraire Philosophique J. Vrin.

[^hintikka-1973]: Hintikka, Jaakko, 1973. *Time and Necessity; Studies in Aristotle’s Theory of Modality*, Oxford: Clarendon Press.

[^ierodiakonou-2002]: Ierodiakonou, Katerina, 2002. “Aristotle’s Use of Examples in the *Prior Analytics*”, *Phronesis*, 47: 127–152.

[^irwin-1988]: Irwin, Terence, 1988. *Aristotle’s First Principles*, Oxford: Clarendon Press.

[^johnson-1994]: Johnson, Fred, 1994. “Apodictic Syllogisms: Deductions and Decision Procedures”, *History and Philosophy of Logic*, 16: 1–18.

[^judson-2019]: Judson, Lindsay, 2019. “Aristotle and Crossing the Boundaries between the Sciences.” *Archiv für Geschichte der Philosophie*, 101: 177–204.

[^le-1939]: Le Blond, J. M., 1939. *Logique et méthode chez Aristote*, Paris: J. Vrin.

[^lear-1980]: Lear, Jonathan, 1980. *Aristotle and Logical Theory*, Cambridge University Press.

[^jan-1957]: Łukasiewicz, Jan, 1957. *Aristotle’s Syllogistic from the Standpoint of Modern Formal Logic*, second edition, Oxford: Clarendon Press.

[^jan-1910]: –––, 1910. *O Zasadzie Sprzecznosci u Arystotelesa. Studium Krytyczne* [On the Principle of Contradiction in Aristotle. A Critical Study], Krakow: Polska Akademia Umieijetnosci; English translation as “On the Principle of Contradiction in Aristotle”, M. Wedin (trans.), *Review of Metaphysics*, 24 (1971): 485–509.

[^leszl-2004]: Leszl, Walter, 2004. “Aristotle’s Logical Works and His Conception of Logic”, *Topoi*, 23: 71–100.

[^malink-2008]: Malink, Marko, 2008. “*ΤΩI* vs. *ΤΩN* in *Prior Analytics* 1.1–22”, *Classical Quarterly*, 58: 519–536.

[^malink-2006]: –––, 2006. “A Reconstruction of Aristotle’s Modal Syllogistic”, *History and Philosophy of Logic*, 27 (2): 95–141.

[^malink-2013]: –––, 2013. *Aristotle’s Modal Syllogistic*, Cambridge, MA: Harvard University Press.

[^malink-2015]: –––, 2015. “The Beginnings of Formal Logic: Deduction in Aristotle’s *Topics* vs. *Prior Analytics*”, *Phronesis*, 60: 267–309.

[^mccall-1963]: McCall, Storrs, 1963. *Aristotle’s Modal Syllogistic*, Amsterdam: North-Holland.

[^mckirahan-1992]: McKirahan, Richard, 1992. *Principles and Proofs*, Princeton: Princeton University Press.

[^moraux-1968]: Moraux, Paul, 1968. “La joute dialectique d’après le huitième livre des *Topiques*”, in Owen 1968.

[^morison-2008]: Morison, Ben, 2008. “What Was Aristotle’s Concept of Logical Form?”, in Morison and Katerina Ierodiakonou (eds.), *Episteme, Etc.* ,Oxford: Oxford University Press, 172–188.

[^nortmann-1996]: Nortmann, Ulrich, 1996. *Modale Syllogismen, mögliche Welten, Essentialismus: eine Analyse der aristotelischen Modallogik*, Berlin: De Gruyter.

[^nortmann-2002]: –––, 2002. “The Logic of Necessity in Aristotle: An Outline of Approaches to the Modal Syllogistic, Together with a General Account of *de dicto*- and *de re*-Necessity”, *History and Philosophy of Logic*, 23: 253–265.

[^nussbaum-1986]: Nussbaum, Martha, 1986. *The Fragility of Goodness*, Cambridge: Cambridge University Press.

[^owen-1961]: Owen, G. E. L., 1961. “*Tithenai ta phainomena*”, in S. Mansion (ed.), *Aristote et les problèmes de méthode*, Louvain: Presses Universitaires de Louvain.

[^owen-1968]: ––– (ed.), 1968. *Aristotle on Dialectic: The Topics* (Proceedings of the Third Symposium Aristotelicum), Cambridge: Cambridge University Press.

[^patterson-1995]: Patterson, Richard, 1995. *Aristotle’s Modal Logic: Essence and Entailment in the Organon*, Cambridge: Cambridge University Press.

[^patzig-1969]: Patzig, Günther, 1969. *Aristotle’s Theory of the Syllogism*, Jonathan Barnes (trans.), Dordrecht: D. Reidel.

[^peterson-1969]: Peterson, Sandra, 1969. *The Masker Paradox*. Ph. D. Dissertation, Princeton.

[^primavesi-1996]: Primavesi, Oliver, 1996. *Die aristotelische Topik*, Munich: C. H. Beck.

[^rapp-2013]: Rapp, Christopher, and Pieter Sjoerd Hasper, 2013. *Logical Analysis and History of Philosophy* 15 (Special Issue: Fallacious Arguments in Ancient Philosophy).

[^rini-2011]: Rini, Adriane, 2011. *Aristotle’s Modal Proofs: Prior Analytics A8–22 in Predicate Logic*, Dordrecht: Springer.

[^ross-1951]: Ross, W. D. (ed.), 1951. *Aristotle’s Prior and Posterior Analytics*, Oxford: Clarendon Press.

[^sedley-1977]: Sedley, David, 1977. “Diodorus Cronus and Hellenistic Philosophy” *Proceedings of the Cambridge Philological Society*, 203 NS 23: 74–120.

[^slomkowski-1997]: Slomkowski, Paul, 1997. *Aristotle’s Topics*, Leiden: Brill.

[^smiley-1973]: Smiley, Timothy, 1973. “What Is a Syllogism?”, *Journal of Philosophical Logic*, 2: 136–154.

[^smiley-1994]: –––, 1994. “Aristotle’s Completeness Proof”, *Ancient Philosophy*, 14 (Special Issue): 25–38.

[^smith-1982]: Smith, Robin, 1982. “What Is Aristotelian Ecthesis?” *History and Philosophy of Logic*, 3: 113–127.

[^smith-1989]: Smith, Robin (translator & commentator), 1989. *Aristotle’s Prior Analytics*, Indianapolis: Hackett.

[^smith-1997]: –––, 1997. *Aristotle, Topics I, VIII, and Selections* (Clarendon Aristotle Series), Oxford: Clarendon Press.

[^solmsen-1929]: Solmsen, Friedrich, 1929. *Die Entwicklung der aristotelischen Logik und Rhetorik*, Berlin: Weidmann.

[^stocks-1933]: Stocks, J. L., 1933. “The Composition of Aristotle’s Logical Works.” *Classical Quartely*, 27: 115–124.

[^striker-2009]: Striker, Gisela (translator & commentator), 2009. *Aristotle, Prior Analytics I* (Clarendon Aristotle Series), Gisela Striker (trans.), Oxford: Clarendon Press.

[^striker-1985]: Striker, Gisela, 1985. “Notwendigkeit mit Lücken”, *Neue Hefte für Philosophie*, 24/25: 146–164.

[^striker-1994]: –––, 1994. “Modal vs. Assertoric Syllogistic”, *Ancient Philosophy*, 14 (Special Issue): 39–51.

[^swanson-2013]: Swanson, Carrie, 2013. “Aristotle’s Expansion of the Taxonomy of Fallacy in *De Sophisticis Elenchis* 8”, in Rapp and Hasper 2013, 200–237.

[^swanson-2016]: –––, 2016. “Begging the Question As a Criticism of an Argument in Itself in *Topics* 8.11”, *History and Philosophy of Logic*, 37: 33–77.

[^swanson-2017]: –––, 2017. “Aristotle on Ignorance of the Definition of Refutation”, *Apeiron*, 50: 153–196.

[^thom-1981]: Thom, Paul, 1981. *The Syllogism*, Munich: Philosophia Verlag.

[^thom-1996]: –––, 1996. *The Logic of Essentialism: An Interpretation of Aristotle’s Modal Syllogistic*, Dordrecht: Kluwer.

[^thomason-1993]: Thomason, Steven K., 1993. “Semantic Analysis of the Modal Syllogistic”, *Journal of Philosophical Logic*, 22: 111–128.

[^rijen-1989]: van Rijen, Jeroen, 1989. *Aspects of Aristotle’s Logic of Modalities*, Dordrecht: Reidel.

[^weidemann-1994]: Weidemann, Hermann (translator & commentator), 1994. *Aristoteles, Peri Hermeneias*, Berlin: Akademie Verlag.

[^weidemann-2004]: –––, 2004. “Aristotle on the Reducibility of All Valid Syllogistic Moods to the Two Universal Moods of the First Figure (Apr A7, 29b1–25)”, *History and Philosophy of Logic*, 25: 73–78.

[^whitaker-1996]: Whitaker, C. W. A., 1996. *Aristotle’s De Interpretatione: Contradiction and Dialectic*, Oxford: Clarendon Press.

[^wedin-1990]: Wedin, Michael V., 1990. “Negation and Quantification in Aristotle”, *History and Philosophy of Logic*, 11 (2): 131–150.
