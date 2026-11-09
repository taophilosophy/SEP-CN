# Relative Identity
**First published Mon Apr 22, 2002; substantive revision Tue Dec 6, 2022**

*Deutsch, Harry, Garbacz, Pawel*

Identity is often said to be a relation each thing bears to itself and to no other thing (e.g., Zalabardo 2000)[^zalabardo-2000]. This characterization is clearly circular (“no *other* thing”) and paradoxical too, unless the notion of “each thing” is qualified. More satisfactory (though partial) characterizations are available and the idea that such a relation of absolute identity exists is commonplace. Some, however, deny that a relation of absolute identity exists. Identity, they say, is relative: It is possible for objects $x$ and $y$ to be the same $F$ and yet *not* the same $G$ (where $F$ and $G$ are predicates representing kinds of things—apples, ships, passengers—rather than merely properties of things—colors, shapes). In such a case “same” cannot mean absolute identity. For example, the same person might be two different passengers, since one person may be counted twice as a passenger. If to say that $x$ and $y$ are the same person is to say that $x$ and $y$ are persons and are (absolutely) identical, and to say that $x$ and $y$ are different passengers is to say that $x$ and $y$ are passengers and are (absolutely) distinct, we have a contradiction. Others maintain that while there are such cases of “relative identity”, there is also such a thing as absolute identity. According to this view, identity comes in two forms: trivial or absolute and nontrivial or relative (Gupta 1980)[^gupta-1980]. These maverick views present a serious challenge to the received, absolutist doctrine of identity. In the first place, cases such as the passenger/person case are more difficult to dismiss than might be supposed (but see below, §3). Secondly, the standard view of identity is troubled by many persistent puzzles and problems, some of recent and some of ancient origin. The relative identity alternative sheds considerable light on these problems even if it does not promise a resolution of them all.

A word about notation. In what follows, lower-case italic letters “$x$”, “$y$”, etc., are used informally either as variables (bound or free) or as (place-holders for) individual constants. The context should make clear which usage is in play. Occasionally, for emphasis or in deference to logical tradition, other expressions for individual constants are employed. Also, the use/mention distinction is not strictly observed; but again the context should resolve any ambiguity.

## 1. The Standard Account of Identity

[Note: The following material is somewhat technical. The reader may wish to casually review it now and return to it as needed, especially in connection with §5. The propositions $\text{Ref}, \text{LL}, \text{Ref}', \text{LL}', \text{NI}$, and $\text{ND}$ are identified in the present section and are referred to as such in the rest of the entry.]

Identity may be formalized in the language $L$ of classical first-order logic (FOL) by selecting a two-place predicate of $L$, rewriting it as “=”, and adopting the universal closures of the following two postulates:

$$\begin{align} \tag{\(\text{Ref}\)} x &= x \\ \tag{\(\text{LL}\)} x &= y \rightarrow[\phi(x) \rightarrow \phi(y)] \end{align}$$

where the formula $\phi(x)$ is like the formula $\phi(y)$ except for having occurrences of $x$ at some or all of the places $\phi(y)$ has occurrences of $y$ (see Enderton 2000, for a precise definition)[^enderton-2000]. Ref is the principle of the *reflexivity of identity* and LL (*Leibniz’ Law*) is the principle of the *indiscernibility of identicals*. It says in effect that identical objects cannot differ in any respect. The other characteristic properties of identity, *symmetry* $(x = y \rightarrow y = x)$, and *transitivity* $(x = y \amp y = z \rightarrow x = z)$, may be deduced from Ref and LL. Any relation that is reflexive, transitive, and symmetric is called an “equivalence relation”. Thus, identity is an equivalence relation satisfying LL. But not all equivalence relations satisfy LL. For example, the relation *x and y are the same size* is an equivalence relation that does not satisfy LL (with respect to a rich language such as English).

Let $E$ be an equivalence relation defined on a set $A$. For $x$ in $A$, $[x]$ is the set of all $y$ in $A$ such that $E(x, y)$; this is *the equivalence class of x determined by E*. The equivalence relation $E$ divides the set $A$ into mutually exclusive equivalence classes whose union is $A$. The family of such equivalence classes is called “the partition of $A$ induced by $E$”.

Now let $A$ be a set and define the relation $I(A,x,y)$ as follows: For $x$ and $y$ in $A$, $I(A,x,y)$ if and only if for each subset $X$ of $A$, either $x$ and $y$ are both elements of $X$ or neither is an element of $X$. This definition is equivalent to the more usual one identifying the identity relation on a set $A$ with the set of ordered pairs of the form $\langle x,x\rangle$ for $x$ in $A$. The present definition proves more helpful in what follows.

Suppose for the moment that we do not assign any special interpretation to the identity symbol. We treat it like any other two-place predicate. Let $M$ be a structure for $L$ and assume that Ref and LL are true in $M$. Call the relation defined in $M$ by the conjunction of Ref and LL “indiscernibility” (see Enderton 2000, for the definition of definability in a structure)[^enderton-2000]. There are three important points to note about the relationship between indiscernibility, and the relation $I(A,x,y)$. First, indiscernibility need not be the relation $I(A,x,y)$ (where $A$ is the domain of the structure). It might be an equivalence relation $E$ having the property that for some elements $u,v$, of the domain, $E(u,v)$ holds, although $I(A,u,v)$ fails. Secondly, there is no way to “correct for” this possibility. There is no sentence or set of sentences that could be added to the list beginning with Ref and LL that would guarantee that indiscernibility coincides with $I(A,x,y)$. This fact is usually expressed by saying that identity is not a first-order or “elementary” relation. (For a proof, see Hodges 1983.)[^hodges-1983] However, in a language such as set theory (as usually interpreted) or second-order logic, in which there is a quantifier “all $X$” permitting quantification over all subsets of a given set, $I(A,x,y)$ is definable (Freund 2019)[^freund-2019].

Third, given any structure $M$ for $L$ in which Ref and LL are true, there is a corresponding structure $\textit{QM}$, the “quotient structure” determined by $M$, in which indiscernibility *does* coincide with $I(A,x,y)$. $\textit{QM}$ is obtained in roughly the following way: Let the elements of $\textit{QM}$ be the equivalence classes $[x]$, for elements $x$ of $M$ determined by indiscernibility in $M$. If $F$ is a one-place predicate true in $M$ of some object $x$ in $M$, then define $F$ to be true of $[x]$ in $\textit{QM}$, and similarly for many-place predicates and constants. It can then be shown that any sentence true in $M$ is true in $\textit{QM}$, and vice versa. The existence of quotient structures makes it possible to treat the identity symbol as a logical constant interpreted in terms of $I(A,x,y)$. There is in fact in general no other way to *guarantee* that Ref and LL will hold in every structure. (As Quine [1970] points out, however, a *finite* language will always contain a predicate satisfying Ref and LL in any structure; cf. Hodges 1983.)[^hodges-1983] The alternative, however, is to view FOL with Ref and LL (FOL⁼) as a proper theory in whose models (structures in which Ref and LL hold) there will be an equivalence relation $E$ such that if $E(x,y)$ holds, then $x$ and $y$ will be indiscernible with respect to the *defined* subsets of the domain. But we cannot in general assume that every subset of the domain is definable. If the domain is infinite, $L$ runs out of defining formulas long before the domain runs out of subsets. Nonetheless, a strong metatheorem asserts that any set of formulas that has a model, has a countable (finite or denumerable) model. This means that the difference between indiscernibility and $I(A,x,y)$ is minimized at least to the extent that, for a sufficiently rich language such as $L$, the valid formulas concerning indiscernibility (i.e., the formulas true in every model of what is termed below “the pure $L$-theory with identity”) coincide with the valid formulas concerning $I(A,x,y)$. (See Epstein 2001 for a sketch of a proof of this fact.)[^epstein-2001] This is not to say, however, that there isn’t a significant difference between identity *qua* indiscernibility and identity *qua* $I(A,x,y)$ (see below). Both points of view—that FOL⁼ is a proper theory and that it is a logic—may be found in the literature (Quine 1970)[^quine-1970]. The latter is the more usual view and it will count here as part of the standard account of identity.

Assume that $L'$ is some fragment of $L$ containing a subset of the predicate symbols of $L$ and the identity symbol. Let $M$ be a structure for $L'$ and suppose that some identity statement $a = b$ (where $a$ and $b$ are individual constants) is true in $M$, and that Ref and LL are true in $M$. Now expand $M$ to a structure $M'$ for a richer language—perhaps $L$ itself. That is, assume we add some predicates to $L'$ and interpret them as usual in $M$ to obtain an expansion $M'$ of $M$. Assume that Ref and LL are true in $M'$ and that the interpretation of the terms $a$ and $b$ remains the same. Is $a = b$ true in $M'$? That depends. If the identity symbol is treated as a logical constant, the answer is “yes”. But if it is treated as a non-logical symbol, then it can happen that $a = b$ is false in $M'$. The indiscernibility relation defined by the identity symbol in $M$ may differ from the one it defines in $M'$; and in particular, the latter may be more “fine-grained” than the former. In this sense, if identity is treated as a logical constant, identity is *not* “language relative”; whereas if identity is treated as a non-logical notion, it $is$ language relative. For this reason we can say that, treated as a logical constant, identity is “unrestricted”. For example, let $L'$ be a fragment of $L$ containing only the identity symbol and a single one-place predicate symbol; and suppose that the identity symbol is treated as non-logical. The formula

$$ \forall x\forall y\forall z(x = y \vee x = z \vee y = z) $$

is then true in any structure for $L'$ in which Ref and LL are true. The reason is that the unique one-place predicate of $L'$ divides the domain of a structure into those objects it satisfies and those it does not. Hence, at least two of any group of three objects will be indiscernible. On the other hand, if the identity symbol is interpreted as $I(A,x,y)$, this formula is false in any structure for $L'$ with three or more elements.

If we do wish to view identity as a non-logical notion, then the phenomenon of language relativity suggests that it is best not to formalize identity using a single identity predicate “=”. Instead, we have the following picture: We begin with a language $L$ and define an *L-theory with identity* to be a theory whose logical axioms are those of FOL and which is such that $L$ contains a two-place predicate $E_L$ satisfying the non-logical axiom $\textrm{Ref}\,'$ and the non-logical axiom schema $\textrm{LL}'$

$$\begin{align} \tag{\(\text{Ref}\,'\)} &E_L (x,x) \\ \tag{\(\text{LL}'\)} &E_L (x,y) \rightarrow (\phi(x) \rightarrow \phi(y)). \end{align}$$

The *pure* $L$-theory with identity is the $L$-theory whose sole non-logical axiom is $\textrm{Ref}\,'$ and whose sole non-logical axiom schema is $\textrm{LL}'$.

Now the phenomenon of language relativity can be described more accurately as follows. Let $L_1$ be a sublanguage of $L_2$ and assume that $T_1$ and $T_2$ are, respectively, the pure $L_1$-theory with identity and the pure $L_2$-theory with identity. Let $M_1$ and $M_2$ be models of $T_1$ and $T_2$, respectively, having the same domain. Assume that $a$ and $b$ are individual constants having the same interpretation in $M_1$ and $M_2$. Let $E_1$ and $E_2$ be the identity symbols of $L_1$ and $L_2$. It can happen that $E_1 (a,b)$ is true in $M_1$ but $E_2 (a,b)$ is false in $M_2$. We can then say, with Geach (1967; see §4) and others, that the self-same objects indiscernible according to one theory may be discernible according to another.

There are two further philosophically significant features of the standard account of identity. First, identity is a *necessary* relation: If $a$ and $b$ are rigid terms (terms whose reference does not vary with respect to parameters such as time or possible world) then

**(NI)**

If $a = b$ is true, then it is necessarily true.

Assuming certain modal principles, the necessity of distinctness (ND) follows from NI.

**(ND)**

If $a \ne b$ is true, then it is necessarily true.

Note that the necessary truth of $a = b$ does not imply the necessary existence of objects $a$ or $b$. We may assume that what a rigid term $a$ denotes at a possible world (or moment of time) $w$ need not exist in $w$. Secondly, we do not ordinarily say things of the form “$x$ is the same as $y$”. Instead, we say “$x$ and $y$ are the same person” or “$x$ and $y$ are the same book”. The standard view is that the identity component of such statements is just “$x$ is the same as $y$”. For example, according to the standard view, “$x$ and $y$ are the same person” reduces to “$x$ and $y$ are persons and $x$ is the same as $y$”, where the second conjunct may be formalized as in FOL⁼.

## 2. Paradoxes of Identity

The concept of identity, simple and settled though it may seem (as characterized by the standard account), gives rise to a great deal of philosophical perplexity. A few (by no means all) of the salient problems are outlined below. These are presented in the form of paradoxes—arguments from apparently undeniable premises to obviously unacceptable conclusions. The aim here is to make clear just what options are available to one who would stick close to the standard account. Often (but not always) little or no defense or critique of any particular option is offered. In the next section, we shall see what the relative identity alternative offers by comparison.

### 2.1 The Paradox of Change

The most fundamental puzzle about identity is the problem of change. Suppose we have two photographs of a dog, Oscar. In one, $A$, Oscar is a puppy, in the other, $B$, he is old and gray-muzzled. Yet we hold that he is the same dog, in, it appears, direct violation of LL. More explicitly, $B$ is a photograph of an old dog with a gray muzzle; $A$ is a photograph of a young dog without a gray muzzle. $A$ and $B$ are photographs of the same dog. But according to LL, if the dog in $B$ has a property (e.g., having a gray muzzle) that the dog in $A$ lacks, then $A$ and $B$ are *not* photographs of the same dog. Contradiction.

Various solutions have been proposed. The most popular are the following two: (1) Simple properties such as having or lacking a gray muzzle are actually relations to times. Oscar has the property of lacking a gray muzzle *at time t* and the property of having a gray muzzle at (a later) $t'$; but there is no incompatibility, since being thus and so related to time $t$ and not being thus and so related to time $t'$ are compatible conditions, and hence change involves no violation of LL. (2) Oscar is an object that is extended in time as well as space. The puppy Oscar and old gray-muzzled Oscar are distinct temporal parts or stages of the whole temporally extended Oscar. Both photographs are therefore not photographs of the whole Oscar at all because there cannot be still photographs of Oscar.

These proposals may seem plausible, and indeed most philosophers subscribe to one or other of them. The most common objections—that on the temporal parts account, objects are not “wholly present” at any given time, and that on the relations-to-times account, seemingly simply properties of objects, such as Oscar having a gray muzzle, are complicated relations—do little more than affirm what their targets deny. Yet the objections are an attempt to give voice to a strong intuition concerning our experience as creatures existing in time. Both (1) and (2) treat time and change from a “God’s eye” point of view. (1) presupposes time laid out “all at once”, so to speak, and similarly for (2). But we experience no such thing. Instead, while we are prepared to wait to see the whole of a baseball game we are watching, we are not prepared to wait to see the whole of a painting we are viewing.

### 2.2 Chrysippus’ Paradox

The following paradox—a variation of the paradox of change—raises some new questions. It is due to the Stoic philosopher Chrysippus (c. 280 BCE – c. 206 BCE) and has been resurrected by Michael Burke (1994). In Chrysippus’s example, “Dion” is the name of a human and “Theon” is the name of the proper part of Dion that includes everything but his [Dion’s] left foot. Dion then loses his foot and Chrysippus wishes to know which of those objects—Dion or Theon—survives after Dion loses the foot. Burke’s example is to suppose that, at some point $t'$ in the future, poor Oscar will lose his tail. He then considers the proper part of Oscar, as he is now (at $t)$, consisting of the whole of Oscar minus his tail. Call this object “Oscar^{−}”. According to the standard account of identity, Oscar and Oscar^{−} are distinct at $t$ and hence, by ND, they are distinct at $t'$. (Intuitively, Oscar and Oscar^{−} are distinct at $t'$ since Oscar has a property at $t'$ that Oscar^{−} lacks, namely, the property of having had a tail at $t$. Notice that this argument involves a tacit appeal to ND—or NI, depending on how you look at it.) Hence, if both survive, we have a case of two distinct physical objects occupying exactly the same space at the same time. Assuming that is impossible, and assuming, as commonsense demands, that Oscar survives the loss of his tail, it follows that Oscar^{−} does not survive. This conclusion is paradoxical because it appears that *nothing happens* to Oscar^{−} in the interval between $t$ and $t'$ that would cause it to perish.

The first group of solutions does not take into consideration the amputation event that occurred at $t'$ when they account for what exists—you may dub them *untemporalized* solutions. One extreme option in this category is to deny that there are such things as Oscar^{−}. Undetached proper parts of objects don’t exist (van Inwagen 1981). A less extreme version allows for commonsense undetached parts, like tails or feet—of course Oscar^{−} does not belong to this category, so it does not exist (Carmichael 2020)[^carmichael-2020]. On the other hand, a more extreme option is to deny the existence of both Oscar and Oscar^{−}—this may follow from some reductionist view like the one that only elementary particles exist. A third, less extreme, option is to insist that objects of *different* kinds, e.g., a clay statue and the piece of clay it is composed of, *can* occupy the same space at the same time, but objects of the same kind, e.g., two statues, cannot (Wiggins 1968; for refinements, see Oderberg 1996)[^oderberg-1996][^wiggins-1968]. So Oscar and Oscar^{−} are different despite the fact that from $t'$ onwards they occupy the same space. Guillon (2021) notes that there are three varieties of this colocationist view. First, one may maintain that they are different despite sharing all parts: every proper part of Oscar is a proper part of Oscar^{−} and *vice versa*. The second colocationist variety allows for two different material objects to be sums of the same set of material objects—so Oscar and Oscar^{−} may be different although they are ultimately composed of the same particles. Finally, one of them, most probably Oscar^{−}, may be considered a proper part of the other. Obviously, these three options are meaningful only if one does *not* assume the full strength of general existentional mereology. The last global option is to claim that Oscar and Oscar^{−} are two distinct temporally extended objects—a dog part, Oscar^{−}, and a dog, Oscar, which overlaps at $t'$. Temporal parts of distinct objects can occupy the same space at the same time.

The solutions in the second group, *temporalized* solutions, recognize the world’s ontological inventory has changed at $t'$. For instance, Chrysippus, according to Philo of Alexandria, claimed that “it is necessary that Dion remains while Theon has perished” (Long and Sedley 1987, p. 172)[^long-1987], so Dion exists throughout the whole period, but Theon dies at $t'$. Accepting some kind of mereological essentialism (Chisholm 1973)[^chisholm-1973], one may hold an opposite view: since all parts are essential to Oscar, the amputation event killed Oscar while Oscar^{−} either was created by the event or enjoyed existence throughout the whole period in question. Then you may maintain that the event at $t'$ either (i) brought Oscar^{−} into existence or (ii) did not disrupt Oscar^{−}’s prior existence (i.e., Oscar^{−} existed at all times from $t$ to $t'$). Finally, a proponent of contingent identity may claim that at *t* Oscar is different from Oscar^{−}, but at $t'$ they become identical.

### 2.3 The Paradox of 101 Dalmatians

(This paradox is also known as the paradox of 1001 cats; Geach 1980, Lewis 1993.)[^geach-1980][^lewis-1993] Focus on Oscar and Oscar^{−} at $t$—before Oscar loses his tail. Is Oscar^{−} a dog? When Oscar loses his tail the resulting creature is certainly a dog. Why then should we deny that Oscar^{−} is a dog? We saw above that one possible response to Chrysippus’ paradox was to claim that Oscar^{−} does not exist from $t'$ on. But even if we adopt this view, how does it follow that Oscar^{−}, existing as it does at $t$, is not a dog? Yet if Oscar^{−} is a dog, then, given the standard account of identity, there are two dogs where we would normally count only one. In fact, for each of Oscar’s hairs, of which there are at least 101, there is a proper part of Oscar—Oscar minus a hair—which is just as much a dog as Oscar^{−}. There are then at least 101 dogs (and in fact many more) where we would count only one. Some claim that things such as dogs are “maximal”. No proper part of a dog is a dog (Burke 1993). One might conclude as much simply to avoid multiplying the number of dogs populating the space reserved for Oscar alone. But the maximality principle may seem to be independently justified as well. When Oscar barks, do all these different dogs bark in unison? If a thing is a dog, shouldn’t it be capable of independent action? Yet Oscar^{−} cannot act independently of Oscar. Nevertheless, David Lewis (1993) has suggested a reason for counting Oscar^{−} and all the 101 dog parts that differ (in various different ways) from one another and Oscar by a hair, as dogs, and in fact as Dalmatians (Oscar is a Dalmatian). Lewis invokes Unger’s (1980) “problem of the many”. Oscar sheds continuously but gradually. His hairs loosen and then dislodge, some such remaining still in place. Hence, within Oscar’s compass at any given time there are congeries of Dalmatian parts sooner or later to become definitely Dalmatians; some in a day, some in a second, or a split second. It seems arbitrary to proclaim a Dalmatian part that is a split second away from becoming definitely a Dalmatian, a Dalmatian, while denying that one a day away is a Dalmatian. As Lewis puts it, we must either deny that the “many” are Dalmatians, or we must deny that the Dalmatians are many. Lewis endorses proposals of both types but seems to favor one of the latter type according to which the Dalmatians are not many but rather “almost one”. In any case, the standard account of identity seems unable on its own to handle the paradox of 101 Dalmatians. It requires that we either deny that Oscar minus a hair is a dog—and a Dalmatian—or else that we must affirm that there is a multiplicity of Dalmatians, all but one of which is incapable of independent action and all of which bark in unison no more loudly than Oscar barks alone.

### 2.4 The Paradox of Constitution

Suppose that on day 1 Jones purchases a piece of clay $c$ and fashions it into a statue $s_1.$ On day 2, Jones destroys $s_1$, but not $c$, by squeezing $s_1$ into a ball and fashions a new statue $s_2$ out of $c$. On day 3, Jones removes a part of $s_2$, discards it, and replaces it using a new piece of clay, thereby destroying $c$ and replacing it by a new piece of clay, $c'$. Presumably, $s_2$ survives this change. Now what is the relationship between the pieces of clay and the statues they “constitute”? A natural answer is: identity. On day $1, c$ is identical to $s_1$ and on day $2, c$ is identical to $s_2$. On day $3, s_2$ is identical to $c'$. But this conclusion directly contradicts NI. If, on day $1, c$ is (identical to) $s_1$, then it follows, given NI, that on day $2, s_1$ is $s_2$ (since $c$ is identical to $s_2$ on day 2) and hence that $s_1$ exists on day 2, which it does not. By a similar argument, on day $3, c$ is $c'$ (since $s_2$ is identical to both) and so $c$ exists on day 3, which it does not. We might conclude, then, that either constitution is not identity or that NI is false. Neither conclusion is wholly welcome. Once we adopt the standard account less NI, the latter principle follows directly from the assumption that individual variables and constants in quantified modal logic are to be handled exactly as they are in first-order logic. And if constitution is not identity, and yet statues, as well as pieces of clay, are physical objects (and what else would they be?), then we are again forced to affirm that distinct physical objects may occupy (exactly) the same space at the same time. The statue $s_1$ and the piece of clay $c$ occupy the same space on day 1. Even if this is deemed possible (Wiggins 1980)[^wiggins-1980], it is unparsimonious. The standard account is thus *prima facie* incompatible with the natural idea that constitution is identity.

Philosophers have not argued by direct appeal to NI or ND. Typically (e.g., Gibbard 1975, Noonan 1993, Johnston 1992)[^gibbard-1975][^johnston-1992][^noonan-1993], arguments that $c$ and $s_1$ are not identical run as follows: $c$ exists prior to the existence of $s_1$ and hence the two are not identical. Again, $s_1$ possesses the property of being such that it will be destroyed by being squeezed into a ball, but $c$ does not possess this property $(c$ will be squeezed into a ball but it will not thereby be destroyed). So again the two are not identical. Further, whatever the future in fact brings, *c might* have been squeezed into a ball and not destroyed. Since that is not true of $s_1$, the two are not identical. On a careful analysis, however, each of these arguments can be seen to rely on NI or ND, *provided one adopts the standard account of modal/temporal predicates.* This last proviso suggests an interesting way out for one who adheres to the standard account of identity but who also holds that constitution is identity (see below).

Some philosophers find it important or at least expedient to frame the issue in terms of the case of a statue $s$ and piece of clay $c$ that coincide throughout their entire existence. We bring both $c$ and $s$ into existence by joining two other pieces of clay together, or we do something else that guarantees total coincidence. It seems that total coincidence is supposed to lend plausibility to the claim that, in such a case at least, constitution is identity (and hence NI is false—Gibbard 1975)[^gibbard-1975]. It may do so, psychologically, but not logically. The same sorts of arguments as against the thesis that constitution is identity apply in such a case. For example, $s$ may be admired for its aesthetic traits, even long after it ceases to exist, but this need not be true of $c$. And $s$ has the property, which $c$ lacks, of being destroyed if squeezed into a ball. Those who defend the thesis that constitution is identity need to defend it in the general case of partial coincidence; and those who attack the thesis do so with arguments that work equal well against both total and partial coincidence. The assumption that $s$ and $c$ are totally coincident is therefore inessential.

The doctrine of temporal parts offers only limited help. The statement that $c$ is identical to $s_1$ on day 1 but identical to $s_2$ on day 2 can be construed to mean that $c$ is a temporally extended object whose day 1 stage is identical to $s_1$ and whose day 2 stage is identical to $s_2$. Since the two stages are not identical, NI does not apply. Similarly, we can regard $s_2$ as a temporally extended object that overlaps $c$ on day 2 and $c'$ on day 3. But unless temporal parts theorists are prepared to defend a doctrine of modally extended objects—objects extended through possible worlds analogous to objects extended in time—there remains a problem. $s_2$ *might* have been made of a different piece of clay, as is in fact the case on day 3. That is, it is logically possible for $s_2$ to fail to coincide with the day 2 stage of $c$. But it is not logically possible for the day 2 stage of $c$ to fail to coincide with itself.

Lewis recognizes this difficulty and proposes to deal with it by appealing to his counterpart theory (Lewis 1971, 1986, and 1993). Different concepts, e.g., *statue* and *piece of clay*, are associated with different counterpart relations and hence with different criteria of trans-world identity. This has the effect of rendering modal predicates “Abelardian” (Noonan 1991, 1993)[^noonan-1991]. The property determined by a modal predicate may be affected by the subject term of a sentence containing the predicate. The subject term denotes an object belonging to this or that kind or sort. But different kinds or sorts may determine different properties (or different counterpart relations). In particular, the properties determined by the predicate “might not have coincided with $c_2$” (where $c_2$ names the day 2 stage of $c)$ in the following sentences,

1. $s_2$ might not have coincided with $c_2$,
2. $c_2$ might not have coincided with $c_2$,

are *different*, and hence (a) and (b) are compatible, even assuming that $s_2$ and $c_2$ are identical. (It should be emphasized that counterpart theory is not the only means of obtaining Abelardian predicates. See Noonan 1991.)[^noonan-1991]

The upshot seems to be that the advocate of the standard account of identity must maintain either that constitution is not identity or that modal predicates are Abelardian. The latter option may be the fruitful one, since for one thing it seems to have applications that go beyond the issue of constitution.

### 2.5 The Ship of Theseus Paradox

Imagine a wooden ship restored by replacing all its planks and beams (and other parts) by new ones. Plutarch reports that such a ship was

> … a model for the philosophers with respect to the disputed arguments … some of them saying it remained the same, some of them saying it did not remain the same. (Plutarch, *Life of Theseus*, 23; translated by Michael Rea in Rea 1995, p. 531)[^rea-1995].

Hobbes added the catch that the old parts are reassembled to create another ship exactly like the original. Both the restored ship and the reassembled one appear to qualify equally to be the original. In the one case, the original is “remodeled”, in the other, it is reassembled. Yet the two resulting ships are clearly not the same ship.

Some have proposed that in a case like this our ordinary “criteria of identity” fail us. The process of dismantling and reassembling usually preserves identity, as does the process of part replacement (otherwise no soldier could be issued just one rifle and body shops would function as manufacturers). But in this case the two processes produce conflicting results: We get two ships, one of which is the same ship as the original, by one set of criteria, and the other is the original ship, by another set of criteria. There is a similar conflict of criteria in the case of personal identity: Brain duplication scenarios (Wiggins 1967, Parfit 1984)[^parfit-1984][^wiggins-1967] suggest that it is logically possible for one person to split into two competitors, each with equal claim to be the original person. We take it for granted that brain duplication will preserve the psychological properties normally relevant to reidentifying persons and we also take it for granted that the original brain continues to embody these properties even after it is duplicated. In this sense there is a conflict of criteria. Such a case of “fission” gives us two distinct embodiments of these properties.

Perhaps we should conclude that identity is not what matters. Instead, what matters is some *other* relation, but one that accounts as readily as identity for such facts as that the owner of the original ship would be entitled to both the restored version and the reassembled one. For the case of personal identity, Parfit (1984) develops such a response in detail. A related reaction would be to claim that if both competitors have equal claim to be the original, then neither *is* the original. If, however, one competitor is inferior, then the other wins the day and counts as the original. It seems that on this view certain contingencies can establish or falsify identity claims. That conflicts with NI. Suppose that $w$ is a possible world in which no ship is assembled from the discarded parts of the remodeled ship. In this world, then, the remodeled ship is the original. By NI, the restored ship and the original are identical in the actual world, contrary to the claim of the “best candidate” doctrine (which says that neither the remodeled nor the reassembled ship is the original). There are, however, more sophisticated “best candidate” theories that are not vulnerable to this objection (Nozick 1982)[^nozick-1982].

Some are convinced that the remodeled ship has the best claim to be the original, since it exhibits a greater degree of spatio-temporal continuity with the original (Wiggins 1967)[^wiggins-1967]. But it is unclear why the intuition that identity is preserved by spatio-temporal continuity should take precedence over the intuition that identity is preserved in the process of dismantlement and reassembly. Furthermore, certain versions of the ship of Theseus problem do not involve the feature that one of the ships competing to be the original possesses a greater degree of spatio-temporal continuity with the original than does the other (see below). Others are equally convinced that identity is *not* preserved by total part replacement. This view is often suggested blindly, as a stab in the dark, but there is in fact an interesting argument in its favor. Kripke (1980) argues that a table made out of a particular hunk of wood *could not* have been made out of a (totally) different hunk of wood. His reasoning is this: Suppose that in the actual world a table $T$ is made out of a hunk of wood $H$; and suppose that there is a possible world $w$ in which this very table, $T$, is made out of a different hunk of wood, $H'$. Then assuming that $H$ and $H'$ are completely unrelated (for example, they do not overlap), so that making a table out of the one is not somehow dependent upon making a table out of the other, there is another possible world $w'$ in which $T$, as in the actual world, is made out of $H$, and another table $T'$, exactly similar to $T$, is made out of $H'$. Since $T$ and $T'$ are not identical in $w'$, it follows by ND that the table made out of $H'$ in $w$ is not $T$. Note, however, that the argument assumes that the table made out of $H'$ in $w'$ is the same table as the table made out of $H'$ in $w$.

Kripke’s reasoning can be applied to the present case (Kripke and others might dispute this claim; see below). Let $w$ be a possible world just like the actual world in that $O$, the original ship, is manufactured exactly as it is in the actual world. In $w$, however, another ship, $S'$, exactly similar to $O$, is simultaneously built out of precisely the same parts that $S$, the remodeled ship, is built out of in the actual world. Since $S'$ and $O$ are clearly different ships in $w$, it follows by ND that $O$ and $S$ are not the same ship in the actual world. Note again that the argument assumes that $S$ and $S'$ are the same ship, but it seems quite a stretch to deny that. Nevertheless, some have done so. Carter (1987) claims (in effect) that $S$ and $S'$ are not identical, but his argument simply *assumes* that $O$ and $S$ are the same ship. Alternatively, one might view the (Kripkean) argument as showing only that while $S$ is the same ship as $O$ in the actual world, $S$ (that is, $S')$ is not the same ship as $O$ in $w$. But this is not an option for one who adheres to the standard account and hence adheres to ND. In defending this view, however, Gallois (1986, 1988) suggests a weakened notion of rigid designation and a corresponding weakened formulation of ND. (See Carter 1987 for criticism of Gallois’ proposals. See also Chandler 1975 for a precursor of Gallois’ argument.)[^carter-1987][^chandler-1975]

If we grant that $O$ and $S$ cannot be the same ship, we seem to have a solution to the ship of Theseus paradox. By the Kripkean argument, only the reassembled ship has any claim to being the original ship, $O$. But this success is short-lived. For we are left with the following additional paradox: Suppose that $S$ eventuates from $O$ by replacing one part of $O$ one day at a time. There seems to be widespread agreement that replacing just one part of a thing by a new exactly similar part preserves the identity of the thing. If so, then, by the transitivity of identity, $O$ and $S$ must be the same ship. It follows that either the Kripkean argument is incorrect, or replacement of even a single part (or small portion) does not preserve identity (a view known as “mereological essentialism”; Chisholm 1973)[^chisholm-1973].

As indicated, Kripke denies that his argument (for the necessity of origin) applies to the case of change over time: “The question whether the table could have *changed* into ice is irrelevant here” (Kripke 1972, p. 351)[^kripke-1972]. So the question whether $O$ could change into $S$ is supposedly “irrelevant”. But Kripke does not give a reason for this claim, and if cases of trans-temporal identity and trans-world identity differ markedly in relevant respects—respects relevant to Kripke’s argument for the necessity of origin—it is not obvious what they are. (But see Forbes 1985, and Lewis 1986, for discussion.)[^forbes-1985][^lewis-1986] The argument above was simply that $O$ and $S$ cannot be the same ship since there is a possible world in which they differ. If this argument is incorrect it is no doubt because there are conclusive reasons showing that $S$ and $S'$ differ. Even so, such reasons are clearly not “irrelevant”. One may suspect that, if applied to the trans-temporal case, Kripke’s reasoning will yield an argument for mereological essentialism. Indeed, a trans-world counterpart of such an argument has been tried (Chandler 1976, though Chandler views his argument somewhat differently)[^chandler-1976]. In its effect, this argument does not differ essentially from the “paradox” sketched in the previous paragraph (which may well be viewed as an argument for mereological essentialism). Subsequent commentators, e.g., Salmon (1979) and Chandler (1975, 1976), do not seem to take Kripke’s admonition of irrelevance seriously.

In any case, there $is$ a close connection between the two issues (the ship of Theseus problem and the question of the necessity of origin). This can be seen (though it may already be clear) by considering a modified version of the ship of Theseus problem. Suppose that when $O$ is built, another ship $O'$, exactly like $O$, is also built. Suppose that $O'$ never sets sail, but instead is used as a kind of graphic repair manual and parts repository for $O$. Over time, planks are removed from $O'$ and used to replace corresponding planks of $O$. The result is a ship $S$ made wholly of planks from $O'$ and standing (in the end), we may suppose, in exactly the place $O'$ has always stood. Now do $O$ and $O'$ have equal claim to be $S$? And can we then declare that neither is $S$? Not according to the Kripkean line of thought. It looks for all the world as though the process of “remodeling” $O$ is really just an elaborate means of dismantling and reassembling $O'$. And if $O'$ and $S$ are the same ship, then since $O$ and $O'$ are distinct, $O$ and $S$ cannot be the same ship.

This argument is vulnerable to the following two important criticisms: First, it conflicts with the common sense principle that (1) the material of an object can be totally replenished or replaced without affecting its identity (Salmon 1979)[^salmon-1979]; and secondly, as mentioned, it conflicts with the additional common sense principle that (2) replacement by a single part or small portion preserves identity. These objections may seem to provide sufficient grounds for rejecting the Kripkean argument and perhaps restricting the application of Kripke’s original argument for the necessity of origin (Noonan 1983)[^noonan-1983]. There is, however, a rather striking problem with (2), and it is unclear whether the conflict between (1) and the Kripkean argument should be resolved in favor of the former.

The problem with (2) is this. Pick a simple sort of objects, say, shoes, or better, sandals. Suppose $A$ and $B$ are two exactly similar sandals, one of which $(A)$ is brand new and the other $(B)$ is worn out. Each consists of a top strap and a sole, nothing more. If $B$’s worn strap is replaced by $A$’s new one, (2) dictates that the resulting sandal is $B$ “refurbished”. In fact, if the parts of $A$ and $B$ are simply exchanged, (2) dictates that the sandal with the new parts, $A'$, is $B$ and the sandal with the old parts, $B'$, is $A$. It follows by ND that $A$ and $A'$ and $B$ and $B'$ are distinct. This is surely the wrong result. The intuition that $A$ and $A'$ are the same sandal is very strong; and the process of exchanging the parts of $A$ and $B$ seems to amount to nothing more than the dismantling and reassembling of each. This example is no different in principle than the more elaborate trans-world cases discussed by Chisholm (1967), Chandler (1976), Salmon (1979), or Gupta (1980). (One who claims that $A$ and $A'$ differ in that $A'$ comes into existence after $A$, does not have much to go on. $A$ cannot be supposed to persist after $A'$ comes into existence. We do not end up with two *new* sandals and one old one. Why then couldn’t it be $A$ itself that reappears at the later time?)

### 2.6 Church’s Paradox

The following paradox—perhaps the ultimate paradox of identity—derives from an argument of Church (1982). Suppose Pierre thinks that London and Londres are different cities, but of course doesn’t think that London is different from London, or that Londres is different from Londres. Assuming that proper names lack Fregean senses, we can apply LL to get the result that London and Londres *are* distinct. We have here an argument that, given the standard account of identity, merely *thinking* that $x$ and $y$ are distinct is enough to make them so. There are, of course, a number of ways around this conclusion without abandoning the standard account of identity. Church himself saw the argument (his version of it) as demonstrating the inadequacy of Russellian intensional logic—in which variables and constants operate as they do in extensional logic, i.e., unequipped with senses. (For another reaction, see Salmon 1986.)[^salmon-1986] But there are strong arguments against the view that names (or variables) have senses (Kripke 1980)[^kripke-1980]. In light of these arguments, Church’s argument may be viewed as posing yet another paradox of identity.

The general form of Church’s argument has been exploited by others to reach further puzzling conclusions. For example, it has been used to show that there can be no such thing as vague or “indeterminate” identity (Evans 1978; and for discussion, Parsons 2000)[^evans-1978][^parsons-2000]. For $x$ is not vaguely identical to $x$; hence, if $x$ is assumed to be vaguely identical to $y$, then by LL, $x$ and $y$ are (absolutely) distinct. As it stands, Evans’ argument shows at best that vaguely identical objects must be absolutely distinct, not that there is no such thing as vague identity. But some have tried to amend the argument to get Evans’ conclusion (Parsons 2000; and see the entry on vagueness)[^parsons-2000]. In any case, it is useful to see the connection between Evans’ argument and Church’s. If, for example, “vaguely identical” is taken to mean “thought to be identical”, then the two arguments collapse into one another. Church’s line of argument would seem to lead ultimately to the extreme antirealist position that any perceived difference among objects is a real difference. If one resolves not to attempt to escape the clutches of LL by some clever dodge—by disallowing straightforward quantifying-in, for example, as with the doctrine of Abelardian predicates—one comes quickly to the absurd conclusion that no statement of the form $x = y$, where the terms are different, or are just different tokens of the same type, can be true. Yet it might just be that the fault lies not in ourselves, but in LL.

### 2.7 The Theological Paradox

The Christian doctrine of Trinity is sometimes construed as a paradox that involves incongruent identity statements. For example, the Athanasian Creed puts it like this: “[…] we worship one God in Trinity. […] the Father is God; the Son is God; and the Holy Spirit is God. And yet they are not three Gods; but one God”. One may conceptually unbundle these statements into the following set of claims:

1. The Father is a God.
2. The Son is a God.
3. The Holy Spirit is a God.
4. The Father is not identical with the Son.
5. The Father is not identical with the Holy Spirit.
6. The Son is not identical with the Holy Spirit.
7. There is at most one God, i.e., if $x$ is a God and $y$ is a God, then $x$ is identical with $y$.

It is easy to see that this set is logically inconsistent and consequently one may claim that the doctrine itself is conceptually incongruent.

## 3. Relative Identity

The fundamental claim of relative identity—the claim the various versions of the idea have in common—is that, as it seems in the passenger/person case, it can and does happen that $x$ and $y$ are the same $F$ and (yet) $x$ and $y$ are not the same $G$. Now it is usually supposed that if $x$ and $y$ are the same $F$ ($G$ etc.), then that implies that $x$ and $y$ are $F$s $(G$s, etc.) If so, then the above schema is trivially satisfied by the case in which $x$ and $y$ are the same person but $x$ ($y$) is not a passenger at all. But let us resolve to use the phrase “$x$ and $y$ are different $G$s” to mean “$x$ and $y$ are $G$s and $x$ and $y$ are not the same $G$”. Then the nontrivial core claim about relative identity is that the following may well be true:

**(RI)**

$x$ and $y$ are the same $F$ but $x$ and $y$ are different $G$s.

RI is a very interesting thesis. It seems to yield dramatically simple solutions to (at least some of) the puzzles about identity. We appear to be in a position to assert that young Oscar and old Oscar are the same dog but nonetheless distinct “temporary” objects; that Oscar and Oscar^{−} are the same dog but different dog parts; that the same piece of clay can be now (identical to) one statue and now another; that London and Londres are the same city but different “objects of thought”, and so forth. Doubts develop quickly, however. Either the *same dog* relation satisfies LL or it does not. If it does not, it is unclear why it should be taken to be a relation of *identity*. But if it satisfies LL, then it follows, given that Oscar and Oscar^{−} are different dog parts, that Oscar^{−} is not the same dog part as Oscar^{−}. Furthermore, assuming that the *same dog part* relation *is* reflexive, it follows from the assumption that Oscar^{−} and Oscar^{−} are the same dog (and that LL is in force), that Oscar and Oscar^{−} are indeed the same dog part, which in fact they are not.

It may seem, then, that RI is simply incoherent. These arguments, however, are a bit too quick. On analysis, they show only that the following three conditions form an inconsistent triad:

1. RI is true (for some fixed predicates $F$ and $G)$.
2. Identity relations are equivalence relations.
3. The relation *x and y are the same F* figuring in (1) satisfies LL.

For suppose that the relation *x and y are the same G*, figuring in (1), is reflexive and that $x$ is a $G$. Then $x$ is the same $G$ as $x$. But according to (1), $x$ and $y$ are not the same $G$s; hence, according to (3), it is not the case that $x$ and $y$ are the same $F$; yet (1) asserts otherwise. Now, most relative identity theorists maintain that while identity relations are equivalence relations, they do not in general satisfy LL. However, according to at least one analysis of the passenger/person case (and others), the *same person* relation satisfies LL but the *same passenger* relation is not straightforwardly an equivalence relation (Gupta 1980)[^gupta-1980]. It should be clear though that this view is incompatible with the principle of the *identity of indiscernibles*: If $x$ and $y$ are different passengers, there must be, by the latter principle, some property $x$ possesses that $y$ does not. Hence if the *same person* relation satisfies LL, it follows that $x$ and $y$ are *not* the same person. For the remainder we will assume that identity relations are equivalence relations. Given this assumption (and assuming that the underlying propositional logic is classical—cf. Parsons 2000)[^parsons-2000], RI and LL are incompatible in the sense that within the framework of a single fixed language for which LL is defined, RI and LL are incompatible.

Yet the advocate of relative identity cannot simply reject any form of LL. There are true and indispensable instances of LL: If $x$ and $y$ are the same dog, then, surely, if $x$ is a Dalmatian, so is $y$. The problem is that of formulating and motivating *restricted* forms of LL that are nonetheless strong enough to bear the burden of identity claims. There has been little systematic work done in this direction, crucial though it is to the relative identity project. (See Deutsch 1997 for discussion of this issue.)[^deutsch-1997] There are, however, equivalence relations that do satisfy restricted forms of LL. These are sometimes called “congruence relations” and they turn up frequently in mathematics. For example, say that integers $n$ and $m$ are congruent if their difference $n - m$ is a multiple of 3. This relation preserves multiplication and addition, but not every property. The numbers 2 and 11 are thus congruent but 2 is even and 11 is not. There are also non-mathematical congruencies. For example, the relation *x and y are traveling at the same speed* preserves certain properties and not others. If objects $x$ and $y$ are traveling at the same speed and $x$ is traveling faster than $z$, the same is true of $y$. Such similarity relations satisfy restricted forms of LL. In fact, any equivalence relation satisfies a certain minimal form of LL (see below).

There are strong and weak versions of RI. The weak version says that RI has some (in fact, many) true instances but also that there are predicates $F$ such that if $x$ and $y$ are the same $F$, then, for any equivalence relation, $E$, whatsoever (whether or not an identity relation), $E(x,y)$. This last condition implies that the relation *x and y are the same F* satisfies LL. The relation $P$ defined so that $P(x,y)$ if and only if $H(x)$ and $H(y)$, where $H$ is some predicate, is an equivalence relation. Hence, if $H$ holds of $x$ but not of $y$, there is an equivalence relation (namely, $P(x,y))$ that fails to hold of $x$ and $y$. If we add that in this instance “$x$ and $y$ are the same $F$” is to be interpreted in terms of the relation $I(A,x,y)$, then the weak version of RI says that there is such a thing as relative identity and such a thing as absolute identity as well. The strong version, by contrast, says that there are (many) true instances of RI but there is no such thing as absolute identity. It is difficult to know what to make of the latter claim. Taken literally, it is false. The notion of unrestricted identity (in the sense of “unrestricted” explained in §1) is demonstrably coherent. We return to this matter in §5.

The puzzles about identity outlined in §2 (and there are many others, as well as many variants of these) put considerable pressure on the standard account. A theory of identity that allows for instances of RI is an attractive alternative (see below §4). But there is a certain kind of example of RI, frequently discussed in the literature, that has given relative identity something of a bad name. The passenger/person example is a case in point. The noun “passenger” is derived from the corresponding relational expression “passenger in (on) …”. A passenger is someone who is a passenger in some vehicle (on some flight, etc.). Similarly, a father is a man who fathers someone or who is the father of someone. This way of defining a kind of things from a relation between things is perfectly legitimate and altogether open-ended. Given any relation $R$, we can define “an $R$” to apply to anything $x$ that stands in $R$ to something $y$. For example, we can define a “schmapple” to be an apple in a barrel. All this is fine. But we can’t *infer* from such a definition that the same apple might be two different schmapples. From the fact that someone is the father of two different children, we don’t judge that he is two different fathers. The fact that airlines choose to count passengers as they do, rather than track persons, is their business, not logic’s.

However, when $R$ is an equivalence relation, we are entitled to such an inference. Consider the notorious case of “surmen” (Geach 1967)[^geach-1967]. A pair of men are the “same surman” if they have the same surname; and a surman is a man who bears this relation to someone. So now it appears that two different men can be the same surman, since two different men can have the same surname. As Geach (1967) insists (also Geach 1973)[^geach-1973], surmen are *defined* to be men, so they are not merely classes of men. Hence we seem to have an instance of RI, and obviously any similarity relation (e.g., $x$ and $y$ have the same shape) will give rise to a similar case. Yet such instances of RI are not very interesting. It is granted all around that when “$F$” is adjectival, different $G$s may be the same $F$. Different men may have the same surname, different objects the same color, etc. Turning an adjectival similarity relation into a substantival one having the form of an identity statement yields an identity statement in name only.

A word about the point of view of those who subscribe to the weak version of RI. The view (call it the “weak view”) is that ordinary identity relations concerning (largely) the world of contingency and change are equivalence relations answering to restricted forms of LL. The exact nature of the restriction depends on the equivalence relation itself, though there is an element of generality. The kinds of properties preserved by the *same dog* relation are intuitively the same *kinds* of properties as are preserved by the *same cat* relation. From a logical point of view the best that can be said is that any identity relation, like any equivalence relation, preserves a certain minimal set of properties. For suppose $E$ is some equivalence relation. Let $S$ be the set containing all formulas of the form $E(x,y)$, and closed under the formation of negations, conjunctions, and quantification. Then $E$ preserves any property expressed by a formula in $S$. Furthermore, on this view, although absolutely distinct objects may be the same $F$, absolutely identical objects cannot differ at all. Any instance of RI implies that $x$ and $y$ are absolutely distinct.

## 4. The Paradoxes Reconsidered

Let us look back at the paradoxes of identity outlined in §2 from the perspective of the weak view regarding relative identity. That view allows that absolutely distinct objects may be the same $F$, but denies that absolutely identical objects can be different $G$’s. This implies that if $x$ and $y$ are relatively different objects, then $x$ and $y$ are absolutely distinct, and hence only pairs of absolutely distinct objects can satisfy RI. If $x$ and $y$ are absolutely distinct, we shall say that $x$ and $y$ are distinct “logical objects”; and similarly, if $x$ and $y$ are absolutely identical objects, then $x$ and $y$ are identical logical objects. The term “logical object” does not stand for some new and special kind of thing. Absolutely distinct apples, for example, are distinct logical objects.

The following is the barest sketch of relativist solutions to the paradoxes of identity discussed in §2. No attempt is made to fully justify any proposed solution, though a modicum of justification emerges in the course of §6. It should be kept in mind that some of the strength of the relativist solutions derives from the weaknesses of the absolutist alternatives, some of which are discussed in §2.

### 4.1 The Paradox of Change

Young Oscar and old Oscar are the same dog but absolutely different things, i.e., different logical objects. The material conditions rendering young Oscar and old Oscar the same dog (and the same Dalmatian) are precisely the same as the material conditions under which young Oscar and old Oscar would qualify as temporal parts of the same dog. The only difference is *logical*. The identity relation between young Oscar and old Oscar can be formalized in an extensional logic (Deutsch 1997)[^deutsch-1997], but a theory of temporal parts requires a modal/temporal apparatus. Young Oscar is wholly present during his youth and possesses the simple, non-relational, property of not having a gray muzzle.

### 4.2 Chrysippus’ Paradox

Oscar and Oscar^{−} both survive Oscar’s loss of a tail. At both $t$ and $t'$ Oscar and Oscar^{−} are the same dog, but at $t$, Oscar and Oscar^{−} are distinct logical objects. This implies (by ND) that Oscar and Oscar^{−} are distinct logical objects even at $t'$ Hence, we must allow that distinct logical objects may occupy the same space at the same time. This is not a problem, however. For although Oscar and Oscar^{−} are distinct logical objects at $t'$, they are physically coincident.

### 4.3 The Paradox of 101 Dalmatians

The relativist denies that dogs are “maximal”. It is not true that no proper part of a dog is dog. All the 101 (and more) proper parts of Oscar differing from him and from one another by a hair are dogs. In fact, many (though of course not all) identity preserving changes Oscar might undergo correspond directly to proper parts of (an unchanged) Oscar. But there is no problem about barking in unison, and no problem about acting independently. All 101 are the same dog, despite their differences, just as young Oscar and old Oscar are the same dog. The relativist denies that the dogs are many rather than deny that the many are dogs (Lewis 1993)[^lewis-1993].

### 4.4 The Paradox of Constitution

Constitution is identity, *absolute* identity. The relation between the piece of clay $c$ and the statue $s_1$ on day 1 is one of absolute identity. So we have that $c = s_1$ on day 1, and for the same reason, $c = s_2$ on day 2. Furthermore, since $s_1$ and $s_2$ are different statues, it follows (on the weak view) that $s_1\ne s_2$. In addition, the piece of clay $c$ constituting $s_1$ on day 1 is (relatively) the same piece of clay as the piece of clay constituting $s_2$ on day 2. (The identity is relative because we have distinct objects—the two statues—that are the same piece of clay.) It follows that *no name of the piece of clay c can be a rigid designator in the standard sense*. That is, no name of $c$ denotes absolutely the same thing on day 1 and on day 2. For on day 1, a name of the piece of clay $c$ would denote $s_1$ and on day 2, it would denote $s_2$, and $s_1$ and $s_2$ are absolutely distinct. Nevertheless, a name of the piece of clay may be *relatively rigid*: it may denote at each time the *same piece of clay*. Although no name of the piece of clay $c$ is absolutely rigid, that does not prevent the introduction of a name of $c$ that denotes $c$ at any time (or possible world). (Kraut 1980 discusses a related notion of relative rigidity.)[^kraut-1980]

There is, however, a certain ambiguity in the notion of a name of the piece of clay, inasmuch as the piece of clay may be any number of absolutely distinct objects. The notion of relative rigidity presupposes that a name for the piece of clay refers, with respect to some parameter $p$, to whatever object counts as the piece of clay relative to that parameter. This may be sufficient in the case of the piece of clay, but in other cases it is not. With respect to a fixed parameter $p$ there may be no unique object to serve as the referent of the name. For example, if any number of dog parts count, at a fixed time, as the same dog, then which of these objects serves as the referent of “Oscar”? We shall leave this question open for the time being but suggest that it may be worthwhile to view names such as “Oscar” as *instantial* terms—terms introduced into discourse by means of existential instantiation. The name “Oscar” might be taken as denoting a representative member of the equivalence class of distinct objects qualifying as the same dog as Oscar. It would follow, then, that most ordinary names are instantial terms. (An alternative is that of Geach 1980, who draws a distinction between a *name of* and a *name for an* object; see Noonan 1997 for discussion of Geach’s distinction.)[^geach-1980][^noonan-1997]

### 4.5 The Ship of Theseus Paradox

In this case, the relativist, as so far understood, may seem to enjoy no advantage over the absolutist. The problem is not clearly one of reconciling LL with ordinary judgments of identity, and the advantage afforded by RI does not seem applicable. Griffin (1977), for example, relying on RI, claims that the original and remodeled ship are the same ship but not the same collection of planks, whereas the reassembled ship is the same collection of planks as the original but not the same ship. This simply doesn’t resolve the problem. The problem is that the reassembled and remodeled ships have, *prima facie*, equal claim to be the original and so the bald claims that the reassembled ship is not—and the remodeled ship is—the original are unsupported. The problem is that of reconciling the intuition that certain small changes (replacement of a single part or small portion) preserve identity, with the problem illustrated by the sandals example of §2.5. It turns out, nevertheless, that the problem $is$ one of dealing with the excesses of LL. To resolve the problem, we need an additional level of relativity. To motivate this development, consider the following abstract counterpart of the sandals example:

On the left there is an object $P$ composed of three parts, $P_1, P_2$, and $P_3$. On the right is an exactly similar but non-identical object, $Q$, composed of exactly similar parts, $Q_1, Q_2$, and $Q_3$, in exactly the same arrangement. For the sake of illustration, we adopt the rule that only replacement of (at most) a *single* part by an exactly similar part preserves identity. Suppose we now interchange the parts of $P$ and $Q$. We begin by replacing $P_1$ by $Q_1$ in $P$ and replacing $Q_1$ by $P_1$ in $Q$, to obtain objects $P^1$ and $Q^1$. So $P^1$ is composed of parts $Q_1,$ $P_2,$ and $P_3$, and Q$^1$ is composed of parts $P_1,$ $Q_2,$ and $Q_3$. We then replace $P_2$ in $P^1$ by $Q_2$, to obtain $P^2$, and so on. Given our sample criterion of identity, and assuming the transitivity of identity, $P$ and $P^3$ are counted the same, as are $Q$ and $Q^3$. But this appears to be entirely the wrong result. Intuitively, $P$ and $Q^3$ are the same, as are $Q$ and $P^3$. For $P$ and $Q^3$ are composed of exactly the same parts put together in exactly the same way, and similarly for $Q$ and $P^3$. Furthermore, $Q_3 (P_3)$ can be viewed as simply the result of taking $P (Q)$ apart and putting *it* back together in a slightly different location. And this last difference can be eliminated by switching the locations of $P^3$ and $Q^3$ as a last step in the process.

Suppose, however, that we replace our criterion of identity by the following more complicated rule: $x$ and $y$ are the same *relative to z*, if both $x$ and $y$ differ from $z$ at most by a single part. (This relation is transitive, and is in fact an equivalence relation.) For example, *relative to* $P$, $P, P^1, Q^2$, and $Q^3$ are the same, but $Q, Q^1, P^2$ and $P^3$, are not. Of course, replacement by a single part is an artificial criterion of identity. In actual cases, it will be a matter of the degree or kind of deviation *from the original* (represented by the third parameter, $z)$. The basic idea is that identity through change is not a matter of identity through successive, accumulated changes—that notion conflicts with both intuition (e.g., the sandals example) and the Kripkean argument: Through successive changes objects can evolve into *other* objects. The three-place relation of identity does not satisfy LL and is consistent with the outlook of the relativist. Gupta (1980) develops a somewhat similar idea in detail. Williamson (1990) suggests a rather different approach, but one that, like the above, treats identity through change as an equivalence relation that does not satisfy LL.

### 4.6 Church’s Paradox

Church’s argument implies that if Pierre’s doxastic position is as described (in §2.6), then London and Londres are distinct objects. Assuming the standard account of identity, the result is that either Pierre’s doxastic position *cannot* be as described or else London and Londres are different *cities* (or else we must punt). Since London and Londres are not different cities, the standard account entails that Pierre’s doxastic position cannot be as described (or else we must punt). This was Church’s own position as regards certain puzzles about synonymy, such as Mates’ puzzle (Mates 1952)[^mates-1952]. Church held that one who believes that lawyers are lawyers, must indeed believe that lawyers are attorneys, despite any refusal to assent to (or desire to dissent from) “Lawyers are attorneys” (Church 1954)[^church-1954]. Kripke later argued (Kripke 1979)[^kripke-1979] that assent and failure to assent must be taken at face value (at least in the case of Pierre) and Pierre’s doxastic position is as described. Kripke chose to punt—concluding that the problem is a problem for any “logic” of belief. The relativist concludes instead that (a) Pierre’s doxastic position is as described, (b) if so, London and Londres are distinct objects, and (c) London and Londres are nonetheless the same city. Whether this resolution of Church’s paradox can be exploited to yield solutions to Frege’s puzzle (Salmon 1986)[^salmon-1986] or Kripke’s puzzle (1979) remains to be seen. Crimmins (1998) has suggested that the analysis of propositional attitudes requires a notion of “semantic pretense”. In reporting Pierre’s doxastic position we engage in a pretense to the effect that London and Londres are different cities associated with different Fregean senses. Crimmins’ goal is to reconcile (a), (c) and the following, (d): that the pure semantics of proper names (“London”, “Londres”) is Millian or directly referential (Kripke 1979)[^kripke-1979]. The relativist proposes just such a reconciliation but suggests that the pretense can be dropped.

### 4.7 The Theological Paradox

The solution provided by RI is straightforward: we need to state the doctrine not in terms of absolute identity, but in terms of relative identity. So instead of one predicate of absolute identity the trinitarian creed may need two predicates of relative identity, e.g., being the same person and being the same being (cf. van Inwagen 1988, 2003), or, as suggested by (Anscombe and Geach 1961)[^anscombe-1961], being the same person and being the same God. Then we may reformulate the creed as follows:

1. The Father is a God.
2. The Son is a God.
3. The Holy Spirit is a God.
4. The Father is not the same person as the Son.
5. The Father is not the same person as the Holy Spirit.
6. The Son is not the same person as the Holy Spirit.
7. There is at most one God, i.e., if $x$ is a God and $y$ is a God, then $x$ is the same being as $y$.

Van Inwagen produced a model (in the sense of formal semantics) where all these statements are satisfied, so under this interpretation the doctrine of Trinity comes out consistent. Incidentally let me note that he also gave an analogous interpretation for the doctrine of Incarnation (see van Inwagen 1994). For an extended discussion of the coherence of this solution see the section on relative identity theories in the entry on Trinity. Note that Branson (2019) provides a taxonomy of all possible solutions to the paradox, including the ones that resort to relative identity.

## 5. Absolute Identity

The philosopher P.T. Geach first broached the subject of relative identity and introduced the phrase “relative identity”. Over the years, Geach suggested specific instances of RI (a variant of the case of Oscar and his tail is due to Geach 1980)[^geach-1980] and in this way he contributed to the development of the weak view concerning relative identity, i.e., the view that while ordinary identity relations are often relative, some are not. But Geach maintains that absolute identity does not exist. What is his argument?

That is hard to say. Geach sets up two strawman candidates for absolute identity, one at the beginning of his discussion and one at the end, and he easily disposes of both. In between he develops an interesting and influential argument to the effect that identity, *even as formalized in the system* FOL⁼, is relative identity. However, Geach takes himself to have shown, by this argument, that absolute identity does not exist. At the end of his initial presentation of the argument in his 1967 paper, Geach remarks:

> We thought we had a criterion for a predicable’s expressing strict identity [i.e., as Geach says, “strict, absolute, unqualified identity”]; but the thing has come apart in our hands; and no alternative rigorous criterion that could replace this one has thus far been suggested. (Geach 1967, p. 6 [1972, p. 241])[^geach-1967]

It turns out, as we’ll see, that all that comes apart is the false notion that in FOL⁼ the identity symbol *defines* the relation $I(A,x,y)$. Let us examine Geach’s line of reasoning in detail, focusing on the presentation in his 1967 article, the *locus classicus* of the notion of relative identity.

Geach begins by urging that a plain identity statement “$x$ and $y$ are the same” is in need of a completing predicate: “$x$ and $y$ are the same $F$”. Frege had argued that statements of number such as “this is one” require a completing predicate: “this is one $F$”, and so it is, Geach claims, with identity statements. This is a natural view for one who subscribes to RI. The latter cannot even be stated without the completing predicates. Nevertheless, both the claim itself and the analogy with Frege have been questioned. Some argue that the analogy with Frege is incorrect. For example, Carrara and Sacchi (2007) maintain that Frege’s position that any ascription of a number to something is always relative to a concept boils down to the claim that concepts are essential in cardinality statements because without them there is no specification of what is to be counted. Once this is settled, Frege would count by means of absolute identity. Others argued that while the analogy is correct, both Frege and Geach are wrong (Perry 1978 and Alston and Bennett 1984)[^alston-1984][^perry-1978]. These matters do not bear directly on the question of the coherence and truth of RI or the question of absolute identity. One who adopts the weak view would not want to follow Geach on this score. And one could maintain the “completing thesis” without being committed to RI. Furthermore, the completing thesis occupies a puzzling role in Geach’s dialectic. Immediately following his statement of the thesis, Geach formalizes FOL⁼ on the basis of the single formula:

**(R)**

$\phi(a) \leftrightarrow \exists x(\phi(x) \wedge x = a)$

(The “W” is for Hao Wang, who first suggested it. The reader is invited to prove Ref and LL from W.) But we hear no complaint about the syntax of W despite its involving a seemingly unrelativized identity symbol. It turns out, however, that Geach apparently thinks of the completing predicate as being given by the whole descriptive apparatus of $L$ or a fragment thereof.

Geach now observes

> … if we consider a moment, we see that an I-predicable in a given theory *T* *need not* express strict, absolute, unqualified identity; it need mean no more than that two objects are indiscernible by the predicables that form the descriptive resources of the theory—the *ideology* of the theory …. (1967, p. 5 [1972, p. 240])

Here an “I-predicable” is a binary relation symbol “=” satisfying (W). Geach’s focus at this point is on the need to relativize an I-predicable to a theory $T$. Geach then immediately saddles the friend of absolute identity with the view that for “real identity” we need not bring in the ideology of a definite theory. This is Geach’s first strawman. When logicians, in discussing FOL⁼, speak of “real identity”—and they often do (see Enderton 2000 or Silver 1994, for example)[^enderton-2000][^silver-1994]—they do not mean a relation of *universal identity*, since the universal set does not exist. Nor do they intend, in formulating LL, to use “true of” in a completely unrestrained way which gives rise to semantic paradox. It is no argument against those who wish to distinguish mere indiscernibility from real identity to say that they “will soon fall into contradictions”, e.g., Grelling’s or Russell’s. The relation $I(A,x,y)$ is sufficiently relativized. (It is relativized to a *set A*.)

We come next to the main point:

> Objects that are indiscernible when we are confined to the ideology of $T$ may perfectly well be discernible in the ideology of a theory $T^1$ of which $T$ is a fragment. (Geach 1967, p. 5 [1972, p. 240])[^geach-1967]

The warrant for this claim can only be the language relativity of identity when treated as a non-logical notion (see §1). That this is what Geach has in mind is clear from some approving remarks he makes in his 1973 article about Quine’s (1970) proposal to treat identity as a non-logical notion. But how does it follow that absolute identity does not exist? Geach seems to think that the defender of absolute identity will look to Ref and LL (or W)—and not beyond—for a full account of “strict, absolute, unqualified” identity. That is not so. The fact that these formulas in themselves define only indiscernibility relations is a logical commonplace. So this is Geach’s second strawman.

Is Geach’s argument at least an argument that identity is relative? Does language relativity support the conclusion that RI is true even of identity as formalized in FOL⁼? The general idea appears to be that language relativity suggests that we take identity *to be* indiscernibility, and conclude that objects identical relative to one ideology $F$ may be different relative to another ideology $G$, and that this confirms RI. Notice first of all that this argument relies on the identity of indiscernibles: that indiscernibility implies identity. This principle is not valid in FOL⁼ even when the latter is treated as a proper theory. Language relativity does not imply that the distinctness of distinct objects cannot go unnoticed.

Secondly, the interesting cases of RI do not involve a shift from an impoverished point of view to an improved one—whether this is seen in epistemic terms (which Geach disputes—Geach 1973)[^geach-1973] or in purely logical terms. We do not affirm that old Oscar and young Oscar, for example, are the same dog on the grounds that there is an ideology with respect to which old Oscar and young Oscar are indistinguishable. Such an ideology would be incapable of describing any change in Oscar. It is true that the *same dog* relation determines a set of predicates that do not discriminate between the members of certain pairs of dogs—the dogs in the photographs mentioned earlier, for example. And it is true that these predicates determine a sublanguage in which the *same dog* relation is a congruence, i.e., no predicate of the sublanguage distinguishes $x$ from $y$, if $x$ and $y$ are the same dog. But the very *sense* of such statements as that old Oscar and young Oscar are the same dog requires a language in which a change in Oscar is expressible. We are talking, after all, about *old* Oscar and *young* Oscar. If we take seriously the idea that change involves the application of incompatible predicates, then the sublanguage cannot express the contrast between old Oscar and young Oscar.

Third, the phenomenon of language relativity (in the technical sense discussed in §1) has led many philosophers, including Geach, to the view that ideology creates ontology. There is no antecedently given domain of objects, already individuated, and waiting to be described. Instead, theories carve up the world in various ways, rendering some things noticeably distinct and others indiscernible, depending on a theory’s descriptive resources. The very notion of *object* is theory-bound (Kraut 1980)[^kraut-1980]. This sort of anti-realism may seem to go hand in hand with relative identity. Model theory, however, is realist to its core and language relativity is a model-theoretic phenomenon. It is a matter of definability (in a structure). Referring back to §1, in order to make sense of language relativity we have to start with a pair of *distinct* objects, $a$ and $b$ (distinct from the standpoint of the metalanguage), and hence a pair of objects we assume are already individuated. These objects, however, are indistinguishable in $M$, since no formula of $L'$ defines a subset of $M$ containing the one object and not the other. When we move to $M'$, we find that there is a formula of the enriched language that defines such a subset in $M'$. Thus, language relativity is not really any sort of relativity of *identity* at all. We must assume that the objects $a$ and $b$ are distinct in order to *describe* the phenomenon. If we are living in $M$, and suspect that Martians living in $M'$ can distinguish $a$ from $b$, our suspicion is not merely to the effect that Martians carve things up differently than we do. Our own model theory tells us that there is more to it than that. Our suspicion must be to the effect that $a$ and $b$ *are* absolutely distinct. If we are blind to the difference between $a$ and $b$, but the Martians are not, then there must be a difference; and even if we are living in $M$, we know there’s a difference, or at least we can suspect there is, since model theory tells us that such suspicion is well founded.

Let us go back to Geach’s remark that we “*need not*” interpret identity absolutely. While this is true, we need not interpret it as indiscernibility either. There are always the quotient structures (Quine 1963)[^quine-1963]. Instead of taking our “reality” to be $M$, and our “identity” to be indiscernibility in $M$, we can move to the quotient structure, $\textit{QM}$, whose elements are the equivalence classes, $[x]$, for $x$ in $M$. If $x$ and $y$ are indiscernible in $M$, then in $\textit{QM}$, $[x]$ and [$y$] are absolutely identical. We can do this even if we wish to treat FOL⁼ as a proper theory. For example, suppose $L'$ is a language in which people having the same income are indiscernible. The domain of $M$ now consists of people. $\textit{QM}$, however, consists of income groups, equivalence classes of people having the same income, and identity in $\textit{QM}$ is absolute. Geach objects to such reinterpretation in terms of the quotient structures on the grounds that it increases the ontological commitments not only of $L'$ but of any language of which $L'$ is a sublanguage.

Let’s focus on $L'$ first. From a purely model-theoretic point of view the question is moot. We cannot deny that $\textit{QM}$ is a structure for $L'$. Thus, $L'$ is committed to people *vis à vis* one structure and to income groups *vis à vis* the corresponding quotient structure. But let’s pretend that the structures are “representations of reality”, and so the question now becomes: Which representation is preferable? Is there then any reason to prefer the ontology of $M$ to that of $\textit{QM}$? $M$ contains people but no sets of people, whereas $\textit{QM}$ contains sets of people but no people. By Quine’s criterion of ontological commitment—that to be is to be the value of a variable—commitment to a set of objects does not carry a commitment to its elements. That is one of the odd consequences of Quine’s criterion. Unless there is some ontological reason to prefer people to sets of people (perhaps because sets are never to be preferred), the ontologies of $M$ and $\textit{QM}$ seem pretty much on a par. Both commit $L'$ to one kind of thing.

Geach makes the additional claim that the ontological commitments of a sublanguage $L'$ of a language $L$ are inherited by $L$ (Geach 1973)[^geach-1973]. Suppose then that $L$ is a language containing expressions for several equivalence relations defined on people: say, *same income*, *same surname*, and *same job*. Geach argues that $L$ need only be committed to the existence of people. Things such as income groups, job groups (equivalence classes of people with the same job), and surmen can all be counted using the equivalencies, without bringing surmen, job groups, and income groups into the picture. Consider any sublanguage for which any one of these equivalence relations is a congruence, i.e., for which $\textrm{LL}'$ holds. Pick the language, $L_1$, for example, in which people having the same job are indiscernible. More precisely, we assume that $T_1$ is the pure theory with identity whose ideology is confined to the language $L_1$. Let $M_1$ be a model of $T_1$. We may imagine the domain of $M_1$ to consist of people, and we can interpret indiscernibility in $M_1$ to be the relation *x and y have the same job*. Geach would argue that if $L_1$ is committed to the elements of $\textit{QM}_1$—the job groups—then so is $L$. But that is not true. If $T$ is a theory of the three distinct equivalence relations formulated in $L$, the most $T$ (or $L)$ would be committed to are the partitions determined by the equivalence relations; and in any case, it would be perfectly consistent to insist that, whatever the ontological commitments of $L_1$, reality, as described by $L$, consists of people.

The foregoing considerations are rather abstract. To see more clearly what is at stake, let us focus on a specific example. Geach (1967) mentions that rational numbers are defined set-theoretically to be equivalence classes of integers determined by a certain equivalence relation defined on “fractions”, i.e., ordered pairs of integers (1/2 is $\langle 1,2\rangle$, 2/4 is $\langle 2,4\rangle$, etc.). He suggests that we can instead construe our theory of rational numbers to be about the fractions themselves, taking the I-predicable of our theory to be the following equivalence relation, $E$:

$$\tag{R} E(\langle x,y\rangle, \langle u,v\rangle) \text{ iff } xv = yu. $$

This approach, Geach says, would have “the advantage of lightening a theory’s set-theoretical burdens. (In our present example, we need not bring in *infinite sets* of ordered pairs of integers into the theory of rationals.)” (Geach 1972, p. 249)[^geach-1972]

The first thing to notice about this example is that *E cannot* be the I-predicable of such a theory, since $E$ is *defined* in terms of identity (look at the right side of R). It is “=” that must serve as the I-predicable, and it renders distinct ordered pairs of integers discernible. The moral is that not all equivalence relations can be drafted to do the job of identity, even given a limited ideology. There is, indeed, a plausible argument that *any* equivalence relation presupposes identity—not necessarily in the direct way illustrated by (R), but indirectly, nonetheless (see §6). Moreover, from the standpoint of general mathematics, once we have (R), we have the (infinite) equivalence classes it determines and the partition it induces. These are inescapable. Even from a more limited viewpoint, it seems that once we have enough set theory to give us ordered pairs of integers and the ability to define (R), we get the partition it induces as well.

Geach perceives an ontological advantage in relative identity; but his argument is unconvincing. Shifting to the quotient structures, as Quine suggested, does not induce a “baroque, Meinongian ontology” (Geach 1967, p. 10 [1972, p. 245])[^geach-1967]. In particular, the “home language” $(L)$ does not inherit the commitment of the fragment $(L_1)$, and the ontology of an arbitrary model of the pure theory of identity based on the latter language is at least no more various than that of the corresponding quotient model. There are, however, a number of ways in which relative identity does succeed in avoiding commitment to certain entities required by its absolute rival. These are discussed in the replies to objections 4 and 5 in the next section.

## 6. Objections and Replies

The following constitute a “start-up” set of objections and replies concerning relative identity and/or aspects of the foregoing account of relative identity and its rival. Time and space constraints prevent a more extended initial discussion. In addition, there is no presumption that the objections discussed below are the most important or that the initial replies to them are without fault. It is hoped that the present discussion will evolve into a more full-blown one, involving contributions by the author and readers alike. Should the discussion become lengthy, old or unchallenged objections and/or replies can be placed in the archives.

**Objection 1**: “Relativist theories of identity, all of which are inconsistent with Leibniz’s principle [LL], currently enjoy little support. The doubts about them are (a) whether they really are theories of numerical identity, (b) whether they can be made internally consistent, and (c) whether they are sufficiently motivated” (Burke 1994, p. 133)[^burke-1994].

**Reply**: In reverse order: (c) The issues discussed in §2 and §4 surely provide sufficient motivation. (b) No proof of inconsistency has ever been forthcoming from opponents of relative identity, and in fact the weak view is consistent inasmuch as it has a model in the theory of similarity relations. The arguments outlined in the second paragraph of §3 are frequently cited as showing that relative identity is incoherent; but they show only that RI is incompatible with (unrestricted) LL. (a) See the replies to objections 2 and 3 below.

**Objection 2**: If an identity relation obeys only a restricted form of LL—if it preserves only *some* properties and not *all*—then how do we *tell* which properties serve to individuate a pair of distinct objects?

**Reply**: Similarity relations satisfy only restricted forms of LL. How then do we *tell* which properties are preserved by the *same shape* relation and which are not? It is no objection to the thesis that identity relations in general preserve some properties and not others to demand to know which are which. At best the objection points to a problem we must face anyway (for the case of similarity). In general, a property is preserved by an equivalence relation if it “spreads” in an equivalence class determined by the relation: If one member of the class has the property, then every member does. Every property spreads in a singleton, as absolute identity demands.

**Objection 3**: If identity statements are mere equivalencies, what distinguishes identity from mere similarity?

**Reply**: The distinction between identity and similarity *statements* (or sentences) is usually drawn in terms of the distinction between substantival and adjectival common nouns. If $F$ is a common noun standing for a kind of *things*, e.g., “horse”, then “$x$ and $y$ are the same $F$” is a statement of identity, whereas if $F$ is an a common noun standing for a kind of *properties* of things, then “$x$ and $y$ are the same $F$” is a statement of similarity. (It’s interesting to note that when the noun is proper, i.e., a proper name, the result is a statement of similarity, not identity—as in “He”s not the same Bill we knew before’.) This distinction rests ultimately on the metaphysical distinction between substance and attribute, object and property. While the distinction no doubt presupposes the concept of individuation (the bundle theory, for example, presupposes that we have the means to individuate properties), there is no obvious reason to suppose that it entails the denial of RI, i.e., the claim that no instance of RI is true. For a beginner’s review—from an historical perspective—of the issues concerning substance and attribute, see O’Connor (1967); and for more recent and advanced discussion and bibliography, see the entry on properties.

**Objection 4**: Consider the following alleged instance of RI:

**(1)**

$A$ is the same word type as $B$, but $A$ and $B$ are different word tokens.

“If ‘$A$’ and ‘$B$’ refer to the same objects throughout (1), the first conjunct of (1) is not an identity statement, and the counterexample (to the thesis that no instance of RI is true) fails. If both conjuncts are identity statements in the required sense, ‘$A$’ and ‘$B$’ must refer to word types in the first conjunct and word tokens in the second, and the counterexample fails” (Perry 1970, p. 189)[^perry-1970].

**Reply**: First, if “in the required sense” means “satisfies LL”, then the objection buys correctness only at the price of begging the question. Advocates of relative identity will maintain that the relation *A is the same word type as* $B$ is an identity relation, defined on tokens, that does not satisfy LL.

Secondly, even if one insists that in this case intuition dictates that if $A$ and $B$ refer to tokens in both conjuncts of (1), then “$A$ is the same word type as $B$” expresses only the similarity relation: *A and B are tokens of the same type*, there are other cases where, intuitively, both conjuncts of RI involve identity relations and yet the relevant terms all refer to the same kind of things; for example,

**(2)**

$A$ and $B$ are the same dog but $A$ and $B$ are different physical objects,

as said of young Oscar and old Oscar. Here there is no temptation to suppose that the relation *A and B are the same dog* is *not* an identity relation. One may invoke a theory—a theory of temporal parts, for example—that construes the relation as a certain kind of similarity, but that is theory, not pretheoretical intuition. It is no objection to the relativist’s *theory*, which holds in part that “$A$ and $B$ are the same dog” expresses a relation of primitive identity, that there is an alternative theory according to which it expresses a similarity relation obtaining between two temporal parts of the same object. Furthermore, in the case of (2), $A$ and $B$ refer, again intuitively, to the same things in both conjuncts.

Third, there are cases in which the relative identity view does possess an ontological advantage. Consider

**(3)**

$A$ and $B$ are the same piece of clay but $A$ and $B$ are different statues.

Suppose $A$ and $B$ are understood to refer to one sort of thing—pieces of clay—in the first conjunct and another—statues—in the second conjunct. Assume that the piece of clay $c$ denoted by $A$ in the first conjunct constitutes, at time $t$, the statue $s.$ Then assuming that statues are physical objects, there are two distinct physical objects belonging to different kinds occupying the same space at $t$. Some, notably Wiggins (1980), hold that this is entirely possible: Distinct physical objects may occupy the same space at the same time, provided they belong to different kinds. The temporal parts doctrine supports and encourages this view. A statue may be a temporal part of a temporally extended piece of clay. But one statue, it seems, cannot be a temporal part of another. Even so, however, the duality of constituter and thing constituted is unparsimonious (cf. Lewis 1993)[^lewis-1993], and the relativist is not committed to it.

Again, consider

**(4)**

$A$ and $B$ are the same book but $A$ and $B$ are different copies (of the book).

One can say that in the first conjunct, $A$ and $B$ refer to books (absolutely the same book), whereas in the second conjunct, $A$ and $B$ refer to (absolutely distinct) copies. But the alleged duality of books and copies of books is unparsimonious and the relativist is not committed to it. There is no reason to concede to the philosopher that we do not actually purchase or read *books*; instead we purchase and read only *copies* of books. Any copy of a book is just as much the “book itself” as is any other copy. Any copy of a book is *the same book* as any other copy. Nelson Goodman once remarked that “Any accurate copy of the text of a poem or novel is as much the original work as any other” (Goodman 1968, p. 114)[^goodman-1968]. Goodman was not suggesting that the distinction between poem and copy collapses. If it does collapse, however, we have an explanation of why any accurate copy is as much the original work as any other: any such copy is the same work as any other.

**Objection 5**: Geach remarks that “[a]s for our recognizing relative identity predicables: any equivalence relation … can be used to specify a criterion of relative identity” (Geach 1972, p. 249)[^geach-1972]. But §3 above contains a counterexample. Some equivalence relations are defined in terms of the I-predicable of a theory and hence cannot serve as such. (Any pair of I-predicables for a fixed theory are equivalent.) In fact it seems that any equivalence relation presupposes identity (cf. McGinn 2000)[^mcginn-2000]. For example, the relation *x and y are the same color* presupposes identity of colors, since it means that there are colors $C$ and $C'$ such that $x$ has $C$ and $y$ has $C'$, and $C = C'$. Identity, therefore, is logically prior to equivalence.

**Reply:** This is a good objection. It does seem to show, as the objector says, that identity is logically prior to ordinary similarity relations. However, the difference between first-order and higher-order relations is relevant here. Traditionally, similarity relations such as *x and y are the same color* have been represented, in the way indicated in the objection, as higher-order relations involving identities between higher-order objects (properties). Yet this treatment may not be inevitable. In Deutsch (1997), an attempt is made to treat similarity relations of the form “$x$ and $y$ are the same $F$” (where $F$ is adjectival) as primitive, first-order, purely logical relations (see also Williamson 1988)[^williamson-1988]. If successful, a first-order treatment of similarity would show that the impression that identity is prior to equivalence is merely a misimpression—due to the assumption that the usual higher-order account of similarity relations is the only option.

**Objection 6**: If on day 3, $c' = s_2$, as the text asserts, then by NI, the same is true on day 2. But the text also asserts that on day 2, $c = s_2$; yet $c \ne c'$. This is incoherent.

**Reply:** The term $s_2$ is not an absolutely rigid designator and so NI does not apply.

**Objection 7**: The notion of relative identity is incoherent: “If a cat and one of its proper parts are one and the same cat, what is the mass of that one cat?” (Burke 1994, p. 138)[^burke-1994].

**Reply**: Young Oscar and Old Oscar are the same dog, but it makes no sense to ask: “What is the mass of that one dog”? Given the possibility of change, identical objects may differ in mass. On the relative identity account, that means that distinct logical objects that are the same $F$ may differ in mass—and may differ with respect to a host of other properties as well. Oscar and Oscar^{−} are distinct physical objects, and therefore distinct logical objects. Distinct physical objects may differ in mass.

**Objection 8**: We can solve the paradox of 101 Dalmatians by appeal to a notion of “almost-identity” (Lewis 1993)[^lewis-1993]. We can admit, in light of the “problem of the many” (Unger 1980)[^unger-1980], that the 101 dog parts are dogs, but we can also affirm that the 101 dogs are not many; for they are “almost one”. Almost-identity is not a relation of indiscernibility, since it is not transitive, and so it differs from relative identity. It is a matter of negligible difference. A series of negligible differences can add up to one that is not negligible.

**Reply**: The difference between Oscar and Oscar^{−} is not negligible and the two are not almost-identical. Lewis concedes this point but proposes to combine almost-identity with supervaluations to give a mixed solution to the paradox. The supervaluation solution starts from the assumption that one and only one of the dog parts is a dog (and a Dalmatian, and Oscar), but it doesn’t matter which. It doesn’t matter which because we haven’t decided as much, and we aren’t going to. Since it is true that any such decision renders one and only one dog part a dog, it is plain-true, i.e., supertrue, that there is one and only one dog in the picture. But it is not clear that this approach enjoys any advantage over that of relative identity; in fact, it seems to produce instances of RI. Compare: Fred’s bicycle has a basket attached to it. Ordinarily, our discourse slides over the difference between Fred’s bicycle with its basket attached and Fred’s bicycle minus the basket. (In this respect, the case of Fred’s bicycle differs somewhat from that of Oscar and Oscar^{−}. We tend not to ignore *that* difference.) In particular, we don’t say that Fred has two bicycles even if we allow that Fred’s bicycle-minus is a bicycle. Both relative identity and supervaluations validate this intuition. However, both relative identity and supervaluations also affirm that Fred’s bicycle and Fred’s bicycle-minus are absolutely distinct objects. That is, the statement that Fred’s bicycle and Fred’s bicycle-minus are distinct is supertrue. So the supervaluation technique affirms both that Fred’s bicycle and Fred’s bicycle-minus are distinct objects *and* that there is one and only one (relevant) bicycle. That is RI, or close enough. The supervaluation approach is not so much an alternative to relative identity as a form of it.

**Objection 9**: One may argue that the plausibility of RI rests to a large degree on certain linguistic phenomena and that we do not need it after all because these phenomena are in fact apparent and the notion of relative identity can be explained away. For example, Moltmann (2013) has recently argued that some apparent statements of sortal-relative identity can be analysed on linguistic grounds as statements of absolute identity. Consider an example of such statements: “This is the same lump of clay but not the same statue as that”, which is uttered in front of, say, two photographs: one presenting the clay and the other showing the statue made out of the clay. Moltmann starts her analysis focussing on the two pronouns at stake: *this* and *that*, the so-called bare demonstratives. The analysis reveals two different functions thereof: referential and presentational. Due to the referential function a bare demonstrative picks up a unique feature, or a trope as Moltmann claims. Secondly, this feature (trope) is used to recognise its bearer (in any possible world that is accessible from the world where the pronoun is uttered). Now in the example above *this* refers to a complex trope, say the complex composed of this particular brownness and this roundness, and “with the help of” this trope maps to a lump of clay as a bearer of this trope. Similarly, *that* refers to another complex trope, say this particular brownness and this angularity and maps to a bearer of this trope. The crucial assumption here is that the tropes in question may have multiple bearers, e.g., the brownness and roundness is a trope borne both by the clay and the statue. Moltmann’s semantics of the (apparent) statements of sortal-relative identity of the form “This is the same … as that” has it that such statements are true if *this* refers to a trope such that at least one, but not all, of its bearers is identical (in the sense of absolute identity) to a bearer of the trope to which *that* refers. So our sentence “This is the same lump of clay but not the same statue as that” is true when (i) one bearer of the *this* trope is the same as a bearer of the *that* trope and (ii) another bearer of that first trope is not the same as a bearer of the other trope.

**Reply**: The semantics outlined by Moltmann has its ontological cost because its proponent needs to acknowledge that a single trope may have multiple bearers. But even if you are persuaded by her argumentation to this controversial position, you may still accept RI. Moltmann’s theory concerns a specific class of relative identity statements and does not directly affect the applications of RI described above, which need not be rendered as identity statements involving bare demonstratives. For instance, accepting this theory you are at liberty to say that the original and remodeled ship are the same ship but not the same collection of planks, whereas the reassembled ship is the same collection of planks as the original but not the same ship. So even if the whole body of linguistic evidence for RI can be explained away, we may use relative identity as a theoretical explanatory tool, e.g., to provide resolutions to the paradoxes described above.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=identity-relative). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/identity-relative/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=identity-relative&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/identity-relative/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

[Please contact the author with suggestions.]

## Related Entries

Christian theology, philosophy and | identity | identity: of indiscernibles | identity: transworld | logic: ancient | logic: classical | personal identity | properties | trinity | vagueness

### Acknowledgments

The SEP editors would like to thank Christopher von Bülow for reporting a list of typographical and other issues in an earlier version of this entry.

[^anscombe-1961]: Anscombe, G.E.M. and P. T. Geach, 1961, *Three philosophers: Aristotle; Aquinas; Frege*, Ithaca: Cornell Press.

[^baker-1997]: Baker, L. R., 1997, “Why Constitution is not Identity”, *Journal of Philosophy*, 94: 599–621.

[^alston-1984]: Alston, W. and J. Bennett, 1984, “Identity and Cardinality: Geach and Frege”, *Philosophical Review*, 93: 553–568.

[^blanchette-1999]: Blanchette, P., 1999, “Relative Identity and Cardinality”, *Canadian Journal of Philosophy*, 29: 205–224.

[^borowski-1975]: Borowski, E.J., 1975, “Diachronic Identity as Relative Identity”, *Philosophical Quarterly*, 25: 271–276.

[^branson-2019]: Branson, B., 2019, “No new solutions to the logical problem of the Trinity”, *Journal of Applied Logics*, 6: 1051–1091.

[^burke-1992]: Burke, M., 1992, “Copper Statues and Pieces of Copper: A Challenge to the Standard Account”, *Analysis*, 52: 12–17.

[^burke-1994]: –––, 1994, “Dion and Theon: An Essentialist Solution to an Ancient Puzzle”, *The Journal of Philosophy*, 91(3): 129–139. doi:10.2307/2940990

[^carmichael-2020]: Carmichael, Chad. 2020, “How to Solve the Puzzle of Dion and Theon Without Losing Your Head”, *Mind*, 129(513): 205–224.

[^carrara-2007]: Carrara, M. and E. Sacchi, 2007, “Cardinality and Identity”, *Journal of Philosophical Logic*, 36: 539–556.

[^carter-1982]: Carter, W. R., 1982, “On Contingent Identity and Temporal Worms”, *Philosophical Studies*, 41: 213–230.

[^carter-1987]: –––, 1987, “Contingent Identity and Rigid Designation”, *Mind*, 96: 250–255.

[^carter-1990]: –––, 1990, *Elements of Metaphysics*, New York: McGraw-Hill.

[^cartwright-1987]: Cartwright, R., 1987, “On the Logical Problem of the Trinity”, in R. Cartwright, *Philosophical Essays*, Cambridge, Mass.: MIT Press.

[^chandler-1971]: Chandler, H., 1971, “Constitutivity and Identity”, *Noûs*, 5: 513–519.

[^chandler-1975]: –––, 1975, “Rigid Designation”, *The Journal of Philosophy*, 72: 363–369.

[^chandler-1976]: –––, 1976, “Plantinga and the Contingently Possible”, *Analysis*, 36: 106–109.

[^chisholm-1967]: Chisholm, R. M., 1967, “Identity through Possible Worlds: Some Questions”, *Noûs*, 1: 1–8.

[^chisholm-1969]: –––, 1969, “The Loose and Popular and the Strict and Philosophical Senses of Identity”, in R. H. Grim and R. Care (eds), *Perception and Personal Identity*, Cleveland: Ohio University Press.

[^chisholm-1973]: –––, 1973, “Parts as Essential to their Wholes”, *Review of Metaphysics*, 26: 581–603.

[^church-1954]: Church, A., 1954, “Intensional Isomorphism and Identity of Belief”, *Philosophical Studies*, 5: 65–73; reprinted in Salmon and Soames, 1988.

[^church-1982]: –––, 1982, “Una observación respecto de la paradoja de Quine sobre la modalidad”, *Análisis Filosófico*, 2(1): 25–32. English version as “A Remark Concerning Quine’s Paradox About Modality” and reprinted in Salmon and Soames 1988.

[^crimmins-1998]: Crimmins, M., 1998, “Hesperus and Phosphorus: Sense, Pretense, and Reference”, *Philosophical Review*, 107: 1–48.

[^deutsch-1997]: Deutsch, H., 1997, “Identity and General Similarity”, *Philosophical Perspectives*, 12: 177–200.

[^dummett-1991]: Dummett, M., 1991, “Does Quantification involve Identity?”, in H.G. Lewis (ed.), *Peter Geach*: *Philosophical Encounters*, Dordrecht: Kluwer Academic Publishers.

[^eglueta-1999]: Eglueta, R. and R. Jansana, 1999, “Definability of Leibniz Equality”, *Studia Logica*, 63: 223–243.

[^enderton-2000]: Enderton, H., 2000, *A Mathematical Introduction to Logic*, New York: Academic Press.

[^epstein-2001]: Epstein, R., 2001, *Predicate Logic*, Belmont, CA: Wadsworth.

[^evans-1978]: Evans, G., 1978, “Can There be Vague Objects?”, *Analysis*, 38: 308.

[^forbes-1985]: Forbes, G., 1985, *The Metaphysics of Modality*, Oxford: Oxford University Press.

[^forbes-1994]: –––, 1994, “A New Riddle of Existence”, *Philosophical Perspectives*, 8: 415–430.

[^freund-2019]: Freund, M. A., 2019, *The Logic of Sortals: A Conceptualist Approach*, Cham: Springer.

[^gallois-1986]: Gallois, A., 1986, “Rigid Designation and the Contingency of Identity”, *Mind*, 95: 57–76.

[^gallois-1988]: –––, 1988, “Carter on Contingent Identity and Rigid Designation”, *Mind*, 97: 273–278.

[^gallois-1990]: –––, 1990, “Occasional Identity”, *Philosophical Studies*, 58: 203–224.

[^gallois-1998]: –––, 1998, *Occasions of Identity*: *A Study in the Metaphysics of Persistence, Change and Sameness*, Oxford: Clarendon Press.

[^garbacz-2002]: Garbacz, P., 2002, “Logics of Relative Identity”, *Notre Dame Journal of Formal Logic*, 43: 27–50.

[^garbacz-2004]: –––, 2004, “Subsumption and Relative Identity”, *Axiomathes*, 14: 341–360.

[^geach-1967]: Geach, P.T., 1967 [1972], “Identity”, *Review of Metaphysics*, 21(1): 3–12. Reprinted in Geach 1972, pp. 238–247.

[^geach-1972]: –––, 1972, *Logic Matters*, Oxford: Blackwell.

[^geach-1973]: –––, 1973, “Ontological Relativity and Relative Identity”, in M. Munitz (ed.), *Logic and Ontology*, New York: New York University Press.

[^geach-1980]: –––, 1980, *Reference and Generality* (third edition). Ithaca: Cornell University Press.

[^gibbard-1975]: Gibbard, A., 1975, “Contingent Identity”, *Journal of Philosophical Logic*, 4: 187–221.

[^goodman-1968]: Goodman, N., 1968, *Languages of Art*, Indianapolis and New York: Bobbs-Merrill Company.

[^griffin-1977]: Griffin, N., 1977, *Relative Identity*, New York: Oxford University Press.

[^guillon-2021]: Guillon, J.-B., 2021, “Coincidence as parthood”, *Synthese*, 198: 4247–4276.

[^gupta-1980]: Gupta, A., 1980, *The Logic of Common Nouns*, New Haven and London: Yale University Press.

[^heller-1990]: Heller, M., 1990, *The Ontology of Physical Objects*, New York: Cambridge University Press.

[^hinchliff-1996]: Hinchliff, M., 1996, “The Puzzle of Change”, *Philosophical Perspectives*, 10: 119–133.

[^hodges-1983]: Hodges, W., 1983, “Elementary Predicate Logic”, in D. Gabbay and F. Guenthner (eds), *Handbook of Philosophical Logic*, v.1, Dordrecht: Reidel.

[^johnston-1992]: Johnston, M., 1992, “Constitution is not Identity”, *Mind*, 101: 89–105.

[^koslicki-2005]: Koslicki, K., 2005, “Almost Indiscernible Objects and the Suspect Strategy”, *The Journal of Philosophy*, 102: 55–77.

[^kraut-1980]: Kraut, R., 1980, “Indiscernibility and Ontology”, *Synthese*, 44: 113–135.

[^kripke-1971]: Kripke, S., 1971, “Identity and Necessity”, in M. Munitz (ed.), *Identity and Individuation*, New York: New York University Press.

[^kripke-1972]: –––, 1972, “Naming and Necessity”, in D. Davidson and G. Harman (eds), *Semantics of Natural Language*, Boston: Reidel. Revised and reprinted as Kripke 1980.

[^kripke-1979]: –––, 1979, “A Puzzle about Belief”, in A. Margalit (ed.), *Meaning and Use*, Dordrecht: Reidel. Reprinted in Salnon and Soames, 1988.

[^kripke-1980]: –––, 1980, *Naming and Necessity*, Oxford: Blackwell.

[^lewis-1986]: Lewis, D. K., 1986, *On the Plurality of Worlds*, Oxford: Blackwell.

[^lewis-1993]: –––, 1993, “Many But Almost One”, in K. Campbell, J. Bacon, and L. Reinhardt (eds), *Ontology, Causality and Mind: Essays on the Philosophy of D.M. Armstrong*, Cambridge, England: Cambridge University Press. Reprinted in Lewis, 1999.

[^lewis-1999]: –––, 1999, *Papers in Metaphysics and Epistemology*, Cambridge, England: Cambridge University Press.

[^long-1987]: Long, A. A. and D. N. Sedley, 1987, *The Hellenistic Philosophers* (Volume 1), Cambridge: Cambridge University Press.

[^lowe-1982]: Lowe, E. J., 1982, “The Paradox of the 1,001 Cats”, *Analysis*, 42: 128–130.

[^lowe-1989]: –––, 1989, *Kinds of Being*, Oxford: Basil Blackwell.

[^lowe-1995]: –––, 1995, “Coinciding Objects: In Defence of the ‘Standard Account”, *Analysis*, 55: 171–178.

[^mates-1952]: Mates, B., 1952, “Synonymity”, in L. Linsky (ed.), *Semantics and the Philosophy of Language*, Champaign-Urbana: University of Illinois Press.

[^mcginn-2000]: McGinn, C., 2000, *Logical Properties*, Oxford: Blackwell.

[^moltmann-2013]: Moltmann, F., 2013, “Tropes, Bare Demonstratives, and Apparent Statements of Identity”, *Noûs*, 47: 346–370.

[^molto-2017]: Molto, D., 2017, “The Logical Problem of the Trinity and the Strong Theory of Relative Identity”, *Sophia*, 56: 227–245.

[^myro-1985]: Myro, G., 1985, “Identity and Time”, in *Philosophical Grounds of Rationality*: *Intentions, Categories, Ends*, R. Grandy and R. Warner (eds). New York and Oxford: Oxford University Press.

[^noonan-1980]: Noonan, H., 1980, *Objects and Identity*, The Hague: Springer Netherlands.

[^noonan-1983]: –––, 1983, “The Necessity of Origin”, *Mind*, 92: 1–20.

[^noonan-1991]: –––, 1991, “Indeterminate Identity, Contingent Identity and Abelardian Predicates”, *The Philosophical Quarterly*, 41: 183–193.

[^noonan-1993]: –––, 1993, “Constitution is Identity”, *Mind*, 102: 133–146.

[^noonan-1997]: –––, 1997, “Relative Identity”, in B. Hale and C. Wright (eds), *A Companion to the Philosophy of Language*, Oxford: Blackwell.

[^nozick-1982]: Nozick. R., 1982, *Philosophical Explanations*, Cambridge, Mass.: Harvard University Press.

[^o’connor-1967]: O’Connor, D.J., 1967, “Substance and Attribute”, in P. Edwards (ed.), *The Encyclopedia of Philosophy*, New York: Macmillan.

[^oderberg-1996]: Oderberg, D., 1996, “Coincidence under a Sortal”, *The Philosophical Review*, 105: 145–171.

[^parfit-1984]: Parfit, D., 1984, *Reasons and Persons*, Oxford: Oxford University Press.

[^parsons-2000]: Parsons, T., 2000, *Indeterminate Identity*, Oxford: Oxford University Press.

[^perry-1970]: Perry, J., 1970, “The Same *F*”, *The Philosophical Review,* 79(2): 181–200. doi:10.2307/2183947

[^perry-1978]: –––, 1978, “Relative Identity and Number”, *Canadian Journal of Philosophy*, 8: 1–15.

[^plutarch-1914]: Plutarch, *The Life of Theseus*, in *The Parallel Lives*, Loeb Classical Library, Cambridge, MA: Harvard University Press, 1914.

[^quine-1960]: Quine, W. V. O., 1960, *Word and Object*, Cambridge, MA: MIT Press.

[^quine-1963]: –––, 1963, *From a Logical Point of View*, New York: Harper and Row.

[^quine-1970]: –––, 1970, *Philosophy of Logic*, Englewood Cliffs, N.J.: Prentice Hall.

[^rea-1995]: Rea, M., 1995, “The Problem of Material Constitution”, *The Philosophical Review*, 104(4): 525–552. doi:10.2307/2185816

[^rea-1997]: ––– (ed.), 1997, *Material Constitution*: *A Reader*, Lanham, MD: Rowman and Littlefield.

[^read-1995]: Read, S., 1995, *Thinking About Logic*, Oxford: Oxford University Press.

[^salmon-1979]: Salmon, N., 1979, “How *Not* to Derive Essentialism from the Theory of Reference”, *The Journal of Philosophy*, 76: 703–725.

[^salmon-1986]: –––, 1986, “Reflexivity”, *Notre Dame Journal of Formal Logic*, 27: 401–429; reprinted in Salmon and Soames, 1988.

[^salmon-1989]: –––, 1989, “The Logic of What Might Have Been”, *Philosophical Review*, 98: 3–34.

[^salmon-1988]: Salmon, N. and S. Soames (eds), 1988, *Propositions and Attitudes*, Oxford: Oxford University Press.

[^sedley-1982]: Sedley, D., 1982, “The Stoic Criterion of Identity”, *Phronesis*, 27: 255–275.

[^silver-1994]: Silver, C., 1994, *From Symbolic Logic…to Mathematical Logic*, Melbourne: Wm. C. Brown, Publishers.

[^simons-1987]: Simons, P., 1987, *Parts: A Study in Ontology*, Oxford: Clarendon Press.

[^swindler-1991]: Swindler, J. K., 1991, *Weaving: An Analysis of the Constitution of Objects*, Savage, MD.: Rowman & Littlefield.

[^thompson-1998]: Thompson, J., 1998, “The Statue and the Clay”, *Noûs*, 32: 149–173.

[^unger-1980]: Unger, P., 1980, “The Problem of the Many”, *Midwest Studies in Philosophy*, 5: 411–467.

[^uzgalis-1990]: Uzgalis, W., 1990, “Relative Identity and Locke’s Principle of Individuation”, *History of Philosophy Quarterly*, 7: 283–297.

[^van-1981]: Van Inwagen, P., 1981, “The Doctrine of Arbitrary Undetached Parts”, *Pacific Philosophical Quarterly*, 62: 123–137.

[^van-1988]: –––, 1988, “And yet there are not three Gods, but one God”, in T. Morris (ed.), *Philosophy and the Christian faith*, Notre Dame: University of Notre Dame Press, pp. 241–278.

[^van-1990]: –––, 1990, *Material Beings*, Ithaca, NY: Cornell University Press.

[^van-1994]: –––, 1994, “Not by Confusion of Substance, but by Unity of Person”, in Richard Swinburne & Alan G. Padgett (eds), *Reason and the Christian Religion: Essays in Honour of Richard Swinburne*, Oxford: Oxford University Press, pp. 201–226.

[^van-2003]: –––, 2003, “Three persons in one being: on attempts to show that the doctrine of the trinity is self-contradictory”, in M.Y. Stewart (ed.), *The Trinity: East/West Dialogue*, Boston: Kluwer, pp. 83–97.

[^wiggins-1967]: Wiggins, D., 1967, *Identity and Spatio-Temporal Continuity*, Oxford: Blackwell.

[^wiggins-1968]: –––, 1968, “On Being in the Same Place at the Same Time”, *Philosophical Review*, 77: 90–95.

[^wiggins-1980]: –––, 1980, *Sameness and Substance*, Oxford: Blackwell.

[^williams-1990]: Williams, C.J.F., 1990, *What is Identity?*, Oxford: Oxford University Press.

[^williamson-1988]: Williamson, T., 1988, “First-order Logics for Comparative Similarity”, *Notre Dame Journal of Formal Logic*, 29: 457–481.

[^williamson-1990]: –––, 1990, *Identity and Discrimination*, Oxford: Blackwell.

[^yablo-1987]: Yablo, S., 1987, “Identity, Essence and Indiscernibility”, *Journal of Philosophy*, 84: 293–314.

[^zalabardo-2000]: Zalabardo, J., 2000, *Introduction to the Theory of Logic*, Boulder, Colorado: Westview Press.

[^zemach-1974]: Zemach, E., 1974, “In Defence of Relative Identity”, *Philosophical Studies*, 26: 207–218.
