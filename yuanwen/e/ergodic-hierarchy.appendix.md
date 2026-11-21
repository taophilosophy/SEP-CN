# ergodic-hierarchy — appendix（supplement）

> （《ergodic-hierarchy》词条补充材料，源：plato.stanford.edu/entries/ergodic-hierarchy/appendix.html）

#### Supplement to The Ergodic Hierarchy

## Appendix

### A. The Conceptual Roots of Ergodic Theory

The notion of an abstract dynamical system is both concise and effective. It focuses on certain structural and dynamical features that are deemed essential to understanding the nature of the seemingly random behaviour of deterministically evolving physical systems. The selected features were carefully integrated, and the end result is a mathematical construct that has proven to be very effective in revealing deep insights that would otherwise have gone unnoticed. This brief note will provide some understanding of the key developments that served to influence the choice of features involved in constructing this concept.

One key development in the early history of mechanics was the realization of the need to settle on a set of fundamental quantities. For example, Descartes regarded volume and speed as fundamental; whereas, Newton regarded mass and velocity as such. Those quantities were then respectively used by each of them to define other important quantities, such as the notion of quantity of motion. Descartes defined it as size (volume) times speed (Descartes 1644, paragraph 2.36); whereas, Newton defined it as mass times velocity (Newton 1687, p 1). (See Cohen 1966 for further discussion of the two views and the historical relationship between them; also, see Dijksterhuis 1986 for discussion of them in a broader historical context.) Both Descartes and Newton regarded a force as that which brings about a change in the quantity of motion; compare Descartes third law of motion (Descartes 1644, paragraph 2.40), and Newton’s second law of motion (Newton 1687, p. 13). However, these are quite distinct notions, and one has deeper ontological significance and substantially greater utility than the other. In Garber 1992, there is an excellent discussion of some of the shortcomings of Descartes’ physics.

Although Newton’s notion of force is extremely effective, questions arose as to whether it is the most fundamental dynamical notion on which mechanics is to be based. Eventually, it was realized that the notion of energy is more fundamental than the notion of force. Both are derived notions, meaning that they are defined in terms of fundamental quantities. The crucial question is how to distinguish the derived quantities that are the most fundamental, or at least more fundamental than the others. The answer to that question is far from straightforward. Sometimes such determinations are made on the basis of principles (such as the principle of virtual work or the principle of least action), or because they prove more useful than others in solving problems or in providing deeper insight. In the history of mechanics, it was eventually realized that it is best to adopt Hamilton’s formulation of mechanics rather than Newton’s; see Dugas 1988 for further discussion of the development of mechanics after Newton. In Hamilton’s formulation, the fundamental equations of motion are defined in terms of the total energy (kinetic plus potential energies) of a system, by contrast with the Newtonian formulation, which define them in terms of the sum of the total forces acting on the system. A number of deeply important insights result from that choice, and some of those are crucial for understanding and appreciating the elegant conciseness of the notion of an abstract dynamical system.

One key innovation of Hamilton’s approach is the use of phase space, a 6N dimensional mathematical space, where N is the number of particles constituting the system of interest. The 6N dimensions are constituted by 3 spatial coordinates per particle and one “generalized” momentum coordinate per spatial coordinate. For a single simple system (such as a particle representing a molecule of a gas) the phase space has 6 dimensions. Each point $x$ in phase space represents a possible physical state (also known as a phase) of the classical dynamical system; it is uniquely specified by an ordered list of 6 (more generally, 6N for an N particle system) numerical values, meaning a 6 dimensional vector. Once the state is known, other properties of the system can be determined; each property corresponds to a mathematical function of the state (onto the set of possible property values). The time evolution of the state of a system (and so of its properties) is governed by a special function, the *Hamiltonian*, which can be determined in many cases from the forces that act on the system (and in other ways). The Hamiltonian specifies the transformation of the state of the system over time by way of Hamilton’s equations of motion, which is a close analogue to Newton’s equation, force equals mass time acceleration. It should perhaps be emphasized that the two formulations of classical mechanics are not completely equivalent; that is to say, for many but not all classical systems the corresponding mathematical representations of them are inter-translatable. For further discussion, see section 1.7 of Lanczos 1986 and section 2.5.3 of Torretti 1999.

The use of Hamilton’s formulation of the equations of motion for Hamiltonians that are not explicitly time dependent leads to two immediate consequences, the conservation of energy and the preservation of phase space volumes; for more discussion, see sections 6.6 and 6.7 of Lanczos 1986. These consequences are crucial for understanding the foundations of ergodic theory. They are quite general, though not fully general since some substantial assumptions (that need not be specified here) must be made to derive them; however, a large class of important systems satisfy those assumptions. The conservation of energy means that the system is restricted to a surface of constant energy in phase space; more importantly for the foundations of ergodic theory is that most of these surfaces are (as it turns out) compact manifolds. The time evolution of a phase space volume that is restricted to a compact manifold has an invariant measure that is bounded, meaning that it can be normalized to unity.

In light of the discussion above, important conceptual ties can be made to the elements that constitute the notion of an abstract dynamical system. As noted above (in the main body of this entry), those elements are a probability space [$X,\Sigma ,\mu$] and a measure preserving transformation $T$ on $[X,\Sigma ,\mu]$. The term $X$ denotes an abstract mathematical space of points. It is the counterpart to the phase space of Hamiltonian mechanics; however, it abstracts away from the physical connections that the coordinate components have to spatial and kinematic elements (the generalized momenta) of a classical system. The term $\Sigma$ denotes a *σ*-algebra of subsets of $X$, and it is the abstract counterpart to the set of all possible phase space volumes. The classical phase space volume is an important measure, and it is replaced by $\mu$, a probability measure on $\Sigma$. The abstraction to a probability measure is ultimately related to the conservation of energy and to the resulting restriction (in many cases) of the time evolution to a compact manifold. In compact manifold cases, units may be chosen so that the total volume of the compact manifold $X$ is unity, in which case the volume measure on the set of sub-volumes (the counterpart to $\Sigma)$ is effectively a probability measure (the counterpart to $\mu)$. The phase-space-volume preserving time-evolution specified by Hamilton’s equations is replaced by the abstract notion of a probability measure preserving transformation $T$ on $X$.

To fully appreciate why the time evolution of volumes of phase space are of special interest in ergodic theory rather than points of phase space, it is necessary to relate the discussion above to developments in classical statistical mechanics. Classical statistical mechanics is typically used to model systems that consist of a large number of sub-systems, such as a volume of gas. A liter of a gas at standard temperature and pressure has on the order of $10^{20}$ molecules, which means that the corresponding phase space has $6 \times 10^{20}$ dimensions (leaving aside other features of the molecules such as their geometric structure, which is often done for the sake of simplicity). For such systems, the Hamiltonian depends on both inter-particle forces as well as external forces. As in classical mechanics, the total energy is conserved (given certain assumptions, as noted earlier) and the time evolution preserves phase space volumes.

One important innovation in classical statistical mechanics is the use of the new notion of an ensemble density. This notion goes back to Gibbs (1902), and has since been widely used, and describes the state of an ensemble. Gibbs remains non-committal about both the interpretation of the this density and its implication for a single system, but he observes that what can be said about single system on the basis of an ensemble ‘can generally be described most accurately and most simply by saying that it is one taken at random from a great number (ensemble) of bodies which are completely described’ (1902, p. 163)

A density function is a function that is normalized to unity over the relevant space of states for the system (meaning a surface of constant total energy). If $f(x)$ denotes the density function that describes the macrostate of a system, then $f(x)$ may be used to calculate the probability that the system is in a given volume $A$ of phase space by integrating the density function over the specified volume, $\int_A f(x)dx$. Such probabilities are sometimes interpreted epistemically, meaning that they represent what is known probabilistically about the microstate of the system with regards to each volume of phase space. Subsets of phase space that can be assigned a volume are known as the Lebesgue measurable sets,[^note-25] and their abstract counterpart in ergodic theory is the *σ*-algebra $\Sigma$ of subsets of $X$. The probability measure $\mu$ is the abstract counterpart to the product of the density function and the Lebesgue measure in classical statistical mechanics.

It turns out that the density function may also be used to obtain information about the average value of each physical quantity of the system with respect to any given volume of phase space. As already noted, each physical quantity of a classical system is represented by a function on phase space. Such functions are similar to density functions in that they must be Lebesgue integrable; however, they need not be normalized to unity. Suppose that $f(x)$ is the macrostate of the system. If $g(x)$ is one of its physical quantities, then $\int_A f(x)g(x)dx$ denotes the average value of $g(x)$ over phase space volume $A$.

The time evolution of an macrostate is defined in terms of the time evolution of the microstates. Suppose that $f(x)$ is the macrostate of the system for some chosen initial time, and let $T_t$ be the time evolution operator associated with the Hamiltonian for the system, which governs its time evolution from the initial time to some other time $t$. During that time interval, $f(x)$ evolves to some other density operator $f_t(x)$ since $T_t$ is measure preserving. It turns out that the time evolved state $f_t(x)$ corresponds to $T_t\,f(x)$, which is by definition equal to $f(T_t x)$. The probability that the system is in a given volume of phase space at a given time is determined by integrating the density function at the given time over the specified volume.

A brief discussion of some key developments in the foundations of statistical mechanics will serve to provide a deeper appreciation for the notion of an abstract dynamical system and its role in ergodic theory. The theory emerged as a new abstract field of mathematical physics beginning with the ergodic theorems of von Neumann and Birkhoff in the early 1930s; see Moore (2015) for a historical discussion of von Neumann’s and Birkhoff’s theorems. The theorems have their roots in Ludwig Boltzmann’s ergodic hypothesis, which was first formulated in the late 1860s (Boltzmann 1868, 1871). Boltzmann introduced the hypothesis in developing classical statistical mechanics; it was used to provide a suitable basis for identifying macroscopic quantities with statistical averages of microscopic quantities, such as the identification of gas temperature with the mean kinetic energy of the gas molecules. Although ergodic theory was inspired by developments in classical mechanics, classical statistical mechanics, and even to some extent quantum mechanics (as will be shown shortly), it became of substantial interest in its own right and developed for the most part in an autonomous manner.

Boltzmann’s hypothesis says that an isolated mechanical system, which is one in which total energy is conserved, will pass through every point that lies on the energy surface corresponding to the total energy of the system in phase space, the space of possible states of the system. Strictly speaking, the hypothesis is false; that realization came about much later with the development of measure theory. Nevertheless the hypothesis is important due in part to its conceptual connections with other key elements of classical statistical mechanics such as its role in establishing the existence and uniqueness of an equilibrium state for a given total energy, which is deemed essential for characterizing irreversibility, a central goal of the theory. It is also important because it is possible to develop a rigorous formulation that is strong enough to serve its designated role. Historians point out that Boltzmann was aware of exceptions to the hypothesis; for more on that, see von Plato 1992.

Over thirty years after Boltzmann’s formulation of the ergodic hypothesis, Henri Lebesgue provided important groundwork for a rigorous formulation of the hypothesis in his development of measure theory, which is based in his theory of integration. About thirty years after that, von Neumann developed his Hilbert space formulation of quantum mechanics, which he developed in a well known series of papers that were published between 1927 and 1929. That inspired Bernard Koopman to develop a Hilbert space formulation of classical statistical mechanics (Koopman 1931). In both cases, the formula for the time evolution of the state of a system corresponds to a unitary operator that is defined on a Hilbert space; a unitary operator is a type of measure-preserving transformation. Von Neumann then used Koopman’s innovation to prove what is known as the mean ergodic theorem (von Neumann 1932). Birkhoff then used von Neumann’s theorem as the basis of inspiration for his ergodic theorem (Birkhoff 1931). That von Neumann’s work influenced Birkhoff despite that Birkhoff’s paper was published before von Neumann’s is explained in Birkhoff and Koopman 1932. Birkhoff’s paper provides a rigorous formulation and proof of Boltzmann’s conjecture that was put forth over sixty years earlier. The key difference is that Birkhoff’s formulation is weaker than Boltzmann’s, only requiring saying that almost all solutions visit any set of positive measure in phase space in the infinite time limit. What is of particular interest here is not Birkhoff’s ergodic theorem per se, but the abstractions that inspired it and that ultimately led to the development of ergodic theory. For further discussion of the historical roots of ergodic theory, see pp. 93–114 of von Plato.

In the Koopman formulation of classical mechanics a unitary operator $T_t$ that is defined in terms of the Hamiltonian represents time evolution. It does so in its action on the state $x \in X$ of the system: If the initial state of a system is $x$, then at time $t$ its state is $T_t x$. It can be shown that the set of operators $\{T_t \mid t \in R\}$ for a given Hamiltonian constitutes a mathematical group. A set of elements $G$ with an operator $G\times G\rightarrow G$ is a group if the following three conditions are satisfied.

Associativity $A\times(B\times C) = (A\times B)\times C$ for all $A,B,C \in G$.

Identity element there is an $I \in G$ such that for all $A \in G$ we have $I\times A = A\times I = A$.

Inverse element for each $A \in G$ there is a $B \in G$ such that $A\times B = B\times A = I$.

The strategy underlying ergodic theory is to focus on simple yet relevant models to obtain deeper insights about notions that are pertinent to the foundations of statistical mechanics while avoiding unnecessary technical complications. Ergodic theory abstracts away from dynamical associations including forces, potential and kinetic energies, and the like. Continuous time evolution is often replaced with discrete counterparts to further simplify matters. In the discrete case, a continuous group $\{T_t \mid t \in R\}$ is replaced by a discrete group $\{T_n \mid n \in Z\}$ (and, as we have seen above, the evolution of $x$ over $n$ units of time corresponds to $n$ᵗʰ iterate of a map $T$: meaning that $T_n x = T^n x)$. Other advantages to the strategy include facilitating conceptual connections with other branches of theorizing and providing easier access to generality. For example, the group structure may be replaced with a semi-group, meaning that the inverse-element condition is eliminated to explore irreversible time evolution, another characteristic feature that one hopes to capture via classical statistical mechanics. This entry restricts attention to invertible maps, but the ease of generalizing to a broader range of phenomena within the framework of ergodic theory is worth noting.

### B. Measure Theory

A set $\Sigma$ is an *algebra of subsets* of $X$ if and only if the following conditions hold:

- The union of any pair of elements of $\Sigma$ is in $\Sigma$,
- the complement of each element of $\Sigma$ is in $\Sigma$, and
- the empty set $\varnothing$ is in $\Sigma$.

In other words, for every $A, B \in \Sigma$, $A \cap B \in \Sigma$ and $X - A \in \Sigma$, where $X - A$ denotes the set of all elements of $X$ that are not in $A$. An algebra $\Sigma$ of subsets of $X$ is a *σ*-algebra if and only $\Sigma$ contains every countable union of countable collections of its elements. In other words, if $\{A_i\} \subseteq \Sigma$ is countable, the countable union $\cup A_i$ is in $\Sigma$.

By definition, $\mu$ is a *probability measure* on $\Sigma$ if and only if the following conditions hold:

- $\mu$ assigns each element of $\Sigma$ a value in the unit interval,
- $\mu$ assigns 1 to $X$, and
- $\mu$ assigns the same value to the unions of finite or countable disjoint elements of $\Sigma$ that it does to the sum of the values that it assigns to those elements.

In other words, $\mu :\Sigma \rightarrow [0,1]$, $\mu(X)=1$, $\mu(\varnothing)=0$, and $\mu(\bigcup B_i)=\sum \mu(B_i)$ whenever $\{B_i\}$ is finite or countable and $B_j \cap B_k =\varnothing$ for each pair of distinct elements $B_j$ and $B_k$ of $\{B_i\}$. The probability measure $\mu$ is the abstract counterpart in ergodic theory to the density function in classical statistical mechanics.

### C. K-Systems

The standard definition of a K-system is the following (see Arnold and Avez 1968, p. 32, and Cornfeld *et al*. 1982, p. 280): A dynamical system $[X,\Sigma ,\mu]$ is a K-system if and only if there is a subalgebra $\Sigma_0 \subseteq \Sigma$ such that the following three conditions hold:

$$\tag{1} \Sigma_0 \subseteq T\Sigma_0, $$ $$\tag{2} \bigcup_{n= -\infty}^{\infty} T^n \Sigma_0 = \Sigma, $$ $$\tag{3} \bigcap_{n= -\infty}^{\infty} T^n \Sigma_0 = N, $$

In this definition, $T^n\Sigma_0$ is the sigma algebra containing the sets $T^n B (B \in \Sigma_0), N$ is the sigma algebra consisting uniquely of sets of measure one and measure zero,

$$ \bigcup_{n= -\infty}^{\infty} T^n \Sigma_0 $$

is the smallest σ*-algebra* containing all the $T^n\Sigma_0$, and

$$ \bigcap_{n= -\infty}^{\infty} T^n \Sigma_0 $$

denotes the largest subalgebra of $\Sigma$ which belongs to each $T^n\Sigma_0$.

The Kolmogorov-Sinai entropy of an automorphism $T$ is defined as follows. Let the function $z$ be:

$$ z(x) := \begin{cases} -x \log(x) &\text{ if } x \gt 0 \\ 0 &\text{ if } x = 0 \end{cases} $$

Now consider a partition *α* of the probability space $[X,B,\mu]$ and let the function $h(\alpha)$ be

$$ h(\alpha) := \sum_{i=1}^{r} z[\mu(\alpha_i)], $$

the so-called ‘entropy of the partition *α*’. Then, the *KS-entropy of the automorphism* $T$ *relative to the partition α* is defined as

$$ h(T,\alpha) := \lim_{n \rightarrow \infty}\frac{h(\alpha \cup T\alpha \cup \ldots \cup T^{n-1}\alpha)}{n} , $$

and the (non-relative) *KS-entropy* of $T$ is defined as

$$ h(T) := \sup_\alpha h(T,\alpha), $$

where the supremum ranges over all finite partitions *α* of $X$.

One can now prove the following theorem (Walters 1982, p. 108; Cornfeld *et al*. 1982, p. 283). If $[X,B,\mu]$ is a probability space and $T : X \rightarrow X$ is a measure-preserving map, then $T$ is a K-automorphism if and only if $h(T,\alpha) \gt 0$ for all finite partitions $\alpha , \alpha \ne N$, (where $N$ is a partition that consists of only sets of measure one and zero). Since the (non-relative) KS-entropy is defined as the supremum of $h(T,\alpha)$ over all finite partitions it follows immediately that a K-automorphism has positive KS-entropy; i.e., $h(T) \gt 0$ (Cornfeld *et al*., p. 283; Walters 1982, p. 109). But notice that the converse it not true: there are automorphisms with a positive KS-entropy that are not K-automorphisms.

### D. Bernoulli systems

Let $Y$ be a finite set of elements $Y = \{f_1 ,\ldots ,f_n\}$ (sometimes also called the ‘alphabet’ of the system) and let $\nu(f_i) = p_i$ be a probability measure on $Y: 0 \le p_i \le 1$ for all $1 \le i \le$ n$,$ and

$$ \sum^{n}_{i=1} = 1. $$

Furthermore, let $X$ be the direct product of infinitely many copies of $Y$:

$$ X = \prod^{+\infty}_{i=-\infty}Y_i , $$

where $Y_i = Y$ for all $i$. The elements of $X$ are doubly-infinite sequences $x = \{x_i\}^{+\infty}_{i = -\infty}$, where $x_i\in Y$ for each $i \in Z$. As the *σ*-algebra $C$ of $X$ we choose the *σ*-algebra generated by all sets of the form

$$\{x \in X \mid x_i = k, m \le i \le m+n\}$$

for all $m \in Z$, for all $n \in N$, and for all $k \in Y$ (the so-called ‘cylinder sets’). As a measure on $X$ we take the product measure

$$\prod^{+\infty}_{i=-\infty}\nu_i ,$$

that is

$$\begin{align} \mu \{x \in X &\mid x_i = k, m \le i \le m+n\} \\ &= \ldots \nu(x_{-2})\nu(x_{-1})\nu(x_0)\nu(x_1)\nu(x_2)\ldots \end{align}$$

The system is stationary if the chance element is constant in time, that is iff for all cylinder sets

$$\begin{align} \mu \{y &\mid y+1_i = w_i, m \le i \le m+n\} \\ &= \mu \{y \mid y_i = w_i, m \le i \le m+n\} \end{align}$$

holds. An invertible measure-preserving transformation $T: X \rightarrow X$, the so-called shift map, is naturally associated with every stationary stochastic process: $Tx= \{y_i\}^{+\infty}_{i = -\infty}$, where $y_i = x_{i+1}$ for all $i \in Z$. It is straightforward to see that the measure $\mu$ is invariant under $T$ (i.e., that $T$ is measure preserving) and that $T$ is invertible. This construction is commonly referred to as a ‘Bernoulli Scheme’ and denoted by ‘$B(p_1 ,\ldots ,p_n)$’. From this it follows that the quadruple $[X,C,\mu ,T]$ is a dynamical system.


## Notes（原文脚注，引自主文）

[^note-25]: 25. Not all subsets of phase space points are measurable—see (Royden 1968, pp. 52–65) for an explanation.