# Confirmation
**First published Thu May 30, 2013; substantive revision Mon Aug 4, 2025**

*Crupi, Vincenzo*

Human cognition and behavior heavily relies on the notion that evidence (data, premises) can affect the credibility of hypotheses (theories, conclusions). This general idea seems to underlie sound and effective inferential practices in all sorts of domains, from everyday reasoning up to the frontiers of science. Yet it is also clear that, even with extensive and truthful evidence available, drawing a mistaken conclusion is more than a mere possibility. For painfully tangible examples, one only has to consider missed medical diagnoses (see Newman-Toker et al. 2022)[^newman-toker-2022] or judicial errors (see Liebman et al. 2000)[^liebman-2000]. The Scottish philosopher David Hume (1711–1776) is usually credited for having disclosed the theoretical roots of these considerations in a particularly transparent way (see Howson 2000, Lange 2011, and Varzi 2008)[^howson-2000][^lange-2011][^varzi-2008]. In most cases of interest, Hume pointed out, many alternative candidate hypotheses remain logically compatible with all the relevant information at one’s disposal, so that none of the former can be singled out by the latter with full certainty. Thus, under usual circumstances, reasoning from evidence must remain fallible.

This fundamental insight has been the source of a lasting theoretical challenge: if amenable to analysis, the role of evidence as supporting (or infirming) hypotheses has to be grasped by more nuanced tools than plain logical entailment. As emphasized in a joke attributed to American philosopher Morris Raphael Cohen (1880–1947), logic textbooks had to be divided in two parts: in the first part, on deductive logic, unwarranted forms of inference (deductive fallacies) are exposed; in the second part, on inductive logic, they are endorsed (see Meehl 1990, 110)[^meehl-1990]. In contemporary philosophy, *confirmation theory* can be roughly described as the area where efforts have been made to take up the challenge of defining plausible models of non-deductive reasoning. Its central technical term—*confirmation*—has often been used more or less interchangeably with “evidential support”, “inductive strength”, and the like. Here we will generally comply with this liberal usage (although more subtle conceptual and terminological distinctions are sometimes drawn).

Confirmation theory has proven a rather difficult endeavour. In principle, it would aim at providing understanding and guidance for tasks such as diagnosis, prediction, and learning in virtually any area of inquiry. Yet popular accounts of confirmation have often been taken to run into troubles even when faced with philosophical toy examples. Be that as it may, there is at least one real-world kind of activity which has remained a prevalent target and benchmark, i.e., scientific reasoning, and especially key episodes from the history of modern and contemporary natural science. The motivation for this is easily figured out. Mature sciences seem to have been uniquely effective in relying on observed evidence to establish extremely general, powerful, and sophisticated theories. Indeed, being capable of receiving genuine support from empirical evidence is itself a very distinctive trait of scientific hypotheses as compared to other kinds of statements. A philosophical characterization of what science is would then seem to require an understanding of the logic of confirmation. And so, traditionally, confirmation theory has come to be a central concern of philosophers of science.

In the following, major approaches to confirmation theory are overviewed according to a classification that is relatively standard (see Earman and Salmon 1992; Norton 2005)[^earman-1992][^earman-1992-2][^norton-2005]: confirmation by instances (Section 1), hypothetico-deductivism and its variants (Section 2), and probabilistic (Bayesian) approaches (Section 3).

## 1. Confirmation by instances

In a seminal essay on induction, Jean Nicod (1924) offered the following important remark:

> Consider the formula or the law: $F$ entails $G$. How can a particular proposition, or more briefly, a fact affect its probability? If this fact consists of the presence of $G$ in a case of $F$, it is favourable to the law […]; on the contrary, if it consists of the absence of $G$ in a case of $F$, it is unfavourable to this law. (219, notation slightly adapted)

Nicod’s work was an influential source for Carl Gustav Hempel’s (1943, 1945) early studies in the logic of confirmation. In Hempel’s view, the key valid message of Nicod’s statement is that the observation report that an object $a$ displays properties $F$ and $G$ (e.g., that $a$ is a swan and is white) confirms the universal hypothesis that all $F$-objects are $G$-objects (namely, that all swans are white). Apparently, it is by means of this kind of confirmation by instances that one can obtain supporting evidence for statements such as “sodium salts burn yellow”, “wolves live in a pack”, or “planets move in elliptical orbits” (also see Russell 1912, Ch. 6)[^russell-1912]. We will now see the essential features of Hempel’s analysis of confirmation.

### 1.1 Hempel’s theory

Hempel’s theory addresses the non-deductive relation of confirmation between evidence and hypothesis, but relies thoroughly on standard logic for its full technical formulation. As a consequence, it also goes beyond Nicod’s idea in terms of clarity and rigor.

Let $\bL$ be the set of the closed sentences of a first-order logical language $L$ (finite, for simplicity) and consider $h, e \in \bL$. Also let $e$, the evidence statement, be consistent and contain individual constants only (no quantifier), and let $I(e)$ be the set of all constants occurring (non-vacuously) in $e$. So, for example, if $e = Qa \wedge Ra$, then $I(e) = \{a\}$, and if $e = Qa \wedge Qb$, then $I(e) = \{a,b\}$. (The non-vacuity clause is meant to ensure that if sentence $e$ happens to be, say, $Qa \wedge Qb \wedge (Rc \vee \neg Rc)$, then $I(e)$ still is $\{a, b\}$, for $e$ does not really state anything non-trivial about the individual denoted by $c$. See Sprenger 2011a, 241–242.) Hempel’s theory relies on the technical construct of the *development* of hypothesis $h$ for evidence $e$, or the $e$-development of $h$, indicated by $dev_{e}(h)$. Intuitively, $dev_{e}(h)$ is all that (and only what) $h$ says once restricted to the individuals mentioned (non-vacuously) in $e$, i.e., exactly those denoted by the elements of $I(e)$.

The notion of the $e$-development of hypothesis $h$ can be given an entirely general and precise definition, but we’ll not need this level of detail here. Suffice it to say that the $e$-development of a universally quantified material conditional $\forall x(Fx \rightarrow Gx)$ is just as expected, that is: $Fa \rightarrow Ga$ in case $I(e) = \{a\}$; $(Fa \rightarrow Ga) \wedge (Fb \rightarrow Gb)$ in case $I(e) = \{a,b\}$, and so on. Following Hempel, we will take universally quantified material conditionals as canonical logical representations of relevant hypotheses. So, for instance, we will count a statement of the form $\forall x(Fx \rightarrow Gx)$ as an adequate rendition of, say, “all pieces of copper conduct electricity”.

In Hempel’s theory, evidence statement $e$ is said to confirm hypothesis $h$ just in case it entails, not $h$ in its full extension, but suitable *instantiations* of $h$. The technical notion of the $e$-development of $h$ is devised to identify precisely those relevant instantiations, that is, the consequences of $h$ as restricted to the individuals involved in $e$. More precisely, Hempelian confirmation can be defined as follows:

**Hempelian confirmation** For any $h,e \in \bL$ such that $e$ is consistent and contains individual constants only (no quantifier):

1. evidence $e$ *directly Hempel-confirms* hypothesis $h$ if and only if $e \vDash dev_{e}(h)$; $e$ *Hempel-confirms* $h$ if and only if, for some $s \in \bL$, $e \vDash dev_{e}(s)$ and $s \vDash h$;
2. evidence $e$ *directly Hempel-disconfirms* hypothesis $h$ if and only if $e \vDash dev_{e}(\neg h)$; $e$ *Hempel-disconfirms* $h$ if and only if, for some $s \in \bL, e \vDash dev_{e}(s)$ and $s \vDash \neg h$;
3. evidence $e$ *is Hempel-neutral* for hypothesis $h$ otherwise.

In each of clauses (i) and (ii), Hempelian confirmation (disconfirmation, respectively) is a generalization of *direct* Hempelian confirmation (disconfirmation). To retrieve the latter as a special case of the former, one only has to posit $s = h$ $(\neg h$, respectively, for disconfirmation).

By direct Hempelian confirmation, evidence statement $e$ that, say, object $a$ is a white swan, $swan(a) \wedge white(a)$, confirms hypothesis $h$ that all swans are white, $\forall x(swan(x) \rightarrow white(x))$, because the former entails the $e$-development of the latter, that is, $swan(a) \rightarrow white(a)$. This is a desired result, according to Hempel’s reading of Nicod. By (indirect) Hempelian confirmation, moreover, $swan(a) \wedge white(a)$ also confirms that a particular further object $b$ will be white, if it’s a swan, i.e., $swan(b) \rightarrow white(b)$ (to see this, just set $s = \forall x(swan(x) \rightarrow white(x))$).

The second possibility considered by Nicod (“the *absence* of $G$ in a case of $F\,$”) can be accounted for by Hempelian disconfirmation. For the evidence statement $e$ that $a$ is a non-white swan—$swan(a) \wedge \neg white(a)$—entails (in fact, is identical to) the $e$-development of the hypothesis that there exist non-white swans—$\exists x(swan(x) \wedge \neg white(x))$—which in turn is just the negation of $\forall x(swan(x) \rightarrow white(x))$. So the latter is disconfirmed by the evidence in this case. And finally, $e = swan(a) \wedge \neg white(a)$ also Hempel-disconfirms that a particular further object $b$ will be white if it’s a swan, i.e., $swan(b) \rightarrow white(b)$, because the negation of the latter, $swan(b) \wedge \neg white(b)$, is entailed by $s = \forall x(swan(x) \wedge \neg white(x))$ and $e \vDash dev_{e}(s)$.

So, to sum up, we have four illustrations of how Hempel’s theory articulates Nicod’s basic ideas, to wit:

- (the observation report of) a white swan (directly) Hempel-confirms that all swans are white;
- (the observation report of) a white swan also Hempel-confirms that a further swan will be white;
- (the observation report of) a non-white swan (directly) Hempel-disconfirms that all swans are white;
- (the observation report of) a non-white swan also Hempel-disconfirms that a further swan will be white.

### 1.2 Two paradoxes and other difficulties

*The ravens paradox* (Hempel 1937, 1945)[^hempel-1937]. Consider the following statements:

**($h$)**

$\forall x(raven(x) \rightarrow black(x))$, i.e., all ravens are black;

**($e$)**

$raven(a) \wedge black(a)$, i.e., $a$ is a black raven;

($e^*$)

$\neg black(a^*) \wedge \neg raven(a^*)$, i.e., $a^*$ is a non-black non-raven (say, a green apple).

Is hypothesis $h$ confirmed by $e$ and $e^*$ alike? That is, is the claim that all ravens are black equally confirmed by the observation of a black raven and by the observation of a non-black non-raven (e.g., a green apple)? One would want to say no, but Hempel’s theory is unable to draw this distinction. Let’s see why.

As we know, $e$ (directly) Hempel-confirms $h$, according to Hempel’s reconstruction of Nicod. By the same token, $e^*$ (directly) Hempel-confirms the hypothesis that all non-black objects are non-ravens, i.e., $h^* = \forall x(\neg black(x) \rightarrow \neg raven(x))$. But $h^* \vDash h$ ($h$ and $h^*$ are just logically equivalent). So, $e^*$ (the observation report of a non-black non-raven), like $e$ (black raven), does (indirectly) Hempel-confirm $h$ (all ravens are black). Indeed, as $\neg raven(a)$ entails $raven(a) \rightarrow black(a)$, it can be shown that $h$ is (directly) Hempel-confirmed by the observation of *any* object that is not a raven (an apple, a cat, a shoe), apparently disclosing puzzling “prospects for indoor ornithology” (Goodman 1955, 71)[^goodman-1955].

$Blite$ (Goodman 1955)[^goodman-1955]. Consider the peculiar predicate “$blite$”, defined as follows: an object is blite just in case (i) it is black if examined at some moment $t$ up to some future time $T$ (say, the next expected appearance of Halley’s comet, in 2061) and (ii) it is white if possibly examined only afterwards. So we posit $blite(x) \equiv (ex_{t\le T}(x) \rightarrow black(x)) \wedge (\neg ex_{t\le T}(x) \rightarrow white(x))$. Now consider the following statements:

**($h$)**

$\forall x(raven(x) \rightarrow black(x))$, i.e., all ravens are black;

($h^*$)

$\forall x(raven(x) \rightarrow blite(x))$, i.e., all ravens are blite;

**($e$)**

$e = raven(a) \wedge ex_{t\le T}(a) \wedge black(a)$, i.e., $a$ is a raven observed no later than $T$ and it is black.

Does $e$ confirm hypotheses $h$ and $h^*$ alike? That is, does the observation of a black raven before $T$ confirm equally the claim that all ravens are black as the claim that all ravens are blite? Here again, one would want to say no, but Hempel’s theory is unable to draw the distinction. For one can check that the $e$-developments of $h$ and $h^*$ are both entailed by $e$. Thus, $e$ (the report of a raven examined no later than $T$ and found to be black) does Hempel-confirm $h^*$ (all ravens are blite) just as it confirms $h$ (all ravens are black). Moreover, $e$ also Hempel-confirms the statement that a raven will be white if examined after $T$, because this is a logical consequence of $h^*$ (which is directly Hempel-confirmed by $e$). And finally, suppose that $blurple(x) \equiv (ex_{t\le T}(x) \rightarrow black(x)) \wedge (\neg ex_{t\le T}(x) \rightarrow purple(x)).$ We then have that the very same evidence statement $e$ Hempel-confirms the hypothesis that all ravens are blurple, and thus also its implication that a raven will be $purple$ if examined after $T$!

A seemingly obvious idea, here, is that there must be something inherently wrong with predicates such as $blite$ or $blurple$ (and perhaps *non-raven* and *non-black*, too) and thus a principled way to rule them out as “unnatural”. Then one could restrict confirmation theory accordingly, i.e., to “natural kinds” only (see, e.g., Quine 1970)[^quine-1970][^quine-1970-2]. Yet this point turns out be very difficult to pursue coherently and it has not borne much fruit in this discussion (Rinard 2014 is a recent exception)[^rinard-2014]. After all, for all we know, it is a perfectly “natural” feature of a token of the “natural kind” *water* that it is found in one physical state for temperatures below 0 degrees Celsius and in an entirely different state for temperatures above that threshold. So why should the time threshold $T$ in $blite$ or $blurple$ be a reason to dismiss those predicates? (The water example comes from Howson 2000, 31–32. See Schwartz 2011, 399 ff., for a more general assessment of this issue.)[^howson-2000][^schwartz-2011]

The above, widely known “paradoxes” then suggest that Hempel’s analysis of confirmation is *too liberal*: it sanctions the existence of confirmation relations that are intuitively very unsound (see Earman and Salmon 1992, 54, and Sprenger 2011a, 243, for more on this)[^earman-1992][^earman-1992-2][^sprenger-2011a]. Yet the Hempelian notion of confirmation turns out to be very restrictive, too, on other accounts. For suppose that hypothesis $h$ and evidence $e$ do not share any piece of non-logical vocabulary. $h$ might be, say, Newton’s law of universal gravitation (connecting force, distances and masses), while $e$ could be the description of certain spots on a telescopic image. Throughout modern physics, significant relations of confirmation and disconfirmation were taken to obtain between statements like these. Indeed, telescopic sightings have been crucial evidence for Newton’s law as applied to celestial bodies. However, as their non-logical vocabularies are disjoint, $e$ and $h$ must simply be logically independent, and so must be $e$ and $dev_{e}(h)$ (with very minor caveats, this follows from Craig’s so-called interpolation theorem, see Craig 1957)[^craig-1957]. In such circumstances, there can be nothing but Hempel-neutrality between evidence and hypothesis. So Hempel’s original theory seems to lack the resources to capture a key feature of inductive inference in science as well as in several other domains, i.e., the kind of “vertical” relationships of confirmation (and disconfirmation) between the description of observed phenomena and hypotheses concerning underlying structures, causes, and processes.

To overcome the latter difficulty, Clark Glymour (1980a) embedded a refined version of Hempelian confirmation by instances in his analysis of scientific reasoning. In Glymour’s revision, hypothesis $h$ is confirmed by some evidence $e$ even if appropriate auxiliary hypotheses and assumptions must be involved for $e$ to entail the relevant instances of $h$. This important theoretical move turns confirmation into a *three*-place relation concerning the evidence, the target hypothesis, and (a conjunction of) auxiliaries. Originally, Glymour presented his sophisticated neo-Hempelian approach in stark contrast with the competing traditional view of so-called *hypothetico-deductivism* (HD). Despite his explicit intentions, however, several commentators have pointed out that, partly because of the due recognition of the role of auxiliary assumptions, Glymour’s proposal and HD end up being plagued by similar difficulties (see, e.g., Horwich 1983, Woodward 1983, and Worrall 1982)[^horwich-1983][^woodward-1983][^worrall-1982]. In the next section, we will discuss the HD framework for confirmation and also compare it with Hempelian confirmation. It will thus be convenient to have a suitable extended definition of the latter, following the remarks above. Here is one that serves our purposes:

**Hempelian confirmation (extended)** For any $h, e, k \in \bL$ such that $e$ contains individual constants only (no quantifier), $k$ contains quantifiers only (no individual constant), $\alpha\ = dev_{e}(k)$, $k \not\vDash h$, and $e\wedge \alpha$ is consistent:

1. $e$ *directly Hempel-confirms* $h$ *relative to* $k$ if and only if $e\wedge \alpha \vDash dev_{e}(h)$; $e$ *Hempel-confirms* $h$ *relative to* $k$ if and only if, for some $s \in \bL, e\wedge \alpha \vDash dev_{e}(s)$ and $s\wedge k \vDash h$;
2. $e$ *directly Hempel-disconfirms* $h$ *relative to* $k$ if and only if $e\wedge \alpha \vDash dev_{e}(\neg h)$; $e$ *Hempel-disconfirms* $h$ *relative to* $k$ if and only if, for some $s\in \bL, e\wedge k \vDash dev_{e}(s)$ and $s\wedge k \vDash \neg h$;
3. $e$ *is Hempel-neutral* for $h$ *relative to* $k$ otherwise.

One can see that in the above definition $\alpha$ includes the $e$-development of further general auxiliary hypotheses (in fact, equations as applied to specific established values, in typical examples from Glymour 1980a)[^glymour-1980a], where such hypotheses are meant to be conjoined in a single statement $k$ for convenience. This implies that the only terms occurring (non-vacuously) in $\alpha$ are individual constants already occurring (non-vacuously) in $e$. For an empty $k$ (that is, tautologous: $k = \top$), $\alpha$ must be empty too, and the original (restricted) definition of Hempelian confirmation applies. As for the proviso that $k \not\vDash h$, it rules out undesired cases of circularity—akin to so-called “macho” bootstrap confirmation, as discussed in Earman and Glymour 1988 (for more on Glymour’s theory and its implications, see Douven and Meijs 2006, and references therein)[^douven-2006].

## 2. Hypothetico-deductivism

The central idea of hypothetico-deductive (HD) confirmation can be roughly described as “deduction-in-reverse”: evidence is said to confirm a hypothesis in case the latter, while not entailed by the former, is able to entail it, with the help of suitable auxiliary hypotheses and assumptions. The basic version (sometimes labelled “naïve”) of the HD notion of confirmation can be spelled out thus:

**HD-confirmation** For any $h, e, k \in \bL$ such that $h\wedge k$ is consistent:

1. $e$ *HD-confirms* $h$ *relative to* $k$ if and only if $h\wedge k \vDash e$ and $k \not\vDash e$;
2. $e$ *HD-disconfirms* $h$ *relative to* $k$ if and only if $h\wedge k \vDash \neg e$, and $k \not\vDash \neg e$;
3. $e$ is *HD-neutral for* hypothesis $h$ *relative to* $k$ otherwise.

Note that clause (ii) above represents HD-disconfirmation as plain logical inconsistency of the target hypothesis with the data (given the auxiliaries) (see Hempel 1945, 98)[^hempel-1945].

### 2.1 HD vs. Hempelian confirmation

HD-confirmation and Hempelian confirmation convey different intuitions (see Huber 2008a for an original analysis)[^huber-2008a]. They are, in fact, distinct and strictly incompatible notions. This will be effectively illustrated by the consideration of the following conditions.

**Entailment condition** (EC) For any $h,e,k \in \bL$, if $e\wedge k$ is consistent, $e\wedge k \vDash h$ and $k \not\vDash h$, then $e$ confirms $h$ relative to $k$.

**Confirmation complementarity** (CC) For any $h, e, k \in \bL$, $e$ confirms $h$ relative to $k$ if and only if $e$ disconfirms $\neg h$ relative to $k$.

**Special consequence condition** (SCC) For any $h, e, k \in \bL$, if $e$ confirms $h$ relative to $k$ and $h\wedge k \vDash h^*$, then $e$ confirms $h^*$ relative to $k$.

On the implicit proviso that $k$ is empty (that is, tautologous: $k = \top$), Hempel (1943, 1945) himself had put forward (EC) and (SCC) as compelling adequacy conditions for any theory of confirmation, and devised his own proposal accordingly. As for (CC), he took it as a plain definitional truth (1943, 127). Moreover, Hempelian confirmation (extended) satisfies all conditions above (of course, for arguments $h$, $e$ and $k$ for which it is defined). HD-confirmation, on the contrary, violates all of them. Let us briefly discuss each one in turn.

It is rather common for a theory of ampliative (non-deductive) reasoning to retain classical logical entailment as a special case (a feature sometimes called “super-classicality”; see Strasser and Antonelli 2019)[^strasser-2019]. That’s essentially what (EC) implies for confirmation. Now given appropriate $e$, $h$ and $k$, if $e\wedge k$ entails $h$, we readily get that $e$ Hempel-confirms $h$ relative to $k$ in two simple steps. First, given that $\alpha\ = dev_{e}(k)$, $dev_{e}(e\wedge \alpha) = dev_{e}(e\wedge k)$ according to Hempel’s full definition of $dev$ (see Hempel 1943, 131)[^hempel-1943]. Then because clearly $e\wedge \alpha \vDash dev_{e}(e\wedge \alpha)$ it also follows that $e\wedge \alpha \vDash dev_{e}(e\wedge k)$, so $e\wedge k$ is (directly) Hempel-confirmed by $e$ relative to $k$ and its logical consequence $h$ is likewise confirmed (indirectly). Logical entailment is thus retained as an instance of Hempelian confirmation in a fairly straightforward way. HD-confirmation, on the contrary, does not fulfil (EC). Here is one odd example (see Sprenger 2011a, 234)[^sprenger-2011a]. With $k = \top$, just let $e$ be the observation report that object $a$ is a black swan, $swan(a) \wedge black(a)$, and $h$ be the hypothesis that black swans exist, $\exists x(swan(x) \wedge black(x))$. Evidence $e$ verifies $h$ conclusively, and yet it does not HD-confirm it, simply because $h \not\vDash e$. So the observation of a black swan turns out to be HD-neutral for the hypothesis that black swans exist! The same example shows how HD-confirmation violates (CC), too. In fact, while HD-neutral for $h$, $e$ HD-disconfirms its negation $\neg h$ that no swan is black, $\forall x(swan(x) \rightarrow \neg black(x))$, because the latter is obviously inconsistent with (refuted by) $e$.

The violation of (EC) and (CC) by HD-confirmation is arguably a reason for concern, for those conditions seem highly plausible. The special consequence condition (SCC), on the other hand, deserves separate and careful consideration. As we will see later on, (SCC) is a strong constraint, and far from sacrosanct. For now, let us point out one major philosophical motivation in its favor. (SCC) has often been invoked as a means to ensure the fulfilment of the following condition (see, e.g., Hesse 1975, 88; Horwich 1983, 57)[^hesse-1975][^horwich-1983]:

**Predictive inference condition** (PIC) For any $e, k \in \bL$, if $e$ confirms $\forall x(Fx \rightarrow Gx)$ relative to $k$, then $e$ confirms $F(a) \rightarrow G(a)$ relative to $k$.

In fact, (PIC) readily follows from (SCC) and so it is satisfied by Hempel’s theory. It says that, if evidence $e$ confirms “all $F$s are $G$s”, then it also confirms that a further object will be $G$ if it is $F$. Notably, this does not hold for HD-confirmation. Here is why. Given $k = Fa$ (i.e., the assumption that $a$ comes from the $F$ population), we have that $e = Ga$ HD-confirms $h = \forall x(Fx \rightarrow Gx)$, because the latter entails the former (given $k$). (That’s the HD reconstruction of Nicod’s insight, see below.) We also have, of course, that $h$ entails $h^* = Fb \rightarrow Gb$. And yet, contrary to (PIC), since $h^*$ does not entail $e$ (given $k$), it is not HD-confirmed by it either. The troubling conclusion is that the observation that a swan is white (or that a million of them are, for that matters) does not HD-confirm the prediction that a further swan will be found to be white.

### 2.2 Back to black (ravens)

One attractive feature of HD-confirmation is that it largely eludes the ravens paradox. As the hypothesis $h$ that all ravens are black does not entail that some generally sampled object $a$ will be a black raven, the HD view of confirmation is not committed to the eminently Hempelian implication that $e = raven(a) \wedge black(a)$ confirms $h$. Likewise, $\neg black(a) \wedge \neg raven(a)$ does not HD-confirm that all non-black objects are non-raven. The derivation of the paradox, as presented above, is thus blocked.

Indeed, HD-confirmation yields a substantially different reading of Nicod’s insight as compared to Hempel’s theory (Okasha 2011 has an important discussion of this distinction)[^okasha-2011]. Here is how it goes. *If object* $a$ *is assumed to have been taken among ravens*—so that, crucially, the auxiliary assumption $k = raven(a)$ is made—and $a$ is checked for color and found to be black, then, yes, the latter evidence, $black(a)$, HD-confirms that all ravens are black $(h)$ relative to $k$. By the same token, $\neg black(a)$ HD-disconfirms $h$ relative to the same assumption $k = raven(a)$. And, again, this is as it should be, in line with Nicod’s mention of “the absence of $G$ [here, non-black as evidence] in a case of $F$ [here, raven as an auxiliary assumption]”. It is also true that an object that is found *not* to be a raven HD-confirms $h$, but *only* relative to $k = \neg black(a)$, that is, if $a$ is assumed to have been taken among non-black objects to begin with; and this seems acceptable too (after all, while sampling from non-black objects, one might have found the counterinstance of a raven, but didn’t). Unlike Hempel’s theory, moreover, HD-confirmation does not yield the debatable implication that, by itself (that is, given $k = \top$), the observation of a non-raven $a$, $\neg raven(a)$, must confirm $h$.

Interestingly, the introduction of auxiliary hypotheses and assumptions shows that the issues surrounding Nicod’s remarks can become surprisingly subtle. Consider the following statements (Maher’s 2006 example)[^maher-2006]:

**($q_1$)**

$\forall x(white(x) \rightarrow \neg black(x))$

**($q_2$)**

$\exists x(swan(x)) \rightarrow \exists y(swan(y) \wedge black(y))$

$q_1$ simply specifies that no object is both white and black, while $q_2$ says that, if there are swans at all, then there also is some *black* swan. Also assume, again, that $e = swan(a) \wedge white(a)$. Under $q_1$ and $q_2$, the observation of a white swan clearly *dis*confirms (indeed, refutes) the hypothesis $h$ that all swans are white. Hempel’s theory (extended) faces difficulties here, because for $\alpha = dev_{e}(q_1 \wedge q_2)$ it turns out that $e\wedge \alpha$ is inconsistent. But HD-confirmation gets this case right, thus capturing appropriate boundary conditions for Nicod’s generally sensible claims. For, with $k = q_1 \wedge q_2$, one has that $h\wedge k$ is consistent and entails $\neg e$ (for it entails that no swan exists), so that $e$ HD-disconfirms (refutes) $h$ relative to $k$ (see Good 1967 for another famous counterexample to Nicod’s condition)[^good-1967].

HD-confirmation, however, is also known to suffer from distinctive “paradoxical” implications. One of the most frustrating is surely the following (see Osherson, Smith, and Shafir 1986, 206, for further specific problems).

*The irrelevant conjunction paradox*. Suppose that $e$ confirms $h$ relative to (possibly empty) $k$. Let statement $c$ be logically consistent with $e\wedge h\wedge k$, but otherwise entirely irrelevant for all of those conjuncts (perhaps belonging to a completely separate domain of inquiry). Does $e$ confirm $h\wedge c$ (relative to $k$) as it does with $h$? One would want to say no, and this implication can be suitably reconstructed in Hempel’s theory. HD-confirmation, on the contrary, can not draw this distinction: it is easy to show that, on the conditions specified, if the HD clause for confirmation is satisfied for $e$ and $h$ (given $k$), so it is for $e$ and $h\wedge c$ (given $k$). (This is simply because, if $h\wedge k \vDash e$, then $h\wedge c\wedge k \vDash e$, too, by the monotonicity of classical logical entailment.)

Kuipers (2000, 25) suggested that one can live with the irrelevant conjunction problem because, on the conditions specified, $e$ would still not HD-confirm $c$ alone (given $k$), so that HD-confirmation can be “localized”: $h$ is the only bit of the conjunction $h\wedge c$ that gets any confirmation on its own, as it were. Other authors have been reluctant to bite the bullet and have engaged in technical refinements of the “naïve” HD view. In these proposals, the spread of HD-confirmation upon frivolous conjunctions can be blocked at the expense of some additional logical machinery (see Gemes 1993, 1998; Schurz 1991, 1994)[^gemes-1993][^schurz-1991].

Finally, it should be noted that HD-confirmation offers no substantial relief from the blite paradox. On the one hand, $e = raven(a) \wedge ex_{t\le T}(a) \wedge black(a)$ does *not*, as such, HD-confirm either $h = \forall x(raven(x) \rightarrow black(x))$ or $h^* = \forall x(raven(x) \rightarrow blite(x))$, that is, for empty $k$. On the other hand, if object $a$ is assumed to have been sampled from ravens before $T$ (that is, given $k = raven(a) \wedge ex_{t\le T}(a))$, then $black(a)$ is entailed by both “all ravens are black” and “all ravens are blite” and therefore HD-confirms each of these hypotheses (and indeed, indefinitely many others: as we know, further variations of $h^*$ can be conceived at will, like the “blurple” hypothesis). One could insist that HD does handle the blite paradox after all, because $black(a)$ (given $k$ as above) does not HD-confirms that a raven will be white if examined after $T$ (Kuipers 2000, 29 ff.)[^kuipers-2000]. Unfortunately (as pointed out by Schurz 2005, 148)[^schurz-2005] $black(a)$ does not HD-confirm that a raven will be black if examined after $T$ either (again, given $k$ as above). That’s because, as already pointed out, HD-confirmation fails the predictive inference condition (PIC) in general. So, all in all, HD-confirmation can not tell black from blite any more than Hempel-confirmation can.

### 2.3 Underdetermination and the Duhemian challenge

The issues above look contrived and artificial to some people’s taste—even among philosophers. Many have suggested a closer look at real-world inferential practices in the sciences as a more appropriate benchmark for assessment. For one thing, the very idea of hypothetico-deductivism has often been said to stem from the origins of Western science. As reported by Simplicius of Cilicia (sixth century A.D.) in his commentary on Aristotle’s *De Caelo*, Plato had challenged his pupils to identify combinations of “ordered” motions by which one could account for (namely, deduce) the planets’ wandering trajectories across the heavens as observed by the Earth. As a matter of historical fact, mathematical astronomy (the first mature empirical science) has engaged in just this task for centuries: scholars have been trying to define geometrical models from which the apparent motion of celestial bodies would derive.

It is fair to say that, at its roots, the kind of challenges that the HD framework faces with scientific reasoning is not so different from the main puzzles that arise from philosophical considerations of a more formal kind. Still, the two areas turn out to be complementary in important ways. The following statement will serve as a useful starting point to extend the scope of our discussion.

**Underdetermination Theorem (UT) for “naïve” HD-confirmation** For any contingent $h, e \in \bL$, if $h$ and $e$ are logically consistent, there exists some $k \in \bL$ such that $e$ HD-confirms $h$ relative to $k$.

(UT) is an elementary logical fact that has been long recognized (see, e.g., Glymour 1980a, 36)[^glymour-1980a]. In purely formal terms, just positing $k = h \rightarrow e$ will do for a proof. To appreciate how (UT) can spark any philosophical interest, one has to combine it with some insightful remarks first put forward by Pierre Duhem (1906) and then famously revived by Quine (1951) in a more radical style. (Indeed, (UT) essentially amounts to the “entailment version” of “Quinean underdetermination” in Laudan 1990, 274.)

Duhem (he himself a supporter of the HD view) pointed out that in mature sciences such as physics most hypotheses or theories of real interest can not be contradicted by any statement describing observable states of affairs. Taken in isolation, they simply do not logically imply, nor rule out, any observable fact, essentially because (unlike “all ravens are black”) they concern unobservable entities and processes. So, in effect, Duhem emphasized that, typically, scientific hypotheses or theories *are* logically consistent with any piece of checkable evidence. Unless, of course, the logical connection is underpinned by auxiliary hypotheses and assumptions suitably bridging the gap between the observational and non-observational vocabulary, as it were. But then, once auxiliaries are in play, logic alone guarantees that *some* $k$ exists such that $h\wedge k$ is consistent, $h\wedge k \vDash e$, and $k \not\vDash e$, so that confirmation holds in naïve HD terms (that’s just the UT result above). Apparently, when Duhem’s point applies, the uncritical supporter of whatever hypothesis $h$ can legitimately claim (naïve HD) confirmation from any $e$ by simply shaping $k$ conveniently. In this sense, hypothesis assessment would be radically “underdetermined” by any amount of evidence practically available.

Influential authors such as Thomas Kuhn (1962/1970) (but see Laudan 1990, 268, for a more extensive survey)[^laudan-1990] relied on Duhemian insights to suggest that confirmation by empirical evidence is too weak a force to drive the evaluation of theories in science, often inviting conclusions of a relativistic flavor (see Worrall 1996 for an illuminating reconstruction along these lines)[^worrall-1996]. Let us briefly consider a classic case, which Duhem himself thoroughly analyzed: the wave *vs*. particle theories of light in modern optics. Across the decades, wave theorists were able to deduce an impressive list of important empirical facts from their main hypothesis along with appropriate auxiliaries, diffraction phenomena being only one major example. But many particle theorists’ reaction was to retain *their* hypothesis nonetheless and to reshape other parts of the “theoretical maze” (i.e., $k$; the term is Popper’s, 1963, p. 330) to recover those observed facts as consequences of their own proposal. And as we’ve seen, *if* the bare logic of naïve HD was to be taken strictly, surely they *could* have claimed their overall hypothesis to be confirmed too, just as much as their opponents.

Importantly, they didn’t. In fact, it was quite clear that particle theorists, unlike their wave-theory opponents, were striving to remedy weaknesses rather than scoring successes (see Worrall 1990)[^worrall-1990]. But why, then? Because, as Duhem himself clearly realized, the logic of naïve HD “is not the only rule for our judgments” (1906, 217). The lesson of (UT) and the Duhemian insight is not quite, it seems, that naïve HD is the last word and scientific inference is unconstrained by stringent rational principles, but rather that the HD view has to be strengthened in order to capture the real nature of evidential support in rational scientific inference. At least, that’s the position of a good deal of philosophers of science working within the HD framework broadly construed. It has even been maintained that “no serious twentieth-century methodologist” has ever subscribed to the naïve HD view above “without crucial qualifications” (Laudan 1990, 278; also see Laudan and Leplin 1991, 466)[^laudan-1990][^laudan-1991].

So the HD approach to confirmation has yielded a number of more articulated variants to meet the challenge of underdetermination. Following (loosely) Norton (2005), we will now survey an instructive sample of them.

### 2.4 The extended HD menu

Naïve HD can be enriched by a resolute form of *predictivism*. According to this approach, the naïve HD clause for confirmation is too weak because $e$ must have been predicted in advance from $h\wedge k$. Karl Popper’s (1934/1959) account of the “corroboration” of hypotheses famously embedded this view, but squarely predictivist stances can be traced back to early modern thinkers like Christiaan Huygens (1629–1695) and Gottfried Wilhelm Leibniz (1646–1716), and in Duhem’s work itself. The predictivist sets a high bar for confirmation. Her favorite examples typically include stunning episodes in which the existence of previously unknown objects, phenomena, or whole classes of them is anticipated: the phases of Venus for Copernican astronomy or the discovery of Neptune for Newtonian physics, all the way up to the Higgs boson for so-called standard model of subatomic particles.

The predictivist solution to the underdetermination problem is fairly radical: many of the relevant factual consequences of $h\wedge k$ will be already known when this theory is articulated, and so unfit for confirmation. Critics have objected that predictivism is in fact far too restrictive. There seem to be many cases in which already known phenomena clearly do provide support to a new hypothesis or theory. Zahar (1973) first raised this problem of “old evidence”, then made famous by Glymour (1980a, 85 ff.) as a difficulty for Bayesianism (see Section 3 below). Examples of this kind abound in the history of science as elsewhere, but the textbook illustration has become the precession of Mercury’s perihelion, a lasting anomaly for Newtonian physics: Einstein’s general relativity calculations got this long-known fact right, thereby gaining a remarkable piece of initial support for the new theory. In addition to this problem with old evidence, HD predictivism also seems to lack a principled rationale. After all, the temporal order of the discovery of $e$ and of the articulation of $h$ and $k$ may well be an entirely accidental historical contingency. Why should it bear on the confirmation relationship among them? (See Giere 1983 and Musgrave 1974 for classic discussions of these issues. Douglas and Magnus 2013 and Barnes 2018 offer more recent views and rich lists of further references.)[^barnes-2018][^douglas-2013][^giere-1983][^musgrave-1974]

As a possible response to the difficulties above, naïve HD can be enriched by the *use-novelty* criterion (UN) instead. The UN reaction to the underdetermination problem is more conservative than the temporal predictivist strategy. According to this view, to improve on the weak naïve HD clause for confirmation one only has to rule out one particular class of cases, i.e., those in which the description of a known fact, $e$, served as a constraint in the construction of $h\wedge k$. The UN view thus comes equipped with a rationale. If $h\wedge k$ was shaped on the basis of $e$, UN advocates point out, then it was bound to get that state of affairs right; the theory never ran any risk of failure, thus did not achieve any particularly significant success either. Precisely in these cases, and just for this reason, the evidence $e$ must not be double-counted: by using it for the construction of the theory, its confirmational power becomes “dried out”, so to speak.

The UN completion of naïve HD originated from Lakatos and some of his collaborators (see Lakatos and Zahar 1975 and Worrall 1978; also see Giere 1979, 161–162, and Gillies 1989 for similar views)[^giere-1979][^gillies-1989][^lakatos-1975][^worrall-1978], although important hints in the same direction can be found at least in the work of William Whewell (1840/1847). Consider the touchstone example of Mercury again. According to Zahar (1973), Einstein did not need to rely on the Mercury data to define theory and auxiliaries as to match observationally correct values for the perihelion precession (also see Norton 2011a; and Earman and Janssen 1993 for a very detailed, and more nuanced, account)[^earman-1993][^norton-2011a]. Being already known, the fact was not of course predicted in a strictly temporal sense, and yet, on Zahar’s reading, it *could have been*: it was “use-novel” and thus fresh for use to confirm the theory (see Crupi 2025 for a possible refinement and an application to the Copernican revolution)[^crupi-2025]. For a more mundane illustration, so-called *cross-validation* techniques represent a routine application of the UN idea in statistical settings (as pointed out by Schurz 2014, 92; also see Forster 2007, 592 ff.)[^forster-2007][^schurz-2014]. According to some commentators, however, the UN criterion needs further elaboration (see Hitchcock and Sober 2004 and Lipton 2005)[^hitchcock-2004][^lipton-2005], while others have criticized it as essentially wrong-headed (see Howson 1990 and Mayo 1991, 2014; also see Votsis 2014)[^howson-1990][^howson-1991][^mayo-1991][^votsis-2014].

Yet another way to enrich naïve HD is to combine it with *eliminativism*. According to this view, the naïve HD clause for confirmation is too weak because there must have been a low (enough) objective chance of getting the outcome $e$ (favorable to $h$) if $h$ was false, so that few possibilities exist that $e$ may have occurred for some reason other than the truth of $h$. Briefly put, the occurrence of $e$ must be such that most alternatives to $h$ can be safely ruled out. The founding figure of eliminativism is Francis Bacon (1561–1626). John Stuart Mill (1843/1872) is a major representative in later times, and Deborah Mayo’s “error-statistical” approach to hypothesis testing arguably develops this tradition (Mayo 1996 and Mayo and Spanos 2010; see Bird 2010, Kitcher 1993, 219 ff., and Meehl 1990 for other contemporary variations)[^bird-2010][^kitcher-1993][^mayo-1996][^mayo-2010][^mayo-2010-2][^meehl-1990].

Eliminativism is most credible when experimentation is at issue (see, e.g., Guala 2012)[^guala-2012]. Indeed, the appeal to Bacon’s idea of *crucial experiment* (*instantia crucis*) and related notions (e.g., “severe testing”) is a fairly reliable mark of eliminativist inclinations. Experimentation is, to a large extent, precisely an array of techniques to keep undesired interfering factors at a minimum by active manipulation and deliberate control (think of the blinding procedure in medical trials, with $h$ the hypothesized effectiveness of a novel treatment and $e$ a relative improvement in clinical endpoints for a target subsample of patients thus treated). When this kind of control obtains, popular statistical tools are supposed to allow for the calculation of the probability of $e$ in case $h$ is false meant as a “relative frequency in a (real or hypothetical) series of test applications” (Mayo 1991, 529)[^mayo-1991], and to secure a sufficiently low value to validate the positive outcome of the test. It is much less clear how firm a grip this approach can retain when inference takes place at higher levels of generality and theoretical commitment, where the hypothesis space is typically much too poorly ordered to fit routine error-statistical analyses. Indeed, Laudan (1997, 315; also see Musgrave 2010)[^musgrave-2010] spotted in this approach the risk of a “balkanization” of scientific reasoning, namely, a restricted focus on scattered pieces of experimental inference (but see Mayo 2010 for a defense)[^mayo-2010][^mayo-2010-2].

Naïve HD can also be enriched by the notion of *simplicity*. According to this view, the naïve HD clause for confirmation is too weak because $h\wedge k$ must be a simple (enough), unified way to account for evidence $e$. A classic reference for the simplicity view is Newton’s first law of philosophizing in the *Principia* (“admit no more causes of natural things than such as are both true and sufficient to explain their appearances”), echoing very closely Ockham’s razor. This basic idea has never lost its appeal—even up to recent times (see, e.g., Quine and Ullian 1970, 69 ff.; Sober 1975; Zellner, Keuzenkamp, and McAleer 2002; Scorzato 2013)[^quine-1970][^quine-1970-2][^scorzato-2013][^sober-1975].

Despite Thomas Kuhn’s (1957, 181) suggestions to the contrary, the success of Copernican astronomy over Ptolemy’s system has remained an influential case study fostering the simplicity view (Martens 2009)[^martens-2009]. Moreover, in ordinary scientific problems such as *curve fitting*, formal criteria of model selection are applied where the paucity of parameters can be interpreted naturally as a key dimension of simplicity (Forster and Sober 1994)[^forster-1994][^sober-1994]. Traditionally, two main problems have proven pressing, and frustrating, for the simplicity approach. First, how to provide a sufficiently coherent and illuminating explication of this multifaceted and elusive notion (see Riesch 2010)[^riesch-2010]; and second, how to justify the role of simplicity as a properly *epistemic* (rather than merely *pragmatic*) virtue (see Kelly 2007, 2008)[^kelly-2007].

Finally, naïve HD can be enriched by the appeal to *explanation*. Here, the naïve HD clause for confirmation is meant to be too weak because $h\wedge k$ must be able (not only to entail, but) to explain $e$. By this move, the HD approach embeds the slogan of the so-called *inference to the best explanation* view: “observations support the hypothesis precisely because it would explain them” (Lipton 2000, 185; also see Lipton 2004)[^lipton-2000][^lipton-2004]. Historically, the main source for this connection between explanation and support is found in the work of Charles Sanders Peirce (1839–1914). Janssen (2003) offers a particularly neat contemporary exhibit, explicitly aimed at “curing cases of the Duhem-Quine disease” (484; also see Thagard 1978, and Douven 2017 for a relevant survey)[^douven-2017][^thagard-1978]. Quite unlike eliminativist approaches, explanationist analyses tend to focus on large-scale theories and relatively high-level kinds of evidence. Dealing with Einstein’s general relativity, for instance, Janssen (2003) greatly emphasizes its explanation of the equivalence of inertial and gravitational mass (essentially a brute fact in Newtonian physics) over the resolution of the puzzle of Mercury’s perihelion. Explanationist accounts are also distinctively well-equipped to address inference patterns from non-experimental sciences (Cleland 2011)[^cleland-2011].

The problems faced by these approaches are similar to those affecting the simplicity view. Agreement is still lacking on the nature of scientific explanation (see Woodward 2019)[^woodward-2019] and it is not clear how far an explanationist variant of HD can go without a sound analysis of that notion (Prasetya 2024)[^prasetya-2024]. Moreover, critics have wondered why the relationship of confirmation should be affected by an explanatory connection with the evidence *per se* (see Salmon 2001)[^salmon-2001].

The above discussion does not display an exhaustive list (nor are the listed options mutually exclusive, for that matter: see, e.g., Baker 2003; also see Worrall 2010 for some overlapping implications in an applied setting of real practical value)[^baker-2003][^worrall-2010]. And our sketched presentation hardly allows for any conclusive assessment. It does suggest, however, that reports of the death of hypothetico-deductivism (see Earman 1992, 64, and Glymour 1980b)[^earman-1992][^earman-1992-2][^glymour-1980b] might have been exaggerated. For all its difficulties, HD has proven fairly resilient at least as a basic framework to elucidate some key aspects of how hypotheses can be confirmed by the evidence (see Betz 2013, Gemes 2005, and Sprenger 2011b for consonant points of view)[^betz-2013][^gemes-2005][^sprenger-2011b].

## 3. Bayesian confirmation theories

*Bayes’s theorem* is a very central element of the probability calculus (see Joyce 2019)[^joyce-2019]. For historical reasons, *Bayesian* has become a standard label to allude to a range of approaches and positions sharing the common idea that probability (in its modern, mathematical sense) plays a crucial role in rational belief, inference, and behavior. According to Bayesian epistemologists and philosophers of science, (i) rational agents have credences differing in strength, which moreover (ii) satisfy the probability axioms, and can thus be represented in probabilistic form. (In non-Bayesian models (ii) is rejected, but (i) may well be retained: see Huber and Schmidt-Petri 2009, Levi 2008, and Spohn 2012.) Well-known arguments exist in favor of this position (see, e.g., Easwaran 2011a; Pettigrew 2016; Skyrms 1987; Vineberg 2016)[^easwaran-2011a][^pettigrew-2016][^skyrms-1987][^vineberg-2016], although there is no lack of difficulties and criticism (see, e.g., Easwaran 2011b; Hájek 2008; Kelly and Glymour 2004; Norton 2011b)[^easwaran-2011b][^hájek-2008][^hájek-2008-2][^kelly-2004][^norton-2011b].

Beyond the core ideas above, however, the theoretical landscape of Bayesianism is quite as hopelessly diverse as it is fertile. Surveys and state of art presentations are already numerous, and ostensibly growing (see, e.g., Good 1971; Joyce 2011; Oaksford and Chater 2007; Sprenger and Hartmann 2020; Weisberg 2015)[^good-1971][^joyce-2011][^oaksford-2007][^weisberg-2015]. For the present purposes, attention can be restricted to a classification that is still fairly coarse-grained, and based on just two dimensions or criteria.

First, there is an important distinction between *permissivism* and *impermissivism* (see Meacham 2014 and Kopec and Titelbaum 2016 for this terminology)[^kopec-2016][^meacham-2014]. For permissive Bayesians (sometimes otherwise labelled “subjectivists”), accordance with the probability axioms is the only clear-cut constraint on the credences of a rational agent. In impermissive forms of Bayesianism (often otherwise called “objective”), further constraints are put forward that significantly restrict the range of rational credences, possibly up to one single “right” probability function in any given setting. Second, there are different attitudes towards so-called principle of *total evidence* (TE) for the probabilities on which a reasoner relies. TE Bayesians maintain that the relevant credences should be represented by a probability function $P$ which conveys the totality of what is known to the agent. For non-TE approaches, depending on the circumstances, $P$ may (or should) be set up so that portions of the evidence available are in fact bracketed. (Unsurprisingly, further subtleties arise as soon as one delves a bit further into the precise meaning and scope of TE; see Fitelson 2008 and Williamson 2002, Chs. 9–10, for important discussions.)[^fitelson-2002][^fitelson-2008][^williamson-2002]

Of course, many intermediate positions exist between extreme forms of permissivism and impermissivism so outlined, and more or less the same applies for the TE issue. The above distinctions are surely rough enough, but useful nonetheless. Impermissive TE Bayesianism has served as a received view in early Bayesian philosophy of science (e.g., Carnap 1950/1962)[^carnap-1950]. But impermissivism is easily found in combination with non-TE positions, too (see, e.g., Maher 1996)[^maher-1996]. TE permissivism seems a good approximation of De Finetti’s (2008) stance, while non-TE permissivism is arguably close to a standard view nowadays (see, e.g., Howson and Urbach 2006)[^howson-2006]. No more than this will be needed to begin our exploration of Bayesian confirmation theories.

### 3.1 Probabilistic confirmation as *firmness*

Let us consider a set $\bP$ of probability functions representing possible states of belief about a domain that is described in a finite language $L$ with $\bL$ the set of its closed sentences. From now on, unless otherwise specified, whenever considering some $h, e, k \in \bL$ and $P \in \bP$, we will invariably rely on the following provisos:

1. both $e\wedge k$ and $h\wedge k$ are consistent;
2. $P(e\wedge k), P(h\wedge k) \gt 0;$
3. $P(k) \gt P(h\wedge k)$ (unless $k \vDash h$);
4. $P(e\wedge k) \gt P(e\wedge h\wedge k)$ (unless $e\wedge k \vDash h$); and
5. $P(e\wedge h\wedge k) \gt 0$, as long as $e\wedge h\wedge k$ is consistent.

(These assumptions are convenient and critical for technical reasons, but not entirely innocent. Festa 1999 and Kuipers 2000, 44 ff., discuss some limiting cases that are left aside here owing to these constraints.)[^festa-1999][^kuipers-2000]

A probabilistic theory of confirmation can be spelled out through the definition of a function $C_{P}(h, e\mid k): \{\bL^3 \times \bP\} \rightarrow \Re$ representing the degree of confirmation that hypothesis $h$ receives from evidence $e$ relative to $k$ and probability function $P$. $C_{P}(h,e\mid k)$ will then have relevant probabilities as its building blocks, according to the following basic postulate of probabilistic confirmation:

**(P0) Formality** There exists a function $g$ such that, for any $h, e, k \in \bL$ and any $P \in \bP$, $C_{P}(h,e\mid k) = g[P(h\wedge e\mid k),P(h\mid k),P(e\mid k)]$.

Note that the probability distribution over the algebra generated by $h$ and $e$, conditional on $k$, is entirely determined by $P(h\wedge e\mid k)$, $P(h\mid k)$ and $P(e\mid k)$. Hence, (P0) simply states that $C_{P}(h, e\mid k)$ depends on that distribution, and nothing else. (The label for this assumption is taken from Tentori, Crupi, and Osherson 2007, 2010.)

Hempelian and HD confirmation, as discussed above, are *qualitative* theories of confirmation. They only tell us *whether* evidence $e$ confirms (disconfirms) hypothesis $h$ given $k$. However, assessments of the *amount* of support that some evidence brings to a hypothesis are commonly involved in scientific reasoning, as well as in other domains, if only in the form of *comparative* judgments such as “hypothesis $h$ is more strongly confirmed by $e_{1}$ than by $e_{2}$” or “$e$ confirms $h_{1}$ to a greater extent than $h_{2}$”. Consider, for instance, the following principle, a veritable cornerstone of probabilistic confirmation in all of its variations (see Crupi, Chater, and Tentori 2013 for a list of references):

**(P1) Final probability** For any $h,e_{1},e_{2},k \in \bL$ and any $P \in \bP$, $C_{P}(h,e_{1}\mid k) \gtreqless C_{P}(h, e_{2}\mid k)$ if and only if $P(h\mid e_{1} \wedge k) \gtreqless P(h\mid e_{2} \wedge k).$

(P1) is itself a comparative, or *ordinal*, principle, stating that, for any fixed hypothesis $h$, the final (or posterior) probability and confirmation always move in the same direction in the light of data, $e$ (given $k$). Interestingly, (P0) and (P1) are already sufficient to single out one traditional class of measures of probabilistic confirmation, if conjoined with the following (see Crupi and Tentori 2016, 656, Schippers 2017, and also Törnebohm 1966, 81)[^crupi-2016][^schippers-2017][^törnebohm-1966]:

**(P2) Local equivalence** For any $h_{1},h_{2},e,k \in \bL$ and any $P\in \bP$, if $h_{1}$ and $h_{2}$ are logically equivalent given $e$ and $k$, then $C_{P}(h_{1},e\mid k) = C_{P}(h_{2}, e\mid k).$

The following can then be shown:

**Theorem 1** (P0), (P1) and (P2) hold if and only if there exists a strictly increasing function $f$ such that, for any $h, e, k \in \bL$ and any $P \in \bP$, $C_{P}(h, e\mid k) = f[P(h\mid e\wedge k)]$.

Theorem 1 provides a simple axiomatic characterization of the class of confirmation functions that are strictly increasing with the final probability of the hypothesis given the evidence (and $k$) (proven in Schippers 2017)[^schippers-2017]. All the functions in this class are *ordinally equivalent*, meaning that they imply the same rank order of $C_{P}(h, e\mid k)$ and $C_{P^*}(h^*,e^*\mid k^*)$ for any $h, h^*,e, e^*,k, k^* \in \bL$ and any $P, P^* \in \bP.$

By (P0), (P1) and (P2), we thus have $C_{P}(h, e\mid k) = f[P(h\mid e \wedge k)]$, implying that the more likely $h$ is given the evidence the more it is confirmed. This approach explicates confirmation precisely as the *overall credibility* of a hypothesis (*firmness* is Carnap’s 1950/1962 telling term, xvi)[^carnap-1950]. In this view, “Bayesian confirmation theory is little more than the examination of [the] properties” of the posterior probability function (Howson 2000, 179)[^howson-2000].

As we will see, the ordinal level of analysis is a solid and convenient middle ground between a purely qualitative and a thoroughly quantitative (metric) notion of confirmation. To begin with, ordinal notions are in general sufficient to move “upwards” to the qualitative level as follows:

**Qualitative confirmation from ordinal relations** (QC) For any $h, e, k \in \bL$ and any $P \in \bP$:

- $e$ $C_{P}$-*confirms* $h$ *relative to* $k$ if and only if $C_{P}(h, e\mid k) \gt C_{P}(\neg h, e\mid k);$
- $e$ $C_{P}$-*disconfirms* $h$ *relative to* $k$ if and only if $C_{P}(h, e\mid k) \lt C_{P}(\neg h, e\mid k);$
- $e$ is $C_{P}$-*neutral for* $h$ *relative to* $k$ if and only if $C_{P}(h, e\mid k) = C_{P}(\neg h, e\mid k).$

Given Theorem 1, (P0), (P1) and (P2) can be combined with the definitions in (QC) to derive the following qualitative notion of probabilistic confirmation as firmness:

**Confirmation as firmness ($F$-confirmation, qualitative)** For any $h, e, k \in \bL$ and any $P \in \bP$:

- $e$ $F$-*confirms* $h$ *relative to* $k$ if and only if $P(h\mid e \wedge k) \gt \bfrac{1}{2};$
- $e$ $F$-*disconfirms* $h$ *relative to* $k$ if and only if $P(h\mid e \wedge k) \lt \bfrac{1}{2};$
- $e$ *is* $F$-*neutral for* $h$ *relative to* $k$ if and only if $P(h\mid e \wedge k) = \bfrac{1}{2}.$

The point of qualitative $F$-confirmation is thus straightforward: $h$ is said to be (dis)confirmed by $e$ (given $k$) if it is more likely than not to be true (false). (Sometimes a threshold higher than a probability $\bfrac{1}{2}$ is identified, but this complication would add little for our present purposes.)

The ordinal notion of confirmation is of high theoretical significance because ordinal divergences, unlike purely quantitative differences, imply opposite comparative judgments for some evidence-hypothesis pairs. A refinement from the ordinal to a properly quantitative level is also be of interest, however, and much useful for tractability and applications. For example, one can have 0 as a convenient neutrality threshold for confirmation as firmness, provided that the following functional representation is adopted (see Peirce 1878 for an early occurrence)[^peirce-1878]:

\begin{align} F(h,e\mid k) & = \log\left[\frac{P(h\mid e \wedge k)}{P(\neg h\mid e \wedge k)}\right] \\ & = \log Odds(h\mid e \wedge k) \end{align}

(The base of the logarithm can be chosen at convenience, as long as it is strictly greater than 1.)

A quantitative requirement that is often put forward is the following stringent form of additivity:

**Strict additivity** (SA) For any $h, e_{1},e_{2},k \in \bL$ and any $P \in \bP$, $\ \ \ C_{P}(h, e_{1} \wedge e_{2}\mid k) = C_{P}(h, e_{1}\mid k) + C_{P}(h, e_{2}\mid e_{1} \wedge k).$

Although extraneous to $F$-confirmation, Strict Additivity will prove of use later on for the discussion of further variants of Bayesian confirmation theory.

### 3.2 Strengths and infirmities of firmness

Confirmation as firmness shares a number of structural properties with Hempelian confirmation. It satisfies the Special Consequence Condition, thus the Predictive Inference Condition too. It satisfies the Entailment Condition and, in virtue of (P1), extends it smoothly to the following ordinal counterpart:

**Entailment condition (ordinal extension)** (EC-Ord) For any $h, e_{1},e_{2},k\in \bL$ such that $k \not\vDash h$ and any $P \in \bP$ :

1. if, $e_{1}\wedge k \vDash h$ and $e_{2}\wedge k \not\vDash h$, then $h$ is more confirmed by $e_{1}$ than by $e_{2}$ relative to $k$, that is, $C_{P}(h, e_{1}\mid k) \gt C_{P}(h, e_{2}\mid k);$
2. if, $e_{1}\wedge k\vDash h$ and $e_{2}\wedge k\vDash h,$ then $h$ is equally confirmed by $e_{1}$ and by $e_{2}$ relative to $k$, that is, $C_{P}(h, e_{1}\mid k) = C_{P}(h, e_{2}\mid k).$

According to (EC-Ord) not only is classical entailment retained as a case of confirmation, it also represents a limiting case: it is the strongest possible form of confirmation that a fixed hypothesis $h$ can receive.

$F$-confirmation also satisfies Confirmation Complementarity and, moreover, extends it to its appealing ordinal counterpart (see Crupi, Festa, and Buttasi 2010, 85–86), that is:

**Confirmation complementarity (ordinal extension)** (CC-Ord) $C_{P}(\neg h, e\mid k)$ is a strictly decreasing function of $C_{P}(h, e\mid k)$, that is, for any $h, h^*,e, e^*,k \in \bL$ and any $P\in \bP,$ $C_{P}(h, e\mid k)\gtreqless C_{P}(h^*,e^*\mid k)$ if and only if $C_{P}(\neg h, e\mid k) \lesseqgtr C_{P}(\neg h^*,e^*\mid k).$

(CC-Ord) neatly reflects Keynes’ (1921, 80) remark that “an argument is always as near to proving or disproving a proposition, as it is to disproving or proving its contradictory”. Indeed, quantitatively, the measure $F(h, e\mid k)$ instantiates Confirmation Complementarity in a simple and elegant way, that is, it satisfies $C_{P}(h, e\mid k) = -C_{P}(\neg h, e\mid k).$

$F$-confirmation also implies another attractive quantitative result, alleviating the ailments of the irrelevant conjunction paradox. In the statement below, indicating this result, the *irrelevance* of $c$ for hypothesis $h$ and evidence $e$ (relative to $k$) is meant to amount to the probabilistic independence of $c$ from $h, e$ and their conjunction (given $k$), that is, to $P(h \wedge c\mid k) = P(h\mid k)P(c\mid k),$ $P(e \wedge c\mid k) = P(e\mid k)P(c\mid k)$, and $P(h \wedge e \wedge c\mid k) = P(h \wedge e\mid k)P(c\mid k)$, respectively.

**Confirmation upon irrelevant conjunction (ordinal solution)** (CIC) For any $h, e, c, k \in \bL$ and any $P \in \bP,$ if $e$ confirms $h$ relative to $k$ and $c$ is irrelevant for $h$ and $e$ relative to $k$, then $\ \ \ C_{P}(h, e\mid k) \gt C_{P}(h \wedge c, e\mid k).$

So, even in case it is qualitatively preserved across the tacking of $c$ onto $h$, the positive confirmation afforded by $e$ is at least bound to quantitatively *decrease* thereby.

Partly because of appealing formal features such as those mentioned so far, there is a long list of distinguished scholars advocating the firmness view of confirmation, from Keynes (1921) and Hosiasson-Lindenbaum (1940) onwards, most often coupled with some form of impermissive Bayesianism (see Hawthorne 2011 and Williamson 2011 for contemporary variations)[^hawthorne-2011][^williamson-2011]. In fact, $F$-confirmation fits most neatly a classical form of TE impermissivism *à la* Carnap, where one assumes that $k = \top,$ that $P$ is an “objective” initial probability based on essentially logical considerations, and that all the non-logical information available is collected in $e$. The spirit of the Carnapian project never lost its appeal entirely (see, e.g., Festa 2003, Franklin 2001, Maher 2010, Paris 2011)[^festa-2003][^franklin-2001][^maher-2010][^paris-2011]. However, the idea of a “logical” interpretation of $P$ got stuck into difficulties that are often seen as insurmountable (e.g., Earman and Salmon 1992, 85–89; Gillies 2000, Ch. 3; Hájek 2019; Howson and Urbach 2006, 59–72; van Fraassen 1989, Ch. 12; Zabell 2011)[^earman-1992][^earman-1992-2][^gillies-2000][^hájek-2019][^howson-2006][^fraassen-1989][^zabell-2011]. And arguably, lacking some robust and effective impermissivist policy, the account of confirmation as firmness ends up loosing much of its philosophical momentum. The issues surrounding the ravens and blite paradoxes provide a useful illustration.

Consider again $h = \forall x(raven(x) \rightarrow black(x))$, and the main analyses of “the observation that $a$ is a black raven” encountered so far, that is:

1. $k = \top$ and $e = raven(a) \wedge black(a)$, and
2. $k = raven(a)$ and $e = black(a).$

In both cases, whether $e$ $F$-confirms $h$ or not (relative to $k$) critically depends on $P$: if the prior $P(h\mid k)$ is low enough, $e$ won’t do no matter what under either (i) or (ii); and if it is high enough, $h$ will be $F$-confirmed either way. As a consequence, the $F$-confirmation view, by itself, does not offer any definite hint as to when, how, and why Nicod’s remarks apply or not.

For the purposes of our discussion, the following condition reveals another debatable aspect of the firmness explication of confirmation.

**Consistency condition** (Cons) For any $h, h^*,e, k \in \bL$ and any $P \in \bP$, if $k \vDash \neg(h\wedge h^*)$ then $e$ confirms $h$ given $k$ if and only if $e$ disconfirms $h^*$ given $k$.

(Cons) says that evidence $e$ can never confirm incompatible hypotheses. But consider, by way of illustration, a clinical case of an infectious disease of unknown origin, and suppose that $e$ is the failure of antibiotic treatment. Arguably, there is nothing wrong in saying that, by discrediting bacteria as possible causes, the evidence confirms (viz. provides some support for) any of a number of alternative viral diagnoses. This judgment clashes with (Cons), though, which then seems an overly strong constraint.

Notably, (Cons) was defended by Hempel (1945) and, in fact, one can show that it follows from the conjunction of (qualitative) Confirmation Complementary and the Special Consequence Condition, and so from both Hempelian and $F$-confirmation. This is but one sign of how stringent the Special Consequence Condition is. Mainly because of the latter, both the Hempelian and the firmness views of confirmation must depart from the plausible HD idea that hypotheses are generally confirmed by their verified consequences (see Hempel 1945, 103–104)[^hempel-1945]. We will come back to this while discussing our next topic: a very different Bayesian explication of confirmation, based on the notion of probabilistic *relevance*.

### 3.3 Probabilistic relevance confirmation

We’ve seen that the firmness notion of probabilistic confirmation can be singled out through one ordinal constraint, (P2), in addition to the fundamental principles (P0)–(P1). The counterpart condition for the so-called *relevance* notion of probabilistic confirmation is the following:

**(P3) Tautological evidence** For any $h_{1},h_{2},k\in \bL$ and any $P\in \bP$, $C_{P}(h_{1},\top \mid k) = C_{P}(h_{2},\top \mid k).$

(P3) implies that any hypothesis is equally “confirmed” by empty evidence. We will say that $C_{P}(h, e\mid k)$ represents the probabilistic relevance notion of confirmation, or relevance-confirmation, if and only if it satisfies (P0), (P1) and (P3). These conditions are sufficient to derive the following, purely qualitative principle, according to the definitional method in (QC) above (see Crupi and Tentori 2014, 82, and Crupi 2015)[^crupi-2015][^crupi-2014].

**Probabilistic relevance confirmation (qualitative)** For any $h, e, k \in \bL$ and any $P\in \bP:$

- $e$ *relevance-confirms* $h$ *relative to* $k$ if and only if $P(h\mid e \wedge k)\gt P(h\mid k);$
- $e$ *relevance-disconfirms* $h$ *relative to* $k$ if and only if $P(h\mid e \wedge k)\lt P(h\mid k);$
- $e$ *is relevance-neutral for* $h$ *relative to* $k$ if and only if $P(h\mid e \wedge k) = P(h\mid k).$

The point of relevance confirmation is that the credibility of a hypothesis can be *changed* in either a positive (confirmation in a strict sense) or negative way (disconfirmation) by the evidence concerned (given $k$). Confirmation (in the strict sense) thus reflects an increase from initial to final probability, whereas disconfirmation reflects a decrease (see Achinstein 2005 for some diverging views on this very idea)[^achinstein-2005].

The qualitative notions of confirmation as firmness and as relevance are demonstrably distinct. Unlike firmness, relevance confirmation can not be formalized by the final probability alone, or any increasing function thereof. To illustrate, the probability of an otherwise very rare disease $(h)$ can be quite low even after a relevant positive test result $(e)$; yet $h$ is relevance-confirmed by $e$ to the extent that its probability rises thereby. By the same token, the probability of the absence of the disease $(\neg h)$ can be quite high despite the positive test result $(e)$, yet $\neg h$ is relevance-disconfirmed by $e$ to the extent that its probability decreases thereby. Perhaps surprisingly, the distinction between firmness and relevance confirmation—“extremely fundamental” and yet “sometimes unnoticed”, as Salmon (1969, 48–49) put it—had to be stressed time and again to achieve theoretical clarity in philosophy (e.g., Popper 1954; Peijnenburg 2012)[^peijnenburg-2012][^popper-1954] as well as in other domains concerned, such as artificial intelligence and the psychology of reasoning (see Horvitz and Heckerman 1986; Crupi, Fitelson, and Tentori 2008; Shogenji 2012)[^horvitz-1986][^shogenji-2012].

The qualitative notion of relevance confirmation already has some interesting consequences. It implies, for instance, the following remarkable fact:

**Complementary Evidence** (CompE) For any $h, e, k\in \bL$ and any $P\in \bP,$ $e$ confirms $h$ relative to $k$ if and only if $\neg e$ disconfirms $h$ relative to $k.$

The importance of (CompE) can be illustrated as follows. Consider the case of a father suspected of abusing his child. Suppose that the child does claim that s/he has been abused (label this evidence $e$). A forensic psychiatrist, when consulted, declares that this confirms guilt $(h)$. Alternatively, suppose that the child is asked and does *not* report having been abused $(\neg e).$ As pointed out by Dawes (2001), it may well happen that a forensic psychiatrist will nonetheless interpret *this* as evidence confirming guilt (suggesting that violence has prompted the child’s denial). One might want to argue that, other things being equal, this kind of “heads I win, tails you lose” judgment would be inconsistent, and thus in principle untenable. Whoever concurs with this line of argument (as Dawes 2001 himself did)[^dawes-2001] is likely to be relying on the relevance notion of confirmation. In fact, no other notion of confirmation considered so far provides a general foundation for this judgment. $F$-confirmation, in particular, would not do, for it does allow that both $e$ and $\neg e$ confirm $h$ (relative to $k$). This is because, mathematically, it is perfectly possible for both $P(h\mid e \wedge k)$ and $P(h\mid \neg e \wedge k)$ to be arbitrarily high above $\bfrac{1}{2}.$ Condition (CompE), on the contrary, ensures that *only one* between the complementary statements $e$ and $\neg e$ can confirm hypothesis $h$ (relative to $k$). (To be precise, HD-confirmation also satisfies condition CompE, yet it would fail the above example all the same, although for a different reason, that is, because the connection between $h$ and $e$ is plausibly one of probabilistic dependence but not of logical entailment.)

Remarks such as the foregoing have induced some contemporary Bayesian theorists to dismiss the notion of confirmation as firmness altogether, concluding with I.J. Good (1968, 134) that “if you had $P(h\mid e \wedge k)$ close to unity, but less than $P(h\mid k)$, you *ought not* to say that $h$ was confirmed by $e$” (also see Salmon 1975, 13)[^salmon-1975]. Let us follow this suggestion and proceed to consider the ordinal (and quantitative) notions of relevance confirmation.

### 3.4 Differences, ratios, and partial entailment

Just as with firmness, the ordinal analysis of relevance confirmation can be characterized axiomatically. With the relevance notion, however, a larger set of options arises. Consider the following principles.

**(P4) Disjunction of alternative hypotheses** For any $e, h_{1},h_{2},k\in \bL$ and any $P\in \bP,$ if $k\vDash \neg (h_{1} \wedge h_{2})$, then $C_{P}(h_{1},e\mid k) \gtreqless C_{P}(h_{1} \vee h_{2},e\mid k)$ if and only if $P(h_{2}\mid e \wedge k)\gtreqless P(h_{2}\mid k).$

**(P5) Law of likelihood** For any $e, h_{1}, h_{2}, k\in \bL$ and any $P\in \bP,$ $C_{P}(h_{1}, e\mid k)\gtreqless C_{P}(h_{2}, e\mid k)$ if and only if $P(e\mid h_{1} \wedge k)\gtreqless P(e\mid h_{2} \wedge k).$

**(P6) Modularity (for conditionally independent data)** For any $e_{1},e_{2},h, k\in \bL$ and any $P\in \bP,$ if $P(e_{1}\mid \pm h \wedge e_{2} \wedge k)=P(e_{1}\mid \pm h \wedge k),$ then $C_{P}(h, e_{1}\mid e_{2} \wedge k) = C_{P}(h, e_{1}\mid k).$

All the above conditions occur more or less widely in the literature (see Crupi, Chater, and Tentori 2013 and Crupi and Tentori 2016 for references and discussion)[^crupi-2016]. Interestingly, they’re all pairwise incompatible on the background of the Formality and the Final Probability principles (P0 and P1 above). Indeed, they sort out the relevance notion of confirmation into three distinct, classic families of measures, as follows (Crupi, Chater, and Tentori 2013; Crupi and Tentori 2016; Heckerman 1988; Merin 2021; Sprenger and Hartmann 2020, Ch. 1)[^crupi-2016][^heckerman-1988][^merin-2021]:

**Theorem 2** Given (P0) and (P1):

1. (P4) holds if and only if $C_{P}(h, e\mid k)$ is a *probability difference measure*, that is, if there exists a strictly increasing function $f$ such that, for any $h, e, k\in \bL$ and any $P\in \bP,$ $C_{P}(h, e\mid k) = f[P(h\mid e \wedge k) - P(h\mid k)];$
2. (P5) holds if and only if $C_{P}(h, e\mid k)$ is a *probability ratio measure*, that is, if there exists a strictly increasing function $f$ such that, for any $h, e, k\in \bL$ and any $P\in \bP,$ $C_{P}(h, e\mid k) =f[\frac{P(h\mid e \wedge k)}{P(h\mid k)}];$
3. (P6) holds if and only if $C_{P}(h, e\mid k)$ is a *likelihood ratio measure*, that is, if there exists a strictly increasing function $f$ such that, for any $h, e, k\in \bL$ and any $P\in \bP,$ $C_{P}(h, e\mid k) =f[\frac{P(e\mid h \wedge k)}{P(e\mid \neg h \wedge k)}].$

If a strictly additive behavior (SA above) is imposed, one functional form is singled out for the quantitative representation of confirmation corresponding to each of the clauses above:

1. $D_{P}(h, e\mid k) = P(h\mid e \wedge k) - P(h\mid k);$
2. $R_{P}(h, e\mid k) = \log[\frac{P(h\mid e \wedge k)}{P(h\mid k)}];$
3. $L_{P}(h, e\mid k) = \log[\frac{P(e\mid h \wedge k)}{P(e\mid \neg h \wedge k)}].$

(The bases of the logarithms are assumed to be strictly greater than 1.)

Before discussing briefly this set of alternative quantitative measures of relevance confirmation, we will address one further related issue. It is a long-standing idea, going back to Carnap at least, that confirmation theory should yield an *inductive logic* that is analogous to classical deductive logic in some suitable sense, thus providing a theory of partial entailment, and partial refutation. Now, the deductive-logical notions of entailment and refutation (contradiction) exhibit the following well-known properties:

**Contraposition of entailment** Entailment is contrapositive, but not commutative. That is, it holds that $e$ entails $h$ $(e\vDash h)$ if and only if $\neg h$ entails $\neg e$ $(\neg h\vDash \neg e),$ while it does not hold that $e$ entails $h$ if and only if $h$ entails $e$ $(h\vDash e).$

**Commutativity of refutation** Refutation, on the contrary, is commutative, but not contrapositive. That is, it holds that $e$ refutes $h$ $(e\vDash \neg h)$ if and only if $h$ refutes $e$ $(h\vDash \neg e)$, while it does not hold that $e$ refutes $h$ if and only if $\neg h$ refutes $\neg e$ $(\neg h \vDash \neg\neg e).$

The confirmation-theoretic counterparts are fairly straightforward:

**(P7) Contraposition of confirmation** For any $e, h, k\in \bL$ and any $P\in \bP,$ if $e$ relevance-confirms $h$ relative to $k,$ then $C_{P}(h, e\mid k) = C_{P}(\neg e,\neg h\mid k).$

**(P8) Commutativity of disconfirmation** For any $e, h, k \in \bL$ and any $P \in \bP,$ if $e$ relevance-disconfirms $h$ relative to $k$, then $C_{P}(h, e\mid k) = C_{P}(e, h\mid k).$

The following can then be proven (Crupi and Tentori 2013)[^crupi-2013][^crupi-2013-2]:

**Theorem 3** Given (P0) and (P1), (P7) and (P8) hold if and only if $C_{P}(h, e\mid k)$ is a *relative distance measure*, that is, if there exists a strictly increasing function $f$ such that, for any $h, e, k\in \bL$ and any $P\in \bP,$ $C_{P}(h, e\mid k) = f[Z(h, e\mid k)],$ where:

$ Z(h,e\mid k)= \begin{cases} \dfrac{P(h\mid e \wedge k) - P(h\mid k)}{1-P(h\mid k)} & \mbox{if } P(h\mid e \wedge k) \ge P(h\mid k) \\ \\ \dfrac{P(h\mid e \wedge k) - P(h\mid k)}{P(h\mid k)} & \mbox{if } P(h\mid e \wedge k) \lt P(h\mid k) \end{cases} $

So, despite some pessimistic suggestions (see, e.g., Hawthorne 2018, and the discussion in Crupi and Tentori 2013)[^crupi-2013][^crupi-2013-2][^hawthorne-2018], a neat confirmation-theoretic generalization of logical entailment (and refutation) is possible after all. Interestingly, relative distance measures can be additive, but *only* for *uniform* pairs of arguments—both confirmatory or both disconfirmatory (see Milne 2014, p. 259)[^milne-2014]. (Note: Crupi, Tentori, and Gonzalez 2007; Crupi, Festa, and Buttasi 2010; and Crupi and Tentori 2013, 2014, Douven 2021, and Fitelson 2021 provide further discussions of the properties of relative distance measures, their motivation and limitations. Also see Mura 2008 for a related analysis.)[^crupi-2013][^crupi-2013-2][^douven-2021][^fitelson-2021][^mura-2008]

The plurality of alternative probabilistic measures of relevance confirmation has prompted some scholars to be skeptical or dismissive of the prospects for a quantitative theory of confirmation (see, e.g., Howson 2000, 184–185, and Kyburg and Teng 2001, 98 ff.)[^howson-2000][^kyburg-2001]. However, as we will see shortly, quantitative analyses of relevance confirmation have proved important for handling a number of puzzles and issues that plagued competing approaches. Moreover, various arguments in the philosophy of science and beyond have been shown to depend critically (and sometimes unwittingly) on the choice of one confirmation measure (or some of them) rather than others (see Festa and Cevolani 2017, Fitelson 1999, Brössel 2013, Glass 2013, Roche and Shogenji 2014, Rusconi *et al*. 2014, and van Enk 2014)[^brössel-2013][^festa-2017][^fitelson-1999][^glass-2013][^roche-2014][^rusconi-2014][^enk-2014].

Arguments have been offered by Huber (2008b) in favor of $D$, by Park (2014), Pruss (2014), and Vassend (2015) in favor of $L$ (also see Morey, Romeijn, and Rouder 2016 for an important connection with statistics), and by Crupi and Tentori (2010) in favor of $Z$. Hájek and Joyce (2008, 123), on the other hand, have seen different measures as possibly capturing “distinct, complementary notions of evidential support” (also see Schlosshauer and Wheeler 2011, Sprenger and Hartmann 2020, Ch.1, and Steel 2007 for tempered forms of pluralism)[^schlosshauer-2011][^steel-2007]. The case of measure $R$ deserves some more specific comments, however. Following Fitelson (2007), one could see $R$ as conveying key tenets of so-called “likelihoodist” position about evidential reasoning (see Royall 1997 for a classic statement, and Chandler 2013 and Sober 1990 for consonant arguments and inclinations)[^chandler-2013][^royall-1997][^sober-1990]. There seems to be some consensus, however, that compelling objections can be raised against the adequacy of $R$ as a proper measure of relevance confirmation (see, in particular, Crupi, Festa, and Buttasi 2010, 85–86; Eells and Fitelson 2002; Gillies 1986, 112; and compare Milne 1996 with Milne 2010, Other Internet Resources)[^eells-2002][^fitelson-2002][^gillies-1986][^milne-1996]. In what follows, too, it will be convenient to restrict our discussion to $D, L$ and $Z$ as candidate measures. All the results to be presented below are invariant for whatever choice among these three options, and across ordinal equivalence with each of them (but those results do *not* always extend to measures ordinally equivalent to $R$).

### 3.5 New evidence, old evidence, and total evidence

Let us go back to a classical HD case, where the (consistent) conjunction $h \wedge k$ (but not $k$ alone) entails $e.$ The following can be proven:

**Surprising prediction theorem** (SP) For any $e, h, k \in \bL$ and any $P\in \bP$ such that $h \wedge k\vDash e$ and $k\not\vDash e:$

1. if $P(e\mid k)\lt 1,$ then $e$ relevance-confirms $h$ relative to $k$ and $C_{P}(h, e\mid k)$ is a decreasing function of $P(e\mid k);$
2. if $P(e\mid k) = 1,$ then $e$ is relevance-neutral for $h$ relative to $k.$

Formally, it is fairly simple to show that (SP) characterizes relevance confirmation (see, e.g., Crupi, Festa, and Buttasi 2010, 80; Hájek and Joyce 2008, 123)[^hájek-2008][^hájek-2008-2], but the philosophical import of this result is nonetheless remarkable. For illustrative purposes, it is useful to assume the endorsement of the principle of total evidence (TE) as a default position for the Bayesian. This means that $P$ is assumed to represent *actual* degrees of belief of a rational agent, that is, given all the background information available. Then, by clause (i) of (SP), we have that the occurrence of $e$, a consequence of $h \wedge k$ (but not of $k$ alone), confirms $h$ relative to $k$ *provided that* $e$ was initially uncertain to some degree (even given $k$). In other words: $e$ *must have been predicted* on the basis of $h \wedge k$. Moreover, again by (i), the confirmatory impact will be stronger the more surprising (unlikely) the evidence was unless $h$ was conjoined to $k$. So, under TE, relevance confirmation turns out to embed a squarely predictivist version of hypothetico-deductivism! As we know, this neutralizes the charge of underdetermination, yet it comes at the usual cost, namely, the old evidence problem. In fact, if TE is in force, then clause (ii) of (SP) implies that no statement that is known to be true (thus assigned probability 1) can ever have confirmatory import.

Interestingly, the Bayesian predictivist has an escape (neatly anticipated, and criticized, by Glymour 1980a, 91–92)[^glymour-1980a]. Consider Einstein and Mercury once again. As effectively pointed out by Norton (2011a, 7), Einstein was extremely careful to emphasize that the precession phenomenon had been derived “*without having to posit any special* [*auxiliary*] *hypotheses at all*”. Why? Well, presumably because if one had allowed herself to arbitrarily devise *ad hoc* auxiliaries (within $k$, in our notation) then one could have been pretty much certain in advance to find a way to get Mercury’s data right (remember: that’s the lesson of the underdetermination theorem). But getting those data right with auxiliaries $k$ that were not thus adjusted—that would have been a natural consequence *had* the theory of general relativity been true *and it would have been surprising otherwise*. Arguably, this line of argument exploits much of the use-novelty idea within a predictivist framework. The crucial points are (i) that the evidence implied is not a verified empirical statement $e$ but the logical fact that $h \wedge k$ entails $e$, and (ii) that the existence of this connection of entailment was not to be obviously anticipated at all, precisely because $h \wedge k$ and $e$ are such that the latter did not serve as a constraint to specify the former. On these conditions, it seems that $h$ can be confirmed by this kind of “second-order” (logical) evidence in line with (SP) *while TE is concurrently preserved*.

At least two main problems arise, however. The first one is more technical in nature. Modelling rational uncertainty concerning logical facts (such as $h \wedge k \vDash e$) by probabilistic means is no trivial task. Garber (1983) put forward an influential proposal, but doubts have been raised that it might not be well-behaved (e.g., van Fraassen 1988; a careful survey with further references can be found in Eva and Hartmann 2020)[^eva-2020][^fraassen-1988]. Second, and more substantially, this solution of the old evidence problem can be charged of being an elusive change of the subject: for it was *Mercury’s data*, not anything else, that had to be recovered as having confirmed (and still confirming, some would add) Einstein’s theory. That’s the kind of judgment that confirmation theory must capture, and which remains unattainable for the predictivist Bayesian. (Earman 1992, 131, voiced this complaint forcefully. Hints for a possible rejoinder appear in Eells’s 1990 thorough discussion; see also Skyrms 1983.)[^earman-1992][^earman-1992-2][^eells-1990][^skyrms-1983]

Bayesians that are unconvinced by the predictivist position are naturally led to dismiss TE and allow for the assignment of initial probabilities lower than 1 even to statements that were known all along. Of course, this brings the underdetermination problem back, for now $k$ can still be concocted *ad hoc* to have known evidence $e$ following from $h \wedge k$ *and moreover* $P(e\mid k)\lt 1$ is not prevented by TE anymore, thus potentially licencing arbitrary confirmation relations. Two moves can be combined to handle this problem. First, unlike HD, the Bayesian framework has the formal resources to characterize the auxiliaries themselves as more or less likely and thus their adoption as relatively safe or suspicious (the standard Bayesian treatment of auxiliary hypotheses is developed along these lines in Dorling 1979 and Howson and Urbach 2006, 92–102, and it is critically discussed in Rowbottom 2010, Strevens 2001, and Worrall 1993; also see Christensen 1997 for an important analysis of related issues)[^christensen-1997][^dorling-1979][^howson-2006][^rowbottom-2010][^strevens-2001][^worrall-1993]. Second, one has to provide indications as to how TE should be relaxed. Non-TE Bayesians of the impermissivist strand often suggest that objective likelihood values concerning the outcome $e$—$P(e\mid h \wedge k)$—can be specified for the competing hypotheses at issue quite apart from the fact that $e$ may have already occurred. Such values would typically be diverse for different hypotheses (thus mathematically implying $P(e\mid k)\lt 1$) and serve as a basis to capture formally the confirmatory impact of $e$ (see Hawthorne 2005 and Climenhaga 2024 for arguments along these lines)[^climenhaga-2024][^hawthorne-2005]. Permissivists, on the other hand, can not coherently rely on these considerations to articulate a non-TE position. They must invoke *counterfactual* degrees of belief instead, suggesting that $P$ should be reconstructed as representing the beliefs that the agent would have, had she not known that $e$ was true (see Howson 1991 for a statement and discussion, and Sprenger 2015 for an original recent variant; also see Jeffrey 1995 and Wagner 2001 for relevant technical results, and Steele and Werndl 2013 for an intriguing case-study from climate science)[^howson-1991][^jeffrey-1995][^sprenger-2015][^steele-2013][^wagner-2001].

### 3.6 Paradoxes probabilified and other elucidations

The theory of Bayesian confirmation as relevance indicates when and why the HD idea works: if $h \wedge k$ (but not $k$) entails $e$, then $h$ is relevance-confirmed by $e$ (relative to $k$) *because* the latter increases the probability of the former—*provided* that $P(e\mid k) \lt 1$. Admittedly, the meaning of the latter proviso partly depends on how one handles the problem of old evidence. Yet it seems legitimate to say that Bayesian relevance confirmation (*unlike* the firmness view) retains a key point of ordinary scientific practice which is embedded in HD and yields further elements of clarification. Consider the following illustration.

**$(e_{1})$**

tigers carry the ND1 gene

**$(e_{2})$**

elephants carry the ND1 gene

$(e_{2}^*)$

lions carry the ND1 gene

**$(h)$**

all mammals carry the ND1 gene

Qualitative confirmation theories comply with the idea that $h$ is confirmed both by $e_{1} \wedge e_{2}$ and by $e_{1} \wedge e_{2}^*.$ In the HD case, it is clear that $h$ entails both conjunctions, given of course $k$ stating that tigers, lions, and elephants are all mammals (an Hempelian account could also be given easily). Bayesian relevance confirmation unequivocally yields the same qualitative verdict. There is more, however. Presumably, one might also want to say that $h$ is more strongly confirmed by $e_{1} \wedge e_{2}$ than by $e_{1} \wedge e_{2}^*,$ because the former offers a more varied and diverse body of positive evidence (interestingly, on experimental investigation, this pattern prevails in most people’s judgment, including children, see Lo et al. 2002). Indeed, the variety of evidence is a fairly central issue in the analysis of confirmation (see, e.g., Bovens and Hartmann 2002, Landes 2020, Schlosshauer and Wheeler 2011, Viale and Osherson 2000)[^bovens-2002][^schlosshauer-2011][^viale-2000]. In the illustrative case above, higher variety is readily captured by lower probability: it just seems *a priori* less likely that species as diverse as tigers and elephants share some unspecified genetic trait as compared to tigers and lions, that is, $P(e_{1} \wedge e_{2}\mid k)\lt P(e_{1} \wedge e_{2}^*\mid k).$ By (SP) above, then, one immediately gets from the relevance confirmation view the sound implication that $C_{P}(h, e_{1} \wedge e_{2}\mid k)\gt C_{P}(h, e_{1} \wedge e_{2}^*\mid k).$

Principle (SP) is also of much use in the ravens problem. Posit $h = \forall x(raven(x)\rightarrow black(x))$ once again. Just as HD, Bayesian relevance confirmation directly implies that $e = black(a)$ confirms $h$ given $k = raven(a)$ and $e^* =\neg raven(b)$ confirms $h$ given $k^* =\neg black(b)$ (provided, as we know, that $P(e\mid k)\lt 1$ and $P(e^*\mid k^*)\lt 1).$ That’s because $h \wedge k\vDash e$ and $h \wedge k^*\vDash e^*.$ But of course, to have $h$ confirmed, sampling ravens and finding a black one is intuitively more significant than failing to find a raven while sampling the enormous set of the non-black objects. That is, it seems, because the latter is very likely to obtain anyway, whether or not $h$ is true, so that $P(e^*\mid k^*)$ is actually quite close to unity. Accordingly, (SP) implies that $h$ is indeed more strongly confirmed by $black(a)$ given $raven(a)$ than it is by $\neg raven(b)$ given $\neg black(b)$—that is, $C_{P}(h, e\mid k)\gt C_{P}(h, e^*\mid k^*)$—as long as the assumption $P(e\mid k)\lt P(e^*\mid k^*)$ applies.

What then if the sampling in not constrained $(k = \top)$ and the evidence now amounts to the finding of a black raven, $e = raven(a) \wedge black(a)$, versus a non-black non-raven, $e^* =\neg black(a) \wedge \neg raven(a)$? We’ve already seen that, for either Hempelian or HD-confirmation, $e$ and $e^*$ are on a par: both Hempel-confirm $h$, none HD-confirms it. In the former case, the original Hempelian version of the ravens paradox immediately arises; in the latter, it is avoided, but at a cost: $e$ is declared flatly irrelevant for $h$—a bit of a radical move. Can the Bayesian do any better? Quite so. Consider the following conditions:

1. $P[raven(a)\mid h] = P[raven(a)] \gt 0$
2. $P[\neg raven(a) \wedge black(a)\mid h] = P[\neg raven(a) \wedge black(a)]$

Roughly, (i) says that the size of the ravens population does not depend on their color (in fact, on $h$), and (ii) that the size of the population of black *non*-raven objects also does not depend on the color of ravens. Note that both (i) and (ii) seem fairly sound as far as our best understanding of our actual world is concerned. It is easy to show that, in relevance-confirmation terms, (i) and (ii) are sufficient to imply that $e = raven(a) \wedge black(a)$, but *not* $e^* = \neg raven(a) \wedge \neg black(a)$, confirms $h$, that is $C_{P}(h,e) \gt C_{P}(h,e^*) = 0$ (this observation is due to Mat Coakley). So the Bayesian relevance approach to confirmation can make a principled difference between $e$ and $e^*$ in both ordinal *and qualitative* terms. (A broader analysis is provided by Fitelson and Hawthorne 2010, Hawthorne and Fitelson 2010 [Other Internet Resources]. Notably, their results include the full specification of the sufficient *and necessary* conditions for the main inequality $C_{P}(h, e) \gt C_{P}(h, e^*)$.)

In general, Bayesian (relevance) confirmation theory implies that the evidential import of an instance of some generalization will often depend on the credence structure, and relies on its formal representation, $P$, as a tool for more systematic analyses. Consider another instructive example. Assume that $a$ denotes some company from some (otherwise unspecified) sector of the economy, and label the latter predicate $S$. So, $k = Sa$. You are informed that $a$ increased revenues in 2019, represented as $e = Ra$. Does this confirm $h = \forall x(Sx \rightarrow Rx)$? It does, at least to some degree, one would say. For an expansion of the whole sector (recall that you have no clue what this is) surely would account for the data. That’s a straightforward HD kind of reasoning (and a suitable Hempelian counterpart reconstruction would concur). But does $e$ also confirm $h^* = Sb \rightarrow Rb$ for some further company $b$? Well, another obvious account of the data $e$ would be that company $a$ has gained market shares at the expenses of some competitor, so that support from $e$ to $h^*,$ may appear quite unwarranted (the revenues example is inspired by a remark in Blok, Medin, and Osherson 2007, 1362).

It can be shown that the Bayesian notion of relevance confirmation allows for this pattern of judgments, because (given $k$) evidence $e$ above increases the probability of $h$ but may well have the opposite effect on $h^*$ (see Sober 1994 for important remarks along similar lines)[^sober-1994]. Notably, $h$ entails $h^*$ by plain instantiation, and so contradicts $\neg h^*$. As a consequence, the implication that $C_{P}(h,e\mid k)$ is positive while $C_{P}(h^*,e\mid k)$ is not clashes with each of the following, and proves them unduly restrictive: the Special Consequence Condition (SCC), the Predictive Inference Condition (PIC), and the Consistency Condition (Cons). Note that these principles were all evaded by HD-confirmation, but all implied by confirmation as firmness (see above).

At the same time, the most compelling features of $F$-confirmation, which the HD model was unable to capture, are retained by confirmation as relevance. In fact, all our measures of relevance confirmation ($D, L$, and $Z$) entail the ordinal extension of the Entailment Condition (EC) as well as $C_{P}(h, e\mid k) = -C_{P}(\neg h, e\mid k)$ and thereby Confirmation Complementarity in all of its forms (qualitative, ordinal, and quantitative). Moreover, the Bayesian confirmation theorist of either the firmness or the relevance strand can avail herself of the same quantitative strategy of “damage control” for the main specific paradox of HD-confirmation, i.e., the irrelevant conjunction problem. (See statement (CIC) above, and Crupi and Tentori 2010, Fitelson 2002. Also see Chandler 2007 for criticism, and Moretti 2006 for a related debate.)

We’re left with one last issue to conclude our discussion, to wit, the blite paradox. Recall that $blite$ is so defined:

$$blite(x) \equiv (ex_{t\le T}(x)\rightarrow black(x)) \wedge (\neg ex_{t\le T}(x)\rightarrow white(x)).$$

As always heretofore, we assume $h = \forall x(raven(x)\rightarrow black(x)),$ $h^* = \forall x(raven(x)\rightarrow blite(x)).$ We then consider the set up where $k = raven(a) \wedge ex_{t\le T}(a),$ $e= black(a),$ and $P(e\mid k)\lt 1.$ Various authors have noted that, with Bayesian relevance confirmation, one has that $P(h\mid k)\gt P(h^*\mid k)$ is sufficient to imply that $C_{P}(h, e\mid k)\gt C_{P}(h^*,e\mid k)$ (see Gaifman 1979, 127–128; Sober 1994, 229–230; and Fitelson 2008, 131)[^fitelson-2008][^gaifman-1979][^sober-1994]. So, as long as the black hypothesis is perceived as initially more credible than its blite counterpart, the former will be more strongly confirmed than the latter. Of course, $P(h\mid k)\gt P(h^*\mid k)$ is an entirely commonsensical assumption, yet these same authors have generally, and quite understandably, failed to see this result as philosophically illuminating. Lacking some interesting, non-question-begging story as to why that inequality should obtain, no solution of the paradox seems to emerge. More modestly, one could point out that a measure of relevance confirmation $C_{P}(h, e\mid k)$ implies (i) and (ii) below.

1. Necessarily (that is, for any $P\in \bP$), $e$ confirms $h$ relative to $k$.
2. Possibly (that is, for some $P\in \bP$), each one of the following obtains:
3. $e$ confirms that a raven will be black if examined after $T$, that is, $(raven(b)\wedge \neg ex_{t\le T}(b)) \rightarrow black(b),$ relative to $k$; *and*
4. $e$ does *not* confirm that a raven will be white if examined after $T$, that is, $(raven(b)\wedge \neg ex_{t\le T}(b)) \rightarrow white(b),$ relative to $k$.

Without a doubt, (i) and (ii) fall far short of a full and satisfactory solution of the blite paradox. Yet it seems at least a legitimate minimal requirement for a compelling solution (if any exists) that it implies both. It is then of interest to note that confirmation as firmness is inconsistent with (i), while Hempelian and HD-confirmation are inconsistent with (ii).

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=confirmation). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/confirmation/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=confirmation&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/confirmation/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- Hawthorne, J. and B. Fitelson, 2010, [An Even Better Solution to the Paradox of the Ravens](http://fitelson.org/wason_addendum.pdf), manuscript available online (PDF).
- Milne, P., 2010, [Measuring Confirmation](http://fitelson.org/few/few_10/milne.pdf) (PDF), slides for a talk at the 7th Annual Formal Epistemology Workshop, Konstanz, 2–4 September 2010.

## Related Entries

Carnap, Rudolf | epistemology: Bayesian | evidence | Hempel, Carl | induction: problem of | logic: inductive | probability, interpretations of | statistics, philosophy of

### Acknowledgments

I would like to thank Gustavo Cevolani, Paul Dicken, and Jan Sprenger for useful comments on previous drafts of this entry, and Prof. Wonbae Choi for helping me correcting a mistake.

[^achinstein-2005]: Achinstein, P. (ed.), 2005, *Scientific Evidence: Philosophical Theories and Applications*, Baltimore: John Hopkins University Press.

[^baker-2003]: Baker, A., 2003, “Quantitative Parsimony and Explanatory Power”, *British Journal for the Philosophy of Science*, 54: 245–259.

[^barnes-2018]: Barnes, E.C., 2018, “Prediction versus Accommodation”, *The Stanford Encyclopedia of Philosophy* (Fall 2018 Edition), E.N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/fall2018/entries/prediction-accommodation/](https://plato.stanford.edu/archives/fall2018/entries/prediction-accommodation/)>.

[^betz-2013]: Betz, G., 2013, “Revamping Hypothetico-Deductivism: A Dialectic Account of Confirmation”, *Erkenntnis*, 78: 991–1009.

[^bird-2010]: Bird, A., 2010, “Eliminative Abduction—Examples from Medicine”, *Studies in History and Philosophy of Science*, 41: 345–352.

[^blok-2007]: Blok, S.V., D.L. Medin, and D. Osherson, 2007, “Induction as Conditional Probability Judgment”, *Memory & Cognition*, 35: 1353–1364.

[^bovens-2002]: Bovens, L. and S. Hartmann, 2002, “Bayesian Networks and the Problem of Unreliable Instruments”, *Philosophy of Science*, 69: 29–72.

[^brössel-2013]: Brössel, P., 2013, “The Problem of Measure Sensitivity Redux”, *Philosophy of Science*, 80: 378–397.

[^carnap-1950]: Carnap, R., 1950/1962, *Logical Foundations of Probability*, Chicago: University of Chicago Press.

[^chandler-2007]: Chandler, J., 2007, “Solving the Tacking Problem with Contrast Classes”, *British Journal for the Philosophy of Science*, 58: 489–502.

[^chandler-2013]: –––, 2013, “Contrastive Confirmation: Some Competing Accounts”, *Synthese*, 190: 129–138.

[^christensen-1997]: Christensen, D., 1997, “What Is Relative Confirmation?”, *Noûs*, 3: 370–384.

[^cleland-2011]: Cleland, C.E., 2011, “Prediction and Explanation in Historical Natural Science”, *British Journal for the Philosophy of Science*, 62: 551–582.

[^climenhaga-2024]: Climenhaga N., 2024, “Epistemic Probabilities Are Degrees of Support, Not Degrees of (Rational) Belief”, *Philosophy and Phenomenological Research*, 108: 153–176.

[^craig-1957]: Craig, W., 1957, “The Uses of the Herbrand-Gentzen Theorem in Relating Model Theory and Proof Theory”, *Journal of Symbolic Logic*, 3: 269–285.

[^crupi-2015]: Crupi, V., 2015, “Inductive Logic”, *Journal of Philosophical Logic*, 44 (40th anniversary issue): 641–650.

[^crupi-2025]: –––, 2025, “The Case of Early Copernicanism: Epistemic Luck *vs*. Predictivist Vindication ”, in R. Frigg, J. Alexander, L. Hudetz, M. Rédei, L. Ross, and J. Worrall (eds.), *The Continuing Influence of Imre Lakatos’s Philosophy: A Celebration of the Centenary of his Birth*, Springer, pp. 105–126.

[^crupi-2010]: Crupi, V. and K. Tentori, 2010, “Irrelevant Conjunction: Statement and Solution of a New Paradox”, *Philosophy of Science*, 77: 1–13.

[^crupi-2013]: –––, 2013, “Confirmation as Partial Entailment: A Representation Theorem in Inductive Logic”, *Journal of Applied Logic*, 11: 364–372 [Erratum in *Journal of Applied Logic*, 12: 230–231].

[^crupi-2014]: –––, 2014, “Measuring Information and Confirmation”, *Studies in the History and Philosophy of Science*, 47: 81–90.

[^crupi-2016]: –––, 2016, “Confirmation Theory”, in A. Hájek and C. Hitchcock (eds.), *Oxford Handbook of Philosophy and Probability*, Oxford: Oxford University Press, pp. 650–665.

[^crupi-2013-2]: Crupi, V., N. Chater, and K. Tentori, 2013, “New Axioms for Probability and Likelihood Ratio Measures”, *British Journal for the Philosophy of Science*, 64: 189–204.

[^crupi-2010-2]: Crupi, V., R. Festa, and C. Buttasi, 2010, “Towards a Grammar of Bayesian Confirmation”, in M. Suárez, M. Dorato, and M. Rédei (eds.), *Epistemology and Methodology of Science*, Dordrecht: Springer, pp. 73–93.

[^crupi-2008]: Crupi, V., B. Fitelson, and K. Tentori, 2008, “Probability, Confirmation, and the Conjunction Fallacy”, *Thinking & Reasoning*, 14: 182–199.

[^crupi-2007]: Crupi, V., K. Tentori, and M. Gonzalez, 2007, “On Bayesian Measures of Evidential Support: Theoretical and Empirical Issues”, *Philosophy of Science* 74: 229–52.

[^dawes-2001]: Dawes, R.M., 2001, *Everyday Irrationality*, Boulder (CO): Westview.

[^de-2008]: De Finetti, B., 2008, *Philosophical Lectures on Probability* (edited by A. Mura), Dordrecht: Springer.

[^dorling-1979]: Dorling, J., 1979, “Bayesian Personalism, the Methodology of Scientific Research Programmes, and Duhem’s Problem”, *Studies in History and Philosophy of Science*, 10: 177–187.

[^douglas-2013]: Douglas, H. and P.D. Magnus, 2013, “Why Novel Prediction Matters”, *Studies in History and Philosophy of Science*, 44: 580–589.

[^douven-2017]: Douven, I., 2017, “Abduction”, in E.N. Zalta (ed.), *The Stanford Encyclopedia of Philosophy* (Summer 2017 Edition), URL = <[https://plato.stanford.edu/archives/sum2017/entries/abduction/](https://plato.stanford.edu/archives/sum2017/entries/abduction/)>.

[^douven-2021]: –––, 2021, “Tracking Confirmation”, *Philosophy of Science*, 88: 398–414.

[^douven-2006]: Douven, I. and W. Meijs, 2006, “Bootstrap Confirmation Made Quantitative”, *Synthese*, 149: 97–132.

[^duhem-1906]: Duhem, P., 1906, *The Aim and Structure of Physical Theory*, Princeton (NJ): Princeton University Press, 1991.

[^earman-1992]: Earman, J., 1992, *Bayes or Bust?*, Cambridge (MA): MIT Press.

[^earman-1983]: ––– (ed.), 1983, *Minnesota Studies in Philosophy of Science*, Vol. 10: *Testing Scientific Theories*, Minneapolis: University of Minnesota Press.

[^earman-1988]: Earman, J. and C. Glymour, 1988, “What Revisions Does Bootstrap Testing Need?”, *Philosophy of Science*, 55: 260–264.

[^earman-1993]: Earman, J. and M. Janssen, 1993, “Einstein’s Explanation of the Motion of Mercury’s Perihelion”, in J. Earman, M. Janssen, and J. Norton (eds.), *The Attraction of Gravity: New Studies in the History of General Relativity*, Boston: Birkhäuser, pp. 129–172.

[^earman-1992-2]: Earman, J. and W.C. Salmon, 1992, “The Confirmation of Scientific Hypotheses”, in M.H. Salmon et al., *Introduction to the Philosophy of Science*, Englewood Cliff: Prentice Hall, pp. 42–103.

[^easwaran-2011a]: Easwaran, K., 2011a, “Bayesianism I: Introduction and Arguments in Favor”, *Philosophy Compass*, 6: 312–320.

[^easwaran-2011b]: –––, 2011b, “Bayesianism II: Criticisms and Applications”, *Philosophy Compass*, 6: 321–332.

[^eells-1990]: Eells, E., 1990, “Bayesian Problems of Old Evidence”, in Savage, 1990, pp. 205–223.

[^eells-2002]: Eells, E. and B. Fitelson, 2002, “Symmetries and Asymmetries in Evidential Support”, *Philosophical Studies*, 107: 129–42.

[^eva-2020]: Eva, B. and S. Hartmann, 2020, “On the Origins of Old Evidence”, *Australasian Journal of Philosophy*, 98: 481–494.

[^festa-1999]: Festa, R., 1999, “Bayesian Confirmation”, in M. Galavotti and A. Pagnini (eds.), *Experience, Reality, and Scientific Explanation*, Dordrecht: Kluwer, pp. 55–87.

[^festa-2003]: –––, 2003, “Induction, Probability, and Bayesian Epistemology”, *Poznan Studies in the Philosophy of Science and the Humanities*, 80: 251–284.

[^festa-2017]: Festa, R. and G. Cevolani, 2017, “Unfolding the Grammar of Bayesian Confirmation: Likelihood and Anti-Likelihood Principles”, *Philosophy of Science*, 84: 56–81.

[^fitelson-1999]: Fitelson, B., 1999, “The Plurality of Bayesian Measures of Confirmation and the Problem of Measure Sensitivity”, *Philosophy of Science*, 66: S362–78.

[^fitelson-2002]: –––, 2002, “Putting the Irrelevance Back into the Problem of Irrelevant Conjunction”, *Philosophy of Science*, 69: 611–622.

[^fitelson-2007]: –––, 2007, “Likelihoodism, Bayesianism, and Relational Confirmation”, *Synthese* 156: 473–89.

[^fitelson-2008]: –––, 2008, “Goodman’s New Riddle”, *Journal of Philosophical Logic*, 37: 613–643.

[^fitelson-2021]: –––, 2021, “A Problem for Confirmation Measure Z”, *Philosophy of Science*, 88: 726–730.

[^fitelson-2010]: Fitelson, B. and J. Hawthorne, 2010, “How Bayesian Confirmation Theory Handles the Paradox of the Ravens”, in E. Eells and J. Fetzer (eds.), *The Place of Probability in Science*, Dordrecht: Springer, pp. 247–276.

[^forster-2007]: Forster, M., 2007, “A Philosopher’s Guide to Empirical Success”, *Philosophy of Science*, 74: 588–600.

[^forster-1994]: Forster, M. and E. Sober, 1994, “How to Tell When Simpler, More Unified, or Less *Ad Hoc* Theories Will Provide More Accurate Predictions”, *British Journal for the Philosophy of Science*, 45: 1–35.

[^franklin-2001]: Franklin, J., 2001, “Resurrecting Logical Probability”, *Erkenntnis*, 55: 277–305.

[^gabbay-2011]: Gabbay, D., S. Hartmann, and J. Woods (eds.), 2011, *Handbook of the History of Logic*, Vol. 10: *Inductive Logic*, Amsterdam: Elsevier.

[^gaifman-1979]: Gaifman, H., 1979, “Subjective Probability, Natural Predicates, and Hempel’s Ravens”, *Erkenntnis*, 14: 105–147.

[^garber-1983]: Garber, D., 1983, “Old Evidence and Logical Omniscience”, in Earman, 1983, pp. 99–131.

[^gemes-1993]: Gemes, K. 1993, “Hypothetico-Deductivism, Content and the Natural Axiomatization of Theories”, *Philosophy of Science*, 60: 477–487.

[^gemes-1998]: –––, 1998, “Hypothetico-Deductivism: The Current State of Play; The Criterion of Empirical Significance: Endgame”, *Erkenntnis*, 49: 1–20.

[^gemes-2005]: –––, 2005, “Hypothetico-Deductivism: Incomplete But Not Hopeless”, *Erkenntnis*, 63: 139–147.

[^giere-1983]: Giere, R.N., 1983, “Testing Theoretical Hypotheses”, in Earman, 1983, pp. 269–298.

[^giere-1979]: –––, 1979, *Understanding Scientific Reasoning*, Belmont (CA): Thomson / Wadsworth, 2006.

[^gillies-1986]: Gillies, D., 1986, “In Defense of the Popper-Miller Argument”, *Philosophy of Science*, 53: 110–113.

[^gillies-1989]: –––, 1989, “Non-Bayesian Confirmation Theory and the Principle of Explanatory Surplus”, in A. Fine and J. Leplin (eds.), *Proceedings of the 1988 Biennial Meeting of Philosophy of Science Association*, Vol. 2, East Lansing (MI): Philosophy of Science Association, pp. 381–392.

[^gillies-2000]: –––, 2000, *Philosophical Theories of Probability*, London: Routledge.

[^glass-2013]: Glass, D.H., 2013, “Confirmation Measures of Association Rule Interestingness”, *Knowledge-Based Systems*, 44: 65–77.

[^glymour-1980a]: Glymour, C., 1980a, *Theory and Evidence*, Princeton (NJ): Princeton University Press.

[^glymour-1980b]: –––, 1980b, “Hypothetico-Deductivism Is Hopeless”, *Philosophy of Science*, 47: 322–325.

[^good-1967]: Good, I.J., 1967, “The White Shoe Is a Red Herring”, *British Journal for the Philosophy of Science*, 17: 322.

[^good-1968]: –––, 1968, “Corroboration, Explanation, Evolving Probabilities, Simplicity, and a Sharpened Razor”, *British Journal for the Philosophy of Science*, 19: 123–43.

[^good-1971]: –––, 1971, “46656 Varieties of Bayesians”, *American Statistician*, 25 (5): 62–63.

[^goodman-1955]: Goodman, N., 1955, *Fact, Fiction, and Forecast*, Cambridge (MA): Harvard University Press, 1983.

[^guala-2012]: Guala, F., 2012, “Experimentation in Economics”, in D. Gabbay, P. Thagard, J. Woods, and U. Mäki (eds.), *Handbook of the Philosophy of Science: Philosophy of Economics*, Amsterdam: Elsevier, pp. 597–640.

[^hájek-2008]: Hájek, A., 2008. “Arguments For—Or Against—Probabilism?”, *British Journal for the Philosophy of Science*, 59: 793–819.

[^hájek-2019]: –––, 2019, “Interpretations of Probability”, E.N. Zalta (ed.), *The Stanford Encyclopedia of Philosophy* (Fall 2019 Edition), URL = <[https://plato.stanford.edu/archives/fall2019/entries/probability-interpret/](https://plato.stanford.edu/archives/fall2019/entries/probability-interpret/)>.

[^hájek-2008-2]: Hájek, A. and J. Joyce, 2008, “Confirmation”, in S. Psillos and M. Curd (eds.), *Routledge Companion to the Philosophy of Science*, New York: Routledge, pp. 115–29.

[^hawthorne-2005]: Hawthorne, J., 2005, “Degrees-of-Belief and Degrees-of-Support: Why Bayesians Need Both Notions”, *Mind*, 114: 277–320.

[^hawthorne-2011]: –––, 2011, “Confirmation Theory”, in D. Gabbay, P. Thagard, J. Woods, P.S. Bandyopadhyay, and M. Forster (eds.), *Handbook of the Philosophy of Science: Philosophy of Statistics*, Dordrecht: Elsevier, pp. 333–389.

[^hawthorne-2018]: –––, 2018, “Inductive Logic”, in E.N. Zalta (ed.), *The Stanford Encyclopedia of Philosophy* (Spring 2018 Edition), URL = <[https://plato.stanford.edu/archives/spr2018/entries/logic-inductive/](https://plato.stanford.edu/archives/spr2018/entries/logic-inductive/)>.

[^heckerman-1988]: Heckerman, D., 1988, “An Axiomatic Framework for Belief Updates”, in J.F. Lemmer and L.N. Kanal (eds.), *Uncertainty in Artificial Intelligence* 2, Amsterdam: North-Holland, pp. 11–22.

[^hempel-1937]: Hempel, C.G., 1937, “Le problème de la vérité”, *Theoria*, 3: 206–246.

[^hempel-1943]: –––, 1943, “A Purely Syntactical Definition of Confirmation”, *Journal of Symbolic Logic*, 8: 122–143.

[^hempel-1945]: –––, 1945, “Studies in the Logic of Confirmation”, *Mind*, 54: 1–26, 97–121.

[^hesse-1975]: Hesse, M. 1975, “Bayesian Methods and the Initial Probabilities of Theories”, in Maxwell and Anderson, 1975, pp. 50–105.

[^hitchcock-2004]: Hitchcock, C. and E. Sober, 2004, “Prediction *versus* Accommodation and the Risk of Overfitting”, *British Journal for the Philosophy of Science*, 55: 1–34.

[^horvitz-1986]: Horvitz, E. and D. Heckerman, 1986, “The Inconsistent Use of Measures of Certainty in Artificial Intelligence Research”, in L.N. Kanal and J.F. Lemmer (eds.), *Uncertainty in Artificial Intelligence*, Amsterdam: North-Holland, pp. 137–151.

[^horwich-1983]: Horwich, P., 1983, “Explanations of Irrelevance”, in Earman, 1983, pp. 55–65.

[^hosiasson-lindenbaum-1940]: Hosiasson-Lindenbaum, J., 1940, “On Confirmation”, *Journal of Symbolic Logic*, 5: 133–148.

[^howson-1990]: Howson, C., 1990, “Fitting Theory to the Facts: Probably Not Such a Bad Idea After All”, in Savage, 1990, pp. 224–244.

[^howson-1991]: –––, 1991, “The ‘Old Evidence’ Problem”, *British Journal for the Philosophy of Science*, 42: 547–555.

[^howson-2000]: –––, 2000, *Hume’s Problem: Induction and the Justification of Belief*, Oxford: Oxford University Press.

[^howson-2006]: Howson, C. and P. Urbach, 2006, *Scientific Reasoning. The Bayesian Approach*, La Salle (IL): Open Court.

[^huber-2008a]: Huber, F., 2008a, “Hempel’s Logic of Confirmation”, *Philosophical Studies*, 139: 181–189.

[^huber-2008b]: –––, 2008b, “Assessing Theories, Bayes Style”, *Synthese*, 161: 89–118.

[^huber-2009]: Huber, F. and C. Schmidt-Petri, 2009, *Degrees of Belief*, Dordrecht: Springer.

[^janssen-2003]: Janssen, M., 2003, “COI Stories: Explanation and Evidence in the History of Science”, *Perspectives on Science*, 10: 457–522.

[^jeffrey-1995]: Jeffrey, R., 1995, “Probability Reparation: The Problem of New Explanation”, *Philosophical Studies*, 77: 97–101.

[^joyce-2019]: Joyce, J., 2019, “Bayes’ Theorem”, in E.N. Zalta (ed.), *The Stanford Encyclopedia of Philosophy* (Spring 2019 Edition), URL = <[https://plato.stanford.edu/archives/spr2019/entries/bayes-theorem/](https://plato.stanford.edu/archives/spr2019/entries/bayes-theorem/)>.

[^joyce-2011]: –––, 2011, “The Development of Subjective Bayesianism”, in Gabbay, Hartmann, and Woods, 2011, pp. 415–476.

[^kelly-2007]: Kelly, K., 2007, “A New Solution to the Puzzle of Simplicity”, *Philosophy of Science*, 74: 561–573.

[^kelly-2008]: –––, 2008, “Ockham’s Razor, Truth, and Information”, in D. Gabbay, P. Thagard, J. Woods, P. Adriaans, and J. van Benthem (eds.), *Handbook of the Philosophy of Science: Philosophy of Information*, Dordrecht: Elsevier, pp. 321–360.

[^kelly-2004]: Kelly, K. and C. Glymour, 2004, “Why Probability Does Not Capture the Logic of Scientific Justification”, in C. Hitchcock (ed.), *Contemporary Debates in the Philosophy of Science*, London: Blackwell, pp. 94–114.

[^keynes-1921]: Keynes, J., 1921, *A Treatise on Probability*, London: Macmillan.

[^kitcher-1993]: Kitcher, P., 1993. *The Advancement of Science*, Oxford: Oxford University Press.

[^kopec-2016]: Kopec, M. and M. Titelbaum, 2016, “The Uniqueness Thesis”, *The Philosophy Compass*, 11: 189–200.

[^kuhn-1957]: Kuhn, T., 1957, *The Copernican Revolution*, Cambridge (MA): Harvard University Press.

[^kuhn-1962]: –––, 1962/1970, *The Structure of Scientific Revolutions*, Chicago: University of Chicago Press.

[^kuipers-2000]: Kuipers, T., 2000, *From Instrumentalism to Constructive Realism*, Dordrecht: Reidel.

[^kyburg-2001]: Kyburg, H.E. and C.M. Teng, 2001, *Uncertain Inference*, New York: Cambridge University Press.

[^lakatos-1975]: Lakatos, I. and E. Zahar, 1975, “Why did Copernicus’ Research Programme Supersede Ptolemy’s?”, in R.S. Westman (ed.), *The Copernican Achievement*, Berkeley (CA): University of California Press, pp. 354–383 (reprinted in Lakatos, I., *Philosophical Papers* I: *The Methodology of Scientific Research Programmes*, Cambridge: Cambridge University Press, 1978, pp. 168–192).

[^landes-2018]: Landes J., 2018, “Variety of Evidence”, *Erkenntnis*, 85: 183–223.

[^lange-2011]: Lange, M., 2011, “Hume and the Problem of Induction”, in Gabbay, Hartmann, and Woods, 2011, pp. 43–91.

[^laudan-1990]: Laudan, L., 1990, “Demystifying Underdetermination”, in Savage, 1990, pp. 267–297.

[^laudan-1997]: –––, 1997, “How About Bust? Factoring Explanatory Power Back into Theory Evaluation”, *Philosophy of Science*, 64: 206–216.

[^laudan-1991]: Laudan, L. and J. Leplin, 1991, “Empirical Equivalence and Underdetermination”, *Journal of Philosophy*, 88: 449–472.

[^levi-2008]: Levi, I., 2008, “Degrees of Belief”, *Journal of Logic and Computation*, 18: 699–719.

[^liebman-2000]: Liebman, J., J. Fagan, V. West, and J. Lloyd, 2000, “Capital Attrition: Error Rates in Capital Cases, 1973–1995”, *Texas Law Review*, 78: 1839–1865.

[^lipton-2000]: Lipton, P., 2000, “Inference to the Best Explanation”, in W.H. Newton-Smith (ed.), *A Companion to the Philosophy of Science*, Oxford: Blackwell, pp. 184–193.

[^lipton-2004]: –––, 2004, *Inference to the Best Explanation*, London: Routledge.

[^lipton-2005]: –––, 2005, “Testing Hypotheses: Prediction and Prejudice”, *Science*, 307: 219–221.

[^lo-2002]: Lo, Y., A. Sides, J. Rozelle, and D.N. Osherson, 2002, “Evidential Diversity and Premise Probability in Young Children’s Inductive Judgment”, *Cognitive Science*, 26: 181–206.

[^maher-1996]: Maher, P., 1996, “Subjective and Objective Confirmation”, *Philosophy of Science*, 63: 149–174.

[^maher-2006]: –––, 2006, “Confirmation Theory”, in D.M. Borchert (ed.), *Encyclopedia of Philosophy* (2ⁿᵈ edition), Detroit (MI): Macmillan Reference.

[^maher-2010]: –––, 2010, “Explication of Inductive Probability”, *Journal of Philosophical Logic*, 39: 593–616.

[^martens-2009]: Martens, R., 2009, “Harmony and Simplicity: Aesthetic Virtues and the Rise of Testability”, *Studies in History and Philosophy of Science*, 40: 258–266.

[^maxwell-1975]: Maxwell, G. and R.M. Anderson, Jr. (eds.), 1975, *Minnesota Studies in Philosophy of Science*, Vol. 6: *Induction, Probability, and Confirmation*, Minneapolis: University of Minnesota Press.

[^mayo-1991]: Mayo, D., 1991, “Novel Evidence and Severe Tests”, *Philosophy of Science*, 58: 523–553.

[^mayo-1996]: –––, 1996, *Error and the Growth of Experimental Knowledge*, Chicago: University of Chicago Press.

[^mayo-2010]: –––, 2010,“Learning from Error: The Theoretical Significance of Experimental Knowledge”, *The Modern Schoolman*, 87: 191–217.

[^mayo-2014]: –––, 2014,“Some Surprising Facts about (the Problem of) Surprising Facts”, *Studies in the History and Philosophy of Science*, 45: 79–86.

[^mayo-2010-2]: Mayo, D. and A. Spanos (eds.), 2010, *Error and Inference: Recent Exchanges on Experimental Reasoning, Reliability, and the Objectivity and Rationality of Science*, Cambridge and London: Cambridge University Press.

[^meacham-2014]: Meacham, C.J.G., 2014, “Impermissive Bayesianism”, *Erkenntnis*, 79: 1185–1217.

[^meehl-1990]: Meehl, P.E., 1990, “Appraising and Amending Theories: The Strategy of Lakatosian Defense and Two Principles That Warrant Using It”, *Psychological Inquiry*, 1: 108–141.

[^merin-2021]: Merin A., 2021, “Evidential Relevance”, in M. Knauff and W. Spohn (eds.), *The Handbook of Rationality*, MIT Press, pp. 265–275.

[^mill-1843]: Mill, J.S., 1843/1872, *A System of Logic*, Honolulu: University Press of the Pacific, 2002.

[^milne-1996]: Milne, P., 1996, “$\Log[P(h\mid eb)/P(h\mid b)]$ Is the One True Measure of Confirmation”, *Philosophy of Science*, 63: 21–6.

[^milne-2014]: –––, 2014, “Information, Confirmation, and Conditionals”, *Journal of Applied Logic*, 12: 252–262.

[^moretti-2006]: Moretti, L., 2006, “The Tacking by Disjunction Paradox: Bayesianism versus Hypothetico-Deductivism”, *Erkenntnis*, 64: 115–138.

[^morey-2016]: Morey, R.D., J.-W. Romeijn, and J.N. Rouder, 2016, “The Philosophy of Bayes Factors and the Quantification of Statistical Evidence”, *Journal of Mathematical Psychology*, 72: 6–18.

[^mura-2008]: Mura, A., 2008, “Can Logical Probability Be Viewed as a Measure of Degrees of Partial Entailment?”, *Logic & Philosophy of Science* 6: 25–33.

[^musgrave-1974]: Musgrave, A., 1974, “Logical *versus* Historical Theories of Confirmation”, *British Journal for the Philosophy of Science*, 25: 1–23.

[^musgrave-2010]: –––, 2010, “Critical Rationalism, Explanation, and Severe Tests”, in D. Mayo and A. Spanos, 2010, pp. 88–112.

[^newman-toker-2022]: Newman-Toker D.E. N. Nassery, A.C. Schaffer, C.W. Yu-Moe, G.D. Clemens, Z. Wangs, Y. Zhu, A.S.S. Tehrani, M. Fanai, A. Hassoon, and D. Siegel, 2022, “Diagnostic Errors in the Emergency Department: A Systematic Review ”, Agency for Healthcare Research and Quality (US), Report No. 22(23)-EHC043, Rockville (MD).

[^nicod-1924]: Nicod, J., 1924, *Le problème logique de l’induction*, Paris: Alcan. (Engl. transl. “The Logical Problem of Induction”, in *Foundations of Geometry and Induction*, London: Routledge, 2000.)

[^norton-2005]: Norton, J., 2005, “A Little Survey on Induction”, in P. Achinstein (ed.), *Scientific Evidence: Philosophical Theories and Applications*, Baltimore: John Hopkins University Press, pp. 9–34.

[^norton-2011a]: –––, 2011a, “History of Science and the Material Theory of Induction: Einstein’s Quanta, Mercury’s Perihelion”, *European Journal for Philosophy of Science*, 1: 3–27.

[^norton-2011b]: –––, 2011b, “Challenges to Bayesian Confirmation Theory”, in D. Gabbay, P. Thagard, J. Woods, S. Bandyopadhyay, and M. Forster (eds.), *Handbook of the Philosophy of Science: Philosophy of Statistics*, Amsterdam: Elsevier, pp. 391–440.

[^oaksford-2007]: Oaksford, M. and N. Chater, 2007, *Bayesian Rationality*, Oxford: Clarendon Press.

[^okasha-2011]: Okasha, S., 2011, “Experiment, Observation, and the Confirmation of Laws”, *Analysis*, 71: 222–232.

[^osherson-1986]: Osherson, D., E.E. Smith, and E. Shafir, 1986, “Some Origins of Belief”, *Cognition*, 24: 197–224.

[^paris-2011]: Paris, J., 2011, “Pure Inductive Logic”, in L. Horsten and R. Pettigrew (eds.), *The Continuum Companion to Philosophical Logic*, London: Continuum, pp. 428–449.

[^park-2014]: Park, I., 2014, “Confirmation Measures and Collaborative Belief Updating”, *Synthese*, 191: 3955–3975.

[^peijnenburg-2012]: Peijnenburg, J., 2012, “A Case of Confusing Probability and Confirmation”, *Synthese*, 184: 101–107.

[^peirce-1878]: Peirce, C.S., 1878, “The Probability of Induction”, in *Philosophical Writings of Peirce* (edited by J. Buchler), New York: Dover, pp. 174–189.

[^pettigrew-2016]: Pettigrew, R., 2016, *Accuracy and the Laws of Credence*, Oxford: Oxford University Press.

[^popper-1934]: Popper, K.R., 1934/1959, *The Logic of Scientific Discovery*, London: Routledge, 2002.

[^popper-1954]: –––, 1954, “Degree of Corroboration”, *British Journal for the Philosophy of Science*, 5: 143–149.

[^popper-1963]: –––, 1963, *Conjectures and Refutations*, London: Routledge, 2002.

[^prasetya-2024]: Prasetya Y., 2024, “Which Models of Scientific Explanation Are (In)Compatible with Inference to the Best Explanation”, *British Journal for the Philosophy of Science*, 75: 209–232.

[^pruss-2014]: Pruss, A.R., 2014, “Independent Tests and the Log-Likelihood Ratio Measure of Confirmation”, *Thought*, 3: 124–135.

[^quine-1951]: Quine, W.v.O., 1951, “Two Dogmas of Empiricism”, in *From a Logical Point of View*, Cambridge (MA): Harvard University Press, pp. 20–46.

[^quine-1970]: –––, 1970, “Natural Kinds”, in N. Rescher (ed.), *Essays in Honor of Carl G. Hempel*, Dordrecht: Reidel, pp. 41–56.

[^quine-1970-2]: Quine, W.v.O. and J. Ullian, 1970, *The web of Belief*, New York: Random House.

[^riesch-2010]: Riesch, H., 2010, “Simple or Simplistic? Scientists’ Views on Occam’s Razor”, *Theoria*, 67: 75–90.

[^rinard-2014]: Rinard, S., 2014, “A New Bayesian Solution to the Problem of the Ravens”, *Philosophy of Science*, 81: 81–100.

[^roche-2014]: Roche, W. and T. Shogenji, 2014, “Dwindling Confirmation”, *Philosophy of Science*, 81: 114–137.

[^rowbottom-2010]: Rowbottom, D.P., 2010, “Corroboration and Auxiliary Hypotheses: Duhem’s Thesis Revisited”, *Synthese*, 177: 139–149.

[^royall-1997]: Royall, R., 1997, *Statistical Evidence: A Likelihood Paradigm*, London: Chapman & Hall.

[^rusconi-2014]: Rusconi, P., M. Marelli, M. D’Addario, S. Russo, and P. Cherubini, 2014, “Evidence Evaluation: Measure *Z* Corresponds to Human Utility Judgments Better than Measure *L* and Optimal-Experimental-Design Models”, *Journal of Experimental Psychology: Learning, Memory, and Cognition*, 40: 703–723.

[^russell-1912]: Russell, B., 1912, *The Problems of Philosophy*, Oxford: Oxford University Press, 1997.

[^salmon-1969]: Salmon, W.C., 1969, “Partial Entailment as a Basis for Inductive Logic”, in N. Rescher (ed.), *Essays in Honor of Carl G. Hempel*, Dordrecht: Reidel, pp. 47–81.

[^salmon-1975]: –––, 1975, “Confirmation and Relevance”, in Maxwell and Anderson, 1975, pp. 3–36.

[^salmon-2001]: –––, 2001, “Explanation and Confirmation: A Bayesian Critique of Inference to the Best Explanation”, in G. Hon and S.S. Rakover (eds.), *Explanation: Theoretical Approaches and Applications*, Dordrecht: Kluwer, pp. 61–91.

[^savage-1990]: Savage, C.W. (ed.), 1990, *Minnesota Studies in the Philosophy of Science*, Vol. 14: *Scientific Theories*, Minneapolis: University of Minnesota Press.

[^schippers-2017]: Schippers, M., 2017, “A Representation Theorem for Absolute Confirmation”, *Philosophy of Science*, 84: 82–91.

[^schlosshauer-2011]: Schlosshauer, M. and G. Wheeler, 2011, “Focussed Correlation, Confirmation, and the Jigsaw Puzzle of Variable Evidence”, *Philosophy of Science*, 78: 376–392.

[^schurz-1991]: Schurz, G., 1991, “Relevant Deduction”, *Erkenntnis*, 35: 391–437.

[^schurz-1994]: –––, 1994, “Relevant Deduction and Hypothetico-Deductivism: A Reply to Gemes”, *Erkenntnis*, 41: 183–188.

[^schurz-2005]: –––, 2005, “Bayesian H-D Confirmation and Structuralistic Truthlikeness: Discussion and Comparison with the Relevant-Element and the Content-Part Approach”, in R. Festa, A. Aliseda, and J. Peijnenburg (eds.), *Confirmation, Empirical Progress, and Truth Approximation. Essays in Debate with Theo Kuipers*, Vol. I, Amsterdam: Rodopi, pp. 141–159.

[^schurz-2014]: –––, 2014, “Bayesian Pseudo-Confirmation, Use-Novelty, and Genuine Confirmation”, *Studies in the History and Philosophy of Science*, 45: 87–96.

[^schwartz-2011]: Schwartz, R., 2011, “Goodman and the Demise of Syntactic and Semantic Models”, in Gabbay, Hartmann, and Woods, 2011, pp. 391–413.

[^scorzato-2013]: Scorzato, L., 2013, “On the Role of Simplicity in Science”, *Synthese*, 190: 2867–2895.

[^shogenji-2012]: Shogenji, T., 2012, “The Degree of Epistemic Justification and the Conjunction Fallacy”, *Synthese*, 184: 29–48.

[^skyrms-1983]: Skyrms, B., 1983, “Three Ways to Give a Probability Assignment a Memory”, in Earman, 1983, pp. 157–162.

[^skyrms-1987]: –––, 1987, “Coherence”, in N. Rescher (ed.) *Scientific Inquiry in Philosophical Perspective*, Pittsburgh: University of Pittsburgh Press, pp. 225–242.

[^sober-1975]: Sober, E., 1975, *Simplicity*, Oxford: Clarendon Press.

[^sober-1990]: –––, 1990, “Contrastive Empiricism”, in Savage, 1990, pp. 392–412.

[^sober-1994]: –––, 1994, “No Model, No Inference: A Bayesian Primer on the Grue Problem”, in D. Stalker (ed.), *Grue! The New Riddle of Induction*, Chicago (IL): Open Court, pp. 225–240.

[^spohn-2012]: Spohn, W., 2012, *The Laws of Belief*, Oxford: Oxford University Press.

[^sprenger-2011a]: Sprenger, J., 2011a, “Hempel and the Paradoxes of Confirmation”, in Gabbay, Hartmann, and Woods, 2011, pp. 231–260.

[^sprenger-2011b]: –––, 2011b, “Hypothetico-Deductive Confirmation”, *Philosophy Compass*, 6: 497–508.

[^sprenger-2015]: –––, 2015, “A Novel Solution to the Problem of Old Evidence”, *Philosophy of Science*, 82: 383–401.

[^sprenger-2019]: Sprenger, J. and S. Hartmann, 2019, *Bayesian Philosophy of Science*, Oxford: Oxford University Press.

[^steel-2007]: Steel, D., 2007, “Bayesian Confirmation Theory and the Likelihood Principle”, *Synthese*, 156: 55–77.

[^steele-2013]: Steele, K. and C. Werndl, 2013, “Climate Models, Calibration, and Confirmation”, *British Journal for the Philosophy of Science*, 64: 609–635.

[^strasser-2019]: Strasser, C. and G.A. Antonelli, 2019, “Non-monotonic Logic”, *The Stanford Encyclopedia of Philosophy* (Summer 2019 Edition), E.N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/sum2019/entries/logic-nonmonotonic/](https://plato.stanford.edu/archives/sum2019/entries/logic-nonmonotonic/)>.

[^strevens-2001]: Strevens, M., 2001, “The Bayesian Treatment of Auxiliary Hypotheses”, *British Journal for the Philosophy of Science*, 52: 515–537.

[^tentori-2007]: Tentori, K., V. Crupi, and D. Osherson, 2007, “Determinants of Confirmation”, *Psychonomic Bulletin & Review*, 14: 877–83.

[^tentori-2010]: –––, 2010, “Second-order Probability Affects Hypothesis Confirmation”, *Psychonomic Bulletin & Review*, 17: 129–34.

[^thagard-1978]: Thagard, P.R., 1978, “The Best Explanation: Criteria for Theory Choice”, *Journal of Philosophy*, 75: 76–92.

[^törnebohm-1966]: Törnebohm, H., 1966, “Two Measures of Evidential Strength”, in J. Hintikka and P. Suppes (eds.), *Aspects of Inductive Logic*, Amsterdam: North-Holland, pp. 81–95.

[^enk-2014]: van Enk, S.J., 2014, “Bayesian Measures of Confirmation from Scoring Rules”, *Philosophy of Science*, 81: 101–113.

[^fraassen-1988]: van Fraassen, B.C., 1988, “The Problem of Old Evidence”, in D.F. Austin (ed.), *Philosophical Analysis*, Dordrecht: Reidel, pp. 153–165.

[^fraassen-1989]: –––, B.C., 1989, *Laws and Symmetry*, Oxford: Oxford University Press.

[^varzi-2008]: Varzi, A.C., 2008, “Patterns, Rules, and Inferences”, in J.A. Adler and L.J. Rips (eds.), *Reasoning: Studies in Human Inference and Its Foundations*, Cambridge: Cambridge University Press, pp. 282–290.

[^vassend-2015]: Vassend, O.B., 2015, “Confirmation Measures and Sensitivity”, *Philosophy of Science*, 82: 892–904.

[^viale-2000]: Viale, R. and D. Osherson, 2000, “The Diversity Principle and the Little Scientist Hypothesis”, *Foundations of Science*, 5: 239–253.

[^vineberg-2016]: Vineberg, S., 2016, “Dutch Book Arguments”, in E.N. Zalta (ed.), *The Stanford Encyclopedia of Philosophy* (Spring 2016 Edition), URL = <[https://plato.stanford.edu/archives/spr2016/entries/dutch-book/](https://plato.stanford.edu/archives/spr2016/entries/dutch-book/)>.

[^votsis-2014]: Votsis, I., 2014, “Objectivity in Confirmation: Post Hoc Monsters and Novel Predictions”, *Studies in the History and Philosophy of Science*, 45: 70–78.

[^wagner-2001]: Wagner, C.G., 2001, “Old Evidence and New Explanation III”, *Philosophy of Science*, 68: S165–S175.

[^weisberg-2015]: Weisberg, J., 2015, “You’ve Come a Long Way, Bayesians”, *Journal of Philosophical Logic*, 44 (The Fortieth Anniversary Issue): 817–834.

[^whewell-1840]: Whewell, W., 1840/1847, *The Philosophy of the Inductive Sciences, Founded Upon Their History*, Charleston (SC): BiblioBazaar, 2011.

[^williamson-2011]: Williamson, J., 2011, “An Objective Bayesian Account of Confirmation”, in D. Dieks, W.J. Gonzalez, S. Hartmann, T. Uebel, and M. Weber (eds.), *Explanation, Prediction, and Confirmation*, Berlin: Springer, 2011, pp. 53–81.

[^williamson-2002]: Williamson, T., 2002, *Knowledge and Its Limits*, Oxford: Oxford University Press.

[^woodward-1983]: Woodward, J., 1983, “Glymour on Theory Confirmation”, *Philosophical Studies*, 43: 147–152.

[^woodward-2019]: –––, 2019, “Scientific Explanation”, *The Stanford Encyclopedia of Philosophy* (Winter 2019 Edition), E.N. Zalta (ed.), URL= <[https://plato.stanford.edu/archives/win2019/entries/scientific-explanation/](https://plato.stanford.edu/archives/win2019/entries/scientific-explanation/)>.

[^worrall-1978]: Worrall, J., 1978, “The Ways in Which the Methodology of Scientific Research Programmes Improves on Popper’s Methodology”, in G. Radnitzky and G. Andersson (eds.), *Progress and Rationality in Science*, Dordrecht: Reidel, 1978, pp. 45–70.

[^worrall-1982]: –––, 1982, “Broken Bootstraps”, *Erkenntnis*, 18: 105–130.

[^worrall-1990]: –––, 1990, “Scientific Revolutions and Scientific Rationality: The Case of the ‘Elderly Holdout’”, in Savage, 1990, pp. 319–354.

[^worrall-1993]: –––, 1993, “Falsification, Rationality, and the Duhem Problem”, in J. Earman, G.J. Massey, and N. Rescher (eds.), *Philosophical Problems of the Internal and External World: Essays on the Philosophy of A.* *Grünbaum*, Pittsburgh: University of Pittsburgh Press, pp. 329–370.

[^worrall-1996]: –––, 1996, “‘Revolution in Permanence’: Popper on Theory-Change in Science”, in A. O’Hear (ed.), *Karl Popper: Philosophy and Problems*, Cambridge: Cambridge University Press, pp. 75–102.

[^worrall-2010]: –––, 2010, “Evidence: Philosophy of Science Meets Medicine”, *Journal of Evaluation in Clinical Practice*, 16: 356–362.

[^zabell-2011]: Zabell, S., 2011, “Carnap and the Logic of Induction”, in Gabbay, Hartmann, and Woods, 2011, pp. 265–310.

[^zahar-1973]: Zahar, E., 1973, “Why Did Einstein’s Programme Supersede Lorentz’s?”, *British Journal for the Philosophy of Science*, 24: 95–123, 223–262.

[^zellner-2002]: Zellner, A., H. Keuzenkamp, and M. McAleer (eds.), 2002, *Simplicity, Inference, and Modelling: Keeping It Sophisticatedly Simple*, Cambridge: Cambridge University Press.
