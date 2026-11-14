# epistemology-bayesian — supplement（supplement）

> （《epistemology-bayesian》词条补充材料，源：plato.stanford.edu/entries/epistemology-bayesian/supplement.html）

#### Supplement to Bayesian Epistemology

## Supplementary Documents

- A. Unsharp Credences and Dutch Books
- B. Comparative Probability and Conditional Credence
- C. The Indifference Principle: The Jeffreys-Jaynes Approach
- D. The Principle of Maximum Entropy
- E. Objective Bayesianism and Impermissive Bayesianism
- F. Shimony’s Qualification of Conditionalization
- G. Jeffrey Conditionalization: A General Formulation
- H. Proof of the Result about the Red Jelly Bean

### A. Unsharp Credences and Dutch Books

Walley (1991: sec. 2.2 and 2.3) develops a betting account of credences that permits one to have a variety of attitudes toward bets or the lack of thereof, which does not force a credence to be as sharp as a real number. On this view, a credence can be unsharp in this way: it can be bounded by one or another interval of real numbers *without* being equal to any particular real number or interval—even the tightest bound on a credence can be an *incomplete* description of that credence. The result is a version of Probabilism permitting that kind of unsharp credences, defended with a Dutch Book argument. The following sketches Walley’s main ideas.

Suppose, for example, that a person is considering a bet that wins $1 if *A* is true, for some specific proposition *A*, and that she takes it acceptable to buy the bet at the price $.8, and acceptable to sell it at the price $.9. In that case, the agent’s credence in proposition *A* is postulated to have a bound $[.8, .9]$. And that credence has that bound even when the agent has different sorts of attitudes toward the prices in between, such as:

1. taking it to be acceptable to buy or sell at some intermediate prices,
2. having made up her mind to *refuse to buy or sell* at some intermediate prices,
3. having *never thought of* some intermediate prices as yet,
4. having thought of some intermediate prices but remaining *undecided*.

Those cases seem to be realistic possibilities that need to be accommodated, and Walley’s account is designed to accommodate them. Now, the agent’s credence in *A* is bounded by interval $[.8, .9]$. This interval-bound is only taken to give an incomplete description of the agent’s credence in *A* because it leaves the four cases (i)–(iv) unspecified. Even when $[.8, .9]$ is the tightest bound of the credence, only case (i) is eliminated and cases (ii)–(iv) remain unspecified, so this interval is still only an *incomplete* description of the credence. That is, even when a credence has $[.8, .9]$ as the tightest bound, it is *not* equal to that bound.

More generally, Walley assumes a certain credence-betting bridge principle, which I take the liberty to simplify as follows for the sake of accessibility:

- *A Credence-Betting Bridge Principle (Bounding Version)*. An agent’s credence in a proposition *A* is bounded by a closed interval $[a, b]$ of real numbers iff it is acceptable for the agent to
- buy the bet “Win $\$x$ if *A* is true” at $\$ax$,
- sell it at $\$bx$.

This setting is also liberal enough to model the case in which one has no credence at all in a proposition: it can be identified with the limiting case in which one’s credence in a proposition is bounded by no closed interval. To see how this bridge principle works, imagine an agent whose credence in proposition $A$ is bounded by $[0.73, 0.80]$ and whose credence in $\neg A$ is bounded by $[0.28, 0.30]$. This agent is susceptible to this Dutch Book:

|   | *A* is true | *A* is false |
| --- | --- | --- |
| buy “win $$100$ if *A* is true” at $\$73$ | $-$73 + $100$ | $-$73$ |
| buy “win $$100$ if $\neg A$ is true” at $\$28$ | $-$28$ | $-$28 + $100$ |
| net payoff | $-$1$ | $-$1$ |

The above example motivates a new version of Probabilism. A function $f$ that maps some propositions to real numbers is said to *satisfy* a bound $[a, b]$ of one’s credence in proposition $A$ if $f(A)$ exists and $a \le f(A) \le b$. Note that there is no probability measure that simultaneously satisfies the two credence bounds in the above example, because even the lower ends of those two bounds, 0.73 and 0.28, are still too large to sum to 1. This observation motivates the following norm:

- *Probabilism (Interval-Satisfiability Version).* An agent’s credences ought be such that their bounds are simultaneously satisfied by a probability measure.

Walley (1991: section 3.3.3) develops a Dutch Book argument for this norm.

The above is only one of the many approaches to unsharp credences. For details and comparisons, see Mahtani (2019) and the entry on imprecise probabilities.

### B. Comparative Probability and Conditional Credence

Comparative probabilities can express nuanced opinions that elude *real-valued* unconditional credences (as mentioned in section 3.3). But Easwaran (2014: sec. 2.4) suggests that comparative probabilities can still be represented *numerically* if there can be conditional credences given a proposition that has a zero credence (such conditional credences are the topic of section 3.4):

1. $A$ is taken to be more probable than $B$ iff, conditional on $A \cup B$, $A$ has a higher credence than $B$ does, i.e., $\Cr(A \mid A \cup B) > \Cr(B \mid A \cup B)$.[^note-10]
2. $A$ is taken to be as probable as $B$ is iff $\Cr(A \mid A \cup B) = \Cr(B \mid A \cup B)$.

Sentences (i) and (ii) can be taken to express a definition of comparative probabilities or, alternatively, a normative constraint. Let’s see how this account works for the Coin Case: Given the disjunction of “the coin is fair” and “the coin is both fair and unfair”, the credence in fairness should be 1 and the credence in the logical contradiction should be 0. So by (i), the fairness of the coin is taken as more probable than the logical contradiction, even though both are assigned unconditional credence 0.

### C. The Indifference Principle: The Jeffreys-Jaynes Approach

The Jeffreys-Jaynes approach to the Indifference Principle yields a consistent answer $1/2$ for the Square Case. Their inspiration comes from a closer look at the Six-Faced Die Case: this case involves a kind of physical symmetry; namely, nothing essential changes when the six faces of the die are transformed into one another by a permutation. So it seems only natural to assign equal credences to those six faces in light of the symmetry. Following that idea, Jeffreys (1946) and Jaynes (1968, 1973) note something to this effect: the Square Case involves a kind of physical symmetry such that nothing essential changes when a *scalar* quantity therein (length or area) is transformed by the choice of a new unit. This kind of symmetry, when properly formalized, gives a consistent answer for the Square Case: credence $1/2$ should be assigned to the proposition that the side length is 1 to 2 cm, and also to the equivalent proposition that the area is 1 to 4 cm².

Let me provide an elementary derivation of the $1/2$ credence. A *scalar* is a quantity that has an absolute zero together with this invariance property: nothing essential changes under the choice of a new unit. Examples include length, area, frequency, and period of time, but perhaps do not include time or potential energy if they lack an absolute zero. A scalar has a second invariance property: nothing essential changes when we take the inverse of the unit, such as transforming period-in-seconds to frequency-in-hertz. For the purposes of the Jeffrey-Jaynes approach, the second invariance property is actually derivable from the first one with the help of calculus, but it is assumed here to facilitate a calculus-free presentation.

Now consider the Square Case. To argue that the length-interval $(1, 2)$ with a unit of one centimeter should be assigned credence $1/2$, it suffices to argue that the length-intervals $(1, 2)$ and $(2, 4)$ should be assigned equal credences (assuming for simplicity that a zero credence should be assigned to the boundary point $2$). To argue for that, first change the unit from 1 centimeter to 2 centimeters. So, dividing everything by 2, the above two length-intervals can be expressed as $(\frac{1}{2}, 1)$ and $(1, 2)$ in the new unit. But those two intervals can be transformed into each other by taking the inverse of the new unit. So they should be assigned equal credences, as promised.

What’s important is how this helps to reply to Bertrand’s paradox. There will be no incompatible results if we apply the same argument to another scalar quantity, area. With a change of unit (namely, dividing everything by $4$), area-intervals $(1, 4)$ and $(4, 16)$ can be transformed to $(\frac{1}{4}, 1)$ and $(1,4)$, which can be transformed into each other by taking the inverse of the new unit.

A thorough presentation that takes care of all possible intervals requires applying calculus to probability density functions and, philosophically, it also requires engaging with the problem of using the so-call *improper* priors: distributions of prior credences that appear to violate the Normalization condition in Probabilism. See Jaynes (1968) for details.

Despite the above reply to Bertrand’s paradox, there is still the worry that this approach fails to solve a version of Bertrand’s paradox due to von Mises (1928 [1981]); see Jaynes (1973: sec. 8) for a reply and see Weisberg (2011: 510–511) for discussion.

### D. The Principle of Maximum Entropy

Core to objective Bayesianism is the focus on this epistemic virtue: freedom from *overly strong/committal opinions* in the absence of sufficient reason or supporting evidence. Following this idea, Jaynes (1968) generalizes the Principle of Indifference to the Principle of Maximum Entropy. Setting aside the technical details about entropy, that principle can be informally stated as follows:

- *The Principle of Maximum Entropy (Informal Version).* Let $S$ be the set of the coherent credence assignments that one has no reason against at the beginning of one’s inquiry. Then one’s prior credence assignment ought to be,
- the least committal one in $S$ (if there exists a unique one),
- or one of the least committal ones in $S$ (if there exist multiple ones),
- or a sufficiently noncommittal one in $S$ (if for every element of $S$ there is always a less committal one in $S$).

The full version of this principle supplements the above with the standard measure of how committal a credence distribution is: (*information*) *entropy*. The rough idea is that, if a credence distribution over some possibilities has more entropy, this distribution will look flatter and, intuitively, it is less committal—expressing a weaker opinion. This intuitive understanding of the concept of entropy is enough for the discussion below. But details are available in the survey by Joyce (2011: sec. 2.1).

Clauses (ii) and (iii) suggest that the Principle of Maximum Entropy is *not* committed to impermissivist Bayesianism, the view that there always exists a uniquely permissible prior. Clause (ii) is needed because multiple credence distributions can share the same entropy. Clause (iii) is needed for those who think that coherence requires Countable Additivity. To see why, consider a countable set $\Omega$ of mutually exclusive and jointly exhaustive possibilities. The least committal (i.e., flattest) distribution of credences over $\Omega$ assigns 0 to each of those possibilities just like de Finetti’s Infinite Lottery (section 3.2), so it violates Countable Additivity. Furthermore, of the probability distributions over $\Omega$ that satisfy Countable Additivity, there is no such thing as the least committal (flattest) one. The reason is roughly that, for any sequence of non-negative real numbers that sum to one (such as a sequence that decays exponentially with a certain rate), there always exists an alternative that is *flatter* (such as a sequence that decays exponentially with a *slower* rate). Therefore, if coherence requires Countable Additivity, no coherent credence distribution over $\Omega$ is least committal (flattest), and hence clause (iii) is needed, as J. Williamson (2010) emphasizes.

There is a worry about the Maximum Entropy Principle: when this principle is applied repeatedly across different times, it might violate the Principle of Conditionalization. The following is a putative counterexample due to Seidenfeld (1979). Suppose that the set of the possibilities under consideration is $\Omega = \{1, 2, 3, 4, 5, 6\}$, and that the initial set of the coherent priors to choose from, $S_\textrm{old}$, is defined by

$S_\textrm{old}$ = the set of the probability distributions $\Cr$ over $\Omega$ such that

$$\sum_{x = 1}^{6} x\,\Cr\big(\{x\}\big) = 3.5.$$

The least committal (flattest) distribution in $S_\textrm{old}$ turns out to be the distribution $\Cr_\textrm{old}$ that assigns equal credences $1/6$ to each of the six possibilities in $\Omega$. So, by the Maximum Entropy Principle, $\Cr_\textrm{old}$ is the uniquely permissible prior. Now, suppose that we receive new evidence $E = \{2, 4, 6\}$, the set of the even-numbered possibilities. The result of conditionalizing the prior $\Cr_\textrm{old}$ on $E$ is the credence distribution $\Cr_\textrm{new}$ that assigns equal credences $1/3$ to the even-numbered possibilities and credences 0 to the other possibilities. But Seidenfeld (1979) argues that, after $E$ is received as new evidence, the updated set of the coherent priors to choose from, $S_\textrm{new}$, should be the initial set $S_\textrm{old}$ “restricted” by $E$ in the following sense:

$$S_\textrm{new} = S_\textrm{old} \cap \{\Cr: \Cr(E) = 1\}.$$

Now, if we apply the Principle of Maximum Entropy to $S_\textrm{new}$, the chosen posterior cannot be the one $\Cr_\textrm{new}$ obtained by conditionalization on $E$. The reason is that $\Cr_\textrm{new}$ cannot be the least committal (flattest) one in $S_\textrm{new}$, for it is already not in $S_\textrm{old}$. (Indeed, $\sum_{x = 1}^{6} x\, \Cr_\textrm{new}\big(\{x\}\big) = 4 \neq 3.5$.) For a reply in favor of objective Bayesianism, see J. Williamson (2010: ch. 4), who also presents other influential challenges to the Maximum Entropy Principle, together with his replies to them.

### E. Objective Bayesianism and Impermissive Bayesianism

Objective Bayesianism and impermissive Bayesianism, as characterized in this entry, are two independent views—neither implies the other. An impermissivist need not accept objective Bayesianism, because she can refrain from endorsing any particular norm to single out the uniquely permissible doxastic state, let alone endorsing the Indifference Principle. An objective Bayesian need not accept impermissivism, either. To see why, note that core to objective Bayesianism is the Indifference Principle, whose normative consequences depend crucially on an account of its inputs, i.e., what counts as insufficient reason or evidential symmetry (recall the discussion of “garbage in, garbage out”). So the Indifference Principle may be rendered too weak to single out a unique prior. For example, Carnap’s (1963) version of the Indifference Principle permits a continuum of different priors, corresponding to stronger or weaker tendencies to infer inductively. Even when the Indifference Principle is generalized to the Principle of Maximum Entropy, it is still not committed to impermissivism; see supplement D for an explanation.

That said, objective Bayesians tend to be sympathetic to impermissivism. Perhaps this is because some motivations of the Indifference Principle lead naturally (although not necessarily) to impermissivism. For an example of such a motivation, think of the Humean thesis that one’s beliefs ought to be proportioned to one’s evidence (Hume 1748/1777: sec. 10, part 1). Now, let that plausible-sounding Humean thesis be developed as follows:

- *A Humean Thesis Reformulated.* One’s credence in a proposition ought to be equal to *the* degree to which that proposition is supported by one’s total evidence.

This thesis motivates a version of the Indifference Principle (that equally supported hypotheses ought to be assigned equal credences). But the same thesis also implies impermissivism if we take seriously the italicized ‘the’ therein, which presupposes that there exists a uniquely correct relation of evidential support. So Schoenfield (2014) argues that, if there is more than one correct relation of evidential support, the above line of motivation will lead to permissivism instead.

### F. Shimony’s Qualification of Conditionalization

Another way to qualify the Principle of Conditionalization is suggested by Shimony (1970):

- *The Principle of Conditionalization (Matching Version).* It ought to be that, upon learning $E$, one’s new credence in $H$ be made to match one’s prior conditional credence in $H$ given $E$, if the latter exists.

Note how this is immune from the Physics Student Case: the student did not think of the logical claim $E_\textrm{logical}$ before, let alone had a conditional credence given that claim—so the if-clause is not satisfied. In that case, there is simply nothing for the new credence to match.

### G. Jeffrey Conditionalization: A General Formulation

In the main text Jeffrey conditionalization is stated with respect to an evidential proposition $E$, but it is often stated more generally with respect to a finite partition $\{E_i : i = 1, \ldots, n\}$ of propositions (which are by definition mutually exclusive and jointly exhaustive):

- *The Principle of Jeffrey Conditionalization.* It ought to be that, whenever the immediate effect of the experience that one just received is a change of the credences in the elements of a finite partition $\{E_i : i = 1, \ldots, n\}$ and those credences were all nonzero right before the change, then one’s credence change from $\Cr$ to $\Cr_\textrm{new}$ meet any one of the following equivalent conditions: (1) for each partition element $E_i$ whose new credence is (still) nonzero, the credence ratios of the propositions that each entail $E_i$ are preserved from $\Cr$ to $\Cr_\textrm{new}$, or equivalently, (2) for each partition element $E_i$ whose new credence is (still) nonzero, the conditional credences given $E_i$ are preserved from $\Cr$ to $\Cr_\textrm{new}$, or equivalently, $$ \begin{align} \Cr(X) &= \sum_{i = 1}^{n} \underbrace{\Cr(X \mid E_i)}_\textrm{held constant} \wcdot \Cr(E_i)\\ &\downarrow\\ \underbrace{\Cr_\textrm{new}(X)}_{\substack{\textrm{new weighted}\\ \textrm{average}}} &= \sum_{i = 1}^{n} \underbrace{\Cr(X \mid E_i)}_\textrm{held constant} \cdot \underbrace{\Cr_\textrm{new}(E_i)}_\textrm{new weight} \end{align}\tag{3} $$

The equivalence among the three formulations (1)–(3) assumes Probabilism and the Ratio Formula. In formulation (3), the prior credence $\Cr(X)$ is expressed as a weighted average of some conditional credences, and the credence change is expressed as a change *only* in the weights, holding the conditional credences constant.

### H. Proof of the Result about the Red Jelly Bean

To prove Weisberg’s (2009b) result about the Red Jelly Bean Case, that it cannot be accommodated by Jeffrey conditionalization, we need a bit of elementary probability theory:

- *Proposition (Symmetry of Independence)* Suppose that $\Cr$ is probabilistic, that $\Cr(A)$ and $\Cr(B)$ lie strictly between 0 and 1, and that the Ratio Formula holds. Then the following conditions are equivalent: $$\begin{align} \Cr(A \mid B) & = \Cr(A)\tag{1}\\ \Cr(B \mid A) & = \Cr(B \mid \neg A)\tag{2}\\ \Cr(A \mid B) & = \Cr(A \mid \neg B)\tag{3}\\ \end{align} $$

Any of those three clauses can be used to define the independence between propositions $A$ and $B$ with respect to credence assignment $\Cr$. Now, assume the following two conditions from the Red Jelly Bean Case:

$$ \begin{align} \Cr_\textrm{new}( \textsf{red} \mid \textsf{tricky} ) & < \Cr_\textrm{new}( \textsf{red} )\tag{a}\\ \Cr_\textrm{old}( \textsf{red} \mid \textsf{tricky} ) & = \Cr_\textrm{old}( \textsf{red} )\tag{b}\\ \end{align} $$

Suppose, for *reductio*, that $\Cr_\textrm{old}$ is obtained from $\Cr_\textrm{old}$ by a Jeffrey conditionalization on $\textsf{red}$. Then (b) implies the following, by (1) $\Rightarrow$ (2):

$$ \Cr_\textrm{old}( \textsf{tricky} \mid \textsf{red} ) = \Cr_\textrm{old}( \textsf{tricky} \mid \neg\textsf{red} ) . $$

That implies the following, thanks to the conditional credences preserved by Jeffrey conditionalization on $\textsf{red}$:

$$ \Cr_\textrm{new}( \textsf{tricky} \mid \textsf{red} ) = \Cr_\textrm{new}( \textsf{tricky} \mid \neg\textsf{red} ). $$

That implies the following, by (2) $\Rightarrow$ (3):

$$ \Cr_\textrm{new}( \textsf{red} \mid \textsf{tricky} ) = \Cr_\textrm{new}( \textsf{red} \mid \neg\textsf{tricky} ). $$

That implies the following, by (3) $\Rightarrow$ (1):

$$ \Cr_\textrm{new}( \textsf{red} \mid \textsf{tricky} ) = \Cr_\textrm{new}( \textsf{red}). $$

But this result contradicts (a), as desired.


## Notes（原文脚注，引自主文）

[^note-10]: 10. Although this idea is attributed by Easwaran (2014: sec. 2.4) to Hájek (2003), it can only be found in the former paper but not in the latter.