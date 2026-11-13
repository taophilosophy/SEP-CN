# Disjunction
**First published Wed Mar 23, 2016; substantive revision Wed Oct 30, 2024**

*Aloni, Maria*

In logic, disjunction is a binary connective ($\vee$) classically interpreted as a truth function the output of which is true if at least one of the input sentences (disjuncts) is true, and false otherwise. Its supposed connection with disjunctive words of natural language like *or* has long intrigued philosophers, logicians and linguists. In this entry we give an overview of logical and linguistic analyses of disjunction with focus on developments at the interface between logic and language. Sections 1 and 2 present disjunction as a binary connective in classical logic and in a number of non-classical interpretations. Section 3 discusses some basic facts concerning disjunctive words in natural language, and introduces a generalized, cross-categorial notion of disjunction as the *join* operator in a (Boolean) algebra. Section 4 and 5 present Grice’s account of the use of *or* in conversation and recent developments in the discussion on inclusive and exclusive uses of linguistic disjunctive words. Finally, sections 6 and 7 introduce recent non-classical accounts of linguistic disjunction and discuss applications to phenomena of free choice, disjunctive questions and counterfactuals with disjunctive antecedents.

## 1. Disjunction in classical logic

In classical logic, disjunction ($\vee$) is a binary sentential operator whose interpretation is given by the following truth table:

**(1)**

Disjunction in classical logic

| $\phi$ | $\psi$ | $(\phi \vee \psi)$ |
| --- | --- | --- |
| 1 | 1 | 1 |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 0 | 0 | 0 |

A disjunction $(\phi \vee \psi)$ is true iff at least one of the disjuncts is true.

Adopting a natural deduction system, the proof-theoretical contribution of disjunctive formulas can be defined by the following two rules, which regulate (i) how disjunctions can be drawn as conclusions (disjunction introduction rule, $I_{\vee}$, also known as *addition*) and (ii) how conclusions can be drawn from disjunctions (disjunction elimination rule, $E_{\vee}$, also known as *reasoning by cases*):

**(2)**

Disjunction introduction ($I_{\vee}$)

$$ \begin{prooftree} \AxiomC{\(\phi\)} \RightLabel{\(I_{\vee}^R\)} \UnaryInfC{\((\phi \vee \psi)\)} \end{prooftree} \qquad \begin{prooftree} \AxiomC{\(\psi\)} \RightLabel{\(I_{\vee}^L\)} \UnaryInfC{\((\phi \vee \psi)\)} \end{prooftree} $$

**(3)**

Disjunction elimination ($E_{\vee}$)

$$ \begin{prooftree} \AxiomC{\((\phi \vee \psi)\)} \alwaysNoLine \AxiomC{\([\phi]\)} \UnaryInfC{\(\vdots\)} \UnaryInfC{\(\theta\)} \AxiomC{\([\psi]\)} \UnaryInfC{\(\vdots\)} \UnaryInfC{\(\theta\)} \singleLine \RightLabel{\(E_{\vee}\)} \TrinaryInfC{\(\theta\)} \end{prooftree} $$

Intuitively, the former tells us that we can conclude $(\phi \vee \psi)$ on the basis of $\phi$ (or of $\psi$), while the latter states that $\theta$ can be derived from a disjunction $(\phi \vee \psi)$ if it can be derived from $\phi$ and also from $\psi$.

One of the goals of a logical system is to arrive at a rigorous characterization of the notion of validity. In a logical system, which normally consists of a language, a proof-theory and a model-theory, validity can be defined proof-theoretically or model-theoretically. Proof-theoretically, validity is defined in terms of formal proofs. An argument is proof-theoretically valid ($\vdash$) if there is a proof from some or all of its premises to its conclusion. Model-theoretically (or semantically), validity is normally defined in terms of the preservation of truth in a model. An argument is model-theoretically valid ($\models$) if there is no model in which its premises are all true and its conclusion false. In classical logic, the proof-theoretical and the model-theoretical perspectives have been proven to characterize exactly the same notion of validity (*soundness and completeness theorems*): an argument is proof-theoretically valid iff it is model-theoretically valid.

Below are some of the principles involving disjunction that classical logic validates. In the list we adopt the model-theoretic notation ($\models$) because such perspective will be more prominent in the following section. $\models \phi$ means $\phi$ is true in all models. The last two principles in the list are model-theoretic analogues of disjunction introduction and elimination, respectively.

$$\begin{align} & \models (\phi \vee \neg \phi) & \text{(law of excluded middle)} \\ & \models \neg (\phi \wedge \psi) \leftrightarrow (\neg \phi \vee \neg \psi) & \text{(De Morgan laws)} \\ & \models \neg (\phi \vee \psi) \leftrightarrow (\neg \phi \wedge \neg \psi) & \\ & \models \phi \wedge (\psi_1 \vee \psi_2) \leftrightarrow (\phi \wedge \psi_1) \vee (\phi \wedge \psi_2) & \text{(distributive laws)} \\ & \models \phi \vee (\psi_1 \wedge \psi_2) \leftrightarrow (\phi \vee \psi_1) \wedge (\phi \vee \psi_2) & \\ & (\phi \vee \psi), \neg \phi \models \psi & \text{(disjunctive syllogism)} \\ & \phi \models (\phi \vee \psi), \quad \psi \models (\phi \vee \psi) & \text{(addition)} \\ & \Gamma, \phi \models \theta \ \ \& \ \ \Gamma, \psi \models \theta \ \ \Rightarrow \ \ \Gamma, (\phi \vee \psi) \models \theta & \text{(reasoning by cases)} \end{align}$$

These principles have been widely discussed and, at times, rejected in the logical-philosophical literature. The following section briefly summarizes parts of these discussions focusing on which alternative interpretation of $\vee$ these discussions have led to.

Before proceeding a note on the origin of the symbol '$\vee$'. As documented in Elkind and Zach (2023), the first known use of a $\vee$-like symbol for expressing disjunctive-like meaning is in a manuscript by Leibniz (Leibniz 1679)[^leibniz-1679], where $\vcap$ is used arguably as an abbreviation of *vel*, the Latin word for *or*. Elkind and Zach however stress that Leibniz does not seem to use the symbol as a sign for propositional disjunction but rather as an operation producing ambiguously referring (non-propositional) terms, as in his example $3 \pm \sqrt{4}= 5 \vcap 1$. According to Elkind and Zach, the $\vee$ symbol originated instead in pre-*Principia* works of Russell and Whitehead (Russell 1903a, 1903b, 1906; Whitehead 1903)[^russell-1903a][^russell-1903b][^russell-1906][^whitehead-1903] and was introduced as a modification of Peano's '$\cup$' (Peano, 1888)[^peano-1888] to separate notations for propositional disjunction and class union. Peano had adopted '$\cup$' for (logical) union and disjunction to avoid the '$+$' from the algebraic tradition (first introduced by Boole and used by Peirce and Schröder), in order to clearly distinguish logical symbols from mathematical ones. Russell and Whitehead's use of '$\vee$' in the *Principia*, where disjunction is one of the primitive notions, and its later adoption by Hilbert and his students (Hilbert 1923; Hilbert and Ackermann 1928)[^hilbert-1923][^hilbert-1928] arguably led to today's wide acceptance of the symbol.

## 2. Non-classical variations

### 2.1 Law of excluded middle and the principle of bivalence

The law of excluded middle (LEM) states that any proposition of the form $(\phi \vee \neg \phi)$ is logically valid. The semantic principle of bivalence states that every proposition is either true or false (and not both). Bivalence and LEM collapse in classical logic, but are distinguished for example in supervaluationism (van Fraassen 1966)[^fraassen-1966], which rejects the former, while retaining the latter. Since Aristotle, who was the first to state these principles, bivalence and LEM have been criticized on various grounds. This section first discusses intuitionistic logic, which invalidates LEM (and part of the De Morgan laws); and then presents some canonical arguments against bivalence and discuss how $\vee$ is interpreted in a number of non-bivalent systems including many-valued logic, dynamic semantics, supervaluationism, as well as quantum logic, which besides bivalence also invalidates the classical distributive laws.

#### 2.1.1 Disjunction in intuitionistic logic

LEM has been rejected in constructivism, in particular in intuitionistic logic (see the entry on intuitionistic logic). The standard informal interpretation of logical operators in intuitionistic logic is the so-called proof-interpretation or Brouwer-Heyting-Kolmogorov (BHK). On such interpretation the meaning of a statement $\phi$ is given by explaining what constitutes a proof of $\phi$ rather than in terms of its truth. The BHK interpretation of disjunction reads as follows:

**(4)**

A proof of $(\phi\vee \psi)$ consists of a proof of $\phi$ or a proof of $\psi$.

On such interpretation, the question concerning the validity of LEM is then equivalent to the question of the possibility of unsolvable (mathematical) problems (Brouwer 1908, translated in Heyting (ed) 1975): LEM should then fail because it is doubtful that for any mathematical statement $\phi$, either there is a proof of $\phi$ or a proof of $\neg \phi$.[^note-1]

Related to its rejection of LEM, intuitionistic logic satisfies the *disjunction property* (Gödel 1932)[^gödel-1932]. A logic is said to have the disjunction property if whenever $(\phi \vee \psi)$ is provable in the logic, so is at least one of $\phi$ and $\psi$. Classical logic does not have such property ($\vdash_{CL} (p \vee \neg p)$, without $\vdash_{CL} p $ or $\vdash_{CL} \neg p$) but has a weaker property called *Halldén-completeness*: every provable disjunction whose disjuncts don’t share any propositional variables has at least one of those disjuncts provable.

The rejection of LEM in intuitionistic logic also implies the rejection of classical *reductio ad absurdum* as a legitimate method of (mathematical) proof. Intuitionistically, *ad absurdum* one can only prove negative statements (via negation introduction $ \Gamma, \phi \vdash \bot \ \Rightarrow \ \Gamma \vdash \neg \phi$). This is because double negation elimination ($\neg \neg \phi \vdash \phi$) does not hold in intuitionistic logic. If it did, LEM would follow from the intuitionistically provable $\neg \neg (\phi \vee \neg \phi)$ (in general it holds that if $\phi$ is classically provable, then $\neg\neg \phi$ is intuitionistically provable).

Finally note that only one of the De Morgan laws is intuitionistically provable, of the other only one half still holds:

- $\vdash_{IT} (\neg \phi \wedge \neg \psi) \leftrightarrow \neg (\phi \vee \psi)$ (De Morgan laws)
- $\vdash_{IT} (\neg \phi \vee \neg \psi) \to \neg (\phi \wedge \psi) $, but $\not\vdash_{IT} \neg (\phi \wedge \psi) \to (\neg \phi \vee \neg \psi)$

Intuitively, $ \neg (\phi \wedge \psi) $ intuitionistically asserts that an effective method has been given, which would convert any proof of $(\phi \wedge \psi)$ into a proof of a contradiction. But this does not imply that either a proof of $\neg \phi$ (i.e., an algorithm which would convert any proof of $\phi$ into a proof of a contradiction) or a proof of $\neg \psi$ has been given, which is what $(\neg \phi \vee \neg \psi)$ intuitionistically asserts.

#### 2.1.2 Disjunction in multi-valued logics

The semantic principle of bivalence states that every proposition is either true or false (and not both). Early arguments against bivalence were linked to the problem of determinism. In *De Interpretatione* (part 9), Aristotle discusses the status of statements about contingent future events, and seems to conclude that for these statements the principle of bivalence should be rejected, otherwise determinism would follow. His argument can be reconstructed as follows. Consider the statement *A sea battle will be fought tomorrow*. If the statement is true, then the sea battle will necessarily take place. If the sentence is false, then it will be impossible for the sea battle to take place. Assuming that statements are either true or false, one concludes that the sea battle is either necessary or impossible. To escape this fatalistic conclusion Aristotle rejects the principle of bivalence (while possibly retaining the law of excluded middle, see van Fraassen 1966: 493–495, and the entry on fatalism)[^fraassen-1966]. Aristotle’s sea battle argument, although criticized by many, constituted one of Łukasiewicz’ original motivations for the development of his trivalent logic (Łukasiewicz 1920, translated in McCall 1967)[^mccall-1967]. Since then various multi-valued logics have been developed where formal disjunction $\vee$ receives a non-classical interpretation. In Łukasiewicz’ original system, but also in strong Kleene three-valued logic (Kleene 1952)[^kleene-1952], disjunction is interpreted according to the following truth table, where # stands for *indefinite* or *possible* in Łukasiewicz, and for *undefined* in Kleene (Łukasiewicz’s and Kleene’s system differ in their interpretation of implication, we will disregard this issue here). Priest’s (1979) Logic of Paradox (LP) also adopts the following table for disjunction. There # should be read as *both true and false*:

**(5)**

Disjunction in strong Kleene logic

| $\vee_s $ | 1 | # | 0 |
| --- | --- | --- | --- |
| 1 | 1 | 1 | 1 |
| # | 1 | # | # |
| 0 | 1 | # | 0 |

On this interpretation, a disjunction is true if at least one of the disjuncts is true, false if both disjuncts are false, undefined otherwise.

In Bochvar’s internal three-valued logic, also known as Kleene’s weak three-valued logic, disjunction receives a different interpretation. The symbol # should be read here as *meaningless*:

**(6)**

Disjunction in weak Kleene logic

| $\vee_w$ | 1 | # | 0 |
| --- | --- | --- | --- |
| 1 | 1 | # | 1 |
| # | # | # | # |
| 0 | 1 | # | 0 |

While on a strong Kleene interpretation, a disjunction can be true even if one of the disjuncts is undefined, on a weak Kleene interpretation, if one of the disjuncts is meaningless, the whole disjunction is meaningless as well.

Negation receives the following interpretation in these systems:

**(7)**

Negation in strong and weak Kleene logic

| $\neg $ |   |
| --- | --- |
| 1 | 0 |
| # | # |
| 0 | 1 |

In both strong and weak Kleene logics then, $(\phi \vee \neg \phi)$ never has value $0$, but it doesn’t always have value $1$ either: if $\phi$ is assigned value #, so is its negation, but then $(\phi \vee \neg \phi)$ will also have value # on both the strong and weak interpretations of $\vee$. Thus $(\phi \vee \neg \phi)$ fails to be logically valid in these systems (unless both $1$ and # are taken to be designated values, as in Priest’s LP, which validates LEM. Priest’s notion of validity is defined later in this section). Other many-valued logics, such as the Łukasiewicz continuum-valued logic, also fail to validate LEM, for similar reasons. In continuum-valued logic, the set of truth values is the set of real numbers between $0$ and $1$, where $1$ stands for completely true, $0$ for completely false, $0.5$ for half true, etc. Disjunction and negation are analyzed as $F_{\vee}(x, y)=max(x,y) $ and $F_{\neg} (x)= 1-x$ respectively, where $max$ means “the maximum of”. But then since $max(x, 1-x)$ need not be equal to $1$, $(\phi \vee \neg \phi)$ can fail to be completely true in this system.

The difference between the strong and weak Kleene’s treatment of disjunction can be better appreciated by looking at the phenomenon of presupposition, which constitutes one of the most well-known linguistic motivations for the rejection of bivalence (other common motivating phenomena include empty names, the semantic paradoxes and vagueness, see the entries on names, liar paradox and sorites paradox, and section 2.1.4 below). Consider Russell’s (1905) example:

**(8)**

The king of France is bald.

According to bivalence, (8) must be either true or false. Which is it? Russell’s answer is well known. According to his theory of descriptions (8) expresses the conjunction “there is a unique king of France and he is bald” of which the first conjunct is false, and therefore the whole sentence is false. Strawson (1950) however criticized Russell’s analysis and argued that the existence and uniqueness of the king of France is not part of what is asserted by an utterance of (8) rather it is part of what is taken for granted or *presupposed*. If there is no king of France, the sentence is not false, rather it is neither true nor false. Adopting a three-valued logic we can assign to (8) value #. Consider now the following three examples where (8) occurs in a disjunction.

**(9)**

Either the king of France is bald or the king of France is not bald.

**(10)**

Either there is no king of France or the king of France is bald.

**(11)**

Either Barack Obama is tall or the king of France is bald.

Both strong and weak Kleene systems predict (9) to be undefined/meaningless, since both disjuncts are undefined/meaningless. However, the predictions of the two systems with respect to (10) and (11) diverge: the strong Kleene system predicts both (10) and (11) to be true since at least one of the disjuncts is true (assuming Barack Obama is in fact tall), while the weak system predicts both (10) and (11) to be meaningless since at least one of the disjuncts is meaningless. Intuitively, however, (10) is true while (11) is more readily judged as undefined/meaningless. Thus the predictions of neither systems are in agreement with common sense judgments. Linguists have observed that the intuitive difference between (10) and (11) is that in the former, but not in the latter the existence of a unique king of France (the presupposition of one of the disjuncts) is entailed by the negation of the other disjunct. Karttunen (1973), who systematically studied the projection behavior of presuppositions (i.e., how the presupposition of a constituent projects at the level of the complex sentence), described disjunction as a *filter*. In his taxonomy of embedding operators, *plugs* block all presuppositions in their scope (an example is *told that*: *I was told that the king of France is bald* does not imply that there is a king of France), *holes* allow presupposition to project freely (e.g., negation: *I didn't see the king of France* does imply that there is a king of France), while *filters* allow only some presuppositions to project (e.g., implication: *If everybody wears a wig, then the king of France is bald* implies that there is a king of France, while *If France is a monarchy then the king of France is bald* doesn't; and conjunction: *Everybody wears a wig and the king of France is bald* implies that there is a king of France, while *France is a monarchy and the king of France is bald* doesn't). Thus implication, conjunction and disjunction are all examples of filters. Karttunen arrived at the following generalisation about their presupposition filtering conditions: In the case of implication, all presuppositions project (i.e., are not cancelled) except those triggered by the consequent and semantically entailed by the antecedent. In the case of conjunction, all presuppositions project except those triggered by the second conjunct and semantically entailed by the first conjunct. In the case of disjunction, all presuppositions project except those triggered by the second disjunct and entailed by the *negation* of the first disjunct. Various analyses have been proposed attempting to capture Karttunen's generalisation. A prominent example is Peters (1979), who showed how Karttunen’s observations can be accounted for within a multi-valued logic with special non-symmetric connectives (see the entry on presupposition for an overview).

#### 2.1.3 Disjunction in dynamic semantics

Another influential attempt to formalize Karttunen’s generalization with respect to presupposition projection, is the dynamic account of Heim (1983), further developed in Beaver (2001). In a dynamic semantics, the interpretation of sentences is given in terms of their context change potentials rather than their truth conditions (see the entry on dynamic semantics). A context (or information state) $c$ is defined as a set of possible worlds, the worlds compatible with the information available to the conversationalists, along the lines of Stalnaker’s (1978) notion of a context set. The meaning of an atomic sentence $p$ is identified with its potential to update the input context $c$, i.e., its potential to eliminate all non-$p$ worlds from $c$: $c[p]=\{w \in c \mid w(p) =1\}$. Here is the dynamic clause for disjunction.

**(12)**

Disjunction in dynamic semantics

$$ c[(\phi \vee \psi)] = c [\phi] \cup (c \setminus c [\phi])[\psi] $$

The result of updating a context $c$ with a disjunction $(\phi \vee \psi)$ consists in the union of (i) the result of updating $c$ with $\phi$ and (ii) the result of updating with $\psi$ the context $c \setminus c [\phi]$ obtained by subtracting from $c$ all worlds which survive after an update with $\phi$. By defining the presupposition of a sentence as what has to be true (or supported) in a context $c$ in order for an update with the sentence to be defined in $c$, the dynamic account of disjunction captures the pattern in (9)–(11). Simplifying, suppose $c$ does not support the information that there is a king of France, then (9) and (11) will be undefined in $c$, because $c [\phi]$ and/or $(c \setminus c [\phi])[\psi]$ will be undefined. But (10) will be defined. This is because the second disjunct in (10), which presupposes that there is a king of France, is interpreted here with respect to the local context $(c \setminus c [\phi])$ which is the context obtained by subtracting from $c$ all worlds which verify the first disjunct, i.e., all worlds in which there is no king of France. Such local context will support the information that there is a king of France. So the whole disjunction does not presuppose anything. The ordering between disjuncts however matters in a dynamic account and so the analysis predicts a difference in presupposition between (10) and the following variant where the presupposition trigger occurs in the first disjunct rather than the second:

**(13)**

Either the king of France is bald or there is no king of France.

This prediction however does not seem to be borne out.

A related discussion concerns the behavior of anaphora in the context of disjunction and in particular the challenge presented by the so-called “bathroom” example (14) from Barbara Partee, where the anaphoric pronoun *it* in the second disjunct refers back to the negative indefinite *no bathroom* in the first disjunct, while negative indefinites are normally inaccessible to subsequent pronouns as illustrated in (15):

**(14)**

Either there is no bathroom in the house, or it is in a funny place.

**(15)**

There is no bathroom in the house. # It is in a funny place.

The contrast between (14) and (15) seems to provide evidence for the analysis of disjunction presented in (12) according to which the second disjunct must be interpreted with respect to a context supporting the negation of the first disjunct (so a context supporting the information that there is a bathroom in the house). Note however that “double negation is not in general eliminable” in standard dynamic semantics for anaphora ($\neg \neg \exists x \phi \not\simeq \exists x \phi$, where $\simeq$ is defined as mutual meaning inclusion, because the two formulas have different dynamic potential, Groenendijk and Stokhof 1991: 22)[^groenendijk-1991]. Therefore a full account of these examples requires some adjustment. Various solutions have been proposed (e.g., Simons 1996)[^simons-1996], but the discussion about anaphora (and presupposition projection) in disjunctions has not been settled yet.

It is easy to see that a dynamic semantics with presuppositions does not validate LEM, because, if $\phi$ contains a presupposition trigger (i.e., an expression like “the king of France” which gives rise to a presupposition), $(\phi \vee \neg \phi)$ will be undefined in any context in which the presuppositions of $\phi$ are not satisfied. For the fragment without presuppositions, however, LEM is validated, but there is a non-trivial sense in which bivalence is still rejected: truth and falsity in dynamic semantics are defined relative to a context, for example, $\phi$ is true (or supported) in $c$ iff $c[\phi]=c$; and $\phi$ is false in $c$ iff $c[\phi]=\emptyset$. But then $p$ might be neither true nor false in a context $c$ (e.g., if $c$ contains both $p$ worlds and non-$p$ worlds), while, for all $ c$, it holds that $(p \vee \neg p)$ is true in $c$.

#### 2.1.4 Disjunction in supervaluationism

Another system which rejects bivalence while validating LEM is supervaluationism (van Fraassen 1966)[^fraassen-1966]. Let $V$ be a set of classical valuations $v$, where a classical valuation is a function assigning T(rue) or F(alse) to any statement in the relevant language. A supervaluation $s_V$ is then a function assigning T (F) to exactly those statements assigned T (F) by all valuations in $V$. Since $V$ can contain classical valuations that assign different values to one and the same statement (e.g., if $v_1(p)$=T and $v_2(p)=$F for $v_1,v_2 \in V$), supervaluations have truth-value gaps ($s_V(p)$ is undefined), so the law of bivalence fails. LEM, by contrast, is validated, since $v(\phi \vee \neg \phi)$=T for all $\phi$ and classical $v$, and thus $s_V(\phi \vee \neg \phi)$ = T, for any $s_V$. Thus, in supervaluationism, a disjunction can be supertrue (i.e., can be assigned T in some $s_V$) without any of its disjuncts being supertrue.

Supervaluational semantics has been largely applied to explain phenomena of vagueness (Lewis 1970; Fine 1975b; Kamp 1975; see also the entry on vagueness)[^fine-1975b][^kamp-1975][^lewis-1970]. A predicate $P$ is vague if it exhibits borderline cases for which it is not clear whether $P$ truly applies or not. Prominent examples of vague predicates are relative adjectives like *tall* or *clever*, while adjectives like *prime* as in *3 is a prime number* are normally taken not to be vague. The basic insight of any supervaluational account of vagueness is that a vague language admits of several precisifications (formalized as a set $V$ of classical valuations) and the semantic value of a statement is fixed only insofar as all those precisifications agree: a statement $\phi$ is true if it is supertrue ($s_V(\phi)=T$), that is, true on every admissible precisification ($v(\phi)=T$, for all $v\in V$), and it is false if it is superfalse ($s_V(\phi)=F$), that is, false on every admissible precisification ($v(\phi)=F$, for all $v\in V$); otherwise it has no semantic value. A common argument in favor of supervaluationism relies on the observation that while a predicate like *tall* may be vague, the compound predicates *tall or not tall* and *tall and not tall* are not vague, the former being true and the latter being false of all entities in the predicate application domain. Thus, while *$a$ is tall* may fail to be true or false (and the same goes for its negation), *$a$ is either tall or not tall* and *$a$ is tall and not tall* are always true and false respectively, as predicted by a supervaluational semantics. More recent experimental work, however, has cast some doubts on these observations (e.g., Ripley 2011)[^ripley-2011]. Supervaluationism has further been criticized for giving rise to counterexamples to familiar inference-patterns (Williamson 1994: 151–152 and 162–163)[^williamson-1994], (see also Keefe 2000; Williams 2008 for further discussion)[^keefe-2000][^williams-2008]. For example, it is easy to see that in this framework, one loses the disjunction elimination rule, at least in languages with a determinately/supertrue operator $D$, where $D \phi$ is true iff $\phi$ is supertrue (more precisely, for every classical $v \in V$, $v(D \phi)=T$ iff $s_V(\phi)=T$). Defining supervalidity, $\models_{sv}$, in terms of preservation of supertruth, we have that $p \models_{sv} D p$, $\neg p \models_{sv} D \neg p$ and $\models_{sv} p \vee \neg p$, but $\not\models_{sv} Dp \vee D \neg p$. So the disjunction elimination rule does not preserve supervalidity in this language (see also Humberstone, chapter 6, pages 830–833). Whether supervalidity is the right notion of validity from a supervaluational perspective is however controversial (e.g., Varzi 2007)[^varzi-2007].

#### 2.1.5 Disjunction in quantum logic

Other logics that lack bivalence are quantum logics, which also typically reject the distributive laws of classical logic (Birkhoff and von Neumann 1936; Putnam 1968)[^birkhoff-1936][^putnam-1968]. Quantum logics were first developed by Birkoff and von Neumann for studying the relation among physical observables in quantum physics. Quantum logics reject bivalence because a state in a quantum system typically assigns probability values to experimental propositions rather than plain true or false. To see why quantum physics can be taken to provide evidence against the distributive laws of classical logic consider a particle moving on a line. Suppose $p$ asserts that the particle’s momentum is within a certain interval, while $q$ and $r$ assert that the particle’s position is in the intervals $\alpha$ and $\beta$ respectively. Suppose the statement $p \wedge (q \vee r)$ is confirmed by our observation, so is true (or has value 1). By the distributive laws we can classically conclude $(p \wedge q) \vee (p \wedge r)$. But in quantum theory the latter might still be false (have value 0), since both conjunctions $(p \wedge q)$ and $(p \wedge r)$ might assert tighter restrictions on simultaneous values of position and momentum than is allowed by Heisenberg’s uncertainty principle (see the entry on the uncertainty principle). So in the “logic of quantum physics” a disjunction $(q \vee r)$ can have value 1 in a state without any of the disjuncts having value 1: if $q$ has value 1 or $r$ has value 1, then $(q \vee r)$ has value 1, but the other direction fails.

Various ways have been proposed to develop a quantum logic which rejects the distributive laws while saving as much as possible of classical logic. One way discussed by Dummett (1978) (who was not a proponent of quantum logic) involves restricting the elimination rule for disjunction so that the distributive laws are no longer derivable (see Humberstone 2011: 298–302 and 918–922 for more details)[^humberstone-2011]. Arguably more natural characterizations of quantum logic use algebraic semantics and probability theory (see the entry quantum logic and probability theory).

### 2.2 Disjunctive syllogism and addition

Disjunctive Syllogism (DS) states that we can infer $\psi$ from $ (\phi \vee \psi) $ and $\neg \phi$. In a story reported by Sextus Empiricus, Chrysippo attributed to a dog the ability to apply DS “when arriving at a juncture of three paths, after sniffing at the two down which the quarry did not go, he rushes off on the third without stopping to sniff.” (Sextus Empiricus, Outlines of Pyrrhonism, I.69). DS, which is valid in classical logic, but also in intuitionistic logic and in the multi-valued logics discussed in the previous section (with the exception of Priest's LP), has however been rejected in relevance logics (Anderson and Belnap 1962, 1975)[^anderson-1962][^anderson-1975]. Relevance logics are non-classical logical systems developed to avoid the paradoxes of material and strict implication (see the entry on relevance logic). These are classically valid principles, like $p \to (q \vee \neg q)$, which however strike us as counterintuitive. This is so because, according to the relevantist, they involve a fallacy of relevance: in these cases the antecedent is typically irrelevant to the consequent. Belnap’s formal criteria of relevance (also known as variable sharing principle) is that in any provable implication, the antecedent and the consequent should share at least one propositional variable, and that no inference can be shown valid if the premises and conclusion do not share at least one propositional variable.

Historically, relevance logic rejected DS because of the role it plays in C.I. Lewis “independent” proof of the fact that an impossible proposition $(A \wedge \neg A)$ can lead to any proposition whatsoever, which is one of the paradoxes of strict implication:

| 1. | $(A \wedge \neg A)$ | [assumption] |
| --- | --- | --- |
| 2. | $ A$ | [from 1, by $E_{\wedge}$] |
| 3. | $\neg A$ | [from 1, by $E_{\wedge}$] |
| 4. | $(A \vee B)$ | [from 2, by $I_{\vee}$, or addition] |
| 5. | $B$ | [from 3,4 by disjunctive syllogism] |

According to Anderson and Belnap “the inference from $\neg A$ and $A\vee B$ to $B$ is an error: […] a fallacy of relevance” (Anderson and Belnap 1962: 19)[^anderson-1962]. Formally, the inference is rejected because according to Anderson and Belnap’s notion of tautological entailment (see their system E) $\neg A \wedge (A\vee B)$ entails $B$ if and only if $(\neg A \wedge A) \vee (\neg A \wedge B)$ entails $B$, only if $(\neg A \wedge A)$ entails $B$, which fails since the premise $(\neg A \wedge A)$ is not relevant to the conclusion $B$ (no shared propositional variables). Anderson and Belnap further argued that we can still have a version of disjunctive syllogism involving an intensional notion of disjunction $\vee_i$, for which addition wouldn’t hold. Intensional disjunction is defined as follows: $(A\vee_i B):= (\neg A \to_i B) $, where $\to_i$ is an intensional implicational connective, i.e., one satisfying the formal criterion of relevance introduced above. The English *or* would then be ambiguous between intensional and extensional (truth-functional) disjunction, and only for the latter would addition hold. Intuitively, the intensional variety of *or* would be one requiring “relevance” between the disjuncts. On the intensional reading, “$A$ or $B$” would entail that $A$ and $B$ are so related that we are entitled to say “If $A$ had not been true, $B$ would have been true” or “If $B$ had not been true, $A$ would have been true” or the like. A disjunction like *Either Napoleon was born in Corsica or else the number of the beast is perfect* clearly fails to have this property and therefore is of the truth-functional kind. Whereas *That is either Drosophilia Melanogaster or D. virilis, I’m not sure which* appears to entail that if it is not the one then it is the other, and thus is of the intensional kind. The distinction between intensional and extensional disjunction has been criticized by various scholars, including Burgess (1981, 1983), but has been defended by Read (1981, 1983) who proposed the following example as a clear case of truth-functional disjunction, for which addition is valid: *You qualify for a grant if either you are over 65 or you earn less than 2000 pounds a year* (Read 1981: 68)[^read-1981]. Now if English *or* had an intensional and an extensional sense, it should be possible to find both in a large variety of linguistic contexts. On a closer inspection however it appears that it is quite hard to find clear cases of intensional disjunction in embedded positions like in the antecedent of a conditional (as in Read’s example), or under negation. For example, *That is not Drosophilia Melanogaster or D. virilisit*, on its most natural reading, simply means that that is not either, but then *or* must be extensional here because to derive “not $A$ and not $B$” from “not ($A$ or $B$)” addition is needed. This seems to suggest that phenomena of relevance should be captured on a pragmatic level rather than on the level of logic (Grice 1989)[^grice-1989]. An explicit Gricean account of relevance of disjunctive sentences has been indeed proposed by Simons (2001), who observes that felicitous utterances of “$A$ or $B$” require the disjuncts to be relevant alternatives, and argues that such condition, which she calls the relatedness condition, can be derived from general principles of conversation interacting with truth functional interpretation of *or*. In “Further Notes on Logic and Conversation” Grice had suggested that to felicitously use a disjunctive sentence “$A$ or $B$”, a speaker must be in possession of a reasonable argument with “$A$ or $B$” as conclusion [by Quality] which does not contain one of the disjuncts as a step [by Quantity] (Grice 1989: 44)[^grice-1989]. According to Simons to arrive at such a kind of evidence is almost certainly impossible in case the disjuncts are not (contextually) related to each other (as they were for example in Belnap and Anderson’s Napoleon example, which indeed requires a special context to be acceptable). Simons (2001) also discusses a second requirement that a disjunction needs to satisfy in order to constitute a felicitous contribution to an ordinary conversation, namely what she calls the distinctness condition (aka known as Hurford’s constraint, from Hurford 1974)[^hurford-1974], which states that the disjuncts in a clausal disjunction must be distinct alternatives. The following, which does not satisfy such a constraint since one of the disjunct entails the other, is indeed highly anomalous (Simons 2001: example (2)):

**(16)**

Either there is dirt in the fuel line or there is something in the fuel line.

Hurford’s constraint has more recently received some attention in the semantic/pragmatic literature because of its role in the debate between localist and globalist analysis of scalar implicatures (e.g., Chierchia, Fox, and Spector 2012)[^chierchia-2012].

Disjunctive syllogism is also invalid (or better quasi-valid) in Priest’s Logic of Paradox (LP). In LP both $1$ and $\#$ are designated values (i.e., preserved in valid inferences), where # stands for both true and false. More formally, validity is defined as follows: $\Sigma \models \phi$ iff there is no valuation $v$ such that for all $\psi \in \Sigma: v(\psi) = 1$ or # and $v(\phi) =0$. Adopting the strong Kleene tables for disjunction and negation presented above, we obtain that $\phi, (\neg \phi \vee \psi) \not\models \psi$, because $\phi$ and thus also $(\neg \phi \vee \psi)$ might be both true and false, while $\psi$ is false. The schema $\phi , (\neg \phi \vee \psi) \models \psi$ however only fails in case $\phi$ is a *dialetheia* (both true and false), in this sense is the scheme quasi-valid. Priest (2006: ch. 8) then argues that applications of disjunctive syllogism can be justified/are reasonable in case $(\phi \wedge \neg \phi)$ is rationally rejectable.

We conclude this section with a final remark on addition, which according to Anderson and Belnap does not hold for intensional disjunction. The validity of addition has also been disputed in relation to imperative logic. We don’t seem to be able to conclude (18) from (17) (Ross’ (1941) paradox):

**(17)**

Post this letter!

**(18)**

Post this letter or burn it!

One way to tackle this would be to treat *or* in (18) as a case of intensional disjunction. This solution however would fail to account for a characteristic aspect of the interpretation of disjunctive imperatives which arguably explains the failure of addition in these cases, namely their choice offering potential. The most natural interpretation of disjunctive imperatives is as one presenting a choice between different actions: (18) implies that you may post the letter and you may burn it (a free choice inference). Imperative (17) then cannot imply (18) otherwise when told the former one would be justified in burning the letter rather than posting it (e.g., Mastop 2005; Aloni 2007; Aloni and Ciardelli 2013)[^aloni-2007][^aloni-2013][^aloni-2013-2][^mastop-2005]. More on free choice in section 6.

## 3. Disjunction in language

From a linguistic point of view disjunction is a kind of coordination, where coordination refers to syntactic constructions in which two or more units of the same type are combined into a larger unit and still have the same semantic relations with other surrounding elements (Haspelmath 2007)[^haspelmath-2007]. An open question is whether disjunctive coordination is a universal that can be found in all languages. All languages appear to possess coordination constructions of some kind, but not all languages seem to have explicit coordinators like *and* and *or*. For example, Maricopa (a Yuman language of Arizona described by Gill 1991)[^gil-1991] and Dyribal (an Australian Aboriginal language described by Dixon 1972)[^dixon-1972] seem to lack explicit coordination structures, so in these languages there is no word corresponding to *or* (see also Winter 1995)[^winter-1995]. This does not necessarily mean however that these languages lack a way to express disjunctive meanings. Maricopa and Dyribal appear to be able to convey “$A$ or $B$”, without explicit disjunctive coordinator, by adding a suffix/particle expressing uncertainty to the main verb. (19) illustrates this strategy for Maricopa (from Gil 1991: 102)[^gil-1991]:

**(19)**

Johnš John-nom Billš Bill-nom v^{ɂ}aawuumšaa. 3-come-pl-fut-infer ‘John or Bill will come’

That it is the “uncertainty” suffix *šaa* which is responsible for the disjunctive interpretation is evidenced by the fact that if omitted the interpretation of the sentence becomes conjunctive (Gil 1991)[^gil-1991]. The close connection between linguistic disjunction and uncertainty (or ignorance) will be further scrutinized in the following sections. Let us now turn to languages which do have specialized disjunctive words like *or*. A first difference between logical disjunction ($\vee$) and disjunctive words in human languages is that while the former is a binary operator, there is no theoretical finite limit to the number of units that the latter can join. Another striking difference is that while logical disjunction is a sentential operator, linguistic disjunction is typically cross-categorial. For example, English *or* can coordinate expressions of different syntactic category as illustrated below, where the units are noun phrases in (20) and verb phrases in (21):

**(20)**

John or Mary sang. ($\Leftrightarrow$ John sang or Mary sang)

**(21)**

Every man sang or danced. ($\not\Leftrightarrow$ every man sang or every man danced)

Adopting an algebraic perspective Keenan and Faltz (1985) showed that we can capture all these uses identifying disjunction with the join operator in a Boolean algebra (or, simplifying a bit, set union), see the entry on the mathematics of Boolean algebra. In the special case of disjunction at the sentence level, the Boolean operator boils down to the classical propositional operator on truth values (see section 7.1 for a recent account which identifies disjunction with the join operator in a Heyting algebra, which at the sentence level yields a non-classical (inquisitive) propositional operator). As an illustration consider the following interpretation of generalized, cross-categorial *or* in terms of generalized union, adapted from Gazdar (1980) (see also Winter 2001)[^winter-2001]. The crucial assumption behind this definition is that noun phrases like *John* or *every man* denote sets or functions rather than individuals (as in Montague 1973)[^montague-1973].

**(22)**

Generalized, cross-categorial disjunction

$$\lbrack\!\lbrack or\rbrack\!\rbrack = \sqcup_{\langle\tau,\tau \tau\rangle} =\left\{ \begin{array}{l l} \vee_{\langle t,tt\rangle} & \quad \mathrm{if } \ \tau=t \\ \lambda X_{\tau}\lambda Y_{\tau} \lambda Z_{\sigma_1}. X(Z) \sqcup_{\langle\sigma_2,\sigma_2 \sigma_2\rangle} Y(Z) & \quad \mathrm{if } \ \tau=\sigma_1 \sigma_2 \end{array} \right.$$

In the type-theoretical language adopted here each expression is assigned a type. Expressions $\alpha_t$ of type $t$ denote truth values; expressions $\alpha_e$ of type $e$ denote ordinary individuals; expressions $\alpha_{\langle e,t\rangle}$ of type $\langle e,t\rangle$ denote functions from individuals into truth values; and so on. Assume that (i) sentences denote truth values (type $t$); (ii) verb phrases (VPs) denote functions from individuals into truth values (type $\langle e,t\rangle$), and (iii) noun phrases denote functions from VP denotations into truth values (type $\langle\langle e,t\rangle, t\rangle$, shortened as $\langle e t, t\rangle$). Cross-categorial disjunction $\sqcup_{\langle\tau,\tau \tau\rangle}$ is of the generalised type $\langle\tau,\tau \tau\rangle$, where $\tau$ can be $t$, delivering sentential disjunction $\vee$ (of type $\langle t,\langle t,t\rangle \rangle$ shortened as $\langle t,tt\rangle$), but also other (functional) types, with $\tau=\langle e,t\rangle$ delivering VP disjunction (such as *sang or danced*), and $\tau=\langle et, t \rangle$ delivering noun phrase disjunction (such as *John or Mary*). Talking about characteristic functions as if they were sets, we have that *John* denotes the set of all John’s properties $[\lambda P_{\langle e,t\rangle}. P(j)]$, *Mary* denotes the set of all Mary’s properties $[\lambda P_{\langle e,t\rangle}. P(m)]$, and *sang* denotes the set of all individuals that sang $[\lambda x_e. S(x) \equiv S_{\langle e,t\rangle}]$. Given (22), *John or Mary* denotes the union of John’s properties with Mary’s properties, i.e., the set consisting of exactly those properties that pertain to either John or Mary $[\lambda Z_{\langle e,t \rangle}. \lambda P. P(j) (Z) \vee \lambda P. P(m)(Z)\ \equiv\ $$\lambda Z. Z(j) \vee Z(m)].$ So *John or Mary sang* will come out true just in case this union has as a member the property of singing $[\lambda Z. Z(j) \vee Z(m) (S) \equiv S(j) \vee S(m)]$. This is the case only if either John sang or Mary sang (see 23a). On the other hand, given (22), *sang or danced* denotes the union of the set of individuals that sang with the set of individuals that danced $[\lambda z_e. S(z) \vee D(z)]$. So every man sang or danced will come out true just in case this union is a member of the property-set denoted by every man $[\lambda P. \forall x (M(x) \to P(x)) (\lambda z_e. S(z) \vee D(z))\ \equiv\ $$\forall x (M(x) \to (S(x)\vee D(x)))]$. From this we cannot infer that either every man sang or every man danced (see 23b).

**(23)**

a. John or Mary sang. $\sing' \in \{ P \mid j\in P \} \cup \{ P \mid m\in P\}$ $\Leftrightarrow \sing' \in \{ P \mid j\in P $ or $ m\in P\}$ $\Leftrightarrow$ $ j\in \sing' \vee m\in \sing'$

**b.**

Every man sang or danced. $\sing' \cup \dance' \in \{ P \mid \man' \subseteq P\}$ $\Leftrightarrow \man' \subseteq \sing' \cup \dance'$ $\not\Leftrightarrow \man' \subseteq \sing' \vee \man' \subseteq \dance'$

One of the assumptions behind this cross-categorial analysis is that the input to the semantic component of grammar involves the units as coordinated at “surface structure” (i.e., no syntactic *conjunction reduction*, mapping non-sentential coordination to sentential coordination at “deep structure”). This is crucial for example to capture example (23b) where non-sentential disjunction could not be syntactically reduced to sentential disjunction without change of meaning. Rooth and Partee (1982) however discussed a number of counterexamples to such an analysis involving cases of wide-scope *or* in opaque contexts. Their famous example is repeated below (Rooth and Partee 1982: example (13)):

**(24)**

Mary is looking for a maid or a cook.

As Rooth and Partee observed the sentence has three readings: (i) the normal *de dicto* reading, according to which Mary would be satisfied if she found any maid and she would also be satisfied if she found any cook (this reading can be generated by combining the verb directly with the disjunctive noun phrase *a maid or a cook*); (ii) the normal *de re* reading according to which Mary is looking for a specific person and this person is either a maid or a cook (this reading can be generated by quantifying in the disjunctive noun phrase into the translation of the sentence *Mary is looking for him$_1$*); but also (iii) a wide scope *or* *de dicto* reading in which either Mary is looking for a maid, any maid, or she is looking for a cook, any cook, we don’t know which of the two. The latter reading cannot be generated by the standard Montagovian techniques. To capture these readings Rooth and Partee (1982) proposed a dynamic analysis of disjunction, while Winter (2000), building on Larson (1985), proposed a syntactic account where *or* can move to various positions correlated to the positions where overt *either* can occur.

## 4. Disjunction in conversation

There are various conclusions one normally draws from the assertion of a disjunctive sentence like (25):

**(25)**

Mary is patriotic or quixotic. a. at least one of the two is true

**b.**

at most one of the two is true [exclusive inference]

**c.**

speaker doesn’t know which is true [ignorance inference]

Since only (25a) follows from the classical truth-functional account of disjunction, there seem to be a divergence in meaning between $\vee$ from classical logic and its natural language counterpart. Grice influentially argued that the assumption that such divergence does in fact exist is a mistake originating “from inadequate attention to the nature and importance of the conditions governing conversation” (Grice 1989: 24)[^grice-1989].

Expanding on parts of Grice’s celebrated argument (Grice 1989: 44–46)[^grice-1989], suppose one would propose to analyze *or* in such a way that not only (25a) would logically follow from (25) but also (25b) and/or (25c). A major problem for such a strong analysis of *or* is that it would fail to account for the fact that both the exclusive and the ignorance inferences are easily cancellable. One can say *Mary invited John or Bill or both* (cancellation of exclusive inference), or *The prize is either in the attic or in the garden. I know that because I know where I put it, but I am not going to tell you* (cancellation of ignorance-modal inference, from Grice 1989: 45)[^grice-1989]. A strong theorist could then respond that there are two senses of *or*, a strong one and a weak (truth-functional) one, with the latter employed in the previous cases of cancelation. But as Grice replied,

> if *or* is supposed to possess a strong sense, then it should be possible for it (*or*) to bear this sense in a reasonably wide range of linguistic settings, for example it should be possible to say *It is not the case that A or B* where we are denying that $A$ or $B$ (in the strong sense of *or*). (Grice 1989: 45)[^grice-1989]

That this is not possible is illustrated by the oddity of the following two cases: *It is not the case that Mary invited John or Bill, because she invited both* or *It is not the case that the prize is either in the attic or in the garden, because I know that it is in the garden*. Since strong senses of *or* seem to be restricted to “unenclosed” uses for which an alternative explanation is available, Grice’s conclusion is that only (25a) should be taken as part of the semantic contribution of the sentence (what is said). The exclusive and ignorance inferences in (25b) and (25c) are merely pragmatic effects (conversational implicatures) which derive from interactions between a weak (truth-functional) interpretation of *or* with general principles of conversation.

On Grice’s account, conversation is a purposeful and cooperative enterprise governed by what he calls the Cooperative Principle:

**(CP)**

Make your conversational contribution such as is required, at the stage at which it occurs, by the accepted purpose or direction of the talk exchange in which you are engaged.

Subsumed under this general principle, Grice distinguishes four categories of more specific maxims, including the maxim of Quantity (here simplified).

**Quantity**

(i) Make your contribution as informative as is required (for the current purposes of the exchange);

**(ii)**

Do not make your contribution more informative than is required.

Conversational implicatures are pragmatic inferences arising from the interplay between basic semantic content and these principles of social interaction. A speaker conversationally implicates what she must be assumed to believe in order to preserve the assumption that she is adhering to the CP and maxims.

Gricean reasonings leading from the assertion of a disjunction to the ignorance and exclusive inference can be summarized as follows:

**(26)**

Mary is patriotic or quixotic $\Rightarrow$ speaker doesn’t know which If the speaker had known that Mary is patriotic, she should have said so (by Quantity). Assuming that the speaker made the most informative relevant statement she could, the hearer can infer that the speaker doesn’t know that Mary is patriotic. Similar reasoning for the second disjunct.

**(27)**

Mary is patriotic or quixotic $\Rightarrow$ not both If the speaker had known that Mary is patriotic and quixotic, she should not have used *or*, but *and* (by Quantity). Assuming that the speaker made the most informative relevant statement she could, the hearer can infer that the speaker doesn’t know that Mary is patriotic *and* quixotic. Assuming that the speaker is opinionated (either believes (A and B) or believes not (A and B)) one can conclude that Mary is not patriotic *and* quixotic.

The assumption in (27) that the speaker must be opinionated about the conjunctive statement is however problematic. Given that the use of *or* implicates that the speaker doesn’t know which, why should there be any pressure to think that the speaker would know both if it were true? A number of authors have indeed argued that Gricean implicatures are always epistemically modalized: so in (27) only the proposition that the speaker *doesn’t know* that Mary is patriotic and quixotic is derivable by Gricean means *contra* the predictions of the classical formalisation of Gricean implicatures of Gazdar (1979) (see Soames 1982: 521 and Horn 1989: 543)[^horn-1989][^soames-1982]. Many other attempts to formalization of (variations) of Gricean reasonings have been proposed in the literature, including Horn (1984) but also the more recent Sauerland (2004), van Rooij and Schulz (2004) and Franke (2011). All these formalizations assume a truth-functional analysis of disjunction and other connectives, as the baseline for the pragmatic reasoning. In what follows we will discuss recent developments in linguistic analysis of disjunction, including also challenges to a Gricean pragmatic view.

## 5. Inclusive and exclusive uses of *or*

While the Gricean argument in the previous section quite conclusively excludes that English *or* is ambiguous between an inclusive and an exclusive interpretation (*contra*, for example, Tarski 1939: 21[^note-2], see also Barrett and Stenner 1971)[^barrett-1971][^tarski-1939], recently some linguists have observed that some disjunctive constructions in languages other than English seem to force exclusive uses. Szabolcsi (2002, 2015) discusses the case of Hungarian *vagy*–*vagy* and Spector (2014) the case of French *soit–soit*. Russian *ili–ili*, Italian *o–o*, French *ou –ou* and German *entweder*–*oder* seem to behave in a similar fashion. These are all cases of fully-iterated disjunctions, with a disjunctive particle preceding each disjunct. Note however that not all fully-iterated disjunctive constructions are of these kinds, for example English *either–or* constructions are clearly not always exclusive (*Nobody ate either rice or beans* simply means nobody ate either), and iterated disjunctive constructions in Sinhala and Malayalam are not exclusive at all (see Szabolcsi 2015)[^szabolcsi-2015]. Finally also Latin *aut*, which is often taken as a paradigmatic example of exclusive disjunction (e.g., Copi 1971)[^copi-1971],[^note-3] has been shown to have inclusive uses (at least in its not iterated variant), for example *Nemo timebat tribunos aut plebes (No one feared the magistrates or the mob)* just means no one feared either. See Dik (1968: 274–276) and Jennings (1994: 239–251) for discussion and more examples.

To show that French *soit*-*soit* constructions tend to force exclusivity inferences, while French plain disjunction *ou* doesn’t, Spector discusses the following examples. The reply in both (28) and (29) contradicts the exclusive inference, but at the same time asserts that the first sentence is true. According to Spector, the fact that such a reply is infelicitous in (29) shows that the exclusive inference is obligatory in this case.

**(28)**

a. Marie ira au cinéma lundi ou mardi. ‘Marie will go to the movies on Monday or Tuesday.’

**b.**

Absolument! Et elle ira même à la fois lundi ET mardi. ‘Absolutely! She will even go both days.’

**(29)**

a. Marie ira au cinéma soit lundi soit mardi. ‘Marie will go to the movies SOIT on Monday SOIT on Tuesday.’

**b.**

# Absolument! Et elle ira même à la fois lundi ET mardi. ‘Absolutely! She will even go both days.’

It is important to notice at this point that logic textbook exclusive disjunction, represented as $\infty$ in the following truth table, would not deliver the correct results for these constructions.

| $\phi$ | $\psi$ | $\phi \vee \psi$ | $\phi \ \infty \ \psi$ |
| --- | --- | --- | --- |
| 1 | 1 | 1 | 0 |
| 1 | 0 | 1 | 1 |
| 0 | 1 | 1 | 1 |
| 0 | 0 | 0 | 0 |

First of all, it is well known that using $\infty$ would give wrong predictions for the cases with more than two disjuncts. For example, $\alpha \ \infty \ (\beta \ \infty \ \gamma)$ is true, if all disjuncts are true, but *Marie ira au cinéma soit lundi soit mardi soit mercredi* is not (see Reichenbach 1947; Simons 2000)[^reichenbach-1947][^simons-2000]. Secondly, the use of exclusive disjunction would also fail to explain certain embedded uses of *soit*-*soit* constructions. While these constructions are ungrammatical under negation, making therefore hard to apply the Gricean argument of the previous section to these cases, they are licensed in the scope of a universal quantifier, but the inferences corresponding with the exclusive reading are no longer present in such cases:

**(30)**

a. Tous mes étudiants étudient soit l’allemand soit l’anglais. ‘Every student of mine studies SOIT German SOIT English.’

**b.**

Absolument! Et certains étudient même les deux. ‘Absolutely! And some even study both.’

On the other hand, Spector notices that the following would be deviant as a reply to (30a):

**(31)**

#Absolument! Et ils étudient même les deux. ‘Absolutely! And they even study both.’

Notice that (31) negates the exclusive (*not both*) implicature derived from (30a) by Gricean reasoning using (32) as a relevant alternative:

**(32)**

Tous mes étudiants étudient l’allemand et l’anglais. ‘Every student of mine studies German and English.’

The generalization suggested by Spector is then that *soit-soit* and other iterated disjunctions *obligatorily* trigger Gricean exclusive inferences which are normally only optionally triggered by plain disjunction. Recent experiments reported in Nicolae et al (2024) however have challenged Spector's generalization showing that *soit-soit* and other iterated disjunctions in Russian, Greek and Romanian, although favouring exclusive interpretations, are not always interpreted exclusively even in unembedded position. It is an open question if Spector's account which involves an obligatorily association of these disjunctive forms with an exhaustivity operator (Fox 2007)[^fox-2007] can be maintained in view of these new findings. Note that the obligatorily triggered implicatures discussed in this literature are different from the Gricean conventional implicatures such as the one carried by *but* or *therefore* (see Grice 1975 and the entry on implicature). While the latter do not contribute to *what is said* and, similarly to presupposition, their *not at issue* contribution typically projects outside of the scope of logical operators (e.g., the contrastive effect produced by *but* does not change if we replace the quantifier in *Everybody/Nobody is poor but happy*), expressions triggering obligatory implicatures can contribute differently in the scope of different logical operators such as universal or negative quantifiers, and their contribution can be targeted by subsequent discourse moves as shown in example (29), and, therefore, is arguably part of *what is said*.

As mentioned above, besides favouring exclusive interpretations, these iterated disjunctions are ungrammatical under negation. Let me conclude this section with a note on the interaction between disjunction and negation. Interactions between disjunction, conjunction and negation in classical logic are regulated by the de Morgan laws. English *or* seems to validate the second de Morgan law $\neg (\phi \vee \phi)$ $\leftrightarrow$ $(\neg \phi \wedge \neg \psi)$. On its preferred reading, (33) means that we didn’t close the door and we didn’t close the window.

**(33)**

We didn’t close the door or the window.

Sentence (33) however has also a second reading, on which it means we did not close the door or did not close the window, but I am not sure which. As Szabolcsi (2002) observed, speakers in many languages including Hungarian, Russian, Italian and French find that their counterpart of (33) only has this second reading. On this reading disjunction scopes over negation, and so Szabolcsi proposes to treat disjunction words in these languages as positive polarity items, i.e., roughly, expressions that cannot be interpreted (anti-licensed) in the immediate scope of a negation, unless the negation is itself in a negative or more generally downward entailing (DE) context. A DE context is one in which replacing a predicate with a stronger predicate preserves truth. For example, the predicate *being Italian* is stronger than the predicate *being European* because all Italians are also Europeans. The antecedent of a conditional and the restriction of a universal quantifier are both DE contexts just like the contexts created by negation because of the following valid entailments: (i) *Antecedent of a conditional*: If Sofia is European, she qualifies for a reduction of the tuition fee $\Rightarrow$ If Sofia is Italian, she qualifies for a reduction of the tuition fee; (ii) *Restrictor of universal quantifier*: All students who have a European passport can be hired as student assistant $\Rightarrow$ All students who have an Italian passport can be hired as student assistant; (iii) *Negation*: Antonio is not European $\Rightarrow$ Antonio is not Italian.

Spector introduces a distinction between local and global positive polarity items (PPIs) and argues that single disjunction in French and other languages are local PPIs (anti-licensed in the *immediate scope of negation*, unless certain constraints are met) as Szabolcsi had proposed, but the iterated disjunctive constructions discussed above are global PPIs (anti-licensed under the scope of negation, *however distant the negation is*, unless certain constraints are met). The following examples illustrate this distinction.

Locality of anti-licensing for local PPI *ou* [e.g., *ou* can be interpreted under the scope of a negation which is sufficiently far away]:

**(34)**

Je ne pense pas que Marie ait invité Pierre ou Julie à dîner. ‘I don’t think that Marie invited Pierre or Julie for dinner.’ [understood as I don’t believe Pierre invited either one]

Long-distance anti-licensing for global PPI *soit-soit* [e.g., *soit-soit* cannot be interpreted under the scope of a negation even if far away]:

**(35)**

#Je ne pense pas que Jacques ait invité soit Anne soit Paul à dîner. [Under a narrow-scope interpretation for disjunction] ‘I don’t think that Jacques invited SOIT Anne SOIT Paul for dinner.’

## 6. Modal accounts of disjunction and free choice

We can think of disjunction as a means of entertaining different alternatives. If I say *either it is raining or it is snowing*, I normally convey that both alternatives are open options for me. Grice, as we just saw, argued against a semantic account of such effects, which he labeled as the non truth-functional ground of disjunction (Grice 1989)[^grice-1989]. Zimmermann (2000), by contrast, proposes a modal analysis of linguistic disjunction which identifies the semantic contribution of *or* with precisely these epistemic effects (see also Geurts 2005 for a further development of this idea)[^geurts-2005]. On Zimmermann’s account linguistic disjunctions should be analyzed as conjunctive lists of epistemic possibilities:

**(36)**

$S_1$ or…or $S_n$ $\mapsto$ $\Diamond S_1 \wedge \dots \wedge \Diamond S_n$, where $\Diamond$ is an epistemic possibility operator

Someone uttering a sentence of the form “$S_1$ or…or $S_n$” generally conveys that (i) any of the $S_1,\dots, S_n$ may be true (genuineness) and (ii) that between them, the $S_1,\dots, S_n$ covers all the relevant possibilities (exhaustivity). While on a standard truth-functional analysis only (ii) is part of the meaning of *or*, Zimmermann identifies (i) as the essential contribution of linguistic disjunction with exhaustivity being conveyed by intonation or other devices, for example *either … or*. Evidence for this division of labor comes from the cases of so-called “open” disjunctions, i.e., disjunction with a terminal rise. In the following examples $\uparrow$ and $\downarrow$ indicate rising and falling pitch contours respectively.

**(37)**

Where shall we go? a. London$\uparrow$ or Berlin$\uparrow$ or Paris$\downarrow$

**b.**

London$\uparrow$ or Berlin$\uparrow$ or Paris$\uparrow$

While the terminal fall in the closed disjunction (37a) indicates that the speaker consider her list of options to be exhaustive, the terminal rise in (37b) conveys the opposite effect. On Zimmermann’s analysis is then the terminal fall which contributes exhaustivity and not *or*.

The main motivation behind Zimmermann’s modal analysis however comes from phenomena of free choice. Sentences of the form “You may $A$ or $B$” are normally understood as implying “You may A and you may B”. The following, however, is not a valid principle in standard deontic logic, e.g., von Wright (1968).

**(38)**

$P(\alpha \vee \beta) \to P \alpha $   [Free Choice Principle]

As Kamp (1973) pointed out, plainly making the Free Choice principle valid, for example by adding it as an axiom, would not do because it would allow us to derive $P q$ from $P p$ as shown in (39), which is clearly unacceptable:

**(39)**

1. $P p$   [assumption]

**2.**

$P (p \vee q)$   [from 1, by principle (38)]

**3.**

$P q $   [from 2, by free choice principle]

The step leading to 2 in (39) uses the following principle which holds in standard deontic logic:

**(40)**

$P \alpha \to P(\alpha \vee \beta)$

Intuitively, however, (40) seems invalid (*You may go to the beach* doesn’t seem to imply *You may go to the beach or the cinema*), while (38) seems to hold, in direct opposition to the principles of deontic logic. Von Wright (1968) labeled this the paradox of free choice permissions. Similar paradoxes arise also for imperatives (see Ross’ paradox, introduced in section 2), epistemic modals (Zimmermann 2000)[^zimmermann-2000], and other modal constructions.

Various solutions have been proposed to the paradox of free choice (see Meyer 2020 for a recent overview)[^meyer-2020]. Many have argued that what we called the Free Choice Principle is merely a pragmatic inference and therefore the step leading to 3 in (39) is unjustified. One argument in favor of such a pragmatic account comes from the observation that free choice effects disappear in negative contexts. For example, *No one is allowed to eat the cake or the ice-cream* cannot merely mean that no one is allowed to eat the cake and the ice-cream, as would be expected if free choice effects were semantic entailments rather than pragmatic implicatures (Alonso-Ovalle 2006)[^alonso-ovalle-2006]. Various ways of deriving free choice inferences as implicatures have been proposed in the neo-Gricean tradition (e.g., Gazdar 1979; Kratzer and Shimoyama 2002; Schulz 2005; Franke 2011; and Champollion, Alsop and Grosu 2019)[^champollion-2019][^franke-2011][^gazdar-1979][^kratzer-2002][^schulz-2005] and in the grammatical theory of scalar implicatures (e.g., Fox 2007, Bar–Lev and Fox 2020; and Del Pinal, Bassi and Sauerland 2024)[^bar-2020][^del-2024][^fox-2007]; see however Fusco 2014 for a critical discussion of implicature accounts to free choice.

Others have proposed modal systems where the step leading to 3 in (39) is justified while the step leading to 2 is no longer valid, e.g., Aloni 2007, which proposes a uniform account of free choice effects of disjunctions and indefinites under both modals and imperatives, and more recently Nygren (2022). Simons (2005) and Barker (2010) also proposed semantic accounts of free choice inferences, the latter crucially employing an analysis of *or* in terms of linear logic additive disjunction combined with a representation of strong permission using the deontic reduction strategy (as in Lokhorst 2006)[^lokhorst-2006].

Finally Zimmermann (2000) reduces all free choice sentences to configurations where disjunction takes wide scope with respect to the modal:

**(41)**

$X$ may $A$ or $X$ may $B$ $\Rightarrow$ $X$ may $A$ and $X$ may $B$

By analyzing disjunctions as conjunctions of epistemic possibilities, the correct logical rendering of (41) seems to be the following:

**(42)**

$\Diamond P \alpha \wedge \Diamond P \beta \Rightarrow P \alpha \wedge P \beta $

Zimmermann, however, actually derives only the weaker principle in (43) (under certain assumptions including his Authority principle). $\Box \alpha$ should be read here as an epistemic necessity, “it must be that $\alpha$”, from which $\alpha$ does not necessarily follow:

**(43)**

$\Diamond P \alpha \wedge \Diamond P \beta \models \Box P \alpha \wedge \Box P \beta $

Semantic approaches to free choice like Zimmermann (2000), Aloni (2007) or Simons (2010), however, typically predict too weak readings for free choice sentences under negation. Goldstein (2019) and Aloni (2022) recently proposed non-implicature accounts of free choice which avoid this problem. In Goldstein (2019), both free choice and dual prohibition (the inference from $\neg$ MAY (A or B) to $\neg$ MAY A and $\neg$ MAY B, e.g., *You may not do A or B* to *You may not do A and you may not do B*) result from a homogeneity presupposition, triggered by constructions of the form MAY(A or B), that either both disjuncts are possible, or neither are. In Aloni (2022), free choice inferences are derived as a consequence of a cognitive bias, called *neglect-zero*. Dual prohibition follows from the adoption of a bilateral notion of negation. Neglect-zero is a tendency in human cognition to avoid *zero-models*, i.e., models which verify sentences by virtue of an empty witness set. Aloni models the neglect-zero tendency using the non-emptiness atom (NE) from team semantics (Yan and Väänänen 2017). In team semantics (introduced originally in Hodges 1997; and developed further in Väänänen 2007)[^hodges-1997][^väänänen-2007], formulas are evaluated with respect to sets of evaluation points (called *teams*), rather than single points. In the modal team-based logic employed by Aloni (2022), teams are sets of possible worlds in a Kripke model and represent speakers’ information *states*. In a team semantics we can use the empty team $\emptyset$ to represent zero-models and the non-emptiness atom NE, which is satisfied in a team only if the team is not empty, to model neglect-zero. There are at least 2 ways to define disjunction in a team/state-based framework:

1. $M,s \models (\phi\vee_1 \psi)$ iff $s=t_1 \cup t_2$ for some $t_1, t_2 \subseteq s$ such that $M,t_1 \models \phi$ and $M,t_2 \models \psi$
2. $M,s \models (\phi\vee_2 \psi)$ iff $M,s \models \phi$ or $M,s \models \psi$

Aloni, following most scholars in the team semantics tradition, but also Cresswell (2004) and Hawke and Steinert-Threlkeld (2018), adopts $\vee_1$, sometimes called split disjunction or tensor disjunction. A split disjunction $(\phi\vee_1 \psi)$ is satisfied in a team iff the team is the union of two subteams each satisfying one of the disjuncts. If we disallow empty teams (either syntactically using NE or model-theoretically) a split disjunction is satisfied in a team $s$ only if each disjunct is an open possibility in $s$. In modal statements this non-emptiness requirement derives free choice inferences. A model where only A is possible is a zero-model for MAY(A or B) because it verifies the sentence by virtue of an empty witness for the second disjunct.

Disjunction $\vee_2$, instead, is employed in Inquisitive Semantics (Ciardelli, Groenendijk and Roelofsen 2018)[^ciardelli-2018].$\vee_2$ also closely relates to the notion of disjunction usually adopted in truthmaker semantics (see Fine 2017)[^fine-2017], where a state $s$ is assumed to verify $P \vee Q$ iff $s$ verifies $P$ or $s$ verifies $Q$. Although differently characterised, as points in a partially ordered set rather than as sets of pointds, states in truthmaker semantics can be viewed as generalisations of inquisitive states. The powerset of any set is isomorphic to a complete atomic Boolean lattice, which is also a partial order.

Disjunction $\vee_2$ formalises an “alternative-based” analysis of *or* where disjunctive sentences like “$A$ or $B$” contribute the set of propositional alternatives $\{A, B\}$. Although Kratzer and Shimoyama (2002), Alonso-Ovalle (2006), Aloni (2007), Simons (2010) and Nygren (2022) differ in their solution of the free choice paradox, they all agree in endorsing such an alternative-based view of *or*. Alonso-Ovalle (2006), for example, uses the alternative set induced by a disjunctive sentence in his pragmatic derivation of the free choice implicatures. Aloni (2007) and Nygren (2022) instead assume that modals explicitly operate on the alternative sets introduced in their scope. For example, on these analyses, *may*$(\phi)$ is true only if the ordinary meaning of *may* is true of all alternative propositions generated by $\phi$. Thus, *You may go to the beach or to the cinema* is true only if *You may go to the beach* and *You may go to the cinema* are both true. In the following section we have a closer look at these alternative-based accounts.

## 7. Alternative-based accounts of disjunction

In the previous section, we saw that recent semantic work has argued that disjunctions like “$A$ or $B$” should be treated as generating a set of propositions $\{A, B\}$ rather than yielding the classical join of the two disjuncts. The intuition behind these accounts is that the main function of a disjunctive sentence is to present a set of alternatives. A disjunction offers characterizations of (at least) two different possible states of affairs, and (under certain circumstances) asserts that at least one of these holds in the actual world. Besides the phenomena of free choice discussed in the previous section, other linguistic facts have been argued to justify an alternative-based analysis of disjunction. In this final section, we first introduce the recent inquisitive semantics as an example of an “alternative-based” system with a fully developed logic, and then briefly discuss these further linguistic motivations.

*Figure 1.*

![[a square with a number on a gray circle in each quadrant. The numbers, left to right then top to bottom, are 11, 10, 01, and 00. The first three of these numbers have a curve enclosing them]](../assets/disjunction/fig-a.png)

(a) classical

![[a square with a number on a gray circle in each quadrant. The numbers, left to right then top to bottom, are 11, 10, 01, and 00. The first two of these numbers have a curve enclosing them as do the first and third numbers.]](../assets/disjunction/fig-b.png)

(b) inquisitive

Figure 1. $(p \vee q)$ in classical logic and in inquisitive logic.

### 7.1 Inquisitive semantics

In standard logic-based analyses of linguistic meanings, the *semantic content* of a sentence $\phi$ is defined as the set of evaluation points which verify $\phi$. Normally, evaluation points are identified with possible worlds and so the semantic content of a sentence is identified with a set of possible worlds (a proposition), those worlds in which the sentence is true. In inquisitive semantics, which is one of the team semantics, formulas are evaluated not at worlds, but at information states, defined as sets of possible worlds (those worlds compatible with the information encoded in the state). The semantic content of $\phi$ is then inquisitively identified with the set of states which support $\phi$, thus a *set of sets* of possible worlds, rather than a set of possible worlds. The original motivation for this move was to arrive at a uniform notion of semantic content which would work for both declarative and interrogative meaning (see Ciardelli, Groenendijk and Roelofsen 2015, 2018)[^ciardelli-2015][^ciardelli-2015-2][^ciardelli-2018], since the latter are standardly characterized as sets of propositions, rather than as sets of possible worlds (see the entry on questions). The move of taking states as evaluation points rather than worlds has important consequences for disjunction. As we saw above, the inquisitive clause of disjunction reads as follows:

**(44)**

$M,s \models (\phi\vee \psi)$ iff $M,s \models \phi$ or $M,s \models \psi$.

The interpretation of the connective is given in terms of support in an information state (rather than truth in a world). For a disjunction to be supported in a state, at least one of the disjuncts should be supported, where an atomic sentence is supported in a state $s$ iff it is true in all worlds in $s$. Fig. 1a and b from (Ciardelli and Roelofsen 2011)[^ciardelli-2011] illustrates how the resulting characterization of the semantic content of disjunctive sentences crucially differs from the classical characterization. These figures assume a propositional language with only two atoms $p$ and $q$; world $11$ makes both $p$ and $q$ true, world $10$ makes $p $ true and $q$ false, *et cetera*. Figure 1a depicts the classical meaning of $(p \vee q)$: the set of all worlds that make either $p$ or $q$, or both, true. Figure 1b depicts the semantic content associated with $(p \vee q)$ in inquisitive semantics. Only the maximal states supporting the disjunction, the so-called *alternatives*, are depicted. A state $s$ supports the disjunction if and only if it is included in either of these alternatives. The semantic content of $(p \vee q)$ contains then two alternatives. One alternative is made up of all worlds that make $p$ true, and the other of all worlds that make $q$ true.

From a logical point of view, inquisitive logic can be axiomatised by expanding intuitionistic logic with the Kreisel-Putnam axiom scheme $(\neg \phi \to (\psi_1\vee \psi_2)) \to (\neg \phi \to \psi_1) \vee (\neg \phi \to \psi_2)$ and the double negation axioms restricted to atoms (Ciardelli and Roelofsen 2011)[^ciardelli-2011], and so is one of the intermediate logics between intuitionistic and classical logic (see the entry on intuitionistic logic, section 6.1). As in intuitionistic logic, in inquisitive logic LEM is not provable and the disjunction property holds ($(\phi \vee \psi)$ is inquisitively provable iff $\phi$ is inquisitively provable or $\psi$ is). From a model-theoretic point of view, LEM is not inquisitively valid because both $\phi$ and $\neg \phi$ may fail to be supported in a state that represents ignorance with respect to $\phi$. Recall that the main motivation behind inquisitive logic is to capture both informational and inquisitive content of sentences. Intuitively, $(\phi \vee\neg \phi)$ is not valid because while informationally vacuous, it can still raise an issue, namely the issue whether $\phi$ is the case or not and, therefore, it is not trivial from an inquisitive point of view.

From an algebraic perspective, as we saw in section 3, there is a long tradition in natural language semantics that analyzes disjunction words as expressing a join operator in a Boolean algebra, which, at the sentential level, delivers the least upper bound of the two disjuncts with respect to classic entailment. Recent work showed that alternative-based systems don’t need to abandon the elegant uniform algebraic perspective of the classical analysis: while classical entailment gives rise to a Boolean algebra, inquisitive entailment gives rise to a Heyting algebra, with meet, join, and relative pseudo-complement operators (Roelofsen 2013)[^roelofsen-2013]. Thus if we identify disjunction with the join operator in such a Heyting algebra, this automatically generates the desired cross-categorial, alternative-based notion (Ciardelli and Roelofsen 2015)[^ciardelli-2015][^ciardelli-2015-2].

### 7.2 Examples of linguistic applications

A number of linguistic phenomena have been argued to justify an alternative-based analysis of disjunction. In the previous section we discussed the case of free choice. The remaining part of this section briefly reviews two additional cases: conditionals and questions.

#### 7.2.1 Disjunction in the antecedent of a conditional

The first phenomenon concerns the interpretation of disjunction in the antecedent of a counterfactual conditional. According to the classical treatment due to Stalnaker (1968) and Lewis (1973), a counterfactual $\phi\leadsto\psi$ is true in a world $w$ just in case, among all worlds that make $\phi$ true, those that *differ minimally* from $w$ also make $\psi$ true. It is well known however that a Lewis/Stalnaker analysis invalidates the following inference pattern (Fine 1975a; Nute 1975)[^fine-1975a][^nute-1975]:

**(45)**

$(\phi_1 \vee \phi_2)\leadsto\psi$ $\models$ $\phi_1 \leadsto\psi$

> for indefinitely close $\phi_1$-worlds may be $\neg \psi$-worlds while all of the much closer $\phi_2$-worlds are $\psi$-worlds. However, the counterfactual *if Thorpe or Wilson were to win the next General Election, Britain would prosper* does seem to imply *if Thorpe were to win the next General Election, Britain would prosper*. (Fine 1975a: 453)[^fine-1975a]

One possible reaction would be to abandon a Lewis/Stalnaker treatment of counterfactuals. But another solution is to adopt an alternative treatment of disjunction (Alonso-Ovalle 2006, 2009; van Rooij 2006)[^alonso-ovalle-2006][^alonso-ovalle-2009][^rooij-2006]. Indeed, if the disjunctive antecedent is taken to generate two alternatives and if verifying the counterfactual involves separately checking every alternative generated by the antecedent, the problem is avoided.

#### 7.2.2 Disjunction in questions

An alternative analysis of disjunction further allows a perspicuous representation of the ambiguity of disjunctive questions like (46), between a polar reading (expected answers: *yes/no*) and an alternative reading (expected answers: *coffee/tea*) (e.g., von Stechow 1991 and Aloni, Égré, & Jager 2013, for the embedded case)[^aloni-2013][^aloni-2013-2][^stechow-1991].

**(46)**

Do you want coffee or tea?

The alternative reading, which was problematic for standard analyses of questions (Groenendijk and Stokhof 1984)[^groenendijk-1984], can be easily represented by adopting alternative/inquisitive disjunction (see figure 1). The polar interpretation naturally follows because the classical notion of disjunction can be recovered from the alternative-based interpretation by adding a closure operator such as the existential propositional quantifier $[\exists]$ in alternative semantics (Kratzer and Shimoyama 2002)[^kratzer-2002], or the double negation closure in inquisitive semantics (Ciardelli, Groenendijk and Roelofsen 2018)[^ciardelli-2018]. The same effect can also be obtained by a flattening operator $F$ defined as follows: $s\models F \phi$ iff $\forall w \in s: \{w\} \models \phi$.

In English, alternative and polar readings of questions can be distinguished by intonation or by using the contrastive marker *either…or*, the question *Do you want either coffee or tea?* only has a polar interpretation. Many languages including Mandarin Chinese, Finnish and Basque can use different disjunctive coordinators to disambiguate in these cases (Haspelmath 2007)[^haspelmath-2007]. These languages have two words for interrogative disjunction and standard disjunction. Interrogative disjunction (e.g., Basque *ala*) can only occur in interrogative clauses, where it forces an alternative reading, standard disjunction (e.g., Basque *edo*) can occur in both declarative and interrogative clauses, in the latter case it forces a polar interpretation. The following Basque example from Saltarelli (1988: 84) illustrates:

**(47)**

Te-a tea-ART **ala** or-INT kafe-a coffee-ART nahi want duzu? you.it ‘Do you want coffee or tea?’ (expected answers: coffee/tea)

**(48)**

Te-a tea-ART **edo** or-STA kafe-a coffee-ART nahi want duzu? you.it ‘Do you want either coffee or tea?’ (expected answers: yes/no)

The interaction between disjunctive words, questions and intonation is much more complex than has been exposed here, see Pruitt and Roelofsen (2013) for a description of the data and an illustration on how alternative-based systems can be employed to clarify these phenomena.

**Suggestion for Further Reading**: An excellent source on disjunction is Humberstone 2011, chapter 6.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=disjunction). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/disjunction/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=disjunction&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/disjunction/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

[Please contact the author with suggestions.]

## Related Entries

connectives: sentence connectives in formal logic | fatalism | implicature | logic: intuitionistic | logic: many-valued | logic: relevance | logical constants | negation | presupposition | questions | semantics: dynamic | semantics: Montague

### Acknowledgments

Many thanks to Floris Roelofsen, Luca Incurvati, Martin Stokhof and Ivano Ciardelli for comments on previous versions of this entry. I am further very grateful to an anonymous reviewer for many very useful suggestions and to the editors for their infinite patience. All mistakes are mine.

## Notes（原文脚注）

[^note-1]: “De vraag naar de geldigheid van het principium *tertii exclusi* is dus aequivalent met de vraag naar de mogelijkheid van onoplosbare wiskundige problemen. Voor de wel eens uitgesproken overtuiging, dat onoplosbare wiskundige problemen niet bestaan, is geen aanwijzing van een bewijs aanwezig (It follows that the question of the validity of the principium *tertii exclusi* is equivalent to the question *whether unsolvable mathematical problems can exist*. There is not a shred of a proof for the conviction, which has sometimes been put forward that there exist no unsolvable mathematical problems)” (Brouwer 1908, page 109 of Heyting 1975)[^brouwer-1908][^heyting-1975].

[^note-2]: “Suppose we see the following notice put up in a bookstore: *Customers who are teachers or college students are entitled to a special reduction.* Here the word *or* is undoubtedly used in the first [inclusive] sense, since it is not intended to refuse the reduction to a teacher who is at the same time a college student. If, on the other hand, a child asked to be taken on a hike in the morning and to a theatre in the afternoon, and we reply: *No, we are going on a hike or we are going to the theatre,* then our usage of the word *or* is obviously of the second [exclusive] kind since we intend to comply with only one of the two requests” (Tarski 1939: 21)[^tarski-1939]. As Gamut (1991: 200) however observes, Tarski’s second example is not very convincing since the word *No* which precedes the disjunction seems to convey precisely the exclusive “not both” inference, which then needs not be part of the semantic contribution of *or*.

[^note-3]: “The Latin word *vel* expresses weak or inclusive disjunction, and the Latin word *aut* corresponds to the word *or* in its strong or exclusive sense” (Copi 1971: 241)[^copi-1971].

[^aloni-2007]: Aloni, M., 2007, “Free choice, modals and imperatives”, *Natural Language Semantics*, 15: 65–94.

[^aloni-2022]: Aloni, M., 2022, “Logic and conversation: the case of free choice”, *Semantics and Pragmatics*, 15(5): 1–60.

[^aloni-2013]: Aloni, M. & I. Ciardelli, 2013, “A logical account of free choice imperatives”, in M. Aloni, M. Franke, & F. Roelofsen (eds.), *The dynamic, inquisitive, and visionary life of $\phi$, $?\phi$, and $\Diamond\phi$*, Institute for Logic, Language; Computation, pp. 1–17.

[^aloni-2013-2]: Aloni, M., P. Égré, & T. de Jager, 2013, “Knowing whether A or B”, *Synthese*, 190(4): 2595–2621.

[^alonso-ovalle-2006]: Alonso-Ovalle, L., 2006, *Disjunction in Alternative Semantics*, PhD thesis, University of Massachusetts, Amherst.

[^alonso-ovalle-2009]: –––, 2009, “Counterfactuals, correlatives, and disjunction”, *Linguistics and Philosophy*, 32(2): 207–244.

[^anderson-1962]: Anderson, A. & N. Belnap, 1962, “Tautological entailment”, *Philosophical Studies*, 13: 9–24.

[^anderson-1975]: –––, 1975, *Entailment: the Logic of Relevance and Necessity*, Princeton: Princeton University Press.

[^barker-2010]: Barker, C., 2010, “Free choice permission as resource sensitive reasoning”, *Semantics and Pragmatics*, 3(10): 1–38.

[^bar-2020]: Bar–Lev, M.E. & D. Fox, 2020, “Free choice, simplification, and Innocent Inclusion”, *Natural Language Semantics*, 28: 175–223.

[^barrett-1971]: Barrett, R.L., & A.J. Stenner, 1971, “The myth of the exclusive 'or'”, *Mind*, 80: 116–121.

[^beaver-2001]: Beaver, D., 2001, *Presupposition and Assertion in Dynamic Semantics*, Stanford University: CSLI Publications.

[^birkhoff-1936]: Birkhoff, G. & Neumann, J. von., 1936, “The logic of quantum mechanics”, *Annals of Mathematics*, 37: 823–843.

[^brouwer-1908]: Brouwer, L.E.J., 1908, “De onbetrouwbaarheid der logische principes”, *Tijdschrift voor Wijsbegeerte*, 2: 152–158. English translation in Heyting (ed.), 1975, pp. 107–111.

[^burgess-1981]: Burgess, J., 1981, “Relevance: A fallacy?”, *Notre Dame Journal of Formal Logic*, 22: 97–104.

[^burgess-1983]: –––, 1983, “Common sense and ‘relevance’”, *Notre Dame Journal of Formal Logic*, 24: 41–53.

[^champollion-2019]: Champollion, L., A. Alsop & I. Grosu, 2019, “Free choice disjunction as a rational speech act”. In *Semantics and linguistic theory*, vol. 29, 238–257.

[^chierchia-2012]: Chierchia, G., D. Fox, & B. Spector, 2012, “Scalar implicature as a grammatical phenomenon”, in C. Maienborn, K. von Heusinger, & P. Portner (eds.), *Semantics. An International Handbook of Natural Language Meaning* Vol. 3, Berlin: Mouton de Gruyter, pp. 2297–2332.

[^ciardelli-2011]: Ciardelli, I. & F. Roelofsen, 2011, “Inquisitive logic”, *Journal of Philosophical Logic*, 40(1): 55–94.

[^ciardelli-2015]: –––, 2015, “Alternatives in Montague grammar”, in E. Csipak & H. Zeijlstra (eds.), *Proceedings of Sinn Und Bedeutung 19*, pp. 161–178.

[^ciardelli-2015-2]: Ciardelli, I., J. Groenendijk, & F. Roelofsen, 2015, “On the semantics and logic of declaratives and interrogatives”, *Synthese*, 192: 1689–1728.

[^ciardelli-2018]: –––, 2018, *Inquisitive Semantics*, Oxford University Press.

[^copi-1971]: Copi, I., 1971, *Introduction to Logic*, New York: Macmillan.

[^cresswell-2004]: Cresswell, M., 2004, “Possibility semantics for intuitionistic logic”, *Australasian Journal of Logic*, 2:11–29.

[^del-2024]: Del Pinal, G., I. Bassi & U. Sauerland, 2024, “Free choice and presuppositional exhaustification”, *Semantics and Pragmatics*, 17(3).

[^dik-1968]: Dik, S.C., 1968, *Coordination: Its Implications for the Theory of General Linguistics*, Amsterdam: North Holland Publishing Company.

[^dixon-1972]: Dixon, R., 1972, *The Dyribal Language of North Queensland*, Cambridge: Cambridge University Press.

[^dummett-1978]: Dummett, M., 1978, *Truth and Other Enigmas*, Cambridge, MA: Harvard University Press.

[^elkind-2023]: Elkind, L. & R. Zach, 2023, “The genealogy of '$\vee$'”, *The Review of Symbolic Logic*, 16(3):862–899.

[^fine-1975a]: Fine, K., 1975a, “Critical notice on *Counterfactuals* by D. Lewis”, *Mind*, 84(1): 451–458.

[^fine-1975b]: –––, 1975b, “Vagueness, truth and logic”, *Synthese*, 54: 235–259.

[^fine-2017]: –––, 2017, “A Theory of Truthmaker Content I: Conjunction, Disjunction and Negation”, *Journal of Philosophical Logic*, 46(6): 625–674.

[^fox-2007]: Fox, D., 2007, “Free choice and the theory of scalar implicatures”, in U. Sauerland & P. Stateva (eds.), *Presupposition and Implicature in Compositional Semantics*, Hampshire: Palgrave MacMillan, pp. 71–120.

[^fraassen-1966]: Fraassen, B. van, 1966, “Singular terms, truth-value gaps and free logic”, *Journal of Philosophy*, 63: 28–35.

[^franke-2011]: Franke, M., 2011, “Quantity implicatures, exhaustive interpretation, and rational conversation”, *Semantics & Pragmatics*, 4(1): 1–82.

[^fusco-2014]: Fusco, M., 2014, “Free choice permission and the counterfactuals of pragmatics”, *Linguistics and Philosophy*, 37: 275–290.

[^gamut-1991]: Gamut, L.T.F., 1991, *Logic, Language and Meaning, Volume I: Introduction to Logic*, Chicago: University of Chicago Press.

[^gazdar-1979]: Gazdar, G., 1979, *Pragmatics: Implicature, Presupposition, and Logical Form*, New York: Academic Press.

[^gazdar-1980]: –––, 1980, “A cross-categorial semantics for coordination”, *Linguistics and Philosophy*, 3(3): 407–409.

[^geurts-2005]: Geurts, B., 2005, “Entertaining alternatives: Disjunctions as modals”, *Natural Language Semantics*, 13: 383–410.

[^gil-1991]: Gil, D., 1991, “Aristotle goes to Arizona, and finds a language without *and*”, in D. Zaefferer (ed),*Semantic Universals and Universal Semantics*, Berlin, New York: Foris, pp. 96–130.

[^gödel-1932]: Gödel, K., 1932, “Zum intuitionistischen Aussagenkalkül”, *Anzeiger der Akademie der Wissenschaftischen in Wien*, 69: 65–66.

[^goldstein-2019]: Goldstein, S., 2019, “Free choice and homogeneity”, *Semantics and Pragmatics*, 12(23): 1–53.

[^grice-1989]: Grice, P., 1989, *Studies in the Way of Words*, Cambridge, MA: Harvard University Press.

[^groenendijk-1984]: Groenendijk, J. & M. Stokhof, 1984, *Studies on the Semantics of Questions and the Pragmatics of Answers*, PhD thesis, University of Amsterdam, Amsterdam.

[^groenendijk-1991]: –––, 1991, “Dynamic predicate logic”, *Linguistics and Philosophy*, 14(1): 39–100.

[^haspelmath-2007]: Haspelmath, M., 2007, “Co-ordination”, in T. Shopen (ed.), *Language Typology and Syntactic Description*, Cambridge: Cambridge University Press, Vol. 2, pp. 1–51.

[^hawke-2018]: Hawke, P. & S. Steinert-Threlkeld, 2018, “Informational dynamics of epistemic possibility modals”, *Synthese*, 195:4309–4342.

[^heim-1983]: Heim, I., 1983, “On the projection problem for presupposition”, in M. Barlow, D. Flickinger, & M. Westcoat (eds.), *Second Annual West Coast Conference on Formal Linguistics*, Dept. of Linguistics, Stanford University, pp. 114–126.

[^heyting-1975]: Heyting, A. (ed.), 1975, *L.E.J. Brouwer: Collected Works* (Volume 1: *Philosophy and Foundations of Mathematics*), Amsterdam and New York: Elsevier.

[^hilbert-1923]: Hilbert, D., 1923, “Die logischen Grundlagen der Mathematik”, *Mathematische Annalen*, 88(1–2), 151–165. Translated as: The logical foundations of mathematics. In Ewald, W. B., editor. *From Kant to Hilbert: A Source Book in the Foundations of Mathematics*, Vol. 2. Oxford: Oxford University Press, 1996, pp. 1134–1148.

[^hilbert-1928]: Hilbert, D. & W. Ackermann, 1928, *Grundzüge der Theoretischen Logik* (first edition). Berlin: Springer.

[^hodges-1997]: Hodges, W., 1997, “Compositional Semantics for a Language of Imperfect Information”, *Logic Journal of the IGPL*, 5(4): 539–563.

[^horn-1984]: Horn, L., 1984, “Towards a new taxonomy for pragmatic inference: Q-based and R-based implicature”, in D. Schiffrin (ed.), *Meaning, Form and Use in Context (GURT ’84)*, Washington, D.C.: Georgetown University Press, pp. 11–42.

[^horn-1989]: –––, 1989, *A Natural History of Negation*, Chicago, IL: University of Chicago Press.

[^humberstone-2011]: Humberstone, L., 2011, *The Connectives*, Cambridge, MA: MIT Press.

[^hurford-1974]: Hurford, J., 1974, “Exclusive or inclusive disjunction”, *Foundations of Language*, 11: 409–411.

[^jennings-1994]: Jennings, R., 1994, *The Genealogy of Disjunction*, Oxford: Oxford University Press.

[^kamp-1973]: Kamp, H., 1973, “Free choice permission”, *Proceedings of the Aristotelian Society*, 74: 57–74.

[^kamp-1975]: –––, 1975, “Two theories about adjectives”, in E. Keenan (ed.), *Formal Semantics of Natural Language: Papers from a Colloquium Sponsored by the King’s College Research Centre, Cambridge*, Cambridge: Cambridge University Press, pp. 123–155.

[^karttunen-1973]: Karttunen, L., 1973, “Presuppositions of compound sentences”, *Linguistic Inquiry*, 4: 167–193.

[^keefe-2000]: Keefe, R., 2000, *Theories of Vagueness*, Cambridge: Cambridge University Press.

[^keenan-1985]: Keenan, E. & L. Faltz, 1985, *Boolean Semantics for Natural Language*, Dordrecht: D. Reidel.

[^kleene-1952]: Kleene, S., 1952, *Introduction to Metamathematics*, Amsterdam: North-Holland.

[^kratzer-2002]: Kratzer, A. & J. Shimoyama, 2002, “Indeterminate pronouns: The view from Japanese”, in Y. Otsu (ed.), *The Proceedings of the Third Tokyo Conference on Psycholinguistics (TCP 2002)*, Tokyo: Hituzi Syobo, pp. 1–25.

[^larson-1985]: Larson, R., 1985, “On the syntax of disjunction scope”, *Natural Language and Linguistic Theory*, 3: 217–264.

[^leibniz-1679]: Leibniz, G. W., 1679, *Matheseos universalis pars prior: De terminis incomplexis*. Gottfried Wilhelm Leibniz Bibliothek. Leibniz Handschriften LH 35, 1, 30.

[^lewis-1970]: Lewis, D., 1970, “General semantics”, *Synthese*, 22(1/2): 18–67.

[^lewis-1973]: –––, 1973, *Counterfactuals*, Oxford: Blackwell Publishers and Cambridge, MA: Harvard University Press, Reprinted with revisions, 1986.

[^lokhorst-2006]: Lokhorst, G.-J., 2006, “Andersonian deontic logic, propositional quantification, and Mally”, *Notre Dame Journal of Formal Logic*, 47(3): 385–395.

[^lokhorst-1920]: Łukasiewicz, J., 1920, “O logice trójwartościowej”, *Ruch Filozoficzny*, 5: 170–171. English translation in McCall (ed.), 1967, pp. 16–18.

[^mastop-2005]: Mastop, R., 2005, *What Can You Do? Imperative Mood in Semantic Theory*, PhD thesis, University of Amsterdam.

[^mccall-1967]: McCall, S. (ed.), 1967, *Polish Logic 1920–1939*, Oxford: Oxford University Press.

[^meyer-2020]: Meyer, M., 2020, “An apple or a pear: free choice disjunction”. In H. Rullmann,T. E. Zimmerman, C. Matthewson & C. Meier (eds.), *Wiley’s Semantics Companion*, Hoboken, NJ: Wiley.

[^montague-1973]: Montague, R., 1973, “The proper treatment of quantification in ordinary English”, in K.J.J. Hintikka, J.M.E. Moravcsik, & P. Suppes (eds.), *Approaches to Natural Language*, Dordrecht, Holland and Boston, USA: D. Reidel.

[^nicolae-2024]: Nicolae, A.C, A. Petrenco, A. Tsilia & P. Marty, 2024, “Do languages have exclusive disjunctions?”, *Open Mind*, 8: 1469–1485.

[^nute-1975]: Nute, D., 1975, “Counterfactuals and the similarity of words”, *The Journal of Philosophy*, 72(21): 773–778.

[^nygren-2022]: Nygren, K., 2022, “Free choice in modal inquisitive logic”, *Journal of Philosophical Logic*, 52(2): 347–391.

[^peano-1888]: Peano, G., 1888, *Calcolo geometrico secondo l’Ausdehnungslehre di H. Grassmann, preceduto dalle operazioni della logica deduttiva*. Turin: Fratelli Bocca. Translated as: *The geometrical calculus according to the Ausdehnungslehre of H. Grassman, preceded by the operations of deductive logic*. In Peano 1973, pp. 75–100.

[^peano-1973]: Peano, G., 1973, *Selected Works of Giuseppe Peano.* Toronto: University of Toronto Press. Edited and translated by Kennedy, H.

[^peters-1979]: Peters, S., 1979, “A truth-conditional formulation of Karttunen’s account of presupposition”, *Synthese*, 40(2): 301–316.

[^priest-1979]: Priest, G., 1979, “The logic of paradox”, *Journal of Philosophical Logic*, 8(1): 21–241.

[^priest-2006]: –––, 2006, *In Contradiction: A Study of the Transconsistent*, Oxford: Oxford University Press.

[^pruitt-2013]: Pruitt, K. & F. Roelofsen, 2013, “The interpretation of prosody in disjunctive questions”, *Linguistic Inquiry*, 44(4): 632—650.

[^putnam-1968]: Putnam, H., 1968, “Is logic empirical?”, in R.S. Cohen & M.W. Wartofsky (eds.), *Boston Studies in the Philosophy of Science*, Vol. 5, Dordrecht, Holland: D. Reidel, pp. 216–241.

[^read-1981]: Read, S., 1981, “What is wrong with disjunctive syllogism?”, *Analysis*, 41(2): 66–70.

[^read-1983]: –––, 1983, “Burgess on Relevance: A Fallacy indeed”, *Notre Dame Journal of Formal Logic*, 24(4): 473–481.

[^reichenbach-1947]: Reichenbach, H., 1947, *Elements of Symbolic Logic*, New York: MacMillan.

[^ripley-2011]: Ripley, D., 2011, “Contradictions at the borders”, in R. Nouwen, R. van Rooij, U. Sauerland, & H.-C. Schmitz (eds.), *Vagueness in Communication*, Springer, LNCS, Vol. 6517, pp. 169–188.

[^roelofsen-2013]: Roelofsen, F., 2013, “Algebraic foundations for the semantic treatment of inquisitive content”, *Synthese*, 190(1): 79–102. [doi:10.1007/s11229-013-0282-4](https://doi.org/10.1007/s11229-013-0282-4)

[^rooij-2006]: Rooij, R. van, 2006, “Free choice counterfactual donkeys”, *Journal of Semantics*, 23(4): 383–402.

[^rooij-2004]: Rooij, R. van & K. Schulz, 2004, “Exhaustive interpretation of complex sentences”, *Journal of Logic, Language, and Information*, 13(4): 491–519.

[^rooth-1982]: Rooth, M. & B. Partee, 1982, “Conjunction, type ambiguity and wide scope ‘or’”, in *Proceedings of the First West Coast Conference on Formal Linguistics*, Dept. of Linguistics, Stanford University.

[^ross-1941]: Ross, A., 1941, “Imperatives and logic”, *Theoria*, 7: 53–71.

[^russell-1903a]: Russell, B., 1903a, *Classes*. Manuscript. Edited as: Classes [1903]. In Russell 1994, pp. 3–37.

[^russell-1903b]: –––, 1903b, *Frege on the Contradiction*. Manuscript. Edited as: Frege on the contradiction. In Russell 1994, pp. 607–619.

[^russell-1905]: –––, 1905, “On denoting”, *Mind*, 14: 479–493. doi:10.1093/mind/XIV.4.479

[^russell-1906]: –––, 1906, “The theory of implication”, *American Journal of Mathematics*, 28(2): 159–202. Reprinted as: The theory of implication [1905–06]. In Russell 2014, pp.14–61.

[^russell-1994]: –––, 1994, *Foundations of Logic, 1903–05. The Collected Papers of Bertrand Russell*, Vol. 4. London and New York: Routledge. Edited by Urquhart, A.

[^russell-2014]: –––, 2014, *Toward Principia Mathematica, 1905–08. The Collected Papers of Bertrand Russell*, Vol. 5. London and New York: Routledge. Edited by Moore, G. H.

[^saltarelli-1988]: Saltarelli, M., 1988, *Basque*, London: Routledge.

[^sauerland-2004]: Sauerland, U., 2004, “Scalar implicatures in complex sentences”, *Linguistics and Philosophy*, 27: 367–391.

[^schulz-2005]: Schulz, K., 2005, “A Pragmatic Solution for the Paradox of Free Choice Permission”, *Synthese*, 142: 343–377.

[^sextus-1996]: Sextus Empiricus, *Outlines of Pyrronism*. Translated, with Introduction and Commentary, by Benson Mates. Oxford University Press, New York Oxford, 1996.

[^simons-1996]: Simons, M., 1996, “Disjunction and anaphora”, in *Proceedings of Semantics and Linguistic Theory (SALT6)*, pp. 245–260. doi:10.3765/salt.v6i0.2760

[^simons-2000]: –––, 2000, *Issues in the Semantics and Pragmatics of Disjunction*, New York: Garland.

[^simons-2001]: –––, 2001, “Disjunction and alternativeness”, *Linguistics and Philosophy*, 24(5): 597–619.

[^simons-2005]: –––, 2005, “Dividing things up: The semantics of *or* and the modal/*or* interaction”, *Natural Language Semantics*, 13(3): 271–316

[^soames-1982]: Soames, S., 1982, “How presuppositions are inherited: A solution to the projection problem”, *Linguistic Inquiry*, 13: 483–545.

[^spector-2014]: Spector, B., 2014, “Global positive polarity items and obligatory exhaustivity”, *Semantics and Pragmatics*, 7: 1–61.

[^stalnaker-1968]: Stalnaker, R., 1968, “A theory of conditionals”, in N. Resher (ed.), *Studies in Logical Theory*, Oxford: Blackwell, pp. 98–112.

[^stalnaker-1978]: –––, 1978, “Assertion”, in P. Cole (ed.), *Syntax and Semantics 9: Pragmatics*, New York: Academic Press, pp. 315–332.

[^stechow-1991]: Stechow, A. von, 1991, “Focusing and backgrounding operators”, in W. Abraham (ed.), *Discourse Particles*, Amsterdam: John Benjamins, pp. 37–83.

[^strawson-1950]: Strawson, P., 1950, “On referring”, *Mind*, 59: 320–44.

[^szabolcsi-2002]: Szabolcsi, A., 2002, “Hungarian disjunctions and positive polarity”, in I. Kenesei & P. Siptár (eds.), *Approaches to Hungarian, Vol. 8*, Akadémiai Kiadó, pp. 217–241.

[^szabolcsi-2015]: –––, 2015, “What do quantifier particles do?”, *Linguistics and Philosophy*, 38: 159–204

[^tarski-1939]: Tarski, A., 1939, *Introduction to Logic and to the Methodology of the Deductive Sciences*, Oxford: Oxford University Press.

[^väänänen-2007]: Väänänen, J., 2007, *Dependence Logic: A New Approach to Independence Friendly Logic*, (London Mathematical Society student texts, 70), Cambridge: Cambridge University Press.

[^varzi-2007]: Varzi, A.C., 2007, “Supervaluationism and its logics”, *Mind*, 116: 633–676.

[^whitehead-1903]: Whitehead, A. N., 1903, *The logic of propositional functions*. RA710.057490. Bertrand Russell Archives, McMaster University.

[^whitehead-1910]: Whitehead, A. N. & B. Russell, 1910, *Principia Mathematica*, Vol. 1. Cambridge: Cambridge University Press.

[^williams-2008]: Williams, J., 2008, “Supervaluationism and logical revisionism”, *Journal of Philosophy*, 105(4): 192–212.

[^williamson-1994]: Williamson, T., 1994, *Vagueness*, London: Routledge.

[^winter-1995]: Winter, Y., 1995, “Syncategorematic conjunction and structured meanings”, in M. Simons & T. Galloway (eds.), *Proceedings of Semantics and Linguistic Theory (SALT5)*, Ithaca, NY: CLC Publications, Cornell University.

[^winter-2000]: –––, 2000, “On some scopal asymmetries of coordination”, in H.J. Bennis, M. Everaert, & E. Reuland (eds.), *Interface Strategies*, Amsterdam: KNAW, Royal Netherlands Academy of Arts; Sciences.

[^winter-2001]: –––, 2001, *Flexibility Principles in Boolean Semantics: Coordination, Plurality and Scope in Natural Language*, Cambridge, MA: MIT Press.

[^wright-1968]: Wright, G. von, 1968, *An Essay on Deontic Logic and the Theory of Action*, Amsterdam: North Holland.

[^yang-2017]: Yang, F. & J. Väänänen, 2017, “Propositional team logics”, *Annals of Pure and Applied Logic*, 168(7): 1406–1441.

[^zimmermann-2000]: Zimmermann, E., 2000, “Free choice disjunction and epistemic possibility”, *Natural Language Semantics*, 8: 255–290.
