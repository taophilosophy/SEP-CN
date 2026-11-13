# Intuitionistic Type Theory
**First published Fri Feb 12, 2016; substantive revision Mon Sep 23, 2024**

*Dybjer, Peter, Palmgren, Erik*

Intuitionistic type theory (also constructive type theory or Martin-Löf type theory) is a formal logical system and philosophical foundation for *constructive mathematics*. It is a full-scale system which aims to play a similar role for constructive mathematics as *Zermelo-Fraenkel Set Theory* does for classical mathematics. It is based on the propositions-as-types principle and clarifies the Brouwer-Heyting-Kolmogorov interpretation of intuitionistic logic. It extends this interpretation to the more general setting of intuitionistic type theory and thus provides a general conception not only of what a constructive proof is, but also of what a constructive mathematical object is. The main idea is that mathematical concepts such as elements, sets and functions are explained in terms of concepts from programming such as data structures, data types and programs. We quote the article “Constructive Mathematics and Computer Programming” (Martin-Löf 1982)[^martin-löf-1982]:

> Now, it is the contention of the intuitionists (or constructivists, I shall use these terms synonymously) that the basic mathematical notions, above all the notion of function, ought to be interpreted in such a way that the cleavage between mathematics, classical mathematics, that is, and programming that we are witnessing at present disappears.

This article describes the formal system of intuitionistic type theory and its semantic foundations.

In this entry, we first give an overview of the most important aspects of intuitionistic type theory—a kind of “extended abstract”. It is meant for a reader who is already somewhat familiar with the theory. Section 2 on the other hand, is meant for a reader who is new to intuitionistic type theory but familiar with traditional logic, including propositional and predicate logic, arithmetic, and set theory. Here we informally introduce several aspects that distinguish intuitionistic type theory from these traditional theories. In Section 3 we present a basic version of the theory, close to Martin-Löf’s first published version from 1972. The reader who was intrigued by the informality of Section 2 will now see in detail how the theory is built up. Section 4 presents a number of important extensions of the original theory. In particular, it emphasizes the fundamental role of inductive (and inductive-recursive) definitions. Section 5 introduces the underlying philosophical ideas including the theory of meaning developed by Martin-Löf. While Section 5 is about philosophy and foundations, Section 6 gives an overview of mathematical models of the theory. In Section 7 finally, we describe several important variations of the core Martin-Löf “intensional” theory described in Section 3 and 4.

## 1. Overview

We begin with a bird’s eye view of some important aspects of intuitionistic type theory. Readers who are unfamiliar with the theory may prefer to skip it on a first reading.

The origins of intuitionistic type theory are Brouwer’s intuitionism and Russell’s type theory. Like Church’s classical simple theory of types it is based on a lambda calculus with types, but differs from it in that it uses the propositions-as-types principle, discovered by Curry (1958) for propositional logic and extended to predicate logic by Howard (1980) and de Bruijn (1970). This extension was made possible by the introduction of indexed families of types (dependent types) for representing the predicates of predicate logic. In this way all logical connectives and quantifiers can be interpreted by type formers. In intuitionistic type theory further types are added, such as a type of natural numbers, a type of small types (a universe) and a type of well-founded trees. The resulting theory contains intuitionistic number theory (Heyting arithmetic) and much more.

The theory is formulated in natural deduction where the rules for each type former are classified as formation, introduction, elimination, and equality rules. These rules exhibit certain symmerties between the introduction and elimination rules following Gentzen’s and Prawitz’ treatment of natural deduction, as explained in the entry on proof-theoretic semantics.

The elements of propositions, when interpreted as types, are called *proof-objects*. When proof-objects are added to the natural deduction calculus it becomes a typed lambda calculus with dependent types, which extends Church’s original typed lambda calculus. The equality rules are computation rules for the terms of this calculus. Each function definable in the theory is total and computable. Intuitionistic type theory is thus a typed functional programming language with the unusual property that all programs terminate.

Intuitionistic type theory is not only a formal logical system but also provides a comprehensive philosophical framework for intuitionism. It is an *interpreted language*, where the distinction between the *demonstration of a judgment* and the *proof of a proposition* plays a fundamental role (Sundholm 2012)[^sundholm-2012]. The meaning of the judgments of intuitionistic type theory is explained in terms of computations of the canonical forms of types and terms. These informal, intuitive meaning explanations are “pre-mathematical” and should be contrasted to formal mathematical models developed inside a standard mathematical framework such as set theory.

This meaning theory also justifies a variety of inductive, recursive, and inductive-recursive definitions. Although proof-theoretically strong notions, such as analogues of certain large cardinals, can be justified, the system is considered predicative. Impredicative definitions of the kind found in higher-order logic, intuitionistic set theory, and topos theory are not part of the theory. Neither is Markov’s principle, and thus the theory is distinct from Russian constructivism.

An alternative formal logical system for predicative constructive mathematics is Myhill and Aczel’s constructive Zermelo-Fraenkel set theory (CZF). This theory, which is based on intuitionistic first-order predicate logic and weakens some of the axioms of classical Zermelo-Fraenkel Set Theory, has a natural interpretation in intuitionistic type theory. Martin-Löf’s meaning explanations thus also indirectly form a basis for CZF.

Variants of intuitionistic type theory underlie several widely used proof assistants, including NuPRL, Coq, and Agda. These proof assistants are computer systems that have been used for formalizing large and complex proofs of mathematical theorems, such as the Four Colour Theorem in graph theory and the Feit-Thompson Theorem in finite group theory. They have also been used to prove the correctness of a realistic C compiler (Leroy 2009)[^leroy-2009] and other computer software.

Philosophically and practically, intuitionistic type theory is a foundational framework where constructive mathematics and computer programming are, in a deep sense, the same. This point has been emphasized by (Gonthier 2008)[^gonthier-2008] in the paper in which he describes his proof of the Four Colour Theorem:

> The approach that proved successful for this proof was to turn almost every mathematical concept into a data structure or a program in the Coq system, thereby converting the entire enterprise into one of program verification.

## 2. Propositions as Types

### 2.1 Intuitionistic Type Theory: a New Way of Looking at Logic?

Intuitionistic type theory offers a new way of analyzing logic, mainly through its introduction of explicit proof objects. This provides a direct computational interpretation of logic, since there are computation rules for proof objects. As regards expressive power, intuitionistic type theory may be considered as an extension of first-order logic, much as higher order logic, but predicative.

#### 2.1.1 A Type Theory

Russell developed type theory in response to his discovery of a paradox in naive set theory. In his ramified type theory mathematical objects are classified according to their *types*: the type of propositions, the type of objects, the type of properties of objects, etc. When Church developed his simple theory of types on the basis of the typed lambda calculus he added the rule that there is a type of functions between any two types of the theory. Intuitionistic type theory further extends the simply typed lambda calculus with dependent types, that is, indexed families of types. An example is the family of types of $n$-tuples indexed by $n$.

Types have been widely used in programming for a long time. Early high-level programming languages introduced types of integers and floating point numbers. Modern programming languages often have rich type systems with many constructs for forming new types. Intuitionistic type theory is a functional programming language where the type system is so rich that practically any conceivable property of a program can be expressed as a type. Types can thus be used as specifications of the task of a program.

#### 2.1.2 An intuitionstic logic with proof-objects

Brouwer’s analysis of logic led him to an intuitionistic logic which rejects the law of excluded middle and the law of double negation. These laws are not valid in intuitionistic type theory. Thus it does not contain classical (Peano) arithmetic but only intuitionistic (Heyting) arithmetic. (It is another matter that Peano arithmetic can be interpreted in Heyting arithmetic by the double negation interpretation, see the entry on intuitionistic logic.)

Consider a theorem of intuitionistic arithmetic, such as the division theorem

$$\forall m, n. m > 0 \supset \exists q, r. mq + r = n \wedge m > r $$

A formal proof (in the usual sense) of this theorem is a sequence (or tree) of formulas, where the last (root) formula is the theorem and each formula in the sequence is either an axiom (a leaf) or the result of applying an inference rule to some earlier (higher) formulas.

When the division theorem is proved in intuitionistic type theory, we do not only build a formal proof in the usual sense but also a *construction* (or *proof-object*) “$\divi$” which witnesses the truth of the theorem. We write

$$\divi : \forall m, n {:} \N.\, m > 0 \supset \exists q, r {:} \N.\, mq + r = n \wedge m > r $$

to express that $\divi$ is a proof-object for the division theorem, that is, an element of the type representing the division theorem. When propositions are represented as types, the $\forall$-quantifier is identified with the dependent function space former (or general cartesian product) $\Pi$, the $\exists$-quantifier with the dependent pairs type former (or general disjoint sum) $\Sigma$, conjunction $\wedge$ with cartesian product $ \times $, the identity relation = with the type former $\I$ of proof-objects of identities, and the greater than relation $>$ with the type former $\GT$ of proof-objects of greater-than statements. Using “type-notation” we thus write

$$ \divi : \Pi m, n {:} \N.\, \GT(m,0)\rightarrow \Sigma q, r {:} \N.\, \I(\N,mq + r,n) \times \GT(m,r) $$

to express that the proof object “$\divi$” is a function that maps two numbers $m$ and $n$ and a proof-object $p$ witnessing that $m > 0$ to a quadruple $(q,(r,(s,t)))$, where $q$ is the quotient and $r$ is the remainder obtained when dividing $n$ by $m$. The third component $s$ is a proof-object witnessing the fact that $mq + r = n$ and the fourth component $t$ is a proof object witnessing $m > r $.

Crucially, $\divi$ is not only a function in the classical sense; it is also a function in the intuitionistic sense, that is, a program which computes the output $(q,(r,(s,t)))$ when given $m$, $n$, $p$ as inputs. This program is a term in a lambda calculus with special constants, that is, a program in a functional programming language.

#### 2.1.3 An extension of first-order predicate logic

Intuitionistic type theory can be considered as an extension of first-order logic, much as higher order logic is an extension of first order logic. In higher order logic we find some individual domains which can be interpreted as any sets we like. If there are relational constants in the signature these can be interpreted as any relations between the sets interpreting the individual domains. On top of that we can quantify over relations, and over relations of relations, etc. We can think of higher order logic as first-order logic equipped with a way of introducing new domains of quantification: if $S_1, \ldots, S_n$ are domains of quantification then $(S_1,\ldots,S_n)$ is a new domain of quantification consisting of all the n-ary relations between the domains $S_1,\ldots,S_n$. Higher order logic has a straightforward set-theoretic interpretation where $(S_1,\ldots,S_n)$ is interpreted as the power set $P(A_1 \times \cdots \times A_n)$ where $A_i$ is the interpretation of $S_i$, for $i=1,\ldots,n$. This is the kind of higher order logic or simple theory of types that Ramsey, Church and others introduced.

Intuitionistic type theory can be viewed in a similar way, only here the possibilities for introducing domains of quantification are richer, one can use $\Sigma, \Pi, +, \I$ to construct new ones from old. (Section 3.1; Martin-Löf 1998 [1972])[^martin-löf-1998]. Intuitionistic type theory has a straightforward set-theoretic interpretation as well, where $\Sigma$, $\Pi$ etc are interpreted as the corresponding set-theoretic constructions; see below. We can add to intuitionistic type theory unspecified individual domains just as in HOL. These are interpreted as sets as for HOL. Now we exhibit a difference from HOL: in intuitionistic type theory we can introduce unspecified family symbols. We can introduce $T$ as a family of types over the individual domain $S$:

$$T(x)\; {\rm type} \;(x{:}S).$$

If $S$ is interpreted as $A$, $T$ can be interpreted as any family of sets indexed by $A$. As a non-mathematical example, we can render the binary relation *loves* between members of an individual domain of *people* as follows. Introduce the binary family Loves over the domain People

$${\rm Loves}(x,y)\; {\rm type}\; (x{:}{\rm People}, y{:}{\rm People}).$$

The interpretation can be any family of sets $B_{x,y}$ ($x{:}A$, $y{:}A$). How does this cover the standard notion of relation? Suppose we have a binary relation $R$ on $A$ in the familiar set-theoretic sense. We can make a binary family corresponding to this as follows

$$ B_{x,y} = \begin{cases} \{0\} &\text{if } R(x,y) \text{ holds} \\ \varnothing &\text{if } R(x,y) \text{ is false.} \end{cases}$$

Now clearly $B_{x,y}$ is nonempty if and only if $R(x,y)$ holds. (We could have chosen any other element from our set theoretic universe than 0 to indicate truth.) Thus from any relation we can construct a family whose truth of $x,y$ is equivalent to $B_{x,y}$ being non-empty. Note that this interpretation does not care what the proof for $R(x,y)$ is, just that it holds. Recall that intuitionistic type theory interprets propositions as types, so $p{:} {\rm Loves}({\rm John}, {\rm Mary})$ means that ${\rm Loves}({\rm John}, {\rm Mary})$ is true.

The interpretation of relations as families allows for keeping track of proofs or evidence that $R(x,y)$ holds, but we may also chose to ignore it.

In Montague semantics, higher order logic is used to give semantics of natural language (and examples as above). Ranta (1994) introduced the idea to instead employ intuitionistic type theory to better capture sentence structure with the help of dependent types.

In contrast, how would the mathematical relation $>$ between natural numbers be handled in intuitionistic type theory? First of all we need a type of numbers $\N$. We could in principle introduce an unspecified individual domain $\N$, and then add axioms just as we do in first-order logic when we set up the axiom system for Peano arithmetic. However this would not give us the desirable computational interpretation. So as explained below we lay down introduction rules for constructing new natural numbers in $\N$ and elimination and computation rules for defining functions on $\N$ (by recursion). The standard order relation $>$ should satisfy

$$ x \gt y \text{ iff there exists } z{:} \N \text{ such that } y+z+1 = x. $$

The right hand is rendered as $\Sigma z{:}\N.\, \I(\N,y+z+1,x)$ in intuitionistic type theory, and we take this as definition of relation $>$. ($+$ is defined by recursive equations, $\I$ is the identity type construction). Now all the properties of $>$ are determined by the mentioned introduction and elimination and computation rules for $\N$.

#### 2.1.4 A logic with several forms of judgment

The type system of intuitionistic type theory is very expressive. As a consequence the well-formedness of a type is no longer a simple matter of parsing, it is something which needs to be proved. Well-formedness of a type is one form of *judgment* of intuitionistic type theory. Well-typedness of a term with respect to a type is another. Furthermore, there are equality judgments for types and terms. This is yet another way in which intuitionistic type theory differs from ordinary first order logic with its focus on the sole judgment expressing the truth of a proposition.

#### 2.1.5 Semantics

While a standard presentation of first-order logic would follow Tarski in defining the notion of model, intuitionistic type theory follows the tradition of Brouwerian meaning theory as further developed by Heyting and Kolmogorov, the so called BHK-interpretation of logic. The key point is that the proof of an implication $A \supset B $ is a *method* that transforms a proof of $A$ to a proof of $B$. In intuitionistic type theory this method is formally represented by the program $f {:} A \supset B$ or $f {:} A \rightarrow B$: the type of proofs of an implication $A \supset B$ is the type of functions which maps proofs of $A$ to proofs of $B$.

Moreover, whereas Tarski semantics is usually presented meta-mathematically, and assumes set theory, Martin-Löf’s meaning theory of intuitionistic type theory should be understood directly and “pre-mathematically”, that is, without assuming a meta-language such as set theory.

#### 2.1.6 A functional programming language

Readers with a background in the lambda calculus and functional programming can get an alternative first approximation of intuitionistic type theory by thinking about it as a typed functional programming language in the style of Haskell or one of the dialects of ML. However, it differs from these in two crucial aspects: (i) it has dependent types (see below) and (ii) all typable programs terminate. (Note that intuitionistic type theory has influenced the extension of Haskell with *generalized algebraic datatypes* which sometimes can play a similar role as inductively defined dependent types.)

### 2.2 The Curry-Howard Correspondence

As already mentioned, the principle that

> *a proposition is the type of its proofs.*

is fundamental to intuitionistic type theory. This principle is also known as the Curry-Howard correspondence or even Curry-Howard isomorphism. Curry discovered a correspondence between the implicational fragment of intuitionistic logic and the simply typed lambda-calculus. Howard extended this correspondence to first-order predicate logic. In intuitionistic type theory this correspondence becomes an *identification* of proposition and types, which has been extended to include quantification over higher types and more.

### 2.3 Sets of Proof-Objects

So what are these proof-objects like? They should not be thought of as logical derivations, but rather as some (structured) symbolic evidence that something is true. Another term for such evidence is “truth-maker”.

It is instructive, as a somewhat crude first approximation, to replace types by ordinary sets in this correspondence. Define a set $\E_{m,n}$, depending on $m, n \in {{\mathbb N}}$, by:

$$\E_{m,n} = \left\{\begin{array}{ll} \{0\} & \mbox{if \(m = n\)}\\ \varnothing & \mbox{if \(m \ne n\).} \end{array} \right.$$

Then $\E_{m,n}$ is nonempty exactly when $m=n$. The set $\E_{m,n}$ corresponds to the proposition $m=n$, and the number $0$ is a proof-object (truth-maker) inhabiting the sets $\E_{m,m}$.

Consider the proposition that *$m$ is an even number* expressed as the formula $\exists n \in {{\mathbb N}}. m= 2n$. We can build a set of proof-objects corresponding to this formula by using the general set-theoretic sum operation. Suppose that $A_n$ ($n\in {{\mathbb N}}$) is a family of sets. Then its disjoint sum is given by the set of pairs

$$ (\Sigma n \in {{\mathbb N}})A_n = \{ (n,a) : n \in {{\mathbb N}}, a \in A_n\}.$$

If we apply this construction to the family $A_n = \E_{m,2n}$ we see that $(\Sigma n \in {{\mathbb N}})\E_{m,2n}$ is nonempty exactly when there is an $n\in {{\mathbb N}}$ with $m=2n$. Using the general set-theoretic product operation $(\Pi n \in {{\mathbb N}})A_n$ we can similarly obtain a set corresponding to a universally quantified proposition.

### 2.4 Dependent Types

In intuitionistic type theory there are primitive type formers $\Sigma$ and $\Pi$ for general sums and products, and $\I$ for identity types, analogous to the set-theoretic constructions described above. The *identity type* $\I(\N,m,n)$ corresponding to the set $\E_{m,n}$ is an example of a *dependent type* since it depends on the elements $m$*,* n : $\N$. It is also called an *indexed family of types* since it is a family of types indexed by $m$ and $n$. Similarly, we can form the general disjoint sum $\Sigma x {:} A.\, B$ and the general cartesian product $\Pi x {:} A.\, B$ of such a family of types $B$ indexed by $x {:} A$, corresponding to the set theoretic sum and product operations above.

Dependent types can also be defined by primitive recursion. An example is the type of $n$-tuples $A^n$ of elements of type $A$ and indexed by $n {:} N$ defined by the equations

$$\begin{align*} A^0 &= 1\\ A^{n+1} &= A \times A^n \end{align*}$$

where $1$ is a one element type and $\times$ denotes the cartesian product of two types. We note that dependent types introduce computation in types: the defining rules above are computation rules. For example, we can compute $A^3$ = $A \times (A \times (A \times 1))$.

### 2.5 Propositions as Types in Intuitionistic Type Theory

With propositions as types, predicates become dependent types. For example, the predicate $\mathrm{Prime}(x)$ becomes the type of proofs that $x$ is prime. This type *depends* on $x$. Similarly, $x < y$ is the type of proofs that $x$ is less than $y$.

According to the Curry-Howard interpretation of propositions as types, the logical constants are interpreted as type formers:

$$\begin{align*} \bot &= \varnothing\\ \top &= 1\\ A \vee B &= A + B\\ A \wedge B &= A \times B\\ A \supset B &= A \rightarrow B\\ \exists x {:} A.\, B &= \Sigma x {:} A.\, B\\ \forall x {:} A.\, B &= \Pi x {:} A.\, B \end{align*}$$

where $\Sigma x {:} A.\, B$ is the disjoint sum of the $A$-indexed family of types $B$ and $\Pi x {:} A.\, B$ is its cartesian product. The canonical elements of $\Sigma x {:} A.\, B$ are pairs $(a,b)$ such that $a {:} A$ and $b {:} B[x:=a]$ (the type obtained by substituting all free occurrences of $x$ in $B$ by $a$). The elements of $\Pi x {:} A.\, B$ are (computable) functions $f$ such that $f\,a {:} B[x:=a]$, whenever $a {:} A$.

For example, consider the proposition

$$\begin{equation} \forall m {:} \N.\, \exists n {:} \N.\, m \lt n \wedge \mathrm{Prime}(n) \tag{1}\label{prop1} \end{equation}$$

expressing that there are arbitrarily large primes. Under the Curry-Howard interpretation this becomes the type $\Pi m {:} \N.\, \Sigma n {:} \N.\, m \lt n \times \mathrm{Prime}(n)$ of functions which map a number $m$ to a triple $(n,(p,q))$, where $n$ is a number, $p$ is a proof that $m \lt n$ and $q$ is a proof that $n$ is prime. This is the *proofs as programs* principle: a constructive proof that there are arbitrarily large primes becomes a program which given any number produces a larger prime together with proofs that it indeed is larger and indeed is prime.

Note that the proof which derives a contradiction from the assumption that there is a largest prime is not constructive, since it does not explicitly give a way to compute an even larger prime. To turn this proof into a constructive one we have to show explicitly how to construct the larger prime. (Since proposition (\ref{prop1}) above is a $\Pi^0_2$-formula we can use Friedman’s A-translation to turn such a proof in classical arithmetic into a proof in intuitionistic arithmetic and thus into a proof in intuitionistic type theory.)

## 3. Basic Intuitionistic Type Theory

We now present a core version of intuitionistic type theory, closely related to the first version of the theory presented by Martin-Löf in 1972 (Martin-Löf 1998 [1972])[^martin-löf-1998]. In addition to the type formers needed for the Curry-Howard interpretation of typed intuitionistic predicate logic listed above, we have two types: the type $\N$ of natural numbers and the type $\U$ of small types.

The resulting theory contains intuitionistic number theory $\HA$ (Heyting arithmetic), Gödel’s System $\T$ of primitive recursive functions of higher type, and the theory $\HA^\omega$ of Heyting arithmetic of higher type.

This core intuitionistic type theory is not only the original one, but perhaps the minimal version which exhibits the essential features of the theory. Later extensions with primitive identity types, well-founded tree types, universe hierarchies, and general notions of inductive and inductive-recursive definitions have increased the proof-theoretic strength of the theory and also made it more convenient for programming and formalization of mathematics. For example, with the addition of well-founded trees we can interpret the Constructive Zermelo-Fraenkel Set Theory $\CZF$ of Aczel (1978 [1977]). However, we will wait until the next section to describe those extensions.

### 3.1 Judgments

In Martin-Löf (1996) a general philosophy of logic is presented where the traditional notion of judgment is expanded and given a central position. A judgment is no longer just an affirmation or denial of a proposition, but a general act of knowledge. When reasoning mathematically we make judgments about mathematical objects. One form of judgment is to state that some mathematical statement is true. Another form of judgment is to state that something is a mathematical object, for example a set.

First-order reasoning may be presented using a single kind of judgment:

> the proposition $B$ is true under the hypothesis that the propositions $A_1, \ldots, A_n$ are all true.

We write this *hypothetical judgment* as a so-called *Gentzen sequent*

$$A_1, \ldots, A_n {\vdash}B.$$

Note that this is a single judgment that should not be confused with the derivation of the judgment ${\vdash}B$ from the judgments ${\vdash}A_1, \ldots, {\vdash}A_n$. When $n=0$, then the *categorical judgment* $ {\vdash}B$ states that $B$ is true without any assumptions. With sequent notation the familiar rule for conjunctive introduction becomes

$$\begin{prooftree} \AxiomC{\(A_1, \ldots,A_n {\vdash}B\)} \AxiomC{\(A_1, \ldots, A_n {\vdash}C\)} \RightLabel{\((\land I)\).} \BinaryInfC{\(A_1, \ldots, A_n {\vdash}B \land C\)} \end{prooftree}$$

### 3.2 Judgment Forms

Martin-Löf type theory has four basic forms of judgments and is a considerably more complicated system than first-order logic. One reason is that more information is carried around in the derivations due to the identification of propositions and types. Another reason is that the syntax is more involved. For instance, the well-formed formulas (types) have to be generated simultaneously with the provably true formulas (inhabited types).

The four forms of *categorical* judgment are

- $\vdash A \; {\rm type}$, meaning that $A$ is a well-formed type,
- $\vdash a {:} A$, meaning that $a$ has type $A$,
- $\vdash A = A'$, meaning that $A$ and $A'$ are equal types,
- $\vdash a = a' {:} A$, meaning that $a$ and $a'$ are equal elements of type $A$.

In general, a judgment is *hypothetical*, that is, it is made in a context $\Gamma$, that is, a list $x_1 {:} A_1, \ldots, x_n {:} A_n$ of variables which may occur free in the judgment together with their respective types. Note that the types in a context can depend on variables of earlier types. For example, $A_n$ can depend on $x_1 {:} A_1, \ldots, x_{n-1} {:} A_{n-1}$. The four forms of hypothetical judgments are

- $\Gamma \vdash A \; {\rm type}$, meaning that $A$ is a well-formed type in the context $\Gamma$,
- $\Gamma \vdash a {:} A$, meaning that $a$ has type $A$ in context $\Gamma$,
- $\Gamma \vdash A = A'$, meaning that $A$ and $A'$ are equal types in the context $\Gamma$,
- $\Gamma \vdash a = a' {:} A$, meaning that $a$ and $a'$ are equal elements of type $A$ in the context $\Gamma$.

Under the proposition as types interpretation

$$\tag{2}\label{analytic} \vdash a {:} A $$

can be understood as the judgment that $a$ is a proof-object for the proposition $A$. When suppressing this object we get a judgment corresponding to the one in ordinary first-order logic (see above):

$$\tag{3}\label{synthetic} \vdash A\; {\rm true}. $$

Remark 3.1. Martin-Löf (1994) argues that Kant’s *analytic judgment a priori* and *synthetic judgment a priori* can be exemplified, in the realm of logic, by ([analytic]) and ([synthetic]) respectively. In the analytic judgment ([analytic]) everything that is needed to make the judgment evident is explicit. For its synthetic version ([synthetic]) a possibly complicated proof construction $a$ needs to be provided to make it evident. This understanding of analyticity and syntheticity has the surprising consequence that “the logical laws in their usual formulation are all synthetic.” Martin-Löf (1994: 95). His analysis further gives:

> “ […] the logic of analytic judgments, that is, the logic for deriving judgments of the two analytic forms, is complete and decidable, whereas the logic of synthetic judgments is incomplete and undecidable, as was shown by Gödel.” Martin-Löf (1994: 97).

The decidability of the two analytic judgments ($\vdash a{:}A$ and $\vdash a=b{:}A$) hinges on the metamathematical properties of type theory: strong normalization and decidable type checking.

Sometimes also the following forms are explicitly considered to be judgments of the theory:

- $\Gamma \; {\rm context}$, meaning that $\Gamma$ is a well-formed context.
- $\Gamma = \Gamma'$, meaning that $\Gamma$ and $\Gamma'$ are equal contexts.

Below we shall abbreviate the judgment $\Gamma \vdash A \; {\rm type}$ as $\Gamma \vdash A$ and $\Gamma \; {\rm context}$ as $\Gamma \vdash.$

### 3.3 Inference Rules

When stating the rules we will use the letter $\Gamma$ as a meta-variable ranging over contexts, $A,B,\ldots$ as meta-variables ranging over types, and $a,b,c,d,e,f,\ldots$ as meta-variables ranging over terms.

The first group of inference rules are general rules including rules of assumption, substitution, and context formation. There are also rules which express that equalities are equivalence relations. There are numerous such rules, and we only show the particularly important *rule of type equality* which is crucial for computation in types:

$$\frac{\Gamma \vdash a {:} A\hspace{2em}\Gamma \vdash A = B} {\Gamma \vdash a {:} B}$$

The remaining rules are specific to the type formers. These are classified as formation, introduction, elimination, and equality rules.

### 3.4 Intuitionistic Predicate Logic

We only give the rules for $\Pi$. There are analogous rules for the other type formers corresponding to the logical constants of typed predicate logic.

In the following $B[x := a]$ means the term obtained by substituting the term $a$ for each free occurrence of the variable $x$ in $B$ (avoiding variable capture).

$\Pi$-formation. $$\frac{\Gamma \vdash A\hspace{2em} \Gamma, x {:} A \vdash B} {\Gamma \vdash \Pi x {:} A. B}$$

$\Pi$-introduction. $$\frac{\Gamma, x {:} A \vdash b {:} B} {\Gamma \vdash \lambda x. b {:} \Pi x {:} A. B}$$

$\Pi$-elimination. $$\frac {\Gamma \vdash f {:} \Pi x {:} A.B\hspace{2em}\Gamma \vdash a {:} A} {\Gamma \vdash f\,a {:} B[x := a]}$$

$\Pi$-equality. $$\frac {\Gamma, x {:} A \vdash b {:} B\hspace{2em}\Gamma \vdash a {:} A} {\Gamma \vdash (\lambda x.b)\,a = b[x := a] {:} B[x := a]}$$

This is the rule of $\beta$-conversion. We may also add the rule of $\eta$-conversion: $$\frac {\Gamma \vdash f {:} \Pi x {:} A. B} {\Gamma \vdash \lambda x. f\,x = f {:} \Pi x {:} A. B}.$$

Furthermore, there are congruence rules expressing that operations introduced by the formation, introduction, and elimination rules preserve equality. For example, the congruence rule for $\Pi$ is

$$\frac{\Gamma \vdash A = A'\hspace{2em} \Gamma, x {:} A \vdash B=B'} {\Gamma \vdash \Pi x {:} A. B = \Pi x {:} A'. B'}.$$

### 3.5 Natural Numbers

As in Peano arithmetic the natural numbers are generated by 0 and the successor operation $\s$. The elimination rule states that these are the only possible ways to generate a natural number.

We write $f(c) = \R(c,d,xy.e)$ for the function which is defined by primitive recursion on the natural number $c$ with base case $d$ and step function $xy.e$ (or alternatively $\lambda xy.e$) which maps the value $y$ for the previous number $x {:} \N$ to the value for $\s(x)$. Note that $\R$ is a new variable-binding operator: the variables $x$ and $y$ become bound in $e$.

$\N$-formation. $$\Gamma \vdash \N$$

$\N$-introduction. $$\Gamma \vdash 0 {:} \N \hspace{2em} \frac{\Gamma \vdash a {:} \N} {\Gamma \vdash s(a) {:} \N}$$

$\N$-elimination.

$$\frac{ \Gamma, x {:} \N \vdash C \hspace{1em} \Gamma \vdash c {:} \N \hspace{1em} \Gamma \vdash d {:} C[x := 0] \hspace{1em} \Gamma, y {:} \N, z {:} C[x := y] \vdash e {:} C[x := s(y)] } { \Gamma \vdash \R(c,d,yz.e) {:} C[x := c] }$$

$\N$-equality (under appropriate premises). $$\begin{align*} \R(0,d,yz.e) &= d {:} C[x := 0]\\ \R(s(a),d,yz.e) &= e[y := a, z := \R(a,d,yz.e)] {:} C[x := s(a)] \end{align*}$$

The rule of $\N$-elimination simultaneously expresses the type of a function defined by primitive recursion and, under the Curry-Howard interpretation, the rule of mathematical induction: we prove the property $C$ of a natural number $x$ by induction on $x$.

Gödel’s System $\T$ is essentially intuitionistic type theory with only the type formers $\N$ and $A \rightarrow B$ (the type of functions from $A$ to $B$, which is the special case of $(\Pi x {:} A)B$ where $B$ does not depend on $x {:} A$). Since there are no dependent types in System $\T$ the rules can be simplified.

### 3.6 The Universe of Small Types

Martin-Löf’s first version of type theory (Martin-Löf 1971a)[^martin-löf-1971a] had an axiom stating that there is a type of all types. This was proved inconsistent by Girard who found that the Burali-Forti paradox could be encoded in this theory.

To overcome this pathological impredicativity, but still retain some of its expressivity, Martin-Löf introduced in 1972 a universe $\U$ of small types closed under all type formers of the theory, except itself (Martin-Löf 1998 [1972])[^martin-löf-1998]. The rules are:

$\U$-formation. $$\Gamma \vdash \U$$

$\U$-introduction. $$\Gamma \vdash \varnothing {:} \U \hspace{3em} \Gamma \vdash 1 {:} \U$$ $$\frac{\Gamma \vdash A {:} \U\hspace{2em} \Gamma \vdash B {:} \U} {\Gamma \vdash A + B {:} \U} \hspace{3em} \frac{\Gamma \vdash A {:} \U\hspace{2em} \Gamma \vdash B {:} \U} {\Gamma \vdash A \times B {:} \U}$$ $$\frac{\Gamma \vdash A {:} \U\hspace{2em} \Gamma \vdash B {:} \U} {\Gamma \vdash A \rightarrow B {:} \U}$$ $$\frac{\Gamma \vdash A {:} U\hspace{2em} \Gamma, x {:} A \vdash B {:} \U} {\Gamma \vdash \Sigma x {:} A.\, B {:} \U} \hspace{3em} \frac{\Gamma \vdash A {:} \U\hspace{2em} \Gamma, x {:} A \vdash B {:} \U} {\Gamma \vdash \Pi x {:} A.\, B {:} \U}$$ $$\Gamma \vdash \N {:} \U$$

$\U$-elimination. $$\frac{\Gamma \vdash A {:} \U} {\Gamma \vdash A}$$

Since $\U$ is a type, we can use $\N$-elimination to define small types by primitive recursion. For example, if $A : \U$, we can define the type of $n$-tuples of elements in $A$ as follows:

$$A^n = \R(n,1,xy.A \times y) {:} \U$$

This type-theoretic universe $\U$ is analogous to a Grothendieck universe in set theory which is a set of sets closed under all the ways sets can be constructed in Zermelo-Fraenkel set theory. The existence of a Grothendieck universe cannot be proved from the usual axioms of Zermelo-Fraenkel set theory but needs a new axiom.

In Martin-Löf (1975) the universe is extended to a countable hierarchy of universes

$$\U_0 : \U_1 : \U_2 : \cdots .$$

In this way each type has a type, not only each small type.

### 3.7 Propositional Identity

Above, we introduced the equality judgment

$$\tag{4}\label{defeq} \Gamma \vdash a = a' {:} A.$$

This is usually called a “definitional equality” because it can be decided by normalizing the terms $a$ and $a'$ and checking whether the normal forms are identical. However, this equality is a judgment and not a proposition (type) and we cannot prove such judgmental equalities by induction. For this reason we need to introduce propositional identity types. For example, the identity type for natural numbers $\I(\N,m,n)$can be defined by $\U$-valued primitive recursion. We can then express and prove the Peano axioms. Moreover, extensional equality of functions can be defined by

$$\I(\N\rightarrow \N,f,f') = \Pi x {:} \N. \I(\N,f\,x,f'\,x).$$

### 3.8 The Axiom of Choice is a Theorem

The following form of the axiom of choice (the type-theoretic axiom of choice) is an immediate consequence of the BHK-interpretation of the intuitionistic quantifiers, and is easily proved in intuitionistic type theory:

$$(\Pi x {:} A. \Sigma y {:} B. C) \rightarrow \Sigma f {:} (\Pi x {:} A. B). C[y := f\,x]$$

The reason is that $\Pi x {:} A. \Sigma y {:} B. C$ is the type of functions which map elements $x {:} A$ to pairs $(y,z)$ with $y {:} B$ and $z {:} C$. The choice function $f$ is obtained by returning the first component $y {:} B$ of this pair.

It is perhaps surprising that intuitionistic type theory directly validates an axiom of choice, since this axiom is often considered problematic from a constructive point of view. A possible explanation for this state of affairs is that the above is an axiom of choice for *types*, and that types are not in general appropriate constructive approximations of sets in the classical sense. For example, we can represent a real number as a Cauchy sequence in intuitionistic type theory, but the set of real numbers is not the type of Cauchy sequences, but the type of Cauchy sequences up to equiconvergence. More generally, a set in Bishop’s constructive mathematics is represented by a type together with an equivalence relation.

If $A$ and $B$ are equipped with equivalence relations, there is of course no guarantee that the choice function, $f$ above, is extensional in the sense that it maps equivalent element to equivalent elements. This is the failure of the *extensional axiom of choice*, see Martin-Löf (2009) for an analysis.

## 4. Extensions

### 4.1 The Logical Framework

The above completes the description of a core version of intuitionistic type theory close to that of (Martin-Löf 1998 [1972])[^martin-löf-1998].

In 1986 Martin-Löf proposed a reformulation of intuitionistic type theory; see Nordström, Peterson and Smith (1990) for an exposition. The purpose was to give a more compact formulation, where $\lambda$ and $\Pi$ are the only variable binding operations. It is nowadays considered the main version of the theory. It is also the basis for the Agda proof assistant. The 1986 theory has two parts:

- the theory of types (the logical framework);
- the theory of sets (small types).

Remark 4.1. Note that the word “set” is used in several different senses in the type theory community. In the logical framework it means “small type”. In Bishop’s constructive mathematics it means a type with an equivalence relations. To avoid confusion the latter are often called “setoids” or “extensional sets” in type. A third use of the word “set” is in homotopy type theory is as “h-set” meaning a type the identity type of which is a proposition. See below.

The logical framework has only two type formers: $\Pi x {:} A. B$ (usually written $(x {:} A)B$ or $(x {:} A) \rightarrow B$ in the logical framework formulation) and $\U$ (usually called $\Set$). The rules for $\Pi x{:} A. B$ ($(x {:} A) \rightarrow B$) are the same as given above (including $\eta$-conversion). The rules for $\U$ ($\Set$) are also the same, except that the logical framework only stipulates closure under $\Pi$-type formation.

The other small type formers (“set formers”) are introduced in the theory of sets. In the logical framework formulation each formation, introduction, and elimination rule can be expressed as the typing of a new constant. For example, the rules for natural numbers become

$$\begin{align*} \N &: \Set,\\ 0 &: \N,\\ \s &: \N \rightarrow \N,\\ \R &: (C {:} \N \rightarrow \Set) \rightarrow C\,0 \rightarrow (( x {:} \N) \rightarrow C\,x \rightarrow C\,(\s\,x)) \rightarrow (c {:} \N) \rightarrow C\,c. \end{align*}$$

where we have omitted the common context $\Gamma$, since the types of these constants are closed. Note that the recursion operator $R$ has a first argument $C {:} \N \rightarrow \Set$ unlike in the original formulation.

Moreover, the equality rules can be expressed as equations

$$\begin{align*} \R\, C\, d\, e\, 0 &= d {:} C\,0\\ \R\, C\, d\, e\, (\s\, a) &= e\, a\, (\R\, C\, d\, e\, a) {:} C\,(\s\,a) \end{align*}$$

under suitable assumptions.

In the sequel we will present several extensions of type theory. To keep the presentation uniform we will however *not* use the logical framework presentation of type theory, but will use the same notation as in section 2.

### 4.2 A General Identity Type Former

As we mentioned above, identity on natural numbers can be defined by primitive recursion. Identity relations on other types can also be defined in the basic version of intuitionistic type theory presented in section 2.

However, Martin-Löf (1975) extended intuitionistic type theory with a uniform primitive identity type former $\I$ for all types. The rules for $\I$ express that the identity relation is inductively generated by the proof of reflexivity, a canonicial constant called $\r$. (Note that $\r$ was coded by the number 0 in the introductory presentation of proof-objects in 2.3). The elimination rule for the identity type is a generalization of identity elimination in predicate logic and introduces an elimination constant $\J$. We here show the formulation due to Paulin-Mohring (1993) rather than the original formulation of Martin-Löf (1975). The inference rules are the following.

$\I$-formation. $$\frac{\Gamma \vdash A \hspace{1em} \Gamma \vdash a {:} A \hspace{1em} \Gamma \vdash a' {:} A} {\Gamma \vdash \I(A,a,a')}$$

$\I$-introduction. $$\frac{\Gamma \vdash A \hspace{1em} \Gamma \vdash a {:} A} {\Gamma \vdash \r {:} \I(A,a,a)}$$

$\I$-elimination.

$$\frac{ \Gamma, x {:} A, y {:} \I(A,a,x) \vdash C \hspace{1em} \Gamma \vdash b {:} A \hspace{1em} \Gamma \vdash c {:} \I(A,a,b) \hspace{1em} \Gamma \vdash d {:} C[x := a, y := r]} { \Gamma \vdash \J(c,d) {:} C[x := b, y:= c]}$$

$\I$-equality (under appropriate assumptions).

$$\begin{align*} \J(r,d) &= d \end{align*}$$

Note that if $C$ only depends on $x : A$ and not on the proof $y : \I(A,a,x)$ (and we also suppress proof objects) in the rule of $\I$-elimination we recover the rule of identity elimination in predicate logic.

By constructing a model of type theory where types are interpreted as *groupoids* (categories where all arrows are isomorphisms) Hofmann and Streicher (1998) showed that it cannot be proved in intuitionistic type theory that all proofs of $I(A,a,b)$ are identical. This may seem as an incompleteness of the theory and Streicher suggested a new axiom $\K$ from which it follows that all proofs of $\I(A,a,b)$ are identical to $\r$.

The $\I$-type is often called the *intensional identity type*, since it does not satisfy the principle of function extensionality. Intuitionistic type theory with the intensional identity type is also often called *intensional intuitionistic type theory* to distinguish it from *extensional intuitionistic type theory* which will be presented in section 7.1.

### 4.3 Well-Founded Trees

A type of well-founded trees of the form $\W x {:} A. B$ was introduced in Martin-Löf 1982 (and in a more restricted form by Scott 1970)[^scott-1970]. Elements of $\W x {:} A. B$ are trees of varying and arbitrary branching: varying, because the branching type $B$ is indexed by $x {:} A$ and arbitrary because $B$ can be arbitrary. The type is given by a *generalized inductive definition* since the well-founded trees may be infinitely branching. We can think of $\W x{:}A. B$ as the free term algebra, where each $a {:} A$ represents a term constructor $\sup\,a$ with (possibly infinite) arity $B[x := a]$.

$\W$-formation. $$\frac{\Gamma \vdash A\hspace{2em} \Gamma, x {:} A \vdash B} {\Gamma \vdash \W x {:} A. B}$$

$\W$-introduction. $$\frac{\Gamma \vdash a {:} A \hspace{2em} \Gamma, y {:} B[x:=a] \vdash b : Wx{:}A. B} {\Gamma \vdash \sup(a, y.b) : \W x {:} A. B}$$

We omit the rules of $\W$-elimination and $\W$-equality.

Adding well-founded trees to intuitionistic type theory increases its proof-theoretic strength significantly (Setzer (1998)).

### 4.4 Iterative Sets and CZF

An important application of well-founded trees is Aczel’s (1978) construction of a type-theoretic model of Constructive Zermelo Fraenkel Set Theory. To this end he defines the type of iterative sets as

$$\V = \W x {:} \U. x.$$

Let $A {:} \U$ be a small type, and $x {:} A\vdash M$ be an indexed family of iterative sets. Then $\sup(A,x.M)$, or with a more suggestive notation $\{ M\mid x {:} A\}$, is an iterative set. To paraphrase: an iterative set is a family of iterative sets indexed by a small type.

Note that an iterative set is a data-structure in the sense of functional programming: a possibly infinitely branching well-founded tree. Different trees may represent the same set. We therefore need to define a notion of extensional equality between iterative sets which disregards repetition and order of elements. This definition is formally similar to the definition of bisimulation of processes in process algebra. The type $\V$ up to extensional equality can be viewed as a constructive type-theoretic model of the cumulative hierarchy, see the entry on set theory: constructive and intuitionistic ZF for further information about CZF.

### 4.5 Inductive Definitions

The notion of an inductive definition is fundamental in intuitionistic type theory. It is a primitive notion and not, as in set theory, a derived notion where an inductively defined set is defined impredicatively as the smallest set closed under some rules. However, in intuitionistic type theory inductive definitions are considered predicative: they are viewed as being built up from below.

The inductive definability of types is inherent in the meaning explanations of intuitionistic type theory which we shall discuss in the next section. In fact, intuitionistic type theory can be described briefly as a theory of inductive, recursive, and inductive-recursive definitions based on a framework of lambda calculus with dependent types.

We have already seen the type of natural numbers and the type of well-founded trees as examples of types given by inductive definitions; the natural numbers is an example of an ordinary finitary inductive definition and the well-founded trees of a generalized possibly infinitary inductive definition. The introduction rules describe how elements of these types are inductively generated and the elimination and equality rules describe how functions from these types can be defined by structural recursion on the way these elements are generated. According to the propositions as types principle, the elimination rules are simultaneously rules for proof by structural induction on the way the elements are generated.

The type formers $0, 1, +, \times, \rightarrow, \Sigma,$ and $\Pi$ which interpret the logical constants for intuitionistic predicate logic are examples of degenerate inductive definitions. Even the identity type (in intensional intuitionistic type theory) is inductively generated; it is the type of proofs generated by the reflexivity axiom. Its elimination rule expresses proof by pattern matching on the proof of reflexivity.

The common structure of the rules of the type formers can be captured by a general schema for inductive definitions (Dybjer 1991)[^dybjer-1991]. This general schema has many useful instances, for example, the type $\List(A)$ of lists with elements of type $A$ has the following introduction rules:

$$\Gamma \vdash \nil {:} \List(A) \hspace{3em} \frac{\Gamma \vdash a {:} A\hspace{2em}\Gamma \vdash as {:} \List(A)} {\Gamma \vdash \cons(a,as) {:} \List(A)}$$

Other useful instances are types of binary trees and other trees such as the infinitely branching trees of the Brouwer ordinals of the second and higher number classes.

The general schema does not only cover inductively defined types, but also inductively defined families of types, such as the identity relation. The above mentioned type $A^n$ of $n$-tuples of type $A$ was defined above by primitive recursion on $n$. It can also be defined as an inductive family with the following introduction rules

$$\Gamma \vdash \nil {:} A^0 \hspace{3em} \frac{\Gamma \vdash a {:} A\hspace{2em}\Gamma \vdash as {:} A^n} {\Gamma \vdash \cons(a,as) {:} A^{\s(n)}}$$

The schema for inductive types and families is a type-theoretic generalization of a schema for iterated inductive definitions in predicate logic (formulated in natural deduction) presented by Martin-Löf (1971b). This paper immediately preceded Martin-Löf’s first version of intuitionistic type theory. It is both conceptually and technically a forerunner to the development of the theory.

It is an essential feature of proof assistants such as Agda and Coq that it enables users to define their own inductive types and families by listing their introduction rules (the types of their constructors). This is much like in typed functional programming languages such as Haskell and the different dialects of ML. However, unlike in these programming languages the schema for inductive definitions in intuitionistic type theory enforces a restriction amounting to well-foundedness of the elements of the defined types.

### 4.6 Inductive-Recursive Definitions

We already mentioned that there are two main definition principles in intuitionistic type theory: the inductive definition of types (sets) and the (primitive, structural) definition of functions by recursion on the way the elements of such types are inductively generated. Usually, the inductive definition of a set comes first: the formation and introduction rules make no reference to the elimination rule. However, there are definitions in intuitionistic type theory for which this is not the case and we simultaneously inductively generate a type and a function from that type defined by structural recursion. Such definitions are simultaneously *inductive-recursive*.

The first example of such an inductive-recursive definition is an alternative formulation *à la Tarski* of the universe of small types. Above we presented the universe formulated *à la Russell*, where there is no notational distinction between the element $A {:} \U$ and the corresponding type $A$. For a universe *à la* Tarski there is such a distinction, for example, between the element $\hat{\N} {:} \U$ and the corresponding type $\N$. The element $\hat{\N}$ is called the *code* for $\N$.

The elimination rule for the universe *à la* Tarski is:

$$\frac{\Gamma \vdash a {:} \U} {\Gamma \vdash \T(a)}$$

This expresses that there is a function $\T$ which maps a code $a$ to its corresponding type $T(a)$. The equality rules define this correspondence. For example,

$$\T(\hat{\N}) = \N.$$

We see that $\U$ is inductively generated with one introduction rule for each small type former, and $\T$ is defined by recursion on these small type formers. The simultaneous inductive-recursive nature of this definition becomes apparent in the rules for $\Pi$ for example. The introduction rule is

$$\frac{\Gamma \vdash a {:} \U\hspace{2em} \Gamma, x {:} \T(a) \vdash b {:} \U} {\Gamma \vdash \hat{\Pi} x {:} a. b {:} \U}$$

and the corresponding equality rule is

$$\T(\hat{\Pi}x {:} a. b) = \Pi x {:} \T(a). \T(b)$$

Note that the introduction rule for $\U$ refers to $\T$, and hence that $\U$ and $\T$ must be defined simultaneously.

There are a number of other universe constructions which are defined inductive-recursively: universe hierarchies, superuniverses (Palmgren 1998; Rathjen, Griffor, and Palmgren 1998)[^palmgren-1998][^rathjen-1998], and Mahlo universes (Setzer 2000)[^setzer-2000]. These universes are analogues of certain large cardinals in set theory: inaccessible, hyperinaccessible, and Mahlo cardinals.

Other examples of inductive-recursive definitions include an informal definition of computability predicates used by Martin-Löf in an early normalization proof of intuitionistic type theory (Martin-Löf 1998 [1972])[^martin-löf-1998]. There are also many natural examples of “small” inductive-recursive definitions, where the recursively defined (decoding) function returns an element of a type rather than a type.

A large class of inductive-recursive definitions, including the above, can be captured by a general schema (Dybjer 2000, Dybjer and Setzer 1999)[^dybjer-2000][^dybjer-1999] which extends the schema for inductive definitions mentioned above. As shown by Setzer, intuitionistic type theory with this class of inductive-recursive definitions is very strong proof-theoretically (Dybjer and Setzer 2003)[^dybjer-2003]. However, as proposed in recent unpublished work by Setzer, it is possible to increase the strength of the theory even further and define universes such as an *autonomous Mahlo universe* which are analogues of even larger cardinals.

## 5. Meaning Explanations

The consistency of intuitionistic type theory relative to set theory can be proved by model constructions. Perhaps the simplest method is an interpretation whereby each type-theoretic concept is given its corresponding set-theoretic meaning, as outlined in section 2.3. For example the type of functions $A \rightarrow B$ is interpreted as the set of all functions in the set-theoretic sense between the set denoted by $A$ and the set denoted by $B$. To interpret $\U$ we need a set-theoretic universe which is closed under all (set-theoretic analogues of) the type constructors. Such a universe can be proved to exist if we assume the existence of an inaccessible cardinal $\kappa$ and interpret $\U$ by $V_\kappa$ in the cumulative hierarchy.

Alternatives are realizability models, and for intensional type theory, a model of terms in normal forms. The latter can also be used for proving decidability of the judgments of the theory.

Mathematical models only prove consistency relative to classical set theory (or whatever other meta-theory we are using). Is it possible to be convinced about the consistency of the theory in a more direct way, so called *simple minded consistency* (Martin-Löf 1984)[^martin-löf-1984]? In fact, is there a way to explain what it *means* for a judgment to be correct in a direct *pre-mathematical* way? And given that we know what the judgments mean can we then be convinced that the inference rules of the theory are valid? An answer to this problem was proposed by Martin-Löf in 1979 in the paper “Constructive Mathematics and Computer Programming” (Martin-Löf 1982)[^martin-löf-1982] and elaborated later on in numerous lectures and notes, see for example, Martin-Löf (1984, 1987). These meaning explanations for intuitionistic type theory are also referred to as the *direct semantics*, *intuitive semantics*, *informal semantics*, *standard semantics*, or the *syntactico-semantical* approach to meaning theory.

This meaning theory follows the Wittgensteinian meaning-as-use tradition. The meaning is based on rules for building objects (introduction rules) of types and computation rules (elimination rules) for computing with these objects. A difference from much of the Wittgensteinian tradition is that also higher order types like $\N \rightarrow \N$ are given meaning using rules.

To explain the meaning of a judgment we must first know how the terms in the judgment are computed to canonical form. Then the formation rules explain how correct canonical types are built and the introduction rules explain how correct canonical objects of such canonical types are built. We quote (Martin-Löf 1982)[^martin-löf-1982]:

> A canonical type $A$ is defined by prescribing how a canonical object of type $A$ is formed as well as how two equal canonical objects of type $A$ are formed. There is no limitation on this prescription except that the relation of equality which it defines between canonical objects of type $A$ must be reflexive, symmetric and transitive.

In other words, a canonical type is equipped with an equivalence relation on the canonical objects. Below we shall give a simplified form of the meaning explanations, where this equivalence relation is extensional identity of objects.

In spite of the *pre-mathematical* nature of this meaning theory, its technical aspects can be captured as a mathematical model construction similar to Kleene’s *realizability* interpretation of intuitionistic logic, see the next section. The realizers here are the terms of type theory rather than the number realizers used by Kleene.

### 5.1 Computation to Canonical Form

The meaning of a judgment is explained in terms of the computation of the types and terms in the judgment. These computations stop when a canonical form is reached. By canonical form we mean a term where the outermost form is a constructor (introduction form). These are the canonical forms used in lazy functional programming (for example in the Haskell language).

For the purpose of illustration we consider meaning explanations only for three type formers: $\N, \Pi x {:} A.B$, and $\U$. The context free grammar for the terms of this fragment of Intuitionistic Type Theory is as follows:

$$ a :: = 0 \mid \s(a) \mid \lambda x.a \mid \N \mid \Pi x{:}a.a \mid \U \mid \R(a,a,xx.a) \mid a\,a . $$

The canonical terms are generated by the following grammar:

$$v :: = 0 \mid \s(a) \mid \lambda x.a \mid \N \mid \Pi x{:}a.a \mid \U ,$$

where $a$ ranges over arbitrary, not necessarily canonical, terms. Note that $\s(a)$ is canonical even if $a$ is not.

To explain how terms are computed to canonical form, we introduce the relation $a \Rightarrow v$ between *closed* terms $a$ and canonical forms (values) $v$ given by the following computation rules:

$$ \frac{c \Rightarrow 0\hspace{1em}d \Rightarrow v}{\R(c,d,xy.e)\Rightarrow v} \hspace{2em} \frac{c \Rightarrow \s(a)\hspace{1em}e[x := d,y := \R(a,d,xy.e)]\Rightarrow v}{\R(c,d,xy.e)\Rightarrow v} $$ $$ \frac{f\Rightarrow \lambda x.b\hspace{1em}b[x := a]\Rightarrow v}{f\,a \Rightarrow v} $$

in addition to the rule

$$v \Rightarrow v$$

stating that a canonical term has itself as value.

### 5.2 The Meaning of Categorical Judgments

A categorical judgment is a judgment where the context is empty and there are no free variables.

The meaning of the categorical judgment $\vdash A$ is that $A$ has a canonical type as value. In our fragment this means that either of the following holds:

- $A \Rightarrow \N$,
- $A \Rightarrow \U$,
- $A \Rightarrow \Pi x {:} B. C$ and furthermore that $\vdash B$ and $x {:} B \vdash C$.

The meaning of the categorical judgment $\vdash a {:} A$ is that $a$ has a canonical term of the canonical type of $A$ as value. In our fragment this means that either of the following holds:

- $A \Rightarrow \N$ and either $a \Rightarrow 0$ or $a \Rightarrow \s(b)$ and $\vdash b {:} \N$,
- $A \Rightarrow \U$ and either $a \Rightarrow \N$ or $a \Rightarrow \Pi x {:} b. c$ where furthermore $\vdash b {:} \U$ and $x {:} b \vdash c {:} \U$,
- $A \Rightarrow \Pi x {:} B. C$ and $a \Rightarrow \lambda x.c$ and $x {:} B \vdash c {:} C$.

The meaning of the categorical judgment $\vdash A = A'$ is that $A$ and $A'$ have the same canonical types as values. In our fragment this means that either of the following holds:

- $A \Rightarrow \N$ and $A' \Rightarrow \N$,
- $A \Rightarrow \U$ and $A' \Rightarrow \U$,
- $A \Rightarrow \Pi x {:} B. C$ and $A' \Rightarrow \Pi x {:} B'. C'$ and furthermore that $\vdash B = B'$ and $x {:} B \vdash C = C'$.

The meaning of the categorical judgment $\vdash a = a' {:} A$ is explained in a similar way.

It is a tacit assumption of the meaning explanations that the repeated computations of canonical forms is well-founded. For example, a natural number is the result of finitely many computations of the successor function $\s$ ended by $0$. A computation which results in infinitely many computations of $\s$ is not a natural number in intuitionistic type theory. (However, there are extensions of type theory, for example, partial type theory, and non-standard type theory, where such infinite computations can occur, see section 7.3. To justify the rules of such theories the present meaning explanations do not suffice.)

### 5.3 The Meaning of Hypothetical Judgments

According to Martin-Löf (1982) the meaning of a hypothetical judgment is reduced to the meaning of the categorical judgments by substituting the closed terms of appropriate types for the free variables. For example, the meaning of

$$x_1 {:} A_1, \ldots, x_n {:} A_n \vdash a {:} A$$

is that the categorical judgment

$$\vdash a[x_1 := a_1, \ldots , x_n := a_n] : A[x_1 := a_1, \ldots , x_n := a_n]$$

is valid whenever the categorical judgments

$$\vdash a_1 {:} A_1, \ldots , \vdash a_n[x_1 := a_1, \ldots , x_{n-1} := a_{n-1}] {:} A_n[x_1 := a_1, \ldots , x_{n-1} := a_{n-1}]$$

are valid.

## 6. Mathematical Models

### 6.1 Categorical Models

#### 6.1.1 Hyperdoctrines

Curry’s correspondence between propositions and types was extended to predicate logic in the late 1960s by Howard (1980) and de Bruijn (1970). At around the same time Lawvere developed related ideas in categorical logic. In particular he proposed the notion of a *hyperdoctrine* (Lawvere 1970)[^lawvere-1970] as a categorical model of (typed) predicate logic. A hyperdoctrine is an indexed category $P {:} T^{op} \rightarrow \mathbf{Cat}$, where $T$ is a category with objects representing types and arrows representing terms. If $A$ is a type then $P(A)$ is a category of propositions depending on a variable $x {:} A$. The arrows in this category are proofs $Q \vdash R$ and can be thought of as proof-objects. Moreover, since we have an indexed category, for each arrow $t$ from $A$ to $B$, there is a reindexing functor $P(B) \rightarrow P(A)$representing substitution of $t$ for a variable $y {:} B$. The category $P(A)$ is assumed to be cartesian closed and conjunction and implications are modelled by products and exponentials in this category. The quantifiers $\exists$ and $\forall$ are modelled by the left and right adjoints of the reindexing functor. Moreover, Lawvere added further structure to hyperdoctrines to model identity propositions (as left adjoints to a diagonal functor) and a comprehension schema.

#### 6.1.2 Contextual categories, categories with attributes, and categories with families

Lawvere’s definition of hyperdoctrines preceded intuitionistic type theory but did not go all the way to identifying propositions and types. Nevertheless Lawvere influenced Scott’s (1970) work on *constructive validity*, a somewhat preliminary precursor of intuitionistic type theory. After Martin-Löf (1998 [1972]) had presented a more definite formulation of the theory, the first work on categorical models was presented by Cartmell in 1978 with his notions of category with attributes and contextual category (Cartmell 1986)[^cartmell-1986]. However, we will not define these structures here but instead the closely related *categories with families* (Dybjer 1996)[^dybjer-1996] which are formulated so that they directly model a variable-free version of a formulation of intuitionistic type theory with explicit substitutions.

A category with families is a functor  $T {\ :\ } C^{op} \rightarrow \mathbf{Fam}$, where $C$ is the category of contexts and substitutions and $\mathbf{Fam}$ is the category of families of sets. If $\Gamma$ is an object of $C$ (a context), then $T(\Gamma)$ is the family of terms of type $A$ which depend on variables in $\Gamma$. If $\gamma$ is an arrow in $C$ representing a substitution, then the arrow part of the functor represents substitution of $\gamma$ in types and terms. A category with families also has a terminal object and a notion of context comprehension, reminiscent of Lawvere’s comprehension in hyperdoctrines. The terminal object captures the rules for empty contexts and empty substitutions. Context comprehension captures the rules for extending contexts and substitutions, and has projections capturing weakening and assumption of the last variable.

Categories with families are algebraic structures which model the general rules of dependent type theory, those which come before the rules for specific type formers, such as $\Pi$, $\Sigma$, identity types, universes, etc. In order to model specific type-former corresponding extra structure needs to be added.

#### 6.1.3 Locally cartesian closed categories

From a categorical perspective the above-mentioned structures may appear somewhat special and ad hoc. A more regular structure which gives rise to models of intuitionistic type theory are the locally cartesian closed categories. These are categories with a terminal object, where each slice category is cartesian closed. It can be shown that the pullback functor has a left and a right adjoint, representing $\Sigma$- and $\Pi$-types, respectively. Locally cartesian closed categories correspond to intuitionistic type theory with extensional identity types and $\Sigma$ and $\Pi$-types (Seely 1984, Clairambault and Dybjer 2014)[^clairambault-2014][^seely-1984]. It should be remarked that the correspondence with intuitionistic type theory is somewhat indirect, since a coherence problem, in the sense of category theory, needs to be solved. The problem is that in locally cartesian closed categories type substituion is represented by pullbacks, but these are only defined up to isomorphism, see Curien (1993) and Hofmann (1994).

### 6.2 Set-Theoretic Models

Intuitionistic type theory is a possible framework for constructive mathematics in Bishop’s sense. Such constructive mathematics is compatible with classical mathematics: a constructive proof in Bishop’s sense can directly be understood as a proof in classical logic. A formal way to understand this is by constructing a set-theoretic model of intuitionistic type theory, where each concept of type theory is interpreted as the corresponding concept in Zermelo-Fraenkel Set Theory. For example, a type is interpreted as a set, and the type of functions in $A \rightarrow B$ is interpreted as the set of all functions in the set-theoretic sense from the set representing $A$ to the set representing $B$. The type of natural numbers is interpreted as the set of natural numbers. The interpretations of identity types, and $\Sigma$ and $\Pi$-types were already discussed in the introduction. And as already mentioned, to interpret the type-theoretic universe we need an inaccessible cardinal.

It can be shown that the interpretation outlined above can be carried out in Aczel’s constructive set theory CZF. Hence it does not depend on classical logic or impredicative features of set theory.

### 6.3 Realizability Models

The set-theoretic model can be criticized on the grounds that it models the type of functions as the set of all set-theoretic functions, in spite of the fact that a function in type theory is always computable, whereas a set-theoretic function may not be.

To remedy this problem one can instead construct a *realizability model* whereby one starts with a set of *realizers*. One can here follow Kleene’s numerical realizability closely where functions are realized by codes for Turing machines. Or alternatively, one can let realizers be terms in a lambda calculus or combinatory logic possibly extended with appropriate constants. Types are then represented by sets of realizers, or often as partial equivalence relations on the set of realizers. A partial equivalence relation is a convenient way to represent a type with a notion of “equality” on it.

There are many variations on the theme of realizability model. Some such models tacitly assume set theory as the metatheory (Aczel 1980, Beeson 1985)[^aczel-1980][^beeson-1985], whereas others explictly assume a constructive metatheory (Smith 1984)[^smith-1984].

Realizability models are also models of the extensional version of intuitionistic type theory (Martin-Löf 1982)[^martin-löf-1982] which will be presented in section 7.1 below.

### 6.4 Model of Normal Forms and Type-Checking

In intuitionistic type theory each type and each well-typed term has a normal form. A consequence of this normal form property is that all the judgments are decidable: for example, given a correct context $\Gamma$, a correct type $A$ and a possibly ill-typed term $a$, there is an algorithm for deciding whether $\Gamma \vdash a {:} A$. This type-checking algorithm is the key component of proof-assistants for Intensional Type Theory, such as Agda.

The correctness of the normal form property can be expressed as a model of normal forms, where each context, type, and term are interpreted as their respective normal forms.

### 6.5 Setoids, Groupoids, and Infinity-Groupoids

#### 6.5.1 Setoid model

As explained in the entry on *constructive mathematics*, when doing mathematics in type theory, one often needs to equip types with an equivalence relation, the combination being known as a setoid. Mappings are then functions that respect those equivalence relations. For example, we can define the real numbers as the setoid of Cauchy sequences with equi-convergence as the equivalence relation. However, developing mathematics using explicit setoids is inconvenient, since one must always check that equivalence relations are preserved by functions. It is therefore desirable to introduce a quotient type former, which maps a setoid to a type in such a way that equivalent elements are identified and functions automatically preserve the equivalence relation. Now, quotienting is not among the basic type formers of intuitionistic type theory, the rules of which are justified by the meaning explanations above. Instead we rely on the fact that setoids form a model of intuitionistic type theory with quotient formation (Hofmann 1995, Altenkirch et al 2019, Palmgren 2022)[^altenkirch-2019][^hofmann-1995][^palmgren-2022]. In this model, functions are required to preserve equivalence relations.

**6.5.2 Groupoid model**

A groupoid is a category where all arrows are isomorphisms. Setoids correspond to groupoids with at most one arrow between any two objects: the elements of the underlying type of the setoid correspond to the objects of the groupoid and the equivalence relation is isomorphism of objects. Groupoids form a model of intuitionistic type theory with a universe $\U$ (Hofmann and Streicher 1998)[^hofmann-1998], where elements of $\I(\U,A,B)$are isomorphisms between A and B. Since there may be several such isomorphism, Hofmann and Streicher’s model refutes the uniqueness of identity proofs rule of extensional type theory. Hofmann and Streicher also showed that the groupoid model justifies the prinicple of universe extensionality, stating that the substitution map associated with the $J$-operator

$$ \I(\U,A,B) \to A \cong B $$

has an inverse. This is a first step towards Voevodsky’s univalence axiom. The groupoid model also provides a first connection with homotopy theory. Objects correspond to points of a topological space and arrows correspond to paths between points. There may be several paths between two points, but paths are identified up to homotopy, that is, up to continuous tranformation of paths.

**6.5.3 Infinity groupoid models**

The identity type former $\I(A,a,b)$can be iterated. We can thus consider the type $\I(\I(A,a,b),p,q)$of identities between identity proofs $p, q : \I(A,a,b)$    , etc. This suggests a correspondence with higher categories and higher groupoids where one considers 2-cells (arrows between arrows), 3-cells (arrows between 2-cells), etc. Similarly, in homotopy theory one considers higher homotopies, such as homotopies between homotopies, etc. An infinity groupoid has $n$-cells for all $n$. Precise connections between identity types and infinity groupoids were discovered by (Awodey and Warren 2009)[^awodey-2009], (Lumsdaine 2010)[^lumsdaine-2010], and (van den Berg and Garner 2011)[^berg-2011]. Voevodsky realized that the whole of intensional intuitionistic type theory could be modelled by Kan simplical sets, a presentation of infinity groupoids studied in classical homotopy theory. This model satisfies the *univalence axiom* that states that the substitution map associated with the $J$-operator

$$\I(\U,A,B) \to A \simeq B$$

is an equivalence. Equivalence ($\simeq$) here refers to a general notion of equivalence of higher dimensional objects, as in the sequence *equal elements, isomorphic sets, equivalent groupoids, biequivalent bigroupoids*, etc. The univalence axiom expresses that “everything is preserved by equivalence”, thereby realizing the informal categorical slogan that all categorical constructions are preserved by isomorphism, and its generalization, that all constructions of categories are preserved by equivalence of categories, etc.

The axiom of univalence was originally justified by Voevodsky’s simplical set model. This model is however not constructive and (Bezem, Coquand and Huber 2014 [2013])[^bezem-2014] has instead proposed a model in Kan cubical sets. The construction of models that are both constructive and serve the purposes of homotopy theory is currently an active area of research.

## 7. Variants of the Theory

### 7.1 Extensional Type Theory

In extensional intuitionistic type theory (Martin-Löf 1982)[^martin-löf-1982] the rules of $\I$-elimination and $\I$-equality for the general identity type are replaced by the following two rules:

$$\frac{\Gamma\vdash c {:} \I(A,a,a')} {\Gamma \vdash a=a' {:} A} \hspace{3em} \frac{\Gamma\vdash c{:}\I(A,a,a')} {\Gamma\vdash c = \r {:} \I(A,a,a')}$$

The first causes the distinction between propositional and judgmental equality to disappear. The second forces identity proofs to be unique. Unlike the rules for the intensional identity type former, the rules for extensional identity types do not fit into the schema for inductively defined types mentioned above.

These rules are however justified by the meaning explanations in Martin-Löf (1982). This is because the categorical judgment

$$\vdash c {:} \I(A,a,a')$$

is valid iff $c \Rightarrow \r$ and the judgment $\vdash a = a' {:} A$ is valid.

However, these rules make it possible to define terms without normal forms. Since the type-checking algorithm relies on the computation of normal forms of types, it no longer works for extensional type theory, see (Castellan, Clairambault, and Dybjer 2015)[^castellan-2015].

On the other hand, certain constructions which are not available in intensional type theory are possible in extensional type theory. For example, function extensionality

$$(\Pi x {:} A. \I(B,f\,x,f'\,x)) \rightarrow \I(\Pi x{:}A.B,f,f')$$

is a theorem.

Another example is that $\W$-types can be used for encoding other inductively defined types in Extensional Type Theory. For example, the Brouwer ordinals of the second and higher number classes can be defined as special instances of the $\W$-type (Martin-Löf 1984)[^martin-löf-1984]. More generally, it can be shown that all inductively defined types which are given by a *strictly positive type operator* can be represented as instances of well-founded trees (Dybjer 1997)[^dybjer-1997].

### 7.2 Univalent Foundations and Homotopy Type Theory

Univalent foundations refer to Voevodsky’s programme for a new foundation of mathematics based on intuitionistic type theory with the univalence axiom as explained in section 6.5.3 about infinity groupoids. Voevodsky introduced the notion of h-level of a type. One defines an h-proposition as a type where all elements (proofs) are identified. Furthermore, one defines an h-set as a type A where the identity type $\I(A,a,b)$ is a proposition. An h-set is said to have h-level 0, and in general one defines a type A to have h-level $n+1$ provided $\I(A,a,b)$ has h-level $n$. Although univalent foundations concern preservation of mathematical structure in general, applications within homotopy theory are particularly actively investigated. Intensional type theory extended with the univalence axiom and so called higher inductive types is therefore also called “homotopy type theory”. We refer to the entry on type theory and the book on Homotopy type theory (The Univalent Foundations Program, 2013*)[^univalent-2013]* for details.

### 7.3 Partial and Non-Standard Type Theory

Intuitionistic type theory is not intended to model Brouwer’s notion of *free choice sequence*, although lawlike choice sequences can be modelled as functions from $\N$. However, there are extensions of the theory which incorporate such choice sequences: namely *partial type theory* and *non-standard type theory* (Martin-Löf 1990)[^martin-löf-1990]. The types in partial type theory can be interpreted as Scott domains (Martin-Löf 1986, Palmgren and Stoltenberg-Hansen 1990, Palmgren 1991)[^martin-löf-1986][^martin-löf-1990][^palmgren-1991][^palmgren-1990]. In this way a type $\N$ which contains an infinite number $\infty$ can be interpreted. However, in partial type theory all types are inhabited by a least element $\bot$, and thus the propositions as types principle is not maintained. Non-standard type theory incorporates non-standard elements, such as an infinite number $\infty {:} \N$ without inhabiting all types.

### 7.4 Impredicative Type Theory

The inconsistent version of intuitionistic type theory of Martin-Löf (1971a) was based on the strongly impredicative axiom that there is a type of all types. However, (Coquand and Huet 1988)[^coquand-1988] showed with their calculus of constructions, that there is a powerful impredicative but consistent version of type theory. In this theory the universe $\U$ (usually called ${\bf Prop}$ in this theory) is closed under the following formation rule for cartesian product of families of types:

$$\frac{\Gamma \vdash A \hspace{2em} \Gamma, x {:} A \vdash B {:} \U} {\Gamma \vdash \Pi x {:} A. B {:} \U}$$

This rule is more general than the rule for constructing small cartesian products of families of small types in intuitionistic type theory, since we can now quantify over arbitrary types $A$, including $\U$, and not just small types. We say that $\U$ is impredicative since we can construct a new element of it by quantifying over all elements, even the element which is constructed.

The motivation for this theory was that inductively defined types and families of types become definable in terms of impredicative quantification. For example, the type of natural numbers can be defined as the type of Church numerals:

$$\N = \Pi X {:} \U. X \rightarrow (X \rightarrow X) \rightarrow X {:} \U$$

This is an impredicative definition, since it is a small type which is constructed by quantification over all small types. Similarly we can define an identity type by impredicative quantification:

$$\I(A,a,a')= \Pi X {:} A \rightarrow \U. X\,a \rightarrow X\,a' {:} \U$$

This is Leibniz’ definition of equality: $a$ and $a'$ are equal iff they satisfy the same properties (ranged over by $X$).

Unlike in intuitionistic type theory, the function type in impredicative type cannot be interpreted set-theoretically in a straightfoward way, see (Reynolds 1984)[^reynolds-1984].

### 7.5 Proof Assistants

In 1979 Martin-Löf wrote the paper “Constructive Mathematics and Computer Programming” where he explained that intuitionistic type theory is a programming language which can also be used as a formal foundation for constructive mathematics. Shortly after that, interactive proof systems which help the user to derive valid judgments in the theory, so called proof assistants, were developed.

One of the first systems was the NuPrl system (PRL Group 1986)[^prl-1986], which is based on an extensional type theory similar to (Martin-Löf 1982)[^martin-löf-1982].

Systems based on versions of intensional type theory go back to the type-checker for the impredicative calculus of constructions which was written around 1984 by Coquand and Huet. This led to the Coq system, which is based on the calculus of inductive constructions (Paulin-Mohring 1993)[^paulin-mohring-1993], a theory which extends the calculus of construction with primitive inductive types and families. The encodings of the pure calculus of constructions were found to be inconvenient, since the full elimination rules could not be derived and instead had to be postulated. We also remark that the calculus of inductive constructions has a subsystem, the predicative calculus of inductive constructions, which follows the principles of Martin-Löf’s intuitionistic type theory.

Agda is another proof assistant which is based on the logical framework formulation of intuitionistic type theory, but adds numerous features inspired by practical programming languages (Norell 2008)[^norell-2008]. It is an intensional theory with decidable judgments and a type-checker similar to Coq’s. However, in contrast to Coq it is based on Martin-Löf’s predicative intuitionistic type theory.

There are several other systems based either on the calculus of constructions (Lego, Matita, Lean) or on intuitionistic type theory (Epigram, Idris); see (Pollack 1994; Asperti *et al.* 2011; de Moura *et al.* 2015; McBride and McKinna 2004; Brady 2011)[^asperti-2011][^brady-2011][^mcbride-2004][^moura-2015][^pollack-1994].

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=type-theory-intuitionistic). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/type-theory-intuitionistic/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=type-theory-intuitionistic&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/type-theory-intuitionistic/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- “[Constructive Mathematics](http://www.iep.utm.edu/con-math/),” entry in the *Internet Encyclopedia of Philosophy*.
- “[Computational Type Theory](http://www.scholarpedia.org/article/Computational_type_theory),” entry in *Scholarpedia*.
- “[Type Theory](https://ncatlab.org/nlab/show/type+theory),” in nLab, a wiki for collaborative work on mathematics, physics, and philosophy.

## Related Entries

logic, history of: intuitionistic logic | logic: intuitionistic | mathematics, philosophy of: intuitionism | mathematics: constructive | proof theory: development of | semantics: Montague | semantics: proof-theoretic | set theory | set theory: constructive and intuitionistic ZF | set theory: Zermelo’s axiomatization of | type theory | type theory: Church’s type theory

[^aczel-1978]: Aczel, Peter, 1978 [1977], “The type theoretic interpretation of constructive set theory”, in *Logic Colloquium ’77*, A. Macintyre, L. Pacholski, J. Paris (eds), Amsterdam-New York: North-Holland, pp. 55–66.

[^aczel-1980]: –––, 1980, “Frege Structures and the Notions of Proposition, Truth and Set”, in *The Kleene Symposium*, J. Barwise, H.J. Keisler, K. Kunen (eds), Studies in Logic and the Foundations of Mathematics 101, Amsterdam: North-Holland, pp. 31–59.

[^altenkirch-2019]: Altenkirch, Thorsten, Simon Boulier, Ambrus Kaposi, Nicolas Tabareau, 2019, “Setoid type theory – a syntactic translation”, MPC 2019 – *13th International Conference on Mathematics of Program Construction*, Oct 2019, Porto, Portugal. pp.155–196.

[^asperti-2011]: Asperti, Andrea, Wilmer Ricciotti, Claudio Sacerdoti Coen, and Enrico Tassi, 2011, “The Matita interactive theorem prover”, in *Automated deduction: CADE-23*, N. Bjørner and V. Sofronie-Stokkermans (eds), Lecture Notes in Computer Science (LNCS), vol. 6803, Heidelberg: Springer-Verlag, pp. 64–69.

[^awodey-2009]: Awodey, Steve and Michael A. Warren, 2009, “Homotopy theoretic models of identity types”, *Mathematical Proceedings of the Cambridge Philosophical Society*, 146(1): 45–55.

[^beeson-1985]: Beeson, Michael, 1985, *Foundations of Constructive Mathematics*, Springer-Verlag, Berlin.

[^berg-2011]: van den Berg, Benno and Richard Garner, 2011, “Types are weak $\omega$-groupoids”, *Proceedings of the London Mathematical Society*, 102(2): 370–394. doi:10.1112/plms/pdq026

[^bezem-2014]: Bezem, Marc, Thierry Coquand, and Simon Huber, 2014 [2013], “A model of type theory in cubical sets”, in *19th International Conference on Types for Proofs and Programs (TYPES 2013)*, Ralph Matthes and Aleksy Schubert (eds), Dagstuhl, Germany: Schloss Dagstuhl--Leibniz-Zentrum fuer Informatik, pp. 107–128.

[^bishop-1967]: Bishop, Errett, 1967, *Foundations of constructive analysis*, New York-Toronto, Ont.-London: McGraw-Hill Book Co..

[^brady-2011]: Brady, Edwin C., 2011, “IDRIS: systems programming meets full dependent types”, in *Proceedings of the 5th ACM workshop on Programming Languages meets Program Verification (PLPV 2011)*, pp. 43–54, doi:10.1145/1929529.1929536.

[^bruijn-1970]: de Bruijn, Nicholas G., 1970, “The mathematical language AUTOMATH, its usage, and some of its extensions”, in *Symposium on Automatic Demonstration (Versailles, 1968)*, Lecture Notes in Mathematics, Vol. 125, Berlin: Springer, pp. 29:61.

[^cartmell-1986]: Cartmell, John, 1986, “Generalised algebraic theories and contextual categories”, *Annals of Pure and Applied Logic*, 32: 209–243.

[^castellan-2015]: Castellan, Simon, Pierre Clairambault, and Peter Dybjer, 2015: “Undecidability of Equality in the Free Locally Cartesian Closed Category”, *TLCA* pp 138-152.

[^clairambault-2014]: Clairambault, Pierre and Peter Dybjer, 2014, “The biequivalence of locally cartesian closed categories and Martin-Löf type theories”, *Mathematical Structures in Computer Science*, 24(6). doi:10.1017/S0960129513000881

[^coquand-1988]: Coquand, Thierry and Gérard Huet, 1988, “The calculus of constructions”, *Information and Computation*, 76(2–3): 95–120, doi:10.1016/0890-5401(88)90005-3.

[^curien-1993]: Curien, Pierre-Louis, 1993, “Substitution up to isomorphism”, *Fundamentae Informatica*, 19: 51–85.

[^curry-1958]: Curry, Haskell B. and Robert Feys, 1958, *Combinatory Logic*, Amsterdam: North-Holland.

[^dybjer-1991]: Dybjer, Peter, 1991, “Inductive sets and families in Martin-Löf’s type theory and their set-theoretic semantics”, in *Logical Frameworks*, Gérard Huet and Gordon Plotkin (eds), Cambridge: Cambridge University Press, pp. 280–306 .

[^dybjer-1996]: –––, 1996, “Internal Type Theory”, in *Types for Proofs and Programs, TYPES '95*, Stefano Berardi and Mario Coppo (eds), Lecture Notes in Computer Science Volume (LNCS), vol. 1158, Heidelberg: Springer-Verlag, pp. 120–134.

[^dybjer-1997]: –––, 1997, “Representing inductively defined sets by wellorderings in Martin-Löf’s type theory”, *Theoretical Computer Science*, 176: 329–335.

[^dybjer-2000]: –––, 2000, “A general formulation of simultaneous inductive-recursive definitions in type theory”, *Journal of Symbolic Logic*, 65: 525–549.

[^dybjer-1999]: Dybjer, Peter and Anton Setzer, 1999, “A finite axiomatization of inductive-recursive definitions”, *Proceedings of Typed Lambda Calculi and Applications: 4th International Conference* (Lecture Notes in Computer Science: 1581), Dordrecht: Springer Verlag.

[^dybjer-2003]: –––, 2003, “Induction-recursion and initial algebras”, *Annals of Pure and Applied Logic*, 124: 1–47.

[^gonthier-2008]: Gonthier, Georges, 2008, “Formal proof of the four-color theorem”, *Notices American Mathematical Society*, 55: 1382–1393.

[^hofmann-1994]: Hofmann, Martin, 1994, “Interpretation of Type Theory in Locally Cartesian Closed Categories”, in *Proceedings of CSL*, Lecture Notes in Computer Science (LNCS), Berlin: Springer-Verlag. doi:10.1007/BFb0022273

[^hofmann-1995]: –––, 1995, *Extensional concepts in intensional type theory*, Ph.D. Thesis, University of Edinburgh.

[^hofmann-1997]: –––, 1997, “Syntax and semantics of dependent types”, in *Semantics and logics of computation*, Andrew M. Pitts and P. Dybjer (eds), Publications of the Newton Institure (No.14), Cambridge: Cambridge University Press, pp. 79–130.

[^hofmann-1998]: Hofmann, Martin and Thomas Streicher, 1998, “The groupoid interpretation of type theory”, in Sambin and Smith 1998: 83–111.

[^howard-1980]: Howard, William A., 1980, “The Formulae-as-Types Notion of Construction”, in *To H.B. Curry: Essays on Combinatory Logic, Lambda Calculus and Formalism*, J.P. Seldin and J.R. Hindley (eds), Academic Press, pp. 479–490.

[^jacobs-1999]: Jacobs, Bart, 1999, *Categorical logic and type theory*, Studies in Logic and the Foundations of Mathematics 141, Amsterdam: North-Holland.

[^lawvere-1970]: Lawvere, F. William, 1970, “Equality in Hyperdoctrines and Comprehension Schema as an Adjoint Functor”, in *Proceedings of the American Mathematical Society Symposium on Pure Mathematics XVII*, pp. 1–14.

[^leroy-2009]: Leroy, Xavier, 2009, “Formal verification of a realistic compiler”, *Communications of the ACM*, 52(7):107–115.

[^lumsdaine-2010]: Lumsdaine, Peter LeFanu, 2010, “Weak omega-categories from intensional type theory”, *Logical Methods in Computer Science*, 6(3), doi:10.2168/LMCS-6(3:24)2010, [[LeFanu Lumsdaine 2010 available online](http://www.lmcs-online.org/ojs/viewarticle.php?id=628)]

[^martin-löf-1971a]: Martin-Löf, Per, 1971a, *An intuitionistic theory of types*, unpublished preprint.

[^martin-löf-1971b]: –––, 1971b, “Hauptsatz for the intuitionistic theory of iterated inductive definitions”, in *Proceedings of the 2nd Scandinavian logic symposium*, J.E. Fenstad (ed.), Amsterdam: North-Holland, pp. 179–216.

[^martin-löf-1975]: –––, 1975, “An intuitionistic theory of types: Predicative part”, in *Logic colloquium ’73*, H.E. Rose and J. Shepherdson (eds), Amsterdam: North-Holland, pp. 73–118.

[^martin-löf-1982]: –––, 1982, “Constructive mathematics and computer programming”, in *Logic, methodology and philosophy of science VI, Proceedings of the 1979 international congress at Hannover, Germany*, L.J. Cohen, J. Los, H. Pfeiffer and K.-P. Podewski (eds). Amsterdam: North- Holland Publishing Company, pp. 153–175.

[^martin-löf-1984]: –––, 1984, *Intuitionistic type theory: Notes by Giovanni Sambin of a series of lectures given in Padua, June 1980*, Napoli: Bibliopolis.

[^martin-löf-1986]: –––, 1986, “Unifying Scott’s theory of domains for denotational semantics and intuitionistic type theory (abstract)”, in *Atti del Congresso ’Logica e Filosofia della Scienza, oggi’, San Gimignano, 7–11 December 1983, Vol. I – Logica*, CLUEB, Bologna.

[^martin-löf-1987]: –––, 1987, “Truth of a proposition, evidence of a judgment, validity of a proof”, *Synthese*, 73: 407–420.

[^martin-löf-1990]: –––, 1990, “Mathematics of infinity”, in *COLOG-88*, P. Martin-Löf and G. Mints (eds), Berlin: Springer, pp. 146–197.

[^martin-löf-1994]: –––, 1994, “Analytic and synthetic judgments in type theory”, in *Kant and contemporary epistemology*, P. Parrini (ed.), Dordrecht: Kluwer, pp. 87–99.

[^martin-löf-1996]: –––, 1996, “On the meanings of the logical constants and the justifications of the logical laws”, *Nordic Journal of Philosophical Logic*, 1(1): 11–60.

[^martin-löf-1998]: –––, 1998 [1972], “An intuitionistic theory of types”, in Sambin and Smith 1998: 127–172. (Written in 1972 but unpublished.)

[^martin-löf-2009]: –––, 2009, “100 years of Zermelo’s Axiom of Choice: What was the problem with it?” in *Logicism, intuitionism, and formalism: What has become of them?*, S. Lindström, E. Palmgren, K. Segerberg, and V. Stoltenberg-Hansen (eds), Dordrecht: Springer, pp. 209–219.

[^mcbride-2004]: McBride, Conor and James McKinna, 2004, “The view from the left”, *Journal of Functional Programming*, 14: 69–111.

[^moura-2015]: de Moura, Leonardo, Soonho Kong, Jeremy Avigad, Floris van Doorn and Jakob von Raumer, 2015, “The Lean Theorem Prover”, in *25th International Conference on Automated Deduction (CADE-25)*, Berlin, Germany. [[de Moura et al. 2015 available online](https://lean-lang.org/papers/system.pdf)]

[^nordström-1990]: Nordström, Bengt, Kent Petersson, and Jan M. Smith, 1990, *Programming in Martin-Löf’s type theory. An introduction*, New York: Oxford University Press.

[^norell-2008]: Norell, Ulf, 2008, “Dependently Typed Programming in Agda”, in *Proceedings of the 6th international conference on Advanced Functional Programming*, pp. 230–266.

[^palmgren-1991]: Palmgren, Erik, 1991, *On Fixed Point Operators, Inductive Definitions and Universes in Martin-Löf Type Theory*, Doctoral dissertation in mathematics, Uppsala University.

[^palmgren-1998]: –––, 1998, “On universes in type theory”, in Sambin and Smith 1998: 191-204.

[^palmgren-2022]: –––, 2022, “From type theory to setoids and back”, *Mathematical Structures in Computer Science*, 32(10): 1283–1312.

[^palmgren-1990]: Palmgren, Erik and Viggo Stoltenberg-Hansen, 1990 “Domain interpretations of Martin-Löf’s partial type theory”, *Annals of Pure and Applied Logic*, 48: 135–196.

[^paulin-mohring-1993]: Paulin-Mohring, Christine, 1993, “Inductive Definitions in the system Coq: Rules and Properties”, in *Proceedings of the International Conference on Typed Lambda Calculi and Applications, TLCA '93*, Marc Bezem and Jan F. Groote (eds), Lecture Notes in Computer Science (LNCS), Springer, pp. 328–345.

[^pollack-1994]: Pollack, Randy, 1994, *The theory of LEGO*, PhD Thesis, Edinburgh.

[^prl-1986]: PRL Group, 1986, *Implementing Mathematics with the Nuprl Proof Development System*, Engelwood Cliffs, NJ: Prentice-Hall.

[^ranta-1994]: Ranta, Aarne, 1994, *Type-theoretical Grammar*, Oxford: Oxford University Press.

[^rathjen-1998]: Rathjen, Michael, Edward R. Griffor, and Erik Palmgren, 1998, “Inaccessibility in constructive set theory and type theory”, *Annals of Pure and Applied Logic*, 94: 181–200.

[^reynolds-1984]: Reynolds, John C., 1984, “Polymorphism is not Set-Theoretic”, in *Semantics of Data Types: International Symposium Sophia-Antipolis, France, June 27–29, 1984 Proceedings*, Giles Kahn, David B. MacQueen, and Gordon Plotkin (eds), Lecture Notes in Computer Science (LNCS), vol. 173, Springer, pp. 145–156.

[^sambin-1998]: Sambin, G. and Jan M. Smith (eds), 1998, *Twenty-five years of constructive type theory*, Oxford: Clarendon Press.

[^scott-1970]: Scott, Dana S., 1970, “Constructive Validity”, in *Symposium on Automatics Demonstration (Versailles, December 1968*, M. Laudet, D. Lacombe, L. Nolin, and M. Schützenberg (eds), Lecture Notes in Mathematics, vol. 125, Springer, pp. 237–275.

[^seely-1984]: Seely, Robert A.G., 1984, “Locally cartesian closed categories and type theory”, *Mathematical Proceedings of the Cambridge Philosophical Society*, 95: 33–48.

[^setzer-1998]: Setzer, Anton, 1998, “Well-ordering proofs for Martin-Löf type theory”, *Annals of Pure and Applied Logic*, 92: 113–159.

[^setzer-2000]: –––, 2000, “Extending Martin-Löf type theory by one Mahlo-universe”, *Archive for Mathematical Logic*, 39: 155–181.

[^smith-1984]: Smith, Jan, 1984, “An interpretation of Martin-Löf’s type theory in a type-free theory of propositions”, *Journal of Symbolic Logic*, 49: 730–753.

[^sundholm-2012]: Sundholm, Göran, 2012, “On the Philosophical Work of Per Martin-Löf”, in P. Dybjer, S. Lindström, E. Palmgren, and G. Sundholm (eds), *Epistemology versus Ontology: Essays on the Philosophy and Foundations of Mathematics in Honour of Per Martin-Löf*, Springer, pp. xxiii–xxiv.

[^univalent-2013]: The Univalent Foundations Program, 2013, *Homotopy Type Theory: Univalent Foundations of Mathematics*, Institute for Advanced Study, Princeton. [[The Univalent Foundations Program 2013](http://homotopytypetheory.org/book) available online].
