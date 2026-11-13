# Plural Quantification
**First published Wed Oct 27, 2004; substantive revision Tue Aug 18, 2026**

*Linnebo, Øystein*

Ordinary English contains different forms of quantification over objects. In addition to the usual *singular* quantification, as in

**(1)**

There is an apple on the table

there is *plural* quantification, as in

**(2)**

There are some apples on the table.

Ever since Frege, formal logic has favored the two singular quantifiers $\forall{x}$ and $\exists{x}$ over their plural counterparts $\forall{xx}$ and $\exists{xx}$ (to be read as *for any things* $xx$ and *there are some things* $xx)$. But in recent decades it has been argued that we have good reason to admit among our primitive logical notions also the plural quantifiers $\forall{xx}$ and $\exists{xx}$ (Boolos 1984 and 1985a)[^boolos-1984][^boolos-1985a].

More controversially, it has been argued that the resulting formal system with plural as well as singular quantification qualifies as “pure logic”; in particular, that it is universally applicable, ontologically innocent, and perfectly well understood. In addition to being interesting in its own right, this thesis will, if correct, make plural quantification available as an innocent but extremely powerful tool in metaphysics, philosophy of mathematics, and philosophical logic. For instance, George Boolos has used plural quantification to interpret monadic second-order logic[^note-1] and has argued on this basis that monadic second-order logic qualifies as “pure logic”. Plural quantification has also been used in attempts to defend logicist ideas, to account for set theory, and to eliminate ontological commitments to mathematical objects and complex objects.

## 1. The Languages and Theories of Plural Quantification

The logical formalisms that have dominated in the analytic tradition ever since Frege do not allow for plural quantification. In introductory logic courses students are therefore typically taught to paraphrase away plural locutions. For instance, they may be taught to render “Alice and Bob are hungry” as “Alice is hungry & Bob is hungry”, and “There are some apples on the table”, as “$\Exists{x} \Exists{y} (x$ is an apple on the table & $y$ is an apple on the table & $x \ne y)$”. However, not only are such paraphrases often unnatural, but they may not even be available. One of the most interesting examples of plural locutions which resist singular paraphrase is the so-called Geach-Kaplan sentence:

**(3)**

Some critics admire only one another

This sentence provably has no singular first-order paraphrase using only the predicates occurring in the sentence itself.[^note-2]

How are we to formalize such sentences? The traditional view, defended for instance by Quine, is that all paraphrases must be given in classical first-order logic, if necessary supplemented with set theory. In particular, Quine suggests that (3) should be formalized as

$$\begin{align} \tag{\(3'\)}\label{ex3prime} \Exists{S}(&\Exists{u}\mstop u \in S \amp \Forall{u}(u\in S \rightarrow Cu)\ \amp \\ &\Forall{u}\Forall{v}(u\in S \amp \textit{Auv} \rightarrow v\in S \amp u\ne v)) \end{align}$$

(1973: 111 and 1982: 293).[^note-3]

In two important articles from the 1980s George Boolos challenges this traditional view (Boolos 1984 and 1985a)[^boolos-1984][^boolos-1985a]. He argues that it is simply a prejudice to insist that the plural locutions of natural language be paraphrased away. Instead he suggests that just as the singular quantifiers $\Forall{x}$ and $\Exists{x}$ get their legitimacy from the fact that they represent certain quantificational devices in natural language, so do their plural counterparts $\Forall{xx}$ and $\Exists{xx}$. For there can be no doubt that in natural language we use and understand the expressions “for any things” and “there are some things”.[^note-4] Since these quantifiers bind variables that take name (rather than predicate) position, they are *first-order* quantifiers, albeit *plural* ones.

### 1.1 Regimenting plural quantification

I will now describe a simple formal language which is widely used in philosophy to regiment plural quantification as it occurs in English and other natural languages.

*The formal language $L_{\textrm{PFO}}$*. Let the formal language $L_{\textrm{PFO}}$ (for *Plural First-Order*) be as follows.

1. $L_{\textrm{PFO}}$ has the following terms (for every natural number $i$):
2. singular variables $x_i$
3. plural variables $xx_i$
4. singular constants $a_i$
5. plural constants $aa_i$
6. $L_{\textrm{PFO}}$ has the following predicates:
7. two dyadic logical predicates = and $\prec$ (to be thought of as *identity* and the relation *is one of*)
8. non-logical predicates $R^{n}_i$ all of whose argument places are singular (for every adicity $n$ and every natural number $i)$
9. $L_{\textrm{PFO}}$ has the following formulas:
10. $R^{n}_i (t_1,\ldots, t_n)$ is a formula when $R^{n}_i$ is an $n$-adic predicate and $t_j$ are singular terms
11. $t \prec T$ is a formula when $t$ is a singular term and $T$ a plural term
12. $\neg \phi$ and $\phi \amp \psi$ are formulas when $\phi$ and $\psi$ are formulas
13. $\Exists{v}\mstop \phi$ and $\Exists{vv}\mstop \phi$ are formulas when $\phi$ is a formula and $v$ is a singular variable and $vv$ a plural one
14. the other connectives are regarded as abbreviations in the usual way.

In $L_{\textrm{PFO}}$ we can formalize a number of English claims involving plurals. For instance, (2) can be formalized as

$$ \tag{\(2'\)}\label{ex2prime} \Exists{xx} \Forall{u} (u\prec xx \rightarrow Au \amp Tu) $$

And the Geach-Kaplan sentence (3) can be formalized as

$$\begin{align} \tag{\(3''\)}\label{ex3pprime} \Exists{xx} [&\Forall{u}(u\prec xx \rightarrow Cu)\ \amp \\ &\Forall{u}\Forall{v}(u\prec xx \amp \textit{Auv} \rightarrow v\prec xx \amp u\ne v)]. \end{align}$$

However, the language $L_{\textrm{PFO}}$ has one severe limitation. We see this by distinguishing between two kinds of plural predication. A predicate $P$ taking plural arguments is said to be *distributive* just in case it is analytic that: $P$ holds of some things $xx$ if and only if $P$ holds of each $u$ such that $u\prec xx$.[^note-5] For instance, the predicate “is on the table” is distributive, since it is analytic that some things $xx$ are on the table just in case each of $xx$ is on the table. A predicate $P$ that isn’t distributive is said to be *non-distributive* or *collective*.[^note-6] For instance, the predicate “form a circle” is non-distributive, since it is not analytic that whenever some things $xx$ form a circle, each of $xx$ forms a circle. Another example of non-distributive plural predication is the second argument-place of the logical predicate $\prec$: for it is not true (let alone analytic) that whenever $u$ is one of $xx, u$ is one of each of $xx$. It is therefore both natural and useful to consider a slightly richer language:

> *The formal language $L_{\textrm{PFO}+}$*. The language $L_{\textrm{PFO}+}$ allows non-distributive plural predicates other than $\prec$. We do this by modifying the definition of $L_{\textrm{PFO}}$ so as to allow predicates $R^{n}_i$ that take one or more *plural* arguments. These predicates can be either logical or non-logical.[^note-7]

Should we also allow predicates with argument places that take both *singular* and *plural* arguments? Lots of English predicates work this way, for instance “… is/are on the table”. So if our primary interest was to analyze natural language, we would probably have to allow such predicates. However, for present purposes it is simpler not to allow such predicates. We will anyway soon allow pluralities that consist of just one thing.[^note-8]

For now, the formal languages $L_{\textrm{PFO}}$ and $L_{\textrm{PFO}+}$ will be interpreted only by means of a translation of them into ordinary English, augmented by indices to facilitate cross-reference (Boolos 1984: 443–5 [1998a: 67–9]; Rayo 2002: 458–9)[^boolos-1984][^rayo-2002]. (More serious semantic issues will be addressed in Section 4, where our main question will be whether our theories of plural quantification are ontologically committed to any sort of “set-like” entities.) The two clauses of this translation which are immediately concerned with plural terms are

**(4)**

$\Tr(x_i \prec xx_j) = \textrm{it}_i$ is one of them$_j$

**(5)**

$\Tr(\Exists{xx_j}\mstop \phi) =$ there are some things$_j$ such that $\Tr(\phi)$

The other clauses are obvious, for instance: $\Tr(\phi \amp \psi) = (\Tr(\phi)$ and $\Tr(\psi))$. This translation allows us to interpret all sentences of $L_{\textrm{PFO}}$ and $L_{\textrm{PFO}+}$, relying on our intuitive understanding of English. It is useful to consider some examples. Applying $\Tr$ to (\ref{ex2prime}), say, yields:

**(2″)**

There are some things$_1$ such that for everything$_2$ (if it$_2$ is one of them$_1$, then it$_2$ is an apple and it$_2$ is on the table).

### 1.2 The Theories PFO and PFO+

We will now describe a theory *PFO* of plural first-order quantification based on the language $L_{\textrm{PFO}}$. Let’s begin with an axiomatization of ordinary first-order logic with identity. For our current purposes, it is convenient to axiomatize this logic as a natural deduction system, taking all tautologies as axioms and the familiar natural deduction rules governing the singular quantifiers and the identity sign as rules of inference. We then extend in the obvious way the natural deduction rules for the singular quantifiers to the plural ones.

Next we need some axioms which for suitable formulas $\phi(x)$ allow us to talk about the $\phi$s. In ordinary English the use of plural locutions generally signals a concern with two or more objects. But the existence of two or more objects may not be semantically required; for instance, “The students who register for this class will learn a lot” seems capable of being true even if only one student registers. It is therefore both reasonable and convenient to demand only that there be at least one object satisfying $\phi(x).$ (Most people who write on the subject make this concession.) This gives rise to the *plural comprehension axioms*, which are the instances of the schema

$$ \tag{Comp} \Exists{u} \phi(u) \rightarrow \Exists{xx} \Forall{u} (u\prec xx \leftrightarrow \phi(u)) $$

where $\phi$ is a formula in $L_{\textrm{PFO}}$ that contains “$u$” and possibly other variables free but contains no occurrence of “$xx$”. (That is, if something is $\phi$ then there are some things such that everything is one of them if and only if it is $\phi$.) In order fully to capture the idea that all pluralities are non-empty, we also adopt the axiom

$$ \tag{6} \Forall{xx} \Exists{u} (u \prec xx). $$

(That is, for any things, there is something that is one of them.)

Let *PFO*+ be the theory based on the language $L_{PFO+}$ which arises in an analogous way, but which in addition has the following axiom schema of indiscernibility, stating that coextensive pluralities satisfy the same formulas:

$$ \tag{7} \Forall{xx}\Forall{yy} [\Forall{u}(u \prec xx \leftrightarrow u \prec yy) \rightarrow(\phi(xx) \leftrightarrow \phi(yy))] $$

(That is, for any things$_1$ and any things$_2$ (if something is one of them$_1$ if and only it is one of them$_2$, then they$_1$ are $\phi$ if and only if they$_2$ are $\phi)$.) This is a plural analogue of Leibniz’s law of indiscernibility of identicals, and as such needs to be restricted to formulas $\phi$ that don’t set up intensional contexts.

While the theories PFO and PFO+ represent what is today the most traditional form of plural logic, there are divergent views that restrict the plural comprehension schema. Even if a plurality is nothing over and above the objects it comprises, these objects need not be properly circumscribed. And on certain metaphysical views, reality as a whole resists proper circumscription (Yablo 2006; Linnebo 2010; Spencer 2012; Hossack 2014; Rumfitt 2018; Florio and Linnebo, ch. 12; Fujimoto 2025)[^fujimoto-2025][^hossack-2014][^rumfitt-2018][^spencer-2012][^yablo-2006]. Based on considerations of this sort, Florio and Linnebo (*op. cit.*) develop an alternative *critical* plural logic.

*Note on terminology*. For ease of communication we will use the word “plurality” without taking a stand on whether there really exist such entities as pluralities. Statements involving the word “plurality” can always be rewritten more longwindedly without use of that word. For instance, the above claim that “all pluralities are non-empty” can be rewritten as “whenever there are some things $xx$, there is something $u$ which is one of the things $xx$”. Where an ontological claim $is$ made, this will be signalled by instead using the locution “plural entity”.

## 2. Plural Quantification vs. Second-Order Quantification

By “second-order logic” we understand a logic that extends ordinary first-order logic by allowing for quantification into *predicate* position. For instance, from “$a$ is an apple” we can in second-order logic infer “$\Exists{F}\mstop Fa$”. But the plural logics described above extend ordinary first-order logic in a different way, namely by allowing quantification into *plural argument* position. But predicates and plural noun phrases belong to different syntactic and semantic categories. For instance, the former consists of expressions that are unsaturated (in Frege’s sense) — that is, that contain gaps or argument places — whereas the latter consists of expressions that are saturated (Higginbotham 1998: sect. 7; Oliver and Smiley 2001 and 2016; Rayo and Yablo 2001: sect. X; Simons 1997; Williamson 2003: sect. IX; Yi 2005; Florio and Linnebo 2021)[^florio-2021][^higginbotham-1998][^oliver-2001][^oliver-2016][^rayo-2001][^simons-1997][^williamson-2003]. Accordingly, second-order quantification and plural quantification are generally regarded as different forms of quantification. In this section I discuss some of the differences and similarities.

### 2.1 Plural quantification and monadic second-order logic

(Readers less interested in technical issues may want to skim this section.) Boolos observed that it is possible to interpret monadic second-order logic in the theory PFO.[^note-9] Let *MSO* be some standard axiomatization of (full impredicative) monadic second-order logic in some suitable language $L_{\textrm{MSO}}$ (Shapiro 1991: ch. 3; Boolos *et al.* 2002: ch. 22)[^shapiro-1991]. Boolos first defines a translation $\Tr'$ that maps any formula of $L_{\textrm{MSO}}$ to some formula of $L_{\textrm{PFO}}$. This definition, which proceeds by induction on the complexity of the formulas of $L_{\textrm{MSO}}$, has as its only non-trivial clauses the following two, which are concerned with the second-order variables:

$$ \tag{8} \Tr'(X_jx_i) = x_i \prec xx_j $$ $$ \tag{9} \Tr'(\Exists{X_j}\mstop\phi) = \Exists{xx_j}\mstop\Tr'(\phi) \lor Tr'(\phi*) $$

where $\phi*$ is the result of substituting $x_i \ne x_i$ everywhere for $X_j x_i$. The idea behind these two clauses is to replace talk about concepts (or whatever entities one takes the monadic second-order variables to range over) with talk about the objects that fall under these concepts. Thus, instead of saying that $x_i$ falls under the concept $X_j$, we say that $x_i$ is one of $xx_j$. The only difficulty is that some concepts have no instances, whereas all pluralities must encompass at least one thing. But the possibility that a concept be uninstantiated is accommodated by the second disjunct on the right-hand side of (9).

By induction on derivations in MSO one easily proves that each theorem of MSO is mapped to some theorem of PFO. Moreover, it is easy to define a “reverse” translation that maps formulas of $L_{\textrm{PFO}}$ to formulas of $L_{\textrm{MSO}}$ and to prove that this translation maps theorems of the former to theorems of the latter. This shows that PFO and MSO are mutually interpretable. A similar result can be proved about PFO+ and an extension MSO+ of MSO which allows predicates of (first-level) concepts, provided MSO+ contains an axiom schema to the effect that coextensive concepts are indiscernible.

It is important to be clear on what the mutually interpretability of PFO and PFO+ with respectively MSO and MSO+ does and does not show (Florio and Linnebo 2021: sect. 4.2)[^florio-2021]. It shows that these two pairs of theories are equivalent for most technical purposes. But by itself it does not show anything about these two pairs of theories’ being equivalent in any of the more demanding senses that philosophers often care about (such as having the same epistemic status, ontological commitments, or degree of analyticity). (For instance PFO is mutually interpretable with atomic extensional mereology, which philosophers tend to find much more problematic than PFO.) In order to show that the two pairs of theories are equivalent in some philosophically important respect $F$, we would need to show that the above translations preserve $F$-ness.

### 2.2 Relations

Although plural quantification provides a fairly natural interpretation of quantification over (monadic) *concepts*, it provides no natural interpretation of quantification over (polyadic) *relations*.

This limitation can be overcome (at least for technical purposes) if there is a pairing function on the relevant domain, that is, if there is a function $\pi$ such that $\pi(u, v) = \pi(u', v')$ just in case $u = u'$ and $v = v'$. For then quantification over dyadic relations can be represented by plural quantification over ordered pairs. Moreover, by iterated applications of the ordered pair function we can represent $n$-tuples and thus also quantification over $n$-adic relations. The question is how this pairing function is to be understood. One option is to proceed as in mathematics and simply postulate the existence of a pairing function as an abstract mathematical object. But this option has the obvious disadvantage of stepping outside of what most people are willing to call “pure logic”. A cleverer option, explored in the Appendix to Lewis 1991 and in Hazen 1997 and 2000, is to simulate talk about ordered pairs using only resources that arguably are purely logical. It turns out that talk about ordered pairs can be simulated in monadic *third-order* logic, given some plausible extra assumptions. Monadic third-order logic can in turn be interpreted either in a theory which combines plural quantification with mereology (Lewis 1991: ch. 3; Burgess and Rosen 1997: II.C.1)[^burgess-1997][^lewis-1991] or in terms of higher-level plural quantification (Section 2.4).

### 2.3 Modal contexts

Another way in which plural quantification and second-order quantification come apart emerges in modal contexts. It is often a contingent matter whether an object falls under a concept. Although I am wearing shoes, I might not have done so. So there is a concept $F$ under which I fall but might not have fallen. In contrast, it seems that being one of some objects is never contingent. Consider the people $aa$ who are all and only the people currently wearing shoes. Then not only am I one of these people, but this seems to hold of necessity (assuming the existence of the relevant objects). Removing me from this plurality of people would just result in a different plurality. For the plurality $aa$ to be the plurality it is, it must include precisely the objects that it in fact includes. So in any world in which the objects $aa$ exist at all, I must be one of them. True, I might not have been wearing shoes. But even so I would have been one of $aa$, only then $aa$ would not have been all and only the people wearing shoes. Plural names and variables thus seem to be rigid in a way that is analogous to the familiar rigidity of singular names and variables: in any world in which a plural term denotes at all, it denotes the same objects. In particular, it is widely believed that pluralities are subject to the following two principles:

$$ \tag{10} u \prec xx \rightarrow \Box(\EExists xx \rightarrow u \prec xx) $$ $$ \tag{11} \neg(u \prec xx) \rightarrow \Box(\EExists u \amp \EExists xx \rightarrow \neg(u \prec xx)) $$

where $\EExists xx$ and $\EExists u$ are suitable formalizations of the claims that respectively $xx$ and $u$ exist.[^note-10]

### 2.4 Higher levels of plural quantification?

One way of going beyond PFO+ would be by allowing quantification into predicate positions, including those of predicates taking plural arguments. Doing so would result in an extension which stands to PFO+ as ordinary (singular) second-order logic stands to ordinary (singular) first-order logic. Such extensions will not be considered here: for whether they are legitimate, and if so what axioms they may support, has less to do with plurals and plural quantification than it does with predication and quantification over the semantic values of predicates.[^note-11]

What $is$ relevant for present purposes is whether there is some form of “super-plural” quantification that stands to ordinary plural quantification as ordinary plural quantification stands to singular quantification. If so, let’s call this *second-level* plural quantification. More generally, we may attempt to introduce plural quantification of any finite level. This would result in a theory which for technical purposes is just like a simple type theory (Hazen 1997: 247; Linnebo 2003: sect. IV; Rayo 2006)[^hazen-1997][^linnebo-2003][^rayo-2006][^rayo-2006-2].

It is not hard to develop formal languages and theories of higher-level plural quantification (Rayo 2006)[^rayo-2006][^rayo-2006-2]. One option is to introduce a separate set of variables for each level of such quantification, say “*xxx*”, etc. for second-level plurals and the relation $xx \prec_2$ *xxx* to be understood in analogy with the relation $x \prec xx$ (Rayo 2006)[^rayo-2006][^rayo-2006-2]. (See Linnebo and Rayo 2012 for extensions to transfinite levels and comparison of the resulting theories with those of ordinary set theory.)[^linnebo-2012] Another option is to use a single set of “all-purpose” variables whose values can be pluralities of any level (Oliver and Smiley 2016, ch. 15; Simons 2016; and Florio and Linnebo 2021, sect. 11.7)[^florio-2021][^oliver-2016][^simons-2016]. This option is considerably simpler and more elegant and therefore enjoys increasing popularity.

Can these formal theories of higher-level plural quantification (whether the first option or the second) be justified by considerations like those that justify the theories PFO and PFO+? Boolos and many other philosophers deny that higher-level plural quantification can be thus justified. Two kinds of arguments are given for this view. Firstly, it is argued that a plurality is always a plurality of *things*. But since plural quantification is ontologically innocent, there are no such things as pluralities. There is thus nothing that can be collected into a second-level plurality (McKay 2006: 46–53 and 137–139)[^mckay-2006]. Secondly, ordinary plural quantification is justified by the fact that it captures certain quantificational devices of English and other natural languages. But English and other natural languages contain no higher-level plural quantification (Lewis 1991: 70–71)[^lewis-1991].

Both arguments are controversial. Concerning the first, it is not clear why ontology should be relevant to the legitimacy of higher-level plurals quantification. It should be sufficient that the base-level objects can be organized in certain complex ways. For instance, the second-level plurality based on Cheerios organized as oo oo oo should be no more ontologically problematic than the first-level plurality based on the same objects organized as oooooo, although the former has an additional level of structure or articulation (Linnebo 2003: 87–8)[^linnebo-2003].

The second of the above two arguments is also problematic. To begin with, the claim that there are no higher-level plural locutions in natural language is almost certainly false. In Icelandic, for instance, the number words have plural forms which count, not individual objects, but *pluralities* of objects that form natural groups. Here is an example:

| *einn skór* | means | one shoe |
| --- | --- | --- |
| *einir skór* | means | one pair of shoes |
| *tvennir skór* | means | two pairs of shoes |

This allows us to talk about pairs of shoes as a second-level plurality rather than as a first-level plurality of objects such as *pairs*. (More examples involving foreign languages can be found in Grimau 2021a.) For an English example, consider a video game in which any number $n$ of teams can compete in an $n$-way competition. Then the following sentence seems to involve a superplural term:

**(12)**

These people, those people, and these other people compete against each other. (Linnebo and Nicolas 2008)[^linnebo-2008][^nicolas-2008]

(See also Oliver and Smiley 2004: 654–656, 2005: 1063, and 2016, ch. 15; Ben-Yami 2013; Simons 2016; Florio and Linnebo 2021, ch. 9; Grimau 2021a and 2021b; and Payton 2025.)[^ben-yami-2013][^florio-2021][^oliver-2004][^payton-2025][^simons-2016]

Moreover, the very idea that the legitimacy of higher-level plural quantification is decided by the existence or non-existence of higher-level plural locutions in English and other natural languages is problematic (Hazen 1993: 138 and 1997: 247; Linnebo 2003: 87; Rayo 2006)[^hazen-1993][^hazen-1997][^linnebo-2003][^rayo-2006][^rayo-2006-2]. What really matters is presumably whether we can iterate the principles and considerations on which our understanding of ordinary first-level plural quantification is based: if we can, then higher-level plural quantification will be justified in much the same way as ordinary first-level plural quantification; and if not, then not. Thus, even if there were no higher-level plural locutions in natural languages, this would provide little or no evidence for the stronger — and philosophically more interesting — claim that there can be no iteration of the step from the singular to the plural in *any* language spoken by intelligent agents. Moreover, any evidence of this sort could be defeated by pointing to independent reasons why higher-level plural locutions are scarce in natural languages. One such independent reason may simply be that ordinary speakers aren’t very concerned about their ontological commitments and thus find it more convenient to express facts involving second-level pluralities by positing objects to represent the first-level pluralities (for instance by talking about two *pairs* of shoes) rather than by keeping track of additional grammatical device for second-level plurals (as in the above example from Icelandic).

## 3. The Logicality Thesis

It is often claimed that the theories PFO and PFO+ qualify as “pure logic”. We will refer to this (admittedly vague) claim as *the Logicality Thesis*. Since the corresponding languages are interpreted by the translation $\Tr$ into ordinary English, this is a claim about the logicality of certain axioms and inferences rules of ordinary English.[^note-12]

Even before the Logicality Thesis is made more precise, it is possible to assess its plausibility for at least some of the axioms and inference rules of PFO and PFO+. First there are the tautologies and the inference rules governing identity and the singular quantifiers. There is broad consensus that these qualify as logical. Next there are the inference rules governing the plural quantifiers. Since these rules are completely analogous to the rules governing the singular quantifiers, it can hardly be denied that they too qualify as logical. Then there are the indiscernibility axioms and the axiom that all pluralities are non-empty. These axioms are unproblematic because they can plausibly be taken to be analytic. What remains are the plural comprehension axioms, where things are much less clear. For these axioms have no obvious singular counterparts, and their syntactical form indicates that they make existential claims. So it is not obvious that these axioms can be taken to be purely logical.

This is not to say that it has not *struck* people as obvious that the plural comprehension axioms are purely logical. For instance, Boolos asserts without argument that the translation of each plural comprehension axiom into English “expresses a *logical* truth if any sentence of English does” (Boolos 1985b: 342 [1998a: 167]; his emphasis)[^boolos-1985b].

In order to assess the Logicality Thesis in a more principled way, more will have to be said about what it might mean for a theory to be “purely logical”. So I will now survey some of the features commonly thought to play a role in such a definition. Although people are free to use the word “logic” as they please, it is important to get clear on what different usages entail; in particular, theories that qualify as purely logical are often assumed to enjoy a variety of desirable philosophical properties such as epistemic and ontological innocence. In the next section, where various applications of plural quantification will be discussed, I will carefully note which strains of the notion of logicality our theories PFO and PFO+ must possess for the various applications of them to succeed.

Perhaps the least controversial candidate for a defining feature of logic is its *topic neutrality*. A logical principle is valid in any kind of discourse, no matter what kind of objects this discourse is concerned with. For instance, modus ponens is valid not only in physics and mathematics but in religion and in the analysis of works of fiction. Frege captures the idea nicely when he says that a logical principle is valid in “the widest domain of all; […] not only the actual, not only the intuitable, but everything thinkable” (Frege 1884: 21)[^frege-1884]. Thus, whereas the principles of physics are valid only in the actual world and in worlds that are nomologically similar to it, the principles of logic govern everything *thinkable*. If one of these principles is denied, “complete confusion ensues” (*ibid*.).

Another feature widely believed to be defining of logic is its *formality*: the truth of a principle of logic is guaranteed by the *form* of thought and/or language and does not in any way depend upon its *matter*. What this feature amounts to will obviously depend on how the distinction between form and matter is understood. The most popular explication of the distinction between form and matter derives from the widely shared view that no objects exist by conceptual necessity (Field 1993; Yablo 2000)[^field-1993][^yablo-2000]. On this view it is natural to regard anything having to do with the existence of objects and with their particular characteristics as belonging to the matter of thought rather than to its form. This gives rise to two features that are often regarded as defining of logic. Firstly, logic has to be *ontologically innocent*; that is, a principle of logic cannot introduce any new ontological commitments (Boolos 1997; Field 1984)[^boolos-1997][^field-1984]. Secondly, the basic notions of logic must not discriminate between different objects but must treat them all alike. This latter idea is often spelled out as the requirement that logical notions must be invariant under permutations of the domain of objects (Tarski 1986)[^tarski-1986].

A third feature which is often regarded as defining of logic is its (alleged) *epistemic primacy*. Primitive logical notions can be grasped without relying on non-logical notions; and logical truths, if knowable, can be known independently of non-logical truths. Assume, for instance, that certain set-theoretic notions or truths must be regarded as extra-logical. Then our grasp of the primitive logical notions, or knowledge of logical truths, cannot depend on or involve any of this set-theoretic material.

The key question, then, is whether the plural comprehension axioms enjoy these features of logicality. As we will see shortly, substantial doubts have been raised, especially concerning these axioms’ ontological innocence and epistemic primacy.

## 4. Applications of Plural Quantification

I will now outline some applications of the theories PFO and PFO+. In the previous section three strains of the notion of logicality were disentangled. Special attention will be paid to the question which of these three strains PFO and PFO+ must possess for the applications to succeed.

### 4.1 Establishing the Logicality of Monadic Second-Order Logic

As we saw in Section 2.1 Boolos defined an interpretation of the theory MSO of monadic second-order logic in the theory PFO of plural quantification. He sought to use this translation to establish the logicality of MSO. Doing so will require two steps. The first step is to argue that PFO is pure logic, that is, to establish the full Logicality Thesis (however exactly it is interpreted). The second step is to argue that the interpretation of MSO in PFO preserves logicality.

Some of the challenges facing the first step will be examined in Section 5. The second step too should not be underestimated. Perhaps the greatest worry here is that Boolos’s translation renders expressions from one category (that of monadic predicates) in terms of expressions from another category (that of plural noun phrases). For instance, “… is an apple” is rendered as “the apples”. But these categories are very different (Section 2).

However, since the thesis that MSO is pure logic is very abstract, much of its cash value will lie in its applications. And given the mutual interpretability of MSO and PFO, it is likely that many applications of the logicality of the former can be served equally well by the logicality of the latter. This reduces somewhat the importance of carrying out the second step.

### 4.2 Logicism

Both Fregean and post-Fregean logicism make essential use of second-order quantification. Frege defined the various objects of pure mathematics as extensions of concepts, and his famous Basic Law V stated that two concepts $F$ and $G$ have the same extension just in case they are co-extensive:

$$ \tag{V} û\mstop Fu = û\mstop Gu \leftrightarrow \Forall{u}(Fu\leftrightarrow Gu) $$

But as is well known, Russell’s paradox shows that the second-order theory with (V) as an axiom is inconsistent.

Philosophers have attempted to rescue some ideas of Fregean logicism by using axioms weaker than (V). One of the most important such attempts is Bob Hale and Crispin Wright’s *neo-logicism*, which gives up Frege’s theory of extensions but holds on to the central idea of his definition of cardinal numbers, namely that the number of $F$s is identical to the number of $G$s just in case the $F$s and the $G$s can be one-to-one correlated. This has become known as *Hume’s Principle*, and can be formalized as

$$ \tag{HP} Nu.Fu = Nu\mstop Gu \leftrightarrow F\approx G $$

where $F\approx G$ says there is a relation that one-to-one correlates the $F$s and the $G$s. The second-order theory with (HP) as an axiom is consistent and allows us to derive all of ordinary (second-order Peano-Dedekind) arithmetic, using some very natural definitions (see the entry on Frege’s Logic, Theorem, and Foundations for Arithmetic).

Even more modest is Boolos’s *sub-logicism*, which rejects the idea (endorsed by both logicists and neo-logicists) that there are logical objects, but insists that Frege’s definition of the *ancestral* of a relation can be used to show, as against Kant, that at least some non-trivial mathematics is analytic (Boolos 1985b)[^boolos-1985b]. Recall that a relation $R$ stands to its ancestral $\Rarel$ as the relation *is a parent of* stands to *is an ancestor of*. (More precisely, $\Rarel$ holds between two objects $x$ and $y$ just in case $x$ and $y$ are connected through a finite sequence of objects each of which bears $R$ to its successor.) Frege gives a second-order definition of the ancestral relation $\Rarel$ by laying down that $x$ and $y$ are related by $\Rarel$ just in case $y$ has every property that is had by $x$’s $R$-successors and inherited under the $R$-relation:

$$\begin{align}\tag{Def \(\Rarel\)} x\Rarel y \leftrightarrow \Forall{F}[&\Forall{u}(x\Rrel u \rightarrow Fu)\ \amp \\ &\Forall{u}(Fu \amp u\Rrel v \rightarrow Fv) \rightarrow Fy] \end{align}$$

Using this definition, Frege 1879 proves some non-trivial mathematical truths, such as that the ancestral $\Rarel$ is transitive and that, for any functional relation $R$, the $R$-ancestors of any object are $\Rarel$-comparable. That is, he proved:

$$\text{Functional}(R) \amp x\Rarel y \amp x\Rarel z \rightarrow y\Rarel z \lor z\Rarel y. $$

It has been suggested that PFO be used to accommodate the post-Fregean logicists’ need for second-order quantification. Since the ancestral of a dyadic predicate can be defined using only monadic second-order quantification, PFO does indeed serve the logical needs of Boolos’s sub-logicism.[^note-13] But since the neo-logicist definition of $F\approx G$ uses dyadic second-order logic, PFO alone does not have sufficient expressive power to accommodate the needs of neo-logicism.

Can neo-logicists overcome this problem? Various strategies have been attempted. One is to simulate dyadic second-order quantification in some suitable extension of PFO, as discussed in Section 2.2[^note-14]. Another is to rework Fregean logicism in a way that eschews all use of polyadic second-order logic in favor of the logical resources afforded by plural logic. For example, Aldo Antonelli (2010) and Francesca Boccuni (2023) propose to regard equinumerosity (or some kindred notion) as primitive. See also Boccuni 2013 for an attempt that relies on plural logic coupled with a thin understanding of relations.

Which strains of the Logicality Thesis are needed for these applications to succeed? Since these logicists attempt to show that parts of mathematics are analytic (or at least knowable *a priori*), this would require that PFO be analytic (or at least knowable *a priori*), which in turn is likely to require that PFO enjoy some form of cognitive primacy. Moreover, PFO would have to be either ontologically innocent or committed only to entities whose existence is conceptually necessary (or at least establishable *a priori*).

### 4.3 Set Theory

Another application of the Logicality Thesis is concerned with set theory. One may for a variety of reasons want to talk about and quantify over collections of sets (Uzquiano 2003)[^uzquiano-2003]. For instance, one may want to assert

**(13)**

There are some sets which are all and only the non-self-membered sets.

If we formalize this as

$$ \tag{\(13'\)} \Exists{R} \Forall{x} (Rx \leftrightarrow x\not\in x), $$

how is the quantifier $\exists{R}$ to be understood? It clearly cannot be taken to range over all sets, as this would lead straight to Russell’s paradox: (13′) would then assert the existence of the Russell-set. Three other responses are prominent in the literature.

The first response is that $\exists{R}$ ranges over *classes* but that some classes are too large (or otherwise unsuited) to be sets. In particular, (13) asserts the existence of the Russell-class, which isn’t a set. This response has been found problematic because it postulates the existence of different kinds of “set-like” entities (Boolos 1984: 442 [1998a: 66] and 1998b: 35)[^boolos-1984]. It has also been objected that this response only postpones the problem posed by (13). For it would also be true that

**(14)**

There are some classes which are all and only the non-self-membered classes.

What kind of entity would this collection of classes be? A super-class? If so, we will be forced to postulate higher and higher levels of classes. Lewis (1991: 68) argues that Russell’s paradox is still inescapable because, when we consider all set-like entities, we realize that the following is true:

**(15)**

There are some set-like things which are all and only the non-self-membered set-like things.

However, Hazen (1993: 141–2) has pointed out that Lewis’s objection violates essential type-restrictions. Classes of different levels belong to different logical types, just as concepts of different levels do. So Lewis’s attempt to talk about all set-like entities in one fell swoop involves an attempt to quantify across different logical types. But this violates type restrictions in the same way as an attempt to quantify simultaneously over objects and concepts of all different levels. Although we can quantify over *each* level of classes, we can never quantify over *all levels simultaneously*.

The second response is that (13) asserts the existence of a set $R$, but that $R$ isn’t in the range of the quantifier $\forall{x}$. This prevents us from instantiating the quantifier $\forall{x}$ with $R$, which means that we cannot draw the fatal conclusion that $R$ is a member of itself just in case it isn’t. However, this response entails that the quantifier $\forall{x}$ cannot be chosen to range over absolutely all sets; for if it could be so chosen, we would not be able deny that $R$ is in this range of quantification. This means that the universe of sets has a certain *inexhaustibility*: whenever we have formed a conception of quantification over some range of sets, we can define a set which isn’t in this range (Dummett 1981: ch. 15 and 1991: ch. 24; Glanzberg 2004; Parsons 1977)[^dummett-1981][^dummett-1991][^glanzberg-2004][^parsons-1977]. However, this response has been criticized for being, at best hard to state, and at worst self-refuting (Boolos 1998b: 30; Lewis 1991: 68; Williamson 2003: sect. V)[^boolos-1998b][^lewis-1991][^williamson-2003]. (See also Rayo and Uzquiano 2006 for a number of essays discussing whether absolutely general quantification is possible.)[^rayo-2006][^rayo-2006-2]

Because of the difficulties involved in the first two responses, a third response has become popular in recent years (Boolos 1984 and 1985a; Burgess 2004; Cartwright 2001; Rayo and Uzquiano 1999; Uzquiano 2003)[^boolos-1984][^boolos-1985a][^burgess-2004][^cartwright-2001][^rayo-1999][^uzquiano-2003]. This is that the quantifier $\exists{R}$ is a plural quantifier (and would thus be better written as $\exists{rr})$ and that plural quantification is ontologically innocent. Therefore (13) does not assert the existence of any “set-like” entity over and above the sets in the range of the quantifier $\forall{x}$. But as we will see in Section 5, the claim about ontological innocence is controversial.

A entirely different application of plural logic to set theory seeks to use plurals to explain sets. Kurt Gödel famously wrote of the operation “set of”, which can be applied to any “well-defined objects” to form their set and whose iterated application yields the cumulative hierarchy of sets (1964: 180). A key question is how to understand the notion of some “well-defined objects”. Suppose we accept that any objects $xx$ qualify as such. Then any objects $xx$ give rise to a set $\{xx\}$. Since the cumulative hierarchy contains no universal set, it follows that there cannot be a universal plurality comprising absolutely all objects. Florio and Linnebo 2020 and 2021, ch. 12 develop a *critical* plural logic that is suited for being combined with such an unrestricted “set of” operation. Thus, this approach forsakes the power of this logic to talk about arbitrary collections of sets and instead uses plurals to account for the nature of, and our knowledge of, sets.

### 4.4 Mathematical Nominalism

Some of the most popular applications of the plural quantification are concerned with ontological economy. The idea is to pay the ontological price of a mere first-order theory and then use plural quantification to get for free (a theory with the force of) the corresponding monadic second-order theory. That would obviously be an ontological bargain. Applications of this sort fall into two main classes, which will be discussed in this sub-section and the next.

One class of applications of plural quantification aim to make ontological bargains in the philosophy of mathematics. In particular, a number of philosophers have attempted to use plural quantification as an ingredient of nominalistic interpretations of mathematics. A nice example is Geoffrey Hellman’s modal nominalism, according to which mathematical statements committed to the existence of abstract objects are to be eliminated in favor of statements about the *possible* existence of concrete objects. For instance, instead of claiming, as the platonist does, that there exists an infinite collection of abstract objects satisfying the axioms of Peano arithmetic (namely the natural numbers), Hellman claims that there *could exist* an infinite collection of concrete objects related so as to satisfy these axioms (Hellman 1989 and 1996)[^hellman-1989][^hellman-1996]. However, even this modal claim appears to talk about *collections* of concrete objects and *relations* on these objects. To forestall the objection that this smuggles in through the back door abstract objects such as sets, Hellman needs some alternative, nominalistically acceptable interpretation of this talk about collections and relations. Plural quantification may offer such an interpretation.

For this application of plural quantification to work, PFO must be applicable to all kinds of concrete objects, and it must be ontologically innocent, or at least not committed to any entities that share those features of abstract objects that are found to be nominalistically objectionable. Moreover, in order to simulate quantification over relations, we will need not just PFO but a theory more like monadic *third-order* logic (Sections 2.2 and 2.4).

### 4.5 Eliminating Complex Objects

Another class of applications attempts to eliminate the commitments of science and common sense to (some or all) complex objects. For instance, instead of employing usual singular quantification over tables and chairs, it is proposed that we use plural quantification over mereological atoms arranged tablewise or chairwise (Rosen and Dorr 2002; Hossack 2000; van Inwagen 1990)[^hossack-2000][^rosen-2002][^inwagen-1990]. For instance, instead of saying that there is a chair in one’s office, one should say that there are some atoms in one’s office arranged chairwise. In this way one appears to avoid committing oneself to the existence of a chair. Note that such analyses require PFO+, not just PFO, since the new predicates “are arranged $F$-wise” are non-distributive.

Let’s set aside purely metaphysical worries about such analyses as irrelevant to our present concern. What $we$ would like to know is what demands these analyses put on the theory PFO+, in particular, which strains of the Logicality Thesis are needed. The most obvious demands are that PFO+ be applicable to all kinds of simple objects and that it be ontologically innocent, or at least not committed to complex objects of the sort to be eliminated.

A less obvious demand has to do with the need to analyze ordinary plural quantification over complex objects, for instance

**(16)**

There are some chairs arranged in a circle.

We have already “used up” ordinary plural quantification and predication to eliminate apparent commitment to individual chairs (Uzquiano 2004)[^uzquiano-2004]. So in order to analyze (16), we will need something like “super-plural” quantification — quantification that stands to ordinary plural quantification as ordinary plural quantification stands to singular — and corresponding non-distributive predication. The legitimacy of such linguistic resources was discussed in Section 2.4.

There have also been attempts to use plural logic to eliminate apparent reference to groups. Instead of referring to the Supreme Court, say, perhaps we might get by with referring plurally to its members. An obvious challenge for this approach is that a group can have different members at different moments of time and possible worlds, while the plurality of its (current and actual) members appears to be rigid, temporally as well as modally (Section 2.3). See (Horden and López de Sa 2021)[^horden-2021] for a defense of the proposed elimination against such challenges.

## 5. Ontological Innocence?

The traditional view in analytic philosophy has been that all plural locutions should be paraphrased away, if need be, by quantifying over sets (Section 1). George Boolos and others objected that it is both unnatural and unnecessary to eliminate plural locutions. This led to the theories PFO and PFO+. Proponents of plural quantification claim that these theories allow plural locutions to be formalized in a way that is fundamentally different from the old set-theoretic paraphrases. In particular, they claim that these theories are ontologically innocent in the sense that they introduce no new ontological commitments to sets or any other kind of “set-like” entities over and above the individual objects that compose the pluralities in question. Let’s call this latter claim *Ontological Innocence*.

Other philosophers question Ontological Innocence. For instance, Michael Resnik expresses misgivings about the alleged ontological innocence of the plural formalization (\ref{ex3pprime}) of the Geach-Kaplan sentence (3). For when (\ref{ex3pprime}) is translated into English as instructed, it reads:

**$(3''')$**

There are some critics such that any one of them admires another critic only if the latter is one of them distinct from the former.

But $(3''')$, Resnik says,

> seems to me to refer to collections quite explicitly. How else are we to understand the phrase “one of them” other than as referring to some collection and as saying that the referent of “one” belongs to it? (Resnik 1988: 77)[^resnik-1988]

Related worries have been expressed in Hazen 1993, Linnebo 2003, Parsons 1990, and Rouilhan 2002; see also Shapiro 1993.

I will now discuss three arguments in favor of Ontological Innocence.

### 5.1 The set-theoretic argument

The first argument begins by asking us to consider the claim

**(17)**

There are some sets which are all and only the non-self-membered sets.

and admit that it is true. It continues by arguing that, if plural expressions were committed to collections or any other “set-like” objects, then the truth of (17) would lead straight to Russell’s paradox. This is sometimes thought to be a knock-down argument in favor of Ontological Innocence (Boolos 1984: 440–443 [1998a: 64–67]; Lewis 1991: 65–69; McKay 2006: 31–32)[^boolos-1984][^lewis-1991][^mckay-2006]. But in fact it is less conclusive than it appears. For as we saw in Section 4.3, Russell’s paradox will follow only if two alternative views are ruled out. Since these views cannot be dismissed out of hand, much work remains before this argument can be said to be conclusive.

### 5.2 The incorrect predication argument

The second argument is nicely encapsulated by Boolos’s remark that “It is haywire to think that when you have some Cheerios, you are eating a *set*” (1984: 448–9 [1998a: 72]). What Boolos is suggesting here is that analyses which deny Ontological Innocence are likely to get the subject of plural predications wrong.

The obvious response is to interpret plural predicates in a way which ensures that what we eat are *the elements* of a set and not the set itself. Consider the sentence:

**(18)**

George Boolos ate some Cheerios for breakfast on January 1, 1985.

When the direct object of the verb “ate” is plural, we can for instance interpret the verb by means of the relation *x ate-the-elements-of y*.

It will be objected that this response makes the verb “ate” ambiguous in an implausible way (Oliver and Smiley 2001)[^oliver-2001]. For when the verb has a direct object that is singular, it will presumably be interpreted by means of the ordinary relation *x ate y*. But there is fairly strong evidence that the verb “ate” isn’t ambiguous in this way. For instance, one effect of an ambiguity is to disallow certain kinds of ellipsis. An example is the ambiguity of “make” in “make breakfast” and “make a plan”, which disallows the following ellipsis:

(*19)

Boolos made breakfast, but his guest, only a plan.

So if “ate” was ambiguous in the way just described, the following ellipsis would be disallowed as well, which it isn’t:

**(20)**

Boolos ate some Cheerios, but his guest, only an apple.

However, it is far from clear that the above response to Boolos’s argument needs to be committed to any such problematic ambiguities. We can for instance let *all* predicates take plural entities as their arguments. The verb “ate” will then always receive as its interpretation the relation *the-elements-of x ate-the-elements-of y*, thus removing any ambiguity. Whether or not this response is ultimately acceptable, it shows that the argument in question remains inconclusive.

### 5.3 The direct argument

Perhaps the most popular argument for Ontological Innocence is the one to which I now turn. In its simplest form, this argument is based on our intuitions about ontological commitments. When you assert (18), you don’t have the feeling that you are committing yourself ontologically to a collection or to any other kind of “set-like” object. Nor do you have any such feeling when you assert the Geach-Kaplan sentence or any other translation of a sentence of PFO or PFO+ into English. Or so the argument goes.

In this simple form the argument is vulnerable to the objection that people’s intuitions provide a poor basis for settling theoretical disputes about ontological commitments. We have seen that there are competent speakers of English, such as Michael Resnik, who don’t share these intuitions. Moreover, as Davidson’s popular analysis of action sentences in terms of events makes clear, ordinary people’s intuitions about ontological commitments cannot always be trusted (Davidson 1967)[^davidson-1967]. For instance, someone may sincerely assert that John walked slowly, without being aware that he has committed himself to the existence of an event (namely a walking which was by John and which was slow).

Although this objection has force, the argument can be sharpened by undertaking a more careful study of what forms of existential generalization are warranted on a sentence containing plural expressions (Boolos 1984: 447 [1998a: 70]; McKay 2006: ch. 2; Yi 2002: 7–15 and 2005: 469–472)[^boolos-1984][^mckay-2006]. For instance, we may ask whether the following can be inferred from (18):

**(21)**

There is an object such that Boolos ate all of its elements (or constituents) for breakfast on January 1, 1985.

This inference would no doubt be quite peculiar. This provides evidence that (18) isn’t committed to any kind of “set-like” entity.

However, this evidence is not incontestable. For there are analogous inferences that seem quite natural. For instance, from

**(22)**

Some students surrounded the building.

most speakers of English would be perfectly happy to infer that

**(23)**

A group of students surrounded the building.

So perhaps the peculiarity of the inference from (18) to (21) is a pragmatic rather than a semantic phenomenon. Perhaps it has to do with the fact that it is less natural to regard some Cheerios as a set (or some other sort of plural entity) than it is to regard some students as a group.

However, let’s assume that the defenders of the Direct Argument are right that (18) does not entail (21). What would follow? It would follow that (18) does not incur any additional ontological commitments *of the sort that can be incurred by singular first-order quantifiers*. But this conclusion falls short of the argument’s desired conclusion that (18) does not incur any additional ontological commitments *of any sort*. In order to get from the actual conclusion to the desired one, we would in addition have to assume that all ontological commitments are of the sort incurred by singular first-order quantifiers. But there is an influential philosophical tradition that denies this assumption and instead holds that all kinds of quantifiers incur ontological commitments, not just singular first-order ones.[^note-15] The most famous exponent of this tradition is Frege, who claims that second-order quantifiers are committed to concepts, just as singular first-order quantifiers are committed to objects. This tradition ties the notion of ontological commitment very closely to that of a semantic value. This will be the topic of the next and final subsection.

### 5.4 Semantic values and ontological commitments

In semantics it is widely assumed that each component of a complex expression makes some definite contribution to the meaning of the complex expression. This contribution is known as the *semantic value* of the component expression. It is also assumed that the meaning of the complex expression is functionally determined by the semantic values of the component expressions and their syntactic mode of composition. This assumption is known as *compositionality*.

According to Frege, the semantic value of a sentence is just its truth-value, and the semantic value of a proper name is its referent (that is, the object to which it refers). Once we have fixed the semantic values assigned to sentences and proper names, it is easy to determine what kinds of semantic value to assign to expressions of other syntactic categories. For instance, the semantic value of a monadic predicate will have to be a function from objects to truth-values. Frege calls such functions *concepts*.

As an example, let’s consider the simple subject-predicate sentence

**(24)**

Socrates is mortal.

The logical form of (24) is $\mathbf{M}(\mathbf{s})$, where $\mathbf{M}$ is the predicate “is mortal” and $\mathbf{s}$ is the singular term “Socrates”. Let’s write [$\mathbf{E}$] for the semantic value of an expression $\mathbf{E}$. In accordance with the previous paragraph, the semantic values relevant to (24) are as follows:

**(25)**

$[\mathbf{s}] = \textrm{Socrates}$

**(26)**

$[\mathbf{M}] =$ the function $f$ from objects to truth-values such that $f(x)$ is the true if $x$ is mortal and $f(x)$ is the false otherwise

The truth-value of (24) is thus determined as

**(27)**

[(24)] $= [\mathbf{M}(\mathbf{s})] = [\mathbf{M}] ([\mathbf{s}]) = f(\textrm{Socrates}) =$ the true (if Socrates is mortal) or the false (otherwise).

Frege took the connection between semantic values and ontological commitments to be a very close one. For on the above analysis, (24) supports two kinds of existential generalizations: not just to $\Exists{x}\mstop\mathbf{M}(x)$ (which is true just in case there exists some object which is mortal) but also to $\Exists{F}\mstop F(s)$ (which is true just in case there exists some concept under which Socrates falls). According to Frege, this shows that sentences such as (24) are ontologically committed not just to an object but also to a concept.

What matters for present purposes is not the truth or falsity of Frege’s claim about concepts but whether a cogent argument of this sort can be developed for plural expressions. To investigate this, let’s consider a simple non-distributive plural predication such as

**(28)**

These apples form a circle.

The logical form of (28) appears to be $\mathbf{C}(\mathbf{aa})$, where $\mathbf{C}$ is the predicate “form a circle” and $\mathbf{aa}$ is the plural term “these apples”. (If you think complex plural demonstrative have internal semantic structure, use instead some plural name stipulated to refer directly to the apples in question.) The natural view will then be as follows.

**(29)**

[$\mathbf{aa}] = a_1$ and … and $a_n$ (where the $a_i$ are all and only the apples demonstrated)

**(30)**

[$\mathbf{C}] =$ the function $g$ from pluralities to truth-values such that $g(xx)$ is the true if $xx$ form a circle and $g(xx)$ is the false otherwise

The truth-value of (28) will then be determined as

**(31)**

[(28)] $= [\mathbf{C}(\mathbf{aa})] = [\mathbf{C}] ([\mathbf{aa}]) = g(a_1$ and … and $a_n$) = the true (if $a_1$ and … and $a_n$ form a circle) or the false (otherwise)

which is what one would expect, given the syntactic similarity between (24) and (28).

Assume that this analysis is correct and that each plural term thus has some objects as its semantic value, just as each singular term has one object as its semantic value. What will this mean for the question of Ontological Innocence? According to the Fregean tradition, which connects the notion of ontological commitment to that of a semantic value, this will mean that plural expressions incur commitment to plural entities, much as predicates incur commitment to concepts. For to say that a sentence incurs a commitment to a plural entity is just to say that the truth of the sentence requires there to be some semantic value of the sort appropriate to plural expressions. However, this line of reasoning will be resisted by other philosophers, who believe that the notion of ontological commitment should be tied (at most) to singular first-order variables.

How can this disagreement be adjudicated? On the one hand, it may count in favor of the Fregean tradition that their view is highly systematic. There may be something *ad hoc* about the idea that some sorts of semantic value give rise to ontological commitments while other sorts don’t. On the other hand, it may count in favor of the alternative view that it does better justice to many people’s strongly felt intuition that plural locutions are ontologically innocent.

Another possibility is that the whole controversy is ultimately just a pseudo-disagreement (see especially Florio and Linnebo 2016, but also Parsons 1990; Shapiro 1993; Linnebo 2003; Rayo 2007; and Linnebo and Rayo 2012)[^florio-2016][^linnebo-2003][^linnebo-2016][^linnebo-2012][^parsons-1990][^rayo-2007][^shapiro-1993]. If both parties agree that plural expressions have semantic values, and if both agree that commitments to *objects* are incurred only by singular first-order terms and variables, then perhaps it does not matter whether other sorts of terms and variables should be regarded as introducing their own distinctive kinds of ontological commitment. Some philosophers speak about a theory’s *ideological commitments* and not just about its ontological commitments. By this is meant the logical and conceptual resources that the theory employs. Perhaps philosophers would be well advised to focus more on the metaphysical and epistemological questions raised by a theory’s ideological commitments and worry less about whether these ideological commitments should be also regarded as introducing a distinctive kind of ontological commitment. After all, the notion of an ontological commitment is a theoretical one, not one that has any sharp content outside of philosophy. So perhaps we should regard the notion more as a means to the end of providing good philosophical explanations and less as a goal in itself.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=plural-quant). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/plural-quant/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=plural-quant&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/plural-quant/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- [PhilPapers Bibliography on Plural Quantification](http://philpapers.org/browse/plural-quantification).

[Please contact the author with suggestions.]

## Related Entries

Frege, Gottlob | Frege, Gottlob: theorem and foundations for arithmetic | generalized quantifiers | logic: and ontology | logicism and neologicism | mereology | Russell’s paradox | set theory

### Acknowledgments

Thanks to Salvatore Florio, Allen Hazen, Frode Kjosavik, Tom McKay, David Nicolas, Agustín Rayo, and Gabriel Uzquiano for discussions and written comments on earlier drafts.

## Notes（原文脚注）

[^note-1]: *Second-order* logic has quantifiers that bind variables taking predicate position. These quantifiers are typically understood as ranging over concepts and relations. *Monadic* second-order logic is the subsystem of second-order logic which admits only quantification over concepts, not over (polyadic) relations.

[^note-2]: See Boolos 1984: 432–3 [1998a: 57] for an ingenious proof, which he attributes to David Kaplan. The basic idea is as follows. Assume for simplicity that the domain consists only of critics. Then the sentence can be formalized as

$$\Exists{xx} \Forall{u}\Forall{v}(u\prec xx \amp \textit{Auv} \rightarrow v\prec xx \amp u\ne v).$$

Now reinterpret the predicate *Auv* as the arithmetical predicate $“u = 0 \vee u = v + 1”.$ The resulting sentence

$$ \Exists{xx} \Forall{u}\Forall{v}(u\prec xx \amp(u = 0 \vee u = v + 1) \rightarrow v\prec xx \amp u\ne v) $$

can be seen to be true in all and only non-standard models of arithmetic, by letting $xx$ be all and only the non-standard elements of the model. But it follows from the compactness theorem for first-order logic that any consistent first-order theory of arithmetic has both standard and non-standard models. Hence the original sentence cannot be formalized in a first-order language.

[^note-3]: For further discussion of this and other attempts to analyze plural locutions in non-plural terms, see, e.g., Oliver and Smiley 2001 and Yi 2005.

[^note-4]: Although most contemporary work on plural quantification appears to have been inspired, directly or indirectly, by the work of George Boolos, there is also a substantial pre-Boolosian literature on the topic. Pluralities are closely related to what the early Bertrand Russell called “classes as many,” as opposed to “classes as one”; see Russell 1903, esp. Sections 70, 74, and 104, as well as Klement 2014 for discussion. Simons 1997 argues that Stanislaw Leśniewski in the early twentieth century anticipated many of the ideas later defended by Boolos. More recent pre-Boolosian writings on plurals include Black 1971; Stenius 1974; Morton 1975; Armstrong 1978: 32–34; and Simons 1982. For more references and historical information, see Lewis 1991: 63 and Hazen 1993: 133–34.

[^note-5]: It does not suffice for the predicate $P$ to be distributive that this biconditional is true or even necessarily true. For instance, let $P$ be “has/have a mereological sum”. Then a believer in arbitrary mereological sums takes the relevant biconditional to the true, perhaps even necessarily so, although the predicate $P$ is not distributive. (I owe this example to Gabriel Uzquiano.)

[^note-6]: The phenomenon of non-distributive predication was noted already by Frege, who pondered the sentence “Siemens and Halske have built the first major telegraph network” and suggested that in it,

> “Siemens and Halske” designates a compound object about which a statement is being made, and the word “and” is used to help form the sign for this object. (Frege 1914: 227–8)[^frege-1914]

[^note-7]: Even this extended language will only capture the core features of the plural locutions of English and other natural languages. No systematic analysis of the syntax or semantics of plural locutions in natural language will be attempted here. For more on the complexities of plural locutions in natural languages, the reader is referred to Landman 2000, Link 1998, Lønning 1997, McKay 2006, and Schein 1993 and 2006.

[^note-8]: See Rayo 2002 and McKay 2006 for plural logics that eliminate singular variables in favor of plural ones.

[^note-9]: Although Boolos never formalized the theory PFO, he was clearly aware of this interpretation. See his 1984 and 1985a.

[^note-10]: See Williamson 2003: 456–457, 2010: 699–700, 2013: 245–251, and 2016; Rumfitt 2005: sect. VII; Uzquiano 2011; and Linnebo 2016; see Hewitt 2012a for criticism. See Florio and Linnebo 2021, ch. 10 for a development and formal proofs of relevant arguments involving plurals and modals, and Roberts 2022 for a defense of a definitive modal logic of plurals involving, but going beyond, the principles (10) and (11). These two principles are assumed and put to philosophical use in Bricker 1989: 386–390 and Forbes 1989: 93–102.

[^note-11]: I will, for related reasons, not discuss a proposal due to Taylor and Hazen 1992, according to which English contains ordered lists of referring expressions, as in “London, Paris, and Berlin are the capitals of England, France, and Germany” and associated quantifiers. See Hewitt 2012b for a related proposal.

[^note-12]: For one useful discussion of the question of logicality, see Rayo 2007.

[^note-13]: However, the “non-trivial mathematical truths” alluded to above will then have to be expressed by meta-language quantification over dyadic predicates rather than by object language quantification over dyadic relations. Besides, since (as A.P. Hazen pointed out to me) the monadic second-order theory of the successor operation is decidable, the amount of mathematics that can be obtained in this way is very limited. See Büchi 1962.

[^note-14]: A further problem is that the neo-logicist construction of the natural numbers makes essential use of empty concepts. But it is doubtful that it makes sense to talk about empty pluralities.

[^note-15]: Some philosophers fail to take this tradition into account or find it unnecessary to do so. They thus move directly from the claim that certain locutions incur no controversial ontological commitments of the kind incurred by singular first-order quantifiers to the claim that these locutions incur no controversial ontological commitment whatsoever. For some examples, see Boolos 1984 and 1985a, and Rayo and Yablo 2001.

[^armstrong-1978]: Armstrong, David, 1978, *Universals and Scientific Realism*, Vol. 1, Cambridge: Cambridge University Press.

[^ben-yami-2004]: Ben-Yami, Hanoch, 2004, *Logic and Natural Language: On Plural Reference and Its Semantic and Logical Significance*, Hants: Ashgate.

[^ben-yami-2009]: –––, 2009, “Plural Quantification Logic: A Critical Appraisal”, *Review of Symbolic Logic*, 2(1): 208–232. doi:10.1017/S1755020309090108

[^ben-yami-2013]: –––, 2013, “Higher-Level Plurals Versus Articulated Reference, and an Elaboration of Salva Veritate”, *Dialectica*, 67(1): 81–102. doi:10.1111/1746-8361.12013

[^black-1971]: Black, Max, 1971, “The Elusiveness of Sets”, *Review of Metaphysics*, 24(4): 614–636.

[^boccuni-2013]: Boccuni, Francesca, 2013, “Plural Logicism”, *Erkenntnis*, 78: 1051–1067. doi:10.1007/s10670-013-9482-z

[^boccuni-2023]: –––, 2023, “Arithmetic on the Cheap: Neologicism and the Problem of the Logical Ontology”, *Thought: A Journal of Philosophy*, 12: 55–63. doi:10.5840/tht202512440

[^boolos-1984]: Boolos, George, 1984, “To Be Is To Be a Value of a Variable (or to Be Some Values of Some Variables)”, *Journal of Philosophy*, 81(8): 430–50; repr. in Boolos 1998a. doi:10.2307/2026308

[^boolos-1985a]: –––, 1985a, “Nominalist Platonism”, *Philosophical Review*, 94(3): 327–344; repr. in Boolos 1998a. doi:10.2307/2185003

[^boolos-1985b]: –––, 1985b, “Reading the *Begriffsschrift*”, *Mind*, 94(375): 331–344; repr. in Boolos 1998a. doi:10.1093/mind/XCIV.375.331

[^boolos-1997]: –––, 1997, “Is Hume’s Principle Analytic?” in Richard G. Heck, Jr. (ed.), *Logic, Language, and Thought*, Oxford: Oxford University Press; repr. in Boolos 1998a.

[^boolos-1998a]: –––, 1998a, *Logic, Logic, and Logic*, Richard Jeffrey (ed.), Cambridge, MA: Harvard University Press.

[^boolos-1998b]: –––, 1998b, “Reply to Charles Parsons’ ‘Sets and Classes’”, in Boolos 1998a: pp. 30–36.

[^boolos-2007]: Boolos, George, John P. Burgess, and Richard C. Jeffrey, 2007, *Computability and Logic*, 5th edition, Cambridge: Cambridge University Press.

[^bricker-1989]: Bricker, Phillip, 1989, “Quantified Modal Logic and the Plural *De Re*”, *Midwest Studies in Philosophy*, 14: 372–394. doi:10.1111/j.1475-4975.1989.tb00198.x

[^büchi-1962]: Büchi, J. Richard, 1962, “On a Decision Method in Restricted Second Order Arithmetic”, in E. Nagel, P. Suppes, and A. Tarski (eds.), *Logic, Methodology, and Philosophy of Science*, Stanford, CA: Stanford University Press, pp. 1–11. Reprinted in *The Collected Works of J. Richard Büchi*, 1990, pp. 425–435. doi:10.1007/978-1-4613-8928-6_23

[^burgess-2004]: Burgess, John P., 2004, “*E Pluribus Unum*: Plural Logic and Set Theory”, *Philosophia Mathematica*, 12(3): 193–221. doi:10.1093/philmat/12.3.193

[^burgess-1997]: Burgess, John P. and Gideon Rosen, 1997, *A Subject with No Object: Strategies for Nominalistic Interpretation of Mathematics*, Oxford: Clarendon Press. doi:10.1093/0198250126.001.0001

[^cartwright-2001]: Cartwright, Richard, 2001, “A Question about Sets”, in Alex Byrne, Robert Stalnaker, and Ralph Wedgwood (eds.), *Fact and Value: Essays on Ethics and Metaphysics for Judith Jarvis Thomson*, Cambridge, MA: MIT Press, pp. 29–46.

[^cocchiarella-2002]: Cocchiarella, Nino B., 2002, “On the Logic of Classes as Many”, *Studia Logica*, 70(3): 303–338. doi:10.1023/A:1015190829525

[^davidson-1967]: Davidson, Donald, 1967, “The Logical Form of Action Sentences”, in *The Logic of Decision and Action*, Nicholas Rescher (ed.), pp. 81–95, Pittsburg: University of Pittsburg Press. Reprinted in his *Essays on Actions and Events*, 1980 (subsequent edition, 2001: 105–148), Oxford: Clarendon. doi:10.1093/0199246270.003.0006

[^dummett-1981]: Dummett, Michael, 1981, *Frege: Philosophy of Language*, 2nd edition, Cambridge, MA: Harvard University Press.

[^dummett-1991]: –––, 1991, *Frege: Philosophy of Mathematics*, Cambridge, MA: Harvard University Press.

[^field-1984]: Field, Hartry, 1984, “Is Mathematical Knowledge Just Logical Knowledge?” *Philosophical Review*, 93(4): 509–552. doi:10.2307/2184826

[^field-1993]: –––, 1993, “The Conceptual Contingency of Mathematical Objects”, *Mind*, 102(406): 285–299. doi:10.1093/mind/102.406.285

[^florio-2014a]: Florio, Salvatore, 2014a, “Semantics and the Plural Conception of Reality” *Philosophers’ Imprint*, 14(22): 1–20. [[Florio 2014a available online](http://hdl.handle.net/2027/spo.3521354.0014.022)]

[^florio-2014b]: –––, 2014b, “Untyped Pluralism”, *Mind*, 123(490): 317–337. doi:10.1093/mind/fzu069

[^florio-2016]: Florio, Salvatore and Øystein Linnebo, 2016, “On the Innocence and Determinacy of Plural Quantification”, *Noûs*, 50(3): 565–583. doi:10.1111/nous.12091

[^florio-2020]: –––, 2020, “Critical Plural Logic”, *Philosophia Mathematica*, 28(2): 172–203. doi:10.1093/philmat/nkaa020

[^florio-2021]: –––, 2021, *The Many and the One: A Philosophical Study of Plural Logic*, Oxford: Oxford University Press. [[Florio & Linnebo 2021 available online](https://fdslive.oup.com/www.oup.com/academic/pdf/openaccess/9780198791522.pdf)]

[^florio-2014]: Florio, Salvatore and Stewart Shapiro, 2014, “Set Theory, Type Theory, and Absolute Generality”, *Mind*, 123(489): 157–174. doi:10.1093/mind/fzu039

[^forbes-1989]: Forbes, Graeme, 1989, *The Languages of Possibility*, Oxford: Blackwell.

[^frege-1879]: Frege, Gottlob, 1879, *Begriffsschrift*, translated in Jean van Heijenoort (ed.), 1967, *From Frege to Gödel*, Cambridge, MA: Harvard University Press.

[^frege-1884]: –––, 1884, *Foundations of Arithmetic*, transl. J.L. Austin, Evanston, IL: Northwestern University Press.

[^frege-1914]: –––, 1914, “Logic in Mathematics”, in his *Posthumous Writings*, H. Hermes et al. (eds), 1979, Oxford: Blackwell, pp. 203–250.

[^fujimoto-2025]: Fujimoto, Kentaro, 2025, “Against Plural Comprehension”, *Journal for the Philosophy of Mathematics*, 2: 9–34. doi:10.36253/jpm-3294

[^glanzberg-2004]: Glanzberg, Michael, 2004, “Quantification and Realism”, *Philosophy and Phenomenological Research*, 69(3): 541–572. doi:10.1111/j.1933-1592.2004.tb00518.x

[^gödel-1964]: Gödel, Kurt, 1964, “What Is Cantor’s Continuum Problem?”, in his *Collected Works* (Volume II), 1990, Oxford: Oxford University Press, pp. 176–188.

[^hazen-1993]: Hazen, A.P., 1993, “Against Pluralism”, *Australasian Journal of Philosophy*, 71(2): 132–144. doi:10.1080/00048409312345142

[^hazen-1997]: –––, 1997, “Relations in Lewis’s Framework without Atoms”, *Analysis*, 57(4): 243–248. doi:10.1111/1467-8284.00082

[^hazen-2000]: –––, 2000, “Relations in Lewis’s Framework without Atoms: a Correction”, *Analysis*, 60(4): 351–353. doi:10.1111/1467-8284.00252

[^hellman-1989]: Hellman, Geoffrey, 1989, *Mathematics without Numbers: Towards a Modal-Structural Interpretation*, Oxford: Clarendon Press. doi:10.1093/0198240341.001.0001

[^hellman-1996]: –––, 1996, “Structuralism without Structures”, *Philosophia Mathematica*, 4(2): 100–123. doi:10.1093/philmat/4.2.100

[^hewitt-2012a]: Hewitt, Simon Thomas, 2012a, “Modalising Plurals”, *Journal of Philosophical Logic*, 41(5): 853–875. doi:10.1007/s10992-011-9194-2

[^hewitt-2012b]: –––, 2012b, “The Logic of Finite Order”, *Notre Dame Journal of Formal Logic*, 53(3): 297–318. doi:10.1215/00294527-1716820

[^higginbotham-1998]: Higginbotham, James, 1998, “On Higher-Order Logic and Natural Language”, *Proceedings of the British Academy*, 95: 1–27. [[Higginbotham 1998 available online](http://www.britac.ac.uk/pubs/proc/volumes/pba95.html)]

[^horden-2021]: Horden, John and Dan López de Sa, 2021, “Groups as Pluralities”, *Synthese*, 198: 10237–10271. doi:10.1007/s11229-020-02715-y

[^hossack-2000]: Hossack, Keith, 2000, “Plurals and Complexes”, *British Journal for Philosophy of Science*, 51(3): 411–443. doi:10.1093/bjps/51.3.411

[^hossack-2014]: –––, 2014, “Sets and Plural Comprehension”, *Journal of Philosophical Logic*, 43(2–3): 517–539. doi:10.1007/s10992-013-9278-2

[^klement-2014]: Klement, Kevin C., 2014, “Early Russell on Types and Plurals”, *Journal For The History of Analytical Philosophy*, 2(6): 1–21. doi:10.15173/jhap.v2i6.47

[^landman-2000]: Landman, Fred, 2000, *Events and Plurality*, Dordrecht: Kluwer.

[^lewis-1991]: Lewis, David, 1991, *Parts of Classes*, Oxford: Blackwell.

[^link-1998]: Link, Godehard, 1998, *Algebraic Semantics in Language and Philosophy*, Stanford, CA: CSLI Publications.

[^linnebo-2003]: Linnebo, Øystein, 2003, “Plural Quantification Exposed”, *Noûs*, 37(1): 71–92. doi:10.1111/1468-0068.00429

[^linnebo-2016]: –––, 2016, “Plurals and Modals”, *Canadian Journal of Philosophy*, 46(4–5): 654–676. doi:10.1080/00455091.2015.1132975

[^linnebo-2008]: Linnebo, Øystein and David Nicolas, 2008, “Superplurals in English”, *Analysis*, 68(3): 186–197. doi:10.1111/j.1467-8284.2008.00737.x

[^linnebo-2012]: Linnebo, Øystein and Agustín Rayo, 2012, “Hierarchies Ontological and Ideological”, *Mind*, 121(482): 269–308. doi:10.1093/mind/fzs050

[^lønning-1997]: Lønning, Jan Tore, 1997, “Plurals and Collectivity”, in J. van Bentham and A. ter Meulen (eds.), *Handbook of Logic and Language*, Amsterdam: Elsevier, pp. 1009–1054.

[^mckay-2006]: McKay, Thomas, 2006, *Plural Predication*, Oxford: Oxford University Press. doi:10.1093/acprof:oso/9780199278145.001.0001

[^morton-1975]: Morton, Adam, 1975, “Complex Individuals and Multigrade Relations”, *Noûs*, 9(3): 309–318. doi:10.2307/2214634

[^nicolas-2008]: Nicolas, David, 2008, “Mass Nouns and Plural Logic”, *Linguistics and Philosophy*, 31(2): 211–244. doi:10.1007/s10988-008-9033-2

[^oliver-2001]: Oliver, Alex and Timothy Smiley, 2001, “Strategies for a Logic of Plurals”, *Philosophical Quarterly*, 51(204): 289–306. doi:10.1111/j.0031-8094.2001.00231.x

[^oliver-2004]: –––, 2004, “Multigrade Predicates”, *Mind*, 113(452): 609–681. doi:10.1093/mind/113.452.609

[^oliver-2005]: –––, 2005, “Plural Descriptions and Many-Valued Functions”, *Mind*, 114(456): 1039–1068. doi:10.1093/mind/fzi1039

[^oliver-2016]: –––, 2016, *Plural Logic*, second edition, revised and enlarged, Oxford: Oxford University Press.

[^parsons-1977]: Parsons, Charles, 1977, “What Is the Iterative Conception of Set?”, in *Logic, Foundations of Mathematics, and Computability Theory*, Robert E. Butts and Jaakko Hintikka (eds), Dordrecht/Boston: D. Reidel, pp. 335–367. Reprinted in Paul Benacerraf and Hilary Putnam (eds.), *Philosophy of Mathematics: Selected Readings*, 2nd edition, 1983, Cambridge: Cambridge University Press, pp. 503–529. doi:10.1007/978-94-010-1138-9_18 and doi:10.1017/CBO9781139171519.027

[^parsons-1990]: –––, 1990, “The Structuralist View of Mathematical Objects”, *Synthese*, 84(3): 303–346. doi:10.1007/BF00485186

[^payton-2025]: Payton, Jonathan, D., 2025, “From Singular to Plural … and beyond?”, *Philosophy and Phenomenological Research*, 110: 983–1012. doi:10.1111/phpr.13136

[^quine-1973]: Quine, W.V., 1973, *Roots of Reference*, La Salle, IL: Open Court.

[^quine-1982]: –––, 1982, *Methods of Logic*, 4th edition, Cambridge, MA: Harvard University Press

[^quine-1986]: –––, 1986, *Philosophy of Logic*, 2nd edition, Cambridge, MA: Harvard University Press

[^rayo-2002]: Rayo, Agustín, 2002, “Word and Objects”, *Noûs*, 36(3): 436–464. doi:10.1111/1468-0068.00379

[^rayo-2006]: –––, 2006, “Beyond Plurals”, in Rayo and Uzquiano 2006: 220–254.

[^rayo-2007]: –––, 2007, “Plurals”, *Philosophy Compass*, 2(3): 411–427. doi:10.1111/j.1747-9991.2007.00060.x

[^rayo-1999]: Rayo, Agustín and Gabriel Uzquiano, 1999, “Toward a Theory of Second-Order Consequence”, *Notre Dame Journal of Formal Logic*, 40(3): 315–325. doi:10.1305/ndjfl/1022615612

[^rayo-2006-2]: –––, 2006 (eds.), *Absolute Generality*, Oxford: Oxford University Press.

[^rayo-2001]: Rayo, Agustín and Stephen Yablo, 2001, “Nominalism through De-Nominalization”, *Noûs*, 35(1): 74–92. doi:10.1111/0029-4624.00288

[^resnik-1988]: Resnik, Michael, 1988, “Second-Order Logic Still Wild”, *Journal of Philosophy*, 85(2): 75–87. doi:10.2307/2026993

[^roberts-2022]: Roberts, Sam, 2022, “Pluralities as Nothing Over and Above”, *Journal of Philosophy*, 119(8): 405–424.

[^rosen-2002]: Rosen, Gideon and Cian Dorr, 2002, “Composition as Fiction”, in Richard M. Gale (ed.), *The Blackwell Guide to Metaphysics*, Oxford: Blackwell, pp. 151–174. doi:10.1002/9780470998984.ch8

[^rouilhan-2002]: Rouilhan, Philippe de, 2002, “On What There Are”, *Proceedings of the Aristotelian Society*, 102(1): 183–200. doi:10.1111/j.0066-7372.2003.00049.x

[^rumfitt-2005]: Rumfitt, Ian, 2005, “Plural Terms: Another Variety of Reference?” in José Luis Bermudez (ed.), *Thought, Reference and Experience: Themes from the Philosophy of Gareth Evans*, Oxford: Oxford University Press, pp. 84–123. doi:10.1093/acprof:oso/9780199248964.003.0004

[^rumfitt-2018]: –––, 2018, “Neo-Fregeanism and the Burali-Forti Paradox”, in Ivette Fred-Rivera and Jessica Leech (eds.), *Being Necessary: Themes of Ontology and Modality from the Work of Bob Hale*, Oxford: Oxford University Press, pp. 188–223. doi:10.1093/oso/9780198792161.003.0010

[^russell-1903]: Russell, Bertrand, 1903, *Principles of Mathematics*, Cambridge: Cambridge University Press.

[^schein-1993]: Schein, Barry, 1993, *Plurals and Events*, Cambridge, MA: MIT Press.

[^schein-2006]: –––, 2006, “Plurals”, in Ernest Lepore and Barry C. Smith (eds.), *Oxford Handbook of Philosophy of Language*, Oxford: Oxford University Press, pp. 716–767. doi:10.1093/oxfordhb/9780199552238.003.0029

[^shapiro-1991]: Shapiro, Stewart, 1991, *Foundations without Foundationalism: A Case for Second-Order Logic*, Oxford: Clarendon. doi:10.1093/0198250290.001.0001

[^shapiro-1993]: –––, 1993, “Modality and Ontology”, *Mind*, 102(407): 455–481. doi:10.1093/mind/102.407.455

[^simons-1982]: Simons, Peter, 1982, “Plural Reference and Set Theory”, in Barry Smith (ed.), *Parts and Moments: Studies in Logic and Formal Ontology*, Munich: Philosophia Verlag, pp. 199–260. [[Simons 1982 available online](http://ontology.buffalo.edu/smith/book/P&M/)]

[^simons-1997]: –––, 1997, “Higher-Order Quantification and Ontological Commitment”, *Dialectica*, 51(4): 255–271. doi:10.1111/j.1746-8361.1997.tb00032.x

[^simons-2016]: –––, 2016, “The Ontology and Logic of Higher-Order Multitudes”, in Massimiliano Carrara, Alexandra Arapinis, and Friederike Moltmann (eds), *Unity and Plurality: Logic, Philosophy, and Linguistics*, Oxford: Oxford University Press, pp. 55–69. doi:10.1093/acprof:oso/9780198716327.003.0004

[^spencer-2012]: Spencer, Joshua, 2012, “All Things Must Pass Away”, *Oxford Studies in Metaphysics*, 7: 67–92.

[^stenius-1974]: Stenius, Eric, 1974, “Sets”, *Synthese*, 27(1–2): 161–188. doi:10.1007/BF00660894

[^tarski-1986]: Tarski, Alfred (and John Corcoran, trans.), 1986, “What Are Logical Notions?”, *History and Philosophy of Logic*, 7(2): 143–154. doi:10.1080/01445348608837096

[^taylor-1992]: Taylor, Barry and A.P. Hazen, 1992, “Flexibly Structured Predication”, *Logique et Analyse*, 35(139–140): 375–393.

[^uzquiano-2003]: Uzquiano, Gabriel, 2003, “Plural Quantification and Classes”, *Philosophia Mathematica*, 11(1): 67–81. doi:10.1093/philmat/11.1.67

[^uzquiano-2004]: –––, 2004, “Plurals and Simples”, *Monist*, 87(3): 429–451. doi:10.5840/monist200487324

[^uzquiano-2011]: –––, 2011, “Plural Quantification and Modality”, *Proceedings of the Aristotelian Society*, 111(2_pt_2): 219–250. doi:10.1111/j.1467-9264.2011.00307.x

[^inwagen-1990]: van Inwagen, Peter, 1990, *Material Beings*, Ithaca, NY: Cornell University Press.

[^williamson-2003]: Williamson, Timothy, 2003, “Everything”, *Philosophical Perspectives*, 17: 415–465. doi:10.1111/j.1520-8583.2003.00017.x

[^williamson-2010]: –––, 2010, “Necessitism, Contingentism, and Plural Quantification”, *Mind*, 119(475): 657–748. doi:10.1093/mind/fzq042

[^williamson-2013]: –––, 2013, *Modal Logic as Metaphysics*, Oxford: Oxford University Press.

[^williamson-2016]: –––, 2016, “Reply to Linnebo”, *Canadian Journal of Philosophy*, 46(4–5): 677–682. doi:10.1080/00455091.2016.1205856

[^yablo-2006]: Yablo, Stephen, 2006, “Circularity and Paradox”, in Thomas Bolander, et al. (eds.), *Self-Reference*, Stanford: CSLI Publications, pp. 139–154.

[^yablo-2000]: –––, 2000, “Apriority and Existence”, in Paul Boghossian and Christopher Peacocke (eds.), *New Essays on the A Priori*, Oxford: Oxford University Press, pp. 197–228. doi:10.1093/0199241279.003.0009

[^yi-1999]: Yi, Byeong-Uk, 1999, “Is Two a Property?” *Journal of Philosophy*, 96(4): 163–190. doi:10.2307/2564701

[^yi-2002]: –––, 2002, *Understanding the Many*, New York, NY: Routledge.

[^yi-2005]: –––, 2005, “The Logic and Meaning of Plurals, Part I”, *Journal of Philosophical Logic*, 34(5): 459–506. doi:10.1007/s10992-005-0560-9

[^yi-2006]: –––, 2006, “The Logic and Meaning of Plurals, Part II”, *Journal of Philosophical Logic*, 35(3): 239–288. doi:10.1007/s10992-005-9015-6
