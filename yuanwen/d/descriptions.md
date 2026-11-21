# Descriptions
**First published Tue Mar 2, 2004; substantive revision Wed Sep 21, 2022**

*Ludlow, Peter*

The analysis of descriptions has played an important role in debates about metaphysics, epistemology, semantics, psychology, logic and linguistics ever since the publication of Bertrand Russell’s paper “On Denoting,” in 1905.  Despite the apparent simplicity of definite and indefinite descriptions, the past 100+ years have seen heated debates about their proper analysis. For example, some philosophers and linguists treat definite descriptions as referential expressions, others treat them as quantificational expressions, and some treat them as predicational expressions. Other analyses of descriptions have held that the determiners ‘the’ and ‘a’ do not make a semantical contribution, but rather a pragmatic contribution to what is communicated. Some recent work in linguistics has even called into question the idea that definite and indefinite determiners correspond to logical elements in natural language.

As we will see, none of this undermines the idea that some expressions in natural language are referential and others quantificational, or that the analysis of these questions isn’t relevant to Russell’s epistemological and metaphysical projects, but it is to suggest that the role of the English words ‘the’ and ‘a’ (and their counterparts in other languages) may be less clear than philosophers in the century following Russell’s paper have imagined.

## 1. What are Descriptions?

Ordinarily, when philosophers talk about descriptions, they have two kinds of expressions in mind: definite descriptions—understood to be phrases of the form ‘the *F*’ (and their equivalents in other languages), and indefinite descriptions—understood to be phrases of the form ‘an *F*’ (and their equivalents in other languages). As we will see, this way of carving up the kinds of descriptions is far too simple. First, there are many kinds of expressions that appear to have this form but that are often argued not to be descriptions. For example, in the expression ‘John is a lawyer’ it is often claimed that ‘a lawyer’ is not a genuine description, but is rather something different—a predicate for example.

Second, it is arguable that there are many expressions having surface forms quite different from ‘the *F*’ or ‘an *F*’ that could count as being descriptions. For example, it seems quite plausible that possessives like ‘my father’ are descriptions (as in ‘the father of me’). Russell also proposed that ordinary proper names could be construed as definite descriptions in disguise. Thus a name like ‘Aristotle’ might be taken as shorthand for ‘the student of Plato who taught Alexander, wrote The Nichomachean Ethics etc.’. Furthermore, as we will see, it has been argued that pronouns like ‘it’ might “stand proxy” for descriptions. So, for example, the pronoun in (1) might be taken to stand proxy for the corresponding definite description (indicated by square brackets) in (1′).

> (1) A man came in the room. He turned on the TV.

> (1′) A man came in the room. [The man who came in the room] turned on the TV.

Similarly, Ludlow (2001)[^ludlow-2001] suggested that temporal anaphors like ‘then’ and modal anaphors like ‘that’ (in ‘that would have been unfortunate’) are descriptions in disguise.

Finally, as noted above, some recent analyses of descriptions have converged on the view that the contributions the determiners ‘the’ and ‘a’ make are not semantical, but rather pragmatic or even syntactic in nature. All of these possibilities will be discussed in due course, but for now we will begin with the analysis of ‘the *F*’ and ‘an *F*’ first taken up in Russell (1905, 1919)[^russell-1905][^russell-1919].

## 2. Russell’s Theory of Descriptions

The key idea of Russell’s proposal is that a sentence like (2) containing an indefinite description, is understood to have the logical form in (2′),

> (2) An *F* is *G*.

> (2′) ∃*x*(*Fx* & *Gx*)

and a sentence like (3) containing a definite description is understood to have the logical form in (3′).

> (3) The *F* is *G*.

> (3′) ∃*x*(*Fx* & ∀y(*Fy* → x=y) & *Gx*)

Boiled down to its simplest non-technical form, the idea is that an expression of the form in (3) is shorthand for the conjunction of three claims:

> (3a) There is an *F*.
> (3b) At most one thing is *F*.
> (3c) Something that is *F* is *G*.

(Following Neale (1990)[^neale-1990] we will find it useful to substitute (3c′) for (3c), which retains Russell’s truth conditions and (as we will see) allows us to extend the theory to plural descriptions in a natural way.)

> (3c′) Everything that is *F* is *G*.

Thus tweaked, Russell’s analysis is that the semantics of a definite description in a sentence involves an *existence claim*, a *uniqueness claim*, and a *maximality claim*.

## 3. Motivations for Russell’s Theory of Descriptions

There are three main motivations for the theory of descriptions; the first is metaphysical, the second involves semantical concerns in the philosophy of language, and the third is epistemological.

### 3.1 Metaphysical motivations for Russell’s theory of descriptions

Consider a negative existential sentence like (4).

> (4) The present king of France does not exist.

Because definite descriptions are devices of quantification on Russell’s view, they can enter into scope relations with other operators—in this case, for example, negation. Accordingly, there is a kind of ambiguity in (4): on one reading it can be interpreted as asserting that it is not the case that the present king of France exists, while on another reading it can be interpreted as asserting, about the present king of France, that he doesn't exist. These two reading can be captured by a difference in logical form, i.e., by representing the difference using the following two logical forms.

> (4a) not ([the *x*: *x* is a present king of France] *x* exists)

> (4b) [the *x*: *x* is a present king of France] not (*x* exists)

Here we are using the *restricted quantifier* notation adopted in Neale (1990)[^neale-1990]. So for example, we read:

> (5) [the *x*: *Fx*](*Gx*)

as saying “the *x* such that *x* is *F*, is such that *x* is *G*”. The material in the square brackets gives the *restriction* on the quantifier, and the formula in parentheses after the bracket constitutes the scope of the restricted quantifier. (We sometimes drop the outer parentheses when it is clear what the scope of the restricted quantifier is, and we sometimes add parentheses around the entire formula for disambiguation.) Thus, (4a) captures the fact that the negation has wide scope in a manner that can be glossed thus: it is not the case that the *x* such that *x* is the present king of France exists. Whereas (4b) gives the restricted quantifier wide scope, in a manner that can be glossed this way: the *x* such that *x* is the present king of France does not exist.

If one wants to avoid the ontological entanglements of nonexistent objects, then one is free to say that (4b) is false (since it involves quantifying over things that don’t exist) but that (4a) is true (since it is not the case that there is a present king of France). What is negated in (4a) is not a claim about some particular individual, but rather a general claim about the world—in effect a claim that the world contains exactly one individual that is presently the king of France and that whoever is presently the king of France exists.

### 3.2 Semantical motivations for Russell’s theory of descriptions

Russell also had a number of concerns that today we might call “semantical”. Consider the expressions ‘the Morning Star’ and ‘the Evening Star’. Both refer to (or at least denote) the planet Venus, but there are contexts in which it seems incorrect to say that they have the same meaning. For example, it was an astronomical discovery that the Morning Star was identical to the Evening Star, so it would be odd to treat an expression like ‘The Morning Star is the Evening Star’ as merely asserting some object to be self-identical. In a similar vein, if we utter (6),

> (6) George wondered whether the Morning Star is the Evening Star.

we are most likely not saying that George was curious about whether Venus was identical to itself.

Frege proposed that that the solution to this puzzle involved the introduction of senses—abstract objects that fix the referents of these expressions, each having a different cognitive significance. In the case of (6), the Fregean solution would be to say that there are different senses attached to ‘the Morning Star’ and ‘the Evening Star’. If we take these expressions to be standing proxy for definite descriptions, then (6) can be unpacked as in (6′).

> (6′) George wondered whether the star that appears in the morning is identical to the star that appears in the evening.

Russell saw that scope relations are relevant here. So, for example, sentences like (6) evince what are sometimes called *de dicto*/*de re* ambiguities. There are circumstances under which George has some object in particular in mind and is wondering, of that object, whether it is the star that appears in the evening. We can use (6) to report this fact as well; In this case we may think of the description as taking wide scope relative to the propositional attitude verb ‘wondered’ yielding a logical form like (7).

> (7) The star *x* that appears in the morning is such that George wondered whether *x* is identical to the star that appears in the evening.

Alternatively, if George has gone mad and is in fact wondering about the law of identity, this may be represented as in (8), where both descriptions have wide scope.

> (8) The star *x* that appears in the morning is such that the star *y* that appears in the evening is such that George wondered whether *x* is identical to *y*.

These considerations speak to a particular semantic consequence, but as Coppock (forthcoming) notes, the analysis of descriptions has also become an inflection point in global disputes around semantic frameworks. For example Coppock notes that the analysis of descriptions may provide evidence in the choice between Situation Semantics (and presumably, Davidson-style event-based semantic theories) and Dynamic Semantics.

### 3.3 Epistemological motivations for Russell’s theory of descriptions

Metaphysical and semantical concerns were important to Russell in his 1905 paper, but epistemological concerns were no less significant. This became particularly clear when he authored his (1910–11) paper “Knowledge by Acquaintance and Knowledge by Description.” In that paper, Russell distinguished between objects that we are directly acquainted with and objects that we only know under a description. So, for example, I might know myself by acquaintance, but I know the tallest man in Iowa only under a description.

Ludlow (2002)[^ludlow-2002] argued that the Cartesianism in Russell’s psychology and epistemology led him into difficulties here. The problem is that we can be in error as to whether we are directly acquainted with someone (did I really have lunch with a colleague or was that a sophisticated hologram?) and this concern (coupled with the Cartesianism that Russell held at that point in his career) propelled Russell to radically minimize the class of cases where we have acquaintance—down to what he called “egocentric particulars,” which is basically to say I’m only acquainted with myself and sense data. This in turn led Russell to extend the theory of descriptions to almost all uses of names—treating them as definite descriptions in disguise.

Russell could have saved himself from some of the more troubling consequences of his view if he had jettisoned the Cartesianism and opted for a more liberal notion of acquaintance. Alternatively, if Hawthorne and Manley (2012) are correct, the true mistake would have come in at the beginning—with the linking of acquaintance and reference. In their view a case can be made that reference comes much cheaper than Russell imagined. It would follow that descriptions need not be relied upon as heavily as he imagined

## 4. Extensions of the Theory of Descriptions

The analysis of descriptions has been extended from canonical examples of descriptions (expressions of the form ‘the *F*’ and ‘an *F*’) to expressions that don’t have this surface form. As we noted in section 3, one of the key motivations for Russell’s theory of descriptions was the idea that it could ameliorate the problem of non-denoting expressions—expressions like ‘the golden mountain’, and ‘the present king of France’. But the account has been extended to other constructions as well, including proper names, pronouns, and temporal anaphors, all with mixed results.

### 4.1 Descriptive theories of proper names

If the theory of descriptions can unburden us metaphysically in the case of nondenoting expressions like ‘the present king of France’ can it do the same for us with nondenoting names like ‘Pegasus’? Perhaps, but there is no shortage of difficulties.

One problem has to do with the fact that there is often no single shared description for certain fictions. Even a simple case like ‘Santa Claus’ presents difficulties here. Many people will associate many different descriptions with the name ‘Santa Claus’. Which, if any of those descriptions is the correct one, and in what sense can we say that all the people deploying the name ‘Santa Claus’ and associating different descriptions with the term are talking about the same thing? Complicating the matter further, others might not use the term ‘Santa Claus’ but a name like ‘Saint Nick’ or ‘Babbo Natale’, and associate those terms with descriptions that converge to some degree with typical Santa descriptions.

At best the Russellian can argue that others are in the same boat here. Consider the option of non-existent objects. If such objects are individuated by their properties then we can again ask which properties the non-existent object Santa Claus is supposed to have. And is the Italian who deploys the term ‘Babbo Natale’ talking about the same nonexistent object as an American that deploys the name ‘Santa Claus’? (See Everett and Hofweber (2000) and French and Wettstein (2001) for papers on these general issues, and see Zalta (1983, 1988)[^zalta-1983][^zalta-1988] for a robust defense of the nonexistent object strategy).

On the face of it then, a naïve application of the descriptive theory of names faces some serious difficulties. Devitt and Sterelney (1998, 48 ff.) catalogue them as follows:

- *The principled basis objection*. There are a number of different descriptions that people might associate with a name like ‘Aristotle’. An historian might favor the description of ‘the teacher of Alexander the Great’, a Catholic Church historian might know him under the description of ‘the leading influence on Saint Aquinas’, some philosophers might know him under the description of ‘the pupil of Plato and author of *The Metaphysics* and *The Nichomachean Ethics*’, Plato himself might have known him under the description ‘the obnoxious student of mine.’ Which of these descriptions is the correct one, what is the principled basis that determines which description is correct?
- *The unwanted ambiguity objection*. Suppose that we respond to the principled basis objection by letting many flowers bloom. That is, suppose we argue that there is no single correct description associated with the name but there are many. We now run into the teeth of the problem of unwanted ambiguity. Are there really that many different names, each corresponding to an different description? If so, why does ‘Aristotle was Aristotle’ seem so much less informative than ‘the teacher of Alexander the Great was the leading influence on Saint Aquinas’?
- *The unwanted necessity objection*. Consider a sentence like ‘Aristotle taught Alexander the Great’. This seems to be a contingent claim—one that is true but matters could have gone otherwise. Aristotle could have decided it was immoral to take the position, or Phillip of Macedonia could have decided that Aristotle was not the best tutor for his young Alexander. We can imagine numerous possible worlds in which the sentence turns out to be false (unlike necessary claims like ‘5+7=12’ which appear to be true in every possible world). But now consider this sentence with the description unpacked. We get something like ‘The pupil of Plato and teacher of Alexander the Great taught Alexander the Great’, and it seems that this would have to be true in every world in which someone satisfies the relevant description. The problem is that the Russellian analysis seems to turn a contingent proposition into a necessary proposition.

Searle (1958, 1969; 162 ff.) offers some modifications designed to overcome these difficulties with the descriptive theory of names. Consider a name like ‘Socrates’. Is it really part of the meaning of that name that its bearer drank hemlock, taught Plato and did all of the other things that we are told that he did when we study the history of philosophy? Searle suggests that we needn’t associate the meaning of a name with a description that contains all of these elements—it might be enough that most of them hold, or that a suitably weighted bundle of them hold. (Other versions of this idea were proposed in Strawson (1959; 180 ff.) and Wilson (1959)[^wilson-1959].)

How does Searle’s proposal help with the objections just listed? The unwanted necessity objection collapses immediately because the use of a name does not commit the speaker to the object in question having all the properties in the bundle. When I say Aristotle authored the *Nichomachean Ethics* it is as though I uttered the following:

> (9) The individual who is associated with some significant number of these properties (taught by Plato, taught Alexander, wrote the *Nichomachean Ethics*, etc.) wrote the *Nichomachean Ethics*.

Someone might be associated with this bundle of properties and not have written the *Nichomachean Ethics* (so long as they had enough of the other properties).

The *principled basis* objection is supposed to collapse because there is now no issue of choosing which description is the correct one—if the theologian, the historian, and the philosopher all associate different descriptions and hence different properties with Aristotle, all of those properties will make it into the bundle of properties for the name ‘Aristotle’. We don’t need to worry about the principled basis for choosing the relevant properties because we don’t have to choose period. We take them all.

The *unwanted ambiguity* objection is supposed to collapse because every use of the name ‘Aristotle’ is now associated with the same bundle of properties. ‘Aristotle is Aristotle’ is uninformative because it is shorthand for (10).

> (10) The individual who is associated with some significant number of these properties (taught by Plato, taught Alexander, wrote the Nichomachean Ethics, etc.) is the individual who is associated with some significant number of these properties (taught by Plato, taught Alexander, wrote the Nichomachean Ethics, etc.).

As compelling as Searle’s proposal may seem at first blush, it soon runs into problems of its own. As Devitt and Sterelny observe, the three objections to the traditional descriptive theory of names come creeping back. For starters, one presumably doesn’t want every single fact about Aristotle to make it into the bundle of properties that we associate with his name (that would lead us down the path to an extreme holism in which every fact that we acquire changes the meaning of the name), so what is the principled basis for deciding what goes into the bundle? Worse, what is the principled basis by which we weight the importance of the properties in the bundle?

The unwanted ambiguity objection returns as well if we allow that different people will associate different bundles of properties with a name or at least weight those properties differently. One might be tempted to dodge this problem by arguing that the relevant bundle of properties for a name is socially fixed and does not vary between individuals, but then it is hard to see how names like ‘Scott’ and ‘Sir Walter’ could be associated with different bundles of properties since the community as a whole is likely to attribute the same bundle of properties (with the same weights) to these names. This is a problem, because different bundles of properties are needed to distinguish the differences in cognitive significance between ‘Scott’ and ‘Sir Walter’. There is a dilemma then: one can avoid the problem of unwanted ambiguity only at the expense of the problem of accounting for the cognitive significance of names.

Finally, as Kripke (1980)[^kripke-1980] argued, Searle’s solution really doesn’t help with the problem of unwanted necessity. Aristotle might have had none of the properties that we ordinarily associate with his name. Searle certainly didn’t think this was possible—for him, if nothing had the properties in question (or enough of them) then Aristotle did not exist. But Kripke (ch. 2) enlisted a number of arguments to show that the behavior of names in modal environments suggests otherwise. For example even if we concede that Aristotle did all the things he was supposed to have done, it is still the case that Aristotle could have refrained from doing any of the things he did. He could have forsaken philosophy for other pursuits. He could have been run over by a chariot at age two. But then how do we make sense of a descriptive name in a sentence like (11)?

> (11) It could have happened that Aristotle was run over by a chariot at age two.

If the description is unpacked, we get something like (11′).

> (11′) It could have happened that the philosopher who was taught by Plato, taught Alexander, etc. was run over by a chariot at age two.

But (11′) is false. There is no nearby possible world where Aristotle did all those things by age two.

Kripke held that the behavior of names in these environments could only be explained if we think of the names as being rigid designators—i.e., as devices that rigidly pick out an individual across possible worlds. Kripke also stressed that this is not really a point about conditional or modal sentences—the same point can be made for simple declarative sentences evaluated in a counterfactual situation. So, for example, take a simple sentence like (12).

> (12) Aristotle was run over by a chariot at age two.

We can evaluate this sentence in other possible worlds. We can say that it might have been true under certain circumstances. But it does not seem plausible that there is a nearby possible world where the following is true.

> (13) The philosopher who was taught by Plato, taught Alexander, etc. was run over by a chariot at age two.

Finally, Donnellan (1972) and Kripke (1980)[^kripke-1980] both argued that the Descriptive Theory of Names suffers from an important epistemological defect. The descriptions that we associate with names routinely do not describe the individuals that we intend to refer to. Asked to come up with a description to substitute for the name ‘Einstein’, many people would write ‘The inventor of the atom bomb’ (which of course he was not). Others might write ‘the inventor of the theory of relativity’, but then asked what the theory of relativity was would respond ‘the theory that Einstein invented’. The descriptive information that we associate with names just is not sufficient to pick out the intended referent.

Kripke’s positive proposal—suggestion really—was that names are associated with a causal chain; there is an initial baptism of an individual (e.g., Albert Einstein as ‘Albert Einstein’) and that referent is passed along to other users of the name. Likewise the referent of ‘Aristotle’ is not fixed by some description, but by a causal chain linking our use of ‘Aristotle’ with some historical individual. (This is not the place for an extended discussion of this proposal, but see Devitt 1981 and Salmon 1991 for development of this idea and Evans (1973, 1980)[^evans-1973] for criticism.)

In spite of the great force of Kripke’s criticism of the descriptive theory of names, there have been some significant attempts to answer them. One idea (explored by Loar (1976)[^loar-1976], McDowell (1977)[^mcdowell-1977], and Schiffer (1978)) would have the description be something like ‘the individual designated by the name ‘Aristotle’. For Kripke (1980)[^kripke-1980], and Devitt (1981)[^devitt-1981] this sort of approach was hopelessly circular. Indeed, Devitt and Sterelny disparagingly referred to the position as “circular descriptivism” (but see Kroon (1989)[^kroon-1989] for an attempt to disarm the circularity charge). Another idea (taken up in Kroon (1987)[^kroon-1987] and Jackson (1998)[^jackson-1998]) was to build reference to the causal chain into the description itself. Thus, ‘Aristotle’ might stand proxy for ‘the individual linked by a causal chain to ‘Aristotle’’ (this view was dubbed “causal descriptivism” by Lewis (1984)[^lewis-1984]). Whatever the merits of these views, they clearly abandon some of the key motivations for the descriptive theories of names—in particular the idea that the description could do the work of providing the sense of the name.

Still, from a linguistic point of view, we should note that there are features of names in natural language that make them appear to be similar to descriptions. Names can take determiners like ‘a’ and ‘the’ (indeed in some languages they routinely do so), which suggests that they are behaving more like nouns than like saturated referring expression. Indeed it is a widespread linguistic analysis of names that they have possibly empty determiner positions, so that a name like Aristotle has at a minimum the following structure, which represents a syntactic structure for a determiner phrase having an empty determiner and the noun ‘Aristotle’ as constituents:

> [_{DP} [_{Det} ∅ ] [_{N} Aristotle]]

In addition, Burge (1973)[^burge-1973] offered a number of arguments in support of the idea that names really are predicates, and further support has come from Hornsby (1976)[^hornsby-1976], Larson and Segal (1995) and Eluguardo (2002)[^eluguardo-2002]. (But see Boer (1975), Bach (1987)[^bach-1987], and Higginbotham (1988)[^higginbotham-1988] for criticism.)

The Burge story had the determiner as something like a bare demonstrative. It is not a long step to the supposition that the default interpretation of the null element is to treat it as the definite determiner ‘the’. This is in effect the proposal offered in Larson and Segal (1995); ‘Aristotle’ stands in for an incomplete definite description of the form ‘the Aristotle’. In both cases, the predicate in question would be something like being named ‘Aristotle’, so again it is difficult to see how this general approach (without emendation) can satisfy Russell’s desiderata that the description play the role of senses.

An alternative riff on these ideas which has been widely discussed, but not, so far as I know, published, would be to suppose that there is a rigid property of being Aristotle—one that only Aristotle could have in any possible world (this property would be completely independent of being named ‘Aristotle’). The idea is that the content of the description could consist solely of that property. For example, when we say that ‘Aristotle might have been run over by a chariot’ we would in effect be saying there is a possible world in which the unique individual who has the property of being Aristotle was run over by a chariot. It seems that charges of circularity are not so easily advanced here, although the view does raise questions about the nature of these rigid properties and our epistemic access to them. (See Parsons (1982)[^parsons-1982] for an account of the logic of rigid properties.)

Another class of responses has attempted to retain the standard descriptive content of names but moved to circumvent Kripke’s modal worries. Dummett (1973; 111–135, 1981) and Sosa (1996; ch. 3, 2001) proposed that the behavior of names in modal contexts can be accounted for if we take names to be descriptions with mandatory wide scope. So, for example, (11) could be taken to have the following logical form.

> (11″) [The *x*: *x* taught Alexander etc.] possibly (it was the case that *x* was run over by a chariot at age two)

Kripke discussed this possibility briefly in the Preface to (1980), holding that the move overlooks the fact that we can simply evaluate (12) in other possible worlds, hence no embedding within modal operators is really necessary. For that matter, consider a sentence like ‘(12) might have been true’. How does a wide scope story help us in this case? More recently, Soames (2002; ch. 2) has expanded on Kripke’s points and marshaled a number of additional arguments against the wide scope thesis, including the observation that if one embeds a name within a propositional attitude environment and in turn embeds the propositional attitude in a modal environment then one is in the peculiar position of needing the description to escape the modal environment (to honor the rigidity facts) but not escape the propositional attitude environment (to honor the ‘Scott’/‘Sir Walter’ cases that Russell (1905)[^russell-1905] employed to motivate the descriptive theory of names). In other words, the description theorists need to have their cake and eat it too.

Another possibility (considered in Nelson (2002)[^nelson-2002]) would be to argue that names are “rigidified descriptions” (i.e., descriptions like ‘The individual who actually was a student of Plato, taught Alexander, etc.’ or perhaps rigidified causal descriptions. This general strategy is criticized by Soames (2002; ch. 2), who argues that ‘the actual *F* is *G*’ and ‘*n* is *G*’, where *n* is a name, do not express the same proposition. The argument for this turns on cases where these expressions are embedded in propositional attitude environments, as in (14a) and (14b).

> (14a) Smith believes that *n* is *G*.
> (14b) Smith believes that the actual *F* is *G*.

According to Soames, there are contexts of utterance and worlds of evaluation where (14a) is true but (14b) is false. Accordingly, ‘the actual *F* is *G*’ and ‘*n* is *G*’ cannot express the same proposition. Hence names cannot be rigidified descriptions. See Nelson (2002)[^nelson-2002] for a response to this argument. (Accounts of rigidified descriptions have been offered elsewhere, see for example Zalta (1988; chapter 5), but typically not as a way to account for the behavior of descriptions in propositional attitude environments.)

Yet another approach to defending descriptions would be to employ a “2-dimensionalist” semantics (in the sense of Stalnaker (1978, 1990)[^stalnaker-1978][^stalnaker-1990], Davies and Humberstone (1980)) to account for the behavior of descriptive names in modal environments. Some form of this idea has been offered by Evans (1982)[^evans-1982], Stanley (1997a, 1997b)[^stanley-1997b], Chalmers (2000, 2002)[^chalmers-2002], and Jackson (1998)[^jackson-1998]. Here the basic idea is that the content of a description picks out different contents in different possible worlds. Accordingly, if we want to evaluate the descriptive content of ‘Aristotle’ in another possible world, we do not use the descriptive content ‘student of Plato…’ in every world, since that is only an appropriate descriptive content for some worlds. In other worlds we will draw on other descriptive contents. As Jackson (1998, 112)[^jackson-1998] puts the idea:

> If speakers can say what refers to what when various possible worlds are described to them, description theorists can identify the property associated in their [the speaker’s] minds with, for example, the word ‘water’: it is the disjunction of the properties that guide the speaker in each particular possible world when they say which stuff, if any, in each world counts as water. This disjunction is in their minds in the sense that they can deliver the answer for each possible world when it is described in sufficient detail, but it is implicit in the sense that the pattern that brings the various disjuncts together as part of the, possibly highly complex, disjunction may be one they cannot state.

Soames (2009)[^soames-2009] has responded that this particular 2-dimensionalist approach is tantamount to the claim that descriptive theories of reference determination are priori irrefutable, since any evidence that a term refers to an object is automatically taken to demonstrate the existence of an implicit description in our minds that successfully determines reference, whether or not we can successfully state it. Additional criticism of 2-dimensionalism criticism can be found in Block and Stalnaker (1998) and Byrne and Pryor (2006).

### 4.2 Descriptive theories of pronominal anaphora

Consider sentence (1) again.

> (1) A man came in the room. He turned on the TV.

One of the arguments that Strawson (1952)[^strawson-1952] enlisted on behalf of the referential theory of descriptions was the following. Since the pronoun in (1) gets its content from the description that it is anaphoric on, and because the pronoun refers, it must be the case that the description also refers. Strawson’s idea was that descriptions refer because their anaphoric pronouns do.

There are obviously two responses to Strawson here. One may either reject the idea that the content of the pronoun is in some sense dependent upon the description (for example, one might claim it independently picks out some object raised to salience (Lewis 1979)[^lewis-1979], one might claim that it is a bound variable (Geach 1962)[^geach-1962]), or one can argue that the pronoun is a kind of definite description in disguise. This third idea has been explored by Parsons (1978, Other Internet Resources), Cooper (1979)[^cooper-1979], Davies (1981)[^davies-1981], Neale (1990, ch. 6), Heim (1990)[^heim-1990], Ludlow (1994)[^ludlow-1994], van Rooy (2001)[^rooy-2001], and Elbourne (2005)[^elbourne-2005] (the view is sometimes attributed to Evans (1977), but it is more accurate to say that he thought the pronouns had their references fixed rigidly by descriptive content). As noted above, the basic idea is that the pronoun in (1) may stand proxy for the square-bracketed definite description in (1′).

> (1′) A man came in. [The man who came in the room] turned on the TV.

The philosophical attraction of this view should be obvious. What it allows us to do is to make sense of cases where we employ nondenoting pronouns in negative existentials, belief reports, and fictional contexts. Examples would be the following:

> (15) The present king of France doesn’t clean my pool. He doesn’t exist, either.
>
> (16) Mary believes that the present king of France exists and that he cleans my pool.

Clearly if these pronouns are referring expressions then any victories won through the theory of descriptions are going to be fleeting. In effect, all the unwelcome metaphysical commitments that we banished by using descriptions would re-enter via the back door as soon as we employ anaphoric pronouns in our discourse. But if we treat anaphors as standing proxy for descriptions, the back door is blocked as well.

Consider an example like (16), with the descriptive material spelled out.

> (16′) Mary believes that ([the *x*: *x* is a present king of France](*x* exists) and [the *x*: *x* is a present king of France & *x* exists](*x* cleans my pool))

Mary’s belief is strange, but general for all that, so we can report it without being committed to the existence of a present king of France.

Nor is this strategy necessarily limited to pronominal anaphora. Ludlow (1999, 2000)[^ludlow-1999] has argued that temporal and modal anaphora can be handled in a similar manner. In effect, one can take a temporal anaphor as standing proxy for a when-clause and a modal anaphor like ‘that’ in ‘that would have hurt’ as standing proxy for the antecedent of a conditional.

To illustrate, consider an example like (17), due to Partee (1972).

> (17) I turned the stove off.

Now clearly this does not mean that I turned the stove off once in my life, but rather there is intuitively some relevant time when I turned it off—for example, when I left the house this morning. The standard analysis would have it that I refer to a past time or past time interval here, but such an analysis does not go down well with presentists, who do not believe that there are such intervals, and at a minimum we might think there is something epistemologically troubling about referring to past and future times (to see this, consider what a Russellian might say, given that some notion of direct acquaintance is required on the Russellian view). An alternative would be to suppose that the implicit temporal anaphora here can be accounted for by the introduction of descriptive material—an explicit temporal when-clause—as in (18), for example.

> (18) I turned the stove off [when I left the house this morning].

The presentist can then treat ‘when’ as a primitive tense that holds between propositions. (See Ludlow (1999)[^ludlow-1999] for discussion of difficulties with this strategy.) As in the pronominal anaphora case, descriptive material does the work that reference does in most other accounts of the semantics of temporal and modal discourse. Again, the goal is metaphysical austerity and faithfulness to our epistemic position.

Clearly descriptive anaphora represents a powerful extension of Russell’s theory of descriptions and a useful tool for presentists and modal antirealists. For all of that, the theory has encountered a number of objections. Consider (19), for example, and a paraphrase (20) in which the pronoun is rendered as a description.

> (19) If a man enters the room, he will turn the switch.
>
> (20) If a man enters the room, the man who enters will turn the switch.

Heim (1982)[^heim-1982] observed that (20) (unlike (19)) implies that a unique man entered the room and that (20) will therefore be false if two men enter the room. The question is, is there some way to answer this objection and retain the descriptive analysis of anaphora? Davies (1981)[^davies-1981], Lappin (1989)[^lappin-1989], Neale (1990, chapter 6), Krifka (1996)[^krifka-1996], and Yoon (1996)[^yoon-1996] explored the possibility that the descriptive pronouns are in fact numberless—that is, the pronoun in (20) might in fact be proxy for something like ‘the man or men who enter’. (See Kanazawa (2001)[^kanazawa-2001] for a literature review and criticism of this idea.)

Another idea, considered in Heim (1990)[^heim-1990], Ludlow (1994)[^ludlow-1994], and Elbourne (2005)[^elbourne-2005] is to see how descriptive theories of pronouns fare when embedded within an event-based (or situation based) theories of conditionals like those articulated by Berman (1987)[^berman-1987], Kratzer (1989)[^kratzer-1989], and Lycan (1984)[^lycan-1984]. On an event-based analysis of conditionals, we would expect a treatment of (19) along the lines of (21).

> (21) For every minimal event/situation in which a man enters the room, he flips the switch in that event/situation.

Sentence (21) seems to accurately reflect the truth conditions of ‘He will turn the switch’, even in the case where two men turn the switch simultaneously. To see this we need merely recognize that even though two men (say Ralph and Norton) may turn the switch simultaneously, it is still the case that we can recognize two independent minimal events; one where Ralph turns the switch and one where Norton turns the switch. The strategy is to show that the supposed loss of uniqueness is an epiphenomenon, and is due to the fact that the descriptive pronoun’s denotation is relativized to events.

Unfortunately, there are more sophisticated versions of these cases where simple relativization to events will not do. These include the sage plant examples discussed in Heim (1982, 1990)[^heim-1982][^heim-1990] and Kadmon (1990)[^kadmon-1990].

> (22) If a man buys a plant he buys nine others along with it.

Here the problem is that the minimal event appears to contain ten sage plants, so we are left to ask how the pronoun, rendered as a definite description complete with a uniqueness claim, is supposed to work. There is no unique sage plant in the minimal events. Or at least a more detailed story needs to be told.

Finally, there is (23). (Heim (1990)[^heim-1990] attributes the example to Hans Kamp and Jan van Eijk).

> (23) If a bishop meets another bishop, he blesses him.

The interesting feature of this example is that the uniqueness implications of the definite descriptions remain problematic, for they imply that there is a unique satisfier of the description in each event. But notice that because the bishops bless each other, it appears there is no unique individual that satisfies either description in the consequent of (23 ). This class of problems, sometimes called *bishop sentences*, has yielded a number of proposed solutions. For example, Elbourne (2005)[^elbourne-2005] has argued that the minimal situation story can suffice if there are subsituations containing only one bishop. Here is a crude version of the idea: If there is a subsituation s1 with only one bishop and a subsituation s2 with one different bishop, there could be a containing situation s0 in which the bishops from those subsituations bless each other (see Kroll (2008)[^kroll-2008] and Elbourne (2009, 2010)[^elbourne-2009][^elbourne-2010] for further discussion).

An alternative idea is to treat the pronoun in these cases as semantically akin to an indefinite description rather than a definite description. (See Groendijk and Stokhof (1991), Chierchia (1996), van der Does (1994), and also see van Rooy (2001)[^rooy-2001] for criticism. The proposal in King (1978) has a similar effect.) If we make this move, then (24) might be glossed as in (24′).

> (24′) If a bishop meets another bishop, a bishop that meets another bishop blesses a bishop that is met by another bishop.

Similarly, the sage plant example in (23) would receive the gloss in (23′).

> (23′) If a man buys a sage plant he buys nine others along with a sage plant he bought.

Such solutions thus surrender the uniqueness entailment in Russell’s proposal (we will return to this idea in section 6.1). Of course, as Kadmon (1990)[^kadmon-1990] stressed, pronouns typically do appear to introduce uniqueness, as an example like (25) shows.

> (25) Leif has a chair. It is in the kitchen.

Notice that the first sentence doesn’t introduce uniqueness, so the pronoun introduces something that indefinites do not. What this means is that whatever account we give of pronouns—through dynamic semantics or whatever—we will want to account for this variation in interpretation in a principled way. We want to know precisely why a pronoun looks like a definite description here, but an indefinite description there. Whether extant accounts are satisfactory in this respect is subject to debate.

Of course, none of this is to say that solving this problem will close the book on the analysis of descriptive pronouns. A number of other puzzles remain, including the problem of pronominal contradiction, which has been discussed by Strawson (1952)[^strawson-1952], Davies (1981)[^davies-1981], Ludlow and Neale (1991), and van Rooy (2001)[^rooy-2001] among many others. Consider the following brief dialogue.

> A: A man fell in front of the train.
> B: He didn’t fall, he was pushed.

The problem is that if the pronoun is to have its descriptive content recovered from previous discourse, the pronoun ‘He’ is going to stand proxy for a description like ‘the man who fell in front of the train’ or ‘a man who fell in front of the train’. Here, considerations about uniqueness implications are of little help. One possibility, advocated by Davies (1981)[^davies-1981] and Ludlow and Neale (1991) is to say that speaker B is engaged in a kind of pretense—playing along with speaker A, as if saying with scare quotes something like B′.

> B′: The “man who fell in front of the train” didn’t fall, he was pushed.

Other strategies are also in play, for example one might ignore the descriptive content of the antecedent and build the content out of thematic roles like agent and theme (Ludlow 1994)[^ludlow-1994] or phi-features represented in the pronoun like gender (‘she’ as “the feminine entity”; Ahn 2019)[^ahn-2019], or perhaps metalinguistic material (“the person you spoke of”). Whatever the ultimate disposition of these cases, it is fair to say that there are more issues here than whether pronouns are to be treated as standing proxy for definite descriptions or indefinite descriptions.

### 4.3 Indefinite descriptions

Most of the action in the philosophy of language has been with definite descriptions, but indefinite descriptions have also generated a fair bit of attention—some of it mirroring the debates about definite descriptions. For example Chastain (1975)[^chastain-1975], Donnellan (1978)[^donnellan-1978], Wilson (1978)[^wilson-1978], and Fodor and Sag (1982), held that indefinite descriptions are ambiguous between referential and quantificational interpretations. That is to say, there are referential and quantificational uses of indefinite descriptions and these are a reflex of a genuine semantical ambiguity. The basic structure of their argument was the following. Referential uses of indefinites must be either a function of quantifier scope or a semantically referential indefinite determiner. Since indefinites with the relevant scopal properties would violate standard syntactic constraints, indefinites must in some cases be semantically referential.

Examples of the kinds of syntactic considerations they had in mind include island constraints like the following. Quantified expressions are ordinarily considered to be clause bound. So, for example, a sentence like (26) is not supposed to have the interpretation in (26′), where the quantified expression takes wide scope.

> (26) Someone believes that every man I know is angry.
>
> (26′) \*[every *y*: man(y) and know(I,*y*)]([Some *x*: person(*x*)](*x* believes that *y* is angry))

On the other hand, it seems more natural to say that (27) can have the interpretation corresponding to the structure in (27′).

> (27) Everyone believes that a man I know is angry.
>
> (27′) [An *x*: man(*x*) and know(I,*x*)]([every *y*: person(*y*)](*y* believes that *x* is angry))

A more compelling example of an island constraint would be the antecedent of a conditional, as in (28), which is not supposed to have the interpretation in (28′).

> (28) If every person I know is happy then I will be happy.
>
> (28′) \*[every *x*: person(*x*) and know(I,*x*)](if *x* is happy then I will be happy)

But a “wide understanding” of (29) does seem to be possible.

> (29) If a person I know is happy then I will be happy.
>
> (29′) [An *x*: person(*x*) and know(I,*x*)](if *x* is happy then I will be happy)

The moral was supposed to be that these “wide” readings are not the reflex of wide scope quantification (that would be to make indefinite descriptions syntactically special), but rather due to the fact that the indefinites in these examples are referring expressions.

The Fodor and Sag argumentation was taken up in the philosophical literature by King (1988)[^king-1988] and Ludlow and Neale (1991), who argued that there is a confusion in the Fodor and Sag discussion. Kripke’s claim, of course, was that referential uses of a description are a function of pragmatics, not quantifier scope. Nor, of course, could a referential use be associated with wide scope, as Kripke (1977)[^kripke-1977] argued forcefully—they simply are not the same phenomenon. The problem is that the Fodor and Sag arguments do not address the pragmatic account of referential uses, which of course was the alternative advanced by Kripke.

In addition, there do appear to be more quantifier scope possibilities than the Fodor and Sag proposal seems to allow. Consider (30), from Ludlow and Neale and (31) from Kripke.

> (30) Each teacher overheard many exclamations that a student of mine cheated.
>
> (31) Hoover charged that the Berrigans plotted to kidnap a high American official.

In the case of (30) ‘a student of mine’ can have narrow scope with respect to ‘every teacher’ but wide scope with respect to ‘many exclamations’. Similarly, as Kripke (1977)[^kripke-1977] observed, intermediate scope is possible in (24) (as when the Berrigans have someone in mind, but Hoover does not know who). Similar observations about the possibility of intermediate scope have been made by Farkas (1981)[^farkas-1981], Rooth and Partee (1982), King (1988)[^king-1988], Ruys (1992) and Abusch (1994). How are Fodor and Sag supposed to generate readings like that, given only a referential/quantificational ambiguity and no relative scope relations? As Kripke put the point, “no two-fold distinction can replace Russell’s notion of scope.” While this tells against referential analysis of indefinites, it opens a can of worms for the other approaches as well; for example, if indefinite descriptions are ordinary quantified expressions, then why do they have such extraordinary island-escaping properties (or at least appear to)?

One attractive possibility that has emerged from the literature in Discourse Representation Theory—in particular in work by Heim (1982)[^heim-1982], Kamp (1984), Deising (1992), Kamp and Reyle (1993)—has been that the appearance of a determiner in an indefinite description is chimeral—‘a man’ in fact comes to an expression containing a predicate and a free variable, as in ‘man *x*’. This free variable might then be picked up by some sort of discourse operator as discussed in the previous section.

Accordingly, a sentence like (1) might have a logical form, or better, a discourse representation structure akin to (1\*) (abstracting from details).

> (1\*) [[man(*x*) came in the room] [*x* turned on the TV]]

This general strategy gives us some explanation for why indefinites sometimes appear to have island escaping properties as in cases like conditionals. The answer is that they don’t escape at all, but are free variables that are bound by (or existentially closed by) operators outside of the island. This describes the DRT strategy only in the most general of terms, but we can already see that the questions that plague the Russellian story have their reflex here as well. Everyone now recognizes that intermediate scope is a possibility in cases like (30) and (31), but the question is just what mechanisms make it possible? The Russellian has to opt for operators with unusual island escaping properties. What is the DRT theorist to do?

One option, explored by Reinhart (1996), Kratzer (1995)[^kratzer-1995], and Winter (1997)[^winter-1997], employs the device of choice functions. As Winter informally characterizes the doctrine, the idea is as follows.

> (A1) Indefinites lack quantificational force of their own
>
> (A2) An indefinite NP in an argument position, however, ends up denoting an individual, because the semantics involves a free function variable that assigns an individual to the restriction predicate.
>
> (A3) This function variable is existentially closed, together with the restriction that it is a choice function: a function that chooses a member from any non-empty predicate it gets.

How does this help in the case of intermediate scope? For Reinhart (1996), choice functions by themselves cannot account for the extant phenomena (in particular cases of intermediate scope), so the theory must be supplemented with standard quantifier raising accounts as well. Winter (1997)[^winter-1997] has offered a more general account employing choice functions (also extending the account to plural indefinites) that purport to make do without the additional resource of quantifier raising.

The interesting conceptual issue that arises, whether we opt for standard DRT accounts or such accounts supplemented with choice functions, is whether this departs from the Russellian analysis of indefinite descriptions in important ways. In one respect, of course, the accounts are very different—Russell takes indefinite descriptions to be existential quantifiers, while the DRT accounts take them to be akin to free variables. On the other hand, once the free variables are interpreted the effect comes to very much the same thing: in both cases the accounts are fundamentally quantificational.

Not everyone has seen DRT theory and choice functions in this light. Kratzer (1995)[^kratzer-1995] maintained that the choice function provided something like a referential interpretation of an indefinite, here understood as a “pointing gesture within the mind of the speaker,” but as Winter points out this raises some difficult methodological issues, and in the view of Ludlow and Neale (1991) this amounts to a conflation of the notions of referentiality and specificity, and a further confusion about the nature of specificity. On their view, using an expression with a particular individual in mind is not the same thing as referring to that individual. For example, according to Ludlow and Neale, there are a number of possible uses to which we can put indefinite descriptions, including referential uses, specific uses, definite uses, and purely existential uses. To understand this distinction, consider the following cases.

- *Referential use*. A teacher announces the following to the class, with a single red haired student in the front row. “I’m not going to name names, but I have good reason to believe that red haired student in the front row cheated on yesterday’s exam.” In this case the teacher has singular grounds for the utterance, and is communicating directly to the audience the identity of the individual that serves as the grounds for the utterance.
- *Specific use*. In this case the teacher has singular grounds, and wishes to communicate that fact to the audience, but does not wish to communicate the identity of the cheater to the class. “I’m sorry to announce that yesterday I witnessed a student cheating on the exam.”
- *Definite use*: In this case the teacher knows that there must have been a unique cheater, but does not know the identity of the cheater and hence does not have singular grounds for the utterance and accordingly is not in a position to communicate the identity of the cheater except under extraordinary circumstances. “I have statistical evidence that a student cheated on the exam. Fortunately there only appears to be one cheater.”
- *Purely quantificational use*: In this instance not only does the teacher fail to know the identity of the cheater, but also fails to know whether or not there was a unique cheater (perhaps there were several). “I have evidence that a student cheated on the exam. The answer sheet was stolen from my office. Hopefully, there was only one student involved. We will know more pending an investigation.”

According to Ludlow and Neale, it is implausible to think that all of these uses can be chalked up to semantic facts. In each case, the proposition expressed is argued to be that which would be expressed if the indefinite determiner were replaced by the existential quantifier. The different uses of descriptions then stem from the application of Gricean principles of conversational implicature to what was literally said.

### 4.4 Plural, mass, and generic descriptions

So far we have discussed singular definite and indefinite descriptions (and the possibility that names are descriptions) but as it turns out these types of descriptions are probably not the most commonly occurring descriptions in English. Ultimately we also want to take into account plural descriptions (as in ‘the dogs are barking’), mass noun descriptions (as in ‘the water is cold’), and generics (as in ‘the dog is a loyal friend’). The question is whether each of these constructions must be treated in a different way, or whether it is possible to unify their treatment with the analysis of definite descriptions discussed above. Sharvy (1980)[^sharvy-1980] suggested that a unified treatment is indeed possible (this is also a possibility that Chomsky (1975)[^chomsky-1975] saw).

Sharvy’s idea was that we could generalize Russell’s theory of descriptions by ‘the *F* (or *F*s) is (are) *G*’ to be equivalent to the following,

> (32) ∃*x*(*Fx* & ∀*y*(*Fy* → *y* ≤ *x*) & *Gx*)

where *F* can be either a singular count noun (like ‘dog’), a plural count noun (like ‘dogs’) or a mass noun (like ‘water’), and the symbol ‘≤’ indicates a parthood relation. Following Brogaard (2007)[^brogaard-2007] we can take this as saying ‘an *F* that every *F* is part of satisfies “*G*”’. It follows then, that a definite description ‘the *F*’ (‘the *F*s’) denotes the maximal sum or mass in the extension of *F*. So, for example, when we utter ‘The dogs’ we are denoting the maximal set of dogs in the domain of discourse. When we utter ‘the water’, we are denoting the maximal mass of water in the discourse. In the case of singular definite descriptions (like ‘the dog’) we are still denoting the maximal set of dogs in the domain of discourse (since in this case there is only one dog). In effect, singular definite descriptions are just special cases of Sharvy’s generalized theory of descriptions.

Fara (2001)[^fara-2001] argued that the same strategy can be extended to generics as well.

> (33) The dog is related to the wolf.

If natural kinds like species and sub-species can bear the parthood relation to one another, then one can extend the Sharvy parthood operator to these cases as well. I don’t mean to suggest that Sharvy’s analysis of these constructions has no competitors, but the fact that he was able to give a unified treatment of these constructions suggests that competitors will have to do the same. It really does seem as though singular, plural, mass, and generic descriptions are not so different in kind. A unified Russellian treatment of the constructions seems possible. In section 7 we will return to the question of whether the maximality claim should be part of the analysis or whether it represents a weakness in the analysis.

## 5. Objections to the Theory of Descriptions

The theory of descriptions has encountered its fair share of criticism. This criticism has ranged from contentions that Russell simply got the truth conditions wrong in important cases to nagging worries about the details of the proposal—in particular worries relating to the nature of the descriptive content. As we will see, none of these concerns have been completely ameliorated.

### 5.1 The challenge to Russell’s truth conditions

Strawson (1950)[^strawson-1950] objected that Russell’s theory is simply incorrect about the truth conditions of sentences like ‘The present king of France is bald’. According to Russell’s analysis, this sentence is false (since it contains an existence claim to the effect that there is a present king of France), but according to Strawson, this does not conform to our intuitions about the truth of an utterance of that sentence. In Strawson’s view, an utterance of the sentence in a world where there is no present king of France is neither true nor false; perhaps the sentence has a truth value gap, or perhaps it fails to express a determinate proposition (Strawson vacillated on this), but either way it does not appear to be false. Strawson held that this fact supported a referential interpretation of expressions like ‘The present king of France’.

If there is no present king of France, then an utterance containing such an expression is somehow defective. It is as if I looked into my desk drawer, not allowing you to see what I was looking at, and said ‘that is a fine green one.’ Strawson held that utterances like these do not entail the existence of a fine green one or the present King of France, but rather *presuppose* their existence. If the expressions fail to refer, then there is a presupposition failure and the utterance fails to have a determinate truth value. (Notice that this sort of failure is not supposed to undermine the meaningfulness of the sentences that we utter; for Strawson, sentences are meaningful in and of themselves, independently of the utterance situation. Utterances of meaningful sentences may be true or false or, if here is a presupposition failure, they may be neither.)

For his part, Russell (1957)[^russell-1957] argued that, despite Strawson’s protestations, the sentence was in fact false:

> Suppose, for example, that in some country there was a law that no person could hold public office if he considered it false that the Ruler of the Universe is wise. I think an avowed atheist who took advantage of Mr. Strawson’s doctrine to say that he did not hold this proposition false would be regarded as a somewhat shifty character.

Does this whole debate come down to a case of intuition swapping? Thomason (1990; 327) and Soames (1976; 169) seemed to think so, and Strawson himself (1964) also came to doubt whether the entailment vs. presupposition debate could be settled by “brisk little formal argument[s]”. However, Neale (1990)[^neale-1990] maintained that the matter could be settled in Russell’s favor, and supported the claim by collecting a number of previously observed cases in which intuitions about truth conditions clearly do not support Strawson’s view. For example, ‘My mother is dating the present king of France’ seems clearly false, as does ‘The present king of France cleans my swimming pool’, and he concluded that these are clearly cases where the Strawsonian truth conditions have gone awry.

But truth value judgments for cases like this are extremely sensitive. Lasersohn (1993)[^lasersohn-1993], von Fintel (2004)[^fintel-2004], Yablo (2006, 2009)[^yablo-2006][^yablo-2009] and Schoubye (2009, 2011)[^schoubye-2009][^schoubye-2011] have collected a number of examples where subtle changes to the example give rise to different judgments of truth value. Consider the following minimal pairs, where the examples marked with ‘#’ indicate ambivalence about assigning a truth value, and ‘F’ indicates it is more plausible to assign a value of falsehood.

> | (34) | a. | # The present king of France is bald. |
> | --- | --- | --- |
> |   | b. | F The present king of France is a bald Nazi. |
> | (35) | a. | # The present king of France is sitting in a chair. |
> |   | b. | F The present king of France is sitting that chair. |
> | (36) | a. | # The present king of France read *Anna Karenina*. |
> |   | b. | F The present king of France wrote *Anna Karenina*. |
> | (37) | a. | # The present king of France heard about Goldbach’s conjecture. |
> |   | b. | F The present king of France proved Goldbach’s conjecture. |

Von Fintel and Yablo offer an explanation for these minimal pairs that draws upon the nature of belief revision. Their idea is that the false presupposition is added to the evaluator’s set of beliefs and is tested against that set of beliefs. So, if we test ‘The king of France read Anna Karenina’ against a typical set of beliefs, there is no clash with existing beliefs. But if we test ‘The king of France wrote *Anna Karenina*’ against this set of beliefs, we get a clash. These are the cases where we judge the sentence false.

Schoubye (2009, 2011)[^schoubye-2009][^schoubye-2011] has argued that the von Fintel/Yablo story fails in key places, in particular with cases where there is no previously existing conflicting belief. We typically believe that *Anna Karenina* was written by Tolstoy, who was not and is not the king of France, but do we really have a belief in which the king of France was not a bald Nazi? Where would that belief come from? A general belief that royals can’t be Nazis? That seems implausible.

More significantly, Schoubye observes that with some modest contextual framing the truth value judgments on these examples can flip. In other words, we don’t even need to change the example sentences. Suppose, for example, that someone says that all the royalty at a party are standing and someone utters ‘The present king of France is sitting in a chair’. Here Schoubye suggests that our truth value judgments firm up and flip from being indeterminate to being clear judgments of falsity.

Schoubye’s positive proposal is that the divergent judgments about truth conditions key off of whether a speaker’s utterance can be interpreted as being cooperative. Here Schoubye draws on Robert’s (1998, 2004) idea of the “topic under discussion.” In the example just given, where we are talking about who is sitting at a particular party, someone who utters (35a) is being an uncooperative discourse partner, in that they are not addressing the topic under discussion.

The literature on presuppositional accounts of definite descriptions has become vast, although not entirely uniform in its criticism of Russellian doctrine. Earlier, we noted that on Russell’s view definite descriptions pack within them an existence claim, a uniqueness claim, and a maximality claim. Different presuppositional accounts have targeted different parts of this package, arguing that the relevant component is not entailed but is presupposed.

For example, beginning with Strawson and the work cited above, we have numerous writers arguing that the existence claim is presupposed. The idea that uniqueness is presupposed is suggested in work by Heim (1991)[^heim-1991], von Fintel (2004)[^fintel-2004], Elbourne (2005, 2013)[^elbourne-2005][^elbourne-2013], Rothschild (2007)[^rothschild-2007], and Schoubye (2013)[^schoubye-2013]. It is possible to understand Cooper (1983), Heim (1983)[^heim-1983], Chemla (2009)[^chemla-2009], Schlenker (2008, 2009) and Romoli (2015)[^romoli-2015] as holding that the maximality component is presupposed. Combinations are possible. The idea that both the existence claim and the uniqueness claim is presupposed can be attributed to Abbott (2008)[^abbott-2008], Hawthorne and Manley (2012) and Schoubye (2013)[^schoubye-2013], among others.  For a detailed defense of the Strawsonian position, see Elbourne (2013)[^elbourne-2013].

### 5.2 Donnellan’s distinction and the argument from misdescription

Donnellan (1966)[^donnellan-1966] observed that there is a sense in which Strawson and Russell are both right (and both wrong) about the proper analysis of descriptions. He argued that definite descriptions can be used in (at least) two different ways. On a so-called attributive use, a sentence of the form ‘The *F* is *G*’ is used to express a proposition equivalent to ‘Whatever is uniquely *F* is *G*’. For example, on seeing murder victim Smith’s badly mutilated corpse, Detective Brown might say “The murderer of Smith is insane” thereby communicating the thought that some unique individual murdered Smith and that whoever that individual is, he/she is insane. Alternatively, on a referential use, a sentence of the form ‘The *F* is *G*’ is used to pick out a specific individual, *x*, and say of *x* that *x* is *G*. For example, suppose Jones is on trial for Smith’s murder and is behaving quite strangely at the defense table. I point at Jones and say, “The murderer of Smith is insane”, thereby communicating the thought that Jones is insane (whether or not Jones is the actual murderer).

Donnellan suggested that Russell’s quantificational account of definite descriptions might capture attributive uses, but that it does not work for referential uses. In effect, we might take Donnellan as saying that in some cases descriptions are Russellian and in some cases they are Strawsonian. Perhaps we could even say that the definite determiner ‘the’ is ambiguous between these two cases (it is not clear whether Donnellan himself intended to endorse a lexical ambiguity of this sort).

Kripke (1977)[^kripke-1977] responded to Donnellan by arguing that the Russellian account of definite descriptions could, by itself, account for both referential and attributive uses; the difference between the two cases could be entirely a matter of pragmatics. Here is the idea: Grice showed us that there is an important distinction to be made between what one literally says by an utterance and what one intends to communicate (what one means) by that utterance. To take a famous example of Grice’s, I might write a letter of recommendation for a student saying that he is very punctual and has excellent handwriting. Now what I have said is something about the student’s punctuality and handwriting, but what I meant was that this is a very weak student.

In a similar vein, we could say that when I use a description referentially—say in Donnellan’s courtroom case—I am literally making a general claim to the effect that there is a murderer of Smith and that he is insane, but what I mean by that utterance is that Jones is insane. That is, when I say ‘The murderer of Smith insane’ what I literally say is that exactly one person, *x*, is such that *x* murdered Smith and *x* is insane, but in that context I would succeed in communicating the singular proposition (about Jones) that Jones is insane. Kripke gave several reasons for thinking that this Gricean solution was preferable to an ambiguity thesis. One reason was a general methodological point that one should not introduce ambiguities blithely—doing so is a kind of philosophical cheat.

Also, Kripke observed that these two uses of definite descriptions are really just subspecies of the general distinction between what is meant (speaker’s reference in Kripke’s terminology) and what is literally said (semantic reference) and not at all unique to descriptions. Kripke noted that the distinction even applies to uses of proper names. So, for example, consider the case where I see a man in the distance raking leaves. I take the man to be Jones but it is actually Johnson. I say ‘Jones is really working up a sweat today’. Now what I have literally said is that Jones is working up a sweat, but what I have communicated (what I meant) is something about Johnson. Clearly no one would argue that the name ‘Jones’ is ambiguous between referring to Jones and referring to Johnson, so why opt for an ambiguity thesis when descriptions are involved? It appears to be exactly the same phenomenon.

One of the advantages of employing the Gricean distinction between the proposition literally communicated and the proposition meant is that it offers an account for our being ambivalent about Donnellan’s (1966)[^donnellan-1966] misdescription cases. In the courtroom case discussed above, I might say “Smith’s murderer is insane,” and still say something true even if the crazy man at the defense table is entirely innocent of the charges and the actual murderer, who is miles from the courtroom, is quite sane. At the same time there is some pull to say that in such a case one is saying something false too. We can say that this is a case where what we literally said was false, but that what we intended to communicate—the proposition meant—was true. The two-level theory thus accounts for our conflicting intuitions.

Similarly, Hornsby (1977)[^hornsby-1977] gave the case of my observing the man ranting at the defense table and (me) saying, “The murderer of Smith is insane” not realizing that the man at the table is both innocent and quite sane, while the actual murderer is at large and quite insane. Again we are ambivalent about the truth of what I say, and as Neale (1990; 91–93) observed, the distinction between the proposition literally expressed and the proposition meant allows us to understand why. In this case, the proposition literally expressed is true, but what I intend to communicate is mistaken.

Unfortunately, there are cases where the two-stage theory doesn’t appear to be sufficient. For example, there remains a difficulty that Ludlow and Segal (2004) have called the *residue of the problem of misdescription*. Consider a case where we are at the crime scene, and unbeknownst to Detective Brown there is not one murderer but several—suppose there were several perpetrators and they were all mad members of an evil cult. When Brown utters the sentence ‘The murderer of Smith is insane’ has he said something true or false? Again we are in two minds about the matter but this time the distinction between what is literally said and what is meant is no help.

### 5.3 The argument from incompleteness

Another persistent problem for the classical Russellian theory of descriptions has been the charge that it fails to account for the problem of “incomplete descriptions” (for discussion see Donnellan (1968), Hornsby (1977)[^hornsby-1977], Devitt (1981, chapter 2; 2004), Wettstein (1981)[^wettstein-1981], Recanati (1986)[^recanati-1986], Salmon (1982)[^salmon-1982], Soames (1986)[^soames-1986], Neale (1990; chapter 2), and Reimer (1992)[^reimer-1992]). In addition, Kripke (1977)[^kripke-1977], while defending Russell’s theory of description against the problem of misdescription, allows that the argument from incomplete descriptions might be enough of a problem to force us to accept referential interpretations of descriptions. The worry, initially raised in Strawson (1950)[^strawson-1950], is that if I say ‘the table is covered with books’, I do not mean to be suggesting that there is only one table in the world. Unfortunately, that seems to be precisely what the Russellian theory of descriptions is committed to. (Recall that on the Russellian analysis my utterance is shorthand for ‘there is a table and only one table and every table is covered with books’.)

One strategy for dealing with this problem is that the context may provide us the means to flesh out the description. For example, perhaps descriptions can be fleshed out appropriately if we allow implicit spatiotemporal locating expressions to be inserted into the description. The suggestion is that when we speak of the table we are implicitly specifying a spatial coordinate—in effect, we are saying ‘the table over there’. One problem with strategies of this nature is that there fails to be a principled basis (in the terminology of Devitt and Sterelny (1999)) for determining what the content of these descriptions is to be. Is it to be a description that the speaker has in mind? Is this description really sufficient to uniquely identify the object in question? Is it always clear that the speaker has a description in mind?

Neale (1990)[^neale-1990] has argued that whatever we may want to say about the problem of incompleteness, it is not very effective as an argument for the referential analysis of descriptions. For example, at the crime scene Detective Brown may simply utter ‘The murderer is insane’ failing to specify exactly which murderer he is talking about (is it the murderer of Smith or Jones or …?). But by hypothesis this case is a canonical example of an attributive use of a definite description. No reference is possible, so how can appeal to reference bail us out? How can any of this be an argument for definite descriptions being semantically referential?

Even stronger, it appears that there are numerous examples involving quantified expressions that suffer the same fate as incomplete descriptions. I can say ‘Everyone came to the party’, not intending to mean everyone in the world. Or I might say, as Yogi Berra once did, ‘Nobody goes there anymore, it’s too crowded’. It certainly appears that what is going on in these cases is similar to the cases of incomplete definite descriptions and that there should be a single strategy for accounting for these different cases of “incompleteness.”

Devitt (2004, 2007)[^devitt-2004][^devitt-2007] and Reimer (1998)[^reimer-1998] have argued that these cases are genuinely different in kind. Their idea is that since definite descriptions are regularly used to express singular thoughts, it stands to reason that the standard meaning of the definite description must be referential. Schoubye (2011, ch. 3) has responded to this claim arguing that it rests on mistaken assumptions about semantic processing and that in any case the line of reasoning would generalize so as to force a referential interpretation of most (possibly all) the other determiners (e.g. ‘every’ and ‘no’).

Alternatively, some writers have argued that that the problem of incomplete definite descriptions can be accounted for if we pursue an appropriate theory of quantifier domain restriction. Stanley and Szabó (2000)[^szabó-2000], for example, take this approach, suggesting that context can restrict the domain of quantification. On their proposal, context can even shift within a sentence, allowing us to make sense of an utterance like ‘The dogs barked at the dogs’, where I mean to say that one group of dogs barked while the other group perhaps suffered in silence. (Their proposal is applicable to all quantified expressions; not just the theory of descriptions. See Bach (2000)[^bach-2000], Neale (2000b)[^neale-2000b], and Lepore (2004)[^lepore-2004] for a more general discussion of the proposal.)

It is important to note (following Szabó (2000)[^szabó-2000] and Ludlow and Segal (2004) that even with a fully functional account of quantifier domain restriction there is a lingering problem here too. Let’s call it the *residue of the incompleteness problem*. Consider cases like (38)

> (38) I put the book on the book.

On the domain restriction proposal, the first use of ‘the book’ cannot have the same domain of quantification as the second use, since that would put two books in the domain of quantification and it would mean that both descriptions in the sentence are incomplete. But one wonders how legitimate a domain-shift analysis is here. Is there really a shift in the domain of quantification between the first utterance of ‘the book’ and the second utterance of that noun phrase? What would count as independent evidence either for, or against, a domain-shift taking place?

## 6. Dissolving Descriptions

As noted in the beginning of this article, the Russellian account of descriptions not only offers a quantificational as opposed to a referential account of descriptions, but it packs three different claims into the analysis of descriptions: an *existence claim*, a *uniqueness claim*, and *a maximality claim*. As we will see, all of these claims can be put under pressure, and all three arguably collapse under that pressure. Let’s begin by examining the uniqueness claim.

### 6.1 Rejecting the uniqueness claim

Given the Gricean resources discussed above, one might speculate that the distinction between definite and indefinite descriptions can be collapsed—that is, perhaps ‘the’ and ‘a’ have the same literal meaning and the only relevant distinction between them is pragmatic.

The motivation for this idea would be as follows. Very few natural languages have what we would recognize as definite and indefinite descriptions. In most Asian and Slavic languages, for example, ‘the man’ and ‘a man’ would both be expressed in the same way—in the determiner-free equivalent of ‘man’. Perhaps it is just our infatuation with surface grammatical form that leads us to think that English or Italian really has two different logical elements corresponding to surface forms ‘the’ and ‘a’. Perhaps there is a single logical element (or perhaps just a free variable) with different pragmatic application conditions. That is, perhaps ‘the’ and ‘a’ have the same literal meaning—i.e., for both ‘An *F* is G’ and ‘The *F* is *G*’ the literal semantics is exhausted by the interpretation that [∃*x*: *Fx*](*Gx*) receives in a standard truth-conditional semantics. A number of linguists and philosophers have entertained this idea in recent years, including Kempson (1975)[^kempson-1975], Breheney (1999), Szabó (2000)[^szabó-2000], Zvolensky (1997)[^zvolensky-1997], Ludlow and Segal (2003) and a version of the idea is at least considered in Heim (1982)[^heim-1982] and Kamp and Reyle (1993).

Obviously there are important differences between our application of the terms ‘the’ and ‘a’, but it does not follow that these differences in application are part of their semantical content. Indeed, many synonyms customarily are put to different uses. Take, for example, Grice (1961, 1975)[^grice-1961][^grice-1975] on the distinction between ‘but’ and ‘and’. On Grice’s story ‘but’ and ‘and’ literally mean the same thing, but different “conventional implicatures” are associated with them; ‘but’ implicates a sense of contrast between the conjuncts.

Ludlow and Segal (2004) offer a similar story about ‘a’ and ‘the’. Following a standard assumption in traditional grammar (see Christophersen 1929), they argue that ‘the’ signals that the object under discussion is given in the conversational context. Noun phrases fronted by the determiner ‘a’ signal that they involve new information. The idea advanced by Ludlow and Segal, however, is that this slender bit of information, combined with Gricean principles, is sufficient to generate the uniqueness implication that is carried by a definite description. That is, an existential claim that there is an *F* that is G, plus a signal that this is given information, is often enough to allow us to implicate that there is unique *F* that is G.

Armed with this idea, let’s return to the some of the loose threads that we left hanging in section 4 above—the residue of the misdescription problem and the residue of the incompleteness problem. As we will see, the unified treatment of definite and indefinite descriptions may provide us an entering wedge for cracking open these puzzles. Let’s look at the misdescription case first.

#### 6.1.1 The residue of the problem of misdescription

Recall the case in which Detective Brown says ‘the murderer of Smith is insane’, incorrectly believing that there was one murderer when in fact the crime was committed by a ghoulish cult of insane individuals. There is a sense in which Brown spoke falsely, but there is also clearly some pull for us to say that what he said was true. As we saw in section 4, the distinction between the proposition literally expressed and the proposition meant was not sufficient to account for this ambivalence on our part. But according to Ludlow and Segal (2004), if we combine this pragmatic distinction with the unified analysis of definite and indefinite descriptions there is something we can say about this last bit of residue.

According to the unified analysis of descriptions, what Detective Brown literally expresses is not the idea that there was a unique murderer of Smith who is insane. To the contrary, he literally expresses the proposition that there is at least one murderer of Smith who is insane. By applying Gricean principles in this context we have made out that Brown intends to say that there is a unique murderer of Smith and that he is insane. We are pulled in two directions by this case because what Brown has said is literally true but what he intended to communicate was, strictly speaking, false.

#### 6.1.2 The residue of the problem of uniqueness

In section 5.3 we considered cases like (38), repeated here, which did not seem to yield in a natural way to the device of quantifier domain restriction.

> (38) I put the book on the book.

But as Szabó (2000)[^szabó-2000] and Ludlow and Segal (2003) have argued, if we combine quantifier domain restriction with the unified analysis of descriptions, the problem seems more amenable to solution. The idea is the following: What one literally expresses in (38) is that the speaker put a book on a book. Pragmatics helps us to make out that one book in particular is being spoken of, which book that is, and where it is to be moved.

### 6.2 Criticism of the Unified View

Although a unified approach is attractive, it has come under criticism from Abbott (2003, 2008)[^abbott-2003][^abbott-2008], Horn (2006)[^horn-2006] and Abbott and Horn (2011). For example, Abbott (2008)[^abbott-2008] argues that the pragmatic story (in which the uniqueness of some descriptions is conversationally implicated) fails because it predicts that the uniqueness implication should be cancellable, but according to Abbott, it is not. (Here we use the hash symbol to indicate a failed implicature cancellation.)

> (39) # Russell was the author of Principia Mathematica, in fact there were two.

One response to this line of argument is that it frontloads our assumptions about written works having single authors. Is (40) any better?

> (40) # Russell authored Principia Mathematica, in fact someone else did too.

This suggests that the uniqueness is not implicated by ‘the’, but is rather built into the meaning of ‘authored’. Strictly speaking, Russell isn’t an author, but a co-author. Contrast both with the following, which seems entirely natural.

> (41) John went to the doctor about his condition, in fact, he went to two doctors because he wanted a second opinion.

This also raises the question of how far one can press the case based on examples like (39). Should we also reject Kripke’s pragmatic analysis of referential descriptions because of the infelicity of examples like (42)?

> (42) (pointing at person in witness chair) # The murderer of Smith is insane, but I don’t know who it is.

Abbott and Horn have suggested that the use of stress in descriptions highlights the uniqueness implications of the utterance. In particular, they claim that in the case of focal stress on the definite, “only uniqueness is at issue with focused *the*, never familiarity.”

Consider the following examples from Horn (2006)[^horn-2006].

> (43) Graham claims that cancer selection is *not* *a* *but* *the* driving force in the emergence of complex animal life.
>
> (44) an idea that the EU is *not* *A* *but* *THE* form of regional integration.
>
> (45) Yet time and again, North Korea is cited as *not only “a” but “the”* major threat to US security.
>
> (46) So Lufthansa is *a—or even the*—German airline.

Setting aside the question of whether these examples offer a case against familiarity, they are not, by themselves, evidence for uniqueness. For example, if (46) is asserting that there is a single unique German airline, it is clearly false, as there are many other German airlines, including Germanwings, Air Berlin, Germania, Hahn Air, and Air Hamburg. Abbot (1999, 2008) recognizes that cases like this are false, but argues that what is going on is that the speakers are engaged in hyperbole. That is, in (46) the speaker is literally saying there is only one German airline and we recognize this as an intentional falsehood, and then infer that the speaker means to communicate the airline is special in some way. The alternative, of course, is to hold that the stressed definite determiner is indicating familiarity or salience. It is also worth noting that Schwarz (2009)[^schwarz-2009] observes there are languages in which separate determiners are used to express familiarity and uniqueness. (See also Coppock forthcoming for discussion of this point.)

Uniqueness accounts also must account for cases in which uniqueness appears to vanish altogether. Consider (47).

> (47) I was driving down *the highway*, when I lost control of my car and it went into *the ditch*. I hit my head on *the side window of the car*. *The ambulance* came and took me to *the hospital* where I had to wait an hour for *the doctor* to see me. I went home in a taxi.

In a similar vein it is hard to overlook the fact that possessives in languages like Italian typically deploy definite determiners (‘*la mia machina*’) without forcing the reading that I own only one car.

Cases of this nature have of course been familiar for some time, but perhaps it has been less on the radar that the uniqueness proposal creates foundational problems for language acquisition theory. It is something of a basic working hypothesis of acquisition theory that semantical components of language are acquired very early and that pragmatic components are acquired much later (see Chien and Wexler (1990), Thornton and Wexler (2000)). This is not surprising, given that pragmatics can involve sophisticated real world reasoning. However, children’s grasp of definite and indefinite descriptions come late in the acquisition process (around age 9; see Karmiloff-Smith 1979 and Warden 1976)[^karmiloff-smith-1979]), prompting Wexler (2011)[^wexler-2011], working on hypothesis that descriptions are Russellian, to question the working hypothesis that semantics is fixed early. But an alternative explanation is that uniqueness is a pragmatic phenomenon, thus saving the working hypothesis. In other words, a basic working hypothesis of acquisition theory is preserved if we reject the Russellian story about the distinction between definite and indefinite determiners.

So far we have been talking about the unified theory in the context of rejecting the uniqueness component of Russell’s analysis. But there are also the existence component and the maximality component to consider. Can these also be rejected?

### 6.3 Rejecting the existence claim

A number of authors have observed that the traditional Russellian analysis of definite descriptions gets us into trouble when we embed descriptions into certain environments like propositional attitudes, conditionals, and questions (see Heim (1991)[^heim-1991] Elbourne (2005, 2010, 2013, forthcoming), Neale (2005)[^neale-2005], Rothschild (2007)[^rothschild-2007], Hawthorne and Manley (2012) and Schoubye (2011, 2013)[^schoubye-2011][^schoubye-2013]). To illustrate the problem, consider the following:

> (48) John wants the ghost in the attic to stop making so much noise.
>
> (49) John wants that there be exactly one ghost in the attic and that it stop making so much noise.

On the standard Russellian analysis, we get something like a claim that John wants that there be a unique ghost in his attic and that it stop making so much noise. Let’s set aside the uniqueness claim for the moment and just focus on the existence claim; is it really the case that John wants there to be a ghost in the attic at all? Notice that it won’t do to try and extract the existence claim from the propositional attitude environment, for then we get an actual existence claim, which is definitely not what we want.

As Rothchild (2007) observes, a similar argument can be made for descriptions embedded in questions (here assuming, as did Russell, that possessives are to be analyzed as definite descriptions):

> (50) Is my child making too much noise?
>
> (51) Is it the case that I have exactly one child and that it is making too much noise?

Clearly, the question being put forth in (50) is not concerned with finding out whether or not the questioner has a child. Responding by saying ‘yes you have a child’ would not be a partial answer to the question.

The phenomenon also seems to apply to modal adverbs. Consider the case where I do not know if my upstairs neighbors have a child, but I speculate that they do and that it is making noise. It would be odd for me to offer up an utterance of (52), even though (53) would be fine.

> (52) It is possible that the child of my upstairs neighbors is making noise.
>
> (53) It is possible that there is exactly one child of my upstairs neighbors and it is making noise.

I believe this can point can be made for other modals as well.

> (54) It is necessary that my identical twin has my DNA.
>
> (55) It is necessary that there is exactly one identical twin of me and that it have my DNA.

Elbourne (forthcoming) believes that the problem can even be constructed in cases that are extensional if we quantify into the description. Consider the following.

> (56) No boy sold the dog he bought.
>
> (57) No boy bought exactly one dog and sold it.

There are circumstances in which the Russellian gloss in (57) is true, but (56) is not true. For example, the case in which no boys bought any dogs.

Schoubye’s (2011)[^schoubye-2011] solution to all these cases bears notice. He argues that the problem can be avoided if we distinguish between the sentence itself, the presupposition, and what is asserted. So, for example, for a sentence like ‘The *F* is *G*’ we have the following:

> | Sentence: | the *F* is *G* |
> | --- | --- |
> | Presupposition: | ∃*x*(*Fx* & ∀*y*(*Fy* → *x*=*y*) & *Gx*) |
> | Assertion: | *Gx* |

So, as in the Ludlow and Segal analysis, the uniqueness claim is not part of what is asserted. On Schoubye’s proposal, uniqueness is not implicated, but is presupposed. But notice also that in this case the existence claim is also not part of what is asserted. What is asserted is simply an open sentence! In some cases, the open sentence will be existentially closed, but in cases like ‘John wants the ghost in the attic to be quiet’ there is no existential closure. Of course it is possible to ask what it means to assert an open sentence, but notice that again we are converging on a view in which the determiners fall out, leaving behind a free variable.

### 6.4 The maximality claim under pressure

We’ve already put the uniqueness and existence claims of descriptions under pressure. Can we do the same with the maximality claim? Here it is difficult to find evidence one way or the other for the case of singular definite descriptions, but earlier we saw that the theory could be generalized *à* *la* Sharvy, to plural descriptions, and in the plural case we could actually probe the question of whether maximality holds.

Recall from section 4.4 that on the Sharvy (1980)[^sharvy-1980] analysis of descriptions we could generalize Russell’s theory of descriptions to plurals by arguing that ‘the *F* (or *F*s) is (are) *G*’ is equivalent to the following,

> (32) ∃*x*(*Fx* & ∀*y*(*Fy* → *y*≤ *x*) & *Gx*)

(again, where *F* can be either a singular count noun (like ‘dog’), a plural count noun (like ‘dogs’) or a mass noun (like ‘water’), and the symbol ‘≤’ indicates a parthood relation.)

Of interest to us at the moment is the fact that this analysis encodes the maximality claim—it says that all the *F*s are *G*s. But is this analysis right? Arguably not. If one says the American people are disappointed in Trump, it doesn’t mean that all of them are. If my neighbor has 101 Dalmatians, I might complain ‘the dogs are barking again’, even if only some of them are barking (and it doesn’t seem plausible to say that I am restricting the domain of discourse to just the 20 or so dogs that are barking). Likewise for definite mass terms; if I say that the bread in the breadbox is moldy I am not saying that the bread is moldy through and through—I’m saying that some of it is. And if I say that ‘the dog is a loyal animal’ I am not saying that all subspecies of dogs are loyal. Arguably the maximality condition in Sharvy’s generalized theory of descriptions should be dropped altogether. (But see Brogaard (2007)[^brogaard-2007] and Bach (2000)[^bach-2000] for defenses of maximality.)

## 7. Descriptions through the Lens of Linguistics

The importance of descriptions, and what is at stake in metaphysics, epistemology etc., have prompted some philosophers to dig deeper into the actual linguistics of descriptions (or better, definite and indefinite determiners) and linguists have been happy to join in the investigation.  What those joint investigations have shown is that the structure of descriptions is not as straightforward as philosophers often imagine.  There have been several areas where this has become evident.

### 7.1 Descriptions as predicates

At the beginning of this article I noted that some uses of the expressions ‘an *F*’ and ‘the *F*’ are argued to be predicational, rather than quantificational. So, for example, consider the following cases.

> (60) John is a lawyer.
>
> (61) John is the mayor of Pittsburgh.

It is not unusual to think of ‘is a lawyer’ and ‘is the mayor of Pittsburgh’ as predicates. In the case of (60), we intuitively are not saying that there is a lawyer such that John is identical to that lawyer. Indeed, as Williams (1983)[^williams-1983] observed, this appearance is even more pronounced if we consider cases like (62).

> (62) John is not a lawyer

(62) does not seem to have the meaning that there is a lawyer such that John is not identical to that lawyer. It is more natural to take an utterance of (62) as denying that John has a certain property.

If this is right, then the copula ‘is’ is really just the ‘is’ of predication and semantically dispensable (significantly, it routinely does not appear in many other languages unless it is needed to carry tense or other inflectional information). Likewise, we might say that the indefinite article ‘a’ is semantically inert as well—a mere “grace note” in Higginbotham’s (1987)[^higginbotham-1987] terminology. In this vein, one widely held view, due to Kamp (1981)[^kamp-1981] and Heim (1982)[^heim-1982], is that we could regard indefinite descriptions as expressions containing free variables which are bound by adverbs of quantification (in the sense of Lewis (1975)[^lewis-1975]) interpreted as existentially quantified by the model theory, or perhaps bound by implicit existential closure operators (Diesing 1992)[^diesing-1992].

For linguists it is now standard to think of indefinite descriptions following the copula as always being predicational, and it is a widespread belief that definite descriptions following the copula are often predicational. Philosophers have also been attracted to this view. See, for example, Geach (1962; section 39), Wiggins (1965, 42 ff.), Kim (1970; 211 ff.), Wilson (1978)[^wilson-1978], Smiley (1981)[^smiley-1981], Heim (1982)[^heim-1982] and Higginbotham (1987)[^higginbotham-1987] among others). Does it follow that we must admit two different kinds of descriptions (quantificational and predicational)? We saw that singular, plural, mass, and generic descriptions can be unified; can we perform the same unification trick here?

Fara (2001)[^fara-2001] pursued the possibility that *all* uses of definite descriptions are predicational—even descriptions in subject position. The idea is that if I say ‘The present King of France is bald’, I am saying something like the following: some *x* is such that *x* is the unique present king of France and *x* is bald. The interesting riff here is the notion that the uniqueness condition is built into the predicate. Extending the Sharvy (1980)[^sharvy-1980] analysis of plural descriptions, we get the following, where *F* is the set of all *F*s, or the mass of all substance that is *F* (the vertical strokes before ad after and after the expression indicate that we are talking about the semantic value, or meaning, of the bordered expression):

> | (63) | \|\|an *F*\|\| = *F* |
> | --- | --- |
> |   | \|\|the *F*\|\| = {*x*: *x* ∈ *F* & ∀*y*(*y*∈*F* → *y*≤*x*)} |

But again we might consider collapsing the distinction between definite and indefinite descriptions here, and say that there is a single rule that interprets all descriptions—definite, indefinite, singular, plural, mass, or generic—as predicates. When we supplement this with the rejection of the uniqueness/maximality clause we get this result:

> (63′) ||the *F*/the *F*s/an *F*/some *F*s|| = *F*

If this is right then the determiners ‘a’ and ‘the’ are both “grace notes” not just in special positions, but across the board.

### 7.2 Determiners decomposed

Normally when we think about determiners we think about them as being fixed unary linguistic objects that have dedicated semantic roles, but is this so? Take the property of being a referring expression, for example. We have spoken about whether descriptions are referring expressions or not, but perhaps it is incorrect to suppose that there are dedicated referring expressions in natural language. Ahn (2019)[^ahn-2019] argues that what is called on to refer can vary greatly in natural language, and that what expressions are deployed in order to refer depends on what else is available to do the job. She proposes a “competition mechanism” which determines which expression might be deployed in order to refer to something.  In some cases it might be a name, in some a demonstrative, in some a pronoun, and in some a description.  It depends on which expression wins the competition in that setting. What this means, if correct, is that the job of reference would not be associated with a single type of syntactic object, but with a large array of syntactic objects. In a similar vein, Ludlow and Živanovic (2022) have suggested that what counts as quantificational may not be a property of individual morphological items, but is more likely a global structural property.  In this instance, the definite and indefinite determiners play more of a role as structure builders and not as individual operators. The kind of quantificational structure that emerges would be a function of the surrounding syntactic objects.

It could also be the case that syntactic objects like the definite and indefinite determiners may not even be as syntactically simple as they appear.  As noted above, Schwarz (2009)[^schwarz-2009] observed that there are languages in which morphologically distinct words are used to express uniqueness and familiarity. Following Stake (2009) and others working in “nanosyntax,” this would create some pressure to say that the definite determiner in English might not be a single functional head, but is “smeared” across a larger phrase structure that has separate functional heads for expressing uniqueness and familiarity.  The English determiner ends up being exploded across the phrase structure.

### 7.3 Determiners as case markers

Determiners are rare in the world’s languages and are not universally employed in Indo-European languages. For example they are not found in Slavic languages, with the exception of southern Slavic languages like Bulgarian. But perhaps this provides an opportunity to gain some insights into the nature of determiners. We can actually study how the Bulgarian determiner system evolved from other Slavic languages.

One interesting fact to observe here, is that as noted by Hewson (1972; 66–67), languages with articles and languages with robust case morphology are typically in complementary distribution. Indeed, as languages evolve, their robust inflectional system gives way to structure dependent language (Leiss (2000)[^leiss-2000]). It is when the case system weakens that determiners begin to appear––an idea that is offered in Abraham (1997:29)[^abraham-1997], Philippi (1997:63–64)[^philippi-1997], Selig (1992)[^selig-1992], Ivančev 1988:105, and (Mayer 1988: 112)[^mayer-1988]. As Mladenova (2007)[^mladenova-2007] puts it, “the morphology of the definite article makes it possible to perpetuate case distinctions long after they have been obliterated elsewhere.” (But see also Mladenova for subtleties in applying this idea to Bulgarian.) Could it be then that determiners serve the purpose of case marking? Iliev (2019)[^iliev-2019] argues that this is what is happening in Bulgarian––genitive case markers have been replace by determiners, which continue to express a kind of possessive relation.

How does this idea work? We can illustrate with some examples from English.

> (64) The car went in the ditch.
>
> (65) I was such a terrible bowler that the ball went in the gutter.
>
> (66) The car needs gas.
>
> (67) The doctor told me to stop eating red meat.

It is easy to hear all of these examples as involving an implicit possessive operator.

> (64′) The car went in *the road’s* ditch.
>
> (65′) I was such a terrible bowler that *my* ball went in *my lane’s* gutter.
>
> (66′) *Our* car needs gas.
>
> (67′) *My* doctor told me to stop eating red meat.

Example (65) is particularly instructive in this regard. If I am an exceptionally terrible bowler I might toss the ball into the gutter of someone else’s lane. In this case I might be more apt to say “The ball went in *a* gutter”; saying that it went in the gutter doesn’t quite seem to do justice to my failure as a bowler. That is because when I say the ball went in *the* gutter it suggests that it at least ended up in *my* gutter.

The claim, however, is not that the definite determiner is functioning as a possessive. The hypothesis is that it is functioning as a multi-purpose case marker, and when it is marking for genitive case, possessive meaning is one possible outcome. But genitive case can be put to other uses. For example, species names are routinely given in the genitive case in Latin, and indeed it is a prescriptive rule about the coining of a new species name that it be placed in genitive case. The underlying deep motivation is presumably that species are part of a genus, so that when one expresses a species name it is shorthand for a more complete description. So, for example, when we say ‘The tiger’, we are offering up an abbreviation of something like ‘tiger, species of genus panthera’ (or more accurately, ‘panthera tigris, of genus panther’). Note the possessive nature of these constructions. In effect, we are saying this: ‘species panthera tigris, belonging to the genus panthera’.

This genitive case analysis perhaps sheds light on what is going on in the array of facts offered by Abbott and Horn. Consider (46) again.

> (46) So Lufthansa is *a—or even the*—German airline.

As observed earlier, (46) can be asserted even if there is more than one German airline. One intriguing possibility here is that the stress is creating what is known as a *superlative genitive*, an example from Latin being *sanctum sanctorum* (holy of holies). In the case of (46), for example, we are saying Lufthansa is the most German airline of German airlines. This idea would require a story involving some movement and copying of the noun within the determiner phrase, but such a story would not be unheard of in contemporary work on the structure of determiner phrases (see Larson (2014)).

What is also intriguing about this line of inquiry is that it suggests a new strategy for accounting for definiteness. It is not pragmatically extruded from givenness (as suggested by Ludlow and Segal) but rather from whatever meaning the genitive case brings with it – often some notion of possession. For example, an appearance of a description of the form ‘the dog’ in a sentence might indicate something like ‘dog of the event’ or ‘dog bearing some thematic role to the event’. From this bit of information, the pragmatics might allow us infer that there is a unique dog.

It would not be fruitful to suggest that definite determiners *always* play the role of case assignment, and they most certainly cannot be cashed out as exclusively assigning genitive case. The prospects for a unified explanation for determiner behavior seems remote. The evidence does suggest however, that definite determiners can often play the role of supplying case, and this may go some way towards explaining some of the most recalcitrant facts involving descriptions.

## 8. Conclusion

A close study of the syntax and semantics of natural language suggests that constructions of the form ‘the *F*’ and ‘an *F*’ are not only rare in natural languages, but potentially misleading in languages like English. These expressions really don’t carry out the logical roles that Russell and subsequent authors have thought. However, Russell’s core insight remains intact: The critical question is whether the sentences in which they appear are quantificational or referential, and Russell may well be right about the critical cases here. That is, many apparently referential constructions may in fact be quantificational. What Russell didn’t see was that surface grammar is more deceptive than even he realized. Elements like ‘the’ and ‘a’ do not directly encode quantifiers or uniqueness clauses. The task for philosophers of language now is the thorny task of figuring out what information they *do* encode.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=descriptions). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/descriptions/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=descriptions&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/descriptions/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- Parsons, T., 1978. “[Pronouns as Paraphrases](http://philosophy.ucla.edu/wp-content/uploads/2016/10/Pronouns-as-Paraphrases-1.pdf),” manuscript, University of Massachusetts, Amherst.

## Related Entries

anaphora | discourse representation theory | logical constructions | logical form | names | nonexistent objects | reference | rigid designators | Russell, Bertrand

### Acknowledgments

Thanks are due to Jason Stanley and Ed Zalta for helpful comments.

[^abbott-1999]: Abbott, B., 1999. “Support for a Unique Theory of Definite Descriptions,” *SALT 9: Proceedings from Semantics and Linguistic Theory IX*, Ithaca, NY: CLC Publications, 1–15.

[^abbott-2003]: –––, 2003. “A Reply to Szabó’s ‘Descriptions and Uniqueness’,” *Philosophical Studies*, 113: 223–231.

[^abbott-2008]: –––, 2008. “Issues in the Semantics and Pragmatics of Definite Descriptions in English,” in J. Gundel & N. Hedberg, (eds.), *Reference: Interdisciplinary perspectives*, Oxford: Oxford University Press, 61–72.

[^abbott-2011]: Abbott, B., and L. Horn, 2011. “Nonfamiliarity and Indefinite Descriptions,” *Paper presented at the annual meeting of the Linguistic Society of America*, Pittsburgh.

[^abraham-1997]: Abraham, W., 1997. “The Interdependence of Case, Aspect and Referentiality in the History of German: The Case of the Verbal Genitive,” in A. van Kemenade and N. Vincent (eds.), *Parameters of Morphosyntactic Change*, Cambridge: Cambridge University Press, 29–61.

[^ahn-2019]: Ahn, Dorothy. 2019. *THAT thesis: A competition mechanism for anaphoric expressions*, Ph.D. Thesis, Harvard University.

[^bach-1987]: Bach, K., 1987. *Thought and Reference*, Oxford: Oxford University Press.

[^bach-2000]: –––, 2000. “Quantification, Qualification, and Context: A Reply to Stanley and Szabó,” *Mind and Language*, 15: 262–283.

[^barker-2008]: Barker, C., and C. Shan., 2008. “Donkey Anaphora is In-scope Binding,” *Semantics and Pragmatics*, 1: 1–40.

[^barker-2004]: –––, 2004. “Descriptions: Points of Reference,” in A. Bezuidenhout and M. Reimer (eds.), *Descriptions and Beyond*, Oxford: Oxford University Press, 189–229.

[^beaver-2001]: Beaver, D., 2001. *Presupposition and Assertion in Dynamic Semantics*. Stanford: CSLI Publications.

[^berman-1987]: Berman, S., 1987. “Situation-based Semantics for Adverbs of Quantification,” in J. Blevins and A. Vainikka (eds.), *Studies in Semantics* (University of Massachusetts Occasional Papers in Linguistics: Volume 12), Amherst: GLSA, 46–68.

[^breheny-1999]: Breheny, R., 1999. *Context Dependence and Procedural Meaning: The Semantics of Definites*, Ph.D thesis, Department of Linguistics, University College, London.

[^brogaard-2007]: Brogaard, B., 2007. “*The* But Not *All*: A Partitive Account of Plural Definite Descriptions,” *Mind and Language*, 22: 402–26.

[^brown-1992]: Brown, M., 1992. “‘On Denoting’ Updated,” *Acta Analytica*, 8: 7–32.

[^burge-1973]: Burge, T., 1973. “Reference and Proper Names,” *The Journal of Philosophy*, 70: 425–439.

[^burge-1980]: –––, 1980. “Truth and Singular Terms,” in M. Platts (ed.), *Reference, Truth and Reality: Essays on the Philosophy of Language*, London: Routledge & Keegan Paul, 167–181.

[^byrne-2006]: Byrne, A. and J. Pryor, 2006. “Bad Intensions,” in M. Garcia-Carpintero and J. Macia (eds.), *Two-Dimensional Semantics: Foundations and Applications*, Oxford: Oxford University Press, 38–54.

[^chastain-1975]: Chastain, C., 1975. “Reference and Context,” in K. Gunderson (ed.), *Language, Mind and Knowledge, Minnesota Studies in the Philosophy of Science* (Volume VII), Minnesota: University of Minnesota Press, 194–269.

[^chalmers-2004]: Chalmers, D., 2004. “The Foundations of Two-Dimensional Semantics,” in M. Garcia-Carpintero & J. Macia, (eds.), *Two-Dimensional Semantics: Foundations and Applications*, Oxford: Oxford University Press.

[^chalmers-2002]: –––, 2002. “The Components of Content,” in D. Chalmers (ed.), *Philosophy of Mind: Classical and Contemporary Readings*, Oxford: Oxford University Press, 608–633.

[^chemla-2009]: Chemla, E., 2009. “Presuppositions of Quantified Sentences: Experimental data,” *Natural Language Semantics*, 17: 299–340.

[^chien-1990]: Chien, Y.-C. and K. Wexler, 1990. “Children’s Knowledge of Locality Conditions in Binding as Evidence for the Modularity of Syntax and Pragmatics,” *Language Acquisition*, 1: 225–295.

[^chomsky-1975]: Chomsky, N., 1975. “Questions of Form and Interpretation,” *Linguistic Analysis*, 1: 75–109.

[^christophersen-1939]: Christophersen, P., 1939. *The Articles: A Study of Their Theory and Use in English*, Copenhagen: Munksgaard.

[^coppock-nd]: Coppock, Elizabeth, forthcoming. “On definite descriptions: Can familiarity and uniqueness be distinguished?” in Daniel Altshuler (ed.), *Linguistics Meets Philosophy*, Cambridge: Cambridge University Press.

[^cooper-1979]: Cooper, R., 1979. “The Interpretation of Pronouns,” in F. Heny and H. Schnelle (eds.), *Syntax and Semantics, vol. 10: Selections from the Third Groningen Round Table*, New York: Academic Press, 61–92.

[^davies-1981]: Davies, M., 1981. *Meaning, Quantification, Necessity*, London: Routledge and Keegan Paul.

[^davies-1980]: Davies, M. and Humberstone, L., 1980. “Two Notions of Necessity,” *Philosophical Studies*, 38: 1–30.

[^devitt-1981]: Devitt, M., 1981. *Designation*, New York: Columbia University Press.

[^devitt-2004]: –––, 2004. “The Case for Referential Descriptions,” in A. Bezuidenhout and M. Reimer (eds.) *Descriptions and Beyond: An Interdisciplinary Collection of Essays on Definite and Indefinite Descriptions*, Oxford: Oxford University Press.

[^devitt-2007]: –––, 2007. “Referential Descriptions and Conversational Implicatures,” *European Journal of Analytic Philosophy*, 3: 7–32.

[^devitt-1999]: Devitt, M., and K. Sterelny, 1999. *Language and Reality: An Introduction to the Philosophy of Language*, 2nd edition, Cambridge, MA: MIT Press.

[^diesing-1992]: Diesing, M., 1992. *Indefinites*, Cambridge, MA: MIT Press.

[^donnellan-1966]: Donnellan, K. S., 1966. “Reference and Definite Descriptions,” *Philosophical Review*, 77: 281–304.

[^donnellan-1978]: –––, 1978. “Speaker Reference, Descriptions, and Anaphora,” in P. Cole (ed.), *Syntax and Semantics 9: Pragmatics*, New York: Academic Press, 47–68.

[^dummett-1973]: Dummett, M., 1973. *Frege: Philosophy of Language*, Cambridge, MA: Harvard University Press.

[^dummett-1981]: –––, 1981. *The Interpretation of Frege’s Philosophy*, London: Duckworth.

[^elbourne-2005]: Elbourne, P., 2005. *Situations and Individuals*, Cambridge, MA: MIT Press.

[^elbourne-2009]: –––, 2009. “Bishop Sentences and Donkey Cataphora: A Response to Barker and Shan,” *Semantics and Pragmatics*, 2: 1–7.

[^elbourne-2010]: –––, 2010. “On Bishop Sentences,” *Natural Language Semantics*, 18: 65–78.

[^elbourne-2013]: –––, 2013. *Definite Descriptions*, Oxford: Oxford University Press.

[^elbourne-2017]: –––, forthcoming. “Definite Descriptions and Negative Existential Quantifiers,” *Philosophical Studies*, first online 27 May 2017. doi:10.1007/s11098-017-0925-2

[^eluguardo-2002]: Eluguardo, R., 2002. “The Predicate View of Proper Names,” in G. Preyer and G. Peter (eds*.), Logical Form and Language*, Oxford: Oxford University Press, 13–53.

[^enç-1986]: Enç, M., 1986. “Towards a Referential Analysis of Temporal Expressions,” *Linguistics and Philosophy*, 9: 405–426.

[^epstein-1996]: Epstein, R., 1996. “Viewpoint and the Definite Article,” in A. Goldberg (ed.), *Conceptual Structure, Discourse and Language*, Stanford: CSLI Publications, 99– 112.

[^evans-1973]: Evans, G., 1973. “The Causal Theory of Names,”*Proceedings of the Aristotelian Society* (Supplementary volume), 47: 187–208.

[^evans-1982]: –––, 1982. *The Varieties of Reference*, Oxford: Oxford University Press.

[^everett-2001]: Everett, A., and T. Hofweber (eds.), 2001. *Empty Names, Fiction and the Puzzles of Non-Existence*, Stanford: CSLI Publications.

[^fara-2001]: Fara, D.G., 2001. “Descriptions as Predicates,” *Philosophical Studies*, 102: 1–42. Published under the name “Delia Graff.”

[^farkas-1981]: Farkas, D.F., 1981. “Quantifier Scope and Syntactic Islands,” in R. Hendrik et al. (eds.), *Proceedings of CLS* 7, Ithaca: CLC Publications, 36–55.

[^felka-2015]: Felka, K., 2015. “On the Presuppositions of Number Sentences,” *Synthese*, 192: 1393–1412.

[^fintel-2004]: von Fintel, K., 2004. “Would You Believe It? The King of France is Back! (Presupposition and Truth-Value Intuitions),” in A. Bezuidenhout and M. Reimer (eds.), *Descriptions and Beyond: An Interdisciplinary Collection of Essays on Definite and Indefinite Descriptions*, Oxford: Oxford University Press.

[^fintel-2008]: –––, 2008. “What is Presuppositional Accommodation, Again?” *Philosophical Perspectives*, 22: 137–170.

[^fodor-1982]: Fodor, J.D., and I. Sag, 1982. “Referential and Quantificational Indefinites,” *Linguistics and Philosophy*, 5: 355–398.

[^french-2001]: French, P., and H. Wettstein (eds.), 2001. *Midwest Studies in Language XXV: Figurative Language*, Oxford: Blackwell.

[^gauker-2008]: Gauker, C., 2008. “Against Accommodation: Heim and van der Sandt and the Presupposition Projection Problem,” *Philosophical Perspectives* 22: 171–205.

[^geach-1962]: Geach, P., 1962. *Reference and Generality,* Ithaca: Cornell University Press.

[^geurts-2011]: Geurts, B., and van der Sandt, R., 2011. “Domain restriction,” in P. Bosch & R. van der Sandt (eds.), *Focus: Linguistic, cognitive, and computational perspectives*, Cambridge: Cambridge University Press, 268–292.

[^geurts-2016]: Geurts, B., and van Tiel, B., 2016). “When ‘All the Five Circles’ are four: New exercises in domain restriction,” *Topoi*, 35: 109–122.

[^grice-1961]: Grice, H.P., 1961. “The Causal Theory of Perception,” *Proceedings of the Aristotelian Society* (Supplementary volume), 35: 121–52.

[^grice-1975]: –––, 1975. “Logic and Conversation,” in J. Cole and J. Morgan (eds.), *Syntax and Semantics, Vol 3: Speech Acts*, New York: Academic Press.

[^grice-1981]: –––, 1981. “Presupposition and Conversational Implicature,” in P. Cole (ed.) *Radical Pragmatics*, New York: Academic Press, 183–198.

[^groenendijk-1991]: Groenendijk, J., and M. Stokhof, 1991. “Dynamic Predicate Logic,” *Linguistics and Philosophy*, 14: 39–100.

[^hawthorne-2012]: Hawthorne, J., and D. Manley, 2012. *The Reference Book*, Oxford: Oxford University Press.

[^heim-1982]: Heim, I., 1982. *The Semantics of Definite and Indefinite Noun Phrases*, Ph.D. Thesis, University of Massachusetts, Amherst.

[^heim-1983]: –––, 1983. “On the Projection Problem for Presuppositions,” in D. Flickinger (ed.), *Proceedings of the Second West Coast Conference on Formal Linguistics*, Stanford: Stanford University Press, 114–125.

[^heim-1990]: –––, 1990. “E-Type Pronouns and Donkey Anaphora,” *Linguistics and Philosophy*, 13: 137–178.

[^heim-1991]: –––, 1991. “Artikel und Definitheit,” in A. von Stechow and D. Wunderlich (eds.), *Semantik. Ein internationales Handbuch der Zeitgenössischen Forschung*, Berlin: Walter de Gruyter, 487–535.

[^heim-1992]: –––, 1992. “Presupposition Projection and the Semantics of Attitude Verbs,” *Journal of Semantics* 9: 183–221.

[^hewson-1972]: Hewson, J., 1972. *Article and Noun in English,* The Hague : Mouton.

[^higginbotham-1987]: Higginbotham, J., 1987. “Indefiniteness and Predication,” in E. Reuland and A. ter Meulen (eds.), *The Representation of (In)definiteness*, Cambridge, MA: MIT Press, 43–70.

[^higginbotham-1988]: –––, 1988. “Contexts, Models, and Meaning: A Note on the Data of Semantics,” in R. Kempson (ed.), *Mental Representations: The Interface between Language and Reality*, Cambridge: Cambridge University Press, 29–48.

[^higginbotham-1981]: Higginbotham, J., and R. May, 1981. “Questions, Quantifiers and Crossing,” *The Linguistic Review*, 1: 51–79.

[^horn-2006]: Horn, L., 2006. “Toward a Fregean Pragmatics: *Voraussetzung, Nebengedanke, Andeutung*,” Essen: Linguistic Agency University of Duisburg-Essen (LAUD), Paper No. 676.

[^hornsby-1976]: Hornsby, J., 1976. “Proper Names: A Defense of Burge,” *Philosophical Studies*, 30: 227–234.

[^hornsby-1977]: –––, 1977. “Singular Terms in Contexts of Propositional Attitude,” *Mind*, 86: 31–48.

[^iliev-2019]: Iliev, I., 2019. “On a Possessive Usage of the Definite Article in Bulgarian,” *Dunarea–Nistru: Anuar*, 6: 233–240.

[^ivančev-1988]: Ivančev, S., 1988. *Bŭlgarskijat Ezik –– Klasičeski i Ekzotičen*, Sofia: Narodna Prosveta.

[^jackson-1998]: Jackson, F., 1998. “Reference and Description Revisited,” in J. Tomberlin (ed.), *Philosophical Perspectives 12: Language, Mind, and Ontology*, Oxford: Blackwell, 201–218.

[^jandrić-2014]: Jandrić, A., 2014. “‘The King of France is Bald’ reconsidered: A case against Yablo,” *Philosophical Studies*, 169: 173–181.

[^kadmon-1990]: Kadmon, N., 1990. “Uniqueness,” *Linguistics and Philosophy*, 13: 273–324.

[^kamp-1981]: Kamp, H., 1981. “A Theory of Truth and Semantic Interpretation,” in J. Groenendijk et al., (eds.), *Formal Methods in the Study of Natural Language*, Amsterdam Centre. Reprinted in J. Groenendijk et.al., (eds.), *Truth, Interpretation, and Information*, Dordrecht: Foris, 1–43 (1984).

[^kamp-1993]: Kamp, H., and U. Reyle, 1993. *From Discourse to Logic*, Dordrecht: Kluwer Academic Publishers.

[^kanazawa-2001]: Kanazawa, M., 2001. “Singular Donkey Pronouns are Semantically Singular,” *Linguistics and Philosophy*, 24: 383–403.

[^karmiloff-smith-1979]: Karmiloff-Smith, A., 1979. *A Functional Approach to Child Language*, Cambridge: Cambridge University Press.

[^keenan-1986]: Keenan, E. and Y. Stavi, 1986. “A Semantic Characterization of Natural Language Determiners,” *Linguistics and Philosophy*, 9: 253–326.

[^kim-1970]: Kim, J., 1970. “Events and Their Descriptions: Some Considerations,” in N. Rescher (ed.), Essays in Honor of Carl G. Hempel. Dordrecht: D. Reidel, 199–215.

[^king-1987]: King, J., 1987. “Pronouns, Descriptions, and the Semantics of Discourse,” *Philosophical Studies*, 51: 341–62.

[^king-1988]: –––, 1988. “Are Indefinite Descriptions Ambiguous?” *Philosophical Studies*, 53: 417–440.

[^kempson-1975]: Kempson, R., 1975. *Presupposition and The Delimitation of Semantics*, Cambridge: Cambridge University Press.

[^kratzer-1995]: Kratzer, A., 1995. “Scope or Pseudoscope? Are there Wide Scope Indefinites?” in F. Hamm and A. von Stechow (eds.), *Proceedings: Recent Developments in the Theory of Natural Language*, Universitäat Täubingen.

[^kratzer-1989]: –––, 1989. “An Investigation of the Lumps of Thought,” *Linguistics and Philosophy*, 12: 607–653.

[^krifka-1996]: Krifka, M., 1996. “Pragmatic Strengthening in Plural Predicates and Donkey Sentences,” in T. Galloway and J. Spence (eds.), *Proceedings of SALT VI*, Ithaca: Cornell University.

[^kripke-1977]: Kripke, S., 1977. “Speaker Reference and Semantic Reference,” in French, Uehling, and Wettstein (eds.), *Contemporary Perspectives in the Philosophy of Language*, Minneapolis: University of Minnesota Press, 6–27.

[^kripke-1980]: –––, 1980. *Naming and Necessity*, Cambridge, MA: Harvard University Press.

[^kroll-2008]: Kroll, N. 2008. “On bishops and donkeys,” *Natural Language Semantics*, 16: 359–372.

[^kroon-1987]: Kroon, F., 1987. “Causal Descriptivism,” *Australasian Journal of Philosophy*, 65: 1–17.

[^kroon-1989]: –––, 1989. “Circles and Fixed Points in Description Theories of Reference,” *Noûs*, 23: 373–392.

[^lappin-1989]: Lappin, S., 1989. “Donkey Pronouns Unbound,” *Theoretical Linguistics*, 15: 263–286.

[^larson-2004]: Larson, R.K., 2004. *On Shell Structure*, London: Routledge.

[^larson-1995]: Larson, R., and G. Segal, 1995. *Knowledge of Meaning*, Cambridge, MA: MIT Press.

[^lasersohn-1993]: Lasersohn, P., 1993. “Existence Presuppositions and Background Knowledge,” *Journal of Semantics*, 10: 112–122.

[^leiss-2000]: Leiss, E., 2000. *Artikel und Aspekt: Die Grammatischen Muster von Definitheit* (*Studia Linguistica Germanica* 55), Berlin: Walter de Gruyter.

[^lepore-2004]: Lepore, E., 2004. “An Abuse of Context in Semantics: The Case of Incomplete Definite Descriptions,” in A. Bezuidenhout and M. Reimer (eds.) *Descriptions and Beyond: An Interdisciplinary Collection of Essays on Definite and Indefinite Descriptions*, Oxford: Oxford University Press.

[^lewis-1975]: Lewis, D., 1975. “Adverbs of Quantification,” in E. Keenan (ed.), *Formal Semantics of Natural Language*, Cambridge: Cambridge University Press, 3–15.

[^lewis-1979]: –––, 1979. “Scorekeeping in a Language Game,” *Journal of Philosophical Logic*, 8: 339–359.

[^lewis-1984]: –––, 1984. “Putnam’s Paradox,” *Australasian Journal of Philosophy*, 62: 221–236.

[^linsky-1992]: Linsky, B., 1992. “The Logical Form of Descriptions (Critical Notice of Stephen Neale’s *Descriptions*),” *Dialogue*, 31: 677–83.

[^linsky-2002]: –––, 2002. “Russell’s Logical Form, LF, and Truth Conditions,” in G. Preyer and G. Peter (eds.), *Logical Form and Language*, Oxford: Oxford University Press, 391–408.

[^loar-1976]: Loar, B., 1976. “The Semantics of Singular Terms,” *Philosophical Studies*, 30: 353–377.

[^ludlow-1994]: Ludlow, P., 1994. “Conditionals, Events, and Unbound Pronouns,” *Lingua e Stile*, 29: 3–20.

[^ludlow-1999]: –––, 1999. *Semantics, Tense, and Time: an Essay in the Metaphysics of Natural Language*, Cambridge, MA: MIT Press.

[^ludlow-2001]: –––, 2001. “Metaphysical Austerity and the Problems of Temporal and Modal Anaphora,” in J. Tomberlin (ed.) *Philosophical Perspectives 15: Metaphysics*, Atascadero: Ridgeview Press.

[^ludlow-2002]: –––, 2002. “Externalism, Logical Form, and Linguistic Intentions,” in A. Barber (ed.), *The Epistemology of Language*, Oxford: Oxford University Press, 132–168.

[^ludlow-1991]: Ludlow, P., and S. Neale, 1991. “Indefinite Descriptions: In Defense of Russell,” *Linguistics & Philosophy*, 14: 171–202.

[^ludlow-2004]: Ludlow, P. and G. Segal, 2004. “On a Unitary Semantical Analysis for Definite and Indefinite Descriptions,” in A. Bezuidenhout and M. Reimer (eds.), *Descriptions and Beyond: An Interdisciplinary Collection of Essays on Definite and Indefinite Descriptions*, Oxford: Oxford University Press, 420–437.

[^ludlow-2022]: Ludlow, P., and S. Živanovic, 2022. *Language, Form, and Logic*, Oxford: Oxford University Press.

[^lyons-1999]: Lyons, C., 1999. *Definiteness*, Cambridge: Cambridge University Press.

[^lycan-1984]: Lycan, W., 1984. “A Syntactically Motivated Theory of Conditionals,” in French, Euhling, and Wettstein (eds.), *Midwest Studies in Philosophy* (Volume IX), Minneapolis: University of Minnesota Press, 437–455.

[^mandelbaum-1994]: Mandelbaum, D., 1994. *Syntactic Conditions on Saturation*, Ph.D. thesis, Graduate Faculty in Linguistics, CUNY Graduate Center.

[^marcus-1948]: Marcus, R., 1948. “Modality and Description,” *Journal of Symbolic Logic*, 13: 31–37. Reprinted in *Modalities: Philosophical Essays*, New York: Oxford University Press, 1993.

[^mayer-1988]: Mayer, G.L., 1988. *The Definite Article in Contemporary Standard Bulgarian*, Wiesbaden: Otto Harrassowitz.

[^meinong-1904]: Meinong, A., 1904. “Über Gegenstandstheorie,” Translated as “The Theory of Objects,” in R. Chisholm (ed.), *Realism and the Background of Phenomenology*, New York: Free Press, 1960.

[^mcdowell-1977]: McDowell, J., 1977. “On the Sense and Reference of Proper Names,” *Mind*, 86: 159–185.

[^mladenova-2007]: Mladenova, O., 2007. *Definiteness in Bulgarian: Modelling the Processes of Language Change* (Trends in Linguistics: Studies and Monographs 182), Berlin: Mouton de Gruyter.

[^neale-1990]: Neale, S., 1990. *Descriptions*, Cambridge, MA: MIT Press Books.

[^neale-1993]: –––, 1993. “Term Limits,” *Philosophical Perspectives*, 7: 89–114.

[^neale-2000a]: –––, 2000a. “On a Milestone of Empiricism,” in P. Kotatko and A. Orenstein (eds.), *Knowledge, Language and Logic: Questions for Quine*, Dordrecht: Kluwer, 237–346.

[^neale-2000b]: –––, 2000b. “On Being Explicit: Comments on Stanley and Szabó, and on Bach,” *Mind and Language* 15: 284–294.

[^neale-2002]: –––, 2002. “Abbreviation, Scope, Ontology,” in G. Preyer and G. Peter (eds*.*), *Logical Form and Language*, Oxford: Oxford University Press, 13–53.

[^neale-2004]: –––, 2004. “This, That and the Other,” in M. Reimer and A. Bezuidenhout (eds.), *Descriptions and Beyond: An Interdisciplinary Collection of Essays on Definite and Indefinite Descriptions*, Oxford: Oxford University Press, 68–182.

[^neale-2005]: –––, 2005. “A Century Later,” *Mind*, 114: 809–871.

[^nelson-2002]: Nelson, M., 2002. “Descriptivism Defended,” *Noûs*, 36: 408–35.

[^parsons-1982]: Parsons, C., 1982. “Intensional Logic in Extensional Language,” *Journal of Symbolic Logic*, 47: 289–328.

[^parsons-1980]: –––, 1980. *Nonexistent Objects*, New Haven: Yale University Press.

[^philippi-1997]: Philippi, J., 1997. “The Rise of the Article in the Germanic Languages,” in A. van Kemenade and N. Vincent (eds.), *Parameters of Morphosyntactic Change*, Cambridge: Cambridge University Press, 62–93.

[^prior-1967]: Prior, A. N., 1967. *Past, Present and Future*, Oxford: Oxford University Press.

[^pupa-2013]: Pupa, F., 2013. “Embedded Definite Descriptions: A Novel Solution to a Familiar Problem,” *Pacific Philosophical Quarterly*, 94: 290–314.

[^recanati-1986]: Recanati, F., 1986. “Contextual Dependence and Definite Descriptions,” *Proceedings of the Aristotelean Society*, 87: 57–73.

[^reimer-1992]: Reimer, M., 1992. “Incomplete Descriptions,” *Erkenntnis*, 37: 347–63.

[^reimer-1998a]: –––, 1998a. “Quantification and Context,” *Linguistics and Philosophy*, 21: 95–115.

[^reimer-1998]: –––, 1998. “Donnellan’s Distinction/Kripke’s Test,” *Analysis*, 58: 89–100.

[^reinhart-1997]: Reinhart, T., 1997. “Quantifier-Scope: How Labor is Divided between QR and Choice Functions,” *Linguistics and Philosophy*, 20: 335–397.

[^roberts-1998]: Roberts, C., 1998. “Information Structure in Discourse: Towards and Integrated Formal Theory of Pragmatics,” in J-H. Yoom and A. Kathol (eds.) *OSU Working Papers in Linguistics: Vol. 49: Papers in Semantics*, Department of Linguistics, Ohio State University.

[^roberts-2003]: –––, 2003. “Uniqueness in Definite Noun Phrases,” *Linguistics and Philosophy*, 26: 287–350.

[^roberts-2004]: –––, 2004. “Context in Dynamic Interpretation,” in L. Horn and G. Ward (eds.), *Handbook of Pragmatics*, Oxford: Blackwell Publishing, 197–221.

[^romoli-2015]: Romoli, J., 2015. “The Presuppositions of Soft Triggers are Obligatory Scalar Implicatures,” *Journal of Semantics*, 32: 173–219.

[^rooy-2001]: van Rooy, J., 2001. “Exhaustivity in Dynamic Semantics: Referential and Descriptive Pronouns,” *Linguistics and Philosophy*, 24: 621–657.

[^rothschild-2007]: Rothschild, D., 2007. “Presuppositions and Scope,” *Journal of Philosophy*, 104: 71–106.

[^rothschild-2011]: –––, 2011. “Explaining Presupposition Projection with Dynamic Semantics,” *Semantics and Pragmatics*, 4: 1–43.

[^russell-1905]: Russell, B., 1905. “On Denoting,” *Mind*, 14: 479–493.

[^russell-1910]: –––, 1910–11. “Knowledge by Acquaintance and Knowledge by Description,” *Proceedings of the Aristotelean Society* (New Series), 11: 108–128. Reprinted in *Mysticism and Logic*, London: George Allen and Unwin, 1917, and New York: Doubleday, 1957.

[^russell-1919]: –––, 1919. *Introduction to Mathematical Philosophy*, London: George Allen and Unwin.

[^russell-1957]: –––, 1957. “Mr. Strawson on Referring,” *Mind*, 66: 385–389.

[^salmon-1982]: Salmon, N., 1982. “Assertion and Incomplete Descriptions,” *Philosophical Studies*, 42: 37–45.

[^salmon-1991]: –––, 1991. *Frege’s Puzzle*, Atascadero: Ridgeview Publishing.

[^schoubye-2009]: Schoubye, A., 2009. “Descriptions, Truth Value Intuitions, and Questions,” *Linguistics and Philosophy*, 32: 583–617.

[^schoubye-2011]: –––, 2011. “On Describing,” Ph.D. Thesis, Department of Philosophy, St. Andrews University.

[^schoubye-2013]: –––, 2013. “Ghosts, Murderers, and the Semantics of Descriptions,” Noûs, 47: 496–533.

[^schwarz-2009]: Schwarz, F., 2009. *Two types of definites in natural language*, Ph.D. Thesis, University of Massachusetts/Amherst.

[^searle-1958]: Searle, J., 1958. “Proper Names,” *Mind*, 67: 166–173.

[^searle-1969]: –––, 1969. *Speech Acts: An Essay in the Philosophy of Language*, Cambridge: Cambridge University Press.

[^selig-1992]: Selig, M., 1992. *Die Entwicklung der Nominaldeterminanten im Spätlatein*, Tübingen: Gunter Narr Verlag.

[^sellars-1954]: Sellars, W., 1954. “Presupposing,” *Philosophical Review*, 63: 197–215.

[^sennet-2002]: Sennet, A., 2002. “An Ambiguity Test for Definite Descriptions,” *Philosophical Studies*, 111: 81–95.

[^sharvy-1980]: Sharvy, Richard, 1980. “A More General Theory of Definite Descriptions,” *The Philosophical Review*, 89: 607–623.

[^shiffer-1978]: Shiffer, S., 1978. “The Basis of Reference,” *Erkenntnis*, 13: 171–206.

[^smiley-1981]: Smiley, T.J., 1981. “The Theory of Descriptions,” *Proceedings of the British Academy*, 67: 331–337.

[^smullyan-1947]: Smullyan, A., 1947. “Review of Quine’s ‘The Problem of Interpreting Modal Logic’,” *Journal of Symbolic Logic*, 12: 139–141.

[^smullyan-1948]: –––, 1948. “Modality and Description,” *Journal of Symbolic Logic*, 13: 483–545.

[^soames-1976]: Soames, S., 1976. *A Critical Examination of Frege’s Theory of Presupposition and Contemporary Alternatives*, Ph.D. thesis, MIT Dept. of Linguistics and Philosophy.

[^soames-1986]: –––, 1986. “Incomplete Definite Descriptions,” *Notre Dame Journal of Formal Logic*, 27: 349–375.

[^soames-2002]: –––, 2002. *Beyond Rigidity: The Unfinished Semantic Agenda of Naming and Necessity*, Oxford: Oxford University Press.

[^soames-2009]: –––, 2009. *Reference and Description: The Case against Two-Dimensionalism*, Princeton: Princeton University Press.

[^sosa-1996]: Sosa, D., 1996. *Representing Thoughts and Language*, Ph.D. Thesis, Princeton University Department of Philosophy.

[^sosa-2001]: –––, 2001. “Rigidity in the Scope of Russell’s Theory,” *Noûs*, 35: 1–38.

[^sperber-1986]: Sperber, D., and D. Wilson, 1986. *Relevance: Communication and Cognition*, Oxford: Blackwell.

[^stalnaker-1978]: Stalnaker, R., 1978. “Assertion,” in P. Cole (ed.), *Syntax and Semantics: Pragmatics* (Volume 9), Cambridge, MA: Academic Press.

[^stalnaker-1990]: –––, 1990. “Narrow Content,” in C. A. Anderson and J. Owens (eds.), *Propositional Attitudes: The Role of Content in Logic, Language and Mind*, Stanford: CSLI Publications, 131–146.

[^stanley-1997]: Stanley, J., 1997. “Names and Rigid Designation,” in B. Hale and C. Wright (eds.), *A Companion to the Philosophy of Language*, Oxford: Blackwell Press, 555–585.

[^stanley-1997b]: –––, 1997b. “Rigidity and Content,” in R. Heck (ed.), *Language, Thought, and Logic: Essays in Honor of Michael Dummett*, Oxford: Oxford University Press, 131–156.

[^stanley-2000]: –––, 2000. “Context and Logical Form,” *Linguistics and Philosophy*, 23: 391–434.

[^stanley-2002]: –––, 2002. “Making it Articulated,” *Mind and Language*, 17: 149–68.

[^stanley-2000-2]: Stanley, J. and Z. Szabó, 2000. “On Quantifier Domain Restriction,” *Mind and Language*, 15: 219–61.

[^stanley-1995]: Stanley, J., and T. Williamson, 1995. “Quantifiers and Context-Dependence,” *Analysis*, 55: 291–5.

[^starke-2009]: Starke, M., 2009. “Nanosyntax: a short primer to a new approach to language,” *Nordlyd*, 36: 1–6.

[^strawson-1950]: Strawson, P.F., 1950. “On Referring,” *Mind*, 59: 320–334.

[^strawson-1952]: –––, 1952. *Introduction to Logical Theory*, London: Methuen.

[^strawson-1959]: –––, 1959. *Individuals*, London: Methuen.

[^strawson-1964]: –––, 1964. “Identifying Reference and Truth-Values,” *Theoria*, 3: 96–118.

[^szabó-2000]: Szabó, Z., 2000. “Descriptions and Uniqueness,” *Philosophical Studies*, 101: 29–57.

[^thomason-1990]: Thomason, R., 1990. “Accommodation, Meaning, and Implicature: Interdisciplinary Foundations for Pragmatics,” in P. Cohen, J. Morgan, and M. Pollack (eds.), *Intentions in Communication*, Cambridge, MA: MIT Press, 325–363.

[^thornton-1999]: Thornton, R., and K. Wexler, 1999. *Principle B, VP Ellipsis and Interpretation in Child Grammar*, Cambridge, MA: MIT Press.

[^sandt-1992]: van der Sandt, R., 1992. “Presupposition Projection as Anaphora Resolution,” *Journal of Semantics*, 9: 333–377.

[^wettstein-1981]: Wettstein, H., 1981. “Demonstrative Reference and Definite Descriptions,” *Philosophical Studies*, 40: 241–257.

[^wexler-2011]: Wexler, K., 2011. “Maximal Trouble in the Determiner System,” in E. Gibson and N. Perlmutter (eds.), *The Processing and Acquisition of Reference*, Cambridge, MA: MIT Press, 15–42.

[^wiggins-1965]: Wiggins, D., 1965. “Identity Statements,” in R.J.Butler (ed.), *Analytical Philosophy*, 2nd edition, Oxford: Basil Blackwell.

[^williams-1983]: Williams, E., 1983. “Semantic vs. Syntactic Categories,” *Linguistics and Philosophy*, 6: 423–446.

[^wilson-1978]: Wilson, G., 1978. “On Definite and Indefinite Descriptions,” *The Philosophical Review*, 87: 48–76.

[^wilson-1959]: Wilson, N., 1959. “Substances without Substrata,” *Review of Metaphysics*, 12: 521–539.

[^yablo-2006]: Yablo, S., 2006. “Non-Catastrophic Presupposition Failure,” in J.J. Thomson and A. Byrne (eds.), *Content and Modality: Themes from the Philosophy of Robert Stalnaker*, Oxford: Oxford University Press, 164–190.

[^yablo-2009]: –––, 2009. “Must Existence Questions Have Answers?” in D. Chalmers, D. Manley, and R. Wasserman (eds.), *Metametaphysics: New Essays on the Foundations of Ontology*, Oxford: Oxford University Press, 507–525.

[^yoon-1996]: Yoon, Y., 1996. “Total and Partial Predicates and the Weak and Strong Interpretations,” *Natural Language Semantics*, 4: 217–236.

[^winter-1997]: Winter, Y., 1997. “Choice Functions and the Scopal Semantics of Indefinites,” *Linguistics and Philosophy*, 20: 399–467.

[^zalta-1983]: Zalta, E., 1983. *Abstract Objects: an Introduction to Axiomatic Metaphysics*, Dordrecht: D. Reidel.

[^zalta-1988]: –––, 1988. *Intensional Logic and the Metaphysics of Intensionality*, Cambridge, MA: MIT Press.

[^zvolensky-1997]: Zvolensky, Z., 1997. “Definite Descriptions: What Frege got Right and Russell Didn’t,” *Aporia*, 7: 1–16.
