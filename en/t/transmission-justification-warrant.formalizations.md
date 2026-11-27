# transmission-justification-warrant — formalizations（supplement）

> （《transmission-justification-warrant》词条补充材料，源：plato.stanford.edu/entries/transmission-justification-warrant/formalizations.html）

#### Supplement to Transmission of Justification and Warrant

## Bayesian Formalizations of the *Information-Dependence Template*

Bayesian epistemologists have attempted to formalize extant explanations of transmissivity and non-transmissivity of justification; they have concentrated on the *information-dependence template*. Many epistemologists would claim that an acceptable Bayesian formalization of this template would illuminate its rational structure and, in some sense, validate the explanation of non-transmissivity resting on it. In this section we present models put forward by Okasha (2004), Chandler (2010) and Moretti (2012). (Chandler 2013 also provides a belief revision AGM-style model that we will not survey in this entry.)

The Bayesian assumes that rational belief comes in degrees and that degrees of rational belief or credences obey the probability calculus. Consider any proposition $x$. The expression $\Pr (x)$—called the *unconditional probability* of $x$—is interpreted by the Bayesian as supplying the degree of credence of a rational subject $s$ in $x$. In probability theory the expression $\Pr(x\mid y)$—called the *conditional probability* of $x$ given a proposition $y$—is customarily defined as $\Pr(x \amp y) / \Pr(y)$ provided that $\Pr(y) \gt 0$. (Hereafter whenever we use an expression with form $\Pr(\ldots \mid y)$ we will always assume that $\Pr(y) \gt 0$.) $\Pr(x\mid y)$ is interpreted by the Bayesian as supplying the degree of credence that $s$ would have in $x$ if the truth of $y$ were given to her. The Bayesian says that $y$ (incrementally) *confirms* $x$ if and only if $\Pr(x\mid y) \gt \Pr(x)$. Furthermore, the Bayesian says that $y$ (incrementally) confirms $x$ *conditional on* a proposition $z$ if and only if $\Pr (x\mid y \amp z) \gt \Pr(x\mid z)$. All Bayesian models for transmissivity and non-transmissivity that we consider here assume that there exists a very close relation between degrees of epistemic justification and degrees of rational belief, so that the latter can faithfully represent the former.

Okasha’s (2004) framework rests on two further modeling assumptions:

**(A1)**

the claim that $s \textrm{'} s$ *learning* $y$ *would provide* $s$ *with some degree of justification for* $x$ and the claim that $y$ *confirms* $x$ translate into one another.

**(A2)**

the claim that $s$’s learning $y$ would provide $s$ with some degree of justification for $x$ *given background information* $z$ and the claim that $y$ confirms $x$ *conditional on* $z$ translate into one another.

Okasha essentially proposes to translate the *information-dependence template* into the following triad:

$$ \begin{align} \Pr(p\mid e \amp q) & \gt \Pr(p\mid q). & \textrm{\((e\) confirms \(p\) conditional on \(q\).)} \tag{I}\\ \Pr(p\mid e) & \le \Pr(p). & \textrm{\((e\) does not confirm \(p\) otherwise.)} \tag{II}\\ p & \vdash q. & \textrm{\((p\) entails \(q\).)} \tag{III}\\ \end{align} $$

On the axioms of probability and the definition of conditional probability, (I)–(III) jointly entail:

$$ \begin{align} \Pr(q\mid e) \le \Pr(q). && \textrm{(\(e\) does not confirm \(q\).)} \tag{IV}\\ \end{align} $$

When the overall formalism is interpreted as detailed above, the entailment of (IV) from (I)–(III) is meant to explain why no justification based on $e$ can transmit from $p$ to $q$ whenever the *information-dependence template* is instantiated. More precisely, this framework seems to be meant to account for non-transmissivity of first-time and quantitatively strengthening justification. Suppose in fact the *information-dependence template* is satisfied so that (I)–(III) are true. Then (IV) is true too. Hence $e$ can provide no degree of justification for $q$. Thus—one might infer—$q$ cannot receive via transmission from $p$ any first-time or quantitatively strengthening justification based on $e$.

In spite of appearance, Okasha’s formalism has been found problematic in different respects. To begin with, (I)–(III) appear unable to explain *non-trivial* cases of transmission failure that the *information-dependence template* is deemed to be able to explain. These are cases in which $e$ does supply $s$ with justification for $p$ conditional on $q$ because $q$ is in background information, but $e$ supplies $s$ with no first-time or quantitatively strengthening justification for $q$. Note that since $q$ is in background information, in these cases $e$ supplies $s$ with no first-time or quantitatively strengthening justification for $q$ *given background information* $q$.

The problem for Okasha’s formalism is this: given (A2), Okasha is committed to translating the claim that $s$’s learning $y$ would provide $s$ with no degree of justification for $x$ *given background information* $z$ as $\Pr(x\mid y \amp z) \le \Pr(x\mid z)$. Thus Okasha should construe formally the proposition that $s$’s learning $e$ would supply $s$ with no justification for $q$ *given background information* $q$ as:

$$\tag{V} \Pr(q\mid e \amp q) \le \Pr(q\mid q). $$

Namely, $e$ does not confirm $q$ *conditional* on $q$ (cf. Moretti 2012). If (V) were a part of Okasha’s framework, the latter could perhaps account for the non-trivial cases of transmission failure mentioned before. But (V) is no part of Okasha’s framework. Note furthermore that the truth of (I)–(III) appears *explanatorily irrelevant* for the truth of (V). This is so because for every $q$ and $e$ such that $\Pr(e \amp q) \gt 0$, $\Pr(q\mid e \amp q) = \Pr(q\mid q) = 1$ so that, *trivially*, $\Pr(q\mid e \amp q) \le \Pr(q\mid q)$.

Okasha’s framework appears affected by a more general difficulty. Although this model doesn’t specify any Bayesian principle of transmissivity of justification, the principle implicitly assumed by Okasha is presumably this:

(*O-Trans*)

If $\Pr(p\mid e) \gt \Pr(p)$ and $p \vdash q$, then $\Pr(q\mid e) \gt \Pr(q)$.

*O-Trans* says that if $e$ confirms $p$, and $p$ entails $q$, then $e$ confirms $q$. If justification is represented as confirmation, a deductive argument with premise $p$, conclusion $q$ and evidence $e$ for $p$ is *transmissive* (of some degree of justification) if and only if *O-Trans* is *non-vacuously* true. It’s been known for a long time that *O-Trans* is not true in general; but that doesn’t exclude its being true in some particular cases, which is what we’re supposed to understand the question of transmission failure coming to, on Okasha’s proposal.

Once *O-Trans* is assumed, it is natural to think that the *non-transmissivity* of an argument of the same type will formally be certified by the argument’s *falsifying* *O-Trans*. Yet note that *O-Trans* is, not false, but *vacuously true* when (I)–(IV) are satisfied. For *O-Trans*’ antecedent embeds the logical negation of (II) (cf. Chandler 2010). It is thus unclear whether Okasha’s model actually supplies a formal account of non-transmissivity. (For further criticism see Chandler 2010 and Moretti 2012.)

Let us turn to Chandler’s (2010) formalization. This model intends to be as faithful as possible to the informal notion of justification that the epistemologists who analyze transmission and transmission failure typically presuppose. A proposition is justified, on this notion, just in case it is *rationally believable* or *acceptable*. Accordingly, Chandler’s framework is based on the following modeling assumption:

> $s$’s learning $y$ would justify $x$ if and only if $s$’s learning $y$ would raise her credence in $x$ and would do so over a relevant probability threshold $t \in [0, 1)$ sufficient for rational belief or acceptance, i.e. if and only if $\Pr(x\mid y) \gt \Pr (x)$ and $\Pr(x\mid y) \gt t$.

The basic version of the principle of transmissivity of justification embedded is this model is the following:

(*C-Trans*)

If $\Pr(p\mid e) \gt \Pr(p)$, $\Pr(p\mid e) \gt t$ and $p \vdash q$, then $\Pr(q\mid e) \gt \Pr(q)$.

*C-Trans* states that if $e$ confirms $p$ such that $p$’s conditional probability given $e$ exceeds $t$, and $p$ entails $q$, then $e$ confirms $q$. According to this model, a deductive argument with premise $p$, conclusion $q$ and evidence $e$ is *transmissive* of justification if and only if *C-Trans* is non-vacuously true. Note that $\Pr(p\mid e) \gt t$ and $p \vdash q$ jointly entail $\Pr(q\mid e) \gt t$. Thus if *C-Trans* is non-vacuously true, $e$ confirms $q$ such that $q$’s conditional probability given $e$ exceeds $t$. A deductive argument with premise $p$, conclusion $q$ and evidence $e$ is *non-transmissive* of justification if and only if *C-Trans* is false.

*C-Trans* seems to be meant to account formally for transmissivity of first-time and quantitatively strengthening justification, in the senses that any deductive argument with premise $p$, conclusion $q$ and evidence $e$ is transmissive of justification of either type if and only if it satisfies *C-Trans*. We have transmissivity of first-time justification only if $\Pr(q) \le t$. We have transmissivity of quantitatively strengthening justification only if $\Pr(q) \gt t$. Note that *C-Trans* can be false for some $e, p$ and $q$ because there are probability distributions that verify its antecedent while falsifying its consequent for any chosen $t \in [0, 1).$ Thus *C-Trans* makes room for non-transmissivity of justification.

In Chandler’s model, the condition that the justification from $e$ for $p$ depends on $q$ being in background information is interpreted as the condition that the justification from $e$ for $p$ depends on $q$ being antecedently justified, which is translated into the following material conditional:

(*C*)

If $\Pr(p\mid e) \gt t$ then $\Pr(q) \gt t$.

The *information-dependence template* is formalized by conjoining the antecedent of *C-Trans* and the above conditional. The resulting proposition is equivalent to the following:

(*C-Fail*)

The antecedent of *C-Trans* is true and $\Pr(q) \gt t$.

*C-Trans* and *C-Fail* actually capture some feature of Wright’s informal framework (cf. Chandler 2010: 338). However, while the satisfaction of the information-dependence template is meant to *suffice* for non-transmissivity, the fulfillment of *C-Fail* is only *necessary* for non-transmissivity but *not* sufficient for it. For it can be shown that, necessarily, *C-Fail* is true if *C-Trans* is false, but there are probability distributions that make *C-Fail* and *C-Trans* true at the same time for any chosen $t \in [0, 1).$

With the purpose to improve on Chandler’s model, Moretti (2012) suggests turning *C-Trans* into this principle:

(*M-Trans*)

If $\Pr(p) \le t$, $\Pr(p\mid e) \gt t$ and $p \vdash q$, then $\Pr(q) \le t$.

Accepting *M-Trans* involves turning *C-Fail* into this condition:

(*M-Fail*)

The antecedent of *M-Trans* is true and $\Pr(q) \gt t$.

*M-Trans* says that if $p$’s unconditional probability does not exceed t while the conditional probability of $p$ given $e$ does, and $p$ entails $q$, then $q$’s unconditional probability does not exceed $t$. *M-Trans* accounts formally for transmissivity of first-time justification in the sense that any deductive argument with premise $p$, conclusion $q$ and evidence $e$ is *transmissive of first-time justification* if and only if *M-Trans* is non-vacuously true. (Note again that $\Pr (p\mid e) \gt t$ and $p \vdash q$ entail $\Pr(q\mid e) \gt t$.) Since *M-Fail* is just the condition of falsehood of *M-Trans*, *M-Fail* provides a formal condition *sufficient* for non-transmissivity of first-time justification.

As we have seen in Sect 3.2, the satisfaction of the *information-dependence template* might turn out to be a sufficient condition for non-transmissivity of both first-time and quantitatively strengthening justification. Yet note that if *M-Fail* were sufficient for non-transmissivity of quantitatively strengthening justification, *M-Fail* would prevent *any* deductive argument whatsoever concluding in $q$ from being transmissive of quantitatively strengthening justification. For the clause in *M-Fail* according to which $\Pr(q) \gt t$ is intuitively a *necessary* condition for transmission of quantitatively strengthening justification to $q$. This would be an unpalatable result because (as we have seen in Sect. 2) some deductive arguments appear capable of transmitting quantitatively strengthening justification (cf. Moretti 2012).

Moretti tentatively proposes a new Bayesian formalization including a condition alternative to *M-Fail* that appears sufficient for non-transmissivity of both first-time and quantitatively strengthening justification. See Moretti (2012) for details.
