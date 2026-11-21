# church — supplementE（supplement）

> （《church》词条补充材料，源：plato.stanford.edu/entries/church/supplementE.html）

#### Supplement to Alonzo Church

## E. Philosophy of Language

- E.1 Why Formal Semantics?
- E.2 Intensional Semantics
- E.3 The Logic of Sense and Denotation
- E.4 LSD and the Criteria of Identity for Concepts
- E.5 Russellian Philosophy of Language

### E.1 Why Formal Semantics?

As noted in the main text, Church’s (1943a) review of Carnap’s (1942) constitutes an important early step in the application of the logistic method to the subject of semantics, not least because of the succinct description of the goal of formal semantics (for similar remarks, see Church 1943c, 1951b, 1952, 1956a). According to this description, the discovery of syntax and semantics begins with observation of how informal language is used, rather like how the discovery of the basic notions of Euclidean geometry begins with observation of how magnitudes are compared and measured (cf. Church 1951b). However, syntax and semantics

> have an abstract character, like that of mathematics: they do not relate how in historical fact the language was used by so-and-so and so-and-so, but they propose a definition of what shall be considered the correct usage of the language, and base an abstract theory on this definition (1943a [BE: 259]).

This is a different theoretical treatment than that given to the “imprecise approximations” to norms that we find in “everyday linguistic behavior” (1951b [BE: 282]). Just as geometry idealizes away imprecisions in the comparison and measurement of magnitudes, a syntax and semantics for a language idealizes away ambiguities, vagaries and inconsistencies of actual use. When a syntax and semantics is provided for an informal (or natural) language like English, it is formulated by extrapolation from just those examples that are judged to be examples of *correct* use (1943c). If, instead, a syntax and semantics is provided for the *formalized counterpart* of English, then, while it should diverge only minimally from the syntax and semantics of English, the formulation of the syntax and semantics must be *as precise as possible*. In this respect, the distinction between English and its formalized counterpart is not entirely sharp (ibid). This puts Church at odds with Carnap (1942), who does draw a sharp distinction between English, which he claims has a descriptive semantics, and formalized languages for which the semantics is *stipulated*. For Church, a syntax and semantics for a given language, whether formal or informal, is a theory of *norms* of correct use for that language; and, in general, syntax and semantics for formal languages is a theory of the languages we *should* speak for the purposes of logical analysis, the discovery and dissolution of paradox, and (other) scientific thought. Church’s view, then, constitutes a more nuanced approach to logical theorizing about languages than the uniform attitude propounded by Montague: that there is “no important theoretical difference between natural languages and the artificial languages of logicians” (1970a: 373).

### E.2 Intensional Semantics

The influence of Frege on Church is evident in the particular semantic theory that Church favors. This theory postulates and assigns to each name a unique sense that in turn determines a unique *designatum*:

> the sense of an expression is in its linguistic meaning, the meaning which is known to any one familiar with the language and for which no knowledge of extralinguistic fact is required; the sense is what we have grasped when we are said to understand the expression. On the other hand the *designatum* of an expression often requires to be discovered by an empirical investigation or other considerations in addition to the knowledge of the language; it may well be possible to understand an expression yet not know its *designatum*. (1943a [BE: 261])

Church agrees with Frege that senses are objective—mind-and-language independent—abstract entities. (Church’s reasons for postulating and assigning entities of this nature to names are discussed in section 3 and section 6). He also agrees with Frege (1892a) that senses are recommended for their power to explain the informative nature of identity statements containing co-designating names, as well as to explain the failure of the substitutivity of co-designating names in intensional contexts (1943a; 1956a: §01).

For example, suppose that the sense of the proper name “Hesperus” is *the first planet visible in the evening*, while the sense of “Phosphorus” is *the last planet visible in the morning.* Because of the difference between these senses, “Hesperus is Phosphorus” expresses information about astronomy of which a competent speaker may be ignorant, while “Hesperus is Hesperus” does not. In the case of proper names of people, like “Sir Walter Scott”, Church claims that they express senses like *the person with the given name “Walter” and the surname “Scott”* (1956a: §01; but compare the remarks about “Capetown” in 1956a: fn. 136). While reflection on actual linguistic behavior reveals that *a speaker* can use “Hesperus” to convey more than one sense, the sense assigned by a semantic theory is “univocal” (ibid). This raises two questions: *which* sense to assign to “Hesperus” and, in particular, which sense to assign to “Hesperus” when it occurs in an indirect context. (We will return to the latter question in a moment.)

Departing from Frege’s terminology, Church calls senses “concepts” and explains the relation that holds between a name and its *designatum* in terms of a more primitive relation that holds between the individual concept expressed by the name and the thing of which it is an individual concept (1956a: §01). For example, suppose that the sense or concept univocally expressed by “Hesperus” is *the first planet visible in the evening*. Further suppose that this is, as a matter of objective fact, a concept of Hesperus that identifies it uniquely. In that case, the *designatum* of “Hesperus” is, in Church’s terminology, “a function of” this concept. This idea is encoded in the first of Church’s compositional principles, which taken together preserve Frege’s important idea that semantic compositionality is function-argument application. The first such principle is as follows:

**(Comp 1)**

The *designatum* of a name, if there is one, is a function of the concept expressed by that name, i.e., there exists a function $f$ such that *designatum* $(N) = f$ (concept expressed by $N)$, for all names $N$ for which there is a *designatum*.

According to Church, there can be non-designating (empty) names (like “Pegasus”) that express individual concepts that are not concepts of any actually existing thing. There can also be individual concepts of things—such as non-recursive real numbers—that have no names (1956a: §01 and fn. 50).

Unlike simple names, which express concepts purely in virtue of linguistic convention, definite descriptions—like “the successor of 0” and “the first planet visible in the evening”—are complex names, ones that express complex structured concepts composed out of other concepts. Further, any asserted sentence is also a complex name that—for the reasons discussed in section 3.2—designates a truth value and expresses a structured proposition composed out of individual concepts and class concepts (more of which in a moment).

According to Church, the proposition expressed by a sentence is its meaning—“that which is grasped when one understands the sentence” (1956a: §04). The proposition is also that which is preserved when the sentence is correctly translated into another language. It is also a concept of a truth value (cf. section 3.2). Like all concepts, propositions are also objective—mind-and-language independent—abstract entities “of the same general category as a class, a number, or a function” (ibid).

Complex names require two more compositional semantic principles:

**(Comp 2)**

The concept expressed by a complex name is a function of the concepts expressed by that name’s component names, so that if a component name is replaced by another expressing the same concept, the concept expressed by the complex name is not changed.

**(Comp 3)**

The *designatum* of a complex name is a function of the *designata* of that name’s component names, so that if a component name is replaced by another with the same *designatum*, the *designatum* of the complex name is not changed.

Another important kind of expression for Church is a *form* (1956a: §02), which is an expression obtained from a complex name by replacing one or more of its constituent names by a free occurrence of a variable (that doesn’t otherwise occur in the original complex). Suppose that we begin with the complex names:

- Venus is the first planet visible in the evening
- Venus is the last planet visible in the morning.

We can then replace the first constituent proper name in each of these with a free occurrence of a variable, to obtain the following (singulary) forms:

- $x$ is the first planet visible in the evening
- $x$ is the last planet visible in the morning.

Two (*n*-ary) forms are *concurrent* if they agree in their values—i.e., have the same value or no value—for every assignment of values to their free variables. For example, the two singulary forms just obtained are concurrent, since they both have the value True for the value Venus of $x$ and the value False for all other values of $x$. (Compare the forms “$x$ is the smallest perfect number” and “$x$ is the factorial of 3”.)

To each singulary form there corresponds a function, according to the rule that *the value of the function can be obtained for a given argument by assigning that argument to the free variable in the corresponding form*. So, two concurrent singulary forms with the same free variable will correspond to the same function (in extension). Just as there can be concepts of things that have no names, so there can be functions that have no corresponding form.

Any function whose range is just the two truth values, and in particular any function associated with a propositional form, is a *propositional function*. Whereas Russell (1903) claimed that the range of a given propositional function consists of propositions, Church argues that it consists of the two truth values (see, once again, §3.2). With that said, we can now state Church’s fourth compositional semantic principle, which extends (Comp 3) to forms:

**(Comp 4)**

If a component form is replaced by another form that is concurrent to it, the entire form is concurrent to the original one.

For example, suppose that we begin with

- Venus is the first planet visible in the evening and also orbits the Sun

and obtain the form

- $x$ is the first planet visible in the evening and also orbits $y.$

If we replace the first component form with a concurrent one, the result is concurrent to the original form:

- $x$ is the last planet visible in the morning and also orbits $y.$

Two forms are *concept-concurrent* if they agree in their concept value for every assignment of concept values to their free variables (1956a: fn. 30). This requires another principle for variables, which we omit from our exposition (see 1951b [BE: 284–5]).

To conclude our discussion of compositionality, it should be noted that what Church’s (Comp) principles can explain is how we are able to understand new complex *names* by calculating which of a stock of familiar complex concepts they express. While this explanation is an impressive achievement, it leaves unexplained how we are also able to grasp new complex *concepts* that we have not previously entertained but which have, as constituents, concepts with which we are familiar. Addressing this aspect of the problem of compositionality from within a Fregean framework like Church’s arguably requires the notion of a *canonical* concept of a concept (see E.III below). Since Church did not introduce such a notion explicitly, applying it to compositionality is beyond the scope of this entry.

According to Church (1941, 1956a), one can, by the process known as “functional abstraction”, obtain a closed expression or “name” of the function corresponding to a given form by prefixing “$\lambda x$” to that form (as is discussed in [supplement D](church.supplementD.md)). For example, prefixing “$\lambda x$” to the singulary form “$x$ is a planet” yields the closed expression “$\lambda x \hdot x$ is a planet”. According to Church, this expresses a class concept—in this case the concept of the class of planets—and designates the characteristic function of this class, the function that that maps any potential value of $x$ to truth iff it is a planet. In this way, one can designate the function that corresponds semantically to the form.

Here we see an important departure from Frege (1892b), who insisted that functions are *incomplete abstractions* (they are “unsaturated”), and so are not the kind of complete thing (or object) that can be designated. In particular, Frege insisted that the function *___ is a horse* is not a function, since “*___ is a horse*” appears to designate it, thereby suggesting that it is an object and not a function. This consequence of Frege’s rather inflexible attitude towards functions is extremely odd, if not paradoxical, and can be avoided by Church’s proposal that the function in question can be designated by “$\lambda x \hdot x$ is a horse”. (Church’s proposal is endorsed by Burge [2005b, 2019] and Kaplan [2005]; cf. Terrance Parsons [1986].)

### E.3 The Logic of Sense and Denotation

Church’s LSD, as described in the text, faces two objections that arise when we consider that once LSD is properly formulated as a theory of concepts, it is supposed to be suitable to serve as the semantics of possible languages.

First, Church’s account of the types does not tell us *which* concept of a given type determines the entity belonging to the type immediately below. So, in the event that LSD was required to serve as a semantic theory for a given language, because it would only tell us that *some* concept of type $\iota_2$ is assigned to “$a_1$”, it would not thereby tell us what “$a_1$” meant (cf. Kripke 2008).

This bring us to the second objection, which arises from the fact that (as we have already seen in the main text) intensional contexts can be iterated:

1. Hesperus is a planet
2. Hammurabi believes that (1)
3. Monica said that (2)
4. Sam believes that (3)
5. *Ad infinitum.*

Replacing such constructions with the corresponding ones in LSD requires an infinity of independent names, “$a_0$”–“$a_n$”, corresponding to the occurrences of “Hesperus” in (1), (2), (3), (4), etc. Likewise, (1), (2), (3), etc. are also an infinity of names expressing *propositional* concepts. If these names named an infinity of primitive and independent concepts, Church’s proposal would be subject to Davidson’s objection that a language for which LSD was a semantic theory could not be learned (1965). To meet this objection, something needs to be said about the nature of the relation $\Delta$ described in the main text.

There is an impressive degree of consensus that these objections can be met. As regards the latter objection, it is argued that what is needed is to be able both to grasp the individual concept expressed by, for example, “$a_0$” and to follow a rule for obtaining each concept of type $\iota_k$ from the concept of type $\iota_{k-1}$ below. There is also considerable consensus that such a rule can be stated (cf. Burge 2005c, 2009; Kripke 2008 [2011a]; Peacocke 2008; Salmón 1993, 2001, 2006). Indeed, there is even agreement among *some* of these authors that whereas, in the case of the various individual concepts that determine ordinary concrete individuals, none of them distinguishes itself by *identifying* which individual it is a concept of, concepts themselves are unlike ordinary concrete individuals in this regard. (Note that the notion of an identifying concept of a *number* is discussed by Church 1956a: fn. 122.) That is, in the case of concepts, it is claimed that the concept of type $\iota_k$ identifies the concept of type $\iota_{k-1}$ below and so, intuitively, tells us which concept it is. (Similar considerations apply to the hierarchy of propositions and propositional concepts.) This is what promises to provide some illumination about the nature of the relation $\Delta$. In which case, if one can (i) grasp the individual concept of $\iota_1$ expressed by “$a_0$”, and (ii) thereby grasp its identifying concept of type $\iota_2$, as well as (iii) repeat this process recursively for each concept of type $\iota_k$ given the concept of type $\iota_{k-1}$, then one *can* in principle learn a language for which LSD is a semantic theory. However, there is still disagreement about exactly what is required for a concept of a concept to be *identifying*; but the issue is beyond the scope of this entry (cf. the citations above.).

### E.4 LSD and the Criteria of Identity for Concepts

It is reasonable to require a criterion of identity for concepts (including propositions). After all, not only are concepts postulated abstract entities whose existence and identity is entailed by the theory in which they are postulated; but also the issue of whether two concepts are identical is very closely related to the natural question whether two expressions mean the same thing. Church’s papers on LSD contain attempts to formulate logistic theories of concepts based on three alternative criteria of identity for them (as well as reformulations of them in the light of the antinomies such as those discussed in section 4 of the main text). As we will see, Church says repeatedly that there is more that one theoretically important criterion of identity for concepts, each of which helps to limn a corresponding notion of concept (or sense). For example:

> No doubt there is more that one meaning of “sense”, according to the criterion adopted for equality of senses, and the decision among them is a matter of convention and expediency. (1956a: fn. 37)

Alternative (2) proposes that two complex concepts are identical iff the expressions that express them are necessarily materially equivalent (i.e., logically equivalent). Church comments that this

> leads to a notion of proposition which serves some purposes, including that of modal logic, but is not suitable for an analysis of indirect quotation. It is not surprising that there should be more than one notion of proposition, according to what identity criterion is adopted (1973a: fn. 11).

The point is that while Alternative (2) can provide insight into modal logic (cf. Kaplan 1975b), it is too coarse grained to be part of a logistic theory of concepts like LSD that is intended to provide an analysis of attributions of propositional attitudes. This is because, for example, all theorems of pure mathematics are necessarily materially equivalent (Bernays 1961). However, if we say, by Alternative (2), that all mathematical theorems express the same proposition, and if we individuate propositional attitudes in terms of the propositions believed, asserted etc., then anyone who believes or asserts one mathematical theorem believes or asserts all of them!

A more stringent criterion is Alternative (1), which is related to the process of functional abstraction. According to Alternative (1), two complex concepts are identical iff the corresponding complex expressions have the same free variables and can each be obtained from the other by a sequence of applications of:

- Alphabetic changes of bound variables, i.e., alpha-conversion (see [supplement D](church.supplementD.md))
- The replacement of component expressions by strict synonyms of the same type
- λ-conversion (see [supplement D](church.supplementD.md)).

Alternative (1) raises a constellation of issues (see the citations to follow). However, the basic issue can be seen from the following example adopted from Kripke’s thought experiment (1979), according to which Peter does not realize that Paderewski the great concert pianist is Paderewski the Polish diplomat. Consider examples (1)–(5), where *a =* Paderewski:

**(1)**

$a$ is an autodidact.

**(2)**

$a$ is taught by $a.$

**(3)**

$\lambda x \hdot x$ is taught by $a a.$

**(4)**

$\lambda x \hdot a$ is taught by $x a.$

**(5)**

$\lambda x \hdot x$ is taught by $x a.$

In Peter’s case, it seems plausible that he might believe that (2) but *not* believe that (5) as well as not being in a position to appreciate that his beliefs are inconsistent (Salmón 2010). It is unclear how this can be explained by Alternative (1), which would have it that (1)–(5) express the same proposition (see Russell 1905; Kripke 2005; Salmón 2010 and the citations therein for further discussion).

Church’s own counterexample to Alternative (1) is stated in unpublished correspondence that is described in Anderson (2001) and Salmón (2010). Recalling (from [supplement D](church.supplementD.md)) that numerals and arithmetical operations can be encoded in the λ-calculus, the λ-expression designating $m \times n$ will in general be λ-convertible with “$k$ ”, where “$k$” is the λ-expression designating the product of $m \times n.$ So, “$m \times n$” and “$k$” express the same concept by Alternative (1). Nevertheless, John might have the false belief reported in (6) without thereby having the false belief reported in (7):

**(6)**

John believes that $k$ is prime

**(7)**

John believes that $m \times n$ is prime.

The criterion that Church seems to favor, for the purposes of analyzing attributions of propositional attitudes in LSD, is Alternative (0), which is motivated in part by a criticism of Carnap’s proposal that two sentences are synonymous iff they are intensionally isomorphic (1947). A given sentence $S$ in a language $L$ is *intensionally isomorphic with* another given sentence $S'$ in a language $L'$ just in case $S$ and $S'$ are syntactically isomorphic and each of the syntactic counterparts in $S$ and $S'$ are cointensional with each other. Carnap’s requirement of syntactic isomorphism places excessively stringent requirements on synonymy. “Anita is Sarah”s lawyer’ and “Anita is Sarah”s attorney’ are intensionally isomorphic. Arguably, so are “Sarah is an autodidact” and “Sarah is self-taught” (assuming that “autodidact” is a compound such that “auto” can be mapped to “self” and “didact” to “taught”). However, “Anita is Sarah’s physician” and “Anita is Sarah”s medical doctor’, though intuitively synonymous, are not intensionally isomorphic because the sentences are not syntactically isomorphic.

Moreover, as Church argues, Carnap’s semantic requirement that the counterparts be cointensional (or necessarily materially equivalent) is too weak (1954). Consider Fermat’s Last Theorem, which is highly non-trivial (and was still unproven when Church gave the example):

$$ \nsim [(\exists x)(\exists y)(\exists z)(\textrm{positive integers } x, y, z) x^n+ y^n = z^n \cdot n \gt 2]]$$

Suppose that we introduce into a language $L$ two number-theoretic predicates “$P$” and “$Q$”, and stipulate in the meta-language that

$$\begin{align} Pn & \equiv_{df} n \lt 3\\ Qn & \equiv_{df} (\exists x)(\exists y)(\exists z)(\textrm{positive integers } x, y, z) [x^n + y^n = z^n]\\ A\approx B & \equiv_{df} A \textrm{ is cointensional with } B\\ \end{align}$$

Given this set up, the following are syntactically isomorphic as well as cointensional, and so intensionally isomorphic:

$$(\exists n) [Qn\approx Pn]$$

and

$$(\exists n) [Pn\approx Pn].$$

Yet someone could believe the proposition expresses by the second without believing that expressed by the first, because the equivalence (which depends on the theorem) is non-trivial.

Church made a modification to Carnap’s criterion by weakening Carnap’s excessively strict syntactic requirement and strengthening his rather lax semantic one. According to Alternative (0) two complex concepts are identical iff their corresponding complex expressions are *synonymously isomorphic*; that is, they have the same free variables and can each be obtained from the other by a sequence of applications of:

- Alphabetic changes of bound variables, i.e., alpha-conversion (see [supplement D](church.supplementD.md))
- The replacement of a component expression of a given type by a simple synonym of the same type
- The replacement of a component simple expression of a given type by a synonym of the same type

In contrast with Alternative (1), λ-conversion is not allowed, so the main issue here is what Church means by “synonym”. The key point appears to be that while complex expressions of a type can be stipulated to be synonymous with simple expressions of that type, and while simple expressions of a type can be stipulated to be synonymous with complex or simple expressions of that type, *complex expressions cannot be stipulated to be synonymous with other complex expressions*. A plausible reason for this is that complex expressions express corresponding complex concepts, which, if they have different parts and structure, are distinct. (This is related to the aforementioned Russell-Myhill Paradox discussed in section 4.5 of the main text.)

This takes care of the above counterexample to intensional isomorphism, since “$Pn$” and “$Qn$” are stipulated to be synonymous with different complexes. Therefore, “$(\exists n) [Qn\approx Pn]$” and “$(\exists n) [Pn\approx Pn]$” are not deemed to express the same proposition by Alternative (0).

This fine-grained criterion will individuate propositions finely enough for the purposes of analyzing attributions of propositional attitudes in LSD. However, it arguably individuates propositions too finely for some purposes. Consider, once again:

$$\nsim [(\exists x)(\exists y)(\exists z)(\textrm{positive integers }x, y, z) [x^n + y^n = z^n \cdot n \gt 2]]$$

and

$$(\exists x)(\exists y)(\exists z)(\textrm{positive integers }x, y, z) [x^n + y^n = z^n ] \supset n = 1 \lor n = 2.$$

As Bernays points out, these cannot be obtained from one another by the above substitutions (1961). However, while a *layperson* might believe one without believing the other, *they both express the same piece of mathematical information value*, viz. Fermat’s Last Theorem. So it is arguable that Alternative (0) individuates propositions too finely to be a correct theory of mathematical information value.

Numerous other counterexamples have been proposed to Alternative (0), which might also suggest that it is too fine grained for certain purposes; these are discussed by Anderson (1980, 1986, 1987, 1998, 2001), Bealer (1982), Kripke (2005) and Salmón (2010).

### E.5 Russellian Philosophy of Language

Earlier we saw that Frege’s treatment of indirect contexts requires us to prohibit the application of Leibniz’s law, because names—including definite descriptions—with the same customary *designatum* but different customary senses cannot be substituted *salva veritate* within such contexts. Russell’s solution (1905; PM) is to distinguish definite descriptions from proper names and to analyze the former as complex quantifier phrases that can have either primary or secondary occurrence—that is, either wide or narrow scope—with respect to a propositional attitude verb. According to Russell’s solution, the following attributions all have very different logical forms, which is why deducing them from each other by Leibniz’s law is prohibited:

**(Id)**

Hammurabi wishes to know whether Hesperus is Hesperus.

**$(2^{ndry})$**

Hammurabi wishes to know whether [the unique $x: x$ is the first planet seen shining in the morning] is Hesperus.

**$(1^{ry})$**

[the unique $x: x$ is the first planet seen shining in the morning] is such that Hammurabi wishes to know whether $x$ is Hesperus.

While Church evidently considers Russell’s philosophy of language to be worthy of serious consideration (1943a; 1956a: §00; 1951b: fn. 14), he also considers the distinction between primary and secondary occurrences of descriptions to be an unwelcome complication imposed by the theory of descriptions (1982: fn. 2). Moreover, in later work (1989), Church shows that Russell’s theory of descriptions is not sufficient to provide an adequate analysis of attributions of propositional attitudes if descriptions are eliminated from $(2^{ndry})$ using the method of *PM* (1925–27 edition, \*14) along with its principle of extensionality for propositional functions. The important moral is that the *intensional* propositional functions from Russell’s earlier (1905; PM) are also crucial to his solution.

Church also observes in his (1984) that in the system of *PM* the correspondents of verbs of propositional attitude would have to be functions and that such functions cannot vary in adicity. How, then, can one express attributions of propositional attitudes, which may be of varying complexity? Church introduces a connective for propositional identity for which we will use a bold equality sign, so that (in addition to identities between propositional variables such as “$p = q$”) identities between *wffs* are well formed. (The connective is governed by fifteen axioms discussed in section 4 and [supplement F](church.supplementF.md).) With this in hand, constructions such as “$p \sequiv$ All planets are massive” are well formed; so we can say, for example, “$p \sequiv$ All planets are massive & Believes (Sam, $p)$”.

As for the failure of Leibniz’s law, instead of appealing to the theory of descriptions, Church proposes a neo-Russellian logistic theory, not of concepts (as in LSD) but of structured entities that are *un-conceptualized*—in the sense that they do not consist of concepts—, which he calls “propositional surrogates” (1989, 1995c). Unlike the neo-Russellian structured *propositions* of Kaplan (1989), these surrogates are composed entirely out of semantic extensions. Further, because they correspond structurally to complex expressions, which consist of predicates or relations with $n$ argument places, the surrogates themselves are also structured complexes—specifically, ordered $n+1$-tuples composed of semantic extensions. These extensions include individuals (the designata of names), “propositional functions” in Church’s sense of functions from individuals to truth values (such as that associated with “$x$ is a planet”), functions from objects to objects (such as that associated with “$x$”s mother’), as well as functions from functions to either individuals or truth values. These, he suggests, can provide an analysis of attributions of propositional attitudes (in a way that is inspired by Ajdukiewicz (1960, 1967)).

For example, according to this proposal,

**(1)**

George IV wishes to know whether Scott is the author of *Waverley*

has two different readings, according to which George IV is related to different surrogates. To find the first reading, we rewrite (1) as follows (where where $G =$ “George IV” and $\stK \sequiv$ “wishes to know whether”)

$$\tag{2} \stK (G, \lambda X \lambda x \lambda y \hdot Xxy, =, \textit{the author of Waverley}, \textit{Scott})$$

$\stK$ is a function *from* George IV, *and* the function designated by “$\lambda X \lambda x \lambda y \hdot Xxy$”, *together with* the latter function’s three arguments, to a truth value. Further, we assume that the adicity of $\stK$ shouldn’t vary depending on the adicity of the function that occupies its 2ⁿᵈ argument position (although see Taylor & Hazen 1992); and so we keep $\stK$’s first argument (George IV) and replace the others with an ordered *n*-tuple consisting of the aforementioned function *and* its arguments:

$$\tag{3} \stK (G, \langle \lambda X \lambda x \lambda y \hdot Xxy, =, \textit{the author of Waverley}, \textit{Scott} \rangle)$$

What (3) says is that George IV wishes to know about the relation of identity, the author of *Waverley*, and Scott, whether the second stands in the first to the third. Since the author of *Waverley* = Scott, we can obtain:

$$\tag{4} \stK (G, \langle \lambda X \lambda x \lambda y \hdot Xxy, =, \textit{Scott}, \textit{Scott} \rangle.)$$

On the other hand, (1) can also be read as reporting that George IV wishes to know whether

$$\tag{5} \stK (G, \langle \lambda X \lambda f \lambda x \lambda y \hdot X (f x,) y, =, \textit{the author of}, \textit{Waverley}, \textit{Scott} \rangle)$$

That is, George IV wishes to know about the relation of identity, the function *the author of*, *Waverley*, and Scott, whether the second applied to the third stands in the first to the fourth. Intuitively, wishing to know *de re* about the author of *Waverley* is wishing to know about Scott, since the author of *Waverley* = Scott. Wishing to know *de re* about *the author of* and *Waverley* without having applied the former to the latter, is not wishing to know about Scott. So, if Sam hasn’t applied the function, he may wish to know (5) but not (4).

By calling these structured entities “surrogates”, Church *might* be showing awareness that structured entities composed of extensions do not unify to produce intrinsically representational propositions. Rather, they are intended as a guide to axiomatizing the theory of propositions. However, since Church is explicit that surrogates are individuated in accordance with either Alternative (0) or Alternative (1), there is a danger that any axiomatic theory of them will be vulnerable to the Russell-Myhill Paradox (discussed in [supplement F](church.supplementF.md)). Church himself notes that

The task of finding a suitable axiomatic theory of propositions has seemed very difficult in the past, especially in regard to the question of identity of propositions and it may well be rendered much easier by using propositional surrogates to guide the choice of axioms, and in the end perhaps even to provide a relative consistency proof (1989: fn. 21 [BE: 838–9]).

Currently, however, it is not known whether such a consistency proof can be provided.
