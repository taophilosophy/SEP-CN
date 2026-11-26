# Bolzano’s Logic
**First published Sun Sep 23, 2007; substantive revision Wed Jul 15, 2026**

*Rusnock, Paul, Šebestik, Jan*

One of the great philosophers of the nineteenth century, Bernard Bolzano (1781–1848) made outstanding contributions in a number of fields (for a more comprehensive survey of his thought and biographical details, see the general entry on Bolzano). As a logician, he focussed on foundations, developing a theoretical framework that is still very much worth studying today, so much so that a highly respected contemporary logician could (only half facetiously) write a quite positive review of Bolzano’s *Theory of Science* (1837) as if it had just appeared (van Benthem 2013)[^benthem-2013]. This is not to say that all aspects of Bolzano’s logical work could be mistaken for contemporary productions: if he seems at times to be at home in the twenty-first century, it is equally clear at others that we have to do with a thinker who was born in the eighteenth.

Bolzano’s presentation of logic in the modern sense is embedded in the vast *Theory of Science* (henceforth *TS*; a shorter introduction to Bolzano’s logic may be found in Bolzano 2004a). The best known innovations of this work belong to his variation logic: definitions of universal validity and analyticity, along with the creation of a complete system of extensional relations between propositions, the most important being compatibility, deducibility (consequence), and equivalence. Bolzano discovered the link between deducibility and conditional probability, according to which deducibility and incompatibility appear as two limit cases of conditional probability. He is also recognized for adopting an anti-psychologistic approach to logic, and for his contributions to semantics. Bolzano’s theory of the grounding relation (*Abfolge*) leading to a hierarchical order among the propositions of a deductive science is the first modern study of axiomatic systems. Moreover, the thorough discussions of concepts of logic and many other insights contribute to make the *TS* one of the classical works in logic and epistemology, on a par with those of Aristotle, Leibniz, and Frege. The extensive historical notes contained in it are a unique source for the history of logic. Although written in natural language, Bolzano’s logic represents a decisive breakthrough in the development of modern logic.

## 1. Early work in logic and methodology

In 1810, Bolzano published a booklet entitled *Contributions to a better founded presentation of mathematics* (Bolzano 1810; Bolzano 2004b) in which he developed his views about the unsatisfactory state of the mathematics of his time and the need for its reform. He proposed a new definition of mathematics as “the science which deals with the general laws (forms) to which things must conform in their existence” (Bolzano 1810, I, §8; Bolzano 2004b: 94), a new division of mathematics into universal mathematics (arithmetic, algebra, analysis, and elements of his future theory of collections) and more specialized mathematical disciplines (e.g., the mathematical theory of time, geometry, rational mechanics), and also put forth some considerations on logic. As with Leibniz, logic is again seen as closely connected with mathematics: it is, indeed, the mathematical method (Bolzano 1810, II, §1; Bolzano 2004b: 103).

The logical theory of the *Contributions* is quite primitive, but the work nonetheless contains a number of important insights. Following Aristotle, Bolzano distinguished two sorts of proofs: those that aim merely to convince us *that* something is the case and those which also show *why* it is so. He called the former “certifications” (Bolzano 2004b: 254: “confirmations”) [*Gewissmachungen*], the latter “groundings” [*Begründungen*]. The concept of grounding reflects the “objective connection among truths”, which need not and usually does not coincide with the subjective order of recognition. It would later become the fundamental concept in Bolzano’s treatment of axiomatic theories in the *TS*.

He then extended this distinction to cover other elements of axiomatic theories. Subjectively, definitions are considerations that acquaint us with the meanings of certain words, while objectively, a definition indicates the parts and structure of a complex concept. Subjectively, some words do not require definition, because their meanings are already clearly understood, while objectively, some concepts cannot be defined because they are simple, i.e., have no parts. Similarly, an axiom or principle in the subjective sense is a proposition whose truth is evident to us, while in the objective sense an axiom is simply an indemonstrable truth from which other truths may be deduced.

Considered objectively, a mathematical theory itself becomes a mathematical object. It has an intrinsic structure, in which complex concepts are ultimately composed of simple ones, and propositions are ordered according to their relations of objective dependence, beginning with the axioms. The goal of foundational research, as he then saw things, is to discover and display this objective order (Bolzano 1810, II, § 2).

The *Contributions* also contains valuable epistemological reflections. Since axioms in the objective sense need not be evident to us, Bolzano states, it can and does happen that, at first anyway, we find them less trustworthy than the theorems that are objectively demonstrable from them. We become convinced of their truth not by contemplating them in isolation, but rather by recognizing their role within a deductive system: that is, by seeing that their objective consequences include the theorems we believe to be true but no propositions we take to be false (Bolzano 1810, II, §21, note; Bolzano 2004b: 119). Similarly, even though simple concepts cannot be defined in an objective sense, they may still require definition in the subjective sense, that is, we may need to develop a clear understanding of them. In such cases, our understanding

> … is brought about by mentioning several sentences, in which the concept in question, designated by its own word, appears in various combinations. From the comparison of these sentences, the reader is able to abstract which determinate concept the word designates. […] This means is well known as that by which each of us learned the first meanings of words in our mother tongue. (Bolzano 1810, II, §8; Bolzano 2004b: 107; our translation)

Bolzano called such circumlocutions “paraphrases” or “circumscriptions” [*Umschreibungen*]. His method points towards a solution of the paradox of definition according to which all concepts are ultimately defined in terms of simple concepts, but these remain undefined and thus devoid of meaning.

Bolzano also presents two important criteria for the correctness of proofs: according to the first, “If the subject (or the hypothesis) of a proposition is as wide as it can be so that the predicate (or the thesis) can be applied to it, then in any correct proof of this proposition all characteristics of the subject must be used, i.e., they must be applied in the derivation of the predicate.” The second is Bolzano’s version of Aristotle’s ban on crossing from one genus to another: one cannot deduce a general proposition from one of its special cases (Bolzano 1810, II, §28, 29; Bolzano 2004b: 122–126). In a proof of the intermediate value theorem, for instance, one of the necessary conditions is that the functions be *real-valued*. An attempted proof that makes no use of any attribute separating the reals from the rationals can accordingly be diagnosed as incorrect according to the first criterion, while an attempted proof that appeals to geometry or kinematics will run afoul of the second. These insights immediately bore fruit in Bolzano’s mathematical work (1816, 1817).

## 2. Logic as theory of science

Bolzano did not long remain satisfied with the logic sketched in the *Contributions* Already in 1812, he recorded his intention to develop a new logic which would lead to a “total transformation of the *a priori* sciences”. The *Theory of Science*, written between 1820 and 1830 and published in 1837, marks its realization, embedded in the broader context of general epistemology and methodology of science (which Bolzano also counted as logic in a broader sense).

Bolzano defined the theory of science by its ultimate goal, which is the division of human knowledge into disciplines and the composition of scientific treatises. According to the definition, the theory of science is

> the collection of all rules which we must follow, if we want to do a competent piece of work, when we divide the total domain of truths into individual sciences, and present them in their respective treatises. (*TS*, I, §1, 7)

This definition presupposes a whole sequence of disciplines involved in the construction of a science, each of which is founded on the preceding one. The ultimate discipline in this sequence deals with the delimitation of sciences and the principles of style of scientific writing that should lead to the composition of a collection of scientific treatises forming an encyclopedia. Bolzano hoped that, following the Great Encyclopedia of Diderot and D’Alembert, the ideal of the Enlightenment, the effort to spread scientifically organized useful knowledge would again find its finest expression in the completion of an encyclopedia. In this way, the *TS* would contribute to the general well-being.

In order to divide truths into different disciplines and present them in particular treatises, we first have to discover them. Such is the goal of *The Art of Discovery* or *Heuristic*, which contains rules for finding new truths. Heuristic presupposes the possibility of recognizing truths, which is the object of *The Theory of Knowledge*. Now, the decisive step in the exploration of the layers of science leads to the most important part of the *TS*, *The Theory of Elements*, which analyses the objective conditions of the subjective activity of knowing, namely the theory of ideas, propositions and deduction, considered in and of themselves, in short: formal logic. The *Theory of Fundamentals* attempts to show that these elements are propositions in themselves and ideas in themselves, that there are infinitely many truths in themselves and that we can know at least some of them. Taking all the disciplines of the *TS* in the due order, we obtain the following structure:

- Theory of Fundamentals (Vol. I, §§17–45),
- Theory of Elements, i.e., formal logic (Vol. I and Vol. II, §§46–268),
- Theory of Knowledge (Vol. III, §§269–321),
- Heuristic (Vol. III, §§322–391),
- Theory of Science Proper, i.e., the theory of the division of the truths into particular sciences and the principles of composition for scientific treatises (Vol. IV, §§392–718).

## 3. Propositions in themselves

Bolzano’s first important innovation in the *TS* aims at the transformation of the domain of logic (more specifically, of the Theory of Elements). According to him, logic is not a theory of ideas and judgments in our mind, it is not an *art de pensée* in the sense of Arnauld’s and Nicole’s *Port-Royal Logic* or an exposition of the laws of thought. Rather, logic is concerned with the objective relations between propositions and ideas *in themselves*, that is, independently of their being thought or expressed.

Although Bolzano took propositions to be composed of parts, which he called *ideas*, he does not offer a definition of the concept of a proposition as a certain kind of structured whole. The reason for this was that no definition he had found in the writings of others, nor any that he could think of himself, was satisfactory. Instead, he seeks to convey what he means by ‘proposition’ using the procedure he had earlier called ‘circumscription’ (cf. *TS*, §668, no. 9), presenting the reader with a number of sentences containing the word that are supposed to be true when it is rightly understood.

> One will gather what I mean by *proposition* as soon as I remark that I do not call a *proposition in itself* or an *objective proposition* that which the grammarians call a proposition, namely, the linguistic expression, but rather simply the meaning of this expression, which must be exactly one of the two, true or false; and that accordingly I attribute actuality to the grasping of a proposition, to *thought* propositions as well as to the *judgments made* in the mind of a thinking being (existence, namely, in the mind of the one who thinks this proposition and who makes the judgment); but the mere proposition in itself (or the *objective proposition*) I count among the kinds of things that do not have any existence whatsoever, and never can attain existence. Our *thinking* of a proposition, our *judgment* that a thing is so and so, is something actual, which began at a certain time and will end at a certain time; the written *signs*, through which we record these propositions in some place or other are equally really existing things; the propositions themselves, however, do not exist in any time or place. (Bolzano 2004a: 40–41)

The expression ‘in itself’, as Bolzano explains elsewhere, is used to indicate that a term is used in its full generality, and hence that any customary tacit additions (such as *thought* or *expressed in a language*) should be suppressed (*TS*,§ 57, no. 2). In view of the unhelpful Kantian associations with the expression ‘in itself’, Bolzano’s expression ‘*an sich*’ might also be rendered as ‘as such ’ (as suggested by Jan Berg) or ‘*per se*’.

Bolzano maintained that *there are* (*es gibt*) propositions in themselves, though they are not *actual* (*wirklich*), that is, do not act, or enter into causal relations. Thus they have the status often accorded to mathematical objects. And although he thought that the recognition of propositions in themselves was crucial for metaphysics, he also sought to persuade those who did not share his metaphysical views to accept propositions based on pragmatic and methodological considerations (*TS*, §20, no. 1).

In this article, we will follow the common practice of the secondary literature on Bolzano by using square brackets to form designations of propositions in themselves and like entities. Thus, for instance, ‘[Socrates has wisdom]’ designates the proposition in itself expressed by the sentence ‘Socrates has wisdom’, while ‘[Socrates]’ designates the part of that proposition (or idea) designated by ‘Socrates’.

### 3.1 Forms of propositions

In Bolzano’s view, propositions can be expressed more or less adequately by sentences, and consideration of linguistic structures accordingly informs his treatment of the parts and structures of propositions. Consider a sentence such as ‘Romeo loves Juliet’, for instance. We recognize that we could replace ‘Romeo’ with another proper name such as ‘Othello’ and still have a perfectly grammatical sentence. Moreover, given a set of proper names, we can specify a class of sentences that differ from ‘Romeo loves Juliet’ at most by having a different one of those names at the beginning. We could proceed similarly with ‘loves’ and a suitable set of transitive verbs. Or we could consider the class of sentences obtainable when both sorts of replacements are permitted, and so on. These classes of sentences would correspond to the *sentential forms* ‘**a** loves Juliet’, ‘Romeo **V** Juliet’, and ‘**a V** Juliet’, respectively.

So too, Bolzano clearly thinks, with propositions in themselves. Given a proposition, we can think of others just like it except for having different parts (ideas) at certain places. And though there can be no actual variation, i.e., no change in time, in the realm of propositions in themselves, nor any places strictly speaking, we can nonetheless speak metaphorically of making substitutions at certain places within propositions, using this as a *façon de parler* about atemporal relations between propositions and their parts. Given a proposition, then, we can consider certain of its parts *variable*, i.e., subject to replacement by other parts, and, given classes of suitable substituends for each site of substitution, we can again determine a class of propositions.

If certain parts of a sentence correspond to parts of the proposition it expresses, the sentential forms we obtain by replacing one or more of these parts with signs for variables, along with a specification of permissible substituends, will determine not just a class of sentences but also a class of propositions of the kind just described. Bolzano sometimes calls such classes of propositions *propositional forms*. Strictly speaking, however, he reserves this term for the sentential forms that determine such classes:

> [T]he proposition “Some people have white skin” occurs in logic at best as an example, and not as the subject of a theorem, while a class of propositions, such as the class determined by the expression “Some **A** are **B**” may well be the subject of a theorem. If these classes of propositions are to be called general *forms* of propositions, then it is permissible to say that logic is concerned with forms rather than with individual propositions. (Actually, only the written or oral *expression* “Some **A** are **B**”, and not the class itself, should be called a form). (*TS*, §12, no. 2 [I.48])

Note that a sentence need not be perfectly distinct (i.e., such that there is a one-to-one structure-preserving correspondence between its parts and the parts of the proposition is expresses) to be used in this way, provided only that the parts of the sentence that are replaced by signs for variables do correspond to parts of the proposition. For instance, if we are satisfied that ‘mammal’ and ‘bear’ correspond to parts of the proposition [Some mammal is a bear], we can use the sentential form ‘Some $A$ is a $B$’ to determine a class of propositions, even if it turns out that this proposition might be more distinctly expressed by a different sentence, e.g., by ‘There exists an individual that is a mammal and that is also a bear.’

Since different parts of a proposition may be considered variable, each proposition belongs to a number of different forms. In particular, there is no absolute distinction between the form and matter of propositions on Bolzano’s definition.

## 4. Ideas

As mentioned above, Bolzano defines an *idea* as a part of a proposition, more precisely, as “any constituent of a proposition that is not itself a proposition” (*TS*, §128, no. 2 [II.18]; cf. §48). For example, assuming the sentence ‘Fido, who is a dog, is not a reptile’ to be a fairly distinct expression of the corresponding proposition, we might distinguish within that proposition ideas (i.e., sub-propositional parts) such as [Fido], [dog], [reptile], but also [who], [is], and [not]. As with propositions, Bolzano carefully distinguishes between ideas in themselves, thought (or subjective) ideas, and linguistic signs for ideas.

Bolzano’s term is ‘*Vorstellung*’. This was the standard rendering of ‘idea’ in German translations of Locke, Hume, *et al.* It is also sometimes rendered as ‘presentation’ or ‘representation’, e.g., in translations of the works of Kant and Husserl. Bolzano’s decision to continue to use the term tends to obscure the vast differences between his views and those he found in the logical literature of his time. Ideas, for him, are akin to Husserl’s part-meanings or to Fregean senses other than thoughts. This is not at all what most of the authors Bolzano discussed meant when they spoke of ideas, even if there was a tiny point of contact in the circumstance that, like him, those authors usually maintained that ideas (or notions, concepts, cognitions) could occur as parts of judgments, namely, as their subjects and predicates.

Bolzano recognizes three individuating features of ideas with objects : *extension, content*, and *structure*. Loosely speaking, the extension of an idea is “the collection of all the objects standing under it” (Bolzano 2004a: 46); more strictly, it is “that particular attribute of an idea by virtue of which it represents only those and no other objects.” (*TS*, §66, I:298). While ideas with different extensions, for example, [prime number] and [odd number], are perforce different on Bolzano’s account, this is only a sufficient condition, witness the coextensive but clearly different ideas [even prime number] and [positive square root of 4].

Though these ideas are coextensive, we can still distinguish them by noting that they have different parts, e.g., that [prime] occurs in the first, but not in the second. Bolzano will say in such cases that the *content* of the two ideas is different. According to his definition, the content of a complex idea is the *sum* of its parts. ‘Sum’ is a technical term in Bolzano’s ontology, designating collections “in which the manner of combination does not matter and in which the parts of the parts may be considered parts of the whole” (*TS*, §84). For our purposes, it is sufficient to note that when Bolzano asks us to think about the content of an idea, he wants us to consider its parts, but not their arrangement.

To resume: ideas with different content also differ. Once again, however, this condition is merely sufficient, as the same parts can be arranged differently, witness: [ignorant son of a learned father], [learned son of an ignorant father]. Accordingly, Bolzano recognizes the *structure* of a complex idea, the way its parts are combined (their *Verbindungsart*), as an additional individuating attribute. Indeed, sometimes structure is the only individuating attribute, as Bolzano shows in *TS* (§96, no. 2) with the clever example of [$2^{4}$] and [$4^{2}$], which have the same content and the same extension but differ nonetheless.

Although in many cases ideas are assumed to be structured like linguistic expressions, it is also clear that Bolzano recognized ideas whose structure cannot be captured in a linear script. For example, in ideas of the form ‘$A$, which has the properties $b, b', b'',\ldots$’, no ordering is supposed between the parts $b, b', b'',\ldots$, which occur in the idea in itself as a unordered collection (*Menge*).

Bolzano was a semantic atomist: in his view, all ideas are ultimately composed of simple parts, which are themselves ideas (*TS*, §61). In the case of simple ideas with objects, there is no content strictly speaking since there are no parts, and hence no structure either. Thus such ideas are individuated by their extensions alone (*TS*, §93, no. 3). The relation of a simple idea to its objects is primitive, hence undefinable. It is instructive to compare this position with the contemporary practice of interpreting a formal language by assigning extensions (objects or sets of objects) to the non-logical constants (or parameters).

Bolzano does not tell us how simple ideas without objects (e.g., [and], [not]) are individuated. This strikes us as a significant oversight.

### 4.1 Varieties of ideas

Some ideas, called *objectual* (*gegenständlich*) by Bolzano, have, or represent, one or more objects, for instance, [the Bolzano-Weierstrass theorem], [raven]. Others are *objectless* (*gegenstandlos*), e.g., [round square], [golden mountain], [not] (*TS*, §67). Not recognizing empty collections, Bolzano says that objectless ideas have no extensions.

If an idea has exactly one object, it is called *singular*, and, if has more than one, *general* (§68). Some general ideas are complex, e.g., [star of the first magnitude]. Others, Bolzano maintains, are simple: he thinks that [object] and [attribute] are likely such. In the case of singular ideas, similarly, he holds that some are complex, e.g., [the most massive planet in our solar system], while others are simple. Appropriating Kant’s term for his own purposes, he calls the latter kind of ideas, that is, simple, singular ideas, *intuitions* (§72). Ideas that are not intuitions and do not have any intuitions among their parts are called (pure) *concepts*, while ideas that have both concepts and intuitions among their parts are called *mixed* (§73).

Those familiar with the role played by logically proper names in Russell’s philosophy of logical atomism will have an easier time understanding Bolzano’s use of the concept of an intuition. Intuitions are the counterpart in the realm of ideas in themselves to the essentially indexical elements in language: they are best expressed by using a bare demonstrative (‘this’) and, in the case of subjective human intuitions, always have particular contemporaneous mental states as their objects. Any singular idea of a contingently existing particular, moreover, must number intuitions among its parts. Intuitions thus serve as markers of empirical content.

If no part of a proposition is an intuition, it is called *purely conceptual*, otherwise *intuitional*. This distinction, defined at the level of propositions in themselves, is prior to the distinction between *a priori* and *a posteriori* judgements, and used to define it:

> If the propositions from which a judgement *M* is deduced, as well as those from which the former follow, down to the immediate judgements, are all purely conceptual propositions, then judgement *M* can be called a *judgement from pure concepts*, or *pure*, or *a priori*. In all other cases it could be said to be *drawn from experience* or *a posteriori*. (*TS*, §306, no. 12)

Some sciences, e.g., number theory or real analysis, consist entirely of purely conceptual propositions, and are accordingly called *purely conceptual sciences*. Though Bolzano optimistically held that *most* purely conceptual truths could be known *a priori*, he refrains from claiming this of all of them, and clearly recognizes that many purely conceptual propositions, even in mathematics, are accepted based at least partly on empirical (intuitional) evidence (*TS*, §133; Bolzano 2004a: 53).

### 4.2 Extensional relations between ideas: the logic of classes

Of the two main parts of Bolzano’s formal logic, the extensional logic of ideas (the logic of classes) and the extensional logic of propositions, the first part comes from a long tradition beginning with Boethius (and derived from Aristotelian syllogistic) and ending — in Bolzano’s times — with Gergonne. Bolzano did not take his logic of classes from Gergonne or Euler, the most influential authors in their time, but rather from a small booklet entitled *Outline of Logic* (*Grundriß der Logik*) by a now completely forgotten logician, J.G.E. Maaß, published in 1793.

In *TS*, §§ 94–108, Bolzano defines a system of relations between the extensions of ideas, and proves various theorems about these relations. To begin with, ideas $A, B, C, \ldots$ are said to be *compatible* just in case there is at least one object that stands under all of them; otherwise, they are called incompatible. In the case in which not only some but all objects represented by $A$ are also represented by $B$, $A$ is said to be *included* in $B$. If the converse also holds, i.e., if $A$ is included in $B$ and $B$ included in $A$, the ideas $A$ and $B$ are called *equivalent* (or *interchangeable*). He defines two further special cases: first, compatibility where neither $A$ is included in $B$, nor $B$ in $A$; Bolzano calls this relation *overlapping* or *linking*. Second, we have the relation of *subordination*, which is inclusion without reciprocity.

Three kinds of incompatibility are distinguished: mutual exclusion, contradiction and contrariety. Ideas $A$, $B$, *C*, … are said to *exclude* each other iff they are pairwise incompatible. The ideas $A$ and $B$ are contradictory iff $B$ has “an extension that includes everything that does not stand under the idea $A$” (*TS* II, §103, 477), i.e. if $B$ is equivalent to *non-A*. They are *contrary*, finally, iff they are incompatible but not contradictory.

As all these relations are derived from compatibility and its negation, it is possible to represent them in the form of a genealogical tree (see Šebestík 1992: 174). Simplifying somewhat, we can define Bolzano’s relations for pairs of ideas in the language of set theory as shown below. (Here, we depart from Bolzano by also admitting universal ideas such as “something in general” [*Etwas überhaupt*], along with objectless ideas and the empty set as their extension (for Bolzano, an objectless idea has no extension, and there are no empty collections)).

| $A \textrm{ is } \textit{compatible} \textrm{ with } B $ | $ =_{\textrm{df}} $ | $Ext(A) \cap Ext(B) \not= \emptyset$ |
| --- | --- | --- |
| $A \textrm{ is }\textit{incompatible}\textrm{ with } B$ | $=_{\textrm{df}}$ | $Ext(A) \cap Ext(B) = \emptyset$ |
| $A\textrm{ is }\textit{included}\textrm{ in } B$ | $=_{\textrm{df}}$ | $A$ is compatible with $B$ and $Ext(A) \subseteq Ext(B)$ |
| $A\textrm{ is }\textit{equivalent}\textrm{ to }B$ | $=_{\textrm{df}}$ | $A$ is included in $B$ and $B$ is included in $A$ |
| $A\textrm{ is }\textit{subordinate}\textrm{ to }B$ | $=_{\textrm{df}}$ | $A$ is included in but not equivalent to $B$ |
| $A\textrm{ is }\textit{contradictory}\textrm{ with } B$ | $=_{\textrm{df}}$ | $A$ is incompatible with $B$ and $ Ext(A) \cup Ext(B) = \textrm{universal class}$ |
| $A$ is *contrary* to $B$ | $=_{\textrm{df}}$ | $A$ and $B$ are incompatible but not contradictory. |

## 5. The analysis of propositions

If Bolzano’s thesis of semantic atomism is correct, then there is a *finest* form for every proposition; namely, the one in which every simple idea in the proposition is considered independently variable. We can see from this the task that confronts someone who seeks to define the concept of a proposition as a certain kind of structured whole using formation rules: this would require not only a specification of all possible syntactic structures, but also a complete set of semantic categories (since different sites of variation may come with different classes of admissible items). Moreover, it would be necessary to do this not just for a formal language of our own devising, or for a single natural language, but for any possible language. Seen in this light, Bolzano’s forthright admission that he could find no satisfactory definition of the concept of a proposition is hardly surprising.

Instead of trying to begin with simple ideas and construct propositions from them, Bolzano works from the outside in, trying to distinguish parts within propositions, generally following what Quine called the “maxim of shallow analysis”, namely, “expose no more logical structure than seems useful for the deduction or other inquiry at hand” (Quine 1960: §33; 160)[^quine-1960]. Since propositions in themselves are causally inert, this cannot be done by inspecting them. Rather, one considers linguistic expressions, drawn from a variety of languages, along with one’s own thoughts, and attempts to identify features of logical significance, bearing in mind that “common usage does not aim at logical correctness but rather at brevity and *sufficient* distinctness.” (*TS*, §170 [II.213]; see also §350, 366).

Bolzano makes a number of specific proposals concerning the analysis of propositions, most of them now of merely historical interest. We will briefly present a few of these here.

First, he argues that every proposition belongs to the subject-predicate form ‘$A$ has $b$’ (*TS*, § 127; recall that this does not prevent them from also belonging to other forms.) He acknowledges that he has no conclusive argument for his thesis, but claims that he has been able to find acceptable subject-predicate paraphrases of all the sentence forms that have occurred to him (Bolzano 1841: 48).

In true propositions of this form, the place marked by ‘$A$’ is occupied by an idea that has one or more objects, while the place marked by ‘$b$’ is occupied by an idea representing one or more attributes. The copula, expressed by ‘has’, understood to be without tense or number, indicates the possession of an attribute. Tense is dealt with by adding temporal determiners to the subject-idea. For example, ‘Smith is in pain’ would be more distinctly expressed as ‘Smith at the present moment–has (tenselessly)–pain’ (§127, no. 5).

Since both the subject- and predicate-ideas may be general, we must understand ‘$A$ has $b$’ to convey that every object standing under the idea [$A$] has an attribute standing under the idea [$b$] (§131). Accordingly, he takes propositions of the form ‘All $A$ have $b$’ to be synonymous with those of the forms ‘Each $A$ has $b$’ and ‘$A$ has $b$’, e.g., ‘All men have mortality’, ‘Each man has mortality’, and ‘Man has mortality.’

Bolzano believes that the subject-predicate form can accommodate relational claims, interpreting them as statements about collections. For instance, a claim that items $A, B, C, \ldots$ are equal in the sense of all having attributes $b, b', b'', \ldots$ could be interpreted as a claim about a collection containing two unordered sub-collections (*Mengen*), i.e., $\langle (A, B, C, \ldots), (b, b', b'', \ldots)\rangle$, stating that the collection has the attribute that every item in the first sub-collection has each of the attributes in the second sub-collection (cf. §135, no.15).

For Bolzano, truth and falsity (or lack-of-truth) are properties of propositions. Given his assumption that all propositions belong to the form ‘$A$ has $b$’, he is able to offer the following definition of truth (*TS*, §28):

> A proposition is true when it states what belongs to its object.

That is,

> [$A$ has $b$] has truth iff $A$ has $b$.

Bolzano’s analysis of existential claims such as ‘There are prime numbers greater than 100’ is also noteworthy. What we mean in such cases, he says, is that the idea [prime number greater than 100] has objectuality (§137). This analysis shows its worth in the case of true negative existentials such as ‘Round squares do not exist’, allowing him to solve the associated riddle of non-being. For this sentence says the same as the more distinct ‘[Round square] has lack-of-objectuality’ according to Bolzano, and, in this case, we have an objectual subject-idea (its object is the *idea* [round square]) and ascribe to its object a property that it has (namely, objectlessness) (§138).

Bolzano proposes similar analyses of forms such as ‘Some $A$ are $B$’ and ‘No $A$ is $B$’. These are taken to be more distinctly expressed as follows: ‘[$A$, which has $b$] has objectuality’, and ‘[$A$, which has $b$] has non-objectuality’, respectively (§137,138).

Claims of objectuality are not to be confused with claims of *actuality* (§142). Though, for example, Bolzano maintained that there are (*es gibt*) propositions and ideas in themselves, as well as geometrical points and other mathematical objects, he denied at the same time that they had actual existence (i.e., they do not act, or enter into causal relations, no spatial or temporal determinations attach to them, etc.). The ideas [proposition in itself], [geometrical point], etc., that is, have objectuality but propositions, points, etc., lack the property of actuality.

Bolzano distinguishes predicate and propositional negation, the former taking the form ‘$A$ has non-$b$’, the latter ‘[$A$ has $b$] has non-truth’ (§189, 1(e); cf. §136). The two forms are not equivalent, since, for example, [Mozart’s 35th piano concerto is not in E-flat] is false, its subject-idea being objectless, while [[Mozart’s 35th piano concerto is in E-flat] has non-truth] is true.

Material disjunctions, i.e., claims of the forms ‘$A$ or $B$ or $C \ldots$’ are paraphrased as follows (§181): ‘[True proposition in the collection ($[A], [B], [C], \ldots$)] has objectuality’ (inclusive disjunction) or as ‘[True proposition in the collection $([A], [B], [C], \ldots$)] has objectuality and [Plurality of true propositions in the collection ($[A], [B], [C], \ldots$)] has non-objectuality’ (exclusive disjunction).

We hope this is enough to give some sense of Bolzano’s approach and some of its limitations. More details may be found in the secondary literature.

## 6. Bolzano’s logic of variation

### 6.1 Propositions and propositional forms

Bolzano’s logic of extensional relations between propositions represents a major innovation which has no equivalent in traditional logic. It is based on the method of variation that we have already encountered. Bolzano introduces this part of his logic as follows:

> Given a proposition, we could merely inquire whether it is true or false. But some very remarkable properties of propositions can be discovered if, in addition, we consider the truth values of all those propositions which can be generated from them, if we take some of their constituent ideas as variable and replace them by any other ideas whatever. (*TS*, §147)

Often, Bolzano uses sentential forms such as ‘The man **A** is mortal’ in his discussions. At other times, he will simply write something like this: “Let us … consider the proposition ‘The man Caius is mortal’, and let us envisage the idea ‘Caius’ as arbitrarily variable” (*TS*, § 147).

These two manners of speaking correspond to two different levels. On the first, linguistic level, we deal with sentential forms, i.e., expressions containing signs for variables, which become sentences (and express propositions) after appropriate substitutions are made. The second level is the level of propositions and ideas in themselves, the level of meaning. Here, Bolzano cannot use variables, letters or other indeterminate signs, for, in the realm of the propositions and ideas in themselves, there are no indeterminate entities that would correspond to sentential forms; there are only propositions, true or false. This might be the reason for Bolzano’s cumbersome way of speaking about “the idea *Caius* considered variable”.

Bolzano’s loose manner of speaking about substitutions of ideas in propositions is adopted in what follows. To declare one or several ideas in a given proposition variable is to consider the class of all propositions which have the same structure and contain the same ideas except perhaps at places occupied by the variable ideas. A proposition which results from such a substitution performed on the given proposition is called a *variant*.

The class of allowable substituends is often restricted by Bolzano; in some cases, for instance, he will require that the substitutions do not “destroy the objectuality of the proposition,” that is, do not produce an objectless subject-idea. Such would be, for example, the effect of substituting [Beijing] for [Nero] in the proposition [Nero, who is a human being, is mortal]. In his discussion of the degree of validity of a proposition relative to certain ideas, too, he stipulates that no two equivalent ideas may be included in the class of possible substituends. Thus when Bolzano speaks of “variable ideas”, we should bear in mind that the specification of a variable also involves the specification of a range of possible values.

### 6.2 Universal validity/invalidity and analyticity

Bolzano begins by defining attributes of of single propositions with variable parts (*TS*, §147). When the method of variation is applied to a proposition, he notes, three different cases may arise: either the class of (objectual) propositions obtained by substitution contains only true propositions, or it contains only false propositions, or it contains both true and false propositions. In the first case, the initial proposition is called *universally valid*, in the second *universally invalid*, in both cases relative to the specified variables. Bolzano does not give a name to the third case; such propositions could be called neutral. Here are some examples:

[The man Caius is mortal]

is universally valid relative to the variable idea [Caius], because each appropriate substitution generates a true proposition, or alternatively, because all its objectual variants are true.

[The man Caius is omniscient]

is universally invalid relative to the same variable idea [Caius], because all its variants are false.

The same proposition

[The man Caius is wealthy]

is neutral relative to the variable idea [wealthy], because some of its variants are true (e.g., the first example quoted) while others are false (the second example).

Consider now the proposition [Murgatroyd’s favourite number, which is an integer between 1 and 10, is prime], and let [Murgatroyd’s favourite number] be tagged as variable. Furthermore, let us restrict the class of permissible substituends by stipulating that (1) objectuality be preserved and (2) no two equivalent ideas be included. In this case, there will be eight permissible substitutions and, of these, four will result in true propositions. The ratio of the number of substitutions resulting in true propositions to the total number is accordingly equal to 1:2. Bolzano calls this the *degree of validity* of the proposition relative to the specified variables. He comments (*TS*, II: 81): “This ratio determines the degree of probability which the proposition takes on under certain circumstances.” Universal validity and universal invalidity are extreme cases, in which the ratio is respectively equal to 1:1 and 0:1.

Bolzano appropriated Kant’s term *analytic* for propositions that are either universally valid or universally invalid relative to some specification of variable parts or other. This choice of terminology was based on his analysis of Kant’s examples. Consider, for instance, the proposition (Kant: judgement): [A right-angled triangle is a triangle]. Kant had declared such judgments analytic because analysis, i.e., decomposition, of the subject concept would reveal the presence of the predicate. For Bolzano, this containment relation was just a distraction: what was truly interesting about this proposition, he thought, was that we could substitute whatever other ideas we like for [triangle] and [right-angled] without changing the truth-value (subject to the proviso about objectuality). That is, as Quine would later put it, certain parts of such propositions occur *vacuously*:

> I believe that th[e] importance [of analytic propositions] lies in the fact that their truth or falsity does not depend upon the individual ideas of which they are composed, but that it remains the same irrespective of the changes to which some of their ideas are subjected, provided only that the objectuality of the proposition is not destroyed. (*TS*, § 148)

The truly noteworthy feature of the propositions Kant had called analytic, that is, is the invariance of their truth-value under an entire class of transformations. It is this feature and no other that Bolzano singles out with his definition of analyticity.

Given the breadth of Bolzano’s definition, it is clear that analytic propositions are quite common, notably in mathematics. Here are some of Bolzano’s examples of analytic propositions, true as well as false, where the underlining or the letters indicate the variable parts:

- If all men are mortal and Caius is a man, then Caius is mortal. (*TS*,§315)
- If $A$ is larger than $B$, then $B$ is smaller than $A$. (*TS*,§148)
- If $P=Mm$, then $M = P/m$. (*TS*, §148)
- The soul of Socrates has been annihilated. (*TS*, § 369)
- The soul of Socrates is a simple substance. (*TS*, §447)
- $A$ is $A$. (*TS*, §148)
- An $A$, which is $B$, is $A$. (*TS*, §148)
- An $A$, which is $B$, is $B$. (*TS*, §148)
- Every object is either $B$ or non-$B$. (*TS*, §148)

The last four examples in the above list are noteworthy, Bolzano claims, because the only invariable parts in them are logical concepts. He speaks of *logical analyticity* in such cases. Like Tarski after him, he comments that his definition of logical analyticity is not completely determinate, because the “domain of concepts belonging to logic is not circumscribed so sharply that controversies could not arise at times” (*TS*, § 148, no. 3; Tarski 1983, 418–419).

Though the similarities should not be exaggerated, there are clear affinities between this narrower notion and later ones in the works of Adjukiewicz, Carnap, Quine, and Tarski (see Künne 2006 for detailed discussion)[^künne-2006].

As Bolzano was well aware, analyticity in his general sense entails neither necessity nor apriority (*TS*, §197). [Truman, who was president of the USA in in the 20th century, was male], for instance, is universally valid with respect to [Truman], and thus analytic according to Bolzano’s definition. Clearly, his use of the term ‘analytic’ differs radically not only from Kant’s, but also from later uses of the term in the writings of Frege, Carnap, and others. This has led to some misunderstandings on the part of some of his later readers (e.g., Bar-Hillel 1950)[^bar-hillel-1950].

### 6.3 Relations among several propositions with variable parts

In contemporary treatments of logic, logical relations between formulas of a formal language are sometimes defined in terms of relations between sets of interpretations of the language. For example, a set of formulas *Γ* might be said to *imply* a formula *α* iff the set of interpretations making all members of *Γ* true is a *subset* of the set of interpretations making *α* true, while *Γ* itself might be said to be *satisfiable* iff the set of interpretations making all its members true is non-empty.

Bolzano’s system of extensional relations between propositions with variable ideas is motivated by similar thoughts, though it is cast in terms of the extensions of ideas, propositions, and variable ideas within them. The key notion is that of a collection of ideas $i’, j’, k’, \ldots$ which, when substituted for the variable ideas $i, j, k, \ldots$ in propositions $A, B, C, \ldots$, results in a collection of propositions all of which are true. (More loosely, Bolzano speaks of “collections of ideas whose substitution for $i, j, k, \ldots$, makes all of $A, B, C, \ldots$ true” (*TS* II: §155, 114, 122, and §156, 133).) We will call such collections of ideas $i’, j’, k’, \ldots$ *verifying ideas* for $A, B, C, \ldots$ relative to the variable ideas $i, j, k, \ldots.$

In a crucial passage, Bolzano sets up the correspondence he needs to carry out his plan:

> With ideas, the crucial question was whether or not a certain object is indeed represented by them; the corresponding question for propositions is whether or not they are true. Just as I have called ideas compatible or incompatible with each other, depending on whether or not they have certain objects in common, so I call propositions compatible or incompatible, depending on whether or not there are certain ideas which make all of them true. (*TS* II: §154, 101; Bolzano 1973: 198–199)

That is, just as *ideas* $A, B, C, \ldots$ are said to be *compatible* iff at least one object stands under each of $A, B, C, \ldots$, so too we can say that *propositions* $A, B, C, \ldots$ are compatible with respect to variable ideas $i, j, k, \ldots$ iff there is at least one collection of ideas $i’, j’, k’, \ldots$ which are verifying ideas for each of $A, B, C, \ldots$. Equivalently, $A, B, C, \ldots$ are compatible relative to $i, j, k, \ldots$ iff the *ideas* [verifying ideas for $A$ relative to $i, j, k, \ldots$], [verifying ideas for $B$ relative to $i, j, k, \ldots$], [verifying ideas for $C$ relative to $i, j, k, \ldots$] are compatible in the previously defined sense; otherwise, they are said to be incompatible.

For example, the propositions [Wellington predeceased Napoleon] and [Napoleon predeceased Wellington] are incompatible when all occurrences of [Napoleon] and [Wellington] are considered uniformly variable, but compatible when [predeceased] is varied in both propositions, since the substitution [fought] for [predeceased] produces two true propositions. (Here, we have to do with the forms ‘ $\mathbf{A}$ predeceased $\mathbf{B}$’ and ‘ $\mathbf{B}$ predeceased $\mathbf{A}$’ in the first case, and ‘Napoleon **R** Wellington’ and ‘Wellington **R** Napoleon’ in the second.)

Next, propositions $M, N, O, \ldots$ are said to be *deducible* from propositions $A, B, C, \ldots$ with respect to variable ideas $i, j, k, \ldots$ iff $A, B, C, \ldots, M, N, O, \ldots$ are compatible with respect to variable ideas $i, j, k, \ldots$ and the idea [verifying ideas for $A, B, C, \ldots$ relative to $i, j, k, \ldots$] is included in the idea [verifying ideas for $M, N, O, \ldots$ relative to $i, j, k, \ldots$] in the previously defined sense, i.e., iff the extension of the former is a subset of the extension of the latter (*TS*, § 155).

In the shorter version of his logic, Bolzano states this definition as follows:

> If one or more propositions $A, B, C, \ldots$ are compatible with one or more others $M, N, \ldots$ with respect to the components $i, j, \ldots$, then there must be, as just said, at least some ideas that, when put in the places of $i, j, \ldots$ make all of $A, B, C, \ldots$ as well as all of $M, N, \ldots$ true. One especially noteworthy case occurs, however, if not just some, but *all* of the ideas that, when substituted for $i, j, \ldots$ in $A, B, C, \ldots$ make all these true, also make all of $M, N, \ldots$ true. In this case I say that the propositions $M, N, \ldots$ stand in the relation of *deducibility* to the propositions $A, B, C, \ldots$ with respect to the variable parts $i, j, \ldots$. (Bolzano 2004a: 54)

He gives the following examples: [All $i$ are $k$] is deducible from [All $i$ are $j$] and [All $j$ are $k$] , and [$\angle ijk = \angle ikj$] is deducible from [$i, j, k$ are the three vertices of a triangle] and [$\overline{ij}$ = $\overline{ik}$], in both cases with respect to $i, j, k$.

Proceeding in this way through his table of relations among ideas, Bolzano obtains at one stroke a complete system of extensional relations between propositions, relative to certain of their parts considered variable (in other words, between propositional *forms* in the sense of *classes* of propositions). The result is a genealogical tree whose fundamental structure is exactly the same as the structure of the tree representing the relations between ideas. In most cases, he uses the same terms, speaking of compatibility, deducibility (inclusion), subordination (unilateral deducibility), equivalence (mutual deducibility), overlapping, contrariety, and contradiction among propositions.

To obtain a clearer overview of these relations, let us introduce some notation and once again use the language of set theory. We will use bold letters to symbolize sets of items (propositions or variable ideas). Thus, for instance, ‘$\mathbf{A(i)}$’ and ‘$\mathbf{M(i)}$’ will be used to represent sets of propositions $\mathbf{A}=\{A, B, C, \ldots\}$ and $\mathbf{M}=\{M, N, O, \ldots\}$ in which the ideas $\mathbf{i}=i, j, k, \ldots$ are considered variable. Let $\mathbf{V(A(i))}$ represent the set of verifying ideas for $\mathbf{A(i)}$. Finally, let $\mathbf{\neg A}$ represent $\{\neg A, \neg B, \neg C, \ldots\}$. We then have:

**A** is compatible with **M** with respect to variable ideas **i**: $\mathbf{V(A(i))} \cap \mathbf{V(M(i))} \not= \emptyset$

**A** is incompatible with **M** with respect to **i**: $\mathbf{V(A(i))} \cap \mathbf{V(M(i))} = \emptyset$

**M** is deducible [*ableitbar*] from **A** with respect to **i**: **A** and **M** are compatible with respect to **i** and $\mathbf{V(A(i))} \subseteq \mathbf{V(M(i))}$.

**A** is equivalent to **M** with respect to **i**: **A** is deducible from **M** and **M** is deducible from **A**, both with respect to **i**, i.e., $\mathbf{V(A(i))} \not= \emptyset$ and $\mathbf{V(A(i))} = \mathbf{V(M(i))}$.

**M** is unilaterally deducible from **A** with respect to **i**: **M** is deducible from but not equivalent to **A** with respect to **i**.

**A** and **M** are contradictory with respect to **i**: $\neg\mathbf{A}$ is equivalent to **M** and **A** equivalent to $\neg\mathbf{M}$, both with respect to **i**.

**A** and **M** are contrary with respect to **i**: **A** and **M** are incompatible but not contradictory with respect to **i**.

Bolzano states and proves a substantial collection of theorems about his relations, including the following:

- If $A, B, C, \ldots$ are incompatible with respect to **i** then any collection of propositions that contains $A, B, C, \ldots$ is also incompatible with respect to **i** (*TS*,§154, no. 10).
- If **A** is compatible with respect to $i, j, \ldots$, then it is also compatible w.r.t. any collection of variands that contains $i, j, \ldots $ (§154, no. 11).
- If $M$ is deducible from $A, B, C, \ldots$ with respect to $i, j, k, \ldots$ then $M$ is also deducible from $A, B, C, \ldots$ relative to any sub-collection of $i, j, k, \ldots$, provided that $A, B, C, \ldots$ are compatible relative to the sub-collection (§155, no. 19).
- $\neg M$ is deducible from **A**, a class of compatible premises, iff **A** is incompatible with *M* (§155, nos. 14, 15).
- If **M** is deducible from **A**, $X$ as well as from **A**, $\neg X$, then **M** is deducible from **A** alone (§155, no. 17).
- If all propositions deducible from the premises **A** are true, **A** is true (§155, no. 6).
- If **M** is deducible from **A**, and **X** from **M**, **R** (both with respect to $i, j, k, \ldots$), then **X** is deducible from **A**, **R** with respect to $i, j, k, \ldots$ (§155, no. 24).
- (§224, no. 2) If the inference: $ \begin{array}{l} A, B, C, D, E, F, G, \ldots \\ \hline M, N, O\\ \end{array} $ is valid, then so is: $ \begin{array}{l} A, B, C, D, \ldots\\ \hline \text{If } E, F, G, \text{ are true, then so are } M, N, O \ldots\\ \end{array} $

### 6.4 Conditional probability

According to Bolzano’s definition, deducibility requires compatibility. This gives rise to some complications, e.g., deducibility is not reflexive, and from the fact that $B$ is deducible from $A$ with respect to $i, j, \ldots$ we can conclude that not-$A$ is deducible from not-$B$ only if $B$ is not universally valid with respect to $i, j, \ldots.$ But it also brings an important benefit, namely, it allows him to integrate a relation of relative probability directly into his system. In *TS*, § 161, he defines the *conditional probability* (or relative validity) of a proposition *M*(**i**) with respect to a class of premises or hypotheses **A**(**i**) with variables **i**, as the ratio of the number of cases in which all the propositions of the class as well as *M*(**i**) are true to the number of cases in which the propositions **A**(**i**) are all true. In other words, it is the ratio of the number of true variants of **A**(**i**) and *M*(**i**) to the number of true variants of **A**(**i**). Bolzano’s conditional probability is objective, *an sich*.

Because for each objectual idea there are infinitely many other equivalent ones, we cannot determine relative probabilities simply by counting variants. It could be done, however, if the class of substitutions were restricted as in the case of relative validity by only allowing one idea among all those equivalent to a given one to be included in the class of substituends, provided that the resulting classes were finite (Bolzano sets out a different proposal in *TS*, §161, no. 7).

For example, consider the premises [The number of eggs in the nest is between 1 and 10] and [The number of eggs in the nest is odd], along with the conclusion [The number of eggs in the nest is prime], in which only the idea [the number of eggs in the nest] is considered variable in each of the propositions. Of the admissible substitutions, four make both premises true and, of those four, three make the conclusion true as well. Thus the degree of validity of the conclusion relative to the premises and the specified variable is .75. We can also think of this as a relation between the forms ‘**A** is between 1 and 10’, ‘**A** is odd’, and ‘**A** is prime’.

One can immediately see why the premises of a probable deduction must be compatible: the probability of *M*(**i**) relative to **A(i)** is defined only if the denominator of the fraction is not zero, which means that the premises **A**(**i**) are compatible. On the other hand, the number of ideas that make both **A**(**i**) and *M*(**i**) true cannot be greater than the number of ideas that make true *M*(**i**); as a consequence, the conditional probability of *M*(**i**) cannot be greater than 1. It is equal to 1 when the number of ideas that make true both **A**(**i**) and *M*(**i**) is equal to the number of ideas that make true **A**(**i**) alone, which means that all substitutions of ideas that make true **A**(**i**) also make true *M*(**i**), i.e., if *M*(**i**) is *deducible* from **A**(**i**). In other words, if *M*(**i**) is deducible from **A**(**i**), its probability relative to **A**(**i**) is equal to 1, which means that the probability equals certainty. The probability is zero if no ideas make both **A**(**i**) and *M*(**i**) true, i.e., if **A**(**i**) and *M*(**i**) are incompatible. Incompatibility and certainty are thus two extreme cases of probability with values of 0 and 1.

Though some details remain rough, this is still an extraordinary achievement. Bolzano’s approach yields the first logical definition of probability. For the first time deductive logic and inductive logic are united in a global theory and the former appears as a limit case of the latter. It is possible that in his *Tractatus* 5.15, Wittgenstein took over Bolzano’s treatment of probability, perhaps through the mediation of the 1st edition of the *Philosophical Propedeutic* of R. Zimmermann (1853)[^zimmermann-1853]. Carnap’s regular confirmation functions, too, are strongly reminiscent of Bolzano’s approach.

Bolzano adds proofs of a number of standard theorems, and also defines subjective probability and different important probabilistic notions such as the degree of confidence, the credibility of a witness, etc. He gives the formula of the degree of credibility of an event reported by independent testimonies as a function of the number of witnesses, of the number of testimonies, and of the number of true and false propositions stated by each witness. All these concepts play an important role in the chapter “on the nature of historical knowledge, particularly concerning miracles” in Bolzano 1834.

Both the class-logical relations and the relations between propositions are constructed from the initial relation of compatibility by adding specific conditions to previously defined relations. Compatibility is thus the basic relation of Bolzano’s extensional logic. It is embedded in the very foundations of his system and all other relations (with the exception of different cases of disjunction, *TS* II, §160), deducibility included, are special cases of it.

### 6.5 Deducibility more closely considered

When defining semantic notions such as joint satisfiability or logical consequence, contemporary logicians generally work with formal languages, the specification of which involves a separation of logical and non-logical elements. Consequence and other semantic relations are then defined in terms of the behaviour of formulas when arbitrary semantic values of the appropriate kinds are assigned to all of the non-logical parameters (usually including a tacit parameter for the domain of quantification). On this view, consequence is a dyadic relation between a set of premises and a conclusion or set of conclusions.

Because non-logical parameters are never held constant, many inferences can only be declared valid if they are interpreted as enthymematic, requiring supplementation in the form of “tacit” premises. For example, $e \lt \pi$ cannot be said to follow from $e \lt 3$ and $3 \lt \pi$ because there are models of $aRb$ and $bRc$ that are not models of $aRc$. Adding $\forall x \forall y \forall z ((Rxy \wedge Ryz) \rightarrow Rxz)$ to the premises, however, we obtain a valid argument form.

By contrast, Bolzano’s deducibility is a relation between propositions in themselves and variable ideas. It does not rely on a strict classification of ideas as either logical or non-logical (as we saw, Bolzano had doubts about whether such a line could be drawn). Indeed, it is not a notion of logical consequence at all, but rather a more general notion of which logical consequence is a special case. Deducibility is a *triadic* relation involving collections of premises, conclusions, and variable ideas.

Thus, for example, [$e \lt \pi$] is deducible from [$e \lt 3$] and [$3 \lt \pi$] with respect to the variable ideas [$e$], [3], and, [*π*]. In agreement with contemporary logic, this conclusion is not deducible from the premises if [$\lt$] is added to the variable ideas, but it is deducible with respect to those variables if we add the allegedly tacit premise. An additional noteworthy feature of Bolzano’s approach is that the allegedly unstated premise is equivalent to the claim that a relation of deducibility holds with respect to the ideas [$e$], [3], and, [*π*] (George 1983)[^george-1983].

The individuation of arguments, on Bolzano’s view, involves not only a specification of premises and conclusions(s) but also of an inference. Usually, inferences embody repeatable patterns or forms. And we determine the form-matter distinction (and thus what the inference is) in each particular case by specifying which ideas are to be considered variable:

> In every inference there are variable ideas with respect to which the deducibility of the conclusion from the premises is stated. … the matter of the inference consist[s] precisely in these variable ideas, while the form consists in what is common to all inferences which differ merely with respect to their matter. (*TS*, §254 [II.516–7])

Limiting our interpretations of arguments to the inferential forms afforded by formal languages in which there are only logical constants thus precludes us from representing the forms of many arguments, in much the same way that the design of the IBM 360 ruled out file names with more than eight characters (cf. van Benthem 2013)[^benthem-2013].

As with analyticity, deducibility can obtain for all sorts of reasons, necessary or contingent, logical or non-logical, known or unknown. [Not all birds fly], for instance, is deducible from [Some birds don’t fly] with respect to [birds] and [fly], and [Buddy is a bird] is deducible from [Buddy is a crow] with respect to [Buddy], while [Harry Truman wasn’t a Buddhist] is also deducible from [Harry Truman was a 20th-century US president] with respect to [Harry Truman]. The last example shows that deducibility does not require that the connection between premises and conclusion be necessary, nor that it be knowable *a priori* (though, unsurprisingly, Bolzano held that there are cases of deducibility that are necessary, some of which are also knowable *a priori*). There is thus a clean isolation of truth-preservation as a phenomenon of intrinsic logical interest.

In some cases, a deduction contains idle elements. For example, in an argument of the form ‘All $A$ are $C$, All $B$ are $C$, All $C$ are $D$, therefore All $A$ are $D$’, the second premise can be omitted without destroying the relation of deducibility. Similarly in an argument of the form ‘Anything that is either $A$ or $B$ is $C$, All $C$ are $D$, therefore All $A$ are $D$’, we could get by with a simpler premise of the form ‘Anything that is $A$ is $C$’ instead of the first premise. Seeing this, Bolzano sought a narrower notion that would filter out redundant or trivial inferences.

In *TS*, § 155, no. 26, he introduces the concept of *exact deducibility*: $M$ is exactly deducible from $A, B, C, \ldots$, we read there, just in case $M$ is deducible from $A, B, C, \ldots$ but no relation of deducibility holds if any of the premises, or any of their parts, is omitted. A deduction that is not exact is called *redundant*. In the shorter version of his logic (Bolzano 2004a: 54), the stipulation about omitting parts is dropped. This was probably wise, as the additional condition seems to have some unwelcome consequences (cf. Rusnock and Šebestík 2019, 312–3)[^rusnock-2019].

Bolzano proves some significant theorems about the narrower relation: If $M$ is exactly deducible from $A, B, C, \ldots$, then none $A, B, C, \ldots, M$ is universally valid or universally invalid with respect to the variables of the deduction. Furthermore, the negation of each premise is compatible with the remaining premises. Hence, since compatibility is required for deducibility, each premise is independent of the others with respect to the variables of the deduction. In addition, it follows from a result proved by Rolf George that when a relation of exact deducibility holds, at least one of the variables must occur both within the premises and within the conclusion (George 1983; cf. Rusnock and Šebestík 2019, 314–5)[^george-1983][^rusnock-2019]. Exact deducibility thus satisfies a condition of relevance (Stelzner 2002)[^stelzner-2002].

Another special case of deducibility is *logical* deducibility; it holds when all the invariable elements in a deduction are logical concepts (*TS*, § 223). There are obvious parallels between this notion and Tarski’s notion of logical consequence. More intriguing, perhaps, are the similarities between Bolzano’s logical deducibility and a relation described by Frege in the course of his dispute with Hilbert and Korselt (Frege 1906, 426ff), which are so striking that Göran Sundholm suggested that Frege may have profited from an unacknowledged acquaintance with Bolzano’s logic (Sundholm 2000; but cf. Künne 2008, 330ff.)[^künne-2008][^sundholm-2000]. Another plausible explanation is that Frege simply reverse-engineered something quite like Bolzanian logical deducibility by making the logical methodology of Hilbert’s *Foundations of Geometry* explicit.

Bolzano’s characterization of logical deducibility is substitutional, an approach examined only to be rejected by Tarski because it was liable to produce unsatisfactory results in cases where “the language we are dealing with does not possess a sufficient stock of extra-logical constants” (Tarski 1936 [1983]: 415)[^tarski-1936]. Bolzano did not face exactly the same problem, because his logic deals with ideas in themselves and not with linguistic expressions. The structural problem underlying Tarski’s criticism also did not occur to him because he assumed that for every object there is an idea in itself that represents it exclusively, a thesis that is not consistently tenable with his other free-wheeling ontological assumptions (the difficulties are discussed in detail by Simons (1987: 42)[^simons-1987] and Siebel (1996: 216–223)[^siebel-1996]). Tarski, who did not make Bolzano’s assumption with respect to languages, stated his definitive formulation in terms of models, or the satisfaction of sentential functions by sequences of objects.

## 7. The objective connection among truths: grounding (*Abfolge*)

The *Contributions* of 1810 already contain speculation about an “objective connection among truths” that is supposed to guide the organization and presentation of scientific knowledge. Bolzano’s discussion of this notion in the *TS* represents the last stage of his development of formal logic and is at the same time the first modern study of axiomatic systems (§162, 168 198–222, 378; see also Bolzano 2004a, §13, 14, 17, and the other Bolzanian texts translated in Roski and Schnieder 2022)[^roski-2022] .

Bolzano’s idea of an objective order among truths has its origin in the Aristotelian distinction between proofs of the *fact* and those that yield the *reason* of the fact. His problem is that of determining what should count as a proof of the second kind, the sort that he calls an *objective grounding* of a truth. Preliminary to this inquiry is one in which he tries to characterize the individual steps of such proofs in terms of the relation of *ground to consequence*, which he calls *Abfolge* (also translated as ‘grounding’).

Finding no satisfactory definition of grounding in the works of others and declaring himself unable to define the concept of grounding (or rather of a ground), he says that he is inclined to regard it as simple (§202). In accordance with his methodology, he tries to at least partially characterize the notion by stating a number of theses about it that he considers to be true. To begin with, he claims that only true propositions stand in the relation of ground to consequence. Perhaps unwisely, he assumes uniqueness: “there is only one objective ground [for a given truth]” (*TS* IV: §528; cf. §206). In many cases, the ground consists of a collection of truths. The parts (members) of this collection are called partial grounds, the collection the complete or total ground. Similarly, Bolzano distinguishes between the total and merely partial consequences of a given ground. In modern terms, we would take the relation he describes to be one that holds between two sets, an option not open to Bolzano because, on his understanding, a collection must contain at least two parts.

Grounding is anti-transitive: If *Γ* is the ground of $\Delta$ and $\Delta$ in turn the ground of $E$, then *Γ* is not the ground of $E$, though we can speak of *supporting truths* or, improperly, of *remote grounds* in such cases. Grounding is also anti-symmetrical and anti-reflexive. It should not be confused with either deducibility or causality. Not with the former because deducibility holds among false as well as true propositions, is reflexive (for propositions that are not universally invalid wrt to the variables of deduction), merely asymmetrical, and merely intransitive (being transitive, notably, in cases where the variables are the same). Nor with the latter, because the causal relation holds between actual objects, while grounding relates non-actual objects, namely, true propositions in themselves. Causality and grounding are nonetheless connected, Bolzano thinks, taking claims of the form ‘A causes B’ to be analyzable as follows: ‘[A exists] (partially) grounds [B exists]’ (*TS*, §168).

Although grounding is not a species of deducibility, Bolzano thinks that there are cases in which a truth is both deducible from, and grounded in, other truths. In some cases of this kind, he thinks, a relation of ground to consequence also holds among the variants of the original propositions, provided only that the resulting propositions are all true. He speaks of *formal grounding* in such cases (*TS*,§162). Later, he cites the following example: [Socrates was an Athenian and a philosopher] is both grounded in and deducible from [Socrates was an Athenian] and [Socrates was a philosopher] (wrt [Socrates], [Athenian], and [philosopher]), and the same holds, he clearly thinks, for all variants consisting of true propositions, e.g., [Nixon was a Republican and a crook], [Nixon was a Republican], [Nixon was a crook] (*TS*, §199; cf. §221, no.7; and, for another example of formal grounding, see §226, no.5).

Bolzano maintains that there are truths that have no grounds, citing the example [There is something]=[[Something] has objectuality] (*TS*, § 214). He calls them *basic truths* (*Grundwahrheiten*). He thinks that there must be more than one basic truth, “for I cannot understand how from a single truth all others would follow either as consequences, or consequences of consequences, etc.” (§215). As in the *Contributions*, Bolzano emphasizes that this is not an epistemic notion: in particular, basic truths need not be evident, and may require proof in the sense of a certification.

Associated with each non-basic truth is a structured collection of supporting truths (grounds, grounds of grounds, and so on). Bolzano depicts such collections as trees (*TS*, §220). In some cases, dependence relations proceed *ad infinitum* , e.g., the grounds of a truth describing a contingent state of a created substance (*TS*, §216). In others, the branches terminate in basic truths.

Bolzano’s discussion in Volume 2 of *TS* ends with a few conjectures bearing especially on formal grounding relations among purely conceptual truths like those of mathematics (*TS*, §221). To begin with, he maintains that the grounds of non-basic purely conceptual truths always lie in other purely conceptual truths. When the consequence is deducible from the ground, there are no redundant premises (a condition satisfied, as we saw above, in cases of exact deducibility). In addition, the individual truths supporting a purely conceptual truth are never more complex than it is. Each is, moreover, the simplest among all propositions equivalent to it. (Bolzano uses these claims to argue that the grounding trees for purely conceptual truths are always finite.) They are also the most general propositions from which the truth can be deduced.

Combining these criteria, he proposed the following as a sufficient condition for formal grounding: If the truth $M$ is exactly deducible from truths $A, B, C, \ldots$ with respect to $i, j, \ldots$, and $A, B, C, \ldots$ are the simplest of all propositions equivalent to them (presumably again wrt $i, j, \ldots$), and if none of $A, B, C, \ldots$ is more complex than $M$, then a relation of formal grounding holds between $A, B, C, \ldots$ and $M$ (§221, no.7).

When these conditions are met systematically in the ordering of truths belonging to a purely conceptual science, he conjectures further, deductive efficiency is also maximized (§221, no. 3). Indeed, at the end of §221, he entertains the thought that grounding might be defined in terms of deductive efficiency:

> I occasionally doubt whether the concept of ground and consequence, which I have above claimed to be simple, is not complex after all; it may turn out to be none other than the concept of an ordering of truths which allows us to deduce from the smallest number of simple premises the largest possible number of the remaining truths as conclusions. (*TS*, §221, 388 note)

Roski (2014: 370)[^roski-2014][^roski-2014-2] sums up the general tendency of Bolzano’s reflections as follows:

> [They are] partial answers to the question under what conditions a deductive argument is explanatory […] On what I took to be the most charitable reading of them, Bolzano’s principles essentially boil down to the claim that a logically valid argument is explanatory, *only if* there is no argument with fewer premises, for none of the premises is there a logically equivalent proposition that is simpler, and none of the premises is more complex than the conclusion.[…] These principles, I have maintained, can be considered to be an explication of the idea that every premise and every concept in an explanatory argument is deductively relevant. More importantly, they can be considered to be an explication of the idea that explanation ought to go in hand with some kind of theoretical economy.

Commentators have drawn attention to a number of shortcomings of Bolzano’s proposals (see, e.g., Mancosu 1999, Rumberg 2013, Roski 2017)[^mancosu-1999][^roski-2017][^rumberg-2013][^roski-2017-2]. This would not have surprised him, since he was himself aware that the above criteria could generate conflicts (see, e.g., 2004a, §17), and had frankly admitted that his remarks about grounding were tentative and incomplete, merely a first attempt to circumscribe the concept:

> Almost everything I advance in this part is tinged with uncertainty, on many topics I have not reached any decision, and at best my inquiries are only fragments and suggestions which will have attained their goal if they provide others with the stimulus to reflect further on these matters. (*TS* II: §195, 327–8)

## 8. Conclusion

Bolzano’s *TS*, especially the Theory of Elements, is a turning point not only in logic, but also in epistemology. According to Cavaillès (2008: 35)[^cavaillès-2008],

> for the first time perhaps, science is not considered as only mediating between the human mind and being in itself, dependent on both and having no proper reality, but as an object *sui generis*, original in its essence, autonomous in its movement.

Science is defined by its structure “which not only is demonstration, but which merges together with demonstration” (*ibid.*, 39). Stressing the fundamental role of demonstrations in scientific knowledge, Bolzano presented a viable alternative to Kant’s philosophy of mathematics based on constructions in pure intuition.

> A truly scientific proof should *ground* the theorem, i.e., integrate it into a scientific theory organised according to the “objective connection of truths”, starting with axioms and fundamental concepts.[…]. These ideas indicate the direction of future research: the notion of normal proofs in the sense of Gentzen, proof trees, König’s lemma (Šebestík 1992: 478).

While at least some of Bolzano’s mathematical work was influential during the nineteenth century, his logic met mostly with indifference and incomprehension. It was only towards the end of the century that philosophers, notably Kerry, Twardowski, Meinong, and Husserl, began to appreciate his achievements. Curiously, Frege, whose ideas were often so close to those of Bolzano and who in his time was one of the few logicians capable of understanding him, never mentions him in any of his publications or surviving papers. He was confronted with Bolzano’s ideas at least three times: in one of Kerry’s articles, in correspondence with Husserl, and later in the controversy with Korselt. We know of no evidence that he ever reacted to their allusions, and it is quite possible that he never laid hands on any of Bolzano’s works. Another interesting coincidence was noted by Mancosu (1996, 110–117 and note 69, p. 234): in §530 of *TS*, Bolzano argues that every indirect proof can be transformed into a direct proof. Mancosu points out the striking similarity of this claim with one to the same effect presented by Frege in one of his posthumous writings (“Logic in Mathematics”). In addition, Bolzano and Frege chose the very same example (Euclid I.19) to illustrate their claims.

After Twardowski (1894)[^twardowski-1894], it was chiefly Husserl who drew philosophers’ attention to Bolzano with his memorable words about *TS* (1900 [1970], I: 222),

> a work which, in its treatment of the logical ‘theory of elements’, far surpasses everything that the world-literature has to offer in the way of a systematic sketch of logic. Bolzano did not, of course, expressly discuss or support any independent demarcation of pure logic in our sense, but he provided one *de facto* in the first two volumes of his work, in his discussion of what underlay a *Wissenschaftslehre* or theory of science in the sense of his conception; he did so with such purity and scientific strictness, and with such a rich store of original, scientifically confirmed and ever fruitful thoughts, that we must count him as one of the greatest logicians of all time.

Nevertheless, he always insisted on the originality of his own phenomenological method. Between the two wars, Bolzano’s logic and philosophy of mathematics inspired Heinrich Scholz and Jean Cavaillès. Also during this period, Tarski discovered the concept of logical consequence independently of Bolzano, only becoming aware of the affinity between his work and Bolzano’s after Scholz (1937 [1961]) pointed it out. However, already in Twardowski (1894)[^twardowski-1894], the founder of the Polish Lvov-Warsaw school, Bolzano’s ideas were discussed and criticized at length, and some of them might have become common lore in the Polish school. In 1920, Hans Hahn edited the *Paradoxes of the infinite* with important critical notes, comparing Bolzano with Cantor. Karl Menger might have taken inspiration for his theory of dimension not only from Poincaré, but also from the *Paradoxes*. Neurath praised Bolzano as one of the ancestors of the Vienna Circle, because of the conciseness of his style and the rejection of Kant’s philosophy. Some important Bolzanian ideas are also found in the work of Quine. All these currents are indebted to Bolzano for the lesson of intellectual rigour and of analytic power. It is Bolzano who is the true founder of the kind of analytical philosophy whose core is logic and which is impregnated with science. His logic has archaic aspects, but he introduced not only new concepts, methods and theories, new themes and new problems, but above all a new spirit that has animated philosophy ever since.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

### Primary Literature

### Secondary Literature

#### Works Cited

#### Collections

#### Other Works on Bolzano

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=bolzano-logic). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/bolzano-logic/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=bolzano-logic&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/bolzano-logic/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- O’Connor, J.J. and E.F. Robertson, “[Bernard Bolzano](https://mathshistory.st-andrews.ac.uk/Biographies/Bolzano/)”, MacTutor History of Mathematics archive.
- [Bernard Bolzano and the Theory of Science](http://www.formalontology.it/bolzanob.htm)

## Related Entries

Bolzano, Bernard | Husserl, Edmund | Tarski, Alfred

[^bolzano-logic-1810]: 1810, *Beyträge zu einer begründeteren Darstellung der Mathematik* (*Contributions to a better grounded presentation of mathematics*), Prague (English transl. Bolzano 2004b; French transl. Bolzano 2010).

[^bolzano-logic-1816]: 1816, *Der binomische Lehrsatz und als Folgerung aus ihm der polynomische, und die Reihen, die zur Berechnung der Logarithmen und Exponentialgrössen dienen, genauer als bisher erwiesen* (The binomial theorem and as a consequence of it the polynomial theorem, and the series that serve in the calculation of logarithms and exponential quantities, proven more exactly than previously) Prague, English transl. Bolzano 2004b).

[^bolzano-logic-1817]: 1817, *Rein analytischer Beweiss des Lehrsatzes, daß zwischen je zwey Werthen, die ein engegengesetztes Resultat gewähren, wenigstens eine reelle Wurzel der Gleichung liege (Purely analytic proof of the theorem that between any two values which give results of opposite sign, there lies at least one real root of the equation)*, Prague (English transl. Bolzano 2004b; French transl. Bolzano 2010).

[^bolzano-logic-1834]: 1834, *Lehrbuch der Religionswissenschaft* (*Treatise of the science of religion*), Sulzbach: Seidel; *Gesamtausgabe* I, 6–8.

[^bolzano-logic-1837]: 1837 [*TS*], *Wissenschaftslehre, Versuch einer ausführlichen und grösstentheils neuen Darstellung der Logik mit steter Rücksicht auf deren bisherige Bearbeiter*, 4 vol., Sulzbach: Seidel; reprint of the 2nd edition 1929–1931, Aalen: Scientia Verlag 1970; *Gesamtausgabe* I, 11–14, with introductions by J. Berg; English translation 2014, *Theory of science*, 4 vol., translated by Paul Rusnock and Rolf George, Oxford: Oxford University Press. (This translation is indicated as *TS*. The page numbers are those of the original German edition which are on the margins of the other editions, so that the reference is the same for the German original, for the *Gesamtausgabe* and for the English translation).

[^vol-nd]: Vol. I: §§1–120

[^vol-nd-2]: Vol. II: §§121–268

[^vol-nd-3]: Vol. III: §§269–391

[^vol-nd-4]: Vol. IV: §§391–718.

[^bolzano-logic-1841]: 1841, *Wissenschaftslehre und Religionswissenschaft in einer beurtheilenden Uebersicht*, Sulzbach: Seidel; *Gesamtausgabe*, I, 17.

[^bolzano-logic-1842]: 1842, *Über die Zusammensetzung der Kräfte*, Prag; *Gesamtausgabe* I, 18, 9–60.

[^bolzano-logic-1851]: 1851, *Paradoxien des Unendlichen* (*Paradoxes of the Infinite*), Leipzig; new editions: 1920 with notes by H. Hahn; 1975, Hamburg: F. Meiner, with notes by B. van Rootselaar; 2012, Hamburg: Meiner, C. Tapp (ed.), D.A. Steele (trans.), 1950, London: Routledge; new transl. S. Russ, Bolzano 2004b; French transl. Paris: Seuil 1993).

[^bolzano-logic-1932]: 1932, *Von dem besten Staate* (On the Best State), edited with an introduction by A. Kowalewski, Prag: Königliche böhmische Gesellschaft der Wissenschaften; *Gesamtausgabe* II A 14; Engl. transl. by P. Rusnock and R. George, in *Selected Writings on Ethics and Politics*, 2007, Amsterdam: Rodopi, pp. 231–359.

[^bolzano-logic-1969]: 1969–present, *Bernard-Bolzano Gesamtausgabe* (complete works), Stuttgart-Bad Cannstatt: Fromann-Holzboog, editors E. Winter, J. Berg., et al., altogether 132 volumes of which 107 have appeared.

[^bolzano-logic-1972]: 1972, *Theory of science, attempt at a detailed and in the main novel exposition of logic with constant attention to earlier authors*, edited and translated by Rolf George, Berkeley and Los Angeles: University of California Press (a selection).

[^bolzano-logic-1973]: 1973, *Theory of science*, edited, with an introduction, by Jan Berg, translated from the German by Burnham Terrell, Dordrecht and Boston: D. Reidel (a selection).

[^bolzano-logic-1976]: 1976, *Einleitung in die Grössenlehre* und *Erste Begriffe der allgemeinen Grössenlehre (Introduction to the Theory of Magnitudes and First concepts of the general Theory of Magnitudes, Gesamtausgabe)*, II A 7, (English translation of the chapter, *On the mathematical method*, 2004, Paul Rusnock and Rolf George, Amsterdam-New York: Rodopi; French translation, Paris: Vrin, 2008; see 2004a).

[^bolzano-logic-1978]: 1978, *Grundlegung der Logik. Wissenschaftslehre I/II*, edited, with an introduction by Friedrich Kambartel, Hamburg: Felix Meiner (a selection; French transl. 2011, Paris: Gallimard).

[^bolzano-logic-2004a]: 2004a, *On the mathematical method and correspondence with Exner*, Paul Rusnock and Rolf George (transl.), Amsterdam-New York: Rodopi; French transl. *De la méthode mathématique et correspondance avec Exner*, 2008, introd. par C. Maigné et J. Šebestík, Paris: Vrin.

[^bolzano-logic-2004b]: 2004b, *The mathematical works of Bernard Bolzano*, S. Russ (transl.), Oxford: Oxford University Press.

[^bolzano-logic-2010]: 2010, *Premiers écrits, Philosophie, logique, mathématique*, trad. fr. par M. Bartzel et al., introd. par C. Maigné et J. Šebestík, Paris: Vrin.

[^arnauld-1662]: Arnauld, A. and P. Nicole, 1662, *Logique ou l’Art de Penser* (also called *Logique de Port-Royal* and *Port-Royal Logic*); reprinted Paris: Vrin, 1993.

[^bar-hillel-1950]: Bar-Hillel, Y., 1950, “Bolzano’s definition of analytic propositions,” *Theoria*, 16(2): 91–117.

[^benthem-2013]: van Benthem, Johan, 2013, “Bernard Bolzano’s *Wissenchaftslehre*,” *Topoi*, 32(2): 301–303.

[^cavaillès-2008]: Cavaillès, J., 2008, *Sur la logique et la théorie de la science*, second edition, preface by G. Canguilhem and G. Bachelard, postface by J. Šebestík, Paris: Vrin.

[^frege-1979]: Frege, G., unpublished, “Logic in Mathematics,” translation by P. Long and R. White, in H. Hermes, F. Kambartel, and F. Kaulbach (eds.), 1979, *Posthumous Writings*, Chicago: U. of Chicago Press, pp. 203–250.

[^george-1983]: George, R., 1983, “Bolzano’s consequence, relevance, and enthymemes,” *Journal of Philosophical Logic*, 12(3): 299–318 ; with a postscript on fallacies: 319–25.

[^husserl-1900]: Husserl, E., 1900, *Logische Untersuchungen, I, Prolegomena zu reiner Logik* (*Logical Investigations*, I, *Prolegomena to pure logic*; Engl. transl. J.N. Findlay, 1970, London: Routledge).

[^kreiser-1981]: Kreiser, L., 1981, “Logical semantics in Bolzano and the reproach of Platonism” (in Czech), *Filozofický časopis*, 29: 94–103.

[^künne-2006]: Künne, W., 2006, “Analyticity and logical truth: from Bolzano to Quine,” in M. Textor (ed.), *The Austrian Contribution to Analytic Philosophy*, London and New York: Routledge: 184–249.

[^künne-2008]: –––, 2008, *Versuche über Bolzano. Essays on Bolzano*, Sankt Augustin: Akademia.

[^maaß-1793]: Maaß, J.G.E., 1793, *Grundriß der Logik*, 4ᵗʰ edition, Leipzig, 1823.

[^mancosu-1996]: Mancosu, P., 1996, *Philosophy of Mathematics and Mathematical Practice in the Seventeenth Century*, Oxford: Oxford University Press.

[^mancosu-1999]: –––, 1999, “Bolzano and Cournot on mathematical explanation,” in Sinaceur 1999: 429–455.

[^quine-1960]: Quine, W.V.O, 1960, *Word and Object*, Cambridge: MIT Press.

[^roski-2014]: Roski, S., 2014, *Bolzano’s Notion of Grounding and the Classical Model of Science*, Amsterdam: CPI Wöhrmann Print Service BV.

[^roski-2017]: –––, 2017, *Bolzano’s Conception of Grounding*, Frankfurt am Main: Klostermann.

[^roski-2022]: Roski, S. and B. Schnieder (eds.), 2022, *Bolzano’s Philosophy of Grounding: Translations and Studies*, Oxford: Oxford University Press.

[^rumberg-2013]: Rumberg, A., 2013, “Bolzano’s concept of grounding (*Abfolge*) against the background of normal proofs,” *Review of Symbolic Logic*, 6(3): 424–459.

[^rusnock-2019]: Rusnock, P. and J. Šebestík, 2019, *Bernard Bolzano: His Life and Work*, Oxford: Oxford University Press.

[^scholz-1961]: Scholz, H., 1961, “Die Wissenschaftslehre Bolzanos: Eine Jahrhundert-Betrachtung (1937),” in *Mathesis Universalis*, Basel-Stuttgart: Benno Schwabe.

[^ík-1992]: Šebestík, J., 1992, *Logique et mathématique chez Bernard Bolzano*, Paris: Vrin.

[^siebel-1996]: Siebel, M., 1996, *Der Begriff der Ableitbarkeit bei Bolzano*, Sankt Augustin: Akademia.

[^simons-1987]: Simons, P., 1987, “Bolzano, Tarski, and the limits of logic,” in Morscher 1987: 378–405.

[^stelzner-2002]: Stelzner, W., 2002, “Compatibility and relevance: Bolzano and Orlov,” in *The Third German-Polish Workshop on Logic & Logical Philosophy*, Dresden, 2001, *Logic and Logical Philosophy*, 10: 137–171.

[^sundholm-2000]: Sundholm, G., 2000, “When and why, did Frege read Bolzano?,” *LOGICA Yearbook 1999*, Prague: Filosofia, pp. 164–174.

[^tarski-1936]: Tarski, A., 1936 [1983], “Über den Begriff der logischen Folgerung,” in *Actes du Congrès International de Philosophie Scientifique*, fasc. 7 (Actualités Scientifiques et Industrielles, vol. 394), Paris: Hermann et Cie, pp. 1–11; English translation by J.H. Woodger in *Logic, Semantics, Metamathematics*, second edition, J. Corcoran (ed.), Indianapolis: Hackett, 1983, pp. 409–420.

[^twardowski-1894]: Twardowski, K., 1894, *Zur Lehre von Inhalt und Gegenstand von Vorstellungen*, Wien; Engl. transl. and introd. by R. Grossmann, 1977, *On the content and object of presentations*, The Hague: Martinus Nijhoff.

[^wittgenstein-1922]: Wittgenstein, L., 1922, *Tractatus Logico-Philosophicus*, transl. C. K. Ogden, London: Routledge and Kegan Paul.

[^zimmermann-1853]: Zimmermann, R., 1853, *Philosophische Propädeutik für Obergymnasien*, 1ˢᵗ ed., Wien.

[^benoist-2000]: Benoist, J. (ed.), 2000, *Bolzano*, *Les Études philosophiques* (special issue), n° 4 (Octobre-Décembre), 433–534.

[^besoli-2011]: Besoli, S., L. Guidetti, and V. Raspa (eds.), 2011, *Bernard Bolzano e la tradizione filosofica*, special issue of *Discipline Filosofiche*, 21(2).

[^centro-1992]: Centro Fiorentino di Storia e Filosofia della Scienza (ed.), 1992 [BW-1987], *Bolzano’s Wissenschaftslehre 1837–1987: International Workshop (Firenze, 16–19 settembre 1987)*, Firenze: Leo S. Olschki.

[^künne-1997]: Künne, W., M. Siebel, and M. Textor (eds.), 1997, *Bolzano and Analytic Philosophy*, special issue of *Grazer philosophische Studien*, 53.

[^lapointe-2003]: Lapointe, S. (ed.), 2003, *Bernard Bolzano. Philosophie de la logique et théorie de la connaissance*, special issue of *Philosophiques*, 30(1).

[^morscher-1987]: Morscher, E. (ed.), 1987, *Bolzano-Studien*, special issue of *Philosophia Naturalis*, 24(4).

[^morscher-2000]: ––– (ed.), 2000, *Bolzanos geistiges Erbe für das 21. Jahrhundert*, Sankt Augustin: Akademia.

[^morscher-2003b]: ––– (ed.), 2003b, *Bernard Bolzanos Leistungen in Logik, Mathematik und Physik*, Sankt Augustin: Akademia.

[^novy-1982]: Novy, M. (ed.), 1982, *Impact of Bolzano’s epoch on the development of science* (Volume 13 of *Acta Historiae Rerum Naturalium Necnon Technicarum*), Prague: Ústav Československých a Světových Dějin ČSAV.

[^sinaceur-1999]: Sinaceur, H. (ed.), 1999, *Mathématique et logique chez Bolzano*, special issue of *Revue d’Histoire des Sciences*, 52(3–4).

[^trlifajová-2006]: Trlifajová, K. (ed.), 2006, *The solitary thinker Bernard Bolzano*, in Czech, Prague: Filosofia.

[^bar-hillel-1952]: Bar-Hillel, Y., 1952, “Bolzano’s propositional logic,” *Archiv für Mathematik, Logik und Grundlagenforschung*, 1: 65–98.

[^bayerová-1994]: Bayerová, M., 1994, *Bernard Bolzano, the European dimension of his thought* (in Czech), Prague: Filosofia.

[^behboud-2000]: Behboud, A., 2000, *Bolzanos Beiträge zur Mathematik und ihrer Philosophie* (*Bolzano’s Contributions to Mathematics and its Philosophy*), Bern: Bern Studies in the History and Philosophy of Science.

[^benoist-1999]: Benoist, J., 1999, *L’a priori conceptuel. Bolzano, Husserl, Schlick*, Paris: Vrin.

[^benthem-1984]: Benthem, J. van, 1984, *Lessons from Bolzano*, Stanford: Center for the Study of Language and Information, Leland Stanford Junior University (13 p.).

[^benthem-1985]: –––, 1985, “The variety of consequence, according to Bolzano,” *Studia Logica*, 44(4): 389–403.

[^benthem-2003]: –––, 2003, “Is there still logic in Bolzano’s key?,” in Morscher 2003b: 11–34.

[^berg-1962]: Berg, J., 1962, *Bolzano’s Logic*, Stockholm: Almquist Wiksell.

[^berg-1973]: –––, 1973, “Editor’s introduction,” in Bolzano 1973: 1–30.

[^berg-1977]: –––, 1977, “Bolzano’s contribution to logic and philosophy of mathematics,” in *Logic Colloquium 76*, R.O. Gandy and J.M. Hyland (eds), Amsterdam: North Holland, 141–171.

[^berg-1987a]: –––, 1987a, “Bolzano and situation semantics: variations on a theme of variation,” in Morscher 1987: 373–377.

[^berg-1987b]: –––, 1987b, “Bolzano on induction,” in Morscher 1987: 442–446.

[^berg-1992]: –––, 1992, *Ontology without ultrafilters and possible worlds: An examination of Bolzano’s ontology*, Sankt Augustin: Akademia.

[^bergmann-1970]: Bergmann, H., 1970, *Das philosophische Werk Bernard Bolzanos*, reprint Hildesheim: Olms.

[^berka-1992]: Berka, K., 1992, “Bolzanos Lehre vom natürlichen Schliessen,” in BW-1987: 141–161.

[^berg-1987]: Berg, J., H. Ganthaler, and E. Morscher, 1987, “Bolzanos Biographie in tabellarischer Übersicht,” in Morscher 1987: 353–372.

[^betti-1998]: Betti, A., 1998, “*De Veritate*: another chapter. The Bolzano-Lesniewski connection,” in *The Lvov-Warsaw School and contemporary philosophy*, K. Kijania-Placek and J. Wolenski (eds), Dordrecht: Kluwer Academic Publishers, pp. 115–137.

[^bouveresse-2000]: Bouveresse, J., 2000, “Sur les représentations sans objet,” J. Benoist (ed.), *Les Études Philosophiques*, n° 4: 519–534.

[^buhl-1961]: Buhl, G., 1961, *Ableitbarkeit und Abfolge in der Wissenschaftslehre Bolzanos*, *Kantstudien*, Ergänzungshefte n° 83.

[^bussotti-2000]: Bussotti, P., 2000, “The problem of the foundations of mathematics at the beginning of the nineteenth century: Two lines of thought: Bolzano and Gauss” (Italian), *Teoria* (New Series), 20(1): 83–95.

[^cantù-1992]: Cantù, P., 1992, “Bolzano versus Kant: Mathematics as a Scientia Universalis,” in *Mind, Values, and Metaphysics, Philosophical Essays in Honor of Kevin Mulligan*, Volume 1, A. Reboul (ed.), Heidelberg, Springer, pp. 295–316.

[^casari-1985]: Casari, E., 1985, “L’universo logico bolzaniano,” *Rivista di filosofia*, 76:339–366.

[^casari-1992]: –––, 1992, “An interpretation of some ontological and semantical notions in Bolzano’s logic,” in BW-1987: 55–105.

[^casari-2016]: –––, 2016, *Bolzano’s Logical System*, Oxford: Oxford University Press.

[^cellucci-1992]: Cellucci, C., 1992, “Bolzano and multiple-conclusion logic,” in BW-1987: 179–189.

[^centrone-2011]: Centrone, S., 2011, “Begründungen bei Bolzano und beim frühen Husserl,” *Zeitschrift für philosophische Forschung*, 65: 5–27.

[^centrone-2015]: Centrone S., 2015, *Studien zu Bolzano*, Sankt Augustin: Akademia Verlag.

[^chihara-1999]: Chihara, C., 1999, “Frege’s and Bolzano’s rationalist conceptions of arithmetic,” in Sinaceur 1999: 343–361.

[^claas-2023]: Claas, J., 2023, “How to distinguish simple objectless ideas,” *History and Philosophy of Logic*, 44(4): 422–441.

[^coffa-1982]: Coffa, A., 1982, “Kant, Bolzano and the emergence of logicism,” *Journal of Philosophy*, 74: 679–689.

[^coffa-1991]: –––, 1991, *The Semantic Tradition from Kant to Carnap*, Cambridge: Cambridge University Press.

[^cohen-1982]: Cohen, J.L., 1982, “Bolzano’s theory of induction,” in L. Nový (ed.) *Impact of Bolzano’s epoch on the development of science*, Prague: Institute of Czechoslovak and General History, 443–457.

[^daněk-1975]: Daněk, J., 1975, *Les projets de Leibniz et de Bolzano: deux sources de logique contemporaine*, Quebec: Presses de l’Université de Laval.

[^detlefsen-1988]: Detlefsen, M., 1988, “Fregean hierarchies and mathematical explanation,” *International Studies in Philosophy of Science*, 3: 97–116.

[^detlefsen-2010]: –––, 2010, “Rigor, Re-proof and Bolzano’s critical program,” in *Constructions*, P. Bour et al. (eds.), Festschrift for Gerhard Heinzmann, pp. 171–184, King’s College Publications.

[^dorn-1987]: Dorn, G.J.W., 1987, “Zu Bolzanos Wahrscheinlichkeitslehre,” in Morscher 1987: 452–468.

[^dorn-2003]: –––, 2003, “Intuitions” (in French), in S. Lapointe (ed.) 2003, *Philosophiques*, 30(1): 19–46.

[^fedorov-1980]: Fedorov, B.I., 1980, *Bernard Bolzano’s Logic* (in Russian), Leningrad: Izdatelstvo Leningradskogo Universiteta.

[^fuentes-2023]: Fuentes Guillén, E., 2023, “Bolzano on Bolzano: A hitherto unknown announcement of Bolzano’s ‘Beyträge’,” *History and Philosophy of Logic*, 44(4): 442–458.

[^genco-2021]: Genco, A., Poggiolesi, F., and Rossi, L., 2021, “Grounding, Quantifiers, and Paradoxes,” *Journal of Philosophical Logic*, 50(6): 1417–1448.

[^george-1986]: George, Rolf, 1986, “Bolzano’s concept of consequence,” *Journal of Philosophy*, 83: 558–64.

[^george-2004]: –––, 2004, “Intuitions—the theories of Kant and Bolzano,” in M. Siebel and M. Textor (eds.), *Semantik und Ontologie*, Frankfurt and Lancaster: Ontos: 319–54.

[^hafner-1999]: Hafner, J., 1999, “Bolzano’s criticism of indirect proofs,” in Sinaceur 1999: 385–398.

[^hale-2015]: Hale, B., 2015, “Bolzano’s definition of analytic propositions,” *Grazer philosophische Studien* 91:325–364.

[^haller-1992]: Haller, R., 1992, “Bolzano and Austrian Philosophy,” in BW-1987: 191–206.

[^husserl-1969]: Husserl, E., 1969, *Formal and Transcendental logic*, transl. D. Cairns, The Hague: Nijhoff.

[^jong-2001]: de Jong, W., 2001, “Bernard Bolzano, analyticity and the aristotelian model of science,” *Kant-Studien*, 92: 328–49.

[^jong-2010]: –––, 2010, “The analytic-synthetic distinction and the classical model of science: Kant, Bolzano and Frege,” *Synthese*, 174: 237–61.

[^kappes-2024]: Kappes, Y., 2024, “Bolzano’s tortoise and a loophole for Achilles,” *Synthese*, 203(93). doi:10.1007/s11229-024-04515-0

[^kerry-1885]: Kerry, B., 1885–1891, “Über Anschauung und ihre psychische Verarbeitung,” *Vierteljahresschrift für wissenschaftliche Philosophie*, 1885, 9: 432–493; 1886, 10: 419–467; 1887, 11: 53–116 and 249–307; 1891, 15: 127–167.

[^kitcher-1975]: Kitcher, K., 1975, “Bolzano’s ideal of algebraic analysis,” *Studies in History and Philosophy of Science*, 6(3): 229–269.

[^kolman-1961]: Kolman, A., 1961, *Bernard Bolzano*, Berlin: Akademie Verlag.

[^kozelmann-2010]: Kozelmann Ziv, A., 2010, *Kräfte, Wahrscheinlichkeit und “Zuversicht”, Bernard Bolzanos Erkenntnislehre*, Sankt Augustin: Akademia Verlag.

[^koreň-2014]: Koreň, L., 2014, “Quantificational account of logical consequence,” II: In the Footsteps of Bolzano, *Organon*, Bratislava, 3(21), 303–326.

[^krause-2004]: Krause, A., 2004, *Bolzanos Metaphysik*, Freiburg/München: Verlag Karl Alber.

[^krickel-1995]: Krickel, F., 1995, *Teil und Inbegriff. Bernard Bolzanos Mereologie*, Sankt Augustin: Akademia.

[^künne-1998]: Künne, W., 1998, “Bernard Bolzano,” in *Routledge Encyclopedia of Philosophy*, 1, London, New York: Routledge, pp. 824–828.

[^lapointe-2000]: Lapointe, S., 2000, “Analyticité, universalité et quantification chez Bolzano,” in *Les Études Philosophiques*, 4: 455–470.

[^lapointe-2008]: –––, 2008, *Qu’est-ce que l’analyse?*, Paris: Vrin.

[^lapointe-2014]: –––, 2014, “Bolzano, Quine, and Logical Truth,” in G. Harman and E. Lepore (eds.) *A Companion to W.V.O. Quine*, Hoboken: Wiley: 296–312.

[^laz-1993]: Laz, J., 1993, *Bolzano critique de Kant*, Paris: Vrin.

[^bolzano-logic-1970]: Łukasiewicz, J., 1970, *The logical foundations of probability calculus*, in *Selected Works*, Amsterdam: North Holland.

[^mačák-1996]: Mačák, K., 1996, “Bernard Bolzano and the calculus of probabilities,” (in Czech), in *Mathematics in the 19th century*, Prague: Prometheus, pp. 39–55.

[^materna-1995]: Materna, P., 1995, *The World of Concepts and Logic* (in Czech), Prague: Filosofia.

[^morscher-1973]: Morscher, E., 1973, *Das logische An-Sich bei Bernard Bolzano*, Salzburg-München: Anton Pustat.

[^morscher-1997]: –––, 1997, “Bolzano’s Method of Variation: Three Puzzles,” W. Künne, et al. (eds.), *Grazer philosophische Studien*, 53: 151–159.

[^morscher-2003a]: –––, 2003a “La définition bolzanienne de l’analyticité logique, ”*Philosophiques*, 30: 149–169.

[^morscher-2007]: –––, 2007, *Studien zur Logik Bernard Bolzanos*, Sankt Augustin: Akademia.

[^mugnai-1992]: Mugnai, M., 1992, “Leibniz and Bolzano on the ‘Realm of truths’,” in BW-1987: 207–220.

[^niiniuloto-1977]: Niiniuloto, I., 1977, “Bolzano and Bayes’ tests,” *Studia Excellentia*, Essays in Honour of Oliva Ketonen, 30–36, Helsinki.

[^nový-1982]: Nový, L., 1982, “Bolzano’s contribution to science and society,” in *Impact of Bolzano’s epoch on the development of science*, Prague: Institute of Czechoslovak and General History, 9–23.

[^patočka-1958]: Patočka, J., 1958, “Bolzanovo místo v dějinách filosofie” (Bolzano’s place in the history of philosophy), *Filosofie v dějinách českého národa*, Praha: Nakl. Československé Akademie Věd, 111–123.

[^prawitz-2019]: Prawitz, D., 2019, “The concepts of proof and ground,” in S.Centrone, S. Negri, D. Sarikaya eds., *Mathesis Universalis: Computability and Proof*, Cham: Springer Cham, 291–309.

[^preti-1976]: Preti, G., 1976, “I fondamenti della logica formale pura nella ‘Wissenschaftslehre’ di B. Bolzano e nelle ‘Logische Unturschungen’ di E. Husserl,” *Saggi filosofici* (vol. I, pp. 11–31), Firenze: La Nuova Italia.

[^prihonsky-1850]: Prihonsky, F., 1850, *Neuer Anti-Kant oder Prüfung der Kritik der reinen Vernunft nach den in Bolzano‘s Wissenschaftslehre niedergelegten Begriffen*, Bautzen; English transl. by S. Lapointe and C. Tolley, 2014, Houndmills: Palgrave and MacMillan.

[^proust-1986]: Proust, J., 1986, *Questions de forme, Logique et proposition analytique de Kant à Carnap*, Paris: Fayard; Engl. transl. *Questions of form, Logic and analytic proposition from Kant to Carnap*, Minneapolis: University of Minnesota Press.

[^proust-1999]: –––, 1999, “Bolzano’s theory of representation,” in Sinaceur 1999: 363–383.

[^rootselaar-1970]: Rootselaar, B. van, 1970–1990, “Bernard Bolzano,” in *Dictionary of Scientific Biography*, New York, II, 273–279.

[^rootselaar-1992]: –––, 1992, “Axiomatics in Bolzanos logico-mathematical research,” in BW-1987: 221–230.

[^rootselaar-2013]: –––, 2013, “*A Priori* Knowledge in Bolzano, Conceptual Truths, and Judgments,” in M. van der Schaar (ed.), *Judgment and the Epistemic Foundation of Logic*, Dordrecht: Springer, 101–130.

[^roski-2017-2]: Roski, S., *Bolzano’s Conception of Grounding*, Frankfurt am Main: Klostermann, 2017.

[^roski-nd]: Roski, S. and A. Rumberg, “Simplicity and Economy in Bolzano’s Theory of Grounding,” *Journal of the History of Philosophy*, 54: 469–96.

[^roski-2014-2]: Roski, S. and P. Rusnock, 2014, “Bolzano on necessary existence,” *Archiv für Geschichte der Philosophie*, 96(3): 320–359. doi:10.1515/agph-2014-0015

[^rumberg-2009]: Rumberg, A., 2009, *Ableitbarkeit und Abfolge bei Bernard Bolzano vor dem Hintergrund des modelltheoretischen und beweistheoretischen Folgerungsbegriff*, Magisterarbeit Universität Tübingen.

[^rusnock-2012]: Rusnock, P., 2012, “Remarks on Bolzano’s conception of necessary truth,” *British Journal for the History of Philosophy*, 20(4): 817–837.

[^rusnock-2013a]: –––, 2013a, “Kant and Bolzano on analyticity,” *Archiv für Geschichte der Philosophie*, 95(3): 298–335.

[^rusnock-2013b]: –––, 2013b, “On Bolzano’s concept of a Sum,” *History and Philosophy of Logic*, 34(2): 155–169.

[^rusnock-2010]: Rusnock, P. and Burke, M., 2010, “Etchemendy and Bolzano on logical consequence,” in *History and Philosophy of Logic*, 31(3): 3–29.

[^rusnock-2004]: Rusnock, P. and R. George, 2004, “Bolzano as logician,” in *Handbook of the History of Logic, vol. 3: The Rise of modern logic: from Leibniz to Frege*, D. Gabbay and J. Woods (eds), Amsterdam: Nort Holland, 177–205.

[^rusnock-2013]: Rusnock, P. and J. Šebestík, 2013, “The *Beyträge* at 200: Bolzano’s quiet revolution in the philosophy of mathematics,” *Journal for the History of Analytic Philosophy*, 1(8).

[^russ-1992]: Russ, S., 1992, “Bolzano’s analytic program,” *The Mathematical Intelligencer*, 14(3): 45–53.

[^russ-1982]: –––, 1982, “Influence of Bolzano’s methodology on the development of his mathematics,” in *Impact of Bolzano’s epoch on the development of science*, Prague, 335–337.

[^schmutz-2009]: Schmutz, J., 2009, “Quand le langage a-t-il cessé d’être mental? Remarques sur les sources scolastiques de Bolzano,” in *Le langage mental du Moyen-Âge à l’Âge classique*, J. Biard (dir.), Louvain: Ed. Peeters, pp. 307–337.

[^schnieder-2002]: Schnieder, B., 2002, *Substanz und Adhärenz. Bolzanos Ontologie des Wirklichen*, Sankt Augustin: Akademia.

[^schwabe-2025]: Schwabe, U., 2025, “Zu Bolzanos Einwand gegen Kants Bestimmung des analytischen Urteils,” *Zeitschrift für philosophische Forschung*, 79(2): 211–227.

[^ík-1999]: Šebestík, J., 1999, “Forme, variation et déductibilité dans la logique de Bolzano,” Sinaceur 1999: 479–506.

[^ík-2018]: –––, 2018, review of E. Casari, *Bolzano’s Logical System*, *History and Philosophy of Logic*, 39(2): 164–186

[^segura-2001]: Segura, L.F., 2001, *La prehistoria del logicismo*, Mexico: Plaza y Valdes.

[^siebel-1997a]: Siebel, M., 1997a, “Variation, derivability, and necessity,” *Grazer philosophische Studien*, 53: 117–37.

[^siebel-1997b]: –––, 1997b, “Bolzanos Ableitbarkeit und Tarskis Logische Folgerung,” pp. 148–56 in G. Meggle, ed., *Analyomen* 2: Proceedings of the 2nd Conference “Perspectives in Analytical Philosophy,” Volume I: Logic, Epistemology, Philosophy of Science New York and Berlin: De Gruyter.

[^siebel-2002]: –––, 2002, “Bolzano’s concept of consequence,” *The Monist*, 85: 580–99.

[^simons-1997]: Simons, P., 1997, “Bolzano on collections,” *Grazer Philosophische Studien*, 53: 87–108.

[^simons-2000]: –––, 2000 “Bolzano über Wahrheit,” pp. 13–28 in Morscher ed., 2000.

[^simons-2011]: –––, 2011, “Bolzano e la logica,” S. Besoli et al. (eds.) 2011: 321–342.

[^sinaceur-1996]: Sinaceur, H., 1996, “Bolzano et les mathématiques,” in *Les philosophes et les mathématiques*, Paris: Ellipses, pp. 150–173.

[^sinaceur-1999-2]: –––, 1999, “Réalisme mathématique, réalisme logique chez Bolzano,” in Sinaceur 1999: 457–477.

[^sundholm-2002]: Sundholm, B.G, 2002, “A Century of Inference: 1837–1936,” in *Logic, Methodology and Philosophy of Science* (11, Cracow 1999), J. Wolenski and K. Placek (eds.), Dordrecht: Kluwer.

[^sundholm-2011]: –––, 2011, “A Garden of Grounding Trees ,” in *Logic and Knowledge*, C. Cellucci, E. Grosholz, and E. Ippoliti, Cambridge: Cambridge Scholars Publishing, pp. 57–74.

[^tatzel-2002]: Tatzel, A., 2002, “Bolzano’s theory of ground and consequence, ” *Notre Dame Journal of Formal Logic*, 43: 1–25.

[^tatzel-2003]: –––, 2003, Bolzano on grounding, in *The Logica Yearbook 2002*, T. Childers and O. Majer (eds.), Prague: Filosofia, 245–258.

[^textor-1996]: Textor, M., 1996, *Bolzanos Propositionalismus*, Berlin-New York: De Gruyter.

[^textor-1997]: –––, 1997, “Bolzano’s Sententialism,” *Grazer philosophische Studien*, 53: 181–202.

[^textor-2000]: –––, 2000, “Bolzano et Husserl sur l’analyticité,” *Études Philosophiques*, 4: 435–54.

[^textor-2003]: –––, 2003, “ ‘Caius–at–noon’. Bolzano on Tense and Persistence,” *History of Philosophy Quarterly*, 20: 81–103.

[^textor-2013]: –––, 2013, “Bolzano on conceptual and intuitive truth: the point and purpose of the distinction,” *Canadian Journal of Philosophy*, 43: 13–36.

[^thompson-1981]: Thompson, P., 1981, “Bolzano’s deducibility and Tarski’s logical consequence,” *History and. Philosophy of Logic*, 2: 11–20.

[^vlasáková-2005]: Vlasáková, M., 2005, *Bernard Bolzano: the road towards logical semantics* (in Czech), Prague: Filosofia.

[^voltaggio-1974]: Voltaggio, F., 1974, *Bernard Bolzano e la dottrina della scienza*, Milano: Edizioni di Comunità.

[^wussing-1981]: Wussing, W., 1981, “Bernard Bolzano und die Grundlegung der Analysis,” *Mitteilungen der Matematischen Gesellschaft der DDR*, 2–4: 128–152.
