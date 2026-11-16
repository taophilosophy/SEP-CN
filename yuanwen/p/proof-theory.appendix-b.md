# proof-theory — appendix-b（supplement）

> （《proof-theory》词条补充材料，源：plato.stanford.edu/entries/proof-theory/appendix-b.html）

#### Supplement to Proof Theory

## B. Turing’s and Feferman’s Results on Recursive Progressions

We will give a proof of Turing’s completeness Theorem 5.2 to be able to discuss its scope. Moreover, we shall also look at Feferman’s much stronger result about progressions based on the uniform reflection principle. As to the hierarchies that have been studied most frequently, please refer to section 5.2. The existence of primitive recursive functions $n\mapsto \psi_n$ in the definition of the different progressions is an easy consequence of the primitive recursion theorem.[^note-49] If all axioms of **T** a true (in the standard model) it can be shown for all $a\in \cO$ by transfinite induction on $\left|a\right|$ that $\bT_a$ is a true theory (in a sufficiently strong metatheory). For numbers *a* outside $\cO$ the theories $\bT_a$ bear no interest. They may actually be inconsistent. For example, the recursion theorem ensures that there exists an *e* such that $\{e\}(0)=\rsuc(\rlim(e))$. As $\bT_{\{e\}(0)} \subseteq \bT_{\rlim(e)}$ and $\bT_{\{e\}(0)}$ proves the consistency of $\bT_{\rlim(e)}$, both theories are inconsistent.

Recall that Turing’s completeness result, Theorem 5.2, asserts that for any true $\Pi^0_1$ sentence *φ* a number $a_{\phi}\in{\cO}$ with ${\left| a_{\phi}\right|}=\omega+1$ can be constructed such that $\bT_{a_{\phi}}\vdash \phi$. Moreover, the function $\phi\mapsto a_{\phi}$ is primitive recursive. The proof proceeds as follows: Let *θ* be $\forall x\,\psi(x)$ with *ψ* primitive recursive. Define *e* by the recursion theorem such that, provably in **PA**,

$${\{e\}(n)} = \left\{ \begin{array}{ll} n_{\cO} & \textrm{if } \psi(\bar{k}) \textrm{ is true for every } k\leq n \\ \rsuc(\rlim(e)) &\textrm{otherwise.} \end{array}\right.$$

Note that $\{e\}$ is total (by induction on *n*). As *θ* is true, we have ${\{e\}(n)}=n_{{\cO}}$ for all *n*. Thus ${\rlim}(e)$ belongs to ${\cO}$ and $\left|{\rlim}(e)\right|=\omega$. We claim that the consistency of $\bT_{{\rlim}(e)}$ entails that *θ* is true. For if *θ* were false we would have $\neg\psi(\bar{m})$ for some *m* and thus $\bT_{{\{e\}(n)}}=\bT_{{\rsuc}({\rlim}(e))}$ for all $n\geq m$. But, by design, $\bT_{{\rsuc}({\rlim}(e))}$ proves the consistency of $\bT_{{\rlim}(e)}$ and $\bT_{{\{e\}(n)}}$ is a subtheory of $\bT_{{\rlim}(e)}$ for all *n*. Thus $\bT_{{\rlim}(e)}$ would prove its own consistency, rendering it inconsistent (by Gödel’s second incompleteness theorem). The foregoing reasoning can be formalized in **PA** and a fortiori in $\bT_{{\rsuc}({\rlim}(e))}$. As a result, $\bT_{{\rsuc}({\rlim}(e))}\vdash \theta$.

This proof is based on the trick of coding the truth of *θ* as a member of ${\cO}$. It shows that the infinitely many iterated consistency axioms $\Con (\bT_0),\Con (\bT_1),\ldots$ of $\bT_{{\rsuc}({\rlim}(e))}$ play no role in proving *θ*. The reason why one has to go to stage $\omega+1$ is simply that only at stage *ω* a non-standard definition of the axioms of $\bigcup_{n<\omega}\bT_n$ can be introduced. And actually a non-standard definition of the axioms of $\bT_0$ would serve the same purpose. Setting $\vartheta(v_0):\Leftrightarrow \psi(v_0) \lor(\exists x\,\neg\psi(x)\land v_0={\Corner{0=1}})$, the theory $\bT_0'$ defined by the $\Sigma^0_1$-formula *ϑ* has the same axioms as $\bT_0$, but the consistency of $\bT_0'$ implies *θ* (provably so in **PA**). Also note that epistemologically recognizing that ${{\rsuc}({\rlim}(e))}$ is in ${\cO}$ hinges on us knowing that *θ* is true, and hence nothing is gained by further knowing that $\bT_{{\rsuc}({\rlim}(e))}\vdash \theta$.

The proof of the Theorem 5.2 works with any consistency progression. Turing actually considered slightly stronger progressions in that he used a special version of local reflection progressions, where (R2) is restricted to $\Pi^0_2$-sentences, i.e., sentences of $\forall\exists$ form with primitive recursive matrix. He took as one of his main aims to show that these progressions are complete for $\Pi^0_2$-sentences. However, this is not the case as we have shown.

Theorem B.1 Let $(\bT_a)_{a\in{\cO}}$ be a progression based on the local reflection principle. Then the following hold:

1. $\bigcup_{a\in{\cO}} \bT_a \subseteq \bT_0+$ all true $\Pi^0_1$-sentences.
2. There is a true $\Pi^0_2$-sentence that is not provable in $\bigcup_{a\in{\cO}} \bT_a$.

**Proof**: Let $\bT^*:= \bT_0+\mbox{all true $\Pi^0_1$-sentences}$.

1. We show by induction on $a\in{\cO}$ that $\bT_a\subseteq \bT^*$. Only the successor step needs to be looked at. So suppose $a={\rsuc}(b)$ and $\bT_b\subseteq \bT^*$. It suffices to show that $\bT^*\vdash \sfPr_{\bT_b}({\Corner{\phi}})\to \phi$ holds for every sentence *φ*. There are two cases to consider. If $\sfPr_{\bT_b}({\Corner{\phi}})$ is false then $\neg \sfPr_{\bT_b}({\Corner{\phi}})$ is a true $\Pi^0_1$-sentence and hence $\bT^*\vdash \neg \sfPr_{\bT_b}({\Corner{\phi}})$ which entails $\bT^*\vdash \sfPr_{\bT_b}({\Corner{\phi}})\to \phi$. If $\sfPr_{\bT_b}({\Corner{\phi}})$ is true then $\bT_b\vdash \phi$ and, by the induction hypothesis, $\bT^*\vdash \phi$ which also yields $\bT^*\vdash \sfPr_{\bT_b}({\Corner{\phi}})\to \phi$.
2. The provability predicate for $\bT^*$ is of complexity $\Sigma^0_2$. If $\bigcup_{a\in{\cO}} \bT_a$ proved all true $\Pi^0_2$-sentences then $\bT^*$ would be $\Pi^0_2$-complete. But that is absurd on account of the arithmetical hierarchy theorem.

The problem left open after Turing’s thesis, namely whether any stronger progressions can be complete for $\Pi^0_2$-statements, was addressed by Feferman (1962) with the surprising result that progressions based on the uniform reflection principle were not only complete with respect to $\Pi^0_2$-sentences but for all arithmetical sentences.

Theorem B.2 (Feferman’s completeness theorem 1962) Let $(\bT_a)_{a\in{\cO}}$ be a progression based on the uniform reflection principle with $\bT_0=\PA$.

For any true arithmetical sentence *θ* there exists $a\in{\cO}$ such that $\bT_a\vdash \theta$. Moreover, $a\in{\cO}$ can be chosen such that $\left|a\right| <\omega^{\omega^{\omega+1}}$.

In contrast to Turing’s result, Theorem 5.2, the proof of B.2 is rather difficult; it also utilizes a theorem from Shoenfield 1959 stating that Peano arithmetic with the recursive *ω*-rule is complete for arithmetical statements.[^note-50] However, as far as mathematical knowledge is concerned, the same circularity as in Turing’s completeness theorem obtains in Theorem B.2 in that recognizing an $a\in{\cO}$ with $\bT_a\vdash \psi$ is at least as hard as recognizing that *ψ* is true. The starting point for constructing such an $a\in{\cO}$ therefore is the truth of *ψ* and as in Turing’s theorem one proceeds to cook up *a* via an application of the primitive recursion theorem, albeit this time a very intricate one.


## Notes（原文脚注，引自主文）

[^note-49]: 49. The usual recursion theorem is formulated for partial recursive functions but there is a version, due to Kleene (1958), that works for primitive recursive functions.

[^note-50]: 50. Accessible accounts can be found in Torkel Franzén’s book (2004a) and his paper (2004b).

### Notes to Appendix C