# possible-worlds — semantics-abstractionist-intensionality（supplement）

> （《possible-worlds》词条补充材料，源：plato.stanford.edu/entries/possible-worlds/semantics-abstractionist-intensionality.html）

#### Supplement to Possible Worlds

## The Intensionality of Abstractionist Possible World Semantics

The intensionality of possible world semantics under an abstractionist ontology is vividly illustrated by extending the formal analysis provided in the supplementary document [The Extensionality of Possible World Semantics](possible-worlds.semantics-extensionality.md). Recall that the formalized first-order metalanguage in that document included the set membership predicate ∈ as well as some additional metalinguistic primitives. However, we will not need the world predicate ‘*World*’ or the constant ‘@’ for the actual world, as these are definable for the abstractionist. Abstractionist semantics requires the following:

| *SOA*(*x*): |   | *x* is a state of affairs |
| --- | --- | --- |
| *Ob(s*): |   | (state of affairs) *s* obtains |
| *T*(φ,*w*): |   | (formula) φ is true at (world) *w* |
| *dom*(*w*): |   | the domain of world *w* |
| *ext*(π,*w*): |   | the extension of (*n*-place predicate) π at world *w* |
| *den*(τ): |   | the denotation of (constant or variable) τ |

We assume there are appropriate abstractionist axioms for these primitives, e.g., that only SOAs can obtain — ◻∀*x*(*Ob*(*x*) → *SOA*(*x*)) — that anything that could be an SOA is an SOA, ◻∀*x* (◇*SOA*(*x*) → *SOA*(*x*)) — and so on. To formalize the abstractionist notion of a possible world and to pick out the actual world, four auxiliary definitions are needed:

| **•** |   | *Poss*(*s*) =_{*def*} ◇*Ob*(*s*) |
| --- | --- | --- |

| **•** |   | *Inc*(*s*,*t*) =_{*def*} ◻(*Ob*(*s*) → *Ob*(*t*)) |
| --- | --- | --- |

| **•** |   | *Pre*(*s*,*t*) =_{*def*} ◻(*Ob*(*s*) → ~*Ob*(*t*)) |
| --- | --- | --- |

| **•** |   | *Max*(*s*) =_{*def*} ∀*t*(*Inc*(*s*,*t*) ∨ *Pre*(*s*,*t*)) |
| --- | --- | --- |

Given these we have:

| **•** |   | *World*(*s*) =_{*def*} *Poss*(*s*) ∧ *Max*(*s*) |
| --- | --- | --- |

| **•** |   | @ =_{*def*} the *s*(*World*(*s*) ∧ *Ob*(*s*)) |
| --- | --- | --- |

As before, truth can be defined as truth in the actual world:

- *True*(φ) =_{*def*} *T*(φ,@).

Now, recall that the formalized definition of truth in basic possible world semantics yielded the following clause for (6):

- *True*(‘◻∀*x*(*Px* → *Mx*)’) ↔ ∀*w*∀*x*((*World*(*w*) ∧ *x* ∈ *dom*(*w*)) → (*x* ∉ *ext*(‘*P*’,*w*) ∨ *x* ∈ *ext*(‘*M*’,*w*))).

Spelling out the '*World*' predicate according to our definition, then, we have:

- *True*(‘◻∀*x*(*Px* → *Mx*)’) ↔ ∀*w*∀*x*((*Poss*(*w*) ∧ *Max*(*w*) ∧ *x* ∈ *dom*(*w*)) → (*x* ∉ *ext*(‘*P*’,*w*) ∨ *x* ∈ *ext*(‘*M*’,*w*))).

And unpacking the definitions of '*Poss* and '*Max*' in turn yields:

- *True*(‘◻∀*x*(*Px* → *Mx*)’) ↔ ∀*w*∀*x*((◇*Ob*(*w*) ∧ (∀s◻(*Ob*(*s*) → *Ob*(*t*)) ∨ ∀s◻(*Ob*(*s*) → ~*Ob*(*t*))) ∧ *x* ∈ *dom*(*w*)) → (*x* ∉ *ext*(‘*P*’,*w*) ∨ *x* ∈ *ext*(‘*M*’,*w*))),

and the irreducibly intensional character of the truth condition becomes evident.

Return to the article “Possible Worlds”
