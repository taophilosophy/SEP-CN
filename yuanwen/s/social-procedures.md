# Formal Approaches to Social Procedures
**First published Mon Sep 8, 2014; substantive revision Thu Nov 7, 2019**

*van Eijck, Jan, Verbrugge, Rineke (L.C.)*

Social procedures that have algorithmic aspects can often be improved by redesign. This holds for voting and other peaceful decision making procedures, for match-making, for auctioning, for fair division of estates, and for many procedures of distributive justice. The algorithmic aspects can be analyzed with formal methods. The term “social software” was coined by Rohit Parikh (2002)[^parikh-2002] for the emerging interdisciplinary enterprise that is concerned with the design and analysis of algorithms that regulate social processes. Such analysis and (re-)design uses methods from logic, game theory and theoretical computer science.[^note-1] The goals of research in formal approaches to social procedures are modeling social situations, developing theories of correctness, and (re-)designing social procedures, ideally leading to new social behavior.

Logic, game theory and computer science are not the only disciplines that have something to say about social mechanisms. Such mechanisms are also an object of study in voting theory, in auction theory, in social choice theory, in social epistemology, in mechanism design theory, and in algorithmic game theory. Multi-agent interaction at a more abstract level is studied in artificial intelligence and distributed computing, so all these disciplines have something to say about the formal analysis of social interaction.

## 1. Social Procedures as Algorithms

Social software cannot be seen as a clearly defined research field on its own, but rather an umbrella for certain types of research in computer science, logic, and game theory. Nevertheless, the social software perspective on social procedures and intelligent interaction, emphasizing algorithms and information, has already produced a wide variety of important insights. In this article, a number of examples will be discussed and pointers will be given to related discussions in philosophy.

The prototypical example of an *algorithm* in mathematics (see also entry on computability and complexity) is Euclid’s recipe for finding the greatest common divisor (GCD) of two positive whole numbers $A$ and $B$. The GCD of two numbers is the greatest number that divides both numbers without residue.

> If $A$ is larger than $B$, then replace $A$ by $A - B$, otherwise, if $B$ is larger than $A$, replace $B$ by $B - A$. Continue like this until $A$ equals $B$.

The final $A = B$ yields the greatest common divisor of the numbers $A$ and $B$ that you started with. For instance, suppose you start the algorithm with $A = 20$, $B = 12$. Then in the first step, $A$ gets replaced by $20 - 12 = 8$, so $8$ becomes the new $A$. In the second step, $B$ gets replaced by $12 - 8 = 4$, so $4$ becomes the new $B$. In the third step, $A$ gets replaced by $8 - 4 = 4$, so $4$ becomes the new $A$ and the two numbers $A$ and $B$ have become equal. The algorithm yields $4$ as the GCD of $20$ and $12$.

Euclid’s recipe is *formal*, and we can analyze it with formal means. The correctness of Euclid’s algorithm follows from the insight that if you have two numbers $A$ and $B$ with $A$ larger than $B$, and you replace $A$ by $A - B$, then the set of common divisors of the number pair does not change.

Algorithms come in many forms and flavors, for example, sequential and parallel ones. For interesting introductions to algorithms in computer science, see Harel & Feldman (2004) and Miller & Boxer (2012). In a similar manner as these algorithms, social procedures can be analyzed with the formal tools of logic and theoretical computer science.[^note-2]

It appears that most amenable to a formal approach are those social procedures for which one wants to guarantee that given certain starting conditions, the procedure preserves or creates specific desired properties. Examples are social procedures for fair division (Section 2), matching (Section 3), communication (Section 4). Finally, the formal perspective is useful for situations requiring participants’ strategic reasoning (Section 5). A common element is that in all these situations, agents’ knowledge and lack of knowledge of other agents’ mental states play an important role. As a counterpart to the examples in the current article, Van Benthem (2018)[^benthem-2018] provides an intriguing overview about the current roles of social perspectives in computer science itself, highlighting social agency and information.

## 2. Fairness

Formal methods by themselves do not solve philosophical issues, as the following tale from Padma (2007)[^padma-2007] illustrates.

> Two farmers, Ram and Shyam were eating chapatis. Ram had 3 pieces of the flat, round bread and Shyam had 5. A traveller who looked hungry and tired rode up to the two men. Ram and Shyam decided to share their chapatis with him. The 3 men stacked the 8 chapatis (like pancakes) and cut the stack into 3 equal parts. They shared the pieces equally and ate until nothing was left. The traveller, who was a nobleman, was so grateful that he gave the two farmers 8 gold coins for his share of the food.
>
> After the traveller left, Ram and Shyam wondered how they should share the 8 gold coins. Ram said that there were 8 coins and only 2 people, so each person should get an equal share of 4 coins. “But that’s not fair,” said Shyam, “since I had 5 chapatis to begin with.” Ram could see his point, but he didn’t really want to give 5 of the coins to Shyam. So he suggested they go see Maulvi, who was very wise. Shyam agreed.
>
> Ram and Shyam told the whole story to Maulvi. After thinking for a long time, he said that the fairest way to share the coins was to give Shyam 7 coins and Ram only 1 coin. Both men were surprised. But when they asked Maulvi to explain his reasoning, they were satisfied that it was a fair division of the 8 coins.

Here are reasons the participants could have given to explain each mentioned division as being fair:

1. Ram: “If the traveller hadn’t arrived, we would have shared the chapatis equally. So it is only *fair* if we now share the eight coins equally as well.”
2. Shyam: “If the traveller hadn’t arrived, you would have bought one chapati from me at the going rate for chapatis. Now that the traveller was so generous, the going rate suddenly went up to one gold coin for a chapati. So your chapatis turned out to be worth three gold coins and mine five gold coins.”
3. Maulvi: “The traveller has eaten one third of eight chapatis. Ram had only three chapatis to start with, and therefore he has eaten $1/3$ chapati from Ram and $7/3$ chapatis from Shyam. So it is only fair if Ram gets one coin and Shyam gets seven.”

A moral of this could be that there is no obviously correct notion of fairness, in this case, and in many cases. Formal analysis always starts from an intuition and can help to turn that intuition into a more precise definition. Then one can check if a given procedure fits the definition; however, if it fits, that does not show that the definition is right.

### 2.1 Fair Division

Social procedures are as old as the world. *Divide and choose* (also known as “I cut, you choose”) is a procedure for two-person fair division of some desirable or undesirable heterogeneous good. One person divides the good into what she believes to be equal shares, and the other person chooses. If the two participants have different value judgements on parts of the goods, it is possible that both participants feel that they received more than 50 percent of the goods. Indeed, let $X$ be a set representing the good to be divided. A valuation function $V$ for $X$ is a function from ${{\cal P}}(X)$ to $[0,1]$ with the properties that $V(\emptyset) = 0$, $V(X) = 1$, and for all subsets $A$, $B$, it holds that $A \subseteq B \subseteq X$ implies $V(A) \leq V(B)$ (for explanation of notation, see supplement on basic set theory). Suppose $V_m$ and $V_y$ are functions for my and your valuation of the contents of $X$. If $V_m$ and $V_y$ are different, this means that you and I value some items in $X$ differently. It follows, as was already observed by Steinhaus in 1948, that there exists a division that gives both parties more than their due part; “this fact disproves the common opinion that differences in estimation make fair division difficult” (Steinhaus 1948)[^steinhaus-1948].

It matters whether the valuations are known to the other party. Such knowledge can be used to advantage by the one who cuts. First consider the case that your valuation is unknown to me, and vice versa. Then if I cut, the best I can do is pick sets $A, B \subseteq X$ with $A \cap B = \emptyset$, $A \cup B = X$, and $V_m(A) = V_m(B)$. If you choose, you will use $V_y$ to pick the maximum of $\{ V_y(A), V_y(B) \}$. It follows immediately that cutting guarantees a fair share, but no more than that, while choosing holds a promise for a better deal. So if you ever get the choice between cutting and choosing in a situation where both parties only know their own valuation, then it is to your advantage to leave the cutting to the other person.

However, if the valuations are common knowledge (see entry on common knowledge), the situation is reversed, for then it is more advantageous to take the role of cutter. As cutter, you can attempt to make a division intp sets $A$ and $B$ with $A$ slightly more valuable than $B$ according to the valuation of the other party, while $B$ is much more valuable than $A$ according to your own valuation.

The example shows that issues of knowledge and ignorance, are crucial for analysis of fair division protocols. Epistemic logic (see entry on epistemic logic) can shed much light on many subtle aspects of knowledge and ignorance in social interactions, and in particular in fair division problems; for an interesting cake-cutting experiment showing the importance of knowledge and ignorance, see Kyropoulou et al. 2019. Still, in traditional studies of fair division the role of knowledge is not taken into account, as is witnessed by the comprehensive study of “cake cutting algorithms” in Robertson & Webb (1998).

### 2.2 Cutting a Cake Among More than Two Participants

In the social choice literature (Brams 2005; Brams & Taylor 1996)[^brams-2005][^brams-1996] it is common practice to use cake cutting as a metaphor for a *division of a single heterogeneous good*. Dividing a piece of land at inheritance would be an example. The cake has different toppings that cannot all be cut into pieces with the same composition: it may have candied cherries on top that someone likes but another person abhors, and so on. A cake division is *simply fair* if each of $n$ players feels she received at least $1/n$ of the cake, according to her individual valuation of its parts. A procedure may be simply fair without ruling out the possibility of hard feelings. A cake division is called *envy-free* if each person feels that nobody else received a larger piece. A sure sign of a division being envy-free is that nobody wishes to trade pieces with anyone else. It turns out to be very hard to design cake cutting procedures that are both fair and envy-free. The *I cut, you choose* procedure is fair, and it is envy-free simply because the rest of the cake is a single piece, so there is no possibility for envy. See the entry on economics [normative] and economic justice for philosophical discussions of envy-freeness.

R. Parikh (2002)[^parikh-2002] analyzes the so-called Banach-Knaster algorithm for cake cutting when the cake has to be divided fairly among at least three persons, which goes like this:

> I cut a piece intended for myself. All others consider it. If nobody objects, I get my piece. If someone raises an objection, she has the right to cut off a slice and put that back with the rest of the cake. She then asks if she can have the reduced piece. If nobody objects, she gets it, otherwise someone else takes the knife and reduces the piece a bit further, and so on, until someone gets the trimmed piece. Then on to the next round, with $n-1$ players. When two players are left, they use the *Divide and choose* algorithm.

Parikh’s discussion shows how the methods of theoretical computer science can be used to argue that the procedure is fair. The key ingredient of the procedure is a loop operation:

> Continue to trim the piece until there are no further objections about the size.

Suppose $r$ stands for the action of trimming a piece of cake and putting it back with the main part of the cake, according to the Banach-Knaster algorithm, and suppose $F(m,k)$ is the proposition that the main part of the cake is large enough for $k$ people. Then surely $F(m,n)$ holds at the beginning: the whole cake is large enough for the whole group to begin with. Moreover, Parikh (1983, 2002)[^parikh-2002][^parikh-1983] uses his game logic to prove that $F(m,k)$ is invariant under the action $r$: If $F(m,k)$ is true before $r$, then it will still be true after $r$ has occurred. Clearly, if one can show that $F(m,k)$ continues to hold through the algorithm, for $k$ running through $n, \ldots, 1$, then this establishes that the division is fair.[^note-3]

### 2.3 Solomon’s Judgement

A variation on *Divide and choose* was played by King Solomon in the famous Judgement of Solomon, in a dispute among two women who both claimed to be the mother of a child. The full story is in 1 Kings 3:16–28. Two women who lived in the same house both had an infant son. One of the women claimed that the other woman had stolen her child, after accidentally smothering her own son during sleep. The other woman denied this and reversed the charge. After hearing their stories, King Solomon called for a sword and declared that there was only one fair solution: cut the living child in two and give both women half of it. Upon hearing this, the true mother cried out that she was willing to give up the child if it could be spared, while the fake mother agreed with the judgement. This behaviour revealed to Solomon who was the real mother, and her child was given back to her.

This procedure is not repeatable. As the Bible story puts it:

> And all Israel heard of the judgment which the king had judged; and they feared the king; for they saw that the wisdom of God was in him, to do justice.

Obviously, in a second similar dispute, both women would exclaim “Give it to her, but let it live!”

Solomon’s handling of the situation can be turned into a social procedure that is repeatable, as follows. Solomon does not call for a sword, but instead explains to the two women the following procedure. First he is going to ask the first woman if she is willing to give up the child. If the answer is “yes”, the dispute is resolved, with no further questions asked. Otherwise he will ask the other woman if she is willing to give up the child. Again, if the answer is “yes” the dispute is resolved. If they both refuse, then the child is his, and then he will allow one of the women to buy it back, at a price that is to be determined as follows. They will both write an amount of money on a sheet of paper, without their names. If the two bids are $A$ and $B$, then the price of the child is set at $\frac{A + B}{2}$, and fate will determine which woman is going to get the child at that price, where the other woman has to pay a small fine. If the two women are rational, one of them will give up the child when being first asked (see Moore 1992 and Pauly 2005; for philosophical discussions of rationality, see the entries on practical reason & game theory and ethics)[^moore-1992][^pauly-2005].

Both Moore (1992)[^moore-1992] and Pauly (2005)[^pauly-2005] discuss the importance of reasoning about common knowledge and ignorance in the King Solomon cases. For example, King Solomon is ignorant of who is the real mother, but both women commonly know from the start who is the true mother, and that the true mother will therefore bid much higher than the other one. This makes the procedure safe. Again, epistemic logic and in particular common knowledge help to shed light on a tricky social procedure. For a more traditionally philosophical introduction to the fair division problem, including more extensive explanations of fairness, manipulability and envy-freeness, see the entry on economics [normative] and economic justice.

The next section shows that the perspective of social software can also shed light on social matching problems. These range from marriages to the assignment of resident doctors to hospitals, college admission procedures, and the assignment of students to housing.

## 3. The Stable Marriage Problem

Suppose equal sets of men and women are given, all of them seeking to marry someone of the opposite gender, and each man has listed his preferences for the women by means of a strict ordering, and similarly for each woman. A *stable marriage match* is a one-to-one mapping between the men and women with the property that if a man prefers another woman over his own wife, then that woman does *not* prefer him to her own husband, and if a woman prefers another man over her own husband, then that man does *not* prefer her to his own wife.

### 3.1 The Gale-Shapley Algorithm

The computer scientists Gale and Shapley proved that stable matchings always exist, and gave an algorithm for finding such matchings, the so-called Gale-Shapley algorithm (Gale & Shapley 1962)[^gale-1962]:

> Initially, all men and all women are free (unengaged).
>
> Next, in a number of rounds, each free man proposes to the most-preferred woman to whom he has not yet proposed and ticks her off from his list. If the woman is free, she accepts, and they become engaged. If the woman is not free, she compares the proponent to her current fiancé. If she likes him better, she dumps the fiancé who becomes free again, and the proponent and his woman of choice become engaged.
>
> This goes on until all men and women are engaged.

As an example, suppose that there are three men $a, b, c$ and three women $d, e, f$, and the lists of preferences are as follows (with the most preferred one first in the list): $a: edf$, $b: {\it fed}$, $c: {\it dfe}$, $d: {\it abc}$, $e: {\it cda}$, $g: {\it acb}$. So $a: {\it edf}$ means that $a$ prefers $e$ to $d$ and $d$ to $f$. It is assumed that preferences are transitive, so $a$ also prefers $e$ to $f$.

An example of a stable match for this situation is represented as three pairs $(a,e)$, $(b,f)$, $(c,d)$. Note that woman $d$ ends up with the man that is at the bottom of her list. But this match is still stable, for although $c$ is willing to swap her husband for any of the other two men, these two candidates will not agree, for they both happen to be married to the woman who is on the top of their own list.

To check that the Gale-Shapley algorithm always produces stable matchings, we can proceed as follows. Obviously, the situation where no-one is engaged is stable.

What does it mean for $E$, an “engagement” mapping, to be stable on the set of women $W$ and the set of men $M$? Let us use $m >_w m'$ for “$w$ prefers $m$ over $m'$” (so bigger is better).

**(1)**

For all $(m,w) \in E$: if there is $w'$ with $w' >_m w$ then there is no $m'$ with $(m',w') \in E$ and $m >_{w'} m'$;

**(2)**

For all $(m,w) \in E$: if there is $m'$ with $m' >_w m$ then there is no $w'$ with $(m',w') \in E$ and $w >_{m'} w'$.

What does it mean for a man to be *free*?

**(3)**

The set of free men should equal the set of all men minus the men that are engaged.

Next, inspect what happens in a single step in the algorithm. The precondition for the step is that there is at least one free man $m$ left. Such a free man $m$ proposes to the highest woman $w$ on his list to whom he has not yet proposed.

There are two cases. If $w$ is free, $w$ accepts the proposal, and they become engaged. Is the new set of engaged pairs stable? We only have to check for the new pair $(w,m)$.

- Suppose that there is a free $w'$ with $w' >_m w$. This cannot be, for $w$ is at the top of $m$'s list.
- Suppose there is $m'$ with $m' >_w m$. Then if $m'$ is engaged, let us say to $w'$, this must mean that not $w >_{m'} w'$. For otherwise $m'$ would have proposed to $w$ instead of to $w'$.
- The new list of free men equals the old list, minus $m$. This is correct, for $m$ just got engaged.

Now the other case: suppose that $w$ is already engaged. There are two subcases. In case $w$ prefers her own current fiancé, nothing happens. The resulting list of engaged pairs is still stable. The list of free men remains the same, for $m$ proposed and got rejected.

In case $w$ prefers $m$ to her own fiancé $m'$, she swaps: $(m,w)$ replaces $(m',w)$ in the set of engaged pairs. Again, it is easy to see that the resulting list of engaged pairs is stable. Man $m$ gets replaced by $m'$ in the set of free men. This is also correct.

Note that the Gale-Shapley matching algorithm is hugely favourable to the party that is doing the proposing. The proposing party gets a chance to make proposals to any candidate, in order of preference. But at the start of the procedure the receiving party has to say “yes” to any proposal! The result of swapping the roles of the men and the women in the algorithm will also compute a stable match, but one that is more advantageous to the women.

The Gale-Shapley procedure runs in time quadratic in the number of men and women (see, e.g., Cechlérová et al. 2005)[^cechlérová-2005]. Pini et al. (2011) show how participants can easily manipulate the outcome of the procedure by misrepresenting their true preferences. Fortunately, Pini et al. also present an alternative procedure for which manipulation is hard, in that coming up with an individually profitable misrepresentation of one’s preferences is a computationally complex task.

The Gale-Shapley algorithm has many important applications, also outside of the area of marriage brokering; Gale and Shapley themselves discuss college admission procedures (1962). The next subsection presents another application.

### 3.2 A University Housing Assignment Procedure

Using the perspective of social software, Parikh and Pauly (2012) investigate a variant of the Gale-Shapley algorithm that is used in the Stanford Housing Draw to assign students to rooms. The situation is more complex than in the marriage setting, because students do not give a complete order on all houses, but only on 8 of them; moreover, they may choose to enter the Draw in groups. In the housing context, the students turn out to have an incentive to honestly submit their true preferences: the draw is *non-manipulable* for them. However, in theory they could still strategize about choosing the subset of 8 houses on which they submit their preferences.

The issue of knowledge is interesting in this case. Even though the algorithm can be found on the Stanford webpages, most students and administrators do not fully understand how it works. Therefore, the Stanford Housing Draw cannot be assumed as common knowledge among the students. An interesting phenomenon seems to occur: even while admitting not to understand the algorithm, most students would say that they believe it to be fair (Parikh & Pauly 2012)[^parikh-2012].

## 4. The Logic of Communication

Communication protocols are important in distributed computing: computing with distributed systems, where a distributed system is a set of computers that are connected through a communication network. Communication protocols are also interesting from a philosophical perspective, especially in the context of discussions of the value of privacy (see entries on privacy and computing and moral responsibility). The formal approach can help in answering philosophical questions such as “Does more security automatically lead to less privacy?”.

### 4.1 Communication and Distributed Computing

In the following example, the inspiration does not only flow from social problems to formal solutions, but also the other way, from successful social practices to formal procedures. Many algorithms for distributed computing are related to social protocols for communication in everyday life. An example is the use of a “talking stick” to regulate discussion and decision making in a group of peers, with the rules that the talking stick gets passed around and only the person who is holding the stick is allowed to talk (Nerburn 1999)[^nerburn-1999].

A computer communication protocol based on this social procedure is the token ring protocol. A *token ring* in distributed computing is a network where each computer is connected to exactly two other computers in such a way that each computer is reachable in the network, and where a single “token” circulates around the ring-shaped network. Communication can only be initiated by the current owner of the token.

Sometimes the token gets lost through computer or network failure. In such cases the token has to be regenerated, with a guarantee that only one computer has the token. This problem of regenerating the token in a token ring is called the *leader election problem*. Here is an algorithm for it:

> Assume that communication takes place clockwise, and each computer can distinguish its clockwise neighbour from its counterclockwise neighbour. Assume that all computers have different identifiers (positive whole numbers) and each computer knows its identifier.
>
> Each computer sends its identifier around the ring. When a computer $c$ receives an identifier, $c$ compares it to its own. If the identifier is greater than its own, $c$ passes it on. If it is less than its own, $c$ discards it. If it is equal to its own, $c$ declares itself to be the leader.

It is not hard to see that this guarantees the computer with the highest identifier $i_{\text{max}}$ to become the leader (see Lynch 1996)[^lynch-1996]. No assumptions need to be made about the number of computers in the ring, nor about any computer knowing anything about the size of the ring or the identifiers of the other computers. A next stage of the protocol could be for the leader to send around a request to register as non-leader and halt.

One further level of abstraction is from distributed computers or processes to interacting intelligent agents, or multi-agent systems. These agents can be computers, robots, humans, teams of humans, or some mix of these. It is commonly assumed that the agents have a degree of autonomy, that the agents have a restricted local view of the system as a whole, and that there is no designated controller of the whole system (see Wooldridge 2002 [2009])[^wooldridge-2002].

### 4.2 Common Knowledge and Social Procedures

Many social procedures are designed to create common knowledge (Lewis 1969; van Ditmarsch et al. 2009; and entry on common knowledge)[^ditmarsch-2009][^lewis-1969]. The old-fashioned ritual that takes place when you withdraw a large amount of money from your bank account and have it paid out to you in cash by the cashier is an example.

How and whether common knowledge can be achieved depends on available communication facilities. Public announcement or publicly observable ritual (the cashier ritual mentioned above) can create common knowledge. But, as Halpern and Moses (1984) proved, message exchange in a distributed environment, where there is no guarantee that messages get delivered, cannot. Halpern and Moses use the example of two generals who are planning a coordinated attack on a city. The generals are on two hills on opposite sides of the city, each with their own army, and they know that they can only succeed in capturing the city if their two armies attack at the same time. But the valley that separates the two hills is in enemy hands, and any messengers that are sent from one army base to the other run a severe risk to get captured. The generals have agreed on a joint attack, but still have to settle the time. So the generals start sending messages, for example, “Let’s attack at 9:00 AM”. But they cannot be sure that the messengers succeed in delivering their message. And if they get through, there is no guarantee that the message of acknowledgement will get delivered. And so on.

Even if common knowledge is sometimes hard to achieve in practice, it serves as necessary presumption in regulating society. Roman lawgivers found out long ago that if citizens within their jurisdiction could plead innocence because of being unaware of the law, no offender could ever get convicted. So they invented principles like *Ignorantia legis neminem excusat*, “ignorance of the law excuses no one”. Societies that abide by the rule of law have to be organized in such a way that citizens *in principle* are in a position to know the law. The laws have to be properly published and distributed, for example, by being printed in a government gazette to which every citizen has access.

In his book “Rational Ritual” (2001), Michael Suk-Young Chwe points out the importance of the *size* of groups for which common knowledge gets established. A brand name that is common knowledge in a large group is worth a lot of money. Chwe analyzes the example of advertisements broadcasted during the American football Super Bowl. He compares the enormous cost of making something common knowledge by means of such advertisements to the obvious benefits. Part of the benefit is in the fact that the advertisements create common knowledge. An important consideration when deciding to buy a smartphone of a particular brand, for example, is the knowledge that others are going to buy the same model too.

Of course in many social situations, you may want to *prevent* common knowledge from arising, for example, if you want to keep a secret from certain others. There are also more interesting cases where everybody knows some fact, for example that a particular country possesses nuclear weapons, but where it would lead to political problems to make this fact common knowledge by making a public announcement. For a number of such social situations where maintaining privacy and ignorance are crucial, see van Eijck and Verbrugge (2009). An interesting recent development is the study of dynamic-epistemic logic-based *epistemic planning*, which enables us to synthesize communication protocols in order to create certain exact configurations of levels of higher-order knowledge within a group (Bolander and Andersen 2011, Löwe, Pacuit, and Witzel 2011)[^bolander-2011][^löwe-2011].

## 5. Strategic Reasoning and Cooperation

The large field of game theory is extensively explained in other lemmas in this encyclopedia (see among others the entry on game theory). This field of research has been very active since the appearance of the seminal book (Von Neumann and Morgenstern 1944)[^von-1944]. Similarly, social choice theory and in particular voting theory (see entries on social choice theory and voting methods) were already thriving fields of research long before the term social software came along.

It is useful to investigate how formal methods and an algorithmic perspective can help solve societal problems. For example, in the case of the famous prisoner’s dilemma (see entry on prisoner’s dilemma) it is interesting to try to design policies that make cheating the other agent less profitable by penalizing it. Notice that this “social software engineering” takes place at the meta-level, on top of the level of the prisoners choosing their strategies (van Eijck 2015)[^eijck-2015].

A related recent trend in game theory that is relevant for social software, is to step away from solution concepts such as the Nash equilibrium and instead to focus on the process of rational deliberation: the “theory of play” (see van Benthem, Pacuit and Roy, 2011, as well as the entry logics for analyzing games)[^benthem-2011]. This type of research delineates both the normative principles guiding the players’ strategic reasoning, and the psychological phenomena explaining the differences between predicted and observed behavior in games (Camerer 2003; Ghosh and Verbrugge 2018; Pacuit 2015; Meijering et al. 2012, 2014; Top et al. 2018)[^camerer-2003][^ghosh-2018][^meijering-2012][^meijering-2014][^pacuit-2015][^top-2018].

In Section 4.2 we briefly discussed the role of the study of knowledge and belief when analyzing social procedures. In this vein, the field of epistemic game theory focuses on agents’ beliefs about other agents’ strategies and those agents’ beliefs about other agents’ strategies, and so on, up to the idealized case of common knowledge among a group of agents that they are all rational (see the entry on epistemic foundations of game theory; Perea 2012; Brandenburger 2014)[^brandenburger-2014][^perea-2012].

It turns out that in voting theory in particular, it is useful to design a logic to explicitly model the knowledge that agents bring to bear when they are voting. It is especially interesting to model what happens in a group when agents vote strategically by misrepresenting their own preferences in order to manipulate the outcome (van Eijck 2015; van Ditmarsch et al. 2012)[^ditmarsch-2012][^eijck-2015].

In recent years in the research area of multi-agent systems, formal approaches to social procedures have also been used to help design actual software, for example for cooperative problem solving in teams, coalition formation, knowledge fusion, auctions, and negotiations among software agents (Bulling et al. 2015; Chalkiadakis et al. 2011; Dunin-Kęplicz and Verbrugge 2010; Pauly 2002; Shoham and Leyton-Brown 2009; Vazirani et al. 2007)[^bulling-2015][^chalkiadakis-2011][^dunin-kęplicz-2010][^pauly-2002][^shoham-2009][^vazirani-2007]. This literature is mostly normative in nature.

In contrast, another fascinating area of research, evolutionary game theory (see entry on evolutionary game theory), investigates how features like altruism, social norms, moral behavior and cooperation could actually have evolved. This area combines both normative and descriptive work (Axelrod 1984; Bowles and Gintis 2011; Sigmund 2010)[^axelrod-1984][^bowles-2011][^sigmund-2010]. As a particular social software contribution to this area, Gärdenfors (2012)[^gärdenfors-2012] characterized how much cognition and communication are required for several kinds of cooperation, from simple flocking behavior, through reciprocal altruism (“I’ll scratch your back if you scratch mine”), up to fully fledged teamwork.

## 6. Conclusion

In conclusion, the formal perspective on social procedures and intelligent interaction, which emphasizes algorithms and information, has produced a wide variety of important insights. It has also led to interesting philosophical discussions. The main challenge for the future appears to be to unify this currently relatively scattered field, in which many contributors do not seem to be aware of relevant work in other subfields.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

### General References

### Fairness

### The Stable Marriage Problem

### The Logic of Communication

### Strategic Reasoning and Cooperation

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=social-procedures). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/social-procedures/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=social-procedures&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/social-procedures/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

### Conference Series

- [AAMAS: Autonomous Agents and Multiagent Systems](http://www.ifaamas.org/).
- [TARK: Theoretical Aspects of Rationality and Knowledge](http://www.tark.org/).
- [LORI: Workshops on Logic, Rationality, and Interaction](http://golori.org/)
- [LOFT: Logic and the Foundations of Game and Decision Theory](http://www.econ.ucdavis.edu/faculty/bonanno/loft.html).

### Other Sites

- [Games, Action and Social Software: ESSLLI 2009 Course by Jan van Eijck and Rineke Verbrugge](https://rinekeverbrugge.nl/teaching/)
- [Logics of Rational Agency: NASSLLI 2010 course by Eric Pacuit](http://ai.stanford.edu/~epacuit/lograt/nasslli2010.html)
- [ A Discrete and Bounded Envy-Free Cake Cutting Protocol: Presentation by Haris Aziz and Simon Mackenzie](https://www.youtube.com/watch?v=jGiAckY00ik)
- [Preprint of the full version of the article on Fair Cake-Cutting in Practice by Kyropoulou et al., 2019; revised 2022](https://arxiv.org/abs/1810.08243)
- [Interactive demo of the Gale-Shapley algorithm for stable matching](http://mathsite.math.berkeley.edu/smp/smp.html)
- [Video of the token ring protocol](https://www.youtube.com/watch?v=rMWH21f7b2Q)

## Related Entries

altruism: biological | Arrow’s theorem | belief merging and judgment aggregation | common knowledge | computability and complexity | computing: and moral responsibility | economics [normative] and economic justice | epistemology: social | game theory | game theory: and ethics | game theory: epistemic foundations of | game theory: evolutionary | justice: transitional | logic: action | logic: epistemic | logic: for analyzing games | logic: paraconsistent | practical reason | prisoner’s dilemma | privacy | redistribution | social choice theory | social institutions | social norms | technology, philosophy of | voting: methods

## Acknowledgments

I would like to express my gratitude to Jan van Eijck for the enjoyable time of writing the first 2014 version of this article together. Thanks are also due to two anonymous referees for suggesting several improvements and additions for this updated version. Because of Jan’s retirement a few years ago, the 2019 update of the article has been made by me (Rineke Verbrugge) and I therefore bear sole responsibility for any remaining infelicities; please let me know if you spot any.

## Notes（原文脚注）

[^note-1]: “Social software” is also used as a name for Internet communication applications like MSN Messenger, Twitter, and Skype. This is not what this entry is about. And what is sometimes called “social software engineering” is again something different: it is a name for the subdiscipline of software engineering that studies its aspect of social interaction.

[^note-2]: Başkent (2017)[^başkent-2017][^başkent-2017-2] convincingly argues that it is useful to look beyond classical logic only when analyzing social procedures. He shows that for some examples’s from Parikh’s work on social software, a para-consistent logic provides a useful perspective (see also entry on paraconsistent logic).

[^note-3]: Parikh (2002)[^parikh-2002] notes:

> Another property which holds is that if $F(m, k + 1)$ is true then it can be true that after the action $c$, of cutting a slice from the cake, the remaining main part is big enough for $k$ people and the slice itself is big enough for one. Note the contrast, that the action $r$ preserves $F(m, k)$ regardless of how $r$ is performed whereas the action $c$, of cutting the cake, may yield the desired outcome but need not.

[^başkent-2017]: Başkent, C., L.S. Moss, and R. Ramanujam, (eds.), 2017, *Rohit Parikh on Logic, Language and Society* (Outstanding Contributions to Logic: Volume 11), Berlin: Springer.

[^başkent-2017-2]: Başkent, C., 2017, “A Non-Classical Logical Approach to Social Software”, in Başkent, Moss, & Ramanujam 2017, pp. 91–110.

[^benthem-2018]: van Benthem, J., 2018, “Computation as Social Agency: What, How and Who”, *Information and Computation*, 261: 519–535.

[^eijck-2017]: Eijck, J. van, and Ph. Elsas, 2017, “What Is Money?”, in Başkent, Moss, & Ramanujam 2017, pp. 67–76.

[^eijck-2009]: Eijck, J. van, and R. Verbrugge (eds.), 2009, *Discourses on Social Software* (Texts in Logic and Games: Volume 5), Amsterdam: Amsterdam University Press.

[^eijck-2012]: ––– (eds.), 2012, *Games, Actions and Social Software: Multidisciplinary Aspects* (Lecture Notes in Computer Science: Volume 7010), Berlin: Springer.

[^harel-2004]: Harel, D., and Y.A. Feldman, 2004, *Algorithmics: The Spirit of Computing*, London: Pearson Education.

[^miller-2012]: Miller, R., and L. Boxer, 2012, *Algorithms Sequential & Parallel: A Unified Approach*, Boston, MA: Cengage Learning.

[^pacuit-2005]: Pacuit, E., 2005, *Topics in Social Software: Information in Strategic Situations*, Ph.D. thesis, New York: City University of New York.

[^parikh-2002]: Parikh, R., 2002, “Social Software”, *Synthese*, 132: 187–211.

[^parikh-2017]: –––, 2017, “Is There a Church-Turing Thesis for Social Algorithms?”, in A. Bokulich and J. Floyd (eds.), *Philosophical Explorations of the Legacy of Alan Turing*, (Boston Studies in the Philosophy of Science, Volume 324), Berlin: Springer, pp. 339–357.

[^pauly-2001]: Pauly, M., 2001, *Logic for Social Software*, Ph.D. thesis, Amsterdam: ILLC.

[^brams-2005]: Brams, S., 2005, “Fair Division”, in B.R. Weingast and D. Witteman (eds.), *Oxford Handbook of Political Economy*, Oxford: Oxford University Press, pp. 425–437.

[^brams-1996]: Brams, S., and A. Taylor, 1996, *Fair Division: From Cake-Cutting to Dispute-Resolution*, Cambridge: Cambridge University Press.

[^kyropoulou-2019]: Kyropoulou, M., J. Ortega, and E. Segal-Halevi, 2019, “Fair Cake-Cutting in Practice”, in *Proceedings of the 2019 ACM Conference on Economics and Computation*, ACM Press, pp. 547–548.

[^moore-1992]: Moore, J., 1992, “Implementation, Contracts, and Renegotiation in Environments with Complete Information”, in J.-J Laffont (ed.), *Advances in Economic Theory — 6ᵗʰ World Congress* (Volume 1), Cambridge: Cambridge University Press.

[^padma-2007]: Padma, T., 2007, *Mathematwist: Number Tales from Around the World*, Chennai: Tulika Publishers.

[^parikh-1983]: Parikh, R., 1983, “Propositional Game Logic”, in *24ᵗʰ Annual Symposium on Foundations of Computer Science*, Washington, DC: IEEE Computer Society, pp. 195–200.

[^pauly-2005]: Pauly, M., 2005, “Changing the Rules of Play”, *Topoi*, 24(2): 209–222.

[^robertson-1998]: Robertson, J., and W. Webb, 1998, *Cake-Cutting Algorithms: Be Fair If You Can*, Boca Raton, FL: A.K. Peters.

[^steinhaus-1948]: Steinhaus, H., 1948, “The Problem of Fair Division”, *Econometrica*, 16: 101–104.

[^gale-1962]: Gale, D., and L. Shapley, L., 1962, “College Admissions and the Stability of Marriage, *American Mathematical Monthly*, 69: 9–15.

[^cechlérová-2005]: Cechlérová, K., and D.F. Manlove, 2005, “The Exchange-Stable Marriage Problem”, *Discrete Applied Mathematics*, 152(1–3): 109–122.

[^parikh-2012]: Parikh, R., and M. Pauly, 2012, “What is Social Software?”, in van Eijck and Verbrugge 2012: 3–14.

[^pini-2011]: Pini, M. S., F. Rossi, K.B. Venable, and T. Walsh, 2011, “Manipulation complexity and gender neutrality in stable marriage procedures”. *Autonomous Agents and Multi-Agent Systems*, 22(1): 183–199.

[^bolander-2011]: Bolander, T., and M.B. Andersen, 2011, “Epistemic Planning for Single-and Multi-Agent Systems”, *Journal of Applied Non-Classical Logics*, 21(1): 9–34.

[^chwe-2001]: Chwe, M. S.-Y., 2001, *Rational Ritual*, Princeton and Oxford: Princeton University Press.

[^ditmarsch-2009]: van Ditmarsch, H., J. van Eijck, and R. Verbrugge, 2009, “Common Knowledge and Common Belief”, in J. van Eijck and R. Verbrugge (eds.), *Discourses on Social Software*, (Texts in Logic and Games), Amsterdam: Amsterdam University Press, pp. 99–122.

[^eijck-2009-2]: van Eijck, J., and R. Verbrugge, 2009, “Eating from the Tree of Ignorance”, in J. van Eijck and R. Verbrugge (eds.), *Discourses on Social Software* (Texts in Logic and Games), Amsterdam: Amsterdam University Press, pp. 184–198.

[^halpern-1984]: Halpern, J., and Y. Moses, 1984, “Knowledge and Common Knowledge in a Distributed Environment”, in *Proceedings of the 3rd ACM Symposium on Principles of Distributed Computing (PODS)*, pp. 50–61; revised, *Journal of the ACM*, 37/3 (1990): 549–587.

[^lewis-1969]: Lewis, D., 1969, *Convention: A Philosophical Study*, Cambridge, MA: Harvard University Press.

[^löwe-2011]: Löwe, B., E. Pacuit, and A. Witzel, 2011, “DEL Planning and Some Tractable Cases”, in Proceedings International Workshop on Logic, Rationality and Interaction (LORI), Berlin, Heidelberg: Springer, pp. 179–192.

[^lynch-1996]: Lynch, N., 1996, *Distributed Algorithms*, San Mateo, CA: Morgan Kaufmann.

[^nerburn-1999]: Nerburn, K., 1999, *The Wisdom of the Native Americans*, Novato, CA: New World Library.

[^wooldridge-2002]: Wooldridge, M., 2002 [2009], *An Introduction to Multi-Agent Systems*, first edition, Chichester: John Wiley and Sons; second edition 2009.

[^axelrod-1984]: Axelrod, R., 1984, *The Evolution of Cooperation*, New York: Basic Books.

[^benthem-2015]: Benthem, J. van, S. Ghosh, and R. Verbrugge (eds.), 2015, *Models of Strategic Reasoning: Logics, Games, and Communities* (FoLLI Publications on Logic, Language and Information, LNCS 8972), Berlin: Springer.

[^benthem-2011]: Benthem, J. van, E. Pacuit, and O. Roy, 2011, “Toward a Theory of Play: A Logical Perspective on Games and Interaction”, *Games*, 2(1): 52–86.

[^bowles-2011]: Bowles, S., and H. Gintis, 2011, *A Cooperative Species: Human Reciprocity and its Evolution*, Princeton and Oxford: Princeton University Press.

[^brandenburger-2014]: Brandenburger, A., 2014, *The Language of Game Theory: Putting Epistemics into the Mathematics of Games*, Singapore: World Scientific.

[^bulling-2015]: Bulling, N., and V. Goranko, 2015, “Logics for Reasoning About Strategic Abiliies in Multi-Player Games”, in van Benthem, Ghosh, & Verbrugge 2015: 93–136.

[^camerer-2003]: Camerer, C.F., 2003, *Behavioral Game Theory: Experiments on Strategic Interaction*, Princeton: Princeton University Press.

[^chalkiadakis-2011]: Chalkiadakis, G., E. Elkind, and M. Wooldridge, 2011, *Computational Aspects of Cooperative Game Theory* (Synthesis Lectures on Artificial Intelligence and Machine Learning: Volume 5), San Rafael, CA: Morgan and Claypool Publishers.

[^ciná-2016]: Ciná, G., and U. Endriss, 2016, “Proving Classical Theorems of Social Choice Theory in Modal Logic”, *Autonomous Agents and Multi-Agent Systems*, 30(5): 963–989.

[^ditmarsch-2012]: Ditmarsch, H. van, J. Lang, and A. Saffidine, 2012, “Strategic Voting and the Logic of Knowledge”, in *Proceedings of the 11th International Conference on Autonomous Agents and Multiagent Systems (AAMAS’12)*, vol. 3, pp. 1247–1248.

[^dunin-kęplicz-2010]: Dunin-Kęplicz, B., and R. Verbrugge, 2010, *Teamwork in Multi-Agent Systems: A Formal Approach*, Chichester: Wiley.

[^eijck-2015]: Eijck, J. van, 2015, “Strategies in Social Software”, in van Benthem, Ghosh, & Verbrugge 2015: 292–317.

[^gärdenfors-2012]: Gärdenfors, P., 2012, “The Cognitive and Communicative Demands of Cooperation”, in van Eijck and Verbrugge 2012: 164–183.

[^ghosh-2018]: Ghosh, S., and R. Verbrugge, 2018, “Studying Strategies and Types of Players: Experiments, Logics and Cognitive Models”, *Synthese*, 195(10): 4265–4307.

[^grädel-2002]: Grädel, E., W. Thomas, and T. Wilke (eds.), 2002, *Automata Logics, and Infinite Games*, (Lecture Notes in Computer Science 2500), Berlin, Heidelberg: Springer.

[^klein-2017]: Klein, D., and E. Pacuit, 2017, “Focusing on Campaigns”, in Başkent, Moss, & Ramanujam 2017, pp. 77–90.

[^meijering-2012]: Meijering, B., H. van Rijn, N. Taatgen, and R. Verbrugge, 2012,“What Eye Movements Can Tell about Theory of Mind in a Strategic Game”, *PLoS ONE*, 7(9), e45961, doi:10.1371/journal.pone.0045961

[^meijering-2014]: Meijering, B., N. Taatgen, H. van Rijn, and R. Verbrugge, 2014, “Modeling Inference of Mental States: As Simple as Possible, as Complex as Necessary“, *Interaction Studies*, 15(3): 455–477.

[^pacuit-2015]: Pacuit, E., 2015, “Strategic Reasoning in Games”, in van Benthem, Ghosh, & Verbrugge 2015: 3–33.

[^pauly-2002]: Pauly, M., 2002, “A Modal Logic for Coalitional Power in Games”, *Journal of Logic and Computation*, 12: 149–166.

[^perea-2012]: Perea, A., 2012, *Epistemic Game Theory: Reasoning and Choice*, Cambridge: Cambridge University Press.

[^shoham-2009]: Shoham, Y., and K. Leyton-Brown, 2009, *Multiagent Systems: Algorithmic, Game-Theoretic and Logical Foundations*, Cambridge: Cambridge University Press.

[^sigmund-2010]: Sigmund, K., 2010, *The Calculus of Selfishness*, (Princeton Series in Theoretical and Computational Biology), Princeton and Oxford: Princeton University Press.

[^top-2018]: Top, J., R. Verbrugge, and S. Ghosh, 2018, “An Automated Method for Building Cognitive Models for Turn-Based Games from a Strategy Logic”, *Games*, 9(3),44; doi:10.3390/g9030044

[^vazirani-2007]: Vazirani, V.V., N. Nisan, T. Roughgarden, and E. Tardos (eds.), 2007, *Algorithmic Game Theory*, Cambridge: Cambridge University Press.

[^von-1944]: Von Neumann, J., and O. Morgenstern, 1944, *Theory of Games and Economic Behavior*, Chichester: Wiley.
