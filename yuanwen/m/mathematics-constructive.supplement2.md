# mathematics-constructive — supplement2（supplement）

> （《mathematics-constructive》词条补充材料，源：plato.stanford.edu/entries/mathematics-constructive/supplement2.html）

#### Supplement to Constructive Mathematics

## Approaches to Constructive Topology

One of the basic results of classical point set topology is the Heine-Borel theorem (HBT): if a set of open intervals covers the closed unit interval [0,1], then already finitely many of them cover the interval; in other words, [0,1] is *open-cover compact*. Within INT the theorem is still valid by an appeal to the full fan theorem (Dummett [2000]). Moerdijk [1984] has shown that HBT is strictly weaker than the full fan theorem, but we do not know of any natural fan theorem to which the Heine-Borel theorem is equivalent relative to BISH. HBT is one example of how fan theorems facilitate the development of topology within INT; see also Troelstra [1978] and Waaldijk [1996]. However the effectivity of HBT can be called into question, as within RUSS the existence of *ε*-singular covers (see Section 3.2 above) provides a strong recursive counterexample to the theorem.

In his practice of analysis, Bishop [1967] took a radical approach by limiting his attention to metric spaces, in which compactness can be defined as completeness plus total boundedness. Moreover, he took the continuity of a function from a compact metric space into a metric space to mean uniform continuity, by definition. This allowed him to regain most of the useful theorems about, for example, suprema and positive measures, without referring to HBT. It is possible to generalise his theory to uniform spaces, but for some applications this is clearly not sufficient: for instance, quotient spaces of uniform spaces need not be uniform spaces, a fact that bars direct applicability to fields such as algebraic topology.

However, almost in passing, Bishop [1967] mentions two possible approaches to the constructive development of topology: neighbourhood spaces and function spaces. Little appears to have been done in the former topic, but Petrakis [2016, 2016a] has made considerable progress in the latter. The two are linked in an interesting article of Ishihara [2013].

The neighborhood structure on a topological space tells us only when points are close, but in general gives little information about the more global structure of the space. In order to go significantly beyond metric and uniform spaces, we need to consider topological spaces endowed with some not-necessarily-uniform structure over and above the neighbourhood one. One such endowment is the function space structure mentioned in the preceding paragraph. We now describe two alternative approaches: apartness spaces, where the fundamental axioms capture the idea of subspaces being apart from one another; and point-free topology, where the notion of open sets and their mutual cover relations are taken as basics.

### Apartness spaces

A classical theory of proximity spaces, based on the primitive notion of two sets being near each other, has been around for over 100 years and has been developed substantially over the last 60 or so; see Riesz [1908], Naimpally & Warrack [1970], and Naimpally [2009]. It soon becomes clear, however, that the notion—a negative one, logically speaking—of nearness does not have much computational strength, and that, in some constructive form, its classical obverse—apartness—is what one needs for a constructively fruitful theory. We sketch such a theory based on a few axioms specifying the fundamental properties of the notion of apartness (a) between a point and a set, and (b) between two sets.

Let $X$ be an inhabited set equipped with an inequality relation $\ne$ : that is, a binary relation on $X$ that satisfies these two properties for all $x, y \in X$ :

$$\begin{align*} x \ne y &\Rightarrow \neg(x=y), \\ x \ne y &\Rightarrow y \ne x. \end{align*}$$

Note that, in general, this inequality relation will be distinct from the special case of the denial inequality, in which the first implication in the preceding display is replaced by a bi-implication. This distinction gives rise to two types of complement for subsets $S$ of $X$:

- the *logical complement*, $\neg S \equiv \{x \in X : \neg(x \in S)\}$;
- the *complement*, ${\sim}S \equiv \{x \in X : \forall s \in S (x \ne s)\}$.

We also equip $X$ with a binary relation $\bowtie$ between points and subsets of $X$. This brings into play a third type of complement:

- the *apartness complement*, ${-}S \equiv \{x \in X : x \bowtie S\}$.

It will follow from the axioms for $\bowtie$ that ${-}S \subset{\sim}S \subset \neg S$.

If $\bowtie$ satisfies the following axioms (in which, for simplicity, we omit the quantifiers), then it is called a (*point-set*) *pre-apartness* on $X$, and $X$, taken with $\bowtie$, becomes a (*point-set*) *pre-apartness space*:

**A1**

$x \bowtie \varnothing $

**A2**

${-}A \subset{\sim}A $

**A3**

$ x \bowtie(A \cup B) \Leftrightarrow(x \bowtie A \wedge x \bowtie B) $

**A4**

${-}A \subset{\sim}B \Rightarrow -A \subset -B $

If, in addition to A1–A4, the pre-apartness satisfies

**A5**

$x \bowtie A \Rightarrow \forall y \in X (x \ne y \vee y \bowtie A),$

then we call it an *apartness*, and the space X a (point-set) apartness space. The value of the additional axiom A5 is that it provides us with alternatives that hold automatically in CLASS and that facilitate many constructive proofs. Nevertheless, it makes good sense to work without A5 where it is not needed.

The canonical example of an apartness space is an inhabited metric space $(X,\varrho)$, taken with the metric inequality defined by

$$ x \ne y \Leftrightarrow \varrho(x, y) \gt 0 $$

and with

$$ x \bowtie S \Leftrightarrow \exists r \gt 0\,\forall s \in S\, (\varrho(x, s) \ge r). $$

The real line $\mathbf{R}$ with its standard metric is such an apartness space. However, if we take the real line with the denial inequality, rather than metric one, then axiom A5 holds if and only if we adopt Markov’s principle; so in the absence of the latter, the resulting space is only a pre-apartness one.

For the rest of this section only, we adopt the convention that a topological space $X$ comes with an inequality relation $\ne$. The topology *τ* then induces a topological pre-apartness $\bowtie_{\tau}$ on $X$, defined by

$$ x \bowtie_{\tau} S \Leftrightarrow x \in({\sim}S)^{\circ}, $$

where, as usual, $^{\circ}$ denotes interior. If $X$ has the *topological A5 property*,

$$ \forall x \in X\, \forall U \in \tau\, (x \in U \Rightarrow \forall y \in X\, (x \ne y \vee y \in U)), $$

then the corresponding pre-apartness is an apartness. Note that on a metric apartness space the apartness corresponding to the metric topology coincides with the metric apartness.

Every pre-apartness $\bowtie$ on an inhabited set induces a natural apartness topology $\tau_{\bowtie}$, in which the *nearly open sets* are the unions of families of apartness complements. In turn, $\tau_{\bowtie}$ induces on $X$ a pre-apartness, which turns out to be the original one. If the pre-apartness $\bowtie$ is induced by a topology *τ* on $X$, then every nearly open subset of $X$ is *τ*-open. When the converse holds, so that the apartness topology and the original one coincide, we say that the topological space $X$ is *topologically consistent*. Topological consistency always holds classically, but need not hold constructively. One condition on $X$ that ensures its topological consistency is that of *topological local decomposability*:

$$ \forall x \in X\, \forall U \in \tau\, (x \in U \Rightarrow \exists V \in \tau\, (x \in V \wedge X = U \cup{\sim}V). $$

If we start with a pre-apartness $\bowtie$ on a set $X$, then we can define a counterpart of this last condition—*local decomposability*:

$$ \forall x \in X\, \forall S \subset X\, (x \in {-}S \Rightarrow \exists T \subset X\, (x \in {-}T \wedge X = {-}S \cup T)). $$

It turns out that a topological space $(X, \tau)$ is topologically locally decomposable if and only if it is topologically consistent and $(X, \bowtie_{\tau})$ is locally decomposable.

One obvious way to introduce continuity of a mapping $f : (X, \bowtie_X) \rightarrow(Y, \bowtie_Y)$ between pre-apartness spaces is to work with the corresponding apartness topologies. Thus we say that $f$ is *topologically continuous* if for each nearly open subset $V$ of $Y, f^{-1}(V)$ is nearly open in $X$. But there is a notion of continuity that is more in the morphic spirit of category theory: we say that $f$ is *apartness continuous* if for all $x \in X$ and $S \subset X$,

$$ f(x) \bowtie_Y f(S) \Rightarrow x \bowtie_X S. $$

If $X$ and $Y$ are metric spaces, then the apartness continuity of $f$ is equivalent to continuity in the usual *ε*-*δ* sense.

The really hard work, with significant rewards, in the theory of apartness comes when we lift our attention to pre-apartness between subsets of an inhabited set $X$. For this, we require the (set-set) pre-apartness $\bowtie$ to satisfy the following axioms:

**B1**

$X \bowtie \varnothing $

**B2**

${-}A \subset{\sim}A $

**B3**

$(A_1 \cup A_2) \bowtie (B_1 \cup B_2) \Leftrightarrow \forall i, j \in \{1, 2\} (A_i \bowtie B_j) $

**B4**

${-}A \subset{\sim}B \Rightarrow {-}A \subset {-}B.$

The rather complicated form of axiom B3 enables us to work without assuming the symmetry of $\bowtie$.

As the reader will have surmised, in axioms B2 and B4, ${-}A$ is the apartness complement of $A$ relative to the point-set relation defined by

$$ x \bowtie A \Leftrightarrow \{x\} \bowtie A, $$

which is a point-set pre-apartness said to be *associated with*, or *induced by*, the set-set relation $\bowtie.$

If axioms B1–B4 hold, then the pair $(X, \bowtie)$, or when no confusion is likely, the set $X$ itself, a (*set-set*) *pre-apartness space*; and if $A \bowtie B$, we say that $A$ is *apart from B*. By a (*set-set*) *apartness* on $X$ we mean a relation $\bowtie$ between subsets of $X$ that satisfies axioms B1–B3 and

**B5**

$x \in A \Rightarrow \exists S \subset X (x \in {-}S \wedge X = {-}A \cup S)$.

The relation $\bowtie$ then also satisfies B4 and so is a pre-apartness. Regarded as a point-set pre-apartness space, $X$ is then locally decomposable (this is precisely what B5 says) and hence satisfies A5. In this case we call $(X, \bowtie)$, or simply $X$ itself, a (*set-set*) *apartness space*.

The canonical example of a set-set apartness is again a metric space $(X, \varrho)$, in which we define the *metric apartness* by

$$ A \bowtie B \Leftrightarrow \exists r \gt 0\, \forall x \in A\, \forall y \in B\, (\varrho(x, y) \gt r). $$

A more general example is a uniform space, whose definition we pass over here.

The natural morphisms in the category of set-set pre-apartness spaces are the functions $f : (X, \bowtie_X) \rightarrow (Y, \bowtie_Y)$ that are *strongly continuous*,in the sense that for all $A, B \subset X$,

$$ f(A) \bowtie_Y f(B) \Rightarrow A \bowtie_X B. $$

Every uniformly continuous mapping between metric spaces is strongly continuous. Among other results connecting types of continuity for a mapping $f : X \rightarrow Y$ between metric spaces we have these:

- $f$ is uniformly continuous if and only if the mapping $f \times f : (x, x') \rightsquigarrow (f(x), f(x'))$ is strongly continuous on the product metric space $X \times X$.
- If $f$ is strongly continuous, then it is uniformly sequentially continuous.
- If $f$ is strongly continuous and $f(X)$ is totally bounded, then $f$ is uniformly continuous.
- If $X$ is totally bounded and $f$ is strongly continuous, then $f$ is uniformly continuous.

The proofs of the second and fourth of these results are particularly involved, and introduce a proof technique that has other applications, for example in the theory of convergence of sequences of functions between apartness spaces. Note that we cannot pass, in general, from uniform sequential continuity to uniform continuity without using $\BDN$.

We refer the reader to Chapter 3 of Bridges & Vîță [2011] for more information, including an extensive bibliography, about set-set apartness relations.

### Point-free topology

In point-free topology the ideal objects (points) $X$ are taken as basic and we group them together in ever narrower so-called *open sets*. The set $O(X)$ of open sets defines the topology, and is required to be closed under arbitrary unions and finite intersections. The open sets are often described in terms of basic open sets, so that every open set may be written as a union of such sets. These basic open sets can be thought of as approximations to the points. To give a specific example, the topology of the real line $\bR$ may be described in terms of the basic open sets

$$ (p, q) = \{x \in \bR : p \lt x \lt q \} $$

where $p$ and $q$ are rational numbers. Each such basic open, an interval with rational endpoints, is specified by finite information and approximates all the real numbers $x$ in the interval.

We may try to reverse the order of concepts, and take the basic opens, or approximations, as fundamental, and derive the ideal objects or points from the opens and their mutual relations. This is what is done in point-free topology, a field which has a long history going back to Wallman [1938], Menger [1940] and in its current form, Ehresmann & Isbell; see Picardo & Pultr [2011]. There is also a precursor in point-free geometry (Whitehead [1919]). We shall here concentrate on *formal topology* (Sambin [1987]), which is a version of *locale theory* (Johnstone [1982], Joyal & Tierney [1984], Picardo & Pultr [2011]), where special consideration has been given to issues of constructivity and predicativity. Some seminal examples in formal topology were developed earlier in Martin-Löf [1970].

A *formal topology* is a triple $\langle A, \le, \cov \rangle$ consisting of a set $A$ of basic opens, a transitive and reflexive relation $\le$ on $A$, and a relation cov between elements of $A$ and subsets of $A$. The relation $a \le b$ is understood as (formal) inclusion, whereas $a$ cov $U$ is read $a$ is covered by $U$. These are supposed to satisfy the following natural axioms.

- $\mathbf{ER}$ (extension and reflexity): $a \cov U$, whenever $a \le b$ for some $b \in U$
- $\mathbf{T}$ (transitivity): $a \cov V$, whenever $a \cov U$, and for each $b \in U$, $b \cov V$
- $\mathbf{L}$ (localization): If $b \cov U$ and $a \le b$, then $a \cov a \downarrow U$, where $$ a \downarrow U \equiv \{x \in A : x \le a \wedge \exists y \in U (x \le y\}). $$

A *point* in this topology is an inhabited subset *α* of basic opens which satisfies these conditions:

- $\mathbf{F}$ (filtering): If $a, b \in \alpha$, then there exists $c \in \alpha$ with $c \le a$ and $c \le b$.
- $\mathbf{S}$ (splitting): If $a \in \alpha$ and $a \cov U$, then for some $b \in U, b \in \alpha$.

We think of a point as a set of approximations. The filtering property insures that any two approximations have a common refinement, whereas the splitting property allows an approximation to be refined in any way the cover relation allows.

For any set $U \subseteq A$, we let $U^*$ be the set of all points *α* where $a \in U$ for some $a \in \alpha$. It can be shown that the points together with the sets $U^*$ form a point-set topology in the usual sense, and that formal cover implies point-wise cover:

$$ a \cov U \Rightarrow \{a\}^* \subseteq U^*. $$

The converse implication usually fails.

For any $S \subseteq A$, we may define an associated closed subspace of $\bA \equiv\langle A, \le, \cov\rangle$ by redefining the cover relation:

$$ a \covs U \equiv a \cov S \cup U. $$

Note that if $a \cov S$, then $a \covs \varnothing$, so, in effect, the open set determined by $S$, gets identified with the empty set, as far as mutual covering goes. The topology

$$ \mathbf{A}\text{-}S \equiv \langle A, \le, \covs\rangle $$

represents the subspace corresponding to the points not in $S$.

To illustrate the methods of formal topology, we give a proof of the point-free *Heine-Borel theorem*:

**HBT**

*Every cover of the unit interval by open sets has a finitely enumerable subcover.*

Note the use of “finitely enumerable” here. A set $S$ is called *finitely enumerable* if there exist a positive integer $N$ and a mapping $f$ of $\{1, \ldots ,N\}$ onto $S$. If the mapping $f$ is one-one, then we say that $S$ is *finite*. If the pairset $\{0, x\}$ is finite, then we can decide whether $x$ equals 0 or not. Thus (see Section 1 above), the statement “every finitely enumerable subset of $\bR$ is finite” implies LPO.

To prove HBT, we need to construct the point-free reals. Accordingly, let $\bR \equiv\langle I, \le_I, \cov\rangle$ be the formal topology given by the following data: $I$ is the set of pairs $(p, q)$ where

- $p \lt q$ are rational numbers, and
- such pairs are ordered by setting $(p', q') \le_I (p, q)$ if and only if $p \le p'$ and $q' \le q$.

A pair in $I$ is regarded as specifying an interval with rational end points. The cover relation $\cov$ is the smallest cover relation that satisfies the following axioms:

**R1**

for $p \lt p' \lt q' \lt q, (p, q) \cov \{(p, q'),(p', q)\}$

**R2**

for $p \lt q, (p, q) \cov \{(p', q') : p \lt p' \lt q' \lt q\}$

These axioms describe two principal ways of covering an interval by shorter intervals. The points of $\bR$ are the *real numbers*. We define the order of the points by taking $\alpha \lt \beta$ if and only if there exist $(p, q) \in \alpha$ and $(p', q') \in \beta$ with $q \lt p'$; we then take $\beta \le \alpha$ to mean that $\alpha \lt \beta$ is false. It is possible to show using transfinite induction on covers (cf. Coquand *et al.* 2003) that we have the following alternative characterisation of the above cover relation:

$(p, q)$ cov $U$ holds if and only if for any $r \lt s$ with $p \lt r \lt s \lt q$, there exist $t_1 \lt t_2 \lt \ldots \lt t_n, n \ge 3$, with $r = t_1, s = t_n$, such that each $(t_i, t_{i+2}) (1\le i \le n - 2)$ is included in some interval of $U$ (Cederquist & Negri [1996]).

Let

$$ S \equiv \{(p, q) \in I : q \lt 0\} \cup \{(p, q) \in I : 1 \lt p\}. $$

It can be shown that the points of $\mathbf{R}\text{-}S$ are the real numbers in the interval [0, 1].

We now have the ingredients to prove HBT. To say that $U$ covers the unit interval $\mathbf{R}\text{-}S$ means that $(p, q) \covs U$ for all $(p, q)$. In particular $(-2, 3) \covs U$; that is, $(-2, 3) \cov S \cup U$. Hence for $r = -1 \lt s = 2$ there are $t_1 \lt t_2 \lt \ldots \lt t_n$ with $r = t_1$ and $s = t_n$, such that each $(t_i, t_{i+2}) (1 \le i \le n-2)$ is included in some interval of $S \cup U$. Thus for $i = 1, \ldots ,n - 2$, there exists $(p_i, q_i) \in S \cup U$ with $(t_i, t_{i+2}) \le(p_i, q_i)$. It follows that there is a finitely enumerable $F \subset U$ such that $(-1, 2) \covs F$. But $(p, q) \covs (-1, 2)$ for all $(p, q) \in I$, so by transitivity, $(p, q) \covs F$. Hence $F$ is a finitely enumerable subcover of the unit interval. This establishes the theorem.

Another surprising result about compactness is that Tychonoff’s theorem holds for formal topologies (Coquand [1992]). In classical point-set topology this theorem is equivalent to the Axiom of Choice (Johnstone [1982]). Moreover, the classically highly non-constructive Stone-Čech compactification has as well a constructive point-free version (Curi [2010]).

The category of (set-presented) formal topologies has good properties from a topological point of view: it has (finite) limits and (finite) colimits. In particular, it is possible to construct quotient spaces and to attach subspaces, so the category seems adequate for doing algebraic topology; see Palmgren [2009].

Many results in functional analysis have natural point-free proofs (Johnstone [1982], Picardo & Pultr [2011]); some of them—for instance, the Riesz representation theorem (Coquand & Spitters [2009])—can also be proved completely constructively. There are, in addition, methods for dealing with the Zariski topology and spectra of rings in a point-free way (Johnstone [1982]); here, too, it is possible to make constructive developments (Schuster [2006], Coquand [2009]).
