# Philosophical Issues in Quantum Theory
**First published Mon Jul 25, 2016; substantive revision Wed Mar 23, 2022**

*Myrvold, Wayne*

This article is an overview of the philosophical issues raised by quantum theory, intended as a pointer to the more in-depth treatments of other entries in the Stanford Encyclopedia of Philosophy.

## 1. Introduction

Despite its status as a core part of contemporary physics, there is no consensus among physicists or philosophers of physics on the question of what, if anything, the empirical success of quantum theory is telling us about the physical world. This gives rise to the collection of philosophical issues known as “the interpretation of quantum mechanics”. One should not be misled by this terminology into thinking that what we have is an uninterpreted mathematical formalism with no connection to the physical world. Rather, there is a common operational core that consists of recipes for calculating probabilities of outcomes of experiments performed on systems subjected to certain state preparation procedures. What are often referred to as different “interpretations” of quantum mechanics differ on what, if anything, is added to the common core. Two of the major approaches, hidden-variables theories and collapse theories, involve formulation of physical theories distinct from standard quantum mechanics; this renders the terminology of “interpretation” even more inappropriate.

Much of the philosophical literature connected with quantum theory centers on the problem of whether we should construe the theory, or a suitable extension or revision of it, in realist terms, and, if so, how this should be done. Various approaches to what is called the “Measurement Problem” propose differing answers to these questions. There are, however, other questions of philosophical interest. These include the bearing of quantum nonlocality on our understanding of spacetime structure and causality, the question of the ontological character of quantum states, the implications of quantum mechanics for information theory, and the task of situating quantum theory with respect to other theories, both actual and hypothetical. In what follows, we will touch on each of these topics, with the main goal being to provide an entry into the relevant literature, including the Stanford Encyclopedia entries on these topics. Contemporary perspectives on many of the issues touched on in this entry can be found in *The Routledge Companion to Philosophy of Physics* (Knox and Wilson, eds., 2021)[^knox-2021]; *The Oxford Handbook of the History of Quantum Interpretations* (Freire, et al. eds., 2022)[^freire-2022] contains essays on the history of discussions of these issues.

## 2. Quantum Theory

In this section we present a brief introduction to quantum theory; see the entry on quantum mechanics for a more detailed introduction.

### 2.1 Quantum states and classical states

In classical physics, with any physical system is associated a state space, which represents the totality of possible ways of assigning values to the dynamical variables that characterize the state of the system. For systems of a great many degrees of freedom, a complete specification of the state of the system may be unavailable or unwieldy; classical statistical mechanics deals with such a situation by invoking a probability distribution over the state space of the system. A probability distribution that assigns any probability other than one or zero to some physical quantities is regarded as an incomplete specification of the state of the system. In quantum mechanics, things are different. There are no quantum states that assign definite values to all physical quantities, and probabilities are built into the standard formulation of the theory.

In formulating a quantum theory of some system, one usually begins with the Hamiltonian or Lagrangian formulation of the classical mechanical theory of that system. In the Hamiltonian formulation of classical mechanics, the configuration of a system is represented by a set of coordinates. These could be, for example, the positions of each of a set of point particles, but one can also consider more general cases, such as angular coordinates that specify the orientation of a rigid body. For every coordinate there is an associated *conjugate momentum*. If the coordinate indicates the position of some object, the momentum conjugate to that coordinate may be what we usually call “momentum,” that is, the velocity of the body multiplied by its mass. If the coordinate is an angle, the momentum conjugate to it is an angular momentum.

Construction of a quantum theory of a physical system proceeds by first associating the dynamical degrees of freedom with *operators*. These are mathematical objects on which operations of multiplication and addition are defined, as well as multiplication by real and complex numbers. Another way of saying this is that the set of operators forms an *algebra*. Typically, it is said that an operator represents an *observable*, and the result of an experiment on a system is said to yield a value for some observable. Two or more observables are said to be *compatible* if there is some possible experiment that simultaneously yields values for all of them. Others require mutually exclusive experiments; these are said to be *incompatible*.

Of course, in a classical theory, the dynamical quantities that define a state also form an algebra also, as they can be multiplied and added, and multiplied by real or complex numbers. Quantum mechanics differs from classical mechanics in that the order of multiplication of operators can make a difference. That is, for some operators $A$,$B$, the product $AB$ is not equal to the product $BA.$ If $AB = BA,$ the operators are said to *commute*.

The recipe for constructing a quantum theory of a given physical systems prescribes algebraic relations between the operators representing the dynamical variables of the system. Compatible observables are associated with operators that commute with each other. Operators representing conjugate variables are required to satisfy what are called the *canonical commutation relations*. If $q$ is some coordinate, and $p$ its conjugate momentum, the operators $Q$ and $P$ representing them are required to not commute. Instead, the difference between $PQ$ and $QP$ is required to be a multiple of the identity operator (that is, the operator $I$ that satisfies, for all operators $A$, $IA = AI).$

A *quantum state* is a specification, for every experiment that can be performed on the system, of probabilities for the possible outcomes of that experiment. These can be summed up as an assignment of an expectation value to each observable. These states are required to be *linear*. This means that, if an operator $C$, corresponding to some observable, is the sum of operators $A$ and $B$, corresponding to other observables, then the expectation value that a quantum state assigns to $C$ must be the sum of the expectation values assigned to $A$ and $B$. This is a nontrivial constraint, as it is required to hold whether or not the observables represented are compatible. A quantum state, therefore, relates expectation values for quantities yielded by incompatible experiments.

Incompatible observables, represented by noncommuting operators, give rise to uncertainty relations; see the entry on the uncertainty principle. These relations entail that there are no quantum states that assign definite values to the observables that satisfy them, and place bounds on how close they can come to be simultaneously well-defined in any quantum state.

For any two distinct quantum states, *ρ*, *ω*, and any real number between 0 and 1, there is a corresponding *mixed state*. The probability assigned to any experimental outcome by this mixed state is $p$ times the probability it is assigned by *ρ* plus $1-p$ times the probability assigned to it by *ω*. One way to physically realize the preparation of a mixed state is to employ a randomizing device, for example, a coin with probability $p$ of landing heads and probability $1-p$ of landing tails, and to use it to choose between preparing state *ρ* and preparing state *ω*. We will see another way to prepare a mixed state after we have discussed entanglement, in section 3. A state that is not a mixture of any two distinct states is called a *pure state*.

It is both useful and customary, though not strictly necessary, to employ a *Hilbert space* representation of a quantum theory. In such a representation, the operators corresponding to observables are represented as acting on elements of an appropriately constructed Hilbert space (see the entry on quantum mechanics for details). Usually, the Hilbert space representation is constructed in such a way that vectors in the space represent pure states; such a representation is called an *irreducible representation*. Irreducible representations, in which mixed states are also represented by vectors, are also possible.

A Hilbert space is a vector space. This means that, for any two vectors $|\psi\rangle$, $|\phi\rangle$ , in the space, representing pure states, and any complex numbers $a$, $b$, there is another vector, $a |\psi\rangle + b |\phi\rangle$, that also represents a pure state. This is called a *superposition* of the states represented by $|\psi\rangle$ and $|\phi\rangle$ . Any vector in a Hilbert space can be written as a superposition of other vectors in infinitely many ways. Sometimes, in discussing the foundations of quantum mechanics, authors fall into talking as if some state are superpositions and others are not. This is simply an error. Usually what is meant is that some states yield definite values for macroscopic observables, and others cannot be written in any way that is not a superposition of macroscopically distinct states.

The noncontroversial operational core of quantum theory consists of rules for identifying, for any given system, appropriate operators representing its dynamical quantities. In addition, there are prescriptions for evolving the state of system when it is acted upon by specified external fields or subjected to various manipulations (see section 1.3). Application of quantum theory typically involves a distinction between the system under study, which is treated quantum mechanically, and experimental apparatus, which is not. This division is sometimes known as the *Heisenberg cut*.

Whether or not we can expect to be able to go beyond the noncontroversial operational core of quantum theory, and take it to be more than a means for calculating probabilities of outcomes of experiments, remains a topic of contemporary philosophical discussion.

### 2.2 Quantum mechanics and quantum field theory

*Quantum mechanics* is usually taken to refer to the quantized version of a theory of classical mechanics, involving systems with a fixed, finite number of degrees of freedom. Classically, a field, such as, for example, an electromagnetic field, is a system endowed with infinitely many degrees of freedom. Quantization of a field theory gives rise to a *quantum field theory*. The chief philosophical issues raised by quantum mechanics remain when the transition is made to a quantum field theory; in addition, new interpretational issues arise. There are interesting differences, both technical and interpretational, between quantum mechanical theories and quantum field theories; for an overview, see the entries on quantum field theory and quantum theory: von Neumann vs. Dirac.

The standard model of quantum field theory, successful as it is, does not yet incorporate gravitation. The attempt to develop a theory that does justice both the quantum phenomena and to gravitational phenomena gives rise to serious conceptual issues (see the entry on quantum gravity).

### 2.3 Quantum state evolution

#### 2.3.1 Schrödinger and Heisenberg pictures

When constructing a Hilbert space representation of a quantum theory of a system that evolves over time, there are some choices to be made. One needs to have, for each time *t*, a Hilbert space representation of the system, which involves assigning operators to observables pertaining to time *t*. An element of convention comes in when deciding how the operators representing observables at different times are to be related.

For concreteness, suppose that have a system whose observables include a position, $x$, and momentum, $p$, with respect to some frame of reference. There is a sense in which, for two distinct times, $t$ and $t'$, *position at time* $t$ and *position at time* $t'$ are distinct observables, and also a sense in which they are values, at different times, of the same observable. Once we have settled on operators $\hat{X}$ and $\hat{P}$ to represent position and momentum at time $t$, we still have a choice of which operators represent the corresponding quantities at time $t.$ On the *Schrödinger picture*, the same operators $\hat{X}$ and $\hat{P}$ are used to represent position and momentum, whatever time is considered. As the probabilities for results of experiments involving these quantities may be changing with time, different vectors must be used to represent the state at different times.

The equation of motion obeyed by a quantum state vector is the *Schrödinger equation.* It is constructed by first forming the operator $\hat{H}$corresponding to the Hamiltonian of the system, which represents the total energy of the system. The rate of change of a state vector is proportional to the result of operating on the vector with the Hamiltonian operator $\hat{H}$.

$$ i \hbar {\,\D}/{\D t}\, \ket{\psi (t)} = \hat{H} \ket{\psi (t)}. $$

There is an operator that takes a state at time 0 into a state at time $t$; it is given by

$$ U(t) = \exp\left(\frac{{-}i H t}{\hbar}\right). $$

This operator is a linear operator that implements a one-one mapping of the Hilbert space to itself that preserves the inner product of any two vectors; operators with these properties are called *unitary operators*, and, for this reason, evolution according to the Schrödinger equation is called *unitary evolution.*

For our purposes, the most important features of this equation is that it is *deterministic* and *linear*. The state vector at any time, together with the equation, uniquely determines the state vector at any other time. Linearity means that, if two vectors $\ket{\psi_1(0)}$ and $\ket{\psi_2(0)}$ evolve into vectors $\ket{\psi_1(t) }$ and $\ket{\psi_2(t)}$, respectively, then, if the state at time 0 is a linear combination of these two, the state at any time $t$ will be the corresponding linear combination of $\ket{\psi_1(t)}$ and $\ket{\psi_2(t)}$.

$$ a\ket{\psi_{1}(0)} + b\ket{\psi_{2}(0)} \rightarrow a\ket{\psi_{1}(t)} + b\ket{\psi_{2}(t)} . $$

The Heisenberg picture, on the other hand, employs different operators $\hat{X}(t)$, $\hat{X}(t')$ for position, depending on the time considered (and similarly for momentum and other observables). If $\hat{A}(t)$is a family of Heisenberg picture operators representing some observable at different times, the members of the family satisfy the Heisenberg equation of motion,

$$ i \hbar d/dt \; \hat{A}(t) = \hat{A}(t) \hat{H} - \hat{H} \hat{A}(t). $$

One sometimes hears it said that, on the Heisenberg picture, the state of the system is unchanging. This is incorrect. It is true that there are not different state vectors corresponding to different times, but that is because a single state vector serves for computing probabilities for all observables pertaining to all times. These probabilities *do* change with time.

#### 2.3.2. The collapse postulate

As mentioned, standard applications of quantum theory involve a division of the world into a system that is treated within quantum theory, and the remainder, typically including the experimental apparatus, that is not treated within the theory. Associated with this division is a postulate about how to assign a state vector after an experiment that yields a value for an observable, according to which, after an experiment, one replaces the quantum state with an eigenstate corresponding to the value obtained. Unlike the unitary evolution applied otherwise, this is a discontinuous change of the quantum state, sometimes referred to as *collapse of the state vector*, or *state vector reduction*. There are two interpretations of the postulate about collapse, corresponding to two different conceptions of quantum states. If a quantum state represents nothing more than knowledge about the system, then the collapse of the state to one corresponding to an observed result can be thought of as mere updating of knowledge. If, however, quantum states represent physical reality, in such a way that distinct pure states always represent distinct physical states of affairs, then the collapse postulate entails an abrupt, perhaps discontinuous, change of the physical state of the system. Considerable confusion can arise if the two interpretations are conflated.

The collapse postulate occurs already in the general discussion at the fifth Solvay Conference in 1927 (see Bacciagaluppi and Valentini, 2009, 437–450)[^bacciagaluppi-2009]. It is also found in Heisenberg’s *The Physical Principles of the Quantum Theory*, based on lectures presented in 1929 (Heisenberg, 1930a, 27; 1930b, 36)[^heisenberg-1930a]. Von Neumann, in his reformulation of quantum theory a few years later, distinguished between two types of processes: Process 1:, which occurs upon performance of an experiment, and Process 2:, the unitary evolution that takes place as long as no measurement is made (von Neumann, 1932; 1955, §V.I)[^neumann-1932]. He does not take this distinction to be a difference between two physically distinct processes. Rather, the invocation of one process or the other depends on a somewhat arbitrary division of the world into an observing part and an observed part (see von Neumann,1932, 224; 1955, 420)[^neumann-1932].

The collapse postulate does not appear in the first edition (1930) of Dirac’s *Principles of Quantum Mechanics*; it is introduced in the second edition (1935). Dirac formulates it as follows.

> When we measure a real dynamical variable *ξ*, the disturbance involved in the act of measurement causes a jump in the state of the dynamical system. From physical continuity, if we make a second measurement of the same dynamical variable *ξ* immediately after the first, the result of the second measurement must be the same as that of the first. Thus after the first measurement has been made, there is no indeterminacy in the result of the second. Hence, after the first measurement has been made, the system is in an eigenstate of the dynamical variable *ξ*, the eigenvalue it belongs to being equal to the result of the first measurement. This conclusion must still hold if the second measurement is not actually made. In this way we see that a measurement always causes the system to jump into an eigenstate of the dynamical variable that is being measured, the eigenvalue this eigenstate belongs to being equal to the result of the measurement (Dirac 1935: 36)[^dirac-1935].

Unlike von Neumann and Heisenberg, Dirac is treating the “jump” as a physical process.

Neither von Neumann nor Dirac take awareness of the result by a conscious observer to be a necessary condition for collapse. For von Neumann, the location of the cut between the “observed” system and the “observer”is somewhat arbitrary. It may be placed between the system under study and the experimental apparatus. On the other hand, we could include the experimental apparatus in the quantum description, and place the cut at the moment when light indicating the result hits the observer’s retina. We could also go even further, and include the retina and relevant parts of the observer’s nervous system in the quantum system. That the cut may be pushed arbitrarily far into the perceptual apparatus of the observer is required, according to von Neumann, by the *principle of psycho-physical parallelism*.

A formulation of a version of the collapse postulate according to which a measurement is not completed until the result is observed is found in London and Bauer (1939). For them, as for Heisenberg, this is a matter of an increase of knowledge on the part of the observer.

Wigner (1961) combined elements of the two interpretations. Like those who take the collapse to be a matter of updating of belief in light of information newly acquired by an observer, he takes collapse to take place when a conscious observer becomes aware of an experimental result. However, like Dirac, he takes it to be a real physical process. His conclusion is that consciousness has an influence on the physical world not captured by the laws of quantum mechanics. This involves a rejection of von Neumann’s principle of psycho-physical parallelism, according to which it must be possible to treat the process of subjective perception as if it were a physical process like any other.

There is a persistent misconception that, for von Neumann, collapse is to be invoked only when a conscious observer becomes aware of the result. As noted, this is the opposite of his view, as the cut may be placed between the observed system and the experimental apparatus, and it is for him an important point that the location of the cut be somewhat arbitrary. In spite of this, von Neumann’s position is sometimes conflated with Wigner’s speculative proposal, and Wigner’s proposal is sometimes erroneously referred to as the *von Neumann-Wigner interpretation*.

None of the standard formulations are precise about when the collapse postulate is to be applied; there is some lee-way as to what is to count as an experiment, or (for versions that require reference to an observer) what is to count as an observer. Some, including von Neumann and Heisenberg, have taken it to be a matter of principle that there be some arbitrariness in where to apply the postulate. It is common wisdom that, in practice, this arbitrariness is innocuous. The rule of thumb that seems to be applied, in practice, in setting the split between the parts of the world treated quantum-mechanically and things treated as classical objects has been formulated by J. S. Bell as, “[w]hen in doubt enlarge the quantum system,” to the point at which including more in the quantum system makes negligible difference to practical predictions (Bell 1986, 362; Bell 2004, 189)[^bell-1986][^bell-2004]. If anything is to be counted as “standard” quantum mechanics, it is the operational core we have discussed, supplemented by a heuristic rule of application of this sort. Standard quantum mechanics works very well. If, however, one seeks a theory that is capable of describing all systems, including macroscopic ones, and can yield an account of the process by which macroscopic events, including experimental outcomes, come about, this gives rise to the so-called “measurement problem”, which we will discuss after we have introduced the notion of entanglement (see section 3).

#### 2.3.3. Wave functions

Among the Hilbert-space representations of a quantum theory are *wave-function* representations.

Associated with any observable is its *spectrum*, the range of possible values that the observable can take on. Given any physical system and any observable for that system, one can always form a Hilbert-space representation for the quantum theory of that system by considering complex-valued functions on the spectrum of that observable. The set of such functions form a vector space. Given a measure on the spectrum of the observable, we can form a Hilbert space out of the set of complex-valued square-integrable functions on the spectrum by treating functions that differ only on a set of zero measure as equivalent (that is, the elements of our Hilbert space are really equivalence classes of functions), and by using the measure to define an inner product (see entry on Quantum Mechanics if this terminology is unfamiliar).

If the spectrum of the chosen observable is a continuum (as it is, for example, for position or momentum), a Hilbert-space representation of this sort is called a *wave function* representation, and the functions that represent quantum states, *wave functions* (also “wave-functions,” or “wavefunctions”). The most familiar representations of this form are position-space wave functions, which are functions on the set of possible configurations of the system, and momentum-space wave functions, which are functions of the momenta of the systems involved.

## 3. Entanglement, nonlocality, and nonseparability

Given two disjoint physical systems, $A$ and $B$, with which we associate Hilbert spaces $H_{A}$ and $H_{B}$, the Hilbert space associated with the composite system is the tensor product space, denoted $H_{A} \otimes H_{B}$.

When the two systems are independently prepared in pure states $\ket{\psi}$ and $\ket{\phi}$, the state of the composite system is the *product state* $\ket{\psi} \otimes \ket{\phi}$ (sometimes written with the cross, $\otimes$, omitted).

In addition to the product states, the tensor product space contains linear combinations of product states, that is, state vectors of the form

$$ a\ket{\psi_{1}} \otimes \ket{\phi_{1}} + b\ket{\psi_{2}} \otimes \ket{\phi_{2}} $$

The tensor product space can be defined as the smallest Hilbert space containing all of the product states. Any pure state represented by a state vector that is not a product vector is an *entangled state*.

The state of the composite system assigns probabilities to outcomes of all experiments that can be performed on the composite system. We can also consider a restriction to experiments performed on system $A$, or a restriction to experiments performed to $B$. Such restrictions yields states of $A$ and $B$, respectively, called the *reduced states* of the systems. When the state of the composite system $AB$ is an entangled state, then the reduced states of $A$ and $B$ are mixed states. To see this, suppose that in the above state the vectors $\ket{\phi_{1}}$ and $\ket{\phi_{2}}$ represent distinguishable states. If one confines one’s attention to experiments performed on $A$, it makes no difference whether an experiment is also performed on $B$. An experiment performed on $B$ that distinguishes $\ket{\phi_{1}}$ and $\ket{\phi_{2}}$ projects the state of $A$ into either $\ket{\psi_{1}}$ or $\ket{\psi_{2}}$, with probabilities $\abs{a}^{2}$ and $\abs{b}^{2}$, respectively, and probabilities for outcomes of experiments performed on $A$ are the corresponding averages of probabilities for states $\ket{\psi_{1}}$ and $\ket{\psi_{2}}$. These probabilities, as mentioned, are the same as those for the situation in which no experiment is performed on $B$. Thus, even if no experiment is performed on $B$, the probabilities of outcomes of experiments on $A$ are exactly as if system $A$ is either in the state represented by $\ket{\psi_{1}}$ or the state represented by $\ket{\psi_{2}}$, with probabilities $\abs{a}^{2}$ and $\abs{b}^{2}$, respectively.

In general, any state, pure or mixed, that is neither a product state nor a mixture of product states, is called an *entangled state.*

The existence of pure entangled states means that, if we consider a composite system consisting of spatially separated parts, then, even when the state of the system is a pure state, the state is not determined by the reduced states of its component parts. Thus, quantum states exhibit a form of *nonseparability*. See the entry on holism and nonseparability in physics for more information.

Quantum entanglement results in a form of nonlocality that is alien to classical physics. Even if we assume that the reduced states of $A$ and $B$ do not completely characterize their physical states, but must be supplemented by some further variables, there are quantum correlations that cannot be reduced to correlations between states of $A$ and $B$; see the entry on Bell’s Theorem.

## 4. The measurement problem

### 4.1 The measurement problem formulated

If quantum theory is meant to be (in principle) a universal theory, it should be applicable, in principle, to all physical systems, including systems as large and complicated as our experimental apparatus. It is easy to show that linear evolution of quantum states, when applied to macroscopic objects, will routinely lead to superpositions of macroscopically distinct states. Among the circumstances in which this will happen are experimental set-ups, and much of the early discussions focussed on how to construe the process of measurement in quantum-mechanical terms. For this reason, the interpretational issues have come to be referred to as the *measurement problem*. In the first decades of discussion of the foundations of quantum mechanics, it was commonly referred to as the *problem of observation*.

Consider a schematized experiment. Suppose we have a quantum system that can be prepared in at least two distinguishable states, $\ket{0} _{S}$ and $\ket{1} _{S}$. Let $\ket{R} _{A}$ be a ready state of the apparatus, that is, a state in which the apparatus is ready to make a measurement.

If the apparatus is working properly, and if the measurement is a minimally disturbing one, the coupling of the system $S$ with the apparatus $A$ should result in an evolution that predictably yields results of the form

$$ \ket{0} _{S} \ket{R} _{A} \Rightarrow \ket{0} _{S}\ket{“0” } _{A} $$ $$ \ket{1} _{S} \ket{R} _{A} \Rightarrow \ket{1} _{S}\ket{“1”} _{A} $$

where $\ket{“0” } _{A}$ and $\ket{“1”} _{A}$ are apparatus states indicating results 0 and 1, respectively.

Now suppose that the system $S$ is prepared in a superposition of the states $\ket{0} _{S}$ and $\ket{1}_{S}$.

$$ \ket{\psi(0)} _{S} = a\ket{0} _{S} + b\ket{1} _{S}, $$

where $a$ and $b$ are both nonzero. If the evolution that leads from the pre-experimental state to the post-experimental state is linear Schrödinger evolution, then we will have

$$ \ket{\psi(0)} _{S} \ket{R} _{A} \rightarrow a\ket{0} _{S} \ket{“0” } _{A} + b\ket{1} _{S}\ket{“1” } _{A}. $$

This is not an eigenstate of the instrument reading variable, but is, rather, a state in which the reading variable and the system variable are entangled with each other. The eigenstate-eigenvalue link, applied to a state like this, does not yield a definite result for the instrument reading. The problem of what to make of this is called the “measurement problem” which is discussed in more detail below.

### 4.2 Approaches to the measurement problem

If quantum state evolution proceeds via the Schrödinger equation or some other linear equation, then, as we have seen in the previous section, typical experiments will lead to quantum states that are superpositions of terms corresponding to distinct experimental outcomes. It is sometimes said that this conflicts with our experience, according to which experimental outcome variables, such as pointer readings, always have definite values. This is a misleading way of putting the issue, as it is not immediately clear how to interpret states of this sort as physical states of a system that includes experimental apparatus, and, if we can’t say what it would be like to observe the apparatus to be in such a state, it makes no sense to say that we never observe it to be in a state like that.

Nonetheless, we are faced with an interpretational problem. If we take the quantum state to be a complete description of the system, then the state is, contrary to what would antecedently expect, not a state corresponding to a unique, definite outcome. This is what led J.S. Bell to remark, “Either the wavefunction, as given by the Schrödinger equation, is not everything, or it is not right” (Bell 1987: 41, 2004: 201)[^bell-1987][^bell-2004]. This gives us a (*prima facie*) tidy way of classifying approaches to the measurement problem:

1. There are approaches that involve a denial that a quantum wave function (or any other way of representing a quantum state) yields a complete description of a physical system.
2. There are approaches that involve modification of the dynamics to produce a collapse of the quantum state in appropriate circumstances.
3. There are approaches that reject both horns of Bell’s dilemma, and hold that quantum states undergo unitary evolution at all times and that a quantum state-description is, in principle, complete.

We include in the first category approaches that deny that a quantum state should be thought of as representing anything in reality at all. These include variants of the Copenhagen interpretation, as well as pragmatic and other anti-realist approaches. Also in the first category are approaches that seek a completion of the quantum state description. These include hidden-variables approaches and modal interpretations. The second category of interpretation motivates a research programme of finding suitable indeterministic modifications of the quantum dynamics. Approaches that reject both horns of Bell’s dilemma are typified by Everettian, or “many-worlds” interpretations.

#### 4.2.1 The “Copenhagen interpretation”

Since the mid-1950’s, the term “Copenhagen interpretation” has been commonly used for whatever it is that the person employing the term takes to be the ‘orthodox’ viewpoint regarding the philosophical issues raised by quantum mechanics. According to Howard (2004)[^howard-2004], the phrase was first used by Heisenberg (1955, 1958), and is intended to suggest a commonality of views among Bohr and his associates, included Born and Heisenberg himself. Recent historiography has emphasized diversity of viewpoints among the figures associated with the Copenhagen interpretation; see the entry on Copenhagen interpretation of quantum mechanics, and references therein. Readers should be aware that the term is not univocal, and that different authors might mean different things when speaking of the“Copenhagen interpretation.”

#### 4.2.2 Non-realist and pragmatist approaches to quantum mechanics

From the early days of quantum mechanics, there has been a strain of thought that holds that the proper attitude to take towards quantum mechanics is an instrumentalist or pragmatic one. On such a view, quantum mechanics is a tool for coordinating our experience and for forming expectations about the outcomes of experiments. Variants of this view include some versions of the Copenhagen interpretation. More recently, views of this sort have been advocated by physicists, including QBists, who hold that quantum states represent subjective or epistemic probabilities (see Fuchs *et al.*, 2014)[^fuchs-2014]. The philosopher Richard Healey defends a related view on which quantum states, though objective, are not to be taken as representational (see Healey 2012, 2017a, 2020)[^healey-2012][^healey-2017a][^healey-2020]. For more on these approaches, see entry on Quantum-Bayesian and pragmatist views of quantum theory.

#### 4.2.2 Hidden-variables and modal interpretations

Theories whose structure include the quantum state but include additional structure, with an aim of circumventing the measurement problem, have traditionally been called “hidden-variables theories”. That a quantum state description cannot be regarded as a complete description of physical reality was argued for in a famous paper by Einstein, Podolsky and Rosen (EPR) and by Einstein in subsequent publications (Einstein 1936, 1948, 1949)[^einstein-1936][^einstein-1948][^einstein-1949]. See the entry on the Einstein-Podolsky-Rosen argument in quantum theory.

There are a number of theorems that circumscribe the scope of possible hidden-variables theories. The most natural thought would be to seek a theory that assigns to all quantum observables definite values that are merely revealed upon measurement, in such a way that any experimental procedure that, in conventional quantum mechanics, would count as a “measurement” of an observable yields the definite value assigned to the observable. Theories of this sort are called *noncontextual* hidden-variables theory. It was shown by Bell (1966)[^bell-1966] and Kochen and Specker (1967) that there are no such theories for any system whose Hilbert space dimension is greater than three (see the entry on the Kochen-Specker theorem).

The Bell-Kochen-Specker Theorem does not rule out hidden-variables theories *tout court*. The simplest way to circumvent it is to pick as always-definite some observable or compatible set of observables that suffices to guarantee determinate outcomes of experiments; other observables are not assigned definite values and experiments thought of as “measurements” of these observables do not reveal pre-existing values.

The most thoroughly worked-out theory of this type is the pilot wave theory developed by de Broglie and presented by him at the Fifth Solvay Conference held in Brussels in 1927, revived by David Bohm in 1952, and currently an active area of research by a small group of physicists and philosophers. According to this theory, there are particles with definite trajectories, that are guided by the quantum wave function. For the history of the de Broglie theory, see the introductory chapters of Bacciagaluppi and Valentini (2009). For an overview of the de Broglie-Bohm theory and philosophical issues associated with it see the entry on Bohmian mechanics.

There have been other proposals for supplementing the quantum state with additional structure; these have come to be called *modal interpretations*; see the entry on modal interpretations of quantum mechanics.

#### 4.2.3 Dynamical Collapse Theories

As already mentioned, Dirac wrote as if the collapse of the quantum state vector precipitated by an experimental intervention on the system is a genuine physical change, distinct from the usual unitary evolution. If collapse is to be taken as a genuine physical process, then something more needs to be said about the circumstances under which it occurs than merely that it happens when an experiment is performed. This gives rise to a research programme of formulating a precisely defined dynamics for the quantum state that approximates the linear, unitary Schrödinger evolution in situations for which this is well-confirmed, and produces collapse to an eigenstate of the outcome variable in typical experimental set-ups, or, failing that, a close approximation to an eigenstate. The only promising collapse theories are stochastic in nature; indeed, it can be shown that a deterministic collapse theory would permit superluminal signalling. See the entry on collapse theories for an overview, and Gao, ed. (2018) for a snapshot of contemporary discussions.

*Prima facie*, a dynamical collapse theory of this type can be a quantum state monist theory, one on which, in Bell’s words, “the wave function is everything”. In recent years, this has been disputed; it has been argued that collapse theories require “primitive ontology” in addition to the quantum state. See Allori *et al.* (2008), Allori (2013)[^allori-2013], and also the entry on collapse theories, and references therein. Reservations about this approach have been expressed by Egg (2017, 2021)[^egg-2017][^egg-2021], Myrvold (2018)[^myrvold-2018], and Wallace (2020)[^wallace-2020].

#### 4.2.4 Everettian, or “many worlds” theories

In his doctoral dissertation of 1957 (reprinted in Everett 2012)[^everett-2012], Hugh Everett III proposed that quantum mechanics be taken as it is, without a collapse postulate and without any “hidden variables”. The resulting interpretation he called the *relative state* interpretation.

The basic idea is this. After an experiment, the quantum state of the system plus apparatus is typically a superposition of terms corresponding to distinct outcomes. As the apparatus interacts with its environment, which may include observers, these systems become entangled with the apparatus and quantum system, the net result of which is a quantum state involving, for each of the possible experimental outcomes, a term in which the apparatus reading corresponds to that outcome, there are records of that outcome in the environment, observers observe that outcome, *etc.*. Everett proposed that each of these terms be taken to be equally real. From a God’s-eye-view, there is no unique experimental outcome, but one can also focus on a particular determinate state of one subsystem, say, the experimental apparatus, and attribute to the other systems participating in the entangled state a *relative state*, relative to that state of the apparatus. That is, relative to the apparatus reading ‘+’ is a state of the environment recording that result and states of observers observing that result (see the entry on Everett’s relative-state formulation of quantum mechanics, for more detail on Everett’s views).

Everett’s work has inspired a family of views that go by the name of “Many Worlds” interpretations; the idea is that each of the terms of the superposition corresponds to a coherent world, and all of these worlds are equally real. As time goes on, there is a proliferation of these worlds, as situations arise that give rise to a further multiplicity of outcomes (see the entry many-worlds interpretation of quantum mechanics, and Saunders 2007, for overviews of recent discussions; Wallace 2012 is an extended defense of an Everettian interpretation of quantum mechanics)[^saunders-2007][^wallace-2012].

There is a family of distinct, but related views, that go by the name of “Relational Quantum Mechanics”. These views agree with Everett in attributing to a system definite values of dynamical variables only relative to the states of other systems; they differ in that, unlike Everett, they do not take the quantum state as their basic ontology (see the entry on relational quantum mechanics for more detail).

### 4.3 Extended Wigner’s friend scenarios as a source of no-go theorems

As mentioned, quantum theory, as standardly formulated, employs a division of the world into a part that is treated with the theory, and a part that is not. Both von Neumann and Heisenberg emphasized an element of arbitrariness in the location of the division. In some formulations, the division was thought of as a distinction between observer and observed, and it became common to say that quantum mechanics requires reference to an observer for its formulation.

The founders of quantum mechanics tended to assume implicitly that, though the “cut” is somewhat moveable, in any given analysis a division would be settled on, and one would not attempt to combine distinct choices of the cut in one analysis of an experiment. If, however, one thinks of the cut as marking the distinction between observer and observed, one is led to ask about situations involving multiple observers. Is each observer permitted to treat the other as a quantum system?

The consideration of such scenarios was initiated by Wigner (1961). Wigner considered a hypothetical scenario in which a friend conducts an observation, and he himself treats the joint system, consisting of the friend and the system experimented upon, as a quantum system. For this reason, scenarios of this sort have come to be known as “Wigner’s friend” scenarios. Wigner was led by consideration of such scenarious to hypothesize that conscious observers cannot be in a superposition of states corresponding to distinct perceptions; the introduction of conscious observers initiates a physical collapse of the quantum state; this involves, according to Wigner, “a violation of physical laws where consciousness plays a role” (Wigner 1961, 294 ;167, 181).

Frauchiger and Renner (2018) initiated the discussion of scenarios of this sort involving more than two observers, which have come to be called “extended Wigner’s friend” scenarios. Further results along these lines include Brukner (2018)[^brukner-2018], Bong et al. (2020), and Guérin et al. (2021). The strategy of these investigations is to present some set of plausible-seeming assumptions (a different set, for each of the works cited), and to show, via consideration of a hypothetical situation involving multiple observers, the inconsistency of that set of assumptions. The theorems are, therefore, no-go theorems for approaches to the measurement problem that would seek to satisfy all of the members of the set of assumptions that has been shown to be inconsistent.

An assumption common to all of these investigations is that it is always permissible for one observer to treat systems containing other observers within quantum mechanics and to employ unitary evolution for those systems. This means that collapse is not regarded as a physical process. It is also assumed that each observer always perceives a unique outcome for any experiment performed by that observer; this excludes Everettian interpretations. Where the works cited vary is in the other assumptions made.

It should be noted that each of the major avenues of approach to the measurement problem is capable of giving an account of goings-on in any physical scenario, including the ones considered in these works. Each of them, therefore, must violate some member of the set of assumptions shown to be inconsistent. These results do not pose problems for existing approaches to the measurement problem; rather, they are no-go theorems for approaches that might seek to satisfy all of the set of assumptions shown to be inconsistent. As the assumptions considered include both unitary evolution and unique outcomes of experiments, and the scenarios considered involved situations involving superpositions of distinct experimental outcomes, these results concern theories on which the quantum state, as given by the Schrödinger equation, is not a complete description of reality, as it fails to determine the unique outcomes perceived by the observers. These preceptions could be thought of as supervening on brain states, in which case there is physical structure not included in the quantum state, or as attributes of immaterial minds. On either interpretation, the sorts of theories ruled out fall under the first horn of Bell’s dilemma, mentioned in section 4.2, and these no-go results in part reproduce, and in part extend, no-go results for certain sorts of modal interpretations (see entry on modal interpretations of quantum mechanics).

These results involving extended Wigner’s friend scenarios have engendered considerable philosophical discussion; see Sudbery (2017, 2019)[^sudbery-2017][^sudbery-2019], Healey (2018, 2020)[^healey-2018][^healey-2020], Dieks (2019)[^dieks-2019], Losada et al. (2019), Dascal (2020)[^dascal-2020], Evans (2020)[^evans-2020], Fortin and Lombardi (2020), Kastner (2020)[^kastner-2020], Muciño & Okon (2020), Bub (2020, 2021)[^bub-2020][^bub-2021], Cavalcanti (2021)[^cavalcanti-2021][^cavalcanti-2021-2], Cavalcanti and Wiseman (2021), and Żukowski and Markiewicz (2021).

### 4.4 The role of decoherence

A quantum state that is a superposition of two distinct terms, such as

$$ \ket{\psi} = a \ket{\psi_{1}} + b \ket{\psi_{2}} , $$

where $\ket{\psi_{1}}$ and $\ket{\psi_{2}}$ are distinguishable states, is not the same state as a mixture of $\ket{\psi_{1}}$ and $\ket{\psi_{2}}$, which would be appropriate for a situation in which the state prepared was either $\ket{\psi_{1}}$ or $\ket{\psi_{2}}$, but we don’t know which. The difference between a coherent superposition of two terms and a mixture has empirical consequences. To see this, consider the double-slit experiment, in which a beam of particles (such as electrons, neutrons, or photons) passes through two narrow slits and then impinges on a screen, where the particles are detected. Take $\ket{\psi_{1}}$ to be a state in which a particle passes through the top slit, and $\ket{\psi_{2}}$, a state in which it passes through the bottom slit. The fact that the state is a superposition of these two alternatives is exhibited in interference fringes at the screen, alternating bands of high and low rates of absorption.

This is often expressed in terms of a difference between classical and quantum probabilities. If the particles were classical particles, the probability of detection at some point $p$ of the screen would simply be a weighted average of two conditional probabilities: the probability of detection at $p$, given that the particle passed through the top slit, and the probability of detection at $p$, given that the particle passed through the bottom slit. The appearance of interference is an index of nonclassicality.

Suppose, now, that the electrons interact with something else (call it the *environment*) on the way to the screen, that could serve as a “which-way” detector; that is, the state of this auxiliary system becomes entangled with the state of the electron in such a way that its state is correlated with $\ket{\psi_{1}}$ and $\ket{\psi_{2}}$. Then the state of the quantum system, $s$, and its environment, $e$, is

$$ \ket{\psi} _{se} = a \ket{ \psi_{1}} _{s} \ket{ \phi_{1}} _{e} + b \ket{ \psi_{2}}_{s} \ket{ \phi_{2}} _{e} $$

If the environment states $\ket{\phi_{1}} _{e}$ are $\ket{\phi_{2}}_{e}$ are distinguishable states, then this completely destroys the interference fringes: the particles interact with the screen as if they determinately went through one slit or the other, and the pattern that emerges is the result of overlaying the two single-slit patterns. That is, we can treat the particles as if they followed (approximately) definite trajectories, and apply probabilities in a classical manner.

Now, macroscopic objects are typically in interaction with a large and complex environment—they are constantly being bombarded with air molecules, photons, and the like. As a result, the reduced state of such a system quickly becomes a mixture of quasi-classical states, a phenomenon known as *decoherence*.

A generalization of decoherence lies at the heart of an approach to the interpretation of quantum mechanics that goes by the name of *decoherent histories approach* (see the entry on the consistent histories approach to quantum mechanics for an overview).

Decoherence plays important roles in the other approaches to quantum mechanics, though the role it plays varies with approach; see the entry on the role of decoherence in quantum mechanics for information on this.

### 4.5 Comparison of approaches to the measurement problem

Most of the above approaches take it that the goal is to provide an account of events in the world that recovers, at least in some approximation, something like our familiar world of ordinary objects behaving classically. None of the mainstream approaches accord any special *physical* role to conscious observers. There have, however, been proposals in that direction (see the entry on quantum approaches to consciousness for discussion).

All of the above-mentioned approaches are consistent with observation. Mere consistency, however, is not enough; the rules for connecting quantum theory with experimental results typically involve nontrivial (that is, not equal to zero or one) probabilities assigned to experimental outcomes. These calculated probabilities are confronted with empirical evidence in the form of statistical data from repeated experiments. Extant hidden-variables theories reproduce the quantum probabilities, and collapse theories have the intriguing feature of reproducing very close approximations to quantum probabilities for all experiments that have been performed so far but departing from the quantum probabilities for other conceivable experiments. This permits, in principle, an empirical discrimination between such theories and no-collapse theories.

A criticism that has been raised against Everettian theories is that it is not clear whether they can even make sense of statistical testing of this kind, as it does not, in any straightforward way, make sense to talk of the probability of obtaining, say, a ‘+” outcome of a given experiment when it is certain that all possible outcomes will occur on some branch of the wavefunction. This has been called the “Everettian evidential problem”. It has been the subject of much recent work on Everettian theories; see Saunders (2007)[^saunders-2007] for an introduction and overview.

If one accepts that Everettians have a solution to the evidential problem, then, among the major lines of approach, none is favored in a straightforward way by the empirical evidence. There will not be space here to give an in-depth overview of these ongoing discussions, but a few considerations can be mentioned, to give the reader a flavor of the discussions; see entries on particular approaches for more detail.

Everettians take, as a virtue of the approach, the fact that it does not involve an extension or modification of the quantum formalism. Bohmians claim, in favor of the Bohmian approach, that a theory on these lines provides the most straightforward picture of events; ontological issues are less clear-cut when it comes to Everettian theories or collapse theories.

Another consideration is compatibility with relativistic causal structure. See Myrvold (2021)[^myrvold-2021] for an overview of relavistic constraints on approaches to the measurement problem.The de Broglie-Bohm theory requires a distinguished relation of distant simultaneity for its formulation, and, it can be argued, this is an ineliminable feature of any hidden-variables theory of this sort, that selects some observable to always have definite values (see Berndl *et al.* 1996; Myrvold 2002, 2021)[^berndl-1996][^myrvold-2002][^myrvold-2021]. On the other hand, there are collapse models that are fully relativistic. On such models, collapses are localized events. Though probabilities of collapses at spacelike separation from each other are not independent, this probabilistic dependence does not require us to single one out as earlier and the other later. Thus, such theories do not require a distinguished relation of distant simultaneity. There remains, however, some discussion of how to equip such theories with beables (or “elements of reality”). See the entry on collapse theories and references therein; see also, for some recent contributions to the discussion, Fleming (2016)[^fleming-2016], Maudlin (2016)[^maudlin-2016], and Myrvold (2016)[^myrvold-2016]. In the case of Everettian theories, one must first think about how to formulate the question of relativistic locality. Several authors have approached this issue in somewhat different ways, with a common conclusion that Everettian quantum mechanics is, indeed, local. (See Vaidman 1994; Bacciagaluppi 2002; Chapter 8 of Wallace 2012; Tipler 2014; Vaidman 2016; and Brown and Timpson 2016.)[^bacciagaluppi-2002][^brown-2016][^tipler-2014][^vaidman-1994][^vaidman-2016][^wallace-2012]

## 5. Ontological Issues

As mentioned, a central question of interpretation of quantum mechanics concerns whether quantum states should be regarded as representing anything in physical reality. If this is answered in the affirmative, this gives rise to new questions, namely, what sort of physical reality is represented by the quantum state, and whether a quantum state could in principle give an exhaustive account of physical reality.

### 5.1 The question of quantum state realism.

Harrigan and Spekkens (2010) have introduced a framework for discussing these issues. In their terminology, a complete specification of the physical properties is given by the *ontic state* of a system. An ontological model posits a space of ontic states and associates, with any preparation procedure, a probability distribution over ontic states. A model is said to be *ψ*-*ontic* if the ontic state uniquely determines the quantum state; that is, if there is a function from ontic states to quantum states (this includes both cases in which the quantum state also completely determines the physical state, and cases, such as hidden-variables theories, in which the quantum state does not completely determine the physical state). In their terminology, models that are not *ψ*-ontic are called \(\psi\)*-epistemic*. If a model is not *ψ*-ontic, this means that it is possible for some ontic states to be the result of two or more preparations that lead to different assignments of pure quantum states; that is, the same ontic state may be compatible with distinct quantum states.

This gives a nice way of posing the question of quantum state realism: are there preparations corresponding to distinct pure quantum states that can give rise to the same ontic state, or, conversely, are there ontic states compatible with distinct quantum states? Pusey, Barrett, and Rudolph (2012) showed that, if one adopts a seemingly natural independence assumption about state preparations—namely, the assumption that it is possible to prepare a pair of systems in such a way that the probabilities for ontic states of the two systems are effectively independent—then the answer is negative; any ontological model that reproduces quantum predictions and satisfies this Preparation Independence assumption must be a *ψ*-ontic model.

The Pusey, Barrett and Rudolph (PBR) theorem does not close off all options for anti-realism about quantum states; an anti-realist about quantum states could reject the Preparation Independence assumption, or reject the framework within which the theorem is set; see discussion in Spekkens (2015)[^spekkens-2015]: 92–93. See Leifer (2014)[^leifer-2014] for a careful and thorough overview of theorems relevant to quantum state realism, and Myrvold (2020)[^myrvold-2020] for a presentation of a case for quantum state realism based on theorems of this sort.

### 5.2 Ontological category of quantum states

The major realist approaches to the measurement problem are all, in some sense, realist about quantum states. Merely saying this is insufficient to give an account of the ontology of a given interpretation. Among the questions to be addressed are: if quantum states represent something physically real, what sort of thing is it? This is the question of the ontological construal of quantum states. Another question is the EPR question, whether a description in terms of quantum states can be taken as, in principle, complete, or whether it must be supplemented by different ontology.

De Broglie’s original conception of the “pilot wave” was that it would be a field, analogous to an electromagnetic field. The original conception was that each particle would have its own guiding wave. However, in quantum mechanics as it was developed at the hands of Schrödinger, for a system of two or more particles there are not individual wave functions for each particle, but, rather, a single wave function that is defined on $n$-tuples of points in space, where $n$ is the number of particles. This was taken, by de Broglie, Schrödinger and others, to militate against the conception of quantum wave functions as fields. If quantum states represent something in physical reality, they are unlike anything familiar in classical physics.

One response that has been taken is to insist that quantum wave functions are fields nonetheless, albeit fields on a space of enormously high dimension, namely, $3n$, where $n$ is the number of elementary particles in the universe. On this view, this high-dimensional space is thought of as more fundamental than the familiar three-dimensional space (or four-dimensional spacetime) that is usually taken to be the arena of physical events. See Albert (1996, 2013)[^albert-1996][^albert-2013], for the classic statement of the view; other proponents include Loewer (1996)[^loewer-1996], Lewis (2004)[^lewis-2004], Ney (2012, 2013a,b, 2021), and North (2013)[^north-2013]. Most of the discussion of this proposal has taken place within the context of nonrelativistic quantum mechanics, which is not a fundamental theory. It has been argued that considerations of how the wave functions of nonrelativistic quantum mechanics arise from a quantum field theory undermines the idea that wave functions are relevantly like fields on configuration space, and also the idea that configuration spaces can be thought of as more fundamental than ordinary spacetime (Myrvold 2015)[^myrvold-2015].

A view that takes a wave function as a field on a high-dimensional space must be distinguished from a view that takes it to be what Belot (2012)[^belot-2012] has called a *multi-field*, which assigns properties to $n$-tuples of points of ordinary three-dimensional space. These are distinct views; proponents of the $3n$-dimensional conception make much of the fact that it restores Separability: on this view, a complete specification of the way the world is, at some time, is given by specification of local states of affairs at each address in the fundamental ($3n$-dimensional) space. Taking a wave function to be a multi-field, on the other hand, involves accepting nonseparability. Another difference between taking wave-functions as multi-fields on ordinary space and taking them to be fields on a high-dimensional space is that, on the multi-field view, there is no question about the relation of ordinary three-dimensional space to some more fundamental space.­ Hubert and Romano (2018) argue that wave-functions are naturally and straightforwardly construed as multi-fields.

It has been argued that, on the de Broglie-Bohm pilot wave theory and related pilot wave theories, the quantum state plays a role more similar to that of a law in classical mechanics; its role is to provide dynamics for the Bohmian corpuscles, which, according to the theory, compose ordinary objects. See Dürr, Goldstein, and Zanghì (1997), Allori *et al.* (2008), Allori (2021)[^allori-2021].

Dürr, Goldstein, and Zanghì (1992) introduced the term “primitive ontology” for what, according to a physical theory, makes up ordinary physical objects; on the de Broglie-Bohm theory, this is the Bohmian corpuscles. The conception is extended to interpretations of collapse theories by Allori *et al.* (2008). Primitive ontology is to be distinguished from other ontology, such as the quantum state, that is introduced into the theory to account for the behavior of the primitive ontology. The distinction is meant to be a guide as to how to conceive of the nonprimitive ontology of the theory.

## 6. Quantum computing and quantum information theory

Quantum mechanics has not only given rise to interpretational conundrums; it has given rise to new concepts in computing and in information theory. *Quantum information theory* is the study of the possibilities for information processing and transmission opened up by quantum theory. This has given rise to a different perspective on quantum theory, one on which, as Bub (2000, 597)[^bub-2000] put it, “the puzzling features of quantum mechanics are seen as a resource to be developed rather than a problem to be solved” (see the entries on quantum computing and quantum entanglement and information).

## 7. Reconstructions of quantum mechanics and beyond

Another area of active research in the foundations of quantum mechanics is the attempt to gain deeper insight into the structure of the theory, and the ways in which it differs from both classical physics and other theories that one might construct, by characterizing the structure of the theory in terms of very general principles, often with an information-theoretic flavour.

This project has its roots in early work of Mackey (1957, 1963)[^mackey-1957][^mackey-1963], Ludwig (1964)[^ludwig-1964], and Piron (1964)[^piron-1964] aiming to characterize quantum mechanics in operational terms. This has led to the development of a framework of generalized probabilistic model. It also has connections with the investigations into quantum logic initiated by Birkhoff and von Neumann (1936) (see the entry quantum logic and probability theory for an overview).

Interest in the project of deriving quantum theory from axioms with clear operational content was revived by the work of Hardy (2001 [2008], Other Internet Resources). Significant results along these lines include the axiomatizations of Masanes and Müller (2011) and Chiribella, D’Ariano, and Perinotti (2011). See Chiribella and Spekkens (2015)[^spekkens-2015] for an overview of this burgeoning research area.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=qt-issues). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/qt-issues/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=qt-issues&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/qt-issues/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- Feynman, R., [Lectures on Physics](http://www.feynmanlectures.caltech.edu/III_toc.html). These are introductory lectures aimed at physics undergraduates.
- Hardy, Lucien, 2001 [2008], “[Quantum Theory from Five Reasonable Axioms](https://arxiv.org/abs/quant-ph/0101012v4)”, manuscript at arxiv.org originally submitted in 2001, but now is labeled version 4 (2008).
- Lewis, Peter J., “[Interpretations of Quantum Mechanics](http://www.iep.utm.edu/int-qm/)”, *Internet Encyclopedia of Philosophy*.
- Norton, John, “[Origins of Quantum Theory](http://www.pitt.edu/~jdnorton/teaching/HPS_0410/chapters/quantum_theory_origins/),” A good introduction to the history of quantum theory, about which little is said in the present entry.
- [PhET Interactive Simulations project](http://phet.colorado.edu/en/simulations/category/physics/quantum-phenomena), University of Colorado Boulder; these pages contain useful simulations of classic quantum experiments.

## Related Entries

Bell’s Theorem | physics: holism and nonseparability | quantum mechanics | quantum mechanics: Bohmian mechanics | quantum mechanics: collapse theories | quantum mechanics: consistent histories approach | quantum mechanics: Copenhagen interpretation of | quantum mechanics: Everettian | quantum mechanics: Kochen-Specker theorem | quantum mechanics: many-worlds interpretation of | quantum mechanics: modal interpretations of | quantum mechanics: relational | quantum mechanics: the role of decoherence in | quantum theory: and consciousness | quantum theory: and mathematical rigor | quantum theory: quantum computing | quantum theory: quantum entanglement and information | quantum theory: quantum field theory | quantum theory: quantum gravity | quantum theory: quantum logic and probability theory | quantum theory: the Einstein-Podolsky-Rosen argument in | Uncertainty Principle

[^albert-1996]: Albert, David Z., 1996, “Elementary quantum metaphysics”, in J.T. Cushing, A. Fine, & S. Goldstein (eds.), *Bohmian Mechanics and Quantum Mechanics: An appraisal*, Dordrecht: Kluwer, 277–284.

[^albert-2013]: –––, 2013, “Wave function realism”, in Ney and Albert (eds.) 2013: 52–57.

[^allori-2013]: Allori, Valia, 2013, “Primitive Ontology and the Structure of Fundamental Physical Theories”, in Ney and Albert (eds.) 2013: 58–90.

[^allori-2021]: Allori, Valia, 2021, “Wave-functionalism”, *Synthese*, 199: 12271–12293.

[^allori-2008]: Allori, Valia, Sheldon Goldstein, Roderich Tumulka, and Nino Zanghì, 2008, “On the Common Structure of Bohmian Mechanics and the Ghirardi–Rimini–Weber Theory”, *The British Journal for the Philosophy of Science*, 59(3): 353–389. doi:10.1093/bjps/axn012

[^bacciagaluppi-2002]: Bacciagaluppi, Guido, 2002, “Remarks on Space-time and Locality in Everett’s Interpretation”, in T. Placzek and J. Butterfield (eds.), *Non-locality and Modality*, Berlin: Springer, 105–124.

[^bacciagaluppi-2009]: Bacciagaluppi, Guido, and Antony Valentini, 2009, *Quantum Theory at the Crossroads: Reconsidering the 1927 Solvay Conference*, Cambridge: Cambridge University Press.

[^bell-1966]: Bell, J.S., 1966, “On the Problem of Hidden Variables in Quantum Mechanics”, *Reviews of Modern Physics*, 38: 447–52; reprinted in Bell 2004: 1–13.

[^bell-1986]: –––, 1986, “Six Possible Worlds of Quantum Mechanics”, in S. Allén (ed.), *Possible Worlds in Humanities, Arts and Sciences*, Berlin, Walter de Gruyter, 359–373; reprinted in Bell 2004, 181–195.

[^bell-1987]: –––, 1987, “Are There Quantum Jumps?” in C.W. Kilmister (ed), *Schrödinger: Centenary celebration of a polymath*, Cambridge: Cambridge University Press, 41–52; reprinted in Bell 2004: 201–212.

[^bell-1990]: –––, 1990, “Against ‘Measurement’”, *Physics World*, 3: 33–40; reprinted in Bell 2004: 213–231.

[^bell-2004]: –––, 2004, *Speakable and Unspeakable in Quantum Mechanics*, 2ⁿᵈ edition, Cambridge: Cambridge University Press.

[^bell-2016]: Bell, Mary and Shan Gao (eds.), 2016, *Quantum Nonlocality and Reality: 50 Years of Bell’s Theorem*, Cambridge: Cambridge University Press.

[^belot-2012]: Belot, Gordon, 2012, “Quantum States for primitive ontologists: a case study”, *European Journal for the Philosophy of Science*, 2: 67–83.

[^berndl-1996]: Berndl, Karin, Detlef Dürr, Sheldon Goldstein, and Nino Zanghì, 1996, “Nonlocality, Lorentz invariance, and Bohmian quantum theory“, *Physical Review A*, 53: 2062–2073.

[^birkhoff-1936]: Birkhoff, Garrett, and John von Neumann, 1936, “The Logic of Quantum Mechanics”, *Annals of Mathematics* (second series), 37: 823–43.

[^bong-2020]: Bong, Kok-Wei, Aníbal Utreras-Alarcón, Farzad Ghafari, Yeong-Cherng Liang, Nora Tischler, Eric G. Cavalcanti, Geoff J. Pryde & Howard M. Wiseman, 2020, “A strong no-go theorem on the Wigner’s friend paradox”, *Nature Physics*, 16: 1199–1205.

[^brown-2016]: Brown, Harvey R. and Christopher G. Timpson, 2016,“Bell on Bell’s Theorem: The Changing Face of Nonlocality”, in Bell and Gao (eds.) 2016: 91–123.

[^brukner-2018]: Brukner, Časlav, 2018, “A no-go theorem for observer-independent facts”, *Entropy*, 20(5): 350.

[^bub-2000]: Bub, Jeffrey, 2000, “Indeterminacy and entanglement: the challenge of quantum mechanics”, *The British Journal for the Philosophy of Science*, 51: 597–615.

[^bub-2020]: –––, 2020, “‘Two Dogmas’ Redux”, in M. Hemmo and O. Shenker (eds.), *Quantum, Probability, Logic: The Work and Influence of Itamar Pitowsky*, Berlin: Springer, 199–216.

[^bub-2021]: –––, 2021, “Understanding the Frauchiger–Renner Argument”, *Foundations of Physics*, 51: 36.

[^cavalcanti-2021]: Cavalcanti, Eric, 2021, “The View from a Wigner Bubble”, *Foundations of Physics*, 51: 39.

[^cavalcanti-2021-2]: Cavalcanti, Eric, and Howard M. Wiseman, 2021, “Implications of Local Friendliness for Violation for Quantum Causality”, *Entropy*, 23: 925.

[^chiribella-2011]: Chiribella, Giulio, Giacomo Mauro D’Ariano, and Paolo Perinotti, 2011, “Informational derivation of quantum theory”, *Physical Review A*, 84: 012311. doi:10.1103/PhysRevA.84.012311

[^chiribella-2015]: Chiribella, Giulio and Robert W. Spekkens (eds.), 2015, *Quantum Theory: Informational Foundations and Foils*, Berlin: Springer.

[^dascal-2020]: Dascal, Michael, 2020, “What’s left for the neo-Copenhagen theorist”, *Studies in History and Philosophy of Modern Physics*, 72: 310–321.

[^deutsch-2000]: Deutsch, David and Patrick Hayden, 2000, “Information flow in entangled quantum systems”, *Proceedings of the Royal Society of London A*, 456: 1759–74.

[^dieks-2019]: Dieks, Dennis, 2019, “Quantum Mechanics and Perspectivalism”, in O. Lombardi, S. Fortin, C. Lopez, and F. Holik (eds.), *Quantum Worlds: Perspectives on the Ontology of Quantum Mechanics*, Cambridge: Cambridge University Press, 51–70.

[^dirac-1935]: Dirac, P.A.M., 1935, *Principles of Quantum Mechanics*, 2ⁿᵈ edition, Oxford: Oxford University Press.

[^dürr-nd]: Dürr, Detlef, Sheldon Goldstein, and Nino Zanghì, “Quantum Equilibrium and the Origin of Absolute Uncertainty”, *Journal of Statistical Physics*, 67: 843–907.

[^dürr-1997]: –––, 1997, “Bohmian Mechanics and the Meaning of the Wave Function”, in R.S. Cohen, M. Horne and J. Stachel (eds.), *Experimental Metaphysics: Quantum Mechanical Studies for Abner Shimony* (Volume 1), Boston: Kluwer Academic Publishers.

[^einstein-1935]: Einstein, Albert, Boris Podolsky, and Nathan Rosen, 1935, “Can Quantum-Mechanical Description of Reality Be Considered Complete?” *Physical Review*, 47: 777–780.

[^einstein-1936]: Einstein, Albert, 1936, “Physik und Realität”, *Journal of the Franklin Institute*, 221: 349–382. English translation in Einstein 1954.

[^einstein-1948]: –––, 1948, “Quanten-Mechanik und Wirklichkeit”, *Dialectica*, 2: 320–324.

[^einstein-1949]: –––, 1949, “Autobiographical notes”, in P.A. Schilpp (ed.), *Albert Einstein: Philosopher-Scientist*, Chicago: Open Court.

[^einstein-1954]: –––, 1954, “Physics and reality”, in *Ideas and Opinions*, New York: Crown Publishers, Inc., 290–323 (translation of Einstein 1936).

[^egg-2017]: Egg, Matthias, 2017, “The physical salience of non-fundamental local beables”, *Studies in History and Philosophy of Modern Physics*, 57: 104–110.

[^egg-2021]: –––, 2021, “Quantum Ontology without Speculation”. *European Journal for Philosophy of Science*, 11: 32.

[^evans-2020]: Evans, Peter W., 2020, “Perspectival objectivity, Or: how I learned to stop worrying and love observer-dependent reality”, *European Journal for Philosophy of Science*, 10: 19.

[^everett-2012]: Everett III, Hugh, 2012, *The Everett Interpretation of Quantum Mechanics: Collected Works 1955–1980 With Commentary*, Jeffrey A. Barrett and Peter Byrne (eds.), Princeton: Princeton University Press.

[^fleming-2016]: Fleming, Gordon N., 2016, “Bell Nonlocality, Hardy’s Paradox and Hyperplane Dependence”, in Bell and Gao (eds.) 2016: 261–281.

[^fortin-2020]: Fortin, Sebastian, and Olimpia Lombardi, 2020, “The Frauchiger-Renner argument: A new no-go result?” *Studies in History and Philosophy of Modern Physics*, 70: 1–7.

[^frauchiger-2018]: Frauchiger, Daniela, & Renato Renner, 2018, “Quantum theory cannot consistently describe the use of itself”, *Nature Communications*, 9: 3711.

[^freire-2022]: Freire Jr., Olival , Guido Bacciagaluppi, Olivier Darrigol, Thiago Hartz, Christian Joas, Alexei Kojevnikov, and Osvaldo Pessoa Jr. (eds.), 2022, *The Oxford Handbook of the History of Quantum Interpretations*, Oxford: Oxford University Press.

[^french-2020]: French, Steven, and Juha Saatsi (eds.), 2020, *Scientific Realism and the Quantum*, Oxford: Oxford University Press.

[^fuchs-2014]: Fuchs, Christopher A., N. David Mermin, and Rüdiger Schack, 2014, “An introduction to QBism with an application to the locality of quantum mechanics”, *American Journal of Physics*, 82: 749–752.

[^gao-2018]: Gao, Shan (ed.), 2018, *Collapse of the Wave Function: Models, Ontology, Origin, and Implications*, Cambridge: Cambridge University Press.

[^guérin-2021]: Guérin, Philippe Allard, Veronika Baumann, Flavio Del Santo, and Časlav Brukner, 2021, “A no-go theorem for the persistent reality of Wigner’s friend’s perception”, *Communications Physics*, 4: 93.

[^harrigan-2010]: Harrigan, Nicholas and Robert W. Spekkens, 2010, “Einstein, Incompleteness, and the Epistemic View of Quantum States”, *Foundations of Physics*, 40: 125–157.

[^healey-2012]: Healey, Richard, 2012, “Quantum Theory: A Pragmatist Approach”, *The British Journal for the Philosophy of Science*, 63: 729–771.

[^healey-2017a]: –––, 2017a, “Quantum States as Objective Informational Bridges”, *Foundations of Physics*, 47: 161–173.

[^healey-2017b]: –––, 2017b, *The Quantum Revolution in Philosophy*, Oxford: Oxford University Press.

[^healey-2018]: –––, 2018, “Quantum theory and the limits of objectivity”, *Foundations of Physics*, 48: 1568–1589.

[^healey-2020]: —, 2020, “Pragmatist Quantum Realism”, in French and Saatsi (eds.), 2021: 123–146.

[^heisenberg-1930a]: Heisenberg, Werner, 1930a, *Die Physicalische Prinzipien der Quantentheorie*, Leipzig: Verlag von S. Hirzel.

[^heisenberg-1930b]: –––, 1930b, *The Physical Principles of the Quantum Theory*, Carl Eckert and F.C. Hoyt (trans.), Chicago: University of Chicago Press.

[^howard-2004]: Howard, Don, 2004, “Who Invented the ‘Copenhagen Interpretation’? A Study in Mythology”, *Philosophy of Science*, 71: 669–682.

[^hubert-2018]: Hubert, Mario, and Davide Romano, 2018, “The wave-function as a multi-field”, *European Journal for the Philosophy of Science*, 8: 521–537.

[^kastner-2020]: Kastner, Ruth, 2020, “Unitary‑Only Quantum Theory Cannot Consistently Describe the Use of Itself: On the Frauchiger–Renner Paradox”, *Foundations of Physics*, 50: 441–456.

[^knox-2021]: Knox, Eleanor, and Alastair Wilson (eds.), 2021, *The Routledge Companion to Philosophy of Physics*, London: Routledge.

[^kochen-1967]: Kochen, Simon and Ernst Specker, 1967, “The Problem of Hidden Variables in Quantum Mechanics”, *Journal of Mathematics and Mechanics*, 17: 59–87.

[^lazarovici-2019]: Lazarovici, Dustin, and Mario Hubert, 2019, “How Quantum Mechanics can consistently describe the use of itself”, *Scientific Reports*, 9: 470.

[^leifer-2014]: Leifer, Matthew Saul, 2014, “Is the Quantum State Real? An Extended Review of *ψ*-ontology Theorems”, *Quanta*, 3: 67–155.

[^lewis-2004]: Lewis, Peter J., 2004, “Life in configuration space”, *The British Journal for the Philosophy of Science*, 55: 713–729. doi:10.1093/bjps/55.4.713

[^loewer-1996]: Loewer, B., 1996, “Humean supervenience”, *Philosophical Topics*, 24: 101–127.

[^london-1939]: London, Fritz and Edmond Bauer, 1939, *La théorie de l’observation en mécanique quantique*, Paris: Hermann. English translation, “The theory of observation in quantum mechanics”, in *Quantum Theory and Measurement*, J.A. Wheeler and W.H. Zurek (eds.), Princeton: Princeton University Press, 1983, 217–259.

[^losada-2019]: Losada, Marcelo, Roberto Laura, and Olimpia Lombardi, 2019, “Frauchiger-Renner argument and quantum histories”, *Physical Review A*, 100: 052114.

[^ludwig-1964]: Ludwig, G., 1964, “Versuch einer axiomatischen Grundlegung der Quantenmechanik und allgemeinerer physikalischer Theorien”, *Zeitschrift für Physik*, 181: 233–260.

[^mackey-1957]: Mackey, George W. 1957, “Quantum Mechanics and Hilbert Space”, *American Mathematical Monthly*, 64: 45–57.

[^mackey-1963]: –––, 1963, *The Mathematical Foundations of Quantum Mechanics: A lecture-note volume*, New York: W.A. Benjamin.

[^masanes-2011]: Masanes, Lluís and Markus P. Müller, 2011, “A derivation of quantum theory from physical Requirements”, *New Journal of Physics*, 13: 063001.

[^maudlin-2016]: Maudlin, Tim, 2016, “Local Beables and the Foundations of Physics”, in Bell and Gao (eds.) 2016: 317–330.

[^muciño-2020]: Muciño, R., and E. Okon, 2020, “Wigner’s convoluted friends”, *Studies in History and Philosophy of Modern Physics*, 72: 87–90.

[^myrvold-2002]: Myrvold, Wayne C., 2002, “Modal Interpretations and Relativity”, *Foundations of Physics*, 32: 1773–1784.

[^myrvold-2015]: –––, 2015, “What is a Wavefunction?” *Synthese*, 192: 3247–3274.

[^myrvold-2016]: –––, 2016, “Lessons of Bell”s Theorem: Nonlocality, Yes; Action at a Distance, Not Necessarily”, in Bell and Gao (eds.) 2016: 237–260.

[^myrvold-2018]: –––, 2018, “Ontology for Collapse Theories,” in Gao (ed.) 2018: 97–123.

[^myrvold-2020]: –––, 2020, “On the Status of Quantum State Realism,” in French and Saatsi (eds.), 2020: 229–251.

[^myrvold-2021]: –––, 2021, “Relativistic Constraints on Interpretations of Quantum Mechanics”, in Knox and Wilson (eds.) 2021: 99–121.

[^ney-2012]: Ney, Alyssa, 2012, “The status of our ordinary three dimensions in a quantum universe”, *Noûs*, 46: 525–560.

[^ney-2013a]: –––, 2013a, “Introduction”, in Ney and Albert (eds.) 2013: 1–51.

[^ney-2013]: –––, 2013*b*, “Ontological reduction and the wave function ontology”, in Ney and Albert (eds.) 2013: 168– 183.

[^ney-2021]: –––, 2021, *The World in the Wave Function: A Metaphysics for Quantum Physics*, Oxford, Oxford University Press.

[^ney-2013-2]: Ney, Alyssa and David Z. Albert (eds.), 2013, *The Wave Function: Essays on the Metaphysics of Quantum Mechanics*, Oxford: Oxford University Press.

[^north-2013]: North, Jill, 2013, “The structure of a quantum world”, in Ney and Albert (eds.) 2013: 184–202.

[^piron-1964]: Piron, Constantin, 1964, “Axiomatique quantique”, *Helvetica Physica Acta*, 37: 439–468.

[^pusey-2012]: Pusey, Matthew F., Jonathan Barrett, and Terry Rudolph, 2012, “On the Reality of the Quantum State”, *Nature Physics*, 8: 475–478.

[^saunders-2007]: Saunders, Simon, 2007. “Many Worlds? An Introduction”, in S. Saunders, J. Barrett, A. Kent, and D. Wallace (eds.), *Many Worlds? Everett, Quantum Theory, and Reality*, Oxford: Oxford University Press, 1–50.

[^spekkens-2007]: Spekkens, Robert W., 2007, “Evidence for the Epistemic view of Quantum States: A Toy Theory”, *Physical Review A*, 75: 032110.

[^spekkens-2015]: –––, 2015, “Quasi-Quantization: Classical Statistical Theories with an Epistemic Restriction”, in Chiribella and Spekkens 2015: 83–135.

[^sudbery-2017]: Sudbery, Anthony, 2017, “Single-world theory of the extended Wigner’s friend experiment”, *Foundations of Physics*, 47: 658–669.

[^sudbery-2019]: –––, 2019, “The Hidden Assumptions of Frauchiger and Renner”, *International Journal of Quantum Foundations*, 5: 98-109.

[^tipler-2014]: Tipler, Frank J., 2014, “Quantum nonlocality does not exist”, *Proceedings of the National Academy of Sciences*, 111: 11281–6.

[^vaidman-1994]: Vaidman, Lev, 1994, “On the paradoxical aspects of new quantum experiments”, in D. Hull, M. Forbes and R.M. Burian (eds.), *PSA 1994* (Volume 1), Philosophy of Science Association, 211–17.

[^vaidman-2016]: –––, 2016, “The Bell Inequality and the Many-Worlds Interpretation”, in Bell and Gao (eds.) 2016: 195–203.

[^neumann-1932]: von Neumann, John, 1932, *Mathematische Grundlagen der Quantenmechanik*, Berlin, Springer Verlag.

[^neumann-1955]: –––, 1955, *Mathematical Foundations of Quantum Mechanics*, Robert T. Beyer (trans.), Princeton: Princeton University Press.

[^wallace-2012]: Wallace, David, 2012, *The Emergent Multiverse: Quantum Theory according to the Everett interpretation*, Oxford: Oxford University Press.

[^wallace-2020]: –––, 2020, “On the Plurality of Quantum Theories: Quantum Theory as a Framework, and its Implications for the Quantum Measurement Problem”, in French and Saatsi (eds.) 2020: 78–102.

[^wigner-1962]: Wigner, Eugene P., 1962, “Remarks on the Mind-Body Problem”, in I.J. Good (ed.), *The Scientist Speculates: An Anthology of Partly-Baked Ideas*, London: William Heinemann, 284–320; reprinted in Wigner (1967), 171–184.

[^wigner-1967]: –––, 1967, *Symmetries and Reflections: Scientific Essays of Eugene P. Wigner*, Bloomington, Indiana University Press.

[^marek-2021]: Żukowski, Marek, and Marcin Markiewicz, 2021, “Physics and Metaphysics of Wigner’s Friends: Even Performed Pre-measurements Have No Results”, *Physical Review Letters*, 126: 130402.
