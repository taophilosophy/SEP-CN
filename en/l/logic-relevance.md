# Relevance Logic
**First published Wed Jun 17, 1998; substantive revision Fri Nov 13, 2020**

*Mares, Edwin*

*Relevance logics* are non-classical logics. Called ‘relevant logics’ in Britain and Australasia, these systems developed as attempts to avoid the paradoxes of material and strict implication. These so-called paradoxes are valid conclusions that follow from the definitions of material and strict implication but are seen, by some, as problematic.

For example, the material implication $(p \rightarrow q)$ is true whenever $p$ is false or $q$ is true — i.e., $(\neg p \vee q)$. So if $p$ is true, then the material implication is true when $q$ is true. Among the paradoxes of material implication are the following:

$$\begin{align} & p \rightarrow(q \rightarrow p), \\ & \neg p \rightarrow(p \rightarrow q), \\ & (p \rightarrow q) \vee(q \rightarrow r). \end{align}$$

The first asserts that every proposition implies a true one; the second that a false proposition implies every proposition, and the third that for any three propositions, either the first implies the second or the second implies the third.

Similarly, the strict implication $(p \rightarrow q)$ is true whenever it is not possible that $p$ is true and $q$ is false — i.e., $\neg \diamond(p \amp \neg q)$. Among the paradoxes of strict implication are the following:

$$\begin{align} & (p \amp \neg p) \rightarrow q, \\ & p \rightarrow(q \rightarrow q), \\ & p \rightarrow(q \vee \neg q). \end{align}$$

The first asserts that a contradiction strictly implies every proposition; the second and third imply that every proposition strictly implies a tautology.

Many philosophers, beginning with Hugh MacColl (1908)[^maccoll-1908], have claimed that these theses are counterintuitive. They claim that these formulae fail to be valid if we interpret $\rightarrow$ as representing the concept of implication that we have before we learn classical logic. Relevance logicians claim that what is unsettling about these so-called paradoxes is that in each of them the antecedent seems irrelevant to the consequent.

In addition, relevance logicians have had qualms about certain inferences that classical logic makes valid. For example, consider the classically valid inference

> The moon is made of green cheese. Therefore, either it is raining in Ecuador now or it is not.

Again here there seems to be a failure of relevance. The conclusion seems to have nothing to do with the premise. Relevance logicians have attempted to construct logics that reject theses and arguments that commit “fallacies of relevance”.

Relevant logicians point out that what is wrong with some of the paradoxes (and fallacies) is that the antecedents and consequents (or premises and conclusions) are on completely different topics. The notion of a topic, however, would seem not to be something that a logician should be interested in — it has to do with the content, not the form, of a sentence or inference. But there is a formal principle that relevant logicians apply to force theorems and inferences to “stay on topic”. This is the *variable sharing principle.* The variable sharing principle says that no formula of the form $A \rightarrow B$ can be proven in a relevance logic if $A$ and $B$ do not have at least one propositional variable (sometimes called a proposition letter) in common and that no inference can be shown valid if the premises and conclusion do not share at least one propositional variable.

At this point some confusion is natural about what relevant logicians are attempting to do. The variable sharing principle is only a necessary condition that a logic must have to count as a relevance logic. It is not sufficient. Moreover, this principle does not give us a criterion that eliminates all of the paradoxes and fallacies. Some remain paradoxical or fallacious even though they satisfy variable sharing. As we shall see, however, relevant logic does provide us with a relevant notion of proof in terms of the real use of premises (see the section “Proof Theory” below), but it does not by itself tell us what counts as a true (and relevant) implication. It is only when the formal theory is put together with a philosophical interpretation that it can do this (see the section “Semantics for Relevant Implication” below).

In this article we will give a brief and relatively non-technical overview of the field of relevance logic.

## 1. Semantics for Relevant Implication

Our exposition of relevant logic is backwards to most found in the literature We will begin, rather than end, with the semantics, since most philosophers at present are semantically inclined.

The semantics that is presented here is the ternary relation semantics due to Richard Routley and Robert K. Meyer. This semantics is a development of Alasdair Urquhart’s “semilattice semantics” (Urquhart 1972)[^urquhart-1972]. There is a similar semantics, due to Kit Fine, that was developed at the same time as the Routley-Meyer theory (Fine 1974)[^fine-1974]. And there is an algebraic semantics due to J. Michael Dunn. Urquhart’s, Fine’s, and Dunn’s models are very interesting in their own right, but we do not have room to discuss them here.

The idea behind the ternary relation semantics is rather simple. Consider C.I. Lewis’ attempt to avoid the paradoxes of material implication. He added a new connective to classical logic, that of strict implication. In post-Kripkean semantic terms, $A \prurel B$ is true at a world $w$ if and only if for all $w'$ such that $w'$ is accessible to $w$, either $A$ fails in $w'$ or $B$ obtains there. Now, in Kripke’s semantics for modal logic, the accessibility relation is a binary relation. It holds between pairs of worlds. Unfortunately, from a relevant point of view, the theory of strict implication is still irrelevant. That is, we still make valid formulae like $p \prurel (q \prurel q)$. We can see quite easily that the Kripke truth condition forces this formula on us.

Like the semantics of modal logic, the semantics of relevance logic relativises truth of formulae to worlds. But Routley and Meyer go modal logic one better and use a three-place relation on worlds. This allows there to be worlds at which $q \rightarrow q$ fails and that in turn allows worlds at which $p \rightarrow(q \rightarrow q)$ fails. Their truth condition for $\rightarrow$ on this semantics is the following:

$A \rightarrow B$ is true at a world $a$ if and only if for all worlds $b$ and $c$ such that $Rabc$ $(R$ is the accessibility relation) either $A$ is false at $b$ or $B$ is true at $c$.

For people new to the field it takes some time to get used to this truth condition. But with a little work it can be seen to be just a generalisation of Kripke’s truth condition for strict implication (just set $b = c$).

The ternary relation semantics can be adapted to be a semantics for a wide range of logics. Placing different constraints on the relation makes valid different formulae and inferences. For example, if we constrain the relation so that $Raaa$ holds for all worlds $a$, then we make it true that if $(A \rightarrow B) \amp A$ is true at a world, then $B$ is also true there. Given other features of the Routley-Meyer semantics, this makes the thesis $((A \rightarrow B) \amp A) \rightarrow B$ valid. If we make the ternary relation symmetrical in its first two places, that is, we constrain it so that, for all worlds $a, b$, and $c$, if $Rabc$ then $Rbac$, then we make valid the thesis $A \rightarrow ((A \rightarrow B) \rightarrow B)$.

The ternary accessibility relation needs a philosophical interpretation in order to give relevant implication a real meaning on this semantics. Recently there have been several interpretations developed based on theories of information.

One interpretation is suggested in Jon Barwise (1993)[^barwise-1993] and developed in Restall (1996)[^restall-1996]. On this view, worlds are taken to be information-theoretic “sites” and “channels”. A site is a context in which information is received and a channel is a conduit through which information is transferred. Thus, for example, when the BBC news appears on the television in my living room, we can consider the living room to be a site and the wires, satellites, and so on, that connect my television to the studio in London to be a channel. Using channel theory to interpret the Routley-Meyer semantics, we take $Rabc$ to mean that $a$ is an information-theoretic channel between sites $b$ and $c$. Thus, we take $A \rightarrow B$ to be true at $a$ if and only if, whenever $a$ connects a site $b$ at which $A$ obtains to a site $c, B$ obtains at $c$.

Similarly, Mares (1997)[^mares-1997] uses a theory of information due to David Israel and John Perry (1990). In addition to other information a world contains informational links, such as laws of nature, conventions, and so on. For example, a Newtonian world will contain the information that all matter attracts all other matter. In information-theoretic terms, this world contains the information that two things’ being material carries the information that they attract each other. On this view, $Rabc$ if and only if, according to the links in $a$, all the information carried by what obtains in $b$ is contained in $c$. Thus, for example, if $a$ is a Newtonian world and the information that $x$ and $y$ are material is contained in $b$, then the information that $x$ and $y$ attract each other is contained in $c$.

Another interpretation is developed in Mares (2004)[^mares-2004]. This interpretation takes the Routley-Meyer semantics to be a formalisation of the notion of “situated implication”. This interpretation takes the “worlds” of the Routley-Meyer semantics to be *situations*. A situation is a perhaps partial representation of the universe. The information contained in two situations, $a$ and $b$ might allow us to infer further information about the universe that is contained in neither situation. Thus, for example, suppose in our current situation that we have the information contained in the laws of the theory of general relativity (this is Einstein’s theory of gravity). Then we hypothesise a situation in which we can see a star moving in an ellipse. Then, on the basis of the information that we have and the hypothesised situation, we can infer that there is a situation in which there is a very heavy body acting on this star.

We can model situated inference using a relation $I$ (for “implication”). Then we have $IabP$, where $P$ is a proposition, if and only if the information in $a$ and $b$ together license the inference to there being a situation in which $P$ holds. We can think of a proposition itself as a set of situations. We set $A \rightarrow B$ to hold at $a$ if and only if, for all situations $b$ in which $A$ holds, $Iab|B|,$ where $|B$| is the set of situations at which $B$ is true. We set $Rabc$ to hold if and only if $c$ belongs to every proposition $P$ such that $IabP$. With the addition of the postulate that, for any set of propositions $P$ such that $IabP$, the intersection of that set $X$ is such that $IabX$, we find that the implications that are made true on any situation using the truth condition that appeals to $I$ are the same as those that are made true by the Routley-Meyer truth condition. Thus, the notion of situated inference gives a way of understanding the Routley-Meyer semantics. (This is a very brief version of the discussion of situated inference that is in chapters 2 and 3 of Mares (2004)[^mares-2004].)

Another informational interpretation is in Dunn (2015)[^dunn-2015]. This interpretation neatly connects the concept of relevance in relevance logic with the pragmatic notion of relevance in Grice’s conversational maxims and in Sperber and Wilson’s pragmatic theory. The idea is that the relation $R$ holds between three “states”, $a,b$, and $c$ if in the context $a, b$ is relevant to $c$. This means that using the information both in $a$ and $b$ allows one to derive the information in $c$. The notion of derivation here is one that Sperber and Wilson call “contextual implication”. The result is derivable from the information in $a$ and $b$, but not from the information in either alone (Sperber and Wilson, 2002, p. 251)[^sperber-2002]. There are various ways to think of the combination of information in $a$ and $b$. One that Dunn discusses is to think of $a$ and $b$ as being similar to computer programs and the combination of the two is their composition -- the result of running $b$ and taking the result of that as input for $a$, and then running $a$. This combination is relevant to $c$ if the information produced by it is all contained in $c$.

A different sort of interpretation is given by Beall, et al. (2012). In fact, Beall, et al (2012) presents three different interpretations of the ternary relation. These interpretations link the ternary relation with different notions of “conditionality”. I discuss only two of these interpretations here. The third is a bit too involved for inclusion in an encyclopedia entry. On the first of these interpretations, a conditional $A\rightarrow B$ holds at a world $a$ if there is no counterexample to this conditional, i.e. a place salient to $a$ at which $A$ holds and $B$ fails to hold. This “place” is not a single world, but a pair of worlds, $b, c$. A pair consists in a counterexample to the conditional if $A$ is true at the first of the pair and $B$ is not true at the second.

On the second interpretation, the points of Routley-Meyer models are considered to be both operators (in the mathematical sense) and the things that they operate on. On this understanding, $Rabc$ means that considered as an operator, $a$ when applied to $b$ yields information all of which is contained in $c$. This interpretation makes the Routley-Meyer semantics very similar in intent to Fine’s operational semantics. And this interpretaion is very closely related to Dunn’s interpetation (in particular in his notion of the combining of information in states).

By itself, the use of the ternary relation is not sufficient to avoid all the paradoxes of implication. Given what we have said so far, it is not clear how the semantics can avoid paradoxes such as $(p \amp \neg p) \rightarrow q$ and $p \rightarrow (q \vee \neg q)$. These paradoxes are avoided by the inclusion of inconsistent and non-bivalent worlds in the semantics. For, if there were no worlds at which $p \amp \neg p$ holds, then, according to our truth condition for the arrow, $(p \amp \neg p) \rightarrow q$ would also hold everywhere. Likewise, if $q \vee \neg q$ held at every world, then $p \rightarrow(q \vee \neg q)$ would be universally true.

An approach to relevance that does not require the ternary relation is due to Routley and Loparic (1978) and Priest (1992) and (2008). This semantics uses a set of worlds and a binary relation, $S$. Worlds are divided into two categories: normal worlds and non-normal worlds. An implication $A \rightarrow B$ is true at a normal world $a$ if and only if for all worlds $b$, if $A$ is true at $b$ then $B$ is also true true at $b$. At non-normal worlds, the truth values for implications are random. Some may be true and others false. A formula is valid if and only if it is true on every such model in its *normal* worlds. This division of worlds into normal and non-normal and the use of random truth values for implications at non-normal worlds enables us to find countermodels for formulas such as $p \rightarrow (q \rightarrow q)$.

Priest interprets non-normal worlds as the worlds that correspond to “logic fictions”. In a science fiction, the laws of nature may be different than those in our universe. Similarly, in a logic fiction the laws of logic may be different from our laws. For example, $A \rightarrow A$ may fail to be true in some logic fiction. The worlds that such fictions describe are non-normal worlds.

One problem with the semantics without the ternary relation is that it is difficult to use it to characterize as wide a range of logical systems as can done with the ternary relation. In addition, the logics determined by this semantics are quite weak. For example, they do not have as a theorem the transitivity of implication — $((A \rightarrow B) \amp(B \rightarrow C)) \rightarrow (A \rightarrow C)$.

Like the ternary relation semantics, this semantics requires some worlds to be inconsistent and some to be non-bivalent.

## 2. Semantics for Negation

The use of non-bivalent and inconsistent worlds requires a non-classical truth condition for negation. In the early 1970s, Richard and Val Routley invented their “star operator” to treat negation (Routley & Routley 1972). The operator is an operator on non-normal worlds. For each world $a$, there is a world $a$\*. And

$\neg A$ is true at $a$ if and only if $A$ is false at $a$\*.

Once again, we have the difficulty of interpreting a part of the formal semantics. One interpretation of the Routley star is that of Dunn (1993)[^dunn-1993]. Dunn uses a binary relation, $C$, on worlds. $Cab$ means that $b$ is compatible with $a. a$\*, then, is the maximal world (the world containing the most information) that is compatible with $a$.

There are other semantics for negation. One, due to Dunn, is a four-valued semantics. As is the case for truth tables for classical logic, this semantics begins with the values T (true) and F (false). A formula is given a set of these truth values. Thus, a formula $A$ can get the values $\{\True\}$, $\{\False\}$, $\{\True,\False\}$, or $\varnothing$. If a formula gets the value $\{\True\}$, then it is just true; likewise, if it gets the value $\{\False\}$ it is just false; if it gets the value $\{\True,\False\}$ it is both true and false; if it gets the value $\varnothing$, it is neither true nor false.

Each formula is given a truth condition and a falsity condition. For example, T is in the value of $\neg A$ if and only if F is in the value of $A$ and F is in the value of $\neg A$ if and only if T is in the value of $A$. With regard to conjunction, T is in the value of $A \amp B$ if and only if T is in the value of $A$ and T is in the value of $B$ and F is in the value of $A \amp B$ if and only if F is the value of $A$ or F is in the value of $B$. Disjunction has very similar truth and falsity conditions.

Dunn put forward his semantics to characterize the logic of First Degree Entailment (FDE), which treats only entailments between implication-free formulas. (For papers on the nature and development of FDE, see Omori & Wansing 2017.)[^omori-2017] Richard Routley (1988) extended the theory to treat some weak relevant logics, and Restall (1995)[^restall-1995] extended the theory to treat logics just weaker than the prominent relevant logics E and R (see sections 4 and 5 below). Mares (2004a)[^mares-2004a] used a neighbourhood semantics, together with four truth-values to give a semantics for R. The four-valued semantics is treated in more detail the entry on paraconsistent logics. Other treatments of negation, some of which have been used for relevance logics, can be found in Wansing (2001)[^wansing-2001] and in the entry on negation.

## 3. Semantics for Quantification

In (1980), Richard Routley conjectured that a constant domain semantics, in the sense that is familiar from modal logic, will characterize quantified relevant relevant logics. On this semantics, a universally quantified formula $\forall xA(x)$ is true at a world if and only if $A(x)$ is true on every interpretation of $x$.

Unfortunately, Kit Fine (1988a)[^fine-1988a] proved that the logic RQ (the logic R of relevant implication together with some standard quantificational axioms) is incomplete over the constant domain semantics.

Fine (1988b)[^fine-1988b] also developed a semantics over which RQ is complete and which can be modified to accommodate any of the mainstream relevance logics. Fine’s semantics is “stratified”. This means that a model is made up of a collection of miniature models, each with its own domain of individuals. Each of these mini-models is related to models with larger domains, and each world in a model is similarly related to worlds in these models with larger domains. A very clear explanation of how Fine’s semantics works is given in Shay Logan (2019)[^logan-2019].

Another semantics for quantified relevance logics is given by Mares and Robert Goldblatt (2006) and further developed in Goldblatt (2011)[^goldblatt-2011]. In addition to worlds and domains, a model on this theory contains a set of propositions, which are designated sets of words. A formula $\forall xA(x)$ is true at a world $w$ if and only if there is a proposition *π* true at $w$ such that *π* entails every instance of $A(x)$. This means that at every world in the set *π*, every instance of $A(x)$ is true.

The Mares-Goldblatt semantics is called an “admissible set” semantics. The propositions are the admissible sets. In some models at least, not every set of worlds counts as a proposition. One rationale for that comes from reflection on how humans relate circumstances together as similar. Not every set of situations are such that we would see a similarity that the members of the set have to one another and to no other situations outside the set. It seems reasonable to think of a proposition as a set of worlds that could act as a content for some person. (Perhaps if we were to construct a language to talk about what people could think in other words, we could index sets of propositions to worlds. But that is a topic to be left for some other time.)

One useful addition to the relevant theory of quantification is a conditional that is used to represent restricted quantification. This is developed by Jc Beall, et al. (2006). Consider the categorial scheme, “All $A$s are $B$s”. This scheme is translated into the language of classical logic as $\forall x(A(x)\supset B(x))$. The material conditional, $\supset$, is too weak to do this job in relevant logic (where $A\supset B$ is understood as $\neg A\vee B)$. If we were to use material implication is this manner, in a model for relevant logic, we could have a world in which all $A$s are $B$s, and some $i$ is $A$, but where $i$ is not $B$. The material conditional is too weak, but relevant implication is too strong. When one says, for example, “Everyone in this room owns a dog”, she does not mean that it follows from being in this room that people own a dog. Rather, it just happens that every person in this room owns a dog. It is this connection, that lies somewhere between material and relevant implication that the restricted quantificational conditional is supposed to capture.

It is unclear, however, that the conditional of Beall, et al. (2006) is the right connective to use, at least with regard to some weaker relevance logics. One virtue of some weaker systems is that they can be used to formalise naive set theory (see section 6). Zach Weber (2010)[^weber-2010] has formalised naive set theory, using this conditional to define the subset relation. The resulting system, unfortunately, is trivial in that every formula is provable in it.

## 4. Proof Theory

The logic that is often taken to be the paradigm relevance logic is the logic $\mathbf{R}$. For an axiomatisation of $\mathbf{R}$, see [Logic $\mathbf{R}$](logic-relevance.logicr.md).

There are now several approaches to the proof theory for $\mathbf{R}$. There is a sequent calculus for the negation-free fragment of the logic $\mathbf{R}$ due to Gregory Mints (1972) and J.M. Dunn (1973)[^dunn-1973] and an elegant and very general approach called “Display Logic” developed by Nuel Belnap (1982)[^belnap-1982]. But here I will only deal with the natural deduction system for the relevant logic $\mathbf{R}$ due to Anderson and Belnap.

Anderson and Belnap’s natural deduction system is based on Fitch’s natural deduction systems for classical and intuitionistic logic. The easiest way to understand this technique is by looking at an example.

| 1. | $A_{\{1\}}$ | Hyp |
| --- | --- | --- |
| 2. | $(A \rightarrow B)_{\{2\}}$ | Hyp |
| 3. | $B_{\{1,2\}}$ | $1,2, \rightarrow$ E |

This is a simple case of modus ponens. The numbers in set brackets indicate the hypotheses used to prove the formula. We will call them ‘indices’. The indices in the conclusion indicate which hypotheses are really used in the derivation of the conclusion. In the following “proof” the second premise is not really used:

| 1. | $A_{\{1\}}$ | Hyp |
| --- | --- | --- |
| 2. | $B_{\{2\}}$ | Hyp |
| 3. | $(A \rightarrow B)_{\{3\}}$ | Hyp |
| 4. | $B_{\{1,3\}}$ | $1,3, \rightarrow$ E |

This “proof” really just shows that the inference from $A$ and $A \rightarrow B$ to $B$ is relevantly valid. Because the number 2 does not appear in the subscript on the conclusion, the second “premise” does not really count as a premise.

Similarly, when an implication is proven relevantly, the assumption of the antecedent must really be used to prove the conclusion. Here is an example of the proof of an implication:

| 1. | $A_{\{1\}}$ | Hyp |
| --- | --- | --- |
| 2. | $(A \rightarrow B)_{\{2\}}$ | Hyp |
| 3. | $B_{\{1,2\}}$ | $1,2, \rightarrow$ E |
| 4. | $((A \rightarrow B) \rightarrow B)_{\{1\}}$ | $2,3, \rightarrow$ I |
| 5. | $A \rightarrow((A \rightarrow B) \rightarrow B)$ | $1,4, \rightarrow$ I |

When we discharge a hypothesis, as in lines 4 and 5 of this proof, the number of the hypothesis must really occur in the subscript of the formula that is to become the consequent of the implication.

Now, it might seem that the system of indices allows irrelevant premises to creep in. One way in which it might appear that irrelevances can intrude is through the use of a rule of conjunction introduction. That is, it might seem that we can always add in an irrelevant premise by doing, say, the following:

| 1. | $A_{\{1\}}$ | Hyp |
| --- | --- | --- |
| 2. | $B_{\{2\}}$ | Hyp |
| 3. | $(A \amp B)_{\{1,2\}}$ | 1,2, &I |
| 4. | $B_{\{1,2\}}$ | 3, &E |
| 5. | $(B \rightarrow B)_{\{1\}}$ | $2,4, \rightarrow$ I |
| 6. | $A \rightarrow(B \rightarrow B)$ | $1,5, \rightarrow$ I |

To a relevance logician, the first premise is completely out of place here. To block moves like this, Anderson and Belnap give the following conjunction introduction rule:

From $A_i$ and $B_i$ to infer $(A \amp B)_i$.

This rule says that two formulae to be conjoined must have the same index before the rule of conjunction introduction can be used.

There is, of course, a lot more to the natural deduction system (see Anderson and Belnap 1975 and Anderson, Belnap, and Dunn 1992)[^anderson-1975], but this will suffice for our purposes. The theory of relevance that is captured by at least some relevant logics can be understood in terms of how the corresponding natural deduction system records the real use of premises.

## 5. Some Systems of Relevance Logic

In the work of Anderson and Belnap the central systems of relevance logic were the logic $\mathbf{E}$ of relevant entailment and the system $\mathbf{R}$ of relevant implication. The relationship between the two systems is that the entailment connective of $\mathbf{E}$ was supposed to be a strict (i.e. necessitated) relevant implication. To compare the two, Meyer added a necessity operator to $\mathbf{R}$ (to produce the logic $\mathbf{NR})$. Larisa Maksimova, however, discovered that $\mathbf{NR}$ and $\mathbf{E}$ are importantly different — that there are theorems of $\mathbf{NR}$ (on the natural translation) that are not theorems of $\mathbf{E}$. This has left some relevant logicians with a quandary. They have had to decide whether to take $\mathbf{NR}$ or $\mathbf{E}$ to be the system of relevant entailment. If $\mathbf{E}$ is chosen, then perhaps it is not reasonable to say that entailment is just relevant implication together with logical necessity. It may be that entailment and implication are related in some other way.

On the other hand, there are those relevance logicians who reject both $\mathbf{R}$ and $\mathbf{E}$. There are those, like Arnon Avron, who accept logics stronger than $\mathbf{R}$ (Avron 1990)[^avron-1990]. And there are those, like Ross Brady, John Slaney, Steve Giambrone, Richard Sylvan, Graham Priest, Greg Restall, and others, who have argued for the acceptance of systems weaker than $\mathbf{R}$ or $\mathbf{E}$. One extremely weak system is the logic $\mathbf{S}$ of Robert Meyer and Errol Martin. As Martin has proven, this logic contains no theorems of the form $A \rightarrow A$. In other words, according to $\mathbf{S}$, no proposition implies itself and no argument of the form ‘$A$, therefore $A$’ is valid. Thus, this logic does not make valid any circular arguments.

For more details on these logics see supplements on the [logic $\mathbf{E}$](logic-relevance.logice.md), [logic $\mathbf{R}$](logic-relevance.logicr.md), [logic $\mathbf{NR}$](logic-relevance.logicnr.md), and [logic $\mathbf{S}$](logic-relevance.logics.md).

Among the points in favour of weaker systems is that, unlike $\mathbf{R}$ or $\mathbf{E}$, many of them are decidable. Another feature of some of these weaker logics that makes them attractive is that they can be used to construct a naïve set theory. A naïve set theory is a theory of sets that includes as a theorem the naïve comprehension axiom, viz., for all formulae $A(y)$,

$\exists x\forall y(y \in x \leftrightarrow A(y))$.

In set theories based on strong relevant logics, like $\mathbf{E}$ and $\mathbf{R}$, as well as in classical set theory, if we add the naïve comprehension axiom, we are able to derive any formula at all. Thus, naïve set theories based on systems such as $\mathbf{E}$ and $\mathbf{R}$ are said to be “trivial”. Here is an intuitive sketch of the proof of the triviality of a naïve set theory using principles of inference from the logic **R.** Let $p$ be an arbitrary proposition:

| 1. | $\exists x\forall y(y \in x \leftrightarrow(y \in y \rightarrow p))$ | Naïve Comprehension |
| --- | --- | --- |
| 2. | $\forall y(y \in z \leftrightarrow (y \in y \rightarrow p))$ | 1, Existential Instantiation |
| 3. | $z \in z \leftrightarrow(z \in z \rightarrow p)$ | 2, Universal Instantiation |
| 4. | $z \in z \rightarrow(z \in z \rightarrow p)$ | 3, df of $\leftrightarrow$ , &-Elimination |
| 5. | $(z \in z \rightarrow (z \in z \rightarrow p)) \rightarrow(z \in z \rightarrow p)$ | Axiom of Contraction |
| 6. | $z \in z \rightarrow p$ | 4,5, Modus Ponens |
| 7. | $(z \in z \rightarrow p)) \rightarrow z \in z$ | 3, df of $\leftrightarrow$ , &-Elimination |
| 8. | $z \in z$ | 6,7, Modus Ponens |
| 9. | $p$ | 6,8, Modus Ponens |

Thus we show that any arbitrary proposition is derivable in this naïve set theory. This is the infamous Curry Paradox. The existence of this paradox has led Grishen, Brady, Restall, Priest, and others to abandon the axiom of contraction $((A \rightarrow (A \rightarrow B)) \rightarrow(A \rightarrow B))$. Brady has shown that by removing contraction, plus some other key theses, from $\mathbf{R}$ we obtain a logic that can accept naïve comprehension without becoming trivial (Brady 2005)[^brady-2005].

In terms of the natural deduction system, the presence of contraction corresponds to allowing premises to be used more than once. Consider the following proof:

| 1. | $A \rightarrow(A \rightarrow B)_{\{1\}}$ | Hyp |
| --- | --- | --- |
| 2. | $A_{\{2\}}$ | Hyp |
| 3. | $A \rightarrow B_{\{1,2\}}$ | $1,2, \rightarrow$ E |
| 4. | $B_{\{1,2\}}$ | $2,3, \rightarrow$ E |
| 5. | $A \rightarrow B_{\{1\}}$ | 2–$4, \rightarrow$ I |
| 6. | $(A \rightarrow(A \rightarrow B)) \rightarrow (A \rightarrow B)$ | 1–$5, \rightarrow$ I |

What enables the derivation of contraction is the fact that our subscripts are sets. We do not keep track of how many times (more than once) that a hypothesis is used in its derivation. In order to reject contraction, we need a way of counting the number of uses of hypotheses. Thus natural deduction systems for contraction-free systems use “multisets” of relevance numerals instead of sets — these are structures in which the number of occurrences of a particular numeral counts, but the order in which they occurs does not. Even weaker systems can be constructed, which keep track also of the order in which hypotheses are used (see Read 1986 and Restall 2000)[^restall-2000].

For three of the better known and more widely used weak relevant logics, $\mathbf{B}, \mathbf{DK}$, and $\mathbf{DJ}$, see the supplement on them:

[The logics $\mathbf{B}, \mathbf{DJ}$, and $\mathbf{DK}$](logic-relevance.logic-b-dj-dk.md).

## 6. Systems Closely Related to Mainstream Relevance Logic

There are some systems that deserve to be called *relevant* that are not mainstream relevant logic. One such system is Graham Priest’s logic N$_4$. The easiest way to present this logic is to explain its semantics.

A model for N$_4$ consists in a set of world that is partitioned into normal and non-normal worlds. At every world, formulas are given one of four truth values, in accordance with Dunn’s semantics explained in section 2 above, with regard to conjunction, disjunction, and negation. But the treatment of implication is rather interesting. At normal worlds, an implication $A\rightarrow B$, is true if and only if in every world w, if $A$ is true in w, then $B$ is also true in w. The implication is false if there is at least one world in which $A$ is true and $B$ is false. At non-normal worlds, implications are made true and false randomly.

N$_4$ is a relevant logic. It has the variable-sharing property. And it has a very simple and intuitive semantics. It is, however, a very weak logic. It does not contain any transitivity axioms for implication. It has a transitivity rule. It does not contain either the contraposition axiom nor the rule form of contraposition.

Another very interesting logic is Neil Tennant’s Core Logic. One of the “fallacies” that relevance logic was created to avoid is ex falso quodlibet, or explosion – the inference from a contradiction to any proposition whatsoever. C.I. Lewis justified explosion by means of a little argument. He started with the premise $p \amp \neg p$. By conjunction elimination he derived, $p$, and by disjunction introduction, $p\vee q$. From the premise, he also derived $\neg p$, by conjunction elimination. Thus, he had $p\vee q$ and $\neg p$. From these, by disjunctive syllogism, Lewis derived $q$. Mainstream relevance logicians block this argument by rejecting disjunctive syllogism. The rejection of disjunctive syllogism, however, has become one of the most controversial aspects of relevance logic.

Tennant’s core logic, however, accepts disjunctive syllogism. It also accepts conjunction elimination and disjunction introduction. In fact, Core Logic supports all the standard primitive rules that we find in the proof theory of intuitionist logic. Thus, one could say that the meanings of the connectives in Core logic are just their meanings in intuitionist logic. What is different is its treatment of one of the structural rules of proof -- it rejects the transitivity of logical consequence in its most general form.

Yet another logical system that is closely related to relevance logic is William Parry’s logic of Analytic Implication. Analytic Implication is motivated by the desire to satisfy a very strong form of variable-sharing. No implication $A\rightarrow B$ is provable in this logic unless $\mathbf{all}$ the variables in $B$ are contained in $A$. In order to satisfy this strong variable-sharing principle, the principle of disjunction introduction needs to be restricted. So, instead of having $A\rightarrow(A\vee B)$ as a theorem for all formulas $A$ and $B$, this schema is valid only when all the propositional variables in $B$ are also in $A$. The principle of contraposition and some transitivity principles for implication also have to be restricted.

Analytic Implication has been given an elegant possible worlds semantics by Kit Fine. Fine adds to a possible worlds model a domain of subject matters. An implication holds at a world if and only if it both preserves truth at all accessible worlds and also every subject matter of the consequent is also a subject matter of the antecedent (Fine 1986)[^fine-1986].

For a comparison of Analytic Implication and relevance logic, see Routley, et al., 1982, pages 96–101. For a detailed examination and defense of Analytic Implication, see Ferguson (2017)[^ferguson-2017].

## 7. Applications and Extensions of Relevance Logic

Apart from the motivating applications of providing better formalisms of our pre-formal notions of implication and entailment and providing a basis for naïve set theory, relevance logic has been put to various uses in philosophy and computer science. Here I will list just a few.

Dunn has developed a theory of intrinsic and essential properties based on relevant logic. This is his theory of *relevant predication*. Briefly put, a thing $i$ has a property $F$ relevantly iff $\forall x(x{=}i \rightarrow F(x))$. Informally, an object has a property relevantly if being that thing relevantly implies having that property. Since the truth of the consequent of a relevant implication is by itself insufficient for the truth of that implication, things can have properties irrelevantly as well as relevantly. Dunn’s formulation would seem to capture at least one sense in which we use the notion of an intrinsic property. Adding modality to the language allows for a formalisation of the notion of an essential property as a property that is had both necessarily and intrinsically (see Anderson, Belnap, and Dunn 1992, §74).

Relevant logic has been used as the basis for mathematical theories other than set theory. Meyer has produced a variation of Peano arithmetic based on the logic $\mathbf{R}$. Meyer gave a finitary proof that his relevant arithmetic does not have $0 = 1$ as a theorem. Thus Meyer solved one of Hilbert’s central problems in the context of relevant arithmetic; he showed using finitary means that relevant arithmetic is absolutely consistent. This makes relevant Peano arithmetic an extremely interesting theory. Unfortunately, as Meyer and Friedman have shown, relevant arithmetic does not contain all of the theorems of classical Peano arithmetic. Hence we cannot infer from this that classical Peano arithmetic is absolutely consistent (see Meyer and Friedman 1992)[^meyer-1992].

Anderson (1967)[^anderson-1967] formulated a system of deontic logic based on $\mathbf{R}$ and, more recently, relevance logic has been used as a basis for deontic logic by Mares (1992)[^mares-1992] and Lou Goble (1999)[^goble-1999]. These systems avoid some of the standard problems with more traditional deontic logics. One problem that standard deontic logics face is that they make valid the inference from $A$’s being a theorem to $OA$’s being a theorem, where ‘$OA$’ means ‘it ought to be that $A$’. The reason that this problem arises is that it is now standard to treat deontic logic as a normal modal logic. On the standard semantics for modal logic, if $A$ is valid, then it is true at all possible worlds. Moreover, $OA$ is true at a world $a$ if and only if $A$ is true at every world accessible to $a$. Thus, if $A$ is a valid formula, then so is $OA$. But it seems silly to say that every valid formula ought to be the case. Why should it be the case that either it is now raining in Ecuador or it is not? In the semantics for relevant logics, not every world makes true every valid formula. Only a special class of worlds (sometimes called “base worlds” and sometimes called “normal worlds”) make true the valid formulae. Any valid formula can fail at a world. By allowing these “non-normal worlds” in our models, we invalidate this problematic rule.

Other sorts of modal operators have been added to relevance logic as well. Fuhrmann (1990)[^fuhrmann-1990] adapts the usual axioms for the familiar classical modal logics to the relevant context to produce a collection of relevant modal logics and proves completeness results for them. Epistemic modal operators have been added to relevance logics by Heinrich Wansing (2002)[^wansing-2002], Marta Bilkova, Ondrej Majer, Michal Peliš, and Greg Restall (2010), among others. Shawn Standefer (2019)[^standefer-2019] has produced a relevant version of justification logic and has very recently added an actuality opertor to relevance logic. There is even a relevant logic of questions and answers (see Punčochář 2020)[^punčochář-2020].

Routley and Val Plumwood (1989) and Mares and André Fuhrmann (1995) present theories of counterfactual conditionals based on relevant logic. Their semantics adds to the standard Routley-Meyer semantics an accessibility relation that holds between a formula and two worlds. On Routley and Plumwood’s semantics, $A\gt B$ holds at a world $a$ if and only if for all worlds $b$ such that $SAab$, $B$ holds at $b$. Mares and Fuhrmann’s semantics is slightly more complex: $A\gt B$ holds at a world $a$ if and only if for all worlds $b$ such that $SAab$, $A \rightarrow B$ holds at $b$ (also see Brady (ed.) 2002, §10 for details of both semantics). Mares (2004)[^mares-2004] presents a more complex theory of relevant conditionals that includes counterfactual conditionals. All of these theories avoid the analogues of the paradoxes of implication that appear in standard logics of counterfactuals.

Relevant logics have been used in computer science as well as in philosophy. Linear logics — a branch of logic initiated by Jean-Yves Girard — is a logic of computational resources. Linear logicians read an implication $A \rightarrow B$ as saying that having a resource of type $A$ allows us to obtain something of type $B$. If we have $A \rightarrow(A \rightarrow B)$, then, we know that we can obtain a $B$ from two resources of type $A$. But this does not mean that we can get a $B$ from a single resource of type $A$, i.e. we don’t know whether we can obtain $A \rightarrow B$. Hence, contraction fails in linear logic. Linear logics are, in fact, relevant logics that lack contraction and the distribution of conjunction over disjunction $((A \amp(B \vee C)) \rightarrow((A \amp B) \vee(A \amp C)))$. They also include two operators (! and ?) that are known as “exponentials”. Putting an exponential in front of a formula gives that formula the ability to act classically, so to speak. For example, just as in standard relevance logic, we cannot usually merely add an extra premise to a valid inference and have it remain valid. But we can always add a premise of the form $!A$ to a valid inference and have it remain valid. Linear logic also has contraction for formulae of the form $!A$, i.e., it is a theorem of these logics that $(!A \rightarrow(!A \rightarrow B)) \rightarrow(!A \rightarrow B)$ (see Troelstra 1992)[^troelstra-1992]. The use of ! allows for the treatment of resources “that can be duplicated or ignored at will” (Restall 2000, p 56)[^restall-2000]. For more about linear logic, see the entry on substructural logic.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

### Books on Relevance Logic and Introductions to the Field:

### Other Works Cited:

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=logic-relevance). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/logic-relevance/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=logic-relevance&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/logic-relevance/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- Jago, M., forthcoming, “[Truthmaker Semantics for Relevant Logic](https://link.springer.com/article/10.1007/s10992-019-09533-9)” *Journal of Philosophical Logic*, first online 7 January 2020, doi:10.1007/s10992-019-09533-9 [This paper develops a semantics for relevance logic based on Kit Fine’s theory of truthmakers.]

## Related Entries

dialetheism | logic: intuitionistic | logic: modal | logic: paraconsistent | logic: substructural | mathematics: inconsistent | negation

### Acknowledgments

The author would like to thank an anonymous reviewer and Shawn Standefer for suggesting corrections and improvements.

[^an-1992]: An extremely good, although slightly out of date, bibliography on relevance logic was put together by Robert Wolff and is in Anderson, Belnap, and Dunn (1992). What follows is a brief list of introductions to and books about relevant logic and works that are referred to above.

[^anderson-1975]: Anderson, A.R. and N.D. Belnap, Jr., 1975, *Entailment: The Logic of Relevance and Necessity*, Princeton, Princeton University Press, Volume I. Anderson, A.R. N.D. Belnap, Jr. and J.M. Dunn (1992) *Entailment*, Volume II. These are both collections of slightly modified articles on relevance logic together with a lot of material unique to these volumes. Excellent work and still the standard books on the subject. But they are very technical and quite difficult.

[^avron-2014]: Avron, A., 2014, “What is Relevance Logic?” *Annals of Pure and Applied Logic* 165:26–48. This paper puts forward a rather different view of what makes a relevance logic relevant.

[^beall-2012]: Beall, Jc, Ross Brady, J. Michael Dunn, A. P. Hazen, Edwin Mares, Robert K. Meyer, Graham Priest, Greg Restall, David Ripley, John Slaney and Richard Sylvan, 2012, “On the ternary relation and conditionality,” *Journal of Philosophical Logic*, 41(3): 595–612.

[^beall-2006]: Beall, JC, R. Brady, A. Hazen, G. Priest, and G. Restall, 2006, “Relevant Restricted Quantification,” *Journal of Philosophical Logic*, 35(6): 587–598.

[^brady-2005]: Brady, R.T., 2005, *Universal Logic*, Stanford: CSLI Publications, 2005. A difficult, but extremely important book, which gives details of Brady’s semantics and his proofs that naïve set theory and higher order logic based on his weak relevant logic are consistent.

[^dunn-1986]: Dunn, J.M., 1986, “Relevance Logic and Entailment,” in F. Guenthner and D. Gabbay (eds.), *Handbook of Philosophical Logic* (Volume 3), Dordrecht: Reidel, pp. 117–24.

[^dunn-1986-2]: Dunn, J.M. and G. Restall, “Relevance Logic” in D. Gabbay & F. Guenthner (eds.), *Handbook of Philosophical Logic* (Volume 6), second edition, Dordrecht: Springer, pp. 1–128. An updated and greatly expanded version of Dunn (1986).

[^mares-2004]: Mares, E.D., 2004, *Relevant Logic: A Philosophical Interpretation*, Cambridge: Cambridge University Press.

[^mares-2001]: Mares, E.D. and R.K. Meyer, 2001, “Relevant Logics,” in L. Goble (ed.), *The Blackwell Guide to Philosophical Logic*, Oxford: Blackwell.

[^norman-1988]: Norman, J. and R. Sylvan, 1988, *Directions in Relevant Logic*, Dordrecht: Kluwer. A good, although somewhat dated, collection of essays on relevance logic together with some on related logics, such as analytic implication.

[^paoli-2002]: Paoli, F., 2002, *Substructural Logics: A Primer*, Dordrecht: Kluwer. Excellent and clear introduction to a field of logic that includes relevance logic.

[^priest-2008]: Priest, G., 2008, *An Introduction to Non-Classical Logic: From If to Is*, Cambridge: University of Cambridge Press. A very good and extremely clear presentation of relevant and other non-classical logics that uses a tableau approach to proof theory.

[^read-1988]: Read, S., 1988, *Relevant Logic*, Oxford: Blackwell. A very interesting and fun book. Idiosyncratic, but philosophically adept and excellent on the pre-history and early history of relevance logic.

[^restall-2000]: Restall, G., 2000, *An Introduction to Substructural Logics*, London: Routledge. Excellent and clear introduction to a field of logic that includes relevance logic.

[^rivenc-2005]: Rivenc, François, 2005, *Introduction à la logique pertinente*, Paris: Presses Universitaires de France. In French. Gives a “structural” interpretation of relevant logic, which is largely proof theoretic. The structures involved are structures of premises in a sequent calculus.

[^routley-1982]: Routley, R., R.K. Meyer, V. Plumwood and R. Brady, 1982, *Relevant Logics and its Rivals* (Volume I), Atascardero, CA: Ridgeview. A very useful book for formal results especially about the semantics of relevance logics. The introduction and philosophical remarks are full of “Richard Routleyisms”. They tend to be Routley’s views rather than the views of the other authors and are fairly radical even for relevant logicians. Volume II updates Volume I and includes other topics such as conditionals, quantification, and decision procedures: R.Brady (ed.), *Relevant Logics and their Rivals* (Volum II), Aldershot: Ashgate, 2003.

[^goldblatt-2011]: Goldblatt, R., 2011, *Quantifiers, Propositions and Identity: Admissible Semantics for Quantified Modal and Substructural Logics*, Cambridge: Cambridge University Press. A detailed account of the admissible semantics for quantified logic, applied to both modal and relevance logic, and provides a new type of semantics for quantified relevance logic called the “cover semantics”.

[^jago-2013]: Jago, M., 2013, “Recent Work in Relevant Logic,” *Analysis*, 73: 526–541. A very clear survey of recent technical and philosophical work in relevance logic.

[^anderson-1967]: Anderson, A.R., 1967, “Some Nasty Problems in the Formal Logic of Ethics,” *Noûs*, 1: 354–360.

[^avron-1990]: Avron, Arnon, 1990, “Relevance and Paraconsistency — A New Approach,” *The Journal of Symbolic Logic*, 55: 707–732.

[^bilková-2010]: Bilková, M., O. Majer, M. Peliš, and G. Restall, 2010, “Relevant Agents” in L. Beklemishev, V. Gorenko, and V. Shehtman (eds.), *Advances in Modal Logic* (Volume 8), London: College Publications, 22–38.

[^barwise-1993]: Barwise, J., 1993, “Constraints, Channels and the Flow of Information,” in P.Aczel, et al. (eds.), *Situation Theory and Its Applications* (Volume 3), Stanford: CSLI Publications, pp. 3–27.

[^belnap-1982]: Belnap, N.D., 1982, “Display Logic,” *Journal of Philosophical Logic*, 11: 375–417.

[^brady-1989]: Brady, R.T., 1989, “The Non-Triviality of Dialectical Set Theory,” in G. Priest, R. Routley and J. Norman (eds.), *Paraconsistent Logic*, Munich: Philosophia Verlag, pp. 437–470.

[^dunn-1973]: Dunn, J.M., 1973, (Abstract) “A ‘Gentzen System’ for Positive Relevant Implication,” *The Journal of Symbolic Logic*, 38: 356–357.

[^dunn-1993]: –––, 1993, “Star and Perp,” *Philosophical Perspectives*, 7: 331–357.

[^dunn-2015]: –––, 2015, “The Relevance of Relevance to Relevance Logic” in M. Banerjee and S.N. Krishna (eds.), *Logic and its Applications: 6th Indian Conference, ICLA 2015Mumbai, India, January 8–10, 2015Proceedings*, Basel: Springer, pp. 11–29.

[^ferguson-2017]: Ferguson, T.M., 2017, *Meaning and Proscription in Formal Logic*, Basel: Springer.

[^fine-1974]: Fine, K., 1974, “Models for Entailment,” *Journal of Philosophical Logic*, 3: 347–372.

[^fine-1986]: –––, 1986, “Analytic Implication” *Notre Dame Journal of Formal Logic*, 27: 169–179.

[^fine-1988a]: –––, 1988a, “Incompleteness for Quantified Relevance Logic” in Norman and Sylvan (eds.), 1988, pp. 205–225.

[^fine-1988b]: –––, 1988b, “Semantics for Quantified Relevance Logic” *Journal of Philosophical Logic*, 17: 27–59.

[^fuhrmann-1990]: Fuhrmann, A., 1990, “Models for Relevant Modal Logics,” *Studia Logica*, 49: 501–514.

[^goble-1999]: Goble, L., 1999, “Deontic Logic with Relevance” in P. McNamara and H. Prakken (eds.), *Norms, Logis and Information Systems*, Amsterdam: ISO Press, pp. 331–346.

[^grishin-1974]: Grishin, V.N., 1974, “A Non-Standard Logic and its Application to Set Theory,” *Studies in Formalized Languages and Non-Classical Logics* (Russian), Moscow: Nauka.

[^israel-1990]: Israel, D. and J. Perry, 1990, “What is Information?,” in P.P. Hanson (ed.), *Information, Language, and Cognition*, Vancouver: University of British Columbia Press, pp. 1–19.

[^logan-2019]: Logan, S.A., 2019, “Notes on Stratified Semantics” *Journal of Philosophical Logic*, 48: 479–486.

[^maccoll-1908]: MacColl, H., 1908, “‘If’ and ‘imply’,” *Mind*, 17: 151–152, 453–455.

[^mares-1992]: Mares, E.D., 1992, “Andersonian Deontic Logic,” *Theoria*, 58: 3–20.

[^mares-1997]: –––, 1997, “Relevant Logic and the Theory of Information,” *Synthese*, 109: 345–360.

[^mares-2004a]: –––, 2004a, ““Four-Valued” Semantics for the Relevant Logic R” *Journal of Philosophical Logic*, 33: 327–341.

[^mares-1995]: Mares, E.D. and A. Fuhrmann, 1995, “A Relevant Theory of Conditionals,” *Journal of Philosophical Logic*, 24: 645–665.

[^mares-2006]: Mares, E.D. and R. Goldblatt, 2006, “An Alternative Semantics for Quantified Relevant Logic” *The Journal of Symbolic Logic*, 71: 163–187.

[^meyer-1992]: Meyer, R.K. and H. Friedman, 1992, “Whither Relevant Arithmetic?,” *The Journal of Symbolic Logic*, 57: 824–831.

[^omori-2017]: Omori, H. and H. Wansing (eds.), 2017, “40 years of FDE: An Introductory Overview” *Studia Logica*, 105: 1021–1049.

[^punčochář-2020]: Punčochář, V., 2020, “A Relevant Logic of Questions” *Journal of Philosophical Logic*, 49: 905–939. doi:10.1007/s10992-019-09541-9

[^rantala-1982]: Rantala, V., 1982, “Quantified Modal Logic: Non-Normal Worlds and Propositional Attitudes,” *Studia Logica*, 41: 41–65.

[^restall-1995]: Restall, G., 1995, “Four-Valued Semantics for Relevant Logics (and Some of their Rivals)” *Journal of Philosophical Logic*, 24: 139–160.

[^restall-1996]: –––, 1996, “Information Flow and Relevant Logics,” in J. Seligman and D. Westerstahl (eds.), *Logic, Language and Computation* (Volume 1), Stanford: CSLI Publications, pp. 463–478.

[^routely-1972]: Routely, R., and V. Routley, 1972, “The Semantics of First Degree Entailment,” *Noûs*, 6(4): 335–369.

[^routely-1980]: Routely, R., 1980, “Problems and Solutions in the Semantics of Quantified Relevant Logics, I” in A.I. Arruda, R. Chuaqui, N.C.A. Da Costa (eds.), *Mathematical Logic in Latin America* Amsterdam: North Holland, 1980, pp. 309–340.

[^routley-1978]: Routley, R. and A. Loparic, 1978, “Semantical Analysis of Arruda-da Costa P Systems and Adjacent Non-Replacement Relevant Systems,” *Studia Logica*, 37: 301–322.

[^sperber-2002]: Sperber, D. and D. Wilson, 2002, “Relevance Theory” in L. Horn & G. Ward (eds.), *The Handbook of Pragmatics*, Oxford: Blackwell, pp. 607–632.

[^standefer-2019]: Standefer, S., 2019, “Tracking Reasons with Extensions of Relevant Logics” *Logic Journal of the IGPL*, 27: 543–569.

[^tennant-2017]: Tennant, Neil., 2017, *Core Logic*, Oxford: Oxford University Press.

[^troelstra-1992]: Troelstra, A.S., 1992, *Lectures on Linear Logic*, Stanford: CSLI Publications.

[^urquhart-1972]: Urquhart, A., 1972, “Semantics for Relevant Logics” *The Journal of Symbolic Logic*, 37: 159–169.

[^wansing-2001]: Wansing, H., 2001, “Negation,” in L. Goble (ed.), *The Blackwell Guide to Philosophical Logic*, Oxford: Blackwell, pp. 415–436.

[^wansing-2002]: –––, 2002, “Diamonds are a Philosopher’s Best Friends,” *Journal of Philosophical Logic*, 31: 591–612.

[^weber-2010]: Weber, Z., 2010, “Extensionality and Restriction in Naive Set Theory” *Studia Logica*, 94: 87–104.
