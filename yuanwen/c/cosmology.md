# Philosophy of Cosmology
**First published Tue Sep 26, 2017**

*Smeenk, Christopher, Ellis, George*

Cosmology (the study of the physical universe) is a science that, due to both theoretical and observational developments, has made enormous strides in the past 100 years. It began as a branch of theoretical physics through Einstein’s 1917 static model of the universe (Einstein 1917)[^einstein-1917] and was developed in its early days particularly through the work of Lemaître (1927).[^note-1] As recently as 1960, cosmology was widely regarded as a branch of philosophy. It has transitioned to an extremely active area of mainstream physics and astronomy, particularly due to the application to the early universe of atomic and nuclear physics, on the one hand, and to a flood of data coming in from telescopes operating across the entire electromagnetic spectrum on the other. However, there are two main issues that make the philosophy of cosmology unlike that of any other science. The first is,

The uniqueness of the Universe: there exists only one universe, so there is nothing else similar to compare it with, and the idea of “Laws of the universe” hardly makes sense.

This means it is the historical science *par excellence*: it deals with only one unique object that is the only member of its class that exists physically; indeed there is no non-trivial class of such objects (except in theoreticians’ minds) precisely for this reason. This issue will recur throughout this discussion. The second is

Cosmology deals with the physical situation that is the context in the large for human existence: the universe has such a nature that our life is possible.

This means that although it is a physical science, it is of particular importance in terms of its implications for human life. This leads to important issues about the explanatory scope of cosmology, which we return to at the end.

## 1. Cosmology’s Standard Model

Physical cosmology has achieved a consensus Standard Model (SM), based on extending the local physics governing gravity and the other forces to describe the overall structure of the universe and its evolution. According to the SM, the universe has evolved from an extremely high temperature early state, by expanding, cooling, and developing structures at various scales, such as galaxies and stars. This model is based on bold extrapolations of existing theories—applying general relativity, for example, at length scales 14 orders of magnitude larger than the those at which it has been tested—and requires several novel ingredients, such as dark matter and dark energy. The last few decades have been a golden age of physical cosmology, as the SM has been developed in rich detail and substantiated by compatibility with a growing body of observations. Here we will briefly introduce some of the central concepts of the SM to provide the minimal background needed for the ensuing discussion.[^note-2]

### 1.1 Spacetime Geometry

Gravity is the dominant interaction at large length scales. General relativity introduced a new way of representing gravity: rather than describing gravity as a force deflecting bodies from inertial motion, bodies free from non-gravitational forces move along the analog of straight lines, called geodesics, through a curved spacetime geometry.[^note-3] The spacetime curvature is related to the distribution of energy and matter through GR’s fundamental equations (Einstein’s field equations, EFE). The dynamics of the theory are non-linear: matter curves spacetime, and the curvature of spacetime determines how matter moves; and gravitational waves interact with each other gravitationally, and act as gravitational sources. The theory also replaces the single gravitational potential, and associated field equation, of Newton’s theory, with a set of 10 coupled, non-linear equations for ten independent potentials.[^note-4] This complexity is an obstacle to understanding the general features of solutions to EFE, and to finding exact solutions to describe specific physical situations. Most exact solutions have been found based on strong idealizations, introduced to simplify the mathematics.

Remarkably, much of cosmology is based on an extremely simple set of solutions found within a decade of Einstein’s discovery of GR. These Friedman-Lemaître-Robertson-Walker (FLRW) solutions have, in a precise sense, the most symmetry possible. The spacetime geometry is constrained to be uniform, so that there are no preferred locations or directions.[^note-5] They have a simple geometric structure, consisting of a “stack” of three-dimensional spatial surfaces $\Sigma(t)$ labeled by values of the cosmic time $t$ (topologically, $\Sigma \times \mathbb{R}$). The surfaces $\Sigma(t)$ are three-dimensional spaces (Riemannian manifolds) of constant curvature, with three possibilities: (1) spherical space, for the case of positive curvature; (2) Euclidean space, for zero curvature; and (3) hyperbolic space, for negative curvature.[^note-6]

These models describe an expanding universe, characterized fully by the behavior of the scale factor $R(t)$. The worldlines of “fundamental observers”, defined as at rest with respect to matter, are orthogonal to these surfaces, and the cosmic time corresponds to the proper time measured by the fundamental observers. The scale factor $R(t)$ represents the spatial distance in $\Sigma$ between nearby fundamental observers as a function of cosmic time. The evolution of these models is described by a simple set of equations governing $R(t)$, implied by Einstein’s field equations (EFE): the Friedmann equation,[^note-7]

$$\label{eq:Fried} \left(\frac{\dot{R}}{R}\right)^2 = \frac{8 \pi G \rho}{3} - \frac{k}{R^2} + \frac{\Lambda}{3},$$

and the isotropic form of the Raychaudhuri equation:

$$\label{eq:Ray} 3 \frac{\ddot{R}}{R} = {- 4}\pi G \left(\rho + 3 p \right) + \Lambda. $$

The curvature of surfaces $\Sigma(t)$ of constant cosmic time is given by $\frac{k}{R^2(t)}$, where $k = \{-1,0,1\}$ for negative, flat, and positive curvature (respectively). The assumed symmetries force the matter to be described as a perfect fluid[^note-8] with energy density $\rho$ and pressure $p$, which obey the energy conservation equation

$$\label{eq:cons} \dot{\rho} + (\rho + p) 3 \frac{\dot{R}}{R} = 0.$$

The unrelenting symmetry of the FLRW models makes them quite simple geometrically and dynamically. Rather than a set of coupled partial differential equations, which generically follow from EFE, in the FLRW models one only has to deal with 2 ordinary differential equations (only two of $(\ref{eq:Fried})$–$(\ref{eq:cons})$ are independent) which are determinate once an equation of state $p = p(\rho)$ is given.

These equations reveal three basic features of these models. First, these are dynamical models: it is hard to arrange an unchanging universe, with $\dot{R}(t) =0$. “Ordinary” matter has positive total stress-energy density, in the sense that $\rho_{\textit{grav}}\coloneqq \rho + 3p > 0$. From ($\ref{eq:Ray}$), the effect of such ordinary matter is to decelerate cosmic expansion, $\ddot{R} < 0$—gravity is a force of attraction. This is only so for ordinary matter: a positive cosmological constant, or matter with negative gravitational-energy density $\rho_{\textit{grav}}$ leads, conversely, to accelerating expansion, $\ddot{R} > 0$. Einstein was only able to construct a static model by delicately balancing the attraction of ordinary matter with a precisely chosen value of $\Lambda$; he unfortunately failed to notice that the solution was unstable, and overlooked the dynamical implications of his own theory.

Second, the expansion rate varies as different types of matter come to dominate the dynamics. As shown by ($\ref{eq:cons}$), the energy density for different types of matter and radiation dilutes at different rates: for example, pressureless dust ($p=0$) dilutes as $\propto R^{-3}$, radiation ($p=\rho/3$) as $\propto R^{-4}$, and the cosmological constant ($p=-\rho$) remains (as the name suggests) constant. The SM describes the early universe as having a much higher energy density in radiation than matter. This radiation-dominated phase eventually transitions to a matter-dominated phase as radiation dilutes more rapidly, followed eventually, if $\Lambda > 0$, by a transition to a $\Lambda$-dominated phase; if $k \neq 0$ there may also be a curvature dominated phase.

Third, FLRW models with ordinary matter have a singularity at a finite time in the past. Extrapolating back in time, given that the universe is currently expanding, eqn. ($\ref{eq:Ray}$) implies that the expansion began at some finite time in the past. The current rate of expansion is given by the Hubble parameter, $H_0 = (\frac{\dot{R}}{R})_0$. Simply extrapolating this expansion rate backward, from eqn. ($\ref{eq:Ray}$) the expansion rate must increase at earlier times, so $R(t) \rightarrow 0$ at a time less than the Hubble time Hubble time $H_0^{-1}$ before now, if $\rho_{\textit{grav}}\geq 0$. As this “big bang” is approached, the energy density and curvature increase without bound provided $\rho_{\textit{inert}}\coloneqq (\rho+p)>0$ (which condition guarantees that $\rho \rightarrow\infty$ as $R\rightarrow0$). This reflects gravitational instability: as $R(t)$ decreases, the energy density and pressure both increase, and they both appear with the same sign on the right hand side of eqn. ($\ref{eq:Ray}$), hence pressure $p>0$ does not help avoid the singularity. Work in the 1960s, discussed below in §4.1, established that the existence of a singularity holds in more realistic models, and is not an artifact of the symmetries of the FLRW models.

The SM adds small departures from strict uniformity in order to account for the formation and evolution of structure. Due to gravitational instability, such perturbations are enhanced dynamically—the density contrast of an initial region that differs from the average density grows with time. Sufficiently small fluctuations can be treated as linear perturbations to a background cosmological model, governed by an evolution equation that follows from EFE. Yet as the fluctuations grow larger, linearized perturbation theory no longer applies. According to the SM, structure grows hierarchically with smaller length scales going non-linear first, and larger structures forming via later mergers. Models of evolution of structures at smaller length scales (e.g., the length scales of galaxies) include physics other than gravity, such as gas dynamics, to describe the collapsing clumps of matter. Cold dark matter (CDM) also plays a crucial role in the SM’s account of structure formation: it clumps first, providing scaffolding for clumping of baryonic matter.

A full account of structure formation requires integrating physics over an enormous range of dynamical scales and including a cosmological constant as well as baryonic matter, radiation, and dark matter. This is an active area of research, primarily pursued using sophisticated $N$-body computer simulations to study features of the galaxy distribution produced by the SM, given various assumptions.[^note-9]

### 1.2 Observations

There are two main ways in which cosmological observations support perturbed FLRW models. First, cosmologists use matter and radiation in the universe to probe the background spacetime geometry and its evolution. The universe appears to be isotropic at sufficiently large scales, as indicated by background radiation (most notably the cosmic microwave background radiation (CMB), discussed below) and discrete sources (e.g., galaxies). Isotropy observed along a single worldline is, however, not sufficient to establish the universe is well described by an FLRW geometry. A further assumption that our worldline is not the *only* vantage point from which the universe appears isotropic, often called the Copernican principle, is needed. Granting this principle, there are theorems establishing that observations of almost isotropic background radiation implies that the spacetime geometry is almost FLRW.[^note-10] The principle itself cannot be established directly via observations (see §2). Given that we live in an almost FLRW models, we need to determine its parameters such as the Hubble constant $H_0$ and the deceleration parameter $q_0 \coloneqq {-}\ddot{R}/(RH_0^2)$, which measures how the rate of expansion is changing, and the normalized density parameters $\Omega_m\coloneqq \rho_m/(3H_0^2)$ for each matter or energy density component $m$. There are a variety of ways to determine the accuracy of the background evolution described by the FLRW models, which depends on these parameters. For this purpose, cosmologists seek effective standard candles and standard rulers—objects with a known intrinsic luminosity and length, respectively, which can then be used to measure the expansion history of the universe.

The second main avenue of testing focuses on the SM’s account of structure formation, which describes the evolution of small perturbations away from the background FLRW geometry in terms of a small number of parameters such as the tilt $n_s$ and the scalar to tensor ratio $r$. Observations from different epochs, such as temperature anisotropies in the CMB and the matter power spectrum based on galaxy surveys, can be used as independent constraints on these parameters as well as on the background parameters (indeed such observations turn out to give the best constraints on the background model parameters). These two routes to testing almost FLRW spacetime geometry are closely linked because the background model provides the context for the evolution of perturbations under the dynamics described by general relativity.

The remarkable success of perturbed FLRW models in describing the observed universe has led many cosmologists to focus almost exclusively on them, yet there are drawbacks to such a myopic approach. For example, the observations at best establish that the observed universe can be well-approximated by an almost FLRW model within some (large) domain. But they are not the only models that fit the data: there are other cosmological models that mimic FLRW models in the relevant domain, yet differ dramatically elsewhere (and elsewhen). Specifically, on the one hand there are a class of spatially homogeneous and anisotropic models (Bianchi models) that exhibit “intermediate isotropization”: namely, they have physical properties that are arbitrarily close to (isotropic) FLRW models over some time scale $T$.[^note-11] Agreement over the time interval $T$ does not imply global agreement, however, as these models have large anisotropies at other times. Relying on the FLRW models in making extrapolations to the early or late universe requires some justification for ignoring models, such as these Bianchi models, that mimic their behavior for a finite time interval. On the other hand there are inhomogeneous spherically symmetric models that can reproduce exactly the background model observations (number counts versus redshifts and angular diameter distance versus redshift, for example) with or without a cosmological constant (Mustapha et al. 1997)[^mustapha-1997]. These can be excluded by direct observations with good enough standard candles (Clarkson et al. 2008)[^clarkson-2008] or by observations of structure formation features in such universes (Clarkson & Maartens 2010)[^clarkson-2010]; but that exclusion cannot take place unless one indeed examines such models and their observational consequences.

Lack of knowledge of the full space of solutions to EFE makes it difficult to assess the fragility of various inferences cosmologists make based on perturbed FLRW models. A fragile inference depends on the properties of the model holding exactly, contrasted with robust inferences that hold even if the models are good approximations (up to some tolerable error) that will hold even if the model is perturbed. The singularity theorems (Hawking & Ellis 1973)[^hawking-1973], for example, establish that the existence of an initial singularity is robust: rather than being features specific to the FLRW models, or other highly symmetric models, singularities are generic in models satisfying physically plausible assumptions. The status of various other inferences cosmologists make is less clear. For example, how sensitively does the observational case in favor of dark energy, which contributes roughly 70% of the total energy density of the universe in the SM, depend upon treating the universe as having almost-FLRW spacetime geometry? As mentioned above, recent work has pursued the possibility of accounting for the same observations based upon large-scale inhomogeneities or local back-reaction, without recourse to dark energy.[^note-12] Studies along these lines are needed to evaluate the possibility that subtle dynamical effects, absent in the FLRW models, provide alternative explanations of observed phenomena. The deduction also depends on the assumption that the EFE hold at cosmological scales - which may not be true: maybe for example some form of scalar-tensor theory should be used. More generally, an assessment of the reliability of a variety of cosmological inferences requires detailed study of a larger space of cosmological models.

### 1.3 Historical Epochs

The SM’s account of the evolution of the matter and radiation in the universe reflects the dynamical effect of expansion. Consider a cube of spacetime in the early universe, filled with matter and radiation. The dynamical effects of the universe’s expansion are locally the same as slowly stretching the cube. For some stages of evolution the contents of the cube interact sufficiently quickly that they reach and stay in local thermal equilibrium as the cube changes volume. (Because of isotropy, equal amounts of matter and radiation enter and leave the cube from neighboring cubes.) But when the interactions are too slow compared to the rate of expansion, the cube changes volume too rapidly for equilibrium to be maintained. As a result, particle species “freeze out” and decouple, and entropy increases. Without a series of departures from equilibrium, cosmology would be boring—the system would remain in equilibrium with a state determined solely by the temperature, without a trace of things past. The rate of expansion of the cube varies with cosmic time. Because radiation, matter, and a cosmological constant term (or dark energy) dilute with expansion at different rates, an expanding universe naturally falls into separate epochs, characterized by different expansion rates.

There are several distinctive epochs in the history of the universe, according to the SM, including the following:

- *Quantum gravity*: Classical general relativity is expected to fail at early times, when quantum effects will be crucial in describing the gravitational degrees of freedom. There is considerable uncertainty regarding physics at this scale.
- *Inflation*: A period of exponential, quasi-De Sitter expansion driven by an “inflaton” field (or fields), leading to a uniform, almost flat universe with Gaussian linear nearly scale invariant density perturbations. During inflation pre-existing matter and radiation are rapidly diluted; the universe is repopulated with matter and energy by the decay of the inflaton field into other fields at the end of inflation (“re-heating”).
- *Big Bang Nucleosynthesis*: At $t \approx 1$ second, the constituents of the universe include neutrons, protons, electrons, photons, and neutrinos, tightly coupled and in local thermal equilibrium. Synthesis of light elements occurs during a burst of nuclear interactions that transpire as the universe falls from a temperature of roughly $10^9$ K to $10^8$ K after neutrinos fall out of equilibrium and consequent onset of neutron decay. The predicted light-element abundances depend on physical features of the universe at this time, such as the total density of baryonic matter and the baryon to photon ratio. Agreement between theory and observation for a specific baryon to photon ratio (Steigman 2007)[^steigman-2007] is a great success of the SM.
- *Decoupling*: As the temperature drops below $\approx 4,000 K$, electrons become bound in stable atoms, and photons decouple from the matter with a black-body spectrum. With the expansion of the universe, the photons cool adiabatically but retain a black-body spectrum with a temperature $T \propto 1/R$. This “cosmic background radiation” (CBR) has been aptly called the cosmic Rosetta stone because it carries so much information about the state of the universe at decoupling (Ade et al. 2016)[^ade-2016].
- *Dark Ages*: After decoupling, baryonic matter consists almost entirely of neutral hydrogen and helium. Once the first generation of stars form, the dark ages come to an end with light from the stars, which re-ionizes the universe.
- *Structure Formation*: Cold dark matter dominates the early stages of the formation of structure. Dark matter halos provide the scaffolding for hierarchical structure formation. The first generation of stars aggregate into galaxies, and galaxies into clusters. Massive stars end their lives in supernova explosions and spread through space heavy elements that have been created in their interiors, enabling formation of second generation stars surrounded by planets.
- *Dark Energy Domination*: Dark energy (or a non-zero cosmological constant) eventually comes to dominate the expansion of the universe, leading to accelerated expansion.[^note-13] This expansion will be never-ending if the dark energy is in fact a cosmological constant.

### 1.4 Status of the Standard Model

The development of a precise cosmological model compatible with the rich set of cosmological data currently available is an impressive achievement. Cosmology clearly relies very heavily on theory; the cosmological parameters that have been the target of observational campaigns are only defined given a background model. The strongest case for accepting the SM rests on the evidence in favor of the underlying physics, in concert with the overdetermination of cosmological parameters. The SM includes several free parameters, such as the density parameters characterizing the abundance of different types of matter, each of which can be measured several ways.[^note-14] These methods have distinctive theoretical assumptions and sources of error. For example, the abundance of deuterium produced during big bang nucleosynthesis depends sensitively on the baryon density. Nucleosynthesis is described using well-tested nuclear physics, and the light element abundances are frozen in within the “first three minutes”. The amplitudes of the acoustic peaks in the CMB angular power spectrum depend on the baryon density at the time of decoupling. Current measurements fix the baryon density to an accuracy of one percent, and the values determined by these two methods agree within observational error. This agreement is one of many consistency checks for the SM.[^note-15] There are important discrepancies, such as that between local versus global measurements of the Hubble parameter $H_0$ (Luković et al. 2016; Bernal et al. 2016)[^bernal-2016][^luković-2016]. The significance and further implications of these discrepancies is not clear.

The SM from nucleosynthesis on can be regarded as well supported by many lines of evidence. The independence and diversity of the measurements provides some assurance that the SM will not be undermined by isolated theoretical mistakes or undetected sources of systematic error. But the SM is far from complete, and there are three different types of significant open issues.

First, we do not understand three crucial components of the SM that require new physics. We do not have a full account of the nature, or underlying dynamics, of dark matter (Bertone et al. 2005)[^bertone-2005], dark energy (Peebles & Ratra 2003)[^peebles-2003], or the inflaton field (Lyth & Riotto 1999; Martin et al. 2014)[^lyth-1999][^martin-2014]. These are well-recognized problems that have inspired active theoretical and observational work, although as we note below in §2.4 they will be challenging to resolve due to inaccessibility of physics at the appropriate scale.

The second set of open questions regards structure formation. While the account of structure formation matches several significant observed features, such as the correlations among galaxies in large scale surveys, there are a number of open questions about how galaxies form (Silk 2017)[^silk-2017]. Many of these, such as the cusp-core problem (Weinberg et al. 2015)[^weinberg-2015], and the dark halos problem (a great many more small dark halos are predicted around galaxies than observed) regard features of galaxies on relatively small scales, which require detailed modeling of a variety of astrophysical processes over an enormous dynamical range. This is also a very active area of research, driven in particular by a variety of new lines of observational research and large-scale numerical simulations.

The third and final set of open issues regards possible observations that would show that the SM is substantially wrong. Any scientific theory should be incompatible with at least some observations, and that is the case for the SM. In the early days of relativistic cosmology, the universe was judged to be younger than some stars or globular clusters. This conflict arose due to a mistaken value of the Hubble constant. There is currently no such age problem for the SM, but obviously discovering an object older than 13.7 Gyr would force a major re-evaluation of current cosmological models. Another example would be if there was not a dipole in matter number counts that agrees with the CMB dipole (Ellis & Baldwin 1984)[^ellis-1984].

### 1.5 Local vs. Global Interplay in Cosmology

Although cosmology is generally seen as fitting into the general physics paradigm of everything being determined in a bottom up manner, as in the discussion above, there is another tradition that sees the effect of the global on the local in cosmology.

The traditional issues of this kind (Bondi 1960; Ellis & Sciama 1972; Ellis 2002)[^bondi-1960][^ellis-2002][^ellis-1972] are

- *Mach’s Principle*: the idea that the origin of inertia is due to the very distant matter in the universe (Barbour & Pfister 1995)[^barbour-1995], nowadays understood as being due to the fact that the vorticity $\omega$ of the universe is very low at present (it could have been otherwise);
- *Olber’s Paradox*: the issue of why the sky is dark at night (Harrison 1984)[^harrison-1984], resolved by evolution of the universe together with the redshift factor of about 1000 since the surface of last scattering (which determines that the temperature of the night sky is the 2.73K of the CMB everywhere except for the small fraction of the sky covered by stars and galaxies)
- *The Arrow of Time*: where does the arrow of time come from, if the underlying physics is time symmetric? This has to be due to special initial conditions at the start of the universe (Ellis 2007)[^ellis-2007]. This is related to the Sommerfeld outgoing radiation condition and Penrose’s Weyl curvature hypothesis (Penrose 2016)[^penrose-2016].

In each case, global boundary conditions have an important effect on local physics. More recent ones relate to

- *Nucleosynthesis*, where the course of nuclear reactions is determined by the $T(t)$ relation that is controlled by cosmological evolution (Steigman 2007)[^steigman-2007] (the temperature $T$ being a coarse grained variable with evolution determined by the average density $\rho$ of matter in the universe through the Friedmann equation)
- *Structure formation* due to gravitational instability (Mukhanov et al. 1992)[^mukhanov-1992], which is affected crucially by the expansion of the universe, which turns what would have been an exponential growth of inhomogeneity(in a static universe) to a power law growth. It is because of this effect that studies of structure such as the BAO and CMB anisotropies give us strong limits on the parameters of the background model (Ade et al. 2016)[^ade-2016].
- *The Anthropic Principle*, discussed below (§4.1), whereby large-scale conditions in the universe (such as the value of the cosmological constant and the initial amplitude of inhomogeneities in the early universe) provide local conditions suitable for life to come into being.

Relevant to all this is the idea of an “effective horizon”: the domain that has direct impact on structures existing on the Earth, roughly 1 Mpc co-moving sphere, see Ellis & Stoeger 2009. This is the part of the universe that actually has a significant effect on our history.

## 2. Underdetermination

Many philosophers hold that evidence is not sufficient to determine which scientific theory we should choose. Scientific theories make claims about the natural world that extend far beyond what can be directly established through observations or experiments. Rival theories may fare equally well with regard to some body of data, yet give quite different accounts of the world. Philosophers often treat the existence of such rivals as inevitable: for a given theory, it is always possible to construct rival theories that have “equally good fit” with available data. Duhem (1914 [1954]) gave an influential characterization of the difficulty in establishing physical theories conclusively, followed a half century later by Quine’s arguments for a strikingly general version of underdetermination (e.g., Quine 1970)[^quine-1970]. The nature of this proposed underdetermination of theory by evidence, and appropriate responses to it, have been central topics in philosophy of science (Stanford 2009 [2016])[^stanford-2009]. Although philosophers have identified a variety of distinct senses of underdetermination, they have generally agreed that underdetermination poses a challenge to justifying scientific theories.

There is a striking contrast with discussions of underdetermination among scientists, who often emphasize instead the enormous difficulty in constructing compelling rival theories.[^note-16] This contrast reflects a disagreement regarding how to characterize the empirical content of theories. Suppose that the empirical content of theory consists of a set of observational claims implied by the theory. Philosophers then take the existence of rival theories to be straightforward. Van Fraassen (1980), for example, defines a theory as “empirically adequate” if what it says about observable phenomena is true, and argues that for any successful theory there are rival theories that disagree about theoretical claims. If we demand more of theories than empirical adequacy in this sense, it is possible to draw distinctions among theories that philosophers would regard as underdetermined. Furthermore, even when scientists do face a choice among competing theories, they are almost never rivals in the philosopher’s sense. Instead, they differ in various ways: intended domain of applicability, explanatory scope, importance attributed to particular problems, and so on.

The scientists’ relatively dismissive attitude towards alleged underdetermination threats may be based on a more demanding conception of empirical success.[^note-17] Scientists demand much more of their theories than mere compatibility with some set of observational claims: they must fit into a larger explanatory scheme, and be compatible with other successful theories. Given a more stringent account of empirical success it is much more challenging to find rival theories. (We return to this issue in §5 below.)

One aspect of underdetermination (emphasized by Stanford 2006)[^stanford-2006] is of more direct relevance to scientific debates: current theories may be indistinguishable, within a restricted domain, from a successor theory, even though the successor theory makes different predictions for other domains. This raises the question of how far we can rely on extrapolating a theory to a new domain. For example, despite its success in describing objects moving with low relative velocities in a weak gravitational field, where it is nearly indistinguishable from general relativity, Newtonian gravity does not apply to other regimes. How far, then, can we rely on a theory to extend our reach? The obstacles to making such reliable inferences reflect the specific details of particular domains of inquiry. Below we will focus on the obstacles to answering theoretical questions in cosmology due to the structure of the universe and our limited access to phenomena.

### 2.1 Underdetermination in Cosmology

Given the grand scope of cosmology, one might expect that many questions must remain unresolved. Basic features of the SM impose two fundamental limits to the ambitions of cosmological theorizing. First, the finitude of the speed of light ensures that we have a limited observational window on the universe due to existence of the visual horizon, representing the most distant matter from which we can receive and information by electromagnetic radiation, and the particle horizon, representing the most distant matter with which we can have had any causal interaction (matter up to that distance can influence what we see at the visual horizon). Recent work has precisely characterized what can be established via idealized astronomical observations, regarding spacetime geometry within, or outside, our past light cone (the observationally accessible region). Second, in addition to enormous extrapolations of well-tested physics in the SM, cosmologists have explored speculative ideas in physics that can only be tested through their implications for cosmology; the energies involved are too high to be tested by any accelerator on Earth. Ellis (2007) has characterized these speculative aspects of cosmology as falling on the far side of a “physics horizon”. We will briefly discuss how this second type of horizon poses limits for cosmological theorizing. In both cases, the type of underdetermination that arises differs from that discussed in the philosophical literature.

### 2.2 Global Structure

To what extent can observations determine the spacetime geometry of the universe directly? The question can be posed more precisely in terms of the region that is, in principle, accessible to an observer at a location in spacetime $p$—the *causal past*, $J^-(p)$, of that point. This set includes all regions of spacetime from which signals traveling at or below the speed of light can reach $p$. What can observations confined to $J^-(p)$, assuming that GR is valid, reveal about the spacetime geometry of $J^-(p)$ itself, and the rest of spacetime?

The observational cosmology program (Kristian & Sachs 1966; Ellis et al. 1985)[^ellis-1985][^kristian-1966] clarifies the extent to which a set of ideal observations can determine the spacetime geometry directly with minimal cosmological assumptions. (By contrast, the standard approach starts by assuming a background cosmological model and then finding an optimal parameter fit.) Roughly put, the ideal data set consists of a set of astrophysical objects that can be used as standard candles and standard rulers. If the intrinsic properties and evolution of a variety of sources are given, observations can directly determine the area (or luminosity) distance of the sources, and the distortion of distant images determines lensing effects. These observations thus directly constrain the spacetime geometry of the past light cone $C^-(p)$. Number counts of discrete sources (such as galaxies or clusters) can be used to infer the total amount of baryonic matter, again granting various assumptions. Ellis et al. (1985) proved the remarkable result that an appropriate idealized data set of this kind is sufficient, if we grant that EFE hold, to fully fix the spacetime geometry and distribution of matter on the past light cone $C^-(p)$, and from that, in the causal past $J^-(p)$ of the observation point $p$.[^note-18] Observers do not have access to anything like the ideal data set, obviously, and in practice cosmologists face challenges in understanding the nature of sources and their evolution with sufficient clarity that they can be used to determine spacetime geometry, so this is the ideal situation.

What does $J^-(p)$ reveal about the rest of spacetime? In classical GR, we would not expect the physical state on $J^-(p)$ to determine that of other regions of spacetime—even the causal past of a point just to the future of $p$.[^note-19] There are some models in which $J^-(p)$ does reveal more: “small universe” models are closed models with a finite maximum length in all directions that is smaller than the visual horizon (Ellis & Schreiber 1986)[^ellis-1986]. Observers in such a model would be able to “see around the universe” in all directions, and establish some global properties via direct observation because they would be able to see all matter that exists.[^note-20]

Unless this is the case, the causal past for a single observer, and even a collection of causal pasts, place very weak constraints on the global properties of spacetime. The global properties of a spacetime characterize its causal structure, such as the presence or absence of singularities.[^note-21] General relativity tolerates a wide variety of global properties, since EFE impose only a local constraint on the spacetime geometry. One way to make this question precise is to consider whether there are any global properties shared by spacetimes that are constructed as follows. For a given spacetime, construct an indistinguishable counterpart that includes the collection of causal pasts $\{J^-(p)\}$ for all points in the original spacetime. The constructed spacetime is indistinguishable from the first, because for any observer in the first spacetime there is a “copy” of their causal past in the counterpart. It is possible, however, to construct counterparts that do not have the same global properties as the original spacetime. The property of having a Cauchy surface, for example, need not be shared by an indistinguishable counterpart.[^note-22] More generally, the only properties that are guaranteed to hold for an indistinguishable counterpart are those that can be established based on the causal past of a single point. This line of work establishes that (some) global properties cannot be established observationally, and raises the question of whether there are alternative justifications.

### 2.3 Establishing FLRW Geometry?

The case of global spacetime geometry is not a typical instance of underdetermination of theory by evidence, as discussed by philosophers, for two reasons (see Manchak 2009, Norton 2011, Butterfield 2014)[^butterfield-2014][^manchak-2009][^norton-2011]. First, this whole discussion assumes that classical GR holds; the question regards discriminating among models of a given theory, rather than a choice among competing theories. Second, these results establish that all observations available to us that are compatible with a given spacetime, with some appealing global property, are equally compatible with its indistinguishable counterparts. But as is familiar from more prosaic examples of the problem of induction, evidence of past events is compatible, in a similar sense, with many possible futures. Standard accounts of inductive inference aim to justify some expectations about the future as more reasonable, e.g., those based on extending past uniformities. The challenge in this case is to articulate an account of inductive inferences that justifies accepting one spacetime over its indistinguishable counterparts.

As a specific instance of this challenge, consider the status of the cosmological principle, the global symmetry assumed in the derivation of the FLRW models. The results above show that all evidence available to us is equally compatible with models in which the cosmological principle does or does not hold. One might take the principle as holding *a priori*, or as a pre-condition for cosmological theorizing (Beisbart 2009)[^beisbart-2009]. A recent line of work aims to justify the FLRW models by appealing to a weaker general principle in conjunction with theorems relating homogeneity and isotropy. Global isotropy around every point implies global homogeneity, and it is natural to seek a similar theorem with a weaker antecedent formulated in terms of observable quantities. The Ehlers-Geren-Sachs theorem (Ehlers et al. 1968)[^ehlers-1968] shows that if all geodesic fundamental observers in an expanding model find that freely propagating background radiation is exactly isotropic, then their spacetime is an FLRW model. If our causal past is “typical”, observations along our worldline will constrain what other observers should see. This is often called the Copernican principle—namely, no point $p$ is distinguished from other points $q$ by any spacetime symmetries or lack thereof (there are no “special locations”). There are indirect ways of testing this principle empirically: the Sunyaev-Zel’dovich effect can be used to indirectly measure the isotropy of the CBR as observed from distant points. Other tests are direct tests with a good enough set of standard candles, and an indirect test based on the time drift of cosmological redshift. This line of work provides an empirical argument that the observed universe is well-approximated by an FLRW model, thus changing that assumption from a philosophically based starting point to an observationally tested foundation.

### 2.4 Physics Horizon

The Standard Model of particle physics and classical GR provide the structure and framework for the SM. But cosmologists have pursued a variety of questions that extend beyond these core theories. In these domains, cosmologists face a form of underdetermination: should a phenomena be accounted for by extending the core theories, or by changing physical or astrophysical assumptions?

The Soviet physicist Yakov Zel’dovich memorably called the early universe the “poor man’s accelerator”, because relatively inexpensive observations of the early universe may reveal features of high-energy physics well beyond the reach of even the most lavishly funded earth-bound accelerators. For many aspects of fundamental physics, including quantum gravity in particular, cosmology provides the only feasible way to assess competing ideas. This ambitious conception of cosmology as the sole testing ground for new physics extends beyond the standard model of particle physics (which is generally thought to be incomplete, even though there are no observations that contradict it). Big bang nucleosynthesis, for example, is an application of well-tested nuclear physics to the early universe, with scattering cross-sections and other relevant features of the physics fixed by terrestrial experiments. While working out how nuclear physics applied in detail required substantial effort, there was little uncertainty regarding the underlying physics. By contrast, in some domains cosmologists now aim to explain the universe’s history while at the same time evaluating new physics used in constructing it.

This contrast can be clarified in terms of the “physics horizon” (Ellis 2007)[^ellis-2007], which delimits the physical regime accessible to terrestrial experiments and observations, roughly in terms of energy scales associated with different interactions. The horizon can be characterized more precisely for a chosen theory, by specifying the regions of parameter space that can be directly tested by experiments and observations.[^note-23] Aspects of cosmological theories that extend past the physics horizon cannot be independently tested through non-cosmological experiments or observations; the only empirical route to evaluating these ideas is through their implications for cosmology. (This is not to deny that there may be strong theoretical grounds to favor particular proposals, as extensions of the core theories.)

Cosmological physics extending beyond the physics horizon faces an underdetermination threat due to the lack of independent lines of relevant evidence. The case of dark matter illustrates the value of such independent evidence. Dark matter was first proposed to account for the dynamical behavior of galaxy clusters and galaxies, which could not be explained using Newtonian gravitational theory with only the luminous matter observed. Dark matter also plays a crucial role in accounts of structure formation, as it provides the scaffolding necessary for baryonic matter to clump, without conflicting with the uniformity of the CMB.[^note-24] Both inferences to the existence of dark matter rely on gravitational physics, raising the question of whether we should take these phenomena as evidence that our gravitational theory fails, rather than as evidence for a new type of matter. There is an active research program (MOND, for *Mo*dified *N*ewtonian *D*ynamics) devoted to accounting for the relevant phenomena by modifying gravity. Regardless of one’s stance on the relative merits of MOND vs. dark matter (obviously MOND needs to be extended to a relativistic theory), direct evidence of existence of dark matter, or indirect evidence via decay products, would certainly reshape the debate. Efforts have been underway for some time to find dark matter particles through direct interactions with a detector, mediated by the weak force. A positive outcome of these experiments would provide evidence of the existence of dark matter that does not depend upon gravitational theory.[^note-25]

Such independent evidence is not available for two prominent examples of new physics motivated by discoveries in cosmology. “Dark energy” was introduced in studies of structure formation, which employed a non-zero cosmological constant to fit observational constraints (the $\Lambda$CDM models). Subsequent observations of the redshift-distance relation, using supernovae (type Ia) as a standard candle, led to the discovery that the expansion of the universe is accelerating.[^note-26] (For $\ddot{R}>0$ in an FLRW model, there must be a contribution that appears in eqn. ($\ref{eq:Ray}$) like a positive $\Lambda$ term.) Rather than treating these observations as simply determining the value of a parameter in the SM, many cosmologists have developed phenomenological models of “dark energy” that leads to an effective $\Lambda$. Unlike dark matter, however, the properties of dark energy insure that any attempt at non-cosmological detection would be futile: the energy density is so small, and uniform, that any local experimental study of its properties is practically impossible. Furthermore these models are not based in well-motivated physics: they have the nature of ‘saving the phenomena’ in that they are tailored to fitting the cosmological observations by curve fitting.[^note-27]

Inflationary cosmology originally promised a powerful unification of particle physics and cosmology. The earliest inflationary models explored the consequences of specific scalar fields introduced in particle physics (the then supposed Higgs field for the strong interactions). Yet theory soon shifted to treating the scalar field responsible for inflation as the “inflaton” field, leaving its relationship to particle physics unresolved, and the promise of unification unfulfilled. If the properties of the inflaton field are unconstrained, inflationary cosmology is extremely flexible; it is possible to construct an inflationary model that matches any chosen evolutionary history of the early universe.[^note-28] Specific models of inflation, insofar as they specify the features of the field or fields driving inflation and its initial state, do have predictive content. In principle, cosmological observations could determine some of the properties of the inflaton field and so select among them (Martin et al. 2014)[^martin-2014]. This could in principle then have implications for a variety of other experiments or observations; yet in practice the features of the inflaton field in most viable models of inflation guarantee that it cannot be detected in other regimes. The one exception to this is if the inflaton were the electroweak Higgs particle detected at the LHC (Ellis & Uzan 2014)[^ellis-2014]. This remains a viable inflaton candidate, so testing if it is indeed the inflaton is an important task (Bezrukov & Gorbunov 2012)[^bezrukov-2012].

The physics horizon poses a challenge because one particularly powerful type of evidence—direct experimental detection or observation, with no dependence on cosmological assumptions—is unavailable for the physics relevant at earliest times (before inflation, and indeed even for baryosynthesis after inflation). Yet this does not imply that competing theories, such as dark matter vs. modified gravity, should be given equal credence. The case in favor of dark matter draws on diverse phenomena, and it has been difficult to produce a compelling modified theory of gravity, consistent with GR, that captures the full range of phenomena as an alternative to dark matter. Cosmology typically demands a more intricate assessment of background assumptions, and the degree of independence of different tests, in evaluating proposed extensions of the core theories. Yet this evidence may still be sufficiently strong, in the sense discussed more fully in §5 below, to justify new physics.

### 2.5 Cosmic Variance

There is a distinctive form of underdetermination regarding the use of statistics in cosmology, due to the uniqueness of the universe. To compare the universe with the statistical predictions of the SM, we conceptualize it as one realization of a family of possible universes, and compare what we actually measure with what is predicted to occur in the ensemble of hypothetical models. When they are significantly different, the key issue is: Are these just statistical fluctuations we can ignore? Or are they serious anomalies that need an explanation?

This question arises in several concrete cases:

- Existence of low CMB anisotropy power at high and angular scales relative to that predicted by the SM (Schwarz et al. 2016; Knight & Knox 2017)[^knight-2017][^schwarz-2016]
- Existence of a CMB cold spot of substantial size (Zhang & Huterer 2010; Schwarz et al. 2016)[^schwarz-2016][^zhang-2010].
- Disagreement about the value of the Hubble parameter as measured directly in the local region on the one hand, and as deduced from CMB anisotropies on the other (Luković et al. 2016; Bernal et al. 2016)[^bernal-2016][^luković-2016].

How do we decide? This will depend on the particular measurement (see e.g., Kamionkowski & Loeb 1997; Marra et al. 2013)[^kamionkowski-1997][^marra-2013], but in general because of the uniqueness of the universe, we don’t know if these potential anomalies are real, pointing to serious problems with the models, or not real—just statistical flukes in the way the family of models differs from the one instance that we have at hand, the unique universe that actually exists. In all the physical sciences, this is a unique problem of cosmology.[^note-29]

## 3. Origins of the Universe

Cosmology confronts a distinctive challenge in accounting for the origin of the universe. In most other branches of physics the initial or boundary conditions of a system do not call out for theoretical explanation. They may reflect, for example, the impact of the environment, or an arbitrary choice regarding when to cut off the description of a subsystem of interest. But in cosmology there are heated debates regarding what form a “theory of the initial state” should take, and what it should contribute to our understanding of the universe. This basic question regarding the nature of aims of a theory of origins has significant ramifications for various lines of research in cosmology.

### 3.1 The Initial State

Contemporary cosmology at least has a clear target for a theory of origins: the SM describes the universe as having expanded and evolved over 13.7 billion years from an initial state where many physical quantities diverged. In the FLRW models, the cosmic time $t$ can be measured by the total proper time elapsed along the worldline of a fundamental observer, from the “origin” of the universe until the present epoch. Extrapolating backwards from the present, various quantities diverge as the cosmic time $t \rightarrow 0$—for example, $R(t) \rightarrow 0$ and the matter density goes to infinity.[^note-30] The worldlines of observers cannot be extended arbitrarily far into the past. Although there is no “first moment” of time, because the very concept of time breaks down as $t\rightarrow 0$, the age of the universe is the maximum length of these worldlines.

### 3.2 Singularity Theorems

The singularity theorems proved in the 60s (see, in particular, Hawking & Ellis 1973)[^hawking-1973] show that the universe is finite to the past in a broad class of cosmological models. Past singularities, signaled by the existence of inextendible geodesics with bounded length, must be present in models with a number of plausible features. (Geodesics are the curves of extreme length through curved spacetime, and freely falling bodies follow timelike geodesics.) Intuitively, extrapolating backwards from the present, an inextendible geodesic reaches, within finite distance, an “edge” beyond which it cannot be extended. There is not a uniquely defined “cosmic time”, in general, but the maximum length of these curves reflects the finite age of the universe. The singularity theorems plausibly apply to the observed universe, within the domain of applicability of general relativity. There are various related theorems differing in detail, but one common ingredient is an assumption that there is sufficient matter and energy present to guarantee that our past light cone refocuses.[^note-31] The energy density of the CMB alone is sufficient to justify this assumption. The theorems also require an energy condition: a restriction on the types of matter present in the model, guaranteeing that gravity leads to focusing of nearby geodesics. (In eqn. ($\ref{eq:Ray}$) above, this is the case if $\rho_{\textit{grav}} > 0$ and $\Lambda=0$; it is possible to avoid a singularity with a non-zero cosmological constant, for example, since it appears with the opposite sign as ordinary matter, counteracting this focusing effect.)

The prediction of singularities is usually taken to be a deep flaw of GR.[^note-32] One potential problem with singularities is that they may lead to failures of determinism, because the laws “break down” in some sense. This concern only applies to some kinds of singularities, however. Relativistic spacetimes that are globally hyperbolic have Cauchy surfaces, and appropriate initial data posed on such surfaces fix a unique solution throughout the spacetime. Global hyperbolicity does not rule out the existence of singularities, and in particular the FLRW models are globally hyperbolic in spite of the existence of an initial singularity. The threat to determinism is thus more qualified: the laws do not apply “at the singularity itself” even though the subsequent evolution is fully deterministic, and there are some types of singularities that pose more serious threats to determinism.

Another common claim is that the presence of singularities establish that GR is incomplete, since it fails to describe physics “at the singularity”.[^note-33] This is difficult to spell out fully without a local analysis of singularities, which would give precise meaning to talk of “approaching” or being “near” the singularity. In any case, it is clear that the presence of a singularity in a cosmological model indicates that spacetime, as described by GR, comes to an end: there is no way of extending the spacetime through the singularity, without violating mathematical conditions needed to insure that the field equations are well-defined. Any description of physical conditions “before the big bang” must be based on a theory that supersedes GR, and allows for an extension through the singularity.

There are two limitations regarding what we can learn about the origins of the universe based on the singularity theorems. First, although these results establish the existence of an initial singularity, they do not provide much guidance regarding its structure. The spacetime structure near a “generic” initial singularity has not yet been fully characterized. Partial results have been established for restricted classes of solutions; for example, numerical simulations and a number of theorems support the BKL conjecture, which holds that isotropic, inhomogeneous models exhibit a complicated form of chaotic, oscillatory behavior. The resulting picture of the approach to the initial singularity contrasts sharply with that in FLRW models.[^note-34] It is also possible to have non-scalar singularities (Ellis & King 1974)[^ellis-1974].

Second, classical general relativity does not include quantum effects, which are expected to be relevant as the singularity is approached. Crucial assumptions of the singularity theorems may not hold once quantum effects are taken into account. The standard energy conditions do not hold for quantum fields, which can have negative energy densities. This opens up the possibility that a model including quantum fields may exhibit a “bounce” rather than collapse to a singularity. More fundamentally, GR’s classical spacetime description may fail to approximate the description provided by a full theory of quantum gravity. According to recent work applying loop quantum gravity to cosmology, spacetime collapses to a minimum finite size rather than reaching a true singularity (Ashtekar & Singh 2011; Bojowald 2011)[^ashtekar-2011][^bojowald-2011]. On this account, GR fails to provide a good approximation in the region of the bounce, and the apparent singularity is an artifact. Classical spacetime “emerges” from a state to which familiar spacetime concepts do not apply. There are several accounts of the early universe, motivated by string theory and other approaches, that similarly avoid the initial singularity due to quantum gravity effects.

### 3.3 Puzzling Features of the Initial State

In practice, cosmologists often take the physical state at the expected boundary of the domain of applicability of GR as the “initial state”. (For example, this might be taken as the state specified on a spatial hypersurface at a very early cosmic time. However, the domain of applicability of GR is not well understood, given uncertainty about quantum gravity.) Projecting observed features of the universe backwards leads to an initial state with three puzzling features:[^note-35]

- *Uniformity*: The FLRW models have a finite particle horizon distance, much smaller than the scales at which we observe the CMB.[^note-36] Yet the isotropy of the CMB, among other observations, indicate that distant regions of the universe have uniform physical properties.
- *Flatness*: An FLRW model close to the “flat” model, with nearly critical density at some specified early time is driven rapidly away from critical density under FLRW dynamics if $\Lambda = 0$ and $\rho+3p>0$. Given later observations, the initial state has to be *very* close to the flat model (or, equivalently, *very* close to critical density, $\Omega=1$) at very early times.[^note-37]
- *Perturbations*: The SM includes density perturbations that are coherent on large scales and have a specific amplitude, constrained by observations. It is challenging to explain both properties dynamically. In the standard FLRW models, the perturbations have to be coherent on scales much larger than the Hubble radius at early times.[^note-38]

On a more phenomenological approach, the gravitational degrees of freedom of the initial state could simply be chosen to fit with later observations, but many proposed “theories of initial conditions” aim to account for these features based on new physical principles. The theory of inflation discussed below aims to explain these issues.

### 3.4 Theories of the Initial State

There are three main approaches to theories of the initial state, all of which have been pursued by cosmologists since the late 60s in different forms. Expectations for what a theory of initial conditions should achieve have been shaped, in particular, by inflationary cosmology. Inflation provided a natural account of the three otherwise puzzling features of the initial state emphasized in the previous section. Prior to inflation, these features were regarded as “enigmas” (Dicke & Peebles 1979)[^dicke-1979], but after inflation, accounting for these features has served as an eligibility requirement for any proposed theory of the early universe.

The first approach aims to reduce dependence on special initial conditions by introducing a phase of attractor dynamics. This phase of dynamical evolution “washes away” the traces of earlier states, in the sense that a probability distribution assigned over initial states converges towards an equilibrium distribution. Misner (1968) introduced a version of this approach (his “chaotic cosmology program”), proposing that free-streaming neutrinos could isotropize an initially anisotropic state. Inflationary cosmology was initially motivated by a similar idea: a “generic” or “random” initial state at the Planck time would be expected to be “chaotic”, far from a flat FLRW model. During an inflationary stage, arbitrary initial states are claimed to converge towards a state with the three features described above.

The second approach regards the initial state as extremely special rather than generic. Penrose, in particular, has argued that the initial state must be very special to explain time’s arrow; the usual approaches fail to take seriously the fact that gravitational degrees of freedom are not excited in the early universe like the others (Penrose 2016)[^penrose-2016]. Penrose (1979) treats the second law as arising from a law-like constraint on the initial state of the universe, requiring that it has low entropy. Rather than introducing a subsequent stage of dynamical evolution that erases the imprint of the initial state, we should aim to formulate a “theory of initial conditions” that accounts for its special features. Penrose’s conjecture is that the Weyl curvature tensor approaches zero as the initial singularity is approached; his hypothesis is explicitly time asymmetric, and implies that the early universe approaches an FLRW solution. (It does not account for the observed perturbations, however.) Later he proposed the idea of Conformal Cyclic Cosmology, where such a special initial state at the start of one expansion epoch is the result of expansion in a previous epoch that wiped out almost all earlier traces of matter and radiation (Penrose 2016)[^penrose-2016].

A third approach rejects the framework accepted by the other two proposals, and regards the “initial state” as a misnomer: it should instead by regarded as a “branch point” where our pocket universe separated off from a larger multiverse. (There are still, of course, questions regarding the initial state of the multiverse ensemble, if one exists.) We will return to this approach in §5 below.

A dynamical approach, even if it is successful in describing a phase of the universe’s evolution, arguably does not offer a complete solution to the problem of initial conditions: it collapses into one of the other two approaches. For example, an inflationary stage can only begin in a region of spacetime if the inflaton field and the geometry are uniform over a sufficiently large region, such that the stress-energy tensor is dominated by the potential term (implying that the derivative terms are small) and the gravitational entropy is small. There are other model-dependent constraints on the initial state of the inflaton field. One way to respond is to adopt Penrose’s point of view, namely that this reflects the need to choose a special initial state, or to derive one from a previous expansion phase. The majority of those working in inflationary cosmology instead appeal to the third approach: rather than treating inflation as an addition to standard big-bang evolution in a single universe, we should treat the observed universe as part of a multiverse, discussed below. But even this must have a theory of initial conditions.

### 3.5 The Limits of Science

Cosmology provokes questions about the limits of scientific explanation because it lacks many of the features that are present in other areas of physics. Physical laws are usually regarded as capturing the features of a type of system that remain invariant under some changes, and explanations often work by placing a particular event in larger context. Theories of the initial state cannot appeal to either idea: we have access to only one universe, and there is no larger context to appeal to in explaining its properties. This contrast between the types of explanation available in cosmology and other areas of physics has often led to dissatisfaction (see, e.g., Unger & Smolin 2014)[^unger-2014]. At the very least, cosmology forces us to reconsider basic questions about modalities, and what constitutes scientific explanation.

One challenge to establishing theories of the initial state is entirely epistemic. As emphasized in §2.4, we lack independent experimental probes of physics at the relevant scales, so the extensions of core theories described above are only tested indirectly through their implications for cosmology. This limitation reflects contingent facts about the universe, namely the contrast between the energy scales of the early universe and those accessible to us, and does not follow from the uniqueness of the universe per se. Yet this limitation does not imply that it would be impossible to establish laws. There are cases in the history of physics, such as celestial mechanics, where confidence in a theory’s laws is based primarily on successful application under continually improving standards of precision.

A further conceptual challenge regards whether it even makes sense to seek “laws” in cosmology (Munitz 1962; Ellis 2007)[^ellis-2007][^munitz-1962]. Laws are usually taken to cover multiple instances of some type of phenomena, or family of objects. What can we mean by “laws” for a unique object (the universe as a whole) or a unique event (its origin)?

Competing philosophical analyses of laws of nature render different verdicts on the possibility of cosmological laws. Cosmological laws, if possible, differ from local physical laws in a variety of ways—they do not apply to subsystems of the universe, they lack multiple instances, and etc. Philosophical accounts of laws take different features to be essential to law-hood. For example, the influential Mill-Ramsey-Lewis account takes the laws to be axioms of the deductive system capturing some body of physical knowledge that optimally balances strength (the scope of derived claims) and simplicity (the number of axioms) (see, e.g., Loewer 1996)[^loewer-1996]. It is quite plausible that a constraint on the initial state, such as Penrose’s Weyl curvature hypothesis, would count as a law on this account. By contrast, accounts that take other features, such as governing evolution, as essential, reach the opposite verdict.

Finally, there are a number of conceptual pitfalls regarding what would count as an adequate “explanation” of the origins of the universe. What is the target of such explanations, and what can be used in providing an explanation? The target might be the state defined at the earliest time when extrapolations based on the SM can be trusted. The challenge is that this state then needs to be explained in terms of a physical theory, quantum gravity, whose basic concepts are still obscure to us. This is a familiar challenge in physics, where substantial work is often required to clarify how central concepts (such as space and time) are modified by a new theory. An explanation of origins in this first sense would explain how it is that classical spacetime emerges from a quantum gravity regime. While any such proposals remain quite speculative, the form of the explanation is similar to other cases in physics: what is explained is the applicability of an older, less fundamental theory within some domain. Such an explanation does not address ultimate questions regarding why the universe exists—instead, such questions are pushed back one step, into the quantum gravity regime.

Many discussions of origins pursue a more ambitious target: they aim to explain the creation of the universe “from nothing”.[^note-39] The target is the true initial state, not just the boundary of applicability of the SM. The origins are supposedly then explained without positing an earlier phase of evolution; supposedly this can be achieved, for example, by treating the origin of the universe as a fluctuation away from a vacuum state. Yet obviously a vacuum state is not nothing: it exists in a spacetime, and has a variety of non-trivial properties. It is a mistake to take this explanation as somehow directly addressing the metaphysical question of why there is something rather than nothing.[^note-40]

## 4. Anthropic Reasoning and Multiverse

### 4.1 Anthropic Reasoning

The physical conditions necessary for our existence impose a selection effect on what we observe. The significance of this point for cosmological theorizing is exemplified by Dicke’s criticism of Dirac’s speculative “large number hypothesis”. Dirac (1937) noted the age of the universe expressed in terms of fundamental constants in atomic physics is an extremely large number (roughly $10^{39}$), which coincides with other large, dimensionless numbers defined in terms of fundamental constants. Inspired by this coincidence, he proposed that the large numbers vary to maintain this order of magnitude agreement, implying (for example) that the gravitational “constant” $G$ is a function of cosmic time. Dicke (1961) noted that creatures like us, made of carbon produced in an earlier generation of red giants and sustained by the light and heat of a main sequence star, can only exist within a restricted interval of cosmic times, and that Dirac’s coincidence holds for observations made within this interval. Establishing that the coincidence holds at a randomly chosen $t$ would support Dirac’s hypothesis, however slightly, but Dicke’s argument shows that *our* evidence does not do so.

Dicke’s reasoning illustrates how taking selection effects into account can mitigate surprise, and undermine the apparent implications of facts like those noted by Dirac (see Roush 2003)[^roush-2003]. These facts reflect biases in the evidence available to us, rather than supporting his hypothesis. It is also clear that Dicke’s argument is “anthropic” in only a very limited sense: his argument does not depend on a detailed characterization of human observers. All that matters is that we can exist at a cosmic time constrained by the time scales of stellar evolution.

How to account for selection effects, within a particular approach to confirmation theory, is one central issue in discussions of anthropic reasoning. This question is intertwined with other issues that are more muddled and contentious. Debates among cosmologists regarding “anthropic principles” ignited in the 70s, prompted by the suggestion that finely-tuned features of the universe—such as the universe’s isotropy (Collins & Hawking 1973)[^collins-1973][^hawking-1973]—can be explained as necessary conditions for the existence of observers.[^note-41] More recently, a number of cosmologists have argued that cosmological theories should be evaluated based on predictions for what a “typical” observer should expect to see. These ideas have dovetailed with work in formal epistemology. A number of philosophers have developed extensions of Bayesianism to account for “self-locating” evidence, for example.[^note-42] This kind of evidence includes indexical information characterizing an agent’s beliefs about their identity and location. At present work in this area has not reached a consensus, and we will present a brief overview of some of the considerations that have motivated different positions in these debates.

In cosmology the most famous example of an “anthropic prediction” is Weinberg (1987)’s prediction for $\Lambda$.[^note-43] One part of Weinberg’s argument is similar to Dicke’s: he argued that there are anthropic bounds on $\Lambda$, due to its impact on structure formation. The existence of large, gravitationally bound structures such as galaxies is only possible if $\Lambda$ falls within certain bounds. Weinberg went a step further than Dicke, and considered what value of $\Lambda$ a “typical observer” should see. He assumed that observers occupy different locations within a multiverse, and that the value of $\Lambda$ varies across different regions. Weinberg further argues that the prior probability assigned to different values of $\Lambda$ should be uniform within the anthropic bounds. Typical observers should expect to see a value close to the mean of the anthropic bounds, leading to Weinberg’s prediction for $\Lambda$.

Essential to Weinberg’s argument is an appeal to the principle of indifference, applied to a class of observers.[^note-44] We should calculate what we expect to observe, that is, as if we are a “random choice” among all possible observers.[^note-45] Bostrom (2002) argues that indifference-style reasoning is necessary to respond to the problem of “freak observers”. As Bostrom formulates it, the problem is that in an infinite universe, *any* observation $O$ is true for *some* observer (even if only for an observer who has fluctuated into existence from the vacuum). His response is that we should evaluate theories based not on the claim that *some observer* sees $O$, but on an indexical claim: that is, *we* make the observation $O$. He assumes that we are a “random” choice among the class of possible observers. (How to justify such a strong claim is a major challenge for this line of thought.) If we grant the assumption, then we can assign low probability to the observations of the “freak” observers, and recover the evidential value of $O$.

There are three immediate questions regarding this proposal. The first is called the “reference class” problem. The assignments of probabilities to events requires specifying how they are grouped together.[^note-46] Obviously, what is typical with respect to one reference class will not be typical with respect to another (compare, for example, “conscious observers” with “carbon-based life”). Second, the principle of indifference has been thoroughly criticized as a justification for probability in other contexts; what justifies the use of indifference in this case? Why should we take ourselves as “randomly chosen” among an appropriate reference class? The third problem reflects the intended application of these ideas: Bostrom and other authors in this line of work are particularly concerned with observes that may occupy an infinite universe. There is no proof that the universe is in fact infinite. These are all pressing problems for those who hold that the principle of indifference is essential to making cosmological predictions.

Furthermore, one way of implementing this approach leads to absurd consequences. The Doomsday Argument, for example, claims to reach a striking conclusion about the future of the human species without any empirical input (see, e.g., Leslie 1992; Gott 1993; Bostrom 2002)[^bostrom-2002][^gott-1993][^leslie-1992]. Suppose that we are “typical” humans, in the sense of having a birth rank that is randomly selected among the collection of all humans that have ever lived. We should then expect that there are nearly as many humans before and after us in overall birth rank. For this to be true, given current rates of population growth, there must be a catastrophic drop in the human population (“Doomsday”) in the near future. The challenge to advocates of indifference applied to observers is to articulate principles that avoid such consequences, while still solving (alleged) problems such as that of freak observers.

In sum, one approach to anthropic reasoning aims to clarify the rules of reasoning applicable to predictions made by observers in a large or infinite universe. This line of work is motivated by the idea that without such principles we face a severe skeptical predicament, as observations would not have any bearing on the theory. Yet there is still not general agreement on the new principles required to handle these cases, which are of course not scientifically testable principles: they are philosophically based proposals. According to an alternative approach, selection effects can and should be treated within the context of a Bayesian approach to inductive inference (see Neal 2006; Trotta 2008)[^neal-2006][^trotta-2008]. On this line of thought, “predictions” like those that Bostrom and others hope to analyze play no direct role in the evaluation of cosmological theories, so further principles governing anthropic reasoning are simply not necessary. There is much further work to be done in clarifying and assessing these (and other) approaches to anthropic reasoning.[^note-47]

### 4.2 Fine-Tuning

Fine-tuning arguments start from a conflict between two different perspectives on certain features of cosmology (or other physical theories). On the first perspective, the existence of creatures like us seems to be sensitive to a wide variety of aspects of cosmology and physics. To be more specific, the prospects for life depend sensitively on the values of the various fundamental constants that appear in these theories. The SM includes about 10 constants, and the particle physics standard model includes about 20 more.[^note-48] Tweaking the SM, or the standard model of particle physics, by changing the values of these constants seems to lead to a barren cosmos.[^note-49] Focusing on the existence of “life” runs the risk of being too provincial; we don’t have a good general account of what physical systems can support intelligent life. Yet it does seem plausible that intelligence requires an organism with complex structural features, living in a sufficiently stable environment.

At a bare minimum, the existence of life seems to require the existence of complex structures at a variety of scales, ranging from galaxies to planetary systems to macro-molecules. Such complexity is extremely sensitive to the values of the fundamental constants of nature. From this perspective, the existence of life in the universe is fragile in the sense that it depends sensitively on these aspects of the underlying theory.

This view contrasts sharply with the status of the constants from the perspective of fundamental physics. Particle physicists typically regard their theories as effective field theories, which suffice for describing interactions at some specified energy scale. These theories include various constants, characterizing the relative strength of the interactions they describe, that cannot be further explained by the effective field theory. The constants can be fixed by experimental results, but are not derivable from fundamental physical principles. (If the effective field theory can be derived from a more fundamental theory, the value of the constants can in principle be determined by integrating out higher-energy degrees of freedom. But this merely pushes the question back one step: the constants appearing in the more fundamental theory are determined experimentally.) Similarly, the constants appearing in the SM are treated as contingent features of the universe. There is no underlying physical principle that sets, for example, the cosmological densities of different kinds of matter, or the value of the Hubble constant.

So features of our theories that appear entirely contingent, from the point of view of physics, are necessary to account for the complexity of the observed universe and the very possibility of life. The fine-tuning argument starts from a sense of unease about this situation: shouldn’t something as fundamental as the complexity of the universe be explained by the *laws* or *basic principles* of the theory, and not left to brute facts regarding the values of various constants? The unease develops into serious discomfort if the specific values of the constants are taken to be extremely unlikely: how could the values of all these constants be *just right*, by sheer coincidence?

In many familiar cases, our past experience is a good guide to when an apparent coincidence calls for further explanation. As Hume emphasized, however, intuitive assessments from everyday life of whether a given event is likely, or requires a further explanation, do not extend to cosmology. Recent formulations of fine-tuning arguments often introduce probabilistic considerations. The constants are “fine-tuned”, meaning that the observed values are “improbable” in some sense. Introducing a well-defined probability over the constants would provide a response to Hume: rather than extrapolating our intuitions, we would be drawing on the formal machinery of our physical theories to identify fine-tuning. Promising though this line of argument may be, there is not an obvious way to define physical probabilities over the values of different constants, or over other features of the laws. There is nothing like the structure used to justify physical probabilities in other contexts, such as equilibrium statistical mechanics.[^note-50]

There are four main responses to fine-tuning:

- *Empiricist Denial*: This response follows Hume in denying that a clear problem has even been identified. One form of this response challenges appeals to probability, undermining the claim that there are unexplained coincidences. Alternatively, fine-tuning is taken to reveal that the laws alone are not sufficient to account for some features of nature; these features are properly explained by the laws in conjunction with various contingent facts.
- *Designer*: Newton famously argued, for example, that the stability of the solar system provides evidence of providential design. For the hypothesized Designer to be supported by fine-tuning evidence, we require some way of specifying what kind of universe the Designer is likely to create; only such a specific Design hypothesis, based in some theory of the nature of the Designer, can offer an explanation of fine-tuning.
- *New Physics*: The fine-tuning can be eliminated by modifying physical theory in a variety of ways: altering the dynamical laws, introducing new constraints on the space of physical possibilities (or possible values of the constants of nature), etc.
- *Multiverse*: Fine-tuning is explained as a result of selection, from among a large space of possible universes (or multiverse).

In the next section we discuss the last response in more detail; see §3 for further discussion of the third response.

### 4.3 Multiverse

The multiverse response replaces a single, apparently finely-tuned universe within an ensemble of universes, combined with an appeal to anthropic selection. Suppose that all possible values of the fundamental constants are realized in individual elements of the ensemble. Many of these universes will be inhospitable to life. In calculating the probabilities that we observe specific values of the fundamental constants, we need only consider the subset of universe compatible with the existence of complexity (or some more specific feature associated with life). If we have some way of assigning probabilities over the ensemble, we could then calculate the probability associated with our measured values. These calculations will resolve the fine-tuning puzzles if they show that we observe typical values for a complex (or life-permitting) universe.

Many cosmologists have argued in favor of a specific version of the multiverse called eternal inflation (EI).[^note-51] On this view, the rapid expansion hypothesized by inflationary cosmology continues until arbitrarily late times in some regions, and comes to an end (with a transition to slower expansion) in others. This leads to a global structure of “pocket” universes embedded within a larger multiverse.

On this line of thought, the multiverse should be accepted for the same reason we accept many claims about what we cannot directly observe—namely, as an inevitable consequence of an established physical theory. It is not clear, however, that EI is inevitable, as not all inflationary models, arguably including those favored by CMB observations, have the kind of potential that leads to EI.[^note-52] Accounts of how inflation leads to EI rely on speculative physics.[^note-53] Furthermore, if inflation does lead to EI, that threatens to undermine the original reasons for accepting inflation (Smeenk 2014)[^smeenk-2014]: rather than the predictions regarding the state produced at the end of inflation taken to provide evidence for inflation, EI seems to imply that, as Guth (2007) put it, in EI “anything that can happen will happen; in fact, it will happen an infinite number of times”.

There have been two distinct approaches to recovering some empirical content in this situation.[^note-54] First, there may be traces of the early formation of the pocket universes, the remnants of collisions between neighboring “bubbles”, left on the CMB sky (Aguirre & Johnson 2011)[^aguirre-2011]. Detection of a distinctive signature that cannot be explained by other means would provide evidence for the multiverse. However, there is no expectation that a multiverse theory would generically predict such traces; for example, if the collision occurs too early the imprint is erased by subsequent inflationary expansion.

The other approach regards predictions for the fundamental constants, such as Weinberg’s prediction of $\Lambda$ discussed above. The process of forming the pocket universes is assumed to yield variation in the local, low-energy physics in each pocket. Predictions for the values of the fundamental constants follow from two things: (1) a specification of the probabilities for different values of the constant over the ensemble, and (2) a treatment of the selection effect imposed by restricting consideration to pocket universes with observers and then choosing a “typical” observer.

The aim is to obtain probabilistic predictions for what a typical observer should see in the EI multiverse. Yet there are several challenges to overcome, alongside those mentioned above related to anthropics. The assumption that the formation of pocket universes leads to variation in constants is just an assumption, which is not yet justified by a plausible, well-tested dynamical theory. The most widely discussed challenge in the physics literature is the “measure problem”: roughly, how to assign “size” to different regions of the multiverse, as a first step towards assigning probabilities. It is difficult to define a measure because the EI multiverse is usually taken to be an infinite ensemble, lacking in the kinds of structure used in constructing a measure. On our view, these unmet challenges undercut the hope that the EI multiverse yields probabilistic predictions. And without such an account, the multiverse proposal does not have any testable consequences. If everything happens somewhere in the ensemble, then any potential observation is compatible with the theory.

Supposing that we grant a successful resolution of all these challenges, the merits of a multiverse solution of fine-tuning problems could then be evaluated by comparison with competing ideas. The most widely cited evidence in favor of a multiverse is Weinberg’s prediction for the value of $\Lambda$, discussed above. There are other proposals to explain the observed value of $\Lambda$; Wang, Zhu, and Unruh (2017), for example, treat the quantum vacuum as extremely inhomogeneous, and argue that resonance among the vacuum fluctuations leads to a small $\Lambda$.

The unease many have about multiverse proposals are only reinforced by the liberal appeals to “infinities” in discussion of the idea.[^note-55] Many have argued, for example, that we must formulate an account of anthropic reasoning that applies to a truly infinite, rather than merely very large, universe. Claims that we occupy one of infinitely many possible pocket universes, filled with an infinity of other observers, rest on an enormous and speculative extrapolation. Such claims fail to take seriously the concept of infinity, which is not merely a large number. Hilbert (1925 [1983]) emphasized that while infinity is required to complete mathematics, it does not occur anywhere in the *accessible* physical universe. One response is to require that infinities in cosmology should have a restricted use. It may be useful to introduce infinity as part of an explanatory account of some aspect of cosmology, as is common practice in mathematical models that introduce various idealizations. Yet this infinity should be eliminable, such that the explanation of the phenomena remains valid when the idealization is removed.[^note-56] Even for those who regard this demand as too stringent, there certainly needs to be more care in clarifying and justifying claims regarding infinities.

In sum, interest in the multiverse stems primarily from speculations about the consequences of inflation for the global structure of the universe. The main points of debate regard whether EI is a disaster for inflation, undermining the possibility of testing inflation at all, and how much predictions such as that for $\Lambda$ lend credence to these speculations.[^note-57] Resolution of these questions is needed to decide whether the multiverse can be tested in a stronger sense, going beyond the special cases (such as bubble collisions) that may provide more direct evidence.

## 5. Testing models

As mentioned at the start, the uniqueness of the universe raises specific problems as regards cosmology as a science. First we consider issues to do with verification of cosmological models, and then make a comment as regards interpreting the human implications of cosmology

### 5.1 Criteria

The basic challenge in cosmology regards how to test and evaluate cosmological models, given our limited access to the unique universe. As discussed above, current cosmological models rely in part on extrapolations of well-tested local physics along with novel proposals, such as the inflaton field. The challenge is particularly pressing in evaluating novel claims that only have cosmological implications, due to the physics horizon (§2.4). Distinctions that are routinely employed in other areas of physics, such as that between laws and initial conditions, or chance and necessity, are not directly applicable, due to the uniqueness of the universe.

Recent debates regarding the legitimacy of different lines of research in cosmology reflect different responses to this challenge. One response is to retreat to hypothetico-deductivism (HD): a hypothesis receives an incremental boost in confidence when one of its consequences is verified (and a decrease if it is falsified).[^note-58] Proponents of inflation argue, for example, that inflation should be accepted based on its successful prediction of a flat universe with a specific spectrum of density perturbations. Some advocates of the multiverse take its successful prediction of the value of $\Lambda$ as the most compelling evidence in its favor.

Despite its appeal, there are well-known problems with taking HD as a sufficient account of how evidence supports theories (this is often called “naïve HD”). In particular, the naïve view lacks the resources to draw distinctions among underdetermined rival theories that make the same predictions (see Crupi 2013 [2016])[^crupi-2013]. We take it as given that scientists do draw distinctions among theories that naïve HD would treat as on par, as is reflected in judgments regarding how much a given body of evidence supports a particular theory. Scientists routinely distinguish among, for example, theories that may merely “fit the data” as opposed to those that accurately capture laws governing a particular domain, and evaluate some successful predictions as being far more revealing than others.

A second response is that the challenge requires a more sophisticated methodology. This may take the form of acknowledging explicitly the criteria that scientists use to assess desirability of scientific theories (Ellis 2007)[^ellis-2007], which include considerations of explanatory power, consistency with other theories, and other factors, in addition to compatibility with the evidence. These come into conflict in unexpected ways in cosmology, and these different factors should be clearly articulated and weighed against one another. Alternatively, one might try to show that some of these desirable features, such as the ability to unify diverse phenomena, should be taken as part of what constitutes empirical success.[^note-59] This leads to a more demanding conception of empirical success, exemplified by historical cases such as Perrin’s argument in favor of the atomic constitution of matter.

### 5.2 Scope of Cosmological Theories and Data

Finally, a key issue is what scope do we expect our theories to have. Ellis (2017) makes a distinction between *Cosmology*, which is the physically based subject dealt with in the textbooks listed in this article, dealing with the expansion of the universe, galaxies, number counts, background radiation, and so on, and *Cosmologia*, where one takes all that as given but adds in consideration about the meaning this all has for life. Clearly the anthropic discussions mentioned above are a middle ground.[^note-60] However a number of popular science books by major scientists are appearing that make major claims about Cosmologia, based purely in arguments from fundamental physics together with astronomical observations. We will make just one remark about this here. If one is going to consider Cosmologia seriously, it is incumbent on one to take seriously the full range of data appropriate to that enterprise. That is, the data needed for the attempted scope of such a theory must include data to do with the meaning of life as well as data derived from telescopes, laboratory experiments, and particle colliders. It must thus include data about good and evil, life and death, fear and hope, love and pain, writings from the great philosophers and writers and artists who have lived in human history and pondered the meaning of life on the basis of their life experiences. This is all of great meaning to those who live on Earth (and hence in the Universe). To produce books saying that science proves there is no purpose in the universe is pure myopia. It just means that one has shut ones eyes to all the data that relates to purpose and meaning; and that one supposes that the only science is physics (for psychology and biology are full of purpose).

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=cosmology). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/cosmology/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=cosmology&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](http://philpapers.org/sep/cosmology/) at [PhilPapers](http://philpapers.org/), with links to its database. |

## Other Internet Resources

- Hossenfelder, Sabine, 2013, [“What do most physicists work on?”](http://backreaction.blogspot.co.za/2013/05/what-do-most-physicists-work-on.html), blog post in BackRe(Action), 8 May 2013.
- [BKL singularity](https://en.wikipedia.org/w/index.php?title=BKL_singularity&oldid=799333893), Wikipedia

## Related Entries

confirmation | fine-tuning | laws of nature | space and time: singularities and black holes | time: thermodynamic asymmetry in | underdetermination, of scientific theories

### Acknowledgments

Work on this entry was supported by a grant from the John Templeton Foundation. The statements made here are those of the authors and are not necessarily endorsed by the Foundation.

## Notes（原文脚注）

[^note-1]: See Smeenk 2012 and O’Raifeartaigh et al. forthcoming for further discussion of Einstein’s contributions.

[^note-2]: There are several excellent textbook treatments of cosmology, including in particular Dodelson 2003, Mukhanov 2005, Durrer 2008, and Peter & Uzan 2013.

[^note-3]: A geodesic is an analog of a straight line in two senses: the geodesic between two points extremizes the length, and the tangent vector to the curve remains parallel to itself as it is parallel transported along the curve.

[^note-4]: Represented compactly using the metric field, $g_{ab}$. The equations are non-linear both in terms of involving products of derivatives $g_{ab,c}$ of $g_{ab}$ with other derivative and also with its inverse $g^{ab}.$

[^note-5]: These solutions are *homogeneous* and *isotropic*: homogeneity requires that at a given moment of cosmic time every spatial point “looks the same,” and isotropy holds if there are no geometrically preferred spatial directions. Thus the spatial geometry of $\Sigma$ is such that there is an isometry carrying any point $p \in \Sigma$ to any other point lying in the same surface (homogeneity), and at any point $p$ the three spatial directions are equivalent to each other (isotropy). An isometry is a transformation that preserves the spacetime geometry; more precisely, a diffeomorphism $\phi$ that leaves the spacetime metric invariant, i.e., $(\phi^*g)_{ab} = g_{ab}$. It is an isotropy about a point $p$ if it leaves $p$ fixed: $(\phi^*p) =p$.

[^note-6]: These are the three possibilities if $\Sigma$ is assumed to be *simply connected*, which holds if every closed loop can be smoothly contracted to a point. There are many possibilities for a globally isotropic space with constant curvature that is multiply connected (Ellis 1971b)[^ellis-1971b], for example a toroidal topology (a closed version of flat space) or projective space (with the same metric as spherical space but a different topology).

[^note-7]: $\dot{R}$ is the derivative of $R$ with respect to cosmic time $t$, $\Lambda$ is the cosmological constant, and $G$ is Newton’s gravitational constant. The Raychaudhuri equation is a fundamental equation that describes the evolution of a cluster of nearby worldlines, e.g., for the particles making up a small ball of dust, in response to spacetime curvature (Ellis 1971a)[^ellis-1971a]. It takes on the simple form given here due to the symmetries we have assumed: in the FLRW models the small ball of dust can change only its volume as a function of time, but in general there can be a volume-preserving distortion (shear) and rotation of the ball as well.

[^note-8]: The stress energy tensor for a perfect fluid is given by $T_{ab} = (\rho + p) u_a u_b + (p) g_{ab}$, where $u_a$ is the unit tangent vector to the trajectories of the fluid elements ($u^a u_a = -1$).

[^note-9]: These models typically treat the evolution of perturbations using Newtonian gravity, over a fixed background cosmological model; the assumptions include specification of the initial spectrum of density perturbations and cosmological parameters. There are enormous computational challenges to giving a fully relativistic account of structure formation of comparable dynamical range, and it is furthermore unclear to what extent a relativistic account diverges from Newtonian N-body simulations.

[^note-10]: See Ellis et al. 2012: §11.1, 13.1 for further discussion and references.

[^note-11]: See Wainwright & Ellis 1997 for discussion.

[^note-12]: See Clarkson & Maartens 2010, February et al. 2010, and Zhang & Stebbins 2011.

[^note-13]: There could in principle be a curvature dominated phase before this happens, but in practice this seems to not be the case. See Ehlers & Rindler 1989 for an illuminating phase space representation of FLRW solutions with pressure and a cosmological constant that shows all the possibilities.

[^note-14]: See Beringer et al. 2012 and Ade et al. 2016 for example, for reviews of evidence bearing on the cosmological parameters. The total number of parameters used to specify a cosmological model varies in different studies, but typically 5–10 fundamental parameters are used to determine the best fit to a given data set.

[^note-15]: See, e.g., Particle Data Group 2016 for a recent review of observational constraints on the cosmological models.

[^note-16]: See Norton (1993, 1994) for a discussion of this contrast between scientific and philosophical attitudes toward underdetermination.

[^note-17]: See, for example, Laudan & Leplin 1991 for a sharp criticism of the treatment of empirical content by Quine, van Fraassen, and others, along these lines.

[^note-18]: The light cone is the boundary of the causal past; EFE can be used to determine the spacetime geometry in the causal past from this data set. On this approach the ideal data set includes various astrophysical assumptions about the nature of sources, and their historical evolution, used to measure spacetime geometry, without assumptions regarding background geometry. There is an important limitation: there is no way to register the impact of dark matter or dark energy directly on the ideal observational set without substantive modeling assumptions.

[^note-19]: The Gauss-Codacci constraint equations do impose some restrictions on spacelike separated regions, although these would not make it possible to determine the state of one region from the other (see Ellis & Sciama 1972)[^ellis-1972]. Events to the future of $J^-(p)$ will in general be influenced by regions of spacetime that did not register on $J^-(p)$, and extrapolations to the future are only valid if a no-interference condition holds.

[^note-20]: For example, there are models which are locally (rather than globally) isotropic and homogeneous, such that the surfaces $\Sigma$ have finite volume but are multiply connected, consisting of, roughly speaking, cells pasted together. Ellis 1971b explores this kind of model; see Lachieze-Rey & Luminet 1995 for a more recent review. Although isotropy and homogeneity hold locally at each point, above some length scale there would be geometrically preferred directions reflecting how the cells are connected.

[^note-21]: A *local* spacetime property is a property such that for any pair of locally isometric spacetimes, they either both have the property or neither does. The property of being a solution to EFE is a local property in this sense. Global properties, by contrast, can vary between locally isometric spacetimes. There are a hierarchy of conditions that characterize the global causal structure of spacetimes. See Manchak 2013 for further discussion and references.

[^note-22]: Roughly, the counterpart can be constructed by stringing together a collection of “copies” of the causal pasts, like laundry hanging on a clothesline. The properties of this counterpart spacetime are not constrained in regions outside the copies of the causal pasts. (For example, a closed timelike curve could exist in a region outside the copies of the causal pasts, violating global hyperbolicity.) See Malament 1977 and Manchak 2009 for further discussion. Malament (1977) reviews several different definitions of observational indistinguishability; Manchak (2009) establishes the generality of Malament’s “clothesline construction.”

[^note-23]: See, for example, Baker et al. (2015) regarding the regimes of gravitational theory probed by solar system tests, observations of gravitational waves, and etc. Obviously, the physics horizon is based in part on an assessment of what is technologically and economically feasible, and will shift over time as new avenues of testing open up.

[^note-24]: The CMB indicates that baryonic matter was very smooth at the time of decoupling because it was strongly coupled to radiation. Dark matter decouples from radiation earlier than baryonic matter, and can be much lumpier at the time the CMB is emitted; these lumps then generate perturbations in baryonic matter.

[^note-25]: At the time of writing, there are no generally accepted candidates for successful detection of dark matter particles; instead, ongoing experimental searches have ruled out parts of the parameter space of candidate particles.

[^note-26]: See Frieman et al. 2008 for a summary.

[^note-27]: Synge’s G-method (Synge 1961)[^synge-1961] states that you can always run the EFE backwards from any given geometry $g_{ab}$ to determine what energy-momentum stress tensor $T_{ab}$ would solve the EFE exactly for that geometry. This does not provide a physical basis for the thus determined nature of such ‘matter’, which will for example generically violate the energy conditions.

[^note-28]: See Ellis and Madsen (1991) for the general procedure, and Lidsey et al. 1997 for its use as regarding reconstructing the inflaton potential; this is essentially a version of Synge’s G-method.

[^note-29]: In the case of say geology, even though each one is different, there are many mountains, rivers, and continents to observe and compare.

[^note-30]: The first singularity theorem showed that these divergences follow from the Raychaudhuri equation (Ellis 1971a)[^ellis-1971a]. One might have hoped that pressure would counteract these divergences, but this is not the case since it enters into the equation with the same sign as the energy density. Equation (2) is a special case of the general Raychaudhuri equation, in which shear, vorticity, and acceleration vanish due to the symmetries of the FLRW models.)

[^note-31]: Refocusing leads to the “onion” shape of the past light cone: it reaches a maximum radius at some finite time, and decreases at earlier times (Ellis 1971a)[^ellis-1971a]. See Ellis & Rothman 1993 for further discussion.

[^note-32]: Cf. Earman (1995)’s defense, following Charles Misner, of “tolerance for spacetime singularities,” based on a critical assessment of the various reasons given in the physics literature for regarding singularities as a shortcoming of GR. See Curiel and Bokulich (2009 [2012]) for further discussion and references.

[^note-33]: Bergmann argues that

> a theory that involves singularities and involves them unavoidably, moreover, carries within itself the seeds of its own destruction; (1980: 186)

similarly, textbook discussions of the singularity theorems (such as Wald 1984: Chapter 9)[^wald-1984] emphasize that the singularity theorems show that the GR’s classical description of gravity breaks down in some regimes. See Curiel and Bokulich (2009 [2012]) for further discussion.

[^note-34]: Penrose has emphasized this point; see Chapter 3 of Penrose 2016 for a recent discussion. Wikipedia has a thorough discussion of the BKL singularity (see Other Internet Resources).

[^note-35]: These features are usually taken to be puzzling because they apparently require “fine-tuning,” discussed further in §4.2.

[^note-36]: A particle horizon at time $t_0$ is the timelike 3-surface in space-time separating world lines of particles moving along fundamental geodesics that could have interacted with a worldline $\gamma$ at the time $t_0$ (their world lines would have intersected the past light cone of that event) from those which could not. On the time slice $t_0$, this defines a 2-sphere comprising the most distant matter that could have interacted with $\gamma$ at that time. For a radiation-dominated FLRW model, the expression for horizon distance $d_h$ is finite; the horizon distance at decoupling corresponds to an angular separation of $\approx 1^{\circ}$ on the surface of last scattering.

[^note-37]: It follows from the FLRW dynamics that $\frac{|\Omega - 1|}{\Omega} \propto R^{3\gamma - 2}(t)$. $\gamma > 2/3$ if the strong energy condition holds, and in that case an initial value of $\Omega$ not equal to 1 is driven rapidly away from 1. Observational constraints on $\Omega (t_0)$ can be extrapolated back to a constraint on the total energy density of the Planck time, namely $|\Omega(t_p) - 1| \leq 10^{-59}$.

[^note-38]: The Hubble radius $d(H_0)$ is defined in terms of the instantaneous expansion rate $\dot{R}(t)$, by contrast with the particle horizon distance $d_h$, which depends upon the expansion history since the start of the universe. For radiation or matter-dominated solutions, the two quantities have the same order of magnitude.

[^note-39]: Brout et al. 1978, Vilenkin 1983, and Hartle & Hawking 1983 are early papers pursuing a quantum account of the creation from different theoretical perspectives; see also Butterfield & Isham 2000.

[^note-40]: Here we are in agreement with Albert 2012, which initiated a polemical exchange with Lawrence Krauss (whose book was the subject of Albert’s review).

[^note-41]: Carter (1974) introduced a terminology that has been widely used: the “weak anthropic principle” refers to a selection effect, as illustrated in the case of Dicke’s response to Dirac, whereas the “strong anthropic principle” holds that the universe *must* (in some sense) allow for the existence of life. These two claims strike us as too different to be weak and strong versions of a single underlying principle. Rather than adopting these terms, below we will draw a related distinction between selection effects and the use of typicality assumptions to make anthropic predictions.

[^note-42]: See Titelbaum (2013) for a recent proposal and references to related work.

[^note-43]: Although we will not pursue the topic here, Weinberg’s argument is a special case that avoids some of the questions that arise in giving a general account of “anthropic prediction.” For example, the argument concerns variation of a single parameter, whereas the general case requires considering the variation of several parameters. See Aguirre (2007) for an account of the challenges and complications involved in carrying out anthropic predictions for a variety of parameters, and Starkman & Trotta 2006 for further problems with these methods.

[^note-44]: This is closely related to Vilenkin (1995)’s “Principle of Mediocrity,” and Bostrom (2002)’s “Self-Sampling Assumption” (although he eventually argues for a principle applied to “observer-moments” rather than observers); see also Dorr and Arntzenius (2017).

[^note-45]: As Aguirre et al. 2007 notes, it is possible to choose some other object to conditionalize on in a Weinberg-style argument; but this leads to similar problems regarding the choice of reference class and appeal to indifference.

[^note-46]: More precisely, the assignment of probabilities depends on algebraic structure—the event algebra—defined on the sample space. Many different event algebras can be assigned over the same sample space.

[^note-47]: See Norton (2010), who is also critical of Bostrom’s approach, but advocates a non-Bayesian approach to inductive reasoning.

[^note-48]: There are different ways of enumerating the fundamental constants in both cases, but the arguments below do not depend upon choosing a specific list.

[^note-49]: Barrow & Tipler 1986 is an influential early discussion of fine-tuning; for more recent discussions, see Barnes 2012 and Lewis & Barnes 2016.

[^note-50]: See McGrew et al. 2001 and Colyvan et al. 2005 for challenges to justifying probabilities in this case, and Manson 2009 for a response and general discussion of fine-tuning.

[^note-51]: A somewhat similar view is taken to follow from the existence of many distinct vacua in string theory (the “landscape”). Both views are distinct from the Everettian multiverse, although there have been speculative attempts to link these distinct multiverses.

[^note-52]: See Ade et al. 2016 and Martin et al. 2014 regarding the most recent constraints from the CMB.

[^note-53]: See Freivogel et al. 2006 for multiverses based in Coleman de Luccia tunnelling, and Aguirre 2007 for a an overview of EI.

[^note-54]: A third one is that it is claimed by some that a multiverse definitively requires universes with spatial sections of negative curvature (Freivogel et al. 2006)[^freivogel-2006], so if if this is not observed the hypothesis is disproved. However that claim is disputed (Buniy et al. 2008)[^buniy-2008].

[^note-55]: See, for example, Vilenkin 2007.

[^note-56]: There are active debates in the philosophy of physics regarding the status of infinite idealizations in other areas of physics; see, e.g., Batterman 2005 and Menon & Callender 2013.

[^note-57]: Despite the prevalence of multiverse debates in popular science, there is in fact only a small minority of cosmologists actively working on this topic: see Hossenfelder’s comments in a blog post (2013, in Other Internet Resources), and the lack of mention of the topic in the standard textbooks referred to above and the data analysis by the Planck team (Ade et al. 2016)[^ade-2016].

[^note-58]: It is also assumed that the consequence does not itself entail the hypothesis.

[^note-59]: For further discussion along these lines, see Norton 2000, Harper 2012, Smith 2014, and Stein 1994; Smeenk (2017) considers the implications of this line of thought for inflation.

[^note-60]: Although most of the anthropic literature is concerned only with *necessary* conditions for life, rather than *sufficient*. In other words, they do not in fact deal with biology, only with conditions for stars, planes, and elements like Carbon and Oxygen to exist. To make the link to life proper one needs to extend this discussion to the possibility spaces for life to function, as discussed for example by Andreas Wagner in his illuminating book *Arrival of the Fittest* (2014) describing various spaces of genotype to phenotype maps.

[^ade-2016]: Ade, P.A.R., N. Aghanim, M. Arnaud, F. Arroja, M. Ashdown, J. Aumont, C. Baccigalupi, M. Ballardini, A. Banday, R. Barreiro, et al., 2016, “*Planck* 2015 results—XX. Constraints on Inflation”, *Astronomy & Astrophysics*, 594: A20. doi:10.1051/0004-6361/201525898

[^aguirre-2007]: Aguirre, Anthony, 2007, “Eternal Inflation, Past and Future”, 4 December 2007, arXiv:0712.0571.

[^aguirre-2007-2]: Aguirre, Anthony, Steven Gratton, and Matthew C. Johnson, 2007, “Hurdles for Recent Measures in Eternal Inflation”, *Physical Review D*, 75(12): 123501. doi:10.1103/PhysRevD.75.123501

[^aguirre-2011]: Aguirre, Anthony and Matthew C. Johnson, 2011, “A Status Report on the Observability of Cosmic Bubble Collisions”, *Reports on Progress in Physics*, 74(7): 074901. doi:10.1088/0034-4885/74/7/074901

[^albert-2012]: Albert, David, 2012, “On the Origin of Everything: ‘A Universe From Nothing’, by Lawrence M. Krauss”, *The New York Times*, March 25, 2012: BR20.

[^ashtekar-2011]: Ashtekar, Abhay and Singh, Parampreet, 2011, “Loop quantum cosmology: a status report”, *Classical and Quantum Gravity*, 28(21): 213001.

[^baker-2015]: Baker, Tessa and Psaltis, Dimitrios, and Skordis, Constantinos, 2015, “Linking tests of gravity on all scales: from the strong-field regime to cosmology”, *Astrophysical Journal*, 802 (1): 63.

[^barbour-1995]: Barbour, Julian B. and Herbert Pfister, 1995, *Mach’s Principle: From Newton’s Bucket to Quantum Gravity*, (Einstein Studies, vol. 6), Boston: Springer Science & Business Media.

[^barnes-2012]: Barnes, L.A., 2012, “The Fine-Tuning of the Universe for Intelligent Life”, *Publications of the Astronomical Society of Australia*, 29(4):529–564.

[^barrow-1986]: Barrow, John D. and Frank J. Tipler, 1986, *The Anthropic Cosmological Principle*, Oxford: Oxford University Press.

[^batterman-2005]: Batterman, Robert W., 2005, “Critical Phenomena and Breaking Drops: Infinite Idealizations in Physics”, *Studies In History and Philosophy of Science Part B: Studies in History and Philosophy of Modern Physics*, 36(2): 225–244. doi:10.1016/j.shpsb.2004.05.004

[^batterman-2013]: ––– (ed.), 2013, *Oxford Handbook of Philosophy of Physics*, Oxford: Oxford University Press. doi:10.1093/oxfordhb/9780195392043.001.0001

[^beisbart-2009]: Beisbart, Claus, 2009, “Can We Justifiably Assume the Cosmological Principle in Order to Break Model Underdetermination in Cosmology?”, *Journal for General Philosophy of Science*, 40(2): 175–205. doi:10.1007/s10838-009-9098-9

[^bergmann-1980]: Bergmann, Peter G., 1980, “Open Discussion, Following Papers by S.W. Hawking and W.G. Unruh,” in Harry Woolf (ed.), *Some Strangeness in the Proportion: A Centennial Symposium to Celebrate the Achievements of Albert Einstein*, Reading, MA. Addison-Wesley.

[^beringer-2012]: Beringer, J., J.-F. Arguin, R. Barnett, K. Copic, O. Dahl, D. Groom, C. Lin, J. Lys, H. Murayama, C. Wohl, et al., 2012, “Review of Particle Physics”, *Physical Review D*, 86(1): 010001. doi:10.1103/PhysRevD.86.010001

[^bernal-2016]: Bernal, José Luis, Licia Verde, and Adam G. Riess, 2016, “The Trouble with $H_0$”, *Journal of Cosmology and Astroparticle Physics*, 2016(10): 019. doi:10.1088/1475-7516/2016/10/019

[^bertone-2005]: Bertone, Gianfranco, Dan Hooper, and Joseph Silk, 2005, “Particle Dark Matter: Evidence, Candidates and Constraints”. *Physics Reports*, 405(5–6): 279–390. doi:/10.1016/j.physrep.2004.08.031

[^bezrukov-2012]: Bezrukov, F.L. and D.S. Gorbunov, 2012, “Distinguishing Between $R^2$-Inflation and Higgs-Inflation”, *Physics Letters B*, 713(4): 365–368. doi:10.1016/j.physletb.2012.06.040

[^bojowald-2011]: Bojowald, Martin, 2011, *Quantum cosmology: a fundamental description of the universe*, Berlin: Springer Science.

[^bondi-1960]: Bondi, Hermann, 1960, *Cosmology*, Cambridge: Cambridge University Press.

[^bostrom-2002]: Bostrom, Nick, 2002, *Anthropic Bias: Observation Selection Effects in Science and Philosophy*, Routledge, New York.

[^brout-1978]: Brout, R., F. Englert, and E. Gunzig, 1978, “The Creation of the Universe as a Quantum Phenomenon”, *Annals of Physics*, 115: 78–106. doi:10.1016/0003-4916(78)90176-8

[^buniy-2008]: Buniy, Roman V., Stephen D.H. Hsu, and A. Zee, 2008, “Does String Theory Predict An Open Universe?”, *Physics Letters B*, 660(4): 382–385. doi:10.1016/j.physletb.2008.01.007

[^butterfield-2014]: Butterfield, Jeremy, 2014, “On Under-Determination in Cosmology”, *Studies In History and Philosophy of Science Part B: Studies In History and Philosophy of Modern Physics*, 46(part A): 57–69. doi:10.1016/j.shpsb.2013.06.003

[^butterfield-2000]: Butterfield, Jeremy and Chris Isham, 2000, “On the Emergence of Time in Quantum Gravity”, In Jeremy Butterfield (ed.), *The Arguments of Time*, Oxford: Oxford University Press, pages 111–168. doi:10.5871/bacad/9780197263464.003.0006

[^carter-1974]: Carter, Brandon, 1974, “Large number coincidences and the anthropic principle in cosmology,” in *Confrontation of cosmological theories with observational data: Proceedings of the symposium, Krakow, Poland, Sept. 10-12, 1973*, Dordrecht: D. Reidel Publishing Co., pp. 291-298.

[^chamcham-2017]: Chamcham, Khalil, Joseph Silk, John D. Barrow, and Simon Saunders (eds), 2017 *The Philosophy of Cosmology*, Cambridge: Cambridge University Press. doi:10.1017/9781316535783

[^clarkson-2008]: Clarkson, Chris, Bruce Bassett, and Teresa Hui-Ching Lu, 2008, “A General Test of the Copernican Principle”, *Physical Review Letters*, 101: 011301. doi:10.1103/PhysRevLett.101.011301

[^clarkson-2010]: Clarkson, Chris and Roy Maartens, 2010, “Inhomogeneity and the Foundations of Concordance Cosmology”, *Classical and Quantum Gravity*, 27(12): 001–023. doi:10.1088/0264-9381/27/12/124008

[^collins-1973]: Collins, Chris and Hawking, Stephen, 1973, “Why is the Universe Isotropic?,” *Astrophysical Journal*, 180: 317–334.

[^colyvan-2005]: Colyvan, Mark, Jay L. Garfield, and Graham Priest, 2005, “Problems with the Argument from Fine Tuning”, *Synthese*, 145(3): 325–338. doi:10.1007/s11229-005-6195-0

[^crupi-2013]: Crupi, Vincenzo, 2013 [2016], “Confirmation”, *The Stanford Encyclopedia of Philosophy* (Winter 2016 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/win2016/entries/confirmation/](https://plato.stanford.edu/archives/win2016/entries/confirmation/)>

[^curiel-2009]: Curiel, Erik and Peter Bokulich, 2009 [2012], “Singularities and Black Holes”, *The Stanford Encyclopedia of Philosophy* (Fall 2012 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/fall2012/entries/spacetime-singularities/](https://plato.stanford.edu/archives/fall2012/entries/spacetime-singularities/)>

[^dicke-1961]: Dicke, R.H., 1961, “Dirac’s Cosmology and Mach's Principle”, *Nature*, 192: 440–441.

[^dicke-1979]: Dicke, R.H. and P.J.E. Peebles, 1979, “The Big Bang Cosmology—Enigmas and Nostrums”, in Hawking & Israel 1979: 504–517.

[^dirac-1937]: Dirac, P. A. M., 1937, “The Cosmological Constants”, *Nature*, 139: 323.

[^dodelson-2003]: Dodelson, Scott, 2003, *Modern Cosmology*, London: Academic Press.

[^dorr-2017]: Dorr, Cian, and Arntzenius, Frank, 2017, “Self-locating priors and cosmological measures”, in *Philosophy of Cosmology*, Chamcham et al. (eds.), Oxford: Oxford University Press.

[^duhem-1914]: Duhem, Pierre Maurice Marie, 1914 [1954], *The Aim and Structure of Physical Theory* (*La théorie physique: son objet et sa structure*, second edition), Philip P. Wiener (trans.), Princeton: Princeton University Press.

[^durrer-2008]: Durrer, Ruth, 2008, *The Cosmic Microwave Background*, Cambridge: Cambridge University Press.

[^earman-1995]: Earman, John, 1995, *Bangs, Crunches, Whimpers, and Shrieks: Singularities and Acausalities in Relativistic Spacetimes*, Oxford: Oxford University Press.

[^ehlers-1968]: Ehlers, J., P. Geren, and R.K. Sachs, 1968, “Isotropic Solutions of the Einstein-Liouville Equations”, *Journal of Mathematical Physics*, 9(9): 1344–1349. doi:10.1063/1.1664720

[^ehlers-1989]: Ehlers, J. and W. Rindler, 1989, “A Phase-Space Representation of Friedmann-Lemaître Universes Containing Both Dust and Radiation and the Inevitability of a Big Bang”, *Monthly Notices of the Royal Astronomical Society*, 238(2): 503–521. doi:10.1093/mnras/238.2.503

[^einstein-1917]: Einstein, Albert, 1917, “Kosmologische Betrachtungen Zur Allgemeinen Relativitätstheorie”, *Preussische Akademie der Wissenschaften (Berlin). Sitzungsberichte*, pages 142–152.

[^ellis-1971a]: Ellis, George F.R., 1971a, “Relativistic Cosmology”, in R.K. Sachs (ed.), *General Relativity and Cosmology*, (Proceedings of the International School of Physics “Enrico Fermi”, Course XLVII), New York: Academic Press, pages 104–182.

[^ellis-1971b]: –––, 1971b, “Topology and Cosmology”, *General Relativity and Gravitation*, 2(1): 7–21. doi:10.1007/BF02450512

[^ellis-2002]: –––, 2002, “Cosmology and Local Physics”, *New Astronomy Reviews*, 46(11): 645–657. doi:10.1016/S1387-6473(02)00234-8

[^ellis-2007]: –––, 2007, “Issues in the Philosophy of Cosmology”, in Jeremy Butterfield & John Earman (eds), *Philosophy of Physics*, Part B, (Handbook of the Philosophy of Science), Elsevier, pages 1183–1286. doi:10.1016/B978-044451560-5/50014-2

[^ellis-2017]: –––, 2017, “The Domain of Cosmology and the Testing of Cosmological Theories”, in Chamcham et al. 2017: 1–23. doi:10.1017/9781316535783.002

[^ellis-1984]: Ellis, G.F.R. and J.E. Baldwin, 1984, “On the Expected Anisotropy of Radio Source Counts”, *Monthly Notices of the Royal Astronomical Society*, 206(2): 377–381. doi:10.1093/mnras/206.2.377

[^ellis-1974]: Ellis, G.F.R. and A.R. King, 1974, “Was the Big Bang a Whimper?”, *Communications in Mathematical Physics*, 38(2): 119–156. doi:10.1007/BF01651508

[^ellis-1991]: Ellis, G.F.R. and M. Madsen, 1991, “Exact Scalar Field Cosmologies,” *Classical and Quantum Gravity*, 8: 667–676.

[^ellis-1993]: Ellis, G.F.R. and T. Rothman, 1993, “Lost Horizons”, *American Journal of Physics*, 61(10): 883–893. doi:10.1119/1.17400

[^ellis-1986]: Ellis, G.F.R. and G. Schrieber, 1986, “Observational and dynamic properties of small universes,” *Physics Letters*, A115: 97–107.

[^ellis-1972]: Ellis, G.F.R. and D.W. Sciama, 1972, “Global and Non-Global Problems in Cosmology”, in L. O’Raifeartaigh (ed.), *General Relativity: Papers in Honour of J.L. Synge*, Oxford: Clarendon Press, pages 35–59.

[^ellis-2009]: Ellis, G.F.R. and W.R. Stoeger, 2009, “The Evolution of Our Local Cosmic Domain: Effective Causal Limits”, *Monthly Notices of the Royal Astronomical Society*, 398(3): 1527–1536. doi:10.1111/j.1365-2966.2009.15209.x

[^ellis-2014]: Ellis, George and Jean-Philippe Uzan, 2014, “Inflation and the Higgs Particle”, *Astronomy & Geophysics*, 55(1): 1–19. doi:10.1093/astrogeo/atu035

[^ellis-2012]: Ellis, George F.R., Roy Maartens, and Malcolm A.H. MacCallum, 2012, *Relativistic Cosmology*, Cambridge: Cambridge University Press. doi:10.1017/CBO9781139014403

[^ellis-1985]: Ellis, G.F.R., S.D. Nel, R. Maartens, W.R. Stoeger, and A.P. Whitman, 1985, “Ideal Observational Cosmology”, *Physics Reports*, 124(5–6): 315–417. doi:10.1016/0370-1573(85)90030-4

[^february-2010]: February, Sean, Julien Larena, Mathew Smith, and Chris Clarkson, 2010, “Rendering Dark Energy Void”, *Monthly Notices of the Royal Astronomical Society*, 405(4): 2231–2242. doi:10.1111/j.1365-2966.2010.16627.x

[^freivogel-2006]: Freivogel, Ben, Matthew Kleban, Maria Rodriguez Martinez, and Leonard Susskind, 2006, “Observational Consequences of a Landscape”, *Journal of High Energy Physics*, 2006(03): 039. doi:10.1088/1126-6708/2006/03/039

[^frieman-2008]: Frieman, Joshua, Michael Turner, and Dragan Huterer, 2008, “Dark Energy and the Accelerating Universe”, *Annual Review of Astronomy and Astrophysics*, 46: 385–432, doi:10.1146/annurev.astro.46.060407.145243

[^gott-1993]: Gott, J. Richard, 1993, “Implications of the Copernican Principle for Our Future Prospects”, *Nature*, 363(6427): 315–319. doi:10.1038/363315a0

[^guth-2007]: Guth, Alan H., 2007, “Eternal Inflation and Its Implications”, *Journal of Physics A: Mathematical and Theoretical*, 40(25): 6811–6826. doi:10.1088/1751-8113/40/25/S25

[^harper-2012]: Harper, William L., 2012, *Isaac Newton’s Scientific Method: Turning Data Into Evidence about Gravity and Cosmology*, Oxford: Oxford University Press.

[^harrison-1984]: Harrison, E.R., 1984, “The Dark Night-Sky Riddle: a ‘Paradox’ that Resisted Solution”, *Science*, 226(4677): 941–946. doi:10.1126/science.226.4677.941

[^hartle-1983]: Hartle, J.B. and S.W. Hawking, 1983, “Wave Function of the Universe”, *Physical Review D*, 28(12): 2960–2975. doi:10.1103/PhysRevD.28.2960

[^hawking-1973]: Hawking, S.W. and G.F.R. Ellis, 1973, *The Large Scale Structure of Space-Time*, Cambridge: Cambridge University Press. doi:10.1017/CBO9780511524646

[^hawking-1979]: Hawking, S.W. and W. Israel (eds), 1979, *General Relativity: An Einstein Centenary Survey*, Cambridge: Cambridge University Press.

[^hilbert-1925]: Hilbert, David, 1925 [1983], “On the Infinite”, in *Philosophy of Mathematics: Selected Readings*, second edition, Paul Benacerraf and Hilary Putnam (eds), Cambridge: Cambridge University Press, pages 183–201. Delivered June 4, 1925, before a congress of the Westphalian Mathematical Society in Munster. Translated by Erna Putnam and Gerald J. Massey from *Mathematische Annalen* (Berlin), 95(1926): 161–190. doi:10.1017/CBO9781139171519.010

[^kamionkowski-1997]: Kamionkowski, Marc and Abraham Loeb, 1997, “Getting Around Cosmic Variance”, *Physical Review D*, 56(8): 4511–4513. doi:10.1103/PhysRevD.56.4511

[^knight-2017]: Knight, Robert and Lloyd Knox, 2017, “The Low Level of Correlation Observed in the CMB Sky at Large Angular Scales and the Low Quadrupole Variance”, 2 May 2017, arXiv:1705.01178

[^kristian-1966]: Kristian, J. and R. K. Sachs, 1966, “Observations in Cosmology,” *Astrophysical Journal* 143: 379-399.

[^lachièze-rey-1995]: Lachièze-Rey, Marc and Jean-Pierre Luminet, 1995, “Cosmic Topology”, *Physics Reports*, 254(3): 135–214. doi:10.1016/0370-1573(94)00085-H

[^laudan-1991]: Laudan, Larry and Jarrett Leplin, 1991, “Empirical Equivalence and Underdetermination”, *Journal of Philosophy*, 88(9): 449–472. doi:10.2307/2026601

[^lemaître-1927]: Lemaître, G., 1927, “Un Univers Homogène de Masse Constante et de Rayon Croissant Rendant Compte de la Vitesse Radiale des Nébuleuses Extra-Galactiques”, in *Annales de la Société scientifique de Bruxelles*, A47: 49–59.

[^leslie-1992]: Leslie, John, 1992, “Doomsday Revisited”, *The Philosophical Quarterly*, 42(166): 85–89. doi:10.2307/2220451

[^lewis-2016]: Lewis, Geraint F. and Luke A. Barnes, 2016, *A Fortunate Universe: Life in a Finely Tuned Cosmos*, Cambridge: Cambridge University Press. doi:10.1017/CBO9781316661413

[^lidsey-1997]: Lidsey, James E., Andrew R. Liddle, Edward W. Kolb, Edmund J. Copeland, Tiago Barreiro, and Mark Abney, 1997, “Reconstructing the Inflaton Potential—An Overview”, *Reviews of Modern Physics*, 69(2): 373–410. doi:10.1103/RevModPhys.69.373

[^loewer-1996]: Loewer, Barry, 1996, “Humean Supervenience”, *Philosophical Topics*, 24(1): 101–127. doi:10.5840/philtopics199624112

[^luković-2016]: Luković, Vladimir V., Rocco D’Agostino, and Nicola Vittorio, 2016, “Is There a Concordance Value For $H_0$?” *Astronomy & Astrophysics*, 595: A109. doi:10.1051/0004-6361/201628217

[^lyth-1999]: Lyth, David H. and Antonio Riotto, 1999, “Particle Physics Models of Inflation and the Cosmological Density Perturbation”, *Physics Reports*, 314(1–2): 1–146. doi:10.1016/S0370-1573(98)00128-8

[^malament-1977]: Malament, David, 1977, “Observationally Indistinguishable Space-Times”, in John Earman, Clark Glymour, and John Statchel (eds), *Foundations of Space-Time Theories*, (*Minnesota Studies in the Philosophy of Science*, 8), University of Minnesota Press, pages 61–80.

[^manchak-2009]: Manchak, John Byron, 2009, “Can We Know the Global Structure of Spacetime?”, *Studies in History and Philosophy of Science Part B: Studies in History and Philosophy of Modern Physics*, 40(1): 53–56. doi:10.1016/j.shpsb.2008.07.004

[^manchak-2013]: –––, 2013, “Global Spacetime Structure”, in Batterman 2013: 587–606.

[^manson-2009]: Manson, Neil A., 2009, “The Fine-Tuning Argument”, *Philosophy Compass*, 4(1): 271–286. doi:10.1111/j.1747-9991.2008.00188.x

[^marra-2013]: Marra, Valerio, Lucca Amendola, Ignacy Sawicki, and Wessel Valkenburg, 2013, “Cosmic Variance and the Measurement of the Local Hubble Parameter”, *Physical Review Letters*, 110(24): 241305. doi:10.1103/PhysRevLett.110.241305

[^martin-2014]: Martin, Jérôme, Christophe Ringeval, and Vincent Vennin, 2014, “Encyclopaedia Inflationaris”, *Physics of the Dark Universe*, 5–6: 75–235. doi:10.1016/j.dark.2014.01.003

[^mcgrew-2001]: McGrew, Timothy, Lydia McGrew, and Eric Vestrup, 2001, “Probabilities and the Fine-Tuning Argument: A Sceptical View”, *Mind*, 110(440): 1027–1038. doi:10.1093/mind/110.440.1027

[^menon-2013]: Menon, Tarun and Craig Callender, 2013, “Turn and Face the Strange … Ch-Ch-Changes: Philosophical Questions Raised by Phase Transitions”, in Batterman 2013: 189–223.

[^misner-1968]: Misner, Charles W., 1968, “The Isotropy of the Universe”, *Astrophysical Journal*, 151: 431–457. doi:10.1086/149448

[^mukhanov-2005]: Mukhanov, Viatcheslav, 2005, *Physical Foundations of Cosmology*, Cambridge: Cambridge University Press.

[^mukhanov-1992]: Mukhanov, V.F., H.A.,Feldman, and R.H. Brandenberger, 1992, “Theory of Cosmological Perturbations”, Part 1. classical perturbations. Part 2. quantum theory of perturbations. Part 3. extensions. *Physics Reports*, 215(5–6): 203–333. doi:10.1016/0370-1573(92)90044-Z

[^munitz-1962]: Munitz, Milton K., 1962, “The Logic of Cosmology”, *British Journal for the Philosophy of Science*, 13(49): 34–50. doi:10.1093/bjps/XIII.49.34

[^mustapha-1997]: Mustapha, Nazeem, Charles Hellaby, and G.F.R. Ellis, 1997, “Large-Scale Inhomogeneity Versus Source Evolution: Can We Distinguish Them Observationally?”, *Monthly Notices of the Royal Astronomical Society*, 292(4): 817–830. doi:10.1093/mnras/292.4.817

[^neal-2006]: Neal, Radford M., 2006, “Puzzles of Anthropic Reasoning Resolved Using Full Non-Indexical Conditioning”, 23 August 2006. arXiv:math/0608592

[^norton-1993]: Norton, John D., 1993, “The Determination of Theory by Evidence: the Case for Quantum Discontinuity, 1900–1915”, *Synthese*, 97(1): 1–31. doi:10.1007/BF01255831

[^norton-1994]: –––, 1994, “Why Geometry is Not Conventional: The Verdict of Covariance Principles”, in Ulrich Majer and H.J. Schmidt (eds), *Semantical Aspects of Spacetime Theories*, Mannheim: BI Wissenschaftsverlag, pages 159–168.

[^norton-2000]: –––, 2000, “‘Nature is the Realisation of the Simplest Conceivable Mathematical Ideas’: Einstein and the Canon of Mathematical Simplicity”, *Studies in the History and Philosophy of Science Part B: Studies in History and Philosophy of Modern Physics*, 31(2): 135–170. doi:10.1016/S1355-2198(99)00035-0

[^norton-2010]: –––, 2010, “Cosmic Confusions: Not Supporting Versus Supporting Not”, *Philosophy of Science*, 77(4): 501–523. doi:10.1086/661504

[^norton-2011]: –––, 2011, “Observationally Indistinguishable Spacetimes: a Challenge for Any Inductivist”, in *Philosophy of Science Matters: The Philosophy of Peter Achinstein*, Gregory J. Morgan (ed.), Oxford: Oxford University Press, pages 164–166.

[^o’raifeartaigh-1917]: O’Raifeartaigh, Cormac, Michael O’Keeffe, Werner Nahm, and Simon Mitton, forthcoming, “Einstein’s 1917 Static Model of the Universe: A Centennial Review”, *The European Physical Journal H*, first online 20 July 2017. doi:10.1140/epjh/e2017-80002-5

[^particle-2016]: Particle Data Group, 2016, “Review of Particle Physics”, *Chinese Physics C*, 40(10): 100001. doi:10.1088/1674-1137/40/10/100001

[^peebles-2003]: Peebles, P.J.E. and Bharat Ratra, 2003, “The Cosmological Constant and Dark Energy”, *Reviews of Modern Physics*, 75(2): 559–606. doi:10.1103/RevModPhys.75.559

[^penrose-1979]: Penrose, Roger, 1979, “Singularities and Time-Asymmetry”, in Hawking & Israel 1979: 581–638.

[^penrose-2016]: –––, 2016, *Fashion, Faith, and Fantasy in the New Physics of the Universe*, Princeton: Princeton University Press.

[^peter-2013]: Peter, Patrick and Jean-Philippe Uzan, 2013, *Primordial Cosmology*, Oxford: Oxford University Press.

[^quine-1970]: Quine, W.V., 1970, “On the Reasons for Indeterminacy of Translation”, *The Journal of Philosophy*, 67(6): 178–183. doi:10.2307/2023887

[^roush-2003]: Roush, Sherrilyn, 2003, “Copernicus, Kant, and the Anthropic Cosmological Principles”, *Studies in History and Philosophy of Science Part B: Studies In History and Philosophy of Modern Physics*, 34(1): 5–35. doi:10.1016/S1355-2198(02)00029-1

[^schwarz-2016]: Schwarz, Dominik J., Craig J. Copi, Dragan Huterer, and Glenn D. Starkman, 2016, “CMB Anomalies After Planck”, *Classical and Quantum Gravity*, 33(18): 184001. doi:10.1088/0264-9381/33/18/184001

[^silk-2017]: Silk, Joseph, 2017, “Formation of Galaxies”, in Chamcham et al. 2017: 161–178. doi:10.1017/9781316535783.009

[^smeenk-2012]: Smeenk, Christopher, 2012, “Einstein’s Role in the Creation of Relativistic Cosmology”, in Michel Janssen and Christopher Lehner (eds), *Cambridge Companion to Einstein*, Cambridge: Cambridge University Press. doi:10.1017/CCO9781139024525.009

[^smeenk-2014]: –––, 2014, “Predictability Crisis in Early Universe Cosmology”, *Studies in History and Philosophy of Science Part B: Studies in History and Philosophy of Modern Physics*, 46(part A): 122–133. doi:10.1016/j.shpsb.2013.11.003

[^smeenk-2017]: –––, 2017, “Testing Inflation”, in Chamcham et al. 2017: 206–227. doi:10.1017/9781316535783.011

[^smith-2014]: Smith, George E., 2014, “Closing the Loop”, in Zvi Biener and Eric Schliesser (eds), *Newton and Empiricism*, Oxford: Oxford University Press, pages 262–351. doi:10.1093/acprof:oso/9780199337095.003.0011

[^stanford-2009]: Stanford, P. Kyle, 2009 [2016], “Underdetermination of Scientific Theory”, *The Stanford Encyclopedia of Philosophy* (Spring 2016 Edition), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/spr2016/entries/scientific-underdetermination/](https://plato.stanford.edu/archives/spr2016/entries/scientific-underdetermination/)>

[^stanford-2006]: –––, 2006, *Exceeding Our Grasp: Science, History, and the Problem of Unconceived Alternatives*, Oxford: Oxford University Press. doi:10.1093/0195174089.001.0001

[^starkman-2006]: Starkman, Glenn D. and Roberto Trotta, 2006, “Why Anthropic Reasoning Cannot Predict $\Lambda$”, *Physical Review Letters*, 97(20): 201301. doi:10.1103/PhysRevLett.97.201301

[^steigman-2007]: Steigman, Gary, 2007, “Primordial Nucleosynthesis in the Precision Cosmology Era”, *Annual Review of Nuclear and Particle Science*, 57: 463–491. doi:10.1146/annurev.nucl.56.080805.140437

[^stein-1994]: Stein, Howard, 1994, “Some Reflections on the Structure of Our Knowledge in Physics”, in *Logic, Metholodogy and Philosophy of Science, Proceedings of the Ninth International Congress of Logic, Methodology and Philosophy of Science*, D. Prawitz, B. Skyrms, and D. Westerståhl (eds), Elsevier Science, pages 633–55.

[^synge-1961]: Synge, J.L., 1961, *Relativity: the General Theory*, Amsterdam: North-Holland.

[^titelbaum-2013]: Titelbaum, Michael G., 2013, *Quitting Certainties: A Bayesian Framework Modeling Degrees of Belief*, Oxford: Oxford University Press. doi:10.1093/acprof:oso/9780199658305.001.0001

[^trotta-2008]: Trotta, Roberto, 2008, “Bayes in the Sky: Bayesian Inference and Model Selection in Cosmology”, *Contemporary Physics*, 49(2): 71–104. doi:10.1080/00107510802066753

[^unger-2014]: Unger, Roberto Mangabeira and Lee Smolin, 2014, *The Singular Universe and the Reality of Time*, Cambridge: Cambridge University Press.

[^fraassen-1980]: van Fraassen, Bas C., 1980, *The Scientific Image*, Oxford: Clarendon Press. doi:10.1093/0198244274.001.0001

[^vilenkin-1983]: Vilenkin, Alexander, 1983, “The Birth of Inflationary Universes”, *Physical Review D*, 27(12): 2848–2855. doi:10.1103/PhysRevD.27.2848

[^vilenkin-1995]: –––, 1995, “Predictions from Quantum Cosmology”, *Physical Review Letters*, 74(6): 846–849. doi:10.1103/PhysRevLett.74.846

[^vilenkin-2007]: –––, 2007, *Many Worlds in One: the Search for Other Universes*, New York: Hill and Wang.

[^wagner-2014]: Wagner, Andreas, 2014, *Arrival of the Fittest: Solving Evolution’s Greatest Puzzle*, New York: Penguin.

[^wainwright-1997]: Wainwright, J. and G.F.R. Ellis, 1997, *Dynamical Systems in Cosmology*, Cambridge: Cambridge University Press.

[^wald-1984]: Wald, Robert M., 1984, *General Relativity*, Chicago: University of Chicago Press.

[^wang-2017]: Wang, Qingdi, Zhen Zhu, and William G. Unruh, 2017, “How the Huge Energy of Quantum Vacuum Gravitates to Drive the Slow Accelerating Expansion of the Universe” *Physical Review D*, 95(10): 103504. doi:10.1103/PhysRevD.95.103504

[^weinberg-2015]: Weinberg, David H., James S. Bullock, Fabio Governato,Rachel Kuzio de Naray, and Annika H.G. Peter, 2015, “Cold Dark Matter: Controversies on Small Scales”, *Proceedings of the National Academy of Sciences*, 112(40): 12249–12255. doi:10.1073/pnas.1308716112

[^weinberg-1987]: Weinberg, Steven, 1987, “Anthropic Bound on the Cosmological Constant”, *Physical Review Letters*, 59(22): 2607–2610. doi:10.1103/PhysRevLett.59.2607

[^zhang-2011]: Zhang, Pengjie and Albert Stebbins, 2011, “Confirmation of the Copernican Principle Through the Anisotropic Kinetic Sunyaev Zel’Dovich Effect”, *Philosophical Transactions of the Royal Society of London A: Mathematical, Physical and Engineering Sciences*, 369(1957): 5138–5145. doi:10.1098/rsta.2011.0294

[^zhang-2010]: Zhang, Ray and Dragan Huterer, 2010, “Disks in the Sky: a Reassessment of the WMAP ‘Cold Spot’”, *Astroparticle Physics*, 33(2): 69–74. doi:10.1016/j.astropartphys.2009.11.005
