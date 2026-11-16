# Deductivism in the Philosophy of Mathematics
**First published Fri Aug 25, 2023**

*Paseau, Alexander, Pregel, Fabian*

Deductivism says that a mathematical sentence $s$ should be understood as expressing the claim that $s$ deductively follows from appropriate axioms. For instance, deductivists might construe “$2 + 2 = 4$” as “the sentence ‘$2 + 2 = 4$’ deductively follows from the axioms of arithmetic”. Deductivism promises a number of benefits. It captures the fairly common idea that mathematics is about “what can be deduced from the axioms”; it avoids an ontology of abstract mathematical objects; and it maintains that our access to mathematical truths requires nothing beyond our ability to make logical deductions. Sections 1 and 2 define and motivate deductivism in more detail. Section 3 covers four authors (Russell, Hilbert, Pasch, Curry) who have endorsed deductivism at some point. Section 4 aims to clarify what semantic claim deductivists make. Sections 5–9 review objections to deductivism and possible replies.

## 1. Introduction

Deductivism is a philosophy of mathematics that was popular in the late nineteenth and early twentieth century. It understands a mathematical sentence $s$ as expressing the claim that $s$ deductively follows from appropriate axioms. For instance, deductivists might construe “$2 + 2 = 4$” as

> the sentence “$2 + 2 = 4$” deductively follows from the axioms of arithmetic,

or “2 is prime” as

> the sentence “2 is prime” deductively follows from the axioms of arithmetic,

or, for a non-arithmetical example, “every group $G$ has exactly one identity element” as

> the sentence “every group $G$ has exactly one identity element” deductively follows from the axioms of group theory.

Deductivists thus reject the surface syntax of mathematics. They do not take “2 is prime” to attribute a property (primeness) to an entity (the number 2); for them, it states that the sentence “2 is prime” follows from some axioms.

This entry will assess deductivism’s strengths and weaknesses, discuss its turn-of-the-twentieth-century heyday, and compare it to contemporary versions of structuralism.

## 2. Motivation

Deductivism is interesting and important for a host of reasons. The first is that it gives proof, indisputably of paramount importance in mathematics, pride of place. Mathematicians take a result to be established only if it has been proved. It is natural to explore what happens if we take this one step further and take mathematical truth to be, not just *established*, but *constituted*, by the existence of a (possibly not yet known) proof.

Second, many mathematicians profess to believe in deductivism or something like it (Maddy 2022: 9)[^maddy-2022]. Ask mathematicians what their subject is about and at least some will reply that it is about “what can be deduced from the axioms”. Naturally, a slogan like this is not a worked-out philosophy, and is more often encountered in conversation than in print. Still, if the slogan and the sentiment behind it point to any specific philosophy, surely it is to deductivism. Moreover, most parts of mathematics are explicitly understood as exploring consequences of stipulated axioms,[^note-1] which deductivism spells out in its own way and generalises to all mathematics. Not only that, but as §3 will briefly document, many influential philosophers of mathematics from the late nineteenth to the early twentieth century were, or could be interpreted as, deductivists.

Third, and this might go some way towards explaining the second point, deductivism is seen as philosophically “clean” (Rheinwald 1984: 49)[^rheinwald-1984] or a way to “avoid philosophical quicksand” (Maddy 2022: 9)[^maddy-2022]. On the epistemological side, the deductivist’s main task is to account for the epistemology of deductive logic—there is no further specific problem of mathematical epistemology. On the metaphysical side, the deductivist construal appears not to presuppose any abstract mathematical objects, often seen as problematic. A further point in deductivism’s favour is that it respects the presumed objectivity of mathematics, because what follows from the axioms is an objective matter, independent of us. Moreover, deductivism seems to offer a promising account of applications: whenever you find a physical system that satisfies the axioms of a particular branch of mathematics, the branch’s theorems must apply to the system. (We shall return to these alleged attractions below.)

The fourth and final reason is that deductivism and structuralism are related. Indeed, deductivism is seen by some (e.g., Bostock 2009: 183)[^bostock-2009] as a syntactic version of eliminative structuralism. And structuralism, in its various guises, and its various problems notwithstanding, is one of the most attractive metaphysics of mathematics on the market today.[^note-2]

Deductivism and eliminative structuralism share some general features. Roughly speaking, both understand a mathematical claim $p$ as “the axioms imply that $p$” (where “the axioms” may be understood as those of the germane branch of mathematics or otherwise—for different versions of deductivism, see §4). Deductivism understands the relevant implication deductively, eliminative structuralism semantically. For deductivists, the relevant notion of implication or consequence is the syntactic one which in logic is denoted by “$\vdash$”; to say that $\Gamma \vdash \delta$ is to say that the sentence *δ* is derivable from *Γ* in some specified deductive system. For eliminative structuralists, the relevant notion of implication or consequence is instead the semantic one which in logic is denoted by “$\vDash$”. Eliminative structuralists, for example, construe “$2 + 2 = 4$” as a claim about what holds in any structure in which the axioms of arithmetic are satisfied.[^note-3]

When we dig down into the details, however, some clear differences emerge. Deductivists take mathematical claims to be about sentences, whereas eliminative structuralists take them to be generalisations over structures. Unlike deductivists, eliminative structuralists therefore owe us an account of the metaphysics of structures. Eliminative structuralists also usually couple their account with the existential assertion that a structure of the right kind exists (or could exist), whereas deductivists often omit the corresponding claim that the axioms are consistent. One well-known version of eliminative structuralism, first articulated by Putnam (1967b)[^putnam-1967b] and developed by Hellman (1989)[^hellman-1989], is modal, whereas deductivism is usually not modal. (Although see §5 for how to spell out deductivism in terms of a primitive modal operator.) Finally, eliminative structuralism is but one of the many forms of structuralism around today. Some, such as Hellman’s version, have much in common with the eliminative variety closest to deductivism; others, such as Shapiro’s ante rem structuralism (Shapiro 1997)[^shapiro-1997], less so.

Still, despite these differences, there are some clear historical and philosophical continuities between the two, so that getting clear about deductivism’s flaws can help us better appreciate the virtues of a broadly structuralist approach. What is certainly true is that prior to Gödel’s 1929 Completeness Theorem for first-order logic (published as a paper the following year), the differences between deductivism and eliminative structuralism were not clearly understood. This point will be illustrated in the historical §3. Also relevant to the story is Gödel’s 1931 First Incompleteness Theorem, which will form the basis of a key objection to deductivism in §9.[^note-4]

A final point of connection is that, when the background logic is axiomatizable, eliminative structuralism and deductivism offer an extensionally equivalent account of mathematical truth.[^note-5] The simple reason is that, for an axiomatizable logic, such as first-order logic, semantic implication is extensionally equivalent to deductive inference. So suppose you are tempted by eliminative structuralism in the philosophy of mathematics and use first-order logic as your default logic.[^note-6] You will then take $p$ to be a mathematical truth exactly when a (first-order) deductivist does. Avoiding a “lapse into a semantic equivalent of deductivism” was precisely one of the reasons Hellman chose a second-order framework for his modal version of eliminative structuralism (Hellman 1989: 18–19)[^hellman-1989]. As explained, however, eliminative structuralism and deductivism are not equivalent in any stronger sense than this extensional one, even when their shared background logic is axiomatisable.

A terminological note: deductivism is sometimes called “if-thenism”. However, “if-thenism” sounds more like the genus whose syntactic and semantic species are deductivism and eliminative structuralism respectively. Rheinwald (1984: 49)[^rheinwald-1984] uses the name “implicationism” for the genus, reserving “syntactic implicationism” for deductivism and “semantic implicationism” for structuralism. This terminology manages to cover both genus and species and also has the great merit of transparency. The present entry sticks to “deductivism” and “structuralism” for the two species, because these names are the more usual ones today (and are shorter).

## 3. Historical Accounts

This section covers four historical accounts of deductivism, advocated by Russell (§3.1), Hilbert (§3.2), Pasch (§3.3), and Curry (§3.4) respectively. The first three are pre-Gödelian; the fourth is a post-Gödelian attempt to defend deductivism.

Attributing deductivism to older authors is harder than it may initially appear, and the existing literature offers no attempts to do so in a comparative way. The difficulty is owed to several conflating factors. The main one is that, before Gödel, there was no clear distinction between semantic and syntactic consequence. And terminological confusion does not help: Curry, for example, refers to his deductivism as “formalism”, a label usually reserved for a different position. This article thus focuses on classifying authors’ substantive claims. A comparison with Brouwer (§3.5), who emphasised proof in mathematics but was no deductivist, will also be relevant.

### 3.1 Russell

Russell’s *The Principles of Mathematics* was published in 1903. The book’s very first sentence contains Russell’s credo about what mathematics is:

> Pure mathematics is the class of all propositions of the form “$p$ implies $q$”, where $p$ and $q$ are propositions containing one or more variables, the same in the two propositions, and neither $p$ nor $q$ contains any constants except logical constants (Russell 1903 [2009: 3])[^russell-1903].

It may seem odd that the propositions $p$ and $q$ are supposed to contain at least one variable. Yet, according to Russell, even “$1+1=2$” contains variables once made fully explicit—namely “If $x$ is one and $y$ is one, and $x$ differs from $y$, then $x$ and $y$ are two” (Russell 1903 [2009: 6])[^russell-1903].

Is Russell’s credo a form of deductivism or structuralism, or some admixture of the two? At the turn of the twentieth century, no one clearly distinguished semantics and syntax, and Russell was no exception. This led Putnam to claim that what Russell really had in mind was, in our terminology, eliminative structuralism. (Putnam christened the structuralism he attributed to Russell “if-thenism”; as explained in §2, this entry avoids the term.) He urged:

> What he meant was not, of course, that all well formed formulas in mathematics have a horseshoe as the main connective! but that mathematicians are in the business of showing that *if* there is any structure which satisfies such-and-such axioms (e.g., the axioms of group theory), *then* that structure satisfies such-and-such further statements (some theorems of group theory or other) (Putnam 1967a [1975: 20])[^putnam-1967a].

However, Putnam’s structuralist interpretation of Russell is controversial, not least because a structuralist reading appears to explicitly contradict the deductivist wording of several passages (Kraal 2014: 1498)[^kraal-2014]. For example, with pure mathematics defined in the above way, Russell went on to assert that

> [b]y the help of ten principles of deduction and ten other premisses of a general logical nature (e.g., “implication is a relation”), all mathematics can be strictly and formally deduced; and all the entities that occur in mathematics can be defined in terms of those that occur in the above twenty premisses (Russell 1903 [2009: 3])[^russell-1903].

The emphasis here is clearly on deduction.

To prove the above deducibility claim is the stated objective of *The Principles of Mathematics* (Russell 1903 [2009: xiii])[^russell-1903]. And like everyone else at the time, Russell tended to assume that logical implication is a deductive relation. Thus, even if it was not his intention to differentiate semantics and syntax sharply, as he historically was not in a position to do, his credo combined with the equation of logical with deductive implication committed him to deductivism. Hence *The Principles*’ key doctrine is more plausibly construed as a version of deductivism than eliminative structuralism.[^note-7]

### 3.2 Hilbert

Other contemporaries of Russell’s also displayed deductivist leanings. Resnik classified Hilbert’s work of around 1900 as a “deductivist period” (1980: 105). However, Hilbert at the time endorsed what can now be separated out as deductivism on the one hand and some form of proto-structuralism on the other. He made no distinction between the two, as we would today, because he assumed complete axiomatisations and proof systems were available.

Consider Hilbert’s 1900 “About the Concept of Number”. In the introduction, Hilbert declares that he intends to apply the axiomatic method, known from geometry, to the concept of number (1900a: 181). He contrasts the axiomatic method with the *ad hoc* approach usually found in the literature of the time. The purpose of his axiomatic approach is to achieve the “final presentation and logical certainty of the content of our understanding” (ibid). He begins by setting out eighteen axioms for the real numbers. To give a flavour, the first axiom is

> From the number $a$ and the number $b$ results through “addition” a specific number $c$, formally: $a + b = c$ or $c = a + b$. (1900a: 18)

Hilbert then asserts that propositions about the real numbers are only valid (*gültig*) if they can be proven from the set of axioms in a finite number of steps (1900a: 184).

The reason for this insistence is explained in his famous lecture to the International Congress of Mathematicians in Paris in the same year (published as “Mathematical Problems”). Here Hilbert expresses the “absolute conviction” that any mathematical problem, no matter how difficult, must be solvable “through a finite number of purely logical steps” (1900b: 261). He maintains that this conviction is shared by all mathematicians and is a major source of motivation; but he also notes that we have no proof that the finite-derivability claim is true (1900b: 262). Despite the absence of such a proof, he takes this conviction to be the natural *modus operandi* of the working mathematician. In “Mathematical Problems”, Hilbert also maintains that, to the extent that new concepts are introduced in mathematics—say, due to their usefulness in scientific explanations—those concepts need to be axiomatized to make them useful for deduction:

> [Their introduction] gives birth to the task for mathematics to research the principles associated with the new concept and then to fix them in a simple and complete axiom system in such a way that the new concepts and their usability *for deduction* is in no way inferior to the old arithmetical concepts. (1900b: 259, our translation and emphasis)

At the same time as emphasising the importance of a deductive framework, Hilbert endorsed proto-structuralist ideas. He mentions “thinking of a system of objects”, saying we “call those objects numbers” and “denote them with *a*, *b*, *c*” (1900a: 181). In his correspondence with Frege one year earlier, for example, Hilbert noted that

> E.g., instead of points, think of a system of love, law, chimney-sweep … which satisfies all axioms; then Pythagoras’ theorem also applies to these things. Any theory can always be applied to infinitely many systems of basic elements. (Letter from 29 Dec 1899, Frege 1976 [1980: 42])[^frege-1976]

Hilbert moved fluidly between both deductivism and proto-structuralism by relying on the completeness assumption. For example, in his letter to Frege dated 29 December 1899, he stated that if the axioms in an axiom system do not contradict one another,

> then they are true, and the things defined by the axioms exist. This for me is the criterion of truth and existence. (Letter from 29 Dec 1899, Frege 1976 [1980: 42])[^frege-1976]

Note that Hilbert does not maintain that the axioms are true if they have a model—consistency and model-existence are equivalent only if the axiom system is complete.

Hilbert at the time, then, was firmly committed to two views. Both understand mathematical claims as true in virtue of implication from axioms. One is that mathematical validity amounts to mathematical provability with a finite number of steps from a finite number of axioms. The second is that mathematics is not about specific objects but that mathematical truth (in a particular domain) is defined by the axioms.

We can also observe differences between Russell’s and Hilbert’s varieties of deductivism. By asserting that

> all the entities that occur in mathematics can be defined in terms of those that occur in the above twenty premisses,

Russell closely links deductivism to the claim that any non-logical vocabulary in axioms and theorems is ultimately eliminable (1903 [2009: xliii]). Thus Russell combines deductivism with a core tenet of logicism, namely that non-logical terms be definable by logical ones.

For the turn-of-the-century Hilbert by contrast, numerals and other non-logical terms (as we could call them) in our deductions remain primitive. But although not eliminable, they are generic. Hilbert asks us to imagine “a system of things, which we will call numbers” (Hilbert 1900a: 181)[^hilbert-1900a]. The axioms then provide a “precise and complete description of numbers” “mutual relations” (Hilbert 1900a: 181)[^hilbert-1900a]. For as he memorably put it, “one must be able to say at all times—instead of points, straight lines, and planes—tables, chairs and beer mugs” (Kennedy 1972: 133)[^kennedy-1972]. Here Hilbert’s stance effectively derives from Pasch. Pasch had called his method “a formalism” and maintained that mathematical proofs must remain valid if the basic concepts are replaced throughout “by any concepts or by meaningless signs” (Schlimm 2010: 103)[^schlimm-2010].

### 3.3 Pasch

This brings us to Moritz Pasch himself, another contemporary of Russell and Hilbert’s who defended a flavour of deductivism. Pasch is best known for his axiomatisation of geometry in his 1882 *Vorlesungen über neuere Geometrie*. A key passage found in the 1882 first edition and, with minimal changes, also in the 1926 second edition, reads as follows:

> Indeed, if geometry is to be truly deductive [*deduktiv*], deduction [*Deduktion*] must be independent everywhere from the meaning of the geometric terms, just as it must be independent of diagrams; only the relations between the geometric terms specified in the utilised theorems and definitions may be considered. During the deduction [*Deduktion*] it is permitted and useful, but in no way necessary, to think of the meanings of the geometric terms; in fact, if it is necessary to do so, this makes plain the gaps in the *deduction*, and under certain circumstances even the inadequacy of the theorems invoked in the proof (1882/1926, our translation and emphasis).[^note-8]

This passage does two things: it maintains that the meaning of geometrical terms has no role to play in geometry at its most rigorous; and it emphasises proof. So it can be seen as advocating deductivism or, possibly, formalism. “Formalism” here means what is sometimes called “game formalism”, i.e., the thesis that mathematics is a mere play with symbols according to defined rules. However, other passages in Pasch’s corpus favour a deductivist interpretation:

> *Mathematics* is a system with two parts that must be clearly distinguished. The first, the properly mathematical part, *is devoted entirely to deduction*. The second makes deduction possible by introducing and elucidating a *series of insights* that are to serve as material for deduction, preparing new material whenever the deductive part requires it. This second part, dwarfed by the properly mathematical one, can be called the pre-mathematical part, while I might refer to the other as the *rigid part*, since it forms a structure *characterized by the absolute rigor of its inference rules*. Though it is tempting to ignore how rigorous these rules are, that does not make them any less rigorous. *The rigid part is, as I said, mathematics proper. It proceeds by mathematical proof and mathematical definition.* (Pasch 1918 [2010: 51], our emphasis)[^pasch-1918]

Pasch thus distinguished between mathematics and what we may call “pre-mathematics”. Mathematics is entirely deductive, whereas pre-mathematics serves to motivate the “material for deduction”. Mathematics “dwarfs” pre-mathematics and is characterised by “absolute rigor of its inference rules”, which is why Pasch calls it “rigid” (*starr*). In light of the above passages, and others, Pasch may reasonably be classified as a deductivist.

Pasch takes a notably different view from Hilbert as to what, among all the possible sets of axioms a deductivist could adopt, characterises a “good” set of axioms. Hilbert’s response to this question foreshadows his future formalism. In “About the Concept of Number”, he maintains that, once the set of axioms has been proven to be consistent, any further doubt about the existence of the concept number “loses all justification” (Hilbert 1900a: 184)[^hilbert-1900a]. Classically, consistency is a necessary condition for a good axiom set, so all forms of classical-logic-based deductivism will adopt it. But whether or not consistency is also *sufficient* is a matter over which various deductivisms may differ. From a modern perspective, we can think about the sufficiency claim as follows: absent a completeness proof, the consistency of a set of axioms does not in general entail that they have a model. To spell out the familiar argument, let PA2 be the set of second-order Peano Axioms, and Con(PA2) a consistency statement for PA2. Then $\textrm{PA2} \cup \{\neg \textrm{Con}(\textrm{PA2})\}$ is consistent provided PA2 is, since $\textrm{PA2} \not\vdash \textrm{Con}(\textrm{PA2})$ by Gödel’s second incompleteness theorem. However, $\textrm{PA2} \cup \{\neg\textrm{Con}(\textrm{PA}2)\}$ lacks a model, and so, under a traditional language-world picture, the language of the axiom system does not pick out anything in the world. But for a deductivist who asserts that only consistency matters, the alleged absence of successful reference is of no significance.

What distinguishes Pasch’s deductivism from Hilbert’s is that Pasch simultaneously maintained an empiricism about the axioms (Schlimm 2010: 95–96)[^schlimm-2010]. He held that the axioms are to have independent empirical grounding (“the pre-mathematical part” above). For example, Pasch grants the possibility of other consistent axiom sets for geometry, but maintains that without empirical grounding such a system constitutes merely “hypothetical geometry” (1917 [2010: 46]). In particular, Pasch maintains, the hypothetical sentences derived in such a geometry may lack applicability (1917 [2010: 46]; Schlimm 2010: 101)[^schlimm-2010].

### 3.4 Curry

A more recent version of deductivism was defended by Haskell Curry in his 1951 *Outlines of a Formalist Philosophy of Mathematics*. As he sees it, “mathematics is the science of formal systems” (1951: 56). For Curry, formal systems are to be understood deductively—they are comprised of a formal language, axioms and inference rules called “rules of procedure” (1951: 11–13). Writing after the discovery of incompleteness, Curry has this to say about its implications:

> The incompleteness theorems […] show that it is hopeless to find a single formal system which will include all of mathematics as ordinarily understood. Moreover the arbitrary nature of the definitions which can constitute the primitive frame of a formal system shows that, in principle at least, all formal systems stand on a par. The essence of mathematics lies, therefore, not in any particular kind of formal system, but in formal structure as such. (Curry 1951: 56)[^curry-1951]

Curry calls his conception *formalist.* But by formalism, Curry just means the science of what can be deduced in formal systems. Formalism and deductivism (as understood in this entry) are similar in their focus on syntax over semantics. However, deductivism holds that mathematical claims have truth-conditions, unlike games; and it regards only logical inferences as permissible, whereas a formalist can in principle condone any symbol-derivation practice. In line with the deductivist rather than the formalist interpretation, Curry uses the notion of truth extensively in his writings and rejects the view that formal systems are to be conceived of as a game:

> There must be an *objective criterion of truth*, and the first task of the mathematical logician is to find it. The first thesis of this book is that such a definition can be found. (1951: 3)
>
> Before we proceed to the discussion of the formalist definition of mathematics, it will be necessary to consider the definition of its fundamental notion, that of a formal system. […] The conception here expounded differs superficially from the usual one in that *such a system is conceived not as a game but as a body of propositions.* […] The first point is that the words “proposition”, “true”, “predicate”, etc., used in the following, are intended in the sense of ordinary discourse. […] [A proposition] indicates certain conditions for verification; when the proposition is asserted—taken as true —, that means that these conditions are fulfilled, so that processes of verification are what determine, essentially, the meaning of the proposition. (1951: 8)
>
> For the purposes of mathematics it is sufficient to have criteria for recognising a formal system as such, and for *deciding which propositions are true*. (1951: 31)

One of the main advantages of this perspective, according to Curry, is the absence of metaphysical speculation—a key motivation for deductivism (see §2):

> The formalist conception of mathematics is thus *free from metaphysical bias*, and is therefore compatible with practically any sort of philosophy. It is the only conception so far proposed which has that character. (1951: 58; our emphasis)

### 3.5 Intuitionism and Brouwer

Intuitionism is sometimes spoken of in the same breath as deductivism. Curry, for example, maintains that

> Indeed, if we subtract from intuitionism its metaphysics, the differences between it and formalism as to the definition of mathematical truth are superficial. The emphasis on constructive methods—Hilbert’s “finite Einstellung”—on recursive definitions and mathematical induction, are made by formalist and intuitionist alike. (1951: 58)

Brouwer’s intuitionism is related to deductivism but differs from it in an interesting way. What, briefly, are the similarities and differences?

In his Cambridge lectures, Brouwer rejects “mathematical creation by means of logical axioms” (1981: 7). Indeed, for him, “all axioms became illusory” (1981: 92). Brouwer’s target here is what he calls the “Old Formalist School”, which for him includes Dedekind, Peano, Russell and Hilbert, and from which he goes to lengths to distance himself. For Brouwer, “the criterion of truth or falsehood of a mathematical assertion” is not a deduction but “mathematical activity itself” (Brouwer 1981: 92)[^brouwer-1981]. The relevant activity is the process of providing a construction. Thus, for the intuitionist, truth and falsehood are replaced with, or cashed out as, the existence or absence of an intuitionistically acceptable construction (Brouwer 1981: 92)[^brouwer-1981].

Constructions are a series of mental acts; they are thus distinct from proofs which are sequences of appropriately linked sentences. For Brouwer, the *first act of intuitionism* is to completely separate “mathematics from mathematical language and hence from the phenomena of language described by theoretical logic” (1981: 4). For Brouwer, no linguistic inscription or utterance can convey the true nature of a construction in intuition. The severance of mathematics from language and logic, a cornerstone of Brouwer’s intuitionism, sharply distinguishes it from deductivism.

That said, intuitionism does have some parallels with deductivism. A notable one is the replacement of the usual referential account of truth in mathematics with a verification-based approach: deductivism does this in terms of proofs, intuitionism in terms of constructions. The development of intuitionistic logic brings out an important fact about deductivism: deductivism is not tied to any particular formal system. It could be based on classical logic, or Heyting’s intuitionist formal system, or some third alternative.[^note-9]

## 4. Meaning Matters

We outlined some of the historical support for deductivism in §3. In §§5–9, we consider some of the challenges it faces. In the present section, we aim to achieve greater clarity on what semantic claim the deductivist makes.

The first point is that we have characterised deductivism as “understanding” or “construing” or “rendering” a mathematical sentence $p$ as “$Ax \vdash p$” This characterisation is deliberately neutral between two more precise readings. One is that deductivists take their construal to capture the meanings of mathematical statements as ordinarily spoken.[^note-10] The other is that they aim to do no such thing but wish instead to provide a reconstruction of mathematics answering to philosophical criteria. One such criterion *might* be proximity to mathematical discourse as ordinarily understood—but typically this will not be an overriding factor. Other criteria will include giving an attractive metaphysics, epistemology and account of the applications of mathematics. This entry will stay neutral on this point, though it should be noted that the first approach faces a considerable burden of proof: there are no obvious grounds to think that we *actually* speak in deductivist fashion.

The second point is that the deductivist has to offer more than the simple claim that a mathematical sentence $p$ should be construed as “$Ax \vdash p$”. For one thing, her (meaning-capturing or reconstructive) semantics for mathematics cannot be confined to the sentence level but must also apply to words. The deductivist must, for instance, give a semantic account of the numeral “2” and the predicate “is prime” compatible with her construal of “2 is prime” as “$Ax \vdash 2$ is prime”.

For another, she must give an account of speech acts involving mathematical statements. It is natural to suppose that she construes an assertion of “569 is prime”, say, as an assertion of “$Ax \vdash 569$ is prime”. Likewise, presumably, for many propositional attitudes: for the deductivist, what we might ordinarily describe as wondering whether 569 is prime should be understood as wondering whether the axioms deductively imply that 569 is prime; what we might ordinarily describe as doubting that 569 is prime should be understood as doubting that the axioms deductively imply that 569 is prime; and so on. A tentative suggestion might then be that the deductivist should take “$Ax \vdash$” to have narrow scope over force operators (asserting, wondering, doubting, etc.).

Neither of these tasks—providing a word-level semantics for mathematical language and an account of speech acts involving mathematical sentences—seems entirely straightforward. As for the first, deductivists’ account of mathematical language must allow for its use in empirical contexts to make straightforwardly literal claims. For example, “there were 569 people in the audience” should presumably not be understood as a covert implication from axioms but rather as a literal claim about a physical situation. For the deductivist, then, this is quite a different use of “569” from a purely mathematical one. §8 discusses the problem of applications for the deductivist (though at the sentence- rather than word-level).

As for the second, it’s not clear that the deductivist will always wish to apply the “$Ax \vdash$ ”-takes-narrow-scope strategy in the same mechanical way. Take for example proof by assumption, in which we first assume $p_1$ and deduce $p_n$ via $p_2 , \ldots , p_{n-1}$. Our initial supposition $p_1$ might be that $m$ is an odd perfect number and the final line $p_n$ might be some interesting fact about any such $m$. It’s not at all obvious that “assume” here takes wide scope and “$Ax \vdash$ ” takes narrow scope. For if it did, “Assume $p_1$” would be construed as “Assume $Ax \vdash p_1$”, which intuitively is a different claim. A more technical way of seeing this is that because $m$ does not occur free in $Ax$, it seems that we can generalise to obtain “$Ax \vdash \forall m p_1$”. If so, “Assume that $Ax$ proves that $m$ is an odd perfect number” implies “Assume that $Ax$ proves that for every $m, m$ is an odd perfect number”. But that latter assumption is an outright false claim. A more promising approach is to take the first step in a supposition as allowing us to add $p_1$ to the axiom set, and to then construe the second line as “$Ax + p_1 \vdash p_2$” (or its equivalent via the Deduction Theorem “$Ax \vdash p_1 \rightarrow p_2$”), the third line as “$Ax + p_1 \vdash p_3$” (or “$Ax \vdash p_1 \rightarrow p_3$”), and so on. All in all, there is work for the deductivist to do on this front to spell out these ideas into a coherent theory.

A third point is based on Parsons’s (2008: 55 n. 35) distinction between what might be called *reflexive* and *unreflexive* deductivism. Deductivism as this entry defined it is reflexive, because it interprets $p$ as “$Ax \vdash p$”. Unreflexive deductivism, by contrast, interprets $p$ as “if $\wedge Ax$ then $p$” ($\wedge$ is an operator that conjoins all the elements of the axiom set) and asserts that this conditional is a deductive logical truth. Rheinwald (1984: 50)[^rheinwald-1984] opts for the former, reflexive form, as we have. Commenting on Rheinwald, Parsons advocates adopting the latter, unreflexive, form instead. For, as he sees it, the reflexive form introduces an inessential element of reflection—explicit mention of the axioms—into the content of mathematical statements, which he thinks they lack. Parsons has a point, especially if deductivism is intended as meaning-capturing. Even so, this entry takes deductivism to be reflexive to avoid the problem faced by unreflexive deductivism when the set of axioms is infinite, as it is for example in the case of the first-order Peano Axioms. For in that case, the sentence “if $\wedge Ax$ then $p$” is infinitely long, so not an ordinary-language one. In contrast, “$Ax \vdash p$” is an ordinary sentence of (mathematical) English, where “$Ax$” is a name denoting the relevant axiom set. That said, it may be that unreflexive deductivism is better equipped to handle some of the problems deductivism faces.

A fourth and final point. So far, this entry remained neutral on what the axioms “$Ax$” in the statement of deductivism are. A “local” deductivist, as illustrated in §1, deductively conditionalises the theorems of a branch of mathematics on the branch’s axioms, e.g., theorems of arithmetic on the axioms of Peano Arithmetic. Another sort of deductivism might conditionalise on the axioms of a particular alleged foundation for mathematics, say ZFC set theory. Thus a ZFC-deductivist understands a mathematical claim $p$ as “$p$ follows deductively from the ZFC axioms”. The choice of ZFC is not essential: if the deductivist’s preferred foundation is not ZFC, but some other set theory, or a topos theory, or something else altogether, they could base their deductivism on that instead. A third, similar but looser form of deductivism than this might be called “whatever-it-takes deductivism”. On this view, the axioms provability from which constitutes mathematical truth are not a specific collection, such as the ZFC axioms, but are more vaguely described: they are whatever axioms it takes to prove the theorems of mathematics. This last version has the advantage over the second of not tying provability, perhaps artificially, to a single foundational system. However, it achieves this at the cost of considerable imprecision.[^note-11] In short, different forms of deductivism result from different understandings of “$Ax$” in deductivism’s canonical statement.

## 5. Provability: to reify or not to reify?

The rest of this entry examines five challenges to deductivism, one per section in §§5–9. The first turns on the notion of provability. Since deductivism claims that mathematics is about what is provable in certain axiom systems, providing an account of provability is central to it. The issue is whether to cash out provability in terms of the existence of proofs or not. In short, to reify or not to reify?

Take the reifying approach first. It reads “$p$ is provable from $Ax$” as “there is a proof of $p$ from axioms $Ax$” (in a particular deductive system understood). This is the most natural and most standard understanding of provability. On this approach, to say that a system $T$ is consistent is just to say that there is no formula *φ* in the language of $T$ such that there is a proof of *φ* from $T$ and a proof of $\neg \phi$ from $T$. However, some formulas and proofs are far too long to have concrete physical instantiations; a simple example would be the proof of a numerical equation involving extremely large numbers. Even a formula with concrete instantiations should not be identified with a particular one of these, or with the class of its instantiations. In other words, proofs as understood here are types rather than tokens: abstract strings conforming to the rules set by a deductive system, which exist irrespectively of any physical instantiations in speech, or on whiteboards, paper or screens. Indeed, if the deductivist wishes to retain the ability to refer to theories, as she will surely want to, she will have to accept linguistic types anyway. (Compare Field-like nominalists, who must also refer to scientific and mathematical theories, even as they try to avoid reference to mathematical objects.)

The moral is that the deductivist will have to admit linguistic types. Her motivation for being a deductivist therefore cannot be to avoid *all* abstract objects (i.e., nominalism), since linguistic types are abstract. She must consequently motivate why admitting some abstract objects such as types is acceptable, whereas admitting mathematical objects is not. She might point to considerations of economy: linguistic types are but a small part of the abstract realm. Or she might argue on the epistemological front that linguistic types are more easily knowable, since they have concrete instances, unlike mathematical objects, which do not. However, the literature is not short of arguments that those who reject abstract mathematical objects should also reject abstract linguistic types; see for example Wetzel’s 2009 book *Types and Tokens*.

Of course, one could be a deductivist for other reasons than an aversion to abstract objects. As we saw in §4, one sort of deductivist might hold that a semantic analysis reveals the *meaning* of mathematical statements to be of the form “$p$ deductively follows from the axioms”. It is perfectly consistent to combine this view with an acceptance of abstract objects and the standard account of deductive consequence in terms of the existence of proofs. Yet, although perfectly coherent, the view appears to lack independent motivation.

The alternative to reifying, evidently, is not to reify, and the most obvious way of doing so is to go down a modal route. Instead of cashing out provability by means of proof-existence, deductivists could take provability to be a modal primitive. Logical possibility and necessity are these days typically understood model-theoretically: a statement is logically possible or consistent just when it is true in some model; and necessary just when it is true in all models. The deductivist must abjure this account of consistency (which she equates with logical possibility), on pain of re-introducing mathematics in the metatheory. Against the prevailing model-theoretic account, she must take “it is logically possible that” as a primitive notion, and forgo its analysis in terms of models (Putnam 1967b)[^putnam-1967b]. In so doing, she is in the same boat as all anti-platonists who cannot help themselves to model theory or set theory in the metatheory. This particular boat is a crowded one: it holds not just eliminative structuralists, but also formalists of various stripes and nominalists as well. Nominalists, for example, do not believe in abstract objects. Hence they face the same predicament—they cannot appeal to the existence of models in the metatheory. Hartry Field (1991)[^field-1991] develops a nominalist logic that takes the notion of logical consistency as primitive, which we may symbolise as $\diamond$, with the associated notion of logical necessity being $\square$. In particular, $\diamond T$ is the claim that the theory $T$ is logically consistent, and claims of logical implication are conditionals prefaced by $\square$.[^note-12] The non-reifying deductivist can avail themself of these resources and thereby construe $G \vdash p$ as $\square(\wedge G \rightarrow p)$.

Such “modalist” accounts of logical consequence à la Field have had a fairly low take-up among logicians. Many see little reason to prefer them to the model-theoretic account of consequence. Modalist accounts suffer from problems of expressive adequacy, because they cannot quantify over possibilities; and they are theoretically less virtuous than the usual model-theoretic one, positing as they do primitive links between the existence of set models and primitive consistency facts. Chapter 4 of Melia (2003)[^melia-2003] is a lucid overview of the problems faced by modalism about *metaphysical* modality, which have counterparts in the logical case. If the deductivist takes the non-reifying route, they will have to come up with a satisfactory response to these sorts of challenges.

## 6. Unaxiomatic Mathematics

A second objection to deductivism is that deductivism cannot account for unaxiomatic mathematics.[^note-13] This includes pre-axiomatic mathematics such as, say, “Old Babylonian” mathematics of the early second millennium BC, in which first principles are never stated explicitly (Robson 2008: 90)[^robson-2008].[^note-14] But it also includes non-deductive mathematics; for example, we might wish to credit the eighteenth-century Swiss mathematician Euler with knowledge of results obtained through analogical reasoning, extensive verification of cases, and the like.

It seems right to attribute mathematical knowledge to Babylonian mathematicians who, among other things, were able to solve specific quadratic equations. Still, the challenge may not be that worrying. That first principles were not explicit does not mean that they were not implicit. Presumably, any mathematical principle that Babylonian mathematicians were willing to accept without argument should count as a first principle or axiom. Independently of this point, deductivists should also point out that unaxiomatic methods can yield knowledge if they track what a proof would yield. Babylonian mathematicians used methods that reliably produced solutions to specific quadratic equations, even if they could not formulate, still less solve, the general quadratic equation. Euler’s methods reliably tracked the existence of proofs for his results; if they had not, he would not have been right as often as he was. This deals with the vast majority of such cases. Moreover—thinking about the residual cases—there is some reason to think that non-deductive reasoning can yield knowledge of mathematical truth even in the absence of proof (Paseau 2015)[^paseau-2015].

## 7. A Regress?

We turn now to the third challenge. To introduce it, consider whether deductivism should apply to a sentence such as

> the sentence “$2 + 2 = 4$” deductively follows from $Ax$

(As usual, we write $Ax$ to preserve neutrality on what the axioms are exactly; see §4 for the options here.) Since proof theory appears to be a branch of mathematics like any other, you might suppose that a consistent deductivist should construe this sentence like any other mathematical one. In which case, the sentence “$2 + 2 = 4$” should be construed not as

> the sentence “$2 + 2 = 4$” deductively follows from $Ax$,

but instead as

> the sentence “the sentence ‘$2 + 2 = 4$’ deductively follows from $Ax$” deductively follows from $Ax'$.

(Where $Ax'$ may or may not be identical to $Ax$—this will not affect the main point.) Now if a deductivist is to go down to this route, she will also have to construe this last sentence like any other mathematical one. So it should be glossed in the same way. The same applies to the resulting gloss, and so on without end. Clearly, we are off on an infinite regress.

It seems to follow that for the deductivist there is no finite formulation of the sentence “$2 + 2 = 4$”. Any such formulation would have to be infinite, and, if it ends at all, must end in a sentence $s$ that is a “fixed-point” of this iteration. In other words, $s$ must be identical (not just logically equivalent) to “the sentence $s$ deductively follows from $Ax$” (for some $Ax)$ since $s$ is construed by the deductivist as

> the sentence $s$ deductively follows from $Ax$

Whether such a sentence exists is highly dubious. Even if it does, an infinitely long sentence, with infinitely many embeddings, is an absurdly complicated way to interpret “$2+ 2 = 4$”, which after all is one of the simplest sentences of mathematics, indeed of the English language.

The objection just raised is premised on the idea that provability claims are mathematical. To support this premise, the objection’s proponent might point out that results in proof theory are typically infused with mathematics. Our conviction that some statement is provable in a deductive system is not usually a result of having carried out the proof ourselves, starting from the axioms and applying the rules of inference to derive the theorem. Rather, it often follows from more abstract mathematical reasoning.

How should the deductivist reply to this challenge? She can agree that we use mathematics, sometimes even quite sophisticated mathematics, to determine what deductively follows from some axioms. That is an *epistemological* point. But it does not affect her thesis about what mathematics *is*. For the deductivist, the truth of a mathematical claim $p$ consists in its being a theorem of an appropriate deductive system $D$. How we determine what $D$’s theorems are may require mathematics—this is to apply mathematics to proof systems—and perhaps other machinery, but that, to repeat, is an epistemological point. The fact that $p$ is a theorem of $D$ is a fact about a deductive system, namely that there is a sequence of formulas starting from axioms and proceeding by rules of the system concluding in $p$. As the deductivist sees it—as she *has* to see it, to avoid the regress—*this* fact is not mathematical, even if we must use mathematics to determine whether it holds or not. (Compare the claim that a large meteor will land on Earth before 2050: a physical fact, but one we verify or falsify using sophisticated mathematics.)

In short, to avoid the regress, deductivists should not apply their interpretation strategy to claims of deductive consequence. For any sentence $s$ and well-specified deductive system $D$, whether $D$ proves $s$ or not should be taken to be a determinate fact. Such facts are the cornerstone of her philosophy and should not be “deductivised”. Rather than have the deductivist recipe applied to them, they must be taken at face value.[^note-15]

## 8. Applications

The fourth challenge concerns applications. §2 mentioned that deductivism appears to provide a straightforward account of the applicability of mathematics: provided a physical system satisfies the axioms of a particular branch of mathematics, the branch’s theorems must apply to the physical system. But what exactly does it mean for a system to satisfy an axiom? The simplest account of applications is the mapping or isomorphism account. Given a physical set-up $P$, stipulate an isomorphism from $P$ to some mathematical structure $M$, deduce some facts about $M$, and then, applying the isomorphism in the reverse direction, read off the corresponding facts about $P$. Resnik (1980, 125)[^resnik-1980], following Russell and Putnam, worries that this account is knee-deep in mathematics—for what is an isomorphism if not a mathematical object? More generally, a satisfactory account of mathematical applications will have to employ mathematics to explain how mathematics relates to the physical world.[^note-16]

This is a major concern that applies to a host of other philosophies. All anti-platonists must set out how to understand the mathematics itself used to explain the applicability of mathematics. Eliminative structuralists must give an account of the mathematics relating structures to the physical world. Nominalists must likewise explain how scientific theories laden with commitment to abstract objects can correctly depict the physical facts despite there being no abstract objects. Each specific anti-platonism seems to face some version of this general problem. Allowing the use of mathematics in the metatheory enables a philosophy to relate mathematics and the natural world; disallowing it appears to hamstring a philosophy—or so this challenge maintains.

So can the deductivist explain mathematics’ applicability? Perhaps her best hope of doing so is by means of a combined mathematical-scientific “total” theory, which we may call *TT*. *TT* incorporates all the axioms of mathematics, as well as established scientific principles and data. Through its combination of mathematics and science, *TT* is able to posit all sorts of relations between mathematical “structures” and physical situations and thereby explain mathematical applications (at least as well as anyone can). The truth-conditions of physical claims derivable from *TT* should be understood in the usual referential manner, as relating to the physical world; whereas the truth-conditions of mathematical claims should, for the deductivist, be understood as above, namely as claims of the form “$p$ is deducible from *TT*”. Importantly, for the deductivist, “structures” and “isomorphisms” are to be understood deductively within the theory *TT*. Effectively, the deductivist internalises model theory into the deductive framework.

This response looks like it dispatches the challenge from applications. Mathematics and science can be discussed and compared within the single overarching theory, *TT*. However, the response has an Achilles heel: mixed statements. The deductivist construes talk of numbers in deductivist fashion and talk of chairs (say) in straightforwardly literal fashion. So what is she to make of a claim such as “My favourite things are the number 7 and this chair”? The claim cannot be read literally, as it involves reference to a number; nor should it be read in deductivist fashion, since it involves reference to a concrete entity, a particular chair. That a chair is one of my favourite things is a claim with empirical content, to be taken literally. The sentence “my favourite things are the number 7 and this chair” is of course a toy example. The point applies much more widely, since mathematics is seamlessly interwoven with ordinary and (especially) scientific language.

The deductivist therefore owes us a recipe for cleaving the mathematical from the non-mathematical in all mixed statements. This is a problem faced by other anti-platonist approaches, for example by fictionalists about mathematics such as Mary Leng.[^note-17] They take applied mathematics to be an “extended fiction” that combines the (alleged) fiction of mathematics with science, which they construe literally (as it is about the physical world). But which is which, where do we draw the line, and how do we deal with statements mixing fiction and the literal, apparently inextricably? Finding good answers to the corresponding questions is a significant challenge for deductivists just as much as it is for fictionalists.

## 9. Truth-Completeness

We move on to the fifth and final challenge to deductivism. One version of it, owed to Michael Resnik, runs as follows.[^note-18] Consider the deductivist’s set theory $T$ and its Gödel sentence $G_T$. By construction, $G_T$ is not derivable from $T$. So the deductivist cannot explain the truth of $G_T$. Resnik’s response: the deductivist can simply challenge the antideductivist to explain how she “sees” the truth of $G_T$. Whatever mathematical argument the antideductivist offers, the deductivist can simply extract from it an axiom set $T^{+}$ and point out that $G_T$ follows from $T^{+}$. Objection parried.

Gödel’s First Incompleteness Theorem does create a significant problem for deductivism; but it is not the one just formulated and responded to. The above version focuses on how, given a particular theory $(T)$, we are supposed to appreciate the truth of its Gödel sentence $(G_T)$. A stronger form of the objection casts it in more global terms and brackets the issue of the Gödel sentence’s truth. What deductivism appears to get wrong is that it disrespects the entrenched understanding of most parts of mathematics as *truth-complete*: for any precisely formulated sentence $p$ from a truth-complete area of mathematics, exactly one of $p$ and not-*p* is true. Analysis and arithmetic are examples of areas standardly understood to be truth-complete. It is standardly thought, for example, that a statement such as Goldbach’s Conjecture is true or false, even if it turns out to be unprovable from any reasonable axioms, not just present ones.[^note-19] But on the deductivist view, undecidable sentences in any formalisation of arithmetic and analysis are false and their negations are also false, since neither deductively follows from the axioms. That there are undecidable sentences follows from Gödel’s First Incompleteness Theorem together with standard constraints on deductive systems.[^note-20] Hence deductivism misdescribes our understanding of truth-complete branches of mathematics such as arithmetic, analysis and geometry.

This objection seems to affect two of the three variants of deductivism we identified at the end of §4: local deductivism and ZFC-deductivism. A form of deductivism the Gödelian objection does not affect is constructivist deductivism, because constructivists do not assume the law of excluded middle in mathematics, so do not assume truth-completeness. Though, as we glimpsed in the discussion of Brouwer (§3.5), constructivists do not tend to be deductivists.

Sticking to classical-logic-using deductivism, its proponent could respond to the objection by idealising the axiom system or the proof system or both. The first approach is to construe “$2 + 2 = 4$” as:

> the sentence “$2 + 2 = 4$” deductively follows from the *ideal* axioms of arithmetic

The resulting position is essentially whatever-it-takes deductivism, mentioned in §4. It adds a little more detail to the position articulated in §4 in that the ideal axioms of arithmetic by stipulation give rise to a complete system, in order to overcome the present objection. (Of course, an informal version of whatever-it-takes deductivism would evade the objection altogether, because it is not based on a formal system. But critics will retort that it does so only because its account of mathematical truth is inherently vague.) The second sort of approach might, for example, take the proof system to include infinitary rules of reasoning, such as the omega-rule, which, as is well-known, restores completeness if added to first-order Peano Arithmetic.[^note-21]

Idealising deductivism in either of these ways, however, is not to rescue but to abandon it. Any combined axiom-and-proof system that is consistent, deductively complete and strong enough to capture all the truths of mathematics lacks an effective proof procedure, by Gödel’s First Incompleteness Theorem. To see this, consider say the deductive “system” whose “theorems” consist of all the true sentences of arithmetic.[^note-22] Assuming the Church–Turing thesis, this list of “theorems” cannot be generated by any mechanical proof procedure (i.e., algorithm). Idealised deductivism is thus eliminative structuralism in thin disguise, since it advocates taking as the combined axiom-and-proof system whatever it takes to capture the structural content of the axioms, be it by beefing up the axioms or the “proof” system or both. If the idea is that mathematicians take a sentence to be true if and only if it is a logical consequence of the semantic content of structure-characterising axioms, one should come clean and accept deductivism’s semantic counterpart: eliminative structuralism. The clear moral is that what lands deductivism in trouble is its focus on syntax. Instead of taking a syntactic turn as it did in the late nineteenth and early twentieth centuries, the “mathematical statements are conditional on axioms” idea must instead take a semantic form.

Deductivists might try another defence. We quoted Curry in §3.4 as holding that “all formal systems stand on a par”. And this is surely a thought many deductivists will find attractive: in principle, any formal system is acceptable, the differences between one formal system and another being owed to the fact that one of them is better suited to applications, or to the fact that one of the systems happens to be the one $we$ use, and so on. So, for the deductivist, if the axioms of arithmetic $Ax$ we explicitly or implicitly accept are incomplete, then any arithmetical sentence $p$ not decided by them is neither true nor false, precisely because its truth-value is relativised to deducibility from $Ax$. Of course, we can strengthen $Ax$ in one way to derive $p$ and in another way to derive not-$p$, and in those respective strengthenings $p$ will be respectively true and false. This, it appears, is Curry’s suggestion about how deductivists should react to Gödel’s result.

The resulting pluralist position rejects truth-completeness for a principled reason. But it rejects it nonetheless, and that must count as a significant cost. For the truth-completeness of arithmetic is a fundamental commitment of mathematics, and permeates most of our thinking about the natural numbers. (A similar point applies to many other areas.) Some would say that respecting it is a non-negotiable constraint on a philosophy of mathematics. Of course, the truth-completeness objection challenges deductivism only in certain areas of mathematics—specifically those typically held to be truth-complete but for which no deductively complete, consistent axiomatisation exists. A complete theory-axiomatisation may be provided even in first-order logic not just for finite structures but for some infinite ones as well.[^note-23] Thus one could still try to defend a deductivism about all other areas. But there is great value in having a uniform philosophy of mathematics. More importantly, given deductivism’s motivations, as outlined in §2, it is hard to see what the point of this sort of eclectic deductivism might be.

Truth-completeness presents the deductivist with a formidable challenge. To meet it, she cannot privilege any system of arithmetic over any other by maintaining that “PA is consistent” is true in one system and false in another. The post-Gödelian realisation that eliminative structuralism fares better here—because it allows for the possibility of truth-completeness if we move to an incompletable semantic consequence relation—led to structuralism’s gain in popularity at the expense of deductivism in the second half of the twentieth century.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=deductivism-mathematics). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/deductivism-mathematics/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=deductivism-mathematics&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/deductivism-mathematics/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

[Please contact the authors with suggestions.]

## Related Entries

algebra | Gödel, Kurt: incompleteness theorems | logicism and neologicism | mathematics, philosophy of: fictionalism | mathematics, philosophy of: formalism | mathematics, philosophy of: intuitionism | mathematics, philosophy of: nominalism | mathematics, philosophy of: Platonism | mathematics, philosophy of: structuralism To be completed.

### Acknowledgments

For comments on previous drafts and presentations, we are very grateful to Wes Wrigley, two anonymous journal referees, an anonymous SEP referee, and audience members at several venues: University College London, the Munich Center for Mathematical Philosophy, the University of Oxford’s Philosophy of Mathematics Graduate seminar and its Philosophy of Mathematics seminar, the Ghent-Brussels Seminar in Logic, History and Philosophy of Science, and the Express-PhilMath seminar. Particular thanks go to Bill D’Alessandro, Carlo Nicolai, Dan Waxman, Deniz Sarikaya, Francesca Poggiolesi, Giorgio Sbardolini, Hannes Leitgeb, Hans Robin Solberg, Luca Incurvati, Steffen Ducheyne, Volker Halbach and Walter Dean.

## Notes（原文脚注）

[^note-1]: Notably, abstract algebra, which includes group theory, field theory, and so on, but also (to use a less widespread name) abstract analysis, which includes topology, the study of Banach spaces, Hilbert spaces, and so on.

[^note-2]: Hellman and Shapiro (2019) is a survey of contemporary structuralism, building on its authors’ individual versions (Hellman 1989; Shapiro 1997)[^hellman-1989][^shapiro-1997].

[^note-3]: This statement bolts on to eliminative structuralism the usual model-theoretic definition of semantic consequence. There may be some deviations from this scheme in special cases, e.g. in the case of set theory.

[^note-4]: Previous critical studies of deductivism include chapter 3 of Resnik (1980)[^resnik-1980] and chapter II of Rheinwald (1984)[^rheinwald-1984], where the view is called “syntactic implicationism” (*syntaktischer Implikationismus*, 1984: 62); a version of deductivism (called “enhanced if-thenism”) is advocated in Maddy (2022)[^maddy-2022] and criticised in Hellman (2021)[^hellman-2021]; and briefer discussions appear in Parsons (2008: 53–6)[^parsons-2008], Linnebo (2017: 48–55)[^linnebo-2017], Shapiro (2000: 148–157)[^shapiro-2000] and Bostock (2009: 180–183)[^bostock-2009], the last two of which focus on Hilbert’s deductivism.

[^note-5]: A logic is axiomatisable just when it has a sound and complete proof procedure.

[^note-6]: As is well known, logical tradition of the past hundred years gives first-order logic a privileged role; and first-order logic is axiomatisable. Although first-order logic is no longer as dominant as it was in the mid-twentieth century, it remains the default logic, especially for metatheoretical investigations, a point stressed in Williamson (2014)[^williamson-2014]. For some, such as Quine (1970: 91)[^quine-1970], first-order logic’s axiomatisability is one of its chief virtues.

[^note-7]: What flavour of deductivism does Russell have in mind? His use of “formally” in the last quotation gives us a sense. Russell distinguishes formal from material implication (1903 [2009: 14]). *Formal implication* is characterised by the antecedent and the consequent both containing the same variables. For example, to say “$x$ is a man implies $x$ is a mortal, for all values of $x$” is to assert a formal implication (1903 [2009: 11]). *Material implication*, by contrast, holds between propositions without variables (1903 [2009: 14]). For example, to claim that Euclid’s fifth proposition follows from the fourth, neither of which has free variables, is to assert a material implication (1903 [2009: 14]). His claim in the earlier quotation that mathematical statements are of the form “*p* implies *q*”, where “*p* and *q* are propositions containing one or more variables, the same in the two propositions” shows that he takes mathematical statements to be formal implications. At times, Russell adds that the formalisation of a mathematical claim should be prefaced by universal quantifiers, so that all the variables in the conditional become bound (1903 [2009: 6]). This understanding of deductivism seems closest to what we term *unreflexive deductivism* in §4, although to firmly categorise Russell’s view as such may be anachronistic.

[^note-8]: The 1882 edition clarifies that the “certain circumstances” are when “the gap cannot be removed through a change in the deduction” (Pasch 1882: 98)[^pasch-1882].

[^note-9]: Given his aversion to formalisation, it would not be Brouwer who would later formalise intuitionistic mathematics and logic but his student Arend Heyting, with contributions from others.

[^note-10]: In John Burgess’s (1983)[^burgess-1983] terminology, an account that captures the meanings of mathematical statements as ordinarily spoken would be *hermeneutic*.

[^note-11]: Maddy’s (2022)[^maddy-2022] “enhanced deductivism” is arguably a species of this whatever-it-takes form. See Hellman (2021)[^hellman-2021] for critical discussion.

[^note-12]: Field adds that there are independent reasons, also available to platonists, for taking logical consistency as a primitive notion rather than reducing it in the standard way to the model-theoretic notion.

[^note-13]: The objection that deductivism cannot account for unaxiomatic mathematics was raised by Resnik (1980: 131–2)[^resnik-1980]. The example of Euler is his.

[^note-14]: See Robson (2008)[^robson-2008] more generally for the mathematics of ancient Iraq, and chapter 4 in particular for the mathematics of the Old Babylonian period (c. 1850–1600 BC).

[^note-15]: Compare the deductivist’s refusal to “deductivise” derivability facts to a recent conventionalist’s insistence that metasemantics is factual and so should not be “conventionalised” (Warren 2020: 334–8)[^warren-2020].

[^note-16]: Maddy (2022: 267–272)[^maddy-2022] also discusses applications, which constitute her second challenge to deductivism.

[^note-17]: For Leng’s fictionalism, see in particular her 2010 book.

[^note-18]: See Resnik (1980: 124–5)[^resnik-1980], which follows Putnam (1967a [1975: 26]).

[^note-19]: It is difficult to spell out what it would be for a statement to lack a proof in some absolute sense. But here we are merely describing the usual attitude, not trying to explicate it. Goldbach’s Conjecture states that every even number greater than 2 is the sum of two primes.

[^note-20]: We assume that relevant deductive systems are recursively axiomatisable and consistent.

[^note-21]: Benacerraf (1973: 665)[^benacerraf-1973] mentions the omega-rule in this connection. The rule allows us to infer “for all $n$, $\phi(n)$” from the infinitely many premises $\phi(0), \phi(1), \phi(2),\ldots$.

[^note-22]: To be more precise, one might specify that these are all and only the true sentences of first-order Dedekind-Peano Arithmetic; but the point applies to any reasonable system of arithmetic.

[^note-23]: For example, as is well known, the first-order theory of dense linear orders without endpoints is complete.

[^benacerraf-1973]: Benacerraf, Paul, 1973, “Mathematical Truth”, *The Journal of Philosophy*, 70(19): 661–679. doi:10.2307/2025075

[^bostock-2009]: Bostock, David, 2009, *Philosophy of Mathematics: An Introduction*, Chichester, UK/Malden, MA: Wiley-Blackwell.

[^brouwer-1981]: Brouwer, Luitzen Egbertus Jan, 1981, *Brouwer’s Cambridge Lectures on Intuitionism*, Dirk van Dalen (ed.), Cambridge/New York: Cambridge University Press.

[^burgess-1983]: Burgess, John Patton, 1983, “Why I Am Not a Nominalist.”, *Notre Dame Journal of Formal Logic*, 24(1): 93–105. doi:10.1305/ndjfl/1093870223

[^curry-1951]: Curry, Haskell Brooks, 1951, *Outlines of a Formalist Philosophy of Mathematics*, (Studies in Logic and the Foundations of Mathematics), Amsterdam: North-Holland Publishing.

[^field-1991]: Field, Hartry, 1991, “Metalogic and Modality”, *Philosophical Studies: An International Journal for Philosophy in the Analytic Tradition,* 62(1): 1–22.

[^frege-1976]: Frege, Gottlob, 1976 [1980], *Wissenschaftlicher Briefwechsel*, volume 2 of *Nachgelassene Schriften und Wissenschaftlicher Briefwechsel*, Gottfried Gabriel, Hans Hermes, Friedrich Kambartel, Christian Thiel, and Albert Veraart (eds), Hamburg: Meiner. Abridged version translated as *Philosophical and Mathematical Correspondence*, Brian McGuinness (ed.), Hans Kaal (trans.), Chicago: University of Chicago Press and Oxford: Blackwell.

[^gödel-1930]: Gödel, Kurt, 1930, “Die Vollständigkeit der Axiome des logischen Funktionenkalküls”, *Monatshefte für Mathematik und Physik,* 37(1): 349–60. doi:10.1007/BF01696781.

[^gödel-1931]: –––, 1931, “Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I”, *Monatshefte für Mathematik und Physik,* 38(1): 173–98. doi:10.1007/BF01700692.

[^hellman-1989]: Hellman, Geoffrey, 1989, *Mathematics without Numbers: Towards a Modal-Structural Interpretation*, Oxford: Clarendon Press. doi:10.1093/0198240341.001.0001

[^hellman-2021]: –––, 2021, “If ‘If-Then’ Then What?”, in his *Mathematics and Its Logics: Philosophical Essays*, Cambridge: Cambridge University Press, 237–255 (ch. 14).

[^hellman-2019]: Hellman, Geoffrey and Stewart Shapiro, 2019, *Mathematical Structuralism*, Cambridge: Cambridge University Press. doi:10.1017/9781108582933

[^hilbert-1900a]: Hilbert, David, 1900a, “Über den Zahlbegriff.”, *Jahresbericht der Deutschen Mathematiker-Vereinigung*, 8: 180–183.

[^hilbert-1900b]: –––, 1900b, “Mathematische Probleme”. *Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen, Mathematisch-Physikalische Klasse* 1900: 253–297.

[^kennedy-1972]: Kennedy, Hubert C., 1972, “The Origins of Modern Axiomatics: Pasch to Peano”, *The American Mathematical Monthly*, 79(2): 133–136. doi:10.1080/00029890.1972.11993005

[^kraal-2014]: Kraal, Anders, 2014, “The Aim of Russell’s Early Logicism: A Reinterpretation”, *Synthese*, 191(7): 1493–1510. doi:10.1007/s11229-013-0342-9

[^leng-2010]: Leng, Mary, 2010, *Mathematics and Reality*, Oxford/New York: Oxford University Press. doi:10.1093/acprof:oso/9780199280797.001.0001

[^linnebo-2017]: Linnebo, Øystein, 2017, *Philosophy of Mathematics*, (Princeton Foundations of Contemporary Philosophy), Princeton, NJ: Princeton University Press.

[^maddy-2022]: Maddy, Penelope, 2022, *A Plea for Natural Philosophy: And Other Essays*, New York: Oxford University Press.

[^melia-2003]: Melia, Joseph, 2003, *Modality*, (Central Problems of Philosophy), Montreal: McGill-Queen’s University Press.

[^parsons-2008]: Parsons, Charles, 2008, *Mathematical Thought and its Objects*. Cambridge: Cambridge University Press.

[^pasch-1882]: Pasch, Moritz, 1882/1926, *Vorlesungen uber neuere Geometrie*, first edition, Leipzig: B.G.Teubner. Second edition, (Die Grundlehren der mathematischen Wissenschaften in Einzeldarstellungen 23), Berlin: J. Springer.

[^pasch-1917]: –––, 1917 [2010], “Grundfragen der Geometrie.”, *Journal für die reine und angewandte Mathematik*, 147: 184–190. Translated as “Fundamental Questions of Geometry”, in Pasch 2010: 45–50. doi:10.1515/crll.1917.147.184 (de) doi:10.1007/978-90-481-9416-2_2 (en)

[^pasch-1918]: –––, 1918 [2010], “Die Forderung der Entscheidbarkeit”, *Jahresbericht der Deutschen Mathematiker-Vereinigung*, 27: 228–232. Translated as “The Decidability Requirement”, in Pasch 2010: 51–54. doi:10.1007/978-90-481-9416-2_3 (en)

[^pasch-2010]: –––, 2010, *Essays on the Foundations of Mathematics by Moritz Pasch*, Stephen Pollard (ed./tran.), (The Western Ontario Series in Philosophy of Science 83), Dordrecht: Springer Netherlands. doi:10.1007/978-90-481-9416-2

[^paseau-2005]: Paseau, Alexander C., 2005, “Naturalism in Mathematics and the Authority of Philosophy”, *The British Journal for the Philosophy of Science*, 56(2): 377–396. doi:10.1093/bjps/axi123

[^paseau-2015]: –––, 2015, “Knowledge of Mathematics without Proof”, *The British Journal for the Philosophy of Science*, 66(4): 775–799. doi:10.1093/bjps/axu012

[^paseau-nd]: –––, forthcoming a, “Trumping Naturalism Revisited”, in *On the Philosophy of Penelope Maddy: Set-theoretic Foundations and Naturalistic Methodology*, Juliette Cara Kennedy (ed.), Springer.

[^paseau-nd-2]: –––, forthcoming b, *What is Mathematics About?* Oxford: Oxford University Press.

[^putnam-1967a]: Putnam, Hilary, 1967a [1975], “The Thesis That Mathematics Is Logic”, in *Bertrand Russell, Philosopher of the Century*, Ralph Schoenman (ed.), London: Allen and Unwin, ch. 18. Reprinted In his *Mathematics, Matter, and Method*, London/New York: Cambridge University Press, 1975, 12–42 (ch. 2). Page refs are to the reprint.

[^putnam-1967b]: –––, 1967b, “Mathematics without Foundations”, *The Journal of Philosophy*, 64(1): 5–22. doi:10.2307/2024603

[^quine-1970]: Quine, Willard Van Orman, 1970, *Philosophy of Logic*, Englewood Cliffs, NJ: Prentice-Hall. Second edition, Cambridge, MA: Harvard University Press, 1986.

[^resnik-1980]: Resnik, Michael D., 1980, *Frege and the Philosophy of Mathematics*,. Ithaca, NY: Cornell University Press.

[^rheinwald-1984]: Rheinwald, Rosemarie, 1984, *Der Formalismus und seine Grenzen. Untersuchungen zur neueren Philosophie der Mathematik* (Analyse und Grundlegung, 11), Königstein: Hain.

[^robson-2008]: Robson, Eleanor, 2008, *Mathematics in Ancient Iraq: A Social History*, Princeton, NJ: Princeton University Press.

[^russell-1903]: Russell, Bertrand, 1903 [2009], *Principles of Mathematics*, first edition, Cambridge: University Press. Reprinted London: Routledge, 2009.

[^russell-1937]: –––, 1937 [2010], *Principles of Mathematics*, second edition, London: G. Allen & Unwin. Reprinted London: Routledge, 2010.

[^schlimm-2010]: Schlimm, Dirk, 2010, “Pasch’s Philosophy of Mathematics”, *The Review of Symbolic Logic*, 3(1): 93–118. doi:10.1017/S1755020309990311

[^shapiro-1997]: Shapiro, Stewart, 1997, *Philosophy of Mathematics: Structure and Ontology*, New York: Oxford University Press. doi:10.1093/0195139305.001.0001

[^shapiro-2000]: –––, 2000, *Thinking about Mathematics: The Philosophy of Mathematics*, New York: Oxford University Press.

[^sieg-2020]: Sieg, Wilfried, 2020, “The Ways of Hilbert’s Axiomatics: Structural and Formal”, in *The Prehistory of Mathematical Structuralism*, Erich H. Reck and Georg Schiemer (eds.), New York: Oxford University Press, 142–165 (ch. 6). doi:10.1093/oso/9780190641221.003.0006

[^warren-2020]: Warren, Jared, 2020, *Shadows of Syntax: Revitalizing Logical and Mathematical Conventionalism*, New York: Oxford University Press. doi:10.1093/oso/9780190086152.001.0001

[^wetzel-2009]: Wetzel, Linda, 2009, *Types and Tokens: On Abstract Objects*, Cambridge, MA: MIT Press. doi:10.7551/mitpress/9780262013017.001.0001

[^williamson-2014]: Williamson, Timothy, 2014, “Logic, Metalogic and Neutrality”, *Erkenntnis*, 79(S2): 211–231. doi:10.1007/s10670-013-9474-z
