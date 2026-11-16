# preferences — revealed-preference（supplement）

> （《preferences》词条补充材料，源：plato.stanford.edu/entries/preferences/revealed-preference.html）

#### Supplement to Preferences

## The Strong Axiom of Revealed Preference

The fifth and strongest of the properties of a choice function is the so-called *strong axiom of revealed preferences* (SARP). In essence, SARP is a recursive closure of WARP:

If

$$\begin{align} X_1,X_2, \ldots ,X_n &\in \mathcal{A}_1, \\ X_2, \ldots, X_n &\in \mathcal{A}_2, \\ &\vdots \\ X_{n-1},X_{n} &\in \mathcal{A}_{n-1}, \\ X_{n} &\in \mathcal{A}_{n}, \\ X_1\in \mathbf{C}(\mathcal{A}_1), X_2\in \mathbf{C}(\mathcal{A}_2), &\ldots ,X_n\in \mathbf{C}(\mathcal{A}_n), \end{align}$$

then,

$$\begin{align} \text{for all } \mathcal{B} \text{ with } X_1,X_2 ,\ldots ,X_n &\in \mathcal{B}, \text{ if } X_i\in \mathbf{C}(\mathcal{B}), i\in \{1,\ldots ,n\}, \\ \text{ then } X_1,X_2 ,\ldots ,X_{i-1}&\in \mathbf{C}(\mathcal{B}) \quad\text{(SARP)} \end{align}$$

Simplified, SARP says that if from a set of alternatives $\mathcal{A}_1, X$ is chosen when $Y$ and $Z$ are available, and if in some other set of alternatives $\mathcal{A}_2, Y$ is chosen while $Z$ is available, then there can be no set of alternatives containing alternatives $X$ and $Z$ for which $Z$ is chosen and $X$ is not. (SARP says this for chains of unlimited length). SARP is much stronger than $\alpha , \beta$ and *γ* combined. However, for choice functions that specify choices over all subsets of the alternative set with at most three elements, SARP is equivalent to WARP and hence to properties *α* and *β* (Sen 1971, 50).

### Second Construction Method

A second construction method defines an alternative $X$ as “at least as good as” an alternative $Y$ if and only if $X$ is chosen from the binary set that contains $Y$.

$$\begin{align} \tag{2} X\succcurlyeq^B Y &\text{ iff } X\in \mathbf{C}(\{X,Y\}) \\ X\succ^B Y &\text{ iff } X\succcurlyeq^B Y \text{ and not } Y\succcurlyeq^B X \\ X\sim^B Y &\text{ iff } X\succcurlyeq^B Y \text{ and } Y\succcurlyeq^B X \end{align}$$

If the choice function is defined over all binary subsets of a set of alternatives, $\succcurlyeq^B$ is complete. However, $\succcurlyeq^B$ does not necessarily satisfy transitivity of strict preference, transitivity of indifference, IP- or PI-transitivity.

A third method defines an alternative $X$ as “strictly preferred to” an alternative $Y$ if and only if $X$ is chosen from some set of alternatives that also contains $Y$, but $Y$ is not chosen from that set.

$$\begin{align} \tag{3} X\succ^R Y &\text{ iff for some } \mathcal{B}, X\in \mathbf{C}(\mathcal{B}) \text{ and } Y\in[\mathcal{B}\backslash \mathbf{C}(\mathcal{B})] \\ X\succcurlyeq^R Y &\text{ iff not } X\succ^R Y \\ X\sim^R Y &\text{ iff } X\succcurlyeq^R Y \text{ and } Y\succcurlyeq^R X \end{align}$$

If the choice function is defined over all relevant subsets of the set of alternatives, $\succcurlyeq^R$ is always complete. However, $\succ^R$ may violate transitivity of strict preference, and $\succcurlyeq^R$ may violate transitivity of indifference, IP- or PI-transitivity.

In constructing $\succcurlyeq^B$, if $\mathbf{C}(\{X,Y\})=\{X,Y\}$, then indifference holds, i.e. $X\sim^B Y$. However, this is not the only possible interpretation. One can interpret $\mathbf{C}(\{X,Y\})=\{X,Y\}$ either as an indifference between $X$ and $Y$ or as *incomparability* between these two alternatives. Extra information is required to distinguish the two. One possibility of obtaining such extra information is the *small improvement argument* (Chang 1997, 23-26). When observing an agent choosing $\mathbf{C}(\{X,Y\}) = \{X,Y\}$, the observer makes the agent repeat the choice, now with an offer of a small independent incentive $i$ attached to one of the alternatives. If the agent chooses $\mathbf{C}(\{X\wedge i,Y\}) = \{X\wedge i\}$, the observer may conclude that the agent was indifferent between $X$ and $Y$, and that the addition of $i$ to $X$ shifted the balance to $X \wedge i$ over $Y$. If the agent however chooses $\mathbf{C}(\{X\wedge i,Y\}) = \{X\wedge i,Y\}$, then the observer may conclude that $X$ and $Y$ were incomparable for the agent, and that the addition of $i$ to $X$ did not alter $X$’s incomparability to $Y$. Because the agent’s evaluation of $i$ is presupposed, this method is not uncontroversial.

The elicitation of preferences through choices is of particular importance in economics, where prices and choices of large groups of agents are often the only available empirical data. The *revealed preference method* proceeds in two steps. In the first step, an agent’s observed choice of a goods bundle $X_i = \langle x_1 ,\ldots ,x_n\rangle$ in combination with the prices $P_i = \langle p_1 ,\ldots ,p_n\rangle$ for these goods determine the set of alternatives from which the agent chooses. If the agent chooses $X_i = \langle x_{i_1},\ldots ,x_{i_n}\rangle$ under prices $P_i = \langle p_{i_1},\ldots ,p_{i_n}\rangle$, her budget is

$$ B = X_{i} \times P_i = \langle x_{i_1},\ldots ,x_{i_n}\rangle \times \langle p_{i_1},\ldots ,p_{i_n}\rangle,$$

assuming that she spends all her resources. Under price regime $P_i$, she can thus choose between all goods bundles $X_j$ that are affordable under the budget $B$, i.e. for which $B \ge X_j \times P_{i}$. In the second step, preference construction method (1) is applied. If the agent is observed choosing bundle $X_i$ from budget $B$, then $X_i$ is declared weakly preferred to all $X_j$ affordable under $B$. The revealed preference connection, in accord with method (1), is then formulated as:

$$\begin{align} X_{i}\succcurlyeq^C X_{j} &\text{ iff } X_i \times P_i \ge X_j \times P_i \\ X\succ^C Y &\text{ iff } X\succcurlyeq^C Y \text{ and not } Y\succcurlyeq^C X \\ X\sim^C Y &\text{ iff } X\succcurlyeq^C Y \text{ and } Y\succcurlyeq^C X \end{align}$$

It may be the case that an agent chooses $X_i$ under prices $P_i$ and $X_j$ under prices $P_j$, even though $X_i \times P_i \ge X_j \times P_i$ and $X_j \times P_j \ge X_i \times P_j.$ The revealed preference method then elicits $X_i \succ^C X_j$ and $X_j\succ^C X_i$, which violates asymmetry of strict preference. To avoid this undesirable conclusion, only those choices are considered that satisfy the *Weak Axiom of Revealed Preferences* (WARP). It says that if $X$ is chosen when $Y$ is available, then there can be no budget set containing both alternatives for which $Y$ is chosen and $X$ is not (see section 5.1). Thus, asymmetry of $\succ^C$ is secured.

As discussed in section 5.1, for situations that specify choices over all subsets (up to three elements) of the alternative set, WARP also ensures that the relation $\succcurlyeq^C$ is transitive. For practical purposes, however, this method is not very helpful, as the space of prices and goods bundles is very large. Social scientists do not have the resources to observe agents’ choices from *all* relevant preference sets. If they want to derive a transitive preference relation from a choice function not defined over all subsets (up to three elements), then they have to restrict themselves to consider only choices that satisfy the *strong axiom of revealed preferences* (SARP). It says that if $X$ is chosen when $Y$ is available, and if in some other budget set $Y$ is chosen when $Z$ is available, then there can be no budget set containing alternatives $X$ and $Z$ for which $Z$ is chosen and $X$ is not. Thus, transitivity of $\succcurlyeq^C$ is ensured.
