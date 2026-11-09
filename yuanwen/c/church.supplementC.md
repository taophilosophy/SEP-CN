# church — supplementC（supplement）

> （《church》词条补充材料，源：plato.stanford.edu/entries/church/supplementC.html）

#### Supplement to Alonzo Church

## C. Applications of the Logistic Method

- C.1 The Slingshot Argument
- C.2 The Translation Argument (CTA) and Mates’ Puzzle
- C.3 Burge’s Reply to Church on Mates’ Puzzle
- C.4 Church on Quine’s Paradox About Modality

### C.1 The Slingshot Argument

A natural reaction to this argument is to think that while it works for an extensional language, it cannot be extended to a language containing modal constructions or other intensional elements. For example, although “Scott is Scott” is a necessary truth (or close enough), “Scott is the author of Waverley” is not, and this might seem to translate into a counterexample to (A)—the principle that co-denoting names or definite descriptions are interchangeable—assuming the conclusion of Church’s argument that sentences denote their truth values. But (A) is neutral as to how such terms as “Scott” behave in modal or other intensional constructions and so at the very least more needs to be said if this criticism is to stick.

In fact, in his 1943 review of Carnap’s (1942), Church gives a version of the Slingshot (the first, in fact) that is independent of the distinction between extension and intension and applies to sentences of any complexity:

> However, if a language, in addition to certain other common properties, contains an abstraction operator “$(\lambda x)$” such that “$(\lambda x)(\ldots)$” means “the class of all $x$ such that …”, then—independently of the question whether the language is intensional or extensional—it is possible to prove that the designata of sentences of the language must be truth values rather than propositions. (1943a [BE: 260])

The following is a somewhat pared down version of Church’s argument (cf. the entry on truth values):

$$ \tag{1} S $$ $$ \tag{2} \{x: x = x \amp \{ \textrm{not-}S\} = \Lambda $$ $$ \tag{3} \Lambda = \Lambda $$

Here $S$ is any true sentence. $\Lambda$ is the empty set. Line (1) records that $S$ is true. Line (2) is obviously true since “not-S” is false, and so $\{x: x = x \amp \textrm{not-}S\}$ has no elements. (1) and (2) are logically equivalent, so assuming that logically equivalent sentences have the same denotation, (1) and (2) denote the same thing. (3) may be derived from (2) by (A). Thus (1) and (3) must have the same denotation; but as Church exclaims, they are as different as can be: “one sentence is L-true and the other not!” ((3) is “L-true” (a logical truth), while $S$ may be assumed not to be.)

This argument relies not only on (A) but also on

**(C)**

Logically equivalent sentences have the same denotation.

Other versions, such as Gödel’s, make the same assumption. (Note that (C) is stronger than (B) in the main text, since logical equivalence is weaker than synonymy.) For more on the Slingshot and its connection to other issues discussed in this entry—such as compositionality and synonymy—see the postscript to (Salmón 2010).

### C.2 The Translation Argument (CTA) and Mates’ Puzzle

Church also employed the CTA for another purpose (1954)—to resolve a puzzle posed by Mates (1950). Consider the following pair of sentences:

**(1)**

Jones believes that lawyers are wealthy

**(2)**

Jones believes that attorneys are wealthy.

Some philosophers have supposed that (1) and (2) can diverge in truth value, contradicting the principle that synonyms (“lawyer” and “attorney”) are intersubstitutable *salva veritate* (without change in truth value). For example, Jones might think that “attorney” means *law student* and that lawyers are wealthy, so that (1) will be true, and (2) false. (But we will shortly raise a question about this explanation.)

Now, Mates cleverly observed that whether or not such a view is correct, (that (1) and (2) can have different truth values), the mere existence of philosophers who *think* it is correct renders the following false:

**(3)**

No one doubts that whoever believes that lawyers are wealthy believes that attorneys are wealthy.

Yet even such philosophers will acknowledge the truth of the following:

**(4)**

No one doubts that whoever believes that lawyers are wealthy believes that lawyers are wealthy.

It therefore seems that there is an outright counterexample to the principle *that synonyms can be freely substituted for one another without inducing a change of truth value*, provided only that there happen to be philosophers who think the principle is false! For the sake of further discussion, let us call the italicized principle “the synonyms principle” (“**syn**” for short). If **syn** is deemed false by anyone, then (3) and (4) constitute a counterexample to it and **syn** must be abandoned and perhaps replaced by some subtler principle. (Putnam [1954] pursues this latter course.)

But if **syn** is true, the conclusion is inevitable that anyone who entertains the slightest doubt that lawyers are attorneys actually doubts that lawyers are lawyers. Similarly, anyone who believes that lawyers are lawyers is committed to the belief that lawyers are attorneys—even if they believe that “attorney” means *law student*. Church defends **syn** and was prepared to accept such results as these. He argues that those who are not so prepared are confused.

Church’s argument in his (1954) turns on the fact that German has no word for a fortnight as opposed to a period of fourteen days. But the argument is applicable to the lawyer/attorney case too, and we will stick with this example. We have only to imagine a possible language that has no pair of synonyms corresponding to “lawyer” and “attorney” but only a single word, “shmoyer”, say, for either. It is then obvious that the translations into this language, Shmenglish, of (3) and (4) are identical. If now “it is true that” is prefixed to (4) and “it is false that” to (3) and the results are translated into Shmenglish, we have an outright contradiction. Church concludes that one can no more doubt that lawyers are attorneys than one can doubt that lawyers are lawyers.

Church recognizes, however, that someone who thinks it is possible to doubt that attorneys are lawyers and yet not possible to doubt that lawyers are lawyers need not fail to understand that “lawyer” and “attorney” are synonyms. They might simply question the truth of **syn**. But Church argues that such skepticism about **syn** is misdirected. The culprit is not **syn** but rather a related semantical principle concerning the satisfaction of open sentences *mentioning* particular linguistic items. Compare:

**(5)**

Whoever is an attorney is a lawyer

**(6)**

Whoever satisfies “$x$ is an attorney” satisfies “$x$ is a lawyer”.

We are accustomed to thinking of these two conditions as virtually identical, but the subtle difference is that in (5) “attorney” and “lawyer” are *used* whereas in (6) they are *mentioned*, so the two linguistic items are part of the subject matter of (6) but not of (5); and hence the two sentences are arguably not synonymous. In fact, invoking the CTA, Church would argue that the sentences are not synonymous precisely on the grounds that their German translations are not synonymous—since, once again, they would convey different information to a German speaker who does not speak English. Church would now argue that someone who appears to doubt that (5) should instead be understood to doubt that (6), which Church would maintain is possible without doubting that whoever satisfies “$x$ is a lawyer” satisfies “$x$ is a lawyer”.

There are thus two key steps to Church’s reply to Mates. The first is the argument that while (3) and (4) may not *seem* synonymous, in fact they are, since their translations into Shmenglish are synonymous and in fact it is not possible to assign them different truth values. The second step is the argument that the seeming possibility of doubting that attorneys are lawyers can be traced to the real possibility of doubting (6) instead.

Yet it may be felt that each of these steps involves some sleight of hand. How could anyone who understands the meanings of “lawyer” and “attorney” entertain any doubt about (6)? And why should translation into a less expressive language demonstrate anything about English—to wit that (3) and (4) are synonymous? These are fair questions, but they reflect a misunderstanding of Church’s basic point of view (adumbrated further in [supplement E](church.supplementE.md)). First, as Church observes, it is no defect of German that it lacks a special abbreviation such as “fortnight” for a period of fourteen days. From the perspective of formal semantics such abbreviations are in principle eliminable and the language without the abbreviation is no less expressive than the language with it. In the language of arithmetic, for example, we abbreviate “less than or equal to” by “$\le$”, but this does not increase the expressive power of the language. Similarly, Church would view “lawyer”, “attorney” and “shmoyer” as three eliminable (in principle) abbreviations for the same longer phrase:

> a person who is qualified to advise clients on their rights and obligations according to the law as well as to represent them in court and to conduct lawsuits.

Shmenglish is not any less expressive than English in the logical sense. In response, some philosophers will say that even if “lawyer” and “attorney” were introduced to abbreviate the same longer phrase, there remains the question of why they should remain synonymous in all contexts and so remain eliminable. To this day, however, Church’s view that “lawyer” and “attorney” are eliminable abbreviations for the same longer phrase seems to describe the *correct* use of those words; as such, its intuitive appeal is as least as great as that of Mates’ view that (3) and (4) can differ in truth value. But there remains the issue of whether such intuitions track semantic properties in a way that makes them immune to reasonable challenge.

Secondly, it is a curious feature of Church’s discussion that he does not directly address the question of just how someone who understands English could actually doubt that (6) (or Church’s corresponding sentence (18) of (1954)). This must be left an open question. What is clear from Church’s discussion is that the information conveyed by (5) differs from the information conveyed by (6), and so insofar as it is possible to doubt that (6), it is consistent to maintain, as Church would, that while it is not possible to consistently doubt that (5) (which would amount to the doubt that lawyers are lawyers), it is possible to doubt that (6).

Some have thought that Church’s resolution of the paradox of analysis and his resolution of Mates’ problem are incompatible. Anderson remarks of the former that it is “Ingenious, compelling, and undeniably correct” (1998: 145). And yet:

> Church has implicitly assumed, in his argument against Mates, that the indirect senses of [“brother”] and [“male sibling”] are identical because these two expressions are synonymous. (1998: 145)

(Anderson’s examples are “fortnight” and “period of fourteen days”.) Church suggests that the concepts denoted by “brother” and “male sibling” are the *customary senses* that “brother” and “male sibling” express in customary contexts in which they are viewed as denoting classes; in the context of the sentence “$b = ms$” however, the two terms *denote* these customary senses and acquire and *different* indirect senses. (Church does not mention Frege’s notion of indirect sense (*ungerade Sinn*) in his review, but he no doubt would have understood the problem if it had been put to him.)

However, Anderson claims that Church’s reply to Mates requires Church to assume that the indirect senses of a pair of synonyms must be identical. For otherwise, apparently, in our terms there would be no guarantee that the propositions expressed by (3) and (4) are identical, as Church requires. As Anderson says, “Something has to give” (1998). He suggests that Church’s attempted resolution of the Mates Problem must be abandoned in favor of one that again invokes Frege’s distinction between sense and denotation. See Bealer (1982) and Salmón (1993) for different assessments of the problem.

### C.3 Burge’s Reply to Church on Mates’ Puzzle

Church formulates Mates’ problem in terms of the pair of synonyms “fortnight” and “period of fourteen days” using analogues of (3), (4), (5), and (6) of the previous subsection. Corresponding to (3) and (5), Church employs the following sentences, where for readability “SCM” abbreviates the phrase “the seventh consulate of Marius”:

**(1)**

Nobody doubts that whoever believes that SCM lasted less than a period of fourteen days believes that SCM lasted less than a fortnight

**(2)**

Nobody doubts that whoever believes that SCM lasted less than a period of fourteen days believes that SCM lasted less than a period of fourteen days.

Church now observes that the German equivalents of (1) and (2) turn out to be the very same sentence of German, since there is no single word corresponding to “fortnight” in German. It then follows that the German equivalents of (1) and (2) cannot differ in truth value, unless we are to count the German language as inconsistent for merely lacking a special term for “fortnight”. Church also remarks that it cannot be a defect of German that it lacks such term. The lack of a single-word translation of “fortnight” cannot be regarded as a deficiency of German

> else we should be obliged to call it a deficiency of German also that there is no word to mean a period of fifty-four days and six hours. (1954 [BE: 354-5])

Church takes this argument to show that the perception that (1) and (2) might differ in truth value (and therefore in meaning) is an illusion.

Church suggests that those who think that (1) and (2) differ in truth value are confusing them with certain other sentences that *mention* specific words and phrases of English and that, therefore, via CTA, can be seen *not* to be synonymous.

Let “*Px*” abbreviate the one-place predicate of English “$x$ believes that the SCM lasted a fortnight” and let “*Qx*” abbreviate the one-place predicate of English “$x$ believes that the SCM lasted a period of fourteen days”; and consider the following metalinguistic counterparts of (1) and (2):

**(3)**

Nobody doubts that if $x$ satisfies $Q$, then $x$ satisfies $P$

**(4)**

Nobody doubts that if $x$ satisfies $Q$, then $x$ satisfies $Q$.

Church contends that those who think that (1) and (2) differ in truth value and thus in meaning are confusing them with (3) and (4), respectively. A German speaker who knows no English but who knows a little logic might well assent to the German translation of (4), call it, and dissent from the German translation of (3) precisely on the grounds that they themselves have the relevant doubt in the one case, and lack it in the other. Church concludes with the following memorable summary:

> Granted this, let us translate into German “Mates doubts that (15) but does not doubt that (14)”. As the resulting German sentence is a direct self-contradiction, and as it cannot matter to the soundness of our reasoning whether we carry it out in English or in German, we must conclude that Mates (whatever he himself may tell us) does not really so doubt-and that he must have mistaken the doubt that (18) for the doubt that (15). (1954 [BE: 355])

The quoted sentence is:

**(5)**

Mates doubts that whoever believes that the SCM lasted a period of fourteen days believes that the SCM lasted a fortnight but does not doubt that whoever believes that the SCM lasted a period of fourteen days believes that the SCM lasted a period of fourteen days.

Its metalinguistic counterpart is:

**(6)**

Mates doubts that if $x$ satisfies $Q$, then $x$ satisfies $P$ but does not doubt that if $x$ satisfies $Q$, then $x$ satisfies $Q$.

Church’s concluding argument is that since the German translation of (5) is a direct contradiction, it cannot be true, and (6) must be true instead. As noted above, however, Church never addresses the question of how (6) could be true.

The CTA has come in for some harsh criticism—even from prominent philosophers, some of whom dismiss the argument out of hand (see Salmón 2001: fn. 4 for references). Most of this criticism can be safely ignored. But there is one argument due to Tyler Burge that is worth rehearsing, since it serves to reveal the (perhaps somewhat hidden) force of the CTA.

Burge remarks that

> Interpreting Bates’s doubt as metalinguistic will enable one to avoid attributing to Bates the original object-language doubt, only if one denies that Bates believes the most obvious truisms connecting metalinguistic semantical sentences with the object-language sentences. (1978: 123; “Bates” is a fictional stand-in for Mates)

One such alleged truism is that in fact

**(7)**

All lawyers are attorneys

**(8)**

Whoever satisfies “$x$ is a lawyer” satisfies “$x$ is an attorney”

are logically equivalent since in general

**(9)**

For any $y$, $y$ satisfies $A(x)$ if and only if $A(y)$,

is a logical truth about the satisfaction relation. This appears to entail both of the following:

**(10)**

For any $y$, $y$ satisfies “$x$ is a lawyer” if and only if $y$ is a lawyer

**(11)**

For any $y$, $y$ satisfies “$x$ is an attorney” if and only if $y$ is an attorney;

And these equivalences can be used to show that (7) and (8) are logically equivalent. Mates’ puzzle is thereby restored. Any doubt about (8), which Church concedes is possible, reduces to a doubt about (7), which Church claims amounts to the doubt that lawyers are lawyers.

Notice, however, that the left-to-right implication of (11) is justified only on the assumption that “$x$ is an attorney” means in the language in which (11) is written—English plus variables—that $x$ is an attorney. Without this assumption, there is no basis for the implication. This is exactly the situation we encountered in section 3.3 of the main text with the inference from the sentences (3) to (2) of that section. A person who lacks this piece of information is not in a position to deduce (7) from (8), and this stops Burge’s argument in its tracks. The formal sentence (9) obscures the problem since it obscures the fact that the formula “$A(x)$” is mentioned, whilst the formula “$A(y)$” is used. (Here “$y$” functions as a mere place-holder and “$A(y)$” is short for something like “it is the case that $y$ has the property or belongs to the class $A$”) Furthermore, it is built into the symbolism used in (9) that “$A(x)$” means that $A(x)$ in the formal language in which (9) is written. But its applications to natural language are another story.

Burge’s objection is therefore not successful and it joins a myriad of failed objections to and false assessments of the CTA (cf. Salmón 2001). The fundamental point is that expressions of the form “believes that so and so” or “means that so and so” resist sententialist interpretation. This in turn supports the idea, endorsed by both Frege and Church, that “that”-complements are names of propositions or properties as objective, language independent, abstract entities. Church was very firm in his belief in the existence of such things (see §6.3).

### C.4 Church on Quine’s Paradox About Modality

Church discusses Quine’s well-known critique of modal logic in an early review (Church 1943b Postscript 1968) of Quine’s (1943), as well as in a much later paper (1982). Despite all the ink spilt on this subject, Church’s relatively brief remarks are well worth reviewing. Church begins his review with the claim that Quine’s distinction between purely designative occurrences of names and others—occurrences open or not open to substitution of co-designative names—is “fully anticipated” by Frege (1892a):

> who distinguishes in the same way between the ordinary (*gewöhnliche*) and the oblique (*ungerade*) use of a name. In fact the relationship between Quine’s present paper and Frege’s of 1892 is close throughout, even to the use of similar, and in one instance identical, illustrations. Quine’s failure to refer to Frege’s paper indicates that he is unacquainted with it, but it is probable that he is indirectly indebted to Frege through Russell’s 1119 [*sic*]. (1943b [BE: 943])

Church decided, as of the 1968 postscript to (1943b), to call the problem of substitutivity of co-designative names “Quine’s Paradox”. The following three sentences illustrate the paradox:

**(1)**

Necessarily, $9 = 9$

**(2)**

$9 =$ the number of planets

**(3)**

Necessarily, the number of planets $= 9$.

The substitution of “the number of planets” for the first occurrence of “9” in (1), which is true, results in (3), which is false. Quine’s diagnosis was that the modal operator in (1) “seals off” the sentence following it from substitution in much the same way that “so-called” in “Giorgione was so-called because of his size” “seals off” the substitution of “Barbarelli” for “Giorgione” (the occurrence of “Giorgione” is not purely designative). Needless to say, modal logic has not developed on the basis of this idea, but Quine’s purpose was only to draw attention to the problem. Extrapolating from Frege (1892a)—who does not discuss modal logic—the occurrences of “9” in (1) do not denote the number but rather the ordinary sense of “9”—the sense it has in “$9 = 9$” standing alone, and the occurrence of this sentence in (1) denotes the proposition that $9 = 9$.

Church was very keen to see this Fregean idea developed in detail. Instead of treating “necessarily”, “possibly”, “believes that”, “asserts that” and the like as attaching to sentences to form new sentences (i.e., as sentential operators syntactically on a par with sentential connectives) they should rather be seen as predicates attaching to names of propositions “and the result of prefixing a modal operator to a sentence is simply not well-formed”. But Church also considers alternative resolutions of the paradox more closely related to the language of *Principia Mathematica.* He mentions, for example, a proposal of Quine’s to treat names as denoting not objects but rather individual concepts. Accordingly, (2) is false and the faulty inference is blocked. Such a proposal, among several others, has been developed independently of the system of *Principia.*

In both the postscript (1968) and (1982), Church discusses another—now famous—problem that Quine raises for modal logic. This concerns not names but variables of quantification. Church notes first that Quine’s paradox is essentially the same as the puzzle about King George IV and Sir Walter Scott of Russell’s (1905) and so

> It is not surprising that Smullyan is able to resolve Quine’s paradox by means of Russell’s theory of descriptions. (1982 [BE: 810])

See Smullyan 1947 and 1948. But now a further problem arises. Elaborating on remarks by Quine, Church notes that the following theorems are “hardly avoidable” if modal logic is formulated using sentential operators:

$$\tag{4} \nsim F(x) \supset_x \hdot F(y) \supset_y x\ne y $$ $$\tag{5} (x) \sim \Diamond x\ne x $$ $$\tag{6} \Diamond[x \ne y] \supset_{xy} x\ne y.$$

(Note that Church adopts the following notational conventions from Russell’s (PM). First, a connective can take a variable as subscript: that variable becomes a universal quantifier whose scope is precisely that of the connective. Second, a dot placed before a connective or (as above) a quantifier brackets a proposition.) (6) follows from (4) and (5), which may be taken as axioms definitive of equality. Church says of (6) that it is a version of Murphy’s Law: What can go wrong will go wrong! He also formulates a parallel argument using belief in place of possibility:

**(7)**

For every $x$ and every $y$, if George IV does not believe that $x\ne x$, if George IV believes that $x\ne y$, then $x\ne y$.

This is merely another substitution instance of (4), and hence assuming that

**(8)**

For every $x$, George IV does not believe that $x\ne x.$

It follows that

**(9)**

For every $x$ and every $y$, if George IV believes that $x\ne y$, then $x\ne y$.

And it does seem to follow from (9) that if George IV believed, as he might have believed at some point, that Scott was not the author of Waverley, then Scott didn’t write Waverley!

Church’s aim is to show that if intensional logic is formulated using sentential operators rather than names of propositions, such anomalies result. But in the case of modal logic, at least, his argument has not been influential. (6) and the necessity of identity are now accepted as theorems of quantified modal logic with identity. We believe that (9) and the like deserve further attention. The issue is closely related to a remark of Church’s summarizing Quine’s query of quantified modal logic. Assume that George IV believed that the author of Ivanhoe and the author of Waverley are one and the same, but that he did not believe that Scott wrote Waverley. Then let us ask for what objects (or individuals) $y$ we have that

**(10)**

George IV believes that $y$ wrote Waverley.

The ordinary notion of belief seems to require that although (10) holds when $y$ is specified in a special way, namely as having written *Ivanhoe*, it may yet fail when the same $y$ is specified in some other way, for example as “scottizer”.

Church’s judgment is that this form of Quine’s paradox is more telling than the previous one concerning modality—it is the problem of the “transparency of belief”—and he terms the problem “Russellian” on the grounds that Russell’s theory of descriptions leads directly to it. Nevertheless,

> The sort of essentialism to which the transparency of notions such as belief and necessity leads does not rise above the level of variables and primitive constants. (1982 [BE: 813])

For example, the universal quantifiers implicit in (6) cannot be instantiated to definite descriptions. Although it is possible that Scott did not write *Waverley*—and so was not identical to that author, supposing there was one—, it does not follow that Scott in fact did not write *Waverley*. By now, this matter has received a good deal of attention (see Fitting & Mendelsohn, 1998). (It’s worth mentioning parenthetically that the general form of argument leading from (4) to (6) or from (7) to (9) has frequently been used to argue for other theses—for example, that there is no such thing as vague identity.)

To avoid these problems with modal logic, Church suggests two ways out: One is to eliminate names altogether by replacing them with predicates—“Scott”, becomes “Scottizes”—a method traceable to Russell. But this still leaves the predicates which themselves are names of attributes, and the attempt to eliminate these leads to a regress. In any case, this approach would severely restrict the category of names and would require that the variables range over intensional entities—with the possible exception of the individual variables. The alternative is the Fregean method which

> maximizes the category of names and allows names of, and variables for, a wide variety of entities, both intensional and extensional.

Church’s attempt to implement the latter approach resulted in his logic of sense and denotation, but he also worked out a way of implementing the Russellian approach (see [supplement E](church.supplementE.md); another Russellian solution is proposed by Salmón [1986]). It’s important to note, however, that if type restrictions are ignored, the idea of treating modality as a predicate of propositions can lead to contradiction, assuming principles valid in standard modal logics—that what is necessarily true, is true, for example (see Montague 1962; Anderson 1983).
