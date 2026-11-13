# Voting Methods
**First published Wed Aug 3, 2011; substantive revision Mon Jun 24, 2019**

*Pacuit, Eric*

A fundamental problem faced by any group of people is how to arrive at a good group decision when there is disagreement among its members. The difficulties are most evident when there is a large number of people with diverse opinions, such as, when electing leaders in a national election. But it is often not any easier with smaller groups, such as, when a committee must select a candidate to hire, or when a group of friends must decide where to go for dinner. Mathematicians, philosophers, political scientists and economists have devised various voting methods that select a winner (or winners) from a set of alternatives taking into account everyone’s opinion. It is not hard to find examples in which different voting methods select different winners given the same inputs from the members of the group. What criteria should be used to compare and contrast different voting methods? Not only is this an interesting and difficult theoretical question, but it also has important practical ramifications. Given the tumultuous 2016 election cycle, many people (both researchers and politicians) have suggested that the US should use a different voting method. However, there is little agreement about which voting method should be used.

This article introduces and critically examines a number of different voting methods. Deep and important results in the theory of social choice suggest that there is no single voting method that is best in all situations (see List 2013 for an overview)[^list-2013][^list-2013-2]. My objective in this article is to highlight and discuss the key results and issues that facilitate comparisons between voting methods.

## 1. The Problem: Who *Should* be Elected?

Suppose that there is a group of 21 voters who need to make a decision about which of four candidates should be elected. Let the names of the candidates be $A$, $B$, $C$ and $D$. Your job, as a social planner, is to determine which of these 4 candidates should win the election given the *opinions* of all the voters. The first step is to elicit the voters’ opinions about the candidates. Suppose that you ask each voter to rank the 4 candidates from best to worst (not allowing ties). The following table summarizes the voters’ rankings of the candidates in this hypothetical election scenario.

| # Voters | Ranking |
| --- | --- |
| 3 | $A\s B\s C\s D$ |
| 5 | $A\s C\s B\s D$ |
| 7 | $B\s D\s C\s A$ |
| 6 | $C\s B\s D\s A$ |

Read the table as follows: Each row represents a ranking for a group of voters in which candidates to the left are ranked higher. The numbers in the first column indicate the number of voters with that particular ranking. So, for example, the third row in the table indicates that 7 voters have the ranking $B\s D\s C\s A$ which means that each of the 7 voters rank $B$ first, $D$ second, $C$ third and $A$ last. Suppose that, as the social planner, you do not have any personal interest in the outcome of this election. Given the voters’ expressed opinions, which candidate should win the election? Since the voters disagree about the ranking of the candidates, there is no obvious candidate that best represents the group’s opinion. If there were only two candidates to choose from, there is a very straightforward answer: The winner should be the candidate or alternative that is supported by more than 50 percent of the voters (cf. the discussion below about May’s Theorem in Section 4.2). However, if there are more than two candidates, as in the above example, the statement “the candidate that is supported by more than 50 percent of the voters” can be interpreted in different ways, leading to different ideas about who should win the election.

One candidate who, at first sight, seems to be a good choice to win the election is $A$. Candidate $A$ is ranked first by more voters than any other candidate. ($A$ is ranked first by 8 voters, $B$ is ranked first by 7; $C$ is ranked first by 6; and $D$ is not ranked first by any of the voters.) Of course, 13 people rank $A$ *last*. So, while more voters rank $A$ first than any other candidate, more than half of the voters rank $A$ last. This suggests that $A$ should *not* be elected.

None of the voters rank $D$ first. This fact alone does not rule out $D$ as a possible winner of the election. However, note that every voter ranks candidate $B$ above candidate $D$. While this does not mean that $B$ should necessarily win the election, it does suggest that $D$ should not win the election.

The choice, then, boils down to $B$ and $C$. It turns out that there are good arguments for each of $B$ and $C$ to be elected. The debate about which of $B$ or $C$ should be elected started in the 18th-century as an argument between the two founding fathers of voting theory, Jean-Charles de Borda (1733–1799) and M.J.A.N. de Caritat, Marquis de Condorcet (1743–1794). For a history of voting theory as an academic discipline, including Condorcet’s and Borda’s writings, see McLean and Urken (1995). I sketch the intuitive arguments for the election of $B$ and $C$ below.

*Candidate $C$ should win*. Initially, this might seem like an odd choice since both $A$ and $B$ receive more first place votes than $C$ (only 6 voters rank $C$ first while 8 voters rank $A$ first and 7 voters rank $B$ first). However, note how the population would vote in the various two-way elections comparing $C$ with each of the other candidates:

| # Voters | $C$ versus $A$ | $C$ versus $B$ | $C$ versus $D$ |
| --- | --- | --- | --- |
| 3 | $\bA\s \gB\s \bC\s \gD$ | $\gA\s \bB\s \bC\s \gD$ | $\gA\s \gB\s \bC\s \bD$ |
| 5 | $\bA\s \bC\s \gB\s \gD$ | $\gA\s \bC\s \bB\s \gD$ | $\gA\s \bC\s \gB\s \bD$ |
| 7 | $\gB\s \gD\s \bC\s \bA$ | $\bB\s \gD\s \bC\s \gA$ | $\gB\s \bD\s \bC\s \gA$ |
| 6 | $ \bC\s \gB\s \gD\s \bA$ | $ \bC\s \bB\s \gD\s \gA$ | $ \bC\s \gB\s \bD\s \gA$ |
| Totals: | 13 rank $C$ above $A$ 8 rank $A$ above $C$ | 11 rank $C$ above $B$ 10 rank $B$ above $C$ | 14 rank $C$ above $D$ 7 rank $D$ above $C$ |

Condorcet’s idea is that $C$ should be declared the winner since she beats every other candidate in a one-on-one election. A candidate with this property is called a **Condorcet winner**. We can similarly define a **Condorcet loser**. In fact, in the above example, candidate $A$ is the Condorcet loser since she loses to every other candidate in a one-on-one election.

*Candidate $B$ should win*. Consider $B$’s performance in the one-on-one elections.

| # Voters | $B$ versus $A$ | $B$ versus $C$ | $B$ versus $D$ |
| --- | --- | --- | --- |
| 3 | $\bA\s \bB\s \gC\s \gD$ | $\gA\s \bB\s \bC\s \gD$ | $\gA\s \bB\s \gC\s \bD$ |
| 5 | $\bA\s \gC\s \bB\s \gD$ | $\gA\s \bC\s \bB\s \gD$ | $\gA\s \gC\s \bB\s \bD$ |
| 7 | $\bB\s \gD\s \gC\s \bA$ | $\bB\s \gD\s \bC\s \gA$ | $\bB\s \bD\s \gC\s \gA$ |
| 6 | $ \gC\s \bB\s \gD\s \bA$ | $ \bC\s \bB\s \gD\s \gA$ | $ \gC\s \bB\s \bD\s \gA$ |
| Totals: | 13 rank $B$ above $A$ 8 rank $A$ above $B$ | 10 rank $B$ above $C$ 11 rank $C$ above $B$ | 21 rank $B$ above $D$ 0 rank $D$ above $B$ |

Candidate $B$ performs the same as $C$ in a head-to-head election with $A$, loses to $C$ by only one vote and beats $D$ in a landslide (everyone prefers $B$ over $D$). Borda suggests that we should take into account *all* of these facts when determining which candidate best represents the overall group opinion. To do this, Borda assigns a score to each candidate that reflects how much support he or she has among the electorate. Then, the candidate with the largest score is declared the winner. One way to calculate the score for each candidate is as follows (I will give an alternative method, which is easier to use, in the next section):

- $A$ receives 24 points (8 votes in each of the three head-to-head elections)
- $B$ receives 44 points (13 points in the competition against $A$, plus 10 in the competition against $C$ plus 21 in the competition against $D$)
- $C$ receives 38 points (13 points in the competition against $A$, plus 11 in the competition against $B$ plus 14 in the competition against $D$)
- $D$ receives 20 points (13 points in the competition against $A$, plus 0 in the competition against $B$ plus 7 in the competition against $C$)

The candidate with the highest score (in this case, $B$) is the one who should be elected.

Both Condorcet and Borda suggest comparing candidates in one-on-one elections in order to determine the winner. While Condorcet tallies how many of the head-to-head races each candidate wins, Borda suggests that one should look at the margin of victory or loss. The debate about whether to elect the Condorcet winner or the Borda winner is not settled. Proponents of electing the Condorcet winner include Mathias Risse (2001, 2004, 2005) and Steven Brams (2008); Proponents of electing the Borda winner include Donald Saari (2003, 2006) and Michael Dummett (1984). See Section 3.1.1 for further issues comparing the Condorcet and Borda winners.

The take-away message from this discussion is that in many election scenarios with more than two candidates, there may not always be one obvious candidate that best reflects the overall group opinion. The remainder of this entry will discuss different methods, or procedures, that can be used to determine the winner(s) given the a group of voters’ opinions. Each of these methods is intended to be an answer to the following question:

Given a group of people faced with some decision, how should a central authority combine the individual opinions so as to best reflect the “overall group opinion”?

A complete analysis of this question would incorporate a number of different issues ranging from central topics in political philosophy about the nature of democracy and the “will of the people” to the psychology of decision making. In this article, I focus on one aspect of this question: the formal analysis of algorithms that aggregate the opinions of a group of voters (i.e., voting methods). Consult, for example, Riker 1982, Mackie 2003, and Christiano 2008 for a more comprehensive analysis of the above question, incorporating many of the issues raised in this article.

### 1.1 Notation

In this article, I will keep the formal details to a minimum; however, it is useful at this point to settle on some terminology. Let $V$ and $X$ be finite sets. The elements of $V$ are called voters and I will use lowercase letters $i, j, k, \ldots$ or integers $1, 2, 3, \ldots$ to denote them. The elements of $X$ are called candidates, or alternatives, and I will use uppercase letters $A, B, C, \ldots $ to denote them.

Different voting methods require different types of information from the voters as input. The input requested from the voters are called **ballots**. One standard example of a ballot is a **ranking** of the set of candidates. Formally, a ranking of $X$ is a relation $P$ on $X$, where $Y\mathrel{P} Z$ means that “$Y$ is ranked above $Z$,” satisfying three constraints: (1) $P$ is *complete*: any two distinct candidates are ranked (for all candidates $Y$ and $Z$, if $Y\ne Z$, then either $Y\mathrel{P} Z$ or $Z\mathrel{P} Y$); (2) $P$ is *transitive*: if a candidate $Y$ is ranked above a candidate $W$ and $W$ is ranked above a candidate $Z$, then $Y$ is ranked above $Z$ (for all candidates $Y, Z$, and $W$, if $Y\mathrel{P} W$ and $W\mathrel{P} Z$, then $Y\mathrel{P} Z$); and (3) $P$ is *irreflexive*: no candidate is ranked above itself (there is no candidate $Y$ such that $Y\mathrel{P} Y$). For example, suppose that there are three candidates $X =\{A, B, C\}$. Then, the six possible rankings of $X$ are listed in the following table:

| # Voters | Ranking |
| --- | --- |
| $n_1$ | $A\s B\s C$ |
| $n_2$ | $A\s C\s B$ |
| $n_3$ | $B\s A\s C$ |
| $n_4$ | $B\s C\s A$ |
| $n_5$ | $C\s A\s B$ |
| $n_6$ | $C\s B\s A$ |

I can now be more precise about the definition of a Condorcet winner (loser). Given a ranking from each voter, the **majority relation** orders the candidates in terms of how they perform in one-on-one elections. More precisely, for candidates $Y$ and $Z$, write $Y \mathrel{>_M} Z$, provided that more voters rank candidate $Y$ above candidate $Z$ than the other way around. So, if the distribution of rankings is given in the above table, we have:

$$\begin{align} A\mathrel{>_M} B\ &\text{ just in case } n_1 + n_2 + n_5 > n_3 + n_4 + n_6 \\ A\mathrel{>_M} C\ &\text{ just in case } n_1 + n_2 + n_3 > n_4 + n_5 + n_6 \\ B \mathrel{>_M} C\ &\text{ just in case } n_1 + n_3 + n_4 > n_2 + n_5 + n_6 \end{align}$$

A candidate $Y$ is called the **Condorcet winner** in an election scenario if $Y$ is the maximum of the majority ordering $>_M$ for that election scenario (that is, $Y$ is the Condorcet winner if $Y\mathrel{>_M} Z$ for all other candidates $Z$). The **Condorcet loser** is the candidate that is the minimum of the majority ordering.

Rankings are one type of ballot. In this article, we will see examples of other types of ballots, such as selecting a single candidate, selecting a subset of candidates or assigning grades to candidates. Given a set of ballots $\mathcal{B}$, a **profile** for a set of voters specifies the ballot selected by each voter. Formally, a profile for set of voters $V=\{1,\ldots, n\}$ and a set of ballots $\mathcal{B}$ is a sequence $\bb=(b_1,\ldots, b_n)$, where for each voter $i$, $b_i$ is the ballot from $\mathcal{B}$ submitted by voter $i$.

A **voting method** is a function that assigns to each possible profile a *group decision*. The group decision may be a single candidate (the winning candidate), a set of candidates (when ties are allowed), or an ordering of the candidates (possibly allowing ties). Note that since a profile identifies the voter associated with each ballot, a voting method may take this information into account. This means that voting methods can be designed that select a winner (or winners) based only on the ballots of some subset of voters while ignoring all the other voters’ ballots. An extreme example of this is the so-called Arrovian dictatorship for voter $d$ that assigns to each profile the candidate ranked first by $d$. A natural way to rule out these types of voting methods is to require that a voting method is **anonymous**: the group decision should depend only on the number of voters that chose each ballot. This means that if two profiles are permutations of each other, then a voting method that is anonymous must assign the same group decision to both profiles. When studying voting methods that are anonymous, it is convenient to assume the inputs are **anonymized profiles**. An anonymous profile for a set of ballots $\mathcal{B}$ is a function from $\mathcal{B}$ to the set of integers $\mathbb{N}$. The election scenario discussed in the previous section is an example of an anonymized profile (assuming that each ranking not displayed in the table is assigned the number 0). In the remainder of this article (unless otherwise specified), I will restrict attention to anonymized profiles.

I conclude this section with a few comments on the relationship between the ballots in a profile and the voters’ opinions about the candidates. Two issues are important to keep in mind. First, the ballots used by a voting method are intended to reflect *some* aspect of the voters’ opinions about the candidates. Voters may choose a ballot that best expresses their personal preference about the set of candidates or their judgements about the relative strengths of the candidates. A common assumption in the voting theory literature is that a ranking of the set of candidates expresses a voter’s *ordinal* preference ordering over the set of candidates (see the entry on preferences, Hansson and Grüne-Yanoff 2009, for an extended discussion of issues surrounding the formal modeling of preferences)[^hansson-2009]. Other types of ballots represent information that cannot be inferred directly from a voter’s *ordinal* preference ordering, for example, by describing the *intensity* of a preference for a particular candidate (see Section 2.3). Second, it is important to be precise about the type of considerations voters take into account when selecting a ballot. One approach is to assume that voters choose *sincerely* by selecting the ballot that best reflects their opinion about the different candidates. A second approach assumes that the voters choose *strategically*. In this case, a voter selects a ballot that she *expects* to lead to her most desired outcome given the information she has about how the other members of the group will vote. Strategic voting is an important topic in voting theory and social choice theory (see Taylor 2005 and Section 3.3 of List 2013 for a discussion and pointers to the literature)[^list-2013][^list-2013-2][^taylor-2005], but in this article, unless otherwise stated, I assume that voters choose sincerely (cf. Section 4.1).

## 2. Examples of Voting Methods

A quick survey of elections held in different democratic societies throughout the world reveals a wide variety of voting methods. In this section, I discuss some of the key methods that have been analyzed in the voting theory literature. These methods may be of interest because they are widely used (e.g., Plurality Rule or Plurality Rule with Runoff) or because they are of theoretical interest (e.g., Dodgson’s method).

I start with the most widely used method:

**Plurality Rule**: Each voter selects one candidate (or none if voters can abstain), and the candidate(s) with the most votes win.

Plurality rule (also called **First Past the Post**) is a very simple method that is widely used despite its many problems. The most pervasive problem is the fact that plurality rule can elect a Condorcet loser. Borda (1784) observed this phenomenon in the 18th century (see also the example from Section 1).

| # Voters | Ranking |
| --- | --- |
| 1 | $A\s B\s C$ |
| 7 | $A\s C\s B$ |
| 7 | $B\s C\s A$ |
| 6 | $C\s B\s A$ |

Candidate $A$ is the Condorcet loser (both $B$ and $C$ beat candidate $A$, 13 – 8); however, $A$ is the plurality rule winner (assuming the voters vote for the candidate that they rank first). In fact, the plurality ranking ($A$ is first with 8 votes, $B$ is second with 7 votes and $C$ is third with 6 votes) reverses the majority ordering $C\mathrel{>_M} B\mathrel{>_M} A$. See Laslier 2012 for further criticisms of Plurality Rule and comparisons with other voting methods discussed in this article. One response to the above phenomenon is to require that candidates pass a certain threshold to be declared the winner.

**Quota Rule**: Suppose that $q$, called the **quota**, is any number between 0 and 1. Each voter selects one candidate (or none if voters can abstain), and the winners are the candidates that receive at least $q \times \# V$ votes, where $\# V$ is the number of voters. **Majority Rule** is a quota rule with $q=0.5$ (a candidate is the **strict** or **absolute** majority winner if that candidate receives strictly more than $0.5 \times \# V$ votes). **Unanimity Rule** is a quota rule with $q=1$.

An important problem with quota rules is that they do not identify a winner in every election scenario. For instance, in the above election scenario, there are no majority winners since none of the candidates are ranked first by more than 50% of the voters.

A criticism of both plurality and quota rules is that they severely limit what voters can express about their opinions of the candidates. In the remainder of this section, I discuss voting methods that use ballots that are more expressive than simply selecting a single candidate. Section 2.1 discusses voting methods that require voters to rank the alternatives. Section 2.2 discusses voting methods that require voters to assign grades to the alternatives (from some fixed set of grades). Finally, Section 2.3 discusses two voting methods in which the voters may have different levels of influence on the group decision. In this article, I focus on voting methods that either are familiar or help illustrate important ideas. Consult Brams and Fishburn 2002, Felsenthal 2012, and Nurmi 1987 for discussions of voting methods not covered in this article.

### 2.1 Ranking Methods: Scoring Rules and Multi-Stage Methods

The voting methods discussed in this section require the voters to **rank** the candidates (see section 1.1 for the definition of a ranking). Providing a ranking of the candidates is much more expressive than simply selecting a single candidate. However, ranking *all* of the candidates can be very demanding, especially when there is a large number of them, since it can be difficult for voters to make distinctions between all the candidates. The most well-known example of a voting method that uses the voters’ rankings is Borda Count:

**Borda Count**: Each voter provides a ranking of the candidates. Then, a score (the Borda score) is assigned to each candidate by a voter as follows: If there are $n$ candidates, give $n-1$ points to the candidate ranked first, $n-2$ points to the candidate ranked second,…, 1 point to the candidate ranked second to last and 0 points to candidate ranked last. So, the Borda score of candidate $A$, denoted $\BS(A)$, is calculated as follows (where $\#U$ denotes the number elements in the set $U)$: $$\begin{align} \BS(A) =\ &(n-1)\times \# \{i\ |\ i \text{ ranks \(A\) first}\}\\ &+ (n-2)\times \# \{i\ |\ i \text{ ranks \(A\) second}\} \\ &+ \cdots \\ &+ 1\times \# \{i\ |\ i \text{ ranks \(A\) second to last}\}\\ &+ 0\times \# \{i\ |\ i \text{ ranks \(A\) last}\} \end{align}$$ The candidate with the highest Borda score wins.

Recall the example discussed in the introduction to Section 1. For each alternative, the Borda scores can be calculated using the above method:

$$\begin{align} \BS(A) &= 3 \times 8 + 2 \times 0 + 1 \times 0 + 0 \times 13 = 24 \\ \BS(B) &= 3 \times 7 + 2 \times 9 + 1 \times 5 + 0 \times 0 = 44 \\ \BS(C) &= 3 \times 6 + 2 \times 5 + 1 \times 10 + 0 \times 0 = 38 \\ \BS(D) &= 3 \times 0 + 2 \times 7 + 1 \times 6 + 0 \times 8 = 20 \end{align}$$

Borda Count is an example of a **scoring rule**. A scoring rule is any method that calculates a score based on weights assigned to candidates according to where they fall in the voters’ rankings. That is, a scoring rule for $n$ candidates is defined as follows: Fix a sequence of numbers $(s_1, s_2, \ldots, s_n)$ where $s_k\ge s_{k+1}$ for all $k=1,\ldots, n-1$. For each $k$,  $s_k $ is the score assigned to a alternatives ranked in position $k$. Then, the score for alternative $A$, denoted $Score(A)$, is calculated as follows:

$$\begin{align} \textit{Score}(A)=\ &s_1\times \# \{i\ |\ i \text{ ranks \(A\) first}\}\\ &+ s_2\times \# \{i\ |\ i \text{ ranks \(A\) second}\}\\ &+ \cdots \\ &+ s_n\times \# \{i\ |\ i \text{ ranks \(A\) last}\}. \end{align}$$

Borda count for $n$ alternatives uses scores $(n-1, n-2, \ldots, 0)$ (call $\BS(X)$ the Borda score for candidate $X$). Note that Plurality Rule can be viewed as a scoring rule that assigns 1 point to the first ranked candidate and 0 points to the other candidates. So, the **plurality score** of a candidate $X$ is the number of voters that rank $X$ first. Building on this idea, **$k$-Approval Voting** is a scoring method that gives 1 point to each candidate that is ranked in position $k$ or higher, and 0 points to all other candidates. To illustrate $k$-Approval Voting, consider the following election scenario:

| # Voters | Ranking |
| --- | --- |
| 2 | $A\s D\s B\s C$ |
| 2 | $B\s D\s A\s C$ |
| 1 | $C\s A\s B\s D$ |

- The winners according to 1-Approval Voting (which is the same as Plurality Rule) are $A$ and $B.$
- The winner according 2-Approval Voting is $D.$
- The winners according to 3-Approval Voting are $A$ and $B.$

Note that the Condorcet winner is $A$, so none of the above methods *guarantee* that the Condorcet winner is elected (whether $A$ is elected using 1-Approval or 3-Approval depends on the tie-breaking mechanism that is used).

A second way to make a voting method sensitive to more than the voters’ top choice is to hold “multi-stage” elections. The idea is to successively remove candidates that perform poorly in the election until there is one candidate that is ranked first by more than 50% of the voters (i.e., there is a strict majority winner). The different stages can be actual “runoff” elections in which voters are asked to evaluate a reduced set of candidates; or they can be built in to the way the winner is calculated by asking voters to submit rankings over the set of all candidates. The first example of a multi-stage method is used to elect the French president.

**Plurality with Runoff**: Start with a plurality vote to determine the top two candidates (the candidates ranked first and second according to their plurality scores). If a candidate is ranked first by more than 50% of the voters, then that candidate is declared the winner. If there is no candidate with a strict majority of first place votes, then there is a runoff between the top two candidates (or more if there are ties). The candidate(s) with the most votes in the runoff elections is(are) declared the winner(s).

Rather than focusing on the top two candidates, one can also iteratively remove the candidate(s) with the fewest first-place votes:

**The Hare Rule**: The ballots are rankings of the candidates. If a candidate is ranked first by more than 50% of the voters, then that candidate is declared the winner. If there is no candidate with a strict majority of first place votes, repeatedly delete the candidate or candidates that receive the fewest first-place votes (i.e., the candidate(s) with the lowest plurality score(s)). The first candidate to be ranked first by strict majority of voters is declared the winner (if there is no such candidate, then the remaining candidate(s) are declared the winners).

The Hare Rule is also called **Ranked-Choice Voting**, **Alternative Vote**, and **Instant Runoff**. If there are only three candidates, then the above two voting methods are the same (removing the candidate with the lowest plurality score is the same as keeping the two candidates with highest and second-highest plurality score). The following example shows that they can select different winners when there are more than three candidates:

| # Voters | Ranking |
| --- | --- |
| 7 | $A\s B\s C\s D$ |
| 5 | $B\s C\s D\s A$ |
| 4 | $D\s B\s C\s A$ |
| 3 | $C\s D\s A\s B$ |
| Candidate $A$ is the Plurality with Runoff winner Candidate $D$ is the Hare Rule winner |   |

Candidate $A$ is the Plurality with Runoff winner: Candidates $A$ and $B$ are the top two candidates, being ranked first by 7 and 5 voters, respectively. In the runoff election (using the rankings from the above table), the groups voting for candidates $C$ and $D$ transfer their support to candidates $B$ and $A,$ respectively, with $A$ winning 10 – 9.

Candidate $D$ is the Hare Rule winner: In the first round, candidate $C$ is eliminated since she is only ranked first by 3 voters. This group’s votes are transferred to $D$, giving him 7 votes. This means that in the second round, candidate $B$ is ranked first by the fewest voters (5 voters rank $B$ first in the profile with candidate $C$ removed), and so is eliminated. After the elimination of candidate $B$, candidate $D$ has a strict majority of the first-place votes: 12 voters ranking him first (note that in this round the group in the second column transfers all their votes to $D$ since $C$ was eliminated in an earlier round).

The core idea of multi-stage methods is to successively remove candidates that perform "poorly" in an election. For the Hare Rule, performing poorly is interpreted as receiving the fewest first place votes. There are other ways to identify "poorly performing" candidates in an election scenario. For instance, the Coombs Rule successively removes candidates that are ranked last by the most voters (see Grofman and Feld 2004 for an overview of Coombs Rule)[^grofman-2004].

**Coombs Rule**: The ballots are rankings of the candidates. If a candidate is ranked first by more than 50% of the voters, then that candidate is declared the winner. If there is no candidate with a strict majority of first place votes, repeatedly delete the candidate or candidates that receive the most last-place votes. The first candidate to be ranked first by a strict majority of voters is declared the winner (if there is no such candidate, then the remaining candidate(s) are declared the winners).

In the above example, candidate $B$ wins the election using Coombs Rule. In the first round, $A$, with 9 last-place votes, is eliminated. Then, candidate $B$ receives 12 first-place votes, which is a strict majority, and so is declared the winner.

There is a technical issue that is important to keep in mind regarding the above definitions of the multi-stage voting methods. When identifying the poorly performing candidates in each round, there may be ties (i.e., there may be more than one candidate with the lowest plurality score or more than one candidate ranked last by the most voters). In the above definitions, I assume that all of the poorly performing candidates will be removed in each round. An alternative approach would use a tie-breaking rule to select one of the poorly performing candidates to be removed at each round.

### 2.2 Voting by Grading

The voting methods discussed in this section can be viewed as generalizations of scoring methods, such as Borda Count. In a scoring method, a voter’s ranking is an assignment of *grades* (e.g., "1st place", "2nd place", "3rd place", ... , "last place") to the candidates. Requiring voters to rank all the candidates means that (1) every candidate is assigned a grade, (2) there are the same number of possible grades as the number of candidates, and (3) different candidates must be assigned different grades. In this section, we drop assumptions (2) and (3), assuming a fixed number of grades for every set of candidates and allowing different candidates to be assigned the same grade.

The first example gives voters the option to either select a candidate that they want to vote *for* (as in plurality rule) or to select a candidate that they want to vote *against*.

**Negative Voting**: Each voter is allowed to choose one candidate to either vote *for* (giving the candidate one point) or to vote *against* (giving the candidate –1 points). The winner(s) is(are) the candidate(s) with the highest total number of points (i.e., the candidate with the greatest score, where the score is the total number of positive votes minus the total number of negative votes).

Negative voting is tantamount to allowing the voters to support either a single candidate or all but one candidate (taking a point away from a candidate $C$ is equivalent to giving one point to all candidates except $C$). That is, the voters are asked to choose a set of candidates that they support, where the choice is between sets consisting of a single candidate or sets consisting of all except one candidate. The next voting method generalizes this idea by allowing voters to choose *any* subset of candidates:

**Approval Voting**: Each voter selects a *subset* of the candidates (where the empty set means the voter abstains) and the candidate(s) with selected by the most voters wins.

If a candidate $X$ is in the set of candidates selected by a voter, we say that the voter approves of candidate $X$. Then, the approval winner is the candidate with the most approvals. Approval voting has been extensively discussed by Steven Brams and Peter Fishburn (Brams and Fishburn 2007; Brams 2008)[^brams-2008][^brams-2007]. See, also, the recent collection of articles devoted to approval voting (Laslier and Sanver 2010)[^laslier-2010][^laslier-2010-2].

Approval voting forces voters to think about the decision problem differently: They are asked to determine which candidates they *approve* of rather than selecting a single candidate to voter *for* or determining the relative ranking of the candidates. That is, the voters are asked which candidates are above a certain “threshold of acceptance”. Ranking a set of candidates and selecting the candidates that are approved are two different aspects of a voters overall opinion about the candidates. They are related but cannot be derived from each other. See Brams and Sanver 2009, for examples of voting methods that ask voters to both select a set of candidates that they approve *and* to (linearly) rank the candidates.

Approval voting is a very flexible method. Recall the election scenario illustrating the $k$-Approval Voting methods:

| # Voters | Ranking |
| --- | --- |
| 2 | $\underline{A}\s D\s B\s C$ |
| 2 | $\underline{B}\s D\s A\s C$ |
| 1 | $\underline{C}\s \underline{A}\s B\s D$ |

In this election scenario, $k$-Approval for $k=1,2,3$ cannot guarantee that the Condorcet winner $A$ is elected. The Approval ballot $(\{A\},\{B\}, \{A, C\})$ does elect the Condorcet winner. In fact, Brams (2008, Chapter 2) proves that if there is a unique Condorcet winner, then that candidate may be elected under approval voting (assuming that all voters vote *sincerely*: see Brams 2008, Chapter 2, for a discussion)[^brams-2008]. Note that approval voting may also elect other candidates (perhaps even the Condorcet loser). Whether this flexibility of Approval Voting should be seen as a virtue or a vice is debated in Brams, Fishburn and Merrill 1988a, 1988b and Saari and van Newenhizen 1988a, 1988b.

Approval Voting asks voters to express something about their *intensity* of preference for the candidates by assigning one of two grades: "Approve" or "Don’t Approve". Expanding on this idea, some voting methods assume that there is a fixed set of grades, or a *grading language*, that voters can assign to each candidate. See Chapters 7 and 8 from Balinksi and Laraki 2010 for examples and a discussion of grading languages (cf. Morreau 2016)[^morreau-2016].

There are different ways to determine the winner(s) given a profile of ballots that assign grades to each candidate. The main approach is to calculate a "group" grade for each candidate, then select the candidate with the best overall group grade. In order to calculate a group grade for each candidate, it is convenient to use numbers for the grading language. Then, there are two natural ways to determine the group grade for a candidate: calculating the mean, or average, of the grades or calculating the median of the grades.

**Cumulative Voting**: Each voter is asked to distribute a fixed number of points, say ten, among the candidates in any way they please. The candidate(s) with the most total points wins the election.

**Score Voting (also called Range Voting)**: The grades are a finite set of numbers. The ballots are an assignment of grades to the candidates. The candidate(s) with the largest average grade is declared the winner(s).

Cumulative Voting and Score Voting are similar. The important difference is that Cumulative Voting requires that the sum of the grades assigned to the candidates by each voter is the same. The next procedure, proposed by Balinski and Laraki 2010 (cf. Bassett and Persky 1999 and [the discussion of this method](http://rangevoting.org/MedianVrange.html) at rangevoting.org), selects the candidate(s) with the largest *median* grade rather than the largest mean grade.

**Majority Judgement**: The grades are a finite set of numbers (cf. discussion of common grading languages). The ballots are an assignment of grades to the candidates. The candidate(s) with the largest median grade is(are) declared the winner(s). See Balinski and Laraki 2007 and 2010 for further refinements of this voting method that use different methods for breaking ties when there are multiple candidates with the largest median grade.

I conclude this section with an example that illustrates Score Voting and Majority Judgement. Suppose that there are 3 candidates $\{A, B, C\}$, 5 grades $\{0,1,2,3,4\}$ (with the assumption that the larger the number, the higher the grade), and 5 voters. The table below describes an election scenario. The candidates are listed in the first row. Each row describes an assignment of grades to a candidate by a set of voters.

|   | Grade (0–4) for: |   |   |
| --- | --- | --- | --- |
| # Voters | $A$ | $B$ | $C$ |
| 1 | 4 | 3 | 1 |
| 1 | 4 | 3 | 2 |
| 1 | 2 | 0 | 3 |
| 1 | 2 | 3 | 4 |
| 1 | 1 | 0 | 2 |
| Mean: | 2.6 | 1.8 | 2.4 |
| Median: | 2 | 3 | 2 |

The bottom two rows give the mean and median grade for each candidate. Candidate $A$ is the score voting winner with the greatest mean grade, and candidate $B$ is the majority judgement winner with the greatest median grade.

There are two types of debates about the voting methods introduced in this section. The first concerns the choice of the *grading language* that voters use to evaluate the candidates. Consult Balinski and Laraki 2010 amd Morreau 2016 for an extensive discussion of the types of considerations that influence the choice of a grading language. Brams and Potthoff 2015 argue that two grades, as in Approval Voting, is best to avoid certain paradoxical outcomes. To illustrate, note that, in the above example, if the candidates are ranked by the voters according to the grades that are assigned, then candidate $C$ is the Condorcet winner (since 3 voters assign higher grades to $C$ than to $A$ or $B$). However, neither Score Voting nor Majority Judgement selects candidate $C$.

The second type of debate concerns the method used to calculate the group grade for each candidate (i.e., whether to use the mean as in Score Voting or the median as in Majority Judgement). One important issue is whether voters have an incentive to misrepresent their evaluations of the candidates. Consider the voter in the middle column that assigns the grade of 2 to $A$, 0 to $B$, and 3 to $C$. Suppose that these grades represents the voter’s true evaluations of the candidates. If this voter increases the grade for $C$ to 4 and decreases the grade for $A$ to 1 (and the other voters do not change their grades), then the average grade for $A$ becomes 2.4 and the average grade for $C$ becomes 2.6, which better reflects the voter’s true evaluations of the candidates (and results in $C$ being elected according to Score Voting). Thus, this voter has an incentive to misrepresent her grades. Note that the median grades for the candidates do not change after this voter changes her grades. Indeed, Balinski and Laraki 2010, chapter 10, argue that using the median to assign group grades to candidates encourages voters to submit grades that reflect their true evaluations of the candidates. The key idea of their argument is as follows: If a voter’s true grade matches the median grade for a candidate, then the voter does not have an incentive to assign a different grade. If a voter’s true grade is greater than the median grade for a candidate, then raising the grade will not change the candidate’s grade and lowering the voter’s grade may result in the candidate receiving a grade that is lowering than the voter’s true evaluation. Similarly, if a voter’s true grade is lower than the median grade for a candidate, then lowering the grade will not change the candidate’s grade and raising the voter’s grade may result in the candidate receiving a grade that is higher than the voter’s true evaluation. Thus, if voters are focused on ensuring that the group grades for the candidates best reflects their true evaluations of the candidates, then voters do not have an incentive to misrepresent their grades. However, as pointed out in Felsenthal and Machover 2008 (Example 3.3), voters can manipulate the outcome of an election using Majority Judgement to ensure a preferred candidate is elected (cf. the discussion of strategic voting in Section 4.1 and Section 3.3 of List 2013)[^list-2013][^list-2013-2]. Suppose that the voter in the middle column assigns the grade of 4 to candidate $A$, 0 to candidate $B$ and 3 to candidate $C$. Assuming the other voters do not change their grades, the majority judgement winner is now $A$, which the voter ranks higher than the original majority judgement winner $B.$ Consult Balinski and Laraki 2010, 2014 and Edelman 2012b for arguments in favor of electing candidates with the greatest median grade; and Felsenthal and Machover 2008, Gehrlein and Lepelley 2003, and Laslier 2011 for arguments against electing candidates with the greatest median grade.

### 2.3 Quadratic Voting and Liquid Democracy

In this section, I briefly discuss two new approaches to voting that do not fit nicely into the categories of voting methods introduced in the previous sections. While both of these methods can be used to select representatives, such as a president, the primary application is a group of people voting directly on propositions, or referendums.

**Quadratic Voting**: When more than 50% of the voters support an alternative, most voting methods will select that alternative. Indeed, when there are only two alternatives, such as when voting for or against a proposition, there are many arguments that identify majority rule as the best and most stable group decision method (May 1952; Maskin 1995)[^maskin-1995][^may-1952]. One well-known problem with always selecting the majority winner is the so-called *tyranny of the majority*. A complete discussion of this issue is beyond the scope of this article. The main problem from the point of view of the analysis of voting methods is that there may be situations in which a majority of the voters weakly support a proposition while there is a sizable minority of voters that have a strong preference against the proposition.

One way of dealing with this problem is to increase the quota required to accept a proposition. However, this gives too much power to a small group of voters. For instance, with Unanimity Rule a single voter can block a proposal from being accepted. Arguably, a better solution is to use ballots that allow voters to express something about their intensity of preference for the alternatives. Setting aside issues about interpersonal comparisons of utility (see, for instance, Hausman 1995)[^hausman-1995], this is the benefit of using the voting methods discussed in Section 2.2, such as Score Voting or Majority Judgement. These voting methods assume that there is a fixed set of *grades* that the voters use to express their intensity of preference. One challenge is finding an appropriate set of grades for a population of voters. Too few grades makes it harder for a sizable minority with strong preferences to override the majority opinion, but too many grades makes it easy for a vocal minority to overrule the majority opinion.

Using ideas from mechanism design (Groves and Ledyard 1977; Hylland and Zeckhauser 1980)[^groves-1977][^hylland-1980], the economist E. Glen Weyl developed a voting method called Quadratic Voting that mitigates some of the above issues (Lalley and Weyl 2018a)[^lalley-2018a]. The idea is to think of an election as a market (Posner and Weyl, 2018, Chapter 2). Each voter can purchase votes at a costs that is quadratic in the number of votes. For instance, a voter must pay $25 for 5 votes (either in favor or against a proposition). After the election, the money collected is distributed on a *pro rata* basis to the voters. There are a variety of economic arguments that justify why voters should pay $v^2$ to purchase $v$ votes (Lalley and Weyl 2018b; Goeree and Zhang 2017)[^goeree-2017][^zhang-2017]. See Posner and Weyl 2015 and 2017 for further discussion and a vigorous defense of the use of Quadratic Voting in national elections. Consult Laurence and Sher 2017 for two arguments against the use of Quadratic Voting. Both arguments are derived from the presence of wealth inequality. The first argument is that it is ambiguous whether the Quadratic Voting decision really outperforms a decision using majority rule from the perspective of utilitarianism (see Driver 2014 and Sinnott-Armstrong 2019 for overviews of utilitarianism)[^driver-2014][^sinnott-armstrong-2019]. The second argument is that any vote-buying mechanism will have a hard time meeting a legitimacy requirement, familiar from the theory of democratic institutions (cf. Fabienne 2017).

**Liquid Democracy**: Using Quadratic Voting, the voters’ opinions may end up being weighted differently: Voters that purchase more of a voice have more influence over the election. There are other reasons why some voters’ opinions may have more weight than others when making a decision about some issue. For instance, a voter may have been elected to represent a constituency, or a voter may be recognized as an expert on the issue under consideration. An alternative approach to group decision making is *direct democracy* in which every citizen is asked to vote on every political issue. Asking the citizens to vote on *every* issue faces a number of challenges, nicely explained by Green-Armytage (2015, pg. 191):

> Direct democracy without any option for representation is problematic. Even if it were possible for every citizen to learn everything they could possibly know about every political issue, people who did this would be able to do little else, and massive amounts of time would be wasted in duplicated effort. Or, if every citizen voted but most people did not take the time to learn about the issues, the results would be highly random and/or highly sensitive to overly simplistic public relations campaigns. Or, if only a few citizens voted, particular demographic and ideological groups would likely be under-represented

One way to deal with some of the problems raised in the above quote is to use *proxy voting*, in which voters can delegate their vote on some issues (Miller 1969)[^miller-1969]. Liquid Democracy is a form of proxy voting in which voters can delegate their votes to other voters (ideally, to voters that are well-informed about the issue under consideration). What distinguishes Liquid Democracy from proxy voting is that proxies may further delegate the votes entrusted to them. For example, suppose that there is a vote to accept or reject a proposition. Each voter is given the option to delegate their vote to another voter, called a proxy. The proxies, in turn, are given the option to delegate their votes to yet another voter. The voters that decide to not transfer their votes cast a vote weighted by the number of voters who entrusted them as a proxy, either directly or indirectly.

While there has been some discussion of proxy voting in the political science literature (Miller 1969; Alger 2006; Green-Armytage 2015)[^alger-2006][^green-armytage-2015][^miller-1969], most studies of Liquid Democracy can be found in the computer science literature. A notable exception is Blum and Zuber 2016 that justifies Liquid Democracy, understood as a procedure for democratic decision-making, within normative democratic theory. An overview of the origins of Liquid Democracy and pointers to other online discussions can be found in Behrens 2017. Formal studies of Liquid Democracy have focused on: the possibility of delegation cycles and the relationship with the theory of judgement aggregation (Christoff and Grossi 2017)[^christoff-2017]; the rationality of delegating votes (Bloembergen, Grossi and Lackner 2018); the potential problems that arise when many voters delegate votes to only a few voters (Kang et al. 2018; Golz et al. 2018)[^golz-2018][^kang-2018]; and generalizations of Liquid Democracy beyond binary choices (Brill and Talmon 2018; Zhang and Zhou 2017)[^brill-2018][^zhang-2017].

### 2.4 Criteria for Comparing Voting Methods

This section introduced different methods for making a group decision. One striking fact about the voting methods discussed in this section is that they can identify different winners given the same collection of ballots. This raises an important question: How should we *compare* the different voting methods? Can we argue that some voting methods are better than others? There are a number of different criteria that can be used to compare and contrast different voting methods:

1. **Pragmatic concerns**: Is the procedure easy to *use*? Is it *legal* to use a particular voting method for a national or local election? The importance of “ease of use” should not be underestimated: Despite its many flaws, plurality rule (arguably the simplest voting procedure to use and understand) is, by far, the most commonly used method (cf. the discussion by Levin and Nalebuff 1995, p. 19)[^levin-1995]. Furthermore, there are a variety of consideration that go into selecting an appropriate voting method for an institution (Edelman 2012a)[^edelman-2012a].
2. **Behavioral considerations**: Do the different procedures *really* lead to different outcomes in practice? An interesting strand of research, *behavorial social choice*, incorporates empirical data about actual elections into the general theory of voting (This is discussed briefly in Section 5. See Regenwetter *et al*. 2006, for an extensive discussion)[^regenwetter-2006].
3. **Information required from the voters**: What type of information do the ballots convey? While ranking methods (e.g., Borda Count) require the voter to compare *all* of the candidates, it is often useful to ask the voters to report something about the “intensities” of their preferences over the candidates. Of course, there is a trade-off: Limiting what voters can express about their opinions of the candidates often makes a procedure much easier to use and understand. Also related to these issues is the work of Brennan and Lomasky 1993 (among others) on *expressive voting* (cf. Wodak 2019 and Aragones et al. 2011 for analyses along these lines touching on issues raised in this article)[^aragones-2011][^wodak-2019].
4. **Axiomatic characterization results and voting paradoxes**: Much of the work in voting theory has focused on comparing and contrasting voting procedures in terms of abstract principles that they satisfy. The goal is to characterize the different voting procedures in terms of *normative* principles of group decision making. See Sections 3 and 4.2 for discussions.

## 3. Voting Paradoxes

In this section, I introduce and discuss a number of *voting paradoxes* — i.e., anomalies that highlight problems with different voting methods. Consult Saari 1995 and Nurmi 1999 for penetrating analyses that explain the underlying mathematics behind the different voting paradoxes.

### 3.1 Condorcet’s Paradox

A very common assumption is that a *rational* preference ordering must be *transitive* (i.e., if $A$ is preferred to $B$, and $B$ is preferred to $C$, then $A$ must be preferred to $C$). See the entry on preferences (Hansson and Grüne-Yanoff 2009)[^hansson-2009] for an extended discussion of the rationale behind this assumption. Indeed, if a voter’s preference ordering is not transitive, for instance, allowing for cycles (e.g., an ordering of $A, B, C$ with $A \succ B \succ C \succ A$, where $X\succ Y$ means $X$ is strictly preferred to $Y$), then there is no alternative that the voter can be said to actually support (for each alternative, there is another alternative that the voter strictly prefers). Many authors argue that voters with cyclic preference orderings have inconsistent opinions about the candidates and should be *ignored* by a voting method (in particular, Condorcet forcefully argued this point). A key observation of Condorcet (which has become known as the Condorcet Paradox) is that the majority ordering may have cycles (even when all the voters submit *rankings* of the alternatives).

Condorcet’s original example was more complicated, but the following situation with three voters and three candidates illustrates the phenomenon:

| # Voters | Ranking |
| --- | --- |
| 1 | $A\s B\s C$ |
| 1 | $B\s C\s A$ |
| 1 | $C\s A\s B$ |

Note that we have:

- Candidate $A$ beats candidate $B$ in a one-on-one election: 2 voters rank $A$ above $B$ compared to 1 voter ranking $B$ above $A$.
- Candidate $B$ beats candidate $C$ in a one-on-one election: 2 voters rank $B$ above $C$ compared to 1 voter ranking $C$ above $B$.
- Candidate $C$ beats candidate $A$ in a one-on-one election: 2 voters rank $C$ above $A$ compared to 1 voter ranking $A$ above $C$.

That is, there is a **majority cycle** $A>_M B >_M C >_M A$. This means that there is no Condorcet winner. This simple, but fundamental observation has been extensively studied (Gehrlein 2006; Schwartz 2018)[^gehrlein-2006][^schwartz-2018].

#### 3.1.1 Electing the Condorcet Winner

The Condorcet Paradox shows that there may not always be a Condorcet winner in an election. However, one natural requirement for a voting method is that if there is a Condorcet winner, then that candidate should be elected. Voting methods that satisfy this property are called **Condorcet consistent**. Many of the methods introduced above are not Condorcet consistent. I already presented an example showing that plurality rule is not Condorcet consistent (in fact, plurality rule may even elect the Condorcet *loser*).

The example from Section 1 shows that Borda Count is not Condorcet consistent. In fact, this is an instance of a general phenomenon that Fishburn (1974) called **Condorcet’s other paradox**. Consider the following voting situation with 81 voters and three candidates from Condorcet 1785.

| # Voters | Ranking |
| --- | --- |
| 30 | $A\s B\s C$ |
| 1 | $A\s C\s B$ |
| 29 | $B\s A\s C$ |
| 10 | $B\s C\s A$ |
| 10 | $C\s A\s B$ |
| 1 | $C\s B\s A$ |

The majority ordering is $A >_M B >_M C$, so $A$ is the Condorcet winner. Using the Borda rule, we have:

$$\begin{align} \BS(A) &= 2\times 31 + 1 \times 39 + 0 \times 11 = 101 \\ \BS(B) &= 2 \times 39 + 1 \times 31 + 0 \times 11 = 109 \\ \BS(C) &= 2 \times 11 + 1 \times 11 + 0 \times 59 = 33 \end{align}$$

So, candidate $B$ is the Borda winner. Condorcet pointed out something more: The only way to elect candidate $A$ using *any* scoring method is to assign more points to candidates ranked second than to candidates ranked first. Recall that a scoring method for 3 candidates fixes weights $s_1\ge s_2\ge s_3$, where $s_1$ points are assigned to candidates ranked 1st, $s_2$ points are assigned to candidates ranked 2nd, and $s_3$ points are assigned to candidates ranked last. To simplify the calculation, assume that candidates ranked last receive 0 points (i.e., $s_3=0$). Then, the scores assigned to candidates $A$ and $B$ are:

$$\begin{align} Score(A) &= s_1 \times 31 + s_2 \times 39 + 0 \times 11 \\ Score(B) &= s_1 \times 39 + s_2 \times 31 + 0 \times 11 \end{align}$$

So, in order for $Score(A) > Score(B)$, we must have $(s_1 \times 31 + s_2 \times 39) > (s_1 \times 39 + s_2 \times 31)$, which implies that $s_2 > s_1$. But, of course, it is counterintuitive to give more points for being ranked second than for being ranked first. Peter Fishburn generalized this example as follows:

**Theorem** (Fishburn 1974)[^fishburn-1974]. For all $m\ge 3$, there is some voting situation with a Condorcet winner such that every scoring rule will have at least $m-2$ candidates with a greater score than the Condorcet winner.

So, no scoring rule is Condorcet consistent, but what about other methods? A number of voting methods were devised specifically to *guarantee* that a Condorcet winner will be elected, if one exists. The examples below give a flavor of different types of Condorcet consistent methods. (See Brams and Fishburn, 2002, and Fishburn, 1977, for more examples and a discussion of Condorcet consistent methods.)[^brams-2002][^fishburn-1977]

**Condorcet’s Rule**: Each voter submits a ranking of the candidates. If there is a Condorcet winner, then that candidate wins the election. Otherwise, all candidates tie for the win.

**Black’s Procedure**: Each voter submits a ranking of the candidates. If there is a Condorcet winner, then that candidate is the winner. Otherwise, use Borda Count to determine the winners.

**Nanson’s Method**: Each voter submits a ranking of the candidates. Calculate the Borda score for each candidate. The candidates with a Borda score below the average of the Borda scores are eliminated. The Borda scores of the candidates are re-calculated and the process continues until there is only one candidate remaining. (See Niou, 1987, for a discussion of this voting method.)[^niou-1987]

**Copeland’s Rule**: Each voter submits a ranking of the candidates. A *win-loss record* for candidate $B$ is calculated as follows:

$$ WL(B) = \#\{C\ \mid\ B >_M C\} - \#\{C\ \mid\ C >_M B\} $$

The Copeland winner is the candidate that maximizes the win-loss record.

**Schwartz’s Set Method**: Each voter submits a ranking of the candidates. The winners are the smallest set of candidates that are not beaten in a one-on-one election by any candidate outside the set (Schwartz 1986)[^schwartz-1986].

**Dodgson’s Method**: Each voter submits a ranking of the candidates. For each candidate, determine the fewest number of pairwise swaps in the voters’ rankings needed to make that candidate the Condorcet winner. The candidate(s) with the fewest swaps is(are) declared the winner(s).

The last method was proposed by Charles Dodgson (better known by the pseudonym Lewis Carroll). Interestingly, this is an example of a procedure in which it is computationally difficult to compute the winner (that is, the problem of calculating the winner is NP-complete). See Bartholdi *et al*. 1989 for a discussion.

These voting methods (and the other Condorcet consistent methods) guarantee that a Condorcet winner, if one exists, will be elected. But, *should* a Condorcet winner be elected? Many people argue that there is something amiss with a voting method that does not always elect a Condorcet winner (if one exists). The idea is that a Condorcet winner best reflects the *overall group opinion* and is stable in the sense that it will defeat any challenger in a one-on-one contest using Majority Rule. The most persuasive argument that the Condorcet winner should not always be elected comes from the work of Donald Saari (1995, 2001). Consider again Condorcet’s example of 81 voters.

| # Voters | Ranking |
| --- | --- |
| 30 | $A\s B\s C$ |
| 1 | $A\s C\s B$ |
| 29 | $B\s A\s C$ |
| 10 | $B\s C\s A$ |
| 10 | $C\s A\s B$ |
| 1 | $C\s B\s A$ |

This is another example that shows that Borda’s method need not elect the Condorcet winner. The majority ordering is

$$ A >_M B >_M C, $$

while the ranking given by the Borda score is

$$ B >_{\Borda} A >_{\Borda} C. $$

However, there is an argument that candidate $B$ is the best choice for this electorate. Saari’s central observation is to note that the 81 voters can be divided into three groups:

|   | # Voters | Ranking |
| --- | --- | --- |
|   | 10 | $A\s B\s C$ |
| Group 1 | 10 | $B\s C\s A$ |
|   | 10 | $C\s A\s B$ |
|   | 1 | $A\s C\s B$ |
| Group 2 | 1 | $C\s B\s A$ |
|   | 1 | $B\s A\s C$ |
| Group 3 | 20 | $A\s B\s C$ |
| 28 | $B\s A\s C$ |   |

Groups 1 and 2 constitute majority cycles with the voters evenly distributed among the three possible rankings. Such profiles are called **Condorcet components**. These profiles form a perfect symmetry among the rankings. So, within each of these groups, it is natural to assume that the voters’ opinions cancel each other out; therefore, the decision should depend only on the voters in group 3. In group 3, candidate $B$ is the clear winner.

Balinski and Laraki (2010, pgs. 74–83) have an interesting spin on Saari’s argument. Let $V$ be a ranking voting method (i.e., a voting method that requires voters to rank the alternatives). Say that $V$ **cancels properly** if for all profiles $\bR$, if $V$ selects $A$ as a winner in $\bP$, then $V$ selects $A$ as a winner in any profile $\bP+\bC$, where $\bC$ is a Condorcet component and $\bP+\bC$ is the profile that contains all the rankings from $\bP$ and $\bC$. Balinski and Laraki (2010, pg. 77) prove that there is no Condorcet consistent voting method that cancels properly. (See the discussion of the multiple districts paradox in Section 3.3 for a proof of a closely related result.)

### 3.2 Failures of Monotonicity

A voting method is **monotonic** provided that receiving more support from the voters is always better for a candidate. There are different ways to make this idea precise (see Fishburn, 1982, Sanver and Zwicker, 2012, and Felsenthal and Tideman, 2013)[^felsenthal-2013][^fishburn-1982][^sanver-2012]. For instance, moving up in the rankings should not adversely affect a candidate’s chances to win an election. It is easy to see that Plurality Rule is monotonic in this sense: The more voters that rank a candidate first, the better chance the candidate has to win. Surprisingly, there are voting methods that do not satisfy this natural property. The most well-known example is Plurality with Runoff. Consider the two scenarios below. Note that the only difference between the them is the ranking of the fourth group of voters. This group of two voters ranks $B$ above $A$ above $C$ in scenario 1 and swaps $B$ and $A$ in scenario 2 (so, $A$ is now their top-ranked candidate; $B$ is ranked second; and $C$ is still ranked third).

| # Voters | *Scenario 1* Ranking | *Scenario 2* Ranking |
| --- | --- | --- |
| 6 | $A\s B\s C$ | $A\s B\s C$ |
| 5 | $C\s A\s B$ | $C\s A\s B$ |
| 4 | $B\s C\s A$ | $B\s C\s A$ |
| 2 | $\bB\s \bA\s C$ | $\bA\s \bB\s C$ |
| *Scenario 1*: Candidate $A$ is the Plurality with Runoff winner |   |   |
| *Scenario 2*: Candidate $C$ is the Plurality with Runoff winner |   |   |

In scenario 1, candidates $A$ and $B$ both have a plurality score of 6 while candidate $C$ has a plurality score of 5. So, $A$ and $B$ move on to the runoff election. Assuming the voters do not change their rankings, the 5 voters that rank $C$ transfer their support to candidate $A$, giving her a total of 11 to win the runoff election. However, in scenario 2, even after moving up in the rankings of the fourth group ($A$ is now ranked first by this group), candidate $A$ does *not* win this election. In fact, by trying to give more support to the winner of the election in scenario 1, rather than solidifying $A$’s win, the last group’s least-preferred candidate ended up winning the election! The problem arises because in scenario 2, candidates $A$ and $B$ are swapped in the last group’s ranking. This means that $A$’s plurality score increases by 2 and $B$’s plurality score decreases by 2. As a consequence, $A$ and $C$ move on to the runoff election rather than $A$ and $B$. Candidate $C$ wins the runoff election with 9 voters that rank $C$ above $A$ compared to 8 voters that rank $A$ above $C$.

The above example is surprising since it shows that, when using Plurality with Runoff, it may not always be beneficial for a candidate to move up in some of the voter’s rankings. The other voting methods that violate monotonicity include Coombs Rule, Hare Rule, Dodgson’s Method and Nanson’s Method. See Felsenthal and Nurmi 2017 for further discussion of voting methods that are not monotonic.

### 3.3 Variable Population Paradoxes

In this section, I discuss two related paradoxes that involve changes to the population of voters.

**No-Show Paradox**: One way that a candidate may receive “more support” is to have more voters show up to an election that support them. Voting methods that do not satisfy this version of monotonicity are said to be susceptible to the **no-show paradox** (Fishburn and Brams 1983)[^fishburn-1983]. Suppose that there are 3 candidates and 11 voters with the following rankings:

| # Voters | Ranking |
| --- | --- |
| 4 | $A\s B\s C$ |
| 3 | $B\s C\s A$ |
| 1 | $C\s A\s B$ |
| 3 | $C\s B\s A$ |
| Candidate $C$ is the Plurality with Runoff winner |   |

In the first round, candidates $A$ and $C$ are both ranked first by 4 voters while $B$ is ranked first by only 3 voters. So, $A$ and $C$ move to the runoff round. In this round, the voters in the second column transfer their votes to candidate $C$, so candidate $C$ is the winner beating $A$ 7-4. Suppose that 2 voters in the first group do not show up to the election:

| # Voters | Ranking |
| --- | --- |
| $\mathbf{2}$ | $A\s B\s C$ |
| 3 | $B\s C\s A$ |
| 1 | $C\s A\s B$ |
| 3 | $C\s B\s A$ |
| Candidate $B$ is the Plurality with Runoff winner |   |

In this election, candidate $A$ has the lowest plurality score in the first round, so candidates $B$ and $C$ move to the runoff round. The first group’s votes are transferred to $B$, so $B$ is the winner beating $C$ 5-4. Since the 2 voters that did not show up to this election rank $B$ above $C$, they prefer the outcome of the second election in which they did not participate!

Plurality with Runoff is not the only voting method that is susceptible to the no-show paradox. The Coombs Rule, Hare Rule and Majority Judgement (using the tie-breaking mechanism from Balinski and Laraki 2010)[^balinski-2010] are all susceptible to the no-show paradox. It turns out that always electing a Condorcet winner, if one exists, makes a voting method susceptible to the above failure of monotonicity.

**Theorem** (Moulin 1988)[^moulin-1988]. If there are four or more candidates, then every Condorcet consistent voting method is susceptible to the no-show paradox.

See Perez 2001, Campbell and Kelly 2002, Jimeno et al. 2009, Duddy 2014, Brandt et al. 2017, 2019, and Nunez and Sanver 2017 for further discussions and generalizations of this result.

**Multiple Districts Paradox**: Suppose that a population is divided into districts. If a candidate wins each of the districts, one would expect that candidate to win the election over the entire population of voters (assuming that the two districts divide the set of voters into disjoint sets). This is certainly true for Plurality Rule: If a candidate is ranked first by the most voters in each of the districts, then that candidate will also be ranked first by a the most voters over the entire population. Interestingly, this is not true for all voting methods (Fishburn and Brams 1983)[^fishburn-1983]. The example below illustrates the paradox for Coombs Rule.

|   | # Voters | Ranking |
| --- | --- | --- |
| District 1 | 3 | $A\s B\s C$ |
| 3 | $B\s C\s A$ |   |
| 3 | $C\s A\s B$ |   |
| 1 | $C\s B\s A$ |   |
| District 2 | 2 | $A\s B\s C$ |
| 3 | $B\s A\s C$ |   |
| District 1: Candidate $B$ is the Coombs winner |   |   |
| District 2: Candidate $B$ is the Coombs winner |   |   |

Candidate $B$ wins both districts:

**District 1**: There are a total of 10 voters in this district. None of the candidates are ranked first by 6 or more voters, so candidate $A$, who is ranked last by 4 voters (compared to 3 voters ranking each of $C$ and $B$ last), is eliminated. In the second round, candidate $B$ wins the election since 6 voters rank $B$ above $C$ and 4 voters rank $C$ above $B$.

**District 2**: There are a total of 5 voters in this district. Candidate $B$ is ranked first by a strict majority of voters, so $B$ wins the election.

Combining the two districts gives the following table:

|   | # Voters | Ranking |
| --- | --- | --- |
| Districts 1 + 2 | 5 | $A\s B\s C$ |
| 3 | $B\s C\s A$ |   |
| 3 | $C\s A\s B$ |   |
| 1 | $C\s B\s A$ |   |
| 3 | $B\s A\s C$ |   |
| Candidate $A$ is the Coombs winner |   |   |

There are 15 total voters in the combined districts. None of the candidates are ranked first by 8 or more of the voters. Candidate $C$ receives the most last-place votes, so is eliminated in the first round. In the second round, candidate $A$ is beats candidate $B$ by 1 vote (8 voters rank $A$ above $B$ and 7 voters rank $B$ above $A$), and so is declared the winner. Thus, even though $B$ wins both districts, candidate $A$ wins the election when the districts are combined.

The other voting methods that are susceptible to the multiple-districts paradox include Plurality with Runoff, The Hare Rule, and Majority Judgement. Note that these methods are also susceptible to the no-show paradox. As is the case with the no-show paradox, every Condorcet consistent voting method is susceptible to the multiple districts paradox (see Zwicker, 2016, Proposition 2.5)[^zwicker-2016]. I sketch the proof of this from Zwicker 2016 (pg. 40) since it adds to the discussion at the end of Section 3.1 about whether the Condorcet winner should be elected.

Suppose that $V$ is a voting method that always selects the Condorcet winner (if one exists) and that $V$ is not susceptible to the multiple-districts paradox. This means that if a candidate $X$ is among the winners according to $V$ in each of two districts, then $X$ must be among the winners according to $V$ in the combined districts. Consider the following two districts.

|   | # Voters | Ranking |
| --- | --- | --- |
| District 1 | 2 | $A\s B\s C$ |
| 2 | $B\s C\s A$ |   |
| 2 | $C\s A\s B$ |   |
| District 2 | 1 | $A\s B\s C$ |
| 2 | $B\s A\s C$ |   |

Note that in district 2 candidate $B$ is the Condorcet winner, so must be the only winner according to $V$. In district 1, there are no Condorcet winners. If candidate $B$ is among the winners according to $V$, then, in order to not be susceptible to the multiple districts paradox, $B$ must be among the winners in the combined districts. In fact, since $B$ is the only winner in district 2, $B$ must be the only winner in the combined districts. However, in the combined districts, candidate $A$ is the Condorcet winner, so must be the (unique) winner according to $V$. This is a contradiction, so $B$ cannot be among the winners according to $V$ in district 1. A similar argument shows that neither $A$ nor $C$ can be among the winners according to $V$ in district 1 by swapping $A$ and $B$ in the first case and $B$ with $C$ in the second case in the rankings of the voters in district 2. Since $V$ must assign at least one winner to every profile, this is a contradiction; and so, $V$ is susceptible to the multiple districts paradox.

One last comment about this paradox: It is an example of a more general phenomenon known as Simpson’s Paradox (Malinas and Bigelow 2009)[^malinas-2009]. See Saari (2001, Section 4.2) for a discussion of Simpson’s Paradox in the context of voting theory.

### 3.4 The Multiple Elections Paradox

The paradox discussed in this section, first introduced by Brams, Kilgour and Zwicker (1998), has a somewhat different structure from the paradoxes discussed above. Voters are taking part in a *referendum*, where they are asked their opinion directly about various propositions (cf. the discussion of Quadratic Voting and Liquid Democracy in Section 2.3). So, voters must select either “yes” (Y) or “no” (N) for each proposition. Suppose that there are 13 voters who cast the following votes for the three propositions (so voters can cast one of eight possible votes):

| # Voters | Propositions |
| --- | --- |
| 1 | YYY |
| 1 | YYN |
| 1 | YNY |
| 3 | YNN |
| 1 | NYY |
| 3 | NYN |
| 3 | NNY |
| 0 | NNN |

When the votes are tallied for each proposition separately, the outcome is N for each proposition (N wins 7–6 for all three propositions). Putting this information together, this means that NNN is the outcome of this election. However, there is *no support* for this outcome in this population of voters. This raises an important question about what outcome reflects the group opinion: Viewing each proposition separately, there is clear support for N on each proposition; however, there is no support for the entire package of N for all propositions. Brams et al. (1998, pg. 234) nicely summarise the issue as follows:

> The paradox does not just highlight problems of aggregation and packaging, however, but strikes at the core of social choice—both what it means and how to uncover it. In our view, the paradox shows there may be a clash between two different meanings of social choice, leaving unsettled the best way to uncover what this elusive quantity is.

See Scarsini 1998, Lacy and Niou 2000, Xia et al. 2007, and Lang and Xia 2009 for further discussion of this paradox.

A similar issue is raised by **Anscombe’s paradox** (Anscombe 1976)[^anscombe-1976], in which:

> It is possible for a majority of voters to be on the losing side of a majority of issues.

This phenomenon is illustrated by the following example with five voters voting on three different issues (the voters either vote ‘yes’ or ‘no’ on the different issues).

|   | Issue 1 | Issue 2 | Issue 3 |
| --- | --- | --- | --- |
| Voter 1 | yes | yes | no |
| Voter 2 | no | no | no |
| Voter 3 | no | yes | yes |
| Voter 4 | yes | no | yes |
| Voter 5 | yes | no | yes |
| Majority: | yes | no | yes |

However, a majority of the voters (voters 1, 2 and 3) do *not* support the majority outcome on a majority of the issues (note that voter 1 does not support the majority outcome on issues 2 and 3; voter 2 does not support the majority outcome on issues 1 and 3; and voter 3 does not support the majority outcome on issues 1 and 2)!

The issue is more interesting when the voters do not vote directly on the issues, but on candidates that take positions on the different issues. Suppose there are two candidates $A$ and $B$ who take the following positions on the three issues:

|   | Issue 1 | Issue 2 | Issue 3 |
| --- | --- | --- | --- |
| Candidate $A$ | yes | no | yes |
| Candidate $B$ | no | yes | no |

Candidate $A$ takes the majority position, agreeing with a majority of the voters on each issue, and candidate $B$ takes the opposite, minority position. Under the natural assumption that voters will vote for the candidate who agrees with their position on a majority of the issues, candidate $B$ will win the election (each of the voters 1, 2 and 3 agree with $B$ on two of the three issues, so $B$ wins the election 3–2)! This version of the paradox is known as **Ostrogorski’s Paradox** (Ostrogorski 1902). See Kelly 1989; Rae and Daudt 1976; Wagner 1983, 1984; and Saari 2001, Section 4.6, for analyses of this paradox, and Pigozzi 2005 for the relationship with the judgement aggregation literature (List 2013, Section 5)[^list-2013][^list-2013-2].

## 4. Topics in Voting Theory

### 4.1 Strategizing

In the discussion above, I have assumed that voters select ballots *sincerely*. That is, the voters are simply trying to communicate their opinions about the candidates under the constraints of the chosen voting method. However, in many contexts, it makes sense to assume that voters choose *strategically*. One need only look to recent U.S. elections to see concrete examples of strategic voting. The most often cited example is the 2000 U.S. election: Many voters who ranked third-party candidate Ralph Nader first voted for their second choice (typically Al Gore). A detailed overview of the literature on strategic voting is beyond the scope of this article (see Taylor 2005 and Section 3.3 of List 2013 for discussions and pointers to the relevant literature; also see Poundstone 2008 for an entertaining and informative discussion of the occurrence of this phenomenon in many actual elections)[^list-2013][^list-2013-2][^poundstone-2008][^taylor-2005]. I will explain the main issues, focusing on specific voting rules.

There are two general types of manipulation that can be studied in the context of voting. The first is manipulation by a moderator or outside party that has the authority to set the agenda or select the voting method that will be used. So, the outcome of an election is not manipulated from within by unhappy voters, but, rather, it is *controlled* by an outside authority figure. To illustrate this type of control, consider a population with three voters whose rankings of four candidates are given in the table below:

| # Voters | Ranking |
| --- | --- |
| 1 | $B\s D\s C\s A$ |
| 1 | $A\s B\s D\s C$ |
| 1 | $C\s A\s B\s D$ |

Note that everyone prefers candidate $B$ over candidate $D$. Nonetheless, a moderator can ask the right questions so that candidate $D$ ends up being elected. The moderator proceeds as follows: First, ask the voters if they prefer candidate $A$ or candidate $B$. Since the voters prefer $A$ to $B$ by a margin of 2 to 1, the moderator declares that candidate $B$ is no longer in the running. The moderator then asks voters to choose between candidate $A$ and candidate $C$. Candidate $C$ wins this election 2–1, so candidate $A$ is removed. Finally, in the last round the chairman asks voters to choose between candidates $C$ and $D$. Candidate $D$ wins this election 2–1 and is declared the winner.

A second type of manipulation focuses on how the voters themselves can manipulate the outcome of an election by *misrepresenting* their preferences. Consider the following two election scenarios with 7 voters and 3 candidates:

| # Voters | *Scenario 1* Ranking | *Scenario 2* Ranking |
| --- | --- | --- |
| 1 | $C\s D\s B\s A$ | $C\s D\s B\s A$ |
| 1 | $B\s A\s C\s D$ | $B\s A\s C\s D$ |
| 1 | $A\s \bC\s \bB\s \bD$ | $A\s \bB\s \bD\s \bC$ |
| 1 | $A\s C\s D\s B$ | $A\s C\s D\s B$ |
| 1 | $D\s C\s A\s B$ | $D\s C\s A\s B$ |
| *Scenario 1*: Candidate $C$ is the Borda winner ($\BS(A)=9, \BS(B)=5, \BS(C)=10$, and $\BS(D)=6$) |   |   |
| *Scenario 2*: Candidate $A$ is the Borda winner ($\BS(A)=9, \BS(B)=6, \BS(C)=8$, and $\BS(D)=7$) |   |   |

The only difference between the two election scenarios is that the third voter changed the ranking of the bottom three candidates. In election scenario 1, the third voter has candidate $A$ ranked first, then $C$ ranked second, $B$ ranked third and $D$ ranked last. In election scenario 2, this voter still has $A$ ranked first, but ranks $B$ second, $D$ third and $C$ last. In election scenario 1, candidate $C$ is the Borda Count winner (the Borda scores are $\BS(A)=9, \BS(B)=5, \BS(C)=10$, and $\BS(D)=6$). In the election scenario 2, candidate $A$ is the Borda Count winner (the Borda scores are $\BS(A)=9, \BS(B)=6, \BS(C)=8$, and $\BS(D)=7$). According to her ranking in election scenario 1, this voter prefers the outcome in election scenario 2 (candidate $A$, the Borda winner in election scenario 2, is ranked above candidate $C$, the Borda winner in election scenario 1). So, if we assume that election scenario 1 represents the “true” preferences of the electorate, it is in the interest of the third voter to misrepresent her preferences as in election scenario 2. This is an instance of a general result known as the **Gibbard-Satterthwaite Theorem** (Gibbard 1973; Satterthwaite 1975)[^gibbard-1973][^satterthwaite-1975]: Under natural assumptions, there is no voting method that *guarantees* that voters will choose their ballots sincerely (for a precise statement of this theorem see Theorem 3.1.2 from Taylor 2005 or Section 3.3 of List 2013)[^list-2013][^list-2013-2][^taylor-2005].

### 4.2 Characterization Results

Much of the literature on voting theory (and, more generally, social choice theory) is focused on so-called *axiomatic characterization results*. The main goal is to characterize different voting methods in terms of abstract principles of collective decision making. See Pauly 2008 and Endriss 2011 for interesting discussions of axiomatic characterization results from a logician’s point-of-view.

Consult List 2013 and Gaertner 2006 for introductions to the vast literature on axiomatic characterizations in social choice theory. In this article, I focus on a few key axioms and results and how they relate to the voting methods and paradoxes discussed above. I start with three core principles.

**Anonymity**: The names of the voters do not matter: If two voters swap their ballots, then the outcome of the election is unaffected.

**Neutrality**: The names of the candidates, or alternatives, do not matter: If two candidates are exchanged in every ballot, then the outcome of the election changes accordingly.

**Universal Domain**: There are no restrictions on the voter’s choice of ballots. In other words, no profile of ballots can be ignored by a voting method. One way to make this precise is to require that voting methods are *total functions* on the set of all profiles (recall that a profile is a sequence of ballots, one from each voter).

These properties ensure that the outcome of an election depends only on the voters’ ballots, with all the voters and candidates being treated equally. Other properties are intended to rule out some of the paradoxes and anomalies discussed above. In section 4.1, there is an example of a situation in which a candidate is elected, even though *all* the voters prefer a different candidate. The next principle rules out such situations:

**Unanimity** (also called the **Pareto Principle**): If candidate $A$ is ranked above candidate $B$ by *all* voters, then candidate $B$ should not win the election.

These are natural properties to impose on any voting method. A surprising consequence of these properties is that they rule out another natural property that one may want to impose: Say that a voting method is **resolute** if the method always selects one winner (i.e., there are no ties). Suppose that $V$ is a voting method that requires voters to rank the candidates and that there are at least 3 candidates and enough voters to form a Condorcet component (a profile generating a majority cycle with voters evenly distributed among the different rankings). First, consider the situation when there are exactly 3 candidates (in this case, we do not need to assume Unanimity). Divide the set of voters into three groups of size $n$ and consider the Condorcet component:

| # Voters | Ranking |
| --- | --- |
| $n$ | $A\s B\s C$ |
| $n$ | $B\s C\s A$ |
| $n$ | $C\s A\s B$ |

By Universal Domain and resoluteness, $V$ must select exactly one of $A$, $B$, or $C$ as the winner. Assume that $V$ select $A$ as the winner (the argument when $V$ selects the other candidates is similar). Now, consider the profile in which every voter swaps candidate $A$ and $B$ in their rankings:

| # Voters | Ranking |
| --- | --- |
| $n$ | $B\s A\s C$ |
| $n$ | $A\s C\s B$ |
| $n$ | $C\s B\s A$ |

By Neutrality and Universal Domain, $V$ must elect candidate $B$ in this election scenario. Now, consider the profile in which every voter in the above election scenario swaps candidates $B$ and $C$:

| # Voters | Ranking |
| --- | --- |
| $n$ | $C\s A\s B$ |
| $n$ | $A\s B\s C$ |
| $n$ | $B\s C\s A$ |

By Neutrality and Universal Domain, $V$ must elect candidate $C$ in this election scenario. Notice that this last election scenario can be generated by permuting the voters in the first election scenario (to generate the last election scenario from the first election scenario, move the first group of voters to the 2nd position, the 2nd group of voters to the 3rd position and the 3rd group of voters to the first position). But this contradicts Anonymity since this requires $V$ to elect the same candidate in the first and third election scenario. To extend this result to more than 3 candidates, consider a profile in which candidates $A$, $B$, and $C$ are all ranked above any other candidate and the restriction to these three candidates forms a Condorcet component. If $V$ satisfies Unanimity, then no candidate except $A$, $B$ or $C$ can be elected. Then, the above argument shows that $V$ cannot satisfy Resoluteness, Universal Domain, Neutrality, and Anonymity. That is, there are no Resolute voting methods that satisfy Universal Domain, Anonymity, Neutrality, and Unanimity for 3 or more candidates (note that I have assumed that the number of voters is a multiple of 3, see Moulin 1983 for the full proof)[^moulin-1983].

Section 3.2 discussed examples in which candidates end up losing an election as a result of more support from some of the voters. There are many ways to state properties that require a voting method to be *monotonic*. The following strong version (called **Positive Responsiveness** in the literature) is used to characterize majority rule when there are only two candidates:

**Positive Responsiveness**: If candidate $A$ is a winner or tied for the win and moves up in some of the voter’s rankings, then candidate $A$ is the unique winner.

I can now state our first characterization result. Note that in all of the example discussed above, it is crucial that there are three or more candidates (for example, stating Condorcet’s paradox requires there to be three or more candidates). When there are only two candidates, or alternatives, Majority Rule (choose the alternative ranked first by more than 50% of the voters) can be singled out as “best”:

**Theorem** (May 1952)[^may-1952]. A voting method for choosing between two candidates satisfies Neutrality, Anonymity, Unanimity and Positive Responsiveness if and only if the method is majority rule.

See May 1952 for a precise statement of this theorem and Asan and Sanver 2002, Maskin 1995, and Woeginger 2003 for alternative characterizations of majority rule.

A key assumption in the proof May’s theorem and subsequent results is the restriction to voting on two alternatives. When there are only two alternatives, the definition of a ballot can be simplified since a ranking of two alternatives boils down to selecting the alternative that is ranked first. The above characterizations of Majority Rule work in a more general setting since they also allow voters to *abstain* (which is ambiguous between not voting and being indifferent between the alternatives). So, if the alternatives are $\{A,B\}$, then there are three possible ballots: selecting $A$, selecting $B$, or abstaining (which is treated as selecting both $A$ and $B$). A natural question is whether there are May-style characterization theorems for more than two alternatives. A crucial issue is that rankings of more than two alternatives are much more informative than selecting an alternative or abstaining. By restricting the information required from a voter to selecting one of the alternatives or abstaining, Goodin and List 2006 prove that the axioms used in May’s Theorem characterize Plurality Rule when there are more than two alternatives. They also show that a minor modification of the axioms characterize Approval Voting when voters are allowed to select more than one alternative.

Note that focusing on voting methods that limit the information required from the voters to selecting one or more of the alternatives hides all the interesting phenomena discussed in the previous sections, such as the existence of a Condorcet paradox. Returning to the study of voting methods that require voters to rank the alternatives, the most important characterization result is Ken Arrow’s celebrated impossibility theorem (1963). Arrow showed that there is no *social welfare function* (a social welfare function maps the voters’ rankings (possibly allowing ties) to a single social ranking) satisfying universal domain, unanimity, non-dictatorship (there is no voter $d$ such that for all profiles, if $d$ ranks $A$ above $B$ in the profile, then the social ordering ranks $A$ above $B$) and the following key property:

**Independence of Irrelevant Alternatives**: The social ranking (higher, lower, or indifferent) of two candidates $A$ and $B$ depends only on the relative rankings of $A$ and $B$ for each voter.

This means that if the voters’ rankings of two candidates $A$ and $B$ are the same in two different election scenarios, then the social rankings of $A$ and $B$ must be the same. This is a very strong property that has been extensively criticized (see Gaertner, 2006, for pointers to the relevant literature, and Cato, 2014, for a discussion of generalizations of this property)[^cato-2014][^gaertner-2006]. It is beyond the scope of this article to go into detail about the proof and the ramifications of Arrow’s theorem (see Morreau, 2014, for this discussion)[^morreau-2014], but I note that many of the voting methods we have discussed do not satisfy the above property. A striking example of a voting method that does not satisfy Independence of Irrelevant Alternatives is Borda Count. Consider the following two election scenarios:

| # Voters | *Scenario 1* Ranking | *Scenario 2* Ranking |
| --- | --- | --- |
| 3 | $A\s B\s C\s \bX$ | $A\s B\s C\s \bX$ |
| 2 | $B\s C\s A\s \bX$ | $B\s C\s \bX\s A$ |
| 2 | $C\s A\s B\s \bX$ | $C\s \bX\s A\s B$ |
| *Scenario 1*: The Borda ranking is $A >_{\Borda} B >_{\Borda} C >_{\Borda} X$ ($\BS(A)=15$, $\BS(B)=14$, $\BS(C)=13$, and $\BS(X)=0$) |   |   |
| *Scenario 2*: The Borda ranking is $C >_{\Borda} B >_{\Borda} A >_{\Borda} X$ ($\BS(A)=11$, $\BS(B)=12$, $\BS(C)=13$, and $\BS(X)=6$) |   |   |

Notice that the relative rankings of candidates $A$, $B$ and $C$ are the same in both election scenarios. In the election scenario 2, the ranking of candidate $X$, that is uniformly ranked in last place in election scenario 1, is changed. The ranking according to the Borda score of the candidates in election scenario 1 puts $A$ first with 15 points, $B$ second with 14 points, $C$ third with 13 points, and $X$ last with 0 points. In election scenario 2, the ranking of $A$, $B$ and $C$ is reversed: Candidate $C$ is first with 13 voters; candidate $B$ is second with 12 points; candidate $A$ is third with 11 points; and candidate $X$ is last with 6 points. So, even though the relative rankings of candidates $A$, $B$ and $C$ do not differ in the two election scenarios, the position of candidate $X$ in the voters’ rankings reverses the Borda rankings of these candidates.

In Section 3.3, it was noted that a number of methods (including all Condorcet consistent methods) are susceptible to the multiple districts paradox. An example of a method that is not susceptible to the multiple districts paradox is Plurality Rule: If a candidate receives the most first place votes in two different districts, then that candidate must receive the most first place votes in the combined the districts. More generally, no scoring rule is susceptible to the multiple districts paradox. This property is called reinforcement:

**Reinforcement**: Suppose that $N_1$ and $N_2$ are disjoint sets of voters facing the same set of candidates. Further, suppose that $W_1$ is the set of winners for the population $N_1$, and $W_2$ is the set of winners for the population $N_2$. If there is at least one candidate that wins both elections, then the winner(s) for the entire population (including voters from both $N_1$ and $N_2$) is the set of candidates that are in both $W_1$ and $W_2$ (i.e., the winners for the entire population is $W_1\cap W_2$).

The reinforcement property explicitly rules out the multiple-districts paradox (so, candidates that win all sub-elections are guaranteed to win the full election). In order to characterize all scoring rules, one additional technical property is needed:

**Continuity**: Suppose that a group of voters $N_1$ elects a candidate $A$ and a disjoint group of voters $N_2$ elects a different candidate $B$. Then there must be some number $m$ such that the population consisting of the subgroup $N_2$ together with $m$ copies of $N_1$ will elect $A$.

We then have:

**Theorem** (Young 1975)[^young-1975]. Suppose that $V$ is a voting method that requires voters to rank the candidates. Then, $V$ satisfies Anonymity, Neutrality, Reinforcement and Continuity if and only if the method is a scoring rule.

See Merlin 2003 and Chebotarev and Smais 1998 for surveys of other characterizations of scoring rules. Additional axioms single out Borda Count among all scoring methods (Young 1974; Gardenfors 1973; Nitzan and Rubinstein 1981)[^gardenfors-1973][^nitzan-1981]. In fact, Saari has argued that “any fault or paradox admitted by Borda’s method also must be admitted by all other positional voting methods” (Saari 1989, pg. 454)[^saari-1989]. For example, it is often remarked that Borda Count (and all scoring rules) can be easily manipulated by the voters. Saari (1995, Section 5.3.1) shows that among all scores rules Borda Count is the least susceptible to manipulation (in the sense that it has the fewest profiles where a small percentage of voters can manipulate the outcome).

I have glossed over an important detail of Young’s characterization of scoring rules. Note that the reinforcement property refers to the behavior of a voting method on different populations of voters. To make this precise, the formal definition of a voting method must allow for domains that include profiles (i.e., sequences of ballots) of different lengths. To do this, it is convenient to assume that the domain of a voting method is an anonymized profile: Given a set of ballots $\mathcal{B}$, an anonymous profile is a function $\pi:\mathcal{B}\rightarrow\mathbb{N}$. Let $\Pi$ be the set of all anonymous profiles. A **variable domain voting method** assigns a non-empty set of voters to each anonymous profile—i.e., it is a function $V:\Pi\rightarrow \wp(X)-\emptyset$). Of course, this builds in the property of Anonymity into the definition of a voting method. For this reason, Young (1975) does not need to state Anonymity as a characterizing property of scoring rules.

Young’s axioms identify scoring rules out of the set of all functions defined from ballots that are rankings of candidates. In order to characterize the voting methods from Section 2.2, we need to change the set of ballots. For example, in order to characterize Approval Voting, the set of ballots $\mathcal{B}$ is the set of non-empty subsets of the set of candidates—i.e., $\mathcal{B}=\wp(X)-\emptyset$ (selecting the ballot $X$ consisting of all candidates means that the voter *abstains*). Two additional axioms are needed to characterize Approval Voting:

**Faithfulness**: If there is exactly one voter in the population, then the winners are the set of voters chosen by that voter.

**Cancellation**: If all candidates receive the same number of votes (i.e., they are elements of the same number of ballots) from the participating voters, then all candidates are winning.

We then have:

**Theorem** (Fishburn 1978b; Alos-Ferrer 2006 )[^alos-ferrer-2006][^fishburn-1978b]. A variable domain voting method where the ballots are non-empty sets of candidates is Approval Voting if and only if it satisfies Faithfulness, Cancellation, and Reinforcement.

Note that Approval Voting satisfies Neutrality even though it is not listed as one of the characterizing properties in the above theorem. This is because Alos-Ferrer (2006) showed that Neutrality is a consequence of Faithfulness, Cancellation and Reinforcement. See Fishburn 1978a and Baigent and Xu 1991 for alternative characterizations of Approval Voting, and Xu 2010 for a survey of the characterizations of Approval Voting (cf. the characterization of Approval Voting from Goodin and List 2006)[^goodin-2006][^list-2006].

Myerson (1995) introduced a general framework for characterizing *abstract scoring rules* that include Borda Count and Approval Voting as examples. The key idea is to think of a ballot, called a **signal** or a **vote**, as a function from candidates to a set $\mathcal{V}$, where $\mathcal{V}$ is a set of numbers. That is, the set of ballots is a subset of $\mathcal{V}^X$ (the set of functions from $X$ to $\mathcal{V}$). Then, an anonymous profile of signals assigns a score to each candidate $X$ by summing the numbers assigned to $X$ by each voter. This allows us to define voting methods by specifying the set of ballots:

- Plurality Rule: The ballots are functions assigning 0 or 1 to the candidates such that exactly one candidate is assigned 1: $\{v\ |\ v\in \{0,1\}^X$ and there is an $A\in X$ such that $v(A)=1$ and for all $B$, if $B\ne A$, then $v(B)=0\}$
- Approval Voting: The ballots are functions assigning 0 or 1 to the candidates: $\{v\ |\ v\in \{0,1\}^X \}$
- Borda Count: The ballots are functions assigning numbers from the set $\{\#X, \#X-1,\ldots,0\}$ such that each candidate is assigned exactly one of the numbers: $\{v\ |\ v\in\{\# X, \# X - 1, \ldots, 0\}^X$ such that $v$ is a bijection$\}$
- Range Voting: The ballots are assignments of real numbers between 0 and 1 to candidates: $[0,1]^X = \{v \ |\ v:X\rightarrow [0,1] \}$
- Cumulative Voting: The ballots are assignments of real numbers between 0 and 1 to candidates such that the assignments sum to 1: $ \{v \ |\ v\in [0,1]^X$ and $\sum_{A\in X} v(A)=1\}$
- Formal Utilitarian: The ballots are assignments of real numbers to candidates: $\mathbb{R}^X = \{v \ |\ v:X\rightarrow\mathbb{R}\}$.

Myerson (1995) showed that an abstract voting rule is an abstract scoring rule if and only if it satisfies Reinforcement, Universal Domain (i.e. it is defined for all anonymous profiles), a version of the Neutrality property (adapted to the more abstract setting), and the Continuity property, which is called **Overwhelming Majority**. Pivato (2013) generalizes this result, and Gaertner and Xu (2012) provide a related characterization result (using different properties). Pivato (2014) characterizes Formal Utilitarian and Range Voting within the class of abstract scoring rules, and Mace (2018) extends this approach to cover a wider class of grading voting methods (including Majority Judgement).

### 4.3 Voting to Track the Truth

The voting methods discussed above have been judged on *procedural* grounds. This “proceduralist approach to collective decision making” is defined by Coleman and Ferejohn (1986, p. 7) as one that “identifies a set of ideals with which any collective decision-making procedure ought to comply. … [A] process of collective decision making would be more or less justifiable depending on the extent to which it satisfies them.” The authors add that a distinguishing feature of proceduralism is that “what justifies a [collective] decision-making procedure is strictly a necessary property of the procedure — one entailed by the definition of the procedure alone.” Indeed, the characterization theorems discussed in the previous section can be viewed as an implementation of this idea (cf. Riker 1982)[^riker-1982]. The general view is to analyze voting methods in terms of “fairness criteria” that ensure that a given method is sensitive to *all* of the voters’ opinions in the right way.

However, one may not be interested only in whether a collective decision was arrived at “in the right way,” but in whether or not the collective decision is *correct*. This *epistemic* approach to voting is nicely explained by Joshua Cohen (1986, p. 34):

> An epistemic interpretation of voting has three main elements: (1) an independent standard of correct decisions — that is, an account of justice or of the common good that is independent of current consensus and the outcome of votes; (2) a cognitive account of voting — that is, the view that voting expresses beliefs about what the correct policies are according to the independent standard, not personal preferences for policies; and (3) an account of decision making as a process of the adjustment of beliefs, adjustments that are undertaken in part in light of the evidence about the correct answer that is provided by the beliefs of others.

Under this interpretation of voting, a given method is judged on how well it “tracks the truth” of some objective fact (the truth of which is independent of the method being used). A comprehensive comparison of these two approaches to voting touches on a number of issues surrounding the justification of democracy (cf. Christiano 2008)[^christiano-2008]; however, I will not focus on these broader issues here. Instead, I briefly discuss an analysis of Majority Rule that takes this epistemic approach.

The most well-known analysis comes from the writings of Condorcet (1785). The following theorem, which is attributed to Condorcet and was first proved formally by Laplace, shows that if there are only two options, then majority rule is, in fact, the best procedure from an epistemic point of view. This is interesting because it also shows that a proceduralist analysis and an epistemic analysis both single out Majority Rule as the “best” voting method when there are only two candidates.

Assume that there are $n$ voters that have to decide between two alternatives. Exactly one of these alternatives is (objectively) “correct” or “better.” The typical example here is a jury deciding whether or not a defendant is guilty. The two assumptions of the Condorcet jury theorem are:

**Independence**: The voters’ opinions are probabilistically independent (so, the probability that two or more voters are correct is the product of the probability that each individual voter is correct).

**Voter Competence**: The probability that a voter makes the correct decision is greater than 1/2 (and this probability is the same for all voters, though this is not crucial).

See Dietrich 2008 for a critical discussion of these two assumptions. The classic theorem is:

**Condorcet Jury Theorem**. Suppose that Independence and Voter Competence are both satisfied. Then, as the group size increases, the probability that the majority chooses the correct option increases and converges to certainty.

See Nitzan 2010 (part III) and Dietrich and Spiekermann 2013 for modern expositions of this theorem, and Goodin and Spiekermann 2018 for implications for the theory of democracy.

Condorcet envisioned that the above argument could be adapted to voting situations with more than two alternatives. Young (1975, 1988, 1995) was the first to fully work out this idea (cf. List and Goodin 2001 who generalize the Condorcet Jury Theorem to more than two alternatives in a different framework)[^list-2001]. He showed (among other things) that the Borda Count can be viewed as the *maximum likelihood estimator* for identifying the *best* candidate. Conitzer and Sandholm (2005), Conitzer et al. (2009), Xia et al. (2010), and Xia (2016) take these ideas further by classifying different voting methods according to whether or not the methods can be viewed as a *maximum likelihood estimator* (for a noise model). The most general results along these lines can be found in Pivato 2013 which contains a series of results showing when voting methods can be interpreted as different kinds of statistical ‘estimators’.

### 4.4 Computational Social Choice

One of the most active and exciting areas of research that is focused, in part, on the study of voting methods and voting paradoxes is *computational social choice*. This is an interdisciplinary research area that uses ideas and techniques from theoretical computer science and artificial intelligence to provide new perspectives and to ask new questions about methods for making group decisions; and to use voting methods in computational domains, such as recommendation systems, information retrieval, and crowdsourcing. It is beyond the scope of this article to survey this entire research area. Readers are encouraged to consult the *Handbook of Computational Social Choice* (Brandt et al. 2016)[^brandt-2016] for an overview of this field (cf. also Endriss 2017)[^endriss-2017]. In the remainder of this section, I briefly highlight some work from this research area related to issues discussed in this article.

Section 4.1 discussed election scenarios in which voters choose their ballots strategically and briefly introduced the Gibbard-Satterthwaite Theorem. This theorem shows that every voting method satisfying natural properties has profiles in which there is some voter, called a **manipulator**, that can achieve a better outcome by selecting a ballot that misrepresents her preferences. Importantly, in order to successfully manipulate an election, the manipulator must not only know which voting method is being used but also how the other members of society are voting. Although there is some debate about whether manipulation in this sense is in fact a problem (Dowding and van Hees 2008; Conitzer and Walsh, 2016, Section 6.2)[^conitzer-2016][^dowding-2008], there is interest in mechanisms that incentivize voters to report their “truthful” preferences. In a seminal paper, Bartholdi et al. (1989) argue that the complexity of computing which ballot will lead to a preferred outcome for the manipulator may provide a barrier to voting insincerely. See Faliszewski and Procaccia 2010, Faliszewski et al. 2010, Walsh 2011, Brandt et al. 2013, and Conitzer and Walsh 2016 for surveys of the literature on this and related questions, such as the complexity of determining the winner given a voting method and the complexity of determining which voter or voters should be *bribed* to change their vote to achieve a given outcome.

One of the most interesting lines of research in computational social choice is to use techniques and ideas from AI and theoretical computer science to design new voting methods. The main idea is to think of voting methods as solutions to an optimization problem. Consider the space of all rankings of the alternatives $X$. Given a profile of rankings, the voting problem is to find an “optimal” group ranking (cf. the discussion or *distance-based rationalizations* of voting methods from Elkind et al. 2015)[^elkind-2015]. What counts as an “optimal” group ranking depends on assumptions about the type of the decision that the group is making. One assumption is that the voters have real-valued **utilities** for each candidate, but are only able to report rankings of the alternatives (it is assumed that the rankings represent the utility functions). The voting problem is to identify the candidates that maximizes the (expected) social welfare (the average of the voters’ utilities), given the partial information about the voters’ utilities—i.e., the profile of rankings of the candidates. See Pivato 2015 for a discussion of this approach to voting and Boutilier et al. 2015 for algorithms that solve different versions of this problem. A second assumption is that there is an objectively correct ranking of the alternatives and the voters’ rankings are noisy estimates of this ground truth. This way of thinking about the voting problem was introduced by Condorcet and discussed in Section 4.3. Procaccia et al. (2016) import ideas from the theory of error-correcting codes to develop an interesting new approach to aggregate rankings viewed as noisy estimates of some ground truth.

## 5. Concluding Remarks

### 5.1 From Theory to Practice

As with any mathematical analysis of social phenomena, questions abound about the “real-life” implications of the theoretical analysis of the voting methods given above. The main question is whether the voting paradoxes are simply features of the formal framework used to represent an election scenario or formalizations of real-life phenomena. This raises a number of subtle issues about the scope of mathematical modeling in the social sciences, many of which fall outside the scope of this article. I conclude with a brief discussion of two questions that shed some light on how one should interpret the above analysis.

How *likely* is a Condorcet Paradox or any of the other voting paradoxes? There are two ways to approach this question. The first is to calculate the probability that a majority cycle will occur in an election scenario. There is a sizable literature devoted to analytically deriving the probability of a majority cycle occurring in election scenarios of varying sizes (see Gehrlein 2006, and Regenwetter *et al*. 2006, for overviews of this literature)[^gehrlein-2006][^regenwetter-2006]. The calculations depend on assumptions about the distribution of rankings among the voters. One distribution that is typically used is the so-called **impartial culture**, where each ranking is possible and occurs with equal probability. For example, if there are three candidates, and it is assumed that the voters’ ballots are rankings of the candidates, then each possible ranking can occur with probability 1/6. Under this assumption, the probability of a majority cycle occurring has been calculated (see Gehrlein 2006, for details)[^gehrlein-2006]. Riker (1982, p. 122) has a table of the relevant calculations. Two observations about this data: First, as the number of candidates and voters increases, the probability of a majority cycles increases to certainty. Second, for a fixed number of candidates, the probability of a majority cycle still increases, though not necessarily to certainty (the number of voters is the independent variable here). For example, if there are five candidates and seven voters, then the probability of a majority cycle is 21.5 percent. This probability increases to 25.1 percent as the number of voters increases to infinity (keeping the number of candidates fixed) and to 100 percent as the number of candidates increases to infinity (keeping the number of voters fixed). Prima facie, this result suggests that we should expect to see instances of the Condorcet and related paradoxes in large elections. Of course, this interpretation takes it for granted that the impartial culture is a realistic assumption. Many authors have noted that the impartial culture is a significant idealization that almost certainly does not occur in real-life elections. Tsetlin et al. (2003) go even further arguing that the impartial culture is a worst-case scenario in the sense that *any* deviation results in lower probabilities of a majority cycle (see Regenwetter *et al*. 2006, for a complete discussion of this issue, and List and Goodin 2001, Appendix 3, for a related result)[^list-2001][^regenwetter-2006].

A second way to argue that the above theoretical observations are robust is to find supporting empirical evidence. For instance, is there evidence that majority cycles have occurred in actual elections? While Riker (1982) offers a number of intriguing examples, the most comprehensive analysis of the empirical evidence for majority cycles is provided by Mackie (2003, especially Chapters 14 and 15). The conclusion is that, in striking contrast to the probabilistic analysis referenced above, majority cycles typically have not occurred in actual elections. However, this literature has not reached a consensus about this issue (cf. Riker 1982)[^riker-1982]: The problem is that the available data typically does not include voters’ opinions about *all* pairwise comparison of candidates, which is needed to determine if there is a majority cycle. So, this information must be *inferred* (for example, by using statistical methods) from the given data.

A related line of research focuses on the influence of factors, such as polls (Reijngoud and Endriss 2012)[^reijngoud-2012], social networks (Santoro and Beck 2017, Stirling 2016)[^santoro-2017][^stirling-2016] and deliberation among the voters (List 2018)[^list-2018], on the profiles of ballots that are actually realized in an election. For instance, List et al. 2013 has evidence suggesting that deliberation reduces the probability of a Condorcet cycle occurring.

**How do the different voting methods compare in actual elections?** In this article, I have analyzed voting methods under highly idealized assumptions. But, in the end, we are interested in a very practical question: Which method should a group adopt? Of course, any answer to this question will depend on many factors that go beyond the abstract analysis given above (cf. Edelman 2012a)[^edelman-2012a]. An interesting line of research focuses on incorporating *empirical evidence* into the general theory of voting. Evidence can come in the form of a computer simulation, a detailed analysis of a particular voting method in real-life elections (for example, see Brams 2008, Chapter 1, which analyzes Approval voting in practice)[^brams-2008], or as *in situ* experiments in which voters are asked to fill in additional ballots during an actual election (Laslier 2010, 2011)[^laslier-2011][^laslier-2010][^laslier-2011-2][^laslier-2010-2].

The most striking results can be found in the work of Michael Regenwetter and his colleagues. They have analyzed datasets from a variety of elections, showing that many of the usual voting methods that are considered irreconcilable (e.g., Plurality Rule, Borda Count and the Condorcet consistent methods from Section 3.1.1) are, in fact, in perfect agreement. This suggests that the “theoretical literature may promote overly pessimistic views about the likelihood of consensus among consensus methods” (Regenwetter *et al*. 2009, p. 840)[^regenwetter-2009]. See Regenwetter *et al*. 2006 for an introduction to the methods used in these analyses and Regenwetter *et al*. 2009 for the current state-of-the-art.

### 5.2 Further Reading

My objective in this article has been to introduce different voting methods and to highlight key results and issues that facilitate comparisons between the voting methods. To dive more into the details of the topics introduced in this article, see Saari 2001, 2008, Nurmi 1998, Brams and Fishburn 2002, Zwicker 2012, and the collection of articles in Felsenthal and Machover 2012. Some important topics related to the study of voting methods not discussed in this article include:

- Saari’s influential geometric approach to study of voting methods and paradoxes (Saari 1995)[^saari-1995];
- The study of measures of *voting power*: the probability that a single voter is decisive in an election (Gelman et al. 2002; Felsenthal and Machover 1998)[^felsenthal-1998][^gelman-2002];
- The study of *probabilistic* voting methods: a voting method in which the output is a lottery over the set of candidates rather than a ranking or set of candidates (Brandt 2017)[^brandt-2017][^brandt-2017-2];
- Questions about whether it is rational to vote in an election (Brennan 2016)[^brennan-2016]; and
- The study of methods for ensuring fair and proportional representation (Balinksi and Young 1982; Pukelsheim 2017)[^pukelsheim-2017].

Finally, consult List 2013 and Morreau 2014 for a discussion of broader issues in theory of social choice.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=voting-methods). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/voting-methods/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=voting-methods&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/voting-methods/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- Lalley, S. and E. G. Weyl, 2018b, “Nash Equilibria for Quadratic Voting,” available at SSRN: [https://ssrn.com/abstract=2488763](https://ssrn.com/abstract=2488763)
- Three videos created by Donald Saari for the 2008 Mathematics Awareness Month which had the theme “mathematics of voting”:
- [Mathematics of Voting](http://www.math.uci.edu/~dsaari/Mathematics%20of%20voting.mov)
- [Creating Voting Paradoxes](http://www.math.uci.edu/~dsaari/Creating%20Voting%20Paradoxes.mov)
- [What Causes Voting Paradoxes](http://www.math.uci.edu/~dsaari/what_causes_voting_paradoxes.mov)
- [The Center for Election Science](https://www.electionscience.org/), organization devoted to the promoting the use of Approval Voting in elections.
- [PrefLib: A Library for Preferences](http://www.preflib.org/), data sets including ballots from real elections and python tools for generating election scenarios.
- [The Center for Range Voting](http://rangevoting.org/), blog promoting the use Score Voting.
- [Tweak the Vote](https://www.wnycstudios.org/story/tweak-vote), Radiolab show discussing some of the voting methods discussed in the entry.
- [Pioneer Press opinion piece arguing in favor of using the Hare system](https://www.twincities.com/2017/04/14/kevin-zollman-dont-return-to-the-democratic-dark-ages-keep-ranked-voting/), by Kevin Zollman.

## Related Entries

Arrow’s theorem | democracy | preferences | social choice theory | voting

### Acknowledgments

I would like to thank Ulle Endriss, Wes Holliday, Christian List, Uri Nodelman, Rohit Parikh, Edward Zalta and two anonymous referees for many valuable comments that greatly improved the readability and content of this article. This first version of the article was written while the author was generously supported by an NWO Vidi grant 016.094.345.

[^alger-2006]: Alger, D., 2006, “Voting by proxy,” *Public Choice*, 126(1–2): 1–26.

[^alos-ferrer-2006]: Alos-Ferrer, C., 2006, “A simple characterization of approval voting,” *Social Choice and Welfare*, 27: 621–625.

[^anscombe-1976]: Anscombe, G. E. M., 1976, “On frustration of the majority by fulfillment of the majority’s will,” *Analysis*, 36(4): 161–168.

[^aragones-2011]: Aragones, E., I. Gilboa, and A. Weiss, 2011, “Making statements and approval voting,” *Theory and Decision,* 71:461–472.

[^arrow-1963]: Arrow, K., 1963, *Social Choice and Individual Values*, New Haven: Yale University Press, 2nd edition.

[^asan-2002]: Asan, G. and R. Sanver, 2002, “Another characterization of the majority rule,” *Economics Letters*, 75(3): 409–413.

[^baigent-1991]: Baigent, N., and Xu, Y., 1991, “Independent necessary and sufficient conditions for approval voting,” *Mathematical Social Sciences*, 21: 21–29.

[^balinski-2007]: Balinski, M. and R. Laraki, 2007, “A theory of measuring, electing and ranking,” *Proceeding of the National Academy of Sciences*, 104(21): 8720–8725.

[^balinski-2010]: –––, 2010, *Majority Judgement: Measuring, Ranking and Electing*, Boston: MIT Press.

[^balinski-2014]: Balinski, M. and R. Laraki, 2014, “What should “majority decision” mean?,” in *Majority Decisions,* (J. Elster and S. Novak eds.), pp. 103–131, Cambridge University Press.

[^balinski-1982]: Balinski, M. and H. P. Young, 1982, *Fair Representation: Meeting the Idea of One Man, One Vote*, Yale University Press.

[^bartholdi-1989]: Bartholdi III, J. J., C. A. Tovey, and M. A. Trick, 1989, “The computational difficulty of manipulating an election,” *Social Choice and Welfare*, 6(3): 227–241.

[^bartholdi-1989-2]: –––, 1989, “Voting schemes for which it can be difficult to tell who won the election,” *Social Choice and Welfare*, 6(2): 157–165.

[^bassett-1999]: Bassett, G. and J. Persky, 1999, “Robust voting,” *Public Choice,* 99(3-4): 299–310.

[^behrens-2017]: Behrens, J., 2017, “The origins of liquid democracy, ” *The Liquid Democracy Journal*, 5(2): 7–17, [available online](http://www.liquid-democracy-journal.org/issue/5/The_Liquid_Democracy_Journal-Issue005-02-The_Origins_of_Liquid_Democracy.html).

[^blum-2016]: Blum, C. and C. I. Zuber, 2016, “Liquid democracy: Potentials, problems, and perspectives,”*Journal of Political Philosophy*, 24(2): 162–182.

[^borda-1784]: Borda, J.-C. de, 1784, “Mémoire sur les élections au scrutin par M. de Borda” in *Mémoires de l’Académie Royale des Sciences année 1781*, Paris: l’Imprimerie Royale, pp. 657–665; Translated in McLean and Urken 1995, pp. 83–89.

[^brams-2008]: Brams, S., 2008, *Mathematics and Democracy*, Princeton: Princeton University Press.

[^brams-2007]: Brams, S. and P. Fishburn, 2007 (2nd Edition), *Approval Voting*, New York: Springer.

[^brams-2002]: –––, 2002, “Voting procedures,” in *Handbook of Social Choice and Welfare*, K. J. Arrow, A. K. Sen, and K. Suzumura (eds.), Amsterdam: Elsevier, pp. 173–236.

[^brams-1988a]: Brams, S., P. Fishburn and S. Merrill III, 1988a, “The responsiveness of approval voting: Comments on Saari and Van Newenhizen,” *Public Choice*, 59(2): 121–131.

[^brams-1988b]: –––, 1988b, “Rejoinder to Saari and Van Newenhizen,” *Public Choice*, 59(2): 149.

[^brams-1998]: Brams, S., D. M. Kilgour D. M., and W. Zwicker, 1998, “The paradox of multiple elections,” *Social Choice and Welfare*, 15(2): 211–236.

[^brams-2015]: Brams, S. and R. Potthoff, 2015, “The paradox of grading systems,” *Public Choice*, 165(3-4): 193–210.

[^brams-nd]: Brams, S. and Sanver, M. R., “Voting systems that combine approval and preference,” in *The Mathematics of Preference, Choice, and Order: Essays in Honor of Peter C. Fishburn*, S. Brams, W. Gehrlein, and F. Roberts (eds.), pp. 215–237, Berlin: Springer.

[^brandt-2017]: Brandt, F., 2017, “Rolling the dice: Recent results in probabilistic social choice,” in *Trends in Computational Social Choice*, U. Endriss (editor): 3–19.

[^brandt-2017-2]: Brandt, F., C. Geist, and D. Peters, 2017, “Optimal bounds for the no-show paradox via SAT solving,” *Mathematical Social Sciences*, 90: 18–27.

[^brandt-2019]: Brandt F., J. Hofbauer, and M. Strobel, 2019, “Exploring the no-show paradox for Condorcet extensions using Ehrhart theory and computer simulations,” in *Proceedings of the 18th International Conference on Autonomous Agents and Multiagent Systems (AAMAS)*, Montreal: AAAI Press.

[^brandt-2013]: Brandt, F., V. Conitzer, and U. Endris, 2013, “Computational social choice,” in G. Weiss, editor, *Multiagent Systems*, pp. 213–283, Cambridge, MA: MIT Press.

[^brandt-2016]: Brandt, F., V. Conitzer, U. Endriss, J. Lang, and A. D. Procaccia, editors, 2016, *Handbook of Computational Social Choice*, Cambridge: Cambridge University Press.

[^brennan-2016]: Brennan, J., 2016, “The ethics and rationality of voting,” *The Stanford Encyclopedia of Philosophy* (Winter 2016 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/win2016/entries/voting/](https://plato.stanford.edu/archives/win2016/entries/voting/)>.

[^brennan-1993]: Brennan, G. and L. Lomasky, 1993, *Democracy and Decision: The Pure Theory of Electoral Preference,* Cambridge: Cambridge University Press.

[^brill-2018]: Brill, M. and N. Talmon, 2018, “Pairwise liquid democracy,” in *Proceedings of the 27th International Joint Conference on Artificial Intelligence (IJCAI),* Stockholm: International Joint Conferences on Artificial Intelligence.

[^boutilier-2015]: Boutilier, C., I. Caragiannis, S. Haber, T. Lu, A. Procaccia, and O. Sheffet, 2015, “Optimal social choice functions: A utilitarian view, ” *Artificial Intelligence*, 227: 190–213.

[^cato-2014]: Cato, S., 2014, “Independence of irrelevant alternatives revisited,” *Theory and Decision* 76(4): 511–527.

[^campbell-2002]: Campbell, D. and J. Kelly, 2002, “Non-monotonicity does not imply the no-show paradox,” *Social Choice and Welfare,* 19(3): 513–515.

[^chebotarev-1998]: Chebotarev, P. and E. Shamis, 1998, “Characterization of scoring methods for preference aggregation,” *Annals of Operations Research*, 80: 299–332.

[^christiano-2008]: Christiano, T., “Democracy,” *The Stanford Encyclopedia of Philosophy* (Fall 2008 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/fall2008/entries/democracy/](https://plato.stanford.edu/archives/fall2008/entries/democracy/)>.

[^christoff-2017]: Christoff, Z. and D. Grossi, 2017, “Binary voting with delegable proxy: An analysis of liquid democracy,” in *Proceedings of TARK 2017*, Liverpool: Electronic Proceedings in Theoretical Computer Science.

[^cohen-1986]: Cohen, J., 1986, “An epistemic conception of democracy,” *Ethics*, 97(1): 26–38.

[^coleman-1986]: Coleman,J. and J. Ferejohn, 1986, “Democracy and social choice,” *Ethics*, 97(1): 6–25.

[^condorcet-1785]: Condorcet, M.J.A.N. de C., Marque de, 1785, *Essai sur l’application de l’analyse à la probabilitié des décisions rendues à la pluralité des voix*, Paris: l’Imprimerie Royale; Translated in Mclean and Urken 1995, pp. 91–113.

[^conitzer-2016]: Conitzer, V. and Wash, T., 2016, “Barriers to manipulation in voting,” Chapter 6 in *Handbook of Computational Social Choice*, 127–145, New York: Cambridge University Press.

[^conitzer-2005]: Conitzer, V. and T. Sandholm, 2005, “Common voting rules as maximum likelihood estimators,” in *Proceedings of the 21st Annual Conference on Uncertainty in Artificial Intelligence* (UAI-05), pp. 145–152.

[^conitzer-2009]: Conitzer, V., M. Rognlie, and L. Xia, 2009, “Preference functions that score rankings and maximum likelihood estimation,” in *1st International Joint Conference on Artificial Intelligence (IJCAI-09)*, pp. 109–115, Pasadena: AAAI Press.

[^daudt-1976]: Daudt, H. and D. W. Rae, 1976, “The Ostrogorski paradox: a peculiarity of compound majority decision,” *European Journal of Political Research*, 4(4): 391–399.

[^dietrich-2008]: Dietrich, F., 2008, “The premises of Condorcet’s jury theorem are not simultaneously justified,” *Episteme – a Journal of Social Epistemology*, 5(1): 56–73.

[^dietrich-2013]: Dietrich, F. and K. Spiekermann, 2013, “Epistemic democracy with defensible premises,” *Economics & Philosophy*, 29(1): 87–120.

[^dowding-2008]: Dowding, K. and M. Van Hees, 2008, “In praise of manipulation,” *British Journal of Political Science*, 38(1): 1–15.

[^driver-2014]: Driver, J., “The history of utilitarianism,” The Stanford Encyclopedia of Philosophy (Winter 2014 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/win2014/entries/utilitarianism-history/](https://plato.stanford.edu/archives/win2014/entries/utilitarianism-history/)>.

[^duddy-2014]: Duddy, C., 2014,“Condorcet’s principle and the strong no-show paradoxes,” *Theory and Decision*, 77(2):275–285.

[^dummett-1984]: Dummett, M., 1984, *Voting Procedures*, Oxford: Clarendon.

[^edelman-2012a]: Edelman, P. H., 2012a, “The institutional dimension of election design,” *Public Choice*, 153(3/4):287–293.

[^edelman-2012b]: –––, 2012b, “Michel Balinski and Rida Laraki: Majority judgment: measuring, ranking, and electing,” *Public Choice*, 151:807–810.

[^elkind-2015]: Elkind, E., P. Faliszewski and A. Slinko, 2015, “Distance rationalization of voting rules,” *Social Choice and Welfare*, 45(2): 345–377.

[^endriss-2011]: Endriss, U., 2011, “Logic and social choice theory,” in *Logic and Philosophy Today*, J. van Benthem and A. Gupta (eds.), London: College Publications.

[^endriss-2017]: Endriss, U. (editor), 2017, *Trends in Computational Social Choice*, Amsterdam: AI Access Publishers.

[^fabienne-2013]: Fabienne, P., 2013, “Political legitimacy,” *The Stanford Encyclopedia of Philosophy* (Spring 2017 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/sum2017/entries/legitimacy/](https://plato.stanford.edu/archives/sum2017/entries/legitimacy/)>.

[^faliszewski-2010]: Faliszewski, P. and A. Procaccia, 2010, “AI’s war on manipulation: Are we winning?,” *AI Magazine*, 31(4): 53–64.

[^faliszewski-2010-2]: Faliszewski, P., E. Hemaspaandra, and L. Hemaspaandra, 2010, “Using complexity to protect elections,” *Communications of the ACM*, 53(11): 74–82.

[^felsenthal-2012]: Felsenthal, D., 2012, “Review of paradoxes afflicting procedures for electing a single candidate,” in *Electoral Systems: Paradoxes, Assumptions and Paradoxes*, pp. 19–91: Dordrecht, Springer.

[^felsenthal-1998]: Felsenthal, D. and M. Machover, 1998, *The Measurement of Voting Power: Theory and Practice, Problems and Paradoxes*, Cheltenham Glos: Edward Elgar Publishing.

[^felsenthal-2012-2]: ––– (editors), 2012, *Electoral Systems: Paradoxes, Assumptions and Procedures*, Dordrecht: Springer.

[^felsenthal-2008]: –––, 2008, “The majority judgment voting procedure: A critical evaluation,” *Homo Oeconomicus,* 25(3/4):319–334.

[^felsenthal-2017]: Felsenthal, D. and H. Nurmi, 2017, *Monotonicity Failures Afflicting Procedures for Electing a Single Candidate*, SpringerBriefs in Economics, Dordrecht:Springer.

[^felsenthal-2013]: Felsenthal, D. and N. Tideman, 2013, “Varieties of failure of monotonicity and participation under five voting methods,” *Theory and Decision*, 75(1): 59–77.

[^fishburn-1983]: Fishburn, P. and S. Brams, 1983, “Paradoxes of preferential voting,” *Mathematics Magazine*, 56(4): 207–214.

[^fishburn-1974]: Fishburn, P., 1974, “Paradoxes of voting,” *American Political Science Review*, 68(2): 537–546.

[^fishburn-1977]: –––, 1977, “Condorcet social choice functions,” *SIAM Journal of Applied Mathematics*, 33(3): 469–489.

[^fishburn-1978a]: –––, 1978a, “Axioms for approval voting: Direct proof,” *Journal of Economic Theory*, 19(1): 180–185.

[^fishburn-1978b]: –––, 1978b, “Symmetric and consistent aggregation with dichotomous preferences,” in *Aggregation and revelation of preferences*, Amsterdam: North-Holland.

[^fishburn-1982]: –––, 1982, “Monotonicity paradoxes in the theory of voting,” *Discrete Applied Mathematics,* 4: 119–134.

[^gaertner-2006]: Gaertner, W., 2006, *A Primer in Social Choice Theory*, Oxford: Oxford University Press.

[^gaertner-2012]: Gaertner, W. and Y. Xu, 2012, “A general scoring rule,” *Mathematical Social Sciences*, 63: 193–196.

[^gardenfors-1973]: Gardenfors, P., 1973, “Positionalist voting functions,” *Theory and Decision*, 4(1): 1–24.

[^gehrlein-2006]: Gehrlein, W., 2006, *Condorcet’s Paradox*, Berlin: Springer.

[^gehrlein-2003]: Gehrlein, V. and D. Lepelley, 2003, “On some limitations of the median voting rule,” *Public Choice,* 117(1-2):177–190.

[^gelman-2002]: Gelman, A., J. Katz and F. Tuerlinckx, 2002, “The mathematics and statistics of voting power, ” *Statistical Science*, 17(4): 420–435.

[^gibbard-1973]: Gibbard, A., 1973, “Manipulation of voting schemes: A general result,” *Econometrica*, 41(4): 587–601.

[^goeree-2017]: Goeree, J. and J. Zhang, 2017, “One man, one bid,” *Games and Economic Behavior,* 101(C): 151–171.

[^golz-2018]: Golz, P., A. Kahng, S. Mackenzie, and A. Procaaccia, 2018, “The fluid mechanics of liquid democracy”, in *Proceedings of WINE: Web and Internet Economics*, 188–202: Oxford, Springer.

[^goodin-2006]: Goodin, R. and C. List, 2006, “A conditional defense of plurality rule: generalizing May’s theorem in a restricted informational environment,” *American journal of political science,* 50(4): 940–949.

[^goodin-2018]: Goodin, R. and K. Spiekermann, 2018, “An Epistemic Theory of Democracy,” Oxford: Oxford University Press.

[^green-armytage-2015]: Green-Armytage, J., 2015, “Direct voting and proxy voting,” *Constitutional Political Economy*, 26(2): 190–220.

[^grofman-2004]: Grofman, B. and S. Feld, 2004, “If you like the alternative vote (a.k.a. the instant runoff), then you ought to know about the Coombs rule,” *Electoral Studies*, 23: 641–659.

[^groves-1977]: Groves, T., and J. Ledyard, 1977, “Optimal allocation of public goods: A solution to the free rider problem,” *Econometrica*, 45(4): 783–810.

[^hansson-2009]: Hansson, S. O. and Grüne-Yanoff, T., “Preferences,” *The Stanford Encyclopedia of Philosophy* (Spring 2009 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/spr2009/entries/preferences/](https://plato.stanford.edu/archives/spr2009/entries/preferences/)>.

[^hausman-1995]: Hausman, D., 1995, “The impossibility of interpersonal utility comparisons,” *Mind*, 104(4): 473–490.

[^hylland-1980]: Hylland, A., and R. Zeckhauser, 1980, “A mechanism for selecting public goods when preferences must be elicited,” *Kennedy School of Government Discussion Paper* , 70D: Boston, Harvard University.

[^jimeno-2009]: Jimeno J. L., J. Perez and E. Garcia, 2009, “An extension of the Moulin no show paradox for voting correspondences,” *Social Choice and Welfare*, 33(3): 343–359.

[^kang-2018]: Kang, A., S. Mackenzie and A. Procaccia, 2018, “Liquid democracy: An algorithmic perspective,” in *Proceedings of 32nd AAAI Conference on Artificial Intelligence*: 1095–1102: New Orleans, AAAI Press.

[^kelly-1989]: Kelly, J.S., 1989, “The Ostrogorski’s paradox,” *Social Choice and Welfare*, 6(1): 71–76.

[^lacy-2000]: Lacy, D. and E. Niou, 2000, “A problem with referenda,” *Journal of Theoretical Politics,* 12(1):5–31. 2000.

[^lalley-2018a]: Lalley, S. and E. G. Weyl, 2018a, “Quadratic voting: How mechanism design can radicalize democracy,” *AEA Papers and Proceedings*, 108: 33–37.

[^lang-2009]: Lang, J. and L. Xia, 2009, “Sequential composition of voting rules in multi-issue domains,” *Mathematical Social Sciences,* 57(3): 304–324.

[^laslier-2011]: Laslier, J.-F., 2011, “Lessons from *in situ* experiments during French elections,” in *In Situ and Laboratory Experiments on Electoral Law Reform: French Presidential Elections*, B. Dolez, B. Grofman and A. Laurent (eds.), Berlin: Springer, pp. 91–104.

[^laslier-2010]: –––, 2010, “Laboratory experiments about approval voting” in *Handbook of Approval Voting*, J.-F. Laslier and R. Sanver (eds.), Berlin: Springer, pp. 339–356.

[^laslier-2011-2]: –––, 2011, “On choosing the alternative with the best median evaluation,” *Public Choice*, 153(3): 269–277.

[^laslier-2012]: –––, 2012, “And the loser is...Plurality voting” in *Electoral Systems: Paradoxes, Assumptions and Procedures*, D. S. Felsenthal and M. Machover (eds.), Berlin: Springer, pp. 327–351.

[^laslier-2010-2]: Laslier, J.-F. and R. Sanver (eds.), 2010, *Handbook on Approval Voting*, Series: Studies in Choice and Welfare, Berlin: Springer.

[^laurence-2017]: Laurence, B. and I. Sher, 2017, “Ethical considerations on quadratic voting,” *Public Choice*, 172:195–222.

[^levin-1995]: Levin, J. and B. Nalebuff, 1995, “An introduction to vote-counting schemes,” *Journal of Economic Perspectives*, 9(1): 3–26.

[^list-2013]: List, C., 2013, “Social choice theory,” *The Stanford Encyclopedia of Philosophy* (Spring 2013 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/win2013/entries/social-choice/](https://plato.stanford.edu/archives/win2013/entries/social-choice/)>.

[^list-2006]: –––, 2006, “The discursive dilemma and public reason,” *Ethics*, 116(2): 362–402.

[^list-2018]: –––, 2018, “Democratic deliberation and social choice: A review,” in *Oxford Handbook of Deliberative Democracy*, Oxford University Press.

[^list-2001]: List, C. and R. Goodin, 2001, “Epistemic democracy: Generalizing the Condorcet jury theorem,” *Journal of Political Philosophy*, 9(3): 277–306.

[^list-2013-2]: List, C., R. C. Luskin, J. S. Fishkin and I. McLean, 2013, “Deliberation, single-peakedness, and the possibility of meaningful democracy: Evidence from deliberative polls,” *Journal of Politics,* 75(1): 80–95.

[^mace-2018]: Mace, A., 2018, “Voting with evaluations: Characterizations of evaluative voting and range voting,” *Journal of Mathematical Economics*, 79: 10–17.

[^mackie-2003]: Mackie, G., 2003, *Democracy Defended*, Cambridge: Cambridge University Press.

[^malinas-2009]: Malinas, G. and J. Bigelow, “Simpson’s paradox,” *The Stanford Encyclopedia of Philosophy* (Fall 2009 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/fall2009/entries/paradox-simpson/](https://plato.stanford.edu/archives/fall2009/entries/paradox-simpson/)>.

[^maskin-1995]: Maskin, E., 1995, “Majority rule, social welfare functions and game forms,” in *Choice, Welfare and Development: A Festschrift in Honour of Amartya K. Sen*, K. Basu, P. Pattanaik, K. Suzumura (eds.), Oxford: Oxford University Press, pp. 100–109.

[^may-1952]: May, K., 1952, “A set of independent necessary and sufficient conditions for simply majority decision,” *Econometrica*, 20(4): 680–684.

[^mclean-1995]: McLean, I. and A. Urken (eds.), 1995, *Classics of Social Choice*, Ann Arbor: The University of Michigan Press.

[^merlin-2003]: Merlin, V., 2003, “ The axiomatic characterizations of majority voting and scoring rules, *Mathematical Social Sciences*, 161: 87–109.

[^miller-1969]: Miller, J., 1969, “A program for direct and proxy voting in the legislative process,” *Public Choice*, 7(1):107–113.

[^morreau-2014]: Morreau, M., 2014, “Arrow’s theorem,” *The Stanford Encyclopedia of Philosophy* (Winter 2016 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/win2016/entries/arrows-theorem/](https://plato.stanford.edu/archives/win2016/entries/arrows-theorem/)>.

[^morreau-2016]: Morreau, M., 2016, “Grading in groups,” *Economics & Philosophy*, 32(2):323–352.

[^moulin-1983]: Moulin, H., 1983, *The Strategy of Social Choice*, Amsterdam: North-Holland.

[^moulin-1988]: –––, 1988, “Condorcet’s principle implies the no show paradox,” *Journal of Economic Theory,*, 45: 53–64.

[^myerson-1995]: Myerson, R., 1995, “Axiomatic derivation of scoring rules without the ordering assumption,” *Social Choice and Welfare*, 12(1): 59–74.

[^nitzan-2010]: Nitzan, S., 2010, *Collective Preference and Choice*, Cambridge: Cambridge University Press.

[^nitzan-1981]: Nitzan, S. and A. Rubinstein, 1981, “A further characterization of Borda ranking method,” *Public Choice*, 36(1): 153–158.

[^niou-1987]: Niou, E. M. S., 1987, “ A note on Nanson’s rule,” *Public Choice*, 54: 191–193.

[^nunez-2017]: Nunez, M. and M. R. Sanver, 2017, “Revisiting the connection between the no-show paradox and monotonicity”, *Mathematical Social Sciences*, 90: 9–17.

[^nurmi-1987]: Nurmi, H., 1987, *Comparing Voting Systems*, Dordrecht: D. Reidel.

[^nurmi-1999]: –––, 1999, *Voting Paradoxes and How to Deal with Them*, Berlin: Springer-Verlag.

[^nurmi-2010]: –––, 2010, “Voting theory,” in *e-Democracy: A Group Decision and Negotiation Perspective*, D. R. Insua and S. French (eds.), Berlin: Springer, pp. 101–124.

[^ostorogorski-1902]: Ostorogorski, M., 1902, *Democracy and the Organization of Political Parties*, London: Macmillan.

[^pauly-2008]: Pauly, M., 2008, “On the role of language in social choice theory,” *Synthese*, 163(2): 227–243.

[^perez-2001]: Perez, J., 2001, “The strong no show paradoxes are a common flaw in Condorcet voting correspondences,” *Social Choice and Welfare*, 18: 601–616

[^pigozzi-2005]: Pigozzi, G., 2005, “Two aggregation paradoxes in social decision making: the Ostrogorski paradox and the discursive dilemma,” *Episteme: A Journal of Social Epistemology,* 2(2): 33–42.

[^pivato-2013]: Pivato, M., 2013, “Variable-population voting rules,” *Journal of Mathematical Economics*, 49: 210–221.

[^pivato-2013-2]: –––, 2013, “Voting rules as statistical estimators,” *Social Choice and Welfare*, 40(2): 581–630.

[^pivato-2014]: –––, 2014, “Formal utilitarianism and range voting,” *Mathematical Social Sciences*, 67: 50–56.

[^pivato-2015]: –––, 2015, “Condorcet meets Bentham,” *Journal of Mathematical Economics*, 59: 58–65.

[^posner-2015]: E. Posner and E. G. Weyl, 2015, “Voting squared: Quadratic voting in democratic politics,” *Vanderbilt Law Review,* 68(2): 441–499.

[^posner-2017]: –––, 2017, “Quadratic voting and the public good: Introduction,”*Public Choice* (Special Issue: Quadratic Voting and the Public Good), 172(1-2): 1–22.

[^poundstone-2008]: Poundstone, W., 2008, *Gaming the Vote: Why Elections aren’t Fair (and What We Can Do About It)*, New York: Hill and Wang Press.

[^pukelsheim-2017]: Pukelsheim, F., 2017, *Proportional Representation: Apportionment Methods and Their Applications*, Dordrecht: Springer.

[^procaccio-2016]: Procaccio, A., N. Shah, and Y. Zick, 2016, “Voting rules as error-correcting codes,” *Artificial Intelligence*, 231: 1–16.

[^regenwetter-2006]: Regenwetter, M., B. Grofman, A.A.J. Marley, A.A.J. and I. Tsetlin, 2006, *Behavioral Social Choice: Probabilistic Models, Statistical Inference, and Applications*, Cambridge: Cambridge University Press.

[^regenwetter-2009]: Regenwetter, M., B. Grofman, A. Popova, W. Messner, C. Davis-Stober, and D. Cavagnaro, 2009, “Behavioural social choice: A status report,” *Philosophical Transactions of the Royal Society B*, 364(1518): 833–843.

[^reijngoud-2012]: Reijngoud, A. and U. Endriss, 2012, “Voter response to iterated poll information,” In *Proceedings of the 11th International Conference on Autonomous Agents and Multiagent Systems (AAMAS-2012)*: 635–644, Valencia, Spain, International Foundation for Autonomous Agents and Multiagent Systems.

[^riker-1982]: Riker, W., 1982, *Liberalism against Populism: A Confrontation between the Theory of Democracy and the Theory of Social Choice*, San Francisco: W. H. Freeman & Co.

[^risse-2001]: Risse, M., 2001, “Arrow’s theorem, indeterminacy, and multiplicity reconsidered,” *Ethics*, 111: 706–734.

[^risse-2004]: –––, 2004, “Arguing for majority rule,” *Journal of Political Philosophy*, 1(1): 41–64.

[^risse-2005]: –––, 2005, “Why the count de Borda cannot beat the Marquis de Condorcet,” *Social Choice and Welfare*, 25: 95–113.

[^saari-1989]: Saari, D., 1989, “A dictionary of voting paradoxes,” *Journal of Economic Theory*, 48(2): 443–475.

[^saari-1995]: –––, 1995, *Basic Geometry of Voting*, Berlin: Springer.

[^saari-2000]: –––, 2000, “Mathematical structure of voting paradoxes: II. Positional voting,” *Economic Theory*, 15(1): 55–102.

[^saari-2001]: –––, 2001, *Decisions and Elections: Explaining the Unexpected*, Cambridge: Cambridge University Press.

[^saari-2003]: –––, 2003, “Capturing the ‘will of the people’,” *Ethics*, 113: 333–334.

[^saari-nd]: –––, “Which is better: the Condorcet or Borda winner?,”*Social Choice and Welfare*, 26: 107–129.

[^saari-2008]: –––, 2008, *Disposing Dictators, Demystifying Voting Paradoxes*, Cambridge: Cambridge University Press.

[^saari-1988a]: Saari, D. and J. Van Newenhizen, 1988a, “The problem of indeterminacy in approval, multiple, and truncated voting systems,” *Public Choice*, 59(2): 101–120.

[^saari-1988b]: –––, 1988b, “Is approval voting an ‘unmitigated evil’: A response to Brams, Fishburn, and Merrill,” *Public Choice*, 59(2): 133–147.

[^santoro-2017]: Santoro, L. R. and P. Beck, 2017, “Social networks and vote choice, ” in *The Oxford Handbook of Political Networks,* Oxford University Press.

[^sanver-2012]: Sanver, M. R., and W. Zwicker, 2012, “Monotonicity properties and their adaption to irresolute social choice rules,” *Social Choice and Welfare*, 39: 371–398.

[^satterthwaite-1975]: Satterthwaite, M., 1975, “Strategy-proofness and Arrow’s conditions: Existence and correspondence theorems for voting procedures and social welfare functions,” *Journal of Economic Theory*, 10(2): 198–217.

[^scarsini-1998]: M. Scarsini, 1998, “A strong paradox of multiple elections,” *Social Choice and Welfare*, 15(2): 237–238.

[^schwartz-1986]: Schwartz, T., 1986, *The Logic of Collective Choice*, New York: Columbia University Press.

[^schwartz-2018]: –––, 2018, *Cycles and Social Choice: The True and Unabridged Story of a Most Protean Paradox*, Cambridge: Cambridge University Press.

[^sinnott-armstrong-2019]: Sinnott-Armstrong, W., “Consequentialism,” The Stanford Encyclopedia of Philosophy (Summer 2019 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/sum2019/entries/consequentialism/](https://plato.stanford.edu/archives/sum2019/entries/consequentialism/)>.

[^stirling-2016]: Stirling, W., 2016, *Theory of Social Choice on Networks,* Cambridge: Cambridge University Press.

[^taylor-2005]: Taylor, A., 2005, *Social Choice and the Mathematics of Manipulation*, Cambridge: Cambridge University Press.

[^tsetlin-2003]: Tsetlin, I., M. Regenwetter, and B. Grofman, 2003, “The impartial culture maximizes the probability of majority cycles,” *Social Choice and Welfare*, 21(3): 387–398.

[^wagner-1983]: Wagner, C., 1983, “Anscombe’s paradox and the rule of three-fourths,” *Theory and Decision*, 15(3): 303–308.

[^wagner-1984]: –––, 1984, “Avoiding Anscombe’s paradox,” *Theory and Decision*, 16(3): 233–238.

[^walsh-2011]: Walsh, T., 2011, “Is computational complexity a barrier to manipulation?, ”*Annals of Mathematics and Artificial Intelligence*, 62(1-2): 7–26.

[^wodak-2019]: Wodak, D., 2019, “The expressive case against plurality rule,” *Journal of Political Philosophy*, 1–25.

[^woeginger-2003]: Woeginger, G., 2003, “A new characterization of the majority rule,” *Economic Letters*, 81(1): 89–94.

[^xia-2016]: Xia, L., 2016, “Bayesian estimators as voting rules, ” in *Proceeding UAI’16 Proceedings of the Thirty-Second Conference on Uncertainty in Artificial Intelligence*, 785–794: New Jersey, AUAI Press.

[^xia-2010]: Xia, L., V. Conitzer and J. Lang, 2010, “Aggregating preferences in multi-issue domains by using maximum likelihood estimator,” in *9th International Joint Conference on Autonomous Agents and Multi Agent Systems (AAMAS-10)*, 399–406: Toronto, International Foundation for Autonomous Agents and Multiagent Systems.

[^xia-2007]: Xia, L., J. Lang, and M. Ying, 2007, “Sequential voting rules and multiple elections paradoxes,” in *Proceedings of the Eleventh Conference on Theoretical Aspects of Rationality and Knowledge (TARK-07)*, 279–288: Brussels, ACM Publishers.

[^young-1995]: Young, H.P., 1995, “Optimal voting rules,” *Journal of Economic Perspectives*, 9(1): 51–64.

[^young-1998]: –––, 1998, “Condorcet’s theory of voting,” *American Political Science Review*, 82(4): 1231–1233.

[^young-1975]: –––, 1975, “Social choice scoring functions,” *SIAM Journal of Applied Mathematics*, 28(4): 824–838.

[^zhang-2017]: Zhang, B. and H. Zhou, 2017, “Brief announcement: Statement voting and liquid democracy,” in *Proceedings of the 36th ACM Symposium on Principles of Distributed Computing (PODC)*, 359–361: Washington DC, ACM Publishers.

[^zwicker-2016]: Zwicker, W., 2016, “Introduction to the theory of voting,” in *Handbook of Computational Social Choice*, V. Conitzer, U. Endriss, J. Lang and A. Procaccia (eds.), 23–56, Boston: Cambridge University Press.
