# logic-many-sorted — early-history（supplement）

> （《logic-many-sorted》词条补充材料，源：plato.stanford.edu/entries/logic-many-sorted/early-history.html）

#### Supplement to Many-Sorted Logic

## Early History of Many-Sorted Logic

- A. Hao Wang
- B. Solomon Feferman

### A. Hao Wang

One of the pioneering articles on many-sorted logic was published in 1952 by Hao Wang. In it, the author indicates that the term “many-sorted” was introduced in Langford’s 1939 review of Schmidt (1938) as a translation of the German word “*mehrsortig*” (Wang thanks Professor Alonzo Church (1952, 105 fn.1) for first calling his attention to Schmidt’s work). In Church (1956), the *many-sorted functional calculus* appears only in the last chapter as a proposed exercise (number 55.24).[^note-34]

In Wang (1952) a many-sorted language is introduced as well as an axiomatic calculus for this logic, a translation into one-sorted logic is defined and several metatheorems relating them are proven. The translation defined is the usual one. Hao Wang declares that the main purpose of his paper is to investigate the relations between any many-sorted theory $T_{n}$ (or the many-sorted logic $L_{n}$) and its corresponding one-sorted theories and logic ($T_{1}^{(n)}$ and $L_{1}^{(n)}$).[^note-35] He remarks:

> By a comparative study of $L_{n}$ and $L_{1}$, we shall also indicate that many known metamathematical results about a usual elementary logic $L_{1}$ have counterparts for $L_{n}$. (Wang 1952: 107)

His system is based on Quine (1940) and hence he uses *ε* as Quine does, in a way similar to the meaning of “is” in English, different from the notion introduced by Russell.[^note-36] Due to this use of connective “*ε*”, which is taken as primitive, Wang says:

> We may either take as primitive or define a predicate denoting the identity relation in $T_{n}$. In any case, it is usually desirable to include in $T_{n}$ the usual theory of identity for the objects of the system. We shall assume that $T_{n}$ contains the usual theory of identity as a part. Then we know that we can introduce descriptions by contextual definitions
>
> […]
>
> But we also know that once we have descriptions at hand, we can make use of additional predicates to get rid of the primitive names and functors. (Wang 1952: 105)

Therefore, his formal language has only predicates as non-logical symbols. His system includes variables of several sorts, as well as “the usual theory of identity”, including “the law of reflexivity and the principle of substitutivity for the variables of the system”. Apart from this theory, the calculus includes:

**Axiomatic calculus:** Wang 1952 uses $\vdash \varphi$ to mean that the closures of *φ* are theorems. As axioms for his system he proposes:

**$1_{n}.$**

If *φ* is a truth-functional tautology, then $\vdash \varphi$.

**$2_{n}.$**

$\vdash \forall x^{i}(\varphi \rightarrow \psi )\rightarrow (\forall x^{i}\varphi \rightarrow \forall x^{i}\psi )$.

**$3_{n}.$**

If $x^{i}$ is not free in *φ*, then $\vdash \varphi \rightarrow \forall x^{i}\varphi$

**$4_{n}.$**

If $x^{i}$ and $y^{i}$ are variables of the same kind, and $\varphi^{\prime}$ is like *φ* except for containing free occurrences of $y^{i}$ whenever *φ* contains free occurrences of $x^{i}$, then $\vdash \forall x^{i}\varphi \rightarrow \varphi^{\prime}$

**$5_{n}.$**

If $\varphi \rightarrow \psi$ and *φ* are theorems of $L_{n}$ so is *ψ*.

By adding certain proper axioms (or also axiom schemata) to $L_{n}$, we obtain a theory $T_{n}$.

Wang (1952: 106) also suggests using the standard translation into one-sorted logic:

> As an alternative way, we may also formulate a system involving several categories of fundamental objects by using merely one kind of variables which have the sum of all the categories as their range of values.

To do this, a unary predicate $S_{i}$ should be added for each sort $i$ and the calculus has to be modified to include:

**$6_{1}.$**

For every $i$ ($i=1,\ldots,n$), $\exists x^{i}S_{i}x^{i}$ is a theorem.

Furthermore, Section 2 of Wang (1952), entitled *The many-sorted elementary logics $L_{n}$*, is devoted to present the semantics as well as to prove soundness and weak completeness for the axiomatic calculus introduced in his Section 1.

Hao Wang also quotes Herbrand’s 1930 dissertation, *Recherches sur la théorie de la démonstration*, where the equivalence between provability of a statement in $T_{n}$ and its translation in $T_{1}^{(n)}$ is established as well as the implication between the consistency of $T_{n}$ and that of $T_{1}^{(n)}$. He also refers (see Wang 1952: 111–14) to an effective way of finding proofs in $T_{1}^{(n)}$ of translated statements using proofs in $T_{n}$ for the original statements, and vice versa.

The paper ends with a section devoted to *The simple theory of types* where he considers the system $P$ which Gödel uses in Gödel 1931 and a one-sorted system $Q$. The system $P$ contains infinitely many kinds of variables: $x_{1},$ $y_{1},\ldots$; $x_{2},$ $y_{2},\ldots$;…, the truth-functional connectives, the quantifiers for all sorts, the membership predicate *ε*, the symbol 0 for zero and the symbol $f$ for the successor function.

Now, according to Russell’s hierarchy of types, he explicitly says that the membership predicate only occurs between one level and the next, $x_{n}\epsilon y_{n+1}$, and introduces equality at level $n$ using the principle of *Identity of indiscernibles*:

$$ x_{n}=y_{n} \textrm{ stands for } \forall z_{n+1}(x_{n}\epsilon z_{n+1}\leftrightarrow y_{n}\epsilon z_{n+1}) $$

The calculus includes axioms $1_{\omega},\ldots,5_{\omega}$ as above, but for the infinitely many sorts of variables we now have. He also adds *Principles of extensionality*,

$$\vdash \forall z_{n}(z_{n}\epsilon x_{n+1}\leftrightarrow z_{n}\epsilon y_{n+1})\rightarrow x_{n+1}=y_{n+1})$$

and *Principles of class existence*,

$$\vdash \exists y_{n+1}\forall x_{n}(x_{n}\epsilon y_{n+1}\leftrightarrow \varphi).$$

*Peano axioms* are included at level 1.

The one-sorted system $Q$ is basically the same as $P$, but with only one sort of variables. Some years later, Gilmore (1958) pointed out that it is necessary to introduce countably many primitive predicates $\epsilon _{i}$ in $Q$ expressing membership between types $i$ and $i+1$. He shows how to avoid this restriction by correcting Wang’s demonstration of the theorem stating that there is an effective way of finding, given any proof of $\gamma ^{\prime}$ in $L_{1}^{(n)}$ (where $\gamma ^{\prime}$ has a translation to *γ*), a proof of *γ* in $L_{n}$.

### B. Solomon Feferman

In his course *Lectures on Proof Theory* at the 1967 European Summer Meeting of the Association for Symbolic Logic, Solomon Feferman (see Feferman 1968) made two important innovations on the subject: the formal language was many-sorted and it was extended by permitting infinitely long expressions built up using infinite conjunctions and disjunctions. The calculus he introduced was a Gentzen’s sequent calculus, proving not only completeness but also cut elimination theorem as well as some interpolation theorems. One of the reasons he gave in favor of many-sorted logic against its one-sorted translation was that an improved version of Craig’s interpolation lemma can be proved for this language, using some of the characteristic of many-sortedness, but one can not use the standard translation into one-sorted logic to drag along this result from the one-sorted version.

Several years later, in Feferman (1974), he developed some applications of this interpolation theorem and in 2008 he published an article in *Synthese* devoted to Craig’s interpolation theorem, its early history as well as its generalizations and applications, “Harmonious logic: Craig’s interpolation theorem and its descendants” (Feferman 2008). His opinion on the subject was:

> Craig’s interpolation theorem (published 50 years ago) has proved to be a central logical property that has been used to reveal a deep harmony between the syntax and semantics of first order logic.
>
> The article concludes with the role of the interpolation property in the quest for “reasonable” logics extending first-order logic within the framework of abstract model theory.

In 2016, Feferman gave a talk at the *AMS/ASL session on applications of Logic, Model Theory, and Theoretical Computer Science to System Biology* at Seattle where he proposed the use of many-sorted first-order structures for biology studies. He suggested the biological system of *Homo Sapiens* can be defined in terms of the sorts, subsorts, functions, and relations among them. He said that, due to the fact that many-sorted logic is complete,

> In principle, then, that could be used to pursue Woodger’s ideal of rigorous reasoning about biological processes. (2016: 10)


## Notes（原文脚注，引自主文）

[^note-34]: 34\. The official publication date by Princeton University Press is 1956, despite the fact that, in the references of Wang (1952), the date of publication is 1944. We know that early forms of the book were available in manuscript form before 1956 (see Henkin 1996, p. 133). Exercise 55.24 (p. 339) is in Chapter 5 and according to the Preface, the work on Chapters 3, 4, and 5 was done in 1948–1951 (Church 1956, vi).

[^note-35]: 35\. The one-sorted elementary logic Wang refers to is the one presented in Quine 1940.

[^note-36]: 36\. In section 22, Quine says:

> We now turn to a connective “*ε*” which embodies the principal meaning of the ambiguous word “is”. Sometimes “is” has the sense of “$=$” or “is the same as”; such is its sense in *“Paris is the capital of France”*…. But in *“Paris is a city”* the word cannot be so construed. In such contexts “is” expresses rather possession of a property, or membership in a class: Paris belongs to the class of cities. (Quine 1940: 119)

Quine also admits:

> …there are differences in detail between the notion of membership developed here and the notion of membership that Tarski and Gödel took over from Whitehead and Russell. (Quine 1940: 126)