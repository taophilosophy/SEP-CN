# Logic and Games
**First published Fri Jul 27, 2001; substantive revision Thu Dec 12, 2024**

*Hodges, Wilfrid, Väänänen, Jouko*

Games between two players, of the kind where one player wins and one loses, became a familiar tool in many branches of logic during the second half of the twentieth century. Important examples are semantic games used to define truth, back-and-forth games used to compare structures, and dialogue games to express (and perhaps explain) formal proofs.

## 1. Games in the History of Logic

The links between logic and games go back a long way. If one thinks of a debate as a kind of game, then Aristotle already made the connection; his writings about syllogism are closely intertwined with his study of the aims and rules of debating. Aristotle’s viewpoint survived into the common medieval name for logic: *dialectics*. In the mid twentieth century Charles Hamblin revived the link between dialogue and the rules of sound reasoning, soon after Paul Lorenzen had connected dialogue to constructive foundations of logic.

There are close links between games and teaching. Writers throughout the medieval period talk of dialogues as a way of ‘teaching’ or ‘testing’ the use of sound reasoning. We have at least two textbooks of logic from the early sixteenth century that present it as a game for an individual student, and Lewis Carroll’s *The Game of Logic* (1887) is another example in the same genre. There are plenty of modern examples too, though probably there has not been enough continuity to justify talking of a tradition of teaching logic by games.

Mathematical game theory was founded in the early twentieth century. Although no mathematical links with logic emerged until the 1950s, it is striking how many of the early pioneers of game theory are also known for their contributions to logic: John Kemeny, J. C. C. McKinsey, John von Neumann, Willard Quine, Julia Robinson, Ernst Zermelo and others. In 1953 David Gale and Frank Stewart made fruitful connections between set theory and games. Shortly afterwards Leon Henkin suggested a way of using games to give semantics for infinitary languages.

The first half of the twentieth century was an era of increasing rigour and professionalism in logic, and to most logicians of that period the use of games in logic would probably have seemed frivolous. The intuitionist L. E. J. Brouwer expressed this attitude when he accused his opponents of causing mathematics ‘to degenerate into a game’ (as David Hilbert quoted him in 1927, cited in van Heijenoort 1967)[^hilbert-1967]. Hermann Weyl (cited in Mancosu 1998) used the notion of games to explain Hilbert’s metamathematics: mathematical proofs proceed like plays of a meaningless game, but we can stand outside the game and ask meaningful questions about it. Wittgenstein’s language games provoked little response from the logicians. But in the second half of the century the centre of gravity of logical research moved from foundations to techniques, and from about 1960 games were used more and more often in logical papers.

By the beginning of the twenty-first century it had become widely accepted that games and logic go together. The result was a huge proliferation of new combinations of logic and games, particularly in areas where logic is applied. Many of these new developments sprang originally from work in pure logic, though today they follow their own agendas. One such area is argumentation theory, where games form a tool for analysing the structure of debates.

Below we will concentrate on those games that are most closely associated with pure logic.

## 2. Logical Games

From the point of view of game theory, the main games that logicians study are not at all typical. They normally involve just two players, they often have infinite length, the only outcomes are winning and losing, and no probabilities are attached to actions or outcomes. The barest essentials of a logical game are as follows.

There are two players. In general we can call them $\forall$ and $\exists$. The pronunciations ‘Abelard’ and ‘Eloise’ go back to the mid 1980s and usefully fix the players as male and female making reference easier: her move, his move. Other names are in common use for the players in particular types of logical game.

The players play by choosing elements of a set $\Omega$, called the *domain* of the game. As they choose, they build up a sequence

$$ a_0, a_1, a_2,\ldots $$

of elements of $\Omega$. Infinite sequences of elements of $\Omega$ are called *plays*. Finite sequences of elements of $\Omega$ are called *positions*; they record where a play might have got to by a certain time. A function $\tau$ (the *turn function* or *player function*) takes each position $\mathbf{a}$ to either $\exists$ or $\forall$; if $\tau(\mathbf{a}) = \exists$, this means that when the game has reached $\mathbf{a}$, player $\exists$ makes the next choice (and likewise with $\forall)$. The game rules define two sets $\W_{\forall}$ and $\W_{\exists}$ consisting of positions and plays, with the following properties: if a position $\mathbf{a}$ is in $\W_{\forall}$ then so is any play or longer position that starts with $\mathbf{a}$ (and likewise with $\W_{\exists})$; and no play is in both $\W_{\forall}$ and $\W_{\exists}$. We say that player $\forall$ *wins* a play $\mathbf{b}$, and that $\mathbf{b}$ is a *win* for $\forall$, if $\mathbf{b}$ is in $\W_{\forall}$; if some position $\mathbf{a}$ that is an initial segment of $\mathbf{b}$ is in $\W_{\forall}$, then we say that player $\forall$ *wins already at* $\mathbf{a}$. (And likewise with $\exists$ and $\W_{\exists}$.) So to summarise, a logical game is a 4-tuple $(\Omega , \tau$, $\W_{\forall}$, $\W_{\exists})$ with the properties just described.

We say that a logical game is *total* if every play is in either $\W_{\forall}$ or $\W_{\exists}$, so that there are no draws. Unless one makes an explicit exception, logical games are always assumed to be total. (Don’t confuse being total with the much stronger property of being determined—see below.)

It is only for mathematical convenience that the definition above expects the game to continue to infinity even when a player has won at some finite position; there is no interest in anything that happens after a player has won. Many logical games have the property that in every play, one of the players has already won at some finite position; games of this sort are said to be *well-founded*. An even stronger condition is that there is some finite number $n$ such that in every play, one of the players has already won by the $n$-th position; in this case we say that the game has *finite length*.

A *strategy* for a player is a set of rules that describe exactly how that player should choose, depending on how the two players have chosen at earlier moves. Mathematically, a strategy for $\forall$ consists of a function which takes each position $\mathbf{a}$ with $\tau(\mathbf{a}) = \forall$ to an element $b$ of $\Omega$; we think of it as an instruction to $\forall$ to choose $b$ when the game has reached the position $\mathbf{a}$. (Likewise with a strategy for $\exists$.) A strategy for a player is said to be *winning* if that player wins every play in which he or she uses the strategy, regardless of what the other player does. At most one of the players has a winning strategy (since otherwise the players could play their winning strategies against each other, and both would win, contradicting that $\W_{\forall}$ and $\W_{\exists}$ have no plays in common). Occasionally one meets situations in which it seems that two players have winning strategies (for example in the forcing games below), but closer inspection shows that the two players are in fact playing different games.

A game is said to be *determined* if one or other of the players has a winning strategy. There are many examples of games that are not determined, as Gale and Stewart showed in 1953 using the axiom of choice. This discovery led to important applications of the notion of determinacy in the foundations of set theory (see entry on large cardinals and determinacy). Gale and Stewart also proved an important theorem that bears their name: Every well-founded game is determined. It follows that every game of finite length is determined—a fact already known to Zermelo in 1913. (A more precise statement of the Gale-Stewart theorem is this. A game $G$ is said to be *closed* if $\exists$ wins every play of $G$ in which she hasn’t already lost at any finite position. The theorem states that every closed game is determined. The proof of the theorem is basically easy: Let us call a position winning for $\forall$ if he has a winning strategy starting from this position. Suppose $\forall$ does not have a winning strategy in the game, that is, in the beginning the position is not winning for $\forall$. If the first move is a move of $\forall$, after his move the position is still not winning for him. If the first move is a move of $\exists$, she must have a move after which the position is still not winning for $\forall$, for otherwise the previous position would have been winning for $\forall$. The game goes on in this way infinitely many moves through positions which are not winning for $\forall$. Because the game is closed, $\exists$ wins.)

Just as in classical game theory, the definition of logical games above serves as a clothes horse that we can hang other concepts onto. For example it is common to have some laws that describe what elements of $\Omega$ are available for a player to choose at a particular move. Strictly this refinement is unnecessary, because the winning strategies are not affected if we decree instead that a player who breaks the law loses immediately; but for many games this way of viewing them seems unnatural. Below we will see some other extra features that can be added to games.

The definitions of game and strategy above were purely mathematical. So they left out what is probably the single most important feature of games, which is that people play them (at least metaphorically). The players aim to win, and by studying the strategies open to them we study what behaviour is rational for a person with a particular aim. In most games there are several players, so we can study what is a rational response to somebody else’s behaviour. By restricting the players’ moves and possible strategies, we can study bounded rationality, where an agent has to make rational decisions under conditions of limited information, memory or time.

In short, games are used for modelling rationality and bounded rationality. This is independent of any connection with logic. But some logics were designed for studying aspects of rational behaviour, and in recent years it has become increasingly common to link these logics to suitable games. See Section 5 (‘Semantic games for other logics’) and its bibliography.

But until recently, logical games were connected with rational behaviour in a quite different way. On the surface, the logic in question had no direct connection with behaviour. But logicians and mathematicians noticed that some ideas could be made more intuitive if they were linked to possible aims. For example in many applications of logical games, the central notion is that of a winning strategy for the player $\exists$. Often these strategies (or their existence) turn out to be equivalent to something of logical importance that could have been defined without using games—for example a proof. But games are felt to give a better definition because they quite literally supply some motivation: $\exists$ is trying to win.

This raises a question that is not of much interest mathematically, but it should concern philosophers who use logical games. If we want $\exists$’s motivation in a game $G$ to have any explanatory value, then we need to understand what is achieved if $\exists$ does win. In particular we should be able to tell a realistic story of a situation in which some agent called $\exists$ is trying to do something intelligible, and doing it is the same thing as winning in the game. As Richard Dawkins said, raising the corresponding question for the evolutionary games of Maynard Smith,

> The whole purpose of our search … is to discover a suitable actor to play the leading role in our metaphors of purpose. We … want to say, ‘It is for the good of … ‘. Our quest in this chapter is for the right way to complete that sentence. (*The Extended Phenotype*, Oxford University Press, Oxford 1982, page 91.)

For future reference let us call this the *Dawkins question*. In many kinds of logical game it turns out to be distinctly harder to answer than the pioneers of these games realised. (Marion 2009 discusses the Dawkins question further.)[^marion-2009]

## 3. Semantic Games for Classical Logic

In the early 1930s Alfred Tarski proposed a definition of truth. His definition consisted of a necessary and sufficient condition for a sentence in the language of a typical formal theory to be true; his necessary and sufficient condition used only notions from syntax and set theory, together with the primitive notions of the formal theory in question. In fact Tarski defined the more general relation ‘formula $\phi(x_1 ,\ldots ,x_n)$ is true of the elements $a_1 ,\ldots ,a_n$’; truth of a sentence is the special case where $n = 0$. For example the question whether

‘For all $x$ there is $y$ such that R$(x, y)$’ is true

reduces to the question whether the following holds:

For every object $a$ the sentence ‘There is $y$ such that R$(a, y)$’ is true.

This in turn reduces to:

For every object $a$ there is an object $b$ such that the sentence ‘R$(a, b)$’ is true.

In this example, that’s as far as Tarski’s truth definition will take us.

In the late 1950s Leon Henkin noticed that we can intuitively understand some sentences which can’t be handled by Tarski’s definition. Take for example the infinitely long sentence

For all $x_0$ there is $y_0$ such that for all $x_1$ there is $y_1$ such that … R$(x_0, y_0, x_1, y_1,\ldots)$.

Tarski’s approach fails because the string of quantifiers at the beginning is infinite, and we would never reach an end of stripping them off. Instead, Henkin suggested, we should consider the game where a person $\forall$ chooses an object $a_0$ for $x_0$, then a second person $\exists$ chooses an object $b_0$ for $y_0$, then $\forall$ chooses $a_1$ for $x_1, \exists$ chooses $b_1$ for $y_1$ and so on. A play of this game is a win for $\exists$ if and only if the infinite atomic sentence

$$ \R(a_0, b_0, a_1, b_1,\ldots) $$

is true. The original sentence is true if and only if player $\exists$ has a winning strategy for this game. Strictly speaking, Henkin used the game only as a metaphor, and the truth condition that he proposed was that the skolemised version of the sentence is true, i.e. that there are functions $f_0, f_1,\ldots$ such that for every choice of $a_0, a_1, a_2$ etc. we have

$$ \R(a_0, f_0 (a_0), a_1, f_1 (a_0, a_1), a_2, f_2 (a_0, a_1, a_2),\ldots). $$

But this condition translates immediately into the language of games; the Skolem functions $f_0, f_1,\ldots$ define a winning strategy for $\exists$, telling her how to choose in the light of earlier choices by $\forall$. (It came to light sometime later that C. S. Peirce had already suggested explaining the difference between ‘every’ and ‘some’ in terms of who chooses the object; for example in his second Cambridge Conference lecture of 1898.)

Soon after Henkin’s work, Jaakko Hintikka added that the same idea applies with conjunctions and disjunctions. We can regard a conjunction ‘$\phi \wedge \psi$’ as a universally quantified statement expressing ‘Every one of the sentences $\phi , \psi$ holds’, so it should be for the player $\forall$ to choose one of the sentences. As Hintikka put it, to play the game $G(\phi \wedge \psi), \forall$ chooses whether the game should proceed as $G(\phi)$ or as $G(\psi)$. Likewise disjunctions become existentially quantified statements about sets of sentences, and they mark moves where the player $\exists$ chooses how the game should proceed. To bring quantifiers into the same style, he proposed that the game $G(\forall x \phi(x))$ proceeds thus: player $\forall$ chooses an object and provides a name $a$ for it, and the game proceeds as $G(\phi(a))$. (And likewise with existential quantifiers, except that $\exists$ chooses.) Hintikka also made an ingenious suggestion for introducing negation. Each game G has a *dual game* which is the same as G except that the players $\forall$ and $\exists$ are transposed in both the rules for playing and the rules for winning. The game $G(\neg \phi)$ is the dual of $G(\phi)$.

One can prove that for any first-order sentence $\phi$, interpreted in a fixed structure $A$, player $\exists$ has a winning strategy for Hintikka’s game $G(\phi)$ if and only if $\phi$ is true in $A$ in the sense of Tarski. Two features of this proof are interesting. First, if $\phi$ is any first-order sentence then the game $G(\phi)$ has finite length, and so the Gale-Stewart theorem tells us that it is determined. We infer that $\exists$ has a winning strategy in exactly one of $G(\phi)$ and its dual; so she has a winning strategy in $G(\neg \phi)$ if and only if she doesn’t have one in $G(\phi)$. This takes care of negation. And second, if $\exists$ has a winning strategy for each game $G(\phi(a))$, then after choosing one such strategy $f_a$ for each $a$, she can string them together into a single winning strategy for $G(\forall x \phi(x))$ (namely, ‘Wait and see what element $a \forall$ chooses, then play $f_a$’). This takes care of the clause for universal quantifiers; but the argument uses the axiom of choice, and in fact it is not hard to see that the statement that Hintikka’s and Tarski’s definitions of truth are equivalent is itself equivalent to the axiom of choice (given the other axioms of Zermelo-Fraenkel set theory).

It’s puzzling that we have here two theories of when a sentence is true, and the theories are not equivalent if the axiom of choice fails. In fact the reason is not very deep. The axiom of choice is needed not because the Hintikka definition uses games, but because it assumes that strategies are deterministic, i.e. that they are single-valued functions giving the user no choice of options. A more natural way of translating the Tarski definition into game terms is to use nondeterministic strategies, sometimes called quasistrategies (see Kolaitis 1985 for details)[^kolaitis-1985]. (However, Hintikka 1996 insists that the correct explication of ‘true’ is the one using deterministic strategies, and that this fact vindicates the axiom of choice.)[^hintikka-1996]

Computer implementations of these games of Hintikka proved to be a very effective way of teaching the meanings of first-order sentences. One such package was designed by Jon Barwise and John Etchemendy at Stanford, called ‘Tarski’s World’. Independently another team at the University of Omsk constructed a Russian version for use at schools for gifted children.

In the published version of his John Locke lectures at Oxford, Hintikka in 1973 raised the Dawkins question (see above) for these games. His answer was that one should look to Wittgenstein’s language games, and the language games for understanding quantifiers are those which revolve around seeking and finding. In the corresponding logical games one should think of $\exists$ as Myself and $\forall$ as a hostile Nature who can never be relied on to present the object I want; so to be sure of finding it, I need a winning strategy. This story was never very convincing; the motivation of Nature is irrelevant, and nothing in the logical game corresponds to seeking. In retrospect it is a little disappointing that nobody took the trouble to look for a better story. It may be more helpful to think of a winning strategy for $\exists$ in $G(\phi)$ as a kind of proof (in a suitable infinitary system) that $\phi$ is true.

Later Jaakko Hintikka extended the ideas of this section in two directions, namely to natural language semantics and to games of imperfect information (see the next section). The name *Game-Theoretic Semantics*, GTS for short, has come to be used to cover both of these extensions.

The games described in this section adapt almost trivially to many-sorted logic: for example the quantifier $\forall x_{\sigma}$, where $x_{\sigma}$ is a variable of sort $\sigma$, is an instruction for player $\forall$ to choose an element of sort $\sigma$. This immediately gives us the corresponding games for second-order logic, if we think of the elements of a structure as one sort, the sets of elements as a second sort, the binary relations as a third and so on. It follows that we have, quite routinely, game rules for most generalised quantifiers too; we can find them by first translating the generalised quantifiers into second-order logic.

## 4. Semantic Games with Imperfect Information

In this and the next section we look at some adaptations of the semantic games of the previous section to other logics. In our first example, the logic (the independence-friendly logic of Hintikka and Sandu 1997, or more briefly IF logic)[^hintikka-1997] was created in order to fit the game. See the entry on independence friendly logic and Mann, Sandu and Sevenster 2011 for fuller accounts of this logic.

The games here are the same as in the previous section, except that we drop the assumption that each player knows the previous history of the play. For example we can require a player to make a choice without knowing what choices the other player has made at certain earlier moves. The classical way to handle this within game theory is to make restrictions on the strategies of the players. For example we can require that the strategy function telling $\exists$ what to do at a particular step is a function whose domain is the family of possible choices of $\forall$ at just his first and second moves; this is a way of expressing that $\exists$ doesn’t know how $\forall$ chose at his third and later moves. Games with restrictions of this kind on the strategy functions are said to be of *imperfect information*, as opposed to the games of *perfect information* in the previous section.

To make a logic that fits these games, we use the same first-order language as in the previous section, except that a notation is added to some quantifiers (and possibly also some connectives), to show that the Skolem functions for these quantifiers (or connectives) are independent of certain variables. For example the sentence

$$ (\forall x)(\exists y/ \forall x)R(x, y) $$

is read as: “For every $x$ there is $y$, not depending on $x$, such that $R(x, y)$”.

There are three important comments to make on the distinction between perfect and imperfect information. The first is that the Gale-Stewart theorem holds only for games of perfect information. Suppose for example that $\forall$ and $\exists$ play the following game. First, $\forall$ chooses one of the numbers 0 and 1. Then $\exists$ chooses one of these two numbers. Player $\exists$ wins if the two numbers chosen are the same, and otherwise player $\forall$ wins. We require that $\exists$, when she makes her choice, doesn’t know what $\forall$ chose; so a Skolem function for her will be a constant. (This game corresponds to the IF sentence above with $R$ read as equality, in a structure with a domain consisting of 0 and 1.) It’s clear that player $\exists$ doesn’t have a constant winning strategy, and also that player $\forall$ doesn’t have a winning strategy at all. So this game is undetermined, although its length is only 2.

One corollary is that Hintikka’s justification for reading negation as dualising (‘players swap places’), in his games for first-order logic, doesn’t carry over to IF logic. Hintikka’s response has been that dualising was the correct intuitive meaning of negation even in the first-order case, so no justification is needed.

The second comment is that already in games of perfect information, it can happen that winning strategies don’t use all the available information. For example in a game of perfect information, if player $\exists$ has a winning strategy, then she also has a winning strategy where the strategy functions depend only on the previous choices of $\forall$. This is because she can reconstruct her own previous moves using her earlier strategy functions.

When Hintikka used Skolem functions as strategies in his games for first-order logic, he made the strategies for a player depend only on the previous moves of the other player. (A Skolem function for $\exists$ depends only on universally quantified variables.) Because the games were games of perfect information, there was no loss in this, by the second comment above. But when he moved to IF logic, the requirement that strategies depend only on moves of the other player really did make a difference. Hodges 1997 showed this by revising the notation, so that for example $(\exists y/x)$ means: “There is $y$ independent of $x$, regardless of which player chose $x$”.

Consider now the sentence

$$ (\forall x)(\exists z)(\exists y/x)(x=y), $$

played again on a structure with two elements 0 and 1. Player $\exists$ can win as follows. For $z$ she chooses the same as player $\forall$ chose for $x$; then for $y$ she chooses the same as she chose for $z$. This winning strategy works only because in this game $\exists$ can refer back to her own previous choices. She would have no winning strategy if the third quantifier was $(\exists y/xz)$, again because any Skolem function for this quantifier would have to be constant. The way that $\exists$ passes information to herself by referring to her previous choice is an example of the phenomenon of *signalling*. John von Neumann and Oskar Morgenstern illustrated it with the example of Bridge, where a single player consists of two partners who have to share information by using their public moves to signal to each other.

The third comment is that there is a dislocation between the intuitive idea of imperfect information and the game-theoretic definition of it in terms of strategies. Intuitively, imperfect information is a fact about the circumstances in which the game is played, not about the strategies. This is a very tricky matter, and it continues to lead to misunderstandings about IF and similar logics. Take for example the sentence

$$ (\exists x)(\exists y/ x)(x=y), $$

again played on a structure with elements 0 and 1. Intuitively one might think that if $\exists$ isn’t allowed to remember at the second quantifier what she chose at the first, then she can hardly have a winning strategy. But in fact she has a very easy one: ‘Always choose 0’!

Compared with first-order logic, IF logic is missing a component that the game semantics won’t supply. The game semantics tells us when a sentence is true in a structure. But if we take a formula with $n$ free variables, what does the formula express about the ordered $n$-tuples of elements of the structure? In first-order logic it would define a set of them, i.e. an $n$-ary relation on the structure; the Tarski truth definition explains how. Is there a similar definition for arbitrary formulas of IF logic? It turns out that there is one for the slightly different logic introduced by Hodges 1997, and it leads to a Tarski-style truth definition for the language of that logic. With a little adjustment this truth definition can be made to fit IF logic too. But for both of these new logics there is a catch: instead of saying when an assignment of elements to free variables makes a formula true, we say when a *set* of assignments of elements to free variables, also called *a* ‘team’, makes the formula true. Väänänen 2007 made this idea the basis for a range of new logics for studying the notion of dependence (see entry on dependence logic). In these logics the semantics is defined without games, although the original inspiration comes from the work of Hintikka and Sandu.

In Väänänen’s logics it is easy to see why one needs sets of assignments, i.e. teams. He has an atomic formula, called a *dependence atom* , expressing ‘$x$ is dependent on $y$’, or more exactly, ‘$x$ is totally determined by $y$’. How can we interpret this in a structure, for example the structure of natural numbers? It makes no sense at all to ask for example whether 8 is dependent on 37. But if we have a team X of ordered pairs of natural numbers, it does make sense to ask whether in X the first member of each pair is dependent on the second; the answer Yes would mean that there is a function $f$ such that each pair $(a,b)$ in X has the form $(f(b),b)$. The advantage of this approach, which at least momentarily, abandons the idea of a game, is that it gives rise to an abundance of other new atomic formulas. For example, we can introduce the *inclusion* atomic formula $x\subseteq y$ with the meaning that every value of $x$ in the team occurs also as a value of $y$, or the atomic formula $x\bot y$ with the meaning that the values of $x$ and $y$ are *independent* of each other in the sense that for any two assignments in the team there is a third which takes the value of $x$ from the first and the value of $y$ from the second. If we identify the team in the obvious sense with a database, these atoms appear in database theory as examples of database constraints.

## 5. Semantic Games for Other Logics

Structures of the following kind give rise to interesting games. The structure $A$ consists of a set $S$ of elements (which we shall call *states*, adding that they are often called *worlds*), a binary relation $R$ on $S$ (we shall read $R$ as *arrow*), and a family $P_1 ,\ldots ,P_n$ of subsets of $S$. The two players $\forall$ and $\exists$ play a game G on $A$, starting at a state $s$ which is given them, by reading a suitable logical formula $\phi$ as a set of instructions for playing and for winning.

Thus if $\phi$ is $P_i$, then player $\exists$ wins at once if $s$ is in $P_i$, and otherwise player $\forall$ wins at once. The formulas $\psi \wedge \theta , \psi \vee \theta$ and $\neg \psi$ behave as in Hintikka’s games above; for example $\psi \wedge \theta$ instructs player $\forall$ to choose whether the game shall continue as for $\psi$ or for $\theta$. If the formula $\phi$ is $\Box \psi$, then player $\forall$ chooses an arrow from $s$ to a state $t$ (i.e. a state $t$ such that the pair $(s, t)$ is in the relation $R)$, and the game then proceeds from the state $t$ according to the instructions $\psi$. The rule for $\Diamond \psi$ is the same except that player $\exists$ makes the choice. Finally we say that the formula $\phi$ is *true at s in A* if player $\exists$ has a winning strategy for this game based on $\phi$ and starting at $s$.

These games stand to modal logic in very much the same way as Hintikka’s games stand to first-order logic. In particular they are one way of giving a semantics for modal logic, and they agree with the usual Kripke-type semantics. Of course there are many types and generalisations of modal logic (including closely related logics such as temporal, epistemic and dynamic logics), and so the corresponding games come in many different forms. One example of interest is the computer-theoretic logic of Matthew Hennessy and Robin Milner, used for describing the behaviour of systems; here the arrows come in more than one colour, and moving along an arrow of a particular colour represents performing a particular ‘action’ to change the state. Another example is the more powerful modal $\mu$-calculus of Dexter Kozen, which has fixed point operators; see Chapter 5 of Stirling 2001.

One interesting feature of these games is that if a player has a winning strategy from some position onwards, then that strategy never needs to refer to anything that happened earlier in the play. It’s irrelevant what choices were made earlier, or even how many steps have been played. So we have what the computer scientists sometimes call a ‘memoryless’ winning strategy.

In the related ‘logic of games’, proposed by Rohit Parikh, games that move us between the states are the subject matter rather than a way of giving a truth definition. These games have many interesting aspects. In 2003 the journal *Studia Logica* ran an issue devoted to them, edited by Marc Pauly and Parikh.

Influences from economics and computer science have led a number of logicians to use logic for analysing decision making under conditions of partial ignorance. (See for example the article on epistemic logic.) There are several ways to represent states of knowledge. One is to take them as states or worlds in the kind of modal structure that we mentioned at the beginning of this section. Another is to use IF logic or a variant of it. How are these approaches related? Johan van Benthem 2006 presents some thoughts and results on this very natural question. See also the papers by Johan van Benthem, Krister Segerberg, Eric Pacuit and K. Venkatesh and their references, in Part IV ‘Logic, Agency and Games’ of Van Benthem, Gupta and Parikh 2011 and the entry on logics for analyzing games for a sample of recent work in this area.

## 6. Back-and-Forth Games

In 1930 Alfred Tarski formulated the notion of two structures $A$ and $B$ being *elementarily equivalent*, i.e., that exactly the same first-order sentences are true in $A$ as are true in $B$. At a conference in Princeton in 1946 he described this notion and expressed the hope that it would be possible to develop a theory of it that would be ‘as deep as the notions of isomorphism, etc. now in use’ (Tarski 1946)[^tarski-1946].

One natural part of such a theory would be a purely structural necessary and sufficient condition for two structures to be elementarily equivalent. Roland Fraïssé, a French-Algerian, was the first to find a usable necessary and sufficient condition. It was rediscovered a few years later by the Kazakh logician A. D. Taimanov, and it was reformulated in terms of games by the Polish logician Andrzej Ehrenfeucht. The games are now known as *Ehrenfeucht-Fraïssé* games, or sometimes as *back-and-forth* games. They have turned out to be one of the most versatile ideas in twentieth-century logic. They adapt fruitfully to a wide range of logics and structures.

In a back-and-forth game there are two structures $A$ and $B$, and two players who are commonly called Spoiler and Duplicator. (The names are due to Joel Spencer in the early 1990s. More recently Neil Immerman suggested Samson and Delilah, using the same initials; this places Spoiler as the male player $\forall$ and Duplicator as the female $\exists$.) Each step in the game consists of a move of Spoiler, followed by a move of Duplicator. Spoiler chooses an element of one of the two structures, and Duplicator must then choose an element of the other structure. So after $n$ steps, two sequences have been chosen, one from $A$ and one from $B$:

$$ (a_0 ,\ldots ,a_{n-1} ; b_0,\ldots ,b_{n-1}). $$

This position is a win for Spoiler if and only if some atomic formula (of one of the forms ‘$\R(v_0 ,\ldots ,v_{k-1})$’ or ‘$\mathrm{F}(v_0 ,\ldots ,v_{k-1}) = v_k$’ or ‘$v_0 =v_1$’, or one of these with different variables) is satisfied by $(a_0 ,\ldots ,a_{n-1})$ in $A$ but not by $(b_0 ,\ldots ,b_{n-1})$ in $B$, or vice versa. The condition for Duplicator to win is different in different forms of the game. In the simplest form, $\EF(A, B)$, a play is a win for Duplicator if and only if no initial part of it is a win for Spoiler (i.e. she wins if she hasn’t lost by any finite stage). For each natural number $m$ there is a game $\EF_m (A, B)$; in this game Duplicator wins after $m$ steps provided she has not yet lost. All these games are determined, by the Gale-Stewart Theorem. The two structures $A$ and $B$ are said to be *back-and-forth equivalent* if Duplicator has a winning strategy for $\EF(A, B)$, and *m-equivalent* if she has a winning strategy for $\EF_m (A, B)$.

One can prove that if $A$ and $B$ are $m$-equivalent for every natural number $m$, then they are elementarily equivalent. In fact, if Eloise has a winning strategy $\tau$ in the Hintikka game G$(\phi)$ on $A$, where the nesting of quantifier scopes of $\phi$ has at most m levels and Duplicator has a winning strategy $\varrho$ in the game $\EF_m (A, B)$, the two strategies $\tau$ and $\varrho$ can be composed into a winning strategy of Eloise in G$(\phi)$ on $B$. On the other hand a winning strategy for Spoiler in $\EF_m (A, B)$ can be converted into a first-order sentence that is true in exactly one of $A$ and $B$, and in which the nesting of quantifier scopes has at most $m$ levels. So we have our necessary and sufficient condition for elementary equivalence, and a bit more besides. For a comparison between the back-and-forth game, the semantic game, and the forcing game (see 7.1 below), see Väänänen 2023. As it turns out and can be indeed expected, these games have a strong sense of similarity which can be manifested by establishing translations between strategies in the three games.

The famous Lindström’s Theorem (see entry on model theory) uses fundamental properties of the game $\EF_m (A, B)$to give a model theoretic characterization of first order logic: the maximal logic satisfying the Compactness Theorem and the Downward Löwenheim-Skolem Theorem.

If $A$ and $B$ are back-and-forth equivalent, then certainly they are elementarily equivalent; but in fact back-and-forth equivalence turns out to be the same as elementary equivalence in an infinitary logic which is much more expressive than first-order logic. There are many adjustments of the game that give other kinds of equivalence. For example Barwise, Immerman and Bruno Poizat independently described a game in which the two players have exactly $p$ numbered pebbles each; each player has to label his or her choices with a pebble, and the two choices in the same step must be labelled with pebbles carrying the same number. As the game proceeds, the players will run out of pebbles and so they will have to re-use pebbles that were already used. The condition for Spoiler to win at a position (and all subsequent positions) is the same as before, except that only the elements carrying labels at that position count. The existence of a winning strategy for Duplicator in this game means that the two structures agree for sentences which use at most $p$ variables (allowing these variables to occur any number of times).

The theory behind back-and-forth games uses very few assumptions about the logic in question. As a result, these games are one of the few model-theoretic techniques that apply as well to finite structures as they do to infinite ones, and this makes them one of the cornerstones of theoretical computer science. One can use them to measure the expressive strength of formal languages, for example database query languages. A typical result might say, for example, that a certain language can’t distinguish between ‘even’ and ‘odd’; we would prove this by finding, for each level $n$ of complexity of formulas of the language, a pair of finite structures for which Duplicator has a winning strategy in the back-and-forth game of level $n$, but one of the structures has an even number of elements and the other has an odd number. Semanticists of natural languages have found back-and-forth games useful for comparing the expressive powers of generalised quantifiers. (See for example Peters and Westerståhl 2006 Section IV.)[^peters-2006]

For most logical languages there is a corresponding Ehrenfeucht-Fraïssé game that charcterizes elementary equivalence. This raises the converse question: if an Ehrenfeucht-Fraïssé game, with rules what the moves are and who wins each play, is given, is it necessarily the elementary equivalence relation with respect to some logical language? In other words, can the binary similarity relation between models, offered by some variant of Ehrenfeucht-Fraïssé game, be always turned to the relation between a sentence and a model? Mark Nadel 1980 investigates this question. Interestingly, Saharon Shelah 2012 defines a new infinitary logic by only giving its Ehrenfeucht-Fraïssé game.

There is also a kind of back-and-forth game that corresponds to our modal semantics above in the same way as Ehrenfeucht-Fraïssé games correspond to Hintikka’s game semantics for first-order logic. The players start with a state $s$ in the structure $A$ and a state $t$ in the structure $B$. Spoiler and Duplicator move alternately, as before. Each time he moves, Spoiler chooses whether to move in $A$ or in $B$, and then Duplicator must move in the other structure. A move is always made by going forwards along an arrow from the current state. If between them the two players have just moved to a state $s$´ in $A$ and a state $t$´ in $B$, and some predicate $P_i$ holds at just one of $s$´ and $t$´, then Duplicator loses at once. Also she loses if there are no available arrows for her to move along; but if Spoiler finds there are no available arrows for him to move along in either structure, then Duplicator wins. If the two players play this game with given starting states $s$ in $A$ and $t$ in $B$, and both structures have just finitely many states, then one can show that Duplicator has a winning strategy if and only if the same modal sentences are true at $s$ in $A$ as are true at $t$ in $B$.

There are many generalisations of this result, some of them involving the following notion. Let $Z$ be a binary relation which relates states of $A$ to states of $B$. Then we call $Z$ a *bisimulation* between $A$ and $B$ if Duplicator can use $Z$ as a nondeterministic winning strategy in the back-and-forth game between $A$ and $B$ where the first pair of moves of the two players is to choose their starting states. In computer science the notion of a bisimulation is crucial for the understanding of $A$ and $B$ as systems; it expresses that the two systems interact with their environment in the same way as each other, step for step. But a little before the computer scientists introduced the notion, essentially the same concept appeared in Johan van Benthem’s PhD thesis on the semantics of modal logic (1976).

## 7. Other Model-theoretic Games

The logical games in this section are mathematicians’ tools, but they have some conceptually interesting features.

### 7.1 Forcing games

Forcing games are also known to descriptive set theorists as *Banach-Mazur games*; see the references by Kechris or Oxtoby below for more details of the mathematical background. Model theorists use them as a way of building infinite structures with controlled properties. In the simplest case $\forall$ and $\exists$ play a so-called Model Existence Game, where $\exists$ claims that a fixed sentence $\phi$ has a model while $\forall$ claims that he can derive a contradiction from $\phi$. In the beginning a countably infinite set $C$ of new constant symbols $a_0, a_1, a_2$ etc is fixed. $\exists$ defends a disjunction by choosing one disjunct, and an existential statement by choosing a constant from $C$ as a witness. $\forall$ can challenge a conjunction by choosing either conjunct, and a universal statement by choosing an arbitrary witness from $C$. $\exists$ wins if no contradicting atomic sentences are played. $\exists$ has a winning strategy (a Consistency Property is one way of describing a winning strategy) if and only if $\phi$ has a model. On the other hand, if $\forall$ has a winning strategy, the tree (which can be made finite) of all plays against his winning strategy is related to a Gentzen style proof of the negation of $\phi$. This method of analysing sentences is closely related to Beth’s method of semantic tableaux and the Dialogical Game (see Section 8). See also Jouko Väänänen 2023.

To sketch the idea of the general Forcing Game, imagine that a countably infinite team of builders are building a house $A$. Each builder has his or her own task to carry out: for example to install a bath or to wallpaper the entrance hall. Each builder has infinitely many chances to enter the site and add some finite amount of material to the house; these slots for the builders are interleaved so that the whole process takes place in a sequence of steps counted by the natural numbers.

To show that the house can be built to order, we need to show that each builder separately can carry out his or her appointed task, regardless of what the other builders do. So we imagine each builder as player $\exists$ in a game where all the other players are lumped together as $\forall$, and we aim to prove that $\exists$ has a winning strategy for this game. When we have proved this for each builder separately, we can imagine them going to work, each with their own winning strategy. They all win their respective games and the result is one beautiful house.

More technically, the elements of the structure $A$ are fixed in advance, say as $a_0, a_1, a_2$ etc., but the properties of these elements have to be settled by the play. Each player moves by throwing in a set of atomic or negated atomic statements about the elements, subject only to the condition that the set consisting of all the statements thrown in so far must be consistent with a fixed set of axioms written down before the game. (So throwing in a negated atomic sentence $\neg \phi$ has the effect of preventing any player from adding $\phi$ at a later stage.) At the end of the joint play, the set of atomic sentences thrown in has a canonical model, and this is the structure $A$; there are ways of ensuring that it is a model of the fixed set of axioms. A possible property P of $A$ is said to be *enforceable* if a builder who is given the task of making P true of $A$ has a winning strategy. A central point (due essentially to Ehrenfeucht) is that the conjunction of a countably infinite set of enforceable properties is again enforceable.

Various Löwenheim-Skolem Theorems of model theory can be proved using variants of the Forcing Game. In these variants we do not construct a model but a submodel of a given model. We start with a big model $M$ for a sentence (or a countable set of sentences) $\phi$. Then we list the subformulas of $\phi$ and each player has a subformula with a free variable to attend to. The player’s task is to make sure that as soon as the parameters of the subformula occur in the game, and there is a witness to the truth of the formula in the big model, one such a witness is played. When the game is over, a countable submodel of $M$ has been built in such a way that it satisfies $\phi$.

The name ‘forcing’ comes from an application of related ideas by Paul Cohen to construct models of set theory in the early 1960s. Abraham Robinson adapted it to make a general method for building countable structures, and Martin Ziegler introduced the game setting. Later Robin Hirsch and Ian Hodkinson used related games to settle some old questions about relation algebras.

Forcing games are a healthy example to bear in mind when thinking about the Dawkins question. They remind us that in logical games it need not be helpful to think of the players as opposing each other.

### 7.2 Cut-and-choose games

In the traditional cut-and-choose game you take a piece of cake and cut it into two smaller pieces; then I choose one of the pieces and eat it, leaving the other one for you. This procedure is supposed to put pressure on you to cut the cake fairly. Mathematicians, not quite understanding the purpose of the exercise, insist on iterating it. Thus I make you cut the piece I chose into two, then I choose one of those two; then you cut this piece again, and so on indefinitely. Some even more unworldly mathematicians make you cut the cake into countably many pieces instead of two.

These games are important in the theory of definitions. Suppose we have a collection $A$ of objects and a family $S$ of properties; each property cuts $A$ into the set of those objects that have the property and the set of those that don’t. Let $\exists$ cut, starting with the whole set $A$ and using a property in $S$ as a knife; let $\forall$ choose one of the pieces (which are subsets of $A)$ and give it back to $\exists$ to cut again, once more using a property in $S$; and so on. Let $\exists$ lose as soon as $\forall$ chooses an empty piece. We say that $(A, S)$ has *rank* at most $m$ if $\forall$ has a strategy which ensures that $\exists$ will lose before her $m$-th move. The rank of $(A, S)$ gives valuable information about the family of subsets of $A$ definable by properties in $S$.

Variations of this game, allowing a piece to be cut into infinitely many smaller pieces, are fundamental in the branch of model theory called *stability theory*. Broadly speaking, a theory is ‘good’ in the sense of stability theory if, whenever we take a model $A$ of the theory and $S$ the set of first-order formulas in one free variable with parameters from $A$, the structure $(A, S)$ has ‘small’ rank. A different variation is to require that at each step, $\exists$ divides into two each of the pieces that have survived from earlier steps, and again she loses as soon as one of the cut fragments is empty. (In this version $\forall$ is redundant.) With this variation, the rank of $(A$,S) is called its *Vapnik-Chervonenkis dimension*; this notion is used in computational learning theory.

### 7.3 Games on the tree of two successor functions

Imagine a tree that has been built up in levels. At the bottom level there is a single root node, but a left branch and a right branch come up from it. At the next level up there are two nodes, one on each branch, and from each of these nodes a left branch and a right branch grow up. So on the next level up there are four nodes, and again the tree branches into left and right at each of these nodes. Continued to infinity, this tree is called the *tree of two successor functions* (namely left successor and right successor). Taking the nodes as elements and introducing two function symbols for left and right successor, we have a structure. A powerful theorem of Michael Rabin states that there is an algorithm which will tell us, for every monadic second-order sentence $\phi$ in the language appropriate for this structure, whether or not $\phi$ is true in the structure. (’Monadic second-order’ means that the logic is like first-order, except that we can also quantify over sets of elements—but not over binary relations on elements, for example.)

Rabin’s theorem has any number of useful consequences. For example Dov Gabbay used it to prove the decidability of some modal logics. But Rabin’s proof, using automata, was notoriously difficult to follow. Yuri Gurevich and Leo Harrington, and independently Andrei Muchnik, found much simpler proofs in which the automaton is a player in a game.

This result of Rabin is one of several influential resuls that connect games with automata. Another example is the *parity games* which are used for verifying properties of modal systems. See for example Stirling (2001)[^stirling-2001] Chapter 6; Bradfield and Stirling (2006) discuss parity games for the modal $\mu$-calculus.

## 8. Games of dialogue, communication and proof

Several medieval texts describe a form of debate called *obligationes*. There were two disputants, Opponens and Respondens. At the beginning of a session, the disputants would agree on a ‘positum’, typically a false statement. The job of Respondens was to give rational answers to questions from Opponens, assuming the truth of the positum; above all he had to avoid contradicting himself unnecessarily. The job of Opponens was to try to force Respondens into contradictions. So we broadly know the answer to the Dawkins question, but we don’t know the game rules! The medieval textbooks do describe several rules that the disputants should follow. But these rules are not stipulated rules of the game; they are guidelines which the textbooks derive from principles of sound reasoning with the aid of examples. (Paul of Venice justifies one rule by the practice of ‘great logicians, philosophers, geometers and theologians’.) In particular it was open to a teacher of obligationes to discover new rules. This open-endedness implies that obligationes are not logical games in our sense.

Not everybody agrees with the previous sentence. For example Catarina Dutilh Novaes (2007, 6) makes a detailed defence of the view that obligationes present “a remarkable case of conceptual similarity between a medieval and a modern theoretical framework”. But whatever view we take on this question, these debates have inspired one important line of modern research in logical games.

Imagine $\exists$ taking an oral examination in proof theory. The examiner gives her a sentence and invites her to start proving it. If the sentence has the form

$$ \phi \vee \psi $$

then she is entitled to choose one of the sentences and say ‘OK, I’ll prove this one’. (In fact if the examiner is an intuitionist, he may insist that she choose one of the sentences to prove.) On the other hand if the sentence is

$$ \phi \wedge \psi $$

then the examiner, being an examiner, might well choose one of the conjuncts himself and invite her to prove that one. If she knows how to prove the conjunction then she certainly knows how to prove the conjunct.

The case of $\phi \rightarrow \psi$ is a little subtler. She will probably want to start by assuming $\phi$ in order to deduce $\psi$; but there is some risk of confusion because the sentences that she has written down so far are all of them things to be proved, and $\phi$ is not a thing to be proved. The examiner can help her by saying ‘I’ll assume $\phi$, and let’s see if you can get to $\psi$ from there’. At this point there is a chance that she sees a way of getting to $\psi$ by deducing a contradiction from $\phi$; so she may turn the tables on the examiner and invite him to show that his assumption is consistent, with a view to proving that it isn’t. The symmetry is not perfect: he was asking her to show that a sentence is true everywhere, while she is inviting him to show that a sentence is true somewhere. Nevertheless we can see a sort of duality.

Ideas of this kind lie behind the dialectical games of Paul Lorenzen. He showed that with a certain amount of pushing and shoving, one can write rules for the game which have the property that $\exists$ has a winning strategy if and only if the sentence that she is presented with at the beginning is a theorem of intuitionistic logic. In a gesture towards medieval debates, he called $\exists$ the Proponent and the other player the Opponent. Almost as in the medieval obligationes, the Opponent wins by driving the Proponent to a point where the only moves available to her are blatant self-contradictions.

Lorenzen claimed that his games provided justifications for both intuitionist and classical logic (or in his words, made them ‘gerechtfertigt’, Lorenzen (1961,196)[^lorenzen-1961]). Unfortunately any ‘justification’ involves a convincing answer to the Dawkins question, and this Lorenzen never provided. For example he spoke of moves as ‘attacks’, even when (like the examiner’s choice at $\phi \wedge \psi$ above) they look more like help than hostility.

The entry dialogical logic gives a fuller account of Lorenzen’s games and a number of more recent variants. In its present form (January 2013) it sidesteps Lorenzen’s claims about justifying logics. Instead it describes the games as providing semantics for the logics (a point that Lorenzen would surely have agreed with), and adds that for understanding the differences between logics it can be helpful to compare their semantics.

From this point of view, Lorenzen’s games stand as an important paradigm of what recent proof theorists have called *semantics of proofs*. A semantics of proofs gives a ‘meaning’ not just to the notion of being provable, but to each separate step in a proof. It answers the question ‘What do we achieve by making this particular move in the proof?’ During the 1990s a number of workers at the logical end of computer science looked for games that would stand to linear logic and some other proof systems in the same way as Lorenzen’s games stood to intuitionist logic. Andreas Blass, and then later Samson Abramsky and colleagues, gave games that corresponded to parts of linear logic, but at the time of writing we don’t yet have a perfect correspondence between game and logic. This example is particularly interesting because the answer to the Dawkins question should give an intuitive interpretation of the laws of linear logic, a thing that this logic has badly needed. The games of Abramsky et al. tell a story about two interacting systems. But while he began with games in which the players politely take turns, Abramsky later allowed the players to act ‘in a distributed, asynchronous fashion’, taking notice of each other only when they choose to. These games are no longer in the normal format of logical games, and their real-life interpretation raises a host of new questions.

Giorgi Japaridze has proposed a ‘computability logic’ for studying computation. Its syntax is first-order logic with some extra items reminiscent of linear logic. Its semantics is in terms of semantic games with some unusual features. For example it is not always determined which player makes the next move. The notion of strategy functions is no longer adequate for describing the players; instead Japaridze describes ways of reading the second player (player $\exists$ in our notation) as a kind of computing machine. Further information is on his website.

Another group of games of the same general family as Lorenzen’s are the proof games of Pavel Pudlak 2000. Here the Opponent (called Prover) is in the role of an attorney in a court of law, who knows that the Proponent (called Adversary) is guilty of some offence. Proponent will insist he is innocent, and is prepared to tell lies to defend himself. Opponent’s aim is to force Proponent to contradict something that Proponent is on record as having said earlier; but Opponent keeps the record and (as in the pebble games above) he sometimes has to drop items from the record for lack of space or memory. The important question is not whether Opponent has a winning strategy (it’s assumed from the outset that he has one), but how much memory he needs for his record. These games are a useful device for showing upper and lower bounds on the lengths of proofs in various proof systems.

Another kind of logical game that allows lies is Ulam’s Game with Lies. Here one player thinks of a number in some given range. The second player’s aim is to find out what that number is, by asking the first player yes/no questions; but the first player is allowed to tell some fixed number of lies in his answers. As in Pudlak’s games, there is certainly a winning strategy for the second player, but the question is how hard this player has to work in order to win. The measure this time is not space or memory but time: how many questions does he have to ask? Cignoli et al. 2000 Chapter 5 relate this game to many-valued logic.

To return for a moment to Lorenzen: he failed to distinguish between different stances that a person might take in an argument: stating, assuming, conceding, querying, attacking, committing oneself. Whether it is really possible to define all these notions without presupposing some logic is a moot point. But never mind that; a refinement of Lorenzen’s games along these lines could serve as an approach to informal logic, and especially to the research that aims to systematise the possible structures of sound informal argument. On this front see Walton and Krabbe 1995. The papers in Bench-Capon and Dunne 2007 are also relevant.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

### Games in the History of Logic

### Games for Teaching Logic

### Logical Games

### Semantic Games for Classical Logic

### Semantic Games with Imperfect Information

### Semantic Games for Other Logics

### Back-and-Forth Games

### Other Model-Theoretic Games

### Games of Dialogue, Communication and Proof

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=logic-games). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/logic-games/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=logic-games&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/logic-games/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- [Giorgi Japaridze’s Computability Logic page](http://www.cis.upenn.edu/~giorgi/cl.html)

## Related Entries

game theory | generalized quantifiers | logic: classical | logic: dialogical | logic: epistemic | logic: for analyzing games | logic: independence friendly | logic: infinitary | logic: informal | logic: intuitionistic | logic: linear | logic: modal | model theory | set theory

[^some-1959]: Some of the seminal papers by Henkin and Lorenzen, and some of the papers cited below, appear in the collection *Infinitistic Methods* (Proceedings of the Symposium on Foundations of Mathematics, Warsaw, 2–9 September, 1959), Oxford: Pergamon Press, 1961. The editors are unnamed.

[^dutilh-2007]: Dutilh Novaes, Catarina, 2007, *Formalizing Medieval Logical Theories: Suppositio, Consequentiae and Obligationes*, New York: Springer-Verlag.

[^hamblin-1970]: Hamblin, Charles, 1970, *Fallacies*, London: Methuen.

[^hilbert-1967]: Hilbert, David, 1967, “Die Grundlagen der Mathematik”, translated as “The foundations of mathematics,” in Jean van Heijenoort (ed.), *From Frege to Gödel*, Cambridge Mass.: Harvard University Press, pp. 464–479.

[^paul-1988]: Paul of Venice, *Logica Magna II (8), Tractatus de Obligationibus*, E. Jennifer Ashworth (ed.), New York: British Academy and Oxford University Press, 1988.

[^weyl-1925]: Weyl, Hermann, 1925–7, “Die heutige Erkenntnislage in der Mathematik,”, translated as “The current epistemological situation in mathematics” in Paolo Mancosu, *From Brouwer to Hilbert: The Debate on the Foundations of Mathematics in the 1920s*, New York: Oxford University Press, 1988, pp. 123–142.

[^zermelo-1913]: Zermelo, Ernst, 1913, “Über eine Anwendung der Mengenlehre auf die Theorie des Schachspiels,” in E. W. Hobson and A. E. H. Love (eds.), *Proceedings of the Fifth International Congress of Mathematicians*, Volume II, Cambridge: Cambridge University Press.

[^barwise-1995]: Barwise, Jon and John Etchemendy, 1995, *The Language of First-Order Logic, including Tarski’s World 3.0*, Cambridge: Cambridge University Press.

[^carroll-1887]: Carroll, Lewis, 1887, *The Game of Logic*, London: Macmillan.

[^dienes-1966]: Dienes, Zoltan P., and E. W. Golding, 1966, *Learning Logic, Logical Games*, Harlow: Educational Supply Association.

[^havas-1999]: Havas, Katalin, 1999, “Learning to think: Logic for children,” in *Proceedings of the Twentieth World Congress of Philosophy* (Volume 3: Philosophy of Education), David M. Steiner (ed.), Bowling Green Ohio: Bowling Green State University Philosophy, pp. 11–19.

[^nifo-nd]: Nifo, Agostino, 1521, *Dialectica Ludicra* (*Logic as a game*), Florence: Bindonis.

[^weng-2010]: Weng, Jui-Feng, with Shian-Shyong Tseng and Tsung-Ju Lee, 2010, “Teaching Boolean logic through game rule tuning,” *IEEE Transactions, Learning Technologies*, 3(4): 319–328. [Uses Pac-Man games to teach Boolean logic to junior high school students.]

[^gale-1953]: Gale, David and F. M. Stewart, 1953, “Infinite games with perfect information,” in *Contributions to the Theory of Games II* (Annals of Mathematics Studies 28), H. W. Kuhn and A. W. Tucker (eds.), Princeton: Princeton University Press, pp. 245–266.

[^kechris-1995]: Kechris, Alexander S., 1995, *Classical Descriptive Set Theory*, New York: Springer-Verlag.

[^marion-2009]: Marion, Mathieu, 2009, “Why play logical games?,” in Ondrej Majer, Ahti-Veikko Pietarinen, and Tero Tulenheimo eds., *Games: Unifying Logic, Language and Philosophy*, New York: Springer-Verlag, pp. 3-25.

[^osbourne-1994]: Osbourne, Martin J. and Ariel Rubinstein, 1994, *A Course in Game Theory*, Cambridge: MIT Press.

[^väänänen-2011]: Väänänen, Jouko, 2011, *Models and Games*, Cambridge: Cambridge University Press.

[^väänänen-2023]: –––, 2023, “The strategic balance of games in logic”, in Alessandra Palmigiano and Mehrnoosh Sadrzadeh (eds.), *Samson Abramsky on Logic and Structure in Computer Science and Beyond* (Outstanding Contributions to Logic: Volume 25), Cham: Springer, pp. 7557ndash;770.

[^benthem-2011]: van Benthem, Johan, 2011, *Logical dynamics of information and interaction*, Cambridge: Cambridge University Press.

[^benthem-2014]: –––, 2014, *Logic in games*, Cambridge, MA: MIT Press.

[^henkin-1961]: Henkin, Leon, 1961, “Some remarks on infinitely long formulas,” in *Infinitistic Methods* (Proceedings of the Symposium on Foundations of Mathematics, Warsaw, 2–9 September, 1959), Oxford: Pergamon Press, pp. 167–183.

[^hintikka-1973]: Hintikka, Jaakko, 1973, *Logic, Language-Games and Information: Kantian Themes in the Philosophy of Logic*, Oxford: Clarendon Press.

[^hintikka-1996]: Hintikka, Jaakko, 1996, *The Principles of Mathematics Revisited*, New York: Cambridge University Press. [See for example pages 40, 82 on the axiom of choice.]

[^hodges-2001]: Hodges, Wilfrid, 2001, “Elementary Predicate Logic 25: Skolem Functions,” in Dov Gabbay, and Franz Guenthner (eds.), *Handbook of Philosophical Logic I*, 2nd edition, Dordrecht: Kluwer, pp. 86–91. [Proof of equivalence of game and Tarski semantics.]

[^kolaitis-1985]: Kolaitis, Ph. G., 1985, “Game quantification,” in J. Barwise and S. Feferman (eds.), *Model-Theoretic Logics*, New York: Springer-Verlag, pp. 365-421.

[^peirce-1898]: Peirce, Charles Sanders, 1898, *Reasoning and the Logic of Things: The Cambridge Conferences Lectures of 1898*, ed. Kenneth Laine Ketner, Cambridge Mass., Harvard University Press, 1992.

[^hintikka-1997]: Hintikka, Jaakko and Gabriel Sandu, 1997, “Game-theoretical semantics,” in Johan van Benthem and Alice ter Meulen (eds.), *Handbook of Logic and Language*, Amsterdam: Elsevier, pp. 361–410.

[^hodges-1997]: Hodges, Wilfrid, 1997, “Compositional semantics for a language of imperfect information,” *Logic Journal of the IGPL*, 5: 539–563.

[^janssen-2006]: Janssen, Theo M. V. and Francien Dechesne, 2006, “Signalling: a tricky business,” in J. van Benthem *et al*. (eds.), *The Age of Alternative Logics: Assessing the Philosophy of Logic and Mathematics Today*, Dordrecht: Kluwer, pp. 223–242.

[^mann-2011]: Mann, Allen L., Gabriel Sandu, and Merlin Sevenster, 2011, *Independence-Friendly Logic: A Game-Theoretic Approach* (London Mathematical Society Lecture Note Series 386), Cambridge: Cambridge University Press.

[^neumann-1944]: von Neumann, John and Oskar Morgenstern, 1944, *Theory of Games and Economic Behavior*, Princeton: Princeton University Press.

[^väänänen-2007]: Väänänen, Jouko, 2007, *Dependence Logic: A New Approach to Independence Friendly Logic*, Cambridge: Cambridge University Press.

[^bradfield-2006]: Bradfield, Julian and Colin Stirling, 2006, “Modal mu-calculi,” in P. Blackburn *et al*. (eds.), *Handbook of Modal Logic*, Amsterdam: Elsevier, pp. 721–756.

[^dekker-2002]: Dekker, Paul, and Marc Pauly (eds.), 2002, *Journal of Logic, Language and Information*, 11(3): 287–387. [Special issue on Logic and Games.]

[^hennessy-1985]: Hennessy, Matthew, and Robin Milner, 1985, “Algebraic laws for indeterminism and concurrency,” *Journal of the ACM*, 32: 137–162.

[^parikh-1985]: Parikh, Rohit, 1985, “The logic of games and its applications,” in Marek Karpinski and Jan van Leeuwen (eds.), “Topics in the Theory of Computation,” *Annals of Discrete Mathematics*, 24: 111–140.

[^pauly-2003]: Pauly, Marc, and Rohit Parikh (eds.), 2003, *Studia Logica*, 72(2): 163–256 [Special issue on Game Logic.]

[^stirling-2001]: Stirling, Colin, 2001, *Modal and Temporal Properties of Processes*, New York: Springer-Verlag.

[^benthem-2006]: van Benthem, Johan, 2006, “The epistemic logic of IF games,” in Randall Auxier and Lewis Hahn (eds.), *The Philosophy of Jaakko Hintikka*, Chicago: Open Court pp. 481–513.

[^benthem-2011-2]: van Benthem, Johan with Amitabha Gupta and Rohit Parikh, 2011, *Proof, Computation and Agency*, Dordrecht: Springer-Verlag.

[^blackburn-2001]: Blackburn, Patrick with Maarten de Rijke and Yde Venema, 2001, *Modal Logic*, Cambridge: Cambridge University Press.

[^doets-1996]: Doets, Kees, 1996, *Basic Model Theory*, Stanford: CSLI Publications and FoLLI.

[^ebbinghaus-1999]: Ebbinghaus, Heinz-Dieter and Jörg Flum, 1999, *Finite Model Theory*, 2nd edition, New York: Springer.

[^ehrenfeucht-1961]: Ehrenfeucht, Andrzej, 1961, “An application of games to the completeness problem for formalized theories,” *Fundamenta Mathematicae*, 49: 129–141.

[^grädel-2007]: Grädel, Erich with Phokion G. Kolaitis, Leonid Libkin, Maarten Marx, Joel Spencer, Moshe Y. Vardi, Yde Venema, and Scott Weinstein, 2007, *Finite Model Theory*, Berlin: Springer-Verlag.

[^libkin-2004]: Libkin, Leonid, 2004, *Elements of Finite Model Theory*, Berlin, Springer-Verlag.

[^lindström-1969]: Lindström, Per 1969, “On extensions of elementary logic”, *Theoria*, 35: 1–11.

[^mekler-1993]: Mekler, Alan with Saharon Shelah, and Jouko Väänänen, 1993, “The Ehrenfeucht-Fraïssé-game of length ω₁”, *Transactions of the American Mathematical Society*, .339(2): 567–580.

[^nadel-1980]: Nadel, Mark, 1980, “An arbitrary equivalence relation as elementary equivalence in an abstract logic”, *Zeitschrift für mathematische Logik und Grundlagen der Mathematik.*, 26: 103–109

[^otto-1997]: Otto, Martin, 1997, *Bounded Variable Logics and Counting—A Study in Finite Models* (Lecture Notes in Logic, 9), Berlin: Springer-Verlag.

[^peters-2006]: Peters, Stanley and Dag Westerståhl, 2006, *Quantifiers in Language and Logic*, Oxford: Clarendon Press.

[^shelah-2012]: Shelah, Saharon 2012, “Nice infinitary logics”, *Journal of the American Mathematical Society*, 25(2): 395–427.

[^tarski-1946]: Tarski, Alfred, 1946, “Address at the Princeton University Bicentennial Conference on Problems of Mathematics (December 17–19, 1946),” Hourya Sinaceur (ed.), *Bulletin of Symbolic Logic*, 6 (2000): 1–44.

[^benthem-2001]: van Benthem, Johan, 2001, “Correspondence Theory,” in Dov Gabbay and Franz Guenthner (eds.), *Handbook of Philosophical Logic III*, 2nd edition, Dordrecht: Kluwer.

[^anthony-1992]: Anthony, Martin, and Norman Biggs, 1992, *Computational Learning Theory*, Cambridge: Cambridge University Press. [For Vapnik-Chervonenkis dimension.]

[^gurevich-1984]: Gurevich, Yuri and Leo Harrington, 1984,“Trees, automata, and games,” in H. R. Lewis (ed.), *Proceedings of the ACM Symposium on the Theory of Computing*, San Francisco: ACM, pp. 171–182.

[^hirsch-2002]: Hirsch, Robin and Ian Hodkinson, 2002, *Relation Algebras by Games*, New York: North-Holland.

[^hodges-1985]: Hodges, Wilfrid, 1985, *Building Models by Games*, Cambridge: Cambridge University Press.

[^hodges-1993]: Hodges, Wilfrid, 1993, *Model Theory*, Cambridge: Cambridge University Press.

[^oxtoby-1971]: Oxtoby, J. C., 1971, *Measure and Category*, New York: Springer-Verlag.

[^ziegler-1980]: Ziegler, Martin, 1980, “Algebraisch abgeschlossene Gruppen,” in S. I. Adian *et al*. (eds.), *Word Problems II: The Oxford Book*, Amsterdam: North-Holland, pp. 449–576.

[^abramsky-1994]: Abramsky, Samson and Radha Jagadeesan, 1994, “Games and full completeness for multiplicative linear logic,” *Journal of Symbolic Logic*, 59: 543–574.

[^abramsky-1999]: Abramsky, Samson and Paul-André Melliès, 1999, “Concurrent games and full completeness,” in *Proceedings of the Fourteenth International Symposium on Logic in Computer Science*, Computer Science Press of the IEEE, pp. 431–442.

[^bench-capon-2007]: Bench-Capon, T. J. M. and Paul E. Dunne, 2007, “Argumentation in artificial intelligence,” *Artificial Intelligence*, 171: 619–641. [The introduction to a rich collection of papers on the same theme on pages 642–937.]

[^blass-1992]: Blass, Andreas, 1992, “A game semantics for linear logic,” *Annals of Pure and Applied Logic*, 56: 183–220.

[^cignoli-2000]: Cignoli, Roberto L. O., Itala M. L. D’Ottaviano, and Daniele Mundici, 2000, *Algebraic Foundations of Many-Valued Reasoning*, Dordrecht: Kluwer.

[^felscher-2001]: Felscher, Walter, 2001, “Dialogues as a foundation for intuitionistic logic,” in Dov Gabbay and Franz Guenthner (eds.), *Handbook of Philosophical Logic V*, 2nd edition, Dordrecht: Kluwer.

[^hodges-2001-2]: Hodges, Wilfrid and Erik C. W. Krabbe, 2001, “Dialogue foundations,” *Proceedings of the Aristotelian Society* (Supplementary Volume), 75: 17–49.

[^japaridze-2003]: Japaridze, Giorgi, 2003, “Introduction to computability logic,” *Annals of Pure and Applied Logic*, 123: 1–99.

[^lorenzen-1961]: Lorenzen, Paul, 1961 “Ein dialogisches Konstruktivitätskriterium,” in *Infinitistic Methods* (Proceedings of the Symposium on Foundations of Mathematics, Warsaw, 2–9 September, 1959), Oxford: Pergamon Press, pp. 193–200.

[^pudlak-2000]: Pudlak, Pavel, 2000, “Proofs as games,” *American Mathematical Monthly*, 107(6): 541–550.

[^walton-1995]: Walton, Douglas N. and Erik C. W. Krabbe, 1995, *Commitment in Dialogue: Basic Concepts of Interpersonal Reasoning*, Albany: State University of New York Press.
