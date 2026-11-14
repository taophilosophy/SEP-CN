# Logical Constants
**First published Mon May 16, 2005; substantive revision Thu Jun 18, 2015**

*MacFarlane, John*

Logic is usually thought to concern itself only with features that sentences and arguments possess in virtue of their logical structures or *forms*. The logical form of a sentence or argument is determined by its syntactic or semantic structure and by the placement of certain expressions called “logical constants.”^{[[^note-1]]} Thus, for example, the sentences

Every boy loves some girl.

and

Some boy loves every girl.

are thought to differ in logical form, even though they share a common syntactic and semantic structure, because they differ in the placement of the logical constants “every” and “some”. By contrast, the sentences

Every girl loves some boy.

and

Every boy loves some girl.

are thought to have the same logical form, because “girl” and “boy” are not logical constants. Thus, in order to settle questions about logical form, and ultimately about which arguments are logically valid and which sentences logically true, we must distinguish the “logical constants” of a language from its nonlogical expressions.

While it is generally agreed that signs for negation, conjunction, disjunction, conditionality, and the first-order quantifiers should count as logical constants, and that words like “red”, “boy”, “taller”, and “Clinton” should not, there is a vast disputed middle ground. Is the sign for identity a logical constant? Are tense and modal operators logical constants? What about “true”, the epsilon of set-theoretic membership, the sign for mereological parthood, the second-order quantifiers, or the quantifier “there are infinitely many”? Is there a distinctive logic of agency, or of knowledge? In these border areas our intuitions from paradigm cases fail us; we need something more principled.

However, there is little philosophical consensus about the basis for the distinction between logical and nonlogical expressions. Until this question is resolved, we lack a proper understanding of the scope and nature of logic, and of the significance of the distinction between the “formal” properties and relations logic studies and related but non-formal ones. For example, the sentence

If Socrates is human and mortal, then he is mortal.

is generally taken to be a logical truth, while the sentence

If Socrates is orange, then he is colored.

is not, even though intuitively both are true, necessary, knowable *a priori*, and analytic. What is the significance of the distinction we are making between them in calling one but not the other “logically true”? A principled demarcation of logical constants might offer an answer to this question, thereby clarifying what is at stake in philosophical controversies for which it matters what counts as logic (for example, logicism and structuralism in the philosophy of mathematics).

This article will discuss the problem of logical constants and survey the main approaches to solving or resolving it.

## 1. Syncategorematic terms

The most venerable approach to demarcating the logical constants identifies them with the language’s *syncategorematic* signs: signs that signify nothing by themselves, but serve to indicate how independently meaningful terms are combined. This approach was natural in the context of the “term logics” that were dominant until the nineteenth century. All propositions were thought to be composed out of propositions of subject-predicate form by means of a small number of connectives (“and”, “or”, “if …then”, and so on). In this framework, words divide naturally into those that can be used as subjects or predicates (“categorematic” words) and those whose function is to indicate the relation between subject and predicate or between two distinct subject-predicate propositions (“syncategorematic” words). For example, “Socrates”, “runs”, “elephant”, and “large” are categorematic words, while “only”, “every”, “necessarily”, and “or” are syncategorematic. (For a more detailed account of the distinction, see Kretzmann 1982, 211–214.)[^kretzmann-1982] The syncategorematic words were naturally seen as indicating the *structure* or *form* of the proposition, while the categorematic words supplied its “matter.” Thus the fourteenth-century logician Buridan writes:

> I say that in a proposition (as we’re speaking here of matter and form), we understand by the “matter” of the proposition or *consequentia* the purely categorical terms, i.e. subjects and predicates, omitting the syncategorematic terms that enclose them and through which they are conjoined or negated or distributed or forced to a certain mode of supposition. All the rest, we say, pertains to the form. (Buridan 1976, I.7.2)[^buridan-1976]

The Fregean revolution in our conception of logical form made this way of demarcating the logical constants problematic. Whereas the term logicians had seen every proposition as composed of subject and predicate terms linked together by syncategorematic “glue,” Frege taught us to see sentences and propositions as built up recursively by functional application and functional abstraction (for a good account, see Dummett 1981, ch. 2)[^dummett-1981]. To see the difference between the two approaches, consider the sentence

$$\label{moby} \text{Every boat is smaller than Moby Dick.} $$

A term logician would have regarded $\refp{moby}$ as composed of a subject term (“boat”) and a predicate term (“thing smaller than Moby Dick”) joined together in a universal affirmative categorical form. Frege, by contrast, would have regimented $\refp{moby}$ as

$$\label{moby-frege} \forall x (x~\text{is a boat} \supset x~\text{is smaller than Moby Dick}) $$

which he would have analyzed as the result of applying the second-level function^{[[^note-2]]}

$$\label{second-level} \forall x (\Phi(x) \supset \Psi(x)) $$

to the first level functions

$$\label{function-boat} \xi~\text{is a boat} $$

and

$$\label{function-smaller} \xi~\text{is smaller than Moby Dick}. $$

(The Greek letters $\xi$, $\Phi$, and $\Psi$ here indicate the functions’ argument places: lowercase Greek letters indicate places that can be filled by proper names, while uppercase Greek letters indicate places that must be filled by function expressions like $\refp{function-boat}$ and $\refp{function-smaller}$.) He would have regarded $\refp{function-smaller}$ as itself the result of “abstracting” on the place occupied by “Shamu” in

$$\label{shamu-smaller} \text{Shamu is smaller than Moby Dick,} $$

which in turn is the result of applying the function

$$\label{smaller-than} \zeta~\text{is smaller than}~\xi $$

to “Shamu” and “Moby Dick”. Frege showed that by describing sentences and propositions this way, in terms of their function/argument composition, we can represent the logical relations between them in a far more complete, perspicuous, and systematic way than was possible with the old subject/predicate model of propositional form.

However, once we have thrown out the old subject/predicate model, we can no longer identify the categorematic terms with the subject and predicate terms, as the medievals did. Nor can we think of the syncategorematic terms as the expressions that have no “independent” significance, or as the “glue” that binds together the categorematic terms to form a meaningful whole. Granted, there is a sense in which the “logical” function $\refp{second-level}$ is the glue that binds together $\refp{function-boat}$ and $\refp{function-smaller}$ to yield $\refp{moby-frege}$. But in the very same sense, the function $\refp{smaller-than}$ is the glue that binds together “Shamu” and “Moby Dick” to yield $\refp{shamu-smaller}$. If we count all functional expressions as syncategorematic on the grounds that they are “incomplete” or “unsaturated” and thus not “independently meaningful,” then the syncategorematic expressions will include not just connectives and quantifiers, but ordinary predicates. On the other hand, if we count all the functional expressions as categorematic, then the syncategoremata will be limited to variables, parentheses, and other signs that serve to indicate functional application and abstraction. In neither case would the distinction be useful for demarcating the logical constants. An intermediate proposal would be to count first-level functions as categoremata and second-level functions as syncategoremata. That would make $\refp{second-level}$ syncategorematic and $\refp{function-boat}$ and $\refp{function-smaller}$ categorematic. However, not every second-level function is (intuitively) “logical.” Consider, for example, the second-level function

$$ \text{Every dog}~x~\text{such that}~\Phi(x)~\text{is such that}~\Psi(x). $$

Granted, standard logical languages do not have a simple expression for this function, but there is no reason in principle why we could not introduce such an expression. Conversely, not every first-level function is (intuitively) nonlogical: for example, the identity relation is usually treated as logical.

In sum, it is not clear how the distinction between categorematic and syncategorematic terms, so natural in the framework of a term logic, can be extended to a post-Fregean function/argument conception of propositional structure. At any rate, none of the natural ways of extending the distinction seem apt for the demarcation of the logical constants. Carnap concedes that the distinction between categorematic and syncategorematic expressions “seems more or less a matter of convention” (1947, 6–7). However, the idea that logical constants are syncategoremata does not wither away entirely with the demise of term logics. Its influence can still be felt in Wittgenstein’s insistence that the logical constants are like punctuation marks (1922, §5.4611),^{[[^note-3]]} in Russell’s claim that logical constants indicate logical form and not propositional constituents (1992, 98; 1920, 199), and in the idea (found in Quine and Dummett) that the logical constants of a language can be identified with its grammatical particles.

## 2. Grammatical criteria

Quine and Dummett propose that the logical constants of a language are its grammatical *particles*—the expressions by means of which complex sentences are built up, step by step, from atomic ones—while non-logical expressions are the simple expressions of which atomic sentences are composed (see Quine 1980, Quine 1986, Dummett 1981, 21–2, and for discussion, Føllesdal 1980 and Harman 1984)[^dummett-1981][^føllesdal-1980][^harman-1984][^quine-1980][^quine-1986]. On this conception, “[l]ogic studies the truth conditions that hinge solely on grammatical constructions” (Quine 1980, 17)[^quine-1980].^{[[^note-4]]} This criterion yields appropriate results when applied to the language of first-order logic (FOL) and other standard logical languages. In FOL (without identity), *all* singular terms and predicates are paradigm nonlogical constants, and *all* operators and connectives are paradigm logical constants.^{[[^note-5]]}

However, this nice coincidence of intuitively logical expressions and grammatical particles in FOL cannot be taken as support for the Quine/Dummett proposal, because FOL was *designed* so that its grammatical structure would reflect logical structure. It is easy enough to design other artificial languages for which the grammatical criterion gives intuitively inappropriate results. For example, take standard FOL and add a variable-binding operator “¢” whose interpretation is “there is at least one cat such that ….” The grammatical criterion counts “¢” as a logical constant, but surely it is not one.

Moreover, there are alternative ways of regimenting the grammar of FOL on which the standard truth-functional connectives are not grammatical particles, but members of a small lexical category (Quine 1986, 28–9)[^quine-1986]. For example, instead of recognizing four grammatical operations that form one sentence from two sentences (one that takes $P$ and $Q$ and yields $\cq{P \vee Q}$, one that takes $P$ and $Q$ and yields $\cq{P \and Q}$, and so on), we could recognize a single grammatical operation that forms one sentence from two sentences and one connective. On this way of regimenting the grammar of FOL, $\dq{\and}$ and $\dq{\vee}$ would not count as grammatical particles.

The upshot is that a grammatical demarcation of logical constants will not impose significant constraints on what counts as a logical constant unless it is combined with some principle for limiting the languages to which it applies (excluding, for example, languages with the operator “¢”) and privileging some regimentations of their grammars over others (excluding, for example, regimentations that treat truth-functional connectives as members of a small lexical category). Quine’s own approach is to privilege the language best suited for the articulation of scientific theories and the grammar that allows the most economical representation of the truth conditions of its sentences. Thus the reason Quine holds that logic should restrict itself to the study of inferences that are truth-preserving in virtue of their grammatical structures is not that he thinks there is something special about the grammatical particles (in an arbitrary language), but rather that he thinks we should employ a language in which grammatical structure is a perspicuous guide to truth conditions: “what we call logical form is what grammatical form becomes when grammar is revised so as to make for efficient general methods of exploring the interdependence of sentences in respect of their truth values” (1980, 21).

Instead of applying the grammatical criterion to artificial languages like FOL, one might apply it to natural languages like English. One could then appeal to the work of empirical linguists for a favored grammatical regimentation. Contemporary linguists posit a structural representation called LF that resolves issues of scope and binding crucial to semantic evaluation. But the question remains which lexical items in the LF should count as logical constants. Generalizing Quine’s proposal, one might identify the logical constants with members of small, “closed” lexical categories: for example, conjunctions and determiners. However, by this criterion prepositions in English would count as logical constants (Harman 1984, 121)[^harman-1984]. Alternatively, one might identify the logical constants with members of *functional categories* (including tense, complementizers, auxiliaries, determiners, and pronouns), and the nonlogical constants with members of *substantive categories* (including nouns, verbs, adjectives, adverbs, and prepositions) (for this terminology, see Chomsky 1995, 6, 54 and Radford 2004, 41)[^chomsky-1995][^radford-2004]. If a distinction that plays an important role in a theory of linguistic competence should turn out to coincide (in large part) with our traditional distinction between logical and nonlogical constants, then this fact would stand in need of explanation. Why should we treat inferences that are truth-preserving in virtue of their LF structures and functional words differently from those that are truth-preserving in virtue of their LF structures and substantive words? Future work in linguistics, cognitive psychology and neurophysiology may provide the materials for an interesting answer to this question, but for now it is important that the question be asked, and that we keep in mind the possibility of a sceptical answer.

## 3. A Davidsonian approach

The Quinean approach identifies the logical constants as the expressions that play a privileged, “structural” role in a systematic grammatical theory for a language. An alternative approach, due to Quine’s student Donald Davidson, identifies the logical constants as the expressions that play a privileged, “structural” role in a systematic theory of *meaning* for a language. A Davidsonian theory of meaning takes the form of a Tarskian truth theory. Thus, it contains two kinds of axioms: *base clauses* that specify the satisfaction conditions of atomic sentences,^{[[^note-6]]} and *recursive clauses* that specify the satisfaction conditions of complex sentences in terms of the satisfaction conditions of their proper parts.^{[[^note-7]]} For example:

*Base Clauses:*

- For all assignments $a$, Ref(“Bill Clinton”, $a$) = Bill Clinton.
- For all assignments $a$, Ref(“Hilary Clinton”, $a$) = Hilary Clinton.
- If $\upsilon$ is a variable, then for all assignments $a$, Ref($\upsilon$, $a$) = $a(\upsilon)$, the value $a$ assigns to $\upsilon$.
- For all terms $\tau$, $\sigma$, and all assignments $a$, $\cq{\tau \text{ is taller than } \sigma}$ is satisfied by $a$ iff Ref($\tau$, $a$) is taller than Ref($\sigma$, $a$).

*Recursive Clauses:*

- For all assignments $a$ and all sentences $\phi, \psi$, $\cq{\phi \text{ or } \psi}$ is satisfied by $a$ iff $\phi$ is satisfied by $a$ or $\psi$ is satisfied by $a$.
- For all assignments $a$, all sentences $\phi, \psi$, and all variables $\upsilon$, $\cq{[\text{Some}~\upsilon : \phi]~\psi }$ is satisfied by $a$ iff there is an assignment $a'$ that differs from $a$ at most in the value it assigns to $\upsilon$, satisfies $\phi$, and satisfies $\psi$.

Davidson suggests that “[t]he logical constants may be identified as those iterative features of the language that require a recursive clause in the characterization of truth or satisfaction” (1984, 71). (In our example, “or” and “some”.)

This criterion certainly gives reasonable results when applied to standard truth theories like the one above (although the sign for identity once more gets counted as nonlogical). But as Davidson goes on to observe, “[l]ogical form, in this account, will of course be relative to the choice of a metalanguage (with its logic) and a theory of truth” (1984, 71). Different truth theories can be given for the same language, and they can agree on the truth conditions of whole sentences while differing in which expressions they treat in the recursive clauses. Here are two examples (both discussed further in Evans 1976)[^evans-1976].

1. We might have recursive clauses for “large” and other gradable adjectives, along these lines:

For all assignments $a$, terms $\tau$, and sentences $\phi$, $\cq{\tau \text{ is a large } \phi }$ is satisfied by $a$ iff Ref($\tau$, $a$) is a large satisfier of $\phi$ on $a$. (cf. Evans 1976, 203)[^evans-1976]

We would in this case have to use a metalanguage with a stronger logic, one that provides rules for manipulating “large satisfier of $\phi$ on $a$.” (As Evans notes, all we would really need in order to derive T-sentences would be a rule licensing the derivation of $\cq{\tau \text{ is a large satisfier of } \phi \text{ on } a}$ from $\cq{\phi \equiv \psi}$ and $\cq{\tau \text{ is a larger satisfier of } \psi \text{ on } a}$.) But such a metalanguage cannot be ruled out without begging the question about the logicality of “large.”

2. We might assign values to “and”, “or”, and the other truth-functional connectives in the *base* clauses, allowing us to get by with a single generic recursive clause for truth-functional connectives:

*Base:* For all assignments $a$, Ref(“or”, $a$) = Boolean disjunction (the binary truth function that takes the value True when either argument is True, and False otherwise).

*Recursive:* For all assignments $a$, sentences $\phi, \psi$, and truth-functional connectives $@$, $\cq{\phi @ \psi }$ is satisfied by $a$ iff Ref($@, a$)(Val($\phi, a$), Val($\psi,a$)) = True (where Val($\phi, a$) = True if $\phi$ is satisfied by $a$, False if $\phi$ is not satisfied by $a$). (cf. Evans 1976, 214)[^evans-1976]

This approach requires a stronger metatheory than the usual approach, since it requires quantification over truth functions. But it is not clear why this is an objection. It is still possible to derive T-sentences whose right sides are no more ontologically committed than the sentences named on their left sides, like

$$ \text{“Snow is white or grass is green” is } \mathrm{true} \\ \text{ iff snow is white or grass is green}. $$

So it is hard to see how the use of functions here is any more objectionable than Davidson’s own appeal to sequences or assignments of values to variables.

In sum, the problem with Davidson’s truth-theoretic proposal is much like the problem discussed above with Quine’s grammatical proposal. Without further constraints on the theory of meaning (or, in Quine’s case, the grammar), it does not yield a definite criterion for logical constancy. I do not mean to suggest that either Davidson or Quine was deluded on this score. As we saw above, Quine appeals to pragmatic considerations to pick out a favored language and grammatical regimentation. No doubt Davidson would do the same, arguing (for example) that the advantages of using a simple and well-understood logic in the metalanguage outweigh any putative advantages of treating “large” and the like in recursive clauses. (For a recent defense of a Davidsonian criterion against Evans’s objections, see Lepore and Ludwig 2002.)[^lepore-2002]

## 4. Topic neutrality

Logic, it seems, is not about anything in particular; relatedly, it is applicable everywhere, no matter what we are reasoning about. So it is natural to suppose that the logical constants can be marked out as the “topic-neutral” expressions (Ryle 1954, 116; Peacocke 1976, 229; Haack 1978, 5–6; McCarthy 1981, 504; Wright 1983, 133; Sainsbury 2001, 365)[^haack-1978][^mccarthy-1981][^peacocke-1976][^ryle-1954][^sainsbury-2001][^wright-1983]. We have reason to care about the topic-neutral expressions, and to treat them differently from others, because we are interested in logic as a *universal* canon for reasoning, one that is applicable not just to reasoning about this or that domain, but to all reasoning.

Unfortunately, the notion of topic neutrality is too vague to be of much help when it comes to the hard cases for which we *need* a principle of demarcation. Take arithmetic, for instance. Is it topic-neutral? Well, yes: anything can be counted, so the theorems of arithmetic will be useful in any field of inquiry. But then again, no: arithmetic has its own special subject matter, the natural numbers and the arithmetical relations that hold between them. The same can be said about set theory: on the one hand, anything we can reason about can be grouped into sets; on the other hand, set theory seems to be about a particular corner of the universe—the sets—and thus to have its own special “topic.” The general problem of which these two cases are instances might be called the *antinomy of topic-neutrality*. As George Boolos points out, the antinomy can be pressed all the way to paradigm cases of logical constants: “it might be said that logic is not so ‘topic-neutral’ as it is often made out to be: it can easily be said to be about the notions of negation, conjunction, identity, and the notions expressed by ‘all’ and ‘some’, among others …” (1975, 517). It is plausible to think that the source of the antinomy is the vagueness of the notion of topic neutrality, so let us consider some ways in which we might make this notion more precise.

Gilbert Ryle, who seems to have coined the expression “topic-neutral”, gives the following rough criterion:

> We may call English expressions “topic-neutral” if a foreigner who understood them, but only them, could get no clue at all from an English paragraph containing them what that paragraph was about. (1954, 116)^{[[^note-8]]}

There are, I suppose, a few paradigm cases of such expressions: “is”, for instance, and “if”. But the criterion gives little help when we venture beyond these clear-cut cases. The problem is that one might answer the question “what is this paragraph about?” at many different levels of generality. Suppose I understand English badly, and I hear someone say:

> blah blah blah *and not* blah blah blah *because it* blah blah blah *to be* blah blah blah *and was always* blah blah blah. *But every* blah blah *is* blah blah, *although a few* blah blah *might be* blah.

Do I have any clue as to what the paragraph is about? Well, surely I have *some* clue. “Because” reveals that the passage is about causal or explanatory relations. “It” reveals that the passage is about at least one object that is not known to be a person. The tense operator “was always” reveals that it is about events that occur in time. “Might be” reveals that it is about the realm of the possible (or the unknown), and not just the actual (or the known). Finally, “every” and “a few” reveal that it is about discrete, countable objects. Perhaps some of these words are not topic-neutral and should not be included in the domain of logic, but we certainly don’t want to rule out *all* of them. And Ryle’s criterion gives no guidance about where to draw the line. One might even suspect that there is no line, and that topic neutrality is a matter of degree, truth-functional expressions being more topic-neutral than quantifiers, which are more topic-neutral than tense and modal operators, which are more topic-neutral than epistemic expressions, and so on (Lycan 1989)[^lycan-1989].

The problem with Ryle’s account is its reliance on vague and unclarified talk of “aboutness.” If we had a precise philosophical account of what it is for a statement to be *about* a particular object or subject matter, then we could define a topic-neutral statement as one that is not about anything—or, perhaps, one that is about everything indifferently. Here we might hope to appeal to Nelson Goodman’s classic account of “absolute aboutness,” which implies that logical truths are not absolutely about anything (1961, 256), or to David Lewis’s (1988)[^lewis-1988] account of what it is for a proposition to be about a certain subject matter, which implies that logical truths are about *every* subject matter indifferently. However, neither account is appropriate for our purpose. On Goodman’s account, “what a statement is absolutely about will depend in part upon what logic is presupposed,” and hence upon which expressions are taken to be logical constants (253–4), so it would be circular to appeal to Goodman’s account of aboutness in a demarcation of the logical constants. On Lewis’s account, *all* necessarily true propositions turn out to be topic-neutral. But if there is any point to invoking topic neutrality in demarcating logic, it is presumably to distinguish the logical truths from a wider class of necessary propositions, some of which are subject matter-specific. If we are willing to broaden the bounds of logic to encompass all necessary propositions (or, alternatively, all analytic sentences), then we might as well demarcate logic as the realm of necessary truth (alternatively, analytic truth). It is only if we want to *distinguish* the logical from the generically necessary, or to demarcate logic without appealing to modal notions at all, that we need to invoke topic neutrality. And in neither of these cases will Lewis’s criterion of aboutness be of service.

We rejected Ryle’s criterion for topic-neutrality because it appealed to an unclarified notion of aboutness. We rejected Goodman’s explication of aboutness because it assumed that the line between logic and non-logic had already been drawn. And we rejected Lewis’s account of aboutness because it did not distinguish logical truths from other kinds of necessary truths. How else might we cash out the idea that logic is “not about anything in particular”? Two approaches have been prominent in the literature.

The first starts from the idea that what makes an expression specific to a certain domain or topic is its capacity to *discriminate* between different individuals. For example, the monadic predicate “is a horse”, the dyadic predicate “is taller than”, and the quantifier “every animal” all distinguish between Lucky Feet, on the one hand, and the Statue of Liberty, on the other:

- “Lucky Feet is a horse” is true; “The Statue of Liberty is a horse” is false.
- “The Statue of Liberty is taller than Lucky Feet” is true; “Lucky Feet is taller than the Statue of Liberty” is false.
- The truth of “Every animal is healthy” depends on whether Lucky Feet is healthy, but not on whether the Statue of Liberty is healthy.

On the other hand, the monadic predicate “is a thing”, the dyadic predicate “is identical with”, and the quantifier “everything” do not distinguish between Lucky Feet and the Statue of Liberty. In fact, they do not distinguish between *any* two particular objects. As far as they are concerned, one object is as good as another and might just as well be switched with it. Expressions with this kind of indifference to the particular identities of objects might reasonably be said to be topic-neutral. As we will see in the next section, this notion of topic neutrality can be cashed out in a mathematically precise way as invariance under arbitrary permutations of a domain. It is in this sense that the basic concepts of arithmetic and set theory are not topic-neutral, since they distinguish some objects (the empty set, the number 0) from others.

The second approach locates the topic neutrality of logic in its universal applicability. On this conception, logic is useful for the guidance and criticism of reasoning about any subject whatsoever—natural or artefactual, animate or inanimate, abstract or concrete, normative or descriptive, sensible or merely conceptual—because it is intimately connected somehow with the very conditions for thought or reasoning. This notion of topic neutrality is not equivalent to the one just discussed. It allows that a science with its own proprietary domain of objects, like arithmetic or set theory, might still count as topic-neutral in virtue of its completely general applicability. Thus, Frege, who took arithmetic to be about numbers, which he regarded as genuine objects, could still affirm its absolute topic neutrality:

> …the basic propositions on which arithmetic is based cannot apply merely to a limited area whose peculiarities they express in the way in which the axioms of geometry express the peculiarities of what is spatial; rather, these basic propositions must extend to everything that can be thought. And surely we are justified in ascribing such extremely general propositions to logic. (1885, 95, in Frege 1984; for further discussion, see MacFarlane 2002)[^frege-1984][^macfarlane-2002]

The tradition of demarcating the logical constants as expressions that can be characterized by purely inferential introduction and elimination rules can be seen as a way of capturing this notion of completely general applicability. For, plausibly, it is the fact that the logical constants are characterizable in terms of notions fundamental to thought or reasoning (for example, valid inference) that accounts for their universal applicability.

The antinomy with which we started can now be resolved by disambiguating. Arithmetic and set theory make distinctions among objects, and so are not topic-neutral in the first sense, but they might still be topic-neutral in the second sense, by virtue of their universal applicability to reasoning about any subject. We are still faced with a decision about which of these notions of topic neutrality is distinctive of logic. Let us postpone this problem, however, until we have had a closer look at both notions.

## 5. Permutation invariance

A number of philosophers have suggested that what is distinctive of logical constants is their insensitivity to the particular identities of objects, or, more precisely, their *invariance* under arbitrary permutations of the domain of objects (Mautner 1946; Mostowski 1957, 13; Scott 1970, 160–161; McCarthy 1981, 1987; Tarski 1986; van Benthem 1989; Sher 1991, 1996; McGee 1996)[^mautner-1946][^mccarthy-1981][^mccarthy-1987][^mcgee-1996][^mostowski-1957][^scott-1970][^sher-1991][^sher-1996][^tarski-1986][^benthem-1989].

Let us unpack that phrase a bit. A *permutation* of a collection of objects is a one-one mapping from that collection onto itself. Each object gets mapped to an object in the collection (possibly itself), and no two objects are mapped to the same object. For example, the following mapping is a permutation of the first five letters of the alphabet:

$$\begin{align*} \textrm{A} &\Rightarrow \textrm{C} \\ \textrm{B} &\Rightarrow \textrm{B} \\ \textrm{C} &\Rightarrow \textrm{E} \\ \textrm{D} &\Rightarrow \textrm{A} \\ \textrm{E} &\Rightarrow \textrm{D} \\ \end{align*}$$

And the function $f(x) = x + 1$ is a permutation of the set of integers onto itself. (Note, however, that a permutation need not be specifiable either by enumeration, as in our first example, or by a rule, as in our second.)

The extension of a predicate is invariant under a permutation of the domain if replacing each of its members with the object to which the permutation maps it leaves us with the same set we started with. Thus, for example, the extension of “is a letter between $\textrm{A}$ and $\textrm{E}$” is invariant under the permutation of letters described above. By contrast, the extension of “is a vowel between $\textrm{A}$ and $\textrm{E}$”, the set $\{\textrm{A}, \textrm{E}\}$, is not invariant under this permutation, which transforms it to a different set, $\{\textrm{C}, \textrm{D}\}$.

We can make the notion of permutation invariance more precise as follows. Given a permutation $p$ of objects on a domain $D$, we define a transformation $p^*$ of arbitrary types in the hierarchy:

- if $x$ is an object in $D$, $p^*(x) = p(x)$.
- if $x$ is a set, then $p^*(x) = \{ y : \exists z (z \in x \and y = p^*(z))\}$ (that is, the set of objects to which $p^*$ maps members of $x$).
- if $x$ is an ordered $n$-tuple $\langle x_1, \dots, x_n \rangle$, then $p^*(x) = \langle p^*(x_1), \dots, p^*(x_n) \rangle$ (that is, the $n$-tuple of objects to which $p^*$ maps $x_1, \dots, x_n$).^{[[^note-9]]}

These clauses can be applied recursively to define transformations of sets of ordered tuples in $D$ (the extensions of two-place predicates), sets of sets of objects in $D$ (the extensions of unary first-order quantifiers), and so on. (For an introduction to the type theoretic hierachy, see the entry on Type Theory.) Where $x$ is an item in this hierarchy, we say that $x$ is *invariant under* a permutation $p$ just in case $p^*(x) = x$. To return to our example above, the set $\{\textrm{A}, \textrm{B}, \textrm{C}, \textrm{D}, \textrm{E}\}$ is invariant under all permutations of the letters $\textrm{A}$ through $\textrm{E}$: no matter how we switch these letters around, we end up with the same set. But it is not invariant under all permutations of the entire alphabet. For example, the permutation that switches the letters $\textrm{A}$ and $\textrm{Z}$, mapping all the other letters to themselves, transforms $\{\textrm{A}, \textrm{B}, \textrm{C}, \textrm{D}, \textrm{E}\}$ to $\{\textrm{Z}, \textrm{B}, \textrm{C}, \textrm{D}, \textrm{E}\}$. The set containing all the letters, however, is invariant under all permutations of letters. So is the set of all sets containing at least two letters, and the relation of identity, which holds between each letter and itself.

So far we have defined permutation invariance for objects, tuples, and sets, but not for predicates, quantifiers, or other linguistic expressions. But it is the latter, not the former, that we need to sort into logical and nonlogical constants. The natural thought is that an expression should count as permutation-invariant just in case its extension on each domain of objects is invariant under all permutations of that domain. (As usual, the extension of a name on a domain is the object it denotes, the extension of a monadic predicate is the set of objects in the domain to which it applies, and the extension of an $n$-adic predicate is the set of $n$-tuples of objects in the domain to which it applies.) As it stands, this definition does not apply to sentential connectives, which do not have extensions in the usual sense,^{[[^note-10]]} but it can be extended to cover them in a natural way (following McGee 1996, 569)[^mcgee-1996]. We can think of the semantic value of an $n$-ary quantifier or sentential connective $C$ on a domain $D$ as a function from $n$-tuples of sets of assignments (of values from $D$ to the language’s variables) to sets of assignments. Where the input to the function is the $n$-tuple of sets of assignments that satisfy $\phi_1, \dots, \phi_n$, its output is the set of assignments that satisfies $C\phi_1 \dots \phi_n$. (Check your understanding by thinking about how this works for the unary connective $\exists x$.) We can then define permutation invariance for these semantic values as follows. Where $A$ is a set of assignments and $p$ is a permutation of a domain $D$, let $p^\dagger(A) = \{ p \circ a : a \in A\}$.^{[[^note-11]]} Then if $e$ is the semantic value of an $n$-place connective or quantifier (in the sense defined above), $e$ is invariant under a permutation $p$ just in case for any $n$-tuple $\langle A_1, \dots, A_n \rangle$ of sets of assignments, $p^\dagger (e(\langle A_1, \dots, A_n\rangle)) = e(\langle p^\dagger (A_1), \dots, p^\dagger (A_n)\rangle$). And a connective or quantifier is permutation-invariant just in case its semantic value on each domain of objects is invariant under all permutations of that domain.

It turns out that this condition does not quite suffice to weed out *all* sensitivity to particular features of objects, for it allows that a permutation-invariant constant might behave differently on domains containing different kinds of objects. McGee (1996, 575)[^mcgee-1996] gives the delightful example of *wombat disjunction*, which behaves like disjunction if the domain contains wombats and like conjunction otherwise. Sher’s fix, and McGee’s, is to consider not just permutations—bijections of the domain onto itself—but arbitrary bijections of the domain onto another domain of equal cardinality.^{[[^note-12]]} For simplicity, we will ignore this complication in what follows and continue to talk of permutations.

Which expressions get counted as logical constants, on this criterion? The monadic predicates “is a thing” (which applies to everything) and “is not anything” (which applies to nothing), the identity predicate, the truth-functional connectives, and the standard existential and universal quantifiers all pass the test. So do the standard first-order binary quantifiers like “most” and “the” (see the entry on descriptions). Indeed, because cardinality is permutation-invariant, every cardinality quantifier is included, including “there are infinitely many”, “there are uncountably many”, and others that are not first-order definable. Moreover, the second-order quantifiers count as logical (at least on the standard semantics, in which they range over arbitrary subsets of the domain), as do all higher-order quantifiers. On the other hand, all proper names are excluded, as are the predicates “red”, “horse”, “is a successor of”, and “is a member of”, as well as the quantifiers “some dogs” and “exactly two natural numbers”. So the invariance criterion seems to accord at least partially with common intuitions about logicality or topic neutrality, and with our logical practice. Two technical results allow us to be a bit more precise about the extent of this accord: Lindenbaum and Tarski (1934–5) show that all of the relations definable in the language of *Principia Mathematica* are permutation-invariant. Moving in the other direction, McGee (1996)[^mcgee-1996] shows that every permutation-invariant operation can be defined in terms of operations with an intuitively logical character (identity, substitution of variables, finite or infinite disjunction, negation, and finite or infinite existential quantification). He also generalizes the Lindenbaum-Tarski result by showing that every operation so definable is permutation invariant.

As Tarski and others have pointed out, the permutation invariance criterion for logical constants can be seen as a natural generalization of Felix Klein’s (1893)[^klein-1893] idea that different geometries can be distinguished by the groups of transformations under which their basic notions are invariant. Thus, for example, the notions of Euclidean geometry are invariant under similarity transformations, those of affine geometry under affine transformations, and those of topology under bicontinuous transformations. In the same way, Tarski suggests (1986, 149), the *logical* notions are just those that are invariant under the widest possible group of transformations: the group of *permutations* of the elements in the domain. Seen in this way, the logical notions are the end point of a chain of progressively more abstract, “formal,” or topic-neutral notions defined by their invariance under progressively wider groups of transformations of a domain.^{[[^note-13]]}

As an account of the distinctive generality of logic, then, permutation invariance has much to recommend it. It is philosophically well-motivated and mathematically precise, it yields results that accord with common practice, and it gives determinate rulings about some borderline cases (for example, set-theoretic membership). Best of all, it offers hope for a sharp and principled demarcation of logic that avoids cloudy epistemic and semantic terms like “about”, “analytic”, and “*a priori*”.^{[[^note-14]]}

A limitation of the permutation invariance criterion (as it has been stated so far) is that it applies only to extensional operators and connectives. It is therefore of no help in deciding, for instance, whether the necessity operator in S4 modal logic or the *H* operator (“it has always been the case that”) in temporal logic are bona fide logical constants, and these are among the questions that we wanted a criterion to resolve. However, the invariance criterion can be extended in a natural way to intensional operators. The usual strategy for handling such operators semantically is to relativize truth not just to an assignment of values to variables, but also to a possible world and a time. In such a framework, one might demand that logical constants be insensitive not just to permutations of the domain of objects, but to permutations of the domain of possible worlds and the domain of times (see Scott 1970, 161, McCarthy 1981, 511–13, van Benthem 1989, 334)[^mccarthy-1981][^scott-1970][^benthem-1989]. The resulting criterion is fairly stringent: it counts the S5 necessity operator as a logical constant, but not the S4 necessity operator or the *H* operator in temporal logic. The reason is that the latter two operators are sensitive to *structure* on the domains of worlds and times—the “accessibility relation” in the former case, the relation of temporal ordering in the latter—and this structure is not preserved by all permutations of these domains.^{[[^note-15]]} (See the entries on modal logic and temporal logic.)

One might avoid this consequence by requiring only invariance under permutations that preserve the relevant structure on these domains (accessibility relations, temporal ordering). But one would then be faced with the task of explaining why *this* structure deserves special treatment (cf. van Benthem 1989, 334)[^benthem-1989]. And if we are allowed to keep some structure on the domain of worlds or times fixed, the question immediately arises why we should not also keep some structure on the domain of *objects* fixed: for example, the set-theoretic membership relation, the mereological part/whole relation, or the distinction between existent and nonexistent objects (see the entry on free logics). Whatever resources we appeal to in answering this question will be doing at least as much work as permutation invariance in the resulting demarcation of logical constants.

It may seem that the only principled position is to demand invariance under *all* permutations. But even that position needs justification, especially when one sees that it is possible to formulate even stricter invariance conditions. Feferman (1999)[^feferman-1999] defines a “similarity invariance” criterion that counts the truth-functional operators and first-order existential and universal quantifiers as logical constants, but not identity, the first-order cardinality quantifiers, or the second-order quantifiers. Feferman’s criterion draws the line between logic and mathematics much closer to the traditional boundary than the permutation invariance criterion does. Indeed, one of Feferman’s criticisms of the permutation invariance criterion is that it allows too many properly mathematical notions to be expressed in purely logical terms. Bonnay (2008)[^bonnay-2008] argues for a different criterion, invariance under potential isomorphism, which counts finite cardinality quantifiers and the notion of finiteness as logical, while excluding the higher cardinality quantifiers—thus “[setting] the boundary between logic and mathematics somewhere between arithmetic and set theory” (37; see Feferman 2010, §6, for further discussion)[^feferman-2010]. Feferman (2010)[^feferman-2010] suggests that instead of relying solely on invariance, we might combine invariance under permutations with a separate *absoluteness* requirement, which captures the insensitivity of logic to controversial set-theoretic theses like axioms of infinity. He shows that the logical operations that are both permutation-invariant and absolutely definable with respect to Kripke–Platek set theory without an axiom of infinity are just those definable in first-order logic.

There is another problem that afflicts any attempt to demarcate the logical constants by appeal to mathematical properties like invariance. As McCarthy puts it: “the logical status of an expression is not settled by the functions it introduces, independently of how these functions are *specified*” (1981, 516). Consider a two-place predicate $\dq{\approx}$, whose meaning is given by the following definition:

$$ \cq{\alpha \approx \beta }\text{ is true on an assignment } a \text{ just in case }\\ a(\alpha) \text{ and } a(\beta) \text{ have exactly the same mass.} $$

According to the invariance criterion, $\dq{\approx}$ is a logical constant just in case its extension on every domain is invariant under every permutation of that domain. On a domain $D$ containing no two objects with exactly the same mass, $\dq{\approx}$ has the same extension as $\dq{=}$—the set $\{ \langle x, x \rangle : x \in D\}$—and as we have seen, this extension is invariant under every permutation of the domain. Hence, if there is *no* domain containing two objects with exactly the same mass, $\dq{\approx}$ counts as a logical constant, and $\dq{\forall x (x \approx x)}$ as a logical truth.^{[[^note-16]]} But it seems odd that the logical status of $\dq{\approx}$ and $\dq{\forall x (x \approx x)}$ should depend on a matter of contingent fact: whether there are distinct objects with identical mass. Do we really want to say that if we lived in a world in which no two objects had the same mass, $\dq{\approx}$ would be a logical constant?^{[[^note-17]]}

A natural response to this kind of objection would be to require that the extension of a logical constant on every *possible* domain of objects be invariant under every permutation of that domain, or, more generally, that a logical constant satisfy the permutation invariance criterion as a matter of *necessity*. But this would not get to the root of the problem. For consider the unary connective $\dq{\#}$, defined by the clause

$$ \cq{\#\phi}~\text{is true on an assignment } a \text{ just in case }\\ \phi \text{ is not true on } a \text { and water is } H_{2}O. $$

Assuming that Kripke (1971; 1980)[^kripke-1971][^kripke-1980] is right that water is *necessarily* H_{2}O, $\dq{\#}$ has the same extension as $\dq{\neg}$ in every possible world, and so satisfies the permutation invariance criterion as a matter of necessity (McGee 1996, 578)[^mcgee-1996]. But intuitively, it does not seem that $\dq{\#}$ should be counted a logical constant.^{[[^note-18]]}

One might evade this counterexample by appealing to an *epistemic* modality instead of a metaphysical one. This is McCarthy’s strategy (1987, 439). Even if it is metaphysically necessary that water is H_{2}O, there are presumably epistemically possible worlds, or information states, in which water is not H_{2}O. So if we require that a logical constant be permutation invariant as a matter of epistemic necessity (or *a priori*), $\dq{\#}$ does not count as a logical constant. But even on this version of the criterion, a connective like $\dq{\%}$, defined by

$$ \cq{\%\phi}~\text{is true on an assignment } a \text{ just in case }\\ \phi \text { is not true on } a \text{ and there are no male widows.} $$

would count as a logical constant (Gómez-Torrente 2002, 21)[^gómez-torrente-2002], assuming that it is epistemically necessary that there are no male widows. It may be tempting to solve *this* problem by appealing to a distinctively *logical* modality—requiring, for example, that logical constants have permutation-invariant extensions as a matter of *logical* necessity. But we would then be explicating the notion of a logical constant in terms of an obscure primitive notion of logical necessity which we could not, on pain of circularity, explicate by reference to logical constants. (McCarthy 1998, §3 appeals explicitly to logical possibility and notices the threat of circularity here.)[^mccarthy-1998]

McGee’s strategy is to invoke semantic notions instead of modal ones: he suggests that “[a] connective is a logical connective if and only if it follows from the meaning of the connective that it is invariant under arbitrary bijections” (McGee 1996, 578)[^mcgee-1996]. But this approach, like McCarthy’s, seems to count $\dq{\%}$ as a logical constant. And, like McCarthy’s, it requires appeal to a notion that does not seem any clearer than the notion of a logical constant: the notion of following (logically?) from the meaning of the connective.

Sher’s response to the objection is radically different from McGee’s or McCarthy’s. She suggests that “logical terms are identified with their (actual) extensions,” so that $\dq{\#}$, $\dq{\%}$, and $\dq{\neg}$ are just different notations for the same term. More precisely: if these expressions are used the way a logical constant must be used—as rigid designators^{[[^note-19]]} of their semantic values—then they can be identified with the operation of Boolean negation and hence with each other. “Qua quantifiers, ‘the number of planets’ and ‘9’ are indistinguishable” (Sher 1991, 64)[^sher-1991]. But it is not clear what Sher can mean when she says that logical terms can be identified with their extensions. We normally individuate connectives *intentionally*, by the conditions for grasping them or the rules for their use, and not by the truth functions they express. For example, we recognize a difference between $\dq{\and}$, defined by

$$ \cq{\phi \and \psi } \text{ is true on an assignment \(a\) just in case}\\ \phi \text{ is true on \(a\) and \(\psi\) is true on \(a\)}, $$

and $\dq{@}$, defined by

$$ \cq{\phi\ @\ \psi } \text{ is true on an assignment \(a\) just in case}\\ \text{it is not the case either that \(\phi\) is not true on \(a\)}\\ \text{or that \(\psi\) is not true on \(a\)}, $$

even though they express the same truth function. The distinction between these terms is not erased, as Sher seems to suggest, if we use them as rigid designators for the truth functions they express. (That “Hesperus”, “Phosphorus”, and “the planet I actually saw near the horizon on the morning of November 1, 2004” all rigidly designate Venus does not entail that they have the same meaning.) Thus Sher’s proposal can only be understood as a *stipulation* that if one of a pair of coreferential rigid designators counts as a logical constant, the other does too. But it is not clear why we should accept this stipulation. It certainly has some counterintuitive consequences: for example, that $\dq{P \vee \#P}$ is a logical truth, at least when $\dq{\#}$ is used rigidly (see Gómez-Torrente 2002, 19, and the response in Sher 2003)[^gómez-torrente-2002][^sher-2003].

It is hard not to conclude from these discussions that the permutation invariance criterion gives at best a necessary condition for logical constancy. Its main shortcoming is that it operates at the level of reference rather than the level of sense; it looks at the logical operations expressed by the constants, but not at their meanings. An adequate criterion, one might therefore expect, would operate at the level of sense, perhaps attending to the way we *grasp* the meanings of logical constants.

## 6. Inferential characterizations

At the end of the section on topic neutrality, we distinguished two notions of topic neutrality. The first notion—insensitivity to the distinguishing features of individuals—is effectively captured by the permutation invariance criterion. How might we capture the second—universal applicability to all thought or reasoning, regardless of its subject matter? We might start by identifying certain ingredients that must be present in anything that is to count as thought or reasoning, then class as logical any expression that can be understood in terms of these ingredients alone. That would ensure a special connection between the logical constants and thought or reasoning as such, a connection that would explain logic’s universal applicability.

Along these lines, it has been proposed that the logical constants are just those expressions that can be characterized by a set of purely inferential introduction and elimination rules.^{[[^note-20]]} To grasp the meaning of the conjunction connective $\dq{\and}$, for example, it is arguably sufficient to learn that it is governed by the rules: \begin{equation*} \frac{A, B}{A \and B} \quad \frac{A \and B}{A} \quad \frac{A \and B}{B} \end{equation*} Thus the meaning of $\dq{\and}$ can be grasped by anyone who understands the significance of the horizontal line in an inference rule. (Contrast $\dq{\%}$ from the last section, which cannot be grasped by anyone who does not understand what a male is and what a widow is.) Anyone who is capable of articulate thought or reasoning at all should be able to understand these inference rules, and should therefore be in a position to grasp the meaning of $\dq{\and}$. Or so the thought goes.^{[[^note-21]]}

To make such a proposal precise, we would have to make a number of additional decisions:

- We would have to decide whether to use natural deduction rules or sequent rules. (See the entry on the development of proof theory.)
- If we opted to use sequent rules, we would have to decide whether or not to allow “substructure” (see the entry on substructural logics) and whether to allow multiple conclusions in the sequents. We would also have to endorse a particular set of purely structural rules (rules not involving any expression of the language essentially).
- We would have to specify whether it is introduction or elimination rules, or both, that are to characterize the meanings of logical constants.^{[[^note-22]]} (In a sequent formulation, we would have to distinguish between right and left introduction and elimination rules.)
- We would have to allow for subpropositional structure in our rules, in order to make room for quantifier rules.
- We would have to say when an introduction or elimination rule counts as “purely inferential,” to exclude rules like these: \begin{equation*} \frac{a~\text{is red}}{Ra} \quad \frac{A, B, \text{water is}~H_{2}O}{A * B} \end{equation*} The strictest criterion would allow only rules in which every sign, besides a single instance of the constant being characterized, is either structural (like the comma) or schematic (like $\dq{A}$). But although this condition is met by the standard rules for conjunction, it is not met by the natural deduction introduction rule for negation, which must employ either another logical constant ($\dq{\bot}$) or another instance of the negation sign than the one being introduced. Thus one must either relax the condition for being “purely inferential” or add more structure (see especially Belnap 1982)[^belnap-1982].

Different versions of the inferential characterization approach make different decisions about these matters, and these differences affect which constants get certified as “logical.” For example, if we use single-conclusion sequents with the standard rules for the constants, we get the intuitionistic connectives, while if we use multiple-conclusion sequents, we get the classical connectives (Kneale 1956, 253)[^kneale-1956]. If we adopt Došen’s constraints on acceptable rules (Došen 1994, 280)[^došen-1994], the S4 necessity operator gets counted as a logical constant, while if we adopt Hacking’s constraints, it doesn’t (Hacking 1979, 297)[^hacking-1979]. Thus, if we are to have any hope of deciding the hard cases in a principled way, we will have to motivate all of the decisions that distinguish our version of the inferential characterization approach from the others. Here, however, we will avoid getting into these issues of detail and focus instead on the basic idea.

The basic idea is that the logical constants are distinguished from other sorts of expressions by being “characterizable” in terms of purely inferential rules. But what does “characterizable” mean here? As Gómez-Torrente (2002, 29)[^gómez-torrente-2002] observes, it might be taken to require either the fixation of reference (semantic value) or the fixation of sense:

*Semantic value determination:* A constant $c$ is characterizable by rules $R$ iff its being governed by $R$ suffices to fix its reference or semantic value (for example, the truth function it expresses), given certain semantic background assumptions (Hacking 1979, 299, 313)[^hacking-1979].

*Sense determination:* A constant $c$ is characterizable by rules $R$ iff its being governed by $R$ suffices to fix its sense: that is, one can grasp the sense of $c$ simply by learning that it is governed by $R$ (Popper 1946–7, 1947; Kneale 1956, 254–5; Peacocke 1987; Hodes 2004, 135)[^hodes-2004][^kneale-1956][^peacocke-1987][^popper-1946][^popper-1947].

Let us consider these two versions of the inferential characterization approach in turn.

### 6.1 Semantic value determination

Hacking shows that, given certain background semantic assumptions (bivalence, valid inference preserves truth), any introduction and elimination rules meeting certain proof-theoretic conditions (subformula property, provability of elimination theorems for Cut, Identity, and Weakening) will uniquely determine a semantics for the constant they govern (Hacking 1979, 311–314)[^hacking-1979]. It is in this sense that these rules “fix the meaning” of the constant: “they are such that if strong semantic assumptions of a general kind are made, then the specific semantics of the individual logical constants is thereby determined” (313).

The notion of determination of semantic value in a well-defined semantic framework is, at least, clear—unlike the general notion of determination of sense. However, as Gómez-Torrente points out, by concentrating on the fixation of reference (or semantic value) rather than sense, Hacking opens himself up to an objection not unlike the objection to permutation-invariance approaches we considered above (see also Sainsbury 2001, 369)[^sainsbury-2001]. Consider the quantifier $\dq{W}$, which means “not for all not …, if all are not male widows, and for all not …, if not all are not male widows” (Gómez-Torrente 2002, 29)[^gómez-torrente-2002]. (It is important here that $\dq{W}$ is a primitive sign of the language, not one introduced by a definition in terms of $\dq{\forall}$, $\dq{\neg}$, “male”, and “widow”.) Since there are no male widows, $\dq{W}$ has the same semantic value as our ordinary quantifier $\dq{\exists}$. (As above, we can think of the semantic value of a quantifier as a function from sets of assignments to sets of assignments.) Now let $R$ be the standard introduction and elimination rules for $\dq{\exists}$, and let $R'$ be the result of substituting $\dq{W}$ for $\dq{\exists}$ in these rules. Clearly, $R'$ is no less “purely inferential” than $R$. And if $R$ fixes a semantic value for $\dq{\exists}$, then $R'$ fixes a semantic value—the very same semantic value—for $\dq{W}$. So if logical constants are expressions whose semantic values can be fixed by means of purely inferential introduction and elimination rules, $\dq{W}$ counts as a logical constant if and only if $\dq{\exists}$ does.

Yet intuitively there is an important difference between these constants. We might describe it this way: whereas learning the rules $R$ is sufficient to impart a full grasp of $\dq{\exists}$, one could learn the rules $R'$ without fully understanding what is meant by $\dq{W}$. To understand $\dq{W}$ one must know about the human institution of marriage, and that accounts for our feeling that $\dq{W}$ is not “topic-neutral” enough to be a logical constant. However, this difference between $\dq{W}$ and $\dq{\exists}$ cannot be discerned if we talk only of reference or semantic value; it is a difference in the *senses* of the two expressions.

### 6.2 Sense determination

The idea that introduction and/or elimination rules fix the *sense* of a logical constant is often motivated by talk of the rules as *defining* the constant. Gentzen remarks that the natural deduction rules “represent, as it were, the ‘definitions’ of the symbols concerned, and the eliminations are no more, in the final analysis, than the consequences of these definitions” (1935, §5.13; 1969, 80). However, a genuine definition would permit the constant to be eliminated from every context in which it occurs (see the entry on Definitions), and introduction and elimination rules for logical constants do not, in general, permit this. For example, in an intuitionistic sequent calculus, there is no sequent (or group of sequents) not containing $\dq{\rightarrow}$ that is equivalent to the sequent $\dq{A \rightarrow B \vdash C}$. For this reason, Kneale (1956, 257)[^kneale-1956] says only that we can “treat” the rules as definitions, Hacking (1979)[^hacking-1979] speaks of the rules “not as defining but only as characterizing the logical constants,” and Došen (1994)[^došen-1994] says that the rules provide only an “analysis,” not a definition.^{[[^note-23]]}

However, even if the rules are not “definitions,” there may still be something to say for the claim that they “fix the senses” of the constants they introduce. For it may be that a speaker’s grasp of the meaning of the constants consists in her mastery of these rules: her disposition to accept inferences conforming to the rules as “primitively compelling” (Peacocke 1987, Hodes 2004)[^hodes-2004][^peacocke-1987]. (A speaker finds an inference form primitively compelling just in case she finds it compelling and does not take its correctness to require external ratification, e.g. by inference.) If the senses of logical constants are individuated in this way by the conditions for their grasp, we can distinguish between truth-functionally equivalent constants with different meanings, like $\dq{\vee}$, $\dq{\ddagger}$, and $\dq{\dagger}$, as defined below:

\begin{align*} A \vee B & \quad A~\text{or}~B\\ A \ddagger B & \quad \text{not both not}~A~\text{and not}~B\\ A \dagger B & \quad (A~\text{or}~B)~\text{and no widows are male} \end{align*}

To understand $\dq{\vee}$ one must find the standard introduction rules primitively compelling:

$$\label{or-intro} \frac{A}{A \vee B} \quad \frac{B}{A \vee B} $$

To understand $\dq{\ddagger}$ one must find the following elimination rule primitively compelling:

$$\label{ddagger-elim} \frac{\neg A, \neg B, A \ddagger B}{C} $$

Finally, to grasp the sense of $\dq{\dagger}$ one must find these introduction rules primitively compelling:

$$\label{dagger-intro} \frac{A, \text{no widows are male}}{A \dagger B} \quad \frac{B, \text{no widows are male}}{A \dagger B} $$

$\dq{\vee}$ and $\dq{\ddagger}$ will count as logical constants, because their sense-constitutive rules are purely inferential, while $\dq{\dagger}$ will not, because its rules are not. (In the same way we can distinguish $\dq{\exists}$ from $\dq{W}$.) Note that appropriately rewritten versions of $\refp{or-intro}$ will *hold* for $\dq{\ddagger}$ and $\dq{\dagger}$; the difference is that one can grasp $\dq{\ddagger}$ and $\dq{\dagger}$ (but not $\dq{\vee}$) without finding these rules *primitively* compelling (Peacocke 1987, 156; cp. Sainsbury 2001, 370–1)[^peacocke-1987][^sainsbury-2001].

Some critics have doubted that the introduction and elimination rules for the logical constants exhaust the aspects of the use of these constants that must be mastered if one is to understand them. For example, it has been suggested that in order to grasp the conditional and the universal quantifier, one must be disposed to treat certain kinds of inductive evidence as grounds for the assertion of conditionals and universally quantified claims (Dummett 1991, 275–8; Gómez-Torrente 2002, 26–7; Sainsbury 2001, 370–1)[^dummett-1991][^gómez-torrente-2002][^sainsbury-2001]. It is not clear that these additional aspects of use can be captured in “purely inferential” rules, or that they can be derived from aspects of use that can be so captured.

It is sometimes thought that Prior’s (1960)[^prior-1960] example of a connective “tonk,”

$$ \frac{A}{A~\text{tonk}~B} \quad \frac{A~\text{tonk}~B}{B} $$

whose rules permit inferring anything from anything, decisively refutes the idea that the senses of logical constants are fixed by their introduction and/or elimination rules. But although Prior’s example (anticipated in Popper 1946–7, 284)[^popper-1946] certainly shows that *not all* sets of introduction and elimination rules determine a coherent meaning for a logical constant, it does not show that *none* do, or that the logical constants are not distinctive in having their meanings determined in this way. For some attempts to articulate conditions under which introduction and elimination rules do fix a meaning, see Belnap (1962)[^belnap-1962], Hacking (1979, 296–8)[^hacking-1979], Kremer (1988, 62–6)[^kremer-1988], and Hodes (2004, 156–7)[^hodes-2004].

Prawitz (1985; 2005)[^prawitz-1985][^prawitz-2005] argues that *any* formally suitable introduction rule can fix the meaning for a logical constant. On Prawitz’s view, the lesson we learn from Prior is that we cannot *also* stipulate an elimination rule, but must justify any proposed elimination rule by showing that there is a procedure for rearranging any direct proof of the premises of the elimination rule into a direct proof of the conclusion. Thus, we can stipulate the introduction rule for “tonk”, but must then content ourselves with the strongest elimination rule for which such a procedure is available:

$$ \frac{A~\text{tonk}~B}{A}. $$

Other philosophers reject Prawitz's (and Gentzen's) view that the introduction rules have priority in fixing the meanings of constants, but retain the idea that the introduction and elimination rules that fix the meaning of a constant must be in *harmony*: the elimination rules must not permit us to infer more from a compound sentence than would be justified by the premises of the corresponding introduction rules (Dummett 1981, 396; Tennant 1987, 76-98)[^dummett-1981][^tennant-1987]. (For analyses of various notions of harmony, and their relation to notions like normalizability and conservativeness, see Milne 1994, Read 2010, and Steinberger 2011.)[^milne-1994][^read-2010][^steinberger-2011]

## 7. Pragmatic demarcations

The proposals for demarcating logical constants that we have examined so far have all been *analytical demarcations*. They have sought to identify some favored property (grammatical particlehood, topic neutrality, permutation invariance, characterizability by inferential rules, etc.) as a necessary and sufficient condition for an expression to be a logical constant. A fundamentally different strategy for demarcating the constants is to start with a *job description* for logic and identify the constants as the expressions that are necessary to do that job. For example, we might start with the idea that the job of logic is to serve as a “framework for the deductive sytematization of scientific theories” (Warmbrod 1999, 516)[^warmbrod-1999], or to characterize mathematical structures and represent mathematical reasoning (Shapiro 1991)[^shapiro-1991], or to “[express] explicitly *within* a language the features of the use of that language that confer conceptual contents on the states, attitudes, performances, and expressions whose significances are governed by those practices” (Brandom 1994, xviii)[^brandom-1994]. Let us call demarcations of this kind *pragmatic demarcations*.

There are some very general differences between the two kinds of demarcations. Unlike analytical demarcations, pragmatic demarcations are guided by what Warmbrod calls a “requirement of minimalism”:

> …logical theory should be as simple, as modest in its assumptions, and as flexible as possible given the goal of providing a conceptual apparatus adequate for the project of systematization. In practice, the minimalist constraint dictates that the set of terms recognized as logical constants should be as small as possible. (Warmbrod 1999, 521)[^warmbrod-1999]

Or, in Harman’s pithier formulation: “Count as logic only as much as you have to” (Harman 1972, 79)[^harman-1972]. Warmbrod uses this constraint to argue that the theory of identity is not part of logic, on the grounds that it is not needed to do the job he has identified for logic: “[w]e can systematize the same sets of sentences by recognizing only the truth-functional connectives and first-order quantifiers as constants, treating ‘=’ as an ordinary predicate, and adopting appropriate axioms for identity” (521; cf. Quine 1986, 63, 1980, 28)[^quine-1980][^quine-1986]. On similar grounds, both Harman and Warmbrod argue that modal operators should not be considered part of logic.^{[[^note-24]]} Their point is not that identity or modal operators lack some feature that the first-order quantifiers and truth-functional operators possess, but merely that, since we *can* get by without taking these notions to be part of our logic, we should. Warmbrod and Tharp even explore the possibility of taking truth-functional logic to be the whole of logic and viewing quantification theory as a non-logical theory (Warmbrod 1999, 525; Tharp 1975, 18)[^tharp-1975][^warmbrod-1999], though both reject this idea on pragmatic grounds.

While pragmatic demarcations seek to minimize what counts as logic, analytical demarcations are inclusive. They count as logical *any* expression that has the favored property. It is simply irrelevant whether an expression is *required* for a particular purpose: its logicality rests on features that it has independently of any use to which we might put it.

Relatedly, pragmatic approaches tend to be holistic. Because it is whole logical *systems* that can be evaluated as sufficient or insufficient for doing the “job” assigned to logic, properties of systems tend to be emphasized in pragmatic demarcations. For example, Wagner (1987, 10–11)[^wagner-1987] invokes Lindstrom’s theorem—that first-order logic is the only logic that is either complete or compact and satisfies the Löwenheim-Skolem theorem—in arguing that logic should be limited to first-order logic, and Kneale and Kneale (1962, 724, 741) invoke Gödel’s incompleteness theorems to similar effect. Although nothing about the idea of an analytical demarcation excludes appeal to properties of whole systems, analytical demarcations tend to appeal to *local* properties of particular expressions rather than global systemic properties.

Finally, on a pragmatic demarcation, what counts as logic may depend on the current state of scientific and mathematical theory. If the advance of science results in an increase or decrease in the resources needed for deductive systematization of science (or whatever is the favored task of logic), what counts as logic changes accordingly (Warmbrod 1999, 533)[^warmbrod-1999]. On an analytical demarcation, by contrast, whether particular resources are logical depends only on whether they have the favored property. If they do not, and if it turns out that they are needed for the deductive systematization of theories, then the proper conclusion to draw is that logic alone is not adequate for this task.

## 8. Problem or pseudoproblem?

Now that we have gotten a sense for the tremendous variety of approaches to the problem of logical constants, let us step back and reflect on the problem itself and its motivation. We can distinguish four general attitudes toward the problem of logical constants: those of the Demarcater, the Debunker, the Relativist, and the Deflater.

*Demarcaters* hold that the demarcation of logical constants is a genuine and important problem, whose solution can be expected to illuminate the nature and special status of logic. On their view, the task of logic is to study features that arguments possess in virtue of their logical forms or structures.^{[[^note-25]]} Although there may be some sense in which the argument

$$\label{chicago-north} \frac{\text{Chicago is north of New Orleans}} {\text{New Orleans is south of Chicago}} $$

is a good or “valid” argument, it is not *formally* valid. On the Demarcater’s view, logicians who investigate the (non-formal) kind of “validity” possessed by $\refp{chicago-north}$ are straying from the proper province of logic into some neighboring domain (here, geography or lexicography; in other cases, mathematics or metaphysics). For the Demarcater, then, understanding the distinction between logical and nonlogical constants is essential for understanding what logic is about. (For a forceful statement of the Demarcater’s point of view, see Kneale 1956.)[^kneale-1956]

*Debunkers*, on the other hand, hold that the so-called “problem of logical constants” is a pseudoproblem (Bolzano 1929, §186; Lakoff 1970, 252–4; Coffa 1975; Etchemendy 1983, 1990, ch. 9; Barwise and Feferman 1985, 6; Read 1994)[^barwise-1985][^bolzano-1929][^coffa-1975][^etchemendy-1983][^etchemendy-1990][^lakoff-1970][^read-1994]. They do not dispute that logicians have traditionally concerned themselves with argument forms in which a limited number of expressions occur essentially. What they deny is that these expressions and argument forms define the *subject matter* of logic. On their view, logic is concerned with validity *simpliciter*, not just validity that holds in virtue of a limited set of “logical forms.” The logician’s *method* for studying validity is to classify arguments by their forms, but these forms (and the logical constants that in part define them) are logic’s *tools*, not its subject matter. The forms and constants with which logicians are concerned at a particular point in the development of logic are just a reflection of the logicians’ progress (up to that point) in systematically classifying valid inferences. Asking what is special about these forms and constants is thus a bit like asking what is special about the mountains that can be climbed in a day: “The information so derived will be too closely dependent upon the skill of the climber to tell us much about geography” (Coffa 1975, 114)[^coffa-1975]. What makes people logicians is not their concern with “and”, “or”, and “not”, but their concern with validity, consequence, consistency, and proof, and the distinctive methods they bring to their investigations.

A good way to see the practical difference between Debunkers and Demarcaters is by contrasting their views on the use of counterexamples to show invalidity. Demarcaters typically hold that one can show an argument to be invalid by exhibiting another argument with the same logical form that has true premises and a false conclusion. Of course, an argument will always instantiate multiple forms. For example, the argument

$$\label{firefighter} \frac{\text{Firefighter(Joe)}} {\exists x\,\text{Firefighter}(x)} $$

can be seen as an instance of the propositional logical form

$$\label{propform} \frac{P}{Q} $$

as well as the more articulated form

$$\label{quantform} \frac{F(a)} {\exists x F(x)}. $$

As Massey (1975)[^massey-1975] reminds us, the fact that there are other arguments with the form $\refp{propform}$ that have true premises and a false conclusion does not show that $\refp{firefighter}$ is invalid (or even that it is “formally” invalid). The Demarcater will insist that a genuine counterexample to the formal validity of $\refp{firefighter}$ would have to exhibit the *full* logical structure of $\refp{firefighter}$, which is not $\refp{propform}$ but $\refp{quantform}$. Thus the Demarcater’s use of counterexamples to demonstrate the formal invalidity of arguments presupposes a principled way of discerning the *full* logical structure of an argument, and hence of distinguishing logical constants from nonlogical constants.^{[[^note-26]]}

The Debunker, by contrast, rejects the idea that one of the many argument forms $\refp{firefighter}$ instantiates should be privileged as *the* logical form of $\refp{firefighter}$. On the Debunker’s view, counterexamples never show anything about a particular argument. All they show is that a *form* is invalid (that is, that it has invalid instances). To show that a particular *argument* is invalid, one sort of Debunker holds, one needs to describe a possible situation in which the premises would be true and the conclusion false, and to give a formal counterexample is not to do *that*.

The Demarcater will object that the Debunker’s tolerant attitude leaves us with no coherent distinction between logic and other disciplines. For surely it is the chemist, not the logician, who will be called upon to tell us whether the following argument is a good one:

$$\label{litmus} \frac{\text{HCl turns litmus paper red}} {\text{HCl is an acid}}. $$

Without a principled distinction between logical and nonlogical constants, it seems, logic would need to be a kind of universal science: not just a canon for inference, but an encyclopedia. If logic is to be a distinctive discipline, the Demarcater will argue, it must concern itself not with all kinds of validity or goodness of arguments, but with a special, privileged kind: *formal* validity.

Against this, the Debunker might insist that deductive validity is a feature arguments have by virtue of the meanings of the terms contained in them, so that anyone who understands the premises and conclusion of an argument must be in a position to determine, without recourse to empirical investigation, whether it is valid. On this conception, logic is the study of *analytic* truth, consequence, consistency, and validity. Because the relation between premise and conclusion in $\refp{litmus}$ depends on empirical facts, not the meanings of terms, $\refp{litmus}$ is not deductively valid.^{[[^note-27]]}

This response will not be available to those who have reservations about the analytic/synthetic distinction. An important example is Tarski (1936a; 1936b; 1983; 1987; 2002)[^tarski-1936a][^tarski-1936b][^tarski-1983][^tarski-1987][^tarski-2002], who was much concerned to define logical truth and consequence in purely mathematical terms, without appealing to suspect modal or epistemic notions. On Tarski’s account, an argument is valid just in case there is no interpretation of its nonlogical constants on which the premises are true and the conclusion false. On this account, an argument containing no nonlogical constants is valid just in case it is materially truth-preserving (it is not the case that its premises are true and its conclusion false). Thus, as Tarski notes, if *every* expression of a language counted as a logical constant, logical validity would reduce to material truth preservation (or, on later versions of Tarski’s definition, to material truth preservation on every nonempty domain) (1983, 419). Someone who found this result intolerable might take it to show either that there *must* be a principled distinction between logical and nonlogical constants (the Demarcater’s conclusion), or that Tarski’s definition is misguided (the Debunker’s conclusion; see Etchemendy 1990, ch. 9)[^etchemendy-1990].

Tarski’s own reaction was more cautious. After concluding that the distinction is “certainly not quite arbitrary” (1983, 418), he writes:

> Perhaps it will be possible to find important objective arguments which will enable us to justify the traditional boundary between logical and extra-logical expressions. But I also consider it to be quite possible that investigations will bring no positive results in this direction, so that we shall be compelled to regard such concepts as ‘logical consequence’, ‘analytical statement’, and ‘tautology’ as relative concepts which must, on each occasion, be related to a definite, although in greater or less degree arbitrary, division of terms into logical and extra-logical. (420; see also Tarski 1987)[^tarski-1987]

Here Tarski is describing a position distinct from both the Demarcater’s position and the Debunker’s. The *Relativist* agrees with the Demarcater that logical consequence must be understood as *formal* consequence, and so presupposes a distinction between logical and nonlogical constants. But she agrees with the Debunker that we should not ask, “Which expressions are logical constants and which are not?” The way she reconciles these apparently conflicting positions is by *relativizing* logical consequence to a choice of logical constants. For each set *C* of logical constants, there will be a corresponding notion of *C*-consequence. None of these notions is to be identified with consequence *simpliciter*; different ones are useful for different purposes. In the limiting case, where every expression of the language is taken to be a logical constant, we get material consequence, but this is no more (and no less) *the* consequence relation than any of the others.

Like the Relativist, the *Deflater* seeks a moderate middle ground between the Demarcater and the Debunker. The Deflater agrees with the Demarcater that there is a real distinction between logical and nonlogical constants, and between formally and materially valid arguments. She rejects the Relativist’s position that logical consequence is a relative notion. But she also rejects the Demarcater’s project of finding precise and illuminating necessary and sufficient conditions for logical constancy. “Logical constant”, she holds, is a “family resemblance” term, so we should not expect to uncover a hidden essence that all logical constants share. As Wittgenstein said about the concept of number: “the strength of the thread does not reside in the fact that some one fibre runs through its whole length, but in the overlapping of many fibres” (Wittgenstein 1958, §67)[^wittgenstein-1958]. That does not mean that there is no distinction between logical and nonlogical constants, any more than our inability to give a precise definition of “game” means that there is no difference between games and other activities. Nor does it mean that the distinction does not matter. What it means is that we should not expect a principled criterion for logical constancy that explains why logic has a privileged epistemological or semantic status. (For a nice articulation of this kind of view, see Gómez-Torrente 2002.)[^gómez-torrente-2002]

The debate between these four positions cannot be resolved here, because to some extent “the proof is in the pudding.” A compelling and illuminating account of logical constants—one that vindicated a disciplinary segregation of $\refp{chicago-north}$ from $\refp{firefighter}$ by showing how these arguments are importantly different—might give us reason to be Demarcaters. But it is important not to get so caught up in the debates between different Demarcaters, or between Demarcaters and Debunkers, that one loses sight of the other positions one might take toward the problem of logical constants.

## Further reading

Other recent general discussions of the problem of logical constants include Peacocke 1976, McCarthy 1998, Warmbrod 1999, Sainsbury 2001, ch. 6, and Gómez-Torrente 2002. Tarski 1936b is essential background to all of these.

For a discussion of grammatical criteria for logical terms, see Quine 1980 and Føllesdal’s (1980)[^føllesdal-1980] reply.

For a discussion of the Davidsonian approach, see Davidson 1984, Evans 1976, Lycan 1989, Lepore and Ludwig 2002, and Edwards 2002.

Tarski 1986 is a brief and cogent exposition of the permutation-invariance approach. For elaboration and criticism, see McCarthy 1981, van Bentham 1989, Sher 1991, McGee 1996, Feferman 1999 and 2010, Bonnay 2008, and Dutilh Novaes 2014. Bonnay 2014 surveys recent work in this area.

Hacking 1979 and Peacocke 1987 are good representatives of the two versions of the inferential characterization approach discussed above. Popper’s papers (1946–7, 1947) are still worth reading; see Schroeder-Heister 1984 for critical discussion and Koslow 1999 for a modern approach reminiscent of Popper’s. See also Kneale 1956, Kremer 1988, Prawitz 1985 and 2005, Tennant 1987, ch. 9, Dummett 1991, ch. 11, Došen 1994, Hodes 2004, and Read 2010.

For examples of pragmatic demarcations, see Wagner 1987 and Warmbrod 1999. A different kind of pragmatic approach can be found in Brandom (2000, ch. 1; 2008, ch. 2), who characterizes logical vocabulary in terms of its *expressive* role.

For critiques of the whole project of demarcating the logical constants, see Coffa 1975, Etchemendy (1983; 1990, ch. 9), and Read 1994.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=logical-constants). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/logical-constants/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=logical-constants&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](http://philpapers.org/sep/logical-constants/) at [PhilPapers](http://philpapers.org), with links to its database. |

## Other Internet Resources

- MacFarlane, J., 2000. [*What Does It Mean to Say that Logic Is Formal?*](http://johnmacfarlane.net/dissertation.pdf). Ph.D. dissertation, University of Pittsburgh.

## Related Entries

analytic/synthetic distinction | Davidson, Donald | definitions | logic: modal | logic: substructural | logic: temporal | logical consequence | logical form | semantics: proof-theoretic | Tarski, Alfred: truth definitions

### Acknowledgments

I am grateful to Fabrizio Cariani, Kosta Došen, Solomon Feferman, Mario Gómez-Torrente, Graham Priest, Greg Restall, Gila Sher, and an anonymous reviewer for comments that helped improve this entry. Parts of the entry are derived from chapters 1, 2, 3, and 6 of my dissertation, “What Does It Mean to Say that Logic is Formal?” (University of Pittsburgh, 2000).

## Notes（原文脚注）

1. They are called “constants” not (as Kuhn 1981 supposes)[^kuhn-1981] because their interpretations do not vary across models—after all, the “nonlogical constants” are called “constants” too—but because they are not *variables*.

2. A *first-level function* is a function whose arguments are objects. A *second-level function* is a function whose arguments are first-level functions.

3. Wittgenstein strenuously rejects the Fregean view that the quantifiers and logical connectives represent relations (1922, §5.42, §5.44): “My fundamental thought is that the ‘logical constants’ do not represent” (§4.0312). But this cannot be the basis for a Wittgensteinian demarcation of the logical constants, because on Wittgenstein’s view, predicate signs do not represent either. On his view, the sign $\dq{R}$ in $\dq{aRb}$ does not stand for a relation; rather, the *fact* that $\dq{R}$ stands between $\dq{a}$ and $\dq{b}$ represents that the object represented by $\dq{a}$ stands in a certain relation to the object represented by $\dq{b}$ (cf. §3.1432). One might say that on Wittgenstein’s theory, all signs except names are syncategorematic.

4. Strictly speaking, it is the grammatical constructions themselves, not the expressions involved in them, that should be called logical or nonlogical: not the sign $\dq{\and}$, but the placing of a token of $\dq{\and}$ between two sentences. That is one lesson of Wilfrid Sellars’s (1962)[^sellars-1962] language Jumblese, which contains nonlogical predicate *constructions* but no nonlogical predicate *expressions*. To say $\dq{a~\text{is green}}$ in Jumblese, one writes the letter $\dq{a}$ in boldface, and to say $\dq{a~\text{is redder than}~b}$, one writes the letter $\dq{a}$ above the letter $\dq{b}$. A similar trick could be used to devise a language with no logical expressions: for example, the disjunction of $A$ and $B$ might be written as $\dq{A^B}$, and the conjunction as $\dq{AB}$. Although this language would not contain specifically logical *expressions*, it would have logical modes of construction. In the main text we abstract from this complexity and assume that aside from predication or functional application, each logical mode of construction is associated with a specific expression, as is the case in most commonly used logical calculi.

5. Quine solves the problem of the sign for identity (“=”) by denying that it is a logical constant (1980, 28) and showing how it can be defined or “simulated” in a language with a finite stock of predicates (1986, 63–64), whereas Dummett qualifies the grammatical criterion and allows “=” to count as a logical constant in virtue of its *semantic* features (1981, 22 n.). More precisely, he proposes that identity should count as logical because it allows us to express “quantifier conditions” (properties of predicates that are invariant under permutations of elements of the domain) that we could not express otherwise.

6. “Satisfaction” is Tarski’s name for truth on an assignment of values to the variables. To specify a satisfaction condition for a sentence is to say on which assignments of values to its variables it comes out true.

7. For simplicity, I assume that all complex terms, e.g. “the mother of Abraham” or “the square of 4”, can be treated as definite descriptions, and hence as quantifiers (see Neale 1990)[^neale-1990]. Otherwise recursive axioms will be needed for reference-on-an-assignment as well as for satisfaction (truth-on-an-assignment).

8. This criterion judges *sets* of expressions together, leaving open the possibility that (say) $\{\textrm{A}, \textrm{B}, \textrm{C}\}$ and $\{\textrm{A}, \textrm{B}, \textrm{D}\}$ will both satisfy the criterion, while $\{\textrm{A}, \textrm{B}, \textrm{C}, \textrm{D}\}$ won’t. However, a criterion that works this way may still be of some use in constraining the choice of logical constants, even if it does not determine it.

9. Note that this third clause is redundant if $\langle x, y \rangle$ is defined in the usual way as $\{\{x\}, \{x, y\}\}$.

10. Note that if we follow Frege and take the two truth values to be objects, then the truth functional connectives *do* have extensions in the usual sense, but they are not permutation invariant, because they treat the True and the False differently from other objects.

11. $p \circ a$ is the composition of $a$ and $p$: ($p \circ a)(x) = p(a(x))$. An assignment is just a function from variables to values, so if $a$ is an assignment, so is $p \circ a$.

12. As McGee acknowledges, the revised criterion still allows logical constants to behave very differently on domains of different *cardinalities*. For example, “it would permit a logical connective which acts like disjunction when the size of the domain is an even successor cardinal, like conjunction when the size of the domain is an odd successor cardinal, and like a biconditional at limits” (577). Feferman 1999 takes this to be a strong reason for preferring a more stringent criterion for logicality: one on which the behavior of a logical connective on one domain connects naturally with its behavior on other domains.

13. For a different way of motivating the permutation invariance criterion for logical constancy, starting from the “pretheoretical intuition that logical consequences are distinguished from material consequences in being necessary and formal,” see Sher 1991, ch. 3.

14. In this respect it seems superior to Peacocke’s epistemic gloss on topic neutrality (Peacocke 1976)[^peacocke-1976]. Peacocke’s idea is that “$\alpha$ is a logical constant if $\alpha$ is noncomplex and, for any expressions $\beta_1 \dots \beta_n$ on which $\alpha$ operates to form expression $\alpha(\beta_1, \dots, \beta_n)$, given knowledge of which sequences satisfy each of $\beta_1 \dots \beta_n$ and of the satisfaction condition of expressions of the form $\alpha(\beta_1, \dots, \beta_n)$, one can know a priori which sequences satisfy $\alpha(\beta_1, \dots, \beta_n)$, in particular without knowing the properties and relations of the objects in the sequences” (223; for a more carefully qualified statement, see 225–6, and for the connection with topic neutrality, see 229). As it stands, this criterion is too demanding, as Peacocke himself points out. One might know which sequences satisfy $\dq{F(x)}$ without knowing that they are *all* the sequences, and hence without being able to determine which sequences satisfy $\dq{\forall x F(x)}$. Yet $\dq{\forall}$ is presumably a logical constant. Similarly, one might know of a sequence $s$ that it satisfies $\dq{F(x)}$ and also that it satisfies $\dq{G(x)}$ without knowing that it satisfies $\dq{F(x) \and G(x)}$. For example, one might know of Venus that it satisfies “is the morning star” and know of Venus that it satisfies “is the evening star” without knowing of Venus that it satisfies “is the morning star and is the evening star.” Peacocke deals with these problems by further specifying the kind of knowledge his imaginary knowers have (227), but his additional conditions seem *ad hoc* (McCarthy 1981, 503–4; Sainsbury 2001, 378)[^mccarthy-1981][^sainsbury-2001]. Moreover, given some natural theses about what is required to “know which object” a number, set, or syntactic string is, Peacocke’s criterion will count “is the successor of ...”, “is the pair set formed from ... and ...”, “is the concatenation of ... and ...”, and other intuitively non-logical expressions as logical constants (McCarthy 1981, 506–7)[^mccarthy-1981]. McCarthy suggests that the notion of topic neutrality Peacocke is trying to capture can be better captured by a non-epistemic invariance criterion like the one we are here considering.

15. The criterion would also appear to rule out operators like “Now it is the case that” and “It is actually the case that”, which pay special attention to the world or time of utterance. However, settling this question would require stating the invariance criterion in a semantic framework suitable for a logic of indexicals: one that relativizes truth to contexts as well as circumstances of evaluation (see Kaplan 1989)[^kaplan-1989]. Such a framework would also be needed to decide whether the invariance criterion rules out counterfactual conditionals, which (on many popular accounts) are sensitive to a contextually determined similarity metric on worlds.

16. Assuming the standard definition of a logical truth as a sentence that is true in all domains and on all reinterpretations of its nonlogical constants. A modal definition of logical truth would give different results here.

17. A similar argument in (McCarthy 1981, 515)[^mccarthy-1981] rests explicitly on the premise that logical truths should be true necessarily.

18. McGee backs up this intuitive claim with the following argument:

1. If $\dq{\#}$ is a logical constant, then $\dq{\#\neg (0=0) \vee \neg (0=0)}$ is a logical truth (that is, it is true in every domain on every interpretation of its nonlogical constants).
2. But $\dq{\#\neg (0=0) \vee \neg (0=0)}$ entails “water is H_{2}O”, which is not a logical truth.
3. And logical truths entail only logical truths. Thus,
4. $\dq{\#}$ is not a logical constant.

The argument is problematic, because it is not clear what McGee means by “entails” in (2) and (3). If he has in mind the standard notion of logical implication (truth preservation on every domain and interpretation of the nonlogical constants), then (2) is false: $\dq{\#\neg(0=0) \vee \neg(0=0)}$ is true on every interpretation, but “water = H_{2}O” is false on many interpretations (those that assign distinct referents to the nonlogical constants “water” and “H_{2}O”). If he has in mind the standard modal notion of entailment ($A$ entails $B$ just in case it is impossible for $A$ to be true and $B$ false), then (3) is false, for in that sense of entailment, logical truths entail all necessary truths, not just other logical truths. Perhaps McGee has in mind some other notion of entailment that makes both premises true, but pending clarification on this point, the force of his argument remains unclear.

19. An expression is a rigid designator if its denotation is constant across possible worlds. (See the entry on rigid designators.)

20. For versions of this idea, see Popper 1946–7, 1947; Kneale 1956; Prawitz 1985; Zucker 1978; Zucker and Tragesser 1978; Hacking 1979; Peacocke 1987; Kremer 1988; Dummett 1991; Koslow 1992, 1999; Došen 1994; Hodes 2004; and Feferman 2015.

21. The premise of this argument is far from obvious. The notion of a valid inference (and hence of an inference rule) is a pretty sophisticated one, and its connection to norms for reasoning is not as straightforward as is sometimes assumed. For example, knowledge that $Y$ can be validly inferred from $X$ does not license one to believe $Y$ if one believes $X$; it may be more rational to abandon one’s belief in $X$, or to take up a sceptical position towards both $X$ and $Y$ (see Harman 1984)[^harman-1984]. The technical practice of “inference” that the introduction and elimination rules govern is not to be confused with “inference” in its more generic sense—the formation of beliefs on the basis of other beliefs. But unless these two senses of “inference” are conflated, it is not clear why we should assume that a capacity for articulate thought and reasoning implies an understanding of the former as well as the latter.

22. Gentzen (1935, §5.13; 1969, 80) holds that a constant is defined by its introduction rules, and that the elimination rules are just consequences of these. This idea is developed further in Prawitz 1985 and Dummett 1991. Koslow (1992, 1999)[^koslow-1992][^koslow-1999] takes the elimination rules as fundamental, defining each logical operation as the weakest object in an implication structure that satisfies the elimination rule. Kneale (1956, 257)[^kneale-1956] uses two-way (reversible) sequent rules, both left and right. Hodes (2004, 143)[^hodes-2004] takes the introduction rules to be fundamental for some constants, the elimination rules for others (and in some cases, he holds, neither is fundamental).

23. Popper (1947)[^popper-1947] and Koslow (1992, 1999)[^koslow-1992][^koslow-1999] give genuine explicit definitions, not of the constants themselves, but of metalinguistic predicates like “is a negation of $A$” and “is a disjunction of $A$ and $B$.” For example, an item $A$ in an implicational structure counts as a “disjunction” of two other items $B$ and $C$ iff it is the weakest item in that structure that is implied by both $B$ and $C$. This definition does not guarantee that in a given implicational structure there will *be* a disjunction of any two arbitrary items. For an excellent critical discussion of Popper’s project, see Schroeder-Heister 1984. On Došen’s (1994)[^došen-1994] view, “[a] constant is logical if, and only if, it can be ultimately analysed in structural terms” (281). An *analysis* of a constant α of a language *L* in a conceptually more “basic” language *M* is an equivalence between a sentence of *M* + {α} containing a single occurrence of α and a sentence of *M* not containing α, such that “[f]rom the equivalence …and from the understanding of *M* and *L* minus α, we can infer every sentence of *L* analytically true in *L* and no sentence of *L* not analytically true in *L*” (1994, 282; for a related idea see Kremer 1988, 65)[^kremer-1988].

24. Warmbrod’s approach is to paraphrase modal claims into first-order claims about relations between possible worlds, while Harman’s is to introduce a non-logical predicate “is necessary” and a logical operator that forms names of propositions. It is also possible to treat the sentential operators “necessarily” and “possibly” as non-logical operators in an intensional language (Kuhn 1981)[^kuhn-1981].

25. I focus on arguments for the sake of brevity. Logic is of course also concerned with properties of sentences (logical truth and falsity, provability), sets of sentences (consistency), and sequences of sentences (proof); and with relations between sentences (logical equivalence and implication) and between sets of sentences and sentences (logical consequence and independence).

26. Frege seems to have been sceptical about the possibility of proving logical invalidity and independence precisely because he saw that such proofs would not be possible without a principled demarcation of logical constants, which he did not see how to provide (Frege 1906, 429; and for discussion, Ricketts 1997)[^frege-1906][^ricketts-1997].

27. An alternative response to the Demarcater’s challenge, one that does not rely on the analytic-synthetic distinction, goes like this. Although logic is the study of validity *as such*, it should not be expected to pronounce on every question about the validity of particular arguments. After all, physics can justly be described as the study of space, time, matter, and energy, even though there are many questions concerning the distribution of matter and energy in spacetime that physics cannot answer. (For example: was there an olive on this marble slab two thousand years ago this day?) Logicians answer *general* questions about validity, and although often the answers to these general questions settle questions about the validity of particular arguments, there is no reason to think they should settle all such questions (Read 1994)[^read-1994]. Alternatively, the Debunker might argue that what is distinctive of logic is its use of certain *methods* (formalization, proof, counterexample) to investigate validity.

[^barwise-1985]: Barwise, J. and S. Feferman (eds.), 1985. *Model-Theoretic Logics*, New York: Springer-Verlag.

[^belnap-1962]: Belnap, N. D., 1962. “Tonk, Plonk and Plink,” *Analysis*, 23: 130–134.

[^belnap-1982]: –––, 1982. “Display Logic,” *Journal of Symbolic Logic*, 11: 357–417.

[^bolzano-1929]: Bolzano, B., 1929. *Wissenschaftslehre* (2nd edition), Leipzig: Felix Meiner.

[^bonnay-2008]: Bonnay, D., 2008. “Logicality and Invariance,” *Bulletin of Symbolic Logic*, 14: 29–68.

[^bonnay-2014]: –––, 2014. “Logical Constants, or How to use Invariance in Order to Complete the Explication of Logical Consequence,” *Philosophy Compass*, 9: 54–65.

[^boolos-1975]: Boolos, G., 1975. “On Second-order Logic,” *Journal of Philosophy*, 72: 509–527.

[^brandom-1994]: Brandom, R., 1994. *Making It Explicit*, Cambridge: Harvard University Press.

[^brandom-2000]: –––, 2000. *Articulating Reasons: An Introduction to Inferentialism*, Cambridge: Harvard University Press.

[^brandom-2008]: –––, 2008. *Between Saying and Doing: Towards an Analytic Pragmatism*, Oxford: Oxford University Press.

[^bueno-2013]: Bueno, O., and S. A. Shalkowski, 2013. “Logical Constants: A Modalist Approach,” *Noûs*, 47: 1–24.

[^buridan-1976]: Buridan, J., 1976. *Tractatus de Consequentiis*, Louvain: Publications Universitaires.

[^carnap-1947]: Carnap, R., 1947. *Meaning and Necessity*, Chicago: University of Chicago Press.

[^chomsky-1995]: Chomsky, N., 1995. *The Minimalist Program*, Cambridge: MIT Press.

[^coffa-1975]: Coffa, J. A., 1975. “Machian Logic,” *Communication and Cognition*, 8: 103–129.

[^davidson-1984]: Davidson, D., 1984. *Inquiries into Truth and Interpretation*, Oxford: Oxford University Press.

[^došen-1994]: Došen, K., 1994. “Logical Constants as Punctuation Marks,” in D. M. Gabbay (ed.), *What Is a Logical System?*, Oxford: Clarendon Press, 273–296.

[^dummett-1981]: Dummett, M., 1981. *Frege: Philosophy of Language* (2nd edition), Cambridge: Harvard University Press.

[^dummett-1991]: –––, 1991. *The Logical Basis of Metaphysics*, Cambridge: Harvard University Press.

[^dutilh-2012]: Dutilh Novaes, Catarina, 2012. “Reassessing Logical Hylomorphism and the Demarcation of Logical Constants,” *Synthese*, 185: 387–410.

[^dutilh-2014]: –––, 2014. “The Undergeneration of Permutation Invariance as a Criterion for Logicality,” *Erkenntnis*, 79: 81–97.

[^edwards-2002]: Edwards, J., 2002. “Theories of Meaning and Logical Constants: Davidson versus Evans,” *Mind*, 111: 249–279.

[^etchemendy-1983]: Etchemendy, J., 1983. “The Doctrine of Logic as Form,” *Linguistics and Philosophy*, 6: 319–334.

[^etchemendy-1990]: –––, 1990. *The Concept of Logical Consequence*, Cambridge, MA: Harvard University Press.

[^etchemendy-2008]: –––, 2008. “Reflections on Consequence” in *New Essays on Tarski and Philosophy*, Douglas Patterson (ed.), New York: Oxford University Press, pp. 263–299.

[^evans-1976]: Evans, G., 1976. “Semantic Structure and Logical Form,” in G. Evans and J. McDowell (eds.), *Truth and Meaning: Essays in Semantics*, Oxford: Clarendon Press, 199–222.

[^feferman-1999]: Feferman, S., 1999. “Logic, Logics, and Logicism,” *Notre Dame Journal of Formal Logic*, 40: 31–54.

[^feferman-2010]: –––, 2010. “Set-theoretical Invariance Criteria for Logicality,” *Notre Dame Journal of Formal Logic*, 51: 3–19.

[^feferman-2015]: –––, 2015. “Which Quantifiers are Logical? A combined semantical and inferential criterion,” In Alessandro Torza (ed.), *Quantifiers, Quantifiers, and Quantifiers*, Dordrecht: Springer (Synthese Library).

[^føllesdal-1980]: Føllesdal, D., 1980. “Comments on Quine,” in S. Kanger and S. Öhman (eds.), *Philosophy and Grammar*, Dordrecht: D. Reidel, 29–35.

[^frege-1885]: Frege, G., 1885. “Über formale Theorien der Arithmetik” (“On Formal Theories of Arithmetic”). *Sitzungsberichte der Jenaischen Gesellschaft für Medizin und Naturwissenschaft* (Supplement), 2: 94–104.

[^frege-1906]: –––, 1906. “Über die Grundlagen der Geometrie II” (“On the Foundations of Geometry: Second series”). *Jahresbericht der Deutschen Mathematiker Vereiningung*, 15: 293–309, 377–403, 423–430.

[^frege-1984]: –––, 1984. *Collected Papers on Mathematics, Logic, and Philosophy*, Oxford: Basil Blackwell.

[^gabbay-1994]: Gabbay, D. M. (ed.), 1994. *What Is a Logical System?* Oxford: Clarendon Press.

[^gentzen-1935]: Gentzen, G., 1935. “Untersuchungen über das logische Schliessen” (“Investigations into Logical Deduction”). *Mathematisches Zeitschrift*, 39: 176–210, 405–431.

[^gentzen-1969]: –––, 1969. *The Collected Papers of Gerhard Gentzen*, Amsterdam: North Holland.

[^gómez-torrente-2002]: Gómez-Torrente, M., 2002. “The Problem of Logical Constants,” *Bulletin of Symbolic Logic*, 8: 1–37.

[^goodman-1961]: Goodman, N., 1961. “About,” *Mind*, 70: 1–24.

[^haack-1978]: Haack, S., 1978. *Philosophy of Logics*, Cambridge: Cambridge University Press.

[^hacking-1979]: Hacking, I., 1979. “What is Logic?” *Journal of Philosophy* 76: 285–319.

[^harman-1972]: Harman, G., 1972. “Is Modal Logic Logic?” *Philosophia*, 2: 75–84.

[^harman-1984]: –––, 1984. “Logic and Reasoning,” *Synthese*, 60: 107–127.

[^hodes-2004]: Hodes, H., 2004. “On the Sense and Reference of a Logical Constant,” *Philosophical Quarterly*, 54: 134–165.

[^kaplan-1989]: Kaplan, D., 1989. “Demonstratives: An Essay on the Semantics, Logic, Metaphysics, and Epistemology of Demonstratives and Other Indexicals,” in J. Almog, J. Perry, and H. Wettstein (eds.), *Themes from Kaplan*, Oxford: Oxford University Press, 481–566.

[^klein-1893]: Klein, F., 1893. “A Comparative Review of Recent Researches in Geometry,” *New York Mathematical Society Bulletin*, 2: 215–249.

[^kneale-1956]: Kneale, W., 1956. “The Province of Logic,” in H. D, Lewis (ed.), *Contemporary British Philosophy*, London: George Allen and Unwin, 237–261.

[^kneale-1962]: Kneale, W. and M. Kneale, 1962. *The Development of Logic*, Oxford: Oxford University Press.

[^koslow-1992]: Koslow, A., 1992. *A Structuralist Theory of Logic*, Cambridge: Cambridge University Press.

[^koslow-1999]: –––, 1999. “The Implicational Nature of Logic: A Structuralist Account,” *European Philosophical Review*, 4: 111–155.

[^kremer-1988]: Kremer, M., 1988. “Logic and Meaning: The Philosophical Significance of the Sequent Calculus,” *Mind*, 47: 50–72.

[^kretzmann-1982]: Kretzmann, N., 1982. “Syncategorema, Exponibilia, Sophismata,” in N. Kretzmann, A. Kenny, and J. Pinborg (eds.), *The Cambridge History of Later Medieval Philosophy*, Cambridge: Cambridge University Press, 211–245.

[^kripke-1971]: Kripke, S., 1971. “Identity and Necessity,” in M. K. Munitz (ed.), *Identity and Individuation*, New York: New York University Press, 135–64.

[^kripke-1980]: –––, 1980. *Naming and Necessity*, Cambridge: Harvard University Press.

[^kuhn-1981]: Kuhn, S. T., 1981. “Logical Expressions, Constants, and Operator Logic,” *Journal of Philosophy*, 78: 487–499.

[^lakoff-1970]: Lakoff, G., 1970. “Linguistics and Natural Logic,” *Synthese*, 22: 151–271.

[^lepore-2002]: Lepore, E. and K. Ludwig, 2002. “What is Logical Form?” in G. Preyer and G. Peter (eds.), *Logical Form and Language*, Oxford: Clarendon Press, 54–90.

[^lewis-1988]: Lewis, D., 1988. “Relevant Implication,” *Theoria*, 54: 161–174.

[^lindenbaum-1934]: Lindenbaum, A. and A. Tarski, 1934–5. “Über die Beschränktheit der Ausdrucksmittel deduktiver Theorien” (“On the Limitations of the Means of Expression of Deductive Theories”). *Ergebnisse eines mathematischen Kolloquiums*, 7: 15–22. (English translation in Tarski 1983.)

[^lycan-1989]: Lycan, W. G., 1989. “Logical Constants and the Glory of Truth-conditional Semantics,” *Notre Dame Journal of Formal Logic*, 30: 390–401.

[^macfarlane-2002]: MacFarlane, J., 2002. “Frege, Kant, and the Logic in Logicism,” *Philosophical Review*, 111, 25–65.

[^massey-1975]: Massey, G. J., 1975. “Are There Any Good Arguments that Bad Arguments are Bad?” *Philosophy in Context*, 4: 61–77.

[^mautner-1946]: Mautner, F. I., 1946. “An Extension of Klein’s Erlanger Program: Logic as Invariant-theory,” *Americal Journal of Mathematics* 68: 345–384.

[^mccarthy-1981]: McCarthy, T., 1981. “The Idea of a Logical Constant,” *Journal of Philosophy*, 78: 499–523.

[^mccarthy-1987]: –––, 1987. “Modality, Invariance, and Logical Truth,” *Journal of Philosophical Logic*, 16: 423–443.

[^mccarthy-1998]: –––, 1998. “Logical Constants,” in E. Craig (ed,), *Routledge Encyclopedia of Philosophy* (Volume 5), London: Routledge, 599–603.

[^mcgee-1996]: McGee, V., 1996. “Logical Operations,” *Journal of Philosophical Logic*, 25: 567–580.

[^milne-1994]: Milne, P., 1994. “Clasical Harmony: Rules of Inference and the Meaning of the Logical Constants.” *Synthese*, 100: 49–94.

[^mostowski-1957]: Mostowski, A., 1957. “On a Generalization of Quantifiers,” *Fundamenta Mathematicae*, 44: 12–35.

[^neale-1990]: Neale, S., 1990. *Descriptions*, Cambridge, MA: MIT Press.

[^peacocke-1976]: Peacocke, C., 1976. “What Is a Logical Constant?” *Journal of Philosophy*, 73: 221–240.

[^peacocke-1987]: –––, 1987. “Understanding Logical Constants: A Realist’s Account,” *Proceedings of the British Academy*, 73: 153–200. Reprinted in T. J. Smiley and T. R. Baldwin (eds.), *{Studies in the Philosophy of Logic and Knowledge* (Oxford: Oxford University Press, 2004), 163–208.

[^popper-1946]: Popper, K. R., 1946–7. “Logic Without Assumptions,” *Proceedings of the Aristotelian Society* (New Series), 47: 251–292.

[^popper-1947]: –––, 1947. “New Foundations for Logic,” *Mind*, 56: 193–235. (Errata in *Mind*, 57: 69.)

[^prawitz-1985]: Prawitz, D., 1985. “Remarks on Some Approaches to the Concept of Logical Consequence,” *Synthese*, 62: 153–171.

[^prawitz-2005]: –––, 2005. “Logical Consequence from a Constructive Point of View,” in S. Shapiro (ed.), *The Oxford Handbook of Philosophy of Mathematics and Logic*, Oxford: Oxford University Press, 671–95.

[^prior-1960]: Prior, A. N., 1960. “The Runabout Inference-ticket,” *Analysis*, 21: 38–39.

[^quine-1980]: Quine, W. V., 1980. “Grammar, Truth, and Logic,” in S. Kanger and S. Öman (eds.), *Philosophy and Grammar*, Dordrecht: D. Reidel, 17–28.

[^quine-1986]: –––, 1986. *Philosophy of Logic* (2nd edition), Cambridge: Harvard University Press.

[^radford-2004]: Radford, A., 2004. *Minimalist Syntax: Exploring the Structure of English*, Cambridge: Cambridge University Press.

[^read-1994]: Read, S., 1994. “Formal and Material Consequence,” *Journal of Philosophical Logic*, 23: 247–265.

[^read-2010]: –––, 2010. “General-Elimination Harmony and the Meaning of the Logical Constants,” *Journal of Philosophical Logic*, 39: 557–576.

[^ricketts-1997]: Ricketts, T., 1997. “Frege’s 1906 Foray into Metalogic,” *Philosophical Topics*, 25: 169–188.

[^russell-1920]: Russell, B., 1920. *Introduction to Mathematical Philosophy*, London. George Allen and Unwin.

[^russell-1992]: –––, 1992. *Theory of Knowledge: The 1913 Manuscript*, London: Routledge.

[^ryle-1954]: Ryle, G., 1954. *Dilemmas*, Cambridge: Cambridge University Press.

[^sainsbury-2001]: Sainsbury, M., 2001. *Logical Forms: An Introduction to Philosophical Logic* (2nd edition), Oxford: Blackwell.

[^schroeder-heister-1984]: Schroeder-Heister, P., 1984. “Popper’s Theory of Deductive Inference and the Concept of a Logical Constant,” *History and Philosophy of Logic*, 5: 79–110.

[^scott-1970]: Scott, D., 1970. “Advice on Modal Logic,” in K. Lambert (ed.), *Philosophical Problems in Logic: Some Recent Developments*, Dordrecht: D. Reidel, 143–173.

[^sellars-1962]: Sellars, W., 1962. “Naming and Saying,” *Philosophy of Science*, 29: 7–26.

[^shapiro-1991]: Shapiro, S., 1991. *Foundations Without Foundationalism: A Case for Second-Order Logic*, Oxford: Oxford University Press.

[^sher-1991]: Sher, G., 1991. *The Bounds of Logic: a Generalized Viewpoint*, Cambridge, MA: MIT Press.

[^sher-1996]: –––, 1996. “Did Tarski Commit ‘Tarski’s Fallacy’?” *Journal of Symbolic Logic*, 61: 653–686.

[^sher-2003]: –––, 2003. “A Characterization of Logical Constants *Is* Possible,” *Theoria: Revista de Teoria, Historia y Fundamentos de la Ciencia*, 18: 189–197.

[^steinberger-2011]: Steinberger, F., 2011. “What Harmony Could and Could Not Be.” *Australasian Journal of Philosophy*, 89: 617–39.

[^tarski-1936a]: Tarski, A., 1936a. “O pojeciu wynikania logicznego” (“On the Concept of Logical Consequence”). *Przeglad Filozoficzny*, 39: 58–68. (English translation in Tarski 2002.)

[^tarski-1936b]: –––, 1936b. “Über den Begriff der logischen Folgerung” (“On the Concept of Logical Consequence”), *Actes du Congrès International de Philosophie Scientifique*, 7: 1–11. (English translation in Tarski 1983, 409–20.)

[^tarski-1983]: –––, 1983. *Logic, Semantics, Metamathematics*, J. Corcoran (ed.). Indianapolis: Hackett.

[^tarski-1986]: –––, 1986. “What are Logical Notions?” *History and Philosophy of Logic*, 7: 143–154. (Transcript of a 1966 talk, ed. J. Corcoran.)

[^tarski-1987]: –––, 1987. “A Philosophical Letter of Alfred Tarski,” *Journal of Philosophy*, 84: 28–32. (Letter to Morton White, written in 1944.)

[^tarski-2002]: –––, 2002. “On the Concept of Following Logically,” *History and Philosophy of Logic*, 23: 155–196. (Translation of Tarski 1936a by M. Stroinska and D. Hitchcock.)

[^tennant-1987]: Tennant, N., 1987. *Anti-realism and Logic.* Oxford: Clarendon Press.

[^tharp-1975]: Tharp, L. H., 1975. “Which Logic Is the Right Logic?” *Synthese*, 31: 1–21.

[^benthem-1989]: van Benthem, J., 1989. “Logical Constants Across Varying Types,” *Notre Dame Journal of Formal Logic*, 30: 315–342.

[^wagner-1987]: Wagner, S. J., 1987. “The Rationalist Conception of Logic,” *Notre Dame Journal of Formal Logic*, 28: 3–35.

[^warmbrod-1999]: Warmbrod, K., 1999. “Logical Constants,” *Mind*, 108: 503–538.

[^wittgenstein-1922]: Wittgenstein, L., 1922. *Tractatus Logico-Philosophicus*, Trans. C. K. Ogden. London: Routledge and Kegan Paul.

[^wittgenstein-1958]: –––, 1958. *Philosophical Investigations* (2nd ed.). Trans. G. E. M. Anscombe. Oxford: Blackwell.

[^wright-1983]: Wright, C., 1983. *Frege’s Conception of Numbers as Objects*, Scots Philosophical Monographs, Aberdeen: Aberdeen University Press.

[^zucker-1978]: Zucker, J. I., 1978. “The Adequacy Problem for Classical Logic,” *Journal of Philosophical Logic*, 7: 517–535.

[^zucker-1978-2]: –––, and R. S. Tragesser, 1978. “The Adequacy Problem for Inferential Logic,” *Journal of Philosophical Logic*, 7: 501–516.
