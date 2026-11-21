# Quantum Logic and Probability Theory
**First published Mon Feb 4, 2002; substantive revision Tue Aug 10, 2021**

*Wilce, Alexander*

Mathematically, quantum mechanics can be regarded as a non-classical probability calculus resting upon a non-classical propositional logic. More specifically, in quantum mechanics each probability-bearing proposition of the form “the value of physical quantity $A$ lies in the range $B$” is represented by a projection operator on a Hilbert space $\mathbf{H}$. These form a non-Boolean—in particular, non-distributive—orthocomplemented lattice. Quantum-mechanical states correspond exactly to probability measures (suitably defined) on this lattice.

What are we to make of this? Some have argued that the empirical success of quantum mechanics calls for a revolution in logic itself. This view is associated with the demand for a realistic interpretation of quantum mechanics, i.e., one not grounded in any primitive notion of measurement. Against this, there is a long tradition of interpreting quantum mechanics operationally, that is, as being precisely a theory of measurement. On this latter view, it is not surprising that a “logic” of measurement-outcomes, in a setting where not all measurements are compatible, should prove not to be Boolean. Rather, the mystery is why it should have the *particular* non-Boolean structure that it does in quantum mechanics. A substantial literature has grown up around the programme of giving some independent motivation for this structure—ideally, by deriving it from more primitive and plausible axioms governing a generalized probability theory.

## 1. Quantum Mechanics as a Probability Calculus

It is uncontroversial (though remarkable) that the formal apparatus of quantum mechanics reduces neatly to a generalization of classical probability in which the role played by a Boolean algebra of events in the latter is taken over by the “quantum logic” of projection operators on a Hilbert space.[^note-1] Moreover, the usual statistical interpretation of quantum mechanics asks us to take this generalized quantum probability theory quite literally—that is, not as merely a formal analogue of its classical counterpart, but as a genuine doctrine of chances. In this section, I survey this quantum probability theory and its supporting quantum logic.[^note-2]

[For further background on Hilbert spaces, see the entry on quantum mechanics. For further background on ordered sets and lattices, see the supplementary document: [The Basic Theory of Ordering Relations](qt-quantlog.supplement.md). Concepts and results explained these supplements will be used freely in what follows.]

### 1.1 Quantum Probability in a Nutshell

The quantum-probabilistic formalism, as developed by von Neumann [1932], assumes that each physical system is associated with a (separable) Hilbert space $\mathbf{H}$, the unit vectors of which correspond to possible physical *states* of the system. Each “observable” real-valued random quantity is represented by a self-adjoint operator $A$ on $\mathbf{H}$, the spectrum of which is the set of possible values of $A$. If $u$ is a unit vector in the domain of $A$, representing a state, then the expected value of the observable represented by $A$ in this state is given by the inner product $\langle Au,u\rangle$. The observables represented by two operators $A$ and $B$ are commensurable iff $A$ and $B$ commute, i.e., *AB = BA*. (For further discussion, see the entry on quantum mechanics.)

### 1.2 The “Logic” of Projections

As stressed by von Neumann, the $\{0,1\}$-valued observables may be regarded as encoding propositions about—or, to use his phrasing, properties of—the state of the system. It is not difficult to show that a self-adjoint operator $P$ with spectrum contained in the two-point set $\{0,1\}$ must be a projection; i.e., $P^2 = P$. Such operators are in one-to-one correspondence with the closed subspaces of $\mathbf{H}$. Indeed, if $P$ is a projection, its range is closed, and any closed subspace is the range of a unique projection. If $u$ is any unit vector, then $\langle Pu,u\rangle = \llvert Pu\rrvert ^2$ is the expected value of the corresponding observable in the state represented by $u$. Since this observable is $\{0,1\}$-valued, we can interpret this expected value as the *probability* that a measurement of the observable will produce the “affirmative” answer 1. In particular, the affirmative answer will have probability 1 if and only if *Pu = u*; that is, $u$ lies in the range of $P$. Von Neumann concludes that

> … the relation between the properties of a physical system on the one hand, and the projections on the other, makes possible a sort of logical calculus with these. However, in contrast to the concepts of ordinary logic, this system is extended by the concept of “simultaneous decidability” which is characteristic for quantum mechanics. (1932: 253)

Let’s examine this “logical calculus” of projections. Ordered by set-inclusion, the closed subspaces of $\mathbf{H}$ form a complete lattice, in which the meet (greatest lower bound) of a set of subspaces is their intersection, while their join (least upper bound) is the closed span of their union. Since a typical closed subspace has infinitely many complementary closed subspaces, this lattice is not distributive; however, it is orthocomplemented by the mapping

$$\mathbf{M} \rightarrow \mathbf{M}^{\bot} = \{v\in \mathbf{H} \mid \forall u\in \mathbf{M}(\langle v,u\rangle = 0)\}.$$

In view of the above-mentioned one-one correspondence between closed subspaces and projections, we may impose upon the set $L(\mathbf{H})$ the structure of a complete orthocomplemented lattice, defining $P\le Q$, where $\rran (P) \subseteq \rran (Q)$ and $P' = 1 - P$ (so that $\rran (P') = \rran (P)^{\bot})$. It is straightforward that $P\le Q$ just in case $PQ = QP = P$. More generally, if *PQ = QP*, then $PQ = P\wedge Q$, the meet of $P$ and $Q$ in $L(\mathbf{H})$; also in this case their join is given by $P\vee Q = P+Q - PQ$.

**1.1 Lemma**: Let $P$ and $Q$ be projection operators on the Hilbert space $\mathbf{H}$. The following are equivalent:

1. $PQ = QP$
2. The sublattice of $L(\mathbf{H})$ generated by $P, Q, P'$ and $Q'$ is Boolean
3. $P, Q$ lie in a common Boolean sub-ortholattice of $L(\mathbf{H})$.

Adhering to the idea that commuting observables—in particular, projections—are simultaneously measurable, we conclude that the members of a Boolean sub-ortholattice of $L(\mathbf{H})$ are simultaneously testable. This suggests that we can maintain a classical logical interpretation of the meet, join and orthocomplement as applied to commuting projections.

### 1.3 Probability Measures and Gleason’s Theorem

The foregoing discussion motivates the following. Call projections $P$ and $Q$ *orthogonal*, and write $P\binbot Q$ iff $P \le Q'$. Note that $P\binbot Q$ iff $PQ = QP = 0$. If $P$ and $Q$ are orthogonal projections, then their join is simply their sum; traditionally, this is denoted $P\oplus Q$. We denote the identity mapping on $\mathbf{H}$ by $\mathbf{1}$.

**1.2 Definition**: A (countably additive) *probability measure* on $L(\mathbf{H})$ is a mapping $\mu : L \rightarrow$ [0,1] such that $\mu(\mathbf{1}) = 1$ and, for any sequence of pair-wise orthogonal projections $P_i, i = 1,2$,…

$$\mu(\oplus_i P_i) = \sum_i \mu(P_i)$$

Here is one way in which we can manufacture a probability measure on $L(\mathbf{H})$. Let $u$ be a unit vector of $\mathbf{H}$, and set $\mu_u (P) = \langle Pu,u\rangle$. This gives the usual quantum-mechanical recipe for the probability that $P$ will have value 1 in the state $u$. Note that we can also express $\mu_u$ as $\mu_u(P) = Tr(P P_u)$, where $P_u$ is the one-dimensional projection associated with the unit vector $u$, i.e., $P_u(x) = \langle x, u \rangle u$ for all $x \in \mathbf{H}$.

More generally, if $\mu_i, i=1,2,\ldots$, are probability measures on $L(\mathbf{H})$, then so is any “mixture”, or convex combination $\mu = \sum_i t_i\mu_i$ where $0\le t_i\le 1$ and $\sum_i t_i = 1$. Given any sequence $u_1, u_2,\ldots$, of unit vectors, let $\mu_i = \mu_{u_{ i}}$ and let $P_i = P_{u_{ i}}$. Forming the operator

$$W = t_1 P_1 + t_2P_2 +\ldots,$$

one sees that

$$\mu(P) = t_1 Tr(P P_1) + t_2 Tr(P P_2) + \ldots = Tr(WP)$$

An operator expressible in this way as a convex combination of one-dimensional projections in is called a *density operator*. Density operators are the standard mathematical representation for general (pure or “mixed”) quantum-mechanical states. We have just seen that every density operator $W$ gives rise to a countably additive probability measure on $L(\mathbf{H})$. The following striking converse, due to A. Gleason [1957], shows that the theory of probability measures on $L(\mathbf{H})$ is co-extensive with the theory of (mixed) quantum mechanical states on $\mathbf{H}$:

**1.3 Gleason’s Theorem**: Let $\mathbf{H}$ have dimension $\gt 2$. Then every countably additive probability measure on $L(\mathbf{H})$ has the form $\mu(P) = Tr(WP)$, for a density operator $W$ on $\mathbf{H}$.

An important consequence of Gleason’s Theorem is that $L(\mathbf{H})$ does not admit any probability measures having only the values 0 and 1. To see this, note that for any density operator $W$, the mapping $u \rightarrow \langle Wu,u\rangle$ is continuous on the unit sphere of $\mathbf{H}$. But since the latter is connected, no continuous function on it can take only the two values 0 and 1. This result is often taken to rule out the possibility of “hidden variables”—an issue taken up in more detail in section 6.

### 1.4 The Reconstruction of QM

From the single premise that the “experimental propositions” associated with a physical system are encoded by projections in the way indicated above, one can reconstruct the rest of the formal apparatus of quantum mechanics. The first step, of course, is Gleason’s theorem, which tells us that probability measures on $L(\mathbf{H})$ correspond to density operators. There remains to recover, e.g., the representation of “observables” by self-adjoint operators, and the dynamics (unitary evolution). The former can be recovered with the help of the Spectral theorem and the latter with the aid of a deep theorem of E. Wigner on the projective representation of groups. See also R. Wright [1980]. A detailed outline of this reconstruction (which involves some distinctly non-trivial mathematics) can be found in the book of Varadarajan [1985]. The point to bear in mind is that, once the quantum-logical skeleton $L(\mathbf{H})$ is in place, the remaining statistical and dynamical apparatus of quantum mechanics is essentially fixed. In this sense, then, quantum mechanics—or, at any rate, its mathematical framework—*reduces to* quantum logic and its attendant probability theory.

## 2. Interpretations of Quantum Logic

The reduction of QM to probability theory based on $L(\mathbf{H})$ is mathematically compelling, but what does it tell us about QM—or, assuming QM to be a correct and complete physical theory, about the world? How, in other words, are we to interpret the quantum logic $L(\mathbf{H})$? The answer will turn on how we unpack the phrase, freely used above,

- (\*) The value of the observable $A$ lies in the range $B$.

One possible reading of (\*) is *operational*: “measurement of the observable $A$ would yield (or will yield, or has yielded) a value in the set $B$”. On this view, projections represent statements about the possible results of measurements. This sits badly with realists of a certain stripe, who, shunning reference to “measurement”, prefer to understand (\*) as a *property ascription*:

> the system has a certain categorical property, which corresponds to the observable $A$ having, independently of any measurement, a value in the set $B$.

(One must be careful in how one understands this last phrase, however: construed incautiously, it seems to posit a hidden-variables interpretation of quantum mechanics of just the sort ruled out by Gleason’s Theorem. I will have more to say about this below.)

### 2.1 Realist Quantum Logic

The interpretation of projection operators as representing the properties of a physical system is already explicit in von Neumann’s *Grundlagen*.. However, the logical operations discussed there apply only to commuting projections, which are identified with simultaneously decidable propositions. In 1936 Birkhoff and von Neumann took a step further, proposing to interpret the lattice-theoretic meet and join of projections as their conjunction and disjunction, *whether or not* they commute. Immediately this proposal faces the problem that the lattice $L(\mathbf{H})$ is not distributive, making it impossible to give these “quantum” connectives a truth-functional interpretation. Undaunted, von Neumann and Birkhoff suggested that the empirical success of quantum mechanics as a framework for physics casts into doubt the universal validity of the distributive laws of propositional logic. Their phrasing remains cautious:

> Whereas logicians have usually assumed that properties … of negation were the ones least able to withstand a critical analysis, the study of mechanics points to the distributive identities … as the weakest link in the algebra of logic. (1936: 837)

In the 1960s and early 1970s, this thesis was advanced rather more aggressively by a number of authors, including especially David Finkelstein and Hilary Putnam, who argued that quantum mechanics requires a revolution in our understanding of logic *per se*. According to Putnam, “Logic is as empirical as geometry. … We live in a world with a non-classical logic” ([1968] 1979: 184).

For Putnam, the elements of $L(\mathbf{H})$ represent categorical properties that an object possesses, or does not, independently of whether or not we look. Inasmuch as this picture of physical properties is confirmed by the empirical success of quantum mechanics, we must, on this view, accept that the way in which physical properties actually hang together is not Boolean. Since logic is, for Putnam, very much the study of how physical properties actually hang together, he concludes that classical logic is simply mistaken: the distributive law is not universally valid.

Classically, if $S$ is the set of states of a physical system, then *every* subset of $S$ corresponds to a categorical property of the system, and vice versa. In quantum mechanics, the state space is the (projective) unit sphere $S = S(\mathbf{H})$ of a Hilbert space. However, not all subsets of $S$ correspond to quantum-mechanical properties of the system. The latter correspond only to subsets of the special form $S \cap \mathbf{M}$, for $\mathbf{M}$ a closed linear subspace of $\mathbf{H}$. In particular, only subsets of this form are assigned probabilities. This leaves us with two options. One is to take only these special properties as “real” (or “physical”, or “meaningful”), regarding more general subsets of $S$ as corresponding to no real categorical properties at all. The other is to regard the “quantum” properties as a small subset of the set of all physically (or at any rate, metaphysically) reasonable, but not necessarily *observable*, properties of the system. On this latter view, the set of *all* properties of a physical system is entirely classical in its logical structure, but we decline to assign probabilities to the non-observable properties.[^note-3]

This second position, while certainly not inconsistent with realism *per se*, turns upon a distinction involving a notion of “observation”, “measurement”, “test”, or something of this sort—a notion that realists are often at pains to avoid in connection with fundamental physical theory. Of course, any realist account of a statistical physical theory such as quantum mechanics will ultimately have to render up some explanation of how measurements are supposed to take place. That is, it will have to give an account of which physical interactions between “object” and “probe” systems count as measurements, and of how these interactions cause the probe system to evolve into final “outcome-states” that correspond to—and have the same probabilities as—the outcomes predicted by the theory. This is the notorious *measurement problem*.

In fact, Putnam advanced his version of quantum-logical realism as offering a (radical) dissolution of the measurement problem: According to Putnam, the measurement problem (and indeed every other quantum-mechanical “paradox”) arises through an improper application of the distributive law, and hence *disappears* once this is recognized. This proposal, however, is widely regarded as mistaken.[^note-4]

As mentioned above, realist interpretations of quantum mechanics must be careful in how they construe the phrase “the observable $A$ has a value in the set $B$”. The simplest and most traditional proposal—often dubbed the “eigenstate-eigenvalue link” (Fine [1973])—is that (\*) holds if and only if a measurement of $A$ yields a value in the set $B$ with certainty, i.e., with (quantum-mechanical!) probability 1. While this certainly gives a realist interpretation of (\*),[^note-5] it does not provide a solution to the measurement problem. Indeed, we can use it to give a sharp formulation of that problem: even though $A$ is certain to yield a value in $B$ when measured, unless the quantum state is an eigenstate of the measured observable $A$, the system does not possess any categorical property corresponding to $A$’s having a specific value in the set $B$. Putnam seems to assume that a realist interpretation of (\*) should consist in assigning to $A$ some unknown value within $B$, for which quantum mechanics yields a non-trivial probability. However, an attempt to make such assignments simultaneously for all observables runs afoul of Gleason’s Theorem.[^note-6]

### 2.2 Operational Quantum Logic

If we put aside scruples about “measurement” as a primitive term in physical theory, and accept a principled distinction between “testable” and non-testable properties, then the fact that $L(\mathbf{H})$ is not Boolean is unremarkable, and carries no implication about logic *per se*. Quantum mechanics is, on this view, a theory about the possible statistical distributions of outcomes of certain measurements, and its non-classical “logic” simply reflects the fact that not all observable phenomena can be observed simultaneously. Because of this, the set of probability-bearing events (or propositions) is *less* rich than it would be in classical probability theory, and the set of possible statistical distributions, accordingly, less tightly constrained. That some “non-classical” probability distributions allowed by this theory are actually manifested in nature is perhaps surprising, but in no way requires any deep shift in our understanding of logic or, for that matter, of probability.

This is hardly the last word, however. Having accepted all of the above, there still remains the question of *why* the logic of measurement outcomes should have the very special form $L(\mathbf{H})$, and never anything more general.[^note-7] This question entertains the idea that the formal structure of quantum mechanics may be *uniquely determined* by a small number of reasonable assumptions, together perhaps with certain manifest regularities in the observed phenomena. This possibility is already contemplated in von Neumann’s *Grundlagen* (and also his later work in continuous geometry), but first becomes explicit—and programmatic—in the work of George Mackey [1957, 1963]. Mackey presents a sequence of six axioms, framing a very conservative generalized probability theory, that underwrite the construction of a “logic” of experimental propositions, or, in his terminology, “questions”, having the structure of a sigma-orthomodular partially-ordered set (see Section 4 and the supplement document [The Basic Theory of Ordering Relations](qt-quantlog.supplement.md) for definitions of these terms). The outstanding problem, for Mackey, was to explain why this poset *ought to* be isomorphic to $L(\mathbf{H})$:

> Almost all modern quantum mechanics is based implicitly or explicitly on the following assumption, which we shall state as an axiom:
>
> > Axiom VII: The partially ordered set of all questions in quantum mechanics is isomorphic to the partially ordered set of all closed subspaces of a separable, infinite dimensional Hilbert space.
>
> This axiom has rather a different character from Axioms I through VI. These all had some degree of physical naturalness and plausibility. Axiom VII seems entirely ad hoc. Why do we make it? Can we justify making it? … Ideally, one would like to have a list of physically plausible assumptions from which one could deduce Axiom VII. Short of this one would like a list from which one could deduce a set of possibilities for the structure … all but one of which could be shown to be inconsistent with suitably planned experiments. [Mackey 1963: 71–72][^mackey-1963]

Since Mackey’s writing there has grown up an extensive technical literature exploring variations on his axiomatic framework in an effort to supply the missing assumptions. The remainder of this article presents a brief survey of the current state of this project.

## 3. Generalized Probability Theory

Rather than restate Mackey’s axioms verbatim, I shall paraphrase them in the context of an approach to generalized probability theory due to D. J. Foulis and C. H. Randall having—among the many more or less analogous approaches available[^note-8]—certain advantages of simplicity and flexibility. References for this section are Foulis, Greechie, and Rüttimann [1992]; Foulis, Piron and Randall [1983]; Randall and Foulis [1983]; see also Gudder [1989]; Wilce [2000b] and Wilce [2009] for surveys.

### 3.1 Discrete Classical Probability Theory

It will be helpful to begin with a review of classical probability theory. In its simplest formulation, classical probability theory deals with a (discrete) set $E$ of mutually exclusive outcomes, as of some measurement, experiment, etc., and with the various *probability weights* that can be defined thereon—that is, with mappings $\omega : E \rightarrow[0,1]$ summing to 1 over $E$.[^note-9]

Notice that the set $\Delta(E)$ of all probability weights on $E$ is *convex*, in that, given any sequence $\omega_1,\omega_2,\ldots$ of probability weights and any sequence $t_1,t_2,\ldots$ of non-negative real numbers summing to one, the convex sum or “mixture” $t_1\omega_1 + t_2\omega_2 +\ldots$ (taken pointwise on $E)$ is again a probability weight. The extreme points of this convex set are exactly the “point-masses” $\delta(x)$ associated with the outcomes $x \in E$:

$$\delta(x)(y) = 1 \textrm{ if } x = y, \textrm{ and } 0 \textrm{ otherwise.}$$

Thus, $\Delta(E)$ is a *simplex*: each point $\omega \in \Delta(E)$ is representable in a unique way as a convex combination of extreme points, namely:

$$\omega = \sum \omega(x)\delta(x)$$

We also need to recall the concept of a *random variable*. If $E$ is an outcome set and $V$, some set of “values” (real numbers, pointer-readings, or what not), a $V$-*valued random variable* is simply a mapping $f : E \rightarrow V$. The heuristic (but it need only be taken as that) is that one “measures” the random variable $f$ by “performing” the experiment represented by $E$ and, upon obtaining the outcome $x \in E$, recording $f(x)$ as the measured value. Note that if $V$ is a set of real numbers, or, more generally, a subset of a vector space, we may define the *expected value* of $f$ in a state $\omega \in \Delta(E)$ by:

$$E(f,\omega) = \sum_{x\in E} f(x)\omega(x).$$

### 3.2 Test Spaces

A very natural direction in which to generalize discrete classical probability theory is to allow for a multiplicity of outcome-sets, each representing a different “experiment”. To formalize this, let us agree that a *test space* is a non-empty collection A of non-empty sets $E,F,\ldots$, each construed as a discrete outcome-set as in classical probability theory. Each set $E \in \mathcal{A}$ is called a *test*. The set $X = \cup \mathcal{A}$ of all outcomes of all tests belonging to $\mathcal{A}$ is called the *outcome space* of $\mathcal{A}$. Notice that we allow distinct tests to overlap, i.e., to have outcomes in common.[^note-10]

If $\mathcal{A}$ is a test space with outcome-space $X$, a *state* on $\mathcal{A}$ is a mapping $\omega : X \rightarrow$ [0,1] such that $\sum_{x\in E} \omega(x) = 1$ for every test $E \in \mathcal{A}$. Thus, a state is a consistent assignment of a probability weight to each test—consistent in that, where two distinct tests share a common outcome, the state assigns that outcome the same probability whether it is secured as a result of one test or the other. (This may be regarded as a normative requirement on the outcome-identifications implicit in the structure of $\mathcal{A}$: if outcomes of two tests are not equiprobable in all states, they ought not to be identified.) The set of all states on $\mathcal{A}$ is denoted by $\Omega(\mathcal{A})$. This is a convex set, but in contrast to the situation in discrete classical probability theory, it is generally not a simplex.

The concept of a random variable admits several generalizations to the setting of test spaces. Let us agree that a *simple (real-valued) random variable* on a test space $\mathcal{A}$ is a mapping $f : E \rightarrow \mathbf{R}$ where $E$ is a test in $\mathcal{A}$. We define the *expected value* of $f$ in a state $\omega \in \Omega(\mathcal{A})$ in the obvious way, namely, as the expected value of $f$ with respect to the probability weight obtained by restricting *ω* to $E$ (provided, of course, that this expected value exists). One can go on to define more general classes of random variables by taking suitable limits (for details, see Younce [1987]).

In classical probability theory (and especially in classical statistics) one usually focuses, not on the set of all possible probability weights, but on some designated subset of these (e.g., those belonging to a given family of distributions). Accordingly, by a *probabilistic model*, I mean pair $(\mathcal{A},\Delta)$ consisting of a test space $\mathcal{A}$ and a designated set of states $\Delta \subseteq \Omega(\mathcal{A})$ on $\mathcal{A}$. I’ll refer to $\mathcal{A}$ as the *test space* and to $\Delta$ as the *state space* of the model.

I’ll now indicate how this framework can accommodate both the usual measure-theoretic formalism of full-blown classical probability theory and the Hilbert-space formalism of quantum probability theory.

### 3.3 Kolmogorovian Probability Theory

Let $S$ be a set, understood for the moment as the state-space of a physical system, and let $\Sigma$ be a *σ*-algebra of subsets of $S$. We can regard each partition $E$ of $S$ into countably many pair-wise disjoint $\Sigma$-measurable subsets as representing a “coarse-grained” approximation to an imagined perfect experiment that would reveal the state of the system. Let $\mathcal{A}_{\Sigma}$ be the test space consisting of all such partitions. Note that the outcome set for $\mathcal{A}_{\Sigma}$ is the set $X = \Sigma \setminus \{\varnothing \}$ of non-empty $\Sigma$-measurable subsets of $S$. Evidently, the probability weights on $\mathcal{A}_{\Sigma}$ correspond exactly to the countably additive probability measures on $\Sigma$.

### 3.4 Quantum Probability Theory

Let $\mathbf{H}$ denote a complex Hilbert space and let $\mathcal{A}_{\mathbf{H}}$ denote the collection of (unordered) orthonormal bases of $\mathbf{H}$. Thus, the outcome-space $X$ of $\mathcal{A}_{\mathbf{H}}$ will be the unit sphere of $\mathbf{H}$. Note that if $u$ is any unit vector of $\mathbf{H}$ and $E \in \mathcal{A}_{\mathbf{H}}$ is any orthonormal basis, we have

$$\sum_{x\in E} \lvert\langle u,x\rangle\rvert^2 = \llvert u\rrvert ^2 = 1$$

Thus, each unit vector of $\mathbf{H}$ determines a probability weight on $\mathcal{A}_{\mathbf{H}}$. Quantum mechanics asks us to take this literally: any “maximal” discrete quantum-mechanical observable is modeled by an orthonormal basis, and any pure quantum mechanical state, by a unit vector in exactly this way. Conversely, every orthonormal basis and every unit vector are understood to correspond to such a measurement and such a state.

Gleason’s theorem can now be invoked to identify the states on $\mathcal{A}_{\mathbf{H}}$ with the density operators on $\mathbf{H}$: to each state *ω* in $\Omega(\mathcal{A}_{\mathbf{H}})$ there corresponds a unique density operator $W$ such that, for every unit vector $x$ of $\mathbf{H}, \omega(x) = \langle Wx,x\rangle = Tr(WP_x), P_x$ being the one-dimensional projection associated with $x$. Conversely, of course, every such density operator defines a unique state by the formula above. We can also represent simple real-valued random variables operator-theoretically. Each bounded simple random variable $f$ gives rise to a bounded self-adjoint operator $A = \sum_{x\in E} f(x)P_x$. The spectral theorem tells us that every self-adjoint operator on $\mathbf{H}$ can be obtained by taking suitable limits of operators of this form.

## 4. Logics associated with probabilistic models

Associated with any probabilistic model $(\mathcal{A},\Delta)$ are several partially ordered sets, each of which has some claim to the status of an “empirical logic” associated with the model. In this section, I’ll discuss two: the so-called *operational logic* $\Pi(\mathcal{A})$ and the *property lattice* $\mathbf{L}(\mathcal{A},\Delta)$. Under relatively benign conditions on $\mathcal{A}$, the former is an *orthoalgebra*. The latter is always a complete lattice, and under plausible further assumptions, atomic. Moreover, there is a natural order preserving mapping from *Π* to $\mathbf{L}$. This is not generally an order-isomorphism, but when it is, we obtain a complete orthomodular lattice, and thus come a step closer to the projection lattice of a Hilbert space.

### 4.1 Operational Logics

If $\mathcal{A}$ is a test space, an $\mathcal{A}$*-event* is a set of $\mathcal{A}$-outcomes that is contained in some test. In other words, an $\mathcal{A}$-event is simply an event in the classical sense for any one of the tests belonging to $\mathcal{A}$. Now, if $A$ and $B$ are two $\mathcal{A}$-events, we say that $A$ and $B$ are *orthogonal*, and write $A\binbot B$, if they are disjoint and their union is again an event. We say that two orthogonal events are *complements* of one another if their union is a test. We say that events $A$ and $B$ are *perspective*, and write $A\sim B$, if they share any common complement. (Notice that any two tests $E$ and $F$ are perspective, since they are both complementary to the empty event.)

**4.1 Definition**: A test space $\mathcal{A}$ is said to be *algebraic* if for all events $A, B, C$ of $\mathcal{A}$, $A\sim B \binbot C$ implies $A\binbot C$.

While it is possible to construct perfectly plausible examples of test spaces that are not algebraic, many test spaces that one encounters in nature do enjoy this property. In particular, the Borel and quantum test spaces described in the preceding section are algebraic. The more important point is that, as an axiom, algebraicity is relatively benign, in the sense that many test spaces can be “completed” to become algebraic. In particular, if every outcome has probability greater than 1/2 in at least one state, then $\mathcal{A}$ is contained in an algebraic test space $\mathcal{B}$ having the same outcomes and the same states as $\mathcal{A}$ (see Gudder [1989] for details).

It can be shown[^note-11] that test space $\mathcal{A}$ is algebraic if and only if it satisfies the condition

For all events $A, B$ of $\mathcal{A}$, if $A\sim B$, then any complement of $B$ is a complement of $A$.

From this, it is not hard to see that, for an algebraic test space $\mathcal{A}$, the relation $\sim $ of perspectivity is then an equivalence relation on the set of $\mathcal{A}$-events. More than this, if $\mathcal{A}$ is algebraic, then $\sim $ is a *congruence* for the partial binary operation of forming unions of orthogonal events: in other words, for all $\mathcal{A}$-events $A, B$, and $C, A\sim B$ and $B\binbot C$ imply that $A\binbot C$ and $A\cup C \sim B\cup C$.

Let $\Pi(\mathcal{A})$ be the set of equivalence classes of $\mathcal{A}$-events under perspectivity, and denote the equivalence class of an event $A$ by $p(A)$; we then have a natural partial binary operation on $\Pi(\mathcal{A})$ defined by $p(A)\oplus p(B) = p(A\cup B)$ for orthogonal events $A$ and $B$. Setting 0 :$= p(\varnothing)$ and 1 :$= p(E), E$ any member of $\mathcal{A}$, we obtain a partial-algebraic structure $(\Pi(\mathcal{A}),\oplus ,0,1)$, called the *logic* of $\mathcal{A}$. This satisfies the following conditions:

1. $\oplus$ is associative and commutative:
2. If $a\oplus(b\oplus c)$ is defined, so is $(a\oplus b)\oplus c$, and the two are equal
3. If $a\oplus b$ is defined, so is $b\oplus a$, and the two are equal.
4. $0\oplus a = a$, for every $a \in \mathbf{L}$
5. For every $a \in \mathbf{L}$, there exists a unique $a' \in \mathbf{L}$ with $a\oplus a' = 1$
6. $a\oplus a$ exists only if $a = 0$

We may now define:

**4.2 Definition**: A structure $(\mathbf{L},\oplus ,0,1)$ satisfying conditions (a)–(d) above is called an *orthoalgebra*.

Thus, the logic of an algebraic test space is an orthoalgebra. One can show that, conversely, every orthoalgebra arises as the logic $\Pi(\mathcal{A})$ of an algebraic test space $\mathcal{A}$ (Golfin [1988]). Note that non-isomorphic test spaces can have isomorphic logics.

### 4.2 Orthocoherence

Any orthoalgebra $\mathbf{L}$ is partially ordered by the relation $a\le b$ iff $b = a\oplus c$ for some $c\binbot a$. Relative to this ordering, the mapping $a\rightarrow a'$ is an orthocomplementation and $a\binbot b$ iff $a\le b'$. It can be shown that $a\oplus b$ is always a minimal upper bound for $a$ and $b$, but it is generally not the *least* upper bound. Indeed, we have the following (Foulis, Greechie and Ruttimann [1992], Theorem 2.12):

**4.3 Lemma**: For an orthoalgebra $(\mathbf{L},\oplus ,0,1)$, the following are equivalent:

1. $a\oplus b = a\vee b$, for all $a, b$ in $\mathbf{L}$
2. If $a\oplus b, b\oplus c$, and $c\oplus a$ all exist, then so does $a\oplus b\oplus c$
3. The orthoposet $(\mathbf{L},\le ,')$ is *orthomodular*, i.e., for all $a, b\in L$, if $a\le b$ then $(b \wedge a') \vee a$ exists and equals $b$.

An orthoalgebra satisfying condition (b) is said to be *orthocoherent*. In other words: an orthoalgebra is orthocoherent if and only if finite pairwise summable subsets of $\mathbf{L}$ are jointly summable. The lemma tells us that every orthocoherent orthoalgebra is, *inter alia*, an orthomodular poset. Conversely, an orthocomplemented poset is orthomodular iff $a\oplus b = a\vee b$ is defined for all pairs with $a\le b'$ and the resulting partial binary operation is associative—in which case the resulting structure $(\mathbf{L},\oplus ,0,1)$ is an orthocoherent orthoalgebra, the canonical ordering on which agrees with the given ordering on $\mathbf{L}$. Thus, orthomodular posets (the framework for Mackey’s version of quantum logic) are equivalent to orthocoherent orthoalgebras.

A condition related to, but stronger than, orthocoherence is that any pairwise *compatible* propositions should be jointly compatible. This is sometimes called *regularity*. Most naturally occurring orthomodular lattices and posets are regular. In particular, Harding (1996, 1998)[^harding-1996][^harding-1998] has shown that the direct-product decompositions of any algebraic, relational or topological structure can be organized in a natural way into a regular orthomodular poset.[^note-12]

Some version of orthocoherence or regularity was taken by Mackey and many of his successors as an axiom. (Orthocoherence appears, in an infinitary form, as Mackey’s axiom V; regularity appears in the definition of a partial Boolean algebra in the work of Kochen and Specker (1965).) However, it is quite easy to construct simple model test spaces, having perfectly straightforward—even classical—interpretations, the logics of which are not orthocoherent. There has never been given any entirely compelling reason for regarding orthocoherence as an essential feature of all reasonable physical models. Moreover, certain apparently quite well-motivated constructions that one wants to perform with test spaces tend to destroy orthocoherence (see section 7).

### 4.3 Lattices of Properties

The decision to accept measurements and their outcomes as primitive concepts in our description of physical systems does not mean that we must forgo talk of the physical properties of such a system. Indeed, such talk is readily accommodated in the present formalism.[^note-13] In the approach we have been pursuing, a physical system is represented by a probabilistic model $(\mathcal{A},\Delta)$, and the system’s states are identified with the probability weights in $\Delta$. Classically, *any* subset *Γ* of the state-space $\Delta$ corresponds to a categorical property of the system. However, in quantum mechanics, and indeed even classically, not every such property will be testable (or “physical”). In quantum mechanics, only subsets of the state-space corresponding to closed subspaces of the Hilbert space are testable; in classical mechanics, one usually takes only, e.g., Borel sets to correspond to testable properties: the difference is that the testable properties in the latter case happen still to form a Boolean algebra of sets, where in the former case, they do not.

One way to frame this distinction is as follows. The *support* of a set of states $\Gamma \subseteq \Delta$ is the set

$$S(\Gamma) = \{x\in X \mid \exists \omega \in \Gamma \omega(x) > 0 \}$$

of outcomes that are possible when the property *Γ* obtains. There is a sense in which two properties are empirically indistinguishable if they have the same support: we cannot distinguish between them by means of a single execution of a single test. We might therefore wish to identify physical properties with classes of physically indistinguishable classical properties, or, equivalently, with their associated supports. However, if we wish to adhere to the programme of representing physical properties as subsets (rather than as equivalence-classes of subsets) of the state-space, we can do so, as follows. Define a mapping $F : \wp(X) \rightarrow \wp(\Delta)$ by $F(J) = \{\omega \in \Delta \mid S(\omega) \subseteq J \}$. The mapping $\Gamma \rightarrow F(S(\Gamma))$ is then a *closure operator* on $\wp(\Delta)$, and the collection of closed sets (that is, the range of $F)$ is a complete lattice of sets, closed under arbitrary intersection.[^note-14] Evidently, classical properties—subsets of $\Delta$—have the same support iff they have the same closure, so we may identify physical properties with closed subsets of the state-space:

**4.4 Definition**: The *property lattice* of the model $(\mathcal{A},\Delta)$ is the complete lattice $\mathbf{L} = \mathbf{L}(\mathcal{A},\Delta)$ of all subsets of $\Delta$ of the form $F(J), J$ any set of outcomes.[^note-15]

We now have two different “logics” associated with a probabilistic model $(\mathcal{A},\Delta)$ with $\mathcal{A}$ algebraic: a “logic” $\Pi(\mathcal{A})$ of experimental propositions that is an orthoalgebra, but generally not a lattice, and a “logic” $\mathbf{L}(\mathcal{A},\Delta)$ of properties that is a complete lattice, but rarely orthocomplemented in any natural way (Randall and Foulis [1983]). The two are connected by a natural mapping [ ] : $\Pi \rightarrow \mathbf{L}$, given by $p \rightarrow[p] = F(J_p)$ where for each $p\in \Pi$, $J_p = \{x\in X \mid p(x) \nleq p' \}$. That is, $J_p$ is the set of outcomes that are consistent with $p$, and [$p$] is the largest (i.e., weakest) physical property making $p$ certain to be confirmed if tested.

The mapping $p \rightarrow[p$] is order preserving. For both the classical and quantum-mechanical models considered above, it is in fact an order-isomorphism. Whenever this is the case, *Π* will inherit from $\mathbf{L}$ the structure of a complete lattice, which will then automatically be orthomodular by Lemma 4.3. In other words, in such cases we have only *one* logic, which is a complete orthomodular lattice. While it is surely too much to expect that [ ] will be an order-isomorphism every *conceivable* physical system—indeed, we can easily construct toy examples to the contrary—the condition is at least reasonably transparent in its meaning.

## 5. Piron’s Theorem

Suppose that the logic and property lattices of a model *are* isomorphic, so that the logic of propositions/properties is a complete orthomodular lattice. The question then arises: how close does this bring us to quantum mechanics—that is, to the projection lattice $L(\mathbf{H})$ of a Hilbert space?

The answer is: without additional assumptions, not very. The lattice $L(\mathbf{H})$ has several quite special order-theoretic features. First it is *atomic*—every element is the join of minimal non-zero elements (i.e., one-dimensional subspaces). Second, it is *irreducible*—it can not be expressed as a non-trivial direct product of simpler OMLs.[^note-16] Finally, and most significantly, it satisfies the so-called *atomic covering law*: if $p \in L(\mathbf{H})$ is an atom and $p\nleq q$, then $p \vee q$ *covers* $q$ (no element of $L(\mathbf{H})$ lies strictly between $p \vee q$ and $q)$.

These properties still do not quite suffice to capture $L(\mathbf{H})$, but they do get us into the right ballpark. Let $\mathbf{V}$ be any inner product space over an involutive division ring $D$. A subspace $\mathbf{M}$ of $\mathbf{V}$ is said to be $\bot$-*closed* iff $\mathbf{M} = \mathbf{M}^{\bot \bot}$, where $\mathbf{M}^{\bot} = \{v\in \mathbf{V} \mid \forall m\in \mathbf{M}( \langle v,m\rangle = 0)\}$. Ordered by set-inclusion, the collection $L(\mathbf{V})$ of all $\bot$-closed subspaces of $\mathbf{V}$ forms a complete atomic lattice, orthocomplemented by the mapping $\mathbf{M} \rightarrow \mathbf{M}^{\bot}$. A theorem of Amemiya and Araki (1966) shows that a real, complex or quaternionic inner product space $\mathbf{V}$ with $L(\mathbf{V})$ orthomodular, is necessarily complete. For this reason, an inner product space $\mathbf{V}$ over an involutive division ring is called a *generalized Hilbert space* if its lattice$L(\mathbf{V})$ of $\bot$-closed subspaces is orthomodular. The following representation theorem is due to C. Piron [1964]:

**5.1 Theorem**: Let $L$ be a complete, atomic, irreducible orthomodular lattice satisfying the atomic covering law. If $L$ contains at least 4 orthogonal atoms, then there exists an involutive division ring $D$ and a generalized Hilbert space $\mathbf{V}$ over $D$ such that $L$ is isomorphic to $L(\mathbf{V})$.

It should be noted that generalized Hilbert spaces have been constructed over fairly exotic division rings.[^note-17] Thus, while it brings us tantalizingly close, Piron’s theorem does not quite bring us all the way back to orthodox quantum mechanics.

### 5.1 Conditioning and the Covering Law

Let us call a complete orthomodular lattice satisfying the hypotheses of Piron’s theorem a *Piron lattice*. Can we give any general reason for supposing that the logic/property lattice of a physical system (one for which these are isomorphic) is a Piron lattice? Or, failing this, can we at least ascribe some clear physical content to these assumptions? The atomicity of $L$ follows if we assume that every pure state represents a “physical property”. This is a strong assumption, but its content seems clear enough. Irreducibility is usually regarded as a benign assumption, in that a reducible system can be decomposed into its irreducible parts, to each of which Piron’s Theorem applies.

The covering law presents a more delicate problem. While it is probably safe to say that no simple and entirely compelling argument has been given for assuming its general validity, Piron [1964, 1976] and others (e.g., Beltrametti and Cassinelli [1981] and Guz [1978]) have derived the covering law from assumptions about the way in which measurement results warrant inference from an initial state to a final state. Here is a brief sketch of how this argument goes. Suppose that there is some reasonable way to define, for an initial state $q$ of the system, represented by an atom of the logic/property lattice $L$, a final state $\phi_p (q)$—either another atom, or perhaps 0—conditional on the proposition $p$ having been confirmed. Various arguments can be adduced suggesting that the only reasonable candidate for such a mapping is the *Sasaki projection* $\phi_p : L \rightarrow L$, defined by

$\phi_p (q) = (q \vee p') \wedge p$.[^note-18]

It can be shown that an atomic OML satisfies the atomic covering law just in case Sasaki projections take atoms again to atoms, or to 0. Another interesting view of the covering law is developed by Cohen and Svetlichny [1987].

## 6. Classical Representations

The perennial question in the interpretation of quantum mechanics is that of whether or not essentially classical explanations are available, even in principle, for quantum-mechanical phenomena. Quantum logic has played a large role in shaping (and clarifying) this discussion, in particular by allowing us to be quite precise about what we *mean* by a classical explanation.

### 6.1 Classical Embeddings

Suppose we are given a statistical model $(\mathcal{A},\Delta)$. A very straightforward approach to constructing a “classical interpretation” of $(\mathcal{A},\Delta)$ would begin by trying to embed $\mathcal{A}$ in a Borel test space $\mathcal{B}$, with the hope of then accounting for the statistical states in *δ* as averages over “hidden” classical—that is, dispersion-free—states on the latter. Thus, we’d want to find a set $S$ and a mapping $X \rightarrow \wp(S)$ assigning to each outcome $x$ of $\mathcal{A}$ a *set* $x* \subseteq S$ in such a way that, for each test $E \in \mathcal{A}, \{x* \mid x \in E\}$ forms a partition of $S$. If this can be done, then each outcome $x$ of $\mathcal{A}$ simply records the fact that the system is in one of a certain set of states, namely, $x$\*. If we let $\Sigma$ be the *σ*-algebra of sets generated by sets of the form $\{x* \mid x \in X\}$, we find that each probability measure $\mu$ on $\Sigma$ pulls back to a state $\mu$\* on $\mathcal{A}$, namely, $\mu *(x) = \mu(x$\*). So long as every state in *δ* is of this form, we may claim to have given a completely classical interpretation of the model $(\mathcal{A},\Delta)$.

The minimal candidate for $S$ is the set of *all* dispersion-free states on $\mathcal{A}$. Setting $x* = \{s\in S \mid s(x) = 1\}$ gives us a classical interpretation as above, which I’ll call the *classical image* of $\mathcal{A}$. Any other classical interpretation factors through this one. Notice, however, that the mapping $x \rightarrow x$\* is injective only if there are sufficiently many dispersion-free states to separate distinct outcomes of $\mathcal{A}$. If $\mathcal{A}$ has $no$ dispersion-free states at all, then its classical image is *empty*. Gleason’s theorem tells us that this is the case for quantum-mechanical models. Thus, this particular kind of classical explanation is not available for quantum mechanical models.

It is sometimes overlooked that, even if a test space $\mathcal{A}$ does have a separating set of dispersion-free states, there may exist statistical states on $\mathcal{A}$ that *can not* be realized as mixtures of these. The classical image provides no explanation for such states. For a very simple example of this sort of thing, consider the test space:

$$\mathcal{A} = \{\{a, x, b\}, \{b, y, c\}, \{c, z, a\}\}$$

and the state $\omega(a) = \omega(b) = \omega(c) = \frac{1}{2}$, $\omega(x) = \omega(y) = \omega(z) = 0$. It is a simple exercise to show that *ω* cannot be expressed as a weighted average of $\{0,1\}$-valued states on $\mathcal{A}$. For further examples and discussion of this point, see Wright [1980].

### 6.2 Contextual Hidden Variables

The upshot of the foregoing discussion is that most test spaces can’t be embedded into any classical test space, and that even where such an embedding exists, it typically fails to account for some of the model’s states. However, there is one very important class of models for which a satisfactory classical interpretation is *always* possible. Let us call a test space $\mathcal{A}$ *semi-classical* if its tests do not overlap; i.e., if $E \cap F = \varnothing$ for $E, F \in \mathcal{A}$, with $E\ne F$.

**6.1 Lemma**: Let $\mathcal{A}$ be semi-classical. Then $\mathcal{A}$ has a separating set of dispersion-free states, and every extreme state on $\mathcal{A}$ is dispersion-free.

As long as $\mathcal{A}$ is locally countable (i.e., no test $E$ in $\mathcal{A}$ is uncountable), every state can be represented as a convex combination, in a suitable sense, of extreme states (Wilce [1992]). Thus, every state of a locally countable semi-classical test space has a classical interpretation.

Even though neither Borel test spaces nor quantum test spaces are semi-classical, one might argue that in any real laboratory situation, semi-classicality is the rule. Ordinarily, when one writes down in one’s laboratory notebook that one has performed a given test and obtained a given outcome, one always has a record of which test was performed. Indeed, given any test space $\mathcal{A}$, we may always form a semi-classical test space simply by forming the co-product (disjoint union) of the tests in $\mathcal{A}$. More formally:

**6.2 Definition**: For each test $E$ in $\mathcal{A}$, let $E^{\sim} = \{ (x,E) \mid x \in E \}$. The *semi-classical cover* of $\mathcal{A}$ is the test space

$$\mathcal{A}^{\sim} = \{E^{\sim} \mid E \in \mathcal{A} \}.$$

We can regard $\mathcal{A}$ as arising from $\mathcal{A}^{\sim}$ by deletion of the record of which test was performed to secure a given outcome. Note that every state on $\mathcal{A}$ defines a state $\omega^{\sim}$ on $\mathcal{A}^{\sim}$ by $\omega^{\sim} (x,E) = \omega(x)$. The mapping $\omega \rightarrow \omega^{\sim}$ is plainly injective; thus, we may identify the state-space of $\mathcal{A}$ with a subset of the state-space of $\mathcal{A}^{\sim}$. Notice that there will typically be many states on $\mathcal{A}^{\sim}$ that *do not* descend to states on $\mathcal{A}$. We might wish to think of these as “non-physical”, since they do not respect the (presumably, physically motivated) outcome-identifications whereby $\mathcal{A}$ is defined.

Since it is semi-classical, $\mathcal{A}^{\sim}$ admits a classical interpretation, as per Lemma 7.1. Let’s examine this. An element of $S(\mathcal{A}^{\sim}$) amounts to a mapping $f : \mathcal{A}^{\sim} \rightarrow X$, assigning to each test $E \in \mathcal{A}$, an outcome $f(E) \in E$. This is a (rather brutal) example of what is meant by a *contextual (dispersion-free) hidden variable*. The construction above tells us that such contextual hidden variables will be available for statistical models quite generally. For other results to the same effect, see Kochen and Specker [1967], Gudder [1970], Holevo [1982], and, in a different direction, Pitowsky [1989].[^note-19]

Note that the simple random variables on $\mathcal{A}$ correspond exactly to the simple random variables on $\mathcal{A}^{\sim}$, and that these, in turn, correspond to *some* of the simple random variables (in the usual sense) on the measurable space $S(\mathcal{A}^{\sim}$). Thus, we have the following picture: The model $(\mathcal{A},\Delta)$ can always be obtained from a classical model simply by omitting some random variables, and identifying outcomes that can no longer be distinguished by those that remain.

All of this might suggest that our generalized probability theory presents no significant conceptual departure from classical probability theory. On the other hand, models constructed along the foregoing lines have a distinctly ad hoc character. In particular, the set of “physical” states in one of the classical (or semi-classical) models constructed above is determined not by any independent physical principle, but only by consistency with the original, non-semiclassical model. Another objection is that the contextual hidden variables introduced in this section are badly non-local. It is by now widely recognized that this non-locality is the principal locus of non-classicality in quantum (and more general) probability models. (For more on this, see the entry on Bell’s theorem.)

## 7. Composite Systems

Some of the most puzzling features of quantum mechanics arise in connection with attempts to describe compound physical systems. It is in this context, for instance, that both the measurement problem and the non-locality results centered on Bell’s theorem arise. It is interesting that coupled systems also present a challenge to the quantum-logical programme. I will conclude this article with a description of two results that show that the coupling of quantum-logical models tends to move us further from the realm of Hilbert space quantum mechanics.

### 7.1 The Foulis-Randall Example

A particularly striking result in this connection is the observation of Foulis and Randall [1981a] that any reasonable (and reasonably general) tensor product of orthoalgebras will fail to preserve ortho-coherence. Consider the test space

$$\mathcal{A}_5 = \{\{a,x,b\}, \{b,y,c\}, \{c,z,d\}, \{d,w,e\}, \{e,v,a\}\}$$

consisting of five three-outcome tests pasted together in a loop. This test space is by no means pathological; it is both ortho-coherent and algebraic, and its logic is an orthomodular lattice. Moreover, it admits a separating set of dispersion-free states and hence, a classical interpretation. It can also be embedded in the test space $\mathcal{A}_{\mathbf{H}}$ of any 3-dimensional Hilbert space $\mathbf{H}$. Now consider how we might model a compound system consisting of two separated sub-systems each modeled by $\mathcal{A}_5$. We would need to construct a test space $\mathcal{B}$ and a mapping $\otimes : X \times X \rightarrow Y = \cup \mathcal{B}$ satisfying, minimally, the following;

1. For all outcomes $x, y, z \in X$, if $x\binbot y$, then $x\otimes z \binbot y\otimes z$ and $z\otimes x \binbot z\otimes y$,
2. For each pair of states $\alpha , \beta \in \Omega(\mathcal{A}_5)$, there exists at least one state *ω* on $\mathcal{B}$ such that $\omega(x\otimes y) = \alpha(x)\beta(y)$, for all outcomes $x, y \in X$.

Foulis and Randall show that no such embedding exists for which $\mathcal{B}$ is orthocoherent. Indeed, suppose we have a test space $\mathcal{B}$ and an embedding satisfying conditions (a) and (b). Consider the set of outcomes

$$S = \{a \otimes b, b \otimes e, c \otimes c, d \otimes a, e \otimes d\}.$$

By (a), this set is pairwise orthogonal. Now let *α* be the state on $\mathcal{A}_5$ taking the value 1/2 on outcomes $a, b, c, d$ and $e$, and the value 0 on $x, y, z, w$ and $v$. By condition (b), there exists state *ω* on $\mathcal{B}$ such that

$$\omega(s \otimes t) = \alpha(s) \alpha(t)$$

for all outcomes $s, t$ in $X$. But this state takes the constant value 1/4 on the set $S$, whence, it sums over this set to $5/4 \gt 1$. Hence, $S$ is not an event, and $\mathcal{B}$ is not orthocoherent.

It is important to emphasize here that the test space $\mathcal{A}_5$ has a perfectly unproblematic quantum-mechanical interpretation, as it can be realized as a set of orthonormal bases in a 3-dimensional Hilbert space $\mathbf{H}$. However, the *state* *ω* figuring in the Foulis-Randall example cannot arise quantum-mechanically (much less classically). (Indeed, this follows from the example itself: the canonical mapping $\mathbf{H} \times \mathbf{H} \rightarrow \mathbf{H} \otimes \mathbf{H}$ provides a mapping satisfying the conditions (a) and (b) above. Since $\mathbf{L}(\mathbf{H} \otimes \mathbf{H})$ is orthocoherent, the set S corresponds to a pairwise orthogonal family of projections, over which a quantum-mechanical state would have to sum to no more than 1.)

### 7.2 Aerts’ Theorem

Another result having a somewhat similar force is that of Aerts [1981]. If $L_1$ and $L_2$ are two Piron lattices, Aerts constructs in a rather natural way a lattice $L$ representing two *separated* systems, each modeled by one of the given lattices. Here “separated” means that each pure state of the larger system $L$ is entirely determined by the states of the two component systems $L_1$ and $L_2$. Aerts then shows that $L$ is again a Piron lattice iff at least one of the two factors $L_1$ and $L_2$ is classical. (This result has recently been strengthened by Ischi [2000] in several ways.)

### 7.3 Ramifications

The thrust of these no-go results is that straightforward constructions of plausible models for composite systems destroy regularity conditions (ortho-coherence in the case of the Foulis-Randall result, orthomodularity and the covering law in that of Aerts’ result) that have widely been used to underwrite reconstructions of the usual quantum-mechanical formalism. This puts in doubt whether any of these conditions can be regarded as having the universality that the most optimistic version of Mackey’s programme asks for. Of course, this does not rule out the possibility that these conditions may yet be motivated in the case of especially *simple* physical systems.

In some quarters, the fact that the most traditional models of quantum logics lack a reasonable tensor product have have been seen as heralding the collapse of the entire quantum-logical enterprise. This reaction is premature. The Foulis-Randall example, for instance, shows that there can be no general tensor product that behaves properly on *all* orthomodular lattices or orthomodular posets (that is, orthocoherent orthoalgebras), *and* on *all* states thereon. But this does not rule out the existence of a satisfactory tensor product for classes of structures *larger* than that of orthomodular posets, or *smaller* than that of orthomodular lattices, or for classes of orthomodular lattices or posets with restricted state spaces. Quantum Mechanics itself provides one example. For another, as Foulis and Randall showed in Foulis and Randall [1981a], the class of unital orthoalgebras—that is, orthoalgebras in which every proposition has probability 1 in some state—*does* support a canonical tensor product satisfying their conditions (a) and (b).

Moving in the opposite direction, one can take it as an axiomatic requirement that a satisfactory physical theory be closed under some reasonable device for coupling separated systems. This suggests taking classes of systems, i.e., physical theories, as distinct from individual systems, as the focus of attention. And in fact, this is exactly the trend in much current work on the foundations of quantum mechanics.

A particularly fruitful approach of this kind, due to Abramsky and Coecke [2009] takes a physical theory to be represented by a symmetric monoidal category—roughly, a category equipped with a naturally symmetric and associative tensor product. Subject to some further constraints (e.g., compact closure), such categories exhibit formal properties strikingly reminiscent of quantum mechanics. Interestingly, it has recently been shown by Harding [2009] that, in every strongly compact closed category with biproducts, every object is associated with an orthomodular poset Proj$(A)$ of “weak projections”, and that Proj$(A \otimes B)$ behaves in many respects as a sensible tensor product for Proj$(A)$ and Proj$(B)$. From this perspective, the FR example simply exhibits a pathological example — $A_5$ and the state *α* — that can not be accommodated in such a theory, establishing that the monoidality requirement imposes a nontrivial restriction on the structure of individual systems.

This recent emphasis on systems in interaction is part of a more general shift of attention away from the static structure of states and observables and towards the *processes* in which physical systems can participate. This trend is evident not only in the category-theoretic formulation of Abramsky and Coecke (see also Coecke [2011]), but also in several recent axiomatic reconstructions of quantum theory (e.g., Hardy [2001, Other Internet Resources], Rau [2009], Dakic-Brukner [2011], Massanes and Mueller [2011], Chiribella-D’Ariano-Perinotti [2011], Wilce [2018]), most of which involve assumptions about how physical systems combine. In a different direction, Baltag and Smets [2005] enrich a Piron-style lattice-theoretic framework with an explicitly dynamical element, arriving at a quantum analogue of propositional dynamical logic.

## 8. Effect Algebras

Another recent development was the introduction in the early 1990s of structures called *effect algebras* (Foulis and Bennett [1994]) generalizing the orthoalgebras discussed in sect 4.1. The definition is almost identical, except that the weaker condition $a \perp a \Rightarrow a = 0$ is replaced by the weaker condition $a \perp 1 \ \Rightarrow \ a = 0$. Like orthoalgebras, effect algebras are partially ordered by setting $a \leq b$ iff $b = a \oplus c$ for some $c \perp a$.[^note-20]

A simple but important example is the effect algebra $[0,1]^{E}$ of functions $\,f : E \rightarrow [0,1]$, with $f \perp g$ iff $f + g \leq 1$ and, in that case, $f \oplus g = f + g$. One can regard elements of $[0,1]^{E}$ as “unsharp” or “fuzzy” versions of indicator functions $f : E \rightarrow \{0,1\}$. The set $\{0,1\}^{E}$ of indicator functions, regarded as a subeffect algebra of $[0,1]^{E}$, is an orthoalgebra and, of course, isomorphic to the boolean algebra of subsets of $E$.[^note-21]

Effect algebras exist in great abundance. In particular, if $\Omega$ is a convex set arising as the state-space of a probabilistic model, then the set ${\mathcal E}(\Omega)$ of bounded affine (convex-linear) functions $f : \Omega \rightarrow [0,1]$ form an effect algebra, with $f \oplus g = f + g$ if $f + g \leq 1$. The idea is that a function $\,f \in {\mathcal E}(\Omega)$ represents an "in principle" measurement outcome, with probability $f(\alpha)$ in state $\alpha \in \Omega$. If $f_0,...,f_n \in {\mathcal E}(\Omega)$ with $f_0 + \cdots + f_n = 1$, then the sequence $(f_0,...,f_n)$ rpresents an “in principle” observable with values $i = 0,...,n$, taking value $i$ with probability $f_i(\alpha)$.

## 8.1 Quantum Effects and Naimark’s Theorem

In the special case where $\Omega = \Omega(\mathbf{H})$, the set of density operators on a Hilbert space $\mathbf{H}$, one can show that every effect $f$ on $\Omega$ has the form $\,f(W) = \textrm{Tr}(W a)$ for a unique positive self-adjoint operator $a$ with $a \leq 1$. Conversely, such an operator defines an effect through the formula just given. One therefore identifies $\mathcal{E}(\Omega(\mathbf{H}))$ with the set $\mathcal{E}(\mathbf{H})$ of all positive self-adjoint operators on $\mathbf{H})$ with $0 \leq a \leq 1$, referring to these also as effects.

Arbitrary quantum effects, and arbitrary effect-valued observables, arise quite naturally as models of actual experimental outcomes. Consider an isolated quantum system $A$ with Hilbert space $\mathbf{H}_A$, and an ancillary system $B$, with Hilbert space $\mathbf{H}_{B}$, maintained in a reference state represented by a density operator $W^{B}_o$. If $A$ is in the state represented by a density operator $W^{A}$ on $\mathbf{H}_A$, thet state of the joint system is represented by $W^{A} \otimes W^{B}_o$. If we make a yes-no measurement on $AB$ represented by a projection operator $P_{AB}$ on $\mathbf{H}_{AB} = \mathbf{H}_{A} \otimes \mathbf{H}_{B}$ then the probability of obtaining a positive result is $\textrm{Tr}(P_{AB}(W^{A} \otimes W^{B}_{o}))$. This defines a bounded convex-linear function of $W^{A}$, and hence, there is a unique effect $a$ with $\textrm{Tr}((W^{A} \otimes W^{B}_{o})P_{AB}) = \textrm{Tr}(W^{A} a)$. This effect $a$ is called the *compression* of $P_{AB}$ onto $\mathbf{H}_{A}.$ In other words, we can understand $a$ as representing the result of measuring $P_{AB}$ on the combined system $AB$, holding $B$ in state $W^{B}_o$, and then “forgetting about” the ancillary system $B$. It is not difficult to show that every every effect on $A$ arises in this way from a projection on $\mathbf{H}_{A} \otimes \mathbf{H}_{B}$ for a suitable Hilbert space $\mathbf{H}_{B}$. More generally, a classic result in operator theory known as *Naimark’s Theorem* asserts that any effect-valued observable $a_1,...,a_n$ on $A$ arises by compression of an ordinary projection-valued observable $P_1,...,P_n$ on $AB$ for a suitable quantum system $B$. Thus, all effects, and indeed all effect-valued observables, on $A$ are physically realizable. In view of this, it is difficult to see why effect algebras should have any less claim to the status of a “quantum logic” than do, say, orthomodular posets.

## 8.2 Sequential effect algebras

A natural question is whether one can characterize those effect algebras of the special form $\mathcal{E}(\mathbf{H})$. One way in which effects arise naturally is in the context of sequential measurements. If $P$ is a projection, a measurement of $P$ in state corresponding to the density operator $W$ leaves the system in the state corresponding to the density operator

$$W_{p} := \frac{P W P}{\textrm{Tr}(W P)}.$$

A subsequent measurement of $q$ in this state then yields a positive result with probability $$\begin{equation} \textrm{Tr}(W_{P} Q) = \frac{\textrm{Tr}(QP W PQ)}{\textrm{Tr}(W P)} = \frac{\textrm{Tr}(W PQP)}{\textrm{Tr}(W P)}. \end{equation}$$ The operator $PQP$ is not a projection unless $P$ and $Q$ commute, but is always an effect. If we write $\Pr(a|W)$ for $\textrm{Tr}(Wa)$ for arbitrary effects $a$, then the above can be rewritten, perhaps more transparently, as

$$\Pr(Q|W_{P})\Pr(P|W) \ = \ \Pr(PQP |W).$$

Thus, $PQP$ represents the “(yes,yes)”-outcome in a sequential measurement of $P$ and $Q$ (in that order).

More generally, the sequential product $a \odot b := \sqrt{a}b\sqrt{a}$ of two effects is another effect, representing the result of observing first $a$ and then $b$ in a sequential measurement (and assuming the state updates according to $W \mapsto (\textrm{Tr}(Wa))^{-1} \sqrt{a} W \sqrt{a}$ after measurement of $a$). Abstracting from this example, S. Gudder and R. J. Greechie ([2002]) defined a *sequential effect algebra* to be an effect algebra $(\mathbf{L},\oplus,0,1)$ equipped with a binary operation $\odot : \mathbf{L} \times \mathbf{L} \rightarrow \mathbf{L}$ satisfying the following conditions for all $a,b,c \in \mathbf{L}$, where $a | b$ means $a \odot b = b \odot a$:

- If $b \perp c$, then $a \circ b \perp a \circ c$ and $a \circ (b \oplus c) = (a \circ b) \oplus (a \circ c)$
- $1 \circ a = a$
- If $a \circ b = 0$, then $b \circ a = 0$
- If $a | b$ then $a | b'$, and $a \circ (b \circ c) = (a \circ b) \circ c$
- If $a | b$ and $a | c$, then (i) $a | b \circ c$ and, (ii) if $b \perp c$, $c | a \oplus b$

A remarkable recent result of J. van de Wetering ([2019]) shows that any finite-dimensional order-unit space whose order interval $[0,u]$ is an SEA under a binary operation continuous in the first variable, is a euclidean (equivalently, formally real) Jordan algebra in a natural way.[^note-22]

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=qt-quantlog). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/qt-quantlog/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=qt-quantlog&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/qt-quantlog/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- Cabello, Adan, 2012, “[Specker’s fundamental principle of quantum mechanics](https://arxiv.org/abs/1212.1756)”, unpublished paper, available at arXiv.org
- Hardy, Lucien, 2001, “[Quantum Theory from Five Reasonable Axioms](https://arxiv.org/abs/quant-ph/0101012)”, unpublished paper, available at arXiv.org
- Henson, Joe, 2012, “[Quantum contextuality from a simple principle?](https://arxiv.org/abs/1210.5978)”, unpublished manuscript, available at arXiv.org

## Related Entries

Bell’s Theorem | quantum mechanics | quantum mechanics: Kochen-Specker theorem | quantum mechanics: modal interpretations of | quantum theory: and mathematical rigor

## Notes（原文脚注）

[^note-1]: A few qualifications are in order already: In a more general formulation, one considers the lattice of projections of a von Neumann algebra. Only in the context of non-relativistic quantum mechanics, and then only absent superselection rules, is this algebra a type I factor. For the expository purposes of this paper, we restrict our discussion to this context.

[^note-2]: Throughout this paper, I use the term “logic” rather narrowly to refer to the algebraic and order-theoretic aspect of propositional logic. There exists a substantial technical literature devoted to non-classical formal deductive systems that are intended to stand to quantum propositional logics rather as classical deductive systems stand to Boolean algebras. A good reference for this material is Kalmbach 1983.

[^note-3]: It is important to note here that even in classical mechanics, only subsets of the state-space that are measurable (in the sense of measure theory) are regarded as representing observable properties of the system, and only these are assigned probabilities. The difference is that in the classical case, the observable properties form a sub-Boolean algebra of the power set of $S$, while in the quantum case, they do not.

[^note-4]: For a recent, and particularly sharp, critique of Putnam’s proposal, see Maudlin 2005. A more slightly more sympathetic treatment is given by Bacciagaluppi (2009)[^bacciagaluppi-2009], who suggests that one’s attitude towards the kind of revision of logic Putnam proposes will be bound up with one’s preferences regarding a physical interpretation of quantum mechanics. In particular, Bacciagaluppi suggests that the Everett interpretation that consistent with something resembling Putnam’s thesis.

[^note-5]: The first explicit formulation of this interpretation seems to have been given by Jauch and Piron (1969).

[^note-6]: So-called *modal* interpretations of quantum mechanics do not attempt to assign actual values (or ranges of values) to *all* observables. Rather, they identify (in various different ways) a privileged observable or class of observables as having “definite values”, and thereby avoid the various no-go theorems for hidden variables. For references and further details, see the entry on modal interpretations of quantum mechanics.

[^note-7]: Of course, another possible response to such a question is to dismiss it, perhaps with the observation that mathematical models of natural phenomena evolve, more or less organically, to fit the facts, and require no a priori justification. Or, to put it differently, we can insist that quantum logic has the structure that it does just because the *world* has that structure.

[^note-8]: These include, besides Mackey’s original formalism, that of Piron (1976)[^piron-1976], the approach based on partial Boolean algebras of Kochen and Specker (1965, 1967), and various approaches emphasizing the convex structure of the set of (statistical) states of a system, e.g., Holevo 1982, Ludwig 1983, Pitowsky 1989.

[^note-9]: Even at this point, a couple of remarks are in order. First, notice that $E$ need not be the set of outcomes of any humanly executable, let alone repeatable, measurement or experiment. Any exhaustive set of mutually exclusive alternatives will serve, at least as long as some sense can be attached to the terms “occurrence” and “realization” (even as terms of art). Secondly, notice that every standard interpretation of probability theory, whether relative-frequentist, propensity, subjective or what-have-you, represents probability weights mathematically in the same way.  Thus, the framework just sketched is agnostic among these interpretations.

[^note-10]: It is worth remarking that all approaches to a generalized probability theory contain some mechanism for identifying outcomes of distinct measurements or values of distinct observables, though this mechanism varies from author to author . The most common approaches are to identify outcomes that are equi-probable in every state (as in the work of Mackey), or to identify outcomes that are certain (i.e., have probability 1) in exactly the same states (as in the work of Piron). Both of these prescriptions become problematic in the context of sequential measurements—see, e.g., Cooke and Hilgevoord 1981. The Foulis-Randall theory has the advantage of remaining neutral as to the precise mechanism whereby outcomes are identified.

[^note-11]: It is easy to see that this condition, which is sometimes used as the definition of algebraicity, implies algebraicity as we have defined it. For the converse, we argue as follows. Let $A, B, C$ be events of an algebraic test space $\mathcal{A}$, with $A \sim B$ and $C$ complementary to $B$. Then, because $\mathcal{A}$ is algebraic, $A\binbot C$, and so $A\cup C$ is an event. To show that $C$ is complementary to $A$, we need to show that $A\cup C$ is a test. To do this, let $D$ be complementary to $A\cup C$. Then $C\cup D$ is complementary to $A$, and, since $A \sim B$ , we have $(C\cup D)\binbot B$. But then $B\cup C\cup D$ is an event, containing the test $B\cup C$.

In an algebraic test space, tests are maximal events; that is, a test has no non-empty complement. If $E$ and $F$ are tests and $E\subseteq F$, then we have $F \sim E$ (since the empty set is a common complement of $F$ and $E$); since $E\binbot(F / E)$, we have $F\binbot(F / E)$ as well, and so $(F / E)$ is empty, and $F = E$.

It follows that $D$ is empty, whence $A\cup C$ is a test.

[^note-12]: Cabello (2012, Other Internet Resources) attributes to Ernst Specker the following comment: “Do you know what, according to me, is the fundamental theorem of quantum mechanics? (…) That is, if you have several questions and you can answer any two of them, then you can also answer all of them.” This is exactly regularity. As Harding’s results show, it is very far from uniquely quantum-mechanical. On the other hand, regularity, and even orthocoherence, are strong constraints on a probabilistic model. For instance, it is pointed out in Henson 2012 (Other Internet Resources) that orthocoherence enforces the quantum-mechanical upper-bound on the so-called “KCBS” parameter, one proposed measure of the degree to which a probabilistic model is contextual. Othocoherent probabilistic models, then, cannot be, by this measure, more “non-contextual” than allowed by quantum mechanics.

[^note-13]: The approach taken here is modeled on, but somewhat less general than, that of Foulis, Piron and Randall (1983)[^randall-1983]. See also Randall and Foulis (1985).

[^note-14]: Indeed, the pair $(S, F)$ is an *adjunction* between $\wp(X)$ and $\wp(\Delta)$—that is, for any $\Gamma \in \wp(\Delta)$ and any $J \in \wp(X)$, we have $S(\Gamma) \subseteq J$ if and only if $\Gamma \subseteq F(J)$. It follows that the mappings

$$\Gamma \rightarrow F(S(\Gamma)) \textrm{ and }J \rightarrow S(F(J))$$

are respectively a closure operator on $\wp(\Delta)$ and an interior operator on $\wp(X)$. The collection of closed subsets of $\Delta$ and the collection of open subsets of $X$ (which are exactly the ranges of the mappings $F$ and $S)$ are complete lattices, closed under intersection and union respectively, and are mapped isomorphically onto one another by $S$ and $F$. (See the supplement on ordering relations for further details.)

[^note-15]: In the case where $\Delta$ is a *convex* set of states the closed subsets of $\Delta$ are *faces* of $\Delta$; that is, $F(J)$ is itself convex, and if a convex combination of states lies in $F(J)$, then those states themselves lie in $F(J)$. The faces of any convex set $\Delta$, ordered by inclusion, form a complete lattice, closed under intersection. Thus, in this context, the property lattice is a complete sublattice of the face lattice of the state-space. This is the starting point for a number of approaches to generalized probability theory. Note that if $\Delta$ is a simplex, as it is for classical models, then the face lattice of $\Delta$ is a Boolean algebra.

[^note-16]: This condition fails for the projection lattice modeling a quantum-mechanical system with superselection rules, but continues to hold for the lattices associated with each superselection sector.

[^note-17]: The first such examples were obtained by H. Keller. Recently, M. P. Soler has shown that if a generalized Hilbert space contains any infinite orthonormal set, it must in fact be a classical Hilbert space—i.e., the division ring D must be the field of real numbers, the field of complex numbers, or the ring of quaternions. See Holland 1995 for references and further discussion. For an interesting recent attempt to motivate the hypothesis of Soler’s theorem, see Pitowsky 2006.

[^note-18]: For a development of this idea in a more general context, see Wilce 2000a.

[^note-19]: Interesting work of Meyer (1999)[^meyer-1999] and Clifton & Kent (2000) shows that the quantum test space $F(\mathbf{H})$ contains a dense semi-classical sub-test space. A detailed hidden-variables model along these lines has not been seriously entertained (and would presumably be otherwise problematic), but these results do suggest that experiments having finite precision can not rule out non-contextual hidden variables.

[^note-20]: Essentially equivalent structures called *weak orthoalgebras* had earlier been introduced by R. Giuntini and H. Grueling [1989]. Also equivalent are the *D-posets* of Kopka and Chovanec [1994].

[^note-21]: In fact, $[0,1]^{E}$ is also an example of an MV algebra, a class of algebraic structures providing the standard semantics for Lukasiewicz’s multivalued logic. MV algebras are provably the same thing as lattice-ordered effect algebras. See Kopka and Chovanec [1994] or Foulis [2000].

[^note-22]: In fact, de Wetering’s result does not require part (i) of condition (d).

[^abramsky-2009]: Abramsky, Samson and Bob Coecke, 2009, “Categorical Quantum Mechanics”, in Engesser, Gabbay, and Lehmann 2009: 261–323. doi:10.1016/B978-0-444-52869-8.50010-4

[^aerts-1981]: Aerts, Diederik, 1981, *The One and the Many: Towards a Unification of the Quantum and Classical Description of One and Many Physical Entities*, Ph.D. Dissertation, Free University of Brussels.

[^amemiya-1966]: Amemiya, Ichiro and Huzihiro Aaraki, 1966, “A Remark on Piron’s Paper”, *Publications of the Research Institute for Mathematical Sciences* (Series A), 2(3): 423–427. doi:10.2977/prims/1195195769

[^baez-2006]: Baez, John, 2006, “Quantum Quandaries: a Category-Theoretic Perspective”, in Steven French, Dean Rickles, and Juha Saatsi (eds), *Structural Foundations of Quantum Gravity*, Oxford: Oxford University Press, 240-265. doi:10.1093/acprof:oso/9780199269693.003.0008.

[^bacciagaluppi-2009]: Bacciagaluppi, Guido, 2009, “Is Logic Empirical?” in Engesser, Gabbay, and Lehmann 2009: 49–78. doi:10.1016/B978-0-444-52869-8.50006-2

[^baltag-2005]: Baltag, A. and S. Smets, 2005, “Complete Axiomatizations for Quantum Actions”, *International Journal of Theoretical Physics*, 44(12): 2267–2282. doi:10.1007/s10773-005-8022-2

[^beltrametti-1981]: Beltrametti, Enrico G. and Gianni Cassinelli, 1981, *The Logic of Quantum Mechanics* (Encyclopedia of Mathematics and its Applications, Volume 15), Reading, MA: Addison-Wesley.

[^birkhoff-1967]: Birkhoff, Garrett, 1967, *Lattice Theory*, Providence: American Mathematical Society.

[^birkhoff-1936]: Birkhoff, Garrett and John von Neumann, 1936, “The Logic of Quantum Mechanics”, *Annals of Mathematics*, 37(4): 823–843. doi:10.2307/1968621

[^chiribella-2011]: Chiribella, Giulio, Giacomo Mauro D’Ariano, and Paolo Perinotti, 2011, “Informational Derivation of Quantum Theory”, *Physical Review A*, 84(1): 012311. doi:10.1103/PhysRevA.84.012311

[^clifton-2000]: Clifton, Rob and Adrian Kent, 2000, “Simulating Quantum Mechanics by Non-Contextual Hidden Variables”, *Proceedings of the Royal Society A*, 456: 2101–2114. doi:10.1098/rspa.2000.0604

[^coecke-2011]: Coecke, Bob, 2011, “A Universe of Processes and Some of Its Guises”, in Hans Halvorson (ed.), *Deep Beauty: Understanding the Quantum World Through Mathematical Innovation*, Cambridge: Cambridge University Press, pp. 129–186.

[^cohen-1987]: Cohen, David W. and George Svetlichny, 1987, “Minimal Supports in Quantum Logics”, *International Journal of Theoretical Physics*, 26(5): 435–450. doi:10.1007/BF00668776

[^cooke-1981]: Cooke, Roger M. and J. Hilgevoord, 1981, “A New Approach to Equivalence in Quantum Logic”, in Enrico G. Beltrammetti and Bas C. van Fraassen (eds.) *Current Issues in Quantum Logic*, New York: Plenum, pp. 101–113. doi:10.1007/978-1-4613-3228-2_7

[^dakic-2011]: Dakic, Borivoje, and Caslav Brukner, 2011, “Quantum Theory and Beyond: Is Entanglement Special?”, in Hans Halvorson (ed.), *Deep Beauty: Understanding the Quantum World Through Mathematical Innovation*, Cambridge: Cambridge University Press, pp. 129–186. doi:10.1017/CBO9780511976971.011

[^davey-1990]: Davey, B.A. and H.A. Priestley, 1990, *Introduction to Lattices and Order*, Cambridge: Cambridge University Press.

[^engesser-2009]: Engesser, Kurt, Dov M. Gabbay, and Daniel Lehmann (eds), 2009, *Handbook of Quantum Logic and Quantum Structures*, Amsterdam: North-Holland.

[^fine-1973]: Fine, Arthur, 1973, “Probability and the Interpretation of Quantum Mechanics”, *British Journal for the Philosophy of Science*, 24(1): 1–37. doi:10.1093/bjps/24.1.1

[^foulis-2000]: Foulis, D. J., 2000, “MV and Heyting effect algebras”, *Foundations of Physics*, 30: 1687–1706.

[^foulis-1994]: Foulis, D. J., and M. K. Bennett, 1994, “Effect algebras and unsharp quantum logics”, *Foundations of Physics*, 24: 1331–1352. doi:10.1007/BF02283036

[^foulis-1992]: Foulis, D.J., R. Greechie, and G.T. Rüttimann, 1992, “Filters and Supports in Orthoalgebras”, *International Journal of Theoretical Physics*, 31(5): 789–807. doi:10.1007/BF00678545

[^foulis-1983]: Foulis, D.J., C. Piron, and C.H. Randall, 1983, “Realism, Operationalism and Quantum Mechanics”, *Foundations of Physics*, 13(8): 813–841. doi:10.1007/BF01906271

[^foulis-1981a]: Foulis, D.J. and C.H. Randall, 1981a, “Empirical Logic and Tensor Products”, in Holger Neumann (ed), *Interpretations and Foundations of Quantum Mechanics: Proceedings of a Conference Hold [sic] in Marburg, 28–30 May 1979* (Grundlagen der exakten Naturwissenschaften, volume 5), Mannheim: Wissenchaftsverlag, pp. 9–20.

[^foulis-1981b]: –––, 1981b, “What Are Quantum Logics and What Ought They to Be?”, in Enrico G. Beltrametti and Bas C. van Fraassen (eds), *Current Issues in Quantum Logic*, New York: Plenum, pp. 35–52. doi:10.1007/978-1-4613-3228-2_3

[^foulis-1984]: –––, 1984, “Stochastic Entities” in P. Mittelstaedt and E. Stachow (eds.), *Recent Developments in Quantum Logic*, Mannheim: B.I. Wissenschaft.

[^giuntini-1989]: Giuntini, Roberto, and Hans Greuling, 1989, “Toward a formal language for unsharp properties”, *Foundations of Physics*, 20: 931–395.

[^gleason-1957]: Gleason, Andrew M., 1957, “Measures on the Closed Subspaces of a Hilbert Space”, *Journal of Mathematics and Mechanics*, 6(6): 885–893.

[^grätzer-1998]: Grätzer, George, 1998, *General Lattice Theory*, Basel: Birkhäuser Verlag (2nd edition).

[^golfin-1988]: Golfin, Andrew S., Jr., 1988, *Representations of Complete Lattices*, Ph. D. Dissertation, University of Massachusetts, Amherst.

[^gudder-1970]: Gudder, Stanley P., 1970, “On Hidden-Variable Theories”, *Journal of Mathematical Physics*, 11(2): 431–436. doi:10.1063/1.1665156

[^gudder-1989]: –––, 1989, *Quantum Probability Theory*, San Diego: Academic Press.

[^gudder-2002]: Gudder, Stan, and Richard Greechie, 2002, “Sequential products on effect algebras”, *Reports on Mathematical Physics*, 49(1): 87–111. doi:10.1016/S0034-4877(02)80007-6

[^guz-1978]: Guz, Wawrzyniec, 1978, “Filter Theory and Covering Law”, *Annales de l’Institut Henri Poincaré. Section A, Physique Théorique*, 29(4): 357–378. [[Guz 1978 available online](http://www.numdam.org/item?id=AIHPA_1978__29_4_357_0)]

[^harding-1996]: Harding, John, 1996, “Decompositions in Quantum Logic”, *Transactions of the American Mathematical Society*, 348(5): 1839–1862. doi:10.1090/S0002-9947-96-01548-6

[^harding-1998]: –––, 1998, “Regularity in Quantum Logic”, *International Journal of Theoretical Physics*, 37(4): 1173–1212. doi:10.1023/A:1026665818335

[^harding-2009]: –––, 2009, “A Link Between Quantum Logic and Categorical Quantum Mechanics”, *International Journal of Theoretical Physics*, 48(3): 769–802. doi:10.1007/s10773-008-9853-4

[^holevo-1982]: Holevo, Alexander S., 1982, *Probabilistic and Statistical Aspects of Quantum Theory*, Amsterdam: North Holland.

[^holland-1995]: Holland, Samuel S. Jr., 1995, “Quantum mechanics in Hilbert space: A result of M.P. Soler”, *Bulletin of the American Mathematical Society*, 32(2): 205–232. doi:10.1090/S0273-0979-1995-00593-8

[^ischi-2000]: Ischi, Boris, 2000, “Endomorphisms of the Separated Product of Lattices”, *International Journal of Theoretical Physics*, 39(11): 2559–2581. doi:10.1023/A:1026405608135

[^jauch-1969]: Jauch, J.M. and C. Piron, 1969, “On the Structure of Quantal Propositional Systems”, *Helvetica Physica Acta*, 42(6): 842–848. doi:10.5169/seals-114098

[^kalmbach-1983]: Kalmbach, Gudrun, 1983, *Orthomodular Lattices*, London: Academic Press.

[^kläy-1988]: Kläy, Matthias P., 1988, “Einstein-Podolsky-Rosen Experiments: The Structure of the Sample Space I, IIç”, *Foundations of Physics Letters*, 1(3): 205–244. doi:10.1007/BF00690066

[^kochen-1965]: Kochen, Simon and E.P. Specker, 1965, “Logical structures arising in quantum theory”, *Symposium on the Theory of Models: Proceedings of the 1963 International Symposium [on the Theory of Models, Held] at Berkeley, [from June 25 to July 11 1963]*, J.W. Addison, Leon Henkin, and Alfred Tarski (eds), Amsterdam: North-Holland, pp. 177–189.

[^kochen-1967]: –––, 1967, “The Problem of Hidden Variables in Quantum Mechanics” *Journal of Mathematics and Mechanics*, 17: 59–87.

[^kôpka-1994]: Kôpka, František, and Ferdinand Chovanec, 1994, “D-posets”, *Mathematica Slovaca*, 44: 21–34.

[^ludwig-1983]: Ludwig, Günther, 1983, *Foundations of Quantum Mechanics I*, New York: Springer-Verlag.

[^mackey-1957]: Mackey, George W., 1957, “Quantum Mechanics and Hilbert Space”, *The American Mathematical Monthly*, 64(8): 45–57. doi:10.2307/2308516

[^mackey-1963]: –––, 1963, *The Mathematical Foundations of Quantum Mechanics: A Lecture-note Volume*, New York: W.A. Benjamin.

[^maudlin-2005]: Maudlin, Tim, 2005, “The Tale of Quantum Logic”, in Yemima Ben-Menahem (ed.), *Hilary Putnam*, Cambridge: Cambridge University Press, pp. 156–187. doi:10.1017/CBO9780511614187.006

[^massanes-2011]: Massanes, Lluis, and Markus Mueller, 2011, “A Derivation of Quantum Theory from Physical Requirements”, *New Journal of Physics*, 13: 063001. doi:10.1088/1367-2630/13/6/063001

[^meyer-1999]: Meyer, David A., 1999, “Finite Precision Measurement Nullifies the Kochen-Specker Theorem”, *Physical Review Letters*, 83(19): 3751–54. doi:10.1103/PhysRevLett.83.3751

[^piron-1964]: Piron, C., 1964, “Axiomatique Quantique”, *Helvetica Physica Acta*, 37(4–5): 439–468. doi:10.5169/seals-113494

[^piron-1976]: –––, 1976, *Foundations of Quantum Physics*, Reading, MA: W.A. Benjamin.

[^pitowsky-1989]: Pitowsky, Itamar, 1989, *Quantum Probability—Quantum Logic* (Lecture Notes in Physics, volume 321), Berlin: Springer-Verlag.

[^pitowsky-2006]: –––, 2006, “Quantum Mechanics as a Theory of Probability”, in William Demopoulos and Itamar Pitowsky (eds.) *Physical Theory and Its Interpretation: Essays in Honor of Jeffrey Bub*, Dordrecht: Springer, pp. 213–240. doi:10.1007/1-4020-4876-9_10

[^putnam-1968]: Putnam, Hilary, 1968, “Is Logic Empirical?” in R. Cohen and M.P. Wartofski (eds.), *Boston Studies in the Philosophy of Science* (Volume 5), Dordrecht: D. Reidel; reprinted as “The Logic of Quantum Mechanics” in Hilary Putnam, *Mathematics, Matter and Method*, Cambridge University Press, 1976, second edition 1979, pp. 174–197. doi:10.1017/CBO9780511625268.012

[^rau-2009]: Rau, Jochen, 2009, “On Quantum vs Classical Probability”, *Annals of Physics*, 324(12): 2622–2637. doi:10.1016/j.aop.2009.09.013

[^randall-1983]: Randall, C.H. and D.J. Foulis, 1983, “Properties and Operational Propositions in Quantum Mechanics”, *Foundations of Physics*, 13(8): 843–863. doi:10.1007/BF01906272

[^randall-1985]: Randall, C.H. and D.J. Foulis, 1985, “Stochastic Entities”, in *Recent Developments in Quantum Logic*, P. Mittelstaedt and E. Stachow (eds.), Mannheim: Bibliographisches Institut, pp. 265–284.

[^selinger-2007]: Selinger, Peter, 2007, “Dagger Compact Closed Categories and Completely Positive Maps” (Extended Abstract), *Proceedings of the 3rd International Workshop on Quantum Programming Languages* (QPL 2005), Chicago. *Electronic Notes in Theoretical Computer Science*, 170: 139–163. doi:10.1016/j.entcs.2006.12.018

[^fraassen-1992]: van Fraassen, Bas C., 1992, *Quantum Mechanics: An Empiricist View*, Oxford: Oxford University Press.

[^varadarajan-1985]: Varadarajan, Veeravalli Sesshadri, 1985, *Geometry of Quantum Mechanics*, New York: Springer-Verlag. doi:10.1007/978-0-387-49386-2

[^neumann-1932]: von Neumann, John, 1932, *Mathematische Grundlagen der Quantenmechanik*, Berlin: Springer-Verlag; English translation: *Mathematical Foundations of Quantum Mechanics*, Princeton: Princeton University Press, 1955.

[^wetering-2019]: de Wetering, John, 2019, “Sequential Product Spaces are Jordan Algebras”, *Journal of Mathematical Physics*, 60(6): 062201. doi:10.1063/1.5093504

[^wilce-1992]: Wilce, Alexander, 1992, “Tensor Products in Generalized Measure Theory”, *International Journal of Theoretical Physics*, 31(11): 1915–1928. doi:10.1007/BF00671964

[^wilce-2000a]: –––, 2000a, “Generalized Sasaki Projections”, *International Journal of Theoretical Physics*, 39: 969–974. doi:10.1023/A:1003607820078

[^wilce-2000b]: –––, 2000b, “Test Spaces and Orthoalgebras”, in Bob Coecke, David Moore, and Alexander Wilce (eds), *Current Research in Operational Quantum Logic*, Dordrecht: Kluwer Academic Publishers, pp. 81–114. doi:10.1007/978-94-017-1201-9_4

[^wilce-2009]: –––, 2009, “Test spaces”, Engesser, Gabbay, and Lehmann 2009: 443–549. doi:10.1016/B978-0-444-52869-8.50014-1

[^wilce-2018]: –––, 2018, “A Royal Road to Quantum Theory (or Thereabouts)”, *Entropy*, 20(4): 227 doi:10.3390/e20040227

[^wright-1980]: Wright, Ron, 1980, “The State of the Pentagon: A Nonclassical Example”, in A.R. Marlowe (ed.), *Mathematical Foundations of Quantum Physics*, New York: Academic Press, pp. 255–274. doi:10.1016/B978-0-12-473250-6.50015-7

[^younce-1987]: Younce, Matthew B., 1987, *Random Variables on Non-Boolean Structures*, Ph.D. Dissertation, Department of Mathematics, University of Massachusetts/Amherst.
