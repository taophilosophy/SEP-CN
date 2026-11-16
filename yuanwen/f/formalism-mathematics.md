# Formalism in the Philosophy of Mathematics
**First published Wed Jan 12, 2011; substantive revision Tue Feb 20, 2024**

*Weir, Alan*

One common understanding of formalism in the philosophy of mathematics takes it as holding that mathematics is not a body of propositions representing an abstract sector of reality but is much more akin to a game, bringing with it no more commitment to an ontology of objects or properties than playing ludo or chess are normally thought to have. This idea has some intuitive plausibility: consider the tyro toiling at multiplication tables or the student using a standard algorithm for differentiating or integrating a function. It also corresponds to some aspects of the practice of advanced mathematicians in some periods—for example, the treatment of imaginary numbers for some time after Bombelli’s introduction of them, and perhaps the attitude of some contemporary mathematicians towards the higher flights of set theory. Finally, it is often the position to which philosophically naïve respondents will gesture towards, when pestered by questions as to the nature of mathematics. Not surprisingly then, given this last observation, many philosophers of mathematics view “game formalism” as hopelessly implausible. This article is concerned with game formalism, its close relatives and with later developments, many of which have tried to overcome the perceived limitations of the cruder varieties.

## 1. Introduction

The *locus classicus* of game formalism is not a defence of the position by a convinced advocate but an attempted demolition job by a great philosopher, Gottlob Frege (1903, *Grundgesetze Der Arithmetik*, Volume II), on the work of real mathematicians, including H. E. Heine (1872)[^heine-1872] and Johannes Thomae (1898)[^thomae-1898]. Part of its relevance is that something like game formalism is still defended by some mathematicians, at least in their rest days when they think about philosophy not mathematics. Whether Heine and Thomae were in fact game formalists is open to serious question, as I’ll indicate in the next section. For now it must be emphasised that “formalism” in this sense—the Heine/Thomae position as interpreted by Frege and its descendants—is to be distinguished from a more sophisticated position (it is claimed), namely Hilbertian formalism. For more information on the latter see Detlefsen (1993)[^detlefsen-1993] or consult the entries on Hilbert’s program and the Frege-Hilbert controversy.) Detlefsen (2005)[^detlefsen-2005] also provides a detailed historical treatment of formalist themes in thinkers from the ancient Greeks up to the period of Frege and Hilbert and beyond which is the focus here.

Although it is the non-Hilbertian approach we will be concerned with in this entry, we briefly discuss the Hilbertian approach. The Hilbertian position differs because it depends on a distinction within mathematical language between a *finitary* sector, whose sentences express contentful propositions, and an *ideal*, or *infinitary* sector. Where exactly Hilbert drew the distinction, or where it should be drawn, is a matter of debate. Crucially, though, Hilbert adopted an instrumentalistic attitude towards the ideal sector. The formulae of this language are, or are treated as if they are, uninterpreted, having the syntactic form of sentences to which we can apply formal rules of transformation and inference but no semantics. Nonetheless they are, or can be useful, if the ideal sector conservatively extends the finitary, that is if no proof from finitary premisses to a finitary conclusion which takes a detour through the infinitary language yields a conclusion we could not have reached using finitary means alone, albeit perhaps (herein lies the utility) by a longer, more unwieldy proof. The goal of the Hilbert programme was to provide a finitary proof of this conservative extension result; most, though not all, think this goal was proved impossible by Gödel’s second incompleteness theorem.

Returning now to our non-Hilbertian focus, the earlier formalism which Frege attacked does not divide mathematics into the aforementioned dual categories of the finitary/contentful, and the infinitary/essentially meaningless but, on the contrary, treats mathematics in a unitary and homogeneous fashion. From now on I will use ‘formalism’, to refer to the non-Hilbertian positions and will start with an account of the formalist views Frege thought he found in Heine and Thomae and the criticisms he made of them. These criticisms are widely believed now to contain conclusive refutations of the game formalist approach. But there are a number of post-Fregean views which seem heavily influenced by, or strongly analogous to, formalism. I will go through these in turn:

- Wittgenstein’s views on mathematics, primarily the conception to be found in his *Tractatus Logico-Philosophicus*;
- formalism as found in the Logical Positivists, particularly Carnap;
- Goodman and Quine’s nominalist formalism;
- Haskell Curry’s version of formalism and
- formalist interpretations of the Curry-Howard correspondence.

I will conclude with a look at more recent formalist philosophers and an overall assessment of the prospects for formalism in contemporary philosophy of mathematics.

## 2. Game and Term Formalism

Frege was a notoriously uncharitable interpreter of others, certainly as he got older. But recent scholarship (see in particular, Lawrence, 2023)[^lawrence-2023] has shown that, in the case of his formalist opponents such as Hankel, Heine and Thomae, his interpretation is particularly wide of the mark. Such is Frege’s stature, however, that his distorted account of their views has been largely accepted by philosophers writing on formalism including, *mea culpa*, this author, in previous versions of this entry.

Perhaps the most important mistake Frege makes is to assume that when Thomae talks of mathematics as a game played with signs, Frege thinks of signs as concrete marks, as “figures that are produced by means of writing or printing on the surface of a physical body (blackboard,paper)” (Frege 1903/1980, §98)[^frege-1903][^frege-1903-2][^frege-1903-3][^note-1]. In fact Thomae often uses ‘sign’ to mean *representation*, for example infinite decimals are conceived of as representations of real numbers:

> an infinite decimal is. . . an abbreviation, a sign for an infinite sequence of the usual finite decimals, or a sign that is assigned to such a sequence (Thomae 1898: 5)[^thomae-1898][^note-1]

and these representations are *potentially* infinite—not *actually* infinite sequences—and so certainly not infinite, nor even unfeasibly large concrete signs. Hence Frege’s sarcastic comment:

> In order to produce it [an infinite series] we would need an infinitely long blackboard, an infinite supply of chalk, and an infinite length of time. We may be censured as too cruel for trying to crush so high a flight of the spirit by such a homely objection; but this is no answer. (Frege, 1903/1980, §124: 199)[^frege-1903][^frege-1903-2][^frege-1903-3]

is itself deserving of censure as too dogmatically dismissive of potentialist understandings of infinity.

Thomae’s thinking was also strongly coloured by his sympathy for Weierstrassian approaches to analysis rather than Riemannian ones (with Frege, it was the other way round). Weierstrass argued that an *algebraic* approach to real and complex analysis based on power series:

> $\sum\limits_{n=0}^{\infty }{{{a}_{0}}+a{}_{1}(x-c)+{{a}_{2}}(x-c){{x}^{2}}\ldots {{a}_{n}}{{(x-c)}^{n}}\ldots }$

where the terms *a_{i }*are to contain only algebraic operators such as the arithmetic functions addition, multiplication and exponentiation, notions more rigorous than the Riemannian one which made use of ‘transcendent’ non-algebraic operators. In Thomae’s exposition of these ideas a key point is that it does not much matter what the arithmetic operators operate on, as long as, whatever they are, they obey the algebraic rules of the ‘game’. Thus his understanding of formalism is much closer to what we would now call structuralism. So when he says:

> Now, for the formal conception, arithmetic is a game with signs which one may well call empty, thereby conveying that (in the calculating game) no other content belongs to them than the content attributed to them with respect to their behavior under certain combinatorial rules (game rules). (Thomae, 1898, 3)[^thomae-1898].

the key phrase is ‘(in the calculating game) no other content belongs to them’. Thomae does not deny that number terms have, or can have, ‘content’ in the sense of referents; they can refer—‘name’— the degree of an equation, for example (Thomae, 1898: 3)[^thomae-1898]. But in performing arithmetical operations on (finite initial segments) of infinite sequences, we ‘bracket’ any content other than that belonging to the operational signs much as we might bracket content in checking for logical correctness a piece of mathematical reasoning in a semi-formalised expansion of natural language—ignoring the meaning of phrases such as ‘real number’, ‘function’, for example, and looking only at formal structure in the sentences in the argument.

In sum, the formalism Frege attacks is a straw man position. But it is a historically important one, not just with respect to Fregean exegesis but because it is one which later philosophers took as a starting point to build on—or a blind alley to avoid. For Frege, anything which smacks of formalism is a blind alley because he takes arithmetic to be a body of truths expressed by utterances in which numerical expressions designate abstract referents independent of the mind (or at least any particular individual’s mind). Frege says that Heine and Thomae talk of mathematical domains and structures, of prohibitions on what may be uttered (e.g. against writing ‘$3\div 0$’ which is deemed, in some special sense, meaningless), of numbers being greater than or less than one another (rather than physical marks being larger or smaller, darker or lighter)—all things which, Frege notes, make no sense if arithmetic is a theory of marks and their physical properties or is just a body of transformations of referent-less symbols. He fails, however, to consider that they may express themselves in this way because they do not in fact take arithmetic as dealing with manipulation of meaningless concrete marks.

Historically two distinct textbook viewpoints have been distilled from Frege’s anti-formalist critique, doctrines which Resnik (1980: 54)[^resnik-1980], and likewise Shapiro (2000: 41–48)[^shapiro-2000] describe as *term formalism* and *game formalism*. The term formalist views the expressions of mathematics, arithmetic for example, as meaningful, the singular terms as referring, but as referring to *symbols* such as themselves, rather than numbers, construed as entities distinct from symbols. The game formalist, however, sticks with the view that mathematical utterances have no meaning; or at any rate the terms occurring therein do not pick out objects and properties and the utterances cannot be used to state facts. Rather mathematics is a calculus in which ‘empty’ symbol strings are transformed according to fixed rules. Game formalism is thus attractive to anyone keen to block, avoid, or sidestep (in some way) any ontological commitment to a problematic realm of abstract objects. For standard mathematics entails a plethora of theorems affirming the existence of infinite realms of entities—numbers, functions, sets, morphisms, categories and so forth, entities which do not seem to be concrete which, indeed, seem hard to fit into a thoroughly naturalistic conception of reality.

Game formalism is the only game in town for the anti-platonist worried about subscribing to an ontology of abstract objects. Term formalism, by contrast, in interpreting mathematics as *about* symbols transforms it into a kind of syntactic theory. However standard syntactic theory entails the existence of an infinity of entities—expression types—which seem every bit as abstract as numbers. Indeed, as Gödel’s arithmetisation of syntax showed, the elements and inter-relationships of standard formal syntax can be modelled as an infinite substructure inside the standard model of arithmetic. So term formalism would seem to be of no use to the anti-platonist.

Of course formal syntax and proof theory later emerged as a branch of mathematics. Frege complains that Heine and Thomae do not provide a syntax and proof theory which is remotely adequate as an account of the mathematics with which they deal. This is true but it took someone of Frege’s stature to revolutionise mathematics by introducing hitherto unprecedented standards of rigour in the formalisation of mathematical theories. He recognised (§90: 185–6) that one could treat mathematical theories, their language, axioms and rules, as formal, mathematical objects in their own right. This is exactly what the Hilbert programme set out successfully to achieve, creating the new disciple of metamathematics.

Given these tools, how should a rigorous game formalist, in Frege’s sense, proceed? She will give us a characterisation of a formal language by setting out what the basic elements are—primitive symbols, and strings thereof—and then give a recursive specification of which strings count as well-formed. Similarly we will be given a rigorous specification of which arrangements of well-formed formulae count as proofs in a given system, and of what theorem they prove in each case. If strings such as ‘$3+1=0$’ or ‘$3 \gt 2$’ come out as provable in the system (arithmetic modulo 4, say) then that is enough to count them as correct utterances of the system. No further issue of truth need arise; nor do we need to assume that there is only one system for a given set of symbols. Nor, furthermore, need we assume that each such system is complete (though Frege took Thomae to task for the incompleteness, massive though readily rectifiable, of his arithmetic calculus). We need make no assumption that the numerals in these strings refer to anything outside the system, indeed we need not assume they refer to anything at all. This rigorous game formalism, then, is not subject to the objection that ‘3 $\gt 2$’ should come out as false, on any legitimate formalist reading of ‘$\gt$’; no need to think of the numerals as referring to concrete marks and ‘$\gt$’ meaning physically greater in size.)

Thus such a game formalist avoids some of the objections Frege raises against the position he attributes to Heine and Thomae. But there are two main objections he sets out which still apply to game formalism as developed using the tools of modern metamathematics. The first is the *question of applicability*: if mathematics is just a calculus in which we shuffle uninterpreted symbols (or symbols whose interpretation is a matter of no importance) then why has it been applied so successfully—and in so many ways, to so many different things—ordinary physical objects, sub-atomic objects, fields, properties, and indeed from one part of mathematics to another (we can count the number of dimensions in a pure geometric space)? Frege writes:

> Now, it is applicability alone which elevates arithmetic from a game to the rank of a science. (§91 in Frege 1903/1980: 167])[^frege-1903][^frege-1903-2][^frege-1903-3]

Secondly, Frege quite rightly and insistently distinguishes on the one hand the ‘game’—arithmetic, set theory, topology or whatever—treated simply as a mathematical object in its own right, a formal system, and, on the another, the theory of the game. ‘Let us remember that the theory of the game must be distinguished from the game itself’ (§107, 183). Thus in the ‘game’ of trigonometry we might derive

$$ \sin^2\theta +\cos^2\theta = 1 $$

from the Pythagorean Theorem. In the metatheory we can prove:

$$ \vdash \langle \sin^2\theta + \cos^2\theta = 1\rangle, $$

the claim that the formula with such and such a code in the mathematical representation of the syntax (the code represented in the meta-meta-theory here by ‘$\langle\sin^2\theta +\cos^2\theta = 1\rangle$’) is provable. Likewise in the meta-theory we can prove lots of other things about proof and refutation, for instance we may be able to show that lots of sentences are neither provable nor refutable.

The problem this raises for the game formalist is as follows: the metatheory is itself a substantial piece of mathematics, ostensibly committed to an infinite realm of objects which are not, on the face of it, concrete. Tokens of the expressions of the object language game calculus may be finite—ink marks and the like; but since there are infinitely many expressions, theorems and proofs, these themselves must be taken to be abstract types. At best, the formalist can achieve no more than a reduction in commitment from the transfinite realms of some mathematical theories, such as set theory, to the countably infinite, but still presumably abstract, realm of arithmetic, wherein the syntax and proof theory of standard countable languages such as those of standard set theory, can, as Gödel showed, be modelled. This may be enough for term formalism, though the reduction of all mathematics to a theory of syntax is not going to go down well with mathematicians (on this see further the section on Curry below). But it will not do for game formalists if we assume they are motivated by some sort of anti-platonism.

Can formalism be developed in such a way as to surmount these two crucial objections, the problem of applicability and the problem of the metatheory, as I will call it? (Not that these are the only objections to formalism, but they are two fundamental ones.) Because Frege’s critique did not quash all formalistic impulses in later philosophers of mathematics, we shall look, now, at future developments, to see how they fare.

## 3. Tractarian Formalism

Wittgenstein was a keen student of Frege’s work, directed to further his studies under Bertrand Russell by Frege himself in the course of a visit he made to see Frege in Jena. One might, then, think him inoculated against formalism. But definite formalistic elements surface in Wittgenstein’s *Tractatus*.

True, the *Tractatus* is a notoriously difficult work to interpret. Even the question as to whether the main portion of the book, essentially all of it other than the ‘frame’ of the preface and the end, is to be taken as a serious attempt to present a metaphysics is controversial. If we leave that hermeneutic controversy aside, and consider the metaphysics which is offered to us, the formalistic aspects one finds are twofold. Firstly, mathematical sentences are said to express ‘pseudo-propositions’, and so are devoid of truth value (only contingent propositions have a truth value). Secondly, mathematics is described as a ‘calculus’ which is not to be used to represent the world as it is in itself but whose value is entirely instrumental. To be sure, the most explicit statement of this is *not* in the *Tractatus* but in comments Wittgenstein wrote on Ramsey’s copy of it:

> The fundamental idea of math. is the idea of *calculus* represented here by the idea of *operation* The beginning of logic presupposes *calculation* and so number. Number is *the* fundamental idea of calculus and must be introduced as such (Lewy, 1967: 421–2)[^lewy-1967].

In the *Tractatus* proper we do get the idea that mathematical propositions are mere instruments (all of mathematics, not just an ‘ideal’ fragment, as in Hilbert):

> Indeed in real life a mathematical proposition is never what we want. Rather, we make use of mathematical propositions only in inferences from propositions that do not belong to mathematics to others that likewise do not belong to mathematics. (In philosophy the question, “What do we actually use this word or this proposition for?” repeatedly leads to valuable insights.) (*Tractatus* ¶6.211.)

This idea is prefaced by the statements:

> Mathematics is a logical method. The propositions of mathematics are equations, and therefore pseudo-propositions. (*ibid*, ¶6.2)

> A proposition of mathematics does not express a thought. (*ibid*, ¶6.21)

Care must be taken, however. Wittgenstein distinguishes utterances which are *sinnlos*, which lack sense (including logical tautologies and contradictions here) from those which are *unsinnig*, nonsensical; it is not clear into which class mathematical utterances fall. One might well think that the game formalist should treat mathematical utterances, on that view just strings of meaningless marks, as *unsinnig*, not just *sinnlos*. One clear difference from game formalism however is this: for Wittgenstein mathematics should not be conceived of as a calculus separate from other uses of language. Rather he attempts to show that parts of arithmetic, at least, can be seen as grounded in non-mathematical uses of language. Frege by contrast, whilst arguing that a proper account of arithmetic (and analysis) should show how its generality enables one to give a uniform account of multifarious different applications (cf. Dummett, 1991 Chapter 20)[^dummett-1991] also argued strongly for the view that mathematical utterances have a meaning independent of, conceptually prior to, their use in applications.

Wittgenstein attempts no theory of mathematics in the *Tractatus* beyond arithmetic, a rather narrow fragment of arithmetic at that. The theory clearly shares the anti-platonism of the game formalist. There are no numbers, arithmetic is to be construed as a calculus in which one manipulates exponents or indices of operators. What is an operator? Wittgenstein distinguishes operator terms from function terms but commentators have struggled to explain what the distinction comes to. It is clear that Wittgenstein held that two occurrences of a function term $f$ applied to different strings $t$ and $u$ have different meanings, where by ‘meaning’ Wittgenstein means referent, something like Frege’s *Bedeutung*. Thus ‘$f$’ in “$f(t)$” does not refer to the same entity as the outermost $f$ in “$f(f(t)$”; this is supposed to be the basis of the solution to Russell’s paradox (¶3.333). In particular ‘the father of’ in “the father of John”, means something different there compared to its outermost occurrence in “the father of the father of John”. There can be no genuine iterated application of functions in other words, a cure for Russell’s paradox that many will find about as bad as the disease.

*Operators*, however, are to be distinguished from functions in at least that aspect: genuine iteration of operators—the sentential operators of propositional logic are a prime example—is possible without supposing a change of sense or reference from one token to the other. What is their meaning or referent then? Wittgenstein denies they have any referents, this is a generalisation of his claim that the logical constants are not representatives. Peter Hylton (1997: 96–98)[^hylton-1997] argues that Wittgenstein in the *Tractatus* has Russellian *propositional functions* in mind when he talks of ‘functions’ and is at pains to distinguish operators from these “substantial” entities. Russellian propositional functions are not the same as ordinary mathematical functions, the model for Frege’s notion of function. Rather they are structured entities, structurally related to the propositions which are their values— gappy states of affairs might be one way to think of them. Operators, by contrast, do not stand for any such entity, they are not parts nor any sort of ingredients of propositions, they “leave no trace” in them.

Sentential operators are conceived as mapping not signs, nor inscriptions, to other signs and ascriptions but rather propositions, (in Wittgenstein’s rather course-grained sense of the term) to propositions. On Wittgenstein’s account of proposition, repeated application of an operation such as negation $\ldots p, {\sim}p, {\sim}{\sim}p\ldots$ may take one back to an earlier point. Nonetheless Wittgenstein attempts to explicate arithmetic in terms of sentential operators applied to non-mathematical language. (One can see intimations here of Church’s later rigorous working out of a similar idea in his treatment of numbers in the lambda calculus as functions which repeatedly apply input functions.) In slogan form, numbers are exponents of operations (*ibid.*, ¶6.021). Thus where $\Omega$ is schematic for an operator and $\Omega p$ (or $\Omega(p))$ for its application to a proposition, then we can view the series

$$ p, \Omega p, \Omega \Omega p, \Omega \Omega \Omega p, \Omega \Omega \Omega \Omega p, \ldots $$

as the starting point for a ‘definition’ of numbers, to be had by rewriting it as

$$ \Omega^0 p, \Omega^{0+1}p, \Omega^{0+1+1}p, \Omega^{0+1+1+1}p, \Omega^{0+1+1+1+1}p,\ldots. $$

Here, then, we have infinitely many schematic rewrite rules. Indices such as ‘$^{0+1+1+1+1}$’ can be abbreviated by numerals in the obvious fashion, with ‘$^{0+1+1+1+1}$’ being abbreviated ‘4’ and so on.

Wittgenstein’s examples show (though he did not explicitly state this) that addition of two number/exponents $\Omega^{n}p + \Omega^{m}p$ (likewise $\Omega^{n+m}p)$ is given by the rule:

$$ \Omega^{n}p + \Omega^m p \Rightarrow \Omega^{n}(\Omega^m p) $$

telling us we may replace the expression on the left in a formula by the one on the right.

This is what underlies the ‘correctness’ of identities such $n + m = r$ except that for Wittgenstein no such identity expresses a truth. On his account, the identity sign disappears in a full analysis of language, wherein sameness and distinction are shown by sameness and distinctness of names, no two of which refer, in fully analysed language, to the same object (this view gives grounds for interpreting mathematical utterances in the *Tractatus* as *unsinnig*). Wittgenstein himself did not trouble to show that abandonment of an identity sign would not cripple the expressive power of language but others such as Hintikka (1956)[^hintikka-1956] and Wehmeier (2004)[^wehmeier-2004] have done so. What is left in the underlying language, with identity excised, are substitution rules (*Tractatus* ¶ 6.23).

These have to be interpreted in a general, and schematic, fashion. Thus when we plug in ${\sim}$ for $\Omega$, we find that (Wittgenstein had no intuitionist scruples here) a double application ${\sim}{\sim}p$ takes us back to (has the same sense as) $p$. But this does not ground the truth of $2 = 0$, since for many other operations $\Omega \Omega p$ is not equivalent to $p$. On the other hand

$$ \Omega \Omega(\Omega \Omega \Omega p) \text{ always has the same sense as } \Omega \Omega \Omega(\Omega \Omega p) $$

Wittgenstein implicitly assumes suitable rules for the interaction of brackets with operators, in particular, generalised associativity. (In fact, he uses a mix of brackets and the notation $\Omega 'p$ to express $\Omega(p)$.)

Since an equation $\Omega^{n}p=\Omega^{m}p$ is, in its underlying logical form, not a universal generalisation $\forall n,m(\Omega^{n}p = \Omega^{m}p)$ but a purely schematic generalisation, there is no form $\exists n,m(\Omega^{n}p \ne \Omega^{m}p)$ with which we can express inequality, even if we can make sense of ‘$\ne$’. Nor can we express the inequality $n \ne m$ schematically as the holding of the inequivalence of $\Omega^n p$ from $\Omega^m p$ for every choice for $\Omega$. Otherwise $2 \ne 0$ would fail since ${\sim}{\sim}p$ is equivalent to $p$. The *Tractarian* theory cannot handle inequalities.

So much for addition and the limitations of its account of that operation. What of multiplication? Wittgenstein does define it, at ¶6.241, by:

$$ \Omega^{n\times m}p \Rightarrow (\Omega^n)^m p $$

but to grasp this as a general principle we need to know how to interpret the notation $(\Omega^n)^m$. In more conventional mathematics, one might simply define $(x^n)^m$ as $x^{n\times m}$ but clearly this (or rather the equivalent for the interaction of exponents of operators) would introduce a circularity into Wittgenstein’s account. Alternatively one could appeal to a recursive theory of exponents – $a^{m\times 0}= a, a^{m\times(n+1)} = a^m + a^{m\times n}$. Since the principle of induction needed to show that the recursion is coherent features nowhere in Wittgenstein’s system, these rules would presumably have to be taken as primitive.

Overall, then, Wittgenstein in the *Tractatus* gives us no account of mathematics in general other than for a fragment of arithmetic, basically positive identities involving only addition. And there he denies that the sentences express propositions with truth values. Of course the book was written under extraordinarily difficult circumstances. Perhaps his account could have been developed further and more plausibly, despite the difficulties noticed above—but for some scepticism on that front, see Landini, 2007. Certainly Wittgenstein made no attempt to do so whilst engaged with F.P. Ramsey and the Vienna Circle in the 1920s. If Wittgenstein’s standpoint was not capable of much further development, we have the choice of either abandoning all of mathematics except, at most, a fragment of the arithmetic of addition; or else of rejecting the *Tractarian* account. One does not need to be slavishly uncritical of contemporary mathematics to see what the reasonable option is here. Admittedly, rejecting the *Tractatus* account is also the option Wittgenstein himself seems to adopt at the end of the book; here then we enter the issue of what the point is of taking us through such a bizarre and unconvincing theory in order to throw it away at the end. (For a more positive appraisal of Wittgenstein’s *Tractarian* position, see Floyd (2002)[^floyd-2002].

Wittgenstein’s later work on philosophy of mathematics, such as the *Remarks on the Foundations of Mathematics* 1956/1978), for a long time attracted even less approval than the *Tractarian* account, though recently philosophers such as Juliet Floyd and Hilary Putnam have come to its defence as an interesting and informed account of mathematics (Floyd/Putnam, 2000)[^floyd-2000]. Its themes include the rejection of the actual infinite (indeed the tendency in his writings is strongly finitist); the denial that undecidable sentences are meaningful; a rejection of Cantor’s powerset proof; the idea that proof discovery changes the very meaning of the terms involved; and other very radical ideas. Among them we find a continued adherence to formalist motifs:

> In mathematics *everything* is algorithm and *nothing* is meaning; (*Philosophical Grammar*: 468).

Another persistent theme in Wittgenstein’s thought is that the meaning of mathematics resides entirely in its utility in non-mathematical applications. But there is no systematic theory of how this applicability comes about, no proof of a conservative extension theorem, for example, showing how application of mathematical calculi to empirical premisses will never lead us to derive an empirical conclusion which does not follow from those premisses. And there is no resolution of the problem of the metatheory. On the other hand, we should observe that these notes of Wittgenstein on the philosophy of mathematics were not published by him, but by others after his death. For an overall view of Wittgenstein’s philosophy of mathematics as a whole see Wittgenstein’s philosophy of mathematics.

## 4. Formalism and the Positivists

Wittgenstein greatly influenced the Vienna Circle. The ‘official’ positivist theory of mathematics, as it were, is not a formalist one. Mathematical theorems express truths, albeit in a special way: true by virtue of meaning alone. The most influential positivist has been Carnap, if one does not classify Quine as a positivist (but Quine’s views, in the 1930s at any rate, were very close to Carnap’s, indeed arguably Quine remained truer to Carnap’s radical empiricism of that era than Carnap did). And one can certainly discern strong elements of formalism in some of Carnap’s writings, for instance in *Logische Syntax der Sprache* (1934/1937) and ‘Empiricism, Semantics, and Ontology’ (1950/1956).

The former book was translated into English as *The Logical Syntax of Language* in 1937. In it, Carnap argued that the correct method in philosophy is to engage in conceptual analysis conceived of as ‘logical syntax’, roughly speaking syntax proper and proof theory. To address philosophical differences, one proposes regimenting the disputed positions in formal languages or ‘frameworks’ which include a system of axioms and rules of proof; given these, some sentences are ‘determinate’, are provable or refutable. These are the analytic, and contradictory, sentences, relative to that framework. How do we choose which system to adopt? Carnap’s *Principle of Tolerance* (1934/1937), 52) allows us to adopt any system we wish:

> *In logic, there are no morals*. Everyone is at liberty to build up his own logic, i.e. his own form of language, as he wishes. [Italics in original]

Carnap extends this unbridled permissiveness to mathematics and indeed foists it on mathematicians generally:

> The tolerant attitude here suggested is, as far as special mathematical calculi are concerned, the attitude which is tacitly shared by the majority of mathematicians. [*ibid*.]

Any such calculus can count as a piece of mathematics, even an inconsistent one. By downplaying or outright discarding semantic notions, we simply bypass traditional ontological disputes concerning the nature of the entities mathematics is ‘about’. The only issue is the pragmatic utility, or otherwise, of any given mathematical calculus.

A number of concerns arise here. How can Carnap distinguish between empirical, scientific theories, and mathematical ones? Secondly, if pragmatic utility is primarily a matter of empirical applications, how does the Carnapian formalist know that a given calculus will conservatively extend empirical theory, how can this be known without appeal to meaningful mathematical results? Carnap writes:

> The formalist view is right in holding that the construction of the system can be effected purely formally, that is to say without reference to the meaning of the symbols; … But the task which is thus outlined is certainly not fulfilled by the construction of a logico-mathematical calculus alone. For this calculus does not contain … those sentences which are concerned with the *application of mathematics* … For instance, the sentence “In this room there are now two people present” cannot be derived from the sentence “Charles and Peter are in this room now and no one else” with the help of the logico-mathematical calculus alone, as it is usually constructed by the formalists; but it can be derived with the help of the logicist system, namely on the basis of Frege’s definition of ‘2’. (Carnap 1934/1937, 326)[^carnap-1934]

adding (italics are Carnap’s) ‘*A structure of this kind fulfils, simultaneously, the demands of both formalism and logicism*.’

But what is to stop us freely stipulating, in accordance with the principle of tolerance, ‘bridge principles’ for operators which proof-theoretically behave like numerical operators— ‘the number of *φ*’s’—via their definitional occurrence in formulations of arithmetic axioms and where the bridge principles include the likes of:

$$\begin{align} \text{the number of }\phi\text{s} &= 0 \leftrightarrow \exists x(\phi x \amp{\sim}\exists y(\phi y \amp y \ne x)) \\ \text{the number of }\phi\text{s} &= 1 \leftrightarrow{\sim}\exists x\phi x\, ? \end{align}$$

That is, we link the numeral for zero with a sentence stating there is exactly one entity of the appropriate type, the numeral for one with a sentence stating there are no such entities. If we do so, add the rules for standard decimal arithmetic, and then try to apply this calculus, disaster will ensue; but do we not need a *contentful* conservative extension result to show that for the calculi we do use, no disaster can occur?

Gödel’s incompleteness theorems pose very difficult problems for Carnap in this and other regards. The first incompleteness theorem tells us that in any $(\omega$-) consistent formal theory whose theorems are recursively enumerable and which entails a certain (rather limited) amount of arithmetic, there will be an arithmetical sentence such that neither it nor its negation is provable. In Carnap’s terminology, this seems to yield non-determinate sentences, which is a problem for him if we are convinced that nonetheless some of these sentences are true; and indeed the key type of sentences used to prove the incompleteness result—‘Gödel sentences’—are in fact true in the standard model of arithmetic if these sentences are constructed in an appropriate way (there are different ways of doing this) from a theory itself true in that model.

Gödel himself wrote, but did not publish, a searching critique of Carnap’s position (Gödel, 1953–9)[^gödel-1953]. Gödel focusses not on his first incompleteness theorem but on the corollary he drew in his second theorem: that, under a certain natural characterisation of the property of consistency, a characterisation which can be given mathematically via his arithmetisation of syntax, no formal theory of the type Gödel considered could prove its own consistency. He argued that Carnap, in order to make good his positivistic thesis that mathematical theorems are devoid of content, needed to give a consistency proof for mathematical calculi in order to show that they do not have empirical content, an abundance thereof indeed, by dint of entailing all empirical sentences. Warren Goldfarb notes, however, (1995: 328) that this point fails to appreciate the deep holism of Carnap’s 1937 position where the distinction between analytic and synthetic is relative to the system in question, the ‘linguistic framework’. (This deep holism, of course, has the counter-intuitive consequence that there is no framework-transcendent distinction between mathematics and empirical sciences.)

Carnap, in fact, understood the import of Gödel’s theorems (Tennant, 2008)[^tennant-2008]; he knew of the results directly from Gödel, who indeed read drafts of the *Logical Syntax*. Despite this he displayed what looks like remarkable insouciance with respect to its implications for his position. He acknowledged the need, in demonstrating consistency, to move to a stronger language (§60c), and freely helped himself to mathematical techniques which could in no sense be classed as finitary (in §14 he used, for example, rules with infinitely many premisses, notably one which was later to be called the *ω*-rule). In this way he can deny, for arithmetic at least, that there are any non-determinate sentences since every true arithmetic sentence is provable using the *ω*-rule (relative to a fairly weak finitary logic, considerably weaker than classical logic and a weak axiom system such as Q—Robinson Arithmetic).

Carnap’s relaxed attitude stems from his abandonment of the search for epistemological foundations. If one hopes to secure our knowledge of mathematics by appeal to a formalist interpretation then the search for a consistency proof of the type Hilbert sought makes sense and one will look for a vindication of mathematics as a whole from within a limited fragment with respect to which our knowledge seems hard to impugn. But Carnap, perhaps as a result of Gödel’s deep theorems, seems to have abandoned that goal and thought that the Principle of Tolerance absolved him of any such need. One can stipulate what one likes, including stronger axiom systems from which one can prove the consistency of a weaker theory. This does not give any firmer grounds for believing or accepting the weaker theory, but one does not need such grounds anyway.

Few nowadays look for Cartesian certitude in mathematics, so Carnap’s position here may seem reasonable. It is not so clear, however, that he has answered the problem of applicability. Even if a conservative extension result can only be given in a more powerful system, we need the result to be a contentful truth, not just a string of symbols we can derive from some system, if we are to have reassurance that a particular calculus we are about to use in designing bridges or computers will be pragmatically useful. And if the Carnapian grants that the result is a contentful truth, we can ask what, according to this formalistic position, constitutes that truth. Carnap, to be sure, was motivated by a horror of becoming embroiled in metaphysical disputation. But if his standpoint is emptied not only of epistemological ambition but is so deflationistic as to say little more than that metamathematical techniques can be applied to formalisations of mathematical and scientific theories then it is also emptied of all philosophical interest and ceases to make an intervention in the debates in philosophy of mathematics.

Not that Carnap really is abandoning metaphysics: this erstwhile opponent of metaphysics is really a brother metaphysician with a rival theory of his own, as F. H. Bradley might have said. Thus the main import of the later ‘Empiricism, Semantics, and Ontology’ is the dismissal of ontological worries as pseudo-problems by dint of the (highly contentious) distinction between ‘internal’ questions, to be settled by the rules of the framework—of mathematics, ordinary ‘thing’ talk or whatever—and ‘external’ questions such as ‘which framework to adopt?’. To these external questions there correspond, Carnap claimed, no propositions with truth values; to no such question, for example, is there a true answer of the form: “Yes, infinitely many abstract numbers exist”. Rather, they are to be answered by *decisions*, decisions to adopt or not based on pragmatic criteria regarding the efficiency, fruitfulness and utility of the framework with respect to the aims of the discourse in question. But what aims could these be? Predicting the flow of ‘sense data’, taken for granted as forming the ultimate furniture of the world? If so, we see that the vaunted ontological neutrality is a sham and we have a radical form of empiricist anti-realist metaphysics.

The vestige of formalism lies in this: Carnap takes ‘correctness’ to be determined by rules which govern a system and not to consist, for example, in correspondence with a realm of facts independent of the system of rules. And he thinks this approach dissolves ontological worries and frees us from any obligation to explain how finite, flesh-and-blood creatures like ourselves could come to have detailed knowledge of this independent realm of facts, this domain of configurations of abstract, non-temporal, non-causal objects and properties, a realm exposed by Carnap as a metaphysical illusion. One strong disanalogy with formalism is that Carnap takes this line with *all* areas of discourse, not just mathematics.

## 5. Nominalist Formalism

W. V. Quine famously rejected the positivist’s doctrine of truth in virtue of meaning and the quasi-logicist conception of mathematics as a body of analytic truths (and, partly as a result, also rejected his mentor Carnap’s internal/external distinction). In conjunction with Nelson Goodman, he produced instead what amounts to a formalist manifesto. His formalist phase does not seem to have lasted very long: he later settled on a form of mathematical platonism, downplaying, if not largely ignoring, his relatively youthful flirtation with ‘nominalism’. But while it lasted he and Goodman greatly advanced the discussion of formalism by tackling head-on the questions which other formalists shirked or ignored.

Goodman and Quine’s ‘Steps towards a constructive nominalism’ (1947) sets forth an uncompromising game formalism:

> The gains which seem to have accrued to natural science from the use of mathematical formulas do not imply that these formulas are true statements. No one, not even the hardiest pragmatist, is likely to regard the beads of an abacus as true; and our position is that the formulas of platonistic mathematics are, like the beads of an abacus, convenient computational aids which need involve no question of truth. (122).

They regard

> the sentences of mathematics merely as strings of marks without meaning

so that

> such intelligibility as mathematics possesses derives from the syntactical or metamathematical rules governing those marks. (111)

Commendably, Goodman and Quine do not shy away from the metatheory problem, the difficulty that syntax and metamathematics itself seems as ontologically rich and committed to abstract objects as arithmetic. On the contrary, they face it squarely and attempt to make do entirely with an ontology of concrete objects, finitely many such objects in fact. (However they do assume fairly powerful mereological principles, in particular universal composition: they assume that any set of objects, however scattered or diffuse, is also a mereological object –a ‘fusion’ or ‘sum’ – in good standing.)

With much ingenuity they try to develop a syntax which “will treat mathematical expressions as concrete objects” (*ibid.*)—as actual physical marks—and give concrete surrogates for notions such as ‘formula’, ‘axiom’ and ‘proof’ as platonistically defined. However they do not address the issue of the application of mathematics, construed in this concrete, formalistic fashion.

In addition to the applicability problem, there are two further crucial problems for formalism as developed by Goodman and Quine. Firstly it is not clear that they are entitled to the general claims they make about syntax, construed as a theory about certain concrete marks and fusions of marks. Thus when arguing that their definition of formula in terms of ‘quasi-formula’ gives us the results we want, they say:

> By requiring also the next more complex alternative denials in $x$ to be alternative denials of quasi-formulas, the definition guarantees these also will be formulas in the intuitively intended sense; and so on, to $x$ itself. (116)

(‘Alternative denial’ is the Sheffer stroke operation $P|Q$ which is true if and only if one component is false.) The problem lies with the ‘and so on’. Goodman and Quine are trying to work their way up through an arbitrary formula showing that their definition will ensure that each larger component is a formula. It is not clear how we can have a guarantee of this for arbitrary $x$, without something like induction over formula complexity; but this is not available as formulas are not generated in the usual inductive set-theoretic fashion. Similar remarks apply to the demonstration that proofs, as defined nominalistically on p. 120, have the internal order of precedence among immediate sub-premisses and conclusions that we intuitively expect. The demonstration proceeds with a generalisation over all numbers $k$ which number the axioms in a concrete proof and then appeals to a sequence of selections on them. This seems to presuppose the truth of generalisations over all numbers and indeed countable choice, resources unavailable to a strict nominalist.

Secondly, what can Goodman and Quine say about a sentence such as

$$ 2^{2^{2^{2^{ 2^2} }}}+1 \text{ is prime}\,? $$

(That is—with ‘2^$n$’ representing ‘2 to the power $n$’—‘[2^(2^(2^(2^(2^2))))]$+1$ is prime’; cf. Tennant, 1997,152.) They cannot deny the sentence exists, for there is the token before our very eyes. But there are strong grounds for thinking that no concrete proof or disproof will exist, for the only methods available may use up more time, space and material than any human could have at her disposal, perhaps than actually exists. There are countless sentences with this property: concrete tokens of them exist but no concrete proof or refutation actually exists, none that a human could manipulate as a meaningful utterance anyway. (Cf. Boolos, 1987.)[^boolos-1987] Formalists of Goodman and Quine’s persuasion seem forced to the conclusion that sentences like the above, sentences which are decidable in the usual formal sense, are neither true nor false, since neither concretely provable nor concretely refutable. To embrace this view, however, would be to butcher mathematics as currently practised; such a consequence should rather be viewed as a *reductio ad absurdum* of their position.

## 6. Term Formalism: Curry

The most substantive attempt at a non-Hilbertian formalist philosophy of mathematics is Haskell Curry’s book *Outline of a Formalist Philosophy of Mathematics* (Curry, 1951)[^curry-1951]. Curry is no game formalist, his position is closer to term formalism, of the two views we started out from. Curry’s philosophy of mathematics, however, is, or attempts to be, a highly anti-metaphysical one, at least to the extent that he thinks he can remain neutral on the issue of the ontological commitments of mathematics.

> Mathematics can be conceived as a science in such a way as to be independent of any except the most rudimentary philosophical hypotheses. (3)

Hence he is not motivated by an anti-platonist horror of abstract objects. His neutrality, indeed, is somewhat compromised by the fact that Curry is perfectly happy to commit to an infinite ontology of presumably abstract expression types. Officially he evinces disinterest in what the primitives—he misleadingly calls them ‘tokens’—of his formal systems are:

> We can take for those tokens any objects we please, and similarly we can take for operators any ways of combining these objects which have the requisite formal properties. (28)

But since for many systems there are infinitely many primitive ‘tokens’, they cannot all be identified with concrete marks which mathematicians have actually produced.

Like the term formalist, Curry takes mathematics, properly reconstructed after philosophical reflection, to have an essentially syntactic subject matter, namely formal systems. Unlike Frege’s adversaries, though, Curry, writing after the development of the discipline of metamathematics, is able to give a far more rigorous (albeit in his case somewhat eccentric) account of what a formal system is.

No restrictions are placed on what form the axioms, rules and therefore theorems of a formal system are to be. Truth for elementary propositions of a formal system consists simply in their provability in the system. One of his formal systems (Example 7: 23) has only one predicate “a unary predicate expressed by Gödel by the words ‘ist beweisbar’” (23), i.e., a provability predicate. The elementary truths of this system can be interpreted as claims about provability in the underlying system. Any formal system of the usual sort could be ‘reduced’ into one in which there is only one provability predicate and truth (= provability) in the reducing system of the elementary proposition *φ* holds only when *φ* is provable in the reduced system: $\vdash \langle \phi \rangle$(34–35). Curry allows that one can form compounds from elementary propositions by means of the usual logical operators in order to express complex propositions in the language of proof theory (Chapter IX).

The upshot is that mathematics in general becomes metamathematics, a contentful theory—Curry’s sentences express propositions with truth values—setting out the truths about what is provable from what in underlying formal systems whose interpretation, or rather interpretations, are not taken to be mathematically important. This standpoint, however, threatens to collapse into structuralism, into viewing mathematical utterances as schemata implicitly generalising over a range of (in general) abstract structures which satisfy the schemata. As to the problem of the metatheory, Curry does not seek to answer this; there is no real attempt to avoid commitment to a rich ontology of objects, except that, by considering only standard formal systems, one could make do with a countable ontology which can play the role of linguistic expressions. Only, however, at the cost of grossly distorting mathematical practice. Set theorists, topologists, analysts *et al*. entertain conjectures, and try to prove things ‘about’ sets, topological spaces, functions on the complex numbers and so on. In their philosophical moments they may wonder just what the concepts they are wrestling with are ‘about’, but they do not in general entertain conjectures or try to prove things ‘about’ expression strings, except where it is of instrumental value to them in proving things about sets, spaces, the complex plane and so on (cf. Resnik: 70–71).

## 7. The Curry-Howard Correspondence

Haskell Curry was also to play an important role in developments linking logic to computer science which some argue can lend support to formalism in mathematics. His work on combinatory logic along with work of W.A. Howard’s led to the ‘Curry-Howard correspondence’ (‘Curry-Howard’ henceforth written ‘CH’) or the ‘CH isomorphism’ linking logic, proof theory and computer science.

Curry intended to provide a general theory of functionality as part of a foundation for logic, “pre-logic”, as Curry called it. See in particular (Curry 1934) and, with Robert Feys, (Curry and Feys 1958)[^curry-1958]. At around the same time as Curry’s first publications in the area, Alonzo Church developed his untyped *λ*-calculus, also designed to provide a foundation for logic, indeed mathematics more generally, and also taking functions, very generally applicable, as fundamental. In these functional calculi, (for a comprehensive account see Barendregt (1984)[^barendregt-1984], also the entry on the lambda calculus) a concatenation $fg$ is used to represent the application of function $f$ to argument $g$ yielding an output value. Both argument and value can themselves be functions and self-application is allowed. Whereas Curry’s system is variable-free, variable binding in Church’s occurs by means of the *λ* term, the variable $x$, if and where it occurs in $N$, being bound in $\lambda x.N$. The fundamental operation in *λ*-calculus is *β*-reduction, the transformation which takes us from $(\lambda x.N)M$ to $N[x := M].$ Here $N[x := M]$ is the result of substituting $M$ for all free occurrences of $x$ in $N$.[^note-3] So, for example, $(\lambda x.xx)f$ *β*-reduces to $ff$. We can write this as:

$$ (\lambda x.xx)f \rhd ff $$

Thus these calculi achieve what Wittgenstein in the *Tractatus* (see above) seems to be gesturing at in his operations/function distinction, for in Church and Curry we have a fully developed theory of ‘operations’, that is functions which can take functions as arguments and values. Of course self-application, as in the infinite looping *β*-reduction:

$$\begin{align} (\lambda x.xx)(\lambda x.xx) &\rhd (\lambda x.xx)(\lambda x.xx) \\ &\rhd (\lambda x.xx)(\lambda x.xx) \\ &\vdots \end{align}$$

raises worries that paradox may emerge. Church thought that eschewing the use of free variables and restricting excluded middle (Church, 1932: 346–7)[^church-1932] blocked paradox but Kleene and Rosser showed (1935), using a strategy based on Richard’s paradox, that the system was trivial: every formula could be derived using the rules. Church fixed this up to produce a consistent untyped *λ* calculus, but the important step with regard to the CH correspondence was the development of typed *λ* calculi.

Now ‘type’ is a very overworked word. Tokens of that type, to use one of its meanings (roughly as abstract syntactic object), have sometimes been used to stand for properties, including higher-order properties, as in Russell’s various type theories. Church was to continue this tradition in his simple typed version of *λ*-calculus (Church, 1940)[^church-1940]. In this usage, types, such as the property of caninity or of being a shape, have instances such as Fido, in the first case, or the lower-order property of being square in the second case. Thus instances of types in this sense need not be abstract objects. Another usage is syntactic, as when the basic expressions of a language are divided into various disjoint categories (‘types’) and formation rules for generating well-formed expressions are set down making use of the type distinctions. In this usage ‘type’ is an expression in the syntactic metatheory of the language of some object theory. In some cases the syntactic theory is in fact part of the object theory under discussion. Independently of this, some presentations of syntactic type theories ‘push down’ the syntactic metatheory into the object theory under discussion by stipulating that the well-formed expressions of the object language contain syntactic proper parts, tags as it were, which are correlated with the metatheoretic type of the expression and have no semantic role. In Howard (1969)[^howard-1969], for example, the well-formed formulae of the conditional fragment of propositional logic are used as type symbols superscripting terms of the type theory.

The expression «$N: \tau$» which is usually read along the lines of:

$$ \text{term } N \text{ is of type } \tau $$

can be, therefore, read in a number of ways, for example:

I: Non-syntactic: the entity referred to by $N$ is an instance of the class/set/property referred to by *τ*, an instance which need not be syntactic nor, more generally, abstract.

II: Meta-syntactic: the expression referred to by $N$ is an instance of the syntactic category *τ*. The syntactic theory in which the ascription of term to type occurs is ‘meta’, relative to a background intellectual context, in that it is not there presented as (under its intended interpretation) part of a more general theory expressed in a language for which it itself provides the syntax.

III: Syntactic: the expression $N$ is an instance of the syntactic category *τ* and the type theory $is$ a syntactic theory for the language which it itself belongs to.

Whilst some textbooks on type theory can seem, to the logician, to be rather hazy on exactly which, if any, of the above interpretations of ‘type’ is at issue this is certainly not generally the case with the pioneers of these theories. Howard, for example, writes in his classic paper ‘The Formula-as-Types Notion of Construction’:

> The title has a second defect; namely, a *type* should be regarded as a [sic] abstract object whereas a *formula* is the name of a type. (1969: 479)

and distinguishes between types and type symbols (480).

There are non-syntactic models of various type theories, though these were developed later, for example (Scott, 1970)[^scott-1970], and make fairly strong set-theoretic cardinality assumptions, such as the existence of inaccessible cardinals. Much more relevant for the formalist are ‘term models’, syntactic models similar to the interpretations of languages which make use of their own symbols as the members of the domain, interpretations to be found in Henkin completeness proofs; and especially ‘syntactic semantic’ approaches, as in some interpretations of Per Martin-Löf’s intuitionist type theory (see the entry on intuitionistic type theory), or the ‘proof-theoretic semantics’ of Peter Schroeder-Heister (see the entry on proof-theoretic semantics) which eschew attempts to give meanings to types and terms by reference to ‘external’ truth-conditions: mathematical language is not to be taken as a representation of some independent reality.

In such a context, the distinction between meta-syntactic and syntactic readings of ‘type’ is not very important. What is important is that the axioms and rules of inference of type theory enable us to prove meta-theorems about types. The situation can be compared to the relation between sequent calculus and natural deduction, with the turnstile $\vdash$ of the former interpretable as a relation of derivability in some underlying natural deduction system, and the sequent calculus providing higher-order theorems about object language derivability. Thus whether or not one thinks of types as meta-theoretic notions, the calculi of type theory are such that one can prove theorems to the effect that term $N$ is of type *τ*.

Now Curry’s work in (1934) and more fully with Feys in (1958) had shown a certain correspondence between provable formulae in the theory of the conditional and the types of basic combinators in type theory. In particular, with $\rightarrow$ as the conditional and $\alpha \Rightarrow \beta$ representing function types, that is types (construed non-syntactically) whose inputs are type *α* functions and outputs type *β* functions, we have, (here $\vdash_{T\rightarrow}$ means provability in the positive (non-relevantist) theory of the conditional and $\vdash_{CL}$ means provability in a suitable combinatory logic):

$$ \vdash_{T\rightarrow} \mathrm{A} \rightarrow \mathrm{B} \text{ iff for some } N, \vdash_{CL} N : \alpha \Rightarrow \beta $$

where $N$ is a term built from basic combinators and *α* is structurally isomorphic to A (likewise *β* to B). That is, one can generate A $\Rightarrow$ B from A $\rightarrow$ B by replacing each occurrence of $\rightarrow$ by $\Rightarrow$, given a uniform substitution (perhaps the trivial identity one) of sentential letters in the formulae of the propositional language by names for basic types.

Curry and Feys (1958) extended the correspondence idea to one between type theory and Gentzen’s sequent calculus. In the paper already cited, circulated in 1969, but only published in a volume in a Festschrift for Curry in 1980, W.A. Howard (1969)[^howard-1969] deepened the CH correspondence by demonstrating a correspondence between intuitionistic sequent form natural deduction and type theory in *λ*-calculus format, generalising to encompass intuitionist arithmetic—‘Heyting arithmetic’ (HA)—(thus requiring an extension from propositional to predicate logic), all as part of a project of investigation of the constructivist notion of a construction. Howard deepened the results by making clear not only a correspondence between provable formulae in the sequent calculus and type ascriptions, but also between the terms in the type ascriptions and proofs of the corresponding formulae.[^note-4] For example, (to the horror of relevantists) A $\rightarrow$ (B $\rightarrow$ A) is provable in T$_{\rightarrow}$. The corresponding type is $\alpha \Rightarrow(\beta \Rightarrow \alpha)$, the type of the basic operator K, whose action is

$$ NM \rhd N $$

and whose *λ* representation is $(\lambda x.(\lambda y.x))$ (usually abbreviated $\lambda xy.x)$, as can be seen by the *β*-reduction chain:[^note-5]

$$ (\lambda x.(\lambda y.x)N)M \rhd (\lambda y.N)M \rhd N. $$

The simplest proof of A $\rightarrow$ (B $\rightarrow$ A) in T$_{\rightarrow}$ is:

$$ \dfrac{\dfrac{\dfrac{}{A}\scriptsize{1}}{B \to A}}{A \to (B \to A)}\scriptsize{1} $$

*Figure 1*

in which the second step, to the intermediate conclusion B $\rightarrow$ A, is an instance of $\rightarrow$I(ntroduction) with vacuous discharge of the unassumed antecedent B (in a sequent calculus version, the rule of thinning, adding extra assumptions in the sequent antecedent, would be used). The type theoretic proof in type theory TT[^note-6] of the construction of a term “inhabiting” the type $\alpha \Rightarrow(\beta \Rightarrow \alpha)$ takes the form:

$$ \dfrac{\dfrac{\dfrac{}{x:\alpha}\scriptsize{x}}{\lambda y.x:\beta \Rightarrow \alpha}}{\lambda xy.x:\alpha \Rightarrow (\beta \Rightarrow \alpha)}\scriptsize{x} $$

*Figure 2*

Here *λ* abstraction, the introduction of *λ* terms, corresponds to $\rightarrow$I, so the *λ* term $\lambda xy.x$ which is shown to have type $\alpha \Rightarrow (\beta \Rightarrow \alpha)$ ‘codes’ two steps of the type correlate of $\rightarrow$I, namely the rule $\Rightarrow$I introducing function types (the first application an example of vacuous discharge) and we can recover the above proof of the propositional theorem. Moreover given the tight connection between type theoretical calculi and programs in certain types of programming languages, we can also see the TT proof as a program of steps in the construction of a certain type of computational object.

In natural deduction systems, normalisation is the procedure by which redundant inferential loops are eliminated. In certain logics (such as intuitionistic logic), a normalisation metatheorem holds and tells us that any proof can be stripped of its redundancy and smoothly reduced to a normal form. A further level of correspondence, brought out by Howard, links normalisation with the ‘evaluation’ of programs in which complex terms are reduced to their simplest forms (this is not always possible in the more expressively powerful type systems).

It seems to be Kreisel who introduced the slogan ‘formulae as types’, with Martin-Löf responsible for the more widespread ‘propositions as types’ slogan (See again, Wadler, 2015)[^wadler-2015]. In the philosophical context, ‘proposition’ is often used to mean something like the meaning of a sentence, i.e. of a formula of a certain sort. Using this terminology, a widespread intuitionist position is that that the proposition expressed by a formula is the set (or species, for the intuitionist) of all proofs of the formula. Given that different provable formulae will correspond to different types, the CH correspondence allows us to rephrase this ‘syntactico-semantics’ position as: the proposition expressed by a formula of HA is the type of its proofs, where ‘type’ is not a straightforward synonym for ‘set’ or ‘species’ but the notion from *λ*-calculus. As noted, this calculus is a formal system with rich interconnections with programming and computer science and readings in which the instances of types are purely syntactic, for example proof-theoretic entities. Hence the meaning of a formula, the proposition expressed, on such readings, does not represent a reality distinct from the linguistic system in which the formula occurs.

The connection with intuitionism, then, is clear: but what is the relevance of the CH correspondence to formalism? There are, in the first place, clear overlaps between some forms of intuitionism and certain formalist positions. Not the philosophical intuitionism of the founding father Brouwer, of course, with its ontology of mathematical objects as mental constructions and an epistemology in which mathematical knowledge is based on internal reflection on the succession of ideas; this is a mathematical metaphysics far removed from formalism. But many constructivists have embraced, without accepting his metaphysics, the Brouwerian identification, or close linkage, of mathematical correctness (truth, if one is prepared to speak of mathematical truth) with provability. This sort of identification is more than congenial to a certain brand of formalism, one which rejects the idea that mathematical theses represent a mind-independent reality and which also divides the mathematical sheep from the goats on the basis of those which are provable, in some formal system, versus those which are disprovable.

But there are also substantial differences between the intuitionist and the formalist. For one thing, not only Brouwer but also many later constructivists refuse to identify provability with provability in some formal system. For another, formalists have generally felt free to help themselves to classical logic, and have emphasised the *free creativity* of the mathematician: she should be free to generate whatever mathematical theories she wishes, subject only to withdrawing them if they turn out to be inconsistent (in the chosen background logic).

On the first point the formalist will, of course, be a formalist! She will link correctness, at least at the most fundamental level, to formal proof. Here, then, the CH correspondence, or better correspondences, are surely very attractive to the formalist. The linkage between propositions and computations, algorithmic reductions of terms coding proofs to irreducible normal forms in particular, fits very snugly with those versions of formalism which take mathematics to be, at heart, shuffling of symbols with no external reference.

On the second point, further work on the CH correspondences generalised the results from intuitionistic logic to a wide variety of other logics, in particular to classical logic (Griffin, 1990)[^griffin-1990], as well as to other logical frameworks such as modal logic and linear logic. There is no burdensome logical restriction imposed by ‘Formulae-as-Types’ then, no need for the formalist to fight with one hand tied behind her back.

What of the free creativity the formalist cherishes? Constructivist type theory has, of course, been extended well beyond Heyting arithmetic; particularly ambitious extensions are to be found in the univalent foundations project based on homotopy type theory (Awodey, 2014)[^awodey-2014]. This, then, is an avenue a formalism based on Formulae-as-Types might pursue. But for a formalist who wishes to be non-revisionist about non-constructivist mathematics the prospects are perhaps less clear. It is not enough just to add in the extra axioms or inference rules which yield the particular theory, in a standard framework, e.g. of a first-order or higher-order language. For one needs to do the further work needed to show that an extension of the CH correspondence obtains in this system.

Moreover there is also an issue with primeness in the sense of the proof-theoretic property (which intuitionist logic satisfies) that when $\vdash$ A $\vee$ B then either $\vdash$ A or $\vdash$ B. Classical theories typically do not have this property, unless negation-complete, and this will pose problems for generalising the CH correspondence and for justifying excluded middle (assuming the formalist does not simply take all non-trivial calculi as legitimate without need of justification). If correctness of a mathematical claim, relative to a particular framework, is identified with provability and if a disjunction can be correct where neither disjunct is provable then the formalist would seem to require some fancy footwork—supervaluationalism is not obviously appropriate here—to justify using classical logic.

There is also the problem of applicability, which Frege thought an insuperable one for formalists. What can the meaning be of applied mathematical notions, such as «the number of *φ*s», where mathematical and non-mathematical discourse is mixed together? Unless the CH formalist wishes to go down the Dummettian anti-realist route and generalise the notion of proof to a notion of verification appropriate for empirical language, she will have to find a way of combining, without too much ad hocness, a proof-theoretic semantics for pure mathematics with a different, perhaps a realist, truth-conditional semantics, for empirical language.

Finally it should be noted that CH formalism, if we can call it such, will be unacceptable to the formalist who is motivated by anti-platonist concerns and wishes to exclude abstract objects from all mathematics, including metamathematics. For the meanings of concrete utterances of mathematical formulae, according to CH formalism, are sets/species/types of proofs, and the latter are abstract objects, infinitely many of them, of arbitrarily long finite length. The problem of the metatheory, in other words, has not been met. The anti-platonist cannot straightforwardly lift the ideas of syntactico-semantics and apply the CH correspondence in support of anti-platonism; a great deal more philosophical work is required.

## 8. Contemporary Formalism

Later developments have been primarily in the ‘Hilbertian’ wing of the formalist movement. P. J. Cohen’s work on the generalised continuum hypothesis showed, in tandem with Gödel’s relative consistency proof, that it and countless related set-theoretic propositions concerning the relations of the cardinality of a set to that of its powerset are undecidable by current axioms. With no obvious, non-ad hoc, ways to extend the axioms to decide these questions, this led some mathematicians, such as Cohen himself (Cohen, 1971)[^cohen-1971] and Abraham Robinson, (Robinson, 1965; 1969)[^robinson-1965] to despair of a realistic interpretation of higher set theory. They therefore treat branches of mathematics in which no plausible axiom set will decide the key questions as ‘ideal’ parts of mathematics, lacking the content to be found in other areas.

As to game formalism, although philosophers may accuse mathematicians of a tendency to lapse into this seemingly discredited position, very few philosophers advance views resembling the game formalists. Gabbay (2010)[^gabbay-2010] and Azzouni (2004; 2005; 2006; 2009)[^azzouni-2004][^azzouni-2005][^azzouni-2006][^azzouni-2009] have marched behind the formalist flag. Gabbay’s formalism (which he develops only with respect to arithmetic in the paper cited) occupies ‘lush middle ground between traditional formalism, fictionalism, logicism and realism’ (Gabbay, 2010: 219)[^gabbay-2010]. Moreover he writes ‘Contrary to traditional (game) formalism, my proposal shall not involve an attempt to provide formal derivations of each and every arithmetic truth’ (Gabbay, 2010: 221)[^gabbay-2010].

Azzouni describes his ‘version of formalism’ (Azzouni, 2004: 105)[^azzouni-2004] as one in which ordinary mathematical proofs ‘indicate’ formal derivations. The indication relation is left rather open: Azzouni does not claim that the indicated derivations all belong to a single formal system; rather ordinary proofs can indicate derivations from a ‘family’ of formal derivations. However, the indicated derivations, Azzouni says need not exist; certainly concrete tokens of them need not exist in the same period as the informal proofs which indicate them. Proofs in ancient Greek geometry indicate 21st century or later derivations. They may never, in fact, exist—they may be too long ever to be written down (Azzouni, 2006: 154)[^azzouni-2006] though these non-existent proofs are supposed to explain the consensus among mathematicians about which informal proofs are correct! In later work Azzouni seems to retreat from this (or any) brand of formalism:

> I kept falling (against my will) into a view that mathematicians had to be engaged in *something* like sophisticated syntactic pattern-recognition while perusing informal mathematical proofs, so that they would be sensitive (without realizing it) to a background of *nonexistent* formal derivations. (Azzouni, 2009: 25)[^azzouni-2009]

moving to an ‘inference package’ view of mathematical reasoning which does not seem formalist: see again Azzouni (2009)[^azzouni-2009].

There are, however, another group of contemporary philosophers of mathematics whose views seem close to formalism, namely (some among the) fictionalists. Now the term ‘fictionalist’ can mislead as not all fictionalists assimilate mathematics to fiction. And even if one did, the question would arise: ‘What philosophical account of fiction, and discourse about fiction, does one adopt?’ Many philosophers resile from a realist ontology of fictional characters just as many reject a realist—platonistic—ontology for mathematics. A very simplistic anti-realism about fictionalism might analyse such statements as ‘Oliver Twist was born in London’ as true (or correct) just in case that sentence, or a synonym, occurs in Dickens’s novel (Field, 1989: 3)[^field-1989]. Even if this worked for fiction, which it pretty clearly does not,[^note-7] a parallel approach for mathematics is patently absurd. If a mathematical thesis is proclaimed a theorem, with or without proof, in a journal, be it however respectable, then, even if this claim is never challenged and the assertion accepted by the mathematical community this by no means entails that the thesis is true (or correct, if one dislikes applying truth predicates to mathematical sentences). Given the number of “theorems” whose purported proofs were later discovered to be incorrect, we can be pretty sure some falsehoods will wrongly remain accepted for all time as proven. Moreover there will be no end of mathematical claims, some true, some false, which never make it into the mathematical literature at all, never being considered by actual mathematicians.

Now the Oliver Twist example is owing to Hartry Field, the founder of the school of fictionalism, if we may term it such. But he qualifies his position as follows:

> most of us believe that Oliver Twist lived in London only in the sense that we believe that the novel says that or *has as a consequence* that Oliver Twist lived in London (1989, 3) [emphasis mine].

Whether or not this will work for fiction (What if the work is inconsistent: must one use a relevant consequence relation? How can it handle comparisons among different works as in the Tolstoy/Dostoyevsky example above?) this is an interesting position on mathematics with definite formalistic overtones. The mathematician can put forward any (consistent) theory she likes. The truths of the theory are then just the consequences of the theory, there is no need to think that the theory represents an external reality. Fictionalism along these lines has been investigated by Mary Leng (2010)[^leng-2010]. But a key question is: how does one read ‘consequence’? For a formalist, this has to be consequence as derivability. But Leng rejects such a reading: her fictionalism is one in which logical consequence is interpreted not syntactically but modally, with the necessity in question taken as primitive. Hence, this subspecies of fictionalism cannot be classed as formalist.

Weir, by contrast, explicitly embraces formalism (1991; 1993; 2010; 2016), moreover formalism in the game formalist tradition. His position, if situated with respect to fictionalism, can be seen as one in which ‘consequence’ is read, in the formalist tradition, syntactically, in terms of formal derivability. As a first approximation, the position is that a mathematical sentence is true if there exists a *concrete* derivation of a token of it, false if there exists a concrete derivation of a token of its negation. Since truth and falsity conditions make no appeal to abstract proofs, this type of formalism is firmly anti-platonist.

This bluntly concretist formalism would seem to face insuperable problems: for example in the shape of the ‘concretely undecidable’, those short theses with unfeasibly long proofs or disproofs mentioned above in connection with Goodman and Quine’s nominalism. Weir’s attempt to address such problems takes as its basis a fairly common ‘post-Fregean’ or ‘neo-Fregean’ perspective on language. Frege, at least early in his career, held that the truth value of a sentence is determined by two factors, the *Sinn*, the sense, literal meaning or informational content, of the sentence; and the way the world is. Indexicality and wider context relativity of sentences he initially supposed could be met by assuming speakers who uttered and grasped such sentences took them as elliptical for more complete utterances whose sense fixed, in combination with the world, a unique truth value.

Later work (including Frege’s own) revealed the inadequacy of this picture, revealed that some indexicality, for instance, is ‘essential’ in John Perry’s phrase, to the thought expressed. I can utter ‘it’s hot now’ truly without knowing where, when or even who (if sufficiently disoriented or out my head) I am. Those who are not utterly sceptical, as radical contextualists are, of systematic theories of meaning, will amend Frege’s view to a tripartite one. A sentence’s truth value, in a particular context, is determined by its informational content, by contextual circumstances related to, ‘fitted to’, the utterance by aspects of the speakers’ practice, and finally by the mind and language-independent world. The contextual circumstances need not figure in the sense or informational content of the utterance; thus a specification of them may include dates and locations, though this is not part of the sense of ‘it’s hot now’ (compare Kaplan’s *character* versus *content* distinction, especially the second sense of ‘content’ discussed in his 1989 (fn 28: 503)).

This picture in turn suggests the idea that the contextual circumstances which ‘make true’, in conjunction with independent reality, an utterance, may make it true in a non-realist fashion. In Weir’s version of game formalism, the fundamental idea is that what makes true (or false) ‘$\sin^2\theta +\cos^2\theta = 1$’ in a particular system is the existence of a concrete proof or refutation, though the statement that such a concrete proof exists is no part of the literal meaning or sense of the claim.

The advantage of this type of formalism is that it not only affirms the meaningfulness, the possession of sense, of mathematical utterances; in sharp contrast with traditional game formalism, it holds that such utterances have truth values, where proofs or refutations exist. The problem of the metatheory is met if one can give, after the fashion of Goodman and Quine 1947, a non-mathematical account of concrete proof. Of course, as noted above, severe problems remain. The problem of applicability has to be met, by providing conservative extension proofs for example. And of course the theory is threatened not only by Gödel—type incompleteness and the undecidable—but intuitively truth-valued- sentences it throws up; even more devastating indeterminacy looms in the form of ‘concretely undecidable’ sentences such as Tennant’s primality claim of section 5.

One strategy for dealing with these problems is to combine formalism with strict finitism (for one brand of which see Yessinin-Volpin (1961; 1970) and for criticism and commentary Dummett (1975)[^dummett-1975] and Wright (1982)[^wright-1982]: only feasibly long “digestible” tokens—of formulae and of proofs—exist. Formulae with no feasible proofs or disproofs simply lack truth value. Since we know from Gödelian speed-up considerations that for many a provable sentence the shortest derivations of it or its negation are vastly longer than the sentence itself, this finitist/formalism position threatens to cause havoc across large areas of perfectly ordinary mathematics.

Weir argues (2010; 2016) that finitist formalism is not only extremely radical, it is incoherent. The reason is the all-pervasive role of abbreviation which generates complex tokens where most of their subparts will never exist, for example abbreviations which create numerals naming (speaking with the platonist) arbitrarily high numbers. As a result, strict finitist specifications cannot be given in the usual inductive fashion, as the intersection of all inductive sets containing the base set and closed under the complexity-forming operations. And this in turn means we cannot prove even very simple facts about wffs and proof.

Idealisation, then, is essential in metamathematics, including the idealised notions of truth and proof found in metamathematics. If the formalist is entitled to assert there are infinitely many primes, whilst denying abstract objects exist, there seems no reason why she cannot affirm that there are infinitely many formulae or infinitely many proofs, whilst also denying that abstract objects exist. Weir (2016: 38–39)[^weir-2016] therefore argues that the formalist can answer the problem of concrete undecidables so long as there are *concrete* proofs (or proof sketches) of results to the effect that formal truth, for a given language or sub-language, coincides with formal provability, and that there is no reason to restrict idealisation to finitary languages.

In conclusion, the formalist who espouses the meaningfulness and indeed truth of standard mathematical theories, including proof theory for example, has more resources to meet such claims than classic game formalism. The question is whether these are enough to salvage a position which it is fair to say most philosophers of mathematics still think hopeless. There is, on the other hand, certainly no universal consensus that formalism is dead and buried and signs of strong sympathy for formalism among some mathematicians and computer scientists.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=formalism-mathematics). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/formalism-mathematics/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=formalism-mathematics&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/formalism-mathematics/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- [‘Does mathematics need a philosophy?’](https://www.dpmms.cam.ac.uk/~wtg10/philosophy.html), by mathematician Timothy Gowers who presents a highly formalistic approach to mathematics

[Please contact the author with further suggestions.]

## Related Entries

Frege, Gottlob: controversy with Hilbert | Gödel, Kurt | Hilbert, David: program in the foundations of mathematics | mathematics, philosophy of | mathematics, philosophy of: fictionalism | mathematics, philosophy of: Platonism | Wittgenstein, Ludwig: philosophy of mathematics

## Acknowledgements

Many thanks to John L. Bell, Richard Lawrence and the editors of the Stanford Encyclopedia for very helpful feedback.

## Notes（原文脚注）

[^note-1]: Translations from Thomae, 1898 are from Lawrence, 2023.

[^note-2]: Translations from Frege (1903)[^frege-1903][^frege-1903-2][^frege-1903-3] are from the historically important Black and Geach translation of parts of the *Grundgesetze* in the third edition of Black and Geach 1980. But compare also the relevant passages in Philip Ebert and Marcus Rossberg’s monumental translation of the *Grundgesetze*, Frege, 1903/2013.

[^note-3]: Subject to some qualifications with respect to variables free in $M$ being captured in $N$ and where $\lambda x.NM = \lambda x.N$ if $x$ is not free in $N$.

[^note-4]: For a useful account of this history here see (Wadler, 2015)[^wadler-2015] and in particular the notes from Howard quoted therein.

[^note-5]: Where the variable $y$ is not free in $N$, then the result of substituting $M$ for $y$ in $\lambda y.N$, that is $\lambda y.N [y := M]$ is just $N$.

[^note-6]: Here by ‘TT’ I am loosely picking out any type theory with sufficient power, a sort of generic “vanilla” version, not a specific theory.

[^note-7]: A great many even relatively simple truths about fictional characters cannot be extracted in such simplistic way from the relevant body of fiction and such an approach seems to have no chance with more complex examples of fictional discourse such as: “Stepan Oblonsky is less of a villain than Fyodor Karamazov” (Tolstoy and Dostoyevsky never wrote a joint novel in which both characters feature. Would a novel in which characters of those names both occur be “about” them? In what sense? ).

[^awodey-2014]: Awodey, Steve, 2014, ‘Structuralism, Invariance, and Univalence’, *Philosophia Mathematica* (III), 22: 135–159.

[^azzouni-2004]: Azzouni, Jody, 2004, ‘The Derivation-Indicator View of Mathematical Practice’, *Philosophia Mathematica*, (III) 12: 81–105.

[^azzouni-2005]: –––, 2005, ‘How to Nominalize Formalism’, *Philosophia Mathematica* (III), 13: 135–159.

[^azzouni-2006]: –––, 2006, *Tracking Reason: Proof, Consequence and Truth*, Oxford: Oxford University Press (especially Chapter 7).

[^azzouni-2009]: –––, 2009, ‘Why do Informal Proofs Conform to Formal Norms’, *Foundations of Science*, 14: 9–26.

[^barendregt-1984]: Barendregt, H.P., 1984, *The Lambda Calculus*, Amsterdam: North Holland.

[^boolos-1987]: Boolos, George, 1987, ‘A Curious Inference’, *Journal of Philosophical Logic*, 16: 1–12; reprinted in George Boolos, *Logic, Logic and Logic* Cambridge, MA: Harvard University Press, 1998, 376–82.

[^black-1980]: Black, M. and Geach, P, 1980, *Translations from the Philosophical Writings of Gottlob Frege*, Oxford: Blackwell, 3rd edition.

[^carnap-1934]: Carnap, Rudolf, 1934 [1937], *Logische Syntax der Sprache*, Vienna: Springer; translated by A. Smeaton as *The Logical Syntax of Language*, London: Kegan, Paul, Trench, Trubner & Co. 1937.

[^carnap-1950]: –––, 1950/1956, ‘Empiricism, Semantics and Ontology’, *Revue Internationale de Philosophie*, 4: 20–40; reprinted in *Meaning and Necessity*, Chicago: University of Chicago Press, 2nd edition, 1956: 205–221.

[^church-1932]: Church, Alonzo, 1932, ‘A Set of Postulates for the Foundation of Logic’, *Annals of Mathematics*, 33(2): 346–366.

[^church-1940]: –––,1940, ‘A Formulation of the Simple Theory of Types’, *Journal of Symbolic Logic*, 5(2): 56–68.

[^cohen-1971]: Cohen, Paul, 1971, ‘Comments on the foundations of set theory’, in Dana Scott (ed.), *Axiomatic Set Theory: Proceedings of Symposia in Pure Mathematics* (Volume 13), Providence: American Mathematical Society: 9–15.

[^curry-1951]: Curry, Haskell, 1951, *Outlines of Formalist Philosophy of Mathematics*, Amsterdam: North Holland.

[^curry-1958]: Curry, Haskell and Feys, Robert, 1958, *Combinatory Logic*, Amsterdam: North Holland.

[^detlefsen-1993]: Detlefsen, Michael, 1993, ‘Hilbert’s Formalism’, *Revue Internationale de Philosophie*, 47(186): 285–304.

[^detlefsen-2005]: –––, 2005, ‘Formalism’, in Stewart Shapiro (ed.), *The Oxford Handbook of Philosophy of Mathematics and Logic*, Oxford: Oxford University Press, 236–317.

[^dummett-1975]: Dummett, Michael, 1975, ‘Wang’s Paradox,’ Synthese, 30(3/4): 301–324 reprinted in *Truth and Other Enigmaas* London: Duckworth, 248–268.

[^dummett-1991]: –––, 1991, *Frege, Philosophy of Mathematics*, London: Duckworth.

[^field-1989]: Field, Hartry, 1989, *Realism, Mathematics and Modality*, Oxford: Blackwell.

[^floyd-2002]: Floyd, Juliet, 2002, ‘Number and Ascriptions of Number in Wittgenstein’s *Tractatus*’, in *From Frege to Wittgenstein: Perspectives on Early Analytic Philosophy*, Erich H. Reck (ed.), Oxford: Oxford University Press, 308–352.

[^floyd-2000]: Floyd, Juliet and Putnam, Hilary, 2000, ‘A Note on Wittgenstein’s ‘Notorious Paragraph’ about the Gödel Theorem’, *Journal of Philosophy*, 97: 624–632.

[^frege-1903]: Frege, Gottlob, 1903, *Grundgesetze der Arithmetik, Begriffsschriftlich Abgeleitet* (Volume II), Jena: Pohle; reprinted 1962, Hildesheim: George Olms.

[^frege-1903-2]: –––, 1903/1980, ‘Frege Against the Formalists: Vol II of Frege 1903, §§86–137 in Black and Geach (1980): 162–213.

[^frege-1903-3]: –––, 1903/2013, *Basic Laws of Arithmetic*, edited and translated by Philip A. Ebert and Marcus Rossberg, Oxford: Oxford University Press.

[^gabbay-2010]: Gabbay, Michael, 2010, ‘A Formalist Philosophy of Mathematics, Part I: Arithmetic’, *Studia Logica*, 96: 219–238.

[^giaquinto-2002]: Giaquinto, Marcus, 2002, *The Search for Certainty*, Oxford: Clarendon. (See especially 210ff).

[^gödel-1953]: Gödel, Kurt, 1953–9, ‘Is Mathematics Syntax of Language’, in S. Feferman *et al*. (eds.), *Kurt Gödel: Collected Works* (Volume III), New York: Oxford University Press, 1995: 334–362,

[^goldfarb-1995]: Goldfarb, Warren, 1995, ‘Introduction to Gödel’s ‘Is Mathematics Syntax of Language’’ in S. Feferman *et al*. (eds.), *Kurt Gödel: Collected Works* (Volume III), New York: Oxford University Press, 1995: 324–34.

[^goodman-1947]: Goodman, Nelson and Quine, W. V., 1947, ‘Steps towards a Constructive Nominalism’, *Journal of Symbolic Logic*, 12: 97–122.

[^griffin-1990]: Griffin, Timothy, 1990, ‘A Formulae–as–Types Notion of Control’, in *Principles of Programming Languages*, *Association of Computing Machinery*, 47–58.

[^heine-1872]: Heine, Eduard, 1872, ‘Die Elemente der Functionenlehre,’ *Journal für die reine und angewandte Mathematik*, 74: 172–188.

[^hintikka-1956]: Hintikka, Jaakko, 1956, ‘Identity, variables, and impredicative definitions,’ *Journal of Symbolic Logic*, 21: 225–45.

[^howard-1969]: Howard, W.A., 1969, ‘The Formula-as-Types Notion of Construction’, in Seldin, J.P. and Hindley, J.R. (eds.) *To H.B. Curry: Essays on Combinatory Logic, Lambda Calculus and Formalism*, London: Academic Press, 1980: 479–490.

[^hylton-1997]: Hylton, Peter, 1997 ‘Functions, Operations and Sense in Wittgenstein’s *Tractatus*’, in W.W. Tait (ed.), *Early analytic philosophy: Frege, Russell, Wittgenstein: essays in honor of Leonard Linsky*, Chicago: Open Court: 91–106.

[^kaplan-1989]: Kaplan, David, 1989, ‘Demonstratives’, in J. Almog, J. Perry, and H. Wettstein (eds.), *Themes from Kaplan*, New York: Oxford University Press, 481–563.

[^kleene-1935]: Kleene, Stephen, and Rosser, J.B., 1935, ‘The Inconsistency of Certain Formal Logics’, *Annals of Mathematics*, 36: 630–636.

[^landini-2007]: Landini, Gregory, 2007, *Wittgenstein’s Apprenticeship with Russell*, Cambridge: Cambridge University Press.

[^lawrence-2023]: Lawrence, Richard, 2023, ‘Frege, Thomae, and Formalism: Shifting Perspectives’, *Journal for the History of Analytic Philosophy*, 11: 1–23.

[^leng-2010]: Leng, Mary, 2010, *Mathematics and Reality*, Oxford: Oxford University Press.

[^lewy-1967]: Lewy, Casimir, 1967, ‘A note on the text of the *Tractatus*’ *Mind*, 76: 416–423.

[^martin-löf-1975]: Martin-Löf, Per, 1975, ‘An intuitionistic theory of types: Predicative part’, in *Logic colloquium ’73*, H.E. Rose and J. Shepherdson (eds.), Amsterdam: North-Holland: 73–118.

[^potter-2000]: Potter, Michael, 2000, *Reason’s Nearest Kin*, Oxford: Oxford University Press; see especially 10–17 and Chapter 6.

[^resnik-1980]: Resnik, Michael, 1980, *Frege and the Philosophy of Mathematics*, Ithaca: Cornell University Press, 1980.

[^robinson-1965]: Robinson, Abraham, 1965, ‘Formalism’ in Bar-Hillel *et al.* (eds.) *Logic, Methodology and Philosophy of Science*, Amsterdam: North Holland.

[^robinson-1969]: –––, 1969, ‘From a Formalist’s point of view’, *Dialectica*, 23: 45–9.

[^scott-1970]: Scott, Dana, 1970, ‘Constructive Validity’, in *Symposium on Automatics Demonstration (Versailles, December 1968)*, M. Laudet, D. Lacombe, L. Nolin, and M. Schützenberg (eds), *Lecture Notes in Mathematics* (Volume 125), Berlin: Springer, 237–275.

[^shapiro-2000]: Shapiro, Stewart, 2000, *Thinking about Mathematics*, Oxford: Oxford University Press.

[^simons-2009]: Simons, Peter, 2009, ‘Formalism’ in Andrew D. Irvine (ed.), *Philosophy of Mathematics*, Amsterdam: North Holland: 291–310.

[^tennant-1997]: Tennant, Neil, 1997, *The Taming of the True*, Oxford: Clarendon Press.

[^tennant-2008]: –––, 2008, ‘Carnap, Gödel, and the Analyticity of Arithmetic’, *Philosophia Mathematica*, 16: 110–12.

[^thomae-1898]: Thomae, Johannes, 1898, *Elementare Theorie der analytischen Functionen einer complexen Veränderlichen*, 2nd edition. Halle a.d. Saale: Verlag von Louis Nebert.

[^wadler-2015]: Wadler, Philip, 2015, ‘Propositions as Types’, *Communications of the Association for Computing Machinery*, 58: 75–84.

[^wehmeier-2004]: Wehmeier, Kai, 2004, ‘Wittgensteinian Predicate Logic’, *Notre Dame Journal of Formal Logic*, 45: 1–11.

[^weir-1991]: Weir, Alan, 1991, ‘An Instructive Nominalism’: Critical Review of H. Field: *Realism, Mathematics and Modality*, *Philosophical Books*, 32: 17–26.

[^weir-1993]: –––, 1993, ‘Putnam, Gödel and Mathematical Realism’, *International Journal of Philosophical Studies*, 1: 255–285.

[^weir-2010]: –––, 2010, *Truth through Proof: A Formalist Foundation for Mathematics*, Oxford: Oxford University Press.

[^weir-2016]: –––, 2016, ‘Informal Proof, Formal Proof and Formalism’, *The Review of Symbolic Logic*, 9: 23–43.

[^wittgenstein-1921]: Wittgenstein, Ludwig, 1921/1960, *Tractatus Logico-Philosophicus*, D. Pears and B. McGuinness (trans.), London: Routledge and Kegan Paul.

[^wittgenstein-1956]: –––, 1956/1978, *Remarks on the Foundations of Mathematics*, revised edition, G. E. M. Anscombe (trans.), G. E. M. Anscombe, R. Rhees, and G. H. von Wright, (eds.), Oxford: Blackwell.

[^wittgenstein-1975]: –––, 1975, *Philosophical Grammar*, A. Kenny (trans.), Rush Rees (ed.), Oxford: Blackwell.

[^wright-1982]: Wright, Crispin, 1982, ‘Strict Finitism’, *Synthese*, 51: 203–282.

[^yessenin-volpin-1961]: Yessenin-Volpin, A., 1961, ‘Le Programme Ultra-Intuitionniste Des Fondements Des Mathématiques.’ in *Infinitistic Methods, Proceedings of the Symposium on the Foundations of Mathematics*, Oxford: Pergamon Press, 201–23.

[^yessenin-volpin-1970]: –––, 1970, ‘The Ultra-Intuitionistic Criticism and the Antitraditional Program for the Foundations of Mathematics’, in A. Kino, J. Myhill, & R. Vesley (eds.), *Intuitionism and Proof Theory*, Amsterdam: North-Holland, 3–45.
