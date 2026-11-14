# Truth Values
**First published Tue Mar 30, 2010; substantive revision Sat Mar 1, 2025**

*Shramko, Yaroslav, Wansing, Heinrich*

Truth values have been put to quite different uses in philosophy and logic, being characterized, for example, as:

- primitive abstract objects denoted by sentences in natural and formal languages,
- abstract entities hypostatized as the equivalence classes of sentences,
- what is aimed at in judgements,
- values indicating the degree of truth of sentences,
- entities that can be used to explain the vagueness of concepts,
- values that are preserved in valid inferences,
- values that convey information concerning a given proposition.

Depending on their particular use, truth values have been treated as unanalyzed, as defined, as unstructured, or as structured entities.

The notion of a truth value has been explicitly introduced into logic and philosophy by Gottlob Frege—for the first time in (Frege 1891)[^frege-1891], and most notably in his seminal paper (Frege 1892)[^frege-1892]. Although it was Frege who made the notion of a truth value to one of the central concepts of semantics, the idea of special semantical values, however, was anticipated by Boole and Peirce already, see the survey article on a “history of truth values” by Béziau (2012)[^béziau-2012]. According to Kneale and Kneale (1962: 413)[^kneale-1962], Boole’s system contains all that is needed for its interpretation “in terms of truth values of propositions”, and as Church (1956: 17)[^church-1956] remarks, the “explicit use of two truth-values appears for the first time in a paper by C.S. Peirce in the *American Journal of Mathematics*, vol. 7 (1885), pp. 180–202”. Frege conceived this notion as a natural component of his language analysis where sentences, being saturated expressions, are interpreted as a special kind of names, which refer to (denote, designate, signify) a special kind of objects: truth values. Moreover, there are, according to Frege, only two such objects: *the True* (*das Wahre*) and *the False* (*das Falsche*):

> Every assertoric sentence … is to be regarded as a proper name, and its *Bedeutung*, if it has one, is either the True or the False. (Frege 1892, trans. Beaney 1997: 158)[^beaney-1997][^frege-1892]

This new and revolutionary idea has had a far reaching and manifold impact on the development of modern logic. It provides the means to uniformly complete the formal apparatus of a functional analysis of language by generalizing the concept of a function and introducing a special kind of functions, namely propositional functions, or truth value functions, whose range of values consists of the set of truth values. Among the most typical representatives of propositional functions one finds predicate expressions and logical connectives. As a result, one obtains a powerful tool for a conclusive implementation of the extensionality principle (also called the principle of compositionality), according to which the meaning of a complex expression is uniquely determined by the meanings of its components. On this basis one can also discriminate between extensional and intensional contexts and advance further to the conception of intensional logics. Moreover, the idea of truth values has induced a radical rethinking of some central issues in the philosophy of logic, including: the categorial status of truth, the theory of abstract objects, the subject-matter of logic and its ontological foundations, the concept of a logical system, the nature of logical notions, etc.

In the following, several important philosophical problems directly connected to the notion of a truth value are considered and various uses of this notion are explained.

## 1. Truth values as objects and referents of sentences

### 1.1 Functional analysis of language and truth values

The approach to language analysis developed by Frege rests essentially on the idea of a strict discrimination between two main kinds of expressions: proper names (singular terms) and functional expressions. Proper names designate (signify, denote, or refer to) singular objects, and functional expressions designate (signify, denote, or refer to) functions. [Note: In the literature, the expressions ‘designation’, ‘signification’, ‘denotation’, and ‘reference’ are usually taken to be synonymous. This practice is used throughout the present entry.] The name ‘Ukraine’, for example, refers to a certain country, and the expression ‘the capital of’ denotes a one-place function from countries to cities, in particular, a function that maps Ukraine to Kyiv. Whereas names are “saturated” (complete) expressions, functional expressions are “unsaturated” (incomplete) and may be saturated by applying them to names, producing in this way new names. Similarly, the objects to which singular terms refer are saturated and the functions denoted by functional expression are unsaturated. Names to which a functional expression can be applied are called the *arguments* of this functional expression, and entities to which a function can be applied are called the *arguments* of this function. The object which serves as the reference for the name generated by an application of a functional expression to its arguments is called the *value* of the function for these arguments. Particularly, the above mentioned functional expression ‘the capital of’ remains incomplete until applied to some name. An application of the function denoted by ‘the capital of’ to Ukraine (as an argument) returns Kyiv as the object denoted by the compound expression ‘the capital of Ukraine’ which, according to Frege, is a proper name of Kyiv. Note that Frege distinguishes between an $n$-place function $f$ as an unsaturated entity that can be completed by and applied to arguments $a_1$,…, $a_n$ and its *course of values*, which can be seen as the set-theoretic representation of this function: the set

$$\{\langle a_1, \ldots, a_n, a\rangle \mid a = f(a_1,\ldots , a_n)\}.$$

Pursuing this kind of analysis, one is very quickly confronted with two intricate problems. *First*, how should one treat declarative *sentences*? Should one perhaps separate them into a specific linguistic category distinct from the ones of names and function symbols? And *second*, how—from a functional point of view—should one deal with *predicate expressions* such as ‘is a city’, ‘is tall’, ‘runs’, ‘is bigger than’, ‘loves’, etc., which are used to denote classes of objects, properties of objects, or relations between them and which can be combined with (applied to) singular terms to obtain sentences? If one considers predicates to be a kind of functional expressions, what sort of names are generated by applying predicates to their arguments, and what can serve as referents of these names, respectively values of these functions?

A uniform solution of both problems is obtained by introducing the notion of a *truth value*. Namely, by applying the criterion of “saturatedness” Frege provides a negative answer to the first of the above problems. Since sentences are a kind of complete entities, they should be treated as a sort of proper names, but names destined to denote some specific objects, namely the truth values: *the True* and *the False*. In this way one also obtains a solution of the second problem. Predicates are to be interpreted as some kind of functional expressions, which being applied to these or those names generate sentences referring to one of the two truth values. For example, if the predicate ‘is a city’ is applied to the name ‘Kyiv’, one gets the sentence ‘Kyiv is a city’, which designates *the True* (i.e., ‘Kyiv is a city’ *is true*). On the other hand, by using the name ‘Mount Everest’, one obtains the sentence ‘Mount Everest is a city’ which clearly designates *the False*, since ‘Mount Everest is a city’ *is false*.

Functions whose values are truth values are called *propositional functions*. Frege also referred to them as concepts (*Begriffe*). A typical kind of such functions (besides the ones denoted by predicates) are the functions denoted by propositional connectives. Negation, for example, can be interpreted as a unary function converting *the* True into *the False* and *vice versa*, and conjunction is a binary function that returns *the True* as a value when both its argument positions are filled in by *the True*, etc. Propositional functions mapping $n$-tuples of truth values into truth values are also called *truth-value functions*.

Frege thus in a first step extended the familiar notion of a numerical function to functions on singular objects in general and, moreover, introduced a new kind of singular objects that can serve as arguments and values of functions on singular objects, the truth values. In a further step, he considered propositional functions taking functions as their arguments. The quantifier phrase ‘every city’, for example, can be applied to the predicate ‘is a capital’ to produce a sentence. The argument of the *second-order* function denoted by ‘every city’ is the *first-order* propositional function on singular objects denoted by ‘is a capital’. The functional value denoted by the sentence ‘Every city is a capital’ is a truth value, *the False*.

Truth values thus prove to be an extremely effective instrument for a logical and semantical analysis of language.[^note-1] Moreover, Frege provides truth values (as proper referents of sentences) not merely with a pragmatical motivation but also with a strong theoretical justification. The idea of such justification, that can be found in Frege 1892, employs the principle of *substitutivity* of co-referential terms, according to which the reference of a complex singular term must remain unchanged when any of its sub-terms is replaced by an expression having the same reference. This is actually just an instance of the compositionality principle mentioned above. If sentences are treated as a kind of singular terms which must have designations, then assuming the principle of substitutivity one “almost inevitably” (as Kurt Gödel (1944: 129)[^gödel-1944] explains) is forced to recognize truth values as the most suitable entities for such designations. Accordingly, Frege asks:

> What else but the truth value could be found, that belongs quite generally to every sentence if the reference of its components is relevant, and remains unchanged by substitutions of the kind in question? (Geach and Black 1952: 64)[^geach-1952]

The idea underlying this question has been neatly reconstructed by Alonzo Church in his *Introduction to Mathematical Logic* (1956: 24–25) by considering the following sequence of four sentences:

**C1.**

Sir Walter Scott is the author of *Waverley*.

**C2.**

Sir Walter Scott is the man who wrote 29 *Waverley* Novels altogether.

**C3.**

The number, such that Sir Walter Scott is the man who wrote that many *Waverley* Novels altogether is 29.

**C4.**

The number of counties in Utah is 29.

C1–C4 present a number of conversion steps each producing co-referential sentences. It is claimed that C1 and C2 must have the same designation by substitutivity, for the terms ‘the author of *Waverley*’ and ‘the man who wrote 29 *Waverley* Novels altogether’ designate one and the same object, namely Walter Scott. And so must C3 and C4, because the number, such that Sir Walter Scott is the man who wrote that many *Waverley* Novels altogether is the same as the number of counties in Utah, namely 29. Next, Church argues, it is plausible to suppose that C2, even if not completely synonymous with C3, is at least so close to C3 “so as to ensure its having the same denotation”. If this is indeed the case, then C1 and C4 must have the same denotation (designation) as well. But it seems that the only (semantically relevant) thing these sentences have in common is that both are true. Thus, taken that there must be something what the sentences designate, one concludes that it is just their truth value. As Church remarks, a parallel example involving false sentences can be constructed in the same way (by considering, e.g., ‘Sir Walter Scott is not the author of *Waverley*’).

This line of reasoning is now widely known as the “slingshot argument”, a term coined by Jon Barwise and John Perry (1981: 395), who stressed thus an extraordinary simplicity of the argument and the minimality of presuppositions involved. Stated generally, the pattern of the argument goes as follows (cf. Perry 1996)[^perry-1996]. One starts with a certain sentence, and then moves, step by step, to a completely different sentence. Every two sentences in any step designate presumably one and the same thing. Hence, the starting and the concluding sentences of the argument must have the same designation as well. But the only semantically significant thing they have in common seems to be their truth value. Thus, what any sentence designates is just its truth value.

A formal version of this argument, employing the term-forming, variable-binding class abstraction (or property abstraction) operator λ$x$ (“the class of all $x$ such that” or “the property of being such an $x$ that”), was first formulated by Church (1943)[^church-1943] in his review of Carnap’s *Introduction to Semantics*. Quine (1953)[^quine-1953], too, presents a variant of the slingshot using class abstraction, see also (Shramko and Wansing 2009a)[^shramko-2009a][^shramko-2009a-2]. Other remarkable variations of the argument are those by Kurt Gödel (1944)[^gödel-1944] and Donald Davidson (1967, 1969)[^davidson-1967][^davidson-1969], which make use of the formal apparatus of a theory of definite descriptions dealing with the description-forming, variable-binding iota-operator (ι$x$, “the $x$ such that”). It is worth noticing that the formal versions of the slingshot show how to move—using steps that ultimately preserve reference—from *any* true (false) sentence to *any* other such sentence. In view of this result, it is hard to avoid the conclusion that what the sentences refer to are just truth values.

The slingshot argument has been analyzed in detail by many authors (see especially the comprehensive study by Stephen Neale (Neale 2001)[^neale-2001] and references therein) and has caused much controversy notably on the part of fact-theorists, i.e., adherents of facts, situations, propositions, states of affairs, and other fact-like entities conceived as alternative candidates for denotations of declarative sentences. Also see the [supplement on the slingshot argument](truth-values.slingshot-argument.md).

### 1.2 Truth as a property versus truth as an object

Truth values evidently have something to do with a general concept of truth. Therefore it may seem rather tempting to try to incorporate considerations on truth values into the broader context of traditional truth-theories, such as correspondence, coherence, anti-realistic, or pragmatist conceptions of truth. Yet, it is unlikely that such attempts can give rise to any considerable success. Indeed, the immense fruitfulness of Frege’s introduction of truth values into logic to a large extent is just due to its philosophical neutrality with respect to theories of truth. It does not commit one to any specific metaphysical doctrine of truth. In one significant respect, however, the idea of truth values contravenes traditional approaches to truth by bringing to the forefront the problem of its categorial classification.

In most of the established conceptions, truth is usually treated as a property. It is customary to talk about a “truth predicate” and its attribution to sentences, propositions, beliefs or the like. Such an understanding corresponds also to a routine linguistic practice, when one operates with the adjective ‘true’ and asserts, e.g., ‘That 5 is a prime number is true’. As Scott Soames observes:

> ‘True’ is an adjective that, in its central use, functions as a grammatical predicate, taking nouns and noun phrases as subjects … This grammatical fact encourages us to think that when we assertively utter such a sentence we typically refer to something and say of it that it is true. The thing referred to is called, by philosophers, the *bearer of truth* (falsity). To say of such a thing that it is true (false) is to predicate truth (falsity) of it. In this view, ‘true’ is a logical as well as a grammatical predicate used to describe or characterize entities as having a certain property––truth. (Soames 1999: 13)[^soames-1999]

By contrast with this apparently quite natural attitude, the suggestion to interpret truth as an object may seem very confusing, to say the least. Nevertheless this suggestion is also equipped with a profound and strong motivation demonstrating that it is far from being just an oddity and has to be taken seriously (cf. Burge 1986)[^burge-1986].

First, it should be noted that the view of truth as a property is not as natural as it appears on the face of it. Frege brought into play an argument to the effect that characterizing a sentence as *true* adds nothing new to its content, for ‘It is true that 5 is a prime number’ says exactly the same as just ‘5 is a prime number’. That is, the adjective ‘true’ is in a sense *redundant* and thus is not a real predicate expressing a real property such as the predicates ‘white’ or ‘prime’ which, on the contrary, cannot simply be eliminated from a sentence without an essential loss for its content. In this case a superficial grammatical analogy is misleading. This idea gave an impetus to the deflationary conception of truth (advocated by Ramsey, Ayer, Quine, Horwich, and others, see the entry on the deflationary theory of truth).

However, even admitting the redundancy of truth as a property, Frege emphasizes its importance and indispensable role in some other respect. Namely, truth, accompanying every act of judgment as its ultimate goal, secures an objective *value of cognition* by arranging for every assertive sentence a transition from the level of sense (the thought expressed by a sentence) to the level of denotation (its truth value). This circumstance specifies the significance of taking truth as a particular object. As Tyler Burge explains:

> Normally, the point of using sentences, what “matters to us”, is to claim truth for a thought. The object, in the sense of the point or *objective*, of sentence use was truth. It is illuminating therefore to see truth as an object. (Burge 1986: 120)[^burge-1986]

As it has been observed repeatedly in the literature (cf., e.g., Burge 1986, Ruffino 2003)[^burge-1986][^ruffino-2003], the stress Frege laid on the notion of a truth value was, to a great extent, pragmatically motivated. Besides an intended gain for his system of “Basic Laws” (Frege 1893/1903)[^frege-1893] reflected in enhanced technical clarity, simplicity, and unity, Frege also sought to substantiate in this way his view on logic as a theoretical discipline with truth as its main goal and primary subject-matter. Incidentally, Gottfried Gabriel (1986)[^gabriel-1986] demonstrated that in the latter respect Frege’s ideas can be naturally linked up with a value-theoretical tradition in German philosophy of the second half of the 19ᵗʰ century; see also (Gabriel 2013)[^gabriel-2013] on the relation between Frege’s value-theoretically inspired conception of truth values and his theory of judgement. More specifically, Wilhelm Windelband, the founder and the principal representative of the Southwest school of Neo-Kantianism, was actually the first who employed the term “truth value” (“*Wahrheitswert*”) in his essay “What is Philosophy?” published in 1882 (see Windelband 1915: 32)[^windelband-1915], i.e., nine years before Frege 1891, even if he was very far from treating a truth value as a value of a function.

Windelband defined philosophy as a “critical science about universal values”. He considered philosophical statements to be not mere judgements but rather *assessments*, dealing with some fundamental values, *the value of truth* being one of the most important among them. This latter value is to be studied by logic as a special philosophical discipline. Thus, from a value-theoretical standpoint, the main task of philosophy, taken generally, is to establish the principles of logical, ethical and aesthetical assessments, and Windelband accordingly highlighted the triad of basic values: “true”, “good” and “beautiful”. Later this triad was taken up by Frege in 1918 when he defined the subject-matter of logic (see below). Gabriel points out (1984: 374) that this connection between logic and a value theory can be traced back to Hermann Lotze, whose seminars in Göttingen were attended by both Windelband and Frege.

The decisive move made by Frege was to bring together a philosophical and a mathematical understanding of values on the basis of a generalization of the notion of a function on numbers. While Frege may have been inspired by Windelband’s use of the word ‘value’ (and even more concretely – ‘truth value’), it is clear that he uses the word in its mathematical sense. If predicates are construed as a kind of functional expressions which, being applied to singular terms as arguments, produce sentences, then the values of the corresponding functions must be references of sentences. Taking into account that the range of any function typically consists of objects, it is natural to conclude that references of sentences must be objects as well. And if one now just takes it that sentences refer to truth values (*the True* and *the False*), then it turns out that truth values are indeed objects, and it seems quite reasonable to generally explicate truth and falsity as objects and not as properties. As Frege explains:

> A statement contains no empty place, and therefore we must take its *Bedeutung* as an object. But this *Bedeutung* is a truth-value. Thus the two truth-values are objects. (Frege 1891, trans. Beaney 1997: 140)[^beaney-1997][^frege-1891]

Frege’s theory of sentences as names of truth values has been criticized, for example, by Michael Dummett who stated rather dramatically:

> This was the most disastrous of the effects of the misbegotten doctrine that sentences are a species of complex singular terms, which dominated Frege’s later period: to rob him of the insight that sentences play a unique role, and that the role of almost every other linguistic expression … consists in its part in forming sentences. (Dummett 1981: 196)[^dummett-1981]

But even Dummett (1991: 242)[^dummett-1991] concedes that “to deny that truth-values are objects … seems a weak response”.

The presentation of truth as an object rather than a property seems also to minimize, if not avoid, certain philosophical difficulties associated with the problem of truth-bearers, which is typical for supporters of the interpretation of truth as a property (cf. the above observation of Soames, and also the subsection on truth-bearers in the entry on truth). Indeed, if we construe truth as a certain property, then the question of a bearer (or bearers) of this property naturally arises, and, in particular, about what kind of things can act as such bearers. It is clear that the nature of these things must have a significant impact on the nature of its properties, and in particular on the property of truth. Now, there can be different candidates for the role of truth bearers: “Truth can be predicated of many kinds of things: propositions, sentences, statements, judgements, assertions, declarations, claims, utterances, beliefs, conjectures, hypotheses, theories, stories, etc” (Bar-Hillel 1973: 303)[^bar-hillel-1973]. Moreover, the properties of, say, utterances as physical objects are inherently different from the properties of propositions as abstract objects. Should we then conclude that there are many properties of being true?

One way to avoid such a conclusion is to adopt a kind of *truth-bearer monism*, where only a certain type of entities, whether sentences, propositions, or something else, can play this role. This view, however, seems to be at odds with the usual linguistic practice when we can say that our beliefs are true as much as our statements. Therefore, a weaker view is often adopted, highlighting some kind of entities as *primary* bearers of truth and defining other bearers, which are considered to be derivative or *secondary*, by means of these, (see, e.g., Bar-Hillel 1973, Hanks 2013)[^bar-hillel-1973][^hanks-2013]. This still leaves the question of whether the entities defined as secondary truth bearers really have the property of being true, and if so, whether this property is the same for secondary truth bearers as for the primary ones.

Andrea Strollo (2022) develops a version of *truth-bearer pluralism*. He stresses that “to understand the nature of truth attention should be paid to the kind of entities that are apt to bear it”, and in this respect, truth is similar to “many other properties”. In particular, it is argued that “different kinds of truth bearers tend to support different properties of truth”, and that “there are reasons to admit a plurality of truth bearers”. Thus, Strollo recognizes not only the plurality of truth bearers, but also the *plurality of truth properties* themselves, and argues for the naturalness of such plurality. Nevertheless, the very naturalness of such multiplication of the notion of truth can be questioned and in any case requires special justification.

The situation here is similar to what we have with many other properties when we try to abstract some general meaning from a term that denotes a particular property in its relation to different bearers. To explain this situation it can be useful to involve Aristotle's account of ‘*pros hen* being’ that one can find in the fourth book of *Metaphysics*, where Aristotle says: “There are many senses in which a thing may be said to ‘be’, but all that ‘is’ is related to one central point [πρόσ ἕν]” (Aristotle, Metaphysics IV ($\Gamma$), 1003a 33). Literally, the Greek phrase “*pros hen*” means “in relation to one”. Famously, G.E.L. Owen (1960)[^owen-1960] “names the *pros hen* relation ‘focal meaning’, and claims that it means that all the ‘senses [of “being”] have one focus, one common element’, or ‘a central sense’, so that ‘all its senses can be explained in terms of substance and of the sense of “being” that is appropriate to substance’.” (Yu 2001: 206). By way of example, Aristotle considers the property of *being healthy*, and observes that “everything which is healthy is related to health, one thing in the sense that it preserves health, another in the sense that it produces it, another in the sense that it is a symptom of health, another because it is capable of it” (Aristotle, Metaphysics IV ($\Gamma$), 1003a 35). It can be noted that “these various senses have something in common: a reference to one central thing, health” (Cohen & Reeve 2025)[^cohen-2025]. Remarkably, the latter is a kind of abstraction (*abstract object*) which, through its ‘focal meaning’, determines the particular meanings of all associated properties (more precisely, the meanings of the corresponding expressions).

Now, in like manner, we can take an abstract object, *Truth*, and consider everything that can be true (propositions, sentences, beliefs, etc.) as connected to it by various relations (denoting, expressing, holding, etc.). We have then the relationships of the focal *substance* to various other things which act as bearers of the corresponding property. In this way, it is hoped to reduce all the variety of different particular meanings associated with the property of *being true* to a single ‘focal meaning’ determined by the relevant substance, a certain truth value.

Generally, as Sefrin-Weis (2009: 262)[^sefrin-weis-2009] explains, “focal meaning establishes a kind of “reductive translation” (Owen 1960: 169 and 180)[^owen-1960] of statements about anything in the general field of being to statements about substance”. In Owen's own words:

> The claim of IV that ‘being’ is an expression with focal meaning is a claim that statements about non-substances can be reduced to—translated into—statements about substances and non-substances are no more than the logical shadows of substances. (Owen 1960: 180)[^owen-1960]

Of course, it is always possible to retain the truth predicate in the meta-language and continue to use the more familiar (predicative) wording, by stipulating that, for example, a sentence (proposition, belief, etc.) is considered to be true if and only if it denotes (or in some other relevant way is related to) the truth value “the True”. Such a linguistic convention, understood as a mere abbreviation, would be philosophically harmless, and should not imply any problematic ontological commitments (other than recognizing the corresponding abstract object).

It is worth mentioning that Zalta (2005) provides an analysis of the Tarski-schema that allows one to interpret truth neither as a property, nor as an object, but as a mode of predication. Namely, let us extend a language for the second-order predicate calculus with an abstraction operator $\lambda$ and interpret the $\lambda$-expressions relationally rather than functionally. Then the principle of $\lambda$-Conversion:

$$[\lambda x_1\ldots x_n\: \phi ]y_1\ldots y_n \equiv \phi [y_1,\ldots ,y_n/x_1,\ldots ,x_n] $$

would assert: “objects $x_1,\ldots , x_n$ exemplify being a $y_1,\ldots , y_n$ such that $\phi$ if and only if $x_1,\ldots , x_n$ are such that $\phi$”. Now, $\lambda$-Conversion has also 0-place instances:

$$[\lambda\: \phi] \equiv \phi, $$

which, being interpreted as the propositional Tarski T-Schema, can be read as “that-$\phi$ is true iff $\phi$”. Zalta argues that the expression $[\lambda\: \phi]$ is both a 0-place relation term and a formula, and thus, truth is represented here as the 0-place case of exemplification, i.e., a certain mode of predication. It seems that such a possibility of analyzing the concept of truth is not elaborated in the literature, but it may be a promising direction of its examination.

### 1.3 The ontology of truth values

If truth values are accepted and taken seriously as a special kind of objects, the obvious question as to the nature of these entities arises. The above characterization of truth values as objects is far too general and requires further specification. One way of such specification is to qualify truth values as *abstract* objects. Note that Frege himself never used the word ‘abstract’ when describing truth values. Instead, he has a conception of so called “logical objects”, truth values being primary and the most fundamental of them (Frege 1976: 121)[^frege-1976]. Among the other logical objects Frege pays particular attention to are sets and numbers, emphasizing thus their logical nature (in accordance with his logicist view).

Church (1956: 25)[^church-1956], when considering truth values, explicitly attributes to them the property of being abstract. Since then it is customary to label truth values as abstract objects, thus allocating them into the same category of entities as mathematical objects (numbers, classes, geometrical figures) and propositions. One may pose here an interesting question about the correlation between Fregean logical objects and abstract objects in the modern sense (see the entry on abstract objects). Obviously, the universe of abstract objects is much broader than the universe of logical objects as Frege conceives them. The latter are construed as constituting an ontological foundation for logic, and hence for mathematics (pursuant to Frege’s logicist program). Generally, the class of *abstracta* includes a wide diversity of platonic universals (such as redness, youngness, justice or triangularity) and not only those of them which are logically necessary. Nevertheless, it may safely be said that logical objects can be considered as paradigmatic cases of abstract entities, or abstract objects in their purest form.

It should be noted that finding an adequate definition of abstract objects is a matter of considerable controversy. According to a common view, abstract entities lack spatio-temporal properties and relations, as opposed to concrete objects which exist in space and time (Lowe 1995: 515)[^lowe-1995]. In this respect truth values obviously *are* abstract as they clearly have nothing to do with physical spacetime. In a similar fashion truth values fulfill another requirement often imposed upon abstract objects, namely the one of a causal inefficacy (see, e.g., Grossmann 1992: 7)[^grossmann-1992]. Here again, truth values are very much like numbers and geometrical figures: they have no causal power and make nothing happen.

Finally, it is of interest to consider how truth values can be introduced by applying so-called *abstraction principles*, which are used for supplying abstract objects with *criteria of identity*. The idea of this method of characterizing abstract objects is also largely due to Frege, who wrote:

> If the symbol *a* is to designate an object for us, then we must have a criterion that decides in all cases whether *b* is the same as *a*, even if it is not always in our power to apply this criterion. (Frege 1884, trans. Beaney 1997: 109)[^beaney-1997][^frege-1884]

More precisely, one obtains a new object by abstracting it from some given kind of entities, in virtue of certain criteria of identity for this new (abstract) object. This abstraction is performed in terms of an equivalence relation defined on the given entities (see Wrigley 2006: 161)[^wrigley-2006]. The celebrated slogan by Quine (1969: 23)[^quine-1969] “No entity without identity” is intended to express essentially the same understanding of an (abstract) object as an “item falling under a sortal concept which supplies a well-defined criterion of identity for its instances” (Lowe 1997: 619)[^lowe-1997].

For truth values such a criterion has been suggested in Anderson and Zalta (2004: 2), stating that for any two sentences $p$ and $q$, the truth value of $p$ is identical with the truth value of $q$ if and only if $p$ is (non-logically) equivalent with $q$ (cf. also Dummett 1959: 141)[^dummett-1959]. This idea can be formally explicated following the style of presentation in Lowe (1997: 620)[^lowe-1997]:

$$ \forall p\forall q[(\textit{Sentence}(p) \mathbin{\&} \textit{Sentence}(q)) \Rightarrow(tv(p)=tv(q) \Leftrightarrow(p\leftrightarrow q))], $$

where &, $\Rightarrow, \Leftrightarrow, \forall$ stand correspondingly for ‘and’, ‘if… then’, ‘if and only if’ and ‘for all’ in the *metalanguage*, and $\leftrightarrow$ stands for some *object language* equivalence connective (biconditional).

Incidentally, Carnap (1947: 26)[^carnap-1947], when introducing truth-values as extensions of sentences, is guided by essentially the same idea. Namely, he points out a strong analogy between extensions of predicators and truth values of sentences. Carnap considers a wide class of designating expressions (“designators”) among which there are predicate expressions (“predicators”), functional expressions (“functors”), and some others. Applying the well-known technique of interpreting sentences as predicators of degree 0, he generalizes the fact that two predicators of degree $n$ (say, $P$ and $Q)$ have the same extension if and only if $\forall x_1\forall x_2 \ldots \forall x_n(Px_1 x_2\ldots x_n \leftrightarrow Qx_1 x_2\ldots x_n)$ holds. Then, analogously, two sentences (say, $p$ and $q)$, being interpreted as predicators of degree 0, must have the same extension if and only if $p\leftrightarrow q$ holds, that is if and only if they are equivalent. And then, Carnap remarks, it seems quite natural to take truth values as extensions for sentences.

Note that this criterion employs a *functional dependency* between an introduced abstract object (in this case a truth value) and some other objects (sentences). More specifically, what is considered is the truth value of a sentence (or proposition, or the like). The criterion of identity for truth values is formulated then through the logical relation of equivalence holding between these other objects—sentences, propositions, or the like (with an explicit quantification over them).

It should also be remarked that the properties of the object language biconditional depend on the logical system in which the biconditional is employed. Biconditionals of different logics may have different logical properties, and it surely matters what kind of the equivalence connective is used for defining truth values. This means that the concept of a truth value introduced by means of the identity criterion that involves a biconditional between sentences is also logic-relative. Thus, if ‘$\leftrightarrow$’ stands for material equivalence, one obtains classical truth values, but if the intuitionistic biconditional is employed, one gets truth values of intuitionistic logic, etc. Taking into account the role truth values play in logic, such an outcome seems to be not at all unnatural.

Anderson and Zalta (2004: 13), making use of an object theory from Zalta (1983)[^zalta-1983], propose the following definition of ‘the truth value of proposition $p$’ (‘$tv(p)$’ [notation adjusted]):

$$ tv(p) =_{df} \iota x(A!x \wedge \forall F(xF \leftrightarrow \exists q(q\leftrightarrow p \wedge F= [\lambda y\: q]))), $$

where $A$! stands for a primitive theoretical predicate ‘being abstract’, $xF$ is to be read as “$x$ encodes $F$” and [λ*y q*] is a propositional property (“being such a $y$ that $q$”). (Note that in this system the variable $q$ is used in both term and formula position; in many systems going back to Church and Frege, there are expressions that are both terms and formulas.) That is, according to this definition, “the extension of $p$ is the abstract object that encodes all and only the properties of the form [λ*y q*] which are constructed out of propositions $q$ materially equivalent to $p$” (Anderson and Zalta 2004: 14)[^anderson-2004].

The notion of a truth value in general is then defined as an object which is the truth value of some proposition:

$$TV(x) =_{df} \exists p(x = tv(p)).$$

Using this apparatus, it is possible to explicitly define the Fregean truth values *the True* $(\top)$ and *the False* $(\bot)$:

$$ \begin{align} \top &=_{df} \iota x(A!x \wedge \forall F(xF \leftrightarrow \exists p(p \wedge F= [\lambda y\: p])));\\ \bot &=_{df} \iota x(A!x \wedge \forall F(xF \leftrightarrow \exists p(\neg p \wedge F= [\lambda y\: p]))).\\ \end{align} $$

Anderson and Zalta prove then that $\top$ and $\bot$ are indeed truth values and, moreover, that there are exactly two such objects. The latter result is expected, if one bears in mind that what the definitions above actually introduce are the *classical* truth values (as the underlying logic is classical). Indeed, $p\leftrightarrow q$ is classically equivalent to $(p\wedge q)\vee(\neg p\wedge \neg q)$, and $\neg(p\leftrightarrow q)$ is classically equivalent to $(p\wedge \neg q)\vee(\neg p\wedge q)$. That is, the connective of material equivalence divides sentences into two distinct collections. Due to the law of excluded middle these collections are exhaustive, and by virtue of the law of non-contradiction they are exclusive. Thus, we get exactly two equivalence classes of sentences, each being a hypostatized representative of one of two classical truth values.

## 2. Truth values as logical values

### 2.1 Logic as the science of logical values

In a late paper Frege (1918)[^frege-1918] claims that the word ‘true’ determines the subject-matter of logic in exactly the same way as the word ‘beautiful’ does for aesthetics and the word ‘good’ for ethics. Thus, according to such a view, the proper task of logic consists, ultimately, in investigating “the laws of being true” (Sluga 2002: 86)[^sluga-2002]. By doing so, logic is interested in truth as such, understood objectively, and not in what is merely taken to be true. Now, if one admits that truth is a specific abstract object (the corresponding truth value), then logic in the first place has to explore the features of this object and its interrelations to other entities of various other kinds.

A prominent adherent of this conception was Jan Łukasiewicz. As he paradigmatically put it:

> All true propositions denote one and the same object, namely truth, and all false propositions denote one and the same object, namely falsehood. I consider truth and falsehood to be *singular* objects in the same sense as the number 2 or 4 is. … Ontologically, truth has its analogue in being, and falsehood, in non-being. The objects denoted by propositions are called *logical values*. Truth is the positive, and falsehood is the negative logical value. … Logic is the science of objects of a special kind, namely a science of *logical values*. (Łukasiewicz 1970: 90)

This definition may seem rather unconventional, for logic is usually treated as the science of correct reasoning and valid inference. The latter understanding, however, calls for further justification. This becomes evident, as soon as one asks, *on what grounds* one should qualify this or that pattern of reasoning as correct or incorrect.

In answering this question, one has to take into account that any valid inference should be based on logical rules which, according to a commonly accepted view, should at least guarantee that in a valid inference the conclusion(s) is (are) true if all the premises are true. Translating this demand into the Fregean terminology, it would mean that in the course of a correct inference the possession of the truth value *the True* should be *preserved* from the premises to the conclusion(s). Thus, granting the realistic treatment of truth values adopted by Frege, the understanding of logic as the science of truth values in fact provides logical rules with an ontological justification placing the roots of logic in a certain kind of ideal entities (see Shramko 2014)[^shramko-2014].

These entities constitute a certain uniform domain, which can be viewed as a subdomain of Frege’s so-called “third realm” (the realm of the objective content of thoughts, and generally abstract objects of various kinds (see Frege 1918, cf. Popper 1972 and also Burge 1992: 634)[^burge-1992][^frege-1918][^popper-1972]. Among the subdomains of this third realm one finds, e.g., the collection of mathematical objects (numbers, classes, etc.). The set of truth values may be regarded as forming another such subdomain, namely the one of *logical values*, and logic as a branch of science rests essentially on this *logical domain* and on exploring its features and regularities.

### 2.2 Many-valued logics, truth degrees and valuation systems

According to Frege, there are exactly two truth values, *the True* and *the False*. This opinion appears to be rather restrictive, and one may ask whether it is really indispensable for the concept of a truth value. One should observe that in elaborating this conception, Frege assumed specific requirements of his system of the *Begriffsschrift*, especially the principle of bivalence taken as a metatheoretical principle, viz. that there exist only two distinct logical values. On the object-language level this principle finds its expression in the famous classical laws of excluded middle and non-contradiction. The further development of modern logic, however, has clearly demonstrated that classical logic is only one particular theory (although maybe a very distinctive one) among the vast variety of logical systems. In fact, the Fregean ontological interpretation of truth values depicts logical principles as a kind of ontological postulations, and as such they may well be modified or even abandoned. For example, by giving up the principle of bivalence, one is naturally led to the idea of postulating *many truth values*.

It was Łukasiewicz, who as early as 1918 proposed to take seriously other logical values different from truth and falsehood (see Łukasiewicz 1918, 1920). Independently of Łukasiewicz, Emil Post in his dissertation from 1920, published as (Post 1921)[^post-1921], introduced $m$-valued truth tables, where $m$ is any positive integer. Whereas Post’s interest in *many-valued logic* (where “many” means “more than two”) was almost exclusively mathematical, Łukasiewicz’s motivation was philosophical (see the entry on many-valued logic). He contemplated the semantical value of sentences about the contingent future, as discussed in Aristotle’s *De interpretatione*. Łukasiewicz introduced a third truth value and interpreted it as “possible”. By generalizing this idea and also adopting the above understanding of the subject-matter of logic, one naturally arrives at the representation of particular logical systems as a certain kind of *valuation systems* (see, e.g., Dummett 1981, 2000; Ryan and Sadler 1992)[^dummett-1981][^dummett-2000][^ryan-1992].

Consider a propositional language $\mathcal{L}$ built upon a set of atomic sentences $\mathcal{P}$ and a set of propositional connectives $\mathcal{C}$ (the set of sentences of $\mathcal{L}$ being the smallest set containing $\mathcal{P}$ and being closed under the connectives from $\mathcal{C})$. Then a *valuation system* $\mathbf{V}$ for the language $\mathcal{L}$ is a triple $\langle \mathcal{V}, \mathcal{D}, \mathcal{F}\rangle$, where $\mathcal{V}$ is a non-empty set with at least two elements, $\mathcal{D}$ is a subset of $\mathcal{V}$, and $\mathcal{F} = \{f_{c _1},\ldots, f_{c _m}\}$ is a set of functions such that $f_{c _i}$ is an $n$-place function on $\mathcal{V}$ if $c_i$ is an $n$-place connective. Intuitively, $\mathcal{V}$ is the set of truth values, $\mathcal{D}$ is the set of *designated* truth values, and $\mathcal{F}$ is the set of truth-value functions interpreting the elements of $\mathcal{C}$. If the set of truth values of a valuation system $\mathbf{V}$ has $n$ elements, $\mathbf{V}$ is said to be $n$-valued. Any valuation system can be equipped with an assignment function which maps the set of atomic sentences into $\mathcal{V}$. Each assignment $a$ relative to a valuation system $\mathbf{V}$ can be extended to all sentences of $\mathcal{L}$ by means of a valuation function $v_a$ defined in accordance with the following conditions:

$$ \begin{align} \forall p &\in \mathcal{P} , &v_a (p) &= a(p) ; \tag{1}\\ \forall c_i &\in \mathcal{C} , & v_a ( c_i ( A_1 ,\ldots , A_n )) &= f_{c_i} ( v_a ( A_1 ),\ldots , v_a ( A_n )) \tag{2} \\ \end{align} $$

It is interesting to observe that the elements of $\mathcal{V}$ are sometimes referred to as *quasi truth values*. Siegfried Gottwald (1989: 2)[^gottwald-1989] explains that one reason for using the term ‘quasi truth value’ is that there is no convincing and uniform interpretation of the truth values that in many-valued logic are assumed in addition to the classical truth values *the True* and *the False*, an understanding that, according to Gottwald, associates the additional values with the naive understanding of being true, respectively the naive understanding of *degrees of being true* (cf. also the remark by Font (2009: 383)[^font-2009] that “[o]ne of the main problems in many-valued logic, at least in its initial stages, was the interpretation of the ‘intermediate’ or ‘non-classical’ values”, et seq.). In later publications, Gottwald has changed his terminology and states that

> [t]o avoid any confusion with the case of classical logic one prefers in many-valued logic to speak of *truth degrees* and to use the word “truth value” only for classical logic. (Gottwald 2001: 4)[^gottwald-2001]

Nevertheless in what follows the term ‘truth values’ will be used even in the context of many-valued logics, without any commitment to a philosophical conception of truth as a graded notion or a specific understanding of semantical values in addition to the classical truth values.

Since the cardinality of $\mathcal{V}$ may be greater than 2, the notion of a valuation system provides a natural foundational framework for the very idea of a many-valued logic. The set $\mathcal{D}$ of designated values is of central importance for the notion of a valuation system. This set can be seen as a generalization of the classical truth value *the True* in the sense that it determines many central logical notions and thereby generalizes some of the important roles played by Frege’s *the True* (cf. the introductory remarks about uses of truth values). For example, the set of tautologies (logical laws) is directly specified by the given set of designated truth values: a sentence $A$ is a *tautology* in a valuation system $\mathbf{V}$ iff for every assignment $a$ relative to $\mathbf{V}$, $v_a(A) \in \mathcal{D}$. Another fundamental logical notion—that of an entailment relation—can also be defined by referring to the set $\mathcal{D}$. For a given valuation system $\mathbf{V}$ a corresponding entailment relation $(\vDash_V)$ is usually defined by postulating the preservation of designated values from the premises to the conclusion:

$$ \tag{3} \Delta\vDash_V A \textrm{ iff }\forall a[(\forall B \in \Delta: v_a (B) \in \mathcal{D}) \Rightarrow v _a (A) \in \mathcal{D}]. $$

A pair $\mathcal{M} = \langle \mathbf{V}, v_a\rangle$, where $\mathbf{V}$ is an $(n$-valued) valuation system and $v_a$ a valuation in $\mathbf{V}$, may be called an $(n$-valued) *model* based on $\mathbf{V}$. Every model $\mathcal{M} = \langle \mathbf{V}, v_a\rangle$ comes with a corresponding entailment relation $\vDash_{\mathcal{M}}$ by defining $\Delta\vDash_{\mathcal{M} }A\textrm{ iff }(\forall B \in \Delta: v_a (B) \in \mathcal{D}) \Rightarrow v_a(A) \in \mathcal{D}$.

Suppose $\mathfrak{L}$ is a syntactically defined logical system $\mathfrak{L}$ with a consequence relation $\vdash_{ \mathfrak{L} }$, specified as a relation between the power-set of $\mathcal{L}$ and $\mathcal{L}$. Then a valuational system $\mathbf{V}$ is said to be *strictly characteristic* for $\mathfrak{L}$ just in case $\Delta\vDash_V A \textrm{ iff } \Delta\vdash_{ \mathfrak{L} }A$ (see Dummett 1981: 431)[^dummett-1981]. Conversely, one says that $\mathfrak{L}$ *is characterized* by $\mathbf{V}$. Thus, if a valuation system is said to *determine* a logic, the valuation system *by itself* is, properly speaking, *not* a logic, but only serves as a semantic basis for some logical system. Valuation systems are often referred to as (*logical*) *matrices*. Note that in (Urquhart 1986)[^urquhart-1986], the set $\mathcal{D}$ of designated elements of a matrix is required to be non-empty, and in Dunn & Hardegree 2001, $\mathcal{D}$ is required to be a non-empty proper subset of $\mathbf{V}$. With a view on semantically defining a many-valued logic, these restrictions are very natural and have been taken up in (Shramko & Wansing 2011)[^shramko-2011] and elsewhere. For the characterization of consequence relations (see the supplementary document [Suszko’s Thesis](truth-values.suszko-thesis.md)), however, the restrictions do not apply.

In this way Fregean, i.e., classical, logic can be presented as determined by a particular valuation system based on exactly two elements: $\mathbf{V}_{cl} = \langle \{T, F\}, \{T\}, \{ f_{\wedge}, f_{\vee}, f_{\rightarrow}, f_{\sim}\}\rangle$, where $f_{\wedge}, f_{\vee}, f_{\rightarrow},f_{\sim}$ are given by the classical truth tables for conjunction, disjunction, material implication, and negation.

As an example for a valuation system based on more that two elements, consider two well-known valuation systems which determine Kleene’s (strong) “logic of indeterminacy” $K_3$ and Priest’s “logic of paradox” $P_3$. In a propositional language without implication, $K_3$ is specified by the *Kleene matrix* $\mathbf{K}_3 = \langle \{T, I, F\}, \{T\}, \{ f_c: c \in \{\sim , \wedge , \vee \}\} \rangle$, where the functions $f_c$ are defined as follows:

$$ \begin{array}{c|c} f_\sim & \\ \hline T & F \\ I & I \\ F & T \\ \end{array}\quad \begin{array}{c|c|c|c} f_\wedge & T & I & F \\ \hline T & T & I & F \\ I & I & I & F \\ F & F & F & F \\ \end{array}\quad \begin{array}{c|c|c|c} f_\vee & T & I & F \\ \hline T & T & T & T \\ I & T & I & I \\ F & T & I & F \\ \end{array} $$

The *Priest matrix* $\mathbf{P}_3$ differs from $\mathbf{K}_3$ only in that $\mathcal{D} = \{T, I\}$. Entailment in $\mathbf{K}_3$ as well as in $\mathbf{P}_3$ is defined by means of (3).

There are natural intuitive interpretations of $I$ in $\mathbf{K}_3$ and in $\mathbf{P}_3$ as the *underdetermined* and the *overdetermined* value respectively—a truth-value gap and a truth-value glut. Formally these interpretations can be modeled by presenting the values as certain subsets of the set of classical truth values $\{T, F\}$. Then $T$ turns into $\mathbf{T} = \{T\}$ (understood as “true only”), $F$ into $\mathbf{F} = \{F\}$ (“false only”), $I$ is interpreted in $K_3$ as $\mathbf{N} = \{\} = \varnothing$ (“*neither* true nor false”), and in $P_3$ as $\mathbf{B} = \{T, F\}$ (“*both* true and false”). (Note that also Asenjo (1966)[^asenjo-1966] considers the same truth-tables with an interpretation of the third value as “antinomic”.) The designatedness of a truth value can be understood in both cases as containment of the classical $T$ as a member.

If one combines all these new values into a joint framework, one obtains the four-valued logic $B_4$ introduced by Dunn (1976)[^dunn-1976] and Belnap (1977a, b). A Gentzen-style formulation can be found in (Font 1997: 7)[^font-1997]. This logic is determined by the *Belnap matrix* $\mathbf{B}_4 = \langle \{\mathbf{N}, \mathbf{T}, \mathbf{F}, \mathbf{B}\}, \{\mathbf{T}, \mathbf{B}\}, \{ f_c: c \in \{\sim , \wedge , \vee \}\}\rangle$, where the functions $f_c$ are defined as follows:

$$ \begin{array}{c|c} f_\sim & \\ \hline T & F \\ B & B \\ N & N \\ F & T \\ \end{array}\quad \begin{array}{c|c|c|c|c} f_\wedge & T & B & N & F \\ \hline T & T & B & N & F \\ B & B & B & F & F \\ N & N & F & N & F \\ F & F & F & F & F\\ \end{array}\quad \begin{array}{c|c|c|c|c} f_\vee & T & B & N & F \\ \hline T & T & T & T & T\\ B & T & B & T & B \\ N & T & T & N & N \\ F & T & B & N & F \\ \end{array} $$

Definition (3) applied to the Belnap matrix determines the entailment relation of $\mathbf{B}_4$. This entailment relation is formalized as the well-known logic of “first-degree entailment” ($E_{fde}$) introduced in Anderson & Belnap (1975) (see also Omori and Wansing 2017)[^omori-2017].

The syntactic notion of a single-conclusion consequence relation has been extensively studied by representatives of the Polish school of logic, most notably by Alfred Tarski, who in fact initiated this line of research (see Tarski 1930a,b; cf. also Wójcicki 1988)[^tarski-1930a][^wójcicki-1988]. In view of certain key features of a standard consequence relation it is quite remarkable—as well as important—that any entailment relation $\vDash_V$ defined as above has the following structural properties (see Ryan and Sadler 1992: 34)[^ryan-1992]:

$$\begin{align} \tag{4} \Delta\cup \{A\}&\vDash_V A &\textrm{(Reflexivity)} \\ \tag{5} \textrm{If } \Delta\vDash_V A \textrm{ then } \Delta\cup \Gamma &\vDash_V A &\textrm{(Monotonicity)}\\ \tag{6} \textrm{If } \Delta\vDash_V A \textrm{ for every } A \in \Gamma &\\ \textrm{ and } \Gamma \cup \Delta \vDash_V B, \textrm{ then } \Delta &\vDash_VB & \textrm{(Cut)} \end{align}$$

Moreover, for every $A \in \mathcal{L}$, every $\Delta \subseteq \mathcal{L}$, and every uniform substitution function $\sigma$ on $\mathcal{L}$ the following *Substitution* property holds ($\sigma(\Delta)$ stands for $\{ \sigma(B) \mid B \in \Delta\})$:

$$ \tag{7} \Delta\vDash_V A \textrm{ implies } \sigma(\Delta)\vDash_V \sigma(A). $$

(The function of uniform substitution $\sigma$ is defined as follows. Let $B$ be a formula in $\mathcal{L}$, let $p_1,\ldots, p_n$ be all the propositional variables occurring in $B$, and let $\sigma(p_1) = A_1,\ldots , \sigma(p_n) = A_n$ for some formulas $A_1 ,\ldots ,A_n$. Then $\sigma(B)$ is the formula that results from B by substituting simultaneously $A_1$,…, $A_n$ for all occurrences of $p_1,\ldots, p_n$, respectively.)

If $\vDash_V$ in the conditions (4)–(6) is replaced by $\vdash_{ \mathfrak{L} }$, then one obtains what is often called a *Tarskian consequence relation*. If additionally a consequence relation has the substitution property (7), then it is called *structural*. Thus, any entailment relation defined for a given valuation system $\mathbf{V}$ presents an important example of a consequence relation, in that $\mathbf{V}$ is strictly characteristic for some logical system $\mathfrak{L}$ with a structural Tarskian consequence relation.

Generally speaking, the framework of valuation systems not only perfectly suits the conception of logic as the science of truth values, but also turns out to be an effective technical tool for resolving various sophisticated and important problems in modern logic, such as soundness, completeness, independence of axioms, etc.

### 2.3 Truth values, truth degrees, and vague concepts

The term ‘truth degrees’, used by Gottwald and many other authors, suggests that truth comes by degrees, and these degrees may be seen as truth values in an extended sense. The idea of truth as a graded notion has been applied to model vague predicates and to obtain a solution to the Sorites Paradox, the Paradox of the Heap (see the entry on the Sorites Paradox). However, the success of applying many-valued logic to the problem of vagueness is highly controversial. Timothy Williamson (1994: 97)[^williamson-1994], for example, holds that the phenomenon of higher-order vagueness “makes most work on many-valued logic irrelevant to the problem of vagueness”.

In any case, the vagueness of concepts has been much debated in philosophy (see the entry on vagueness) and it was one of the major motivations for the development of *fuzzy logic* (see the entry on fuzzy logic). In the 1960s, Lotfi Zadeh (1965)[^zadeh-1965] introduced the notion of a *fuzzy set*. A characteristic function of a set $X$ is a mapping which is defined on a superset $Y$ of $X$ and which indicates membership of an element in $X$. The range of the characteristic function of a classical set $X$ is the two-element set $\{0,1\}$ (which may be seen as the set of classical truth values). The function assigns the value 1 to elements of $X$ and the value 0 to all elements of $Y$ not in $X$. A fuzzy set has a membership function ranging over the real interval [0,1]. A vague predicate such as ‘is much earlier than March 20ᵗʰ, 1963’, ‘is beautiful’, or ‘is a heap’ may then be regarded as denoting a fuzzy set. The membership function $g$ of the fuzzy set denoted by ‘is much earlier than March 20ᵗʰ, 1963’ thus assigns values (seen as truth degrees) from the interval [0, 1] to moments in time, for example $g$(1p.m., August 1ˢᵗ, 2006) $= 0$, $g$(3a.m., March 19ᵗʰ, 1963) $= 0$, $g$(9:16a.m., April 9ᵗʰ, 1960) $= 0.005$, $g$(2p.m., August 13ᵗʰ, 1943) $= 0.05$, $g$(7:02a.m., December 2ⁿᵈ, 1278) $= 1$.

The application of continuum-valued logics to the Sorites Paradox has been suggested by Joseph Goguen (1969)[^goguen-1969]. The Sorites Paradox in its so-called conditional form is obtained by repeatedly applying *modus ponens* in arguments such as:

- A collection of 100,000 grains of sand is a heap.
- If a collection of 100,000 grains of sand is a heap, then a collection 99,999 grains of sand is a heap.
- If a collection of 99,999 grains of sand is a heap, then a collection 99,998 grains of sand is a heap.
- …
- If a collection of 2 grains of sand is a heap, then a collection of 1 grain of sand is a heap.
- Therefore: A collection of 1 grain of sand is a heap.

Whereas it seems that all premises are acceptable, because the first premise is true and one grain does not make a difference to a collection of grains being a heap or not, the conclusion is, of course, unacceptable. If the predicate ‘is a heap’ denotes a fuzzy set and the conditional is interpreted as implication in Łukasiewicz’s continuum-valued logic, then the Sorites Paradox can be avoided. The truth-function $f_{\rightarrow}$ of Łukasiewicz’s implication $\rightarrow$ is defined by stipulating that if $x \le y$, then $f_{\rightarrow}(x, y) = 1$, and otherwise $f_{\rightarrow}(x, y) = 1 - (x - y)$. If, say, the truth value of the sentence ‘A collection of 500 grains of sand is a heap’ is 0.8 and the truth value of ‘A collection of 499 grains of sand is a heap’ is 0.7, then the truth value of the implication ‘If a collection of 500 grains of sand is a heap, then a collection 499 grains of sand is a heap.’ is 0.9. Moreover, if the acceptability of a statement is defined as having a value greater than $j$ for $0 \lt j \lt 1$ and all the conditional premises of the Sorites Paradox do not fall below the value $j$, then *modus ponens* does not preserve acceptability, because the conclusion of the Sorites Argument, being evaluated as 0, is unacceptable.

Alasdair Urquhart (1986: 108)[^urquhart-1986] stresses

> the extremely artificial nature of the attaching of precise numerical values to sentences like … “Picasso’s *Guernica* is beautiful”.

To overcome the problem of assigning precise values to predications of vague concepts, Zadeh (1975)[^zadeh-1975] introduced *fuzzy truth values* as distinct from the numerical truth values in [0, 1], the former being fuzzy subsets of the set [0, 1], understood as *true*, *very true*, *not very true*, etc.

The interpretation of continuum-valued logics in terms of fuzzy set theory has for some time be seen as defining the field of mathematical fuzzy logic. Susan Haack (1996)[^haack-1996] refers to such systems of mathematical fuzzy logic as “base logics” of fuzzy logic and reserves the term ‘fuzzy logics’ for systems in which the truth values themselves are fuzzy sets. Fuzzy logic in Zadeh’s latter sense has been thoroughly criticized from a philosophical point of view by Haack (1996)[^haack-1996] for its “methodological extravagances” and its linguistic incorrectness. Haack emphasizes that her criticisms of fuzzy logic do not apply to the base logics. Moreover, it should be pointed out that mathematical fuzzy logics are nowadays studied not in the first place as continuum-valued logics, but as many-valued logics related to residuated lattices (see Hajek 1998; Cignoli *et al.* 2000; Gottwald 2001; Galatos *et al.* 2007)[^cignoli-2000][^galatos-2007][^gottwald-2001][^hajek-1998], whereas fuzzy logic in the broad sense is to a large extent concerned with certain engineering methods.

A fundamental concern about the semantical treatment of vague predicates is whether an adequate semantics should be truth-functional, that is, whether the truth value of a complex formula should depend functionally on the truth values of its subformulas. Whereas mathematical fuzzy logic is truth-functional, Williamson (1994: 97)[^williamson-1994] holds that “the nature of vagueness is not captured by any approach that generalizes truth-functionality”. According to Williamson, the degree of truth of a conjunction, a disjunction, or a conditional just fails to be a function of the degrees of truth of vague component sentences. The sentences ‘John is awake’ and ‘John is asleep’, for example, may have the same degree of truth. By truth-functionality the sentences ‘If John is awake, then John is awake’ and ‘If John is awake, then John is asleep’ are alike in truth degree, indicating for Williamson the failure of degree-functionality.

One way of in a certain sense non-truthfunctionally reasoning about vagueness is supervaluationism. The method of supervaluations has been developed by Henryk Mehlberg (1958)[^mehlberg-1958] and Bas van Fraassen (1966)[^fraassen-1966] and has later been applied to vagueness by Kit Fine (1975)[^fine-1975], Rosanna Keefe (2000)[^keefe-2000] and others.

Van Fraassen’s aim was to develop a semantics for sentences containing non-denoting singular terms. Even if one grants atomic sentences containing non-denoting singular terms and that some attributions of vague predicates are neither true nor false, it nevertheless seems natural not to preclude that compound sentences of a certain shape containing non-denoting terms or vague predications *are* either true or false, e.g., sentences of the form ‘If $A$, then $A$’. Supervaluational semantics provides a solution to this problem. A three-valued assignment $a$ into $\{T, I, F\}$ may assign a truth-value gap (or rather the value $I)$ to the vague sentence ‘Picasso’s *Guernica* is beautiful’. Any classical assignment $a'$ that agrees with $a$ whenever $a$ assigns $T$ or $F$ may be seen as a precisification (or superassignment) of $a$. A sentence may than be said to be supertrue under assignment $a$ if it is true under every precisification $a'$ of $a$. Thus, if $a$ is a three-valued assignment into $\{T, I, F\}$ and $a'$ is a two-valued assignment into $\{T, F\}$ such that $a(p) = a'(p)$ if $a(p) \in \{T, F\}$, then $a'$ is said to be a *superassignment* of $a$. It turns out that if $a$ is an assignment extended to a valuation function $v_a$ for the Kleene matrix $\mathbf{K}_3$, then for every formula $A$ in the language of $\mathbf{K}_3$, $v_a (A) = v_{a'}(A)$ if $v_a (A) \in \{T, F\}$. Therefore, the function $v_{a'}$ may be called a *supervaluation* of $v_a$. A formula is then said to be *supertrue* under a valuation function $v_a$ for $\mathbf{K}_3$ if it is true under every supervaluation $v_{a'}$ of $v_a$, i.e., if $v_{a'}(A) = T$ for every supervaluation $v_{a'}$ of $v_a$. The property of being *superfalse* is defined analogously.

Since every supervaluation is a classical valuation, every classical tautology is supertrue under every valuation function in $\mathbf{K}_3$. Supervaluationism is, however, not truth-functional with respect to supervalues. The supervalue of a disjunction, for example, does not depend on the supervalue of the disjuncts. Suppose $a(p) = I$. Then $a(\neg p) = I$ and $v_{a'} (p\vee \neg p) = T$ for every supervaluation $v_{a'}$ of $v_a$. Whereas $(p\vee \neg p)$ is thus supertrue under $v_a,p\vee p$ is *not*, because there are superassignments $a'$ of $a$ with $a'(p) = F$. An argument against the charge that supervaluationism requires a non-truth-functional semantics of the connectives can be found in MacFarlane (2008)[^macfarlane-2008] (cf. also other references given there).

Although the possession of supertruth is preserved from the premises to the conclusion(s) of valid inferences in supervaluationism, and although it might be tempting to consider supertruth an abstract object on its own, it seems that it has never been suggested to hypostatize supertruth in this way, comparable to Frege’s *the True*. A sentence supertrue under a three-valued valuation $v$ just takes the Fregean value *the True* under every supervaluation of $v$. The advice not to confuse supertruth with “real truth” can be found in Belnap (2009)[^belnap-2009].

### 2.4 Suszko’s thesis and anti-designated values

One might, perhaps, think that the mere existence of many-valued logics shows that there exist infinitely, in fact, uncountably many truth values. However, this is not at all clear (recall the more cautious use of terminology advocated by Gottwald).

In the 1970’s Roman Suszko (1977: 377)[^suszko-1977] declared many-valued logic to be “a magnificent conceptual deceit”. Suszko actually claimed that “there are but two logical values, true and false” (Caleiro *et al*. 2005: 169)[^caleiro-2005], a statement now called *Suszko’s Thesis*. For Suszko, the set of truth values assumed in a logical matrix for a many-valued logic is a set of “admissible referents” (called “algebraic values”) of formulas but not a set of logical values. Whereas the algebraic values are elements of an algebraic structure and referents of formulas, the logical value *true* is used to define valid consequence: If every premise is true, then so is (at least one of) the conclusion(s). The other logical value, *false*, is preserved in the opposite direction: If the (every) conclusion is false, then so is at least one of the premises. The logical values are thus represented by a bi-partition of the set of algebraic values into a set of designated values (truth) and its complement (falsity).

Essentially the same idea has been taken up earlier by Dummett (1959)[^dummett-1959] in an influential paper, where he asks

> what point there may be in distinguishing between different ways in which a statement may be true or between different ways in which it may be false, or, as we might say, between degrees of truth and falsity. (Dummett 1959: 153)[^dummett-1959]

Dummett observes that, first,

> the sense of a sentence is determined wholly by knowing the case in which it has a designated value and the cases in which it has an undesignated one,

and moreover,

> finer distinctions between different designated values or different undesignated ones, however naturally they come to us, are justified only if they are needed in order to give a truth-functional account of the formation of complex statements by means of operators. (Dummett 1959: 155)[^dummett-1959]

Suszko’s claim evidently echoes this observation by Dummett.

Suszko’s Thesis is substantiated by a rigorous proof (the Suszko Reduction) showing that every structural Tarskian consequence relation and therefore also every structural Tarskian many-valued propositional logic is characterized by a bivalent semantics. (Note also that Richard Routley (1975)[^routley-1975] has shown that every logic based on a λ-categorical language has a sound and complete bivalent possible worlds semantics.) The dichotomy between designated values and values which are not designated and its use in the definition of entailment plays a crucial role in the Suszko Reduction. Nevertheless, while it seems quite natural to construe the set of designated values as a generalization of the classical truth value $T$ in some of its significant roles, it would not always be adequate to interpret the set of non-designated values as a generalization of the classical truth value $F$. The point is that in a many-valued logic, unlike in classical logic, “not true” does not always mean “false” (cf., e.g., the above interpretation of Kleene’s logic, where sentences can be neither true nor false).

In the literature on many-valued logic it is sometimes proposed to consider a set of *antidesignated* values which not obligatorily constitute the complement of the set of designated values (see, e.g., Rescher 1969, Gottwald 2001)[^gottwald-2001][^rescher-1969]. The set of antidesignated values can be regarded as representing a generalized concept of falsity. This distinction leaves room for values that are *neither* designated *nor* antidesignated and even for values that are *both* designated *and* antidesignated.

Grzegorz Malinowski (1990, 1994)[^malinowski-1990][^malinowski-1994] takes advantage of this proposal to give a counterexample to Suszko’s Thesis. He defines the notion of a single-conclusion *quasi*-consequence $(q$-consequence) relation. The semantic counterpart of $q$-consequence is called $q$-entailment. Single-conclusion $q$-entailment is defined by requiring that if no premise is antidesignated, the conclusion is designated. Malinowski (1990)[^malinowski-1990] proved that for every structural $q$-consequence relation, there exists a characterizing class of $q$-matrices, matrices which in addition to a subset $\mathcal{D}^{+}$of designated values comprise a disjoint subset $\mathcal{D}^-$of antidesignated values. Not every $q$-consequence relation has a bivalent semantics.

In the supplementary document [Suszko’s Thesis](truth-values.suszko-thesis.md), Suszko’s reduction is introduced, Malinowski’s counterexample to Suszko’s Thesis is outlined, and a short analysis of these results is presented.

Can one provide evidence for a multiplicity of logical values? More concretely, $is$ there more than one logical value, each of which may be taken to determine its own (independent) entailment relation? A positive answer to this question emerges from considerations on truth values as structured entities which, by virtue of their internal structure, give rise to natural partial orderings on the set of values.

### 2.5 Some approaches to truth value functions

One way of generalizing the notion of a truth value function was proposed by Arnon Avron and his collaborators by introducing the idea of *non-deterministic matrices* (see, e.g., Avron and Konikowska 2005, Avron and Lev 2005, Avron and Zamansky 2010, and, for earlier work, Kearns 1981, Ivlev 1988)[^avron-2005][^avron-2005-2][^avron-2010][^ivlev-1988][^kearns-1981]. The standard valuation systems as described above rely on the principle of compositionality, so that the truth value of a (compound) sentence is uniquely determined by the truth values of its components. However, this principle may be too strong for some situations, and one may try to weaken it by allowing (in certain cases) the truth values of sentences to be chosen *nondeterministically* from some non-empty set of options. In this way we obtain the notion of a non-deterministic matrix, which differs from a standard valuation system in that each truth value function from a set of functions $\cal{F}$ $=$ $\{f_{c_{1}}, \ldots f_{c_{m}}\}$ is now defined as a map from ${\cal V}^n$ to ${\cal P}({\cal V}) \backslash \lbrace \varnothing\rbrace$. Thus, the value $v_{a}(c_i (A_1, \ldots , A_n))$ of the sentence $c_i (A_1, \ldots , A_n)$ induced by an assignment $a$ is taken (non-deterministically) from a non-empty set of values. Such a situation may occur, in particular, in cases of linguistic ambiguity, when, for example, we use the connective “or” and it is not quite clear whether we are dealing with inclusive or exclusive disjunction, see (Avron and Zamansky 2010)[^avron-2010]. Then we simply allow the disjunction to take some value from the set $\{T, F\}$ if both disjuncts are true, and which value is chosen in this or that case may depend on additional information, namely whether “or” is used inclusively or exclusively:

$$\begin{array}{c|c|c} f_\vee & T & F \\ \hline T & \{T, F\} & \{T\} \\ F & \{T\} & \{F\} \\ \end{array}$$

Non-deterministic matrices have proven to be very useful in various areas, such as automated deduction, approximating logics, paraconsistent logics, fuzzy logics and others. There is now a bulk of work on non-deterministic semantics, including especially non-deterministic semantics for modal logics (see, for example Omori and Skurt 2016, 2020, Coniglio, del Cerro, and Peron 2019, Pawlowski and Skurt 2024)[^omori-2016][^omori-2019][^omori-2020][^pawlowski-2024]. In (Omori and Skurt 2020)[^omori-2020] it is shown that there exist modal logics that possess a non-deterministic semantics but no standard Kripke semantics.

Usually, in a context, sentences are taken to be connected by various relations. From a logical perspective, it is important to focus on those relations between sentences that are determined by the relations between their truth-values. Such relations are associated with truth functions. On the other side, every function is a relation. Humberstone (2023)[^humberstone-2023] discusses, as one way of connecting a relation with a given function, the association of an $n$-place Boolean truth function ${f \!\!:}$ ${\{T,F\}^n {\longrightarrow} \{T,F\}}$ with the $n$-place de-characteristic relation ${\stackrel{\leftarrow}{\chi}}(f)$ of $f$ that is defined as follows:

$${\stackrel{\leftarrow}{\chi}}(f) := \{\langle a_1, \ldots , a_n\rangle \mid f( a_1, \ldots , a_n) = T\}.$$

Since ${\stackrel{\leftarrow}{\chi}}({\stackrel{}{\chi}}(R)) = R$ for any relation $R$ and its characteristic function ${\stackrel{}{\chi}}(R)$ and ${\stackrel{}{\chi}} ({\stackrel{\leftarrow}{\chi}}(f)) = f$ for any function into $\{T,F\}$, the functional and relational perspectives are intertranslatable. Humberstone shows that the relational point of view nevertheless can be useful in practice, for instance, when the consideration of relations among truth values is lifted to relations among formulas of propositional languages that obtain in virtue of the truth-value relations among the truth-values assigned to the formulas. Given a class $\cal V$ of valuation functions taking values in $\{T,F\}$ and $v \in {\cal V}$, and restricting attention to binary connectives $\sharp$, two kinds of such relations among formulas can be defined by setting:

$$ \begin{array}{lcl} R^{\sharp}_{{v}}(A , B) & \mbox{iff} & v(A \sharp B) = T \\ R^{\sharp}_{{\cal V}}(A , B) & \mbox{iff} & \mbox{for all } v \in {\cal V}\!: R^{\sharp}_{{v}}(A , B), \end{array} $$

where in general $\sharp$ is not required to denote a truth function over $\cal V$ such that there is a function ${g\!:}$ $\{T,F\}^2 \longrightarrow \{T,F\}$ and for all $v \in {\cal V}$ and formulas $A$, $B$, $v(A \sharp B) = g((v(A), v(B))$. If such a function $g$ exists, then the first item can be stated as $R^{\sharp}_{{v}}(A ,B)$ iff $\langle v(A), v(B)\rangle \in {\stackrel{\leftarrow}{\chi}} (g)$. One can then compare properties of the local relations $R^{\sharp}_{{v}}$ with properties of the global relation $R^{\sharp}_{{\cal V}}$. If the semantic consequence relation $\models _{{\cal V}}$ with respect to $\cal V$ is as usually defined by requiring that for any set $\Gamma \cup \{A\}$ of formulas and $v \in {\cal V}$, $\Gamma \models _{{\cal V}} A$ iff $v(A) = T$ whenever $v(B) = T$ for every $B \in \Gamma$, one can observe, e.g., that in general the transitivity of $R^{\sharp}_{{\cal V}}$ does not imply the transitivity of the relations $R^{\sharp}_{{v}}$ and that also the symmetry of $R^{\sharp}_{{\cal V}}$ does not imply the symmetry of the relations $R^{\sharp}_{{v}}$. Humberstone's motivation for taking the truth-value relational perspective is its explanatory value, for example in making certain proofs more evident by invoking facts such as that any reflexive relation on a two-element set is transitive.

## 3. Ordering relations between truth-values

### 3.1 The notion of a logical order

As soon as one admits that truth values come with valuation *systems*, it is quite natural to assume that the elements of such a system are somehow *interrelated*. And indeed, already the valuation system for classical logic constitutes a well-known algebraic structure, namely the two-element Boolean algebra with $\cap$ and $\cup$ as meet and join operators (see the entry on the mathematics of Boolean algebra). In its turn, this Boolean algebra forms a lattice with a *partial order* defined by $a\le_t b \textrm{ iff } a\cap b = a$. This lattice may be referred to as *TWO*. It is easy to see that the elements of *TWO* are ordered as follows: $F\le_t T$. This ordering is sometimes called the *truth order* (as indicated by the corresponding subscript), for intuitively it expresses an increase in truth: $F$ is “less true” than $T$. It can be schematically presented by means of a so-called Hasse-diagram as in Figure 1.

*Figure 1:* Lattice *TWO*

It is also well-known that the truth values of both Kleene’s and Priest’s logic can be ordered to form a lattice (*THREE*), which is diagrammed in Figure 2.

*Figure 2:* Lattice *THREE*

Here $\le_t$ orders $T, I$ and $F$ so that the intermediate value $I$ is “more true” than $F$, but “less true” than $T$.

The relation $\le_t$ is also called a *logical order*, because it can be used to determine key logical notions: logical connectives and an entailment relation. Namely, if the elements of the given valuation system $\mathbf{V}$ form a lattice, then the operations of meet and join with respect to $\le_t$ are usually seen as the functions for conjunction and disjunction, whereas negation can be represented by the inversion of this order. Moreover, one can consider an entailment relation for $\mathbf{V}$ as expressing agreement with the truth order, that is, the conclusion should be at least as true as the premises taken together:

$$ \tag{8} \Delta\vDash B\textrm{ iff }\forall v_a[\Pi_t\{ v_a (A) \mid A \in \Delta\} \le_t v_a (B)], $$

where $\Pi_t$ is the lattice meet in the corresponding lattice.

The Belnap matrix $\mathbf{B}_4$ considered above also can be represented as a partially ordered valuation system. The set of truth values $\{\mathbf{N}, \mathbf{T}, \mathbf{F}, \mathbf{B}\}$ from $\mathbf{B}_4$ constitutes a specific algebraic structure – the *bilattice* FOUR$_2$ presented in Figure 3 (see, e.g., Ginsberg 1988, Arieli and Avron 1996, Fitting 2006)[^arieli-1996][^fitting-2006][^ginsberg-1988].

*Figure 3:* The bilattice *FOUR*$_2$

This bilattice is equipped with *two* partial orderings; in addition to a truth order, there is an information order $(\le_i )$ which is said to order the values under consideration according to the information they give concerning a formula to which they are assigned. Lattice meet and join with respect to $\le_t$ coincide with the functions $f_{\wedge}$ and $f_{\vee}$ in the Belnap matrix $\mathbf{B}_4$, $f_{{\sim}}$ turns out to be the truth order inversion, and an entailment relation, which happens to coincide with the matrix entailment, is defined by (8). *FOUR*$_2$ arises as a combination of two structures: the approximation lattice $A_4$ and the logical lattice $L_4$ which are discussed in Belnap 1977a and 1977b (see also, Anderson, Belnap and Dunn 1992: 510–518)[^anderson-1992]).

### 3.2 Truth values as structured entities. Generalized truth values

Frege (1892: 30)[^frege-1892] points out the possibility of “distinctions of parts within truth values”. Although he immediately specifies that the word ‘part’ is used here “in a special sense”, the basic idea seems nevertheless to be that truth values are not something amorphous, but possess some inner structure. It is not quite clear how serious Frege is about this view, but it seems to suggest that truth values may well be interpreted as complex, structured entities that can be divided into parts.

There exist several approaches to semantic constructions where truth values are represented as being made up from some primitive components. For example, in some explications of Kripke models for intuitionistic logic propositions (identified with sets of “worlds” in a model structure) can be understood as truth values of a certain kind. Then the empty proposition is interpreted as the value *false*, and the maximal proposition (the set of all worlds in a structure) as the value *true*. Moreover, one can consider non-empty subsets of the maximal proposition as intermediate truth values. Clearly, the intuitionistic truth values so conceived are composed from some simpler elements and as such they turn out to be complex entities.

Another prominent example of structured truth values are the “truth-value objects” in topos models from category theory (see the entry on category theory). For any topos $C$ and for a $C$-object Ω one can define a truth value of $C$ as an arrow $1 \rightarrow \Omega$ (“a subobject classifier for $C$”), where 1 is a terminal object in $C$ (cf. Goldblatt 2006: 81, 94)[^goldblatt-2006]. The set of truth values so defined plays a special role in the logical structure of $C$, since arrows of the form $1 \rightarrow \Omega$ determine central semantical notions for the given topos. And again, these truth values evidently have some inner structure.

One can also mention in this respect the so-called “factor semantics” for many-valued logic, where truth values are defined as ordered $n$-tuples of classical truth values $(T$-$F$ sequences, see Karpenko 1983)[^karpenko-1983]. Then the value $3/5$, for example, can be interpreted as a $T$-$F$ sequence of length 5 with exactly 3 occurrences of $T$. Here the classical values $T$ and $F$ are used as “building blocks” for non-classical truth values.

Moreover, the idea of truth values as compound entities nicely conforms with the modeling of truth values considered above in three-valued (Kleene, Priest) and four-valued (Belnap) logics as certain subsets of the set of classical truth values. The latter approach stems essentially from Dunn (1976)[^dunn-1976], where a generalization of the notion of a classical truth-value function has been proposed to obtain so-called “underdetermined” and “overdetermined” valuations. Namely, Dunn considers a valuation to be a function not from sentences to elements of the set $\{T, F\}$ but from sentences to subsets of this set (see also Dunn 2000: 7)[^dunn-2000]. By developing this idea, one arrives at the concept of a *generalized truth value function*, which is a function from sentences into the *subsets* of some *basic set of truth values* (see Shramko and Wansing 2005)[^shramko-2005]. The values of generalized truth value functions can be called *generalized truth values*.

By employing the idea of generalized truth value functions, one can obtain a hierarchy of valuation systems starting with a certain set-theoretic representation of the valuation system for classical logic. The representation in question is built on a single initial value which serves then as the designated value of the resulting valuation system. More specifically, consider the singleton $\{\varnothing \}$ taken as the basic set subject to a further generalization procedure. Set-theoretically the basic set can serve as the universal set (the complement of the empty set) for the valuation system $\mathbf{V}^{\varnothing}_{cl}$ introduced below. At the first stage $\varnothing$ comes out with no specific intuitive interpretation, it is only important to take it as some distinct *unit*. Consider then the power-set of $\{\varnothing \}$ consisting of exactly two elements: $\{\{\varnothing \}, \varnothing \}$. Now, these elements can be interpreted as Frege’s *the True* and *the False*, and thus it is possible to construct a valuation system for classical logic, $\mathbf{V}^{\varnothing}_{cl} = \langle \{\{\varnothing \}, \varnothing \}, \{\{\varnothing \}\}, \{f_{\wedge}, f_{\vee}, f_{\rightarrow}, f_{\sim}\}\rangle$, where the functions $f_{\wedge}, f_{\vee}, f_{\rightarrow}, f_{\sim}$ are defined as follows (for $$ \begin{align} X, Y \in \{\{\varnothing \}, \varnothing \}:\quad & f_{\wedge}(X, Y) = X\cap Y; \\ & f_{\vee}(X, Y) = X\cup Y; \\ & f_{\rightarrow}(X, Y) = X^{c}\cup Y; \\ & f_{\sim}(X) = X^{c}. \end{align} $$ It is not difficult to see that for any assignment $a$ relative to $\mathbf{V}^{\varnothing}_{cl}$, and for any formulas $A$ and $B$, the following holds:

$$\begin{align} v_a (A\wedge B) = \{\varnothing \}&\Leftrightarrow v_a (A) = \{\varnothing \} \text{ and } v_a (B) = \{\varnothing \}; \\ v_a (A\vee B) = \{\varnothing \}&\Leftrightarrow v_a (A) = \{\varnothing \} \text{ or } v_a (B) = \{\varnothing \}; \\ v_a (A\rightarrow B) = \{\varnothing \}&\Leftrightarrow v_a (A) = \varnothing \text{ or } v_a (B) = \{\varnothing \}; \\ v_a (\sim A) = \{\varnothing \}&\Leftrightarrow v_a (A) = \varnothing. \end{align}$$

This shows that $f_{\wedge}, f_{\vee}, f_{\rightarrow}$ and $f_{\sim}$ determine exactly the propositional connectives of classical logic. One can conveniently mark the elements $\{\varnothing \}$ and $\varnothing$ in the valuation system $\mathbf{V}^{\varnothing}_{cl}$ by the classical labels $T$ and $F$. Note that within $\mathbf{V}^{\varnothing}_{cl}$ it is fully justifiable to associate $\varnothing$ with falsity, taking into account the virtual *monism of truth* characteristic for classical logic, which treats falsity not as an independent entity but merely as the absence of truth.

Then, by taking the set $\mathbf{2} = \{F, T\}$ of these classical values as the basic set for the next valuation system, one obtains the four truth values of Belnap’s logic as the power-set of the set of classical values $\mathcal{P}(\mathbf{2}) = \mathbf{4}: \mathbf{N} = \varnothing$, $\mathbf{F} = \{F\} (= \{\varnothing \})$, $\mathbf{T} = \{T\} (= \{\{\varnothing \}\})$ and $\mathbf{B} = \{F, T\} (= \{\varnothing, \{\varnothing \}\})$. In this way, Belnap’s four-valued logic emerges as a certain generalization of classical logic with its two Fregean truth values. In Belnap’s logic truth and falsity are considered to be full-fledged, self-sufficient entities, and therefore $\varnothing$ is now to be interpreted not as falsity, but as a real truth-value gap (*neither* true *nor* false). The dissimilarity of Belnap’s truth and falsity from their classical analogues is naturally expressed by passing from the corresponding classical values to their singleton-sets, indicating thus their new interpretations as *false only* and *true only*. Belnap’s interpretation of the four truth values has been critically discussed in (Lewis 1982)[^lewis-1982] and (Dubois 2008)[^dubois-2008] (see also the reply to Dubois in Wansing and Belnap 2010)[^wansing-2010][^wansing-2010-2].

Generalized truth values have a strong intuitive background, especially as a tool for the rational explication of incomplete and inconsistent information states. In particular, Belnap’s heuristic interpretation of truth values as information that “has been told to a computer” (see Belnap 1977a,b; also reproduced in Anderson, Belnap and Dunn 1992, §81)[^anderson-1992][^belnap-1977a] has been widely acknowledged. As Belnap points out, a computer may receive data from *various* (maybe independent) sources. Belnap’s computers have to take into account various kinds of information concerning a given sentence. Besides the standard (classical) cases, when a computer obtains information either that the sentence is (1) true or that it is (2) false, two other (non-standard) situations are possible: (3) nothing is told about the sentence or (4) the sources supply inconsistent information, information that the sentence is true and information that it is false. And the four truth values from $\mathbf{B}_4$ naturally correspond to these four situations: there is no information that the sentence is false and no information that it is true $(\mathbf{N})$, there is *merely* information that the sentence is false $(\mathbf{F})$, there is *merely* information that the sentence is true $(\mathbf{T})$, and there is information that the sentence is false, but there is also information that it is true $(\mathbf{B})$.

Joseph Camp in (2002: 125–160) provides Belnap’s four values with quite a different intuitive motivation by developing what he calls a “semantics of confused thought”. Consider a rational agent, who happens to mix up two very similar objects (say, $a$ and $b)$ and ambiguously uses one name (say, ‘$C$’) for both of them. Now let such an agent assert some statement, saying, for instance, that $C$ has some property. How should one evaluate this statement if $a$ has the property in question whereas $b$ lacks it? Camp argues against ascribing truth values to such statements and puts forward an “epistemic semantics” in terms of “profitability” and “costliness” as suitable characterizations of sentences. A sentence $S$ is said to be “profitable” if one would profit from acting on the belief that $S$, and it is said to be “costly” if acting on the belief that $S$ would generate costs, for example as measured by failure to achieve an intended goal. If our “confused agent” asks some external observers whether $C$ has the discussed property, the following four answers are possible: ‘yes’ (mark the corresponding sentence with $\mathbf{Y})$, ‘no’ (mark it with $\mathbf{N})$, ‘cannot say’ (mark it with **?**), ‘yes’ and ‘no’ (mark it with **Y&N**). Note that the external observers, who provide answers, are “non-confused” and have different objects in mind as to the referent of ‘$C$’, in view of all the facts that may be relevant here. Camp conceives these four possible answers concerning epistemic properties of sentences as a kind of “semantic values”, interpreting them as follows: the value $\mathbf{Y}$ is an indicator of profitability, the value $\mathbf{N}$ is an indicator of costliness, the value **?** is no indicator either way, and the value **Y&N** is both an indicator of profitability and an indicator of costliness. A strict analogy between this “semantics of confused reasoning” and Belnap’s four valued logic is straightforward. And indeed, as Camp (2002: 157)[^camp-2002] observes, the set of implications valid according to his semantics is exactly the set of implications of the entailment system $E_{fde}$. In (Zaitsev and Shramko 2013)[^zaitsev-2013] it is demonstrated how ontological and epistemic aspects of truth values can be combined within a joint semantical framework. Kapsner (2019)[^kapsner-2019] extends Belnap’s framework by two additional values “Contestedly-True” and “Contestedly-False” which allows for new outcomes for disjunctions and conjunctions between statements with values $\mathbf{B}$ and $\mathbf{N}$.

The conception of generalized truth values has its purely logical import as well. If one continues the construction and applies the idea of generalized truth value functions to Belnap’s four truth values, then one obtains further valuation systems which can be represented by various *multilattices*. One arrives, in particular, at *SIXTEEN*$_3$ – the *trilattice* of 16 truth-values, which can be viewed as a basis for a logic of computer networks (see Shramko and Wansing 2005, 2006; Kamide and Wansing 2009; Odintsov 2009; Wansing 2010; Odintsov and Wansing 2015; cf. also Shramko, Dunn, Takenaka 2001)[^dunn-2001][^kamide-2009][^odintsov-2009][^odintsov-2015][^shramko-2001][^shramko-2005][^shramko-2006][^wansing-2010][^wansing-2010-2]. The notion of a multilattice and *SIXTEEN*$_3$ are discussed further in the supplementary document [Generalized truth values and multilattices](truth-values.generalized-truth-values.md). A comprehensive study of the conception of generalized logical values can be found in (Shramko and Wansing 2011)[^shramko-2011].

## 4. Concluding remarks

Gottlob Frege’s notion of a truth value has become part of the standard philosophical and logical terminology. The notion of a truth value is an indispensable instrument of realistic, model-theoretic approaches to semantics. Indeed, truth values play an essential role in applications of model-theoretic semantics in areas such as, for example, knowledge representation and theorem proving based on semantic tableaux, which could not be treated in the present entry. Moreover, considerations on truth values give rise to deep ontological questions concerning their own nature, the feasibility of fact ontologies, and the role of truth values in such ontological theories. There also exist well-motivated theories of generalized truth values that lead far beyond Frege’s classical values *the True* and *the False*. (For various directions of further logical and philosophical investigations in the area of truth values see Shramko & Wansing 2009b, 2009c.)[^shramko-2009b][^shramko-2009c]

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=truth-values). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/truth-values/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=truth-values&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/truth-values/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- Roy, Sayantan, Roy, Sankha S. Basu, and Mihir K. Chakraborty, 2024, “[Suszko’s Thesis and Many-valued Logical Structures](https://arxiv.org/abs/2408.13769)”, manuscript at arxiv.org.

## Related Entries

abstract objects | Boolean algebra: the mathematics of | Church, Alonzo | facts | Frege, Gottlob | logic: classical | logic: fuzzy | logic: many-valued | Sorites paradox | truth: deflationism about | vagueness

### Acknowledgments

We'd like to thank an anonymous reviewer for comments about the material in Section 1.2, which led to an improved discussion.

## Notes（原文脚注）

[^note-1]: One should also note that there exist alternatives to truth-conditional semantics, such as algebraic, game-theoretic, and proof-theoretic semantics. According to the latter approach, “the central notion in terms of which meanings are assigned to certain expressions of our language, in particular to logical constants, is that of proof rather than truth. In this sense proof-theoretic semantics is semantics in terms of proof” (see the entry on proof-theoretic semantics).

The case of proof-theoretic semantics shows that the notions of truth and falsity that are central to denotational semantics as a methodology for assigning meaning to sentences are not indispensable for developing an account of linguistic meaning. For some approaches to meaning without truth values, or even without truth at all, see e.g., Pietroski 2018 and Predelli 2013.

[^anderson-1975]: Anderson, Alan R. and Nuel D. Belnap, 1975, *Entailment: The Logic of Relevance and Necessity* (Volume I), Princeton, NJ: Princeton University Press.

[^anderson-1992]: Anderson, Alan R., Nuel D. Belnap, and J. Michael Dunn, 1992, *Entailment: The Logic of Relevance and Necessity*, Vol. II, Princeton, NJ: Princeton University Press.

[^anderson-2004]: Anderson, David and Edward Zalta, 2004, “Frege, Boolos, and logical objects”, *Journal of Philosophical Logic*, 33: 1–26.

[^arieli-1996]: Arieli, Ofer and Arnon Avron, 1996, “Reasoning with logical bilattices”, *Journal of Logic, Language and Information*, 5: 25–63.

[^asenjo-1966]: Asenjo, Florencio G., 1966, “A calculus of antinomies”, *Notre Dame Journal of Formal Logic*, 7: 103–105.

[^avron-2005]: Avron, Arnon and Beata Konikowska, 2005, “Multi-valued calculi for logics based on non-determinism”, *Logic Journal of the IGPL*} 13: 365–387.

[^avron-2005-2]: Avron, Arnon and Iddo Lev, 2005, “Non-deterministic multi-valued structures”, *Journal of Logic and Computation*, 15: 241–261.

[^avron-2010]: Avron, Arnon and Anna Zamansky, 2010, “Non-deterministic semantics for logical systems”, *Handbook of Philosophical Logic* (Volume 16), Dordrecht: Springer, 227–304.

[^bar-hillel-1973]: Bar-Hillel, Yehoshua, 1973, “Primary truth bearers”, *Dialectica*, 27: 303–312.

[^barrio-2015]: Barrio, Eduardo, Lucas, Rosenblatt, and Diego Tajer, 2015, “The logics of strict-tolerant logic”, *Journal of Philosophical Logic*, 44: 551–571.

[^barrio-2020]: Barrio, Eduardo, Federico, Pailos, and Damian Szmuc, 2020, “A hierarchy of classical and paraconsistent logics”, *Journal of Philosophical Logic*, 49: 93–120.

[^barwise-1981]: Barwise, Jon and John Perry, 1981, “Semantic innocence and uncompromising situations”, *Midwest Studies in the Philosophy of Language*, VI: 387–403.

[^beall-2020]: Beall, Jc and Caleb Camrud, 2020, “A note on FDE ‘All the way up’,”, *Notre Dame Journal of Formal Logic*, 61: 283–296.

[^beaney-1997]: Beaney, Michael (ed. and transl.), 1997, *The Frege Reader*, Oxford: Wiley-Blackwell.

[^belnap-1977a]: Belnap, Nuel D., 1977a, “How a computer should think”, in G. Ryle (ed.), *Contemporary Aspects of Philosophy*, Stocksfield: Oriel Press Ltd., 30–55.

[^belnap-1977b]: –––, 1977b, “A useful four-valued logic”, in J.M. Dunn and G. Epstein (eds.), *Modern Uses of Multiple-Valued Logic*, Dordrecht: D. Reidel Publishing Co., 8–37.

[^belnap-2009]: –––, 2009, “Truth values, neither-true-nor-false, and supervaluations”, *Studia Logica*, 91: 305–334.

[^belnap-nd]: –––, forthcoming, “How case-intensional semantics prevents the Slingshot from hitting its target”, *Studia Logica*.

[^bennett-1988]: Bennett, Jonathan, 1988, *Events and their Names*. New York: Hackett.

[^béziau-2012]: Béziau, Jean-Yves, 2012, “A History of Truth-Values”, in D. Gabbay et al. (eds.), *Handbook of the History of Logic.* Vol. 11*, Logic: A History of its Central Concepts*, Amsterdam: North-Holland, 235–307.

[^blasio-2017]: Blasio, Carolina, João, Marcos, and Heinrich Wansing, 2017, “An inferentially many-valued two-dimensional notion of entailment”, *Bulletin of the Section of Logic*, 46: 233–262.

[^brown-1999]: Brown, Bryson and Peter Schotch, 1999, “Logic and aggregation”, *Journal of Philosophical Logic*, 28: 265–287.

[^bressan-1972]: Bressan, Aldo, 1972, *A General Interpreted Modal Calculus*, New Haven: Yale University Press.

[^burge-1986]: Burge, Tyler, 1986, “Frege on truth”, in L. Haaparanta and J. Hintikka (eds.), *Frege Synthesized*, Dordrecht: D. Reidel Publishing Co., 97–154.

[^burge-1992]: –––, 1992, “Frege on knowing the Third Realm”, *Mind*, 101: 633–650.

[^caleiro-2005]: Caleiro, Carlos, Walter Carnielli, Marcelo Coniglio, and João Marcos, 2005, “Two’s company: ‘The humbug of many logical values’”, in J.-Y. Béziau (ed.), *Logica Universalis*, Basel: Birkhäuser Verlag, 169–189.

[^camp-2002]: Camp, Joseph L., 2002, *Confusion: A Study in the Theory of Knowledge*, Cambridge, MA: Harvard University Press.

[^carnap-1942]: Carnap, Rudolf, 1942, *Introduction to Semantics*, Cambridge, MA: Harvard University Press.

[^carnap-1947]: –––, 1947, *Meaning and Necessity. A Study in Semantics and Modal Logic*, Chicago: University of Chicago Press.

[^chemla-2019]: Chemla, Emmanuel and Paul Égré, 2019, “Suszko’s problem: Mixed consequence and compositionality”, *Review of Symbolic Logic*, 12: 736–767.

[^church-1943]: Church, Alonzo, 1943, “Review of Rudolf Carnap, *Introduction to Semantics*”, *The Philosophical Review*, 52: 298–304.

[^church-1956]: –––, 1956, *Introduction to Mathematical Logic*, Vol. I, Princeton: Princeton University Press.

[^cignoli-2000]: Cignoli, Roberto, Itala D’Ottaviano, and Daniele Mundici, 2000, *Algebraic Foundations of Many-valued Reasoning*, Dordrecht: Kluwer Academic Publishers.

[^cobreros-2012]: Cobreros, Pablo, Paul Égré, David, Ripley, and Robert van Rooij, 2012, “Tolerant, classical, strict”, *Journal of Philosophical Logic*, 41: 347–385

[^coniglio-2020]: Coniglio, Marcelo, Luis Farias del Cerro, and Newton M. Peron, 2020, “Modal logic with non-deterministic semantics: Part I—Propositional case”, *Logic Journal of the IGP*L, 28: 281–315.

[^costa-1996]: da Costa, Newton, Jean-Yves Béziau, and Otávio Bueno, 1996, “Malinowski and Suszko on many-valued logics: on the reduction of many-valuedness to two-valuedness”, *Modern Logic*, 6: 272–299.

[^czelakowski-2001]: Czelakowski, Janusz, 2001, *Protoalgebraic Logics*, Dordrecht: Kluwer Academic Publishers.

[^cohen-2025]: Cohen, S. Marc and C. D. C. Reeve, 2025, “Aristotle’s Metaphysics”, *The Stanford Encyclopedia of Philosophy* (Spring 2025 Edition), Edward N. Zalta & Uri Nodelman (eds.), URL = <[https://plato.stanford.edu/archives/spr2025/entries/aristotle-metaphysics/](https://plato.stanford.edu/archives/spr2025/entries/aristotle-metaphysics/)>.

[^davidson-1967]: Davidson, David, 1967, “Truth and meaning”, *Synthese*, 17: 304–323.

[^davidson-1969]: –––, 1969, “True to the facts”, *Journal of Philosophy*, 66: 748–764.

[^deutsch-1984]: Deutsch, Harry, 1984, “Paraconsistent analytic implication”, *Journal of Philosophical Logic*, 13: 1–11.

[^dubois-2008]: Dubois, Didier, 2008, “On ignorance and contradiction considered as truth-values”, *Logic Journal of the IGPL*, 16: 195–216.

[^dummett-1959]: Dummett, Michael, 1959, “Truth”, in *Proceedings of the Aristotelian Society*, 59: 141–162 (Reprinted in *Truth and Other Enigmas*, Cambridge, MA: Harvard University Press, 1978, 1–24).

[^dummett-1981]: –––, 1981, *Frege: Philosophy of Language*, 2ⁿᵈ edition, London: Duckworth Publishers.

[^dummett-1991]: –––, 1991, *Frege and Other Philosophers*, Oxford: Oxford University Press.

[^dummett-2000]: –––, 2000, *Elements of Intuitionism*, 2ⁿᵈ ed., Oxford: Clarendon Press.

[^dunn-1976]: Dunn, J. Michael, 1976, “Intuitive semantics for first-degree entailment and ‘coupled trees’”, *Philosophical Studies*, 29: 149–168.

[^dunn-2000]: –––, 2000, “Partiality and its dual”, *Studia Logica*, 66: 5–40.

[^dunn-2001]: Dunn, J. Michael and Gary M. Hardegree, 2001, *Algebraic Methods in Philosophical Logic* (Oxford Logic Guides, Volume 41), Oxford: Science Publications.

[^ferguson-2017]: Ferguson, Thomas Macaulay, 2017, *Meaning and Proscription in Formal Logic. Variations on the Propositional Logic of William T. Parry* (Trends in Logic: Volume 49), Berlin: Springer, 2017.

[^fine-1975]: Fine, Kit, 1975, “Vagueness, truth and logic”, *Synthese*, 30: 265–300.

[^fitting-2006]: Fitting, Melvin, 2006, “Bilattices are nice things”, in T. Bolander, V. Hendricks, and S.A. Pedersen (eds.), *Self-Reference*, Stanford: CSLI Publications, 53–77.

[^font-1997]: Font, Josep Maria, 1997, “Belnap’s four-valued logic and De Morgan lattices”, *Logic Journal of IGPL*, 5: 1–29.

[^font-2009]: –––, 2009, “Taking degrees of truth seriously”, *Studia Logica*, 91: 383–406.

[^fraassen-1966]: van Fraassen, Bas, 1966, “Singular terms, truth-value gaps, and free logic”, *Journal of Philosophy*, 63: 481–495.

[^frankowski-2004]: Frankowski, Szymon, 2004, “Formalization of a plausible inference”, *Bulletin of the Section of Logic*, 33: 41–52.

[^frege-1884]: Frege, Gottlob, 1884, *Grundlagen der Arithmetik. Eine logisch-mathematische Untersuchung über den Begriff der Zahl*, Hamburg: Felix Meiner Verlag, 1988.

[^frege-1891]: –––, 1891, “Function und Begriff. Vortrag, gehalten in der Sitzung vom 9. Januar 1891 der Jenaischen Gesellschaft für Medicin und Naturwissenschaft”, Jena: H. Pohle (Reprinted in Frege 1986.)

[^frege-1892]: –––, 1892, “Über Sinn und Bedeutung”, *Zeitschrift für Philosophie und philosophische Kritik*, 100: 25–50. (Reprinted in Frege 1986.)

[^frege-1893]: –––, 1893/1903, *Grundgesetze der Arithmetik*, 2 volumes, Jena: Verlag Hermann Pohle; reprinted, Darmstadt: Wissenschaftliche Buchgesellschaft, 1962.

[^frege-1918]: –––, 1918, “Der Gedanke”, *Beiträge zur Philosophie des deutschen Idealismus* 1: 58–77. (Reprinted in Frege 1967.)

[^frege-1967]: –––, 1967, *Kleine Schriften*, Ignacio Angelli (ed.), Darmstadt: Wissenschaftliche Buchgesellschaft.

[^frege-1976]: –––, 1976, *Wissenschaftlicher Briefwechsel*, G. Gabriel, H. Hermes, F. Kambartel, C. Thiel, and A. Veraart (eds.), Hamburg: Felix Meiner Verlag.

[^frege-1986]: –––, 1986, *Funktion, Begriff, Bedeutung. Fünf logische Studien*, G. Patzig (ed.), Göttingen: Vandenhoeck & Ruprecht.

[^frege-1990]: –––, 1990, “Einleitung in die Logik”, in Frege, G., *Schriften zur Logik und Sprachphilosophie*, Hamburg: Felix Meiner Verlag, 74–91.

[^gabriel-1984]: Gabriel, Gottfried, 1984, “Fregean connection: Bedeutung, value and truth-value”, *The Philosophical Quarterly*, 34: 372–376.

[^gabriel-1986]: –––, 1986, “Frege als Neukantianer”, *Kant-Studien*, 77: 84–101.

[^gabriel-2013]: –––, 2013, “Truth, value, and truth value. Frege’s theory of judgement and its historical background”, in M. Textor (ed.), *Judgement and Truth in Early Analytic Philosophy and Phenomenology*, Basingstoke: Palgrave Macmillan, 36–51.

[^galatos-2007]: Galatos, Nikolaos, Peter Jipsen, Tomasz Kowalski and Hiroakira Ono, 2007, *Residuated Lattices: An Algebraic Glimpse at Substructural Logics*, Amsterdam: Elsevier.

[^geach-1952]: Geach, Peter and Max Black (eds.), 1952, *Translations from the Philosophical Writings of Gottlob Frege*, New York: Philosophical Library.

[^ginsberg-1988]: Ginsberg, Matthew, 1988, “Multivalued logics: a uniform approach to reasoning in AI”, *Computer Intelligence*, 4: 256–316.

[^gödel-1944]: Gödel, Kurt, 1944, “Russell’s mathematical logic”, in P.A. Schilpp (ed.), *The Philosophy of Bertrand Russell*, Evanston and Chicago: Northwestern University Press, 125–53.

[^goldblatt-2006]: Goldblatt, Robert, 2006, *Topoi: The Categorial Analysis of Logic*, Mineola, NY: Dover Publications.

[^gottwald-1989]: Gottwald, Siegfried, 1989, *Mehrwertige Logik. Eine Einführung in Theorie und Anwendungen*, Berlin: Akademie-Verlag.

[^gottwald-2001]: –––, 2001, *A Treatise on Many-valued Logic*, Baldock: Research Studies Press.

[^goguen-1969]: Goguen, Joseph, 1969, “The logic of inexact concepts”, *Synthese*, 19: 325–373.

[^grossmann-1992]: Grossmann, Reinhardt, 1992, *The Existence of the World*, London: Routledge.

[^haack-1996]: Haack, Susan, 1996, *Deviant Logic, Fuzzy Logic. Beyond the Formalism*, Chicago: University of Chicago Press.

[^hajek-1998]: Hajek, Petr, 1998, *Metamathematics of fuzzy logic*, Dordrecht: Kluwer Academic Publishers.

[^hanks-2013]: Hanks, Peter, 2013, “What are the primary bearers of truth?”, *Canadian Journal of Philosophy*, 43: 558–574.

[^humberstone-2023]: Humberstone, Lloyd, 2023, “Truth-value relations and logical relations”, *Theoria*, 89: 124–147.

[^ivlev-1988]: Ivlev, Yuri. V., 1988, “A semantics for modal calculi”, *Bulletin of the Section of Logic*, 17: 114–121.

[^jennings-1984]: Jennings, Ray and Peter Schotch, 1984, “The preservation of coherence”, *Studia Logica*, 43: 89–106.

[^kamide-2009]: Kamide, Norihiro and Heinrich Wansing, 2009, “Sequent calculi for some trilattice logics”, *Review of Symbolic Logic*, 2: 374–395.

[^kapsner-2019]: Kapsner, Andreas, 2019, “Removing the oddity in first degree entailment”, *Thought. A Journal of Philosophy*, 48: 240–249.

[^karpenko-1983]: Karpenko, Alexander, 1983, “Factor semantics for $n$-valued logics”, *Studia Logica*, 42: 179–185.

[^kearns-1981]: Kearns, John T., 1981, “Modal semantics without possible worlds”, *Journal of Symbolic Logic*, 46: 77–86.

[^keefe-2000]: Keefe, Rosanna, 2000, *Theories of Vagueness*, Cambridge: Cambridge University Press.

[^kneale-1962]: Kneale, William and Martha Kneale, 1962, *The Development of Logic*, Oxford: Oxford University Press.

[^lewis-1943]: Lewis, Clarence Irving, 1943, “The modes of meaning”, *Philosophy and Phenomenological Research*, 4: 236–249.

[^lewis-1982]: Lewis, David, 1982, “Logic for equivocators”, Noûs, 16: 431–441.

[^lowe-1995]: Lowe, Jonathan, 1995, “The metaphysics of abstract objects”, *The Journal of Philosophy*, 92: 509–524.

[^lowe-1997]: –––, 1997, “Objects and criteria of identity”, in *A Companion to the Philosophy of Language*, R. Hale and C. Wright (eds.), Oxford: Basil Blackwell, 613–33.

[^jan-1918]: Łukasiewicz, Jan, 1918, “Farewell lecture by professor Jan Łukasiewicz,” delivered in the Warsaw University Lecture Hall in March, 1918, in Łukasiewicz 1970, 87–88.

[^jan-1920]: –––, 1920, “O logice trójwartościowej”, *Ruch Filozoficny*, 5: 170–171. (English translation as “On three-valued logic” in Łukasiewicz 1970, 87–88.)

[^jan-1921]: –––, 1921, “Logika dwuwartościowa”, *Przegl ad Filosoficzny*, 13: 189–205. (English translation as “Two-valued logic” in Łukasiewicz 1970, 89–109.)

[^jan-1970]: –––, 1970, *Selected Works*, L. Borkowski (ed.), Amsterdam: North-Holland, and Warsaw: PWN.

[^macfarlane-2002]: MacFarlane, John, 2002, “Review of Stephen Neale, *Facing Facts*”, *Notre Dame Philosophical Reviews*, [[MacFarlane 2002 available online](http://ndpr.nd.edu/review.cfm?id=1117)].

[^macfarlane-2008]: –––, 2008, “Truth in the garden of forking paths”, in *Relative Truth*, Max Kölbel and Manuel García-Carpintero (eds.), Oxford: Oxford University Press, 81–102.

[^malinowski-1990]: Malinowski, Grzegorz, 1990, “Q-consequence operation”, *Reports on Mathematical Logic*, 24: 49–59.

[^malinowski-1993]: –––, 1993, *Many-Valued Logics*, Oxford: Clarendon Press.

[^malinowski-1994]: –––, 1994, “Inferential many-valuedness”, in Jan Wolenski (ed.), *Philosophical Logic in Poland*, Dordrecht: Kluwer Academic Publishers, 75–84.

[^mehlberg-1958]: Mehlberg, Henryk, 1958, *The Reach of Science*, Toronto: University of Toronto Press.

[^meyer-1978]: Meyer, Robert K., 1978 *Why I Am Not a Relevantist*, Research Paper No. 1, Canberra: Australian National University (Logic Group, Research School of the Social Sciences).

[^neale-1995]: Neale, Stephen, 1995, “The Philosophical significance of Gödel’s slingshot”, *Mind*, 104: 761–825.

[^neale-2001]: –––, 2001, *Facing Facts*, Oxford: Oxford University Press.

[^odintsov-2009]: Odintsov, Sergei, 2009, “On axiomatizing Shramko-Wansing’s logic”, *Studia Logica*, 93: 407–428. doi:10.1007/s11225-009-9181-6

[^odintsov-2015]: Odintsov, Sergei and Heinrich Wansing, 2015, “The logic of generalized truth values and the logic of bilattices”, *Studia Logica*, 103(1): 91–112. doi:10.1007/s11225-014-9546-3

[^oller-1999]: Oller, Carlos, 1999, “Paraconsistency and analyticity”, *Logic and Logical Philosophy*, 7: 91–99.

[^omori-2016]: Omori, Hitoshi and Daniel Skurt, 2016, “More modal semantics without possible worlds”, *IfCoLog Journal of Logics and their Applications*, 3: 815–845.

[^omori-2019]: –––, 2019, “*SIXTEEN*$_3$ in light of Routley stars”, in R. Iemhoff, R. Moortgat, and R. de Queiroz R. (eds), *Logic, Language, Information, and Computation*. WoLLIC 2019 (Lecture Notes in Computer Science: Volume 11541), Berlin: Springer, 516–532.

[^omori-2020]: –––, 2020, “A semantics for a failed axiomatization of K”, in N. Olivetti, R. Verbrugge, S. Negri, and G. Sandu (eds.), *Advances in Modal Logicx* (Volume 13), London: College Publications, 481–501.

[^omori-2021]: –––, 2021, “Untruth, falsity and non-deterministic semantics”, *IEEE 51st International Symposium on Multiple-Valued Logic* (ISMVL), Nur-sultan, Kazakhstan, 74–180.

[^omori-2017]: Omori, Hitoshi and Heinrich Wansing, 2017, “40 years of FDE: and introductory overview”, *Studia Logica*, 105: 1021–1049.

[^oppy-1997]: Oppy, Graham, 1997, “The Philosophical Insignificance of Gödel’s Slingshot”, *Mind*, 106(421): 121–141.

[^owen-1960]: Owen, G. E. L., 1960, “Logic and metaphysics in some earlier works of Aristotle”, in Düring, I. and G. E. L. Owen (eds.) *Aristotle and Plato in the Mid-Fourth Century*, Göteborg: Elanders Boktryckeri Aktiebolag, 163–190.

[^pawlowski-2024]: Pawlowski, Pawel and Daniel Skurt, 2024, “8 Valued Non-Deterministic Semantics for Modal Logics”*, Journal of Philosophical Logic*, 53: 351–71.

[^peirce-1885]: Peirce, C.S., 1885, “On the Algebra of Logic: A Contribution to the Philosophy of Notation”, *American Journal of Mathematics*, 7(2): 180–202. doi:10.2307/2369451

[^perry-1996]: Perry, John, 1996, “Evading the slingshot”, in A. Clark, J. Ezquerro, and J. Larrazabal (eds.), *Philosophy and Cognitive Science. Categories, Consciousness, and Reasoning*, Dordrecht: Kluwer Academic Publishers, 95–114.

[^pietroski-2018]: Pietroski, Paul M., 2018, *Conjoining Meanings. Semantics Without Truth Values*, Oxford: Oxford University Press.

[^predelli-2013]: Predelli, Stefano, 2013, *Meaning without Truth*, Oxford: Oxford University Press.

[^popper-1972]: Popper, Karl, 1972, *Objective Knowledge: An Evolutionary Approach*, Oxford: Oxford University Press.

[^post-1921]: Post, Emil, 1921, “Introduction to a general theory of elementary propositions”, *American Journal of Mathematics*, 43: 163–185.

[^priest-1979]: Priest, Graham, 1979, “Logic of Paradox”, *Journal of Philosophical Logic*, 8: 219–241.

[^quine-1953]: Quine, Willard Van Orman, 1953, “Reference and modality”, in W.v.O. Quine, *From a Logical Point of View*, Cambridge, MA: Harvard University Press, 139–159.

[^quine-1960]: –––, 1960, *Word and Object*, Cambridge, MA: MIT Press.

[^quine-1969]: –––, 1969, *Ontological Relativity and Other Essays*, New York: Columbia University Press.

[^reck-2007]: Reck, Erich, 2007, “Frege on truth, judgment, and objectivity”, *Grazer Philosophische Studien*, 75: 149–173.

[^rescher-1969]: Rescher, Nicholas, 1969, *Many-Valued Logic*, New York: McGraw-Hill.

[^routley-1975]: Routley, Richard, 1975, “Universal semantics?”, *The Journal of Philosophical Logic*, 4: 327–356.

[^ruffino-2003]: Ruffino, Marco, 2003, “Wahrheit als Wert und als Gegenstand in der Logik Freges”, in D. Greimann (ed.), *Das Wahre und das Falsche. Studien zu Freges Auffassung von Wahrheit*, Hildesheim: Georg Olms Verlag, 203–221.

[^russell-1918]: Russell, Bertrand, 1918, 1919 [1992], “The philosophy of logical atomism”, *Monist*, 28: 495–527; 29: 32–63, 190–222, 345–380. reprinted in his *Logic and Knowledge*, London: Allen and Unwin, 1956. Page numbers from the Routlege edition, 1992, 175–282.

[^ryan-1992]: Ryan, Mark and Martin Sadler, 1992, “Valuation systems and consequence relations”, in S. Abramsky, D. Gabbay, and T. Maibaum (eds.), *Handbook of Logic in Computer Science*, Vol. 1., Oxford: Oxford University Press, 1–78.

[^searle-1995]: Searle, John, 1995, “Truth: A Reconsideration of Strawson’s View”, in L.E. Hahn (ed.), *The Philosophy of P.F. Strawson*, Chicago: Open Court.

[^sefrin-weis-2009]: Sefrin-Weis, Heike, 2009, “Colloquium 8: *Pros Hen* and the Foundations of Aristotelian Metaphysics”, *Proceedings of the Boston Area Colloquium in Ancient Philosophy*, 24(1): 261–300.

[^shramko-2014]: Shramko, Yaroslav, 2014, “The logical way of being true: Truth values and the ontological foundation of logic”, *Logic and Logical Philosophy*.

[^shramko-2016]: –––, 2016, “Truth, falsehood, information and beyond: the American Plan generalized”, in Katalin Bimbó (ed.), *J. Michael Dunn on Information Based Logics* (Outstanding Contributions to Logic: Volume 8), Berlin: Springer, 191–212.

[^shramko-2001]: Shramko, Yaroslav, J. Michael Dunn, and Tatsutoshi Takenaka, 2001, “The trilaticce of constructive truth values”, *Journal of Logic and Computation*, 11: 761–788.

[^shramko-2005]: Shramko, Yaroslav and Heinrich Wansing, 2005, “Some useful 16-valued logics: how a computer network should think”, *Journal of Philosophical Logic*, 34: 121–153.

[^shramko-2006]: –––, 2006, “Hypercontradictions, generalized truth values, and logics of truth and falsehood”, *Journal of Logic, Language and Information*, 15: 403–424.

[^shramko-2009a]: –––, 2009a, “The Slingshot-Argument and sentential identity”, *Studia Logica*, 91: 429–455.

[^shramko-2009b]: –––, 2009b, “Editorial Introduction. Truth Values: Part I”, in Shramko & Wansing (eds.) 2009a, 295–304. doi:10.1007/s11225-009-9176-3

[^shramko-2009c]: –––, 2009c, “Editorial Introduction. Truth Values: Part II”, in Shramko & Wansing (eds.) 2009b, 143–146. doi:10.1007/s11225-009-9191-4

[^shramko-2011]: –––, 2011, *Truth and Falsehood: An Inquiry into Generalized Logical Values*, Trends in Logic Vol. 36, Dordrecht, Heidelberg, London, New York: Springer.

[^shramko-2009a-2]: Shramko, Yaroslav and Heinrich Wansing (eds.), 2009a, *Truth Values* (Part I), Special issue of *Studia logica*, 91(3).

[^shramko-2009]: ––– (eds.), 2009, *Truth Values* (Part II), Special issue of *Studia logica*, 92(2).

[^sluga-2002]: Sluga, Hans, 2002, “Frege on the indefinability of truth”, in E. Reck (ed.), *From Frege to Wittgenstein: Perspectives on Early Analytic Philosophy*, Oxford: Oxford University Press, 75–95.

[^soames-1999]: Soames, Scott, 1999, *Understanding Truth*, Oxford, New York: Oxford University Press.

[^strollo-2023]: Strollo, Andrea, 2023, “Truth (bearers) pluralism”, *Synthese*, 201: 124. doi:10.1007/s11229-023-04081-x

[^stoutland-2003]: Stoutland, Frederick, 2003, “What philosophers should know about truth and the slingshot”, in Matti Sintonen, Petri Ylikoski, and Kaarlo Miller (eds.), *Realism in Action: Essays in the Philosophy of the Social Sciences*, Dordrecht: Kluwer Academic Publishers, 3–32. doi:10.1007/978-94-007-1046-7_1 (republished in: Fred Stoutland and Jeff Malpas, 2019, *What Philosophers Should Know About Truth*, Berlin, Boston: De Gruyter, pp. 1–34. doi:10.1515/9783110620788)

[^suszko-1977]: Suszko, Roman, 1977, “The Fregean axiom and Polish mathematical logic in the 1920s”, *Studia Logica*, 36: 373–380. doi:10.1007/BF02120672

[^tarski-1930a]: Tarski, Alfred, 1930a, “Über einige fundamentale Begriffe der Metamathematik”, *Comptes Rendus des Séances de la Société des Sciences et des Lettres de Varsovie* XXIII, Classe III: 22–29.

[^tarski-1930b]: –––, 1930b, “Fundamentale Begriffe der Methodologie der deduktiven Wissenschaften, I”, *Monatshefte für Mathematik und Physik*, 37: 361–404.

[^taylor-1985]: Taylor, Barry, 1985, *Modes of Occurrence: Verbs, Adverbs and Events*, Oxford: Blackwell.

[^urquhart-1986]: Urquhart, Alasdair, 1986, “Many-valued logic”, in D. Gabbay and F. Guenther (eds.), *Handbook of Philosophical Logic*, Vol. III., D. Reidel Publishing Co., Dordrecht, 71–116.

[^wansing-2010]: Wansing, Heinrich, 2010, “The power of Belnap. Sequent systems for *SIXTEEN*$_3$”, *Journal of Philosophical Logic*, 39(4): 369–393. doi:10.1007/s10992-010-9139-1

[^wansing-2010-2]: Wansing, Heinrich and Nuel Belnap, 2010, “Generalized truth values: A reply to Dubois”, *Logic Journal of the IGPL*, 18(6): 921–935. doi:10.1093/jigpal/jzp068

[^wansing-2008]: Wansing, Heinrich and Yaroslav Shramko, 2008, “Suszko’s Thesis, inferential many-valuedness, and the notion of a logical system”, *Studia Logica*, 88: 405–429, 89: 147.

[^williamson-1994]: Williamson, Timothy, 1994, *Vagueness*, London: Routledge.

[^windelband-1915]: Windelband, Wilhelm, 1915, *Präludien: Aufätze und Reden zur Philosophie und ihrer Geschichte*, 5. Aufgabe, Bnd. 1., Tübingen.

[^wójcicki-1970]: Wójcicki, Ryszard, 1970, “Some remarks on the consequence operation in sentential logics”, *Fundamenta Mathematicae*, 68: 269–279.

[^wójcicki-1988]: –––, 1988, *Theory of Logical Calculi. Basic Theory of Consequence Operations*, Dordrecht: Kluwer Academic Publishers.

[^wrigley-2006]: Wrigley, Anthony, 2006, “Abstracting propositions”, *Synthese*, 151: 157–176.

[^yu-2001]: Yu, Jiyuan, 2001, “What is the focal meaning of being in Aristotle?“, *Apeiron*, 34: 205–232.

[^zadeh-1965]: Zadeh, Lotfi, 1965, “Fuzzy sets”, *Information and Control*, 8: 338–53.

[^zadeh-1975]: –––, 1975, “Fuzzy logic and approximate reasoning”, *Synthese*, 30: 407–425.

[^zaitsev-2013]: Zaitsev, Dmitry and Yaroslav Shramko, 2013, “Bi-facial truth: a case for generalized truth values”, *Studia Logica*, 101: 1299–1318.

[^zalta-1983]: Zalta, Edward, 1983, *Abstract Objects: An Introduction to Axiomatic Metaphysics*, Dordrecht: D. Reidel Publishing Co.

[^zalta-2014]: –––, 2014, “The Tarski T-Schema is a tautology (literally)”, *Analysis*, 74: 5–11.
