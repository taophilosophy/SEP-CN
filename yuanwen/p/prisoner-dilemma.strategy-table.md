# prisoner-dilemma — strategy-table（supplement）

> （《prisoner-dilemma》词条补充材料，源：plato.stanford.edu/entries/prisoner-dilemma/strategy-table.html）

#### Supplement to Prisoner’s Dilemma

## Strategies for the Iterated Prisoner’s Dilemma

| **Name** | **Abbreviation** | **Description** |
| --- | --- | --- |
| Unconditional Cooperator | **Cu** | Cooperates unconditionally. |
| Unconditional Defector | **Du** | Defects unconditionally. |
| Random | **Random** (=**C.5** or **R(.5,.5,.5)** or **S(.5,.5,.5,.5)** below) | Cooperates with probability one-half. |
| Probability *p* Cooperator | C**p** for $0\le$p$\le 1$ | Cooperates with fixed probably $p$. |
| Tit for Tat | **TFT** (=**R(1,1,0)** or **S(1,0,1,0)** below) | Cooperates on the first round and imitates its opponent’s previous move thereafter. |
| Suspicious Tit for Tat | **STFT** (=**R(0,1,0)** below) | Defects on the first round and imitates its opponent’s previous move thereafter. |
| Generous Tit for Tat | **GTFT** (=**R(1,1,g(R,P,T,S))** below) | Cooprates on the first round and after its opponent cooperates. Following a defection, it cooperates with probability $g(R, P, T, S)= \min\{1-\frac{T-R}{R-S}, \frac{R-P}{T-P}\}$, where $R,$ $P,$ $T$ and $S$ are the reward, punishment, temptation and sucker payoffs. |
| Gradual Tit for Tat | **GrdTFT** | TFT with two differences: (1) it increases the string of punishing defection responses with each additional defection by its opponent (2) it apologizes for each string of defections by cooperating in the subsequent two rounds. |
| Imperfect TFT | **ImpTFT** | Imitates opponent’s last move with high (but less than one) probability. |
| Tit for Two Tats | **TFTT** (or **TF2T**) | Cooperates unless defected against twice in a row. |
| Two Tits for Tat | **TTFT** (or **2TFT**) | Defects twice after being defected against, otherwise cooperates. |
| Omega Tit for Tat | **ΩTFT** | Plays TFT unless measures of deadlock or randomness exceed specified thresholds. When deadlock threshold is exceeded it cooperates and resets the measure. When randomness threshold is exceded, it switches to unconditional defection. For full specificiation see Slaney and Kienreich, p184. **ΩTFT** finished second in the 2005 reprise of the Axelrod IPD tournament. |
| GRIM (or TRIGGER) | **GRIM** (= **S(1,0,0,0)** below) | Cooperates until its opponent has defected once, and then defects for the rest of the game. |
| Discriminating Altruist | **DA** | In the Optional IPD, cooperates with any player that has never defected against it, and otherwise refuses to engage. |
| Pavlov (or Win-stay, Lose-shift) | **WSLS** ( =**P₁** below) | Cooperates if it and its opponent moved alike in previous move and defects if they moved differently. |
| n-Pavlov | **Pₙ** | Adjusts its probability of cooperation in units of $\tfrac{1}{n}$ according to its payoff on the previous round. More specifically it cooperates with probability $p_1=1$ on round 1 and probability $p_{n+1}$ on round $n+1$, where <table class="no-rules"> <tr> <td>$p_{n+1}=$</td> <td>$p_n\,[+]\tfrac{1}{n}$ if payoff on last round was Reward $(R)$,</td> </tr> <tr> <td></td> <td>$p_n\,[-]\tfrac{1}{n}$ if payoff on last round was Punishment $(P)$,</td> </tr> <tr> <td></td> <td>$p_n\,[+]\tfrac{2}{n}$ if payoff on last round was Temptation $(T)$,</td> </tr> <tr> <td></td> <td>$p_n\,[-]\tfrac{2}{n}$ if payoff on last round was Sucker $(S)$.</td> </tr> </table> $p_n$ is the probability of cooperation on round n, $x[+]y = min(x+y,1)$ and x[-]y=max(x-y,0). |
| Adaptive Pavlov | **APavlov** | Employs **TFT** for the first six rounds, places opponent into one of five categories according to its responses and plays an optimal strategy for each. Details described in Li pp 89-104. **APavolv** was the highest scoring strategy in the 2005 reprise of Axelrod’s IPD tournament. |
| Reactive (with parameters y,p,q) | **R(y,p,q)** | Cooperates with probability y in first round and with probabilities p or q after opponent cooperates or defects. |
| Memory-one (with parameters p,q,r,s) | **S(p,q,r,s)** | Cooperates with probabilities probabilities p,q,r or s after outcomes (C,C), (C,D), (D,C) or (C,D). |
| Zero Determinant | **ZD** | A class of memory-one strategies that guarantee that a player’s long-term average payoff in the infinitely repeated, two-player prisoner’s dilemma (2IPD) will be related to his opponent’s according to a fixed linear equation. |
| Equalizer (or dictator) | **SET-n** (for P≤n≤R) | A **ZD** strategy that guarantees the opponent’s long term average payoff is n. As it turns out, in a PD with payoffs 5,3,1 and 0, **SET-2**=**S(¾¼½¼)**. |
| Extortionary | **Extort-n** | An extortionary strategy is a **ZD** strategy that guarantees that an opponent’s average payoff can exceed the punishment payoff only if one’s own long term average payoff is greater. **Extort-n** guarantees that one’s gain over punishment is n times one’s opponent’s. As it turns out, for a PD with the payoffs above, **EXTORT-2**=**S(⁷⁄₈, ⁷⁄₁₆,³⁄₈,0)**). |
| Generous | **Gen-n** | A generous strategy is a **ZD** strategy that guarantees that an opponent’s average payoff can be lower than the reward payoff only if one’s own long term average payoff is even lower. **GEN-n** guarantees that one’s loss relative to the reward is n times one’s opponent’s. As it turns out, for a PD with the payoffs above, **GEN-2**=**S(1, ⁹⁄₁₆,¹⁄₂,¹⁄₈)**). |
| Good | **GOOD** | A good strategy for the infinitely-repeated, two-player PD is a strategy with the following properties: (1) its use by both players ensures that each gets reward as long-term average payoff, (2) it is a Nash equilibrium with itself, and (3) if it is employed by both, any deviation by one that reduces the average payoff of the other will also reduce its own average payoff. Aikin, 2013 provides a simple characterization of the memory-one strategies that are good. |
| Lookup tables | **LookerUp** | **LookerUp** is a family of strategy-archetypes. For positive integers k,m,n a LookerUp strategy can be obtained by using a learning algorithm to calculate the best reponse to the opponents first k moves and last m moves and the player’s own last n moves while playing a PD-tournament within some universe of strategies. |
| Neural Net | **ANN** | A neural net strategy is obtained by using a learning algorithm to set connection weights on a feed-forward neural network with one hidden layer while playing PD tournaments within some universe of strategies. Further details can be found in Harper et al. |
| Finite State Machine | **FSM** | A finite state machine strategy is obtained by using a learning algorithm to set PD-moves and state-transitions while playing PD tournaments within some universe of strategies. Further details can be found in Harper et al. |

Return to Prisoner’s Dilemma Entry
