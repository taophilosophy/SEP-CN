# Propositional Function
**First published Wed Jul 20, 2011; substantive revision Fri Dec 19, 2025**

*Mares, Edwin*

As the name suggests, propositional functions are functions that have propositions as their values. Propositional functions have played an important role in modern logic, from their beginnings in Frege’s theory of concepts and their analyses in Russell’s works, to their appearance in very general guise in contemporary type theory and categorial grammar.

This entry gives an historical overview of the use of propositional functions in logical theory and survey some views about their nature and ontological status.

## 1. Pre-History

Before we begin our discussion of propositional functions, it will be helpful to note what came before their introduction. In traditional logic, the role of propositional functions is approximately held by *terms*. In traditional logic, statements such as ‘dogs are mammals’ are treated as postulating a relation between the subject term, ‘dog’, and the predicate term, ‘mammal’.

A term is treated either extensionally as a class of objects (i.e. the extension of the term) or intensionally as a set of properties (those properties that are essential to something that satisfies the term). The intensional treatment of ‘dogs are mammals’ interprets this sentence as true because the semantic interpretation of the subject is a *superset* of the interpretation of the predicate. For example, the ‘intent’ of the term ‘dog’ includes all the properties that are included in the intent of ‘mammal’. On the extensional treatment of the sentence, however, the sentence is true because the interpretation of the subject (the class of dogs) is a *subset* of the interpretation of the predicate (the set of mammals).

These two treatments of the predicate are typical of the two traditions in traditional logic – the intensional and the extensional traditions. Logicians who can be counted among the intensional logicians are Gottfried Leibniz, Johann Lambert, William Hamilton, Stanley Jevons, and Hugh MacColl. Among the extensional logicians are George Boole, Augustus De Morgan, Charles Peirce, and John Venn.

The way that intensional logics treated certain categorical sentences might seem strange to modern readers. The intension of a predicate, in 20ᵗʰ Century philosophy, includes only those properties that any competent speaker of a language would associate with that predicate. These properties are not enough to make true ordinary statements like ‘every dog in my house is asleep’. But we can make sense of the intensional view of terms by considering its origins. One of the founders of the intensional logic tradition is Leibniz, who thinks that all truths are grounded in the nature of individuals. The complete concept of an individual contains everything that is true of it. Building on this, we can see that the complete concept of a term will include enough to ground any truth about it as well.

In both the intensional and extensional logic traditions, we see theories of complex terms. In the extensional tradition, disjunctive and conjunctive terms are interpreted by taking the union and intersection of classes. The conjunctive term $AB$ is interpreted as the intersection of the class $A$ and the class $B$ and the extension of the disjunctive term $A{+}B$ is understood as the union of the extensions of $A$ and $B$.

In the intensional tradition, the reverse holds. The term $AB$ is interpreted as the union of the properties in the intent of $A$ and the intent of $B$ and $A{+}B$ is interpreted as the intersection of the properties in the intents of $A$ and $B$. This reversal makes sense, since more things fit a smaller number of properties and fewer things fit a larger number of properties. As Leibniz says,

> when I say *Every man is an animal* I mean that all men are included amongst all the animals; but at the same time I mean that the idea of animal is included in the idea of man. ‘Animal’ comprises more individuals than ‘man’ does, but ‘man’ comprises more ideas or more attributes: one has more instances, the other has more degrees of reality; one has the greater extension, the other the greater intension. (Leibniz (1982) 486)

Although some of the logicians working in term logic have very complicated treatments of negation, we can see the origin of the modern conception in the extensional tradition as well. In Boole and most of his followers, the negation of a term is understood as the set theoretic complement of the class represented by that term. For this reason, the negation of classical propositional logic is often called ‘Boolean negation’.

On the subject of Boole, interestingly, he interprets statements as terms of a sort, as sets of times in which they are true. See the entry on [George Boole](https://plato.stanford.edu/entries/boole/#MathAnalLogi1847) for more about his logic and how he interprets it.

## 2. The Logic of Relatives

In Charles Peirce’s ‘Logic of Relatives’ (1883), we see a theory that is in some ways intermediate between traditional term logic and the treatment of predicate expressions as propositional functions. One problem with traditional term logic is that it lacks the ability to deal with relations. Peirce’s logic of relatives is meant to remedy that. He adds terms to Boolean algebra that represent relations, and gives an extensional interpretation of them. They are not propositional functions in the full sense. Peirce’s relatives are ‘common names’ that represent classes of pairs of objects (1883, 328). Thus, the logic of relatives represents a generalization of traditional logic rather than a departure from it.

Peirce extends the algebra of terms to deal with particular features of relations. Like other terms, we can have conjunctive, disjunctive, and negative terms. Where $f$ and $g$ are relatives, then $fg$ represents the class of pairs $(I,J)$ such that $I$ bears both $f$ and $g$ to $J$. Similarly, the disjunctive relative, $f{+}g$ is such that it represent $(I,J)$ if $I$ bears either $f$ or $g$ to $J$ and $f'$ – the negation of the term $f$ – represents the class of pairs $(I,J)$ such that $f$ does not hold between them. Peirce also has a composition operator, $;$ , such that $f{;}g$ names $(I,J)$ if there is some entity $K$ such that $f$ names $(I,K)$ and $g$ names $(K,J)$.

In ‘The Critic of Arguments’ (1892), Peirce adopts a notion that is even closer to that of a propositional function. There he develops the concept of the ‘rhema’. He says the rhema is like a relative term, but it is not a term. It contains a copula, that is, when joined to the correct number of arguments it produces an assertion. For example, ‘__ is bought by __ from __ for __’ is a four-place rhema. Applying it to four objects $a, b, c$, and $d$ produces the assertion that $a$ is bought by $b$ from $c$ for $d$ (ibid. 420).

One especially interesting point about Peirce’s rhema is that he uses the same chemical analogy as Frege does when they discuss the relation between relations and their arguments. They both compare relations (and properties) to ‘atoms or radicals with unsaturated bonds’. What exactly this analogy says of relations or properties, either in Frege or Peirce is somewhat unclear.

See the entry on Peirce’s logic, for a more complete exposition of his work.

## 3. Propositional Functions and the Birth of Mathematical Logic

In the work of Giuseppe Peano (1858–1932), we find another important step towards the modern notion of a propositional function. Although his work is not as sophisticated as Frege’s (see below), it is important in particular because of its influence on Bertrand Russell.

In his ‘Principles of Arithmetic Presented by a New Method’ (1889), Peano introduces propositional connectives in the modern sense (an implication, negation, conjunction, disjunction, and a biconditional) and propositional constants (a verum and a falsum).

More important for us is his treatment of quantification. Peano allows propositions to contain variables, that is to say, he utilizes open formulas. He does not give an interpretation of open formulas. He does not tell us what they represent. But they are used in his theory of quantification. Peano only has a universal quantifier. He does not define an existential quantifier in the ‘Principles’. The quantifier is always attached to a conditional or biconditional. Quantified propositions are always of the form

> $A \supset_{x,y,\ldots} B$

or

> $A =_{x,y,\ldots} B$

Peano reads ‘$A \supset_{x,y,\ldots} B$’ as saying ‘whatever $x,y,\ldots$ may be, from the proposition $A$ one deduces $B$’ and ‘=’ is Peano’s biconditional, that he defines in the usual way from the conditional and conjunction.

Predication is understood, as in Boole and his followers, as set membership. In the formula $a\supset b$, the symbols ‘$a$’ and ‘$b$’ denote classes and the horseshoe (or hook) is a subset sign. Thus, the horseshoe is understood in Peano as both material implication and as subset. Variables are understood as ‘indeterminate objects’, but Peano does not discuss what this means. (Frege later cricitises that terminology as meaning nothing.)

## 4. Fregean Functions and Concepts

Frege’s central ontological distinction is between functions and objects. A function is an unsaturated entity that requires an object as its argument to be, in some sense, complete. In the *Begriffsschrift*, we first see the interpretation of an atomic sentence – $\Phi(A)$ – as meaning that a function $\Phi$ is applied to an argument $A$. In the Begriffsschrift, formulae represent *judgeable contents*. Judgeable contents are remarkably similar to Russellian propositions but also to Bolzano’s propositions-in-themselves and Meinong’s objectives.

In the early 1890s, Frege rejects judgeable contents and instead comes to think of sentences as repersenting sentential senses (or “thoughts”) and, as their denotations, truth values (i.e. the True and the False).

Consider the sentence

> My dog is asleep on the floor.

This sentence, like all linguistic expressions, has both a sense and a referent. Its sense is an abstract object – a thought. Its referent is its truth value (which as I write this is the True). We will discuss Frege’s analysis of the thought soon, but right now let us look at the referents of the expressions that make up this sentence.

The expression ‘my dog’, according to Frege, is a singular term. It picks out an object (my dog, Zermela). The expression ‘is asleep on the floor’ refers to a *concept*. Concepts are functions of a sort. In this case, the concept is a function from objects to truth values (which are also objects). So, we can treat the above sentence as representing the concept __ *is asleep on the floor* as applying to the object *my dog*.

Frege’s concepts are very nearly propositional functions in the modern sense. Frege explicitly recognizes them as functions. A concept, like any other function and like Peirce’s rhema, is *unsaturated*. They are in some sense incomplete. Although Frege never gets beyond the metaphorical in his description of the incompleteness of concepts and other functions, one thing is clear: the distinction between objects and functions is the main division in his metaphysics. There is *something* special about functions that makes them very different from objects and this something is their unsaturatedness.

Let us consider ‘my dog is asleep on the floor’ again. Frege thinks that this sentence can be analyzed in various different ways. Instead of treating it as expressing the application of __ *is asleep on the floor* to *my dog*, we can think of it as expressing the application of the concept

> *my dog is asleep on* __

to the object

> *the floor*

(see Frege 1919)[^frege-1919]. Frege recognizes what is now a commonplace in the logical analysis of natural language. *We can attribute more than one logical form to a single sentence*. Let us call this the **principle of multiple analyses**. Frege does not claim that the principle always holds, but as we shall see, modern type theory does claim this.

With regard to the sense of sentences, they are also the result of applying functions to objects. The sense of ‘my dog’ is an abstract object. The sense of ‘is asleep on the floor’ is a function from individual senses, like that of ‘my dog’, to thoughts (see Frege 1891)[^frege-1891]. The sense of ‘is asleep on the floor’ is a *conceptual sense*. It would seem that the principle of multiple analyses holds as much for senses as it does for referents. Frege, however, sometimes talks as if the senses of the constituent expressions of a sentence are actually contained somehow in the thought. It is difficult to understand how all such senses could be in the thought if there are different ways in which the sentence can be analyzed into constituent expressions.

In addition to concepts and conceptual senses, Frege holds that there are extensions of concepts. Frege calls an extension of a concept a ‘course of values’. A course of values is determined by the value that the concept has for each of its arguments. Thus, the course of values for the concept __ *is a dog* records that its value for the argument Zermela is the True and for Socrates is the False, and so on. If two concepts have the same values for every argument, then their courses of values are the same. Thus, courses of values are extensional.

Frege’s strict ontological division of entities into functions and objects leads to some rather interesting problems. Take, for example, his infamous claim that the phrase “the concept horse” does not denote a concept. Concepts are all functions, but “the concept horse” is something that can be used as the subject of a sentence, and hence names an object. Nothing for Frege can be both an object and a function. Thus, “the concept horse” must name something else, an object that represents the concept (see Frege (1892) and Parsons (1986)). This view makes for a rather complicated theory of reference and a rather complicated understanding of how Frege’s philosophical metalanguage can accurately describe his own ontology.

For more about Frege’s theory of concepts and its relation to his logic, see the entry on Frege’s theorem and foundations for arithmetic.

## 5. The Emergence of Propositional Functions

The term ‘propositional function’ appears in print for the first time in Bertrand Russell’s *Principles of Mathematics* (1903). Russell introduces the notion through a discussion of kinds of propositions. Consider propositions of the type that says of something that it is a dog. This is the kind ‘$x$ is a dog’. This kind is a propositional function that takes any object $o$ to the proposition that $o$ is a dog.

In this early period, Russell holds that propositions are entities that have individuals and properties and relations as constituents. The proposition that Socrates is a man has Socrates and the property of being a man as constituents. In complex propositions the relation between propositional function and the proposition is less clear. Like Frege, Russell allows the abstraction of a propositional function from any omission of an entity from a proposition. Thus, we can view the proposition

> *if Socrates drinks hemlock he will die*

as representing the application of the function

> *x drinks hemlock $\supset$ x will die*

to Socrates, or the function

> *Socrates will drink x $\supset$ Socrates will die*

to hemlock, and so on. In other words, Russell accepts the principle of multiple analyses.

In the *Principles*, the quantifier ‘all’ is analyzed as a part of referring phrases that pick out classes (1903, 72). This, we can see, is a hold-over from the 19ᵗʰ Century extensional logicians (see Section 1). But in slightly later works, such as ‘On Denoting’ (1905), propositional functions are said to be constituents of universal propositions. According to this analysis the proposition expressed by sentences such as ‘All dogs bark’ is made up of the propositional function *x is a dog* $\supset$ *x barks* and a function (of propositional functions) that is represented by the quantifier phrase ‘all’. Quantified propositions are interesting for us because they contain propositional functions as constituents.

In what follows, Russell’s notation is used to represent Russell’s propositional functions. (Lambda notation is used in the discussion of Montague grammar). Here is a simple example: where ‘$R(a,b)$’ is a well-formed formula,

> $\hat{x}R(x,b), \hat{y}R(a,y), \hat{x}\hat{y}R(x,y), \hat{X}X(a,b), \ldots $

are propositional functions. More generally, where $A(x)$ is an open formula,

> $\hat{x}A(x)$

is a propositional function.

## 6. Propositional Functions in Simple Type Theory

While writing the *Principles of Mathematics*, Russell discovered the paradox that now bears his name. Before we get to Russell’s paradox, let us discuss some the method of **diagonalization** by which this and many other paradoxes are generated.

The power set of a set $S, \wp S$ contains all the subsets of $S$. Georg Cantor (1845–1918) used the method of diagonalization to show that for any set $S, \wp S$ is larger than $S$.

Here is Cantor’s proof. Suppose that $\wp S$ and $S$ are the same size. Then, by the set-theoretic definition of “same size” (more correctly, ‘same cardinality’) there is a one-to-one **surjection** between $S$ and $\wp S$. This means that there is a function that matches up each member of $S$ with a unique member of $\wp S$ so that there are no members of $\wp S$ left over. Let us call this function, $f$. Then, if $x$ is a member of $S, f(x)$ is in $\wp S$. Now, since $\wp S$ is the power set of $S$, it may be that $x$ is in $f(x)$ or it may not be in $f(x)$. Let us now define a set $C$:

> $C = \{x \in S: x \not\in f(x)\}$

Clearly, $C$ is a subset of $S$, so it is in $\wp S$. By hypothesis, $f$ is $\mathbf{onto}$ – for every member $y$ of $\wp S$, there is an $x \in S$ such that $f(x) = y$. Thus there must be some $c \in S$ such that

> $f(c) = C$

Now, either

> $c \in C$

or

> $c \not\in C$.

Suppose that $c$ is in $C$. Then, by the definition of $C, c$ is not in $f(c)$. That is to say, $c \not\in C$. But, if $c$ is not in $C$, then $c \not\in f(c)$. So, by the definition of $C, c$ is in $C$. Thus,

> $c$ is in $C$ if and only if $c$ is not in $C$.

Therefore, the assumption that a set is the same size as its power set leads to a paradox, and so this assumption must be false.

Cantor’s theorem has important consequences for the theory of propositional functions. Consider a model for a (first-order) logical language that has a domain $D$. The variables of the language range over members of $D$. Now let us add predicate variables to the language. These stand for propositional functions. How are we to interpret them in the model? The standard way of doing so – that is inherited from the extensional logic tradition – is to have predicate variables range over subsets of the domain. A model in which predicate variables range over all subsets of the domain is called a ‘standard model’ for second-order logic. Cantor’s theorem tells us that the domain for predicate variables in the standard model is larger than the domain for individual variables. If we have predicates of predicates, then the domain for third order predicates is even larger. And so on.

Russell’s paradox is very closely related to Cantor’s theorem. There are two versions of the paradox: (1) the class version; (2) the propositional function version. This entry only discusses the propositional function version of the paradox.

In his early writings, Russell wants logic to be a universal science. It should allow us to talk about properties of everything. By this he means that the variables in logic should be taken to range over all entities. But propositional functions, at least in the *Principles*, are entities. So variables should range over them. Let’s consider a logic in which variables range over both individuals and propositional functions – and propositional functions are all of only a single type. Now consider the predicate $R$ such that,

> $(\forall x)(Rx = \neg xx)$

(This may look ill-formed, but that’s because we are used to making type distinctions. This is a discussion of what happens when we don’t make those distinctions.) If we instantiate and substitute $R$ for $x$, we obtain

> $RR \equiv \neg RR$

It seems, then, that the treatment of variables as completely general together with the liberty to define propositional functions by means of any well-formed formula enables us to derive a contradiction.

Russell blocks the contradiction in the *Principles* by the introduction of a theory of types. This is a simple theory of types, that only distinguishes between the types of various propositional functions (or, in its class-form, of classes). Let us depart from Russell’s own exposition of the theory of types in order to give a more rigorous and more modern version of the theory. This will make my presentations of the ramified theory of types and more modern versions of type theory easier.

We’ll use one basic type, $i$ (the type of individuals) and define the types as follows:

1. $i$ is a type;
2. if $t_1 ,\ldots ,t_n$ are types, then so is $\langle t_1, \ldots ,t_n\rangle$, where $n \ge 0$.
3. Nothing else is a type except by repeated applications of (1) and (2).

The type $\langle t_1 ,\ldots ,t_n\rangle$ is the type of a relation among entities of types $t_1 ,\ldots ,t_n$. But, for simplicity, we will interpret this as the type of a function that takes these entities to a proposition. (Note that when $n = 0$, then the empty type, $\langle \rangle$, is the type for propositions.) This definition incorporates the idea of a well-founded structure. There are no cycles here. We cannot have a function that takes as an argument a function of the same or higher type. Thus, simple type theory bans the sort of self-application that gives rise to Russell’s paradox.

The type hierarchy corresponds neatly to the hierarchy of domains that we saw in our discussion of Cantor’s theorem. A unary predicate has the type $\langle i\rangle$; its domain is $D$ – the set of individuals. A unary predicate of predicates has the type $\langle \langle i\rangle \rangle$, and this corresponds to the domain of subsets of $D$. And so on.

For more, see the entry on Russell’s paradox.

## 7. Propositional Functions in Ramified Type Theory

After the *Principles*, however, Russell comes to believe that the simple theory of types is insufficient. The reason for it has to do with the *liar paradox*. Suppose that ‘$L$’ is a name for the proposition:

> $L$ is false.

This statement is false if and only if it is true. The problem here has something to do with self-reference, but it cannot be avoided by the simple theory of types alone. For simple types only give us a hierarchy of types of propositional functions. In simple type theory, all propositions have the same type.

The idea behind ramified type theory is to introduce a hierarchy of propositions as well. On this view, propositions and propositional functions have an *order*. If a propositional function is applied to a proposition of a particular order, then it yields a proposition of a higher order. And every function must have a higher order than its arguments. Thus, we avoid the liar paradox by banning a proposition from occurring within itself. If a proposition $p$ occurs within another proposition, as the argument of a function such as *x is false*, then the resulting proposition is of a higher order than $p$.

Unfortunately, Russell never gives a precise formulation of ramified type theory. Perhaps the best formulation is due to Alonzo Church (1976).[^note-1]

Almost at the same time as he adopts the ramified theory of types, Russell abandons propositions. From about 1908 until 1918, although Russell retains the idea that there are true propositions (i.e. he accepts facts), he denies that there are false ones. When we think about something that is false, say, *Zermela is a cat*, we are not thinking about a false proposition, but rather the objects of our thought are just Zermela and the property of being a cat. It might seem odd to have a hierarchy especially designed to stratify the propositions and then claim that there are no propositions. Some interpreters, however, have claimed that Russell’s denial of the existence of propositions should not be taken seriously and that there are very good reasons to read *Principia* as being largely a theory of propositions (see Church 1984)[^church-1984].

One reason to take the ramified theory of types seriously (even without accepting propositions) is that it can be usefully incorporated into a substitutional theory of quantification. On the substitutional interpretation of the quantifiers, a universally quantified formula such as $(\forall x)Fx$ is true if and only if all of its instances $Fa_1, Fa_2, Fa_3,\ldots$ are true. Similarly, $(\forall x)Fx$ is true if and only if at least one of its instances is true.

Consider a substitutional interpretation of quantifiers with variables ranging over predicates, as in the formula, $(\forall P)Pa$. This formula is true if and only if all of its instances are true. On a simple theory of types, the type of the variable $P$ is $\langle i\rangle$, since its arguments are all individuals (or singular terms). But the simple type of the function, $(\forall P)Px$ is also $\langle i \rangle$. So an instance of $(\forall P)Pa$ is $(\forall P)Pa$ itself. A substitutional interpretation of the quantifiers requires that instances be simpler than the formulas of which they are instances. In this case, all we find out is that a particular formula is true only if it is true. This is uninformative and it seems viciously circular.

To block this sort of circularity, we can turn to the ramified theory of types. On the ramified theory, the propositional function $(\forall P)Px$ is of order 2, because of the presence of the quantifier binding a variable of order 1. In this way, the ramified theory forces formulas to be simpler (at least in terms of order) than the formulas of which they are instances (see Hazen and Davoren 2000)[^hazen-2000].

## 8. Universals and Propositional Functions

In *The Problems of Philosophy* (1912), Russell gives a sustained argument for the existence of universals. A universal is an entity that can exist in many different things. It is predicable of those things and, in may cases, is supposedly perceptable in them. As Russell says, we are “acquainted” with them. Although propositional functions are often used to represent universals’ holding of things, propositional function and universal are distinct ontological categories.

Linsky (1999) argues that Russell distinguished between propositional functions and universals, and it would be difficult to see how he could have identified them. When Russell believed in propositions, he thought of propositions as complex structures of individuals and universals. Consider, for example, the proposition that Dave loves Carol:

> $\langle\Loves,d,c\rangle$

The principle of multiple analyses allows us to construct several different propositional functions from this proposition. Among them are those that are represented by the following expressions:

> $\hat{x}\Loves(x,c), \hat{y}\Loves(d,y), \hat{R}R(d,c), \ldots$

Russell continued to believe in the existence of universals, even after he had abandoned propositions. This view is discussed further in section section 9.

To move away from discussing Russell for a moment, George Bealer (1989) gives some general reasons for distinguishing between universals and propositional functions. Here is one of his arguments. Our modern notion of a function is an extensional one: if functions $f$ and g have the same values for every argument, then $f$ and $g$ are identical with one another. But our notion of a universal (or a property) is intensional. We could live in a world in which every round thing is red and every red thing is round, but this would not make roundness and redness the same property. We might even want to distinguish between two properties that are necessarily co-extensive. Consider the property of being a possible world that satisfies the law of excluded middle and being a possible world that satisfies the law of non-contradiction. These two laws are logically equivalent, but we might want, in order to provide an adequate theory of intentionality, say, to distinguish these two properties. But the corresponding propositional functions would be the same.

## 9. What is a Propositional Function in Russell?

After 1905, we see in Russell a parsimonious inclination. He wants to prune a number of entities from his ontology. Some time between 1908 and 1910 he begins to deny the existence of propositions and this denial continues until he develops a theory of propositions as structures of images or words in (1918). What, then, is the fate of propositional functions? The logicism of *Principia* needs propositional functions. Facts about classes (which form the basis of the reduction of mathematics to logic) are reducible to facts about propositional functions. If propositional functions themelves disappear altogether, then, the nature of the logicist reduction becomes completely obscure.

Whitehead and Russell say:

> By a ‘propositional function’ we mean something which contains a variable $x$, and expresses a proposition as soon as a value is assigned to $x$. That is to say, it differs from a proposition solely by the fact that it is ambiguous: it contains a variable of which the value is unassigned. (1910, 38).

In this passage, it seems as though they are saying that a propositional function is an ambiguous proposition, but it is unclear exatly what that means.

What it does mean is a matter of debate among Russell scholars. On the realist side are the interpretations given by Alonzo Church (1984) and Warren Goldfarb (1989). Goldfarb thinks that the logical theory of *Principia* is motivated by Russell’s attempt to find the real nature of propositional functions and that this nature is independent of our thinking about it. Goldfarb has a good point, since Russell’s logic is supposed to be a perspicuous representation of the way things actually are. Thus Goldfarb interprets Russell as a Platonist about propositional functions.

Landini (1998) argues that this realist interpretation cannot be correct. By the time that Whitehead and Russell had began to write *Principia*, Russell had already rejected the existence of propositions. Without the existence of propositions, what sense can we make of the claim that propositional variables are ambiguous propositions? Landini answers that the only entities that Russell has in his ontology that can do the jobs that propositional functions are supposed to do are linguistic entities: open formulas ((1998) p 277).

A position that occupies a middle ground between the realism of Church and Goldfarb and Landini’s nominalism is the logical constructivist view. This is put forward by Kurt Gödel (1944). On Gödel’s interpretation, Russell’s propositional functions are human constructs of some sort. They depend on our ability to think about them or refer to them. But it seems that when Whitehead and Russell quantify over them in *Principia*, there need to be more propositional functions than anyone every has or ever will imagine. A different version of the constructive interpretation can be found in Linsky (1999). On this view, propositional functions are logical constructions, which depend on the abstractions that one *could* make, rather than the ones that are in fact made.

With regard to abstractions, however, it would seem that propositional functions must be abstracted from something that actually exists. If propositions do not exist, then there must be something else that from which propositional functions are abstracted. One possibility is that propositional functions are abstracted from facts. Consider again the proposition that Dave loves Carol. Suppose that Dave and Carol do not even know each other. But they do have some relation to one another. Perhaps they live 150 miles from one another. Thus, there is a fact, $\langle M,d,c\rangle$. We can then abstract the propositional functions

> $\hat{R}R(d,c), \hat{R}\hat{x}\hat{y}R(x,y), \ldots.$

We can then construct other functions, such as

> $\hat{R}(\hat{x}R(x,c))\Loves,$

which is extensionally the same as

> $\hat{x}\Loves(x,c).$

Note that

> $\hat{R}R(d,c)\Loves, \hat{x}\Loves(x,c)d, \ldots $

and similar constructions are not the same as the proposition that Dave loves Carol. That proposition, if it exists (and is a “Russellian proposition”), is not a construction and does not have propositional functions as constituents. But we should also note that the construction of propositional functions allows that there do exist these sorts of *complete* constructions that might substitute for propositions in some contexts.

## 10. Possible Worlds and Propositional Functions

Jumping ahead some decades, adding possible worlds together with set theory to the logicians’ toolbox has provided them with a very powerful and flexible framework for doing semantics.

The modern notion of a function was discussed briefly in section 8. Here we need to say a bit more about it. From a set theoretic point of view, a function is a set of ordered pairs. If $\langle a,b\rangle$ is in a function $f$, this means that the value of $f$ for the argument $a$ is $b$ or, more concisely, $f(a) = b$. By the mathematical definition of a function, for each argument of a total (as opposed to partial) function there is one and only one value. So, if the ordered pair $\langle a,b\rangle$ is in a function $f$ and so is $\langle a,c\rangle$, then $b$ is the same thing as $c$. (A total function is a function that has a value for any argument. Thus, for example, the function $x^2$ is total, when its domain is the natural numbers. The function $1/x$, however, is partial on that same domain. It has values for all values of $x$ except 0. A partial function, then, is one that is undefined when given certain arguments. It would make sense to discuss partial propositional functions if the topic of truth-value gaps were to be included in this entry.)

The possible worlds construction of propositional functions begins with possible worlds, individuals, and some simple set theory. Let us call the set of possible worlds $W$. A proposition is a set of possible worlds. The proposition that Zermela barks, for example, is all the sets of worlds in which Zermela barks. We also need to assume that there is a set $I$ of possible individuals (i.e., the individuals that exist in at least one possible world). We now have all the materials to construct a simple type-theoretic hierarchy of functions.

The usual treatment of the meaning of predicates differs slightly from the manner described here. Usually, the intension of a predicate is taken to be a function from possible worlds to sets of individuals (or sets of ordered pairs of individuals for binary relations, ordered triples for three place relations, and so on). Strictly speaking, these functions are not propositional functions because they do not take propositions as values. But for each such function, we can construct an ‘equivalent’ propositional function by using a process called ‘Currying’ after the logician Haskell Curry. Let’s start with a function $f$ from worlds to sets of individuals. Then we can construct the corresponding propositional function $g$ as follows. For each world $w$ and individual $i$, we construct $g$ so that

> $w$ is in $g(i)$ if and only if $i$ is in $f(w)$.

So, the more standard treatment of the meanings of predicates is really equivalent to the use of propositional functions.

## 11. Montague Semantics

Now that we have a whole hierarchy of propositional functions, we should find some work for them to do. One theory in which propositional functions do good work is Montague semantics, developed in the late 1960s by Richard Montague.

In order to understand Montague’s method we need to understand *lambda abstraction*. Lambda abstracts are very similar to Russell’s circumfex variable binders for propositional functions. For the formula $A(x)$ we read the expression $\lambda x[A(x)]$ as a predicate expression. Its extension (in a given possible world) is the set of things that satisfy the formula $A(x)$. Lambda abstractors are governed by two rules, known as $\alpha$-conversion and $\beta$-reduction:

> $(\alpha$-con) $A(a)$ (a formula with $a$ free for $x)$ can be replaced by $\lambda x[A(x)]a$.

> $(\beta$-red) $\lambda x[A(x)]a$ can be replaced by $A(a)$ (where $x$ is free for $a$ in $A(x))$.

Because of the equivalence between a formula $A(x)$ and $\lambda x[A(x)]a$, one might wonder why add lambda abstractors to our language. In Montague semantics, the answer has to do with the very direct way that he translates expressions of natural languages into his logical language. We will discuss that soon, but first let us learn a bit about Montague’s *intensional logic*.

Montague adds two other pieces of notation to his language: $^{\wedge}$ and $^{\vee}$. The expression $^{\wedge}\lambda x[Fx]$ represents a function from worlds to sets of individuals. Given a possible world $w, ^{\wedge}\lambda x[Fx]$ represents a function that takes $w$ to the extension of $\lambda x[Fx]$. The operator $^{\vee}$ takes expressions of the form $^{\wedge}\lambda x[Fx]$ ‘down’ to their extensions at the world in which the expression is being evaluated. For example, the extension of $^{\vee\wedge}\lambda x[Fx]$ at $w$ is just the same as the extension of $\lambda x[Fx]$ at $w$.

What is so special about Montague semantics is that it can be used in a very direct way as a semantics for large fragments of natural languages. Consider the following sentence:

> Zermela barks.

The meaning of this sentence is understood in Montague semantics as a structure of the meanings of its constituent expressions. Montague represents the meanings of expressions using translation rules. Here we use the following translation rules:

> **Zermela** translates into $\lambda P[(^{\vee}P)z]$

> **barks** translates into $^{\wedge}B$

Now we can construct a formula that gives the meaning of ‘Zermela barks’:

> $\lambda P[(^{\vee}P)z]^{\wedge}B$

Notice that in constructing the sentence we place the expressions in the same order in which they occur in English. The use of lambda abstracts allows us to reverse the order of two expressions from the way in which they would appear in ordinary statements of a formal logical language (that does not have lambdas). Now we can use $\beta$-reduction to obtain:

> $(^{\vee \wedge}B)z$

And now we apply Montague’s rule to eliminate $^{\vee \wedge}$:

> $Bz$

In this process we start with an expression that has the same order of expressions as the original English sentence and then reduce it to a very standard formula of logic. This tells us that the truth condition of the sentence ‘Zermela barks’ is the set of worlds that is the proposition expressed by $Bz$. Of course we knew that independently of Montague’s work, but the point is that the Montague reduction shows us how we can connect the surface grammar of English sentences to the formula of our logical language. The formula of standard logic, moreover, displays its truth-conditions in a very perspicuous way. So, the Montague reduction shows us the connection between sentences of natural languages to their truth conditions.

## 12. Categorial Grammar

Categorial grammars were first constructed in the 1930s by Kazamir Ajdukiewicz (1890–1963), and developed by Yehoshua Bar Hillel (1915–1975) and Joachim Lambek (1922–2014) in the 1950s an 1960s. Categorial grammars are logical tools for representing the syntax of languages.

In categorial grammar, the syntax of languages is represented using a different sort of generalization of the functional notation than in Montague semantics. In Montague Semantics, the lambda abstractor is used to move the meaning of an expression to the location that the expression occupies in a sentence. In categorial grammar, predicates and many other sorts of expressions are taken to be functions of sorts. But there is a distinction in categorial grammar between two sorts of application of a function to its arguments.

Let’s see how this works. Let’s start with the primitive types CN (common noun) and NP (noun phrase). The indefinite article ‘a’ takes a common noun (on its right) and returns a NP. So it has the type NP/CN. The common noun ‘dog’, of course, has the type CN. We write ‘$A$ has the type $T$’ as ‘$A\vdash T$’. So we have,

> $\mathbf{a} \vdash$ NP/CN

and

> $\mathbf{dog} \vdash$ CN

In order to put these two sequents together, we can use a form of the rule modus ponens which says that from a sequent $X \vdash A/B$ and a sequent $Y \vdash B$, we can derive the sequent $X{.}Y \vdash A$. We can use this rule to derive:

> $\mathbf{a}.\mathbf{dog} \vdash$ NP

Moreover, an intransitive verb has the type NP\S, where S is the type of sentences. The backslash in NP\S means that the expression takes an argument of type NP *on the left side* and returns an expression of type S. The verb ‘barks’ is intransitive, that is,

> **barks** $\vdash$ NP\S

The version of modus ponens that we use with the backslash is slightly different. It tells us that from $X \vdash A \backslash B$ and $Y \vdash A$ we can derive $Y{.}X \vdash B$. So we now can obtain,

> $(\mathbf{a}.\mathbf{dog})$.**barks** $\vdash$ S

This says that ‘a dog barks’ is a sentence.

The logics used to describe grammars in this way are substructural logics.

What is of interest to us here is that in categorial grammars determiners such as ‘a’ and verbs are thought of as functions, but they can differ from one another in terms of whether they take arguments on their right or on their left. In the set theoretic concept of function as a set of ordered pairs, functions are thought of just in terms of their correlating arguments with values. A function, as it is understood in categorial grammar has more structure than this. This is an interesting generalization of the notion of a function as it is used in logic. We can see that it also has important links to the concept of a propositional function, especially as it is used in Montague semantics.

In categorial grammar we can attribute more than one type to a single expression in a language. Let us call this the **principle of multiple types**. Here is an example due to Mark Steadman. Consider the sentence

> I dislike, and Mary enjoys, musicals.

The transitive verbs ‘dislike’ and ‘enjoys’ have the type (NP\S)/NP, that is, they take a noun phrase on their right and return a verb phrase. But in the case of ‘I dislike, and Mary enjoys musicals’ the verbs are separated from their object and joined to their objects. Steadman deals with this by raising the type of the subjects ‘I’ and ‘Mary’. Usually, we treat these words as having the type NP, but here they have the type S/(NP\S). This is the type of an expression that takes a verb phrase on its right and returns a sentence. Steadman then uses a rule that makes the backslash transitive and derives that ‘I.dislike’ has the type S/NP, which takes a noun phrase (such as ‘musicals’) on its right an returns a sentence.

We can see that the principle of multiple types also holds if analyze sentences other type theories, such as the simple theory of types. For consider the sentence

> Mary eats a hamburger.

In interpreting this sentence we can take ‘Mary’ to be of type $i$, but we can also take it to be of type $\langle \langle i \rangle \rangle$, that is, the type of a propositional function on propositional functions of individuals. We can also raise the type of ‘eats a hamburger’ to $\langle \langle \langle i \rangle \rangle \rangle$, a propositional function on propositional functions on propositional functions on individuals. And so on. The principle of multiple types and the principle of multiple analyses together show that a single expression or sentence can be interpreted as having a very large number of logical forms.

## 13. Conclusion

This brief history of propositional functions shows that they are useful entities and that they have played a central role in logic as it is used in philosophy and linguistics. The entry has omitted the more mathematical uses of propositional functions, for example, in Russell’s and Ramsey’s constructions of classes, in Paul Halmos’s polyadic algeba, and in Leon Henkin’s general models for higher-order logic. But the topic of propositional functions is a big one and we can’t cover it all in a single encyclopedia article.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

### Important Works in which Propositional Functions Play a Key Role

### Textbooks in which Propositional Functions Feature Prominently

### Other Primary Sources

### Other Works Cited

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=propositional-function). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/propositional-function/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=propositional-function&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/propositional-function/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

[Please contact the author with suggestions.]

## Related Entries

Frege, Gottlob: theorem and foundations for arithmetic | logic: modal | logic: second-order and higher-order | logic: substructural | Peirce, Charles Sanders: logic | propositional attitude reports | Russell, Bertrand | Russell’s paradox

## Notes（原文脚注）

## Notes to Propositional Function

[^note-1]: Here is Church’s inductive definition of the ramified hierarchy

1. $i$ is a type;
2. If $t_1 , \ldots ,t_n$ are types then $\langle t_1 , \ldots ,t_n\rangle /m$ is a type, where $m$ is a natural number greater than or equal to 1.

An expression of type $\langle t_1 , \ldots ,t_n\rangle /m$ is a propositional function that takes arguments of types $t_1 ,\ldots ,t_n$to a proposition of the order $N$, where $N = m +$ the highest order of $t_1 ,\ldots ,t_n$ (the order of $i$ is 0). Since $m$ must be at least 1, the order of proposition that results from applying a propositional function to $p$ must be at least one greater than the order of $p$.

[^church-2019]: Church, Alonzo, 2019, *The Collected Works of Alonzo Church*, edited by Tyler Burge and Herbert Enderton, Cambridge, MA: MIT Press. (This has Church’s papers in which he develops an intensional logic. In this logic the hierarchy of propositional functions plays an important role in dealing with paradoxes concerning propositional attitude reports – i.e., statements about what people believe, think, deny, etc.)

[^cresswell-1973]: Cresswell, M. J., 1973, *Logics and Languages*, London: Methuen. (This presents a simpler cousin of Montague semantics. The view is used as a semantics for propositional attitude reports in M. Cresswell, *Structured Meanings*, Cambridge, MA: MIT Press, 1985.)

[^frege-1892]: Frege, Gottlob, 1892, “On Concept and Object”, in *Collected Papers*, Oxford: Blackwell, 1991, 182–194. (This is the classic presentation of Frege’s notion of a concept.)

[^goldblatt-2011]: Goldblatt, Robert, 2011, *Quantifers, Propositions and Identity*, Cambridge: Cambridge University Press. (This presents a new semantics for modal predicate logic that uses propositions as well as worlds. Chapter 4 explores some formal reasons for also adding propositional functions to the semantics.)

[^montague-1973]: Montague, Richard, 1973, *Formal Philosophy*, New Haven: Yale University Press. (The latter half of the book is about Montague’s intensional logic and his semantics for natural language.)

[^ramsey-1925]: Ramsey, Frank, 1925, “Foundations of Mathematics”, in F. Ramsey, *Foundations: Essays in Philosophy, Logic, Mathematics and Economics*, Atlantic Highlands, NJ: Humanities Press, 1978, 152–212. (This presents a theory of propositional functions as a key element of Ramsey’s philosophy of mathematics.)

[^russell-1903]: Russell, Bertrand, 1903, *The Principles of Mathematics*, New York: Norton and Norton. (This is Russell’s first sustained discussion of propositional functions.)

[^whitehead-1910]: Whitehead, Alfred North, and Bertrand Russell, 1910–1913 [1925], *Principia Mathematica*, Cambridge: Cambridge University Press. (This is a sustained, but extremely difficult, presentation of ramified type theory.)

[^dowty-1981]: Dowty, David R., Robert E. Wall, and Stanley Peters, 1981, *Introduction to Montague Semantics*, Dordrecht: Reidel, 1981. (This is a very clear textbook on Montague semantics.)

[^gamut-1991]: Gamut, L. T. F., 1991, *Logic, Language, and Meaning*, Chicago: University of Chicago Press. (A very good and clearly written textbook that covers modal logic, categorial grammar, and Montague semantics, among other topics.)

[^hylton-1990]: Hylton, Peter, 1990, *Russell, Idealism and the Emergence of Analytic Philosophy*, Oxford: Oxford University Press, 1990.

[^hylton-2005]: Hylton, Peter, 2005, *Propositions, Functions, and Analysis: Selected Essays on Russell’s Philosophy*, Oxford: Oxford University Press. (This work and Hylton 1990 are important texts on the interpretation of Russell’s logic. Hylton maintains that Russell’s notion of a propositional function does not fit with the rest of his metaphysics.)

[^moortgat-1988]: Moortgat, Michael, 1988, *Categorial Investigations: Logical and Linguistic Aspects of the Lambek Calculus*, Dordrecht: Foris Publications. (This is a dated but excellent book on categorial grammar.)

[^bealer-1989]: Bealer, George, 1989, “On the Identification of Properties and Propositional Functions”, *Linguistics and Philosophy*, 12: 1–14.

[^boole-1854]: Boole, George, 1854, *An Investigation of the Laws of Thought on Which are Founded the Mathematical Theories of Logic and Probabilities*, New York: Dover, 1958.

[^frege-1891]: Frege, Gottlob, 1891, Letter to Edmund Husserl, dated 24 May 1891, in Frege, *Philosophical and Mathematical Correspondence*, Chicago: University of Chicago Press, 1980, 61–64.

[^frege-1919]: Frege, Gottlob, 1919, “Notes for Ludwig Darmstaedter”, in Frege, *Posthumous Writings*, Chicago: University of Chicago Press, 1979, 253–257.

[^frege-1991]: Frege, Gottlob, *Collected Papers on Mathematics, Logic, and Philosophy*, Oxford: Blackwell, 1991.

[^jevons-1890]: Jevons, W. S., 1890, *Pure Logic and other Minor Works*, Whitefish, MT: Kessinger Publishing, 2009.

[^peano-1889]: Peano, Giuseppe, 1889, “The Principles of Arithmetic Presented by a New Method”, in J. van Heijenoort (ed.), *From Frege to Gödel: A Sourcebook in Mathematical Logic, 1879–1931*, Cambridge, MA: Harvard University Press, 1981, 83–97.

[^peirce-1883]: Peirce, C. S., 1883, “The Logic of Relatives”, in *Collected Papers of Charles Sanders Peirce* (Volume III: Exact Logic), Cambridge, MA: Harvard University Press, 1933, 195–209.

[^peirce-1892]: Peirce, C. S., 1892, “The Critic of Arguments”, in *Collected Papers of Charles Sanders Peirce* (Volume III: Exact Logic), Cambridge, MA: Harvard University Press, 1933, 250–264.

[^russell-1912]: Russell, Bertrand, 1912, *The Problems of Philosophy*, Oxford: Oxford University Press.

[^church-1976]: Church, Alonzo, 1976, “Comparison of Russell’s Resolution of the Semantical Antinomies with that of Tarski”, *The Journal of Symbolic Logic*, 41: 747–760.

[^church-1984]: Church, Alonzo, 1984, “Russell’s Theory of Identity of Propositions”, *Philosophia Naturalis*, 21: 513–22.

[^gödel-1944]: Gödel, Kurt, 1944, “Russell’s Mathematical Logic”, in P. A. Schilpp (ed.), *The Philosophy of Bertrand Russell*, New York: Tudor Publishing Co., 123–144.

[^goldfarb-1989]: Goldfarb, Warren, 1989, “Russell’s Reasons for Ramification”, in C. W. Savage and C. A. Anderson (eds.), *Rereading Russell: Essays on Bertrand Russell’s Metaphysics and Epistemology*, Minneapolis: University of Minnesota Press, 24–40.

[^hazen-2000]: Hazen, A. P. and J. M. Davoren, 2000, “Russell’s 1925 Logic”, *Australasian Journal of Philosophy*, 78: 534–556.

[^kneale-1984]: Kneale, William and Martha Kneale, 1984, *The Development of Logic*, Oxford: Oxford University Press.

[^landini-1998]: Landini, Gregory, 1998, *Russell’s Hidden Substitutional Theory*, Oxford: Oxford University Press.

[^lewis-1918]: Lewis, C. I., 1918, *A Survey of Symbolic Logic*, Berkeley: University of California Press.

[^linsky-1999]: Linsky, Bernard, 1999, *Russell’s Metaphysical Logic*, Stanford: Center for the Study of Language and Information Publications.

[^parsons-1986]: Parsons, Terence, 1986, “Why Frege should not have said that “The Concept Horse is not a Concept”$$”, *History of Philosophy Quarterly*, 3: 449–465.

[^steadman-1991]: Steadman, Mark, 1991, “Type Raising and Directionality in Combinatory Grammar”, Technical Report MS-CIS-91-11, University of Pennsylvania Department of Computer and Information Science .
