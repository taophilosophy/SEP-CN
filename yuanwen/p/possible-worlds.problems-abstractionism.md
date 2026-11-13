# possible-worlds — problems-abstractionism（supplement）

> （《possible-worlds》词条补充材料，源：plato.stanford.edu/entries/possible-worlds/problems-abstractionism.html）

#### Supplement to Possible Worlds

## Problems with Abstractionism

### Lack of Formal Rigor

With the notable exception of Zalta (1983, 1993), a pervasive problem for nearly all abstractionist accounts is that they lack sufficient formal rigor. More specifically, abstractionists rely heavily upon an ontology of abstract entities but typically do not provide adequate formal underpinnings for their theories, notably, a formal language, model theory, logic, and a set of axioms. (Sider's (2002) linguistic ersatzism is not lacking in rigor but he does not axiomatize his theory and its heavily model theoretic approach is subject to well known cardinality problems to which Zalta's theory appears to be immune.)

To illustrate: Plantinga (1985) offers up a proof of the *extensional adequacy* of his notion of a possible world, that is, a proof of:

| **EA** |   | For every SOA *s*, *s* is possible iff there is a possible world that includes *s*. |
| --- | --- | --- |

The proof of the left-to-right direction, however — which is, in fact, offered as a general proof that possible worlds exist — depends upon a metaphysical analog of the compactness theorem for first-order logic that is demonstrably false in the context of Plantinga's rich ontology of states of affairs. (See Menzel 1989 for details.)

And again: Plantinga (1974, 45) offers up a proof that there is a unique actual world. However, as McNamara (1993) demonstrates, the argument rests essentially on the principle that necessarily equivalent SOAs are identical, a principle clearly at odds with the fine-grainedness of SOAs that Plantinga assumes elsewhere (and often) in various applications of his theory.

### The Threat of Paradox

A more pernicious threat arising from the lack of adequate formal rigor is the threat of paradox. Adams (1974), for example, defines a possible world (or "world story") to be maximal consistent set of propositions, where a set *S* of propositions is *maximal* just in case, for every proposition *p*, *S* contains either *p* or its negation ¬*p*, and *consistent* just in case it is possible that all of *S*'s members be jointly true. Suppose now the following three propositions (all of which appear to be embraced by Adams):

| (A) |   | For every set *S* of propositions there is a distinct proposition *p_{S}* (e.g., the proposition *that S is nonempty*). |
| --- | --- | --- |

| (B) |   | Every proposition *p* has a negation ¬*p*. |
| --- | --- | --- |

| (C) |   | If *S* and *S*′ are distinct sets of propositions, then p_{S}, p_{S′}, and their negations are all pairwise distinct. |
| --- | --- | --- |

Then a paradox follows. For let *w* be a world story. By (A), (B), and the maximality of *w*, for every subset *S* of *w* either *p_{S}* ∈ *w* or ¬*p_{S}* ∈ *w* and, by (C) and the consistency of *w*, this proposition is correlated uniquely with *S*. It follows that function *f*(*S*) = *p_{S}* maps the set ℘(*w*) of all subsets of *w* one-to-one into *w*. Hence ℘(*w*) is no larger than *w*, in violation of Cantor's Theorem. (For more on this paradox, see Bringsjord 1985, Menzel 1986, Grim 1986, Beall 2000, and Menzel 2012.) Because Plantinga (1974, 44–5) accepts (A)–(C) and postulates, for each of his worlds *w*, the existence of a corresponding world story (which he calls *the book on w*), this paradox arises for him as well. However, making reasonable assumptions about the nature of Plantinga's underlying metaphysics, Chihara (1998, 126–7) reconstructs a similar paradox directly for Plantinga's notion of a possible world.

Divers (2002, Ch. 15) presents a detailed and illuminating overview of the problem of paradox for abstractionism. Further difficulties for Adams' conception of a world story and for Plantinga’s notion of an haecceity can be found in the entry on the possibilism-actualism debate. A discussion of how Zalta's world theory avoids cardinality problems and paradox can be found in Bueno et al. (2014).

Return to Possible Worlds
