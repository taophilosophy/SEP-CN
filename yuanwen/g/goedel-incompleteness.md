# Gödel’s Incompleteness Theorems
**First published Mon Nov 11, 2013; substantive revision Wed Oct 8, 2025**

*Raatikainen, Panu*

Gödel’s two incompleteness theorems are among the most important results in modern logic, and have deep implications for various issues. They concern the limits of provability in formal axiomatic theories. The first incompleteness theorem states that in any consistent formal system $F$ within which a certain amount of arithmetic can be carried out, there are statements of the language of $F$ which can neither be proved nor disproved in $F$. According to the second incompleteness theorem, such a formal system cannot prove that the system itself is consistent (assuming it is indeed consistent). These results have had a great impact on the philosophy of mathematics and logic. There have been attempts to apply the results also in other areas of philosophy such as the philosophy of mind, but these attempted applications are more controversial. The present entry surveys the two incompleteness theorems and various issues surrounding them. (See also the entry on Kurt Gödel for a discussion of the incompleteness theorems that contextualizes them within a broader discussion of his mathematical and philosophical work.)

## 1. Introduction

### 1.1 Outline

Gödel’s incompleteness theorems are among the most important results in modern logic. These discoveries revolutionized the understanding of mathematics and logic, and had dramatic implications for the philosophy of mathematics. There have also been attempts to apply them in other fields of philosophy, but the legitimacy of many such applications is much more controversial.

In order to understand Gödel’s theorems, one must first explain the key concepts essential to it, such as “formal system”, “consistency”, and “completeness”. Roughly, a *formal system* is a system of axioms equipped with rules of inference, which allow one to generate new theorems. The set of axioms is required to be finite or at least decidable, i.e., there must be an algorithm (an effective method) which enables one to mechanically decide whether a given statement is an axiom or not. If this condition is satisfied, the theory is called “recursively axiomatizable”, or, simply, “axiomatizable”. The rules of inference (of a formal system) are also effective operations, such that it can always be mechanically decided whether one has a legitimate application of a rule of inference at hand. Consequently, it is also possible to decide for any given finite sequence of formulas, whether it constitutes a genuine derivation, or a proof, in the system—given the axioms and the rules of inference of the system.

A formal system is *complete* if for every statement of the language of the system, either the statement or its negation can be derived (i.e., proved) in the system. A formal system is *consistent* if there is no statement such that the statement itself and its negation are both derivable in the system. Only consistent systems are of any interest in this context, for it is an elementary fact of logic that in an inconsistent formal system every statement is derivable, and consequently, such a system is trivially complete.

Gödel established two different though related incompleteness theorems, usually called the first incompleteness theorem and the second incompleteness theorem. “Gödel’s theorem” is sometimes used to refer to the conjunction of these two, but may refer to either—usually the first—separately. Accommodating an improvement due to J. Barkley Rosser in 1936, the first theorem can be stated, roughly, as follows:

**First incompleteness theorem** Any consistent formal system $F$ within which a certain amount of elementary arithmetic can be carried out is incomplete; i.e., there are statements of the language of $F$ which can neither be proved nor disproved in $F$.

Gödel’s theorem does not merely claim that such statements exist: the method of Gödel’s proof explicitly produces a particular sentence that is neither provable nor refutable in $F$; the “undecidable” statement can be found mechanically from a specification of $F$. The sentence in question is a relatively simple statement of number theory, a purely universal arithmetical sentence.

A common misunderstanding is to interpret Gödel’s first theorem as showing that there are truths that cannot be proved. This is, however, incorrect, for the incompleteness theorem does not deal with provability in any absolute sense, but only concerns derivability in some particular formal system or another. For any statement $A$ unprovable in a particular formal system $F$, there are, trivially, other formal systems in which $A$ is provable (take $A$ as an axiom). On the other hand, there is the extremely powerful standard axiom system of Zermelo-Fraenkel set theory (denoted as **ZF**, or, with the axiom of choice, **ZFC**; see the section on the axioms of ZFC in the entry on set theory), which is more than sufficient for the derivation of all ordinary mathematics. Now there are, by Gödel’s first theorem, arithmetical truths that are not provable even in **ZFC**. Proving them would thus require a formal system that incorporates methods going beyond **ZFC**. There is thus a sense in which such truths are not provable using today’s “ordinary” mathematical methods and axioms, nor can they be proved in a way that mathematicians would today regard as unproblematic and conclusive.

Gödel’s second incompleteness theorem concerns the limits of consistency proofs. A rough statement is:

**Second incompleteness theorem** For any consistent system $F$ within which a certain amount of elementary arithmetic can be carried out, the consistency of $F$ cannot be proved in $F$ itself.

In the case of the second theorem, $F$ must contain a little bit more arithmetic than in the case of the first theorem, which holds under very weak conditions. It is important to note that this result, like the first incompleteness theorem, is a theorem about formal provability, or derivability (which is always relative to some formal system; in this case, to $F$ itself). It does not say anything about whether, for a particular theory $T$ satisfying the conditions of the theorem, the statement “$T$ is consistent” can be proved in the sense of being shown to be true by a conclusive argument, or by a proof generally acceptable for mathematicians. For many theories, this is perfectly possible.

### 1.2 Some Formalized Theories

The existence of incomplete theories is hardly surprising. Take any theory, even a complete one (see below for examples), and drop some axiom; unless the axiom is redundant, the resulting system is incomplete. The incompleteness theorems, however, deal with a much more radical kind of incompleteness phenomenon. Unlike the above sort of trivially incomplete theories, which can be easily completed, there is no way of completing the relevant theories; all their extensions, inasmuch as they are still formal systems and hence axiomatizable, are also incomplete. They remain, so to speak, eternally incomplete and can never be completed. They are “essentially incomplete”.

In the first and loose statements of the incompleteness theorems given above, the vague requirement that “a certain amount of elementary arithmetic can be carried out” occurred. It is time to make this more precise.

#### 1.2.1 Arithmetical Theories

The weakest standard system of arithmetic that is usually considered in connection with incompleteness and undecidability is so-called Robinson arithmetic (due to Raphael M. Robinson; see Tarski, Mostowski and Robinson 1953)[^tarski-1953], standardly denoted as **Q**. As axioms, it has the following seven assumptions:

$$\begin{align} \tag{A1} &\neg(0 = x') \\ \tag{A2} &x' = y' \rightarrow x = y \\ \tag{A3} &\neg(x = 0) \rightarrow \exists y(x = y') \\ \tag{A4} &x + 0 = x \\ \tag{A5} &x + y' = (x + y)' \\ \tag{A6} &x \times 0 = 0 \\ \tag{A7} &x \times y' = (x \times y) + x \end{align}$$

The intended interpretation of “$x'$” is the successor function, and obviously, of “+” and “$\times$”, the addition and the multiplication functions, respectively. “0” is the only constant and denotes the number zero.

Adding to these elementary axioms the axiom scheme of induction:

$$\tag{IND} \phi(0) \wedge \forall x[\phi(x) \rightarrow \phi(x')] \rightarrow \forall x\phi(x), $$

results in (first order) Peano Arithmetic (**PA**). Note that unlike **Q**, **PA** contains infinitely many axioms, because all (infinitely many) instances of the induction scheme, one corresponding to every formula $\phi(x)$ (with at least one free variable) of the language, are taken as axioms. But it is a routine mechanical task to check whether a given sentence is an instance of this scheme. **PA** is generally taken as the standard first-order system of arithmetic.

Another natural and much-studied arithmetical system, which lies between **Q** and **PA** in strength, is Primitive Recursive Arithmetic (**PRA**). It contains not just the above axioms of **Q** governing successor, addition and multiplication, but also defining axioms for all primitive recursive functions (see the entry on recursive functions), and the application of the induction scheme is restricted to quantifier-free formulas (i.e., $\phi(x)$ is not allowed to contain any (unbounded) quantifiers).

However, essentially the same system is obtained if one takes just the axioms of **Q** and the induction scheme restricted to, roughly, purely existential formulas (in technical terms, $\Sigma^{0}_1$-formulas; see below) (this was first showed by Parsons 1970)[^parsons-1970]. Moreover, $\Sigma^{0}_1$-induction can be shown (Paris and Kirby 1978)[^paris-1978] to be equivalent to the induction scheme restricted to (roughly) purely universal formulas $(\Pi^{0}_1$-formulas). **PRA** can also be formulated as a “logic-free” equational calculus. **PRA**, or something equivalent to it, is sufficient for developing the theory of syntax for formalized theories. It is often taken as the unproblematic background theory in which various other systems, whose legitimacy may be more controversial, are studied.

A much stronger system than **PA**, important in the foundations of mathematics, which will be mentioned now and then below, is second-order arithmetic **PA$^2$** (also often denoted by **Z$_2$**). It is more than sufficient for developing all ordinary analysis and algebra. Its language is a two-sorted first-order language (see the entry on second-order and higher-order logic), i.e., it contains two sorts of variables, number variables $x_1,x_2,\ldots$ (or $x, y, z, \ldots$) and property variables $X_1, X_2,\ldots$ (or $X, Y, Z,\ldots)$, where properties are extensionally conceived. As axioms it includes, in addition to the basic axioms of **PA**, all instances of the second-order comprehension scheme:

$$ \exists X\forall x[Xx \leftrightarrow \phi(x)] $$

where $\phi(x)$ can be any formula of the language of **PA$^2$** in which $X$ doesn’t occur free. (It should be mentioned that **PA$^2$** can also be formulated by adding the primitive notion of set membership $(\in)$ to the language, regarding the variables $X, Y, Z,\ldots$, as explicitly ranging over sets, and reformulating second-order comprehension as $\exists X\forall x[x \in X \leftrightarrow \phi(x)$].)

**PA$^2$** is a very strong theory. Via the method of interpretations (see below), one can show that it is proof-theoretically as strong as the Zermelo-Fraenkel set theory **ZFC** without the power-set axiom, call it **ZFC–Pow** (whereas the standard, first-order **PA** is similarly proof-theoretically equivalent to **ZFC** without the axiom of infinity, **ZFC–Inf**). (Cf. the section on the axioms of ZFC in the entry on set theory.)

Obviously, it is assumed that our formal systems are also equipped with a system of *rules of inferences* (and possibly some logical axioms), usually some standard system of classical logic (though the incompleteness theorems do not essentially presuppose classical logic, but also apply to systems with, e.g., intuitionistic logic). The above standard systems all come with classical logic. The standard notation $F \vdash A$ is used to express (in the meta-level) that $A$ is derivable in $F$, that is, that there is a proof of $A$ in $F$, or, in other words, that $A$ is a *theorem* of $F$. Accordingly, $F \not\vdash A$ means that $A$ is *not* derivable in $F$.

To summarize: when it is said, in the context of the incompleteness theorems, that “a certain amount of elementary arithmetic can be carried out” in a system, this usually means that it contains **PRA** or at least **Q**. For the first incompleteness theorem, **Q** is sufficient; for the standard proofs of the second theorem, something like **PRA**, at a minimum, is needed. There is a version of the second incompleteness theorem for **Q** (see Bezboruah & Shepherdson 1976)[^bezboruah-1976] but there has been some debate on whether the relevant statement in **Q** can really be taken to express consistency, **Q** being so weak (see Kreisel 1958; Bezboruah & Shepherdson 1976; Pudlák 1996; Franks 2009)[^bezboruah-1976][^franks-2009][^kreisel-1958][^pudlák-1996].

#### 1.2.2 Theories not Formulated in the Language of Arithmetic

Of course, there are many important and interesting theories in mathematics which are not even formulated in the language of arithmetic. However, the applicability of the incompleteness theorems can be dramatically extended outside the language of first-order arithmetic and its extensions, when it is noted that all that is needed is that weak theories such as **Q**, or **PRA**, can be *interpreted* in the system in question. Most importantly, this involves various systems of set theory. For example, the incompleteness theorems hold for **ZFC–Inf** (i.e., **ZFC** without the axiom of infinity) and all its extensions, however strong (as long as they are axiomatizable.)

Roughly, a theory $T_1$ is interpretable in another theory $T_2$ if the primitive concepts and the range of the variables of $T_1$ are definable in $T_2$ so that it is possible to translate every theorem of $T_1$ into a theorem of $T_2$. One should not misunderstand such interpretations as providing anything like intuitive synonymity. Two theories may have radically different intended subject matter and yet, as formal systems, one may be interpretable in another. (As an illustration: a simple theory of ancestors may be, taken as a formal system, interpreted in arithmetic; obviously this does not mean that grandmothers and such are really numbers.) What is significant is that interpretability preserves certain elementary *formal* properties of theories, most importantly, consistency: if $T_1$ is interpretable in $T_2$ and $T_2$ is consistent, $T_1$ is also consistent. And any system in which **Q** can be interpreted is guaranteed to be essentially incomplete. For any such theory in which **Q** is interpretable, the incompleteness could be proved also directly; for example, in various theories of set theory, one can code formulas and derivations (instead of numbers) by sets, “Gödel sets”, and proceed then as usual (see, e.g., Fitting 2007)[^fitting-2007]. However, for most purposes, it is just much simpler to establish the interpretability of **Q** in the theory at issue.

In sum, when it is said that “a certain amount of elementary arithmetic can be carried out within a system”, what is meant is either that the system is an axiomatizable extension of **Q**, or that **Q** can be interpreted in it. (In the case of (the standard proofs of) the second incompleteness theorem, substitute **PRA** for **Q**.)

#### 1.2.3 Some Exceptions: Complete Theories

On the other hand, not all theories of arithmetic are incomplete. The theory of only addition of natural numbers but without multiplication (often called “Presburger arithmetic”), for example, is complete (and decidable) (Presburger 1929)[^presburger-1929], as is the theory of multiplication of the positive integers (Skolem 1930)[^skolem-1930]. These theories are, though, very weak. But in any case, at least a theory which deals with both addition and multiplication is needed. More interestingly, the natural first-order theory of arithmetic of *real numbers* (with both addition and multiplication), the so-called theory of real closed fields $(\mathbf{RCF})$, is both complete and decidable, as was shown by Tarski (1948)[^tarski-1948]; he also demonstrated that the first-order theory of Euclidean geometry is complete and decidable. Thus, one should keep in mind that there are some non-trivial and interesting theories to which Gödel’s theorems do not apply.

### 1.3 The Relevance of the Church-Turing Thesis

Gödel originally only established the incompleteness of a particular though very comprehensive formalized theory **P**, a variant of Russell’s type-theoretical system **PM** (for *Principia Mathematica*, see the sections on Paradoxes and Russell’s Type Theories in the entries on type theory and *Principia Mathematica*), and all extension of **P** with the same language, whose set of axioms is primitive recursive. He also suggested, though did not demonstrate, that the proof could be adapted to apply also to the standard axiom systems of set theory such as **ZFC**. Though it turns out that Gödel in fact already had a very general result, it was, at the time, unclear just how general this really was (see also Section 5).

What was still missing was an analysis of the intuitive notion of decidability, needed in the characterization of the notion of an arbitrary formal system. Recall that the set of axioms and the proof relation of a formalized system are required to be decidable. Mathematicians and logicians have implicitly used the intuitive notion of a decision method since antiquity, and as long as one asked for a positive solution, it was sufficient that one presented a concrete method that intuitively striked everyone as a mechanical method. For the general limitative results, such as the general incompleteness theorems, or the undecidability results (see 4.2), however, a precise mathematical explication of the notion would be needed. Instead of decidable sets or properties, one often considers effective or computable functions or operations, but in fact these are just two sides of the same coin—talk of one can be easily transcribed to talk of another.

Gödel (1934)[^gödel-1934], Alonzo Church (1936a, b) and Alan Turing (1936–7) came up independently with different proposals for an exact mathematical definition of computable functions, and consequently, of decidable sets (of numbers). These proposals, though, all turned out to be equivalent. Turing’s careful conceptual analysis which used fictional and abstract computing machines (nowadays conventionally called “Turing machines”; see the entry on Turing machines) was particularly important, as Gödel himself emphasized (see, e.g., Gödel 1963)[^gödel-1963]. The equation of the intuitive notion and some of these mathematical explications is often called “The Church-Turing-thesis”. The label “recursive function” has, for historical reasons, been dominant in the logical literature. Consequently, decidable sets are often called “recursive sets”. (See the entries on computability, recursive functions and the Church-Turing thesis.)

For a proper understanding of the incompleteness and undecidability results, it is vital to understand the difference between the two key notions regarding sets. First, there may be a mechanical method which decides whether any given number belongs to the set at issue or not (in which case the set is called “decidable” or “recursive”), and, second, there may be a mechanical method which generates or lists the elements of the set, number by number. In the latter case, the set is called “recursively enumerable” (r.e.), that is to say, it can be effectively generated, or it is “semi-decidable.” It is a fundamental result of the theory of computability (or “the theory of recursive functions”) that there are semi-decidable sets, sets which can be effectively generated (i.e., are recursively enumerable), but are *not* decidable (i.e., not recursive). In fact, this is, in the very abstract level, the essence of the first incompleteness theorem. However, if both a set and its complement are recursively enumerable, the set is recursive, i.e., decidable.

## 2. The First Incompleteness Theorem

In this section, the main lines of the proof of the first incompleteness theorem are sketched. A reader interested in more details can consult the supplementary documents ([Gödel Numbering](goedel-incompleteness.sup1.md) and [The Diagonalization Lemma](goedel-incompleteness.sup2.md)).

### 2.1 Preliminaries

The formal term (“numeral”) canonically denoting the natural number $\boldsymbol{n}$ is abbreviated as $\overline{n}$. In the standard language of arithmetic used here, the number $\boldsymbol{n}$ is denoted by the term $0^{\prime\cdots\prime}$, where the successor symbol ‘$'$’ is iterated $n$ times. That is, numerals which name 1, 2, 3, … are $0', 0'', 0''',\ldots$ and are abbreviated by $\overline{1}$, $\overline{2}$, $\overline{3}$, …

In his original proof, Gödel used his specific notion of *ω*-consistency, and for some purposes, it is still convenient to follow Gödel’s original approach. A formalized theory $F$ is *ω*-*consistent* if it is *not* the case that for some formula $A(x)$, both $F \vdash \neg A(\overline{n})$ for all $\boldsymbol{n}$, *and* $F \vdash \exists xA(x)$. Naturally this implies normal consistency, and follows from the assumption that the natural numbers satisfy the axioms of $F$.

Actually, a simple special case of *ω*-consistency suffices here; namely, the assumption is only needed with respect to what logicians call $\Sigma^{0}_1$-formulas; these are, roughly, the purely existential formulas; more exactly, formulas of the form $\exists x_1\exists x_2 \ldots \exists x_n A$, where $A$ does not contain any unbounded quantifiers ($A$ may contain bounded universal quantifiers $\forall x \lt t$ and bounded existential quantifiers $\exists x \lt t)$. This restricted *ω*-consistency is called 1-consistency.

*ω*-consistency and 1-consistency are purely syntactic notions. If the use of the notions of truth and falsity is allowed, the assumption of 1-consistency can be expressed intuitively simply as the requirement that the formal system in question does not prove any false $\Sigma^{0}_1$-sentences (i.e., the system is *sound* at least in the case of such sentences). From now on, it is assumed that the formalized systems under consideration contain **Q** and are assumed to be at least 1-consistent, unless otherwise stated.

### 2.2 Representability

Gödel’s proof also requires the notion of representability of sets and relations in a formal system $F$. More precisely, two related notion are needed.

A set $S$ of natural numbers is ***strongly representable*** in $F$ if there is a formula $A(x)$ of the language of $F$ with one free variable $x$ such that for every natural number $\boldsymbol{n}$:

$$\begin{align} \boldsymbol{n} \in S &\Rightarrow F \vdash A(\overline{n}); \\ \boldsymbol{n} \not\in S &\Rightarrow F \vdash \neg A(\overline{n}), \end{align}$$

A set $S$ of natural numbers is ***weakly representable*** in $F$ if there is a formula $A(x)$ of the language of $F$ such that for every natural number $\boldsymbol{n}$:

$$ \boldsymbol{n} \in S \Leftrightarrow F \vdash A(\overline{n}). $$

It is obvious how all these notions are generalized to many-place relations. There are also related notions of representability for functions. As the incompleteness results in particular teach us, there are sets which are only weakly but not strongly representable (the key example being the set of statements provable in the system).

[**Warning:** Here the terminology in the literature varies a lot: “strongly represent” is sometimes called, e.g., “represent”, “numeralwise express”, “bi-numerate”, “define” or “strongly define”; “weakly represent” is in turn also expressed, e.g., by “represent”, “define”, “weakly define”, or “numerate”. One should be careful here and focus on the relevant definitions, and not let the words mislead.]

In the case of both kinds of representability (weak and strong), there is always a simple existential $\Sigma^{0}_1$-formula, which (weakly or strongly) represents the set in question, and usually such a formula is used to represent $S$.

Though these notions are relative to the formal system, it has turned out that strong and weak representability are extremely stable. Quite independently of the particular formal system chosen, exactly the decidable, or recursive, sets (relations) are strongly representable, and exactly the semi-decidable, or recursively enumerable sets (relations) are weakly representable. This holds for all formalized systems which contain Robinson arithmetic **Q**, from Robinson arithmetic itself to the strongest axioms systems of set theory like **ZFC** and beyond (as long as they are (recursively) axiomatizable). Instead of using the notion of “representability”, Gödel took a different approach by speaking of sets being “decidable in a formal system $F$” (*“entscheidungsdefinit”*). If the proofs of $F$ are systematically generated, it will be eventually determined, for any given number $\boldsymbol{n}$, whether it belongs to $S$ or not—given that $S$ is strongly representable in $F$.

In sum, we have:

**The Representability Theorem** In any consistent formal system which contains **Q**:

1. A set (or relation) is strongly representable if and only if it is recursive;
2. A set (or relation) is weakly representable if and only if it is recursively enumerable.

Both notions of representability—strong and weak—must be clearly distinguished from mere *definability* (in the standard sense of the word). A set $S$ is *definable* in the language of arithmetic if there is a formula $A(x)$ in the language such that $A(\overline{n})$ is true in the standard structure of natural numbers (the intended interpretation) if and only if $\boldsymbol{n} \in S.$ There are many sets which can be defined in the language of arithmetic but not (even weakly) represented in any $F$, such as the set of the Gödel numbers of consistent formulas, of sentences unprovable in the system $F$, or of the Diophantine equations with no solutions (see below).

### 2.3 Arithmetization of the Formal Language

The next essential step of Gödel’s proof is to take the language of a formal system, which is always precisely defined (this is part of being a formal system), and fix a correspondence of a certain kind between the expressions of that language and the system of natural numbers—a coding, “arithmetization”, or “Gödel numbering”, of the language. There are many possible ways of accomplishing this, and the details do not really matter (for some more details of one quite standard approach, see the supplementary document [Gödel Numbering](goedel-incompleteness.sup1.md)). The essential point is that the chosen mapping is effective: it is always possible to pass, purely mechanically, from an expression to its code number, and from a number to the corresponding expression. Today, when most of us are familiar with computers and the fact that so many things can be coded by zeros and ones, the possibility of such an arithmetization is hardly surprising.

Roughly, one proceeds as follows: First, the primitive symbols of the language are paired with distinct natural numbers, “symbol numbers”. A little number theory then suffices to code *sequences* of numbers by single numbers. Consequently, well-formed formulas, as sequences of primitive symbols, are each assigned a unique number. Finally derivations, or proofs, of the system, being sequences of formulas, are arithmetized, and are also assigned specific numbers. Such a code, the “Gödel number” of a formula $A$, is denoted as $\ulcorner A\urcorner$, and similarly for derivations.

In this way, syntactical properties, relations and operations are reflected in arithmetic: for example, $\textit{neg}(x)$ is the arithmetical function that sends the Gödel number of a formula to the Gödel number of its negation; in other words, $\textit{neg}(\ulcorner A\urcorner) = (\ulcorner \neg A\urcorner)$; similarly, $\impl(x, y)$ is the function which maps the Gödel numbers of a pair of formulas to the Gödel number of the implication of the formulas: $\impl(\ulcorner A\urcorner ,\ulcorner B\urcorner) = \ulcorner A \rightarrow B\urcorner$; and so on. There is an arithmetical formula, call it $\textit{Fmla}(x)$, which is true of $\boldsymbol{n}$ iff $\boldsymbol{n}$ is a Gödel number of a well-formed formula of the system. There is also an arithmetical formula $M(x,y,z)$ which is true exactly if one has a valid application of the rule of inference *modus ponens* for some formulas $A$ and $B$ with $x = \ulcorner A\urcorner$, $y = \ulcorner A \rightarrow B\urcorner$ and $z = \ulcorner B\urcorner$; etc. In this way, all the syntactic properties and operations can be simulated at the level of numbers, and moreover they are strongly representable in all theories which contain **Q**.

As it is decidable (by the definition of formal systems) whether a given sequence of formulas constitutes a proof of a given sentence, according to the rules of the chosen formal system $F$, the binary relation “$x$ is (the Gödel number of) a proof of the formula (with the Gödel number) $y$” can be strongly represented in all systems containing **Q**, and thus in $F$ in particular. Let us denote the formula which strongly represents this relation in $F$ itself as $\Prf_F (x, y)$. The property of being provable in $F$ can then be defined as $\exists x\Prf_F (x, y)$. Let us abbreviate this formalized *provability predicate* as $\Prov_F (x)$. It follows that the latter property is weakly representable (though, it turns out, not strongly):

$$ F \vdash A \Rightarrow F \vdash\Prov_F (\ulcorner A\urcorner). $$

It is always possible to choose the provability predicate $\Prov_F (x)$ to be a $\Sigma^{0}_1$-formula.

### 2.4 Diagonalization, or, “Self-reference”

The next and perhaps somewhat surprising ingredient of Gödel’s proof is the following important lemma (we still assume that $F$ is a formal system which contains **Q**):

**The Diagonalization Lemma**

Let $A(x)$ be an arbitrary formula of the language of $F$ with only one free variable. Then a sentence $D$ can be mechanically constructed such that

$$ F \vdash D \leftrightarrow A(\ulcorner D\urcorner). $$

(For a sketch of the proof; see the supplementary document [The Diagonalization Lemma](goedel-incompleteness.sup2.md))

In the literature, this lemma is sometimes also called “the self-referential lemma” or “the fixed point lemma”. It has many important applications beyond the incompleteness theorems. Such a sentence is also often called a fixed point (in $F$) of the predicate $A(x).$

It is often said that given a property denoted by $A(x)$, the sentence $D$ is a self-referential sentence which “says of itself” that it has the property $A$. Such figures of speech may be heuristically useful, but they are also easily misleading and suggest too much. For example, note that the lemma only provides a (provable) material equivalence between $D$ and $A(\ulcorner D\urcorner)$ (which states that both sides must have the same truth-value) and does not claim any sort of sameness of meaning. In particular, $D$ and $A(\ulcorner D\urcorner)$ are by no means identical—and neither are $\ulcorner D\urcorner$ and $\ulcorner A(\ulcorner D\urcorner)\urcorner$.

### 2.5 The First Incompleteness Theorem—Proof Completed

To complete the proof, the Diagonalization Lemma is applied to the negated provability predicate $\neg\Prov_F (x)$: this gives a sentence $G_F$ such that

$$\tag{G} F \vdash G_F \leftrightarrow \neg\Prov_F (\ulcorner G_F\urcorner). $$

Thus, it can be shown, even inside $F$, that $G_F$ is true if and only if it is not provable in $F$.

It is not difficult to show that $G_F$ is neither provable nor disprovable in $F$, if $F$ only is 1-consistent.

For the first half, assume that $G_F$ were provable. Then, by the weak representability of *provability-in-*$F$ *by* $\Prov_F(x)$, $F$ would also prove $\Prov_F (\ulcorner G_F\urcorner)$. However, because $F$ in fact also proves the equivalence (G), i.e, $F \vdash G_F \leftrightarrow \neg\Prov_F (\ulcorner G_F\urcorner)$, $F$ would then prove $\neg G_F$ too. But this would mean that $F$ is inconsistent. In sum, if $F$ is consistent, then $G_F$ is not provable in $F$. For this first half, the assumption of the simple consistency of $F$ suffices.

For the second half, it has to be assumed that $F$ is 1-consistent (if $\Prov_F (\ulcorner G_F\urcorner)$ has been chosen such that it is a $\Sigma^{0}_1$-sentence; otherwise, the more general assumption of *ω*-consistency is needed).

Assume that $F \vdash \neg G_F$. Then $F$ cannot prove $G_F$, for otherwise $F$ would be simply inconsistent. Hence no natural number $\boldsymbol{n}$ is the Gödel number of a proof of $G_F$, and because the proof relation is strongly representable, for all $\boldsymbol{n}$, $F \vdash \neg\Prf_F (\overline{n}, \ulcorner G_F\urcorner)$. If also $F \vdash \exists x\Prf_F (x, \ulcorner G_F\urcorner)$, $F$ is not 1-consistent, against the assumption. Therefore $F$ does not prove $\exists x\Prf_F (x, \ulcorner G_F\urcorner)$, in other words, by the definition of $\Prov_F (x), F$ does not prove $\Prov_F (\ulcorner G_F\urcorner)$. By the key equivalence (G), $F$ also does not prove $\neg G_F$.

**Gödel’s First Incompleteness Theorem**

Assume $F$ is a formalized system which contains Robinson arithmetic **Q**. Then a sentence $G_F$ of the language of $F$ can be mechanically constructed from $F$ such that:

1. If $F$ is consistent, then $F \not\vdash G_F$.
2. If $F$ is 1-consistent, then $F \not\vdash \neg G_F$

Such an independent, or “undecidable” (that is, neither provable nor refutable in $F)$ statement $G_F$ in $F$ is often called “the Gödel sentence” of $F$.

In fact, in favourable circumstances, it can be shown that $G_F$ is true, provided that $F$ is indeed consistent. This is the case if, for example, the provability predicate $\Prov_F (x)$ has been chosen as a $\Sigma^{0}_1$-formula: The Gödel sentence is then provably equivalent to the universal formula $\forall x\neg\Prf_F (x, \ulcorner G_F\urcorner)$. Such formulas can be proved false whenever they in fact are false: if false, there would be a number $\boldsymbol{n}$ such that $F \vdash\Prf_F (\overline{n}, \ulcorner G_F\urcorner)$ (this holds already in **Q**). This, however, would contradict the incompleteness theorem. Therefore, $G_F$ cannot be false, and must be true. For this reason, the Gödel sentence is often called “true but unprovable”.

One should not get confused here: “Gödel’s theorem” is the general incompleteness result of Gödel which concerns a large class of formal systems, while the “Gödel sentence” is the constructed, formally undecidable sentence which varies from one formal system to another. This is why it is important to include the subscript $F$ in $G_F$. Furthermore, one should not confuse the two different senses of “undecidable” in this context. On the one hand, *a particular sentence*, like the Gödel sentence, may be undecidable in the sense of being independent, i.e., neither provable not refutable in a chosen system. On the other hand, *a theory* may be undecidable (see below) in the sense that there does not exist a decision method for determining of an arbitrary given sentence of the language whether or not it is derivable in the theory (so this latter sense of “undecidable” concerns, so to speak, an infinite class of statements).

In informal explanations of the first incompleteness theorem, it is often said that the Gödel sentence $G_F$ “says of itself that it is not provable”. Such imprecise statements, however, should be taken at least with a grain of salt. There are a number of reasons to conclude that, at least in general, Gödel sentences do not really say anything substantial about themselves (Milne 2007 is a careful analysis of such issues)[^milne-2007]; for example, as was previously noted in the case of the Diagonalization Lemma, one is usually operating here with mere material equivalences.

#### Rosser’s Improvement—From *ω*-consistency to Consistency

In 1936, J. Barkley Rosser made an important improvement that allows one to get rid of the somewhat clumsy assumption of *ω*-consistency in the proof of Gödel’s *first* theorem. For this purpose, Rosser introduced a new, somewhat artificial “provability predicate” $\Prov^*(x)$ which was constructed, informally, as follows:

There *exists* $y$ such that $y$ is the Gödel number of a proof of the formula with Gödel number $x$, AND *there does not exist* $z$ smaller than $y$ such that $z$ is the Gödel number of a proof the negation of the formula with Gödel number $x$.

More formally:

$$ \Prov^*(x) =_{\textit{def}} \exists y[\Prf_F (y, x) \wedge \forall z \lt y(\neg\Prf_F (z, \textit{neg}(x)))], $$

where $\Prf_F (y, x)$ is the more standard proof relation discussed earlier.

As it happens, if the formal system $F$ under consideration is indeed consistent, Rosser’s provability predicate is co-extensional with the ordinary provability predicate. Applying the Diagonalization Lemma to the negation of Rosser’s provability predicate $\Prov^*(x)$ gives:

**Rosser’s modification of the first theorem (Rosser 1936)[^rosser-1936]** Let $F$ be consistent formalized system which contains **Q**. Then there is a sentence $R_F$ of the language of $F$ such that neither $R_F$ nor $\neg R_F$ is provable in $F$.

### 2.6 Incompleteness and Non-standard Models

It is illuminating to reflect on the first incompleteness theorem also from the model theoretic perspective—though the theorem itself does not in any way require this. Namely, it is possible to conclude that any theory $F$ satisfying the conditions of the theorem must possess, in addition to the intended interpretation or “standard model” (in the case of arithmetical theories, the structure of natural numbers), non-intended interpretations or “non-standard models”—that no such theory can rule out the latter and fix uniquely the intended interpretation. Namely, if there are independent statements such as $G_F, F$ must have both models which satisfy $G_F$ and models which rather satisfy $\neg G_F$. As $\neg G_F$ is equivalent to $\exists x\Prf_F (x, \ulcorner G_F\urcorner)$, the latter models must possess entities which satisfy the formula $\Prf_F (x, \ulcorner G_F\urcorner)$. And yet we know (because $\Prf_F (x, y)$ strongly represents the proof relation) that for any numeral $\overline{n}, F$ can prove $\neg\Prf_F (\overline{n}, \ulcorner G_F\urcorner)$. Therefore, no natural number $\boldsymbol{n}$ can witness the formula. It follows that any such non-standard model must contain, in addition to natural numbers (denotations of the numerals $\overline{n})$, “infinite” non-natural numbers after the natural numbers.

The study of non-standard models did not start with Gödel’s results—Skolem, in particular, was already aware of them earlier in a different context (he had discovered that first-order theories of set theory have unnaturally small, namely, countable models, in Skolem 1922; cf. the entry on Skolem’s paradox)—but the first incompleteness theorem elucidates the existence of non-standard models in the context of arithmetic, while the nonstandard models elucidate the first incompleteness theorem. Non-standard models have since then become a rich research area in mathematical logic (see, e.g., Boolos & Jeffrey 1989: Ch. 17; Kaye 1991)[^boolos-1989][^kaye-1991].

## 3. The Second Incompleteness Theorem

### 3.1 Preliminaries

Informally, the reasoning leading to the second incompleteness theorem is relatively simple. Given the arithmetized provability predicate, it is also easy to present an arithmetized consistency statement: pick some manifestly inconsistent formula (in arithmetical theories, a standard choice is $(\overline{0} = \overline{1})$); let us denote it by $\bot$; (the arithmetized counterpart of) the consistency of the system can then be defined as $\neg\Prov_F (\ulcorner \bot \urcorner)$. Let us abbreviate this formula by $\Cons(F)$. The proof of the first part of the first incompleteness theorem (i.e., the case (i) above) can then presumably be formalized *inside* $F$ (in practice this would certainly be intricate). This gives:

$$ F \vdash \Cons(F) \rightarrow G_F, $$

where $G_F$ is the Gödel sentence for $F$ provided by the first theorem. If $\Cons(F)$ were provable in $F$, so would be $G_F$, by simple logic. This would contradict Gödel’s first theorem. Consequently, $\Cons(F)$ cannot be provable in $F$ either.

**Gödel’s second incompleteness theorem** Assume $F$ is a consistent formalized system which contains elementary arithmetic. Then $F \not\vdash\Cons(F)$.

There is a question of philosophical importance that should be mentioned here: As it stands, Gödel’s second incompleteness theorem only establishes the unprovability of *one* sentence, $\Cons(F)$. But does this sentence really express that $F$ is consistent? (Compare this with the remark above that $G_F$ does not, strictly speaking, express its own unprovability.) Furthermore, might there not be *other* sentences which are provable and also express the consistency of $F$?

Giving a rigorous proof of the second theorem in a more general form that covers all such sentences, however, has turned out to be very complicated. The basic reason for this is that, unlike in the first theorem, not just any, merely extensionally adequate provability predicate works for the formalization of the consistency claim. The manner of presentation makes all the difference. For example, Rosser’s provability predicate mentioned above would not do; one can prove the “consistency” of $F$ in $F$, if consistency is expressed in terms of Rosser’s provability predicate. One must thus add some further conditions for the provability predicate in order for the proof of the second incompleteness theorem to go through. Following Feferman (1960)[^feferman-1960], it is customary to say that whereas the first theorem and its relatives are *extensional* results, the second theorem is *intensional*: it must be possible to think that $\Cons(F)$ in some sense *expresses* the consistency of $F$—that it really *means* that $F$ is consistent.

### 3.2 Derivability Conditions

The proof of the second incompleteness theorem requires that the provability predicate in $F$ satisfies a number of conditions which are used in the details of the proof. There are several different sets of conditions that will do.

The first detailed proof of the second incompleteness theorem appeared in (Hilbert & Bernays 1939)[^hilbert-1939] (mainly written by Bernays), though only for one specific theory, **PA**. It uses a rather awkward set of conditions for the provability predicate. These were more technical lemmas for the needs of a particular proof and not any sort of analysis of “natural” provability predicates. A much more elegant, now standard list of “derivability conditions” was presented by Löb (1955)[^löb-1955]—though their intended use was somewhat different (see below).

**Löb’s Derivability Conditions** $$\begin{align} \tag{D1} F &\vdash A \Rightarrow F \vdash\Prov_F (\ulcorner A\urcorner). \\ \tag{D2} F &\vdash\Prov_F (\ulcorner A\urcorner) \rightarrow\Prov_F (\ulcorner\Prov_F (\ulcorner A\urcorner)\urcorner). \\ \tag{D3} F &\vdash\Prov_F (\ulcorner A\urcorner) \wedge\Prov_F (\ulcorner A \rightarrow B\urcorner) \rightarrow\Prov_F (\ulcorner B\urcorner). \end{align}$$

(D1) is simply a restatement of the requirement from the proof of the first theorem that provability is weakly representable. Roughly put, (D2) requires that the whole demonstration of (D1), for the candidate provability predicate $\Prov_F$, can itself be formalized inside $F$. Finally, (D3) requires that the provability predicate is closed under Modus Ponens.

If the arithmetized provability predicate indeed satisfies these conditions, the second theorem can be proved. Let $G_F$ once again be the Gödel sentence for $F$ given by the first theorem. It is not too difficult to show, using the derivability conditions, that:

$$ F \vdash G_F \leftrightarrow \Cons(F). $$

This immediately yields the unprovability of $\Cons(F)$, given the first incompleteness theorem.

Furthermore, Jeroslow (1973)[^jeroslow-1973] demonstrated, with an ingenious trick, that it is in fact possible to establish the second theorem without (D3). However, in some other cases (e.g., when proving Löb’s theorem; see below), and in Provability Logic, all three conditions are still needed.

### 3.3 Feferman’s Alternative Approach to the Second Theorem

Under the assumption that a provability predicate for a theory satisfies the derivability conditions (or, by Jeroslow’s trick, at least D1 and D2) it is relatively easy to prove the relevant case of the second incompleteness theorem. However, in practise one has to establish whether a proposed arithmetized provability predicate really satisfies the conditions case by case, and typically this is long and tedious.

This drawback, among other things (see Feferman 1997)[^feferman-1997], led Solomon Feferman in the late 1950s to look for an alternative line of attack to the second theorem (see Feferman 1960)[^feferman-1960]. Feferman approaches the issue in two steps: First, he isolates the formulas $\Prov_{FOL}(x)$ which arithmetize some standard notion of derivability in *first-order logic* in order to allow us to fix one chosen formula for provability in logic. How the set of non-logical axioms of the system at issue are presented is left open at this stage. Secondly, Feferman looks for a suitable constraint for presenting the axioms. Among the formulas of the language of arithmetic, he isolates what he calls PR- and RE-formulas; the former correspond to the canonical primitive recursive (PR) definitions in arithmetic, and the latter to existential generalizations of the former. Every recursively enumerable (RE) set can be defined by a formula of the latter sort; these are just the $\Sigma^{0}_1$-formulas. These two classes are easy to discriminate purely by their syntactical form. (In fact, by the MRDP Theorem (see below), one could—instead of RE-formulas—focus on even simpler class of existentially quantified Diophantine equations.)

We have above noted the important fact that in all arithmetical theories $F$ containing **Q**, a set is strongly representable in $F$ if and only if it is recursive, and a set is recursively enumerable if and only if it is weakly representable. Furthermore, one can always take the formula weakly or strongly representing the set to be a RE-formula (i.e., $\Sigma^{0}_1$-formula; and, by MRDP Theorem, even an existentially quantified Diophantine equation). It is then natural to require that the set of non-logical axioms of the system at issue is represented by such a formula. If the arithmetized definition of the set of Gödel numbers of axioms reflects how the axioms, if infinite, are inductively defined, the resulting formula will be $\Sigma^{0}_1$. (For theories which are axiomatizable with finitely many axioms, there is a unique representation of the axioms in the form of a list, and consequently, a unique consistency statement relative to $\Prov_{FOL}(x)$.) In contrast to determining whether the derivability conditions are satisfied, it is a relatively routine task to determine that a given formula which formalizes the axioms is indeed of the required form ($\Sigma^{0}_1$).

Now the version of the second incompleteness theorem presented in Feferman 1960 is:

**A variant of second incompleteness theorem (Feferman 1960)[^feferman-1960]** Let $F$ be a consistent extension of **PA**, and let $Ax_F (x)$ be a $\Sigma^{0}_1$-formula which weakly represents the axioms of $F$, and $\Cons(F)$ be a consistency statement constructed from $Ax_F (x)$ and $\Prov_{FOL}(x)$. Then $\Cons(F)$ is not provable in $F$.

For still different approaches to the second incompleteness theorem, see Feferman 1982, 1989a; Visser 2011. For some philosophical complications concerning the second theorem, see Detlefsen 1979, 1986, 1990, 2001; Auerbach 1985, 1992; Roeper 2003; Franks 2009 (see also section on incompleteness in the entry on Hilbert’s program).

## 4. Results Related to the Incompleteness Theorems

### 4.1 Tarski’s Theorem on the Undefinability of Truth

Gödel first arrived at the incompleteness results (see Section 5 below) by noting that truth (of the language of a system) must be undefinable in the system, a result conventionally credited to Tarski (there are certain real virtues in Tarski’s way of presenting the issue; see Gómez Torrente 2004)[^gómez-2004]. Let us now view the result in the context of Tarski’s approach to truth.

Tarski clearly distinguished the object language, i.e., the language the truth of whose sentences is at stake, and the metalanguage in which the former is discussed. He also required (see the entry on Tarski’s truth definitions) that any satisfactory definition of truth $\True(x)$ for the object language should satisfy his “Convention T”, that is, it should have as its consequence all equivalences (“T-equivalences”) of the form

$$\tag{T} \True(\ulcorner A\urcorner) \leftrightarrow B, $$

where $\ulcorner A\urcorner$ is a name of a sentence of the object language, and $B$ its translation in the metalanguage. If the metalanguage is identical with the object language, or is an extension of the object language, $B$ is simply $A$ *itself*, and the T-equivalences are of the form:

$$ \True(\ulcorner A\urcorner) \leftrightarrow A. $$

What the undefinability theorem shows is that the object language and the metalanguage cannot coincide, but must be distinct.

**Tarski’s Undefinability Theorem** Let $F$ be a consistent formalized system that contains a sufficient amount of arithmetic. Then there is no formula $Tr(x)$ in the language of $F$ such that for every sentence $A$ of the language of $F$:

$$ F \vdash Tr(\ulcorner A\urcorner) \leftrightarrow A. $$

**The idea of the proof:** If there were such a formula of the language of $F$, an easy application of the Diagonalization Lemma to its negation would result in the paradoxical sentence $L$ (for “Liar”; see the Liar paradox), such that:

$$ F \vdash \neg Tr(\ulcorner L\urcorner) \leftrightarrow L, $$

which, together with the T-equivalences, which were assumed to be derivable, would quickly give an explicit contradiction, thus contradicting the assumption that $F$ is consistent.

Similarly, it can be proved that the set of true sentences of $F$ is not definable in the intended interpretation of $F$—in the now standard sense of “definability” (see above).

### 4.2 The Undecidability Results

The tools used in proving Gödel’s theorems also provide various important undecidability results. A theory is called *decidable* if the set of its theorems (sentences derivable in it) is decidable, that is (by the Church-Turing thesis) recursive. Otherwise, the theory is undecidable. Informally, being decidable means that there is a mechanical procedure which enables one to decide whether an arbitrary given sentence (of the language of the theory) is a theorem or not.

If a theory is complete, it is decidable (proof sketch: given a sentence $A$, systematically generate the theorems of the theory; by completeness, eventually either $A$ or $\neg A$ will be produced in a finite time). The converse, though, does not always hold: there are incomplete theories which are decidable. Nevertheless, incompleteness at least opens the possibility of undecidability. Moreover, all theories which contain Robinson arithmetic **Q** (either directly, or **Q** can be interpreted in them) are both incomplete and undecidable. Thus, for a very wide class of theories, incompleteness and undecidability go hand in hand.

One elegant and simple way of demonstrating the undecidability of extensions of **Q** goes, roughly, as follows: Let $F$ be any consistent theory that contains **Q**. Assume then that the set of its theorems is decidable, that is (by the Church-Turing thesis), recursive. It would then follow that the set (of the Gödel numbers) of the theorems of $F$ is *strongly representable* in $F$ itself. Recall that this means that there is some formula $B(x)$ of the language of $F$ such that not only $F \vdash B(\ulcorner A\urcorner)$ whenever $F \vdash A$ (which even weak representability guarantees), but also that $F \vdash \neg B(\ulcorner A\urcorner)$ whenever $F \not\vdash A$. However, the technique used in the proof of the first incompleteness theorem also shows that there are always sentences for which the latter does not hold: it is possible to construct a Gödel sentence $G^B$ relative to $B(x)$ for $F$ such that:

$$\tag{D} F \vdash G^B \leftrightarrow \neg B(\ulcorner G^B\urcorner). $$

As before, it follows that $F \not\vdash G^B$. It has been assumed that $B(x)$ strongly represents the set of theorems, so this entails $F \vdash \neg B(\ulcorner G^B \urcorner)$, and therefore, by (D), $F \vdash G^B$, a contradiction. Therefore, $F$ must be undecidable.

A theory $F$ is called *essentially undecidable* if every consistent extension of it in the language of $F$ is undecidable. The above proof sketch in fact establishes that **Q** is essentially undecidable. (There are some very weak theories that are undecidable but not essentially undecidable.)

Recall that **Q** has only finitely many axioms and let $A_Q$ stand for the single sentence consisting of the conjunction of the axioms of **Q**. Then for any sentence $B$ of the language of arithmetic,

$\mathbf{Q} \vdash B$ if and only if it is a theorem of first-order logic that $A_Q \rightarrow B$.

But then a decision procedure for first-order logic would provide a decision method for **Q**. The latter, however, is impossible, as it has already been shown. Therefore, it can be concluded:

**Church’s Theorem** First-order predicate logic is undecidable.

(This undecidability result was first established by Church 1936a, b; the method of deriving it via the undecidability of **Q** is due to Tarski, Mostowski and Robinson 1953.)[^church-1936a][^tarski-1953]

Subsequently, a number of theories and problems from different areas of mathematics have been shown to be undecidable (see, e.g., Davis 1977; Murawski 1999: Ch 3)[^davis-1977][^murawski-1999].

### 4.3 Reflection Principles and Löb’s Theorem

Heuristically, one may view the Gödel sentence $G_F$ as expressing its own unprovability—saying “I am not provable”—though, as was already emphasized, such claims should be taken with a grain of salt. Leon Henkin put forward the question whether the sentence expressing its own *provability* (“I am provable”) is true or false, and provable or not (Henkin 1952)[^henkin-1952]. Georg Kreisel soon pointed out that this depends vitally on how provability is expressed; with different choices, one gets opposite answers (Kreisel 1953)[^kreisel-1953].

The paper of Martin Hugo Löb (1955)[^löb-1955], augmented by comments of a referee, brought substantial advances on various fronts. First, it introduces the now standard Löb derivability conditions discussed previously in the context of the second incompleteness theorem. Second, it contains Löb’s solution of Henkin’s problem about sentences “expressing their own provability”. Third, it contains a generalization now called “Löb’s Theorem”, but which Löb actually credits to the anonymous referee (who happened to be none other than Henkin himself; the whole story is told in Smoryński 1991.)[^smoryński-1991]

In order to understand Löb’s theorem properly it is useful to first consider the so-called “reflection principles”. Above, the focus has been on expressing, inside a formal system, that the system is consistent, i.e., on $\Cons(F)$. But naturally the theory should not merely be consistent but also *sound*, i.e., prove only true sentences. How should the soundness of a system, i.e., the claim that everything derivable in the system is true, be expressed? If one wants to express this in the language of the system itself, it cannot be done by a single statement saying this, because there is, by the undefinability of truth, no suitable truth predicate available in the language. Various restricted and unrestricted soundness claims can, however, be expressed in the form of a scheme, the so-called *Reflection Principles*:

$$\tag{Ref} \Prov_F(\ulcorner A\urcorner) \rightarrow A. $$

By taking $A$ to be $\bot$, and noting that $\bot$ is refutable in $F$, it is easy to see that Reflection Principle entails the consistency statement Cons$(F)$, i.e., $\neg\Prov_F (\ulcorner \bot \urcorner)$; hence it cannot be generally provable in the system.

The scheme can also be restricted. Equivalent to the assumption of 1-consistency, or $\Sigma^{0}_1$-soundness, for example, is the Reflection Principle restricted to $\Sigma^{0}_1$-sentences (i.e., the sentence $A$ in the scheme is required to be a $\Sigma^{0}_1$-sentence.) Or, it can be restricted to the universal $\Pi^{0}_1$-sentences; and so forth.

Exactly which instances of the reflection scheme are actually provable in the system? Löb’s Theorem gives a precise answer to this question (assuming that $\Prov_F (x)$ satisfies the derivability conditions):

**Löb’s Theorem** Let $A$ be any sentence of the language of $F$. Then: $F \vdash\Prov_F (\ulcorner A\urcorner) \rightarrow A$ if, and only if, $F \vdash A.$

Hence, the instances of soundness (reflection principle) provable in a system are exactly the ones which concern sentences which are themselves provable in the system. As a consequence, this also settles Henkin’s original problem: assuming that the arithmetized provability predicate is again “normal” (i.e., satisfies Löb’s derivability conditions), all sentences “asserting their own provability” are provable.

Actually, Löb’s theorem can be proved quite quickly as a consequence of the second incompleteness theorem. Kreisel has also noted that, in the opposite direction, the second incompleteness theorem can also be easily derived as a consequence of Löb’s theorem.

### 4.4 Hilbert’s Tenth Problem and the MRDP Theorem

The tenth on Hilbert’s famous list of important open problem in mathematics from 1900 asks for a decision method for the so-called Diophantine equations. Despite the unfamiliar term “Diophantine,” what is at issue here is truly elementary. Consider any equation with one or more variables and with integer coefficients, which involves only addition and multiplication, such as $x^2 + y^2 = 2$, or $3x^2 + 5y^2 + 2xy = 0$. If real-number solutions are sought, one usually speaks simply about an “equation”. However, in number theory, typically a solution is sought consisting only of integers. That makes a great difference. The former of the above equations has infinitely many solutions among real numbers, but only four among integers. The equation $x^2 + y^2 = 3$ also has infinitely many real solutions but no integer solutions. When the focus is on the integer solutions, one talks about “Diophantine equations” (after the ancient number theorist Diophantus of Alexandria).

For a positive solution of Hilbert’s tenth problem, it would have sufficed to present a particular concrete method which would have intuitively been a “mechanical” decision method. However, Turing’s pioneering analysis of the notion of decision method brought into focus the possibility of a negative solution. Beginning in the early 1950s, Julia Robinson and Martin Davis worked on this problem, later joined by Hilary Putnam. As a result of their collaboration, the first important result in this direction was achieved. Call an equation “an exponential Diophantine equation” if it involves also exponentiation, as well as addition and multiplication (that is, one can have both constants and variables as exponents); naturally, the focus is still in the integer solutions. Davis, Putnam, and Robinson (1961), showed that the problem of solvability of exponential Diophantine equations is undecidable. In 1970, Yuri Matiyasevich added the final missing piece, and demonstrated that the problem of the solvability of Diophantine equations is undecidable. Hence the overall result is often called MRDP Theorem (for an exposition, see, e.g., Davis 1973; Matiyasevich 1993)[^davis-1973][^matiyasevich-1993].

The essential technical achievement was that all semi-decidable (recursively enumerable) sets can be given a Diophantine representation, i.e., they can be represented by a simple formula of the form $\exists x_1 \ldots \exists x_n (s = t)$, where $(s = t)$ is a Diophantine equation. More exactly, for any given recursively enumerable set $S$, there is a Diophantine equation $(s(y, x_1 , \ldots ,x_n) = t(y, x_1 , \ldots ,x_n))$ such that $\boldsymbol{n} \in S$ if and only if $\exists x_1 \ldots \exists x_n (s(\overline{n}, x_1 , \ldots ,x_n) = t(\overline{n}, x_1 , \ldots ,x_n))$.

As there are semi-decidable (recursively enumerable) sets which are not decidable (recursive), the general conclusion follows immediately:

**MRDP Theorem** There is no general method for deciding whether or not a given Diophantine equation has a solution.

This also provides an elegant variant of the incompleteness theorems dealing with Diophantine equations:

**Corollary** For any 1-consistent axiomatizable formal system $F$ there are Diophantine equations which have no solutions but cannot be proved in $F$ to have no solutions.

(The question of avoiding the requirement of 1-consistency here is tricky; see Dyson, Jones and Shepherson 1982.)[^dyson-1982]

### 4.5 Concrete Cases of Unprovable Statements

The undecidable sentences provided by Gödel’s proofs are (if written out) extremely complicated formulas with no intuitive significance, construed only for the purposes of the incompleteness proofs. The question then arises whether there are any simple and natural mathematical statements which are likewise undecidable in chosen basic theories, e.g., in **PA**. There are now various specific statements with clear mathematical content which are known to be undecidable in some standard theories (though, just how natural even these are has been disputed; see Feferman 1989b)[^feferman-1989b]. Some well known, natural examples are listed below, beginning with some quite natural mathematical statements which are independent of **PA**, and proceeding to more and more powerful theories. Sometimes such results are called variants of Gödel’s theorem, or their proofs of independence alternative proofs of Gödel’s theorem, but this is misleading: interesting as they may be, they don’t have the generality of Gödel’s theorems proper, but only provide statements independent of a particular theory.

It is often stated that before the celebrated Paris-Harrington theorem (see below), no such natural independent mathematical statements were known. This is not, however, strictly speaking, correct. Already much earlier, around 1935, Gerhard Gentzen (see the entry on the development of proof theory) had provided such a statement. It is very natural to generalize the idea of induction from the domain of natural numbers to the domain of ordinal numbers. In set theory, such generalizations are called principles of transfinite induction. Though some constructivists may be sceptical about the legitimacy of full set theory, there are limited and more concrete cases of transfinite induction (only dealing with some well-defined classes of *countable* ordinals) that are perfectly acceptable even from the constructivist or intuitionist viewpoint. One important case is the principle of transfinite induction up to the ordinal called $\varepsilon_0$. Gentzen showed that the consistency of **PA** can be proved if this transfinite induction principle is assumed. Therefore, because of the second incompleteness theorem, the principle itself cannot be provable in **PA** (Gentzen 1936)[^gentzen-1936].

Ramsey’s theorem is a result in infinitary combinatorics, established by Frank Ramsey (1930)[^ramsey-1930], and deals with possibilities of “colouring” for certain graphs. Jeff Paris and Leo Harrington formulated a finitary variant of Ramsey’s theorem, and showed that it is not provable in **PA** (Paris & Harrington 1977)[^paris-1977]. This provides a quite natural statement of finite combinatorics which is independent of **PA**. Perhaps an even cleaner example is Goodstein’s theorem, due to Reuben Goodstein (1944)[^goodstein-1944], which is purely number theoretic in nature. First one defines a certain natural class of sequences of natural numbers, now called “Goodstein sequences”. The theorem states that every Goodstein sequence eventually terminates at 0. Goodstein’s theorem is certainly a natural mathematical statement, for it was formulated and proved (obviously by proof methods that go beyond **PA**) by Goodstein long before (that is, in 1944) it was shown, in 1982, that the theorem is not provable in **PA** (Kirby & Paris 1982)[^kirby-1982].

Moving now to stronger theories beyond **PA**, one can mention, for example, Kruskal’s Theorem. This is a theorem which concerns certain orderings of finite trees (Kruskal 1960)[^kruskal-1960]. Harvey Friedman showed that this theorem is unprovable even in subsystems of second-order arithmetic much stronger than **PA** (see Simpson 1985)[^simpson-1985]. In particular, it is not provable in any theory which is predicatively justified (under a widely accepted explication of “predicative”, cf. the section on predicativism in the entry on the philosophy of mathematics).

There are some concrete examples of mathematical statements undecided even in stronger theories which come from the so-called descriptive set theory. This field of mathematics is related to topology and was initiated by the French semi-intuitionists (Lebesgue, Baire, Borel; see the section on descriptive set theory, etc., in the entry on intuitionism in the philosophy of mathematics). It studies sets which possess relatively simple definitions (in contradistinction to the ideas of arbitrary sets and various higher power-sets, which the semi-intuitionists rejected as meaningless) called projective or analytic sets. Classically these were defined as the sets that can be built up from a countable intersection of open sets by taking continuous images and complements finitely many times; they coincide with the sets which are definable in the language of **P$^2$**. In particular, the so-called Borel sets can be simply defined both by a formula of the form $\exists XA(x)$ and by a formula of the form $\forall XB(x)$, where $A$ and $B$ do not contain any set variables (in logician’s terminology, Borel sets are the $\Delta^{1}_1$ sets). A Borel function is defined analogously (see, e.g., Martin 1977)[^martin-1977].

Harvey Friedman has established the following theorem: roughly, if $S$ is a Borel set, then there exists a Borel function $f$ such that the graph of $f$ is either included in or disjoint from $S$. Friedman showed that this simple-sounding theorem is not provable even in full second-order arithmetic **P$^2$**, but proving it necessarily requires the full power of **ZFC** (see Simpson 1999: 23)[^simpson-1999].

Further, it was a traditional question of descriptive set theory (a question which can be formulated in the language of second order arithmetic) whether all projective sets (see above) are Lebesque measurable. This remained an open problem for many decades, and for a good reason: it turned out that the statement is independent even of the full **ZFC** set theory (see Solovay 1970)[^solovay-1970]. Only by postulating the existence of some extremely large cardinals (so-called Woodin cardinals) can the hypothesis that all projective sets are Lebesque measurable be proved (this was achieved as a consequence of their work on so-called projective determinacy by Woodin, Martin and Steel; see Woodin 1988; Martin & Steel 1988, 1989)[^martin-1988][^martin-1989][^woodin-1988].

Sometimes Paul Cohen’s celebrated result, that the Continuum Hypothesis (CH) is independent of **ZFC** (Cohen 1963, 1964; and the entry on independence and large cardinals)[^cohen-1963][^cohen-1964], is mentioned in this connection. However, this case is very different. In all the above independence results the relevant statements are still theorems of mathematics, taken as shown to be true (the last case, which requires large cardinal axioms that go beyond **ZFC**, is more controversial; still, at least many set-theoreticians find such axioms plausible). And with the first incompleteness theorem itself, the truth of the unprovable statement easily follows, given that the assumption of the consistency of the system is indeed correct. However, in the case of Cohen’s result, there is absolutely no indication whether CH should be considered true, false, or perhaps lacking a truth-value.

## 5. The History and Early Reception of the Incompleteness Theorems

Gödel’s results were certainly surprising, but some sort of incompleteness phenomenon was not totally unexpected. The possibility of incompleteness in the context of set theory was discussed by Bernays and Tarski already in 1928, and von Neumann, in contrast to the dominant spirit in Hilbert’s program, had considered it possible that logic and mathematics were not decidable. Gödel himself had mentioned the possibility of an undecidable problem concerning real numbers in his thesis in 1929 (see Dawson 1985)[^dawson-1985]. Hilbert (1928)[^hilbert-1928], on the other hand, had assumed that Peano Arithmetic and other standard theories were complete. Apparently Gödel was also impressed by Brouwer, who in his lecture in Vienna in 1928 had suggested that mathematics is inexhaustible and cannot be completely formalized (see Wang 1987, 84; and the section on Brouwer’s view of the formalist program in the entry on the development of intuitionistic logic).

Be that as it may, it seems that Gödel actually arrived at the first exact observations about incompleteness via a different route, during his attempts to *contribute* to Hilbert’s program, and not to undermine it (see Dawson 1997: Ch. IV)[^dawson-1997]. Namely, in 1930, Gödel made an effort to advance Hilbert’s program by attempting to prove the consistency of analysis (or, second-order arithmetic) with the resources of arithmetic, and thus reduce the consistency of the former to the consistency of the latter. In his attempted proof, he needed the notion of truth. Gödel soon faced various paradoxes (such as the Liar paradox), and had to conclude that arithmetical truth cannot be defined in arithmetic. Hence, Gödel first arrived at a version of the undefinability of truth theorem, usually associated with Tarski (cf. Murawski 1998)[^murawski-1998]. This also easily yields a weak version of the incompleteness result: the set of sentences provable in arithmetic can be defined in the language of arithmetic, but the set of true arithmetical sentences cannot; therefore the two cannot coincide. Moreover, under the assumption that all provable sentences are true, it follows that there must be true sentences which are not provable. This approach, though, does not exhibit any particular such sentence.

However, the intellectual environment of Gödel was that of the Vienna Circle with its radically anti-metaphysical attitude. In particular, even the notion of truth was considered as suspicious or even nonsensical at the time, at least by some logical positivists (e.g., Neurath, Hempel). Therefore, Gödel worked hard to eliminate any appeal to the notion of truth and attempted to do without it. He therefore introduced the notion of *ω*-consistency, which can be defined rigorously and purely syntactically. This led to the incompleteness theorems in the form that they are now known.

As to *the Diagonalization Lemma*, actually Gödel himself originally demonstrated only a special case of it, that is, only for the provability predicate. The general lemma was apparently first discovered by Carnap 1934 (see Gödel 1934, 1935)[^gödel-1934][^gödel-1935]. Still more general versions, for formulas with free variables, were presented in Ehrenfeucht & Feferman 1960 and Montague 1962 (see Smoryński 1981)[^smoryński-1981].

The reception of Gödel’s results was mixed. Some important figures in the field of logic and the foundations of mathematics quite quickly assimilated the results and understood their relevance, but there was also quite a lot of misunderstanding and resistance (for detailed accounts of the reception, see Dawson 1985; Mancosu 1999)[^dawson-1985][^mancosu-1999].

Gödel revealed his results to Carnap in Vienna on 26 August 1930, and announced his result (the first theorem) in a casual discussion remark in the famous Königsberg Conference on September 7, 1930. John von Neumann, who was in the audience and was at the time working in the context of Hilbert’s program, immediately understood the great importance of the result. On 20 November he wrote a letter to Gödel on a “remarkable” corollary of Gödel’s result he had discovered: the unprovability of consistency (the second theorem). Meanwhile Gödel himself, however, had found the same idea and had already sent the final version of his article, which now contained also a statement of the second incompleteness theorem, for publication. The article was published in January 1931 (Gödel 1931; helpful introductions to Gödel’s original paper are Kleene 1986 and Zach 2005)[^gödel-1931][^gödel-1986][^kleene-1986][^zach-2005]. The word quickly started to spread of these results which apparently had great importance for the foundations of mathematics—though views on what really was the moral varied. Paul Bernays, perhaps the most important collaborator of Hilbert, showed great interest in the results, though he first had difficulties in understanding them properly. His active correspondence with Gödel also shows that Gödel was already at the time fully aware of the undefinability of truth.

As Gödel’s original approach focused on his specific though very comprehensive system **P** and its (primitive recursive) extensions, some doubted the generality of Gödel’s results. Alonzo Church, for example, in a letter to Gödel in July 1932, suggested that Gödel’s results would not apply to his system of *λ*-conversion (the system was later proved to be inconsistent by Kleene and Rosser). Gödel was anxious to generalize his discoveries, and extended the results to a wider class of systems in papers in 1932 and 1934. He also suggested that his methods would be applicable to standard systems of set theory (however, it was only after the satisfactory characterization of decidability and the Church-Turing thesis a few years later that it was possible to give a fully general formulation of the incompleteness theorems (see above); this was first done in Kleene 1936). The eminent set-theorist Ernst Zermelo directed some rather harsh criticism towards Gödel’s work, but the two also corresponded on the topic. Zermelo seems to have had serious difficulties in understanding the relevant concepts and results.

In March 1933, Gödel received a letter from Paul Finsler, from Zürich, who suggested that he had already earlier (in Finsler 1926)[^finsler-1926] done closely related work but with a more general relevance. Gödel replied that Finsler’s system was not really defined at all. In his heated response, Finsler claimed that it was not necessary to be able to study a system for it to be sharply defined, and that there was no difference in principle between his ideas and Gödel’s. In retrospect, it is quite clear that the approaches of Finsler and Gödel were very different: for Gödel’s work, the notion of formalized system was essential, whereas Finsler rejected the very notion as artificially restrictive. In fact, it is far from clear that Finsler’s ideas make any sense—whatever vague analogies there may be between them and Gödel’s proof.

On the other hand, it is fair to say that Emil Post had in some respects anticipated Gödel’s discoveries. He obtained abstract versions of incompleteness results apparently already in 1922. In particular, he observed that his methods would provide a statement undecidable in *Principia Mathematica.* These results were, however, based on Post’s own version of the “Church-Turing thesis”, with which he was dissatisfied, and his work was left unpublished. It was reported much later in (Post 1941)[^post-1941].

The correctness of Gödel’s theorems remained the subject of lively debate throughout the 1930s (see Dawson 1985)[^dawson-1985]. In 1939, Hilbert and Bernays’ second volume of *Die Grundlagen der Mathematik* appeared, including a detailed proof of the second incompleteness theorem. Thereafter, serious opposition to Gödel’s conclusions disappeared at least among those who were working actively in mathematical logic and the foundations of mathematics. However, in more philosophical circles, some resistance remained. Most famously, Wittgenstein made some critical remarks concerning Gödel’s theorem in his posthumously published *Remarks on the Foundations of Mathematics.* The dominant initial reaction was that Wittgenstein simply failed to understand the result. More charitable interpretations have emerged, and the debate is still very much alive (see the section on Gödel and undecidable propositions in the entry on Wittgenstein’s philosophy of mathematics).

## 6. Philosophical Implications—Real and Alleged

### 6.1 Philosophy of Mathematics

Of the various fields of philosophy, Gödel’s theorems are obviously most immediately relevant for the philosophy of mathematics. To begin with, they pose, at least *prima facie*, serious problems for Hilbert’s program (this issue is discussed in some detail in the section on the impact of incompleteness in the entry on Hilbert’s Program and the supplement “Did the Incompleteness Theorems Refute Hilbert’s Program?” in the entry on Kurt Gödel.). Then again, they have important consequences for *intuitionism* (see the entry on intuitionism in the philosophy of mathematics) (see also Gödel 1933, 1941; Raatikainen 2005)[^gödel-1933][^gödel-1941][^raatikainen-2005].

There has been some dispute on the issue as to whether Gödel’s theorems conclusively refute *logicism* (see the entry on logicism). Henkin (1962)[^henkin-1962] and Musgrave (1977)[^musgrave-1977], for example, argue it does; Sternfeld (1976)[^sternfeld-1976] and Rodríguez-Consuegra (1993)[^rodríguez-consuegra-1993] disagree (see also Hellman 1981; Raatikainen 2005)[^hellman-1981][^raatikainen-2005].

Gödel himself developed an argument against the conventionalist philosophy of mathematics of logical positivism, and of Carnap’s in particular, based on the incompleteness results (Gödel 1953/9)[^gödel-1953]. It is discussed in Goldfarb and Ricketts 1992; Ricketts 1995; Goldfarb 1995; Crocco 2003; Awodey & Carus 2003, 2004; Tennant 2008; see also the supplementary document “A Philosophical Argument About the Content of Mathematics” in the entry on Kurt Gödel.

### 6.2 Self-evident and analytical truths

One can also give more general epistemological interpretations of Gödel’s theorems. Quine and Ullian (1978), for example, consider the traditional philosophical picture that all truths could be proved by self-evident steps from self-evident truths and observation. They then point out that even the truths of elementary number theory are presumably not in general derivable by self-evident steps from self-evident truths (Quine & Ullian 1978: 64–65.)[^quine-1978] Hilary Putnam (1975)[^putnam-1975] in turn submits that, under a certain natural understanding of “analytic”, there must be, by Gödel’s theorems, synthetic truths in mathematics. In fact, Gödel himself made remarks in a very similar spirit that even the theory of integers is demonstrably non-analytic (Gödel 1944)[^gödel-1944].

### 6.3 ‘Gödelian’ arguments against mechanism

There have been repeated attempts to apply Gödel’s theorems to demonstrate that the powers of the human mind outrun any mechanism or formal system. Such a Gödelian argument against mechanism was considered, if only in order to refute it, already by Turing in the late 1940s (see Piccinini 2003)[^piccinini-2003]. An unqualified anti-mechanist conclusion was drawn from the incompleteness theorems in a widely read popular exposition, *Gödel’s Theorem*, by Nagel and Newman (1958). Shortly afterwards, J.R. Lucas (1961)[^lucas-1961] famously proclaimed that Gödel’s incompleteness theorem

> proves that Mechanism is false, that is, that minds cannot be explained as machines.

He stated that

> given any machine which is consistent and capable of doing simple arithmetic, there is a formula it is incapable of producing as being true … but which we can see to be true.

More recently, very similar claims have been put forward by Roger Penrose (1989, 1994)[^penrose-1989][^penrose-1994]. John Searle (1997)[^searle-1997] has joined the discussion and partly defended Penrose against his critics. Crispin Wright (1994, 1995)[^wright-1994][^wright-1995] has endorsed related ideas from an intuitionistic point of view (for criticism, see Detlefsen 1995)[^detlefsen-1995]. They all insist that Gödel’s theorems imply that the human mind infinitely surpasses the power of any finite machine or formal system.

These Gödelian anti-mechanist arguments are, however, problematic, and there is wide consensus that they fail. The standard response to this argument goes along the following lines (this objection goes back to Putnam 1960; see also Boolos 1968, Shapiro 1998)[^boolos-1968][^putnam-1960][^shapiro-1998]: The argument assumes that for any formalized system, or a finite machine, there exists the Gödel sentence which is unprovable in that system, but which the human mind can see to be true. Yet Gödel’s theorem has in reality a conditional form, and the alleged truth of the Gödel sentence of a system depends on the assumption of the consistency of the system. The anti-mechanist’s argument thus also requires that the human mind can always see whether or not a given formalized theory is consistent. However, this is highly implausible (cf. Davis 1990)[^davis-1990]. Lucas, Penrose and others have attempted to reply to such criticism (see, e.g., Lucas 1996; Penrose 1995, 1997)[^lucas-1996][^penrose-1995][^penrose-1997]. For detailed criticism of Penrose, see Boolos 1990; Davis 1990, 1993; Feferman 1995; Lindström 2001; Pudlák 1999; Shapiro 2003; many of these considerations are also relevant for what Lucas says).

### 6.4 Gödel and Benacerraf on Mechanism and Platonism

Interestingly, Gödel himself also presented an anti-mechanist argument although it was more cautious and only published posthumously (in his *Collected Works*, Vol. III, in 1995). That is, in his 1951 Gibbs lecture, Gödel drew the following disjunctive conclusion from the incompleteness theorems:

> either … the human mind (even within the realm of pure mathematics) infinitely surpasses the power of any finite machine, or else there exist absolutely unsolvable diophantine problems.

Gödel speaks about this statement as a “mathematically established fact” (Gödel 1951; for more discussion on Gödel’s disjunctive claim, see, e.g., Shapiro 1998)[^gödel-1951][^shapiro-1998]. According to Gödel, the second alternative

> seems to disprove the view that mathematics is only our own creation … that mathematical objects and facts … exist objectively and independently of our mental acts and decisions.

Gödel was nonetheless inclined to deny the possibility of absolutely unsolvable problems, and although he did believe in mathematical Platonism, his reasons for this conviction were different, and he did not maintain that the incompleteness theorems alone establish Platonism. Thus Gödel believed in the first disjunct, that the human mind infinitely surpasses the power of any finite machine. Still, this conclusion of Gödel follows, as Gödel himself clearly explains, only if one denies, as does Gödel, the possibility of humanly unsolvable problems. It is not a necessary consequence of incompleteness theorems.

Now Gödel was, unlike the later advocates of the so-called Gödelian anti-mechanist argument, sensitive enough to admit that both mechanism and the alternative that there are humanly absolutely unsolvable problems are consistent with his incompleteness theorems. His fundamental reasons for disliking the latter alternative are much more philosophical. Gödel thought in a somewhat Kantian way that human reason would be fatally irrational if it asked questions it could not answer (for critical discussion, see Kreisel 1967; Boolos 1995; Raatikainen 2005)[^boolos-1995][^kreisel-1967][^raatikainen-2005].

As a reaction to Lucas’ argument, but before the publication of Gödel’s Gibbs Lecture, Paul Benacerraf (1967)[^benacerraf-1967] put forward more qualified conclusions that interestingly resemble some ideas of Gödel. He argued that it is consistent with all the facts that I am indeed a Turing machine, but that I cannot ascertain which one. For some critical discussion, see Chihara 1972 and Hanson 1971.

### 6.5 Mysticism and the existence of God?

Sometimes quite fantastic conclusions are drawn from Gödel’s theorems. It has been even suggested that Gödel’s theorems, if not exactly prove, at least give strong support for mysticism or the existence of God. These interpretations seem to assume one or more misunderstandings which have already been discussed above: it is either assumed that Gödel provided an absolutely unprovable sentence, or that Gödel’s theorems imply Platonism, or anti-mechanism, or both.

For more discussion about the philosophical aspects of the incompleteness theorems, see Raatikainen 2005 and Franzén 2005.

## Further reading

A standard reference for the incompleteness theorems is:

- Smoryński, C., 1977, “The incompleteness theorems,” in *Handbook of Mathematical Logic*, J. Barwise (ed.), Amsterdam: North-Holland, pp. 821–866 [[available online](http://www.karlin.mff.cuni.cz/~krajicek/smorynski.pdf)].

There are several introductory textbooks in mathematical logic which give a good exposition of the incompleteness theorems and related topics; for example:

- Boolos, G., and R. Jeffrey, 1989, *Computability and Logic*, 3ʳᵈ revised edition, Cambridge: Cambridge University Press.
- Enderton, H., 1972, *A Mathematical Introduction to Logic*, New York: Academic Press.
- Van Dalen, D., 2004, *Logic and Structure*, 4ᵗʰ edition, Berlin: Springer.

Two books that are dedicated to the incompleteness theorems are:

- Smullyan, R., 1991, *Gödel’s Incompleteness Theorems*, Oxford: Oxford University Press.
- Smith, P., 2007, *An Introduction to Gödel’s Theorems*, Cambridge: Cambridge University Press.

Another useful book on the incompleteness theorems and related topics is:

- Murawski, R., 1999, *Recursive Functions and Metamathematics: Problems of Completeness and Decidability, Gödel’s Theorems.* Dordrecht: Kluwer.

A comprehensive, more advanced book on these themes is:

- Hájek, P. and Pudlák, P., 1993, *Metamathematics of First-Order Arithmetic*, Berlin: Springer.

Another useful book, including also some more advanced topics is:

- Franzén, T., 2004, *Inexhaustibility: A Non-Exhaustive Treatment*, Lecture Notes in Logic 16, ASL, Wellesley: A.K. Peters.

The more philosophical aspects around the incompleteness theorems are surveyed in the following two sources (Franzén is an accessible, informal, and yet reliable, explanation of the incompleteness theorems):

- Raatikainen, P., 2005, “On the Philosophical Relevance of Gödel’s Incompleteness Theorems,” *Revue Internationale de Philosophie*, 59: 513–534 [[available online](https://www.cairn.info/revue-internationale-de-philosophie-2005-4-page-513.htm)].
- Franzén, T., 2005, *Gödel’s Theorem: An Incomplete Guide to its Use and Abuse*, Wellesley: A.K. Peters.

The following two papers survey various issues around the first incompleteness theorem:

- Beklemishev, L. D., 2010, “Gödel incompleteness theorems and the limits of their applicability. I,” *Russian Mathematical Surveys*, 65: 857–898.
- Buldt, B., 2014, “The scope of Gödel’s first incompleteness theorem,” *Logica Universalis*, 8: 499–552.

Finally, there is an open-source e-book that contains a presentation of the incompleteness theorems:

- Zach, Richard, 2021, [*Incompleteness and Computability*](https://ic.openlogicproject.org/), e-Book published by the Open Logic Project.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=goedel-incompleteness). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/goedel-incompleteness/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=goedel-incompleteness&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/goedel-incompleteness/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- Papers and Reviews by Sol Feferman on Gödel’s incompleteness theorem:
- [Review of Rebecca Goldstein’s *The Proof and Paradox of Kurt Gödel*](https://www.lrb.co.uk/v28/n03/solomon-feferman/provenly-unprovable), in *London Review of Books*, 28(3) (9 February 2006).
- [The impact of the incompleteness theorems on mathematics](https://www.ams.org/notices/200604/fea-feferman.pdf), preprint, *Notices American Mathematical Society*, 53(4) (April 2006): 434–439.
- [The nature and significance of Gödel’s incompleteness theorem](https://web.archive.org/web/20171211005909/http://math.stanford.edu/~feferman/papers/Godel-IAS.pdf), lecture for the Princeton Institute for Advanced Study Gödel Centenary Program, Nov. 17, 2006.
- [Gödel’s incompleteness theorems, free will and mathematical thought](https://web.archive.org/web/20171211010122/http://math.stanford.edu/~feferman/papers/GodelFreeWill.pdf), preprint of paper in *Free Will and Modern Science*, R. Swinburne (ed.), Oxford: Oxford University Press, 2011, 102–122.
- [Penrose’s Gödelian argument](http://journalpsyche.org/files/0xaa23.pdf), preprint of review that appeared in *PSYCHE*, 2 (1996): 21–32.
- [Special Issue (April 2006) of the *Notices of the American Mathematical Society*](http://www.ams.org/notices/200604/), (Volume 53, Issue 4), marking the centennial of the birth of Kurt Gödel with a collection of articles about Gödel, his work, and its impact on mathematics.

## Related Entries

Church-Turing Thesis | Gödel, Kurt | Hilbert, David: program in the foundations of mathematics | logic, history of: intuitionistic logic | logic: second-order and higher-order | mathematics, philosophy of | mathematics, philosophy of: intuitionism | proof theory | proof theory: development of | recursive functions | set theory | set theory: independence and large cardinals | Turing machines | Wittgenstein, Ludwig: philosophy of mathematics

### Acknowledgments

The author would like to thank Richard Zach for his careful and valuable comments on the earlier drafts of this entry. The author and SEP editors would like to thank Richard O’Callaghan for bringing to our attention that, in an earlier version of the supplement on the Diagonalization Lemma, the definition of the substitution function, although standard, didn’t suffice for the purposes of the proof.

[^auerbach-1985]: Auerbach, David, 1985, “Intensionality and the Gödel theorems,” *Philosophical Studies*, 48 (3):337–51.

[^auerbach-1992]: –––, 1992, “How to say things with formalisms,” in *Proof, Logic, and Formalization*, M. Detlefsen (ed.), London: Routledge, 77–93 [[available online](https://www.lib.ncsu.edu/resolver/1840.2/98)].

[^awodey-2003]: Awodey, S. & A.W. Carus, 2003, “Carnap versus Gödel on Syntax and Tolerance,” in *Logical Empiricism: Historical and Contemporary Perspectives*, P. Parrini et al. (eds.), Pittsburgh: University of Pittsburgh Press, pp. 57–64 [[available online](https://www.cmu.edu/dietrich/philosophy/docs/tech-reports/106_Awodey.pdf)].

[^awodey-2004]: –––, 2004, “How Carnap Could Have Replied to Gödel,” in S. Awodey and C. Klein (eds.), *Carnap Brought Home: The View from Jena*, LaSalle, IL: Open Court, pp. 203–223 [[available online](https://www.cmu.edu/dietrich/philosophy/docs/tech-reports/123_Awodey.pdf)].

[^barzin-1940]: Barzin, M., 1940, “Sur la portée du théorème de M. Gödel,” *Académie Royale de Belgique, Bulletin de la Classe des Sciences*, Series 5, 26: 230–39.

[^benacerraf-1967]: Benacerraf, P., 1967, “God, the Devil, and Gödel,” *The Monist*, 51: 9–32 [[available online](http://www2.units.it/etica/2003_1/3_monographica.htm)].

[^bezboruah-1976]: Bezboruah, A. and J.C. Shepherdson, 1976, “Gödel’s Second Incompleteness Theorem for Q,” *The Journal of Symbolic Logic*, 41: 503–512.

[^boolos-1968]: Boolos, G., 1968, “Review of ‘Minds, Machines and Gödel’, by J.R. Lucas, and ‘God, the Devil, and Gödel’,” *Journal of Symbolic Logic*, 33: 613–15.

[^boolos-1990]: –––, 1990, “On ‘Seeing’ the Truth of Gödel Sentence,” *Behavioral and Brain Sciences*, 13: 655–656.

[^boolos-1995]: –––, 1995, “Introductory Note to \*1951,” in Gödel 1995: 290–304.

[^boolos-1989]: Boolos, G. and R. Jeffrey, 1989, *Computability and logic*, 3ʳᵈ revised edition, Cambridge: Cambridge University Press.

[^carnap-1934]: Carnap, R., 1934, *Logische Syntax der Sprache*, Vienna: Julius Springer.

[^chihara-1972]: Chihara, C., 1972, “On Alleged Refutations of Mechanism Using Gödel’s Incompleteness Results,” *Journal of Philosophy*, 69: 507–26.

[^church-1936a]: Church, A., 1936a, “An Unsolvable Problem of Elementary Number Theory,” *American Journal of Mathematics*, 58: 354–363. Republished in Davis 1965, 89–107.

[^church-1936b]: –––, 1936b, “A Note on Entscheidungsproblem,” *Journal of Symbolic Logic*, 1: 40–41; correction, *ibid.*, 101–102. Republished in Davis 1965, 110–115.

[^cohen-1963]: Cohen, P. J., 1963, “The Independence of the Continuum Hypothesis I,” *Proceedings of the National Academy of Sciences*, (U.S.A.), 50(6): 1143–48.

[^cohen-1964]: –––, 1964, “The Independence of the Continuum Hypothesis II,” *Proceedings of the National Academy of Sciences*, (U.S.A.), 51(1): 105–110.

[^crocco-2003]: Crocco, G., 2003, “Gödel, Carnap, and the Fregean Heritage,” *Synthese*, 137: 21–41.

[^davis-1965]: Davis, M., 1965, *The Undecidable: Basic Papers on Undecidable Propositions, Unsolvable Problems and Computable Functions*, Hewlett, NY: Raven Press.

[^davis-1973]: –––, 1973, “Hilbert’s Tenth Problem is Unsolvable,” *The American Mathematical Monthly*, 80: 233–269.

[^davis-1977]: –––, 1977, “Unsolvable Problems,” in *Handbook of Mathematical Logic*, J. Barwise (ed.), Amsterdam: North-Holland, pp. 567–594.

[^davis-1990]: –––, 1990, “Is Mathematical Insight Algorithmic?” *Behavioral and Brain Sciences*, 13: 659–660.

[^davis-1993]: –––, 1993, “How Subtle is Gödel’s Theorem? More on Roger Penrose,” *Behavioral and Brain Sciences*, 16: 611–612.

[^davis-1961]: Davis, M., H. Putnam, and J. Robinson, 1961, “The decision problem for exponential diophantine equations,” *Annals of Mathematics (2)*, 74(3): 425–436.

[^dawson-1985]: Dawson, J., 1985, “The Reception of Gödel’s Incompleteness Theorems,” *PSA: Proceedings of the Biennial Meeting of the Philosophy of Science Association 1984*, vol. II, pp. 253–271.

[^dawson-1997]: –––, 1997, *Logical Dilemmas: The Life and Work of Kurt Gödel*, Natick, MA: A. K. Peters.

[^detlefsen-1979]: Detlefsen, M., 1979, “On Interpreting Gödel’s Second Theorem,” *Journal of Philosophical Logic*, 8(1): 297–313.

[^detlefsen-1986]: –––, 1986, *Hilbert’s Program: An Essay in Mathematical Instrumentalism*, Dordrecht: Reidel.

[^detlefsen-1990]: –––, 1990, “On an Alleged Refutation of Hilbert’s Program Using Gödel’s First Incompleteness Theorem,” *Journal of Philosophical Logic*, 19(4): 343–377.

[^detlefsen-1995]: –––, 1995, “Wright on the Non-mechanizability of Intuitionist Reasoning,” *Philosophia Mathematica*, 3(1): 103–118.

[^detlefsen-2001]: –––, 2001, “What Does Gödel’s Second Theorem Say?” *Philosophia Mathematica*, 9: 37–71.

[^dyson-1982]: Dyson, V., J.P. Jones, and J.C. Shepherdson, 1982, “Some Diophantine Forms of Gödel’s Theorem,” *Archiv für Mathematische Logik und Grundlagenforschung*, 22: 51–60.

[^ehrenfeucht-1960]: Ehrenfeucht, A. and S. Feferman, 1960, “Representability of recursively enumerable sets in formal theories”, *Arch. Math. Logik Grundlag.*, 5(1–2), 37–41.

[^feferman-1960]: Feferman, S., 1960, “Arithmetization of Metamathematics in a General Setting,” *Fundamenta Mathematicae*, 49: 35–92.

[^feferman-1982]: –––, 1982, “Inductively Presented Systems and the Formalization of Meta-mathematics,” in *Logic Colloquium ’80*, D. van Dalen et al. (eds.), Amsterdam: North-Holland, pp. 95–128.

[^feferman-1989a]: –––, 1989a, “Finitary Inductively Presented Logics,” in *Logic Colloquium ‘88*, R. Ferro, et al. (eds.), Amsterdam: North-Holland, pp. 191–220. [[available online](https://web.archive.org/web/20170311004001/http://math.stanford.edu/~feferman/papers/presentedlogics.pdf)]

[^feferman-1989b]: –––, 1989b, “Infinity in Mathematics: Is Cantor Necessary?” *Philosophical Topics*, 17(2): 23–45.

[^feferman-1995]: –––, 1995, “Penrose’s Gödelian argument: A Review of *Shadows of Mind*, by Roger Penrose,” *Psyche*, 2 (7).

[^feferman-1997]: –––, 1997, “My Route to Arithmetization,” *Theoria*, 63: 168–181.

[^finsler-1926]: Finsler, P., 1926, “Formale Beweise und die Entscheidbarkeit,” *Mathematische Zeitschrift*, 25: 676–82.

[^fitting-2007]: Fitting, M., 2007, *Incompleteness in the land of sets*, London: College Publications. Series: Studies in logic ; v. 5.

[^franks-2009]: Franks, C., 2009, *The Autonomy of Mathematical Knowledge. Hilbert’s Program Revisited*, Oxford: Oxford University Press.

[^gaifman-2006]: Gaifman, H., 2006, “Naming and Diagonalization, From Cantor to Gödel to Kleene,” *Logic Journal of the IGPL*, 14: 709–728. [[available online](https://haimgaifman.files.wordpress.com/2016/07/22odel-to-kleene.pdf)]

[^gentzen-1936]: Gentzen, G., 1936, “Die Widerspruchsfreiheit der reinen Zahlentheorie,” *Mathematische Annalen*, 112: 493–565.

[^gödel-1931]: Gödel, K., 1931, “Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I,” *Monatshefte für Mathematik Physik*, 38: 173–198. English translation in van Heijenoort 1967, 596–616, and in Gödel 1986, 144–195.

[^gödel-1932]: –––, 1932, “Über Vollständigkeit und Widerspruchsfreiheit,” *Ergebnisse eines mathematischen Kolloquiums*, 3: 12–13. English translation “On Completeness and Consistency” in Gödel 1986: 235–7.

[^gödel-1933]: –––, 1933, “The Present Situation in Foundations of Mathematics,” in Gödel 1995: 45–53.

[^gödel-1934]: –––, 1934, “On Undecidable Propositions of Formal Mathematical Systems” (mimeographed lecture notes; taken by S. Kleene and J. Rosser), reprinted with corrections in Davis 1965, 41–81, and Gödel 1986, 346–371.

[^gödel-1935]: –––, 1935, “Review of Carnap 1934,” in Gödel 1986: 389.

[^gödel-1941]: –––, 1941, “In What Sense is Intuitionistic Logic Constructive?” in Gödel 1995: 189–200.

[^gödel-1944]: –––, 1944, “Russell’s Mathematical Logic,” in *The Philosophy of Bertrand Russell*, P. A. Schilpp (ed.), Evanston, Il.: Northwestern University, pp. 125–153. Reprinted in Gödel 1990: 119­–141.

[^gödel-1951]: –––, 1951, “Some Basic Theorems on the Foundations of Mathematics and their Implications” (Gibbs Lecture), in Gödel 1995: 304­–323.

[^gödel-1953]: –––, 1953/9, “Is Mathematics a Syntax of Language?,” lecture manuscript (two versions), in Gödel 1995: 334–362.

[^gödel-1963]: –––, 1963, “Note added 28 August 1963” (to Gödel 1931), in Gödel 1986: 195.

[^gödel-1986]: –––, 1986, *Collected Works I. Publications 1929–1936*, S. Feferman et al. (eds.), Oxford: Oxford University Press.

[^gödel-1990]: –––, 1990, *Collected Works II. Publications 1938–1974*, S. Feferman et al. (eds.), Oxford: Oxford University Press.

[^gödel-1995]: –––, 1995, *Collected Works III. Unpublished Essays and Lectures*, S. Feferman et al. (eds.), Oxford: Oxford University Press.

[^goldfarb-1995]: Goldfarb, W., 1995, “Introductory Note to \*1953/9,” in Gödel 1995: 324–334.

[^goldfarb-1992]: Goldfarb, W. and T. Ricketts, 1992, “Carnap and the Philosophy of Mathematics,” in *Science and Subjectivity*, D. Bell and W. Vossenkuhl (eds.), Berlin: Akademie Verlag, pp. 61–78.

[^gómez-2004]: Gómez Torrente, M., 2004, “The Indefinability of Truth in the *Wahrheitsbegriff*,” *Annals of Pure and Applied Logic*, 126(1–3): 27–37. [[available online](http://dx.doi.org/10.1016/j.apal.2003.10.005)]

[^goodstein-1944]: Goodstein, R., 1944, “On the Restricted Ordinal Theorem,” *The Journal of Symbolic Logic*, 9: 33–41.

[^grelling-1937]: Grelling, K., 1937, “Gibt es eine Gödelsche Antinomie?,” *Theoria*, 3: 297–306.

[^hanson-1971]: Hanson, W.H., 1971, “Mechanism and Gödel’s theorems,” *The British Journal for the Philosophy of Science*, 22: 9–16.

[^hellman-1981]: Hellman, G., 1981, “How to Gödel a Frege-Russell: Gödel’s Incompleteness Theorems and Logicism,” *Nous*, 15: 451–468.

[^helmer-1938]: Helmer, O., 1938, “Perelman versus Gödel,” *Mind*, 46: 58–60.

[^henkin-1952]: Henkin, L., 1952, “Problem,” *The Journal of Symbolic Logic*, 17: 160.

[^henkin-1962]: –––, 1962, “Are Mathematics and Logic Identical?” *Science*, 138: 788–794.

[^hilbert-1928]: Hilbert, D., 1928, “Die Grundlagen der Mathematik,” *Abhandlungen aus dem Mathematischen Seminar der Hamburgischen Universität*, 6: 65–85. English translation in van Heijenoort 1967.

[^hilbert-1939]: Hilbert, D. and P. Bernays, 1939, *Grundlagen der Mathematik*, vol. 2, Berlin: Springer.

[^jeroslow-1973]: Jeroslow, R., 1973, “Redundancies in the Hilbert-Bernays Derivability Conditions for Gödel’s Second Incompleteness Theorem,” *Journal of Symbolic Logic*, 38: 359–367.

[^kaye-1991]: Kaye, R., 1991, *Models of Peano Arithmetic* (Oxford Logic Guides), Oxford: Clarendon Press.

[^kirby-1982]: Kirby, L. and J. Paris, 1982, “Accessible Independence Results for Peano Arithmetic,” *Bull. London. Math. Soc.*, 14: 285–93.

[^kleene-1936]: Kleene, S.C., 1936, “General recursive functions of natural numbers,”, *Mathematische Annalen* 112(1): 727–742.

[^kleene-1937a]: –––,1937a, “Review of Perelman 1936,” *Journal of Symbolic Logic*, 2: 40–41.

[^kleene-1937b]: –––, 1937b, “Review of Helmer 1937,” *Journal of Symbolic Logic*, 2: 48–49.

[^kleene-1986]: –––, 1986, “Introductory note to 1930b, 1931 and 1932b”, in Gödel 1986, pp. 126–141.

[^kreisel-1953]: Kreisel, G., 1953, “On a Problem of Henkin’s,” *Proc. Netherlands Acad. Sci.* 56: 405–406.

[^kreisel-1958]: –––, 1958, “Mathematical significance of consistency proofs,” *The Journal of Symbolic Logic*, 23: 159–182.

[^kreisel-1967]: –––, 1967, “Mathematical Logic: What Has it Done For the Philosophy of Mathematics?” in *Bertrand Russell: Philosopher of the Century*, R. Schoenman (ed.), London: George Allen and Unwin.

[^kruskal-1960]: Kruskal, J.B., 1960, “Well-quasi-ordering, the Tree Theorem, and Vazsonyi’s Conjecture,” *Transactions of the American Mathematical Society*, 95 (2): 210–225.

[^lindström-2001]: Lindström, P., 2001, “Penrose’s New Argument,” *Journal of Philosophical Logic*, 30(3): 241–250.

[^lucas-1961]: Lucas, J. R., 1961, “Minds, Machines, and Gödel,” *Philosophy*, 36(137): 112–137 [[available online](https://web.archive.org/web/20070819165214/http://users.ox.ac.uk/~jrlucas/Godel/mmg.html)].

[^lucas-1996]: –––, 1996, “Minds, Machines, and Gödel: A Retrospect,” in *Machines and Thought. The Legacy of Alan Turing*, Vol. 1, P.J.R. Millican and A. Clark (eds.), Oxford: Oxford University Press, 103–124.

[^löb-1955]: Löb, M. H., 1955, “Solution of a Problem of Leon Henkin,” *Journal of Symbolic Logic*, 20: 115–118.

[^mancosu-1999]: Mancosu, P., 1999, “Between Vienna and Berlin: The Immediate Reception of Gödel’s Incompleteness Theorems,” *History and Philosophy of Logic*, 20: 33–45.

[^martin-1977]: Martin, D., 1977, “Descriptive Set Theory: Projective Sets,” in *Handbook of Mathematical Logic*, J. Barwise (ed.), Amsterdam: North-Holland, 783–815.

[^martin-1988]: Martin, D. and Steel, J., 1988, “Projective Determinacy,” *Proceedings of the National Academy of Sciences*, (U.S.A.), 85: 6582–86.

[^martin-1989]: –––, 1989, “A Proof of Projective Determinacy,” *Journal of the A.M.S.*, 2: 71–125.

[^matiyasevich-1970]: Matiyasevich, Y., 1970, “Diofantovost’ perechislimykh mnozhestv,” *Dokl. Akad. Nauk SSSR*, 191(2): 297–282 (Russian). (English translation, 1970, “Enumerable sets are Diophantine,” *Soviet Math. Dokl.*, 11(2): 354–358.)

[^matiyasevich-1993]: –––, 1993, *Hilbert’s Tenth Problem*, Cambridge, MA: MIT Press.

[^milne-2007]: Milne, P., 2007, “On Gödel Sentences and What They Say,” *Philosophia Mathematica*, 15: 193–226.

[^montague-1962]: Montague, R., 1962, “Theories Incomparable with Respect to Relative Interpretability,” *The Journal of Symbolic Logic*, 27: 195–211.

[^murawski-1998]: Murawski, R., 1998, “Undefinability of Truth. The Problem of Priority: Tarski vs. Gödel,” *History and Philosophy of Logic*, 19: 153–160.

[^murawski-1999]: –––, 1999, *Recursive Functions and Metamathematics: Problems of Completeness and Decidability, Gödel’s Theorems*, Dordrecht: Kluwer.

[^musgrave-1977]: Musgrave, A., 1977, “Logicism Revisited,” *British Journal for the Philosophy of Science*, 28: 99–127.

[^nagel-1958]: Nagel, E. and J.R. Newman, 1958, *Gödel’s Proof*, New York: New York University Press.

[^odifreddi-1989]: Odifreddi, P., 1989, *Classical Recursion Theory* (Oxford Logic Guides), Amsterdam: North-Holland.

[^paris-1977]: Paris, J. and L. Harrington, 1977, “A Mathematical Incompleteness in Peano Arithmetic,” in *Handbook of Mathematical Logic*, J. Barwise (ed.), Amsterdam: North-Holland, pp. 1133–1142 [[available online](http://www.karlin.mff.cuni.cz/~krajicek/ph.pdf)].

[^paris-1978]: Paris, J. and L. Kirby, 1978, “$S_n$ Collection Schema in Arithmetic,” in *Logic Colloquium ’77*, A. McIntyre et al. (eds.), Amsterdam: North-Holland, pp. 199–209.

[^parsons-1970]: Parsons, C., 1970, “On Number Choice Schema and its Relation to Induction,” in *Intuitionism and Proof Theory*, Kino et al. (eds.), Amsterdam: North-Holland, pp. 459–473.

[^penrose-1989]: Penrose, R., 1989, *The Emperor’s New Mind: Concerning Computers, Minds, and the Laws of Physics*, New York: Oxford University Press.

[^penrose-1994]: –––, 1994, *Shadows of the Mind: A Search for the Missing Science of Consciousness*, New York: Oxford University Press

[^penrose-1995]: –––, 1995, “Beyond the Doubting of a Shadow: A Reply to Commentaries of *Shadows of the Mind*,” *Psyche*, Vol 2.

[^penrose-1997]: –––, 1997, “On understanding understanding”, *International Studies in the Philosophy of Science*, 11: 7–20.

[^perelman-1936]: Perelman, C., 1936, “L’Antinomie de M. Gödel,” *Académie Royale de Belgique. Bulletin de la Classe des Sciences* (Series 5), 22: 730–36.

[^piccinini-2003]: Piccinini, G., 2003, “Alan Turing and the Mathematical Objection,” *Minds and Machines*, 13: 23–48.

[^post-1941]: Post, E., 1941, “Absolutely Unsolvable Problems and Relatively Unsolvable Propositions: Account of an Anticipation,” published in Davis 1965, 338–433.

[^presburger-1929]: Presburger, M., 1929, “Über die Vollständigkeit eines gewissen Systems der Arithmetik ganzer Zahlen, in welchem die Addition als einzige Operation hervortritt,” *Sprawozdanie z I Kongresu Matematyków Krajów Slowiańskich*, (= Comptes-rendus du I Congrès Mathématiciens des Pays Slaves), Warsaw, pp. 92–101. English translation, 1991,“On the completeness of a certain system of arithmetic of whole numbers in which addition occurs as the only operation,” *History and Philosophy of Logic*, 12(2): 225–232.

[^pudlák-1996]: Pudlák, P., 1996, “On the Length of Proofs of Consistency,” *Collegium Logicum, Annals of the Kurt-Gödel-Society*, 2: 65–86.

[^pudlák-1999]: –––, 1999, “A Note on Applicability of the Incompleteness Theorem to Human Mind,” *Annals of Pure and Applied Logic*, 96: 335–342.

[^putnam-1960]: Putnam, H., 1960, “Minds and machines,” in *Dimensions of Mind*, S. Hook (ed.), New York: New York University Press. Reprinted in H. Putnam, 1975, *Mind, Language, and Reality. Philosophical Papers, Vol 2*, Cambridge: Cambridge University Press, pp. 325–341.

[^putnam-1975]: –––, 1975, “What is Mathematical Truth?” *Historia Mathematica*, 2: 529–545. Reprinted in H. Putnam, 1975, *Mathematics, Matter and Method. Philosophical Papers, Vol 1*, Cambridge: Cambridge University Press, pp. 60–78.

[^quine-1978]: Quine, W.V. and J.S. Ullian, 1978, *The Web of Belief*, 2ⁿᵈ ed., New York: Random House.

[^raatikainen-2005]: Raatikainen, P., 2005, “On the Philosophical Relevance of Gödel’s Incompleteness Theorems,” *Revue Internationale de Philosophie*, 59: 513–534.

[^ramsey-1930]: Ramsey, F. P., 1930, “On a Problem of Formal Logic,” *Proceedings of the London Mathematical Society*, series 2, 30: 264–286.

[^ricketts-1995]: Ricketts, T., 1995, “Carnap’s Principle of Tolerance, Empiricism, and Conventionalism,” in *Reading Putnam*, P. Clark & B. Hale (eds.), Cambridge: Blackwell, pp. 176–200.

[^rodríguez-consuegra-1993]: Rodríguez-Consuegra, F., 1993, “Russell, Gödel and Logicism,” in *Philosophy of Mathematics*, J. Czermak (ed.), Vienna: Hölder-Pichler-Tempsky, pp. 233–42. Reprinted in, 1998, *Bertrand Russell: Critical Assessments*, A. Irvine (ed.), vol. 2: *Logic and mathematics*, London: Routledge, pp. 320–29.

[^roeper-2003]: Roeper, P., 2003, “Giving an Account of Provability within a Theory,” *Philosophia Mathematica*, 11: 332–340.

[^rosser-1936]: Rosser, J. B., 1936, “Extensions of Some Theorems of Gödel and Church,” *Journal of Symbolic Logic*, 1: 87–91.

[^rosser-1938]: –––, 1938, “Review: Kurt Grelling, *Gibt es eine Godelsche Antinomie?* [Grelling 1937/8],” *Journal of Symbolic Logic*, 3(2): 86.

[^searle-1997]: Searle, J., 1997, “Roger Penrose, Kurt Gödel, and the Cytoskeletons,” in J. Searle: *Mystery of Consciousness*, New York: New York Review of Books, pp. 55–93.

[^shapiro-1998]: Shapiro, S., 1998, “Incompleteness, Mechanism, and Optimism,” *Bulletin of Symbolic Logic*, 4: 273–302.

[^shapiro-2003]: –––, 2003, “Mechanism, Truth and Penrose’s New Argument,” *Journal of Philosophical Logic*, 32(1): 19–42.

[^simpson-1985]: Simpson, S.G., 1985, “Nonprovability of Certain Combinatorial Properties of Finite Trees,” in *Harvey Friedman’s Research on the Foundations of Mathematics*, L. Harrington et al. (eds.), Studies in Logic and the Foundations of Mathematics, Amsterdam: North-Holland, pp. 87–117

[^simpson-1999]: –––, 1999, *Subsystems of Second Order Arithmetic*, Berlin: Springer.

[^skolem-1930]: Skolem, T., 1930, “Über einige Satzfunktionen in der Arithmetik,” *Skrifter utgitt av Det Norske Videnskaps-Akademi i Oslo*, I, no. 7, 1–28. Reprinted in T. Skolem, 1970, *Selected Works in Logic*, (J. Fenstad, editor), Oslo: Universitetsforlaget, pp. 281–306.

[^smoryński-1977]: Smoryński, C., 1977, “The Incompleteness Theorems,” in *Handbook of Mathematical Logic*, J. Barwise (ed.), Amsterdam: North-Holland, pp. 821–865.

[^smoryński-1981]: –––, 1981, “Fifty Years of Self-reference in Arithmetic,” *Notre Dame Journal of Formal Logic*, 22(4): 357–374.

[^smoryński-1991]: –––, 1991, “The Development of Self-reference: Löb’s Theorem,” in *Perspectives on the History of Mathematical Logic*, T. Drucker (ed.), Birkhauser, pp. 111–133.

[^smullyan-1992]: Smullyan, R., 1992, *Gödel’s Incompleteness Theorems*, Oxford: Oxford University Press.

[^solovay-1970]: Solovay, R.M., 1970, “A Model of Set Theory in which Every Set of Reals is Lebesgue Measurable,” *Annals of Mathematics*, 92: 1–56.

[^sternfeld-1976]: Sternfeld, R., 1976, “The Logistic Thesis,” in *Studien zu Frege/Studies on Frege I*, M. Schirn (ed.), Stuttgart-Bad Cannstatt: Frommann-Holzboog, pp. 139–160.

[^tarski-1948]: Tarski, A., 1948, *A Decision Method for Elementary Algebra and Geometry*, manuscript. Santa Monica, CA: RAND Corp., 1948. Republished as *A Decision Method for Elementary Algebra and Geometry*, 2nd ed. Berkeley, CA: University of California Press, 1951.

[^tarski-1953]: Tarski, A., A. Mostowski, and R.M. Robinson, 1953, *Undecidable Theories*, Amsterdam: North-Holland.

[^tennant-2008]: Tennant, Neil, 2008, “Carnap, Gödel, and the Analyticity of Arithmetic”, *Philosophia Mathematica*, 16: 100–112.

[^turing-1936]: Turing, A.M., 1936–7, “On Computable Numbers, with an Application to the *Entscheidungsproblem*,” *Proceedings of the London Mathematical Society*, Series 2, 42: 230–265; correction, *ibid.*, 43: 544–546. Republished in Davis 1965, 115–154.

[^van-1967]: Van Heijenoort, J. (ed.), 1967, *From Frege to Gödel: A Source Book in Mathematical Logic, 1879–1931*, Cambridge, MA: Harvard University Press.

[^visser-2011]: Visser, A., 2011, “Can We Make the Second Incompleteness Theorem Coordinate Free,” *Journal on Logic and Computation*, 21(4): 543–560.

[^woodin-1988]: Woodin, H., 1988, “Supercompact Cardinals, Sets of Reals, and Weakly Homogeneous Trees,” *Proceedings of the National Academy of Sciences*, (U.S.A.), 85: 6587–91.

[^wright-1994]: Wright, C., 1994, “About ‘The Philosophical Significance of Gödel’s Theorem’: Some Issues,” in *The Philosophy of Michael Dummett*, B. McGuinness and G. Oliveri (eds.) Dordrecht: Kluwer, pp. 167–202.

[^wright-1995]: –––, 1995, “Intuitionists are not (Turing) Machines,” *Philosophia Mathematica*, 3: 86–102.

[^zach-2005]: Zach, R., 2005, “Paper on the Incompleteness Theorems,” in *Landmark Writings in Western Mathematics*, I. Grattan-Guinness (ed.), Amsterdam: Elsevier, pp. 917–25 [[available online](https://philarchive.org/rec/ZACKGP)].
