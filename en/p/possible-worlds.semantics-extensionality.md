# possible-worlds — semantics-extensionality（supplement）

> （《possible-worlds》词条补充材料，源：plato.stanford.edu/entries/possible-worlds/semantics-extensionality.html）

#### Supplement to Possible Worlds

## The Extensionality of Possible World Semantics

As noted, possible world semantics does not make modal logic itself extensional; the substitutivity principles all remain invalid for modal languages under (basic) possible worlds semantics. Rather, it is the semantic theory itself — more exactly, the logic in which the theory is expressed — that is extensional. Specifically, basic possible world semantics for a given modal language ℒ, when formalized, is expressed in a (non-modal) first-order language ℒ_{PWS} that contains the set membership predicate ‘∈’ supplemented with dedicated predicates, function symbols, and constants, as well as mechanisms for talking about the expressions of ℒ and their possible world interpretations, notably:

| *World*(*w*): |   | *w* is a world |
| --- | --- | --- |
| *T*(φ,*w*): |   | (formula) φ is true at (world) *w* |
| *dom*(*w*): |   | the domain of world *w* |
| *ext*(π,*w*): |   | the extension of (*n*-place predicate) π at world *w* |
| *den*(τ): |   | the denotation of (constant or variable) τ |
| @: |   | the actual world |

Thus, for example, by formalizing the definition of truth simpliciter as truth in the actual world:

- *True*(φ) =_{*def*} *T*(φ,@)

the complete statement of the truth conditions for (6), expressed more formally in ℒ_{PWS}, take on the following form:

- *True*(‘◻∀*x*(*Px* → *Mx*)’) ↔ ∀*w*∀*x*((*World*(*w*) ∧ *x* ∈ *dom*(*w*)) → (*x* ∉ *ext*(‘ *P*’,*w*) ∨ *x* ∈ *ext*(‘*M*’,*w*))).

The semantic theory for this language ℒ_{PWS}, of course, is just our Tarskian semantics above. Thus, the logic of possible world semantics is simply an extensional first-order logic in a dedicated language. It is in this clear sense that basic possible world semantics is an extensional semantic theory for modal languages. It can therefore be said that modal logic with a basic possible world semantics is itself extensional in a derivative sense: the logic that gives full expression to the meanings of modal sentences is extensional in the primary sense that, in that logic, all substitutivity principles are valid.

Return to the article “Possible Worlds”
