# curry-paradox — supplement（supplement）

> （《curry-paradox》词条补充材料，源：plato.stanford.edu/entries/curry-paradox/supplement.html）

#### Supplement to Curry’s Paradox

## Curry on Curry’s Paradox

### Curry’s Target Systems

When Curry (1942b) introduced the paradox to demonstrate the inconsistency of “certain systems of formal logic”, the systems he had in mind were theories of functional application, specifically Church’s untyped lambda calculus and Curry’s own combinatory logic (Church 1932; Curry 1930; Seldin 2006). Besides variables, the syntax of both systems consists only of terms that denote entities (e.g. numbers, properties and propositions). A binary operation on terms forms a term standing for the result of applying one entity to another. For example, applying the property *evenness* to the number *two* yields a true proposition.

Curry’s key assumption is that the target systems are “combinatorially complete”. This means that “any function we can define intuitively by means of a variable can be represented formally as an entity of the system” using a denoting term (Curry & Feys 1958: 5). For example, there is a function that, applied to some entity $x$, yields the result of applying $x$ to $x$ itself. In the lambda calculus, this function is formally represented by the expression $\lambda x\mathord{.}xx$. The principle of combinatory completeness is Curry’s counterpart of the property abstraction principle (Property) stated in main entry section 2.

### Curry’s Response

Curry regarded his paradox as a constraint on an adequate theory of functional application. He insisted that the *wrong* lesson would be to give up the unrestricted property abstraction that lets the theory contain expressions such as one that corresponds to $h$ in section 2.1. Speaking informally, this term denotes the function that, when applied to a given argument $x$, yields the result of applying the implication function to the self-application of $x$ together with an arbitrary proposition $p$.

> The presence of these paradoxical terms is an advantage, because it enables the paradoxes to be represented in the system where it is possible to analyze them. (Curry 1942a: 56n14a)

Curry also criticized attempts to resolve the paradox by embracing a non-classical logic for the conditional. He claimed that the logics available to play this role were either *ad hoc* or failed to be “adequate for mathematics” (Curry & Feys 1958: 261).

To understand the lesson Curry drew from his paradox, one must keep in mind that his formulation doesn’t involve Curry *sentences*, but rather Curry *terms*. In place of the sentence $h \ \epsilon \ h$ of section 2.1, he employs a term denoting the result of applying a certain function to itself. According to him, the term in question is a meaningful denoting expression, but it fails to “denote a proposition” (Curry 1942a: 62). Yet the logical principles used in deriving the paradox are said to be principles that apply to propositions only.

Curry’s approach isn’t available in response to the versions of the paradox considered in the main entry. That’s because, as is now standard, expressions such as $h \ \epsilon \ h$, $c \in c$ and $T\langle\xi\rangle$ are there treated as sentences, not as names denoting entities. Nonetheless, a counterpart of his approach holds that these sentences, while meaningful, fail to *express* propositions. Several remarks by Kripke (1975; esp. pp. 699–700) suggest that this is one way to understand his response to truth-theoretic paradox. For a more recent defense of this approach, which is one example of what section 4 calls a *topic-specific approach*, see Goldstein 2000.

### Curry’s Professed Debt to Carnap

Curry remarks that “the central idea” of his derivation of the paradox was “suggested by some work of R. Carnap” (Curry 1942b). He cites Carnap 1934, the relevant portion of which appears in translation as §60a-d of the expanded English-language edition of Carnap’s *Logical Syntax of Language* (1937). This remark is puzzling, since Carnap’s discussion contains nothing resembling Curry’s proof of his central result, namely the Lemma of which the Curry-Paradox Lemma of section 3.1 is a variant. Carnap’s discussion does focus on Russell’s paradox of properties and Grelling’s semantic paradox, the same two sources Curry draws on in order to obtain his paradoxical sentences (see section 2).

However, Curry also directs the reader to Hilbert & Bernays 1939 for a “summary” of the work of Carnap that inspired his central result. That reference suggests he may have had in mind the precursor of the generalized diagonal lemma cited by Carnap in §60c of *Logical Syntax* (and presented in §35). Carnap writes in §60c:

> it is possible to construct, for any and every … property formulable in $S$, a sentence of $S$, $\mathfrak{S_1}$, such that $\mathfrak{S_1}$ attributes this property … to itself.

If this is the claim Curry had in mind, the “central idea” would be the general applicability of Gödel’s fixed-point result to any definable property, rather than just the property of *not being provable*. This may have suggested to Curry the possibility of a paradox that involves implication rather than negation. (See entries on paradoxes and contemporary logic and Gödel’s incompleteness theorems.)
