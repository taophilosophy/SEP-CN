# prop-attitude-reports — dere（supplement）

> （《prop-attitude-reports》词条补充材料，源：plato.stanford.edu/entries/prop-attitude-reports/dere.html）

#### Supplement to Propositional Attitude Reports

## The De Re/De Dicto Distinction

Propositional attitude verbs are *opacity inducing*. That is, they seem to create linguistic environments that do not permit substitution of co-designating singular terms *salva veritate*. This is the basis of Frege’s puzzle. Modals like ‘it is necessary that’ and ‘it is possible that’ are also opacity inducing. Opacity inducing expressions give rise to a *de re/de dicto* distinction. The *de re/de dicto* distinction has meant different things to different people. Below we’ll distinguish three different conceptions of this distinction, the first two concerning the status of sentences and the third being more metaphysical. We begin by motivating the distinction.

W. V. Quine, in his 1956, pointed out an ambiguity in (1) below.

> (1) Ralph believes that someone is a spy.

(1) could mean either of the following.

> (2) Ralph believes that there are spies

or

> (3) Someone is such that Ralph believes that s/he is a spy.

The truth of (3) but not (2), to echo Quine, would give the FBI cause to be interested in Ralph. We might paraphrase (3) as follows: “Someone is such that Ralph believes of that person that s/he is a spy.” The distinction between (2) and (3) can be seen as a distinction of scope for the existential quantifier. In (2), the existential quantifier is interpreted as having narrow scope, occurring within the scope of ‘believes’, which we can represent with the following hybrid sentences.

> (2*) Ralph believes: ∃*x*(*x* is a spy).

In (3), however, the existential quantifier has wide scope and binds a variable that occurs freely within the scope of ‘believes’ and so binds across the attitude verb.

> (3*) ∃*x*(Ralph believes that *x* is a spy).

Russell’s theory of definite descriptions employs just such a distinction in answering Frege’s puzzles about belief.

The same distinction can be found with both modals and temporal modifiers. (4) below is ambiguous between (4n) and (4w).

> (4) The shortest spy might not have been/was not a spy.
>
> (4n) It is possible/was the case that: the shortest spy is not a spy.
>
> (4w) The shortest spy is such that it is possible the case that s/he is not a spy.

(4n) is false; necessarily, any spy such that no spy is shorter than that person is a spy. But presumably (4w) is true; the person who in fact is shortest of all spies might not have gone into espionage and surely wasn’t born into the business.

This very natural and elegant explanation of the ambiguity in (1) leads us to the first conception of the *de re/de dicto* distinction.

> Syntactically *de re*/*de dicto*:
> A sentence is *syntactically de re* just in case it contains a pronoun or free variable within the scope of an opacity verb that is anaphoric on or bound by a singular term or quantifier outside the scope of that verb. Otherwise, it is *syntactically de dicto*.

So, (2) and its quasi-formalization (2*) are syntactically *de dicto* because the quantifier ‘someone’ occurs within the scope of ‘believes’ along with the variable it binds. (3) and its quasi-formalization (3*), on the other hand, are syntactically *de re* because the quantifier ‘someone’ occurs outside the scope of ‘believes’ and yet binds a variable within its scope. Similarly, (5) and (6) below are syntactically *de dicto* while (7) and (8) are syntactically *de re*.

> (5) Sally believes that Bill is happy.
>
> (6) Sally believes that someone is happy.
>
> (7) Bill is such that Sally believes that he is happy.
>
> (8) Someone is such that Sally believes that he is happy.

In his 1956, Quine rejects this simple account of the different readings of (1) because it involves *quantifying into opaque environments*, which Quine thought was incoherent. In particular, making sense of one reading of (1) in terms of (3) and (3*) requires making sense of quantifying in, which Quine maintained could not be done without changing the meaning of the quantifier or the attitude verb.

On the standard semantics for quantification, the interpretation of (3*) requires making sense of an individual satisfying the open sentence ‘Ralph believes that *x* is a spy’. This is because the standard semantics for quantification is objectual: A quantified sentence ∃*x**Φx* is true just in case there is an object that satisfies *Φx*. Quine thought that this leads to contradiction when the open sentence contains an opacity-inducing expression like ‘believes’. He thought this largely because of considerations involving Frege-style cases. Quine’s arguments follow his earlier arguments against quantified modal logic (see, for example, Quine 1980).

Quine thought that (3*) is non-sense because he thought it is incoherent to say of some individual – Ortcutt, let’s say – that the open sentence ‘Ralph believes that he is a spy’ is true of him. He thought this, in turn, for the following reason. Suppose that Ralph knows of Ortcutt under two guises. Under one – say, the mayor of the town guise – Ralph thinks of him as the town pillar who would hardly engage in espionage. Under the other – say, the guy he saw sneaking around in the shadows at night in a trench coat – he thinks of him as a suspicious character engaged in espionage. Let’s associate the first with the term ‘Mayor’ and the second with the term ‘he [pointing at the man in the dark]’. (9) below seems true while (10) seems false.

> (9) Ralph believes that he [pointing at the man in the dark] is a spy.
>
> (10) Ralph believes that Mayor is a spy.

But then whether or not Ortcutt satisfies the open formula ‘Ralph believes that *Φx* is a spy’ depends on how Ortcutt is designated. In particular, Ortcutt satisfies the formula when designated as ‘he [pointing at the man in the dark]’ and doesn’t satisfy the formula when designated as ‘Mayor’. But the notion of an individual satisfying an open sentence is not sensitive to how that individual is designated; the notion of satisfaction is a direct relation between object and condition not mediated by designations of the individual. So, Quine concluded, it is simply non-sense to say that Ortcutt himself, independent of a way of designating him, satisfies or doesn’t satisfy the condition. But then, given the standard objectual semantics for quantification, (3*) is nonsense, as it is objects themselves, however or even whether they are designated, that satisfy or do not satisfy conditions. So, says Quine, we should abandon the attractive project of making sense of the two readings (1) gives rise to in terms of a difference in scope and in terms of the syntactic conception of the *de re*/*de dicto* distinction.

We’ll return to this argument shortly. First, however, let’s introduce our second conception of the *de re/de dicto* distinction. We shall call it “the semantically *de re/de dicto* distinction.”

> Semantically *de re*/*de dicto*:
> A sentence is *semantically de re* just in case it permits substitution of co-designating terms *salva veritate*. Otherwise, it is *semantically de dicto*.

(7) from above non-controversially counts as semantically *de re*. Suppose that Bill is Sally’s brother. Then (7) is true iff (11) below is true.

> (11) Sally’s brother is such that Sally believes that he is happy.

The truth of (11) does not require that Sally conceive of the object of her belief as her brother. For example, if Sally is watching a person across the room laughing who happens to be her brother, although unbeknownst to Sally, and says to herself, “He [pointing at the laughing man] is happy,” then (11) is true. (6) is non-controversially semantically *de dicto*. Similarly, it is all but non-controversial that (12) below is semantically *de dicto*.

> (12) Sally believes that the happy guy in the corner is happy.

Even though Sally’s brother is the happy guy in the corner, (13) below doesn’t seem to follow from the truth of (12), as Sally does not conceptualize the person she sees in the corner as her brother.

> (13) Sally believes that her brother is happy.

What about a sentence like (5) from above, which we categorized as syntactically *de dicto*? Is that sentence semantically *de re* or semantically *de dicto*? In general, what is the relationship between the syntactic conception and the semantic conception? If Fregeanism is true, then every syntactically *de dicto* sentence is semantically *de dicto* as well. On Frege’s own view, remember, attitude verbs induce a reference shift. Furthermore, a large part of the motivation for accepting a sense/reference distinction for singular terms is to ensure that substitution on the basis of an ordinary co-reference relation fails within the scope of an attitude verb. So, any syntactically *de dicto* sentence should be one that does not permit, without further assumptions, substitution and hence is semantically *de dicto* as well.

Sophisticated forms of Russellianism (see section 6 on Contextualist theories in the main text) yield a similar result. Substitution within the scope of an attitude verb is, in general, not permitted and hence any syntactically *de dicto* sentence will be semantically *de dicto* for the reasons given above.

But what if Naive Russellianism is true? (See Section 4 in the main text.) Suppose that both proper names and demonstratively used pronouns are directly referential. And suppose that Naive Russellianism is true. Then (5) from above is true if and only if (14) below is true.

> (14) Sally believes that he [pointing at the laughing man] is happy.

That is because both ‘Bill’ and ‘he [pointing at the laughing man]’ refer to the same person, Bill, and Sally stands in the believing relation to the singular proposition that Bill/he [pointing at the laughing man] is happy.

Now suppose that definite descriptions are singular terms and suppose that they function roughly as Russell says they do. (We say roughly because Russell thought that definite descriptions are not singular terms. For more on Russell’s theory of definite descriptions, see the entry on descriptions. Our thought is that one can agree with the Russellian truth conditions for sentences with definite descriptions while insisting that definite descriptions are singular terms and do not break up under analysis.) Then the fact that Bill is Sally’s brother together with the truth of both (5) and (14) do not suffice for the truth of (13) from above. That is because, even though ‘Bill’ and ‘Sally’s brother’ have a common designation, ‘Sally’s brother’ is not a directly referential expression and so the embedded sentences ‘Bill is happy’ and ‘Sally’s brother is happy’ express different propositions, the first of which Sally stands in the belief relation to, as she accepts ‘He [pointing at the laughing man] is happy’, while the second she does not. The truth of (13) requires that Sally believes true a proposition to the effect that whoever is uniquely at a brother of Sally is happy.

The upshot is that some syntactically *de dicto* sentences, like (5) and (13), are semantically *de re*; they entail, and are entailed by, their syntactically *de re* counterparts, in the sense that (5) is true if and only if (7) is true. But other syntactically *de dicto* sentences, like (13), are not entail by their semantically *de re* counterparts. More precisely, if Naive Russellianism is true, then, for any syntactically *de dicto* propositional attitude containing embedded sentences with directly referential expression, that same sentence is semantically *de re* and both entails and is entailed by its syntactically *de re* counterpart. These connections are not guaranteed when the syntactically *de dicto* propositional attitude sentence contains an embedded sentence with a nondirectly referential expression in subject position. This is a bit surprising but, we think, perfectly acceptable.

We can go a step further in drawing relating the different conceptions. Naive Russellianism, and perhaps neo-Russellianism in general, seems to give rise to a very interesting form of reduction of the *de re* to the *de dicto*. On some conceptions of the reduction of the *de re* to the *de dicto*, all *de re* beliefs involve completely conceptualized beliefs. (See, for example, Kaplan 1969, Chisholm 1976, and Sosa 1970. Kaplan abandoned the view in his later work.) The neo-Russellian is not likely to embrace this sort of reduction. But there is a less ambitious reduction that she may well find congenial: Namely, for any true *de re* reporting sentence, there is a true *de dicto* reporting sentence. This is because the *de re* and *de dicto* reporting sentences will report the very same belief, as is witnessed by the Naive Russellian view of the relationship between (5) and (7). Believing that Bill is happy just is, on this view, believing of Bill, who happens to be the person Sally demonstrated while saying to herself, ‘He [pointing at the laughing man] is happy’, that he is happy. Both (5) and (7), that is, report belief in the same singular proposition. (For a suggestion of the relationship between neo-Russellianism and the reduction of the *de re*, see Kaplan 1986; for more details, see Salmon 1995, 1997.) If this view is correct, then we can see that Quine’s argument against the natural and elegant account of the ambiguity we found in (1) that we opened with above fails.

Let us return to our discussion of Quine. Quine rejects, remember, (3*). But he does not deny that there is an intuitive distinction between two ways of reading (1) that the simple Russell-inspired account in terms of (2) and (3) is trying to get at. Quine offered an account of that intuitive distinction in terms of a lexical ambiguity in ‘believes’ (and other propositional attitude verbs). (The Russell-inspired account considered above makes sense of the distinction as a syntactic ambiguity of scope.) There is, first, the two-place relation *believes-notional*, which is a relation between an agent and a proposition. (Quine, in section 4 of his 1956, went on to eliminate *propositional* attitudes in terms of *believing-true* a sentence. See the discussion of sententialism in the section Denying the assumption of structured-propositionalism in the main text.) In addition, there is an irreducible three-place relation *believes-relational*, which obtains between an agent, an object, and an abstract. If Quine were right, there would be no reducibility thesis of any kind between the semantically *de re* and the semantically *de dicto*. Burge, in his 1977a/b, agrees with Quine on this score.

Although it may be tempting to think of the ambiguity uncovered in (1) as an ambiguity in the verb ‘believe’, positing lexical ambiguities to explain the data is unnecessary, as we have seen above in our discussion of neo-Russellianism. And there have also been Fregean account of the distinction offered in Kaplan 1969 and Forbes 1996 that do not require positing a lexical ambiguity. Given the dictum that lexical ambiguities should be invoked only when necessary, this calls into question the Quinean account of the two readings of (1).

There is a final conception of the *de re/de dicto* distinction that is worth briefly considering. We shall label it the metaphysical conception of the *de re/de dicto* distinction. This conception of the distinction concerns the role a given object plays in the truth of a sentence. This conception of the distinction is best brought out by contrasting the simple theory of predication that forms the basis of standard predicate logic with quotation. In standard predicate logic, an *n*-place predicate is interpreted by being assigned a set of *n*-tuples of individuals from the domain of discourse; intuitively, the set of *n*-tuples to which the predicate applies. An atomic sentence of the form Φα is true in an interpretation just in case the value of α in that interpretation is in the extension of Φx in that interpretation. Contrast this with the relationship between ordinary objects and quotation. The truth of (15) below does not directly involve Henry himself but instead the name ‘Henry’.

> (15) ‘Henry’ has 5 letters.

At best Henry is indirectly, if at all, involved in the truth of (15) in virtue of his having a name (namely, the name ‘Henry’) that has the attribute of having 5 letters. Here, it is the name, not Henry himself, that is the direct object of predication.

With this in mind, we can formulate our third conception of the de re/de dicto distinction as follows.

> Metaphysically *de re*/*de dicto*:
> An attribution is metaphysically *de re* with respect to an object **o** just in case it directly attributes a property to **o**.

Are belief attributions metaphysically *de re*? While it seems clear that a sentence like (5) is metaphysically *de re* with respect to Sally, is there also a sense in which it is metaphysically *de re* with respect to Bill, the object of Sally’s belief? And how does our third conception of the *de re* relate to the other two conceptions introduced earlier? The answers to these questions differ depending on the theory of belief attributions one adopts.

Suppose that an attribution is metaphysically *de re* with respect to **o**. Then the expression in the attribution that designates **o** should be open to substitution and hence the attribution is semantically *de re* as well. For suppose it were not. Then the truth of the attribution would depend on how the object is designated. But then whether or not the attribution is true would not depend solely on how the object itself is and so the attribution would not be metaphysically *de re*.

Suppose that Sally believes that Bill is happy. Does it thereby follow that Bill himself has a property – namely, the property of being believed by Sally to be happy? Neo-Russellians say “yes,” for reasons discussed above: Namely, Sally’s believing that Bill is happy involves Sally’s standing in the belief relation to a singular proposition that involves Bill himself as a direct constituent. Those that reject neo-Russellianism, however, answer “no.” This is because Sally’s belief, which is truly reported by (5), does not involve Bill himself but rather mode of presentation of Bill. Bill himself is at best indirectly implicated in the truth of (5), by being determined by the mode of presentation in question.

Claiming that belief attributions are not metaphysically *de re* is problem, for the following reasons. Suppose that Sally has reason to believe, on purely general grounds, that there is exactly one person at Disneyland and that whoever is at Disneyland is a happy person. Then (16) below seems true.

> (16) Sally believes that the person at Disneyland is happy.

Suppose now that Bill is the person at Disneyland. In this case, although in some sense it is Bill that Sally believes to be happy, in that she believes true a proposition that is about Bill in virtue of his satisfying the condition of uniquely being at Disneyland, it is intuitive that Bill himself does not have the property of being believed by Sally to be happy and that Bill himself does not directly factor into Sally’s cognitive state. So, the truth of (16) does not entail a metaphysically *de re* attribution to Bill. This is in contrast to the case in which Brenda’s grounds for believing that the person at Disneyland is happy is her having spied on Bill from her hotel room, witnessing and cognizing Bill’s rapture while in the happiest place of earth. Then it is plausible that Brenda has a *de re* belief of Bill to the effect that he is happy.

Consider now (17).

> (17) The person at Disneyland is such that Sally believes that he is happy.

(17) is syntactically *de re*, non-controversially allows substitution, and hence is semantically *de re* as well. Intuitively the truth of (17), combined with the fact that Bill is the person at Disneyland, entails (7). (17) and (7) do seem to be metaphysically *de re* with respect to Bill. The challenge is to explain why (16) entails neither (17) nor (7).

A plausible answer is this. The truth of (17) and (7) require that Sally stand in the belief relation to a singular proposition involving Bill himself as a direct constituent. But (16) can be true even if Sally believes no such proposition. The truth of (16) requires only that Sally stand in the belief relation to a purely general proposition to the effect that there is someone who uniquely is at Disneyland and that person is happy, a proposition both the grasping and adequate justification for believing of which does not require any cognitive relations to Bill in particular. In the situation described, Sally is only in a position to entertain a general proposition about Bill and not the singular proposition that would support the truth of (17) and (7). More generally, a designating term within the that-clause is open to exportation, transforming a syntactically *de dicto* propositional attitude ascription into a semantically and metaphysically *de re* one, precisely when that expression is directly referential, as grasping the content of such an expression requires a real cognitive relation to its referent.

This is an answer that only a neo-Russellian is in a position to offer. This is because it presupposes that singular propositions are the contents of the attitudes. One serious problem facing those who reject neo-Russellianism is to explain the intuition that (16) does not entail (17). While a complete survey of the options is out of the question here, it seems that there are two main options. The first is to reject the intuition, claiming that (16) does entail (17). This is to accept a form of *latitudinarianism* about *de re* attitudes, according to which (nonempty) designating terms within propositional attitude verbs freely export outside the scope of propositional attitude verbs. (Defenses of this view can be found in Baker 1982, Chisholm 1976, and Sosa 1970, 1995.) This view does not comport well with the intuition that there is an important difference between the cognitive states of Sally and Brenda. The second option is to accept that (16) does not entail (17) and seek to provide an account of the conditions under which such an entailment obtains, consistent with the thesis that the contents of thought are always fully conceptualized and Fregean. Kaplan 1969 develops the best version of this option. He asks whether Ralph’s believing that the shortest spy is a spy on the grounds that there are finitely many spies and none of them have exactly the same height suffices for Ralph’s having a *de re* belief concerning the shortest spy that he is a spy. Kaplan claims that it does not, thus agreeing that an inference like that of (17) from (16) is not generally valid. Kaplan went on to complicate his simple account of *de re* belief by requiring *vivid* names *of* the object of belief in order for a term to export outside the scope of an attitude verb. The requirements of *of*-ness and *vividness*, however, or any other condition of their kind, seem contrary to Fregeanism, as such notions seem to suggest a distinction between directly referential and descriptive terms and involve direct cognitive relations between the mind and external reality, which leads to some form of Russellianism. One can find, then, the seeds of Kaplan’s ultimate anti-Fregeanism already present in his robust defense of a Fregean account of quantifying in and *de re* belief.

The issues involving the *de re/de dicto* distinction are very complex. In this short note we have distinguished three different conceptions of that distinction. Exactly how these different conceptions line up is controversial. We have tried to explore some connections one might forge between the view one takes on the nature of propositional attitudes and one’s conception of the *de re/de dicto* distinction.
