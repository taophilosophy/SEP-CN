# intuition — supplement（supplement）

> （《intuition》词条补充材料，源：plato.stanford.edu/entries/intuition/supplement.html）

#### Supplement to Intuition

## The Logical Structure of the Method of Cases

If one considers the four examples of the method of cases in §2.2, it may seem that their logical structure is clear. One begins with a candidate generalization, theory, or analysis which is put in terms of a necessary bi-conditional. Then, by appeal to a hypothetical case, one justifies the claim that it is possible for the *analysandum* property to be absent though the properties alleged by the analysis to be sufficient are present or one justifies the claim it is possible for the *analysandum* property to be present though some property alleged by the analysis to be necessary is lacking.

As this sketch would have it, the proposition which entails the falsity of the analysis in question is justified in some manner by the content of an intuition. However, Williamson (2007) argues, in connection with the Gettier intuition, that difficulties are revealed by considering how to formalize the implicit argument. In particular, as a hypothetical case is being described, one may wonder about the precise content of the allegedly refuting intuition. After all, the scenario contemplated is not believed to be actual. In light of the traditional rationalist’s view that intuition reveals necessary truths, consider a regimentation on which the central intuition has as its content a claim about necessity:

| $\mathrm{K}(x, p)$: | *x* knows that *p*. |
| --- | --- |
| $\textrm{JTB}(x, p)$: | *x* has a justified true belief that *p*. |
| $\textrm{GC}(x, p)$: | *x* stands to *p* as in the Gettier text. |

**(1)**

$\Diamond \exists x\exists p\textrm{GC}(x, p)$

**(2)**

$\Box \forall x\forall p (\textrm{GC}(x, p) \supset (\textrm{JTB}(x, p) \amp{\sim}\mathrm{K}(x, p)))$

Therefore,

**(3)**

$\Diamond \exists x\exists p (\textrm{JTB}(x, p) \amp{\sim}\mathrm{K}(x, p))$

(3) contradicts the JTB theory, construed as

$$\Box \forall x\forall p (\textrm{JTB}(x, p) = \mathrm{K}(x, p)).$$

The problem with this account, as Williamson points out, is that (2) is false because the relation $\textrm{GC}(x, p)$ is, in virtue of the incompleteness of Gettier’s description, one which may be instantiated in a variety of ways. Some of those possible instantiations are cases in which the subject lacks justified true belief which is not knowledge. One, for example, is a case in which *x* has further evidence which undermines the justification of *x*’s belief that *p* and renders false the claim that *S*’s belief is justified. Another involves further independent evidence for *p* or some other fact which renders false the claim that *S*’s belief that *p* is not knowledge.

Williamson’s own response to this worry is to weaken (2) to a counterfactual claim, yielding the following:

**(1)**

$\Diamond \exists x\exists p\,\textrm{GC}(x, p)$

**(2c)**

$\exists x\exists p\,\textrm{GC}(x, p) \boxright \forall x\forall p (\textrm{GC}(x, p) \supset (\textrm{JTB}(x, p) \amp{\sim}\mathrm{K}(x, p)))$

Therefore,

**(3)**

$\Diamond \exists x\exists p (\textrm{JTB}(x, p) \amp{\sim}\mathrm{K}(x, p))$

(Williamson admits (2007: 195–6) that (2c) is not a completely adequate formalization of the anaphora in the ordinary language subjunctive he seeks to capture—“If a thinker were to stand to a proposition as in the Gettier text, he/she would have justified belief in it without knowledge.”)

This account of the second premise of the argument has been alleged to be problematic (Ichikawa and Jarvis 2009; Malmgren 2011). First, the counterfactual it features is a contingent truth, justified, if at all, on *a posteriori* grounds. Hence, a typical philosophical appeal to intuition yields, surprisingly, an *a posteriori* conclusion. Second, the premise is false if the actual world (or nearest possible one) contains a confounding realization of the Gettier story—a realization in which the subject has knowledge that *p* or lacks justification for believing that *p*. If so, then Gettier’s case is not really a counterexample to the JTB theory. Third, we are not in a position to rule out such confounding realizations with assurance. Hence, we seem substantially less justified than we normally take ourselves to be in thinking that Gettier provided a counterexample the JTB theory.

Geddes (2018) provides an related reconstruction which may ameliorate the second and third difficulties just raised for Williamson’s account. On his reconstruction, the informal counterfactual conditional formalized in (2c) is modified so as to hold that if someone were to stand to a proposition *p* as in the Gettier case, then, “*normally*, he would have a justified true belief that *p* but not know that *p*.” While providing no formal semantics for this conditional, Geddes suggests that we understand it adequately and that it is (1) true and inconsistent with the JTB theory and, (2) not falsified if there is an actual or close Gettier case in which the agent knows that *p* or is not justified in believing *p*. Still, the claim appears plausibly *a posteriori* and contingent.

A third solution (Williamson 2007: 202), is to weaken (2c) to:

**(2pc)**

$\Diamond(\exists x\exists p\, \textrm{GC}(x, p) \boxright \forall x\forall p (\textrm{GC}(x, p) \supset (\textrm{JTB}(x, p) \amp{\sim}\mathrm{K}(x, p)))).$

(2pc) would avoid the concerns noted above about (2c) and Williamson allows that S5 would enable us to deduce (3) from (1) and (2pc). Still, he rejects this reconstruction because it requires, unlike the argument from (1) and (2c), (a) the correctness of the relevant principles of S5 and (b) the attribution of a commitment to such principles to people who have never considered them.

A fourth solution, defended by Ichikawa and Jarvis (2009), appeals to the distinction between what is *explicitly stated in* the text of a fictional story and what is *true in* the fiction. While Williamson’s worry gains its purchase from the fact that a fictional *text* can be consistently “filled out” in different ways, the alleged fact that many fictional truths are not explicitly stated in a fictional text provides a way of endeavoring to block the worry. For example, it allows one to claim that it is true in the Gettier story (though not explicitly stated in the Gettier text) that the subject does not have further evidence or knowledge which would undermine her justification. Letting the set of propositions *true in* Gettier’s fiction be named “SET,” a person may, upon encountering Gettier’s text, consider the proposition, *g*, that every proposition in SET is true. Ichikawa and Jarvis allege that this is possible even though one has not entertained in *propia persona* each of the propositions in SET because the content is in some way demonstrative—things are like *that*. Then (setting aside worries about fictional proper names) the Gettier reasoning might be formalized as follows:

**(1f)**

$\Diamond g$

**(2f)**

$\Box(g \supset \exists x\exists p (\textrm{JTB}(x, p) \amp{\sim}\mathrm{K}(x, p)))$

Therefore,

**(3)**

$\exists x\exists p (\textrm{JTB}(x, p) \amp{\sim}\mathrm{K}(x, p))$

One worry about this account is that statements about fictional truth are, on the most influential account (Lewis 1978), analyzed in counterfactual terms. On such a view, which set of propositions constitutes the set to which a given agent is related by encountering a fictional text depends on contingent facts about what their world is like. Hence, as Williamson (2009: 466) points out, contingencies can prevent one from knowing the truth of the relevant instance of (2f), even if one has encountered and understood the Gettier text. (See Malmgren 2011 for further objections to this proposal and to other attempts to rescue (2) by changing its embedded proposition.)

A fifth solution, which also holds that the second premise of the reconstruction invokes a strict implication, is provided by Grundmann and Horvath (2014a, 2014b; Horvath 2023). They suggest that the Gettier case can be enriched with sufficient facts about *S*’s justification for believing *p* to rule out the intuitively deviant realizations (those which fail to involve justified true belief which is not knowledge). One benefit of the proposal is that it makes the Gettier intuition independent of contingent facts about the actual world. However, it seems quite uncertain that a similar move can be provided to rule out deviant realizations of other thought experiment cases. Moreover, the psychological means by which those who consider Gettier’s limited textual description arrive at the much enriched content required by this proposal, and the manner of their grasping this enriched content, remains unclear. Some of these issues may be resolved by Saint-Germier’s 2021 proposal that the enriched content is generated through various generalized pragmatic implicatures.

A sixth solution (Malmgren 2011) holds that the Gettier premise is the simple claim that it is possible that some *x* stand to some *p* as does the subject in the Gettier text and to have justified true belief that *p* while lacking knowledge that *p*. More precisely, it is

(1*)

$\Diamond \exists x\exists p (\textrm{GC}(x, p) \amp \textrm{JTB}(x, p) \amp{\sim}\mathrm{K}(x, p))$

(1*) entails, without the aid of other premises, (3). That there are possible realizations of the Gettier text in which the person would fail to have JTB but not knowledge is irrelevant to the truth of (1*).

It might be objected that this proposal makes the intuition’s content too close to a simple denial of the JTB theory. However, this worry can be assuaged if one recalls that the JTB theory has little or no intuitive justification of its own and was justifiably accepted by its proponents only on the grounds that it provided the best account of our pre-Gettier intuitions. Geddes (2018) raises worries about how Malmgren’s proposal handles cases in which people deny the Gettier claim. Malmgren’s proposal seems to imply that one who holds that Gettier’s subject neither has a justified true belief, nor knows, that *p*, is holding that it is possible that *S* stand to a proposition *p* as in the Gettier case and that *S* fail to have justified belief or knowledge that *p*. That claim, however, is true and does not contradict the orthodox claim about the Gettier case. Ichikawa and Jarvis (2013) object to Malmgren’s account that one might reject the standard claim about the Gettier case but still accept (1*) because one thinks there are other possible cases of JTB without knowledge which are compossible with the Gettier case.

Much of the relevant literature appears to assume that Williamson’s worry will arise for any appeal to a hypothetical case. Williamson himself adopts

> the background working hypothesis … that [Gettier’s] thought experiments are paradigmatic, in the sense that if any thought experiments can succeed in philosophy, his do: thus to determine whether Gettier’s thought experiments succeed is in effect to determine whether there can be successful thought experiments in philosophy. (2007: 179–180)

However, there may be cases in which the relevant second premise is not, even formalized as a necessary universal quantification, open to Williamson’s worry. Consider, as one example, the standard New Evil Demon case, in which we are to suppose that there are persons who have (and have always had) internal mental lives exactly like our own but who are radically deceived by an evil demon (Cohen 1984). The intuition that they are justified in believing as they do is taken to refute a crude form of reliabilism. Here, the ambitious reading of (2) appears to go through:

| $\mathrm{J}(x, p)$: | *x* is justified in believing *p*. |
| --- | --- |
| $\textrm{ED}(x, p)$: | *x* stands to *p* as in the Evil Demon story. |
| $\textrm{R}(x, p)$: | *x*’s belief that *p* is reliably produced. |

**(1)**

$\Diamond \exists x\exists p\, \textrm{ED} (x, p)$

**(2)**

$\Box \forall x\forall p\,\textrm{ED}(x, p) \supset (\mathrm{J}(x, p) \amp{\sim}\mathrm{R}(x, p)))$

Therefore,

**(3)**

$\Diamond \exists x\exists p (\textrm{J}(x, p) \amp{\sim}\textrm{R}(x, p))$

(3) contradicts a reliabilist theory of justified belief according to which $\Box \forall x\forall p (\mathrm{J}(x, p) = \mathrm{R}(x, p))$.
