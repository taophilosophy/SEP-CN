# truthlikeness — complex-frameworks（supplement）

> （《truthlikeness》词条补充材料，源：plato.stanford.edu/entries/truthlikeness/complex-frameworks.html）

#### Supplement to Truthlikeness

## Extending the likeness approach to first-order and higher-order frameworks

Simple propositional examples are convenient for the purposes of illustration, but what the likeness approach needs is some evidence that it can transcend such simple examples. Can the likeness program be generalized to arbitrarily complex frameworks? For example, does the idea extend even to first-order frameworks the possible worlds of which may well be infinitely complex?

There is no straightforward, natural or obvious way to construct distance or likeness measures on worlds considered as non-denumerably infinite collections of basic or “atomic” states. But a fruitful way of implementing the likeness approach in frameworks that are more interesting and realistic than the toy propositional weather framework, involves cutting the space of possibilities down into manageable chunks. This is not just an *ad hoc* response to the difficulties imposed by infinite states, but is based on a principled view of the nature of inquiry – of what constitutes an *inquiry*, a *question*, a *query*, a *cognitive problem*, or a *subject matter*. Although these terms might seem to signify quite different notions they all have something deep in common.

Consider the notion of a *query* or a *question*. Each well-formed question $Q$ receives an answer in each complete possible state of the world. Two worlds are *equivalent* with respect to the question $Q$ if they receive the *same* answer in both worlds. Given that $Q$ induces an equivalence relation on worlds, the question partitions the logical space into a set of mutually exclusive and jointly exhaustive cells: $\{C_1, C_2 , \ldots ,C_i , \ldots \}$. Each cell $C_i$ is a complete possible answer to the question $Q$. And each *incomplete* answer to $Q$ is tantamount to the union, or disjunction, of some collection of the complete answers. For example, the question *what is the number of the planets?* partitions the set of worlds into those in which $N=0$, those in which $N=1,\ldots$, and so on. The question *what is the state of the weather?* (relative to our three toy factors) partitions the set of worlds into those in which is hot, rainy and windy, those in which it is hot, rainy and still, … and so on. (See Oddie 1986a.) In other words, the so-called “worlds” in the simple weather framework are in fact surrogates for large classes of worlds, and in each such class the answer to the coarse-grained weather question is the same. The elements of this partition are all complete answers to the weather question, and distances between the elements of the partition can be handled rather easily as we have seen. Essentially the same idea can be applied to much more complex questions.

Niiniluoto characterizes the notion of a *cognitive problem* in the same way, as a partition of a space of possibilities. And this same explication has been remarkably fruitful in clarifying the notions of *aboutness* and of a *subject matter* (Oddie 1986a, Lewis 1988).

Each inquiry is based on some question that admits of a range of possible complete answers, which effect a partition $\{C_1, C_2 , \ldots ,C_n , \ldots \}$ of the space of worlds. Incomplete answers to the question are equivalent to disjunctions of those complete answers which entail the incomplete answer. Now, often there is a rather obvious measure of distance between the elements of such partitions, which can be extended to a measure of distance of an arbitrary answer (whether complete or partial) from the true answer.

One rather promising source of natural partitions (Tichý 1976, Niiniluoto 1977) are Hintikka’s *distributive normal forms* (Hintikka 1963). These are smooth generalizations of the familiar maximal conjunctions of propositional frameworks used above. What corresponds to the maximal conjunctions are known as *constituents*, which, like maximal conjunctions in the propositional case, are jointly exhaustive and mutually exclusive. Constituents lay out, in a very perspicuous manner, all the different ways individuals can be related to each other – relative, of course, to some collection of basic attributes. (These correspond to the collection of atomic propositions in the propositional case.) The basic attributes can be combined by the usual boolean operations into complex attributes which are also like the maximal conjunctions, in that they form a partition of the class of individuals. These complex predicates are called $Q$-predicates in the simple monadic case, and *attributive constituents* in the more general case. Constituents specify, for each member in this set of mutually exclusive and jointly exhaustive complex attributes, whether or not that complex attribute is exemplified.

In the simplest case a framework of three basic monadic attributes $(F,G$ and $H)$ gives rise to eight complex attributes: – Carnap’s $Q$-predicates:

$$\tag{\(Q_1\)} F(x) \amp G(x) \amp H(x)$$ $$\tag{\(Q_2\)} F(x) \amp G(x) \amp{\sim}H(x)$$

$\ \vdots$

$$\tag{\(Q_8\)} {\sim}F(x) \amp{\sim}G(x) \amp{\sim}H(x)$$

The simplest constituents run through these $Q$ – predicates (or *attributive constituents*) specifying for each one whether or not it is instantiated.

$$\tag{\(C_1\)} \exists xQ_1 (x) \amp \exists xQ_2 (x) \amp \cdots \amp \exists xQ_7 (x) \amp \exists xQ_8 (x) $$ $$\tag{\(C_2\)} \exists xQ_1 (x) \amp \exists xQ_2 (x) \amp \cdots \amp \exists xQ_7 (x) \amp{\sim}\exists xQ_8 (x) $$

$\ \vdots$

$$\tag{\(C_{255}\)} {\sim}\exists xQ_1 (x) \amp{\sim}\exists xQ_2 (x) \amp \cdots \amp {\sim}\exists xQ_7 (x) \amp \exists xQ_8 (x) $$ $$\tag{\(C_{256}\)} {\sim}\exists xQ_1 (x) \amp{\sim}\exists xQ_2 (x) \amp \cdots \amp {\sim} \exists xQ_7(x) \amp{\sim}\exists xQ_8 (x) $$

In effect the partition induced by the set constituents corresponds to the question: *Which $Q$-predicates are instantiated*? A complete answer to that question will specify one of the constituents, an incomplete answer will specify a disjunction of such.

Note that the last constituent in this listing, $C_{256}$, is logically inconsistent. Given that the set of $Q$-predicates is jointly exhaustive, each individual has to satisfy one of them, so at least one of them has to be instantiated. Once such inconsistent constituents are omitted, every sentence in a monadic language (without identity or constants) is equivalent to a disjunction of a unique set of these constituents. (In the simple monadic case here there is only one inconsistent constituent, but in the general case there are many inconsistent constituents. Identifying inconsistent constituents is equivalent to the decision problem for first-order logic.)

For example, the sentence $\forall x (F(x) \amp G(x) \amp H(x))$ is logically equivalent to:

$$\tag{\(C_{64}\)} \exists xQ_1 (x) \amp{\sim} \exists xQ_2 (x) \amp \cdots \amp {\sim}\exists xQ_7 (x) \amp{\sim} \exists xQ_8 (x). $$

The sentence $\forall x({\sim}F(x) \amp G(x) \amp H(x))$ is logically equivalent to:

$$\tag{\(C_{128}\)} {\sim}\exists xQ_1(x) \amp \exists xQ_2(x) \amp \cdots \amp {\sim}\exists xQ_7(x) \amp{\sim}\exists xQ_8(x). $$

The sentence $\forall x({\sim}F(x) \amp{\sim}G(x) \amp{\sim}H(x))$ is logically equivalent to:

$$\tag{\(C_{255}\)} {\sim}\exists xQ_1 (x) \amp{\sim}\exists xQ_2 (x) \amp \cdots \amp {\sim}\exists xQ_7(x) \amp \exists xQ_8(x). $$

More typically, a sentence is equivalent to disjunction of constituents. For example the sentence $\forall x(G(x) \amp H(x))$ is logically equivalent to:

$$ C_{64}\vee C_{128}. $$

And the sentence $\forall x (F(x)\vee G(x)\vee H(x))$ is logically equivalent to:

$$ C_1\vee C_2 \vee \ldots \vee C_{253}\vee C_{254}. $$

Before considering whether distributive normal forms (disjunctions of constituents) can be generalized to more complex and interesting frameworks (involving relations and greater quantificational complexity) it is worth thinking about how to define distances between these constituents, since they are the simplest of all.

If we had a good measure of distance between constituents then presumably the distance of some disjunction of constituents from one particular constituent could be obtained using the right extension function (§1.4.2) whatever that happens to be. And then the distance of an arbitrary expressible proposition from the truth could be defined as the distance of its normal form from the true constituent.

As far as distances between constituents go, there is an obvious generalization of the city-block (or symmetric difference) measure on the corresponding maximal conjunctions (or propositional constituents): namely, the size of the *symmetric difference* of the sets of $Q$-predicates associated with each constituent. So, for example, since $C_1$ and $C_2$ differ on the instantiation of just one $Q$-predicate (namely $Q_8)$ the distance between them would be 1. At the other extreme, since $C_2$ and $C_{255}$ disagree on the instantiation of every $Q$-predicate, the distance between them is 8 (maximal).

Niiniluoto first proposed this as the appropriate distance measure for these constituents in his 1977, and since he found a very similar proposal in Clifford, he called it the *Clifford measure*. Since it is based on symmetric differences it yields a function that satisfies the triangular inequality (the distance between $X$ and $Z$ is no greater than the sum of the distances between $X$ and $Y$ and $Y$ and $Z)$.

Note that on the Clifford measure the distance between $C_{64}$ (which says that $Q_1$ is the only instantiated $Q$-predicate) and $C_{128}$ (which says that $Q_2$ is the only instantiated $Q$-predicate) is the same as the distance between $C_{64}$ and $C_{255}$ (which says that $Q_8$ is the only instantiated $Q$-predicate).

$$\tag{\(C_{255}\)} {\sim}\exists xQ_1(x) \amp{\sim}\exists xQ_2(x) \amp \cdots \amp {\sim}\exists xQ_7 (x) \amp \exists xQ_8 (x) $$

$C_{64}$ says that everything has $F$, $G$ and $H$; $C_{128}$, that everything has ${\sim}F, G$ and $H$; $C_{255}$, that everything has ${\sim}F, {\sim}G$ and ${\sim}H$. If the likeness intuitions in the weather framework have anything to them, then $C_{128}$ is closer to $C_{64}$ than $C_{255}$ is. Tichý (1976 and 1978) captured this intuition by first measuring the distances between $Q$-predicates using the city-block measure. Then the basic idea is to extend this distances between sets of $Q$-predicates by identifying the “minimal routes” from one set of such $Q$-predicates to another. The distance between two sets of $Q$-predicates is the distance along some minimal route.

Suppose that two normal forms feature the same number of constituents. That is, the two sets of $Q$-predicates associated with two constituents are the same size. Let a *linkage* be any 1-1 mapping from one set to the other. Let the *breadth* of the linkage be the average distance between linked items. Then according to Tichý the distance between two constituents (or their associated sets of $Q$-predicates) is the breadth of the narrowest linkage between them. If one constituent $C$ contains more $Q$-predicates than the other then a linkage is defined as a surjection from the larger set to the smaller set, and the rest of the definition is the same.

This idea certainly captures the intuition concerning the relative distances between $C_{128},$ $C_{64}$ and $C_{255}$. But it suffers the following defect: it does not satisfy the triangular inequality. This is because in a linkage between sets with different numbers of members, some $Q$-predicates will be unfairly represented, thereby possibly distorting the intuitive distance between the sets. This can be remedied, however, by altering the account of a linkage to make them *fair*. The details need not detain us here (for those see Oddie 1986a) but in a fair linkage each $Q$-predicate in a constituent receives the same weight in the linkage as it possesses in the constituent itself.

The simple Clifford measure ignores the distances between the $Q$-predicates, but it can be modified and refined in various ways to take account of such distances (see Niiniluoto 1987).

Hintikka showed that the distributive normal form theorem can be generalized to first-order sentences of any degree of relational or quantificational complexity. Any sentence of a first-order sentence comes with a certain quantificational *depth* – the number of its overlapping quantifiers. So, for example, analysis in the first-order idiom would reveal that (1) is a depth-1 sentence; (2) is a depth-2 sentence; and (3) is a depth-3 sentence.

**(1)**

Everyone loves himself.

**(2)**

Everyone who loves another is loved by the other.

**(3)**

Everyone who loves another loves the other’s lovers.

We could call a proposition *depth-d* if the shallowest depth at which it can be expressed is $d$. Hintikka showed how to define both attributive constituents and constituents of depth-$d$ recursively, so that every depth-$d$ proposition can be expressed by a disjunction of a unique set of (consistent) depth-$d$ constituents.

Constituents can be represented as finite tree-structures, the nodes of which are all like $Q$-predicates – that is, strings of atomic formulas either negated or unnegated. Consequently, if we can measure distance between such *trees* we will be well down the path of measuring the truthlikeness of depth-$d$ propositions – it will be some function of the distance of constituents in its normal form from the true depth-d constituent. And we can measure the distance between such trees using the same idea of a minimal path from one to the other. This too can be spelt out in terms of fair linkages between trees, thus guaranteeing the triangular inequality.

This program for defining distance between expressible propositions has proved quite flexible and fruitful, delivering a wide range of intuitively appealing results, at least in simple first-order cases. And the approach can be further refined – for example, by means of Carnap’s concept of a family of properties.

There are yet more extension problems for the likeness program. First-order theories can be infinitely deep – that is to say, there is no finite depth at which such a theory theory can be expressed. The very feature of first-order constituents that makes them manageable – their finite structure – ensures that they cannot express propositions that are not finitely axiomatizable in a first-order language. Clearly it would be desirable for an account of truthlikeness to be able, in principle, to rank propositions that go beyond the expressive power of first-order sentences. First-order sentences lack the expressive power of first-order theories in general, and first-order languages lack the expressive resources of higher-order languages. A theory of truthlikeness that applies only to first-order sentences, while not a negligible achievement, would still have limited application.

There are plausible ways of extending the normal-form approach to these more complex cases. The relative truthlikeness of infinitely deep first-order propositions can be captured by taking limits as depth increases to infinity (Oddie 1978, Niiniluoto 1987). And Hintikka’s normal form theorem, along with suitable measures of distance between higher-order constituents, can be extended to embrace higher-order languages (These higher-order “permutative constituents” are defined in Oddie 1986a and a normal form theorem proved.) Since there are propositions that are only expressible by a non-finitely axiomatizable theory in first-order logic that can be expressed by a single sentence of higher-order logic this greatly expands the reach of the normal-form approach.

Although scientific progress sometimes seems to consist in the accumulation facts about the existence of certain kinds of individuals (witness the recent excitement evoked by the discovery of the Higgs boson, for example) mostly the scientific enterprise is concerned with causation and laws of nature. L. J. Cohen has accused the truthlikeness program of completely ignoring this aspect of the aim of scientific inquiry.

> … the truth or likeness to truth that much of science pursues is of a rather special kind – we might call it ‘physically necessary truth’ (Cohen 1980, 500)

The discovery of instances of new kinds (as well as the inability to find them when a theory predicts that they will appear under certain circumstances) is generally welcomed because of the light such discoveries throw on the structure of the laws of nature. The trouble with first-order languages is that they lack adequate resources to represent genuine laws. Extensional first-order logic embodies the Humean thesis that there are no necessary connections between distinct existences. At best first-order theories can capture pervasive, but essentially accidental, regularities.

There are various ways of modeling laws. According to the theory of laws favored by Tooley 1977 and Armstrong 1983, laws of nature involve higher-order relations between first-order universals. These, of course, can be represented easily in a higher-order language (Oddie 1982). But one might also capture lawlikeness in a first-order modal language supplemented with sentential operators for natural necessity and natural possibility (Niiniluoto 1983). And an even simpler representation in terms of nomic conjunctions in a propositional framework, which utilizes the simple city-block measure on partial constituents, has recently been developed in Cevolani, Festa and Kuipers 2012.

Another problem for the normal-form approach involves the fact that most interesting theories in science are not expressible in frameworks generated by basic properties and relations alone, but rather require continuous magnitudes – world-dependent functions from various entities to numbers. All the normal-form based accounts (even those developed for the higher-order) are for systems that involve basic properties and relations, but exclude basic functions. Of course, magnitudes can be finitely approximated by Carnap’s families of properties, and relations between those can be represented in higher-order frameworks, but if those families are infinite then we lose the finitude characteristic of regular constituents. Once we lose those finite representations of states, the problem of defining distances becomes intractable again.

There is a well-known way of reducing $n$-argument functions to $n+1$-place relations. One could represent a magnitude of $n$-tuples of objects as a relation between $n$ objects and numbers. One would have to include the set of real or complex numbers in the domain of individuals, or else have multiple domains at the lowest level. However, not only is that a somewhat *ad hoc* solution to the problem, but no interesting applications based on such a reduction have been explored. So each space has to be treated differently and the resulting theory lacks a certain unity. It would clearly be preferable to be able to give a unified treatment with different applications. It would also be preferable to be able to treat basic magnitudes on a par with basic properties and relations in the generation of logical space. Niiniluoto (in his 1987) showed how to extend the likeness approach to functional spaces (see also Kieseppa 1996) but so far there is no good extension of the distributive normal-form approach that both combines functions with properties and relations, and reduces the infinite complexity that these generate to finite or manageable proportions. Until such an account is forthcoming, the normal form approach does not provide a comprehensive theory of closeness to truth.

The problem of complexity might force a reconsideration of the methodology here. Instead of trying to define specific distance measures in a bottom-up piecemeal way, a more modest, more tractable, top-down approach might be to posit the existence of a (possibly partial) relation of likeness on worlds, satisfying various plausible structural features and desirable principles. Assuming these principles are consistent, this would in turn determine a class of numerical distance functions (all those that represent or realize them). Plausible principles could then be explored to narrow the class of admissible likeness functions. This idea is developed a little further in §1.5. But before we go there the most important objection to the likeness approach needs to be addressed.
