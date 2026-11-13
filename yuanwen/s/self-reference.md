# Self-Reference and Paradox

*Bolander, Thomas*

![animation representing self-reference](../assets/self-reference/poster_all_pos250.gif)
# Self-Reference and Paradox
**First published Tue Jul 15, 2008; substantive revision Fri Jul 19, 2024**

In the context of language, *self-reference* is used to denote a statement that refers to itself or its own referent. The most famous example of a self-referential sentence is the *liar sentence*: “This sentence is not true.” Self-reference is often used in a broader context as well. For instance, a picture could be considered self-referential if it contains a copy of itself (see the animated image above); and a piece of literature could be considered self-referential if it includes a reference to the work itself. In philosophy, self-reference is of specific interest in relation to the analysis of language, but also to the analysis of the mind. Self-reference is also a field of special interest in mathematics and computer science, in particular in relation to the foundations of these sciences.

We also talk about self-reference when using the first-person pronoun “I” like in “I feel pain” or “I know this song”. Self-reference in the sense of an agent referring to herself as well as how self-attribution and self-identification differs from attributing to or identifying others is covered in several other entries of this encyclopedia, including self-knowledge, knowledge of the self, self-consciousness, Descartes’ epistemology, and introspection.

A major part of the philosophical interest in self-reference is centered around the paradoxes. A *paradox* is a seemingly sound piece of reasoning, based on apparently true assumptions, that still leads to a contradiction (Quine, 1976)[^quine-1976]. Consider again the liar sentence from above. It is a sentence $L$ expressing “The sentence $L$ is not true.” We are led to a contradiction when trying to determine whether $L$ is true or not. If we first assume $L$ to be true, then it must be expressing a true statement about the world. As $L$ expresses “The sentence $L$ is not true,” we now have that $L$ is not true, which is a contradiction. Suppose, conversely, that $L$ is not true. Then the expression “The sentence $L$ is not true” is true. But the expression in the quotes is exactly the statement expressed by $L$, so $L$ must be true, again a contradiction. Hence, independently of whether we assume $L$ to be true or not, we are led to a contradiction. Thus we now have a contradiction obtained by a seemingly sound piece of reasoning based on apparently true assumptions. It hence qualifies as a paradox. This paradox is known as the *liar paradox*. The liar sentence leads to a paradox *because* it is self-referential, but self-reference is not a sufficient condition for paradoxicality. The *truth-teller sentence* “This sentence is true” is not paradoxical, and neither is the sentence “This sentence contains four words” (it is false, though).

Most paradoxes of self-reference may be categorised as either *semantic*, *set-theoretic* or *epistemic*. The semantic paradoxes, like the liar paradox, are primarily relevant to theories of truth. The set-theoretic paradoxes are relevant to the foundations of mathematics, and the epistemic paradoxes are relevant to epistemology. Even though these paradoxes are different in the subject matter they relate to, they share the same underlying structure, and may often be tackled using the same mathematical means.

In the present entry, we will first introduce a number of the most well-known paradoxes of self-reference, and discuss their common underlying structure. Subsequently, we will discuss the profound consequences that these paradoxes have on a number of different areas: theories of truth, set theory, epistemology, foundations of mathematics, computability. Finally, we will present the most prominent approaches to solving the paradoxes.

## 1. Paradoxes of Self-Reference

### 1.1 Semantic Paradoxes

Paradoxes of self-reference have been known since antiquity. The discovery of the liar paradox is often credited to Eubulides the Megarian who lived in the 4th century BC. The liar paradox belongs to the category of *semantic* paradoxes, since it is based on the semantic notion of truth. Other well-known semantic paradoxes include Grelling’s paradox, Berry’s paradox, and Richard’s paradox.

*Grelling’s paradox* involves a predicate defined as follows. Say a predicate is *heterological* if it is not true of itself, that is, if it does not itself have the property it expresses. Then the predicate “German” is heterological, since it is not itself a German word, but the predicate “deutsch” is not heterological. The question that leads to the paradox is now:

> Is “heterological” heterological?

It is easy to see that we obtain a contradiction independently of whether we answer “yes” or “no” to this question (the argument runs more or less like in the liar paradox). Grelling’s paradox is self-referential, since the definition of the predicate heterological refers to *all* predicates, including the predicate heterological itself. Definitions such as this which depends on a set of entities, at least one of which is the entity being defined, are called *impredicative*.

*Berry’s paradox* is another paradox based on an impredicative definition, or rather, an impredicative description. Some phrases of the English language are descriptions of natural numbers, for example, “the sum of five and seven” is a description of the number 12. Berry’s paradox arises when trying to determine the denotation of the following description:

> the least number that cannot be referred to by a description containing less than 100 symbols.

The contradiction is that this description containing 93 symbols denotes a number which, by definition, cannot be denoted by any description containing less than 100 symbols. The description is of course impredicative, since it implicitly refers to *all* descriptions, including itself.

*Richard’s paradox* considers phrases of the English language defining real numbers rather than natural numbers. For example, “the ratio between the circumference and diameter of a circle” is a phrase defining the number $\pi$. Assume an enumeration of all such phrases is given (e.g. by putting them into lexicographical order). Now consider the phrase:

> the real number whose $n$th decimal place is 1 whenever the $n$th decimal place of the number denoted by the $n$th phrase is 0; otherwise 0.

This phrase defines a real number, so it must be among the enumerated phrases, say number $k$ in this enumeration. But, at the same time, by definition, it differs from the number denoted by the $k$th phrase in the $k$th decimal place. Thus we have a contradiction. The defining phrase is obviously impredicative. The particular construction employed in this paradox is called *diagonalisation*. Diagonalisation is a general construction and proof method originally invented by Georg Cantor (1891) to prove the uncountability of the power set of the natural numbers. It was also used as a basis for Cantor’s paradox, one of the set-theoretic paradoxes to be considered next.

### 1.2 Set-Theoretic Paradoxes

The best-known set-theoretic paradoxes are Russell’s paradox and Cantor’s paradox. *Russell’s paradox* arises from considering the *Russell set* $R$ of all sets that are not members of themselves, that is, the set defined defined by $R = \{ x \mid x \not\in x \}$. The contradiction is then derived by asking whether $R$ is a member of itself, that is, whether $R \in R$ holds. If $R \in R$ then $R$ is a member of itself, and thus $R \not\in R$, by definition of $R$. If, on the other hand, $R \not\in R$ then $R$ is not a member of itself, and thus $R \in R$, again by definition of $R$.

*Cantor’s paradox* is based on an application of Cantor’s theorem. *Cantor’s theorem* states that given any finite or infinite set $S$, the power set of $S$ has strictly larger cardinality (greater size) than $S$. The theorem is proved by a form of diagonalisation, the same idea underlying Richard’s paradox. Cantor’s paradox considers the set of all sets. Let us call this set the *universal set* and denote it by $U$. The power set of $U$ is denoted $\wp(U)$. Since $U$ contains *all* sets it will in particular contain all elements of $\wp(U)$. Thus $\wp(U)$ must be a subset of $U$ and must thus have a cardinality (size) which is less than or equal to the cardinality of $U$. However, this immediately contradicts Cantor’s theorem.

The *Hypergame paradox* is a more recent addition to the list of set-theoretic paradoxes, invented by Zwicker (1987). Let us call a two-player game *well-founded* if it is bound to terminate in a finite number of moves. Tournament chess is an example of a well-founded game. We now define *hypergame* to be the game in which player 1 in the first move chooses a well-founded game to be played, and player 2 subsequently makes the first move in the chosen game. All remaining moves are then moves of the chosen game. Hypergame must be a well-founded game, since any play will last exactly one move more than some given well-founded game. However, if hypergame is well-founded then it must be one of the games that can be chosen in the first move of hypergame, that is, player 1 can choose hypergame in the first move. This allows player 2 to choose hypergame in the subsequent move, and the two players can continue choosing hypergame *ad infinitum*. Thus hypergame cannot be well-founded, contradicting our previous conclusion.

### 1.3 Epistemic Paradoxes

The most well-know epistemic paradox is the *paradox of the knower* (Kaplan & Montague, 1960; Montague, 1963)[^kaplan-1960][^montague-1963]. This paradox has many equivalent formulations, one of them based on the sentence “This sentence is not known by anyone.” Let us call this sentence the *knower sentence*, abbreviated $KS. KS$ is obviously quite similar to the liar sentence, except the central concept involved is knowledge rather than truth. The reasoning leading to a contradiction from $KS$ is a bit more complex than in the liar paradox. First $KS$ is shown to be true by the following piece of reasoning:

> Assume to obtain a contradiction that $KS$ is not true. Then what $KS$ expresses cannot be the case, that is, $KS$ must be known by someone. Since everything known is true (this is part of the definition of the concept of knowledge), $KS$ is true, contradicting our assumption. This concludes the proof that $KS$ is true.

The piece of reasoning just carried out to prove the truth of $KS$ should be available to any agent (person) with sufficient reasoning capabilities. That is, an agent should be able to prove the truth of $KS$, and thus come to know that $KS$ holds. However, if $KS$ is known by someone, then what it expresses is not the case, and thus it cannot be true. This is a contradiction, and thus we have a paradox. The role of self-reference in this paradox is obvious, as it is based on a sentence, $KS$, referring directly to itself.

The paradox of the knower is just one of many epistemic paradoxes involving self-reference. See the entry on epistemic paradoxes for further information on the class of epistemic paradoxes. A quite recent epistemic paradox, cast in the setting of beliefs and assumptions in a two-player game, is the Brandenburger-Keisler paradox (Brandenburger & Keisler, 2006)[^brandenburger-2006], described in detail in the entry on epistemic foundations of game theory. For a detailed discussion and history of the paradoxes of self-reference in general, see the entry on paradoxes and contemporary logic.

### 1.4 Common Structures in the Paradoxes

The paradoxes above are all quite similar in structure. In the case of the paradoxes of Grelling and Russell, this can be seen as follows. Define the *extension* of a predicate to be the set of objects it is true of. For a predicate $P$ we denote its extension by ext$(P)$. Grelling’s paradox involves the predicate heterological, which is true of all those predicates that are not true of themselves. Thus the extension of the predicate heterological is the set $\{ P \mid P \not\in$ ext$(P) \}$. Compare this to the Russell set $R$ given by $\{ x \mid x \not\in x \}$. The only significant difference between these two sets is that the first is defined on predicates whereas the second is defined on sets. The proofs of contradictions based on these two sets also share the same structure, as seen below (where “het” abbreviates “heterological”):

$$\begin{align*} \tag{Grelling} \het \in \ext(\het) &\Leftrightarrow \het \in \{ P \mid P \not\in \ext(P)\} \\ &\Leftrightarrow \het \not\in \ext(\het). \\ & \\ \tag{Russell} R \in R &\Leftrightarrow R \in \{ x \mid x \not\in x\} \\ &\Leftrightarrow R \not\in R. \end{align*}$$

We have here two paradoxes of an almost identical structure belonging to two distinct classes of paradoxes: one is semantic and the other set-theoretic. What this teaches us is that even if paradoxes seem different by involving different subject matters, they might be almost identical in their underlying structure. Thus in many cases it makes most sense to study the paradoxes of self-reference under one, rather than study, say, the semantic and set-theoretic paradoxes separately.

Russell and Cantor’s paradoxes are also more similar than they appear at first. Cantor’s paradox is based on an application of Cantor’s theorem to the universal set $U$ (cf. Section 1.2 above). Below we give the proof of Cantor’s theorem for an arbitrary set $S$.

We need to prove that $\wp(S)$ has greater cardinality than $S$. Assume to obtain a contradiction that this is not the case. Then there must exist a (potentially partial) map $f$ from $S$ onto $\wp(S)$. Now consider the set $C = \{ x \in dom(f) \mid x \not\in f(x) \}$. Clearly $C \subseteq S$, so $C \in \wp(S)$. Since $f$ is onto $\wp(S)$, there must then exist a set $c \in dom(f)$ such that $f(c)=C$. However, we now obtain a contradiction, since the following holds:

$$\begin{align*} c \in f(c) &\Leftrightarrow c \in \{ x \in dom(f) \mid x \not\in f(x) \} \\ &\Leftrightarrow c \not\in f(c). \end{align*}$$

Note the similarity between this sequence of equivalences and the corresponding sequences of equivalences derived for Russell’s and Grelling’s paradoxes above. Now consider the special case of Cantor’s theorem where $S$ is the universal set. Then we can simply choose $f$ to be the identity function on $\wp(S)$, since $S$ is the universal set and hence $ \wp(S) \subseteq S$ (any set must be a subset of the universal set). So $f$ is the partial function $f: \wp(S) \to \wp(S)$ defined by $f(x) = x$. But then $C$ above becomes the Russell set, and the sequence of equivalences become the proof of contradiction in Russell’s paradox! Thus Cantor’s paradox is nothing more than a slight variant of Russell’s paradox; the core argument leading to the contradiction is the same in both.

Priest (1994) gives even firmer evidence to the similarity between the paradoxes of self-reference by showing that they all fit into what he originally called the *Qualified Russell’s Schema*, now termed the *Inclosure Schema*. The idea behind it goes back to Russell himself (1905) who also considered the paradoxes of self-reference to have a common underlying structure. Given two predicates predicates $P$ and $Q$, and a possibly partial function $\delta$, the Inclosure Schema consists of the following two conditions:

1. $w = \{ x \mid P(x) \}$ exists and $Q(w)$ holds;
2. if $y$ is a subset of $w$ such that $Q(y)$ holds then:
3. $\delta(y) \not\in y$,
4. $\delta(y) \in w$.

If these conditions are satisfied we have the following contradiction: Since $w$ is trivially a subset of $w$ and since $Q(w)$ holds by condition 1, we have both $\delta(w) \not\in w$ and $\delta(w) \in w$, by 2a and 2b, respectively. Thus any triple $(P,Q,\delta)$ satisfying the Inclosure Schema will produce a paradox. Priest shows how most of the well-known paradoxes of self-reference fit into the schema. Below we will consider only a few of these paradoxes, starting with Russell’s paradox. In this case we define the triple $(P,Q,\delta)$ as follows:

- $P(x)$ is the predicate “$x \not\in x$”.
- $Q(y)$ is the universal predicate true of any object.
- $\delta$ is the identity function.

Then $w$ in the Inclosure Schema becomes the Russell set and the contradiction obtained from the schema becomes Russell’s paradox.

In the case of Richard’s paradox we define the triple by:

- $P(x)$ is the predicate “$x$ is a real definable by a phrase in English.”
- $Q(y)$ is the predicate “$y$ is a denumerable set of reals definable by a phrase in English.”
- $\delta$ is the function that maps any denumerable set $y$ of reals to the real $z$ whose $n$th decimal place is 1 whenever the $n$th decimal of the $n$th real in $y$ is 0; otherwise 0. (Any enumeration of the elements in $y$ will do.)

Here $w = \{ x \mid P(x) \}$ becomes the set of all reals definable by phrases in English. For any denumerable subset $y$ of $w, \delta(y)$ is a real that by construction will differ from all reals in $y$ (it differs from the $n$th real in $y$ on the $n$th decimal place). Letting $y$ equal $w$ we thus get $\delta(w) \not\in w$. However, at the same time $\delta(w)$ is definable by a phrase in English, so $\delta(w) \in w$, and we have a contradiction. This contradiction is Richard’s paradox.

The liar paradox also fits Russell’s schema, albeit in a slightly less direct way:

- $P(x)$ is the predicate “$x$ is true.”
- $Q(y)$ is the predicate “$y$ is definable.”
- $\delta(y)$ is the sentence “this sentence does not belong to the set $y$.”

Here $w = \{ x \mid P(x) \}$ becomes the set of true sentences, and $\delta(w)$ becomes a version of the liar sentence: “this sentence does not belong to the set of true sentences”.

From the above it can be concluded that all, or at least most, paradoxes of self-reference share a common underlying structure—independent of whether they are semantic, set-theoretic or epistemic. Priest (1994) argues that they should then also share a common solution. Priest calls this the *principle of uniform solution*: “same kind of paradox, same kind of solution.” Whether the Inclosure Schema can in full generality count as a necessary and sufficient condition for self-referential paradoxicality is however disputable (Slater, 2002; Abad, 2008; Badici, 2008; Zhong, 2012, and others)[^abad-2008][^badici-2008][^slater-2002][^zhong-2012], hence not all authors agree on the principle of uniform solution either.

The sorites paradox is a paradox that on the surface does not involve self-reference at all. However, Priest (2010b, 2013) argues that it still fits the inclosure schema and can hence be seen as a paradox of self-reference, or at least a paradox that should have the same kind of solution as the paradoxes of self-reference. This has led Colyvan (2009), Priest (2010) and Weber (2010b) to all advance a dialetheic approach to solving the Sorites paradox. This approach to the Sorites paradox has been attacked by Beall (2014a, 2014b) and defended by Weber et al. (2014). Cobreros et al. (2015) investigate the notion of *permissive consequence* with an aim to give a unified treatment of the paradoxes of vagueness (like the sorites paradox) and the paradoxes of self-reference. The permissive consequence relation is a weakened version of the classical consequence relation in the setting of multi-valued logic: it only requires that when the premises take value 1 (are true-only), then the conclusion must not take value 0 (is not false-only). An even more recent unified diagnosis of semantic and soritical paradoxes is by Bruni & Rossi (2023), identifying their source in a general form of indiscernibility.

### 1.5 Paradoxes without Negation

Most paradoxes considered so far involve negation in an essential way, e.g. sentences saying of themselves that they are *not* true or knowable. The central role of negation will become even clearer when we formalise the paradoxes of self-reference in Section 2 below. *Curry’s paradox* is a similar paradox of self-reference that however does not directly involve negation. A semantic variant of Curry’s paradox comes from the following *Curry sentence* $C$: “If this sentence is true then $F$”, where $F$ can be any statement, for instance an obviously false one. Suppose the Curry sentence $C$ is true. Then it expresses a true fact, that is, if $C$ is true then $F$. However, we already assumed $C$ to be true, so we can infer $F$, using Modus Ponens. We have now proved that if we assume $C$ to be true, then $F$ follows. This is exactly what the Curry sentence itself expresses. In other words, we have proved that the Curry sentence itself is true! But then we also have that $F$ is true, and this is a paradox, since $F$ can be any statement, including things that are obviously false. We can for instance easily prove that Santa Claus exists by simply letting $F$ be the sentence “Santa Claus exists” (Boolos, 1993; Smullyan, 2006)[^boolos-1993][^smullyan-2006]. In a classical logical setting where the implication $C \rightarrow F$ is equivalent to $\neg C \vee F$, Curry’s paradox still implicitly involves negation, but Curry’s paradox is still independently interesting since it goes through with fewer assumptions about the underlying logic than the liar paradox. See the entry on Curry’s paradox for more details.

### 1.6 Paradoxes without Self-Reference

Most classical paradoxes of self-reference involve *direct* self-reference as in the liar paradox where a sentence refers directly to itself. However, it is easy to construct paradoxes that only employ *indirect* self-reference, i.e., sentences that refer to other sentences that refer to yet other sentences in such a way as to form a loop back to the original sentence. One example is the *postcard paradox*, often attributed to Philip Jourdain (1879–1919), though according to Roy Sorensen (2003, p. 332), the true inventor is G.G. Berry (1867–1928), the Oxford librarian to whom also the earlier mentioned Berry’s paradox is accredited. In the postcard paradox, the front side of a postcard reads “the sentence on the back side is true”, whereas the back side reads “the sentence on the front side is false”. For the sentence on the front to be true, the sentence on the back needs to be true, but for the sentence on the back to be true, the sentence on the front needs to be false. This is a contradiction, achieved similarly as in the liar paradox. There are even much earlier examples of indirect self-reference in the literature: Sophism 9 in John Buridan’s 14th century Sophismata (Buridan [SD], Hughes 1982)[^hughes-1982] is structurally equivalent to the postcard paradox.

In 1985, Yablo succeeded in constructing a semantic paradox that does not involve self-reference at all, not even indirect self-reference. Instead, it consists of an infinite chain of sentences, each sentence expressing the untruth of all the subsequent ones. More precisely, for each natural number $i$ we define $S_i$ to be the sentence “for all $j\gt i, S_j$ is not true”. We can then derive a contradiction as follows:

First we prove that none of the sentences $S_i$ can be true. Assume to obtain a contradiction that $S_i$ is true for some $i$. Then it is true that “for all $j\gt i, S_j$ is not true”. Thus none of the sentences $S_j$ for $j\gt i$ are true. In particular, $S_{i+1}$ is not true. $S_{i+1}$ is the sentence “for all $j\gt i+1, S_j$ is not true”. Since this sentence is not true, there must be some $k\gt i+1$ for which $S_k$ is true. However, this contradicts that none of the sentences $S_j$ with $j\gt i$ are true.

We have now proved that none of the sentences $S_i$ are true. Then, in particular, we have that for all $j\gt 0$, S$_j$ is not true. This is exactly what is expressed by S$_0$, so S$_0$ must be true. This is again a contradiction.

Yablo calls this paradox the $\omega$*-liar*, but others usually refer to it as *Yablo’s paradox*. Note that none of the sentences $S_i$ refer to themselves (not even indirectly), but only to the ones that occur later in the sequence. Yablo’s paradox is semantic, but as shown by Yablo (2006), similar set-theoretic paradoxes involving no self-reference can be formulated in certain set theories.

Yablo’s paradox demonstrates that we can have logical paradoxes without self-reference—only a certain kind of non-wellfoundedness is needed to obtain a contradiction. There are obviously structural differences between the ordinary paradoxes of self-reference and Yablo’s paradox: The ordinary paradoxes of self-reference involve a cyclic structure of reference, whereas Yablo’s paradox involve an acyclic, but non-wellfounded, structure of reference. More precisely, we can think the referential structure underlying a paradox as a directed graph. The vertices of this graph are sentences, and there is a directed edge from sentence $S$ to sentence $T$ if $S$ refers directly to $T$. The referential structure of the liar is then a graph with a single reflexive loop. The referential structure of the postcard paradox is a cyclic graph with 2 vertices each having an edge to the other vertex. All paradoxes of direct or indirect self-reference have cyclic structures of reference (their underlying graphs are cyclic). It is different with Yablo’s paradox. The referential structure in Yablo’s paradox is isomorphic to the usual less-than ordering on the natural numbers, which is a strict total order (contains no cycles). Even though there is this difference, Yablo’s paradox still share most properties with the ordinary paradoxes of self-reference. When solving paradoxes we might thus choose to consider them all under one, and refer to them as *paradoxes of non-wellfoundedness*. In the following we will however stick to the term *paradoxes of self-reference*, even though most of what we say will apply to Yablo’s paradox and related paradoxes of non-wellfoundedness as well.

Given the insight that not only cyclic structures of reference can lead to paradox, but also certain types of non-wellfounded structures, it becomes interesting to study further these structures of reference and their potential in characterising the necessary and sufficient conditions for paradoxicality. This line of work was initiated by Gaifman (1988, 1992, 2000), and later pursued by Cook (2004), Walicki (2009) and others.

Significant amounts of newer work on self-reference has gone into trying to make a complete graph-theoretical characterisation of which structures of reference admit paradoxes, including Rabern and Macauley (2013), Cook (2014) and Dyrkolbotn and Walicki (2014). A complete characterisation is still an open problem (Rabern, Rabern and Macauley, 2013)[^rabern-2013], but it seems to be a relatively widespread conjecture that all paradoxical graphs of reference are either cyclic or contain a Yablo-like structure. The conjecture has been confirmed for certain sub-classes of infinite graphs (Walicki, 2019)[^walicki-2019], but it is still open whether it holds for arbitrary graphs. If the conjecture is indeed true, it means that in terms of structures of reference, all paradoxes of reference are either liar-like or Yablo-like. What it exactly means for a structure (graph) to be Yablo-like can be defined in several different, but equivalent, ways, including: 1) the graph contains the reference graph of the Yablo paradox, $ (\omega,\lt) $, as a finitary minor (Beringer & Schindler, 2017)[^beringer-2017][^schindler-2017]; 2) the graph contains a ray (an infinite path) on which there are infinitely many vertices each having infinitely many disjoint paths to infinitely many other vertices on the ray (Walicki, 2019)[^walicki-2019].

Even though the structure of reference involved in Yablo’s paradox does not contain any cycles (each sentence only refers to later sentences in the sequence), it is still being discussed whether the paradox is self-referential or not (Cook, 2014; Halbach and Zhang, 2017)[^cook-2014][^halbach-2017]. Yablo (1993) himself argues that it is non-self-referential, whereas Priest (1997) argues that it is self-referential. Butler (2017) claims that even if Priest is correct, there will be other Yablo-like paradoxes that are not self-referential in the sense of Priest. In the analysis of Yablo’s paradox, it is essential to note that it involves an *infinite* sequence of sentences, where each sentence refers to *infinitely* many other sentences. To formalise it in a setting of propositional logic, it is hence necessary to use infinitary propositional logic (see the entry on infinitary logic). Any finitary variant of Yablo’s sequence—where every sentence only refers to finitely many later sentences in the sequence—must necessarily be consistent (non-paradoxical) due to the compactness theorem in propositional logic (every finite subset of sentences in the sequence induces a well-founded reference relation and the sentences can hence consistently be assigned truth-values bottom-up). In finitary first- and second-order arithmetic, one can instead attempt to formalise Yablo’s paradox by a unary predicate $S(x)$ where, for every natural numbers $i$, $S({\inumeral})$ represents the formalisation of the $i$th sentence $S_i$ of the Yablo sequence (where $\inumeral{ }$ is the numeral representing $i)$. How and whether the Yablo paradox can truthfully be represented this way, and how it relates to compactness of the underlying logic, has been investigated by Picollo (2013).

Yablo’s paradox has also inspired the creation of similar paradoxes involving non-wellfounded, acyclic structures of reference in other areas than truth, e.g. the “Yabloesque” variant of the Brandenburger-Keisler paradox of epistemic game theory by Başkent (2016), a variant concerning provability by Cieśliński and Urbaniak (2013), and a variant in the context of Gödel’s incompleteness theorems by Leach-Krouse (2014).

## 2. Why the Paradoxes Matter

After having presented a number of paradoxes of self-reference and discussed some of their underlying similarities, we will now turn to a discussion of their *significance*. The significance of a paradox is its indication of a flaw or deficiency in our understanding of the central concepts involved in it. In case of the semantic paradoxes, it seems that it is our understanding of fundamental semantic concepts such as *truth* (in the liar paradox and Grelling’s paradox) and *definability* (in Berry’s and Richard’s paradoxes) that are deficient. In case of the set-theoretic paradoxes, it is our understanding of the concept of a *set*. If we fully understood these concepts, we should be able to deal with them without being led to contradictions.

To illustrate this, consider the case of Zeno’s classical paradox on *Achilles and the Tortoise* (see the entry Zeno’s paradoxes for details). In this paradox we seem able to prove that the tortoise can win a race against the 10 times faster Achilles if given an arbitrarily small head start. Zeno used this paradox as an argument against the possibility of motion. It has later turned out that the paradox rests on an inadequate understanding of infinity. More precisely, it rests on an implicit assumption that any infinite series of positive reals must have an infinite sum. The later developments of the mathematics of infinite series has shown that this assumption is invalid, and thus the paradox dissolves. The original acceptance of Zeno’s argument as a paradox was a symptom that the concept of infinity was not sufficiently well understood at the time. In analogy, it seems reasonable to expect that the existence of semantic and set-theoretic paradoxes is a symptom that the involved semantic and set-theoretic concepts are not yet sufficiently well understood. Or, at least, that we need to revise our view on what counts as “natural assumptions”. Russell’s paradox rests on the assumption that any predicate on mathematical objects determines a set consisting of exactly the objects that satisfy the predicate, and the liar paradox rests on the assumption that it is possible for a language to contain its own truth predicate. As a response to the paradoxes, these otherwise seemingly sensible assumptions have been revised, see Section 3 below.

Another possible answer could be that it is our understanding of the very concept of “contradiction” that is flawed. The reasoning involved in the paradoxes of self-reference all end up with some contradiction, a sentence concluded to be both true and false. We consider this an impossibility, hence the paradox, but maybe we don’t have to? *Dialetheism* is the view that there can be “true contradictions”, meaning that it is not impossible for a sentence to be both true and false. If adopting the view of dialetheism, all the paradoxes of self-reference dissolve and instead become existence proofs of certain “dialetheia”: sentences being both true and false. Priest (1987) is a strong advocate of dialetheism, and uses his principle of uniform solution (see Section 1.4 above) to defend the dialetheist solution. See the entries on dialetheism and paraconsistent logic for more information.

Currently, no commonly agreed upon solution to the paradoxes of self-reference exists. They continue to pose foundational problems in semantics and set theory. No claim can be made to a solid foundation for these subjects until a satisfactory solution to the paradoxes has been provided. Problems surface when it comes to formalising semantics (the concept of truth) and set theory. If formalising the intuitive, “naive” understanding of these subjects, inconsistent systems linger as the paradoxes will be formalisable in these systems.

### 2.1 Consequences of the Semantic Paradoxes

The liar paradox is a significant barrier to the construction of formal theories of truth as it produces inconsistencies in these potential theories. A substantial amount of research in self-reference concentrates on formal theories of truth and ways to circumvent the liar paradox. There are two articles that have influenced the work on formal theories of truth and the liar paradox more than any other: Alfred Tarski’s “The Concept of Truth in Formalised Languages” (1935) and Saul Kripke’s “Outline of a Theory of Truth” (1975). Below we first introduce some of the ideas and results of Tarski’s article. Kripke’s article is discussed in Section 3.2.

Tarski gives a number of conditions that, as he puts it, any *adequate definition of truth* must satisfy. The central of these conditions is what is now most often referred to as *Schema T* (or the *T-schema* or *Convention T* or the *Tarski biconditionals*):

$$ \tag{Schema \(T\)} \phi \leftrightarrow T \langle \phi \rangle,\text{ for all sentences } \phi. $$

Here $T$ is the predicate intended to express truth and $\langle \phi \rangle$ is a *name* for the sentence $\phi$. Applying the predicate $T$ to the name $\langle \phi \rangle$ gives the expression $T\langle \phi \rangle$ intended to represent the phrase “$\phi$ is true”. Schema $T$ thus expresses that for every sentence $\phi , \phi$ holds if and only if the sentence “$\phi$ is true” holds. The $T$-schema is usually regarded as a set of sentences within a formal theory. It is customary to use first-order arithmetic, that is, first-order predicate logic extended with a set of standard axioms for arithmetic like PA (Peano Arithmetic) or Robinson’s Q. What is being said in the following will apply to any such first-order formalisation of arithmetic. In this setting, $\langle \phi \rangle$ above denotes the *Gödel code* of $\phi$, and $T\langle \phi \rangle$ is short for $T(\langle \phi \rangle)$. The reader not familiar with Gödel codings (also known as Gödel numberings) can just think of the mapping $\langle \cdot \rangle$ as a naming device or quotation mechanism for formulae—just like quotation marks in natural language. Often used notational variants for $\langle \phi \rangle$ are $\ulcorner \phi \urcorner$ and ‘$\phi$’.

Tarski showed that the liar paradox is formalisable in any formal theory containing his schema T, and thus any such theory must be inconsistent. This result is often referred to as *Tarski’s theorem on the undefinability of truth*. The result is basically a formalisation of the liar paradox within first-order arithmetic extended with the $T$-schema. In order to construct such a formalisation it is necessary to be able to formulate self-referential sentences (like the liar sentence) within first-order arithmetic. This ability is provided by the diagonal lemma.

> **Diagonal lemma.**
> Let $S$ be a theory extending first-order arithmetic. For every formula $\phi(x)$ there is a sentence $\psi$ such that $S \vdash \psi \leftrightarrow \phi \langle \psi \rangle$.

Here the notation $S \vdash \alpha$ means that $\alpha$ is provable in the theory S, and $\phi \langle \psi \rangle$ is short for $\phi(\langle \psi \rangle)$. Assume a formula $\phi(x)$ is given that is intended to express some property of sentences – truth, for instance. Then the diagonal lemma gives the existence of a sentence $\psi$ satisfying the biimplication $\psi \leftrightarrow \phi \langle \psi \rangle$. The sentence $\phi \langle \psi \rangle$ can be thought of as expressing that the sentence $\psi$ has the property expressed by $\phi(x)$. The biimplication thus expresses that $\psi$ is equivalent to the sentence expressing that $\psi$ has property $\phi$. One can therefore think of $\psi$ as a sentence *expressing of itself* that it has property $\phi$. In the case of truth, it would be a sentence expressing of itself that it is true. The sentence $\psi$ is of course not self-referential in a strict sense, but mathematically it behaves like one. It is therefore possible to use sentences generated by the diagonal lemma to formalise paradoxes based on self-referential sentences, like the liar. The diagonal lemma is sometimes called the *fixed-point lemma*, since the equivalence $\psi \leftrightarrow \phi \langle \psi \rangle$ can be seen as expressing that $\psi$ is a fixed-point of $\phi(x)$.

A theory in first-order predicate logic is called *inconsistent* if a logical contradiction is provable in it. Tarski’s theorem (on the undefinability of truth) may now be stated and proved.

**Tarski’s theorem.** Any theory extending first-order arithmetic and containing schema $T$ is inconsistent.

*Proof.* Assume the existence of a consistent formal theory $S$ extending first-order arithmetic and containing schema $T$. We need to show that this assumption leads to a contradiction. The proof mimics the liar paradox. Apply the diagonal lemma to obtain a sentence $\lambda$ satisfying $\lambda \leftrightarrow \neg T \langle \lambda \rangle$ in S. The sentence $\lambda$ expresses of itself that it is not true, so $\lambda$ corresponds to the liar sentence. Instantiating schema $T$ with the sentence $\lambda$ gives us $\lambda \leftrightarrow T\langle \lambda \rangle$. We now have that both $\lambda \leftrightarrow \neg T\langle \lambda \rangle$ and $\lambda \leftrightarrow T\langle \lambda \rangle$ hold in $S$ (are provable in $S)$, and thus $T\langle \lambda \rangle \leftrightarrow \neg T\langle \lambda \rangle$ must hold in $S$. This contradicts $S$ being consistent. $\Box$

Note that the contradiction $T\langle \lambda \rangle \leftrightarrow \neg T\langle \lambda \rangle$ above expresses: The liar sentence is true if and only if it is not. Compare this to the informal liar presented in the beginning of the article. Tarski’s theorem shows that, in the setting of first-order arithmetic, it is not possible to give what Tarski considers to be an “adequate theory of truth”. The central question then becomes: How may the formal setting or the requirements for an adequate theory of truth be modified to regain consistency—that is, to prevent the liar paradox from trivialising the system? There are many different answers to this question, as there are many different ways to regain consistency. In Section 3 we will review the most influential approaches.

### 2.2 Consequences of the Set-Theoretic Paradoxes

The set-theoretic paradoxes constitute a significant challenge to the foundations of mathematics. They show that it is impossible to have a concept of set satisfying the *unrestricted comprehension principle* (also called *full comprehension* or *unrestricted abstraction*):

> **Unrestricted comprehension:**
> $\forall u (u \in \{ x \mid \phi(x)\} \leftrightarrow \phi(u))$, for all formulae $\phi(x)$.

In an informal setting, the formulae $\phi(x)$ could be allowed to be arbitrary predicates. In a more formal setting they would be formulae of e.g. a suitable first-order language. The unrestricted comprehension principle says that for any property (expressed by $\phi)$ there is the *set* of those entities that satisfy the property. This sounds as a very reasonable principle, and it more or less captures the intuitive concept of a set. Indeed, it is the concept of set originally brought forward by the father of set theory, Georg Cantor (1895), himself. Unfortunately, the principle is not sound, as it gives rise to Russell’s paradox. Consider the property of non-self-membership. This can be expressed by the formula $x \not\in x$. If we let $\phi(x)$ be the formula $x \not\in x$ then the set $\{ x \mid \phi(x) \}$ becomes the Russell set $R$, and we obtain the following instance of the unrestricted comprehension principle:

$$ \forall u (u \in R \leftrightarrow u \not\in u). $$

Analogous to the argument in Russell’s paradox a contradiction is now obtained by instantiating $u$ with $R$:

$$ R \in R \leftrightarrow R \not\in R. $$

This contradiction expresses that the Russell set is a member of itself if and only if it is not. What has hereby been proven is the following.

> **Theorem (Inconsistency of Naive Set Theory).**
> Any theory containing the unrestricted comprehension principle is inconsistent.

Compare this theorem with Tarski’s theorem. Tarski’s theorem expresses that if we formalise the intuitively most obvious principle concerning truth we end up with an inconsistent theory. The theorem above expresses that the same thing happens when formalising the intuitively most obvious principle concerning set existence and membership.

Given the inconsistency of unrestricted comprehension, the objective becomes to find a way to restrict either the comprehension principle itself or the underlying logical principles to regain a consistent theory, that is, a set theory that will not be trivialised by Russell’s paradox. Many alternative set theories excluding the unrestricted comprehension principle have been developed during the last century, among them the type theory of Russell and Whitehead, Simple Type theory (ST), Gödel-Bernays set theory (GB), Zermelo-Fraenkel set theory (ZF), and Quine’s New Foundations (NF). These are all believed to be consistent, although no simple proofs of their consistency are known. At least they all escape the known paradoxes of self-reference. We will return to a discussion of this in Section 3.

### 2.3 Consequences of the Epistemic Paradoxes

The epistemic paradoxes constitute a threat to the construction of formal theories of knowledge, as the paradoxes become formalisable in many such theories. Suppose we wish to construct a formal theory of *knowability* within an extension of first-order arithmetic. The reason for choosing to formalise knowability rather than knowledge is that knowledge is always relative to a certain agent at a certain point in time, whereas knowability is a universal concept like truth. We could have chosen to work directly with knowledge instead, but it would require more work and make the presentation unnecessarily complicated. To formalise knowability we introduce a special predicate $K$, and use sentences of the form $K\langle \phi \rangle$ to express that $\phi$ is knowable. Analogous to the cases of truth and set membership, there must be certain logical principles that $K$ needs to satisfy in order for our formal theory to qualify as an adequate theory of knowability. First of all, all knowable sentences must be true. This property can be formalised by the following logical principle:

**A1.**

$K\langle \phi \rangle \rightarrow \phi$, for all sentences $\phi$.

Of course this principle must itself be knowable, that is, we get the following logical principle:

**A2.**

$K\langle K\langle \phi \rangle \rightarrow \phi \rangle$, for all sentences $\phi$.

In addition, all theorems of first-order arithmetic ought to be knowable:

**A3.**

$K\langle \phi \rangle$, for all sentences $\phi$ of first-order arithmetic.

Furthermore, knowability must be closed under logical consequences:

**A4.**

$K\langle \phi \rightarrow \psi \rangle \rightarrow (K\langle \phi \rangle \rightarrow K\langle \psi \rangle)$,   for all sentences $\phi$.

Now, the principles A1–A4 is all it takes to formalise the paradox of the knower. More precisely, we have the following theorem, from Montague (1963), whose proof may be given in the following form (see Bolander 2004)[^bolander-2004].

**Montague’s theorem.** Any formal theory extending first-order arithmetic and containing axiom schemas A1–A4 is inconsistent.

*Proof.* Assume the existence of a consistent formal theory $S$ extending first-order arithmetic and containing axiom schemas A1–A4. We need to show that this assumption leads to a contradiction. The proof mimics the paradox of the knower. Apply the diagonal lemma to obtain a sentence $\lambda$ satisfying $\lambda \leftrightarrow \neg K \langle \lambda \rangle$ in $S$. The sentence $\lambda$ expresses of itself that it is not knowable, so $\lambda$ roughly corresponds to the knower sentence, $KS$. The first piece of argumentation used in the paradox of the knower led to the conclusion that $KS$ is indeed true. This piece of argumentation is mimicked by the following piece of formal reasoning within $S$:

| 1. | $\lambda \rightarrow \neg K\langle \lambda \rangle$ | by choice of $\lambda$ |
| --- | --- | --- |
| 2. | $\neg K\langle \lambda \rangle \rightarrow \lambda$ | by choice of $\lambda$ |
| 3. | $K\langle \lambda \rangle \rightarrow \lambda$ | axiom A1 |
| 4. | $(K\langle \lambda \rangle \rightarrow \lambda) \rightarrow$ $ ((\lambda \rightarrow \neg K\langle \lambda \rangle) \rightarrow \neg K\langle \lambda \rangle)$ | propositional tautology |
| 5. | $(\lambda \rightarrow \neg K\langle \lambda \rangle) \rightarrow \neg K\langle \lambda \rangle$ | modus ponens on 4,3 |
| 6. | $\neg K\langle \lambda \rangle$ | modus ponens on 5,1 |
| 7. | $\lambda$ | modus ponens on 2,6 |

This proof shows that $\lambda$, our formal version of $KS$, is provable in $S$. The proof corresponds to the informal argument that $KS$ is true. As argued in the paradox of the knower, any agent with sufficient reasoning capabilities will be able to prove the truth of $KS$, and thus come to know that $KS$ holds. Thus $KS$ must be knowable. What this means in the present formal framework is that we can also prove the knowability of $\lambda$ in $S$:

| 8. | $K\langle \lambda \rightarrow \neg K\langle \lambda \rangle \rangle$ | by A3 and choice of $\lambda$ |
| --- | --- | --- |
| 9. | $K\langle \neg$K$\langle \lambda \rangle \rightarrow \lambda \rangle$ | by A3 and choice of $\lambda$ |
| 10. | $K\langle K \langle \lambda \rangle \rightarrow \lambda \rangle$ | axiom A2 |
| 11. | $K\langle(K\langle \lambda \rangle \rightarrow \lambda) \rightarrow$ $ ((\lambda \rightarrow \neg K\langle \lambda \rangle) \rightarrow \neg K\langle \lambda \rangle)\rangle$ | axiom A3 on propositional tautology |
| 12. | $K\langle(\lambda \rightarrow \neg K\langle \lambda \rangle) \rightarrow \neg K\langle \lambda \rangle \rangle$ | axiom A4 on 11,10 |
| 13. | $K\langle \neg K\langle \lambda \rangle \rangle$ | axiom A4 on 12,8 |
| 14. | $K\langle \lambda \rangle$ | axiom A4 on 9,13 |

This completes the proof of the knowability of $\lambda$, corresponding to the informal argument that $KS$ is known by some agent. Note the similarity between the two pieces of proof in lines 1–7 and 8–14. The only difference is that in the latter all formulae are preceded by an extra K. This is because lines 8–14 express the same line of reasoning as lines 1–7 with the only difference that the latter is a proof of the *knowability* of $\lambda$ rather than the *truth* of $\lambda$. Having concluded that $\lambda$ is both true and knowable, we now immediately obtain a contradiction as in the paradox of the knower:

| 15. | $\neg K\langle \lambda \rangle$ | modus ponens on 1,7 |
| --- | --- | --- |
| 16. | $K\langle \lambda \rangle \wedge \neg K\langle \lambda \rangle$ | conjunction of 14 and 15 |

This completes the proof of Montague’s theorem. $\Box$

The above proof directly mimicks the reasoning underlying the paradox of the knower. Montague’s theorem shows that in the setting of first-order arithmetic we cannot have a theory of knowledge or knowability satisfying even the basic principles A1–A4. Montague’s theorem is a generalisation of Tarski’s theorem. If a predicate symbol $K$ satisfies Tarski’s schema $T$ then it is easy to see that it will also satisfy axiom schemas A1–A4. Thus axiom schemas A1–A4 constitute a weakening of the $T$-schema, and Montague’s theorem shows that even this much weaker version of the $T$-schema is sufficient to produce inconsistency. One possible reply might be that even axiom schemas A1–A4 are too strong, and should be weakened further. However, as in the previous formalisations of paradoxes, it’s not clear how to weaken the assumptions further, as all assumptions seem sensible and natural for the concept we’re formalising (knowability in this case). Another possible way out of the inconsistency result might be to preserve the principles in their current form, but only apply them to a subset of the available sentences (meaning that A1–A4 are only required to hold for sentences $\phi \in S$ for some subset $S$). The principles should hold for all “normal” sentences, but we might not want to insist on them holding for certain pathological sentences expressing self-referential statements. It is however not at all clear that we can sensibly point out exactly which sentences are normal and which are pathological. But we might still be able to find *some* sensible subsets to which we can instantiate our principles and still have a consistent theory. Revières and Levesque (1988) showed that the principles stay consistent when only instantiated over the so-called *regular sentences*, and this result was later generalised to the more inclusive class of so-called *RPQ sentences* (Morreau and Kraus, 1998)[^morreau-1998]. Most solutions to the paradox-driven inconsistency results are actually of this kind: stratify or limited the applicability of the principles that lead to inconsistency, whether it’s the principles of truth, set existence, knowability or something fourth. We will look much more into this in Section 3.

Formalising knowledge as a predicate in a first-order logic is referred to as the *syntactic treatment* of knowledge. Alternatively, one can choose to formalise knowledge as a modal operator in a suitable modal logic. This is referred to as the *semantic treatment* of knowledge (see the entry on epistemic logic). In the semantic treatment of knowledge, one generally avoids problems of self-reference, and thus inconsistency, but it is at the expense of the expressive power of the formalism (the problems of self-reference are avoided by propositional modal logic not admitting anything equivalent to the diagonal lemma for constructing self-referential formulas). In fact, the regular sentences mentioned above are achieved exactly by a translation of first-order modal logic into predicate logic, so only instantiating the principles over the regular sentences is a way of following the syntactic treatment of knowledge, but still ensure consistency by limiting the knowledge operator to the expressivity it has in the semantic treatment.

### 2.4 Consequences Concerning Provability and Computability

The central argument given in the proof of Tarski’s theorem is closely related to the central argument in Gödel’s first incompleteness theorem (Gödel, 1931)[^gödel-1931]. Gödel’s theorem can be given the following formulation.

> **Gödel’s first incompleteness theorem.**
> If first-order arithmetic is $\omega$-consistent, then it is incomplete.

A theory is called $\omega$-*consistent* if the following holds for every formula $\phi(x)$ containing $x$ as its only free variable: If $\vdash \neg \phi(n)$ (meaning: $\neg \phi(n)$ is provable) for every natural number $n$ then $\not\vdash \exists x\phi(x)$ (meaning: $\exists x\phi(x)$ is not provable). $\omega$-consistency is a stronger condition than ordinary consistency, so any $\omega$-consistent theory will also be consistent. A theory is *incomplete* if it contains a formula which can neither be proved nor disproved.

*Proof sketch of Gödel’s first incompleteness theorem*. Assume first-order arithmetic is both $\omega$-consistent and complete. We need to show that this leads to a contradiction. Gödel constructs a formula *Bew* (for “Beweis”) in formal arithmetic satisfying, for all $\phi$ and all $n$,

**(1)**

$\vdash$*Bew*$(n, \langle \phi \rangle)$ iff $n$ is the Gödel code of a proof of $\phi$.

Assuming the theory to be $\omega$-consistent and complete we can prove that for all sentences $\phi$,

**(2)**

$\vdash \exists x$*Bew*$(x, \langle \phi \rangle)$ iff $\vdash \phi$.

The proof of (2) runs like this. First we prove the implication from left to right. If $\vdash \exists x$*Bew*$(x, \langle \phi \rangle)$ then there is some $n$ such that $\not\vdash \neg$*Bew*$(n, \langle \phi \rangle)$, by $\omega$-consistency. By completeness we get $\vdash$*Bew*$(n, \langle \phi \rangle)$ for this $n$. By (1) above we get that $n$ denotes a proof of $\phi$. That is, $\phi$ is provable, so we have $\vdash \phi$. To prove the implication from right to left, note that if $\vdash \phi$ then there must be an $n$ such that $\vdash$ *Bew*$(n, \langle \phi \rangle)$, by (1). From this we get $\vdash \exists x$*Bew*$(x, \langle \phi \rangle)$, as required. This concludes the proof of (2). Now, when in a complete theory we have (2), we must also have:

**(3)**

$\vdash \exists x$*Bew*$(x, \langle \phi \rangle) \leftrightarrow \phi$, for all sentences $\phi$.

If we let $\exists x$*Bew*$(x, \langle \phi \rangle)$ be abbreviated $T\langle \phi \rangle$ then (3) becomes:

$$ \vdash T\langle \phi \rangle \leftrightarrow \phi, \text{ for all sentence } \phi. $$

This is the $T$-schema! Thus if we assume first-order arithmetic to be $\omega$-consistent and complete then schema $T$ turns out to be interpretable in it. Now, Tarski’s theorem above shows that there exists no such consistent theory, and we thus have a contradiction. $\Box$

In the proof above we reduced Gödel’s incompleteness theorem to an application of Tarski’s theorem in order to show the close link between the two (this version of the proof is due to Bolander, 2002)[^bolander-2002]. Gödel was well aware of this link, and indeed it seems that Gödel even proved Tarski’s theorem before Tarski himself did (Feferman, 1984)[^feferman-1984]. Gödel’s theorem can be interpreted as demonstrating a limitation in what can be achieved by purely formal procedures. It says that if first-order arithmetic is $\omega$-consistent (which it is believed to be), then there must be arithmetical sentences that can neither be proved nor disproved by the formal procedures of first-order arithmetic. One might at first expect this limitation to be resolvable by the inclusion of additional axioms, but Gödel showed that the incompleteness result still holds when first-order arithmetic is extended with an arbitrary finite set of axiom schemas (or, more generally, an arbitrary recursive set of axioms). Thus we obtain a general limitation result saying that there cannot exist a formal proof procedure by which any given arithmetical sentence can be proven to hold or not to hold. For more details on Gödel’s incompleteness theorem, see the entry on Kurt Gödel.

The limitation result of Gödel’s theorem is closely related to another limitation result known as the *undecidability of the halting problem*. This is a result stating that there are limitations to what can be computed. We will present this result in the following. The result is based on the notion of a *Turing machine*, which is a generic model of a computer program running on a computer having unbounded memory. Thus any program running on any computer can be thought of as a Turing machine (see the entry on Turing machines for more details). When running a Turing machine, it will either terminate after a finite number of computation steps, or it will continue running forever. In case it terminates after a finite number of computation steps, we say that it *halts*. The *halting problem* is the problem of finding a Turing machine that can decide whether other Turing machines halt or not. We say that a Turing machine $H$ *decides the halting problem* if the following holds:

> $H$ takes as input a pair $(\langle A\rangle ,x)$ consisting of the Gödel code $\langle A\rangle$ of a Turing machine $A$ and an arbitrary string $x. H$ returns the answer “yes” if the Turing machine $A$ halts when given input $x$, and “no” otherwise.

Thus if a Turing machine $H$ decides the halting problem, we can use it to determine for an arbitrary Turing machine $A$ and arbitrary input $x$ whether $A$ will halt on input $x$ or not. The *undecidability of the halting problem* is the following result, due to Turing (1937), stating that no such machine can exist:

**Theorem (Undecidability of the Halting Problem).** There exists no Turing machine deciding the halting problem.

*Proof.* Assume the existence of a Turing machine $H$ deciding the halting problem. We need to show that this assumption leads to a contradiction. The proof mimics Grelling’s paradox. We call a Turing machine $A$ *heterological* if $A$ doesn’t halt on input $\langle A\rangle$, that is, if $A$ doesn’t halt when given its own Gödel code as input. Using $H$, we can construct a Turing machine $G$ that halts if and only if it is given the Gödel code of a heterological Turing machine as input. $G$ works as follows:

> $G$ takes as input the Gödel code of a Turing machine $A$. Then it runs $H$ on input $(\langle A\rangle ,\langle A\rangle)$. If $H$ on input $(\langle A\rangle ,\langle A\rangle)$ returns “no”, $G$ is halted. If, on the other hand, $H$ on input $(\langle A\rangle ,\langle A\rangle)$ returns “yes”, then $G$ is forced into an infinite loop (that is, is forced to never halt).

In analogy to Grelling’s paradox we can now ask whether $G$ is a heterological Turing machine or not. This leads to the following sequence of equivalences:

$$\begin{align*} &G \text{ is heterological } \\ &\Leftrightarrow G \text{ doesn’t halt on input } \langle G\rangle \quad \text{(by def. of being heterological)} \\ &\Leftrightarrow H \text{ returns “no” on input } (\langle G\rangle ,\langle G\rangle) \quad \text{(since }H\text{ decides the halting prob.)} \\ &\Leftrightarrow G \text{ halts on input } \langle G\rangle \quad \text{(by construction of }G\text{)} \\ &\Leftrightarrow G \text{ is not heterological} \quad \text{(by def. of being heterological)} \end{align*}$$

This gives the required contradiction. $\Box$

From the two theorems above we see that in the areas of provability and computability, the paradoxes of self-reference turn into limitation results: there are limits to what can be proven and what can be computed. This is actually quite similar to what happened in the areas of semantics, set theory and epistemology: The paradoxes of self-reference turned into theorems showing that there are limits to which properties we can consistently assume a truth predicate to have (Tarski’s theorem), a set theory to have (inconsistency of naive set theory), and a knowledge predicate to have (Montague’s theorem). It is hard to accept these limitation results because most of them conflict with our intuitions and expectations. The central role played by self-reference in all of them potentially makes them even harder to accept, at least it definitely makes them more puzzling. However, we are forced to accept them, and forced to accept the fact that in these areas we cannot have all we might (otherwise) reasonably ask for.

## 3. Solving the Paradoxes

The present section takes a look at how to solve—or rather, circumvent—the paradoxes. To solve or circumvent a paradox one has to weaken some of the assumptions leading to the contradiction. It is very difficult to choose which assumptions to weaken, since each of the explicitly stated assumptions underlying a paradox appears to be “obviously true”—otherwise it would not qualify as a paradox. Below we will take a look at the most influential approaches to solving the paradoxes.

So far the presentation has been structured according to type of paradox, that is, the semantic, set-theoretic and epistemic paradoxes have been dealt with separately. However, it has also been demonstrated that these three types of paradoxes are similar in underlying structure, and it has been argued that a solution to one should be a solutions to all (the principle of uniform solution). Therefore, in the following, the presentation will be structured not according to type of paradox but according to type of solution. Each type of solution considered in the following can be applied to any of the paradoxes of self-reference, although in most cases the constructions involved were originally developed with only one type of paradox in mind.

### 3.1 Building Explicit Hierarchies

Building hierarchies is a method to circumvent both the set-theoretic, semantic and epistemic paradoxes. Russell’s original solution to his paradox—as well as Tarski’s original solution to his *undefinability of truth* problem—was to build hierarchies. In Russell’s case, this led to *type theory*. In Tarski’s case, it led to what is now known as *Tarski’s hierarchy of languages*. In both cases, the idea is to stratify the universe of discourse (sets, sentences) into levels. In type theory, these levels are called *types*. The fundamental idea of type theory is to introduce the constraint that any set of a given type may only contain elements of lower types (that is, may only contain sets which are located lower in the stratification). This effectively blocks Russell’s paradox, since no set can then be a member of itself.

In Tarski’s case, the stratification is obtained in the following way. Assume one wants to equip a language $L_0$ with a truth predicate. From Tarski’s theorem (Section 2.1) it is known that this truth predicate cannot be part of the language $L_0$ itself—at least not as long as we want the truth predicate to satisfy schema $T$. Instead one builds a hierarchy of languages, $L_0, L_1, L_2,\ldots$, where each language $L_{i+1}$ has a truth predicate $T_{i+1}$ that only applies to the sentences of $L_j, j\le i$. In this hierarchy, $L_0$ is called the *object language* and, for all $i, L_{i+1}$ is called the *meta-language* of $L_i$. This hierarchy effectively blocks the liar paradox, since now a sentence can only express the truth or untruth of sentences at lower levels, and thus a sentence such as the liar that expresses its *own* untruth cannot be formed.

Russell’s type theory can be regarded as a solution to Russell’s paradox, since type theory demonstrates how to “repair” set theory such that the paradox disappears. Similarly, Tarski’s hierarchy can be regarded as a solution to the liar paradox. It is the same stratification idea that underlies both of Russell’s and Tarski’s solutions. The point to note is that Russell’s paradox and the liar paradox depend crucially on circular notions (*self*-membership and *self*-reference). By making a stratification in which an object may only contain or refer to objects at lower levels, circularity disappears. In the case of the epistemic paradoxes, a similar stratification could be obtained by making an explicit distinction between first-order knowledge (knowledge about the external world), second-order knowledge (knowledge about first-order knowledge), third-order knowledge (knowledge about second-order knowledge), and so on. This stratification actually comes for free in the semantic treatment of knowledge, where knowledge is formalised as a modal operator.

Building explicit hierarchies is sufficient to avoid circularity, and thus sufficient to block the standard paradoxes of self-reference. However, there also exist paradoxes such as Yablo’s that do not rely on circularity and self-reference. Such paradoxes can also be blocked by a hierarchy approach, but it is necessary to further require the hierarchy to be well-founded, that is, to have a lowest level. Otherwise, the paradoxes of non-wellfoundedness can still be formulated. For instance, Yablo’s paradox may be formalised in a *descending* hierarchy of languages. A descending hierarchy of languages consists of languages $L_0, L_{-1}, L_{-2},\ldots$ where each language $L_{-i}$ has a truth predicate that only applies to the sentences of the languages $L_{-j}, j\gt i$. Similarly, a set-theoretic paradox of non-wellfoundedness may be formulated in a type theory allowing negative types. The conclusion drawn is that a stratification of the universe is not itself sufficient to avoid all paradoxes—the stratification also has to be well-founded.

Building an explicit (well-founded) hierarchy to solve the paradoxes is today by most considered an overly drastic and heavy-handed approach. The hierarchies introduce a number of complicating technicalities not present in a “flat universe”, and even though the paradoxes do indeed disappear, so do all non-paradoxical occurrences of self-reference. Kripke (1975) gives the following illustrative example taken from ordinary discourse. Let $N$ be the following statement, made by Nixon,

**$(N)$**

All of Jones’ utterances about Watergate are true,

and let $J$ be the following statement, made by Jones,

**$(J)$**

Most of Nixon’s utterances about Watergate are false.

In a Tarskian language hierarchy, the sentence $N$ would have to be on a higher level than all of Jones’ utterances, and, conversely, the sentence $J$ would have to be on a higher level than all of Nixon’s utterances. Since $N$ is an utterance of Nixon, and $J$ is an utterance of Jones, $N$ would have to be on a higher level than $J$, and $J$ on a higher lever than $N$. This is obviously not possible, so in a hierarchy like the Tarskian, these sentences cannot even be formulated. The sentences $N$ and $J$ are indeed both indirectly self-referential, since $N$ makes reference to a totality including $J$, and $J$ makes reference to a totality including $N$. Nevertheless, in most cases $N$ and $J$ are harmless, and do not produce a paradox. A paradox is only produced in the special case where all of Jones’ utterances except possibly $J$ are true, and exactly half of Nixon’s utterances are false, disregarding $N$. Kripke uses the fact that $N$ and $J$ are only problematic in a certain special case as an argument against an approach that altogether excludes the possibility of formulating $N$ and $J$.

Another argument against the hierarchy approach is that explicit stratification is not part of ordinary discourse, and thus it might be considered somewhat *ad hoc* to introduce it into formal settings with the sole purpose of circumventing the paradoxes. Not having an explicit stratification in ordinary discourse obviously doesn’t imply the non-existence of an underlying, implicit, stratification, but at least it’s not explicitly represented in our syntax.

The arguments given above are among the reasons the work of Russell and Tarski has not been considered to furnish the final solutions to the paradoxes. Many alternative solutions have been proposed. One might for instance try to look for *implicit* hierarchies rather than *explicit* hierarchies. An implicit hierarchy is a hierarchy not explicitly reflected in the syntax of the language. In the following section we will consider some of the solutions to the paradoxes obtained by such implicit stratifications.

### 3.2 Building Implicit Hierarchies

Tarski’s hierarchy approach to the semantic paradoxes dominated the field until 1975, when Kripke published his famous and highly influential paper, “Outline of a Theory of Truth”. This paper has greatly shaped most later approaches to theories of truth and the semantic paradoxes. It should be noted, however, that ideas quite similar to Kripke’s were developed simultaneously and independently by Martin and Woodruff (1975), and that a parallel approach in a set-theoretic setting was developed independently by Gilmore (1974).

#### 3.2.1 Kripke’s Theory of Truth

Kripke’s ideas are based on an analysis of the problems involved in Tarski’s hierarchy approach. Kripke lists a number of arguments against having a language hierarchy in which each sentence lives at a fixed level, determined by its syntactic form. He proposes an alternative solution which still uses the idea of having levels, but where the levels are not becoming an explicit part of the syntax. Rather, the levels become stages in an iterative construction of a truth predicate. To explain Kripke’s construction, some additional technical machinery is required.

At each stage in Kripke’s construction, the truth predicate is only *partially defined*, that is, it only applies to some of the sentences of the language. To deal with such partially defined predicates, a *three-valued logic* is employed, that is, a logic which operates with a third value, *undefined*, in addition to the truth values *true* and *false*. Often the third value is denoted “$u$” or “$\bot$” (bottom). A partially defined predicate only receives one of the classical truth values, *true* or *false*, when it is applied to one of the terms for which the predicate has been defined, and otherwise it receives the value *undefined*. There are several different three-valued logics available, differing in how they treat the third value. Here only one of them is briefly described, called *Kleene’s strong three-valued logic*. More detailed information on this and related logics can be found in the entry on many-valued logic.

In Kleene’s strong three-valued logic, the value $\bot$ (*undefined*) can be interpreted as “not yet defined”. So one could think of formulae with the value $\bot$ as formulae that actually have a classical truth value (*true* or *false*), but which has just not been determined yet. This interpretation of *undefined* is reflected in the truth tables for the logic, given below. The upper truth table is for disjunction, the lower for negation:

| $\vee$ | true | false | $\bot$ |
| --- | --- | --- | --- |
| true | true | true | true |
| false | true | false | $\bot$ |
| $\bot$ | true | $\bot$ | $\bot$ |

| $\neg$ |   |
| --- | --- |
| true | false |
| false | true |
| $\bot$ | $\bot$ |

These truth tables define the three-valued logic completely, as $\vee$ and $\neg$ are taken to form an adequate set of connectives and existential and universal quantification are treated as infinite disjunction and conjunction, respectively.

To handle partially defined truth predicates, it is necessary to introduce the notion of partial models. In a *partial model* for a first-order language, each $n$-place predicate symbol $P$ is interpreted by a pair $(U,V)$ of disjoint $n$-place relations on the domain of the model. $U$ is called the *extension* of $P$ and $V$ its *anti-extension*. In the model, $P$ is true of the objects in $U$, false of the objects in $V$, and undefined otherwise. In this way, any atomic sentence receives one of the truth values *true*, *false* or *undefined* in the model. Non-atomic formulae are given truth values in the model by using Kleene’s strong three-valued logic for evaluating the connectives.

Given the definition of a partial model, a *partially interpreted language* is a pair $(L,M)$ where $L$ is a first-order language and $M$ is a partial model of $L$. Kripke recursively defines a sequence of partially interpreted languages $L_0, L_1, L_2,\ldots$, only differing in their interpretation of the truth predicate $T$. The first language, $L_0$, is taken to be an arbitrary language in which both the extension and anti-extension of $T$ are the empty set. Thus in $L_0$, the truth predicate is completely undefined. For any $\alpha$, the language $L_{\alpha +1}$ is like $L_{\alpha}$ except that $T$ is interpreted by the extension/anti-extension pair $(U,V)$ given by:

- $U$ is the set of Gödel codes $\langle \phi \rangle$ of sentences $\phi$ true in $L_{\alpha}$.
- $V$ is the set of Gödel codes $\langle \phi \rangle$ of sentences $\phi$ false in $L_{\alpha}$.

This definition immediately gives that for all $\alpha$,

**(4)**

$\phi$ is true (false) in $L_{\alpha} \Leftrightarrow T\langle \phi \rangle$ is true (false) in $L_{\alpha +1}$.

What has been constructed is a sequence $L_0, L_1, L_2,\ldots$ of partially interpreted languages such that $T$ is interpreted in $L_{\alpha +1}$ as the truth predicate for $L_{\alpha}$. This is just like Tarski’s hierarchy of languages, except that here there is no syntactic distinction between the different languages and their truth predicates.

The sequence $L_0, L_1, L_2,\ldots$ has an important property: For each $\alpha$, the interpretation of $T$ in $L_{\alpha +1}$ extends the interpretation of $T$ in $L_{\alpha}$, that is, both the extension and anti-extension of $T$ increase (or stay the same) when moving from $L_{\alpha}$ to $L_{\alpha +1}$. This means that one can define a new partially interpreted language $L_{\omega}$ by letting the extension of $T$ be the union of all the extensions of $T$ in $L_0, L_1, L_2,\ldots$; and similarly for the anti-extension. Thus in $L_{\omega}$, the interpretation of $T$ extends the interpretation that $T$ receives in all previous languages. This furnishes a strategy for continuing the iterative construction of a truth predicate into the transfinite: For each successor ordinal $\alpha +1$, define $L_{\alpha +1}$ from $L_{\alpha}$ exactly as in the finite case above; and for each limit ordinal $\sigma$, define $L_{\sigma}$ from the preceding languages $(L_i)_{i\lt \sigma}$ in the same way as $L_{\omega}$ was defined (for a detailed explanation of the ordinal numbers and their use in this context, see the entry on the revision theory of truth). A simple cardinality consideration now shows that this transfinite sequence of languages will eventually *stabilise*: There is an ordinal $\gamma$ such that $L_{\gamma} = L_{\gamma +1}$. Hence the following instance of (4) is obtained:

**(5)**

$\phi$ is true (false) in $L_{\gamma} \Leftrightarrow T\langle \phi \rangle$ is true (false) in $L_{\gamma}$.

This shows that $L_{\gamma}$ is actually a language containing its own truth predicate: Any sentence $\phi$ is true (false) if and only if the sentence expressing its truth, $T\langle \phi \rangle$, is true (false). The equivalence (5) is nothing more than a semantic analogue of Tarski’s schema $T$ in a three-valued setting. The construction of the language $L_{\gamma}$ was one of the major contributions of Kripke (1975). It shows that in a three-valued logical setting it is actually possible for a language to contain its own truth predicate. It is easy to see that the third value, *undefined,* is essential to making things work: If $L_{\gamma}$ had been a totally interpreted language (that is, a language with no undefined sentences), then $L_{\gamma}$ would satisfy schema T, by (5) above. However, it immediately contradicts Tarski’s theorem that such a totally interpreted language can exist.

Among the sentences that receive the value *undefined* in $L_{\gamma}$ is the liar sentence. The solution to the liar paradox implicit in Kripke’s theory is this: Since both assuming that the liar sentence is true and that it is false leads to a contradiction it must be neither, it is *undefined*. The liar sentence is said to suffer from a *truth-value gap*. The idea of avoiding the liar paradox by allowing truth-value gaps did in fact appear several times in the literature before Kripke’s paper, but Kripke was among the first to make it an integral part of a genuine theory.

As with the hierarchy solution to the liar paradox, the truth-value gap solution is by many considered to be problematic. The main criticism is that by using a three-valued semantics, one gets an interpreted language which is expressively weak. One cannot, for instance, in any of Kripke’s languages have a predicate expressing the property of being *undefined*. This is in fact noted by Kripke himself. If a partially interpreted language contained such a predicate, the following *strengthened liar sentence* within the language could be formulated: “This sentence is either false or undefined”. The strengthened liar sentence is true if and only if false or undefined, so we have a new paradox, called the *strengthened liar paradox*. The problem with the strengthened liar paradox is known as a *revenge problem*: Given any solution to the liar, it seems we can come up with a new strengthened paradox, analogous to the liar, that remains unsolved. The idea is that whatever semantic status the purported solution claims the liar sentence to have, if we are allowed freely to refer to this semantic status in the object language, we can generate a new paradox.

The inability of the Kripkean language to express its own *undefined* predicate also means that we cannot in the Kripkean object-language express a statement such as: “The liar sentence is undefined”. In fact in Kripke’s language $L_{\gamma}$, the liar sentence $is$ undefined, so the previous sentence expresses a truth about $L_{\gamma}$ that cannot be expressed within $L_{\gamma}$ itself (hence the language is expressively incomplete). To express the true statement “The liar sentence is undefined”, we are forced to ascend into a meta-language of $L_{\gamma}$. As Kripke (1975) himself puts it: “The ghost of the Tarski hierarchy is still with us.”

#### 3.2.2 Extensions and Alternatives to Kripke’s Theory of Truth

Succeeding the work of Kripke, many attempts have been made to construct languages containing their own truth predicate and not suffering from the revenge problem of strengthened liars. Many of these attempts have focused on modifying or extending the underlying strong three-valued logic, e.g. modifying the semantics of the conditional (Field, 2003, 2008)[^field-2003][^field-2008] or allowing an unbounded number of truth-values (Cook, 2007; Schlenker, 2010; Tourville and Cook, 2016)[^cook-2007][^schlenker-2010].

Kripke’s theory circumvents the liar paradox by assigning it the value *undefined*. An alternative way to circumvent the liar paradox would be to assign it the value *both true and false* in a suitable paraconsistent logic. This would be the correct solution according to the dialetheist view, cf. Section 2. One of the simplest paraconsistent logics is LP, which is a three-valued logic with the same truth tables as Kleene’s strong three-valued logic presented above—the only difference is that the third truth value is interpreted as *both true and false* rather than *undefined*. A reason for preferring a paraconsistent logic over a partial logic is that paradoxical sentences such as the liar can then be modelled as *true contradictions* (dialetheia) rather than truth-value gaps. We refer again to the entries on dialetheism and paraconsistent logic for more information.

The choice is between *truth-value gaps* and *truth-value gluts*: A truth-value gap is a statement with no truth-value, neither true or false (like *undefined* in Kleene’s strong three-valued logic), and a truth-value glut is a statement with several truth-values, e.g. both true and false (like in the paraconsistent logic LP). There are also arguments in favour of allowing both gaps and gluts, e.g. by letting the set of truth-values form of a bilattice (Fitting, 2006; Odintsov and Wansing, 2015)[^fitting-2006][^odintsov-2015]. The simplest non-trivial bilattice has exactly four values, which in the context of truth-values are interpreted as: *true*, *false*, $\bot$ (neither true nor false), and $\top$ (both true and false).

For a more extensive discussion of Kripke’s theory, its successors and rivals, see the entry on the liar paradox.

#### 3.2.3 Implicit Hierarchies in Set Theories

Building implicit rather than explicit hierarchies is also an idea that has been employed in set theory. New Foundations (NF) by Quine (1937) is a modification of simple type theory where the stratification into syntactic types has been replaced by a stratification on the comprehension principle:

> **NF comprehension:**
> $\forall u(u \in \{ x \mid \phi(x)\} \leftrightarrow \phi(u))$, for all *stratified* formulae $\phi(x)$.

A formula $\phi$ is *stratified* if there exists a mapping $\sigma$ (a *stratification*) from the variables of $\phi$ to the natural numbers such that if $u \in v$ is a subformula of $\phi$ then $\sigma(v) = \sigma(u)+1$ and if $u = v$ is a subformula of $\phi$ then $\sigma(v) = \sigma(u)$. Obviously the formula $x \not\in x$ is not stratified, and thus the NF comprehension principle cannot be used to formulate Russell’s paradox in the theory. Quine’s New Foundations is essentially obtained from type theory by hiding the types from the syntax. Thus, the theory still makes use of a hierarchy approach to avoid the paradoxes, but the hierarchy is made implicit by not representing it in the syntax of formulae. Cantini (2015) has investigated the possibility of mimicking this implicit hierarchy approach in the context of theories of truth (achieving an implicitly represented Tarskian truth hierarchy).

Zermelo-Fraenkel set theory (ZF) is another theory that builds on the idea of an implicit hierarchy to circumvent the paradoxes. However, it does so in a much less direct way than NF. In ZF, sets are built bottom-up, starting with the empty set and iterating a construction of bigger and bigger sets using the operations of union and power set. This produces a hierarchy with the empty set on the lowest level, level 0, and with the power set operation producing a set of level $\alpha +1$ from a set of level $\alpha$. Analogous to Kripke’s iterative construction, the procedure is continued into the transfinite using the union operator at the limit ordinal levels. The hierarchy obtained is called the *cumulative hierarchy*. One of the axioms of ZF, the axiom of foundation, states that every set of ZF lives on a certain level in this cumulative hierarchy. In other words, the axiom of foundation states that there are no sets in ZF besides the ones that can be constructed bottom-up by the iterative procedure just described. Since in a cumulative hierarchy, there can be no sets containing themselves, no universal set, and no non-wellfounded sets, none of the known paradoxes can immediately be formulated in the theory. This does obviously not in itself ensure the consistency of ZF, but at least it illustrates how the idea of a set hierarchy plays a significant role in ZF as well. ZF has a privileged status among set theories, as it is today the most widely acknowledged candidate for a formal foundation of mathematics.

### 3.3 General Fixed Point Approaches

Kripke’s iterative construction of a truth predicate presented above may be viewed as an instance of a more general *fixed point approach* towards building formal theories of truth. Fixed point approaches have become central to contemporary formal theories of truth. The main idea is to have a *truth revision operator* and then look for fixed points of this operator. At heart of such fixed point approaches is some suitable *fixed point theorem* guaranteeing the existence of fixed points for certain kinds of operators. There are several different fixed point theorems available. Consider now one of the simpler ones.

> **Fixed point theorem**.
> Let $\tau$ be a monotone operator on a chain complete partial order (henceforth ccpo). Then $\tau$ has a least fixed point, that is, there is a least f such that $\tau(f) = f$.

A *ccpo* is a partial order $(D,\lt)$ in which every totally ordered subset of $D$ has a least upper bound. The totally ordered subsets of $D$ are called *chains* in $D$. A *monotone operator* on $(D,\lt)$ is a mapping $\tau : D \rightarrow D$ satisfying:

$$ d_1 \le d_2 \Rightarrow \tau(d_1) \le \tau(d_2), \text{ for all } d_1, d_2 \in D. $$

Kripke’s construction fits into the fixed point theorem above in the following way. First note that the set of partially interpreted languages that only differ on the interpretation of $T$ forms a ccpo: Simply define the ordering on these languages by $L_1 \le L_2$ iff the interpretation of $T$ in $L_2$ extends the interpretation of $T$ in $L_1$ (that is, the extension and anti-extension of $T$ in $L_1$ are included in those of $L_2)$. Then define a truth revision operator $\tau$ on these languages by:

**(6)**

$\tau(L) = L'$, where $T\langle \phi \rangle$ is true (false) in $L'$ iff $\phi$ is true (false) in $L$.

Note that if $L_{\alpha}$ is one of the languages in Kripke’s construction, then $L_{\alpha +1} = \tau(L_{\alpha})$. The idea of this truth revision operator $\tau$ is that if $\tau(L)=L'$ then $L'$ will be a language in which $T$ is interpreted as the truth predicate for $L$. If therefore $\tau(L)=L$ for some $L$, that is, if $L$ is a fixed point of $\tau$, then $L$ will be a language containing its own truth predicate. This motivates the search for fixed points of $\tau$. Since $\tau$ is easily seen to be monotone, by the fixed point theorem it has a least fixed point. It is not hard to see that this fixed point is exactly the language $L_{\gamma}$ constructed in Kripke’s theory of truth. Kripke’s construction is thus recaptured in the setting of fixed points for monotone operators.

The point of introducing the additional machinery was not just to rediscover the language $L_{\gamma}$. The point is rather to have provided a much more general and abstract framework which may lead to new theories of truth and give further insights into the semantic paradoxes. It turns out that the truth revision operator $\tau$ defined above has many interesting fixed-points in addition to $L_{\gamma}$. It is also possible to obtain new theories of truth by considering alternative ways of making the set of interpreted languages into a ccpo. One may for instance add an additional truth value and consider the situation in a four-valued logic, as considered by Fitting (1997); or one may remove the third truth value *undefined* and construct a ccpo in a completely classical setting. In the classical setting, attention is restricted to the totally interpreted languages (languages in which every sentence is either true or false), and an ordering on them is defined by: $L_1 \le L_2$ holds iff the extension of the truth predicate in $L_1$ is included in the extension of the truth predicate in $L_2$, that is, iff $L_2$ points out at least as many sentences as true as $L_1$. This gives a ccpo. By using the fixed point theorem in this setting on a suitably defined revision operator, it is fairly easy to prove the existence of a totally interpreted language containing a *positive definition of truth*. By this is meant that the interpreted language has a predicate $T$ satisfying the following restricted version of the $T$-schema:

**(7)**

$\phi \leftrightarrow T(\langle \phi \rangle)$, for all *positive* sentences $\phi$,

where the positive sentences are those built without using negation $(\neg)$. Since (7) is satisfiable in a totally interpreted language, the first-order theory containing the sentences of (7) as axioms must be consistent. This should be contrasted with Tarski’s theorem stating that the *unrestricted* $T$-schema is inconsistent. If the unrestricted comprehension principle is similarly restricted to the positive formulae, we also get a consistent theory. This was originally shown by Gilmore (1974).

The fixed point approach is also the point of departure of the *revision theory of truth* developed by Belnap and Gupta (1993). The revision theory of truth is the most influential theory of truth and the semantic paradoxes that has been developed since the theory of Kripke. The revision theory considers the standard truth revision operator $\tau$ defined by (6) as an operator on the *totally* interpreted languages. On these languages $\tau$ doesn’t have a fixed point: If it had such a fixed point $L$ then $L$ would be a totally interpreted language satisfying the full schema $T$, directly contradicting Tarski’s theorem. Since $\tau$ doesn’t have a fixed point on the totally interpreted languages, the revision theory instead considers transfinite sequences $L_1, L_2$, … , $L_{\omega}, L_{\omega +1}$, … of totally interpreted languages satisfying:

- For any successor ordinal $\alpha +1, L_{\alpha +1} = \tau(L_{\alpha})$.
- For any limit ordinal $\sigma$ and any sentence $\phi$, if $\phi$ stabilises on the value true (false) in the sequence $(L_{\alpha})_{\alpha \lt \sigma}$ then $\phi$ is true (false) in $L_{\sigma}$.

In such a sequence, each sentence $\phi$ will either eventually stabilise on a classical truth value (true or false), or it will never stabilise. An example of a sentence that will never stabilise is the liar sentence: If the liar sentence is true in one of the languages $L_{\alpha}$ it will be false in $L_{\alpha +1}$, and vice versa. The revision theory thus gives an account of truth that correctly models the behaviour of the liar sentence as one that never stabilises on a truth value. In the revision theory it is argued that this gives a more correct account of truth and self-reference than Kripke’s theory in which the liar sentence is simply assigned the value undefined. Both the revision theory of truth and Kripke-style fixed-point theories are still being actively researched (Gupta and Standefer, 2017; Hsiung, 2017; Schindler, 2017)[^gupta-2017][^hsiung-2017][^schindler-2017]. A full account of the revision theory can be found in the entry on the revision theory of truth.

Studying self-referential phenomena as fixed-points is not limited to theories of truth. For instance, in the context of epistemic paradoxes, the Brandenburger-Keisler paradox has been cast as a fixed-point result by Abramsky and Zvesper (2015).

## 4. Recent Developments

Murzi and Massimiliano (2015) give an overview of recent developments in approaches to solving the paradoxes: paracompleteness (allowing truth-value gaps), paraconsistency (allowing truth-value gluts), substructural logics (weakening the logical principles of classical logic), and the revenge problems that these approaches will or could lead to. Recent developments in substructural logics as a cure to the paradoxes include French (2016) (dropping reflexivity), Caret, Colin and Weber (2015), Shapiro and Lionel (2015), Mares and Paoli (2014) (dropping contraction), and Cobreros, Égré, Ripley and van Rooij (2014) (dropping transitivity). More recently, a special volume of *Synthese* has been devoted to substructural approaches to paradox (December 2021 issue, with an introduction by Zardini, 2021)[^zardini-2021]. The volume by Achourioti et al. (eds., 2015) has several papers on self-reference and how to avoid paradoxes in the context of theories of truth.

Volker Halbach and Albert Visser (2014a, 2014b) have made a very detailed study of self-reference in arithmetic, studying what it means for a sentence of arithmetic to ascribe itself a property, and how this depends on the chosen encoding, the details of fixed-point construction etc. Albert Visser (2019) is also among the authors who have studied how little self-reference we can get away with when proving classical theorems like Gödel’s second incompleteness theorem.

There is also still work on trying to characterise what exactly it means for something to be a paradox (Hsiung, 2022)[^hsiung-2022]. This is somewhat in the spirit of Priest’s Inclosure Schemes and the graph-theoretical classifications of paradoxicality mentioned above. Finding the exact necessary and sufficient ingredients required for paradox is still an open problem. There has also been further work in defining exactly it means for something to be self-referential (Picollo, 2018, 2020)[^picollo-2018][^picollo-2020]. Grabmayr, Halbach and Ye (2023) distinguishes between genuine and accidental self-reference, and hence tries to provide a more fine-grained analysis of self-referentiality. A more fine-grained analysis of self-referentiality can also be made by taking a closer look at the kind of Gödel numbering we use (Grabmayr and Visser, 2023; Kripke, 2023)[^grabmayr-2023][^grabmayr-2023-2][^kripke-2023].

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Other Internet Resources

- [Logical Paradoxes](https://www.iep.utm.edu/p/par-log.htm), by B. Hartley Slater, in the *Internet Encyclopedia of Philosophy*.
- [Truth](https://www.iep.utm.edu/t/truth.htm), by Bradley Dowden and Norman Swartz, in the *Internet Encyclopedia of Philosophy*.

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=self-reference). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/self-reference/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=self-reference&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/self-reference/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Related Entries

Buridan, John [Jean] | computability and complexity | Curry’s paradox | dialetheism | epistemic paradoxes | Fitch’s paradox of knowability | game theory: epistemic foundations of | Gödel, Kurt | Gödel, Kurt: incompleteness theorems | insolubles [= *insolubilia*] | liar paradox | logic: epistemic | logic: many-valued | logic: paraconsistent | logic: provability | mathematics, philosophy of | mathematics: inconsistent | paradoxes: and contemporary logic | Quine, Willard Van Orman: New Foundations | Russell’s paradox | set theory | set theory: alternative axiomatic theories | set theory: early development | Tarski, Alfred: truth definitions | truth | truth: axiomatic theories of | truth: deflationism about | truth: revision theory of | Turing, Alan | Turing machines | type theory

[^abad-2008]: Abad, Jordi Valor, 2008, “The inclosure scheme and the solution to the paradoxes of self-reference”, *Synthese*, 160(2): 183–202.

[^abramsky-2015]: Abramsky, Samson, and Jonathan Zvesper, 2015, “From Lawvere to Brandenburger-Keisler: Interactive forms of diagonalization and self-reference”, *Journal of Computer and System Sciences*, 81(5): 799–812.

[^achourioti-2015]: Achourioti, T. et al. (eds.), 2015, *Unifying the Philosophy of Truth*, vol. 36 of Logic, Epistemology, and the Unity of Science, Springer.

[^badici-2008]: Badici, Emil, 2008, “The liar paradox and the inclosure schema 1”, *Australasian Journal of Philosophy*, 86(4): 583–596.

[^başkent-2016]: Başkent, Can, 2016, “A Yabloesque paradox in epistemic game theory”, *Synthese* 1–24.

[^bartlett-1992]: Bartlett, S.J. (ed.), 1992, *Reflexivity—A Source-Book in Self-Reference*, Amsterdam: North-Holland Publishing Co.

[^bartlett-1987]: Bartlett, S.J. and Peter Suber (eds.), 1987, *Self-Reference—Reflections on Reflexivity*, Dordrecht: Martinus Nijhoff Publishers.

[^barwise-1987]: Barwise, J. and J. Etchemendy, 1987, *The Liar—An Essay on Truth and Circularity*, New York: Oxford University Press.

[^barwise-1996]: Barwise, J. and L. Moss, 1996, *Vicious Circles—On the Mathematics of Non-Wellfounded Phenomena*, Stanford: CSLI Publications.

[^beall-2009]: Beall, Jc, 2009, *Spandrels of truth*, OUP Oxford.

[^beall-2003]: –––, 2003, *Liars and Heaps: New Essays on Paradox*, Oxford: Clarendon.

[^beall-2007]: –––, 2007, *Revenge of the Liar: New essays on the paradox*, Oxford: Oxford University Press.

[^beall-2014a]: –––, 2014a, “Finding tolerance without gluts”, *Mind* 123(491): 791–811.

[^beall-2014b]: –––, 2014b, “End of inclosure”, *Mind* 123(491): 829–849.

[^beringer-2017]: Beringer, T. and Schindler, T., 2017, “A Graph-Theoretic Analysis of the Semantic Paradoxes”, *The Bulletin of Symbolic Logic*, 24(4): 442–892.

[^bernardi-2001]: Bernardi, Claudio, 2001, “Fixed points and unfounded chains”, *Annals of* *Pure and Applied Logic*, 109(3): 163–178.

[^bolander-2002]: Bolander, Thomas, 2002, “Self-reference and logic”, *Phi News*, 1: 9–44.

[^bolander-2004]: –––, 2004, “Logical Theories for Agent Introspection ”, Ph.D. Thesis, Technical University of Denmark, Denmark.

[^bolander-2006]: Bolander, T. and V.F. Hendricks and S.A. Pedersen (eds.), 2006, *Self-Reference*, Stanford: CSLI Publications.

[^boolos-1993]: Boolos, G., 1993, *The Logic of Provability*, Cambridge: Cambridge University Press.

[^brandenburger-2006]: Brandenburger, Adam and Keisler, H. Jerome, 2006, “An impossibility theorem on beliefs in games”, *Studia Logica*, 84(2): 211–240.

[^bruni-2023]: Bruni, Riccardo and Lorenzo Rossi, 2023, “Truth Meets Vagueness. Unifying the Semantic and the Soritical Paradoxes”, *Journal of Philosophical Logic*, 52: 1637–1671.

[^buridan-2001]: Buridan, John, [SD], *Summulae de Dialectica–An annotated translation, with a philosophical introduction by Gyula Klima*, New Haven and London: Yale University Press, 2001.

[^butler-2017]: Butler, Jesse M., 2017, “An entirely non-self-referential Yabloesque paradox”, *Synthese* 1–13.

[^cantini-2009]: Cantini, Andrea, 2009, “Paradoxes, self-reference and truth in the 20th century”, *Handbook of the History of Logic*, 5: 875–1013.

[^cantini-1996]: –––, 1996, *Logical Frameworks for Truth and Abstraction—An Axiomatic Study*, Amsterdam: North-Holland Publishing Co.

[^cantini-2009-2]: –––, 2009, “Paradoxes, self-reference and truth in the 20th century”, *Handbook of the History of Logic*, vol. V, Amsterdam: Elsevier, pp. 875–1013.

[^cantini-2015]: –––, 2015, “On stratified truth”, in *Unifying the philosophy of truth*, Netherlands: Springer.

[^cantor-1895]: Cantor, Georg, 1895, “Beiträge zur Begründung der transfiniten Mengenlehre”, *Mathematische Annalen*, 46(4): 481–512.

[^cantor-1891]: –––, 1891, “Über eine Elementare Frage der Mannigfaltigkeitslehre,” *Jahresbericht der Deutschen Mathematiker-Vereinigung*, 1: 75–78.

[^cieśliński-2013]: Cieśliński, C. and R. Urbaniak, 2013, “Gödelizing the Yablo Sequence”, *Journal of Philosophical Logic* 42(5): 679–695.

[^caret-2015]: Caret, Colin R. and Zach Weber, 2015, “A Note on Contraction-Free Logic for Validity”, *Topoi* 34(1): 63–74.

[^chapuis-2000]: Chapuis, A. and A. Gupta, 2000, *Circularity, Definition and Truth*, New Delhi: Indian Council of Philosophical Research.

[^cobreros-2013]: Cobreros, Pablo, Paul Égré, David Ripley, and Robert van Rooij, 2013, “Reaching Transparent Truth”, *Mind* 122(488): 841–866.

[^cobreros-2015]: –––, 2015, “Vagueness, Truth and Permissive Consequence”, in T. Achourioti *et al*. (eds.), *Unifying the Philosophy of Truth*, Dordrecht: Springer, 409–430.

[^colyvan-2009]: Colyvan, Mark, 2009, “Vagueness and Truth”, in Dyke, Heather (ed.): *From Truth to Reality: New Essays in Logic and Metaphysics*, Oxford: Routledge.

[^cook-2007]: Cook, Roy, 2007, “Embracing revenge: on the indefinite extensibility of language”, *Revenge of the Liar: New Essays on the Paradox*, Oxford: Oxford University Press.

[^cook-2004]: –––, 2004, “Patterns of paradox”, *The Journal of Symbolic Logic*, 69(3): 767–774.

[^cook-2009]: –––, 2009, “What is a truth value and how many are there?”, *Studia Logica*, 92(2): 183–201.

[^cook-2013]: –––, 2013, *Paradoxes*, Polity Press.

[^cook-2014]: –––, 2014, *The Yablo paradox: An essay on circularity*, Oxford: Oxford University Press.

[^dyrkolbotn-2014]: Dyrkolbotn, S. and M. Walicki, 2014, “Propositional discourse logic”, *Synthese*, 191(5): 863–899.

[^erickson-1998]: Erickson, G. W. and J. A. Fossa, 1998, *Dictionary of Paradox*, Lanham: University Press of America.

[^feferman-1984]: Feferman, S., 1984, “Kurt Gödel: conviction and caution”, *Philosophia Naturalis*, 21: 546–562.

[^feferman-1984a]: –––, 1984a, “Toward useful type-free theories I”, *The Journal of Symbolic Logic*, 49: 75–111.

[^feferman-1991]: –––, 1991, “Reflecting on incompleteness”, *The Journal of Symbolic Logic*, 56: 1–49.

[^field-2003]: Field, Hartry, 2003, “A revenge-immune solution to the semantic paradoxes”, *Journal of Philosophical Logic*, 32(2): 139–177.

[^field-2008]: –––, 2008, *Saving truth from paradox*, Oxford University Press, USA.

[^fitting-1986]: Fitting, M., 1986, “Notes on the mathematical aspects of Kripke’s theory of truth”, *Notre Dame Journal of Formal Logic*, 27(1): 75–88.

[^fitting-1997]: –––, 1997, “A theory of truth that prefers falsehood”, *The Journal of Philosophical Logic*, 26(5): 477–500.

[^fitting-2006]: –––, 2006, “Bilattices are nice things.”, in Bolander, Hendricks, Pedersen (eds.), *Self-reference*, Stanford: CSLI Publications.

[^forster-1995]: Forster, T. E., 1995, *Set Theory with a Universal Set*, New York: The Clarendon Press.

[^french-2016]: French, Rohan, 2016, “Structural reflexivity and the paradoxes of self-reference”, *Ergo, an Open Access Journal of Philosophy* 3.

[^gaifman-1988]: Gaifman, Haim, 1988, “Operational pointer semantics: Solution to self-referential puzzles i”, in *Proceedings of the 2nd Conference on Theoretical Aspects of Reasoning about Knowledge*, Morgan Kaufmann Publishers Inc., 43–59.

[^gaifman-1992]: –––, 1992, “Pointers to truth”, *The Journal of Philosophy*, 89(5): 223–261.

[^gaifman-2000]: –––, 2000, “Pointers to propositions”, in A. Chapuis and A. Gupta, *Circularity, definition and truth*, Indian Council of Philosophical Research, 79–121.

[^gilmore-1974]: Gilmore, P. C., 1974, “The consistency of partial set theory without extensionality”, *Axiomatic set theory (Proc. Sympos. Pure Math., Vol. XIII, Part II)*, pp. 147–153, Providence RI: Amer. Math. Soc.

[^gödel-1931]: Gödel, K., 1931, “Über formal unentscheidbare Satze der Principia Mathematica und verwandter Systeme I”, *Monatshefte für Mathematik und Physik*, 38: 173–198.

[^grabmayr-2023]: Grabmayr, Balthasar, Volker Halbach, and Lingyuan Ye, 2023, “Varieties of Self-Reference in Metamathematics”. *Journal of Philosophical Logic*, 52: 1005–1052.

[^grabmayr-2023-2]: Grabmayr, Balthasar, and Albert Visser, 2023, “Self-reference upfront: A study of self-referential Gödel numberings”. *The Review of Symbolic Logic*, 16(2): 385–424.

[^gupta-1993]: Gupta, A. and N. Belnap, 1993, *The Revision Theory of Truth*, Cambridge MA: MIT Press.

[^gupta-2017]: Gupta, A. and S. Standefer, 2017, “Conditionals in theories of truth”, *Journal of Philosophical Logic* 46(1): 27–63.

[^halbach-2008]: Halbach, Volker, 2008, “On a side effect of solving Fitch’s paradox by typing knowledge”, *Analysis*, 68(298): 114–120.

[^halbach-2011]: –––, 2011, *Axiomatic theories of truth*, Cambridge: Cambridge University Press.

[^halbach-2014a]: Halbach, Volker, and Albert Visser, 2014a, “Self-reference in Arithmetic I”, *The Review of Symbolic Logic* 7(4): 671–691.

[^halbach-2014b]: –––, 2014b, “Self-reference in arithmetic II”, *The Review of Symbolic Logic* 7(4): 692–712.

[^halbach-2017]: Halbach, Volker, and Shuoying Zhang, 2017, “Yablo Without Gödel”, *Analysis* 77(1): 53–59.

[^hsiung-2017]: Hsiung, Ming, 2017, “Boolean Paradoxes and Revision Periods”, *Studia Logica*, 105(5): 881–914.

[^hsiung-2022]: –––, 2022, “From Paradoxicality to Paradox”, *Erkenntnis*, first online 06 December 2022. doi:10.1007/s10670-022-00640-9

[^heijenort-1967]: van Heijenort, J., 1967, *From Frege to Gödel. A source book in mathematical logic, 1879–1931*, Cambridge (MA): Harvard University Press.

[^horsten-2011]: Horsten, Leon, 2011, *The Tarskian Turn: Deflationism and Axiomatic Truth*, Cambridge, MA: MIT Press.

[^hughes-1982]: Hughes, G.E., 1982, *John Buridan on self-reference–Chapter Eight of Buridan’s ‘Sophismata’, with a Translation, an Introduction, and a Philosophical Commentary*, Cambridge: Cambridge University Press.

[^kaplan-1960]: Kaplan, David, and Richard Montague, 1960, “A paradox regained”, *Notre Dame Journal of Formal Logic*, 1(3): 79–90

[^kripke-1975]: Kripke, S., 1975, “Outline of a Theory of Truth”, *The Journal of Philosophy*, 72: 690–716.

[^kripke-2023]: –––, 2023, “Gödel’s theorem and direct self-reference”. *The Review of Symbolic Logic*, 16(2): 650–654.

[^leach-krouse-2014]: Leach-Krouse, Graham, 2014, “Yablifying the Rosser sentence”, Journal of Philosophical Logic 43(5): 827–834.

[^leitgeb-2008]: Leitgeb, Hannes, 2008, “On the probabilistic convention t”, *The Review of Symbolic Logic*, 1(02): 218–224.

[^mares-2014]: Mares, Edwin and Francesco Paoli, 2014, “Logical Consequence and the Paradoxes”, *Journal of Philosophical Logic*, 43(2–3): 439–469.

[^martin-1984]: Martin, R. L., 1984, *Recent Essays on Truth and the Liar Paradox*, Oxford: Oxford University Press.

[^martin-1975]: Martin, R. L. and P. W. Woodruff, 1975, “On representing ‘True-in-L’ in L”, *Philosophia*, 5: 213–217.

[^mcgee-1990]: McGee, V., 1990, *Truth, Vagueness, and Paradox—An Essay on the Logic of Truth*, Indianapolis: Hackett Publishing Co.

[^mcgee-1992]: –––, 1992, “Maximal consistent sets of instances of Tarski’s Schema (T)”, *The Journal of Philosophical Logic*, 21(3): 235–241.

[^montague-1963]: Montague, R., 1963, “Syntactical treatment of modality, with corollaries on reflection principles and finite axiomatizability”, *Acta Philosophica Fennica*, 16: 153–167.

[^morreau-1998]: Morreau, Michael and Sarit Kraus, 1998, “Syntactical treatments of propositional attitudes”, *Artificial Intelligence*, 106(1): 161–177.

[^murzi-2015]: Murzi, Julien, and Massimiliano Carrara, 2015, “Paradox and logical revision. A short introduction”, *Topoi* 34(1): 7–14.

[^odintsov-2015]: Odintsov, Sergei P. and Heinrich Wansing, 2015, “The logic of generalized truth values and the logic of bilattices.” *Studia Logica*, 103(1): 91–112.

[^pacuit-2007]: Pacuit, Eric, 2007, “Understanding the Brandenburger-Keisler paradox”, *Studia Logica*, 86(3): 435–454.

[^pelling-2011]: Pelling, Charlie, 2011, “A self-referential paradox for the truth account of assertion”, *Analysis*, 71(4): 688–688.

[^perlis-1994]: Perlis, D. and V. S. Subrahmanian, 1994, “Meta-languages, Reflection Principles and Self-Reference”, *Handbook of Logic in Artificial Intelligence and Logic Programming*, 2: 323–358.

[^picollo-2013]: Picollo, Lavinia, 2013, “Yablo’s paradox in second-order languages: Consistency and unsatisfiability”, *Studia Logica*, 101(3): 601–617.

[^picollo-2018]: –––, 2018, “Reference in arithmetic”. *The Review of Symbolic Logic*, 11(3): 573–603.

[^picollo-2020]: –––, 2020, “Alethic reference”. *Journal of Philosophical Logic*, 49(3): 417–438.

[^priest-2010a]: Priest, Graham, 2010a, “Badici on inclosures and the liar paradox”, *Australasian Journal of Philosophy*, 88(2): 359–366.

[^priest-2010b]: –––, 2010b, “Inclosures, vagueness, and self-reference”, *Notre Dame Journal of Formal Logic*, 51(1): 69–84.

[^priest-2013]: –––, 2013, “Vague Inclosures”, in *Paraconsistency: Logic and Applications*, Netherlands: Springer.

[^priest-1987]: –––, 1987, *In Contradiction—A Study of the Transconsistent*, Dordrecht: Martinus Nijhoff Publishers.

[^priest-1994]: –––, 1994, “The Structure of the Paradoxes of Self-Reference”, *Mind*, 103: 25–34.

[^priest-1995]: –––, 1995, *Beyond the Limits of Thought*, Cambridge: Cambridge University Press.

[^priest-1997]: –––, 1997, “Yablo’s paradox”, *Analysis* 57(4): 236–242.

[^quine-1937]: Quine, W.V., 1937, “New foundations for mathematical logic”, *American Mathematical Monthly*, 44: 70–80.

[^quine-1976]: –––, 1976, *The Ways of Paradox and Other Essays*, Cambridge, Massachusetts: Harvard University Press.

[^rabern-2013]: Rabern, Landon, and Brian Rabern and Matthew Macauley, 2013, “Dangerous reference graphs and semantic paradoxes”, *Journal of Philosophical Logic* 42(5): 727–765.

[^revières-1988]: de Revières, J., and H.J. Levesque, 1988, “The consistency of syntactical treatments of knowledge”, *Computational Intelligence*, 4: 31–41.

[^rosado-2001]: Rosado Haddock, G. E., 2001, “Recent truth theories: A case study”, *Axiomathes*, 12(1): 87–115.

[^russell-1905]: Russell, B., 1905, “On some difficulties in the theory of transfinite numbers and order types”, *Proceedings of the London Mathematical Society*, 4: 29–53.

[^schindler-2017]: Schindler, Thomas, 2017, “Some Notes on Truths and Comprehension”, *Journal of Philosophical Logic* 1–31.

[^schlenker-2010]: Schlenker, Philippe, 2010, “Super liars”, *The Review of Symbolic Logic*, 1(1): 1–41.

[^shapiro-2015]: Shapiro, Lionel, 2015, “Naive Structure, Contraction and Paradox”, *Topoi*, 34(1): 75–87.

[^sheard-1994]: Sheard, M., 1994, “A guide to truth predicates in the modern era”, *The Journal of Symbolic Logic*, 59(3): 1032–1054.

[^simmons-1993]: Simmons, K., 1993, *Universality and the Liar—An Essay on Truth and the Diagonal Argument*, Cambridge: Cambridge University Press.

[^slater-2002]: Slater, Hartley, 2002, “The Fallacy in Russell’s Schema”, *Russell: the Journal of Bertrand Russell Studies*, 22(2): 4.

[^slater-2010]: –––, 2010, “What Priest (amongst many others) has been missing”, *Ratio*, 23(2): 184–198.

[^smullyan-1992]: Smullyan, R. M., 1992, *Gödel’s Incompleteness Theorems*, Oxford: Oxford University Press.

[^smullyan-1994]: –––, 1994, *Diagonalization and self-reference*, Oxford: Oxford University Press.

[^smullyan-2006]: –––, 2006, “Self-Reference in All Its Glory!”, in Bolander, Hendricks, Pedersen (eds.), *Self-reference*, Stanford: CSLI Publications.

[^snapper-2012]: Snapper, Jeff, 2012, “The liar paradox in new clothes”, *Analysis*, 72(2): 319–322.

[^sorensen-2003]: Sorensen, Roy A., 2003, *A Brief History of the Paradox: Philosophy and the Labyrinths of the Mind*. New York: Oxford University Press.

[^tarski-1935]: Tarski, A., 1935, “Der Wahrheitsbegriff in den formalisierten Sprachen”, *Studia Philosophica*, 1: 261–405.

[^tarski-1968]: –––, 1968, *Undecidable Theories*, Amsterdam: North-Holland Publishing Co.

[^thomason-1980]: Thomason, R., 1980, “A note of syntactical treatments of modality”, *Synthese*, 44: 391–395.

[^tourville-nd]: Tourville, Nicholas, and Roy T. Cook, “Embracing the Technicalities: Expressive Completeness and Revenge”, *The Review of Symbolic Logic*, 9(2): 325–358.

[^turing-1936]: Turing, A.M., 1936, “On Computable Numbers, With an Application to the Entscheidungsproblem”, *Proceedings of the London Mathematical Society*, 42(2): 230–265; correction *ibid*., 43: 544–546 (1937).

[^tucker-2011]: Tucker, Dustin and Richmond H. Thomason, 2011, “Paradoxes of intensionality”, *The Review of Symbolic Logic*, 4(03): 394–411.

[^urbaniak-2009]: Urbaniak, Rafał, 2009, “Leitgeb, ‘about,’ Yablo”, *Logique & Analyse*, 207: 239–254.

[^visser-1989]: Visser, A., 1989, “Semantics and the liar paradox”, *Handbook of Philosophical Logic* (Vol. IV), Dordrecht: Kluwer, pp. 617–706.

[^visser-2019]: –––, 2019, “From Tarski to Gödel – or how to derive the second incompleteness theorem from the undefinability of truth without self-reference”, *Journal of Logic and Computation*, 29(5): 595–604.

[^walicki-2009]: Walicki, Michał, 2009, “Reference, paradoxes and truth”, *Synthese*, 171(1): 195–226.

[^walicki-2019]: –––, 2019, “Kernels of digraphs with finitely many ends”, *Discrete Mathematics* 342: 473–486.

[^weber-2010a]: Weber, Zach, 2010a, “Explanation and solution in the inclosure argument”, *Australasian Journal of Philosophy*, 88(2): 353–357.

[^weber-2010b]: –––, 2010b, “A Paraconsistent Model of Vagueness”, *Mind* 119: 1026–1045.

[^weber-2014]: Weber, Zach, et al., 2014, “Tolerating gluts”, *Mind* 123(491): 813–828.

[^wintein-2012]: Wintein, Stefan, 2012, “Assertoric semantics and the computational power of self-referential truth”, *Journal of philosophical logic*, 41(2): 317–345.

[^yablo-1985]: Yablo, Stephen, 1985, “Truth and reflection”, *Journal of Philosophical Logic*, 14(3): 297–349.

[^yablo-1993]: –––, 1993, “Paradox without self-reference”, *Analysis*, 53: 251–252.

[^yablo-2006]: –––, 2006, “Circularity and Paradox”, in Bolander, Hendricks, Pedersen (eds.), *Self-reference*, Stanford: CSLI Publications.

[^zardini-2011]: Zardini, Elia, 2011, “Truth without contra(di)ction”, *Review of Symbolic Logic*, 4(4): 498–535.

[^zardini-2021]: –––, 2021, “Substructural approaches to paradox: an introduction to the special issue”, *Synthese*, 199(3): 493–525.

[^zhong-2012]: Zhong, Haixia, 2012, “Definability and the structure of logical paradoxes”, *Australasian Journal of Philosophy*, 90(4): 779–788.

[^zwicker-1987]: Zwicker, W.S., 1987, “Playing Games with Games: The Hypergame Paradox,” *The American Mathematical Monthly*, 94(6): 507–514.
