# Dialogical Logic
**First published Fri Feb 4, 2022**

*Clerbout, Nicolas, McConaughey, Zoe*

*Dialogical logic* is a dialogue-based approach to logic and argumentation rooted in a research tradition that goes back to dialectics in Greek Antiquity, when problems were approached through dialogues in which opposing parties discussed a thesis through questions and answers. The dialogical framework was first worked out in its modern form by Paul Lorenzen and Kuno Lorenz in the context of constructive mathematics and logic, and inspired many “dialogical logics” that follow more or less the initial program, thus creating what can be called traditions in dialogical logic. This entry focuses on the developments of dialogical logic in the Lorenzen and Lorenz tradition, which developed in the 1990s and 2000s into a fruitful framework for the study, comparison, and combination of various non-classical systems, giving rise to what has been called *dialogical pluralism*. References to the other traditions will nonetheless be provided.

In the Lorenzen and Lorenz tradition, dialogical logic uses concepts of both game and argumentation theory to provide a pragmatist approach to meaning and reasoning constituted during the interaction of two players arguing on a given thesis. The game rules allow these players to challenge the other’s statements or defend their own statements in such a way that one player wins and the other loses after a finite number of moves. The meaning of the logical constants is provided by a set of interaction rules (the local rules) and the dialogical equivalent of a demonstration is a construction of plays through which it is shown that one player may win whatever the other player’s moves may be (winning strategy). Thus, both the dialogical meaning of the logical constants and the dialogical conception of demonstration are constituted by interaction.

## 1. A Brief Overview of Dialogical Logic

In the dialogical framework the meaning of an expression is explained in game-theoretic terms, as opposed to the main-stream model-theoretic semantics. In this fashion, the meaning of the logical constants is explained by means of rules prescribing how to use these constants in argumentation games. Various traditions can be distinguished in the game-theoretical approach (see also Rahman & Keiff 2005)[^rahman-2005]:

1. The constructivist tradition of Paul Lorenzen and Kuno Lorenz. This is the main tradition of dialogical logic and the present entry will focus on it and its recent developments. Dialogical logic is considered (especially by Lorenz) as a semantic project, and was initially developed in order to overcome the limitations of operative logic (Lorenzen 1955; see also Schroeder-Heister 2008)[^lorenzen-1955][^schroeder-heister-2008]. Dialogues are finitary games about an initial formula, which is said to be *valid* if, and only if, the proponent has a *winning strategy* for it (see Section 2.1.2). Expanding this tradition, Shahid Rahman and collaborators have made dialogical logic a framework for expressing various logics other than the initial intuitionistic logic, as presented in Section 2.2 (see in particular Rahman 1993, Rahman and Rückert 2001, Rahman and Keiff 2005)[^rahman-1993][^rahman-2001][^rahman-2005][^rückert-2001]. Walter Felscher (1985) follows a common method for writing winning strategies (Lorenzen & Lorenz 1978; Lorenz 1981)[^lorenz-1981][^lorenzen-1978] that uses the semantic tableaux of Beth (1955), and his technical achievements have strongly influenced some logicians when working with the dialogical framework or some variation of it, notably Sørensen and Urzyczyn (2007); Alama et al. (2011); Uckelman et al. (2014); Dutilh Novaes (2015; 2020); Dutilh Novaes and French (2018); French (2021). Another author which had considerable influence for these works is Christian Fermüller, for example Fermüller (2003).
2. The game-theoretical tradition of Jaakko Hintikka (1968), called GTS (see the entry on independence friendly logic). This tradition shares the game-theoretical tenets of dialogical logic for logical constants, but switches to standard model theory at the level of elementary statements, for which standard truth-functional formal semantics comes into play.
3. The argumentation theory tradition of Else Barth and Erick Krabbe (1982; see also Gethmann 1979)[^gethmann-1979]. This tradition links dialogical logic with informal logic (or critical reasoning), which originated in the work of Perelman and Olbrechts-Tyteca (1958), and studies the underlying logical regularities of concrete dialogues. In this tradition figures Toulmin’s argumentation theory (Toulmin 1958)[^toulmin-1958], Barth and Krabbe’s theory of dialogue (Barth & Krabbe 1982)[^barth-1982], Douglas Walton (1984), Ralph Johnson (1999), Woods’ argumentation theory (Woods 1989; Woods et al. 2000)[^woods-1989][^woods-2000], and critical thinking (Anand Jayprakash Vaidya 2013, among others)[^vaidya-2013].
4. The ludics tradition of Jean-Yves Girard (2001). This tradition provides an overall theory of proof-theoretical meaning based on interactive computation. Andreas Blass (1992) proposed a dialogical semantics (in the sense of tradition 1) for linear logics, to which ludics is often associated.
5. The recent developments of dialogical logic in constructive mathematics. New developments in this field are becoming more and more important and it can safely be called a full-fledged tradition. Nowadays, these developments are deeply related to the links between dialogical logic and constructive type theory, and have even started to make interesting connections with new programs in Philosophy of Mathematics such as Homotopy Theory. Prominent works related to this field are for instance Coquand (1995) and Sterling (2021).

These traditions sometimes share common features, sometimes challenge features of other traditions, sometimes try to make links with other traditions. Thus, traditions 1 and 3 share an epistemic and proof-theoretical background. Traditions 2 and 3 challenge the dialogical conception of logic of tradition 1 in order to bring about a framework in which meaning is not reduced to a formal approach, but is understood as setting out content. Recent works claim to answer this kind of challenge while still staying within tradition 1 (see Section 3.2). Other recent efforts have tried to link traditions 1 and 3: Prakken (2005), for example, focuses on logical analysis in the context of legal reasoning and non-monotonic reasoning; more recent and quite different perspectives explore substructural approaches to paradoxes in terms of natural argumentation and its treatment in a game-theoretical setting inspired by tradition 1 (French 2015; Dutilh Novaes & French 2018; Dutilh Novaes 2020)[^dutilh-2020][^dutilh-2018][^french-2015]. The present entry focuses on the original work of Lorenzen and Lorenz (tradition 1) with its developments during the last decades. Historical remarks on the relations between logic and dialogues can be found in the entry on logic and games, and in Lorenz (2001).

Section 2 presents the essential features of the standard dialogical framework, and how it can accommodate various logics. Section 3 presents two variations on the standard framework: a first that endeavors to stay within tradition 1; a second that emancipates itself from tradition 1 while stressing the merits of such a dialogical approach for dealing with problems of philosophy of logic.

## 2. The Standard Dialogical Framework of the Lorenzen and Lorenz Tradition

As hinted by its name, the dialogical framework studies dialogues; but it also takes the form of dialogues. In a dialogue, two parties (players) argue on a thesis (a certain statement that is the subject of the whole argument) and follow certain fixed rules in their argument. The player who states the thesis is the proponent, called **P**, and his rival, the player who challenges the thesis, is the opponent, called **O**. In challenging the proponent’s thesis, the opponent is requiring that the proponent defends his statement.

The two players are thus rivals during the play, they have opposing goals, but the opposition does not necessarily have to go any further. Indeed, as spelled out by Marion (2006; 2009; 2010) and Keiff (2007), the dialogues are a kind of “game of giving and asking for reasons” (Brandom 1994, see also Sellars 1997)[^brandom-1994][^brandom-1997][^sellars-1997], and this kind of game can be for a common goal (e.g., figuring out the truth). There does not seem to be a consensus on whether the framework does allow cooperation or not. Some, like Dutilh Novaes (2015; 2020), have argued that the original dialogical framework is only adversarial and does not consider cooperation games. However, others have argued on the contrary that even the original framework is actually not entirely adversarial: Hodges (2001), for example, considers that some attacks in these games actually amount to helping the adversary.

Actions in a dialogue are called moves; they are often understood as speech-acts involving declarative utterances (statements) and interrogative utterances (requests). The rules for dialogues thus never deal with expressions isolated from the act of uttering them; by defining the appropriate interactions in a dialogue, these rules define the meaning of the expressions. Such an approach to meaning finds its roots in Wittgenstein’s observation that in language, there is no exterior perspective that would allow one to determine the meaning of something and how it links to syntax. In other words, language is unavoidable, one cannot go beyond it (this is Wittgenstein’s “*Unhintergehbarkeit der Sprache*”). Accordingly, language is studied with and through language-games; these language-games need to acknowledge the fact that they are part of their object of study. In this respect, all the speech-acts pertaining to the meaning and “formation” of an expression are made explicit in the dialogical framework. We are thus far from the metalinguistic perspective constitutive of the model-theoretic conceptions of meaning (see Lorenz 1970: 109; Sundholm 1997; 2001)[^lorenz-1970][^sundholm-1997].

### 2.1 Intuitionistic logic in the standard dialogical framework

This section presents the general features of what may be called the “standard” dialogical framework (as opposed to the more recent developments presented in Section 3.2).

The word “standard” here does not mean that the presentation below strictly follows in all its details the initial presentation of dialogical logic as introduced by Lorenzen and Lorenz. As a matter of fact, there has been a lot of variations on terminology and presentation throughout the years (in the works of Felscher, Krabbe, Rahman, Fermüller to mention but a few). Still, despite all the different variations in the literature, there are some fundamental features which this Section presents.

As mentioned above, the two players in a dialogue argue on a thesis (the statement that is the subject of the whole argument). They challenge and defend statements according to rules, which spell out the play’s progress and the meaning of statements in terms of possible interaction between players. There are two kinds of game rules that need to be distinguished: particle rules (*Partikelregeln*) and structural rules (*Rahmenregeln*). Particle rules determine what kind of move each player is allowed to make during a play, whereas the structural rules determine the structure of the play: how it starts, ends, and what special rules apply to players. The game rules are detailed in Section 2.1.1.

The game rules (particle rules and structural rules) constitute what is called the *play level* of the dialogical approach—constituting the backbone of dialogical logic in the Lorenzen and Lorenz tradition—which should be distinguished from the *strategy level*, the dialogical counterpart to demonstration (see Section 2.1.2). The play level is constituted by individual plays developed according to the game rules, whereas the strategy level consists in a certain perspective on all the possible plays regarding the same initial thesis. Validity belongs to the strategy level, but the meaning of statements and determining what logic is currently being used both belong to the play level through the game rules. Most non-dialogical frameworks focus on the level dealing with validity, and some dialogical ones also, following in this regard Felscher.

The constitutive role of the play level for developing a meaning explanation has been stressed by Kuno Lorenz’s definition of a proposition (Lorenz 2001: 258)[^lorenz-2001]:

> for an entity to be a proposition there must exist a dialogue game associated with this entity, i.e., the proposition *A*, such that an individual play of the game where A occupies the initial position, i.e., a dialogue $D(A)$ about *A*, reaches a final position with either win or loss after a finite number of moves according to definite rules: the dialogue game is defined as a finitary open two-person zero-sum game. Thus, propositions will in general be dialogue-definite, and only in special cases be either proof-definite or refutation-definite or even both which implies their being value-definite.

Here, “definite” refers to Lorenzen’s search for a concept which is both characteristic of propositions *and* decidable, which is one of the main reasons why he abandoned his operative logic and introduced dialogical logic (see Lorenz, 2001: 257–258)[^lorenz-2001]. That a proposition is always “dialogue-definite” means that there is always a finite dialogue for this proposition ending with victory or loss for a player. On the other hand, a proposition is not in general “proof-” or “refutation-definite” since there is no decidable provability or unprovability predicate for arbitrary propositions.

Winning and losing a play (play level) yields propositional content, without saying anything about the truth or falsity of the proposition. An immediate consequence is that the dialogical notion of validity (strategy level) will not be defined truth-functionally (see Section 2.1.2). The dialogical perspective on propositions is that of the perspective of the inside (“local”) view of the development of a play.

#### 2.1.1 The rules of the game: the play level

For the remainder of this section, $\mathcal{L}$ is a first-order language built as usual upon the propositional connectives, the quantifiers, a denumerable set of individual variables, a denumerable set of individual constants and a denumerable set of predicate symbols (each with a fixed arity). This first-order language is then extended with two labels **O** and **P**, standing for the players of the game, and the two symbols “$\state$” and “$\rqst$” standing respectively for statements and requests.

As mentioned above, in the standard dialogical framework, there are two kinds of rules called the *particle* rules and the *structural* rules, which will now be introduced. The rules of the game determine which sequences of moves are *plays*—i.e., which sequences are legal. Hence the name “play level” for the level governed by these rules. First, the particle rules will be presented and an example will be provided. Then, the structural rules will be presented and three examples will be commented.

Particle rules

Particle rules (*Partikelregeln*), or rules for logical constants, determine the legal moves in a play and regulate interaction by establishing the relevant moves constituting *challenges* and *defences*, depending on the main logical constant in the expression at stake. The appropriate challenges and defences (interaction) are the appropriate ways of asking for reasons and of giving them, and are specific to each kind of statement.

For instance, if the statement is a conjunction, there are two appropriate challenges, one for each conjunct, which consist in requesting that the other player states the chosen conjunct. There is one appropriate defence for each challenge, which consists in stating the requested conjunct. The particle rules define both the meaning of connectives and the statement based on its form. These particle rules explicit the meaning of statements in terms of the players’ various commitments and entitlements regarding each statement—i.e., what moves are allowed.

These rules govern what is called the *local level of meaning* (distinguished from the global level provided by the structural rules): each kind of statement (e.g., conjunction, disjunction, universal quantification) receive its meaning through the appropriate challenges and defences, which are spelled out by the particle rules. Thus, the meaning of the statements are constituted in a dynamic way through the appropriate interaction during a dialogical game.

Accordingly, the meaning of the statements in a dialogue does not lie in some external semantic, but is immanent to the dialogue itself, i.e., in the specific and appropriate way the players interact. (This is linked to the Wittgensteinian conception of meaning as use.) The rules are the same for the two players and the meaning of the connectives is therefore independent of who uses them. This is why the rules are formulated using the variables $\mathbf{X}$ and $\mathbf{Y}$. Recall that the symbols “!” and “?” are used for statements and requests, respectively.

For the benefit of those who are new to the dialogical framework, let us start with two particle rules, conjunction and implication.

The particle rules for a conjunction are the following: when a player $\mathbf{X}$ (either **P** or **O**) states a conjunction, the other player $\mathbf{Y}$ may challenge the conjunction by choosing one of the conjuncts (the left one $L^{\land}$ or the right one $R^{\land}$) and requesting it (? in front of the chosen conjunct). The first player $\mathbf{X}$ defends the conjunction by stating the requested conjunct.

| *Statement* | *Challenge* | *Defence* |
| --- | --- | --- |
| $\mathbf{X}\ {\state \varphi\land\psi}$ | $\mathbf{Y}\ {\rqst L^{\land}}$ or $\mathbf{Y}\ {\rqst R^{\land}}$ | $\mathbf{X}\ {\state \varphi}$ respectively $\mathbf{X}\ {\state \psi}$ |

The particle rules for the implication are the following: when $\mathbf{X}$ states an implication, $\mathbf{Y}$ may challenge it by stating the antecedent, and $\mathbf{X}$ defends it by stating the consequent.

| *Statement* | *Challenge* | *Defence* |
| --- | --- | --- |
| $\mathbf{X}\ {\state \varphi\supset\psi}$ | $\mathbf{Y}\ {\state \varphi}$ | $\mathbf{X}\ {\state \psi}$ |

Here is an example, which uses the structural rules that will be presented below. Let us consider propositional logic in this case. In order to build a play for $((p \land q) \supset p)$, one must first set up a table which will record the moves (utterances) of each player, **P** and **O**, in their respective columns.

| **O** | **P** |
| --- | --- |
|   |   |

Add an *outer column* (*A*) in which the *number of the move* will be recorded, and an *inner column* (*B*) in which the number of the *challenged move* will be recorded.

| **O** | **P** |   |   |   |   |
| --- | --- | --- | --- | --- | --- |
| move | statement | challenge to move | challenge to move | statement | move |
| *A* |   | *B* | *B* |   | *A* |
|   |   |   |   |   |   |

Next, write the *thesis*, here $((p \land q) \supset p)$, as the first statement of the play, marked “!” and made by **P**. It is move 0, so 0 is written in the outer column on **P**’s side.

| **O** | **P** |   |   |   |   |
| --- | --- | --- | --- | --- | --- |
| move | statement | challenge to move | challenge to move | statement | move |
|   |   |   |   | $\state((p \land q) \supset p)$ | 0 |

It is now **O**’s turn to play. She challenges the implication. She must state the antecedent, here $(p \land q)$. It is move 1 (outer column), and she challenges move 0 (inner column).

| **O** | **P** |   |   |   |   |
| --- | --- | --- | --- | --- | --- |
| move | statement | challenge to move | challenge to move | statement | move |
|   |   |   |   | $\state((p \land q) \supset p)$ | 0 |
| 1 | $\state(p \land q)$ | (0) |   |   |   |

It is now **P**’s turn. He can either defend the challenge on the implication, or challenge **O**’s statement (move 1). If he defends the implication, he must state the consequent (here $p$). If he challenges the conjunction, he must choose one of the conjuncts and request it.

**P** challenges the conjunction (see below the Formal Rule SR2 which compels him to do so). He requests the left conjunct.

| **O** | **P** |   |   |   |   |
| --- | --- | --- | --- | --- | --- |
| move | statement | challenge to move | challenge to move | statement | move |
|   |   |   |   | $\state ((p \land q) \supset p)$ | 0 |
| 1 | $\state(p \land q)$ | (0) |   |   |   |
|   |   |   | (1) | $\rqst L^{\land}$ | 2 |

*Note: Each challenge is written on a new line (with the number of the challenged move written in the inner column), and each defence is written on the same line as its challenge. This move 2 is a challenge on move 1 (inner column), and is a request (question mark before what is requested).*

It is now **O**’s turn. She must defend her conjunction (there is no other available move left) and state the requested conjunct. It is move 3 and she states $p$, written on the same line as the challenge.

| **O** | **P** |   |   |   |   |
| --- | --- | --- | --- | --- | --- |
| move | statement | challenge to move | challenge to move | statement | move |
|   |   |   |   | $\state((p \land q) \supset p)$ | 0 |
| 1 | $\state(p \land q)$ | (0) |   |   |   |
| 3 | $\state p$ |   | (1) | $\rqst L^{\land}$ | 2 |

It is now **P**’s turn. He must defend his implication (there is no other available move left) and state the consequent. It is move 4 and he states $p$, written on the same line as the challenge.

| **O** | **P** |   |   |   |   |
| --- | --- | --- | --- | --- | --- |
| move | statement | challenge to move | challenge to move | statement | move |
|   |   |   |   | $\state ((p \land q) \supset p)$ | 0 |
| 1 | $\state (p \land q)$ | (0) |   | $\state p$ | 4 |
| 3 | $\state p$ |   | (1) | $\rqst L^{\land}$ | 2 |

It is now **O**’s turn to play. She has no available move, so she loses the play. **P** wins.

| **O** | **P** |   |   |   |   |
| --- | --- | --- | --- | --- | --- |
| move | statement | challenge to move | challenge to move | statement | move |
|   |   |   |   | $\state ((p \land q) \supset p)$ | 0 |
| 1 | $\state (p \land q)$ | (0) |   | $\state p$ | 4 |
| 3 | $\state p$ |   | (1) | $\rqst L^{\land}$ | 2 |
| **P** wins the play. |   |   |   |   |   |

The particle rules for $\mathcal{L}$

Going back to our first-order language $\mathcal{L}$, here are the particle rules for conjunction, disjunction, implication, negation, universal quantification and existential quantification. In the rules for quantifiers, individual constants are numbered with an index $i$ from the positive integers. See below for examples of plays using these rules.

|   | Statement | Challenge | Defence |
| --- | --- | --- | --- |
| Conjunction | $\mathbf{X}\state \varphi\land\psi$ | $\mathbf{Y}\rqst L^{\land}$ or $\mathbf{Y}\rqst R^{\land}$ | $\mathbf{X}\state \varphi$ (resp.) $\mathbf{X}\state \psi$ |
| Disjunction | $\mathbf{X}\state \varphi\lor\psi$ | $\mathbf{Y}\rqst_{\lor}$ | $\mathbf{X}\state \varphi$ or $\mathbf{X}\state \psi$ |
| Implication | $\mathbf{X}\state \varphi\supset\psi$ | $\mathbf{Y}\state \varphi$ | $\mathbf{X}\state \psi$ |
| Negation | $\mathbf{X}\state \neg\varphi$ | $\mathbf{Y}\state \varphi$ | $--$ |
| Universal quantification | $\mathbf{X}\state \forall x\varphi(x)$ | $\mathbf{Y}\rqst [x/a_{i}]$ | $\mathbf{X}\state \varphi(x/a_{i})$ |
| Existential quantification | $\mathbf{X}\state \exists x\varphi(x)$ | $\mathbf{Y}\rqst_{\exists}$ | $\mathbf{X}\state \varphi(x/a_{i})$ |

The choices involved in the rules defining logical constants are important. The difference between a conjunction and a disjunction for instance is that in the case of a conjunction, it is the challenger who may choose the conjunct that will be defended, whereas in the case of a disjunction, it is the defender who may choose the disjunct. The notion of choice has a similar importance for the meaning of the quantifiers. The meaning of logical constants, therefore, is not captured only in terms of which propositions are stated or requested: choices are an essential part of the interaction process as they determine the local meaning of expressions.

Structural rules

Structural rules (*Rahmenregeln*) determine the general course of a dialogue game, such as how it is initiated, how to play it, how it ends, and so on. The point of these rules is not to spell out the meaning of the logical constants by specifying how to act in an appropriate way (this is the role of the particle rules); it is rather to specify the structure according to which interactions take place. It is one thing to determine the meaning of the logical constants as a set of appropriate challenges and defences (as above), it is another to define whose turn it is to play and when a player is allowed to play a move. One could indeed have the same local meaning (i.e., particle rules) and change a structural rule, saying for instance that one of the players is allowed to play two moves at a time instead of simply one: this would considerably change the game without changing the local meaning of what is said. This is actually one of the main ways the dialogical framework can be used in order to deal with other logical systems, and some examples are discussed in Section 2.2.

It should be noted that in some works—e.g., Sørensen and Urzyczyn (2006); Dutilh Novaes and French (2018); Dutilh Novaes (2020); French (2021)—game rules come from another framework such as sequent calculus or a “sequent perspective on natural deduction” (Dutilh Novaes & French 2018: 135)[^dutilh-2018]. What is called “structural rules” then refers to rules like weakening or contraction. In this regard, these are rather variations on the standard dialogical framework. See Section 3.3 for an example of this kind.

There are four basic structural rules in the standard dialogical framework, defining which conditions must be respected for a given sequence of moves to constitute a legitimate play.

- **SR0: Starting Rule** A play starts with the proponent stating a proposition called the *thesis*. After the thesis has been stated, the opponent chooses a positive integer which will be her *repetition rank* during the play. Then the proponent chooses his own repetition rank.

Notice that the identity of the players is established by this rule: **P** is the player who states the thesis, whereas **O** is the one who chooses her repetition rank first. According to a generalized version of this rule, a play may begin with the opponent stating initial concessions before the thesis is stated. This generalized version will be used in Section 3.2 whereas, for the sake of simplicity, Section 2 only considers the rule just presented.

- **SR1i: Intuitionistic Game-playing Rule** After the repetition ranks have been chosen, each move is a challenge or a defence in reaction to a previous move, in accordance with the particle rules shown previously. Each player can challenge the same previous move at most $\mathtt{n}$ times—where $\mathtt{n}$ is the player’s repetition rank—or defend against the adversary’s *last unanswered* challenge.

The repetition rank of the player applies to the number of challenges he is able to make against a given statement of the adversary. As for the number of defences he is able to make, the constraint is actually stronger: each challenge can be answered at most once, and only if it is the last unanswered challenge. This constraint is called the *Last Duty First* rule. See example 3, on the law of Excluded Third.

Repetition ranks ensure that plays are finite. This allows defining a simple winning condition for plays (see the Winning Rule). Different presentations of the framework have had different approaches of finiteness of plays. Some like Krabbe (1985) have introduced other means to ensure it, while others like Felscher (1985) decided to allow infinite plays (see also Hodges 2001 [2019 with Väänänen])[^hodges-2001][^hodges-2001-2], often for the sake of generality. But it is clear from Lorenz’s quote above that the framework originally defines individual plays as finite. It should be noted that, because of how the Winning Rule SR3 below defines victory, the fact that plays are always finite means that victory in a play is decidable. However, it is well-known that first-order logic is undecidable. This immediately shows that the notion of victory in a play is not the dialogical counterpart of validity. Section 2.1.2 goes into further details on that topic.

It is worth noticing that the relation between repetition ranks and victory is not as liberal as one may think at first. That is, victory will not in general be ensured simply by choosing a large repetition rank in order to overcome the adversary with more repetitions. In the case of challenges, a large repetition rank does little since the repetition rank of the adversary applies to his defences against each particular challenge. So if player $\mathbf{Y}$ is able to answer a specific challenge once, he will also be able to answer repetitions of that same challenge. In the case of defences, a large repetition ranks also does little because players have to answer to the last *unanswered* challenge. While there may be some special cases where the repetition rank has a slightly more significant influence on victory, they are not the main factor. Clerbout (2014b) discusses the relations between repetition ranks, victory, validity, and decidability.

- **SR2: Formal Rule (also known as Copy-Cat Rule)** **P** can play an atomic formula (e.g., $\Pa$) only if **O** has stated it previously in the play.

- **SR3: Winning Rule** The play ends when it is a player’s turn to make a move but he has no available move left. That player loses and the other player wins.

The Formal Rule is often described as an essential aspect of the dialogical framework, and rightly so. It is, for example, one of the most salient differences between the dialogical approach and Hintikka’s Game-Theoretical Semantics. Contrary to the other rules, the Formal Rule is not “anonymous”: it does not apply equally to both players since it puts a restriction on the moves the proponent is allowed to play. Thus, the opponent is not concerned by exactly the same rules as the proponent.

The Formal Rule accounts for analyticity: the proponent, who brings the thesis forward, will have to defend it without bringing any elementary statement (i.e., without introducing any new atomic formula) of his own in the play. His defence of the thesis will have to rely only on the elementary statements of the opponent. What is more, everything the opponent states comes only from her challenges of the proponent’s statements (especially the thesis), so that the opponent’s statements proceed from the meaning of the thesis (or, in some cases, her own initial concessions—see Section 3.2 for examples of dialogues with concessions).

This rule is also importantly connected to the topic of the dialogical account of formality (Section 2.1.3) and, for that reason, to some critics against the framework on the relation between formality and content which are discussed in Section 3. In the standard dialogical framework, the only elements whose meaning is left unspecified in formal plays are the elementary statements. The Formal Rule ensures that, in order to back the thesis, the proponent is not bringing in any elementary statement that the opponent might not agree with: the proponent can only back his thesis with elementary statements that the opponent herself has already stated. Recent developments of the framework, as discussed in Section 3.2, allow the opponent to challenge elementary statements; the proponent then needs to specify on what ground he makes this statement, thus giving rise to *material dialogues* where the meaning of elementary statements is analysed more deeply than in the standard, formal dialogues.

*Note*. It is possible to add rules for the Identity predicate, but in general these are not included in works on the standard dialogical framework. The reason for this is that no consensus on the appropriate kind of rule can seem to be reached: should there be special particle rules, thus fully embracing the idea that this predicate is a logical constant of the vocabulary? or should there be special clauses in the Formal Rule for this predicate because it is the rule that deals with elementary statements? Either way, the rules have the effect of capturing the reflexivity, transitivity, and symmetry of the Identity predicate as well as the principle of substitution of identicals.

Here is an example that liberalizes the Formal Rule so as to give special permissions to players when elementary statements involve the $\Id$ predicate. Each player is allowed to play $\Id(c_i,c_i)$. Moreover, each player is allowed to state $\Id(c_j,c_i)$ if $\Id(c_i,c_j)$ has been stated previously, as well as $\Id(c_i,c_k)$ if both $\Id(c_i,c_j)$ and $\Id(c_j,c_k)$ have been stated previously. Finally, if $\Id(c_i,c_j)$ and $\varphi(c_i)$ have been stated previously, they are allowed to state $\varphi(c_j)$.

As a side note, the Immanent Reasoning framework presented in Section 3 provides the means for delving into the meaning of the Identity predicate and distinguish it from other forms of equalities. It is not possible to give all the details in this entry, but some basic explanations will be given together with the relevant bibliography.

Three examples

Three simple examples of plays will allow to see how the rules operate.

Example 1.

Play for $(\Pa\supset(\Pa\lor\Qa))$

- **Moves 0–2:** in accordance with the Starting Rule SR0, the play starts with the proponent stating the thesis at move 0. Then the opponent chooses her repetition rank (in this case she chooses $\rank{1}$ as her rank) at move 1, and the proponent chooses his at move 2.

  | **O** | **P** |   |   |   |   |
  | --- | --- | --- | --- | --- | --- |
  | move | statement | challenge to move | challenge to move | statement | move |
  |   |   |   |   | $\state (\Pa\supset(Pa\lor{}\Qa))$ | 0 |
  | 1 | $\mathtt{n} :=\rank{1}$ |   |   | $\mathtt{m} :=\rank{1}$ | 2 |
- **Move 3:** applying the particle rule for material implication, the opponent **O** challenges the thesis by stating the antecedent. Accordingly, the number of the challenged move is indicated in the inner column.

  | **O** | **P** |   |   |   |   |
  | --- | --- | --- | --- | --- | --- |
  | move | statement | challenge to move | challenge to move | statement | move |
  |   |   |   |   | $\state (\Pa\supset(\Pa\lor{}\Qa))$ | 0 |
  | 1 | $\mathtt{n} :=\rank{1}$ |   |   | $\mathtt{m}:=\rank{1}$ | 2 |
  | 3 | $\state \Pa$ | (0) |   |   |   |
- **Move 4:** also applying the particle rule for material implication, the proponent **P** states the consequent in order to answer **O**’s challenge. In this case, the consequent is a disjunction.

  | **O** | **P** |   |   |   |   |
  | --- | --- | --- | --- | --- | --- |
  | move | statement | challenge to move | challenge to move | statement | move |
  |   |   |   |   | $\state (\Pa\supset(\Pa\lor{}\Qa))$ | 0 |
  | 1 | $\mathtt{n} :=\rank{1}$ |   |   | $\mathtt{m}:=\rank{1}$ | 2 |
  | 3 | $\state \Pa$ | (0) |   | $\state (\Pa\lor{}\Qa)$ | 4 |
- **Move 5:** the opponent **O** challenges **P**’s last statement, in accordance with the particle rule for disjunction.

  | **O** | **P** |   |   |   |   |
  | --- | --- | --- | --- | --- | --- |
  | move | statement | challenge to move | challenge to move | statement | move |
  |   |   |   |   | $\state (\Pa\supset(\Pa\lor{}\Qa))$ | 0 |
  | 1 | $\mathtt{n} :=\rank{1}$ |   |   | $\mathtt{m}:=\rank{1}$ | 2 |
  | 3 | $\state \Pa$ | (0) |   | $\state (\Pa\lor{}\Qa)$ | 4 |
  | 5 | $\rqst_{\lor}$ | (4) |   |   |   |
- **Move 6:** in order to answer **O**’s challenge at move 5, the proponent needs to choose a disjunct and state it. Because of the Formal Rule SR2, he is not allowed to choose $\Qa$ because the opponent has not previously stated it. However, **P** is allowed to choose $\Pa$ because **O** stated it at move 3.

  | **O** | **P** |   |   |   |   |
  | --- | --- | --- | --- | --- | --- |
  | move | statement | challenge to move | challenge to move | statement | move |
  |   |   |   |   | $\state (\Pa\supset(\Pa\lor{}\Qa))$ | 0 |
  | 1 | $\mathtt{n} :=\rank{1}$ |   |   | $\mathtt{m}:=\rank{1}$ | 2 |
  | 3 | $\state \Pa$ | (0) |   | $\state (\Pa\lor{}\Qa)$ | 4 |
  | 5 | $\rqst_{\lor}$ | (4) |   | $\state \Pa$ | 6 |
  | **P** wins the play. |   |   |   |   |   |

The opponent has no further possible move. Because her repetition rank is $\rank{1}$, she cannot challenge again the proponent’s move, as established in the Game-playing Rule SR1i. Notice that moves 3 to 6 follow the rule SR1i: after the repetition ranks have been chosen, each move is a challenge or a defence in reaction to a previous move. Since **O** cannot make any move after move 6, the proponent wins the play according to the Winning Rule SR3.

Example 2.

The next example involves a quantifier: $(\forall xPx\supset{}\Pa)$

This example illustrates the importance of keeping track of the order of the moves (outer columns).

- **Moves 0–3:** similarly to the previous example, the play starts with **P** stating the thesis and both players choosing their repetition ranks, in accordance with SR0. Then **O** challenges the thesis at move 3 by stating the antecedent while applying the particle rule for the material implication.

  | **O** | **P** |   |   |   |   |
  | --- | --- | --- | --- | --- | --- |
  | move | statement | challenge to move | challenge to move | statement | move |
  |   |   |   |   | $\state (\forall xPx\supset{}\Pa)$ | 0 |
  | 1 | $\mathtt{n} :=\rank{1}$ |   |   | $\mathtt{m}:=\rank{1}$ | 2 |
  | 3 | $\state \forall xPx$ | (0) |   |   |   |
- **Move 4:** in order to defend himself, the proponent would need to play an elementary statement which has not yet been stated by the opponent. Because of the Formal Rule, this is not allowed. But there is something else the proponent can do: he can challenge the statement **O** made at move 3.

  | **O** | **P** |   |   |   |   |
  | --- | --- | --- | --- | --- | --- |
  | move | statement | challenge to move | challenge to move | statement | move |
  |   |   |   |   | $\state (\forall xPx\supset{}\Pa)$ | 0 |
  | 1 | $\mathtt{n} :=\rank{1}$ |   |   | $\mathtt{m}:=\rank{1}$ | 2 |
  | 3 | $\state \forall xPx$ | (0) |   |   |   |
  |   |   |   | (3) | $\rqst [x/a]$ | 4 |
  *Note that move 4 does not appear in front of move 3 since it is not a defence against that move: it is a new challenge. With his challenge, the proponent applies the particle rule for universal quantification and chooses the individual constant $a$.*
- **Moves 5–6:** **O** defends her universal quantification by instanciating her statement with **P**’s choice of instance (see the particle rule). By doing so, she states the elementary statement that the proponent needed in order to answer to move 3: he does so with move 6, which is written in front of the corresponding challenge. With this the proponent wins the play.

  | **O** | **P** |   |   |   |   |
  | --- | --- | --- | --- | --- | --- |
  | move | statement | challenge to move | challenge to move | statement | move |
  |   |   |   |   | $\state (\forall xPx\supset{}\Pa)$ | 0 |
  | 1 | $\mathtt{n} :=\rank{1}$ |   |   | $\mathtt{m}:=\rank{1}$ | 2 |
  | 3 | $\state \forall xPx$ | (0) |   | $\state \Pa$ | 6 |
  | 5 | $\state \Pa$ |   | (3) | $\rqst [x/a]$ | 4 |
  | **P** wins the play. |   |   |   |   |   |

Example 3.

The third example illustrates the *Last Duty First* restriction of the Intuitionistic Game-playing Rule: $(\Pa\lor\neg{}\Pa)$

- **Moves 0–3:** the play starts with **P** stating the thesis and both players choosing their repetition ranks, in accordance with SR0. Then **O** challenges the thesis at move 3 by applying the particle rule for disjunction (request).

  | **O** | **P** |   |   |   |   |
  | --- | --- | --- | --- | --- | --- |
  | move | statement | challenge to move | challenge to move | statement | move |
  |   |   |   |   | $\state \Pa\lor\neg{}\Pa$ | 0 |
  | 1 | $\mathtt{n} :=\rank{1}$ |   |   | $\mathtt{m}:=\rank{2}$ | 2 |
  | 3 | $\rqst_{\lor}$ | (0) |   |   |   |
- **Move 4:** in order to defend himself, the proponent must choose one of the components of the disjunction. But one is an elementary statement which has not yet been played by the opponent. So the proponent’s only choice is to choose the other disjunct and state $\neg{}\Pa$.

  | **O** | **P** |   |   |   |   |
  | --- | --- | --- | --- | --- | --- |
  | move | statement | challenge to move | challenge to move | statement | move |
  |   |   |   |   | $\state \Pa\lor\neg{}\Pa$ | 0 |
  | 1 | $\mathtt{n} :=\rank{1}$ |   |   | $\mathtt{m}:=\rank{2}$ | 2 |
  | 3 | $\rqst_{\lor}$ | (0) |   | $\state \neg{}\Pa$ | 4 |
- **Move 5:** the opponent challenges this statement by stating $\Pa$, in accordance with the particle rule for negation. According to the particle rule for negation, there is no move that the proponent may play to defend himself against the opponent’s last challenge. There is nothing **P** can challenge, since **O**’s only statement is elementary. He loses the play.

  | **O** | **P** |   |   |   |   |
  | --- | --- | --- | --- | --- | --- |
  | move | statement | challenge to move | challenge to move | statement | move |
  |   |   |   |   | $\state \Pa\lor\neg{}\Pa$ | 0 |
  | 1 | $\mathtt{n} :=\rank{1}$ |   |   | $\mathtt{m}:=\rank{2}$ | 2 |
  | 3 | $\rqst_{\lor}$ | (0) |   | $\state \neg{}\Pa$ | 4 |
  | 5 | $\state \Pa$ | (4) |   |   |   |
  | **O** wins the play. |   |   |   |   |   |

What about answering a second time to the opponent’s move 3? Even though his repetition rank is $\rank{2}$ and the opponent stated $\Pa$ at move 5, the proponent cannot answer a second time to move 3 by choosing the first disjunct. This is because move 3 is no longer the last unanswered challenge made by the opponent: at this point, move 5 is the last one. Thus, the proponent has no further possible move and he loses the play. Notice that, unlike the proof-theoretic account of intuitionistic logic, the meaning of the Excluded Third does not amount to knowing what could count as having a proof of it but to the fact that it can constitute the thesis of a play that ends with one of the players winning or losing. The proof-theoretic account of knowing what counts as having a proof manifests itself, in a dialogical setting, in terms of having a winning *strategy*. See Section 2.2.1 for classical dialogical games which have rules that allow **P** to win.

#### 2.1.2 The strategy level

The level of strategies is the level at which one can study games in terms of collections of plays rather than staying at the level of individual plays. There may be various reasons to do so. The main reason is that one may thus determine whether a player can win no matter how his adversary would play, and not just whether that player happens to win a particular play. This distinction is important for validity. To understand the distinction, consider first the following play:

| **O** | **P** |   |   |   |   |
| --- | --- | --- | --- | --- | --- |
| move | statement | challenge to move | challenge to move | statement | move |
|   |   |   |   | $\state (\Pa\land(\Pa\supset{}\Pa))$ | 0 |
| 1 | $\mathtt{n} :=\rank{1}$ |   |   | $\mathtt{m}:=\rank{1}$ | 2 |
| 3 | $\rqst R^{\land}$ | (0) |   | $\state (\Pa\supset{}\Pa)$ | 4 |
| 5 | $\state \Pa$ | (4) |   | $\state \Pa$ | 6 |
| **P** wins the play. |   |   |   |   |   |

**Explanations**

- **Moves 0–3:** **P** states the thesis and the players choose their repetition rank. **O** challenges the thesis, which is a conjunction, by requesting the right conjunct.
- **Moves 4–6:** **P** states the right conjunct, it is an implication. **O** challenges it by stating the antecedent, and **P** defends it by stating the consequent.

The proponent wins this play. But one may wonder if there is not something that the opponent could do in order to win. In fact, this question arises quite naturally if one is curious about the relationship between winning a play and proving the validity of a thesis in a dialogical setting. In the play above, the proponent happens to win a play for a formula that is clearly not valid. Now, it is quite easy to see that, in fact, the opponent had a way to win by making another choice at move 3:

| **O** | **P** |   |   |   |   |
| --- | --- | --- | --- | --- | --- |
| move | statement | challenge to move | challenge to move | statement | move |
|   |   |   |   | $\state (\Pa\land(\Pa\supset{}\Pa))$ | 0 |
| 1 | $\mathtt{n} :=\rank{1}$ |   |   | $\mathtt{m}:=\rank{1}$ | 2 |
| 3 | $\rqst L^{\land}$ | (0) |   |   |   |
| **O** wins the play. |   |   |   |   |   |

In this play, the opponent chooses the left part of the conjunction when challenging the thesis. In order to defend, the proponent must bring forward an elementary statement. But since the opponent has not stated it previously, the Formal Rule prevents the proponent from defending the thesis. Since the proponent has no other available move, he loses the play, as established by the Winning Rule (SR3).

Thus, it is possible for the proponent to win merely because the opponent has played poorly. Conversely, it is also possible for the proponent to lose for having made the wrong choice:

| **O** | **P** |   |   |   |   |
| --- | --- | --- | --- | --- | --- |
| move | statement | challenge to move | challenge to move | statement | move |
|   |   |   |   | $\state ((\Pa\land{}\Qa)\lor(\Pa\supset{}\Pa))$ | 0 |
| 1 | $\mathtt{n} :=\rank{1}$ |   |   | $\mathtt{m}:=\rank{1}$ | 2 |
| 3 | $\rqst_{\lor}$ | (0) |   | $\state (\Pa\land{}\Qa)$ | 4 |
| 5 | $\rqst L^{\land}$ | (4) |   |   |   |
| **O** wins the play. |   |   |   |   |   |

After move 5, there is nothing the proponent can do: he cannot answer to move 5 because of the Formal Rule. But at move 4 the proponent was able to choose which disjunct to state in order to defend. Had he chosen the other disjunct, he would have been able to win:

| **O** | **P** |   |   |   |   |
| --- | --- | --- | --- | --- | --- |
| move | statement | challenge to move | challenge to move | statement | move |
|   |   |   |   | $\state ((\Pa\land{}\Qa)\lor(\Pa\supset{}\Pa))$ | 0 |
| 1 | $\mathtt{n} :=\rank{1}$ |   |   | $\mathtt{m}:=\rank{1}$ | 2 |
| 3 | $\rqst_{\lor}$ | (0) |   | $\state (\Pa\supset{}\Pa)$ | 4 |
| 5 | $\state \Pa$ | (4) |   | $\state \Pa$ | 6 |
| **P** wins the play. |   |   |   |   |   |

In order to reason about a collection of plays and consider questions such as “what would happen if player $\mathbf{X}$ had made another choice?”, game-theoretical settings have the key concept of *strategies*. There are various equivalent ways to define strategies, though in the Lorenzen and Lorenz tradition, winning strategies can be built from plays through a procedure that allows to check if every possible choice of **P** has been taken into account. However, in the context of results connecting the dialogical framework with other frameworks, it is useful and quite common to identify strategies with their extensive forms. Here are the relevant definitions.

Simply put, a *strategy* for player $\mathbf{X}$ in a dialogical game is a complete conditional plan of action. It is conditional in the sense that the strategy informs how $\mathbf{X}$ plays depending on the moves of the adversary. It is complete in the sense that it must inform how $\mathbf{X}$ plays for every possible choice of move by the adversary. Given a formula $\varphi$, a strategy for $\mathbf{X}$ in the game for $\varphi$ can be described as a function that assigns an $\mathbf{X}$-move $M$ to every non-terminal play $\Delta$ ending with a $\mathbf{Y}$-move such that extending $\Delta$ with $M$ results in a play for $\varphi$. Such a strategy is *winning* if all terminal plays resulting from it are $\mathbf{X}$-terminal (i.e., won by $\mathbf{X}$). In other words, a winning strategy for a player is a complete conditional plan of action leading to the player’s victory no matter how the adversary plays.

The *extensive form* of a dialogical game $\mathcal{D}(\varphi)$ for $\varphi$ is simply the tree representation of the game, where each path represents a play and branches represent terminal plays. Thus, the extensive form $\mathfrak{E}_{\varphi}$ of $\mathcal{D}(\varphi)$ is the tree ($T$, $\ell$, $S$) such that:

- Every node $t\in{}T$ is labelled with a move $M$ in $\mathcal{D}(\varphi)$
- $\ell: T\longrightarrow\mathbb{N}$
- $S\subseteq{}T^{2}$ such that:
- There is a unique $t_{0}\in{}T$ labelled with the thesis of $\mathcal{D}(\varphi)$ and such that $\ell(t_{0})=0$,
- For every $t\neq{}t_{0}$ there is a unique $t'$ such that $t'St$,
- For every $t$, $t'\in{}T$, if $tSt'$ then $\ell(t')=\ell(t)+1$,
- For every play $\Delta\in\mathcal{D}(\varphi)$, if move $M'$ immediately follows move $M$ in $\Delta$ then there are nodes $t$ and $t'$ in $T$ such that $\ell(t')=\ell(t)+1$, $t$ is labelled with $M$ and $t'$ is labelled with $M'$.

Being identified with its extensive form, a strategy for player $\mathbf{X}$ in $\mathcal{D}(\varphi)$ is the fragment $S_{x}$ of $\mathfrak{E}_{\varphi}$ such that each path in $S_{x}$ represents a play resulting from the $\mathbf{X}$ strategy. In other words: (i) for every node $t$ in $\mathfrak{E}_{\varphi}$ labelled with an $\mathbf{X}$ move, every successor of $t$ in $\mathfrak{E}_{\varphi}$ appears in $S_{x}$ whenever $t$ is in $S_{x}$; and (ii) for every node $t$ in $\mathfrak{E}_{\varphi}$ labelled with a $\mathbf{Y}$ move, if there is at least a successor for $t$ in $\mathfrak{E}_{\varphi}$ then there is a unique $t'$ labelled with an $\mathbf{X}$ move such that $t'$ is the successor of $t$ in $S_{x}$ and $t'$ is the move prescribed by the strategy. Thus, in an $\mathbf{X}$ strategy the ramifications corresponding to $\mathbf{X}$ having multiple choices are not kept (since a given strategy selects *one* $\mathbf{X}$ move) but the ones corresponding to $\mathbf{Y}$’s choices are kept (since the strategy must consider all possible moves of $\mathbf{Y}$).

Here are some examples of results which pertain to the level of strategies. For details on the proofs of most of these results, see Clerbout (2014a):

- Winning **P** strategies and leaves. Let $S_{p}$ be a winning **P** strategy in the game for $\varphi$. Then every leaf in $S_{p}$ is labelled with a **P** elementary statement.
- Determinacy. There is a winning $\mathbf{X}$ strategy in the game for $\varphi$ if and only if there is no winning $\mathbf{Y}$ strategy in this game.
- Soundness/Completeness of Tableaux. Felscher (1985) showed that there is a tableau proof for $\varphi$ if and only if there is a winning **P** strategy in the intuitionistic dialogical game for $\varphi$. This being the first correct and complete proof, it is very influential in some dialogical traditions, despite the fact that Felscher’s rules do not guarantee finiteness of plays. Clerbout (2014a) showed that tableaux for classical logic (Smullyan 1968)[^smullyan-1968] are sound and complete for classical dialogical games as defined in Section 2.2.1, i.e., with repetition ranks. By soundness and completeness of the tableau method with respect to model-theoretic semantics, it follows that existence of a winning **P** strategy coincides with validity: There is a winning **P** strategy in the game for $\varphi$ if and only if $\varphi$ is valid. The correspondence between the dialogical approach and other frameworks such as tableaux is to be found at the level of strategies, and more precisely of strategies for the proponent. So, from the dialogical point of view, tableaux rules are limited to how (particle) rules are applied in the context of a **P**-strategy; they are thus insensitive to the play level (where semantics is defined in terms of interaction). In fact, in the demonstration of the equivalence it is made clear how transforming a winning **P**-strategy into a tableau proof supposes getting rid of most elements constitutive of interaction (such as most challenges) until the player labels **O** and **P** become nothing more than an alternative way of writing the usual tableau signatures $T$ and $F$.

#### 2.1.3 Formality

As pointed out when presenting the structural rule in Section 2.1.1, the Formal Rule is one of the most salient features of the dialogical framework. With this rule the dialogical approach comes with an internal account of elementary propositions in terms of interaction only, without depending on metalogical meaning explanations for the non-logical vocabulary. More prominently, this means that the dialogical account does not rely—contrary to Hintikka’s GTS games—on the model-theoretic approach to meaning for elementary propositions. Hence, just as Lorenz (2001) clearly stated, the dialogical notion of proposition does not assume truth-conditional semantics.

Just like the particle rules for logical constants, the Formal Rule sets the meaning of elementary statements purely in terms of dialogical interaction. This has clear roots in the Ancient Greek tradition of logic, most particularly in Plato and Aristotle. Lorenzen alluded to Greek dialectics in his 1960 paper. On this matter, Marion and Rückert (2016) discuss how the dialogical framework can directly be related with this Platonist and Aristotelian conception. Plato’s *Gorgias* (472b–c), for example, expresses an idea which can be freely summed up with the following statement:

> *there is no better grounding of an assertion within an argument than indicating that it has already been conceded by the opponent or that it follows from these concessions.*

The dialogical account of formality is rooted in this idea. Indeed:

1. formality is understood as a kind of *interaction*; and
2. formal reasoning *should not* be understood as devoid of content and reduced to purely syntactic moves.

In the case of the Formal Rule seen in Section 2.1.1, point 1 is clearly accounted for. Point 2, however, is maybe less obvious and some objections against the dialogical framework are directly related to the topic on content. These objections are sometimes collectively referred to as “the content challenge” (see Section 3.1). Indeed, in the standard dialogical framework there is no way of asking for reasons for elementary statements and giving them: in this sense, the form of interaction differs notably from the one defined for statements having logical constants. As a consequence, some interpretations of standard dialogical logic did understand plays in a purely syntactic manner. Thus, the standard formulation seems particularly prone to the frequent criticism against formal reasoning and logic according to which they are reduced to syntactic manipulation devoid of content. Various answers have been provided, see Section 3.

### 2.2 Other logics in the dialogical framework: dialogical pluralism

In the 1990s and the 2000s, the original ideas of the dialogical approach were developed by Shahid Rahman and collaborators into a conceptual framework that proved useful for studying, comparing and even combining non-classical logics (Rückert 2011)[^rückert-2011]. These developments led to *dialogical pluralism* (see in particular Rahman & Keiff 2005 and Keiff 2007)[^keiff-2007][^rahman-2005]. In a nutshell, this pluralism studies the semantic and logical consequences of modifying the structural rules or extending the set of logical constants. The general idea is that different logics involve different ways to deal with information in (sub)plays (a subplay is simply a sequence of moves within a play; this notion is particularly useful when comparing plays which have a common initial segment but differ in two different subplays resulting from a player’s choice). The task is then to determine what information gets transferred from one play to another and how this transfer operates. Two general cases may be distinguished:

1. The information-transfer is regulated by means of specific structural rules (global level); in some cases, however, these additional rules can be prompted by operators. Example 1: in classical logic the specific structural rule is not related to special additional operators. Example 2: modal logics are a case where the specific structural rules are related to the modal operators whose local meaning gets defined by particle rules.
2. The information-transfer is already regulated with the particle rules for special operators (local level). Example: the dialogical approach to linear logic. This is Girard’s point in distinguishing additives from multiplicatives, as they should not (as in the standard approach to modal logic) be defined through structural rules (global level) but through particle rules (local level) as two different connectives (or operators) of interaction.

This section presents with more details the examples of classical and basic modal logics within the dialogical framework. The section ends with some literature relevant to the dialogical approaches of various logics and to dialogical pluralism.

#### 2.2.1 Dialogues for classical first-order logic

Section 2.1 presented the dialogical framework for intuitionistic logic. Classical logic results when a structural rule is modified: the Game-playing Rule SR1. In the dialogical setting, the logical constants have the same local meaning, which manifests itself by the fact that the particle rules are the same. The difference between classical and intuitionistic logic appears as a difference in the structural rules (namely in SR1). Structural rules are mainly procedural rules for the development of a dialogue and, although these procedural rules may have an effect on *how* the local meaning of logical constants is implemented *in the course of a play*, this does not amount to a change in the local meaning of the logical constants. In other words, the development of a play, for both intuitionistic and classical logic, assumes that the interaction follows the same particle rules (local meaning) for the logical constants.

For Classical dialogical games, the following structural rule SR1c replaces SR1i provided in Section 2.1.1.

- **SR1c: Classical Game-playing Rule** After repetition ranks have been chosen, each move is a challenge or a defence in reaction to a previous move, in accordance with the particle rules shown previously. Each player can challenge the same previous move, or defend against the same previous challenge, at most *n* times, where *n* is that player’s repetition rank.

This rule is a liberalized version of the Intuitionistic Game-Playing Rule insofar as the *Last Duty First* constraint disappears. The rest of the rule is identical to the rule from the previous Section. As a result of the liberalization, information that would maybe not be available to players in some subplays in intuitionistic dialogical games (due to the intuitionistic constraint) becomes available. Thus, classical logic results from allowing more information to be available between different parts of a play. Notice that this availability of information does not suppose changing to a truth-functional concept of proposition: the dialogical definition of *proposition* remains unchanged since availability of elementary statements in an argumentative debate does not commit to their being true.

To see the difference with intuitionistic dialogical games, consider the following example. This is a play for a thesis we have seen at the end of Section 2.1.1, but played this time with the Classical Game-Playing Rule (SR1c).

| **O** | **P** |   |   |   |   |
| --- | --- | --- | --- | --- | --- |
| move | statement | challenge to move | challenge to move | statement | move |
|   |   |   |   | $\state \Pa\lor\neg{}\Pa$ | 0 |
| 1 | $\mathtt{n} :=\rank{1}$ |   |   | $\mathtt{m}:=\rank{2}$ | 2 |
| 3 | $\rqst_{\lor}$ | (0) |   | $\state \neg{}\Pa$ | 4 |
| 5 | $\state \Pa$ | (4) |   |   |   |
|   |   |   |   | $\state \Pa$ | 6 |
| **P** wins the play. |   |   |   |   |   |

**Explanations**

- **Moves 0–5:** the play develops exactly as in the intuitionistic dialogical game for the same thesis.
- **Move 6:** This time, the proponent is not restricted by the *Last Duty First* SR1i rule. Since his repetition rank is $\rank{2}$, he is allowed to answer a second time to the opponent’s challenge made at move 3. And since **O** played the elementary statement $\Pa$ at move 5, **P** is able to choose it and play it at move 6. The opponent has no other possible move and the proponent wins this play.

#### 2.2.2 Dialogues for basic modal logic

In the case of modal logic, the information transfer between subplays is regulated by structural rules which are related to the modal operators, introduced in the object-language, which get their local meaning through corresponding particle rules. This is the general dialogical tenet on modal logic. The differences between distinct normal modal systems (such as **K**, **T**, **B**, etc.) manifest as differences in the dedicated structural rules while the local meaning of the operators remains unchanged.

The case of modal logics is probably one in which the process of distinguishing between subplays is made the most explicit. The idea of the dialogical approach to modal logics is to add a further element to the information about moves: in addition to the player who performs the move, and the nature of the move (statement or request), each move comes with a label indicating in which dialogical context it is performed. The particle rules for modal operators define how changes of dialogical contexts are triggered. The result is the generation of different subplays which are distinguished by the dialogical contexts assigned to them. Accordingly, and given the usual definition of the basic modal language, the particle rules are:

|   | Statement | Challenge | Defence |
| --- | --- | --- | --- |
| Conjunction | $\mathbf{X}\state A\land{}B - c_{i}$ | $\mathbf{Y}\rqst L^{\land} - c_{i}$ or $\mathbf{Y}\rqst R^{\land} - c_{i}$ | $\mathbf{X}\state A - c_{i}$ (resp.) $\mathbf{X}\state B - c_{i}$ |
| Disjunction | $\mathbf{X}\state A\lor{}B - c_{i}$ | $\mathbf{Y}\rqst_{\lor} - c_{i}$ | $\mathbf{X}\state A - c_{i}$ or $\mathbf{X}\state B - c_{i}$ |
| Implication | $\mathbf{X}\state A\supset{}B - c_{i}$ | $\mathbf{Y}\state A - c_{i}$ | $\mathbf{X}\state B - c_{i}$ |
| Negation | $\mathbf{X}\state \neg{}A - c_{i}$ | $\mathbf{Y}\state A - c_{i}$ | $--$ |
| Necessity operator | $\mathbf{X}\state \square A - c_{i}$ | $\mathbf{Y}\rqst [c_{j}/c_{i}]$ | $\mathbf{X}\state A - c_{j}$ |
| Possibility operator | $\mathbf{X}\state \lozenge A - c_{i}$ | $\mathbf{Y}\rqst_{\lozenge}$ | $\mathbf{X}\state A - c_{j}$ |

The particle rules for propositional connectives are like those in Section 2.1.1, with an additional indication concerning the dialogical context (denoted $c_{i}$), which, however, does not modify the current context. Propositional connectives are thus unlike unary connectives such as modal operators, which provoke a dialogical context change according to the particle rules. In this regard, the only difference between the possibility operator and the necessity operator pertains to which player may choose the new context (in the rule for the necessity operator, “$c_{j}/c_{i}$” is read as the request to substitute $c_j$ for $c_i$). This point illustrates once again the key role of choice in the dialogical approach to meaning built through the game rules.

This integration of the “local” perspective *of the players* into the framework is an important proposal. Dialogical contexts are labels used to identify different parts (subplays) of a given dialogue and thus keep track of the information flow between these parts. This can be seen as a step towards *hybridation* (having syntactical tools to name states or worlds). Patrick Blackburn (2001) argued, however, that a thorough discussion of the benefits of such an integration advocates for a complete hybridation and that the idea behind dialogical modal logics should be pursued to its fullest. Thus, from a model-theoretic perspective, dialogical contexts will correspond to (names of) possible worlds. But one important difference is that in the dialogical framework the contexts are explicitly part of the players’ interaction through particle rules and through the special structural rule introduced below.

The way information is transferred from one subplay to another is managed at the level of structural rules, which need to be updated in order to account for the presence of dialogical contexts in the moves. The rules seen in Section 2.1.1 remain, although relativized to dialogical contexts. An additional special rule is added about context changes.

- **SR0: Starting Rule** A play starts with the proponent **P** stating a proposition, called the thesis, *at context* $c_{1}$. After the thesis has been stated, the opponent **O** chooses a positive integer which will be her repetition rank during the play. Then the proponent **P** chooses his own repetition rank. *Repetition ranks are chosen at context $c_{1}$*.

- **SR1: Game-playing Rule** After repetition ranks have been chosen, each move is a challenge or a defence in reaction to a previous move, in accordance with the particle rules. Each player can challenge the same previous move, or defend against the same previous challenge, at most *n* times, where *n* is that player’s repetition rank.

Notice that it is possible to play with the intuitionistic version of this rule and, thus, to combine aspects from intuitionistic dialogical logic and modal dialogical logic.

- **SR2: Formal Rule (also known as Copy-Cat Rule)** **P** can state an elementary statement *at some context* $c_{i}$ only if **O** stated it beforehand in the play *at this context* $c_{i}$.

This relativization of the Formal Rule to contexts is an essential part of the dialogical approach to modal logic. Close attention should be paid to how information is transferred between subplays: it is crucial to know clearly what elementary statements **P** is allowed to make *at any given context*.

- **SR3: Winning Rule** The play ends when it is a player’s turn to make a move but he has no available move left. That player loses and the other player wins.

In addition to these familiar rules, an extra rule is needed to give an account of how new contexts may be generated by means of the particle rules for modal operators. This, combined with the Formal Rule relativized to dialogical contexts, is the way in which the transfer of information is regulated in dialogical games for modal logics.

Different constraints on the transfer of information (that is to say, ultimately, on the generation of new contexts) mean different possible versions of a rule regulating it. A first example is the following one:

- **SRK: K-availability of contexts** Whenever he is to choose a context when applying the particle rule of a modal operator, **P** can choose context $c_{j}$ at $c_{i}$ only if **O** chose $c_{j}$ at $c_{i}$ beforehand.

Like the Formal Rule, this rule is asymmetrical: it puts restrictions on the proponent’s ability to choose new contexts. Both rules specify how information—about elementary statements or contexts—becomes available to **P** only if **O** has previously provided it.

This structural rule SRK embodies the dialogical definition of the modal system **K**. Various versions of this rule can be used to account for other (normal) modal systems. In this fashion, the (normal) modal systems’ differences are manifested in the dialogical approach through different constraints on context information available to **P** (Rahman & Keiff 2005)[^rahman-2005]. Here is an example of a play resulting from the rules seen so far (i.e., with SRK):

| **O** | **P** |   |   |   |   |   |   |
| --- | --- | --- | --- | --- | --- | --- | --- |
| move | context | statement | challenge to move | challenge to move | statement | context | move |
|   |   |   |   |   | $\state \square(p\supset{}q)\supset(\square{}p\supset\square{}q)$ | $c_{1}$ | 0 |
| 1 | $c_{1}$ | $\mathtt{n} :=\rank{1}$ |   |   | $\mathtt{m}:=\rank{2}$ | $c_{1}$ | 2 |
| 3 | $c_{1}$ | $\state \square(p\supset{}q)$ | (0) |   | $\state \square{}p\supset\square{}q$ | $c_{1}$ | 4 |
| 5 | $c_{1}$ | $\state \square{}p$ | (4) |   | $\state \square{}q$ | $c_{1}$ | 6 |
| 7 | $c_{1}$ | $\rqst [c_{2}/c_{1}]$ | (6) |   | $\state q$ | $c_{2}$ | 14 |
| 9 | $c_{2}$ | $\state p\supset{}q$ |   | (3) | $\rqst [c_{2}/c_{1}]$ | $c_{1}$ | 8 |
| 11 | $c_{2}$ | $\state p$ |   | (5) | $\rqst [c_{2}/c_{1}]$ | $c_{1}$ | 10 |
| 13 | $c_{2}$ | $\state q$ |   | (9) | $\state p$ | $c_{2}$ | 12 |
| **P** wins the play. |   |   |   |   |   |   |   |

The constraints on contexts available to **P** can be made stronger or weaker, as the following rules for other well-known modal systems illustrate. In some cases an example is added to illustrate the rule and in each example the move where the corresponding rule is applied is indicated.

- **SRT: T-availability of contexts** Whenever he is to choose a context when applying the particle rule of a modal operator, **P** can choose context $c_{j}$ at $c_{i}$ only if **O** chose $c_{j}$ at $c_{i}$ beforehand, or $c_{i}=c_{j}$.

Example:

| **O** | **P** |   |   |   |   |   |   |
| --- | --- | --- | --- | --- | --- | --- | --- |
| move | context | statement | challenge to move | challenge to move | statement | context | move |
|   |   |   |   |   | $\state \square{}p\supset{}p$ | $c_{1}$ | 0 |
| 1 | $c_{1}$ | $\mathtt{n} :=\rank{1}$ |   |   | $\mathtt{m}:=\rank{2}$ | $c_{1}$ | 2 |
| 3 | $c_{1}$ | $\state \square{}p$ | (0) |   | $\state p$ | $c_{1}$ | 6 |
| 5 | $c_{1}$ | $\state p$ |   | (3) | $\rqst [c_{1}/c_{1}]$ | $c_{1}$ | 4 |
| **P** wins the play. |   |   |   |   |   |   |   |

- **SRKB: KB-availability of contexts** Whenever he is to choose a context when applying the particle rule of a modal operator, **P** can choose context $c_{j}$ at $c_{i}$ only if **O** chose $c_{j}$ at $c_{i}$ beforehand, or **O** chose $c_{i}$ at $c_{j}$ beforehand.

Example:

| **O** | **P** |   |   |   |   |   |   |
| --- | --- | --- | --- | --- | --- | --- | --- |
| move | context | statement | challenge to move | challenge to move | statement | context | move |
|   |   |   |   |   | $\state p\supset\square\lozenge{}p$ | $c_{1}$ | 0 |
| 1 | $c_{1}$ | $\mathtt{n} :=\rank{1}$ |   |   | $\mathtt{m}:=\rank{2}$ | $c_{1}$ | 2 |
| 3 | $c_{1}$ | $\state p$ | (0) |   | $\state \square\lozenge{}p$ | $c_{1}$ | 4 |
| 5 | $c_{1}$ | $\rqst [c_{2}/c_{1}]$ | (4) |   | $\state \lozenge{}p$ | $c_{2}$ | 6 |
| 7 | $c_{2}$ | $\rqst_{\lozenge}$ | (6) |   | $\state p$ | $c_{1}$ | 8 |
| **P** wins the play. |   |   |   |   |   |   |   |

- **SRB: B-availability of contexts** Whenever he is to choose a context when applying the particle rule of a modal operator, **P** can choose context $c_{j}$ at $c_{i}$ only if **O** chose $c_{j}$ at $c_{i}$ beforehand, or **O** chose $c_{i}$ at $c_{j}$ beforehand, or $c_{i}=c_{j}$.

- **SRS4: S4-availability of contexts** Whenever he is to choose a context when applying the particle rule of a modal operator, **P** can choose context $c_{j}$ at $c_{i}$ only if **O** chose $c_{j}$ at $c_{i}$ beforehand, or $c_{i}=c_{j}$, or there is a context $c_{k}$ such that **P** can choose $c_{k}$ at $c_{i}$, and $c_{j}$ at $c_{k}$.

- **SRS5: S5-availability of contexts** Whenever he is to choose a context when applying the particle rule of a modal operator, **P** can choose context $c_{j}$ at $c_{i}$ only if **O** chose $c_{j}$ at $c_{i}$ beforehand, or $c_{i}=c_{j}$, or **O** chose $c_{i}$ at $c_{j}$ beforehand, or there is a context $c_{k}$ such that **P** can choose $c_{k}$ at $c_{i}$ and $c_{j}$ at $c_{k}$.

Example:

| **O** | **P** |   |   |   |   |   |   |
| --- | --- | --- | --- | --- | --- | --- | --- |
| move | context | statement | challenge to move | challenge to move | statement | context | move |
|   |   |   |   |   | $\state \lozenge{}p\supset\square\lozenge{}p$ | $c_{1}$ | 0 |
| 1 | $c_{1}$ | $\mathtt{n} :=\rank{1}$ |   |   | $\mathtt{m}:=\rank{2}$ | $c_{1}$ | 2 |
| 3 | $c_{1}$ | $\state \lozenge{}p$ | (0) |   | $\state \square\lozenge{}p$ | $c_{1}$ | 4 |
| 5 | $c_{1}$ | $\rqst [c_{2}/c_{1}]$ | (4) |   | $\state \lozenge{}p$ | $c_{2}$ | 6 |
| 7 | $c_{2}$ | $\rqst_{\lozenge}$ | (6) |   | $\state p$ | $c_{3}$ | 10 |
| 9 | $c_{3}$ | $\state p$ |   | (3) | $\rqst_{\lozenge}$ | $c_{1}$ | 8 |
| **P** wins the play. |   |   |   |   |   |   |   |

#### 2.2.3 Literature on other logics in the dialogical framework

A detailed account of recent developments on, among others, relevant logic, linear logic and paraconsistent logic can be found in Rahman and Keiff (2005), Rückert (2011) and Rahman (2012). Helge Rückert’s book includes a dialogical approach to multivalued logics, which is a topic that has been studied in a different way by Fermüller (2008) and Fermüller and Roschger (2014). An important development on the relations between dialogical logic and constructive mathematics was made in Coquand (1995). Keiff (2004) and Keiff (2007) are other works on the dialogical approach to modal logic. Fiutek et al. (2010) studied the dialogical approach to belief revision. The framework has been used to propose fruitful reconstructions of various logical traditions such as, among others, medieval *obligationes* (Dutilh Novaes 2007; Popek 2012)[^dutilh-2007][^popek-2012], Jain logic (Clerbout et al. 2011)[^clerbout-2011], or Aristotle’s syllogistic (Crubellier et al. 2019)[^crubellier-2019]. Redmond (2011) developed a dialogical approach to fiction, building on previous works on free logics. The book of Fontaine (2013) deals with intentionality, fiction and dialogues, the book of Magnier (2013) deals with dynamic epistemic logic and legal reasoning in a dialogical framework, while the work of Shafiei (2018) gives dialogical foundations to the phenomenological approach to meaning, intentionality, and reasoning.

A different take on dialogical pluralism is hinted at by Dutilh Novaes and French (2018), Dutilh Novaes (2020), and French (2021), in which pluralism stems from the dialogical reading of the structural rules of sequent calculus or natural deduction. An important recent work on the relations between sequent calculus and the dialogical approach is Fermüller (2021).

## 3. Variations on the Standard Dialogical Framework

The previous section presented the standard dialogical framework in the Lorenzen and Lorenz tradition. Different logics can be expressed within this framework, they can thus also be compared (e.g., classical and intuitionistic logic, and modal logics). Different objections have been raised against the standard framework, as the three objections presented below attest; various answers have been given by logicians interested in the dialogical perspective, often abandoning the Lorenzen and Lorenz tradition 1 in order to build a framework most appropriate to their own purposes (for other objections and their answer, see Rückert 2001)[^rückert-2001].

In this section two variations of the standard framework are briefly considered, with their answers to objections made to the standard framework: the Immanent Reasoning framework maintains itself in the initial tradition, whereas the Built-In Opponent (BIO) framework distances itself from the standard approach.

### 3.1 Objections against the standard dialogical framework

**The standard dialogical framework is too formal.** A recurrent objection made to the standard dialogical framework is that it is too formal, in the sense that the dialogues in this “dialogical” logic are not real dialogues, with actual content, they only deal with the logical constants. See for instance Hintikka (1973: 77–82), Peregrin (2014: 100, 106), Trafford (2017: 86–88), and Dutilh Novaes and French (2018: 131).

At least two options adopted provide an answer to this objection: one, which is not in the Lorenzen and Lorenz tradition, consists in linking dialogues with empirical social interaction in line with argumentation theory (Barth & Krabbe 1982; Gethmann 1979, for example)[^barth-1982][^gethmann-1979]; the other intends to stay in the Lorenzen and Lorenz tradition and go all the way with dialogues, which supposes providing content through dialogical means. The Immanent Reasoning framework’s *material dialogues* is a proposal to deal with this contentual aspect, especially regarding elementary propositions. Such a project is consistent with the work of Lorenz (1970; 2009; 2010; 2011), which deals with predication from a dialogical perspective, discussing the interaction between perceptual and conceptual knowledge.

Material dialogues have in fact been included in the dialogical framework from the start, as Krabbe (1985: 297) points out. Material dialogues indeed had priority over formal dialogues in Lorenzen and Lorenz’s work (Kamlah & Lorenzen 1967 [1972]; Lorenz 1961, 1968)[^kamlah-1967][^lorenz-1961][^lorenz-1968]. However, Krabbe further points out that the standard dialogical framework developed thereafter did not focus on the material dialogues; he interprets this fact as a sign that formal dialogues had, after all, priority over material dialogues in the dialogical framework.

**The reasons are not explicit in the standard dialogical framework.** It may be objected to the standard dialogical framework that it claims to be a “game of giving and asking for reasons”, but that these reasons are implicit. One way to answer this challenge is proposed in the Immanent Reasoning framework which provides “local” and “strategic” reasons to answer this objection.

**The standard dialogical framework is not completely dialogical.** The original project of the dialogical framework was to have language games that link meaning and use so tightly together that no extra theoretic construction would be required for these games (Lorenz 1970: 109)[^lorenz-1970]: syntax and meaning are dealt with at the level of the language games, without necessitating any metalogical approach (which would deprive the signs from their meaning). But could this project be carried out? The standard dialogical framework does not require any metalogical reasoning at the level, say, of the particle rules, but it does presuppose for example that the players use well-formed formulas (*wff*) for statements. The well formation can be checked at will, but only with the usual meta reasoning by which one checks that the expression does indeed observe the definition of a *wff*.

So can the dialogical framework be entirely based on language games, without any metalogical recourses? Or does it need at some point to call on devices outside dialogues themselves? A typology of dialogical approaches to logic can be sketched according to their degree of dependency on non-dialogical frameworks:

- complete dependency (exits the Lorenzen and Lorenz tradition): e.g., the Built-In Opponent conception of deduction, which depends on another framework, usually Natural Deduction (Dutilh Novaes & French 2018; French 2021)[^dutilh-2018][^french-2021];
- limited dependency: the standard dialogical framework, which depends on metalogical considerations for checking that the statements are syntactically well formed;
- no dependency: the Immanent Reasoning framework, in which 1. the meaning of the logical constants, 2. the syntactic formation of the statements, and 3. the content of the elementary statements, are all taken in charge through dialogues and their rules.

### 3.2 Immanent Reasoning

An outline of the Immanent Reasoning framework will here be sketched, with an emphasis on the elements answering to the three objections mentioned above (Section 3.1), and which constitute major amendments to the standard dialogical framework. The framework is extensively presented and discussed in Rahman et al. (2018).

First, the local reasons will be introduced, which answer the second objection that the reasons are not explicit in the standard framework. Then the synthesis and analysis of local reasons, and the structural rules are briefly mentioned, which replace the particle and structural rules of the standard framework. A detailed example follows, illustrating how dialogues in the Immanent Reasoning framework are carried out. The formation dialogues are then introduced (answering the third objection), and finally the material dialogues, which can deal with content at the elementary level, and with empirical propositions (answering the first objection).

#### 3.2.1 Making everything explicit using local reasons

Dialogues are games of giving and asking for reasons; yet, in the standard dialogical framework, the reasons for each statement are left implicit and do not appear in the notation of the statement. Statements of the form

$\mathbf{X} \state A$

where $A$ is an elementary proposition, are to be read as

$\mathbf{X}$ states $A$.

These statements do not give any information on the *reasons* backing this statement.

The Immanent Reasoning framework imports Martin-Löf’s 1984 Constructive Type Theory (CTT) form of a judgement in order to make these reasons explicit. Fully developed, statements thus have the following form:

$\mathbf{X} \ a : A$

where $A$ is a proposition and $a$ its *local reason*, i.e., the particular, circumstantial reason that entitles one to state $A$, which is read as

$\mathbf{X}$ states that $a$ provides evidence for $A$.

In this fashion, the reasons one has for making a statement are specified at the object-language level. The Immanent Reasoning framework distinguishes *local* reasons and *strategic* reasons. Local reasons are brought forth in particular plays, whereas strategic reasons are a recapitulation of all the possible plays: local reasons provide relevant and sufficient means for winning a play, but in general a local reason does not provide the appropriate ground for constituting a winning strategy. Strategic reasons entitle to make assertions, i.e.,  provide relevant and sufficient means for constituting a winning strategy justifying an assertion. The word “statement” is used for the posits that have not yet reached the level of a justified assertion.

When the reason is not explicit, the exclamation mark “!” marks the presence of an *implicit* reason. Thus, in the standard dialogical framework, each statement has an implicit reason backing it: $\mathbf{X} \state A$. This implicit reason may be made explicit in the Immanent Reasoning framework (but it does not have to). To make this point more palatable, take for instance the statement

$\mathbf{X} \state$ *Bachir Diagne is from Senegal.*

This statement has an implicit reason, which is the piece of evidence for stating the proposition *that Bachir Diagne is from Senegal*. This piece of evidence can be a passport, for instance. By expliciting the (empirical) local reason, the statement becomes:

$\mathbf{X}$ *passport* : *Bachir Diagne is from Senegal.*

Taking inspiration in Martin-Löf’s CTT goes with adopting an enriched language which aims at making everything explicit within the language itself. For example, quantification is always restricted to a particular specified set, so that the formula $(\forall x: A)Px\ [A: set]$ reads *For all $x$ in $A$ $Px$, where $A$ is a set*. Expressions such as $A: set$ are added to the elementary statements. Importantly, this does not mean that set-theoretic semantics is suddenly introduced in the framework: CTT is in fact based on the proposition-as-type principle or Curry-Howard correspondence (see the entry on Intuitionistic Type Theory). Other works about the relation between game-based approaches to logic and Martin-Löf’s CTT have been made with different perspectives and aims, starting with Ranta (1994). Recent works have provided important results on the use of game-based approaches to CTT for constructive mathematics, inspired by Coquand (1995); see for instance Sterling (2021).

#### 3.2.2 Local rules and an example

The particle rules determining the possible interaction of logically constant terms and modal operators in the standard framework (see Section 2) are replaced in the Immanent Reasoning framework by synthesis and analysis rules in order to take the local reasons into account. The rules for the logical constants presented here will determine interaction for *producing* local reasons appropriate to the logical constant at stake (synthesis rules), or for *extracting* local reasons embedded in more complex local reasons in a way that is characteristic of the constant at stake (analysis rules).

Synthesis and analysis of local reasons (equivalent of particle rules)

Rules that prescribe how to explicitly bring forward local reasons are called the *synthesis rules* for local reasons. They are player-independent rules. A statement with an implicit reason (“!”) is challenged, and through this interaction the implicit local reasons are made explicit. For instance, the synthesis of local reasons for an implication ($\varphi \supset \psi$) is a challenge on the implication with implicit reason, where the challenger ($\mathbf{Y}$) states the antecedent ($\varphi$) with an explicit reason of his choice ($p_1)$, and the defender ($\mathbf{X}$) states the consequent ($\psi)$ with an explicit reason of his choice ($p_2)$:

| Statement | Challenge | Defence |
| --- | --- | --- |
| $\mathbf{X}\ {\state {\varphi \supset \psi}}$ | $\mathbf{Y}\ p_1 : \varphi$ | $\mathbf{X}\ p_2 : \psi$ |

The synthesis of local reasons for universal quantification requires that the challenger provides an element of the set (an instance, which is also a local reason), the one he wishes (here $p_1$), and the defender provides a local reason ($p_2$) for the quantified proposition, in which the variable ($x$) is replaced by the challenger’s instance ($p_1$):

| Statement | Challenge | Defence |
| --- | --- | --- |
| $\mathbf{X}\state {(\forall x:A) \varphi(x)}$ | $\mathbf{Y}\ p_1 : A$ | $\mathbf{X}\ p_2 : \varphi(p_1)$ |

The complete and precise definition of the synthesis of local reasons is given by rules for the statements depending on their form (like the two examples above). The complete table of synthesis rules can be found in Rahman et al. (2018).

Once the local reasons are explicit, statements can be further challenged and defended in accordance to another set of rules called the *analysis rules* for local reasons which prescribe how to decompose the local reason associated with a statement in such a way that the component(s) render the local reasons prescribed by the synthesis rules. They require *instructions*, which are procedures that need to be carried out (the resolution of instructions), and the successive application of this process will eventually yield local reasons for elementary statements. For example, in the case of an implication, the local reason is actually a *complex* “local” reason: there is a reason for the antecedent, and a reason for the consequent. The instructions are procedures that isolate these parts of a complex reason: the left instruction (here $L^{\supset}(p)$) takes the reason for the antecedent, and the right instruction (here $R^{\supset}(p)$) takes the reason for the consequent:

| Statement | Challenge | Defence |
| --- | --- | --- |
| $\mathbf{X}\ p : \varphi \supset \psi$ | $\mathbf{Y}\ L^{\supset}(p) : \varphi$ | $\mathbf{X}\ R^{\supset}(p) : \psi$ |

The resolution of instructions is defined by a structural rule. Both players are entitled to request that the other player resolves his instructions and provides a proper local reason, as showcased in moves 6 and 9 of the example below.

The analysis and synthesis of local reasons replace the particle rules of the standard framework and enable to deal with explicit local reasons.

Structural rules for Immanent Reasoning

The structural rules in the Immanent Reasoning framework are modified to allow for the explicit mention of reasons, for the use of initial concessions, for inserting formation dialogues, for the resolution of instructions, for challenging and defending elementary statements, and for making explicit the equalities that are *used* in the standard framework’s Formal Rule (“my reasons for stating $A$ are the same as yours”). The latter two points (about elementary statements and equalities) are defined by the *Socratic Rule* which replaces the Formal Rule of the standard framework. Instead of providing all the rules for this framework in details, we will illustrate them in a commented example below. But let us give some basic information about the Socratic Rule:

- An *elementary statement is a move of the form $\mathbf{X}\state \varphi(c_i)$ or $\mathbf{X}\,a:\varphi(c_i)$, where $\varphi(c_i)$ is an atomic formula;*
- There is a synthesis rule for elementary statements: from a move $\mathbf{X}\state \varphi(c_i)$, player $\mathbf{Y}$ can request $\mathbf{X}$ to make the local reason for the atomic formula explicit;
- There are analysis rules for elementary statements: players can challenge moves of the form $a:\varphi(c_i)$. The defences involve tracking the origin of local reasons in a play in terms of equalities between local reasons or, in the case of resolution of instructions, between local reasons and instructions. For the precise formulation of these rules, see Rahman et al. (2018).

Example: play for $(\forall x:A)(B(x)\supset B(x))$, with explanations

- **Moves 0–4:** the proponent states the thesis, the players choose their repetition ranks. The opponent challenges the thesis using the *synthesis rule* for universal quantification and the proponent defends by instantiating his universal claim.

  | **O** | **P** |   |   |   |   |
  | --- | --- | --- | --- | --- | --- |
  | move | statement | challenge to move | challenge to move | statement | move |
  |   |   |   |   | $\state (\forall x:A)(B(x)\supset B(x))$ | 0 |
  | 1 | $\mathtt{n} :=\rank{1}$ |   |   | $\mathtt{m}:=\rank{2}$ | 2 |
  | 3 | $p_1 : A$ | (0) |   | $p_2 : B(p_1) \supset B(p_1)$ | 4 |
- **Move 5:** the opponent challenges the implication with local reason (analysis rule). A local reason for an implication is complex: it has a left part for the antecedent, and a right part for the consequent. She thus uses an instruction to take only the left part of $p_2$ as the reason for the antecedent.

  | **O** | **P** |   |   |   |   |
  | --- | --- | --- | --- | --- | --- |
  | move | statement | challenge to move | challenge to move | statement | move |
  |   |   |   |   | $\state (\forall x:A)(B(x)\supset B(x))$ | 0 |
  | 1 | $\mathtt{n} :=\rank{1}$ |   |   | $\mathtt{m}:=\rank{2}$ | 2 |
  | 3 | $p_1 : A$ | (0) |   | $p_2 : B(p_1) \supset B(p_1)$ | 4 |
  | 5 | $L^{\supset}(p_2) : B(p_1)$ | (4) |   |   |   |
- **Moves 6–7:** before answering the opponent’s challenge, the proponent requests that she resolves the instruction in move 5, i.e., that she gives a proper local reason instead of an instruction (structural rule, resolution of instructions). The opponent resolves the instruction of move 5 and provides a proper local reason for her statement. Note that “$\rqst \dots/L^{\supset}(p_2)$” can be read as requesting what local reasons stand for $L^{\supset}(p_2)$, thus asking the adversary to fill in the dots.

  | **O** | **P** |   |   |   |   |
  | --- | --- | --- | --- | --- | --- |
  | move | statement | challenge to move | challenge to move | statement | move |
  |   |   |   |   | $\state (\forall x:A)(B(x)\supset B(x))$ | 0 |
  | 1 | $\mathtt{n} :=\rank{1}$ |   |   | $\mathtt{m}:=\rank{2}$ | 2 |
  | 3 | $p_1 : A$ | (0) |   | $p_2 : B(p_1) \supset B(p_1)$ | 4 |
  | 5 | $L^{\supset}(p_2) : B(p_1)$ | (4) |   |   |   |
  | 7 | $p_{2.1} : B(p_1)$ |   | (5) | $\rqst \dots /L^{\supset}(p_2)$ | 6 |
- **Moves 8–9:** the proponent answers the pending challenge on the implication by using an instruction that selects the right part of the local reason for the implication, thus backing the consequent. The opponent requests the resolution of that instruction.

  | **O** | **P** |   |   |   |   |
  | --- | --- | --- | --- | --- | --- |
  | move | statement | challenge to move | challenge to move | statement | move |
  |   |   |   |   | $\state (\forall x:A)(B(x)\supset B(x))$ | 0 |
  | 1 | $\mathtt{n} :=\rank{1}$ |   |   | $\mathtt{m}:=\rank{2}$ | 2 |
  | 3 | $p_1 : A$ | (0) |   | $p_2 : B(p_1) \supset B(p_1)$ | 4 |
  | 5 | $L^{\supset}(p_2) : B(p_1)$ | (4) |   | $R^{\supset}(p_2) : B(p_1)$ | 8 |
  | 7 | $p_{2.1} : B(p_1)$ |   | (5) | $\rqst \dots /L^{\supset}(p_2)$ | 6 |
  | 9 | $\rqst \dots / R^{\supset}(p_2)$ | (8) |   |   |   |
- **Moves 10–11:** the proponent resolves the instruction by providing a proper local reason, $p_{2.1}$. He is entitled to this elementary statement since the opponent has already stated it (move 7). The opponent however requests that the link with her own statements be made explicit, she asks that the local reason be justified by an equality with her own local reasons (structural Socratic Rule).

  | **O** | **P** |   |   |   |   |
  | --- | --- | --- | --- | --- | --- |
  | move | statement | challenge to move | challenge to move | statement | move |
  |   |   |   |   | $\state (\forall x:A)(B(x)\supset B(x))$ | 0 |
  | 1 | $\mathtt{n} :=\rank{1}$ |   |   | $\mathtt{m}:=\rank{2}$ | 2 |
  | 3 | $p_1 : A$ | (0) |   | $p_2 : B(p_1) \supset B(p_1)$ | 4 |
  | 5 | $L^{\supset}(p_2) : B(p_1)$ | (4) |   | $R^{\supset}(p_2) : B(p_1)$ | 8 |
  | 7 | $p_{2.1} : B(p_1)$ |   | (5) | $\rqst \dots /L^{\supset}(p_2)$ | 6 |
  | 9 | $\rqst \dots / R^{\supset}(p_2)$ | (8) |   | $p_{2.1} : B(p_1)$ | 10 |
  | 11 | $\rqst = p_{2.1}$ | (10) |   |   |   |
- **Move 12:** the proponent uses the Socratic Rule in order to explicit where his local reason comes from: it is exactly the same reason that the opponent used in order to resolve the instruction $L^{\supset}(p_2)$. In other words, in this case, the reason for stating the consequent (i.e., the resolution of $R^{\supset}(p_2)$) is exactly the same as the reason for stating the antecedent of the implication.

  | **O** | **P** |   |   |   |   |
  | --- | --- | --- | --- | --- | --- |
  | move | statement | challenge to move | challenge to move | statement | move |
  |   |   |   |   | $\state (\forall x:A)(B(x)\supset B(x))$ | 0 |
  | 1 | $\mathtt{n} :=\rank{1}$ |   |   | $\mathtt{m}:=\rank{2}$ | 2 |
  | 3 | $p_1 : A$ | (0) |   | $p_2 : B(p_1) \supset B(p_1)$ | 4 |
  | 5 | $L^{\supset}(p_2) : B(p_1)$ | (4) |   | $R^{\supset}(p_2) : B(p_1)$ | 8 |
  | 7 | $p_{2.1} : B(p_1)$ |   | (5) | $\rqst \dots /L^{\supset}(p_2)$ | 6 |
  | 9 | $\rqst \dots / R^{\supset}(p_2)$ | (8) |   | $p_{2.1} : B(p_1)$ | 10 |
  | 11 | $\rqst = p_{2.1}$ | (10) |   | $L^{\supset}(p_2) = p_{2.1} : B(p_1)$ | 12 |
  | **P** wins the play. |   |   |   |   |   |

#### 3.2.3 Formation dialogues

The enriched framework of Immanent Reasoning allows the players to first enquire on the formation of the components of a statement within a play, before carrying out the play asking for the reasons backing a statement and giving them. Accordingly, additional dialogical rules explain the formation of statements involving logical constants. The formation of elementary propositions is governed by the Socratic Rule (like the *use* of elementary statements was governed by the Formal Rule in the standard framework).

In this way, the opponent may (but does not have to) examine the well formation of the thesis with the challenge “$\rqst_{\bprop}$” before starting to ask for reasons. The formation rules for *logical constants* and for *falsum* are given in the following table. Notice that a statement “$\bot: \bprop$” (which reads *$\bot$ is a proposition*) cannot be challenged; this is the dialogical account for falsum “$\bot$” being by definition a proposition.

|   | Statement | Challenge | Defence |
| --- | --- | --- | --- |
| Conjunction | $\mathbf{X}\,A\land{}B: \bprop$ | $\mathbf{Y}\rqst F_{\land{}1}$ or $\mathbf{Y}\rqst F_{\land{}2}$ | $\mathbf{X}\,A: \bprop$ (resp.) $\mathbf{X}\,B: \bprop$ |
| Disjunction | $\mathbf{X}\,A\lor{}B: \bprop$ | $\mathbf{Y}\rqst F_{\lor{}1}$ or $\mathbf{Y}\rqst F_{\lor{}2}$ | $\mathbf{X}\,A: \bprop$ (resp.) $\mathbf{X}\,B: \bprop$ |
| Implication | $\mathbf{X}\,A\supset{}B: \bprop$ | $\mathbf{Y}\rqst F_{\supset{}1}$ or $\mathbf{Y}\rqst F_{\supset{}2}$ | $\mathbf{X}\,A: \bprop$ (resp.) $\mathbf{X}\,B: \bprop$ |
| Universal quantification | $\mathbf{X}\,(\forall{}x: A)B(x): \bprop$ | $\mathbf{Y}\rqst F_{\forall{}1}$ or $\mathbf{Y}\rqst F_{\forall{}2}$ | $\mathbf{X}\,A: \bset$ (resp.) $\mathbf{X}\,B(x): \bprop{}[x: A]$ |
| Existential quantification | $\mathbf{X}\,(\exists{}x: A)B(x): \bprop$ | $\mathbf{Y}\rqst F_{\exists{}1}$ or $\mathbf{Y}\rqst F_{\exists{}2}$ | $\mathbf{X}\,A: \bset$ (resp.) $\mathbf{X}\,B(x): \bprop{}[x: A]$ |
| Falsum | $\mathbf{X}\,\bot: \bprop$ | $--$ | $--$ |

Example of a formation dialogue

The thesis is $(\forall x:A)(B(x)\supset B(x))$. Before applying the synthesis rule for universal quantification and initializing a play about reasons, the opponent opens a formation dialogue by requesting (move 3) that the proponent states that his thesis is a proposition (move 4).

| **O** | **P** |   |   |   |   |
| --- | --- | --- | --- | --- | --- |
| move | statement | challenge to move | challenge to move | statement | move |
|   |   |   |   | $\state (\forall x:A)(B(x)\supset B(x))$ | 0 |
| 1 | $\mathtt{n} :=\rank{1}$ |   |   | $\mathtt{m}:=\rank{2}$ | 2 |
| 3 | $\rqst_{\bprop}$ | (0) |   | $(\forall x:A)(B(x)\supset B(x)):\bprop$ | 4 |

- **Move 5:** the opponent can challenge this statement by applying the formation rule for universal quantification given in the table above, and chooses one of the possible challenges: she asks for the first part of the expression with “$\rqst_{\forall{}1}$”.

  | **O** | **P** |   |   |   |   |
  | --- | --- | --- | --- | --- | --- |
  | move | statement | challenge to move | challenge to move | statement | move |
  |   |   |   |   | $\state (\forall x:A)(B(x)\supset B(x))$ | 0 |
  | 1 | $\mathtt{n} :=\rank{1}$ |   |   | $\mathtt{m}:=\rank{2}$ | 2 |
  | 3 | $\rqst_{\bprop}$ | (0) |   | $(\forall x:A)(B(x)\supset B(x)):\bprop$ | 4 |
  | 5 | $\rqst_{\forall{}1}$ | (4) |   |   |   |

The proponent wants to answer that $A$ is a set, which would trigger material considerations (is $A$ a set or not?). See below for material dialogues (Section 3.2.4). In order to avoid (for whatever reason) these material considerations, *initial concessions* may be added to the thesis in square brackets, for instance $A: \bset$. When accepting to play, the opponent also accepts these concessions for the sake of the argument.

Example of a formation dialogue with initial concessions

The thesis is the same as the previous one, with the added initial concessions $A: \bset$ and $B(x) : \bprop \, [x : A]$.

$$(\forall x:A)(B(x)\supset B(x))\quad \big[ A: \bset \,;\, B(x) : \bprop{} \,[x : A]\big]$$

The proponent states the thesis (move 0), the opponent starts playing: she accepts the concessions (0.1 and 0.2) and chooses her repetition rank (move 1). The play is then the same as above up to move 5.

| **O** | **P** |   |   |   |   |
| --- | --- | --- | --- | --- | --- |
| move | statement | challenge to move | challenge to move | statement | move |
| 0.1 | $A: \bset$ |   |   | $\state (\forall x:A)(B(x)\supset B(x))$ | 0 |
| 0.2 | $B(x) : \bprop{} [x : A]$ |   |   | $[A: \bset ; B(x) : \bprop{} [x : A]]$ |   |
| 1 | $\mathtt{n} :=\rank{1}$ |   |   | $\mathtt{m}:=\rank{2}$ | 2 |
| 3 | $\rqst_{\bprop}$ | (0) |   | $(\forall x:A)(B(x)\supset B(x)):\bprop$ | 4 |
| 5 | $\rqst_{\forall{}1}$ | (4) |   |   |   |

- **Moves 6–7:** the proponent is entitled to the elementary statement $A: \bset$, since the opponent has already stated it (concession 0.1). Since the opponent’s repetition rank is $\rank{1}$, she cannot attack anymore, the formation dialogue is over and she challenges the universal quantifier of the thesis. The rest of the play is, except for the move labels, the same as above.

  | **O** | **P** |   |   |   |   |
  | --- | --- | --- | --- | --- | --- |
  | move | statement | challenge to move | challenge to move | statement | move |
  | 0.1 | $A: \bset$ |   |   | $(\forall x:A)(B(x)\supset B(x))$ | 0 |
  | 0.2 | $B(x) : \bprop{} [x : A]$ |   |   | $[A: \bset ; B(x) : \bprop [x : A]]$ |   |
  | 1 | $\mathtt{n} :=\rank{1}$ |   |   | $\mathtt{m}:=\rank{2}$ | 2 |
  | 3 | $\rqst_{\bprop}$ | (0) |   | $(\forall x:A)(B(x)\supset B(x)):\bprop$ | 4 |
  | 5 | $\rqst_{\forall{}1}$ | (4) |   | $A: \bset$ | 6 |
  | 7 | $p_1 : A$ | (0) |   |   |   |
  *Note: if the opponent wants to challenge both sides of the formation of the universal quantification in the same play, she must choose repetition rank 2.*

#### 3.2.4 Material dialogues

As pointed out by Krabbe (1985: 297) and mentioned above, *material dialogues*—that is, dialogues in which propositions have content—receive, in the writings of Paul Lorenzen and Kuno Lorenz, priority over formal dialogues: material dialogues constitute the *locus* where the logical constants are introduced. However, in the standard dialogical framework, both material and formal dialogues have a purely syntactic notion of the Formal Rule, through which logical validity is defined (because of how it accounts for analyticity and formality, as explained in the previous sections). The original intention of having content is thus bypassed in the standard framework, with the consequence that Krabbe and others after him considered that *formal* dialogues have, all in all, priority over material ones. In the context of the Immanent Reasoning framework, this is explained as stemming from shortcomings of the standard approach, and it is argued that this can be overcome when local reasons are expressed. The claim is then that by doing so it is possible to fulfill this original intention of the dialogical framework.

The point of material dialogues is that each elementary sentence involving a set such as $a: A$—where $A:set$—requires a special adaptation of the Socratic Rule (i.e., the rule about elementary sentences which replaces the standard Formal Rule). This special Socratic Rule prescribes, for each elementary statement, what a player is committing to when making that statement. Note that these rules are *not* player independent, they belong to the structural rules. This amounts to the following general points.

1. Material dialogues must include synthesis rules for elementary statements.
2. When **O** states an elementary statement, she can be asked to produce the local reason specific to that elementary statement, according to the suitable synthesis rule or equality rule. The specific rules depend on the elementary statements at stake: for example, the rules for statements about some object being a natural number will be different from the ones for statements about some individual being French, and so on. Rahman et al. (2018) introduce some examples, including the rules for elementary statements involving the identity predicate.
3. Only when the previous step has been accomplished can **P** take over in order to fulfill his duty of defending the same elementary statement.

Example: natural numbers

Take for instance the statements about natural numbers, e.g.,

- $\mathbf{X}~ 0 : \mathbb{N}$ ($\mathbf{X}$ states that 0 is a natural number)
- $\mathbf{X}~ s(0) : \mathbb{N}$ ($\mathbf{X}$ states that the successor of 0 is a natural number)
- $\mathbf{X}~ n : \mathbb{N}$ ($\mathbf{X}$ states that $n$ is a natural number)

These are all elementary statements. The rules for elementary statements concerning natural numbers are the following: if a player $\mathbf{X}$ states that $n$ is a natural number, $\mathbf{Y}$ may request that $\mathbf{X}$ states that $s(n)$ is a natural number.

| *Statement* | *Challenge* | *Defence* |
| --- | --- | --- |
| $\mathbf{X}~ n:\mathbb{N} $ | $\mathbf{Y}\rqst s(n)$ | $\mathbf{X}~ s(n):\mathbb{N}$ |

The special Socratic Rule for natural numbers establishes a set of nominal definitions (*defiendum* $\equiv_{df}$ *definiens*):

$$\begin{align} 1 & \equiv_{df} s(0)\\ 2 & \equiv_{df} s(s(0))\\ & \vdots\\ n & \equiv_{df} s(s(\ldots s(0)\ldots )). \end{align}$$

What is more, **O** may challenge a statement **P** $n:\mathbb{N}$ by requesting (**O** $\rqst n$) that **P** provides one of the accepted nominal definitions above (**P** $s(s(\ldots s(0)\ldots )) \equiv_{df} n : \mathbb{N}$). However, **P** may provide such a nominal definition only if **O** has previously stated the *definiens* (here $s(s(\ldots s(0)\ldots ))$).

Example of material play for the thesis $2:\mathbb{N} ~ [0:\mathbb{N}]$.

| **O** | **P** |   |   |   |   |
| --- | --- | --- | --- | --- | --- |
| move | statement | challenge to move | challenge to move | statement | move |
| 0.1 | $0:\mathbb{N}$ |   |   | $2:\mathbb{N} ~ [0:\mathbb{N}]$ | 0 |
| 1 | $\mathtt{n} :=\rank{1}$ |   |   | $\mathtt{m}:=\rank{2}$ | 2 |
| 3 | $\rqst 2$ | (0) |   | $2 \equiv_{df} s(s(0)) : \mathbb{N}$ | 8 |
| 5 | $s(0) : \mathbb{N}$ |   | (0.1) | $\rqst s(0)$ | 4 |
| 7 | $s(s(0)): \mathbb{N}$ |   | (5) | $\rqst s(s(0))$ | 6 |
| **P** wins the play. |   |   |   |   |   |

Explanations

- **Move 0:** **P** states the thesis: 2 is a natural number, provided that 0 is a natural number.
- **Moves 0.1–3:** **O** states the initial concession, that 0 is a natural number; the players choose their repetition ranks and **O** challenges **P**’s thesis by requesting that he justifies his claim that 2 is a natural number.
- **Moves 4–5:** before answering **O**’s challenge, **P** challenges **O**’s concession (move 0.1), and requests that **O** states that the successor of 0 is a natural number. **O** complies.
- **Moves 6–7:** **P** proceeds in the same way for the successor of 0, **O** complies. Thus, **O** has stated the required *definiens* for **P**’s thesis.
- **Move 8:** **P** is able to answer **O**’s pending challenge (move 3) by stating the nominal definition that 2 is the successor of the successor of 0, thus justifying his thesis that 2 is a natural number. **O** has no available move left, so she loses.

### 3.3 The Built-In Opponent

As mentioned in Section 1, the present entry focuses on the Lorenzen and Lorenz tradition of dialogical logic (tradition 1). It may however be of use to outline the general ideas of the Built-In Opponent (BIO) conception of deduction, even though Catarina Dutilh Novaes stresses in her work that this approach is distinct from the Lorenzen and Lorenz dialogical tradition (e.g., Dutilh Novaes 2015: 600; 2020: 37; Dutilh Novaes & French 2018: 135)[^dutilh-2015][^dutilh-2018].

The BIO conception of deduction is a rational reconstruction of deductive reasoning inspired by certain historical considerations (see for example Dutilh Novaes, 2016)[^dutilh-2016]. In this regard, it claims neither historical nor factual accuracy, but it is a *rational reconstruction* of deductive reasoning, historically *inspired*. The purpose of this framework is to provide a dialogical interface—in the sense of a junction point—between actual reasoning (deduction understood as a social practice, not as a logical norm) and formal logic. The BIO interface deals mostly with people’s actual reasoning patterns (Dutilh Novaes 2013)[^dutilh-2013] and informal logic (Dutilh Novaes & French 2018: 131)[^dutilh-2018], bringing the general features of logic and argumentation to the fore. Thus,

> the main claim is that, rather than comprising the canons for correct *thinking*, the traditional principles of deduction reflect rules for engaging in certain kinds of *dialogical practices*. (Dutilh Novaes 2015: 599)[^dutilh-2015]

This interface thus allows to approach empirical studies concerning the way people actually reason with a dialogical model in mind, and thus explain the greater or lesser magnitude (across cultures and within a culture) with which people’s reasoning patterns diverge from the norms of classical logic, by the greater or lesser familiarity these people have with certain types of dialogues they engage in. Thus, for instance, familiarity with testing situations common in school would greatly help people understand what is expected of them during the questioning process the empirical studies use for obtaining their data (Dutilh Novaes 2013)[^dutilh-2013].

But this BIO interface also allows to approach *logical* considerations from a dialogical perspective, either by considering deduction as a very specialized social practice, or by putting Gentzen’s Natural Deduction or Sequent Calculus into a dialogical setting (French 2015; Dutilh Novaes & French 2018; French 2021)[^dutilh-2018][^french-2015][^french-2021]. Deduction in itself is considered as an essentially dialogical matter (Dutilh Novaes 2013; 2015; 2016; 2020)[^dutilh-2013], where the role of the interlocutor (the Opponent or Skeptic) has been “internalized” over time, in the sense that the deductive method has integrated its role, which is not apparent anymore (Dutilh Novaes 2015: 600)[^dutilh-2015]. In this regard, when a mathematician or a logician spells out a proof, they adopt both roles, the proponent’s and the opponent’s. This is the idea behind the “Built-In Opponent” expression which was inspired by Göran Sundholm’s lectures and talks on assertion, by the year 2000, when suggesting the idea that elimination rules can be read as the moves of an opponent aimed at testing the thesis. Another work dealing with the connexion between Natural Deduction and the dialogical approach in the sense of tradition 1 is Rahman et al. (2009) which was also directly influenced by Sundholm’s suggestion, and where the branches in the inference rules are said to *incarnate* the choices of the players as they appear in the extensive form of a strategy. The BIO conception shares this inspiration but developed in its own, proper dialogical conception and its proper objectives.

The BIO interface mostly takes the form of Prover-Skeptic games inspired from Sørensen and Urzyczyn (2006), which developed a dialogical framework motivated by questions in the study of computation. In the BIO, the Prover (or proponent) is the player who proves that the conclusion of the deduction follows from the premises, and the Skeptic (or opponent) is the player who doubts each step of the proof and who will raise objections if he can. The game starts with Prover asking Skeptic to grant the premises, which Skeptic accepts for the sake of the argument. Then Prover states what necessarily follows from these premises, and Skeptic’s role is to make sure that each new statement made by Prover clearly follows from the previous statements. Prover can thus provide counter-examples to a statement or ask clarifications (“why does this follow?”). Skeptic’s role is thus to check that the proof is compelling. The play is asymmetric, since Prover defends and Skeptic attacks.

From this informal structure, the BIO interface can import traditional Natural Deduction, with the introduction and elimination rules, or even a “‘structurally explicit’ sequent to sequent style” version (French 2021: section 3.1)[^french-2021] in the fashion of Dummett (1977). Prover then brings forth sequents for Skeptic to accept, and Prover is entitled to state sequents that follow in virtue of the introduction and elimination rules or in virtue of “structural” rules.

As mentioned above, “structural rules” may refer to two things: either to the standard dialogical structural rules presented in Section 2, or, as it is here the case, to rules imported from another framework (which would be called “strategic” rules in the standard framework). In the BIO approach, Prover can thus produce sequents that follow from others in virtue of rules such as contraction or weakening. The aim of this kind of dialogical approach is to understand the “structural” properties of deduction.

When concerned with formal logic, the BIO interface thus has purely strategic considerations, and is not much concerned by the play level. In this respect, the disappearance of the opponent in deductive proofs is justified through the strategic focus: Prover does not actually need Skeptic if Prover is careful enough in carrying out the deductive method (making gap-free proofs).

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=logic-dialogical). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/logic-dialogical/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=logic-dialogical&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/logic-dialogical/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- [Dialogical Logic](https://iep.utm.edu/dial-log/), Internet Encyclopedia of Philosophy entry by Thomas Piecha
- Keiff, Laurent, “Dialogical Logic”, *Stanford Encyclopedia of Philosophy* (Winter 2021 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/win2021/entries/logic-dialogical/](https://plato.stanford.edu/archives/win2021/entries/logic-dialogical/)>. [This was the previous entry on this topic in the *Stanford Encyclopedia of Philosophy* – see the [version history](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=logic-dialogical).]

## Related Entries

argument and argumentation | logic: and games | logic: epistemic | logic: free | logic: independence friendly | logic: linear | logic: modal | logic: paraconsistent | logic: substructural | logical pluralism

[^alama-2011]: Alama, Jesse, Aleks Knocks, and Sara L. Uckelman, 2011, “Dialogue Games for Classical Logic”, in Martin Giese and Roman Kuznets (eds.), *Tableaux 2011: Workshops, Tutorials and Short Papers*, Technical Report IAM-11-002, University of Bern, pp. 82–86.

[^austin-1946]: Austin, J. L., 1946, “Other Minds”, part of “Symposium: Other Minds”, J. Wisdom, J. L. Austen, and A. J. Ayer, *Aristotelian Society Supplementary Volume*, 20: 148–187. doi:10.1093/aristoteliansupp/20.1.122

[^barth-1982]: Barth, E. M. and E. C. W. Krabbe, 1982, *From Axiom to Dialogue: A Philosophical Study of Logics and Argumentation*, Berlin and New York: Walter de Gruyter.

[^beth-1955]: Beth, Evert Willem, 1955, *Semantic Entailment and Formal Derivability*, (Mededelingen Der Koninklijke Nederlandse Akademie van Wetenschappen. Afd. Letterkunde. Nieuwe Reeks, deel 18, no. 13), Amsterdam: Noord-Hollandsche Uitg. Mij.

[^blackburn-2001]: Blackburn, Patrick, 2001, “Modal Logic as Dialogical Logic”, in Rahman and Rückert 2001, pp. 57–93. doi:10.1023/A:1010358017657

[^blass-1992]: Blass, Andreas, 1992, “A Game Semantics for Linear Logic”, *Annals of Pure and Applied Logic*, 56(1–3): 183–220. doi:10.1016/0168-0072(92)90073-9

[^bour-2010]: Bour, Pierre Edouard, Manuel Rebuschi, and Laurent Rollet (eds.), 2010, *Construction: Festschrift for Gerhard Heinzmann*, (Tributes 14), London: College Publications.

[^brandom-1994]: Brandom, Robert, 1994, *Making it Explicit: Reasoning, Representing, and Discursive Commitment*, Cambridge, MA: Harvard University Press.

[^brandom-1997]: –––, 1997, “A Study Guide”, in Sellars 1997, pp. 119–189.

[^brandom-2000]: –––, 2000, *Articulating Reasons*, Cambridge, MA: Harvard University Press.

[^clerbout-2014a]: Clerbout, Nicolas, 2014a, “First-Order Dialogical Games and Tableaux”, *Journal of Philosophical Logic*, 43(4): 785–801. doi:10.1007/s10992-013-9289-z

[^clerbout-2014b]: –––, 2014b, “Finiteness of plays and the dialogical problem of decidability”, *IfCoLog Journal of Logics and their Applications* 1(1): 115–130.

[^clerbout-2011]: Clerbout, Nicolas, Marie-Hélène Gorisse, and Shahid Rahman, 2011, “Context-Sensitivity in Jain Philosophy: A Dialogical Study of Siddharṣigaṇi’s *Commentary on the Handbook of Logic*”, *Journal of Philosophical Logic*, 40(5): 633–662. doi:10.1007/s10992-010-9164-0

[^coquand-1995]: Coquand, Thierry, 1995, “A Semantics of Evidence for Classical Arithmetic”, *Journal of Symbolic Logic*, 60(1): 325–337. doi:10.2307/2275524

[^crubellier-2019]: Crubellier, Michel, Mathieu Marion, Zoe McConaughey, and Shahid Rahman, 2019, “Dialectic, the Dictum de Omni and Ecthesis”, *History and Philosophy of Logic*, 40(3): 207–233. doi:10.1080/01445340.2019.1586623

[^dummett-1977]: Dummett, Michael A. E., 1977, *Elements of Intuitionism*, Oxford: Clarendon Press. Second edition, 2000.

[^dutilh-2007]: Dutilh Novaes, Catarina, 2007, *Formalizing Medieval Logical Theories: Suppositio, Consequentiae and Obligationes*, Dordrecht: Springer Netherlands. doi:10.1007/978-1-4020-5853-0

[^dutilh-2013]: –––, 2013, “A Dialogical Account of Deductive Reasoning as a Case Study for How Culture Shapes Cognition”, *Journal of Cognition and Culture*, 13(5): 459–482. doi:10.1163/15685373-12342104

[^dutilh-2015]: –––, 2015, “A Dialogical, Multi-Agent Account of the Normativity of Logic”, *Dialectica*, 69(4): 587–609. doi:10.1111/1746-8361.12118

[^dutilh-2016]: –––, 2016, “Reductio Ad Absurdum from a Dialogical Perspective”, *Philosophical Studies*, 173(10): 2605–2628. doi:10.1007/s11098-016-0667-6

[^dutilh-2020]: –––, 2020, *The Dialogical Roots of Deduction: Historical, Cognitive, and Philosophical Perspectives on Reasoning*, Cambridge: Cambridge University Press. doi:10.1017/9781108800792

[^dutilh-2018]: Dutilh Novaes, Catarina and Rohan French, 2018, “Paradoxes and Structural Rules from a Dialogical Perspective”, *Philosophical Issues*, 28(1): 129–158. doi:10.1111/phis.12119

[^felscher-1985]: Felscher, Walter, 1985, “Dialogues, Strategies, and Intuitionistic Provability”, *Annals of Pure and Applied Logic*, 28(3): 217–254. doi:10.1016/0168-0072(85)90016-8

[^fermüller-2003]: Fermüller, Christian G., 2003, “Parallel Dialogue Games and Hypersequents for Intermediate Logics”, in *Automated Reasoning with Analytic Tableaux and Related Methods*, Marta Cialdea Mayer and Fiora Pirri (eds.), (Lecture Notes in Computer Science 2796), Berlin, Heidelberg: Springer, pp. 48–64. doi:10.1007/978-3-540-45206-5_7

[^fermüller-2008]: –––, 2008, “Dialogue Games for Many-Valued Logics — an Overview”, *Studia Logica*, 90(1): 43–68. doi:10.1007/s11225-008-9143-4

[^fermüller-2021]: –––, 2021, “Connecting Sequent Calculi with Lorenzen-Style Dialogue Games”, in Heinzmann and Wolters 2021, pp. 115–141. doi:10.1007/978-3-030-65824-3_8

[^fermüller-2014]: Fermüller, Christian G. and Christoph Roschger, 2014, “From Games to Truth Functions: A Generalization of Giles’s Game”, *Studia Logica*, 102(2): 389–410. doi:10.1007/s11225-014-9550-7

[^fiutek-2010]: Fiutek, Virginia, Helge Rückert, and Shahid Rahman, 2010, “A Dialogical Semantics for Bonanno’s System of Belief Revision”, in Bour, Rebuschi, and Rollet 2010, pp. 315–334.

[^fontaine-2013]: Fontaine, Matthieu, 2013, *Argumentation et engagement ontologique. Être, c’est être choisi*, London: College Publications.

[^french-2015]: French, Rohan, 2015, “Prover-Skeptic Games and Logical Pluralism”, in *Proceedings of the 20th Amsterdam Colloquium*, Thomas Brochhagen, Floris Roelofsen, and Nadine Theiler (eds.), University of Amsterdam, 128–136.

[^french-2021]: –––, 2021, “A Dialogical Route to Logical Pluralism”, *Synthese*, 198(S20): 4969–4989. doi:10.1007/s11229-019-02404-5

[^gethmann-1979]: Gethmann, Carl Friedrich, 1979, *Protologik. Untersuchungen zur formalen Pragmatik von Begründungsdiskursen*, Frankfurt a.M.: Suhrkamp.

[^girard-2001]: Girard, Jean-Yves, 2001, “Locus Solum: From the Rules of Logic to the Logic of Rules”, *Mathematical Structures in Computer Science*, 11(3): 301–506. doi:10.1017/S096012950100336X

[^heinzmann-2021]: Heinzmann, Gerhard and Gereon Wolters (eds.), 2021, *Paul Lorenzen—Mathematician and Logician*, (Logic, Epistemology, and the Unity of Science 51), Cham: Springer International Publishing. doi:10.1007/978-3-030-65824-3

[^hintikka-1968]: Hintikka, Jaakko, 1968, “Language-Games for Quantifiers”, in *Studies in Logical Theory: Essays*, James W. Comman (ed.), (American philosophical quarterly. Monograph series 2), Oxford: Basil Blackwell, pp. 46–72.

[^hintikka-1973]: –––, 1973, *Logic, Language-Games and Information: Kantian Themes in the Philosophy of Logic*, Oxford: Clarendon Press.

[^hodges-2001]: Hodges, Wilfrid, 2001, “Dialogue Foundations: A Sceptical Look”, *Proceedings of the Aristotelian Society (Supplement)* 75: 17–32. doi:10.1111/1467-8349.00076

[^hodges-2001-2]: Hodges Wilfrid and Jouko Väänänen, 2001 [2019], “Logic and Games”, *Stanford Encyclopedia of Philosophy* (Fall 2019 edition), Edward N. Zalta (ed.), (Väänänen added as author for the Fall 2019 version), URL = <[https://plato.stanford.edu/archives/fall2019/entries/logic-games/](https://plato.stanford.edu/archives/fall2019/entries/logic-games/)>.

[^johnson-1999]: Johnson, Ralph H., 1999, “The Relation between Formal and Informal Logic”, *Argumentation*, 13(3): 265–274. doi:10.1023/A:1007789101256

[^kamlah-1967]: Kamlah, Wilhelm and Paul Lorenzen, 1967 [1973], *Logische Propädeutik: Vorschule des vernünftigen Redens*, Mannheim: Bibliographisches Institut. Second edition 1973. Translated as *Logical Propaedeutic: Pre-School of Reasonable Discourse*, Hoke Robinson (trans.), Lanham, MD: University Press of America, 1984.

[^keiff-2004]: Keiff, Laurent, 2004, “Heuristique formelle et logiques modales non normales”, *Philosophia Scientiae*, 8(2): 39–59.

[^keiff-2007]: –––, 2007, *Le Pluralisme dialogique : Approches dynamiques de l’argumentation formelle*, PhD thesis, University of Lille.

[^krabbe-1985]: Krabbe, Erik C. W., 1985, “Formal Systems of Dialogue Rules”, *Synthese*, 63(3): 295–328. doi:10.1007/BF00485598

[^lorenz-1961]: Lorenz, Kuno, 1961, *Arithmetik und Logik als Spiele*, PhD thesis, Universität zu Kiel. Partially reprinted in Lorenzen and Lorenz 1978, pp. 17–95.

[^lorenz-1968]: –––, 1968, “Dialogspiele als Semantische Grundlage von Logikkalkülen”, *Archiv für Mathematische Logik und Grundlagenforschung*, 11(1–2): 32–55 and 11(3–4): 73–100. doi:10.1007/BF01973341 doi:10.1007/BF01967817

[^lorenz-1970]: –––, 1970, *Elemente der Sprachkritik. Eine Alternative zum Dogmatismus und Skeptizismus in der Analytischen Philosophie*, Frankfurt: Suhrkamp.

[^lorenz-1981]: –––, 1981, “Dialogic Logic”, in *Dictionary of Logic as Applied in the Study of Language*, Witold Marciszewski (ed.), The Hague: Martinus Nijhoff, pp. 117–125. doi:10.1007/978-94-017-1253-8_24

[^lorenz-2001]: –––, 2001, “Basic Objectives of Dialogue Logic in Historical Perspective”, in Rahman and Rückert 2001, pp. 255–263. doi:10.1023/A:1010367416884

[^lorenz-2009]: –––, 2009, *Dialogischer Konstruktivismus*, Berlin: Walter de Gruyter. doi:10.1515/9783110210392

[^lorenz-2010]: –––, 2010, *Logic, Language and Method: On Polarities in Human Experience*, New York/Berlin: Walter de Gruyter. doi:10.1515/9783110216790

[^lorenz-2011]: –––, 2011, *Philosophische Variationen: Gesammelte Aufsätze Unter Einschluss Gemeinsam Mit Jürgen Mittelstraß Geschriebener Arbeiten Zu Platon Und Leibniz*, Berlin/New York: De Gruyter. doi:10.1515/9783110218800

[^lorenzen-1955]: Lorenzen, Paul, 1955, *Einführung in die operative Logik und Mathematik*, Berlin: Springer.

[^lorenzen-1960]: –––, 1960, “Logik und Agon”, in *Atti del XII Congresso Internazionale di Filosofia*, vol. 4, Florence: Sansoni Editore, pp. 187–194.

[^lorenzen-1978]: Lorenzen, Paul and Kuno Lorenz, 1978, *Dialogische Logik*, Darmstadt: Wissenschaftliche Buchgesellschaft.

[^magnier-2013]: Magnier, Sébastien, 2013, *Approche dialogique de la dynamique épistémique et de la condition juridique*, London: College Publications.

[^marion-2006]: Marion, Mathieu, 2006, “Hintikka on Wittgenstein: from Language Games to Game Semantics”, in Tuomo Aho and Ahti-Veikko Pietarinen (eds.), *Truth and Games: Essays in Honour of Gabriel Sandu*, (Acta Philosophica Fennica LXXVIII), Helsinki: Societas Philosophica Fennica, pp. 237–256.

[^marion-2009]: –––, 2009, “Why Play Logical Games?”, in *Games: Unifying Logic, Language, and Philosophy*, Ondrej Majer, Ahti-Veikko Pietarinen, and Tero Tulenheimo (eds.), (Logic, Epistemology, and the Unity of Science 15), Dordrecht: Springer Netherlands, pp. 3–26. doi:10.1007/978-1-4020-9374-6_1

[^marion-2010]: –––, 2010, “Between Saying and Doing: From Lorenzen to Brandom and Back”, in Bour, Rebuschi, and Rollet 2010, pp. 489–497.

[^marion-2016]: Marion, Mathieu and Helge Rückert, 2016, “Aristotle on Universal Quantification: A Study from the Point of View of Game Semantics”, *History and Philosophy of Logic*, 37(3): 201–229. doi:10.1080/01445340.2015.1089043

[^martin-löf-1984]: Martin-Löf, Per, 1984, *Intuitionistic Type Theory. Notes by Giovanni Sambin of a Series of Lectures given in Padua, June 1980*, Naples: Bibliopolis.

[^mcdowell-2009]: McDowell, John, 2009, *Having the World in View: Essays on Kant, Hegel and Sellars*, Cambridge, MA: Harvard University Press.

[^peregrin-2014]: Peregrin, Jaroslav, 2014, *Inferentialism. Why Rules Matter*, New York: Palgrave MacMillan.

[^perelman-1958]: Perelman, Chaim and Lucie Olbrechts-Tyteca, 1958, *Traité de l’argumentation : la nouvelle rhétorique*, Paris: Presses Universitaires de France.

[^plato-1997]: Plato, *Gorgias*, in *Plato: Complete Works*, John Cooper and Douglas Hutchinson (eds.), Indianapolis: Hackett, 1997.

[^popek-2012]: Popek, Aude, 2012, “Logical Dialogues from Middle Ages”, in Cristina Barés Gómez, Sébastien Magnier, and Francisco J. Salguero (eds.), *Logic of Knowledge: Theory and Applications*, London: College Publications, pp. 223–244.

[^prakken-2005]: Prakken, Henry, 2005, “Coherence and Flexibility in Dialogue Games for Argumentation”, *Journal of Logic and Computation*, 15(6): 1009–1040. doi:10.1093/logcom/exi046

[^prior-1960]: Prior, Arthur N., 1960, “The Runabout Inference-Ticket”, *Analysis*, 21(2): 38–39. doi:10.1093/analys/21.2.38

[^rahman-1993]: Rahman, Shahid, 1993, *Über Dialoge, Protologische Kategorien und andere Seltenheiten*, Berlin: Peter Lang Verlag

[^rahman-2012]: –––, 2012, “Negation in the Logic of First Degree Entailment and *Tonk*”, in *The Realism-Antirealism Debate in the Age of Alternative Logics*, Shahid Rahman, Giuseppe Primiero, and Mathieu Marion (eds.), Dordrecht: Springer Netherlands, pp. 213–250. doi:10.1007/978-94-007-1923-1_12

[^rahman-2001]: Rahman, Shahid and Helge Rückert (eds), 2001, *New Perspectives in Dialogical Logic*, special issue of *Synthese*, 127(1/2): 57–93.

[^rahman-2005]: Rahman, Shahid and Laurent Keiff, 2005, “On How to Be a Dialogician: A Short Overview on Recent Developments on Dialogues and Games”, in *Logic, Thought and Action*, Daniel Vanderveken (ed.), Dordrecht: Springer Netherlands, pp. 359–408. doi:10.1007/1-4020-3167-X_17

[^rahman-2009]: Rahman, Shahid, Nicolas Clerbout, and Laurent Keiff, 2009, “On Dialogues and Natural Deduction”, in Giuseppe Primiero and Shahid Rahman (eds.), *Acts of Knowledge: History, Philosophy and Logic*, London: College Publications, pp. 301–336.

[^rahman-2018]: Rahman, Shahid, Zoe McConaughey, Ansten Klev, and Nicolas Clerbout, 2018, *Immanent Reasoning or Equality in Action: A Plaidoyer for the Play Level*, (Logic, Argumentation & Reasoning 18), Cham: Springer International Publishing. doi:10.1007/978-3-319-91149-6

[^ranta-1994]: Ranta, Aarne, 1994, *Type-Theoretical Grammar*, Oxford: Oxford University Press.

[^read-2008]: Read, Stephen, 2008, “Harmony and Modality”, in Cédric Dégremont, Laurent Keiff and Helge Rückert (eds.), *Dialogues, Logics and Other Strange Things: Essays in Honour of Shahid Rahman*, London: College Publications, pp. 285–303.

[^read-2010]: –––, 2010, “General-Elimination Harmony and the Meaning of the Logical Constants”, *Journal of Philosophical Logic*, 39(5): 557–576. doi:10.1007/s10992-010-9133-7

[^redmond-2011]: Redmond, Juan, 2011, *Logique Dynamique de la Fiction. Pour une approche dialogique*, London: College Publications.

[^redmond-2011-2]: Redmond, Juan and Matthieu Fontaine, 2011, *How to Play Dialogues. An Introduction to Dialogical Logic*, London: College Publications.

[^rückert-2001]: Rückert, Helge, 2001, “Why Dialogical Logic?”, in Heinrich Wansing (ed.), *Esssays on Non-Classical Logic*, Singapore: World Scientific, pp. 165–185. doi:10.1142/4799

[^rückert-2011]: –––, 2011, *Dialogues as a Dynamic Framework for Logic*, London: College Publications.

[^schroeder-heister-2008]: Schroeder-Heister, Peter, 2008, “Lorenzen’s Operative Justification of Intuitionistic Logic”, in *One Hundred Years of Intuitionism (1907–2007): The Cerisy Conference*, Mark van Atten, Pascal Boldini, Michel Bourdeau, and Gerhard Heinzmann (eds.), (Publications Des Archives Henri Poincaré / Publications of the Henri Poincaré Archives), Basel: Birkhäuser, pp. 214–240.

[^sellars-1963]: Sellars, Wilfrid, 1963, *Science, Perception and Reality*, London: Routledge & Kegan Paul and New York: The Humanities Press. Reprinted, Atascadero, CA: Ridgeview Publishing Company, 1991.

[^sellars-1997]: –––, 1997, *Empiricism and the Philosophy of Mind*, Cambridge, MA: Harvard University Press.

[^shafiei-2018]: Shafiei, Mohammad, 2018, *Meaning and Intentionality: a Dialogical Approach*, London: College Publications.

[^smullyan-1968]: Smullyan, Raymond M., 1968, *First-Order Logic*, New York: Dover Publications.

[^sørensen-2006]: Sørensen, Morten Heine and Paweł Urzyczyn, 2006, *Lectures on the Curry-Howard Isomorphism*, New York: Elsevier Science.

[^sørensen-2007]: –––, 2007, “Sequent Calculus, Dialogues, and Cut-Elimination”, in Erik Barendsen, Herman Geuvers, Venanzio Capretta, and Milad Niqui (eds.), *Reflections on Type-Theory, λ-Calculus, and the Mind: Essays Dedicated to Henk Barendregt on the Occasion of His 60th Birthday*, Nijmegen: Radboud Universiteit Nijmegen, pp. 253–261.

[^sterling-2021]: Sterling, Jonathan, 2021, “Higher Order Functions and Brouwer’s Thesis”, *Journal of Functional Programming*, 31: E11. doi:10.1017/S0956796821000095

[^sundholm-1997]: Sundholm, Göran, 1997, “Implicit Epistemic Aspects of Constructive Logic”, *Journal of Logic*, Language and Information, 6(2): 191–212. doi:10.1023/A:1008266418092

[^sundholm-2001]: –––, 2001, “A Plea for Logical Atavism”, in Ondrey Majer (ed.), *The Logica Yearbook 2000*, Prague: Filosofía, pp. 151–162.

[^sundholm-2006]: –––, 2006, “Semantic Values for Natural Deduction Derivations”, *Synthese*, 148(3): 623–638. doi:10.1007/s11229-004-6298-z

[^sundholm-2012]: –––, 2012, “‘Inference versus Consequence’ Revisited: Inference, Consequence, Conditional, Implication”, *Synthese*, 187(3): 943–956. doi:10.1007/s11229-011-9901-0

[^toulmin-1958]: Toulmin, Stephen Edelston, 1958, *The Uses of Argument*, Cambridge: Cambridge University Press.

[^trafford-2017]: Trafford, James, 2017, *Meaning in Dialogue: An Interactive Approach to Logic and Reasoning*, (Studies in Applied Philosophy, Epistemology and Rational Ethics 33), Cham: Springer International Publishing. doi:10.1007/978-3-319-47205-8

[^uckelman-2014]: Uckelman, Sara L., Jesse Alama, and Aleks Knoks, 2014, “A Curious Dialogical Logic and Its Composition Problem”, *Journal of Philosophical Logic*, 43(6): 1065–1100. doi:10.1007/s10992-013-9307-1

[^vaidya-2013]: Vaidya, Anand Jayprakash, 2013, “Epistemic Responsibility and Critical Thinking”, *Metaphilosophy*, 44(4): 533–556. doi:10.1111/meta.12047

[^walton-1984]: Walton, Douglas N., 1984, *Logical Dialogue-Games and Fallacies*, Lanham, MD: University Press of America.

[^woods-1989]: Woods, John, 1989, “The Pragma-Dialectics: A Radical Departure in Fallacy Theory”, *Communication and Cognition*, 24: 43–54.

[^woods-2000]: Woods, John, Andrew Irvine, and Douglas Walton, 2000, *Argument: Critical Thinking, Logic and The Fallacies*, Toronto: Prentice-Hall.
