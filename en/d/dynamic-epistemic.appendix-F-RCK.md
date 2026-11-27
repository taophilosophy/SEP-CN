# dynamic-epistemic — appendix-F-RCK（supplement）

> （《dynamic-epistemic》词条补充材料，源：plato.stanford.edu/entries/dynamic-epistemic/appendix-F-RCK.html）

#### Supplement to Dynamic Epistemic Logic

## Appendix F: The axiomatic theories of Relativized Common Knowledge

We base this theory, just as for $\PAL$, on a PAL-friendly logic $\L$. Here we let $\LRCKP$ be the extension of $\LPAL$ obtained by adding relativized common knowledge formulas.

**The axiomatic theory $\RCKP$.**

- Axiom schemes and rules for a PAL-friendly logic $\L$
- Reduction axioms (all in the language $\LRCKP$):
- $[F!]p\leftrightarrow(F\to p)$ for letters $p\in\sP$ “After a false announcement, every letter holds—a contradiction. After a true announcement, letters retain their truth values.”
- $[F!](G\land H)\leftrightarrow([F!]G\land [F!]H)$ “A conjunction is true after an announcement iff each conjunct is.”
- $[F!]\lnot G\leftrightarrow(F\to\lnot[F!]G)$ “*G* is false after an announcement iff the announcement, whenever truthful, does not make *G* true.”
- $[F!][a]G\leftrightarrow(F\to[a][F!]G)$ “*a* knows *G* after an announcement iff the announcement, whenever truthful, is known by *a* to make *G* true.”
- $[F!][B*](G|H)\leftrightarrow (F\to[B*]([F!]G\mid F\land[F!]H))$ “*G* is *H*-relative common knowledge among *B* after an announcement iff the announcement, whenever truthful, ensures that, relative to the announcement being true and *H* holding after the announcement, it is common knowledge among *B* that the announcement makes *G* true.”
- Announcement Necessitation Rule: from *G*, infer $[F!]G$ whenever the latter is in $\LRCKP$. “A validity holds after any announcement.”
- Axiom schemes for relativized common knowledge:
- $[B*](F\to G\mid H)\to ([B*](F|H)\to [B*](G|H))$ “Relativized common knowledge is closed under logical consequence.”
- $[B*](F|H)\leftrightarrow [B](H\to(F\land[B*][F|H)))$, the “Mix axiom” “Relativized knowledge is equivalent to group knowledge that the relativization implies truth and relativized common knowledge.”
- $([B](H\to F)\land [B*](F\to[B](H\to F)\mid H))\to [B*](F|H)$, the “Induction axiom” “If there is common knowledge that truth implies group knowledge and there is truth, then there is common knowledge.”
- RCK Necessitation Rule: from *F*, infer $[B*](F|H)$ “There is relativized common knowledge of every validity.”

**The axiomatic theory** $\RCK$ is obtained from the axiomatic theory of $\RCKP$ by omitting the reduction axioms and restricting formulas to the language (RCK).

**$\RCK$ Soundness and Completeness (van Benthem, van Eijck, and Kooi 2006).** $\RCK$ is sound and complete with respect to the collection $\sC_*$ of pointed Kripke models for which the underlying modal logic $\L$ is sound and complete. That is, for each (RCK)-formula *F*, we have that $\RCK\vdash F$ if and only if $\sC_*\models F$.

As per the design, every formula in the language [RCK+P] of relativized common knowledge can be rewritten in an equivalent announcement-free form.

**RCK+P Reduction Theorem (van Benthem, van Eijck, and Kooi 2006).** Given a PAL-friendly theory $\L$, every *F* in the language $\LRCKP$ of relativized common knowledge with public announcements is $\RCKP$-provably equivalent to a formula $F^\circ$ coming from the announcement-free language (RCK) of relativized common knowledge.

In the same way that the completeness of $\PAL$ was reduced to the completeness of the underlying modal logic $\L$, the soundness of $\RCKP$ and the Reduction Theorem for $\RCKP$ together reduce the completeness of $\RCKP$ to the completeness of the announcement-free underlying logic $\RCK$.

**$\RCKP$ Soundness and Completeness (van Benthem, van Eijck, and Kooi 2006).** Given a PAL-friendly theory $\L$, the theory $\RCKP$ is sound and complete with respect to the collection $\sC_*$ of pointed Kripke models for which the underlying modal logic $\L$ is sound and complete. That is, for each $\LRCKP$-formula *F*, we have that $\RCKP\vdash F$ if and only if $\sC_*\models F$.

The Reduction Theorem also tells us that adding public announcements to the language (RCK) of relativized common knowledge does not let us express anything that we could not already express before. We state this result formally in the following theorem along with a few other results that relate the languages we have looked at thus far in terms of expressivity.

**Relative Expressivity Theorem.** Over the class of all pointed Kripke models, we have each of the following.

- (RCK+P) and (RCK) are equally expressive (van Benthem, van Eijck, and Kooi 2006).
- (RCK) is strictly more expressive than (PAL+C): $[C](\lnot[a]p\mid p)$ is equivalent to no (PAL+C)-formula (van Benthem, van Eijck, and Kooi 2006).
- (PAL+C) is strictly more expressive than (PAL): $[p!][C]q$ is equivalent to no (PAL)-formula (Baltag, Moss, and Solecki 1999; see also van Ditmarsch, van der Hoek, and Kooi 2007).
- (PAL) and (ML) are equally expressive (Plaza 1989, 2007; Gerbrandy and Groeneveld 1997).

A useful general reference on completeness via reduction axioms is Kooi (2007).

← beginning of main article
