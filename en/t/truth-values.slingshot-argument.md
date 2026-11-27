# truth-values — slingshot-argument（supplement）

> （《truth-values》词条补充材料，源：plato.stanford.edu/entries/truth-values/slingshot-argument.html）

#### Supplement to Truth Values

## The Slingshot Argument

The argument known as the “slingshot” was specially designed to provide a formally strict proof of the claim that all true sentences designate (denote, refer to) one and the same thing. Moreover, according to the argument, all false sentences designate the same thing as well. These things are precisely the truth values: *the True* and *the False*. The argument is already anticipated (implicitly at least) by Frege (see, e.g., Frege 1892: 49), and was first formulated explicitly by Alonzo Church (1943) in his review of Carnap’s *Introduction to Semantics*. Church took the result to show that sentences cannot designate propositions—contrary to what Carnap had claimed in his book.

“The slingshot argument” is a kind of an umbrella term covering a broad family of arguments rather than a single line of reasoning. However, in all its forms the argument essentially rests on the assumption that every sentence has a designation. Another important assumption is the principle of *Substitutivity* for co-referential terms:

> If a sentence is converted into another sentence by substituting any term for a term with exactly the same designation, the resulting and the initial sentences also designate the same.

Church formulates this principle as a demand of “interchangeability of synonymous expressions”. This is actually just an instance of the compositionality principle, according to which the meaning of a complex expression (when identified with its designation) is uniquely determined by the structure of this expression and the meanings (designations) of its components.

The next assumption, explicitly made by Church in 1943, is the synonymity of logically equivalent sentences:

**(A0)**

If sentences $A$ and $B$ are *logically equivalent*, then they have the same designation.

Church makes use of an abstraction operator $\lambda x$ for constructing *lambda-terms* of the form $\lambda x X$ understood as “the class of all $x$ such that $X$” (1943: 299), and considers the following three sentences (where $A$ is true):

$$ \begin{align} A \tag{Ch1}\\ \lambda x (x = x \wedge {\sim}A) &= \lambda x (x \neq x) \tag{Ch2}\\ \lambda x (x \neq x) &= \lambda x (x \neq x)\tag{Ch3} \end{align} $$

Clearly, Ch2 is true, because ${\sim}A$ is false, and hence, $\lambda x (x = x \wedge {\sim}A)$ and $\lambda x (x \neq x)$ denote then one and the same object, namely the empty class. Moreover, Ch1 and Ch2 cannot differ in their truth-value, and thus, are logically equivalent. Indeed, if Ch1 is true, Ch2 must also be true as stated above. If Ch1 is false, then ${\sim}A$ is true, hence $\lambda x (x = x \wedge {\sim}A)$ does not designate the empty class, and thus Ch2 must be false. By (A0), Ch1 and Ch2 must have one and the same designation. By substitutivity, the designation of Ch2 and Ch3 is also the same. Thus, Ch1 and Ch3 must designate the same thing if any. $A$ is arbitrary, and hence, we can restate Ch1–Ch3 by taking any other true sentence $B$ instead of $A$. Since the designation of $A$ is the same as the one of Ch3, it is also the designation of $B$. As the result we get that any two true sentences $A$ and $B$ must designate one and the same thing (“be synonymous”). This means in particular that $A$ and $B$ cannot designate propositions, since the propositions corresponding to $A$ and $B$ are certainly not the same in general.

> By a similar method any two false sentences can be shown to be synonymous. Therefore finally no possibility remains for the designata of sentences except that they be truth-values. (Church 1943: 300)

It seems that Carnap found this argument convincing enough: in his next book (1947: 26) he *did* postulate truth values as “extensions” of sentences and, moreover, provided independent reasons for this. It should be noted, however, that the evidential value of the argument depends heavily on the acceptance of its assumptions—Substitutivity and (A0) in this version. Both these assumptions have been frequently criticized by different authors. In particular, Barwise and Perry (1981) reject them on the basis of their situation semantics. For a critical discussion of these principles, see also (Bennett 1988, Neale 2001, Searle 1995, and Taylor 1985).

A rather informal and pedagogically more comprehensible textbook-version of the argument from (Church 1956: 24–25)—presented by items C1–C4 in the main body of this entry—does not use assumption (A0). Yet, it relies on another principle called *redistribution*: “Rearrangement of the parts of a sentence does not effect what it designates, as long as the truth conditions remain the same” (Perry 1996: 100). This principle may seem controversial. Moreover, Barwise and Perry (1981: 396–397) argue that it is incompatible with Substitutivity, and thus, taking them together appears to be problematic.

Note that the sequence C1–C4, as well as the sequence Ch1–Ch3 above, does not constitute a logical inference in a strong sense. It is rather a number of conversion steps each producing co-referential sentences. However, the argument can be re-articulated as a formal derivation by applying suitable technical machinery.

An appropriate opportunity for such a strict deductive formalization is given with a version of the argument sketched by Gödel in (1944: 128–129), where he highlights the impact of various theories of descriptions on the problem of what sentences designate. According to Gödel, if—in addition to substitutivity—we take the apparently obvious view that a descriptive phrase denotes the object described, then the conclusion that “all true sentences have the same signification (as well as all false ones)” is almost inevitable. Gödel hints at a “rigorous proof” of this claim by making use of some further assumptions. Let $(\iota x)(x=a \wedge Fx)$ stand for the definite description “the $x$ such that $x$ is identical to $a$ and $x$ is $F$”, and let for any sentence $A$, $[ A ]$ stand for what $A$ designates. Then Gödel’s assumptions can be articulated as follows:

**(A1)**

$[Fa] = [a=(\iota x)(x=a \wedge Fx)]$.

**(A2)**

Every sentence can be transformed into an equivalent sentence of the form $Fa$. (This assumption allows Gödel to expand his argument beyond the atomic sentences, cf. Neale 1995: 778.)

(A1) is called the “Gödelian equivalence” by Neale (2001: 166) and is meant to be a weaker replacement for (A0). (A2) simply says that any sentence can be put into a predicate-argument form. This could be illustrated by a transformation of sentences like “Socrates snored and Plato snored” into “Socrates is an $x$ such that $x$ snored and Plato snored ” (see Neale 2001: 130).

One can reconstruct Gödel’s proof in the form of an “official” logical inference. (The reconstruction below stems essentially from Neale (1995: 777—779, 789), although the exact formulation is somewhat different). Making use of the introduced notation, it is possible to prove that for any true sentences $A$ and $B$, $[A] = [B]$. For this an additional rule of inference governing the description operator will be needed:

$$ \iota\dd\textsc{INTR}: \frac{A(x/a)}{a=(\iota x)(x=a \land A(x))} $$

where $a$ is a singular term, $A (x)$ is a sentence containing at least one free occurrence of the variable $x$, and $A(x/a)$ is the result of replacing every occurrence of $x$ in $A(x)$ by $a$.

Note the close connection between this rule and (A1). As Neale (1995: 789) observes, *ι*-intr (as well as its counterpart rule *ι*-elim, which goes in the opposite direction) must be a valid rule of inference in any (extensional) theory of descriptions (as it is in Russell’s).

Another inference rule, which allows substitution for definite descriptions, is also taken from Neale (1995: 787):

$$ \begin{array}{cccc} \iota\dd\textsc{SUB} & (\iota x)\phi = (\iota x) \psi & (\iota x)\phi = a & (\iota x)\phi = a \\ &\frac{A((\iota x)\phi)}{A((\iota x)\psi)} & \frac{A((\iota x)\phi)}{A(a)} & \frac{A(a)}{A((\iota x)\phi)} \end{array} $$

where in an expression of the form $\frac{A(y)}{A(z)}$ $A(z)$ is the result of replacing at least one occurrence of $y$ in $A(y)$ by $z$.

With this machinery at hand, suppose the sentences G1–G3 below are true.

$$ \begin{gather} Fa \tag{G1}\\ a \ne b \tag{G2}\\ Gb \tag{G3}\\ \end{gather} $$

Then one can proceed as follows:

$$ \begin{align} a&=(\iota x)(x=a \wedge Fx) \quad\quad \textrm{G1}, \iota\dd\textsc{INTR}\tag{G4}\\ a&=(\iota x)(x=a \wedge x \ne b) \quad\quad\textrm{G2}, \iota\dd\textsc{INTR}\tag{G5}\\ b& =(\iota x)(x=b \wedge Gx) \quad\quad\textrm{G3}, \iota\dd\textsc{INTR}\tag{G6}\\ b&=(\iota x)(x=b \wedge a \ne x) \quad\quad\textrm{G2}, \iota\dd\textsc{INTR}\tag{G7}\\ (\iota x)(x=a \wedge Fx)& =(\iota x)(x=a \wedge x \ne b) \quad\quad\textrm{G4, G5}, \iota\dd\textsc{SUB}\tag{G8}\\ (\iota x)(x=b \wedge Gx)& =(\iota x)(x=b \wedge a \ne x) \quad\quad\textrm{G6, G7}, \iota\dd\textsc{SUB}\tag{G9}\\ [Fa] & = [a=(\iota x)(x=a \wedge Fx)] \quad\quad\textrm{(A1)}\tag{G10}\\ [a \ne b] & = [a=(\iota x)(x=a \wedge x \ne b)] \quad\quad\textrm{(A1)}\tag{G11}\\ [Fa] & = [a=(\iota x)(x=a \wedge x \ne b)] \quad\quad\textrm{G8, G10}, \iota\dd\textsc{SUB}\tag{G12}\\ [Fa] & = [a \ne b] \quad\quad \text{G11, G12}, \textit{Transitivity of} =\tag{G13}\\ [Gb] & = [b=(\iota x)(x=b \wedge Gx)] \quad\quad\textrm{(A1)}\tag{G14}\\ [a \ne b] & = [b=(\iota x)(x=b \wedge a \ne x)] \quad\quad\textrm{(A1)}\tag{G15}\\ [Gb] & = [b=(\iota x)(x=b \wedge x \ne a)] \quad\quad\textrm{G9, G14}, \iota\dd\textsc{SUB}\tag{G16}\\ [Gb] & = [a \ne b] \quad\quad\textrm{G15, G16}, \textit{Transitivity of} =\tag{G17}\\ [Fa] & = [Gb] \quad\quad\textrm{G13, G17}, \textit{Transitivity of} =\tag{G18}\\ \end{align} $$

The inference can be easily repeated if instead of G2 we take its non-negated form $a=b$. That is, in any case (in view of the assumption that sentences do designate) $Fa$ and $Gb$ must have one and the same designation. But $Fa$ and $Gb$ may be completely different sentences having nothing (of semantic relevance) in common, except that they are both true, as had been assumed, such as “Socrates is wise” and “Mount Everest is high”. Then, taking into account the assumption (A2), one can easily extend this claim to any true sentences $A$ and $B$.

The paper where Gödel put forward his argument was published in a volume from the “Library of Living Philosophers” devoted to Bertrand Russell. As is well known, Russell considered facts to be *meanings* of true sentences, so that, e.g., “Socrates is mortal” means a certain fact, see Russell (1992 [1918,1919]: 186). In this case the argument above would demonstrate that all true sentences mean one and the same fact, reducing thus Russell’s view to an absurdity.

Therefore, the slingshot argument sometimes has been characterized as a “collapsing argument”, for what it admittedly shows is that there are fewer entities of a given kind than one might suppose (Neale 1995: 761). In this sense the argument can be equally used to show that sentences do not designate situations, states of affairs or anything of the sort, leading any attempt to assume so to a breakdown of the class of supposed designata “into a class of just two entities (which might as well be called ‘Truth’ and ‘Falsity’)” (Neale 1995: 761). Another famous argument of this kind is due to W.V. Quine (see 1953, 1960), who intended to demonstrate that quantifying into modal contexts leads to a collapse of modality.

As Gödel in contrast to Church offers only a rough outline of his argument, one can find in the literature several different supposedly authentic reconstructions of Gödel’s proof, and it is not easy to see which one of them reproduces Gödel’s line of reasoning more accurately than the others. However, such reconstructions, being different in the assumptions involved or in their technical implementation, all end up with the same conclusion. It should be understood, that questioning these assumptions, and more concretely, the supposed applicability of the rules *ι*-intr and *ι*-sub in a particular context can undermine the certainty of this conclusion. For a critical discussion of these rules in connection with Gödel’s slingshot (see Neale 2001, Oppy 1997, and Stoutland 2003).

An explicit feature of Gödel’s slingshot, besides replacing (A0) with the less controversial (A1), is the use of an arbitrary object $a$ (rather than a class abstract or definite description), and considering it to be the object which has some property and is identical to $a$. Interestingly, if one returns to the stronger assumption (A0) maintained by Church and considers equivalent transformations of Gödelian expressions like $a=(\iota x)(x=a \wedge Fx)$, then one obtains another, very simple (even simplified) version of the slingshot which—though not exactly Gödelian—is clearly inspired by Gödel’s ideas. Moreover, this version (see, e.g., MacFarlane 2002) is to some degree intermediate between Gödel’s original argument and the ones developed by Church and Davidson.

Namely, let $R$ and $T$ be any true sentences and $a$ be some term which has a designation. Then we have the following four sentences which all have the same designation:

$$ \begin{gather} R\tag{S1}\\ a=(\iota x)(x=a \wedge R) \tag{S2}\\ a=(\iota x)(x=a \wedge T) \tag{S3}\\ T\tag{S4} \end{gather} $$

Indeed, S1 and S2 are logically equivalent. As Stoutland (2003: 15–16) observes, since $(\iota x)(x=a \wedge R)$ has as its reference the unique object $x$ such that $x = a$ and $R$, then

> if $R$ is true, this will simply be the unique object such that $x = a$; but if $R$ is false, there will be no such thing as the unique object such that $x = a$ and $R$. (notation adjusted)

The same holds for S3 and S4. Now, because $(\iota x)(x=a \wedge R)$ and $(\iota x)(x=a \wedge T)$ designate one and the same object, namely $a$, by substitutivity, S2 and S3 also designate the same object. Hence, S1 and S4 must have the same designation as well. And there is nothing left but taking it to be their truth value.

Davidson used his own version of the “slingshot” (see the supplementary document to the entry “Facts”) to undermine a widespread view that true sentences correspond to facts. The line of reasoning in accordance with the slingshot schema forces us to admit then that all true sentences refer to one and the same fact, which Davidson (1969), nimbly enough, calls *The Great Fact*. This conclusion is often employed to make a case against the correspondence theory of truth. The idea is that facts—when related to a sentence—appear to be non-localizable, and thus any true sentence seems to correspond to the whole universe rather than to some of its “parts”. As it was suggested by C.I. Lewis (1943: 242), a proposition refers then not to some limited state of affairs, but to the “kind of *total* state of affairs we call a world”. And further:

> All *true* propositions have the same extension, namely, this actual world; and all *false* propositions have the same extension, namely, zero-extension.

Such an understanding is especially congenial to the Fregean account of truth values.

The slingshot argument has received an extensive and comprehensive treatment in the literature, see, e.g., the thorough monograph by Neale (2001) and also the relevant discussion in the entries on the identity theory of truth, Alonzo Church, facts. A recent approach to the analysis of this argument is presented in the work of Nuel Belnap (forthcoming), where he draws attention to the fact that all standard versions of the slingshot argument rely on what Carnap (1947) calls “the method of the name relation”. In contrast, Belnap proposes “to see what the slingshot comes to if, instead of the name relation, one depends on ‘the method of extension and intension’”, which Carnap develops in the same book. In doing so, Belnap employs a particular version of the latter method called “case-intensional semantics”, which is due to Bressan (1972). The key idea of this semantics is that by evaluating linguistic expressions it assumes an additional structural parameter of *cases*, thus abandoning such thing as *the* extension of expression $E$ in favour of the more fundamental semantic locution “the extension of expression $E$ in case *γ*. The intension of a linguistic expression is then understood as “the pattern of extensions-in-*γ* as *γ* varies over the set of all cases”.

Belnap further observes that a statement about the meaning-identity of situations (or facts) is of a modal character, and thus, introducing this modality in a context is legitimate if and only if this context has the same extension *in all cases*. More concretely, Belnap argues that the expressions ‘Newton’s apple is Newton’s apple’ and ‘Newton’s apple struck Newton’s head’ can have the same extension (namely, truth) in one case (when Newton’s apple does struck Newton’s head), and different extensions (truth and falsity) in another case (when Newton’s apple does not struck Newton’s head). Consequently, the statement about the coextensiveness of the expressions has itself different extensions in the two cases, which precludes the conclusion that these expressions denote the same situation (or fact). In other words, Belnap’s analysis shows that even if the claim that two sentences are coextensive happens to be true in some cases, the conclusion that these sentences denote the same situation will be wrong if there is at least one case in which such coextensiveness fails. Thus, Belnap argues, the correct interchangeability of names must presuppose not only the identity of their extensions, but the identity of intensions as well.

We conclude with the following observation by Frederick Stoutland (2003: 4):

> Although the slingshot can be made rigorously valid, its conclusion can be evaded by challenging one or more of its assumptions, not all of which are by any means self-evident. At the same time, reflection on these assumptions sheds a great deal of light on philosophical questions, and anyone who thinks about issues like truth ought to know what is at stake in accepting or rejecting the argument and the assumptions it requires.
