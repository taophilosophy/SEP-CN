# Medieval Theories of Consequence
**First published Mon Jun 11, 2012; substantive revision Mon Oct 21, 2024**

*Dutilh Novaes, Catarina, Crimi, Milo*

Latin medieval theories of consequence are systematic analyses by Latin medieval authors[^note-1] of the logical relations between sentences[^note-2], in particular the notions of entailment and valid inference, but also the semantics of conditionals. When does a sentence B follow from a sentence A? (For example, from ‘Every human is an animal’ one may infer ‘Some animal is a human’.) What are the grounds for the relation of entailment/consequence? Are there different kinds of consequences? These and other questions were extensively debated by these authors.

Theories of consequence explicitly acquired an autonomous status only in the 14ᵗʰ century, when treatises specifically on the concept of consequence began to appear; but some earlier investigations also deserve the general title of ‘theories of consequence’, in view of their scope, sophistication and systematicity. Taken as a whole, medieval theories of consequence represent the first sustained attempt at adopting a sentential/propositional perspective[^note-3] since the Stoics in Greek antiquity, and — unlike Stoic logic, which had little historical influence — provide the historical background for subsequent developments leading to the birth of modern logic in the 19ᵗʰ century. Indeed, it may be argued that the medieval concept of *consequentia* (in its different versions) is the main precursor of the modern concept of logical consequence.

## 1. Preliminary Considerations

### 1.1 A genealogy of modern conceptions of consequence

In his much-discussed 1936 paper ‘On the concept of logical consequence’, Tarski presents two criteria of material adequacy for formal accounts of logical consequence, which jointly capture the ‘common notion’ of logical consequence (or so he claims) (Tarski 2002, §2.3)[^tarski-2002]. They can be formulated as:

**(TP)**

*necessary truth-preservation*: it is impossible for the antecedent to be true while the consequent is not true;

**(ST)**

*substitution of terms*: the relation of consequence is preserved under any (suitable) substitution of the non-logical terms of the sentences in question; this is now often referred to as the *formality criterion*.

Different accounts of logical consequence can be (and have been) formulated on the basis of (TP) and/or (ST): they can be viewed as both necessary but independent components of the notion of logical consequence, as Tarski seems to suggest in the passage above; they can also be viewed as closely related, in particular if (TP) can be *reduced* to (ST) (i.e. satisfaction of (ST) would entail satisfaction of (TP) and vice-versa) — a view that Etchemendy (1990) attributes to Tarski; or one may hold that the actual core of the notion of (logical) consequence is (TP), and that (ST) simply specifies a particular subclass of valid consequences, often referred to as *formal consequences* (Read 1994)[^read-1994].

Tarski correctly identified these two features as key components of the notion of logical consequence as entertained by philosophers and mathematicians of his time (and also today). But the question arises: why these two features and not others? In particular, through which (historical) processes have they come to constitute the conceptual core of the notion of logical consequence? These questions are even more pressing in view of the fact that both features have been challenged as correct renditions of the conceptual core of logical consequence — Etchemendy (1990) challenged the centrality of formality and (ST); Fields (2008) challenged the centrality of necessary truth-preservation in view of the semantic paradoxes.

To make further progress in these debates, an important element is arguably the historical development of the notion of (logical) consequence over the centuries, so that we may come to understand where the informal notion(s) of logical consequence come(s) from. Engaging in an exercise of ‘conceptual history’ may allow for a better grasp of the reasons why this notion (now widely endorsed) established itself as such in the first place. If these are compelling reasons, then they may count as arguments in favor of the centrality of formality and necessary truth-preservation; but if they rest on disputable, contentious assumptions, then the analysis may provide elements for a critical evaluation of each of these two components as truly constitutive of the concept of logical consequence.

From this point of view, the historical developments in the Latin Middle Ages, in particular from the 12ᵗʰ to the 14ᵗʰ century, occupy a prominent position. As will be argued, it is in this period that concepts and ideas inherited from Greek Antiquity (Aristotle in particular, but also the ancient commentators) were shaped and consolidated into conceptions of consequence that bear a remarkable resemblance to the Tarskian condition of material adequacy presented above. Thus, an analysis of these historical developments is likely to contribute significantly to our understanding of the current notion(s) of logical consequence.

Besides variations of (TP) and (ST), criteria of relevance, containment, causation and explanatoriness also appear frequently in the writings of medieval authors (as well as earlier authors). As Normore (2015, 357) puts it, there seems to be

> a pervasive ambiguity of terms like ‘ergo’ and ‘igitur’ in Latin, ‘therefore’ in English, and similar particles in other European languages between a broadly truth-preserving and a broadly causal/explanatory sense.

This ambiguity is reflected in the different core conceptions of consequence throughout the history of logic: is necessary truth preservation sufficient, or do we require something else, namely a deeper causal (and/or epistemic) connection between antecedent and consequent for the consequence to hold? Indeed, in addition to variations of (TP) and (ST), there is a third recurrent theme in medieval discussions on consequence:

**(Co)**

*containment*: in a valid consequence, the conclusion is contained/understood in the premises.

Different interpretations of this clause run through medieval discussions on consequence, ranging from the 12th to the 15th century and beyond. A number of authors seem to treat the notion of containment in metaphysical and/or semantic terms, while others (in particular the British authors of the second half of the 14th century) lean more heavily towards what appears to be an epistemic interpretation (see section 3.4). And just as (TP) and (ST) still very much inform how most of us think about (logical) consequence, variations of the containment theme, as captured in (Co), remain pervasive among contemporary authors, motivating for example the development of a number of relevance logics (see entry on relevance logic in this encyclopedia). However, notice that (Co) is also interpreted metaphysically by a number of medieval authors; this metaphysical focus is not nearly as present among contemporary philosophers and logicians (with the exception perhaps of some of the recent discussions on the concept of grounding).

Naturally, as with any historical analysis, an investigation of these developments has intrinsic historical value in and of itself, independently of its possible contribution to modern debates. Indeed, medieval theories of consequence are a genuine medieval contribution: while medieval authors are clearly taking ancient Greek sources and ideas as their starting point, the emergence of theories of consequence as such is a Latin medieval innovation. But as it turns out, following the thread provided by the three key notions (TP), (ST) and (Co) as formulated above provides a suitable vantage point to investigate the development of the notion of consequence in the Latin Middle Ages. In other words, historical and conceptual analysis can easily be combined in this case.

### 1.2 What are medieval theories of consequence theories *of*?

At first sight, it is not immediately clear what the object of analysis of medieval theories of consequence is (Boh 1982)[^boh-1982]. Is it the semantics of conditional sentences? Is it the validity of inferences and arguments? Is it the relation of consequence, construed as an abstract entity? In fact, at times it seems that medieval authors do not properly distinguish between these different notions. After all, these are very different concepts: a conditional is a sentence, which can be true or false; an argument or inference is an act, a consecution of assertions, which can be valid or invalid; a consequence is a relation between sentential/propositional entities, which can hold or fail to hold (Sundholm 1998)[^sundholm-1998].

However, even though the medieval authors may use the same terminology to refer to these different concepts, this does not mean that they are not aware of the relevant differences, in particular between a conditional and a consequence (Normore 2015)[^normore-2015]. As Buridan (*Tractatus de Consequentiis* (henceforth TC), 21) remarks, it is for the most part a matter of terminology: he says he will adopt the definition of consequence as a true hypothetical sentence, but then throughout his text also uses the terminology of a consequence being valid or holding rather than simply being true or false. At any rate, it seems fair to say that, even though analyses of conditionals are often in the background (as is especially obvious in Boethius and Abelard with examples such as ‘if it is a human, it is an animal’, and in analyses of the syncategorematic term ‘*si*’, ‘if’ (Spruyt 2018)[^spruyt-2018]), a main focus of medieval theories of consequence tends to be the logical relations between sentential/propositional components (King 2001; Read 2010)[^king-2001][^read-2010], essentially (though not entirely) in the spirit of modern accounts of the notion of logical consequence (Shapiro 2005)[^shapiro-2005] (Caret and Hjortland 2015)[^caret-2015]. Some modern scholars (e.g. Spade in his translation of Burley’s *De Puritate*; Read 2010)[^read-2010] prefer to translate the medieval term ‘*consequentia*’ as ‘inference’, but arguably ‘consequence’ is a more appropriate translation, both for etymological and for conceptual reasons.

One may also wonder to what extent medieval theories of consequence really add anything novel to the Aristotelian logical legacy. Kant (in)famously claimed that Aristotle had discovered everything there was to know about logic, and insofar as they deal with logical relations between sentences, it might be thought that theories of consequence would not have added anything substantially new to Aristotle’s theory of syllogistic in particular. In fact, the relations between theories of syllogistic and theories of consequence at different times seem essentially to fall within one of three categories:

1. Syllogistic and consequence are essentially disjoint concepts, each having their own foundations and scope. In such cases, the framework of Aristotle’s *Topics* is often (though not always) summoned to provide the foundations for non-syllogistic arguments/consequences.
2. All valid arguments, including non-syllogistic ones, are ultimately to be reduced to syllogistic arguments, as syllogistic offers the grounds for the validity of every single valid argument. A proponent of this approach is the 13ᵗʰ-century author Robert Kilwardby.
3. Theories of consequence are seen as an expansion and generalization of syllogistic; syllogistic is a special case of consequence. In these cases, syllogistic is absorbed by consequence, which is a more general framework in that it can deal with a much wider range of inferences (Klima 2016)[^klima-2016]. The 14ᵗʰ-century author John Buridan, for example, treats extensively of syllogisms, both assertoric and modal, in his treatise on consequence.

It is fair to say that approach 3 became predominant in the 14ᵗʰ century, the golden age of medieval theories of consequence; but the earlier Boethian view that all valid arguments (including syllogistic arguments) are valid in virtue of topical rules can also be seen as belonging to category 3. However, given that medieval theories of syllogistic are treated extensively elsewhere (see the entry on medieval theories of the syllogism of this encyclopedia), in what follows we shall focus on non-syllogistic consequences/arguments, but with the proviso that many of the interesting developments in syllogistic in the 14ᵗʰ century are presented in treatises or chapters on consequence.

Another point worth mentioning is the fact that medieval discussions of the concept of consequence cover both what we would now describe as ‘philosophy of logic’ and as ‘logic proper’. As for the latter, a number of medieval authors such as Abelard (Martin 2004)[^martin-2004], Burley (*De Puritate*), and Buridan (TC) formulated rules of inference and proved theorems about them (Klima 2016)[^klima-2016]. Many authors had for the most part understood the logical behavior of what we now view as the main sentential/propositional operators, such as ‘if…then’, ‘or’, negating terms, as well as meta-level rules such as the transitivity of consequence, ‘from the impossible anything follows’, or ‘the necessary follows from anything’ (the latter two were however not unanimously endorsed — see Martin 1986, Read 1993, 2010)[^martin-1986][^read-1993][^read-2010]. (For discussions of the rules formulated by different authors, see Pozzi 1978, Boh 2001, Dutilh Novaes 2008)[^boh-2001][^dutilh-2008][^pozzi-1978]. They also offered sophisticated investigations of the logical behavior of e.g. modal terms (Buridan, TC, Johnston 2014)[^johnston-2014].

Besides this more technical layer, medieval authors also discussed extensively the very nature of the notion of consequence: what counts as appropriate grounds for a valid consequence, adequate definitions, subdivisions of kinds of consequence etc. In what follows, the predominant focus will be on the ‘philosophy of logic’ side of medieval theories of consequence, i.e. how they articulated this very notion, rather than on spelling out the exact inferential rules endorsed by the different authors. But some medieval treatises on consequence also contain a high level of technical sophistication, even though the language used is the regimented academic Latin of the time – the only symbolic device present is the use of schematic letters, which in fact dates back to Aristotle.

## 2. Early Theories of Consequence

### 2.1 Precursors

One of the most important ancient sources for the development of theories of consequence by medieval authors is, unsurprisingly, Aristotle. The *Prior Analytics* and the theory of syllogistic provided the main model for the correctness/validity of arguments for centuries, and even though theories of consequences can be seen as a generalization of the rather narrow theory of validity presented in the *Prior Analytics*, it is clear that syllogistic remains one of the key elements in the background. Indeed, the famous definition of a valid deduction (syllogism) at the beginning of the *Prior Analytics* is already a formulation of the necessary truth-preservation criterion (TP):

> A deduction is a discourse in which, certain things being stated, something other than what is stated follows of necessity from their being so. (24ᵇ19–20)

Retracing the historical sources for the development of this notion would take us too far afield, but it seems that the emergence of the idea of ‘following of necessity’ is closely related to dialectical practices of debates (Dutilh Novaes 2021)[^dutilh-2021], both in philosophy/logic (Castelnérac and Marion 2009)[^castelnérac-2009] and in mathematics (Netz 1999)[^netz-1999]. But while it is a necessary condition, necessary truth-preservation is notoriously not a sufficient condition for syllogistic validity. For example, as is well known, Aristotle’s syllogistic does not validate the principle of reflexivity, i.e., ‘A implies A’ for any sentence A, even though this principle is the most transparent occurrence of necessary truth-preservation one can think of. Instead, it seems that syllogistic validity requires a great deal more to hold (Thom 2010)[^thom-2010] (Thom 2016)[^thom-2016]. Interestingly, Aristotle himself suggests that the premises in a syllogism are the material causes for the conclusion (*Metaphysics* 1013b19–20; *Physics* 195a18–19), “in the sense of ‘that from which’”, thus somewhat in the spirit of the idea of premises containing the conclusion expressed in (Co), and more generally the idea that the antecedent is the cause of the consequent (which would become widespread in the 13th century (Spruyt 2018)[^spruyt-2018]). Indeed, it has been claimed that

> Ancient logics were all in some sense relevance logics. They insisted that for an argument to be valid, conditions must be met that guaranteed both that it would be impossible for the premises to be true and the conclusion false and that there would be connections of various kinds between the premises and conclusions. (Normore 1993, 448)[^normore-1993]

Indeed, besides variations of (TP) and (ST), criteria of causation, relevance and containment also appear frequently in the writings of medieval authors.

The extent to which (ST) is present in the *Prior Analytics* is also a moot point (Thom 2010, Dutilh Novaes 2021)[^dutilh-2021][^thom-2010]. Aristotle does not apply the concepts of form and matter anywhere in his logical writings, but his consistent use of schematic letters and many of his argumentative strategies in this work suggest that he relies on something resembling what we now refer to as the ‘logical form’ of arguments. What is not clear is whether Aristotle relies on (ST) merely as a convenient technical device to capture the more fundamental property of necessary truth-preservation, or whether for him (TP) and (ST) are independent core components of the concept of a syllogism/deduction (or perhaps even that (TP) is to be reduced to (ST)).

The *Prior Analytics* is not the only Aristotelian text providing the historical background for the development of the notion of consequence. Equally important is one of his (presumably) ‘older’ logical texts, the *Topics*; this text, which even more explicitly than the *Analytics* clearly presupposes a dialectical background, presents various considerations on how to argue well in dialectical encounters (see the entry on ancient logic of this encyclopedia, section 2.1). By discussing which moves are allowed in a debate, it naturally ends up addressing the general idea of ‘what follows from what’ (Dutilh Novaes 2021)[^dutilh-2021]. As we will see, the *Topics* became an important starting point for discussions on the validity of arguments; the theory of syllogistic only covers a rather limited range of arguments (two-premised arguments containing only the four kinds of categorical sentences), and the framework of the *Topics* was often called upon to fill in the gap between what syllogistic had to offer and the much larger range of putatively valid arguments one might be interested in Klima 2016.

Two other ancient traditions which may have contributed to the development of medieval theories of consequence are the Stoic tradition (see the entry on ancient logic of this encyclopedia, section 5) and the tradition of the ancient commentators (Barnes 1990, 2008; entry on the ancient commentators of this encyclopedia)[^barnes-1990]. But in fact, while a Stoic connection is prima facie plausible — unlike Aristotelian term-based logic, Stoic logic is also largely sentence-based — historical evidence for direct Stoic influence remains elusive; for now, no record of actual channels of influence has been identified.[^note-4] The ancient commentators, by contrast, had significant (both indirect and direct) impact on the development of the notion of consequence — at first via Boethius, later via the Arabic authors, and as their commentaries were translated and read by the Latin authors in the 13ᵗʰ century and onwards.

While the notion of necessary truth-preservation was already quite mature in the *Prior Analytics*, the conceptual development of the substitutivity criterion is essentially a later contribution of the ancient commentators (Barnes 1990, 2008; Dutilh Novaes 2012a)[^barnes-1990][^dutilh-2012a]. Recall that Aristotle had not applied the metaphysical notions of form and matter to logical objects such as sentences and arguments in any systematic way; this crucial step was undertaken by the ancient commentators. References to the form and matter of syllogisms are pervasive in their writings, especially in commentaries on the *Prior Analytics*, from that of Alexander of Aphrodisias (2ⁿᵈ century AD) up to that of Ammonius (6ᵗʰ century AD). The ancient commentators not only distinguished between the form and the matter of syllogisms: they sometimes also suggested (though usually rather obliquely) that the form of an argument is precisely that in virtue of which it is valid and reliable. This would later pave the way for the distinction between formal and material consequences and the idea of validity in virtue of form. Here is an illustrative passage by Alexander of Aphrodisias:

> Combinations are called syllogistic and reliable if they do not alter together with differences in the matter — i.e. if they do not deduce and prove different things at different times, but always and in every material instance preserve one and the same form in the conclusion. Combinations which change and alter configuration together with the matter and acquire different and conflicting conclusions at different times, are non-syllogistic and unreliable. (Alexander of Aphrodisias, *in Apr* 52.20–24, 114)

Alexander also comments on Aristotle’s use of schematic letters, and clearly relates what takes the place of schematic letters to the *matter* of the argument:

> He uses letters in his exposition in order to indicate to us that the conclusions do not depend on the matter but on the figure, on the conjunction of the premises and on the moods. For so-and-so is deduced syllogistically not because the matter is of such-and-such a kind but because the combination is so-and-so. The letters, then, show that the conclusion will be such-and-such universally, always, and for every assumption. (Alexander of Aphrodisias, *in Apr* 53.28–54.2, 116)

In first instance, the Greek logical heritage was almost single-handedly (though selectively) passed on to the Latin tradition by one man, the neo-platonic philosopher Boethius. Prior to the late 12ᵗʰ century (Aristotle’s and other ancient texts became widely read again in the Christian parts of Europe only in the 12ᵗʰ century — see Dod 1982)[^dod-1982], what the medieval authors had inherited from Greek logic had been almost exclusively transmitted by Boethius, who had also established the logical terminology in Latin. His translations of Aristotle’s *Categories* and *De Interpretatione* were widely read, as well as his textbooks on syllogistic and his two texts *De hypotheticis syllogismis* (*On Hypothetical Syllogisms* – HS) (dating 516–522) and *De topicis differentiis* (*On Topical differentiae* — TD) (dating 522–523).

Boethius uses the term ‘*consequentia*’ to refer to that which a hypothetical sentence such as ‘If it’s day, then it’s light’ signifies:

> For it [the sentence] does not propose that it’s day and it’s light, but rather that if it’s day, then it’s light. Whence it signifies a certain consequence (*consequentia*) and not the being [of things]. (Boethius, *Commentary on ‘On Interpretation’* 2, 109–10, translation in Martin 2009, 67.)[^martin-2009][^note-5]

It is from Boethius that later authors inherited the term ‘*consequentia*’, but the influence of Boethius is not only terminological. In HS, he focuses on conditionals of the form “If something’s (not) *A*, then it’s (not) *B*” (*si* (*non*) *est* A, (*non*) *est* B), and lists a number of principles and rules governing the logical behavior of such sentences (Martin 2009, 66–78)[^martin-2009]. Boethius’ considerations are not sufficiently worked-out as to be viewed as a full-fledged ‘theory of consequence’, and indeed there are a number of tensions and inconsistencies in his doctrines. But HS will prove to be an important source for the later development of theories of consequence. For example, in this text Boethius introduces the distinction between natural and accidental consequences, which then remains the main subdivision of consequences up until the beginning of 14ᵗʰ century (when it is surpassed by the distinction between formal and material consequences) (Martin 2018, Archambault 2018a)[^archambault-2018a][^martin-2018]. For Boethius, both kinds of consequences, natural and accidental, entail inseparability, roughly meaning that the antecedent cannot be true while the consequent is false (i.e. a version of (TP)), but natural consequences entail something more, namely a real causal, metaphysical connection between the items in question.

The other text mentioned above, *De topicis differentiis*, is equally significant for the development of later theories of consequence. It presents a discussion of Cicero’s *Topics*, which in turn claims to have been inspired by Aristotle’s *Topics*. Cicero’s work, however, is very different from Aristotle’s, and Boethius in some sense attempts to offer a unification of both approaches (he also discusses the dialectical topics of the Greek commentator Themistius). One of the key concepts introduced by this text is the concept of ‘maximal propositions’, which he claims are the general principles underlying the correctness of topical arguments. As described by C. Martin,

> Such [maximal] propositions may either appear as a premise in a categorical syllogism or, much more importantly for the history of logic, as the warrant for an inference. In this second case they are the generalizations of the consequential relation which may hold between the premises and conclusion of an enthymeme or the antecedent and the conclusion of a conditional proposition. (Martin 2009, 79)[^martin-2009]

Crucially, topical arguments were originally seen as merely probable, contrasting with the necessary truth-preservation of syllogisms. So for maximal propositions to serve as grounds for the relation of consequence, a transformation on the status of topical arguments (from probable to necessary) had to occur at a later stage (Stump 1982, 290)[^stump-1982]. Moreover, it is important to notice that, although Boethius is familiar with the work of the Greek ancient commentators and incorporates some elements from their discussions, he does not explicitly apply the form vs. matter distinction to syllogisms, as the earlier authors had done. Barnes (1990) suggests that the logical hylomorphism (i.e. the application of Aristotle’s doctrine of form and matter to logic) of these authors is nevertheless present in Boethius’ terminology, such as in the opposition between *propositionum complexio* and *rerum natura* (the structure of a sentence vs. the nature of things) (e.g. HS II ii 5). But Boethius does not present the idea of substitution/variation of terms as a property related to the validity of arguments, as Alexander of Aphrodisias had suggested. In other words, substitutivity of terms as captured by (ST) is not a key element of Boethius’ account of validity — neither terminologically nor conceptually.

It has also been suggested that Boethius was the first to formulate a version of (Co) with respect to consequences (Green-Pedersen 1984)[^green-pedersen-1984]. However, on closer inspection, Boethius’ notion of containment is not really used to define or describe the relation between the antecedent and the consequent of a consequence (Bosman 2018)[^bosman-2018]. Instead, the Boethian relation of containment in question seems to pertain primarily to metaphysical relations of containment between genus, species and differentiae. For example, an argument based on the topic from genus involves a notion of containment: the genus is taken to contain something that the species is then also inferred to contain. For example, since all mammals are mortal, we can infer that human beings are mortal too: the genus ‘mammal’ contains something, namely mortality, that the species ‘human being’ also contains (Bosman 2018, 235)[^bosman-2018]. This metaphysical notion of containment then gives rise to a related semantic notion, which establishes relations of semantic containment between concepts (Bosman 2018)[^bosman-2018]. The upshot is thus that Boethius does not seem to have had in mind a relation of containment between antecedent and consequent, but his observations on what the metaphysics of genus and species entails for certain forms of inference may well have been the historical precursor of (Co).

### 2.2 Abelard

The period from Boethius in the 6ᵗʰ century to Abelard in the 12ᵗʰ century remains for now quite understudied, in particular as a consequence of the scarcity of extant manuscript evidence. As far as we can tell, the approach to logic in the 8ᵗʰ and 9ᵗʰ centuries appears to have been largely Platonist and metaphysical in character (Wilks 2016)[^wilks-2016]. Subsequently, a more linguistic orientation began to emerge, including investigations into inferential relations between categorical and hypothetical statements (Wilks 2016)[^wilks-2016]. It seems fair to say, however, that none of these investigations count as fully-fledged theories of consequence.

Indeed, it was only in the 12ᵗʰ century, with Abelard, that a novel and highly sophisticated theory of consequence/entailment was to be formulated. Abelard’s starting point is the same material inherited from Boethius which had been available for centuries, and yet what he does with it is quite extraordinary; in particular, he understood better than anyone before him the nature of what we now refer to as propositional operations. His treatment of the conditional and of the disjunction echoes what is now known as connexive logic (Martin 2018)[^martin-2018] (see the entry on connexive logic). And yet, his account is ultimately untenable, as the resulting system is in fact inconsistent (Martin 2004, 2018)[^martin-2004][^martin-2018].

Tellingly, his theory of consequence is presented in the part of the *Dialectica* dedicated to the topical framework (the book *De Locis*), which again illustrates the close historical connections between theories of consequence and the *Topics*. Abelard speaks mostly of ‘*inferentia*’ rather than ‘*consequentia*’, as the latter is for him a subspecies of the former. He defines the concept of *inferentia* as follows:

> Therefore, inference consists in the necessity of consecution, that is, in that the sense (*sententia*) of the consequent is required (*exigitur*) by the sense (*sensus*) of the antecedent, as is asserted with a hypothetical proposition … (*Dial.* 253, translation from Martin 2004, 170)[^martin-2004]

The phrase ‘necessity of consecution’ could be viewed as Abelard’s formulation of the criterion of necessary truth-preservation (TP), but he seems to demand something more than mere truth-preservation, namely a tighter connection of relevance (*exigitur*) between the senses of antecedent and consequent (Martin 2004, section II.5)[^martin-2004]. Indeed, Abelard seems to entertain different conceptions of the containment relation (Co) between antecedent and consequent: as a metaphysical (*Dial.* 255), semantic (*Dial.* 253), and epistemic (*Dial.* 255) relation.

Abelard then further distinguishes perfect from imperfect inferences,[^note-6] and this distinction sets him apart from the whole preceding tradition:

> But inferences are either perfect or imperfect. An inference is perfect when, from the structure of the antecedent itself, the truth of the consequent is manifest, and the construction of the antecedent is so disposed that it contains also the construction of the consequent in itself, just as in syllogisms or in conditionals which have the form of syllogisms. (*Dial.* 253/4)

He goes on to argue that what warrants a perfect inference, i.e. its ‘*vis inferentiae*’, is the construction itself: “‘the truth of perfect inferences comes from the structure (*complexio*), not from the nature of things” (*Dial*. 255). This is a novel development, as for authors such as Boethius and those following him, the warrant of *all* consequences is ultimately to be found in the ‘nature of things’, and is captured by means of topical principles. (Abelard then goes on to provide arguments directed against this Boethian view, see MacFarlane 2000, A.4.)[^macfarlane-2000] What Abelard refers to as the construction/structure of an inference is indeed roughly what we now understand as a *schema* (see entry on schemata of this encyclopedia), as his discussion of examples suggests: it is the substitution of *terms by other terms* while preserving the consecution (i.e. a version of (ST)) that is the hallmark of perfect inferences. “Whatever terms you substitute, whether they are compatible or incompatible with one another, the consecution can in no way be broken.” (*Dial*. 255, translation from Martin 2004, 171)[^martin-2004]

Now, while early traces of the substitutional conception of validity might be perceived in Aristotle as well as in some of the ancient commentators, with Abelard it is (arguably) for the first time presented as providing the grounds for a certain class of consequences. And yet, Abelard’s conception of consequence is not *reduced* to (ST), given that imperfect inferences are just as legitimate/valid as the perfect ones: imperfect inferences are those that fail the substitution criterion but satisfy the ‘necessity of consecution’ criterion. Thus, for Abelard, (ST) defines a special subclass among valid inferences, but a combination of (TP) and (Co) remains the true core of his notion of inference/consequence (see *Dial.* 283–4 for two senses of necessity of consecution). Indeed, in his subsequent discussion he deals with imperfect inferences much more extensively than with the perfect ones.

Many of Abelard’s logical concepts were tacitly absorbed by later authors, though not by means of direct influence, and often with no explicit attribution to Abelard (Martin 2004)[^martin-2004]. Ultimately, the Abelardian approach to consequences did not prevail (Normore 2015)[^normore-2015]. It is revealing that we now have only one surviving copy of his *Dialectica*, a clear sign that it was not widely read.

### 2.3 13ᵗʰ Century

The two main features of 13ᵗʰ-century logic are arguably the emergence of the terminist tradition (authors such as Peter of Spain, William of Sherwood and Lambert of Auxerre/Lagny) and the absorption of the newly rediscovered Aristotelian texts and other Greek sources, resulting in an extensive commentary tradition (Uckelman and Lagerlund 2016)[^uckelman-2016] The latter resulted in the distinction between three groups of logical theories: what became known as the *logica vetus* (= old logic) (topics emerging from the traditional texts which had remained available throughout: the *Categories*, *On Interpretation*, Porphyry’s *Isagoge*); the *logica nova* (= new logic) (covering the material from the newly discovered Aristotelian texts); and the *logica* *modernorum* (= logic of the moderns) (topics not directly related to the Aristotelian corpus, such as consequence, insolubles and obligations).

The terminist authors did not address consequence as an autonomous topic of investigation; their views on the matter are scattered among their analyses of sentences, the *Topics*, fallacies and syncategoremata (the syncategorema ‘*si*’ in particular) (Spruyt 2018)[^spruyt-2018]. For 13th-century authors, the two main types of consequence were natural and accidental consequences (Martin 2018)[^martin-2018]; another frequently drawn distinction was that between simple and as-of-now consequences (Archambault 2018a)[^archambault-2018a]. But one cannot really speak of full-fledged theories of consequence among the terminist authors, at least not if compared with what was to come in the 14ᵗʰ century.

Overall, 13ᵗʰ-century authors viewed the semantics of conditionals and the relation of consequence predominantly through metaphysical lenses; the main line of thought was that the antecedent had to be somehow causally related to the consequent (Spruyt 2018)[^spruyt-2018]. These metaphysical relations continued to be conceptualized in terms of the framework from the *Topics*, as they had been by Boethius. Given this metaphysical focus, 13ᵗʰ-century authors typically did not recognize (TP) as a sufficient criterion for a relation of consequence to hold; some stronger connection between antecedent and consequent was required, often conceptualized in terms of containment (Co).

Also significant for the overall development of the concept of consequence is the increasing presence of Aristotelian hylomorphism in logical contexts. While hylomorphism had not been entirely unknown to Latin authors prior to the rediscovery of the remaining Aristotelian texts in the late 12ᵗʰ and 13ᵗʰ centuries, in this period an explosion of applications of Aristotelian metaphysical concepts in other areas occurred, especially in logic (Spruyt 2003)[^spruyt-2003]. In particular, applications of the form-matter distinction to arguments (specifically, syllogisms) became frequent again, after a hiatus of many centuries since the ancient commentators. Such applications can be found in the only known 12ᵗʰ-century commentary on the *Prior Analytics*, the *Anonymus Aurelianensis* III (Ebbesen 1981)[^ebbesen-1981], in the *Dialectica Monacensis* (an anonymous text of the early 13ᵗʰ century, edited in De Rijk 1962/7)[^de-1962], and in Robert Kilwardby’s commentary on the Prior Analytics (1230s — see Thom 2007, 2019)[^thom-2007][^thom-2019], among other texts. The significance of these applications is that they paved the way for the consolidation of the notion of formal consequence in the 14ᵗʰ century (Dutilh Novaes 2012b)[^dutilh-2012b], which in turn was to have a huge impact on the rest of the history of logic.

Indeed, one of the earliest known uses of the phrase ‘formal consequence’ can be found in Simon of Faversham’s questions on the *Sophistical Refutations*, written in the 1280s:

> When it is said that “an animal is a substance; therefore a man is a substance” is a good consequence I reply that this consequence does not hold in virtue of form (*ratione formae*), but rather in virtue of matter. Because according to the Commentator [Averroes] on the first book of the *Physics*, an argument which is valid (*concludens*) in virtue of form must hold in all matter. This consequence, however, holds only for features which are essential […] and so this consequence is not formal (*formalis*). (Simon of Faversham, *Quaestiones Super Libro Elenchorum*, quaestio 36, 200; translation from Martin 2005, 135.)[^martin-2005]

It is significant that Simon refers to Averroes’ commentary on the *Physics*, thus illustrating the importation of the Aristotelian (meta)physical framework into logical analyses. We here have the notion of ‘valid in virtue of form’ (as with Abelard’s ‘*complexio*’), and the association of form and formality with the idea of substitution of terms (ST). Other authors of the same period, John Duns Scotus for example, also use the phrase ‘*consequentia formalis*’ and its variants, but not in the substitutional sense of holding ‘in all matter’ (Martin 2005)[^martin-2005].

This is the historical background for the consolidation of the distinction between formal and material consequences in the 14ᵗʰ century: a progression towards general theories of consequence rather than exclusive focus on syllogisms, and the increasing application of hylomorphism to arguments — at first to syllogisms, and later to arguments and consequences in general.

## 3. 14ᵗʰ-Century Theories of Consequence

### 3.1 The emergence of treatises on consequence in the 14ᵗʰ century

The precise historical origins of 14ᵗʰ-century theories of consequence are still debated among scholars. What we know is that, at the beginning of the 14ᵗʰ century, treatises and chapters bearing the title *De consequentiis* and similar titles began to appear. Why then, and not before? Naturally, the subject itself, that is, the logical/inferential relations between sentences, had been extensively discussed by earlier authors, as we have seen. But no treatises or chapters were specifically dedicated to the topic or bore such titles before the 14ᵗʰ century.

According to a once influential hypothesis, medieval theories of consequences would have emerged from the tradition commenting on and discussing Aristotle’s *Topics* (Bird 1961; Stump 1982)[^bird-1961][^stump-1982]. This hypothesis may seem plausible: traditionally, the role of the topical framework was often to account for the patterns of (correct) inference and reasoning which did not fit into the syllogistic system presented in the *Prior Analytics*. So, conceptually, it would seem quite natural that the tradition on the *Topics* might represent the historical origins of theories of consequences. Moreover, as we have seen, most earlier discussions of the notion of consequence (e.g., Abelard) were conducted explicitly within the context of the topical framework, following Boethius.

However, it has been argued that this hypothesis does not receive historical and textual confirmation. (Green-Pedersen 1984, chapter E in particular)[^green-pedersen-1984] is still the most comprehensive study on this subject, covering virtually every text known to us that is relevant for the hypothesis.) Green-Pedersen argues (1984, 270) that the late 13ᵗʰ-century literature on the *Topics*, that is, the period immediately preceding the emergence of treatises on consequences, gives absolutely no indication of what was to come. In other words, there are no significant similarities between the contents of these 13ᵗʰ-century treatises on the *Topics* and the 14ᵗʰ-century treatises on consequences. Therefore, we may conclude that the *Topics* could not have been the main, and in any case certainly not the only, source for the emergence of 14ᵗʰ-century theories of consequences.

Be that as it may, the importance of the *Topics* for the development of 14ᵗʰ-century theories of consequences should not be altogether dismissed. It is worth noticing that two of the first authors who presented systematic discussions of consequence in the 14ᵗʰ century, namely Ockham and Burley, are both in some way or another influenced by the *Topics*. Burley explicitly says that all valid consequences are based on dialectical topics (*On the purity*, p. 158 and 162). In contrast, the relation of Ockham’s theory of consequence to the topical framework is more convoluted; Green-Pedersen argues that Bird’s reconstruction of Ockham’s theory within the topical framework (Bird 1961)[^bird-1961] is not satisfactory (Green-Pedersen 1984, 268)[^green-pedersen-1984], but he also confirms that Ockham’s ‘intrinsic’ and ‘extrinsic’ middles, crucial concepts for his theory of consequence (to be explained shortly), are concepts essentially taken (albeit in modified form) from the topical framework.

In short, although the current availability of texts still does not allow for definitive conclusions to be drawn, the picture that at this point seems most plausible is that different strands of traditional logical theories converged in order to give rise to the 14ᵗʰ-century theories of consequences. It seems that at least four traditions contributed substantially to these developments: treatises on *syncategoremata*, especially in connection with the syncategorema ‘*si*’; discussions of hypothetical syllogisms; commentaries on the *Prior Analytics*; and the tradition of the *Topics*. Different elements of each of these traditions contributed to the development of different aspects of the theories of consequence.[^note-7] Green-Pedersen (1984, 295) argues, for example, that the late 13ᵗʰ-century treatises that most resemble early 14ᵗʰ-century treatises on consequences are “the treatises on syncategorematic words and a number of sophism-collections arranged after syncategoremes.”

The different 14ᵗʰ-century treatises on consequences can be divided into four main groups:

1. The treatises on consequences from the very beginning of the 14ᵗʰ century: Burley’s *De consequentiis* and two anonymous treatises of roughly the same time (Green-Pedersen 1981)[^green-pedersen-1981]. They are in fact rather unsystematic collections of rules of consequence/inference; it seems that their purpose was solely to provide ‘rules of thumb’ to deal with sophismata related to some syncategorematic terms. No conceptual or systematic discussion of the nature of consequence is presented.
2. The second group is represented by Burley’s *De Puritate*, the chapters on consequence in Ockham’s *Summa Logicae* (III-3), the *Elementarium logicae* and *Tractatus logicae medius* (sometimes attributed to Ockham but whose authorship is not definitively established), and the anonymous *Liber consequentiarium* (edited in Schupp 1988)[^schupp-1988]. In these texts, the concept of (intrinsic and extrinsic) middles and other topical concepts occupy a prominent place. They display a much deeper interest in the very nature of consequence than the previous group, presenting general definitions and criteria for what is to count as a consequence, as well as divisions of kinds of consequence.
3. The third group is represented by Buridan’s treatise on consequence and the treatises inspired by it, most notably Albert of Saxony’s (a chapter of his *Perutilis logica*) and Marsilius of Inghen’s treatise on consequence (Ciola 2018)[^ciola-2018]. There is also the interesting commentary on the *Prior Analytics* formerly attributed to Scotus,[^note-8] which is thought to have been composed before or in any case independently of Buridan’s treatise (Lagerlund 2000, chapter 6)[^lagerlund-2000]. In these treatises, topical notions such as the doctrine of intrinsic and extrinsic middles have disappeared completely. What characterizes them as a group is the definition of formal consequence based on the substitutivity criterion, in the spirit of (ST) (more on this below). This tradition is usually referred to as the Parisian/continental tradition on consequences.
4. The fourth group of treatises is predominantly British, and is represented by a significantly greater number of surviving treatises than group (3). It is represented by the treatises by Robert Fland, John of Holland, Richard Billingham, Richard Lavenham, Ralph Strode, and the *Logica Oxoniensis,* among others (Ashworth and Spade 1992)[^ashworth-1992]. What characterizes this group as such is the definition of formal consequence in terms of containment of the consequent in the antecedent, in the spirit of (Co), usually interpreted in epistemic terms.

Chronologically, the development of theories of consequence in the 14ᵗʰ century is thus characterized by an early, unsystematic stage (1), then by a stage of further development, in which topical notions play a prominent role (2), and then by two further traditions which run more or less parallel, namely the Parisian/continental tradition (3) and the British tradition (4). While they differed in particular in the various definitions given to the formal vs. material consequence distinction, they all agreed that necessary truth-preservation (TP) is a necessary (but perhaps not sufficient) condition for something to count as a (valid) consequence (Dutilh Novaes 2008)[^dutilh-2008].

Before moving on, it is important to note that, in the 14ᵗʰ century, rules of consequence were often discussed against the background of the genre of oral disputation known as *obligationes* (see entry on *obligationes* of this encyclopedia). It is common to encounter formulations of rules of consequence in obligational terms, for example: if you have conceded the consequence and its antecedent, then you must concede the consequent. Thus, interesting reflections on consequence are also to be found in *obligationes* treatises (and vice-versa).

### 3.2 Burley and Ockham

Walter Burley is the author of the oldest treatise on consequence with known authorship (edited by Brown in 1980), but it is in his later work *De Puritate*, longer version, that one finds his fully developed theory of consequence (Archambault 2018b)[^archambault-2018b]. The shorter version of *De Puritate* is thought to have been composed before Ockham’s *Summa Logicae*, and contains only a section on consequence and a section on *syncategoremata*. It is believed that after becoming acquainted with Ockham’s *Summa Logicae*, Burley abandoned the text of what is now known as the shorter version of *De Puritate* and began to work on a new draft, which was to become the longer version (Spade 2000)[^spade-2000]. The theory of consequence presented in the shorter version is based on ten basic principles, four of which are clearly sentential/propositional, while the other six take terms as the basic logical unit (Boh 1982)[^boh-1982]. The only distinction of consequence that Burley discusses is that between simple and as-of-now consequence, a traditional distinction which remained popular in the 14ᵗʰ century:

> First therefore I assume a certain distinction, namely this one: One kind of [consequence] is simple, another kind is as-of-now (*ut nunc*). A simple [consequence] is one that holds for every time. For example ‘A man runs; an animal runs.’ An as-of-now [consequence] holds for a determinate time and not always. For example ‘Every man runs; therefore, Socrates runs’. For that [consequence] does not hold always, but only while Socrates is a man. (Burley, *De Puritate*, 3)

This temporal understanding of the simple vs. as-of-now distinction is the one adopted by most authors, both before and after Burley (however, see Pseudo-Scotus’ formulation, discussed in the next section), and is repeated verbatim in the longer version of *On the Purity…* (p. 146). Another interesting feature of the shorter version is the fact that it treats syllogisms under the concept of consequence, thus illustrating the absorption of syllogistic by theories of consequences in the 14ᵗʰ century. Burley’s mature theory of consequence, as presented in the longer version of *De Puritate*, is best discussed against the background of the theory of consequence presented in Ockham’s *Summa Logicae*, so let us now turn to Ockham first.

Ockham’s *Summa Logicae* is thought to date to the first years of the 1320s; section 3 of Part III is entirely dedicated to consequences. In chapter 1 of III-3, Ockham presents a complicated account of consequences based on nine distinctions, including the simple vs. as-of-now distinction; the distinction between formal and material consequence is the last one presented.[^note-9] Ockham’s *Summa* presents one of the earliest-known systematic discussions of this distinction (Martin 2005)[^martin-2005], but Ockham offers virtually no justification for his use of the notions of form and matter with respect to consequences. It is also possible that Ockham deliberately ignores the well-entrenched distinction between natural and accidental consequences, given that he mentions *nine* distinctions, but not this one. Here is how Ockham introduces the notion of a formal consequence:

> Formal consequences are of two kinds. Some hold in virtue of an extrinsic middle, which concerns the form of propositions. For example, such rules as ‘from an exclusive to a universal, with transposition of terms, is a good consequence’; ‘if the major premise is necessary and the minor premise is assertoric (*de inesse*), the conclusion is necessary’. Others hold immediately in virtue of an intrinsic middle, and mediately in virtue of an extrinsic middle regarding the general conditions of the proposition, […] such as in ‘Socrates is not running, therefore a man is not running.’ (William of Ockham, *Summa Logicae* III-3, ch. 1, lines 45–54)

Thus, Ockham’s view appears to be that formal consequences are those that hold in virtue of *middles*, be they intrinsic or extrinsic. (But see Crimi 2018 for a somewhat different interpretation, based on a somewhat different rendering of the above passage, as recommended by Schupp 1993.)[^crimi-2018][^schupp-1993] A consequence holds immediately in virtue of an intrinsic middle when it holds in virtue of the truth of a different sentence formed from its terms. For example, ‘Socrates is not running, therefore a man is not running’ holds in virtue of this middle: ‘Socrates is a man’, since if ‘Socrates is a man’ is not true, the consequence does not hold. These are typically enthymematic consequences, i.e. consequences with a ‘missing premise’ (with the additional premise, they become a valid syllogism). An extrinsic middle, by contrast, is a sentence not containing the terms that form the antecedent and the consequent of the putative consequence, but which is a general rule describing the ‘fact’ that warrants the passage from the antecedent to the consequent (reminiscent of Boethius’ maximal propositions), and which concerns the *form* of sentences. Ockham’s example of a consequence holding immediately in virtue of an extrinsic middle is ‘Only a man is a donkey, therefore every donkey is a man’, which holds in virtue of this general rule: ‘an exclusive and a universal with transposed terms signify the same and are convertible’.

Notice however that ‘Socrates is not running, therefore a man is not running’ and ‘Only a man is a donkey, therefore every donkey is a man’ are both *formal* consequences for Ockham (since both hold in virtue of middles), whereas the former is clearly an enthymeme, not valid in all substitutional instances of the terms ‘Socrates’, ‘man’, and ‘running’, thus not satisfying (ST) (see Crimi 2018 on the discrepancy between Ockham’s notion of formal consequence and Buridan’s (ST)-based notion of formal consequence). The latter, on the other hand, is valid in all substitutional instances of ‘donkey’ and ‘man’, and indeed this seems to be the case of most, if not all, of Ockham’s formal consequences immediately valid in virtue of extrinsic middles; he explicitly says for example that syllogisms are of the latter kind. Effectively, formal consequences immediately valid in virtue of extrinsic middles satisfy the (ST) criterion of being valid ‘in all matter’, but the same does not hold of Ockham’s (enthymematic) consequences valid in virtue of an intrinsic middle.

Curiously, while Ockham can be credited with having been the first to use the terms ‘formal consequence’ and ‘material consequence’ systematically, the *content* of his distinction did not pass on to later authors. This is arguably because Ockham’s distinction is cast in terms of intrinsic and extrinsic middles, peculiar concepts belonging to the Boethian framework which was already losing its influence by Ockham’s time (Green-Pedersen 1984)[^green-pedersen-1984]. Indeed, one seldom encounters the concept of ‘middles’ in writings of the post-Ockham period, except for texts under his direct influence.

As for material consequences, it is not entirely clear how exactly Ockham intended to define this class of consequences. He says that material consequences are those that hold in virtue solely of (the meaning of) their terms (Ockham, *Summa Logicae* III-3, ch. 1, lines 55–57) but the two examples he gives are of a consequence with an impossible antecedent and a consequence with a necessary consequent. This suggests – but does not definitely establish – that for Ockham this category consists exclusively of consequences of this sort (*ex impossibili* and *ad necessarium* consequences). In any case, Ockham did not offer any explicit motivation for his use of the concept of *matter* to characterize this class of consequences.[^note-10]

As mentioned above, the longer version of Burley’s *De Puritate* is thought to be largely a response to Ockham’s *Summa Logicae*, not exclusively but also with respect to consequence. Burley recovers the natural vs. accidental distinction which had been deliberately neglected by Ockham (Archambault 2018b)[^archambault-2018b], but in fact formulates it with a terminology similar to that used by Ockham for formal consequences, namely in terms of the concepts of intrinsic and extrinsic topics (rather than ‘middles’, but this appears to be above all a mere terminological difference):

> Simple [consequence] is of two kinds. One is natural. That happens when the antecedent includes the consequent. Such an inference holds through an intrinsic topic. An accidental inference is one that holds through an extrinsic topic. That happens when the antecedent does not include the consequent but the inference holds through a certain extrinsic rule. (Burley, *De Puritate*, 146)

Notice again the reference to the idea that the antecedent may include/contain the consequent (in natural consequences). One may conjecture that Burley sought to neutralize Ockham’s distinction between formal and material consequences in terms of intrinsic and extrinsic middles by formulating the traditional distinction between natural and accidental consequences in terms of containment and intrinsic/extrinsic topics. Moreover, when discussing the notion of formal consequence later in the text (pp. 171–173, replying to a possible objection), Burley seems to be criticizing Ockham’s definition of material consequences as those which hold solely in virtue of the meaning of terms:

> Thus for a [consequence] to hold by reason of the terms can happen in two ways, either because it holds materially by reason of the terms, or because it holds formally by reason of the terms — that is, by the *formal* reason of the terms. (Burley, *On the Purity*, 173)

In other words, Burley seems to be saying that Ockham’s formulation of the distinction is ineffective and thus inadequate. The exact formulation of the distinction between formal and material consequences presented by Ockham was indeed not adopted by later authors, but it would be excessively speculative to attribute this outcome to Burley’s criticism. In effect, even less of a Burleian legacy is to be found in later authors specifically with respect to consequence, in particular as the formal vs. material distinction became the main subdivision of consequence later on (albeit under different formulations).

### 3.3 Buridan and the Parisian tradition

John Buridan’s treatise on consequence (TC, edited by H. Hubien in 1976, English translation in (Buridan 2015)[^buridan-2015]) quite likely represents the pinnacle of sophistication for (Latin) medieval discussions of the concept of consequence. Its modern editor dates it to the 1330s, thus belonging to the early stages of Buridan’s career. We currently know much less about Buridan’s immediate predecessors than about Burley’s or Ockham’s, so it is not clear who Buridan takes inspiration from or is criticizing. The treatise is composed of four books: Book I presents general considerations on the very notion of consequence; Book II treats of consequences involving modal sentences; Book III treats of syllogisms involving assertoric (i.e. non-modal) sentences; Book IV deals with syllogisms involving modal sentences. Each of them is remarkable in its own way (Book III for example represents a radical subversion of Aristotelian orthodoxy, with the suggestion that third-figure syllogisms are more foundational than first-figure syllogisms), but here we shall focus on the first two books (Book I in particular), given the methodological decision of leaving syllogistic aside in the present analysis.

In Book I, Buridan presents the general definition of a consequence in the familiar terms of necessary truth-preservation:

> Hence, many say that of two propositions one is antecedent to the other if it is impossible for the one to be true without the other being true, and one is consequent to the other if it is impossible for the one not to be true when the other is true, so that every proposition is antecedent to every other proposition for which it is impossible for it to be true without the other being true. (Buridan, TC, 21; transl. 67)

He then goes on to reformulate the definition for reasons related to his view that only actually produced sentences (sentence-tokens) can have a truth-value (Klima 2004; Dutilh Novaes 2005)[^dutilh-2005][^klima-2004]. ‘No sentence is negative, therefore no donkey is running’ comes out as a valid consequence according to the criterion thus formulated, because ‘No sentence is negative’ can never be true: its mere existence falsifies itself whenever it is produced. According to Buridan, this example should not count as a valid consequence, and one reason he gives for this is that its contrapositive ‘Some donkey is running, therefore some sentence is negative’ is not a valid consequence. He formulates a definition of consequences in terms of ‘howsoever the antecedent/consequent signifies things to be’ in order to accommodate such counterexamples, but adds that in most cases, the simpler definition is sufficiently accurate.

Commitment to sentence-tokens aside, Buridan’s notion of consequence clearly has necessary truth-preservation (TP) as its fundamental component. So for him, enthymematic consequences such as ‘a man runs, therefore an animal runs’ are just as valid as syllogistic consequences or other consequences satisfying the criterion of preservation of validity under term substitution (ST). However, Buridan does recognize that there is an important distinction between consequences which do and those which do not satisfy the substitutional criterion; giving continuation to a tradition which includes Alexander of Aphrodisias and Simon of Faversham, he conceptualizes this distinction in hylomorphic terms, more specifically in terms of the distinction between formal and material consequence:

> A consequence is called formal if it is valid in all terms retaining a similar form. Or if you want to put it explicitly, a formal consequence is one where every proposition similar in form that might be formed would be a good consequence, e.g., ‘That which is A is B, so that which is B is A’. (Buridan, TC, 22–23, transl. 68; my emphasis)

Material consequences are those which do satisfy the necessary truth-preservation criterion (TP) but do not satisfy the substitutional criterion (ST) (Crimi 2018)[^crimi-2018]. At first sight, Buridan’s distinction between formal and material consequence seems very similar to, for example, Abelard’s distinction between perfect and imperfect inferences. There is, however, a fundamental difference; while Buridan says formal consequences are *formal* in virtue of satisfying (ST), nowhere does he suggest that formal consequences are *valid* in virtue of (ST), as Abelard had claimed for the ‘*complexio*’ of perfect inferences (Dutilh Novaes and Bosman 2017)[^dutilh-2017]. Rather, for Buridan, formal consequences – like all consequences – are valid in virtue of satisfying (TP). Regarding material consequences, Buridan says they are *made evident* only by means of a reduction to a formal consequence (TC, 1.4), but this observation pertains to the epistemic level of how the validity of a consequence is made apparent to us, not to the quasi-metaphysical level of what grounds it.[^note-11]

Buridan also comments explicitly on what is to be understood as the form and the matter of a consequence:

> I say that when we speak of matter and form, by the matter of a proposition or consequence we mean the purely categorematic terms, namely, the subject and predicate, setting aside the syncategoremes attached to them by which they are conjoined or denied or distributed or given a certain kind of supposition; we say all the rest pertains to the form (Buridan, TC, 30, transl. 74)

The view that the form of a consequence/argument pertains to its syncategorematic terms while its matter pertains to its categorematic terms is presupposed in both earlier and subsequent texts, but here with Buridan it receives a rare explicit formulation. A modern version of this idea still survives, in the form of the doctrine of the logical form of arguments and the modern preoccupation with logical constants (Read 1994; Dutilh Novaes 2012a; entry on logical constants of this encyclopedia)[^dutilh-2012a][^read-1994]. However, it is worth emphasizing once again that drawing the line between the form and the matter of an argument/consequence in this manner still does not entail the thesis that the form is that in virtue of which a valid argument is valid; nor does it entail the thesis that *only* the arguments/consequences satisfying the substitutional criterion are indeed valid. Buridan, in particular, does not hold either one of these theses.

In the final section of Book I, Buridan formulates a series of general principles which follow from his proposed definition of consequence, such as that from the impossible anything follows (first conclusion; see D’Ors 1993 and Normore 2015 on Buridan and the *ex impossibili* principle)[^d’ors-1993][^normore-2015], the principle of contraposition (third conclusion), and also many principles pertaining to the semantic properties of the categorematic terms in a consequence (see entry on medieval theories of properties of terms). Thus, here again we see that medieval theories of consequence never completely abandon the term perspective to adopt an exclusively sentential/propositional perspective.

Book II of Buridan’s treatise presents a sophisticated analysis of the logical behavior of modal sentences. Modal sentences can be either composite or divided, depending on where the modal term occurs: if it is either the subject or the predicate of the sentence, while the other term is an embedded sentence in nominalized form (in ‘dictum’ form, in the medieval terminology), then the sentence is a composite modal sentence. If however the modal term occurs as an adverb modifying the copula, then it is a divided modal sentence. Buridan then proves a series of conclusions and equivalences for each kind of modal sentences, such as that ‘*B* is necessarily *A*’ is equivalent to ‘*B* is not possibly not *A*’ (Johnston 2014)[^johnston-2014].

The other treatises on consequence in the Parisian/continental tradition do not seem to depart significantly from Buridan’s overall analysis, with one possible exception: the commentary on the *Prior Analytics* formerly attributed to Scotus (edited in Yrjönsuuri 2001)[^yrjönsuuri-2001], and whose authorship remains controversial. The dating is equally problematic; crucially, it is not clear whether it was written before or after Buridan’s treatise, but some scholars (Lagerlund 2000, chapter 6)[^lagerlund-2000] have argued that at any rate Pseudo-Scotus displays no knowledge of Buridan’s treatise (likewise, there is no obvious evidence that Buridan was familiar with Pseudo-Scotus’ text).

The treatise proceeds very much in the spirit of chapter 3 of Book I of Buridan’s treatise: a putative definition of consequence is proposed, but then quickly a counterexample is found, namely something that should not count as a consequence and yet satisfies the criterion, or the other way round (Boh 1982, 307–310)[^boh-1982].[^note-12] But while Buridan rests his case after the third proposed definition, Pseudo-Scotus goes on, and formulates a counterexample to the definition that Buridan settles on: ‘God exists, hence this argument is invalid’. If this consequence is valid, then it has a necessary antecedent and a false consequent (since the consequent says that it is invalid). But then it is invalid. In sum, if it is valid, it is invalid; thus, by the *consequentia mirabilis* ((*A* → ~*A*) → ~*A*), it is invalid. But if it is invalid, it is necessarily so, since the premise is a necessary sentence; therefore, we have a consequence with a necessary consequent, thus satisfying the necessary truth-preservation criterion, but which is plainly invalid. This has been described as a “proto-version” of Curry’s paradox.[^note-13]

Moreover, the Pseudo-Scotus treatise also offers an interesting formulation of the simple vs. as-of-now distinction: in contrast with e.g. Burley, according to Pseudo-Scotus this distinction applies only to material consequences (recall that for him, a formal consequence is the one that satisfies the substitutional criterion), and amounts to the modal value of the missing premise that can be added in order to turn the (enthymematic) consequence into a formal one. That is, if the missing premise is a necessary sentence, then the consequence is an absolute/simple one. But if the missing premise is a contingent truth (it has to be true with respect to the time indicated by the verbs of the consequence, otherwise the original material consequence does not hold), then the original material consequence holds only in some situations, namely the situations in which the contingent sentence happens to be true, and is thus an as-of-now consequence. The same formulation of the simple vs. as-of-now distinction can be found in Buridan’s treatise, Book I chapter 4, which again illustrates the conceptual connection between the two texts.

### 3.4 The British School

In the British tradition, which is then continued in Italy in the late 14ᵗʰ century and 15ᵗʰ century (Courtenay 1982)[^courtenay-1982], the definition of consequence in terms of necessary truth-preservation (TP) is also unanimously adopted, as for example in Billingham (Billingham/Weber 2003, 80)[^billingham-2003], Strode (cited in (Pozzi 1978, 237)[^pozzi-1978]) and Paul of Venice (*Logica Parva*, p. 167). In fact, these authors present variations of (TP) without much discussion or analysis, contrary to what is found in Buridan’s treatise, for example. More generally, the treatises in this tradition are characterized by a lesser degree of conceptual sophistication if compared to the earlier treatises by Ockham, Burley or Buridan. The goal seems to be mostly pedagogical, i.e. presenting ‘rules of thumb’ to argue correctly, rather than presenting a systematic, conceptual analysis of the concept of consequence.

Still, what is characteristic of this tradition is a specific interpretation of the idea of the conclusion being contained/understood (*intelligitur*) in the premises — that is, condition (Co) – which these authors rely on extensively to define the concept of formal consequence. We have seen that for Abelard, something like (Co) is a necessary condition for all consequences/inferences, which Martin (2004) spells out in terms of a criterion of relevance. 13ᵗʰ-century authors, such as Kilwardby (for whom (Co) provided the definition of natural consequences) and Faversham, also discussed variations of this idea (Read 2010, 177/8)[^read-2010], but prior to the late 14ᵗʰ century, it was not always formulated in epistemic/psychological terms. The authors in the 14ᵗʰ-century British tradition typically formulate the definition of formal consequence on the basis of variations of (Co), but giving it a very explicitly epistemic twist.

Lavenham, for example, says (as quoted in King 2001, 133)[^king-2001]: “A consequence is formal when the consequent necessarily belongs to the understanding of the antecedent, as it is in the case of syllogistic consequence, and in many enthymematic consequences”. Strode presents a similar formulation:

> A consequence said to be formally valid is one of which if it is understood to be as is adequately signified through the antecedent then it is understood to be just as is adequately signified through the consequent. For if someone understands you to be a man then he understands you to be an animal. (Translation in Normore 1993, 449)[^normore-1993].

Several other authors formulated similar definitions, such as Billingham (Weber 2003, 80) and Fland (Fland/Spade 1976)[^fland-1976]. Normore (1993, 449) argues that a significant transformation occurred in the 14ᵗʰ-century British tradition, which “puts in play the idea that deduction is not an objective relation between abstract objects or sentences but a mental operation performed on the bases of what can be understood or imagined.” This is noticeable not only in the definitions of formal (as opposed to material) consequence, but also in the very definitions of consequence which begin to mention mental acts, such as: “a consequence is a derivation (*illatio*) of the consequent from the antecedent” (Strode, quoted in Normore 1993, 449)[^normore-1993].

The epistemic/psychological interpretation of these formulations of formal consequences has not gone uncontested; arguably, they are equally compatible with a *semantic* interpretation emphasizing the signification of sentences (Read 2010, 178)[^read-2010]. But it is clear that, while the Parisian tradition defined the concept of formal consequence in terms of (ST), the British tradition formulated the same concept in terms of (Co). Both were ideas that had been floating around for centuries, but which yield very different conceptions of what counts as a formal consequence. These two approaches are not only intensionally divergent; they also disagree on the extension of the class of formal consequences. (ST)-formal consequences do not include enthymematic consequences such as ‘Socrates is a man, therefore Socrates is an animal’, but (Co)-formal consequences typically do. For British authors, the class of material consequences is often composed exclusively of consequences of the kind ‘from the impossible anything follows’ and ‘the necessary follows from anything’, which satisfy the truth-preservation criterion (TP) *a fortiori*, but typically fail relevant/containment criteria. ‘God does not exist, therefore you are a donkey’ counts as a valid consequence according to (TP) (‘God does not exist’ is considered to be an impossible sentence), but the consequent is not contained in the antecedent in the same way as in ‘Socrates is a man, therefore Socrates is an animal’. To mark this distinction, 14ᵗʰ-century British authors would typically view the former as a material consequence and the latter as a formal consequence (Ashworth & Spade 1992)[^ashworth-1992].

## 4. Conclusion

We started by surveying the ancient background for the emergence of Latin medieval theories of consequence, in particular Aristotle’s *Topics* and *Prior Analytics*, the commentaries by the ancient commentators, and Boethius’ influential logical texts. Theories of consequence only became an autonomous topic of investigation in the 14ᵗʰ century, but previous developments, in particular Abelard’s theory of inference/entailment and the increasing application of hylomorphism to logic in the 13ᵗʰ century, are equally deserving of attention. Nevertheless, the golden age for theories of consequence was the 14ᵗʰ century, when different theories were proposed by Burley, Ockham, Buridan, Billingham, Strode, Paul of Venice, and many others. As with much of scholastic logic, the topic of consequence continued to be explored in the 15ᵗʰ century and beyond (Ashworth 1974, chapter III)[^ashworth-1974], providing the background for much of what was to come in the history of logic, in particular the persistent association between logic and forms (MacFarlane 2000)[^macfarlane-2000].

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

### Primary Literature

### Secondary Literature

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=consequence-medieval). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/consequence-medieval/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=consequence-medieval&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/consequence-medieval/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- Some papers by Stephen Read on medieval theories of consequence:
- [John Buridan’s Theory of Consequence and his Octagons of Opposition](http://www.st-andrews.ac.uk/~slr/Buridan_Octagon.pdf)
- [The Medieval Theory of Consequence](https://link.springer.com/content/pdf/10.1007%2Fs11229-011-9908-6.pdf)

## Related Entries

Abelard [Abailard], Peter | Albert of Saxony | Aristotle, commentators on | Aristotle, General Topics: logic | Boethius, Anicius Manlius Severinus | Buridan, John [Jean] | Burley [Burleigh], Walter | insolubles [= *insolubilia*] | logic: ancient | logic: relevance | logical consequence | logical constants | medieval philosophy | modality: medieval theories of | *obligationes*, medieval theories of | Ockham [Occam], William | Paul of Venice | schema | syllogism: medieval theories of | Tarski, Alfred | terms, properties of: medieval theories of

### Acknowledgments

This entry was originally written by Catarina Dutilh Novaes for the Summer 2012 Edition of the SEP and was maintained and updated by her through the Fall 2020 Edition. She thanks Stephen Read, E. Jennifer Ashworth, and Bianca Bosman for helpful comments. Milo Crimi lightly revised parts of the entry for the Fall 2024 Edition and will maintain it going forward.

## Notes（原文脚注）

[^note-1]: The analysis here will focus exclusively on the developments in the Latin medieval tradition, thus not addressing the significant developments elsewhere, especially in the Arabic tradition. Henceforth, the entry will no longer use the qualification ‘Latin’, but the reader must bear in mind that there is much more to medieval philosophy than merely the Latin tradition. See for example the chapters on Arabic logic in Dutilh Novaes and Read (eds.) 2016.

[^note-2]: Throughout the text, the term ‘sentence’ will be used as a translation of the Latin term ‘*propositio*’, except when quoting translations of Latin texts, where occasionally ‘proposition’ will appear. What Latin authors meant by *propositio* is best captured by the notion of a declarative sentence, not by the modern abstract notion of proposition.

[^note-3]: Traditional Aristotelian logic, syllogistic in particular, is term-based in that the basic units of analysis are terms, not whole sentences: “All *A* is *B*, all *B* is *C*, thus all *A* is *C*” is a typical term-based valid schema. The Stoics had famously adopted a sentential perspective when investigating schemata such as modus ponens and modus tollens; Latin medieval authors, while under no direct Stoic influence, also investigated sentential operations and sentential connectives. But it would be a mistake to view the medieval theories as entirely sentential, in the sense of modern sentential/propositional logic: term-based analysis remains an important component of these theories.

[^note-4]: Martin (2009, 67) categorically asserts that Boethius had no direct knowledge of Stoic logic when developing the notion of hypothetical syllogism, even though his use of some of the classic Stoic examples suggests at least some kind of indirect influence.

[^note-5]: All translations from the Latin are my own, unless otherwise stated.

[^note-6]: The perfect vs. imperfect terminology is likely a reference to Aristotle’s distinction between perfect and imperfect syllogisms. Notice however that Aristotle’s imperfect syllogisms (i.e. those not belonging to the first figure) count as perfect inferences by Abelard’s criterion.

[^note-7]: See chapter E of (Green-Pedersen 1984)[^green-pedersen-1984].

[^note-8]: On the identity of the author of this text, see Read 1993 (fn. 10).

[^note-9]: Ockham’s multiple distinctions do not seem to be meant to be organized in a specific way, i.e. some being sub-distinctions of others, but rather as alternative ways of classifying consequences.

[^note-10]: The passage where Ockham defines material consequences is thought by some to be corrupted, so the exact content of this definition is still controversial among scholars — see Schupp 1993 and Crimi 2018.

[^note-11]: One is here reminded of the distinction between first-figure, perfect syllogisms and second- and third-figure imperfect but equally valid syllogisms, which is also essentially an epistemic distinction (Corcoran 1974)[^corcoran-1974].

[^note-12]: This similarity simply confirms that this way of arguing was very widespread at the time; incidentally, one is easily reminded of the current method of arguing by counterexamples in analytic philosophy.

[^note-13]: See Read 2001 for an account of Pseudo-Scotus’s ‘paradox’, where it is also argued that this so-called paradox did not obtain the desired effect of violating the modal criterion.

[^abelard-1956]: Abelard, Peter, *Dialectica*, edited by Lambertus M. de Rijk, Assen: van Gorcum, 1956.

[^albert-1988]: Albert of Saxony, *Perutilis logica*, in the incunabular edition of Venice 1522, with a Spanish translation by A. Muñoz García, Maracaibo: Univ. del Zulia, 1988.

[^alexander-1991]: Alexander of Aphrodisias, *On Aristotle’s Prior Analytics* 1.1–7, translation J. Barnes, S. Bobzien, K. Flannery, K. Ierodiakonou, London: Duckworth, 1991.

[^billingham-2003]: Billingham, Richard, *De Consequentiis*, in S. Weber, *Richard Billingham “De Consequentiis” mit Toledo-Kommentar*, Amsterdam: B.R. Grüner, 2003.

[^boethius-1969]: Boethius, *De hypotheticis syllogismis*, L. Obertello (ed.), with Italian translation, Brescia: Paideia, 1969.

[^boethius-1969-2]: –––, *De topicis differentiis*, D.Z. Nikitas (ed.), in *Boethius: De topicis differentiis kai hoi buzantines metafraseis tou Manouel Holobolou kai Prochorou Kudone*, Athens/Paris/Brussels: Academy of Athens/Vrin/Ousia (Corpus Philosophorum Medii Aevi. Philosophi Byzantini 5), 1969.

[^buridan-1976]: Buridan, John, *Iohannis Buridani tractatus de consequentiis*, edited by Hubert Hubien), Series *Philosophes Médievaux*, Vol. XVI, Louvain: Université de Louvain, 1976.

[^buridan-2015]: –––, *Treatise on Consequences*, translation by S. Read, New York: Fordham University Press, 2015.

[^buridan-2001]: –––, *Summulae de Dialectica*, translation by G. Klima, New Haven: Yale University Press, 2001.

[^burley-1955]: Burley, Walter, *De Puritate Artis Logicae — Tractatus Longior*, ed. Ph. Boehner, St. Bonaventure: The Franciscan Institute, 1955.

[^burley-1980]: –––, “De Consequentiis,” ed. N.J. Green-Pedersen, *Franciscan Studies*, 40 (1980): 102–166.

[^burley-2000]: –––, *On the Purity of the Art of Logic — the shorter and the longer treatises*, transl. P.V. Spade, New Haven: Yale University Press, 2000.

[^fland-1976]: Fland, Robert, *Consequentiae*, in P.V. Spade, “Robert Fland’s *Consequentiae*: An Edition.” *Mediaeval Studies*, 38 (1976): 54–84.

[^garlandus-1959]: Garlandus Compotista, *Dialectica*, edited by Lambertus M. de Rijk, Assen: van Gorcum, 1959.

[^lavenham-1974]: Lavenham, Richard, in P.V. Spade, “Five Logical Tracts by Richard Lavenham,” in J. Reginald O’Donnell, ed., *Essays in Honour of Anton Charles Pegis*, Toronto: Pontifical Institute of Mediaeval Studies, 1974, pp. 70–124.

[^ockham-1974]: Ockham, William (of), *Opera Philosophica I*, St. Bonaventure: The Franciscan Institute, 1974.

[^paul-1984]: Paul of Venice, *Logica Parva*, translation by. A. Perreiah, Munich: Philosophia Verlag, 1984.

[^paul-2002]: –––, *Logica Parva*, edited by A. Perreiah, Leiden: Brill, 2002.

[^pseudo-scotus-2001]: Pseudo-Scotus, “Questions on Aristotle’s *Prior Analytics*: Question X,” In Yrjönsuuri (ed.) 2001, pp. 225–234.

[^schupp-1988]: Schupp, F., *Logical problems of the medieval theory of consequences, with the edition of the* Liber consequentiarum, Naples: Bibliopolis, 1988.

[^simon-1984]: Simon of Faversham, *Quaestiones Super Libro Elenchorum*, edited by Sten Ebbesen et al, Toronto: Pontifical Institute of Medieval Studies, 1984.

[^strode-1973]: Strode, Ralph, *Tractatus de Consequentiis*, in W. Seaton, *An Edition and Translation of the “Tractatus de Consequentiis” by Ralph Strode, Fourteenth Century Logician and Friend of Geoffrey Chaucer*, Ph.D. Dissertation, University of California, Berkeley, 1973.

[^archambault-2018a]: Archambault, J., 2018a, “Introduction: Consequences in Medieval Logic,” *Vivarium*, 56 (3–4): 201–221.

[^archambault-2018b]: –––, 2018b, “Consequence and Formality in the Logic of Walter Burley, ” *Vivarium*, 56 (3–4): 292–319.

[^ashworth-1974]: Ashworth, E.J., 1974, *Language and Logic in the Post-Medieval Period*, Dordrecht: Reidel.

[^ashworth-1992]: Ashworth, E.J. and P.V. Spade, 1992, “Logic in Late Medieval Oxford,” in J.I. Catto and R. Evans (eds.), *The History of the University of Oxford*, Oxford: Clarendon Press, pp. 35–64

[^barnes-1990]: Barnes, J., 1990, “Logical form and logical matter,” in A. Alberti (ed.), *Logica, Mente*, *e Persona*, Florence: Leo S. Olschki, pp. 1–119.

[^barnes-2007]: –––, 2007, *Truth etc.*, Oxford: Oxford University Press.

[^bird-1961]: Bird, O., 1961, “Topic and consequence in Ockham’s logic,” *Notre Dame Journal of Formal Logic*, 2: 65–78.

[^boh-1982]: Boh, I., 1982, “Consequences,” in N. Kretzmann, A. Kenny, J. Pinborg (eds.) 1982, pp. 300–314.

[^boh-2001]: –––, 2001, “Consequences and Rules of Consequence in the Post-Ockham Period,” in M. Yrjönsuuri (ed.) 2001, pp. 147–181.

[^boehner-1951]: Boehner, Ph., 1951, “Does Ockham know of material implication?” *Franciscan Studies*, 11: 203–230.

[^bosman-2018]: Bosman, B., 2018, “The Roots of the Notion of Containment in Theories of Consequence,” *Vivarium*, 56 (3–4): 222–240.

[^caret-2015]: Caret, C. and Hjortland, O. (eds.), 2015, *Foundations of Logical Consequence*, Oxford: Oxford University Press.

[^castelnérac-2009]: Castelnérac, B. and Marion, M., 2009, “Arguing for Inconsistency: Dialectical Games in the Academy,” in G. Primiero and S. Rahman (eds.), *Acts of Knowledge: History, Philosophy and Logic*, London: College Publications, pp. 37 –76.

[^ciola-2018]: Ciola, G., 2018, “Marsilius of Inghen on the Definition of consequentia,” *Vivarium*, 56 (3–4): 272–291.

[^corcoran-1974]: Corcoran, J., 1974, “Aristotle’s Natural Deduction System,” in J. Corcoran (ed.), *Ancient Logic and its Modern Interpretations*, Dordrecht: Kluwer, pp. 85–131.

[^courtenay-1982]: Courtenay, W., 1982, “The early stages in the introduction of Oxford logic into Italy,” in A. Maierù (ed.), 1982, pp. 13–32.

[^courtenay-2004]: –––, 2004, “The University of Paris at the time of Jean Buridan and Nicole Oresme,” *Vivarium*, 42 (1): 3–17.

[^crimi-2018]: Crimi, M., 2018, “Formal and Material Consequences in Ockham and Buridan,” *Vivarium*, 56 (3–4): 241–271.

[^de-1962]: De Rijk, L. M., 1962–1967, *Logica Modernorum*, Assen: van Gorcum.

[^dod-1982]: Dod, B., 1982, “Aristoteles Latinus,” in N. Kretzmann, A. Kenny, J. Pinborg (eds.) 1982, pp. 46–79.

[^d’ors-1993]: D’Ors, A., 1993, “*Ex impossibili quodlibet sequitur* (Jean Buridan)”, in Jacobi (ed.) 1993, pp. 195–212.

[^dutilh-2005]: Dutilh Novaes, C., 2005, “Buridan’s *consequentia*: consequence and inference within a token-based semantics,” *History and Philosophy of Logic*, 26(4): 277–297.

[^dutilh-2008]: –––, 2008, “Logic in the 14ᵗʰ century after Ockham,” in D. Gabbay and J. Woods (eds.), *Handbook of the History of Logic* (Volume 2), Amsterdam: Elsevier, pp. 433–504.

[^dutilh-2012a]: –––, 2012a, “Reassessing logical hylomorphism and the demarcation of logical constants,” *Synthese*, 185: 387–410.

[^dutilh-2012b]: –––, 2012b, “Form and Matter in Later Latin Medieval Logic: the cases of *suppositio* and *consequentia*,” *Journal of the History of Philosophy*, 50(3): 339–364.

[^dutilh-2021]: –––, 2021, *The Dialogical Roots of Deduction*, Cambridge: Cambridge University Press.

[^dutilh-2017]: Dutilh Novaes, C. and Bosman, B., 2017, “Formal, material, and hybrid grounding for consequence: Peter Abelard and John Buridan,” in C. Grellard (ed.), *Miroir de l’Amitié: Mélanges offerts â Joël Biard*, Paris: Vrin, pp. 229–242.

[^dutilh-2016]: Dutilh Novaes, C. and Read, S. (eds.), 2016, *The Cambridge Companion to Medieval Logic*, Cambridge: Cambridge University Press.

[^ebbesen-1981]: Ebbesen, S., 1981, “Analyzing Syllogisms or *Anonymus Aurelianensis III* — the (presumably) Earliest Extant Latin Commentary on the Prior Analytics, and its Greek Model,” *Cahiers de l’Institut du Moyen-Age Grec et Latin*, 37: 1–20.

[^etchemendy-1990]: Etchemendy, J., 1990, *The Concept of Logical Consequence*, Cambridge, MA: Harvard University Press.

[^field-2008]: Field, H., 2008, *Saving Truth from Paradox*, Oxford: Oxford University Press.

[^green-pedersen-1980]: Green-Pedersen, N.J., 1980, “Two Early Anonymous Tracts on Consequences,” *Cahiers de l’Institut du Moyen-Age Grec et Latin*, 35: 12–28.

[^green-pedersen-1981]: –––, 1981, “Walter Burley, *De consequentiis* and the origin of the theory of consequence,” in H.A.G. Braakhuis, C.H. Kneepkens and L.M. de Rijk, (eds.) *English Logic and Semantics*, Nijmegen: Ingenium, pp. 279–301.

[^green-pedersen-1984]: –––, 1984, *The Tradition of the Topics in the Middle Ages*, Munich: Philosophia Verlag.

[^green-pedersen-1985]: –––, 1985, “Early British Treatises on Consequences,” in P. Osmund Lewry O.P. (ed.), *The Rise of British Logic*, Toronto: Pontifical Institute of Mediaeval Studies, pp. 285–307.

[^jacobi-1993]: Jacobi, K. (ed.), 1993, *Argumentationstheorie*, Leiden: Brill.

[^johnston-2014]: Johnston, S., 2014, “A Formal Reconstruction of Buridan’s Modal Syllogism”. *History and Philosophy of Logic* 36 (1): 2–17.

[^kaufmann-1993]: Kaufmann, M., 1993, “Nochmals; Ockhams consequentiae und die materiale implication,” in K. Jacobi (ed.), pp. 223–232.

[^king-2001]: King, P., 2001, “Medieval proof theory,” in M. Yrjönsuuri (ed.), pp. 117–145.

[^klima-2004]: Klima, G., 2004, “Consequences of a Closed, *Token-Based Semantics*: The Case of John. Buridan,” *History and Philosophy of Logic*, 25: 95–110

[^klima-2016]: –––, 2016, “Consequence,” in C. Dutilh Novaes and S. Read (ed.), 2016, pp.316–341.

[^kretzmann-1982]: Kretzmann, N., A. Kenny, and J. Pinborg (eds.), 1982, *The Cambridge History of Later Medieval Philosophy*, Cambridge: Cambridge University Press.

[^lagerlund-2000]: Lagerlund, H., 2000, *Modal Syllogistics in the Middle Ages*, Leiden: Brill.

[^macfarlane-2000]: MacFarlane, J., 2000, *What does it mean to say that logic is formal?*, University of Pittsburgh, Ph.D. dissertation [[available online](http://johnmacfarlane.net/books.html)].

[^maierù-1982]: Maierù, A. (ed.), 1982, *English Logic in Italy in the 14th and 15th Centuries*, Napoli: Bibliopolis.

[^martin-1986]: Martin, C.J., 1986, “William’s Machine,” *The Journal of Philosophy*, 83 (10): 564–572.

[^martin-2004]: –––, 2004, “Logic,” in J. Brower and K. Gilfoy (eds.), *The Cambridge Companion to Abelard*, Cambridge: Cambridge University Press, pp. 158–199.

[^martin-2005]: –––, 2005, “Formal consequence in Scotus and Ockham: towards an account of Scotus’ logic,” in O. Boulnois, E. Karger, J.-L. Solre, G. Sondag (eds.), *1302: Duns Scot à Paris 1302*–*2002, Actes du colloque de Paris, septembre 2002*, Turnout: Brepols, pp. 117–150.

[^martin-2009]: –––, 2009, “The logical textbooks and their influence,” in J. Marenbon (ed.) *The Cambridge Companion to Boethius*, Cambridge: Cambridge University Press, pp. 56–84.

[^martin-2018]: –––, 2018, “The Theory of Natural Consequence,” *Vivarium*, 56 (3–4): 340–366.

[^moody-1953]: Moody, E.A., 1953, *Truth and Consequence in Medieval Logic*, New York and Amsterdam, North Holland.

[^netz-1999]: Netz, R., 1999, *The Shaping of Deduction in Greek Mathematics: A study in cognitive history*, Cambridge: Cambridge University Press.

[^normore-1993]: Normore, C., 1993, “The necessity in deduction: Cartesian inference and its medieval background,” *Synthese*, 96: 437–454.

[^normore-2015]: –––, 2015, “*Ex impossibili quodlibet sequitur,*” *Vivarium*, 53: 353–371.

[^pozzi-1978]: Pozzi, L., 1978, *Le consequentiae nella logica medievale*, Padova: Liviana.

[^read-1993]: Read, S., 1993, “Formal and material consequence, disjunctive syllogism and Gamma,” in K. Jacobi (ed.) 1993, pp. 233–262.

[^read-1994]: –––, 1994, “Formal and material consequence,” *Journal of Philosophical Logic*, 23: 247–65

[^read-2001]: –––, 2001, “Self-reference and validity revisited,” in M. Yrjönsuuri (ed.) 2001, pp. 183–196.

[^read-2010]: –––, 2010, “Inference,” in R. Pasnau (ed.), *The Cambridge History of Medieval Philosophy*, Cambridge: Cambridge University Press.

[^read-2015]: –––, 2015, “ The medieval theory of consequence,” *Synthese*, 187(3): 899–912.

[^schupp-1993]: Schupp, F., 1993, “Zur Textrekonstruktion der formalen und materialen Folgerung in der kritischen Ockham-Ausgabe,” in K. Jacobi (ed.) 1993, pp. 213–221.

[^shapiro-2005]: Shapiro, S., 2005, “Logical consequence, proof theory, and model theory,” in S. Shapiro, *Oxford Handbook of Philosophy of Mathematics and Logic*, Oxford: Oxford University Press, pp. 651–670.

[^spade-2000]: Spade, P.V., 2000, Introduction to Walter Burley, *On the Purity of the Art of Logic*, New Haven: Yale University Press.

[^spruyt-2003]: Spruyt, J., 2003, “The *Forma-Materia* Device in Thirteenth-Century Logic and Semantics,” *Vivarium*, 41: 1–46.

[^spruyt-2018]: –––, 2018, “Consequence and ‘Cause’: Thirteenth-Century Reflections on the Nature of Consequences,” *Vivarium*, 56 (3–4): 320–339.

[^stump-1982]: Stump, E., 1982, “Topics: their development and absorption into consequences,” in N. Kretzmann, A. Kenny, J. Pinborg (eds.) 1982, pp. 273–299.

[^sundholm-1998]: Sundholm, B. G., 1998, “Inference, consequence, implication: a constructivist’s perspective,” *Philosophia Mathematica*, 6: 178–194.

[^tarski-2002]: Tarski, A., 2002, “On the Concept of Following Logically,” *History and Philosophy of Logic*, 23: 155–196.

[^thom-2007]: Thom, P., 2007, *Logic and Ontology in the Syllogistic of Robert Kilwardby*, Leiden: Brill.

[^thom-2010]: –––, 2010, “Three conceptions of formal logic,” *Vivarium*, 48 (1–2): 228–242.

[^thom-2016]: –––, 2016, “The Syllogism and Its Transformations, ” in C. Dutilh Novaes and S. Read, 2016, pp. 290–315.

[^thom-2019]: –––, 2019, *Robert Kilwardby’s Science of Logic*, Leiden: Brill.

[^uckelman-2016]: Uckelman, S. and Lagerlung, H., 2016, “Logic in the Latin Thirteenth Century, ” in C. Dutilh Novaes and S. Read (eds.) 2016, pp. 119–141.

[^wilks-2016]: Wilks, I., 2016, “ Latin Logic up to 1200, ” in C. Dutilh Novaes and S. Read (eds.) 2016, pp. 94–118.

[^yrjönsuuri-2001]: Yrjönsuuri, M. (ed.), 2001, *Medieval Formal Logic*, Dordrecht: Kluwer.
