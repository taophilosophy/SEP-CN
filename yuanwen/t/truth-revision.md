# The Revision Theory of Truth
**First published Fri Dec 15, 1995; substantive revision Tue Jun 6, 2023**

*Kremer, Philip, Rivello, Edoardo*

Consider the following sentence:

**(1)**

(1) is not true.

It has long been known that the sentence, (1), produces a paradox, the so-called *liar’s paradox*: it seems impossible consistently to maintain that (1) is true, and impossible consistently to maintain that (1) is not true: if (1) is true, then (1) says, truly, that (1) is not true so that (1) is not true; on the other hand, if (1) is not true, then what (1) says is the case, i.e., (1) is true. (For details, see Section 1, below.) Given such a paradox, one might be sceptical of the notion of truth, or at least of the prospects of giving a scientifically respectable account of truth.

Alfred Tarski’s great accomplishment was to show how to give — contra this scepticism — a formal definition of truth for a wide class of formalized languages. Tarski did *not*, however, show how to give a definition of truth for languages (such as English) *that contain their own truth predicates*. He thought that this could not be done, precisely because of the liar’s paradox. More generally, Tarski reckoned that *any* language with its own truth predicate would be inconsistent, as long as it obeyed the rules of standard classical logic, and had the ability to refer to its own sentences. As we will see in our remarks on Theorem 2.1 in Section 2.3, Tarski was not quite right: there are consistent classical interpreted languages that refer to their own sentences and have their own truth predicates. (This point originates in Gupta 1982 and is strengthened in Gupta and Belnap 1993.)[^gupta-1982][^gupta-1993]

Given the close connection between *meaning* and *truth*, it is widely held that any semantics for a language $L$, i.e., any theory of meaning for $L$, will be closely related to a theory of truth for $L$: indeed, it is commonly held that something like a Tarskian theory of truth for $L$ will be a central part of a semantics for $L$. Thus, the impossibility of giving a Tarskian theory of truth for languages with their own truth predicates threatens the project of giving a semantics for languages with their own truth predicates.

We had to wait until the work of Kripke 1975 and of Martin & Woodruff 1975 for a systematic formal proposal of a semantics for languages with their own truth predicates. The basic thought is simple: take the offending sentences, such as (1), to be *neither true nor false*. Kripke, in particular, shows how to implement this thought for a wide variety of languages, in effect employing a semantics with three values, *true*, *false* and *neither*.[^note-1] It is safe to say that Kripkean approaches have replaced Tarskian pessimism as the new orthodoxy concerning languages with their own truth predicates.

One of the main rivals to the three-valued semantics is the Revision Theory of Truth, or RTT, independently conceived by Hans Herzberger and Anil Gupta, and first presented in publication in Herzberger 1982a and 1982b, Gupta 1982 and Belnap 1982 — the first monographs on the topic are Yaqūb 1993 and the *locus classicus*, Gupta & Belnap 1993. The RTT is designed to model the kind of reasoning that the liar sentence leads to, *within a two-valued context*. (See Section 5.2 on the question of whether the RTT is genuinely two-valued.) The central idea is the idea of a *revision process*: a process by which we *revise* hypotheses about the truth-value of one or more sentences. The present article’s purpose is to outline the Revision Theory of Truth. We proceed as follows:

## 1. Semiformal introduction

Let’s take a closer look at the sentence (1), given above:

**(1)**

(1) is not true.

It will be useful to make the paradoxical reasoning explicit. First, suppose that:

**(2)**

(1) is not true.

It seems an intuitive principle concerning truth that, for any sentence $p$, we have the so-called T-biconditional

**(3)**

‘$p$’ is true iff $p$.

(Here we are using ‘iff’ as an abbreviation for ‘if and only if’.) In particular, we should have

**(4)**

‘(1) is not true’ is true iff (1) is not true.

Thus, from (2) and (4), we get

**(5)**

‘(1) is not true’ is true.

Then we can apply the identity,

**(6)**

(1) = ‘(1) is not true.’

to conclude that (1) is true. This all shows that if (1) is not true, then (1) is true. Similarly, we can also argue that if (1) is true then (1) is not true. So (1) seems to be both true and not true: hence the paradox. As stated above, the three-valued approach to the paradox takes the liar sentence, (1), to be neither true nor false. Exactly how, or even whether, this move blocks the above reasoning is a matter for debate.

The RTT is not designed to block reasoning of the above kind, but to model it — or most of it.[^note-2] As stated above, the central idea is the idea of a *revision process*: a process by which we *revise* hypotheses about the truth-value of one or more sentences.

Consider the reasoning regarding the liar sentence, (1) above. Suppose that we *hypothesize* that (1) is not true. Then, with an application of the relevant T-biconditional, we might revise our hypothesis as follows:

| Hypothesis: | (1) is not true. |
| --- | --- |
| T-biconditional: | ‘(1) is not true’ is true iff (1) is not true. |
| Therefore: | ‘(1) is not true’ is true. |
| Known identity: | (1) = ‘(1) is not true’. |
| Conclusion: | (1) is true. |
| New *revised* hypothesis: | (1) is true. |

We could continue the revision process, by revising our hypothesis once again, as follows:

| New hypothesis: | (1) is true. |
| --- | --- |
| T-biconditional: | ‘(1) is not true’ is true iff (1) is not true. |
| Therefore: | ‘(1) is not true’ is not true. |
| Known identity: | (1) = ‘(1) is not true’. |
| Conclusion: | (1) is not true. |
| *New* new revised hypothesis: | (1) is not true. |

As the revision process continues, we flip back and forth between taking the liar sentence to be true and not true.

**Example 1.1** It is worth seeing how this kind of revision reasoning works in a case with several interconnected sentences. Let’s apply the revision idea to the following three sentences:

**(7)**

(8) is true or (9) is true.

**(8)**

(7) is true.

**(9)**

(7) is not true.

Informally, we might reason as follows. Either (7) is true or (7) is not true. Thus, either (8) is true or (9) is true. Thus, (7) is true. Thus (8) is true and (9) is not true, and (7) is still true. Iterating the process once again, we get (8) is true, (9) is not true, and (7) is true. More formally, consider any initial hypothesis, $h_0$, about the truth values of (7), (8) and (9). Either $h_0$ says that (7) is true or $h_0$ says that (7) is not true. In either case, we can use the T-biconditional to generate our revised hypothesis $h_1$: if $h_0$ says that (7) is true, then $h_1$ says that ‘(7) is true’ is true, i.e. that (8) is true; and if $h_0$ says that (7) is not true, then $h_1$ says that ‘(7) is not true’ is true, i.e. that (9) is true. So $h_1$ says that either (8) is true or (9) is true. So $h_2$ says that ‘(8) is true or (9) is true’ is true. In other words, $h_2$ says that (7) is true. So no matter what hypothesis $h_0$ we start with, two iterations of the revision process lead to a hypothesis that (7) is true. Similarly, three *or more* iterations of the revision process, lead to the hypothesis that (7) is true, (8) is true and (9) is not true — regardless of our initial hypothesis. In Section 3, we will reconsider this example in a more formal context.

One thing to note is that, in Example 1.1, the revision process yields *stable* truth values for all three sentences. The notion of a sentence *stably true in all revision sequences* will be a central notion for the RTT. The revision-theoretic treatment contrasts, in this case, with the three-valued approach: on most ways of implementing the three-valued idea, all three sentences, (7), (8) and (9), turn out to be neither true nor false.[^note-3] In this case, the RTT arguably better captures the correct informal reasoning than does the three-valued approach: the RTT assigns to the sentences (7), (8) and (9) the truth-values that were assigned to them by the informal reasoning given at the beginning of the example.

## 2. Framing the problem

### 2.1 Truth languages

The goal of the RTT is *not* to give a paradox-free account of truth. Rather, the goal of the RTT is to give an account of our often unstable and often paradoxical reasoning about truth. RTT seeks, more specifically, to give a two-valued account that assigns stable classical truth values to sentences when intuitive reasoning would assign stable classical truth values. We will present a formal semantics for a formal language: we want that language to have both a truth predicate and the resources to refer to its own sentences.

Let us consider a first-order language $L$, with connective &, $\vee$, and $\neg$, quantifiers $\forall$ and $\exists$, the equals sign =, variables, and some stock of names, function symbols and relation symbols. We will say that $L$ is a *truth language*, if it has a distinguished predicate $\boldsymbol{T}$ and quotation marks ‘ and ’, which will be used to form *quote names*: if $A$ is a sentence of $L$, then ‘$A$’ is a name. Let $\textit{Sent}_L = \{A : A$ is a sentence of $L\}$.

It will be useful to identify the $\boldsymbol{T}$-free fragment of a truth language $L$: the first-order language $L^-$ that has the same names, function symbols and relation symbols as $L$, *except* the unary predicate $\boldsymbol{T}$. Since $L^-$ has the same names as $L$, including the same quote names, $L^-$ will have a quote name ‘$A$’ for every sentence $A$ of $L$. Thus $\forall x\boldsymbol{T}x$ is not a sentence of $L^-$, but ‘$\forall x\boldsymbol{T}x$’ is a name of $L^-$ and $\forall x(x =$ ‘$\forall x\boldsymbol{T}x$’) is a sentence of $L^-$.

### 2.2 Ground models

Other than the truth predicate, we will assume that our language is interpreted classically. More precisely, let a *ground model* for $L$ be a classical model $M = \langle D,I\rangle$ for $L^-$, the $\boldsymbol{T}$-free fragment of $L$, satisfying the following:

1. $D$ is a nonempty domain of discourse;
2. $I$ is a function assigning
3. to each name of $L$ a member of $D$;
4. to each $n$-ary function symbol of $L$ a function from $D^n$ to $D$; and
5. to each $n$-ary relation symbol, other than $\boldsymbol{T}$, of $L$ a function from $D^n$ to one of the two truth-values in the set $\{\mathbf{t}, \mathbf{f}\}$;[^note-4]
6. $\textit{Sent}_L$ $\subseteq$ $D$; and
7. $I$(‘$A$’) $= A$ for every $A \in$ $\textit{Sent}_L$.

Clauses (1) and (2) simply specify what it is for $M$ to be a classical model of the $\boldsymbol{T}$-free fragment of $L$. Clauses (3) and (4) ensure that $L$, when interpreted, can talk about its own sentences. Given a ground model, we will consider the prospects of providing a satisfying interpretation of $\boldsymbol{T}$. The most obvious desideratum is that the ground model, expanded to include an interpretation of $\boldsymbol{T}$, satisfy Tarski’s T-biconditionals, i.e., the biconditionals of the form

$$ \boldsymbol{T}\lsquo A\rsquo \text{ iff } A $$

for each $A \in$ $\textit{Sent}_L$.

Some useful terminology: Given a ground model $M$ for $L$ and a name, function symbol or relation symbol $X$, we can think of $I(X)$ as the *interpretation* or, to borrow a term from Gupta and Belnap, the *signification* of $X$. Gupta and Belnap characterize an expression’s or concept’s *signification* in a world $w$ as “an abstract something that carries all the information about all the expression’s [or concept’s] extensional relations in $w$.” If we want to interpret $\boldsymbol{T}x$ as ‘$x$ is true’, then, given a ground model $M$, we would like to find an appropriate signification, or an appropriate range of significations, for $\boldsymbol{T}$.

### 2.3 Three ground models

We might try to assign to $\boldsymbol{T}$ a *classical* signification, by expanding $M$ to a classical model $M' = \langle D',I'\rangle$ for all of $L$, including $\boldsymbol{T}$. Also recall that we want $M'$ to satisfy the T-biconditionals: for our immediate purposes, let us interpret these classically. Let us say that an expansion $M'$ of a ground model $M$ is *Tarskian* iff $M'$ is a classical model and all of the T-biconditionals, interpreted classically, are true in $M'$. We would like to expand ground models to Tarskian models. We consider three ground models in order to assess our prospects for doing this.

**Ground model** $M_1$

Our first ground model is a formalization of Example 1.1, above. Suppose that $L_1$ contains three non-quote names, $\alpha , \beta$, and $\gamma$, and no predicates other than $\boldsymbol{T}$. Let $M_1 = \langle D_1 ,I_1 \rangle$ be as follows: $$\begin{align} D_1 &= \textit{Sent}_{L_1} \\ I_1(\alpha) &= \boldsymbol{T}\beta \vee \boldsymbol{T}\gamma \\ I_1 (\beta) &= \boldsymbol{T}\alpha \\ I_1 (\gamma) &= \neg \boldsymbol{T}\alpha \end{align}$$

**Ground model** $M_2$

Suppose that $L_2$ contains one non-quote name, $\tau$, and no predicates other than $\boldsymbol{T}$. Let $M_2 = \langle D_2 ,I_2 \rangle$ be as follows: $$\begin{align} D_2 &= \textit{Sent}_{L_2} \\ I_2 (\tau) &= \boldsymbol{T}\tau \end{align}$$

**Ground model** $M_3$

Suppose that $L_3$ contains one non-quote name, $\lambda$, and no predicates other than $\boldsymbol{T}$. Let $M_3 = \langle D_3 ,I_3 \rangle$ be as follows: $$\begin{align} D_3 &= \textit{Sent}_{L_3} \\ I_3 (\lambda) &= \neg \boldsymbol{T}\lambda \end{align}$$

**Theorem 2.1**

**(1)**

$M_1$ can be expanded to exactly one Tarskian model: in this model, the sentences $(\boldsymbol{T}\beta \vee \boldsymbol{T}\gamma)$ and $\boldsymbol{T}\alpha$ are true, while the sentence $\neg \boldsymbol{T}\alpha$ is false.

**(2)**

$M_2$ can be expanded to exactly two Tarskian models, in one of which the sentence $\boldsymbol{T}\tau$ is true and in the other of which the sentence $\boldsymbol{T}\tau$ is false.

**(3)**

$M_3$ cannot be expanded to a Tarskian model.

The proofs of (1) and (2) are beyond the scope of this article, but some remarks are in order.

Re (1): The fact that $M_1$ can be expanded to a Tarskian model is not surprising, given the reasoning in Example 1.1, above: any initial hypothesis about the truth values of the three sentences in question leads, after three iterations of the revision process, to a stable hypothesis that $(\boldsymbol{T}\beta \vee \boldsymbol{T}\gamma)$ and $\boldsymbol{T}\alpha$ are true, while $\neg \boldsymbol{T}\alpha$ is false. The fact that $M_1$ can be expanded to *exactly* one Tarskian model needs the so-called *Transfer Theorem*, Gupta and Belnap 1993, Theorem 2D.4.

Remark: In the introductory remarks, above, we claim that there are consistent classical interpreted languages that refer to their own sentences and have their own truth predicates. Clauses (1) of Theorem 2.1 delivers an example. Let $M_1 '$ be the unique Tarskian expansion of $M_1$. Then the language $L_1$, interpreted by $M_1 '$ is an interpreted language that has its own truth predicate satisfying the T-biconditionals classically understood, obeys the rules of standard classical logic, and has the ability to refer to each of its own sentences. Thus Tarski was not quite right in his view that any language with its own truth predicate would be inconsistent, as long as it obeyed the rules of standard classical logic, and had the ability to refer to its own sentences.

Re (2): The only potential problematic self-reference is in the sentence $\boldsymbol{T}\tau,$ the so-called *truth teller*, which says of itself that it is true. Informal reasoning suggests that the truth teller can consistently be assigned either classical truth value: if you assign it the value $\mathbf{t}$ then no paradox is produced, since the sentence now truly says of itself that it is true; and if you assign it the value $\mathbf{f}$ then no paradox is produced, since the sentence now falsely says of itself that it is true. Theorem 2.1 (2) formalizes this point, i.e., $M_2$ can be expanded to one Tarskian model in which $\boldsymbol{T}\tau$ is true and one in which $\boldsymbol{T}\tau$ is false. The fact that $M_2$ can be expanded to *exactly* two Tarskian models needs the Transfer Theorem, alluded to above. Note that the language $L_2$, interpreted by either of these expansions, provides another example of an interpreted language that has its own truth predicate satisfying the T-biconditionals classically understood, obeys the rules of standard classical logic, and has the ability to refer to each of its own sentences.

Proof of (3). Suppose that $M_3 ' = \langle D_3 ,I_3 '\rangle$ is a classical expansion of $M_3$ to all of $L_3$. Since $M_3 '$ is an expansion of $M_3, I_3$ and $I_3 '$ agree on all the names of $L_3$. So

$$ I_3 '(\lambda) = I_3 (\lambda) = \neg \boldsymbol{T}\lambda = I_3(\lsquo \neg \boldsymbol{T}\lambda \rsquo) = I_3 '(\lsquo \neg \boldsymbol{T}\lambda\rsquo). $$

So the sentences $\boldsymbol{T}\lambda$ and $\boldsymbol{T}$‘$\neg \boldsymbol{T}\lambda$’ have the same truth value in $M_3 '$. So the T-biconditional

$$ \boldsymbol{T}\lsquo \neg \boldsymbol{T}\lambda\rsquo \equiv \neg \boldsymbol{T}\lambda $$

is false in $M_3 '$.

Remark: The language $L_3$ interpreted by the ground model $M_3$ formalizes the liar’s paradox, with the sentence $\neg \boldsymbol{T}\lambda$ as the offending liar’s sentence. Thus, despite Theorem 2.1, Clauses (1) and (2), Clause (3) strongly suggests that in a semantics for languages capable of expressing their own truth concepts, $\boldsymbol{T}$ cannot, in general, have a classical signification; and the ‘iff’ in the T-biconditionals will not be read as the classical biconditional. We take these suggestions up in Section 4, below.

## 3. Basic notions of the RTT

### 3.1 Revision rules

In Section 1, we informally sketched the central thought of the RTT, namely, that we can use the T-biconditionals to generate a *revision rule* — a rule for revising a hypothesis about the extension of the truth predicate. Here we will formalize this notion, and work through an example from Section 1.

In general, let L be a truth language and $M$ be a ground model for $L$. An *hypothesis* is a function $h:D \rightarrow \{\mathbf{t}, \mathbf{f}\}$. A hypothesis will in effect be a hypothesized classical interpretation for $\boldsymbol{T}$. Let’s work with an example that combines features from the ground models $M_1$ and $M_3$. We will state the example formally, but reason in a semiformal way, to transition from one hypothesized extension of $\boldsymbol{T}$ to another.

**Example 3.1** Suppose that $L$ contains four non-quote names, $\alpha , \beta , \gamma$ and $\lambda$ and no predicates other than $\boldsymbol{T}$. Also suppose that $M = \langle D,I\rangle$ is as follows: $$\begin{align} D &= \textit{Sent}_L \\ I(\alpha) &= \boldsymbol{T}\beta \vee \boldsymbol{T}\gamma \\ I(\beta) &= \boldsymbol{T}\alpha \\ I(\gamma) &= \neg \boldsymbol{T}\alpha \\ I(\lambda) &= \neg \boldsymbol{T}\lambda \end{align}$$

It will be convenient to let

$$\begin{align} &A \text{ be the sentence } \boldsymbol{T}\beta \vee \boldsymbol{T}\gamma \\ &B \text{ be the sentence } \boldsymbol{T}\alpha \\ &C \text{ be the sentence } \neg \boldsymbol{T}\alpha \\ &X \text{ be the sentence } \neg \boldsymbol{T}\lambda \end{align}$$

Thus:

$$\begin{align} D &= \textit{Sent}_L \\ I(\alpha) &= A \\ I(\beta) &= B \\ I(\gamma) &= C \\ I(\lambda) &= X \end{align}$$

Suppose that the hypothesis $h_0$ hypothesizes that $A$ is false, $B$ is true, $C$ is false and $X$ is false. Thus

$$\begin{align} h_0 (A) &= \mathbf{f} \\ h_0 (B) &= \mathbf{t} \\ h_0 (C) &= \mathbf{f} \\ h_0 (X) &= \mathbf{f} \end{align}$$

Now we will engage in some semiformal reasoning, *on the basis of hypothesis* $h_0$. Among the four sentences, $A, B, C$ and $X, h_0$ puts only $B$ in the extension of $\boldsymbol{T}$. Thus, reasoning from $h_0$, we conclude that:

$$\begin{align} \neg \boldsymbol{T}\alpha &\text{ since the referent of } \alpha \text{ is not in the extension of } \boldsymbol{T} \\ \boldsymbol{T}\beta &\text{ since the referent of } \beta \text{ is in the extension of } \boldsymbol{T} \\ \neg \boldsymbol{T}\gamma &\text{ since the referent of } \gamma \text{ is not in the extension of } \boldsymbol{T} \\ \neg \boldsymbol{T}\lambda &\text{ since the referent of } \lambda \text{ is not in the extension of } \boldsymbol{T}. \end{align}$$

The T-biconditional for the four sentences $A, B, C$ and $X$ are as follows:

$$\begin{align} \tag{T$_A$} A \text{ is true iff }& \boldsymbol{T}\beta \vee \boldsymbol{T}\gamma \\ \tag{T$_B$} B \text{ is true iff }& \boldsymbol{T}\alpha \\ \tag{T$_C$} C \text{ is true iff }& \neg \boldsymbol{T}\alpha \\ \tag{T$_X$} X \text{ is true iff }& \neg \boldsymbol{T}\lambda \end{align}$$

Thus, reasoning from $h_0$, we conclude that:

$$\begin{align} &A \text{ is true} \\ &B \text{ is not true} \\ &C \text{ is true} \\ &X \text{ is true} \end{align}$$

This produces our new hypothesis $h_1$:

$$\begin{align} h_1 (A) &= \mathbf{t} \\ h_1 (B) &= \mathbf{f} \\ h_1 (C) &= \mathbf{t} \\ h_1 (X) &= \mathbf{t} \end{align}$$

Let’s revise our hypothesis once again. So now we will engage in some semiformal reasoning, *on the basis of hypothesis* $h_1$. Hypothesis $h_1$ puts $A, C$ and $X$, but not $B$, in the extension of the $\boldsymbol{T}$. Thus, reasoning from $h_1$, we conclude that:

$$\begin{align} \boldsymbol{T}\alpha &\text{ since the referent of } \alpha \text{ is not in the extension of } \boldsymbol{T} \\ \neg \boldsymbol{T}\beta &\text{ since the referent of } \beta \text{ is in the extension of } \boldsymbol{T} \\ \boldsymbol{T}\gamma &\text{ since the referent of } \gamma \text{ is not in the extension of } \boldsymbol{T} \\ \boldsymbol{T}\lambda &\text{ since the referent of } \lambda \text{ is not in the extension of } \boldsymbol{T}. \end{align}$$

Recall the T-biconditionals for the four sentences $A, B, C$ and $X$, given above. Reasoning from $h_1$ and these T-biconditionals, we conclude that:

$$\begin{align} &A \text{ is true} \\ &B \text{ is true} \\ &C \text{ is not true} \\ &X \text{ is not true} \end{align}$$

This produces our *new* new hypothesis $h_2$:

$$\begin{align} h_2 (A) &= \mathbf{t} \\ h_2 (B) &= \mathbf{t} \\ h_2 (C) &= \mathbf{f} \\ h_2 (X) &= \mathbf{f} \end{align}$$ $\Box$

Let’s formalize the semiformal reasoning carried out in Example 3.1. First we hypothesized that certain sentences were, or were not, in the extension of $\boldsymbol{T}$. Consider ordinary classical model theory. Suppose that our language has a predicate $G$ and a name $a$, and that we have a model $M = \langle D,I\rangle$ which places the referent of $a$ inside the extension of $G$:

$$ I(G)(I(\alpha)) = \mathbf{t} $$

Then we conclude, classically, that the sentence $Ga$ is true in $M$. It will be useful to have some notation for the classical truth value of a sentence $S$ in a classical model $M$. We will write $\textit{Val}_M (S)$. In this case, $\textit{Val}_M (Ga) = \mathbf{t}$. In Example 3.1, we did not start with a classical model of the whole language $L$, but only a classical model of the $\boldsymbol{T}$-free fragment of $L$. But then we added a hypothesis, in order to get a classical model of all of $L$. Let’s use the notation $M + h$ for the classical model of all of $L$ that you get when you extend $M$ by assigning $\boldsymbol{T}$ an extension via the hypothesis $h$. Once you have assigned an extension to the predicate $\boldsymbol{T}$, you can calculate the truth values of the various sentences of $L$. That is, for each sentence $S$ of $L$, we can calculate

$$ \textit{Val}_{M + h}(S) $$

In Example 3.1, we started with hypothesis $h_0$ as follows:

$$\begin{align} h_0 (A) &= \mathbf{f} \\ h_0 (B) &= \mathbf{t} \\ h_0 (C) &= \mathbf{f} \\ h_0 (X) &= \mathbf{f} \end{align}$$

Then we calculated as follows:

$$\begin{align} \textit{Val}_{M+h_0}(\boldsymbol{T}\alpha) &= \mathbf{f} \\ \textit{Val}_{M+h_0}(\boldsymbol{T}\beta) &= \mathbf{t} \\ \textit{Val}_{M+h_0}(\boldsymbol{T}\gamma) &= \mathbf{f} \\ \textit{Val}_{M+h_0}(\boldsymbol{T}\lambda) &= \mathbf{f} \end{align}$$

And then we concluded as follows:

$$\begin{align} \textit{Val}_{M+h_0}(A) &= \textit{Val}_{M+h_0}(\boldsymbol{T}\beta \lor \boldsymbol{T}\gamma) = \mathbf{t} \\ \textit{Val}_{M+h_0}(B) &= \textit{Val}_{M+h_0}(\boldsymbol{T}\alpha) = \mathbf{f} \\ \textit{Val}_{M+h_0}(C) &= \textit{Val}_{M+h_0}(\neg\boldsymbol{T}\alpha) = \mathbf{t} \\ \textit{Val}_{M+h_0}(X) &= \textit{Val}_{M+h_0}(\neg\boldsymbol{T}\lambda) = \mathbf{t} \end{align}$$

These conclusions generated our new hypothesis, $h_1$:

$$\begin{align} h_1 (A) &= \mathbf{t} \\ h_1 (B) &= \mathbf{f} \\ h_1 (C) &= \mathbf{t} \\ h_1 (X) &= \mathbf{t} \end{align}$$

Note that, in general,

$$ h_1 (S) = \textit{Val}_{M+h_0}(S). $$

We are now prepared to define the *revision rule* given by a ground model $M = \langle D,I\rangle$. In general, given an hypothesis $h$, let $M + h = \langle D,I'\rangle$ be the model of $L$ which agrees with $M$ on the $\boldsymbol{T}$-free fragment of $L$, and which is such that $I'(\boldsymbol{T}) = h$. So $M + h$ is just a classical model for all of $L$. For any model $M + h$ of all of $L$ and any sentence $S$ of $L$, let $\textit{Val}_{M+h}(S)$ be the ordinary classical truth value of $S$ in $M + h$.

**Definition 3.2**

Suppose that $L$ is a truth language and that $M = \langle D,I\rangle$ is a ground model for $L$. The *revision rule*, $\tau_M$, is the function mapping hypotheses to hypotheses, as follows: $$\tau_M (h)(d) = \begin{cases} \mathbf{t}, \text{ if } d\in D \text{ is a sentence of } L \text{ and } \textit{Val}_{M+h}(d) = \mathbf{t} \\ \mathbf{f}, \text{ otherwise} \end{cases}$$

The ‘otherwise’ clause tells us that if $d$ is not a sentence of $L$, then, after one application of revision, we stick with the hypothesis that $d$ is not true.[^note-5] Note that, in Example 3.$1, h_1 = \tau_M (h_0)$ and $h_2 = \tau_M (h_1)$. We will often drop the subscripted ‘$M$’ when the context make it clear which ground model is at issue.

### 3.2 Revision sequences

Let’s pick up Example 3.1 and see what happens when we iterate the application of the revision rule.

**Example 3.3** (Example 3.1 continued) Recall that $L$ contains four non-quote names, $\alpha , \beta , \gamma$ and $\lambda$ and no predicates other than $\boldsymbol{T}$. Also recall that $M = \langle D,I\rangle$ is as follows: $$\begin{align} D &= \textit{Sent}_L \\ I(\alpha) &= A = \boldsymbol{T}\beta \vee \boldsymbol{T}\gamma \\ I(\beta) &= B = \boldsymbol{T}\alpha \\ I(\gamma) &= C = \neg \boldsymbol{T}\alpha \\ I(\lambda) &= X = \neg \boldsymbol{T}\lambda \end{align}$$

The following table indicates what happens with repeated applications of the revision rule $\tau_M$ to the hypothesis $h_0$ from Example 3.1. In this table, we will write $\tau$ instead of $\tau_M$:

| $S$ | $h_0 (S)$ | $\tau(h_0)(S)^{}$ | $\tau^2 (h_0)(S)$ | $\tau^3 (h_0)(S)$ | $\tau^4 (h_0)(S)$ | $\cdots$ |
| --- | --- | --- | --- | --- | --- | --- |
| $A$ | $\mathbf{f}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\cdots$ |
| $B$ | $\mathbf{t}$ | $\mathbf{f}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\cdots$ |
| $C$ | $\mathbf{f}$ | $\mathbf{t}$ | $\mathbf{f}$ | $\mathbf{f}$ | $\mathbf{f}$ | $\cdots$ |
| $X$ | $\mathbf{f}$ | $\mathbf{t}$ | $\mathbf{f}$ | $\mathbf{t}$ | $\mathbf{f}$ | $\cdots$ |

So $h_0$ generates a *revision sequence* (see Definition 3.7, below). And $A$ and $B$ are *stably true* in that revision sequence (see Definition 3.6, below), while $C$ is *stably false*. The liar sentence $X$ is, unsurprisingly, neither stably true nor stably false: the liar sentence is *unstable*. A similar calculation would show that $A$ is stably true, regardless of the initial hypothesis: thus $A$ is *categorically true* (see Definition 3.8).

Before giving a precise definition of a *revision sequence*, we give an example where we would want to carry the revision process beyond the finite stages, $h, \tau^1 (h), \tau^2 (h), \tau^3 (h)$, and so on.

**Example 3.4** Suppose that $L$ contains nonquote names $\alpha_0, \alpha_1, \alpha_2, \alpha_3,\ldots$, and unary predicates $G$ and $\boldsymbol{T}$. Now we will specify a ground model $M = \langle D,I\rangle$ where the name $\alpha_0$ refers to some tautology, and where $$\begin{align} &\text{the name } \alpha_1 \text{ refers to the sentence } \boldsymbol{T}\alpha_0 \\ &\text{the name } \alpha_2 \text{ refers to the sentence } \boldsymbol{T}\alpha_1 \\ &\text{the name } \alpha_3 \text{ refers to the sentence } \boldsymbol{T}\alpha_2 \\ &\ \vdots \end{align}$$

More formally, let $A_0$ be the sentence $\boldsymbol{T}\alpha_0 \vee \neg \boldsymbol{T}\alpha_0$, and for each $n \ge 0$, let $A_{n+1}$ be the sentence $\boldsymbol{T}\alpha_n$. Thus $A_1$ is the sentence $\boldsymbol{T}\alpha_0$, and $A_2$ is the sentence $\boldsymbol{T}\alpha_1$, and $A_3$ is the sentence $\boldsymbol{T}\alpha_2$, and so on. Our ground model $M = \langle D,I\rangle$ is as follows:

$$\begin{align} D &= \textit{Sent}_L \\ I(\alpha_n) &= A_n \\ I(G)(A) &= \mathbf{t} \text{ iff } A = A_n \text{ for some } n \end{align}$$

Thus, the extension of $G$ is the following set of sentences: $$\{A_0, A_1, A_2, A_3 , \ldots \} = \{(\boldsymbol{T}\alpha_0 \vee \neg \boldsymbol{T}\alpha_0), \boldsymbol{T}\alpha_0, \boldsymbol{T}\alpha_1, \boldsymbol{T}\alpha_2, \boldsymbol{T}\alpha_3 , \ldots \}. $$ Finally let $B$ be the sentence $\forall x(Gx \supset \boldsymbol{T}x)$. Let $h$ be any hypothesis for which we have, for each natural number $n$,

$$ h(A_n) = h(B) = \mathbf{f}. $$

The following table indicates what happens with repeated applications of the revision rule $\tau_M$ to the hypothesis $h$. In this table, we will write $\tau$ instead of $\tau_M$:

| $S$ | $h(S)$ | $t(h)(S)$ | $\tau^2 (h)(S)$ | $\tau^3 (h)(S)$ | $\tau^4 (h)(S)$ | $\cdots$ |
| --- | --- | --- | --- | --- | --- | --- |
| $A_0$ | $\mathbf{f}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\cdots$ |
| $A_1$ | $\mathbf{f}$ | $\mathbf{f}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\cdots$ |
| $A_2$ | $\mathbf{f}$ | $\mathbf{f}$ | $\mathbf{f}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\cdots$ |
| $A_3$ | $\mathbf{f}$ | $\mathbf{f}$ | $\mathbf{f}$ | $\mathbf{f}$ | $\mathbf{t}$ | $\cdots$ |
| $A_4$ | $\mathbf{f}$ | $\mathbf{f}$ | $\mathbf{f}$ | $\mathbf{f}$ | $\mathbf{f}$ | $\cdots$ |
| $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ |
| $B$ | $\mathbf{f}$ | $\mathbf{f}$ | $\mathbf{f}$ | $\mathbf{f}$ | $\mathbf{f}$ | $\cdots$ |

At the $0^{\text{th}}$ stage, each $A_n$ is outside the hypothesized extension of $\boldsymbol{T}$. But from the $n{+}1^{\text{th}}$ stage onwards, $A_n$ is $in$ the hypothesized extension of $\boldsymbol{T}$. So, for each $n$, the sentence $A_n$ is eventually stably hypothesized to be true. Despite this, there is no *finite* stage at which all the $A_n$’s are hypothesized to be true: as a result the sentence $B = \forall x(Gx \supset \boldsymbol{T}x)$ remains false at each finite stage. This suggests extending the process as follows:

| $S$ | $h(S)$ | $\tau(h)(S)$ | $\tau^2 (h)(S)$ | $\tau^3 (h)(S)$ | $\cdots$ | $\omega$ | $\omega +1$ | $\omega +2$ | $\cdots$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $A_0$ | $\mathbf{f}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\cdots$ | $\mathbf{t}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\cdots$ |
| $A_1$ | $\mathbf{f}$ | $\mathbf{f}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\cdots$ | $\mathbf{t}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\cdots$ |
| $A_2$ | $\mathbf{f}$ | $\mathbf{f}$ | $\mathbf{f}$ | $\mathbf{t}$ | $\cdots$ | $\mathbf{t}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\cdots$ |
| $A_3$ | $\mathbf{f}$ | $\mathbf{f}$ | $\mathbf{f}$ | $\mathbf{f}$ | $\cdots$ | $\mathbf{t}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\cdots$ |
| $A_4$ | $\mathbf{f}$ | $\mathbf{f}$ | $\mathbf{f}$ | $\mathbf{f}$ | $\cdots$ | $\mathbf{t}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\cdots$ |
| $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ |
| $B$ | $\mathbf{f}$ | $\mathbf{f}$ | $\mathbf{f}$ | $\mathbf{f}$ | $\cdots$ | $\mathbf{f}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\cdots$ |

Thus, if we allow the revision process to proceed beyond the finite stages, then the sentence $B = \forall x(Gx \supset \boldsymbol{T}x)$ is stably true from the $\omega{+}1^{\text{th}}$ stage onwards. $\Box$

In Example 3.4, the intuitive verdict is that not only should each $A_n$ receive a stable truth value of $\mathbf{t}$, but so should the sentence $B = \forall x(Gx \supset \boldsymbol{T}x)$. The only way to ensure this is to carry the revision process beyond the finite stages. So we will consider revision sequences that are very long: not only will a revision sequence have a $n^{\text{th}}$ stage for each finite number $n$, but a $\eta^{\text{th}}$ stage for every *ordinal* number $\eta$. (The next paragraph is to help the reader unfamiliar with ordinal numbers.)

One way to think of the ordinal numbers is as follows. Start with the finite natural numbers:

$$ 0, 1, 2, 3, \ldots $$

Add a number, $\omega$, greater than all of these but not the immediate successor of any of them:

$$ 0, 1, 2, 3, \ldots ,\omega $$

And then take the successor of $\omega$, its successor, and so on:

$$ 0, 1, 2, 3, \ldots ,\omega , \omega +1, \omega +2, \omega +3\ldots $$

Then add a number $\omega +\omega$, or $\omega \times 2$, greater than all of these (and again, not the immediate successor of any), and start over, reiterating this process over and over:

$$\begin{align} &0, 1, 2, 3, \ldots \\ &\omega , \omega +1, \omega +2, \omega +3,\ldots, \\ &\omega \times 2, (\omega \times 2)+1, (\omega \times 2)+2, (\omega \times 2)+3,\ldots, \\ &\omega \times 3, (\omega \times 3)+1, (\omega \times 3)+2, (\omega \times 3)+3,\ldots \\ &\ \vdots \end{align}$$

At the end of this, we add an ordinal number $\omega \times \omega$ or $\omega^2$:

$$\begin{align} &0, 1, 2, \ldots ,\omega , \omega +1, \omega +2, \ldots ,\omega \times 2, (\omega \times 2)+1,\ldots, \\ &\omega \times 3, \ldots ,\omega \times 4, \ldots ,\omega \times 5, \ldots ,\omega^2, \omega^2 +1,\ldots \end{align}$$

The ordinal numbers have the following structure: every ordinal number has an immediate successor known as a *successor ordinal*; and for any infinitely ascending sequence of ordinal numbers, there is a *limit ordinal* which is greater than all the members of the sequence and which is not the immediate successor of any member of the sequence. Thus the following are successor ordinals: $5, 178, \omega +12, (\omega \times 5)+56, \omega^2 +8$; and the following are limit ordinals: $\omega , \omega \times 2, \omega^2 , (\omega^2 +\omega)$, etc. Given a limit ordinal $\eta$, a sequence $S$ of objects is an $\eta$-*long* sequence if there is an object $S_{\delta}$ for every ordinal $\delta \lt \eta$. We will denote the class of ordinals as $\textsf{On}$. Any sequence $S$ of objects is an $\textsf{On}$-*long* sequence if there is an object $S_{\delta}$ for every ordinal $\delta$.

When assessing whether a sentence receives a stable truth value, the RTT considers sequences of hypotheses of length $\textsf{On}$. So suppose that $S$ is an $\textsf{On}$-long sequence of hypotheses, and let $\zeta$ and $\eta$ range over ordinals. Clearly, in order for $S$ to represent the revision process, we need the $\zeta{+}1^{\text{th}}$ hypothesis to be generated from the $\zeta^{\text{th}}$ hypothesis by the revision rule. So we insist that $S_{\zeta +1} = \tau_M(S_{\zeta})$. But what should we do at a limit stage? That is, how should we set $S_{\eta}$(d) when $\eta$ is a limit ordinal? Clearly any object that is stably true [false] *up to* that stage should be true [false] $at$ that stage. Thus consider Example 3.4. The sentence $A_2$, for example, is true up to the $\omega^{\text{th}}$ stage; so we set $A_2$ to be true $at$ the $\omega^{\text{th}}$ stage. For objects that do not stabilize up to that stage, Gupta and Belnap 1993 adopt a liberal policy: when constructing a revision sequence $S$, if the value of the object $d \in D$ has not stabilized by the time you get to the limit stage $\eta$, then you can set $S_{\eta}$(d) to be whichever of $\mathbf{t}$ or $\mathbf{f}$ you like. Before we give the precise definition of a *revision sequence*, we continue with Example 3.3 to see an application of this idea.

**Example 3.5** (Example 3.3 continued) Recall that $L$ contains four non-quote names, $\alpha , \beta , \gamma$ and $\lambda$ and no predicates other than $\boldsymbol{T}$. Also recall that $M = \langle D,I\rangle$ is as follows:

$$\begin{align} D &= \textit{Sent}_L \\ I(\alpha) &= A = \boldsymbol{T}\beta \vee \boldsymbol{T}\gamma \\ I(\beta) &= B = \boldsymbol{T}\alpha \\ I(\gamma) &= C = \neg \boldsymbol{T}\alpha \\ I(\lambda) &= X = \neg \boldsymbol{T}\lambda \end{align}$$

The following table indicates what happens with repeated applications of the revision rule $\tau_M$ to the hypothesis $h_0$ from Example 3.3. For each ordinal $\eta$, we will indicate the $\eta^{\text{th}}$ hypothesis by $S_{\eta}$ (suppressing the index $M$ on $\tau)$. Thus $S_0 = h_0,$ $S_1 = \tau(h_0),$ $S_2 = \tau^2 (h_0),$ $S_3 = \tau^3 (h_0),$ and $S_{\omega},$ the $\omega^{\text{th}}$ hypothesis, is determined in some way from the hypotheses leading up to it. So, starting with $h_0$ from Example 3.3, our revision sequence begins as follows:

| $S$ | $S_0 (S)$ | $S_1 (S)$ | $S_2 (S)$ | $S_3 (S)$ | $S_4 (S)$ | $\cdots$ |
| --- | --- | --- | --- | --- | --- | --- |
| $A$ | $\mathbf{f}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\cdots$ |
| $B$ | $\mathbf{t}$ | $\mathbf{f}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\cdots$ |
| $C$ | $\mathbf{f}$ | $\mathbf{t}$ | $\mathbf{f}$ | $\mathbf{f}$ | $\mathbf{f}$ | $\cdots$ |
| $X$ | $\mathbf{f}$ | $\mathbf{t}$ | $\mathbf{f}$ | $\mathbf{t}$ | $\mathbf{f}$ | $\cdots$ |

What happens at the $\omega^{\text{th}}$ stage? $A$ and $B$ are stably true *up to* the $\omega^{\text{th}}$ stage, and $C$ is stably false *up to* the $\omega^{\text{th}}$ stage. So $at$ the $\omega^{\text{th}}$ stage, we must have the following:

| $S$ | $S_0 (S)$ | $S_1 (S)$ | $S_2 (S)$ | $S_3 (S)$ | $S_4 (S)$ | $\cdots$ | $S_{\omega}(S)$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| $A$ | $\mathbf{f}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\cdots$ | $\mathbf{t}$ |
| $B$ | $\mathbf{t}$ | $\mathbf{f}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\cdots$ | $\mathbf{t}$ |
| $C$ | $\mathbf{f}$ | $\mathbf{t}$ | $\mathbf{f}$ | $\mathbf{f}$ | $\mathbf{f}$ | $\cdots$ | $\mathbf{f}$ |
| $X$ | $\mathbf{f}$ | $\mathbf{t}$ | $\mathbf{f}$ | $\mathbf{t}$ | $\mathbf{f}$ | $\cdots$ | **?** |

But the entry for $S_{\omega}(X)$ can be either $\mathbf{t}$ or $\mathbf{f}$. In other words, the initial hypothesis $h_0$ generates at least two revision sequences. Every revision sequence $S$ that has $h_0$ as its initial hypothesis must have $S_{\omega}(A) = \mathbf{t}, S_{\omega}(B) = \mathbf{t}$, and $S_{\omega}(C) = \mathbf{f}$. But there is some revision sequence $S$, with $h_0$ as its initial hypothesis, and with $S_{\omega}(X) = \mathbf{t}$; and there is some revision sequence $S'$, with $h_0$ as its initial hypothesis, and with $S_{\omega}'(X) = \mathbf{f}. \Box$

We are now ready to define the notion of a *revision sequence*:

**Definition 3.6**

Suppose that $L$ is a truth language, and that $M = \langle D,I\rangle$ is a ground model. Suppose that $S$ is an $\textsf{On}$-long sequence of hypotheses. Then we say that $d \in D$ is *stably* $\mathbf{t} [\mathbf{f}]$ in $S$ iff for some ordinal $\theta$ we have $$ S_{\zeta}(d) = \mathbf{t}\ [\mathbf{f}], \text{ for every ordinal } \zeta \ge \theta. $$ Suppose that $S$ is a $\eta$-long sequence of hypothesis for some limit ordinal $\eta$. Then we say that $d \in D$ is *stably* $\mathbf{t}$ $[\mathbf{f}]$ in $S$ iff for some ordinal $\theta \lt \eta$ we have $$ S_{\zeta}(d) = \mathbf{t}\ [\mathbf{f}], \text{ for every ordinal } \zeta \text{ such that } \zeta \ge \theta \text{ and } \zeta \lt \eta. $$ If $S$ is an $\textsf{On}$-long sequence of hypotheses and $\eta$ is a limit ordinal, then $S|_{\eta}$ is the initial segment of $S$ up to but not including $\eta$. Note that $S|_{\eta}$ is a $\eta$-long sequence of hypotheses.

**Definition 3.7**

Suppose that $L$ is a truth language, and that $M = \langle D,I\rangle$ is a ground model. Suppose that $S$ is an $\textsf{On}$-long sequence of hypotheses. $S$ is a *revision sequence for* $M$ iff $S_{\zeta +1} = \tau_M(S_{\zeta})$, for each $\zeta \in \textsf{On}$, and for each limit ordinal $\eta$ and each $d \in D$, if $d$ is stably $\mathbf{t}$ $[\mathbf{f}$] in $S|_{\eta}$, then $S_{\eta}(d) = \mathbf{t} [\mathbf{f}$].

**Definition 3.8**

Suppose that $L$ is a truth language, and that $M = \langle D,I\rangle$ is a ground model. We say that the sentence $A$ is *categorically true* [*false*] *in* $M$ iff $A$ is stably $\mathbf{t}$ $[\mathbf{f}]$ in every revision sequence for $M$. We say that $A$ is *categorical in* $M$ iff $A$ is either categorically true or categorically false in $M$.

We now illustrate these concepts with an example. The example will also illustrate a new concept to be defined afterwards.

**Example 3.9** Suppose that $L$ is a truth language containing nonquote names $\beta , \alpha_0, \alpha_1, \alpha_2, \alpha_3,\ldots$, and unary predicates $G$ and $\boldsymbol{T}$. Let $B$ be the sentence $$ \boldsymbol{T}\beta \vee \forall x\forall y(Gx \amp \neg \boldsymbol{T}x \amp Gy \amp \neg \boldsymbol{T}y \supset x=y). $$

Let $A_0$ be the sentence $\exists x(Gx \amp \neg \boldsymbol{T}x)$. And for each $n \ge 0$, let $A_{n+1}$ be the sentence $\boldsymbol{T}\alpha_n$. Consider the following ground model $M = \langle D,I\rangle$

$$\begin{align} D &= \textit{Sent}_L \\ I(\beta) &= B \\ I(\alpha_n) &= A_n \\ I(G)(A) &= \mathbf{t} \text{ iff } A = A_n \text{ for some } n \end{align}$$

Thus, the extension of $G$ is the following set of sentences: $\{A_0, A_1, A_2, A_3 , \ldots \} = \{\exists x(Gx \amp \neg \boldsymbol{T}x), \boldsymbol{T}\alpha_0, \boldsymbol{T}\alpha_1, \boldsymbol{T} \alpha_2, \boldsymbol{T}\alpha_3 , \ldots \}$. Let $h$ be any hypothesis for which we have, $h(B) = \mathbf{f}$ and for each natural number $n$,

$$ h(A_n) = \mathbf{f}. $$

And let $S$ be a revision sequence whose initial hypothesis is $h$, i.e., $S_0 = h$. The following table indicates some of the values of $S_{\gamma}(C)$, for sentences $C \in \{B, A_0, A_1, A_2, A_3 , \ldots \}$. In the top row, we indicate only the ordinal number representing the stage in the revision process.

|   | 0 | 1 | 2 | 3 | $\cdots$ | $\omega$ | $\omega{+}1$ | $\omega{+}2$ | $\omega{+}3$ | $\cdots$ | $\omega{\times}2$ | $(\omega{\times}2){+}1$ | $(\omega{\times}2){+}2$ | $\cdots$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $B$ | $\mathbf{f}$ | $\mathbf{f}$ | $\mathbf{f}$ | $\mathbf{f}$ | $\cdots$ | $\mathbf{f}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\cdots$ | $\mathbf{t}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\cdots$ |
| $A_0$ | $\mathbf{f}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\cdots$ | $\mathbf{t}$ | $\mathbf{f}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\cdots$ | $\mathbf{t}$ | $\mathbf{f}$ | $\mathbf{t}$ | $\cdots$ |
| $A_1$ | $\mathbf{f}$ | $\mathbf{f}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\cdots$ | $\mathbf{t}$ | $\mathbf{t}$ | $\mathbf{f}$ | $\mathbf{t}$ | $\cdots$ | $\mathbf{t}$ | $\mathbf{t}$ | $\mathbf{f}$ | $\cdots$ |
| $A_2$ | $\mathbf{f}$ | $\mathbf{f}$ | $\mathbf{f}$ | $\mathbf{t}$ | $\cdots$ | $\mathbf{t}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\mathbf{f}$ | $\cdots$ | $\mathbf{t}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\cdots$ |
| $A_3$ | $\mathbf{f}$ | $\mathbf{f}$ | $\mathbf{f}$ | $\mathbf{f}$ | $\cdots$ | $\mathbf{t}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\cdots$ | $\mathbf{t}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\cdots$ |
| $A_4$ | $\mathbf{f}$ | $\mathbf{f}$ | $\mathbf{f}$ | $\mathbf{f}$ | $\cdots$ | $\mathbf{t}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\cdots$ | $\mathbf{t}$ | $\mathbf{t}$ | $\mathbf{t}$ | $\cdots$ |
| $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\ddots$ |

It is worth contrasting the behaviour of the sentence B and the sentence $A_0$. From the $\omega{+}1^{\text{th}}$ stage on, $B$ stabilizes as true. In fact, $B$ is stably true in every revision sequence for $M$. Thus, $B$ is categorically true in $M$. The sentence $A_0$, however, never quite stabilizes: it is usually true, but within a few finite stages of a limit ordinal, the sentence $A_0$ can be false. In these circumstances, we say that $A_0$ is *nearly stably true* (See Definition 3.10, below.) In fact, $A_0$ is nearly stably true in every revision sequence for $M. \Box$

Example 3.9 illustrates not only the notion of stability in a revision sequence, but also of near stability, which we define now:

**Definition 3.10.**

Suppose that $L$ is a truth language, and that $M = \langle D,I\rangle$ is a ground model. Suppose that $S$ is an $\textsf{On}$-long sequence of hypotheses. Then we say that $d \in D$ is *nearly stably* $\mathbf{t}$ $[\mathbf{f}]$ *in* $S$ iff for some ordinal $\theta$ we have for every $\zeta \ge \theta$, there is a natural number $n$ such that, for every $m \ge n, S_{\zeta +m}(d) = \mathbf{t}$ $[\mathbf{f}]$.

Gupta and Belnap 1993 characterize the difference between stability and near stability as follows: “Stability *simpliciter* requires an element [in our case a sentence] to settle down to a value $\mathbf{x}$ [in our case a truth value] after some initial fluctuations say up to [an ordinal $\eta$]… In contrast, near stability allows fluctuations after $\eta$ also, but these fluctuations must be confined to finite regions just after limit ordinals” (p. 169). Gupta and Belnap 1993 introduce two theories of truth, $\boldsymbol{T}^*$ and $\boldsymbol{T}^{\#}$, based on stability and near stability. Theorems 3.12 and 3.13, below, illustrate an advantage of the system $\boldsymbol{T}^{\#}$, i.e., the system based on near stability.

**Definition 3.11**

Suppose that $L$ is a truth language, and that $M = \langle D,I\rangle$ is a ground model. We say that a sentence $A$ is *valid in* $M$ *by* $\boldsymbol{T}^*$ iff $A$ is stably true in every revision sequence[^note-6]. And we say that a sentence $A$ is *valid in* $M$ *by* $\boldsymbol{T}^{\#}$ iff $A$ is nearly stably true in every revision sequence.

**Theorem 3.12**

Suppose that $L$ is a truth language, and that $M = \langle D,I\rangle$ is a ground model. Then, for every sentence $A$ of $L$, the following is valid in $M$ by $\boldsymbol{T}^{\#}$: $$ \boldsymbol{T}\lsquo \neg A\rsquo \equiv \neg \boldsymbol{T}\lsquo A\rsquo. $$

**Theorem 3.13**

There is a truth language $L$ and a ground model $M = \langle D,I\rangle$ and a sentence $A$ of $L$ such that the following is *not* valid in $M$ by $\boldsymbol{T}^*$: $$ \boldsymbol{T}\lsquo \neg A\rsquo \equiv \neg \boldsymbol{T}\lsquo A\rsquo. $$

Gupta and Belnap 1993, Section 6C, note similar advantages of $\boldsymbol{T}^{\#}$ over $\boldsymbol{T}^*$. For example, $\boldsymbol{T}^{\#}$ does, but $\boldsymbol{T}^*$ does not, validate the following semantic principles:

$$\begin{align} \boldsymbol{T}\lsquo A \amp B\rsquo &\equiv \boldsymbol{T}\lsquo A\rsquo \amp \boldsymbol{T}\lsquo B\rsquo \\ \boldsymbol{T}\lsquo A \vee B\rsquo &\equiv \boldsymbol{T}\lsquo A\rsquo \vee \boldsymbol{T}\lsquo B\rsquo \end{align}$$

Gupta and Belnap remain noncommittal about which of $\boldsymbol{T}^{\#}$ and $\boldsymbol{T}^*$ (and a further alternative that they define, $\boldsymbol{T}^c)$ is preferable.

## 4. Interpreting the formalism

The main formal notions of the RTT are the notion of a *revision rule* (Definition 3.2), i.e., a rule for revising hypotheses; and a *revision sequence* (Definition 3.7), a sequence of hypotheses generated in accordance with the appropriate revision rule. Using these notions, we can, given a ground model, specify when a sentence is *stably* (or *nearly stably) true* or *stably* (or *nearly stably) false* (Definition 3.6 and 3.10, respectively) in a particular revision sequence. Thus we could define two theories of truth, $\boldsymbol{T}^*$ and $\boldsymbol{T}^{\#}$ (Definition 3.11), based on stability and near stability (respectively). The final idea is that each of these theories delivers a verdict on which sentences of the language are *valid* (Definition 3.11), given a ground model.

Recall the suggestions made at the end of Section 2:

> In a semantics for languages capable of expressing their own truth concepts, $\boldsymbol{T}$ will not, in general, have a classical signification; and the ‘iff’ in the T-biconditionals will not be read as the classical biconditional.

Gupta and Belnap fill out these suggestions in the following way.

### 4.1 The signification of $\boldsymbol{T}$

First, they suggest that the signification of $\boldsymbol{T}$, given a ground model $M$, is the revision rule $\tau_M$ itself. As noted in the preceding paragraph, we can give a fine-grained analysis of sentences’ statuses and interrelations on the basis of notions generated directly and naturally from the revision rule $\tau_M$. Thus, $\tau_M$ is a good candidate for the signification of $\boldsymbol{T}$, since it does seem to be “an abstract something that carries all the information about all [of $\boldsymbol{T}$’s] extensional relations” in $M$. (See Gupta and Belnap’s characterization of an expression’s *signification*, given in Section 2, above.)

### 4.2 The ‘iff’ in the T-biconditionals

Gupta and Belnap’s related suggestion concerning the ‘iff’ in the T-biconditionals is that, rather than being the classical biconditional, this ‘iff’ is the distinctive biconditional used to *define* a previously undefined concept. In 1993, Gupta and Belnap present the revision theory of truth as a special case of a revision theory of *circularly defined concepts*. Suppose that $L$ is a language with a unary predicate $F$ and a binary predicate $R$. Consider a new concept expressed by a predicate $G$, introduced through a definition like this:

$$ Gx =_{df} \forall y(Ryx \supset Fx) \vee \exists y(Ryx \amp Gx). $$

Suppose that we start with a domain of discourse, $D$, and an interpretation of the predicate $F$ and the relation symbol $R$. Gupta and Belnap’s revision-theoretic treatment of concepts thus circularly introduced allows one to give categorical verdicts, for certain $d \in D$ about whether or not $d$ satisfies $G$. Other objects will be unstable relative to $G$: we will be able categorically to assert neither that $d$ satisfies $G$ nor that d does not satisfy $G$. In the case of truth, Gupta and Belnap take the set of T-biconditionals of the form

$$\tag{10} \boldsymbol{T}\lsquo A\rsquo =_{df} A $$

together to give the definition of the concept of truth. It is their treatment of ‘$=_{df}$’ (the ‘iff’ of definitional concept introduction), together with the T-biconditionals of the form (10), that determine the revision rule $\tau_M$.

### 4.3 The paradoxical reasoning

Recall the liar sentence, (1), from the beginning of this article:

**(1)**

(1) is not true

In Section 1, we claimed that the RTT is designed to model, rather than block, the kind of paradoxical reasoning regarding (1). But we noted in footnote 2 that the RTT does avoid contradictions in these situations. There are two ways to see this. First, while the RTT does endorse the biconditional

(1) is true iff (1) is not true,

the relevant ‘iff’ is not the material biconditional, as explained above. Thus, it does not follow that both (1) is true and (1) is not true. Second, note that on no hypothesis can we conclude that both (1) is true and (1) is not true. If we keep it firmly in mind that revision-theoretical reasoning is hypothetical rather than categorical, then we will not infer any contradictions from the existence of a sentence such as (1), above.

### 4.4 The signification thesis

Gupta and Belnap’s suggestions, concerning the signification of $\boldsymbol{T}$ and the interpretation of the ‘iff’ in the T-biconditionals, dovetail nicely with two closely related intuitions articulated in Gupta & Belnap 1993. The first intuition, loosely expressed, is “that the T-biconditionals are analytic and *fix* the meaning of ‘true’” (p. 6). More tightly expressed, it becomes the “Signification Thesis” (p. 31): “The T-biconditionals fix the signification of truth in every world [where a world is represented by a ground model].”[^note-7] Given the revision-theoretic treatment of the definition ‘iff’, and given a ground model $M$, the T-biconditionals (10) do, as noted, fix the suggested signification of $\boldsymbol{T}$, i.e., the revision rule $\tau_M$.

### 4.5 The supervenience of semantics

The second intuition is *the supervenience of the signification of truth*. This is a descendant of M. Kremer’s 1988 proposed *supervenience of semantics*. The idea is simple: which sentences fall under the concept *truth* should be fixed by (1) the interpretation of the nonsemantic vocabulary, and (2) the empirical facts. In non-circular cases, this intuition is particularly strong: the standard interpretation of “snow” and “white” and the empirical fact that snow is white, are enough to determine that the sentence “snow is white” falls under the concept *truth*. The supervenience of the signification of truth is the thesis that the signification of truth, whatever it is, is fixed by the ground model $M$. Clearly, the RTT satisfies this principle.

It is worth seeing how a theory of truth might violate this principle. Consider a truth-teller sentence, i.e., the sentence that says of itself that it is true:

**(11)**

(11) is true

As noted above, Kripke’s three-valued semantics allows three truth values, true $(\mathbf{t})$, false $(\mathbf{f})$, and neither $(\mathbf{n})$. Given a ground model $M = \langle D,I\rangle$ for a truth language $L$, the candidate interpretations of $\boldsymbol{T}$ are three-valued interpretations, i.e., functions $h:D \rightarrow \{\mathbf{t}, \mathbf{f}, \mathbf{n}\}$. Given a three-valued interpretation of $\boldsymbol{T}$, and a scheme for evaluating the truth value of composite sentences in terms of their parts, we can specify a truth value $\textit{Val}_{M+h}(A) = \mathbf{t}, \mathbf{f}$ or $\mathbf{n}$, for every sentence $A$ of $L$. The central theorem of the three-valued semantics is that, given any ground model $M$, there is a three-valued interpretation h of $\boldsymbol{T}$ so that, for every sentence $A$, we have $\textit{Val}_{M+h}(\boldsymbol{T}\lsquo A\rsquo) = \textit{Val}_{M+h}(A)$.[^note-8] We will call such an interpretation of $\boldsymbol{T}$ an *acceptable* interpretation. Our point here is this: if there’s a truth-teller, as in (11), then there is not only one acceptable interpretation of $\boldsymbol{T}$; there are three: one according to which (11) is true, one according to which (11) is false, and one according to which (11) is neither. Thus, there is no single “correct” interpretation of $\boldsymbol{T}$ given a ground model M. Thus the three-valued semantics seems to violate the supervenience of semantics.[^note-9]

The RTT does not assign a truth value to the truth-teller, (11). Rather, it gives an analysis of the kind of reasoning that one might engage in with respect to the truth-teller: If we start with a hypothesis $h$ according to which (11) is true, then upon revision (11) remains true. And if we start with a hypothesis $h$ according to which (11) is not true, then upon revision (11) remains not true. And that is all that the concept of truth leaves us with. Given this behaviour of (11), the RTT tells us that (11) is neither categorically true nor categorically false, but this is quite different from a verdict that (11) is neither true nor false.

### 4.6 A nonsupervenient interpretation of the formalism

We note an alternative interpretation of the revision-theoretic formalism. Yaqūb 1993 agrees with Gupta and Belnap that the T-biconditionals are definitional rather than material biconditionals, and that the concept of truth is therefore circular. But Yaqūb interprets this circularity in a distinctive way. He argues that,

> since the truth conditions of some sentences involve reference to truth in an essential, irreducible manner, these conditions can only obtain or fail in a world that already includes an extension of the truth predicate. Hence, in order for the revision process to determine an extension of the truth predicate, an *initial* extension of the predicate must be posited. This much follows from circularity and bivalence. (1993, 40)

Like Gupta and Belnap, Yaqūb posits no privileged extension for $\boldsymbol{T}$. And like Gupta and Belnap, he sees the revision sequences of extensions of $\boldsymbol{T}$, each sequence generated by an initial hypothesized extension, as “capable of accommodating (and diagnosing) the various kinds of problematic and unproblematic sentences of the languages under consideration” (1993, 41). But, unlike Gupta and Belnap, he concludes from these considerations that “*truth in a bivalent language is not supervenient*” (1993, 39). He explains in a footnote: for truth to be supervenient, the truth status of each sentence must be “fully determined by nonsemantical facts”. Yaqūb does not explicitly use the notion of a concept’s *signification*. But Yaqūb seems committed to the claim that the signification of $\boldsymbol{T}$ — i.e., that which determines the truth status of each sentence — is given by a particular revision sequence itself. And no revision sequence is determined by the nonsemantical facts, i.e., by the ground model, alone: a revision sequence is determined, at best, by a ground model and an initial hypothesis.[^note-10]

### 4.7 Classifying sentences

To obtain a signification of $\boldsymbol{T}$ and a notion of validity based on the concept of stability (or near stability) is by no means the only use we can make of revision sequences. For one thing, we could use revision-theoretic notions to make rather fine-grained distinctions among sentences: Some sentences are unstable in every revision sequence; others are stable in every revision sequence, though stably true in some and stably false in others; and so on. Thus, we can use revision-theoretic ideas to give a fine-grained analysis of the status of various sentences, and of the relationships of various sentences to one another. Hsiung (2017)[^hsiung-2017] explores further this possibility by generalizing the notion of a revision sequence to a *revision mapping* on a digraph, in order to extend this analysis to *sets* of sentences of a certain kind, called *Boolean paradoxes*. As shown in Hsiung 2022 this procedure can also be reversed, at least to some extent: Not only we can use revision sequences (or mappings) to classify paradoxical sentences by means of their revision-theoretic patterns, but we can also construct “new” paradoxes from given revision-theoretic patterns. Rossi (2019)[^rossi-2019] combines the revision-theoretic technique with graph-theoretic tools and fixed-point constructions in order to represent a threefold classification of paradoxical sentences (liar-like, truth-teller-like, and revenge sentences) within a single model.

## 5. Further issues

### 5.1 Three-valued semantics

We have given only the barest exposition of the three-valued semantics, in our discussion of the supervenience of the signification of truth, above. Given a truth language $L$ and a ground model $M$, we defined an *acceptable* three-valued interpretation of $\boldsymbol{T}$ as an interpretation $h:D \rightarrow \{\mathbf{t}, \mathbf{f}, \mathbf{n}\}$ such that $\textit{Val}_{M+h}(\boldsymbol{T}\lsquo A\rsquo) = \textit{Val}_{M+h}(A)$ for each sentence $A$ of $L$. In general, given a ground model $M$, there are many acceptable interpretations of $\boldsymbol{T}$. Suppose that each of these is indeed a truly acceptable interpretation. Then the three-valued semantics violates the supervenience of the signification of $\boldsymbol{T}$.

Suppose, on the other hand, that, for each ground model $M$, we can isolate a privileged acceptable interpretation as *the* correct interpretation of $\boldsymbol{T}$. Gupta and Belnap present a number of considerations against the three-valued semantics, so conceived. (See Gupta & Belnap 1993, Chapter 3.)[^gupta-1993] One principal argument is that the central theorem, i.e., that for each ground model there is an acceptable interpretation, only holds when the underlying language is expressively impoverished in certain ways: for example, the three-valued approach fails if the language has a connective ${\sim}$ with the following truth table:

| $A$ | ${\sim}A$ |
| --- | --- |
| $\mathbf{t}$ | $\mathbf{f}$ |
| $\mathbf{f}$ | $\mathbf{t}$ |
| $\mathbf{n}$ | $\mathbf{t}$ |

The only negation operator that the three-valued approach can handle has the following truth table:

| $A$ | $\neg A$ |
| --- | --- |
| $\mathbf{t}$ | $\mathbf{f}$ |
| $\mathbf{f}$ | $\mathbf{t}$ |
| $\mathbf{n}$ | $\mathbf{n}$ |

But consider the liar that says of itself that it is ‘not’ true, in this latter sense of ‘not’. Gupta and Belnap urge the claim that this sentence “ceases to be intuitively paradoxical” (1993, 100). The claimed advantage of the RTT is its ability to describe the behaviour of genuinely paradoxical sentences: the genuine liar is unstable under semantic evaluation: “No matter what we hypothesize its value to be, semantic evaluation refutes our hypothesis.” The three-valued semantics can only handle the “weak liar”, i.e., a sentence that only weakly negates itself, but that is not guaranteed to be paradoxical: “There are appearances of the liar here, but they deceive.”

We’ve thus far reviewed two of Gupta and Belnap’s complaints against three-valued approaches, and now we raise a third: in the three-valued theories, truth typically behaves like a nonclassical concept even when there’s no vicious reference in the language. Without defining terms here, we note that one popular precisification of the three-valued approach, is to take the correct interpretation of T to be that given by the ‘least fixed point’ of the ‘strong Kleene scheme’: putting aside details, this interpretation always assigns the truth value $\mathbf{n}$ to the sentence $\forall$x$(\boldsymbol{T}$x $\vee \neg \boldsymbol{T}$x), even when the ground model allows no circular, let alone vicious, reference. Gupta and Belnap claim an advantage for the RTT: according to revision-theoretic approach, they claim, truth always behaves like a classical concept when there is no vicious reference.

Kremer 2010 challenges this claim by precisifying it as a formal claim against which particular revision theories (e.g. $\boldsymbol{T}^*$ or $\boldsymbol{T}^{\#}$, see Definition 3.11, above) and particular three-valued theories can be tested. As it turns out, on many three-valued theories, truth does in fact behave like a classical concept when there’s no vicious reference: for example, the least fixed point of a natural variant of the supervaluation scheme always assigns $\boldsymbol{T}$ a classical interpretation in the absence of vicious reference. When there’s no vicious reference, it is granted that truth behaves like a classical concept if we adopt Gupta and Belnap’s theory $\boldsymbol{T}^*$, however, so Kremer argues, this is not the case if we instead adopt Gupta and Belnap’s theory $\boldsymbol{T}^{\#}$. This discussion is further taken up by Wintein 2014. A general assessment of the relative merits of the three-valued approaches and the revision-theoretic approaches, from a metasemantic point of view, is at the core of Pinder 2018.

### 5.2 Two values?

A contrast presupposed by this entry is between allegedly two-valued theories, like the RTT, and allegedly three-valued or other many-valued rivals. One might think of the RTT itself as providing infinitely many semantic values, for example one value for every possible revision sequence. Or one could extract three semantic values for sentences: categorical truth, categorical falsehood, and uncategoricalness.

In reply, it must be granted that the RTT generates many *statuses* available to sentences. Similarly, three-valued approaches also typically generate many statuses available to sentences. The claim of two-valuedness is not a claim about statuses available to sentences, but rather a claim about the *truth values* presupposed in the whole enterprise.

### 5.3 Amendments to the RTT

We note three ways to amend the RTT. First, we might put constraints on which hypotheses are acceptable. For example, Gupta and Belnap 1993 introduce a theory, $\mathbf{T}^c$, of truth based on *consistent* hypotheses: an hypothesis $h$ is *consistent* iff the set $\{A:h(A) = \mathbf{t}\}$ is a complete consistent set of sentences. The relative merits of $\mathbf{T}^*, \mathbf{T}^{\#}$ and $\mathbf{T}^c$ are discussed in Gupta & Belnap 1993, Chapter 6.

Second, we might adopt a more restrictive *limit policy* than Gupta and Belnap adopt. Recall the question asked in Section 3: How should we set $S_{\eta}(d)$ when $\eta$ is a limit ordinal? We gave a partial answer: any object that is stably true [false] *up to* that stage should be true [false] *at* that stage. We also noted that for an object $d \in D$ that does not stabilize up to the stage $\eta$, Gupta and Belnap 1993 allow us to set $S_{\eta}(d)$ as either $\mathbf{t}$ or $\mathbf{f}$. In a similar context, Herzberger 1982a and 1982b assigns the value $\mathbf{f}$ to the unstable objects. And Gupta originally suggested, in Gupta 1982, that unstable elements receive whatever value they received at the initial hypothesis $S_0$.

These first two ways of amending the RTT both, in effect, restrict the notion of a revision sequence, by putting constraints on which of *our* revision sequences really count as acceptable revision sequences. The constraints are, in some sense local: the first constraint is achieved by putting restrictions on which hypotheses can be used, and the second constraint is achieved by putting restrictions on what happens at limit ordinals. A third option would be to put more global constraints on which putative revision sequences count as acceptable. Yaqūb 1993 suggests, in effect, a limit rule whereby acceptable verdicts on unstable sentences at some limit stage $\eta$ depend on verdicts rendered at *other* limit stages. Yaqūb argues that these constraints allow us to avoid certain “artifacts”. For example, suppose that a ground model $M = \langle D,I\rangle$ has two independent liars, by having two names $\alpha$ and $\beta$, where $I(\alpha) = \neg \boldsymbol{T}\alpha$ and $I(\beta) = \neg \boldsymbol{T}\beta$. Yaqūb argues that it is a mere “artifact” of the revision semantics, naively presented, that there are revision sequences in which the sentence $\neg \boldsymbol{T}\alpha \equiv \neg \boldsymbol{T}\beta$ is stably true, since the two liars are independent. His global constraints are developed to rule out such sequences. (See Chapuis 1996 for further discussion.)[^chapuis-1996]

The first and the second way of amending the RTT are in some sense put together by Campbell-Moore (2019)[^campbell-moore-2019][^campbell-moore-2019-2]. Here, the notion of stability for objects is extended to sets of hypotheses: A set $H$ of hypotheses is stable in a sequence $S$ of hypotheses if for some ordinal $\theta$ all hypotheses $S_{\zeta}$, with $\zeta \ge \theta$, belong to $H$. With this, we can introduce the notion of $P$-revision sequence: If $P$ is a class of sets of hypotheses, a sequence $S$ is a $P$-revision sequence just in case that, at every limit ordinal $\eta$, if a set of hypotheses $H$ belongs to $P$ and is stable in $S$, then $S_{\eta}$ belongs to $H$. It can be shown that, for a suitable choice of $P$, all limit stages of $P$-revision sequences are *maximal consistent* hypotheses.

### 5.4 Revision theory for circularly defined concepts

As indicated in our discussion, in Section 4, of the ‘iff’ in the T-biconditionals, Gupta and Belnap present the RTT as a special case of a revision theory of circularly defined concepts. To reconsider the example from Section 4. Suppose that $L$ is a language with a unary predicate F and a binary predicate R. Consider a new concept expressed by a predicate $G$, introduced through a definition, $D$, like this:

$$ Gx =_{df} A(x,G) $$

where $A(x,G)$ is the formula

$$ \forall y(Ryx \supset Fx) \vee \exists y(Ryx \amp Gx). $$

In this context, a *ground model* is a classical model $M = \langle D,I\rangle$ of the language $L$: we start with a domain of discourse, $D$, and an interpretation of the predicate $F$ and the relation symbol $R$. We would like to extend $M$ to an interpretation of the language $L + G$. So, in this context, an hypothesis will be thought of as an hypothesized extension for the newly introduced concept $G$. Formally, a hypothesis is simply a function $h:D \rightarrow \{\mathbf{t}, \mathbf{f}\}$. Given a hypothesis $h$, we take $M+h$ to be the classical model $M+h = \langle D,I'\rangle$, where $I'$ interprets $F$ and $R$ in the same way as $I$, and where $I'(G) = h$. Given a hypothesized interpretation $h$ of $G$, we generate a new interpretation of $G$ as follows: and object $d \in D$ is in the new extension of $G$ just in case the defining formula $A(x,G)$ is true of $d$ in the model $M+h$. Formally, we use the ground model $M$ and the definition $D$ to define a *revision rule*, $\delta_{D,M}$, mapping hypotheses to hypotheses, i.e., hypothetical interpretations of $G$ to hypothetical interpretations of $G$. In particular, for any formula $B$ with one free variable $x$, and $d \in D$, we can define the truth value $\textit{Val}_{M+h,d}(B)$ in the standard way. Then,

$$ \delta_{D,M}(h)(d) = \textit{Val}_{M+h,d}(A) $$

Given a revision rule $\delta_{D,M}$, we can generalize the notion of a *revision sequence*, which is now a sequence of hypothetical extensions of $G$ rather than $\boldsymbol{T}$. We can generalize the notion of a sentence $B$ being *stably true*, *nearly stably true*, etc., relative to a revision sequence. Gupta and Belnap introduce the systems $\mathbf{S}^*$ and $\mathbf{S}^{\#}$, analogous to $\mathbf{T}^*$ and $\mathbf{T}^{\#}$, as follows:[^note-11]

> **Definition 5.1.**
>
> - A sentence $B$ is *valid on the definition* $D$ *in the ground model* $M$ *in the system* $\mathbf{S}^*$ (notation $M \vDash_{*,D} B)$ iff $B$ is stably true relative to each revision sequence for the revision rule $\delta_{D,M}$.
> - A sentence $B$ is *valid on the definition* $D$ *in the ground model* $M$ *in the system* $\mathbf{S}^{\#}$ (notation $M \vDash_{\#,D} B)$ iff $B$ is *nearly* stably true relative to each revision sequence for the revision rule $\delta_{D,M}$.
> - A sentence $B$ is *valid on the definition* $D$ *in the system* $\mathbf{S}^*$ (notation $\vDash_{*,D} B)$ iff for all classical ground models $M$, we have $M \vDash_{*,D} B$.
> - A sentence $B$ is *valid on the definition* $D$ *in the system* $\mathbf{S}^{\#}$ (notation $\vDash_{\#,D} B)$ iff for all classical ground models $M$, we have $M \vDash_{\#,D} B$.

One of Gupta and Belnap’s principle open questions is whether there is a complete calculus for these systems: that is, whether, for each definition $D$, either of the following two sets of sentences is recursively axiomatizable: $\{B:\vDash_{*,D} B\}$ and $\{B:\vDash_{\#,D} B\}$. Kremer 1993 proves that the answer is no: he shows that there is a definition $D$ such that each of these sets of sentences is of complexity at least $\Pi^{1}_2$, thereby putting a lower limit on the complexity of $\mathbf{S}^*$ and $\mathbf{S}^{\#}$. (Antonelli 1994a and 2002 shows that this is also an upper limit.)[^antonelli-1994a][^antonelli-2002]

Kremer’s proof exploits an intimate relationship between circular definitions understood *revision*-theoretically and circular definitions understood as *inductive* definitions: the theory of inductive definitions has been quite well understood for some time. In particular, Kremer proves that every inductively defined concept can be revision-theoretically defined. The expressive power and other aspects of the revision-theoretic treatment of circular definitions is the topic of much interesting work: see Welch 2001, Löwe 2001, Löwe and Welch 2001, and Kühnberger *et al*. 2005.

Alongside Kremer’s limitative result there is the positive observation that, for some semantic system of definitions based on restricted kinds of revision sequences, sound and complete calculi *do* exist. For instance, Gupta and Belnap give some examples of calculi and revision-theoretic systems which use only finite revision sequences. Further investigation on proof-theoretic calculi capturing some revision-theoretic semantic systems is done in Bruni 2013, Standefer 2016, Bruni 2019, and Fjellstad 2020.

### 5.5 Axiomatic Theories of Truth and the Revision Theory

The RTT is a clear example of a semantically motivated theory of truth. Quite a different tradition seeks to give a satisfying axiomatic theory of truth. Granted we cannot retain all of classical logic and all of our intuitive principles regarding truth, especially if we allow vicious self-reference. But maybe we can arrive at satisfying axiom systems for truth, that, for example, maintain consistency and classical logic, but give up only a little bit when it comes to our intuitive principles concerning truth, such as the T-biconditionals (interpreted classically); or maintain consistency and all of the T-biconditionals, but give up only a little bit of classical logic. Halbach 2011 comprehensively studies such axiomatic theories (mainly those that retain classical logic), and Horsten 2011 is in the same tradition. Both Chapter 14 of Halbach 2011 and Chapter 8 of Horsten 2011 study the relationship between the Friedman-Sheard theory FS and the revision semantics, with some interesting results. For more work on axiomatic systems and the RTT, see Horsten et al 2012.

Field 2008 makes an interesting contribution to axiomatic theorizing about truth, even though most of the positive work in the book consists of model building and is therefore semantics. In particular, Field is interested in producing a theory as close to classical logic as possible, which retains all T-biconditionals (the conditional itself will be nonclassical) and which at the same time can express, in some sense, the claim that such and such a sentence is defective. Field uses tools from multivalued logic, fixed-point semantics, and revision theory to build models showing, in effect, that a very attractive axiomatic system is consistent. Field’s construction is an intricate interplay between using fixed-point constructions for successively interpreting T, and revision sequences for successively interpreting the nonclassical conditional — the final interpretation being determined by a sort of super-revision-theoretic process.

The connection between revision and Field’s theory is explored further in Standefer 2015b and in Gupta and Standefer 2017.

### 5.6 Applications

Given Gupta and Belnap’s general revision-theoretic treatment of circular definitions — of which their treatment of *truth* is a special case — one would expect revision-theoretic ideas to be applied to other concepts. Antonelli 1994b applies these ideas to non-well-founded sets: a non-well-founded set $X$ can be thought of as circular, since, for some $X_0 , \ldots ,X_n$ we have $X \in X_0 \in \ldots \in X_n \in X$. Chapuis 2003 applies revision-theoretic ideas to rational decision making. This connection is further developed by Bruni 2015 and by Bruni and Sillari 2018. For a discussion of revision theory and abstract objects see Wang 2011. For a discussion of revision theory and vagueness, see Asmus 2013.

Standefer (2015a)[^standefer-2015a] studies the connection between the circular definitions of revision theory and a particular modal logic RT (for “Revision Theory”). Campbell-Moore *et al.* 2019 and Campbell-Moore 2021 use revision sequences to model probabilities and credences, respectively. Cook 2019 employs a revision-theoretic analysis to find a new possible solution of Benardete’s version of the Zeno paradox.

In recent times, there has been increasing interest in bridging the gap between classic debates on the nature of truth — deflationism, the correspondence theory, minimalism, pragmatism, and so on — and formal work on truth, motivated by the liar’s paradox. The RTT is tied to pro-sententialism by Belnap 2006; deflationism, by Yaqūb 2008; and minimalism, by Restall 2005.

We must also mention Gupta 2006. In this work, Gupta argues that an experience provides the experiencer, not with a straightforward entitlement to a proposition, but rather with a hypothetical entitlement: as explicated in Berker 2011, if subject S has experience $e$ and is entitled to hold view $v$ (where S’s *view* is the totality of S’s concepts, conceptions, and beliefs), then S is entitled to believe a certain class of perceptual judgements, $\Gamma(v)$. (Berker uses “propositions” instead of “perceptual judgements” in his formulation.) But this generates a problem: how is S entitled to hold a view? There seems to be a circular interdependence between entitlements to views and entitlements to perceptual judgements. Here, Gupta appeals to a general form of revision theory — generalizing beyond both the revision theory of truth and the revision theory of circularly defined concepts (Section 5.4, above) — to given an account of how “hypothetical perceptual entitlements could yield categorical entitlements” (Berker 2011)[^berker-2011].

### 5.7 An open question

We close with an open question about $\mathbf{T}^*$ and $\mathbf{T}^{\#}$. Recall Definition 3.11, above, which defines when a sentence $A$ of a truth language $L$ is *valid in the ground model* $M$ *by* $\mathbf{T}^*$ or *by* $\mathbf{T}^{\#}$. We will say that $A$ is *valid by* $\mathbf{T}^*$ [alternatively, *by* $\mathbf{T}^{\#}$] iff $A$ is valid in the ground model $M$ by $\mathbf{T}^*$ [alternatively, by $\mathbf{T}^{\#}$] for every ground model $M$. Our open question is this: What is the complexity of the set of sentences valid by $\mathbf{T}^* [\mathbf{T}^{\#}$]?

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=truth-revision). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/truth-revision/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=truth-revision&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/truth-revision/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- Hammer, E., 2003, “The Revision Theory of Truth”, *The Stanford Encyclopedia of Philosophy* (Spring 2003 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/spr2003/entries/truth-revision/](https://plato.stanford.edu/archives/spr2003/entries/truth-revision/)>. (This was the entry on the revision theory of truth which appeared in the active portion of the SEP from 1997–2006.)

## Related Entries

Curry’s paradox | definitions | liar paradox | Tarski, Alfred: truth definitions | truth | truth: axiomatic theories of

## Notes（原文脚注）

[^note-1]: Kripke prefers to treat *neither* not as a third truth value but as the absence of a truth value.

[^note-2]: The RTT is also designed to avoid contradictions in these situations, so the last step, to (1) being both true and not true, will be blocked. See Section 4, below.

[^note-3]: Proving this would, of course, necessitate explicating in detail the various ways of implementing the three-valued approach.

[^note-4]: For an $n$-ary predicate $R$, standard presentations of classical model theory require $I(R)$ to be a subset of $D^n$. Clause (2c) is clearly equivalent to that, but will be slightly easier to generalize to three-valued logics.

[^note-5]: Permanently declaring nonsentences to be nontrue is an inessential feature of the RTT. We could allow the revision rule only to specify the value of sentences, allowing nonsentences to be in or out of the extension of $\boldsymbol{T}$, willy-nilly. One complication with this is that the rule would not determine the new hypothesis given the old, since it would not determine the new hypothesis’s verdicts concerning nonsentences.

[^note-6]: According to the definition, a sentence $A$ is *valid in* $M$ *by* $\boldsymbol{T}^*$ iff $A$ is *categorically true in* $M$.

[^note-7]: See Section 2 for the notion of a concept’s or predicate’s *signification*.

[^note-8]: This ‘fixed-point’ theorem holds if our scheme for evaluating the truth of composite sentences has a certain nice property of *monotonicity*, which we will not define here.

[^note-9]: There are common interpretations of the three-valued semantics according to which one of the many ‘acceptable’ interpretations of $\boldsymbol{T}$ can be picked out as *the* correct interpretation. This would restore the supervenience of semantics in the Kripkean context. M. Kremer 1988 argues that these interpretations violate the *fixed-point conception of truth*, according to which the concept of truth is exhausted by the following: truth can be asserted of a sentence iff that sentence can be asserted, and denied of a sentence iff that sentence can be denied. In correspondence with the author, Kripke has endorsed M. Kremer’s understanding of the three-valued semantics.

[^note-10]: And not even that: we need to make certain decisions at the limit ordinal stages.

[^note-11]: The definitions we give are not theirs, but are equivalent to theirs.

[^antonelli-1994a]: Antonelli, G.A., 1994a, “The complexity of revision”, *Notre Dame Journal of Formal Logic*, 35: 204–218.

[^antonelli-1994b]: –––, 1994b, “Non-well-founded sets via revision rules”, *Journal of Philosophical Logic*, 23: 633–679.

[^antonelli-2002]: –––, 2002, “The complexity of revision, revised”, *Notre Dame Journal of Formal Logic*, 43: 75–78.

[^asmus-2013]: Asmus C.M., 2013, “Vagueness and revision sequences”, *Synthese*, 190: 953–974.

[^belnap-1982]: Belnap, N., 1982, “Gupta’s rule of revision theory of truth”, *Journal of Philosophical Logic*, 11: 103–116.

[^belnap-2006]: –––, 2006, “Prosentence, Revision, Truth, and Paradox”, *Philosophy and Phenomenological Research*, 73: 705–712.

[^berker-2011]: Berker S., 2011, “Gupta’s gambit”, *Philosophical Studies*, 152: 17–39.

[^bruni-2013]: Bruni, R., 2013, “Analytic calculi for circular concepts by finite revision”, *Studia Logica*, 101(5): 915–932.

[^bruni-2015]: –––, 2015, “Some remarks on the finite theory of revision”, in *Unifying the Philosophy of Truth*, Achourioti *et al*. (eds.), Dordrecht: Springer, 169–187.

[^bruni-2019]: –––, 2019, “Addressing circular definitions via systems of proofs”, in *Mathesis Universalis, Computability and Proof* (Synthese Library 412), Centrone *et al*. (eds.), Cham: Springer, 75–100.

[^bruni-2018]: Bruni, R., and Sillari, G., 2018, “A rational way of playing: Revision theory for strategic interaction”, *Journal of Philosophical Logic*, 47(3): 419–448.

[^campbell-moore-2019]: Campbell-Moore, C., 2019, “Limits in the revision theory”, *Journal of Philosophical Logic*, 48(1): 11–35.

[^campbell-moore-2021]: –––, 2021, “Indeterminate Truth and Credences”, in *Modes of Truth* (Routledge Studies in Contemporary Philosophy), London: Routledge, 182–208.

[^campbell-moore-2019-2]: Campbell-Moore, C., Horsten, L., and Leitgeb, H., 2019, “Probability for the revision theory of truth”, *Journal of Philosophical Logic*, 48(1): 87–112.

[^chapuis-1996]: Chapuis, A., 1996, “Alternate revision theories of truth”, *Journal of Philosophical Logic*, 25: 399–423.

[^chapuis-2003]: –––, 2003, “An application of circular definitions: rational decision”, in Löwe, Malzkorn, and Räsch (eds.), *Foundations of the Formal Sciences II: Applications of Mathematical Logic in Philosophy and Linguistics*, Dordrecht: Kluwer, 47–54.

[^cook-2019]: Cook, R. T., 2019, “Revising Benardete’s Zeno”, *Journal of Philosophical Logic*, 48(1): 37–56.

[^field-2008]: Field H., 2008, *Saving Truth from Paradox*, Oxford: Oxford University Press.

[^fjellstad-2020]: Fjellstad, A., 2020, “Herzberger’s limit rule with labelled sequent calculus”, *Studia Logica*, 108(4): 815–855.

[^gupta-1982]: Gupta, A., 1982, “Truth and paradox”, *Journal of Philosophical Logic*, 11: 1–60.

[^gupta-2006]: –––, 2006, *Empiricism and Experience*, Oxford: Oxford University Press.

[^gupta-1993]: Gupta, A., and Belnap, N., 1993, *The Revision Theory of Truth*, Cambridge, MA: MIT Press.

[^gupta-2017]: Gupta, A., and Standefer, S., 2017, “Conditionals in theories of truth”, *Journal of Philosophical Logic*, 46(1): 27–63.

[^halbach-2011]: Halbach, V., 2011, *Axiomatic Theories of Truth*, Cambridge: Cambridge University Press.

[^hammer-2003]: Hammer, E., 2003, “The Revision Theory of Truth”, *The Stanford Encyclopedia of Philosophy* (Spring 2003 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/spr2003/entries/truth-revision/](https://plato.stanford.edu/archives/spr2003/entries/truth-revision/)>.

[^herzberger-1982]: Herzberger, H.G., 1982, “Notes on naive semantics”, *Journal of Philosophical Logic*, 11: 61–102.

[^herzberger-1982-2]: –––, 1982, “Naive semantics and the liar paradox”, *Journal of Philosophy*, 79: 479–497.

[^horsten-2011]: Horsten, L., 2011, *The Tarskian Turn: Deflationism and Axiomatic Truth*, Cambridge, MA: MIT Press.

[^horsten-2012]: Horsten, L., Leigh, G.E., Leitgeb, H., and Welch, P., 2012, “Revision Revisited”, *The Review of Symbolic Logic*, 5: 642–665.

[^hsiung-2017]: Hsiung, M., 2017, “Boolean paradoxes and revision periods”, *Studia Logica*, 105(5): 881–914.

[^hsiung-2022]: –––, 2022, “Designing Paradoxes: A Revision-theoretic Approach”, *Journal of Philosophical Logic*, 51: 739–789.

[^kremer-1988]: Kremer, M., 1988, “Kripke and the logic of truth”, *Journal of Philosophical Logic*, 17: 225–78.

[^kremer-1993]: Kremer, P., 1993, “The Gupta-Belnap systems $\mathbf{S}^{\#}$ and $\mathbf{S}^*$ are not axiomatisable”, *Notre Dame Journal of Formal Logic*, 34: 583–596.

[^kremer-2010]: –––, 2010, “How Truth Behaves When There’s No Vicious Reference”, *Journal of Philosophical Logic*, 39: 345–367.

[^kripke-1975]: Kripke, S., 1975, “Outline of a theory of truth”, *Journal of Philosophy*, 72: 690–716.

[^kühnberger-2005]: Kühnberger, K., Löwe, B., Möllerfeld, M., and Welch, P., 2005, “Comparing inductive and circular definitions: parameters, complexity and games”, *Studia Logica*, 81: 79–98.

[^löwe-2001]: Löwe, B., 2001 “Revision sequences and computers with an infinite amount of time”, *Journal of Logic and Computation*, 11: 25–40.

[^löwe-2001-2]: Löwe, B., and Welch, P., 2001, “Set-theoretic absoluteness and the revision theory of truth”, *Studia Logica*, 68(1): 21–41.

[^martin-1975]: Martin, R., and Woodruff, P., 1975, “On representing ‘True-in-L’ in L”, *Philosophia*, 5: 217–221.

[^pinder-2018]: Pinder, M., 2018, “How to find an attractive solution to the liar paradox”, *Philosophical Studies*, 175(7): 1661–1680.

[^restall-2005]: Restall, G., 2005, “Minimalists about Truth Can (and Should) Be Epistemicists, and it Helps if They Are Revision Theorists too”, in *Deflation and Paradox*, JC Beall and B. Armour-Garb (eds.), Oxford: Oxford University Press, 97–106.

[^rossi-2019]: Rossi, L., 2019, “A unified theory of truth and paradox”, *The Review of Symbolic Logic*, 12(2): 209–254.

[^standefer-2015a]: Standefer, S., 2015a, “Solovay-type theorems for circular definitions”, *The Review of Symbolic Logic*, 8(3): 467–487.

[^standefer-2015b]: –––, 2015b, “On artifacts and truth-preservation”, *Australasian Journal of Logic*, 12(3): 135–158.

[^standefer-2016]: –––, 2016, “Contraction and revision”, *Australasian Journal of Logic*, 13(3): 58–77.

[^wang-2011]: Wang, W., 2011, “Theories of abstract objects without ad hoc restriction”, *Erkenntnis* 74: 1–15.

[^welch-2001]: Welch, P., 2001, “On Gupta-Belnap revision theories of truth, Kripkean fixed points, and the Next stable set”, *Bulletin for Symbolic Logic*, 7: 345–360.

[^wintein-2014]: Wintein, S., 2014, “Alternative Ways for Truth to Behave When There’s no Vicious Reference”, *Journal of Philosophical Logic* 43: 665–690.

[^yaqūb-1993]: Yaqūb, A., 1993, *The Liar Speaks the Truth : A Defense of the Revision Theory of Truth*, Oxford: Oxford University Press.

[^yaqūb-2008]: –––, 2008, “Two types of deflationist”, *Synthese*, 165: 77–106.
