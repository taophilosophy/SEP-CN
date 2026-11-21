# proof-theory — appendix-e（supplement）

> （《proof-theory》词条补充材料，源：plato.stanford.edu/entries/proof-theory/appendix-e.html）

#### Supplement to Proof Theory

## E. Combinatorial Independence Results

Results that have been achieved through ordinal analysis mainly fall into four groups: (1) Consistency of subsystems of classical second order arithmetic and set theory relative to constructive theories, (2) reductions of theories formulated as conservation theorems, (3) combinatorial independence results, and (4) classifications of provable functions and ordinals. In this appendix we shall just provide a few examples of (3).[^note-56] (4) is to be discussed in [Appendix F](proof-theory.appendix-f.md).

Gödel’s Incompleteness Theorems raised the question of whether there is a strictly mathematical example of an incompleteness in first-order Peano arithmetic and stronger systems, one which is mathematically simple and interesting and does not require the numerical coding of metamathematical notions. The first such examples were found by Gentzen and Goodman. Recall from section 3 the ordinal representation for $\varepsilon_0$ based on Cantor’s normal form with its ordering $\prec$. Let PRWO$(\varepsilon_0)$ be the statement that there are no infinite primitive recursive $\prec$-descending sequences.

Theorem E.1 (Gentzen 1938b)

1. The theory of primitive recursive arithmetic, **PRA**, proves that PRWO$(\varepsilon_0)$ implies the consistency of **PA**.
2. Assuming that **PA** is consistent, **PA** does not prove PRWO$(\varepsilon_0)$.

This theorem is not explicitly stated in his 1938b but it is an immediate consequence of his consistency proof of **PA**.[^note-57] Goodstein, upon studying Gentzen’s 1936, established a connection between descending sequences of ordinals below $\varepsilon_0$ and certain sequences of natural numbers. He realized that given two ordinals $\alpha,\beta<\varepsilon_0$ one could replace the base *ω* in their complete Cantor normal forms by a sufficiently large number *b* and the resulting natural numbers $\hat\rT^{\omega}_{b}(\alpha)$ and $\hat{\rT}^{\omega}_{b}(\beta)$ would stand in the same ordering as *α* and *β*. This is a consequence of the fact that the criteria for comparing ordinals in Cantor normal form are the same as for natural numbers in complete base *b*-representation. There is a Cantor normal form for positive integers *m* to any base *b* with $b\geq 2$, namely we can express *m* uniquely in the form

$$\tag{e1} m= b^{n_1}\cdot k_1+\ldots +b^{n_r}\cdot k_r $$

where $m>n_1>\ldots>n_r\geq 0$ and $0<k_1,\ldots, k_r<b$. As each $n_i>0$ is itself of this form we can repeat this procedure, arriving at what is called the *complete b-representation* of *m*. In this way we get a unique representation of *m* over the alphabet $0,1,\ldots,b,+,\cdot$.

For example

$$ \begin{align} 7\,625\,597\,485\,157 &= 3^{27}\cdot 1+ 3^4\cdot 2 + 3^1\cdot 2+3^0\cdot 2 \\ & = 3^{3^3}+ 3^{3+1}\cdot 2 + 3^1\cdot 2+2. \end{align} $$

In 1944 Goodstein defined what came to be called *Goodstein sequences*.

Definition E.2 For naturals $m>0$ and $c\geq b\geq 2$ let $\rS^{b}_{c}(m)$ be the integer resulting from *m* by replacing the base *b* in the complete *b*-representation of *m* everywhere by *c*. For example ${\rS^{3}_{4}(34)}=265$, since $34=3^3+3\cdot 2+1$ and $4^4+4\cdot 2+1=265$.

Given any natural number *m* and non-decreasing function

$$f:\bbN\to \bbN$$

with $f(0)\geq 2$ define

$$ m^{f}_{0} = m,\ldots, m^{f}_{i+1} = \rS^{f(i)}_{f(i+1)} (m^{f}_{i}) \monus 1 $$

where $k \monus 1$ is the predecessor of *k* if $k>0$, and $k \monus 1=0$ if $k=0$.

We shall call $(m_i^f)_{i\in \bbN}$ a *Goodstein sequence*. Note that a sequence $(m_i^f)_{i\in \bbN}$ is uniquely determined by *f* once we fix its starting point $m=m_0^f$.

The case when *f* is just a shift function has received special attention. Given any *m* we define $m_0=m$ and $m_{i+1}:=\rS^{i+2}_{i+3} (m_i) \monus 1$ and call $(m_i)_{i\in \bbN}$ a *special Goodstein sequence*. Thus $(m_i)_{i\in \bbN}= (m^{\textrm{id}_2}_i)_{i\in \bbN}$, where $\textrm{id}_2(x)=x+2$. Special Goodstein sequences can differ only with respect to their starting points. They give rise to a recursive function $f_{\textrm{good}}$ defined as follows: $f_{\textrm{good}}(m)$ is the least *i* such that $m_i=0$ where $(m_i)_{i\in{\bbN}}$ is the special Goodstein sequence starting with $m_0=m$.

Goodstein proved that all Goodstein sequences are finite. From his work combined with that of Gentzen 1938b he could have concluded the following result (see Rathjen 2015: Theorem 2.9).

Theorem E.3 Termination of primitive recursive Goodstein sequences is not provable in **PA**.

Already the termination of special Goodstein sequences, i.e., those where the base change is governed by the shift function, is not provable in **PA**. This result was obtained only much later by Kirby and Paris (1982) using model-theoretic tools. The latter prompted Cichon (1983) to find a different (short) proof that harked back to older proof-theoretic work of Kreisel (1952) which identified the so-called $<\varepsilon_0$-recursive functions as the provably recursive functions of **PA**; see [Appendix F](proof-theory.appendix-f.md), Definition F.1. Other results pivotal to Cichon (1983) were ordinal-recursion-theoretic classifications of Schwichtenberg (1971) and Wainer (1970) which showed that the latter class of recursive functions consists exactly of those elementary in one of the fast growing functions $F_{\alpha}$ with $\alpha<\varepsilon_0$. As $F_{\varepsilon_0}$ eventually dominates any of these functions it is not provably total in **PA**. Cichon verified that $F_{\varepsilon_0}$ is elementary in the function $f_{\textrm{good}}$ of Definition E.2. Thus termination of special Goodstein sequences is not provable in **PA**.[^note-58]

Mathematical independence results enjoyed great popularity in the 1970s and 1980s. Perhaps the most elegant of these is a strengthening of the Finite Ramsey Theorem due to Paris and Harrington (1977). The original proofs of the independence of combinatorial statements from **PA** all used techniques from non-standard models of arithmetic. Only later on alternative proofs using proof-theoretic techniques were found. However, results from ordinal-theoretic proof theory turned out to be pivotal in providing independence results for theories stronger than **PA**, and even led to a new combinatorial statement. The stronger theories referred to are Friedman’s system $\ATR_0$ of *arithmetical transfinite recursion* and the system $(\Pi^1_1\mbox{-}\bCA)_0$ based on $\Pi^1_1$-comprehension. The independent combinatorial statements have their origin in certain embeddability questions in the theory of finite graphs. The first is a famous theorem of Kruskal asserting that every set of finite trees has only finitely many minimal elements.

Definition E.4 A *finite tree* is a finite partially ordered set $\bbB=(B,\leq)$ such that:

1. *B* has a smallest element (called the *root* of $\bbB$);
2. for each $s\in B$ the set $\{t\in B : t\leq s\}$ is a totally ordered subset of *B*.

Definition E.5 For finite trees $\bbB_1$ and $\bbB_2$, an *embedding* of $\bbB_1$ into $\bbB_2$ is a one-to-one mapping $f: \bbB_1 \rightarrow \bbB_2$ such that $f(a\land b)=f(a) \land f(b)$ for all $a,b\in \bbB_1$, where $a\land b$ denotes the infimum of *a* and *b*.

We write $\bbB_1\leq \bbB_2$ to mean that there exists an embedding $f: \bbB_1 \rightarrow \bbB_2$.

Theorem E.6 *(Kruskal’s theorem)* For every infinite sequence of trees $\left(\bbB_k : k<\omega\right)$, there exist indices *i* and *j* such that $i<j<\omega$ and $\bbB_i\leq \bbB_j$. (In particular, there is no infinite set of pairwise nonembeddable trees.)

Theorem E.7 Kruskal’s Theorem is not provable in $\ATR_0$ (cf. Simpson 1985).

The proof of the above independence result exploits a connection between finite trees and ordinal representations for ordinals $<\Gamma_0$ and the fact that $\Gamma_0$ is the proof-theoretic ordinal of $\ATR_0$. Each ordinal representation $\fraka$ is assigned a finite tree $\bbB_{\fraka}$ to the effect that for two representations ${\fraka}$ and $\frakb$, $\bbB_{\fraka}\leq \bbB_\frakb$ implies ${\fraka}\leq \frakb$. Hence Kruskal’s theorem implies the well-foundedness of $\Gamma_0$ and is therefore not provable in $\ATR_0$. The connection between finite trees and ordinal representations for ordinals $<\Gamma_0$ was noticed by Friedman (cf. Simpson 1985) and independently by Diana Schmidt (1979).

A hope in connection with ordinal analyses is that they may lead to discoveries of new combinatorial principles which encapsulate considerable proof-theoretic strength. Examples are still scarce. One case where ordinal notations led to a new combinatorial result was Friedman’s extension of Kruskal’s Theorem, EKT, which asserts that finite trees are well-quasi-ordered under gap embeddability (see Simpson 1985). The gap condition imposed on the embeddings is directly related to an ordinal notation system that was used for the analysis of $\Pi^1_1$ comprehension. The principle EKT played a role in the proof of the graph minor theorem of Robertson and Seymour.

Definition E.8 For $n<\omega$, let $\cB_n$ be the set of all finite trees with labels from *n*, i.e., $(\bbB,\ell)\in {\mathcal B}_n$ if $\bbB$ is a finite tree and $\ell:B\rightarrow\{0,\ldots,n-1\}$. The set $\cB_n$ is quasiordered by putting $(\bbB_1,\ell_1)\leq (\bbB_2,\ell_2)$ if there exists an embedding $f: \bbB_1 \rightarrow \bbB_2$ with the following properties:

1. for each $b\in B_1$ we have $\ell_1(b)=\ell_2(f(b))$;
2. if *b* is an immediate successor of $a\in\bbB_1$, then for each $c\in \bbB_2$ in the interval $f(a)<c<f(b)$ we have $\ell_2(c)\geq\ell_2(f(b))$.

The condition (ii) above is called a *gap condition*.

Theorem E.9 For each $n<\omega$, $\cB_n$ is a well quasi ordering (abbreviated $\WQO(\cB_n)$), i.e., there is no infinite set of pairwise nonembeddable trees.

Theorem E.10 $\forall n<\omega\;\WQO(\cB_n)$ is not provable in $(\Pi^1_1-\bCA)_0$.

The proof of Theorem E.10 employs the ordinal representation system of section 5.3.1. for the proof-theoretic ordinal of $(\Pi^1_1-{\bCA})_0$ which is $\psi_{\lower{.8ex}{\Omega_1}} (\Omega_{\omega})$. The connection between $<\omega$ labeled trees and this ordinal is that $\forall n<\omega\;\WQO(\cB_n)$ implies the well-foundedness of $\psi_{\lower{.8ex}{\Omega_1}}(\Omega_{\omega})$ (on the basis of $\ACA_0$ say). The connection is even closer in that the gap condition imposed on the embeddings between trees is actually gleaned from the ordering of the ordinal representations. If one views these terms as labeled trees, then the gap condition is exactly what one needs to ensure that an embedding of two such trees implies that the ordinal corresponding to the first tree is less than the ordinal corresponding to the second tree. It is also for that reason that criticism had been leveled against the principle EKT for being too contrived or too metamathematical. But this was superseded by the role that EKT played in the proof of the graph minor theorem (see Friedman, Robertson, & Seymour 1987).

As to the importance attributed to the graph minor theorem, let us quote from a book on Graph Theory:

> Our goal […] is a single theorem, one which dwarfs any other result in graph theory and may doubtless be counted among the deepest theorems that mathematics has to offer: *in every infinite set of graphs there are two such that one is a minor of the other*. This *minor theorem*, inconspicuous though it may look at first glance, has made a fundamental impact both outside graph theory and within. Its proof, due to Neil Robertson and Paul Seymour, takes well over 500 pages. (Diestel 1997: 249)

Definition E.11 Let $e=xy$ be an edge of a graph $G=(V,E)$, where *V* and *E* denote its vertex and edge set, respectively. By $G/e$ we denote the graph obtained from *G* by *contracting* the edge *e* into a new vertex $v_e$, which becomes adjacent to all the former neighbors of *x* and of *y*. Formally, $G/e$ is a graph $(V',E')$ with vertex set $V':=(V\setminus\{x,y\})\,\cup\,\{v_e\}$ (where $v_e$ is the “new” vertex, i.e., $v\notin V\,\cup\,E$) and edge set

$$ \begin{align} E' & := \left\{vw\in E \mid \{v,w\} \cap \{x,y\}=\emptyset\right\} \\ &\qquad \cup \left\{v_ew \mid xw\in E\setminus\{e\} \lor yw\in E\setminus\{e\}\right\}. \end{align} $$

If *X* is obtained from *Y* by first deleting some vertices and edges, and then contracting some further edges, *X* is said to be a *minor* of *Y*. In point of fact, the order in which deletions and contractions are applied is immaterial as any graph obtained from another by repeated deletions and contractions in any order is its minor.

Theorem E.12 (Robertson and Seymour 2004) If $G_0$, $G_1$, $G_2$,… is an infinite sequence of finite graphs, then there exist $i<j$ so that $G_i$ is isomorphic to a minor of $G_j$.

As a corollary to the graph minor theorem one obtains positive answers to two famous conjectures.

Corollary E.13

1. (Vázsonyi’s conjecture) If all the $G_k$ are trivalent, then there exist $i<j$ so that $G_i$ is embeddable into $G_j$.
2. (Wagner’s conjecture) For any 2-manifold *M* there are only finitely many graphs which are not embeddable in *M* and are minimal with this property.

Theorem E.14 (Friedman, Robertson, and Seymour 1987)

1. GMT implies EKT within, say, $\RCA_0$.
2. GMT is not provable in $(\Pi^1_1-\bCA)_0$.

A further independence result that ensues from ordinal analysis is due to Buchholz (1987). It concerns an extension of the hydra game of Kirby and Paris. It is shown in that paper that the assertion that Hercules has a winning strategy in this game is not provable in the theory $(\Pi^1_1-\bCA)+\BI$.

It would be very desirable to also find mathematically fruitful combinatorial principles hidden in stronger representation systems such as the ones based on Mahlo cardinals and weakly compact cardinals used for analyzing Kripke-Platek set theory with a recursively Mahlo universe and with $\Pi_3$-reflection, respectively.


## Notes（原文脚注，引自主文）

[^note-56]: 56. For more details see Rathjen 1999a.

[^note-57]: 57. For more details see Rathjen 2015. As for the unprovability of $\Con(\PA)$ in **PA**, Gentzen (1943) explicitly states that his proof makes no appeal to the second incompleteness theorem.

[^note-58]: 58. In Rathjen 2015 the question is pondered whether the latter result could have been proved much earlier (from a technical as well as sociological point of view).

### Notes to Appendix F