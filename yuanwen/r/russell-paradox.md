# Russell’s Paradox
**First published Fri Dec 8, 1995; substantive revision Fri Mar 13, 2026**

*Deutsch, Harry, Marshall, Oliver, Irvine, Andrew David*

Russell’s paradox is a contradiction—a logical impossibility—of concern to the foundations of set theory and logical reasoning generally. It was discovered by Bertrand Russell in or around 1901. In a letter to Gottlob Frege, Russell outlined the problem as it affects Frege’s major work *Grundgesetze der Arithmetik*. Frege responded with both dismay and admiration, and never recovered from the blow dealt to his life’s work. Russell was also alarmed by the extent to which the paradox threatened his own project. Struggling to solve the paradox during a period of intensive work and emotional upheaval, he made some of his most important discoveries including his theory of denoting phrases and definite descriptions, and his theory of types. Since then, the paradox has prompted major advances in logic, set theory and the philosophy and foundations of mathematics. Although Russell is justly famous for his type-theoretic solution, it is less well known that he wrestled for several years with other candidate solutions. The paradox also inspired fruitful proposals from great mathematicians such as David Hilbert, Ernst Zermelo, and John von Neumann. It continues to inspire work in logic and foundations to this day. In his introductory note to Russell’s letter published more than fifty years ago, Jean van Heijenoort wrote that “Russell’s paradox has been leaven in modern logic and countless works have dealt with it.” The leavening effect of Russell’s Paradox has not diminished.

## 1. The Paradox

Central to any theory of sets is a statement of the conditions under which sets are formed. In addition to simply listing the members of a set, it was initially assumed that any well-defined condition (or precisely specified property) could be used to determine a set. For example, if $T$ is the property of being a teacup, then the set, $S$, of all teacups might be defined as $S = \{x: T(x)\}$, the set of all individuals, $x$, such that $x$ has the property of being $T$. Even a contradictory property might be used to determine a set. For example, the property of being both $T$ and not-$T$ would determine the empty set, the set having no members.

More precisely, naïve set theory assumes the so-called naïve or unrestricted comprehension principle that for any formula $\phi(x)$ containing $x$ as a free variable, there will exist the set $\{x: \phi(x)\}$ whose members are exactly those objects that satisfy $\phi(x)$. Thus, if the formula $\phi(x)$ stands for “$x$ is prime”, then $\{x: \phi(x)\}$ will be the set of prime numbers. If $\phi(x)$ stands for “${\sim}(x = x)$”, then $\{x: \phi(x)\}$ will be the empty set.

But from the assumption of this principle, Russell’s contradiction follows. Let $\phi(x)$ stand for $x \in x$ and let $R = \{x: {\sim}\phi(x)\}$. Then $R$ is the set whose members are exactly those objects that are not members of themselves.

Is $R$ a member of itself? If it is, then it must satisfy the condition of not being a member of itself and so it is not. If it is not, then it must not satisfy the condition of not being a member of itself, and so it must be a member of itself. This is a contradiction, one that is a problem even for systems of logic weaker than the classical system.

Although the reasoning leading to the paradox applies to set theory, it does not actually require any principle of set theory. Suppose that $y$ is such that for all $x$, $x\in y \equiv x \notin x$. Then take the case where $x=y$ to get $y\in y \equiv y\notin y$. In fact, the reasoning is entirely general and does not even require that the relation in question is $\in$. This is already suggested by the example of the village barber who shaves all and only villagers who don’t shave themselves, which later associated with Russell's paradox. (This is emphasized in both Levy 1979 and Kripke 2014.)[^kripke-2014][^levy-1979] The reasoning is an applied instance of the following theorem of pure logic, labelled T269 in Kalish, Montague, and Mar 2000:

$$\tag{T269} {\sim}\exists y\forall x(Fxy\equiv{\sim}Fxx)$$

We return to this generalization in section 5.

Some related paradoxes are discussed in the second chapter of the Introduction to Whitehead and Russell (1910, 2nd edition, 60–65), as well as in the entry on paradoxes and contemporary logic in this encyclopedia. A few of these are discussed later in this entry.

## 2. History of the Paradox

### 2.1 Anticipations of the Paradox and Related History

Russell discovered the paradox during a period when similar antinomies were being discovered. In 1897, Cesare Burali-Forti, an assistant to Giuseppe Peano, noticed that since the set of ordinals is well-ordered, it too must have an ordinal. However, this ordinal must be both an element of the set of all ordinals and yet greater than every such element. (In fact, Burali-Forti did not recognize this argument as a paradox but instead, due to a misunderstanding of Cantor’s concept of a well-ordering, as a proof by reductio ad absurdum that the trichotomy law failed for the ordinals. Cantor too knew of this reasoning and communicated it to Dedekind in a now famous letter (Cantor 1889) but also did not consider it to be a paradox but, rather, to be a proof that the collection of all ordinals was “too large” to be a set. For details, see Moore and Garciadiego 1981, Menzel 1984, Purkert 1989, and section 3 of the entry on the early development of set theory.)

Further, Cantor had proved in 1882 that there is no greatest cardinal number (Cantor 1883)[^cantor-1883], which Russell found “paradoxical” since he believed that there is a universal set containing everything and, hence, that this set must have the greatest cardinal number. Unlike there paradoxes, however, Russell’s paradox does not involve either ordinals or cardinals, relying instead only on much more primitive notions.

Zermelo noticed a similar contradiction sometime between 1897 and 1902, possibly anticipating Russell by some years (Ebbinghaus and Peckhaus 2007, 43–48; Tappenden 2013, 336)[^ebbinghaus-2007][^tappenden-2013], although Kanamori concludes that the discovery could easily have been as late as 1902 (Kanamori 2009, 411)[^kanamori-2009]. As Linsky points out, Zermelo’s argument, while similar to Russell’s, is best understood as one of a cluster of arguments by Zermelo, Schröder and Cantor that “indeed anticipated” the mathematical argument Russell developed but that turned out to be different in small but significant ways from Russell’s argument (Linsky 2013, 11)[^linsky-2013].

Russell appears to have made his discovery in the late spring of 1901, while studying Cantor’s argument and working on his *Principles of Mathematics* (1903a). Exactly when the discovery took place is not clear. Russell claims that he came across his paradox “in June 1901” (1944, 13). Later he reports that the discovery took place “in the spring of 1901” (1959, 75). Still later he reports that he came across the paradox, not in June, but in May of that year (1969, 221). For more details see Grattan-Guinness 1978, Coffa 1979, and Lavine 1994. Further primary sources for Russell’s work in the period 1900–1902 are collected in Moore 1994.

### 2.2 Cantor’s Method of Diagonalization

Russell discovered his paradox by examining Cantor’s proof that there is no largest cardinal number. The proof relies on a neat trick known as “diagonalization” that was reinvented for a novel purpose by Cantor himself. The essence of this method was also described by Russell with typical foresight in (Russell 1903a, section 102)[^russell-1903a], which can be compared with (Shoenfield 1967, p. 131)[^shoenfield-1967]. Here we discuss the method in general terms. Then, in the next section and [the supplement](russell-paradox.supplement.md), we turn to some of the details of Russell’s struggle with diagonalization.

A common form of diagonalization involves an *enumeration* —a list of elements such as formulas, sets, or functions in which every element is associated with some natural number— in which an element’s place in the enumeration is exploited to define a diagonal construction. For example, assuming an enumeration of one-place functions of natural numbers, $f_1, f_2, f_3, \ldots$, it can be shown that the enumeration cannot be exhaustive: There must be a one-place function not in the enumeration. Define $g(n)$ to be $f_n(n)+1$. Then $g$ cannot be in the enumeration, say, at the $q$th place, since then $g(q)=g(q)+1$, a contradiction. Variations of this method are used throughout set theory and metamathematics.

It’s easy to see why the method is called “diagonalization.” List the functions $f$ as follows:

$$\begin{array}{cccccc} F_0: & \boldsymbol{f_0(0)}, & f_0(1) & f_0(2), & f_0(3), & \ldots\\ F_1: & f_1(0), & \boldsymbol{f_1(1)} & f_1(2), & f_1(3), & \ldots\\ F_2: & f_2(0), & f_2(1) & \boldsymbol{f_2(2)}, & f_2(3), & \ldots\\ F_3: & f_3(0), & f_3(1) & f_3(2), & \boldsymbol{f_3(3)}, & \ldots\\ & & \vdots & & & \\ \end{array}$$

The function $g(n) = f_n (n) + 1$ is defined by raising the value of $f_n$ along the bolded left-to-right diagonal by one. So $g(n)$ differs from any $f_n$ at $f_n (n)$ and so cannot be in the list $F_0, F_1, F_2$.... Cantor used this method to prove that there are more real numbers than natural numbers, although both kinds of numbers are infinite in extent. Cantor’s method set off a firestorm of activity in set theory and metamathematics; and a more general kind of diagonal reasoning—perhaps not involving an enumeration—led Russell to his paradox as we will soon see.

A very basic principle involving diagonalization is the following:

**Cantor’s Lemma (CL)**

Let $f$ be a function with domain $X$ and range $Y$. Then, on pain of contradiction, the diagonal set $D_f =$ $\{x \in X: x \not\in f(x)\}$ $\not\in Y$. *Proof.* Suppose $D_f \in Y$. Then, since $Y$ is the range of $f$, there is (by the definition of ‘range’) a $z \in X$ such that $f(z) = D_f$. But then, since $D_f =$ $\{x \in X: x \not\in f(x)\}$, and $z$ is an $x \in X, z \in D_f \equiv z \not\in D_f$.

Now consider the case in which $X = Y$. Let $f$ be the identity mapping $I$, where $I(x) = x$. The set defined by diagonalization in this case is $R_X = D_f = \{x \in X: x\not\in x\}$. (CL) implies that $R_X \not\in Y$, and since $X = Y$, $R\not\in X$. Thus, for any set $X$, $R_X$is never an element of $X$. It follows that there cannot be a universal set. However, Russell was convinced that there must be a universal set, $V$. His conclusion was, in effect, that $R_V$, which is just $R$, does not exist. If it did, it would be both a member and a non-member of itself. This is a consistent position, but modern ZF set theory has an axiom —the axiom of foundation, or regularity— that implies that no set is a member of itself and hence that $V$ and $R_V$ coincide and so neither is a set.

It is a corollary of (CL) that there is no onto function with domain $X$ and range the *power set* of $X$ (the set of all subsets of $X)$. This is a form of Cantor’s Theorem. If such a function existed, then it would have $D_f$ in its range (since $D_f$ is a subset of $X)$. By (CL), this is impossible. However, there is a one-to-one correspondence between $X$ and a subset of the power set of $X$ – namely the family of all singletons of elements of $X$. This correspondence is a function into the power set of $X$. Since there is a function with domain $X$ into the power set of $X$, but no function with domain $X$ onto the powerset of $X$, the cardinal size of $X$ is *strictly smaller* than that of the powerset of $X$. This is the result that is more usually called Cantor’s theorem.

### 2.3 Russell’s Discovery

As Russell tells us in his (1919), it was after he applied the same kind of reasoning found in Cantor’s diagonal argument to a “supposed class of all imaginable objects” that he was led to the contradiction. Griffin (2004)[^griffin-2004] is a scholary account of Russell’s discovery. What follows is a reconstruction of his reasoning that continues to show the logical connection between his paradox and diagonalization. How might he have discovered that the relation defined by diagonalization is $R$?

The comprehensive or universal set $V$ that Russell was considering contains everything, including itself, as an element. (Strictly speaking, Russell’s theory concerned *classes* rather than sets, but this distinction can be ignored for a moment.) Since $V$ contains everything as an element, and since subsets are things, $V$ should contain all its subsets as elements (Russell 1901, p. 69). For this reason, Russell seems to have thought that it was possible to map every subset of $V$ to an element of $V$. This would be achieved by mapping every subset of $V$ to itself. To do this in a general way that also takes account of the elements of $V$ that are not sets, he considered the following many-to-one mapping: $f(x) = x$ if $x$ is a set, $f(x) =$ the singleton of $x$ if $x$ is not a set (Russell 1903a, §349)[^russell-1903a]. (The mapping is many-to-one because both $x$ and the singleton of $x$ are mapped to the singleton of $x$.) To simplify things, focus on the clause that $f(x) = x$ if $x$ is a set. Let $f$ be the identity mapping $I$, where $I(x) = x$, whose domain is the subset $V^*$ (of $V)$ that contains all and only sets, and whose codomain is the powerset of $V^*$. For every $y$ in the codomain, there is an $x$ in the domain such that $f(x) = y$. So the codomain is the range of $f$. So, by definition of ‘onto’, $f$ is a function from domain $V^*$ onto the powerset of $V^*$. This contradicts Cantor’s theorem. Let us focus, then, on what must be omitted from the mapping: the diagonal set $D_f$, which (CL) tells us is not in the range of $f$.

Recall from 2.2 that the diagonal set $D_f$ is $\{x \in X: x \not\in f(x)\}$. In English, this is the set of all sets that are not members of the sets to which they are mapped by $f$. Since $f$ maps every set to itself, $D_f$ is the set of all sets that are not members of themselves. More precisely,

$$\forall x \in V^* (x \in f(x) \equiv x \not\in D_f)$$

implies:

$$\forall x (x \in x \equiv x \not\in D_f),$$

since those sets not in $D_f$ are members of the sets —themselves— to which they are mapped by $f$. Hence

$$\forall x (x \not\in x \equiv x \in D_f).$$

This because $f$ maps every set to itself, so $D_f$ is the set of all sets that are not members of themselves. That is,

$$D_f = \{x: x \not\in x\}.$$

By the reasoning in section 1, this implies Russell’s paradox: $D_f \in D_f \equiv D_f \not\in D_f$. Since Russell remained convinced that $V$ exists, he sought a principled way of ruling out functions that allow this diagonal argument to get started. This is discussed in 3. Then, in 4, the modern reaction to the argument is considered: that $V$ does not exist.

Returning to the history of the paradox, it is worth noting that the cluster of arguments due to Russell, Zermelo and Schröder were thought to be of minor importance by everyone other than Russell until it was realized how detrimental they were to Gottlob Frege’s foundations for arithmetic.

### 2.4 Russell’s letter to Frege

Russell wrote to Frege with news of the paradox on June 16, 1902. (For the relevant correspondence, see Russell 1902 and Frege 1902, in van Heijenoort 1967.)[^frege-1902][^russell-1902][^russell-1967][^heijenoort-1967] After he had expressed his great admiration for Frege’s work, Russell broke the devastating news, gently:

> Let $w$ be the predicate of being a predicate that cannot be predicated of itself. Can $w$ be predicated of itself? From either answer follows its contradictory. We must therefore conclude that $w$ is not a predicate. Likewise, there is no class (as a whole) of those classes which, as wholes, are not members of themselves. From this I conclude that under certain circumstances a definable set does not form a whole. (1902, p. 125)

Russell’s letter arrived just as the second volume of Frege’s *Grundgesetze der Arithmetik* (*The Basic Laws of Arithmetic*, 1893, 1903) was in press. Frege’s letter in response contained a solution to the predicational version of the paradox described in Russell’s letter (see Landini 1993, Klement 2010a)[^klement-2010a][^landini-1993]. Immediately appreciating the difficulty that the paradox posed for classes, Frege added to the *Grundgesetze* a hastily composed appendix discussing Russell’s discovery (more of which in section 3). In the appendix Frege observes that the consequences of Russell’s paradox are not immediately clear. For example:

> Is it always permissible to speak of the extension of a concept, of a class? And if not, how do we recognize the exceptional cases? Can we always infer from the extension of one concept’s coinciding with that of a second, that every object which falls under the first concept also falls under the second? These are the questions raised by Mr Russell’s communication (1903, 127).

We will now discuss the first and third questions, before turning to the second question in section 3.

### 2.5 The Paradox in Frege’s System

Consider the first question raised by Frege. As Frege uses it in the quote above, “class” denotes an extension of a concept, something rather like what Russell above calls “a class as whole” and what we today call a “set.” Further, a concept or function to truth values is what in Frege’s system corresponds to a property. Thus the concept of having mammary glands distinguishes the class of mammals from reptiles, birds and other living organisms. In that case, it is permissible to speak of the class of mammals. The concept of being both square and not square (or any other conjunction of contradictory concepts) distinguishes the empty class, and so on. The intuition that it is, in Frege’s words, “always permissible to speak of the extension of a concept, of a class” (1903, 127) can be codified in a naïve or unrestricted comprehension principle saying that every concept may be used to determine a corresponding class:

> For every concept $f$, there exists a class $C_f$ such that for all objects $x$, $x$ is a member of $C_f$ if and only if $x$ falls under $f$.

Note, however, that Frege does not adopt such a principle as an axiom (or “basic law”). Rather, as is explained below, it is a consequence of his basic law V.

Exactly how naïve comprehension is stated depends on the theory in question. In theories based on a first order formal language, and using the set-theoretic $\in$ rather than Frege’s own notion of membership, the principle states that

$$\tag{NC}\exists y \forall x [x \in y \equiv \phi(x)],$$

(Note that ‘$y$’ is not free in the formula ‘*φ*’, for if it were then $\phi(x)$ could be $x \not\in y$, and so $x \in y \equiv x \not\in y$.) (NC) says, “There is a set $y$ such that for any object $x, x$ is an element of $y$ if and only if the condition expressed by *φ* holds.” Where ‘*φ*’ is the well-formed formula ‘$x \not\in$ *x’*, and $y$ is the corresponding set, this implies Russell’s Paradox. Hence Russell’s diagnosis in his letter to Frege (quoted above): “under certain circumstances a definable set does not form a whole.”

Frege’s own notion of membership is that $x \in y$ if and only if $y$ is the extension of a concept under which $x$ falls. Writing ‘$\varepsilon f$’ for the extension of a concept $f$:

$$x \in y \equiv_{df} \exists f [y = \varepsilon f \wedge f(x)].$$

Using this, it is possible to derive the principle corresponding to (NC) in Frege’s system:

$$\tag{NCF}\forall f \exists y \forall x[x \in y \equiv f(x)].$$

First, however, recall Frege’s third question. Frege is committed to (NCF) by his basic law V about the identity of ranges of values. As he wrote in response to Russell’s letter, after expressing his shock and dismay:

> It seems accordingly that the transformation of the generality of an identity into an identity of ranges of values (sect. 9 of my *Basic Laws*) is not always permissible, that my law V (sect. 20, p. 36) is false, and that my explanations in sect. 31 do not suffice to secure a meaning for my combinations of signs in all cases. (1902, 127)

This requires some explanation. For Frege, concepts or functions are incomplete entities in need of an argument or object to complete them. Thus, he identifies concepts not in isolation but based on how they behave when completed by all their arguments i.e., based on whether they agree on or have the same value for every argument. If they do agree, then they are the same, which justifies writing ‘$\forall x[f(x) = g(x)$]’. (Note that where it is now customary to write ‘$\equiv$’ for material equivalence Frege writes ‘=’, because when given arguments the expressions standing for concepts denote truth values. From now on, we will comport with modern practice and write ‘$\equiv$’.) This is what Frege calls “the generality of an identity” between concepts. Further, according to Frege, objects are unlike concepts in being complete (or self-standing); hence concepts are not objects. However, Frege introduces objects corresponding to concepts by the familiar mathematical method of transforming entities that have something in common —standing in an equivalence relation— into the thing they have in common. In this case, the entities are concepts. What they have in common is that they have the same value for every argument – “the generality of an identity.” This is the equivalence relation in question. The object abstracted from this equivalence relation is called the “range of values” of a concept, also called “the graph of a function” – the set of pairs of arguments and values corresponding to the concept. The special case in which a range of values corresponds to a concept —or function to one of the truth values— is called an “extension.” (For the rest of this section, this is our preferred terminology.) Frege’s law V states that the extension of a concept $f(~)$ is identical to the extension of a concept $g(~)$ if and only if $f(~)$ and $g(~)$ agree on their values for every argument, i.e., if and only if $\forall x[f(x) \equiv g(x)$]. Thus “the transformation of the generality of an identity into an identity of ranges of values”. Hence law V:

$$\tag{V} \varepsilon f = \varepsilon g \equiv \forall x[f(x) \equiv g(x)].$$

This implies (NCF). First fix $f$ and let $y = \varepsilon f$. To prove the left-to-right direction of (NCF), assume $x \in y$. Then, by the definition of ‘$\in$’,

$$\exists g [y = \varepsilon g \wedge g(x)].$$

So,

$$\varepsilon f = \varepsilon g.$$

Hence, by (V),

$$\forall x[f(x) \equiv g(x)].$$

Further, we have $g(x)$, so $f(x)$ as required.

To prove the right-to-left direction of (NCF), assume $f(x)$. Because $y = \varepsilon f$, Frege’s definition is satisfied, and so $x \in y$ as required.

Note also that (NCF) implies (V). Assuming that $\varepsilon f = \varepsilon g$,

$$\forall x[x \in \varepsilon f \equiv x \in \varepsilon g].$$

But by (NCF),

$$\forall x[x \in \varepsilon f\equiv f(x)],$$

and

$$\forall x[x \in \varepsilon g \equiv g(x)].$$

So,

$$\forall x[f(x) \equiv g(x)].$$

(NCF) should not be confused with the purely first order condition we have labelled (NC). T. Parsons (1987)[^parsons-1987] proved that the first order version of (V) is consistent – it has a model in the natural numbers. But of course (NC) is inconsistent. So, in the first order context, (V), now treated as a first order schema, does not imply (NC).

As Frege points out in his letter to Russell, the thing corresponding to $R$ in Frege’s system is: *is a concept whose extension doesn’t fall under it*. This is described by the following formula of second order logic:

$$\tag{RF} \exists f [x = \varepsilon f \wedge{\sim} f(x)].$$

Recalling the proof of (NCF), abbreviate the formula labeled $(RF)$ by the formula ‘$Rx$’ and substitute this “Russell concept” for $f(x)$ in (NCF). Then it follows in Frege’s system that the extension of the concept $R(~)$ falls under $R(~)$ if and only if it does not: $R(\varepsilon R) \equiv{\sim} R(\varepsilon R)$. Consider the extension of $R, \varepsilon R$. If $R(\varepsilon R)$ is true, then, by definition, there is a concept $f$ such that $\varepsilon R$ is the extension of $f$ and $f(\varepsilon R)$ is false. So, by law V, $R(\varepsilon R)$ is false as well, because $\varepsilon R$ is also the extension of $f$ and $\forall x[f(x) \equiv R(x)$]. Therefore, if $R(\varepsilon R)$ is true, then $R(\varepsilon R)$ is false. So $R(\varepsilon R)$ is false. Then there is a concept $f$ such that $\varepsilon R$ is the extension of $f$ and $f(\varepsilon R)$ is false. So, by definition, $R(\varepsilon R)$ is true. This contradicts the claim that $R(\varepsilon R)$ is false.

(See 2.3–2.5 of the entry on Frege’s Theorem for more details. See also section 2.4.1 of the entry on Gottlob Frege, and the papers in section II of Boolos 1998.)[^boolos-1998]

Because of these problems, Frege eventually felt forced to abandon many of his views about logic and mathematics. Even so, as Russell points out, Frege met the news of the paradox with remarkable fortitude:

As I think about acts of integrity and grace, I realise that there is nothing in my knowledge to compare with Frege’s dedication to truth. His entire life’s work was on the verge of completion, much of his work had been ignored to the benefit of men infinitely less capable, his second volume was about to be published, and upon finding that his fundamental assumption was in error, he responded with intellectual pleasure clearly submerging any feelings of personal disappointment. It was almost superhuman and a telling indication of that of which men are capable if their dedication is to creative work and knowledge instead of cruder efforts to dominate and be known. (Quoted in van Heijenoort 1967, 127.)[^heijenoort-1967]

Of course, Russell too was concerned about the consequences of the contradiction. Upon learning that Frege agreed with him about the significance of the result, he immediately began writing an appendix for his own soon-to-be-released *Principles of Mathematics*. Entitled “Appendix B: The Doctrine of Types,” the appendix represents Russell’s first attempt at providing a principled method for avoiding what soon was to become known as “Russell’s paradox.” We return to this below.

## 3. Early Responses to the Paradox

### 3.1 Cantor

One early skeptic concerning (NC) was the originator of modern set theory, Georg Cantor. Even prior to Russell’s discovery, Cantor had rejected (NC) in favor of what was, in effect, a distinction between sets and classes, recognizing that some properties (such as the property of being an ordinal) produced collections that were simply too large to be sets. Thus, he thought that the entities that are today called sets should be restricted (Cantor 1899)[^cantor-1899]. Various ways of implementing this line of response are discussed below. (Details can be found in Moore 1982, Hallett 1984, and Menzel 1984.)[^hallett-1984][^menzel-1984][^moore-1982] For the moment, note that Frege and Russell were responding to a paradox that afflicts their notion of an extension or class as defined by (NC); it is not clear that there was an analogous crisis for set theory as Cantor understood it. Rather, as Hilbert would insist, what Cantor’s theory needed was a precise axiomatization (Hilbert 1904)[^hilbert-1904].

### 3.2 Frege

Recall Frege’s second question quoted above, How to recognize the exceptions to (NCF)? Because (NCF) follows from (V) in Frege’s system, isolating the exceptions to the former requires isolating the exceptions to the latter. His basic idea is that when considering whether $\varepsilon f = \varepsilon g$, one must *not* consider whether these extensions contain themselves; only then may one identify them when the corresponding concepts or functions agree on every (other) argument. While the proposal was ultimately unsuccessful, Frege’s strategy of isolating the problematic instances and excluding them by restricting (V) is of historical interest, because of the influence it appears to have had on Russell. For this reason, Frege’s strategy and Russell’s related proposals are discussed in the [supplement on Frege’s Way Out](russell-paradox.supplement.md).

### 3.3 Russell

Russell worked (with A. N. Whitehead) on various candidate solutions to the paradox between 1902 and 1905. Early on, he toyed with an idea like Cantor’s that some properties produced collections that are not legitimate sets. This is reflected in Russell’s distinction between a class as one and a class as many, where the size of the former needs to be restricted (1903a, 60, 102–3). Russell would later return to theories that limit the sizes of legitimate sets and complain that such theories do not decide how big, or how high up in order, is too big, or too high, to form a set. In particular, he complains that such theories do not decide which ordinals are legitimate (Russell 1907, 44)[^russell-1907]. Since this complaint began to be addressed, subsequently, by axiomatizations beginning with that in Zermelo 1908, and since some such axiomatizations can be justified by a coherent basic conception of the sort discussed in Shoenfield 1967 and Boolos 1971, we put the complaint to one side.

Although Russell first introduced his theory of types in Appendix B of his 1903 *Principles of Mathematics*, he recognized immediately that more work needed to be done, since his initial account seemed to resolve some but not all of the paradoxes. For example, the initial account is subject to Russell’s paradox of propositions. This is discussed later.

In a letter to Frege in May 1903, Russell suggests that “classes are entirely superfluous… this seems to me to avoid the contradiction” (Russell 1903b)[^russell-1903b]. Russell means that there is no need for his theory to make reference to classes in any sense of that term – no need for reference to extensions, or sets, or Fregean functions. Because of this feature, Russell calls it a “no-classes theory.” However, this does not address the fact that Frege’s (NCF) can also be obtained from (V). Moreover, Russell’s suggestion still faces the question of what to do about the predicational version of Russell’s paradox that he stated without reference to classes or extensions in the original letter to Frege.

Here the reader should recall from section 2 the account of how to define relations and functions via diagonalization. Russell’s answer was to try various principled ways of restricting his definitions to rule out diagonalization. See Russell 1994b, Landini 1992, and Urquhart 1994, xxi–xxii. Much of his work in 1904 is on ruling out the relevant propositional functions using the restrictions of the so-called zigzag theory (Urquhart 1994, xxvi)[^urquhart-1994]. The theory is so-called because given a propositional function *φ* that purports to determine a class $u$, diagonalization exploits “a certain zigzag quality,” that $x \not\in u$ when $\phi x$ or $x \in u$ when ${\sim}\phi x$ (Russell 1907, 38)[^russell-1907]. This particular strategy shows the influence of Frege and is discussed along with Frege’s “way out” in the aforementioned [supplement on Frege’s Way Out](russell-paradox.supplement.md).

Russell’s revisionary ideas about denoting and propositions were developed around 1904–5 while he worked on the zigzag theory. The paper in which this theory was summarized was submitted in November 1905, mere months after “On Denoting” was submitted in August after completion in late July 1905. See Urquhart’s introduction to Russell 1905 (p. 414). Indeed, the first recorded evidence of Russell’s view that

> a complex is denoting or un-denoting, not in its own nature, but according to its position in another complex, i.e., a proposition (Russell 1904a, 126)[^russell-1904a]

occurs in his notes on zigzag theories.

Concerning the implications of the new theory of denoting for the paradox, there were many false starts. Russell wrote (with his characteristic wit and understatement) to his wife on April 14ᵗʰ 1904:

> Alfred [Whitehead] and I had a happy hour yesterday, when we thought the present King of France had solved the Contradiction; but it turned out finally that the royal intellect was not quite up to that standard (quoted by Urquhart in (Urquhart 1994, xxxiii)[^urquhart-1994]).

This brings us to the relevant aspects of Russell’s theory of denoting phrases and definite descriptions (see Section 4 of the entry on Bertrand Russell), which plays a role in all his proposed solutions to the paradox from 1904 onward.

Definite descriptions (like ‘the smallest prime number’) are of fundamental importance to mathematics, in which one often speaks of the unique entity satisfying a given condition (or two such conditions in the case of equations). Russell’s theory is that definite descriptions, like denoting phrases in general, have no meaning in isolation —in the way that, say, the proper name ‘Walter Scott’ does— but only in the context of larger expressions in which they occur. This reflects the influence of Russell’s mathematical education, which included the 19th century method for eliminating apparent reference to infinitesimal quantities by giving meaning not to phrases that purport to denote them but to the larger expressions in which these occur. In the case of definite descriptions, like the one occurring in

The present King of France is bald,

Russell’s analysis of them as complex quantifier phrases raises the question of whether or not the purportedly denoted entity exists. In the case of phrases that purport to denote classes, his analysis shows that there is simply no reason to say that classes exist. Rather, the analysis reveals that what are said to exist are propositional functions. For example, the following statement that purports to be about the class of $G$s,

$\{x: Gx\}$ is abstract,

is analyzed as something that can be rendered informally as:

There is a *φ* such that for all $x~Gx$ if and only if $\phi x \amp \phi$ is abstract,

where *φ* is a variable for propositional functions. (See Russell 1910, 72, 188. For a formalization of this analysis in modern notation, see section 9 of the entry on the notation of *Principia Mathematica*. For further discussion of Russell’s theory of denoting phrases and its role in the elimination of classes and other paradoxical entities, see Urquhart 1994, Kaplan 2005, and Klement 2010a,b.) Of course, eliminating classes does not address the predicational version of Russell’s paradox. What is required, then, is a principle governing propositional functions that can block the paradox. Eventually, Russell would settle on the *vicious circle principle*, to which we return below. First, however, he considered another kind of no-classes theory – the aforementioned substitutional theory (Russell 1906, 1907)[^russell-1906][^russell-1907].

The substitutional theory is officially debuted as the preferred version of the no-classes theory in (Russell 1907)[^russell-1907]. In a note added to this paper on February 5ᵗʰ 1906, Russell records that he “now feel[s] hardly any doubt that the no-classes theory affords the complete solution of all the difficulties stated” (Russell 1907)[^russell-1907]. (This attitude may seem alien to the modern reader familiar with model theory, which assumes some set theory thus giving the latter a logically primary status. But this was not the attitude of the time.) Russell’s published description of the substitutional theory is extremely sketchy. Further, while a solution to Russell’s paradox can be gleaned from the theory, it does not rule out diagonalization entirely and so faces a paradox of its own. However, the theory played a large role in Russell’s thinking and influenced his subsequent work on type theory, so aspiring Russell scholars should know something about it. The substitutional theory and its problems are discussed in more detail in the [supplement on Frege’s Way Out](russell-paradox.supplement.md). See also Landini 1998, 2004, 2011, Grattan-Guiness 1974, Urquhart 1986, Urquhart and Pelham 1995, Klement 2010a, and Galaugher 2013.

The substitutional theory led to type theory’s more mature expression five years later in Russell’s 1908 article, “Mathematical Logic as Based on the Theory of Types,” and in the monumental work he co-authored with Alfred North Whitehead, *Principia Mathematica* (1910, 1912, 1913). Russell’s type theory thus appears in two versions: the “simple theory” of 1903 and the “ramified theory” of 1908. Both versions have been criticized for being too ad hoc to eliminate the paradox successfully. For a passionate defense of a version of simple type theory against this charge, see (Andrews 1986)[^andrews-1986].

Russell’s basic idea is to avoid commitment to $R$ (the set of all sets that are not members of themselves) by arranging all sentences (or, more precisely, all propositional functions, functions which give propositions as their values) into a hierarchy. It is then possible to refer to all objects for which a given condition (or predicate) holds only if they are all at the same level or of the same “type.”

The resulting solution to Russell’s paradox is motivated in large part by adoption of a principle that he viewed as a constraint on logically possible theories of propositional functions: the so-called *vicious circle principle*. The principle in effect states that no propositional function can be defined prior to specifying exactly those objects to which the function applies – the function’s domain. For example, before defining “$x$ is a prime number,” one first needs to define the collection of objects that might satisfy it, namely the set $N$ of natural numbers. As Whitehead and Russell explain,

> An analysis of the paradoxes to be avoided shows that they all result from a kind of vicious circle. The vicious circles in question arise from supposing that a collection of objects may contain members which can only be defined by means of the collection as a whole. Thus, for example, the collection of *propositions* will be supposed to contain a proposition stating that “all propositions are either true or false.” It would seem, however, that such a statement could not be legitimate unless “all propositions” referred to some already definite collection, which it cannot do if new propositions are created by statements about “all propositions.” We shall, therefore, have to say that statements about “all propositions” are meaningless. … The principle which enables us to avoid illegitimate totalities may be stated as follows: “Whatever involves *all* of a collection must not be one of the collection”; or, conversely: “If, provided a certain collection had a total, it would have members only definable in terms of that total, then the said collection has no total.” We shall call this the “vicious-circle principle,” because it enables us to avoid the vicious circles involved in the assumption of illegitimate totalities. (1910 [2nd edn], 37)

If Whitehead and Russell are right, it follows that no function’s domain includes any object presupposing the function itself. As regards Russell’s paradox, since classes or extensions presuppose the functions that define them, no function’s domain includes any class or extension that presupposes that function. This blocks the construction of $R$ by diagonalization. It will be recalled, however, that the theory of *Principia Mathematica* is another version of the no-classes theory, according to which classes are entirely superfluous. A more important result of the vicious circle principle is, then, that propositional functions are arranged in a hierarchy of the kind Russell proposes. This suffices to restrict Frege’s

$$ \tag{NCF} \forall f \exists y \forall x[x \in y \equiv f(x)],$$

based on the demand that no functions or relations of the level of $f$ or higher fall under $f(~)$.

As Gödel pointed out (in his 1944), Russell’s type restriction is not well motivated in cases describing propositional functions, or sets (like $N)$, that are mind and language independent. As Quine put it, memorably, such descriptions are

> not visibly more vicious than singling out an individual as the most typical Yale man on the basis of averages of Yale scores including his own (1967, 243).

Note however that in the 1908 article, Russell reaches the conclusion that his restriction should be dropped in the case of extensional mathematics and *only applied when characterizing intensional entities such as propositional functions* (1908, 243). The attitude taken in *Principia* is similar. This attitude is endorsed in (Church 1978)[^church-1978], (Myhill 1979)[^myhill-1979] and (Kripke 2011)[^kripke-2011].

### 3.4 Hilbert

In response to Russell’s paradox, David Hilbert also expanded his program of building a consistent, axiomatic foundation for mathematics that included an axiomatic foundation for quantificational logic and set theory (Peckhaus 2004)[^peckhaus-2004]. Underlying this approach was the idea of allowing the use of only finite, well-defined and intuitively constructible objects, together with rules of inference deemed to be absolutely certain. A foundation based on this idea, Hilbert thought, would be sufficiently definite and certain to ensure that paradoxes could not arise.

Hilbert credited Cantor with seeing that some classes were simply too large to be sets and that any assumption to the contrary would lead to inconsistency. Hilbert’s demand was that Cantor’s set theory be given an axiomatic foundation (Hilbert 1904, p. 131)[^hilbert-1904]. This is worth emphasizing because it was glossed over in a much more famous paper, where Hilbert did not clearly distinguish Cantor’s work from that of Frege (Hilbert 1925, p. 375)[^hilbert-1925]. Hilbert may also have underestimated the extent to which axiomatic set theory can be justified by a coherent basic conception of the sort discussed in Shoenfield 1967 and Boolos 1971.

### 3.5 The Constructivists

Two more major figures who are worth mentioning introduced versions of *constructivism*, the basic idea of which was that one cannot assert the existence of a mathematical object unless one can define a procedure for constructing it.

Henri Poincaré read Russell’s work and in his (1910) advocated a version of the vicious circle principle, which is presented not so much in response to Russell’s paradox as to Richard’s. Elsewhere (1909), Poincaré claims that Zermelo’s axiom of separation does not guarantee safety from paradox, because it does not require one to define a procedure for constructing a set prior to asserting its existence:

> Zermelo has no qualms about talking about all the objects that are part of a certain Menge, a Menge which also satisfies a certain condition […] By laying down his Menge M in advance, he has raised a wall of enclosure that stops any troublemakers who might come from outside. But he does not ask himself whether there might not be troublemakers from within (1909, 477).

For Poincaré, asserting the existence of an object cannot be justified by intuition, which allows us to *follow rules* rather than to *represent objects* such as sets. If the existence of a set is to be asserted based on a legitimate use of intuition, then it must be accompanied by a rule of construction. In the absence of such a rule, there is always the danger that intuition will lead to paradox.

Finally, Luitzen Brouwer developed a more permissive form of constructivism, *intuitionism*. Brouwer differed from Poincaré about intuition of objects, which Brouwer accepted as legitimate so long as the object’s existence is not simply posited to fill a “gap” but is supported by a procedure for constructing it that meets certain conditions. The demand for such a procedure underlied his opposition to higher number classes and was partly a response to the classical infinitary perspective assumed by the existence axioms of set theory and by the set-theoretic definition of the continuum. However, Brouwer’s dissertation (1907) also contains a critique of Cantorian set theory and a specific criticism of comprehension. Some of this is summarized in his Inaugural Lecture (1912), which also addresses comprehension and the axiom of separation (which he calls “the axiom of inclusion”). A theme of the lecture is that set theoretic axioms extrapolate without adequate justification from the finite to the infinite. As in the case of Poincaré, these criticisms are presented not so much in response to Russell’s paradox as to those of Richard and Burali-Forti. Note also that the derivation of Russell’s paradox does not depend upon an instance of the principle of Excluded Middle, that either $R$ is a member of $R$ or it is not. This is discussed in section 4.

## 4. Russell’s Paradox in Contemporary Logic

Russell’s paradox is often seen as a negative development – as bringing down Frege’s *Grundgesetze* and as one of the original conceptual sins leading to our expulsion from Cantor’s paradise (Hilbert 1925)[^hilbert-1925]. W.V. Quine describes the paradox as an “antinomy” that “packs a surprise that can be accommodated by nothing less than a repudiation of our conceptual heritage” (1966, 11). Quine is referring to the principle (NC) mentioned earlier. Despite Quine’s comment, it is possible to see Russell’s paradox in a more positive light.

Later research has revealed that the paradox does not necessarily short circuit Frege’s derivation of arithmetic from logic together with the Hume-Cantor Principle that the number of $F$s $=$ the number of $G$s if and only if there is a one-to-one correspondence between the $F$s and the $G$s. If this is taken as a (non-logical) axiom, instead of a theorem derived from Frege’s law V, the latter can simply be abandoned. (For details, see the entry on Frege’s theorem and foundations for arithmetic.) For critiques, see the papers in section II of Boolos 1998, and Burgess 2005.

To take a different tack, Church gives an elegant formulation of the simple theory of types that with the axioms of infinity and choice is an adequate framework for extant mathematics (Church, 1940)[^church-1940]. It has also proven fruitful even in areas removed from the foundations of mathematics. (For details, see the entries on Alonzo Church and on Church’s Type Theory.)

For some set theorists today, what the paradox highlights is that there is a problem with Frege’s and Russell’s *logical* notions of a class according to which it is specified by a formula that indicates a Fregean concept, a propositional function or an attribute. Some, such as Lavine (1994)[^lavine-1994] go further and argue that the paradox does not afflict Cantor’s combinatorial notion of a set as an object formed simply by collecting its members. An intermediate position (McLarty, 1997)[^mclarty-1997] is that while the paradox was a crisis for Frege and Russell, it was merely a source of problems and questions for set theorists. This is why they concentrated on finding precise axiomatizations that determine which sets exist. However, Frege and Russell were also seeking to state precise theories of concepts and propositional functions, respectively, if not directly of sets. Moreover, it is still worth asking what the distinction between the logical and combinatorial conceptions amounts to, because it is impossible to formulate set theory without formulas for the definitions of sets.

In any case, the development of axiomatic (as opposed to naïve) set theories exhibits various ingenious and mathematically and philosophically significant ways of dealing with Russell’s paradox. This paved the way for stunning results in the metamathematics of set theory. These results have included Gödel’s and Cohen’s theorems on the independence of the axiom of choice and Cantor’s continuum hypothesis. So let us see, roughly, how some of these methods – specifically, the so-called “untyped” methods – deal with Russell’s paradox.

Zermelo replaces (NC) with the following axiom schema of Separation (or *Aussonderungsaxiom*):

$$\tag{ZA}\forall A \exists B \forall x (x \in B \equiv(x \in A \wedge \phi)).$$

Note that ‘$B$’ is not free in ‘*φ*’. (ZA) demands that in order to gain entry into $B, x$ must be a member of an existing set $A$. As one might imagine, this requires a host of additional set-existence axioms, none of which would be required if (NC) had held up.

How does (ZA) avoid Russell’s paradox? One might think at first that it doesn’t. Let $A$ be $V$ —the whole universe of sets— and *φ* be $x \not\in x$, a contradiction again appears to arise. But in this case, all the contradiction shows is that $V$ is not a set. All the contradiction shows is that “$V$” is an empty name (i.e., that it has no denotation, that $V$ does not exist), since the ontology of Zermelo’s system consists solely of sets.

This same point can be made in yet another way, involving a relativized form of Russell’s argument. Let $B$ be any set. By (ZA), the set $R_B = \{x \in B: x \not\in x\}$ exists, but it cannot be an element of $B$. For if it is an element of $B$, then it is reasonable to ask whether or not it is an element of $R_B$; and it is if and only if it is not. Thus something, namely $R_B$, is “missing” from each set $B$. So again, $V$ is not a set, since nothing can be missing from $V$. But notice the following subtlety: unlike the previous argument involving the direct application of *Aussonderungs* to $V$, the present argument hints at the idea that, while $V$ is not a set, “$V$” is not an empty name. The next strategy for dealing with Russell’s paradox capitalizes on this hint.

John von Neumann’s (1925)[^neumann-1925] untyped method for dealing with paradoxes, and with Russell’s paradox in particular, is simple and ingenious. Von Neumann introduces a distinction between membership and non-membership and, on this basis, draws a distinction between sets and classes. An object is a *member* (simpliciter) if it is a member of some class; and it is a *non-member* if it is not a member of any class. (Actually, von Neumann develops a theory of functions, taken as primitive, rather than classes, wherein corresponding to the member/non-member distinction one has a distinction between an object that can be an argument of some function and one that cannot. In its modern form, due to Bernays and Gödel, it is a single-sorted theory of classes.)

Sets are then defined as members, and non-members are labeled “proper classes.” Only sets can be members of classes. So for example, the Russell class, $R$, cannot be a member of any class, and hence is not a set but a proper class. If $R$ is assumed to be an element of a class $A$, then it follows from one of von Neumann’s axioms that $R$ is not equivalent to $V$. But $R$ is equivalent to $V$, and hence not an element of $A$. Thus, von Neumann’s method is closely related to the result stated above about the set $R_B$, for arbitrary $B$. Von Neumann’s method, while admired by the likes of Gödel and Bernays, has been undervalued in recent years. (One notable exception is Burgess (2005)[^burgess-2005]). See (Bernays, 1968)[^bernays-1968], which summarizes his work on this beginning in the mid-1930s, and (Gödel, 1944)[^gödel-1944].

Quine (1937)[^quine-1937] and (1967) similarly provide another untyped method (in letter if not in spirit) of blocking Russell’s paradox, and one that is rife with interesting anomalies. Quine’s basic idea is to allow the universal set $V$ and to introduce a *stratified comprehension axiom*. In effect, the axiom blocks circularity by introducing a hierarchy (or stratification) that is similar to type theory in some ways, and dissimilar in others. (Details can be found in the entry on Quine’s New Foundations.) For the criticism that Quine’s theory compares unfavorably to Zermelo’s, see Martin 1970 and Boolos 1971. For another approach that allows the universal set, see Church 1974b.

Ackerman (1956) also distinguishes sets and classes, but in a different way than does Von Neumann. All objects of the theory are classes (represented by upper case variables), which are individuated by the usual principle of extensionality: $\forall x (x \in U \equiv x \in W) \rightarrow U = W$. The comprehension axiom for classes allows that there exists a class that contains all and only those sets that satisfy *φ*, for any condition *φ*. Because classes contain only sets that satisfy *φ*, there is no longer a proof of Russell’s paradox in the case where *φ* is $x \not\in x$. Consider a $Y$ such that for all $x, x \in Y \equiv x \not\in x$. By comprehension $Y$ exists and is the class $\{x: x \not\in x\}$. Take the case where $x = Y$ to get $Y \in Y \equiv Y \not\in Y$. This shows that $Y$ is not a set.

Some classes are also sets, so Ackerman introduces a second primitive relation symbol (in addition to $\in)$, the unary ‘$M$’, where ‘$M(x)$’ means that $x$ is a set. His comprehension axiom for sets is less restrictive than (ZA). It merely requires that sets are defined without reference to the class of all sets. More precisely, if every class that satisfies *φ* is a set, then there exists a set containing exactly those sets that satisfy *φ*, so long as *φ* does not involve $M$ and all parameters in *φ* are set parameters. Formally:

$$\tag{ACS}\forall x_1 ....x_n [\forall W (\phi(W) \rightarrow M(W)) \rightarrow \exists z \forall W (W \in z \equiv \phi(W))],$$

where *φ* is any condition that contains no occurrence of $M$ and contains no parameters other than set parameters $x_1 ,\ldots ,x_n$. The consequent of the main conditional says that $\{W: \phi(W)\}$ exists (by class comprehension) and is a set. Suppose that the restriction on $M$ was lifted and *φ* allowed to be $M \wedge \phi$. Then, by (ACS), for any condition *φ*, the class of all $W$ satisfying *φ* would be a set. In particular, the class $\{W: W \not\in W\}$ would be a set and Russell’s paradox would follow. Now suppose that the restriction that *φ* contains no parameters other than set parameters was lifted. Then class parameters in *φ* would be allowed. Choosing $W \in Y$ for $\phi(W)$, would yield the following instance of (ACS):

$$\forall W (W \in Y \rightarrow M(W)) \rightarrow \exists z \forall W (W \in z \equiv W \in Y).$$

It follows by generalization on $Y$ that for any class, if all its members are sets, then the class of its members exists (by class comprehension) and is a set:

$$\forall Y \forall W (W \in Y \rightarrow M(W)) \rightarrow \exists z \forall W (W \in z \equiv W \in Y).$$

It follows, by instantiation to the class $\{x: \phi(x)\}$, where *φ* is any condition, that every class that exists (by class comprehension) is a set:

$$\forall W (W \in \{x: \phi(x)\} \rightarrow M(W)) \rightarrow \exists z \forall W (W \in z \equiv W \in \{x: \phi(x)\}).$$

Taking $x \not\in x$ for *φ* yields Russell’s paradox. Clearly, then, considerable care has to be taken to avoid the paradox, if one takes Ackerman’s less restrictive approach to set comprehension rather than that of limitation of size. Note also that Ackerman’s set theory is equivalent to ZF and that (ACS) allows one to prove the so-called axiom of infinity as a theorem. See (Fraenkel, Bar-Hillel and Levy, 1973)[^fraenkel-1973] for more discussion as well as section 5.2 of the entry on alternative axiomatic set theories.

In contrast to Zermelo’s, von Neumann’s, Ackerman’s and Quine’s strategies, which are in a sense purely set theoretic, there have also been attempts to avoid Russell’s paradox by altering the underlying logic. There have been many such attempts, but one stands out as being both radical and, at the moment, somewhat popular (although not with set theorists *per se*): this is the *paraconsistent* approach, which limits the overall effect of an isolated contradiction on an entire theory. Classical logic mandates that any contradiction trivializes a theory by making every sentence of the theory provable. This is because, in classical logic, the following is a theorem:

$$\tag{Ex Falso Quodlibet} A \supset({\sim}A \supset B).$$

Now, virtually the only way to avoid EFQ is to give up disjunctive syllogism, that is, given the usual definitions of the connectives, *modus ponens*! So altering basic sentential logic in this way is radical indeed. Unfortunately, even giving up EFQ is not enough to retain a semblance of (NC). One also has to give up the following additional theorem of basic sentential logic:

$$\tag{Contraction} (A \supset(A \supset B)) \supset(A \supset B).$$

Using (Contraction) it can be argued that (NC) leads directly, not merely to an isolated contradiction, but to triviality. (For the argument that this is so, see the entry on Curry’s paradox, section 2.2. Note too that it is not enough merely to retain the name “*modus ponens*”; it is the rule itself that becomes modified within non-traditional logics.) Thus it seems that the woes of (NC) are not confined to Russell’s paradox but also include a negation-free paradox due to Curry.

Another suggestion might be to conclude that the paradox depends upon an instance of the principle of Excluded Middle, that either $R$ is a member of $R$ or it is not. This is a principle that is rejected by some non-classical approaches to logic, including intuitionism. However it is possible to formulate the paradox without appealing to Excluded Middle by relying instead upon the Law of Non-contradiction. Given the definition of $R$ it follows that $R \in R \equiv{\sim}(R \in R)$. So $R \in R \supset{\sim}(R \in R)$. But it is also true that $R \in R \supset R \in R$. So $R \in R \supset(R \in R \wedge{\sim}(R \in R))$. But by the Law of Non-contradiction ${\sim}(R \in R \wedge{\sim}(R \in R))$. So by *modus tollens* ${\sim}(R \in R)$. At the same time, since $R \in R \equiv{\sim}(R \in R)$, it follows that ${\sim}(R \in R) \supset R \in R$, and thus that $R \in R$. So both $R \in R$ and its negation are deduced using only intuitionistically acceptable methods. See Bell 2004 for relevant discussion.

It seems, therefore, that proponents of non-classical logics cannot claim to have preserved (NC) in any significant sense, other than preserving the purely syntactical form of the principle, and neither intuitionism nor paraconsistency plus the abandonment of Contraction will offer an advantage over the untyped solutions of Zermelo, von Neumann, or Quine. (Further discussion can be found in Meyer, Routley and Dunn 1979; Irvine 1992; Priest 2006, ch. 18; Weber 2010, 2012, and in the entries on Curry’s paradox (sec. 2.2) and paraconsistent logic (sec. 2.3).)

## 5. Russell’s Other Paradox and Russell’s Law

Russell’s paradox was not the only paradox that troubled Russell and, hence, not the only motivation for the type restrictions one finds in *Principia Mathematica*. In his earlier work, *The Principles of Mathematics*, Russell devotes a chapter to “the Contradiction” (Russell’s paradox), presenting it in several forms and dismissing several non-starter responses. He then signals that he will “shortly” discuss the doctrine of types. This doesn’t happen for several hundred pages, until he reaches the very end of the book, in Appendix B! There Russell presents an incipient, simple theory of types, not the theory of types we find in *Principia Mathematica*. Why was the later theory needed? The reason is that in Appendix B Russell also presents another paradox which he thinks cannot be resolved by means of the simple theory of types. This paradox concerns propositions, not classes, and it, together with the semantic paradoxes, led Russell to formulate his ramified version of the theory of types. For more on Russell’s discovery of the propositional paradox in 1902 see the primary sources and Urquhart’s introduction in (Russell 1994b)[^russell-1994b]. See also (Church 1978)[^church-1978] and (Deutsch 2022)[^deutsch-2022].

The propositional version of the paradox did not figure prominently in the subsequent development of logic and set theory, but it sorely puzzled Russell. For one thing, it seems to contradict Cantor’s theorem. Russell writes: “We cannot admit that there are more ranges [classes of propositions] than propositions” (1903, 527). The reason is that there seem to be easy, one to one correlations between classes of propositions and propositions. For example, the class $m$ of propositions can be correlated with the proposition that every proposition in $m$ is true. This, together with a fine-grained principle of individuation for propositions (asserting, for one thing, that if the classes $m$ and $n$ of propositions differ, then any proposition about $m$ will differ from any proposition about $n)$ leads to contradiction.

For some time, there was relatively little discussion of this paradox, although it played a key role in the development of Church’s logic of sense and denotation. While there are several set theories to choose from, there is only one well-developed formal theory of Russellian propositions, although such propositions are central to the views of Millians and direct-reference theorists. One would think that such a theory would be required for the foundations of semantics, if not for the foundations of mathematics. Thus, while one of Russell’s paradoxes has led to the fruitful development of the foundations of mathematics, there is more to be done in response to his “other” paradox in the foundations of semantics. To be sure, Church (1974a)[^church-1974a] and Anderson (1989)[^anderson-1989] have attempted to develop a Russellian intensional logic based on the ramified theory of types. (See the entry on Alonzo Church.) But an argument can be made that the ramified theory is too restrictive to serve as a foundation for the semantics of natural language. There have also been some recent attempts to obtain the beginnings of a Russellian intensional logic based on untyped set theories (Cantini 2004; Deutsch 2014)[^cantini-2004][^deutsch-2014]. And there is now a growth of interest in a related topic, that of “structure principles” in metaphysics. See (Bacon 2023)[^bacon-2023] and the citations therein.

It is also worth noting that a number of seemingly purely set-theoretical principles are actually (applied) instances of theorems of pure logic (i.e., of first-order quantification theory with identity). There is a (partial) list of these in Kalish, Montague, and Mar 2000. As mentioned earlier, Russell’s paradox is an instance of T269 in this list:

$$\tag{T269} {\sim}\exists y \forall x (Fxy \equiv{\sim} Fxx).$$

Reading the dyadic predicate letter “$F$” as “is a member of”, this says that it is not the case that there is a $y$ such that for any $x, x$ is a member of $y$ if and only if $x$ is not a member of $x$. Does this mean that Russell’s paradox reduces to T269?

Certainly the proof of T269 distills the essence of Russell’s argument, its pattern of reasoning. But that pattern also underwrites an endless list of seemingly frivolous “paradoxes” such as the famous paradox of the village barber who shaves all and only those villagers who do not shave themselves or, similarly, the paradox of the benevolent but efficient God who helps all and only those who do not help themselves.

How do these “pseudo paradoxes,” as they are sometimes called, differ, if at all, from Russell’s paradox? The pattern of reasoning is the same and the conclusion – that there is no such Barber, no such efficient God, no such set of non-self-membered sets – is the same: such things simply don’t exist. (However, as von Neumann showed, it is not necessary to go quite this far. Von Neumann’s method instructs us not that such things as $R$ do not exist, but just that we cannot say much about them, inasmuch as $R$ and the like cannot fall into the extension of any predicate that qualifies as a class.)

The standard answer to this question is that the difference lies in the subject matter. Quine asks, “why does it [Russell’s paradox] count as an antinomy and the barber paradox not?”; and he answers, “The reason is that there has been in our habits of thought an overwhelming presumption of there being such a class but no presumption of there being such a barber” (1966, 14). Even so, psychological talk of “habits of thought” is not illuminating. More to the point, Russell’s paradox sensibly gives rise to the question of what sets there are; but it is nonsense to wonder, on such grounds as T269, what barbers or Gods there are!

This verdict, however, is not quite fair to fans of the Barber or of T269 generally. They will insist that the question raised by T269 is not what barbers or Gods there are, but rather what non-paradoxical objects there are. This question is virtually the same as that raised by Russell’s paradox itself. Thus, from this perspective, the relation between the Barber and Russell’s paradox is much closer than many (following Quine) have been willing to allow (Salmon 2013, Kripke 2014)[^kripke-2014].

Note that there is a first-order logical formula that bears the same relation to the principle about the $R_B$’s that T269 bears to Russell’s paradox. It is the following:

$$\tag{T273} \forall z \forall y (\forall x [Fxy \equiv(Fxz \wedge{\sim} Fxx)] \supset{\sim} Fyz).$$

(We have taken the liberty of extending the numbering used in Kalish, Montague and Mar 2000 to T273.)[^kalish-2000]

Of particular interest is the logical status of the principle called “Cantor’s Diagonal Lemma”. Recall (CL) from above:

**(CL)**

Let $f$ be a function with domain $X$ and range $Y$. Then, on pain of contradiction, the diagonal set $D_f =$ $\{x \in X: x \not\in f(x)\}$ $\not\in Y$.

As stated earlier, an immediate corollary is that there is no function from domain $X$ onto the powerset of $X$ and this latter fact underpins Cantor’s theorem itself. In fact, it alone might well deserve to be called “Cantor’s theorem.” Then the principle that is more usually called Cantor’s theorem —that the cardinality of $X$ is always strictly less than the cardinality of the powerset of $X$ —follows as an easy corollary. Yet there is indeed a formula of pure logic that distills the essence of (CL) It is the following:

$${\sim}\exists y \forall x (x \in f(y) \equiv x \not\in f(x)).$$

Substituting an arbitrary binary relation symbol $P$ for epsilon, we have:

$${\sim}\exists y \forall x (P(x, f(y)) \equiv{\sim}P(x, f(x)).$$

But this formula is merely a substitution instance of T269! There is, therefore, a very close purely logical relationship between Russell’s paradox in the form of T269 and Cantor’s theorem in the form of Cantor’s lemma, (CL). The latter is a simple generalization of the former obtained by substituting a function letter $f$ for the variables at certain points in T269. Similarly, one obtains T269 from the formula above by taking $f$ to be the identity function. As we have seen, Russell was led to his paradox by contemplating Cantor’s theorem as applied to the universe $V$. We now see that from a purely logical point of view, the two are even more closely related than anyone might have imagined.

But not all set-theoretic paradoxes are similarly related to first-order logical theorems. The Burali-Forti paradox is an example, since the notion of a well-ordering is not elementary; that is, it is not first-order definable.

Russell’s paradox has never been passé, but recently there has been an explosion of interest in it by scholars involved in research in mathematical logic and in philosophical and historical studies of modern logic. Kripke (2014)[^kripke-2014] argues that Gödel’s first incompleteness theorem is a pure-logical consequence of the inconsistency of (NC), from which he proves non-constructively, i.e. without producing an example, that there is a true and unprovable sentence in formal systems of arithmetic. No particular paradox is used in this argument. Kripke then goes on to show how use of paradox in addition to pure logic can yield a constructive proof of incompleteness. Kripke uses the heterological paradox to get something like “Unprovable of itself is unprovable of itself.” From this point of view, the Gödel sentence makes an intelligible assertion that can be stated. Kripke takes the heterological paradox to be a version of Russell’s paradox with membership replaced with satisfaction. Both are instances of (T269).

Moreover, a glance at the contents of the 2004 volume *One Hundred Years of Russell’s Paradox* shows prominent mathematical and philosophical logicians and historians of logic poring over the paradox, proposing new ways back into Cantor’s paradise, or other ways of resolving the issue. Further investigations include radically new ways out of the dilemma posed by the paradox, such as plural quantification. (See Boolos 1984, McGee and Rayo 2000, Spencer 2012, and Pruss and Rasmussen 2015)[^boolos-1984][^mcgee-2015][^mcgee-2000][^pruss-2015][^spencer-2012]. There are also new studies of the theories of types (simple and ramified, and extensions thereof), new interpretations of Russell’s paradox, and constructive theories, of Russell’s paradox of propositions and of his own attempt at an untyped theory (the substitution theory), and so forth. More recently, it has even been debated whether the connection of Cantorian arguments to Russell’s paradox casts doubt on Cantor’s paradise. See Whittle 2015 for the claim that it does and the response in McGee 2015.

All of this reminds us that fruitful work can arise from the most unlikely of observations. As Dana Scott has put it, “It is to be understood from the start that Russell’s paradox is *not* to be regarded as a disaster. It and the related paradoxes show that the naïve notion of all-inclusive collections is untenable. That *is* an interesting result, no doubt about it” (1974, 207).

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=russell-paradox). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/russell-paradox/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=russell-paradox&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/russell-paradox/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- [Bertrand Russell Archives](http://www.mcmaster.ca/russdocs/russell.htm)
- [Bertrand Russell Research Centre](http://www.humanities.mcmaster.ca/~russell/)
- [Bertrand Russell Society](http://www.users.drew.edu/~jlenz/brs.html)
- [*Bertrand Russell Society Quarterly*](http://www.lehman.cuny.edu/faculty/rcarey/BRSQ/)
- [*Principia Mathematica*: Volume 1](http://name.umdl.umich.edu/AAT3201.0001.001) (University of Michigan Historical Math Collection)
- [*Principia Mathematica*: Volume 2](http://name.umdl.umich.edu/AAT3201.0002.001) (University of Michigan Historical Math Collection)
- [*Principia Mathematica*: Volume 3](http://name.umdl.umich.edu/AAT3201.0003.001) (University of Michigan Historical Math Collection)
- [*Russell: The Journal of Bertrand Russell Studies*](https://mulpress.mcmaster.ca/russelljournal/)
- [Russell’s Antinomy](http://mathworld.wolfram.com/RussellsAntinomy.html) (Wolfram MathWorld)
- [Russell’s Paradox](https://www.cut-the-knot.org/selfreference/russell.shtml), webpage at the site *Interactive Mathematics Miscellany and Puzzles*, by Alexander Bogomolny.

## Related Entries

Church, Alonzo | Frege, Gottlob | Frege, Gottlob: theorem and foundations for arithmetic | *Principia Mathematica* | Quine, Willard Van Orman: New Foundations | Russell, Bertrand | self-reference | set theory | set theory: alternative axiomatic theories | set theory: early development | type theory | Whitehead, Alfred North

### Acknowledgments

We’d like to thank the following people, who provided feedback on various iterations of this entry: Haim Gaifman; Chris Menzel for a corrections regarding Cantor and Burali-Forti; Gary Ostertag for discussion of Russell; Carl Posy for discussion of Brouwer; David Stump and Gerhard Heinzmann for discussion of Poincaré and help with our translation; Eduardo Ugalde for discussion of Shoenfield; and Tony Anderson for encouraging our approach to Cantor’s theorem via (CL). We’d like to also thank the following people, who provided helpful comments on earlier versions of this entry: Ken Blackwell, Fred Kroon, Paolo Mancosu, Chris Menzel, Jim Robinson, Fred Spiessens, Richard Zach, and several anonymous referees. Part of this entry was written with the support of Instituto Investigaciones Filosoficas (UNAM), PAPIITs IG400422 and IA400124.

[^anderson-1989]: Anderson, C. Anthony, 1989. “Russellian Intensional Logic,” in Joseph Almog, John Perry and Howard Wettstein (eds), *Themes from Kaplan*, Oxford: Oxford University Press, 67–103.

[^andrews-1986]: Andrews, Peter B., 1986. *Introduction to Mathematical Logic and Type Theory: To Truth Through Proof*, Orlando, FL: Academic Press.

[^bacon-2023]: Bacon, Andrew, 2023. *A Philosophical Introduction to Higher Order Logics*, London: Routledge.

[^barwise-1975]: Barwise, Jon, 1975. *Admissible Sets and Structures*, Berlin: Springer-Verlag.

[^barwise-1987]: ––– and John Etchemendy, 1987. *The Liar: An Essay on Truth and Circularity*, Oxford: Oxford University Press.

[^barwise-1996]: ––– and Lawrence Moss, 1996. *Vicious Circles*, Stanford: CSLI Publications.

[^bealer-1982]: Bealer, George, 1982. *Quality and Concept*, New York: Oxford University Press.

[^bell-2004]: Bell, John L, 2004. “Russell’s Paradox and Diagonalization in a Constructive Context,” in Godehard Link (ed.), *One Hundred Years of Russell’s Paradox*, Berlin and New York: Walter de Gruyter, 221–225.

[^beaney-2003]: Beaney, Michael, 2003. “Russell and Frege,” in Nicholas Griffin (ed.), *The Cambridge Companion to Bertrand Russell*, Cambridge: Cambridge University Press, 128–170.

[^bernays-1968]: Bernays, Paul, 1968. *Axiomatic Set Theory*, Amsterdam: North Holland.

[^boolos-1971]: Boolos, George, 1971. “The Iterative Conception of Set,” *The Journal of Philosophy*, 68: 215–232; reprinted in Boolos 1998, 13–29.

[^boolos-1984]: –––, 1984. “To be is to be the value of a variable (or to be some values of some variables),” *The Journal of Philosophy*, 81: 430–449; reprinted in Boolos 1998, 54–72.

[^boolos-1998]: –––, 1998. *Logic, Logic and Logic*, Richard Jeffrey (ed.), Cambridge, MA: Harvard University Press.

[^brouwer-1907]: Brouwer, L.E.J., 1907. “On the Foundations of Mathematics,” in Brouwer, 1975, *Collected Works 1. Philosophy and Foundations of Mathematics*, A. Heyting (ed.), Amsterdam: North-Holland.

[^brouwer-1912]: –––, 1912. “Intuitiosm and Formalism,” *Bulletin of the American Mathematical Society*, 37, 55–64.

[^burgess-2005]: Burgess, John, P., 2005. *Fixing Frege*, New York: Oxford University Press.

[^cantini-2004]: Cantini, Andrea, 2004. “On a Russellian Paradox about Propositions and Truth,” in Godehard Link (ed.) (2004) *One Hundred Years of Russell’s Paradox*, Berlin and New York: Walter de Gruyter, 259–284.

[^cantini-2009]: –––, 2009. “Paradoxes, Self-Reference and Truth in the 20th Century,” in Dov M. Gabbay and John Woods (eds) (2009) *Handbook of the History of Logic: Volume 5 – Logic From Russell to Church*, Amsterdam: Elsevier/North Holland, 875–1013.

[^cantor-1883]: Cantor, Georg, 1883. *Grundlagen einer allgemeinen Mannigfaltigkeitslehre*, Leipzig: B.G. Teubner; reprinted in Cantor 1932: 165–208; English translation in William B. Ewald (ed.), *From Kant to Hilbert: A source book in the foundations of mathematics*, 2 volumes, Oxford: Oxford University Press, 1996.

[^cantor-1899]: –––, 1899. “Letter to Dedekind” in Jean van Heijenoort (ed.), *From Frege to Gödel*, Cambridge, MA: Harvard University Press, 1967, 113–117.

[^church-1940]: Church, Alonzo, 1940. “A Formulation of the Simple Theory of Types,” *Journal of Symbolic Logic*, 5(2): 56–68; reprinted in Tyler Burge and Herbert Enderton (eds.), *The Collected Works of Alonzo Church*, Cambridge, MA: MIT Press, 2019.

[^church-1974a]: –––, 1974a. “Russellian Simple Type Theory,” *Proceedings and Addresses of the American Philosophical Association*, 47: 21–33.

[^church-1974b]: –––, 1974b. “Set Theory with a Universal Set,” *Proceedings of the Tarski Symposium*, 297–308; repr. in *International Logic Review*, 15: 11–23.

[^church-1978]: –––, 1978. “A Comparison of Russell’s Resolution of the Semantical Antinomies with that of Tarski,” *Journal of Symbolic Logic*, 41: 747–760; repr. in A.D. Irvine, *Bertrand Russell: Critical Assessments*, vol. 2, New York and London: Routledge, 1999, 96–112.

[^coffa-1979]: Coffa, Alberto, 1979. “The Humble Origins of Russell’s Paradox,” *Russell*, 33–34: 31–7.

[^cook-2015]: Cook, Roy, T., 2015. “Frege’s Little Theorem and Frege’s Way Out,” in Phillip A. Ebert and Marcus Rossberg (eds.), *Essays on Frege’s Basic Laws of Arithmetic*, Oxford: Oxford University Press, 2019, 384–410.

[^copi-1971]: Copi, Irving, 1971. *The Theory of Logical Types*, London: Routledge and Kegan Paul.

[^demopoulos-2005]: Demopoulos, William, and Peter Clark, 2005. “The Logicism of Frege, Dedekind and Russell,” in Stewart Shapiro (ed.), *The Oxford Handbook of Philosophy of Mathematics and Logic*, Oxford: Oxford University Press, 129–165.

[^deutsch-2014]: Deutsch, Harry, 2014. “Resolution of Some Paradoxes of Propositions,” *Analysis*, 74: 26–34.

[^deutsch-2022]: –––, 2022. “Propositional Paradoxes,” in Chris Tillman and Adam Murray (eds.), *The Routledge Handbook of Propositions*, London: Routledge, 533–545.

[^ebbinghaus-2007]: Ebbinghaus, Heinz-Dieter, and Volker Peckhaus, 2007. *Ernst Zermelo: An Approach to His Life and Work*, Berlin: Springer-Verlag.

[^forster-1995]: Forster, T.E., 1995. *Set Theory with a Universal Set*, 2nd edn, Oxford: Clarendon Press.

[^fraenkel-1973]: Fraenkel, Abraham A., Bar-Hillel, Yehoshua, and Levy, Azriel, 1973. *Foundations of Set Theory Second Revised Edition*, Amsterdam: Elsevier.

[^frege-1902]: Frege, Gottlob, 1902. “Letter to Russell,” in Jean van Heijenoort (ed.), *From Frege to Gödel*, Cambridge, MA: Harvard University Press, 1967, 126–128.

[^frege-1903]: –––, 1903. “The Russell Paradox,” in Gottlob Frege, *The Basic Laws of Arithmetic*, Berkeley: University of California Press, 1964, 127–143; abridged and repr. in A.D. Irvine, *Bertrand Russell: Critical Assessments*, vol. 2, New York and London: Routledge, 1999, 1–3.

[^gabbay-2009]: Gabbay, Dov M., and John Woods (eds.), 2009. *Handbook of the History of Logic: Volume 5 – Logic From Russell to Church*, Amsterdam: Elsevier/North Holland.

[^gaifman-2006]: Gaifman, Haim, 2006. “Naming and Diagonalization, from Cantor to Gödel to Kleene”, *Logic Journal of IGPL*, 14(5): 709–728.

[^galaugher-2013]: Galaugher, J.B., 2013. “Substitution’s Unsolved ‘Insolubilia’,” *Russell*, 33: 5–30.

[^garciadiego-1992]: Garciadiego, A., 1992. *Bertrand Russell and the Origins of the Set-theoretic “Paradoxes”*, Boston: Birkhäuser.

[^gödel-1940]: Gödel, Kurt, 1940. *The Consistency of the Axiom of Choice and of the Generalized Continuum Hypothesis with the Axioms of Set Theory*, Annals of Mathematics, Studies 3. Princeton.

[^gödel-1944]: –––, 1944. “Russell’s Mathematical Logic,” in A. Schilpp (ed.), *The Philosophy of Bertrand Russell*, New York: Tudor.

[^grattan-guinness-1971]: Grattan-Guinness, Ivor, 1971. “The Correspondence Between Georg Cantor and Philip Jourdain,” *Jbr. Dtsch. Math.-Ver*., 73(1):111–130.

[^grattan-guinness-1978]: –––, 1978. “How Bertrand Russell Discovered His Paradox,” *Historia Mathematica*, 5: 127–37.

[^grattan-guinness-2000]: –––, 2000. *The Search for Mathematical Roots: 1870–1940*, Princeton and Oxford: Princeton University Press.

[^griffin-2003]: Griffin, Nicholas (ed.), 2003. *The Cambridge Companion to Bertrand Russell*, Cambridge: Cambridge University Press.

[^griffin-2004]: –––, 2004. “The Prehistory of Russell’s Paradox,” in Godehard Link (ed.), *One Hundred Years of Russell’s Paradox*, Berlin and New York: Walter de Gruyter, 349–371.

[^griffin-2011]: ––– Bernard Linsky and Kenneth Blackwell (eds.), 2011. *Principia Mathematica at 100*, Hamilton, ON: Bertrand Russell Research Centre; also published as Special Issue, Volume 31, Number 1 of *Russell*.

[^hallett-1984]: Hallett, Michael, 1984. *Cantorian Set Theory and Limitation of Size*, Oxford: Clarendon.

[^halmos-1960]: Halmos, Paul R., 1960. *Naive Set Theory*, Princeton: D. van Nostrand.

[^hilbert-1904]: Hilbert, David, 1904. “On the Foundations of Logic and Arithmetic,” in Jean van Heijenoort (ed.), *From Frege to Gödel*, Cambridge, MA: Harvard University Press, 1967, 130–138.

[^hilbert-1925]: –––, 1925. “On the Infinite,” in Jean van Heijenoort (ed.), *From Frege to Gödel*, Cambridge, MA: Harvard University Press, 1967, 367–392.

[^irvine-1992]: Irvine, A.D., 1992. “Gaps, Gluts and Paradox,” *Canadian Journal of Philosophy* (Supplementary Volume), 18: 273–299.

[^irvine-2009]: ––– (ed.), 2009. *Philosophy of Mathematics*, Amsterdam: Elsevier/North Holland.

[^kalish-2000]: Kalish, Donald, Richard Montague and Gary Mar, 2000. *Logic: Techniques of Formal Reasoning*, 2nd edn, New York: Oxford University Press.

[^kanamori-2004]: Kanamori, Akihiro, 2004. “Zermelo and Set Theory,” *The Bulletin of Symbolic Logic*, 10: 487–553.

[^kanamori-2009]: –––, 2009. “Set Theory from Cantor to Cohen,” in A.D. Irvine (ed.), *Philosophy of Mathematics*, Amsterdam: Elsevier/North Holland, 395–459.

[^kaplan-2005]: Kaplan, David, 2005. “Reading On Denoting on its Centenary,” *Mind*, 114: 933–1003.

[^klement-2005]: Klement, Kevin, 2005. “The Origins of the Propositional Functions Version of Russell’s Paradox,” *Russell*, 24: 101–132.

[^klement-2010a]: –––, 2010a. “Russell, His Paradoxes and Cantor’s Theorem: Part I and Part II,” *Philosophy Compass*, 5(1): 16–41.

[^klement-2010b]: –––, 2010b. “The Functions of Russell’s No Class Theory,” *The Review of Symbolic Logic*, 3(4): 633–664.

[^klement-2014]: –––, 2014, “The Paradoxes and Russell’s Theory of Incomplete Symbols,” *Philosophical Studies*, 169: 183–207.

[^kripke-2011]: Kripke, Saul A., 2011, “A Puzzle about Time and Thought”, in Kripke, *Philosophical Troubles: Collected Papers, Volume 1*, Oxford: Oxford University Press: ch. 13, pp. 273–380.

[^kripke-2014]: –––, 2014. “The Road to Gödel,” in Jonathan Berg (ed.), *Naming and Necessity and More*, London: Palgrave Macmillan, 223–241.

[^landini-1993]: Landini, Gregory, 1993. “Russell to Frege, 24 May 1903: ‘I believe I have discovered that classes are entirely superfluous.’” *Russell: The Journal of the Bertrand Russell Archives* (Winter 1992–1993): 160–185.

[^landini-1998]: –––, 1998. *Russell’s Hidden substitutional Theory*, New York: Oxford University Press.

[^landini-2004]: –––, 2004. “Logicism’s ‘Insolubilia’ and Their Solution by Russell’s Substitutional Theory,” in Godehard Link (ed.), *One Hundred Years of Russell’s Paradox*, Berlin and New York: Walter de Gruyter, 373–399.

[^landini-2006]: –––, 2006. “The Ins and Outs of Frege’s Way Out,” *Philosophia Mathematica*, 14: 1–25.

[^landini-2011]: –––, 2011. *Russell*, London: Routledge.

[^landini-2013]: –––, 2013. “Zermelo ‘and’ Russell’s Paradox: Is There a Universal Set?” *Philosophia Mathematica*, 21: 180–199.

[^lavine-1994]: Lavine, Shaughan, 1994. *Understanding the Infinite*, Cambridge, MA: Harvard University Press.

[^levy-1979]: Levy, Azriel., 1979. *Basic Set Theory*, Berlin: Springer-Verlag; New York: Heidelberg.

[^link-2004]: Link, Godehard (ed.), 2004. *One Hundred Years of Russell’s Paradox*, Berlin and New York: Walter de Gruyter.

[^linsky-1990]: Linsky, Bernard, 1990. “Was the Axiom of Reducibility a Principle of Logic?” *Russell*, 10: 125–140; reprinted in A.D. Irvine (ed.), *Bertrand Russell: Critical Assessments* (Volume 2), 4 volumes, London: Routledge, 1999, 150–264.

[^linsky-2002]: –––, 2002. “The Resolution of Russell’s Paradox in *Principia Mathematica*,” *Philosophical Perspectives*, 16: 395–417.

[^linsky-2003]: –––, 2003. “The Substitutional Paradox in Russell’s Letter to Hawtrey,” *Russell: The Journal of Bertrand Russell Studies*, 151–160.

[^linsky-2013]: –––, 2013. “Ernst Schroeder and Zermelo’s Anticipation of Russell’s Paradox,” in Karine Fradet and François Lepage, *La crise des fondements : quelle crise?*, Montréal: Les Cahiers d’Ithaque, 7–23.

[^mares-2007]: Mares, Edwin, 2007. “The Fact Semantics for Ramified Type Theory and the Axiom of Reducibility,” *Notre Dame Journal of Formal Logic*, 48: 237–251.

[^martin-1970]: Martin, Donald A., 1970. “Review of *Set Theory and its Logic*,” *The Journal of Philosophy*, 67(4): 111–114.

[^mclarty-1997]: McLarty, Colin, 1997. “Review of Understanding the Infinite,” *Notre Dame Journal of Formal Logic*, 38: 314–324.

[^mcgee-2015]: McGee, Vann, 2015. “Whittle’s Assault on Cantor’s Paradise,” in Karen Bennett and Dean Zimmerman (eds.), *Oxford Studies in Metaphysics* (Volume 9), New York, Oxford University Press.

[^mcgee-2000]: McGee, Vann and Rayo, Augustin, 2000. “A Puzzle About De Rebus Beliefs,” *Analysis*, 60: 297–299.

[^menzel-1984]: Menzel, Christopher, 1984. “Cantor and the Burali-Forti Paradox,” *Monist*, 67: 92–107.

[^meyer-1979]: Meyer, Robert K., Richard Routley and Michael Dunn, 1979. “Curry’s Paradox,” *Analysis*, 39: 124–128.

[^moore-1982]: Moore, Gregory H., 1982. *Zermelo’s Axiom of Choice*, New York: Springer.

[^moore-1988]: –––, 1988. “The Roots of Russell’s Paradox,” *Russell*, 8: 46–56.

[^murawski-2011]: Murawski, Roman, 2011. “On Chwistek’s Philosophy of Mathematics,” in Nicholas Griffin, Bernard Linsky and Kenneth Blackwell (eds) (2011) *Principia Mathematica at 100*, in *Russell* (Special Issue), 31(1): 121–130.

[^myhill-1979]: Myhill, John R., 1979. “A Refutation of An Unjustified Attack on the Axiom of Reducibility”, *Bertrand Russell Memorial Volume*, George W. Roberts (ed.), New York: Humanities Press. pp. 81–90.

[^parsons-1987]: Parsons, Terence, 1987. “On the Consistency of the First Order Portion of Frege’s Logical System,” *Notre Dame Journal of Formal Logic*, 28(1): 161–168.

[^peckhaus-2004]: Peckhaus, Volker, 2004. “Paradoxes in Göttingen,” in Godehard Link (ed.), *One Hundred Years of Russell’s Paradox*, Berlin and New York: Walter de Gruyter, 501–515.

[^pelham-1995]: Pelham, Judy and Urquhart Alasdair, 1995. “Russellian Propositions,” in Dag Prawitz, Brian Skyrms and Dag Westertal (eds.), *Logic, Methodology and Philosophy of Science* IX, Elsevier, 307–326.

[^poincaré-1909]: Poincaré, Henri, 1909. “La logique de l’infini,” *Revue de métaphysique et morale*, 17: 461–482.

[^poincaré-1910]: –––, 1910. “On Transfinite Numbers,” in William Ewald (ed.), *From Kant to Hilbert: A Sourcebook in the Foundations of Mathematics* (Volume 2), Oxford, Clarendon Press.

[^priest-2006]: Priest, Graham, 2006. *In Contradiction*, 2nd edition, New York: Oxford University Press.

[^pruss-2015]: Pruss, A. R. and Rasmussen, J., 2015. “Problems with Plurals,” in Karen Bennett and Dean Zimmerman (eds.), *Oxford Studies in Metaphysics* (Volume 9), New York, Oxford University Press.

[^purckert-1989]: Purckert, Walter, 1989. “Cantor’s View of the Foundations of Mathematics,’ in Rowe and McLeary (eds.), *The History of Modern Mathematics Volume 1: Ideas and their Reception*, Academic Press, 49-65.

[^quine-1937]: Quine, W.V.O., 1937. “New Foundations for Mathematical Logic,” *American Mathematical Monthly*, 44: 70–80; reprinted in W.V.O. Quine, *From a Logical Point of View*, London: Harper & Row, 1953.

[^quine-1955]: –––, 1955. “On Frege’s Way Out,” *Mind*, 64(254): 145–159.

[^quine-1966]: –––, 1966. *The Ways of Paradox and Other Essays*, New York: Random House.

[^quine-1967]: –––, 1967. *Set Theory and Its Logic*, Harvard: Belknap Press.

[^russell-1902]: Russell, Bertrand, 1902. “Letter to Frege,” in Jean van Heijenoort (ed.), *From Frege to Gödel*, Cambridge, MA: Harvard University Press, 1967, 124–125.

[^russell-1903a]: –––, 1903a. *The Principles of Mathematics*, Cambridge: Cambridge University Press.

[^russell-1903b]: –––, 1903b. “Appendix B: The Doctrine of Types,” in Bertrand Russell, *The Principles of Mathematics*, Cambridge: Cambridge University Press, 1903, 523–528.

[^russell-1903c]: –––, 1903c. “Letter to Frege,” in Jean van Heijenoort (ed.), *From Frege to Gödel*, Cambridge, MA: Harvard University Press, 1967.

[^russell-1904a]: –––, 1904a. “Fundamental Notions,” in Alasdair Urquhart (ed.), *The Collected Papers of Bertrand Russell vol. 4 Foundations of Logic 1903–5*, London: Routledge, 1994, 111–259.

[^russell-1904b]: –––, 1904b. “On Functions,” in Alasdair Urquhart (ed.), *The Collected Papers of Bertrand Russell* (Volume 4: *Foundations of Logic 1903–5*), London: Routledge, 1994, 96–110.

[^russell-1905]: –––, 1905. “On Denoting,” *Mind*, 14(56): 479–493; reprinted in Bertrand Russell, *The Collected Papers of Bertrand Russell* (Volume 4: Foundations of Logic 1903–5), Alasdair Urquhart (ed.), London: Routledge, 1994.

[^russell-1906]: –––, 1906. “On Substitution,” in Bertrand Russell, *The Collected Papers of Bertrand Russell* (Volume 5: Towards Principia Mathematica 1905–8), Gregory Moore (ed.), London: Routledge, 2014.

[^russell-1907]: –––, 1907. “On Some Difficulties in the Theory of Transfinite Numbers and Order Types,” *Proceedings of the London Mathematical Society*, 2–4(1): 29–53.

[^russell-1908]: –––, 1908. “Mathematical Logic as Based on the Theory of Types,” *American Journal of Mathematics*, 30: 222–262; reprinted in Bertrand Russell, *Logic and Knowledge*, London: Allen and Unwin, 1956, 59–102; reprinted in Jean van Heijenoort (ed.), *From Frege to Gödel*, Cambridge, MA: Harvard University Press, 1967, 152–182.

[^russell-1919]: –––, 1919. *Introduction to Mathematical Philosophy*, London: George Allen and Unwin Ltd, and New York: The Macmillan Co.

[^russell-1944]: –––, 1944. “My Mental Development,” in Paul Arthur Schilpp (ed.), *The Philosophy of Bertrand Russell*, 3rd edition, New York: Tudor, 1951, 3–20.

[^russell-1959]: –––, 1959. *My Philosophical Development*, London: George Allen and Unwin, and New York: Simon & Schuster.

[^russell-1967]: –––, 1967, 1968, 1969. *The Autobiography of Bertrand Russell*, 3 volumes, London: George Allen and Unwin; Boston: Little Brown and Company (Volumes 1 and 2), New York: Simon and Schuster (Vol. 3).

[^russell-1994a]: –––, 1994a. *The Collected Papers of Bertrand Russell* (Volume 3: Towards the ‘Principles of Mathematic’s 1900–02), Gregory H. Moore (ed.), London: Routledge.

[^russell-1994b]: –––, 1994b. *The Collected Papers of Bertrand Russell* (Volume 4: Foundations of Logic 1903–5), Alasdair Urquhart (ed.), London: Routledge.

[^salmón-2013]: Salmón, Nathan, 2013. “A Note on Kripke’s Paradox about Time and Thought,” *Journal of Philosophy*, 110: 213–220.

[^scott-1974]: Scott, Dana, 1974. “Axiomatizing Set Theory,” in T.J. Jech (ed.), *Proceedings of Symposia in Pure Mathematics* (Volume 13, part 2), American Mathematical Society, 207–214.

[^shapiro-2005]: Shapiro, Stewart (ed.), 2005. *The Oxford Handbook of Philosophy of Mathematics and Logic*, Oxford: Oxford University Press.

[^shoenfield-1967]: Shoenfield, Joseph R., 1967. *Mathematical Logic*, Addison-Wesley Publishing.

[^simmons-2000]: Simmons, Keith, 2000. “Sets, Classes and Extensions: A Singularity Approach to Russell’s Paradox,” *Philosophical Studies*, 100: 109–149.

[^simmons-2005]: –––, 2005. “A Berry and a Russell without Self-Reference,” *Philosophical Studies*, 126: 253–261.

[^sobociński-1949]: Sobociński, Boleław 1949/1984. Leśniewski’s Analysis of Russell’s Paradox’, in Jan T.J. Srzednicki, V.F. Rickey, and J. Czelakowski (eds.), Leśniewski’s Systems: Ontology and Mereology. Boston: Martinus Nijhoff, pages 11–44.

[^sorensen-2002]: Sorensen, Roy A., 2002. “Philosophical Implications of Logical Paradoxes,” in Dale Jacquette (ed.), *A Companion to Philosophical Logic*, New York: Oxford University Press, 131–142.

[^sorensen-2003]: –––, 2003. “Russell’s Set,” in *A Brief History of the Paradox*, New York: Oxford University Press, 316–332.

[^spencer-2012]: Spencer, Joshua, 2012. “All Things Must Pass Away,” in Karen Bennett and Dean Zimmerman (eds.), *Oxford Studies in Metaphysics* (Volume 7), New York, Oxford University Press.

[^stevens-2004]: Stevens, Graham, 2004. “From Russell’s Paradox to the Theory of Judgement: Wittgenstein and Russell on the Unity of the Proposition,” *Theoria*, 70: 28–61.

[^stevens-2005]: –––, 2005. *The Russellian Origins of Analytical Philosophy*, London and New York: Routledge.

[^tappenden-2013]: Tappenden, Jamie, 2013. “The Mathematical and Logical Background to Analytic Philosophy,” in Michael Beaney (ed.) *The Oxford Handbook of the History of Analytic Philosophy*, Oxford: Oxford University Press, 318–354.

[^urquhart-1988]: Urquhart, Alasdair, 1988. “Russell’s Zig-Zag Path to the Ramified Theory of Types,” *Russell*, 8: 82–91.

[^urquhart-1994]: –––, 1994. “Introduction,” in *The Collected Papers of Bertrand Russell* (Volume 4: Foundations of Logic 1903–5), Alasdair Urquhart (ed.), London: Routledge, xiii-xliv.

[^urquhart-2003]: –––, 2003. “The Theory of Types,” in Nicholas Griffin (ed.), *The Cambridge Companion to Bertrand Russell*, Cambridge: Cambridge University Press, 286–309.

[^urquhart-2016]: –––, 2016. “Russell and Gödel,” *The Bulletin of Symbolic Logic*, 22(4): 504–520.

[^heijenoort-1967]: van Heijenoort, Jean (ed.), 1967. *From Frege to Gödel: A Source Book in Mathematical Logic, 1879–1931*, Cambridge, MA: Harvard University Press.

[^neumann-1925]: von Neumann, John, 1925. “An Axiomatization of Set Theory,” in Jean van Heijenoort (ed.), *From Frege to Gödel*, Cambridge, MA: Harvard University Press, 1967, 393–413.

[^wahl-2011]: Wahl, Russell, 2011. “The Axiom of Reducibility,” in Nicholas Griffin, Bernard Linsky and Kenneth Blackwell (eds.) *Principia Mathematica at 100*, in *Russell* (Special Issue), 31(1): 45–62.

[^weber-2010]: Weber, Z., 2010. “Transfinite Numbers in Paraconsistent Set Theory,” *Review of Symbolic Logic*, 3: 71–92.

[^weber-2012]: –––, 2012. “Transfinite Cardinals in Paraconsistent Set Theory,” *Review of Symbolic Logic*, 5: 269–293.

[^whitehead-1910]: Whitehead, Alfred North, and Bertrand Russell, 1910, 1912, 1913. *Principia Mathematica*, 3 volumes, Cambridge: Cambridge University Press; second edition, 1925 (Volume 1), 1927 (Volumes 2, 3); abridged as *Principia Mathematica to \*56*, Cambridge: Cambridge University Press, 1962.

[^whittle-2015]: Whittle, Bruno, 2015. “On Infinite Size,” in Karen Bennett and Dean Zimmerman (eds.), *Oxford Studies in Metaphysics* (Volume 9), New York, Oxford University Press.
