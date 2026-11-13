# Preferences
**First published Wed Oct 4, 2006; substantive revision Mon Mar 14, 2022**

*Hansson, Sven Ove, Grüne-Yanoff, Till*

The notion of preference has a central role in many disciplines, including moral philosophy and decision theory. Preferences and their logical properties also have a central role in rational choice theory, a subject that in its turn permeates modern economics, as well as other branches of formalized social science. The notion of preference and the way it is analysed vary between these disciplines. A treatment is still lacking that takes into account the needs of all usages and tries to combine them in a unified approach. This entry surveys the most important philosophical uses of the preference concept and investigates their compatibilities and conflicts.

## 1. The Basic Concept of Preference

In common parlance, the term “preference” assumes different meanings, including that of comparative evaluation, prioritisation or favouring, and choice ranking (See for instance the *Oxford English Dictionary*). In this entry, we discuss the notion of preference as *subjective comparative evaluations*, of the form “Agent $A$ prefers $X$ to $Y$”. This characterisation distinguishes preference from other evaluative concepts.

Preferences are *evaluations*: they concern matters of value, typically in relation to practical reasoning, i.e. questions about what should be done, or should have been done. This distinguishes preferences from concepts that concern matters of fact.

Furthermore, preferences are *subjective* in that the evaluation is typically attributed to an agent – where this agent might be either an individual or a collective. This distinguishes them from statements to the effect that “$X$ is better than $Y$” in an objective or otherwise impersonal sense. The logic of preference has often also been used to represent such objective evaluations (e.g. Broome 1991b), but the substantial notion of preference includes this subjective element.

Finally, preferences are *comparative* in that they express the evaluation of an item $X$ *relative to* another item $Y$. This distinguishes them from monadic concepts like “good”, “is desired”, etc. which only evaluate one item.

Most philosophers take the evaluated items to be propositions. In contrast to this, economists commonly conceive of items as bundles of goods, represented as vectors.[^note-1] However, this approach has a difficult ambiguity. If preferences are subjective evaluations of the alternatives, then what matters are the results that can be obtained with the help of these goods, not the goods themselves. Whether an agent has a preference e.g. for a batch of wood over a crate of bricks will depend on whether she intends to use it to generate warmth, build a shelter or create a sculpture. Economists have tried to solve this ambiguity by coupling preferences over goods with household production functions (Lancaster 1966, Becker and Michael 1973)[^becker-1973][^lancaster-1966]; but as these functions are very difficult to determine, it is often thought more parsimonious to stick with the sentential or propositional representations of states of the world.

Serious engagement with preferences began in the 20th century. In the social sciences, the preference concept became important for explanatory and predictive purposes with Irving Fisher’s (1892) and Vilfredo Pareto’s (1909) methodological criticisms of hedonistic cardinal utility. Previously, economists largely agreed that decisions were motivated by the individual’s quest for pleasure, and that the difference in quantity of pleasure derived from different alternatives was an important influence on decisions. In that framework, the notion of preference, to the extent that it was used at all, was merely derived from hedonistic utility: $X$ is preferred to $Y$ iff $X$ yields more utility than $Y$. Pareto argued that because an accurate measurement procedure for cardinal hedonic utility was not available, social scientists should constrain themselves to merely ordinal comparisons (Bruni and Guala 2001). This argument turned preference into a fundamental notion of the social sciences, replacing (hedonic) utility.

Economists in the 1930s (Hicks and Allen 1934) radicalised Pareto’s idea and argued that cardinal utility should be excluded in order to expunge economics from psychological hedonism. However, their concept of preference retained psychological content: people are assumed to act purposefully and therefore to have preferences that really constitute mental evaluations, rather than being ex-post rationalisations of behaviour (Lewin 1996). Furthermore, Ramsey (1926) and later von Neumann and Morgenstern (1944) devised formal tools allowing the representation of preference magnitudes as utility functions on an interval scale. This new utility, however, was very different from the older hedonic concept: the preference concept was basic. The cardinal utility function was constructed to reflect the preference ordering, but was not completely determined by it.

Psychologists also sought to move away from the old psychophysical assumptions and began seeing mental concepts like preferences with increased suspicion. Instead, they sought not only to connect and measure psychological events, but indeed replace them by the behavioural criteria with which they were hitherto connected. (See the entry on behaviorism). Again, it was an economist, Paul Samuelson, who formulated this principle most explicitly for the concept of preference. In 1938 he suggested to “start anew … dropping off the last vestiges of the utility analysis” (1938, p. 62). Preferences were supposed to be defined in terms of choice, thus eliminating reference to mental states altogether. Although this approach was highly influential at the time, economists have largely not followed Samuelson in this radical proposal (Hausman 2012)[^hausman-2012], and it might indeed be the case that Samuelson himself later changed his mind (Hands 2014). With the increasing convergence of (parts of) economics and psychology, the ordinal psychological interpretation of preferences appears to currently dominate in these disciplines. However, there is an ongoing discussion amongst philosophers whether the current concept of preference used by economists is this mental, “folk-theoretic” notion or a separate theoretical concept (Mäki 2000, Ross 2014, Thoma 2021)[^mäki-2000][^ross-2014][^thoma-2021].

In philosophy, the concept of preference gained increased attention in the wake of the conceptual developments in the social sciences. Because the hedonic utility notion was increasingly questioned, utilitarian philosophers sought alternative foundations for their ethical theories. Today, *preferentialism* defends satisfaction of individual preferences as the only intrinsic value bearer, and thus is a subcategory of the broad welfarist family of value theories, which identify intrinsic value with well-being. Few people defend the view that well-being is constituted by the satisfaction of *any* preference, but a number of authors defend refined versions of preferentialism (e.g. Rawls 1971, Scanlon 1998)[^rawls-1971]. Philosophers have also discussed the formal properties of preferences in *preference logic*. To this we turn in the next section.

## 2. Preference logic

Although not all philosophical references to preference make use of formal tools, preferences are almost always assumed to have structural properties of a type that is best described in a formalized language. The study of the structural properties of preferences can be traced back to Book III of Aristotle’s *Topics*. Since the early twentieth century several philosophers have studied the structure of preferences with logical tools. In 1957 and in 1963, respectively, Sören Halldén and Georg Henrik von Wright proposed the first complete systems of preference logic (Halldén 1957, von Wright 1963)[^halldén-1957][^wright-1963]. The subject also has important roots in utility theory and in the theory of games and decisions. The preferences studied in preference logic are usually the preferences of rational individuals, but preference logic is also used in psychology and behavioural economics, where the emphasis is on actual preferences as revealed in behaviour.

### 2.1 Concepts and notation

There are two fundamental comparative value concepts, namely “better” (strict preference) and “equal in value to” (indifference) (Halldén 1957, 10)[^halldén-1957]. These terms are used to express the wishes of persons, but they are also used for other purposes, for instance to express objective or intersubjectively valid betterness that does not coincide with the pattern of wishes of any individual person. However, the structural (logical) properties of betterness and value equality do not seem to differ between the cases when they correspond to what we usually call “preferences” and the cases when they do not. The term “preference logic” is standardly used to cover the logic of these concepts even in cases when we would typically not use the term “preference” in a non-formalized context.

The relations of preference and indifference between alternatives are usually denoted by the symbols $\succ$ and $\sim$ or alternatively by $P$ and $I$. In accordance with a long-standing philosophical tradition, $A\succ B$ is taken to represent “$B$ is worse than $A$”, as well as “$A$ is better than $B$”.

The objects of preference are represented by the relata of the preference relation $(A$ and $B$ in $A\succ B)$. In order to make the formal structure determinate enough, every preference relation is assumed to range over a specified set of relata. In most applications, the relata are assumed to be mutually exclusive, i.e. none of them is compatible with, or included in, any of the others. Preferences over a set of mutually exclusive relata are referred to as *exclusionary* preferences. When the relata are mutually exclusive, it is customary to call the set of relata an *alternative set*, or set of alternatives, $\mathcal{A}$.

The following four properties of the two exclusionary comparative relations are usually taken to be part of the meaning of the concepts of (strict) preference and indifference:

$$\begin{align} \tag{1} A\succ B \rightarrow \neg(B\succ A) &\quad\text{(asymmetry of preference)}\\ \tag{2} A\sim B \rightarrow B\sim A &\quad\text{(symmetry of indifference)}\\ \tag{3} A\sim A &\quad\text{(reflexivity of indifference)}\\ \tag{4} A\succ B \rightarrow \neg(A\sim B) &\quad\text{(incompatibility of preference} \\ &\quad\text{ and indifference)} \end{align}$$

It follows from (1) that strict preference is irreflexive, i.e. that $\neg(A\succ A)$.

The relation $\succcurlyeq$, “at least as good as” (or more precisely: “better than or equal in value to”), can be defined as follows:

$$ A\succcurlyeq B \leftrightarrow A\succ B \vee A\sim B \quad\text{(weak preference)} $$

The alternative notation $R$ is sometimes used instead of $\succcurlyeq$.

For reasons of convenience, weak preference is usually taken to be the primitive relation of preference logic. Then both (strict) preference and indifference are introduced as derived relations, as follows:

$$\begin{align} A\succ B &\text{ if and only if } A\succcurlyeq B \text{ and } \neg(B\succcurlyeq A) \\ A\sim B &\text{ if and only if } A\succcurlyeq B \text{ and } B\succcurlyeq A \end{align}$$

$\succ$ is the *strict part* of $\succcurlyeq$ and $\sim$ its *symmetric part*.

Two common notational conventions should be mentioned. First, chains of relations can be contracted. Hence, $A\succcurlyeq B\succcurlyeq C$ abbreviates $A\succcurlyeq B \wedge B\succcurlyeq C$, and $A\succ B\succ C\sim D$ abbreviates $A\succ B \wedge B\succ C \wedge C\sim D$. Second, the ancestral symbol * is used to contract repeated uses of the same relation; hence $\succ$* stands for $\succ$ repeated any finite non-zero number of times (and similarly for the other relations). Thus $A\succ *C$ denotes that either $A\succ C$ or there are $B_1 \ldots B_n$ such that

$$ A\succ B_1 \wedge B_1 \succ B_2 \wedge \ldots B_{n-1}\succ B_n \wedge B_n\succ C. $$

### 2.2 Completeness

In most applications of preference logic, it is taken for granted that the following property, called *completeness* or *connectedness*, should be satisfied:

$$ A\succcurlyeq B \vee B\succcurlyeq A $$

or equivalently:

$$ A\succ B \vee A\sim B \vee B\succ A $$

The following weaker version of the property is sometimes useful:

$$ \text{If } A\ne B, \text{ then } A\succcurlyeq B \vee B\succcurlyeq A \quad\text{(weak connectivity)} $$

(*Completeness* holds if and only if both *weak connectivity* and *reflexivity of indifference* hold.)

Completeness (connectedness) is commonly assumed in many applications, not least in economics. Bayesian decision theory is a case in point. The Bayesian decision maker is assumed to make her choices in accordance with a complete preference ordering over the available options. However, in many everyday cases, we do not have, and do not need, complete preferences. Consider a person who has to choose between five available objects $A, B, C, D$, and $E$. If she knows that she prefers $A$ to the others, then she does not have to make up her mind about the relative ranking among $B, C, D$, and $E$.

In terms of resolvability, there are three major types of preference incompleteness. First, incompleteness may be *uniquely resolvable*, i.e. resolvable in exactly one way. The most natural reason for this type of incompleteness is lack of knowledge or reflection. Behind what we perceive as an incomplete preference relation there may be a complete preference relation that we can arrive at through observation, introspection, logical inference, or some other means of discovery.

Secondly, incompleteness may be *multiply resolvable*, i.e. possible to resolve in several different ways. In this case it is genuinely undetermined what will be the outcome of extending the relation to cover the previously uncovered cases.

Thirdly, incompleteness may be *irresolvable*. The most natural reason for this is that the alternatives differ in terms of advantages or disadvantages that we are unable to put on the same footing. A person may be unable to say which she prefers—the death of two specified acquaintances or the death of a specified friend. She may also be unable to say whether she prefers the destruction of the pyramids in Giza or the extinction of the giant panda. In environmental economics, as a third example, it is a controversial issue whether and to what extent environmental damage is comparable to monetary loss.

Two alternatives are called “incommensurable” whenever it is impossible to measure them with the same unit of measurement. Cases of irresolvable incompleteness are often also cases of incommensurability (Chang 1997)[^chang-1997]. In moral philosophy, irresolvable incompleteness is usually discussed in terms of the related notion of a moral dilemma.

### 2.3 Transitivity

By far the most discussed logical property of preferences is the following:

$$ A\succcurlyeq B \wedge B\succcurlyeq C \rightarrow A\succcurlyeq C \quad\text{(transitivity of weak preference)} $$

The corresponding properties of the other two relations are defined analogously:

$$ A\sim B \wedge B\sim C \rightarrow A\sim C \quad\text{(transitivity of indifference)} $$ $$ A\succ B \wedge B\succ C \rightarrow A\succ C \quad\text{(transitivity of strict preference)} $$

A weak preference relation $\succcurlyeq$ is called *quasi-transitive* if its strict part $\succ$ is transitive.

Many other properties have been defined that are related to transitivity. The following three are among the most important of these:

- $A\sim B \wedge B\succ C \rightarrow A\succ C \quad\text{(IP-transitivity)}$
- $A\succ B \wedge B\sim C \rightarrow A\succ C \quad\text{(PI-transitivity)}$
- There is no series $A_1 ,\ldots ,A_n$ of alternatives such that $A_1 \succ \ldots \succ A_n\succ A_1$ $\text{(acyclicity)}$

All of these are ways of weakening the transitivity of $\succcurlyeq$. Thus, if $\succcurlyeq$ satisfies transitivity then $\succ$ and $\sim$ are also transitive, and furthermore, IP-transitivity, PI-transitivity and acyclicity hold.

Furthermore, if $\succcurlyeq$ is transitive, then no cycles containing $\succ$ are possible, i.e. there are no $A$ and $B$ such that $A\succcurlyeq *B\succ A$. Preferences with such a $\succ$-containing cycle are called *cyclic preferences*.

Transitivity is a controversial property, and many examples have been offered to show that it does not hold in general. A classic type of counterexample to transitivity is the so-called Sorites Paradox. It employs a series of objects that are so arranged that we cannot distinguish between two adjacent members of the series, whereas we can distinguish between members at greater distance (Armstrong 1939, Armstrong 1948, Luce 1956)[^armstrong-1939][^armstrong-1948][^luce-1956]. Consider 1000 cups of coffee, numbered $C_0, C_1, C_2,\ldots$ up to $C_{999}$. Cup $C_0$ contains no sugar, cup $C_1$ one grain of sugar, cup $C_2$ two grains etc. Since one cannot taste the difference between $C_{999}$ and $C_{998}$, one might consider them to be equally good (of equal value), $C_{999}\sim C_{998}$. For the same reason, we have $C_{998}\sim C_{997}$, etc. all the way to $C_1\sim C_0$, but clearly $C_0 \succ C_{999}$. This contradicts transitivity of indifference, and therefore also transitivity of weak preference.

In a related example proposed by Warren S. Quinn, a device has been implanted into the body of a person (the self-torturer). The device has 1001 settings, from 0 (off) to 1000. Each increase leads to a negligible increase in pain. Each week, the self-torturer “has only two options—to stay put or to advance the dial one setting. But he may advance only one step each week, and he may *never* retreat. *At each advance he gets $10,000.*” In this way he may “eventually reach settings that will be so painful that he would then gladly relinquish his fortune and return to 0” (Quinn 1990, 79)[^quinn-1990].

In an important type of counterexamples to transitivity of strict preference, different properties of the alternatives dominate in different pairwise comparisons. Consider an agent choosing between three boxes of Christmas ornaments (Schumm 1987)[^schumm-1987]. Each box contains three balls, coloured green, red and blue, respectively; they are represented by the vectors $\langle R_1,G_1,B_1\rangle,$ $\langle R_2,G_2,B_2\rangle$, and $\langle R_3,G_3,B_3\rangle$. The agent strictly prefers box 1 to box 2, since they contain (to her) equally attractive blue and green balls, but the red ball of box 1 is more attractive than that of box 2. She prefers box 2 to box 3, since they are equal but for the green ball of box 2, which is more attractive than that of box 3. And finally, she prefers box 3 to box 1, since they are equal but for the blue ball of box 3, which is more attractive than that of box 1. Thus,

$$R_1\succ R_2\sim R_3\sim R_1,$$ $$G_1\sim G_2\succ G_3\sim G_1,$$ $$B_1\sim B_2\sim B_3\succ B_1;$$

and from this follows

$$ \langle R_1,G_1,B_1\rangle \succ \langle R_2,G_2,B_2\rangle \succ \langle R_3,G_3,B_3\rangle \succ \langle R_1,G_1,B_1\rangle. $$

The described situation yields a preference cycle, which contradicts transitivity of strict preference. (Notice the structural similarity to Condorcet’s Paradox, see the entry on voting methods.)

These and similar examples can be used to show that actual human beings may have cyclic preferences. It does not necessarily follow, however, that the same applies to the idealized *rational* agents of preference logic. Perhaps such patterns are due to irrationality or to factors, such as lack of knowledge or discrimination, that prevent actual humans from being rational. There is a strong tradition, not least in economic applications, to regard full $\succcurlyeq$-transitivity as a necessary prerequisite of rationality.

The most famous argument in favour of preference transitivity is the money pump argument. The basic idea was developed by F.P. Ramsey (1928a, 182), who pointed out that if a subject’s behaviour violated certain axioms of probability and preference, then he would be willing to buy a bet that yields a gain to the seller, and a loss to the buyer, no matter what happens. The argument was developed in more detail in Davidson et al. (1955).

The following example can be used to show how the argument works in a non-probabilistic context: A certain stamp-collector has cyclic preferences with respect to three stamps, denoted $A, B$, and $C$. She prefers $A$ to $B, B$ to $C$, and $C$ to $A$. Following Ramsey, we may assume that there is an amount of money, say 10 cents, that she is prepared to pay for exchanging $B$ for $A, C$ for $B$, or $A$ for $C$. She comes into a stamp shop with stamp $A$. The stamp-dealer offers her to trade in $A$ for $C$, if she pays 10 cents. She accepts the deal.

For a precise notation, let $\langle X,V\rangle$ denote that the collector owns stamp $X$ and has paid $V$ cents to the dealer. She has now moved from the state $\langle A,0\rangle$ to the state $\langle C,10\rangle$.

Next, the stamp-dealer takes out stamp $B$ from a drawer, and offers her to swap $C$ for $B$, against another payment of 10 cents. She accepts, thus moving from the state $\langle C,10\rangle$ to $\langle B,20\rangle$. The shop-owner can go on like this forever. What causes the trouble is the following sequence of preferences:

$$\begin{align} \langle C,10\rangle &\succ \langle A,0\rangle \\ \langle B,20\rangle &\succ \langle C,10\rangle \\ \langle A,30\rangle &\succ \langle B,20\rangle \\ \langle C,40\rangle &\succ \langle A,30\rangle \\ \langle B,50\rangle &\succ \langle C,40\rangle \\ \langle A,60\rangle &\succ \langle B,50\rangle \\ &\vdots \end{align}$$

The money-pump argument relies on a particular, far from uncontroversial, way to combine preferences in two dimensions, which is only possible if two crucial assumptions are satisfied: (1) The primary alternatives (the stamps) can be combined with some other commodity (money) to form composite alternatives. (2) Irrespectively of the previous transactions there is always, for each preferred change of primary alternatives, some non-zero loss of the auxiliary commodity (money) that is worth that change. The money-pump can be used to extract money from a subject with cyclic preferences only if these two conditions are satisfied.

Another argument for the normative appropriateness of preference transitivity suggests that transitivity is constitutive of the meaning of preference, in addition to the minimal properties mentioned in section 2.1. Drawing an analogy to length measurement, Davidson (1976, 273) asks: “If length is not transitive, what does it mean to use a number to measure length at all? We could find or invent an answer, but unless or until we do, we must strive to interpret ‘longer than’ so that it comes out transitive. Similarly for ‘preferred to’”. Violating transitivity, Davidson claims, thus undermines the very meaning of preferring an option over others.

Yet another argument rests on the importance of preferences for choice. When agents choose from an alternative set, then preferences should be *choice guiding*. They should have such a structure that they can be used to guide our choice among the elements of that set. But when choosing e.g. from $\{A,B,C\}$, a preference relation $\succ$ such that $A\succ B\succ C\succ A$ does not guide choice at all: any or none of the alternatives should be chosen according to $\succ$. The transitivity of preference, it is therefore suggested, is a necessary condition for a meaningful connection between preferences and choice. A critic, however, can point out that preferences are important even when they cannot guide choices. Take e.g. preferences over lottery outcomes: these are real preferences, regardless of the fact that one cannot choose between lottery outcomes. Further, the necessary criteria for choice guidance are much weaker than weak transitivity (Hansson 2001, 23–25; compare also versions of decision theory in which transitivity fails, e.g. Fishburn 1991)[^hansson-2001]. Last, the indifference relation does not satisfy choice guidance either. That does not make it irrational to be indifferent between alternatives. Thus, choice guidance can be an argument for the normative appropriateness of transitivity only under certain restrictions, if at all (For further discussion, see Anand 1993)[^anand-1993].

### 2.4 Order typology

One more property of preference relations needs to be specified. A relation is *antisymmetric* if

$$ A\succcurlyeq B \wedge B\succcurlyeq A \rightarrow A=B \text{ (antisymmetry of preference)} $$

The categories summarized in the table below (based on Sen 1970a)[^sen-1970a] are standardly used to denominate preference relations that satisfy certain logical properties.

|   | *Properties* | *Name(s)* |
| --- | --- | --- |
| 1. | reflexive, transitive | Preorder, Quasi-order |
| 2. | reflexive, transitive, anti-symmetric | Partial order |
| 3. | irreflexive, transitive | Strict partial order |
| 4. | reflexive, transitive, complete | Total preorder, Complete quasi-ordering, Weak ordering |
| 5. | reflexive, transitive, complete, anti-symmetric | Chain, Linear ordering, Complete ordering |
| 6. | asymmetric, transitive, weakly connected | Strict total order, Strong ordering |

### 2.5 Combinative preferences

Sections 2.1–2.4 were devoted to exclusionary preferences, i.e. preferences that refer to a set of mutually exclusive alternatives. In practice, people also have preferences between relata that are not mutually exclusive. These are called *combinative preferences*.

Relata of combinative preferences are not specified enough to be mutually exclusive. To say that one prefers having a dog over having a cat neglects the possibility that one may have both at the same time. Depending on how one interprets it, this preference expression may say very different things. It may mean that one prefers a dog (and no cat) to a cat (and no dog). Or, if one already has a cat, it may mean that one prefers a dog and a cat to just having a cat. Or, if one already has a dog, it may mean that one prefers just a dog to both a cat and a dog. Combinative preferences are usually taken to have states of affairs as their relata. These are represented by sentences in sentential logic. It is usually assumed that logically equivalent expressions can be substituted for each other.

Properties such as completeness, transitivity and acyclicity can be transferred from exclusionary to combinative preferences. In addition, there are interesting logical properties that can be expressed with combinative preferences but not with exclusionary preferences. The following are some examples of these (some of which are controversial):

$$\begin{align} p\succcurlyeq q \rightarrow p\succcurlyeq(p\vee q)\succcurlyeq q &\quad\text{(disjunctive interpolation)} \\ p\succcurlyeq q \rightarrow \neg q\succcurlyeq \neg p &\quad\text{(contraposition of weak preference)} \\ p\sim q \rightarrow \neg q\sim \neg p &\quad\text{(contraposition of indifference)} \\ p\succ q \rightarrow \neg q\succ \neg p &\quad\text{(contraposition of strict preference)} \\ p\succcurlyeq q \leftrightarrow (p\wedge \neg q)\succcurlyeq(q\wedge \neg p) &\quad\text{(conjunctive expansion of} \\ &\quad\text{ weak preference)} \\ p\succ q \leftrightarrow (p\wedge \neg q)\succ(q\wedge \neg p) &\quad\text{(conjunctive expansion of} \\ &\quad\text{ strict preference)} \\ p\sim q \leftrightarrow (p\wedge \neg q)\sim(q\wedge \neg p) &\quad\text{(conjunctive expansion of indifference)} \\ (p\vee q)\succcurlyeq r \leftrightarrow p\succcurlyeq r \wedge q\succcurlyeq r &\quad\text{(left disjunctive distribution of } \succcurlyeq) \\ p\succcurlyeq(q\vee r) \leftrightarrow p\succcurlyeq q \wedge p\succcurlyeq r &\quad\text{(right disjunctive distribution of } \succcurlyeq) \end{align}$$

Combinative preferences can be derived from exclusionary preferences, which are then taken to be more basic. In most variants of this approach, the underlying alternatives (to which the exclusionary preferences refer) are possible worlds, represented by maximal consistent subsets of the language (Rescher 1967, von Wright 1972)[^rescher-1967][^wright-1972]. However, it has been argued that a more realistic approach should be based on smaller alternatives that cover all the aspects under consideration – but not all the aspects that might have been considered. This approach may be seen as an application of Simon’s “bounded rationality view” (Simon 1957, 196–200)[^simon-1957].

The derivation of combinative preferences from exclusionary preferences can be obtained with a representation function. By this is meant a function $f$ that takes us from a pair $\langle p,q\rangle$ of sentences to a set $f(\langle p,q\rangle)$ of pairs of alternatives (perhaps possible worlds). Then $p\succcurlyeq$*$_f$q* holds if and only if $A\succcurlyeq B$ for all $\langle A,B\rangle \in f(\langle p,q\rangle)$ (Hansson 2001, 70–73)[^hansson-2001].

### 2.6 Preference-based monadic value predicates

In addition to the comparative notions, “better” and “of equal value”, informal discourse on values contains monadic (one-place) value predicates, such as “good”, “best”, “very bad”, “fairly good”, etc. Predicates representing these notions can be inserted into a formal structure that contains a preference relation.

Two major attempts have been made to define the principal monadic predicates “good” and “bad” in terms of the preference relation. One of these defines “good” as “better than its negation” and “bad” as “worse than its negation” (Brogan 1919)[^brogan-1919].

$$\begin{align} G_N p \leftrightarrow p\succ \neg p &\quad\text{(negation-related good)} \\ B_N p \leftrightarrow \neg p\succ p &\quad\text{(negation-related bad)} \end{align}$$

The other definition requires that we introduce, prior to “good” and “bad”, a set of neutral propositions. Goodness is predicated of everything that is better than some neutral proposition, and badness of everything that is worse than some neutral proposition. The best-known variant of this approach was proposed by Chisholm and Sosa (1966). According to these authors, a state of affairs is indifferent if and only if it is neither better nor worse than its negation. Furthermore, a state of affairs is good if and only if it is better than some indifferent state of affairs, and bad if and only if some indifferent state of affairs is better than it.

$$\begin{align} G_I p \leftrightarrow (\exists q)(p\succ q\sim \neg q) &\quad\text{(indifference-related good)} \\ B_I p \leftrightarrow (\exists q)(\neg q\sim q\succ p) &\quad\text{(indifference-related bad)} \end{align}$$

The negation-related and the indifference-related “good” respectively “bad” do not necessarily coincide. Both definitions have been developed with complete preference relations in mind, but formal models are available that do not require completeness. (Hansson 2001)[^hansson-2001]

A proposal for defining preferences in terms of the monadic predicates for “good” and “bad” was put forward by van Benthem (1982, p. 195). It assumes that goodness and badness are defined in relation to an alternative set, so that for instance $G_{\{x,y\}}x$ means that $x$ is good among the alternatives in $\{x,y\}$ and $B_{\{x,z,w\}}x$ that $x$ is bad among the alternatives in $\{x,z,w\}$. This gives rise to the following definitions:

$x \succ y$ if and only if $G_{\{x,y\}}x \amp \neg G_{\{x,y\}}y$  (goodness-based preference)

$x \succ y$ if and only if $B_{\{x,y\}}y \amp \neg B_{\{x,y\}}x$  (badness-based preference)

However, these two definitions are not equivalent, and neither of them is plausible in all cases. For instance, let $x$ be good and not bad in the context $\{x,y\}$, and let $y$ be neither good nor bad in the same context. Then $x \succ y$ holds according to first definition but $\neg(x \succ y)$ according to the second. To avoid such problems, Hansson and Liu (2014) proposed the following definition:

$x \succ y$ if and only if either $G_{\{x,y\}}x \amp \neg G_{\{x,y\}}y$ or $B_{\{x,y\}}y \amp \neg B_{\{x,y\}}x$ (bivalently based preference)

## 3. Numerical Representation of Preference

Preferences can be represented numerically. $A\succ B$ is then expressed by a set if numerical utility functions $\{u_i\}$, each of which assigns a higher value to $A$ than to $B$, while $A\sim B$ is represented by assigning the same value to the two. Such numerical representations might serve different purposes, one being that utility functions can be analysed with the tools of maximisation under constraints, as done in economics. It is important, however, to stress the limitations of such representations. First, not all preferences can be represented numerically. Second, there are different scales by which preferences can be represented, which require premises of different strengths. Third, the resulting utility representation must be clearly distinguished from the older hedonistic concept of utility.

### 3.1 Representing preferences ordinally

The simplest form of numerical representation stipulates the following equivalence:

$$ A\succ B \text{ iff } u(A)\gt u(B) \quad\text{(Ordinal representation)} $$

Any function $u$ that assigns a larger number to $A$ than to $B$ will work as such a representation. Consequently, the function $u$ can be replaced with any function *u’* as long as *u’* is a *positive monotone transformation* of $u$. As this transformation property is the defining characteristic of *ordinal scales*, we call this an ordinal preference representation (See the entry on measurement in science.)

A preference relation has an ordinal representation only if it satisfies both completeness and transitivity. However, even if $\mathcal{A}$ is finite, there can be complete and transitive preference relations on $\mathcal{A}$ that cannot be represented by a utility function (for a counter-example based on a lexicographic preference relation, see Debreu 1954)[^debreu-1954].[^note-2]

An *incomplete* preference ordering also has a value representation of the following type:

$$ \text{If } A\succ B, \text{ then } u(A)\gt u(B) $$

The inverse is obviously not true. However, under fairly wide circumstances, given the set of *all* utility functions thus defined, one can find the preference relation (Aumann 1962)[^aumann-1962].

### 3.2 Representing preferences cardinally

Ordinal numerical representations of preference are just a convenient tool – they do not represent any information that cannot be represented by the relation $\succ$ itself. However, there is relevant information about preferences that is not represented by the relation $\succ$ itself. For example, when an agent expresses two preferences, say $A\succ B$ and $C\succ B$, one might ask *how much* the agent prefers $A$ to $B$, in particular in comparison to how much she prefers $C$ to $B$. To answer this question, one needs to determine both a measurement procedure for measuring preference intensities and a measurement scale for representing these measurements.

Measurement scales that represent magnitudes of intervals between properties, or even magnitudes of ratios between properties, are called *cardinal* scales. Although the discussion in the social sciences often merely distinguishes between ordinal and cardinal preference measures, it is important to further distinguish between interval and ratio scales among the latter, as these require different assumptions to hold. An interval scale allows for meaningful comparisons of differences (e.g. “43°C is as much hotter than 41 °C as 29°C is hotter than 27°C”). In addition, a ratio scale also allows for meaningful comparisons of ratios (e.g. “12m is twice as long as 6m”). Although there have been some attempts to measure preferences on a ratio scale (in particular, see Kahneman and Tversky’s (1979) *Prospect Theory*, which requires a natural zero point and thus a ratio scale), most efforts have focussed on measuring preferences on an interval scale.

The basic idea of interval preference measurement is to assume that acts have uncertain consequences, and that each act is equivalent to a lottery between these outcomes. An agent who expresses a preference for an act over others by choosing it thus expresses a preference for the equivalent lottery over the lotteries equivalent to other acts. The utilities of these acts are then determined as the expected utilities of the equivalent lotteries, calculated as the probability-weighted average of the lottery’s consequences. This approach was pioneered by Ramsey (1928) and refined by von Neumann and Morgenstern (1944); other approaches have been presented by Savage (1954/72) and Jeffrey (1965/90). There are substantial differences between these approaches and their respective assumptions. For more detail, see decision theory.

### 3.3 Alternative utility-based representations of preference

As mentioned in section 3.1, all transitive and complete preference relations can be represented by a utility function according to the following simple relationship

$$ A\succ B \text{ iff } u(A) \gt u(B) $$

However, as can be seen from the Sorites paradox discussed in section 2.3, this recipe for the representation of preferences is too demanding for some purposes. If $u(A)\gt u(B)$, but $u(A)-u(B)$ is so small that it cannot be discerned, then $A\succ B$ cannot be expected to hold. One way to represent this feature is to employ a cardinal utility function and to introduce a fixed limit of indiscernibility, such that $A\succ B$ holds if and only if $u(A)-u(B)$ is larger than that limit. Such a limit is commonly called a *just noticeable difference* (JND).

$$ A\succ B \text{ iff } u(A)-u(B) \gt \delta, \quad(\text{JND representation, } \delta \gt 0) $$

If the set of alternatives is finite, then $\succcurlyeq$ has a JND representation if and only if $\succcurlyeq$ is complete, and satisfies the two properties that for all (A, B, C, D):

$$\begin{align} &A\succ B \wedge B\succ C \rightarrow A\succ D \vee D\succ C \text{ and } \\ &A\succ B \wedge C\succ D \rightarrow A\succ D \vee C\succ B. \end{align}$$

Another interesting construction is to assign to each alternative an interval instead of a single number. This requires two real-valued functions, $u_{max}$ and $u_{min}$, such that for all $A, u_{max}(A)\ge u_{min}(A)$. Here, $u_{max}(A)$ represents the upper limit of the interval assigned to $A$, and $u_{min}(A)$ its lower limit. $A \succ B$ holds if and only if all elements of the interval assigned to $A$ have higher value than all elements of the $B$ interval:

$$ A\succ B \text{ iff } u_{min}(A)\gt u_{max}(B) \quad\text{(Interval representation)} $$

It has been shown that a preference relation $\succcurlyeq$ has an interval representation if and only if it satisfies completeness and the property that for all $A, B, C, D$:

$$ A\succ B \wedge C\succ D \rightarrow A\succ D \vee C\succ B $$

(Fishburn 1970)[^fishburn-1970].

A final generalization is to let the threshold of discrimination depend on both relata.

$$\begin{align} A\succ B \text{ iff } u(A)-u(B)\gt \sigma(A, B) &\quad(\text{Doubly variable threshold}\\ &\quad\text{ representation } \sigma(A,B)\gt 0) \end{align}$$

If the set of alternatives is finite, then $\succcurlyeq$ has a doubly variable threshold representation if and only if it satisfies acyclicity.

For more details on these representations, see Scott and Suppes (1958) and Abbas (1995).

## 4. Preferences combination

In practical decision making, there are often several preference relations that have to be taken into account. The different preference relations represent different aspects of the subject matter concerned by the decision. For instance, when choosing among alternative architectural designs for a new building, we will have a whole set of aspects, each of which can be expressed with a preference relation: costs, sustainability, aesthetics, fire safety etc. In other cases, the various preference relations represent the wishes or interests of different persons. This applies for instance when a group of people with different preferences plan a joint vacation trip.

### 4.1 Managing preference conflicts

The most convenient way to represent problems with multiple preference aspects is to introduce a vector $\langle \succcurlyeq_1 ,\ldots ,\succcurlyeq_n \rangle$ whose elements are the preference relations we have to take into account. For simplicity, we can assume that all these preferences are complete (or we can treat incompleteness as indifference). We can call such a vector *conflict free* if and only if it has no elements $\succcurlyeq_k$ and $\succcurlyeq_m$ such that $X \succ_k Y$ and $Y \succ_m X$ for any alternatives $X$ and $Y$. If $\langle \succcurlyeq_1 ,\ldots ,\succcurlyeq_n \rangle$ is conflict free, then we can define a combined preference relation $\succcurlyeq$ such that (1) $X\succ Y$ if there is some $\succcurlyeq_k$ such that $X\succ_k Y$, (2) $Y\succ X$ if there is some $\succcurlyeq_k$ such that $Y\succ_k X$, and (3) otherwise $X\sim Y$. This is a plausible construction for conflict free preferences, since the combined preference relation does not contradict any of the strict preferences expressed in the component vectors.

For *conflictual* preference vectors, i.e. vectors that are not conflict free, there is no such simple solution that is plausible in all applications. There are five common ways to deal with conflicts among preferences.

*1. Reduction to a single dimension.* Such reductions are usually performed by first translating all preference relations into some numerical value, and then, for each alternative, adding up the values assigned to it for all aspects. In utilitarian moral philosophy, a fictional value unit, “utile”, is used for this purpose. In economics, cost-benefit analysis (CBA) instead uses monetary units. However in many cases there is uncertainty or disagreement on how the reductions should be performed.

*2. Assuming that all conflicts cancel each other out.* This amounts to extending the above definition of a combined preference relation so that $X\sim Y$ will hold in all cases of conflict, i.e. whenever there are $\succcurlyeq_k$ and $\succcurlyeq_m$ such that $X \succ_k Y$ and $Y \succ_m X$. Although usually not expressed in this way, this is the effect of applying efficiency as the sole criterion (e.g. Pareto efficiency as the sole criterion in a multi-person case). This method has the obvious disadvantage that it sometimes lets a small disadvantage in one dimension outweigh a large advantage in another dimension.

*3. Majoritarian solutions.* Another way to deal with conflicts is to look for the alternatives that are favoured by most (but not necessarily all) of the preference relations. This requires that the aspects covered by the different preference relations are valued equally. Therefore, this solution is commonly used when the elements of the vector correspond to the wishes or interests of different persons, but not when they correspond to more general aspects of a decision (such as sustainability and aesthetics in the example of of choosing an architectural design).

*4. Intuitive weighing.* In practice, decision makers often weigh different preference dimensions against each other intuitively, without any prior attempt to reduce the multi-dimensionality of the decision. This way of dealing with multiple preferences has practical advantages, but it also has the disadvantage of lacking efficient mechanisms for ensuring consistency in decision-making.

*5. Modifying at least one of the conflicting preference relations.* This is what happens when people involved in negotiations or discussions approach each other’s views in ways that make their preference relations less conflicting. The Delphi method is a systematized procedure that can be used to reduce interindividual differences in preferences. On an intraindividual level, strivings for a reflective equilibrium can take the form of adjusting preference relations that concern different aspects of an issue to each other. From a psychological point of view, such changes can be described as reductions of cognitive dissonance in value issues.

Voting procedures are often described as methods for aggregating or combining preferences. Such aggregation can also be performed by a benevolent planner striving to take the wishes and/or interests of all concerned persons into account. The aggregation of preferences is a major topic of social choice theory. See the entry on social choice theory.

### 4.2 Total and partial preferences

Consider again the choice among alternative architectural designs for a new building. As indicated above, our preferences can be expressed with a vector $\langle \succcurlyeq_1 ,\ldots ,\succcurlyeq_n \rangle$, each of whose elements represents our *partial* preferences with respect to some particular aspect such as sustainability or aesthetics. If we manage to aggregate the vector to a single preference relation $\succcurlyeq$, then $\succcurlyeq$ represents our *total preferences*, or, as they are also called, our “preferences *tout court*” or “preferences all things considered”.

Some authors have argued that the preference notion in economics always refers to total preferences (Hausman 2012)[^hausman-2012]. However, there are also economists who recognize partial preferences, often identifying them with preferences over properties or characteristics of economic goods (Lancaster 1966)[^lancaster-1966]. In contrast, philosophers often treat partial preferences as referring to different reasons that one may have to prefer one of the options to another (Pettit 1991, Osherson and Weinstein 2012)[^pettit-1991].

Authors who recognize partial preferences usually give them priority, and consider total preferences to be completely determined by the partial preferences. In other words, they assume that a total preference relation is uniquely determined by the partial preference relations through a process of aggregation. There are different views on the nature of this process. According to a *quantitative* approach, each partial preference is connected with a cardinal partial utility function for the aspect in question, and the total preference relation can be obtained by aggregating these partial utility functions using an appropriate set of weights. This requires strong assumptions of preference independence in order to justify additivity of utility (Keeney and Raiffa 1993).

An alternative strategy employs *tools from social choice theory* to map a vector of partial preferences into a total preference relation. This approach only makes use of ordinal information, and disregards any utility information that has no impact on the partial preference relations. Unsurprisingly, the impossibility results of social choice theory affect this method. Steedman and Krause (1986) have shown that there is no rule for deriving total preferences from a preference vector that satisfies four seemingly plausible conditions and also yields a transitive and complete total preference ordering. When applied to an intrapersonal conflict this means that an agent may be rational in the sense of having a complete and transitive (partial) relation for each of the aspects, but may still be irrational either in the sense of not satisfying plausible conditions on the relations between partial and total preferences, or in the sense of not having a complete and transitive total preference ordering for her overall appraisal of the options in question. This argument connects with a long philosophical tradition, including Plato and Bishop Butler, that draws an analogy between intrapersonal conflicts and citizens’ conflicting preferences within a state.

There are also authors who reject the idea that total preferences are uniquely derivable from partial preferences. Instead they claim that total preferences are *constructed* at the moment of elicitation, and thus influenced by contexts and framings of the elicitation procedure that are not encoded in pre-existing partial preferences (Payne, Bettman and Johnson 1993)[^payne-1993]. Total preferences seem to be influenced by direct affective responses that are independent of cognitive processes (Zajone 1980). For instance, food preferences seem to be partly determined by habituation and are therefore difficult to explain as the outcome of a process exclusively based on well-behaved partial preferences. According to this view, partial preferences are in many cases *ex post* rationalisations of total preferences, rather than the basis from which total preferences are derived.

A closely related standpoint was expressed by Nozick (1981, 244): “Reasons do not come with previously assigned weights; the decision process is not one of discovering such precise weights but of assigning them. The process not only weighs reasons, it (also) weights them.” According to Kranz (1991, 34), “[p]eople do *and should* act as problem solvers, not maximizers, because they have many different and incommensurable … goals to achieve”. Much in the same vein, Levi (1986, 246) maintained that “an agent may terminate deliberation and take decisions without having resolved the moral, political, economic and aesthetic conflicts relevant to their predicaments”.

## 5. Preferences and choice

There is a strong tradition, particularly in economics, to relate preference to choice. Preference is linked to hypothetical choice, and choice to revealed preference. We begin this section by presenting choice functions and some of their main properties. We then proceed to discuss how choice functions and their properties can be derived from preferences. Finally, we view the relationship from the other end, and introduce some approaches to inferring preferences from observed choices.

### 5.1 Choice functions and their properties

Given an alternative set $\mathcal{A}$, we can represent (hypothetical) choice as a function $\mathbf{C}$ that, for any given subset $\mathcal{B}$ of $\mathcal{A}$, delivers those elements of $\mathcal{B}$ that a deliberating agent has not ruled out for choice. For brevity’s sake we will call them ‘chosen elements’. The formal definition of a choice function is as follows:

$\mathbf{C}$ is a choice function for $\mathcal{A}$ if and only if it is a function such that for all $\mathcal{B} \subseteq \mathcal{A}$:

1. $\mathbf{C}(\mathcal{B}) \subseteq \mathcal{B}$, and
2. if $\mathcal{B} \ne \varnothing$, then $\mathbf{C}(\mathcal{B}) \ne \varnothing$.

A large number of rationality properties have been proposed for choice functions. The two most important of these are described here.

$$ \text{If } \mathcal{B} \subseteq \mathcal{A} \text{ then } \mathcal{B} \cap \mathbf{C}(\mathcal{A}) \subseteq \mathbf{C}(\mathcal{B}) \quad\text{(Property } \alpha, \text{ “Chernoff”)} $$

This property states that if some element of a subset $\mathcal{B}$ of $\mathcal{A}$ is chosen from $\mathcal{A}$, then it is also chosen from $\mathcal{B}$. According to property $\alpha$, removing some of the alternatives that are not chosen does not influence choice. This property has often been assumed to hold, but counterarguments have been raised against it. Consider the following example. Erna is invited to an acquaintance’s house for dinner. Her choice for dessert is between an apple (which is the last piece of fruit in the fruit basket) $(X)$ and nothing instead $(Y)$. Because Erna is polite, she chooses $Y$. Had she faced a choice between an apple $(X)$, nothing $(Y)$ and an orange $(Z)$, she would have taken the apple. Thus her choices are:

$$ \mathbf{C}(\{X,Y,Z\}) =\{X\} $$

and

$$\mathbf{C}(\{X,Y\}) =\{Y\}, $$

which violate property $\alpha$. More generally, property $\alpha$ has been contested with reference to cases when alternatives are preferred for their position in an alternative set, when the set of alternatives itself constitutes important information about the alternative chosen, or when certain alternatives provide the chooser with the freedom to reject them (Sen 1993, 501–503)[^sen-1993].[^note-3]

The second property states that if $X$ and $Y$ are both chosen from the subset $\mathcal{B}$ of $\mathcal{A}$, then one of them cannot be chosen in $\mathcal{A}$ without the other also being chosen.

$$\begin{align} \text{If } &\mathcal{B} \subseteq \mathcal{A} \text{ and } X, Y \in \mathbf{C}(\mathcal{B}), \text{ then } X \in \mathbf{C}(\mathcal{A}) \\ &\text{ iff } Y \in \mathbf{C}(\mathcal{A}) \quad(\text{Property } \beta) \end{align}$$

To exemplify property $\beta$, suppose that we have three restaurants, $X, Y$ and $Z$, within walking distance, and two additional restaurants, $V$ and $W$, that we can reach by car. Furthermore, suppose that we begin by choosing among the restaurants within walking distance. We agree that the choice is between $X$ and $Y$, but we find no reasons to choose one of them rather than the other, i.e. $\mathbf{C}(\{X, Y, Z\})=\{X,Y\}$. Then we find out that we do in fact have access to a car. Property $\beta$ says that if $X$ is one of the chosen restaurants in this situation, then so is $Y$, and vice versa. In other words: $X\in \mathbf{C}(\{X, Y, Z, V, W\})$ holds if and only if $Y \in \mathbf{C}(\{X, Y, Z, V, W\})$.

A third property, $\gamma$, is described in footnote.[^note-4]

The above properties are mainly found in the social choice literature. A related property in the economic literature is the so-called *Weak Axiom of Revealed Preferences* (WARP). It says that if $X$ is chosen when $Y$ is available, then there must not be an alternative set $\mathcal{B}$ containing both alternatives for which $Y$ is chosen and $X$ is not.

If $X,Y\in \mathcal{A}$ and $X\in \mathbf{C}(\mathcal{A})$, then for all $\mathcal{B}$, if $X\in \mathcal{B}$, and $Y\in \mathbf{C}(\mathcal{B})$, then $X\in \mathbf{C}(\mathcal{B})$   (WARP)

WARP is equivalent to the combination of properties $\alpha$ and $\beta$ (Sen 1971, 50)[^sen-1971]. A stronger version, SARP, is discussed in the first part of the supplementary document.

[The Strong Axiom of Revealed Preference](preferences.revealed-preference.md)

Counterexamples have been offered to show that these properties are not plausible in all situations. Consider an agent who chooses to stay at a friend’s house for a cup of tea $(T)$ rather than to go home $(H)$, but who leaves in a hurry when the friend offers a choice between tea and cocaine $(C)$ at his next visit. Then $\mathbf{C}(\{T,H\}) =\{T\}$ and $\mathbf{C}(\{T,H,C\}) =\{H\}$, and hence the visitor violates both properties $\alpha$ and $\beta$.

### 5.2 Determining choice from preference

A choice function that is defined on the basis of a preference relation is called *relational* (also *binary*). The most obvious way to construct a choice function from a preference relation $\succcurlyeq$ is to have the function always choose the elements that are best according to $\succcurlyeq$:

*The best choice connection* $\mathbf{C}^B(\mathcal{B}) = \{X \in \mathcal{B} \mid \forall Y \in \mathcal{B}: (X\succcurlyeq Y)\}$

$\mathbf{C}^B$ is a choice function (i.e. satisfies the defining criteria for a choice function given in section 5.1) if and only if $\succcurlyeq$ is complete and acyclical. It will then also satisfy properties $\alpha$ and $\gamma$. Furthermore, $\mathbf{C}^B$ satisfies property $\beta$ if and only if $\succcurlyeq$ is transitive and complete (Sen 1970a, 19)[^sen-1970a].

When the underlying preference relation is incomplete, there may not be an element that is preferred to all other elements. A function $\mathbf{C}$ constructed according to the best choice connection will then be empty, and hence not a choice function. To avoid this, an alternative connection constructs the choice function as choosing those elements that are not dispreferred to any other elements of the set:

*The non-dominance choice connection* $\mathbf{C}^L(\mathcal{B}) = \{X \in \mathcal{B} \mid \forall Y \in \mathcal{B}: \neg(Y\succ X)\}$

$\mathbf{C}^L$ is a choice function if and only if $\succcurlyeq$ is acyclical. It will then satisfy properties $\alpha$ and $\gamma$. Furthermore, $\mathbf{C}^L$ satisfies property $\beta$ if and only if $\succcurlyeq$ is transitive and complete (Herzberger 1973)[^herzberger-1973].

When the preference relation over $\mathcal{A}$ is cyclical, neither $\mathbf{C}^B$ nor $\mathbf{C}^L$ may be a relational choice function for $\mathcal{A}$. In the simplest case, with a cyclical preference $A\succ B\succ C\succ A$, $\mathbf{C}^B(A,B,C) = \mathbf{C}^L(A,B,C) = \varnothing$. Schwarz (1972) therefore proposes a third relational choice function, which operates even on the basis of cyclical preferences. Its basic idea is to select elements that are not dominated by non-cyclical preference.

### 5.3 Inferring preference from choice

The close connections between preference axioms and choice axioms can also be employed to construct a preference ordering from a choice function that satisfies certain axioms. In economics, the *revealed preference* approach has been used to define preference in terms of choice. Historically, this approach developed out of the pursuit of behaviouristic foundations for economic theories—i.e. the attempt to eliminate the preference framework altogether. Today, it serves to derive preference orderings from an agent’s observed choices, and to test the empirical validity of the preference axioms by testing for the violation of choice axioms (Grüne-Yanoff 2004)[^grüne-yanoff-2004].

There are many ways to construct preference relations from observed choices. The simplest method defines an alternative $X$ as “at least as good as” an alternative $Y$ if and only if $X$ is chosen from some set of alternatives that also contains $Y$.

$$\begin{align} \tag{1} X\succcurlyeq^S Y &\text{ iff for some } \mathcal{B}, X\in \mathbf{C}(\mathcal{B}) \text{ and } Y\in \mathcal{B} \\ X\succ^S Y &\text{ iff } X\succcurlyeq^S Y \text{ and not } Y\succcurlyeq^S X \\ X\sim^S Y &\text{ iff } X\succcurlyeq^S Y \text{ and } Y\succcurlyeq^S X \end{align}$$

If the choice function is defined over all subsets of $\mathcal{B}, \succcurlyeq^S$ is complete. $\succ^S$ does not necessarily satisfy transitivity of strict preference, transitivity of indifference, IP- or PI-transitivity. Two further methods are described in the supplementary document:

[The Strong Axiom of Revealed Preference](preferences.revealed-preference.md)

The formal relation to choice raises the question of the ontological status of preferences. Are preferences prior to choices, and function potentially as their cause? Or are preferences merely representations of actual or potential choice patterns? Debates about how to interpret preferences in economics have a long history, and in recent years the topic has received renewed attention. This discussion tended to focus on an opposition between behaviourist vs. mentalist interpretations. Many (but certainly not all) economists have interpreted the dominant revealed preference theory in behaviourist terms, claiming for example that “Standard economics does not address mental processes, and as a result, economic abstractions are typically not appropriate for describing them” (Gul and Pesendorfer 2008, 21). Consequently, these authors take the formal relations presented in this section as the determinants of the ontological question what preferences are. Furthermore, they also reject the interpretation of preferences as causes of choice, instead insisting that they only capture choice patterns (Binmore 2008, 19–22)[^binmore-2008].

Mentalists, in contrast, insist that choices and preferences are entities of quite different categories: Preferences are *states of mind* whereas choices are *actions*. Consequently, they reject the strong behaviourist program (Hausman 2012)[^hausman-2012]. An important mentalist argument against behaviourist interpretations concerns the role of beliefs in decision making. According to this argument, some choices are not based on stable preferences over actions, but are constructed from more basic cognitive and evaluative elements. A simple choice – like choosing between two pieces of candy – might be based on a preference for a world in which one eats candy $X$ over a world in which one eats candy $Y$. But more complex choices – e.g. choosing one’s higher education – depend on what one *believes* these choices to bring about, and how one evaluates these consequences. In those cases, a more complex framework specifies beliefs about the probability or plausibility of possible states of the world, preferences over the consequences of choices in those worlds, and an aggregation mechanism of these preferences under those beliefs. The need for such a cognitive structure to account for preferences has been proposed as an argument against the ontological reduction of preferences to choices (Hausman (2012).

Another argument against behaviourist interpretations points to the apparent existence of preferences over alternatives that one cannot choose between – for example preferences for winning a certain prize of a lottery, or for particular configurations of Paradise. This contradicts the claim that preferences exclusively transpire from choices. One way to substantiate preferences over alternatives that one cannot choose between is to ask people what they prefer. Their answers can be interpreted as further choice evidence – as verbal or writing *behaviour*. This interpretation treats their answers on a par with all other forms of behaviour. Alternatively, their answers can be interpreted as *introspective* reports. This interpretation treats answers as agents’ privileged access to their own minds. Furthermore, mentalists also distinguish between those agents who indeed have preferences as states of minds – e.g. humans, and maybe higher animals – and those agents who do not – e.g. machines, plants or institutions. The former category may choose on the basis of their preferences, and hence the above-discussed effort can aim at eliciting the preferences on which their choices are based. The latter category, despite their lack of states of mind, may nevertheless exhibit behaviour that can be interpreted as relational choice.

Functionalists’ accounts of preferences deny such an intrinsically mental interpretation of preferences, without reducing them to behaviour. In functionalism, the nature of preferences, like that of other mental states, is determined by what roles they play – e.g. in evaluating choice alternatives, and in motivating actions. Yet who assigns these roles, and what justifies such assignments? Most authors agree that it is “the ontological commitments of our best theory or theories in the relevant area” that perform this assignment (List and Dietrich 2016, 257)[^list-2016]. How preferences are individuated, then, is dependent on the purposes for ascribing them. For example, revealed preferences are considered real if they are non-redundantly useful for describing regularities in an individual’s behaviour:

> To show that RPT [revealed preference theory] is useful we must find some real structures that are usefully measured – where “usefully” means nonredundantly relevant to explanation and prediction–using coefficients and relations defined by its axioms. (Ross 2005, 143)[^ross-2005]

Revealed preference theory is nonredundantly relevant, Ross claims, because it makes sense of patterns like intentionality and agency that don’t reduce to physical patterns. To the extent that this is not merely a predictive but an explanatory task, one needs to admit the existence of these patterns, thus endorsing “intentional stance functionalism without sliding into instrumentalism” (Ross 2005, 143–4)[^ross-2005]. According to such a view, preferences are identified by the causal roles they play in generating human, animal and machine behaviour; and they are real to the extent that the best theories of such behaviour require their attribution.

Recently, some authors have sought to dissolve the simple dialectic between mentalism and behaviourism. Guala (2019, 389) argues that the debate is mainly motivated by a methodological, rather than an ontological concern: whether or not economics should accept a healthy injection of psychological theory and methods depends on the explanatory tasks at hand. Clark (2020) reasons that whether and how to treat preferences as genuine cognitive variables is a question that depends on the epistemic purposes of the investigation (or as he phrased it, “the ultimate aims of economics”). Similarly, Thoma (2021) and Vredenburgh (2020) argue that for their specific purposes, economists often have good reasons to largely “black box” the causes of choice in their modelling of economic behaviour.

## 6. Preference and welfare

Preference relates to welfare in rather intricate ways. Welfare is a fundamental concept in moral philosophy and economics. It refers to the fundamental good for individual human beings, and it is therefore an anthropocentric and individualist concept. In order to clarify the relationship between preference and welfare we need to distinguish between three variants of the concept of welfare.

According to the *material view*, a person’s welfare is a matter of her material conditions, such as access to food, shelter, healthcare and, generally speaking, the necessities and perhaps luxuries of life. This view of welfare has been criticized for being materialistic in the sense of pursuing material possessions at the expense of higher values. It also has to face the difficulties inherent in weighing different material goods against each other.

The other two principal views both treat welfare as a mental rather than a material issue. The *wish-based mental view* uses each person’s wishes (i.e. preferences in the informal sense of that word) as the criterion of welfare (Sen 1979)[^sen-1979]. A person is considered to have more welfare, the more her wishes are satisfied. If this view is applied within a utilitarian framework, then it gives rise to preference utilitarianism. This view of welfare has difficulties in dealing with misinformed and self-defeating wishes. It can also have difficulties with certain types of other-regarding wishes, e.g. malevolent ones. The usual way to deal with this is to require that preferences are filtered (“laundered”) and/or refined before they are used to judge a person’s welfare.

The filtering (“laundering”) of preferences can be justified by the everyday experience that some preferences are much more important for a person’s well-being than others. It can be argued that a plausible preference-based account of welfare cannot be based on total preferences, but would have to be based on a subset of “core” preferences that are important for the individual. The determination of that subset is expectedly contentious. If it is to be determined by others than the individual whose welfare is concerned, then problems of paternalism will be difficult to avoid.

Refinement of preferences is usually assumed to result in the person’s (hypothetical) “rational” or “ideally considered” preferences. “My ideally considered preferences are those I would have if I were to engage in thoroughgoing deliberation about my preferences with full pertinent information, in a calm mood, while thinking clearly and making no reasoning errors.” (Arneson 1989, 83; cf. Brandt 1979 and Rosati 2009)[^arneson-1989][^brandt-1979][^rosati-2009] A problem for this view is that there does not seem to be any easy way to determine, based on a person’s preferences and circumstances, what her ideally considered preferences would be.

Finally, the *state-dependent mental view* identifies a person’s welfare with some mental state such as happiness or satisfaction. It is assumed that the relevant states of mind can at least in principle be judged by external assessors. If such a view is applied within a utilitarian framework, then it can give rise to hedonistic utilitarianism. This view can be criticized for paternalism and for being uncritical towards arrangements in which individuals are happy in spite of being oppressed or deprived. Furthermore, the difficulties involved in comparing mental properties such as happiness in different persons creates a problem for views that depend on such comparisons for the determination of welfare. However, recent work on the measurement of happiness and life satisfaction has challenged that view, and may have opened up new avenues for research in both economics and moral philosophy. (Ng 1997)

Only one of these three views, namely the wish-based one, refers to what we usually call preferences. However, the other two can also be expressed in terms of preference (betterness) relations. We can use such relations to order material conditions respectively mental states in terms of how they satisfy the criteria of welfare that we have chosen to apply. It is important to distinguish between on the one hand preferences in the common sense of comparative likings, and on the other hand the use of a preference relation to express grades of any property whose structure satisfies the common formal requirement of such a relation.

A common problem for attempts to account for welfare in terms of preference is that we expect a person’s view of her own welfare to be essentially self-regarding, but her preferences can refer to concerns that are not self-regarding, such as her concerns for other people, her views on social justice, and her commitments for instance to traditions, conventions, and moral ideas (Sen 1977)[^sen-1977]. Our choices are influenced by this wide range of preferences. Therefore, it does not seem possible to link preferences strongly to welfare and at the same time link them strongly to choice.

## 7. Preference change

Preferences relate to time in several ways. Preference at one point in time can refer to what happens or happened at other points in time. Furthermore, preferences can change over time, due to changes in beliefs, values, tastes, or a combination of these. Section 7.1 explains why preference change requires explanatory and theoretical treatment. In the following sections, three types of explanatory models are discussed. (For more detail, see Grüne-Yanoff and Hansson 2009.)[^grüne-yanoff-2009] *Time preference* models (section 7.2) only refer to the temporal relationship between the occurrence of a preference and the objects it refers to. *Doxastic* change models (section 7.3) investigate how a change of an agent’s beliefs leads to a change in her preferences. *Valuational* change models (section 7.4) investigate how a change in an agent’s basic evaluations leads to a change in her preferences.

### 7.1 Evidence for preference change

Some authors have argued that preference change is only a superficial perception, and that the underlying preferences remain stable over time. But there are at least four arguments to the effect that people’s preferences really do change over time. First, many successful explanations of behavioural change have interpreted the empirical behavioural evidence as preference change. These explanations can be differentiated into models of *external influences* and models of *internal coherence*. External influence models attempt to establish general links between external events and agents’ preference formations. They include, for example, social imitation (Leibenstein 1950)[^leibenstein-1950], parental influence (Cavalli-Sforza 1973)[^cavalli-sforza-1973], habit formation (Pollack 1976)[^pollack-1976], and the effect of production patterns on consumption (Duesenberry 1949)[^duesenberry-1949]. Internal coherence models take certain external influences as given, and model preference change as an accommodation of these external influences. They include, for example, religious convictions (Iannaccone 1990)[^iannaccone-1990] and the effect of cognitive dissonance on preferences (Elster 1982)[^elster-1982].

A second argument for preference change is based on the correlations between physiological changes and changes in behaviour. Changes in blood sugar levels, for example, are correlated to feeding behaviour, sexual behaviour varies with hormonal changes, and many behavioural patterns change with increasing age (for references and discussion, see Loewenstein 1996)[^loewenstein-1996]. These correlations are not deterministic; such behavioural changes can be resisted in many cases. It is plausible to incorporate these potential physiological effects as *visceral preferences* in the general preference framework, and to treat the relevant physiological changes as closely connected with preference changes.

Third, most humans have introspective evidence for their own preferences changing over time. The favourite activities of a child are replaced by new pleasures as we grow up. Thus was the experience of Shakespeare’s Benedick: “…but doth not the appetite alter? A man loves the meat in his youth that he cannot endure in his age” (*Much ado about nothing* Act II, Scene III). Even in adult life, we are literally overcome by sudden and very radical (“transformative”) changes of preference. Paul (2014) has investigated the types of decision-making that this involves. It would be strange to claim in such cases that it is only our beliefs about the different types of activities that change. Explanations in terms of preference change are much more in line with how we spontaneously interpret our experiences of such changes.

Last, certain concepts like taste refinement or self-restraint cannot easily be understood without a notion of real preference change. In particular, self-restraint presupposes that the motivational components of one’s self can change, for example, through maturation or social influence; and that one can and should plan one’s future self by curbing certain appetites or by designing the environment in ways that affect one’s preferences.

### 7.2 Time preferences

The value that we assign to obtaining an advantage or disadvantage usually varies with the point in time when we obtain it. In typical cases, values decrease with time. For instance, most of us would prefer receiving a large sum of money now to receiving it five years later. Analytically, this temporal factor of evaluations is often separated from time-independent factors of evaluations.

The standard approach to this issue in economic analysis treats preference as based on value. Value is dealt with in a bifactorial model, in which the value of a future good is assumed to be equal to the product of two factors. One of these factors is a time-independent evaluation of the good in question, i.e. the value of obtaining it immediately. The other factor represents the subject’s pure time preferences. It is a function of the length of the delay, and is the same for all types of goods. The most common type of time preference function can be written

$$ v(A,t) = \frac{v(A,t_0)}{(1 + r)^{t-t_0}} $$

where $r$ is a discount rate and $t-t_0$ the duration of the delay. This is the *exponetentially discounted utility model* (DU), proposed by Samuelson (1937), which still dominates in economic analysis.

The choice of a discount rate can have a large impact on the calculated values. It is therefore often politically controversial. As one example of this, the discount rate used in assessing the economic effects of climate change can have significant consequences for the policy recommendations that are based on these assessments.

There is some evidence that the standard discounted utility model does not adequately represent human behaviour. For a simple example, consider a person who prefers one apple today to two apples tomorrow, but yet (today) prefers two apples in 51 days to one apple in 50 days. Although this is a plausible preference pattern, it is incompatible with the *exponentially* discounted utility model. It can however be accounted for in a bifactorial model with a declining discount rate. Pioneered by Ainslie (1992), psychologists and behavioural economists have therefore proposed to replace Samuelson’s exponential discounting model with a model of hyperbolic discounting. The hyperbolic model discounts the future consumption with a parameter inversely proportional to the delay of the consumption, and can therefore cover examples like the above.

Other deviations from the discounted utility model have also been demonstrated. Experimental evidence indicates that we tend to discount gains more than losses, and small amounts more than large amounts. Discount rates also differ between different goods (such as money and health). For some—but only some—types of goods, improving sequences of outcomes are preferred to declining sequences. For instance, many would prefer an increasing rather than a decreasing living standard across their work life. These are all patterns that cannot be handled in the bifactorial model with its object-independent time preferences (Loewenstein et al 2002)[^loewenstein-2002]. Given the empirical evidence, it is an open question whether the concept of “time preferences” is at all descriptively adequate.

It is a separate question whether pure time preferences are rational. Critics argue that one should want one’s life, *as a whole*, to go as well as possible, and that counting some parts of life more than others interferes with this goal (Pigou, 1920; Ramsey, 1928b; Rawls 1971)[^pigou-1920][^ramsey-1928b][^rawls-1971]. According to this view, it is irrational to prefer a smaller immediate good to a greater future good, because now and later are equally parts of one life. Choosing the smaller good or the greater bad makes one’s life, as a whole, turn out worse: “Rationality requires an impartial concern for all parts of our life. The mere difference of location in time, of something’s being earlier or later, is not a rational ground for having more or less regard for it” (Rawls 1971, 293)[^rawls-1971]. Critics of pure temporal preferences often attribute apparent departures from temporal neutrality to a *cognitive illusion* (which causes people to see future pleasures or pains in some diminished form) or to a *weakness of will* (which causes people to choose options against their better judgment).

Against the temporal neutrality of preferences, some have argued that there is no enduring, irreducible entity over time to whom all future utility can be ascribed; they deny that all parts of one’s future are *equally* parts of oneself (Parfit 1984)[^parfit-1984]. They argue, instead, that a person is a succession of overlapping selves related to varying degrees by memories, physical continuities, and similarities of character and interests, etc. By this view, it may be just as rational to discount one’s “own” future preferences, as to discount the preferences of another distinct individual, because the divisions between the stages of one’s life may be as “deep” as the distinctions between individuals.

If pure time preferences are rational, the question arises whether they are rationally required to adopt a certain form. Economists widely consider the EDU model to be the rational standard, to the extent that hyperbolic discounting is considered an indicator of irrationality worthy of policy intervention (Strotz 1956, O’Donoghue and Rabin 2015)[^o’donoghue-2015]. Samuelson (1937, 161), the inventor of the EDU, was more cautious:

> any connection between utility as discussed here and any welfare concept is disavowed. The idea that such a [mathematical] investigation could have any influence upon ethical judgments of policy is one which deserves the impatience of modern economists.

Recently, some authors developed critiques of the normative validity of EDU. Hedden (2015) argues that defending EDU would force one to make untestable distinctions between actual and ultimate preferences. Callender (2021, see also replies in this special issue) argues that EDU is not a universally valid standard, but instead is dependent on contextual factors as yet unspecified; and that many of the current policy recommendations derived from this purported normative standard are questionable.

A quite different critical approach to discounting is connected with the idea of sustainability. If sustainability is interpreted as meaning that future generations should have access to the same resources as those that the present generation has at its disposal, then sustainability is sure to be in conflict with economic policies based on exponential discounting. However, there are also views on sustainability that allow us to use up natural resources if we replace them by non-natural resources such as new technologies that will compensate for the loss. Such a “weak” notion of sustainability appears to be compatible with policies based on discounting of future effects, but it has been criticized for putting future generations at disadvantage. (Ng 2005)

### 7.3 Doxastic preference change

Two kinds of beliefs are especially important for doxastic models. The first is the belief that the presence of state $X$ makes a desired state $Y$ more likely. Take for example the belief that fluoride prevents dental cavities. This can lead a person to prefer fluoride toothpaste to others. If she comes to disbelieve this connection, she may well abandon this preference. More generally, if $X\wedge Y$ is preferred to $X\wedge \neg Y$, then a rise of the probability that $Y$ given $X$ will result in a rise in the desirability of $X$, and vice versa.

The second kind of belief relevant for doxastic preference change concerns prospects that influence the preference for other prospects without being probabilistically related. For example, one’s preference for winning a trip to Florida in the lottery will crucially depend on one’s belief about the weather there during the specified travel time, even though these two prospects are probabilistically unrelated. More generally, if $X\wedge Y$ is preferred to $X\wedge \neg Y$, with $X$ and $Y$ probabilistically not correlated, then a rise of the probability that $X$ will result in a rise in the desirability of $Y$ (even if it does not affect the probability of $Y)$, and vice versa.

Jeffrey (1977) provides a simple model of preference change as the consequence of an agent coming to believe a proposition $A$ to be true. His model incorporates both kinds of belief relevant for doxastic preference change. It is based on the notion of conditional preferences. Jeffrey treats preferences as a relation over propositions, viz. sets of possible worlds. They are represented by a utility function $\mathbf{U}$ (see section 2), such that:

$$ X\succcurlyeq Y \text{ iff } \mathbf{U}(X) \ge \mathbf{U}(Y). $$

$\mathbf{U}(X)$ in turn is defined as the probability-weighted average of the utility $u$ of all the possible worlds $w$ in which $X$ is true. For unconditional preferences the weighing is built on the probability function $P$ that represents the agent’s actual information. The conditional preference ordering $\succcurlyeq_A$, in contrast, is based on $P_A$, the probability distribution representing the counterfactual scenario that the agent accepts proposition $A$ as true. (For more discussion on the existence and uniqueness conditions of conditional preferences, see Luce and Krantz 1971, Joyce 1999, chapter 4, Bradley 1999)[^bradley-1999][^joyce-1999][^luce-1971]. Jeffrey shows that the posterior utility function $\mathbf{U}_A$ is related to the prior utility function $\mathbf{U}$ as follows:

$$ \mathbf{U}_A (X) = \mathbf{U}(A\cap X) $$

Conditional preferences allow modelling doxastic preference change. What matters for an agent’s evaluation and behaviour are his unconditional preferences, $\succcurlyeq_t$, which are unconditional only in the sense that they rely on the agent’s actual information at time $t$. When the agent accepts a new proposition $A$ at time $t+1$, his conditional-on-$A$ preferences become his unconditional preferences at $t+1$: $\succcurlyeq_{t+1} = \succcurlyeq_{A}.$

Jeffrey’s model is restricted in two ways. First, it requires an unchanging evaluative function $u$ defined over the atoms of the propositional space, viz. possible worlds. Thus for all doxastically changed preference orderings, the preferences over worlds remain identical. Second, the model only considers the effects of a belief change to certainty. But it is plausible that one’s preference – say, for a vacation in Florida – changes just because one believes that it is more likely that there will be a hurricane next week. Jeffrey’s model can be generalised by introducing a more general probability updating rule (e.g., Jeffrey conditionalisation). An alternative solution was proposed by Bradley (2005). It is based on relatively strong assumptions on the relation between prior and posterior unconditional preferences.

An important discussion from economics needs mentioning, namely the question whether models of doxastic preference change are capable in principle to represent *all* preference changes. This question originates with an important paper by Stigler and Becker (1977), who argued that a wide range of phenomena which are commonly thought of as preference changes—like addiction, habitual behaviour, fashions and the effects of marketing—can be explained by stable, well-behaved preferences. In a rather informal fashion, they argue that such explanations involve only changes in information (more precisely: prices and income), while leaving preferences intact. As a result of this, economists largely abandoned the discussion of preference change, believing that all preference change phenomena can be explained in this way. Prima facie, their proposed explanations exhibit important similarities to the discussed accounts of doxastic preference change. The results from that discussion, which show that models of doxastic preference change are subject to relatively strong constraints, may therefore put doubt on the orthodox position in economics that models of doxastic preference change are capable in principle to represent *all* preference changes.

### 7.4 Valuational preference change

If an agent forms a specific preference as a result of some experience, further changes in her overall preference state are often necessary to regain consistency. A model of preference change can therefore be constructed as an input-output model in the same style as standard models of belief change. (Hansson 1995, Liu 2011)[^hansson-1995][^liu-2011] Changes in preference are triggered by inputs that are represented by sentences expressing new preference patterns. Hence, if the subject grows tired of her previous favourite brand of mustard, $A$, and starts to like brand $C$ better, then this will be represented by a change with the sentence “$C$ is better than $A$”, in formal language $C\succ A$, as an input. However, a change in which the previous preference $A\succ C$ is replaced by the new preference $C\succ A$ can take place in different ways. For instance, there may be a third brand $B$ that was previously placed between $A$ and $C$ in the preference ordering. The instruction to make the new preference relation satisfy $C\succ A$ does not tell us where $B$ should be placed in the new ordering. The new ordering may for instance be either $C\succ A\succ B$ or $C\succ B\succ A$. One way to deal with this is to include additional information in the input, for instance specifying which element(s) of the alternative set should be moved while the others keep their previous positions. In our example, if only $C$ is going to be moved, then the outcome should satisfy $C\succ A\succ B$. These and other considerations make it necessary to modify the standard model of belief change in order to accommodate the subject matter of preferences.

## 8. Preference criticism

In scholarly discussions, preferences are usually taken to be open to rational criticism only insofar as (i) they have been inconsistent, violating some of the rationally justifiable preference axioms, or (ii) they (in combination with beliefs) commit the agent to inconsistent inferences.

Can there be rationally justifiable claims that certain *intrinsic* preferences – i.e. preferences that are not dependent on other preferences – are wrong, or should be changed? The Humean position answers no. Hume distinguished reason from the passion, and argued “that reason alone can never be a motive to any action of the will; that it can never oppose passion in the direction of the will” (*Treatise*, Book II, Part III, Section III). Humeans often took this distinction between beliefs and desires to imply not only that beliefs alone cannot motivate action, but also that desires are not open to similar rational criticism as beliefs. Therefore, Humeans conclude, preferences can only be criticised if they are *extrinsic* – i.e. instrumentally derived from other preferences on the basis of beliefs – or inconsistent. Such criticism of extrinsic preferences would seem ultimately to be a criticism of false beliefs, and it could be argued that it is therefore not really criticism of preferences (Broome 1993)[^broome-1993].

Several authors have argued for a more substantial criticism of preferences, including that of intrinsic ones. Some critics argue that some or all preferences are in fact a kind of belief, and hence open to the same rational criticism as beliefs. Two defences have been presented to counter this challenge. First, it has been claimed that that desires (standing for motivation in general) are fundamentally distinct from epistemic states in their *direction of fit*. Beliefs are directed to fit the world; hence their insufficient fit provides the basis for their criticism. Desires are directed to fit the world to them; hence they lack this basis for criticism (Smith 1987)[^smith-1987]. Second, Humeans have argued that treating desires as beliefs is incompatible with Bayesian decision theory and also with other, non-quantitative, decision theories (Lewis 1988, Collins 1991, Byrne/Hajek 1997)[^byrne-1997][^lewis-1988].

Some proponents of the criticizability of preferences have referred to second-order preferences. An addict may prefer not to prefer smoking; a malevolent person may prefer not to prefer evil actions; an indolent may prefer not to prefer to shun work; a daydreamer may prefer not to prefer what cannot be realised, etc. First-order preferences are criticisable if they do not comply with second-order preferences. (For accounts of second-order preferences, see Frankfurt 1971, Sen 1977.)[^frankfurt-1971][^sen-1977] Second-order preferences may trigger attempts to change one’s preferences. Methods of self-restraint, self-command and self-improvement have been extensively described (Schelling 1984, Elster 1989, 2000)[^elster-2000][^schelling-1984]. Already Hume described the possibility of rationally choosing such expedience (Grüne-Yanoff & McClennen 2006)[^grüne-yanoff-2006][^grüne-yanoff-2006-2].

Critics have argued against the possibility of rationally choosing such indirect preference-modifying strategies. Millgram (1998) argues that knowledge of the way such desires-at-will were brought about makes it impossible for them to actually function as the desires they are intended to be. He gives the example of a car salesman, who, in order to be successful in his work, makes himself prefer the various useless knick-knacks that the brand he represents offers for its cars. When the salesman is laid off, the car-dealer offers him a car with all the useless extras that he made himself prefer. Because he remembers how he acquired these preferences, he chooses not to act on them. So, Millgram argues, the desire-at-will was not genuine. What is missing, he points out, are the backward-directed inferential commitments that genuine preferences bring with them. Only if one forgets that one acquired a specific preference at will, or if one also acquires the inferential commitments of such a preference, can preferring-at-will be successful.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=preferences). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/preferences/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=preferences&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](http://philpapers.org/sep/preferences/) at [PhilPapers](http://philpapers.org/), with links to its database. |

## Other Internet Resources

[Please contact the author with suggestions.]

## Related Entries

behaviorism | decision theory | economics: philosophy of | economics [normative] and economic justice | measurement: in science | practical reason | social choice theory | Sorites paradox | voting: methods | well-being

## Notes（原文脚注）

[^note-1]: Bundles of goods are represented as vectors, where each position in the vector represents a specific good, and the scalar at that position denotes the number of units of that good. For convenience, economists often operate in two-goods worlds, where one good—the *numeraire*—stands for all the other goods (money is the most common numeraire). The countability of such bundles allows formulating two important preference properties.

Preferences are *monotone* if larger bundles are always preferred to smaller bundles of the same goods, i.e. if $A=\langle a_1,\ldots,a_n\rangle$ is preference ranked and there is a bundle $B=\langle b_1,\ldots,b_n \rangle$ such that for at least one $i$: $a_i\gt b_i$ and for all other $j$: $a_j\ge b_j$, then $A\succ B$.

Preferences are *homothetic* if indifference is retained under proportional expansions, i.e. if $A\sim B,$ then $aA\sim aB$ for any $a\ge 0 (aA$ is the vector obtained by multiplying each element of $A$ by $a)$. These properties allow inferring a preference relation over many alternatives on the basis of only a few observations.

[^note-2]: A lexicographic preference relation gives absolute priority to one good over another. In the case of two-goods bundles, $A\succ B$ if $a_1\gt b_1$, or $a_1 =b_1$ and $a_2 \gt b_2$. Good 1 then cannot be traded off by any amount of good 2. Debreu shows that such a preference relation cannot be represented by a standard utility function.

[^note-3]: This and the counterexample below have been dismissed on the ground that properties $\alpha$ and $\beta$ were intended only for changes in the set of alternatives which do not change the agent’s information of the alternatives’ desirability. However, it is not clear how much of a distinction can be made between cases for which the properties hold and those for which they do not, without recurring to criteria of the same type as $\alpha$ or $\beta$. Such a criticism thus runs the danger of turning into an immunising defence of the properties.

[^note-4]: The expansion property $\gamma$ requires that an element $X$ that is chosen from every set in a particular class must also be chosen from their union.

$$ \mathbf{C}(\mathcal{B}_1) \cap \ldots \cap \mathbf{C}(\mathcal{B}_n) \subseteq \mathbf{C}(\mathcal{B}_1 \cup \cdots \cup \mathcal{B}_n) \quad (\text{Property } \gamma, \text{Expansion}) $$

As an example of property $\gamma$, if one of the university’s best teachers in non-classical logic is also one of its best teachers in classical logic, then she is one of its best logic teachers.

[^abbas-1995]: Abbas, Moncef, 1995. “Any Complete Preference Structure Without Circuits Admits an Interval Representation”, *Theory and Decision*, 39: 115–126.

[^ainslie-1992]: Ainslie, George, 1992, *Picoeconomics: The Strategic Interaction of Successive Motivational States Within the Person*, Cambridge: Cambridge University Press.

[^anand-1993]: Anand, Paul, 1993, “The Philosophy of Intransitive Preference”, *Economic Journal*, 103: 337–346.

[^arneson-1989]: Arneson, Richard J., 1989, “Equality and Equal Opportunity for Welfare”, *Philosophical Studies*, 56: 77–93.

[^arrow-1963]: Arrow, Kenneth J., 1963, *Social Choice and Individual Values*, New Haven and London: Yale University Press, first edition 1951.

[^armstrong-1939]: Armstrong, Wallace E., 1939, “The Determinateness of the Utility Function”, *Economic Journal*, 49: 453–467.

[^armstrong-1948]: –––, 1948, “Uncertainty and the Utility Function”, *Economic Journal*, 58: 1–10.

[^aumann-1962]: Aumann, Robert J., 1962, “Utility Theory Without the Completeness Axiom”, *Econometrica*, 30(3): 445–462.

[^becker-1973]: Becker, Gary S. and Michael, Robert T., 1973, “On the New Theory of Consumer Behavior”, *The Economic Approach to Human Behavior*, Chicago: University of Chicago Press, 1976, pp. 131–149.

[^binmore-2008]: Binmore, K., 2008, *Rational Decisions*, Princeton: Princeton University Press.

[^böckenholt-2002]: Böckenholt, Ulf, 2002, “A Thurstonian Analysis of Preference Change”, *Journal of Mathematical Psychology*, 46: 300–314.

[^bradley-2005]: Bradley, Richard, 2005, “Radical Probabilism and Mental Kinematics”, *Philosophy of Science*, 72: 342–364.

[^bradley-1999]: –––, 1999, “Conditional Desirability”, *Theory and Decision*, 47(1): 23–55.

[^brandt-1979]: Brandt, Richard B., 1979, *A Theory of the Good and the Right*, Oxford: Oxford University Press.

[^brandt-1998]: –––, 1998, “The Rational Criticism of Preferences”, in *Preferences*, C. Fehige and U. Wessels (eds.), Berlin and New York: de Gruyter, pp. 63–77.

[^brogan-1919]: Brogan, Albert P., 1919, “The Fundamental Value Universal”, *Journal of Philosophy, Psychology and Scientific Method*, 16: 96–104.

[^broome-1993]: Broome, John, 1993, “Can a Humean be moderate?”, in *Value, Welfare and Morality*, R. G. Frey and Christopher Morris (eds.), Cambridge: Cambridge University Press, pp. 51–73.

[^byrne-1997]: Byrne, Alan and Alan Hájek, 1997, “David Hume, David Lewis, and Decision Theory”, *Mind*, 105: 422–428.

[^callender-2021]: Callender, C., 2021, “The Normative Standard for Future Discounting”, *Australian Philosophical Reviews*, forthcoming; [preprint of Callender 2021 available online](https://b41c42d4-d5c2-43d3-adb1-7757eb49d78b.filesusr.com/ugd/b2eedd_c7c672250c8a4139a13a45e108bb0f92.pdf?index=true).

[^cavalli-sforza-1973]: Cavalli-Sforza, L. Luca and M. W. Feldman, 1973, “Cultural Versus Biological Inheritance: Phenotypic Transmission from Parents to Children”, *Human Genetics*, 25: 618–637.

[^chang-1997]: Chang, Ruth, ed., 1997, *Incommensurability, Incomparability, and Practical Reason*, Cambridge: Cambridge University Press.

[^chisholm-1966]: Chisholm, Roderick and Ernest Sosa, 1966, “On the Logic of Intrinsically Better” *American Philosophical Quarterly*, 3: 244–49.

[^clarke-2020]: Clarke, C., 2020, “Functionalism and the Role of Psychology in Economics”, *Journal of Economic Methodology*, 27(4): 292–310.

[^collins-1988]: Collins, John, 1988, “Belief, Desire, and Revision”, *Mind*, 97: 333–42.

[^davidson-1976]: Davidson, Donald, 1976, “Hempel on Explaining Action”, in *Essays on Actions and Events*, Oxford: Oxford University Press, 1980, pp. 261–275.

[^davidson-1955]: –––, John McKinsey and Patrick Suppes, 1955, “Outlines of a Formal Theory of Value, I”, *Philosophy of Science*, 22: 140–160.

[^debreu-1954]: Debreu, Gerard, 1954, “Representation of a Preference Ordering by a Numerical Function”, in Thrall *et al*. (eds.), *Decision Processes*, New York: John Wiley, pp. 159–66.

[^duesenberry-1949]: Duesenberry, James S., 1949, *Income, Saving, and the Theory of Consumer* *Behavior*, Cambridge, MA and London: Harvard University Press.

[^easwaran-2014]: Easwaran, Kenny, 2014, “Decision Theory without Representation Theorems”, *Philosophers’ Imprint*, 14(27): 1–30.

[^elster-1979]: Elster , 1979, *Ulysses and the Sirens*, Cambridge: Cambridge University Press.

[^elster-1982]: –––, 1982, “Sour Grapes: Utilitarianism and the Genesis of Wants”, in Amartya Sen and Bernard Williams (eds.), *Utilitarianism and Beyond*, Cambridge: Cambridge University Press, 1982, pp. 219–238.

[^elster-2000]: –––, 2000, *Ulysses Unbound*, Cambridge: Cambridge University Press.

[^fishburn-1970]: Fishburn, Peter C., 1970, “Intransitive Indifference with Unequal Indifference Intervals”, *Journal of Mathematical Psychology*, 7: 144–149.

[^fishburn-nd]: –––“Nontransitive Additive Conjoint Measurement”, *Journal of Mathematical Psychology*, 35: 1–40.

[^frankfurt-1971]: Frankfurt, Harry, 1971, “Freedom of the Will and the Concept of a Person”, *Journal of Philosophy*, 68: 5–20.

[^friedman-1953]: Friedman, Milton, 1953, “The Methodology of Positive Economics”, in *Essays in Positive Economics*, Chicago: University of Chicago Press, pp. 3–43.

[^grüne-yanoff-2004]: Grüne-Yanoff, Till, 2004, “The Problems of Testing Preference Axioms with Revealed Preference Theory”, *Analyse & Kritik*, 26(2): 382–397.

[^grüne-yanoff-2006]: –––, 2006, “Why Don’t You Want to be rich? Preference Explanations on the Basis of Causal Structure”, in J.K. Campbell and M. O’Rourke (eds.), *Topics in Contemporary Philosophy: Explanation and Causation*, Cambridge, MA and London: MIT Press, pp. 217–240.

[^grüne-yanoff-2015]: –––, 2015, “Models of Temporal Discounting 1937–2000: An Interdisciplinary Exchange Between Economics and Psychology”, *Science in Context*, 28(4): 675–713.

[^grüne-yanoff-2006-2]: –––, and Edward McClennen, 2006, “Hume’s Framework for a Natural History of the Passions”, in Margaret Schabas and Carl Wennerlind (eds.), *Hume’s Political Economy*, London and New York: Routledge, pp. 86–104.

[^grüne-yanoff-2009]: –––, and S. O. Hansson (eds.), 2009, *Preference Change: Approaches from Philosophy, Economics and Psychology* (Theory and Decision Library), Dordrecht: Springer.

[^guala-2019]: Guala, F., 2019, “Preferences: Neither Behavioural nor Mental”, *Economics and Philosophy*, 35(3): 383–401.

[^halldén-1957]: Halldén, Sören, 1957, *On the Logic of Better*, Lund: Library of Theoria.

[^hansson-1995]: Hansson, Sven Ove, 1995, “Changes in Preference”, *Theory and Decision*, 38: 1–28.

[^hansson-2001]: –––, 2001, *The Structure of Values and Norms*, Cambridge: Cambridge University Press.

[^hansson-2014]: –––and Fenrong Liu, 2014, “From Good to Better. Using Contextual Shifts to Define Preference in Terms of Monadic Value”, in Alexandru Baltag and Sonja Smets (eds.), *Johan van Benthem on Logic and Information Dynamics*, Dordrecht: Springer, pp. 729–747.

[^hausman-2012]: Hausman, Daniel M., 2012, *Preference, Value, Choice, and Welfare*, New York: Cambridge University Press.

[^hedden-2015]: Hedden, B., 2015, *Reasons without Persons: Rationality, Identity, and Time*, Oxford: Oxford University Press.

[^herzberger-1973]: Herzberger, Hans G., 1973, “Ordinal Preference and Rational Choice”, *Econometrica*, 41(2): 187–237.

[^hutcheson-1726]: Hutcheson, Francis, 1726, *An Inquiry into the Original of Our Ideas of Beauty and Virtue in Two Treatises*, ed. Wolfgang Leidhold, Indianapolis: Liberty Fund, 2004.

[^iannaccone-1990]: Iannaccone, Laurence R, 1990, “Religious Practice: A Human Capital Approach”, *Journal for the Scientific Study of Religion*, 29: 297–314.

[^jeffrey-1977]: Jeffrey, Richard C, 1977, “A Note on the Kinematics of Preference”, *Erkenntnis*, 11: 135–141.

[^joyce-1999]: Joyce, James, 1999, *Foundations of Causal Decision Theory*, Cambridge: Cambridge University Press.

[^krantz-1991]: Krantz, David. H.,1991, “From Indices to Mappings: The Representational Approach to Measurement”, in D. R. Brown & J. E. K. Smith (eds.), Frontiers of Mathematical Psychology: Essays in honor of Clyde Coombs, Berlin, Heidelberg and New York: Springer Verlag, pp. 1–52.

[^kusser-1989]: Kusser, Anna, 1989, *Dimensionen der Kritik von Wünschen*, Frankfurt am Main: Athenäum.

[^lancaster-1966]: Lancaster, Kevin J., 1966, “A New Approach to Consumer Theory”, *Journal of Political Economy*, 74: 132–57.

[^leibenstein-1950]: Leibenstein, Harvey, 1950, “Bandwagon, Snob, and Veblen Effects in the Theory of Consumer Demand”, *Quarterly Journal of Economics*, 64: 183–207.

[^levi-1986]: Levi, Isaac, 1986, *Hard Choices*, Cambridge: Cambridge University Press.

[^lewis-1988]: Lewis, David, 1988, “Desire as Belief”, *Mind*, 97: 323–332.

[^list-2016]: List, C. and F. Dietrich, 2016, “Mentalism versus Behaviourism in Economics: A Philosophy-of-Science Perspective”, *Economics and Philosophy*, 32(2): 249–281.

[^liu-2011]: Liu, Fenrong, 2011, *Reasoning About Preference Dynamics*. Dordrecht: Springer.

[^loewenstein-1996]: Loewenstein, George, 1996, “Out of Control: Visceral Influences on Behavior”, *Organizational Behavior and Human Decision Processes*, 65: 272–92.

[^loewenstein-2002]: Loewenstein, G., Read, D. and Baumeister, R. (eds.), 2002, *Time and Decision: Economic and Psychological Perspectives on Intertemporal Choice*, New York: Russell Sage Foundation Press.

[^loomes-1982]: Loomes, G. and R. Sugden. (1982). “Regret Theory: An Alternative Theory of Rational Choice Under Uncertainty”, *The Economic Journal*, 92: 805–824.

[^luce-1956]: Luce, R. Duncan 1956, “Semiorders and a Theory of Utility Discrimination”, *Econometrica*, 24: 178–191.

[^luce-1971]: –––, and Krantz, DH, 1971, “Conditional Expected Utility”, *Econometrica*, 39: 253–271.

[^mäki-2000]: Mäki, U., 2000, “Reclaiming relevant realism”, *Journal of Economic Methodology*, 7(1): 109–125.

[^millgram-1998]: Millgram, Elijah, 1998, “Deciding to Desire”, in *Preferences*, C. Fehige and U. Wessels (eds.), Berlin and New York: de Gruyter, pp. 3–25.

[^ng-1997]: Ng, Yew-Kwang, 1997, “A Case for Happiness, Cardinalism, and Interpersonal Comparability”, *Economic Journal*, 107: 1848–1858.

[^ng-2005]: –––, 2005. “Intergenerational Impartiality: Replacing Discounting by Probability Weighting”, *Journal of Agricultural and Environmental Ethics*, 18(3): 237–257.

[^nozick-1981]: Nozick, Robert, 1981, *Philosophical Explanations*, Cambridge: Belknap Press.

[^o’donoghue-2015]: O’Donoghue, T., and M. Rabin, 2015, “Present Bias: Lessons Learned and to be Learned”, *American Economic Review*, 105(5): 273–79.

[^parfit-1984]: Parfit, Derek, 1984, *Reasons and Persons*, Oxford: Oxford University Press.

[^paul-2014]: Paul, L.A., 2014, *Transformative Experience*, New York, NY: Oxford University Press.

[^payne-1993]: Payne, John W., James R. Bettman and Eric J. Johnson, 1993, *The Adaptive Decision Maker*, Cambridge: Cambridge University Press.

[^pettit-1991]: Pettit, Philip, 1991, “Decision Theory and Folk Psychology”, in *Rules, Reasons, and Norms: Selected Essays*, Oxford: Oxford University Press, Oxford, 2002, pp. 192–221.

[^pigou-1920]: Pigou, Arthur, C., 1920, *The Economics of Welfare*, London: MacMillan & Co.

[^pollack-1976]: Pollack, Robert A., 1976, “Habit Formation and Long Run Utility Functions”, *Journal of Economic Theory*, 13: 272–297.

[^quinn-1990]: Quinn, Warren S., 1990, “The Puzzle of the Self-Torturer”, *Philosophical Studies*, 59: 79–90.

[^ramsey-1928]: Ramsey, Frank P., 1928, “Truth and Probability”, in *The Foundations of Mathematics and other Logical Essays*, ed. R. B. Braithwaite, London: Routledge & Kegan Paul, 1950, pp. 156–198.

[^ramsey-1928b]: –––, 1928b, “A Mathematical Theory of Saving”, *Economic Journal*, 38: 543–59.

[^rawls-1971]: Rawls, John, 1971, *A Theory of Justice*, Oxford: Oxford University Press.

[^rescher-1967]: Rescher, Nicholas, 1967, “Semantic Foundations for the Logic of Preference”, in *The Logic of Decision and Action*, Pittsburgh: University of Pittsburgh Press, pp. 37–62.

[^rosati-2009]: Rosati, Connie S. 2009, “Relational Good and the Multiplicity Problem”, *Philosophical Issues*, 19(1): 205–34.

[^ross-2005]: Ross, D., 2005, *Economic Theory and Cognitive Science: Microexplanation*, Cambridge, MA: MIT Press.

[^ross-2014]: –––, 2014, *Philosophy of Economics*, New York: Palgrave Macmillan.

[^russell-1992]: Russell, Bernard, 1992, *The Autobiography of Bertrand Russell*, London and New York: Routledge.

[^samuelson-1937]: Samuelson, Paul A., 1937, “A Note on Measurement of Utility”, *Review of Economic Studies*, 4: 155–61.

[^samuelson-1938]: –––, 1938, “A Note on the Pure Theory of Consumer's Behaviour”, *Economica*, 5: 61–67.

[^schelling-1984]: Schelling, Thomas, C. 1984, “The Intimate Contest for Self-Command”, in *Choice and Consequence: Perspectives of an Errant Economist*, Cambridge, MA: Harvard University Press, pp. 57–82.

[^schumm-1987]: Schumm, George F., 1987, “Transitivity, Preference and Indifference”, *Philosophical Studies*, 52: 435–437.

[^schwartz-1972]: Schwartz, Thomas, 1972, “Rationality and the Myth of the Maximum”, *Noûs*, 6: 97–117.

[^scott-1958]: Scott, Dana, and Patrick Suppes, 1958. “Foundational aspects of theories of measurement”, *Journal of Symbolic Logic*, 23:113–128.

[^sen-1970a]: Sen, Amartya, 1970a, *Collective Choice and Social Welfare*, San Francisco: Holden Day, Inc..

[^sen-1970b]: –––, 1970b, “The Impossibility of a Paretian Liberal”, *Choice Welfare and Measurement*, Cambridge, MA: Harvard University Press, 1982, pp. 285–290.

[^sen-1971]: –––, 1971, “Choice Functions and Revealed Preference”, *Choice Welfare and Measurement*, Cambridge, MA: Harvard University Press, 1982, pp. 41–53.

[^sen-1977]: –––, 1977, “Rational Fools”, *Choice Welfare and Measurement*, Cambridge, MA: Harvard University Press, 1982, pp. 84–106.

[^sen-1979]: –––, 1979,“Utilitarianism and Welfarism”, *Journal of Philosophy*, 76(9): 463–489.

[^sen-1993]: –––, 1993, “Internal Consistency of Choice”, *Econometrica*, 61(3): 495–521.

[^smith-1987]: Smith, Michael, 1987, “The Humean Theory of Motivation”, *Mind*, 96: 36–61.

[^simon-1957]: Simon, Herbert, 1957, *Models of Man*, John Wiley & Sons, New York.

[^steedman-1986]: Steedman, Ian and Ulrich Krause, 1986, “Goethe’s Faust, Arrow’s Possibility Theorem and the Individual Decision-Taker”, in Jon Elster (ed.), *The Multiple Self*, Cambridge: Cambridge University Press, pp. 197–232.

[^stigler-1977]: Stigler, George J. and Gary S. Becker, 1977, “De Gustibus Non Est Disputandum”, *American Economic Review*, 67: 76–90.

[^thoma-2021]: Thoma, J., 2021, “In Defence of Revealed Preference Theory”, *Economics and Philosophy*, 37(2): 163–187.

[^benthem-1982]: van Benthem, Johan, 1982, “Later than Late: On the Logical Origin of the Temporal Order”, *Paciﬁc Philosophical Quarterly*, 63: 193–203.

[^wright-1963]: von Wright, Georg H., 1963, *The Logic of Preference*, Edinburgh: Edinburgh University Press.

[^wright-1972]: –––, 1972, “The Logic of Preference Reconsidered”, *Theory and Decision*, 3: 140–169.

[^vredenburgh-2020]: Vredenburgh, K., 2020, “A Unificationist Defence of Revealed Preferences”, *Economics and Philosophy*, 36(1): 149–169.
