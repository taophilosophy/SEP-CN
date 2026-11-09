# Curry’s Paradox
**First published Wed Sep 6, 2017; substantive revision Sat Jun 20, 2026**

*Shapiro, Lionel, Beall, Jc*

“Curry’s paradox”, as the term is used by philosophers today, refers to a wide variety of paradoxes of self-reference or circularity that trace their modern ancestry to Curry (1942b) and Löb (1955).[^note-1] The common characteristic of these so-called Curry paradoxes is the way they exploit a notion of implication, entailment, or consequence, either in the form of a connective or in the form of a predicate. Curry’s paradox arises in a number of different domains. Like Russell’s paradox, it can take the form of a paradox of set theory or the theory of properties. But it can also take the form of a semantic paradox, closely akin to the Liar paradox. Curry’s paradox differs from both Russell’s paradox and the Liar paradox in that it doesn’t essentially involve the notion of negation. Common truth-theoretic versions involve a sentence that says of itself that if it is true then an arbitrarily chosen claim is true, or—to use a more sinister instance—says of itself that if it is true then every falsity is true. The paradox is that the existence of such a sentence appears to imply the truth of the arbitrarily chosen claim, or—in the more sinister instance—of every falsity. In this entry, we show how the various Curry paradoxes can be constructed, examine the space of available solutions, and explain some ways Curry’s paradox is significant and poses distinctive challenges.

## 1. Introduction: Two Guises of the Paradox

### 1.1 An Informal Argument

Suppose that your friend tells you: “If what I’m saying using this very sentence is true, then time is infinite”. It turns out that there is a short and seemingly compelling argument for the following conclusion:

**(P)**

The mere existence of your friend’s assertion has as a consequence that time is infinite.

Many hold that (P) is beyond belief (and, in that sense, paradoxical), even if time is indeed infinite. Or, if that isn’t bad enough, consider another version, this time involving a claim known to be false. Let your friend say instead: “If what I’m saying using this very sentence is true, then all numbers are prime”. Now, *mutatis mutandis*, the same short and seemingly compelling argument yields (Q):

**(Q)**

The mere existence of your friend’s assertion has as a consequence that all numbers are prime.

Here is the argument for (P). Let $k$ be the self-referential sentence your friend uttered, simplified somewhat, so that it reads “If $k$ is true then time is infinite”.

Suppose now

**(1)**

$k$ is true.

In view of what $k$ says, this means

**(2)**

If $k$ is true then time is infinite.

Reasoning under our supposition, we can use *modus ponens* to derive the consequent of that conditional:

**(3)**

Time is infinite.

The rule of conditional proof now entitles us to affirm a conditional with our supposition as antecedent:

**(4)**

If $k$ is true then time is infinite.

But, since (4) just is $k$ itself, we thus have

**(5)**

$k$ is true.

Finally, putting (4) and (5) together by *modus ponens*, we get

**(6)**

Time is infinite.

We seem to have established that time is infinite relying only on the existence of the self-referential sentence $k$, along with propositional logic and the seemingly obvious principles about truth that took us from (1) to (2) and from (4) to (5). And the same goes for (Q), since we could have used the same form of argument to reach the false conclusion that all numbers are prime.

### 1.2 A Constraint on Theories

One challenge posed by Curry’s paradox is to pinpoint what goes wrong in the foregoing informal argument for (P), (Q) or the like. But starting with Curry’s initial presentation in Curry 1942b (see the supplementary document on [Curry on Curry’s Paradox](curry-paradox.supplement.md)), discussion of Curry’s paradox has usually had a different focus. It has concerned various formal systems—most often set theories or theories of truth. In this setting what poses the paradox is a proof that the system has a particular feature. Typically, the feature at issue is *triviality*. A theory is said to be trivial, or *absolutely inconsistent*, when it affirms every claim that is expressible in the language of the theory.[^note-2]

An argument establishing that a particular formal theory is trivial will pose a problem if either of the following is the case: (i) we wish to use the formal theory in our inquiries, as we use set theory when doing mathematics, or (ii) we wish to use the formal theory in order to model features of language or thought, in particular the claims to which some speakers or thinkers are committed. Either way, the target theory’s triviality would show that it is inadequate for its intended purpose. So this is a second challenge posed by Curry’s paradox.

To spell out the sense in which Curry’s paradox constrains theories we need to say what a *Curry sentence* is. Informally, a Curry sentence is a sentence that is equivalent, by the lights of some theory, to a conditional *with itself as antecedent*. For example, one might think of the argument of section 1.1 as appealing to an informal theory of truth. Then the sentence “$k$ is true” serves as a Curry sentence for that theory. That is because, given what our informal theory tells us about what $k$’s truth involves, “$k$ is true” should be equivalent to “If $k$ is true, then time is infinite” (since this conditional is $k$ itself).

In what follows, the notation $\vdash_{\mathcal{T}} \alpha$ is used to say that theory $\mathcal{T}$ contains sentence $\alpha$, and $\Gamma \vdash_{\mathcal{T}} \alpha$ is used to say that $\alpha$ follows from the assumptions collected in $\Gamma$ according to $\mathcal{T}$ (i.e., according to $\mathcal{T}$’s consequence relation $\vdash_{\mathcal{T}}$).[^note-3] For the most part, however, we will be concerned only with claims about what follows according to the theory from a single assumption, i.e., claims expressed by sentences of form $\gamma \vdash_{\mathcal{T}} \alpha$. (We rely on context to make clear where such a sentence is being used and where it is being mentioned.) Consequences from multiple assumptions will only be considered in section 4.2.1, which discusses proposals to resolve Curry’s paradox by restricting the rule of “structural contraction”.

Two sentences (in the language of theory $\mathcal{T}$) will be called *intersubstitutable* according to $\mathcal{T}$ provided the truth of any claim of the form $\Gamma \vdash_{\mathcal{T}} \alpha$ is unaffected by substitutions of one for the other within $\alpha$ or within any of the sentences in $\Gamma$. Finally, we assume that the language contains a connective ${\rightarrow}$ that serves, in some suitable sense, as a conditional. For purposes of the following definition, we don’t place any specific requirements on the behavior of this conditional. We can now define the notion of a *Curry sentence for a sentence-theory pair*.

**Definition 1** (Curry sentence) Let $\pi$ be a sentence of the language of $\mathcal{T}$. A Curry sentence for $\pi$ and $\mathcal{T}$ is any sentence $\kappa$ such that $\kappa$ and $\kappa {\rightarrow}\pi$ are intersubstitutable according to $\mathcal{T}$.[^note-4]

The various versions of Curry’s paradox arise from the existence of arguments in favor of the following very general claim. (These arguments, which rest on assumptions about the conditional ${\rightarrow}$, will be discussed in detail in section 3.)

**Troubling Claim** For every theory $\mathcal{T}$, and any sentence $\pi$ in the language of $\mathcal{T}$, if there is a Curry sentence for $\pi$ and $\mathcal{T}$, then $\vdash_{\mathcal{T}} \pi$.

An argument that appears to establish the Troubling Claim will count as paradoxical provided there is also compelling reason to believe that this claim is false. A counterexample to the Troubling Claim would be any theory $\mathcal{T}$ and sentence $\pi$ such that there is a Curry sentence for $\pi$ and $\mathcal{T}$ but it is not the case that $\vdash_{\mathcal{T}} \pi$.

As noted above, Curry’s paradox is often understood as a challenge to the existence of nontrivial theories. Given the Troubling Claim, a theory will be trivial whenever a Curry sentence can be formulated for *any* sentence in the language of the theory. Indeed, triviality follows from a weaker condition, which the following definition makes explicit.

**Definition 2** (Curry-complete theory) A theory $\mathcal{T}$ is Curry-complete provided that for every sentence $\pi$ in the language of $\mathcal{T}$, there is some $\pi'$ such that (i) there is a Curry sentence for $\pi'$ and $\mathcal{T}$ and (ii) if $\vdash_{\mathcal{T}} \pi'$ then $\vdash_{\mathcal{T}} \pi$.

One instance of $\pi'$ satisfying the condition (ii) would be $\pi$ itself. Another instance would be an “explosive” sentence $\bot$ that is contained in a theory only if *every* sentence is contained in the theory.[^note-5]

The Troubling Claim now has an immediate consequence: a Curry-complete theory must contain every sentence in its language.

**Troubling Corollary** Every Curry-complete theory is trivial.

Again, any argument that appears to establish the Troubling Corollary will count as paradoxical provided that there is compelling reason to believe that there are nontrivial theories (indeed true theories) that are Curry-complete.

### 1.3 Overview

For the remainder of this entry, Curry’s paradox will be understood as imposing a paradoxical constraint on theories, namely the one stated by the above Troubling Corollary. Presenting a version of Curry’s paradox, understood this way, involves doing two things:

- arguing that $\mathcal{T}$ is Curry-complete, for some apparently nontrivial target theory $\mathcal{T}$, and
- giving an argument for the Troubling Claim.[^note-6]

Sections 2 and 3 discuss these two tasks in that order.

For now, the basic idea can be conveyed using the example of the self-referential sentence $k$ that reads “If $k$ is true then time is infinite”. First, given our understanding of truth, we recognize that the sentence “$k$ is true” is intersubstitutable with “If $k$ is true, then time is infinite”. Second, the informal argument of section 1.1 derives a paradoxical conclusion from this equivalence. Readers chiefly interested in the logical principles involved in that argument and related ones, and the options for resisting such arguments, may wish to turn to section 3.

## 2. Constructing Curry Sentences

As it is standardly presented today, Curry’s paradox afflicts “naive” truth theories (those featuring a “transparent” truth predicate) and “naive” set theories (those featuring unrestricted set abstraction). This section will explain how each kind of theory can give rise to Curry sentences. We start, however, with a version that concerns theories of properties, a version that more closely resembles Curry’s formulation. (The supplementary document [Curry on Curry’s Paradox](curry-paradox.supplement.md) briefly characterizes the targets of Curry’s own versions of the paradox.)

A theory of properties features *unrestricted property abstraction* provided that for any condition statable in the language of the theory, there exists a property that (according to the theory) is exemplified by precisely the things that meet this condition. Consider a theory $\mathcal{T_P}$ formulated in a language with a property abstraction device $[x: \phi x]$ and an exemplification relation $\epsilon$. For example, if $\phi(t)$ says that the object which the term $t$ stands for is triangular, $t \ \epsilon \ [x: \phi x]$ says that this object exemplifies the property of triangularity. Then, given unrestricted property abstraction, we should have the following principle.

**(Property)** For every open sentence $\phi$ with one free variable, and every term $t$, the sentences $t \ \epsilon \ [x: \phi x]$ and $\phi t$ are intersubstitutable according to $\mathcal{T_P}$.

In effect, Curry (1942b) sketches two “methods of constructing” Curry sentences using his counterpart of (Property). He says that the first is “based on the Russell paradox”, while the second is “based on the Epimenides paradox”. Although both methods are property-theoretic, the first method yields a precursor of set-theoretic versions of Curry’s paradox, while the second yields a precursor of truth-theoretic versions.

### 2.1 Curry’s First Method, and Set-Theoretic Curry Sentences

The version of Russell’s paradox which Curry’s first method resembles is the one that concerns property exemplification. Its topic is the property of being such that *one fails to exemplify oneself*. We obtain a property-theoretic Curry sentence by considering instead the property of being such that *one exemplifies oneself only if time is infinite.* Say that we introduce the name $h$ for that property, by stipulating $h =_{def} [x: x \ \epsilon \ x {\rightarrow}\pi]$, where the sentence $\pi$ says that time is infinite.[^note-7] Applying the principle (Property) to the sentence $h \ \epsilon \ h$, we find:

$h \ \epsilon \ h$ and $h \ \epsilon \ h {\rightarrow}\pi$ are intersubstitutable according to $\mathcal{T_P}$.

In other words, $h \ \epsilon \ h$ is a Curry sentence for $\pi$ and $\mathcal{T_P}$.

Curry’s first method subsequently gave rise to set-theoretic Curry sentences. A theory of sets features *unrestricted set abstraction* provided that for any condition statable in the language of the theory, there exists a set that (according to the theory) contains all and only the things that meet this condition. Let $\mathcal{T_S}$ be our theory of sets, formulated in a language that expresses set abstraction using $\{ x: \phi x\}$ and set membership using $\in$. Then the counterpart of (Property) is

**(Set)** For every open sentence $\phi$ with one free variable, and every term $t$, the sentences $t \in \{ x: \phi x\}$ and $\phi t$ are intersubstitutable according to $\mathcal{T_S}$.

To obtain a set-theoretic Curry sentence, consider the set consisting of anything that is a member of itself only if time is infinite. Say that we introduce the name $c$ for that set, by stipulating $c =_{def} \{ x: x \in x {\rightarrow}\pi \}$. Applying the principle (Set) to the sentence $c \in c$, we find:

$c \in c$ and $c \in c {\rightarrow}\pi$ are intersubstitutable according to $\mathcal{T_S}$.

In other words, $c \in c$ is a Curry sentence for $\pi$ and $\mathcal{T_S}$.

The set-theoretic version of Curry’s paradox was introduced in Fitch 1952[^note-8] and is also presented in Moh 1954 and Prior 1955.

### 2.2 Curry’s Second Method, and Truth-Theoretic Curry Sentences

Despite his remark about the “Epimenides paradox”, a form of the Liar paradox, Curry’s second method is a variant of a related semantic paradox, Grelling’s paradox.[^note-9] In its original form, Grelling’s paradox considers a property possessed by many words, namely the property a word has when it *fails to exemplify the property it stands for* (Grelling & Nelson 1908)[^grelling-1908]. For example, the word “offensiveness” has that property: it fails to exemplify the property it stands for, since it isn’t offensive (see entry on paradoxes and contemporary logic). In effect, Curry considers instead the property a word has provided it *exemplifies the property it stands for only if time is infinite*. Now suppose that our theory introduces a name $u$ for this property. Curry then shows how to construct a sentence that (speaking informally) says that the name $u$ exemplifies the property it stands for. He shows that this sentence will serve as a Curry sentence for a theory of properties and the denotation of names.[^note-10]

Though this method of obtaining a Curry sentence is based on a *semantic feature of expressions*, it still relies on property abstraction. Nonetheless, it can be viewed as a precursor to a wholly semantic version. (Rather than consider the above-introduced *property*, one could consider the *predicate* “applies to itself only if time is infinite”.) Accordingly, as Geach (1955) and Löb (1955) were the first to show, Curry sentences can be obtained using semantic principles alone, without any reliance on property abstraction. Their route corresponds to the informal argument, in section 1.1, involving the self-referential sentence $k$ that reads “If $k$ is true then time is infinite”.

For this purpose, let $\mathcal{T_T}$ be a theory of truth, where $T$ is the truth predicate. Assume the “transparency” principle

**(Truth)** For every sentence $\alpha$, the sentences $T\langle \alpha \rangle$ and $\alpha$ are intersubstitutable according to $\mathcal{T_T}$.

To obtain a Curry sentence using this principle, assume there is a sentence $\xi$ that is $T\langle \xi \rangle {\rightarrow}\pi$.[^note-11] Then it follows immediately from (Truth) that

$T\langle \xi \rangle$ and $T\langle \xi \rangle {\rightarrow}\pi$ are intersubstitutable according to $\mathcal{T_T}$.

In other words, $T\langle \xi \rangle$ is a Curry sentence for $\pi$ and $\mathcal{T_T}$.

Geach notes that the semantic paradox that results from a sentence like $T\langle \xi \rangle$ resembles “the Curry paradox in set theory”. Löb, who doesn’t mention Curry’s work, credits the paradox to a referee’s observation about the proof of what is now known as Löb’s theorem concerning provability (see entry on Gödel’s incompleteness theorems). The referee, now known to have been Leon Henkin (Halbach & Visser 2014: 257)[^halbach-2014], suggested that the method Löb used in his proof “leads to a new derivation of paradoxes in natural language”, namely the informal argument of section 1.1 above.[^note-12]

## 3. Deriving the Paradox

Suppose that we have used one of the above methods to show, for some theory of truth, sets, or properties, that the theory is Curry-complete (in virtue, say, of containing a Curry sentence for each sentence of the language, or for an explosive sentence). To conclude that the theory in question is trivial, it now suffices to give an argument for the Troubling Claim. This is the claim that for every theory $\mathcal{T}$, if there is a Curry sentence for $\pi$ and $\mathcal{T}$, then $\vdash_{\mathcal{T}} \pi$. Such an argument will make use of assumptions about the logical behavior of the conditional ${\rightarrow}$ mentioned in Definition 1. Assuming the Troubling Claim must be resisted, this accordingly places constraints on the behavior of this conditional.

### 3.1 The Curry-Paradox Lemma

To start, here is a very general limitative result, a close variant of the Lemma in Curry 1942b.[^note-13]

**Curry-Paradox Lemma** Suppose that theory $\mathcal{T}$ and sentence $\pi$ are such that (i) there is a Curry sentence for $\pi$ and $\mathcal{T}$, i.e. a $\kappa$ such that $\kappa$ and $\kappa {\rightarrow}\pi$ are $\mathcal{T}$-intersubstitutable, (ii) all instances of the identity rule (Id) $\alpha \vdash_{\mathcal{T}} \alpha$ hold, and (iii) the conditional ${\rightarrow}$ satisfies both of the following principles:

$$\tag{MP} \textrm{If } \vdash_{\mathcal{T}} \alpha {\rightarrow}\beta \textrm{ and }\vdash_{\mathcal{T}} \alpha \textrm{ then } \vdash_{\mathcal{T}} \beta $$ $$\tag{Cont} \textrm{If } \alpha \vdash_{\mathcal{T}} \alpha {\rightarrow}\beta \textrm{ then } \vdash_{\mathcal{T}} \alpha {\rightarrow}\beta $$

Then $\vdash_{\mathcal{T}} \pi$.

Here MP is a version of *modus ponens*, and Cont is a principle of *contraction*: two occurrences of the sentence $\alpha$ are “contracted” into one. (We will soon encounter related principles that are more commonly referred to as contraction.[^note-14]) The Curry-Paradox Lemma entails that any Curry-complete theory must violate one or more of Id, MP or Cont on pain of triviality.

To prove the Lemma one shows that Id, MP and Cont, together with the “Curry-intersubstitutivity” of $\kappa$ with $\kappa {\rightarrow}\pi$, suffice to establish $\vdash_{\mathcal{T}} \pi$. The following derivation resembles the informal argument of section 1.1. That argument also included a subargument for the principle Cont, which will be examined below.

$$ \begin{array}{rll} 1 & \kappa \vdash_{\mathcal{T}} \kappa & \textrm{Id}\\ 2 & \kappa \vdash_{\mathcal{T}} \kappa {\rightarrow}\pi & \textrm{1 Curry-intersubstitutivity}\\ 3 & \vdash_{\mathcal{T}} \kappa {\rightarrow}\pi & \textrm{2 Cont}\\ 4 & \vdash_{\mathcal{T}} \kappa & \textrm{3 Curry-intersubstitutivity}\\ 5 & \vdash_{\mathcal{T}} \pi & \textrm{3, 4 MP} \end{array} $$

Section 4 will discuss ways one might justify, and ways one might reject, each of the two principles concerning ${\rightarrow}$ assumed in the Curry-Paradox Lemma, namely MP and Cont.

### 3.2 Alternative Premises

There are counterparts of the Curry-Paradox Lemma that invoke alternative sets of logical principles (see, e.g., Rogerson & Restall 2004 and Bimbó 2006)[^bimbó-2006][^rogerson-2004]. Probably the most common version replaces the *rules* Id and Cont with corresponding *laws*:

$$\tag{IdL} \vdash_{\mathcal{T}} \alpha {\rightarrow}\alpha $$ $$ \tag{ContL} \vdash_{\mathcal{T}} (\alpha {\rightarrow}(\alpha {\rightarrow}\beta)) {\rightarrow}(\alpha {\rightarrow}\beta) $$

The derivation now goes as follows:

$$ \begin{array}{rll} 1 & \vdash_{\mathcal{T}} \kappa {\rightarrow}\kappa & \textrm{IdL }\\ 2 & \vdash_{\mathcal{T}} \kappa {\rightarrow}(\kappa {\rightarrow}\pi) & \textrm{1 Curry-intersubstitutivity }\\ 3 & \vdash_{\mathcal{T}} (\kappa {\rightarrow}(\kappa {\rightarrow}\pi)) {\rightarrow}(\kappa {\rightarrow}\pi) & \textrm{2 ContL }\\ 4 & \vdash_{\mathcal{T}} \kappa {\rightarrow}\pi & \textrm{2, 3 MP }\\ 5 & \vdash_{\mathcal{T}} \kappa & \textrm{4 Curry-intersubstitutivity }\\ 6 & \vdash_{\mathcal{T}} \pi & \textrm{4, 5 MP }\\ \end{array} $$

A second common counterpart of the Curry-Paradox Lemma is due to Meyer, Routley, and Dunn (1979).[^note-15] It uses two principles concerning conjunction: the law form of *modus ponens* and the idempotency of conjunction.

$$\tag{MPL} \vdash_{\mathcal{T}} ((\alpha {\rightarrow}\beta) \wedge \alpha) {\rightarrow}\beta $$

**(Idem$_{\wedge}$)**

The sentences $\alpha$ and $\alpha \wedge \alpha$ are intersubstitutable according to $T$

This time the derivation goes as follows:

$$ \begin{array}{rll} 1 & \vdash_{\mathcal{T}} ((\kappa {\rightarrow}\pi) \wedge \kappa) {\rightarrow}\pi & \textrm{MPL }\\ 2 & \vdash_{\mathcal{T}} (\kappa \wedge \kappa) {\rightarrow}\pi & \textrm{1 Curry-intersubstitutivity }\\ 3 & \vdash_{\mathcal{T}} \kappa {\rightarrow}\pi & \textrm{2 Idem}_{\wedge}\\ 4 & \vdash_{\mathcal{T}} \kappa & \textrm{4 Curry-intersubstitutivity }\\ 5 & \vdash_{\mathcal{T}} \pi & \textrm{3, 4 MP }\\ \end{array} $$

Formulating the Curry-Paradox Lemma using Cont, rather than ContL or MPL, will make it easier to call attention (in section 4.2) to significant differences within the class of responses that reject both of the latter principles.[^note-16]

### 3.3 Strengthening the Lemma

One of the conditions in the Curry-Paradox Lemma was that there is a Curry sentence for $\pi$ and $\mathcal{T}$, i.e. a $\kappa$ such that $\kappa$ and $\kappa {\rightarrow}\pi$ are $\mathcal{T}$-intersubstitutable. In fact, this requirement of intersubstitutivity is not necessary. It suffices that there be a sentence $\kappa$ that meets the following weaker pair of conditions: (i.a) $\kappa \vdash_{\mathcal{T}} \kappa {\rightarrow}\pi$ and (i.b) if $\vdash_{\mathcal{T}} \kappa {\rightarrow}\pi$ then $\vdash_{\mathcal{T}} \kappa$.

This yields additional ways of deriving paradoxes. For example, suppose that $K\langle \alpha \rangle$ expresses the claim that it is knowable (alternatively, provable in an informal sense) that $\alpha$ is true. Arguably, a theory $\mathcal{T}_{K}$ of knowability (or informal proof) should be such that

$$ K\langle \alpha \rangle\ \vdash_{\mathcal{T}_{K}} \alpha $$ $$ \textrm{If } \vdash_{\mathcal{T}_{K}} \alpha \textrm{ then }\vdash_{\mathcal{T}_{K}} K\langle \alpha \rangle\ $$

Now let $\gamma$ be the sentence $K\langle \gamma \rangle\ {\rightarrow}\pi$. Then the sentence $K\langle \gamma \rangle$ will satisfy conditions (i.a) and (i.b) for the theory $\mathcal{T}_{K}$, thus yielding $\vdash_{\mathcal{T}_{K}} \pi$. This is a version of the paradox of the Knower (see e.g., Priest 2006: 237–238 or Murzi & Rossi 2021; the paradox is due to Kaplan & Montague 1960 and Myhill 1960)[^kaplan-1960][^murzi-2021][^myhill-1960][^priest-2006][^priest-2021].

## 4. Responses to Curry’s Paradox

Responses to Curry’s paradox can be divided into two classes, based on whether they accept the Troubling Corollary that all Curry-complete theories are trivial.

- *Topic-specific responses* accept the Troubling Corollary. However, they deny that the target theories of properties, sets or truth are Curry-complete. Topic-specific responses can, and usually do, embrace classical logic.
- *Logical responses* reject the Troubling Corollary; they insist that there can be nontrivial Curry-complete theories. Any such theory must violate one or more of the logical principles assumed in the Curry-Paradox Lemma. Since classical logic validates those principles, these responses invoke a non-classical logic.

There is also the option of advocating a topic-specific response to Curry paradoxes arising in one domain, say set theory, while advocating a logical response to Curry paradoxes arising in another domain, say property theory (e.g., Field 2008, Beall 2009)[^beall-2009][^field-2008].

### 4.1 Topic-Specific Responses

Examples of prominent theories of truth that supply topic-specific responses to Curry’s paradox include Tarski’s hierarchical theory, the revision theory of truth (Gupta & Belnap 1993)[^gupta-1993] and the contextualist approaches (Burge 1979, Simmons 1993, and Glanzberg 2001, 2004)[^burge-1979][^glanzberg-2001][^simmons-1993]. These theories all restrict the “naive” transparency principle (Truth). For an overview, see the entry on the Liar paradox. In the context of set theory topic-specific responses include Russellian type theories and various theories that restrict the “naive” set abstraction principle (Set). See the entries on Russell’s paradox and alternative axiomatic set theories.

In general, the considerations relevant to evaluating most topic-specific responses don’t appear to be specific to Curry’s paradox, but pertain equally to the Liar paradox (in the truth-theoretic domain) and Russell’s paradox (in the set- and property-theoretic domains).[^note-17] For that reason the rest of this entry will focus on logical responses, though section 6.3 briefly returns to the distinction in the context of so-called validity Curry paradoxes.

### 4.2 Logical Responses

Logical responses to Curry’s paradox hold that there are theories that are Curry-complete yet nontrivial; such a theory must violate one or more of the logical principles assumed in the Curry-Paradox Lemma. Since the rule Id has generally been left unquestioned (but see French 2016 and Nicolai & Rossi 2018)[^french-2016][^nicolai-2018], this has meant denying that the conditional ${\rightarrow}$ of a nontrivial Curry-complete theory satisfies both MP and Cont. Accordingly, responses have fallen into two categories.

**(I)**

The most common strategy has been to accept that such a theory’s conditional obeys MP, but deny that it obeys Cont. Since Cont is a contraction principle, such responses can be called *contraction-free*. This strategy was first proposed by Moh (1954), who is cited approvingly by Geach (1955) and Prior (1955).

**(II)**

A second and much more recent strategy is to accept that such a theory’s conditional obeys Cont, but deny that it obeys MP (sometimes called the rule of “detachment”). Such responses can be called *detachment-free*. This strategy is advocated, in different ways, by Ripley (2013) and Beall (2015).

Each category of logical responses can in turn be subdivided according to how it blocks purported derivations of Cont and MP.

#### 4.2.1 Contraction-Free Responses

The principle Cont that is rejected by contraction-free responses follows from two standard principles. These are single-assumption conditional proof and a slightly more general version of *modus ponens*, involving at most one assumption $\gamma$:

**(MP′)**

If $\gamma \vdash_{\mathcal{T}} \alpha {\rightarrow}\beta$ and $\gamma \vdash_{\mathcal{T}} \alpha$ then $\gamma \vdash_{\mathcal{T}} \beta$

**(CP)**

If $\alpha \vdash_{\mathcal{T}} \beta$ then $\vdash_{\mathcal{T}} \alpha {\rightarrow}\beta$

$$ \begin{array}{rll} 1 & \alpha \vdash_{\mathcal{T}} \alpha {\rightarrow}\beta & \\ 2 & \alpha \vdash_{\mathcal{T}} \alpha & \textrm{Id }\\ 3 & \alpha \vdash_{\mathcal{T}} \beta & \textrm{1, 2 MP}'\\ 4 & \vdash_{\mathcal{T}} \alpha {\rightarrow}\beta & \textrm{3 CP }\\ \end{array} $$

Contraction-free responses must thus reject one or the other of these two principles for the conditional of a nontrivial Curry-complete theory. Accordingly, two subcategories of theorists in category (I) can be identified:

**(Ia)**

A *strongly contraction-free* response denies that ${\rightarrow}$ obeys MP′ (e.g., Mares & Paoli 2014, Slaney 1990, Weir 2015, Zardini 2011)[^mares-2014][^slaney-1990][^weir-2015][^zardini-2011].

**(Ib)**

A *weakly contraction-free* response accepts that ${\rightarrow}$ obeys MP′, but denies that it obeys CP (e.g., Field 2008, Beall 2009, Nolan 2016)[^beall-2009][^field-2008][^nolan-2016].

The reason why responses in category (Ib) only count as *weakly* contraction-free is that, as steps 1–3 show, they accept the contraction principle according to which if $\alpha \vdash_{\mathcal{T}} \alpha {\rightarrow}\beta$ then $\alpha \vdash_{\mathcal{T}} \beta$.

Proponents of strongly contraction-free responses hold that MP′ doesn’t properly express the relevant form of *modus ponens*. They typically present their own form of that rule in a “substructural” framework, specifically one that lets us distinguish between what follows from an assumption *taken once* and what follows from the same assumption *taken twice*. (See the entry on substructural logics.) Accordingly, MP′ needs to be replaced by

**(MP″)**

If $\gamma \vdash_{\mathcal{T}} \alpha {\rightarrow}\beta$ and $\gamma \vdash_{\mathcal{T}} \alpha$ then $\gamma, \gamma \vdash_{\mathcal{T}} \beta$

and the rule of “structural contraction” needs to be rejected:

**(sCont)**

If $\Gamma, \gamma, \gamma \vdash_{\mathcal{T}} \beta$ then $\Gamma, \gamma \vdash_{\mathcal{T}} \beta$

It is because they reject structural contraction that strongly contraction-free approaches can claim to preserve *modus ponens* despite rejecting MP′ (see Shapiro 2011, Zardini 2013, and Ripley 2015a)[^ripley-2015a][^shapiro-2011][^zardini-2013].

Strongly contraction-free responses also need to block a derivation of MP′ using a pair of principles involving conjunction:

**(MP′$_{\land}$)**

If $\gamma \vdash_{\mathcal{T}} \alpha {\rightarrow}\beta$ and $\delta \vdash_{\mathcal{T}} \alpha$ then $\gamma \wedge \delta \vdash_{\mathcal{T}} \beta$

**(Idem$_{\wedge}$)**

The sentences $\alpha$ and $\alpha \wedge \alpha$ are intersubstitutable according to $T$

$$ \begin{array}{rll} 1 & \gamma \vdash_{\mathcal{T}} \alpha {\rightarrow}\beta & \\ 2 & \gamma \vdash_{\mathcal{T}} \alpha & \\ 3 & \gamma \wedge \gamma \vdash_{\mathcal{T}} \beta & \textrm{1, 2 MP}'_{\wedge}\\ 4 & \gamma \vdash_{\mathcal{T}} \beta & \textrm{3 Idem}_{\wedge}\\ \end{array} $$

Avoiding this derivation of MP′ requires denying that there is a conjunction $\wedge$ that obeys both MP′$_{\wedge}$ and Idem$_{\wedge}$. According to many strongly contraction-free responses (e.g., Mares & Paoli 2014, Zardini 2011)[^mares-2014][^zardini-2011], one kind of conjunction—the “multiplicative” kind, or “fusion”—obeys MP′$_{\wedge}$ but not Idem$_{\wedge}$, whereas another kind—the “additive” kind—obeys Idem$_{\wedge}$ but not MP′$_{\wedge}$ (see the entry on linear logic, and Ripley 2015a)[^ripley-2015a]. If the substructural framework discussed above is used, the failure of MP′$_{\wedge}$ amounts to the fact that for additive conjunction, $\gamma, \delta \vdash_{\mathcal{T}} \beta$ is not equivalent to $\gamma \wedge \delta \vdash_{\mathcal{T}} \beta$.

As for weakly contraction-free responses, the failure of CP has sometimes been motivated using “worlds” semantics of the sort that involve a distinction between logically *possible* and *impossible* worlds (e.g., Beall 2009, Nolan 2016)[^beall-2009][^nolan-2016]. To refute CP we need the truth of $\alpha \vdash_\mathcal{T} \beta$ and the falsity of $\vdash_\mathcal{T} \alpha{\rightarrow}\beta$. On the target “worlds” approaches $\vdash_\mathcal{T}$ is defined as truth preservation over a proper subset of worlds (in a model), namely, the “possible worlds” of the model. Hence, for $\alpha \vdash_\mathcal{T} \beta$ to be true is for there to be no possible world (in any model) at which $\alpha$ is true and $\beta$ untrue. In turn, to refute $\vdash_\mathcal{T}\alpha{\rightarrow}\beta$ we need a possible world at which $\alpha{\rightarrow}\beta$ is untrue. How does that happen? Because connectives are defined in a way that takes account of *all* (types of) worlds in the model (possible and, if there be any, impossible) there’s an option for $\alpha{\rightarrow}\beta$ to be untrue at a possible world in virtue of $\alpha$ being true and $\beta$ being untrue at an *impossible* world. And that’s just what happens on the target approaches. (Exactly how one defines the truth-at-a-world and falsity-at-a-world conditions for the arrow depends on the exact “worlds” approach at issue.)

#### 4.2.2 Detachment-Free Responses

Detachment-free responses must block a straightforward derivation of MP based on a principle of transitivity together with the converse of single-assumption conditional proof:

**(Trans)**

If $\alpha \vdash_{\mathcal{T}} \beta$ and $\vdash_{\mathcal{T}} \alpha$, then $\vdash_{\mathcal{T}} \beta$

**(CCP)**

If $\vdash_{\mathcal{T}} \alpha {\rightarrow}\beta$ then $\alpha \vdash_{\mathcal{T}} \beta$

$$ \begin{array}{rll} 1 & \vdash_{\mathcal{T}} \alpha {\rightarrow}\beta & \\ 2 & \vdash_{\mathcal{T}} \alpha & \\ 3 & \alpha \vdash_{\mathcal{T}} \beta & \textrm{1 CCP }\\ 4 & \vdash_{\mathcal{T}} \beta & \textrm{2, 3 Trans }\\ \end{array} $$

There are two subcategories of theorists in category (II):

**(IIa)**

A *strongly detachment-free* response denies that ${\rightarrow}$ obeys CCP (Goodship 1996, Beall 2015)[^beall-2015][^goodship-1996].

**(IIb)**

A *weakly detachment-free* response accepts that ${\rightarrow}$ obeys CCP, but rejects Trans (Ripley 2013)[^ripley-2013].

The reason why responses in category (IIb) are only *weakly* detachment-free is that CCP, which these responses accept, can be regarded as a kind of detachment principle for the conditional.

One strategy for replying to the charge that detachment-free responses are counterintuitive has been to appeal to a connection between consequence and our acceptance and rejection of sentences. According to this connection, whenever it is the case that $\alpha \vdash_{\mathcal{T}} \beta$, this means (or at least implies) that it is incoherent by the lights of theory $\mathcal{T}$ to accept $\alpha$ while rejecting $\beta$ (see Restall 2005)[^restall-2005]. Now suppose that, by the lights of a theory $\mathcal{T}$, it is incoherent to reject $\alpha$ and it is also incoherent to accept $\alpha$ while rejecting $\beta$. Then, Ripley (2013) argues, there need be nothing incoherent by the theory’s lights about rejecting $\beta$, as long as one doesn’t also accept $\alpha$. There is thus room to give up Trans and adopt a weakly detachment-free response to Curry’s paradox. Beall’s defense of the strongly detachment-free approach rests on related considerations. He argues, in effect, that a principle weaker than CCP can play the relevant role in constraining the combinations of acceptance and rejection of sentences including $\alpha$, $\beta$, and $\alpha {\rightarrow}\beta$.

#### 4.2.3 Application to the Informal Paradoxical Argument

The approaches to Curry’s paradox just distinguished find fault with different inferences and sub-conclusions of the informal paradoxical argument in section 1.1.

- A strongly contraction-free response corresponds to blocking step (3) of that argument. That is because this step’s reasoning takes the form MP′, which contracts two uses of supposition (1) into one.
- A weakly contraction-free response instead blocks step (4), since it rejects CP.
- Even though detachment-free responses don’t accept the informal argument’s reasoning by MP′ leading to (3), they do allow an alternative derivation of (4) by Cont. Hence, since weakly detachment-free responses accept CCP, these also accept that (3) follows from supposition (1).
- However, detachment-free responses find fault with the final move to (6) by MP.

## 5. The Significance of Curry’s Paradox

In this section, we explain some distinctive lessons that can be learned by considering Curry’s paradox. For discussion of the kinds of significance that versions of Curry’s paradox share with related paradoxes, see the entries on Russell’s paradox and the Liar paradox.

### 5.1 Dashing Hopes for Solutions to Negation Paradoxes

Starting with Church (1942), Moh (1954), Geach (1955), Löb (1955) and Prior (1955), discussion of Curry’s paradox has emphasized that it differs from Russell’s paradox, and the Liar paradox, in that it doesn’t “involv[e] negation essentially” (Anderson 1975: 128)[^anderson-1975][^anderson-1975-2][^anderson-1975-3].[^note-18] One reason the negation-free status of Curry’s paradox matters is that it renders the paradox resistant to some resolutions that might be adequate for such “negation paradoxes”.

Geach argues that Curry’s paradox poses a problem for any proponents of naive truth theory or naive set theory who, faced with negation paradoxes,

> might … hope to avoid [these paradoxes] by using a logical system in which ‘$p$ if and only if not-$p$’ were a theorem for some interpretations of ‘$p$’ without our being able to infer thence any arbitrary statement…. (Geach 1955: 71)[^geach-1955]

The problem, he says, is that Curry’s paradox “cannot be resolved merely by adopting a system that contains a queer sort of negation”. Rather, “if we want to retain the naive view of truth, or the naive view of classes …, then we must modify the elementary rules of inference relating to ‘if’” (1955: 72). Geach’s view of the significance of Curry’s paradox is closely echoed by Meyer, Routley, and Dunn (1979: 127). They conclude that Curry’s paradox frustrates those who had “hoped that weakening classical negation principles” would resolve Russell’s paradox.[^note-19]

In short, the point is that there are non-classical logics with weak negation principles that resolve Russell’s paradox and the Liar, yet remain vulnerable to Curry’s paradox. These are logics with the following features:

**(a)**

They can serve as the basis for a nontrivial theory according to which some sentence is intersubstitutable with its own negation.

**(b)**

They can’t serve as the basis for a nontrivial theory that is Curry-complete.

While it is unclear which logics Geach may have had in mind, there are indeed non-classical logics that meet these two conditions. Theories based on these logics accordingly remain vulnerable to Curry’s paradox.

#### 5.1.1 Some Paraconsistent Solutions Frustrated

Meyer, Routley, and Dunn (1979) call attention to one class of logics that meet conditions (a) and (b). They are among the paraconsistent logics, which are logics according to which a sentence together with its negation will not entail any arbitrary sentence. Paraconsistent logics can be used to obtain theories that resolve Russell’s paradox, and the Liar, by embracing negation inconsistency without succumbing to triviality.

According to such a theory $\mathcal{T}$, sentences $\lambda$ and $\lnot\lambda$ can be intersubstitutable, as long as both $\vdash _{\mathcal{T}} \lambda$ and $\vdash _{\mathcal{T}} \lnot \lambda$. Such theories are “glutty”, in the sense that they affirm some sentence together with its negation (see entry on dialetheism). Yet a number of prominent paraconsistent logics can’t serve as the basis for Curry-complete theories on pain of triviality. Such logics are sometimes said to fail to be “Curry paraconsistent” (Slaney 1989)[^slaney-1989].[^note-20]

#### 5.1.2 Some Paracomplete Solutions Frustrated

Many of the non-classical logics that have been proposed to underwrite responses to Russell’s paradox and the Liar paradox are *paracomplete logics*, logics that reject the law of excluded middle. These logics make possible “gappy” theories. In particular, where $\lambda$ and $\lnot\lambda$ are intersubstitutable according to such a theory $\mathcal{T}$, it will fail to be the case that $\vdash _{\mathcal{T}} \lambda \lor \lnot \lambda$. Some of these paracomplete logics likewise meet conditions (a) and (b).

One example is the logic Ł$_{3}$ based on the three-valued truth-tables of Łukasiewicz (see, e.g., Priest 2008)[^priest-2008]. Since it meets condition (a), Ł$_{3}$ offers a possible response to Russell’s paradox and the Liar—in particular, a gappy response. Yet consider the iterated conditional $\alpha {\rightarrow}(\alpha {\rightarrow}\beta)$, which we abbreviate as $\alpha \Rightarrow \beta$. Suppose that a Curry sentence for $\pi$ and an Ł$_{3}$-based theory $\mathcal{T}$ is redefined to be any sentence $\kappa$ intersubstitutable with $\kappa \Rightarrow \pi$. Then $\mathcal{T}$ will meet all the conditions of the Curry-Paradox Lemma, as was first noted by Moh (1954). Hence, as long as there is a $\kappa$ that is intersubstitutable with $\kappa \Rightarrow \pi$ according to $\mathcal{T}$, then $\vdash _{\mathcal{T}} \pi$. Consequently Ł$_{3}$ won’t underwrite a response to Curry’s paradox.[^note-21]

To summarize: Curry’s paradox stands in the way of some otherwise available avenues for resolving paradoxes by means of glutty or gappy theories. As a result, the need to evade Curry’s paradox has played a significant role in the development of non-classical logics (e.g., Priest 2006, Field 2008)[^field-2008][^priest-2006].

### 5.2 Pointing to a General Paradox Structure

The negation-free status of Curry’s paradox matters for a second reason. Prior makes the following important point:

> We can … say not only that Curry’s paradox does not involve negation but that even Russell’s paradox presupposes only those properties of negation which it shares with implication. (Prior 1955: 180)[^prior-1955][^note-22]

What he has in mind is that Russell’s paradox and Curry’s paradox can be understood as resulting from the *same general structure*, which can be instantiated either using negation or using a conditional.[^note-23]

The general structure can be made explicit by defining a type of unary connective that gives rise to Curry’s paradox, and showing how this type is exemplified both by negation and by a unary connective defined in terms of a conditional.[^note-24]

**Definition 3** (Curry connective) Let $\pi$ be a sentence in the language of theory $\mathcal{T}$. The unary connective $\odot$ is a Curry connective for $\pi$ and $\mathcal{T}$ provided it satisfies two principles:

$$\tag{P1} \textrm{If} \vdash_{\mathcal{T}} \alpha \textrm{ and } \vdash_{\mathcal{T}} \odot\alpha \textrm{ then } \vdash_{\mathcal{T}} \pi. $$ $$\tag{P2} \textrm{If } \alpha \vdash_{\mathcal{T}} \odot\alpha \textrm{ then } \vdash_{\mathcal{T}} \odot\alpha. $$

**Generalized Curry-Paradox Lemma** Suppose that $\mathcal{T}$ is such that Id holds and that for some pair of sentences $\pi$ and $\mu$, (i) $\mu$ and $\odot\mu$ are intersubstitutable according to $\mathcal{T}$ and (ii) $\odot$ is a Curry connective for $\pi$ and $\mathcal{T}$. In that case $\vdash_{\mathcal{T}} \pi$.[^note-25]

*Proof*:

$$ \begin{array}{rll} 1 & \mu \vdash_{\mathcal{T}} \mu & \textrm{Id }\\ 2 & \mu \vdash_{\mathcal{T}} \odot\mu & \textrm{1 Curry-intersubstitutivity }\\ 3 & \vdash_{\mathcal{T}} \odot\mu & \textrm{2 P2 }\\ 4 & \vdash_{\mathcal{T}} \mu & \textrm{3 Curry-intersubstitutivity }\\ 5 & \vdash_{\mathcal{T}} \pi & \textrm{3, 4 P1 }\\ \end{array} $$

The Generalized Curry-Paradox Lemma can now be instantiated in two different ways, so as to yield either Curry’s paradox or a negation paradox:

- To obtain Curry’s paradox, let the unary connective $\odot$ be such that $\odot\alpha$ is $\alpha {\rightarrow}\pi$, and let $\mu$ be a sentence intersubstitutable with $\mu {\rightarrow}\pi$ according to $\mathcal{T}$. Then P1 amounts to the instance of MP used in our derivation of the Curry-Paradox Lemma, while P2 is an instance of Cont. $$\tag{MP} \textrm{If }\vdash_{\mathcal{T}} \alpha {\rightarrow}\beta\textrm{ and }\vdash_{\mathcal{T}} \alpha\textrm{ then }\vdash_{\mathcal{T}} \beta $$ $$\tag{Cont} \textrm{If }\alpha \vdash_{\mathcal{T}} \alpha {\rightarrow}\beta\textrm{ then }\vdash_{\mathcal{T}} \alpha {\rightarrow}\beta $$
- To obtain a negation paradox, let $\odot\alpha$ be $\lnot\alpha$, and let $\mu$ be a sentence intersubstitutable with $\lnot\mu$ according to $\mathcal{T}$.[^note-26] Then P1 amounts to an instance of *ex contradictione quodlibet* (or “explosion”), while P2 is an instance of a *reductio* principle. $$\tag{ECQ} \textrm{If }\vdash_{\mathcal{T}} \alpha\textrm{ and }\vdash_{\mathcal{T}} \lnot\alpha\textrm{ then }\vdash_{\mathcal{T}} \beta $$ $$\tag{Red} \textrm{If }\alpha \vdash_{\mathcal{T}} \lnot\alpha\textrm{ then }\vdash_{\mathcal{T}} \lnot\alpha $$

Prior’s point is that the features of negation that are relevant to Russell’s paradox or the Liar paradox are *exhausted by its status as a Curry connective*. This makes clear why these paradoxes do not depend on features of negation, such as excluded middle or double negation elimination, that fail to hold in nonclassical theories where negation remains a Curry connective (e.g., in intuitionistic theories, where ECQ and Red both hold).[^note-27]

Moreover, a Curry connective need not be very negation-like at all. It may fail to be even a *minimal negation* (see entry on negation), since it need not obey the law of double introduction:

$$\tag{DI} \alpha \vdash _{\mathcal{T}} \odot\odot\alpha. $$

For example, suppose that $\odot\alpha$ is $\alpha {\rightarrow}\pi$. Then in order for $\odot$ to obey DI, it would have to be the case that $\alpha \vdash _{\mathcal{T}} (\alpha {\rightarrow}\pi) {\rightarrow}\pi$. That principle is violated by a number of non-classical theories for which $\odot$, when defined this way, *does* qualify as a Curry connective.[^note-28]

To summarize: Curry’s paradox points to a general structure instantiated by a wide range of paradoxes. This structure doesn’t itself involve negation, but it is also displayed by paradoxes that (unlike Curry’s paradox) do essentially involve negation, such as Russell’s paradox and the Liar paradox.

### 5.3 Uniformity of Solution

The issue of which paradoxes display a common structure becomes important in light of the “principle of uniform solution” influentially advocated by Priest (1994). According to this principle, paradoxes that belong to the “same kind” should receive the “same kind of solution”. Suppose that we delimit one kind of paradox as follows:

**Definition 4** (Generalized Curry paradox) We have a generalized Curry paradox in any case where the assumptions stated in the Generalized Curry-Paradox Lemma appear to hold.

Assuming one accepts the principle of uniform solution, the question becomes what counts as proposing a uniform solution to all generalized Curry paradoxes. In particular, does it suffice to show, for every instance of the kind thus delimited, that what appears to be a Curry connective in fact fails to be one? It would seem that this should indeed be enough. It’s unclear why uniformity should additionally require that all seeming Curry connectives fail to qualify as such *in virtue of violating the same condition*. For instance, suppose that negation and our unary connective defined using ${\rightarrow}$ both appear to satisfy the generalized principle P2, in the former case because ${\lnot}$ appears to obey Red and in the latter case because ${\rightarrow}$ appears to obey Cont. Unless these two appearances share a common source (e.g., an implicit reliance on structural contraction, as claimed by Zardini 2011)[^zardini-2011], there need be nothing objectionably non-uniform about taking one appearance at face value while dismissing the other as deceptive. (For discussion of the philosophical issue here, applied to a different class of paradoxes, see the exchange in Smith 2000 and Priest 2000.)[^priest-2000][^smith-2000]

If that is right, the desideratum that generalized Curry paradoxes be resolved uniformly needn’t discriminate between the various logically revisionary solutions that have been pursued. These include the following three options:

- One might hold that it is principle P1 alone that fails when $\odot\alpha$ is instantiated as $\lnot\alpha$ (to get a negation paradox), whereas it is P2 alone that fails when $\odot\alpha$ is instantiated as $\alpha {\rightarrow}\pi$ (to get a Curry paradox). On this approach, ECQ and Cont fail, while Red and MP hold (Priest 1994 & 2006)[^priest-1994][^priest-2006].
- One might hold that P2 alone fails for both instantiations of $\odot$. On this approach, Red and Cont fail, while ECQ and MP hold (Field 2008, Zardini 2011)[^field-2008][^zardini-2011].
- One might hold that P1 alone fails for both instantiations of $\odot$. On this approach, ECQ and MP fail, while Red and Cont hold (Beall 2015, Ripley 2013, Tapia-Navarro & Estrada-González 2020)[^beall-2015][^ripley-2013][^tapia-navarro-2020].

Thus, for example, the approach in Priest (1994 & 2006) would count as resolving Curry’s paradox and the Liar paradox uniformly *qua examples of generalized Curry paradox*. This would be the case despite the fact that Priest evaluates Liar sentences as both true and false, whereas he rejects the claim that Curry sentences are true.[^note-29]

In any event, Curry’s paradox raises challenges in connection with the issue of what type of uniformity should be required of solutions to various paradoxes (Pleitz 2015 and Zardini 2015)[^pleitz-2015][^zardini-2015]. Priest himself calls attention to a kind of paradox narrower than the generalized Curry paradoxes, a kind whose instances include the negation paradoxes but *exclude* Curry’s paradox. This kind is picked out by Priest’s “Inclosure Schema” (2002); see the entry on self-reference. One ongoing dispute is about whether there might be a version of Curry’s paradox that counts as an “inclosure paradox”, and what restrictions either answer imposes in light of the principle of uniform solution (see the exchange in Beall 2014b, Weber et al. 2014, Beall 2014a, and Priest 2017; also Pleitz 2015, Tapia-Navarro & Estrada-González 2020, and Ahmad 2022)[^ahmad-2022][^beall-2014a][^beall-2014b][^pleitz-2015][^priest-2017][^tapia-navarro-2020][^weber-2014][^weber-2014-2].

## 6. Validity Curry

The last two decades (as of the date of this version of this entry) have witnessed a boom in attention to what have been called *validity Curry* or *v-Curry* paradoxes (Whittle 2004, Shapiro 2011, Beall & Murzi 2013)[^beall-2013][^shapiro-2011][^whittle-2004].[^note-30] V-Curry involves Curry sentences that specifically invoke a theory’s consequence or “validity” relation, by using either a conditional or a predicate that purports to express theory $\mathcal{T}$’s relation $\vdash_\mathcal{T}$ in the language of $\mathcal{T}$ itself.

### 6.1 Connective Form

For one form of v-Curry paradox, let the conditional mentioned in the definition of a Curry sentence (Definition 1) be a *consequence connective* ${\Rightarrow}$. A sentence with ${\Rightarrow}$ as its major operator is to be interpreted thus: “That $p$ entails (according to $\mathcal{T}$) that $q$”. We now immediately obtain property-theoretic, set-theoretic or truth-theoretic versions of Curry’s paradox, provided only that ${\Rightarrow}$ meets the conditions MP and Cont of the Curry-Paradox Lemma.

What makes this instance of the Curry-Paradox Lemma particularly troublesome is that it poses an obstacle to one common response to Curry’s paradox, namely the *weakly contraction-free* response (section 4.2.1). That response depended on rejecting the rule CP of single-assumption conditional proof, one direction of the single-assumption “deduction theorem”. But this is a rule that has seemed difficult to resist for a consequence connective (Shapiro 2011, Weber 2014, Zardini 2013)[^shapiro-2011][^weber-2014][^weber-2014-2][^zardini-2013]. If $\beta$ is a consequence of $\alpha$ according to the consequence relation of theory $\mathcal{T}$, where this theory has ${\Rightarrow}$ as its own consequence connective, then $\mathcal{T}$ must surely contain the consequence claim $\alpha {\Rightarrow}\beta$.

Likewise, this variety of Curry paradox poses an obstacle for *detachment-free* responses, which require rejecting the rule MP (section 4.2.2). If a theory with its own consequence connective contains both $\alpha$ and the consequence conditional $\alpha {\Rightarrow}\beta$, then it must surely contain $\beta$ as well. Or so, at least, it has seemed. Admittedly, the proponent of a *weakly* detachment-free response will argue that MP for ${\Rightarrow}$ illicitly builds in transitivity (see section 4.2.2). Still, what seems inescapable is the converse of CP:

**(CCP)**

If $\vdash_{\mathcal{T}} \alpha {\Rightarrow}\beta$ then $\alpha \vdash_{\mathcal{T}} \beta$

If a theory contains the consequence conditional $\alpha {\Rightarrow}\beta$, then surely $\beta$ follows from $\alpha$ according to the theory. That would still rule out a *strongly* detachment-free response, one that rejects not just MP but even CCP.

### 6.2 Predicate Form

A second form of v-Curry paradox arises for a theory $\mathcal{T}_V$ whose subject-matter includes the single-assumption consequence relation $\vdash_{\mathcal{T}_{V}}$ that obtains, according to that very theory, between sentences in its language.[^note-31] Let this relation be expressed by the predicate $Val(x,y)$, and assume further that there is a sentence $\chi$ that is either $Val(\langle\chi\rangle, \langle\pi\rangle)$, or is at least intersubstitutable with the latter according to $\mathcal{T}_V$. To obtain a v-Curry paradox, replace the connective $\alpha{\rightarrow}\beta$ with the metalinguistic predicate $Val(\langle\alpha\rangle, \langle\beta\rangle)$ in Definition 1 of a Curry sentence, as well as in the Curry-Paradox Lemma.

This form of v-Curry paradox is usually presented using analogues of MP′ and CP of section 4.2.1. These are two principles governing $Val$, which we call “validity detachment” and “validity proof” following Beall & Murzi (2013). $$\tag{VD} \textrm{If }\gamma \vdash_{\mathcal{T}_{V}} Val(\langle\alpha\rangle, \langle\beta\rangle)\textrm{ and }\gamma \vdash_{\mathcal{T}_{V}} \alpha\textrm{ then }\gamma \vdash_{\mathcal{T}_{V}} \beta $$ $$\tag{VP} \textrm{If }\alpha \vdash_{\mathcal{T}_{V}} \beta\textrm{ then }\vdash_{\mathcal{T}_{V}} Val(\langle\alpha\rangle, \langle\beta\rangle) $$

Using these principles, we get the following quick argument for $\vdash_{\mathcal{T}_{V}} \pi$. $$ \begin{array}{rll} 1 & \chi \vdash_{\mathcal{T}_{V}} \chi & \text{Id}\\ 2 & \chi \vdash_{\mathcal{T}_{V}} Val(\langle\chi\rangle, \langle\pi\rangle) & \text{1 Assumption about }\chi\\ 3 & \chi \vdash_{\mathcal{T}_{V}} \pi & \text{1, 2 VD}\\ 4 & \vdash_{\mathcal{T}_{V}} Val(\langle\chi\rangle, \langle\pi\rangle) & \text{3 VP}\\ 5 & \vdash_{\mathcal{T}_{V}} \chi & \text{4 Assumption about }\chi\\ 6 & \vdash_{\mathcal{T}_{V}} \pi & \text{4, 5 VD}\\ \end{array} $$

Notice that the role of the principles (VD) and (VP) characterizing the “naive validity” predicate differs from the role of the transparency principle characterizing a “naive truth” predicate in the truth-theoretic form of Curry’s paradox. Whereas the transparency of $T$ is used to obtain a Curry sentence, the principles governing $Val$ are used to derive paradox from the existence of a Curry sentence $\chi$ that is (intersubstitutable with) $Val(\langle\chi\rangle, \langle\pi\rangle)$.

Like the connective form, the *predicate form* of v-Curry poses obstacles to *weakly contraction-free* and *detachment-free* responses. A weakly contraction-free response would resist the “contraction” from step 2 to step 4 by rejecting the rule VP. A detachment-free response would reject VD, even in the zero-assumption form used at step 6. Again, though, both VP and zero-assumption VD have seemed inescapable in view of the intended interpretation of the predicate $Val$ (Beall & Murzi 2013, Murzi 2014, Murzi & Shapiro 2015, Priest 2015, Zardini 2014)[^beall-2013][^murzi-2014][^murzi-2015][^priest-2015][^shapiro-2015][^zardini-2014].[^note-32] Finally, even if VD is rejected as illicitly involving transitivity, what seems inescapable is the converse of VP:

**(CVP)**

If $\vdash_{\mathcal{T}_{V}} Val(\langle\alpha\rangle, \langle\beta\rangle)$ then $\alpha \vdash_{\mathcal{T}_{V}} \beta$

If so, that would at least rule out a *strongly* detachment-free response, one that rejects not just VD but even CVP.

An arguably more powerful version of v-Curry reasoning is presented by Shapiro (2013) and Field (2017: 7). This reasoning can take either connective or predicate form, but it doesn’t depend on CP or VP. Here we give the predicate form using $Val$. As above, we first derive that $\chi \vdash_{\mathcal{T}_{V}} \pi$ using VD. In view of the meaning of $Val$, the conclusion that $\chi \vdash_{\mathcal{T}_{V}} \pi$ shows that $Val(\langle\chi\rangle, \langle\pi\rangle)$ is true, i.e., that $\chi$ is true. But if $\chi$ is true and $\chi \vdash_{\mathcal{T}_{V}} \pi$, then it would seem that, according to the theory $\mathcal{T}_V$, any sentence (including any absurdity) will be the consequence of a true sentence. Yet the appearance that an absurdity follows from true claims is a standard characterization of paradox. Since *weakly* detachment-free (nontransitive) responses to v-Curry do allow the derivation of $\chi \vdash_{\mathcal{T}_{V}} \pi$, this reasoning poses an objection to such responses as well.[^note-33]

### 6.3 Significance

The lively and wide-ranging debate on v-Curry paradoxes has resulted in genuine progress in our understanding of Curry paradoxes. Nonetheless, while v-Curry paradoxes may invite different resolutions from non-v-Curry paradoxes, they typically remain within the same mold as generalized Curry paradoxes. In particular, in the general template of section 5.2 one may take $\odot$ to express (either as a predicate or as a connective) consequence in light of $\vdash_\mathcal{T}$ itself. This is the heart of v-Curry. Inasmuch as there are (many) different (formal) consequence relations definable over our language (e.g., logical consequence in virtue of logical vocabulary, epistemic consequence in virtue of logical-plus-epistemic vocabulary, and so on) there are thereby many different v-Curry paradoxes that may arise. Still, the space of solutions to these paradoxes is the space of solutions to the generalized Curry paradoxes canvassed in this entry.

There remain, however, at least three reasons v-Curry paradoxes merit separate attention. First, as noted above, two categories of logical responses—the weakly contraction-free one that gives up single-assumption conditional proof and the strongly detachment-free one that gives up its converse—have appeared especially problematic in the case of v-Curry paradoxes. If, in fact, v-Curry paradoxes aren’t amenable to these responses, then (assuming the rule Id is retained) the space of logical responses is restricted to *strongly contraction-free* and *weakly detachment-free* responses. The former responses, as explained in section 4.2.1, are typically presented by reformulating *modus ponens* (or detachment for the validity predicate) in a substructural deduction system and rejecting the structural contraction rule sCont. The latter responses, as explained in section 4.2.2, reject the structural principle of transitivity. For this reason, v-Curry paradoxes have sometimes been taken to motivate *substructural* consequence relations (e.g., Barrio et al. 2021, Beall & Murzi 2013, Ripley 2015a, Shapiro 2011 & 2015)[^barrio-2021][^beall-2013][^ripley-2015a][^shapiro-2011][^shapiro-2015].[^note-34]

Second, v-Curry has played an important role in generating the attention recently paid to the topic of the validity of *meta-inferences*: inferences that relate sets of inferences. For one thing, it has been argued that in order for a predicate $Val$ to express validity according to a theory employing that very predicate, the theory must not only “internalize” its own valid inferences (as required by VP and CVP) but must also internalize its valid meta-inferences by yielding sentences that use $Val$ to express the consequence relations that obtain between consequence claims. This requirement is violated by some theories that have been proposed as responses to v-Curry paradox, including weakly detachment-free and strongly contraction-free theories (Barrio et al. 2021, Hlobil 2018 & 2019, Rosenblatt 2017)[^barrio-2021][^hlobil-2018][^hlobil-2019][^rosenblatt-2017]. Rather than require that we can use a predicate $Val$ to capture the theory’s valid meta-inferences, another approach introduces a separate predicate $Val_1$. This approach extends to a hierarchy of validity predicates for meta-meta-inferences, and so on. Porter (2023) shows how to construct a v-Curry paradox involving $Val_1$ that is not resolved by any of the logical responses to v-Curry already mentioned (including substructural ones), and similarly for validity predicates higher in the hierarchy. This is a “revenge” objection to solutions to Curry’s paradox, according to which purported solutions of the paradox end up being plagued by versions of the same paradox. Ensuing discussion has turned, in part, on the question of which solutions count as treating paradoxes at different levels of the hierarchy in a uniform manner (Barrio & Bezerra 2024, Pailos 2025)[^barrio-2024][^pailos-2025].

Third, v-Curry muddies the distinction between topic-specific and logical responses to given instances of Curry’s paradox. Whether or not a response that targets the behavior of the predicate $Val$ or the connective $\Rightarrow$ counts as logical will depend on whether these are considered logical vocabulary (see entry on logical constants).[^note-35] Still, we can say that some responses to v-Curry resemble logical responses to truth- or set-theoretic versions of Curry’s paradox, while others resemble topic-specific responses. Examples of the latter are responses that deny that a theory can express its own consequence relation, holding instead that it can only express a hierarchy of consequence relations, each of which takes into account the behavior of predicates or connectives expressing consequence relations prior in the hierarchy (see, e.g., Myhill 1975, Whittle 2004)[^myhill-1975][^whittle-2004]. Such a view can be combined with a non-hierarchical response to ordinary truth- or set-theoretical Curry paradoxes. Thus, a “non-uniform” solution to ordinary Curry paradoxes and v-Curry paradoxes may—once again—be a motivated non-uniformity.[^note-36]

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

### Key Historical Sources

### Other References

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=curry-paradox). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/curry-paradox/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=curry-paradox&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/curry-paradox/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

[Please contact the author with suggestions.]

## Related Entries

dialetheism | Gödel, Kurt: incompleteness theorems | lambda calculus, the | liar paradox | logic: algebraic propositional | logic: combinatory | logic: linear | logic: paraconsistent | logic: substructural | negation | paradoxes: and contemporary logic | Russell’s paradox | self-reference | set theory: alternative axiomatic theories

### Acknowledgments

We are grateful to Julien Murzi, Lorenzo Rossi, and an anonymous referee for detailed comments that led to clarifications and improvements. We also wish to thank the participants of our 2016 graduate seminar at UConn on this topic.

## Notes（原文脚注）

## Notes to Curry’s Paradox

[^note-1]: The term “Curry’s paradox” appears to originate in Fitch 1952; other influential early formulations include Moh 1954, Geach 1955, and Prior 1955. These will be discussed in section 2. Precursors to Curry’s paradox are also found in the work of medieval and late scholastic logicians: for references and discussion, see Ashworth 1974: 125, Read 2001 and Hanke 2013.

[^note-2]: Curry’s paper is entitled “The Inconsistency of Certain Formal Logics” (1942b). By “inconsistency”, he means *absolute* inconsistency, i.e., triviality.

[^note-3]: Typically, a theory’s consequence relation will be a *closure relation*, in the sense that $\Gamma \vdash_{\mathcal{T}} \alpha$ if and only if $\alpha$ is among the sentences in $Cn(\Gamma)$, where $Cn$ is a closure operation. See entry on algebraic propositional logic. However, Ripley (2015b) shows that the consequence relations of many of the theories that yield “contraction-free” responses to Curry’s paradox (see section 4.2.1) fail to be closure relations.

[^note-4]: The term “Curry sentence” is sometimes used in a narrower sense, namely for a sentence that says of itself (only) that *if it is true*, then $p$ (or, alternatively, an absurdity) is true (e.g., Beall 2009: 33, Zardini 2011: 503)[^beall-2009][^zardini-2011]. Some discussions (e.g., Restall 1994: vii, Humberstone 2006)[^humberstone-2006][^restall-1994] demarcate the relevant notion using a *biconditional* rather than intersubstitutability, namely as any $\kappa$ such that $\vdash_{\mathcal{T}} \kappa {\leftrightarrow}(\kappa {\rightarrow}\pi)$. The disadvantage here is that the behavior of the ${\rightarrow}$ is tied to that of the ${\leftrightarrow}$, even though they play very different roles in generating paradox. Note that the mere existence of a Curry sentence for a sentence-theory pair poses no paradox, nor is it an objection to the theory in question. For example, $\pi {\rightarrow}\pi$ will be a Curry sentence for $\pi {\rightarrow}\pi$ and the theory that consists of the theorems of classical logic, since $\pi {\rightarrow}\pi$ will be intersubstitutable with $(\pi {\rightarrow}\pi) {\rightarrow}(\pi {\rightarrow}\pi)$. The authors thank Lorenzo Rossi for raising this issue.

[^note-5]: If the consequence relation $\vdash_{\mathcal{T}}$ is assumed to be transitive, condition (ii) can be replaced with the condition that $\pi' \vdash_{\mathcal{T}} \pi$. However, one of the responses to Curry’s paradox considered below rejects transitivity.

[^note-6]: Section 3.3 and Section 6 will consider somewhat broader families of paradoxes.

[^note-7]: The letter $h$ is chosen to correspond with the $\mathfrak{H}$ that Curry 1942b uses to denote this property; likewise for $u$ below.

[^note-8]: Fitch considers the paradox in both its property-theoretic and set-theoretic versions (Fitch 1952: 89)[^fitch-1952].

[^note-9]: This is noted in Church’s contemporaneous review (Church 1942)[^church-1942].

[^note-10]: Strictly speaking, in his presentation, the “names” are numerals that denote numbers, not properties; properties are then given numerical codes.

[^note-11]: Geach actually uses diagonalization based on a theory of syntax to achieve the required self-reference. He adds that “we might instead use the familiar Gödelian devices” for simulating self-reference using diagonalization based on a theory of arithmetic. See entry on Gödel’s incompleteness theorems.

[^note-12]: On the relationship between Curry’s paradox and Löb’s theorem, see van Benthem (1978), who remarks on the “strange anti-parallel between Gödel’s proof, where a well-known semantic paradox inspired a formal result in terms of provability rather than truth, and Löb’s proof, where a semantic paradox … was extracted from a formal result about provability” (1978: 59). See also Priest (2021).

[^note-13]: This is not to be confused with a result in proof theory known as Curry’s Lemma following Anderson & Belnap (1975: 136).

[^note-14]: Zardini (2015), who calls Cont the rule of “absorption”, notes that given MP it entails there can be no Curry sentence for an “unacceptable sentence” $\pi$.

[^note-15]: It is also closely related to the method used in Löb’s original proof of Löb’s theorem (1955).

[^note-16]: A third counterpart of the Curry-Paradox Lemma replaces Cont with a rule which, in light of Peirce’s Law $\vdash_{\mathcal{T}} ((\alpha {\rightarrow} \beta ) {\rightarrow}\alpha)) {\rightarrow}\alpha$, could be called Peirce’s Rule:

**(PR)**

If $\alpha {\rightarrow}\beta \vdash_{\mathcal{T}} \alpha$ then $\vdash_{\mathcal{T}} \alpha$.

The proof of the Lemma is then structurally analogous to that in section 3.1. Here, too, one could instead use IdL and Peirce’s Law. Cf. Bunder 1986, Rogerson & Restall 2004. Unlike the principles used so far, Peirce’s Law and Peirce’s Rule fail in intuitionistic logic.

[^note-17]: The grounds given for denying that a target theory $\mathcal{T}$ is Curry-complete are typically parallel to grounds for denying that there is a sentence $\lambda$ such that it and its negation $\lnot\lambda$ are intersubstitutable according to $\mathcal{T}$. And the respective moves will have parallel philosophical ramifications. An exception may be the early response to Curry’s paradox by Fitch (1952, 1969). Fitch presents several possible restrictions on the inference rules of a natural deduction system that are motivated specifically by Curry’s paradox. Since their effect is to ensure violations of (Property) and (Set), these are Curry-incompleteness responses. In particular, Fitch’s systems allow a derivation of $\vdash_{\mathcal{T_P}} h \ \epsilon \ h {\rightarrow}\pi$. Yet, based on global features of that derivation, his “special restriction” and “restriction on nonrecurrence” would both block its extension to a derivation of $\vdash_{\mathcal{T_P}} h \ \epsilon \ h$. For helpful discussion, see Anderson 1975 and Rogerson 2007.

[^note-18]: Counterparts of the Curry-Paradox Lemma can be formulated using principles involving negation. For example, $\lnot\alpha \vdash_{\mathcal{T}} \alpha {\rightarrow}\beta$ together with the classical *reductio* rule

If $\lnot\alpha \vdash_{\mathcal{T}} \alpha$ then $\vdash_{\mathcal{T}} \alpha$

yield Peirce’s Rule of note 16. (Of course, in a language whose only “conditional” $\alpha {\rightarrow}\beta$ is the material conditional $\lnot\alpha \lor \beta$, the corresponding version of Curry’s paradox will involve negation. In that setting, Curry’s paradox poses a less distinctive challenge.)

[^note-19]: Like Geach, they add that Curry’s paradox shows that “the properties of implication … do us in on their own”. (By “implication”, they mean a conditional; see note 23.)

[^note-20]: Meyer et al. (1979) cite the relevant logics $E$ and $R$; the same is true of the contraction-free relevant logic $RWX$ (Slaney 1989)[^slaney-1989]. Glutty responses to paradox that *do* admit of Curry-complete theories include Priest 2006, Beall 2009, and Beall 2015.

[^note-21]: See also Restall 1993. Geach cites Moh’s paper, but there is little reason to think he had Ł$_{3}$ in mind as a logic with which one “might … hope” to avoid the Liar paradox but which remains vulnerable to Curry’s paradox. That is because Curry sentences with respect to the primitive conditional ${\rightarrow}$, which fails to satisfy Cont, pose no problem for a theory based on Ł$_{3}$. Gappy responses to paradox that admit of nontrivial Curry-complete theories include Kripke 1975, White 1979, and Field 2008.

[^note-22]: See also Curry & Feys 1958: 259. By “implication”, Prior means a conditional. Several years earlier, Quine had remarked that the use of “conditional” in place of “implication” is “encouragingly on the increase” (1953: 451).

[^note-23]: The fact that Curry’s paradox calls attention to this general structure could perhaps be what Curry et al. (1972) have in mind when they refer to Curry’s paradox as “the generalized Russell paradox”. However, their point is likely a different one, namely that Russell’s paradox becomes a *special case* of (the property- or set-theoretic form of) Curry’s paradox provided $\lnot\alpha$ is defined as $\alpha {\rightarrow}\bot$, as is possible in intuitionistic and classical logic.

[^note-24]: Since 2017, there have been proposals related to this one. Instead of characterizing a general *kind* of connective, Tapia-Navarro & Estrada-González (2020) introduce a particular “generalized negation” connective defined in terms of a conditional. Ahmad (2022) proposes a “general recipe” for semantic paradoxes, including the Liar paradox and the semantic version of Curry’s paradox. However, his recipe’s characterization of the logical behavior of the required “partial negative modality” differs from our conditions (P1) and (P2) on a Curry connective $\odot$ in that it does not exhaust the relevant behavior used in deriving the various paradoxes. Applying his recipe to yield the Liar paradox requires using additional rules for negation, and applying it to yield a Curry paradox requires using additional rules for the conditional.

[^note-25]: The same result obtains if the requirement that $\odot$ be a Curry connective is replaced with the requirement that it be a Curry′ connective, where this is defined by replacing P2 with

**(P2′)**

If $\odot\alpha \vdash_{\mathcal{T}} \alpha$ then $\vdash_{\mathcal{T}} \alpha$. (See note 16.)

For what are, in effect, quite a number of other ways of generalizing the Curry-Paradox Lemma, see Bimbó 2006 and Humberstone 2006. See also Section 3.3 on how the requirement of intersubstitability of $\mu$ and $\odot\mu$ may be weakened.

[^note-26]: In the case of Russell’s paradox in set theory, $\mu$ can be $\{x: x \notin x\} \in \{x: x \notin x\}$. In the case of the Liar paradox, $\mu$ can be $T\langle\lambda\rangle$ where $\lambda$ is $\lnot T\langle\lambda\rangle$.

[^note-27]: See also Curry & Feys 1958: 259. They add: “If one insists on regarding [$\odot\alpha$, defined as $\alpha {\rightarrow}\pi$] as a species of negation, then that negation is a minimal negation”. As noted below, this is strictly speaking incorrect. The explanation is that Curry’s proof of the corresponding claim, in Curry 1952, assumes that the conditional is characterized using an extension of the sequent calculus in Curry 1950: 32–33, which includes the rule of structural exchange. This is what guarantees that $\alpha \vdash (\alpha {\rightarrow}\pi) {\rightarrow}\pi$, i.e., $\alpha \vdash _{\mathcal{T}} \odot\odot\alpha$.

[^note-28]: These include the relevant logics $T$ and $E$ of Anderson & Belnap 1975, and many of the logics explored in Brady 2006.

[^note-29]: More recently, Priest (2017) has expressed ambivalence between the first and third options for addressing semantic versions of the paradoxes.

[^note-30]: More recent work includes Bacon 2015, Barrio et al. 2021, Cook 2014, Field 2017, Hlobil 2018 & 2019, Mares & Paoli 2014, Meadows 2014, Murzi 2014, Pailos 2020, Murzi & Rossi 2021, Murzi & Shapiro 2015, Nicolai & Rossi 2018, Pailos & Tajer 2017, Priest 2015, Rosenblatt 2017, Shapiro 2013 & 2015, Wansing & Priest 2015, Weber 2014, Zardini 2013 & 2014.

[^note-31]: The predicate form of v-Curry is discussed in detail by Beall & Murzi (2013); it is mentioned by Whittle (2004) and Shapiro (2011) and formulated for a predicate expressing informal provability in Carrara and Martino (2011). The connective and predicate forms are equivalent provided $Val(\langle\alpha\rangle, \langle\beta \rangle)$ and $\alpha {\Rightarrow}\beta $ are intersubstitutable according to $\mathcal{T}_{V}$. Accordingly, while the predicate form is a *semantic* paradox (in the sense that it concerns a feature of expressions that depends on their interpretation), it can be obtained by constructing a property- or set-theoretic Curry sentence $\kappa$ intersubstitutable according to $\mathcal{T}_{V}$ with $\kappa {\Rightarrow}\pi$ and ensuring that the latter sentence is in turn intersubstitutable with $Val(\langle\kappa\rangle, \langle\pi\rangle)$.

[^note-32]: The status of rules such as VP and VD is a topic of controversy: see Field 2017, Hlobil 2019.

[^note-33]: The present objection is specifically posed by the conclusion that $\pi$ is *true*, as opposed to the conclusion that $\vdash_{\mathcal{T}_{V}} \pi$. The fact that Ripley (2013) affirms the latter is not obviously problem for their nontransitive approach. On that approach, the claim that $\vdash_{\mathcal{T}_{V}} \pi$ amounts only to the claim that $\pi$ is *undeniable* according to $\mathcal{T}_V$. According to Ripley, paradoxical sentences are undeniable but may not be (“strictly”) asserted to be true.

[^note-34]: Indeed, Nicolai & Rossi (2018) argue that v-Curry paradoxes motivate responses according to which a third structural principle, namely the reflexivity principle $\phi \vdash_{\mathcal{T}_{V}}\! \phi$ codified by Id, can fail in cases where $\phi $ contains a predicate expressing the relation $\vdash_{\mathcal{T}_{V}}$. See also Murzi & Rossi 2021.

[^note-35]: Cook (2014) has argued influentially that the notion of logical validity does not give rise to a v-Curry paradox.

[^note-36]: The non-uniformity considered at the start of section 4 was a matter of giving different responses to ordinary Curry paradoxes arising in different domains (such as property theory set theory). The non-uniformity considered in section 5.2 was a matter of different connectives failing to qualify as Curry connectives for different reasons.

[^curry-1942a]: Curry, Haskell B., 1942a, “The Combinatory Foundations of Mathematical Logic”, *Journal of Symbolic Logic*, 7(2): 49–64. doi:10.2307/2266302

[^curry-1942b]: –––, 1942b, “The Inconsistency of Certain Formal Logics”, *Journal of Symbolic Logic*, 7(3): 115–117. doi:10.2307/2269292

[^curry-1958]: Curry, Haskell B. and Robert Feys, 1958, *Combinatory Logic*, volume 1, Amsterdam: North-Holland.

[^fitch-1952]: Fitch, Frederic B., 1952, *Symbolic Logic: An Introduction*, New York: Ronald Press Company.

[^geach-1955]: Geach, P.T., 1955, “On *Insolubilia*”, *Analysis*, 15(3): 71–72. doi:10.1093/analys/15.3.71

[^löb-1955]: Löb, M.H., 1955, “Solution of a Problem of Leon Henkin”, *Journal of Symbolic Logic*, 20(2): 115–118. doi:10.2307/2266895

[^meyer-1979]: Meyer, Robert K., Richard Routley, and J. Michael Dunn, 1979, “Curry’s paradox”, *Analysis*, 39(3): 124–128. doi:10.1093/analys/39.3.124

[^moh-1954]: Moh Shaw-Kwei, 1954, “Logical Paradoxes for Many-Valued Systems”, *Journal of Symbolic Logic*, 19(1): 37–40. doi:10.2307/2267648

[^prior-1955]: Prior, A.N., 1955, “Curry’s Paradox and 3-valued Logic”, *Australasian Journal of Philosophy*, 33(3): 177–82. doi:10.1080/00048405585200201

[^ahmad-2022]: Ahmad, Rashed, 2022, “A Recipe for Paradox”, *Australasian Journal of Logic*, 19(5): 254–281. doi:10.26686/ajl.v19i5.7887

[^anderson-1975]: Anderson, Alan Ross, 1975, “Fitch on Consistency”, in Anderson, Marcus, and Martin 1975: 123–141.

[^anderson-1975-2]: Anderson, Alan Ross and Nuel D. Belnap, Jr., 1975, *Entailment: the Logic of Relevance and Necessity*, volume 1, Princeton, NJ: Princeton University Press.

[^anderson-1975-3]: Anderson, Alan Ross, Ruth Barcan Marcus, and R.M. Martin (eds), 1975, *The Logical Enterprise*, New Haven, CT: Yale University Press.

[^ashworth-1974]: Ashworth, E.J., 1974, *Language and Logic in the Post-Medieval Period*, Dordrecht: Reidel.

[^bacon-2015]: Bacon, Andrew, 2015, “Paradoxes of Logical Equivalence and Identity”, *Topoi*, 34(1): 89–98. doi:10.1007/s11245-013-9193-8

[^barrio-2024]: Barrio, Eduardo and Edson Bezerra, 2024, “The Logics of a Universal Language”, *Asian Journal of Philosophy*, 3(12): 1–22. doi:10.1007/s44204-024-00140-3

[^barrio-2021]: Barrio, Eduardo, Lucas Rosenblatt, and Diego Tajer, 2021, “Capturing Naive Validity in the Cut-Free Approach”, *Synthese*, 199(Suppl 3): 707–723. doi:10.1007/s11229-016-1199-5

[^beall-2009]: Beall, Jc, 2009, *Spandrels of Truth*, Oxford: Oxford University Press. doi:10.1093/acprof:oso/9780199268733.001.0001

[^beall-2014a]: –––, 2014a, “End of Inclosure”, *Mind*, 123(491): 829–849. doi:10.1093/mind/fzu075

[^beall-2014b]: –––, 2014b, “Finding Tolerance Without Gluts”, *Mind*, 123(491): 791–811. doi:10.1093/mind/fzu081

[^beall-2015]: –––, 2015, “Free of Detachment: Logic, Rationality, and Gluts”, *Noûs*, 49(2): 410–423. doi:10.1111/nous.12029

[^beall-2013]: Beall, Jc and Julien Murzi, 2013, “Two Flavors of Curry’s Paradox”, *Journal of Philosophy*, 110(3): 143–165. doi:10.5840/jphil2013110336

[^bimbó-2006]: Bimbó, Katalin, 2006, “Curry-Type Paradoxes”, *Logique & Analyse*, 49(195): 227–240.

[^brady-2006]: Brady, Ross, 2006, *Universal Logic*, Stanford, CA: CSLI Publications.

[^bunder-1986]: Bunder, M.W., 1986, “Tautologies That, with An Unrestricted Comprehension Axiom, Lead to Inconsistency or Triviality”, *Journal of Non-Classical Logic*, 3(2): 5–12.

[^burge-1979]: Burge, Tyler, 1979, “Semantical Paradox”, *Journal of Philosophy*, 76(4): 169–198. doi:10.2307/2025724

[^carnap-1934]: Carnap, Rudolf, 1934, “Die Antinomien und die Unvollständigkeit der Mathematik”, *Monatshefte für Mathematik*, 41: 263–84.

[^carnap-1937]: –––, 1937, *The Logical Syntax of Language*, Amethe Smeaton (trans), London: K. Paul Trench.

[^carrara-2011]: Carrara, Massimiliano and Enrico Martino, 2011, “*Curry’ Paradox*: A New Argument for *Trivialism*”, *Logic and Philosophy of Science*, 9(1): 199–206.

[^church-1932]: Church, Alonzo, 1932, “A Set of Postulates for the Foundation of Logic”, *Annals of Mathematics*, 33(2): 346–366. doi:10.2307/1968337

[^church-1942]: –––, 1942, “Review: *The Inconsistency of Certain Formal Logics* by Haskell B. Curry”, *Journal of Symbolic Logic*, 7(4): 170–71. doi:10.2307/2268117

[^cook-2014]: Cook, Roy T., 2014, “There is No Paradox of Logical Validity!”, *Logica Universalis*, 8(3–4): 447–467. doi:10.1007/s11787-014-0094-4

[^curry-1930]: Curry, Haskell B., 1930, “Grundlagen der kombinatorischen Logik (Teile I & II)”, *American Journal of Mathematics*, 52: 509–36, 789–834.

[^curry-1950]: –––, 1950, *A Theory of Formal Deducibility*, (Notre Dame Mathematical Lectures, 6), Notre Dame, IN: University of Notre Dame Press. [[Curry 1950 available online](http://projecteuclid.org/euclid.ndml/1175197175)]

[^curry-1952]: –––, 1952, “On the Definition of Negation by a Fixed Proposition in Inferential Calculus”, *Journal of Symbolic Logic*, 17(2): 98–104. doi:10.2307/2266240

[^curry-1972]: Curry, Haskell B., J. Roger Hindley, and Jonathan P. Seldin, 1972, *Combinatory Logic*, volume 2, (Studies in Logic and the Foundations of Mathematics, 65), Amsterdam: North-Holland.

[^field-2008]: Field, Hartry, 2008, *Saving Truth from Paradox*, Oxford: Oxford University Press. doi:10.1093/acprof:oso/9780199230747.001.0001

[^field-2017]: –––, 2017, “Disarming a Paradox of Validity”, *Notre Dame Journal of Formal Logic*, 58(1): 1–19. doi:10.1215/00294527-3699865

[^fitch-1969]: Fitch, Frederic B., 1969, “A Method for Avoiding the Curry Paradox”, in Nicholas Rescher (ed.), *Essays in Honor of Carl. G. Hempel*, Dordrecht: Reidel, pp. 255–265.

[^french-2016]: French, Rohan, 2016, “Structural Reflexivity and the Paradoxes of Self-Reference”, *Ergo*, 3(5): 113–131. doi:10.3998/ergo.12405314.0003.005

[^glanzberg-2001]: Glanzberg, Michael, 2001, “The Liar in Context”, *Philosophical Studies*, 103(3): 217–251. doi:10.1023/A:1010314719817

[^glanzberg-2004]: –––, 2004, “A Contextual-Hierarchical Approach to Truth and the Liar Paradox”, *Journal of Philosophical Logic*, 33(1): 27–88. doi:10.1023/B:LOGI.0000019227.09236.f5

[^goldstein-2000]: Goldstein, Laurence, 2000, “A Unified Solution to Some Paradoxes”, *Proceedings of the Aristotelian Society*, 100(1): 53–74. doi:10.1111/j.0066-7372.2003.00003.x

[^goodship-1996]: Goodship, Laura, 1996, “On Dialethism”, *Australasian Journal of Philosophy*, 74(1): 153–161. doi:10.1080/00048409612347131

[^grelling-1908]: Grelling, Kurt and Leonard Nelson, 1908, “Bemerkungen zu den Paradoxien von Russell und Burali-Forti”, *Abhandlungen der Fries’schen Schule*, 2: 301–334.

[^gupta-1993]: Gupta, Anil and Nuel Belnap, 1993, *The Revision Theory of Truth*, Cambridge, MA: MIT Press.

[^halbach-2014]: Halbach, Volker and Albert Visser, 2014, “The Henkin Sentence”, in Maria Manzano, Ildikó Sain, and Enrique Alonso (eds), *The Life and Work of Leon Henkin*, (Studies in Universal Logic), Cham: Springer International, pp. 249–264. doi:10.1007/978-3-319-09719-0_17

[^hanke-2013]: Hanke, Miroslav, 2013, “Implied-Meaning Analysis of the Currian Conditional”, *History and Philosophy of Logic*, 34(4): 367–380. doi:10.1080/01445340.2013.812832

[^hilbert-1939]: Hilbert, David and Paul Bernays, 1939, *Grundlagen der Mathematik*, volume II, Berlin: Springer.

[^hlobil-2018]: Hlobil, Ulf, 2018, “The Cut-Free Approach and the Admissibility-Curry”, *Thought*, 7: 40–48. doi:10.1002/tht3.267

[^hlobil-2019]: –––, 2019, “Faithfulness for Naive Validity”, *Synthese*, 196: 4759–4774. doi:10.1007/s11229-018-1687-x

[^humberstone-2006]: Humberstone, Lloyd, 2006, “Variations on a Theme of Curry”, *Notre Dame Journal of Formal Logic*, 47(1): 101–131. doi:10.1305/ndjfl/1143468315

[^kaplan-1960]: Kaplan, David and Richard Montague, 1960, “A Paradox Regained”, *Notre Dame Journal of Formal Logic*, 1(3): 79–90. doi:10.1305/ndjfl/1093956549

[^kripke-1975]: Kripke, Saul A., 1975, “Outline of a Theory of Truth”, *Journal of Philosophy*, 72(19): 690–716. doi:10.2307/2024634

[^mares-2014]: Mares, Edwin and Francesco Paoli, 2014, “Logical Consequence and the Paradoxes”, *Journal of Philosophical Logic*, 43(2–3): 439–469. doi:10.1007/s10992-013-9268-4

[^meadows-2014]: Meadows, Toby, 2014, “Fixed Points for Consequence Relations”, *Logique & Analyse*, 57(227): 333–357. doi:10.2143/LEA.227.0.3053509

[^murzi-2014]: Murzi, Julien, 2014, “The Inexpressibility of Validity”, *Analysis*, 74(1): 65–81. doi:10.1093/analys/ant096

[^murzi-2021]: Murzi, Julien and Lorenzo Rossi, 2021, “Naïve Validity”, *Synthese*, 199(Suppl 3): 819–841. doi:10.1007/s11229-017-1541-6

[^murzi-2015]: Murzi, Julien and Lionel Shapiro, 2015, “Validity and Truth-Preservation”, in Theodora Achourioti, Henri Galinon, José Martínez-Fernández, and Kentaro Fujimoto (eds), *Unifying the Philosophy of Truth*, Dordrecht: Springer. doi:10.1007/978-94-017-9673-6_22

[^myhill-1960]: Myhill, John, 1960, “Some Remarks On the Notion of Proof”, *Journal of Philosophy*, 57(14): 461–471. doi:10.2307/2023664

[^myhill-1975]: –––, 1975, “Levels of Implication”, in Anderson, Marcus, and Martin 1975: 179–185.

[^nicolai-2018]: Nicolai, Carlo and Lorenzo Rossi, 2018, “Principles for Object-Linguistic Consequence: from Logical to Irreflexive”, *Journal of Philosophical Logic*, 47: 549–577. doi:10.1007/s10992-017-9438-x

[^nolan-2016]: Nolan, Daniel, 2016, “Conditionals and Curry”, *Philosophical Studies*, 173(10): 2629–2649. doi:10.1007/s11098-016-0666-7

[^pailos-2020]: Pailos, Federico, 2020, “Validity, Dialetheism and Self-Reference”, *Synthese*, 197: 773–792. doi:10.1007/s11229-018-1731-x

[^pailos-2025]: –––, 2025, “Metainferentially Substructural Validity Theories”, *Journal of Applied Non-Classical Logics*, 35(3): 244–265. doi:10.1080/11663081.2024.2430107

[^pailos-2017]: Pailos, Federico and Diego Tajer, 2017, “Validity in a Dialetheist Framework”, *Logique & Analyse*, 60(238): 191–202. doi:10.2143/LEA.238.0.3212073

[^pleitz-2015]: Pleitz, Martin, 2015, “Curry’s Paradox and the Inclosure Scheme”, in Pavel Arazim and Michal Dančák (eds), *Logica Yearbook 2014*, London: College Publications.

[^porter-2023]: Porter, Brian, 2023, *Three Essays on Substructural Approaches to Semantic Paradoxes*, PhD thesis, City University of New York. [[Porter 2023 available online](https://academicworks.cuny.edu/gc_etds/5144/)]

[^priest-1994]: Priest, Graham, 1994, “The Structure of the Paradoxes of Self-Reference”, *Mind*, 103(409): 25–34. doi:10.1093/mind/103.409.25

[^priest-2000]: –––, 2000, “On the Principle of Uniform Solution: A Reply to Smith”, *Mind*, 109(433): 123–126. doi:10.1093/mind/109.433.123

[^priest-2002]: –––, 2002, *Beyond the Limits of Thought*, Oxford: Oxford University Press. Expanded edition (first published 1995). doi:10.1093/acprof:oso/9780199254057.001.0001

[^priest-2006]: –––, 2006, *In Contradiction*, Oxford: Oxford University Press. Expanded edition (first published 1987). doi:10.1093/acprof:oso/9780199263301.001.0001

[^priest-2008]: –––, 2008, *An Introduction to Non-Classical Logic: From If to Is*, 2nd edition, Cambridge: Cambridge University Press. doi:10.1017/CBO9780511801174

[^priest-2015]: –––, 2015, “Fusion and Confusion”, *Topoi*, 34(1): 55–61. doi:10.1007/s11245-013-9175-x

[^priest-2017]: –––, 2017, “What *If*? The Exploration of an Idea”, *Australasian Journal of Logic*, 14(1): 54–127. doi:10.26686/ajl.v14i1.4028

[^priest-2021]: –––, 2021, “Löb’s Theorem and Curry’s Paradox”, *Inference*, 6(3): 1–18. doi:10.37282/991819.21.49

[^quine-1953]: Quine, W.V.O., 1953, “Mr. Strawson on Logical Theory”, *Mind*, 62(248): 433–451. doi:10.1093/mind/LXII.248.433

[^read-2001]: Read, Stephen, 2001, “Self-Reference and Validity Revisited”, in Mikko Yrjönsuuri (ed.), *Medieval Formal Logic*, Dordrecht: Kluwer Academic Publishers, pp. 183–196. doi:10.1007/978-94-015-9713-5_7

[^restall-1993]: Restall, Greg, 1993, “How to be *Really* Contraction Free”, *Studia Logica*, 52(3): 381–91. doi:10.1007/BF01057653

[^restall-1994]: –––, 1994, *On Logics Without Contraction*, PhD thesis, The University of Queensland. [[Restall 1994 available online](http://consequently.org/writing/onlogics/)]

[^restall-2005]: –––, 2005, “Multiple Conclusions”, in Petr Hájek, Luis Valdés-Villanueva, and Dag Westerståhl (eds), *Logic, Methodology and the Philosophy of Science: Proceedings of the Twelfth International Congress*, London: College Publications, pp. 189–205. [[Restall 2005 available online](http://consequently.org/writing/multipleconclusions/)]

[^ripley-2013]: Ripley, Ellie, 2013, “Paradoxes and Failures of Cut”, *Australasian Journal of Philosophy*, 91: 139–164. doi:10.1080/00048402.2011.630010

[^ripley-2015a]: –––, 2015a, “Comparing Substructural Theories of Truth”, *Ergo*, 2(13): 299–328. doi:10.3998/ergo.12405314.0002.013

[^ripley-2015b]: –––, 2015b, “Contraction and Closure”, *Thought*, 4(2): 131–138. doi:10.1002/tht3.166

[^rogerson-2007]: Rogerson, Susan, 2007, “Natural Deduction and Curry’s Paradox”, *Journal of Philosophical Logic*, 36(2): 155–179. doi:10.1007/s10992-006-9032-0

[^rogerson-2004]: Rogerson, Susan and Greg Restall, 2004, “Routes to Triviality”, *Journal of Philosophical Logic*, 33(4): 421–436. doi:10.1023/B:LOGI.0000036853.44128.8f

[^rosenblatt-2017]: Rosenblatt, Lucas, 2017, “Naive Validity, Internalization, and Substructural Approaches to Paradox”, *Ergo*, 4(4): 93–120. doi:10.3998/ergo.12405314.0004.004

[^seldin-2006]: Seldin, Jonathan P., 2006, “The Logic of Curry and Church”, in Dov M. Gabbay and John Woods (eds), *Handbook of the History of Logic, Volume 5: Logic from Russell to Church*, Amsterdam: Elsevier, pp. 819–873.

[^shapiro-2011]: Shapiro, Lionel, 2011, “Deflating Logical Consequence”, *The Philosophical Quarterly*, 61(243): 320–42. doi:10.1111/j.1467-9213.2010.678.x

[^shapiro-2013]: –––, 2013, “Validity Curry Strengthened”, *Thought*, 2: 100–107. doi:10.1002/tht3.80

[^shapiro-2015]: –––, 2015, “Naive Structure, Contraction and Paradox”, *Topoi*, 34(1): 75–87. doi:10.1007/s11245-014-9235-x

[^simmons-1993]: Simmons, Keith, 1993, *Universality and the Liar: An Essay on Truth and the Diagonal Argument*, Cambridge: Cambridge University Press.

[^slaney-1989]: Slaney, John, 1989, “RWX in Not Curry Paraconsistent”, in Graham Priest, Richard Routley, and Jean Norman (eds), *Paraconsistent Logic: Essays on the Inconsistent*, Munich: Philosophia, pp. 472–480.

[^slaney-1990]: –––, 1990, “A General Logic”, *Australasian Journal of Philosophy*, 68(1): 74–88. doi:10.1080/00048409012340183

[^smith-2000]: Smith, Nicholas J.J., 2000, “The Principle of Uniform Solution (of the Paradoxes of Self-Reference)”, *Mind*, 109(433): 117–122. doi:10.1093/mind/109.433.117

[^tapia-navarro-2020]: Tapia-Navarro, Manuel and Luis Estrada-González, 2020, “When Curry Met Abel”, *Logic Journal of the IGPL*, 28(6): 1233–1242. doi:10.1093/jigpal/jzaa006

[^benthem-1978]: van Benthem, Johan, 1978, “Four Paradoxes”, *Journal of Philosophical Logic*, 7(1): 49–72. doi:10.1007/BF00245920

[^wansing-2015]: Wansing, Heinrich and Graham Priest, 2015, “External Curries”, *Journal of Philosophical Logic*, 44(4): 453–471. doi:10.1007/s10992-014-9336-4

[^weber-2014]: Weber, Zach, 2014, “Naïve Validity”, *The Philosophical Quarterly*, 64(254): 99–114. doi:10.1093/pq/pqt016

[^weber-2014-2]: Weber, Zach, Ellie Ripley, Graham Priest, Dominic Hyde, and Mark Colyvan, 2014, “Tolerating Gluts”, *Mind*, 123(491): 813–828. doi:10.1093/mind/fzu057

[^weir-2015]: Weir, Alan, 2015, “A Robust Non-Transitive Logic”, *Topoi*, 34(1): 99–107. doi:10.1007/s11245-013-9176-9

[^white-1979]: White, Richard B., 1979, “The Consistency of the Axiom of Comprehension in the Infinite-Valued Predicate Logic of Łukasiewicz”, *Journal of Philosophical Logic*, 8(1): 509–534. doi:10.1007/BF00258447

[^whittle-2004]: Whittle, Bruno, 2004, “Dialetheism, Logical Consequence and Hierarchy”, *Analysis*, 64: 318–26. doi:10.1093/analys/64.4.318

[^zardini-2011]: Zardini, Elia, 2011, “Truth Without Contra(di)ction”, *Review of Symbolic Logic*, 4(4): 498–535. doi:10.1017/S1755020311000177

[^zardini-2013]: –––, 2013, “Naive *Modus Ponens*”, *Journal of Philosophical Logic*, 42(4): 575–593. doi:10.1007/s10992-012-9239-1

[^zardini-2014]: –––, 2014, “Naive Truth and Naive Logical Properties”, *Review of Symbolic Logic*, 7(2): 351–384. doi:10.1017/S1755020314000045

[^zardini-2015]: –––, 2015, “Getting One for Two, or the Contractors’ Bad Deal. Towards a Unified Solution to the Semantic Paradoxes”, in Theodora Achourioti, Henri Galinon, José Martínez-Fernández, and Kentaro Fujimoto (eds.), *Unifying the Philosophy of Truth*, Dordrecht: Springer. doi:10.1007/978-94-017-9673-6_23
