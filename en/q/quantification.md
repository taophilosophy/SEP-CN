# Quantifiers and Quantification
**First published Wed Sep 3, 2014; substantive revision Sun Dec 18, 2022**

*Uzquiano, Gabriel*

Quantifier expressions are marks of generality. They come in many syntactic categories in English, but determiners like “all”, “each”, “some”, “many”, “most”, and “few” provide some of the most common examples of quantification.[^note-1] In English, they combine with singular or plural nouns, sometimes qualified by adjectives or relative clauses, to form explicitly restricted quantifier phrases such as “some apples”, “every material object”, or “most planets”. These quantifier phrases may in turn combine with predicates in order to form sentences such as “some apples are delicious”, “every material object is extended”, or “most planets are visible to the naked eye”. We may conceive of determiners like “every” and “some” as binary quantifiers of the form $Q(A,B)$, which may operate on two predicates, $A$ and $B$, in order to form a sentence.

Binary quantifiers of this sort played an important role in what is perhaps the first formal study of quantification developed by Aristotle in the *Prior Analytics*. The details of Aristotle’s syllogistic logic are given in the entry on Aristotle’s Logic. Aristotle investigated a restricted class of inferential patterns, which he called syllogisms, in which two *categorical propositions* served as premises and a third served as a conclusion. A categorical proposition is a sentence obtained from one of four binary quantifiers “$all(A, B)$”, “$some(A, B)$”, “$no(A, B)$” and “$not \ all(A, B)$”, when suitable predicates are substituted for $A$ and $B$. In a syllogism, each categorical proposition contains two of three shared predicates. The logical relations, which, according to Aristotelian logic, obtain between them are codified by the square of opposition. Although Aristotle’s syllogistic logic dominated logic for centuries, it eventually revealed itself inadequate for the representation of mathematical argumentation. Aristotelian logic finally became displaced by the advent of modern quantificational logic, which originated with George Boole’s algebraic approach to logic and Gottlob Frege’s approach to logic and quantification (1879).

Modern quantificational logic has chosen to focus instead on formal counterparts of the unary quantifiers “everything” and “something”, which may be written $\forall x$ and $\exists x$, respectively. They are unary quantifiers because they require a single argument in order to form a sentence of the form $\forall xA$ or $\exists xA$. Frege (and Russell) devised an ingenious procedure for regimenting binary quantifiers like “every” and “some” in terms of unary quantifiers like “everything” and “something”: they formalized sentences of the form $\ulcorner$Some $A$ is $B$$\urcorner$ and $\ulcorner$Every $A$ is $B$$\urcorner$ as $\exists x(Ax \wedge Bx)$ and $\forall x(Ax \rightarrow Bx)$, respectively. They analyzed a sentence like “some apples are delicious” in terms of the sentence “something is an apple and delicious”, whereas they parsed the sentence “every material object is extended” as “everything is extended, if it is a material object”. Unfortunately, this procedure cannot be generalized to cover quantifier phrases like “many”, “most”, or “few”. It would be a mistake to regiment the sentence “most planets are visible to the naked eye” by means of “most things are planets and visible to the naked eye” or “most things are such that they are visible to the naked eye, if they are planets”. Instead, they are better analyzed as irreducibly binary quantifiers, and their study has given rise to the theory of generalized quantifiers, which has become a fruitful subject of study partly because of its applications in the semantics of natural language.

## 1. Classical Quantificational Logic

What is now a commonplace treatment of quantification began with Frege (1879)[^frege-1879], where the German philosopher and mathematician, Gottlob Frege, devised a formal language equipped with quantifier symbols, which bound different styles of variables. He formulated axioms and rules of inference, which allowed him to represent a remarkable range of mathematical argumentation. Classical quantificational logic is sometimes known as “first-order” or “predicate” logic, which is generally taken to include functional and constant symbols. The vocabulary of classical quantificational logic is often supplemented with an identity predicate to yield the classical theory of quantification with identity.

### 1.1 Pure Quantificational Logic

At the core of classical quantificational logic lies what we may call pure quantificational logic, which makes no provision for any singular terms other than variables. In pure quantificational logic, one may still make use of Russell’s theory of definite description to simulate singular terms for which we have a method of contextual elimination.

#### 1.1.1 The Language of Pure Quantificational Logic

The vocabulary of pure quantificational logic contains the usual propositional connectives: $\lnot$, $\wedge$, $\vee$, $\rightarrow$, and $\leftrightarrow$. It contains predicate letters of different adicities: one-place predicate letters with or without subscripts, $P^{1}, Q^{1}, R^{1}, P^{1}_{1}$, …, two-place predicate letters, $P^{2}, Q^{2}, R^{2}, P^{2}_{1}$, …, and more generally, $n$-place predicate letters. Sentence letters are 0-place predicates. There is, in addition to this, an infinite stock of variables with or without subscripts: $x, y, z, x_1, y_1, z_1$, … , and two quantifiers $\forall$ and $\exists$. In a classical framework, we need not treat all these symbols as primitive; we may, for example, treat $\lnot$, $\rightarrow$, and $\forall$ as primitive and provide standard definitions for the other propositional connectives and quantifiers in terms of them. For example, the existential quantifier, $\exists x A$, may be defined: $\lnot \forall x\lnot A$.

The definition of a formula of the language of pure quantificational logic proceeds recursively as follows. First, one defines an *atomic formula* to consist of an $n$-place predicate followed by $n$ variables: $P^{n}_{i} x_{1}$, …, $x_{n}$. One then defines $A$ to be a formula of the language of pure quantificational logic if, and only if, (i) $A$ is an atomic formula, or (ii) $A$ is of the form $\lnot B$, where $B$ is a formula, or (iii) $A$ is of the form $(B \rightarrow C)$, where $B$ and $C$ are each a formula, or (iv) $A$ is of the form $\forall x B$, where $x_i$ is a variable and $B$ is a formula.[^note-2]

All occurrences of variables in an atomic formula are *free*. The free occurrences of variables in the negation of a formula $\lnot B$ are the free occurrences of variables in $B$. The free occurrences of variables in a formula of the form $(B \rightarrow C)$ are the free occurrences of variables in $B$ and $C$. Finally, the free occurrences of variables in a quantified formula $\forall xB$ are the variables other than $x$ that are free in $B$. We call $B$ the scope of the initial occurrence of the quantifier $\forall x$ in $\forall xB$. If an occurrence of a variable is not free in a formula $A$, then it is bound; all occurrences of $x$ in $B$ are bound in the quantified formula $\forall xB$. In fact, we will often write that they lie within the scope of the initial quantifier.

A formula $A$ is *closed* if, and only if, all of its variables are bound. Otherwise, $A$ is *open*. A variable $y$ is *free for* $x$ if, and only if, no free occurrences of $x$ lies within the scope of a quantification on $y$, $\forall y$. We write $A(y/x)$ for the formula that results from $A$ when every free occurrence of $x$ in $A$ is replaced by an occurrence of the variable $y$. A sentence is a closed formula of the language.

#### 1.1.2 Axioms for Pure Quantificational Logic

Frege’s *Begriffsschrift* develops a formal system, which includes axioms for quantification over individual objects and concepts. For Frege, objects are the appropriate values for singular variables, and a concept is what is referred to by a predicate. Notice that despite Frege’s use of the term, concepts, for him, are nothing like mental constructs, but rather objective constituents of the world. In particular, concepts are functions, which map objects into truth values. Since a predicate like “is extended” is true of some objects and false of others, Frege takes the concept *being extended* to assign truth to an object if, and only if, it is extended.

Frege’s system is an axiomatization of what has come to be known as second-order logic, which is an important extension of classical quantificational logic. Hilbert & Ackermann (1928) contains the first axiomatic treatment of quantificational logic as a subject of its own, which they called “the narrower functional calculus”. In what follows, we look at what is now a common axiomatization of pure quantificational logic. This axiom system adopts all tautologies of propositional logic as axioms and *modus ponens* as a rule of inference, and it supplements them with two more axiom schemata and a rule of universal generalization. The first two axiom schemata are:

- ($\forall 1$) $\forall xA \rightarrow A(y/x)$, *provided $y$ is free for $x$ in $A$*.
- ($\forall 2$) $\forall x(A \rightarrow B) \rightarrow (A \rightarrow \forall xB)$, *provided $x$ does not occur free in $A$*.

The first axiom, ($\forall 1$), is commonly known as the axiom of *universal instantiation*. To complete the axiomatization, we need to add a rule of *universal generalization*:

- ($\forall 3$) from $A$, infer $\forall xA$.

Since $\exists xA$ abbreviates $\lnot \forall x \lnot A$, we have a principle of *existential generalization*:

- $A(y/x) \rightarrow \exists xA$, *provided $y$ is free for $x$ in $A$*.

This principle is not without consequence. Since $Px \rightarrow Px$ is a tautology, the combination with *modus ponens* and existential generalization yields $\exists x(Px \rightarrow Px)$ as a theorem. For another example, consider the theorem $\forall xPx \rightarrow \exists xPx$, which is similarly derivable from the axioms by combining universal instantiation and existential generalization. Some have found these consequences objectionable on the grounds that the existence of an object should not be derivable from logic alone.

#### 1.1.3 Interpretations for Pure Quantificational Logic

The interpretation of the language of pure quantificational logic requires one to specify both a domain for the variables to range over and an extension for each non-logical predicate of the language. Alfred Tarski developed what is now known as a model theory for a wide range of formal languages. We recall some definitions from the entry on model theory. A model for the language of pure quantificational logic is an ordered pair, $\langle D, I\rangle$, where $D$ is a non-empty set, and $I$ is an interpretation function, which maps each $n$-place predicate of the language into a set of ordered $n$-tuples of objects in the set $D$. This set provides the domain of discourse for the quantifier, and $I$ provides each predicate of the language with an extension: one-place predicates are mapped into subsets of $D$, two-place predicates are mapped into sets of ordered pairs of members of $D$, and more generally, $n$-place predicates are mapped into sets of $n$-tuples of members of $D$.

Truth in a model is then defined in terms of satisfaction. A variable assignment $s$ for the model $\langle D, I\rangle$ is a function from the set of variables of the language into the domain $D$. A formula $A$ is satisfied in a model $\langle D, I\rangle$ by an assignment $s$ of objects to variables. If $s$ is a variable assignment for $\langle D, I\rangle$, we write $s[x/d]$ to specify a variable assignment, which is just like $s$ except perhaps for assigning $d$ in $D$ to the variable $x$.

We define a formula to be *satisfied* in a model $\langle D, I \rangle$ by an assignment $s$ recursively as follows. An atomic formula $P^{n}_{i} x_{1}, \ldots , x_{n}$ is satisfied in $\langle D, I\rangle$ by $s$ if, and only if, $\langle s(x_{1}), \ldots, s(x_{n})\rangle \in I(P^{n}_{i})$, which means that the $n$-tuple of objects $s$ assigns to the variables that occur in the formula is in the interpretation of the predicate $P^{n}_{i}$ under $I$. A negation $\lnot B$ is satisfied in $\langle D, I\rangle$ by $s$ if, and only if, $B$ is not satisfied in $\langle D, I\rangle$ by $s$. A conditional $(B \rightarrow C)$ is satisfied in $\langle D, I\rangle$ by $s$ if, and only if, $B$ is not satisfied or $C$ is satisfied in $\langle D, I\rangle$ by $s$. Finally, $\forall xB$ is satisfied in $\langle D, I\rangle$ by $s$ if, and only if, $B$ is satisfied in $\langle D, I\rangle$ by all assignments of the form $s[x/d]$, where $d$ is a member of the domain $D$.

A formula $A$ is *true in a model* $\langle D, I\rangle$ if, and only if, $A$ is satisfied in $\langle D, I\rangle$ under all assignments for the model. A formula $A$ is *valid* if, and only if, $A$ is true in all models.

#### 1.1.4 Metatheory for Pure Quantificational Logic

The Tarskian model theory for pure quantificational logic gives us exactly what we want. Since the axioms of pure quantificational logic are valid and the rules of inference preserve validity, all theorems of pure quantificational logic are valid. (Soundness).[^note-3] One may in addition, prove that all valid formulas are, in fact, derivable from the axioms of pure quantificational logic. (Completeness). The entry on classical logic outlines a proof.

Call a set of formulas *Γ* *satisfiable* if, and only if, there is a model $\langle D, I\rangle$ and a variable assignment $s$, which satisfies each formula $A$ in *Γ* in the model. A set *Γ* of formulas is satisfiable if, and only if, every *finite* subset of *Γ* is satisfiable. (Compactness). This is a simple corollary of Completeness.

A simple version of the Löwenheim-Skolem theorem states that if a set of formulas *Γ* has an infinite model, then it has a denumerable model, where a *denumerable* model is one whose domain is no larger than the set of natural numbers. There is a generalized form as well. If we let the cardinality *κ* of the non-logical vocabulary be greater than $\aleph_0$, which is the cardinality of the set of natural numbers, then if *Γ* has an infinite model, then it has a model of cardinality *κ*.

Model-theoretic interpretations are sets: a model is an ordered pair of a non-empty set and an interpretation function. But since modern set theory proves that there is no universal set, no model can ever interpret the quantifiers by means of a universal domain of discourse. It may seem, then, that there are interpretations of the language of pure quantificational logic to which no model corresponds. And this raises the question of whether truth in all models may fall short of truth under all interpretations of the language.

Fortunately, there is an elegant argument due to Georg Kreisel (1967)[^kreisel-1967], which tells us that we can safely restrict attention to models for the specification of the set of validities of pure quantificational logic: a formula $A$ of the language of quantificational logic is true under every interpretation of the language if, and only if, it is true in every model. The argument is a simple application of Completeness. If $A$ is true under every interpretation, whether it is a model or not, then $A$ will be true in every model. The challenge, however, is to argue for the converse. But if $A$ is true in every model, then, by Completeness, $A$ is a theorem of pure quantificational logic. And since every theorem is presumably true under every interpretation, not just model-theoretic ones, it follows that $A$ is true under every interpretation. Thus Kreisel’s argument suggests we can make do with models for the purpose of characterizing validity in pure quantificational logic.[^note-4]

### 1.2 Classical Quantificational Logic with Identity

Classical quantificational logic allows for singular terms other than variables. There are, first, individual constants, and, second, singular terms, which result from the combination of a function symbol with an appropriate number of singular terms. In addition to this, classical quantificational logic with identity makes provision for a special identity predicate.

The vocabulary of the classical theory of quantification and identity extends the vocabulary of pure quantificational logic with a set of individual constants with or without subscripts, $a, b, c, a_1$, …, and a set of function symbols of various kinds: one-place function symbols, $f^{1}, g^{1}, f^{1}_{1}$, …, two-place function symbols, $f^{2}, g^{2}, g^{2}_{1}$, etc.[^note-5] In addition to this, we may add a special two-place predicate, $=$, for identity.

Before we modify the definition of *formula* for the expanded language, we may give a recursive definition of a *term* of the language of the classical theory of quantification and identity. An expression $t$ is a term if, and only if, (i) $t$ is an individual variable, or (ii) $t$ is an individual constant, or (iii) $t$ is an expression of the form $f^{n}_{i}t_{1}, \ldots, t_{n}$, where $f^{n}_{i}$ an $n$-place function symbol and $t_1$, …, $t_n$ are themselves terms. Given the definition of term, we can reformulate the definition of *atomic formula* for the expanded language to consist of all and only expressions $A$ of the form $P^n_i t_1, \ldots, t_n$, where $P^n_i$ is an $n$-place predicate and $t_1$, …, $t_n$ are each terms or $t_i = t_j$ in which $t_i$ and $t_j$ are terms. At this point, we may adapt the usual recursive definition of *formula* for the expanded language.

The axioms of classical quantificational logic with identity include axioms for quantification and axioms for identity. The axioms for quantification include a suitably modified variant of $(\forall 1)$ in addition to $(\forall 2)$ and $(\forall 3)$. The minimal adjustment in $(\forall 1)$ is meant to accommodate the presence of function symbols and individual constants. We call a term $t$ *free for* a variable $x$ if, and only if, no free occurrence of $x$ lies within the scope of a quantifier $\forall y$ or $\exists y$, where $y$ is a variable which occurs in $t$. The axiom of universal instantiation, $(\forall 1)$, now reads:

- $\forall xA \rightarrow A(t/x)$, *provided $t$ is free for $x$ in $A$*.

The other set of axioms concerns identity. In particular, we will supplement the axioms for quantification with an axiom, (I1), and an axiom schema, (I2), designed to govern the identity predicate:

- (I1) $t = t$
- (I2) $t_1 = t_2 \rightarrow (A(t_1/x) \rightarrow A(t_2/x))$ *provided $t_1$ and $t_2$ are free for $x$ in $A$*

The first axiom is sometimes known as Reflexivity, and the second is known as the Indiscernibility of Identicals. When combined, they enable one to derive the symmetry and transitivity of identity as immediate consequences.[^note-6]

We need only make minimal adjustments in the model theory in order to accommodate the expanded vocabulary of the classical theory of quantification and identity. A model $\langle D, I \rangle$ will still consist of a non-empty domain, $D$, and an interpretation function, $I$. One difference, however, is that we now take $I$, in addition, to assign a member of the domain $D$ to each individual constant and to assign an $n$-place function from the set of ordered $n$-tuples of members of $D$, $D^{n}$, into $D$ to each function symbol $f^{n}_{i}$.

We now define satisfaction in terms of *denotation*. Given a model $\langle D, I\rangle$ and an assignment $s$ for the model, we say that a term $t$ *denotes* a member $d$ of the domain under assignment $s$, in symbols $Den_{s}(t) = d$, if, and only if, (i) $t$ is a variable $x_i$ and $s(x_i) = d$, or (ii) $t$ is an individual constant $c$ and $I(c) = d$, or (iii) $t$ is of the form $f^{n}_{i}t_1 , \ldots, t_n$ and $d = I(f^{n}_{i})(Den_{s}(t_1), \ldots, Den_{s}(t_n))$.

The definition of satisfaction in a model $\langle D, I\rangle$ by an assignment $s$ proceeds much like before, except for the obvious clauses for atomic formulas of the form $P^n_i t_1, \ldots, t_n$ and $t_i = t_j$: $P^n_i t_1, \ldots, t_n$ is satisfied by $s$ in $\langle D, I\rangle$ if and only if $\langle Den_{s}(t_1), \ldots, Den_{s}(t_n) \rangle \in I(P^n_i)$. And $t_i = t_j$ is satisfied by $s$ in $\langle D, I\rangle$ if and only if the denotation of $t_i$ under $s$ is identical to the denotation of $t_j$ under $s$.

The definitions of *truth in a model* and *validity* carry over from pure quantificational logic.

We have Soundness and Completeness theorems for classical quantificational logic with identity as well as Compactness and Löwenheim-Skolem theorems. The entry on first-order model theory offers an in-depth examination of these and other meta-theoretic results for classical quantificational logic with identity.

## 2. Departures from Classical Quantificational Logic

In what follows, we look at three rival accounts of quantification in modern logic. They are departures from classical quantification logic because they reject some of classical axioms of quantification or because they question some aspect of the Tarskian model theory we have used to interpret the language of classical quantification logic.

### 2.1 Inclusive and Free Quantificational Logic

In pure quantificational logic, one may, for example, derive the conditional $\forall xPx \rightarrow \exists xPx$ as an immediate consequence of the axioms. But the derivability of this sentence—and others like $\exists x (Px \rightarrow Px)$—may give one pause. To the extent to which logic should remain neutral in ontological matters, the axioms of pure quantificational logic should not by themselves be able to prove that there is something rather than nothing. From a model-theoretic perspective, the exclusion of the empty domain as an eligible domain for a model may likewise seem artificial. Since the validity of formulas like $\forall xPx \rightarrow \exists xPx$ or $\exists x(Px \rightarrow Px)$ is largely a byproduct of what may seem an *ad hoc* stipulation, one may be motivated to expand the range of models in order to allow for a model with an empty domain of discourse. Quine (1954)[^quine-1954] used the label “inclusive” to refer to alternatives to quantificational logic that make allowance for such a model.

According to Quine (1954)[^quine-1954], an inclusive quantificational logic should evaluate every universally quantified formula of the form $\forall x A$ to be vacuously true in a model $\langle D, I\rangle$ in which $D$ is empty, and it should evaluate every existentially quantified formula of the form $\exists x A$ to be false in such a model. $\forall xPx \rightarrow \exists xPx$ and $\exists x(Px \rightarrow Px)$ are therefore not valid on the expanded model theory. However, it is quite a delicate matter to provide a compositional amendment of the Tarskian definition of truth in a model $\langle D, I \rangle$ under an assignment $s$ that delivers Quine’s verdicts.[^note-7]

An axiomatization of inclusive quantificational logic should weaken the axiom of universal instantiation in order to prevent the derivation of theorems such as $(\forall xPx \rightarrow \exists x Px)$ or $\exists x(Px \rightarrow Px)$. One option independently explored by Kripke (1963)[^kripke-1963] and Lambert (1963)[^lambert-1963] is to replace ($\forall 1$) with a closed axiom schema:

- ($\forall 1^{-}$) $\forall y(\forall xA \rightarrow A(y/x))$, *provided $y$ is free for $x$ in $A$*.

In the absence of identity, by itself, this change results in an inadequate axiomatization of pure quantificational logic, one which cannot yield every instance of a permutation principle discussed by Fine (1983)[^fine-1983]:

- $\forall x\forall y A \rightarrow \forall y\forall xA$.

The permutation principle, however, becomes redundant in the presence of axioms for identity.

The axiomatization of classical quantification logic with identity that emerges is discussed by Lambert (1963)[^lambert-1963] with a different motivation in mind. While classical quantificational logic assumes singular terms denote members of the domain of quantification, Lambert wanted to allow for systems that remain “free” from such assumptions. Free quantificational logic makes room for empty singular terms, which fail to denote any member of the domain. That means that free logic need not prove every formula of the form:

- $\exists x(x = t)$.

These are all theorems of quantificational logic with identity. Given Reflexivity (I1), the classical axiom of universal instantiation ($\forall 1$) is all that is required for the proof of these theorems. So, free logicians have another incentive for the retreat from ($\forall 1$) to ($\forall 1^{-}$). It is not uncommon to use an existence predicate in order to distinguish terms that denote members of the domain from those that do not. In general, $E!t$ is read to be true if $t$ denotes a member of the domain, and false if it does not. This existence predicate is sometimes taken as primitive and sometimes defined by the formula $\exists x(x =t)$. That suggests a different weakening of ($\forall 1$):

- $ \forall xA \rightarrow (E!t \to A(t/x)) $, *provided $y$ is free for $x$ in $A$*.

What is less obvious is how to modify the model theory for the language in order to accommodate empty terms. One important choice point is the evaluation of atomic formulas in a model of free quantificational logic with identity. One approach is to declare as false an atomic formula of the form $P^n_i t_1, \dots, t_n$ or $t_i = t_j$ if any of the terms involve fail to denote anything in the domain. That would result in a *negative* model theory for the language. On the other hand, we could make allowance for true atomic formulas even if some of the relevant terms denote nothing in the domain, e.g., we might declare $t = t$ true even if nothing in the domain of quantification is a denotation for the term in question. That would result in a *positive* model theory for the language. Finally, we could declare atomic formulas not of the form $E!t$ to be neither true nor false, which would result in a *neutral* model theory for the language. The entry on free logic explores all these options in detail.

### 2.2 Intuitionistic Quantificational Logic

Intuitionistic propositional logic is weaker than classical propositional logic. All intuitionistically valid formulas are classically valid, but classically valid formulas like $(A \vee \lnot A)$ and $(\lnot \lnot A \rightarrow A)$ are not intuitionistically valid.[^note-8] The exclusion of these formulas from the range of intuitionistic theorems can be motivated by the usual Brouwer-Heyting-Kolmogorov interpretation of the connectives:

- A proof of $\lnot A$ consists of a proof that there cannot be a proof of $A$.
- A proof of $(A \wedge B)$ consists of a proof of $A$ and a proof of $B$.
- A proof of $(A \vee B)$ consists of a proof of $A$ or a proof of $B$.
- A proof of $(A \rightarrow B)$ consists of a construction, which turns a proof of $A$ into a proof of $B$.

Despite the differences in interpretation, there is an important connection between intuitionistic and classical propositional logic. For we know that a formula $A$ is a theorem of classical propositional logic if, and only if, $\neg \neg A$ is a theorem of intuitionistic propositional logic. Thus while $(A \vee \neg A)$ is obviously not a theorem of intuitionistic propositional logic, $\neg \neg (A \vee \neg A)$ is in fact intuitionistically provable. This fact is at the core of a familiar translation from classical into intuitionistic propositional logic due to Kurt Gödel and Gerhard Gentzen. For a summary of this and related facts, the reader may consult the entry on intuitionistic logic.

Now, intuitionistic quantificational logic may be motivated by the Brouwer-Heyting-Kolmogorov interpretation of the quantifiers:

- A proof of $\exists xA$ is given by a specification of some $d$ and a proof that $A$ obtains for $d$.
- A proof of $\forall xA$ is given by a construction, which given an object $d$, produces a proof that $A$ obtains for $d$.

The intuitionistic interpretation doesn’t sanction the classical equivalence between $\exists x A$ and $\neg \forall x \neg A$. Indeed, the two quantifiers must remain part of the primitive vocabulary of intuitionistic quantificational logic.

#### 2.2.1 Axioms for Intuitionistic Quantificational Logic

The intuitionistic axioms of quantification include counterparts of the classical axioms of universal instantiation and existential generalization:

- ($\forall^{I}1$) $\forall xA \rightarrow A(y/x)$ *provided $y$ is free for $x$ in $A$*.
- ($\exists^{I}1$) $A(y/x) \rightarrow \exists x A$ *provided $y$ is free for $x$ in $A$*.

In addition to this, we have two more principles:

- ($\forall^{I}2$) $\forall x(A \rightarrow B) \rightarrow (A \rightarrow \forall xB)$, *provided $x$ does not occur freely in $A$*.
- ($\exists^{I}2$) $\forall x(A \rightarrow B) \rightarrow (\exists xA \rightarrow B)$, *provided $x$ does not occur freely in $B$*.

We have a rule of universal generalization:

- ($\forall^{I}3$) from $A$, infer $\forall xA$.

It is not generally true that a formula $A$ is a theorem of pure quantificational logic if, and only if, $\neg \neg A$ is a theorem of intuitionistic quantificational logic, but there is a more sophisticated double-negation interpretation of theorems of pure quantificational logic. In particular, we have that a formula $A$ is a theorem of quantificational logic if, and only if, it is a theorem of intuitionistic quantificational logic supplemented with a double negation schema:

- (DNS) $\forall x \neg \neg A \rightarrow \neg \neg \forall xA$

Much like in the propositional case, one may exploit this fact to give a more sophisticated translation from pure quantificational logic into intuitionistic quantificational logic. Details are given in Moschovakis (2010)[^moschovakis-2010].

In intuitionistic quantificational logic, we cannot move from $\neg \forall x \neg A$ to $\exists x A$, but we still have this:

- $\exists x A \rightarrow \neg \forall x \neg A$

Moreover, since $A$ intuitionistically entails $\lnot \lnot A$, we can infer:

- $\forall x A \rightarrow \lnot \lnot \forall x A$

In intuitionistic quantificational logic, $\forall x \lnot \lnot A$ is strictly weaker than $\lnot \lnot \forall x A$, since we have:

- $\lnot \lnot \forall x A \rightarrow \forall x \lnot \lnot A$.

#### 2.2.2 Kripke Models for Intuitionistic Quantificational Logic

A variety of interpretations have been advanced for intuitionistic quantificational logic, but the model theory developed by Kripke (1965)[^kripke-1965] is perhaps the most similar to the model theory of classical quantificational logic. A Kripke model $\mathcal{K}$ is based on a frame $\langle S, \preceq \rangle$, which consists of a set of *stages* partially ordered by an accessibility relation $\preceq$. A Kripke model assigns an inhabited domain, $D_{s}$, to each stage $s \in S$, subject to the constraint that $D_s \subseteq D_{s'}$ when $s \preceq s'$. We may assume that suitable names for the members of each $D_s$ have been adjoined to the language. Finally, for $n>0$, a Kripke model assigns a set of $n$-tuples of members of $D_s$ for each $n$-place predicate $P^{n}$ at each stage $s$ in $S$, subject to the constraint that if $s \preceq s'$ and $P^n$ is true of $\langle d_1, \ldots, d_n \rangle$ at $s$, then $P^{n}$ is still true of $\langle d_1, \ldots, d_n \rangle$ at $s'$.

The entry on intuitionistic logic provides a more formal and complete statement of Kripke’s model theory for intuitionistic quantificational logic and states Soundness and Completeness Theorems for it. Very roughly, a negation $\neg A$ is true at a stage $s$ if, and only if, $A$ is not true at any stage $s'$ such that $s \preceq s'$; an existentially quantified formula $\exists x A$ is true at a stage $s$ if, and only if, $A$ is true of some $d$ in $D_s$ at $s$; and a formula $\forall xA$ is true at a stage $s$ if, and only if, $A$ is true of every $d$ in $D_{s'}$ for every $s'$ such that $s \preceq s'$.

For a taste of what Kripke models can do, consider:

1. $\neg \forall x \neg A \rightarrow \exists x A$
2. $\lnot \lnot \forall x A \rightarrow \forall x A$
3. $\forall x \lnot \lnot A \rightarrow \lnot \lnot \forall x A$

Let $\mathcal{K}$ be a Kripke model based on a frame in which we have two stages $s_0 \preceq s_1$. Assume $\{d \}$ is the domain associated to each stage by the model, and let a monadic predicate $P$ be true of $d$ at $s_1$ but not at $s_0$. We may verify that $\neg \forall x \neg Px$ is true at $s_0$, even though $\exists x Px$ is not true at $s_0$. So, (i) is not intuitionistically valid. One may likewise verify that $\lnot \lnot \forall x Px$ is true at $s_0$, even though $\forall x Px$ is not true at $s_0$. It follows that (ii) is not intuitionistically valid either.

For (iii), consider, for example, a Kripke model based on a frame in which we have an infinite number of stages $s_0 \preceq s_1 \preceq \ldots \preceq s_n \preceq \ldots$. We may assume that $D_{s_{n}} = \{ d_0 , \ldots, d_n \}$ and that a monadic predicate $P$ is true at $s_n$ of every $d_m$ in the domain except for $d_n$. It turns out that $\forall x \lnot \lnot Px$ is true at $s_0$ even though $\lnot \lnot \forall x Px$ is not true at $s_0$. Therefore, $\forall x \lnot \lnot A \rightarrow \lnot \lnot \forall x A$ is not intuitionistically valid either. These and similar examples are discussed in Burgess 2009.

### 2.3 Substitutional Quantification

The model-theoretic interpretation of the language of quantificational logic relied on the Tarskian definition of satisfaction in a model by an assignment of values to the variables. But the assignment of an object to a variable is never dependent on the availability of a term, $t$, for the object in the language for which one defines truth in a model. Indeed, an existentially quantified formula $\exists x A$ may well be true in a model even if no atomic formula of the form $A(t/y)$ is true in the model.

Substitutional quantifiers $\Pi \alpha \ A$ and $\Sigma \alpha \ A$ are interpreted differently. An interpretation associates with them not a domain of quantification, but rather a substitution class, $C$, of linguistic expressions of an appropriate syntactic category in the initial language. The truth conditions for substitutionally quantified sentences of the form $\Sigma \alpha \ A$ and $\Pi \alpha \ A$ may be given in terms of the truth conditions of suitable substitution instances of $A(\epsilon / \alpha)$ in which each occurrence of the substitutional variable *α* has been replaced with a linguistic expression, *ε*, of the appropriate syntactic category in the substitution class for the quantifier:

- A sentence of the form $\Sigma \alpha \ A$ is true relative to a substitution class $C$ if, and only if, some substitution of the variable *α* for an expression *ε* in the substitution class $C$ for the quantifier, $A(\epsilon / \alpha)$, is true.
- A sentence of the form $\Pi \alpha \ A$ is true relative to a substitution class $C$ if, and only if, every substitution of the variable *α* for an expression *ε* in the substitution class $C$ for the quantifier, $A(\epsilon / \alpha)$, is true.

This characterization of substitutional quantification allows for substitutional variables of different syntactic categories, whether singular terms, predicates or sentences. Indeed, substitutional quantification is often used to mimic quantification into predicate and sentence position of the kinds discussed later in this entry.

Early work on substitutional quantification was developed in Marcus (1961)[^marcus-1961] but it soon became the subject of intense debate in the next two decades as philosophers made use of substitutional quantification in ontology and the philosophy of language and mathematics. Belnap and Dunn (1968), Parsons (1971)[^parsons-1971], Grover (1972)[^grover-1972], and Kripke (1976)[^kripke-1976] are some of the relevant papers in the debate. For a sense of some of the purported applications of substitutional quantification, the reader may consult the essays collected in Gottlieb 1981. For further discussion, see Hand (2007)[^hand-2007].

#### 2.3.1 A simple example

Let us momentarily focus on singular terms. To keep matters simple, consider an impoverished fragment of the language of arithmetic with one constant, $0$, read: “zero” and one functional symbol, $S$, read: “the successor of”. The domain of the intended interpretation consists of a set of natural numbers, which are named by singular terms of the form $0,$ $SS0,$ $SSS0,$ …, etc. If we now associate the class of all such terms to the substitutional quantifiers $\Sigma \alpha$ and $\Pi \alpha$, then a sentence like $\Sigma \alpha \ \alpha = \alpha$ is evaluated as true in virtue of the truth of formulas like $0 = 0$, whereas $\Pi \alpha \ \alpha < \alpha$ is evaluated as false in virtue of falsity of formulas like $0 < 0$. In general, a sentence of the form $\Sigma \alpha \ A$ exhibits the same truth conditions as an infinitary disjunction of the form: $$A(0/\alpha) \vee A(S0/\alpha) \vee \ldots\vee A(SS \overbrace{\ldots}^n S0/\alpha) \vee \ldots$$ whereas a sentence of the form $\Pi \alpha \ A$ exhibits the same truth conditions as an infinitary conjunction: $$A(0/\alpha) \wedge A(S0/\alpha) \wedge \ldots\wedge A(SS \overbrace{\ldots}^n S0/\alpha) \wedge \ldots$$ The case of arithmetic is optimal because we have a name for each member of the intended domain. This means that in general, a quantified sentence of the form $\exists x A$ will be true if, and only if its substitutional counterpart $\Sigma \alpha \ A$ is likewise true. But in this respect, however, the language of arithmetic is the exception and not the rule. In real analysis, for example, there are too many objects in the domain to have a name in a countable language. In such a situation, we must confront the risk that a sentence of the form $\exists x A$ may be true even if $\Sigma \alpha \ A$ remains false in virtue of the lack of a true substitution instance of the form $A(t/ \alpha)$. This may happen, for example, if the objects that satisfy the open formula $A$ are not denoted by any singular term in the language.

Call the initial language “the object language”. And call the language in which we explain the truth conditions of sentences of the initial language “the metalanguage”. In the metalanguage, we have explained the truth condition for $\Sigma \alpha \ A$ in terms of what looks like objectual quantification over linguistic expressions. To acknowledge this is of course not to claim that the intended interpretation of substitutional quantification is one on which it is merely objectual quantification over linguistic expressions. But just what the intended interpretation of the substitutional quantifier might be has been the subject of intense controversy. Indeed, van Inwagen (1981)[^inwagen-1981] and Fine (1989)[^fine-1989], for example, have each argued that there is no separate intended interpretation we can understand independently from our grasp of objectual quantification over linguistic expressions of the relevant sort.

#### 2.3.2 Kripke on Substitutional Quantification

Whatever the philosophical import of substitutional quantification, Kripke (1976)[^kripke-1976] makes plain that there is no technical obstacle to introducing substitutional quantifiers into a given language. In what is perhaps the canonical treatment of substitutional quantification, he explained how to extend an interpreted language $\mathcal{L}$ into a substitutional language $\mathcal{L}^{\Sigma}$ equipped with substitutional quantification over a class of expressions in $\mathcal{L}$. One first expands the vocabulary of $\mathcal{L}$ with an infinite stock of variables $\alpha_1$, $\alpha_2$, … and a substitutional quantifier $\Sigma$. (Kripke defines *Π* as the dual of $\Sigma$, where $\Pi \alpha \ A$ abbreviates: $\lnot \Sigma \alpha \lnot \ A$.)

An *atomic preformula* is an expression that results from a sentence of $\mathcal{L}$ when zero or more terms are replaced by a substitutional variable. A *form* is an atomic preformula, where the replacement of its substitutional variables with terms yields back a sentence. We can now define a formula of $\mathcal{L}^{\Sigma}$ recursively. $A$ is a formula of $\mathcal{L}^{\Sigma}$ if and only if either (i) $A$ is a *form* of $\mathcal{L}^{\Sigma}$ or (ii) $A$ is $\lnot B$, where $B$ is a formula of $\mathcal{L}^{\Sigma}$ or (iii) $A$ is $(B \rightarrow C)$, where $B$ and $C$ are each formulas of $\mathcal{L}^{\Sigma}$ or (iv) $A$ is $\Sigma \alpha \ B$, where $B$ is a formula of $\mathcal{L}^{\Sigma}$. A sentence of $\mathcal{L}^{\Sigma}$ is a formula without free substitutional variables.

Kripke defines truth for sentences of $\mathcal{L}^{\Sigma}$ recursively in terms of truth in $\mathcal{L}$. If $A$ is an atomic sentence of $\mathcal{L}^{\Sigma}$—which may well be a complex sentence of $\mathcal{L}$, then $A$ is true in $\mathcal{L}^{\Sigma}$ if, and only if, $A$ is true in $\mathcal{L}$. If $A$ is a sentence of the form $\lnot B$, then $A$ is true in $\mathcal{L}^{\Sigma}$ if, and only if, $B$ is not true in $\mathcal{L}^{\Sigma}$. If $A$ is of the form $(B \rightarrow C)$, then $A$ is true in $\mathcal{L}^{\Sigma}$ if, and only if, $B$ is not true or $C$ is true in $\mathcal{L}^{\Sigma}$. Finally, and more crucially, if $A$ is of the form $\Sigma \alpha \ B$, then $A$ is true in $\mathcal{L}^{\Sigma}$ if and only if $B(\epsilon/\alpha)$ is true in $\mathcal{L}^{\Sigma}$ for some *ε* in the substitution class $C$ associated with $\Sigma$.

Kripke then defines a sentence $A$ of the language of pure substitutional quantificational logic to be valid if, and only if $A$ comes out true no matter what base language $\mathcal{L}$ and non-empty class of terms $\mathcal{C}$ we take as input for the substitutional expansion and what predicates of $\mathcal{L}$ we substitute for the predicates of $A$. In particular, Kripke notes that when the quantifiers of a valid sentence of pure quantificational logic are suitably rewritten as substitutional quantifiers, we obtain a valid sentence in the language of pure substitutional quantificational logic.

## 3. Extensions of Classical Quantificational Logic

Each departure from classical quantificational logic we have considered originated from an objection to either axioms of pure quantificational logic or the Tarskian definition of satisfaction in a model by an assignment of objects to the variables of the language. We now take both for granted and look at proposed extensions of classical quantificational logic with new styles of quantification. Each extension will generally require us to add new axioms for the new styles of quantification and to expand the Tarskian definition of truth in a model in terms of satisfaction.

### 3.1 Generalized Quantifiers

Frege originally conceived of the quantifier $\forall$ as a monadic predicate that is true of a first-level concept $F$ under which only objects fall if, and only if, all objects fall under $F$; likewise, Frege assimilated $\exists$ to a monadic predicate that is true of a first-level concept if, and only if, at least one object falls under $F$. In modern terms, we may say that the truth conditions of $\forall x A$ are given in terms of a certain condition on the extension of the formula $A$. Given a model $\langle D, I\rangle$ and a formula $A(x)$ with a single free variable $x$, it will be convenient to use $A(x)[d]$ to abbreviate: $A$ is satisfied in $\langle D, I\rangle$ by variable assignments on which $d$ is the value assigned to the variable $x$. The extension of a formula $A(x)$ with a single free variable $x$ in a model $\langle D, I\rangle$ is just $\{ d \in D: A(x)[d] \}$, which we may abbreviate $I(A)$.

- $\forall x A$ is true in $\langle D, I\rangle$ if, and only if, $D \subseteq I(A)$.

The contemporary study of generalized quantifiers begins with Mostowski (1957)[^mostowski-1957] and Lindström (1966)[^lindström-1966] (the entry on generalized quantifiers provides a survey of recent developments and applications in logic and natural language). Lindström and Mowstoski began with a generalization of Frege’s conception of a quantifier in at least two dimensions. First, they considered additional unary quantifiers $Q(A)$, which behave syntactically like $\forall$ and $\exists$ but set a different condition on the extension of $A$. Second, they considered binary quantifiers $Q(A, B)$, which set a given condition based on a relation between the extensions of $A$ and $B$.

#### 3.1.1 Cardinality Quantifiers

Cardinality quantifiers provide a simple example of the first sort of generalization. If we write $card(S)$ to denote the cardinality of a given set $S$, we may introduce unary quantifiers of the form $Q(A)$, which set a cardinality condition on the extension of a formula $A$:

- $\exists_{\geq n} x A$ is true in $\langle D, I\rangle$ if, and only if, $card(I(A)) \geq n$
- $\exists !_{n} x A$ is true in $\langle D, I\rangle$ if, and only if, $card(I(A)) = n$

$\exists_{\geq n}$ is read: “at least $n$ objects” and $\exists !_{n}$ is read: “exactly $n$ objects.” Both quantifiers are definable in terms of a standard quantifier against the background of classical quantificational logic.

Other cardinality quantifiers, however, do increase the expressive power of classical quantifical logic. We may, for example, introduce cardinality quantifiers of the form $Q(A)$, which require the extension of $A$ to have an infinite cardinality:

- $Q_0 x \ A$ is true in $\langle D, I\rangle$ if, and only if, $card(I(A)) \geq \aleph_0$
- $Q_1 x \ A$ is true in $\langle D, I\rangle$ if, and only if, $card(I(A)) \geq \aleph_1$

$\aleph_0$ is the cardinality of the set of natural numbers, and $\aleph_1$ is the next transfinite cardinal.[^note-9] When we supplement classical quantificational logic with $Q_0$, read: “at least $\aleph_0$ objects”, we must relinquish Compactness even if we can still retain the Löwenheim-Skolem theorem. The opposite is the case, however, when we supplement classical quantificational logic with $Q_1$, read: “at least $\aleph_1$ objects” instead.

Two more cardinality quantifiers that have been studied in the literature are the Chang quantifier and the Rescher quantifier:

- $Cx \ A$ is true in $\langle D, I\rangle$ if, and only if, $card(I(A)) = card(D)$
- $R x \ A$ is true in $\langle D, I\rangle$ if, and only if, $card(I(A)) > card(D - I(A))$

The Chang quantifier collapses into $\forall$ only in the finite case; if $D$ is infinite, then the extension of a formula $A$, $I(A)$, may match the cardinality of the domain, $D$, even if the two sets are different and $I(A) \neq D$.

#### 3.1.2 Generalized Binary Quantifiers

The second dimension of generalization concerns the number of arguments we let quantifiers take. We can, for example, introduce binary quantifiers, $Q(A, B)$, whose truth condition is given in terms of a binary relation between the extension of the formula $A$ and the extension of the formula $B$ in a model.

- $All(A, B)$ is true in $\langle D, I\rangle$ if, and only if, $I(A) \subseteq I(B)$
- $More(A, B)$ is true in $\langle D, I\rangle$ if, and only if, $card(I(A)) > card(I(B))$
- $Most(A, B)$ is true in $\langle D, I\rangle$ if, and only if, $card(I(A) \cap I(B)) > card(I(A)-I(B))$

As defined above, $Most(A, B)$, for example, is true if and only if more objects are both $A$ and $B$ than there are objects that are $A$ and not $B$.

Of special interest in the philosophy of language is the case of Russellian definite descriptions, which can be subsumed under the category of a binary quantifier:

- $The(A, B)$ is true in $\langle D, I\rangle$ if, and only if, $card(I(A)) = 1$ and $I(A) \subseteq I(B)$

For a systematic discussion of these issues, the reader may consult Peters & Westerståhl (2006).

### 3.2 Many-Sorted Quantification

We generally let quantifiers bind a single type of variable, but we may find it helpful, on occasion, to let them bind additional types of variables in order to quantify over different sorts of values. In arithmetic, for example, we may want to be able to quantify over natural numbers and sets thereof and we may find it convenient to classify the individual variables of the language into at least two categories. We may reserve lowercase variables $x, y, z, x_1$, … to range over natural numbers, and we may use uppercase variables $X, Y, Z, X_1$, … to range over sets of natural numbers. In a many-sorted language with functional symbols and individual constants, each singular term would be assigned a single sort. If we want identity, we need to include an identity predicate for each sort of a variable and insist on each such predicate to be flanked only by singular terms of the appropriate sort. Other predicates may nevertheless take arguments of different sorts; for example, in a two-sorted language in which lowercase variables range over numbers and uppercase variables range over sets of numbers, $x \epsilon X$, for example, can take as arguments variables of different sorts and may be read “$x$ is in $X$”.

To accommodate the new styles of variables in the model theory for many-sorted logic, we may add a domain for each style of variable. A model for a two-sorted language, for example, may consist of an ordered triple $\langle D_1, D_2, I\rangle$ in which $D_1$ and $D_2$ specify the domain of quantification associated to each style of variable, and $I$ is an interpretation function, which assigns appropriate values and extensions to each expression in the non-logical vocabulary. (Since each singular term is assigned a sort, $I$ must be constrained to make sure singular terms of each sort denote objects in the appropriate domain.) The metatheory for many-sorted logic is closely related to the metatheory for classical quantificational logic. One may, for example, prove many-sorted versions of Compactness and the Löwenheim-Skolem Theorem. Details may be found in Enderton 2001.

However, the move to a many-sorted language is largely a matter of convenience. Many-sorted quantification may be analyzed in terms of restricted one-sorted quantification. For each many-sorted language with $n$ styles of variable, we may introduce a one-sorted language, which comes with a one-place predicate, $S_i$, for each sort in the many-sorted language. We may set out to translate each formula of the many-sorted language into a formula of the one-sorted language: we translate each identity in terms of a single identity predicate; a quantification on a variable of sort $i$, $\forall x^i A$, is replaced with a formula of the form $\forall x(S_i x \rightarrow A)$. We may, in addition, turn each model for the many-sorted language $\langle D_1, \ldots, D_n, I \rangle$ into a model for the resulting one-sorted language $\langle \bigcup_{n} D_n, I^\ast \rangle$ in which we take the domain to consist in the union of the domains associated to each original sort. The interpretation function, $I^\ast$ will coincide with $I$ when it comes to predicates and individual constants. However, $I^\ast$ will generally have to extend the interpretation of a functional symbol, $f^n_i$, by $I$, in one way or another. Finally, $I^\ast$ will interpret the identity predicate as usual.

Still, even if there is no real gain in expressive power, one reason to flag the availability of many-sorted quantification is because some of the extensions of classical quantificational logic to be examined below are closely related to certain theories couched in the language of two-sorted logic. In particular, second-order logic and the theory of plural quantification will be each closely related to two first-order two-sorted theories, which lack the expressive resources often attributed to each extension of classical quantificational logic.

### 3.3 Second-Order Quantifiers

Second-order logic is an extension of classical quantificational logic in which we allow for quantification into predicate position. Second-order logic originated with Frege (1879)[^frege-1879], which developed a formal language equipped with predicate variables of the form $X^{n}_{i}$. Predicate variables behave syntactically like $n$-place predicates of the form $P^{n}_{i}$. In second-order logic, a predicate variable $X^{n}_{i}$ followed by $n$ variables $X^{n}x_{1}, \ldots, x_{n}$ counts as an atomic formula. We finally let the quantifiers $\forall$ and $\exists$ bind predicate variables as in $\forall X^{n}\, A$ and $\exists X^{n}\,A$.

#### 3.3.1 Axioms for second-order quantification

The axioms for second-order logic supplement the axioms of classical quantificational logic with distinctive axioms for the second-order quantifiers. Call a predicate variable $Y^n$ *free for* $X^n$ in $A$ if, and only if, no free occurrences of $X^n$ lie within the scope of a quantification on $Y^n$, $\forall Y^n$ or $\exists Y^n$:

- ($\forall^{2}1$) $\forall X^{n}\,A \rightarrow A(U^{n}_{j}/X^{n})$, *provided $U^{n}_{j}$ is free for $X^{n}$ in $A$*.
- ($\forall^{2}2$) $\forall X^{n}(A \rightarrow B) \rightarrow (A \rightarrow \forall X^{n}\,B)$, *provided $X^{n}$ does not occur freely in $A$*.

($\forall^2 1$) is a second-order version of *universal instantiation*. The second-order version of *universal generalization* becomes:

- ($\forall^{2}3$) from $A$, infer $\forall X^{n}\,A$.

Observe that while $\forall X(Xx) \rightarrow Px$ is an instance of ($\forall^2 1$), the formula $\forall X(Xx) \rightarrow (Px \wedge Qx)$ is not an instance of the axiom. But whatever one takes the value of a second-order variable to be, you may think that there should be one under which an object falls if and only if it satisfies the condition stated by the formula $(Px \wedge Qx)$. To make sure, we may rely on an axiom of *second-order comprehension*:

- $\exists X^{n} \forall x_1, \ldots x_n(X^{n}x_1, \ldots, x_n \leftrightarrow A(x_1, \ldots, x_n))$ *provided $X^{n}$ does not occur freely in $A(x_1, \ldots , x_n)$*.

A formula like $\forall X(Xx) \rightarrow (Px \wedge Qx)$ now follows from the combination of second-order universal instantiation and an instance of second-order comprehension: $\exists X\forall x(Xx \leftrightarrow (Px \wedge Qx))$.[^note-10]

#### 3.3.2 Standard Models for Second-Order Logic

To develop a model theory for a second-order language, we may still take a model $\langle D, I\rangle$ to consist of a non-empty domain and an interpretation function. We now let an assignment $s$ for $\langle D, I\rangle$ to be a function that assigns a member of $D$ to each individual variable and a set of $n$-tuples of members of $D$ to each predicate variable $X^n$. We then modify the definition of satisfaction to let a formula of the form $\forall X^n\,B $ be satisfied in $\langle D, I \rangle$ by an assignment $s$ if, and only if, $B$ is satisfied by all assignments of the form $s[X^n/R^n]$, where $R^n$ is a set of $n$-tuples of members of $D_1$. The definitions of truth in a model and validity proceed exactly as in the first-order case.

The entry on second-order and higher-order logic provides more detail and gives some indication of the complexity of the set of valid second-order formulas in the standard model theory for second-order logic. No Completeness, Compactness, or Löwenheim-Skolem theorem is available for second-order logic with standard models. The entry on second-order and higher-order logic provides concrete illustrations of these facts.

#### 3.3.3 Henkin Models for Second-Order Logic

A Henkin model lets a second-order variable $X^n$ range over some subset of the set of $n$-tuples of members of the domain $D$. Thus a Henkin model consists of a domain $D$ of individuals, a domain $D^n_2$ of sets of $n$-tuples of objects in $D$ for each $n \leq 1$, and an interpretation function $I$. To make sure that every instance of second-order comprehension is validated in the model, we require each $D^n_2$ to contain every set of $n$-tuples of members of $D$ that is definable by a formula $A$ of the language.

This is what the entry on second-order and higher-order logic calls general semantics. The metatheory of second-order logic with Henkin models is very much like the metatheory of classical quantificational logic in that it is complete, compact, and subject to a Löwenheim-Skolem theorem. One reason for this is that second-order logic under the Henkin model theory is only a notational variant of a two-sorted first-order theory in which the axioms of quantificational logic are supplemented by suitable axioms of comprehension.

Which model theory is more appropriate for second-order logic? There is a trade-off between the attractive features of the metatheory of second-order logic with Henkin models, on the one hand, and the expressive power of second-order logic with standard models, on the other. Frege’s own interest in second-order quantification had much to do with its ability to express the concept of the *ancestral* of a dyadic relation $R$, which allowed him in turn to define the concept *natural number* in terms of $0$ and *successor*. For details, the reader may consult the entry on Frege’s Theorem and Foundations of Arithmetic. There are, in addition, *categorical* axiomatizations of arithmetic, where a set of sentences is *categorical* if, and only if, all of its models are isomorphic, which means that there is only one model up to isomorphism. Dedekind (1893)[^dedekind-1893] famously proved, for example, that the second-order formulation of the Peano Axioms characterized the structure of the natural number system. There is a similar result for real analysis. For second-order set theory, Zermelo (1930)[^zermelo-1930] observed that given two models of second-order Zermelo-Fraenkel set theory, one is isomorphic to a strongly inaccessible initial segment of the other. The entry on set theory describes the axioms of set theory. Other examples of the expressive resources afforded by second-order quantification with standard models are discussed in Shapiro (1991)[^shapiro-1991]. The adoption of a model theory based on Henkin models requires one to surrender all these applications.

#### 3.3.4 Models and Interpretations

Much like in the case of pure quantificational logic, no model—standard or otherwise—for the language of second-order logic interprets the quantifiers to range over a universal domain of discourse. But if there are interpretations of the language of second-order logic to which no model corresponds, the question arises again of whether truth in all models is tantamount to truth under all interpretations of the language. Unfortunately, in the absence of a Completeness theorem, Kreisel’s argument is not available for second-order logic with standard models.

One may nevertheless argue that a formula is true in all models only if it is true under all interpretations of the language by appeal to a second-order principle of reflection. This reflection principle makes sure that a formula $A$ of the language of second-order set theory is true when the quantifiers are taken to range unrestrictedly over the universal domain if, and only if, $A$ is true when the quantifiers are restricted to some set-sized initial segment of the universe of a certain sort.[^note-11] Shapiro (1987)[^shapiro-1987] discusses both the set-theoretic principle and its role in the justification of the claim that if a sentence is true in every standard model, then it is true under every interpretation of the language. Unfortunately, second-order reflection takes us beyond the scope of second-order Zermelo-Fraenkel set theory and the axiom of choice (ZFC).

To make sense of interpretations over a universal domain, one may conceive of an interpretation as a value of a second-order predicate variable, $I$, which applies to ordered pairs of a certain sort. An interpretation, $I$, applies to ordered pairs of the form $\langle \forall, o \rangle$, when $o$ is in the domain of the interpretation, and $I$ applies to ordered pairs of the form $\langle P^{n}_{i}, \langle a_1, \ldots, a_n\rangle \rangle$, when $P^{n}_{i}$ is taken to apply to the objects in $\langle a_1, \ldots, a_n\rangle$. The usual definition of an assignment is then replaced by one on which an assignment is given by the value of a second-order variable $S$, which applies to an ordered pair of the form $\langle x, o\rangle$, where $o$ is an object, for each first-order variable in the language, and to ordered pairs of the form $\langle X, o\rangle$, where $o$ is an object, for each second-order variable in the language. An assignment $S$ is required to pair each first-order variable with exactly one object, but it is allowed to pair a second-order variable with any objects whatever. In the presence of these definitions, we can generalize Tarski’s definition satisfaction in an interpretation by an assignment, truth, and validity.[^note-12]

#### 3.3.5 How to Understand Second-Order Quantification

The status of second-order quantification remains controversial. The standard model theory for second-order quantification states the truth conditions of a formula of the form $\forall X\,A$ in terms of ordinary quantification over subsets of the domain. This may have inclined some to agree with Quine (1986)[^quine-1986] that second-order quantification is only intelligible as covert first-order quantification over sets. Second-order logic would, on this view, be best conceived as a species of two-sorted first-order set theory. But the model-theoretic interpretation is not the *only*, much less *the* intended interpretation of second-order quantification. Indeed, Boolos (1984)[^boolos-1984] proposed an alternative interpretation of *monadic* second-order logic in terms of an ingenious translation into a fragment of natural language on which second-order quantifiers became plural quantifiers on which more below. There is an even more radical alternative, which is to deny that the interpretation of second-order quantification should be determined by either the model theory for second-order logic or by means of any explicit or tacit translation into some fragment of natural language. Instead, the thought continues, one may have to rely a more direct method and learn what second-order quantifiers mean through immersion and triangulation with natural language. For we understand what is meant by quantification into the position of a singular term in a predication in natural language. That constrains the interpretation of second-order quantification, which stands to predicates as first-order quantification stands to singular terms. This is similar to the approach one finds in Prior 1971 (Ch. 3) and Williamson 2003.

### 3.4 Plural Quantifiers

Much of the recent interest in plural quantification in logic and philosophy began with Boolos(1984)[^boolos-1984], who provided a plural interpretation of monadic second-order quantification. Boolos wanted to defend second-order axiomatizations of set theory against the charge that second-order quantification over the domain of all sets is incoherent, since there is no set of all sets. In response, he explained how to interpret the second-order quantifier, $\forall X$, over the domain of all sets in terms of the plural quantifier “some sets”, and how to interpret atomic formulas of the form $Xx$ in terms of the plural locution “is one of”. The fact that plural locutions are systematically used and perfectly understood in natural language, Boolos thought, helped address the charge of incoherence. The Boolos translation is described in detail in the entry on plural quantification.

Whatever the merits of the Boolos translation, plural quantification is nowadays generally distinguished from second-order quantification on the grounds that they bind expressions of different syntactic and semantic categories—while predicates are *unsaturated* in Frege’s terminology and contain argument places to be completed by expressions of an appropriate syntactic category, plural terms are often thought to be akin to *saturated* singular terms. Different variations on this theme may be found, for example, in Higginbotham 1998; Oliver & Smiley 2001; Rayo & Yablo 2001; Williamson 2003, 2013. This is a book, which includes an extensive discussion of important differences in the behavior of plural and second-order quantification in modal contexts. Plural quantification has consequently become the subject of its own study.

The language of plural quantification is carefully described in the entry on plural quantification. Syntactically, it is closely related to a two-sorted first-order language in which we have an infinite number of variables $xx$, $yy$, $zz$, $xx_{1}$, …. , and a two-place predicate $\prec$, read “one of,” which will be flanked by singular and plural terms, respectively. Identity predicate can only flanked by singular terms.

The axioms for plural quantification extend the axioms of quantificational logic with plural counterparts of ($\forall 1$), ($\forall 2$), and ($\forall 3$). Like in the second-order case, the axioms of quantification are supplemented with an axiom schema of plural comprehension:

- $\exists x A \rightarrow \exists xx \forall y(y \prec xx \leftrightarrow A)$ *provided $xx$ does not occur freely in $A$*.

One important difference with respect to monadic second-order logic is that instances of plural comprehension are conditionals that state that if something satisfies a certain condition, then some objects are all and only objects satisfying the condition. The antecedent of each conditional is motivated by an interpretation of the plural quantifier $\exists xx$ to mean “one or more objects”. Indeed, Linnebo (2013)[^linnebo-2013] explicitly supplements the theory of plural quantification with an axiom that states that no matter what some objects may be, there is at least one of them:

- $\forall xx \ \exists y (y \prec xx)$

Like in the case of second-order logic, we may provide at least two sorts of models for the theory of plural quantification. In both cases, we interpret plural quantification in terms of quantification over non-empty sets of individuals in the domain $D$. The difference is that in standard models we let plural variables range over the full power set of $D$, whereas plural variables range over a set $S$ of non-empty subsets of $D$, provided only that $S$ contains all sets definable by some formula.

Both approaches take place in a singular metalanguage. Since the models are based on set theory, they require the domain of individuals to form a set. Furthermore, the definition of satisfaction explains what is for a formula $\forall xx A$ to be satisfied in a model by an assignment in terms of *singular* quantification over non-empty subsets of the domain of individuals. This may perhaps encourage the impression that plural quantification is only intelligible as singular quantification over non-empty sets of individuals. Note, however, that neither the use of set-based models nor the use of singular quantification in the definition of satisfaction for a formula of the form $\forall xx$ is compulsory. In a plural metatheory in which we have a theory of ordered pairs, one may adapt the generalized conception of an interpretation developed in Rayo & Uzquiano (1999) to provide a plural model theory in which one uses neither. This model theory is developed, for example, in Burgess 2004.

The status of plural quantification remains controversial. All parties agree that plural locutions are systematically used in natural languages, but there is no consensus as to whether or not the truth conditions for plurally quantified sentences should ultimately involve covert reference to complex objects of some kind or another. The entry on plural quantification discusses some reasons generally offered in favor of the irreducibility of plural quantification to singular quantification over sets. But an influential argument against the identification of plural quantification and singular quantification over sets traces back to Boolos 1984, which claims that the following two sentences differ in truth value when we let the domain of quantification include all sets there are:

1. There is a set of all, and only, non-self-membered sets.
2. Some sets are all, and only, non-self-membered sets.

We know from Russell’s paradox that there is no set of all, and only, non-self-membered sets, which makes the first sentence false.[^note-13] But this is not to deny of course that some sets are all and only non-self-membered sets, even if they fail to compose a set. Unfortunately, the argument depends on a certain interpretation of Russell’s paradox that is itself controversial and will fail to convince philosophers who think that the moral of Russell’s paradox is that no singular quantifier can range unrestrictedly over all the sets there are.

Even if you take plural quantification at face value as opposed to covert singular quantification over sets, you may still think that the specification of some objects in the plural is all it takes to characterize a set whose members are exactly those objects. This type of consideration has recently led Florio and Linnebo (2021) to develop what they call “critical plural logic” as an alternative to classical plural logic characterized by a restriction of the axiom of plural comprehension above.

### 3.5 Propositional Quantifiers

It is not uncommon to let the vocabulary of classical quantificational logic include 0-place predicates, which are treated as propositional variables. This approach makes propositional logic a proper fragment of pure quantificational logic, and it construes quantification into the position of a sentence as a species of second-order quantification, i.e., quantification into the position of a 0-place predicate.

Or we may supplement the language of propositional logic with a propositional quantifier, $\forall$, which is allowed to bind propositional letters such as $p$, $q$, $r$, …. This is, for example, the course of action taken by Prior (1971)[^prior-1971], who outlines a system of propositional quantification. Prior insisted that propositional quantification should not be confused with either objectual quantification over propositions or substitutional quantification over sentences. Rather, propositional quantification is a species of non-nominal quantification, since it is quantification into sentence position.

#### 3.5.1 Quantified Propositional Logic

The vocabulary of quantified propositional logic contains propositional letters $p$, $q$, $r$, $p_1$, … and propositional connectives $\neg, \rightarrow, \wedge, \vee, \leftrightarrow$. We may as usual treat $\neg$ and $\rightarrow$ as primitive and take the others as defined. The usual recursive definition of a formula for propositional logic is appropriately supplemented with a clause that states that $\forall p A$ is a formula whenever $A$ is a formula.

#### 3.5.2 Axioms for Propositional Quantification

The axioms for propositional quantification are direct counterparts of $(\forall 1)-(\forall 3)$. Call a sentence $B$ *free for* a propositional variable $p$ in $A$ if, and only if, no free occurrences of $p$ lies within the scope of a quantification on $q$, $\forall q$ or $\exists q$, where $q$ is a propositional variable which occurs in $B$. Now:

- ($\forall^{P}1$) $\forall p A \rightarrow A(B/p)$ *provided $B$ is free for $p$ in $A$*.
- ($\forall^{P}2$) $\forall p(A \rightarrow B) \rightarrow (A \rightarrow \forall pB)$ *provided $p$ is not free in $A$*.
- ($\forall^{P}3$) from $A$, to infer $\forall p A$

For a taste of what they can do, notice that they yield a succinct justification of a rule of Uniform Substitution, whereby a formula of the form $A(B/p)$ is a theorem whenever $A$ is a theorem, provided that $B$ is free for $p$ in $A$. So, for example, if $p\rightarrow (q \rightarrow p)$ is a theorem, then $\neg r \rightarrow (q \rightarrow \neg r)$ is likewise a theorem, since this last formula is just $p\rightarrow (q \rightarrow p)(\neg r/p)$.[^note-14]

The axioms immediately deliver every instance of a propositional comprehension schema as a theorem:

- $\exists p(p \leftrightarrow A)$, *provided $p$ is not free in $A$*.

This is one important difference with respect to second-order quantification generally, since we are not automatically able derive every instance of second-order comprehension from the other quantificational axioms. On the other hand, a simple instance of existential generalization allows one to move from suitable formulas of the form $A \leftrightarrow A$ to an instance of propositional comprehension of the form $\exists p(p \leftrightarrow A)$.

#### 3.5.3 Propositional Quantification and Truth

Propositional quantification has been used in order to present a deflationary theory of truth. Grover, Camp, & Belnap (1975) and Grover (1992)[^grover-1992] have, for example, proposed to make use of propositional quantification in order to provide a variation on Ramsey’s redundancy theory of truth. The main claim they make is that we can conceive of phrases like “that is true” or “it is true” as *protosentences*, which are supposed to stand to sentences as pronouns stand to nouns; unlike pronouns like “it”, protosentences occupy sentence position, but just like pronouns may be used for purposes of cross-reference to earlier nouns, protosentences may be used for purposes of cross-reference to sentences uttered earlier in a conversation. Thus phrases like “that is true” or “it is true” are akin to propositional variables, which may be bound by propositional quantifiers.

#### 3.5.4 Intensional Paradoxes

Prior (1961)[^prior-1961] makes use of propositional quantification in order to provide an intensional version of the Liar Paradox. In particular, if $T$ is a sentential operator of the appropriate sort, then the following is a consequence of the axioms for propositional quantification:

- (P) $T \forall p(Tp \rightarrow \neg p) \rightarrow (\exists p(Tp \wedge p) \wedge \exists p(Tp \wedge \neg p))$

If we take $T$ as Prior did, to stand for the sentential operator “It is said by a Cretan that”, then we may read the theorem as the claim that if it is said by a Cretan that whatever is said by a Cretan is not the case, then there are at least two things said by a Cretan. So, quite unexpectedly, we learn that it is inconsistent to assume that the only thing said by a Cretan is that nothing a Cretan says is the case.

Prior’s observation makes no special appeal to special principles governing the behavior of the sentential operator he chose, and the result carries over to a range of propositional attitude operators such as “S believes that”, “S hopes that”, “S writes on the board at midnight that”, etc. It is, for example, inconsistent to suppose that the only thing S writes on the board at midnight is that everything S writes on the board at midnight is false.

Kaplan (1995)[^kaplan-1995] makes use of a related observation to raise a problem for the standard model theory for quantified propositional modal logic. He observed, in particular, that if $Q$ is a sentential operator of the appropriate sort, then the sentence (K) below is not satisfiable in anny possible worlds model $\langle W, \mathcal{I} \rangle$ consisting of a set of possible worlds $W$ and an interpretation function, $\mathcal{I}$ assigning a set of sets of possible worlds to the sentential operator:

- (K) $\forall p \Diamond \forall q (Qq \leftrightarrow p=q)$

When we let the propositional quantifier range over sets of worlds in $W$, we find that Kaplan’s sentence can only be satisfied in such a model if there is a map from the set of sets of worlds in $W$ into $W$, which is not possible on account of Cantor’s theorem. Kaplan thought this is a problem because the model theory for quantified propositional model should not unduly constrain the space of intuitive possibilities. If we interpret $Qp$ to mean that $p$ is Queried, i.e., it is asked whether it is the case that $p$, then (K) states that for every proposition, $p$, it is possible that $p$ and only $p$ is Queried.

The two observations are related. Prior’s theorem provides a witness to the claim that some propositions cannot be Queried uniquely. If the proposition expressed by the condition $\forall p(Qp\rightarrow \neg p)$ is the only proposition that is Queried, then it is true if and only if it is false. So, it can only be Queried if it is false. But it is false only if something true is Queried.[^note-15]

#### 3.5.5 Quantified Propositional Modal Logic

Propositional quantification made an early appearance in Lewis, Langford, & Lamprecht 1932, which is commonly acknowledged to have pioneered the study of modal logic. They outlined a formal system of modal logic with propositional quantification, which they used to formulate an *Existence Postulate* designed to guarantee the existence of at least two propositions that are consistent and independent from each other. (This is postulate B9 in the entry on the modern origins of modal logic.) They used the postulate to make sure strict implication did not collapse into material implication.[^note-16]

Kripke (1959)[^kripke-1959], Fine (1970)[^fine-1970], and Kaplan (1970)[^kaplan-1970] went on to consider systems of propositional modal logic supplemented with propositional quantifiers governed by appropriate axioms and rules of inference. Moreover, they explained how to generalize the Kripkean model theory for propositional modal logic in order to accommodate the presence of propositional quantification. A Kripke model for the language of propositional modal logic is an ordered triple, $\langle W, R, \mathcal{I} \rangle$, in which $W$ is a non-empty set of worlds, $R$ is a binary relation on $W$, and $\mathcal{I}$ is an interpretation function, which can be taken to assign a set of possible worlds to each sentence letter in the language. This suggests we interpret propositional quantification in terms of quantification over sets of worlds in $W$. An assignment of values to the propositional variables $s$ will map each propositional variable into a set of worlds, and we define satisfaction at a world by an assignment $s$ as usual, except for an appropriate clause for the quantifier: $\forall p A$ is satisfied at a world $w$ in $W$ in $\langle W, R, \mathcal{I} \rangle$ by assignment $s$ if, and only if, $A$ is satisfied at $w$ by every assignment $s[p/S]$ in which $S$ is a subset of $W$. The definitions of truth at a world and truth in a Kripke model then proceed as usual.

The axioms for propositional quantification are sound with respect to the class of extended Kripke models for quantified propositional modal logic. Unfortunately, they are not complete with respect to the same class, since they do not allow us to derive the following as a theorem:

- $\exists p(p \wedge \forall q(q \rightarrow \Box (p \rightarrow q)))$

However, this formula is valid in every extended Kripke model for the simple reason that its truth at a world in a model only requires the existence of a maximally specific proposition, one which is true at exactly one world.

#### 3.5.6 How to Understand Propositional Quantification

The question remains of how to understand quantification into sentence position. One may in fact be tempted to assimilate propositional quantification to either singular quantification over propositions or to substitutional quantification over a range of sentences. While Prior (1971)[^prior-1971] and Grover (1972)[^grover-1972], for example, take propositional quantification to be importantly different from singular and substitutional quantification, Richard (1996)[^richard-1996] suggests that propositional quantification should at the end of the day be treated as a species of singular quantification, e.g., singular quantification over propositions. Indeed, one may be tempted by this option by reflecting on what we did above. We expanded the language of propositional modal logic with a new style of quantification, but the model theory explained the truth conditions associated with the propositional quantifier, $\forall p A$, in terms of singular quantification over sets of worlds in the model.

One question is how to develop a fruitful model theory for the language of quantified propositional logic and another question is whether there is an intelligible interpretation of the formalism on which propositional quantification is construed as neither singular quantification over propositions nor as substitutional quantification over a range of sentences. One option at this point is to deny again that the interpretation of propositional quantification should be determined by either the model theory for the language or by translation into some fragment of natural language. Indeed, one may adopt the line we mentioned above in connection to second-order quantification. The best method to learn what is meant by a propositional quantifier is through immersion and triangulation with natural language by reflection on the fact that propositional quantifiers stand to sentences as first-order quantifiers stand to singular terms.

## 4. Quantification and Ontology

Much of contemporary ontology builds on the assumption that existence is to be understood in terms of quantification: in a slogan, to exist is to be something. Ontology is largely concerned with the domain of the *existential* quantifier. This assumption can be traced back to the work of Frege and Russell, both of whom analyzed quantification in terms of predication, and plays a crucial role in Quine’s admonition to transform ontology into the study of the ontological commitments of our global theory of the world regimented in the language of quantificational logic and identity.

### 4.1 Quantification, Predication, and Existence: Frege and Russell

By the link between quantification and existence, we mean the claim that to exist is to be identical to something. This view can be traced back to Frege and Russell, who offered roughly the same broad analysis of quantification in terms of predication. The entry on existence provides a helpful overview and discussion of their account of existence against the background of the historical context in which they produced it. In what follows, we highlight a distinction between the Frege-Russell analysis of quantification in terms of predication, on the one hand, and the link between quantification and existence, on the other.

#### 4.1.1 Quantification and Predication

Frege (1980a, 1980b)[^frege-1980a][^frege-1980b] explicitly analyzed quantification in terms of predication. For Frege, first-level predicates express concepts under which objects fall. A quantifier expresses a second-level concept under which first-level concepts fall. In particular, he proposed to take a sentence like (3) below to predicate of a first-level concept that it has instances:

- (3) There is at least one square root of 4.
- (4) The concept *square root of 4* is instantiated.

The existential quantifier, $\exists$, is, for Frege, a second-level predicate, which expresses a second-level concept under which a first-level concept such as *square root of 4* falls if and only if it has some instances. Likewise, the universal quantifier, $\forall$, is a second-level predicate, which expresses a second-level concept under which a first-level concept such as *self-identical* falls if and only if it has all objects as instances.

Russell (1905)[^russell-1905] offered a similar account of quantification. On Russell’s analysis, the proposition expressed by (5) predicates of a certain propositional function that it maps every object whatever into a true proposition. (The entry on propositional functions provides more detail on the role of propositional functions in the early development of modern logic.)

- (5)Everything is self-identical.
- (6)The propositional function $x$ *is self-identical* is always true.

The propositional function $x$ *is self-identical* maps the Moon to the true proposition that the Moon is self-identical, it maps the Sun to the true proposition that the Sun is self-identical, etc. The thrust of (5) is the proposition that no matter what object we supply as argument, the propositional function $x$ *is self-identical* will map it into a true proposition. The only salient difference between Frege and Russell’s account of quantification lies in the choice of concepts and propositional functions, respectively, as the objects of predication; while Frege takes each quantifier to correspond broadly to a second-level concept, Russell analyzes them in terms of certain properties of propositional functions.

#### 4.1.2 Quantification and Existence

Both Frege and Russell combine their account of quantification in terms of predication with the substantive thesis that existence is to be understood in terms of quantification. For Frege, existence is to be identified with the second-level concept expressed by the second-level predicate expressed by $\exists$. For Russell, existence is identified with a certain property of propositional functions, e.g., being sometimes true. This may seem overkill; if true, it might seem that only first-level concepts exist, not the objects they instantiate. For only first-level concepts are instances of the second-level concept expressed by $\exists$.[^note-17] Instead, they are mostly concerned with the thesis that statements of existence such as (7) are *not* cases in which a primitive property of existence is predicated of an object, but rather should be understood as an implicitly quantified statement such as (8), which is to be analyzed in terms of predication in (9) and (10) for Frege and Russell, respectively:

- (7) 2 exists.
- (8) Something is identical to 2.
- (9) The concept *identical to 2* is instantiated.
- (10) The propositional function $x$ *is identical to 2* is sometimes true.

This point is perfectly compatible with the existence of a first-level concept under which all and only those objects that exist fall. Take, for example, the concept *being self-identical*. Likewise for Russell. The propositional function $x$ *is self-identical* will map all objects that exist into a true proposition.

Note, however, that one could in principle retain their analysis and deny, for example, that first-level concepts and propositional functions, respectively, can only be saturated by objects that exist. One could take the view that some great philosophers who once existed, no longer exist. Socrates, for example, was a great philosopher who no longer exists. He can nevertheless instantiate the first-level concept *admired by many philosophers*. Or consider the bookcase I would have built, had I finally assembled all the materials I purchased according to the assembly instructions that came with them. I have had concrete plans to build the bookcase for ages now; never mind the fact that I may never find the skill, time or energy to assemble it. My planned bookcase does not exist yet, and knowing myself, it might well never exist. But one might take the view that we can refer to it and that it instantiates many first-level concepts such as *being a planned bookcase*. On a view like this, the assertion that there are planned bookcases that do not exist would remain true even if none of its instances exist.

A view like this would be classified as a form of Meinongianism by Nelson (2012)[^nelson-2012], and it would be subject to some of the difficulties other forms of Meinongianism face. Suffice it to say, for present purposes, that it would, however, require a radical departure from a very influential approach to ontology advocated by Quine and endorsed by philosophers like Peter van Inwagen and David Lewis and their followers.

### 4.2 Quine’s Criterion of Ontological Commitment

Quine (1948)[^quine-1948] explicitly characterizes ontology as an attempt to answer the question “what is there?” As he observed, the question may seem deceptively simple, since it may be answered in a word: “everything”. The problem with this answer is that it is largely uninformative. All parties agree that everything is something, but there is still plenty of room of disagreement as to what kinds of objects are there. Are there mereologically composite objects? Are there concrete possible worlds? Are there mathematical objects? If there are such objects, then they will of course lie in the domain of the quantifier “everything”. However, philosophers are still intensely divided as to whether they do.

Quine’s strategy for the regimentation and resolution of ontological disputes has informed much of contemporary ontology. He advised philosophers to look at the ontological commitments incurred by our best global theory of the word—best by ordinary scientific standards or principled extensions thereof—when appropriately regimented in the language of pure quantificational logic with identity.[^note-18] One may perhaps think of the ontological commitments of our best global theory of the world as the demands that the truth of our total theory imposes on the world. For example, we are committed to the existence of objects of kind $K$ if a proper regimentation of our best global theory includes—or entails—a sentence of the form $\exists x Fx$, where $F$ is a predicate under which only objects of kind $K$ fall. Quine’s advice comes accompanied with a criterion of ontological commitment whereby an appropriately regimented body of doctrine is ontologically committed to objects of kind $K$ just in case objects of kind $K$ *must* lie in the range of our bound variables for the sentences of our theory to be true. More details are given in section 5 of the entry on Quine.

As Cartwright (1954)[^cartwright-1954] observed, it is far from clear how one is supposed to interpret the modality in Quine’s official formulation of the criterion. A purely extensional version of the criterion is plainly inadequate: $T$ is ontologically committed to objects of kind $K$ if, and only if, $T$ is true *only if* the variables range over objects of kind $K$. But the material conditional is much too weak for Quine’s purposes as it makes any false theory to be ontologically committed to all kinds of objects.[^note-19] Quine’s general hostility to non-extensional notions makes the problem all the more delicate for him.

Under Quine’s approach to ontology, an argument for the existence of objects of kind $K$—whether mereologically complex objects, or concrete possible worlds, or mathematical objects—takes the form of an argument for the thesis that quantification over such objects is indispensable to our best global theory of the world. One of the most familiar instances of such arguments is the Quine-Putnam argument for the existence of mathematical objects. Since mathematical objects are indispensable for scientific purposes, we should expect the quantifiers of our best global theory of the world to range over them. But once we settle the question of whether the quantifiers of our best global theory of the world range over mathematical objects, we have settled the ontological question of whether such objects exist. The entry on indispensability arguments in mathematics includes extensive discussion of this and related indispensability arguments in mathematics. Similar arguments have been deployed outside mathematics to argue for the existence of possible worlds, mereologically complex objects, and the like.

This brings us to a family of applications for different styles of quantification explored above. It is not uncommon to respond to indispensability arguments for the existence of objects of a certain kind by means of a paraphrase strategy, which if successful, would show how to make do without the ontological commitment to objects of the offending kind. Oftentimes, the paraphrase will involve a different style of quantification, whether an alternative to classical quantification or an extension thereof. For example, Gottlieb (1980)[^gottlieb-1980] attempted to respond to the Quine-Putnam indispensability argument for the existence of numbers by dispensing with objectual quantification in favor of substitutional quantification in arithmetic. Burgess & Rosen (1997) provides an extensive catalogue of different expressive resources philosophers have used in order to bypass apparent commitment to mathematical objects. Or take the question, for example, whether there are composite objects of various kinds. Dorr & Rosen (2002), Hossack (2000)[^hossack-2000]; and van Inwagen (1995)[^inwagen-1995] have each argued that plural quantification can be used to paraphrase away apparent ontological commitment to composite objects—other than organisms in van Inwagen’s case: we need only replace apparent singular quantification over composite objects with plural quantification over its alleged parts, and replace apparent singular predications of a composite object with plural predications of their parts.[^note-20]

### 4.3 Unrestricted Quantification

When Quine answers “everything” to the fundamental ontological question of what there is, he presumably intends the quantifier to range unrestrictedly over all objects at once. This observation applies to ontological inquiry more generally. When a nominalist asserts that there are no mathematical objects, she does not intend the thesis to be qualified by a restriction to a domain of concrete objects; otherwise, the thesis would be devoid of interest. But unrestricted quantification is not a very common phenomenon outside highly theoretical contexts such as logic and ontology. Take a typical use of a quantifier expression in English as exemplified in a typical utterance of the sentence:

- (11) Everything is on sale.

In a typical context, the use of the quantifier “everything” is tacitly restricted to a domain of contextually salient objects. In particular, it would be inappropriate for another participant in the conversation to point out that the Moon is not on sale. The Moon is not an exception to the statement made by my utterance of (11) because the Moon does not lie in the domain of quantification associated to my use of the quantifier.

But the fact that unrestricted quantification is relatively uncommon is no reason to doubt it is attainable in certain contexts. Unfortunately, many philosophers have recently doubted that genuinely unrestricted quantification is even coherent, much less attainable.[^note-21] Note that these philosophers face at least two preliminary challenges, both of which are forcefully pressed by Williamson (2003)[^williamson-2003]. First, they face the question of what to make of the prospects of ontological inquiry without unrestricted generality. How should we formulate substantive ontological positions such as nominalism, if we cannot hope to quantify over all objects at once? The second challenge for the skeptics is to state their own position. To the extent to which the thesis that we cannot quantify over everything appears to entail that there is something over which cannot quantify, skeptics seem to find themselves in a bind by inadvertently quantifying over what, by their own lights, lies beyond a legitimate domain of quantification.[^note-22] Typical responses to each problem involve a surrogate for unrestricted generality in the form of either schematic generality or the use of certain modal operators to simulate quantification over a series of ever more comprehensive domains of quantification.[^note-23]

At the core of the problem lies the assumption that the set-theoretic paradoxes cast doubt upon the existence of a comprehensive domain of all objects. What they reveal, according to Dummett (1991, 1993)[^dummett-1991][^dummett-1993], is the existence of indefinitely extensible concepts like *set*, *ordinal*, and *object*. For Dummett, the indefinite extensibility of *set* is incompatible with the existence of a comprehensive domain of all sets, since no matter what putative domain of all sets we isolate, we find that we can employ Russell’s reasoning to characterize further sets that lie beyond the putative domain of all sets with which we began. The set of all non-self-membered sets in the initial domain cannot, on pain of contradiction, be in that domain, which means that it must lie in a more comprehensive domain of all sets. If there is no domain of all sets, there is, the thought continues, no hope for a domain of all objects. One may respond to this line of argument by contesting Dummett’s diagnosis of the set-theoretic antinomies. Boolos (1993)[^boolos-1993] suggests that we take Russell’s paradox, for example, to establish that not every condition determines a set. The moral of Russell’s paradox is that there is no set of all non-self-membered sets, not that it lies beyond the initial domain of quantification.

For another line of attack against the coherence of unrestricted quantification, one may ask what exactly is a domain of quantification supposed to be. Skeptics often take a page from modern model theory and think of a domain of quantification as a set—or at least as a set-like object, which contains as members all objects over which the putatively unrestricted quantifier is supposed to range. They take for granted that for a speaker to be able to quantify over some objects, they must all be members of some set-like object, which constitutes a domain of quantification. Cartwright (1994)[^cartwright-1994] called this thesis the All-in-One Principle. Now, if there is unrestricted quantification, then the domain of quantification associated to it cannot be a set-like object. For we could then deploy a suitable variation on Russell’s paradox in order to obtain a contradiction.[^note-24] Many have concluded from this that there is no genuinely unrestricted quantification over all objects at once.

The All-in-One principle is not beyond doubt. One application of plural quantification, which is explored by Cartwright (1994)[^cartwright-1994], is to abandon the All-in-One principle and to understand talk of a domain of quantification not as singular talk of collections but rather as plural talk of its members. To speak of a domain of certain objects is just to speak of the objects themselves—or to speak of a first-level concept under which they all fall; and to claim of a given object that it lies in the domain is to claim of the object that it is one of them. Alternatively, one may opt for the expressive resources of second-order quantification with the second-order quantifiers taken to range over Fregean concepts. Williamson (2003)[^williamson-2003] outlines a conception of a domain of quantification as a Fregean concept under which certain objects may fall. To speak of a domain of all objects on this view is to speak of a Fregean concept under which all objects—without restriction—fall, and to claim of a given object that it lies in the domain is merely to claim that the object falls under the relevant Fregean concept.

### 4.4 Quantification, Tense and Modality

The combination of quantification and modality traces back to Barcan (1946, 1947)[^barcan-1946][^barcan-1947] and Carnap (1946)[^carnap-1946]. Historically, however, this combination came under sustained attack by Quine, who, like Carnap, assumed that $\Box$ could only interpreted in terms of logical necessity or analyticity. As Carnap himself recognized, the linguistic conception of necessity raises the question of how to assign intelligible truth conditions to *de re* modal generalizations of the form $\exists x \Box Px$.[^note-25] For the truth conditions for such a sentence appear to require one to make sense of the truth of an open formula of the form $\Box Px$ with respect to an assignment of a value to the variable $x$. If we read $\Box$ to mean: “it is analytic that”, then one may wonder what sense could be made of the claim that an open formula $Px$ is analytic with respect to an assignment of an object to $x$. Quine had anticipated the issue in Quine (1943)[^quine-1943], and he pressed the criticism again in Quine (1953, 1960)[^quine-1953][^quine-1960]. Quine’s objections are commonly taken not to apply to other interpretations of $\Box$ in terms of metaphysical necessity as discussed, for example, in Kripke (1980)[^kripke-1980]. When we move past Quine’s criticisms and combine pure quantificational logic with propositional modal logic, we obtain quantified modal logic.

The interaction of quantification and modality turns out to raise difficult philosophical problems. As we will see, some of these difficulties have, in fact, inclined some philosophers to rethink the scope of pure quantificational logic. The problem is that certain theorems of quantified modal logic suggest that everything is necessarily something. The subject matter of ontology is necessary: nothing could have failed to be something.

#### 4.4.1 Quantification and Modality

Quantified modal logic is the system that combines pure quantificational logic with propositional modal logic. Propositional modal logic investigates the logic of the modal operators $\Box$ and $\Diamond$ and is discussed in the entry on modal logic. The language of propositional modal logic supplements the language of propositional logic with the sentential operator $\Box$, and $\Diamond$ may then be explicitly defined as $\neg \Box \neg$. A weak propositional modal logic called K logic includes as axioms all tautologies and all instances of schema K:

- (K)$\Box(A \rightarrow B) \rightarrow (\Box A \rightarrow \Box B)$

The rules of inference of the system include *modus ponens* and what is often known as a rule of necessitation:

- (RN)from $A$, infer $\Box A$

The combination of propositional modal logic and pure quantificational logic is often called quantified modal logic and is discussed in section 13 of the entry on modal logic and the entry on the possibilism-actualism debate. This combination immediately delivers what we may call the *necessity of being*:

- (NB)$\forall x \Box \exists y(x=y)$

The key to this observation is that the open formula $\exists y (x = y)$ is a theorem of pure quantificational logic. Successive applications of the rule of necessitation and universal generalization are all it takes to complete the proof.

On the alethic interpretation of $\Box$ in terms of metaphysical necessity, this theorem reads as the claim that everything is necessarily something. Take the Griffith Observatory, for example. It is a consequence of the theorem that it is necessarily something. The Griffith Observatory would have been something even if no funds had been available for construction and nothing had ever been built in the site it occupies. And what is true of the Griffith Observatory is true of us: each of us is necessarily something. When we combine this result with the link between quantification and existence, we conclude that everything exists necessarily, which flies in the face of the assumption that we exist only contingently.

With the help of schema K, one may prove the Converse Barcan Formula:

- (CBF)$\Box \forall x A \rightarrow \forall x \Box \ A$

On the alethic interpretation of the modality, this states that if necessarily, everything is $A$, everything is necessarily $A$. The proof is given, for example, in one of the supplements to the entry on the possibilism-actualism debate. But this provides another route to the necessity of being: since necessarily, everything is something, everything is necessarily something. In the presence of a further plausible modal principle, B, we may even prove the Barcan Formula. The Brouwerian principle, B, states that whatever is the case is necessarily, possibly the case:

- (B)$A \rightarrow \Box \Diamond A$

The Barcan Formula states that if everything is necessarily $A$, then necessarily, everything is $A$:

- (BF)$\forall x \Box A \rightarrow \Box \forall x A$

Or, equivalently:

- $\Diamond \exists x A \rightarrow \exists x \Diamond A$

The entry on the possibilism-actualism debate includes a supplement with a proof of BF against the background of (B). But this formula is deemed unacceptable by many philosophers. Consider my plans to build a bookcase. Even if I never manage to build one, it is certainly possible for me to build one. So, it is possible for there to be some bookcase I have built. By the Barcan Formula, it seems to follow that something is possibly a bookcase I build. The Barcan Formula does not settle whether or not this object is in fact a concrete object, much less a bookcase one may in fact use to store one’s books. In fact, to deny this is one way to come to terms with the Barcan Formula.

#### 4.4.2 Quantification and Tense

What is true of the combination of pure quantificational logic with propositional modal logic is *mutatis mutandis* true of the combination of pure quantificational logic and propositional tense logic. Certain theorems of quantified tense logic suggest that everything has always been, is, and will always be something. The domain of ontology is immutable: nothing ever fails to be something.

Propositional tense logic investigates the logic of tense operators like $H$, read: “it has always been the case that”, $P$, read: “it was the case that”, $G$, read: “it will always be the case that”, and $F$, read: “it will be the case that”. In place of K, we have distribution axioms:

- $H(A \rightarrow B) \rightarrow (HA \rightarrow HB)$
- $G(A \rightarrow B) \rightarrow (GA \rightarrow GB)$

And in place of the rule of necessitation, we have rules of temporal generalization:

- from $A$, infer $HA$
- from $A$, infer $GA$

More details are provided in the entry on temporal logic.

The combination of propositional tense logic and pure quantificational logic immediately delivers the eternality of being:

- (EB)$\forall x (G\exists y(x = y) \wedge \exists y(x = y) \ \wedge F\exists y(x = y))$,

which states that everything has has always been, is, and will always be, something. The Griffith Observatory was something even before it was built in 1935—and will always be something—even billions of years from now. And what is true of the Griffith Observatory is true of us: each of us has always been, is, and will be something—even before our birth and long after our death.

Quantified tense logic proves temporal versions of CBF:

- $H \forall xA \rightarrow \forall x H A$
- $G\forall x A \rightarrow \forall x G A$

And, finally, we have two temporal versions of BF:

- $\forall x H A \rightarrow H \forall x A$
- $\forall x G A \rightarrow G \forall x A$

In order to appreciate the difficulty, we may take the contrapositive of the temporal version of BF for $H$, where $P$ is defined as usual, as: $\neg H \neg$:

- $P \exists x A \rightarrow \exists x P A$

We infer, for example, that there were dinosaurs only if there are past dinosaurs. If to exist is to be something, then past dinosaurs exist. But whether this commits us to flesh-and-blood dinosaurs is of course a different matter, since being a past dinosaur need not require being a dinosaur.

#### 4.4.3 From Logic to Ontology

The interaction between pure quantificational logic and tense and modality suggests the domain of ontology is immutable and necessary. But we can only draw these conclusions by making use of some auxiliary assumptions, some of which are far from obvious. The highly counterintuitive character of the conclusions has consequently led many philosophers to place some of the auxiliary assumptions under close scrutiny. Other philosophers have followed argument where it leads, and they have sought to reconcile the eternal and necessary character of the domain of ontology with the apparent temporary and contingent character of existence. In fact, Williamson 2013 set out to provide a separate battery of arguments for the necessity and immutability of ontology.

One auxiliary assumption one may question is the traditional link between quantification and existence. Even if there is no change in the domain of quantification, you may nevertheless think that existence is only temporary. Socrates did not exist either before 490 BCE or after 399 BCE, and the mere fact that he is, has and will always be something is not reason to attribute existence to him. One variant of this move is a direct descendant of Meinong’s view on existence as a mere species of being. But to the extent to which Meinongianism may be accompanied with the implausible thesis that no matter what condition we substitute for $F$ in “the $F$ is $F$” gives rise to a true sentence, it would seem to entail that “the round square is a round square” is true, which seems hopeless. But the Meinongian thesis is not compulsory for more plausible developments of the view that not everything exists, even though everything is something.[^note-26] What is not negotiable, though, is the thesis that existence should not be taken to be expressed by a quantificational expression, but rather by a predicate which may or not apply to objects in the domain. The moral of the temporal versions of BF and CBF is only that unrestricted quantification ranges over an immutable and necessary domain of objects, whether or not they enjoy temporary and contingent existence. The difficult question remains of how to answer Quine’s question “what is there?” once one abandons the thesis that no matter what condition $F$ may be, there are objects that satisfy the condition. For more on different variants of Meinongianism, the reader may consult the entry on existence.

There is, in the second place, the assumption that the axioms of pure quantificational logic remain true when we expand the language to include other sentential operators, whether temporal, modal or otherwise.[^note-27] What is perhaps the most common response to our predicament is to recoil from pure quantificational logic into a suitably weakened variant of it. This is, for example, the path taken in Kripke (1963)[^kripke-1963], where Kripke proposes to weaken the axiom of universal instantiation in line with the first version of inclusive quantificational logic discussed earlier. Since $\exists y(x = y)$ is not a theorem of inclusive quantificational logic, we are not in a position to necessitate, which blocks the derivation of the necessity of being.[^note-28] Kripke’s quantified modal logic is discussed in the entry on the possibilism-actualism debate. Others have fallen back into alternative forms of free logic, but there appears to be no consensus as to which one is the best alternative to pure quantificational logic. It may be helpful to note, however, that some of the relevant free logics merely restrict the axiom of universal instantiation by means of an existence predicate and do nothing to block the derivation of other allegedly problematic principles such as the necessity of identity, which is the thesis that everything is necessarily self-identical. Since, presumably, an object can only be necessarily self-identical if it exists necessarily, opponents of CBF will also want to have some resources to block the necessity of identity.

The derivability of the necessity of identity from the axioms of identity and the rule of necessitation may perhaps invite one to consider another option. Maybe the culprit is not pure quantificational logic, but rather the indiscriminate use of the rule of necessitation. The rationale for necessitation is that every provable sentence should be necessarily true, but it is not clear how this thought is supposed to generalize to open formulas, which, strictly speaking, are not true or false. Open formulas are merely true or false under an assignment of values to their free variables. But the fact that $x = x$, for example, is true under an assignment $s$ on which $x$ is assigned a table is no reason to think that $x = x$ is necessarily true under such an assignment if you think that the table could have not been there.[^note-29] One problem for this strategy is that it is of little help when we allow closed terms such as constant symbols into the language of quantified modal logic. In the presence of constant symbols, classical quantificational logic allows us to derive the sentence $\exists x (a = x)$ as a theorem, whence, by necessitation for complete sentences, we infer $\Box \exists x(a = x)$, which seems objectionable if $a$ is suppose to regiment a name for an object that exists only contingently. One could avoid the problems by barring closed terms from the language, but such a radical exclusion seems *ad hoc* and artificial. So, if one chooses to restrict necessitation, one must provide a different rationale for it. Deutsch (1990)[^deutsch-1990] provides an example of this strategy.

The fourth and final option to consider is to take the derivability of CBF in tense and modal logic at face value, and embrace the conclusion that existence is indeed immutable and necessary. These are the theses that Williamson (2013)[^williamson-2013] calls “permanentism” and “necessitism”. The task for each approach is to explain our initial reluctance to embrace them in the first place. Take the apparent resistance to accept the claim that Socrates will always be something despite the fact that he died in 399 BCE. The permanentist may respond that if we are initially disinclined to accept this claim, it is only because we mistakenly think that because a person, for example, is a concrete object, a past or a future person must be concrete as well. Socrates, which is a past person, was not a person either before 490 BCE or after 399 BCE; indeed, Socrates is now not a person, nor will he be one in the future. Likewise, a merely possible person need not be a person either and neither the Barcan nor the Converse Barcan Formula threaten the temporary and contingent character of concreteness. Since I could have found the time, skill and energy to build a bookcase, some object is possibly a bookcase built by me. But the necessitist will be at pains to add that to be a possible bookcase built by me is not to be a bookcase built by me, much less a bookcase. This outlook is defended by Linsky & Zalta (1994) and Williamson (2013)[^williamson-2013]. But there are other points of contact. For example, all versions of necessitism must reject unqualified “essentialist” theses such as the view that a person is necessarily a person; at most, one can perhaps maintain the weaker thesis that a person is necessarily if concrete, a person. Likewise, all versions of necessitism seem committed to the actual existence of many more nonsets than can form a set. Sider (2009)[^sider-2009], for example, argues that necessitism is committed to the actual existence of at least *κ* nonsets for each set-theoretic cardinal *κ*. And Hawthorne & Uzquiano (2011) raises other cardinality problems for a combination of necessitism with certain common mereological assumptions.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=quantification). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/quantification/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=quantification&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/quantification/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- [PhilPapers on Quantifiers](http://philpapers.org/browse/quantifiers/)

## Related Entries

Aristotle, General Topics: logic | existence | generalized quantifiers | logic: and ontology | logic: classical | logic: free | logic: intuitionistic | logic: modal | logic: second-order and higher-order | model theory | ontological commitment | plural quantification | possibilism-actualism debate | square of opposition

## Notes（原文脚注）

[^note-1]: It is not difficult to give examples of quantifier phrases of different syntactic categories. Certain adjectives such as “finite”, “uncountable” and adverbs such as “sometimes”, “often”, and “never” may likewise be used to make general statements. Even non-phrasal constructions such as “there is” or “there are” may express generality.

[^note-2]: In what follows, we will sometimes omit a pair of parentheses in accordance to standard abbreviations in logic. We will, for example, let the expression $B \rightarrow C$ abbreviate $(B \rightarrow C)$.

[^note-3]: Notice that the validity of theorems like $\exists x(Px \rightarrow Px)$ and $\forall x Px \rightarrow \exists x Px$ is merely a byproduct of the stipulation that the domain of a model be non-empty.

[^note-4]: Note the role of Completeness. Kreisel's argument will not be available for some of the extensions of quantificational logic for which no completeness result is available.

[^note-5]: Note that we could in principle treat constants as zero-place function symbols.

[^note-6]: Symmetry is given by the formula $\forall x \forall y(x = y \rightarrow y =x)$, whereas Transitivity is given by the formula $\forall x \forall y \forall z ((x = y \wedge y = z) \rightarrow x=z)$.

[^note-7]: See Williamson (1999)[^williamson-1999] for a discussion of the problem.

[^note-8]: Notice that in an intuitionistic framework, we must take all the usual propositional connectives $\wedge$, $\vee$, $\rightarrow$, and $\neg$ to be part of the primitive vocabulary.

[^note-9]: Since the cardinality of the power set of the set of natural numbers, $\wp (\mathcal{N})$, is greater than $\aleph_0$, i.e., $2^{\aleph_0} > \aleph_0$, we know that $2^{\aleph_0} \geq \aleph_1$. Unfortunately, the axioms of set theory do not settle the question of whether $\aleph_1$ is in fact $2^{\aleph_0}$.

[^note-10]: Some axiomatizations of second-order logic add a version of the axiom of choice, which states, very roughly, that for any dyadic relation $R$ whose domain includes all individuals, there is a sub-relation $S$ of $R$ that pairs each object in the domain with exactly one object.

[^note-11]: This reflection principle, which is due to Bernays (1976)[^bernays-1976] is a second-order generalization of the reflection principle of Montague (1966)[^montague-1966] and Levy (1960)[^levy-1960].

[^note-12]: The reader may consult Rayo & Uzquiano (1999) and Rayo & Williamson (2003)[^williamson-2003] for details.

[^note-13]: We reason by reductio. Suppose that $R$ is a set of all, and only, non-self-membered sets. Then $R$ is a member of $R$ if and only if $R$ is not a member of $R$. If $R$ is a member of $R$, then, since $R$ contains only non-self-membered sets, $R$ is not a member of $R$. But on the other hand, if $R$ is not a member of $R$, then since $R$ contains all non-self-membered sets, $R$ is a member of $R$. By propositional logic, a contradiction follows from the claim that $R$ is a member of $R$ if and only if $R$ is not a member of $R$.

[^note-14]: Here is the argument:

1. $\vdash A$ $A$ is a theorem
2. $\vdash \forall p A$ by $(\forall^p 3)$
3. $\vdash \forall p A \rightarrow A(B/p)$ $(\forall^p 1)$ since $B$ is free for $p$ in $A$.
4. $\vdash A(B/p)$ Modus Ponens 2, 3

[^note-15]: In fact, Kaplan's observation can be strengthened further. Consider the sentence:

$\forall p \Diamond \forall q (Qq \leftrightarrow (p \leftrightarrow q))$.

This sentence tells us that for each proposition $p$ it is possible to Query only propositions with the same truth value as $p$. Not only is this sentence unsatisfiable in simple possible worlds models of the sort outlined above, it is, in fact, inconsistent in the presence of necessitation. For details, the reader may consult Bacon, Hawthorne, and Uzquiano (2016). Uzquiano (2021)[^uzquiano-2021] discusses a family of related observations.

[^note-16]: See Williamson 2013, Chapter 5, section 2 for further discussion.

[^note-17]: This point is made in Soames 2014, chapter 1 on Frege and chapter 11 on Russell.

[^note-18]: Pure quantificational logic because, for Quine, the use of a name carries no commitment to the object allegedly named by it.

[^note-19]: Matters are not much better if one requires the material conditional to be a logical truth.

[^note-20]: There are some limits to the strategy of plural paraphrase, which are explored in Uzquiano (2004)[^uzquiano-2004].

[^note-21]: For examples, the reader may consult Dummett 1991; Fine 2006; Glanzberg 2004; Hellman 2006; Lavine 2006; and Parsons 2006.

[^note-22]: Recall that the inference from $\neg \forall x A$ to $\exists x \neg A$ is not intuitionistically valid. Indeed, some opponents of unrestricted generality like Michael Dummett have in fact advocated the use of intuitionistic logic for putatively unrestrictedly general statements. Santos (2013)[^santos-2013] develops these issues further.

[^note-23]: For a survey of some of these moves, the reader may consult some of the pieces in Rayo & Uzquiano (2006).

[^note-24]: For suppose that a certain set-like object, $D$, is the relevant domain. An attractive principle for domains of quantification is an analogue to a separation principle for set theory: if $D$ is a domain of quantification and $A(x)$ is a condition, which may perhaps be expressed by a predicate of the language, then the restriction of the domain to the objects that satisfy the condition constitutes another domain of quantification. In particular, if $D$ is the domain associated to a truly unrestricted use of the quantifier, then there is a domain, $R$, of all and only objects in $D$, which are not members of themselves. The problem of course is that $R$ cannot be a member of $D$ on pain of contradiction. (If $R$ is a member of $D$, then either $R$ is in $R$ or $R$ is not in $R$. But if $R$ is in $R$, then $R$ is a member of $D$ that fails to satisfy the condition *non-self-membered*, whence $R$ is not in $R$. And if $R$ is in $R$, then $R$ is a member of $D$ that satisfies the condition *non-self-membered*, whence $R$ is in $R$.) But if $R$ is not in $D$, then $D$ is not the domain associated to a truly unrestricted use of the quantifier.

[^note-25]: Carnap's own response was to appeal to a different style of quantification, whether substitutional or quantification over individual concepts.

[^note-26]: See for example T. Parsons (1980)[^parsons-1980] and E. Zalta (1988)[^zalta-1988] and Priest (2005)[^priest-2005].

[^note-27]: It should be clear that perfectly parallel arguments should enable one to prove versions of CBF for other sentential operators such as “it is true according to fiction $F$” or “it ought to be the case”.

[^note-28]: The sentence $\forall x \exists y (x = y)$ is of course a theorem of the weaker quantificational logic, but once we necessitate, we only obtain the harmless $\Box \forall x \exists y(x = y)$.

[^note-29]: Compare Burgess (2009)[^burgess-2009]. Similar proposals are made in Prior 1957; Adams 1981; Menzel 1991; and Wiggins 1995.

[^adams-1981]: Adams, R., 1981, “Actualism and Thisness”, *Synthese*, 49(1): 3–41.

[^bacon-2016]: Bacon, A., Hawthorne, J., and Uzquiano, G., 2016, “Higher-Order Free Logic and the Prior-Kaplan Paradox”, *Canadian Journal of Philosophy* 46(4–5): 493–541.

[^barcan-1946]: Barcan, R.C., 1946, “A Functional Calculus of First Order Based on Strict Implication”, *Journal of Symbolic Logic*, 11(1): 1–16.

[^barcan-1947]: –––, 1947, “The Identity of Individuals in a Strict Functional Calculus of Second Order”, *Journal of Symbolic Logic*, 12(1): 12–15.

[^bernays-1976]: Bernays, P., 1976, “On the Problem of Schemata of Infinity in Axiomatic Set Theory”, in *Sets and classes: On the work of Paul Bernays*, Amsterdam: North Holland, pp. 121–172.

[^boolos-1984]: Boolos, G., 1984, “To Be is to Be a Value of a Variable (or to be Some Values of Some Variables)”, *The Journal of Philosophy*, 81: 430–49.

[^boolos-1993]: –––, 1993, “Whence the contradiction?”, *Aristotelian Society Supplementary Volume*, 67: 211–233.

[^burgess-2004]: Burgess, J.P., 2004, “E Pluribus Unum: Plural Logic and Set Theory”, *Philosophia Mathematica* (3), 15(1): 79–93.

[^burgess-2009]: –––, 2009, *Philosophical logic*, Princeton: Princeton University Press.

[^burgess-1997]: Burgess, J.P. & G. Rosen, 1997, *A subject with no object*, New York: Oxford University Press.

[^carnap-1946]: Carnap, R., 1946, “Modalities and Quantification”, *Journal of Symbolic Logic*, 11(2): 33–64.

[^cartwright-1954]: Cartwright, R., 1954, “Ontology and the Theory of Meaning”, *Philosophy of Science*, 21: 316–325.

[^cartwright-1994]: –––, 1994, “Speaking of Everything”, *Noûs*, 28(1): 1–20.

[^dedekind-1893]: Dedekind, R., 1893, *Was sind und was sollen die Zahlen?* Braunshweig: Vieweg. [An English translation, “The Nature and Meaning of Numbers”, is contained in Dedekind (1901)].

[^dedekind-1901]: Dedekind, R., 1901, *Essays on the Theory of Numbers*, Chicago: Open Court.

[^deutsch-1990]: Deutsch, H. 1990, “ Contingency and Modal Logic”, *Philosophical Studies*, 60(1/2): 89–102.

[^dorr-2002]: Dorr, C. & G. Rosen, 2002, “Composition as a Fiction”, in *The Blackwell Companion to Metaphysics*, Oxford: Blackwell.

[^dummett-1991]: Dummett, M., 1991, *Frege: Philosophy of Mathematics*, Cambridge, MA: Harvard University Press.

[^dummett-1993]: –––, 1993, “What is Mathematics about?”, in *The seas of Language*, Oxford: Clarendon Press.

[^dunn-nd]: Dunn, J. M. and N. D. Belnap, “The Substitution Interpretation of the Quantifiers”, *Noûs*, 2(2): 177–185.

[^enderton-2001]: Enderton, H.B., 2001, *A Mathematical Introduction to Logic*, 2ⁿᵈ edition, San Diego: San Diego University Press.

[^fine-1970]: Fine, K., 1970, “Propositional Quantifiers in Modal Logic”, *Theoria*, 36: 336–346.

[^fine-1983]: –––, 1983, “The Permutation Principle in Quantificational Logic”, *Journal of Philosophical Logic*, 12(1): 33–37.

[^fine-1989]: –––, 1989, “The Problem of *de re* Modality”, in J.Perry, J. Almog, & H.K. Wettstein (eds), *Themes from Kaplan*, Oxford: Oxford University Press, pp. 197–272

[^fine-2006]: –––, 2006, “Relatively unrestricted quantification”, in Rayo & Uzquiano 2006: 20–44.

[^florio-2021]: Florio, S. & Ø. Linnebo, 2021, *The Many and the One: A Philosophical Study of Plural Logic*, Oxford: Oxford University Press.

[^frege-1879]: Frege, G., 1879, *Begriffsschrift*, Halle: Louis Nebert.

[^frege-1980a]: –––, 1980a, “Concept and Object”, in P. Geach & M. Black (eds.), *Translations form the Philosophical Writings of Gottlob Frege*, Oxford: Blackwell, pp. 192–205.

[^frege-1980b]: –––, 1980b, *The foundations of arithmetic*, Evanston, IL: Northwestern University Press.

[^glanzberg-2004]: Glanzberg, M., 2004, “Quantification and Realism\*”, *Philosophy and Phenomenological Research*, 69(3): 541–572.

[^gottlieb-1980]: Gottlieb, D., 1980, *Ontological Economy: Substitutional Quantification and Mathematics*, Oxford: Oxford University Press.

[^grover-1972]: Grover, D.L., 1972, “Propositional Quantifiers”, *Journal of Philosophical Logic*, 1(2): 111–136.

[^grover-1992]: –––, 1992, *A Prosentential Theory of Truth*, Princeton: Princeton University Press.

[^grover-1975]: Grover, D.L., J.L. Camp, & N.D. Belnap, 1975, “A Prosentential Theory of Truth”, *Philosophical Studies*, 27(2): 73–125.

[^hand-2007]: Hand, M., 2007, “Objectual and Substitutional Interpretations of the Quantifiers”, in D. Jacquette (ed.), *Philosophy of logic*, Amsterdam: Elsevier.

[^hawthorne-2011]: Hawthorne, J. & G. Uzquiano, 2011, “How Many Angels Can Dance on the Point of a Needle? Transcendental Theology Meets Modal Metaphysics”, *Mind*, 120(477): 53–81.

[^hellman-2006]: Hellman, G., 2006, “Against ‘Absolutely Everything’!”, in Rayo & Uzquiano 2006: 75–97.

[^higginbotham-1998]: Higginbotham, J., 1998, “Higher-Order Logic and Natural Language”, *Proceedings of the British Academy*, 95: 1–27.

[^hilbert-1928]: Hilbert, D. & W. Ackermann, 1928, *Die Grundlagen der theoretischen Logik*, Berlin: Springer.

[^hossack-2000]: Hossack, K., 2000, “Plurals and Complexes”, *British Journal for the Philosophy of Science*, 51(3): 411–443.

[^inwagen-1981]: Inwagen, P. van, 1981, “Why I Don’t Understand Substitutional Quantification”, *Philosophical Studies*, 39(3): 281–285.

[^inwagen-1995]: –––, 1995, *Material Beings*, Ithaca: Cornell University Press.

[^kaplan-1970]: Kaplan, D., 1970, “S5 with Quantifiable Propositional Variables”, *Journal of Symbolic Logic*, 35(2): 355.

[^kaplan-1995]: –––, 1995, “A Problem in Possible-World Semantics”, in Sinott-Armstrong, Raffman, & Asher 1995: 41–52.

[^kreisel-1967]: Kreisel, G., 1967, “Informal Rigour and Completeness Proofs”, in I. Lakatos (ed.), *Problems in the Philosophy of Mathematics*, Amsterdam: North Holland, pp. 138–186.

[^kripke-1959]: Kripke, S., 1959, “A Completeness Theorem in Modal Logic”, *The Journal of Symbolic Logic*, 24(1): 1–14.

[^kripke-1963]: –––, 1963, “Semantical Considerations on Modal Logic”, *Acta Philosophica Fennica*, 16(1963): 83–94.

[^kripke-1965]: –––, 1965, “Semantical Analysis of Intuitionistic Logic I”, in J. N. Crossley & M. A. E. Dummett (eds.), *Formal Systems and Recursive Functions: Proceedings of the Eighth Logic Colloquium, Oxford July 1963*, Amsterdam: North Holland, pp. 92–130.

[^kripke-1976]: –––, 1976, “Is There a Problem About Substitutional Quantification?”, in *Truth and meaning*, Oxford: Oxford University Press, pp. 324–419.

[^kripke-1980]: –––, 1980, *Naming and necessity*, Cambridge, MA: Harvard University Press.

[^lambert-1963]: Lambert, K., 1963, “Existential Import Revisited”, *Notre Dame Journal of Formal Logic*, 4(4): 288–292.

[^lavine-2006]: Lavine, S., 2006, “Something about Everything: Universal Quantification in the Universal Sense of Universal Quantification”, in Rayo & Uzquiano 2006: 98–148.

[^levy-1960]: Levy, A., 1960, “Axiom Schemata of Strong Infinity in Axiomatic Set Theory”, *Pacific Journal of Mathematics*, 10(1): 223–238.

[^lewis-1932]: Lewis, C.I., C.H. Langford, & S.P. Lamprecht, 1932, *Symbolic Logic*, 2nd edition (Volume 5), New York: Dover Publications.

[^lindström-1966]: Lindström, P., 1966, “First Order Predicate Logic with Generalized Quantifiers”, *Theoria*, 32: 186–195.

[^linnebo-2013]: Linnebo, Ø., 2013, “Plural quantification”, *The Stanford Encyclopedia of Philosophy* (Spring 2013), E. N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/spr2013/entries/plural-quant/](https://plato.stanford.edu/archives/spr2013/entries/plural-quant/)>.

[^linsky-1994]: Linsky, B. & E.N. Zalta, 1994, “In Defense of the Simplest Quantified Modal Logic”, *Philosophical Perspectives*, 8: 431–458.

[^marcus-1961]: Marcus, R.B., 1961, *Modalities: Philosophical essays*, Oxford: Oxford University Press.

[^menzel-1991]: Menzel, C., 1991, “The True Modal Logic”, *Journal of Philosophical Logic*, 20(4): 331–374.

[^montague-1966]: Montague, R., 1966, “Fraenkel’s Addition to the Axioms of Zermelo”, in A. A. Fraenkel & Y. Bar-Hillel (eds.), *Essays on the foundations of mathematics*, Jerusalem: Magnes Press Hebrew University.

[^moschovakis-2010]: Moschovakis, J., 2010, “Intuitionistic logic”, in *The Stanford Encyclopedia of Philosophy* (Summer 2010) E. N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/sum2010/entries/logic-intuitionistic/](https://plato.stanford.edu/archives/sum2010/entries/logic-intuitionistic/)>.

[^mostowski-1957]: Mostowski, A., 1957, “On a Generalization of Quantifiers”, *Fundamenta Mathematicae*, 44: 12–36.

[^nelson-2012]: Nelson, M., 2012, “Existence”, *The Stanford Encyclopedia of Philosophy* (Winter 2012), E. N. Zalta (ed.), URL= <[http://plato. stanford.edu/archives/win2012/entries/existence/](https://plato.stanford.edu/archives/win2012/entries/existence/)>.

[^oliver-2001]: Oliver, A. & T. Smiley, 2001, “Strategies for a Logic of Plurals”, *Philosophical Quarterly*, 51: 289–306.

[^parsons-1971]: Parsons, C., 1971, “A Plea for Substitutional Quantification”, *Journal of Philosophy*, 68: 231–237.

[^parsons-2006]: Parsons, C., 2006, “The problem of Absolute Universality”, in Rayo & Uzquiano 2006: 203–19.

[^parsons-1980]: Parsons, T., 1980, *Nonexistent Objects*, New Haven: Yale University Press.

[^peters-2006]: Peters, S. & D. Westerståhl, 2006, *Quantifiers in Language and Logic*, Oxford: Clarendon Press.

[^priest-2005]: Priest, G., 2005, *Towards Non-Being*, Oxford: Clarendon Press.

[^prior-1957]: Prior, A.N., 1957, *Time and Modality*, Oxford: Oxford University Press.

[^prior-1961]: –––, 1961, “On a family of paradoxes”, *Notre Dame Journal of Formal Logic*, 2(1): 16–32. [[Prior 1957 available online](http://projecteuclid.org/euclid.ndjfl/1093956750)]

[^prior-1971]: –––, 1971, *Objects of thought*, P.T. Geach and A.J.P. Kenny (eds.), Oxford: Clarendon Press.

[^quine-1943]: Quine, W.V., 1943, “Notes on Existence and Necessity”, *Journal of Philosophy*, 40(5): 113–127.

[^quine-1948]: –––, 1948, “On What There Is”, *Review of Metaphysics*, 2: 21–38.

[^quine-1953]: –––, 1953, *From a Logical Point of View*, Cambridge, MA: Harvard University Press.

[^quine-1954]: –––, 1954, “Quantification and the Empty Domain”, *Journal of Symbolic Logic*, 19(3): 177–179.

[^quine-1960]: –––, 1960, *Word and Object*, Cambridge, MA: MIT Press.

[^quine-1986]: –––, 1986, *Philosophy of Logic*, Cambridge, MA: Harvard University Press.

[^rayo-1999]: Rayo, A. & G. Uzquiano, 1999, “Toward a Theory of Second-Order Consequence”, *Notre Dame Journal of Formal Logic*, 40(3): 315–325.

[^rayo-2006]: ––– (eds), 2006, *Absolute Generality*, Oxford: Oxford University Press.

[^rayo-2003]: Rayo, A. & T. Williamson, 2003, “A Completeness Theorem for Unrestricted First-Order Languages”, in *Liars and heaps*, Oxford: Oxford University Press.

[^rayo-2001]: Rayo, A. & S. Yablo, 2001, “Nominalism Through De-Nominalization”, *Noûs*, 35(1): 74–92.

[^richard-1996]: Richard, M., 1996, “Propositional Quantification”, *Logic and Reality: Essays on the Legacy of Arthur Prior, Oxford: Oxford University Press*, 437–460.

[^russell-1905]: Russell, B., 1905, “On Denoting”, *Mind*, 14: 479–493.

[^santos-2013]: Santos, G., 2013, “Numbers and Everything”, *Philosophia Mathematica*, 21(3): 297–308.

[^shapiro-1987]: Shapiro, S., 1987, “Principles of Reflection and Second-Order Logic”, *Journal of Philosophical Logic*, 16(3): 309–333.

[^shapiro-1991]: –––, 1991, *Foundations without Foundationalism: A Case for Second-Order Logic*, Oxford: Oxford University Press.

[^sider-2009]: Sider, T., 2009, “Williamson’s Many Necessary Existents”, *Analysis*, 69(2): 250–258.

[^sinott-armstrong-1995]: Sinott-Armstrong, W., D. Raffman, & N. Asher (eds), 1995, *Modality, Morality and Belief: Essays in Honor of Ruth Barcan Marcus*, Cambridge: Cambridge University Press.

[^soames-2014]: Soames, S., 2014, *The Analytic Tradition in Philosophy*, Princeton: Princeton University Press.

[^uzquiano-2004]: Uzquiano, G., 2004, “Plurals and Simples”, *The Monist*, 87(3): 705–725.

[^uzquiano-2021]: –––, 2021, “Elusive Propositions”, *The Journal of Philosophical Logic*, 50(4): 429–451.

[^wiggins-1995]: Wiggins, D., 1995, “The Kant-Frege-Russell View of Existence: Toward the Rehabilitation of the Second-Level View”, in Sinott-Armstrong, Raffman, & Asher 1995: 93–113.

[^williamson-1999]: Williamson, T., 1999, “A Note on Truth, Satisfaction and the Empty Domain”, *Analysis*, 59(1): 3–8.

[^williamson-2003]: –––, 2003, “Everything”, *Philosophical Perspectives*, 17(1): 415–465.

[^williamson-2013]: –––, 2013, *Modal Logic as Metaphysics*, Oxford: Oxford University Press.

[^zalta-1988]: Zalta, E., 1988, *Intensional logic and the Metaphysics of Intentionality*, Cambridge, MA: MIT Press.

[^zermelo-1930]: Zermelo, E., 1930, “Über Grenzzahlen und Mengenbereiche: Neue Untersuchungen über die Grundlagen der Mengenlehre”, *Fundamenta Mathematicae*, 16: 29–47.
