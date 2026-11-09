# infinity — decision-problems（supplement）

> （《infinity》词条补充材料，源：plato.stanford.edu/entries/infinity/decision-problems.html）

#### Supplement to Infinity

## Tacitly Infinite Decision Problems: Two Envelopes

You are offered a choice between two envelopes, $E_1$ and $E_2$. All that you know about them is that one contains twice as much money as the other. After you have chosen one of the envelopes, you are offered the opportunity to switch the envelope that you have chosen for the other envelope. Here is a tempting line of reasoning that suggests that you should make this trade. Suppose that you have chosen $E_1$. Call the amount of money in $E_1$ $\$x.$ Then the amount of money in $E_2$ is either $\$2x$ or $\$0.5x.$ Moreover—since your choice between the two envelopes was undertaken in complete ignorance of the contents of the two envelopes—you should regard the two possible outcomes as equally likely. So, while the expected utility of hanging on to $E_1$ is $\$x,$ the expected utility of exchanging $E_1$ for $E_2$ is

$$ 0.5 \times \$2x + 0.5 \times \$0.5x = \$1.25x.$$

(We assume that money is linear in utility.) Since the expected utility of trading $E_1$ for $E_2$ is greater than the expected utility of hanging on to $E_1$, you should switch.

But, tempting as this line of reasoning may be, it cannot be correct. The mere choosing of $E_1$ cannot give you a reason to prefer $E_2$ to $E_1$. Had you chosen $E_2$ instead, exactly the same form of reasoning would tell you that you should trade $E_2$ for $E_1$. Indeed, if you do trade $E_2$ for $E_1$, then a parallel argument will tell you that you now ought to trade $E_2$ for $E_1$. And so on, ad infinitum.

So there is something wrong with the tempting line of reasoning. But what? The key steps were:

1. For any $x$, $P(E_2 \text{ has } 2x \mid E_1 \text{ has } x) = \frac{1}{2},$ and $P(E_2 \text{ has } \frac{1}{2}x \mid E_1 \text{ has } x) = \frac{1}{2}.$

Therefore,

1. For any $x,$ the conditional expected utility of $E_2,$ given that $E_1$ has $x,$ is greater than that of $E_1.$ (Conditional expected utility replaces the unconditional probabilities in the expected utility formula with conditional probabilities, given the condition.)

Therefore,

1. The expected utility of $E_2$ is greater than that of $E_1.$

Therefore,

Conclusion. You should switch from $E_1$ to $E_2$.

However, 1 and 2 are clearly false in real life, with real money. If $x$ is the smallest unit of currency (a cent), then $E_2$ cannot have half as much. If $x$ is more than half of all of the money in the world, then $E_2$ cannot have twice as much. You surely do not have a uniform probability distribution over all the possible values of $x,$ as 1 assumes, and so we have no basis for 2.

Now, we may simply idealize, and imagine that our prizes are infinitely divisible (say, gunky gold), and that there is no bound on their utilities. But if your probability distribution has finite mean, then 1 and 2 are still false. (See Chalmers 2002.)

We are still not out of the woods, however. There are certain distributions with *infinite* expected value such that 1 is false, but 2 is still true (Broome 1995). But for those distributions, the inference from 2 to 3 is invalid. It is an instance of conglomerability of expected utility:

(Expectation conglomerability) If for every possible outcome $O_i$,

$$ EU(Y \mid O_i) \gt EU(X \mid O_i)$$

then

$$EU(Y) \gt EU(X),$$

where $EU(\_\mid O_i)$ is the conditional expected utility, given $O_i$.

The thought is roughly that we can ‘discharge’ the supposition about $O_i$, since whatever it is, we get the same verdict regarding the expected utilities.

However, conglomerability of expected utility fails in such infinite cases. Conditional on each value in $E_2$, the expectation of $E_2$ is indeed greater than that of $E_1$. But it is *not* the case that $EU(E_2) \gt EU(E_1),$ since they are both infinite. (Since these expected values are infinite sums of finite real numbers, they must be the extended real number $+\infty$ rather than coming from one of the systems with multiple positive infinities of different sizes.)

To summarize: the expected utility of the amount in each of the envelopes is either finite or infinite. If it is finite, then 1 and 2 are false. If it is infinite, then the argument from 2 to 3 is invalid. See Arntzenius and McCarthy (1997) and Chalmers (2002).

For further discussion of the two-envelope—‘trading’, ‘exchange’—paradox, see, for example, Littlewood (1953), Nalebuff (1989), Cargile (1992), Christensen and Utts (1992), Castell and Batens (1994), Jackson, Menzies and Oppy (1994), Broome (1995), Arntzenius and McCarthy (1997), McGrew, Shier and Silverstein (1997), Scott and Scott (1997), Wagner (1999), Clark and Schackel (2000), Chalmers (2002), Chase (2002), McDonnell and Abbott (2009), Markosian (2011), and Powers (2015). For more about decision theory, see the entries on decision theory, interpretations of probability, and philosophy of statistics.
