# common-knowledge — rubinsteinsproof（supplement）

> （《common-knowledge》词条补充材料，源：plato.stanford.edu/entries/common-knowledge/rubinsteinsproof.html）

#### Supplement to Common Knowledge

## Rubinstein’s Proof

[Note: See Definition 3.2 for the notation used in this proof.]

Let $T_2$ denote the number of messages that Joanna’s e-mail system sends, and $T_1$ denote the number of messages that Lizzi’s e-mail system sends. We might suppose that $T_i$ appears on each agent’s computer screen. If $T_1 = 0$, then Lizzi sends no message, that is, $\omega_1$ has occurred, in which case Lizzi’s unique best response is to choose $A$. If $T_2 = 0$, then Joanna did not receive a message. She knows that in this case, either $\omega_1$ has occurred and Lizzi did not send her a message, which occurs with probability .51, or $\omega_2$ has occurred and Lizzi sent her a message which did not arrive, which occurs with probability $.49\varepsilon$. If $\omega_1$ has occurred, then Lizzi is sure to choose $A$, so Joanna knows that whatever Lizzi might do at $\omega_2$,

$$\begin{align} E(u_2 (A) \mid T_2 =0) &\ge \frac{2(.51) + 0(.49)\varepsilon}{.51 + .49\varepsilon} \\ &\gt \frac{-4(.51) + 2(.49)\varepsilon}{.51 + .49\varepsilon} \\ &\ge E(u_2(B) \mid T_2 =0) \end{align}$$

so Joanna is strictly better off choosing A no matter what Lizzi does at either state of the world.

Suppose next that for all $T_i \lt t$, each agents’ unique best response given her expectations regarding the other agent is $A$, so that the unique Nash equilibrium of the game is $(A,A)$. Assume that $T_1 = t$. Lizzi is uncertain whether $T_2 = t$, which is the case if Joanna received Lizzi’s $t$ᵗʰ automatic confirmation and Joanna’s $t$ᵗʰ confirmation was lost, or if $T_2 = t - 1$, which is the case if Lizzi’s $t$ᵗʰ confirmation was lost. Then

$$\begin{align} \mu_1 (T_2 = t-1 \mid T_1 = t) &= z \\ &= \frac{\varepsilon}{\varepsilon + (1-\varepsilon)\varepsilon} \\ &\gt \frac{1}{2}. \end{align}$$

Thus[^note-rubinsteinsproof-1] it is more likely that Lizzi’s last confirmation did not arrive than that Joanna did receive this message. By the inductive assumption, Lizzi assesses that Joanna will choose $A$ if $T_2 = t-1$. So

$$\begin{align} E(u_1 (B) \mid T_1 = t) &\le -4z + 2(1-z) \\ &= -6z + 2 \\ &\lt -3 + 2 \\ &= -1, \end{align}$$

and

$$ E(u_1 (A) \mid T_1 = t) = 0 $$

since Lizzi knows that $\omega_2$ is the case. So Lizzi’s unique best action is $A$. Similarly, one can show that $A$ is Joanna’s best reply if $T_2 = t$. So by induction, $(A,A)$ is the unique Nash equilibrium of the game for every $t \ge 0$.

Return to Coordination and Common $p$-Belief
