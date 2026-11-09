# common-knowledge — example2-1（supplement）

> （《common-knowledge》词条补充材料，源：plato.stanford.edu/entries/common-knowledge/example2-1.html）

#### Supplement to Common Knowledge

## Example of a Nonpartitional Knowledge function

Let us assume that axioms K1–K4 are valid, but the axiom of wisdom (K5) is not. It may be the case that an agent does not know that she does not know. The workings of nonpartitional knowledge systems of the kind discussed here are frequently illustrated with the example of Sir Conan Doyle’s “curious incident.” The dialogue between Watson and Holmes goes as follows:

> “Is there any other point to which you would wish to draw my attention?”
>
> “To the incident of the dog in the night-time.”
>
> “The dog did nothing in the night-time.”
>
> “That was the curious incident,” remarked Sherlock Holmes.

Consider a space set with two possible worlds, $\omega_1$ and $\omega_2$. At $\omega_1$ there has been a break in the previous night, while at $\omega_2$ there has been no break in. While Holmes realizes that the dog not barking in the night-time means that there was no intrusion, Watson fails to draw such an inference. At $\omega_2$ Holmes knows there was no intrusion, Watson does not. What about $\omega_1$? Had the dog barked, both Holmes and Watson would have realized that there had been an intrusion. Hence Holmes’ possibility set partitions the space set as follows:

$$ \mathcal{H}_H = \{\{\omega_1\},\{\omega_2\}\}. $$

What about Watson’s possibility set? Had the dog barked, he would have known that the state was $\omega_1$, i.e. that there had been an intruder in the night-time. Being less sharp that Holmes, however, Watson does not realize that, at $\omega_2$ (since the dog did not bark) there has been no intruder. Not knowing that there has not been an intruder means that, at $\omega_2$, Watson cannot distinguish between $\omega_1$ and $\omega_2$. Hence, his possibility set does *not* partition the state space, and is as follows:

$$ \mathcal{H}_W = \{\{\omega_1\},\{\omega_1, \omega_2\}\}. $$

It is easy to see that Watson is violating the axiom of wisdom (K5): let us denote the event “there was an intruder” with $E$ and its complement “there was not an intruder” with $F$. Obviously, $E = \{\omega_1\}$ and $F = \{\omega_2\}$. We also have that, at $\omega_1, \mathbf{K}_W E$ holds, while at $\omega_2$ Watson does not know anything, hence both $-\mathbf{K}_W E$ and $-\mathbf{K}_W F$ hold. Axiom K5 requires that, at $\omega_2, \mathbf{K}_W -\mathbf{K}_W E$ hold. However, $\mathbf{K}_W E = \{\omega_1\}$, hence $-\mathbf{K}_W E = \{\omega_2\} = F.$ Hence $\mathbf{K}_W -\mathbf{K}_W E = \mathbf{K}_W F.$ But at $\omega_2$ we have that $-\mathbf{K}_W F,$ hence $-\mathbf{K}_W -\mathbf{K}_W E,$ and K5 fails.
