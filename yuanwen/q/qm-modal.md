# Modal Interpretations of Quantum Mechanics
**First published Tue Nov 12, 2002; substantive revision Mon Oct 20, 2025**

*Lombardi, Olimpia, Dieks, Dennis*

The original “modal interpretation” of non-relativistic quantum theory was born in the early 1970s, and at that time the phrase referred to a single interpretation. The phrase now encompasses a *class* of interpretations, and is best taken to refer to a general approach to the interpretation of quantum theory. We shall describe the history of modal interpretations, how the phrase has come to be used in this way, and the general program of (at least some of) those who advocate this approach.

## 1. The origin of the modal approach

In traditional approaches to quantum measurement theory a central role is played by the projection postulate, which asserts that upon measurement the state of a physical system undergoes a discontinuous change: it is projected (“collapses”) onto an eigenstate corresponding to the measurement result. This postulate leads to many difficulties: When exactly does a collapse takes place? What defines a “measurement” as opposed to an ordinary physical interaction? The postulate is especially worrying when applied to entangled compound systems whose components are well-separated in space. For example, in the Einstein-Podolsky-Rosen (EPR) experiment there are strict correlations between two systems that have interacted in the past, in spite of the fact that the correlated quantities are not sharply defined in the individual systems. The projection postulate in this case implies that the collapse resulting from a measurement on one of the systems instantaneously defines a sharp property in the distant other system. (See the discussion of the collapse or projection postulate in the entry on philosophical issues in quantum theory.)

A possible way out of these problems was noticed by van Fraassen (1972, 1974, 1991), who proposed to eliminate the projection postulate from the theory and to give a probabilistic interpretation to the remaining formalism of unitary quantum mechanics. Van Fraassen’s interpretation relied on the distinction between the “dynamical state” and the “value state” of a system at any instant:

- The *dynamical state* determines what *may be* the case: which physical properties the system may possess, and what probabilities are attached to these possibilities.
- The *value state* represents what *actually is* the case, that is, all the system’s physical properties that are sharply defined at the instant in question.

The dynamical state is the ordinary quantum state that occurs in the Schrödinger equation (in non-relativistic quantum mechanics), i. e. a vector or density matrix in Hilbert space, with the proviso that it always evolves unitarily, so never collapses.

The motivation for distinguishing between dynamical and value state is the idea that a system may have a sharp value of an observable even if its unitarily evolving state is not an eigenstate of that observable. This thought contradicts the so-called “eigenstate-eigenvalue link”, which says that a system possesses a sharp value of an observable (namely, one of its eigenvalues) if and only if its quantum state is the corresponding eigenstate. The modal approach accepts the “if” part, but denies the “only if” part of this statement. Van Fraassen accordingly introduced the notion of “value state”: a system’s physical properties (the sharply defined observables) are not one-to-one represented by the dynamical state, which occurs in the evolution equation, but by the value state, which typically differs from the dynamical state.

Van Fraassen called his proposal “modal” because it naturally connects to a modal logic of quantum propositions. Indeed, the dynamical state in general only tells us what is possible and specifies probabilities for the various possibilities. According to van Fraassen, this modal and probabilistic aspect is fundamental to quantum mechanics and should not be viewed as arising from an incompleteness of the description (see Bueno 2014 for the relation between this and van Fraassen’s constructive empiricism)[^bueno-2014].

What then are the definite quantities and value states for a given system at a given time? Empirical adequacy requires that, in cases of measurement, the after-measurement value state of the measuring device should correspond to a definite measurement result. Therefore, the scheme minimally has to generate the Born probability measure over value states that represent the possible measurement results. Van Fraassen’s interpretation did not go further than this; it did not specify precise value states outside of measurement situations and defended agnosticism about the properties of physical systems in general (see Ruetsche 1996 for critical discussion concerning this point)[^ruetsche-1996].

It is easy to see how these ideas could motivate a program for providing a more elaborate modal interpretation of quantum theory that assigns definite properties to physical systems even when no measurements are taking place. To this more general modal program we now turn.

## 2. General features of modal interpretations

In the 1980s several authors presented realist interpretations which can be regarded as variations on the just-mentioned modal themes (for an overview and references, see Dieks and Vermaas 1998)[^dieks-1998][^dieks-1998-2][^vermaas-1998]. There are differences between these modal interpretations, but all agree on the following points:

- The interpretation should be based on the standard formalism of quantum mechanics without the projection postulate: a modal interpretation is a “non-collapse interpretation”, that is, an interpretation of unitary quantum mechanics.
- The interpretation should be “realist” in the sense that it assumes that quantum systems always possess a number of definite properties, which may change with time.
- Quantum mechanics is taken to be universal: it applies both to microscopic and to macroscopic systems.
- The unitarily evolving state of the system contains information about the possible physical properties of the system and the corresponding probabilities. So, there is a probabilistic relation between the dynamical state and physical possibilities (represented by possible value states).
- A quantum measurement is an ordinary physical interaction, during which the dynamical state always evolves unitarily.

The Kochen-Specker theorem (1967) is an obstacle to any traditional realist interpretation of quantum mechanics, since it proves the impossibility of ascribing precise values to *all* physical quantities (observables) of a quantum system simultaneously, while preserving the functional relations between commuting observables. (See the entry on the Kochen-Specker theorem.) Therefore, realist non-collapse interpretations are committed to selecting a (Boolean) subset of definite-valued observables out of all observables. Each modal interpretation thus supplies a “rule of definite-value ascription” or “actualization rule”, which picks out, from the set of all the observables of a quantum system, the subset of definite-valued properties, which may change in time.

What should this actualization rule look like? In the mid-1990s a series of authors confronted this question (Clifton 1995a, 1995b, Dickson 1995a, 1995b)[^clifton-1995a][^clifton-1995b][^dickson-1995a][^dickson-1995b]. These authors proposed conditions to be satisfied by an actualization rule that defines a set of possibilities purely from the dynamical state, and concluded that the possible value states of the components of a two-part composite system should be given by the states occurring in the Schmidt (bi-orthogonal) decomposition of the dynamical state, or, equivalently, by the projectors occurring in the spectral decomposition of the density matrices representing partial systems (obtained by partial tracing) —see Section 4 for details.

The problem of definite-valued properties was approached in a more general way by Bub and Clifton (1996); for an improved version, see Bub, Clifton and Goldstein 2000). These authors started from the assumption that the definite-valued subset is determined by the dynamical state $\ket{\phi}$ *plus* a “privileged observable” $\boldsymbol{R}$, representing a property that is always definite-valued *a priori*. From this perspective, Bub (1992, 1994, 1997) drew the conclusion that with hindsight a number of traditional interpretations of quantum theory might be viewed as modal interpretations. Among them are (what Bub took to be) the Dirac-von Neumann interpretation and Bohr’s interpretation; and, as a more clear-cut case, Bohm’s theory. Indeed, this theory (Bohm 1952)[^bohm-1952] is a modal non-collapse interpretation with *position* as the privileged observable $\boldsymbol{R}$. A more recent proposal for a modal scheme using a privileged observable is the Modal-Hamiltonian interpretation (see Section 8).

## 3. Relation to other non-collapse interpretations

The proposal to do without the projection postulate was also made by others, before van Fraassen published his work. In particular, Bohm’s hidden-variables theory (itself preceded by de Broglie’s proposals from the 1920s) and Everett’s (1957) relative-state scheme (elaborated by De Witt (1970) into the many-worlds interpretation) followed this path. According to Bohm’s theory, physical systems are built up from particles that always possess definite positions, while the wave function specifies the probabilities associated with the various possible values these positions may have. There are no collapses in Bohm’s theory: the wave function evolves unitarily at all times. Therefore, the theory qualifies as a modal interpretation of quantum mechanics: the state determines a range of possible particle configurations and specifies the probabilities for these possibilities to be actually realized.

Everett (1957) also eliminated collapses, so that after a measurement object system and measuring device (or observer) end up in an entangled superposition. To reconcile this description with the uniqueness of our experience, Everett introduced the notion of *relative state*: individual terms of the superposition represent different definite measurement results, and *relative to* the corresponding device states the object systems possess definite properties as well. This interpretative move was worked out by DeWitt and others into the idea that *all* measurement results represented in the post-measurement superposition are realized: in a measurement worlds are multiplied, and in each world a different measurement outcome becomes determinate.

As a matter of historical fact, it is unclear whether this idea of many co-existing worlds accords with Everett’s own view: Everett stated that the wave function serves the purpose of providing us with a set of factual and counterfactual descriptions of the world we live in, and this suggests that he rather saw his relative-state interpretation as a theory about one single world. This would make Everett’s interpretation a modal interpretation (see for extensive discussion Dieks 2022a)[^dieks-2022a].

The feature that distinguishes modal interpretations from other non-collapse interpretations is that modal interpretations pertain to one single world, about which they make “modal statements”, i.e. statements concerning possibilities and their probabilities. Rovelli’s relational interpretation (1996) also assigns single-world properties to physical systems, in a probabilistic way, without assuming collapses. It can therefore also be considered to belong to the family of modal interpretations, in this case modal interpretations of the relational or perspectival kind, see Section 7 and (Dieks 2022b)[^dieks-2022b].

## 4. Biorthogonal-decomposition and spectral-decomposition modal interpretations

We now turn to those modal interpretations in which the set of physical possibilities is determined by the (dynamical) quantum state of a system (see the penultimate paragraph of Section 2).

In the biorthogonal-decomposition interpretation (BDMI, sometimes known as “Kochen-Dieks modal interpretation”, Kochen 1985, Dieks 1988, 1989)[^dieks-1988][^dieks-1989][^kochen-1985], the definite-valued observables are picked out by the biorthogonal (Schmidt) decomposition of the state.

**Biorthogonal Decomposition Theorem**: Given a vector $\ket{\psi}$ in a tensor-product Hilbert space $\mathcal{H}^1 \otimes \mathcal{H}^2$, there exist bases $\{\ket{a_i}\}$ and $\{\ket{p_i}\}$ for $\mathcal{H}^1$ and $\mathcal{H}^2$ respectively, such that $\ket{\psi}$ can be written as a linear combination of terms of the form $\ket{a_i} \otimes \ket{p_i}$. If the absolute values (modulus) of the coefficients in this linear combination are all unequal, then the bases are unique (see, for example, Schrödinger 1935 for a proof)[^schrödinger-1935].

Applied to quantum mechanics the theorem says that, given a composite system consisting of two subsystems, its state picks out (in many cases, uniquely) a basis for each of the subsystems. In BDMI, those bases are taken to generate the definite-valued properties of the corresponding subsystems: the definite-valued observables are those that commute with all the projections on these basis vectors.

BDMI can be applied directly to the quantum measurement problem. Let us consider an ideal measurement according to the standard von Neumann model, in which a quantum measurement is an interaction between a system $S$ and a measuring apparatus $M$. Before the interaction, $M$ is prepared in a ready-to-measure state $\ket{p_0}$, eigenvector of the pointer observable $P$ of $M$, and the state of $S$ is a superposition of the eigenstates $\ket{a_i}$ of an observable $A$ of $S$. The interaction introduces a correlation between the eigenstates $\ket{a_i}$ of $A$ and the eigenstates $\ket{p_i}$ of $P$:

$$ \ket{\psi_0} = \sum_{i} c_i \ket{a_i} \otimes \ket{p_0} \rightarrow \ket{\psi} = \sum_i c_i \ket{a_i} \otimes \ket{p_i} $$

In this case, according to the BDMI actualization rule, the preferred context of the measured object system $S$ is defined by the set $\{\ket{a_i}\}$ and the preferred context of the measuring apparatus $M$ is defined by the set $\{\ket{p_i}\}$. Therefore, the pointer position is a definite-valued property of the apparatus: as a result of the interaction with the object system the pointer acquires one of its possible values (eigenvalues) $p_i$. Likewise, after the interaction the measured observable is a definite-valued property of the object system, and acquires one of its possible values (eigenvalues) $a_i$.

In spite of the fact that this modal interpretation is characterized by the central role played by biorthogonal decomposition, two different versions can be distinguished. One of them adopts a metaphysics in which all properties are relational and, as a consequence, the fact that the application of the interpretation is restricted to subsystems of a two-component compound system is not a problem (Kochen 1985)[^kochen-1985]. This relation has been called “witnessing”: properties are not possessed by the system absolutely, but only when it is “witnessed” by another system. Consider the measurement described above: the pointer “witnesses” the value acquired by the measured observable of the measured system.

By contrast, according to the other version the properties ascribed to the system do not have a relational character. This proposal therefore faces consistency questions about the assignments of definite values to observables according to different ways of splitting up the total system into components. Consider, for example, the three-component composite system $\alpha \beta \chi$. We could apply the biorthogonal decomposition theorem to the two-component system (i) $\alpha(\beta \chi)$, or (ii) $\beta(\chi \alpha)$ or (iii) $\chi(\alpha \beta)$. Suppose that, as a result of this, in case (i) the system $\alpha$ has the definite-valued property $P$, in case (ii) the system $\beta$ has the definite-valued property $Q$, and in case (iii) the system $\alpha \beta$ has the definite-valued property $R$. How do the definite-valued properties of $\alpha$ and $\beta$ relate to those of $\alpha \beta$? Are the definite-values properties of system $\alpha \beta$ $P \amp Q$, or $R$, or both?

A generalization is the spectral-decomposition modal interpretation (SDMI, Vermaas and Dieks 1995)[^vermaas-1995]. SDMI is based on the spectral decomposition of the reduced density operator: the definite-valued properties $\Pi_i$ of a system and their corresponding probabilities $\mathrm{Pr}_i$ are given by the non-zero diagonal elements of the spectral decomposition of the system’s state,

$$ \varrho = \sum_{i} \alpha_i\Pi_i \qquad \mathrm{Pr}_i = \mathrm{Tr}(\varrho \Pi_i) $$

This new proposal matches the old one in cases where the old one applies, and generalizes it by fixing the definite-valued properties in terms of multi-dimensional projectors when the biorthogonal decomposition is degenerate: definite-valued properties need not always be represented by one-dimensional vectors—higher-dimensional subspaces of the Hilbert space can also occur.

The SDMI also has a direct application to the measurement situation. Consider quantum measurement as described above, where the reduced states of the measured system $S$ and the measuring apparatus $M$ are

$$\begin{align*} \varrho_r^S &= \mathrm{Tr}_{(M)} \ket{\psi} \bra{\psi} = \sum_i \norm{c_i}^2 \ket{a_i} \bra{a_i} = \sum_i \norm{c_i}^2 \Pi_i^a \\ \varrho_r^M &= \mathrm{Tr}_{(S)}\ket{\psi}\bra{\psi} = \sum_i \norm{c_i}^2 \ket{p_i} \bra{p_i} = \sum_i \norm{c_i}^2 \Pi_i^p \end{align*}$$

According to SDMI, the preferred context of $S$ is defined by the projectors $\Pi_i^a$ and the preferred context of $M$ is defined by the projectors $\Pi_i^p$. Therefore, also in SDMI, the observables $A$ of $S$ and $P$ of $M$ acquire actual definite values, whose probabilities are given by the diagonal elements of the diagonalized reduced states.

Healey (1989), who was among the first to make use of the biorthogonal decomposition theorem for interpretational purposes, has proposed a somewhat different modal scheme. After using the biorthogonal decomposition theorem, Healey modifies the set of possible properties in order to fulfill a variety of additional desiderata, e.g. pertaining to the relationship between composite systems and their subsystems. The structure of definite-valued properties that emerges from these conditions is rather complicated. Some progress has been made since Healey’s book was published (see Reeder and Clifton 1995)[^reeder-1995] but, in general, it remains difficult to see what the set of definite-valued properties is according to this approach.

## 5. Property composition and atomic modal interpretation

The modal property attributions as reviewed above raise consistency questions when a system can be split up into components in different ways. Consider, for example, the three-component composite system $\alpha \beta \chi$. We could apply the biorthogonal decomposition theorem to the two-component system (i) $\alpha(\beta \chi)$, or (ii) $\beta(\chi \alpha)$, or (iii) $\chi(\alpha \beta)$. Suppose that, as a result of this, in case (i) the system $\alpha$ has the definite-valued property $P$, in case (ii) the system $\beta$ has the definite-valued property $Q$, and in case (iii) the system $\alpha \beta$ has the definite-valued property $R$. How do the definite-valued properties of $\alpha$ and $\beta$ relate to those of $\alpha \beta$? Are the definite-values properties of system $\alpha \beta$ $P \amp Q$, or $R$, or both? This problem was addressed by different authors during the 1990s (see Vermaas 1999, Bacciagaluppi 1996)[^bacciagaluppi-1996][^bacciagaluppi-1996-2][^vermaas-1996][^vermaas-1999].

Elaborating on this, let us take a composite system $\alpha \beta$, whose component subsystems $\alpha$ and $\beta$ are represented by the Hilbert spaces $\mathcal{H}^{\alpha}$ and $\mathcal{H}^{\beta}$, respectively, and consider a property represented by the projector $\Pi^{\alpha}$ defined on $\mathcal{H}^{\alpha}$. It is usual to assume that $\Pi^{\alpha}$ represents the same property as that represented by $\Pi^{\alpha} \otimes I^{\beta}$ defined on $\mathcal{H}^{\alpha} \otimes \mathcal{H}^{\beta}$, where $I^{\beta}$ is the identity operator on $\mathcal{H}^{\beta}$. This assumption is based on the observational indistinguishability of the magnitudes represented by $\Pi^{\alpha}$ and $\Pi^{\alpha} \otimes I^{\beta}$: if the $\Pi^{\alpha}$-measurement has a certain outcome, then the $\Pi^{\alpha} \otimes I^{\beta}$-measurement has exactly the same outcome.

The question now arises whether the rules of BDMI and SDMI, applied to $\alpha$, assign a value to $\Pi^{\alpha}$ that is the same as the value assigned to $\Pi^{\alpha} \otimes I^{\beta}$ when the rules are applied to the composite system $\alpha \beta$ (a condition known as Property Composition), and vice versa (Property Decomposition). The answer to this question is negative: BDMI and SDMI violate Property Composition and Property Decomposition (for a proof, see Vermaas 1998)[^vermaas-1998].

If one maintains that the projectors $\Pi^{\alpha}$ and $\Pi^{\alpha} \otimes I^{\beta}$ must represent the same property, the violation of Property Composition and Property Decomposition is a serious problem. Thus, Arntzenius (1990) finds the violation of Property Composition bizarre, since different truth values are assigned to propositions like ‘the left-hand side of a table is green’ and ‘the table has a green left-hand side’; a similar argument is put forward by Clifton (1996, see also Clifton 1995c)[^clifton-1995c].

However, Vermaas (1998) argues that the observational indistinguishability of the magnitudes represented by $\Pi^{\alpha}$ and $\Pi^{\alpha} \otimes I^{\beta}$ does not force one to consider these two projectors as representing the same property: in fact, they are different from a theoretical viewpoint, since they are defined on different Hilbert spaces. Moreover, he argues that the examples developed by Arntzenius and Clifton sound bizarre precisely in the light of Property Composition and Property Decomposition. But in the quantum realm we must accept that the questions of which properties are possessed by a system and which by its subsystems are different questions: the properties of a composite system $\alpha\beta$ don’t always fix the properties of subsystem $\alpha$, and vice versa. Vermaas concludes that the tenet that $\Pi^{\alpha}$ and $\Pi^{\alpha} \otimes I^{\beta}$ do represent the same property can be viewed as an addition to quantum mechanics, which can be denied as, for instance, van Fraassen (1991) did.

A similar problem is due to the fact that the factorization of Hilbert spaces is not unique: any given factorization $\mathcal{H} = \mathcal{H}^1 \otimes \mathcal{H}^2$ can be “rotated” to produce different factorizations $\mathcal{H}' = \mathcal{H}^1{}^\prime \otimes \mathcal{H}^2{}^\prime$. Are we to apply the same rules to each such factorization? How are the results related, if at all? A theorem due to Bacciagaluppi (1995, see also Vermaas 1997)[^vermaas-1997] shows that if one applies SDMI to every factorization and insists that the values of observables that occur in the different factorizations are factorization-independent, then one will end up with a mathematical contradiction of the Kochen-Specker type.

One possible reaction to these difficulties is to assume that there is a preferred factorization. (One may also regard the above problems as an indication that systems possess their properties in a relational way, see Section 5). The Atomic Modal Interpretation (AMI, Bacciagaluppi and Dickson 1999)[^bacciagaluppi-1999] thus assumes that nature fixes a set of mutually disjoint atomic quantum systems $S^j$ that constitute the building blocks of all other quantum systems. From the mathematical point of view, this means that the Hilbert space $\mathcal{H}^{\univ}$ of the entire universe can only be meaningfully factorized in a single way, which defines a preferred factorization. If each atomic quantum system $S^j$ corresponds to a Hilbert space $\mathcal{H}^j$, then the Hilbert space $\mathcal{H}^{\univ}$ of the universe must be written as

$$ \mathcal{H}^{\univ} = \mathcal{H}^1 \otimes \mathcal{H}^2 \otimes \cdots \otimes \mathcal{H}^j \otimes \cdots $$

The appeal of this idea is that it is in consonance with the standard model of particle physics, where the fundamental blocks of nature are the elemental particles, e.g., quarks, electrons, photons, etc., and their interactions. Moreover, the problems mentioned above can be evaded in AMI: once the atomic building blocks have been assigned definite properties, one may stipulate that composite systems have properties that follow from property composition. Some of these ideas are implemented in the Modal-Hamiltonian Interpretation, to be discussed in Section 8. The property ascription to the atomic quantum systems in the AMI further follows the general idea of modal interpretations, that is, the ascription depends via a fixed rule on the dynamical state of the system.

The main challenge for AMI is to justify the assumption that there is a preferred partition of the universe and to provide some idea about what this factorization should look like. AMI also faces another problem. A non-atomic quantum system $S^{\sigma}$, defined as composite of atomic quantum systems, does not necessarily have properties that correspond to the outcomes of measurements. The reason is that the system $S^{\sigma}$ might be in the quantum state $\varrho^{\sigma}$ with an eigenprojector $\Pi^{\sigma}$ such that $\mathrm{Tr}^{\sigma}(\varrho^{\sigma}\Pi^{\sigma}) = 1$. This implies that if one measured the property represented by $\Pi^{\sigma}$, one would obtain a positive outcome with probability 1. But it may be the case that the projector $\Pi^{\sigma}$ is not a composite of atomic properties and, therefore, according to AMI, it is not a property possessed by the composite quantum system $S^{\sigma}$.

Two answers to this difficulty have been proposed. The first allows the existence of dispositional properties in addition to ordinary properties (Clifton 1996)[^clifton-1996]. According to the second answer, the outcome 1 of the projector $\Pi^{\sigma}$ is a collective dynamical effect onto the measurement device (Dieks 1998)[^dieks-1998][^dieks-1998-2]: the composite quantum system may behave as a collective entity, screening off the atomic quantum systems. This implies that a non-atomic quantum system $S^{\sigma}$ may sometimes be taken as if it were atomic within a coarse-grained description.

## 6. Dynamics of properties

As we have seen, modal interpretations intend to provide, for every instant, a set of definite-valued properties and their probabilities. Some advocates of modal interpretations are willing to leave the matter at that. Others take it to be crucial that also questions of the following form are answered: given that the property $P$ of a system has the actual value $\alpha$ at time $t_0$, what is the probability that its property $P'$ has the actual value $\beta$ at time $t_1 \gt t_0$? In other words, they want a *dynamics* of actual properties.

There are arguments on both sides (van Fraassen 1997)[^fraassen-1997]. Those who argue for the necessity of such a dynamics maintain that we have to assure that the *trajectories* of actual properties *really are*, at least for macroscopic objects, like we see them to be, i.e., like the records contained in memories. For example, we should require not only that the book at rest on the desk possesses a definite location, but also that, if undisturbed, its location relative to the desk does not change in time. Accordingly, one cannot get away with simply specifying possible definite properties at each instant of time. We need also to show that this specification is at least compatible with a reasonable dynamics; better still, to specify this dynamics explicitly.

Those who consider a dynamics of actual properties to be superfluous reply that such a dynamics is more than what an interpretation of quantum mechanics needs to provide. Memory contents for each instant are enough to make empirical adequacy possible.

Ruetsche (2003) argues that it is important in this connection whether the modal interpretation is viewed as leading to a *hidden-variables theory*, in which value states are added as hidden variables to the original formalism in order to obtain a full description of the physical situation, or rather as an interpretive move that equips the original formalism with a new semantics (see also Section 11). In the first case one would expect a full dynamics of actual properties, in the second this is not so clear.

Of course, modal interpretations admit a trivial dynamics, namely, one in which there is no correlation from one time to the next. In this case, the probability of the transition from the property $P$ having the actual value $\alpha$ at $t_0$ to the property $P'$ having the actual value $\beta$ at $t_1 \gt t_0$ is just the single-time probability for $P'$ having $\beta$ at $t_1$. However, this dynamics is unlikely to interest those who feel the need for a dynamics at all. Several researchers have contributed to the project of constructing a more interesting form of dynamics for modal interpretations (see Vermaas 1996, 1998)[^vermaas-1996][^vermaas-1998]. An important account is due to Bacciagaluppi and Dickson (1999, see also Bacciagaluppi 1998)[^bacciagaluppi-1998]. That work shows the most significant challenges that the construction of a dynamics of actual properties must face.

The first challenge is posed by the fact that the set of definite-valued properties—let us call it ‘$S$’—may change over time. One therefore has to define a family of maps, each one being a 1–1 map from $S_0$ at time $t_0$ to a different $S_t$ at time $t$, for any time. With such a family of maps, one can effectively define conditional probabilities within a single state space, and then translate them into “transition” probabilities. For this technique to work, $S_t$ must have the same cardinality at any time. However, in general this is not the case: for instance, in SDMI, the number of different projectors appearing in the spectral decomposition of the density matrix may vary with time.

A way out of this is to augment $S$ at each time so that its cardinality matches the highest cardinality that $S$ ever achieves. Of course, one hopes to do so in a way that is not completely ad hoc. For example, in the context of SDMI, Bacciagaluppi, Donald and Vermaas (1995) show that the “trajectory” through Hilbert space of the spectral components of the reduced state of a physical system will, under reasonable conditions, be continuous, or have only isolated discontinuities, so that the trajectory can be naturally extended to a continuous trajectory (see also Donald 1998)[^donald-1998]. This result suggests a natural family of maps as discussed above, which map each spectral component at one time to its unique continuous evolved component at later times.

The second challenge to the construction of a dynamics arises from the fact that one wants to define transition probabilities over infinitesimal units of time, and then derive the finite-time transition probabilities from them. Bacciagaluppi and Dickson (1999) argue that, adapting results from the theory of stochastic processes, one can show that the procedure may be carried out for modal interpretations of at least some varieties.

Finally, one must define infinitesimal transition probabilities that will give rise to the proper quantum-mechanical probabilities at each time. Following earlier papers by Bell (1984), Vink (1993), and others, Bacciagaluppi and Dickson (1999) define an infinite class of such infinitesimal transition probabilities, such that all of them generate the correct single-time probabilities, which arguably are all we can really test. However, Sudbery (2002) has contended that the form of the transition probabilities *would* be relevant to the precise form of spontaneous decay or the “Dehmelt quantum jumps”; he independently develops the dynamics of Bacciagaluppi and Dickson and applies it in such a way that it leads to the correct predictions for these experiments. Gambetta and Wiseman (2003, 2004) have developed a dynamical modal account in the form of a non-Markovian process with noise, also extending their approach to positive operator-valued measures (POVMs). More recently, Hollowood (2013a, 2013b, 2014) has elaborated the idea that the dynamics of value states can be modeled by a discrete-time Markov chain.

## 7. Perspectival modal interpretation

In Section 5 it was discussed how the attribution of physical properties to systems in an absolute (monadic) sense leads to consistency questions. Such questions may be avoided if one adopts a metaphysics in which properties are *relational*. In fact, it can be argued that the mathematical structure of non-collapse quantum mechanics strongly suggests a relational picture anyhow, as evidenced, for example, by Everett’s (1957) reasons for introducing his *relative* states (these reasons relate to the non-collapse treatment of Wigner’s friend paradox).

An early relational modal interpretation was proposed by Kochen (1985). According to Kochen, in a bi-partite system one system possess properties “as witnessed” by the other system.

Bene and Dieks (2002) have developed a more general perspectival modal interpretation (PMI), in which the properties of any physical system are defined with respect to arbitrary other physical systems that serve as “reference systems” (Bene 1997)[^bene-1997]. PMI is closely related to SDMI since similar rules are used to assign properties to quantum systems.

In more detail, the state of $S$ with respect to the reference system $R$ is denoted by $\varrho_{R}^{S}$. In the special case in which $R$ coincides with $S$, the state $\varrho_{S}^{S}$ is called “*the state of S with respect to itself*”. If the system $S$ is contained in a system $A$, the state $\varrho_{A}^{S}$ is defined as the density operator that can be derived from $\varrho_{A}^{A}$ by taking the partial trace over the degrees of freedom in $A$ that do not pertain to $S$:

$$ \varrho_{A}^{S} = \mathrm{Tr}_{(A\setminus S)} \varrho_{A}^{A} $$

PMI starts with the dynamical state of the whole universe with respect to itself, which it is assumed to be a pure state $\varrho_{U}^{U} = \ket{\psi} \bra{\psi}$, evolving unitarily according to the Schrödinger equation. For any system $S$ contained in the universe, its value state with respect to itself $\varrho_{S}^{S}$ is postulated to be one of the projectors of the spectral resolution of $\varrho_{U}^{S} = \mathrm{Tr}_{(U\setminus S)} \varrho_{U}^{U} = \mathrm{Tr}_{(U\setminus S)} \ket{\psi} \bra{\psi}$. In particular, if there is no degeneracy among the eigenvalues of $\varrho_{U}^{S}$, $\varrho_{S}^{S}$ is the one-dimensional projector $\ket{\psi_{S}} \bra{\psi_{S}}$.

Within PMI it may happen that a system is localized from the perspective of one observer and, nevertheless, is delocalized from a different perspective. However, when different observers look at the same macroscopic object, this effect will be suppressed due to decoherence effects.

The “metaphysical” idea behind this perspectival interpretation is that different relational descriptions, given from different perspectives, are to be considered as equally objective; physical reality has a relational character and perspectival states cannot be reduced to more fundamental non-relational states.

In this relational/perspectival interpretation the course of events in experiments of the EPR-type may be described in a local manner. The idea is that the change in the relational state of particle 2 with respect to particle 1 can be understood as a consequence of the change in the reference system brought about by the local measurement interaction between particle 1 and the measuring device. This local measurement is responsible for the creation of a new perspective, and from this new perspective there is a new relational state of particle 2. According to this account, nothing changes at the position of particle 2 when the measurement on particle 1 takes place. For more complicated situations in which there is also a measurement at particle 2, and observers later compare their results, a radical form of perspectivalism (or relationism) has to be adopted to achieve locality from all points of view (Dieks 2022b)[^dieks-2022b].

PMI agrees with Bohr’s statement that the definition of physical reality in the quantum realm should include the experimental context (see Dieks 2017 for a detailed discussion of Bohr’s views and a comparison with the modal approach)[^dieks-2017]. However, PMI is more general and technically precise: PMI defines the state of a system with respect to arbitrary contexts, not necessarily related to measurements. This removes the threat of subjectivism, as the relational states follow unambiguously from the quantum formalism and the physics of the situation.

Berkovitz and Hemmo (2006) suggest that a relational approach is needed to generalize modal interpretations to the relativistic case. Dieks (2021) provides a detailed scheme with the help of which PMI can be made relativistically covariant (borrowing ideas from the many-worlds interpretation).

Rovelli and coworkers have also proposed a relational interpretation of quantum mechanics in which there is the possibility of different perspective-dependent descriptions of a physical system (Rovelli 1996, Rovelli and Smerlak 2007, Laudisa and Rovelli 2021, see also van Fraassen 2010 and the entry relational quantum mechanics.)[^laudisa-2021][^rovelli-1996][^rovelli-2007][^fraassen-2010] There are many similarities between PMI and Rovelli’s relational interpretation, but also some differences. In Rovelli’s proposal, discrete interaction events (some of which correspond to measurements) are fundamental and are assumed to produce definite values of relational quantities. By contrast, in PMI relative states define perspectival quantities at all times.

## 8. Modal-Hamiltonian interpretation

As Bub (1997) points out (see Section 2), in most modal interpretations the preferred context of definite-valued observables is determined solely by the dynamical state of the system; but one could also introduce a preferred definite-valued observable. An example is Bohmian mechanics, in which the preferred context is a priori defined by the position observable; in this case, property composition and property decomposition hold. But this is not the only reasonable possibility for a modal interpretation with a fixed preferred observable. In fact, the modal-Hamiltonian interpretation (MHI, Lombardi and Castagnino 2008; for an updated version, see Lombardi 2025)[^lombardi-2025][^lombardi-2008] endows the Hamiltonian of a system with a determining role, both in the definition of systems and subsystems and in the selection of the preferred context.

The MHI is based on the following postulates:

**Systems postulate (SP):** A quantum system $S$ is represented by a pair $(\mathcal{O}, H)$ such that (i) $\mathcal{O}$ is a space of self-adjoint operators on a Hilbert space, representing the observables of the system, (ii) $H \in \mathcal{O}$ is the time-independent Hamiltonian of the system $S$, and (iii) if $\varrho_0 \in \mathcal{O}'$ (where $\mathcal{O}'$ is the dual space of $\mathcal{O})$ is the initial state of $S$, it evolves according to the Schrödinger equation.

Although any quantum system can be decomposed in parts in many ways, according to MHI a decomposition leads to parts which are also quantum systems only when the components’ behaviors are dynamically independent of each other, that is, when there is no interaction among the subsystems:

**Composite systems postulate (CSP):** A quantum system represented by $S: (\mathcal{O}, H)$, with initial state $\varrho_0 \in \mathcal{O}'$, is *composite* when it can be partitioned into two quantum systems $S^1 : (\mathcal{O}^1, H^1)$ and $S^2 : (\mathcal{O}^2, H^2)$ such that (i) $\mathcal{O} = \mathcal{O}^1 \otimes \mathcal{O}^2$, and (ii) $H = H^1 \otimes I^2 + I^1 \otimes H^2$ (where $I^1$ and $I^2$ are the identity operators in the corresponding tensor product spaces). In this case, we say that $S^1$ and $S^2$ are *subsystems* of the composite system $S = S^1 \cup S^2$. If the system is not composite, it is *elemental*.

With respect to the preferred context, the basic idea of MHI is that the Hamiltonian of the system defines actualization. Any observable that does not have the symmetries of the Hamiltonian cannot acquire a definite actual value, since this actualization would break the symmetry of the system in an arbitrary way.

**Actualization rule (AR):** Given an elemental quantum system represented by $S: (\mathcal{O}, H)$, the actual-valued observables of $S$ are $H$ and all the observables commuting with $H$ and having, at least, the same symmetries as $H$.

The selection of the preferred context exclusively on the basis of a preferred observable has been criticized by arguing that in the Hilbert space formalism all observables are on an equal footing. However, quantum mechanics is not just Hilbert space mathematics: it is a physical theory that includes a dynamical law in which the Hamiltonian is singled out to play a central role.

The justification for selecting the Hamiltonian as the preferred observable ultimately lies in the success of MHI and its ability to solve interpretive difficulties (see Lombardi and Castagnino 2008, Sections 5 and 6)[^lombardi-2008]. With respect to the first point: the scheme has been applied to several well-known physical situations (free particle with spin, harmonic oscillator, free hydrogen atom, Zeeman effect, fine structure, the Born-Oppenheimer approximation), leading to results consistent with empirical evidence. With respect to interpretation, MHI confronts quantum contextuality by selecting a preferred context, and has proved to be able to supply an account of the measurement problem, both in its ideal and its non-ideal versions; moreover, in the non-ideal case it gives a criterion to distinguish between reliable and non-reliable measurements.

In MHI property composition and property decomposition hold because the actualization rule only applies to *elemental* systems: the definite-valued properties of composite systems are selected on the basis of those of the elemental components and following the usual quantum assumption according to which the observable $A^1$ of a subsystem $S^1$ and the observable $A = A^1 \otimes I^2$ of the composite system $S = S^1 S^2$ represent the same property.

The preferred context of MHI does not change with time: the definite-valued observables always commute with the Hamiltonian and, therefore, they are constants of motion of the system. This means that they are the same during the whole “life” of the quantum system as a closed system, since its initial “birth”, when it arises as a result of an interaction, up to its final “death”, when it disappears by interacting with another system. As a consequence, there is no need of accounting for the dynamics of the actual properties as in BDMI and SDMI.

In more recent years, MHI has extended its applications to further situations, such as the non-collapse account of consecutive measurements in physics (Ardenghi, Lombardi, and Narvaja 2013)[^ardenghi-2013] and the problem of optical isomerism in chemistry (Fortin, Lombardi, and Martínez González 2018)[^fortin-2018].

## 9. Non-ideal measurements

Above we suggested that BDMI and SDMI immediately solve the measurement problem. This is right in the case of ideal von Neumann measurements, in which the eigenstates $\ket{a_i}$ of the measured observable $A$ of the object system $S$ become perfectly correlated with the eigenstates $\ket{p_i}$ of the pointer $P$ of the measuring apparatus $M$. However, ideal measurements can never be achieved in practice: the interaction between $S$ and $M$ never produces a completely perfect correlation between $A$ and $P$. Two kinds of non-ideal measurements are usually distinguished in the literature:

- *Imperfect measurement* (*first kind*) $\sum_i c_i \ket{a_i} \otimes \ket{p_0} \rightarrow \sum_{ij} d_{ij} \ket{a_i} \otimes \ket{p_j}$ (in general, $d_{ij} \ne 0$ with $i \ne j)$
- *Disturbing measurement* (*second kind*) $\sum_i c_i \ket{a_i} \otimes \ket{p_0} \rightarrow \sum_i c_i \ket{a_i^d} \otimes \ket{p_i}$ (in general, $\braket{a_i^d}{a_j^d} \ne \delta_{ij}$)

Note, however, that disturbing measurement can be rewritten as imperfect measurements (and vice versa).

Imperfect measurements pose a challenge to BDMI and SDMI, since their rules for selecting the definite-valued properties in this case do not pick out the right properties for the apparatus (see Albert and Loewer 1990, 1991, 1993; also Ruetsche 1995)[^albert-1990][^albert-1991][^albert-1993][^ruetsche-1995]. An example that clearly brings out the difficulties was formulated in the context of Stern-Gerlach experiments (Elby 1993)[^elby-1993]. This argument uses the fact that the wavefunctions in the $z$-variable typically have infinite “tails” that introduce non-zero cross-terms; therefore, the “tail” of the wavefunction of the “down” beam may produce detection in the upper detector, and vice versa (see Dickson 1994 for a detailed discussion)[^dickson-1994].

If the biorthogonal decomposition is applied to the non-perfectly correlated state $\sum_{ij} d_{ij} \ket{a_i} \otimes \ket{p_j} = \sum_i c_i' \ket{a_i'} \otimes \ket{p_i'}$, according to BDMI the result does not select the pointer $P$ as a definite-valued property, but a different observable $P'$ with eigenstates $\ket{p_i'}$. In this case, in which the selected definite-valued properties are different from those expected, the question arises how different they are. In the case of an imperfect measurement, it may be assumed that the $d_{ij} \ne 0$, with $i \ne j$, be small; then, the difference might be also small. But in the case of a disturbing measurement, the $d_{ij} \ne 0$, with $i \ne j$, need not be small and, as a consequence, the disagreement between the modal interpretation assignment and the experimental result might be unacceptable (see a full discussion in Bacciagaluppi and Hemmo 1996)[^bacciagaluppi-1996][^bacciagaluppi-1996-2]. This fact has been considered as a “silver bullet” for killing the modal interpretations of the BDMI and SDMI types (Harvey Brown, cited in Bacciagaluppi and Hemmo 1996)[^bacciagaluppi-1996][^bacciagaluppi-1996-2]. This is premature: a fuller analysis involving environmental decoherence is able to remove many of these problems—see below.

Another problem for the BDMI and SDMI interpretations relates to degeneracy. When the final state of the composite system (measured system plus measuring device) is very nearly degenerate when written in the basis given by the measured observable and the apparatus’ pointer (that is, when the probabilities for the various results are almost equal), the spectral decomposition need not, in general, select definite-valued properties that are close to those ideally expected. In fact, the observables so selected may be incompatible (non-commuting) with the observables that we expect on the basis of observation (Bacciagaluppi and Hemmo 1994, 1996)[^bacciagaluppi-1996][^bacciagaluppi-1994][^bacciagaluppi-1996-2].

In order to solve these problems, several authors have appealed to the phenomenon of decoherence; this will now be discussed.

## 10. The role of decoherence

According to the environment-induced approach to decoherence (Zurek 1981, 2003; see also Schlosshauer 2007)[^schlosshauer-2007][^zurek-1981][^zurek-2003], any macroscopic measuring apparatus is an open system in continuous interaction with its environment; as a consequence of this interaction, the reduced state of the apparatus becomes, almost instantaneously, indistinguishable from a state that would represent an ignorance mixture (“proper mixture”) over unknown but definite positions of the apparatus’ macroscopic pointer. The idea that decoherence might play an important role in modal interpretations, by making macroscopic quantities definite, was suggested by several authors early on. Consideration of decoherence has acquired central relevance in the discussion of non-ideal measurements.

As we have seen, in BDMI and SDMI, the biorthogonal and spectral decompositions do generally not pick out the right properties for the apparatus in non-ideal measurements. However, Bacciagaluppi and Hemmo (1996) show that, when the apparatus is a finite-dimensional system in interaction with an environment containing a large number of degrees of freedom, decoherence guarantees that the spectral decomposition of the reduced apparatus’ state will be very close to the ideally expected result and, as a consequence, an observable very close to and indistinguishable from the apparatus pointer will be selected as definite-valued. Alternatively, Bub (1997) suggests that instead of decoherence—with the “tracing out” of the environment and the diagonalization of the reduced state of the apparatus—the triorthogonal or $n$-orthogonal decomposition theorem involving the environment may be used to single out a unique pointer basis for the apparatus.

In either case, interaction with the environment solves the problem of non-ideal measurements in BDMI and SDMI for the case of finite-dimensional macroscopic apparatuses. However, the case of *infinitely* many distinct states for the apparatus is more troublesome. Bacciagaluppi (2000) has analyzed this situation, using a continuous model of the apparatus’ interaction with the environment. He concludes that in this case the spectral decomposition of the reduced state of the apparatus generally does not pick out properties that are close enough to empirically required ones. This result seems to apply generally to cases where a macroscopic system with infinitely many degrees of freedom experiences decoherence due to interaction with its environment (see Donald 1998)[^donald-1998]. However, model calculations by Hollowood (2013, 2014) indicate that the problem may be less severe in realistic circumstances than originally supposed, and the issue needs further investigation.

Modal interpretations with an a priori fixed preferred observable (MHI, and Bohm’s interpretation) are immune to the above objections: decoherence by the environment need not be invoked in order to account for the definiteness of the apparatus’ pointer position (neither in ideal nor in non-ideal measurements). However, in MHI there still is a relation with the decoherence program. In fact, the measuring apparatus is always a macroscopic system with a huge number of degrees of freedom, and the pointer must therefore be a “collective” and empirically accessible observable; as a consequence, the many degrees of freedom —and the corresponding degeneracies— of the pointer play the role of a decohering “internal environment” (for details, see Lombardi et al. 2011)[^lombardi-2011]. The role of decoherence in the MHI becomes clearer when the phenomenon of decoherence is understood from a closed-system perspective (Castagnino, Fortin, and Lombardi 2010)[^castagnino-2010][^lombardi-2010]. (See the entry on the role of decoherence in quantum mechanics.)

## 11. The measurement problem revisited: completeness and hidden variables

The measurement problem is usually given the form of the incompatibility of three assertions of the following form (cf. Maudlin 1995, Myrvold 2018)[^maudlin-1995][^myrvold-2018]:

1. The quantum state is “complete”.
2. The quantum state always evolves in accordance with a linear dynamical equation (e.g., the Schrödinger equation).
3. Successful measurements have unique and determinate outcomes.

To avoid inconsistency three interpretive strategies are standardly considered: denying completeness (a), which is often taken to lead to hidden-variable theories; denying (b), which results in theories according to which collapses take place; or denying (c), which leads to many worlds.

Modal interpretations accept both (b) and (c), so that it follows that they must violate (a). Thus, it seems clear that modal interpretations have to view quantum mechanics as “incomplete”. Indeed, it is true that according to modal interpretations the quantum state does not fix all actual physical properties (i.e., the actual values of all definite-valued physical quantities) of a system, which is the criterion of incompleteness presupposed in (a).

However, many proponents of modal schemes argue that the latter feature is not appropriately expressed by saying that quantum mechanics, modally conceived, is incomplete. They object that this incompleteness terminology is apt to suggest a defect of the theory, and the need for completion (by hidden variables). But modal theorists maintain that their interpretations of quantum mechanics are not in need of additions, because these interpretations already contain everything that can reasonably be expected from theories describing a fundamentally probabilistic (indeterministic) world. First, modal schemes completely specify which observables are definite-valued. Second, they fix the possible values that may be taken by these observables and they provide the probabilities with which these values may be realized. Since it is a core modal principle that the actualization of properties in the quantum world is a fundamentally probabilistic (indeterministic) process, nothing more than this probabilistic description is possible. From this viewpoint, insisting that modally interpreted quantum mechanics is necessarily incomplete is tantamount to stipulating that any probabilistic theory must be incomplete by definition—even if it applies to a fundamentally probabilistic world. But that appears an inappropriate use of terminology.

## 12. The interpretation of probability

The leading ideas of modal interpretations are thus *indeterminism* and *probabilism*: quantum mechanics does not describe actuality but provides us with a list of possibilities and their probabilities. This central position of the concept of probability raises two issues: the formal treatment of probabilities and the interpretation of probability.

Since the set of all projector operators on a given Hilbert space does not have a Boolean structure, the Born probability (which is defined over these projectors) does not satisfy the definition of probability of Kolmogorov (which applies to a Boolean algebra of events). For this reason, some authors define a generalized non-Kolmogorovian probability function over the ortho-algebra of quantum events (Hughes 1989, Cohen 1989)[^cohen-1989][^hughes-1989]. Modal interpretations do not follow this path: they conceive probabilities as represented by a Kolmogorovian measure on the Boolean algebra representing the definite-valued quantities, generated by mutually commuting projectors. As we have seen, the various modal interpretations differ from each other in their definitions of the preferred context on which the Kolmogorovian probability is defined.

In general, a context can be described as a complete set of orthogonal projectors $\{\Pi_{\alpha}\}$, such that $\sum_{i} \Pi_{i} = I$ and $\Pi_{i}\Pi_j = \delta_{ij}\Pi_{i}$, where $I$ is the identity operator in $\mathcal{H} \otimes \mathcal{H}$. Each such context generates a Boolean structure, and the state of the system defines a Kolmogorovian probability function on each individual context. However, only the probabilities defined on the preferred context selected by the modal interpretation at hand correspond to physical possibilities, one of which is actual.

So we are dealing with possible events, among which only one is actual. The fact that the actual event is not singled out by modal interpretations, as a point of principle, is what makes them fundamentally probabilistic. This aspect distinguishes modal interpretations from many-worlds interpretations, where all events are actual and in which probability must consequently be a problematic notion. Nevertheless, this modal unanimity about the fundamental role of probability does not mean that all modal interpretations agree about the interpretation of probability.

In the context of BDMI, SDMI and PMI it is usually claimed that, given the space of possible events, the state generates an ignorance-interpretable probability measure over this set: quantum probabilities quantify the ignorance of the observer about the actual values acquired by the system’s observables (see, e.g., Clifton 1995a, Vermaas 1999)[^clifton-1995a][^vermaas-1999].

By contrast to this “actualism”—the conception that reduces possibility to actuality (see Bueno 2014)[^bueno-2014]—some modal interpretations, in particular MHI, adopt a possibilist conception, according to which possible events—*possibilia*—constitute a basic ontological category (see Menzel 2018)[^menzel-2018]. The probability measure is in this case seen as a representation of an ontological propensity of a possible quantum event to become actual (Suárez 2004; Terekhovich 2019 [Other Internet Resources])[^suárez-2004].

It is to be noted that the indeterminism of modal quantum mechanics does not imply that the present quantum state of a system fails to determine its future quantum states. The Schrödinger equation is deterministic, and the probabilities encoded in the quantum state therefore evolve in a deterministic way. Indeterminism comes in when we consider the actual values of observables, which are not predetermined even if the quantum state is completely fixed: modal interpretations take processes of actualization to be essentially probabilistic.

In this context, the two mentioned views about probability (actualism versus possibilism) do not exclude each other. That probabilities quantify ignorance about actual values of observables (as in actualism) does not entail that this ignorance is due to a lack of knowledge about underlying deterministic processes. Possibilism adds that quantum probabilities represent propensities and that our ignorance is a necessary consequence of the indeterministic ontology of the physical world, in which propensities constitute a fundamental category.

## 13. Open problems and perspectives

Many quantum physicists implicitly subscribe to modal ideas in their work, in the sense that they employ the formalism of unitary quantum mechanics in order to make probabilistic statements about one single world (our own). This use of unitary quantum mechanics is especially popular in quantum information theory. There is also a growing interest in questions concerning the conceptual consequences of a consistent application of unitary (noncollapse) quantum mechanics to the physical world (see, e.g., Frauchiger and Renner 2018 and ensuing discussions)[^frauchiger-2018]. These questions find their natural place within the modal interpretation program.

During the last decade, modal interpretations have also more explicitly drawn the attention of practicing physicists and mathematicians interested in foundational matters. For instance, Hollowood (2014) offers an interpretation of quantum mechanics inspired by PMI: in this account the state of an open system represents its properties as seen from the perspective of the closed system of which it is a subsystem. Barandes and Kagan (2014a, 2014b, 2020) propose a “minimal modal interpretation”, inspired by SDMI, according to which the preferred context is given by the evolving reduced state of the open system. Nakayama (2014a, 2014b) has explored connections between the modal interpretation and the framework of topos theory.

There are also several specifically philosophical issues connected to the modal program: about the nature of the “things” to which quantum mechanics refers, that is, about the basic categories of the quantum ontology. As we have seen, in general the properties of quantum systems are considered to be monadic in modal interpretations, with the exception of the perspectival version PMI where these properties are relational. In both cases, it may be asked whether a quantum system has to be conceived as an individual substratum supporting properties or as a mere “bundle” of properties which do not need to constitute an individual in the ordinary sense. Following an original idea of the MHI, da Costa and Lombardi (2014) have suggested that, in the modal context, the bundle view is the most appropriate one to supply an answer to the problem of indistinguishability of identical quantum particles (French and Krause 2006)[^french-2006]. As noticed by Steven French (2020 [Other Internet Resources]), this view of non-individual bundles finds a natural resonance with ontic structural realism, which was mainly motivated by the ontological challenges of quantum mechanics (Ladyman 1998)[^ladyman-1998]. Moreover, this ontology of properties has been taken as a basis for a metaphysical interpretation of relational quantum mechanics (Oldofredi 2021)[^oldofredi-2021] and as a paradigmatic case of quantum indeterminacy (Calosi 2022)[^calosi-2022], and it has been applied to quantum field theory (Rossanese 2023)[^rossanese-2023]. It should be noted that this bundle ontology does not contradict the emergence of classical distinguishable particles in certain situations, e.g. the classical limiting case (Lombardi and Dieks 2016)[^lombardi-2016].

Also other ontological topics relating to modal interpretations have recently become subjects of discussion. Thus, Calosi (2018) argues that BDMI and AMI pose significant challenges to quantum monism, that is, the view according to which there is only one fundamental entity —the universe as a whole. In the context of the discussion about the classification between ${\psi}$-ontic and ${\psi}$-epistemic models, Oldofredi and López (2020) show that such a classification is too narrow to include relational interpretations such as PMI.

There are also more technical issues that await further discussion. Modal interpretations as discussed here are based on the standard Hilbert space formalism of quantum mechanics. However, Brown, Suárez, and Bacciagaluppi (1998) argue that there is more to quantum reality than what is described by operators and quantum states: they claim that gauges and coordinate systems are important to our description of physical reality as well, while modal interpretations (AM, BDMI and SDMI) have standardly not taken such things into consideration. In a similar vein, in the context of the MHI it has been argued that Galilean space-time symmetries endow the formal skeleton of quantum mechanics with physical flesh and blood and identify the fundamental physical magnitudes that allow the theory to be applied to concrete physical situations. If the set of definite-valued observables of a system is postulated to be invariant under Galilean transformations (the intuition being that a mere change in inertial reference frame does not change this set), the MHI rule of actualization can be reformulated in an explicitly invariant form, in terms of the Casimir operators of the Galilean group (Ardenghi, Castagnino, and Lombardi 2009)[^ardenghi-2009].

Another fundamental question is the relativistic extension of the modal approach. Dickson and Clifton (1998) have shown that a large class of modal interpretations of ordinary quantum mechanics cannot be made Lorentz-invariant in a straightforward way (see also Myrvold 2002)[^myrvold-2002]. With respect to the extension to algebraic quantum field theory (see Kitajima 2004)[^kitajima-2004], Clifton (2000) proposed a natural generalization of the non-relativistic modal scheme, but Earman and Ruetsche (2005) showed that it is not yet clear whether it will be able to deal with measurement situations and whether it is empirically adequate. The problems revealed by these investigations relate to the fact that modal interpretations employ the non-relativistic concept of a global state, of an extended system, at one instant. In a local field-theoretic context this becomes different, and this may help avoiding conflicts with relativity (Earman and Ruetsche 2005)[^earman-2005]. Berkovitz and Hemmo (2005) and Hemmo and Berkovitz (2005) propose a different way out: they argue that perspectivalism can come to the rescue here (see also Berkovitz and Hemmo 2006)[^berkovitz-2006]. The idea that perspectivalism is essential for ensuring compatibility with special relativity is elaborated by Dieks (2021), who puts forward a relativistically covariant treatment of experiments of the EPR-type, based on PMI.

In the context of MHI an alternative program for achieving relativistic covariance has been developed, based on the idea that the actualization rule, expressed in terms of the Casimir operators of the Galilean group in non-relativistic quantum mechanics, can be transferred to the relativistic domain by changing the symmetry group accordingly. In this case the definite-valued observables of a system become those represented by the Casimir operators of the Poincaré group. Since the mass operator and the squared spin operator are the only Casimir operators of the Poincaré group, these then are always definite-valued observables. This conclusion is in agreement with a usual assumption in quantum field theory: elemental particles always have definite values of mass and spin, and those values are precisely what define the different kinds of elemental particles of the theory (Lombardi, Castagnino, and Ardenghi 2010)[^castagnino-2010][^lombardi-2010].

These various proposals and developments have arisen in the context of detailed technical investigations. This illustrates two features of the modal approach: on the one hand it makes use of a precise mathematical framework; on the other hand it is flexible and open-ended, and can accommodate different views concerning the rules determining the set of definite-valued observables. It is natural to expect new offshoots; for example, it seems plausible that strategies followed in many-worlds interpretations to define different “branches” can also be incorporated in the modal approach in order to define single-world possibilities. Whatever these prospects, one can at least say that the modal approach has given rise to a fruitful series of investigations into the structure of quantum theory.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=qm-modal). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/qm-modal/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=qm-modal&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/qm-modal/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- French, S., 2020, “[What is this thing called structure? (Rummaging in the toolbox of metaphysics for an answer)](http://philsci-archive.pitt.edu/id/eprint/16921),” unpublished manuscript, PhiSci Archives.
- Terekhovich, V., 2019, “[Modal approaches in metaphysics and quantum mechanics](https://arxiv.org/abs/1909.10046v1),” manuscript at arXiv.org. Published in Russian in *Metaphysics*, 2015, 1(15): 129–152.

## Related Entries

quantum mechanics | quantum mechanics: Bohmian mechanics | quantum mechanics: Everettian | quantum mechanics: Kochen-Specker theorem | quantum mechanics: many-worlds interpretation of | quantum mechanics: relational | quantum mechanics: the role of decoherence in | quantum theory: philosophical issues in | quantum theory: the Einstein-Podolsky-Rosen argument in

### Acknowledgments

As of the December 2012 update, the credited authors for this entry are Olimpia Lombardi and Dennis Dieks. The [original version of this entry](https://plato.stanford.edu/archives/fall2007/entries/qm-modal/) (published in 2002, last archived in Fall 2007) was authored solely by Michael Dickson and we acknowledge that some sentences of that first version are still part of the current entry.

[^albert-1990]: Albert, D. and B. Loewer, 1990, “Wanted dead or alive: two attempts to solve Schrödinger’s paradox,” in *Proceedings of the PSA 1990* (Volume 1), A. Fine, M. Forbes, and L. Wessels (eds.), East Lansing, Michigan: Philosophy of Science Association, pp. 277–285.

[^albert-1991]: –––, 1991, “Some alleged solutions to the measurement problem,” *Synthese*, 88: 87–98.

[^albert-1993]: –––, 1993, “Non-ideal measurements,” *Foundations of Physics Letters*, 6: 297–305.

[^ardenghi-2009]: Ardenghi, J. S., M. Castagnino, and O. Lombardi, 2009, “Quantum mechanics: modal interpretation and Galilean transformations,” *Foundations of Physics*, 39: 1023–1045.

[^ardenghi-2013]: Ardenghi, J. S., O. Lombardi, and M. Narvaja, 2013, “Modal interpretations and consecutive measurements,” in *EPSA 2011: Perspectives and Foundational Problems in Philosophy of Science*, V. Karakostas, and D. Dieks (eds.), Berlin: Springer, pp. 207–217.

[^arntzenius-1990]: Arntzenius, F., 1990, “Kochen’s interpretation of quantum mechanics,” in *Proceedings of the PSA 1990*, Vol. 1, A. Fine, M. Forbes, and L. Wessels (eds.), East Lansing, Michigan: Philosophy of Science Association, pp. 241–249.

[^bacciagaluppi-1995]: Bacciagaluppi, G., 1995, “A Kochen-Specker theorem in the modal interpretation of quantum mechanics,” *International Journal of Theoretical Physics*, 34: 1205–1216.

[^bacciagaluppi-1996]: –––, 1996, *Topics in the Modal Interpretation of Quantum Mechanics*. Dissertation, Cambridge University.

[^bacciagaluppi-1998]: –––, 1998, “Bohm-Bell dynamics in the modal interpretation,” in *The Modal Interpretation of Quantum Mechanics*, D. Dieks and P. Vermaas (eds.), Dordrecht: Kluwer Academic Publishers, pp. 177–211.

[^bacciagaluppi-2000]: –––, 2000, “Delocalized properties in the modal interpretation of a continuous model of decoherence,” *Foundations of Physics*, 30: 1431–1444.

[^bacciagaluppi-1999]: Bacciagaluppi, G. and M. Dickson, 1999, “Dynamics for modal interpretations,” *Foundations of Physics*, 29: 1165–1201.

[^bacciagaluppi-1995-2]: Bacciagaluppi, G., M. Donald, and P. Vermaas, 1995, “Continuity and discontinuity of definite properties in the modal interpretation,” *Helvetica Physica Acta*, 68: 679–704.

[^bacciagaluppi-1994]: Bacciagaluppi, G. and M. Hemmo, 1994, “Making sense of approximate decoherence,” in *Proceedings of the PSA 1994*, Vol. 1, D. Hull, M. Forbes, and R. Burian (eds.), East Lansing, Michigan: Philosophy of Science Association, pp. 345–354.

[^bacciagaluppi-1996-2]: –––, 1996, “Modal interpretations, decoherence and measurements,” *Studies in History and Philosophy of Modern Physics*, 27: 239–277.

[^ballentine-1998]: Ballentine, L., 1998, *Quantum Mechanics: A Modern Development*, Singapore: World Scientific.

[^barandes-2014a]: Barandes, J. and D. Kagan, 2014a, “A synopsis of the minimal modal interpretation of quantum theory,” *arXiv*: 1405.6754v3.

[^barandes-2014b]: –––, 2014b, “The minimal modal interpretation of quantum theory,” *arXiv*: 1405.6755v3.

[^barandes-2020]: –––, 2020, “Measurement and quantum dynamics in the minimal modal interpretation of quantum theory,” *Foundations of Physics*, 50: 1189–1218.

[^bell-1984]: Bell, J. S., 1984, “Beables for quantum field theory,” in *Speakable and Unspeakable in Quantum Mechanics* (1987), Cambridge: Cambridge University Press, pp. 173–180.

[^bene-1997]: Bene, G., 1997, “Quantum reference systems: A new framework for quantum mechanics,” *Physica A*, 242: 529–565.

[^bene-2002]: Bene, G. and D. Dieks, 2002, “A perspectival version of the modal interpretation of quantum mechanics and the origin of macroscopic behavior,” *Foundations of Physics*, 32: 645–671.

[^berkovitz-2005]: Berkovitz, J. and M. Hemmo, 2005, “Can modal interpretations of quantum mechanics be reconciled with relativity?,” *Philosophy of Science*, 72: 789–801.

[^berkovitz-2006]: –––, 2006, “A new modal interpretation in terms of relational properties,” in *Physical Theory and its Interpretation: Essays in honor of Jeffrey Bub*, W. Demopoulos, and I. Pitowsky (eds.), New York: Springer, pp.1–28.

[^bohm-1952]: Bohm, D., 1952, “A suggested interpretation of the quantum theory in terms of ‘hidden’ variables, I and II,” *Physical Review*, 85: 166–193.

[^brown-1998]: Brown, H., M. Suárez, and G. Bacciagaluppi, 1998, “Are ‘sharp values’ of observables always objective elements of reality?,” in *The Modal Interpretation of Quantum Mechanics*, D. Dieks and P. Vermaas (eds.), Dordrecht: Kluwer Academic Publishers, pp. 69–101.

[^bub-1992]: Bub, J., 1992, “Quantum mechanics without the projection postulate,” *Foundations of Physics*, 22: 737–754.

[^bub-1994]: –––, 1994, “On the structure of quantal proposition systems,” *Foundations of Physics*, 24: 1261–1279.

[^bub-1997]: –––, 1997, *Interpreting the Quantum World*, Cambridge: Cambridge University Press.

[^bub-1996]: Bub, J. and R. Clifton, 1996, “A uniqueness theorem for interpretations of quantum mechanics,” *Studies in History and Philosophy of Modern Physics*, 27: 181–219.

[^bub-2000]: Bub, J., R. Clifton, and S. Goldstein, 2000, “Revised proof of the uniqueness theorem for ‘no collapse’ interpretations of quantum mechanics,” *Studies in History and Philosophy of Modern Physics*, 31: 95–98.

[^bueno-2014]: Bueno, O., 2014, “Constructive empiricism, partial structures and the modal interpretation of quantum mechanics,” *Quanta*, 3: 1–15.

[^calosi-2018]: Calosi, C., 2018, “Quantum monism: an assessment,” *Philosophical Studies*, 175: 3217–3236.

[^calosi-2022]: Calosi, C., 2022, “Quantum modal indeterminacy,” *Studies in History and Philosophy of Science*, 95: 177–184.

[^castagnino-2010]: Castagnino, M., S. Fortin, and O. Lombardi, 2010, “Is the decoherence of a system the result of its interaction with the environment?,” *Modern Physics Letters A*, 25: 1431–1439.

[^clifton-1995a]: Clifton, R., 1995a, “Independently motivating the Kochen-Dieks modal interpretation of quantum mechanics,” *The British Journal for the Philosophy of Science*, 46: 33–57.

[^clifton-1995b]: –––, 1995b, “Making sense of the Kochen-Dieks ‘no-collapse’ interpretation of quantum mechanics independent of the measurement problem,” *Annals of the New York Academy of Science*, 755: 570–578.

[^clifton-1995c]: –––, 1995c, “Why modal interpretations of quantum mechanics must abandon classical reasoning about the physical properties,” *International Journal of Theoretical Physics*, 34: 1302–1312.

[^clifton-1996]: –––, 1996, “The properties of modal interpretations of quantum mechanics,” *The British Journal for the Philosophy of Science*, 47: 371–398.

[^clifton-2000]: –––, 2000, “The modal interpretation of algebraic quantum field theory,” *Physics Letters A*, 271: 167–177.

[^cohen-1989]: Cohen, D. W., 1989, *An Introduction to Hilbert Space and Quantum Logic*, New York: Springer-Verlag.

[^da-2014]: Da Costa, N. and O. Lombardi, 2014, “Quantum mechanics: ontology without individuals,” *Foundations of Physics*, 44: 1246–1257.

[^de-1970]: De Witt, B. S. M., 1970, “Quantum mechanics and reality,” *Physics Today*, 23: 30–35.

[^dickson-1994]: Dickson, M., 1994, “Wavefunction tails in the modal interpretation,” in *Proceedings of the PSA 1994*, Vol. 1, D. Hull, M. Forbes, and R. Burian (eds.), East Lansing, Michigan: Philosophy of Science Association, pp. 366–376.

[^dickson-1995a]: –––, 1995a, “Faux-Boolean algebras, classical probability, and determinism,” *Foundations of Physics Letters*, 8: 231–242.

[^dickson-1995b]: –––, 1995b, “Faux-Boolean algebras and classical models,” *Foundations of Physics Letters*, 8: 401–415.

[^dickson-1998]: Dickson, M. and R. Clifton, 1998, “Lorentz-invariance in modal interpretations,” in *The Modal Interpretation of Quantum Mechanics*, D. Dieks and P. Vermaas (eds.), Dordrecht: Kluwer Academic Publishers, pp. 9–48.

[^dieks-1988]: Dieks, D., 1988, “The formalism of quantum theory: an objective description of reality?,” *Annalen der Physik*, 7: 174–190.

[^dieks-1989]: –––, 1989, “Resolution of the measurement problem through decoherence of the quantum state,” *Physics Letters A*, 142: 439–446.

[^dieks-1998]: –––, 1998, “Preferred factorizations and consistent property attribution”, in *Quantum Measurement: Beyond Paradox*, R. Healey and G. Hellman (eds.), Minneapolis: University of Minnesota Press, pp. 144–160.

[^dieks-2002]: –––, 2002, “Events and covariance in the interpretation of quantum field theory,” in *Ontological Aspects of Quantum Field Theory*, M. Kuhlmann, H. Lyre, and A. Wayne (eds.), Singapore: World Scientific, pp. 215–234.

[^dieks-2009]: –––, 2009, “Objectivity in perspective: relationism in the interpretation of quantum mechanics,” *Foundations of Physics*, 39: 760–775.

[^dieks-2017]: –––, 2017, “Niels Bohr and the formalism of quantum mechanics,” in J. Faye and H. J. Folse (eds.), *Niels Bohr and the Philosophy of Physics: Twenty-First-Century Perspectives*, London: Bloomsbury Academic, pp. 303–333.

[^dieks-2019]: –––, 2019, “Quantum mechanics and perspectivalism,” in O. Lombardi, S. Fortin, C. López, and F. Holik (eds.), *Quantum Worlds: Perspectives on the Ontology of Quantum Mechanics*, Cambridge: Cambridge University Press, pp. 51–70.

[^dieks-2022a]: –––, 2022a, “Modal interpretations of quantum mechanics,” in O. Freire (ed.), *Oxford Handbook of the History of Interpretations of Quantum Mechanics*, Oxford: Oxford University Press, Ch. 47.

[^dieks-2022b]: –––, 2022b, “Perspectival quantum realism,” *Foundations of Physics*, 52(95). doi:0.1007/s10701-022-00611-8

[^dieks-1998-2]: Dieks, D. and P. Vermaas (eds.), 1998, *The Modal Interpretation of Quantum Mechanics*, Dordrecht: Kluwer Academic Publishers.

[^donald-1998]: Donald, M., 1998, “Discontinuity and continuity of definite properties in the modal interpretation,” in *The Modal Interpretation of Quantum Mechanics*, D. Dieks and P. Vermaas (eds.), Dordrecht: Kluwer Academic Publishers, pp. 213–222.

[^earman-2005]: Earman, J. and L. Ruetsche, 2005, “Relativistic invariance and modal interpretations,” *Philosophy of Science*, 72: 557–583.

[^elby-1993]: Elby, A., 1993, “Why ‘modal’ interpretations of quantum mechanics don’t solve the measurement problem,” *Foundations of Physics Letters*, 6: 5–19.

[^everett-1957]: Everett, H., 1957, “*Relative state* formulation of quantum mechanics,” *Review of Modern Physics*, 29: 454–462.

[^fortin-2018]: Fortin, S., O. Lombardi, and J. C. Martínez González, 2018, “A new application of the modal-Hamiltonian interpretation of quantum mechanics: the problem of optical isomerism,” *Studies in History and Philosophy of Modern Physics*, 62: 123–135.

[^frauchiger-2018]: Frauchiger, D. and R. Renner, 2018, “Quantum theory cannot consistently describe the use of itself,” *Nature Communications*, 9: 3711.

[^french-2006]: French, S. and D. Krause, 2006, *Identity in Physics: A Historical, Philosophical and Formal Analysis*, Oxford: Oxford University Press.

[^gambetta-2003]: Gambetta, J. and H. M. Wiseman, 2003, “Interpretation of non-Markovian stochastic Schrödinger equations as a hidden-variable theory,” *Physical Review A*, 68: 062104.

[^gambetta-2004]: –––, 2004, “Modal dynamics for positive operator measures,” *Foundations of Physics*, 34: 419–448.

[^healey-1989]: Healey, R., 1989, *The Philosophy of Quantum Mechanics: An Interactive Interpretation*, Cambridge: Cambridge University Press.

[^hemmo-2005]: Hemmo, M. and J. Berkovitz, 2005, “Modal interpretations of quantum mechanics and relativity: a reconsideration,” *Foundations of Physics*, 35: 373–397.

[^hollowood-2013a]: Hollowood, T., 2013a, “The Copenhagen interpretation as an emergent phenomenon,” *Journal of Physics A: Mathematical and Theoretical*, 46: 325302.

[^hollowood-2013b]: –––, 2013b, “New modal quantum mechanics,” *arXiv*: 1312.4751v1.

[^hollowood-2014]: –––, 2014, “The emergent Copenhagen interpretation of quantum mechanics,” *Journal of Physics A: Mathematical and Theoretical*, 47: 18530.

[^hughes-1989]: Hughes, R. I. G., 1989, *The Structure and Interpretation of Quantum Mechanics*, Cambridge. Massachusetts: Harvard University Press.

[^kitajima-2004]: Kitajima, Y., 2004, “A remark on the modal interpretation of algebraic quantum field theory,” *Physics Letters A*, 331: 181–186.

[^kochen-1985]: Kochen, S., 1985, “A new interpretation of quantum mechanics,” in *Symposium on the Foundations of Modern Physics 1985*, P. Mittelstaedt and P. Lahti (eds.), Singapore: World Scientific, pp. 151–169.

[^kochen-1967]: Kochen, S. and E. Specker, 1967, “The problem of hidden variables in quantum mechanics,” *Journal of Mathematics and Mechanics*, 17: 59–87.

[^ladyman-1998]: Ladyman, J., 1998, “What is structural realism?,” *Studies in History and Philosophy of Science*, 29: 409–424.

[^laudisa-2021]: Laudisa, F. and C. Rovelli, 2021, “Relational quantum mechanics,” in *The Stanford Encyclopedia of Philosophy*, Spring 2021 Edition, Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/spr2021/entries/qm-relational/](https://plato.stanford.edu/archives/spr2021/entries/qm-relational/)>.

[^lombardi-2025]: Lombardi, O., 2025, *The Modal-Hamiltonian Interpretation of Quantum Mechanics*, Oxford: Oxford University Press.

[^lombardi-2011]: Lombardi, O., J. S. Ardenghi, S. Fortin, and M. Castagnino, 2011, “Compatibility between environment-induced decoherence and the modal-Hamiltonian interpretation of quantum mechanics,” *Philosophy of Science*, 78: 1024–1036.

[^lombardi-2008]: Lombardi, O. and M. Castagnino, 2008, “A modal-Hamiltonian interpretation of quantum mechanics,” *Studies in History and Philosophy of Modern Physics*, 39: 380–443.

[^lombardi-2010]: Lombardi, O., M. Castagnino, and J. S. Ardenghi, 2010, “The modal-Hamiltonian interpretation and the Galilean covariance of quantum mechanics,” *Studies in History and Philosophy of Modern Physics*, 41: 93–103.

[^lombardi-2016]: Lombardi, O. and D. Dieks, 2016, “Particles in a quantum ontology of properties,” in *Metaphysics in Contemporary Physics*, T. Bigaj, and C. Wüthrich (eds.), Leiden: Brill-Rodopi, pp. 123–143.

[^maudlin-1995]: Maudlin, T., 1995, “Three measurement problems,” *Topoi*, 14: 7–15.

[^menzel-2018]: Menzel, C., 2018, “Actualism,” in *The Stanford Encyclopedia of Philosophy*, Summer 2018 Edition, Edward N. Zalta (ed.), URL=<[https://plato.stanford.edu/archives/sum2018/entries/actualism/](https://plato.stanford.edu/archives/sum2018/entries/actualism/)>).

[^myrvold-2002]: Myrvold, W., 2002, “Modal interpretations and relativity,” *Foundations of Physics*, 32: 1773–1784.

[^myrvold-2018]: –––, 2018, “Philosophical issues in quantum theory,” in *The Stanford Encyclopedia of Philosophy*, Fall 2018 Edition, Edward N. Zalta (ed.), URL=<[https://plato.stanford.edu/archives/fall2018/entries/qt-issues/](https://plato.stanford.edu/archives/fall2018/entries/qt-issues/)>).

[^nakayama-2008a]: Nakayama, K., 2008a, “Reformulation of a modal interpretation of quantum mechanics in the topos M-set,” *Ryokoku Journal of Humanities and Sciences*, 29: 159–168.

[^nakayama-2008b]: –––, 2008b, “Topos-theoretic extension of a modal interpretation of quantum mechanics,” *International Journal of Theoretical Physics*, 47: 2065–2094.

[^oldofredi-2021]: Oldofredi, A., 2021, “The bundle theory approach to relational quantum mechanics,” *Foundations of Physics*, 51: 1–22.

[^oldofredi-2020]: Oldofredi, A. and C. López, 2020, “On the classification between ${\psi}$-ontic and ${\psi}$-epistemic ontological models,” *Foundations of Physics*, 50: 1315–1345.

[^reeder-1995]: Reeder, N. and R. Clifton, 1995, “Uniqueness of prime factorizations of linear operators in quantum mechanics,” *Physics Letters A*, 204: 198–204.

[^rossanese-2023]: Rossanese, E., 2023, “Reconsidering an ontology of properties for quantum theories,” *Argumenta*, 8: 427–442

[^rovelli-1996]: Rovelli, C., 1996, “Relational quantum mechanics,” *International Journal of Theoretical Physics*, 35: 1637–1678.

[^rovelli-2007]: Rovelli, C. and M. Smerlak, 2007, “Relational EPR,” *Foundations of Physics*, 37: 427–445.

[^ruetsche-1995]: Ruetsche, L., 1995, “Measurement error and the Albert-Loewer problem,” *Foundations of Physics Letters*, 8: 327–344.

[^ruetsche-1996]: –––, 1996, “Van Fraassen on preparation and measurement,” *Philosophy of Science*, 63: S338–S346.

[^ruetsche-2003]: –––, 2003, “Modal semantics, modal dynamics and the problem of state preparation,” *International Studies in the Philosophy of Science*, 17: 25–41.

[^schlosshauer-2007]: Schlosshauer, M., 2007, *Decoherence and the Quantum-to-Classical Transition*, Heidelberg-Berlin: Springer.

[^schrödinger-1935]: Schrödinger, E., 1935, “Discussion of probability relations between separated systems,” *Proceedings of the Cambridge Philosophical Society*, 31: 555–563.

[^suárez-2004]: Suárez, M., 2004, “Quantum selections, propensities and the problem of measurement,” *The British Journal for the Philosophy of Science*, 55: 219–255.

[^sudbery-2002]: Sudbery, A., 2002, “Diese verdammte Quantenspringerei,” *Studies in History and Philosophy of Modern Physics*, 33: 387–411.

[^fraassen-1972]: van Fraassen, B. C., 1972, “A formal approach to the philosophy of science,” in *Paradigms and Paradoxes: The Philosophical Challenge of the Quantum Domain*, R. Colodny (ed.), Pittsburgh: University of Pittsburgh Press, pp. 303–366.

[^fraassen-1974]: –––, 1974, “The Einstein-Podolsky-Rosen paradox,” *Synthese*, 29: 291–309.

[^fraassen-1991]: –––, 1991, *Quantum Mechanics*, Oxford: Clarendon Press.

[^fraassen-1997]: –––, 1997, “Modal interpretation of repeated measurement: A rejoinder to Leeds and Healey,” *Philosophy of Science*, 64: 669–676.

[^fraassen-2010]: –––, 2010, “Rovelli’s world,” *Foundations of Physics*, 40: 390–417.

[^vermaas-1996]: Vermaas, P., 1996, “Unique transition probabilities in the modal interpretation,” *Studies in History and Philosophy of Modern Physics*, 27: 133–159.

[^vermaas-1997]: –––, 1997, “A no-go theorem for joint property ascriptions in modal interpretations of quantum mechanics,” *Physical Review Letters*, 78: 2033–2037.

[^vermaas-1998]: –––, 1998, “The pros and cons of the Kochen-Dieks and the atomic modal interpretation,” in *The Modal Interpretation of Quantum Mechanics*, D. Dieks and P. Vermaas (eds.), Dordrecht: Kluwer Academic Publishers, pp. 103–148.

[^vermaas-1999]: –––, 1999, *A Philosopher’s Understanding of Quantum Mechanics: Possibilities and Impossibilities of a Modal Interpretation*, Cambridge: Cambridge University Press.

[^vermaas-1995]: Vermaas, P. and D. Dieks, 1995, “The modal interpretation of quantum mechanics and its generalization to density operators,” *Foundations of Physics*, 25: 145–158.

[^vink-1993]: Vink, J., 1993, “Quantum mechanics in terms of discrete beables,” *Physical Review A*, 48: 1808–1818.

[^zurek-1981]: Zurek, W. H., 1981, “Pointer basis of quantum apparatus: into what mixtures does the wave packet collapse?,” *Physical Review D*, 24: 1516–1525.

[^zurek-2003]: –––, 2003, “Decoherence, einselection, and the quantum origins of the classical,” *Reviews of Modern Physics*, 75: 715–776.
