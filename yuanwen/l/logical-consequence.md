# Logical Consequence
**First published Fri Jan 7, 2005; substantive revision Fri May 17, 2024**

*Beall, Jc, Restall, Greg, Sagi, Gil*

A good argument is one whose conclusions follow from its premises; its conclusions are *consequences* of, or *entailed by*, its premises. But in what sense do conclusions *follow from* premises? What is it for a conclusion to be a *consequence of*, or *entailed by*, premises? Those questions, in many respects, are at the heart of logic (as a philosophical discipline). In this entry we'll primarily talk in terms of conclusions *following from* or being a *consequence of* premises, since *entailment* is sometimes used elsewhere in philosophy and logic in a different or stronger sense.

Consider the following argument:

1. If we charge high fees for university, only the rich will enroll. We charge high fees for university. Therefore, only the rich will enroll.

There are many different things one can say about this argument, but many agree that if we do not equivocate (if the terms mean the same thing in the premises and the conclusion) then the argument is *valid*, that is, the conclusion follows deductively from the premises. This does not mean that the conclusion is true. Perhaps the premises are not true. However, if the premises are true, then the conclusion is also true, as a matter of logic. This entry is about the relation between premises and conclusions in valid arguments.

Contemporary analyses of the concept of consequence—of the *follows from* relation—take it to be both *necessary* and *formal*, with such answers often being explicated via *proofs* or *models* (or, in some cases, both). Our aim in this article is to provide a brief characterisation of some of the notions that play a central role in contemporary accounts of logical consequence.

We should note that we only highlight a few of the *philosophical* aspects of logical consequence, leaving out almost all technical details, and also leaving out a large number of philosophical debates about the topic. Our rationale for doing as much is that one will get the technical details, and the particular philosophical issues that motivated them, from looking at *specific logics*—specific theories of logical consequence (e.g., relevant logics, substructural logics, non-monotonic logics, dynamic logics, modal logics, theories of quantification, and so on). (Moreover, debates about almost any feature of language—structure versus form of sentences, propositions, context sensitivity, meaning, even truth—are relevant to debates about logical consequence, making an exhaustive discussion practically impossible.) Our aim here is simply to touch on a few of the very basic issues that are central to logical consequence.

## 1. Deductive and Inductive Consequence

Some arguments are such that the (joint) truth of the premises is *necessarily sufficient* for the truth of the conclusions. In the sense of *logical consequence* central to the current tradition, such “necessary sufficiency” distinguishes deductive validity from *inductive* validity. In inductively valid arguments, the (joint) truth of the premises is *very likely (but not necessarily) sufficient* for the truth of the conclusion. An inductively valid argument is such that, as it is often put, its premises make its conclusion more likely or more reasonable (even though the conclusion may well be untrue given the joint truth of the premises). The argument

1. All swans observed so far have been white. Smoothy is a swan. Therefore, Smoothy is white.

is not deductively valid because the premises are not necessarily sufficient for the conclusion. Smoothy may well be a black swan.

Distinctions can be drawn between different inductive arguments. Some inductive arguments seem quite reasonable, and others are less so. There are many different ways to attempt to analyse inductive consequence. We might consider the degree to which the premises make the conclusion *more likely* (a probabilistic reading), or we might check whether the most *normal* circumstances in which the premises are true render the conclusion true as well. (This leads to some kinds of default or non-monotonic inference.) The field of inductive consequence is difficult and important, but we shall leave that topic here and focus on *deductive* validity.

(See the entries on inductive logic and non-monotonic logic for more information on these topics.)

The constraint of *necessity* is not sufficient to settle the notion of deductive validity, for the notion of *necessity* may also be fleshed out in a number of ways. To say that a conclusion necessarily follows from the premises is to say that the argument is somehow *exceptionless*, but there are many different ways to make that idea precise.

A first stab at the notion might use what we now call metaphysical necessity. Perhaps an argument is valid if it is *(metaphysically) impossible* for the premises to be true and the conclusion to be untrue, valid if—holding fixed the interpretations of premises and conclusion—in every possible world in which the premises hold, so does the conclusion. This constraint is plausibly thought to be a necessary condition for logical consequence (if it *could be* that the premises are true and the conclusion isn’t, then there is no doubt that the conclusion does not follow from the premises); however, on most accounts of logical consequence, it is not a sufficient condition for validity. Many admit the existence of *a posteriori* necessities, such as the claim that water is H$_2$O. If that claim is necessary, then the argument:

1. $x$ is water. Therefore, $x$ is H$_2$O.

is necessarily truth preserving, but it seems a long way from being deductively valid. It was a genuine discovery that water is H$_2$O, one that required significant empirical investigation. While there may be genuine discoveries of valid arguments that we had not previously recognised as such, it is another thing entirely to think that these discoveries require empirical investigation.

An alternative line on the requisite sort of *necessity* turns to *conceptual necessity*. On this line, the conclusion of (3) is not a consequence of its premise given that it is not a conceptual truth that water is H$_2$O. The concept *water* and the concept $H_2O$ happen to pick out the same property, but this agreement is determined partially by the world.

A similar picture of logic takes consequence to be a matter of what is *analytically* true, and it is not an analytic truth that water is H$_2$O. The word “water” and the formula “H$_2$O” agree in extension (and necessarily so) but they do not agree in *meaning*.

If metaphysical necessity is too coarse a notion to determine logical consequence (since it may be taken to render too many arguments deductively valid), an appeal to conceptual or analytic necessity might seem to be a better route. The trouble, as Quine argued, is that the distinction between analytic and synthetic (and similarly, conceptual and non-conceptual) truths is not as straightforward as we might have thought in the beginning of the 20th Century. (See the entry on the analytic/synthetic distinction.) Furthermore many arguments seem to be truth-preserving on the basis of analysis alone:

1. Peter is Greg’s mother’s brother’s son. Therefore, Peter is Greg’s cousin.

One can understand that the conclusion follows from the premises, on the basis of one’s understanding of the concepts involved. One need not know anything about the identity of Peter, Greg’s cousin. Still, many have thought that (4) is not deductively valid, despite its credentials as truth-preserving on analytic or conceptual grounds. It is not quite as general as it could be because it is not as *formal* as it could be. The argument succeeds only because of the particular details of family concepts involved.

A further possibility for carving out the distinctive notion of *necessity* grounding logical consequence is the notion of *apriority*. Deductively valid arguments, whatever they are, can be known to be so without recourse to experience, so they must be knowable *a priori*. A constraint of apriority certainly seems to rule argument (3) out as deductively valid, and rightly so. However, it will not do to rule out argument (4). If we take arguments like (4) to turn not on matters of deductive validity but something else, such as an *a priori* knowable definition, then we must look elsewhere for a characterisation of logical consequence.

## 2. Formal and Material Consequence

The strongest and most widespread proposal for finding a narrower criterion for logical consequence is the appeal to *formality*. The step in (4) from “Peter is Greg’s mother’s brother’s son” to “Peter is my cousin” is a *material* consequence and not a formal one, because to make the step from the premise to the conclusion we need more than the *structure* or *form* of the claims involved: we need to understand their *contents* too.

What could the distinction between *form* and *content* mean? We mean to say that consequence is formal if it depends on the *form* and not the *substance* of the claims involved. But how is that to be understood? We will give at most a sketch, which, again, can be filled out in a number of ways.

The obvious first step is to notice that all presentations of the *rules* of logical consequence rely on schemes. Aristotle’s syllogistic is a proud example.

F*e*r*io*: No $F$ is $G$. Some $H$ is $G$. Therefore some $H$ is not $F$.

Inference schemes, like the one above, display the structure of valid arguments. Perhaps to say that an argument is formally valid is to say that it falls under some general scheme of which every instance is valid, such as F*e*r*io*.

That, too, is an incomplete specification of formality. The material argument (4) is an instance of:

1. $x$ is $y$’s mother’s brother’s son. Therefore, $x$ is $y$’s cousin.

every instance of which is valid. We must say more to explain why some schemes count as properly formal (and hence a sufficient ground for logical consequence) and others do not. A general answer will articulate the notion of logical form, which is an important issue in its own right (involving the notion of logical constants, among other things). Instead of exploring the details of different candidates for logical form, we will mention different proposals about the *point* of the exercise.

What is the point in demanding that validity be underwritten by a notion of logical form? There are at least three distinct proposals for the required notion of formality, and each provides a different kind of answer to that question.

We might take the formal rules of logic to be totally *neutral* with respect to particular features of *objects*. Laws of logic, on this view, must abstract away from particular features of objects. Logic is formal in that it is totally *general*. One way to characterise what counts as a totally *general notion* is by way of permutations. Tarski proposed (1986) that an operation or predicate on a domain counted as general (or logical) if it was invariant under permutations of objects. (A permutation of a collection of objects assigns for each object a unique object in that collection, such that no object is assigned more than once. A permutation of $\{a, b, c, d\}$ might, for example, assign $b$ to $a, d$ to $b, c$ to $c$ and $a$ to $d$.) A $2$-place predicate $R$ is invariant under permutation if for any permutation $p$, whenever $Rxy$ holds, $Rp(x)p(y)$ holds too. You can see that the *identity* relation is permutation invariant—if $x = y$ then $p(x) = p(y)$—but the *mother-of* relation is not. We may have permutations $p$ such that even though $x$ is the mother of $y$, $p(x)$ is not the mother of $p(y)$. We may use permutation to characterise logicality for more than predicates too: we may say that a one-place sentential connective ‘$\bullet$’ is permutation invariant if and only if, for all $A$, $p(\bullet A)$ is true if and only if $\bullet p(A)$ is true. Defining this rigorously requires establishing how permutations operate on sentences, and this takes us beyond the scope of this article. Suffice to say, an operation such as negation passes the test of invariance, but an operation such as ‘JC believes that’ fails.

A closely related analysis for formality is that formal rules are totally *abstract*. They abstract away from the semantic *content* of thoughts or claims, to leave only semantic structure. The terms ‘mother’ and ‘cousin’ enter essentially into argument (5). On this view, expressions such as propositional connectives and quantifiers do not add new semantic content to expressions, but instead add only ways to combine and structure semantic content. Expressions like ‘mother’ and ‘cousin’, by contrast, add new semantic content.

Another way to draw the distinction (or to perhaps to draw a different distinction) is to take the formal rules of logic to be *constitutitive norms* for thought, regardless of its subject matter. It is plausible to hold that no matter what we think about, it makes sense to conjoin, disjoin and negate our thoughts to make new thoughts. It might also make sense to quantify. The behaviour, then, of logical vocabulary may be used to structure and regulate *any* kind of theory, and the norms governing logical vocabulary apply totally universally. The norms of valid argument, on this picture, are those norms that apply to thought irrespective of the particular content of that thought.[^note-1]

## 3. Mathematical Tools: Models and Proofs

Twentieth Century *technical* work on the notion of logical consequence has centered on two different mathematical tools, proof theory and model theory. Each of these can be seen as explicating different aspects of the concept of logical consequence, backed by different philosophical perspectives.

### 3.1 The model-theoretic account of logical consequence

We have characterized logical consequence as *necessary truth preservation in virtue of form*. This idea can be explicated formally. One can use mathematical structures to account for the range of possibilities over which truth needs to be preserved. The formality of logical consequence can be explicated formally by giving a special role to the logical vocabulary, taken as constituting the forms of sentences. Let us see how model theory attends to both these tasks.

The *model-centered approach* to logical consequence takes the validity of an argument to be *absence of counterexample*. A *counterexample* to an argument is, in general, some way of manifesting the manner in which the premises of the argument *fail* to lead to a conclusion. One way to do this is to provide an argument of the same form for which the premises are clearly true and the conclusion is clearly false. Another way to do this is to provide a *circumstance* in which the premises are true and the conclusion is false. In the contemporary literature, the intuitive idea of a counterexample is developed into a theory of *models*.

The exact structure of a model will depend on the kind of language at hand (extensional/intensional, first/higher-order, etc.). A model for an extensional first order language consists of a non-empty set which constitutes the *domain*, and an *interpretation function*, which assigns to each nonlogical term an extension over the domain—any extension agreeing with its semantic type (individual constants are assigned elements of the domain, function symbols are assigned functions from the domain to itself, one-place first-order predicates are assigned subsets of the domain, etc.).

The contemporary model-theoretic definition of logical consequence traces back to Tarski (1936)[^tarski-1936]. It builds on the definition of *truth in a model* given by Tarski in (1935). Tarski defines a *true sentence in a model* recursively, by giving truth (or satisfaction) conditions on the logical vocabulary. A conjunction, for example, is true in a model if and only if both conjuncts are true in that model. A universally quantified sentence $\forall xFx$ is true in a model if and only if each instance is true in the model. (Or, on the Tarskian account of satisfaction, if and only if the open sentence $Fx$ is satisfied by every object in the domain of the model. For detail on how this is accomplished, see the entry on Tarski’s truth definitions.) Now we can define logical consequence as preservation of truth over models: an argument is valid if in any *model* in which the premises are true (or in any *interpretation* of the premises according to which they are true), the conclusion is true too.

The model-theoretic definition is one of the most successful mathematical explications of a philosophical concept to date. It promises to capture both the necessity of logical consequence—by looking at truth over all models, and the formality of logical consequence—by varying the interpretations of the nonlogical vocabulary across models: an argument is valid no matter what the nonlogical vocabulary means. Yet, models are just sets, which are merely mathematical objects. How do they account for the range of possibilities, or circumstances required? John Etchemendy (1990)[^etchemendy-1990] offers two perspectives for understanding models. On the *representational approach*, each model is taken to represent a possible world. If an argument preserves truth over models, we are then guaranteed that it preserves truth over possible worlds, and if we accept the identification of necessity with truth in all possible worlds, we have the necessary truth preservation of logical consequence. The problem with this approach is that it identifies logical consequence with metaphysical consequence, and it gives no account of the formality of logical consequence. On the representational approach, there is no basis for a distinction between the logical and the nonlogical vocabulary, and there is no explanation of why the interpretations of the nonlogical vocabulary are maximally varied. The second perspective on models is afforded by the *interpretational approach*, by which each model assigns extensions to the nonlogical vocabulary from the actual world: what varies between models is not the world depicted but the meaning of the terms. Here, the worry is that necessity isn’t captured. For instance, on the usual division of the vocabulary into logical and nonlogical, identity is considered a logical term, and can be used to form statements about the cardinality of the domain (e.g., ‘‘there are at least two things’’) which are true under every reinterpretation, but perhaps are not necessarily true. On this approach, there is no basis for considering models with domains other than the universe of what actually exists, and specifically, there is no explanation of model theory’s use of domains of different sizes. Each approach, as described here, is flawed with respect to our analysis of logical consequence as necessary and formal. The interpretational approach, by looking only at the actual world fails to account for necessity, and the representational approach fails to account for formality (for details, see Etchemendy 1990, Sher 1996, and Shapiro 1998, and for refinements see Etchemendy 2008)[^etchemendy-1990][^etchemendy-2008][^shapiro-1998][^sher-1996]. A possible response to Etchemendy would be to blend the representational and the interpretational perspectives, viewing each model as representing a possible world under a re-interpretation of the nonlogical vocabulary (Shapiro 1998, see also Sher 1996 and Hanson 1997 for alternative responses)[^hanson-1997][^shapiro-1998][^sher-1996].

One of the main challenges set by the model-theoretic definition of logical consequence is to distinguish between the logical and the nonlogical vocabulary. The logical vocabulary is defined in all models by the recursive clauses (such as those mentioned above for conjunction and the universal quantifier), and in that sense its meaning is fixed. The choice of the logical vocabulary determines the class of models considered when evaluating validity, and thus it determines the class of the logically valid arguments. Now, while each formal language is typically defined with a choice of a logical vocabulary, one can ask for a more principled characterization of logical vocabulary. Tarski left the question of a principled distinction open in his 1936, and only gave the lines of a relativistic stance, by which different choices of the logical vocabulary may be admissible. Others have proposed criteria for logicality, demanding that logical constants be appropriately formal, general or topic neutral (for references and details, see the entry on logical constants). Note that a choice of the logical vocabulary is a special case of setting constraints on the class of models to be used. It has been suggested that the focus on criteria for the logical vocabulary misses this point, and that more generally the question is which *semantic constraints* should be adopted, limiting the *admissible models* for a language (Sagi 2014a, Zinke 2017)[^sagi-2014a].

Another challenge faced by the model-theoretic account is due to the limitations of its set-theoretic basis. Recall that models are sets. The worry is that truth-preservation over models might not guarantee necessary truth preservation—moreover, it might not even guarantee material truth preservation (truth preservation in the actual world). The reason is that each model domain is a set, but the actual world presumably contains all sets, and as a collection which includes all sets is too ‘‘large’’ to be a set (it constitutes a *proper class*), the actual world is not accounted for by any model (see Shapiro 1987)[^shapiro-1987].

One way of dealing with this worry is to employ external means, such as proof theory, in support of the model-theoretic definition. This is done by Georg Kreisel in his “squeezing argument”, which we present in section 3.3. Kreisel’s argument crucially depends on the language in question having a sound and complete proof system. Another option is to use set-theoretic reflection principles. Generally speaking, reflection principles state that whatever is true of the universe of sets, is already true in an initial segment thereof (which is always a set). If reflection principles are accepted, then at least as concerns the relevant language, one can argue that an argument is valid if and only if there is no counter set-model (see Kreisel 1967, Shapiro 1987, Kennedy & Väänänen 2017)[^kennedy-2017][^kreisel-1967][^shapiro-1987].

Finally, the explanation of logical consequence in terms of truth in models is typically preferred by “Realists”, who take truth of sentences to be independent of what can be known. Explaining logical consequence in terms of truth in models is rather close to explaining logical consequence in terms of *truth*, and the analysis of truth-in-a-model is sometimes taken to be an explication of truth in terms of correspondence, a typically Realist notion. Some, however, view logical consequence as having an indispensable epistemic component, having to do with the way we establish the conclusion on the basis of the premises. “Anti-realists”, who eschew taking truth (or at least, correspondence-truth) as an explanatory notion, will typically prefer explaining logical consequence in terms of *proof*—to which we turn next.

### 3.2 The proof-theoretic account of logical consequence

On the *proof-centered approach* to logical consequence, the validity of an argument amounts to there being a *proof* of the conclusions from the premises. Exactly what proofs *are* is a big issue but the idea is fairly plain (at least if you have been exposed to some proof system or other). Proofs are made up of small steps, the primitive inference principles of the proof system. The 20th Century has seen very many different kinds of proof systems, from so-called Hilbert proofs, with simple rules and complex axioms, to natural deduction systems, with few (or even no) axioms and very many rules.

The proof-centered approach highlights epistemic aspects of logical consequence. A proof does not merely attest to the validity of the argument: it provides the steps by which we can establish this validity. And so, if a reasoner has grounds for the premises of an argument, and they infer the conclusion via a series of applications of valid inference rules, they thereby obtain grounds for the conclusion (see Prawitz 2012)[^prawitz-2012]. One can go further and subscribe to *inferentialism*, the view by which the meaning of expressions is determined by their role in inference. The idea is that our use of a linguistic expression is regulated by rules, and mastering the rules suffices for understanding the expression. This gives us a preliminary restriction on what semantic values of expressions can be: they cannot make any distinctions not accounted for by the rules. One can then go even further, and reject any kind of meaning that goes beyond the rules—adopting the later Wittgensteinian slogan “meaning is use”. This view is favored by anti-realists about meaning, since meaning on this view is fully explained by what is knowable.

The condition of necessity on logical consequence obtains a new interpretation in the proof-centered approach. The condition can be reformulated thus: in a valid argument, the truth of the conclusion follows from the truth of the premises by necessity of thought (Prawitz 2005)[^prawitz-2005]. Let us parse this formulation. *Truth* is understood *constructively*: sentences are true in virtue of *potential evidence* for them, and the facts described by true sentences are thus conceived as constructed in terms of potential evidence. (Note that one can completely forgo reference to truth, and instead speak of assertibility or acceptance of sentences.) Now, the necessity of thought by which an argument is valid is explained by the meaning of the terms involved, which compels us to accept the truth of the conclusion given the truth of the premises. Meanings of expressions, in turn, are understood through the rules governing their use: the usual *truth conditions* give their way to *proof conditions* of formulas containing an expression.

One can thus provide a *proof-theoretic semantics* for a language (Schroeder-Heister 1991)[^schroeder-heister-1991]. When presenting his system of natural deduction, Gentzen remarked that the introduction rules for the logical expressions represent their “definitions,” and the elimination rules are consequences of those definitions (Gentzen 1933). For example, the introduction rule for conjunction dictates that a conjunction $A \amp B$ may be inferred from both conjuncts $A$ and $B$, and this rule captures the meaning of the connective. Conversely, the elimination rule for conjunction says that from $A \amp B$ one may infer both $A$ and $B$. The universal quantifier rules tell us that from the universally quantified claim $\forall xFx$ we can infer any instance $Fa$, and we can infer $\forall xFx$ from the instance $Fa$, provided that no other assumption has been made involving the name $a$. Under certain requirements, one can show that the elimination rule is validated by the introduction rule.

One of the main challenges for the proof-centered approach is that of distinguishing between rules that are genuinely meaning-determining and those that are not. Some rules for connectives, if added to a system, would lead to triviality. Prior (1960)[^prior-1960] offered the following rules for a connective “$\tonk$”. Its introduction rule says that from $A$ one can infer $A \tonk B$, and its elimination rule says that from $A \tonk B$ one can infer $B$. With the introduction of these rules, the system becomes trivial so long as at least one thing is provable, since from any assumption $A$ one can derive any conclusion $B$. Some constraints have to posed on inference rules, and much of subsequent literature has been concerned with these constraints (Belnap 1962, Dummett 1991, Prawitz 1974)[^dummett-1991][^belnap-1962][^prawitz-1974].

To render the notions of proof and validity more systematized, Prawitz has introduced the notion of a *canonical proof*. A sentence might be proved in several different ways, but it is the direct, or canonical proof that is constitutive of its meaning. A canonical proof is a proof whose last step is an application of an introduction rule, and its immediate subproofs are canonical (unless they have free variables or undischarged assumptions—for details see Prawitz 2005)[^prawitz-2005]. A canonical proof is conceived as giving direct evidence for the sentence proved, as it establishes the truth of the sentence by the rule constitutive of the meaning of its connectives. For more on canonical proofs and the ways other proofs can be reduced to them, see the entry on proof-theoretic semantics.

We have indicated how the condition of necessity can be interpreted in the proof-centered approach. The condition of formality can be accounted for as well. Note that on the present perspective as well, there is a division of the vocabulary into logical and nonlogical. This division can be used to define *substitutions* of an argument. A substitution of an argument is an argument obtained from the original one by replacing the nonlogical terms with terms of the same syntactic category in a uniform manner. A definition of validity that respects the condition of formality will entail that an argument is valid if and only if all its substitutions are valid, and in the present context, this is a requirement that there is a proof of all its substitutions. This condition is satisfied in any proof system where rules are given only for the logical vocabulary. Of course, in the proof-centered approach as well, there is a question of distinguishing the logical vocabulary (see the entry on logical constants).

Finally, it should be noted that a proof theoretic semantics can be given for classical logic as well as a variety of non-classical logics. However, due to the epistemic anti-realist attitude that lies at the basis of the proof-centered approach, its proponents have typically advocated intuitionistic logic (see Dummett 1991)[^dummett-1991].

For more on the proof-centered perspective and on proof-theoretic semantics, see the entry on proof-theoretic semantics.

### 3.3 Between models and proofs

The proof-theoretic and model-theoretic perspectives have been considered as providing rival accounts of logical consequence. However, one can also view “logical consequence” and “validity” as expressing *cluster concepts*: “A number of different, closely related notions go by those names. They invoke matters of modality, meaning, effectiveness, justification, rationality, and form” (Shapiro 2014)[^shapiro-2014]. One can also note that the division between the model-theoretic and the proof-theoretic perspectives is a modern one, and it was only made possible when tools for metamathematical investigations were developed. Frege’s *Begriffsschrift*, for instance, which predates the development of those tools, is formulated as an axiomatic proof system, but the meanings of the connectives are given via truth conditions.

Once there are two different analyses of a relation of logical consequence, one can ask about possible interactions, and we’ll do that next. One can also ask what general features such a relation has independently of its analysis as proof-theoretic or model-theoretic. One way of answering this question goes back to Tarski, who introduced the notion of consequence operations. For our purposes, we note only some features of such operations. Let $Cn(X)$ be the consequences of $X$. (One can think of the operator $Cn$ as deriving from a prior consequence relation which, when taking $X$ as ‘input (or premise)’ set, tells you what follows from $X$. But one can also see the ‘process’ in reverse, and a key insight is that consequence relations and corresponding operations are, in effect, interdefinable. See the entry on algebraic propositional logic for details.) Among some of the minimal conditions one might impose on a consequence relation are the following two (from Tarski):

1. $X$ is a subset of $Cn(X)$.
2. $Cn(Cn(X)) = Cn(X)$.

If you think of $X$ as a set of claims, then the first condition tells you that the consequences of a set of claims includes the claims themselves. The second condition demands that the consequences of $X$ just are the consequences of the consequences of $X$. Both of these conditions can be motivated from reflection on the model-theoretic and proof-theoretic approaches; and there are other such conditions too. (For a general discussion, see the entry on algebraic propositional logic.) But as with many foundation issues (e.g., ‘what are the essential features of consequence relations in general?’), even such minimal conditions are contentious in philosophical logic and the philosophy of logic. For example, some might take condition (2) to be objectionable on the grounds that, for reasons of vagueness (or more), important consequence relations over natural languages (however formalized) are not generally transitive in ways reflected in (2). (See Tennant 1994, Cobreros et al 2012, and Ripley 2013, for philosophical motivations against transitive consequence.)[^cobreros-2012][^ripley-2013][^tennant-1994] But we leave these issues for more advanced discussion.

While the philosophical divide between Realists and Anti-realists remains vast, proof-centered and model-centered accounts of consequence have been united (at least with respect to extension) in many cases. The great soundness and completeness theorems for different proof systems (or, from the other angle, for different model-theoretic semantics) show that, in an important sense, the two approaches often coincide, at least in extension. A proof system is *sound* with respect to a model-theoretic semantics if every argument that has a proof in the system is model-theoretically valid. A proof system is *complete* with respect to a model-theoretic semantics if every model-theoretically valid argument has a proof in the system. While soundness is a principal condition on any proof system worth its name, completeness cannot always be expected. Admittedly, these definitions are biased towards the model-theoretic perspective: the model-theoretic semantic sets the standard to what is “sound” and “complete”. Leaving terminological issues aside, if a proof system is both sound and complete with respect to a model-theoretic semantics (as, significantly, in the case of first order predicate logic), then the proof system and the model-theoretic semantics agree on which arguments are valid.

Completeness results can also support the adequacy of the model-theoretic account, as in Kreisel’s “squeezing argument”. We have noted a weakness of the model-theoretic account: all models are sets, and so it might be that no model represents the actual world. Kreisel has shown that if we have a proof system that is “intuitively sound” and is complete with respect to the model-theoretic semantics, we won’t be missing any models: every intuitively valid argument will have a counter-model. Let $L$ be a first order language. Let $Val$ denote the set of intuitively valid arguments in $L$. Kreisel takes intuitive validity to be preservation of truth across all structures (whether sets or not). His analysis privileges the modal analysis of logical consequence—but note that the weakness we are addressing is that considering set-theoretic structures might not be enough. Let $V$ denote the set of model-theoretic validities in $L$: arguments that preserve truth over models. Let $D$ be the set of deductively valid arguments, by some accepted proof system for first order logic. Now, any such proof system is “intuitively sound”, meaning that what is deductively valid by the system is intuitively valid. This gives us $D \subseteq Val$. And obviously, by the definitions we’ve given, $Val \subseteq V$, since an argument that preserves truth over all structures will preserve truth over set-structures.

By the completeness result for first order logic, we have: $V$ ⊆ $D$. Putting the three inclusions together (the “squeeze”), we get that all three sets must be equal, and in particular: $V = Val$. In this way, we’ve proven that if there is some structure that is a counterexample to a first order argument, then there is a set-theoretic one.

Another arena for the interaction between the proof-theoretic and the model-theoretic perspectives has to do with the definition of the logical vocabulary. For example, one can hold a “moderate” inferentialist view which defines the meanings of logical connectives through their semantics (i.e. truth conditions) but demands that the meaning of a connective be determined by inference rules. Carnap has famously shown that the classical inference rules allow non-standard interpretations of the logical expressions (Carnap 1943)[^carnap-1943]. Much recent work in the field has been devoted to the exact nature and extent of Carnap’s categoricity problem (Raatikainen 2008, Murzi and Hjortland 2009, Woods 2012, Garson 2013, Peregrin 2014, Bonnay and Westerståhl 2016. See also the entry on sentence connectives in formal logic)[^bonnay-2016][^garson-2013][^murzi-2014][^murzi-2009][^peregrin-2014][^raatikainen-2008][^woods-2012].

Finally, we should note that while model theory and proof theory are the most prominent contenders for the explication of logical consequence, there are alternative frameworks for formal semantics such as algebraic semantics, game-theoretic semantics and dynamic semantics (see Wansig 2000).

## 4. Premises and Conclusions

There has also been dissent, even in Aristotle’s day, as to the “shape” of logical consequence. In particular, there is no settled consensus on the number of premises or conclusions appropriate to “tie together” the consequence relation.

In Aristotle’s syllogistic, a syllogism relates two or more premises and a single conclusion. In fact, Aristotle focuses on arguments with exactly two premises (the major premise and the minor premise), but nothing in his definition forbids arguments with three or more premises. Surely, such arguments should be permitted: if, for example, we have one syllogism from two premises $A$ and $B$ to a conclusion $C$, and we have another from the premises $C$ and $D$ to the conclusion $E$, then in some sense, the longer argument from premises $A, B$ and $D$ to conclusion $E$ is a good one. It is found by chaining together the two smaller arguments. If the two original arguments are formally valid, then so too is the longer argument from three premises. On the other hand, on a common reading of Aristotle’s definition of syllogism, *one*-premise arguments are ruled out—but this seems arbitrary, as even Aristotle’s own “conversion” inferences are thus excluded.

For such reasons, many have taken the relation of logical consequence to pair an arbitrary (possibly infinite) *collection* of premises with a single conclusion. This account has the added virtue of having the special case of an empty collection of premises. Arguments to a conclusion from no premises whatsoever are those in which the conclusion is true by logic alone. Such “conclusions” are *logical truths* (sometimes *tautologies*) or, on the proof-centered approach, *theorems*.

Perhaps there is a reason to allow the notion of logical consequence to apply even more broadly. In Gentzen’s proof theory for classical logic, a notion of consequence is defined to hold between multiple premises and multiple conclusions. The argument from a set $X$ of premises to a set $Y$ of conclusions is valid if the truth of every member of $X$ guarantees (in the relevant sense) the truth of some member of $Y$. There is no doubt that this is formally perspicuous, but the philosophical applicability of the multiple premise—multiple conclusion sense of logical consequence remains an open philosophical issue. In particular, those anti-Realists who take logical consequence to be defined in terms of *proof* (such as Michael Dummett) reject a multiple conclusion analysis of logical consequence. For an Anti-realist, who takes good inference to be characterised by the way *warrant* is transmitted from premise to conclusion, it seems that a multiple conclusion analysis of logical consequence is out of the question. In a multiple conclusion argument from $A$ to $B, C$, any warrant we have for $A$ does not necessarily transmit to $B$ or $C$: the only conclusion we are warranted to draw is the disjunction $B$ *or* $C$, so it seems for an analysis of consequence in terms of warrant we need to understand some logical vocabulary (in this case, disjunction) in order to understand the consequence relation. This is unacceptable if we hope to use logical consequence as a tool to *define* that logical vocabulary. No such problems appear to arise in a single conclusion setting. (However, see Restall (2005)[^restall-2005] for a defence of multiple conclusion consequence for Anti-realists; and see Beall (2011)[^beall-2011] for a defence of certain sub-classical multiple-conclusion logics in the service of non-classical solutions to paradox.)

Another line along which the notion has been broadened (or along which some have sought to broaden it) involves recent work on substructural logic. The proposal here is that we may consider doing without some of the standard rules governing the way that premises (or conclusions) of an argument may be combined. Structural rules deal with the *shape* or *structure* of an argument in the sense of the way that the premises and conclusions are collected together, and not the way that those statements are constructed. The structural rule of *weakening* for example, states that if an argument from some collection of premises $X$ to a conclusion $C$ is valid, then the argument from $X$ together with another premise $A$ to the conclusion $C$ is also valid. This rule has seemed problematic to some (chiefly on the grounds that the extra premise $A$ need not be used in the derivation of the conclusion $C$ and hence, that $C$ does not follow *from* the premises $X,A$ in the appropriate sense). *Relevant logics* are designed to respect this thought, and do without the structural rule of weakening. (For the proof-theoretic picture, see Negri and von Plato (2001).)

Other structural rules are also a called into question. Another possible application of substructural logic is found in the analysis of paradoxes such as Curry’s paradox. A crucial move in the reasoning in Curry’s paradox and other paradoxes like it seems to require the step reducing two applications of an assumption to a single one (which is then discharged). According to some, this step is problematic, and so, they must distinguish an argument from $A$ to $B$ and an argument from $A, A$ to $B$. The rule of *contraction* is rejected.

In yet other examples, the *order* in which premises are used is important and an argument from $A, B$ to $C$ is to be distinguished from an argument from $B, A$ to $C$. (For more details, consult the entry on substructural logics.) There is no doubt that the formal systems of substructural logics are elegant and interesting, but the case for the philosophical importance and applicability of substructural logics is not closed.

## 5. One or Many?

We have touched only on a few central aspects of the notion of logical consequence, leaving further issues, debates and, in particular, details to emerge from particular accounts (accounts that are well-represented in this encyclopedia). But even a quick glance at the *related links* section (below) will attest to a fairly large number of different logical theories, different accounts of what (logically) follows from what. And that observation raises a question with which we will close: Is there one notion of logical consequence that is the target of all such theories, or are there many?

We all agree that there are many different formal techniques for studying logical consequence, and very many different formal systems that each propose different relations of logical consequence. But given a particular argument, is the question as to whether it is deductively valid an all-or-nothing affair? The orthodoxy, logical *monism*, answers affirmatively. There is one relation of deductive consequence, and different formal systems do a better or worse job of modelling that relation. (See, for example, Priest 1999 for a defence of monism.)[^priest-1999] The logical *contextualist* or *relativist* says that the validity of an argument depends on the subject matter or the frame of reference or some other context of evaluation. (For example, a use of the law of the excluded middle might be valid in a classical mathematics textbook, but not in an intuitionistic mathematics textbook, or in a context where we reason about fiction or vague matters.) The logical *pluralist*, on the other hand, says that of one and the same argument, in one and the same context, there are sometimes different things one should say with respect to its validity. For example, perhaps one ought say that the argument from a contradictory collection of premises to an unrelated conclusion is *valid* in the sense that in virtue of its form it is not the case that the premises are true an the conclusion untrue (so it is valid in one precise sense) but that nonetheless, in another sense the form of the argument does not ensure that the truth of the premises *leads to* the truth of the conclusion. The monist or the contextualist holds that in the case of the one argument a single answer must be found for the question of its validity. The pluralist denies this. The pluralist holds that the notion of logical consequence itself may be made more precise in more than one way, just as the original idea of a “good argument” bifurcates into deductive and inductive validity (see Beall and Restall 2000 for a defence of pluralism)[^restall-2000][^beall-2000].

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

### History of Logical Consequence

#### Expositions

#### Source Material

### 20th Century Developments

### Philosophy of Logical Consequence

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=logical-consequence). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/logical-consequence/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=logical-consequence&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/logical-consequence/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- MacFarlane, John, 2000, [*What Does it Mean to Say that Logic is Formal?*](http://johnmacfarlane.net/dissertation.pdf), Ph. D. Dissertation, Philosophy Department, University of Pittsburgh.

## Related Entries

Aristotle, General Topics: logic | Bolzano, Bernard | Carnap, Rudolf | Frege, Gottlob: theorem and foundations for arithmetic | logic: algebraic propositional | logic: classical | logic: inductive | logic: intuitionistic | logic: non-monotonic | logic: normative status of | logic: substructural | logical constants | logical form | logical pluralism | logical truth | model theory | proof theory | Russell, Bertrand | schema | semantics: proof-theoretic

## Notes（原文脚注）

[^note-1]: The foregoing section owes much to the work of John MacFarlane in his thesis MacFarlane 2000 (Other Internet Resources). MacFarlane distinguished the three kinds of formality at which we have merely waved at here, and he provides a detailed discussion of the notions, making many distinctions over which we have passed.

[^coffa-1993]: Coffa, J. Alberto, 1993, *The Semantic Tradition from Kant to Carnap*, Linda Wessels (ed.), Cambridge: Cambridge University Press. An historical account of the Kantian origins of the rise of analytic philosophy and its development from Bolzano to Carnap.

[^kneale-1962]: Kneale, W. and Kneale, M., 1962, *The Development of Logic*, Oxford: Oxford University Press; reprinted, 1984. The classic text on the history of logic until the middle 20th Century.

[^ewald-1996]: Ewald, William, 1996, *From Kant to Hilbert: a source book in the foundations of mathematics* (Volumes I and II), Oxford: Oxford University Press. Reprints and translations of important Texts, including Bolzano on logical consequence.

[^heijenoort-1967]: van Heijenoort, Jean, 1967, *From Frege to Gödel: a sourcebook in mathematical logic 1879–1931*, Cambridge, MA: Harvard University Press. Reprints and translations of central texts in the development of logic.

[^husserl-1900]: Husserl, Edmund, 1900 [2001], *Logical Investigations* (Volumes 1 and 2), J. N. Findlay (trans.), Dermot Moran (intro.), London: Routledge.

[^mill-1872]: Mill, John Stuart, 1872 [1973], *A System of Logic* (8th edition), in J. M. Robson (ed.), *Collected works of John Stuart Mill* (Volumes 7 & 8), Toronto: University of Toronto Press.

[^anderson-1975]: Anderson, A.R., and Belnap, N.D., 1975, *Entailment: The Logic of Relevance and Necessity* (Volume I), Princeton: Princeton University Press.

[^anderson-1992]: Anderson, A.R., Belnap, N.D. Jr., and Dunn, J.M., 1992, *Entailment* (Volume II), Princeton: Princeton University Press. This book and the previous one summarise the work in relevant logic in the Anderson–Belnap tradition. Some chapters in these books have other authors, such as Robert K. Meyer and Alasdair Urquhart.

[^dummett-1991]: Dummett, Michael, 1991 *The Logical Basis of Metaphysics*, Cambridge, MA: Harvard University Press. Groundbreaking use of natural deduction proof to provide an anti-realist account of logical consequence as the central plank of a theory of meaning.

[^gentzen-1969]: Gentzen, Gerhard, 1969, *The Collected Papers of Gerhard Gentzen*, M. E. Szabo (ed.), Amsterdam: North Holland.

[^mancosu-1998]: Mancosu, Paolo, 1998, *From Brouwer to Hilbert*, Oxford: Oxford University Press. Reprints and translations of source material concerning the constructivist debates in the foundations of mathematics in the 1920s.

[^negri-2001]: Negri, Sara and von Plato, Jan, 2001, *Structural Proof Theory*, Cambridge: Cambridge University Press. A very accessible exposition of so-called structural proof theory (which involves a rejection of some of the standard structural rules at the heart of proof theory for classical logic).

[^shoesmith-1978]: Shoesmith D. J. and Smiley, T. J., 1978, *Multiple-Conclusion Logic*, Cambridge: Cambridge University Press. The first full-scale exposition and defence of the notion that logical consequence relates multiple premises and multiple conclusions.

[^restall-2000]: Restall, Greg, 2000, *An Introduction to Substructural Logics*, Lond: Routledge. ([Précis available online](http://consequently.org/isl/)) An introduction to the field of substructural logics.

[^tarski-1935]: Tarski, Alfred, 1935, “The Concept of Truth in Formalized Languages,” J.H. Woodger (trans.), in Tarski 1983, pp. 152–278.

[^tarski-1936]: –––, 1936, “On The Concept of Logical Consequence,” J.H. Woodger (trans.), in Tarski 1983, pp. 409–420.

[^tarski-1983]: –––, 1983, *Logic, Semantics, Metamathematics: papers from 1923 to 1938*, second edition, J. H. Woodger (trans.), J. Corcoran (ed.), Indianapolis, IN: Hackett.

[^there-nd]: There are many (many) other works on this topic, but the bibliographies of the following will serve as a suitable resource for exploring the field.

[^avron-1994]: Avron, Arnon, 1994, “What is a Logical System?” in *What is a Logical System?*, D.M. Gabbay (ed.), Oxford: Clarendon Press (Studies in Logic and Computation: Volume 4), pp. 217–238.

[^beall-2011]: Beall, Jc, 2011, “Multiple-conclusion LP and default classicality,” *Review of Symbolic Logic*, 4(2): 326–336.

[^beall-2000]: Beall, Jc and Restall, Greg, 2000, “Logical Pluralism,” *Australasian Journal of Philosophy*, 78: 457–493.

[^belnap-1962]: Belnap, Nuel D., 1962, “Tonk, Plonk and Plink,” *Analysis*, 22 (6): 130–134.

[^bonnay-2012]: Bonnay, Denis and Westerståhl, Dag, 2012, “Consequence Mining: Constants Versus Consequence Relations,” *Journal of Philosophical Logic*, 41(4): 671–709.

[^bonnay-2016]: –––, 2016, “ Compositionality Solves Carnap’s Problem,” *Erkenntnis*, 81 (4): 721–739.

[^brandom-1994]: Brandom, Robert, 1994, *Making It Explicit*, Cambridge, MA: Harvard University Press. [See especially Chapters 5 and 6 on the account of logical consequence according to which truth is not a fundamental explanatory notion.]

[^caret-2015]: Caret, Colin R. and Hjortland, Ole T. (eds.), 2015, *Foundations of Logical Consequence*, Oxford: Oxford University Press.

[^carnap-1943]: Carnap, Rudolf, 1943, *Formalization of Logic*, Cambridge, MA: Harvard University Press.

[^cobreros-2012]: Cobreros, Pablo; Égré, Paul; Ripley, David and van Rooij, Robert, 2012, “Tolerance and mixed consequence in the s’valuational setting,” *Studia Logica*, 100(4): 855–877.

[^etchemendy-1990]: Etchemendy, John, 1990, *The Concept of Logical Consequence*, Cambridge, MA: Harvard University Press.

[^etchemendy-2008]: –––, 2008, “Reflections on Consequence”, in D. Patterson (ed.), 2008.

[^garson-2013]: Garson, James W., 2013, *What Logics Mean: From Proof Theory to Model-Theoretic Semantics*, Cambridge: Cambridge University Press.

[^gomez-torrente-1996]: Gomez-Torrente, Mario, 1996, “Tarski on Logical Consequence,” *Notre Dame Journal of Formal Logic*, 37: 125–151.

[^griffiths-2022]: Griffiths, Owen, and Paseau, A.C., 2022, *One True Logic: A Monist Manifesto*, Oxford: Oxford University Press.

[^hanson-1997]: Hanson, William H., 1997, “The Concept of Logical Consequence,” *The Philosophical Review*, 106 (3): 365–409.

[^kennedy-2017]: Kennedy, Juliette and Väänänen, Jouko, 2017, “Squeezing arguments and strong logics,”, in Hannes Leitgeb, Ilkka Niiniluoto, Elliot Sober and P. Seppälä (eds.), *Logic, Methodology, and the Philosophy of Science: Proceedings of the Fifteenth International Congress* (CLMPS 2015), London: College Publications.

[^kreisel-1967]: Kreisel, Georg, 1967, “Informal Rigour and Completeness Proofs,” in I. Lakatos (ed.), *Problems in the Philosophy of Mathematics*, (Studies in Logic and the Foundations of Mathematics: Volume 47), Amsterdam: North Holland, pp. 138–186.

[^mcgee-1992]: McGee, Vann, 1992, “Two Problems with Tarski’s Theory of Consequence,” *Proceedings of the Aristotelian Society*, 92: 273–292.

[^murzi-2014]: Murzi, Julien and Carrara, Massimiliano, 2014, “More Reflections on Consequence,” *Logique et Analyse*, 57 (227): 223–258.

[^murzi-2009]: Murzi, Julien and Hjortland, Ole T., 2009, “Inferentialism and the Categoricity Problem: Reply to Raatikainen,” *Analysis*, 69 (3): 480–488.

[^patterson-2008]: Patterson, Douglas, (ed.), 2008, *New Essays on Tarski and Philosophy*, Oxford: Oxford University Press.

[^peregrin-2014]: Peregrin, Jaroslav, 2014, *Inferentialism: Why Rules Matter*, UK: Palgrave Macmillan.

[^prawitz-1974]: Prawitz, Dag, 1974, “On the Idea of a General Proof Theory,” *Synthese*, 27 (1–2): 63–77.

[^prawitz-1985]: –––, 1985, “Remarks on some approaches to the concept of logical consequence,” *Synthese*, 62: 153–171.

[^prawitz-2005]: –––, 2005, “Logical Consequence from a Constructivist Point of View,” in S. Shapiro (ed.), *The Oxford Handbook of the Philosophy of Mathematics and Logic*, Oxford: Oxford University Press, pp. 671–695.

[^prawitz-2012]: –––, 2012, “The Epistemic Significance of Valid Inference,” *Synthese*, 187: 887–898.

[^priest-1999]: Priest, Graham, 1999, “Validity,” *European Review of Philosophy*, 4: 183–205 (Special Issue: *The Nature of Logic*, Achillé C. Varzi (ed.), Stanford: CSLI Publications.

[^prior-1960]: Prior, Arthur N., 1960, “The Runabout Inference-Ticket,” *Analysis*, 21 (2): 38–39.

[^putnam-1971]: Putnam, Hilary, 1971, *Philosophy of Logic*, New York: Harper & Row.

[^quine-1986]: Quine, W.V.O., 1986 (2nd Ed.), *Philosophy of Logic*, Cambridge, MA: Harvard University Press.

[^raatikainen-2008]: Raatikainen, Panu, 2008, “On Rules of Inference and the Meanings of Logical Constants,” *Analysis*, 68 (300): 282–287.

[^ray-1996]: Ray, Greg, 1996, “Logical Consequence: A Defense of Tarski,” *The Journal of Philosophical Logic*, 25 (6): 617–677.

[^read-1994]: Read, Stephen, 1994, “Formal and Material Consequence,” *The Journal of Philosophical Logic*, 23 (3): 247–265.

[^restall-2005]: Restall, Greg, 2005, “Multiple Conclusions,” in P. Hájek, L. Valdés-Villanueva, and D. Westerståhl (eds.), *Logic, Methodology and Philosophy of Science: Proceedings of the Twelfth International Congress*, London: KCL Publications, pp. 189–205. [[Preprint available online in PDF](http://consequently.org/papers/multipleconclusions.pdf)].

[^ripley-2013]: Ripley, David, 2013, “Paradoxes and failures of cut,” *Australasian Journal of Philosophy*, 91(1): 139–164. doi: 10.1080/00048402.2011.630010.

[^sagi-2014a]: Sagi, Gil, 2014a, “Formality in Logic: From Logical Terms to Semantic Constraints,” *Logique et Analyse*, 57 (227): 259–276.

[^sagi-2014b]: –––, 2014b, “Models and Logical Consequence,” *Journal of Philosophical Logic*, 43 (5): 943–964.

[^shapiro-1987]: Shapiro, Stewart, 1987, “Principles of Reflection and Second Order Logic,” *Journal of Philosophical Logic* 16 (3): 309–333.

[^shapiro-1998]: –––, 1998, “Logical Consequence: Models and Modality,” in M. Schirn (ed.), *The Philosophy of Mathematics Today*, Oxford: Oxford University Press, pp. 131–156.

[^shapiro-2005]: –––, 2005, “Logical Consequence, Proof Theory, and Model Theory,” in S. Shapiro (ed.), *The Oxford Handbook of the Philosophy of Mathematics and Logic*, Oxford: Oxford University Press, pp. 651–670.

[^shapiro-2014]: –––, 2014, *Varieties of Logic*, Oxford: Oxford University Press.

[^sher-1991]: Sher, Gila, 1991, *The Bounds of Logic*, Cambridge, MA: MIT Press.

[^sher-1996]: –––, 1996, “Did Tarski Commit Tarski’s Fallacy?,” *Journal of Symbolic Logic*, 61 (2): 653–686.

[^sher-2022]: Sher, Gila, 2022, *Logical Consequence*, Cambridge: Cambridge University Press.

[^schroeder-heister-1991]: Schroeder-Heister, Peter, 1991, “Uniform Proof-Theoretic Semantics for Logical Constants (Abstract),” *Journal of Symbolic Logic*, 56: 1142.

[^tarski-1986]: Tarski, Alfred, 1986, “What are Logical Notions,” *History and Philosophy of Logic*, 7: 143–154.

[^tennant-1994]: Tennant, Neil, 1994, “The Transmission of Truth and the Transitivity of Deduction,” in *What is a Logical System?* (Studies in Logic and Computation: Volume 4), D.M. Gabbay (ed.), Oxford: Clarendon Press, pp. 161–177.

[^wansing-2000]: Wansing, Heinrich, 2000, “The Idea of a Proof-Theoretic Semantics and the Meaning of the Logical Operations,” *Studia Logica*, 64 (1): 3–20.

[^westerståhl-2012]: Westerståhl, Dag, 2012, “From constants to consequence, and back,” *Synthese*, 187 (3): 957–971.

[^woods-2012]: Woods, Jack, 2012, “Failures of Categoricity and Compositionality for Intuitionistic Disjunction,” *Thought: A Journal of Philosophy*, 1 (4): 281–291.

[^zinke-2018]: Zinke, Alexandra, 2018, *The Metaphysics of Logical Consequence* (Studies in Theoretical Philosophy: Volume 6), Frankfurt am Main: Vittorio Klostermann.
