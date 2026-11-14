# The Notation in *Principia Mathematica*
**First published Thu Aug 19, 2004; substantive revision Tue Apr 7, 2026**

*Linsky, Bernard*

*Principia Mathematica* [PM] by A.N. Whitehead and Bertrand Russell, published 1910–1913 in three volumes by Cambridge University Press, contains a derivation of large portions of mathematics using notions and principles of symbolic logic. The notation in that work has been superseded by the subsequent development of logic during the 20ᵗʰ century, to the extent that the beginner has trouble reading PM at all. This article provides an introduction to the symbolism of PM, showing how that symbolism can be translated into a more contemporary notation using concepts which should be familiar to anyone who has had a first course in symbolic logic or set theory. This translation is offered as an aid to learning the original notation, which itself is a subject of scholarly dispute, and embodies substantive logical doctrines so that it cannot simply be replaced by contemporary symbolism. Learning the notation, then, is a first step to learning the distinctive logical doctrines of *Principia Mathematica*.

## 1. Why Learn the Symbolism in *Principia Mathematica?*

*Principia Mathematica* [PM] was written jointly by Alfred North Whitehead and Bertrand Russell over several years, and published in three volumes, which appeared between 1910 and 1913. It presents a system of symbolic logic and then turns to the foundations of mathematics to carry out the logicist project of defining mathematical notions in terms of logical notions and proving the fundamental axioms of mathematics as theorems of logic. While hugely important in the development of logic, philosophy of mathematics and more broadly of “Early Analytic Philosophy”, the work itself is no longer studied for these topics. As a result the very notation of the work has become alien to contemporary students of logic, and that has become a barrier to the study of *Principia Mathematica*. We include a series of definitions of notions such as transfinite cardinal numbers, well-orderings, rational and real numbers. These are defined differently in the theory of types of PM than than in axiomatic set theory.

This entry is intended to assist the student of PM in reading the symbolic portion of the work. What follows is a partial translation of the symbolism into a more contemporary notation, which should be familiar from other articles in this Encyclopedia, and which is quite standard in contemporary textbooks of symbolic logic. No complete algorithm is supplied, rather various suggestions are intended to help the reader learn the symbolism of PM. Many issues of interpretation would be prejudged by only using contemporary notation, and many details that are unique to PM depend on that notation. It will be seen below, with some of the more contentious aspects of the notation, that doctrines of substance are built into the notation of PM. Replacing the notation with a more modern symbolism would drastically alter the very content of the book.

## 2. Primitive Symbols of Mathematical Logic (Part I)

Below the reader will find, in the order in which they are introduced in PM, the following symbols, which are briefly described. More detail is provided in what follows:

| ∗ | pronounced “star”; indicates a number, or chapter, as in ∗1, or ∗20. |
| --- | --- |
| · | a centered dot (an old British decimal point); indicates a numbered sentence in the order by first digit (all the 0s preceding all the 1s etc.), then second digit, and so on. The first definitions and propositions of ∗1 illustrate this “lexicographical” ordering: 1·01, 1·1, 1·11, 1·2, 1·3, 1·4, 1·5, 1·6, 1·7, 1·71, 1·72. |
| $\vdash$ | the assertion-sign; precedes an *assertion*, either an *axiom* (i.e., a *primitive proposition*, which are also annotated “$\Pp$”) or a *theorem*. |
| $\Df$ | the definition sign; follows a *definition*. |
| $.$,   $:$,   $:.$,   $::$,  etc. | are dots used for delimiting punctuation; in contemporary logic, we use ( ), [ ], $\{\ \}$, etc. |
| $p, q, r$, etc. | are *propositional variables*. These appear almost exclusively as free variables. There is no formal theory of propositions in PM beyond the propositional logic of ∗1 to ∗5. |
| $\lor$, $\supset$, $\osim$, $\equiv$ and . , :, :., etc. | are the familiar sentential *connectives*, corresponding to “*or*”, “*if-then*”, “*not*”, “*if and only if*”, and “*and*” respectively. (The dual use of dots for conjunction and punctuation will be explained below.) In the Second Edition of PM, 1925–27, the Sheffer Stroke “$\mid$” is the one primitive connective. It means “*not both* … *and* ___”. |
| $x, y, z$, *w* etc. | are *individual variables*, which are to be read with “typical ambiguity”, i.e., with their *logical types* to be filled in (see §6 below). |
| $a, b, c$, etc. | are also *individual variables*, but are used almost always as free variables. This allows them to be used as *constants* (see §6 below). |
| $xRy, aRb, R(x)$, etc. | are *atomic predications*, in which the objects named by the variables or constants stand in the relation $R$ or have the property $R$. The predications $R(x), R(x,y)$, etc., are used in Second Edition to the stand for the *universals* that are constituents of *atomic facts.* |
| $\phi$, $\psi$, $\chi$, etc., and $f, g$, etc. | are higher-order variables which range over *propositional functions*, no matter whether those functions are simple or complex. |
| $\phi x$, $\psi x$, $\phi(x,y)$, etc. | open atomic formulas in which both “$x$” and “$\phi$” are free. [An alternative interpretation is to view “$\phi x$” as a schematic letter standing for a formula in which the variable “$x$” is free.] |
| $\hat{\phantom{x}}$ | the circumflex; when placed over a variable in an open formula (as in “$\phi \hat{x}$”) results in a term for a function. [This matter is controversial. See Landini 1998.][^landini-1998] When the circumflected variable precedes a complex variable, the result indicates a class, as in $\hat{x}\phi x$ which is the class of $ x $ which are $ \phi $, $ \{ x \mid \phi x\} $ in modern notation. |
| $\phi\hat{x}, \psi\hat{x}, \phi(\hat{x},\hat{z}),$ etc. | Terms for propositional functions. Here are examples of such terms which are constants: “$\hat{x}$ is happy”, “$\hat{x}$ is bald and $\hat{x}$ is happy”, “$4 \lt \hat{x} \lt 6$”, etc. If we apply, for example, the function “$\hat{x}$ is bald and $\hat{x}$ is happy” to the particular individual $b$, the result is the proposition “$b$ is bald and $b$ is happy”. |
| $\exists$ and ( ) | are the *quantifiers* “there exists” and “for all” (“every”), respectively. For example, where $\phi x$ is a simple or complex open formula, <table class="cellpad-med"> <tbody> <tr> <td>$(\exists x)\phi x$</td> <td>asserts</td> <td>&ldquo;there exists an $x$ such that $\phi x$&rdquo;</td> </tr> <tr> <td>$(\exists \phi)\phi x$</td> <td>asserts</td> <td>&ldquo;there exists a propositional function $\phi$ such that $\phi x$&rdquo;</td> </tr> <tr> <td>$(x)\phi x$</td> <td>asserts</td> <td>&ldquo;every $x$ is such that $\phi x$&rdquo;</td> </tr> <tr> <td>$(\phi)\phi x$</td> <td>asserts</td> <td>&ldquo;every propositional function $\phi$ is such that $\phi x$&rdquo;</td> </tr> </tbody> </table> [These were used by Peano. More recently, $\forall$ has been added for symmetry with $\exists$. Some scholars see the quantfiers $(\phi)$ and $(\exists \phi$) as substitutional.] |
| $\phi x \supset_x \psi x$ $\phi x \equiv_x \psi x$ | This is notation that is used to abbreviate universally quantified variables. In modern notation, these become $\forall x(\phi x \supset \psi x)$ and $\forall x(\phi x \equiv \psi x)$, respectively. See the definitions for this notation at the end of Section 3.2 below. |
| $\bang$ | pronounced “shriek”; indicates that a function is *predicative*, as in $\phi \bang x$ or $\phi\bang \hat{x}$. See Section 7. |
| = | the identity symbol; expresses *identity*, which is a defined notion in PM, not primitive as in contemporary logic. |
| $\atoi$ | read as “the”; is the inverted *iota* or *description operator* and is used in expressions for definite descriptions, such as $(\atoi x)\phi x$ (which is read: the $x$ such that $\phi x$). |
| [$(\atoi x)\phi x$] | a definite description in brackets; this is a *scope indicator* for definite descriptions. |
| $E\bang$ | is defined at ∗14·02, in the context $E\bang (\atoi x)\phi x$, to mean that the description $(\atoi x)\phi x$ is *proper*, i.e., there is one and only one thing that is $\phi$. |
| $\exists\bang$ | is defined at ∗24·03, in the context $\exists \bang \alpha$, to mean that the class $\alpha$ is *non-empty*, i.e., has a member. |

The evolution of this selection of primitive symbols out of Peano’s symbolism is traced in Elkind and Zach (2023).

## 3. The Use of Dots in PM

An immediate obstacle to reading PM is the unfamiliar use of dots for punctuation, instead of the more common parentheses and brackets. The system is precise, and can be learned with just a little practice. The use of dots for punctuation is not unique to PM. Originating with Peano, it was later used in works by Alonzo Church, W.V.O. Quine, and others, but it has now largely disappeared. Alan Turing made a study of the use of dots from a computational point of view in 1942, presumably in his spare time after a day’s work at Bletchley Park breaking the codes of the Enigma Machine. Turing suggests that the use of juxtaposition to indicate conjunction is similar to the use of juxtaposition arithmetic to indicate multiplication:

> In most systems there is some operation which is described simply by juxtaposition, without any special operator. In Church’s system this is the application of a function to its argument; in Russell’s it is conjunction and in algebra it is multiplication. (Turing 1942, 151)[^turing-1942]

In his earlier work, such as *The Principles of Mathematics,* from 1903, Russell followed Peano’s practice of indicating conjunction by simply juxtaposing formulas. Thus the conjunction of $p$ and $q $ was written $p q $. Russell began to use the punctuation dot for conjunction by 1905. The use of dots for punctuation in logic is now only of historical interest, although some textbooks use a raised dot $p \cdot q $ for conjunction. Below we will explain the dual use of dots for punctuation and conjunction in PM.

The best way to learn to use it is to look at a few samples which are translated to formulae using parentheses, and thus to get the feel for it. What follows is an explanation as presented in PM, pages 9–10, followed by a number of examples which illustrate each of its clauses:

> The use of dots. Dots on the line of the symbols have two uses, one to bracket off propositions, the other to indicate the logical product of two propositions. Dots immediately preceded or followed by “$\lor$” or “$\supset$” or “$\equiv$” or “$\vdash$”, or by “$(x)$”, “$(x,y)$”, “$(x,y,z)$” … or “$(\exists x)$”, “$(\exists x,y)$”, “$(\exists x,y,z)$” … or “$[(\atoi x)(\phi x)]$” or “$[R‘y]$” or analogous expressions, serve to bracket off a proposition; dots occurring otherwise serve to mark a logical product. The general principle is that a larger number of dots indicates an outside bracket, a smaller number indicates an inside bracket. The exact rule as to the scope of the bracket indicated by dots is arrived at by dividing the occurrences of dots into three groups which we will name I, II, and III. Group I consists of dots adjoining a sign of implication $(\supset)$ or equivalence $(\equiv)$ or of disjunction $( \lor)$ or of equality by definition $(=\Df)$. Group II consists of dots following brackets indicative of an apparent variable, such as $(x)$ or $(x,y)$ or $(\exists x)$ or $(\exists x,y)$ or $[(\atoi x)(\phi x)]$ or analogous expressions. Group III consists of dots which stand between propositions in order to indicate a logical product. Group I is of greater force than Group II, and Group II than Group III. The scope of the bracket indicated by any collection of dots extends backwards or forwards beyond any smaller number of dots, or any equal number from a group of less force, until we reach either the end of the asserted proposition or a greater number of dots or an equal number belonging to a group of equal or superior force. Dots indicating a logical product have a scope which works both backwards and forwards; other dots only work away from the adjacent sign of disjunction, implication, or equivalence, or forward from the adjacent symbol of one of the other kinds enumerated in Group II. Some examples will serve to illustrate the use of dots. (PM, 9–10)

For a deeper discussion of this passage on dot notation, see the supplement on:

[The Use of Dots for Punctuation and For Conjunction](pm-notation.dots.md).

### 3.1 Some Basic Examples

Consider the following series of extended examples, in which we examine propositions in PM and then discuss how to translate them step by step into modern notation. (Symbols below are sometimes used as names for themselves, thus avoiding some otherwise needed quotation marks. Russell is often accused of confusing use and mention, so there may well be some danger in this practice.)

#### Example 1

$$\tag*{∗1·2} {\vdash} \colon p \lor p \ldot {\supset} \ldot p \quad\Pp $$

This is the second assertion of “star” 1. It is in fact an axiom or “Primitive Proposition” as indicated by the ‘$\Pp$’. That this is an assertion (axiom or theorem) and not a definition is indicated by the use of “$\vdash$”. (By contrast, a definition would omit the assertion sign but conclude with a “$\Df$” sign.) Now the first step in the process of translating ∗1·2 into modern notation is to note the colon. Recall, from the above quoted passage, that “a larger number of dots indicates an outside bracket, a smaller number indicates an inside bracket”. Thus, the colon here (which consists of a larger number of dots than the single dots occurring on the line in ∗1·2) represents an outside bracket. The brackets “[” and “]” represent the colon in ∗1·2. The scope of the colon thus extends past any smaller number of dots (i.e., one dot) to the end of the formula. Since formulas are read from left to right the expression “past” means “to the right of”.

So, the first step is to translate ∗1·2 to:

$$ \vdash[ p \lor p \ldot {\supset} \ldot p] $$

Next, the dots around the “$\supset$” are represented in modern notation by the parenthesis around the antecedent and consequent. Recall, in the above passage, we find “… dots only work away from the adjacent sign of disjunction, implication, or equivalence …”. Thus, the next step in the translation process is to move to the formula: $$ \vdash [(p \lor p) \supset(p)] $$

Finally, standard modern conventions allow us to delete the outer brackets and the parentheses around single letters, yielding:

$$ \vdash(p \lor p) \supset p $$

Our next example involves conjunction:

#### Example 2

$$ \tag*{∗3·01} p \sdot q \ldot {=} \ldot \osim(\osim p \lor \osim q) \quad\Df $$

The dual use of dots to “indicate” conjunction and punctuation can be understood through a careful examination of the details of the paragraph on the use of dots from pages 9 to 11 of PM. Try reading the dots as punctuation first, and then, if that won’t work, those dots must indicate conjunction.

∗3·01 defines the use of dots to indicate conjunction. (That first dot, when read as punctuation would extend until an equal number of dots, namely the dot before the = sign, yielding the incoherent expression: “( $p ( q) =_\mathit{df} ( \osim (\osim p \lor \osim q) ) $”. It must, therefore, indicate a conjunction.) The dots around a sign of equality by definition $=_\mathit{df} $ are in Group I, and so the parentheses that replace them extend to the ends of the expression:

$$ (p \: .\: q) =_\mathit{df} ( \osim (\osim p \lor \osim q) ) $$ Then, we delete the outer parentheses on the right and left as unnecessary for interpreting the formula, so we have: $$ p . q =_\mathit{df} \osim (\osim p \lor \osim q) $$ in a modern notation $$ p \amp q =_\mathit{df} \osim (\osim p \lor \osim q) $$

Notice that the scope of the negation sign “$\osim$” in ∗3·01 is not indicated with dots, even in the PM system, but rather uses parentheses.

#### Example 3

$$ \tag*{∗9·01} \osim \{(x) \sdot \phi x\} \ldot {=} \ldot (\exists x) \sdot \osim \phi x \quad\Df $$

We apply the rule “dots only work away from the adjacent sign of disjunction, implication, or equivalence, or forward from the adjacent symbol of one of the other kinds enumerated in Group II” (where Group II includes “$(\exists x)$”). In this case the first dot extends to the punctuation symbol $ \} $ which is allowed optionally to replace dots. No such punctuation after the quantifier (or after the negation) occur in the modern equivalent which would be: $$ \osim (x)\phi x =_\mathit{df} (\exists x)\osim \phi x $$ or $$ \osim \forall x\phi x =_\mathit{df} \exists x\osim \phi x $$

The ranking of connectives in terms of relative “force”, or *scope*, is a standard convention in contemporary logic. If there are no explicit parentheses to indicate the scope of a connective those which have precedence in the ranking are presumed to be the principal connective, and so on for subformulas. Thus, instead formulating the following DeMorgan’s law as the cumbersome:

$$ [(\osim p) \lor (\osim q)] \equiv[\osim (p \amp q)] $$

we nowadays write it as:

$$ \osim p \lor \osim q \equiv\osim (p \amp q) $$

This simpler formulation follows from the convention that $\equiv$ has wider scope than $\lor$ and &, and the latter have wider scope than $\osim$. Indeed parentheses are often unneeded around $\equiv$, given a further convention on which $\equiv$ has wider scope than $\supset$. Thus, the formula $p \supset q \equiv\osim p\lor q$ becomes unambiguous. We might represent these conventions by listing the connectives in groups with those with widest scope at the top:

$$\begin{array}{c} \equiv \\ \supset \\ \amp, \lor \\ \osim \end{array}$$

For Whitehead and Russell, however, the symbols $\supset$, $\equiv$, $\lor$ and $\ldots =\ldots \Df$, in Group I, are of equal force. Group II consists of the variable binding expressions, quantifiers and scope indicators for definite descriptions, and Group III consists of conjunctions. Negation is below all of these. So the ranking in PM would be:

$$\begin{array}{c} \supset, \equiv, \lor \text{ and } \ldots = \ldots \quad\Df \\ (x), (x,y) \ldots (\exists x), (\exists x,y) \ldots [(\atoi x)\phi x] \\ p \sdot q \\ \osim \end{array}$$

This is what Whitehead and Russell seem to mean when they say “Group I is of greater force than Group II, and Group II than Group III.” Consider the following:

#### Example 4

$$ \tag*{∗3·12} {\vdash} \colon \osim p \ldot {\lor} \ldot \osim q \ldot {\lor} \ldot p \sdot q $$

This theorem illustrates how to read multiple uses of the same number of dots within one formula. Grouping “associates to the left” both for dots and for a series of disjunctions, following the convention of reading from left to right and the definition:

$$ \tag*{∗2·33} p \vee q \vee r \ldot {=} \ldot (p \vee q) \vee r \quad\Df $$

In ∗3·12, the first two dots around the $\lor$ simply “work away” from the connective. The second “extends” until it meets with the next of the same number (the third single dot). That third dot, and the fourth “work away” from the second $\lor$, and the final dot indicates a conjunction with least force. The result, formulated with all possible punctuation for maximum explicitness, is:

$$ \{[(\osim p) \lor (\osim q)] \lor (p \amp q)\} $$

If we employ all the standard conventions for dropping parentheses, this becomes:

$$ (\osim p \lor \osim q) \lor (p \amp q) $$

This illustrates the passage in the above quotation which says “The scope of the bracket indicated by any collection of dots extends backwards or forwards beyond any smaller number of dots, or any equal number from a group of less force, until we reach either the end of the asserted proposition or a greater number of dots or an equal number belonging to a group of equal or superior force.”

Before we look at a wider range of examples, a detailed example involving quantified variables will prove to be instructive. Whitehead and Russell follow Peano’s practice of expressing universally quantified conditionals (such as “All $\phi$s are $\psi$s”) with the bound variable subscripted under the conditional sign. Similarly with universally quantified biconditionals (“All and only $\phi$s are $\psi$s”). That is, the expressions “$\phi x \supset_x \psi x$” and “$\phi x \equiv_x \psi x$” are defined as follows:

$$ \tag*{∗10·02} \phi x \supset_x \psi x \ldot {=} \ldot (x) \ldot \phi x \supset \psi x \quad\Df $$ $$ \tag*{∗10·03} \phi x \equiv_x \psi x \ldot {=} \ldot (x) \ldot \phi x \equiv \psi x \quad\Df $$

and correspond to the following more modern formulas, respectively:

$$ \forall x(\phi x \supset \psi x) $$ $$ \forall x(\phi x \equiv \psi x) $$

As an exercise the reader might be inclined to formulate a rigorous algorithm for converting PM into a particular contemporary symbolism (with conventions for dropping parentheses), but the best way to learn the system is to look over a few more examples of translations, and then simply begin to read formulae directly.

### 3.2 More Examples

In the examples below, each formula number is followed first by *Principia* notation and then its modern translation. Notice that in ∗1·5 parentheses are used for punctuation in addition to dots. (Primitive Propositions ∗1·2, ∗1·3, ∗1·4, ∗1·5, and ∗1·6 together constitute the axioms for propositional logic in PM.) Proposition ∗1·5 was shown to be redundant by Paul Bernays in 1926. It can be derived from appropriate instances of the others and the rule of modus ponens.

| ∗1·3 | ${\vdash} \colon q \ldot {\supset} \ldot p \lor q \quad\Pp$ $q \supset p \lor q$ |
| --- | --- |
| ∗1·4 | ${\vdash} \colon p \lor q \ldot {\supset} \ldot q \lor p \quad\Pp$ $p \lor q \supset q \lor p$ |
| ∗1·5 | ${\vdash} \colon p \lor (q \lor r ) \ldot {\supset} \ldot q \lor (p \lor r ) \quad\Pp$ $p \lor (q \lor r ) \supset q \lor (p \lor r )$ |
| ∗1·6 | ${\vdash} \colondot q \supset r \ldot {\supset} \colon p \lor q \ldot {\supset} \ldot p \lor r \quad\Pp$ $(q \supset r ) \supset(p \lor q \supset p \lor r )$ |
| ∗2·03 | ${\vdash} \colon p \supset \osim q \ldot {\supset} \ldot q \supset\osim p$ $(p \supset\osim q) \supset(q \supset\osim p)$ |
| ∗3·3 | ${\vdash} \colondot p \sdot q \ldot {\supset} \ldot r \colon {\supset} \colon p \ldot {\supset} \ldot q \supset r$ $[(p \amp q) \supset r] \supset [p \supset(q \supset r)]$ |
| ∗4·15 | ${\vdash} \colondot p \sdot q \ldot {\supset} \ldot \osim r \colon {\equiv} \colon q \sdot r \ldot {\supset} \ldot \osim p$ $[(p \amp q )\supset\osim r ] \equiv [(q \amp r )\supset\osim p ]$ |

| ∗5·71 | ${\vdash} \colondot q \supset\osim r \ldot {\supset} \colon p \lor q \sdot r \ldot {\equiv} \ldot p \sdot r$ $(q \supset\osim r) \supset \{ [(p \lor q) \amp r ] \equiv (p \amp r) \}$ |
| --- | --- |
| ∗9·04 | $p \ldot {\lor} \ldot (x) \ldot \phi x \colon {=} \ldot (x) \ldot \phi x \lor p \quad\Df$ $p \lor \forall x\phi x =_\mathit{df} \forall x(\phi x \lor p)$ |

| ∗9·521 | ${\vdash} \colons (\exists x) \ldot \phi x \ldot {\supset} \ldot q \colon {\supset} \colondot (\exists x) \ldot \phi x \ldot {\lor} \ldot r \colon {\supset} \ldot q \lor r$ [$(\exists x\phi x) \supset q] \supset [((\exists x\phi x) \lor r) \supset (q \lor r)$] |
| --- | --- |
| ∗10·55 | ${\vdash} \colondot (\exists x) \ldot \phi x \sdot \psi x \colon \phi x \supset_x \psi x \colon {\equiv} \colon (\exists x) \ldot \phi x \colon \phi x \supset_x \psi x$ $\exists x(\phi x \amp \psi x) \amp \forall x(\phi x \supset \psi x) \equiv \exists x\phi x \amp \forall x(\phi x \supset \psi x)$ |

Notice that there are two uses of double dots ‘:’ in ∗10·55 to indicate conjunctions.

## 4. Propositional Functions

There are two kinds of functions in PM. Propositional functions such as “$\hat{x}$ is a natural number” are to be distinguished from the more familiar mathematical functions, which are called “descriptive functions” (PM, Chapter $\ast$31). Descriptive functions are defined using relations and definite descriptions. Examples of descriptive functions are $x + y$ and “the successor of $n$”.

Focusing on propositional functions, Whitehead and Russell distinguish between expressions with a free variable (such as “$x$ is hurt”) and names of functions (such as “$\hat{x}$ is hurt”) (PM, 14–15). The propositions which result from the formula by assigning allowable values to the free variable “$x$” are said to be the “ambiguous values” of the function. Expressions using the circumflex notation, such as $\phi \hat{x}$ only occur in the introductory material in the technical sections of PM and not in the technical sections themselves (with the exception of the sections on the theory of classes), prompting some scholars to say that such expressions do not really occur in the formal system of PM. This issue is distinct from that surrounding the interpretation of such symbols. Are they “term-forming operators” which turn an open formula into a name for a function, or simply a syntactic device, a placeholder, for indicating the variable for which a substitution can be made in an open formula? If they are to be treated as term-forming operators, the modern notation for $\phi \hat{x}$ would be $\lambda x\phi x$. The $\lambda$-notation has the advantage of clearly revealing that the variable $x$ is *bound* by the term-forming operator $\lambda$, which takes a predicate $\phi$ and yields a term $\lambda x\phi x$ (which in some logics is a singular term that can occur in the subject position of a sentence, while in other logics is a complex predicative expression). Unlike $\lambda$-notation, the PM notation using the circumflex cannot indicate scope. The function expression “$\phi(\hat{x},\hat{y}$)” is ambiguous between $\lambda x\lambda y\phi xy$ and $\lambda y\lambda x\phi xy$, without some further convention. Indeed, Whitehead and Russell specified this convention for relations in extension (on p. 200 in the introductory material of ∗21, in terms of the order of the variables), but the ambiguity is brought out most clearly by using $\lambda$ notation: the first denotes the relation of being an $x$ and $y$ such that $\phi xy$ and the second denotes the converse relation of being a $y$ and $x$ such that $\phi xy$.

## 5. The Missing Notation for Types and Orders

This section explains notation that is not in *Principia Mathematica*. Except for some notation for “relative” types in $\ast 63$, and again in early parts of Volume II, there are famously no symbols for types in *Principia Mathematica*! Sentences are generally to be taken as “typically ambiguous” and so standing for expressions of a whole range of types and so just as there are no individual or predicate constants, there are no particular functions of any specific type. The project of PM is to reduce mathematics to logic, and part of the view of logic behind this project is that logical truths are all completely general. The derivation of truths of mathematics from definitions and truths of logic will thus not involve any particular constants other than those introduced by definition from purely logical notion. As a result no notation is included in PM for describing those types. Those of us who wish to consider PM as a logic which can be applied, must supplement it with some indication of types.

Readers should note that the explanation of types outlined below is not going to correspond with the statements about types in the text of PM. Alonzo Church [1976] developed a simple, rational reconstruction of the notation for both the simple and ramified theory of types as implied by the text of PM. (There are alternative, equivalent notations for the theory of types.) The full theory can be seen as a development of the *simple theory of types*.

### 5.1 Simple Types

A definition of the simple types can be given as follows:

- $\iota$ (Greek iota) is the type for an *individual*.
- Where $\tau_1,\ldots,\tau_n$ are any types, then $\ulcorner(\tau_1,\ldots,\tau_n)\urcorner$ is the type of a propositional function whose arguments are of types $\tau_1,\ldots,\tau_n$, respectively.
- $\ulcorner (\ ) \urcorner$ is the type of propositions.

Here are some intuitive ways to understand the definition of type. Suppose that “Socrates” names an individual. (We are here ignoring Russell’s considered opinion that such ordinary individuals are in fact classes of classes of sense data, and so of a much higher type.) Then the individual constant “Socrates” would be of type $\iota$. A monadic propositional function which takes individuals as arguments is of type $(\iota)$. Suppose that “is mortal” is a predicate expressing a property of individuals. The function “$\hat{x}$ is mortal” will be of the type $(\iota)$. A two-place or *binary* relation between individuals is of type $(\iota,\iota)$. Thus, a relation expression like “parent of” and the function “$\hat{x}$ is a parent of $\hat{z}$” will be of type $(\iota,\iota)$.

Propositional functions of type $(\iota)$ are often called “first order”; hence the name “first order logic” for the familiar logic where the variables only range over arguments of first order functions. A monadic function of arguments of type $\tau$ are of type $(\tau)$ and so functions of such functions are of type $((\tau))$. “Second order logic” will have variables for the arguments of such functions (as well as variables for individuals). Binary relations between functions of type $\tau$ are of type $(\tau,\tau)$, and so on, for relations of having more than 2 arguments. Mixed types are defined by the above. A relation between an individual and a proposition (such as “$\hat{x}$ believes that $\hat{P}$”) will be of type $(\iota,(\ ))$.

### 5.2 Ramified Types (r-types)

To construct a notation for the full ramified theory of types of PM, another piece of information must be encoded in the symbols. Church calls the resulting system one of *r-types*. The key idea of ramified types is that any function defined using quantification over functions of some given type has to be of a higher “order” than those functions. To use Russell’s example:

$\hat{x}$ has all the qualities that great generals have

is a function true of persons (i.e., individuals), and from the point of view of *simple* type theory, it has the same simple logical type as particular qualities of individuals (such as bravery and decisiveness). However, in ramified type theory, the above function will be of a higher order than those particular qualities of individuals, since unlike those particular qualities, it involves a quantification over those qualities. So, whereas the expression “$\hat{x}$ is brave” denotes a function of r-type $(\iota)/1$, the expression “$\hat{x}$ has all the qualities that great generals have” will have r-type $(\iota)/2$. In these r-types, the number after the “/” indicates the *level* of the function. The order of the functions will be defined and computed given the following definitions.

Church defines the r-types as follows:

- $\iota$ (Greek iota) is the r-type for an *individual*.
- Where $\tau_1,\ldots,\tau_m$ are any r-types and $ n $ is a positive integer, $\ulcorner(\tau_1,\ldots,\tau_m)/n\urcorner$ is an r-type; this is the r-type of a $m$-ary propositional function of *level* $n$, which has arguments of r-types $\tau_1,\ldots,\tau_m$.

The *order* of an entity is defined as follows (here we no longer follow Church, for he defines orders for variables, i.e., expressions, instead of orders for the things the variables range over):

- the order of an individual (of r-type $ \iota)$ is 0,
- the order of a function of r-type $(\tau_1,\ldots,\tau_m)/n$ is $n+N$, where $N$ is the greatest of the order of the arguments $\tau_1,\ldots,\tau_m$.

These two definitions are supplemented with a principle which identifies the levels of particular defined functions, namely, that the level of a defined function should be one higher than the highest order entity having a name or variable that appears in the definition of that function.

To see how these definitions and principles can be used to compute the order of the function “$\hat{x}$ has all the qualities that great generals have”, note that the function can be represented as follows, where “$x, y$” are variables ranging over individuals of r-type $\iota$ (order 0), “GreatGeneral$(y)$” is a predicate denoting a propositional function of r-type $(\iota)/1$ (and so of order 1), and “$\phi$” is a variable ranging over propositional functions of r-type $(\iota)/1$ (and so of order 1) such as *great general*, *bravery*, *leadership*, *skill*, *foresight*, etc.:

$$ (\phi)\{[(y)(\textrm{GreatGeneral}(y) \supset \phi(y)] \supset \phi \hat{x} \} $$

We first note that given the above principle, the r-type of this function is $(\iota)/2$; the level is 2 because the level of the r-type of this function has to be one higher than the highest order of any entity named (or in the range of a variable used) in the definition. In this case, the denotation of GreatGeneral, and the range of the variable “$\phi$”, is of order 1, and no other expression names or ranges over an entity of higher order. Thus, the level of the function named above is defined to be 2. Finally, we compute the order of the function denoted above as it was defined: the sum of the level plus the greatest of the orders of the arguments of the above function. Since the only arguments in the above function are individuals (of order 0), the order of our function is just 2.

Quantifying over functions of r-type $(\tau)/n$ of order $k$ in a definition of a new function yields a function of r-type $(\tau)/n+1$, and so a function of order one higher, $k+1$. Two kinds of functions, then, can be of the *second order*: (1) functions of first-order functions of individuals, of r-type $((\iota)/1)/1$, and (2) functions of r-type $(\iota)/2$, such as our example “$\hat{x}$ has all the qualities that great generals have”. This latter will be a function true of individuals such as Napoleon, but of a higher order than simple functions such as “$\hat{x}$ is brave”, which are of r-type $(\iota)/1$.

Logicians today use a different notion of “order”. Today, first-order logic is a logic with only variables for individuals. Second order logic is a logic with variables for both individuals and properties of individuals. Third-order logic is a logic with variables for individuals, properties of individuals, and properties of properties of individuals. And so forth. By contrast, Church would call these logics, respectively, the logic of functions of the types $(\iota)/1$ and $(\iota,\ldots,\iota)/1$, the logic of functions of the types $((\iota)/1)/1$ and $((\iota,\ldots,\iota)/1,\ldots,(\iota,\ldots,\iota)/1)/1$, and the logic of functions of the types $(((\iota)/1)/1)/1$ etc. (i.e., the level-one functions of the functions of the preceding type). Given Church’s definitions, these are logics of first-, second- and third-order functions, respectively, thus coinciding with the modern terminology of “$n$ᵗʰ-order logic”.

## 6. Variables and Constants

As mentioned previously, there are no individual or predicate constants in the formal system of PM, only variables. The Introduction, however, makes use of the example “$a$ standing in the relation $R$ to $b$” in a discussion of “elementary judgements” (PM, 43), called “atomic propositions” in the Second Edition (PM *xv*). Although “$R$” is later used as a variable that ranges over relations in extension, and “$a,b,c,\ldots$” are individual variables, let us temporarily add them to the system as predicate and individual constants, respectively, in order to discuss the use of variables in PM.

PM makes special use of the distinction between “real”, or free, variables and “apparent”, or bound, variables. Since “$x$” is a variable, “$xRy$” will be an atomic formula in our extended language, with “$x$” and “$y$” real variables. When such formulae are combined with the propositional connectives $\osim$, $\lor$, etc., the result is a *matrix*. For example, “$aRx \ldot {\lor} \ldot xRy$” would be a matrix.

As we saw earlier, there are also variables which range over functions: “$\phi$, $\psi$, $\ldots,f, g$”, etc. The expression “$\phi x$” thus contains two variables and stands for a proposition, in particular, the result of applying the function $\phi$ to the individual $x$.

Theorems are stated with real variables, which gives them a special significance with regard to the theory. For example,

$$ \tag*{∗10·1} \vdash \colon (x) \ldot \phi x \ldot {\supset} \ldot \phi y \quad\Pp $$

is a fundamental axiom of the quantificational theory of PM. In this Primitive Proposition the variables “$\phi$” and “$y$” are real (free), and the “$x$” is apparent (bound). As there are no constants in the system, this is the closest that PM comes to a rule of universal instantiation.

We find an account of constants in the comment on this theorem:

> $ \ast 10 \cdot 26 \; \; \vdash \; : . (z) . \phi z \supset \psi z : \phi x : \; \supset .\psi x \ \ \ \ \ \ \ [ \ast 10 \cdot 1, \mathrm{imp} ] $
>
> This is one form of the syllogism in Barbara. E.g. Put $\phi $ *z* = *z* is a man, $\psi $ *z* = *z* is mortal, x = Socrates. Then the proposition becomes: “If all men are mortal, and Socrates is a man, then Socrates is mortal.” (PM 144).

In the Second Edition we learn that this “putting” amounts to an assignment of objects to free individual variables that is “outside logic”:

> …constants do not occur in logic, that is to say the *a*, *b*, *c* which we have been supposing constant are to be regarded as obtained by an extra-logical assignment of values to variables. They may be absorbed into the *x*, *y*, *z*,… . (PM *xxx*)

We assume that the same account is to be given of the assignment of individuals to free variables and propositional functions to Greek (predicate) letters in the instance of Barbara above.

**Typical Ambiguity.** Whitehead and Russell interpret “$(x) \sdot \phi x$” as “the proposition which asserts *all* the values for $\phi \hat{x}$” (PM 41). The use of the word “all” has special significance within the theory of types. They present the *vicious circle principle*, which underlies the theory of types:

> … generally, given any set of objects such that, if we suppose the set to have a total, it will contain members which presuppose this total, then such as set cannot have a total. By saying that the set has “no total”, we mean, primarily, that no significant statement can be made about “all its members”. (PM 37)

Specifically, then, a quantified expression, since it talks about (presupposes) “all” the members of a totality, must express a member of a different, higher, logical type than those members in order to observe the vicious circle principle. Thus, when interpreting a bound variable, we must assume that it ranges over a specific type of entity, and so types must be assigned to the other entities represented by expressions in the formula, in observance with the theory of types.

A question arises, however, once one realizes that the statements of primitive propositions and theorems in PM such as ∗10·1 are taken to be “typically ambiguous” (i.e., ambiguous with respect to type). These statements are actually schematic and represent all the possible specific assertions which can be derived from them by interpreting types appropriately. But if statements like ∗10·1 are schemata and yet have bound variables, how do we assign types to the entities over which the bound variables range? The answer is to first decide which type of thing the free variables in the statement range over. For example, assuming that the variable $y$ in ∗10·1 ranges over individuals (of type $\iota)$, then the variable $\phi$ must range over functions of type $(\iota)/n$, for some $n$. Then the bound variable $x$ will also range over individuals. If, however, we assume that the variable $y$ in ∗10·1 ranges over *functions* of type $(\iota)/1$, then the variable $\phi$ must range over functions of type $((\iota)/1)/m$, for some $m$. In this case, the bound variable $x$ will range over functions of type $(\iota)/1$.

So $y$ and $\phi$ are called “real” variables in ∗10·1 not only because they are free but also because they can range over any type. Whitehead and Russell frequently say that real variables are taken to ambiguously denote “any” of their instances, while bound variables (which also ambiguously denote) range over “all” of their instances (within a legitimate totality, i.e. type).

> **Examples in modern notation with individual and predicate constants and r-type symbols**:
>
> **Example 1**: If all men are mortal, and Socrates is a man, then Socrates is mortal.
>
> - Vocabulary:
> - $ a^{\iota } $     (an individual constant for Socrates)
> - $ M^{( \iota)/1} x^{\iota} $     ($x$ is mortal)
> - $ H^{( \iota)/1} x^{\iota} $    ($x$ is a man (human))
> - (By convention the type of a symbol is only indicated when it first appears in a formula.)
> - The sentence is symbolized as: $ ( \forall x^{\iota} ) ( H^{( \iota)/1} x \supset M^{( \iota)/1} x )\ \&\ Ha\ \supset\ Ma $
>
> **Example 2**: If bravery is a property of all great generals and Napoleon is a great general, then Napoleon is brave.
>
> - Vocabulary:
> - $ G^{(\iota)/1}x^{\iota} $    ($x$ is a great general)
> - $ GG^{(( \iota )/1)/1} (F) $ =_{df} $(\forall z^{\iota}) \{ (\forall H^{(\iota)/1)} [ (\forall y^{\iota}) (G^{(\iota)/1} y \supset Hy ) \supset Hz] \supset F^{(\iota)/1} z \} $     ($F$ is a property possessed by all great generals)
> - $ B^{(\iota)/1}x $    ($x$ is brave)
> - $ n^{\iota} $    (Napoleon)
> - The sentence is symbolized as: $ GG^{(( \iota )/1 )/1}(B^{(\iota)/1} )\ \&\ G^{(\iota)/1 } n^{ \iota } \supset Bn $

## 7. Predicative Functions and Identity

The exclamation mark “!” following a variable for a function and preceding the argument, as in “$f\bang \hat{x}$”, “$\phi \bang x$”, “$\phi\bang \hat{x}$”, indicates that the function is *predicative*, that is, of the lowest order which can apply to its arguments. In Church’s notation, this means that predicative functions are all of the first level, with types of the form $(\ldots)/1$. As a result, predicative functions will be of order one more than the highest order of any of their arguments. This analysis is based on quotations like the following, in the *Introduction* to PM:

> We will define a function of one variable as predicative when it is of the next order above that of its argument, i.e., of the lowest order compatible with its having that argument. (PM 53)

Unfortunately in the summary of ∗12, we find “A predicative function is one which contains no apparent variables, i.e., is a matrix” [PM, 167]. Reconciling this statement with that definition in the *Introduction* is a problem for scholars.

To see the shriek notation in action, consider the following definition of identity:

$$ \tag*{∗13·01} x = y \ldot {=} \colon (\phi) \colon \phi \bang x \ldot {\supset} \ldot \phi \bang y \quad\Df $$

That is, $x$ is identical with $y$ if and only if $y$ has every predicative function $\phi$ which is possessed by $x$. (Of course the second occurrence of “=” indicates a definition, and does not independently have meaning. It is the first occurrence, relating individuals $x$ and $y$, which is defined.)

To see how this definition reduces to the more familiar definition of identity (on which objects are identical iff they share the same properties), we need the Axiom of Reducibility. The Axiom of Reducibility states that for any function there is an equivalent function (i.e., one true of all the same arguments) which is predicative:

Axiom of Reducibility: $$ \tag*{∗12·1} \vdash \colon (\exists f) \colon \phi x \ldot {\equiv_x} \ldot f\bang x \quad\Pp $$

To see how this axiom implies the more familiar definition of identity, note that the more familiar definition of identity is:

$$ x = y \ldot {=} \colon (\phi) \colon \phi x \ldot {\supset} \ldot \phi y \quad\Df $$

for $\phi$ of “any” type. (Note that this differs from ∗13·01 in that the shriek no longer appears.) Now to prove this, assume both ∗13·01 and the Axiom of Reducibility, and suppose, for proof by *reductio*, that $x = y$, and $\phi x$, and not $\phi y$, for some function $\phi$ of arbitrary type. Then, the Axiom of Reducibility ∗12·1 guarantees that there will be a predicative function $\psi \bang$, which is coextensive with $\phi$ such that $\psi \bang x$ but not $\psi \bang y$, which contradicts ∗13·01.

## 8. Definite Descriptions

The inverted Greek letter iota “$\atoi$” is used in PM, always followed by a variable, to begin a definite description. $(\atoi x) \phi x$ is read as “the $x$ such that $x$ is $\phi$”, or more simply, as “the $\phi$”. Such expressions may occur in subject position, as in $\psi(\atoi x) \phi x$, read as “the $\phi$ is $\psi$”. The formal part of Russell’s famous “theory of definite descriptions” consists of a definition of all formulas “…$\psi(\atoi x) \phi x$…” in which a description occurs. To distinguish the portion $\psi$ from the rest of a larger sentence (indicated by the ellipses above) in which the expression $\psi(\atoi x) \phi x$ occurs, the *scope* of the description is indicated by repeating the definite description within brackets:

$$ [(\atoi x) \phi x] \sdot \psi(\atoi x) \phi x $$

The notion of scope is meant to explain a distinction which Russell famously discusses in “On Denoting” (1905). Russell says that the sentence “The present King of France is not bald” is ambiguous between two readings: (1) the reading where it says of the present King of France that he is not bald, and (2) the reading which denies that the present King of France is bald. The former reading requires that there be a unique King of France on the list of things that are not bald, whereas the latter simply says that there is not a unique King of France that appears on the list of bald things. Russell says the latter, but not the former, can be true in a circumstance in which there is no King of France. Russell analyzes this difference as a matter of the scope of the definite description, though as we shall see, some modern logicians tend to think of this situation as a matter of the scope of the negation sign. Thus, Russell introduces a method for indicating the scope of the definite description.

To see how Russell’s method of scope works for this case, we must understand the definition which introduces definite descriptions (i.e., the inverted iota operator). Whitehead and Russell define:

$$ \tag*{∗14·01} [(\atoi x) \phi x] \sdot \psi(\atoi x) \phi x \ldot {=} \colon (\exists b) \colon \phi x \ldot {\equiv_x} \ldot x=b \colon \psi b \quad\Df $$

(Note that $b$ occurs here as a *bound* individual variable.) This kind of definition is called a *contextual definition*, which are to be contrasted with *explicit* definitions. An explicit definition of the definition description would have to look something like the following:

$$ (\atoi x)(\phi x) = \colon \ldots \quad\Df $$

which would allow the definite description to be replaced in any context by whichever defining expression fills in the ellipsis. By contrast, ∗14·01 shows how a sentence, in which there is occurrence of a description $(\atoi x)(\phi x)$ in a context $\psi$, can be replaced by some other sentence (involving $\phi$ and $\psi$) which is equivalent. To develop an instance of this definition, start with the following example:

Example. The present King of France is bald.

Using $PKFx$ to represent the propositional function of being a present King of France and $B$ to represent the propositional function of being bald, Whitehead and Russell would represent the above claim as:

$$ [(\atoi x)(PKFx)] \sdot B(\atoi x)(PKFx) $$

which by ∗14·01 means:

$$ (\exists b) \colon PKFx \ldot {\equiv_x} \ldot x=b \colon Bb $$

In words, there is one and only one $b$ which is a present King of France and $b$ is bald. In modern symbols, using $b$ non-standardly, as a variable, this becomes:

$$ (\exists b)[\forall x(PKFx \equiv x=b) \amp Bb] $$

Now we return to the example which shows how the scope of the description makes a difference:

Example. The present King of France is not bald.

There are two options for representing this sentence.

$$ [(\atoi x)(Kx)] \sdot \osim B(\atoi x)(Kx) $$

and

$$ \osim [(\atoi x)(Kx)] \sdot B(\atoi x)(Kx) $$

In the first, the description has “wide” scope, and in the second, the description has “narrow” scope. Russell says that the description has “primary occurrence” in the former, and “secondary occurrence” in the latter. Given the definition ∗14·01, the two PM formulas immediately above become expanded into primitive notation as:

$$ \begin{align} (\exists b) \colon PKFx \equiv_x x=b \colon \osim Bb\\ \osim (\exists b) \colon PKFx \equiv_x x=b \colon Bb \end{align} $$

In modern notation these become:

$$ \begin{align} \exists x[\forall y(PKFy \equiv y=x) \amp \osim Bx]\\ \osim \exists x[\forall y(PKFy \equiv y=x) \amp Bx] \end{align} $$

The former says that there is one and only one object which is a present King of France and this object is not bald; i.e., there is exactly one present King of France and he is not bald. This reading is false, given that there is no present King of France. The latter says it is not the case that there is exactly one thing that is a present King of France and that object is bald. This reading is true because there is not even one present King of France.

Although Whitehead and Russell take the descriptions in these examples to be the expressions which have scope, the above readings in both expanded PM notation and in modern notation suggest why some modern logicians take the difference in readings here to be a matter of the scope of the negation sign.

## 9. Classes, Relations, and Functions

The circumflex “ˆ” over a variable preceding a formula is used to indicate a class, thus $\hat{x} \psi x$ is the class of things $x$ which are such that $\psi x$. In modern notation we represent this class as $\{x \mid \psi x\}$, which is read: the class of $x$ which are such that $x$ has $\psi$. Recall that “$\phi \hat{x}$”, with the circumflex over a variable after the predicate variable, expresses the propositional function of being an $x$ such that $\phi x$. In the type theory of PM, the class $\hat{x} \phi x$ has the same logical type as the function $\phi \hat{x}$. This makes it appropriate to use the following contextual definition, which allows one to eliminate the class term $\hat{x} \psi x$ from occurrences in the context $f$: $$ \tag*{∗20·01} f\{ \hat{z}(\psi z)\} \ldot {=} \colon (\exists \phi) \colon \phi \bang x \ldot {\equiv_x} \ldot \psi x \colon f \{ \phi\bang \hat{z}\} \quad\Df $$ or in modern notation: $$ f\{z \mid \psi z\} =_\mathit{df} \exists \phi[\forall x(\phi x \equiv \psi x) \amp f(\lambda x \phi x)] $$ where $\phi$ is a predicative function of $x$

Note that $f$ has to be interpreted as a higher-order function which is predicated of the function $\phi \bang \hat{z}$. In the modern notation used above, the language has to be a typed language in which $\lambda$ expressions are allowed in argument position. As was pointed out later (Chwistek 1924, Gödel 1944, and Carnap 1947)[^carnap-1947][^chwistek-1924][^gödel-1944] there should be scope indicators for class expressions just as there are for definite descriptions. (The possibility of scope ambiguities in propositions about classes is mentioned in the final sentences of the *Introduction* (PM I, 84)). Chwistek, for example, proposed copying the notation for definite descriptions, thus replacing ∗20·01 with:

$$ [\hat{z}(\psi z)] \sdot f\{ \hat{z}(\psi z)\} \ldot {=} \colon (\exists \phi) \colon \phi \bang x \ldot {\equiv_x} \ldot \psi x \colon f \{ \phi\bang \hat{z} \} $$

Contemporary formalizations of set theory make use of something like these contextual definitions, when they require an “existence” theorem of the form $\exists x\forall y(y \in x \equiv \ldots y\ldots)$, in order to justify the introduction of a singular term $\{y \mid \ldots y\ldots \}$. See Suppes (1960). Given the law of extensionality, it follows from $\exists x\forall y(y \in x \equiv \ldots y\ldots)$ that there is a unique such set. The relation of membership in classes $\in$ is defined in PM by first defining a similar relationship between objects and propositional functions: $$ \tag*{∗20·02} x \in (\phi\bang \hat{z}) \ldot {=} \ldot \phi \bang x \quad\Df $$ or, in modern notation: $$ x \in \lambda z\phi z =_\mathit{df} \phi x $$

∗20·01 and ∗20·02 together are then used to define the more familiar notion of membership in a class. The formal expression “$y \in \{ \hat{z}(\phi z)\}$” can now been seen as a context in which the class term occurs; it is then eliminated by the contextual definition ∗20·01. (Exercise)

In PM there is a class of all classes, Cls, defined as: $$ \tag*{∗20·03} \Cls = \hat{\alpha} \{ (\exists \phi ). \alpha = \hat{z} ( \phi ! z) \} \quad\Df $$

PM also has Greek letters for classes: $\alpha, \beta, \gamma$, etc. These will appear as real (free) variables, apparent (bound) variables and in abstracts for propositional functions true of classes, as in $\phi \hat{\alpha}$. Only definitions of the bound Greek variables appear in the body of the text, the others are informally defined in the *Introduction*: $$ \tag*{∗20·07} (\alpha) \sdot f \alpha \ldot {=} \ldot (\phi) \sdot f \{ \hat{z}(\phi\bang z)\} \quad\Df $$ or, in modern notation, $$ \forall \alpha\, f\alpha =_\mathit{df} \forall \phi f\{z\mid\phi z\} $$ where $\phi$ is a predicative function.

Thus universally quantified class variables are defined in terms of quantifiers ranging over predicative functions. Likewise for existential quantification: $$ \tag*{∗20·071} (\exists \alpha) \sdot f \alpha \ldot {=} \ldot (\exists \phi) \sdot f \{ \hat{z}(\phi\bang z)\} \quad\Df $$ or, in modern notation, $$ \exists \alpha\, f\alpha =_\mathit{df} \exists \phi f\{z\mid\phi z\} $$ where $\phi$ is a predicative function.

Expressions with a Greek variable to the left of $\in$ are defined: $$ \tag*{∗20·081} \alpha \in \psi\bang \hat{\alpha} \ldot {=} \ldot \psi \bang \alpha \quad\Df $$

These definitions do not cover all possible occurrences of Greek variables. In the Introduction to PM, further definitions of $f \alpha$ and $f \hat{\alpha}$ are proposed, but it is remarked that the definitions are in some way peculiar and they do not appear in the body of the work. The definition considered for $f \hat{\alpha}$ is:

$$ f \hat{\alpha} \ldot {=} \ldot (\exists \psi) \sdot \hat{\phi} \bang x \equiv_x \psi \bang x \sdot f \{ \psi\bang \hat{z} \} $$

or, in modern notation,

$$ \lambda \alpha\, f\alpha =_\mathit{df} \lambda \phi f\{x \mid \phi x\} $$

That is, $f \hat{\alpha}$ is an expression naming the function which takes a function $\phi$ to a proposition which asserts $f$ of the class of $\phi$s. (The modern notation shows that in the proposed definition of $f \hat{\alpha}$ in PM notation, we shouldn’t expect $\alpha$ in the definiens, since it is really a bound variable in $f \hat{\alpha}$; similarly, we shouldn’t expect $\phi$ in the definiendum because it is a bound variable in the definiens.) One might also expect definitions like ∗20·07 and ∗20·071 to hold for cases in which the Roman letter “$z$” is replaced by a Greek letter. The definitions in PM are thus not complete, but it is possible to guess at how they would be extended to cover all occurrences of Greek letters. This would complete the project of the “no-classes” theory of classes by showing how all talk of classes can be reduced to the theory of propositional functions.

## 10. Concluding Mathematical Logic

Although students of philosophy usually read no further than ∗20 in PM, this is in fact the point where the “construction” of mathematics really begins. ∗21 presents the “General Theory of Relations” (the theory of relations in extension; in contemporary logic these are treated as sets of ordered pairs, following Wiener). $\hat{x} \hat{y} \psi(x, y)$ is the relation between $x$ and $y$ which obtains when $\psi(x, y)$ is true. In modern notation we represent this as as the set of ordered pairs $\{\langle x, y \rangle \mid \psi(x, y)\}$, which is read: the set of ordered pairs $\langle x, y \rangle$ which are such that $x$ bears the relation $\psi$ to $y$.

The following contextual definition (∗21·01) allows one to eliminate the relation term $\hat{x} \hat{y}\psi (x, y)$ from occurrences in the context $f$:

$$ f \{ \hat{x} \hat{y} \psi ( x, y )\} \ldot {=} \colondot (\exists \phi) \colon \phi \bang ( x, y ) \ldot {\equiv_{x,y}} \ldot \psi( x,y ) \colon f \{ \phi\bang (\hat{u}, \hat{v} )\} \quad\Df $$

or in modern notation:

$$ f \{\langle x, y \rangle \mid \psi( x, y )\} =_\mathit{df} \exists \phi[\forall xy (\phi(x, y) \equiv \psi( x, y) ) \amp f ( \lambda u \lambda v \phi(u,v))] $$

where $\phi$ is a predicative function of $u$ and $v$.

*Principia* does not analyze relations (or mathematical functions) in terms of sets of ordered pairs, but rather takes the notion of propositional function as primitive and defines relations and functions in terms of them. The upper case letters ${R}, {S}$ and ${T}$, etc., are used after ∗21 to stand for these “relations in extension”, and are distinguished from propositional functions by being written between the arguments. Thus it is $\psi(x,y)$ with arguments after the propositional function symbol, but $xRy$. From ∗21 functions “$\phi$ and $\psi$”, etc., disappear and only relations in extension, ${R}$, ${S}$ and ${T}$, etc., appear in the pages of *Principia*. While propositional functions might be “intensional”, that is two functions may be true of the same objects yet not be identical, no distinct relations in extension are true of all the same objects. The logic of *Principia* is thus “extensional”, from page 200 in volume I, through to the end in Volume III.

∗22 on the “Calculus of Classes” presents the elementary set theory of intersections, unions and the empty set which is often all the set theory used in elementary mathematics of other sorts. The student looking for the set theory of *Principia* to compare it with, say the Zermelo-Fraenkel system, will have to look at various numbers later in the text. The Axiom of Choice is defined at ∗88 as the “Multiplicative Axiom” and a version of the Axiom of Infinity appears at ∗120 in Volume II as “Infin ax”. The set theory of *Principia* comes closest to Zermelo’s axioms of 1908 among the various familiar axiom systems, which means that it lacks the Axiom of Foundation and Axiom of Replacement of the now standard Zermelo-Fraenkel axioms of set theory. The system of *Principia* differs importantly from Zermelo’s in that it is formulated in the simple theory of types. As a result, for example, there are no quantifiers ranging over all sets, and there is a set of all things (for each type).

∗30 on “Descriptive Functions” provides Whitehead and Russell’s analysis of mathematical functions in terms of relations and definite descriptions. Frege had used the notion of function, in the mathematical sense, as a basic notion in his logical system. Thus a Fregean “concept” is a function from objects as arguments to one of the two “truth values” as its values. A concept yields the value “True” for each object to which the concept applies, and “False” for all others. Russell, from well before discovering his theory of descriptions, had preferred to analyze functions in terms of the relation between each argument and value, and the notion of “uniqueness”. With modern symbolism, his view would be expressed as follows. For each function $\lambda x f(x)$, there will be some relation (in extension) $R$, such that the value of the function for an argument $a$, that is $f(a)$, will be the unique individual which bears the relation $R$ to $a$. The result is that there are no function symbols in *Principia*. As Whitehead and Russell say, the familiar mathematical expressions such as “$\sin \pi/2$” will be analyzed with a relation and a definite description, as a “descriptive function”. The “descriptive function”, $R‘y$ (the $R$ of $y)$, is defined as follows:

$$ \tag*{∗30·01} R‘y = (\atoi x)xRy \quad\Df $$

If the relation $R$ is between persons $ x $ and $ y $ when $ x $ is the father of $ y $ then the function will take an individual $y $ as argument to the value $x $ as their father. For instance, if $xRy$ is the relation ‘$x$ is father of $y$’, then R‘$y$ is the function which maps $y$ to the father of $y$ (if he exists). Note that here the left argument $x$ corresponds to the value of the function, whereas the right argument $y$ of R is the argument, or input, to the function R‘$y$. Likewise if $xSy$ is the relation of a number to its successor, $n$ to $n + 1$, then S‘$y$ would be the argument of the function which maps $y$ to the number that it succeeds, rather than expressing the “successor function” which maps a number to its successor. This is the reverse of the order that is now commonly used when relating functions and relations. Nowadays we reduce functions to a binary relation between the argument in the first place and value in the second place. This may lead to some confusion in the definitions of notions such as the *domain* and *range* of a relation below.

We conclude this section by presenting a number of prominent examples from these remainder of Volume I, with their intuitive meaning, location in PM, definition in PM, and a modern version. (Some of these numbers are theorems rather than definitions.) Note, however, that the modern formulations will sometimes logically differ from the original version in PM, such as by treating relations as classes of ordered pairs, etc. More prominent is the practice in PM of defining notions as relations, or higher order relations between relations, rather than as functions determined by those relations. In his account of the logic of *Principia*, W.V. Quine (1951) objects to the complexity and even redundancy of much of this symbolism in comparison with axiomatic set theory. These formulas can be worked out, however, with a step by step application of the definitions.

For each formula number, we present the information in the following format:

| PM Symbol | (Intuitive Meaning)   [Location] PM Definition Modern Version |
| --- | --- |

$\ast 22 $ *Calculus of Classes*

| $\alpha \subset \beta$ | ($\alpha$ is a *subset* of $\beta$)    [∗22·01] $x\in \alpha \ldot {\supset_x} \ldot x\in \beta$ $\alpha \subseteq \beta$ |
| --- | --- |
| $\alpha \cap \beta$ | (the *intersection* of $\alpha$ and $\beta)$    [∗22·02] $\hat{x} (x \in \alpha \sdot x \in \beta$) $\alpha \cap \beta$ |
| $\alpha \cup \beta$ | (the *union* of $\alpha$ and $\beta$)    [∗22·03] $\hat{x} (x \in \alpha \lor x \in \beta$) $\alpha \cup \beta$ |
| $-\alpha$ | (the *complement* of $\alpha)$    [∗22·04] $\hat{x} (x\osim \in \alpha$) [i.e., $\hat{x} \osim (x \in \alpha$) by ∗20·06] $\{x \mid x \not\in \alpha \}$ |
| $\alpha - \beta$ | ($\alpha$ *minus* $\beta)$    [∗22·05] $\alpha \cap -\beta$ $\{x \mid x\in \alpha \amp x\not\in \beta \}$ |

$\ast 23 $ *Calculus of Relations*

| $R \: \subset \! \! \! · \: S$ | ($R$ is a *subrelation* $S$)    [∗23·01]   $xRy \: . \supset_{x,y} \: . xSy $ $\forall x \forall y (x R y \: \supset \: x S y)$ |
| --- | --- |
| $R \: \dot{\cap} \: S$ | (the *intersection* of $R$ and $S$)    [∗23·02] $\hat{x}\hat{y} (x R y \: . \: x S y)$ $\{\langle x, y \rangle &#124; Rxy \; \amp \; Sxy \}$ |
| $ \dot{-} R $ | (the *negation* of $R$)    [∗23·04] $ \dot{-} R = \hat{x} \hat{y} \{ \sim (xRy) \} $ $\{\langle x, y \rangle &#124; \sim Rxy \}$ |

$\ast 24 $ *The Existence of Classes*

| $\mathrm{V}$ | (the *universal* class)    [∗ 24·01] $\hat{x} (x$ = $x)$ $\mathrm{V}$ or $\{x \mid x = x\}$ |
| --- | --- |
| $\Lambda$ | (the *empty* class)    [∗24·02] $-\mathrm{V}$ $\varnothing$ |
| $\exists! \alpha $ | (the class $ \alpha $ *exists*)    [∗24·03] $(\exists x ). x \in \alpha $ $\exists x ( x \in \alpha )$ |

$\ast 25 $ *The Existence of Relations*

| $\dot{\exists}! R$ | (the relation $R$ *exists*)    [∗25·03] $(\exists x,y) .\: xRy$ $ \exists x \exists y Rxy$ |
| --- | --- |

$\ast 30 $ *Descriptive Functions*

| $R‘y$ | (the $R$ of $y)$ (a descriptive function)    [∗30·01] ($\atoi x)(xRy)$ $R‘y$ is the (possibly partial) function where $f_R (y) = x $ if $x$ R$ y$ and this $x$ is unique, and otherwise is undefined. |
| --- | --- |

$\ast 31 $ *Converses of Relations*

| Cnv | (the relation between a relation and its *converse*)    [∗31·01] $\hat{Q} \hat{P} \{ xQy . \equiv_{x,y} . yPx \}$ $\{ \langle Q , P \rangle \: \mid \: \forall x \forall y (Qxy \equiv Pyx) \: \} $ |
| --- | --- |
| $\breve{R}$ | (the *converse* of $ R $ )    [∗31·02] $\hat{x} \hat{z} (zRx)$ $\{\langle x,z\rangle \mid Rzx\}$ |

$\ast 32 $ *Referents and Relata of a Given Term*

| $\overrightarrow{R}‘y$ | (the *R-predecessors* of $y)$    [∗32·01] $\hat{x} (xRy)$ $\{x \mid Rxy \}$ |
| --- | --- |
| $\overleftarrow{R}‘x$ | (the *R-successors* of $x)$    [∗32·02] $\hat{z} (xRz)$ $\{z \mid Rxz \}$ |

$\ast 33 $ *Domains and Fields of Relations*

| $ \text{D} ‘R$ | (the *domain* of $R)$    [∗33·01] $\hat{x} \{ (\exists y) \sdot xRy \}$ $\{x \mid \exists y Rxy \}$ also: $\mathcal{D}` R$ |
| --- | --- |
| $ \backd ‘R$ | (the *converse domain* (range) of $R)$    [∗33·02] $\hat{z} \{(\exists x) \sdot xR z \}$ $\{z \mid \exists x Rxz \}$ also $\mathcal{R}`R$ |
| $C‘R$ | (the *field* of $R)$    [∗33·03] $\hat{x} \{(\exists y): xRy \ldot {\lor} \ldot yRx\}$ $\{x \mid \exists y (Rxy \lor Ryx)\}$ also $\mathcal{F}`R$ |

$\ast 34 $ *The Relative Product of Two Relations*

| $R\mid S$ | (the *relative product* of $R$ and $S)$    [∗34·01] $\hat{x} \hat{z} \{(\exists y) \sdot xRy \sdot ySz \}$ $R \circ S$ or $\{\langle x,z\rangle \mid \exists y(Rxy \amp Syz)\}$ |
| --- | --- |

$\ast 35 $ *Limited Domains and Converse Domains*

| $\alpha \upharpoonleft R$ | (the *restriction* of the domain of $R$ to $\alpha )$    [∗35·01] $\hat{x} \hat{y}[ x\in \alpha \sdot xRy]$ $\{\langle x,y \rangle \mid x \in \alpha \amp Rxy \}$ |
| --- | --- |
| $R \restriction \beta$ | (the *restriction* of the range of $R$ to $\beta)$    [∗35·02] $\hat{x} \hat{y}[xRy \sdot y \in \beta]$ $\{\langle x,y \rangle \mid Rxy \amp y \in \beta\}$ |
| $\alpha \uparrow \beta$ | (the relation of members of $\alpha$ to members of $\beta)$    [∗35·02]. $\hat{x} \hat{y}[x \in \alpha \sdot y \in \beta$] $\{\langle x,y\rangle \mid x \in \alpha \amp y\in \beta \}$, the *Cartesian product* of $\alpha$ and $\beta $. |

$\ast 36 $ *Relations with Limited Fields*

| $P \restriction \! \! \! \downharpoonright \alpha$ | (the *restriction* of $R$ to $\alpha)$    [∗36·01] $\alpha \upharpoonleft P \restriction \alpha$ $\{\langle x,y \rangle \mid x \in \alpha \amp y \in \alpha \amp Rxy \}$ |
| --- | --- |

$\ast 37 $ *Plural Descriptive Functions*

| $R ‘‘\beta$ | (the terms which have the relation $R$ to members of $\beta$)    [∗37·01] ∗ $\hat{x} \{(\exists y) \sdot y\in \beta \sdot x Ry\}$ $\{x \mid \exists y(y\in \beta \amp Rxy)\}$ |
| --- | --- |
| $ R_{\in}$ | (the relation of $\alpha$ to $\beta $ when $\alpha$ is the class of terms which have $R $ to members of $\beta$)    [∗37·02] $\hat{\alpha} \hat{\beta} ( \alpha = R ‘‘ \beta )$ $\{\langle \alpha, \beta \rangle \mid x \in \alpha \amp \exists z ( y \in z \amp z \in \beta \amp Ryz ) \}$ |

$\ast 38$ *Double descriptive functions*. PM uses a metalinguistic variable “$ \venus $” that can be replaced by a any of a range of relations between individuals, classes, or relations, that are treated as *operations* on their arguments. The operation of intersection can be represented as a higher order function of its first argument. Thus $\cap \beta ` \alpha = \alpha \cap \beta$.

| $\venus \: y$ | (the relation of $ x \: \venus \: y $ to $x $ for any $ x $)    [∗38·02] $\hat{u} \hat{x} ( u = x \: \venus\: y)$ $\{\langle u,x \rangle \mid u = x \: \venus \: y \}$ |
| --- | --- |

This notion will be used later. An example with the notion of relative product is an instance, thus:

| $\mid R$ | (the relation of one power of $R$ to the next)    [∗38·02] $\hat{P}\hat{S}(P = R \mid S )$ $\{ \langle P, S \rangle \mid P = R \circ S \}$ |
| --- | --- |
| $\alpha \: \venus_{\! \! \! ,,} \: y$ | (the class of values of $x \: \venus \: y \: $ when $x$ is an $ \alpha $)    [∗38·03] $ \venus \: y $ `` $\alpha $ $\{u \mid \exists x ( x \in \alpha \: \amp \: u = x \: \venus y \: ) \: \}$ |
| $s ‘ \kappa$ | (the *sum* or union of the $\kappa$s)    [∗40·02] $\hat{x} \{ ( \exists \alpha ). \: \alpha \in \kappa \; . \; x \in \alpha \}$ $\cup \kappa$, or $\{ x \mid \exists \beta ( \beta \in \kappa \amp x \in \beta ) \}$ |
| $\dot{s} ‘ \lambda $ | (the *sum* of the relations in $\lambda$)    [∗41·02] $\hat{x}\hat{y} \{ ( \exists R ). \: R \in \lambda \; . \; x R y \}$ $\{ \langle x, y \rangle \mid \exists R \: (R \in \lambda \; \amp \; Rxy ) \}$ |

## 11. Prolegomena to Cardinal Arithmetic (Part II)

Contemporary philosophers would consider the transition to mathematics to begin with the theory of sets (or proper classes which are too large to be sets), but in PM that is also a part of Mathematical Logic. The Prolegomena to Arithmetic thus begins with the definitions in terms of logic of explicitly arithmetical notions, the cardinal numbers 1 and 2.

| $I $ | (the relation of identity)    [∗50·01] $ I = \hat{x}\hat{y} (x = y) $ $\{ \langle x , y \rangle \mid x = y \}$ |
| --- | --- |
| $J $ | (the relation of diversity)    [∗50·02] $ I = \dot{-} I $ $\{ \langle x , y \rangle \mid x \neq y \}$ |
| $\iota ‘ x$ | (the *unit class* of $x$) as defined by theorem    [∗51·1] from definition    [∗51·01] $\hat{y} (y = x)$ $\{ y \mid y = x \}$ (the *singleton* $x$) |
| $\mathbf{1}$ | (the cardinal number 1)    [∗52·01] $\hat{\alpha} \{ (\exists x) \sdot \alpha = \iota‘x \}$ $\{ \alpha \mid \exists x \; ( \alpha = \{x \} ) \}$ (the class of all singletons) The variable $ x $ is typically ambiguous here, so will be a distinct number 1 for each type that $ x $ can assume. This applies to 2, as well, and all the natural numbers, as we will see below. |
| $\mathbf{2}$ | (the cardinal number 2)    [∗54·02] $\hat{\alpha} \{ (\exists x,y) \sdot x \neq y \sdot \alpha = \iota‘x \cup \iota‘y \}$ $\{ \alpha \mid \exists y \exists z( y \neq z \amp \alpha = \{y \} \cup \{z\} ) \}$ (the class of all pairs) |
| $x \downarrow y$ | (the *ordinal couple* of $x$ and $y$)    [∗55·01] $\iota‘x \uparrow \iota‘y$ $\langle x, y \rangle$ (the *ordered pair* $\langle x,y \rangle$) |

The paperback abridged edition of *Principia Mathematica to* ∗56 only goes this far, so the remaining definitions have only been available to those with access to the full three volumes of PM. Russell did not make the decision to end the 1962 abridged version at this point, but the choice is understandable. It is here that contemporary set theory begins to look even more different from PM. Set theory follows Norbert Wiener (1914) by representing relations as sets of ordered pairs, which themselves defined as sets. (Wiener’s proposal of $ \langle x, y \rangle =_\mathit{df} \{ \{ \{x \}, \emptyset \}, \{ \{y \} \} \} $ has generally been replaced by Kuratowski’s simpler $\{ \{x \}, \{ x,y \} \}$) . The remainder of PM examines the structure of relations that lead to the mathematics of natural and real numbers, and the portion of the theory of transfinite sets that can be carried out in the theory of types. This looks very different from the development of these notions in axiomatic set theory.

| $\Cl\ ` \alpha$ | (the class of *subclasses* of $\alpha$)    [∗60·12] $\hat{\beta} (\beta \subset \alpha) \}$ $\wp{\alpha}$, the *power set* of $\alpha$, $\{x &#124; x \subseteq \alpha\}$ |
| --- | --- |
| $\Cl\ \ex\ ` \alpha$ | (the class of *existent subclasses* of $\alpha$)    [∗60·13] $ \hat{\beta} (\beta \subset \alpha \; . \; \exists ! \beta ) \}$ $\{x &#124; x \subseteq \alpha \; \amp \; x \neq \emptyset\}$ |
| $\Rl\ ` P$ | (the class of *sub relations* of $P$)    [∗61·12] $\hat{R} \{ R \subset \! \! \! \! \cdot \; P \}$ $\{ R \mid \forall x \forall y ( \langle x, y \rangle \in R \supset \langle x,y \rangle \: \in P) \}$ |
| $\in$ | (the *relation of membership in a class*)    [∗62·01] $\hat{x} \hat{\alpha} ( x \in \alpha)$ $\{ \langle x,y \rangle \mid \: x \in y \}$ |

$\ast 63$ *Relative Types of Classes.* The theory of types in PM allows for expressions relating classes of different types. The gap between set theory and the theory of classes in PM comes from the lack of a cumulative theory of classes of *any* type. These PM system allows definitions of relations between, say, individuals and classes of individuals. These are needed in the account of real numbers in terms of classes of classes of ratios in Volume III.

| $t‘x$ | (the type of which $x$ is a member)    [∗63·01] $\iota ` x \cup - \iota ` x$ $\{ x \} \cup \{ y \mid y \not \in \{ x \} \}$ |
| --- | --- |
| $t_0‘\alpha$ | (the type in which $\alpha$ is contained)    [∗63·02] $\alpha \cup - \alpha$ $\alpha \cup \{ x \mid x \not \in \alpha \}$ |
| $t_1‘ \kappa$ | (the type next below that in which $\kappa$ is contained)    [∗63·03] $t_0 `s`\kappa$ $\cup \: \{ \: \cup \{ \alpha \mid \alpha \in \kappa \} \: , \: \{ \beta \mid \beta \not \in \cup \{ \alpha \mid \alpha \in \kappa \} \} \: \}$ |
| $t_{11}‘ \alpha$ | (the type of pairs of classes of types $t_1 ‘ \alpha$)    [∗64·022] $t ‘ ( t_1 ‘ \alpha \uparrow t_1 ‘ \alpha )$ The type of a pair of classes of a given type will be the same as that of classes of those classes. This definition is in order as it stands, but would be very complex to write in contemporary notation. We leave it as an open problem for readers to devise a concise formula formulation. |
| $\alpha \rightarrow \beta$ | (The relations with *referents* in $ \alpha $ and *relata* in $ \beta $ ) (from $ \alpha $ *onto* $ \beta $)    [∗70·01] $\hat{R} (\overrightarrow{R}“\backd ‘R \subset \alpha \sdot \overleftarrow{R}“D‘R \subset \beta )$ $ \{ R \mid \forall x \forall y \: ( Rxy \supset [ \: \{z \mid Rxz \} \in \alpha \: \amp \: \{u \mid Rxu \} \in \beta \} \: ]\: \} $ Since 1 is the class of singleton classes, $(1 \rightarrow 1) $ will be the class of one to one (surjective) relations. |
| $\alpha \mathbin{\overline{\mathrm{sm}}} \beta$ | (the class of similarity relations between $\alpha$ and $\beta$)    [∗73·03] $ \{ R \mid R \in 1 \rightarrow 1 \: .\: \alpha = D‘R \: .\: \beta = \backd ‘R \} $ $\{f \mid f : \alpha \stackrel{1-1}{\longrightarrow} \beta\}$ |
| $\mathrm{sm}$ | (the relation of *similarity*)    [∗73·02] $\hat{\alpha} \hat{\beta}(\exists! \alpha \mathbin{\overline{\mathrm{sm}}} \beta)$ $\alpha \approx \beta$ |

$\ast 80$ *Selections*. A *selection function* for a class $\kappa$ is a function $f$ making each element $x$ of $\kappa$ to a member of $x$. These are denoted by $ \in_{\Delta} `\kappa$. The cardinal number of the product of two classes $\alpha X \beta$ is the cardinal number of the class of all pairs of members selected from $\alpha$ and $\beta$, so the guarantee that such selections exist is called the *Multiplicative Axiom* in PM. This is now known as the *Axiom of Choice*, which had been identified as an assumption used in proofs in set theory by Ernst Zermelo in 1904. In PM it is defined as asserting that if a class $\kappa$ is a set of mutually exclusive, non-empty classes, then there exists a class $\mu$ which contains exactly one member of each element of $\kappa$.

| $\in_{\Delta}`\kappa$ | (the *selective relations* for $\in$)    [∗80·01] $(1 \rightarrow Cls) \; \cap \; Rl` \in \; \cap \; \overleftarrow{\backd}`\kappa$ $\{ f \mid \forall \alpha (\alpha \in \kappa \supset f(\alpha) \in \alpha ) \}$ |
| --- | --- |
| $\Cls ^2 \ \excl$ | (*class of mutually exclusive classes*)    [∗84·01] $\hat{\kappa} ( \alpha , \beta \in \kappa \; .\; \alpha \neq \beta \; . \supset_{\alpha , \beta} . \; \alpha \cap \beta = \Lambda )$ $\{ \kappa \mid \forall \alpha \forall \beta (\alpha , \beta \in \kappa \; \amp \; \alpha \neq \beta \supset \alpha \cap \beta = \emptyset)\}$ |
| $\Cls\ \ex ^{2} \ \excl$ | (*class of mutually exclusive non-empty classes*)  [∗84·03] $\Cls^2 \; \excl \; - \overleftarrow{\in} ` \Lambda$ $\{ \kappa \mid \; \forall \alpha (\alpha \in \kappa \supset \alpha \neq \emptyset) \; \amp$ $\; \forall \alpha \forall \beta \: [ \alpha \in \kappa \: \amp \: \beta \in \kappa \supset (\alpha = \beta \vee \alpha \cap \beta = \emptyset) ] \}$ |
| Mult ax | (the *Multiplicative Axiom*)    [∗88·03 ] $\kappa \: \epsilon \: \mathrm{Cls \; ex^2 excl} \: . \supset_{\kappa} \: : (\exists \mu) : \alpha \: \epsilon \: \kappa \: . \supset_{\alpha} . \: \mu \cap \alpha \: \epsilon \: 1$ $\forall \kappa \{ [ \; \forall \alpha (\alpha \in \kappa \supset \alpha \neq \emptyset ) \; \amp$ $\; \forall \alpha \forall \beta \: (\alpha \in \kappa \: \amp \: \beta \in \kappa \supset (\alpha = \beta \vee \alpha \cap \beta = \emptyset)) \:] \;\supset$ $\; \exists \mu \forall \alpha \exists x \: (\alpha \in \kappa \supset \mu \cap \alpha = \{x \} ) \}$ |

$\ast 90$ *Inductive Relations*. The concluding section of Volume I presents a generalization of the structure of the natural numbers that underlies the principle of mathematical induction.

| $R_*$ | (the *ancestral* of $R)$    [∗90·01] $\hat{x} \hat{y} \{ x \in C‘ R \colon \breve{R}“\mu \subset \mu \sdot x \in \mu \ldot {\supset_{\mu}} \ldot y \in \mu \}$ $\{ \langle x, y \rangle \mid x \in \mathcal{F}`R \; \amp$ $\; \forall_{\mu} [ \forall z \forall w [( z \in \mu \; \amp \; Rzw ) \supset w \in \mu ] \supset y \in \mu ] \}$ Now written $R^*$ this follows Frege’s definition: $y$ is in all the $R$-hereditary classes that contain $x$. |
| --- | --- |
| $R_{\text{ts}}$ | (the relation between $ R $ and the series of its *powers* $ R^n$ for $n \gt 0$ , i.e., $ R (= R^1) $, $R^2$ $R^3$, etc. )    [∗91·02] $( \: \mid R)_{\ast}$ $\{ \langle P,S \rangle \mid P = R^n \: \amp \: S = R^{n+1} \} $ |
| Pot $‘ R$ | (the *positive powers*, i.e., *Potentia*, of $R$)    [∗91·03] $\overrightarrow{R}_{\text{ts}} ‘ R$ $\{ S \: \mid \; \exists n >0 \: ( S = R^n ) \} $ |
| $R_{\text{po}}$ | (the union of the positive powers of $R$)    [∗91·05] $\dot{s}‘ \text{Pot} ‘ R$ $ \{ \langle x, y \rangle \mid \exists S \: \exists n \gt 0 \:( S = R^n \: \amp \: Sxy ) \} $ |
| $xB‘P$ | ( $x$ *begins* the relation $P$)    [∗93·01] $x \in D ‘ P - \backd ‘P$ $\{ x \mid \exists y \: Pxy \; \amp \sim \exists z Pzx \}$ |
| $x \:$ min$_P ` \alpha$ | ( $x$ is a *minimal* member of $ \alpha $ with respect to $P$)    [∗93·02] $x \in \alpha \cap C`P - \breve{P} `` \alpha$ $x \in \alpha \; \amp \; x \in \mathcal{F}P \; \amp \; \sim \exists z \: (Pzx \: \amp \: z \in \alpha )$ |
| $\stackrel{\leftrightarrow}{R} `x$ | ( the *family* of $R$, ancestry and posterity)    [∗97·01] $\overrightarrow{R}`x \cup (\iota ` x \cap C ` R)\cup \overleftarrow{R}` x$ $\{ y \mid Rxy \; \vee \; ( y = x \: \amp \: x \in \mathcal{F} `R) \; \vee \; Rxy \} $ |

## 12. Cardinal Arithmetic (Part III)

With $\ast 100$ at the start of Volume II, *Principia Mathematica* finally begins developing the theory of cardinal numbers with the *Frege-Russell Definition* of numbers as classes of equinumerous classes.

| $\mathrm{N_c}$ | (the relation between a class and its cardinal number)    [∗100·01] $\overrightarrow{\mathrm{sm}}$ $\{ \langle \alpha, \beta \rangle \mid \beta = \{ \gamma \mid \gamma \approx \alpha \} \} $ |
| --- | --- |
| $\mathrm{NC}$ | (the *Cardinal Numbers*)    [∗100·02] $ \mathrm{D} ‘ \mathrm{N_c} $ $ \{ \alpha \mid \exists \beta ( \alpha = \{ \gamma \mid \gamma \approx \beta \} \: \}$ |
| $\mathbf{0}$ | (the cardinal number 0)    [∗101·01] $0 = \mathrm{N_c}‘\Lambda$ $\{\varnothing\}$ The class of all classes equinumerous with the empty set is just the singleton containing the empty set. |
| $\text{N}_0 \text{c}‘\alpha$ | ( the *homogeneous cardinal* of $\alpha$)    [∗103·01] $\text{Nc}‘ \alpha \; \cap \; t‘\alpha$ $\{ \beta \mid \beta \approx \alpha \}$ for $\beta$ of the same type as $\alpha$ |
| $\text{N}_0\text{C}$ | (the *Homogeneous Cardinals*)    [∗103·02] $\text{D}‘ \text{N}_0 \text{c} $ $\{ \alpha \mid \exists \beta (\alpha \; \text{is the homogenous cardinal of}\; \beta ) \}$ |
| $\alpha + \beta$ | (the *arithmetic sum* of $\alpha$ and $\beta$)    [∗110·01] $\downarrow (\Lambda \cap \beta)“\iota“\alpha \cup (\Lambda \cap \alpha) \downarrow“\iota“\beta $ This is the union of $\alpha$ and $\beta$ after they are made disjoint by pairing each element of $\beta$ with $\{ \alpha \}$ and each element of $\alpha$ with $\{ \beta \}$. The classes $\alpha$ and $\beta$ are intersected with the empty class, $\Lambda$, to adjust the type of the elements of the sum. $\{ \langle \{ a \} , \emptyset \rangle \mid a \in \alpha \} \cup \{ \emptyset , \{b \} \rangle \mid b \in \beta \}$ |
| $\mu +_c \nu$ | (the *cardinal sum* of $\mu$ and $\nu$)    [∗110·02] $\hat{\xi}\{(\exists \alpha,\beta) \sdot \mu = \mathrm{N_0 c}‘\alpha \sdot \nu = \mathrm{N_0 c}‘\beta\sdot\xi\,\mathrm{sm}(\alpha + \beta)\}$ Cardinal addition is the arithmetic sum of homogeneous cardinals: $ \{\gamma \mid \exists \alpha \exists \beta \: [ \gamma \approx ( \alpha + \beta ) ] \: \} $ when $\alpha $ and $ \beta $ are homogenous cardinals. |

The reader can now appreciate why this elementary theorem is not proved until page 83 of Volume II of *PM*:

$$\tag*{∗110·643} 1 +_c 1 = 2 $$

Whitehead and Russell remark that “The above proposition is occasionally useful. It is used at least three times, in …”. This joke reminds us that the theory of natural numbers, so central to Frege’s works, appears in PM as only a special case of a general theory of cardinal and ordinal numbers and even more general classes of isomorphic structures.

| $\beta \times \alpha$ | (the *product* of classes)    [∗113·02] $s` \alpha \downarrow_{\! \! \!,,} ``\beta$ $\{ \langle x , y \rangle \mid x \in \beta \; \amp \; y \in \alpha \}$ |
| --- | --- |
| $\mu \times_{\text{c}} \nu$ | (the *product* of homogenous cardinal numbers)    [∗113·03] $\hat{\xi} \{ (\exists \alpha, \beta) . \: \mu = N_0\text{c}` \alpha \: . \: \nu = N_0\text{c}` \beta \; . \; \xi \: \text{sm} \: (\alpha \times \beta)\}$ If $\mu = \bar{\bar{\alpha}} \; \amp \; \nu = \bar{\bar{\beta}}$ then $\mu \times \nu = \{ \beta \mid \beta \approx ( \alpha \times \beta) \}$ |
| $\alpha$ exp $ \beta $ | (the *exponentiation* of classes)    [∗116·01] Prod ‘ $ \alpha \downarrow_{\! \! \! ,,} $‘‘ $ \beta $ $\{ f \mid \mathcal{D} f = \beta \; \amp \; \mathcal{R} f \subseteq \alpha \}$ |
| $\mu^{\nu}$ | (the *exponentiation* of cardinal numbers)    [∗116·02] $\hat{\gamma} \{ (\exists \alpha, \beta) . \: \mu = N_0\text{c}` \alpha \: . \: \nu = \mathrm{N}_0\text{c}` \beta \; . \; \gamma$ sm $(\alpha$ exp $\beta)\}$ $\{ \gamma \mid \exists \alpha \exists \beta \: ( \mu = \bar{\bar{\alpha}} \; \amp \; \nu = \bar{\bar{\beta}} \; \amp \; \gamma \approx \alpha^{\beta} )\}$ |

The following theorem, that the cardinality of the power set of $\alpha$ is 2 raised to the power of the cardinality of $\alpha$, $\; \bar{\bar{ \wp{\alpha} }} = 2^{\bar{\bar{\alpha}}}$, is called “*Cantor’s Proposition*”, and is said to be “very useful” (PM II, 140):

$$\tag*{∗116·72} \text{Nc}‘\text{Cl}‘\alpha = 2^{\text{Nc}‘\alpha} $$

Next the notion of *greater than* arbitrary cardinals, finite and infinite. The cardinal number of $ \alpha $ is greater than the cardinal number of $ \beta $ just in case there is a subset of $ \alpha $ that is equinumerous with $ \beta $, but there is no subset of $\beta $ that is equinumerous with $\alpha $. Cantor’s famous “diagonal argument” shows that cardinal number $ \aleph_c $ of the class of real numbers is greater than $ \aleph_0 $, the cardinal number of the class of natural numbers.

| $\mu \gt \nu $ | (*greater than*)    [∗117·01] $ (\exists \alpha, \beta ) \: . \: \mu = \text {N}_0\text{c}` \alpha\: . \: \nu = \mathrm{N}_0\text{c}` \beta \: . \: \exists ! \: \text{Cl} ‘ \alpha \: \cap \: \text{Nc} ‘ \beta \: . \: \sim \exists ! \: \text{Cl} ‘ \beta \: \cap \: \text{Nc} ‘ \alpha $ $ \exists \delta (\delta \in \wp{\alpha} \; \amp \; \delta \in \bar{\bar{\beta}} ) \; \amp \; \sim \exists \gamma (\gamma \in \wp{\beta} \; \amp \; \gamma \in \bar{\bar{\alpha}} ) $ |
| --- | --- |

The more familiar result, *Cantor’s Theorem*, proves the power set of $\alpha$ is strictly larger, $2^{\bar{\bar{\alpha}}} \gt \bar{\bar{ \alpha }}$.

$$\tag*{∗117·661} \mu \in \text{N}_0\text{C} \; . \: \supset \: . \; 2^{\mu} \gt \mu $$

| NC induct | (the *Inductive Cardinals*)    [∗120·01] $\hat{\alpha}\{\alpha({+_c}1)_* 0\}$ $\{x \mid 0 S^* x\}$ The inductive cardinals are the “*natural numbers*”, that is, 0 and all those cardinal numbers that are related to 0 by the ancestral of the “successor relation” $S$, where $xSy$ just in case $y = x +1$. |
| --- | --- |
| Infin ax | (the *Axiom of Infinity*)    [∗120·03] $\alpha \in \text{NC induct}\:\sdot \supset_{\alpha} \sdot \: \exists!\alpha$ $\forall \alpha (\alpha \in \{x \mid 0S^* x\} \supset \alpha \neq \varnothing)$ |

The Axiom of Infinity asserts that all inductive cardinals are non-empty. (Recall that 0 = $\{ \varnothing \}$, and so 0 is not empty.) The Axiom of Infinity is not a “primitive proposition” but instead to be listed as an “hypothesis” where used, that is as the antecedent of a conditional, where the consequent will be said to depend on the axiom. Technically it is not an *axiom* of PM as [∗120·03] is a *definition*, so this is just further notation in PM!

| Prog | (*Progressions*, or $\omega$ orderings)    [∗122·01] $(1 \rightarrow 1) \cap \hat{R} (D`R = \overleftarrow{R_{\ast}} ‘‘ B ‘R)$ $\{ R \mid R$ is isomorphic to the ancestral of a relation for which every subset of the domain has a first element. } |
| --- | --- |

“By a ‘progression’ we mean a series which is like the series of the inductive cardinals in order of magnitude (assuming that all the inductive cardinals exist) *i.e.* a series whose terms can be called $1_R, 2_R, 3_R, \ldots \nu_R, \ldots $. It is not convenient to *define* a progression as a series which is ordinally similar to that of the inductive cardinals, both because this definition only applies if we assume the axiom of infinity, and because we have in any case to show that (assuming the axiom of infinity) the series of inductive cardinals has certain properties, which can be used to afford a direct definition of progressions.” (PM II, 245)

| $\aleph_0$ | (the smallest of Cantor’s transfinite cardinals)    [∗123·01] $D‘‘$Prog $\bar{\bar{\omega}}$ |
| --- | --- |

## 13. Relation Arithmetic (Part IV)

The notion of *relation number*, is the generalization of the notion of a well-ordering to an arbitrary relation. Just as a cardinal number is defined in PM as a class of equinumerous classes, an arbitrary relation number is a class of *ordinally similar* relations.

| $S^{;}Q$ | (S is a *correlator* of Q)    [∗150·01] $S \mid Q \mid \breve{S}$ $S \circ Q \circ S^{-1}$ |
| --- | --- |
| $P \: \overline{\text{smor}} \: Q$ | (the class of *similarities of* between $P$ and $Q$ )    [∗151·01] $\hat{S} \{ S \in 1 \rightarrow 1 \; . \; C‘Q = \backd ‘S \; . \; P = S^{;} Q \}$ $\{ f \mid \mathcal{F} P \stackrel{1-1}{\longrightarrow} \mathcal{F} Q \; \amp \; \forall x \forall y [ (x \in \mathcal{D} f ) \supset Pxy \equiv Q f(x) f(y)]\}$ |
| $P \;$ smor $\:Q$ | ($P$ is *ordinary similar to* $Q$ )    [∗151·02] $\{ \langle P, Q \rangle \mid \exists ! \; P \: \overline{\text{smor}} \: Q \} $ $P \cong Q$ ( $P$ is *isomorphic* to $Q$). |
| Nr$`P$ | (the *relation number* of $P$)    [∗152·01] $\overrightarrow{\text{smor}} ‘ P$ $\{ Q \mid P \cong Q\}$ |

$\ast 170$ The relation of *first differences* orders classes on the basis of an ordering of their members. The method is a variation on the notion of *lexicographic ordering* of classes as in the alphabetical ordering of words in a dictionary. See Fraenkel (1968). PM uses two versions of the notion.

| $P_{\text{cl}}$ | (ordering of classes by *first differences* of $P$)    [∗170·01] $\hat{\alpha}\hat{\beta} \{ \alpha, \beta \in \text{Cl}`C`P \; . \; \exists ! \; \alpha - \beta - \breve{P}`` ( \beta - \alpha ) \}$ For $\prec$ an ordering of individuals, $\alpha \prec_{\text{cl}} \beta$ is $\{ \langle \alpha , \beta \rangle \mid \alpha$ , $\beta \subseteq \mathcal{F}( \prec ) \; \amp \; \alpha \not\subseteq \beta \; \amp \; \forall x \forall y (x \in \beta \; \amp \; y \not \in \alpha \; \supset \; y \prec x )\: \} $ |
| --- | --- |

This is explained in the *Summary of* $\ast 170$: “$\alpha$ and $\beta$ each pick out terms from $C`P$, and these terms have an order conferred by $P$; we suppose that the earlier terms selected by $\alpha$ and $\beta$ are perhaps the same, but sooner or later, if $\alpha \neq \beta$, we must come to terms which belong to one but not the other. We assume that the earliest terms of this sort belong to $\alpha$, not to $\beta$; in this case, $\alpha$has to $ \beta$ the relation $P_{\text{cl}}$. That is, where $\alpha$ and $\beta$ begin to differ, it is terms of $\alpha$ that we come to, not terms of $\beta$. We do not assume that there is a *first* term which belongs to $\alpha$ but not $\beta $, since this would introduce undesirable restrictions in case $P$ is not well-ordered.” (PM II, 399)

| $P_{\text{lc}}$ | (*converse* ordering of classes by *first differences* of $P$)    [∗170·02] Cnv $` (\breve{P})_{\text{cl}}$ $ \{ \langle \alpha, \beta \rangle \mid \alpha \prec_{cl} \beta \} $ |
| --- | --- |

“Thus $\alpha P_{\text{lc}} \beta$ means, roughly speaking, that $\beta - \alpha$ goes on longer than $ \alpha - \beta$, just as $\alpha P_{\text{cl}} \beta$ means that $ \alpha - \beta$ begins sooner. This if $P$ is the relation of earlier and later in time, and $\alpha$ and $\beta$ are the times when $A$ and $B$ respectively are out of bed, ‘$\alpha P_{\text{cl}} \beta$’ will mean that $A$ gets up earlier than $B$ and ‘$\alpha P_{\text{lc}} \beta$’ will mean that $B$ goes to bed later than $A$.” (PM II, 401)

## 14. Series (Part V)

“*Series*” in PM are *linear orderings*. Volume II concludes halfway through this part, with Volume III beginning at $\ast250$ and the theory of well-orderings. These concepts are defined in the now standard way. This section is only alien to the modern reader because of the notation.

| trans $ P $ | ($P$ is *transitive* relations)    [∗201·1] $P^2 \subset \! \! \! \! \cdot \;\; P$ $\forall x \forall y \forall z (Pxy \: \amp \: Pyz \: \supset \: Pxz)$ |
| --- | --- |
| connex P | (P is *connected*)    [∗202·1] $x \in C` P \; . \supset_x . \; \stackrel{\leftrightarrow}{P} ` x = C`P$ $\forall x \forall y [(x, y \in \mathcal{F} P ) \: \amp \: x \neq y \supset Pxy \vee Pyx ]$ |
| Ser | (*series*)    [∗204·01] Rl $\: ‘ J \cap$ trans $\cap$ connex $\{ P \mid \; \forall x \forall y (Pxy \supset x \neq y) \; \amp \; P$ is transitive $\amp \; P$ is connected $\}$ or $P$ is a *linear ordering* |
| sect | (*sections*)    [∗211·01] sect $ ‘ P = \hat{\alpha} ( \alpha \subset C ‘ P \:. \: P “ \alpha \subset \alpha) $ $\{ \alpha \mid \alpha \subset \mathcal{F}P \: \amp \: \forall x [ \exists y ( y \in \alpha \: \amp \: Pxy ) \supset x \in \alpha \: ] \: \} $ |

“The theory of the modes of separation of a series into two classes, one of which wholly precedes the other, and which together make up the whole series, is of fundamental importance. $ \ldots $ Any class which can be the first of such a pair we call a *section* of our series.” (PM II, 603)

| $\varsigma ‘ P$ | (the series of *segments* of $P$)    [∗212·01] $P_{\text{lc}} \restriction \! \! \! \downharpoonright$ D$`P_{\in}$ |
| --- | --- |

The *Summary* of $\ast 211$ explains the definition as follows: “The members of D$ “P_{\epsilon} $ are called the *segments* of the series generated by *P*. In a series in which every sub-class has a maximum or a sequent [immediate successor (cf. $ ∗206 ) ] $, $ \text{D} “P_{\epsilon} = \overrightarrow{P}“C‘P $ $(∗211·38)$, i.e. the predecessors of a class are always the predecessors of a single term, namely the maximum of the class if it exists, or the sequent if no maximum exists. $ \ldots $ Thus in general the series of segments will be larger than the original series. For example, if our original series is of the type of the series of rationals in order of magnitude, the series of segments is of the type of the series of real numbers, i.e. the type of the continuum.” (PM II, 603)

> We have no need for a special notation for the series of sections, since, in virtue of ∗211·13, it is $\varsigma ‘ P_{\ast} \ldots $. (PM II, 628)

Volume III begins with $\ast 250$ on *well-orderings*. An *ordinal number* is then defined as a class of ordinary similar well-orderings.

| Bord | (*well ordered* relations - *Bene ordinata*)    [∗250·01] $\hat{P} \{$ Cl ex $‘C ‘P \subset \backd ‘ \text{min}_{P} \}$ $\{ P \mid \forall \alpha \; [ \: (\alpha \subseteq \mathcal{F}P \: \amp \: \alpha \neq \emptyset )\supset \exists x (x \in \alpha \amp \forall z (z \in \alpha \supset \sim Pzx )\: )\: ] $ |
| --- | --- |
| $\Omega$ | (the well ordered series)    [∗250·02] Ser $\; \cap \;$ Bord $\Omega$ is the class of well ordered linear orderings. |
| NO | (*Ordinal Numbers*)    [∗251·01] $\text{Nr}\, ``\, \Omega$ The ordinal numbers are classes of isomorphic well-ordered linear orderings. |

“Zermelo’s Theorem”, that the Multiplicative Axiom (Axiom of Choice) implies that every set can be well-ordered, is derived in $\ast 258$. This was first proved in Zermelo (1904).

$$\tag*{∗258·32 } \mu \sim \in \: 1 \: . \; \exists ! \in_{\Delta}‘\text{Cl ex} ‘ \mu \: . \supset . \: \mu \: \epsilon \: C“ \Omega $$

## 15. Quantity (Part VI)

The last section of PM studies the *rational numbers* and *real* numbers. They are constructed from relations between entities, such as *being longer than*, or *being heavier than*, that might be measured with a ruler or balance scale. Contemporary *measurement theory* studies the relations among entities in order to determine which *scales*, or systems of independently characterized numbers, might be assigned to them as representing the “quantities” of various properties, such as length or weight, that they possess. Notice that the real numbers are not constructed as classes of rational numbers, but are of a uniform type as “Dedekind cuts” in a series of classes of ratios. In PM, as in contemporary mathematics, because the class (*segment*) of rational numbers $ \{ r | r^2 \leq 2 \} $ will have no rational number as a *least upper bound* , that class itself will be identified with the irrational number $ \sqrt{2}$. The rational number $ 1/2 $ is identified with its (lower) segment of rationals, $ \{ r | r \lt 1/ 2 \} $.

| $U$ | (*greater than* for inductive cardinals)    [∗300·01] $(+_c 1)_{\text{po}} \; \upharpoonright \! \! \! \downharpoonright \; ( \text{NC induct } - \iota ` \Lambda)$ $\{ \langle n, m \rangle \mid \; n \gt m \}$ |
| --- | --- |
| Prm | (*relative primes*)    [∗302·01] $\hat{\rho}\hat{\sigma} \{ \rho , \sigma \: \epsilon \: \text{NC induct} \; :$ $\;\rho = \xi \times_c \tau \: . \: \sigma = \eta \times_c \tau . \supset_{\xi, \eta, \tau} . \tau = 1\}$ $r \; \text{and} \; s \; \text{are}$ *relatively prime* iff $\forall j \: \forall l \: \forall k \: [ ( r = j \times k \; \amp \; s = l \times k) \supset k = 1]$ |
| $(\rho , \sigma) \text{Prm}_{\tau} (\mu , \nu )$ | ($\rho / \sigma \; \text{is}\; \mu / \nu$ in its *lowest terms* and $\tau$ is the highest common factor of $\mu \; \text{and} \; \nu$ )    [∗302·02] $\rho \: \text{Prm} \: \sigma \; . \; \tau \in \text{NC induct} - \iota ` 0 \; . \; \mu = \rho \times_{\text{c}} \tau \; . $ $\; \nu = \sigma \times_{\text{c}} \tau$ The ratio of $r/s$ is $m /n$ in its lowest terms with $k$ as its highest common factor $=_{\text{df}}$ $r$ and $s$ are relatively prime and $ m = r \times k \; \amp \; n = k \times s$ |
| $(\rho , \sigma) \text{Prm}(\mu , \nu )$ | (the ratio $\rho / \sigma \; \text{is}\; \mu / \nu \; \text{in its}$ lowest terms)    [∗302·03] $(\exists \tau) . \: (\rho, \sigma ) \text{Prm}_{\tau} (\mu , \nu)$ The ratio of $r/s$ is $m /n$ in its lowest terms $=_{\text{df}} \exists k (\text{The ratio of}\; r/s \; \text{ is} \; m /n \text{in its lowest terms with}\; k$ as its highest common factor.) |
| $\mu / \nu$ | (the *ratio* of relations $ \mu $ and $ \nu $)    [∗303·01] $\hat{R} \hat{S} \{ (\exists \rho, \sigma) . (\rho, \sigma) \text{Prm}(\mu, \nu) . \: \dot{\exists} ! \; R^{\sigma} \: \dot{\cap} \: S^{\rho} \}$ $\{ \langle R, S \rangle \mid \exists r \exists s \:( r/s $ is $ m/n $ in lowest terms and $\exists x \exists y (R^s xy \amp S^r xy) \}$ |

“A distance on a line is a one-one relation whose converse domain (and its domain too) is the whole line. If we call two such distances $R$ and $S$, we may say that they have the ratio $\mu / \nu$ if, starting from some point $x$ , $\nu$ repetitions of $R$ take us to the same point $y$ as we reach by $\mu \;$repetitions of $S$, *i.e.*, if $xR^{\nu} y \: . \: x S^{\mu} y$.” (PM III, 260)

| Rat def | (*definite ratios*)    [∗303·05] $\hat{X} \{ (\exists \mu, \nu) . \: \mu , \nu \: \epsilon \: \text{D}`U \: \cap \; \backd `U . \: X = (\mu / \nu) \upharpoonright \!\!\! \downharpoonright \; t_{11} ` \mu \}$ The class of ratios restricted to members of a given type. Notice that the following definitions will not depend on the Axiom of Infinity. |
| --- | --- |
| $X \lt_r Y$ | (*less than* between ratios)    [∗304·01] $( \exists \mu, \nu, \rho , \sigma).$ $\: \mu, \nu, \rho , \sigma \: \epsilon \: \text{Nc induct} \: . \sigma \neq 0 .$ $\; \mu \times_c \sigma \lt \nu \times_c \rho \: . \; X = \mu / \nu \: . \; Y = \rho / \sigma$ $X \lt Y =_{\text{df}} \exists j \: \exists k \: \exists m \: \exists n$ $\: ( j \times m \lt k \times n \; \amp \; X = j/k \; \amp \; Y = n/m )$ |
| $H$ | (the relation *less than* between definite ratios)    [∗304·02] $\hat{X} \hat{Y} \{ X,Y \: \in \: \text{Rat def} \: . \: X \lt_r Y \}$ $\{ \langle r, s \rangle \mid \; r \: \text{is rational} \; \amp \; s \: \text{is rational} \; \amp \; r \lt s \}$ “H” is a capital *eta* “$\eta$”, Cantor’s symbol for rational numbers. |
| $\Theta$ | (*real numbers*)    [∗310·01] $(\varsigma ‘ H ) \upharpoonright \!\!\! \downharpoonright \; ( - \iota ‘ \Lambda - \iota ‘\text{D}‘ H)$ |

“The series of real numbers other than 0 and infinity” (PM III, 316) are the series of the segments of rational numbers other than the empty class and the whole series.

## 16. Conclusion

This summary cites about 110 of the definitions in PM. The last eight pages (667–674) of Volume I of the second edition (1925) consists of a complete list of 498 definitions from all three volumes. Correspondence in the Bertrand Russell Archives confirms that this was compiled by Dorothy Wrinch. Her list can be used to trace every one of the other defined expressions of PM back to the notation discussed in this entry.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=pm-notation). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/pm-notation/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=pm-notation&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/pm-notation/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- [*Principia Mathematica*](http://quod.lib.umich.edu/cgi/t/text/text-idx?c=umhistmath;cc=umhistmath;view=toc;idno=AAT3201.0001.001), first edition (1910–13), reproduced in the University of Michigan Historical Math Collection.
- [Russell’s “On Denoting”](http://cscs.umich.edu/~crshalizi/Russell/denoting/), from the reprint in *Logic and Knowledge* (R. Marsh, ed., 1956) of the original article in *Mind* 1905, typed into HTML by Cosma Shalizi (Center for the Study of Complex Systems, U. Michigan)

## Related Entries

Frege, Gottlob | Frege, Gottlob: theorem and foundations for arithmetic | generalized quantifiers | measurement: in science | *Principia Mathematica* | Russell, Bertrand | schema | set theory: alternative axiomatic theories | type theory | Whitehead, Alfred North

### Acknowledgments

The author would like to thank: Gregory Landini, Dick Schmitt, Franz Fritsche, Rafal Urbaniak, Adam Trybus, Pawel Manczyk, Kenneth Blackwell, Dirk Schlimm, and Paolo Argolo for corrections to this entry. Axel Boldt studied the most recent revisions and found numerous mathematical errors and among other insights pointed out the use of double dots for conjunction at [∗10·55] and the oddity involved in the PM notions of the domain and range of a function.

[^boolos-2007]: Boolos G. , Burgess, J., and Jeffrey, R., 2007, *Computability and Logic*, 5th edition, Cambridge: Cambridge University Press.

[^carnap-1947]: Carnap, R., 1947, *Meaning and Necessity*, Chicago: University of Chicago Press.

[^church-1976]: Church, A., 1976, “Comparison of Russell’s Resolution of the Semantical Antinomies with That of Tarski”, *Journal of Symbolic Logic*, 41: 747–60.

[^chwistek-1924]: Chwistek, L., 1924, “The Theory of Constructive Types”, *Annales de la Société Polonaise de Mathématique* (*Rocznik Polskiego Towarzystwa Matematycznego*), II: 9–48.

[^curry-1937]: Curry, H.B., 1937, “On the use of Dots as Brackets in Logical Expressions”, *Journal of Symbolic Logic*, 2: 26–28.

[^elkind-2023]: Elkind, Landon D.C., and Zach, R., 2023, “The Genealogy of $ \vee $”, *Review of Symbolic Logic*, 16(3): 862–899.

[^feys-1969]: Feys, R. and Fitch, F.B., 1969, *Dictionary of Symbols of Mathematical Logic*, Amsterdam: North Holland.

[^fraenkel-1968]: Fraenkel, A.A., 1968, *Abstract Set Theory*, Amsterdam: North Holland.

[^gödel-1944]: Gödel, K., 1944, “Russell’s Mathematical Logic”, in P.A. Schilpp, ed., *The Philosophy of Bertrand Russell*, LaSalle: Open Court, 125–153.

[^krivine-1971]: Krivine, J-L., 1971, *Introduction to Axiomatic Set Theory*, Dordrecht: D. Reidel.

[^landini-1998]: Landini, G., 1998, *Russell’s Hidden Substitutional Theory*, New York and Oxford: Oxford University Press.

[^linsky-1999]: Linsky, B., 1999, *Russell’s Metaphysical Logic*, Stanford: CSLI Publications.

[^linsky-2009]: –––, 2009, “From Descriptive Functions to Sets of Ordered Pairs”, in *Reduction – Abstraction – Analysis*, A. Hieke and H. Leitgeb (eds.), Ontos: Munich, 259–272.

[^linsky-2011]: –––, 2011, *The Evolution of Principia Mathematica: Bertrand Russell’s Manuscripts and Notes for the Second Edition*, Cambridge: Cambridge University Press.

[^quine-1951]: Quine, W.V.O., 1951, “Whitehead and the Rise of Modern Logic”, *The Philosophy of Alfred North Whitehead*, ed. P.A. Schilpp, 2nd edition, New York: Tudor Publishing, 127–163.

[^russell-1905]: Russell, B., 1905, “On Denoting”, *Mind* (N.S.), 14: 530–538.

[^suppes-1960]: Suppes, P., 1960, *Axiomatic Set Theory*, Amsterdam: North Holland.

[^turing-1942]: Turing, A.M., 1942, “The Use of Dots as Brackets in Church’s System”, *Journal of Symbolic Logic*, 7:146–156.

[^whitehead-1910]: Whitehead, A.N. and B. Russell, [PM], *Principia Mathematica*, Cambridge: Cambridge University Press, 1910–13, 2nd edition, 1925–27.

[^whitehead-1962]: Whitehead, A.N. and B. Russell, 1962, *Principia Mathematica to ∗56*, Cambridge: Cambridge University Press.

[^zermelo-1904]: Zermelo, E., 1904, “Proof that every set can be well-ordered”, in *From Frege to Gödel*, J. van Heijenoort (ed.), Cambridge, Mass: Harvard University Press, 1967, 139–141.
