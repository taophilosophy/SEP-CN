# infinity — gods-lottery（supplement）

> （《infinity》词条补充材料，源：plato.stanford.edu/entries/infinity/gods-lottery.html）

#### Supplement to Infinity

## God’s Lottery

Storrs McCall and D.M. Armstrong (1989) considered a lottery in which God chooses a number from the set of all positive integers (this is also called *de Finetti’s lottery*). God’s lottery is assumed to be fair in that the chance of any given number being chosen is the same as that of any other number. (To generate interest high stakes were set: the winner would receive eternal salvation.) God offers participants the following five choices:

1. All tickets numbered 1 to 100, or all tickets numbered 101 to 1,000,000.
2. All even numbered tickets, or all tickets the numbers of which are multiples of three.
3. Multiples of three or multiples of 47198.
4. Multiples of 47198 or all numbers less than $10^{1010}$.
5. Multiples of six or multiples of three.

What attitude should be taken with respect to the previous choices? McCall and Armstrong pointed out a certain tension between our intuitions (about finite and infinite lotteries) and a Cantorian approach to the problem. Rather than rehearsing McCall’s and Armstrong’s entertaining discussion, we will give a more systematic overview of the problem. The problems raised by God’s lottery are very deep and go to the very core of our intuitions about probability and infinity. In order to clarify what the problems are, we have to describe the mathematical situation more carefully. Recent work promises to substantially alter our understanding of them.

### Finite lotteries

Let us consider the situation with fair finite lotteries. Suppose we have a lottery with tickets numbered 1 to 90. Let us call the *sample space* the tickets numbered from 1 to 90, which can be represented by the set $\{1, \ldots ,90\}$, and the *event space* the power set of $\{1, \ldots ,90\}$. In a fair finite lottery, each event’s probability is proportional to its cardinality: a subset of size $k$ has probability $k/90$. This assignment of probability satisfies all of Kolmogorov’s three axioms for a probability measure discussed in the main text. The sample space has probability 1; the co-domain of the function is included in a set of rationals (hence, the reals) between 0 and 1; and countable additivity holds trivially. If we choose an arbitrary $n$ in place of 90, we have the general situation for fair finite lotteries.

If we try to spell out the intuitive principles on which our conception of fair finite lotteries rests, we can list the following (see Wenmackers and Horsten 2013, which we follow in this discussion):

**FAIR:**

the lottery is fair; every individual ticket has the same probability of winning as any other one;

**ALL:**

every combination of tickets has a probability of winning;

**SUM:**

the probability of a combination of tickets can be found by summing the individual probabilities;

**LABEL:**

the labeling of tickets does not affect the probability value assigned to an event.

In the case of our fair lottery with 90 numbers, FAIR and ALL hold, because every individual ticket has been assigned probability 1/90 and every combination of $n$ tickets has probability $n/90$ of winning. SUM holds because any subset of tickets, perforce finite, has a probability given by summing the individual probabilities of its tickets. LABEL holds because if we were to label any ticket with number $n$ $(1 \le n \le 90)$ by some other natural number $m$, with $1 \le m \le 90$, (and vice versa), its probability would not change.

### From finite to infinite lotteries

What happens when we try to generalize the above setting for finite lotteries to God’s lottery? As we have seen in section 7, de Finetti (1974) observed that a fair infinite lottery on the natural numbers cannot satisfy all of Kolmogorov’s axioms for probability. De Finetti’s solution was to abandon countable additivity (thus, SUM) and require only finite additivity. The reason motivating the abandonment of countable additivity is that in the context of God’s lottery, if we decide to hold on to FAIR, we have to give all tickets the same probability of winning. This probability is either 0 or $k$, for $0 \lt k \lt 1$.

Consider now the singletons $\{ n \}$ for each natural number $n$. If the probability of $\{ n \}$ is 0, then by countable additivity the entire space has probability zero, contradicting Kolmogorov’s axiom assigning 1 to the entire space. If the probability is a number between 0 and 1, then by the Archimedean nature of the real number field, and countable additivity, we end up with a probability for the total space $\gt 1$ – again, contradicting this axiom. As described in the main text, a way out for de Finetti is, by abandoning countable additivity, to assign probability 0 to each single ticket and 1 to the entire space. Thus, holding on to FAIR while giving up SUM, in the form of countable additivity, still leads to the very unintuitive conclusion that each ticket has probability 0 of occurring.

Incidentally, notice that LABEL fails badly in the infinite set up. On account of cardinality considerations, every countably infinite set can be mapped one-to-one into any other countably infinite set, thereby giving exactly the same probability for the multiples of 2 and the multiples of 4, for instance.

Whenever we face a challenge of this type, a delicate foundational and conceptual balancing must take place. Obviously one or more of the principles holding for finite lotteries (and thus for probability theory) must be given up. But which principles we give up can only emerge from a subtle dialectic between mathematical coherence and intuitive desiderata. Are there any alternatives to those just explained? Our situation when generalizing from finite to infinite lotteries is similar to the one we have encountered in the main text concerning the generalization from finite to infinite numbers, which led to Cantor’s theory of infinite numbers but also to the theory of numerosities.

The mathematical reader might now object that there is a probabilistic measure used in number theory, *asymptotic density*, that seems to yield what we are looking for. Asymptotic density is defined as follows. Let $A$ be a subset of the natural numbers. The asymptotic density of $A$ is given by the limit as $n$ goes to infinity (if it exists) of $\#(A \cap \{1\ldots n\})/n$ where $\#$ indicates the finite cardinality of the set. According to asymptotic density, the even numbers have probability ½ and so do the odd numbers. Moreover, the multiples of 4 have probability ¼ and this seems to preserve some of our intuitions about the part-whole principle.

But there are serious problems with using this measure as an account of God’s infinite lottery. First of all, every finite subset has probability zero. This is highly unintuitive, for it clashes with our intuitions that the drawing of any one ticket should have *smaller* probability than drawing a ticket from, say, the interval $[0, 10^{10}].$ In fact, some infinite sets (such as the set of primes) are given the same probability of occurring as a single number, namely 0. Moreover, this measure does not satisfy ALL, for not every event is given a probability. For instance, the set of numbers with an odd number of digits does not have an asymptotic density (it includes about 10% of the numbers up to $10^{2n}$ but about 90% of the numbers up to $10^{2n+1})$. It doesn’t even satisfy the weaker condition that the intersection of any two events with a probability has a probability – the set of all $n$ such that ($n$ + the number of digits in $n$) is even has asymptotic density ½, but its intersection with the odd numbers has no asymptotic density. This not only violates ALL but it violates Kolmogorov’s axioms, since the events that receive probability do not form an algebra. Thus, asymptotic density satisfies FAIR but not ALL (see Tenenbaum 1995). A recent generalization of the limit concept (see Schurz and Leitgeb 2008) allows an extension of asymptotic density to satisfy ALL. But we still cannot preserve SUM, for countable additivity fails (only finite additivity holds). And we still have to give up the intuition that every ticket has a non-zero chance of winning.

### Tying the theory of numerosities with God’s lottery

While mathematically compelling, the developments mentioned above require sacrificing some of our most cherished intuitions about finite lotteries. How can we account for God’s lottery preserving the intuition that every ticket has a non-zero chance of winning, while not sacrificing FAIR and not retreating completely from Countable Additivity to Finite Additivity? Wenmackers and Horsten (2013) points the way to using the theory of numerosities to achieve just that. The theory of numerosities was developed as an alternative foundation to non-standard analysis. Importantly, in this theory we are able to preserve the part-whole intuition, and we can use the non-standard model of analysis to which numerosities give rise to assign infinitesimal non-zero probabilities to each ticket in God’s lottery. The specific constructions of the theory of numerosities are essential for some of the details of the probability assignments. One abandons the requirement in Kolmogorov’s axiomatization that the probability function is real-valued. We now assign values from a non-standard model $(R^*)$ of the reals (actually, a non-standard model of the rationals suffices). However, every subset of natural numbers receives a probability value in such a way that FAIR and ALL are satisfied.

In addition, one can prove that a principle of hypercountable additivity holds (although countable additivity does not). This proposal has sparked a rich literature on non-Archimedean probabilities—see Benci, Horsten, and Wenmackers (2013), Wenmackers and Horsten (2013), Benci, Horsten, and Wenmackers (2018), and Wenmackers (2019).
