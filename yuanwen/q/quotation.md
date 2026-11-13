# Quotation
**First published Sat Jul 16, 2005; substantive revision Wed Apr 19, 2023**

*Cappelen, Herman, Lepore, Ernest, McKeever, Matthew*

Starting with Frege, the semantics (and pragmatics) of quotation has received a steady flow of attention over the last one hundred or so years. It has not, however, been subject to the same kind of intense debate and scrutiny as, for example, the semantics of definite descriptions or of propositional attitude verbs. Many philosophers probably share Davidson’s experience: ‘When I was initiated into the mysteries of logic and semantics, quotation was usually introduced as a somewhat shady device, and the introduction was accompanied by a stern sermon on the sin of confusing the use and mention of expressions’ (Davidson 1979, p. 79)[^davidson-1979]. Those who leave it at that, however, miss out on one of the most difficult and interesting topics in the philosophy of language.

Consider the following sentences:[^note-1]

**(1)**

‘Snow is white’ is true in English iff snow is white.

**(2)**

‘Aristotle’ refers to Aristotle.

**(3)**

‘The’ is the definite article in English.

**(4)**

‘Bachelor’ has eight letters.

Quotation interests philosophers and linguists for various reasons, including these:

- When language is used to attribute properties to language or otherwise theorize about it, a linguistic device is needed that ‘turns language on itself’. Quotation is one such device. It is our primary meta-linguistic tool and if you don’t understand quotation, then you can’t understand sentences like (1)–(4). Those who are in the business of theorizing about language are particularly interested in understanding the mechanisms that render (1)–(4) intelligible.
- Theories of quotation address questions not just about *how* quotations refer, but also about *what* they refer to. In this regard, theories of quotation tell us what we are talking about in (1)–(4).
- Quotation is a paradigmatic opaque context, i.e. a context in which substitution of synonymous or co-referential expressions can fail to preserve truth-value. To understand the nature of opacity you must understand how quotation functions.
- Quotation is a device for talking about language, but it does so in a particularly tricky way: somehow quotation manages to use its referent to do (or at least to participate in) the referring. Putting quotation marks around a word creates a device that refers to that very word: ‘‘Aristotle’’ refers to ‘Aristotle’. As such, quotation is a particularly interesting referential device.
- As with all issues in the philosophy of language, theories of quotation harbor assumptions about how best to draw the distinction between semantics and pragmatics, and they do so in a particularly illuminating way.
- Accounting for quotation presents some interesting technical challenges in formal semantics, attempting to resolve which can shed light on our understanding of such fundamental notions as indexicality, monstrosity, and compositionality.

The entry is structured as follows:

## 1. How to Characterize Quotation

Problems arise right at the outset since quotation is not an easy thing to characterize. We start with reflections on how one might try to do so.

### 1.1 Quotation Identified Through Examples

There’s an easy and relatively non-controversial way to *identify* quotation: it is the *sort* of linguistic phenomenon exemplified by the subject in (4) and the direct object[^note-2] in (5); these are instances of *pure* and *direct* quotation, respectively.

**(5)**

Quine said, ‘Quotation has a certain anomalous feature’.

That leaves open the question of which semantic and syntactic devices belong to that sort. Any characterization of a more specific nature, either of a syntactic or a semantic sort, moves into controversial territory immediately.

### 1.2 Quotation Identified Syntactically

A *syntactic characterization* might go something like this: Take two quotation marks— single apostrophes in Britain, double in the United States, double angles in parts of Europe — and put, for example, a letter, a word, or a sentence between the two. What results is a quotation, as in (4)–(5). But then consider the following sentences:

**(6)**

My name is Donald.

**(7)**

*Bachelor* has eight letters.

We can see there are two problems with the syntactic characterization:

- In spoken language, no obvious correlates of quotation marks exist. Spoken utterances of (6) seem often to be *un*accompanied by lexical items corresponding to ‘quote/unquote’.
- Even if attention is restricted to written language, quotation is not invariably indicated by the use of quotation marks. Sometimes, for example, italicization is used instead, as in (7).

Other devices employed as substitutes for quotation marks include bold face, indentation, and line indentation (cf. Quine 1940, pp. 23–24; Geach 1957, p. 82)[^geach-1957][^quine-1940]. There’s no clear limit on the range of distinct written options, other than that they are used as quotation marks, but this renders the syntactic characterization incomplete, and thus, unsatisfactory.

### 1.3 Quotation Identified Semantically

Another tempting strategy is to say that an expression is quoted if it is *mentioned*. There are two problems with this characterization.

- Several theorists want to distinguish between mention and quotation (see Section 3.5). This definition would rule their theories out by stipulation.
- This characterization is no clearer than the intuitive distinction between use and mention, and matters become even more complicated as soon as we do try to characterize ‘mention’ and ‘use’. Isn’t ‘bachelor’ in (4) in some sense used to refer to itself? If the response is that it is used, but not with its normal semantic value, then we are left with the challenge of defining ‘normal’ and ‘abnormal’ semantic values. That, again, leads immediately to controversy.

In order to remain as neutral as possible, we will stick with a simple identification-through-examples strategy, and emphasize that it is an open question as to how to identify the sort of linguistic devices to which the subject in (4) belongs.

## 2. Basic Quotational Features

Quotation is a subject matter that brings together a rather spectacular array of linguistic and semantic issues. Here are six basic quotational features of particular importance (BQ1–BQ6, for short) that will guide our search for an adequate account:

**BQ1.** *In quotation you cannot substitute co-referential or synonymous terms salva veritate*.

An inference from (4) to (8), for example, fails to preserve truth-value.

**(4)**

‘Bachelor’ has eight letters

**(8)**

‘Unmarried man’ has eight letters

No theory of quotation is adequate unless it explains this feature (and no theory of opacity is complete before it explains why quotation has this feature).

**BQ2.** *It is not possible to quantify into quotation.*

(9), for example, does not follow from (4):

**(9)**

$(\exists x)$(‘$x$’ has eight letters)

An adequate theory of quotation must explain why not. The product of quoting ‘$x$’ is an expression that refers to the 24ᵗʰ letter of the Roman alphabet. The point is that quotation marks, at least in natural language, cannot be quantified into because they trap the variable; what results is a quotation that refers to that very variable. Together, BQ1 and BQ2 place tough constraints on developing a compositional theory for quotation: **BQ1** would suggest quotational environments are opaque yet opaque environments often permit quantifying in which, per **BQ2**, quotation doesn’t. For discussion of compositionality and quotation, see Pagin and Westerståhl 2010, Bazzoni 2016, and Rabern 2022.

**BQ3.** *Quotation can be used to introduce novel words, symbols and alphabets; it is not limited to the extant lexicon of any one language.*

Both (10) and (11) are true English sentences:

**(10)**

‘$\Phi$’ is not a part of any English expression.

**(11)**

‘❦’ is not an expression in any natural language.

An adequate theory of quotation must explain what makes this practice possible.

**BQ4.** *There’s a particularly close relationship between quotations and their semantic values.*

“lobsters” and its semantic value are more intimately related than ‘lobster’ and its semantic value, i.e., the relationship between “lobster” and ‘lobster’ is closer than that which obtains between ‘lobsters’ and lobsters. Whereas the quotation (i.e., “lobster”), in some way to be further explained, has its referent (i.e., ‘lobster’) contained in it, the semantic value of ‘lobsters’, i.e., lobsters, are not contained in ‘lobster’. One way to put it is that an expression e is *in* the quotation of e. No matter how one chooses to spell this out, any theory of quotation must explain this relationship.

**BQ5.** *To understand quotation is to have an infinite capacity, a capacity to understand and generate a potential infinity of new quotations.*

We don’t learn quotations one by one. Never having encountered the quotation in (10) or (11) does nothing to prohibit comprehending them (Christensen 1967, p. 362)[^christensen-1967] and identifying their semantic values.

Similarly, there doesn’t seem to be any upper bound on a speaker’s ability to generate novel quotations. One natural explanation for this is that quotation is a *productive* device in natural language.

**BQ6.** *Quoted words can be simultaneously used and mentioned.*

This is an important observation due to Davidson, as exemplified in (12).[^note-3]

**(12)**

Quine said that quotation ‘has a certain anomalous feature’.

(12) is called a ‘mixed quotation’. This is because it mixes the direct quotation (as in (5)) and indirect (as in (13)).

**(5)**

Quine said ‘quotation has a certain anomalous feature’.

**(13)**

Quine said that quotation has a certain anomalous feature.

In this regard, the quotation in (12) is, in an intuitive sense, simultaneously used and mentioned. It is used to say what Quine said (*viz.* that quotation has a certain anomalous feature), and also to say that Quine used the words ‘has a certain anomalous feature’ in saying it.

Mixed quotation had not been much discussed prior to Davidson (1979) but it has recently taken center stage in discussions of theories of quotation. For those who believe themselves unfamiliar with the data, we point out that mixed quotation is one of the most frequently used forms of quotation. Casually peruse any newspaper and you will find passages like the following from the *New York Times*:

> *NYT* Dec 7, 2004: The court ruled that the sentence was invalid because the document signed into law by President Bill Clinton contained a phrase that was illogical. The law said that defendants like Mr. Pabon, who was convicted two years ago of advertising to receive or distribute child pornography over the Internet, should be fined or receive a mandatory minimum sentence of 10 years ‘and both.’ The appeals court said this language ‘makes no sense.’

In the 21st century, mixed quotation has become one of the central topics in the theory of quotation: a range of interesting data has been brought to light and a flurry of theories have been defended. In Section 4 below we introduce some of the data.

In what follows we will refer back to these six features and make the following assumption:

It is a necessary adequacy condition on a theory of quotation that it either explains how quotations can exhibit features (BQ1)–(BQ6), or, if it fails to do so, then it must present an argument for why any unexplained feature doesn’t require explanation.

Before going on, an important note: quotation, perhaps more than any other area of language, is difficult because not only is there no consensus about what the correct theory is, but there’s also basic disagreements about the space of options, and about the data to be accounted for. We’ll see this below, but it’s important to bear in mind that when it comes to quotation, the consensus is that there’s no consensus, and disagreement is the norm.

### 2.1 Guiding Questions for Theories of Quotation

BQ1–BQ6 play an important role because theories of quotation are attempts to answer certain questions, and those questions won’t have satisfactory answers unless BQ1–BQ6 are accounted for. Three questions can be thought of as the guiding questions for a theory of quotation:

Q1. In a quotation, *what* does the referring? There are three options:

- The quotation marks
- The expression between the quotation marks
- A complex of the expression and the quotation marks

Alternatively, one might hold that quotations fail to refer at all, but rather that speakers refer contingent upon the intentions with which they use an expression—with or without quotation marks.

Q2. *How* do quotations refer?

Are they names, descriptions, demonstratives, functors or some *sui generis* linguistic category?

In addition to Q1 and Q2, theories of quotation often try answer a third question:

Q3. *What* do quotations refer to?

What kinds of objects are picked out? Is it always the same object or are quotations ambiguous?[^note-4]

Our primary focus in what follows will be in Q1 and Q2, but along the way we will also address Q3. (Section 5 is entirely devoted to Q3.)

### 2.2 The Use-Mention Distinction

It is standard practice in philosophy to distinguish the *use* of an expression from the *mentioning* of it. Confusing these two is often taken to be a philosophical mortal sin. Despite its ubiquitous appeal, it is controversial exactly how to draw the distinction. The initial thought is easy enough. Consider (D1) and (D2):

D1. Jim went to Paris

D2. ‘Jim’ has three letters

In (D1) the word ‘Jim’ is used to talk about (or signify, or denote) a person, i.e. Jim, and the sentence says about that person that he went to Paris. In (D2) the word is not used in that way. Instead, ‘Jim’ is used to talk about (or signify or denote) a word, i.e. ‘Jim’, and the sentence says about that word that it has three letters[^note-5]. In (D1), ‘Jim’ is being *used* and in (D2) it is being *mentioned*.

The initial thought seems right as far as it goes, but it might be thought it doesn’t go far enough. One might hope that we could say *more* to flesh it out in an uncontroversial way, a theory-neutral way that any party to the debate could agree on. In fact, though (and this is not recognized enough), this is not straightforward. To see this, consider a couple of ways to try to build on the initial characterization:

1. Expression $E$ is mentioned in sentence $S$ just in case $E$ is quoted in $S$.

A problem with this is that according to some theories, an expression can be mentioned without being quoted (see Objection 3 in section 3.3.2).

1. Expression $E$ is mentioned in sentence $S$ just in case it is used to refer to itself in $S$.

This is problematic in a couple of ways. First, notice that according to (ii), $E$ must be used in order to mention it; that’s potentially puzzling. More significantly, it is controversial whether standard meta-linguistic devices such as quotation are referring expressions. The theories presented in sections 3.2 and 3.3 treat quotations as descriptions. If descriptions are quantified expressions, then quotations are quantifiers, and quantifiers are typically not treated as referring expressions. Proposals along the lines of (ii) would also have to ensure that ‘the first seven words in this sentence’ in (D3) don’t end up referring to ‘the first seven words in this sentence’:

D3. The first seven words in this sentence contain thirty-two letters.

What this suggests is that any attempt to characterize the distinction between *use* and *mention* more sophisticated than the initial characterization in this section will need to address at least some of the tricky issues that face the various theories of quotation we describe in what follows.

## 3. Five Theories of Quotation

There are, roughly, five kinds of theories of quotation that have been central to the discussion of quotation: the Proper Name Theory, the Description Theory, the Demonstrative/Paratactic Theory, the Disquotational Theory, and the Use/Identity Theory. (See here Maier’s taxonomy (2014b), which just includes the first four theories, and which evaluates them according in terms of formal desiderata like compositionality and productivity, and cf. Saka 2013, which includes ten. This divergence, incidentally, is a good illustration of the point we made above about lack of consensus among theorists of quotation.) In the following sections we discuss each of these and review their strengths and weaknesses.

### 3.1 The Proper Name Theory

It is now almost a tradition in the literature on quotation to include a brief dismissive discussion of the Proper Name Theory of Quotation. This view is described, although not clearly endorsed, in passages in Quine and Tarski (e.g., Quine 1940, pp. 23–26; 1961, p. 140; Tarski 1933, p. 159ff)[^quine-1940][^tarski-1933], and comments in passing in both Reichenbach (1947, p. 335) and Carnap (1947, p. 4) strongly suggest they were adherents. That said, there is some debate about whether Quine and Tarski ever held the view (see, e.g., Bennett 1988, Richard 1986, Saka 1998, and Gomez-Torrente 2001)[^bennett-1988][^gomez-torrente-2001][^richard-1986][^saka-1998]. And so it is worth mentioning that although we quote both Quine and Tarski below, we do not thereby mean to attribute the Proper Name Theory to either of them; we do so merely because they describe it clearly.

Until recently, it was generally held that the name theory was ‘an utter failure’ (Saka 1998, p. 114)[^saka-1998], of interest only as showing us how not to theorize about quotation. In recent years, however, there have been at least two defenses of something like the name theory (Gomez-Torrente 2013 and Johnson 2018)[^gomez-torrente-2013][^johnson-2018]. We here present the reasons the name theory was long taken to be a non-starter, as well as the responses to these problems by the authors mentioned above.

According to the Proper Name Theory, quotations are unstructured proper names of the quoted expressions. Quine writes:

> From the standpoint of logical analysis each whole quotation must be regarded as a single word or sign, whose parts count for no more than serifs or syllables. (Quine 1940, p. 26)[^quine-1940]
>
> The personal name buried within the first word of the statement ‘‘Cicero’ has six letters’, e.g., is logically no more germane to the statement than is the verb ‘let’ which is buried within the last word. (Quine 1940, p. 26)[^quine-1940]

Tarski formulates the view as follows:

> Quotation-mark names may be treated like single words of a language, and thus like syntactically simple expressions. The single constituents of these names—the quotation marks and the expressions standing between them—fulfill the same function as the letters and complexes of successive letters in single words. Hence they can possess no independent meaning. Every quotation-mark name is then a constant individual name of a definite expression (the expression enclosed by the quotation marks) and is in fact a name of the same nature as the proper name of a man. (Tarski 1933, p. 159)[^tarski-1933]

#### 3.1.1 Strengths of the Proper Name Theory

The Proper Name Theory nicely accommodates (BQ1)–(BQ3); that is, on this theory we see why co-referential expressions cannot be substituted for one another. According to the Proper Name Theory, the name ‘Cicero’ does not occur in ‘‘Cicero’’; from the mere fact that Cicero = Tully, it does not follow that ‘Tully’ can be substituted for ‘Cicero’ in ‘‘Cicero’’. As Quine puts it, ‘[t]o make substitution upon a personal name, with such a context, would be no more justifiable than to make a substitution upon the term ‘cat’ within the context ‘cattle’ (Quine 1961, p. 141)[^quine-1961]. The Proper Name Theory permits the creation of new quotations much as natural languages permit the introduction of new names. And it prohibits quantifying in, since each quotation is a single word, and so there is nothing to quantify into. To see this, consider the following. We obviously can’t quantify into words. The idea barely makes sense. Imagine we have the sentence ‘there is a birth dearth in Europe’. We can’t quantify into, say, the word ‘dearth’. The following doesn’t make sense, where we’re trying to express an existential generalization satisfied by the word or string ‘earth’:

**(14)**

$(\exists x)$ (there is a birth $dx$ in Europe)

This is nonsense: ‘dx’ just can’t mean ‘d’ combined with the value of the variable ‘x’. Now consider:

**(15)**

‘bachelor’ has eight letters.

**(16)**

$(\exists x)$(‘$x$’ has eight letters)

This is also ill-formed. The proper name theorist can explain it. Remember, for the proper name theorist, quotations are akin to names and quotation marks are akin to letters. But then if that’s so, (16) is on a par with (14): both are trying to quantify into expressions (the former expressions beginning with ‘d’ and the latter expressions beginning with ‘ and ending with ‘). The obvious badness of (14) can explain the badness of (16), for the proper name theorist.

#### 3.1.2 Weaknesses of the Proper Name Theory

Here are three objections to the Proper Name Theory of Quotation. (The main objections are in Davidson (1979, pp. 81–83), though some were anticipated by Geach (1957, p.79ff).)

**Objection 1:** *The Proper Name Theory cannot explain how we can generate and interpret an indefinite number of novel quotations (see BQ5).*

If quotations were proper names and lacked semantic structure altogether, then there would be no rule for determining how to generate or interpret novel quotations. To understand one would be to learn a new name. (Remember, the quotation marks, according to Quine, carry no more significance than the serifs you see on these letters.) But (11), e.g., can be understood by someone who has never encountered its quoted symbol before.

**(11)**

‘❦’ is not a letter in any language

Understanding (11) is not like understanding a sentence with a previously unknown proper name. Upon encountering (11), it would seem that you know exactly which symbol is being referenced in a way that you do not with a name you’ve never before encountered.

For a long time, this objection was thought fatal. However, a paper by Mario Gomez-Torrente (2013) suggests a way to square something like the name view with **Objection 1**. In brief, he points out that there are some names that can be indefinitely generated and interpreted. For example, street names. ‘East 6th Street’, presumably, is a bona fide name, but one doesn’t either need to individually bestow it on the particular street it applies to (the street between East 5th and East 7th), nor does one need to have already learned it to understand what ‘East 6th Street has some great bars’ means.

**Objection 2**: *There’s a special relationship between quotations and their semantic values (see BQ4).*

According to the Proper Name Theory, the relationship between “lobsters” and ‘lobsters’ is no closer than the relationship between ‘lobsters’ and lobsters. That seems to miss the fundamental aspect of quotation spelled out in (BQ4).

Davidson summarizes these first two objections succinctly:

> If quotations are structureless singular terms, then there is no more significance to the *category* of quotation-mark names than to the category of names that begin and end with the letter ‘a’ (‘Atlanta’, ‘Alabama’, ‘Alta’, ‘Athena’, etc.). On this view, there is no relation, beyond an accident of spelling, between an expression and the quotation-mark name of that expression. (Davidson 1979, pp. 81–82; cf., also, Garcia-Carpintero 1994, pp. 254–55)[^davidson-1979][^garcia-carpintero-1994]

Again, however, some work has pushed back against these old objections. Michael Johnson (2018) points to some names which bear special relationships to their referents. In particular, he points to *onomatopoeia*. For example, ‘buzz’ refers to a sound, a buzzing sound. But the word ‘buzz’, when uttered, makes the sound it refers to. Roughly speaking, Johnson holds that we could view quotations in the same way: as he says, ‘the name of a person sounds like the name of his name’ (2018). For some discussion of Johnson’s view, see Miller 2019.

**Objection 3**: *Proper Name Theory leaves no room for dual use and mention (see BQ6).*

If quotations were proper names, and if their interiors lacked significant structure, there would seem to be no room for dual usage of the kind found in (12); indeed, on the Proper Name Theory, (12) has the same interpretive form as (17):

**(12)**

Quine said that quotation ‘has a certain anomalous feature’.

**(17)**

Quine said that quotation Ted.

That is, the Proper Name Theory fails to account for (BQ6).

Other objections have been raised against the Proper Name Theory of Quotation. For further discussion, see Davidson (1979), Cappelen and Lepore (1997b) and Saka (1998). Whether the recent defenders of the name theory will be able to take it off its deathbed remains to be seen, but it’s fair to say that their work shows that reports of its demise have been, at least, a bit premature.

### 3.2 The Description Theory of Quotation

The Description Theory of Quotation was introduced in order to guarantee that ‘a quoted series of expressions is always a series of quoted expressions’ (Geach 1957, p. 82)[^geach-1957] and not ‘a single long word, whose parts have no separate significance’ (*ibid*., p. 82). According to this theory, there is a set of basic units in each language: words, according to Geach (*ibid*., Ch. 18 and 1970); letters, according to Tarski (1956, p. 160) and Quine (1960, p. 143, p. 212)).[^note-6]

This view retains the Proper Name Theory for basic quotations, e.g., according to Quine, “$a$” is a name of one letter, “$b$” a name of another, etc. For Geach, each word has a quotation name. Complex quotations, i.e., quotations with more than one basic unit, are understood as descriptions of concatenations of the basic units. Here is an illustration from Geach (where ‘-’ is his sign for concatenation):

> …the quotation ‘‘man is mortal’’ is rightly understood only if we read it as meaning the same as ‘‘man’-‘is’-‘mortal’’, i.e., read it as *describing* the quoted expression in terms of the expressions it contains and their order. (Geach 1957, pp. 82–83)[^geach-1957]

For Quine and Tarski, (4) gets analyzed as (18):

**(4)**

‘Bachelor’ has eight letters.

**(18)**

‘B’-‘a’-‘c’-‘h’-‘e’-‘l’-‘o’-‘r’ has eight letters

where ‘-’ is their sign for concatenation and the individual quotations are names of the letters.

Davidson characterizes the difference between the two versions as follows:

> In primitive notation, which reveals all structure to the eye, Geach has an easier time writing (for only each word needs quotation marks) but a harder time learning or describing the language (he has a much larger primitive vocabulary—twice normal size if we disregard iteration). (Davidson 1979, p. 84)[^davidson-1979]

That is to say, if Geach’s theory were true, the appropriate representation of (4) is simply (4), whereas for Tarski and Quine it’s the much more unwieldy (18). On the other hand, a Geachian language has (at least) twice as many words as we might expect: for each word in the dictionary, there would also be the word that stands for that word (got by enclosing the initial word in quotation marks).

#### 3.2.1 Strengths and Weaknesses of the Description Theory

In one respect the Description Theory is an immense improvement over the Proper Name Theory: it deals with no more than a finite set of basic names, thus, potentially accommodating (BQ5). In other respects, however, the theory is, by a wide consensus, not much of an improvement over the Proper Name Theory. At the basic level, the theory still treats quotations as names. So, at that level, it inherits many of the problems confronting the simpler Proper Name Theory. Some of the more obvious objections are these (again we mention only some of the most obvious ones here since the theory is not central to contemporary discussions):

- At the basic level (i.e., the level of words or letters), there’s no rule for determining how to interpret and generate novel quotations (BQ3). This is so because there is no *a priori* reason to believe there are finitely many basic expressions (cf., Lepore 1999)[^lepore-1999].
- At the basic level, it doesn’t explain the special relationship between the expression and the quotation of that expression (BQ4). It’s obvious to us that “Sam” and “Alice” do not refer to the same expression, but how can Geach explain this triviality if both are just proper names; ditto for Quine with respect to “a” and “b” (cf., Davidson 1979, p. 87)[^davidson-1979].
- At the basic level, it fails to account for dual use and mention (BQ6). This is particularly a problem for Geach’s version. Any account, including the Proper Name Theory, according to which the semantic function of word-tokens inside quotation marks is just to refer to word-types (or some other type of linguistic entity) fails to assign correct truth-conditions to (12). In essence, it predicts that (12) is syntactically equivalent to something like ‘Quine said that quotation the phrase’, which is ungrammatical as containing a definite description where a verb phrase should be.
- According to Davidson (1979, pp. 86–87), the Description Theory can’t explain why we can’t quantify into quotation (i.e. it fails to account for BQ2). Roughly, the thought seems to be that we can existentially generalize from (4) to ‘some word has eight letters’. But by a similar sort of reasoning, we should be able to move from (18) to ‘some letter is that such that ‘B’-‘a’-‘c’-‘h’-‘e’-‘l’-it-‘r’ has eight letters’. But clearly no such move can be made.

### 3.3 The Demonstrative Theory of Quotation

The seminal paper on quotation in the twentieth century is, by almost universal consensus, Davidson’s ‘Quotation’ (1979). It is without comparison the most discussed and influential paper on the subject. The view Davidson defends is called the Demonstrative Theory. (It is also called the Paratactic Theory, though we shall use the former label in our discussion.) The Demonstrative Theory is presented in the final pages of ‘Quotation’ and the key passages are these:[^note-7]

> …quotation marks…help refer to a shape by pointing out something that has it…The singular term is the quotation marks, which may be read ‘the expression a token of which is here’. (Davidson 1979, p. 90)[^davidson-1979]
>
> On my theory which we may call the demonstrative theory of quotation, the inscription inside does not refer to anything at all, nor is it part of any expression that does. Rather it is the quotation marks that do all the referring, and they help to refer to a shape by pointing out something that has it. (Davidson 1979, p. 90)[^davidson-1979]
>
> Quotation marks could be warped so as to remove the quoted material from a sentence in which they play no semantic role. Thus instead of:
>
> > ‘Alice swooned’ is a sentence.
>
> we could write:
>
> > Alice swooned. The expression of which this is a token is a sentence.
>
> (Davidson 1979, p. 90)[^davidson-1979]

The Demonstrative Theory has three central components. First, the quotation marks are treated as contributing a definite description containing a demonstrative to sentences in which they occur, i.e., the quotation marks in (4) become ‘The expression of which this is a token’, as in (19):

**(4)**

‘Bachelor’ has eight letters.

**(19)**

Bachelor. The expression of which that is a token has eight letters.

Second, in the logical form of a sentence containing a quotation, the token that occurs between the two quotation marks in the surface syntax is displaced, so to speak, from the sentence containing the quotation. What occurs between the quotation marks in the surface syntax is not part of the sentence in which those quotation marks occur. Having been displaced from its surface syntactic position, it serves as an object apt for demonstrative reference (An analogy: if I utter ‘consider the word ‘apples’.’, ‘apples’ becomes available for demonstrative reference, as when I continue ‘It is an English word.’)

Third, utterances of quotation marks, by virtue of having a demonstrative/indexical ingredient, refer to the expression instantiated by the demonstrated token, i.e., the expression instantiated by the token that in surface syntax sits between the quotation marks.

#### 3.3.1 Strengths of the Demonstrative Theory

The Demonstrative Theory is attractive for at least five reasons. First, to grasp the function of quotation marks is to acquire a capacity with infinite applications (BQ5). The Demonstrative Theory explains why: there’s no limit to the kinds of entities we can demonstrate. Hence, (BQ5) is explained without making quotation a productive device (for elaboration see Cappelen and Lepore 1997b)[^cappelen-1997b].

Second, opacity is explained (BQ1): There’s no reason to think that two sentences demonstrating different objects will have the same truth-value. (4) and (8) demonstrate different objects, so there’s no more reason to think the move from (4) to (8) is truth preserving than there is to think that the move from (20) to (21) is:

**(20)**

That’s nice.

**(21)**

That’s nice.

Third, we have an elegant explanation of mixed quotation, i.e., we can explain (BQ6). Davidson says:

> I said that for the demonstrative theory the quoted material was no part, semantically, of the quoting sentence. But this was stronger than necessary or desirable. The device of pointing can be used on whatever is in range of the pointer, and there is no reason why an inscription in active use can’t be ostended in the process of mentioning an expression. (Davidson 1979, p. 91)[^davidson-1979]

This, according to Davidson, is what goes on in (12). A token that is being used for one purpose is at the same time demonstrated for another: ‘Any token may serve as target for the arrows of quotation, so in particular a quoting sentence may after all by chance contain a token with the shape needed for the purposes of quotation’ (Davidson 1979, pp. 90–91; cf., also, Cappelen and Lepore 1997b)[^cappelen-1997b][^davidson-1979]. On this view, (12) is understood as (22). (Note: the ‘these’ in (22) is accompanied by a pointing or indexing to the token of Quine’s words.)

**(12)**

Quine said that quotation ‘has a certain anomalous feature’

**(22)**

Quine said, using words of which these are a token, that quotation has a certain anomalous feature.[^note-8]

Fourth, there is no mystery about how to introduce new vocabulary; since there’s no limit to what can be demonstrated, there’s no limit to what can be quoted. (BQ3) is explained.

Finally, quantifying-in is obviously ruled out, since the quoted token is placed outside the quoting sentence, i.e., the Demonstrative Theory can explain (BQ2).

The Demonstrative Theory is both bold and radical. It triggered an entire cottage industry devoted to criticizing and defending it. For proponents, see, for example, Partee 1973; Garcia-Carpintero 1994, 2017, 2018; Cappelen and Lepore 1997b; McCullagh 2007; and Predelli 2008; for critics, see just about anyone else writing on quotation after 1979.

#### 3.3.2 Weaknesses of the Demonstrative Theory

In what follows we present five criticisms of the Demonstrative Theory. Needless to say, the list is not exhaustive (e.g., see Sorensen 2008 and Saka 2011b on the problem of empty quotation)[^saka-2011b][^sorensen-2008], and indeed, each objection has triggered lively discussion which space limitations prohibit our taking up here.

**Objection 1.** *If the Demonstrative Theory were correct, it should be possible for (4) to demonstrate, e.g., a penguin.*

Here is an argument that mimics a range of objections raised against Davidson’s account of the semantics for indirect reports (Burge 1986, Stainton 1999)[^burge-1986][^stainton-1999].[^note-9]

Recall that according to Davidson the logical form of (4) is (19).

**(4)**

‘Bachelor’ has eight letters.

**(19)**

Bachelor. The expression of which that is a token has eight letters.

(19) contains a demonstrative and demonstratives refer to whatever is demonstrated with their use. What is demonstrated on a given occasion depends on the speaker (either the demonstration or the intention or some combination of the two). It should be possible, then, for a speaker to utter (4) and *not* demonstrate the exhibited token of ‘bachelor’. That is to say, if there really is a demonstrative in (19), that demonstrative should have the same kind of freedom that other demonstratives have: it should be able to refer to, for example, a nearby penguin. Of course, no utterance of (4) makes reference to a penguin. So the Demonstrative Theory is wrong.[^note-10] (For replies to this objection see Cappelen and Lepore 1999b.)[^cappelen-1999b]

**Objection 2**. *The Problem of Relevant Features*

According to Davidson, a quotation refers to an expression indirectly, by referring to a token that instantiates that expression. Davidson thinks expressions are *shapes* or *patterns* (see Davidson 1979, p. 90)[^davidson-1979]. A problem for this view is that any one token instantiates indefinitely many distinct shapes or patterns, i.e. many different expressions. So how, on Davidson’s view, do we get from a particular token to a unique type, i.e., from a token to an expression?

Jonathan Bennett formulates the problem as follows:

> Any displayed token has countless features, and so it is of countless different kinds. Therefore, to say the inscription-types instantiated here: Sheep or what amounts to the same thing, the inscription-type each token of which is like this: Sheep is to leave things open to an intolerable degree. How do we narrow it down? That is what I call the problem of relevant features. It urgently confronts the demonstrative theory which must be amplified so as to meet it. (Bennett 1988, p. 403, see also Washington 1992, pp. 595–7.)[^bennett-1988][^washington-1992]

A related worry is this: Read (4) out loud. It seems obvious that a spoken utterance says (makes) the same claim as a written utterance of (4). On the Demonstrative Theory it is unclear why this should be so: the spoken utterance demonstrates a vocal pattern, and the written utterance a graphemic pattern. They seem to be attributing properties to different objects. (Several suggestions are on offer for how to amend the Demonstrative Theory in this respect: cf., Garcia-Carpintero 1994, Cappelen and Lepore 1997b, 1999c, and Davidson 1999.)[^cappelen-1997b][^davidson-1999][^garcia-carpintero-1994]

**Objection 3**. *The Problem of Missing Quotation Marks*

According to Davidson, quotation marks are what are used to do the referring. They are descriptions containing demonstratives whose uses refer to whatever pattern is instantiated by the demonstrated token. This makes the presence of quotation marks essential. Much recent work on quotation argues that we can quote (or do something quote-like) *without* quotation marks and that a theory of quotation should be capable of explaining how quotation can take place in the absence of quotation marks. Here is Reimer’s version of this objection:

Consider the following sentence:

**(7)**

*Bachelor* has eight letters.

Here, we have a case in which an expression is quoted—not by means of quotation marks—but by means of italicization. But surely it would be absurd to suppose (consistently with Davidson’s view) that the italicization of (7)’s subject term is itself a demonstrative expression! (Reimer 1996, p. 135)[^reimer-1996]

The same idea is expressed by Washington (1992):

> In conversation, oral promptings (‘Quote-unquote’) or finger-dance quotes can often be omitted without impairing the intelligibility or well-formedness of the utterance. When I introduce myself, I do not say ‘My name is quote-unquote Corey,’ nor do I make little finger gestures or even use different intonation in order to show that it is my name and not myself that is being talked about. (Washington 1992, p. 588; Saka 1998, pp. 118–19; Recanati 2001; and Benbaji 2004a, 2004b.)[^benbaji-2004a][^recanati-2001][^saka-1998][^washington-1992]

The Demonstrative Theory depends on the presence of quotation marks (inasmuch as they are what get used to do the referring), so if quotation can occur without quotation marks (as in the Reimer and Washington cases), it’s hard to see how the Demonstrative Theory is adequate.

Proponents have been unimpressed. Consider an utterance of (6):

**(6)**

My name is Donald.

Several possible replies can be made by proponents of the Demonstrative Theory. One thing a Demonstrative Theorist might say is that there are no missing quotation marks in (6): they are in the logical form of the sentence, not in its surface syntax.

Alternatively, quotation marks for an utterance of (6) could be generated as conversational or conventional implicatures. (He can’t be saying that Donald, the person, is his name as he knows that that is false, so he must be conversationally implicating that the expression of which he used a token is a name (cf. Garcia-Carpintero 1994, pp. 262–63)[^garcia-carpintero-1994]). Or perhaps we could appeal to the distinction between semantic reference and speaker reference. (6) is grammatically correct but false; nonetheless, someone can succeed in communicating something true about Donald’s name if he succeeds in conveying to his audience his intention to refer to it (cf., Gomez-Torrente 2001)[^gomez-torrente-2001].

Finally, a Demonstrative Theorist can argue that these other quotation-like phenomena are just that—quotation-like. They require a separate treatment. There’s no need for a unified theory (cf., Cappelen and Lepore 2003)[^cappelen-2003].

**Objection 4**. *The Problem of Iteration*

The Demonstrative Theory seems to have difficulty dealing with iterated quotation. (24) refers to the quotation in (23):

**(23)**

‘Smooth’ is an English expression.

**(24)**

“Smooth” is an English expression.

The Demonstrative Theory’s account for (23) is (25).

**(25)**

Smooth. The expression of which that is a token is an English expression

How, then, can the account accommodate (24)? (24), after all, includes *two* sets of quotation marks. It might seem like the Demonstrative Theory would have to treat it as the ungrammatical (26) or the unintelligible (27).

**(26)**

Smooth. That that is an English expression.

**(27)**

Smooth. That. That is an English expression.

This objection has been raised by Saka (1998, pp. 119–20), Reimer (1996), and Washington (1992).

In response, Demonstrative Theorists insist that quotations are not iterative. On this topic, Cappelen and Lepore write:

> Quoted expressions are exhibited so that speakers can talk about the patterns (according to Davidson) they instantiate. The semantic properties of the tokens are not in active use; they are semantically inert…So, quotation marks within quotation marks are semantically inert. (Cappelen and Lepore 1997b, pp. 439–40)[^cappelen-1997b]

For further discussion of whether quotation is a genuinely iterative device, see Cappelen and Lepore (1999a) and Saka (2013).

**Objection 5.** *The Problem of Open Quotation: Dangling Singular Terms*

Recanati (2001) focuses on cases where quoted expressions do not serve as noun phrases in sentences. He has in mind cases like (29) and (30):

**(29)**

Stop that John! ‘Nobody likes me’, ‘I am miserable’… Don’t you think you exaggerate a bit?

**(30)**

The story-teller cleared his throat and started talking. ‘Once upon a time, there was a beautiful princess named Arabella. She loved snakes and always had a couple of pythons around her…’

In these cases it looks like the Demonstrative Theory would have to postulate a dangling singular term, something like (31) or (32):

**(31)**

Stop that John. That. Nobody likes me. That. I am miserable. … Don’t you think you exaggerate a bit?

**(32)**

The story-teller cleared his throat and started talking. That. Once upon a time, there was a beautiful princess named Arabella. She loved snakes and always had a couple of pythons around her…

In response to the idea that (29) is elliptical for (33),

**(33)**

Stop that John! *You say* ‘Nobody likes me’, ‘I am miserable’ … Don’t you think you exaggerate a bit?

Recanati says:

> I deny that [29] and [33] are synonymous. Nor are there any grounds for postulating ellipsis here except the desire to save the theory in the face of obvious counterexamples (Recanati 2001, p. 654)[^recanati-2001].

### 3.4 Disquotational Theory of Quotation

Less baroque than the Demonstrative Theory, the Disquotational Theory is probably the simplest, most natural and obvious account of quotation. It is endorsed by a wide range of authors, often in passing, as if completely obvious. A simple version of it can be found in Richard’s Disquotational Schema (DQR):

DQR: For any expression $e$, the left quote (lq) followed by e followed by the right quote (rq) denotes e (Richard 1986, p. 397)[^richard-1986]

Ludwig and Ray write:

> Its semantic function is given by the following reference clause in the theory: (ref$(\ulcorner$‘E’$\urcorner) =$ E (Ludwig and Ray, 1998, p.163, note 43)

where the ‘$\ulcorner$’ and ‘$\urcorner$’ are the left and right corner quotes. (See also Smullyan 1957, Mates 1972, p. 21; Wallace 1972, p. 237; Salmon 1986, p. 6, Gomez-Torrente 2001, Botteral and Stainton 2005. A nearby view is the minimalism of Cappelen and Lepore 2007; discussion of it can be found in Garcia-Carpintero 2011.)[^cappelen-2007][^gomez-torrente-2001][^mates-1972][^salmon-1986][^smullyan-1957][^wallace-1972]

On this account, quotations are not proper names, or descriptions or demonstratives but rather they are functors that take an expression as their argument and return it as value.

#### 3.4.1 Strengths of Disquotational Theory

The two most obvious strengths of the Disquotational Theory are its simplicity and intuitiveness. If asked how quotation functions, the obvious reply is something along the lines of (DQR). It is also an axiom (or axiom schema) that’s pleasingly simple and requires no complicated assumptions about the surface structure of the sentence (in this respect, it has a clear edge on the Demonstrative Theory).

In addition to be being exceedingly simple and intuitive, this theory easily accounts for three of the Basic Facts about Quotation.

First, it explains opacity: ‘bachelor’ and ‘unmarried man’ have different semantic values because what is between the quotation marks are distinct expressions. An expression’s semantic value is irrelevant for determining the semantic value of the quotation of that expression, thus accounting for (BQ1).

Second, since quotations are functor expressions without internal structure, (BQ2) is explained: there’s no possibility of quantifying into a quotation on this view.

Finally, since quotations, as functors, map all expressions onto themselves, this account can explain the special relationship between a quotation and the quoted expression—namely, identity—thus explaining (BQ4).

#### 3.4.2 Weaknesses of the Disquotational Theory

Even with these advantages, at least three serious difficulties confront the Disquotational Theory.

First, (BQ3) says that we can use quotation to refer to symbols that are not in the English lexicon, as in (9) and (10):

**(9)**

‘$\Phi$’ is not a part of any English expression.

**(10)**

‘❦’ is not an expression in any language.

(DQR) says we can take *any expression* e, put quotation marks around e, and what results is an expression that refers to e. What exactly is meant by ‘any expression’ in (DQR)? Richard offers the following answer:

> It is *easy enough* to come up with a *finite* list of elements (the letters, punctuation symbols, the digits, the space, etc.) and an operation (concatenation) with which one can generate all of the concatenates…If we are formalizing a grammar for a language with quotation names, we would include, as part of the specification of the lexicon, a proviso to the effect that, for each concatenate e, the left quote (lq), followed by e, followed by the right quote (rq) is a singular term (Richard 1986, pp. 386–89, our emphasis)[^richard-1986].

If this is how expressions are generated, how then are we to account for the truth of (9) and (10)? More generally, the worry is this: (DQR) needs to specify, in some manner or other, the domain of expressions over which it quantifies. How can it do this without unreasonably limiting the kinds of symbols that can be quoted?[^note-11] (See Lepore (1999) for elaboration on this point.)

Second, according to (BQ6), a theory of quotation should leave room for dual use and mention. It is hard to see how (DQR) leaves such room. If quotes are referring expressions (as they are according to DQR), then if we let ‘Ted’ name the expression ‘has a certain anomalous feature’, (12) should say the same as, express the same proposition as, (17).

**(12)**

Quine said that quotation ‘has a certain anomalous feature’.

**(17)**

Quine said that quotation Ted.

Not only should (12) and (17) express the same proposition, according to DQR, they should also have the same logical form. That’s an obviously incorrect account of (12). (For further discussion of mixed quotation see Section 4 below.)

Finally, those who raise Objection 4 against the Demonstrative Theory would probably raise the same objection here: the Disquotational Theory fails to account for quotation without quotation marks. All the work is being done by quotation marks, so there’s no room for quotation without quotation marks. (DQR) proponents would presumably be as unimpressed as Demonstrative Theorists and their replies would be much the same (see above).

### 3.5 The Identity Theory of Quotation (or, better: the Use-Theory of Quotation)

The label ‘the Identity Theory of Quotation’ was first used, as far as we know, by Washington (1992), though he attributes the view to Frege (1892) and Searle (1969). However, the passages in which this view was allegedly offered prior to Washington hardly count as presenting a theory; they read more like dogmatic pronouncements devoid of argumentation. Since Washington’s paper was published related views have been developed in more detail by Saka (1998, 2004, 2011a), Reimer (1996), Recanati (2000, 2001) and others.

Washington’s presentation of the Identity Theory is somewhat compressed—the key passage is this:

> The quotation as a whole is analyzed into the marks that signify quotational use of the quoted expression and the quoted expression itself used to mention an object. All expressions, even those whose standard uses are not as mentioning expressions, become mentioning expressions in quotation…a quoted expression is related to its value by identity: a quoted expression mentions itself. (Washington 1992, p. 557)[^washington-1992]

There are three important components of this view:[^note-12]^{,} [^note-13]

- The use of quotation marks (as in (4)) is a *derivative* phenomenon. The basic phenomenon is what Washington calls *quotational use* (Washington 1992, p. 557)[^washington-1992].
- The primary function of quotation marks is to indicate that words are used quotationally (or mentioned) and not (merely) used with their regular extensions.
- Quotation marks do *not* refer according to Washington; that which is doing the referring in the quotation is the expression itself, so in (2), for example, it is ‘Aristotle’, not “Aristotle” that refers to ‘Aristotle’, i.e., ‘Aristotle’ refers to itself. It refers to itself because it is being used quotationally (not with its regular extension.)

One way to get a handle on this kind of view is to consider a spoken utterance of (6)

**(6)**

My name is Donald.

According to the Use/Identity theory, (6), when spoken, is grammatical (Washington 1992, pp. 588–90)[^washington-1992]. There are no missing (or implicit) quotation marks. When uttered by a person whose name is ‘Donald’ it is true (if ‘Donald’ is used quotationally). The function of quotation marks in written language is simply to indicate that words are being used in this special, quotational, way, i.e. not (only) with their regular extensions. In other words, ‘Donald’ can be used in two different ways: with its usual semantic value (its regular referent) or quotationally. In the latter case, its semantic value is an expression.

We wish that the Identity Theory were not called ‘the Identity Theory’. (In private communication, Washington has expressed the same sentiment.) The ‘identity’ component is picked up from the formulation, ‘a quoted expression is related to its value by identity: a quoted expression mentions itself’. This formulation, however, is deeply misleading, since according to both Washington (and later, for example, Saka (1998)), quotations are ambiguous. They can, according to Washington, refer to types, tokens, or shapes (see Washington 1992, p. 594)[^washington-1992] and according to another proponent of this kind of view, Saka, they are even more flexible (Saka 1998, see further presentation of Saka’s view below)[^saka-1998]. A better label would be ‘the Use-Theory of Quotation’, since this emphasizes the point that a proper understanding of quotation requires appealing to a special way of using language. In what follows, we use the ungainly compromise ‘the Use/Identity Theory’.

It is useful to contrast Washington’s account with the Disquotational Theory. Recall, that, according to DQR*, quotation marks* have a semantic function and that function is spelled out in the disquotational schema (DQR). (DQR) is a semantic axiom. It treats quotation marks as identity functions. Speakers’ intentions figure not at all in this axiom (other than the intention to speak English). There is no need, on the Disquotational Theory, to appeal to a special kind of quotational usage. For Washington, the quotation marks have no genuine semantic function. They are no more than a heuristic device for indicating that expressions are used in a special way, i.e. quotationally.

#### 3.5.1 Other Versions of the Use/Identity Theory: Reimer, Recanati, Saka, and the Picture Theory

Several recent views share important components of Washington’s. Reimer (2003) combines versions of the Demonstrative Theory and the Identity Theory. Recanati (2000, 2001, 2010) doesn’t explicitly discuss any version of the Identity Theory, but his theory incorporates some of its components; it is distinctive by focusing on what he calls ‘Open Quotation’ (see Objection 5 to the Demonstrative Theory above) and the *iconic* aspects of quotation (see Recanati 2001 for elaboration)[^recanati-2001]. Two theories might be worth a closer look for those interested in exploring Use/Identity Theories further (the second of these is mostly of historical interest).

First, Saka (1998, 1999, 2003) has developed a theory that has much in common with Washington’s (though it also differs in important respects). He agrees with Washington in emphasizing ‘quotational use’ (Saka calls it ‘mentioning’), but Saka has more to say about mentioning than Washington has to say about quotational use (see Saka 1998 and 2003)[^saka-1998][^saka-2003]. Saka also goes further than Washington in claiming that quotation marks are not required for mentioning even in written language. (For Washington, it is only in spoken language that we can quote without quotation marks). According to Saka, (34) ‘is a grammatical and true sentence’ (Saka 1998, p.118.)[^saka-1998]

**(34)**

Cats is a noun.

Even though Saka agrees with Washington that quotation marks ‘announce ‘I am not (merely) using expression X; I am also mentioning it’’ (Saka 1998, p. 127)[^saka-1998], he differs from Washington in that he assigns them a genuine syntactic and semantic function (Saka, 1998, p. 128). In this respect he incorporates components of what we above called the Disquotational Theory.[^note-14]^{,} [^note-15]

Saka’s account also differs from Washington’s in that he emphasizes that quotations are ambiguous (or indeterminate) and that what they refer to depends on the speaker’s intentions (see Saka 1998, pp. 123–4)[^saka-1998]. For further discussion of this point, see Section 5 below.

Second, there is one view we have not discussed and which might (admittedly with some difficulty) be squeezed into the category of the Use/Identity Theory. Quine said a number of things about quotation; in one passage he writes:

> …a quotation is not a description but a hieroglyph; it designates its object not by describing it in terms of other objects, but by picturing it. (Quine 1940, p. 26)[^quine-1940]

Davidson (1979), taking his cue from this passage and others, baptized the view intimated in Quine’s passage as ‘the Picture Theory of Quotation’ (cf., also, Christensen 1967, p. 362)[^christensen-1967]. As Davidson notes, on this view:

> …it is not the entire quotation, that is, expression named plus quotation marks, that refers to the expression, but rather the expression itself. The role of the quotation marks is to indicate how we are to take the expression within: the quotation marks constitute a linguistic environment within which expressions do something special… (Davidson 1979, pp. 83–84)[^davidson-1979]

Notice that according to Davidson’s description of this view, the quotation marks *per se* have no semantic function; rather, they indicate that the words are being used in a special way. They are being used ‘autonymously’, that is, to name themselves. So understood, the Picture Theory has at least this much in common with a Use/Identity Theory: they agree that quotation marks are inessential; they only indicate a special use. They indicate that expressions are being used as a picture (or as a hieroglyph). The Picture Theory—if it’s even appropriate to call it a theory—is never elaborated in any great detail and we suspect that if it were, it would become obvious that it is a version of the Use/Identity Theory.

#### 3.5.2 Strengths of the Use/Identity Theory

Use/Identity Theorists claim that their theories are explanatorily more powerful than traditional semantic theories. By seeing quotation marks as a parasitic phenomenon, they are able to explain the semantics of both quotation and this more general phenomenon in a unified way.

There’s a great deal of specific data that these theories claim to be able to explain. The most important of these is the possibility of mentioning without quotation marks (as in spoken language and in written language when no quotation marks are used). If we take appearances at face value, that means meta-linguistic discourse (call it mentioning or quotational use) can take place in the absence of quotation marks. Hence, an account of meta-linguistic discourse must proceed independently of an account of the semantics (or pragmatics) for quotation marks.

The following are additional claims made on behalf of the Use/Identity Theory (we take it to be an open question at this point whether these points are sustainable):

- Whatever can be mentioned can be quoted. If new symbols and signs can be mentioned, then they can also be quoted; hence, (BQ3) is satisfied.
- There is, on this view, often a particularly close relationship between the quoted material and the referent; sometimes it is identity, sometimes it is instantiation, etc, so in various ways we might say that (BQ4) is satisfied.
- If our capacity for mentioning is limitless, then we have an account of how quotation can be too (i.e., we have at least the beginning of an account of (BQ1)).

#### 3.5.3 Weaknesses of the Use/Identity Theory

Discussion of the Use/Identity Theories is not yet as extensive as discussion of the Demonstrative Theory, so there are fewer objections to report. We discuss four concerns that have surfaced in various discussions.

*Question about the Relevance of Quotational Use/Mention:* Use/Identity Theories put a great deal of weight on the idea that the semantics for quotation cannot be developed without an account of *quotational usage* (*mention* in Saka’s terminology.) There are several reasons for doubting this, two of which are these:

- It is not obvious that the alleged phenomenon of mention without quotation marks is genuine. It might very well be, as mentioned in connection with Objection 3 to the Demonstrative Theory, that it is not possible to mention without using quotation marks. The cases appealed to might all turn out to be cases in which a conversational or conventional implicature is generated and where that implicature contains quotation marks. Alternatively, the quotation marks might actually be in the logical form of the sentence through some form of ellipsis. (See Garcia-Carpintero 1994 and Cappelen and Lepore 1999)[^garcia-carpintero-1994][^lepore-1999].
- Even if we suppose that the phenomenon of mentioning without quotation marks is genuine, it is not clear why we should consider it relevant to the semantics for quotation. Suppose that you’re in the business of trying to develop a semantic theory of sentences with quotation marks. Suppose it also turns out that it is possible to talk about language by mentioning without the use of quotation marks. This might just be a different way of talking about language. An interesting phenomenon, no doubt, but not one that needs to have anything to do with the semantics for sentences containing quotation marks. It does not follow from there being a variety of ways in which language can be used to talk about language, that all of these ways are relevant to the semantics of quotation.

*Question about the Semantics-Pragmatics Divide*: On the Use/Identity Theory, a lot of work is done by pragmatic mechanisms. The appeal to speaker intentions plays a central role on all levels of analysis. On Saka’s view, for example, what a quoted expression refers to is largely up to the speaker’s intentions (and, maybe, what’s salient in the context of utterance). A consequence of this view is that there is no guarantee, for example, that an utterance of (35) or (36) will be true:

**(35)**

‘$a$’ = ‘$a$’

**(36)**

‘run’ is a verb in English

The two ‘$a$’s in (35) could refer to different objects; the “run” in (36) might refer to, for example, a concept (see Cappelen and Lepore 1999b and Saka 1999, 2003, 2011)[^cappelen-1999b][^lepore-1999][^saka-1999].

*Over-generation Problems*: According to Use/Identity Theories, you can do a lot with quotation. The question is whether this results in such theories running into problems of over-generation. Take, for example, Saka’s claim that a quotation refers to an item *associated* with the expression. There’s only one restriction: This item cannot be the expression’s regular extension. If this is the *sole* restriction on what quotations can be used to refer to, we should be able to do things with quotation that there’s no evidence that we can. It could, for example, be the case that in a particular context, the (regular) extension of ‘love’, call it *love*, was associated with the expression ‘money’; maybe, for some reason, that association was contextually salient. Nonetheless, (37) cannot be used to say that *love* plays a central role in many peoples’ lives.

**(37)**

‘Money’ plays a central role in many peoples’ lives.

Use/Identity Theories have to explain what blocks such readings (or show that they are possible). (See Saka 2003, and Cappelen and Lepore 2003.)[^cappelen-2003][^saka-2003]

*Dual Use-Mention (BQ6):* Washington says that quotation marks indicate quotational usage and that expressions used quotationally refer to themselves (or some related entity). If so, the logical form of (12) should be that of (17), clearly not a correct result.

**(12)**

Quine said that quotation ‘has a certain anomalous feature’.

**(17)**

Quine said that quotation Ted.[^note-16]

It is at least a challenge to Identity/Use theorists to explain how the theory can accommodate simultaneous use and mention.

In addition to the above points, there’s a lively debate about the specifics of identity/use theories. For discussions of Saka, see Cappelen and Lepore (2003), Reimer (2003), and for discussions of Recanati, see Cappelen and Lepore (2003), Reimer (2003), Benbaji (2003, 2004a, 2004b), and Cumming (2003).

We now turn from discussions of large-scale theories of quotation to discussions of how to understand specific aspects of our quotational practice. Two issues have been particularly important in the recent discussions: Mixed Quotation and the alleged ambiguity of quotations. One’s view of these issues has wide reaching implications for which theory of quotation one favors. We discuss these in turn.

## 4. Mixed Quotation

From around the millennium, beginning with Cappelen and Lepore’s 1997a, which made the topic mainstream, mixed quotation has been, arguably, the area in which theorizing about quotation has advanced the most. The problem has attracted the attention of both philosophers and linguists, and our understanding of both the data to be accounted for, and the various possibilities for doing so, has been greatly improved.

It’s important to reiterate our above note that here as elsewhere in the theory of quotation what comprises the phenomenon is up for debate; different theorists emphasise or play down different bits of data. What follows, accordingly, doesn’t represent a consensus position on the problem, simply because there isn’t one (indeed, somewhat unfortunately, there isn’t even consensus about the terminology, some calling it ‘hybrid’ or ‘impure’, and some subsuming mixed quotation under ‘scare quoting’; De Brabanter 2010 is helpful here, as well as being a useful survey of the field from a linguist’s point of view). We will simply present some of the more interesting and central data points and problems for a theory of mixed quotation (for the theories themselves, we refer the reader to Maier’s (2020) overview article which presents some of the main formal semantic theories out there. For recent theories by philosophers on mixed quotation, see Gomez-Torrente 2005, Kirk and Ludwig 2017, McCullagh 2007, 2017. The main linguists to consult are cited in this section.)

The paradigm example of mixed quotation is the following, repeated:

**(12)**

Quine said that quotation ‘has a certain anomalous feature’.

It is mostly agreed that this sentence puts forward the following claim: Quine said (expressed the proposition or content) that quotation has an anomalous feature, and did so by uttering the expression ‘has an anomalous feature’. This suggests two initial requirements:

- An adequate theory of mixed quotation must account for the fact that the quoted material is used by the reporter to characterise the proposition that the reportee expressed.
- It must also account for the fact that the quoted material was uttered by the reportee.

Let’s call these the **use requirement** and the **mention requirement**, respectively.

While these both seem clearly on the right lines (if you doubt this, open or scroll to a newspaper and read until you find the first mixed quotation (it shouldn’t take long) and see if the requirements are operative) there are problems with both of them. It might initially seem that the mention requirement requires that the reportee have uttered verbatim the words ascribed to him or her. That would account for the anomalousness of:

**(38)**

# Quine said quotation ‘has a certain anomalous feature’, although he didn’t use the words ‘has a certain anomalous feature’.

Things aren’t so clear, though. Certain other pieces of data are in tension with this purported feature of the mention requirement, most notably that one can mixed quote someone correctly in a language other than the one they spoke (Cappelen and Lepore 2007 p. 44)[^cappelen-2007]. Thus the following, as well as its parenthesised continuation, is fine:

**(39)**

Kant said that concepts without intuition ‘are empty’, (although he didn’t use those words: he said ‘sind leer’).

Moreover, more subtle problems for the use requirement come from inflected languages (Shan 2010, Maier 2014a)[^maier-2014a]. Thus in Italian, nouns must agree in gender and number with adjectives. Imagine Ken says:

**(40)**

Gli uomini italiani mi sembrano molto carini.

This means ‘I find Italian men very cute’, and since the noun ‘uomini’ (men) is m.pl, so is the adjective ‘carini’ (cute). But if one wanted to mixed quote Ken, using a different word than ‘uomini’, that different word would have to agree:

**(41)**

Ken ha detto che le persone italiane ‘mi sembrano molto carine’

So the mixed quoted material used to report Ken’s utterance is not what he said verbatim: he said ‘carini’ and he is reported as saying ‘carine’ (the example is from Shan 2010). Maier presents similar cases for Dutch. Yet a third problem comes from the fact that one can ‘clean up’ quotations, by removing grammatical slurs, umms and ahhs, and so on (see Cappelen and Lepore 2007 p. 45)[^cappelen-2007].

What exactly the mention requirement requires is uncertain, then. But nor, however, is the use requirement without its problems. There are at least two, which again differ in subtlety. From the beginning, it’s been realised that indexicals in mixed quotations cause intriguing problems. Consider:

**(42)**

Mr. Greenspan said he agreed with Labor Secretary R. B. Reich ‘on quite a lot of things’. Their accord on this issue, he said, has proved ‘quite a surprise to both of us’. (Cappelen and Lepore 1997b, p. 429)[^cappelen-1997b]

If the second mixed quotation were simply being used, then the second sentence should be true provided accord was a surprise to the people writing the report, not to Greenspan and Reich. That’s clearly the wrong result, and shows that the use requirement needs some modifiction (for discussion about indexicals in mixed quotation, and whether they call for Kaplanian monstrous operators, see also Recanati (2001), Cumming (2003), Geurts and Maier (2003), and Maier (2016)).

The behaviour of indexicals in mixed quotation is important, because it gives strong evidence against the possibility that mixed quotation is a pragmatic phenomenon. A typical pragmatic analysis would say that the semantic contribution of the quoted material in a mixed quotation is just its unquoted semantic value (so that the literal semantic content of (12) is simply ‘Quine said that quotation has a certain anomalous feature’), but that to utter a mixed quotation is to imply, but not to say, that the quoted material was used by the speaker to say what they said.

The advantages of a pragmatic analysis of mixed quotation are those typical of pragmatic analyses in general: no extra semantic machinery is required to account for the problem cases. As such, versions of such an analysis have had many adherents at the end of the twentieth century (see, for example, Recanati (2001), Clark & Gerrig (1990), Wilson (2000), Sperber & Wilson (1981), Tsohatzidis (1998), Staintion (1999), Saka (2003) and the discussion in by Reimer (2003)).

However, the behaviour of indexicals in mixed quotation make the pragmatic analysis harder to uphold. One needs to say that (42) is literally false, and while that is a move that can be made, it’s not particularly attractive. Accordingly, the pragmatic analysis has gone somewhat out of fashion, and has been argued against explicitly explicitly by Gomez-Torrente (2017), and implicitly by most of the linguists working in the field, for whom the behaviour of indexicals is a key explanandum of a theory of mixed quotation, and not something to be explained *away* (although see De Brabanter 2019 for a pragmatic theory of indexicals in mixed quotation).

The second, more subtle, problem is a consequence of the fact that one can mixed quote an expression belonging to a dialect other than the one one speaks, or even to no dialect at all (Shan 2010). Thus even in informal British English, ‘accident’ always takes the preposition ‘by’ and never ‘on’. A British speaker can draw attention to this fact, by uttering, about an American friend of theirs:

**(43)**

Meagan said she took out the trash ‘on accident’.

But a British speaker can’t felicitiously use ‘on accident’ because that’s not a part of British English speakers’ dialect. Similarly, ‘misunderestimated’ isn’t a word in most anybody’s dialects, but we can say:

**(44)**

Bush said that his opponents ‘misunderestimated’ him.

A different, more fundamental, source of complication arises from the fact that it’s unclear exactly how much to include under mixed quotation. Thus consider:

**(45)**

Quine wrote a couple of papers on quotation, the ‘anomalous feature’ of which he thought about a lot.

**(46)**

A: *The Godfather II* is a total snooze. B: Well, Pauline Kael said this ‘total snooze’ is a defining moment in American cinema. (Potts 2007, p 420)[^potts-2007]

Should we include such phenomena in our theory of mixed quotation? The first sentence doesn’t contain a speech verb, while the second does, but the person to whom the mixed quotation is attributed isn’t the person who uttered the mixed quoted words. It’s unclear. Things get even more uncertain when we consider scare quotes (Predelli 2003a,b, Saka 2013, Gomez-Torrente 2017)[^gomez-torrente-2017][^saka-2013] and what are known euphemistically as grocers’ quotes:

**(47)**

Teens are spending more and more time ‘sexting’, something of concern to parents and even technology companies.

**(48)**

[written on a desiccate in a new pair of shoes] Do not ‘eat’!

In the former case, there isn’t any one person who used ‘sexting’; rather, the writer is marking that it’s used in a community which they are not part of or disapprove of. In the latter case, the quotation marks are serving as emphasis. While we probably don’t want to spend a lot of time seriously theorizing about grocers’ quotes (although see Abbott 2003)[^abbott-2003], whether or not scare quotes should be treated as we treat mixed quotation (indeed, whether or not they’re one and the same) is an open question (see McCullagh 2017 for discussion and an affirmative answer to these questions; Gomez-Torrente 2017 demurs)[^gomez-torrente-2017][^mccullagh-2017].

This isn’t even an exhaustive characterization. Thus it’s important to attend to cognate phenomena like dequotation (Shan 2010) and free indirect discourse (Maier 2015, 2017)[^maier-2015]. And the theorist of mixed quotation should at least be aware of the problem of mixed quoting non-constituent clauses (Abbott 2003, De Brabanter 2022)[^abbott-2003], and the possibility that one can mixed quote without quotation marks (De Brabanter 2010). The complexity of the data has inspired much interesting theorizing, and we expect that mixed quotation will continue to be a focal question in the theory of quotation.

## 5. What Kinds of Entities do Quotations Refer to?

Running parallel to the debate about *how* quotations refer (how they manage to hook up with their semantic values) is a debate about *what* quotations refer to. One view that is widespread is that quotations are ambiguous or indeterminate. That is, one and the same quotation, e.g. “lobster” can, on this view, refer to different objects on different occasions of use, all depending on the context of utterance. Garcia-Carpintero (1994, p. 261) illustrates this kind of view and the kind of argument typically given for it. He says that “gone” can refer to any of the following:

- The expression (‘ ‘gone’ is dissyllabic’);
- Different types instantiated by the tokens (‘ ‘*gone*’ is cursive’);
- Different types somehow related to the token (say, the graphic version of the uttered quoted material, or the spoken version of the inscribed quoted material, as in ‘ ‘gone’ sounds nice’);
- Different tokens somehow related to the quoted token (‘What was the part of the title of the movie which, by falling down, caused the killing?—‘gone’ was’);
- The quoted token itself (‘At least one of these words is heavier than ‘gone’ which you should imagine written in big wooden letters’);

Others think quotation can pick out contents or concepts. Goldstein says:

> For when Elvis says ‘Baby, don’t say ‘don’t’,’ he is not just requiring his baby to refrain, when confronted with a certain request, from uttering tokens of the same phonetic shape as ‘don’t’, but from uttering any tokens that *mean* the same. (Goldstein 1984, p. 4)[^goldstein-1984]

Saka (1998, p. 124) concurs and claims that “premise” and “premiss” in (38) pick out concepts:

**(38)**

The concept ‘premise’ is the same as the concept ‘premiss’.

Tsohatzidis (1998) claims that since T1 is true, even though Descartes didn’t speak English, “is a thinking substance” in T1 can’t refer to an English expression.

(T1) In one of the greatest philosophy books ever written in Latin, Descartes said that man ‘is a thinking substance’.

These arguments all take the same form: first, they identify a sentence $S$ that we are inclined to interpret as true and suggest that the only way to understand how $S$ can be true is to assume that quotations can refer to some kind of object $O$. This is then alleged to be evidence that quotations can be used to refer to objects of kind $O$.

If quotation has this kind of flexibility, the five theories discussed above will all have to be evaluated with respect to whether they can accommodate it. The Proper Name Theory, Description theory, and Disquotational Theory, all seem to have particular difficulties in this respect.

Not all, however, are convinced that quotations are flexible in just this way. Some have expressed skepticism both about the form of argument (see Cappelen and Lepore 1999a)[^cappelen-1999a] and about the specific examples. Cappelen and Lepore (1999a) also argue that the multiple ambiguity view over-generates, i.e., it predicts that it is possible to express propositions with quotation sentences that it is not possible to express with such sentences. For further discussion, see also Saka (2003).

## 6. Alternative Quotational Devices

A number of authors over the years have thought that our standard practices of quotation are not suitable for all purposes and have, in effect, introduced new technical devices. They cannot all be summarized here, but here is a brief sketch of some such devices.

### 6.1 Token Quotes

Reichenbach (1947, p. 284) writes: ‘Whereas the ordinary-quotes operation leads from a word to the name of that word, the token-quotes operation leads from a token to a token denoted by that token’. Reichenbach uses little arrows ($\tokenquote{\,}$) for token quotes, so that the sign (39):

**(39)**

$\tokenquote{a}$

represents not a name for the token of ‘a’, but a token for it. That is, the token in (39) cannot be repeated. (40), for example, is not only a token different from (39) but refers to a different token (Reichenbach 1947, pp. 285–86)[^reichenbach-1947].

**(40)**

$\tokenquote{a}$

Token quotes then are much like writing a demonstrative expression like ‘this’ and fastening to it an object to produce a symbol of that object. (As noted above, some authors (Bennett 1988, Saka 1998, Washington 1992)[^bennett-1988][^saka-1998][^washington-1992] opine that this is how ordinary quotation sometimes functions.)

### 6.2 Corner (Quasi) Quotation

As Quine (1940, §6) notes, the quotation:

> ‘$(\mu)$’

designates only the specific expression therein depicted, containing a specific Greek letter. In order to effect reference to the unspecified expression he introduces a new notation of *corners* (namely, ‘$\ulcorner$’ and ‘$\urcorner$’). So, for example, if we take the expression ‘Quine’ as $\mu$, then $\ulcorner(\mu)\urcorner$ is ‘(Quine)’. The quasi-quotation is synonymous with the following verbal description: The result of writing ‘(’ and then $\mu$ and ‘)’ (Quine 1940, p. 36)[^quine-1940]. For an interesting suggestion about quasi-quotation in natural language, see Saka (2017).

### 6.3 Dot Quotes

Someone who uses the word ‘red’ in speaking or thinking would generally be held to be employing the same concept as a French person who uses ‘rouge’. Assuming that ‘rouge’ is a good translation of ‘red’, Sellars (1963) thought it convenient to have a general term by which to classify words that are functional counterparts in this way. Such a term is provided by Sellars’ dot quotes. Dot-quotes form a common noun true of items in any language that play the role performed in our language by the tokens exhibited between them, so any expression that is a functional counterpart to ‘red’ can be described as a _{·}red_{·}. In Sellars’ terminology, the concept *red* is something that is common and peculiar to _{·}red_{·}s.

### 6.4 Unambiguous Quotes

Consider (41):

**(41)**

‘a’ concatenated with ‘b’ is an expression.

Michael Ernst claims this sentence is ambiguous. Read one way, (41) means that the concatenation of the first letter of the Roman alphabet with the second letter is an expression; read another way it means that the expression between the two outer quote marks is an expression. Confronted with this ambiguity, Boolos (1995) introduced a notation for quotation in which every quotation mark ‘knows its mate’. So understood there are denumerably many distinct quotation marks, each formed by prefixing a natural number n of strokes to a small circle, and in order to meaningfully enclose an expression with Boolos quotation marks we have to choose quotation marks of a ‘higher order’ than the quotation marks that occur in the expression to be quoted (if there are any) and each quotation mark in a grammatical sentence is to be ‘paired’ with the next identical quotation mark (Boolos 1995, p. 291)[^boolos-1995]. Accordingly, reading (41) as containing Boolos quotation marks, we get the more natural reading according to which it says that the first letter of the Roman alphabet concatenated with the second is an expression.

## 7. Formal-Material Modes

Carnap introduced in *Logical Syntax of Language* (1937) a distinction between formal and material modes. The material mode is generally used to describe the non-linguistic world; the formal mode is generally used to discuss the language that is used to describe the material world. Thus ‘one is a number’ is a sentence in material mode; and ‘‘one’ is a number word’ is its sentential counterpart in formal mode. This distinction is mentioned in passing here since some authors have thought it corresponds to the use/mention distinction. Since the use/mention distinction isn’t particularly about quotation, there isn’t much that needs to be said about the material/formal mode here either. Revealing that a statement is basically about the use of language may succeed in removing some of its metaphysical mystery. And it may even be that semantic ascent (that is, the device of making a sentence the topic, instead of what the sentence purports to refer to) succeeds in demystifying much of what goes on in certain quarters of philosophy. But as we’ve said, this distinction, and the various philosophical moves surrounding it, doesn’t have much to do with quotation per se.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=quotation). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/quotation/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=quotation&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/quotation/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

[Please contact the author with suggestions.]

## Related Entries

Davidson, Donald | descriptions | Quine, Willard Van Orman | reference | Tarski, Alfred

### Acknowledgments

The authors would like to thank Poppy Mankowitz and a reviewer for suggesting several helpful changes, Mike Cohen for pointing out a typo, and two anonymous readers (in 2018 and 2023) for pointing out an unclarity in our discussion of the Proper Name Theory. The editors would like to thank Milan Emil Mosse for noting and reporting a number of typographical errors that have subsequently been corrected.

## Notes（原文脚注）

[^note-1]: To follow this text, pay close attention to the difference between single quotes and double quotes. Double quotes are used to quote quotations. Triple quotes to quote quotations of quotations. Etc.

[^note-2]: See Munro (1982) for a challenge to the claim that the ‘says’ of direct reporting is transitive.

[^note-3]: Partee (1971, p. 411) also discusses the phenomenon but does not go on to theorize about it since, according to her, ‘such sentences do not occur in ordinary spoken language’. We disagree. Were you to hear someone utter:

> John said with a heavy Jersey accent that he ‘ain’t gonna take it anymore’

you would almost certainly take some of the material after ‘he’ as mixed quoted.

[^note-4]: At least one author (Gomez-Torrente 2001)[^gomez-torrente-2001], however, thinks that Q3 is ‘less important than the other two’ questions. He believes that distinct answers to Q1 and Q2 ‘can be supplemented with any of a series of different answers to’ Q3.

[^note-5]: Note that this characterization of (D2) should be read as neutral over whether it is ‘Jim’ or the quoted expression, ‘’Jim’’ that is used to talk about ‘Jim’. An initial characterization of the use-mention distinction should remain neutral on that question.

[^note-6]: For Quine and Tarski, the Description Theory was largely presented as an alternative to natural language quotation, and not as an analysis of natural language; this was not so for Geach.

[^note-7]: Similar views are intimated in Prior (1971, pp. 60-61) and Christensen (1967); Partee (1973, pp. 416-18) was also an early adherent. An interesting historical factoid: Davidson’s paper was drafted in the early 1960s and circulated among various philosophers and linguists. It is, for example, referenced in Partee 1973, some six years before its publication date.

[^note-8]: There is a separate issue about how best to treat the semantics of indirect discourse. Davidson, of course, has a demonstrative view about that as well (cf., Davidson 1968)[^davidson-1968].

[^note-9]: For a defense of Davidson’s theory of indirect discourse against its opponents, cf., Lepore and Loewer (1989).

[^note-10]: For further criticisms surrounding the use of a demonstrative in the logical form of a quotation sentence, see Seymour (1994, pp. 16ff).

[^note-11]: One possibility is to quantify over literally *everything*, or at least everything that can be put between quotation marks.

[^note-12]: According to Washington, Searle endorses the same view when he writes that in quotation ‘a word is uttered…but not in its normal use. The word itself is presented and then talked about, and that it is to be taken as presented rather than used conventionally to refer is indicated by the quotes’ (Searle 1969, p. 76)[^searle-1969]. (Gomez (2001) challenges Washington’s claim that Searle is an Identity Theorist.)

[^note-13]: Washington tries also to locate a commitment to the Identity Theory in this passage from Frege: ‘If words are used in the ordinary way, what one intends to speak of is what they mean. It can also happen, however, that one wishes to talk about the words themselves or their sense. This happens, for instance, when the words of another are quoted. One’s own words then first designate words of the other speaker, and only the latter have their usual meaning. We then have signs of signs. In writing, the words are in this case enclosed in quotation marks. Accordingly, a word standing between quotation marks must not be taken as having its ordinary meaning’ Frege (1892, p. 58). We find this passage insufficiently clear to establish what Frege’s view on quotation is. For an alternative interpretation of Frege on quotation, see Parsons (1982).

[^note-14]: Saka summarizes the relationship between quotation and mention as follows:

> As a consequence of my account, the mention of *X* and the use of ‘*X*’ quite properly secure the same reference. Further, whereas the use-mention distinction is characterized in terms of the speaker’s intentions, the distinction between a quotation and a non-quotation is a formal, grammatical affair. Distinguishing between use and mention in a language without quote marks is a purely pragmatic affair, but in a language with quote marks mentioning can be explicitly marked (although such marking is not obligatory). Saka (1998, p.128)

[^note-15]: A particularly interesting and illuminating consequence of this view is that quotations can be both used and mentioned. See Saka (1998, p. 128) for further discussion.

[^note-16]: Or (given that several words are quoted) the more complex: Quine said that quotation Ted Sally Bill Jane Peter.

[^abbott-2003]: Abbott, Barbara, 2003. ‘Some Notes on Quotation’, *Belgian Journal of Linguistics*, 17(1): 13–26.

[^bazzoni-2016]: Bazzoni, André, 2016. ‘Pure quotation, metalanguage and metasemantics’, *Linguistics and Philosophy*, 39(2): 119–149.

[^benbaji-2003]: Benbaji, Yitzhak, 2003. ‘Who needs semantics of quotation marks?’ *Belgian Journal of Linguistics*, 17: 27–49.

[^benbaji-2004a]: –––, 2004a. ‘A demonstrative analysis of “open quotation”‘. *Mind and Language*, 19: 534–547.

[^benbaji-2004b]: –––, 2004b. ‘Using others’ words’, *Journal of Philosophical Research*, 29: 93–112.

[^bennett-1988]: Bennett, Jonathan, 1988. ‘Quotation’, *Noûs*, 22: 399–418.

[^boolos-1995]: Boolos, George, 1995. ‘Quotational ambiguity’, in *On Quine*, P. Leonardi and M. Santambrogio (eds.), Cambridge: Cambridge University Press, pp. 283–296.

[^botterell-2005]: Botterell, Andrew and Stainton, Robert, 2005. ‘Quotation: Compositionality and Innocence without Demonstration’, *Critica: Revista Hispanoamericana de Filosofia*, 37(110): 3–33.

[^burge-1986]: Burge, Tyler, 1986. ‘On Davidson’s ‘Saying that’’, in *Truth and Interpretation*, Basil E. Lepore (ed.), Oxford: Blackwell, pp. 190–208.

[^cappelen-1997]: Cappelen, Herman, 1997. *Signs*, Doctoral Dissertation, Philosophy Department, University of California-Berkeley.

[^cappelen-1997a]: Cappelen, Herman and Ernest Lepore, 1997a. ‘On an alleged connection between semantic theory and indirect quotation’, *Mind and Language*, 12: 278–296.

[^cappelen-1997b]: –––, 1997b. ‘Varieties of quotation’, *Mind*, 106: 429–50.

[^cappelen-1998]: –––, 1998. ‘Using, mentioning, and quoting: reply to Tsohatzidis’, *Mind*, 107: 665–666.

[^cappelen-1999a]: –––, 1999a. ‘Reply to Saka’, *Mind*, 108: 741–50.

[^cappelen-1999b]: –––, 1999b. ‘Reply to Stainton’, in Kumiko and Robert, pp. 279–283.

[^cappelen-1999c]: –––, 1999c. ‘Reply to Pietroski’, in Kumiko and Robert, pp. 283–285.

[^cappelen-1999d]: –––, 1999d. ‘Semantics of quotation’, in Zeglen, pp. 90–99.

[^cappelen-2003]: –––, 2003. ‘Varieties of quotation revisited’, *Belgian Journal of Linguistics*, 17: 51–75.

[^cappelen-2004]: –––, 2004. *Insensitive Semantics*, Oxford: Basil Blackwell Publishers.

[^cappelen-2007]: –––, 2007. *Language Turned On Itself*, Oxford: Oxford University Press.

[^carnap-1937]: Carnap, Rudolf, 1937. *Logical Syntax of Language*, London: Routledge and Kegan Paul.

[^carnap-1947]: –––, 1947. *Meaning and Necessity*, Chicago: University of Chicago Press.

[^christensen-1967]: Christensen, Niels, 1967. ‘The alleged distinction between use and mention’, *Philosophical Review*, 76: 358–67.

[^clark-1990]: Clark, Herbert & Richard Gerrig, 1990. ‘Quotations as demonstrations’, *Language*, 66(4): 764–805.

[^cumming-2003]: Cumming, Sam, 2003. ‘Two accounts of indexicals in mixed quotation’, *Belgian Journal of Linguistics*, 17: 77–88.

[^de-2010]: De Brabanter, Philippe, 2010. ‘The semantics and pragmatics of hybrid quotations’, *Language and Linguistics Compass*, 4(2): 107–120.

[^de-2019]: –––, 2019. ‘The Interpretation of Indexicals in Hybrid Quotation: A Pragmatic Account’, *Anglophonia: French Journal Of English Linguistics*, 28. doi:10.4000/anglophonia.2646.

[^de-2022]: –––, 2022. ‘Accounting for non-constituents in hybrid quotations. Why unquotation is not the answer’, *Journal of Linguistics*, 59(1): 1–22. doi:10.1017/S0022226722000184.

[^elugardo-1999]: Elugardo, Reinaldo, 1999. ‘Mixed quotation’, in Murasugi & Stainton.

[^davidson-1968]: Davidson, Davidson, 1968. ‘On saying that’, in *Inquiries Into Truth and Interpretation*, Oxford: Oxford University Press, pp. 93–108.

[^davidson-1975]: –––, 1975. ‘Thought and talk’, in *Inquiries Into Truth and Interpretation*, Oxford: Oxford University Press, pp. 155–170.

[^davidson-1979]: –––, 1979. ‘Quotation’, in *Inquiries Into Truth and Interpretation*, Oxford: Oxford University Press, pp.79–92. Originally published in *Theory and Decision*, 11 (1979): 27–40.

[^davidson-1999]: –––, 1999. ‘Reply to Cappelen and Lepore’, in Zeglen, pp. 100–102.

[^frege-1892]: Frege, Gottlob, 1892. ‘On sense and reference’, in *Translations from the Philosophical Writings of Gottlob Frege*, P. Geach and M. Black (eds.), 3rd edition, Oxford: Basil Blackwell, 1980, pp. 56–78.

[^garcia-carpintero-1994]: Garcia-Carpintero, Manuel, 1994. ‘Ostensive signs: against the identity theory of quotation’, *Journal of Philosophy*, 91: 253–64.

[^garcia-carpintero-2004]: –––, 2004. ‘The deferred ostension theory of quotation’, *Noûs*, 38(4): 674–692.

[^garcia-carpintero-2012]: –––, 2012. ‘Minimalism on quotation? Critical Review of Cappelen and Lepore’s Language Turned On Itself’, *Philosophical Studies*, 161(2): 207–225.

[^garcia-carpintero-2017]: –––, 2017. ‘Reference and Reference-Fixing in Pure Quotation’, in Saka and Johnson (eds.) 2017, pp. 169–194.

[^garcia-carpintero-2018]: –––, 2018. ‘Pure Quotation Is Demonstrative Reference’, *Journal of Philosophy*, 115 (7): 361–381.

[^geach-1957]: Geach, Peter, 1957. *Mental Acts*, London: Routledge Kegan Paul.

[^geach-1970]: –––, 1970. ‘Quotation and quantification’, in *Logic Matters*, Oxford: Basil Blackwell.

[^geurts-2003]: Geurts, Bart and Emar Maier, 2003. ‘Quotation in context’, *Belgian Journal of Linguistics*, 17: 109–128.

[^goddard-1966]: Goddard, Leonard and Richard Routley, 1966. ‘Use, mention, and quotation’, *Australasian Journal of Philosophy*, 44: 1–49.

[^goldstein-1984]: Goldstein, Laurence, 1984. ‘Quotation of types and types of quotation’, *Analysis*, 44: 1–6.

[^gomez-torrente-2001]: Gomez-Torrente, Mario, 2001. ‘Quotation revisited’, *Philosophical Studies*, 102: 123–53.

[^gomez-torrente-2005]: –––, 2005. ‘Remarks on Impure Quotation’, in Philippe De Brabanter (ed.), *Hybrid Quotations* (*Belgian Journal of Linguistics* 2003 Yearbook, Volume 17), Amsterdam: John Benjamins, pp. 129–151.

[^gomez-torrente-2013]: –––, 2013. ‘How Quotations Refer’, *Journal of Philosophy*, 110(7): 353–390.

[^gomez-torrente-2017]: –––, 2017. ‘Semantics vs. Pragmatics in Impure Quotation’, in Saka and Johnson 2017, pp. 135–16.

[^johnson-2018]: Johnson, Michael, 2018. ‘Pure Quotation and Natural Naming’, *Journal of Philosophy*, 115(10): 550–566.

[^kaplan-1973]: Kaplan, David, 1973. ‘Bob, Ted, Carol and Alice’, in *Approaches to Natural language*, J. Hintikka, et al. (eds.), pp. 490–518.

[^kaplan-1989]: –––, 1989. ‘Demonstratives’, in *Themes from Kaplan*, J. Almog, J. Perry, and H. Wettstein (eds.), Oxford: Oxford University Press, pp. 481–564.

[^lepore-1999]: Lepore, Ernest, 1999. ‘The scope and limits of quotation.’ in *The Philosophy of Donald Davidson*, L. E. Hahn (ed.), Open Court Publishers, pp. 691–714.

[^lepore-1989]: Lepore, Ernest, and Barry Loewer, 1989. ‘You can say that again’, *Midwest Studies in Philosophy*, 14: 338–356.

[^ludwig-1998]: Ludwig, Kurt and Greg Ray, 1998. ‘Semantics for opaque contexts.’ *Philosophical Perspectives*, 12: 141–166.

[^ludwig-2017]: –––, 2017. ‘Unity in the Variety of Quotation’, in Saka and Johnson (eds.) 2017, pp.99–134.

[^maier-2014a]: Maier, Emar, 2014a. ‘Mixed quotation: the grammar of apparently transparent opacity’, *Semantics and Pragmatics*, 7(7): 1–67.

[^maier-2014b]: –––, 2014b. ‘Pure Quotation’, *Philosophy Compass*, 9(9): 615–630.

[^maier-2015]: –––, 2015. ‘Quotation and unquotation in free indirect discourse’, *Mind and Language*, 30(3): 345–373.

[^maier-2016]: –––, 2016. ‘A plea against monsters’, *Grazer Philosophische Studien*, 93: 363–395.

[^maier-2017]: –––, 2017. ‘The Pragmatics Of Attraction. Explaining Unquotation in Direct and Free Indirect Discourse’, in Saka and Johnson (eds.) 2017: 259–302.

[^maier-2020]: –––, 2020. ‘Mixed Quotation’, in *The Companion to Semantics*, Daniel Gutzmann, Lisa Matthewson, Cécile Meier, Hotze Rullman, and Ede Zimmerman (eds.), Wiley Blackwell.

[^mates-1972]: Mates, B., 1972. *Elementary Logic*, 2ⁿᵈ edition, Oxford: Oxford University Press.

[^mccullagh-2006]: McCullagh, Mark, 2006. ‘Understanding mixed quotation’, *Mind*, 116: 927–46.

[^mccullagh-2017]: –––, 2017. ‘Scare-quoting and incorporation’, in Saka and Johnson (eds.) 2017, pp.3–34.

[^miller-2019]: Miller, James, 2019. ‘Natural Name Theory and Linguistic Kinds’, *Journal of Philosophy*, 116(9): 494–508.

[^munro-1982]: Munro, Pamela, 1982. ‘On the transitivity of say-verbs’ in P. Hopper & S. Thompson (eds.), *Studies in Transitivity. Syntax and Semantics*, New York, San Francisco, London: Academic Press, pp. 301–318.

[^murasugi-1999]: Murasugi, Kumiko & Robert Stainton (eds.), 1999. *Philosophy and Linguistics*, Boulder CO: Westview.

[^pagin-2010]: Pagin, Peter & Westerståhl, Dag, 2010. ‘Pure quotation and general compositionality’, *Linguistics and Philosophy*, 33(5): 381–415.

[^parsons-1982]: Parsons, Terence, 1982. ‘What do quotation marks name? Frege’s theories of quotations and that-clauses’, *Philosophical Studies*, 42: 315–328.

[^partee-1973]: Partee, Barbara, 1973. ‘The syntax and semantics of quotation’, in *A Festschrift for Morris Halle*, S.R. Anderson and P. Kiparsky (eds.), New York: Holt, Reinehart and Winston, pp. 410–418.

[^pietroski-1999]: Pietroski, Paul, 1999. ‘Compositional quotation’, in Murasugi & Stainton, pp. 245–58.

[^potts-2007]: Potts, Christopher, 2007. ‘The Dimensions of Quotation’, in Chris Barker and Pauline Jacobsen (eds.), *Direct Compositionality*, Oxford: Oxford University Press, pp. 405–431.

[^predelli-2003]: Predelli, Stefano, 2003. ‘Scare quotes and their relation to other semantic issues’, *Linguistics and Philosophy*, 26(1): 1–28.

[^predelli-2003-2]: –––, 2003. ‘“Subliminable” messages, scare quotes, and the use hypothesis’, *Belgian Journal of Linguistics*, 17: 153–166.

[^predelli-2008]: –––, 2008. ‘The demonstrative theory of quotation’, *Linguistics and Philosophy*, 31(5): 555–572.

[^prior-1971]: Prior, Arthur, 1971. *Objects of Thought*, Oxford: Oxford University Press.

[^quine-1940]: Quine, Willard Van Orman., 1940. *Mathematical Logic*, Boston, MA: Harvard University Press.

[^quine-1955]: –––, 1955. ‘Quantifiers and propositional attitudes’, *Journal of Philosophy*, 53: 177–86.

[^quine-1960]: –––, 1960. *Word and Object*, Cambridge, MA: MIT Press.

[^quine-1961]: –––, 1961. ‘Reference and modality’, in Quine 1961a, pp. 139–159.

[^quine-1961a]: –––, 1961a. *From a Logical Point Of View*, Cambridge, MA: Harvard University Press.

[^rabern-2022]: Rabern, Brian, forthcoming. ‘Pure quotation in linguistic context’, *Journal of Philosophical Logic*, first online 07 September 2022. doi:10.1007/s10992-022-09675-3

[^read-1997]: Read, Stephen, 1997. ‘Quotation and Geach’s puzzle’, *Acta Analytica*, 19(S): 9–20.

[^recanati-2000]: Recanati, François, 2000. *Oratio Obliqua, Oratio Recta: An Essay on Metarepresentation*, Cambridge, MA: MIT Press.

[^recanati-2001]: –––, 2001. ‘Open quotation’, *Mind*, 110: 637–87.

[^recanati-2010]: –––, 2010. *Truth-conditional Pragmatics*, Oxford: Oxford University Press.

[^reichenbach-1947]: Reichenbach, Hans, 1947. *Elements of Symbolic Logic*, New York: Free Press.

[^reimer-1996]: Reimer, Marga, 1996. ‘Quotation marks: demonstratives or demonstrations?’ *Analysis*, 56: 131–42.

[^reimer-2003]: –––, 2003. ‘Too counter-intuitive to believe? Pragmatic accounts of mixed quotation’, *Belgian Journal of Linguistics*, 17: 167–186.

[^richard-1986]: Richard, Mark, 1986. ‘Quotation, grammar, and opacity’, *Linguistics and Philosophy*, 9: 383–403.

[^saka-1998]: Saka, Paul, 1998. ‘Quotation and the use-mention Distinction’, *Mind*, 107: 113–35.

[^saka-1999]: –––, 1999. ‘Quotation: a reply to Cappelen & Lepore’, *Mind*, 108(432): 751–54.

[^saka-2003]: –––, 2003. ‘Quotational constructions’, *Belgian Journal of Linguistics*, 17: 187–212.

[^saka-2006]: –––, 2006. ‘The Demonstrative and Identity Theories of Quotation’, *The Journal of Philosophy*, 103(9): 452–471.

[^saka-2011a]: –––, 2011a. ‘The act of quotation’, in E. Brendal, J. Meibauer, M. Steinbach (eds.), *Understanding Quotation*, Berlin: Mouton De Gruyter, 303–22.

[^saka-2011b]: –––, 2011b. ‘Quotation And Conceptions Of Language’, *dialectica*, 65(2): 205–220.

[^saka-2013]: –––, 2013. ‘Quotation’, *Philosophy Compass*, 8(10): 935–949.

[^saka-2017]: –––, 2017. ‘*Blah,Blah,Blah*: Quasi-quotation and Unquotation’, in Saka and Johnson (eds.) 2017, pp. 35–63.

[^saka-2017-2]: Saka, Paul and Michael Johnson (eds.), 2017. *The Semantics and Pragmatics of Quotation*, Dordrecht: Springer.

[^salmon-1986]: Salmon, Nathan, 1986. *Frege’s Puzzle*, Cambridge, MA: MIT Press.

[^searle-1969]: Searle, John, 1969. *Speech Acts*, Cambridge: Cambridge University Press, §4.1.

[^sellars-1963]: Sellars, W., 1963. ‘Abstract entities’, *Review of Metaphysics*, 16(4): 627–671; reprinted in Sellars, *Philosophical Perspectives*, Springfield, IL, Charles Thomas, 1967, pp. 229–269.

[^seymour-1994]: Seymour, Michel, 1994. ‘Indirect discourse and quotation’, *Philosophical Studies*, 74: 1–38.

[^smullyan-1957]: Smullyan, Raymond, 1957, ‘Languages in which self-reference is possible’, *Journal of Symbolic Logic*, 22: 55–67.

[^sorensen-2008]: Sorensen, Roy, 2008. ‘Empty quotation’, *Analysis*, 68(297): 57–61.

[^sperber-1981]: Sperber, Dan and Deirdre Wilson, 1981. ‘Irony and the use-mention distinction’, in P. Cole (ed.), *Radical Pragmatics*, New York: Academic Press, pp. 295–318.

[^sperber-1986]: –––, 1986. *Relevance: Communication and Cognition*, Oxford: Blackwell; 2nd edition, 1995.

[^stainton-1999]: Stainton, Robert, 1999, ‘Remarks on the syntax and semantics of mixed quotation’, in Murasugi & Stainton, 259–278.

[^tarski-1933]: Tarski, Alfred, 1933. ‘The concept of truth in formalized languages’, in A. Tarski, *Logic, Semantics, Metamathematics*, 2ⁿᵈ edition, Indianapolis: Hackett, 1983, pp. 152–278.

[^tsohatzidis-1998]: Tsohatzidis, Savas, 1998. ‘The hybrid theory of mixed quotation’, *Mind*, 107: 661–64.

[^wallace-1972]: Wallace, Jay, 1972. ‘On the frame of reference’, in *Semantics of Natural Language*, D. Davidson and G. Harman (eds.), Dordrecht: D. Reidel, pp. 219–252.

[^washington-1992]: Washington, Corey, 1992. ‘The identity theory of quotation’, *Journal of Philosophy*, 89: 582–605.

[^wertheimer-1999]: Wertheimer, Roger, 1999. ‘Quotation apposition’, *Philosophical Quarterly*, 49(197): 514–19.

[^wilson-2000]: Wilson, Dan, 2000. ‘Metarepresentation in linguistic communication’, in D. Sperber (ed.), *Metarepresentations: A Multidisciplinary Perspective*, New York: Oxford University Press, pp. 411–448.

[^zeglen-1999]: Zeglen, Urszula, 1999. *Donald Davidson: Truth, Meaning and Knowledge*, London: Routledge.
