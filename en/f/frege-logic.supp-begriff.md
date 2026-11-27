# frege-logic — supp-begriff（supplement）

> （《frege-logic》词条补充材料，源：plato.stanford.edu/entries/frege-logic/supp-begriff.html）

#### Supplement to Frege’s Logic

## The Supposed Contradiction in *Begriffsschrift*

Jean van Heijenoort argues, in his introductory essay on *Begriffsschrift*, that Frege applies his rule of substitution in illicit ways—ways that will lead to contradictions:

> Frege allows a functional letter to occur in his quantifier[…] This license is not a necessary feature of quantification theory, but Frege has to admit it in his system for the definitions and derivations of the third part of the book. The result is that the difference between function and argument is blurred[…] It is true that Frege writes[…] that, if a functional letter occurs in a quantifier, “this circumstance must be taken into account”. But the phrase remains vague. The most generous interpretation would be that, in the scope of the quantifier in which it occurs, a functional letter has to be treated as such, that is, must be provided with a pair of parentheses and one or more arguments. Frege, however, does not say as much, and in the derivation of formula (77) he substitutes $\mathfrak{F}$ for $a$ in $f(a)$, at least as an intermediate step. If we also observe that in the derivation of formula (91) he substitutes $\mathfrak{F}$ for $f$, we see that he is on the brink of a paradox. (Van Heijenoort 1967b: 3)

The examples that van Heijenoort cites are from well into the third section of *Begriffsschrift*, and involve the definition of the ancestral, hence explaining them would take us far beyond an introduction to the basic mechanics of Frege’s logic, but we can sketch the general worry as follows. Earlier in *Begriffsschrift* Frege proves formula 63:

![judgement conditional {term g(x)} {term conditional {term m} {term conditional {all gothic a term conditional {term g(gothic a)} {term f(gothic a)}} {term f(x)}}}](../assets/frege-logic/supp-begriff-formula63.svg)

and formula 68:

![judgement conditional {term [(all gothic a f(gothic a)) equiv b]} {term conditional term b term f(c)}](../assets/frege-logic/supp-begriff-formula68.svg)

Then, in proving Formula 77, Frege uses a substitution instance of Formula 68 that involves replacing the (apparently objectual) concavity-bound variable $\mathfrak{a}$ with the (apparently conceptual) concavity-bound variable $\mathfrak{F}$. In an intermediate step of the proof of Formula 91, however, Frege applies the concavity introduction rule to Formula 63, replacing the (apparently conceptual) Roman letter $f$ with a concavity-bound $\mathfrak{F}$ applying to the consequent of the conditional. The worry, of course, is that if each of these substitutions is allowed individually, what is to stop us from making both substitutions simultaneously in a formula of the form:

![judgement all gothic a \Phi(f(gothic a))](../assets/frege-logic/supp-begriff-formA1.svg)

obtaining:

![judgement all gothic F all gothic G term \Phi(gothic G(gothic F))](../assets/frege-logic/supp-begriff-formA2.svg)

which would entail worrisomely circular:

![judgement all gothic F term \Phi(gothic F(gothic F))](../assets/frege-logic/supp-begriff-formA3.svg)

As Bynum notes in a footnote to his translation of *Begriffsschrift* (By72), Frege never performs such problematic substitutions, and steers well clear of paradox in the derivations of *Begriffsschrift*, even if he is not yet able to clearly articulate the constraints on substitution that allow him to do so:

> To prove 77, Frege cites 68; but he could not use 68 itself. He needs an analogous second-order principle (call it 68′) involving quantification over *functions*[…] To state his thought precisely, however, required the notational machinery (which he had not yet devised) to distinguish first- from second-level functions. With that available, the difficulty can be easily resolved. Van Heijenoort […] is in error in supposing that any paradox can arise in the system. In the *Conceptual Notation* Frege never confuses first- and second-level functions, though he does not yet have separate terms for them. (By72: 175, fn. 2)

So, should we understand the logic of *Begriffsschrift* as having the type restrictions made explicit in *Grundgesetze* already at work implicitly, as Bynum suggests, or is van Heijenoort correct, and the logic actually presented by Frege in 1879 is inconsistent? The answer is somewhat more complicated.

One of the distinctive innovations Frege introduced in the logic of *Begriffsschrift* is the analysis of sentences in terms of function and argument, rather than in terms of subject and predicate, but what is missing is explicit recognition of the different types of argument, and different types of function, that would become central to the logic of *Grundgesetze*. Thus, when Frege writes something like “$f(a)$” in *Begriffsschrift*, this should be understood as indicating that “$f$” denotes the function, and “$a$” denotes the argument, but it does not specify whether $a$ denotes an object or a function, hence whether “$f$” denotes (in Frege’s later terminology) a first- or second-level function. Thus, in a *Begriffsschrift* expression of the form:

![all gothic f all gothic a term gothic f(gothic a)](../assets/frege-logic/supp-begriff-formB.svg)

it is not the case that “$\mathfrak{a}$” ranges over objects and “$\mathfrak{f}$” ranges over (first-level) functions. Rather, “$\mathfrak{a}$” ranges over *arguments* (which could be either objects or functions), and “$\mathfrak{f}$” ranges over functions pairwise appropriate to those arguments.

The substitutions that Frege performs at both Theorem 77 and Theorem 91 are, on this interpretation of the logic of *Begriffsschrift*, legitimate, since in both cases Frege has substituted an argument for one variable and a function appropriate to that argument for the other. We can speculate that the sort of self-application inducing substitutions that lead van Heijenoort to worry that the logic of *Begriffsschrift* is inconsistent, however, would presumably not strike the *Begriffsschrift*-era Frege as legitimate, since for no function $\mathfrak{F}$ can $\mathfrak{F}$ play the both the role of function and the role of argument simultaneously (Frege does not, of course, explicitly forbid the analyses of sentences into function and argument where the function is identical to the argument, but we can speculate that he would find such “fixed points” as strange as we typically do).
