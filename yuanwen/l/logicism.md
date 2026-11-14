# Logicism and Neologicism
**First published Wed Aug 21, 2013; substantive revision Sat Dec 2, 2023**

*Tennant, Neil*

Logicism is a philosophical, foundational, and *foundationalist* doctrine that can be advanced with respect to any branch of mathematics. Traditionally, logicism has concerned itself especially with arithmetic and real analysis. It comes in a stronger and a weaker version.

The *strong* version of logicism maintains that all mathematical *truths* in the chosen branch(es) form a species of logical truth. The weak version of logicism, by contrast, maintains only that all the *theorems* do. (By ‘theorems’ we mean results that are *provable* within the branch of mathematics in question.) The foundationalism is with respect to those parts of mathematics that the logicist reconstructs. Success in this regard is compatible, however, with a non-foundationalist (e.g., coherentist) view of the parts of mathematics that cannot be so reconstructed.

Both versions of logicism—strong and weak—maintain that

1. *All* the objects forming the subject matter of those branches of mathematics are logical objects; and
2. Logic—in some suitably general and powerful sense that the logicist will have to define—is capable of furnishing definitions of the primitive concepts of these branches of mathematics, allowing one to derive the mathematician’s ‘first principles’ therein as results within Logic itself. (The branch of mathematics in question is thereby said to have been *reduced* to Logic.)

For the foundationalist who accepts Kant’s distinction between analytic and synthetic truth, the truths of logic are paradigm cases of analytic truths. They are true *solely by virtue of the meanings of the linguistic expressions involved* in expressing them; or, as Kant might have preferred it, by virtue of internal relations among the concepts involved. A successful logicist reduction of any branch of mathematics will therefore show that its truths (strong version) or its theorems (weak version) are analytic.

Another consequence of successful logicist reduction of a given branch of mathematics is that mathematical certainty (within that branch) is of a piece with certainty about logical truth. The same holds for necessity; and for the *a priori* character of the knowledge concerned.

Logicist doctrines were espoused in two main forms—Fregean and Russellian—until around 1930, at which point logicism went into decline, largely because of the discovery of Gödelian incompleteness, and the ascendancy of Zermelo-Fraenkel set theory, which displaced the Russellian theory of types as the most promising foundational theory for mathematics. The doctrine of *neo-logicism* subsequently revived some of the core ideas of logicism, with its first hints appearing in the mid-1960s, and its more substantive contributions beginning in the 1980s.

The main technical and philosophical innovation of the *neo*-logicists is their use of *abstraction principles* in order to secure the existence of such things as numbers, understood, with Frege, as *logical* objects. One favored kind of abstraction principle typically effects the reification of equivalence classes of an equivalence relation.[^note-1] One of Frege’s favorite examples involved the equivalence relation of parallelism among lines. The relevant abstraction would be that of the *direction* of a line. Thus, two lines $l_1$ and $l_2$ have *the same direction* just in case they are parallel:

$$d(l_1) = d(l_2) \Leftrightarrow l_1 || l_2.$$

The function denoted by the abstraction operator $d(\,)$ is here applied to lines, and produces *directions* (new abstract objects) as its values. Note that the abstraction operator can take variables as arguments.

The neo-logicists characterize abstraction operators that produce *numbers* as their values. Details of notation and method will be provided in due course.

There has not been any historical trend discernible as an *evolution* of the doctrine of logicism, with incremental adjustments to deal with occasional problems as they arose, while maintaining a reasonably stable trajectory towards an ideal formulation. Rather, the doctrine has been characterized by abrupt shifts as far as methods and materials are concerned, even if the goal has remained relatively constant through such changes.[^note-2] We shall allow the pattern of change to become evident as the different phases of logicism are recounted below.

## 1. Historical background

Kant had held that both arithmetic and (Euclidean) geometry were synthetic *a priori*, just as—for him—metaphysics was. Indeed, this was to explain the special status of both mathematics and metaphysics, so that the latter could enjoy the exalted status of the former. For Kant, both mathematics and metaphysics afforded informative insights into the nature of reality (they were synthetic); yet, for all that, the rational intellect needed no sensory experience in order to attain such insights (they were *a priori*). On Kant’s account, even a simple computational statement of arithmetic—let alone a statement involving quantification over the natural numbers—is synthetic. Here is how he put the matter in his *Critique of Pure Reason*, at B16:

> We might, indeed, at first suppose that the proposition $7 + 5 = 12$ is a merely analytical proposition, and follows by the principle of contradiction from the concept of a sum of $7$ and $5$. But if we look more closely we find that the concept of the sum of $7$ and $5$ contains nothing save the union of the two numbers into one, and in this no thought is being taken as to what that single number may be which combines both. The concept of $12$ is by no means already thought in merely thinking this union of $7$ and $5$; and I may analyze my concept of such a possible sum as long as I please, still I shall never find the $12$ in it. (Translation by Norman Kemp Smith)

Kant’s search for conceptual containments is confined to those that he might be able to find among just the explicit constituents of the proposition concerned, unmediated by any connections with related concepts that do not themselves occur within the proposition. (We note this in anticipation of a contrast to be made in due course with Frege’s modification of Kant’s conception of analytic truth.)[^note-3] For Kant, the *a priori* character of arithmetical truth derives not from conceptual containments (within the proposition in question), but from the *pure form of our intuition of time*, as affording an unbounded series of successive moments. According to Michael Friedman, Kant held that

> only the general features of succession and iteration in time can guarantee the existence and uniqueness of the sum of $7$ and $5$ …; only the unboundedness of temporal succession can guarantee the infinity of the number series, and so on ….[^note-4]

Likewise, on Kant’s account, the *a priori* character of Euclidean geometry derives from the *pure form of our intuition of space*, which enables the thinker, correctly one may presume, to intuit straight lines in space as continuous.

These two pure forms of intuition—time and space—delivered, for Kant, the theories of arithmetic and Euclidean geometry respectively, and endowed them both with their *a priori* character. And they made possible the spatio-temporal manifold of intuitions (*Anschauungen*) which would then in turn, upon structuring by the exercise of concepts of the understanding (especially the concepts of *substance* and *cause*) make possible objective knowledge of things and events in the external world.

The logicists, then, could be seen as adopting Kant’s distinction, but applying it to radically different effect. Their first move was to argue that *arithmetic*, at least, is *analytic*, not synthetic.

The doctrine of logicism had its first glimmerings in the writings of Dedekind, but it really only came to full flowering in the work of Frege. In Dedekind’s work, the ideas were presented in a form accessible to his contemporaries in the mathematical community. Precise and rigorous though those ideas were, they nevertheless enjoyed a relatively informal presentation. No one had yet come up with the idea of formal deductive systems of logic adequate for formalizing the mathematical reasoning of their day; so no logicist thesis in Dedekind’s day could be formulated in the way that is now familiar to us. Matters were different, of course, with Frege, for his crowning achievement was a formal deductive system of logic by reference to which a logicist thesis could at last be expressed.

Now, when crediting Frege also with the pioneering of a detailed execution of a logicist program, one cannot ignore his continuing insistence that the truths of Euclidean geometry were *synthetic a priori*, and founded in a completely different way from the truths of arithmetic.[^note-5] Hence they were not subject to his doctrine of logicism. This is why we have exercised care in our introductory characterization of the doctrine of logicism, as concerned first and foremost with the truths of arithmetic and of real analysis.

The combined contributions of Dedekind and Frege represented a culmination of the trend, by their time well under way among leading mathematicians, towards the *arithmetization* of real (and complex) analysis. This trend had its beginnings in the even earlier works of Gauss and Bolzano. It came to maturity in the works of Cauchy and Weierstraß, and became the dominant paradigm in Western thought about the nature of mathematics. The leading idea of the arithmetizers was that the concepts and first principles of arithmetic and analysis are to be found in the concepts of the understanding (as a Kantian might put it), independently of one’s geometric intuitions concerning any spatial or temporal continua. Arithmetic and analysis are completely *conceptual* and *logical* in their axiomatic sources and in their deductive development.

We proceed now to consider Dedekind and Frege in turn.

### 1.1 Dedekind

It is fair to say that Dedekind enabled the trend of arithmetization to culminate in the doctrine of logicism. The recommendation (or statement of the methodological maxim) that one *ought* to avoid all matters geometric when providing a foundation for real analysis goes back at least to Dedekind, *Stetigkeit und Irrationale Zahlen* (1872). This work was published late. Its breakthrough idea had come fourteen years earlier, in 1858.[^note-6] At pages 3–4 Dedekind writes in an engaging and revelatory way of his earlier struggle in the autumn of 1858 to furnish “*eine wirklich wissenschaftliche Begründung der Arithmetik*” (a really scientific foundation for Arithmetic [i.e., real analysis]).[^note-7]

It is clear that Dedekind is writing on the *presumption*—assumed to be so widespread as not to call for any justificatory argument—that one should have *no recourse at all* to geometric intuitions or first principles when founding the theory of the real numbers. This presumption, said Dedekind, ‘no one will deny’. Dedekind wanted “a *purely arithmetical* and perfectly rigorous foundation for the principles of infinitesimal analysis” [Emphases added].[^note-8]

The presumption receives further emphatic statement in Dedekind’s later work (1888) *Was sind und was sollen die Zahlen?*, which, like the earlier work, was published much later than it could (or should) have been. In the preface to the first edition (Dedekind 1996b: 790–1)[^dedekind-1996b] Dedekind writes

> In speaking of arithmetic (algebra, analysis) as merely part of logic I mean to imply that I consider the number-concept *entirely independent of the notions or intuitions of space and time*—that I rather consider it an immediate product of the pure laws of thought.… It is only through the purely logical process of building up the science of numbers and by thus acquiring the continuous number-domain that we are enabled accurately to investigate our notions of space and time by bringing them into relation with this number-domain created in our mind.[fn] [Emphasis added]

Once again we see the presumption at work: in laying a foundation for the theory of real numbers, one *must avoid* any recourse to geometrical intuition. To inquire how such a presumption become so widespread, and in whose works it originated, is a topic outside the scope of the present study.

### 1.2 Frege

It is clear from Frege’s Preface to his *Begriffsschrift* (at pp. IX–X) that he shared Dedekind’s methodological concerns, and that he had an eventual logicist treatment of arithmetic in his sights when devising his concept script. Frege distinguished two kinds of truths that require a *Begründung* (justification): those whose proofs could proceed purely logically; and those which had to be supported by experiential facts (*Erfahrungsthatsachen*). And he sought to inquire how far one could succeed in capturing arithmetic by means only of inferences based on the laws of thought that transcend all particularities (“*durch Schlüsse allein …, nur gestützt auf die Gesetze des Denkens, die über allen Besonderheiten erhaben sind*”). He made it clear that he wished to get at the root concept of *ordering in a series*, and to advance from there to the concept of number. Then comes this unmistakeable echo of Dedekind:

> In order that, in doing this, nothing intuitive could intrude unnoticed, everything would turn on there being no gaps in the chain of inferences.
>
> *Damit sich hierbei nicht unbemerkt etwas Anschauliches eindrängen könnte, musste Alles auf die Lückenlosigkeit der Schlusskette ankommen.*

Frege stressed that he was concerned to reveal how the analyticity of arithmetical truths derived from their justifications. In §3 of Frege 1884 (*Grundlagen der Arithmetik*) he wrote

> … these distinctions between a priori and a posteriori, synthetic and analytic, concern … the justification for making the judgement. … When a proposition is called … analytic in my sense, … it is a judgement about the ultimate ground upon which rests the justification for holding it to be true.
>
> … The problem becomes … that of finding the proof of the proposition, and of following it up right back to the primitive truths. *If, in carrying out this process, we come only on general logical laws and on definitions, then the truth is an analytic one*, bearing in mind that we must take account also of all propositions upon which the admissibility of any of the definitions depends. [Emphasis added]

We see, then, that Frege’s conception of the analytic was suitably broader than Kant’s. Kant required that conceptual containments be evident within the sentence, rather than that the sentence be displayed as a conclusion following logically from axioms whose own logical or conceptual truth was self-evident, and which might contain expressions not occurring in the sentence in question. As we saw from the quote from B16, Kant did not regard ‘$7 + 5 = 12$’ as an analytic truth. The Fregean, by contrast, is able to exploit the internal structure of the numerals, and to invoke the recursion axioms for addition (which themselves would have to have been derived in logicist fashion).[^note-9] So, for the Fregean, even if not for Kant, ‘$7 + 5 = 12$’ is an analytic truth. Where $s$ is the successor function, Kant’s example takes the more detailed form $$sssssss0 + sssss0 = ssssssssssss0,$$ which is provable using the recursion axioms

$$\begin{align} &\forall x(x + 0 = x); \\ &\forall x\forall y(x + sy = s(x + y)). \end{align}$$

The latter axiom justifies each of the transitions below:

$$\begin{align} sssssss0 + sssss0 &= s(sssssss0 + ssss0) \\ &= s(s(sssssss0 + sss0)) \\ &= s(s(s(sssssss0 + ss0))) \\ &= s(s(s(s(sssssss0 + s0)))) \\ &= s(s(s(s(s(sssssss0 + 0)))) \end{align}$$

At this point the former axiom secures

$$ s(s(s(s(s(sssssss0 + 0))))) = s(s(s(s(s(sssssss0))))) $$

Hence (suppressing parentheses) we have

$$ sssssss0 + sssss0 = ssssssssssss0, $$

as foreshadowed.[^note-10]

Frege went on in this work to give his famous elucidation of ‘number of’ as a concept of concepts, along with devastating critiques of rival accounts of number by contemporaries in the grip of psychologism, empiricism, or formalism. He kept technicalities to a minimum, in a *tour de force* of philosophical elucidation.

#### 1.2.1 Numbers as higher-level concepts

Frege’s key insight, which he never abandoned, was first expressed in §46: “… the content of a statement about number is an assertion about a concept”. By way of illustration: Suppose one states that

**$(\nu)$**

The number of apples in the basket is (i.e., *is identical to*) the number 2.

$(\nu)$ is definitely a statement ‘about number’. Yet all one is saying, when asserting $(\nu)$, is that

**$(\gamma)$**

There are exactly two apples in the basket.

For Frege, $(\gamma)$ is an assertion about the *concept* “___is an apple in the basket”. It is not an assertion about the number 2, since the *adjectival* occurrence of ‘two’ in $(\gamma)$ can be avoided. One could re-phrase $(\gamma)$ as

**$(\gamma')$**

There is an apple in the basket, and another apple in the basket, and they are the only apples in the basket.

We shall show how Frege’s point here can be made watertight, and general, after providing a few words of explanation about notation for number-abstraction.

In the simple example above about line-directions, the abstraction operator $d(\,)$ is a function sign, and does not bind any variables. But with *numerical* abstractions, matters are subtly different. Here, the abstraction operator $\#$, meaning “the number of …”, can be deployed in two different ways. On the one hand, it can be a function symbol: if $F$ is a predicate (resp., a second-level variable), then $\#F$ is a singular term denoting the number of things falling under $F$ (resp., in the extension assigned to the second-level variable).[^note-11] On the other hand, the operator $\#x$ can be applied to the open sentence $\Phi(x)$ with $x$ free, thereby binding the variable $x$. The complex term thus formed is read as “the number of $\Phi$s”.[^note-12]

With that explanation of notation in place, suppose one makes a statement about number of the following form, where $\#xFx$ is the formal rendering of “the number of $F$s”:

$$\# xFx = 2.$$

Then one is thereby (says Frege) making the assertion that

$$\exists x\exists y(x\ne y \wedge Fx \wedge Fy \wedge \forall z(Fz \rightarrow(z = x \vee z = y))).$$

The concept $F$ is the only one finding expression in this last assertion, apart from standard logical operators. Therefore the assertion is about the concept $F$. It is in the general form of a *numerosity assertion*, which does not necessarily refer to, or generalize about, numbers. For arbitrary $n$, the logical form in question will be

$$\exists x_1 \ldots \exists x_n (\wedge_{1\le i\lt j\le n} x_i \ne x_j \wedge_{1\le i\le n} Fx_i \wedge \forall z(Fz \rightarrow \vee_{1\le i\le n} z = x_{i})).$$

Of course (returning to our example where $n = 2$), one can consider matters in the converse logical direction. If one makes the numerosity assertion first, then one can regard that as a justifying ground for the subsequent statement that the number of $F$s is identical to 2.

If, with Frege, we countenance these two different ways of ‘carving’ one and the same propositional content, then we shall require, in whatever language is rich enough to provide the two forms of expression in question, the following logical equivalence, indicated by the two-way deducibility sign $\dashv \vdash$:

$$ \#xFx = 2 \dashv \vdash \exists x\exists y(x \ne y \wedge Fx \wedge Fy \wedge \forall z(Fz \rightarrow(z = x \vee z = y))). $$

As Frege put it, the propositional content on the right-hand side has been ‘re-carved’ as the identity statement on the left-hand side. One and the same thought has been presented in two very different ways. They have the same truth conditions, but different logico-grammatical forms.

The form on the right, within a language devoid of the operator $\#$, is completely innocent of any commitment to numbers as objects. If such a language is extended, however, by adding $\#$ to its stock of logical expressions, then one is thereby able to express the form on the left, which is number-committal.

By being aware that the concept-numerosity thought on the right can be rendered equivalently (in the extended language) as the number-committal thought on the left, one comes to recognize numbers as abstract, logical objects. In the extended language, their existence can be established on purely logical grounds.

#### 1.2.2 Hume’s Principle and the Caesar Problem

In the *Grundlagen*, Frege considered the following equivalence, known as *Hume’s Principle*:

$$\tag{HP} \# xFx = \# xGx \leftrightarrow \exists R(R \text{ maps the \(F\)s 1-1 onto the \(G\)s}).$$

There are two important features to note.

First, HP is explicitly *second order* on the right-hand side, involving, as it does, a second-order quantification over relations $R$; and HP is *purely logical* on the right-hand side. Here, the notion to be defined (the *definiendum*) is that of a relation $R$ mapping the $F$s 1-1 onto the $G$s. This can be spelled out in purely logical terms: every $F$ bears $R$ to exactly one $G$, and every $G$ is borne $R$ by exactly one $F$. In symbols, this *definiens* reads as follows:

$$\begin{align} \forall x(Fx &\rightarrow \exists y\forall z(z = y \leftrightarrow (Gz \wedge Rxz))) \\ &\wedge \forall x(Gx \rightarrow \exists y\forall z(z = y \leftrightarrow (Fz \wedge Rzx))), \end{align}$$

which we shall abbreviate as[^note-13]

$$ Rxy[Fx \underset{\text{onto}}{\overset{1\text{-}1}{\mapsto}} Gy]. $$

Secondly, HP involves two predicates, $F$ and $G$. It does so in order to state an important *criterion of identity* for numbers denoted, respectively, as $\# xFx$ and as $\# xGx$. Note that both terms in the identity-statement on the left-hand side are abstractive terms.

Let us call (neo-)Fregean abstraction principles (like HP) that seek to specify the truth conditions of identities involving *two* distinct abstractive terms (involving the same abstraction operator @) *double-barreled abstraction principles*. (Contrasting single-barreled abstraction principles for identities will be discussed shortly.)[^note-14] Double-barreled abstraction principles have the general form

$$ @xFx = @xGx \leftrightarrow \Psi(F,G), $$

where the right-hand side expresses a second-order equivalence relation $\Psi$ between $F$ and $G$, and is stated without use of $ @$. But that does not preclude instances of such a principle where either $F$ or $G$, or both, contain occurrences of $@$.

Typically these double-barreled abstraction principles are laid down as postulates, or axioms (or axiom schemes). But that is not absolutely necessary. All that is important is whether the theory in question contains such a principle as a theorem (or theorem-scheme). Like the earlier abstraction principle for directions, HP is a double-barreled abstraction principle. So too is Frege’s ill-fated Basic Law V, which we shall discuss in due course.

HP tells us that the numbers $\#xFx$ and $\# xGx$ will be identical *if and only if* the predicate-extensions that they respectively number are in one-one correspondence (under some two-place relation $R)$. Another way of expressing this latter condition is to say that $F$ and $G$ are *equinumerous*.

The basic idea of this equivalence is owed to Hume (whence the current name of the principle); and it had of course been exploited to great effect by Cantor, well before Frege wrote the *Grundlagen*.[^note-15] Without the use of one-one correspondences in this way, Cantor would not have been able to motivate his later groundbreaking idea that there are distinct infinite numbers (see Cantor 1891)[^cantor-1891].

Frege considered whether HP might be laid down as a constitutive definition of numbers—a definition that would give a full and exact characterization of their nature. But he concluded that HP could not meet this more exigent, yet reasonable, demand. The reason is what has now become known as the *Julius Caesar Problem*. Frege insisted (*Grundlagen*, §56), that our definition of number should enable us to decide that Julius Caesar is *not* a number. His conclusion was that HP could not enable us to do this.

For, suppose we say that if there are exactly two apples in the basket, then the number of apples in the basket is Julius Caesar. For the sake of consistency, it would be enough (in conformity with HP) simply to make sure that one assigns the same number (i.e., Julius Caesar) to any other concept that is in one-one correspondence with the concept “…is an apple in the basket”. Thus, for example, the number of prime numbers strictly between 4 and 8 is Julius Caesar. Indeed, the number of prime numbers strictly between 1 and 4 is Julius Caesar, one of those prime numbers being Julius Caesar himself!

On the one hand, HP is, to be sure, a necessary condition on number. It must be satisfied by any licit interpretation of the abstraction operator $\#$. HP is not, however, *sufficient* to ensure that the things denoted by terms of the form $\# xFx$ *really are numbers!*

On the other hand—as revealed in Frege’s painstaking deductive work—HP suffices for a logicist derivation of the Dedekind-Peano postulates for the arithmetic of natural numbers. This is what accounts for the vaunted status of HP in certain subsequent neo-logicist accounts (see §2).

But Frege wanted more than just a logically powerful enough source for arithmetic; he wanted, in addition, a principle that would account for the *metaphysical* nature of numbers. They must, surely, at least be *abstract*? Numbers are also eternal and necessary. They are not located in space, and they do not enter into any causal interactions. Frege therefore sought a deeper logical theory that might be able to vouchsafe for numbers these latter characteristics, and thereby solve the Caesar Problem.

Unfortunately, in this regard he arguably failed (and did so quite independently of Russell’s Paradox, of which more in due course). Frege thought (mistakenly, according to Dummett (1998)[^dummett-1998]) that he could avoid the Julius Caesar problem by identifying numbers as special kinds of *classes*, or *extensions* (of concepts). In the *Grundlagen*, at §68, he wrote

> My definition [of Number] is … as follows:
>
> > the Number which belongs to the concept $F$ is the extension [*Umfang*][fn.] of the concept “equal [*gleichzahlig*] to the concept $F$”.

And the footnote to “*Umfang*” ends with the sentence “I assume that it is known what the extension of a concept is.” For those who nevertheless needed some instruction in this regard, the *Grundgesetze* were intended to supply it.

The Julius Caesar problem would, in principle, bedevil any double-barreled abstraction principle. (It is not a problem specifically for *logicism*; it is a problem for abstraction principles of a specific form.)[^note-16] The problem can be avoided by using single-barreled abstraction principles.

The general form of a single-barreled abstraction principle, when expressed by a sentence rather than by rules of inference, is

$$ t = @xFx \leftrightarrow \ldots t \ldots F\ldots, $$

where $t$ is a placeholder for *singular terms in general* (including parameters), and not just for $@$-terms. The right-hand side may contain occurrences of $@$; moreover, when taking instances, expressions substituted for either $F$ or $t$ may contain occurrences of $@$. And all that is important with a single-barreled abstraction principle is whether the theory in question contains it as a theorem (or theorem-scheme).

Some examples of single-barreled abstraction principles are the following. Here, $\exists !t$ is short for $\exists x x = t$. It may be read as “$t$ exists”.

For definite descriptions (on Smiley’s treatment, Smiley 1970)[^smiley-1970]:

$$ t = \iota xFx \leftrightarrow(\exists !t \wedge \forall x(x = t \leftrightarrow Fx)). $$

For set abstracts:[^note-17]

$$ t = \{x\mid Fx\} \leftrightarrow(\exists !t \wedge \forall x(x \in t \leftrightarrow Fx).$$

For number-abstracts (on Tennant’s treatment—see §4):

$$ t = \# xFx \leftrightarrow \exists R\exists G(Rxy[Fx 1\text{–}1 Gy] \wedge t = \# xGx).$$

For number-abstracts (on Zalta’s treatment—see §5):[^note-18]

$$ t = \#G \leftrightarrow t = \iota x(Ax \wedge \forall F(xF \leftrightarrow F \text{ is equinumerous with } G)).$$

The important feature of single-barreled abstraction principles of the kind on which we are focusing is that they are free of ontological commitment. Theories that postulate or prove them need to be supplemented with specific further ontologically committal postulates before incurring commitment to the sort of entities whose broad logical behavior is captured by a single-barreled abstraction principle. For example, the set-abstraction principle above merely places constraints on how sets, membership (‘$\in$’) and set-defining conditions $F$ interrelate. It logically implies both extensionality and the conversion schemata (“If $u$ is a member of the set of all and only $F$s, then $u$ is an $F$”, and “If $u$ is an $F$, and the set of all and only $F$s exists, then $u$ is a member of it”), but does not guarantee the existence of any *sets*—not even that of the empty set.

#### 1.2.3 The *Grundgesetze*

The heart of Frege’s logicist achievement was deferred to the *Grundgesetze der Arithmetik*, the first volume of which appeared in 1893. This almost decade-long delay after the *Grundlagen* he explained in his foreword as being occasioned by some re-thinking of his *Begriffsschrift* (Frege 1879)[^frege-1879]—the most important innovation being the introduction of the notion of, and notation for, the *Werthverlauf* (value-range, or extension) of a concept. Frege had also, by the time of publication of the *Grundgesetze*, formulated his distinction between sense and reference, and decided to treat truth-values as objects, and indeed as referents of sentences.

He confessed that he expected his symbolism to be a *grosses Hemmniss* (great obstacle) standing in the way of the spread and impact of his ideas (Frege 1893: x)[^frege-1893]. On the one hand, the exacting notation and absolutely rigorous and logically watertight proofs were essential to his logicist project. On the other hand, he feared, mathematicians would think *metaphysica sunt, non leguntur!* (it’s metaphysics, and is not [to be] read!), and philosophers would think *mathematica sunt, non leguntur!* (it’s mathematics, and is not [to be] read!); (Frege 1893: xii)[^frege-1893]. Poor Frege might have been right. But the reason why the beef of his *Grundgesetze* was never properly digested can be read off the sandwiching. His foreword to Volume I ends with the confident words

> The only refutation I would acknowledge would be if someone actually showed that a better and more sustainable edifice could be erected on other foundational convictions, or if someone were to show that my axioms led to obviously false consequences. But no one will succeed in doing that. (Frege 1893: xxvi; author’s translation)[^frege-1893]

This confident statement belies somewhat his own prescient misgiving expressed a few pages earlier, over his Basic Law V:

> As far as I can see, controversy could arise only over my Basic Law of Value-ranges (V), which perhaps has not been given special expression by logicians, even though one thinks of it, for example, when one talks of extensions of concepts. I hold it to be purely logical. Anyway, this marks the place where the decision must fall. (Frege 1893: vii; author’s translation)[^frege-1893]

And fall it did. Frege, it turned out, had gone in for overkill with the formal system that was to vindicate his logicism. He sought to unify all of arithmetic and analysis within a general theory of *classes*, or extensions (of concepts). Classes were supposed to be logical objects *par excellence*. The strategy was to define the natural numbers, say, as particular classes within a much more capacious universe of abstract, logical objects. Using the definitions, one would then derive the first principles of arithmetic (the Dedekind-Peano axioms, say) as theorems within the theory of classes. To that end one would exploit, ultimately, only the deeper underlying axioms (or basic laws) governing classes themselves. For more details on this strategy, see §1.2.4.

Among these deeper axioms was Frege’s ill-fated Basic Law V. This, like HP, is a double-barreled abstraction principle. Basic Law V, however, allows for the abstraction of *classes*, and the equivalence relation by which this is effected is the relation of coextensiveness among defining predicates. Frege never raised the Julius Caesar objection against his Basic Law V. Using modern notation, Basic Law V can be stated as the following axiom schema, in which $\Phi$ and $\Psi$ are placeholders for formulas:

$$ \tag{Basic Law V} \{x\mid \Phi x\} = \{x \mid \Psi x\} \leftrightarrow \forall x(\Phi x \leftrightarrow \Psi x). $$

Frege was assuming a ‘logically perfect’ language, in which every well-formed term—including any class-abstractive term of the form $\{x\mid \Phi x\}$—denotes. If, by contrast, one countenances the possibility that certain well-formed singular terms in one’s language might *not* denote objects, then one has to employ a different kind of logic—a so-called *free* logic. (It is ‘free’ of the background assumption that all singular terms denote.) Such a logic qualifies the quantifier rules with ‘existential presuppositions’ concerning the terms involved. For example, instead of being able to infer directly from “for all $x, F(x)$” to “$F(t)$”, as one may, when using the *un*free logic of a logically perfect language:

$$\frac{\forall xF(x)}{F(t)}$$

one needs, in the case of a free logic dealing with possibly non-denoting terms, to ensure that the singular term $t$ denotes:

$$ \frac{\forall xF(x) \qquad \exists !t}{ F(t)} $$

The reader is reminded that $\exists !t$, to be read “$t$ exists”, is short for $\exists x\, x = t$. Similar modifications are required for the other quantifier rules.

Even if Frege had *not* been assuming a logically perfect language, and had instead been using a free logic, Basic Law V would still have committed him to the existence of the class of all $\Phi$s, whatever the defining formula $\Phi$ might be. The proof proceeds as follows.

**Proof.** Note, first, that it is a logical truth that

$$ \forall x(\Phi x \leftrightarrow \Phi x). $$

By Basic Law V in the right-to-left direction, taking $\Phi$ for $\Psi$, it follows that

$$ \{x \mid \Phi x\} = \{x \mid \Phi x\}. $$

But in free logic, an identity holds only if its terms denote. Hence

$$ \exists y(y = \{x \mid \Phi x\}). $$

$\Box$

This schema is known nowadays as ‘Naïve Comprehension’. (Comprehension is the abstraction of sets or classes.) Basic Law V committed Frege to claiming that, corresponding to *any* defining predicate $\Phi$, there exists the class of all and only those things that satisfy $\Phi$.

Note that *any* double-barreled abstraction principle for an abstraction operator $@$, whose right-hand side

1. adverts to concepts or predicates $\Phi$ and $\Psi$ and
2. is logically true upon taking $\Phi$ for $\Psi$,

will generate existential commitment to a denotation for any well-formed abstract term $@x\Phi x$. This is because, in light of (ii), the self-identity $@x\Phi x = @x\Phi x$ will also be logically true. And $@x\Phi x = @x\Phi x$ is true only if $\exists!@x\Phi x$. This consideration holds for *any* defining predicate $\Phi$. This invites the objection, raised both by Tennant (1987: 236)[^tennant-1987] and by Boolos (1987: 184)[^boolos-1987] that in certain conspicuous cases there is no *a priori* justification for commitment to the existence of denotations for these terms, in the case of particularly problematic concepts $\Phi$ (such as self-identity). This was the earliest form of the ‘Bad Company objection’.[^note-19]

#### 1.2.4 Frege’s treatment of the natural numbers

We shall not dwell on the peculiarities of Frege’s class theory, but shall try instead to set out the overall shape of the leading ideas in Frege’s account, as they were set forth informally in the *Grundlagen* and executed formally in the *Grundgesetze*.

First Frege had to identify $0$, which he defined as the number of any empty concept. A necessarily empty concept is that of *non-self-identity*:

$$ 0 =_{df} \#x(x \ne x). $$

Next Frege had to specify what it was for one natural number to be the *successor* of another, or the *next largest* natural number. How might one define what it is for $m$ to *immediately succeed* $n$? The answer is found by appeal to concepts $F$ and $G$, say, that respectively enjoy $m$ and $n$ as their (finite) cardinals. There must be exactly one more object falling under the concept $F$ than there are objects falling under the concept $G$. And *this* will consist in there being a one-one correspondence $(R$, say) between all the $G$s and all but one of the $F$s. Formally:[^note-20]

$$ \begin{align} m &\text{ immediately succeeds } n \leftrightarrow \\ &\ \exists G(n = \# xGx \wedge \exists F(m = \# xFx \\ &\ \wedge\ \exists R \exists y (Fy \wedge Rzw[Gz \underset{\text{onto}}{\overset{1\text{-}1}{\mapsto}} (Fw \wedge w \ne y)]))). \end{align}$$

It is easy to show that $n$ has exactly one immediate successor. That is, if $m$ immediately succeeds $n$, and $m'$ immediately succeeds $n$, then $m = m'$.

What, now, can we say about the extension of the concept ‘natural number’? It must consist of 0 along with any number than can be reached from 0 by *finitely many* steps of immediate succession. This characterization, however, threatens to be circular: for, how is one to understand the adverb ‘finitely’ here, if not by appeal to the notion of natural number itself?

Frege’s genius revealed itself in the solution he devised to this circularity problem. He had already covered the necessary logical and conceptual ground in his *Begriffsschrift* of 1879. For any two-place relation $R$, Frege had defined what it was for $x$ to be *an $R$-ancestor of $y$* (abbreviated here as $R^* xy)$. For this definition, he had employed two ancillary notions. The first was that of a concept $F$ being *$R$-hereditary*:

$$ \forall x\forall y(Fx \rightarrow (Rxy \rightarrow Fy)). $$

Let us abbreviate this as

$$ \mathcal{H}xy(Fx, Rxy). $$

The second ancillary notion we shall express here as “$x$ is $R$-barred by $F$”, or “$F$ $R$-bars $x$”, and it is defined thus:

$$ \forall z(Rxz \rightarrow Fz). $$

Let us abbreviate this as

$$ \mathcal{B}z(Rxz,Fz). $$

Now we are in a position to give Frege’s definition of the ancestral relation $R^* xy$ as follows:

$$ \forall G(\mathcal{H}vw(Gv, Rvw)\rightarrow (\mathcal{B}z(Rxz,Gz) \rightarrow Gy)). $$

This tells us that $y$ falls under any concept $G$ that is $R$-hereditary and $R$-bars $x$.

Still following Frege, one can then define $Nx$ (“$x$ is a natural number”) as short for

$$ 0 = x \vee \text{successor}^* 0x. $$

The relation $Rxy$ on which Frege focuses is that of $y$ (immediately) succeeding $x$. This has the further advantage of being a *function*, i.e., a many-one relation. This enabled Frege to prove that the ancestral of successor is *linear*:

$$\begin{align} \forall x\forall y\forall z((\text{successor}^* xy &\wedge \text{successor}^* xz)\\ &\rightarrow\ (y = z \vee \text{successor}^* yz \vee \text{successor}^* zy)). \end{align}$$

This definition of $Nx$ secures the desired result: every natural number is but finitely many steps of immediate succession away from 0. Ancestralization captures the notion ‘finitely many’ without invoking the notion of natural number, and indeed serves as an independent logico-conceptual basis for the definition of the notion of natural number itself. Note also that it is an essentially second-order notion.

Given the functional character of the relation of immediate succession, one can write $m = sn$ when $m$ immediately succeeds $n$. One especially important consequence of Frege’s definition of $Nx$ is that it enables one to prove, as a *purely logical result*, the Principle of Mathematical Induction:

$$ \forall F(F0 \rightarrow(\forall x((Nx \wedge Fx) \rightarrow Fsx) \rightarrow \forall z(Nz \rightarrow Fz))). $$

So too could Frege derive, logically, all the other Dedekind-Peano postulates (involving the name 0 and the successor function-sign $s$) for the natural numbers.

The most important of these remaining postulates is the one saying that every natural number has a unique (immediate) successor. In order to prove this in full generality, Frege had of course to take into account the possibility that an arbitrarily given natural number might far exceed the size of any collection of physical objects in the universe. To what concept, then, could he turn (for a given natural number $n)$, whose cardinality would be the successor of $n$?

His answer has earned the label ‘Frege’s trick’. The sought concept would be none other than ‘successor$^* xn$’, i.e., “$x$ is a natural number preceding or identical to $n$”. The natural numbers relentlessly generate ever more of their kind, as soon as we try to count them. *This* is why there are infinitely many of them. The idea that each natural number tallies its predecessors in the series of natural numbers was fully formed in the *Grundlagen*, at §82, and rigorously executed in Volume I of the *Grundgesetze*, at §§114–119.

By the time of the *Grundgesetze*, Frege had settled on an explication of cardinal numbers in class-theoretic terms, which would preserve the structure of the foregoing considerations. The number of $F$s (i.e., the cardinal number of the class of all $F$s) was identified as the class of all classes that are equinumerous with (i.e., in 1–1 correspondence with) the class of all $F$s.[^note-21] Thus the class of all $F$s is a member of its own cardinal number. So too is any class that is equinumerous with the class of all $F$s. Thus the cardinal number of any one-membered class is the class of all one-membered classes; the cardinal number of any two-membered class is the class of all two-membered classes; … and so on. It is easy to see that, on Frege’s class-theoretic definition of cardinal number, any two equinumerous classes have the same cardinal number. And numbers are not *sui generis*, but are rather classes of a very special kind. See also the Encyclopedia article on Frege’s Theorem and Foundations for Arithmetic.

#### 1.2.5 Russell’s Paradox

In the language of modern logic, supplied with the binary predicate $\in$ of membership, Frege’s principle of naïve comprehension, to which he was committed by Basic Law V in the *Grundgesetze*, can also be rendered as the following schema:

$$\exists x\forall y(y \in x \leftrightarrow \Phi y).$$

Russell’s famous paradox ensues.

> **Proof.** For $\Phi$y in the foregoing expression of naïve comprehension, take $y \not\in y$ (non-self-membership). One thereby obtains
>
> $$\exists x\forall y(y \in x \leftrightarrow y \not\in y).$$
>
> Let $r$ be such an $x$. So
>
> $$\forall y(y \in r \leftrightarrow y \not\in y).$$
>
> But $r$ is an object within the scope of this generalization. Instantiating with respect to $r$, one obtains
>
> $$r \in r \leftrightarrow r \not\in r.$$
>
> But one can show in short order, within a very weak propositional logic, that any statement of the form
>
> $$A \leftrightarrow \neg A$$
>
> is inconsistent.[^note-22] So Frege’s Basic Law V is inconsistent. $\Box$

This simple formal discovery occasioned the ‘crisis in foundations’ early in the 20th century.

Frege’s Afterword to Volume II of his *Grundgesetze*, written in October 1902, begins with the heart-breaking words

> Hardly anything more undesirable can befall a scientific writer than to have, at the completion of his work, one of the foundation-stones of his edifice shattered. (Frege [1903], p. 253; author’s translation)

Russell’s paradox consigned the details of the *Grundgesetze* to relative obscurity. The scholarly community had to wait a long time for a complete English translation of the work. And this was unfortunate, given its importance for the neo-Fregean revival that began in the 1960s.[^note-23]

### 1.3 Logicism after Frege and up to Zermelo

#### 1.3.1 Russell’s type theory

Russell offered his own solution to the problem of his paradox, in the form of his *theory of types* (both simple and ramified).[^note-24] By stratifying the universe of objects into types, Russell sought to avoid the vicious circularity that he had diagnosed as the underlying problem with Fregean class abstraction.

Individuals would form the lowest type. Attributes or properties of individuals (or what Russell called *propositional functions* that could be true or false of individuals) would form the next higher type … and so on. In Russell’s type theory, the relation of membership can hold only between objects of different types: if $\alpha$ is a member of $\beta$, then $\alpha$ is of lower type than $\beta$. In type theory, the variables are typed. That is, a given variable is to be construed as ranging only over objects of a certain type. Thus there will be ‘individual’ variables (of type 0, say) ranging over just the individuals. At the next type up—type 1—there will be ‘property’ and ‘relation’ variables ranging over such properties and relations as hold of, or among, individuals. (0 and 1 here are serving as *indices* of types.) The idea iterates to cover all types of finite index. Moreover, in Russell’s theory, *only* the finitely indexed types could be formed. These are the types that can be indexed, from ‘outside’, so to speak, by natural numbers $n$. There are no transfinite types, i.e., no types that would be indexed by transfinite ordinals such as $\omega$.[^note-25]

A *predicative* propositional function is one that involves no quantifications over types higher than those of its arguments. Russell stratifies not only the universe of discourse (the various types, and objects of those types); he also stratifies the *language*. Suppose that a Russellian class (or predicative propositional function) $\beta$ is first formed at a higher rank than is $\alpha$. Then it is supposed to be *meaningless* (in the language of type theory) to say that $\beta$ is a member of $\alpha$, where this is construed in the official sense of supposedly attributing the attribute corresponding to $\alpha$ to the object $\beta$. (By contrast, *in the language of set theory*, it is *meaningful*—even if false—to say that $\beta \in \alpha$.) Thus it is impossible, within Russell’s type theory, to deal with the would-be predicate or property of non-self-membership. For that requires that the predicate $x \in x$ of self-membership be meaningful (and well-formed); which it is not. So, in his type theory, Russell blocked the kind of derivation of his own paradox to which Frege’s class theory fell victim.

Russell, however, sought to *preserve* Frege’s approach to defining cardinal numbers as classes of similar-sized classes:

> The cardinal number of a class $\alpha$ is defined as the class of all classes similar to $\alpha$, two classes being similar when there is a one-one relation between them. (Russell 1908: 256)[^russell-1908]

This definition, and the problems it engenders, survived into *Principia Mathematica.*

Because of Russell’s partitioning of the logical universe into types, his ‘cardinal numbers’ became *typically ambiguous*. (In the following quotation, the symbol $\Lambda$ stands for the null, or empty, class.) As Russell conceded (1908: 257),

> … 0 and 1 and all the other cardinals, according to [our] definitions, are ambiguous symbols, like cls, and have as many meanings as there are types. To begin with 0: the meaning of 0 depends upon that of $\Lambda$, and the meaning of $\Lambda$ is different according to the type of which it is the null-class. Thus there are as many 0’s as there are types; and the same applies to all the other cardinals.

Russell does not, however, fully accept the strictures thus imposed. In more expansive mood he immediately adds

> Nevertheless, if two classes $\alpha , \beta$ are of different types, we can speak of them as having the same cardinal … because a one-one relation may hold between the members of $\alpha$ and the members of $\beta,$ *even when $\alpha$ and $\beta$ are of different types*. [Emphasis added]

By giving in to this structuralist impulse, Russell in effect puts a second construal of cardinal numbers into contention with his official type-theoretic one. The new construal is of a cardinal number as something that results from *abstracting* from classes on the basis of their similarity, rather than from forming classes of similar classes. Such abstraction takes the Humean form (famously exploited by Cantor)

$$\text{Card}(\alpha) = \text{Card}(\beta) \Leftrightarrow \exists R(R : \alpha \underset{\text{onto}}{\overset{1\text{-}1}{\mapsto}} \beta).$$

For the reasons internal to type theory explained above, a Card cannot be an object within any type within the official ontology of type theory. For its would-be domain of definition would not only have to straddle distinct types, but also include classes of all types. But that is not possible for any type-theoretically admissible function or operation. This fact also precludes Russell from using Frege’s trick to ensure an infinity of numbers.[^note-26] For Frege had each natural number $n$ be the number of preceding natural numbers. For the latter to be thus numbered, they have to be objects in the official ontology—which, however, as just observed, Russell’s Card(inal)s are not.

Partitioning the universe into types accordingly exacted a high price for the ‘logicism’ that might result. It is not reassuring to learn that the logicist reconstruction on offer for one’s favorite mathematical structures is so generous as to be uniquely re-presented within each type. One would wish to capture their *commonalities* within *some one structure*. And that, as we have just seen, is what Russell was trying to do, even though it was doomed to failure from the start, on account of its being committed to the existence of a different series of the ‘same’ numbers within each type.

The motivation for the typing that led to this *embarras de richesses* was understandable at the time. Russell wished to avoid any potentially vicious circularity that might result from impredicative definitions. According to Russell, it should be illicit to define a class $C$ in a way that involves generalizing about any range of individuals to which $C$ itself would have to belong. Thus, with partitioning into types, the notion of self-membership, along with non-self-membership, could not even be deployed.

This Russellian constraint on class abstraction, however, had the consequence that with impredicative ‘class abstracts’ of the form “the class of all $x$ such that $\Phi(x)$”, the *existence* of such a class could not be guaranteed *as a matter of logic*. So Russell had to *postulate* that such classes existed. This came to be regarded as detracting from their status as would-be logical objects, and revealing them instead as no more than mathematical posits. Their existence was once again (at best) a *synthetic a priori* matter, rather than one of analytic necessity and certainty.

One might wonder why such classes would qualify as logical objects courtesy of a single immensely powerful postulate (had it been consistent), but would not so qualify if their existence has to be secured in a more piecemeal postulational fashion. But that was the Achilles heel of Russellian logicism. The existential postulation present in Russell’s Multiplicative Axiom (nowadays known as the Axiom of Choice) and in his Axiom of Infinity were seen as marks of the merely mathematical, albeit against the background of a much more capacious universe of abstract objects than just the natural numbers or the real numbers themselves.

Russellian types are *ramified*: that is, propositional functions of one and the same type belong to different *orders*, depending on their internal logical structures. The *type* of a propositional function, as we have seen, is determined by the types of its free variables. But two propositional functions $\phi$ and $\phi '$ of the same type can involve different kinds of quantifications. If $\phi$ involves quantifications whose (bound) variables range over higher types than do the bound variables within $\phi '$, then $\phi$ is of correspondingly higher order than $\phi '$, even though $\phi$ and $\phi '$ are of the same *type*. Recall that an impredicative propositional function $\phi$ is one that contains bound variables ranging over types as high as or higher than the type of $\phi$ itself. Assigning an impredicative propositional function to a higher order is the ramifier’s way of marking it as not kosher.

Russell ramified his theory of types in order to avoid explicitly impredicative definitions (against which definitions Poincaré influentially inveighed). Russell then found himself hamstrung, unable to derive certain desired mathematical results. Among these results were Cantor’s Theorem, and the theorem of real analysis which states that every set $X$ of real numbers that is bounded above has a least upper bound *of the same order as the real numbers in $X$*. Ramified type theory appeared powerless to prove these results. So Russell, in pragmatist spirit, introduced the Axiom of Reducibility simply in order to get things done.

Russell’s Axiom of Reducibility in type theory states that every propositional function is coextensive with a predicative one—that is, one whose quantifiers range only over types lower than that of the propositional function itself. The non-trivial content of this axiom is that every *impredicative* propositional function is coextensive with a predicative one. A well known example to illustrate this is the impredicative propositional function $\forall F(Fx \leftrightarrow Fy)$. The Axiom of Reducibility could be vindicated on this example by adducing the predicative propositional function $x = y$—provided that one accepts Leibniz’s controversial principle of the identity of indiscernibles. If, *contra* Leibniz, one believes it is possible for indiscernibles to be distinct, then, in order to vindicate the Axiom of Reducibility, it would be necessary to adduce some other predicative propositional function, $x \sim y$ say, for which it is true that

$$\forall F(Fx \leftrightarrow Fy) \leftrightarrow x \sim y.$$

The Axiom of Reducibility, however, is tantamount to conceding the admissibility of impredicative definitions after all. For it collapses the orders for propositional functions of type 1. Critics pointed out that it would be better to eschew ramification and embrace the procedure of impredicative definition as licit after all.

One was then left with simple type theory (and no need for the Axiom of Reducibility). But even the simple theory of types eventually fell out of favor as a foundational theory for mathematics—possibly because in the wake of the Byzantine ramified theory, no version of type theory could find favor among mathematicians themselves. Type theory was displaced by the newly emerging *set theory* due to Zermelo and Fraenkel, which mathematicians could recognize more easily as a formal codification of Cantorian mathematical practice. A definitive and richly detailed history of the reception and eventual demise of Russellian logicism can be found in Grattan-Guinness (2000)[^grattan-guinness-2000]. (The terminology of ‘sets’ was adopted in order to contrast these ‘safer’, paradox-free objects with the problematic *classes* of Frege’s inconsistent theory.)

#### 1.3.2 Zermelo-Fraenkel set theory

With some justice ZFC (Zermelo-Fraenkel set theory with the Axiom of Choice) can be construed as an intellectual descendant of Russellian type theory, even though both theories date from the same year, 1908.

The displacement of type theory by set theory took place during the 1920s. The aim was still to unify all of mathematics, and to provide a capacious universe of abstract objects in order to do so. All the different mathematical theories would be interpretable within set theory, upon suitable identification of ‘set-theoretic surrogates’ for the objects studied by those theories. So, for example, the finite von Neumann ordinals can serve as set-theoretic surrogates for the natural numbers.[^note-27] And $\wp(\omega)$, the power set of the set of natural numbers, is the set-theoretic surrogate for the real continuum.[^note-28]

ZFC set theory is an account of a cumulative hierarchy $V$ of pure sets, built up, ultimately, from the empty set $\varnothing$. Each set within $V$ is ‘formed’ by some ordinally indexed rank. The ranks are cumulative, and are generated, at successor ordinals, by application of the power-set operation. The erstwhile types are born again as ranks, except that ranks are *cumulative*—every rank contains all members of lower ranks. Their members are put on all fours, so to speak, for they are taken to occupy one single extensionalized, untyped universe $V$ of sets.

Quine (1969)[^quine-1969], chapters XI and XII, is a masterly tracing of a route consisting of incremental theoretical adjustments that one could in principle make, beginning with the type theory of *Principia Mathematica* (PM), and ending with Zermelo-Fraenkel set theory. The purpose behind postulating the Axiom of Reducibility in type theory, as already observed, was to ensure that every propositional function is coextensive with a predicative one. As Quine points out, however (and as Ramsey had pointed out before him), the Axiom of Reducibility really defeats the purpose behind its own postulation, thereby motivating the adoption of a simple type theory in place of PM’s ramified one. If one then reformulates simple type theory with ‘general’, or untyped, variables, and lets the types be cumulative (rather than remain stratified one from another without overlap), one effects the segue to Zermelo set theory. Fraenkel’s Axiom Scheme of Replacement finally allows one to “[pierce] all type ceilings” (Quine 1969: 282)[^quine-1969], and reach Zermelo-Fraenkel set theory. Replacement says that any function that is defined on a set as its domain has a set as its range. This allows one to form, for example, for any transfinite ordinal number $\kappa$, the set

$$\{\aleph_{\alpha} \mid \alpha \lt \kappa \}$$

of all infinite cardinals numbers $\aleph_{\alpha}$, where $\alpha = 0,1,2,\ldots \lt \kappa$. The ordinals $\alpha$ less than $\kappa$ form a set (indeed: $\kappa$ itself). $\aleph_{\alpha}$, better thought of as $\aleph(\alpha)$, is the $\alpha$-th infinite cardinal number. So $\aleph$ is a function with domain $\kappa$, whose value on $\alpha$ is the $\alpha$-th infinite cardinal number. By Replacement, the set $\{\aleph_{\alpha} \mid \alpha \lt \kappa \}$ exists. Such a set resides at a rank way above $\kappa$.

Quine’s account amplifies the slightly less detailed one that is to be found in Gödel (1993/1995).[^note-29] As Gödel observed (pp. 45–6), the ‘theory of aggregates’, or set theory,

> … as presented by Zermelo, Fraenkel and von Neumann … is nothing else but a natural generalization of the theory of types, or rather, it is what becomes of the theory of types if certain superfluous restrictions are removed.

These removals are threefold: make the types cumulative; untype the variables; and allow type formation to extend into the transfinite.

ZFC avoids Russell’s Paradox, even though all its member-sets are on all fours, within an untyped universe. This is because its universe $V$ itself is *not* a set. By not espousing any powerful enough set-abstraction principle, the set theorist avoids Russell’s paradox. Partitioning the universe of discourse into types appears to have been a methodologically costly over-reaction to the problem of Russell’s Paradox. The latter would of course be re-instated if one were ever to treat the universe $V$ as a set. Simply apply the Axiom Scheme of Separation

$$\forall y\exists z(z = \{x\mid x \in y \wedge \Phi(x)\}),$$

using for $\Phi(x)$ the Russellian formula-instance $x \not\in x$, and instantiating $\forall y$ with respect to $V$.

Mathematicians have a well-established practice of treating set-abstracts as well-formed terms. They are of the logico-grammatical form $\{x \mid \Phi(x)\}$.[^note-30] If one’s formalizing logic is to respect this practice, then it must provide the *variable-binding term-forming operator* (*v.b.t.o.*) of set-abstraction:

$$\{x \mid \ldots x \ldots \}.$$

Such an operator may be applied to any formula $\Phi$ to produce a term. Among such formulae are the hazardous ones $x = x$ and $x \not\in x$. The formalizing foundationalist will therefore be careful to adopt a *free logic* in which it is *not* assumed, of every well-formed term, that it enjoys a denotation. The proof of Russell’s Paradox can then be deprived of its sting: it simply becomes a proof of the negative existential $\neg \exists x\, x = \{y \mid y \not\in y\}$.

Adopting a free logic, however, brings with it the following obligation: if one wishes to recognize that certain sorts of objects exist, or that a particular object exists, then one will have to postulate their existence explicitly. No longer does such existence derive from a kind of built-in, or tacit, default assumption of the underlying logic. Rather, it demands explicit expression as a *theoretical commitment*.

*You want an empty set?* the ZFC-theorist asks. *By all means! Here it is:*

$$\exists x(x = \{y \mid y \ne y\}).$$

*You want singletons? Sure thing!:*

$$\forall x\exists y(y = \{w \mid w = x\}).$$

*… Or, if you prefer, get them from the axiom of unordered pairs, by taking the same instance twice over:*

$$\forall x_1\forall x_2\exists y(y = \{z \mid z = x_1 \vee z = x_2\}).$$

*You want an infinite set? By all means! Here is a very useful one:*

$$\exists x(x = \{y \mid Ny\}),$$

*where $Ny$ means that $y$ is a finite von Neumann ordinal (and this concept can be explicitly defined in set-theoretic terms).*

ZFC theorists wear their ontological commitments, either outright or conditional, very much on their postulational sleeve. They are out to characterize a very rich mathematical universe, to be sure—one in which there are so many things, and of such great variety of structure(s), that one should be able to find, therein, a set-theoretic ‘surrogate’ for virtually any kind of mathematical object or structure about which one may wish to make conjectures and prove theorems. With only this over-riding concern to unify all of mathematics within one overarching domain,[^note-31] the ZFC theorist is not particularly committed to a *logicist* view of the objects and structures involved. If anything, logicism has acquired a new challenge: show how *set theory itself*—like arithmetic and analysis, say—is simply a body of logical truths in definitional disguise; and show how *sets themselves* can be (re-)construed as some kind of definitional concoction from *purely logical objects*![^note-32]

## 2. Neo-Fregeanism

The neo-Fregean revival had its origin in an insight of Charles Parsons (see Parsons 1965: 183 and 194)[^parsons-1965]. He pointed out that what he called principle (A) below suffices, given the structure of Frege’s argumentation in the *Grundlagen*, for the derivation of the axioms of Peano arithmetic. Parsons uses the binary quantifier ‘*Glz*’ to abbreviate “*gleichzahlig*” (equinumerous), and uses $N_x$ to abbreviate “the number of”:

> $$\tag{A} N_{x}Fx = N_{x}Gx \equiv Glz_x (Fx,Gx). $$
>
> … we can put [Frege’s procedure] in the form of defining Peano’s three primitives ‘0’, ‘natural number’ and ‘successor’, and proving Peano’s axioms. … it is not necessary to use any axioms of set existence except in introducing terms of the form ‘$N_x Fx$’ and in proving (A), so that the argument could be carried out by taking (A) as an axiom.

This is nowadays called ‘Frege’s Theorem’.[^note-33] Frege’s Theorem has Principle (A) as its hypothesis. Curiously, the stress Frege places, in the *Grundlagen*, on the importance of this principles (that two concepts have the same number just in case they are *gleichzahlig*) is dissipated in the *Grundgesetze*, where the two halves of the biconditional appear widely separated: in §53 Frege proves that if two concepts correspond 1–1, then their numbers are identical, and in §69 he proves the converse. But nowhere in the *Grundgesetze* does he re-assemble the biconditional and accord it prime philosophical importance. Had he done so, he *might* well have become the first neo-Fregean in response to Russell’s Paradox. In order to do so, however, he would have had to overcome his reluctance to view (A) as a logical axiom.[^note-34]

The neo-Fregean movement seeks to reveal that a significant amount of mathematics is analytic. This is a stronger claim than that it is *a priori* and derives no part of its justification from empirical science, or even from successful applications within the empirical sciences. For that would hold of mathematics (or indeed any other branch of knowledge) conceived of as synthetic *a priori*. The neo-Fregean maintains in addition that significant parts of mathematics flow logically from principles that are analytic of (or definitional of) their central concepts or predicates, such as ‘natural number’ or ‘real number’. That is, they flow from the very meanings of those central predicates. (We opt here for the linguistic version of the analyticity claim). Note the stress here on ‘significant parts’.[^note-35] We know from Gödel’s second incompleteness theorem that any consistent and sufficiently strong theory of arithmetic is unable to prove or refute (the formalized statement of) its own consistency. The latter statement is true, but unprovable. In light of the incompleteness phenomena, one would be hard pressed to make good on the claim that *all* mathematical truths are true by virtue only of such *logical* considerations as can be captured in systems of formal proof.[^note-36] When the first principles of a mathematical theory, such as arithmetic, form an essentially incomplete axiomatization, the logicist will have to maintain that the justification of any *new* first principle can be furnished in some strictly logical sense.

Note that the foregoing remarks describe the general context for a neo-Fregean revival of logicism of any kind. They do not dictate the exact form of any such revival. In §3 we discuss the particular form of the revival that involves extending second-order logic with Hume’s Principle; and in §4, we discuss constructive logicism.

These two forms of neo-Fregean revival of logicism share the following three important features with Frege’s own treatment.

First, the number 0 (zero) is still defined as the number of any empty concept: in particular, as *the number of non-self-identical things* (formally: $\# x \neg x = x$).

Secondly, once the existence of any natural number $n$ is secured, that of its successor, $s(n)$, is secured by taking $s(n)$ to be the number of *all natural numbers from* 0 *to $n$, inclusive* (Frege’s trick).

Thirdly, the definition of the concept of natural number exploits the notion of the *ancestral* of the relation of succession: $x$ bears the succession-ancestral relation to $y$ just in case $y$ is at most finitely many steps of succession away from $x$. (As already made clear, any apparent circularity in this definition, deriving from the adverbial gloss ‘finitely’, turns out, upon closer inspection of the definitions used, to be just that: merely apparent.) The concept “$z$ is a natural number” is then defined as “either 0 is $z$, or 0 bears the succession-ancestral relation to $z$”. And this is what allows the neo-Fregean logicist to derive the principle of mathematical induction for the natural numbers. The reader of this survey article will be spared the formal details. They can be found in Tennant (2022)[^tennant-2022].

## 3. Second-order logic with Hume’s Principle

The neo-Fregean revival began in earnest with Wright.[^note-37] Wright (1983)[^wright-1983] sought to derive the Dedekind-Peano axioms for successor arithmetic from what was called N$^=$ and has since come to be known as Hume’s Principle (that is, Parsons’s principle (A) above):

$$\# xFx = \# xGx \leftrightarrow \exists R (R \text{ maps the \(F\)s \(1\text{-}1\) onto the \(G\)s}).$$

Wright sketched a derivation of the Dedekind-Peano axioms from Hume’s Principle. The deductions sketched would be carried out in standard second-order logic—‘standard’ in the sense that, in the presence of HP, all number-abstractive terms of the form $\# x\Phi(x)$ can be proved to denote. Such a system is *unfree with respect to its number-abstractive terms.* This point holds *even if* the second-order logic in question is a free logic in the official sense of not being committed to the theorem-scheme $\exists !t$ (i.e., $\exists x\, x = t$) for any well-formed singular term $t$. The proof of this point is short and easy, and is like the one given in §1.2.3. We shall given an informal version as follows.

> Clearly, the identity relation is a one-one correspondence of the $\Phi$s onto the $\Phi$s. Therefore it is a theorem of second-order logic that
>
> $$\exists R(R \text{ maps the \(\Phi\)s \(1\text{-}1\) onto the \(\Phi\)s}).$$
>
> This is the right-hand side of that instance of HP whose left-hand side is
>
> $$\# x\Phi(x) = \# x\Phi(x).$$
>
> The latter has now been established as a theorem-scheme of second-order logic with HP. Hence in this system we have the theorem-scheme
>
> $$\exists !\# x\Phi(x).$$

The overarching theme is that we can redeem Frege’s key philosophical insights concerning (natural and real) numbers and our knowledge of them, despite Russell’s discovery of paradox in Frege’s own theory of classes. That paradox notwithstanding, numbers are still logical objects, characterized by methods or principles of abstraction—which of course cannot be as ambitious as Frege’s Basic Law V. These principles afford a distinctive form of epistemic access to numbers. The usual mathematical axioms governing the two kinds of numbers are to be derived as results in (higher-order) logic—essentially following Frege’s deductive plan. These derivations will exploit appropriate definitions of the primitive constants, functions, and predicates of the brand of number theory concerned. (For example: 0, 1; $s, +, \times$; $\lt$; $N(x)$; $\mathbb{R}(x)$.)

The main difference is this: the neo-Fregean no longer accepts Frege’s definition of numbers as classes of equinumerous classes. Instead, the numbers are vouchsafed as *sui generis*, courtesy of newly chosen abstraction principles. The Wrightian neo-logicist (henceforth: the HP-er) opts for HP; the constructive logicist opts, much more modestly, for rules permitting the introduction of zero and of successors. Apart from this key difference, however, the neo-Fregeans hew in other places quite closely to Frege’s overall deductive strategy when deriving the Dedekind-Peano postulates.

No supplementation by intuition or sensory experience will be needed in the derivations of these postulates. The trains of reasoning involved will depend only on our grasp of logical validities, supplemented by appropriate definitions. Purported result (for the HP-er): *because HP is analytic*, logicism is vindicated; and the mathematical knowledge derived in this way is revealed to be analytic, not synthetic.

For reservations about this claimed result, however, see Boolos (1997)[^boolos-1997]. The main objection with which the HP-er needs to contend is that Hume’s Principle is neither a logical nor an analytic truth. It cannot be logical, so the objection would go, because it has such a huge ledger of ontological commitments: for *every* concept, its alleged number. And it cannot be analytic, because the two sides of the biconditional have *different* ontological commitments: the right-hand side has *no* commitments to numbers, while the left-hand side is brimming with such commitments. In order to defend against these objections, the HP-er needs to do two things. First—as any logicist needs to do—he needs to challenge the dogma that no logical principle can carry any ontological commitments. Secondly, he needs to provide an account of analyticity according to which a biconditional can be analytic even when the explicit ontological commitments of each side of the biconditional differ. (These commitments are to be judged by considering each side as a sentence in the restricted language whose vocabulary is just sufficient to allow the sentence in question to be formed.)

The HP-er advocates Hume’s Principle in its unrestricted form, and is thereby committed, as we have seen, to the existence of a denotation for every term of the form $\{x \mid \Phi(x)\}$. The HP-er is committed, not only to the number of all natural numbers, but also to the number of all self-identical things—or, at least, so Wright was in Wright (1983)[^wright-1983]. This ‘universal number’ $\# x(x = x$) is sometimes called ‘anti-zero’. In n. 5 on p. 187 one reads

> It is worth stressing that it is, of course, absolutely essential that there be such a number as $Nx : x = x$; for it is impossible to imagine what sort of ground there could be for admitting $Nx : x \ne x$ if that were in doubt.

Boolos (1987)[^boolos-1987], after raising qualms about the universal number, provided an ingenious model (which had been anticipated informally by Geach (1975: 446–7)[^geach-1975]) to allay the misgiving about the consistency of full second-order logic with HP (the system now known as FA, for ‘Frege Arithmetic’). Simply take the natural numbers along with the distinct object $\omega$ as the elements of the domain. The element $\omega$ serves as the denotation of any term of the form $\# x\Phi(x)$ where $\Phi$ is satisfied by infinitely many elements. Note, however, that this consistency proof works only when FA is taken on its own.[^note-38] The Geach–Boolos model cannot be relied upon to secure the consistency of FA *in conjunction with* other theories, such as set theory, that one might wish to extend with FA. Since, however, counting finite extensions ought to be a universally applicable intellectual operation, regardless of subject matter, it will be the exception rather than the rule that FA is to be applied *only to the natural numbers* (plus, perhaps, the unnatural factotum $\omega)$. Rather, FA should be applicable not only to concrete objects, but also to abstract mathematical entities such as real numbers and sets. Provided only that one has a criterion of identity for the objects in question, one should be in a position to count any finite collection of them.

Subsequently, in Hale and Wright 2001 (p. 315), Wright expressed reservations over whether “$x = x$” counts as a sortal predicate eligible to be prefixed by “the number of $x$ such that”. Now Wright was inquiring after what “is wanted for the *exorcism* of anti-zero” (p. 314, emphasis added). His considered answer is that a term of the form $\# xFx$ will denote a number only if the concept $F$ is both sortal and not indefinitely extensible.[^note-39] So Wright subsequently hoped to make actual what he had previously alleged to be impossible to imagine. The technical proposal must therefore be that Hume’s Principle is to be restricted to predicates that (express concepts that) are both sortal and not indefinitely extensible. But this, of course, raises the question whether there is an effective method for determining, of any given predicate $F$, whether $F$ (expresses a concept that) is both sortal and not indefinitely extensible. In the absence of any such effective method, the theory will not have been axiomatized.

This survey perforce confines itself, in the main, to (neo-)logicist accounts of the *natural* numbers. But it is worth raising one more question about the extension of a neo-Fregean account in an attempt to cope with the *real* numbers. We shall call it the *inclusion question*. How is one to appreciate that the natural numbers *qua* reals *are* (in the non-punning sense of numerical identity) the natural numbers vouchsafed by logicism about the naturals?[^note-40] This question is not answered by the neo-Fregean abstractionist account of the reals in Shapiro (2000)[^shapiro-2000][^shapiro-2000-2]. In that account, the various new abstracta are abstracted from quite varying equivalence relations, and no attempt is made to leave it open as a possibility that the natural number $n$ *is* the integer $n$, *is* the rational number $n$, and *is* the real number $n$. (Although on p. 339 Shapiro writes that he proposes “to avoid the issue [of *identity* under inclusion] here”, his proposed treatment nevertheless answers the inclusion question negatively.)

One issue that is not satisfactorily disposed of, is this: in what sense can Wright’s neo-Fregean logicist claim to be furnishing an *epistemic foundation* for, let us say, first-order Peano arithmetic, if their axiomatic principle HP, along with the second-order logic employed ($=\text{FA}$), puts the supposed ‘foundation’ much higher in the hierarchy of consistency-strengths than the weaker theory being ‘founded’? (This is to raise once again the worry expressed by Boolos (1997: 248–9)[^boolos-1997].)[^note-41]

It is an age-old tradition in foundational investigations to provide a foundation that is not only obviously consistent, but obviously true, and from which all the results in the branch(es) of mathematics being founded will follow logically. Moreover, this following logically is itself something that must be epistemically accessible—hence the importance of checkable proof. A foundational effort can be directed at many different branches of mathematics simultaneously, or just at some particular branch, such as arithmetic. In the former case, it is understandable if the foundational theory chosen (such as ZFC) has a higher consistency strength in relation to any one branch of mathematics being founded. But if the effort is directed at just that one branch (say, arithmetic), then the foundation provided should be of a consistency-strength that is as low as possible, in relation to that branch.

The consistency-strength of FA is that of second-order arithmetic $Z_2$ (i.e., real analysis), which is equal to that of Zermelo–Fraenkel set theory without the Axiom of Power Sets. The consistency-strength of first-order Peano arithmetic is much weaker, namely that of Zermelo–Fraenkel set theory without the Axiom of Power Sets *and* without the Axiom of Infinity.

By adopting second-order logic along with Hume’s Principle in an unrestricted form, Wright incurred commitment (as a matter of analyticity) not only to each natural number, *seriatim*, but also to the cardinal number of *any* concept whatsoever. We know now, however, that Gödel’s prescient ‘completionary’ insight has long since been fully borne out. The insight in question was that the set-theorist’s key to proving stronger and stronger results in mathematics—and in particular the consistency of each newly attained system—is to postulate the existence of ever-larger cardinal numbers. If all these cardinals were available across the board courtesy of Hume’s Principle applied to appropriately expressed concepts, then Wright would be proposing a foundational theory of enormous strength. The only reason why FA is not even more powerful than $Z_2$ is that the former system’s ontology is being generated solely by the abstractions. There is no other source of existential postulation, as there would be if one were to add, say, set theory to the theoretical mix.

Upon such addition further care would be needed when considering the nature of Wright’s transfinite cardinals begotten by Hume’s Principle. As the investigations of Kit Fine (1998: 515; 2002) have revealed, any attempt to combine such an abstractive account of transfinite cardinals with set theory must resort to treating the abstracted cardinals as *Urelemente* rather than as sets. Set theory cannot, by itself, provide a set-surrogate for every transfinite cardinal that would be generated by Hume’s Principle.

Another and rather different line of criticism of the claim that HP is analytic can be found in Mancosu (2016: Chapter 4). Ironically, Mancosu advances what he calls a *Good Company* objection to HP. HP jostles for primacy with at least infinitely many ‘Good Companion’ abstraction principles. They are good because, like HP, they permit the logical derivation of the Dedekind-Peano axioms. They do so via their respective ‘number’-abstraction operators with predicates whose extensions are (Dedekind-)*finite*. They assign such extensions the right natural numbers as their cardinal numbers. When that operator is applied to a predicate whose extension is (Dedekind-)*infinite*, however, these other principles give results arbitrarily different from what one would expect from the more Cantorian principle HP. HP and these Good Companions get matters right on all finite extensions. But the Good Companions give rise to a confusing variety of ‘number’-assignments to infinite extensions. The problem for the HP-er, as Mancosu sees it, is how to maintain the case for the analyticity of HP in light of all this good company. We see here another manifestation of the epistemological worry that HP is of excessive consistency strength when the logicist project is simply to furnish a deeper but analytic foundation for Dedekind-Peano arithmetic. All that such a foundation requires is what HP *and* these competing Good Companion principles *agree upon*—namely, that predicates with (Dedekind-)*finite* extensions should get the right numbers assigned to them (i.e., the natural numbers). There is no need for the logicist about Dedekind-Peano arithmetic to make pronouncements about any infinite numbers.

Mancosu’s Good Companions to HP arise only because he shares with the HP-er a fundamental logical commitment: *every* singular term of the language must denote. This means that the logic furnishing the supposed logicist foundation for arithmetic is not a *free* logic. Every singular term formed by applying the number-abstraction operator to a predicate is taken to stand for some object. This refusal to adopt a free logic complicates matters unduly if ones sees as part of the logicist project the task of generating only epistemically *justifiable* commitment to numbers as abstract existents. We want, as it were, to be able to recognize only those numbers whose existential credentials are absolutely compelling. In particular, the logicist should be able to deliver *only* the natural numbers, when furnishing deeper logical derivations of the Dedekind-Peano postulates.

## 4. Constructive Logicism

### 4.1 Motivation for a different kind of neo-logicism

We begin this section with some remarks about Gentzenian proof theory. This is not because it played any direct role in the development of logicism—far from it—but because we seek in this section to describe in broad terms a different kind of neo-logicism that draws more heavily on proof-theoretic resources.

It was only with the work of Gerhard Gentzen in the early 1930s (see Gentzen 1934, 1935)[^gentzen-1934] that researchers in foundations were equipped with formal calculi of deduction that could do real justice to the actual structure of inferential dependencies within mathematical proofs. What we have in mind here are the dependencies of conclusions upon both premises and assumptions that may have been made only “for the sake of argument”. A good example of assumptions of the latter kind are *reductio* assumptions (assume $\phi$; derive absurdity; conclude $\neg \phi$, now independently of $\phi)$.

It is extraordinary that the community of mathematical logicians took so long to discover the calculi of natural deduction (and the *sequent calculi*), once Frege, in 1879, had cracked the previously hidden grammatical code of multiply quantified sentences. It is remarkable that Gödel, in 1929, could have demonstrated the completeness of first-order logic *before* Gentzen’s natural formulation of it, when that logic was available only in the forms of the highly unnatural deductive calculi devised by Frege, by Hilbert, and by Russell and Whitehead.

The essential breakthrough of Gentzen’s treatment was to characterize each logical operator in isolation, with rules of its own, rules in which *only* that operator would explicitly feature. Moreover, the rules in question would deal only with a *single occurrence* (in dominant position) of the operator in question. The rule for reasoning to a conclusion with the operator dominant was called the operator’s *introduction* rule; while the rule for reasoning *from* a premise with the operator dominant was called its *elimination* rule.

The introduction and elimination rules for any logical operator have to be in a certain kind of *equilibrium*, an equilibrium that lends itself to an interpretation of the rules as matching the inferential obligations of any responsible, rational and sincere speaker to the inferential entitlements of any responsible, rational and trusting listener.[^note-42]

The equilibrium in question is explicated by the so-called *reduction procedures* for the logical operators. These procedures enable one to remove from a proof any sentence occurrence that stands both as the conclusion of an application of an introduction rule and as the major premise of an application of the corresponding elimination rule. Repeated application of the procedures will eventually turn the proof into one that is in *normal form*—essentially, one that is not eligible for any further application of the procedures.[^note-43] The significance of proofs in normal form is that they represent *direct* deductive routes from their premises to their conclusions.

Powerful, incisive and revolutionary though Gentzen’s approach has since proved to be, it was, in its turn, curiously limited. It was restricted to just the universally acknowledged *logical* operators of first-order logic: $\neg , \wedge , \vee , \rightarrow , \exists$ and $\forall$.

At exactly the same time there appeared Carnap (1934)[^carnap-1934], *Logische Syntax der Sprache*, which offered an account of analyticity for languages in which all logico-*mathematical* operators could make similar contributions to the status of a sentence as analytically true (or analytically false). Carnap, however, did this by employing axiomatizations involving all the various logico-mathematical operators, co-functioning in grammatically complex axioms. His approach was therefore quite unlike the more ‘natural’ one of Gentzen, which was *single-operator focused*. Moreover, the unnatural approach was still Carnap’s preferred choice in work as late as his *Foundations of Logic and Mathematics* (Carnap 1939)[^carnap-1939].[^note-44] We mention Carnap in contrast with Gentzen here because of Gentzen’s tragic early death at the end of the Second World War. Who knows how Gentzen might have extended his exquisitely conceived inferentialist techniques to items on the broad logicist agenda? His writings appeared in English translation only in 1969 (see Gentzen 1934/1935 [1969])[^gentzen-1934]. Carnap, however, did survive to exert considerable influence on the thinking of a new generation of philosophers of mathematics on the problems and prospects for logicism; and he was able to do so from the mid-1930s, in the USA, writing in English.

After the early 1940s, proof theory did not broaden and diversify so as to address a potentially fertile agenda: an investigation of the various forms that introduction and elimination rules might take, as it examines rule-governed expressions whose rules are not quite so neatly classifiable as introduction and elimination rules. This is the case, for example, with families of ‘coeval’ and interdependent concepts of a nevertheless logico-mathematical kind. An example of such a family is that of the *ordered pair* of any two things; the *first member* of any ordered pair; and the *second member* of the same. An important feature of this example, and of other examples that could be given, is that the operators in question are *term-forming operators*. Gentzen had confined his study to sentence-forming operators. Perhaps it was Tarski’s theory of truth for formalized languages (see Tarski 1956 [1933])[^tarski-1956] that deflected interest away from further development of this essentially *inferentialist* approach to the meanings of logical and mathematical operators.

### 4.2 Anti-realism and an inferentialist approach to logicism

An inferentialist approach holds special appeal for the semantic anti-realist. According to Michael Dummett’s influential characterization of semantic realism, the realist is one who believes that every declarative sentence of one’s language is determinately true or false, independently of our means of coming to know which. This is what is supposed to justify the realist’s use of strictly classical logical principles such as the Law of Excluded Middle. The anti-realist, by contrast, insists that all truths are *knowable*; and is quick to point out that we do not have any effective method for deciding the truth or falsity of statements in mathematics. Anti-realists, accordingly, reject the Law of Excluded Middle (and all other strictly classical rules that are intuitionistically equivalent to it), and advocate the use of intuitionistic or constructive logic, rather than classical logic.

An anti-realist concerned to demonstrate the analyticity of the basic laws of arithmetic would inquire whether one can eschew strictly classical passages of inference when deriving the Peano postulates. For, if those postulates are analytically true, then the anti-realist would expect to attain them by means of rules justifiable by appeal only to the constructive contents involved (see Rumfitt 1999)[^rumfitt-1999]. And indeed the anti-realist can. She can avoid recourse to the full power of Hume’s Principle. The innocuous ingredients of the conceptual content of Hume’s Principle, insofar as finite numbers are concerned, will find expression in the inferential rules that the anti-realist lays down for zero, #, and successor. Heyting arithmetic, after all, has exactly the same axioms as Peano arithmetic, and is the logical closure of those axioms under intuitionistic, rather than classical, logic. The two systems PA and HA differ only in respect of the logic used for closure. It would be rather odd if the intuitionist were debarred from being a logicist in the sense at issue here.

The pursuit of analyticity in the foundations of arithmetic is one that could be very well served by the proof-theoretic methods favored by the Dummettian anti-realist’s theory of meaning. Central to such a proof-theoretic approach is the formulation of inferential rules governing all the expression-forming operators in question—rules that come, preferably, in introduction-elimination pairs. The rules are constitutive of the respective operators’ meanings; whence results proved solely by means of those rules qualify as analytic. A question that will be raised by any alert meaning-theorist, therefore, is the following: Might there not be some anti-realist (constructive, or intuitionistic) derivation, in Fregean spirit, of the basic laws of arithmetic by appeal to suitable meaning-constituting rules of inference that conform to the general requirements of an anti-realist theory of meaning? Anti-realist doctrine invites such extension to the mathematical expressions in fundamental theories such as arithmetic. It could give Fregean logicists what they are seeking: fundamental derivations of the Dedekind-Peano postulates from more basic logical principles, logical principles that are at least as secure, epistemically, as the mathematical postulates they are seeking to derive.

### 4.3 Execution

A theory of this kind, called *constructive logicism*, was presented in Tennant (1987)[^tennant-1987]. Its distinguishing features may be summarized as follows.

1. **Finitude:** It proves the existence of numbers of concepts with at most *finite* extensions;
2. **Logical weakness:** it uses only *free intuitionistic relevant* logic;
3. **Conceptual Adequacy:** It proves all instances of Schema N (for which, see below);
4. **Rigor:** It provides a ‘fully rigorous deduction of the Peano postulates’ (Burgess 2005: 147)[^burgess-2005].[^note-45]
5. **Single-barreled abstraction:** Its basic principles are rules of inference effecting ‘single-barreled’ abstraction.

Constructive logicism departs altogether from both the formal method of the *Grundgesetze*, with its double-barreled abstraction principle Basic Law V, and from the use of use Hume’s Principle, which is many neo-logicists’ choice of starting point—but double-barreled once again. It is essential (and prophylactically sufficient) to make this departure in a *free* logic, that is, a logic free of the dogmatic (and straitjacketing) Fregean assumption that every well-formed singular term of one’s language must denote some object. Single-barreled abstraction principles can be formulated in free logic as introduction and elimination rules for any variable-binding abstraction operator $\alpha$, governing its occurrences in *canonical identity statements* of the form $t = @ xA(x)$. The constructive logicist, of course, seeks to take $\#$ for $@$.

Details of this alternative approach, in pursuit of neologicist derivation of the theories not only of natural numbers, but also of rational and real numbers, are to be found in Tennant 2022. The approach can also be applied to set theory itself; see Tennant forthcoming. There, the revealed ‘logic of sets’ is what Quine called virtual set theory: the body of doctrine that *we* would call analytic, concerning the interconnections among set-abstraction, predication, and membership, without making any ontological commitments. Zermelo’s Axiom of Extensionality is derivable as a logical theorem on this approach.

Constructive logicism is based on rules of natural deduction that are arguably analytic of the central notions zero (0), successor $(s)$, and ‘number of’ ($\#$). The rules pin down the meaning of the number-term-forming operator $\# x\Phi(x)$ (the number of $\Phi$s). In the terminology introduced above, the rules for $\# x$ amount to a *single-barreled abstraction* principle. The remaining rules are allowed to carry only very local and modest ontological commitment, on the grounds that it is part of the very meaning of a term such as ‘0’ that its use in the language commits one to the existence of the number 0. Here, for example, are the natural-deduction rules governing zero. ‘$\bot$’ is the symbol for absurdity.

| $$\text{0-Introduction }\frac{ \begin{array}{c} \underbrace{{\scriptsize (i)}\dfrac{\ }{F(a)}\ \ \dfrac{\ }{\exists!a}{\scriptsize (i)}} \\ \vdots \\ \bot \end{array} } { 0 = \# xF(x) }{\scriptsize{(i)}}$$ | $$\text{0-Elimination }\frac{0= \# xF(x) \quad \exists !t F(t)}{\bot } $$ |
| --- | --- |
| (where the parameter $a$ may occur only in the assumptions) |   |

In order to temper the modest commitment just mentioned, all derivations are constructed within a *free* logic, so that all existential commitments other than those incurred by the rules themselves would have to be made explicit.[^note-46] All of the existential commitments that the constructive logicist incurs in this way will be incurred, anyway, by the HP-er who advocates Hume’s Principle in its unrestricted form. Recall that the HP-er is committed, not only to the number of all natural numbers, but also to the number of all self-identical things.

The ontological bill for the constructive logicist is much more modest, compared to that of the HP-er. The constructive logicist is not even committed (by the rules he lays down) to the existence of the number of all natural numbers. Commitment is incurred (by employing Frege’s trick) to the natural numbers *seriatim*, as necessary existents. No commitment is incurred, however, to any other cardinal numbers.

Chapter 25 of Tennant (1987)[^tennant-1987], titled “On deriving the basic laws of arithmetic: Or, how to Frege–Wright a Dedekind-Peano”, provides detailed formal derivations of the Dedekind-Peano axioms, within a free, intuitionistic relevant logic. All the derivations given are intuitionistic, in conformity with the anti-realist aspirations explained above, and in order to warrant the adjective ‘constructive’ in the phrase ‘constructive logicism’.

Heck (1997b)[^heck-1997b] dealt with so-called ‘finite Frege arithmetic’. His treatment was classical. But Heck was concerned, as constructive logicism had been, to derive the basic laws of arithmetic while incurring ontological commitment only to the natural numbers. To this end Heck restricted Hume’s Principle to predicates with finite extensions. It is therefore natural to conjecture that constructive logicism is the *intuitionistic (relevant) fragment* of Heck’s finite Frege arithmetic.

Tennant (1987)[^tennant-1987] argues that a condition of adequacy for any logicist theory is to explain the applicability of the finite cardinals (see p. 234). Let $\exists_n xFx$ be the formula of first-order logic with identity, defined inductively in the usual way, that says that there are exactly $n F$s. Let $\underline{n}$ be the numeral denoting the natural number $n$, that is, “$s\ldots s0$”, with $n$ occurrences of the successor symbol $s$. Schema N is the following biconditional, an instance of which is obtained by fixing on a particular natural number $n$ and open formula $\Phi$.

$$ \tag{Schema N} \# x\Phi x = \underline{n} \leftrightarrow \exists_n x\Phi x. $$

An adequate theory of number would allow one to derive every instance of Schema N;[^note-47] and the theory of constructive logicism does that. Tennant suggests that this constitutes a solution to the problem of the applicability of natural numbers in counting finite collections.

All the logicist accounts discussed so far dealt only with zero, successor, and “…is a natural number”. But there are important differences among them. It is not at all clear that constructive logicism has the same high consistency-strength of Frege Arithmetic. There appears to be no way to derive, within the constructive logicist system, an existence claim of the form

$$ \exists y(y = \# xF(x)), $$

where the extension of $F$ is an infinite set (such as the set of all natural numbers). Contrast this with the fact that FA proves

$$\exists y(y = \# x(x \text{ is a natural number})).$$

The present author therefore conjectures that the consistency-strength of this system is lower than that of FA.

In Tennant (2009)[^tennant-2009], the constructive logicist treatment is extended to deal with both addition and multiplication. The key innovation is a ‘logic of orderly pairing’: a system of natural-deduction rules of inference governing the formation of the ordered pair $\pi(t,u)$ from existing objects $t$ and $u$, and the projections $\lambda(u)$ of the left, and $\varrho(u)$ of the right, member of any ordered pair $u$.

## 5. Modal Neo-Logicism

Zalta (1999)[^zalta-1999] proposes an interestingly different, because *modal-logical*, route to the natural numbers. Although Zalta does not himself classify it as such, his approach would appear to warrant the adjective ‘neo-logicist’. (We prescind from questions about the logical status of modal logic.)

Zalta employs a classical second-order modal logic (S5) with identity, and with both the first-order Barcan ‘formula’, or axiom-scheme

$$\Diamond \exists x\psi(x) \rightarrow \exists x\Diamond \psi(x).$$

and its second-order correlate

$$\Diamond \exists F\psi(F) \rightarrow \exists F\Diamond \psi(F).$$

The first-order Barcan formula forces one to interpret quantifiers as ranging over all possible individuals, whatever world one is ‘in’—no ‘expansion’ or ‘contraction’ of the domain can be involved as one traverses the accessibility relation from possible world to possible world.

The logic is free, and descriptive terms (the description operator $\iota$ is primitive) are interpreted rigidly—that is, the denotation of a descriptive term in the actual world, if it has one there, is its denotation in any other possible world.

There are the usual alethic modalities $\Box$ and $\Diamond$ of necessity and possibility (as interpreted by S5, of course), and the actuality operator $\mathcal{A}$. The relation $xF$ of *encoding* can hold between an *abstract* object $x$ and a property $F$.

> $Ax$ will mean that $x$ is an abstract object. The properties that an abstract object encodes are constitutive of its nature, and as such, are essential to its identity as an object. (Zalta 1993: 396)[^zalta-1993]

For example, Plato’s Form of a Triangle encodes the property of being a triangle, but does not exemplify it.

Among Zalta’s fundamental principles are the following.

- Ordinary objects cannot encode any properties.
- Given any condition on properties, some abstract object encodes just those properties meeting that condition.
- Identical individuals are intersubstitutable *salva veritate*.
- Identical properties are intersubstitutable *salva veritate*.
- Particular encodings are necessary if possible.

Zalta defines an equinumerosity relation $\approx$ among properties with respect to *ordinary* objects—that is, the *possibly concrete* ones. With $\approx$ in hand, Zalta offers the notion of a (cardinal) number (Zalta 1993: 630)[^zalta-1993]:

$$\textit{Numbers}(x,G) \equiv_{df} Ax \wedge \forall F(xF \leftrightarrow F \approx G).$$

It follows that $x$ numbers $G$ just in case $x$ is an abstract object that encodes exactly the properties equinumerous to $G$ (where, *nota bene*, equinumerosity is judged only with respect to the *ordinary* objects). And it follows easily from Zalta’s first principles that “for every property $G$, there is a unique object which numbers $G$”.

Zalta’s system delivers Hume’s Principle:

$$\# F = \# G \leftrightarrow F \approx G,$$

and the following obvious corollary:

$$\forall G\exists y(y = \# G).$$

In this regard Zalta’s system is as powerful as Wright’s: they both guarantee for every property its number. Wright, however, begins with Hume’s Principle as a first principle, whereas Zalta derives Hume’s Principle (as Frege originally did) from his own ‘more basic’ (and possibly more powerful) principles.

We note the following three points, in concluding our exposition of Zalta’s system. In his sense of ‘concrete’ and ‘abstract’,

1. Properties holding of *ordinary* objects can be assigned numbers.
2. Properties holding of *abstract* objects (including numbers themselves), cannot be assigned numbers.
3. The existence of all infinitely many natural numbers depends on the possible existence of unboundedly (but finitely) many concrete objects.

In points (2) and (3), Zalta departs explicitly from Frege and all other (neo-)logicists discussed above.

## 6. Recent Work Inspired by the *Grundgesetze*, or Departing From It

We have seen that there has been a revival of interest in neologicism since the early 1980s. One of the ways in which work in this period has sought to rescue logicism from Fregean disaster (without sacrificing Basic Law V altogether, and without invoking HP as a starting point) has been the study of various ‘fragments of *Grundgesetze*’. The collectively shared idea of this company of scholars, deriving from Parsons 1987, is as follows: *Frege’s Grundgesetze succumbed to Russell’s Paradox. But Frege’s system is a big one. Let us see if we can extract a fragment of it that is (a) consistent, and (b) strong enough to afford a decent amount of Arithmetik*.[^note-48] This is typical of standard consistency-restoring revisions of theories troubled by inconsistency, but whose main goal(s) one is trying to salvage from the wreckage. The progress that has been made in this direction thus far is worth reporting. We shall call these theoretical efforts ‘fragmenting’.

The fragmenting scholars just mentioned all take as primitive a term-forming variable-binding abstraction operator that applies to predicates to form singular terms. Their notational choices for this operator vary. Here we shall speak generically of terms of the form $@xA(x)$. For $@$, Parsons follows Frege in using a breath mark (like a comma) placed *above* the variable $x$. Heck uses a caret (circumflex) placed immediately *before* $x$, and places a period immediately after $x$ in the variable-binding prefix. Wehmeier uses the caret placed immediately *above* $x$. Boccuni (not exactly a fragmenter—see below) uses the formulation $\{x:A(x)\}$ with a colon where contemporary set theorists would have a solidus: $\{x \mid A(x)\}$. Each of these authors is therefore using some form of set- or class-abstraction terms, formed by means of a variable-binding abstraction operator.

Returning to our use of $@$ as a generic symbol covering each of these idiosyncratic variants, we remind the reader that Basic Law V, in *schematic* form (where $A(x)$ and $B(x)$ are placeholders for formulae), would be expressed as

$$@xA(x)=@xB(x)\leftrightarrow\forall x(A(x)\leftrightarrow B(x)).$$

Basic Law V in *axiomatic* form would be second-order:

$$ \forall F \forall G [@xF(x) = @xG(x) \leftrightarrow \forall x(F(x) \leftrightarrow G(x))]. $$

Parsons 1987 gives a model-theoretic proof that *schema* V is consistent with first-order logic. (This had been conjectured by Schroeder-Heister 1987.)[^schroeder-heister-1987] J. Burgess 1998 gives a proof-theoretic and constructive proof of the same result. Heck 1996 extends Parsons’ argument to prove that both the simple and the ramified *predicative* fragments of Frege’s system are consistent. Wehmeier 1999 provides a consistency proof for a theory in monadic second-order logic, consisting of *axiom* V and a higher-order comprehension principle. Ferreira and Wehmeier 2002 proves the consistency of *schema* V and the same comprehension principle. The higher-order principle in question is known as $\Delta^{1}_1$-comprehension.[^note-49]

Another recent innovation akin to the study of proper fragments of *Grundgesetze* involves use of the resources of the logic of plural quantification. This of course takes us out of the realm of genuine *fragments* of *Grundgesetze*. But the ideas are closely related to those of the foregoing fragmenters.

Boccuni 2011 provides an interpretation for a language admitting plural quantification, an interpretation that Boccuni argues makes true every instance of the principles constituting the system she calls PG (short for ‘Plural *Grundgesetze*’). These are a Plural Comprehension Principle, a Predicative Comprehension Principle, and Schema V. Boccuni 2013 presents PG as ‘a consistent second-order system which is aimed [at deriving] second-order Peano arithmetic’.[^note-50]

Another recent innovation in the quest for a workable neologicist understanding of Fregean (double-barreled) abstraction that is worthy of mention was by Studd 2016. As he points out,

> The key drawback with existing responses in this style [i.e., avoiding ‘full second-order logic with an impredicative comprehension principle for Concepts’] is that they undermine the neologicist recovery of mathematics. Frege’s theorem relies on full second-order logic. The predicative theory, and its ramified variants, are too weak to interpret second-order arithmetic, PA$_2$ (see John P. Burgess 2005, ch. 2)[^burgess-2005].

In his exposition Studd eschews the use of plural logic, but makes remarks along the way to the effect that one could use plural-logical language to express his claims, if one so wished. He reverts to consideration of abstractive terms. He diagnoses the problem of finding an “adequacy criterion … to sift the ‘good’ [double-barreled—NT] abstraction principles like Hume’s principle from the ‘bad’ ones like Basic Law V.” He concludes that this approach to the bad company problem

> is on the wrong track … if neologicists are to retain the ambition of extending their success with arithmetic to other branches of mathematics, including standard Zermelo–Fraenkel set theory.

Studd diagnoses the problem with double-barreled abstraction principles as arising from the fact that they are *static*. They are taken to govern an all-inclusive domain that cannot itself be extended with denotations for the abstractive terms featuring on the left-hand side. Studd proposes that we should instead conceive of abstraction as *dynamic*, in allowing for extension of the domain by the newly abstracted abstracta. And he formulates a theory of double-barreled abstraction that would permit this.

## 7. Summary of Problems for Logicism

We see from the foregoing discussion that there are various problems to be faced by extant versions of logicism or neo-logicism in the literature. The reader who remains mindful of them will be in a position to examine the details of any proposed new neo-logicist account with a more critically focused eye.

Some of these problems confront any version of logicism, and their solutions might be required as ‘conditions of adequacy’ on the latter. Others among these problems arise only in response to the particular methods or posits employed by the version of logicism under consideration. The following problems appear to have loomed large in the foregoing discussion.

1. **Frege’s ‘conceptualization problem’** How do we apprehend numbers, if we are persuaded that arithmetic is *not* grounded in Kant’s “pure form of intuition of time”? As Frege put it in *Grundlagen* §62: “How … are numbers to be given to us, if we cannot have any ideas or intuitions of them?”
2. **Frege’s ‘Julius Caesar problem’** How can one show that, given a would-be logicist account of the nature of numbers, *Julius Caesar is not a number?* More generally: how can one show, on such an account, that *no number is a concrete individual*?
3. **The ‘applicability problem’** Can the logicist account for (i) how *natural* numbers may be applied in counting finite collections, and (ii) how *real* numbers may be applied in measuring continuously varying magnitudes such as lengths, periods of time, etc.?
4. **The ‘inclusion problem’** How does one show that the *natural* number $n$ is the very same abstract object as the *integer* $n$, the *rational* number $n$, and the *real* number $n$? (See footnote 40.)
5. **The ‘abstraction problem’** What is the correct form for number-abstraction principles (to be espoused by those who hold that numbers are logical *abstracta*)?
6. **The ‘analyticity problem’** Can one demonstrate that one’s chosen number-abstraction principles are analytic?
7. **The ‘existence problem’** Can Logic commit one to the existence of any thing, or kind of thing?[^note-51]
8. **The ‘infinity problem’** Is the logicist permitted to simply *postulate* an Axiom of Infinity, to the effect that there are infinitely many things (perhaps of a certain kind)?
9. **The ‘demarcation problem’** What makes something a logical constant? Which notions commonly held to be mathematical can actually be defined, implicitly or otherwise, in a properly formulated Logic for logicism?[^note-52]
10. **‘Bad Company’,**[^note-53] or **‘Embarrassment of Riches’** Some abstraction principles are inconsistent. Yet others, though individually consistent, are mutually inconsistent. How then can we know, of any proposed abstraction principle, whether we should accept it?
11. **‘Theoretical Invariance’** Natural numbers are universally applicable; they enjoy their arithmetical properties and enter into their arithmetical relations necessarily, independently of what other kinds of things there might be, and of how these things might be. So abstraction principles for natural numbers should be consistent with any consistent theory about any domain of discourse. Are they?

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=logicism). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/logicism/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=logicism&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/logicism/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- Koellner, Peter, “[Carnap on the Foundations of Logic and Mathematics](http://logic.harvard.edu/koellner/CFLM.pdf)” (PDF), unpublished manuscript, 2009.

## Related Entries

analytic/synthetic distinction | choice, axiom of | Dedekind, Richard: contributions to the foundations of mathematics | Frege, Gottlob | Frege, Gottlob: theorem and foundations for arithmetic | Gödel, Kurt | identity: of indiscernibles | Kant, Immanuel | Leibniz, Gottfried Wilhelm | plural quantification | Russell’s paradox | set theory | type theory

### Acknowledgments

The author is grateful for helpful comments on various earlier drafts from Julian Cole, Mauro Corneli, Salvatore Florio, Teresa Kouri, Lisa Shabel, Stewart Shapiro, Matthew Souba and Ed Zalta. Thanks are owed especially to John MacFarlane, who provided detailed, insightful and helpful refereeing comments on later but still ancestral drafts. The author is solely responsible for any defects that remain.

## Notes（原文脚注）

[^note-1]: These are called *double-abstraction* principles below; see §1.2.2 for explanation and discussion.

[^note-2]: Benacerraf (1981: 21)[^benacerraf-1981] claims that “If Frege was the first logicist, then he was also the last.” Naturally one’s assessment of this claim will turn on how broad is one’s conception of logicism.

[^note-3]: Lanier Anderson (2004)[^anderson-2004] argues that “Kant deploys a clear and defensible notion of concept containment” and that

> [o]nce we understand it, that notion of containment provides resources for a compelling argument that arithmetic must be synthetic, *sensu* Kant. (p. 503)

But the logicist will be unmoved by this: the rejoinder will be that the most appropriate sense of ‘analytic’, for the purposes of establishing an interesting logicist thesis about mathematics, is one that *departs* in carefully considered and well-motivated ways from analyticity *sensu* Kant.

[^note-4]: See Michael Friedman 1992 (p. 84). Another useful discussion of the role of the pure form of temporal intuition in Kant’s account of arithmetic is Parsons 1983.

[^note-5]: In his *Habilitationsschrift* of 1874, Frege wrote:

> *Die Elemente aller geometrischen Konstruktionen sind Anschauungen, und auf Anschauung verweist die Geometrie als Quelle ihrer Axiome. Da das Objekt der Arithmetik keine Anschaulichkeit hat, so können auch ihre Grundsätze aus der Anschauung nicht stammen.* (Frege 1967: 50)[^frege-1967]

We offer the following translation:

> The elements of all geometrical constructions are intuitions, and geometry points to intuition as the source of its axioms. Since the object of arithmetic lacks intuitiveness, so too are its basic laws unable to stem from intuition.

This early conviction of Frege’s to the effect that the ultimate justification for the axioms of geometry was to be found in intuition, was reprised in 1903, in “*Über die Grundlagen der Geometrie*” (see Frege 1967: 262)[^frege-1967].

[^note-6]: The date of 1853 in the English translation Dedekind (1996b: 793)[^dedekind-1996b] of the preface to the first edition of Dedekind’s later work *Was sind und was sollen die Zahlen?* is in error. The German original (Dedekind 1888: 339)[^dedekind-1888] has 1858.

[^note-7]: This passage is one of the most important ‘position statements’ ever written on foundational matters, and is worth quoting here in full. This translation, due to W. W. Beman and extensively revised by William Ewald, is from Dedekind (1996a: 767)[^dedekind-1996a]. Emphases have been added:

> In discussing the concept of the approach of a variable magnitude to a fixed limiting value—in particular, in proving the theorem that every magnitude which grows continually, but not beyond all limits, must certainly approach a limiting value—I took refuge in geometrical evidence. Even now I regard such invocation of geometric intuition [*Anschauung*] in a first presentation of the differential calculus as exceedingly useful from a pedagogic standpoint, and indeed it is indispensable, if one does not wish to lose too much time. But no one will deny that this form of introduction into the differential calculus can make no claim to being scientific. For myself this feeling of dissatisfaction was so overpowering that I resolved to meditate on the question until I should find a *purely arithmetical and perfectly rigorous foundation* [*Begründung*] for the principles of infinitesimal analysis. The statement is frequently made that the differential calculus deals with continuous quantities, yet an explanation of this continuity is nowhere given; even the most rigorous expositions of the differential calculus do not base their proofs upon continuity but they either appeal more or less consciously to geometric representations or to representations suggested by geometry, or they depend upon theorems which are never established in a purely arithmetical manner. Among these, for example, belongs the above-mentioned theorem, and a more careful investigation convinced me that this theorem, or any one equivalent to it, can be regarded as a more or less sufficient foundation for infinitesimal analysis. It only remained to discover *its true origin in the elements of arithmetic* [*sic*], and thereby to secure a real definition of the essence of continuity. I succeeded on November 24, 1858 …

[^note-8]: This English translation is from Dedekind (1996a: 767)[^dedekind-1996a]. The German original, in Dedekind (1872: 4)[^dedekind-1872] is: “*eine rein arithmetische und völlig strenge Begründung der Prinzipien der Infinitesimalanalysis*”.

[^note-9]: The reason why we speak here of ‘the Fregean’ is that Frege himself, in the *Grundgesetze*, did not treat of addition and multiplication on the natural numbers. He treated only zero and successor.

[^note-10]: It might be objected that our decimal place-notation ‘12’ is really to be regimented as $(1 \times 10) + 2$—which involves multiplication as well as addition. If *that* is how the Kantian is to be accommodated, then the composite singular term for ‘12’ in the $(0, s, +, \times)$—language of Peano arithmetic would be

$$ (s0 \times ssssssssss0) + ss0, $$

and the derivation of ‘$7+5=12$’ as

$$ sssssss0 + sssss0 = (s0 \times ssssssssss0) + ss0 $$

would involve appeal to the recursion axioms for multiplication, which are

$$\begin{align} & \forall x x \times 0 = 0; \\ & \forall x\forall y\, x \times sy = (x \times y) + x. \end{align}$$

The logicist will have derived these axioms too (whose variables are understood as ranging over natural numbers) from deeper, ‘logical’ principles involving expressions not occurring in the recursion axioms themselves. The same kind of reply, in principle, would deal with the even more exigent requirement that the place-notation numeral ‘12’ be regimented as $(1 \times(10^1)) + (2 \times(10^0))$, which now brings in exponentiation as well.

[^note-11]: If, instead of using the language of second-order logic, one were to have a two-sorted first-order logic in which properties are one of the sorts and in which there are singular terms $t$ denoting properties, then $\#$ could be used as a function symbol like $d(\ )$, so that $\#t$ could be a singular term denoting the number of things falling under the concept denoted by $t$. But we shall not be discussing such variants in what follows.

[^note-12]: We shall see in due course (§§2,3) what abstraction principle(s) the neo-logicists have put forward in their attempts to characterize the meaning of this number-abstraction operator. Some, like Wright and Tennant, use the variable-binding operator $\#x$; others, like Heck and Zalta, use the variable-free operator $\#$, and apply it to either second-order variables or predicates.

[^note-13]: This displayed pasigraph is just a useful abbreviation. Note that it has no free variables. So there is no need, here, for quantifiers to be prefixed in order to bind the variables $x$ and $y$. In the abbreviatory pasigraph given, the free occurrences of $x$ and $y$ in the part $$ [Fx \underset{\text{onto}}{\overset{1-1}{\mapsto}} Gy] $$ can be thought of as bound by the initial occurrence of $Rxy$. There are different but equivalent pasigraphic (abbreviatory) notations in the literature for registering the existence of a one-one, onto mapping between the $F$s and the $G$s; any one of them will do. What matters rather is the *definiens* which the pasigraph abbreviates.

[^note-14]: The reader is put on notice that the contrast here between single- and double-abstraction principles is a contrast drawn within a purposely narrowed class: abstraction principles in biconditional form that have *identities* on their left-hand sides. With the double-abstraction identity principles, the left-hand sides will be of the form $\#xFx = \#xGx$; whereas with single-abstraction identity principles they will be of the form $t = \#xFx$. There are of course many other kinds of abstraction principle in the literature which are correctly called ‘single-abstraction’ principles, but they are ones that do not deal with identities of the latter form on their left-hand sides. (Indeed, some of them are not even of biconditional form.) Examples of ‘single-abstraction’ principles of biconditional form whose left-hand sides are not identity statements are

$$ t \in \{x \mid x \in A \wedge \phi x\} \leftrightarrow (t \in A \wedge \phi t). $$

and $\beta$-conversion in the $\lambda$-calculus:

$$ [\lambda x_1 \ldots x_n\phi(x_1 ,\ldots ,x_n)]t_1 \ldots t_n \leftrightarrow \phi(t_1 ,\ldots ,t_n). $$

Such principles are being purposely excluded from consideration here as single-abstraction principles, because our focus is on the use made of single-abstraction principles by neo-Fregeans, which are all identity abstraction principles.

[^note-15]: As early as December 7, 1873 Cantor wrote to Dedekind that he had “found the reason why the totality [of real numbers] … *cannot* be correlated one-one with the totality [of natural numbers]” (see Ewald 1996: 846)[^ewald-1996]. The proof in question (which did not use his famous diagonal method) was published as Cantor 1874.

[^note-16]: As Richard Heck (1997a)[^heck-1997a] points out, Frege also developed the ‘Caesar’ objection to his doubly-abstractive definition of line-directions. The objection was that the definition would not enable us to distinguish England from the direction of the Earth’s axis.

[^note-17]: Exercise: Show that this set-abstraction principle logically implies the Axiom of Extensionality,

$$\forall x \forall y (\forall z (z \in x \leftrightarrow z \in y) \rightarrow x = y). $$

[^note-18]: Courtesy of Zalta’s definition (1999: 630)

$$ \#G =_{\textit{df}} \iota x(Ax \wedge \forall F(xF \leftrightarrow F \text{ is equinumerous with } G)) $$

[^note-19]: Explicit use of the label ‘Bad Company’ has an interesting early history. Dummett (1991: 188–9)[^dummett-1991] is quoted at length by Wright (1998: 344–5; §II, titled “Bad Company?”). Dummett’s complaint had been

> [I]f the context principle, as expounded by Wright, is enough to validate the ‘contextual’ method of introducing the cardinality operator, it must be enough to validate a similar means of introducing the [class] abstraction operator.

Dummett (1998: 375; title: “Neo-Fregeans: In Bad Company?”), reprises the criticism thus:

> In *Grundgesetze*, value-ranges are introduced in a manner precisely analogous to that in which Wright argued, in his book, that Frege ought to have introduced cardinal numbers …: and yet it was so far from being justified as to lead to actual contradiction.

Clearly, at the time of those writings of theirs quoted above, Tennant, Boolos, Dummett and Wright construed the ‘bad company’ for HP as consisting of BLV alone; and this construal endured through the late 1980s and even into the early 1990s. Subsequently, further formal discoveries were made, of yet other (double-)abstraction principles that are individually consistent, but jointly inconsistent (and some of them inconsistent with HP). The seminal paper in this regard is Boolos 1997. The problem highlighted by the proliferation of conflicting principles has been given the label ‘Embarrassment of Riches’ by Weir (2003)[^weir-2003]. But this label has not caught on. Instead, the ‘Bad Company’ label was happily extended so as to emphasize the worsened delinquency of the group with its newly admitted companions. This has induced a shift in our collective understanding of what comprises ‘Bad Company’, and what the Bad Company problem amounts to. An informative collection of essays on these more recent developments is Linnebo, ed. (2009). As Linnebo puts it in the abstract of his editorial Introduction,

> …the acceptable abstraction principles are surrounded by unacceptable (indeed often paradoxical) ones. This is the ‘bad company problem.’

[^note-20]: The reader is reminded that the variables $z$ and $w$ are bound in the right-hand side of this biconditional. See footnote 13.

[^note-21]: See Definition Z at the end of §40 of Volume I of the *Grundgesetze*, at p. 57.

[^note-22]: We have been using the mathematician’s ‘relation-slash’ notation $r \not\in r$ instead of the logician’s ‘sentence-prefix’ notation $\neg(r \in r)$.

[^note-23]: Fortunately, this has recently been remedied. The Arché project at St. Andrews has brought out an English translation of the *Grundgesetze*. See the Bibliographic reference to Frege 1893, and its citation to Ebert and Rossberg translation.

[^note-24]: Russell’s “Mathematical Logic as Based on the Theory of Types” (1908) is an accessible presentation of these ideas. The official, full development is *Principia Mathematica* (Whitehead and Russell 1910)[^whitehead-1910].

[^note-25]: The modern set-theoretic conception of an ordinal number is due to von Neumann. The very first ordinal is the empty set $\varnothing$. If $\alpha$ is an ordinal, then $\alpha \cup \{\alpha \}$ is the *successor* of $\alpha$. Beginning with $\varnothing$, and taking only successors, one obtains the finite ordinals. These are the usual set-theoretic surrogates for the natural numbers. The first transfinite ordinal, $\omega$, is the set of all finite ordinals. Every ordinal has a successor. But not every ordinal *is* a successor. Ordinals which are like $\omega$ in that they are not successors are called *limit* ordinals. Every ordinal is the set of all ordinals that precede it. A *cardinal* number is an ordinal that is not in 1-1 correspondence with any preceding ordinal. So a cardinal number is the first ordinal of ‘its size’. The finite ordinals are the finite cardinals. But in the transfinite, of course—$\omega$ and beyond—the cardinals are more thinly sprinkled among the ordinals. *Qua* cardinal number, $\omega$ is called $\aleph_0$. It is *countably infinite*. The first *uncountable* cardinal is $\aleph_1$, which is the first ordinal after $\aleph_0$ not in 1-1 correspondence with any ordinal preceding it.

[^note-26]: For this latter observation, the author is indebted to John MacFarlane.

[^note-27]: We do not say the finite von Neumann ordinals are *the* set-theoretic surrogates for the natural numbers, because of the well-known ‘Benacerraf point’ that there are other recursive progressions within the universe of (hereditarily finite) pure sets that could serve just as well—Zermelo’s finite ordinals, for example (see Benacerraf 1965)[^benacerraf-1965]. Interestingly, though, Boolos has argued that von Neumann’s finite ordinals are the most natural representatives, within a theory of extensions, of Frege’s finite cardinals (see Boolos 1987; see also Demopoulos 1998)[^boolos-1987][^demopoulos-1998].

[^note-28]: Cantor’s theorem (that every set has strictly more subsets than members) has the special case that $\wp(\omega)$ has more members than $\omega$ does, hence is uncountable.

[^note-29]: This was an unpublished lecture delivered in Cambridge, Massachusetts, at a joint meeting of the Mathematical Association of America and the American Mathematical Society, 29–30 December 1933. See Feferman’s introductory note to Gödel 1993/1995 (p. 36).

[^note-30]: John MacFarlane suggested that a “perhaps superior option” would be to require explicit domains $D$ in the abstracts, thus: $\{x \in D \mid \Phi(x)\}$. Then a free logic would not be needed, because, by Separation, the denotation for any such term would exist.

[^note-31]: Quine (1960: 267)[^quine-1960] advocates strongly for “the power of the notion of class to unify our abstract ontology”. He goes on to assert

> To surrender this benefit and face the old abstract objects again in all their *primeval disorder* would be a wrench …. [Emphasis added]

[^note-32]: Snapper (1979: 208)[^snapper-1979] contends that logicism survived the shift from type theory to set theory. Here is how he viewed matters:

> Of course, instead of *Principia*, one can use any other formal set theory just as well. Since today the formal set theory developed by Zermelo and Fraenkel (ZF) is so much better known than *Principia*, we shall from now on refer to ZF instead of *Principia*. ZF has only nine axioms and, although several of them are actually axiom schemas, we shall refer to all of them as “axioms”. The formulation of the logicist’s program now becomes: Show that all nine axioms of ZF belong to logic.

Against this, it could be maintained that the move from *Principia* to ZF represented an abandonment of the aspirations of logicism, and an acknowledgement that the foundations of mathematics can at best be provided within just one branch of mathematics itself, namely set theory.

Cook 2015 is a subtle and technically demanding study that supports a principled pessimism about the prospects for a suitably modified neologicist approach to a theory of sets (or value-ranges) that might avoid the disaster that befell Frege’s Basic Law V, and deliver enough in the way of sets to allow the neologicist to develop a version of Frege’s account of cardinal numbers. Cook limits himself to a consideration of only double-abstraction principles; but his conclusion must give this kind of neologicist serious pause. Cook 2016 pursues the topic further, revealing a virtually uninhabitable neologicist no-man’s land between Hume’s Principle (which is consistent) and Basic Law V (which of course is not). These negative reflections on the potential reach of neologicism continue a theme from the earlier work Cook 2002, which concluded that ‘the sort of abstraction needed to obtain a theory of the reals is rampantly inflationary’, and accordingly epistemologically suspect.

Boccuni 2013 has introduced a new twist in attempted reconstructions of Fregean foundations for number theory, with a system called ‘*Plural Grundgesetze*’, based on the relational concept $x\eta X$ (‘the individual $x$ is among the $X$s’). Its ‘Fregean devices’ include ‘the infamous Basic Law V’, along with a *Plural Comprehension Principle*

$$ \exists X\forall x(x\eta X \leftrightarrow \phi x) \text{ (where \(\phi\) does not contain \(X\) free)} $$

Contradiction is presumed to be avoided by replacing George Boolos’ plural semantics with Enrico Martino’s *Acts of Choice Semantics*. It is too early to judge whether these novel resources will prove to be a consistent mix.

[^note-33]: Although Frege more or less explicitly proved Frege’s Theorem in the *Grundlagen* (and proved it fully explicitly in the *Grundgesetze*), Frege himself never actually put his finger explicitly on the ‘it’ in question.

[^note-34]: For useful discussion, see MacFarlane 2002 (pp. 40–42), which concludes, in effect, that Frege was deterred by worry about the truth of HP (i.e., of Principle (A)), because of it similarity to Basic Law V. For Frege did not have the benefit of knowing that second-order logic with HP is consistent if Real Analysis is. So perhaps Frege himself deserves credit for being the first thinker to appreciate the force of the ‘Bad Company’ objection (in the sense it enjoyed when first deployed with that label—see footnote 19).

[^note-35]: The author is aware that the notion of a ‘significant part’ of a branch of mathematics requires further explication. For the time being, it is enough to note that what Quine called virtual set theory is a significant part of ZFC set theory; and PA is a significant part of Th(ℕ).

[^note-36]: The incompleteness phenomena affect *provability*. One could of course adopt a second-order axiomatization that secures every truth (about, say, ℕ) as a (second-order) logical consequence; but then one would have to live with the drawback that second-order logical consequence is not axiomatizable. See Rayo 2005.

[^note-37]: Wright appears, with hindsight, to have been rather too exclusively focused on the *Grundlagen*, and somewhat underinfluenced by Frege’s own logical maneuvers in the *Grundgesetze*. We note this assessment from Dummett (1991: 123)[^dummett-1991]:

> Crispin Wright devotes a whole section of his book … to demonstrate that, if we were to take the equivalence in question as an implicit or contextual definition of the cardinality operator, we would still derive the same theorems as Frege does. He could have achieved the same result with less trouble by observing that Frege himself gives just such a derivation of those theorems. He derives them all from that equivalence, with no further appeal to his explicit definition.

“[J]ust such a derivation”, of course, appears only in the *Grundgesetze*.

[^note-38]: As pointed out by Tennant (1987: 236–7)[^tennant-1987], Boolos’s model for FA works only for FA taken by itself; and that model

> will not serve its intended purpose when [FA] is embedded within a wider theory—such as the theory of sets—calling for models in which there are distinct infinities of objects.

The “theory of number …, like logic, is to apply to all subject matters.” The consistency of a logicist theory of number “is not to depend upon the particular subject matter over which numerical notions are deployed.” Boolos (1997: 260)[^boolos-1997] agrees:

> The worry is that … Frege Arithmetic … is incompatible with Zermelo–Fraenkel set theory plus standard definitions, on the usual and natural readings of the non-logical expressions of both theories.

(Note that Boolos is not a logicist; he admits only the standard logical operators as logical expressions.)

[^note-39]: As Dummett (1993: 441)[^dummett-1993] explains,

> an indefinitely extensible concept is one such that, if we can form a definite conception of a totality all of whose members fall under the concept, we can, by reference to that totality, characterize a larger totality all of whose members fall under it.

[^note-40]: Some philosophers of mathematics do not share this intuition; and some of those who do might be reluctant to make it a *sine qua non* of any successful logicist account. Thanks to both Julian Cole and Stewart Shapiro for raising this ‘structuralist’ point. The point is made also by Carnap (1931: 93)[^carnap-1931] in what was intended to be a sympathetic exposition of the aims and partial achievements of logicism. Here is the English translation taken from Carnap 1983 (p. 43):

> The natural numbers do not constitute a subset of the fractions but are merely correlated in obvious fashion with certain fractions. Thus the natural number 3 and the fraction 3/1 are not identical but merely correlated with one another. Similarly we must distinguish the fraction 1/2 from the real number correlated with it.

Carnap’s view here is deferential to the similar view of Russell, who in turn had inherited from Frege this need to resort to a form of structuralism. The inability to answer the inclusion question in turn derives from not taking seriously enough the need to explain how the various numbers are canonically *applied* in our theorizing not only about numbers but also about concrete things. A correct solution to the applicability problem could well point the way to an answer to the inclusion question. Real numbers are used for measuring continuous magnitudes in terms of some unit of measurement. When we say that a rod is 3 units-of-length (say, meters) long, we are in effect saying that the length of the rod, in meters, is 3. Equivalently: the number of units-of-length that comprise the length of the rod is 3. The latter is the familiar natural number 3.

[^note-41]: It is well known that by Gödel’s Second Incompleteness Theorem, no consistent, sufficiently strong theory $T$ of arithmetic can prove its own consistency-statement $\Con_T$. So the extended theory $T + \Con_T$ is of higher consistency-strength than the theory $T$ itself. In general, for consistent theories $T, T'$ containing a sufficiently strong fragment of arithmetic, theory $T'$ is of higher consistency strength than theory $T$ just in case $T'$ proves that $T$ is consistent. Usually this is done in one of two ways. Either $T'$ proves $\Con_T$ (the sentence of arithmetic expressing the consistency of $T)$; or $T'$ proves the existence of a model for (the axioms of) $T$. A vast range of mathematical theories can be, and have been, compared according to their consistency-strengths. These comparisons have involved fragments of arithmetic, fragments of real analysis, set theories, and type theories. The two ways in which strength can be increased in second-order theories of arithmetic is by allowing broader classes of substituends (complexity classes of formulae) in their axiom-scheme of comprehension, and in their axiom-scheme of mathematical induction. The main way in which strength can typically be increased in set theory is by postulating the existence of ever-larger cardinal numbers. The deep and puzzling phenomenon that has emerged is that consistency-strengths are *linearly* ordered. The modern program of Reverse Mathematics, due to Harvey Friedman (see Friedman 1975, 1976)[^friedman-1975][^friedman-1976], is the major source of such insights into the relative strengths of various mathematical theories. The best avenue into the relevant literature is Simpson 1999. For a thorough investigation of the question of consistency-strengths of various foundational theories that are pertinent to logicism, see Burgess 2005, especially Table E.

[^note-42]: It has been Michael Dummett, especially, who has advanced this interpretation.

[^note-43]: The normalization theorem is due to Prawitz (see Prawitz 1965)[^prawitz-1965].

[^note-44]: For a cogent critique of Carnap’s lack of appreciation of certain metamathematical subtleties in holding to his position that both logical and mathematical truths were analytic *in Carnap’s explicating sense*, see Koellner (Carnap ms in Other Internet Resources).

[^note-45]: By contrast, Wright’s proof-sketch “stops short of being a fully rigorous deduction” (Burgess 2005: 147)[^burgess-2005].

[^note-46]: The use of free logic for logicist purposes has also been explored more recently by Shapiro and Weir (2000).

[^note-47]: The condition of adequacy involving Schema N was put forward in Tennant 1984.

[^note-48]: We refer here to the works Parsons 1987, Heck 1996, Burgess 1998, Wehmeier 1999, Ferreira 2002, Boccuni 2010, 2011, 2013, and 2014.

[^note-49]: A formula is called $\Sigma^1_1$ if it is of the form $\exists F\phi$ and called $\Pi^1_1$ if it is of the form $\forall F\phi$, provided (in each case) that $\phi$ has no second-order quantifier. $\Delta^1_1$-Comprehension is the schema:

$$\forall x(\phi(x) \leftrightarrow \psi(x)) \to \exists G\forall x(Gx \leftrightarrow \phi(x))\,$$

where $\phi(x)$ is $\Sigma^1_1$, $\psi(x)$ is $\Pi^1_1$, and $G$ is not free in $\phi$.

[^note-50]: For a full account of the primitive expressions and well-formed formulae of PG, see (Boccuni 2010)[^boccuni-2010], at pp. 316–317, and (Boccuni 2011)[^boccuni-2011], at pp. 329–330. The first of these papers shows that second-order Peano arithmetic can be derived in PG. The second one furnishes a model-theoretic consistency proof for PG, based on ideas in (Heck 1996)[^heck-1996].

[^note-51]: Note that an affirmative answer to this question invites the reflection that, if Logic commits one to the existence of any thing or kind of thing, then such existence will be *necessitated*. The things in question will be *necessary* existents.

[^note-52]: This is properly classified as a demarcation problem because of a particular pre-formal view with which such a logicist methodology would be in tension. The view in question combines two main theses. The first thesis is that there is some clearly identifiable body of *mathematical* theorizing, employing mathematical concepts, whose eligibility for logicist reduction is in question. The second thesis is that the problem for the logicist would be to show how to ‘logicize’ this theorizing by (i) defining those mathematical concepts in purely logical terms, and then (ii) deriving as logical theorems the *translations* induced by those definitions of the erstwhile mathematical theorems.

[^note-53]: This label is used here in its more recently acquired sense, not its original one. See footnote 19.

[^anderson-2004]: Anderson, Lanier, 2004, “It Adds Up After All: Kant’s Philosophy of Arithmetic in Light of the Traditional Logic”, *Philosophy and Phenomenological Research*, LXIX(3): 501–540.

[^benacerraf-1965]: Benacerraf, Paul, 1965, “What numbers could not be”, *The Philosophical Review*, 74(1): 47–73.

[^benacerraf-1981]: –––, 1981, “Frege: The Last Logicist”, *Midwest Studies in Philosophy*, 6(1): 17–35.

[^boccuni-2010]: Boccuni, Francesca, 2010, “Plural *Grundgesetze*,” *Studia Logica*, 96(2): 315–330.

[^boccuni-2011]: –––, 2011, “On the Consistency of a Plural Theory of Frege’s *Grundgesetze*,” *Studia Logica*, 97(3): 329–345.

[^boccuni-2013]: –––, 2013, “Plural Logicism”, *Erkenntnis*, 78(5): 1051–1067.

[^boccuni-2014]: –––, 2014, “Minimal Logicism,” *Philosophia Scientiæ*, 18(3): 81–94.

[^boolos-1987]: Boolos, George, 1987, “The Consistency of Frege’s Foundations of Arithmetic”, in *On Being and Saying: Essays in Honor of Richard Cartwright*, Judith Jarvis Thompson, ed., Cambridge, MA, October: MIT Press, 3–20.

[^boolos-1997]: –––, 1997, “Is Hume’s Principle analytic?”, in *Language Thought and Logic: Essays in Honour of Michael Dummett*, Richard G. Heck Jnr, ed., Oxford: Clarendon Press, 245–61.

[^burgess-1998]: Burgess, John P., 1998, “On a consistent subsystem of Frege’s *Grundgesetze*,” *Notre Dame Journal of Formal Logic*, 39: 274–278.

[^burgess-2005]: –––, 2005, *Fixing Frege*, Princeton: Princeton University Press.

[^cantor-1874]: Cantor, Georg, 1874, “Über eine Eigenschaft des Inbegriffs aller reellen algebraischen Zahlen”, *Journal für die reine und angewandte Mathematik*, 77: 258–262.

[^cantor-1891]: –––, 1891, “Über eine elementare Frage der Mannigfaltigkeitslehre”, *Jahresbericht der Deutschen Mathematiker-Vereinigung*, 1: 75–78.

[^carnap-1931]: Carnap, Rudolf, 1931, “Die logizistische Grundlegung der Mathematik”, *Erkenntnis*, 2(1): 91–105.

[^carnap-1934]: –––, 1934, *Logische Syntax der Sprache*, Vienna: J. Springer.

[^carnap-1939]: –––, 1939, *Foundations of Logic and Mathematics*, International Encyclopedia, vol. 1, no. 3, Chicago: University of Chicago Press.

[^carnap-1983]: –––, 1983, “The logicist foundations of mathematics”, in *Philosophy of Mathematics: Selected Readings*, 2nd edition, Paul Benacerraf and Hilary Putnam, eds., Cambridge: Cambridge University Press, 41–52.

[^cook-2002]: Cook, Roy T., 2002, “The State of the Economy: Neo-logicism and Inflation”, *Philosophia Mathematica* (III), 10(1): 43–66.

[^cook-2015]: –––, 2015, “Frege’s Cardinals and Neo-Logicism”, *Philosophia Mathematica* (III), 24(1): 60–90.

[^cook-2016]: –––, 2016, “Abstraction and Four Kinds of Invariance (Or: What’s So Logical About Counting)”, *Philosophia Mathematica* (III), 25(1): 3–25.

[^dedekind-1872]: Dedekind, Richard, 1872, *Stetigkeit und Irrationale Zahlen*, Braunschweig: Vieweg & Sohn.

[^dedekind-1888]: –––, 1888, *Was sind und was sollen die Zahlen?*, Braunschweig: Vieweg.

[^dedekind-1996a]: –––, 1996a, “Continuity and Irrational Numbers”, in Ewald, ed., 1996, Volume II, 765–778.

[^dedekind-1996b]: –––, 1996b, “Was sind und was sollen die Zahlen?”, in Ewald, ed., 1996, Volume II, 787–833.

[^demopoulos-1998]: Demopoulos, William, 1998, “The Philosophical Basis of Our Knowledge of Number”, *Noûs*, 32(4): 481–503.

[^dummett-1991]: Dummett, Michael, 1991, *Frege: Philosophy of Mathematics*, Cambridge, Massachusetts: Harvard University Press.

[^dummett-1993]: –––, 1993, *The Seas of Language*, Oxford and New York: Oxford University Press.

[^dummett-1998]: –––, 1998, “Neo-Fregeans: In Bad Company?”, in *Philosophy of Mathematics Today*, Mathias Schirn, ed., Oxford: Clarendon Press, 368–388.

[^ewald-1996]: Ewald, William, 1996, *From Kant to Hilbert: A Source Book in the Foundations of Mathematics*, Volume II, Oxford: Clarendon Press.

[^ferreira-2002]: Ferreira, F. and K. F. Wehmeier, 2002, “On the Consistency of the $\Delta^{1}_1$-CA Fragment of Frege’s *Grundgesetze*,” *Journal of Philosophical Logic*, 31: 301–311.

[^fine-1998]: Fine, Kit, 1998, “The limits of abstraction”, in *Philosophy of Mathematics Today*, Mathias Schirn, ed., Oxford: Clarendon Press, 503–629.

[^fine-2002]: –––, 2002, *The Limits of Abstraction*, Oxford: Clarendon Press.

[^frege-1879]: Frege, Gottlob, 1879, *Begriffsschrift, eine der arithmetischen nachgebildete Formelsprache des reinen Denkens*, Halle: Louis Nebert.

[^frege-1884]: –––, 1884, *Die Grundlagen der Arithmetik: eine logisch mathematische Untersuchung über den Begriff der Zahl*, Hildesheim: Georg Olms Verlagsbuchhandlung, reprinted 1961.

[^frege-1893]: –––, 1893; *Grundgesetze der Arithmetik* (Volume I), Hildesheim: Georg Olms Verlagsbuchhandlung, reprinted 1962; translated and edited by Philip A. Ebert and Marcus Rossberg, as *Gottlob Frege: Basic Laws of Arithmetic*, Oxford: Oxford University Press, 2013.

[^frege-1967]: –––, 1967, *Kleine Schriften*, edited by Ignacio Angelelli, Wissenschaftliche Buchgesellschaft, Darmstadt and G. Olms, Hildesheim.

[^friedman-1975]: Friedman, Harvey, 1975, “Some systems of second order arithmetic and their use”, *Proceedings of the 1974 International Congress of Mathematicians*, 1: 235–242.

[^friedman-1976]: –––, 1976, “Subsystems of Second Order Arithmetic with Restricted Induction I, II, abstracts”, *Journal of Symbolic Logic*, 41(2): 557–559.

[^friedman-1992]: Friedman, Michael, 1992, *Kant and the Exact Sciences*, Cambridge, MA: Harvard University Press.

[^geach-1975]: Geach, Peter, 1975, “Review of M. Dummett, Frege: Philosophy of Language”, *Mind*, 84: 436–499.

[^gentzen-1934]: Gentzen, Gerhard, 1934/1935 [1969], “Untersuchungen über das logische Schliessen”, *Mathematische Zeitschrift*, I, II: 176–210, 405–431. Translated as “Investigations into Logical Deduction”, in *The Collected Papers of Gerhard Gentzen*, edited by M. E. Szabo, North-Holland, Amsterdam, 1969, pp. 68–131.

[^gödel-1993]: Gödel, Kurt, 1993/1995, “The present situation in the foundations of mathematics”, in *Collected Works, Volume III: Unpublished Essays and Lectures*, Solomon Feferman, John W. Dawson, Jr., Warren Goldfarb, Charles Parsons, and Robert N. Solovay, eds., New York and Oxford: Oxford University Press, 45–53.

[^grattan-guinness-2000]: Grattan-Guinness, Ivor, 2000, *The Search for Mathematical Roots: Logics, Set Theories and the Foundations of Mathematics from Cantor through Russell and Goedel*, Princeton: Princeton University Press.

[^hale-2001]: Hale, Bob and Crispin Wright, 2001, *The Reason’s Proper Study: Essays towards a Neo-Fregean Philosophy of Mathematics*, Oxford: Clarendon Press.

[^heck-1996]: Heck, Richard, 1996, “The Consistency of Predicative Fragments of Frege’s *Grundgesetze der Arithmetik*,” *History and Philosophy of Logic*, 17: 209–220.

[^heck-1997a]: –––, 1997a, “The Julius Caesar Objection”, in *Language, Thought and Logic: Essays in Honour of Michael Dummett*, Richard G. Heck Jnr, ed., Oxford: Oxford University Press, 273–308.

[^heck-1997b]: –––, 1997b, “Finitude and Hume’s Principle”, *Journal of Philosophical Logic*, 26(6): 589–617.

[^linnebo-2009]: Linnebo, Ø., 2009, “Introduction”, *Synthese*, 170(3):321–329.

[^macfarlane-2002]: MacFarlane, John, 2002, “Frege, Kant, and the Logic in Logicism”, *The Philosophical Review*, 111(1): 25–65.

[^mancosu-2016]: Mancosu, Paolo, 2016, *Abstraction and Infinity*, Oxford: Oxford University Press.

[^parsons-1965]: Parsons, Charles, 1965, “Frege’s theory of number”, in *Philosophy in America*, Max Black, ed., Ithaca: New York: Cornell University Press, 180–203.

[^parsons-1983]: –––, 1983, “Kant’s philosophy of arithmetic (1969), with postscript”, in *Mathematics in Philosophy: Selected Essays*, Ithaca, NY: Cornell University Press, 110–149.

[^parsons-1987]: Parsons, Terence, 1987, “On the Consistency of the First-Order Portion of Frege’s Logical System,” *Notre Dame Journal of Formal Logic*, 28: 161–68.

[^prawitz-1965]: Prawitz, Dag, 1965, *Natural Deduction: A Proof-Theoretical Study*, Stockholm: Almqvist & Wiksell.

[^quine-1960]: Quine, W. V. O., 1960, *Word and Object*, Cambridge, MA: MIT Press.

[^quine-1969]: –––, 1969, *Set Theory and Its Logic*, revised edition, Cambridge, MA: The Belknap Press of Harvard University Press.

[^rayo-2005]: Rayo, Augustin, 2005, “Logicism Reconsidered”, in *The Oxford Handbook of Philosophy of Mathematics and Logic*, Stewart Shapiro, ed., New York: Oxford University Press, 203–235.

[^rumfitt-1999]: Rumfitt, Ian, 1999, “Frege’s logicism”, *Proceedings of the Aristotelian Society*, Supplementary Volume, 73: 151–180.

[^russell-1908]: Russell, Bertrand, 1908, “Mathematical Logic as Based on the Theory of Types”, *American Journal of Mathematics*, 30(3): 222–262.

[^schroeder-heister-1987]: Schroeder-Heister, P., 1987, “A Model-Theoretic Reconstruction of Frege’s Permutation Argument,” *Notre Dame Journal of Formal Logic*, 28: 69–79.

[^shapiro-2000]: Shapiro, Stewart, 2000, “Frege meets Dedekind: a Neologicist Treatment of Real Analysis”, *Notre Dame Journal of Formal Logic*, 41(4): 335–364.

[^shapiro-2000-2]: Shapiro, Stewart and Alan Weir, 2000, “ ‘Neo-logicist’ logic is not epistemically innocent”, *Philosophica Mathematica*, 8: 160–189.

[^simpson-1999]: Simpson, Stephen G., 1999, *Subsystems of Second order Arithmetic*, Berlin, Heidelberg, New York: Perspectives in Mathematical Logic. Springer.

[^smiley-1970]: Smiley, Timothy, 1970, *Lecture Notes in Mathematical Logic (unpublished)*, Cambridge.

[^snapper-1979]: Snapper, Ernest, 1979, “The Three Crises in Mathematics: Logicism, Intuitionism, and Formalism”, *Mathematics Magazine*, 52(4): 207–216.

[^studd-2016]: Studd, J. P., 2016, “Abstraction Reconceived,” *British Journal for the Philosophy of Science*, 67(2): 579–615.

[^tarski-1956]: Tarski, Alfred, 1956 [1933], “The Concept of Truth in Formalized Languages”, in *Logic, Semantics, Metamathematics*, J. H. Woodger, ed., Oxford: Clarendon Press, 152–278. First published, in Polish, in 1933.

[^tennant-1984]: Tennant, Neil, 1984, “Constructive logicism: an adequate theory of number”, *Minutes of the Cambridge University Moral Sciences Club*, October 23rd.

[^tennant-1987]: –––, 1987, *Anti-Realism and Logic: Truth as Eternal*, Clarendon Library of Logic and Philosophy, Oxford University Press, June.

[^tennant-2009]: –––, 2009, “Natural logicism via the logic of orderly pairing”, in *Logicism, Intuitionism, Formalism: What has become of them?*, Sten Lindström, Erik Palmgren, Krister Segerberg, and Viggo Stoltenberg-Hansen, eds., Synthese Library, Springer Verlag, 91–125.

[^tennant-2022]: –––, 2022, *The Logic of Number*, Oxford: Oxford University Press.

[^tennant-nd]: –––, forthcoming, “Frege’s Class Theory and the Logic of Sets,” in Kai Wehmeier & Thomas Piecha (ed.), *Peter Schroeder-Heister on Proof-Theoretic Semantics* (Series: Outstanding Contributions to Logic), Berlin: Springer.

[^wehmeier-1999]: Wehmeier, K. F., 1999, “Consistent Fragments of *Grundgesetze* and the Existence of Non-Logical Objects,” *Synthese*, 121: 309–328.

[^weir-2003]: Weir, A., 2003, “Neo-Fregeanism: An Embarrassment of Riches”, *Notre Dame Journal of Formal Logic*, 44(1): 13–48.

[^whitehead-1910]: Whitehead, A. N. and B. Russell, 1910, *Principia Mathematica*, Cambridge: Cambridge University Press.

[^wright-1983]: Wright, Crispin, 1983, *Frege’s Conception of Numbers as Objects*, Aberdeen: Aberdeen University Press.

[^wright-1998]: –––, 1998, “On the Harmless Impredicativity of N$^=$ (‘Hume’s Principle’)”, in *Philosophy of Mathematics Today*, Mathias Schirn, ed., Oxford: Clarendon Press, 339–368.

[^zalta-1993]: Zalta, Edward N., 1993, “Twenty-Five Basic Theorems in Situation and World Theory”, *Journal of Philosophical Logic*, 22(4): 385–428.

[^zalta-1999]: –––, 1999, “Natural Numbers and Natural Cardinals as Abstract Objects: A Partial Reconstruction of Frege’s *Grundgesetze* in Object Theory”, *Journal of Philosophical Logic*, 28(6): 619–660.
