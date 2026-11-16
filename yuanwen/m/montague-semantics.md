# Montague Semantics
**First published Mon Nov 7, 2011; substantive revision Wed Feb 5, 2025**

*Janssen, Theo M. V., Zimmermann, Thomas Ede*

Montague semantics is a theory of natural language semantics and of its relation with syntax. It was originally developed by the logician Richard Montague (1930–1971) and subsequently modified and extended by linguists, philosophers, and logicians. The most important features of the theory are its use of model theoretic semantics which is nowadays commonly used for the semantics of logical languages and its adherence to the principle of compositionality—that is, the meaning of the whole is a function of the meanings of its parts and their mode of syntactic combination. This entry presents the origins of Montague Semantics, summarizes important aspects of the classical theory, and sketches more recent developments. We conclude with a small example, which illustrates some modern features.

## 1. Introduction

### 1.1 Background

Montague semantics is the approach to the semantics of natural language introduced by Richard Montague in the 1970s. He described the aim of his enterprise as follows:

> The basic aim of semantics is to characterize the notion of a true sentence (under a given interpretation) and of entailment (Montague 1970c, 373 fn)[^montague-1970c].

The salient points of Montague’s approach are a model theoretic semantics, a systematic relation between syntax and semantics, and a fully explicit description of a fragment of natural language. His approach constituted a revolution: after the Chomskyan revolution that brought mathematical methods into syntax, now such methods were introduced in semantics.

Montague’s approach became influential, as many authors began to work in his framework and conferences were devoted to ‘Montague grammar’. Later on, certain aspects of his approach were adapted or changed, became generally accepted or were entirely abandoned. Nowadays not many authors would describe their own work as ‘Montague semantics’ given the many differences that have taken shape in semantics since Montague’s own work, but his ideas have left important traces, and changed the semantic landscape forever. In our presentation of Montague semantics the focus will be on these developments.

Richard Montague was a mathematical logician who had specialized in set theory and modal logic. His views on natural language must be understood with his mathematical background in mind. Montague held the view that natural language was a formal language very much in the same sense as predicate logic was a formal language. As such, in Montague’s view, the study of natural language belonged to mathematics, and not to psychology (Thomason 1974, 2)[^thomason-1974]. Montague formulated his views:

> There is in my opinion no important theoretical difference between natural languages and the artificial languages of logicians; indeed I consider it possible to comprehend the syntax and semantics of both kinds of languages with a single natural and mathematically precise theory. (Montague 1970c, 373)[^montague-1970c]

Sometimes only the first part of the quote is recalled, and that might raise the question whether he did not notice the great differences: for instance that natural languages develop without an a priori set of rules whereas artificial languages have an explicit syntax and are designed for a special purpose. But the quote as a whole expresses clearly what Montague meant by ‘no important theoretical difference’; the ‘single natural and mathematically precise theory’ which he aimed at, is presented in his paper ‘Universal Grammar’ (Montague 1970c)[^montague-1970c]. He became most well-known after the appearance of Montague 1973, in which the theory is applied to some phenomena which were discussed intensively in the philosophical literature of those days.

According to Caponigro (forthcoming), Montague’s interest in the field arose when preparing a seminar on the philosophy of language as a visiting professor in Amsterdam in 1966. Only a couple of years earlier, he had deemed the “systematic exploration of the English language, indeed of what might be called the ‘logic of ordinary English’, […] either extremely laborious or impossible” and did ‘not find it rewarding’ (Montague and Kalish 1964, 10)[^montague-1964]. Yet he appears to have changed his mind after perusing Quine’s (1960)[^quine-1960] *Word and Object* as well as Chomsky’s (1965)[^chomsky-1965] *Aspects of the Theory of Syntax*: the latter opened the perspective of treating the syntax of natural language as a formal system but failed to provide any serious analysis of linguistic meaning; the former offered a systematic connection between traditional grammar and formal logic – and much more systematically so than contemporary logic texts. In fact, Montague’s semantic work owes a lot to Quine’s descriptive insights into the ‘logic of ordinary English’, but differs from his predecessor by making the connection between language and logic in rigorous, mathematical terms:

> It should be emphasized that this is not a matter of vague intuition, as in elementary logic courses, but an assertion to which we have assigned exact significance. (Montague 1973, 237)[^montague-1973]

We next describe the basic ideas of Montague semantics. Section 2 presents several components of Montague semantics in more detail. Section 3 includes a discussion of philosophically interesting aspects, and Section 4 provides a detailed example and further reading.

### 1.2 Basic Aspects

To implement his objective, Montague applied the method which is standard for logical languages: model theoretic semantics. This means that, using constructions from set theory, a model is defined, and that natural language expressions are interpreted as elements (or sets, or functions) in this universe. Such a model should not be conceived of as a model of reality. On the one hand, the model gives more than reality: natural language does not only speak about past, present and future of the real world, but also about situations that might be the case, or are imaginary, or cannot be the case at all. On the other hand, however, the model offers less: it merely specifies reality as conceived by language. An example: we speak about mass nouns such as *water* as if every part of water is water again, as if it has no minimal parts, which physically is not correct. For more information on natural language metaphysics, see Bach 1986b.

Montague semantics is not interested in a particular situation (e.g. the real world) but in semantical properties of language. When formalizing such properties, reference to a class of models has to be made, and therefore the interpretation of a language will be defined with respect to a set of (suitable) models. For example, in the introduction we mentioned that the characterization of entailment was a basic goal of semantics. That notion is defined as follows. Sentence $A$ entails sentence $B$ if in all models in which the interpretation of $A$ is true, also the interpretation of $B$ is true. Likewise, a tautology is true in all models, and a contradiction is true in no model.

An essential feature of Montague semantics is the systematic relation between syntax and semantics. This relation is described by the *Principle of Compositionality*, which reads, in a formulation that is standard nowadays:

> The meaning of a compound expression is a function of the meanings of its parts and of the way they are syntactically combined. (Partee 1984, 281)[^partee-1984]

An example: Suppose that the meaning of *walk*, or *sing* is (for each model in the class) defined as the set of individuals who share respectively the property of (being an individual that is) walking or the property of (being an individual that is) singing. By appealing to the principle of compositionality, if there is a rule that combines these two expressions to the verb phrase *walk and sing*, there must be a corresponding rule that determines the meaning of that verb phrase. In this case, the resulting meaning will be the intersection of the two sets. Consequently, in all models the meaning of *walk and sing* is a subset of the meaning of *walk*. Furthermore, we have a rule that combines the noun phrase *John* with a verb phrase. The resulting sentence *John walks and sings* means that John is an element of the set denoted by the verb phrase. Note that in any model in which John is element of the intersection of walkers and singers, he is an element of the set of walkers. So *John walks and sings* entails *John walks*.

An important consequence of the principle of compositionality is that all the parts that play a role in the syntactic composition of a sentence must also have a meaning. And furthermore, each syntactic rule must be accompanied by a semantic rule which says how the meaning of the compound is obtained. Thus, the meaning of an expression is determined by the way in which the expression is formed, and as such the derivational history plays a role in determining the meaning. For further discussion, see Section 2.5.

The formulation of the aim of Montague semantics mentioned in the introduction (‘to characterize truth and entailment of sentences’) suggests that the method is restricted to declarative sentences. But this need not be the case. In Montague 1973 (241 fn) we already find suggestions for how to deal with imperatives and questions. Hamblin (1973)[^hamblin-1973] and Karttunen (1977)[^karttunen-1977] have given a semantics for questions by analyzing them as expressing sets of propositions, viz. those expressed by their (declarative) answers; an alternative approach, taken by Groenendijk and Stokhof (1989) considers questions as partitioning logical space into mutually excluding possibilities.

Since Montague only considered sentences in isolation, certain commentators pointed out that the sentence boundary was a serious limitation for the approach. But what about discourse? An obvious requirement is that the sentences from a discourse are interpreted one by one. How then to treat co-referentiality of anaphora over sentence boundaries? The solution which was proposed first was *Discourse Representation Theory* (Kamp 1981)[^kamp-1981]. On the one hand, that was an offspring of Montague’s approach because it used model theoretic semantics; on the other hand, it was a deviation because (discourse) representations were an essential ingredient. Nowadays there are several reformulations of DRT that fit into Montague’s framework (see van Eijck and Kamp 1997)[^eijck-1997]. A later solution was based upon a change of the logic; dynamic Montague semantics was developed and that gave a procedure for binding free variables in logic which has an effect on subsequent formulas (Groenendijk and Stokhof 1990, 1991)[^groenendijk-1990][^groenendijk-1991]. Hence the sentence boundary is not a fundamental obstacle for Montague semantics.

## 2. Components of Montague Semantics

### 2.1 Unicorns and Meaning Postulates

Montague’s most influential article was ‘The Proper Treatment of Quantification in Ordinary English’ (Montague 1973)[^montague-1973], commonly abbreviated as ‘PTQ’. It presented a fragment of English that covered several phenomena which were in those days discussed extensively. One of the examples gave rise to the trademark of Montague grammar: the unicorn (several publications on Montague grammar are illustrated with unicorns).

Consider the two sentences *John finds a unicorn* and *John seeks a unicorn*. These are syntactically alike (subject-verb-object), but are semantically very different. From the first sentence follows that there exists at least one unicorn, whereas the second sentence is ambiguous between the so called *de dicto* (or *non-specific*, or *notional*) reading which does not imply the existence of unicorns, and the *de re* (or *specific,* or *objectual*) reading from which existence of unicorns follows.

The two sentences are examples of a traditional problem called ‘quantification into intensional contexts’. Traditionally, the second sentence as a whole was seen as an intensional context, and the novelty of Montague’s solution was that he considered the object position of *seek* as the source of the phenomenon. He formalized *seek* not as a relation between two individuals, but as a relation between an individual and a more abstract entity (see section 2.2). Under this analysis the existence of a unicorn does not follow. The *de re* reading is obtained in a different way (see section 2.5).

It was Montague’s strategy to apply to all expressions of a category the most general approach, and narrow this down, when required, by meaning postulates (and, in some cases, logical decomposition). So initially, *find* is also considered to be a relation between an individual and such an abstract entity, but some meaning postulate restricts the class of models in which we interpret the fragment to only those models in which the relation for *find* is the (classical) relation between individuals.

As a consequence of this strategy, Montague’s paper has many meaning postulates. Nowadays semanticists often prefer to express the semantic properties of individual lexical items directly in their lexical meaning, and then *find* is directly interpreted as a relation between individuals. Meaning postulates are mainly used to express structural properties of the models (for instance, the structure of the time axis), and to express relations between the meanings of words. For a discussion of the role of meaning postulates, see Zimmermann 1999.

### 2.2 Noun Phrases and Generalized Quantifiers

Noun phrases like *a pig*, *every pig*, and *Babe*, behave in many respects syntactically alike: they can occur in the same positions, can be conjoined, etc. But a uniform semantics seems problematic. There were proposals which said that *every pig* denotes the universally generic pig, and *a pig* an arbitrary pig. Such proposals were famously rejected by Lewis (1970)[^lewis-1970], who raised, for instance, the question which would be the color of the universal pig, all colors, or would it be colorless?

Montague proposed the denotation of a descriptive phrase to be a set of properties. For instance, the denotation of *John* is the set consisting of properties which hold for him, and of *every man* the set of properties which hold for every man. Thus they are semantically uniform, and then conjunction and/or disjunction of arbitrary quantifier phrases (including e.g. *most but not all*) can be dealt with in a uniform way.

This abstract approach has led to generalized quantifier theory, see Barwise and Cooper 1981 as well as Peters and Westerståhl 2006. Among the most popular achievements of generalized quantifier theory is a semantic characterization of so-called ‘negative polarity items’: words like *yet* and *ever*. Their occurrence can be licensed by negation: *The 6:05 has arrived yet* is out, whereas *The 6:05 hasn’t arrived yet* is OK. But there are more contexts in which negative polarity items may occur, and syntacticians did not succeed in characterizing them. Ladusaw (1980)[^ladusaw-1980] did so by using a characterization from generalized quantifier theory. This has been widely acknowledged as a great success for formal semantics. His proposal roughly was as follows. Downward entailing expressions are expressions that license inferences from supersets to subsets. *No* is downward entailing because from *No man walks* it follows that *No father walks*. A negative polarity item is acceptable only if it is interpreted in the scope of a downward entailing expression, e.g. *No man ever walks*. Further research showed that the analysis needed refining, and that a hierarchy of negative polarity items should be used (Ladusaw 1996, Homer 2021)[^homer-2021][^ladusaw-1996].

### 2.3 Logic and Translation

An expression may directly be associated with some element from the model. For instance, *walk* with some set of individuals. Then also the operations on meanings have to be specified directly, and that leads to formulations such as:

> $G_3 (\ulcorner$is$\urcorner)$ is that function $f \in ((2^I)^{A\times A})^{A^{ \omega}}$ such that, for all $x \in A^{\omega}$, all $u,t \in A$ and all $i \in I : f(x)(t,u)(i) = 1$ if and only if $t = u$. (Montague 1970a, 195)[^montague-1970a]

Such descriptions are not easy to understand, nor convenient to work with. Montague (1973, 228)[^montague-1973] said, ‘it is probably more perspicuous to proceed indirectly’. For this purpose he introduced a language, called ‘intensional logic’. The operation described above is then represented by $^{\wedge}\lambda t\lambda u[t = u$]. The $\lambda t$ says that it is a function that takes $t$ as argument, likewise for $\lambda u$. So $\lambda t\lambda u[t = u$] is a function which takes two arguments, and yields true if the arguments are equal, and otherwise false. The preceding $^{\wedge}$ says that we consider a function from possible worlds and moments of time to the thus defined function.

Three features of the Montague’s ‘intensional logic’ attracted attention:

1. It is a *higher-order* logic. Even though type logic was already an established logical framework in those days, linguists, philosophers and mathematicians were more familiar with first order logic (the logic in which there are only variables for basic entities). Since in Montague semantics the parts of expressions must have meaning too, a higher order logic was needed (we have already seen that *every man* denotes a set of properties).
2. It is *intensional* in that it obeys neither Leibniz’ law of substitution of co-extensional terms nor existential generalization, thereby seemingly bringing logic closer to natural language. To achieve this, Montague generalized Kripke’s (1963)[^kripke-1963] groundbreaking semantic techniques from first-order modal logic to higher-order type logic. However, the same interpretive effect could have been achieved by using a two-sorted, extensional type logic (Gallin 1975; Zimmermann 1989; 2021)[^gallin-1975][^zimmermann-1989], which many semanticsists prefer today.
3. Montague used **λ*-abstraction*, which at the time was not a standard ingredient of logic. As illustrated in section 4.1, the *λ*-operator makes it possible to express higher-order functions, which may serve as the contributions that parts of sentences make to their truth-values. The importance of *λ*-expressions was once expressed by Barbara Partee in a talk on ‘The first decade of Montague Grammar’: ‘Lambdas changed my life’ (Partee 1996, 24)[^partee-1996]. Nowadays *λ*-expressions are a standard tool in natural language semantics, and particularly in the type-driven approach made popular by Heim and Kratzer (1998). In section 4.1, an example will be given that illustrates the power of *λ*-expressions.

This motivation for *indirect interpretation* – by way of compositional translation as a tool for obtaining perspicuous representations of meaning – has a number of important consequences:

1. Translation is a tool to obtain formulas which *represent* meanings. Different, but equivalent formulas are equally acceptable. In the introduction of this article it was said that Montague grammar provided a mechanical procedure for obtaining the logical translation. As a matter of fact, the result of Montague’s translation of *Every man runs* is not identical with the traditional translation, although equivalent with it, see the example in Section 4.1.
2. The translation into logic is a mere notational convenience and in principle dispensable. So in Montague semantics, translation into logical notation does not provide unique ‘logical forms’.
3. For each syntactic construction (operation plus rule, in the terminology of Montague 1970c)[^montague-1970c] there is a semantic rule that combines the corresponding representations of the meanings. Bach (1976)[^bach-1976] aptly called this interpretive strategy the ‘rule-to-rule hypothesis‘.
4. Operations depending on syntactic features of formulas are not allowed. Janssen (1997)[^janssen-1997] criticized several proposals on this aspect. He showed that proposals that are deficient in this respect are either incorrect (make wrong predictions for closely related sentences), or can be corrected and generalized, and thus improved.

The method of using logical notation for representing meanings has a long history, going back at least to philosophers such as Dalgarno and Leibniz who developed formal languages in order to express philosophy clearly. In the 19th century, there were several proposals for artificial languages in order to make mathematical argumentation more transparent, for instance by Frege and by Peano. Frege’s ‘Begriffsschrift’ (Frege 1879)[^frege-1879] can be seen as the birth of predicate logic: he introduced quantifiers. His motivation came from mathematical needs; he did not use his Begriffsschrift in his papers on natural language. Russell (1905)[^russell-1905] used logic to represent the meanings of natural language. A classical example in his paper is the analysis of *The king of France is bald*. Syntactically it has the form subject-predicate, but if it were constructed logically as a subject-predicate, then *the king of France*, which denotes nothing, cannot be the subject. So syntactic form and logical form may diverge: natural language obscures the view of the real meaning. This became known as the ‘misleading form thesis’. Therefore, philosophers of language saw, in those days, the role of logic as a tool to improve natural language, an aim that is alien to Montague semantics. In fact, using higher-order functional type theory (Church 1940)[^church-1940] as the target of his translation, Montague (1970c)[^montague-1970c] developed a ‘compositional’ version of Russell‘s analysis, which does preserve the constituent structure of the source language (English). An interesting overview of the history of translating natural language into logic is given in Stokhof 2007.

### 2.4 Intensionality and Tautologies

Montague defined the denotation of a sentence as a function from possible worlds and moments of time to truth values. Such a function is called an ‘intension’. As he said (Montague 1970a, 220)[^montague-1970a], this made it possible to deal with the semantics of common phenomena such as modifiers, e.g. in *Necessarily the father of Cain is Adam*. Its denotation cannot be obtained from the truth value of *The father of Cain is Adam*: one needs to know the truth value for other possible worlds and moments of time. The intensional approach also made it possible to deal with several classical puzzles. Two examples from Montague 1973 are: *The temperature is rising*, which should not be analyzed as stating that some number is rising; and *John wishes to catch a fish and eat it*, which should not be analyzed as implying that John has a particular fish in mind.

Intensional semantics has been criticized for the fact that all tautologies get the same meaning (are synonymous). Indeed, a tautology as *John is ill or he is not ill* gets as intension the function that constantly yields **true**, and the same holds for other tautologies. If one is interested in discriminating semantically between tautologies, then a refinement of the notions ‘meaning’ and ‘equivalence’ is needed: ‘meaning’ should see distinctions between tautologies, and ‘equivalence’ should be sensitive for the thus refined notion of meaning. The oldest proposals to account for this problem goes back to Carnap (1947, §14) and was later taken up by Lewis (1970, sec. 5): propositions are structured by including in their meanings also the meanings of their parts. Then indeed *Green grass is green* and *White snow is white* have different meanings. However, lexical synonyms still pose a problem. Since *woodchuck* and *groundhog* are names for the same species, *John believes that Phil is a groundhog* is, under this view, equivalent with *John believes that Phil is a woodchuck*. One could consider belief contexts a separate problem, but most authors see it as part of the problem of equivalence of all tautologies.

Later several proposals for dealing with this have been developed; surveys can be found in Bäuerle and Cresswell (2003), Fox and Lappin (2005), and Egré (2021)[^egré-2021]. The latter authors explain that there are two strategies: the first is to introduce impossible worlds in which *woodchuck* and *groundhog* are not equivalent, and the second is to introduce an entailment relation with the property that identity does not follow from reciprocal entailment. Fox and Lappin follow the second strategy.

### 2.5 Scope and Derivational History

A well known example of scope ambiguity is *Every man loves a woman*. Is there only one woman involved (e.g. Mother Mary), or does every man love a different woman? The sentence has no lexically ambiguous words, and there are no syntactic arguments to assign them more than one constituent structure. How to account for the ambiguity?

In Montague 1973, the scope ambiguity is dealt with by providing for the sentence two different derivations. On the reading that *every* has wide scope, the sentence is produced from *every man* and *loves a woman*. On the reading that only one woman is involved, the sentence is obtained from *Every man loves him*$_1$. The *him*$_1$ is an artifact, a placeholder, or, one might say, a syntactic variable. A special kind of rule, called a ‘quantifying-in rule’, will replace this *him*$_1$ by a noun phrase or a pronoun (in case there are more occurrences of this placeholder). The placeholder corresponds with a logical variable that becomes bound by the semantic counterpart of the quantifying-in rule. For the sentence under discussion, the effect of the application of the quantifying-in rule to *a woman* and *Every man loves him*$_1$ is that the desired sentence is produced and that the quantifier corresponding with *a woman* gets wide scope. When we would depict its derivation as a tree, this tree would be larger than the constituent structure of the sentence due to the introduction and later removal of *him*$_1$.

This quantifying-in rule is used by Montague for other phenomena as well. An example is co-referentiality: *Mary loves the man whom she kissed* is obtained from *He*$_1$ *loves the man whom he*$_1$ *kissed*. And the *de re* reading of *John seeks a unicorn* is obtained from *a unicorn* and *John seeks him*$_1$.

Many researchers did not like this analysis in which powerful syntactic rules and artificial symbols (*him*$_1)$ are used. Below we consider two strategies to remedy.

The first strategy was to deny the ambiguity. Some linguists have argued that the scope order is the same as the surface order; this is known as ‘Jackendoff’s principle’ (Jackendoff 1972)[^jackendoff-1972]. But there are sentences where this does not work. Others said that it is sufficient only to obtain the weakest reading (*every* wide scope), and that the stronger reading is inferred when additional information is available. But there are sentences for which the different scope readings are logically independent, as in *Every woman loves one man*.

The second strategy was to capture the ambiguity in another way than by the quantifying-in rules. Historically the first method was to put the interpretations of the noun phrases in a store from which these interpretations could be retrieved when needed: different stages of retrieving correspond with differences in scope. One might see this as a grammar in which the direct correspondence between syntax and semantics has been relaxed. The method is called ‘Cooper Store’, after the author who proposed this (Cooper 1983)[^cooper-1983]. A later proposal is DRT $(=$ Discourse Representation Theory), where representations are used to account for such ambiguities (van Eijck and Kamp 1997)[^eijck-1997].

A recent method is by means of ‘lifting rules’ (see section 3.3): the meaning of a noun-phrase is ‘lifted’ to a more abstract level, and different levels yield different scope readings (see Hendriks 2001 and Jacobson 2014)[^hendriks-2001][^jacobson-2014].

Even if the role of derivational history can be avoided for scope and co-referentiality, other phenomena remain for which derivational histories have a role. An example is *John wondered when Alice said she would leave*. This is ambiguous between John asking for the time of leaving, or for the time of saying. So the sentence is ambiguous, even though there are no arguments for assigning to it more than one constituent structure. Pelletier (1993)[^pelletier-1993] presents this sentence and others, and says: ‘In order to maintain the Compositionality Principle, theorists have resorted to a number of devices which are all more or less unmotivated (except to maintain the Principle): Montagovian “quantifying-in” rules, traces, gaps, […].’ Pelletier’s objection can be appreciated if one assumes that meaning assignment is directly linked with constituent structure. But, as explained in Section 1.2, this is not the case. The derivation specifies which rules are combined in which order, and this derivation constitutes the input to the meaning assignment function. The constituent structure is determined by the output of the syntactic rules, and different derivation processes may generate one and the same constituent structure. In this way, semantic ambiguities are accounted for. One should not call something ‘constituent structure’ if it is not intended as such, and next refute it because it does not have the desired properties.

The distinction between a derivation tree and a constituent tree is made in several theories of grammar. In Tree Adjoining Grammars (TAGs) the different scope readings of the sentence about loving a woman differ in the order in which the noun-phrases are substituted in the basic tree. A classical example in Chomskyan grammar is *The shooting of the hunters was bloody*, which is ambiguous between the hunters shooting, or the hunters being shot at. The two readings come from two different sources: one in which *the hunters* is the subject of the sentence, and one in which it is the object.

## 3. Philosophical Aspects

### 3.1 From Frege to Intensions

Throughout most of his semantic work, Montague avowedly adopted a version of Frege’s (1892)[^frege-1892] distinction between ‘sense’ and ‘denotation’. Frege’s original line of thought concerns sentences like *The Greeks did not know that the morning star is the evening star*, which does not seem to express that the Greeks were confused about the self-identity of Venus. Frege’s analysis accounts for this observation by having descriptive names like *the morning star* denote their referents in ordinary contexts, but something different in embedded clauses (or, more generally, in ‘indirect contexts’): their ‘sense’ – a semantic value that captures the way in which an object is referred to. Since referring to a celestial object by *the morning star* differs from referring to it by *the evening star*, the embedded clause does not denote an analytic truth but a contingent proposition, whose truth may well have escaped the Greeks.

Frege’s approach is known to run into a number of problems. One of them concerns the iteration of indirect contexts, as in *Gottlob suspected that the Greeks did not know that the morning star is the evening star.* Though he did not explicitly address the issue, Frege is usually understood as resorting to an infinite hierarchy of ever more indirect senses to be associated with each otherwise non-ambiguous expression (Dummett 1981, 267; Carnap 1947, §30; Kripke 2008, 183; see however Parsons 1981 for a more cautious interpretation)[^carnap-1947][^dummett-1981][^kripke-2008][^parsons-1981]. The purported Fregean line of analysis has been criticized for multiplying ambiguity beyond necessity (Janssen 2012)[^janssen-2012] as well as raising serious learnability issues (Davidson 1968, 11)[^davidson-1968]. Though Montague did acknowledge a hierarchy of senses, he did not employ it for the analysis of iterated indirect contexts. Instead, he identified Frege’s (1892)[^frege-1892] senses with *intensions* along the lines of Carnap (1947)[^carnap-1947] – set theoretic functions on a logical space of possible worlds (or world-time-pairs) whose values are the denotations of expressions – their *extensions*. In particular, the way in which a description refers to its referent is captured by its dependence on contingent facts. As a case in point, the famous Fregean descriptions differ in intension as long as there is a possible world in which the brightest star at dawn is not the same object as the brightest star at night.

The replacement of senses by intensions paves the way to an alternative approach to iterated intensionality: generalizing Kripke’s (1963)[^kripke-1963] semantics of modality, Montague (1970b, 73)[^montague-1970b] accounted for clausal embedding in terms of propositional operators whose extension, like that of their argument, depends on a given point in logical space. As it turns out, this so-called ‘neighborhood semantics’ of clausal embedding does without reference to a sense hierarchy even in iterated indirect environments (*ibid.,* 76), which is why Montague used it as the basis for his general compositional analysis of natural language. Montague (*ibid.*, 75f.) still presented his approach as being in line with Frege’s, thereby emphasizing the commonalities in the overall architecture of semantic theory, which he identified as ‘Frege’s functionality principle’:

> the extension of a formula is a function of the extensions (ordinary extensions) of those of its parts not standing within indirect contexts (that is […] not standing within the scope of an operator), together with the intensions (what Frege also called *indirect extensions*) of those parts that do stand within indirect contexts. (Montague 1970b, 74f.)[^montague-1970b]

Moreover, Montague (1970c, 390)[^montague-1970c] called one of the key constructions of his general theory of reference ‘Fregean interpretation’; and in his type-logical hierarchy, intensions are marked by the letter ‘$s$’, which is short for ‘sense’ (*ibid.*, 379). This notation has become quite common in linguistic semantics, although the ‘$s$’ is frequently taken to stand for possible $s$ituations!

Only at one point in his semantic work did Montague abandon his Fregean stance: in his essay ‘English as a formal language’ (1970a), he employed a one-level architecture of ‘Russellian’ denotations and expressed his doubts about the cogency of Frege’s motivation for non-propositional senses (*ibid*., sec. 9, remark xi), thereby foreshadowing Kaplan’s (1975)[^kaplan-1975] comparison between the frameworks of Frege 1892 and Russell 1905. Yet in his ‘Universal Grammar’, Montague commented:

> I should like, however, to withdraw my emphasis […] on the possibility of doing without a distinction between sense and denotation. While such a distinction can be avoided in special cases, it remains necessary for the general theory, and probably provides the clearest approach even to the special cases in question. (Montague 1970c, 374, fn.)[^montague-1970c]

Even though Montague tended to play down the difference, the switch from senses to intensions is known to have dramatic consequences on the fine-grainedness of semantic analysis. In particular, as mentioned in section 2.4, any two logically equivalent sentences come out as having the same intension; yet their senses will diverge if their truth value is not determined in the same way. Montague indicated how this unwelcome consequence may be avoided in terms of mismatches between worlds and contexts, creating what he called ‘“unactualizable” points of reference’ (*ibid.*, 382), but he did not provide a detailed analysis to substantiate his sketchy remarks.

### 3.2 Compositionality

For Montague the principle of compositionality did not seem to be a subject of deliberation or discussion, but the only way to proceed. In effect he made compositionality the core part of his ‘theory of meaning’ (Montague 1970c, 378)[^montague-1970c], which was later summed up in the slogan: ‘Syntax is an algebra, semantics is an algebra, and meaning is a homomorphism between them’ (Janssen 1983, 25)[^janssen-1983]. Yet although Montague used the term ‘Frege’s functionality principle’ for the way in which extension and intension are compositionally intertwined, he did not have a special term for compositionality in general. Later authors, who identified the Principle of Compositionality as a cornerstone of Montague’s work, also used the term ‘Frege’s Principle’ (originating with Cresswell 1973, 75)[^cresswell-1973]; Thomason 1980 is an early source for the term ‘compositional’.

It has been claimed that Montague’s analysis of pronouns is not compositional. This is, however, not the case. In order to explain the compositional nature of his treatment of pronouns, both Janssen (1997)[^janssen-1997] and Dowty (2007)[^dowty-2007] explain how variables are interpreted in logic; we follow their explanations. Consider the following clauses from the traditional Tarskian interpretation of predicate logic.

1. $\llbracket \varphi \wedge \psi \rrbracket^g = \mathbf{1}$ if and only if $\llbracket \varphi \rrbracket^g = \mathbf{1}$ and $\llbracket \psi \rrbracket^g = \mathbf{1}$
2. $\llbracket \exists \ x\varphi \rrbracket^g = \mathbf{1}$ if and only if for some $h, h \sim_x g$ and $\llbracket \varphi \rrbracket^h = \mathbf{1}$

The first clause says: $\varphi \wedge \psi$ is true when using assignment $g$ if and only if *φ* and *ψ* are true when the assignment $g$ is used. In the second clause assignments $h$ are introduced (by $\sim_x g)$ which are equal to $g$ except maybe for the value they assign to variable $x$. Montague uses the same format, with the difference that besides $g$ he also has $i$, the time of reference and $j$, the possible world, as superscripts.

In the formulation of the clauses there is nothing which can be pointed at as ‘the meaning’, in fact it is a definition of truth with $g$ and $h$ as parameters. So how is it possible that this (and Montague’s work) are compositional?

The answer requires a shift in perspective. The meaning of a formula *φ*, shortly $M(\varphi)$, is the set of assignments for which the formula is true. Then the first clause says that

$$ M(\varphi \wedge \psi) = M(\varphi) \cap M(\psi), $$

so a simple set-theoretic combination on the two meanings is performed. And

$$ M(\exists x \ \varphi) = \{g \sim_x h\mid h \in M(\varphi)\}, $$

i.e., $\{g \mid \text{for some }h \in M(\varphi), g \sim_x h \}$, which can be described as: extend the set $M(\varphi)$ with all $x$-variants. (The reference to ‘$x$’ may be felt as problematic, but Montague even eliminated this trace of non-compositionality by assigning appropriate meanings to variables; see Zimmermann and Sternefeld 2013, ch. 10, for pertinent details.)[^zimmermann-2013] In general, in Montague semantics the meaning of an expression is a function which has as domain the triples $\langle$moment of time, possible world, assignment to variables$\rangle$.

Is it possible to achieve compositionality for natural language? Obvious candidates for counterexamples are idioms, because their meanings seem not to be built from their constituting words. However, Westerståhl (2002)[^westerståhl-2002] presents a collection of methods, varying from compound basic expressions, to deviant meanings for constituting parts. Janssen (1997)[^janssen-1997] refutes several other counterexamples that are put forward in the literature.

How strong is compositionality? Mathematical results show that any language can be given a compositional semantics, either by using an unorthodox syntax (Janssen 1997)[^janssen-1997] or by using an unorthodox semantics (Zadrozny 1994)[^zadrozny-1994]. However their proofs are not helpful in practice. Hodges (2001)[^hodges-2001] showed under which circumstances a given compositional semantics for a fragment can be extended to a larger language.

There is no general agreement among formal semanticists about the role and status of compositionality; at least the following four positions have been held (nearly the same list is given in Partee 1996)[^partee-1996]:

1. Compositionality is a basic methodological principle; any proposal should obey it. Janssen (1997)[^janssen-1997] and Jacobson (2014)[^jacobson-2014] are adherents of this position.
2. Compositionality is a good method, but other methods can be used as well. For instance formal meaning representation can be used in an essential way. An example is DRT (discourse representation theory, Kamp 1981)[^kamp-1981].
3. Compositionality is an ideal, but a proposal need not satisfy it.
4. It is an empirical issue whether compositionality can be achieved. See Dowty 2007 for a discussion.

An extensive discussion of compositionality is given in Janssen 1997, and in the entry on compositionality.

### 3.3 Syntactic Categories and Semantic Types

According to Montague, the purpose of syntax is to provide the input to semantics:

> I fail to see any interest in syntax except as a preliminary to semantics. (Montague 1970c, 223)[^montague-1970c]

Although syntax was in his eyes subordinate, he was fully explicit in his rules in which he used some ad hoc syntactic tools.

In Montague 1970a and 1970c, the relation between syntactic categories and semantic types is given only by a list. Montague (1973)[^montague-1973] defines a systematic relation which amounts to the same relation as one would have in categorial grammar. However, Montague’s syntax is not a categorial syntax because the rules are not always category driven and because some of the rules are not concatenation rules.

For each of these two aspects, proposals have been put forward to change the situation. One direction was to stay closer to the ideals of categorial grammar, with only type-driven rules, sometimes allowing for a restricted extension of the power of concatenation rules (see, for example, Morrill 1994, Carpenter 1998)[^carpenter-1998][^morrill-1994]. The other approach was to incorporate in Montague grammar as much as possible the insights from syntactic theories, especially originating from the tradition of Chomsky. A first step was made by Partee (1973)[^partee-1973], who let the grammar produce structures (labelled bracketings); a syntactically sophisticated grammar (with Chomskyan movement rules) was used in the Rosetta translation project (Rosetta 1994)[^rosetta-1994]. The influential textbook by Heim and Kratzer (1998) combined the two approaches by applying type-driven interpretation to the syntactic level of (Chomskyan) Logical Forms.

In his syntactic accounts, Montague tended to treat ‘logical‘ words like determiners (*the, a*, *every*) and conjunctions (*and*, *or, not*) syncategorematically, i.e., not by means of lexical entries, but as the effect of specific syntactic rules; the reason for this decision is unknown, but it may be speculated that it was part of a characterization of grammatical meaning in terms of logicality, presumably along the lines of Tarski’s 1986 invariance criterion. As a consequence, a different rule is needed for *John walks and sings* than for *John walks and Mary sings*: syntactically the first one is a conjunction of verb phrases and the second one of sentences. However, the two meanings of *and* are closely related and a generalization is missed. As a general solution it was proposed to use rules (or alternatively general principles) that change the category of an expression – a change that corresponds with a semantic rule that ‘lifts’ the meaning. For instance, the meaning of *and* as a connective between verb phrases is obtained by lifting the meaning of the sentence connective $\wedge$ to $\lambda P\lambda Q\lambda x[P(x) \wedge Q(x)].$ The line of analysis has been extensively studied in Partee and Rooth 1983, Partee 1987, Hendriks 2001, and Winter 2001.

Montague’s method of defining fragments with a fully explicit syntax has become far less popular than it was in the heyday of Montague Grammar in the 1980s. Nowadays semanticists prefer to focus on specific phenomena, suggesting rules which are only explicit concerning the semantic side. This tendency has been criticized by Partee in Janssen 1997 and Jacobson 2014, where a fragment is actually provided.

### 3.4 Pragmatics

The truth conditions of sentences sometimes vary with the context of use. Thus, whether *I am happy* is true, depends on who the speaker is; other examples include the referents of *here* and *this*. Montague (1968; 1970b)[^montague-1968][^montague-1970b] addressed these factors, indicating that they could be treated by introducing additional parameters besides the time and the possible world. Despite occasional critcism (Cresswell 1973, 111; Lewis 1980, 86f.)[^cresswell-1973][^lewis-1980], the treatment of contextual dependence by way of a fixed finite list of parameters has become quite standard in formal semantics.

Montague initially treated contextual parameters on a par with times and worlds, but in ‘Universal Grammar’ (Montague 1970c)[^montague-1970c] he indicated that a distinction should be made between those that determine the content (which, following Frege 1892, is what is denoted in indirect contexts)[^frege-1892] from those that constitute it:

> Thus meanings are functions of two arguments– a possible world and a context of use. The second argument is introduced in order to permit a treatment […] of such indexical locutions as demonstratives, first- and second-person singular pronouns, and free variables (which are treated […] as a kind of demonstrative). Senses on the other hand […] are functions of only one argument, regarded as a possible world. The intuitive distinction is this: meanings are those entities that serve as interpretations of expressions (and hence, if the interpretation of a compound is always to be a function of the interpretations of its components, cannot be identified with functions of possible worlds alone), while senses are those intensional entities that are sometimes denoted by expressions. (Montague 1970c, 379)[^montague-1970c]

While these remarks are still a far cry from double-indexing approaches to context dependence (Kamp 1971)[^kamp-1971], they do exhibit the basic idea underlying the shiftability criterion for distinguishing context and index (Lewis 1980)[^lewis-1980]. In particular, Montague’s meanings share a core feature with Kaplan’s (1989)[^kaplan-1989] characters: both map paramteterized contexts to propositions, understood as (characteristic functions of) sets of possible worlds.

Montague (1970c, 68)[^montague-1970c] followed Bar-Hillel 1954 in treating context dependence as part of pragmatics. It was only after his death, that his framework was connected to other aspects of pragmatics. In particular, in early work on Montague grammar, various proposals were made to give compositional characterizations of presuppositions and (conventional) implicatures (Peters 1979; Karttunen and Peters 1979)[^karttunen-1979][^peters-1979], but later treatments were not always completely compositional, taking several contextual factors into account (Beaver 1997)[^beaver-1997]. In a similar vein, early work in the tradition was rather optimistic about directly applying Montague semantics to non-declarative uses of (declarative) sentences (Cresswell 1973)[^cresswell-1973], but later accounts had to invoke a lot more than linguistic meaning, including models of interlocutors’ perspectives (Gunlogson 2003)[^gunlogson-2003].

### 3.5 Ontology

Montague’s semantic analyses were given in terms of a type-logical hierarchy whose basic ingredients were truth values, possible individuals, and possible worlds. While the exact nature of individuals and worlds depends on the (arbitrary) choice of a particular model (or ‘Fregean interpretation’), the truth values 1 (true) and 0 (false) transcend the class of all models, thus emphasizing their status as logical objects. A lot of work in current linguistic semantics still applies Montague’s type-logical hierarchy, which is however often enriched by *events* (or, more generally: *eventualities*) that serve as the referents of verbs and verb phrases (Bach 1986a; Parsons 1990)[^bach-1986a][^parsons-1990].

In early work on intensional analysis (Carnap 1947, Kaplan 1964)[^carnap-1947][^kaplan-1964], possible worlds had been identified with models of a suitable extensional language. For reasons indicated in section 3.1, Montague (1969, 164)[^montague-1969] broke with this tradition, appealing to Kripke’s account of modality based on possible worlds as unstructured basic objects. In his essay ‘On the nature of certain philosophical entities’ (Montague 1969)[^montague-1969], he argued that this seemingly minor technical innovation opens a new perspective in philosophical analysis, by reducing certain ‘dubious’ entities to predicate intensions or *properties* – functions mapping possible worlds to sets of objects. The idea was that, once the conceptual and techical problems of the semantics of intensional languages had been overcome, they may replace extensional predicate logic as a basis of philosophical argument:

> Philosophy is always capable of enlarging itself; that is, by metamathematical or model-theoretic means – means available within set theory – one can “justify” a language or theory that transcends set theory, and then proceed to transact a new branch of philosophy within the new language. It is now time to take such a step and to lay the foundations of intensional languages. (Montague 1969,165f.)[^montague-1969]

Montague illustrated his claim by detailed analyses of (talk about) pains, tasks, obligations, and events in terms of second-order intensional logic, which contained the core elements of his (slightly) later compositional interpretation of English.

Although it has since become common in linguistic semantics to analyse content in terms of possible worlds, they are not always taken to be totally devoid of structure. As a case in point, Kratzer (2002)[^kratzer-2002] has argued that the verb *know* relates subjects to facts and thus its interpretation requires appeal to the mereology of worlds: facts are concrete parts worlds. Moreover, as in Kripke’s original approach, semantic theory frequently imposes some external structure on logical space. Thus, accessibility relations and distance measures between worlds are invoked to account for, respectively, propositional attitudes (along the lines of Hinitkka 1969) and counterfactual conditionals (following Lewis 1973)[^lewis-1973]. In a similar vein, the universe of individuals (or ‘entities’, in Montague’s parlance) nowadays gives way to a richer domain of structured objects, including substances and their parts, which may serve as extensions of mass nouns such as *water* (Pelletier & Schubert 2003)[^pelletier-2003], as well as groups and their members, which are denoted by plural noun phrases (Link 1983)[^link-1983]. Also when properties (*loving John*) are considered as entities for which predicates may hold (*Mary likes loving John*), additional structure is needed: property theory gives the tools to incorporate them (Turner 1983)[^turner-1983].

Occasional doubts have been raised as to the adequacy of Montague’s higher-order intensional logic as a tool for the semantic interpretation of natural language:

> It seems to me that this is the strategy employed by Montague Grammarians, who are in fact strongly committed to compositionality. […]. There is a price to be paid however. The higher order entities evoked in this “type theoretical ascent” are much less realistic philosophically and psycholinguistically than our original individuals. Hence the ascent is bound to detract from the psycholinguistic and methodological realism of one’s theory. (Hintikka 1983, 20)[^hintikka-1983]

This objection does not appreciate the role played by higher-order abstraction in compositional semantics, which is not to form sentences about higher-order functions. Rather, *λ*-abstraction is used as a heuristic tool to describe compositional contributions of expressions to larger syntactic environments (cf. Zimmermann 2021, sec. 2.1)[^zimmermann-2021]. Thus, e.g., the extension of a determiner is defined as its contribution to the truth value of a sentence in which it occurs (in subject position), which can be described in terms of the extensions of the nouns and verb phrases it combines with – and these extensions are themselves sets (by a similar reasoning). The abstract higher-order objects are thus merely convenient ways of describing the kinematics of compositionality and do not serve as the objects that the sentences of the language so described are about, or that its terms refer to. As a case in point, it can be shown that even though the (indirect) interpretation of the English fragment of Montague 1973 makes use of *λ*-abstraction over second-order variables, its expressive power is much weaker than higher-order type logic and does not even have the resources to formulate certain meaning postulates to which its lexical items abide (Zimmermann 1983)[^zimmermann-1983]. In fact, Hintikka’s alternative (game-theoretical) semantics fares no better once it is formulated in a compositional way (see Hodges 1997 or Caicedo *et al*. 2009)[^caicedo-2009][^hodges-1997].

## 4. Concluding Remarks

### 4.1 Legacy

Montague revolutionized the field of semantic theory. He introduced methods and tools from mathematical logic, and set standards for explicitness in semantics. Now all semanticists know that logic has more to offer than first-order logic only.

### 4.2 Further Reading

A recent introduction is Jacobson 2014. It is a gentle introduction to the field, especially for linguists and philosophers. It presents several successes obtained by the approach. Older introductions are Dowty *et al.* 1981 and Gamut 1991, which are more technical and prepare for Montague’s original papers. An overview of the history of the field is given by Partee and Hendriks (1997) as well as Partee (2011)[^partee-2011]; Caponigro (forthcoming) provides an extensive biographical background on Montague. Collections of important papers are Portner and Partee (eds.) 2002 and Partee 2004; further information is provided in the volume edited by McNally and Szabó (2022), which includes a short account of PTQ (Zimmermann 2022)[^zimmermann-2022]. The ‘Handbook of compositionality’(Werning et al. 2011) discusses many aspects of the approach. The most important journals in the field are *Linguistics and Philosophy*, the *Journal of Semantics*, *Natural Language Semantics*, and *Semantics and Pragmatics*.

### 4.3 Example

A small example is presented below, it consists of the two sentences *John is singing*, and *Every man is singing*. The example is not presented in Montague’s original way, but modernized: there is a lifting rule, the determiner is a basic expression, and intensional aspects are not considered.

The grammar has four basic expressions:

1. *John* is an expression of the category Proper Name. Its denotation is an individual represented in logic by **John**.
2. The Intransitive Verb *sing* denotes a set (the set of singers), and is represented by the predicate symbol **sing**.
3. The Common Noun *man*, which denotes a set, represented by **man**.
4. The Determiner *every*. Its denotation is $\lambda P\lambda Q\forall x[P(x) \rightarrow Q(x)$]; an explanation of this formula will be given below.

The grammar has three rules.

1. A rule which takes as input a Proper Name, and produces a Noun Phrase. The input word is not changed: it is lifted to a ‘higher’ grammatical category. Semantically its meaning is lifted to a more abstract, a ‘higher’ meaning: the representation of the denotation of *John* as Noun Phrase is $\lambda P[P(\textbf{John})$]. An explanation of the formula is as follows. $P$ is a variable over properties: if we have chosen an interpretation for $P$, we may say whether $P$ holds for John or not, i.e. whether $P(\textbf{John})$ is true. The $\lambda P$ abstracts from the possible interpretations of $P$: the expression $\lambda P[P(\textbf{John})$] denotes a function that takes as input properties and yields **true** if the property holds for John, and **false** otherwise. So the denotation of *John* is the characteristic function of the set of properties he has.
2. A rule that takes as input a Noun Phrase and an Intransitive Verb, and yields as output a Sentence: from *John* and *sing* it produces *John is singing*. The corresponding semantic rule requires the denotation of the Noun Phrase to be applied to the denotation of the Intransitive Verb. This is represented as $\lambda P[P(\textbf{John})](\textbf{sing})$. When applied to the argument **sing**, the function represented by $\lambda P[P(\textbf{John})$] yields **true** if the predicate **sing** holds for John, so precisely in case **sing**(**John**) is **true**. So $\lambda P[P(\textbf{John})](\textbf{sing})$ and **sing**(**John**) are equivalent. The latter formula can be obtained by removing the $\lambda P$ and substituting **sing** for $P$. This is called ‘lambda-conversion’.
3. A rule that takes as inputs a Determiner and a Common Noun, and yields a Noun Phrase: from *every* and *man* it produces *every man*. Semantically the denotation of the Determiner has to be applied to the denotation of the Common Noun, hence $\lambda P\lambda Q\forall x[P(x) \rightarrow Q(x)](\textbf{man})$. By lambda conversion (just explained) this is simplified to $\lambda Q\forall x[\textbf{man}(x) \rightarrow Q(x)$]. This result denotes a function that, when applied to property $A$, yields **true** just in case all man have property $A$.

The example given with the last rule helps us to understand the formula for *every* : that denotes a relation between properties $A$ and $B$ which holds in case every $A$ has property $B$.

The next step is now easy. Apply the rule for combining a Noun Phrase and an Intransitive Verb to the last result, producing *Every man is singing*. The output of the semantic rule is $\lambda Q\forall x[\textbf{man}(x) \rightarrow Q(x)](\textbf{sing})$. By lambda conversion we obtain $\forall x[\textbf{man}(x) \rightarrow \textbf{sing}(x)],$ which is the traditional logical representation of *Every man is singing*.

Note the role of lambda-operators:

1. *John* and *every man* are interpreted in a similar way: sets of properties. These sets can be represented due to lambda-operators.
2. *Every man* and *sing* are syntactically on the same level, but semantically *sing* has a subordinated role: it occurs embedded in the formula. This switch of level is possible due to lambda-operators.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=montague-semantics). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/montague-semantics/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=montague-semantics&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/montague-semantics/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

[Please contact the author with suggestions.]

## Related Entries

compositionality | discourse representation theory | Frege, Gottlob | generalized quantifiers | identity: transworld | impossible worlds | intensional transitive verbs | intentionality | logic: intensional | logical form | mass expressions: logic of | possible worlds | presupposition | propositional attitude reports | propositions: structured | questions | reference | rigid designators | semantics: dynamic | type theory | type theory: Church’s type theory

[^angelelli-1967]: Angelelli, I. (ed.), 1967, *Gottlob Frege. Kleine Schriften*, Hildesheim: Olms.

[^bach-1976]: Bach, E., 1976, “An extension of classical transformational grammar”, in J. M. Sadock, D. J. Dwyer, S. C. Song, and E. W. Bach (eds.), *Problems in Linguistic Metatheory* (Proceedings of the 1976 conference), pp. 183–224. East Lansing, Michigan: Michigan State University.

[^bach-1986a]: –––, 1986a, “The algebra of events”, *Linguistics and Philosophy*, 9: 5–16; reprinted in Portner and Partee (eds.) 2002, pp. 324–33.

[^bach-1986b]: –––, 1986b, “Natural language metaphysics”, in R. Barcan Marcus, G. J. W. Dorn, and P. Weingartner (eds.), *Logic, Methodology, and Philosophy of Science VII*, pp. 573–595, Amsterdam: North Holland.

[^bar-hillel-1954]: Bar-Hillel, Y., 1954, “Indexical Expressions”, *Mind*, 63: 359–376.

[^barwise-1981]: Barwise, J. and Cooper, R., 1981, “Generalized quantifiers and natural language”, *Linguistics and Philosophy*, 4: 159–219. Reprinted in Portner and Partee (eds.) 2002, pp. 75–126.

[^bäuerle-2003]: Bäuerle, R. and Cresswell, M. J., 2003, “Propositional attitudes”, in Gabbay and Guenthner (eds.) 2003, pp. 121–141.

[^bäuerle-1983]: Bäuerle, R., Schwarze, C., and von Stechow, A. (eds.), 1983, *Meaning, Use and Interpretation of Language*, Berlin: de Gruyter.

[^beaver-1997]: Beaver, D. I., 1997, “Presupposition”, in J. van Benthem and A. ter Meulen (eds.) 1997, pp. 939–1008.

[^benthem-1997]: van Benthem, J. and ter Meulen, A. (eds.), 1997, *Handbook of Logic and Language*, Amsterdam: Elsevier.

[^benthem-2011]: van Benthem, J. and ter Meulen, A. (eds.), 2011, *Handbook of Logic and Language. Second edition*, Amsterdam: Elsevier MIT Press.

[^caicedo-2009]: Caicedo, X., Dechesne, F., and Janssen, T. M. V., 2009, “Equivalence and quantifier rules for logics with imperfect information”, *Logic Journal of the IGPL*, 17: 91–129.

[^caponigro-nd]: Caponigro, I., forthcoming: *Richard Montague: The Simplicity of Language, the Complexity of Life*, New York: Oxford University Press.

[^carnap-1947]: Carnap, R., 1947, *Meaning and Necessity: A Study in Semantics and Modal Logic*, Chicago: University of Chicago Press.

[^carpenter-1998]: Carpenter, B., 1998, *Type-Logical Semantics*, Cambridge, MA: MIT Press.

[^chomsky-1965]: Chomsky, N., 1965, *Aspects of the Theory of Syntax*, Cambridge, MA: MIT Press.

[^church-1940]: Church, A., 1940, “A Formulation of the Simple Theory of Types”, *Journal of Symbolic Logic*, 5: 56–68.

[^cooper-1983]: Cooper, R., 1983, *Quantification and Syntactic Theory* (Synthese Language Library, 21), Dordrecht: Reidel.

[^cresswell-1973]: Cresswell, M. J., 1973, *Logics and Languages*, London: Methuen.

[^davidson-1968]: Davidson, D., 1968, “On saying that”, *Synthese*, 19: 130–146.

[^davidson-1972]: Davidson, D. and Harman, G. (eds.), 1972, *Semantics of Natural Language* (Synthese Library, 40), Dordrecht: Reidel.

[^dowty-2007]: Dowty, D., 2007, “Compositionality as an empirical problem”, in C. Barker and P. Jacobson (eds.), *Direct Compositionality* (Oxford Studies in Theoretical Linguistics, 14), Oxford: Oxford University Press, pp. 23–101.

[^dowty-1981]: Dowty, D., Wall, R., and Peters, S., 1981, *Introduction to Montague Semantics* (Synthese Language Library, 11), Dordrecht: Reidel.

[^dummett-1981]: Dummett, M., 1981, *Frege – Philosophy of Language*, second edition, Cambridge, MA: Harvard University Press.

[^egré-2021]: Egré, P., 2021, “Logical Omniscience”, in D. Gutzmann, L. Matthewson, C. Meier, H. Rullmann, and T. E. Zimmermann (eds.), *The Wiley Blackwell Companion to Semantics* (Volume 3), Hoboken: Wiley-Blackwell, Hoboken: Wiley-Blackwell, pp. 1725–1749.

[^eijck-1997]: van Eijck, J. and Kamp, H., 1997, “Representing discourse in context”, in J. van Benthem and A. ter Meulen (eds.) 1997, pp. 179–237; revised reprint in J. van Benthem and A. ter Meulen (eds.) 2011, pp. 181–252.

[^fox-2005]: Fox, C. and Lappin, S., 2005, *Foundations of Intensional Semantics*, Malden, MA: Blackwell.

[^frege-1879]: Frege, G., 1879, *Begriffsschrift, eine der arithmetischen nachgebildete Formelsprache des reinen Denkens*, Halle: Nebert.

[^frege-1892]: –––, 1892, “Über Sinn und Bedeutung”, *Zeitschrift für Philosophie und philosophische Kritik*, 100: 25–50; reprinted in Angelelli 1967, pp. 143–162; translated as ‘On Sense and Reference’ in Geach and Black 1952, pp. 56–58.

[^gabbay-2003]: Gabbay, D. M. and Guenthner, F. (eds.), 2003, *Handbook of Philosophical Logic*, second edition, Dordrecht: Kluwer.

[^gallin-1975]: Gallin, D., 1975, *Intensional and higher-order Modal Logic*, Amsterdam: North-Holland.

[^geach-1952]: Geach, P. T. and Black, M. (eds.), 1952, *Translations from the Philosophical Writings of Gottlob Frege*, Oxford: Blackwell.

[^gamut-1991]: Gamut, L. T. F., 1991, *Logic, Language and Meaning. Volume 2: Intensional Logic and Logical Grammar*, Chicago and London: The University of Chicago Press.

[^groenendijk-1989]: Groenendijk, J. and Stokhof, M., 1989, “Type-shifting rules and the semantics of questions”, in *Properties, Types and Meanings* (Volume 2: Semantic Issues), G. Chierchia, B. H. Partee, and R. Turner (eds.), Dordrecht: Reidel, pp. 21–68; reprinted in Portner and Partee (eds.) 2002, pp. 421–457.

[^groenendijk-1990]: –––, 1990, “Dynamic Montague Grammar”, in *Proceedings of the Second Symposion on Logic and Language*, L. Kalman & L Polos (eds.), Budapest: Eotvos Lorand University Press, pp. 3–48.

[^groenendijk-1991]: –––, 1991, “Dynamic predicate logic”, *Linguistics and Philosophy*, 14: 39–100.

[^gunlogson-2003]: Gunlogson, C., 2003, *True to Form*, New York: Routledge.

[^hamblin-1973]: Hamblin, C. L., 1973, “Questions in Montague English”, *Foundations of Language*, 10: 41–53.

[^heim-1998]: Heim, I. and Kratzer, A., 1998, *Semantics in Generative Grammar*, Oxford: Blackwell.

[^hendriks-2001]: Hendriks, H., 2001, “Compositionality and model-theoretic interpretation”, *Journal of Logic, Language and Information*, 10: 29–48.

[^hintikka-1969]: Hintikka, J., 1969, “Semantics for Propositional Attitudes”, in *Philosophical Logic*, J. W. Davis *et al*. (eds.), Dordrecht: Reidel, pp. 21–45.

[^hintikka-1983]: –––, 1983, *The Game of Language. Studies in Game-Theoretical Semantics and Its Applications* (Synthese Language Library, 22), Dordrecht: Reidel.

[^hodges-1997]: Hodges, W., 1997, “Compositional semantics for a language of imperfect information”, *Logic Journal of the IGPL*, 5(4): 539–563.

[^hodges-2001]: –––, 2001, “Formal features of compositionality”, *Journal for Logic Language and Computation*, 10: 7–28.

[^homer-2021]: Homer, V., 2021, “Negative Polarity”, in D. Gutzmann, L. Matthewson, C. Meier, H. Rullmann, and T. E. Zimmermann (eds.), *The Wiley Blackwell Companion to Semantics* (Volume 4), Hoboken: Wiley-Blackwell, pp. 2025–2063.

[^jackendoff-1972]: Jackendoff, R. S., 1972, *Semantic Interpretation in Generative Grammar*, Cambridge, MA: MIT Press.

[^jacobson-2014]: Jacobson, P., 2014, *Compositional Semantics. An introduction to the syntax/semantics interface*, Oxford: Oxford University Press.

[^janssen-1983]: Janssen, T. M. V., 1983, *Foundations and Applications of Montague Grammar*, Ph.D. Dissertation, University of Amsterdam.

[^janssen-1997]: –––, 1997, “Compositionality (with an appendix by B. Partee)”, in van Benthem and ter Meulen (eds.) 1997, pp. 417–473.

[^janssen-2001]: –––, 2001, “Frege, contextuality and compositionality”, *Journal of Logic, Language and Information*, 10: 115–136.

[^janssen-2012]: –––, 2012, “Compositionality: its historic context”, in *The Oxford Handbook of Compositionality*, M. Werning et al. (eds.), Oxford: Oxford University Press, pp. 19–46.

[^kamp-1971]: Kamp, H., 1971, “Formal Properties of ‘Now’”, *Theoria*, 37: 227–273.

[^kamp-1981]: –––, 1981, “A theory of truth and semantic representation”, in J. Groenendijk, T. Janssen, and M. Stokhof (eds.), *Formal Methods in the Study of Language*, Centre for Mathematics and Computer Science, Amsterdam, pp. 1–14; reprinted in Portner and Partee (eds.) 2002, pp. 189–222.

[^kaplan-1964]: Kaplan, D., 1964, *Foundations of Intensional Logic*, UCLA dissertation.

[^kaplan-1975]: –––, 1975, “How to Russell a Frege-Church ”, *Journal of Philosophy*, 72: 716–729.

[^kaplan-1989]: –––, 1989, “Demonstratives”, in J. Almog, J. Perry, and H. Wettstein (eds.), *Themes from Kaplan*, Oxford: Oxford University Press, pp. 481–563.

[^karttunen-1977]: Karttunen, L., 1977, “Syntax and semantics of questions”, *Linguistics and Philosophy*, 1: 3–44. Reprinted in Portner and Partee (eds.) 2002, pp. 382–420.

[^karttunen-1979]: Karttunen, L. and Peters, S., 1979, “Conventional Implicature”, in *Presupposition* (Syntax and Semantics, 11), New York: Academic Press, pp. 1–56.

[^kratzer-2002]: Kratzer, A., 2002, “Facts: Particulars or Information Units?”, *Linguistics and Philosophy*, 25: 655–670.

[^kripke-1963]: Kripke, S., 1963, “Semantical Considerations on Modal Logic”, *Acta Philosophica Fennica*, 16: 83–94.

[^kripke-2008]: –––, 2008 “Frege’s Theory of Sense and Reference: Some Exegetical Notes”, *Theoria*, 74: 181–218.

[^ladusaw-1980]: Ladusaw, W. A., 1980, “On the notion *Affective* in the analysis of negative-polarity items”, *Journal of Linguistic Research*, 1: 1–16; reprinted in Portner and Partee (eds.) 2002, pp. 457–470.

[^ladusaw-1996]: –––, 1996, “Negation and polarity items”, in Lappin (ed.) 1996, chapter 12, pp. 321–341.

[^lappin-1996]: Lappin, S. (ed.), 1996, *The Handbook of Contemporary Semantic Theory* (Blackwell Handbooks in Linguistics, 3), Oxford: Blackwell.

[^lewis-1970]: Lewis, D., 1970, “General semantics”, *Synthese*, 22: 18–67.

[^lewis-1973]: –––, 1973, *Counterfactuals*, Oxford: Blackwell.

[^lewis-1980]: –––, 1980, “Index, Context, and Content”, in S. Kanger and S. Öhman (eds.), *Philosophy and Grammar*, Dordrecht: Reidel, pp. 79–100.

[^link-1983]: Link, G., 1983, “The logical analysis of plurals and mass terms: a lattice-theoretic approach”, in Bäuerle *et al*. 1983, 302–323; reprinted in Portner and Partee (eds.) 2002, pp. 127–146.

[^mcnally-2022]: McNally, L. and Szabó, Z. (eds.), 2022, *A Reader’s Guide to Classic Papers in Formal Semantics* (Studies in Linguistics and Philosophiy, 100), Cham: Springer.

[^montague-1968]: Montague, R., 1968, “Pragmatics”, in R. Klibansky (ed.), *Contemporary Philosophy. A Survey*, Florence: La Nuova Italia Editrice, pp. 102–122; reprinted in Thomason (ed.) 1974, pp. 95–118.

[^montague-1969]: –––, 1969, “On the nature of certain philosophical entities”, *The Monist*, 353: 159–194; reprinted in Thomason (ed.) 1974, pp. 148–187.

[^montague-1970a]: –––, 1970a, “English as a formal language”, in B. Visentini, et al. (eds.), *Linguaggi nella Società e nella Tecnica*, Milan: Edizioni di Communita, pp. 189–224; reprinted in Thomason (ed.) 1974, pp. 188–221.

[^montague-1970b]: –––, 1970b, “Pragmatics and intensional logic”, *Synthese*, 22: 68–94; reprinted in Thomason (ed.) 1974, pp. 119–147.

[^montague-1970c]: –––, 1970c, “Universal grammar”, *Theoria*, 36: 373–398; reprinted in Thomason (ed.) 1974, pp. 7–27.

[^montague-1973]: –––, 1973, “The proper treatment of quantification in ordinary English”, in K. J. J. Hintikka, J. M. E. Moravcsik, and P. Suppes (eds.), *Approaches to Natural Language* (Synthese Library, 49), Dordrecht: Reidel, 221–242; reprinted in Portner and Partee (eds.) 2002, pp. 17–35.

[^montague-1964]: Montague, R. and Kalish, D., 1964, *Logic: Techniques of Formal Reasoning*, New York: Harcourt, Brace, and Jovanovich.

[^morrill-1994]: Morrill, G. V., 1994, *Type Logical Grammar. The Logic of Signs*, Dordrecht: Kluwer.

[^parsons-1981]: Parsons, T., 1981, “Frege’s Hierarchies of Indirect Senses and the Paradox of Analysis”, *Midwest Studies in Philosophy*, 6: 37–57.

[^parsons-1990]: –––, 1990, *Events in the semantics of English. A study in subatomic semantics*, Cambridge, MA: MIT Press.

[^partee-1973]: Partee, B. H., 1973, “Some transformational extensions of Montague grammar”, *Journal of Philosophical Logic*, 2: 509–534; reprinted in Partee 1976, pp. 51–76.

[^partee-1984]: –––, 1984, “Compositionality”, in F. Landman and F. Veltman (eds.), *Varieties of Formal Semantics: Proceedings of the 4th Amsterdam Colloquium* (Groningen-Amsterdam Studies in Semantics, No. 3), Dordrecht: Foris, pp. 281–311; reprinted in Partee 2004, pp. 153–181.

[^partee-1987]: –––, 1987, “Noun phrase interpretation and type-shifting principles”, in J. Groenendijk, D. de Jongh, and M. Stokhof (eds.), *Studies in Discourse Representation Theory and the Theory of Generalized Quantifiers* (Groningen-Amsterdam Studies in Semantics, 8), Dordrecht: Foris, pp. 115–143; reprinted in Partee 2004, pp. 203–224.

[^partee-1996]: –––, 1996, “The development of formal semantics in linguistic theory”, in Lappin (ed.) 1996, pp. 11–38.

[^partee-2004]: –––, 2004, *Compositionality in Formal Semantics. Selected Papers by B. H. Partee* (Explorations in Semantics 1), Malden, MA: Blackwell.

[^partee-2011]: –––, 2011, “Formal Semantics: Origins, Issues, Early Impact”, *Baltic International Yearbook of Cognition, Logic and Communication*, 6: 1–52.

[^partee-1997]: Partee, B. H. with Hendriks, H., 1997, “Montague grammar”, in van Benthem and ter Meulen (eds.) 1997, pp. 7–91; reprinted in van Benthem and ter Meulen (eds.) 2011, pp. 3–94

[^partee-1983]: Partee, B. and Rooth, M., 1983, “Generalized conjunction and type ambiguity”, in Bäuerle *et al*. (eds.) 1983, pp. 361–383; reprinted in Portner and Partee (eds.) 2002, pp. 334–356.

[^pelletier-1993]: Pelletier, F. J., 1993, “Remarks involving internal and external semantics”, in J. MacNamara and G. Reges (eds.), *The Logical Foundations of Cognition*, Oxford: Oxford University Press, 283–295.

[^pelletier-2003]: Pelletier, F. J. and Schubert, L. K., 2003, “Mass expressions”, in Gabbay and Guenthner (eds.) 2003, 249–335.

[^peters-1979]: Peters, S., 1979, “A truth-conditional formulation of Karttunen’s account of presupposition”, *Synthese*, 40: 301–316.

[^peters-2006]: Peters, S. and Westerståhl, D., 2006, *Quantifiers in Language and Logic*, Oxford: Oxford University Press.

[^portner-2002]: Portner, P. and Partee, B. (eds.), 2002, *Formal Semantics: the Essential Readings*, Oxford: Blackwell.

[^quine-1960]: Quine, W. V. O., 1960, *Word and Object*, Cambridge, MA: MIT Press.

[^rosetta-1994]: Rosetta, M. T., 1994, *Compositional Translation* (Kluwer International Series in Engineering and Computer Science, 230), Dordrecht: Kluwer.

[^russell-1905]: Russell, B., 1905, “On denoting”, *Mind*, 14: 175–226; reprinted in R. C. Marsh (ed.), *Logic and Knowledge. Essays 1901–1950*, New York: Macmillan, pp. 33–56.

[^stokhof-2007]: Stokhof, M., 2007, “Hand or hammer? On formal and natural languages in semantics”, *Journal of Indian Philosophy*, 35: 597–626.

[^tarski-1986]: Tarski, A., 1986, “What are logical notions?”, edited by J. Corcoran, *History and Philosophy of Logic*, 7: 143–154.

[^thomason-1974]: Thomason, R. H. (ed.), 1974, *Formal Philosophy. Selected Papers of Richard Montague*, New Haven: Yale University Press.

[^thomason-1980]: –––, 1980, “A Model Theory for Propositional Attitudes”, *Linguistics and Philosophy*, 4: 47–70.

[^turner-1983]: Turner, R., 1983, “Montague semantics, nominalizations and Scott’s domains”, *Linguistics and Philosophy*, 6: 259–288.

[^werning-2012]: Werning, M., Hinzen, W. and Machery, E. (eds.), 2012, *The Oxford Handbook of Compositionality*, Oxford: Oxford University Press

[^westerståhl-2002]: Westerståhl, D., 2002, “On the compositionality of idioms. An abstract approach”, in D. Barker-Plummer, D. I. Beaver, J. van Benthem, and P. S. di Luzio (eds.), *Words, Proofs and Diagrams* (CSLI Lecture Notes 141), Stanford: CSLI Publications, pp. 241–271.

[^winter-2001]: Winter, Y., 2001, *Flexibility Principles in Boolean Semantics: Coordination, Plurality and Scope in Natural Language* (Current Studies in Linguistics, 37), Cambridge, MA: MIT Press.

[^zadrozny-1994]: Zadrozny, W., 1994, “From compositional to systematic semantics”, *Linguistics and Philosophy*, 17: 329–342.

[^zimmermann-1983]: Zimmermann, T. E., 1983, “A Note on Transparency Postulates”, *Journal of Semantics*, 4: 67–77.

[^zimmermann-1989]: –––, 1989, “Intensional logic and two-sorted type theory”, *Journal of Symbolic Logic*, 54: 65–77.

[^zimmermann-1999]: –––, 1999, “Meaning postulates and the model-theoretic approach to natural language semantics”, *Linguistics and Philosophy*, 22: 529–561.

[^zimmermann-2021]: –––, 2021, “Representing intensionality”, in D. Gutzmann, L. Matthewson, C. Meier, H. Rullmann, and T. E. Zimmermann (eds.), *The Wiley Blackwell Companion to Semantics* (Volume 4), Hoboken: Wiley-Blackwell, pp. 2607–2643.

[^zimmermann-2022]: –––, 2022, “On Montague’s ‘The proper treatment of quantification in ordinary English’”, in L. McNally & Z. Szabó (eds.), 2022: 331–366.

[^zimmermann-2013]: Zimmermann, T. E. and Sternefeld, W., 2013, *Introduction to Semantics*, Berlin: De Gruyter.
