# Proof Theory
**First published Mon Aug 13, 2018; substantive revision Wed Feb 21, 2024**

*Rathjen, Michael, Sieg, Wilfried*

Proof theory is not an esoteric technical subject that was invented to support a formalist doctrine in the philosophy of mathematics; rather, it has been developed as an attempt to analyze aspects of mathematical experience and to isolate, possibly overcome, methodological problems in the foundations of mathematics. The origins of those problems, forcefully and sometimes contentiously formulated in the 1920s, are traceable to the transformation of mathematics in the nineteenth century: the emergence of abstract mathematics, its reliance on set theoretic notions, and its focus on logic in a broad, foundational sense. Substantive issues came to the fore already in the mathematical work and the foundational essays of Dedekind and Kronecker; they concerned the legitimacy of undecidable concepts, the existence of infinite mathematical objects, and the sense of non-constructive proofs of existential statements.

In an attempt to mediate between conflicting foundational positions, Hilbert shifted issues, already around 1900, from a mathematical to a vaguely conceived metamathematical level. That approach was rigorously realized in the 1920s, when he took advantage of the possibility of formalizing mathematics in deductive systems and investigated the underlying formal frames from a strictly constructive, “finitist” standpoint. Hilbert’s approach raised fascinating metamathematical questions—from semantic completeness through mechanical decidability to syntactic incompleteness; however, the hoped-for mathematical resolution of the foundational issues was not achieved. The failure of his *finitist consistency program* raised and deepened equally fascinating methodological questions. A broadened array of problems with only partial solutions has created a vibrant subject that spans computational, mathematical, and philosophical issues—with a rich history.

The main part of our article covers these exciting investigations for an expanded Hilbert Program through 1999—with special, detailed attention to results and techniques that by now can be called “classical” and are of continued interest. Newer, but still closely connected developments are sketched in Appendices: the *proof theory of set theories* in Appendix D, *combinatorial independence results* in Appendix E, and *provably total functions* in Appendix F. Here (infinitary) sequent calculi and suitable systems of ordinal notations are crucial proof theoretic tools. However, we discuss in section 4.2 also Gödel’s Dialectica Interpretation and some of its extensions as an alternative for obtaining relative consistency proofs and describe in section 5.2.1 the systematic attempt of completing the incomplete through recursive progressions. Both topics are analyzed further in Appendix C.2 and Appendix B, respectively. To complete this bird’s eye view of our article, we mention that the *Epilogue*, section 6, not only indicates further proof theoretic topics, but also some directions of current research that are connected to proof theory and of deep intrinsic interest. We have tried to convey the vibrancy of a subject that thrives on concrete computational and (meta-) mathematical work, but also invites and is grounded in general philosophical reflection.

## 1. Proof Theory: A New Subject

Hilbert viewed the *axiomatic method* as the crucial tool for mathematics (and rational discourse in general). In a talk to the Swiss Mathematical Society in 1917, published the following year as *Axiomatisches Denken* (1918), he articulates his broad perspective on that method and presents it “at work” by considering, in detail, examples from various parts of mathematics and also from physics. Proceeding axiomatically is not just developing a subject in a rigorous way from first principles, but rather requires, for advanced subjects, their deeper conceptual organization and serves, for newer investigations, as a tool for discovery. In his talk Hilbert reflects on his investigations of the arithmetic of real numbers and of Euclidean geometry from before 1900. We emphasize the particular form of his axiomatic formulations; they are not logical formulations, but rather mathematical ones: he defines Euclidean space in a similar way as other abstract notions like group or field; that’s why we call it *structural axiomatics*.[^note-1] However, Hilbert turns from the past and looks to the future, pointing out a programmatic direction for research in the *foundations* of mathematics; he writes:

> To conquer this field [concerning the foundations of mathematics] we must turn the concept of a specifically mathematical proof itself into an object of investigation, just as the astronomer considers the movement of his position, the physicist studies the theory of his apparatus, and the philosopher criticizes reason itself.

He then asserts, “The execution of this program is at present still an unsolved task”. During the following winter term 1917–18, Hilbert—with the assistance of Paul Bernays—gave a lecture course entitled *Prinzipien der Mathematik*. Here modern mathematical logic is invented in one fell swoop and completes the shift from structural to formal axiomatics. This dramatic shift allows the constructive, elementary definition of the syntax of theories and, in particular, of the concept of *proof in a formal theory*. This fundamental insight underpins the articulation of the consistency problem and seems to open a way of proving, meta-mathematically, that no proof in a formal theory establishes a contradiction.

That perspective is formulated first in a talk Bernays presented in the fall of 1921, published as “Über Hilberts Gedanken zur Grundlegung der Mathematik” (1922). Starting with a discussion of *structural axiomatics* and pointing out its assumption of a system of objects that satisfies the axioms, he asserts this assumption contains “something so-to-speak transcendent for mathematics”. He raises the question, “which principled position should be taken with respect to it?” Bernays believes that it might be perfectly coherent to appeal to an *intuitive* grasp of the natural number sequence or even of the manifold of real numbers. However, that could not be an intuition in any primitive sense and would conflict with the tendency of the exact sciences to use only restricted means to acquire knowledge.

> Under this perspective we are going to try, whether it is not possible to give a foundation to these transcendent assumptions in such a way that only primitive intuitive knowledge is used. (Bernays 1922: 11)[^bernays-1922]

Meaningful mathematics is to be based, Bernays demands, on primitive intuitive knowledge that includes, however, induction concerning natural numbers—both as a proof and definition principle. In the outline for the lectures *Grundlagen der Mathematik* to be given in the winter term 1921–22, Bernays discusses a few weeks after his talk “constructive arithmetic” and then the “broader formulation of constructive thought”:

> Construction of the proofs, by means of which the formalization of the higher inferences is made possible and the consistency problem is becoming accessible in a general way.

Bernays concludes the outline by suggesting, “This would be followed by the development of proof theory”. The outline was sent to Hilbert on 17 October 1921 and it was followed strictly in the lectures of the following term—with only one terminological change: “constructive” in the above formulations is turned into “finitist”.[^note-2]

Bernays’s notes of the 1921/22 lectures reflect the consequence of that change in attitude. They contain a substantial development of “finitist arithmetic” and “finitist logic” in a quantifier-free formalism. Finitist arithmetic involves induction and primitive recursion[^note-3] from the outset, and the central metamathematical arguments all proceed straightforwardly by induction on proof figures. The third part of these lectures is entitled *The grounding of the consistency of arithmetic by Hilbert’s new proof theory*. Here we find the first significant consistency proof—from a finitist perspective.[^note-4] The proof is sketched in Hilbert’s Leipzig talk (Hilbert 1923: 184)[^hilbert-1923] and was presented in a modified form during the winter term of 1922/23; in that form the proof is given in Ackermann 1925: 4–7. Ackermann’s article was submitted for publication in early 1924, and by then the proof had taken on a certain canonical form that is still found in the presentation of Hilbert and Bernays 1934: 220–230. Let us see what was achieved by following Ackermann’s concise discussion.

### 1.1 Hilbert’s *Ansatz* and Results

The proof is given in section II of Ackermann’s paper entitled, tellingly, *The consistency proof before the addition of the transfinite axioms*. Ackermann uses a logical calculus in axiomatic form that is taken over from Hilbert’s lectures and is discussed below in section 2. Here we just note that it involves two logical rules, namely, modus ponens and substitution (for individual, function and statement variables) in axioms. The non-logical axioms concern identity, zero and successor, and recursion equations that define primitive recursive functions. The first step in the argument turns the linear proof into a tree, so that any formula occurrence is used at most once as a premise of an inference (*Auflösung in Beweisfäden*); this is done in preparation for the second step, namely, the elimination of all necessarily free variables (*Ausschaltung der Variablen*); in the third step, the numerical value of the closed terms is computed (*Reduktion der Funktionale*). The resulting syntactic configurations, a *Beweisfigur*, contains now only *numerical formulae* that are built up from equations or inequations between numerals and Boolean connectives; these formulae can be effectively determined to be true or false. By induction on the “*Beweisfigur*” one shows that all its component formulae are true; thus, a formula like $0\ne 0$ is not provable. The induction principle can be directly incorporated into these considerations when it is formulated as a rule for quantifier-free statements. That was not done in Ackermann’s discussion of the proof, but had been achieved already by Hilbert and Bernays in their 1922/23 lectures.

These proof theoretic considerations are striking and important as they involve for the first time genuine transformations of formal derivations. Nevertheless, they are preliminary as they concern a quantifier-free theory that is a *part* of finitist mathematics and *need* not be secured by a consistency proof. What has to be secured is “transfinite logic” with its “ideal elements”, as Hilbert put it later. The strategy was direct and started to emerge already in 1921. First, introduce functional terms by the *transfinite axiom*[^note-5]

$$A(a) \to A(\varepsilon x\ldot A(x))$$

and define quantifiers by

$$ \exists x A(x) \leftrightarrow A(\varepsilon x\ldot A(x)) $$

and

$$ \forall x A(x) \leftrightarrow A(\varepsilon x\ldot \neg A(x)). $$

Using the epsilon terms, quantifiers can now be eliminated from proofs in quantificational logic, thus transforming them into quantifier-free ones. Finally, the given derivation allows one, so it was conjectured, to determine numerical values for the epsilon terms. In his Leipzig talk of September 1922, published in 1923, Hilbert discussed this *Ansatz* for eliminating quantifiers and reducing the transfinite case to that of the quantifier-free theory. He presented the actual execution of this strategic plan only “for the simplest case” (in Hilbert 1923: 1143–1144)[^hilbert-1923]. However, the talk was crucial in the development of proof theory and the finitist program: “With the structure of proof theory, presented to us in the Leipzig talk, the principled form of its conception had been reached”. That is how Bernays characterizes its achievement in his essay on *Hilbert’s investigations of the foundations of arithmetic* (1935: 204)

Ackermann continued in section III of his 1925 at the very spot where Hilbert and Bernays had left off. His paper, submitted to *Mathematische Annalen* in March of 1924, and the corrective work he did in 1925 led to the conviction that the consistency of elementary arithmetic had been established. The corrective work had been done to address difficulties von Neumann had pointed out, but was not published by Ackermann; it was only presented in the second volume of Hilbert and Bernays 1939 (pp. 93–130).[^note-6] Von Neumann’s own proof theoretic investigations, submitted to *Mathematische Zeitschrift* in July 1925, were published under the title *Zur Hilbertschen Beweistheorie* in 1927. Hilbert’s 1928 Bologna Lecture prominently took Ackermann’s and von Neumann’s work as having established the consistency of elementary arithmetic, the proof making use only of finitist principles. Let F be a theory containing exclusively such principles, like *primitive recursive arithmetic* **PRA**; the principles of **PRA** (defined in more detail in [^note-3]) consist of the Peano axioms for zero and successor, the defining equations for all primitive recursive functions, and induction for atomic formulas. Now the significance of a consistency proof in F can be articulated as follows:

Theorem 1.1 Let T be a theory that contains a modicum of arithmetic and let *A* be a $\Pi^0_1$-statement, i.e., one of the form $\forall x_1\ldots\forall x_n\,P(x_1,\ldots,x_n)$ with quantifiers ranging over naturals and *P* a primitive recursive predicate, i.e., a predicate with a primitive recursive characteristic function. If F proves the consistency of T and T proves *A*, then F proves *A*.

This theorem can be expressed and proved in **PRA** and ensures that a T-proof of a “real”, finitistically meaningful statement *A* leads to a finitistically valid statement. This point is made clear in Hilbert’s 1927-Hamburg lecture (Hilbert 1927)[^hilbert-1927]. There he takes *A* to be the Fermat proposition and argues that if we had a proof of *A* in a theory containing “ideal” elements, a finistist consistency proof for that theory would allow us to transform that proof into a finitist one.

The belief that Ackermann and von Neumann had established the consistency of elementary arithmetic was expressed as late as December 1930 by Hilbert in his third Hamburg talk (Hilbert 1931a)[^hilbert-1931a] and by Bernays in April 1931 in a letter to Gödel (see Gödel 2003: 98–103)[^gödel-2003]. Bernays asserts there that he has “repeatedly considered [Ackermann’s modified proof] and viewed it as correct”. He continues, referring to Gödel’s incompleteness results,

> On the basis of your results one must now conclude, however, that that proof cannot be formalized within the system *Z* [of elementary number theory]; this must in fact hold true even if the system is restricted so that, of the recursive definitions, only those for addition and multiplication are retained. On the other hand, I don’t see at which place in Ackermann’s proof the formalization within *Z* should become impossible, …

At the end of his letter, Bernays mentions that Herbrand misunderstood him in a recent conversation on which Herbrand had reported in a letter to Gödel with a copy to Bernays. Not only had Herbrand misunderstood Bernays, but Bernays had also misunderstood Herbrand as to the extent of the latter’s consistency result that was to be published a few months later as Herbrand 1931. Bernays understood Herbrand as having claimed that he had established the consistency of full first-order arithmetic: Herbrand’s system is indeed a first-order theory with a rich collection of finitist functions, but it uses the induction principle only for quantifier-free formulae.[^note-7] Gödel asserted in December 1933 that this theorem of Herbrand’s was even then the strongest result that had been obtained in the pursuit of Hilbert’s finitist program, and he formulated the result in a beautiful informal way as follows:

> If we take a theory, which is constructive in the sense that each existence assertion made in the axioms is covered by a construction, and if we add to this theory the non-constructive notion of existence and all the logical rules concerning it, e.g., the law of the excluded middle, we shall never get into any contradiction. (Gödel 1933: 52)[^gödel-1933]

Gödel himself had been much more ambitious in early 1930; his goal was then to prove the consistency of analysis! According to Wang (1981: 654), his idea was “to prove the consistency of analysis by number theory, where one can assume the truth of number theory, not only the consistency”. The plan for establishing the consistency of analysis relative to number theory did not work out, instead Gödel found that sufficiently strong formal theories like *Principia Mathematica* and Zermelo-Fraenkel set theory are (syntactically) incomplete.

### 1.2 Incompleteness and a Reduction

In 1931 Gödel published a paper (1931a) that showed that there are true arithmetic statements that cannot be proved in the formal system of *Principia Mathematica*, assuming *PM* to be consistent. His methods not only applied to *PM* but to any formal system that contains a modicum of arithmetic. A couple of months after Gödel had announced this result at a conference in Königsberg in September 1930, von Neumann and Gödel independently realized that a striking corollary could be drawn from the incompleteness theorem. Every consistent and effectively axiomatized theory that allows for the development of basic parts of arithmetic cannot prove its own consistency. This came to be known as the *second incompleteness theorem*. (For details on these theorems and their history see appendix A.4) The second incompleteness theorem refutes the general ambitions of Hilbert’s program under the sole and very plausible assumption that finitist mathematics is contained in one of the formal theories of arithmetic, analysis or set theory. As a matter of fact, contemporary characterizations of finitist mathematics have elementary arithmetic as an upper bound.[^note-8] In response to Gödel’s result, Hilbert attempted in his last published paper (1931b) to formulate a strategy for consistency proofs that is reminiscent of his considerations in the early 1920s (when thinking about the object theories as constructive) and clearly extends the finitist standpoint. He introduced a broad constructive framework that includes full intuitionist arithmetic and suggested extendibility of the new “method” to “the case of function variables and even higher sorts of variables”. He also formulated a new kind of rule that allowed the introduction of a new axiom $\forall x A(x)$ as soon as all the numerical instances $A(n)$ had been established by finitist proofs; in 1931 that is done for quantifier-free $A(x)$, whereas in 1931b that is extended to formulae of arbitrary complexity. The semi-formal calculi, which articulate the broader framework, are based on rules that reflect mathematical practice, but also define the meaning of logical connectives. Indeed, Hilbert’s reasons for taking them to be evidently consistent are expressed in a single sentence: “All transfinite rules and inference schemata are consistent; for they amount to definitions”. Adding the *tertium non datur* in the form

$${\forall x A(x)} \lor {\exists x \neg A(x)}$$

yields now the classical version of the theory and it is that addition that has to be justified.[^note-9] Hilbert’s problematic considerations for this new metamathematical step inspired Gentzen’s “Urdissertation” when he began working in late 1931 on a consistency proof for elementary arithmetic.[^note-10]

As part of his “Urdissertation”, Gentzen had established by the end of 1932 the reduction of classical to intuitionist arithmetic, a result that had also been obtained by Gödel. Gentzen’s investigations led, finally in 1935, to his first consistency proof for arithmetic. In the background was a normal form theorem for intuitionist logic that will be discussed in the next section together with Gentzen’s actual dissertation and the special calculi he introduced there. Now we just formulate the Gentzen-Gödel result “connecting” classical first-order number theory **PA** with its intuitionist version **HA**. The non-logical principles of these theories aim at describing $\fN$, the arguably most important structure in mathematics, namely, Dedekind’s simply infinite system $\bbN$ together with zero, successor, multiplication, exponentiation and the less-than relation:

$${\fN}=(\bbN; 0^{\bbN}, S^{\bbN},+^{\bbN},\times^{\bbN},E^{\bbN},<^{\bbN}).$$

They are formulated in the first-order language that has the relation symbols =, <, the function symbols *S*, +, $\times$, *E* and the constant symbol 0. The axioms comprise the usual equations for zero, successor, addition, multiplication, exponentiation, and the less-than relation. In addition, the *induction principle* is given by the schema $$\tag{IND} {F(0)} \land {\forall x[F(x)\to F(Sx)]\to \forall x F(x)} $$ for all formulae $F(x)$ of the language. These principles together with classical logic constitute the theory of *first order arithmetic* or *first order number theory*, also known as *Dedekind-Peano arithmetic*, **PA**; together with intuitionist logic they constitute *intuitionistic first order arithmetic* commonly known as *Heyting-arithmetic*, **HA**.

Now we are considering the syntactic translation $\tau$ from the common language of **PA** and **HA** into its “negative” fragment that replaces disjunctions $A\lor B$ by their de Morgan equivalent $\neg (\neg A\land \neg B)$ and existential statements $\exists x A(x)$ by $\neg \forall x \neg A(x)$. The reductive result obtained by Gentzen and Gödel in 1933 is now stated quite easily:

Theorem 1.2

1. **PA** proves the equivalence of *A* and $\tau(A)$ for any formula *A*.
2. If **PA** proves *A*, then **HA** proves $\tau(A)$.

For atomic sentences like $1\ne 1$ the translation $\tau$ is clearly the identity, and the provability of $1\ne 1$ in **PA** would imply its provability in **HA**. Thus, **PA** is consistent relative to **HA**. This result is technically of great interest and had a profound effect on the perspective concerning the relationship between finitism and intuitionism: finitist and intuitionist mathematics were considered as co-extensional; this theorem showed that intuitionist mathematics is actually stronger than finitist mathematics. Thus, if the intuitionist standpoint is taken to guarantee the soundness of **HA**, then it guarantees the consistency of **PA**. The corresponding connection between classical and intuitionist logic had been established already by Kolmogorov (1925) who not only formalized intuitionist logic but also observed the translatability of classical into intuitionist logic. His work, though, seems not to have been noticed at the time or even in 1932, when Gentzen and Gödel established their result for classical and intuitionist arithmetic.

The foundational discussion concerning extended “constructive” viewpoints is taken up in section 4. There, and throughout our paper the concepts of “proof-theoretic reducibility” and “proof-theoretic equivalence” will play a central role. The connection between **PA** and **HA** is paradigmatic and leads to the notion of *proof-theoretic reduction*. Before we can furnish a precise definition, we should perhaps stress that many concepts can be expressed in the language of **PRA** (as well as **PA**) via coding, also known as *Gödel numbering*. Any finite object such as a string of symbols or an array of symbols can be coded via a single natural number in such a way that the string or array can be retrieved from the number when we know how the coding is done. Typical finite objects include formulae in a given language and also proofs in a theory. Talk about formulae or proofs can then be replaced by talking about predicates of numbers that single out the codes of formulae and proofs, respectively. We then say that the concepts of formula and proof have been arithmetized and thereby rendered expressible in the language of **PRA**.

Definition 1.3 Let $\bT_1$, $\bT_2$ be a pair of theories with languages $\cL_1$ and $\cL_2$, respectively, and let $\Phi$ be a (primitive recursive) collection of formulae common to both languages. Furthermore, $\Phi$ should contain the closed equations of the language of **PRA**.

We then say that $\bT_1$ is *proof-theoretically $\Phi$-reducible to $\bT_2$*, written $\bT_1\leq_{\Phi}\bT_2$, if there exists a primitive recursive function *f* such that

$$\tag{1} \PRA\vdash \forall x \forall y\,[ {\rform_{\Phi}(x)} \land {\proof_{\bT_1}( y,x)} \rightarrow {\proof_{\bT_2}(f(y),x)}].$$

Here $\rform_{\Phi}$ and $\proof_{\bT_i}$ are arithmetized formalizations of $\Phi$ and the proof relation in $\bT_i$, respectively, i.e., $\rform_{\Phi}(x)$ expresses that *x* is the Gödel number of a formula in $\Phi$ while $\proof_{\bT_i}(y,x)$ expresses that *y* codes a proof in $\bT_i$ of a formula with Gödel number *x*.

$\bT_1$ and $\bT_2$ are said to be *proof-theoretically $\Phi$-equivalent*, written $\bT_1\equiv_{\Phi}\bT_2$, if $\bT_1\leq_{\Phi}\bT_2$ and $\bT_2\leq_{\Phi}\bT_1$.

The appropriate class $\Phi$ is revealed in the process of reduction itself, so that in the statement of theorems we simply say that $\bT_1$ is *proof-theoretically reducible* to $\bT_2$ (written $\bT_1\leq \bT_2$) and $\bT_1$ and $\bT_2$ are *proof-theoretically equivalent* (written $\bT_1 \equiv \bT_2$), respectively. Alternatively, we shall say that $\bT_1$ and $\bT_2$ have the *same proof-theoretic strength* when $\bT_1\equiv \bT_2$. In practice, if $\bT_1\equiv \bT_2$ is shown via proof-theoretic means[^note-11] this always entails that the two theories prove at least the same $\Pi^0_2$ sentences (those of the complexity of the twin prime conjecture). The complexity of formulae of **PRA** is stratified as follows. The $\Sigma^0_0$ and $\Pi^0_0$ formulae are of the form $R(t_1,\ldots,t_n)$ where *R* is a predicate symbol for an *n*-ary primitive recursive predicate. A formula is $\Sigma^0_{k+1}$ ($\Pi^0_{k+1}$) if it is of the form

$$ \exists y_1\ldots \exists y_m\,F(y_1,\ldots,y_m) (\forall y_1\ldots \forall y_m\,F(y_1,\ldots,y_m)) $$

with $F(y_1,\ldots,y_m)$ being of complexity $\Pi^0_k$ ($\Sigma^0_k$). Thus the complexity of a formula is measured in terms of quantifier alternations. For instance $\Pi^0_2$-formulae have two alternations starting with a block of universal quantifiers or more explicitly they are of the shape

$$\forall x_1\ldots\forall x_n \exists y_1\ldots \exists y_m\,R(x_1,\ldots,x_n,y_1,\ldots,y_m)$$

with *R* primitive recursive.

## 2. New Logical Calculi

For the reduction of classical elementary number theory to its intuitionist version, Gödel and Gentzen used different logical calculi. Gödel used the system Herbrand had investigated in his 1931, whereas Gentzen employed the formalization of intuitionist arithmetic from Heyting 1930. For his further finitist investigations Gentzen introduced new calculi that were to become of utmost importance for proof theory: natural deduction and sequent calculi.

### 2.1 From Axioms to Rules: Natural Reasoning

As we noted above, Gentzen had already begun in 1931 to be concerned with the consistency of full elementary number theory. As the logical framework he used, what we now call, natural deduction calculi. They evolved from an axiomatic calculus that had been used by Hilbert and Bernays since 1922 and introduced an important modification of the calculus for sentential logic. The connectives $\land $ and $\lor$ are incorporated, and the axioms for these connectives are as follows:

$$\begin{align} A\land B & \to A \\ A\land B & \to B \\ A & \to (B \to A\land B) \\ A & \to A\lor B \\ B & \to A\lor B \\ (A \to C) & \to ((B \to C) \to (A\lor B \to C)) \end{align}$$

Hilbert and Bernays introduced this new logical formalism for two reasons, (i) to be able to better and more easily formalize mathematics, and (ii) to bring out the understanding of logical connectives in methodological parallel to the treatment of geometric concepts in *Foundations of geometry*. The methodological advantages of this calculus are discussed in Bernays 1927: 10:

> The starting formulae can be chosen in quite different ways. A great deal of effort has been spent, in particular, to get by with a minimal number of axioms, and the limit of what is possible has indeed been reached. However, for the purposes of logical investigations it is better to separate out, in line with the axiomatic procedure for geometry, different axiom groups in such a way that each of them expresses the role of a single logical operation.

Then Bernays lists four groups, namely, axioms for the conditional $\to$, for $\land $ and $\lor$ as above, and for negation $\neg$. The axioms for the conditional are not only reflecting logical properties, but also structural features as in the later sequent calculus (and in Frege’s *Begriffsschrift*, 1879).

$$\begin{align} A & \to (B \to A)\\ (A \to (A \to B)) & \to (A \to B)\\ (A \to (B \to C)) & \to (B \to (A \to C))\\ (B \to C) & \to ((A \to B) \to (A \to C)) \end{align}$$

As axioms for negation one can choose:

$$\begin{align} A & \to (\neg A \to B)\\ (A \to B) & \to ((\neg A \to B) \to B) \end{align}$$

Hilbert formulates this logical system in *Über das Unendliche* and in his second Hamburg talk of 1927, but gives a slightly different formulation of the axioms for negation, calling them the *principle of contradiction* and the *principle of double negation*:

$$\begin{align} (A \to (B \land \neg B)) &\to \neg A\\ \neg\neg A & \to A \end{align}$$

Clearly, the axioms correspond directly to the natural deduction rules for these connectives, and one finds here the origin of Gentzen’s natural deduction calculi. Bernays had investigated in his *Habilitationsschrift* (1918) rule based calculi. However, in the given context, the simplicity of the metamathematical description of calculi seemed paramount, and in Bernays 1927 (p. 17) one finds the programmatic remark: “We want to have as few rules as possible, rather put much into axioms”.

Gentzen was led to a rule-based calculus with *introduction* and *elimination rules* for every logical connective. The truly distinctive feature of this new type of calculus was for Gentzen, however, making and discharging assumptions. This feature, he remarked, most directly reflects a crucial aspect of mathematical argumentation.[^note-12] Here we formulate the distinctive rules that involve contradictions and go beyond minimal logic that has I- and E-rules for all logical connectives. Intuitionist logic is obtained from minimal logic by adding the rule: from $\perp$ infer any formula *A*, i.e., *ex falso quodlibet*. In the case of classical logic, if a proof of $\perp$ is obtained from the assumption $\neg A$, then infer *A* (and cancel the assumption $\neg A$). Gentzen discovered a remarkable fact for the intuitionist calculus, having observed that proofs can have peculiar *detours* of the following form: a formula is obtained by an I-rule and is then the major premise of the corresponding E-rule. For conjunction such a detour is depicted as follows:

$$ \cfrac{\begin{array}{c}\vdots \\ A\end{array} \quad \begin{array}{c}\vdots \\ B\end{array}} {\cfrac{A\land B}{B}} $$

Clearly, a proof of *B* is already contained in the given derivation. Proofs without detours are called *normal*, and Gentzen showed that any proof can be effectively transformed via “reduction steps” into a normal one.

Theorem 2.1 (Normalization for intuitionist logic) A proof of *A* from a set of assumptions $\Gamma$ can be transformed into a normal proof of *A* from the same set of assumptions.

Focusing on normal proofs, Gentzen proved then that the complexity of formulae in such proofs can be bounded by that of assumptions and conclusion.

Corollary 2.2 (Subformula property) If $\cD$ is a normal proof of *A* from $\Gamma$, then every formula in $\cD$ is either a subformula of an element $\Gamma$ or of *A*.

As Gentzen recounts matters at the very beginning of his dissertation (1934/35), he was led by the investigation of the natural calculus to his *Hauptsatz*[^note-13] when he could not extend the considerations to classical logic.

> To be able to formulate it [the *Hauptsatz*] in a direct way, I had to base it on a particularly suitable logical calculus. The calculus of natural deduction turned out not to be appropriate for that purpose.

So, Gentzen focused his attention on sequent calculi that had been introduced by Paul Hertz and which had been the subject of Gentzen’s first scientific paper (1932).

### 2.2 Sequent Calculi

In his thesis Gentzen introduced a form of the sequent calculus and his technique of *cut elimination*. As this is a tool of utmost importance in proof theory, an outline of the underlying ideas will be discussed next. The sequent calculus can be generalized to so-called infinitary logics and is central for ordinal analysis. The *Hauptsatz* is also called the *cut elimination theorem*.

We use upper case Greek letters $\Gamma,\Delta,\Lambda,\Theta,\Xi\ldots$ to range over finite lists of formulae. $\Gamma\subseteq \Delta$ means that every formula of $\Gamma$ is also a formula of $\Delta$. A *sequent* is an expression $\Gamma\Rightarrow \Delta$ where $\Gamma$ and $\Delta$ are finite sequences of formulae $A_1,\ldots,A_n$ and $B_1,\ldots, B_m$, respectively. We also allow for the possibility that $\Gamma$ or $\Delta$ (or both) are empty. The empty sequence will be denoted by $\emptyset$. $\Gamma \Rightarrow \Delta$ is read, informally, as $\Gamma$ yields $\Delta$ or, rather, the *conjunction* of the $A_i$ yields the *disjunction* of the $B_j$.

The *logical axioms* of the calculus are of the form

$$A \Rightarrow A $$

where *A* is any formula. In point of fact, one could limit this axiom to the case of atomic formulae *A*. We have *structural rules* of the form

$$ \frac{\Gamma \Rightarrow \Delta}{\Gamma' \Rightarrow \Delta'} \qquad \textrm{if } \Gamma \subseteq \Gamma', \Delta \subseteq \Delta'. $$

A special case of the structural rule, known as *contraction*, occurs when the lower sequent has fewer occurrences of a formula than the upper sequent. For instance, $A, \Gamma\Rightarrow\Delta, B$ follows structurally from $A,A,\Gamma \Rightarrow \Delta,B,B$.

Now we list the rules for the logical connectives.

$$\begin{array}{cc} \textrm{Left} & \textrm{Right} \\ \displaystyle \frac{\Gamma \Rightarrow {\Delta,A}}{{\neg A, \Gamma} \Rightarrow \Delta} & \displaystyle \frac{{B, \Gamma} \Rightarrow {\Delta}}{{\Gamma} \Rightarrow {\Delta, \neg B}} \\[2ex] \displaystyle \frac{{\Gamma} \Rightarrow {\Delta, A} \qquad {B,\Lambda} \Rightarrow {\Theta}} {{{A\rightarrow B},\Gamma, \Lambda} \Rightarrow {\Delta, \Theta}} & \displaystyle \frac{{A, \Gamma} \Rightarrow {\Delta, B}}{{\Gamma} \Rightarrow {\Delta, {A \rightarrow B}}} \\[2ex] \displaystyle \frac{{A, \Gamma} \Rightarrow {\Delta}}{{A\land B,\Gamma} \Rightarrow {\Delta}} \quad \frac{{B, \Gamma} \Rightarrow {\Delta}}{{A\land B,\Gamma} \Rightarrow {\Delta}} & \displaystyle \frac{{\Gamma} \Rightarrow {\Delta, A} \qquad {\Gamma} \Rightarrow {\Delta, B}} {{\Gamma} \Rightarrow {\Delta, {A\land B}}} \\[2ex] \displaystyle \frac{{A,\Gamma} \Rightarrow {\Delta} \qquad {B,\Gamma} \Rightarrow {\Delta}} {{{A\lor B},\Gamma} \Rightarrow {\Delta}} & \displaystyle \frac{{\Gamma} \Rightarrow {\Delta, A}}{{\Gamma} \Rightarrow {\Delta, {A\lor B}}} \quad \frac{{\Gamma} \Rightarrow {\Delta, B}}{{\Gamma} \Rightarrow {\Delta, {A\lor B}}} \end{array} $$ $$\begin{array}{lccclc} \forall L & \displaystyle \frac{F(t),\Gamma \Rightarrow \Delta}{\forall x F(x),\Gamma \Rightarrow \Delta} & && \forall R & \displaystyle \frac{\Gamma \Rightarrow {\Delta, F(a)}}{\Gamma \Rightarrow {\Delta, \forall x F(x)}} \\[2ex] \exists L & \displaystyle \frac{F(a),\Gamma \Rightarrow \Delta}{\exists x F(x),\Gamma \Rightarrow \Delta} & && \exists R & \displaystyle \frac{\Gamma \Rightarrow {\Delta, F(t)}}{\Gamma \Rightarrow {\Delta, \exists x F(x)}} \end{array} $$

In $\forall L$ and $\exists R$, *t* is an arbitrary term. The variable *a* in $\forall R$ and $\exists L$ is an *eigenvariable* of the respective inference, i.e., *a* is not to occur in the *lower sequent*.

Finally, we have the special *Cut Rule*

$$ \frac{\Gamma \Rightarrow {\Delta, A} \qquad {A, \Lambda} \Rightarrow \Theta} {{\Gamma, \Lambda} \Rightarrow {\Delta, \Theta}} \tag*{Cut} $$

The formula *A* is called the *cut formula* of the inference.

In the rules for logical operations, the formulae highlighted in the premises are called the *minor formulae* of that inference, while the formula highlighted in the conclusion is the *principal formula* of that inference. The other formulae of an inference are called *side formulae*. A *proof* (also known as a *deduction* or *derivation*) $\cD$ is a tree of sequents satisfying the conditions that (i) the topmost sequents of $\cD$ are logical axioms and (ii) every sequent in $\cD$ except the lowest one is an upper sequent of an inference whose lower sequent is also in $\cD$. A sequent $\Gamma \Rightarrow \Delta$ is *deducible* if there is a proof having $\Gamma \Rightarrow \Delta$ as its bottom sequent.

The Cut rule differs from the other rules in an important respect. With the rules for introducing connectives, one sees that every formula that occurs above the line occurs below the line either directly, or as a subformula of a formula below the line. That is also true for the structural rules. (Here $A(t)$ is counted as a subformula, in a slightly extended sense, of both $\exists xA(x)$ and $\forall xA(x)$.) But in the case of the Cut rule, the cut formula *A* disappears. Gentzen showed that rules with “vanishing formulas” can be eliminated.

Theorem 2.3 (Gentzen’s *Hauptsatz*) If a sequent $\Gamma \Rightarrow \Delta$ is deducible, then it is also deducible without the Cut rule; the resulting proof is called *cut-free* or *normal*.

The secret to Gentzen’s *Hauptsatz* is the symmetry of left and right rules for all the logical connectives including negation. The proof of the cut elimination theorem is rather intricate as the process of removing cuts interferes with the structural rules. It is contraction that accounts for the high cost of eliminating cuts. Let $\lvert \cD\rvert$ be the *height* of the deduction $\cD$ and let $rank(\cD)$ be the *supremum* of the *lengths of cut formulae* occurring in $\cD$. Turning $\cD$ into a cut-free deduction of the same end sequent results, in the worst case, in a deduction of height $\cH(rank(\cD),\lvert \cD\rvert)$ where $\cH(0,n)=n$ and $\cH(k+1,n)=4^{\cH(k,n)}$, yielding hyper-exponential growth.

The sequent calculus we have been discussing allows the proof of classically, but not intuitionistically correct formulae, for example, the law of excluded middle. An intuitionist version of the sequent calculus can be obtained by a very simple structural restriction: there can be at most one formula on the right hand side of the sequent symbol $\Rightarrow$. The cut elimination theorem is also provable for this intuitionist variant. In either case, the *Hauptsatz* has an important corollary that parallels that of the Normalization theorem (for intuitionist logic) and expresses the subformula property.

Corollary 2.4 (Subformula property) If $\cD$ is a cut-free proof of the sequent $\Gamma\Rightarrow\Delta$, then all formulae in $\cD$ are subformulae of elements in either $\Gamma$ or $\Delta$.

This Corollary has another direct consequence that explains the crucial role of the *Hauptsatz* for obtaining consistency proofs.

Corollary 2.5 (Consistency) A contradiction, i.e., the empty sequent $\emptyset \Rightarrow \emptyset$, is not provable.

**Proof**: Assume that the empty sequent is provable; then, according to the *Hauptsatz* it has a cut-free derivation $\cD$. The previous corollary assures us that only empty sequents can occur in $\cD$; but such a $\cD$ does not exist since every proof must contain axioms. $\qed$

The foregoing results are solely concerned with pure logic. Formal theories that axiomatize mathematical structures or serve as formal frameworks for developing substantial chunks of mathematics are based on logic but have additional axioms germane to their purpose. If they are of the latter kind, such as *first-order arithmetic* or *Zermelo-Fraenkel set theory*, they will assert the existence of *mathematical objects* and their properties. What happens when we try to apply the procedure of cut elimination to theories? Axioms are usually detrimental to this procedure. It breaks down because the symmetry of the sequent calculus is lost. In general, one cannot remove cuts from deductions in a theory T when the cut formula is an axiom of T. However, sometimes the axioms of a theory are of *bounded syntactic complexity*. Then the procedure applies partially in that one can remove all cuts that exceed the complexity of the axioms of T. This gives rise to *partial cut elimination*. It is a very important tool in proof theory. For example, it can be used to analyze theories with restricted induction (such as fragments of **PA**; cf. Sieg 1985)[^sieg-1985]. It also works very well if the axioms of a theory can be presented as *atomic intuitionist sequents* (also called *Horn clauses*), yielding the completeness of *Robinson*’s *resolution method* (see Harrison 2009)[^harrison-2009].

Using the *Hauptsatz* and its Corollary, Gentzen was able to capture all of the consistency results that had been obtained prior to 1934 including Herbrand’s, that had been called by Gödel in his 1933 “the most far-reaching” result. They had been obtained at least in principle for fragments of elementary number theory; in practice, Gentzen did not include the quantifier-free induction principle. Having completed his dissertation, Gentzen went back to investigate natural deduction calculi and obtained in 1935 his first consistency proof for full first-order arithmetic. He formulated, however, the natural calculus now in “sequent form”: instead of indicating the assumptions on which a particular claim depended by the undischarged ones in its proof tree, they are attached now to every node of the tree. The “sequents” that are being proved are of the form $\Gamma \Rightarrow A$, where all the logical inferences are carried out on the right hand side. This proof was published only in 1974; it was subsequently analyzed most carefully in Tait 2015 and Buchholz 2015. It was due to criticism of Bernays and Gödel that Gentzen modified his consistency proof quite dramatically; he made use of transfinite induction, as will be discussed in detail in the next section. Here we just mention that Bernays extensively discussed transfinite induction in *Grundlagen der Mathematik II*. The main issue for Bernays was the question, *is it still a finitist principle?*—Bernays did not discuss, however, two other aspects of Gentzen’s work, namely, the use of structural features of formal deductions in consistency proofs and the attempt of gaining a constructive, semantic understanding of intuitionist arithmetic. The former became crucial for proof theoretic investigations; the latter influenced Gödel and his functional interpretation via computable functionals of finite type.[^note-14] The two aspects together opened a new era for proof theory and mathematical logic with the goal of proving the consistency of analysis. We will see, how far current techniques lead us and what foundational significance one can attribute to them.

## 3. Gentzen’s Consistency Proof

Cut elimination fails for first-order arithmetic (i.e., **PA**), not even partial cut elimination is possible since the induction axioms have unbounded complexity. Gentzen, however, found an ingenious way of dealing with purported contradictions in arithmetic. In Gentzen 1938b he showed how to effectively transform an alleged **PA**-proof of an inconsistency (the empty sequent) in his sequent calculus into another proof of the empty sequent such that the latter gets assigned a smaller ordinal than the former. Ordinals are a central concept in set theory as well as in proof theory. To present Gentzen’s work we shall first discuss the notion of ordinal from a proof-theoretic point of view.

### 3.1 Ordinals in Proof Theory

This is the first time we talk about the transfinite and ordinals in proof theory. Ordinals have become very important in advanced proof theory. The concept of an ordinal is a generalization of that of a natural number. The latter are used for counting finitely many things whereas ordinals can also “count” infinitely many things. It is derived from the concept of an ordering $\prec$ of a set *X* which arranges the objects of *X* in order, one after another, in such a way that for every predicate *P* on *X* there is always a first element of *X* with respect to $\prec$ that satisfies *P* if there is at least one object in *X* satisfying *P*. Such an ordering is called a *well-ordering* of *X*. The usual less-than relation on $\bbN$ is certainly a well-ordering. Here every number $\ne 0$ is the successor of another number. If one orders the natural numbers $>0$ in the usual way but declares that 0 is bigger than every number $\ne 0$ one arrives at another ordering of $\bbN$. Let’s call it $\prec$. $\prec$ is also a well-ordering of $\bbN$. This time 1 is the least number with respect to $\prec$. However, 0 plays a unique role. There are infinitely many numbers $\prec 0$ and there is no number $m\prec 0$ such that 0 is the next number after *m*. Such numbers are are called limit numbers (with respect to $\prec$).

In order to be able to formulate Gentzen’s results from the end of section 3.3, we have to “arithmetize” the treatment of ordinals. Let us first state some precise definitions and a Cantorian theorem.

Definition 3.1 A non-empty set *A* equipped with a total ordering $\prec$ (i.e., $\prec$ is transitive, irreflexive, and

$$\forall x,y\in A\,[{x\prec y}\lor {x=y}\lor {y\prec x}])$$

is a *well-ordering* if every non-empty subset *X* of *A* contains a $\prec$-least element, i.e.,

$$(\exists u\in X)(\forall y\in X)[{u\prec y}\lor {u=y}].$$

The elements of a well-ordering $(A,\prec)$ can be divided into three types. Since *A* is non-empty there is a least element with respect to $\prec$ which is customarily denoted by 0 or $0_A$. Then there are elements $a\in A$ such that there exists $b\prec a$ but there is no *c* between *b* and *a*. These are the successor elements of *A*, with *a* being the successor of *b*. An element $c\in A$ such that $0\prec c$ and for all $b\prec c$ there exists $d\in A$ with $b\prec d\prec c$ is said to be a limit element of *A*.

In set theory a set is called *transitive* just in case all its elements are also subsets. An *ordinal* in the set-theoretic sense is a transitive set that is well-ordered by the elementhood relation $\in$. It follows that each ordinal is the set of its predecessors. According to the trichotomy above, there is a least ordinal (which is just the empty set) and all other ordinals are either successor or limit ordinals. The first limit ordinal is denoted by $\omega$.

Fact 3.2 Every well-ordering $(A,\prec)$ is order isomorphic to a unique ordinal $(\alpha,\in)$.

Ordinals are traditionally denoted by lower case Greek letters $\alpha,\beta,\gamma,\delta,\ldots$ and the relation $\in$ on ordinals is notated simply by $<$. If $\beta $ is a successor ordinal, i.e., $\beta$ is the successor of some (necessarily unique) ordinal $\alpha$, we also denote $\beta$ by $\alpha'$. Another important fact is that for any family of ordinals $\alpha_i$ for $i\in I$ (*I* some set) there is a smallest ordinal, denoted by $\sup_{i\in I}\alpha_i$, that is bigger than every ordinal $\alpha_i$.

The operations of addition, multiplication, and exponentiation can be defined on all ordinals by using case distinctions and transfinite recursion (on $\alpha$). The following states the definitions just to convey the flavor:

$$\begin{align} \beta+0 &= \beta & \beta+\alpha' &=(\beta+\alpha)' &\displaystyle \beta+\lambda &=\sup_{\xi<\lambda}(\beta+\xi)\\ \beta\cdot 0 &= 0 & \beta\cdot \alpha' &=(\beta\cdot\alpha)+\beta &\displaystyle \beta\cdot \lambda &=\sup_{\xi<\lambda}(\beta\cdot\xi)\\ \beta^ 0 &= 0' & \beta^{ \alpha'} &=\beta^{\alpha}\cdot \beta &\displaystyle \beta^\lambda &=\sup_{\xi<\lambda}(\beta^\xi) \end{align}$$

However, addition and multiplication are in general not commutative.

We are interested in representing specific ordinals $\alpha$ as relations on $\bbN$. In essence Cantor defined the first ordinal representation system in 1897. Natural *ordinal representation system*s are frequently derived from structures of the form

$$\tag{2} {\frakA} = \langle\alpha,f_1,\ldots,f_n,<_{\alpha}\rangle $$

where $\alpha$ is an ordinal, $<_{\alpha}$ is the ordering of ordinals restricted to elements of $\alpha$ and the $f_i$ are functions

$$\tag{3} f_i:\underbrace{\alpha\times\cdots\times\alpha}_{k_i \textrm{ times}} \longrightarrow \alpha $$

for some natural number $k_i$.

$$ \bbA = \langle A,g_1,\ldots,g_n,\prec\rangle $$

is a *computable* (or *recursive*) *representation* of $\frakA$ if the following conditions hold:

1. $A\subseteq\bbN$ and *A* is a computable set.
2. $\prec$ is a computable total ordering on *A* and the functions $g_i$ are computable.
3. $\frakA \cong\bbA$, i.e., the two structures are isomorphic.

Theorem 3.3 (Cantor 1897)[^cantor-1897] For every ordinal $\beta>0$ there exist unique ordinals $\beta_0\geq\beta_1\geq\dots\geq\beta_n$ such that

$$\tag{4}\label{epsilon} \beta = \omega^{\beta_0}+\ldots+\omega^{\beta_n}.$$

The representation of $\beta$ in (4) is called its *Cantor normal form*. We shall write $\beta \mathbin{=_{\sCNF}} \omega^{\beta_1}+\cdots +\omega^{\beta_n}$ to convey that $\beta_0\geq\beta_1\geq\dots\geq\beta_k$.

The rather famous ordinal that emerged in Gentzen’s consistency proof of **PA** is denoted by $\varepsilon_0$. It refers to first ordinal $\alpha>0$ such that $(\forall \beta<\alpha)\,\omega^{\beta}<\alpha$. $\varepsilon_0$ can also be described as the least ordinal $\alpha$ such that $\omega^{\alpha}=\alpha$.

Ordinals $\beta<\varepsilon_0$ have a Cantor normal form with exponents $\beta_i<\beta$ and these exponents have Cantor normal forms with yet again smaller exponents. As this process must terminate, ordinals $<\varepsilon_0$ can be coded by natural numbers. For instance a coding function

$${\Corner{\mathord{\,.\,}}}:\varepsilon_0\longrightarrow \bbN$$

could be defined as follows:

$${\Corner{\alpha}} = \left\{\begin{array}{ll} 0 & \textrm{if } \alpha=0\\ \langle{\Corner{\alpha_1}},\ldots,{\Corner{\alpha_n}}\rangle & \textrm{if } \alpha \mathbin{=_{\sCNF}} \omega^{\alpha_1}+\cdots+\omega^{\alpha_n} \end{array}\right.$$

where $\langle k_1,\cdots,k_n\rangle\coloneqq 2^{k_1+1}\cdot\ldots\cdot p_n^{k_n+1}$ with $p_i$ being the *i*th prime number (or any other coding of tuples). Further define:

$$\begin{align} A_0 &{} \coloneqq \textrm{range of }\ {\Corner{\mathord{.} }} \\ {\Corner{\alpha}}\prec{\Corner{\beta}} &{} \mathbin{:\Leftrightarrow} \alpha<\beta \\ {\Corner{\alpha}} \mathop{\hat{+}} {\Corner{\beta}} &{} \coloneqq {\Corner{\alpha+\beta}} \\ {\Corner{\alpha}} \mathop{\hat{\cdot}} {\Corner{\beta}} &{} \coloneqq {\Corner{\alpha\cdot\beta}} \\ \hat{\omega}^{{\Corner{\alpha}}} &{} \coloneqq {\Corner{\omega^{\alpha}}}.\\ \end{align}$$

Then, using arrow notation $x\mapsto f(x)$ for functions $f$,

$$ {\langle\varepsilon_0,+,\cdot,\delta\mapsto \omega^{\delta},<\rangle} \cong {\langle A_0,\hat{+},\hat{\cdot},x\mapsto\hat{\omega}^{x},\prec\rangle} .$$

$A_0,\hat{+},\hat{\cdot},x\mapsto\hat{\omega}^{x},\prec$ are primitive recursive. Finally, we can spell out the scheme PR-TI$(\varepsilon_0)$ in the language of **PA**:

$$ \forall x\, {\left[\forall y\, \left({y\prec x} \to {P(y)}\right) \to {P(x)}\right]} \to {\forall x\, {P(x)}} $$

for all primitive recursive predicates *P*.

Given a natural ordinal representation system $\langle A,\prec,\ldots\rangle$ of order type $\tau$ let $\PRA+\rTI_{\qf}(<\tau)$ be **PRA** augmented by quantifier-free induction over all initial (externally indexed) segments of $\prec$. This is perhaps best explained via the representation system for $\varepsilon_0$ given above. There one can take the initial segments of $\prec$ to be determined by the Gödel numbers of the ordinals $\omega_0\coloneqq 1$ and $\omega_{n+1}\coloneqq \omega^{\omega_n}$ whose limit is $\varepsilon_0$.

Definition 3.4 We say that a theory *T* has *proof-theoretic ordinal* $\tau$, written $\lvert T\rvert =\tau$, if *T* can be proof-theoretically reduced to $\PRA+\rTI_{\qf}(<\tau)$, i.e.,

$$ T \mathbin{\equiv_{\Pi^0_2}} \PRA+\rTI_{\qf}(<\tau). $$

Unsurprisingly, the above notion has certain intensional aspects and hinges on the naturality of the representation system (for a discussion see Rathjen 1999a: section 2.)[^rathjen-1999a].

### 3.2 Infinite Proofs

Gentzen’s consistency proof for **PA** employs a reduction procedure $\cR$ on proofs *P* of the empty sequent together with an assignment *ord* of representations for ordinals to proofs such that $\ord(\cR(P))< \ord(P)$. Here $<$ denotes the ordering on ordinal representations induced by the ordering of the pertinent ordinals. For this purpose he needed representations for ordinals $<\varepsilon_0$ where $\varepsilon_0$ is the smallest ordinal $\tau$ such that whenever $\alpha<\tau$ then also $\omega^{\alpha}<\tau$ with $\alpha\mapsto \omega^{\alpha}$ being the function of ordinal exponentiation with base $\omega$. Moreover, the functions $\cR$ and *ord* and the relation $<$ are computable (when viewed as acting on codes for the syntactic objects), they can be chosen to be primitive recursive. With $g(n)= \ord(\cR^n(P))$, the *n*-fold iteration of $\cR$ applied to *P*, one has $g(0)>g(1)> g(2)> \ldots > g(n)$ for all *n*, which is absurd as the ordinals $<\varepsilon_0$ are well-founded. Hence **PA** is consistent.

Gentzen’s proof, though elementary, was very intricate and thus more transparent proofs were sought. As it turned out, the obstacles to cut elimination, inherent to **PA**, could be overcome by moving to a richer proof system, albeit in a drastic way by going *infinite*. This richer system allows for proof rules with infinitely many premises.[^note-15] The inference commonly known as the $\omega$-*rule* consists of the two types of *infinitary inferences*:

$$ \begin{align} \frac{\Gamma \Rightarrow {\Delta, F(0)};\; \Gamma \Rightarrow {\Delta,F(1)};\; \ldots; \Gamma \Rightarrow {\Delta,F(n)};\; \ldots} {\Gamma \Rightarrow {\Delta,\forall x\,F(x)}} \tag*{\(\omega R\)} \\[1ex] \frac{{F(0),\Gamma} \Rightarrow {\Delta};\; {F(1), \Gamma} \Rightarrow {\Delta};\; \ldots; {F(n),\Gamma} \Rightarrow {\Delta}; \ldots} {\exists x\,F(x), {\Gamma \Rightarrow \Delta} } \tag*{\(\omega L\)} \end{align}$$

The price to pay will be that deductions become infinite objects, i.e., *infinite well-founded trees*.

The sequent-style version of Peano arithmetic with the $\omega$-*rule* will be denoted by $\PA_{\omega}$. $\PA_{\omega}$ has no use for free variables. Thus free variables are discarded and all *terms* will be closed. All formulae of this system are therefore closed, too. The *numerals* are the terms $\bar{n}$, where $\bar{0}=0$ and $\overline{n+1}=S\bar{n}$. We shall identify $\bar{n}$ with the natural number *n*. All terms *t* of $\PA_{\omega}$ evaluate to a numeral $\bar{n}$.

$\PA_{\omega}$ has all the inference rules of the sequent calculus except for $\forall R$ and $\exists L$. In their stead, $\PA_{\omega}$ has the $\omega R$ and $\omega L$ inferences. The *Axioms* of $\PA_{\omega}$ are the following: (i) $\emptyset\Rightarrow A$ if *A* is a *true* atomic sentence; (ii) $B\Rightarrow \emptyset$ if *B* is a *false* atomic sentence; (iii) $F(s_1,\ldots,s_n)\Rightarrow F(t_1,\ldots,t_n)$ if $F(s_1,\ldots,s_n)$ is an atomic sentence and the $s_i$ and $t_i$ evaluate to the same numerals, respectively.

With the aid of the $\omega$-rule, each instance of the induction scheme becomes logically deducible with an infinite proof tree. To describe the cost of cut elimination for $\PA_{\omega}$, we introduce the measures of *height* and *cut rank* of a $\PA_{\omega}$ deduction $\cD$. We will notate this by

$$\cD \stile{\alpha}{k} \Gamma \Rightarrow \Delta.$$

The above relation is defined inductively following the buildup of the deduction $\cD$. For the *cut rank* we need the definition of the *length* $\lvert A\rvert$ of a formula:

$$ \begin{align} \lvert A\rvert & =0 \textrm{ if } A \textrm{ is atomic; }\\ \lvert \neg A_0\rvert & =\lvert A_0\rvert +1; \\ \lvert A_0\mathbin{\Box} A_1\rvert & =\max(\lvert A_0,A_1\rvert)+1 \end{align} $$

where $\Box=\land,\lor,\to$; $\lvert \exists x\,F(x)\rvert =\lvert \forall x\,F(x)\rvert =\lvert F(0)\rvert +1$.

Now suppose the last inference *I* of $\cD$ is of the form

$$ \frac{ \begin{array}{c} \cD_0\\ {\Gamma_0\Rightarrow \Delta_0} \end{array} \ \ldots\ \begin{array}{c} \cD_n\\ {\Gamma_n\Rightarrow \Delta_n} \end{array} \ \ldots\ n<\tau } {\Gamma\Rightarrow \Delta} I $$

where $\tau=1,2,\omega$ and the $\cD_n$ are the immediate subdeductions of $\cD$. If

$${\cD_n \stile{\alpha_n}{k} \Gamma_n} \Rightarrow \Delta_n$$

and $\alpha_n<\alpha$ for all $n<\tau$ then

$${\cD \stile{\alpha}{k} \Gamma} \Rightarrow \Delta$$

providing that in the case of *I* being a *cut* with cut formula *A* we also have $\lvert A\rvert <k$. We will write ${\PA_{\omega} \stile{\alpha}{k} \Gamma} \Rightarrow \Delta$ to convey that there exists a $\PA_{\omega}$-deduction ${\cD\stile{\alpha}{k} \Gamma}\Rightarrow \Delta$. The ordinal analysis of **PA** proceeds by first unfolding any **PA**-deduction into a $\PA_{\omega}$-deduction:

$$\tag{5}\label{einbett} \textrm{If } {\PA \vdash \Gamma}\Rightarrow \Delta \textrm{ then } {\PA_{\omega} \stile{\omega+m}{k} \Gamma} \Rightarrow \Delta $$

for some $m,k<\omega$. The next step is to get rid of the cuts. It turns out that the cost of lowering the cut rank from $k+1$ to *k* is an exponential with base $\omega$.

Theorem 3.5 (Cut Elimination for $\PA_{\omega}$) If ${\PA_{\omega} \stile{\alpha}{k+1} \Gamma} \Rightarrow \Delta$, then

$$ {\PA_{\omega} \stile{\omega^{\alpha}}{k} \Gamma} \Rightarrow \Delta. $$

As a result, if ${\PA_{\omega} \stile{\alpha}{n} \Gamma}\Rightarrow \Delta$, we may apply the previous theorem *n* times to arrive at a cut-free deduction ${\PA_{\omega} \stile{\rho}{0} \Gamma} \Rightarrow \Delta$ with $\rho=\omega^{\omega^{\iddots^{\omega^{\alpha}}}}$, where the stack has height *n*. Combining this with the result from $(\ref{einbett})$, it follows that every sequent $\Gamma\Rightarrow \Delta$ deducible in **PA** has a cut-free deduction in $\PA_{\omega}$ of length $<\varepsilon_0$. Ruminating on the details of how this result was achieved yields a consistency proof for **PA** from transfinite induction up to $\varepsilon_0$ for elementary decidable predicates on the basis of finitist reasoning (as described below).

Gentzen did not deal explicitly with infinite proof trees in his second published proof of the consistency of **PA** (Gentzen 1938b)[^gentzen-1938b]. However, in the unpublished first consistency proof of Gentzen 1974 he aims at showing that a proof of a sequent in first-order arithmetic gives rise to a a well-founded reduction tree; that tree can be identified with a cut-free proof in the sequent calculus with the $\omega$-rule. The infinitary version of **PA** with the $\omega$-rule was investigated by Schütte (1950). There remained the puzzle, how Gentzen’s work that used an ingenious method of assigning ordinals to purported proofs of the empty sequent relates to the infinitary approach. Much later work by Buchholz (1997) and others revealed an intrinsic connection between Gentzen’s assignment of ordinals to deductions in **PA** and the standard one to infinite deductions in $\PA_{\omega}$. In the 1950s infinitary proof theory flourished in the hands of Schütte. He extended his approach to **PA** to systems of ramified analysis to be discussed below in section 5.2.

One last remark about the use of ordinals: Gentzen showed that transfinite induction up to the ordinal $\varepsilon_0$ suffices to prove the consistency of **PA**. Using the arithmetized formalization of the proof predicate (see above, after Definition 1.3) and taking *k* as the numeral denoting the Gödel number of the formula $0=1$, we can express the consistency of **PA**, $\Con (\PA)$, by the formula $\forall x \,\neg\proof_{\PA}(x,k)$. To appreciate Gentzen’s result it is pivotal to note that he applied transfinite induction up to $\varepsilon_0$ only for primitive recursive predicates (the latter principle was denoted above by PR-TI$(\varepsilon_0)$). Otherwise, Gentzen’s proof used only finistist means. Hence, a more accurate formulation of Gentzen’s result is

$$\tag{6}\label{picture} \bF+\textrm{PR-TI}(\varepsilon_0) \vdash \Con (\PA),$$

where F, as above, contains only finitistically acceptable means. In his 1943 paper Gentzen also showed that this result is best possible, as **PA** proves transfinite induction up to any $\alpha<\varepsilon_0$. So one might argue that the non-finitist part of **PA** is encapsulated in PR-TI$(\varepsilon_0)$ and therefore “measured” by $\varepsilon_0$. $\varepsilon_0$ is also the proof-theoretic ordinal of **PA** as specified in Definition 3.4. Gentzen hoped that results of this character could also be obtained for stronger mathematical theories, in particular for analysis. Hilbert’s famous second problem asked for a direct consistency proof of that mathematical theory. Gentzen wrote in 1938 that

> the most important [consistency] proof of all in practice, that for *analysis*, is still outstanding. (1938a [Gentzen 1969: 236])[^gentzen-1969].

He actually worked on a consistency proof for analysis as letters (e.g. one to Bernays on 23.6.1935 translated in von Plato 2017: 240)[^bernays-1935][^plato-2017] and stenographic notes from 1945 (e.g., Gentzen 1945)[^gentzen-1945] show. Formally, “analysis” was identified already in Hilbert 1917/18 as a form of second order number theory $\bZ_2$. Hilbert and Bernays developed mathematical analysis in their $\bZ_2$ and to a much larger extent in a supplement of the second volume of “Grundlagen der Mathematik”. We take $\bZ_2$ as given in the following way. Its language extends that of **PA** by an additional sort of variables $X,Y,Z,\ldots$ that range over sets of numbers and the binary membership relation $t\in X$. Its axioms are those of **PA**, but the principle of proof by induction is formulated as the *second order induction axiom*

$$\forall X(0\in X\land\forall x(x\in X\rightarrow S(x)\in X) \rightarrow \forall x(x\in X)).$$

Finally, the axiom schema of *comprehension*, **CA**, asserts that for every formula ${F}(u)$ of the language of $\bZ_2$, there is a set $X=\{u\mid {F}(u)\}$ having exactly those numbers *u* as members that satisfy ${F}(u)$. More formally,

$$\label{CA}\tag{\(\bCA\)} \exists X\forall u(u\in X\leftrightarrow{F}(u)) $$

for all formulae ${F}(u)$ in which *X* does not occur. That $\bZ_2$ is often called “analysis” is due to the realization that, via the coding of real numbers and continuous functions as sets of natural numbers, a good theory of the continuum can be developed from these axioms.

Modern analyses of “finitist mathematics” consider it as situated between **PRA** and **PA**. When arguing that Gödel’s second incompleteness theorem refutes Hilbert’s finitist program, von Neumann argued that finitist mathematics is included in **PA** and, if not there, undoubtedly in $\bZ_2$. So it is quite clear that a consistency proof of $\bZ_2$ would use non-finitist principles or that the pursuit of the consistency program would require an extension of the finitist standpoint. In the next section we discuss briefly a variety of extensions and elaborate two in greater detail.

## 4. Hilbert’s Program, Extended

According to Bernays, the reductive result due to Gödel and Gentzen, Theorem 1.2, has a dramatic impact on the work concerned with Hilbert’s program. It opened in a very concrete and precise way the finitist perspective to a broader “constructive” one. Hilbert himself had taken such a step in a much vaguer way in his last paper (Hilbert 1931b)[^hilbert-1931b]. Theorem 1.2 showed, after all, that **PA** is contained in **HA** via the negative translation. Since **HA** comprises just a fragment of Brouwer’s intuitionism, the consistency of **PA** is secured on the basis of the intuitionist standpoint. In a letter to Heyting of 25 February 1933, Gentzen suggested investigating the consistency of **HA** since a consistency proof for classical arithmetic had not been given so far by finitist means. He then continued

> If on the other hand, one admits the intuitionistic position as a secure basis in itself, i.e., as a consistent one, the consistency of classical arithmetic is secured by my result. If one wished to satisfy Hilbert’s requirements, the task would still remain of showing intuitionistic arithmetic consistent. This, however, is not possible by even the formal apparatus of classical arithmetic, on the basis of Gödel’s result in combination with my proof. Even so, I am inclined to believe that a consistency proof for intuitionistic arithmetic, from an even more evident position, is possible and desirable. (quoted and translated in von Plato 2009: 672)[^plato-2009]

Gödel took a very similar position in December of 1933 (Gödel 1995: 53)[^gödel-1995]. There he broadened the idea of a revised version of Hilbert’s program allowing constructive means that go beyond the finitist ones without accepting fully fledged intuitionism; the latter he considered to be problematic, in particular on account of the impredicative nature of intuitionist implication. As to an extension of Hilbert’s position he wrote:

> But there remains the hope that in future one may find other and more satisfactory methods of construction beyond the limits of the system A [capturing finitist methods], which may enable us to found classical arithmetic and analysis upon them. This question promises to be a fruitful field for further investigations.

In section 3.2 we described Gentzen’s considerations; in section 4.2 we discuss Gödel’s as developed in the late 1930s. In section 4.1 we *sketch* some other constructive positions.

### 4.1 Constructive Frameworks

A particularly appealing idea is to pursue Hilbert’s program relative to a constructive point of view and determine which parts of classical mathematics are demonstrably consistent relative to that standpoint (see Rathjen 2009 for pursuing this with regard to Martin-Löf type theory)[^rathjen-2009]. As one would suspect, there are differing “schools” of constructivism and different layers of constructivism. Several frameworks for developing mathematics from such a point of view have been proposed. Some we will refer to in this article (arguably the most important) are:

1. Arithmetical Predicativism.
2. Theories of higher type functionals.
3. Takeuti’s “Hilbert-Gentzen finitist standpoint”.
4. Feferman’s explicit mathematics.
5. Martin-Löf’s intuitionistic type theory.
6. Constructive set theory (Myhill, Friedman, Beeson, Aczel).

At this point we will just give a very rough description of these foundational views. A few more details, especially about their scope on a standard scale of theories and proof-theoretic ordinals, will be provided at the very end of section 5.3.

(a) Arithmetical Predicativism originated in the writings of Poincaré and Russell in response to the set-theoretic paradoxes. It is characterized by a ban of impredicative definitions. Whilst it accepts the completed infinite set of naturals numbers, all other sets are required to be constructed out of them via an autonomous process of arithmetical definitions. A first systematic attempt at developing mathematics predicatively was made in Weyl’s 1918 monograph *Das Kontinuum* (Weyl 1918)[^weyl-1918].

(b) Theories of higher type functionals comprise Gödel’s *T* and Spector’s extension of *T* via functionals defined by bar recursion. The basic idea goes back to Gödel’s 1938 lecture at Zilsel’s (Gödel 1995: 94)[^gödel-1995]. It was inspired by Hilbert’s 1926 *Über das Unendliche*, which considered a hierarchy of functionals over the natural numbers, not only of finite but also of transfinite type.

(c) To understand Takeuti’s finitist standpoint it is important to pinpoint the place where in a consistency proof à la Gentzen the means of **PRA** are exceeded. Gentzen’s proof employs a concrete ordering $\prec$ of type $\varepsilon_0$, it uses an assignment of ordinals to proofs and provides a reduction procedure on proofs such that any alleged proof of an inconsistency is reduced to another proof of an inconsistency which gets assigned a smaller element of the ordering. The ordering, the ordinal assignment and the reduction procedure are actually primitive recursive and the steps described so far can be carried out in a small fragment of **PRA**. The additional principle needed to infer the consistency of **PA** is the following:

- (*)There are no infinite elementary recursive sequences $\alpha_0,\alpha_1,\alpha_2,\ldots$ such that $\alpha_{n+1}\prec \alpha_n$ holds for all *n*.

Takeuti refers to (*) as the accessibility of $\prec$. Note that this is a weaker property than the well-foundedness of $\prec$ which refers to arbitrary sequences. There is nothing special about the case of **PA** since any ordinal analysis of a theory *T* in the literature can be made to fit this format. Thus epistemologically (*) is the fulcrum in any such consistency proof. Takeuti’s central idea (1987, 1975) was that we can carry out *Gedankenexperimente* (thought experiments) on concretely given (elementary) sequences to arrive at the insight that (*) obtains.[^note-16]

(d) Errett Bishop’s novel (informal) approach to constructive analysis (1967) made a great impression on mathematicians with constructive leanings. In it, he dealt with different kinds of mathematical objects (numbers, functions, sets) as if they were given by explicit presentations, each kind being equipped with its own germane “equality” relation conceived in such a way that operations on them would lead from representations to representations respecting the equality relation. An important ingredient that made Bishop’s constructivism workable is the systematic use of witnessing data as an integral part of what constitutes a mathematical object. For instance, a real number comes with a modulus of convergence while a function of real numbers comes equipped with a modulus of (uniform) convergence. In his *explicit mathematics*, Feferman (1975, 1979) aims (among other things) at formalizing the core of Bishop’s ontology. Explicit mathematics is a theory that describes a realm of concretely and explicitly given objects (a universe *U* of symbols) equipped with an operation $\bullet$ of application in such a way that given two objects $a,b\in U$, *a* may be viewed as a program which can be run on input *b* and may produce an output $a\bullet b\in U$ or never halt (such structures are known as partial combinatory algebras or Schönfinkel algebras). Moreover, some of the objects of *U* represent sets of elements of *U*. The construction of new sets out of given sets is either done explicitly by elementary comprehension or by a process of inductive generation. If one also adds principles to the effect that every internal operation (given as $\lambda x.a\bullet x$ for some $a\in U$) which is monotone on sets possesses a least fixed point one arrives at a remarkably strong theory (cf. Rathjen 1998, 1999b, 2002)[^rathjen-1998].

(e) Martin-Löf type theory is an intuitionist theory of dependent types intended to be a full scale system for formalizing constructive mathematics. Its origins can be traced to *Principia Mathematica*, Hilbert’s *Über das Unendliche*, the natural deduction systems of Gentzen, taken in conjunction with Prawitz’s reduction procedures, and to Gödel’s Dialectica system. It incorporates inductively defined data types that, together with the vehicle of internal reflection via universes, endow it with considerable consistency strength.

(f) Constructive set theory (as do the theories under (d) and (e)) sets out to develop a framework for the style of constructive mathematics of Bishop’s 1967 *Foundations of constructive analysis* in which he carried out a development of constructive analysis, based on informal notions of constructive function and set, which went substantially further mathematically than anything done before by constructivists. Where Brouwer reveled in differences, Bishop stressed the commonalities with classical mathematics. What was novel about his work was that it could be read as a piece of classical mathematics as well.

The ‘manifesto’ of constructive set theory was most vividly expressed by Myhill:

> … the argumentation of [Bishop 1967][^bishop-1967] looks very smooth and seems to follow directly from a certain conception of what sets, functions, etc. are, and we wish to discover a formalism which isolates the principles underlying this conception in the same way that Zermelo-Fraenkel set-theory isolates the principles underlying classical (nonconstructive) mathematics. We want these principles to be such as to make the process of formalization completely trivial, as it is in the classical case. (Myhill 1975: 347)[^myhill-1975]

Despite first appearances, there are close connections between the approaches of (d)–(f). Constructive set theory can be interpreted in Martin-Löf type theory (due to Aczel 1978)[^aczel-1978] and explicit mathematics can be interpreted in constructive set theory (see Griffor & Rathjen 1994, Theorem 3.9)[^griffor-1994]. Perhaps the closest fit between (e) and (f), giving back and forth interpretations, is provided by Rathjen & Tupailo 2006. Some concrete mathematical results are found at the end of section 5.3.

### 4.2 The Dialectica Interpretation: Gödel and Spector

Among the proposals for extending finitist methods put forward in his 1938 lecture at Zilsel’s, Gödel appears to have favored the route via higher type functions. Details of what came to be known as the Dialectica interpretation were not published until 1958 (Gödel 1958)[^gödel-1958] but the D-interpretation itself was arrived at by 1941. Gödel’s system ${T}$ axiomatizes a class of functions that he called the *primitive recursive functionals of finite type*. ${T}$ is a largely equational theory whose axioms are equations involving terms for higher type functionals with just a layer of propositional logic on top of that. In this way the quantifiers, problematic for finists and irksome to intuitionists, are avoided. To explain the benefits of the D-interpretation we need to have a closer look at the syntax of ${T}$ and its principles.

Definition 4.1 ${T}$ has a many-sorted language in that each terms is assigned a type. Type (symbols) are generated from 0 by the rule: If $\sigma$ and $\tau$ are types then so is $\sigma\to\tau$. Intuitively the ground type 0 is the type of natural numbers. If $\sigma$ and $\tau$ are types that are already understood then $\sigma\to\tau$ is a type whose objects are considered to be functions from objects of type $\sigma$ to objects of type $\tau$. In addition to variables $x^{\tau},y^{\tau},z^{\tau},\ldots$ for each type $\tau$, the language of ${T}$ has special constants 0, $\rsuc$, $\rK_{\sigma,\tau}$, $\rS_{\rho,\sigma,\tau}$, and $\rR_{\sigma}$ for all types $\rho,\sigma,\tau$. The meaning of these constants is explained by their defining equations. $\rK_{\sigma,\tau}$ and $\rS_{\rho,\sigma,\tau}$ are familiar from combinatory logic which was introduced by Schönfinkel in 1924 and became more widely known through Curry’s work (1930). 0 plays the role of the first natural number while $\rsuc$ embodies the successor function on objects of type 0. The constants $\rR_{\sigma}$, called *recursors*, provide the main vehicle for defining functionals by recursion on $\bbN$. Term formation starts with constants and variables, and if *s* and *t* are terms of type $\sigma\to\tau$ and $\sigma$, respectively, then $s(t)$ is a term of type $\tau$. To increase readability we shall write $t(r,s)$ instead of $(t(r))(s)$ and $t(r,s,q)$ instead of $(t(r,s))(q)$ etc. Also $\rsuc(t)$ will be shortened to $t'$. The defining axioms for the constants are the following:[^note-17]

1. $\neg t'=0$
2. $t'=r'\to t=r$
3. $\rK_{\sigma,\tau}(s,t)=s$
4. ${\rS}_{\rho,\sigma,\tau}(r,s,t)= (r(t))(s(t))$
5. $\rR_{\sigma}(f,g,0) = f$
6. $\rR_{\sigma}(f,g,n')= g(n,\rR_{\sigma}(f,g,n)).$

The axioms of ${T}$ consist of the above defining axioms, equality axioms and axioms for propositional logic. Inference rules are modus ponens and the induction rule

$$ \textrm{from } A(0) \textrm{ and } A(x) \to A(x') \textrm{ conclude }A(t) $$

for *t* of type 0 and *x* not in $A(0)$.

The first step towards the D-interpretation of Heyting arithmetic in ${T}$ consists of associating to each formula *A* of arithmetic a syntactic translation $A^D$ which is of the form

$$\tag{7}\label{D-Form} A^D \equiv {\exists x^{\sigma_1} \ldots \exists x^{\sigma_n} \forall y^{\tau_1} \ldots \forall y^{\tau_m} A_D(\vec{x},\vec{y})} $$

with $A_D(\vec{x},\vec{y})$ being quantifier free. Thus $A^D$ is not a formula of ${T}$ but of its augmentation via quantifiers $\forall x^{\tau}$ and $\exists y^{\tau}$ for all types $\tau$. The translation proceeds by induction on the buildup of *A*. The cases where the outermost logical symbol of *A* is among $\land$, $\lor$, $\exists x$, $\forall x$ are rather straightforward. The crucial case occurs when *A* is an implication $B\to C$. To increase readability we shall suppress the typing of variables. Let $B^D\equiv \exists \vec{x}\, \forall \vec{y}\, B_D(\vec{x},\vec{y})$ and $C^D\equiv {\exists \vec{u}\, \forall \vec{v}\, C_D(\vec{u},\vec{v})}$. Then one uses a series of judicious equivalences to bring the quantifiers in $B^D\to C^D$ to the front and finally employs skolemization of existential variables as follows:

$$\begin{align} \tag{i} \exists \vec{x}\,\forall \vec{y} B_D(\vec{x},\vec{y})&\to \exists \vec{u}\,\forall \vec{v} C_D(\vec{u},\vec{v})\\ \tag{ii} \forall \vec{x}[\,\forall \vec{y} B_D(\vec{x},\vec{y})&\to \exists \vec{u}\,\forall \vec{v} C_D(\vec{u},\vec{v})]\\ \tag{iii} \forall \vec{x}\,\exists\vec{u}[\,\forall \vec{y} B_D(\vec{x},\vec{y})&\to \forall \vec{v} C_D(\vec{u},\vec{v})]\\ \tag{iv} \forall \vec{x}\,\exists\vec{u}\,\forall \vec{v}[\,\forall \vec{y} B_D(\vec{x},\vec{y})&\to C_D(\vec{u},\vec{v})]\\ \tag{v} \forall \vec{x}\,\exists\vec{u}\,\forall \vec{v}\,\exists \vec{y}[B_D(\vec{x},\vec{y})&\to C_D(\vec{u},\vec{v})]\\ \tag{vi} \forall \vec{x}\,\exists\vec{u}\,\exists Y\,\forall \vec{v}[B_D(\vec{x},Y(\vec{v}))&\to C_D(\vec{u},\vec{v})]\\ \tag{vii}\exists U\,\exists Z\,\forall \vec{x}\,\forall \vec{v}[B_D(\vec{x},Z(\vec{x},\vec{v}))&\to C_D(U(\vec{x}),\vec{v})]. \end{align}$$

$A^D$ is then defined to be the formula in (vii). Note, however, that these equivalences are not necessarily justified constructively. Only (i) $\Leftrightarrow$ (ii) and (iii) $\Leftrightarrow$ (iv) hold constructively whereas (v) $\Leftrightarrow$ (vi) and (vi) $\Leftrightarrow$ (vii) are justified constructively only if one also accepts the axiom of choice for all finite types (AC^{*ft*}). Equivalences (ii) $\Leftrightarrow$ (iii) and (iv) $\Leftrightarrow$ (v) use a certain amount of classical logic known as the *principle of independence of premise* (IP^{*ft*}) and *Markov’s principle* (MP^{*ft*}) for all finite types, respectively. At this point $A\mapsto A^D$ is just a syntactic translation. But amazingly it gives rise to a meaningful interpretation of **HA** in *T*.

Theorem 4.2 (Gödel 1958)[^gödel-1958] Suppose $\cD$ is a proof of *A* in **HA** and $A^D$ as in $(\ref{D-Form})$. Then one can effectively construct a sequence of terms $\vec t$ (from $\cD$) such that ${T}$ proves $A_D(\vec t,\vec y\,)$.

If one combines the *D*-interpretation with the Kolmogorov-Gentzen-Gödel negative translation of **PA** into **HA** one also arrives at an interpretation of **PA** in ${T}$. Some interesting consequences of the latter are that the consistency of **PA** follows finitistically from the consistency of ${T}$ and that every total recursive function of **PA** is denoted by a term of ${T}$.

The three principles AC^{*ft*}, IP^{*ft*} and MP^{*ft*} which figured in the *D*-translation actually characterize the *D*-translation in the sense that over the quantifier extension of ${T}$ with intuitionistic logic, called $\bHA^{\omega}$, they are equivalent to the schema

$$ C\leftrightarrow C^D $$

for all formulae *C* of that theory. Principles similar to the three above are also often validated in another type of computational interpretation of intuitionistic theories known as *realizability*. Thus, it appears that they are intrinsically related to computational interpretations of such theories.

A further pleasing aspect of Gödel’s interpretation is that it can be extended to stronger systems such as higher order systems and even to set theory (Burr 2000, Diller 2008)[^burr-2000][^diller-2008]. Moreover, it sometimes allows one to extract computational information even from proofs of specific classical theorems (see, e.g., Kohlenbach 2007)[^kohlenbach-2007]. It behaves nicely with respect to modus ponens and thus works well for ordinary proofs that are usually structured via a series of lemmata. This is in contrast to cut elimination which often requires a computationally costly transformation of proofs.

Spector (1962) extended Gödel’s functional interpretation, engineering an interpretation of $\bZ_2$ into *T* augmented via a scheme of transfinite recursion on higher type orderings. This type of recursion, called *bar recursion*, is conceptually related to Brouwer’s bar induction principle. (For a definition of bar induction and a presentation of Spector’s result see [Appendix C](proof-theory.appendix-c.md).)

## 5. Beyond Arithmetic: Subsystems of $\bZ_2$

We described the system $\bZ_2$ of second order arithmetic already at the end of section 3.2. It was viewed as the “next”system to be proved consistent—after first-order arithmetic **PA** had been shown to be. As we mentioned $\bZ_2$ is also called “analysis”, because it allows the straightforward development of classical mathematical analysis after coding real numbers and continuous functions as sets of natural numbers. Indeed, Hermann Weyl showed in 1918 that a considerable portion of analysis can be developed in small fragments of $\bZ_2$ that are actually conservative over **PA**. The idea of singling out the minimal fragment of $\bZ_2$ required to expose a particular part of ordinary mathematics led in the 1980s to the research program of *reverse mathematics*. However, before discussing that program, we are going to describe proof-theoretic investigations of $\bZ_2$ and its subsystems that have been a focal point until the very early 1980s.

### 5.1 Takeuti’s Fundamental Conjecture

After Gentzen, it was Gaisi Takeuti who worked on a consistency proof for $\bZ_2$ in the late 1940s. He conjectured that Gentzen’s *Hauptsatz* not only holds for first order logic but also for higher order logic, also known as simple type theory, **STT**. This came to be known as Takeuti’s fundamental conjecture.[^note-18] The particular sequent calculus he introduced was called a generalized logic calculus, GLC (Takeuti 1953)[^takeuti-1953]. $\bZ_2$ can be viewed as a subtheory of GLC. In the setting of GLC the comprehension principle **CA** is encapsulated in the right introduction rule for the existential second-order quantifier and the left introduction rule for the universal second-order quantifier. In order to display these rules the following notation is convenient. If $F(U)$ and $A(a)$ are formulae then $F(\{v\mid A(v)\})$ arises from $F(U)$ by replacing all subformulae $t\in U$ of $F(U)$ (with *U* indicated) by $A(t)$. The rules for second order quantifiers can then be stated as follows:[^note-19]

$$\begin{array}{lcclc} (\forall_2\,\bL) & \displaystyle \frac {{ F(\{v\mid A(v)\}) },\Gamma\Rightarrow \Delta} {\forall X\,{F(X),\Gamma} \Rightarrow \Delta } & & (\forall_2\,\rR) & \displaystyle\frac {\Gamma\Rightarrow {\Delta, F(U)}} {\Gamma\Rightarrow \Delta, {\forall X\,F(X) }} \\[2ex] (\exists_2\,\bL) & \displaystyle \frac{F(U),\Gamma\Rightarrow \Delta} {{ \exists X\,F(X)},\Gamma\Rightarrow \Delta } & & (\exists_2\,\rR) & \displaystyle \frac{\Gamma\Rightarrow \Delta,F(\{ v\mid A(v)\})} {\Gamma\Rightarrow \Delta,{\exists X\,F(X) }} \end{array} $$

To deduce an instance $\exists X\,\forall x\,[x\in X \leftrightarrow A(x)]$ of **CA** just let $F(U)$ be the formula $\forall x\,[x\in U \leftrightarrow A(x)]$ and observe that

$$F(\{v\mid A(v)\})\equiv \forall x\,[A(x)\leftrightarrow A(x)], $$

and hence

$$ \begin{gather} \vdots \\ \displaystyle \frac{\Gamma\Rightarrow \Delta, \forall x\,[A(x)\leftrightarrow A(x)]} {\Gamma\Rightarrow \Delta, \exists X\,\forall x\,[x\in X \leftrightarrow A(x)]} \tag{\(\exists_2\,\rR\)} \end{gather} $$

As the deducibility of the empty sequent is ruled out if cut elimination holds for GLC (or just the fragment GLC₂ corresponding to $\bZ_2$), Takeuti’s Fundamental Conjecture entails the consistency of $\bZ_2$. However, note that it does not yield the subformula property as in the first-order case. After all, the minor formula $F(\{x\mid A(x)\})$ in $(\exists_2\,\rR)$ and $(\forall_2\,\bL)$ may have a much higher (quantifier) complexity than the principal formula $\exists XF(X)$ and $\forall XF(X)$, respectively. Indeed, $\exists XF(X)$ may be a proper subformula of $A(x)$ which clearly exhibits the impredicative nature of these inferences and shows that they are strikingly different from those in predicative analysis, where the subformula property obtains.

In 1960a Schütte developed a semantic equivalent to the (syntactic) fundamental conjecture using partial or semi-valuations. He employed the method of search trees (or deduction chains) to show that a formula *F* that cannot be deduced in the cut-free system has a deduction chain without axioms which then gives rise to a partial valuation *V* assigning the value “false” to *F*. From the latter he inferred that the completeness of the cut-free system[^note-20] is equivalent to the semantic property that every partial valuation can be extended to a total valuation (basically a Henkin model of **STT**). In 1966 Tait succeeded in proving cut-elimination for second order logic using Schütte’s semantic equivalent for that fragment. Soon afterwards, Takahashi (1967) and Prawitz (1968) independently proved for full classical simple type that every partial valuation extends to a total one, thereby establishing Takeuti’s fundamental conjecture. These results, though, were somewhat disappointing as they were obtained by highly non-constructive methods that provided no concrete method for eliminating cuts in a derivation. In contrast, Girard showed in 1971 that simple type theory not only allows cut-elimination but that there is also a terminating normalization procedure.[^note-21] These are clearly very interesting results, but as far as instilling trust in the consistency of $\bZ_2$ or **SST** is concerned, the cut elimination or termination proofs are just circular since they blatantly use the very comprehension principles formalized in these theories (and a bit more). To quote Takeuti:

> My fundamental conjecture itself has been resolved in a sense by Motoo Takahashi and Dag Prawitz independently. However, their proofs rely on set theory, and so it cannot be regarded as an execution of Hilbert’s Program. (Takeuti 2003: 133)[^takeuti-2003]

Takeuti’s work on his conjecture instead focused on partial results. A major breakthrough that galvanized research in proof theory, especially ordinal-theoretic investigations, was made by him in 1967. In Takeuti 1967 he gave a consistency proof for $\Pi^1_1$-comprehension and thereby for the first time obtained an ordinal analysis of an impredicative theory. For this Takeuti vastly extended Gentzen’s method of assigning ordinals (ordinal diagrams, to be precise) to purported derivations of the empty sequent. It is worth quoting Takeuti’s own assessment of his achievements.

> … the subsystems for which I have been able to prove the fundamental conjecture are the system with $\Pi^1_1$ comprehension axiom and a slightly stronger system, that is, the one with $\Pi^1_1$ comprehension axiom together with inductive definitions.[…] I tried to resolve the fundamental conjecture for the system with the $\Delta^1_2$ comprehension axiom within our extended version of the finite standpoint. Ultimately, our success was limited to the system with provably $\Delta^1_2$ comprehension axiom. This was my last successful result in this area. (Takeuti 2003: 133)[^takeuti-2003]

The subsystems of $\bZ_2$ that are alluded to in the above discussion are now to be described. We consider the axiom schema of $\cC$-*comprehension* for formula classes $\cC$ which is given by

$$ \tag*{\(\cC\Hy\bCA\)} \Gamma\Rightarrow \exists X\forall u(u\in X\leftrightarrow{F}(u)) $$

for all formulae ${F}\in\cC$ in which *X* does not occur. Natural formula classes are the *arithmetical formulae*, consisting of all formulae without second order quantifiers $\forall X$ and $\exists X$, and the $\Pi^1_n$-*formulae*, where a $\Pi^1_n$-formula is a formula of the form $\forall X_1\ldots Q X_n\,A(X_1,\ldots,X_n)$ with $\forall X_1\ldots Q X_n$ being a string of *n* alternating set quantifiers, commencing with a universal one, followed by an arithmetical formula $A(X_1,\ldots,X_n)$. Note that in this notation the class of arithmetical formulae is denoted by $\Pi^1_0$.

Also “mixed” forms of comprehension are of interest, e.g.,

$$\tag*{\(\Delta^1_n{\Hy}\bCA\)} \Gamma\Rightarrow \forall u\,[F(u)\leftrightarrow G(u)] \to \exists X\,\forall u\,[u\in X \leftrightarrow F(u)] $$

where $F(u)$ is in $\Pi^1_n$ and $G(u)$ in $\Sigma^1_n$.

One also considers $\Delta^1_n$ comprehension rules:

$$ \frac{\emptyset \Rightarrow \forall u\,[F(u)\leftrightarrow G(u)]} {\Gamma\Rightarrow \exists X\,\forall u\,[u\in X \leftrightarrow F(u)]} \quad \quad\quad \begin{split} \textrm{if } & F(u)\in\Pi^1_n,\\ & G(u)\in\Sigma^1_n \end{split} \tag*{\(\Delta^1_n{\Hy}\bCR\)} $$

For each axiom scheme $\mathbf{Ax}$ we denote by $(\mathbf{Ax})_0$ the theory consisting of the basic arithmetical axioms plus the scheme $\mathbf{Ax}$. By contrast, $(\mathbf{Ax})$ stands for the theory $(\mathbf{Ax})_0$ augmented by the scheme of induction for all $\cL_2$-formulae. An example for these notations is the theory $(\bPi^1_1-\bCA)_0$ which has the comprehension schema for $\bPi^1_1$-formulae.

In **PA** one can define an elementary injective pairing function on numbers, e.g., $(n,m)\coloneqq 2^n\times3^m$. With the help of this function an infinite sequence of sets of natural numbers can be coded as a single set of natural numbers. The $n^{th}$ section of set of natural numbers *U* is defined by $U_n\,\coloneqq \,\{m:\,(n,m)\in U\}$. Using this coding, we can formulate a form of the axiom of choice for formulae ${F}$ in $\cC$ by

$$\tag*{\(\cC{\Hy}\bAC\)} \Gamma\Rightarrow \forall x\exists Y{F}(x,Y)\rightarrow\exists Y\forall x{F}(x,Y_x). $$

The basic relations between the above theories are discussed in Feferman and Sieg 1981a.

### 5.2 Predicative Theories

A major stumbling block for proving Takeuti’s fundamental conjecture is that in $(\forall_2\bL)$ and $(\exists_2\rR)$ inferences the minor formula $F(\{v\mid A(v)\})$ can have a much higher complexity than the principal (inferred) formula $QX\,F(X)$. If, instead, one allowed these inferences only in cases where the ‘abstraction’ term $\{v\mid A(v)\}$ had (in some sense) a lower complexity than $QX\,F(X)$, cut elimination could be restored. To implement this idea, one introduces a hierarchy of sets (formally represented by abstraction terms) whose complexity is stratified by ordinal levels $\alpha$, and a pertaining hierarchy of quantifiers $\forall X^{\beta}$ and $\exists X^{\beta}$ conceived to range over sets of levels $<\beta$. This is the basic idea underlying the ramified analytic hierarchy. The problem of which ordinals could be used for the transfinite iteration led to the concept of *autonomous progressions of theories*. The general idea of progressions of theories is very natural and we shall consider it first before discussing the autonomous versions.

#### 5.2.1 Progressions of theories: Completing the incomplete

As observed earlier, Hilbert attempted to overcome the incompleteness of first-order arithmetic by introducing as axioms $\Pi^0_1$-statements all of whose instances had been finitistically proved (Hilbert 1931a)[^hilbert-1931a]. In a way he modified the concept of a “formal” theory by invoking finitist provability. Bernays, in his letter to Gödel of January 18, 1931 (Gödel 2003: 86–88)[^gödel-2003], proposed a *rule* of a more general form. He indicated also that it would allow the elimination of the induction principle—in exchange for dealing with infinite proofs.

These considerations among others raised the issue of what constitutes a properly *formal* theory. Gödel paid very special attention to it when giving his Princeton Lectures in 1934. At the very end he introduced the general recursive functions. This class of number theoretic functions was shown to be co-extensional with Church’s λ-definable ones by Church and Kleene. In Church 1936 an “identification” of effective calculability and general recursiveness was proposed, what is usually called *Church’s thesis*. Turing, of course, proposed his machine computability for a very similar purpose and proved its equivalence to λ-definability in an appendix to his 1936. Church and Turing used their respective notion to establish the undecidability of first-order logic. For Gödel, this was the background for formulating the incompleteness theorems in “full generality” for all formal theories (containing a modicum of number or set theory); see the Postscriptum to the Princeton Lectures Gödel wrote in 1964:

> In consequence of later advances, in particular of the fact that, due to A.M. Turing’s work, a precise and unquestionably adequate definition of the general concept of formal system can now be given, the existence of undecidable arithmetical propositions and the non-demonstrability of the consistency of a system in the same system can now be proved rigorously for *every* consistent formal system containing a certain amount of finitary number theory. (Gödel 1986: 369)[^gödel-1986].

The first incompleteness is proved for any such theory T, by explicitly producing an unprovable yet true statement $G_\bT$. That formula can then be added to T making $\bT+G_\bT$ a “less incomplete” theory. Von Neumann had already established the equivalence of $G_\bT$ with the consistency statement for T, $\Con (\bT)$; the latter expresses that there is no proof in *T* of a blatantly false statement such as $0=1$. This gives then rise to an extension procedure leading from T to $\bT'$, namely (R1) $\bT'=\bT+G_\bT$.

Thus one might try to address the incompleteness of T by forming a sequence of theories $\bT=\bT_0\subset \bT_1\subset\bT_2\subset\ldots$ where $\bT_{i+1}=\bT_i'$ and to continue this into the transfinite. The latter can be achieved by letting $\bT_{\lambda}=\bigcup_{\alpha<\lambda}\bT_{\alpha}$ for limit ordinals λ and $\bT_{\alpha+1}=\bT_{\alpha}'$ for successor ordinals $\alpha+1$. However, the consistency statement for $\bT_{\lambda}$, thus the provability predicate for the theory, has to be expressed in the language of $\bT_{\lambda}$, and one cannot simply use set theoretic ordinals. Furthermore, the extensions of T are all supposed to be formal theories, i.e., the axioms have to be enumerable by recursive functions. To deal with both issues at once, one has to deal with ordinals in an effective way.

That is what Turing did in his Princeton dissertation (1939) concerning, what he called, *ordinal logics*. There he considers two ways of achieving the effective representation of ordinals. The first way is via the set $\rW$ of numbers *e* for recursive well-orderings $\leq_e$, the second is provided by the class of Church-Kleene notations for ordinals (Church and Kleene 1936)[^church-1936][^church-1936-2] that used expressions in the λ-calculus to describe ordinals. The latter approach was then modified in Kleene 1938 to an equivalent recursion-theoretic definition that uses numerical codes to denote countable ordinals and is known as Kleene’s ${\cO}$.

Definition 5.1 A *computable* or *recursive function* on the naturals is one that can be computed by a Turing machine. The program of a Turing machine *M* can be assigned a Gödel number ${\Corner{M}}$. For natural numbers $e,n$, to convey that the Turing machine with Gödel number *e* computes a number *m* on input *n*, we use the notation $\{e\}(n)$ for *m*.

Kleene uses ${\rsuc}(a)\coloneqq 2^a$ as notations for successor ordinals and and ${\rlim}(e)\coloneqq 3\cdot 5^e$ for limit ordinals.

The class ${\cO}$ of ordinal notations, the partial ordering relation $\relLTcO$ between such notations, and the ordinal ${\mid}{a}{\mid}$ denoted by $a\in {\cO}$ are defined simultaneously as follows:

1. $0\in{\cO}$, and ${\mid}{0}{\mid} =0$.
2. If $a\in{\cO}$ then ${\rsuc}(a)\in{\cO}$, $a \relLTcO {\rsuc}(a)$ and ${\lvert {\rsuc}(a)\rvert}={\lvert a\rvert}+1$.
3. If *e* is an index of a total recursive function and ${\{e\}(n)} \relLTcO{\{e\}(n+1)}$ holds for all $n\in{\bbN}$, then ${\rlim}(e)\in{\cO}$, and ${\lvert {\rlim}(e)\rvert}=\sup\{{\lvert {\{e\}(n)}\rvert}\mid n\in{\bbN}\}$.
4. If $a \relLTcO b$ and $b \relLTcO c$ then $a \relLTcO c$.

The first ordinal $\tau$ such that there is no recursive well-ordering of order type $\tau$ is usually denoted by $\omega^{CK}$ in honor of Church and Kleene. It can be shown for the above definition of ${\cO}$ that the recursive ordinals are exactly those that have a notation in ${\cO}$.

When it comes to theories T, quite unlike to other areas of logic (e.g., model theory), results as those presented in this section depend not only on the set of axioms of T, but also on the way they are presented. When talking about a theory T we assume that T is given by a $\Sigma^0_1$-formula $\psi(v_0)$ such that *F* is an axiom of T just in case $\psi({\Corner{F}})$ holds; a $\Sigma^0_1$-formula is of the form $\exists y_1\ldots\exists y_n\,R(y_1,\ldots y_n)$ with *R* primitive recursive. This consideration together with Kleene’s ${\cO}$ allows us to build a transfinite hierarchy of theories based on any suitable theory T. A *consistency progression* based on T is a primitive recursive function $n\mapsto \psi_n$ that associates with every natural number *n* a $\Sigma^0_1$-formula $\psi_n(v_0)$ that defines $\bT_n$ such that **PA** proves: (i) $\bT_0=\bT$; (ii) $\bT_{{\rsuc}(n)}=\bT_n'$, and (iii) $\bT_{{\rlim}(n)}=\bigcup_{x\in{\bbN}}\bT_{\{n\}(x)}$. So, finally we can formulate Turing’s completeness result.

Theorem 5.2 For any true $\Pi^0_1$ sentence *F* a number $a_{F}\in{\cO}$ can be constructed such that ${{\mid}\,{a_{F}}\,{\mid}}=\omega+1$ and $\bT_{a_{F}}\vdash F$. Moreover, the function $F\mapsto a_{F}$ is given by a primitive recursive function.

At first glance Turing’s theorem seems to provide some insight into the nature of true $\Pi^0_1$-statements. That this is an “illusion” is revealed by the analysis of its simple proof which is just based on the trick of coding the truth of *F* as a member of ${\cO}$. The proof also shows that the infinitely many iterated consistency axioms $\Con (\bT_0),\Con (\bT_1),\ldots$ of $\bT_{{{\rsuc}}({\rlim}(e))}$ are irrelevant for proving *F*. As it turns out, the reason why one has to go to stage $\omega+1$ is simply that only at stage $\omega$ a non-standard definition of the axioms of $\bigcup_{n<\omega}\bT_n$ can be introduced. More details and other results on recursive progressions are discussed in [Appendix B](proof-theory.appendix-b.md). Here let us just mention that one has considered other progressions based on various extension procedures $\bT \mapsto \bT'$ that strengthen a given theory, notably:[^note-22]

- (R2)$\bT'= \bT+\{\exists y\,\proof_\bT(y,{\Corner{F}})\to F\mid F$ closed$\}$.
- (R3)$\bT'= \bT+\{\forall x\,\exists y\, \proof_\bT(y,{\Corner{F(\bar{x})}})\to \forall x F(x)\mid \textrm{ all } F(x)$ with at most *x* free$\}$.

(R2) is called an extension by the *local reflection principle*, whereas (R3) uses the *uniform reflection principle*. Feferman obtained in 1962 an amazing result that strengthens Turing’s result in a dramatic way.

Let $(\bT_a)_{a\in{\cO}}$ be a progression using the uniform reflection principle with **PA** as the base theory T. Then we have: for any true arithmetical sentence *F* there is an $a\in{\cO}$, such that $\bT_a\vdash F$. Moreover, $a\in{\cO}$ can be chosen such that ${{\mid}\,{a}\,{\mid}}\leq \omega^{\omega^{\omega+1}}$.

For further discussion see [Appendix B](proof-theory.appendix-b.md). Here we just note that the union of the $\bT_a$ is no longer a formal theory.

In the foregoing progressions the ordinals remained external to the theory. *Autonomous progressions of theories* are the proper internalization of the general concept of progressions. In the autonomous case one is allowed to ascend to a theory $\bT_a$ only if one already has shown in a previously accepted theory $\bT_b$ that $a\in{\cO}$. This idea of generating a hierarchy of theories via a boot-strapping process appeared for the first time in Kreisel 1960, where it was proposed as a way of characterizing finitism and predicativism in mathematically precise way. In more formal terms, the starting point is a theory $\bT_0$ which is accepted as correct and an extension procedure $\bT\mapsto\bT'$ which is viewed as leading from a correct theory T to a more encompassing correct theory $\bT'$. Moreover, the language of these theories is supposed to contain a formula $\rAcc(x)$ such that provability of $\rAcc(\bar{a})$ in a correct theory entails that $a\in{\cO}$.[^note-23] Kreisel singled out two autonomous progressions of theories $\{{{\bF}}_a\}$ and $\{{{\bR}}_a\}$ for finitism and predicativity, respectively, and determined the least upper bound of the $\lvert a\rvert$ appearing in the first hierarchy to be the ordinal $\varepsilon_0$ which is also the proof-theoretic ordinal of **PA**. The determination of the least upper bound for the predicative hierarchy $\{{{\bR}}_a\}$ was achieved independently by Feferman (1964) and Schütte (1964, 1965). It turned out that this ordinal can be expressed in a notation system developed by Veblen that will be presented next.

#### 5.2.2 Stronger ordinal representations: The Veblen and Bachmann hierarchies

As we saw above, ordinals below $\varepsilon_0$ suffice for the proof-theoretic treatment of **PA**. For stronger theories segments larger than $\varepsilon_0$ have to be employed, requiring new normal forms akin to Cantor’s normal form. Ordinal representation systems utilized by proof theorists in the 1960s first emerged in a purely set-theoretic context more than 50 years earlier. In 1904 Hardy wanted to “construct” a subset of $\bbR$ of size $\aleph_{1}$, the first uncountable cardinal. His method was to represent countable ordinals via increasing sequences of natural numbers and then to correlate a decimal expansion with each such sequence. Hardy used two processes on sequences: (i) Removing the first element to represent the successor; (ii) Diagonalizing at limits. For example, if the sequence $1,2,3,\ldots$ represents the ordinal 1, then $2,3,4,\ldots$ represents the ordinal 2 and $3,4,5,\ldots$ represents the ordinal 3 etc., while the ‘diagonal’ $1,3,5,\ldots$ provides a representation of $\omega$. In general, if $\lambda=\lim_{n\in\bbN}\lambda_n$ is a limit ordinal with $b_{n1},b_{n2},b_{n3},\ldots$ representing $\lambda_n<\lambda$, then $b_{11},b_{22},b_{33},\ldots$ represents λ. This representation, however, depends on the sequence chosen with limit λ. A sequence $(\lambda_n)_{n\in\bbN}$ with $\lambda_n<\lambda$ and $\lim_{n\in \bN}\lambda_n=\lambda$ is called a *fundamental sequence* for λ. Hardy’s two operations give explicit representations for all ordinals $<\omega^2$.

Veblen in 1908 extended the initial segment of the countable for which fundamental sequences can be given effectively. The new tools he devised were the operations of *derivation* and *transfinite iteration* applied to *continuous increasing functions* on ordinals.

Definition 5.4 Let ${\ON}$ be the class of ordinals. A (class) function $f:{\ON}\to{\ON}$ is said to be *increasing* if $\alpha<\beta$ implies $f(\alpha)<f(\beta)$ and *continuous* (in the order topology on ${\ON}$) if

$$ f(\lim_{\xi<\lambda}\alpha_{\xi})=\lim_{\xi<\lambda}f(\alpha_{\xi}) $$

holds for every limit ordinal λ and increasing sequence $(\alpha_{\xi})_{\xi<\lambda}$. *f* is called *normal* if it is increasing and continuous.

The function $\beta\mapsto \omega+\beta$ is normal while $\beta\mapsto \beta+\omega$ is not continuous at $\omega$ since $\lim_{\xi<\omega}(\xi+\omega)=\omega$ but $(\lim_{\xi<\omega}\xi)+\omega=\omega+\omega$.

Definition 5.5 The *derivative* $f'$ of a function $f:{\ON}\rightarrow {\ON}$ is the function which enumerates in increasing order the solutions of the equation $f( \alpha )= \alpha$, also called the *fixed points* of *f*.

If *f* is a normal function, $\{\alpha:\,f(\alpha)=\alpha\}$ is a proper class and $f'$ will be a normal function, too.

Definition 5.6 Now, given a normal function $f:\ON \rightarrow \ON$, define a hierarchy of normal functions as follows:

$$\begin{align} f_{0}&=f \\ f_{\alpha +1}& =f_{\alpha}'\\ f_{\lambda}(\xi) &= \xi^{\textrm{th}} \textrm{ element of } \bigcap_{\alpha<\lambda} \left(\textrm{Range of } f_{\alpha}\right) \quad\mbox{ for }\lambda \textrm{ a limit ordinal}. \end{align}$$

In this way, from the normal function *f* we get a two-place function, $\varphi_{f} ( \alpha , \beta )\coloneqq f_{\alpha} ( \beta )$. One usually discusses the hierarchy when $f=\ell$, where $\ell( \alpha )=\omega^{\alpha}$. The least ordinal $\gamma>0$ closed under $\varphi_{\ell}$, i.e., the least ordinal $>0$ satisfying $(\forall\alpha,\beta<\gamma)\;\varphi_{\ell}(\alpha,\beta)<\gamma$ is called $\Gamma_0$. It has a somewhat iconic status, in particular since Feferman and Schütte determined it to be the least ordinal ‘unreachable’ by certain *predicative* means expressed in terms of autonomous progressions of theories (defined in section 5.2).

Veblen extended this idea first to arbitrary finite numbers of arguments, but then also to transfinite numbers of arguments, with the proviso that in, for example $\Phi_{f} ( \alpha_{0} , \alpha_{1} , \ldots , \alpha_{\eta} )$, only a finite number of the arguments $\alpha_{\nu}$ may be non-zero. Finally, Veblen singled out the ordinal $E(0)$, where $E(0)$ is the least ordinal $\delta > 0$ which cannot be named in terms of functions $\Phi_{\ell} ( \alpha_{0} , \alpha_{1} , \ldots , \alpha_{\eta} )$ with $\eta < \delta$, and each $\alpha_{ \gamma } < \delta$.

Though the “great Veblen number” (as $E(0)$ is sometimes called) is quite an impressive ordinal it does not furnish an ordinal representation sufficient for the task of analyzing a theory as strong as $\Pi^1_1$-comprehension. Of course, it is possible to go beyond $E(0)$ and initiate a new hierarchy based on the function $\xi\mapsto E(\xi)$ or even consider hierarchies utilizing finite type functionals over the ordinals. Still all these further steps amount to rather modest progress over Veblen’s methods. In 1950 Bachmann presented a new kind of operation on ordinals which dwarfs all hierarchies obtained by iterating Veblen’s methods. Bachmann builds on Veblen’s work but his novel idea was the systematic use of *uncountable ordinals* to keep track of the functions defined by diagonalization. Let ${\Omega}$ be the first uncountable ordinal. Bachmann defines a set of ordinals $\fB$ closed under successor such that with each limit $\lambda\in \fB$ is associated an increasing sequence $\langle \lambda[\xi]:\,\xi<\tau_{\lambda}\rangle$ of ordinals $ \lambda[\xi] \in \fB$ of length $\tau_{\lambda}\leq\Omega$ and $\lim_{\xi<\tau_{\lambda}}\lambda[\xi]=\lambda$. A hierarchy of functions $(\varphi^{\ssfB}_{\alpha})_{\alpha \in \fB}$ is then obtained as follows:

$$\tag{8}\label{bachmann} \begin{align} {\varphi^{\ssfB}_0 (\beta)} = \omega^{\beta} \quad & {\varphi^{\ssfB}_{\alpha+1}} = {\left(\varphi^{\ssfB}_{\alpha}\right)'} \\ \varphi^{\ssfB}_{\lambda} \textrm{ enumerates } & \bigcap_{\xi<\tau_{\lambda}}(\mbox{Range of }\varphi^{\ssfB}_{\lambda[\xi]}) &\kern-12pt \textrm{if } \lambda \textrm{ is a limit with } \tau_{\lambda}<{\Omega} \\ \varphi^{\ssfB}_{\lambda}\textrm{ enumerates } & \{\beta< {\Omega} : \varphi^{\ssfB}_{\lambda[\beta]}(0)=\beta\} &\kern-10pt \textrm{if }\lambda \textrm{ is a limit with } \tau_{\lambda}={\Omega}. \end{align}$$

After the work of Bachmann, the story of ordinal representations becomes very complicated. Significant papers (by Isles, Bridge, Pfeiffer, Schütte, Gerber to mention a few) involve quite horrendous computations to keep track of the fundamental sequences. Also Bachmann’s approach was combined with uses of higher type functionals by Aczel and Weyhrauch. Feferman proposed an entirely different method for generating a Bachmann-type hierarchy of normal functions which does not involve fundamental sequences. Buchholz further simplified the systems and proved their computability. For details we recommend the preface to Buchholz et al. 1981.

#### 5.2.3 Infinitary proofs for predicative theories

The ordinal that Feferman and Schütte determined as the least upper bound for $\{{{\bR}}_a\}$ is $\Gamma_0$, the least non-zero ordinal closed under the Veblen function $\alpha,\beta\mapsto\varphi_{\alpha}(\beta)$. This was a genuine proof-theoretic result with the tools coming ready-made from Schütte’s (1960b) monograph. There he had calculated the proof-theoretic ordinals of the ${{\bR}}_a$ as a function of $\lvert a\rvert$, using cut elimination techniques for logics with infinitary rules (dubbed “semi-formal systems”). If $\lvert a\rvert =\omega^{\alpha}$ then $\lvert {{\bR}}_a\rvert =\varphi_{\alpha}(0)$. “Semi-formal” is a terminology employed by Schütte and refers to the fact that this proof system has rules with infinitely many premises, similar to the $\omega$-rule.

Definition 5.7 In the following we assume that the ordinals come from some representation system. The language of $\bRA^*$ is an extension of that of first order arithmetic. For each ordinal $\alpha$ and $\beta>0$ it has free set variables $U_0^\alpha,U^\alpha_1,U^\alpha_2\ldots$ of level $\alpha$ and bound set variables of level $\beta$. The level, ${\textrm{lev}(A)}$, of a formula *A* of $\bRA^*$ is defined to be the maximum of the levels of set variables that occur in *A*. Expressions of the form $\{x\mid A(x)\}$ with $A(u)$ a formula will be called *abstraction terms*, their level being the same as that of the formula $A(u)$.

The inference rules of $\bRA^*$ comprise those of the sequent calculus with the exception of $(\forall R)$ and $(\exists L)$ which are replaced by those for the $\omega$-rule: $\omega$R and $\omega$L. Below $\fP_{\beta}$ stands for the set of all abstraction terms with levels $<\beta$. The rules for the set quantifiers are as follows:

$$ \tag*{\({\forall_\beta\,\bL}\)} \frac{F(P),\Gamma\Rightarrow \Delta,} {\forall X^\beta\,F(X^\beta),\Gamma\Rightarrow \Delta} $$ $$ \tag*{\({\forall_\beta}\,\rR\)} \frac{\Gamma\Rightarrow \Delta, F(P)\ \textrm{ all } P\in{\fP}_{\beta}} {\Gamma\Rightarrow \Delta, \forall X^\beta\,F(X^\beta)} $$ $$ \tag*{\({\exists_\beta}\,\bL\)} \frac{F(P),\Gamma\Rightarrow \Delta\ \textrm{ all } P\in{\fP}_{\beta}} {\exists X^\beta\,F(X^\beta),\Gamma\Rightarrow \Delta} $$ $$ \tag*{\({\exists_\beta}\,\rR\)} \frac{\Gamma\Rightarrow \Delta,F(P)} {\Gamma\Rightarrow \Delta, \exists X^{\beta} F(X^{\beta})} $$

where in $\forall_\beta\bL$ and $\exists_\beta\rR$, *P* is an abstraction term of level $<\beta$.

As per usual, the price one has to pay for rules with infinitely many premises is that derivations become infinite (well-founded) trees. The length of a derivation can then be measured by the ordinal rank associated with the tree. One also wants to keep track of the complexity of cuts in the derivation. The length we assign to a formula *A*, $\lvert A\rvert$, measures its complexity. It is an ordinal of the form $\omega\cdot \alpha+n$ where $\alpha$ is the level of *A* and $n<\omega$. One then defines a notion of derivability in ${{\bRA}}$,

$$ \bRA^* \stile{\alpha}{\rho} \Gamma\Rightarrow \Delta $$

where $\alpha$ majorizes the transfinite length of the derivation and $\rho$ conveys that all cut formulae in the derivation have length $<\rho$.

Cut elimination works smoothly for $\bRA^*$. However, the prize one has to pay can only be measured in terms of Veblen’s $\varphi$ function. The optimal result is the so-called second cut elimination theorem.

Theorem 5.8 (Second Cut Elimination Theorem)

$$ \textrm{If } \bRA^* \stile{\alpha}{\rho+\omega^\nu} \Gamma\Rightarrow \Delta \textrm{ then } \bRA^* \stile{\varphi_{\nu}(\alpha)}{\rho} \Gamma\Rightarrow \Delta $$

It entails of course the special case that $\bRA^* \stile{\alpha}{\omega^\nu} \Gamma\Rightarrow \Delta$ yields $\bRA^* \stile{\varphi_{\nu}(\alpha)}{0} \Gamma\Rightarrow \Delta$, and thus, as the latter deduction is cut-free, all cuts can be removed. Several subtheories of $\bZ_2$ can be interpreted in $\bRA^*$, yielding upper bounds for their proof-theoretic ordinals via Theorem 5.8. Here is a selection of such results:[^note-24]

Theorem 5.9

1. $\lvert (\Pi^1_0{\Hy}\bCA)_0\rvert =\varepsilon_0$.
2. $\lvert (\Pi^1_0{\Hy}\bCA)\rvert = \varphi_2(0)=\varepsilon_{\varepsilon_0}$.
3. $\lvert (\Delta^1_1{\Hy}\bCR)\rvert = {\varphi}_{\omega}(0)$.
4. $\lvert (\Delta^1_1{\Hy}\bCA)\rvert = \lvert (\Sigma^1_1{\Hy}\bAC)\rvert = {\varphi}_{\varepsilon_0}(0)$.

For the definitions of the theories in this theorem, see end of section 5.1. To obtain the results about theories in (iii) and (iv) it is somewhat easier to first reduce them to systems of the form $(\Pi^0_1{\Hy}\bCA)_{<\rho}$ as the latter have a straightforward interpretation in ${{\bRA}}^*$. Reductions of $(\Delta^1_1{\Hy}\bCR)$ to $(\Pi^0_1{\Hy}\bCA)_{<\omega^{\omega}}$ and of $(\Sigma^1_1{\Hy}\bAC)$ to $(\Pi^0_1{\Hy}\bCA)_{<\varepsilon_0}$ are due to Feferman (1964) and Friedman (1970), respectively.[^note-25]

The investigation of such subsystems of analysis and the determined effort to establish their mathematical power led to a research program that was initiated by Friedman and Simpson some thirty years ago and dubbed *Reverse Mathematics*. The objective of the program is to investigate the role of set existence principles in ordinary mathematics.[^note-26] The main question can be stated as follows:

Given a specific theorem $\tau$ of ordinary mathematics, which set existence axioms are needed in order to prove $\tau$?

Central to the above is the reference to what is called ‘ordinary mathematics’. This concept, of course, doesn’t have a precise definition. Roughly speaking, by ordinary mathematics we mean main-stream, non-set-theoretic mathematics, i.e., the core areas of mathematics which make no essential use of the concepts and methods of set theory and do not essentially depend on the theory of uncountable cardinal numbers.

For many mathematical theorems $\tau$, there is a weakest natural subsystem ${\bS}(\tau)$ of $\bZ_2$ such that ${\bS}(\tau)$ proves $\tau$. Very often, if a theorem of ordinary mathematics is proved from the weakest possible set existence axioms, the statement of that theorem will turn out to be provably equivalent to those axioms over a still weaker base theory. Moreover, it has turned out that ${\bS}(\tau)$ often belongs to a small list of specific subsystems of $\bZ_2$ dubbed $\RCA_0$, $\WKL_0$, $\ACA_0$, $\ATR_0$ and $({\bPi}^1_1{\Hy}{\bCA})_0$, respectively.[^note-27] The systems are enumerated in increasing strength. The main set existence axioms of $\RCA_0$, $\WKL_0$, $\ACA_0$, $\ATR_0$, and $({{\bPi}}^1_1{\Hy}{\bCA})_0$ are recursive comprehension, weak König’s lemma, arithmetical comprehension, arithmetical transfinite recursion, and $\bPi_1^1$-comprehension, respectively. $\ACA_0$ is actually the same theory as $(\Pi^1_0{\Hy}\bCA)_0$. For exact definitions of all these systems and their role in reverse mathematics see Simpson 1999. Examples of mathematical statements provable in $\RCA_0$ are the intermediate value theorem and the Baire category theorem. Reversals for $\WKL_0$ are the Heine/Borel covering lemma and the local existence theorem for solutions of ordinary differential equations. Among the many reversals for $\ACA_0$, $\ATR_0$, and $(\bPi^1_1{\Hy}{\bCA})_0$ one finds the existence of maximal ideals in countable rings, Ulm’s theorem, and the Cantor-Bendixson theorem, respectively.

The proof-theoretic strength of $\RCA_0$ is weaker than that of **PA** while $\ACA_0$ has the same strength as **PA**. To get a sense of scale, the strengths of the first four theories are best expressed via their proof-theoretic ordinals:

Theorem 5.10

1. $\lvert \RCA_0\rvert =\lvert \WKL_0\rvert =\omega^{\omega}$.
2. $\lvert \ACA_0\rvert =\varepsilon_0$.
3. $\lvert \ATR_0\rvert =\Gamma_0$.

$\lvert (\bPi^1_1\Hy\bCA)_0\rvert$, however, eludes expression in the ordinal representations introduced so far. This will require the much stronger representation to be introduced in Definition 5.11.

There are important precursors of reverse mathematics. Weyl (1918) started to develop analysis using a minimalist foundation (that equates to $\ACA_0$) whilst Hilbert and Bernays (1939) developed analysis in second order arithmetic, whereby on closer inspection one sees that all they used is $(\bPi^1_1\Hy\bCA)_0$. The first theorem of genuinely reverse mathematics was established by Dedekind in his essay *Stetigkeit und irrationale Zahlen* (1872). It states that his continuity (or completeness) principle is equivalent to a well-known theorem of analysis, namely, every bounded, monotonically increasing sequence has a limit. He emphasizes,

> This theorem is equivalent to the principle of continuity, i.e., it loses its validity as soon as we assume a single real number not to be contained in the domain $\cR$ [of all real numbers, i.e., of all cuts of rational numbers]. (1872 [1996: 778])

It is to bring out “the connection between the principle of continuity and infinitesimal analysis” (1872 [1996: 779]).

### 5.3 Impredicative Subsystems and Generalized Inductive Definitions

Spector’s (1962) functional interpretation of $\bZ_2$ via bar recursive functionals was of great interest to proof theory. However, it was not clear whether there was a constructive foundation of these functionals along the lines of hereditarily continuous functionals that can be represented by computable functions (akin to Kleene 1959; Kreisel 1959)[^kleene-1959][^kreisel-1959] which would make them acceptable on intuitionistic grounds. In 1963 Kreisel conducted a seminar the expressed aim of which was to assay the constructivity of Spector’s interpretation (see Kreisel 1963)[^kreisel-1963]. Specifically he asked whether an intuitionistic theory of monotonic inductive definitions, $\bID^i_1(\text{mon})$, could model bar recursion, or even more specifically, formally capture a class of indices of representing functions of these functionals. In a subsequent report the seminar’s conclusion was later summarized by Kreisel:

> … the answer is negative by a wide margin, since not even bar recursion of type 2 can be proved consistent [from intuitionistically accepted principles]. (Kreisel in “Reports of the Seminar on the Foundations of Analysis, Stanford, Summer 1963”, as quoted in Feferman 1998: 223)[^feferman-1998]

He not only introduced theories of one inductive definition but also of $\nu$-times transfinitely iterated inductive definitions, $\bID_{\nu}$. Albeit it soon became clear that even the theories $\bID_{\nu}$ couldn’t reach the strength of $\bZ_2$ (in point of fact, such theories are much weaker than the fragment of $\bZ_2$ based on $\Pi^1_2$-comprehension); they became the subject of proof-theoretic investigation in their own right and occupied the attention of proof theorists for at least another 15 years. One reason for this interest was surely that the intuitionistic versions corresponding to the accessible (i.e., well-founded) part of a primitive recursive ordering are immediately constructively appealing and a further reason was that they were thought to be more amenable to direct proof-theoretic treatments than fragments of $\bZ_2$ or set theories.

We shall not give a detailed account of the formalization of these theories, but focus on the non-iterated case $\bID_1$ and its intuitionistic version $\bID_1^i$ to convey the idea. A monotone operator on $\bbN$ is a map $\Gamma$ that sends a set $X\subseteq \bbN$ to a subset $\Gamma(X)$ of $\bbN$ and is monotone, i.e., $X\subseteq Y\subseteq \bbN$ implies $\Gamma(X) \subseteq \Gamma(Y)$. Owing to monotonicity, the operator $\Gamma$ will have a least fixed point $I_{\Gamma}\subseteq\bbN$, i.e., $\Gamma( I_{\Gamma})=I_{\Gamma}$ and for every other fixed point *X* it holds $I_{\Gamma} \subseteq X$. Set-theoretically $I_{\Gamma}$ is obtained by iterating $\Gamma$ through the ordinals,

$$ \begin{align} \Gamma^0&=\emptyset,\\ \Gamma^1&=\Gamma(\Gamma^0),\\ \Gamma^{\alpha}&=\Gamma\left(\bigcup_{\xi<\alpha}\Gamma^{\xi}\right). \end{align} $$

Monotonicity ensures (in set theory) that one finds an ordinal $\tau$ such that $\Gamma(\Gamma^{\tau})=\Gamma^{\tau}$, and the set $\Gamma^{\tau}$ will be the least fixed point. If one adds a new 1-place predicate symbol *P* to the language of arithmetic, one can describe the so-called positive arithmetical operators. They are of the form

$$ \Gamma_A(X)=\{n\in\bbN\mid A(n,X)\} $$

where $A(x,P)$ is a formula of the language of **PA** augmented by *P* in which the predicate *P* occurs only positively.[^note-28] The syntactic condition of positivity then ensures that the operator $\Gamma_A$ is monotone. The language of $\bID_1$ is an extension of that of **PA**. It contains a unary predicate symbol $I_A$ for each positive arithmetical operator $\Gamma_A$ and the axioms

$$\label{id1} \begin{align} \tag{Id1} \forall x\,(A(x,I_A)\rightarrow I_A(x))\\ \tag{Id2} \forall x\,[A(x,F)\to F(x)]\to \forall x\,[I_A(x)\to F(x)] \end{align} $$

where in (Id2) $F(x)$ is an arbitrary formula of $\bID_1$ and $A(x,F)$ arises from $A(x,P)$ by replacing every occurrence of $P(t)$ in the formula by $F(t)$. Collectively these axioms assert that $I_A$ is the least fixed point of $\Gamma_A$, or more accurately the least among all sets of natural numbers definable in the language of $\bID_1$. $\bID_1^i$ will be used to denote the intuitionistic version. Its subtheory $\bID_{1}^{i}(\cO)$ is obtained by just adding the predicate symbol $I_A$ and the pertaining axioms (Id1) and (Id2), where $\Gamma_A$ is the operator that defines Kleene’s $\cO$ (cf. Definition 5.1).

By a complicated passage through formal theories for choice sequences it was known that the theory $\bID_{1}$ can be reduced to $\bID_{1}^{i}(\cO)$. The first ordinal analysis for the theory $\bID_{1}^{i}(\cO)$ was obtained by Howard (1972). Via the known proof-theoretical reductions this entailed also an ordinal analysis for $\bID_{1}$. The proof-theoretic ordinal of $\bID_{1}$ is the *Bachmann-Howard ordinal*, which is denoted by ${\psi_{\sOmega_{1}}(\varepsilon_{\Omega_1+1})}$ in the system of Definition 5.11.

As inductively defined sets can be the starting point of another inductive definition, the procedure of inductively defining predicates can be iterated along any well-ordering $\nu$ in a uniform way. This leads to the theories $\bID_{\nu}$ which allow one to formalize $\nu$-times iterated inductive definitions, where $\nu$ stands for a primitive recursive well-ordering. If $\nu$ is a well-ordering on constructive grounds then also the $\nu$-times iterated version of Kleene’s $\cO$ has a clear constructive meaning. As a result the formal theories ${{\bID}}^i_{\nu}(\cO)$ that embody this process are constructively justified. The topic of theories of iterated inductive definitions was flourishing at the 1968 conference on Intuitionism and Proof Theory in Buffalo (see Kino et al. 1970)[^kino-1970]. One of the main proof-theoretic goals was to find a reduction of the classical theories $\bID_{\nu}$ to their intuitionistic counterparts ${{\bID}}^i_{\nu}(\cO)$. This was all the more desirable because of known reductions of important fragments of second order arithmetic to theories of the former kind. Friedman (1970) had shown that the second order system with the $\Sigma _2^1$-axiom of choice can be interpreted in the system $\hbox{($\Pi_1^1$-CA)}_{<{\varepsilon_0}}$ of less than ${\varepsilon_0}$-fold iterated $\Pi_1^1$-comprehensions and Feferman (1970a) had shown that less than $\nu$-fold iterated $\Pi_1^1$-comprehensions could be interpreted in the system

$$ \bID_{<\nu} \coloneqq \bigcup_{\alpha<\nu}\bID_{\alpha} $$

for $\nu=\omega^{\gamma}$ with $\gamma$ limit. However, Zucker (1973) showed that there are definite obstacles to a straightforward reduction of the theories $\text{ID}_{\nu}$ for $\nu > 1$ to their intuitionistic cousins. Sieg (1977) attacked the problem by a method adapted from Tait (1970) who had used cut elimination for an infinitary propositional logic with formulae indexed over constructive number classes to obtain a consistency proof for second order arithmetic theory with the schema of $\Sigma _2^1$ dependent choices. He achieved a reduction of $\bID_{<\nu}$ to $\bID_{<\nu}^i(\cO)$ for limit $\nu$ by carrying out the proof theory for a system of $\PL_{\alpha}$ of propositional logic with infinitely long conjunctions and disjunctions indexed over the constructive number classes $\cO_{\alpha}$ for $\alpha<\nu$ inside $\bID^i_{\alpha+1}(\cO)$. As $\bID_{\alpha}$ can be reduced to $\PL_{\alpha}$ this brought about the reduction. Ordinal analyses for theories of iterated inductive definitions, first for finite and then also for transfinite iterations, were obtained by Pohlers using Takeuti’s reduction procedure for $\Pi_1^1$-comprehension (see Pohlers 1975, 1977)[^pohlers-1975]. Working independently, Buchholz (1977a) used a new type of rules, dubbed $\Omega_{\mu+1}$-rules to recapture these results without use of Takeuti’s methods. These rules are an extension of the Ω-rule described in Definition C.3.

#### 5.3.1 Interlude: an ordinal representation system beyond Bachmann’s

The ordinal representation systems encountered so far are not sufficient for expressing the strength of theories of iterated inductive definitions nor that of the strongest of the standard system of reverse mathematics, $(\Pi^1_1{\Hy}\bCA)_0$. Therefore we intersperse a brief account of how to proceed onwards, adumbrating the main ideas.

Bachmann’s bold move of using large ordinals to generate names for small ordinals was a very important idea. To obtain ordinal analyses of ever stronger theories one has to find new ways of defining ordinal representation systems that can encapsulate their strength. The latter goes hand in hand with the development of new cut elimination techniques that are capable of removing cuts in (infinitary) proof systems with strong reflection rules. Ordinal representations, however, appear to pose a considerable barrier to understanding books and articles in this research area. Nonetheless we think that they are the best way to express the proof-theoretic strength of a theory as they provide a scale by means of which one can get a grasp of how much stronger a theory $S_1$ is than another theory $S_2$ (rather than the bland statement that $S_1$ is stronger than $S_2$).

As an example we will introduce an ordinal representation system which characterizes the theory $(\Pi^1_1{\Hy}\bCA)+{{\BI}}$, following Buchholz 1977b. It is based on certain ordinal functions $\psi_{\sOmega_n}$ which are often called *collapsing functions*. The definition of these functions, that is of the value ${\psi_{\sOmega_{n}}(\alpha)}$ at $\alpha$, proceeds by recursion on $\alpha$ and gets intertwined with the definition of sets of ordinals $C^{{\Omega_{\omega}}}(\alpha,\beta)$, dubbed “Skolem hulls” since they are defined as the smallest structures closed under certain functions specified below.

Let $\bbN^+$ be the natural numbers without 0. Below we shall assume that $\Omega_n$ $(n\in\bbN^+)$ is a “large” ordinal and that $\omega<\Omega_n <\Omega_{n+1}$. Their limit, $\sup_{n\in\bbN^+}\Omega_n$, will be denoted by $\Omega_{\omega}$.

Definition 5.11 By recursion on $\alpha$ we define:

$$\begin{align} C^{\Omega_{\omega}}(\alpha,\beta) & = \left\{\begin{array}{l} \textrm{closure of } \beta\cup\{0,\Omega_{\omega}\}\cup\{\Omega_n\mid n\in\bbN^+\} \\ \textrm{under: }\\ +, (\xi\mapsto \omega^{\xi})\\ (\xi\longmapsto{\psi_{\sOmega_{n}}(\xi)})_{\xi<\alpha}\textrm{ for } n\in\bbN^+ \end{array}\right. \\[1ex] {\psi_{\sOmega_{n}}(\alpha)}&= \min\{\rho<\Omega_n\mid\;C^{\Omega_{\omega}}(\alpha,\rho)\cap\Omega_n=\rho\}. \end{align}$$

At this point it is not clear whether ${\psi_{\sOmega_{n}}(\alpha)}$ will actually be defined for all $\alpha$ since there might not exist a $\rho<\Omega_n$ such that

$$ C^{{\Omega_{\omega}}}(\alpha,\rho)\cap\Omega_n=\rho. $$

This is where the “largeness” of $\Omega_n$ comes into play. One (easy) way of guaranteeing this consists in letting $\Omega_n$ be the $n^{th}$ uncountable regular cardinal, that is $\Omega_n\coloneqq \aleph_n$. However, such strong set-theoretic assumptions can be avoided. For instance, it suffices to let $\Omega_n$ be the $n^{th}$ recursively regular ordinal (which is a countable ordinal) (see Rathjen 1993a)[^rathjen-1993a].

To get a better feel for what $\psi_{\sOmega_{n}}$ is doing, note that if $\rho={\psi_{\sOmega_{n}}(\alpha)}$, then $\rho<\Omega_n$ and with $[\rho,\Omega_n)$ being the interval consisting of ordinals $\rho\leq\alpha<\Omega_n$ one has

$$ [\rho,\Omega_n)\cap C^{\Omega_{\omega}} (\alpha,\rho) =\emptyset $$

thus the order-type of the ordinals below $\Omega_n$ which belong to the “Skolem hull” $C^{{\Omega_{\omega}}}(\alpha,\rho)$ is $\rho$. In more pictorial terms, $\rho$ is said to be the $\alpha^{th}$ *collapse* of $\Omega_n$ since the order-type of $\Omega_n$ viewed from within the structure $C^{{\Omega_{\omega}}}(\alpha,\rho)$ is actually $\rho$.

The ordinal representation system we are after is provided by the set

$$ C^{{\Omega_{\omega}}}(\varepsilon_{\Omega_{\omega}+1},0) $$

where $\varepsilon_{\Omega_{\omega}+1} $ is the least epsilon number after $\Omega_{\omega}$, i.e., the least ordinal $\eta>\Omega_{\omega}$ such that $\omega^{\eta}=\eta$. The proof-theoretic ordinal of $(\Pi^1_1{\Hy}\bCA)+{{\BI}}$ is ${\psi_{\sOmega_{1}}(\varepsilon_{\Omega_{\omega}+1})}$. Although the definition of the set $C^{{\Omega_{\omega}}}(\varepsilon_{\Omega_{\omega}+1},0)$ and its ordering is set-theoretic, it turns that it also has a purely primitive recursive definition which can be given in a fragment of **PRA**. Thus the set-theoretic presentation mainly serves the purpose of a “visualization” of an elementary well-ordering.

The pattern of definition exhibited in Definition 5.11 continues for stronger systems, albeit only as a basic template since for theories beyond the level of $(\Delta^1_2{\Hy}\bCA)+{{\BI}}$ substantially new ideas are required. Analogies between large set-theoretic ordinals (cardinals) and recursively large ordinals on the one hand and ordinal representation systems on the other hand can be a fruitful source of inspiration for devising new representation systems. More often than not, hierarchies and structural properties that have been investigated in set theory and recursion theory on ordinals turn out to have proof-theoretic counterparts.

#### 5.3.2 Assigning proof-theoretic ordinals

Using an extended version of the representation system from Definition 5.11 if $\nu>\omega$,[^note-29] the outcome of all the work on the theories of inductive definitions can be summarized by the following theorem.[^note-30]

Theorem 5.12 For recursive $\nu$,

$$ \lvert \bID_{\nu}\rvert = \lvert \bID^i_{\nu}(\cO)\rvert = \psi_{\sOmega_\nu}(\varepsilon_{\sOmega_{\nu}+1}). $$

A generalized treatment of theories of iterated inductive definitions for arbitrary well-orderings and of autonomous iteration was carried out in Rathjen 1988, 2010. These theories are stronger than $(\Delta^1_2{\Hy}\bCA)$ if $\nu\geq\varepsilon_0$.

Theorem 5.12 played an important role in determining the exact strength of some fragments of $\bZ_2$. The major ordinal-theoretic results pertaining to subsystems of $\bZ_2$ of the pre-1980 area given in the next theorem.[^note-31]

Theorem 5.13

1. $\lvert (\Pi^1_1{\Hy}\bCA)_0\rvert = \lvert \bID_{<\omega}\rvert =\psi_{\sOmega_1}(\Omega_{\omega})$
2. $\lvert (\Pi^1_1{\Hy}\bCA)\rvert =\psi_{\sOmega_1}(\Omega_{\omega}\cdot\varepsilon_0)$
3. $\lvert (\Pi^1_1{\Hy}\bCA)+{{\BI}}\rvert =\lvert \bID_{\omega}\rvert =\psi_{\sOmega_1}(\varepsilon_{\sOmega_{\omega}+1})$
4. $\lvert (\Delta^1_2{\Hy}\bCR)\rvert = \psi_{\sOmega_1}(\Omega_{\omega^{\omega}})$
5. $\lvert (\Delta^1_2{\Hy}\bCA)\rvert = \psi_{\sOmega_1}(\Omega_{\varepsilon_0})$

The next challenge after $(\Delta^1_2{\Hy}\bCA)$ was posed by the theory $(\Delta^1_2{\Hy}\bCA)+{{\BI}}$. Its treatment not only required a considerably stronger ordinal representation system but also coincided with a shift away from $\cL_2$ theories and theories of iterated inductive definitions to a direct proof-theoretic treatment of set theories. Pioneering work on the proof theory of set theories is mainly due to Jäger (1980, 1982). The analysis of $(\Delta^1_2{\Hy}\bCA)+{{\BI}}$ in Jäger & Pohlers 1982 provides a particularly nice application of this new approach which has been called *admissible proof theory*, owing to its concern with theories extending Kripke-Platek set theory by axioms asserting the existence of admissible sets (for some details see Appendix D.1).

Theorem 5.14 $\lvert (\Delta^1_2{\Hy}\bCA)+\BI\rvert = \psi_{\sOmega_1}(\varepsilon_{I+1})$

The “*I*” in the foregoing notation is supposed to be indicative of “*inaccessible cardinal*”. Indeed, the easiest way to build an extended ordinal representation system sufficient unto this task (modeled on Definition 5.11) is to add an inaccessible *I*, close the Skolem hulls under $\xi\mapsto \Omega_\xi$ for $\xi<I$ and introduce collapsing functions $\psi_{\pi}$ for all $\pi$ of either form *I* or $\Omega_{\xi+1}$.

The goal of giving an ordinal analysis of full second order arithmetic has not been attained yet. For many years $\Pi^1_2$-comprehension posed a formidable challenge and the quest for its ordinal analysis attained something of a holy grail status (cf. Feferman 1989)[^feferman-1989]. At first blush it might be difficult to see why the latter comprehension is so much more powerful than $\Delta^1_2$-comprehension (plus ${{\BI}}$). To get a sense for the enormous difference, it seems advisable to work in (admissible) set theory and consider a hierarchy of recursively large ordinal notions wherein these comprehension schemes correspond to the bottom and the top end of the scale, respectively. That is discussed in [Appendix D](proof-theory.appendix-d.md). Here we just mention a few reductions to “constructive” frameworks. The reductions we have in mind, underlie a broadened view of “constructivity”. Constructive theories of functions and sets that relate to Bishop’s constructive mathematics as theories like **ZFC** relate to Cantorian set theory have been proposed by Myhill, Martin–Löf, Feferman and Aczel. Among those are Feferman’s constructive theory of operations and classes, $\bT_0$ in 1975 and 1979, Martin-Löf’s intuitionistic type theory (1984) and constructive set theory, especially Constructive Zermelo-Fraenkel Set Theory, **CZF**, the latter also combined with the regular extension axiom, **REA**. By employing an ordinal analysis for set theory **KPi** which is an extension of Kripke-Platek set theory via an axiom asserting that every set is contained in an admissible set (see [Appendix D](proof-theory.appendix-d.md)) it has been shown that **KPi** and consequently $(\Delta^1_2{\Hy}\bCA)+{{\BI}}$ can be reduced to both of these theories:

Theorem 5.15 (Feferman 1975; Jäger 1983; Jäger & Pohlers 1982; Rathjen 1993b)[^feferman-1975][^jäger-1982][^jäger-1983][^jäger-1982-2][^pohlers-1982] $(\Delta^1_2{\Hy}\bCA)+\BI$, **KPi**, $\bT_0$ and **CZF**+**REA** are proof-theoretically equivalent. In particular, these theories prove the same theorems in the negative arithmetic fragment.

Theorem 5.16 (Rathjen 1993b; Setzer 1998)[^setzer-1998] The soundness of the negative arithmetic fragment of $\Delta^1_2-\bCA+\BI$ and **KPi** is provable in Martin-Löf’s 1984 type theory.

A detailed account of these results has been given in section 3 of Rathjen 1999a.

## 6. Epilogue

Proof theory has become a large subject with many specialized branches that can be mathematically quite complex. So we have tried to present developments close to the main artery of its body, starting with its inception at the beginning of the twentieth century and ending with results from the close of the century. The theorems mentioned at the end of section 5 foreshadow investigations in the twenty-first century that are presented in Rathjen (2018) and concern relationships between Feferman’s systems of explicit mathematics and Martin-Löf type theories; the paper touches also on the completely new developments of homotopy type theory (see Awodey 2012)[^awodey-2012]. Some additional contemporary proof theoretic developments are described in appendices [D](proof-theory.appendix-d.md), [E](proof-theory.appendix-e.md) and [F](proof-theory.appendix-f.md). The theme of [Appendix E](proof-theory.appendix-e.md), the extraction of computational information from proofs in particular formal theories, is the central topic of Schwichtenberg and Wainer’s 2012. They deal with theories of arithmetic and analysis up to $(\Pi^1_1{\Hy}\bCA)_0$. Standard texts on proof theory covering ordinal analysis are Takeuti 1985 and Schütte 1977. An introductory text book on ordinal analysis is Pohlers 2009 and a more recent one is Arai 2020. Finally, some new directions of proof theoretic work are taken in contributions to both Kahle & Rathjen 2015 and Jäger & Sieg 2018.

Let us also report on progress on the methodological issues the finitist consistency program was to address. First of all, due to quite a bit of important historical work, we have a much better grasp of the evolution of the program in the 1920s and its roots in the development toward modern structuralist mathematics in the nineteenth century. The work of editing Hilbert’s unpublished lecture notes has opened a treasure of information.[^note-32] The connections to the development in nineteenth century mathematics are hinted at in [Appendix A](proof-theory.appendix-a.md), but they are explored in greater depth, for example, in Ferreirós 2008; Reck 2003, 2013; and the papers Sieg wrote on Dedekind with Morris (2018) and Schlimm (2005, 2014), respectively. The 2020 volume edited by Reck & Schiemer explores this connection in a rich way. Secondly, as to the properly methodological issues, we presented some broad considerations in section 4.1, namely, that consistency proofs should be given relative to “constructive” theories. We did not make any remarks about what is characteristic of a constructive perspective and why such a perspective has not only a mathematical, but also a philosophical point. There is, of course, a very rich literature. Let us point to some informative sources: van Atten (2007) as defending Brouwer’s views, Martin-Löf (1984) as exposing the philosophical motivation for his type theory, Feferman (1988, 2000) discussing the foundational point of proof theory, Bernays (1976) as presenting crucial aspects of an informed philosophy of mathematics, and (Sieg 2013, 2020)[^sieg-2013] as explicating (the context for) his *reductive structuralism*.

Back to proof theory: We have to admit that we neglected some classical topics. One is the study of different proof systems and their relationships going back to Gentzen’s dissertation (1935). In their *Basic Proof Theory*, Troelstra and Schwichtenberg (2000) give an excellent selection, but some important calculi such as the Schütte proof systems are not covered (see, for example, Schütte 1960b, 1977)[^schütte-1960b]. They also do not cover proof systems for temporal and modal logic, neither are substructural logics presented.[^note-33]

A second omission concerns Bounded Arithmetic, where feasibility issues are a central focus: one studies formal theories with provably recursive functions that form very small subclasses of the primitive recursive ones. Indeed, the class of the provably total functions of Buss’ base theory is that of functions that can be computed in polynomial time, and there was the hope that proof theoretic investigations might contribute novel results in complexity theory. A third omission concerns proof mining; that line of deep mathematical investigations using proof theoretic tools was initiated by Kreisel (1958, 1982) and Luckhardt (1989), but really perfected only by Kohlenbach (2007). We hinted at the work of his school at the very end of section 4.1.

Proof theory, as we described it, deals primarily with formal proofs or derivations. Hilbert aimed, however, as we pointed out in section 1, for a more general analysis of ordinary, informal mathematical proofs. For Gentzen in his 1936, “the objects of proof theory shall be the *proofs* carried out in mathematics proper” (p. 499). The aim of Hilbert and his collaborators was undoubtedly to achieve a deeper mathematical and conceptual understanding, but also to find general methods of proof construction in formal calculi. This is now being pursued in the very active area of using powerful computers for the interactive verification of proofs and programs as well as the fully automated search for proofs of mathematical theorems.[^note-34] That can be pursued with a cognitive scientific purpose of modeling mathematical reasoning (see Sieg 2010, Ganesalingam & Gowers 2017, and Sieg & Derakhshan 2021)[^ganesalingam-2017][^sieg-2010][^sieg-2021]. It is clearly in the spirit of Hilbert who articulated matters in his second Hamburg talk of 1927 as follows:

> The formula game … has, besides its mathematical value, an important general philosophical significance. For this formula game is carried out according to certain definite rules, in which the technique of our thinking is expressed. These rules form a closed system that can be discovered and definitively stated.

Then he continues with a provocative statement about the cognitive goal of proof theoretic investigations.

> The fundamental idea of my proof theory is none other than to describe the activity of our understanding, to make a protocol of the rules according to which our thinking actually proceeds. (Hilbert 1927 [1967: 475])[^hilbert-1927]

It is clear to us, and it was clear to Hilbert, that mathematical thinking does not proceed in the strictly regimented ways imposed by an austere formal theory. Though formal rigor is crucial, it is not sufficient to shape proofs intelligibly or to discover them efficiently, even in pure logic. Recalling the principle that mathematics should solve problems “by a minimum of blind calculation and a maximum of guiding thought”, we have to investigate the subtle interaction between understanding and reasoning, i.e., between introducing concepts and proving theorems.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=proof-theory). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/proof-theory/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=proof-theory&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/proof-theory/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

[Please contact the author with suggestions.]

## Related Entries

epsilon calculus | Hilbert, David: program in the foundations of mathematics | logic: linear | mathematics: constructive | proof theory: development of | reasoning: automated | semantics: proof-theoretic | set theory: constructive and intuitionistic ZF | type theory

### Acknowledgments

Some passages in this entry first appeared in W. Sieg, *Hilbert’s Programs and Beyond*, Oxford: Oxford University Press, 2013.

## Notes（原文脚注）

## Notes to Proof Theory

[^note-1]: The evolution of this methodological perspective to formal axiomatics is described in [Appendix A](proof-theory.appendix-a.md).

[^note-2]: The term “finit” is used without much explanation; one is led to think that it was a thoroughly familiar one. Indeed, the 1919 article by Bernstein calls “finit” all considerations that have a constructive feature, from Kronecker through Poincaré to Brouwer. It is obviously used also to emphasize the contrast with “transfinit”. The term was also prominently used by Weyl in *Das Kontinuum* (1918).

[^note-3]: *Primitive recursion* is given by the equations

$$f(x_1,\ldots, x_n,0)=g(x_1,\ldots,x_n)$$

and

$$f(x_1,\ldots,x_n,S(x))=h(x_1,\ldots,x_n,f(x_1,\ldots,x_n,x),x)$$

where *S* is the successor function and *g*, *h* are previously defined primitive recursive functions. The class of primitive recursive functions is obtained from the constant 0 function, *S* and the projection functions $P^i_n(x_1,\ldots,x_n)=x_i$ by closure under composition and the above recursion schema.

The language of **PRA** has the equality symbol = and function symbols for all primitive recursive functions. The axioms of **PRA** consist of the defining equations for the primitive recursive functions and the induction scheme $$ {A(0)} \land {\forall x[A(x)\to A(Sx)]\to \forall x A(x)} $$ for atomic formulas $A(x)$. Note that atomic formulas $A(x)$ of **PRA** are of the form $t_1(x)=t_2(x)$ for terms $t_1(x)$ and $t_2(x)$.

[^note-4]: Many contemporary writers consider Hilbert 1922 as the beginning of Hilbert’s finitist program; see, for example, Franks 2009. However, Hilbert’s paper is split into two parts, according to the editors of the third volume of Hilbert’s *Gesammelte Abhandlungen* in which it was republished: the first part stems from the older considerations that go back to the Heidelberg talk (Hilbert 1905)[^hilbert-1905]; see appendix A.3. In the second part a new direction is taken that involves a significantly expanded formal theory; however, the theory is by design “constructive”, as negation is applied only to equations. A consistency proof for this expanded theory is not presented and could not be obtained by the old techniques; the result, when suitably restricted as the Editors of the volume suggest, can be obtained by the methods introduced in early 1922. It is only then that the finitist standpoint is taken.

[^note-5]: There is a delicate evolution from “tau” to “epsilon” that can be followed in Ewald and Sieg 2013; here we use directly the epsilon terms.

[^note-6]: The so-called $\varepsilon$-substitution method has been re-invigorated by work of Tait and Mints; a broad survey is given in Avigad and Zach 2007.

[^note-7]: The Ackermann function was included among Herbrand’s finitist functions. At this point, the system F was not “identified” with **PRA**.

[^note-8]: See, for detailed discussion, mathematical analysis and additional references, Tait 2002 and Feferman & Strahm 2010. A penetrating explication of the finitist standpoint taken by Hilbert and Bernays is given in Ravaglia 2003.

[^note-9]: Hilbert’s considerations are analyzed in Sieg 2012 (section 5) and are also discussed in Hallett 2013.

[^note-10]: For the close connections between Hilbert’s proposal and Gentzen’s attempt to mould it into a consistency proof, see section 6 of Sieg 2012. The work in Gentzen’s “Urdissertation” is described in von Plato 2008 and 2009.

[^note-11]: For instance through an ordinal analysis as explained in Definition 3.4.

[^note-12]: For a detailed descriptions of natural deduction calculi see Prawitz 1965 or Troelstra & Schwichtenberg 2000. To achieve a more symmetric treatment of negation one can replace in the above axiomatic formulation the *principle of double negation* by the axiom $(B\land\neg B)\to A$ (to obtain intuitionist logic) and by the axiom $(\neg A\to (B\land\neg B))\to A$ (to obtain classical logic).

[^note-13]: The *Hauptsatz* states informally, according to Gentzen (1934/35: 177), that every purely logical proof can be transformed into a certain, by no means unique, normal form. One of the essential properties of such normal proofs is expressed by: “It does not make detours”.

[^note-14]: Though the crucial paper was published only in 1958, the central ideas of the “Dialectica Interpreation” go back to lectures Gödel presented at Yale in April of 1941. See Gödel 1942 in volume III of his *Collected Works*.

[^note-15]: Both Brouwer (1927) and Zermelo (1932), from dramatically different foundational perspectives, considered infinite proofs. Indeed, Brouwer asserted concerning his infinite proofs:

> These mental mathematical proofs that in general contain infinitely many terms must not be confused with their linguistic accompaniments, which are finite and necessarily inadequate, hence do not belong to mathematics. (Brouwer 1927: 460, note 8)[^brouwer-1927].

He added that this remark contains his “main argument against the claims of Hilbert’s metamathematics”.

[^note-16]: “Because of Gödel’s result consistency proofs now require a method that is finite (or constructive) but which is nevertheless very strong when formalized. People think this is impossible or at least unlikely and extremely difficult. The situation is somewhat similar to that of finding a new axiom that carries conviction and decides the continuum hypothesis”. (Takeuti 1975: 366)[^takeuti-1975]

[^note-17]: Terms have to be of appropriate type, e.g., in (2) below, *t* and *r* have to be of type 0 while in (3) *s* and *t* have to be of type $\sigma$ and $\tau$, respectively. The required typing should always be clear from the context.

[^note-18]: “Having proposed the fundamental conjecture, I concentrated on its proof and spent several years in an anguished struggle trying to resolve the problem day and night” (Takeuti 2003: 133)[^takeuti-2003].

[^note-19]: Below in $(\forall_2\bL)$ and $(\exists_2\rR)$, $A(a)$ is an arbitrary formula. The variable *U* in $(\forall_2\rR)$ and $(\exists_2\bL)$ is an eigenvariable of the respective inference, i.e., *U* is not to occur in the lower sequent.

[^note-20]: Meaning that it proves the same formulae as the system with cuts.

[^note-21]: In the 1970s Martin-Löf gave a normalization proof for a type theory with a universe that contained itself. The metatheory for this proof was basically a slight extension of the same type theory. Ironically, it turned out that the type theory was inconsistent.

[^note-22]: Below Con(T) and Proof$_\bT$ are arithmetized formalizations of the consistency of T and provability in T, respectively, as explained in Definition 1.3. $\Corner{F}$ denotes the Gödel number of a formula *F*. For every number *n*, $\bar{n}$ denotes the $n^{th}$ numeral, i.e., the term obtained from 0 by putting *n* successor function symbols in front of it.

[^note-23]: This is straightforward for languages allowing for quantifiers over sets of natural numbers, but for theories like **PA** one would have to add a new predicate symbol to the language.

[^note-24]: Recall that the class of arithmetical formulae is denoted by $\Pi^1_0$. These formulae can still contain free set variables which can be utilized to show that $(\Pi^1_0\Hy\bCA)_0=(\Pi^0_1\Hy\bCA)_0$.

[^note-25]: They were re-obtained in purely proof-theoretic ways (and generalized) by Feferman & Sieg (1981b).

[^note-26]: The attribute “reverse” comes from this additional objective: *When a theorem is proved from the right axioms, the axioms can be proved from the theorem.*

[^note-27]: Ironically, the counterexamples that come to mind as soon as one begins to think about it come from one of the main inventors of reverse mathematics.

[^note-28]: Using classical logic and just the connectives $\land$,$\lor$, $\neg$ and quantifiers $\forall$, $\exists$, any formula can be re-written in such a way that the negation sign occurs only in front of atomic formulas. A formula of the latter form is *P*-positive if *P* does not appear negated in it.

[^note-29]: The extension then has ordinals $\Omega_{\alpha}$ for all $\alpha\leq\nu$ and each ordinal of the form $\Omega_{\beta+1}$ gets furnished with its own collapsing function $\psi_{\!_{\Omega_{\beta+1}}}$.

[^note-30]: For a detailed account of the history of the proof theory of iterated inductive definitions see Buchholz et al. 1981.

[^note-31]: Upper bounds for (i) and (iii) are due to Takeuti (1967) while upper bounds for (iv) and (v) are owed to Takeuti and Yasugi (1973). The exacts bound in (iii) and (ii) are due to Pohlers (1977) and Buchholz (1977a), respectively. Other exact bounds involve the work of several people.

[^note-32]: The Hilbert project has produced three volumes of unpublished lecture notes and material that is no longer easily accessible, for example the original first edition of *Grundlagen der Geometrie* and that of the 1928 book of Hilbert and Ackermann. Associated with the edition and study of that material is also a rich secondary literature with papers, for example, by Mancosu (1998, 1999a) and Zach (2003, 2004).

[^note-33]: Proof-theoretic studies play an important role in areas such as temporal and modal logics with applications to software verification. Linear logic and the other substructural logics are being used successfully in linguistics. Here the computational aspects of the logics are important, and the development of proof systems for such logics aims to find systems that are both expressive and efficient. Our list of “Related Entries” below points the interested reader to information concerning these logics and their applications.

[^note-34]: The best-known systems are Coq, Isabel, HOL, and the more recent theorem prover Lean. Sieg has developed with collaborators and students the system AProS; see www.phil.cmu.edu/projects/apros.

### Notes to Appendix A

[^note-35]: 35. These four conditions correspond to the conditions $(\alpha)$ through $(\delta)$ of $\#71$ in Dedekind 1888; they are easily seen to be equivalent to the so-called Peano axioms. The *chain* of the system $\{1\}$ (with respect to the mapping $\varphi$ of N) is the intersection of all systems that contain 1 as an element and are closed under $\varphi$.

[^note-36]: 36. In Torretti 1978 [1984: 234], for example, one finds the following observation:

> … the completeness axiom is what nowadays one would call a metamathematical statement, though one of a rather peculiar sort, since the theory with which it is concerned includes Axiom V2 [i.e., the completeness axiom] itself.

[^note-37]: 37. We have modified the translation one finds in the *Collected Works*. In particular, logical expression stands for *logischer Ausdruck*, satisfy for *erfüllen*, domain of thought for *Denkbereich*, statement for *Aussage*, and proposition for *Satz*.

[^note-38]: 38. In *On the Infinite* Hilbert writes retrospectively:

> In particular, a contradiction discovered by Zermelo and Russell had, when it became known, a downright catastrophic effect in the world of mathematics. (Hilbert 1926: 375)[^hilbert-1926]

More can be learnt about Hilbert’s reaction at the time from various reports in 1902 and 1903 (cf. Peckhaus 1990: 57)[^peckhaus-1990].

[^note-39]: 39. One should keep in mind that the “existence of sets” was the central issue, and it was to be guaranteed by the consistency of an appropriate axiom system, a viewpoint shared by Poincaré. The latter was, on the whole, impressed by Hilbert’s novel approach.

[^note-40]: 40. See Mancosu 1999b. Not only the details of *Principia Mathematica* were of significance; on the contrary, the broad logicist outlook had a real impact on Hilbert. Hilbert’s notes for a course on *Set Theory* (from the summer term 1917) and his talk *Axiomatisches Denken* reveal a logicist direction in his work. In the latter essay Hilbert writes:

> The examination of consistency is an unavoidable task; thus, it seems to be necessary to axiomatize logic itself and *to show that number theory as well as set theory are just parts of logic*. (Hilbert 1918: 153)[^hilbert-1918].

If we try to achieve such a reduction to logic, Hilbert says at the very end of the set theory notes, “… we are facing one of the most difficult problems of mathematics”. (Hilbert 1917)[^hilbert-1917][^hilbert-1917-2]

[^note-41]: 41. This is reported in Dawson 1997 (p. 68) based on doc 023-73-04 in the Carnap Nachlass at the University of Pittsburgh.

[^note-42]: 42. Volume III of Gödel’s Collected Works contains a paper entitled “Vortrag über Vollständigkeit des Funktionenkalkül’s” that is taken to be the manuscript for his talk in Königsberg. However, Gödel’s talk was a contributed talk of just 20 minutes; only a small part of the paper could have been delivered.

[^note-43]: 43. The historical context and relevant details are presented in Sieg 2012.

[^note-44]: 44. More precisely, we define a function CODE by recursion on formulae that associates with each formula $\varphi$ a term in the language of $T$, which is also denoted by ${\Corner{\varphi}}$.

[^note-45]: 45. The representability conditions for PROOF are as follows: If PROOF$(D, \varphi)$ then $T \vdash \iproof(\Corner{D},\Corner{\varphi})$, and if NOT PROOF$(D,\varphi)$ then $T\vdash \neg \iproof(\Corner{D},\Corner{\varphi})$.

[^note-46]: 46. Note that *G* is, as Dawson put it (on p. 68), “an involved combinatorial statement expressed in the richer language of the system of *Principia Mathematica*” (or set theory). It is only after the “arithmetization of syntax” and the representation of the syntactic notions in elementary number theory that *G* is turned into an arithmetical statement; section 3 of Gödel 1931a. See the remarks below from Wang 1981 concerning this development after the Königsberg conference, and the further very detailed description of how *G* is equivalent to a Diophantine equation in section 8 of Gödel’s 1934 Princeton lectures and in Gödel 1938/9.

[^note-47]: 47. The letter, to the best of our knowledge, has not been published. One of the authors, Sieg, had received a copy from Chevalley’s daughter quite a few years ago.

[^note-48]: 48. As to the details of their interaction, see the Introductory Notes to Gödel’s correspondence with von Neumann and Herbrand, in volume V of the *Collected Works*. Gödel’s contrary perspective on the formalizability of finitist proofs is expressed not only at the end of his 1931 paper, but also in his letters to von Neumann and Herbrand, as well as in his contribution to the meeting of the Schlick Circle on 15 January 1931 and in the “*Nachtrag*” to his Königsberg remarks. In the latter he wrote:

> For a system in which all finitist (i.e., intuitionistically proper) forms of proof are formalized, a finitist consistency proof as sought by the formalists would be altogether impossible. However, it seems doubtful, whether one of the systems formulated up to now, say *Principia Mathematica*, is so comprehensive (or whether such a comprehensive system exists at all). (Gödel 1931b: 204)[^gödel-1931b].

### Notes to Appendix B

[^note-49]: 49. The usual recursion theorem is formulated for partial recursive functions but there is a version, due to Kleene (1958), that works for primitive recursive functions.

[^note-50]: 50. Accessible accounts can be found in Torkel Franzén’s book (2004a) and his paper (2004b).

### Notes to Appendix C

[^note-51]: 51. Brouwer did not include (Hyp 2) among the hypothesis. It expresses the “monotonicity” of the bar. Classically it’s rather superfluous but intuitionistically it is essential as Kleene observed: $\BI_{\igen}$ formulated without (Hyp 2) yields instances of excluded middle that are incompatible with Brouwer’s continuity principles (Kleene & Vesley 1965: 7.14)[^kleene-1965].

[^note-52]: 52. A bar *B* gives rise to a well-founded ordering $\prec$ on $\bbN^*$ where $t\prec s$ means that *t* is a node above *s* and $t\notin B$. Viewed in this way, $\BI_{\igen}$ is a principle of transfinite induction along $\prec$. For the implication $\BI_{\igen}\to{\bCA}$ to hold it is important that *B* can be of arbitrary complexity. Thus the moral drawable from this is that impredicative comprehension can be deduced from transfinite induction on impredicatively defined orderings.

[^note-53]: 53. Girard is also very skeptical about the intuitionistic setting of Spector’s interpretation: “all these topics have *nothing to do* with intuitionism” (Girard 1987: 479)[^girard-1987].

[^note-54]: 54. As a matter of clarification, cut free proofs are not allowed to contain other instances of $\tilde{\Omega}$.

### Notes to Appendix D

[^note-55]: 55. For more background information see Takeuti 1985: 259; Feferman 1989: 362, and Pohlers 1991: 374.

### Notes to Appendix E

[^note-56]: 56. For more details see Rathjen 1999a.

[^note-57]: 57. For more details see Rathjen 2015. As for the unprovability of $\Con(\PA)$ in **PA**, Gentzen (1943) explicitly states that his proof makes no appeal to the second incompleteness theorem.

[^note-58]: 58. In Rathjen 2015 the question is pondered whether the latter result could have been proved much earlier (from a technical as well as sociological point of view).

### Notes to Appendix F

[^note-59]: 59. For extensions and reflections see Sieg 1991.

[^note-60]: 60. Theorem F.4 can be extracted from Kreisel, Mints and Simpson (1975), Lopez-Escobar (1976) or Schwichtenberg (1977) and was certainly known to these authors.

[^english-nd]: The translations in this paper are ours, unless we explicitly refer to an English edition.

[^ackermann-1925]: Ackermann, Wilhelm, 1925, “Begründung des ‘tertium non datur’ mittels der Hilbertschen Theorie der Widerspruchsfreiheit”, *Mathematische Annalen*, 93: 1–36. doi:10.1007/BF01449946

[^aczel-1978]: Aczel, Peter, 1978, “The Type Theoretic Interpretation of Constructive Set Theory”, in A. MacIntyre, L. Pacholski, and J. Paris (eds.), *Studies in Logic and the Foundations of Mathematics, 96*, Amsterdam: North-Holland, pp. 55–66. doi:10.1016/S0049-237X(08)71989-X

[^arai-2003]: Arai, Toshiyasu, 2003, “Proof theory for theories of ordinals I: recursively Mahlo ordinals”, *Annals of Pure and Applied Logic*, 122(1–3): 1–85. doi:10.1016/S0168-0072(03)00020-4

[^arai-2004]: –––, 2004, “Proof theory for theories of ordinals II: $\Pi_3$-Reflection”, *Annals of Pure and Applied Logic*, 129(1–3): 39–92. doi:10.1016/j.apal.2004.01.001

[^arai-2020]: –––, 2020, *Ordinal Analysis with an Introduction to Proof Theory*, Singapore: Springer. doi.org/10.1007/978-981-15-6459-8

[^avigad-2007]: Avigad, Jeremy and Richard Zach, 2007, “The Epsilon Calculus”, *Stanford Encyclopedia of Philosophy* (Fall 2007), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/fall2007/entries/epsilon-calculus/](https://plato.stanford.edu/archives/fall2007/entries/epsilon-calculus/)>

[^awodey-2012]: Awodey, Steve, 2012, “Homotopy Type Theory and Univalent Foundations”, Slides from a talk at Carnegie Mellon, March 2012. [[ Awodey 2012 available online](https://www.andrew.cmu.edu/user/awodey/hott/CMUslides.pdf)]

[^bachmann-1950]: Bachmann, Heinz, 1950, “Die Normalfunktionen und das Problem der ausgezeichneten Folgen von Ordinalzahlen”, *Vierteljahrsschrift der Naturforschenden Gesellschaft Zürich*, 95(2): 115–147. [[Bachmann 1950 available online](http://www.ngzh.ch/archiv/1950_95/95_2/95_14.pdf)]

[^barwise-1975]: Barwise, Jon, 1975, *Admissible Sets and Structures: An Approach to Definability Theory*, (Perspectives in Mathematical Logic, 7), Berlin: Springer.

[^barwise-1977]: ––– (ed.), 1977, *Handbook of Mathematical Logic*, ( Studies in Logic and the Foundations of Mathematics, 90), Amsterdam: North Holland.

[^bernays-1918]: Bernays, Paul, 1918, *Beiträge zur axiomatischen Behandlung des Logik-Kalküls*, Habilitationsschrift, Göttingen, reprinted in Ewald and Sieg 2013: 222–272.

[^bernays-1921]: –––, 1921, “Disposition for Hilbert’s Seminar: MI”, published in Sieg 2013: 123–124.

[^bernays-1922]: –––, 1922 [1998], “Über Hilberts Gedanken zur Grundlegung der Mathematik”, *Jahresberichte der Deutschen Mathematiker-Vereinigung*, 31: 10–19. Translated in Mancosu 1998: 215–222.

[^bernays-1927]: –––, 1927, “Probleme der theoretischen Logik”, *Unterrichtsblätter für Mathematik und Naturwissenschaften*, 33: 369–377.

[^bernays-1935]: –––, 1935, “Hilberts Untersuchungen über die Grundlagen der Arithmetik”, in Hilbert 1935: 196–216. doi:10.1007/978-3-662-38452-7_14

[^bernays-1965]: –––, 1965, “Betrachtungen zum Sequenzenkalkül”, in Anna-Teresa Tymieniecka and C. Parsons (eds.), *Contributions to Logic and Methodology, in honor of J. M. Bochenski*, Amsterdam: North-Holland, 1–44. doi:10.1016/B978-1-4832-3159-4.50007-1

[^bernays-1976]: –––, 1976, *Abhandlungen zur Philosophie der Mathematik*, Darmstadt: Wissenschaftliche Buchgesellschaft.

[^bernstein-1919]: Bernstein, Felix, 1919, “Die Mengenlehre Georg Cantors und der Finitismus”, *Jahresberichte der Deutschen Mathematiker-Vereinigung*, 28: 63–78.

[^bishop-1967]: Bishop, Errett, 1967, *Foundations of Constructive Analysis*, New York: McGraw-Hill.

[^brouwer-1927]: Brouwer, Luitzen Egbertus Jan, 1927, “Über Definitionsbereiche von Funktionen”, Mathematische Annalen, 97: 60–75. doi:10.1007/BF01447860 English translation in van Heijenoort 1967: 446–463.

[^brouwer-1928]: –––, 1928 [1967], “Intuitionistische Betrachtungen über den Formalismus”, *Koninklijke Akademie van wetenschappen te Amsterdam, Proceedings of the section of sciences*, 31: 374–379. English translation in van Heijenoort 1967: 490–492.

[^buchholz-1977a]: Buchholz, Wilfried, 1977a, *Eine Erweiterung der Schnitteliminationsmethode*, Habilitationsschrift, München.

[^buchholz-1977b]: –––, 1977b, “A New System of Proof-Theoretic Ordinal Functions”, *Annals of Pure and Applied Logic*, 32: 195–207. doi:10.1016/0168-0072(86)90052-7

[^buchholz-1987]: –––, 1987, “An independence result for $(\Pi^1_1$-CA+BI)”, *Annals of Pure and Applied Logic*, 33: 131–155. doi:10.1016/0168-0072(87)90078-9

[^buchholz-1993]: –––, 1993, “A Simplified Version of Local Predicativity”, in Peter Aczel, Harold Simmons, and Stanley S. Wainer (eds.), *Proof Theory: A selection of papers from the Leeds Proof Theory Programme 1990*, Cambridge: Cambridge University Press, 115–147. doi:10.1017/CBO9780511896262.006

[^buchholz-1997]: –––, 1997, “Explaining Gentzen’s Consistency Proof Within Infinitary Proof Theory”, in Georg Gottlob, Alexander Leitsch, and Daniele Mundici (eds.), *KGC ’97 Proceedings of the 5th Kurt Gödel Colloquium on Computational Logic and Proof Theory,*, Lecture Notes in Computer Science 1289, Berlin: Springer-Verlag, pp. 4–17. doi:10.1007/3-540-63385-5_29

[^buchholz-2015]: –––, 2015, “On Gentzen’s First Consistency Proof for Arithmetic” in Kahle and Rathjen 2015: 63–87. doi:10.1007/978-3-319-10103-3_4

[^buchholz-1981]: Buchholz, Wilfried, Solomon Feferman, Wolfram Pohlers, and Wilfried Sieg, 1981, *Iterated Inductive Definitions and Subsystems of Analysis: Recent Proof-Theoretical Studies*, (Lecture Notes in Mathematics, 897), Berlin: Springer. doi:10.1007/BFb0091894

[^buchholz-1988]: Buchholz, Wilfried and Kurt Schütte, 1988, *Proof Theory of Impredicative Subsystems of Analysis*, Naples: Bibliopolis.

[^buchholz-1990]: Buchholz, Wilfried and Wilfried Sieg, 1990, “A Note on Polynomial Time Computable Arithmetic”, in Sieg 1990: 51–56. doi:10.1090/conm/106/1057815

[^buchholz-1987-2]: Buchholz, Wilfried and Stan Wainer, 1987, “Provable Computable Functions and the Fast Growing Hierarchy”, in Simpson 1987: 179–198. doi:10.1090/conm/065/891248

[^burr-2000]: Burr, Wolfgang, 2000, “Functional Interpretation of Aczel’s Constructive Set Theory”, *Annals of Pure and Applied Logic*, 104: 31–73. doi:10.1016/S0168-0072(00)00007-5

[^buss-1986]: Buss, Samuel R., 1986, *Bounded Arithmetic*, Napoli: Bibliopolis. [[Buss 1986 draft available online](http://math.ucsd.edu/~sbuss/ResearchWeb/BAthesis)]

[^cantor-1872]: Cantor, Georg, 1872, “Ueber die Ausdehnung eines Satzes aus der Theorie der trigonometrischen Reihen”, *Mathematische Annalen*, 5: 123–132. [[Cantor 1872 available online](http://eudml.org/doc/156562)]

[^cantor-1897]: –––, 1897, “Beiträge zur Begründung der transfiniten Mengenlehre II”, *Mathematische Annalen*, 49(2): 207–246. doi:10.1007/BF01444205

[^carnap-1934]: Carnap, Rudolf, 1934, *Logische Syntax der Sprache*, Wien: Springer. doi:10.1007/978-3-662-25376-2

[^church-1936]: Church, Alonzo, 1936, “An Unsolvable Problem of Elementary Number Theory”, *American Journal of Mathematics*, 58(2): 345–363. doi:10.2307/2371045

[^church-1936-2]: Church, Alonzo and S.C. Kleene, 1936, “Formal Definitions in the Theory of Ordinal Numbers”, *Fundamenta Mathematicae*, 28(1): 11–21. [[Church and Kleene 1936 available online](http://pldml.icm.edu.pl/pldml/element/bwmeta1.element.bwnjournal-article-fmv28i1p3bwm)]

[^cichon-1983]: Cichon, E.A., 1983, “A Short Proof of Two Recently Discovered Independence Results Using Recursion Theoretic Methods”, *Proceedings of the American Mathematical Society*, 87(4): 704–706. doi:10.1090/S0002-9939-1983-0687646-0

[^curry-1930]: Curry, Haskell B., 1930 “Grundlagen der Kombinatorischen Logik”, *American Journal of Mathematics*, 52(3): 509–536, 52(4): 789–834. doi:10.2307/2370619 (part 1) doi:10.2307/2370716 (part 2)

[^dawson-1997]: Dawson, John W., 1997, *Logical Dilemmas: The Life and Work of Kurt Gödel*, Wellesley, MA: A.K. Peters.

[^dedekind-1872]: Dedekind, Richard, 1872, *Stetigkeit und irrationale Zahlen*, Braunschweig: Vieweg. Translated by Wooster Woodruff Beman as “Continuity and Irrational Numbers”, in *Essays on the Theory of Numbers*, Chicago: Open Court, 1901; reprinted with corrections by William Ewald in Ewald 1996: 765–779 (vol. 2).

[^dedekind-1888]: –––, 1888, *Was sind und was sollen die Zahlen*, Braunschweig: Vieweg. Translated by Wooster Woodruff Beman as “The Nature and Meaning of Numbers”, in *Essays on the Theory of Numbers*, Chicago: Open Court, 1901; reprinted with corrections by William Ewald in Ewald 1996: 787–833 (vol. 2).

[^dedekind-1890]: –––, 1890 [1967], “Letter to H. Keferstein”, Cod. Ms. Dedekind III, I, IV (1890). Printed in Sinaceur 1974: 270–278. Translated in van Heijenoort 1967: 98–103.

[^dedekind-1932]: –––, 1932, *Gesammelte mathematische Werke*, Volume 3, Robert Fricke, Emmy Noether, and Öystein Ore (eds), Braunschweig: Vieweg. [[Dedekind 1932 available online](http://resolver.sub.uni-goettingen.de/purl?PPN23569441X)]

[^diestel-1997]: Diestel, Reinhard, 1997 *Graph Theory*, New York, Berlin, Heidelberg: Springer. doi:10.1007/978-3-662-53622-3 (doi is for the fifth edition but page numbers are from the first edition).

[^diller-2008]: Diller, Justus, 2008, “Functional Interpretations of Constructive Set Theory in All Finite Types”, *Dialectica*, 62(2): 149–177. doi:10.1111/j.1746-8361.2008.01133.x

[^diller-1975]: Diller, Justus and Gert H. Müller (eds), 1975, *$\models$ ISILCProof Theory Symposium: Proceedings of the International Summer Institute and Logic Colloquium, Kiel 1974*, (Lecture Notes in Mathematics, 500), Berlin: Springer.

[^dugac-1976]: Dugac, Pierre, 1976, *Richard Dedekind et les fondements des mathématiques*, Paris: VRIN.

[^ewald-1996]: Ewald, William (ed.), 1996, *From Kant to Hilbert: A Source Book in the Foundations of Mathematics*, Oxford: Oxford University Press, two volumes.

[^ewald-2013]: Ewald, William and Wilfried Sieg (eds.), 2013, *David Hilbert’s Lectures on the Foundations of Arithmetic and Logic 1917–1933*, Heidelberg: Springer. doi:10.1007/978-3-540-69444-1

[^feferman-1962]: Feferman, Solomon, 1962, “Transfinite Recursive Progressions of Axiomatic Theories”, *Journal of Symbolic Logic*, 27(3): 259–316. doi:10.2307/2964649

[^feferman-1964]: –––, 1964, “Systems of Predicative Analysis”, *Journal of Symbolic Logic*, 29(1): 1–30. doi:10.2307/2269764

[^feferman-1968]: –––, 1968, “Autonomous Transfinite Progressions and the Extent of Predicative Mathematics”, in *Logic, Methodology, and Philosophy of Science III*, Proceedings of the Third International Congress, Amsterdam, 1967, (Studies in Logic and the Foundations of Mathematics, Volume 52), Amsterdam: North-Holland, 121–135. doi:10.1016/S0049-237X(08)71190-X

[^feferman-1970a]: –––, 1970a, “Hereditarily Replete Functionals Over the Ordinals”, in Kino, Myhill, and Vesley 1970: 289–301. doi:10.1016/S0049-237X(08)70760-2

[^feferman-1970b]: –––, 1970b, “Formal Theories for Transfinite Inductive Definitions and Some Subsystems of Analysis”, in Kino, Myhill, and Vesley 1970: 303–326. doi:10.1016/S0049-237X(08)70761-4

[^feferman-1975]: –––, 1975, “A Language and Axioms for Explicit Mathematics”, in *Algebra and Logic Papers from the 1974 Summer Research Institute of the Australian Mathematical Society, Monash University, Australia*, (Lecture Notes in Mathematics, 450), John Newsome Crossley (ed.), Berlin: Springer, 87–139. doi:10.1007/BFb0062852

[^feferman-1979]: –––, 1979, “Constructive Theories of Functions and Classes”, in Maurice Boffa, Dirk van Dalen, Kenneth McAloon (eds.), *Logic Colloquium ’78: Proceedings of the colloquium held in Mons, 1 August 1978*, Amsterdam: North-Holland, 159–224. doi:10.1016/S0049-237X(08)71625-2

[^feferman-1987]: –––, 1987, “Proof Theory: A Personal Report”, in Takeuti 1987: 445–485.

[^feferman-1988]: –––, 1988, “Hilbert’s Program Relativized: Proof-Theoretical and Foundational Reductions”, *Journal of Symbolic Logic*, 53(2): 364–384. doi:10.1017/S0022481200028310

[^feferman-1989]: –––, 1989, “Remarks for ‘The Trends in Logic’”, in R. Ferro, C. Bonotto, S. Valentini, and A. Zanardo (eds), *Logic Colloquium ‘88: Proceedings of the Colloquium held in Padova Italy 22–31 August 1988*, (Studies in Logic and the Foundations of Mathematics, 127), Amsterdam: North-Holland, 361–363. doi:10.1016/S0049-237X(08)70276-3

[^feferman-1998]: –––, 1998, *In the Light of Logic*, Oxford: Oxford University Press.

[^feferman-2000]: –––, 2000, “Does Reductive Proof Theory Have a Viable Rationale?”, *Erkenntnis*, 53(1–2): 63–96. doi:10.1023/A:1005622403850

[^feferman-1981a]: Feferman, Solomon and Wilfried Sieg, 1981a, “Inductive Definitions and Subsystems of Analysis”, in Buchholz, Feferman, Pohlers, and Sieg 1981: 16–77. doi:10.1007/BFb0091895

[^feferman-1981b]: –––, 1981b, “Proof Theoretic Equivalences between Classical and Constructive Theories for Analysis”, in Buchholz, Feferman, Pohlers, and Sieg 1981: 78–142. doi:10.1007/BFb0091896

[^feferman-2010]: Feferman, Solomon and Thomas Strahm, 2010, “Unfolding Finitist Arithmetic”, *Review of Symbolic Logic*, 3(4): 665–689. doi:10.1017/S1755020310000183

[^ferreira-1990]: Ferreira, Fernando, 1990, “Polynomial Time Computable Arithmetic”, in Sieg 1990: 137–156. doi:10.1090/conm/106/1057819

[^ferreirós-2008]: Ferreirós, José, 2008, *Labyrinth of Thought: A History of Set Theory and Its Role in Modern Mathematics*, second revised edition, Basel: Birkhäuser. First edition was published in 1999. doi:10.1007/978-3-7643-8350-3

[^franks-2009]: Franks, Curtis, 2009, *The Autonomy of Mathematical Knowledge: Hilbert’s Program Revisited*, Cambridge: Cambridge University Press. doi:10.1017/CBO9780511642098

[^franzén-2004a]: Franzén, Torkel, 2004a, *Inexhaustability. A non-exhaustive treatment*, (Lecture Notes in Logic 16), Association for Symbolic Logic, Wellesley, MA: A.K. Peters.

[^franzén-2004b]: –––, 2004b, “Transfinite Progressions: a Second Look at Completeness”, *Bulletin of Symbolic Logic*, 10(3): 367–389. doi:10.2178/bsl/1102022662

[^frege-1879]: Frege, Gottlob, 1879, *Begriffsschrift: eine der arithmetischen nachgebildete Formelsprache des reinen Denkens*, Halle: Verlag von Louis Nebert.

[^friedman-1970]: Friedman, Harvey, 1970, “Iterated Inductive Definitions and $\Sigma^1_2$-AC”, in Kino, Myhill, and Vesley 1970: 435–442. doi:10.1016/S0049-237X(08)70769-9

[^friedman-1987]: Friedman, Harvey, Neil Robertson, and Paul Seymour, 1987, “The Metamathematics of the Graph Minor Theorem”, in Simpson 1987: 229–261. doi:10.1090/conm/065/891251

[^friedman-1995]: Friedman, Harvey and Michael Sheard, 1995, “Elementary Descent Recursion and Proof Theory”, *Annals of Pure and Applied Logic*, 71(1): 1–45. doi:10.1016/0168-0072(94)00003-L

[^gabriel-1980]: Gabriel, Gottfried, Friedrich Kambartel, and Christian Thiel (eds.), 1980, *Gottlob Freges Briefwechsel mit D. Hilbert, E. Husserl, B. Russell, sowie ausgewählte Einzelbriefe Freges*, (Philosophische Bibliothek, Band 321), Hamburg: Felix Meiner Verlag.

[^ganesalingam-2017]: Ganesalingam, Mohan and W. Timothy Gowers, 2017, “A Fully Automatic Theorem Prover with Human-Style Output”, *Journal of Automated Reasoning*, 58(2): 253–291. doi:10.1007/s10817-016-9377-1

[^gentzen-1932]: Gentzen, Gerhard, 1932, “Über die Existenz unabhängiger Axiomensysteme zu unendlichen Satzsystemen”, *Mathematische Annalen*, 107: 329–350. English translation, “On the Existence of Independent Axiom Systems for Infinite Sentence Systems”, in Gentzen 1969: 29–52. doi:10.1007/BF01448897 (de) doi:10.1016/S0049-237X(08)70820-6 (en)

[^gentzen-1933]: –––, [1933] 1974, “Über das Verhältnis zwischen intuitionistischer und klassischer Arithmetik”, *Archiv für mathematische Logik und Grundlagenforschung*, 16(3–4): 119–132. Written in 1933, but withdrawn from publication after the appearence of Gödel 1933. English translation, “On the Relation Between Intuitionist and Classical Arithmetic”, in Gentzen 1969: 53–67. doi:10.1007/BF02015371 (de) doi:10.1016/S0049-237X(08)70821-8 (en)

[^gentzen-1934]: –––, 1934/35, “Untersuchungen über das logische Schließen I,II”, *Mathematische Zeitschrift*, 39: 176–210, 405–431. English translation, “Investigations into Logical Deduction”, in Gentzen 1969: 68–131. doi:10.1007/BF01201353 (I, de) doi:10.1007/BF01201363 (II, de) doi:10.1016/S0049-237X(08)70822-X (en)

[^gentzen-1936]: –––, 1936, “Die Widerspruchsfreiheit der reinen Zahlentheorie”, *Mathematische Annalen*, 112: 493–565. English translation, “The Consistency of Elementary Number Theory”, in Gentzen 1969: 132–213. doi:10.1007/BF01565428 (de) doi:10.1016/S0049-237X(08)70823-1 (en)

[^gentzen-1938a]: –––, 1938a, “Die gegenwärtige Lage in der mathematischen Grundlagenforschung”, *Forschungen zur Logik und zur Grundlegung der exakten Wissenschaften*, Neue Folge 4, Leipzig: Hirzel, 5–18. English translation, “The Present State of Research into the Foundations of Mathematics”, in Gentzen 1969: 234–251. doi:10.1016/S0049-237X(08)70826-7 (en)

[^gentzen-1938b]: –––, 1938b, “Neue Fassung des Widerspruchsfreiheitsbeweises für die reine Zahlentheorie”, *Forschungen zur Logik und zur Grundlegung der exacten Wissenschaften*, Neue Folge 4, Leipzig: Hirzel, 19–44. English translation, “New Version of the Consistency Proof for Elementary Number Theory”, in Gentzen 1969: 252–286. doi:10.1016/S0049-237X(08)70827-9

[^gentzen-1943]: –––, 1943, “Beweisbarkeit und Unbeweisbarkeit von Anfangsfällen der transfiniten Induktion in der reinen Zahlentheorie”, *Mathematische Annalen*, 119(1): 140–161. English translation, “Provability and Nonprovability of Restricted Transfinite Induction in Elementary Number Theory”, in Gentzen 1969: 287–308. doi:10.1007/BF01564760 (de) doi:10.1016/S0049-237X(08)70828-0 (en)

[^gentzen-1945]: –––, 1945, *Stenogramm von G. Gentzen*, Transcription by H. Kneser and H. Urban, 13 pages.

[^gentzen-1969]: –––, 1969, *The Collected Papers of Gerhard Gentzen*, (Studies in Logic and the Foundations of Mathematics, 55), translated and edited by M.E. Szabo, Amsterdam: North-Holland.

[^gentzen-1974]: –––, 1974, “Der erste Widerspruchsfreiheitsbeweis für die klassische Zahlentheorie”, *Archiv für Mathematische Logik und Grundlagenforschung*, 16(3–4): 97–118. doi:10.1007/BF02015370

[^girard-1971]: Girard, Jean-Yves, 1971, *Une extension de l’interpretation de Gödel a l’analyse et son application a l’élimination des coupures dans l’analyse et la théorie des types*, in J.E. Fenstad (ed.), 1971, *Proceedings of the Second Scandinavian Logic Symposium*, (Studies in Logic and the Foundations of Mathematics, 63), Amsterdam: North-Holland, 63–92. doi:10.1016/S0049-237X(08)70843-7

[^girard-1987]: –––, 1987, *Proof Theory and Logical Complexity, Volume 1*, Napoli: Bibliopolis.

[^gödel-1929]: Gödel, Kurt, 1929 [1986], *Über die Vollständigkeit des Logikkalküls*, Dissertation, Wien, also in Gödel 1986: 60–101.

[^gödel-1931a]: –––, 1931a, “Über formal unentscheidbare Sätze der Principia mathematica und verwandter Systeme I”, *Monatshefte für Mathematik und Physik*, 38: 173–198. doi:10.1007/BF01700692

[^gödel-1931b]: –––, 1931b [1986], “Nachtrag [to the Diskussion zur Grundlegung der Mathematik]”, *Erkenntnis*, 2: 149–151 (the full *Diskussion* starts on 135). Reprinted in Gödel 1986: 200–205. doi:10.1007/BF02028146 (de)

[^gödel-1933]: –––, 1933, “Zur intuitionistischen Arithmetik und Zahlentheorie”, *Ergebnisse eines mathematischen Kolloquiums*, 4: 34–38, in English translation in Gödel 1986.

[^gödel-1934]: –––, 1934, “On Undecidable Propositions of Formal Mathematical Systems”, Princeton lecture notes, in Gödel 1986: 346–371.

[^gödel-1938]: –––, 1938/9, “On Undecidable Diophantine Propositions”, Manuscript for a lecture written 1938 or 1939, in Gödel 1995: 164–175.

[^gödel-1942]: –––, 1942, “In what sense is intuitionistic logic constructive?”, in Gödel 1995: 189–200.

[^gödel-1958]: –––, 1958, “Über eine bisher noch nicht benützte Erweiterung des finiten Standpunktes”, *Dialectica*, 12(3–4): 280–287. doi:10.1111/j.1746-8361.1958.tb01464.x

[^gödel-nd]: –––, *Collected Works*, Oxford: Oxford University Press. Includes both the German originals with English translations, Solomon Feferman, Editor-in-Chief.

[^gödel-1986]: 1986, *Volume I: Publications 1929–1936*, Solomon Feferman, John W. Dawson, Jr., Stephen C. Kleene, Gregory H. Moore, Robert M. Solovay, and Jean van Heijenoort (eds).

[^gödel-1990]: 1990, *Volume II: Publications 1938–1974*, Solomon Feferman, John W. Dawson, Jr., Stephen C. Kleene, Gregory H. Moore, Robertt M. Solovay, and Jean van Heijenoort (eds).

[^gödel-1995]: 1995, *Volume III: Unpublished Essays and Lectures*, Solomon Feferman, John W. Dawson, Jr., Warren Goldfarb, Charles Parsons, and Robert M. Solovay (eds).

[^gödel-2003]: 2003, *Volume IV: Correspondence, A–G*, Solomon Feferman, John W. Dawson, Warren Goldfarb, Charles Parsons, and Wilfred Sieg (eds).

[^goodstein-1944]: Goodstein, R.L., 1944, “On the Restricted Ordinal Theorem”, *Journal of Symbolic Logic*, 9(2): 33–41. doi:10.2307/2268019

[^gowers-2016]: Gowers, Timothy (with Alexander Diaz-Lopez), 2016, “Interview with Sir Timothy Gowers”, *Notices of the American Mathematical Society*, 63(9): 1026–1028. doi:10.1090/noti1432

[^griffor-1994]: Griffor, Edward and Michael Rathjen, 1994, “The Strength of some Martin-Löf Type Theories”, *Archive for Mathematical Logic*, 33: 347–385.

[^hallett-2013]: Hallett, Michael, 2013, “Introduction to Hilbert’s 1931 Göttingen Lecture”, in Ewald and Sieg 2013: 983–984.

[^hallett-2013-2]: Hallett, Michael and Wilfried Sieg, 2013, “Introduction to the Kneser Mitschriften”, in Ewald and Sieg 2013: 565–576.

[^hardy-1904]: Hardy, G.H., 1904, “A Theorem Concerning the Infinite Cardinal Numbers”, *Quarterly Journal of Mathematics*, 35: 87–94.

[^harrison-2009]: Harrison, John, 2009, *Handbook of Practical Logic and Automated Reasoning*, Cambridge: Cambridge University Press. doi:10.1017/CBO9780511576430

[^herbrand-1930]: Herbrand, Jacques, 1930, *Recherches sur la théorie de la démonstration*, Dissertation, University of Paris. [[Herbrand 1930 available online](http://www.numdam.org/item?id=THESE_1930__110__1_0)]

[^herbrand-1931]: –––, 1931, “Sur la non-contradiction de l’arithmétique”, *Crelles Journal für die reine und angewandte Mathematik*, 166: 1–8. doi:10.1515/crll.1932.166.1

[^heyting-1930]: Heyting, Arend, 1930, “Die formalen Regeln der intuitionistischen Logik und Mathematik”, (*Sitzungsberichte der Preußischen Akademie der Wissenschaften, Physikalisch-Mathematische Klasse*), Berlin.

[^heyting-1959]: ––– (ed.), 1959, *Constructivity in Mathematics, Proceedings of the Colloquium held at Amsterdam, 1957*, (Studies in Logic and the Foundations of Mathematics), Amsterdam: North-Holland Publishing Company.

[^hilbert-1898]: Hilbert, David, 1898/99, *Grundlagen der Euklidischen Geometrie*, Lecture Notes by H. von Schaper, MI. Printed in Hilbert 2004: 302–395.

[^hilbert-1899]: –––, 1899, “Grundlagen der Geometrie”, in Festschrift zur Feier der Enthüllung des Gauss-Weber Denkmals in Göttingen, Teubner 1899: 1–92.

[^hilbert-1900a]: –––, 1900a, “Über den Zahlbegriff”, *Jahresberichte der Deutschen Mathematiker-Vereinigung*, 8: 180–194. English translation in Ewald 1996: 1089–1095. [[Hilbert 1900a available online](https://eudml.org/doc/144659)]

[^hilbert-1900b]: –––, 1900b, “Mathematische Probleme”, *Nachrichten der Königlichen Gesellschaft der Wissenschaften zu Göttingen*, 253–297, translated in Ewald 1996: 1096–1105.

[^hilbert-1904]: –––, 1904, *Zahlbegriff und Quadratur des Kreises*, Lecture notes by M. Born.

[^hilbert-1905]: –––, 1905 [1967], “Über die Grundlagen der Logik und der Arithmetik”, in *Verhandlungen des Dritten Internationalen Mathematiker-Kongresses*, Teubner, 174–185. Translated in van Heijenoort 1967: 129–138.

[^hilbert-1917]: –––, 1917, *Mengenlehre*, Lecture notes by M. Goeb, MI.

[^hilbert-1917-2]: –––, 1917–18, *Prinzipien der Mathematik*, Lecture notes by P. Bernays, MI. Published in Ewald and Sieg 2013: 59–221.

[^hilbert-1918]: –––, 1918, “Axiomatisches Denken”, *Mathematische Annalen*, 78: 405–415. doi:10.1007/BF01457115 Reprinted in Hilbert 1935: 146–156.

[^hilbert-1922]: –––, 1922, “Neubegründung der Mathematik”, *Abhandlungen aus dem mathematischen Seminar der Hamburgischen Universität*, 1: 157–177; translated in Ewald 1996: 1117–1134.

[^hilbert-1922-2]: –––, 1922–23, *Logische Grundlagen der Mathematik*, Lecture notes by P. Bernays, SUB 567.

[^hilbert-1923]: –––, 1923, “Die logischen Grundlagen der Mathematik”, *Mathematische Annalen*, 88(1–2): 151–165; translated in Ewald 1996: 1136–1148. doi:10.1007/BF01448445 (de)

[^hilbert-1926]: –––, 1926, “Über das Unendliche”, *Mathematische Annalen*, 95: 161–190. doi:10.1007/BF01206605 English translation in van Heijenoort 1967: 367–392.

[^hilbert-1927]: –––, 1927 [1967], “Die Grundlagen der Mathematik”, Vortrag gehalten auf Einladung des Mathematischen Seminars im Juli 1927 in Hamburg, published in *Abhandlungen aus dem mathematischen Seminar der Hamburgischen Universität*, 6(1/2): 65–85; translated in van Heijenoort 1967: 464–479. doi:10.1007/BF02940602 (de)

[^hilbert-1928]: –––, 1928, “Probleme der Grundlegung der Mathematik”, *Mathematische Annalen*, 102: 1–9. Reprint, with emendations and additions, of paper with the same title, published in Atti del Congresso internazionale dei matematici, Bologna 1928, 135–141. doi:10.1007/BF01782335 (original)

[^hilbert-1931a]: –––, 1931a, “Die Grundlegung der elementaren Zahlenlehre”, *Mathematische Annalen*, 104: 485–494; translated in Ewald 1996: 1148–1157. doi:10.1007/BF01457953 (de)

[^hilbert-1931b]: –––, 1931b, “Beweis des tertium non datur”, *Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen, Mathematisch-physikalische Klasse*, 120–125.

[^hilbert-1935]: –––, 1935, *Dritter Band: Analysis · Grundlagen der Mathematik · Physik Verschiedenes*, of his *Gesammelte Abhandlungen*, volume 3, Berlin: Springer. doi:10.1007/978-3-662-38452-7

[^hilbert-1891]: –––, *David Hilbert’s Lectures on the Foundations of Mathematics and Physics, 1891–1933*, Berlin: Springer.

[^hilbert-2004]: 2004, volume 1, *David Hilbert’s Lectures on the Foundations of Geometry, 1891–1902*, Michael Hallett and Ulrich Majer (eds).

[^hilbert-2009]: 2009, volume 5, *David Hilbert’s Lectures on the Foundations of Physics, 1915–1927*, Tilman Sauer and Ulrich Majer (eds). doi:10.1007/b12915

[^hilbert-2013]: 2013, volume 3, *David Hilbert’s Lectures on the Foundations of Arithmetic and Logic, 1917–1933*, Ewald and Sieg (eds).

[^hilbert-1928-2]: Hilbert, David and Wilhelm Ackermann, 1928, *Grundzüge der theoretischen Logik*, Berlin: Springer.

[^hilbert-nd]: Hilbert, David and Paul Bernays, *Grundlagen der Mathematik*, Berlin: Springer, with revisions detailed in foreword by Bernays.

[^hilbert-1934]: 1934, Volume 1, second edition, 1968

[^hilbert-1939]: 1939, Volume II, second edition, 1970

[^howard-1963]: Howard, William A., 1963, “The Axiom of Choice ($\Sigma^1_1$-$\mathrm{AC}_{01}$), Bar Induction and Bar Recursion”, in *Reports of the Seminar on the Foundations of Analysis*, Stanford,(mimeographed), Mathematical Sciences Library, Stanford University, 2.1–2.44.

[^howard-1968]: –––, 1968, “Functional Interpretation of Bar Induction by Bar Recursion”, *Compositio Mathematica*, 20: 107–124. [[Howard 1968 available online](https://eudml.org/doc/88970)]

[^howard-1972]: –––, 1972, “A System of Abstract Constructive Ordinals”, *Journal of Symbolic Logic*, 37(2): 355–374. doi:10.2307/2272979

[^jäger-1980]: Jäger, Gerhard, 1980, “Beweistheorie von KPN”, *Archiv für Mathematische Logik und Grundlagenforschung*, 20(1–2): 53–63. doi:10.1007/BF02011138

[^jäger-1982]: –––, 1982, “Zur Beweistheorie der Kripke-Platek-Mengenlehre über den natürlichen Zahlen”, *Archiv für Mathematische Logik und Grundlagenforschung*, 22(3–4): 121–139. doi:10.1007/BF02297652

[^jäger-1983]: –––, 1983, “A well-ordering proof for Feferman’s theory $T_0$”, *Archiv für Mathematische Logik und Grundlagenforschung*, 23(1): 65–77. doi:10.1007/BF02023014

[^jäger-1986]: –––, 1986, *Theories for Admissible Sets: A Unifying Approach to Proof Theory*, Napoli: Bibliopolis.

[^jäger-1982-2]: Jäger, Gerhard and Wolfram Pohlers, 1982, “Eine beweistheoretische Untersuchung von $\Delta^1_2$-CA+BI und verwandter Systeme”, *Sitzungsberichte der Bayerischen Akademie der Wissenschaften, Mathematisch–Naturwissenschaftliche Klasse*, 1–28.

[^jäger-2018]: Jäger, Gerhard and Wilfried Sieg (eds), 2018, *Feferman on Foundations: Logic, Mathematics, Philosophy*, (Outstanding Contributions to Logic, 13), Cham: Springer. doi:10.1007/978-3-319-63334-3

[^kahle-2015]: Kahle, Reinhard and Michael Rathjen (eds), 2015, *Gentzen’s Centenary: The Quest for Consistency*, Cham: Springer. doi:10.1007/978-3-319-10103-3

[^kanamori-1978]: Kanamori, A. and M. Magidor, 1978,“The Evolution of Large Cardinal Axioms in Set Theory”, in Gert H. Müller and Dana Scott (eds.), *Higher Set Theory*, (Lecture Notes in Mathematics, 669), Berlin: Springer, pp. 99–275. doi:10.1007/BFb0103104

[^kino-1970]: Kino, A., J. Myhill, and R. Vesley (eds), 1970, *Intuitionism and Proof Theory: Proceedings of the Summer Conference at Buffalo N.Y. 1968*, (Studies in Logic and the Foundations of Mathematics, 60), Amsterdam: North-Holland.

[^kirby-1982]: Kirby, Laurie and Jeff Paris, 1982, “Accessible Independence Results for Peano Arithmetic”, *Bulletin of the London Mathematical Society*, 14: 285–293. doi:10.1112/blms/14.4.285

[^kleene-1938]: Kleene, Stephen Cole, 1938, “On Notations for Ordinal Numbers”, *Journal of Symbolic Logic*, 3(4): 150–155. doi:10.2307/2267778

[^kleene-1958]: –––, 1958, “Extension of an Effectively Generated Class of Functions by Enumeration”, *Colloquium Mathematicum*, 6: 67–78. doi:10.4064/cm-6-1-67-78

[^kleene-1959]: –––, 1959, “Countable Functionals”, in Heyting 1959: 81–100.

[^kleene-1965]: Kleene, Stephen Cole and Richard Eugene Vesley, 1965, *The Foundations of Intuitionistic Mathematics, Especially in Relation to Recursive Functions*, Amsterdam: North Holland.

[^kohlenbach-2007]: Kohlenbach, Ulrich, 2007, *Applied Proof Theory: Proof Interpretations and Their Use in Mathematics*, Berlin, Heidelberg: Springer. doi:10.1007/978-3-540-77533-1

[^kolmogorov-1925]: Kolmogorov, Andrei Nikolaevich, 1925 [1967], “O principe tertium non datur” (Russian), *Matematiceskij Sbornik*, 32: 646–667. Translated as “On the Principle of the Excluded Middle” in van Heijenoort 1967: 414–437.

[^kreisel-1952]: Kreisel, Georg, 1952, “On the Interpretation of Non-Finitist Proofs, Part II: Interpretation of Number Theory, Applications”, *Journal of Symbolic Logic*, 17(1): 43–58. doi:10.2307/2267457

[^kreisel-1958]: –––, 1958, “Mathematical Significance of Consistency Proofs”, *Journal of Symbolic Logic*, 23(2): 155–182. doi:10.2307/2964396

[^kreisel-1959]: –––, 1959, “Interpretation of Analysis by Means of Constructive Functionals of Finite Type”, in Heyting 1959: 101–128.

[^kreisel-1960]: –––, 1960, “Ordinal Logics and the Characterization of Informal Concepts of Proof”, *Proceedings of the International Congress of Mathematicians, 14–21 August 1958, Edinburgh*, Cambridge: Cambridge University Press, 289–299. [[Kreisel 1960 available online](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf)]

[^kreisel-1963]: –––, 1963, “Generalized Inductive Definitions”, in *Reports of the Seminar on the Foundations of Analysis*, Stanford,(mimeographed), Mathematical Sciences Library, Stanford University, 3.1–3.25.

[^kreisel-1982]: –––, 1982, “Finiteness Theorems in Arithmetic: An Application of Herbrand’s Theorem for $\Sigma_2$-Formulas”, in J. Stern (ed.), *Proceedings of the Herbrand Symposium*, (Studies in Logic and the Foundations of Mathematics, 107), North-Holland Publishing Company, 39–55. doi:10.1016/S0049-237X(08)71876-7

[^kreisel-1975]: Kreisel, G., G.E. Mints, and S.G. Simpson, 1975, “The Use of Abstract Language in Elementary Metamathematics: Some Pedagogic Examples”, in Rohit Parikh (ed.), *Logic Colloquium Symposium on Logic Held at Boston, 1972–73*, Berlin: Springer, 38–131. doi:10.1007/BFb0064871

[^lejeune-nd]: Lejeune Dirichlet, Peter Gustav and Richard Dedekind, *Vorlesungen über Zahlentheorie* (*Lectures on Number Theory*), Braunschweig, Vieweg.

[^lejeune-1863]: 1863, first edition

[^lejeune-1871]: 1871, second edition

[^lejeune-1879]: 1879, third edition

[^lejeune-1894]: 1894, fourth edition

[^lipschitz-1986]: Lipschitz, Rudolf, 1986, *Briefwechsel mit Cantor, Dedekind, Helmholtz, Kronecker, Weierstrass und anderen*, Winfried Scharlau (ed.), Braunschweig: Vieweg. doi:10.1007/978-3-663-14205-8

[^lópez-escobar-1976]: López-Escobar, E.G.K., 1976, “On an Extremely Restricted $\omega$-rule”, *Fundamenta Mathematicae*, 90(2): 159–172. [[Lópex-Escobar 1976 available online](http://pldml.icm.edu.pl/pldml/element/bwmeta1.element.bwnjournal-article-fmv90i1p15bwm)]

[^luckhardt-1989]: Luckhardt, H., 1989, “Herbrand-Analysen zweier Beweise des Satzes von Roth: polynomiale Anzahlschranken”, *Journal of Symbolic Logic*, 54(1): 234–263. doi:10.2307/2275028

[^mancosu-1998]: Mancosu, Paolo, 1998, *From Brouwer to Hilbert. The Debate on the Foundations of Mathematics in the 1920s*, Oxford: Oxford University Press.

[^mancosu-1999a]: –––, 1999a, “Between Russell and Hilbert: Behmann on the Foundations of Mathematics”, *Bulletin of Symbolic Logic*, 5(3): 303–330. doi:10.2307/421183

[^mancosu-1999b]: –––, 1999b, “Between Vienna and Berlin: The Immediate Reception of Gödel’s Incompleteness Theorems”, *History and Philosophy of Logic*, 20(1): 33–45. doi:10.1080/014453499298174

[^martin-löf-1984]: Martin-Löf, Per, 1984, *Intuitionistic Type Theory*, Naples: Bibliopolis.

[^mints-1981]: Mints, G.E., 1981, “Closed Categories and the Theory of Proofs”, *Journal of Soviet Mathematics*, 15(1): 45–62. doi:10.1007/BF01404107

[^myhill-1975]: Myhill, John, 1975, “Constructive Set Theory”, *Journal of Symbolic Logic*, 40(3): 347–382. doi:10.2307/2272159

[^noether-1932]: Noether, Emmy, 1932, “Remark on Dedekind 1872”, in Dedekind 1932: 334.

[^paris-1977]: Paris, Jeff and Leo Harrington, 1977, “A Mathematical Incompleteness in Peano Arithmetic”, Barwise 1977: 1133–1142. doi:10.1016/S0049-237X(08)71130-3

[^peano-1889]: Peano, Giuseppe, 1889, *Arithmetices principia, nova methodo exposita*, Turin. [[Peano 1889 available online](http://archive.org/details/arithmeticespri00peangoog)]

[^peckhaus-1990]: Peckhaus, Volker, 1990, *Hilbertprogramm und Kritische Philosophie*, Göttingen: Vandenhoeck & Ruprecht.

[^pohlers-1975]: Pohlers, Wolfram, 1975, “An Upper Bound for the Provability of Transfinite Induction in Systems with N-Times Iterated Inductive Definitions”, in Diller and Müller 1975: 271–289. doi:10.1007/BFb0079558

[^pohlers-1977]: –––, 1977, *Beweistheorie der iterierten induktiven Definitionen*, Habilitationsschrift, München.

[^pohlers-1982]: –––, 1982, “Cut Elimination for Impredicative Infinitary Systems, Part II: Ordinal Analysis for Iterated Inductive Definitions”, *Archiv für mathematische Logik und Grundlagenforschung*, 22(1–2): 113–129. doi:10.1007/BF02318028

[^pohlers-1991]: –––, 1991, “Proof Theory and Ordinal Analysis”, *Archive for Mathematical Logic*, 30(5–6): 311–376. doi:10.1007/BF01621474

[^pohlers-2009]: –––, 2009, *Proof Theory: The First Step into Impredicativity*, Berlin: Springer. doi:10.1007/978-3-540-69319-2

[^poincaré-1905]: Poincaré, Henri, 1905 [1996], “Les mathématiques et la logique”, *Revue de Métaphysique et de Morale*, 13(6): 815–835; translated in Ewald 1996: 1021–1038).

[^prawitz-1965]: Prawitz, Dag, 1965, *Natural Deduction: A Proof-Theoretical Study*, Stockholm: Almqvist & Wiksell..

[^prawitz-1968]: –––, 1968, “Hauptsatz for Higher Order Logic”, *Journal of Symbolic Logic*, 33(3): 452–457. doi:10.2307/2270331

[^rathjen-1988]: Rathjen, Michael, 1988, *Untersuchungen zu Teilsystemen der Zahlentheorie zweiter Stufe und der Mengenlehre mit einer zwischen $\Delta^1_2$-CA und $\Delta^1_2$-CA+BI liegenden Beweisstärke,* Ph.D. thesis, University of Münster, Münster.

[^rathjen-1990]: –––, 1990, “Ordinal Notations Based on a Weakly Mahlo Cardinal”, *Archive for Mathematical Logic*, 29(4): 249–263. doi:10.1007/BF01651328

[^rathjen-1991]: –––, 1991, “Proof-Theoretic Analysis of KPM”, *Archive for Mathematical Logic*, 30(5–6): 377–403. doi:10.1007/BF01621475

[^rathjen-1993a]: –––, 1993a, “How to Develop Proof-Theoretic Ordinal Functions on the Basis of Admissible Sets”, *Mathematical Logic Quarterly*, 39(1): 47–54. doi:10.1002/malq.19930390107

[^rathjen-1994a]: –––, 1994a, “Collapsing Functions Based on Recursively Large Ordinals: A Well-Ordering Proof for KPM”, *Archive for Mathematical Logic*, 33(1): 35–55. doi:10.1007/BF01275469

[^rathjen-1994b]: –––, 1994b, “Proof Theory of Reflection”, *Annals of Pure and Applied Logic*, 68(2): 181–224. doi:10.1016/0168-0072(94)90074-4

[^rathjen-1995]: –––, 1995, “Recent Advances in Ordinal Analysis: $\Pi^1_2$-CA and Related Systems”, *Bulletin of Symbolic Logic*, 1(4): 468–485. doi:10.2307/421132

[^rathjen-1998]: –––, 1998, “Explicit Mathematics with the Monotone Fixed Point Principle”, *Journal of Symbolic Logic*, 63(2): 509–542. doi:10.2307/2586846

[^rathjen-1999a]: –––, 1999a, “The Realm of Ordinal Analysis”, in S. Barry Cooper and John K. Truss (eds.), *Sets and Proofs*, Cambridge: Cambridge University Press, 219–279. doi:10.1017/CBO9781107325944.011

[^rathjen-1999b]: –––, 1999b, “Explicit Mathematics with the Monotone Fixed Point Principle II: Models”, *Journal of Symbolic Logic*, 64(2): 517–550. doi:10.2307/2586483

[^rathjen-2002]: –––, 2002, “Explicit Mathematics with Monotone Inductive Definitions: A Survey”, in Sieg, Sommer, and Talcott 2002: 335–352.

[^rathjen-2005a]: –––, 2005a, “An Ordinal Analysis of Stability”, *Archive for Mathematical Logic*, 44(1): 1–62. doi:10.1007/s00153-004-0226-2

[^rathjen-2005b]: –––, 2005b, “An Ordinal Analysis of Parameter-Free $\Pi^1_2$-Comprehension”, *Archive for Mathematical Logic*, 44(3): 263–362. doi:10.1007/s00153-004-0232-4

[^rathjen-2006]: –––, 2006, “Theories and Ordinals in Proof Theory”, *Synthese*, 148(3): 719–743. doi:10.1007/s11229-004-6297-0

[^rathjen-2009]: –––, 2009, “The Constructive Hilbert Programme and the Limits of Martin-Löf Type Theory”, in Sten Lindström, Erik Palmgren, Krister Segerberg, and Viggo Stoltenberg-Hansen (eds.), *Logicism, Intuitionism, and Formalism: What Has Become of Them?*, (Synthese Library, 341), Dordrecht: Springer Netherlands, 397–433.

[^rathjen-2010]: –––, 2010, “Investigations of Subsystems of Second Order Arithmetic and Set Theory in Strength Between $\Pi^1_1$-CA and $\Delta^1_2$-CA+BI: Part I”, in Ralf Schindler (ed.), *Ways of Proof Theory*, (Ontos Mathematical Logic, 2), Frankfurt: Ontos Verlag, 363–439.

[^rathjen-2015]: –––, 2015, “Goodstein’s Theorem Revisited”, in Kahle and Rathjen 2015: 229–242. doi:10.1007/978-3-319-10103-3_9

[^rathjen-2018]: –––, 2018 “Proof Theory of Constructive Systems: Inductive Types and Univalence”, in Jäger and Sieg 2018: 385–419.

[^rathjen-2006-2]: Rathjen, Michael and Sergei Tupailo, 2006, “Characterizing the Interpretation of Set Theory in Martin-Löf Type Theory”, *Annals of Pure and Applied Logic*, 141(3): 442–471. doi:10.1016/j.apal.2005.12.008

[^rathjen-1993]: Rathjen, Michael and Andreas Weiermann, 1993, “Proof-Theoretic Investigations on Kruskal’s Theorem”, *Annals of Pure and Applied Logic*: 60(1): 49–88. doi:10.1016/0168-0072(93)90192-G

[^ravaglia-2003]: Ravaglia, Mark, 2003, *Explicating the Finitist Standpoint*, PhD Dissertation, Carnegie Mellon University.

[^reck-2003]: Reck, Erich H., 2003, “Dedekind’s Structuralism: An Interpretation and Partial Defense”, *Synthese*, 137(3): 389–419. doi:10.1023/B:SYNT.0000004903.11236.91

[^reck-2013]: –––, 2013, “Frege, Dedekind, and the Origins of Logicism”, *History and Philosophy of Logic*, 34(3): 242–265. doi:10.1080/01445340.2013.806397

[^reck-2020]: Reck, Erich and Georg Schiemer (eds), 2020, “The Prehistory of Mathematical Structuralism”, Oxford: Oxford University Press.

[^richter-1973]: Richter, Wayne and Peter Aczel, 1973, “Inductive Definitions and Reflecting Properties of Admissible Ordinals”, in Jens E. Fenstad and P. G. Hinman (eds.), 1973, *Generalized Recursion Theory: Proceedings of the 1972 Oslo Symposium*, (Studies in Logic and the Foundations of Mathematics, 79), Amsterdam: North Holland, 301–381. doi:10.1016/S0049-237X(08)70592-5

[^robertson-2004]: Robertson, Neil and Paul Seymour, 2004, “Graph Minors. XX. Wagner’s conjecture”, *Journal of Combinatorial Theory* (Series B), 92(2): 325–357. doi:10.1016/j.jctb.2004.08.001

[^schmidt-1979]: Schmidt, Diana, 1979, *Well-Partial Orderings and Their Maximal Order Types*, Habilitationsschrift, Heidelberg, 77 pages.

[^schönfinkel-1924]: Schönfinkel, M., 1924 [1967], “Über die Bausteine der mathematischen Logik”, *Mathematische Annalen*, 92(3–4): 305–316. English translation in van Heijenoort 1967: 355–366. doi:10.1007/BF01448013 (de)

[^schütte-1950]: Schütte, Kurt, 1950, “Beweistheoretische Erfassung der unendlichen Induktion in der Zahlentheorie”, *Mathematische Annalen*, 122(5): 369–389. doi:10.1007/BF01342849

[^schütte-1960a]: –––, 1960a, “Syntactical and Semantical Properties of Simple Type Theory”, *Journal of Symbolic Logic*, 25(4): 305–326. doi:10.2307/2963525

[^schütte-1960b]: –––, 1960b, *Beweistheorie*, (Grundlehren der mathematischen Wissenschaften, 103), Berlin: Springer. Revised version translated to English as Schütte 1977.

[^schütte-1964]: –––, 1964, “Eine Grenze für die Beweisbarkeit der transfiniten Induktion in der verzweigten Typenlogik”, *Archiv für Mathematische Logik und Grundlagenforschung*, 7(1–2): 45–60. doi:10.1007/BF01972460

[^schütte-1965]: –––, 1965, “Predicative Well-Orderings”, in J.N. Crossley and M.A.E. Dummett (eds.), *Formal Systems and Recursive Functions*, (Studies in Logic and the Foundations of Mathematics, 40), Amsterdam: North Holland, 280–303. doi:10.1016/S0049-237X(08)71694-X

[^schütte-1977]: –––, 1977, *Proof Theory*, ( Grundlehren der mathematischen Wissenschaften, 225), J.N. Crossley (trans.), Berlin: Springer. Translation of a revised version of Schütte 1960b. doi:10.1007/978-3-642-66473-1

[^schwichtenberg-1971]: Schwichtenberg, Helmut, 1971, “Eine Klassifikation der $\varepsilon_0$-Rekursiven Funktionen”, *Zeitschrift für mathematische Logik und Grundlagen der Mathematik*, 17: 61–74. doi: 10.1002/malq.19710170113

[^schwichtenberg-1977]: –––, 1977, “Proof Theory: Some Applications of Cut-Elimination”, in Barwise 1977: 867–895. doi:10.1016/S0049-237X(08)71124-8

[^schwichtenberg-2012]: Schwichtenberg, Helmut and Stanley S. Wainer, 2012, *Proofs and Computations*, (Perspectives in Logic), Cambridge: Cambridge University Press. doi:10.1017/CBO9781139031905

[^setzer-1998]: Setzer, Anton, 1998, “A Well-Ordering Proof for the Proof Theoretical Strength of Martin-Löf Type Theory”, *Annals of Pure and Applied Logic*, 92(2): 113–159. doi:10.1016/S0168-0072(97)00078-X

[^setzer-2000]: –––, 2000, “Extending Martin-Löf Type Theory by One Mahlo-Universe”, *Archive for Mathematical Logic*, 39(3): 155–181. doi:10.1007/s001530050140

[^shoenfield-1959]: Shoenfield, J.R., 1959, “On a restricted $\omega$-rule”, *Bulletin de L’Académie Polonaise des Sciences*, Série des sciences Mathématiques, Astronomiques et Physiques, 7: 405–407.

[^sieg-1977]: Sieg, Wilfried, 1977, *Trees in Metamathematics (Theories of Inductive Definitions and Subsystems of Analysis)*, Ph.D. Thesis, Stanford.

[^sieg-1981]: –––, 1981, “Inductive Definitions, Constructive Ordinals, and Normal Derivations”, in Buchholz et al. 1981: 143–187. doi:10.1007/BFb0091897

[^sieg-1985]: –––, 1985, “Fragments of Arithmetic”, *Annals of Pure and Applied Logic*, 28: 33–71. doi:10.1016/0168-0072(85)90030-2

[^sieg-1990]: ––– (ed.), 1990, *Logic and Computation*, (Contemporary Mathematics, 106), Providence, Rhode Island: American Mathematical Society. doi:10.1090/conm/106

[^sieg-1991]: –––, 1991, “Herbrand Analyses”, *Archive for Mathematical Logic*, 30(5–6): 409–441. doi:10.1007/BF01621477

[^sieg-2010]: –––, 2010, “Searching for Proofs (and Uncovering Capacities of the Mathematical Mind)”, in *Proofs, Categories, and Computations: Essays in Honor of Grigori Mints*, Solomon Feferman and Wilfried Sieg (eds), London: College Publications, 189–215.

[^sieg-2012]: –––, 2012, “In the Shadow of Incompleteness: Hilbert and Gentzen”, in P. Dybjer, Sten Lindström, Erik Palmgren, and G. Sundholm (eds.), *Epistemology versus Ontology: Essays on the Philosophy and Foundations of Mathematics in Honour of Per Martin-Löf*, Dordrecht, Heidelberg: Springer, 87–128. doi:10.1007/978-94-007-4435-6_5

[^sieg-2013]: –––, 2013, *Hilbert’s Programs and Beyond*, Oxford: Oxford University Press.

[^sieg-2020]: –––, 2020, “Methodological Frames: Paul Bernays, Mathematical Structuralism, and Proof Theory”, in: Reck and Schiemer 2020: 352–382.

[^sieg-2021]: Sieg, Wilfried and Farzaneh Derakhshan, 2021, “Human-centered automated proof search”, *Journal of Automated Reasoning*, 65: 1153–1190.

[^sieg-2018]: Sieg, Wilfried and Rebecca Morris, 2018, “Dedekind’s Structuralism: Creating Concepts and Deriving Theorems”, in: *Logic, Philosophy of Mathematics, and Their History: Essays in Honor of W.W. Tait*, London: College Publication, 251–301.

[^sieg-2005]: Sieg, Wilfried and Dirk Schlimm, 2005, “Dedekind’s Analysis of Number: Systems and Axioms”, *Synthese*, 147(1): 121–170. doi:10.1007/s11229-004-6300-9

[^sieg-2014]: –––, 2014, “Dedekind’s Abstract Concepts: Models and Mappings”, *Philosophia Mathematica*, 25(3): 292–317. doi:10.1093/philmat/nku021.

[^sieg-2002]: Sieg, Wilfried, Richard Sommer, and Carolyn Talcott (eds.), 2002, *Reflections on the Foundations of Mathematics: Essays in Honor of Solomon Feferman*, (Lecture Notes in Logic, 15), Urbana, IL: Association for Symbolic Logic.

[^simpson-1985]: Simpson, Stephen G., 1985, “Nichtbeweisbarkeit von gewissen kombinatorischen Eigenschaften endlicher Bäume”, *Archiv für Mathematische Logik und Grundlagenforschung*, 25(1): 45–65. doi:10.1007/BF02007556

[^simpson-1987]: ––– (ed.), 1987, *Logic and Combinatorics*, (Contemporary Mathematics, 65), Providence, Rhode Island: American Mathematical Society. doi:10.1090/conm/065

[^simpson-1999]: –––, 1999, *Subsystems of Second Order Arithmetic*, Berlin: Springer.

[^sinaceur-1974]: Sinaceur, Mohammed-A., 1974, “L’infini et les nombres: Commentaires de R. Dedekind à « Zahlen » La correspondance avec Keferstein”, *Revue d’histoire des sciences*, 27(3): 251–278. doi:10.3406/rhs.1974.1089

[^spector-1962]: Spector, Clifford, 1962, “Provably Recursive Functions of Analysis: A Consistency Proof of Analysis by An Extension of Principles Formulated in Current Intuitionistic Mathematics”, in J.C.E. Dekker (ed.), *Recursive Function Theory: Proceedings of the Fifth Symposia in Pure Mathematics*, New York, April 6–7, 1961, pp. 1–27. doi:10.1090/pspum/005/0154801

[^tait-1966]: Tait, W.W., 1966, “A Nonconstructive Proof of Gentzen’s Hauptsatz for Second Order Predicate Logic”, *Bulletin of the American Mathematical Society*, 72(6): 980–983.

[^tait-1970]: –––, 1970, “Applications of the Cut Elimination Theorem to Some Subsystems of Classical Analysis”, in Kino, Myhill, and Vesley 1970: 475–488. doi:10.1016/S0049-237X(08)70772-9

[^tait-1981]: –––, 1981, “Finitism”, *Journal of Philosophy*, 78(9): 524–546. doi:10.2307/2026089

[^tait-2002]: –––, 2002, “Remarks on Finitism”, in Sieg, Sommer and Talcott 2002: 410–419.

[^tait-2015]: –––, 2015, “Gentzen’s Original Consistency Proof and the Bar Theorem”, in Kahle and Rathjen 2015: 213–228. doi:10.1007/978-3-319-10103-3_8

[^takahashi-1967]: Takahashi, Moto-o, 1967, “A Proof of Cut-Elimination in Simple Type Theory”, *Journal of the Mathematical Society of Japan*, 19(4): 399–410. doi:10.2969/jmsj/01940399

[^takeuti-1953]: Takeuti, Gaisi, 1953, “On a Generalized Logic Calculus”, *Japanese Journal of Mathematics*, 24: 149–156. doi:10.4099/jjm1924.23.0_39

[^takeuti-1967]: –––, 1967, “Consistency Proofs of Subsystems of Classical Analysis”, *Annals of Mathematics*, 86(2): 299–348. doi:10.2307/1970691

[^takeuti-1975]: –––, 1975, “Consistency Proofs and Ordinals”, in Diller and Müller 1975: 365–369. doi:10.1007/BFb0079562

[^takeuti-1985]: –––, 1985, “Proof Theory and Set Theory”, *Synthese*, 62(2): 255–263. doi:10.1007/BF00486049

[^takeuti-1987]: –––, 1987, *Proof Theory*, second edition, Amsterdam: North-Holland.

[^takeuti-2003]: –––, 2003, *Memoirs of a Proof Theorist: Gödel and Other Logicians*, translated into English by Mariko Yasugi and Nicholas Passell, River Edge, NJ: World Scientific. doi:10.1142/5202

[^takeuti-1973]: Takeuti, Gaisi and Mariko Yasugi, 1973, “The Ordinals of the Systems of Second Order Arithmetic with the Provably $\Delta^1_2$-Comprehension and the $\Delta^1_2$-Comprehension Axiom Respectively”, *Japanese Journal of Mathematics*, 41: 1–67. doi:10.4099/jjm1924.41.0_1

[^torretti-1978]: Torretti, Roberto, 1978 [1984], *Philosophy of Geometry from Riemann to Poincaré*, Dordrecht: D. Reidel. doi:10.1007/978-94-009-9909-1

[^troelstra-1973]: Troelstra, Anne S. (ed.), 1973, *Metamathematical Investigations of Intuitionistic Arithmetic and Analysis*, (Lecture Notes in Mathematics, 344), Heidelberg, Berlin: Springer. doi:10.1007/BFb0066739

[^troelstra-2000]: Troelstra, A.S. and H. Schwichtenberg, 2000, *Basic Proof Theory*, second edition, Cambridge: Cambridge University Press. doi:10.1017/CBO9781139168717

[^turing-1936]: Turing, A.M., 1936, “On Computable Numbers with an Application to the Entscheidungsproblem”, *Proceedings of the London Mathematical Society*, series 2, 42(1): 230–265. doi:10.1112/plms/s2-42.1.230

[^turing-1939]: –––, 1939, “Systems of Logic Based on Ordinals”, *Proceedings of the London Mathematical Society*, series 2, 45(2239): 161–228. doi:10.1112/plms/s2-45.1.161

[^atten-2007]: van Atten, Mark, 2007, *Brouwer Meets Husserl: On the Phenomenology of Choice Sequences*, (Synthese Library, 335), Dordrecht: Springer Netherlands. doi:10.1007/978-1-4020-5087-9

[^heijenoort-1967]: van Heijenoort, Jean (ed.), 1967, *From Frege to Gödel. A Source Book in Mathematical Logic 1879–1931*, Cambridge, MA: Harvard University Press (reprinted 1970).

[^veblen-1908]: Veblen, Oswald, 1908, “Continuous Increasing Functions of Finite and Transfinite Ordinals”, *Transactions of the American Mathematics Society*, 9(3): 280–292. doi:10.1090/S0002-9947-1908-1500814-9

[^neumann-1927]: von Neumann, J., 1927, “Zur Hilbertschen Beweistheorie”, *Mathematische Zeitschrift*, 26: 1–46. doi:10.1007/BF01475439

[^plato-2008]: von Plato, Jan, 2008, “Gentzen’s Proof of Normalization for Natural Deduction”, *Bulletin of Symbolic Logic*, 14(2): 240–257. doi:10.2178/bsl/1208442829

[^plato-2009]: –––, 2009, “Gentzen’s logic”, in D.M. Gabbay and J. Woods (eds), *Handbook of the History of Logic 5, Logic from Russell to Church*, Amsterdam: Elsevier, 667–721. doi:10.1016/S1874-5857(09)70017-2

[^plato-2017]: –––, 2017, *Saved from the Cellar: Gerhard Gentzen’s Shorthand Notes on Logic and Foundations of Mathematics*, Berlin: Springer. doi:10.1007/978-3-319-42120-9

[^wainer-1970]: Wainer, S.S., 1970, “A Classification of the Ordinal Recursive Functions”, *Archiv für Mathematische Logik und Grundlagenforschung*, 13(3–4): 136–153. doi:10.1007/BF01973619

[^wang-1981]: Wang, Hao, 1981, “Some Facts About Kurt Gödel”, *Journal of Symbolic Logic*, 46(3): 653–659. doi:10.2307/2273764

[^weiermann-1996]: Weiermann, A., 1996, “How to Characterize Provably Total Functions by Local Predicativity”, *Journal of Symbolic Logic*, 61(1): 52–69. doi:10.2307/2275597

[^weyl-1918]: Weyl, Hermann, 1918, *Das Kontinuum*, Leipzig: Veit.

[^weyl-1946]: –––, 1946, “Mathematics and Logic”, *American Mathematical Monthly*, 53(1): 2–13. doi:10.2307/2306078

[^zach-1999]: Zach, Richard, 1999, “Completeness Before Post: Bernays, Hilbert, and the Development of Propositional Logic”, *Bulletin of Symbolic Logic*, 5(3): 331–366. doi:10.2307/421184

[^zach-2003]: –––, 2003, “The Practice of Finitism: Epsilon Calculus and Consistency Proofs in Hilbert’s Program”, *Synthese*, 137(1–2): 211–259. doi:10.1023/A:1026247421383

[^zach-2004]: –––, 2004, “Hilbert’s ‘*Verunglückter Beweis*’, the First Epsilon Theorem, and Consistency Proofs”, *History and Philosophy of Logic*, 25(2): 79–94. doi:10.1080/01445340310001606930

[^zermelo-1932]: Zermelo, E., 1932, “Über Stufen der Quantifikation und die Logik des Unendlichen”, *Jahresberichte der Deutschen Mathematiker-Vereinigung*, 41: 85–88.

[^zucker-1973]: Zucker, J.I., 1973, “Iterated Inductive Definitions, Trees, and Ordinals”, in Troelstra 1973: 392–453. doi:10.1007/BFb0066745
