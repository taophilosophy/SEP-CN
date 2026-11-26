# Thermodynamic Asymmetry in Time
**First published Thu Nov 15, 2001; substantive revision Fri Jun 12, 2026**

*Callender, Craig*

The thermodynamic time asymmetry is one of the most salient and consequential features of the physical universe. Heat flows from hot to cold. The smell of coffee spreads throughout its available volume. Car engines convert fuel energy into work and thermal energy. And so on. The temporally reversed order of these processes never happen. The science of thermodynamics is able to capture these generalizations and much more as consequences of its claim that systems spontaneously evolve to future equilibrium states but do not spontaneously evolve away from equilibrium states. This generalization covers an amazing amount of macroscopic physics and is rightly celebrated as one of the great laws of physics.

Although familiar, the thermodynamic arrow of time raises many deep questions relevant to both philosophy and the foundations of physics. This entry concentrates on two of them. In contemporary parlance, they are each questions about grounding. (1) What grounds the thermodynamic asymmetry in time? In a world possibly governed at bottom by time-symmetric laws, how do the time-asymmetric laws of thermodynamics arise? (2) Does the thermodynamic time asymmetry ground any other temporal asymmetries? Does it account, for instance, for the fact that we know more about the past than the future? The discussion thus divides between thermodynamics being an explanandum or explanans. What grounds the thermodynamic asymmetry, and given the asymmetry, what does it ground?

## 1. Thermodynamic Time Asymmetry: A Brief Guide

Thermodynamics is the science of heat and temperature. In English, the term “thermo-dynamic” was first used by William Thomson in 1849 to describe a steam engine that converted heat into work. That is an appropriate introduction because the scientific development of classical thermodynamics is intimately associated with the industrial revolution and the desire to improve the efficiency of engines that turned heat into motion. In the mid-nineteenth century, Rudolf Clausius in Germany and William Thomson in England (later becoming Lord Kelvin) invented the theory, which (at a coarse-level) was the result of weaving together advances in understanding the conservation of energy with a central insight found in Carnot (1824)[^carnot-1824]. The resulting science quickly spread throughout Europe by the late nineteenth and early twentieth centuries (Brush 1976, Cardwell 1971, Mendoza 1961, Müller 2006, Saslaw 2020)[^brush-1976][^cardwell-1971][^mendoza-1961][^müller-2006]. As it was refined the theory’s scope grew from engines and the like to an increasingly wide range of macroscopic processes.

Although the science was only developed in the nineteeth century, thermodynamic generalizations have been known for all of human history. Rubbing one’s hands warms them. Striking pyrite with flint creates fire. There was also a long history of perpetual motion skeptics. Da Vinci, for example, wrote, “Oh, ye seekers after perpetual motion, how many vain chimeras have you pursued? Go and take your place with the alchemists” (Da Vinci 1494). In addition to such qualitative regularities, quantitative generalizations were also known prior to the development of the science. For example, Galileo’s “thermoscope” of 1626 measured air density and was later calibrated; regularities between its readings and weather patterns were discovered. For the early history of empirical temperature, see Chang 2004. Newton’s law of cooling, which is still commonly used today, was not expressed explicitly in a formula, but the mathematical relationship was clear: that the surface temperature of any object is proportional to the difference between its temperature and that of its ambient surroundings (Besson 2012)[^besson-2012].

Thermodynamics is a “phenomenal” science. That means that its variables range over macroscopic parameters such as temperature, pressure and volume. These are properties that hold at equilibrium, i.e., when the values of the macroscopic variables remain approximately stable. Whether the microphysics underlying these variables are motive atoms in the void or an “imponderable” (massless) fluid like caloric is largely irrelevant to this science. The developers of the theory both prided themselves on this fact and at the same time worried about it. Clausius, for instance, was one of the first to speculate that heat consisted solely of the motion of particles (without an ether), for it made the equivalence of heat with mechanical work less surprising. However, as was common, he kept his “ontological” beliefs separate from his official statement of the principles of thermodynamics because he didn’t wish to (in his words) “taint” the latter with the speculative character of the former. For a nice discussion of this point within the debate about scientific realism, see Psillos (1994)[^psillos-1994].

Thermodynamics begins with characterizing the thermodynamic state of systems. A state is given by the minimal set of thermodynamic variables necessary to define a system. The variables are divided into intensive and extensive ones. Intensive variables have the same value throughout the system at equilibrium, independent of the amount or extent of material. Pressure and temperature are examples. Extensive variables don’t have the same value throughout the system at equilibrium and depend on the amount or extent of material. Volume and entropy are examples. The product of intensive and extensive variables has dimensions of work, which suggests a kind of Newtonian analogy where intensive variables are like forces and extensive ones like displacements. Thermodynamics finds equations of state that are functional relationships amongst thermodyanmic parameters in equilibrium. So, for instance, for a homogenous fluid, one can measure the temperature *T*, volume *V*, and pressure *P*. These are not independent: $f(T,V,P) = 0$. Hence the thermodynamic state can be characterized by two of the three variables. Boyle’s (or Mariotte’s) Law, Charles’ Law, and the Ideal Gas Law, are examples of well-known equations of state.

The science is usually presented with the statements it takes to be laws of nature. Founded upon observations of relationships amongst particular macroscopic parameters, they are justified by the fact they are empirically adequate. No further justification of these laws is to be found – at this stage – from the details of microphysics. Rather, stable, counterfactual-supporting generalizations about macroscopic features are enshrined as law. It is worth remarking that there are almost as many “packages” of laws proposed to capture thermodynamics as there are presentations. The founders of the subject often started with different primitive kinds and/or observational regularities as foundational. Many of these are not equivalent. This rather messy state of affairs triggered attempts to clean up the subject with greater mathematical rigor. Originating from the early axiomatization by Carathéodory in 1909, the development of “rational thermodynamics” has clarified the concepts and logic of classical thermodynamics to a degree not generally appreciated. There now exist many mathematically exact approaches to thermodynamics. (For a popular presentation of a recent axiomatization, see Lieb and Yngvason 2000; for a philosophical dispute about the origins of time asymmetry within this formalism, see Uffink 2001 and Henderson 2014.)[^lieb-2000][^uffink-2001] Even these, however, are often not formally equivalent to one another.

In the traditional approach to the subject classical thermodynamics has two laws, the First and Second Laws. This approach is based on the historical fact that Clausius and Thomson each presented the theory in this way (see Clausius 1850, 1854, Thomson 1849, 1851)[^clausius-1851][^thomson-1849].

The First Law expresses the conservation of energy and is founded upon the impossibility of creating a machine that can create energy from nothing. The law uses the concept of the internal energy of a system, $U$, which is a function of the system’s macroscopic variables, e.g., temperature, volume. For thermally isolated (adiabatic) systems – think of systems such as coffee in a thermos – the law states that this function, $U$, is such that the work $W$ delivered to a system’s surroundings is compensated by a loss of internal energy, i.e., $dW = -dU$. When James Joule and Robert Mayer showed that mechanical work and heat were interconvertible, consistency with the principle of energy conservation demanded that heat, $Q$, considered as a different form of energy, be taken into account. For non-isolated systems we extend the conservation law as $dQ = dU + dW$, where $dQ$ is the differential of the amount of heat added to the system (in a reversible manner).

Placing no limitations on transforming energy from one form into another, the First Law permits the possibility of machines that remove heat from their environment and turn it entirely into work (a so-called perpetual mobile of the second kind). In skeptical discussions of perpetual motion machines that would deliver “free” work, there was a growing sense that nature always “taxed” our transactions, that one could not get work for free. In this thought we find the seed for the Second Law.

The Second Law was first discovered by Carnot in 1824 and later reproduced and expanded by Clapeyron 1834. Carnot’s theorem is the central insight behind thermodynamics. Using a theoretical construct we now call a Carnot engine, which is an idealized heat engine operating on a perfectly reversible thermodynamic cycle, Carnot proves that no engine can have greater efficiency than a Carnot engine operating between two temperatures. In an era of constantly improved steam engines, this result was remarkable. It means that no matter how clever you are, you can’t do better than a Carnot engine. The law transcends all modifications of engine design and working substances. It represents an upper limit in nature, like the speed of light. And since all actual engines are irreversible, a corollary is that no real engine can be perfectly efficient. They always take a “tax.” Another important corollary is that this perfect efficiency defines an absolute (as opposed to merely empirical) temperature scale. (On puzzles regarding the notion of reversibility, see Norton (2016)[^norton-2016].)

Although Carnot was the first to state it, the formulations of Thomson (typically called “Kelvin” in this context) and Clausius are standard:

Kelvin’s Second Law: There is no thermodynamic process whose sole effect is to transform heat extracted from a source at uniform temperature completely into work.

Clausius’ Second Law: There is no thermodynamic process whose sole effect is to extract a quantity of heat from a colder reservoir and deliver it to a hotter reservoir.

Kelvin’s version is essentially the same as the version arrived at by both Carnot and (later) Planck, whereas Clausius’ version differs from these in a few ways. (A third version, inequivalent to both of the above, is Carathéodory’s law. It states that in the neighborhood of any equilibrium state of a system there are states that are inaccessible by an adiabatic process. This considerably more abstract version of the second law forbids a more general type of process than the other formulations.)

Clausius’ version transparently rules out anti-thermodynamic behavior such as a hot iron bar extracting heat from a neighboring cold iron bar. The cool bar cannot give up a quantity of heat to the warmer bar (without something else happening). Kelvin’s statement is perhaps less obvious. It originates in an observation about steam engines, namely, that heat energy is a “poor” grade of energy. Consider a gas-filled cylinder with a frictionless piston holding the gas down at one end. If we put a flame under the cylinder, the gas will expand and the piston can perform work, e.g., it might move a ball. However, we can never convert the heat energy straight into work without some other effect occurring. In this case, the gas occupies a larger volume.

In 1854, Clausius introduced the notion of the “equivalence value” of a transformation, a concept that is the ancestor of the modern day concept of entropy. Later in 1865 Clausius coined the term “entropy” for a similar concept (the word derives from the Greek word for transformation). The entropy of a state $A$, $S(A)$ is defined as the integral $S(A) = \int^{A}_{O} dQ/T$ over a reversible transformation, where $O$ is some arbitrary fixed state. For $A$ to have an entropy, the transformation from $O$ to $A$ must be quasi-static, i.e., a succession of equilibrium states. Continuity considerations then imply that the initial and final states $O$ and $A$ must also be equilibrium states. Put in the language of entropy, the Second Law states that in a transformation from equilibrium state $A$ to equilibrium state $B$, the inequality $S(B) - S(A)$ is greater than or equal to the $\int^{A}_{B} dQ/T$. Loosely put, for realistic systems, this implies that in the spontaneous evolution of a thermally closed system the entropy can never decrease and that it attains its maximum value at equilibrium. We are invited to think of the Second Law as driving the system to its new, higher entropy equilibrium state.

With the Second Law, thermodynamics is able to characterize an extraordinary range of phenomena under one simple law. Remarkably, whether they are gases filling their available volumes, iron bars in contact coming to the same temperature, vinegar and oil separating, or milk mixing in your coffee, they all have an observable property in common: their entropy increases. Coupled with the First Law, the Second Law is remarkably powerful. Penrose 1970 claims that all classical thermodynamical behavior can be derived from these two simple statements.

The above sketch represents the conventional way of describing thermodynamics and its two laws. The “core” of the science is the result of meshing together energy conservation (especially the mechanical equivalence of heat established by James Joule and Robert Mayer) with Carnot’s theorem on the limits of efficiency. Often these treatments are supplemented with two additionals laws, the Zeroth and the Third. The Zeroth Law is that the ‘equilibrium with’ relation is transitive. If two systems are each in equilibrium with a third, then they must be in equilibrium with one another. While this law is sometimes found loosely put in writings by Maxwell, Sommerfeld 1951 claims that Ralph H. Fowler coined the term “zeroth law” while discussing Saha and Srivastava 1935. Associated with Walther Nerst, the Third Law holds that the entropy of a closed system at thermodynamic equilibrium tends to a constant value as its temperature approaches absolute zero (Nerst 1966). This law is notorious for coming in various inequivalent formulations.

Many interesting philosophical questions arise about the Second Law.

First, what is its scope? There are two issues here. First, does it apply to the universe as a whole, so that we can say the universe’s entropy is increasing, or does it only apply to select sub-systems of the universe? Many philosophers and physicists have balked at the idea that the universe itself has an entropy. As one might expect, those in the grip of operationalist or strongly empircist philosophies may be especially prone to deny that the universe as a whole has an entropy. See Uffink 2001. Second, what sub-systems of the universe does it govern? Are the principles of thermodynamics responsible for generalizations about black holes? The field of black hole thermodynamics assumes it is (see singularities and black holes), although not all are convinced. See Dougherty and Callender 2026, Prunkl and Timpson 2019, and Wallace 2018 for discussion. Does the Second Law cover systems who primarily interact via gravitational self-interaction, such as stars, galaxies, and clusters? See Callender 2010, 2011a, Lorenzetti 2025, Robertson 2019, Wallace 2010.

Second, how are these laws framed in a quantum and relativistic universe? They were developed in the nineteenth century with a classical spacetime background in mind. How do we write the theory in a modern formulation? Surprisingly, the issue is as much conceptual as technical. The correct (special) relativistic transformation rules for thermodynamic quantities are controversial. Do Lorentz boosted gases appear hotter or colder in the new inertial frame? Albert Einstein himself answered the question about the gas differently throughout his life! With so much activity in physics focused on the thermodynamics of black holes in general relativity and quantum gravity, it is amusing to note that special relativistic thermodynamics is still a field with many open questions, both physically and philosophically (see Earman 1981, Liu 1994, Chua 2023, Wallace 2025a)[^chua-2023][^liu-1994][^wallace-2025a]. A separate issue arises in general relativity when one tries to accomodate the Tolman-Ehrenfest effect into the usual laws of thermodynamics. See Chua and Callender (2026) and Santago and Visser (2019). As one might expect, understanding the laws quantum mechanically is also challenging (see, e.g. Chua 2026)[^chua-2026][^chua-2026-2].

Third, do thermodynamic concepts such as entropy, temperature, and so on “reduce” to their mechanical, or statistical mechanical, basis? As even a cursory glance at statistical mechanics reveals, there are many candidates for the statistical mechanical entropy, each the center of a different program in the foundations of the field. Surprisingly, there is no consensus as to which entropy is best suited to be the reduction basis of the thermodynamic entropy (see, for example, Albert 2000, Callender 1999; Goldstein et al 2020, Lavis 2005; Lebowitz 1993a, 1993b; Frigg 2008; Myrvold 2021; Robertson 2022, Roberts 2022, Sklar 1993)[^albert-2000][^callender-1999][^frigg-2008][^goldstein-2020][^lavis-2005][^lebowitz-1993a][^lebowitz-1993b][^myrvold-2021][^roberts-2022][^robertson-2022][^sklar-1993]. Consequently, there is little agreement about what grounds the Second Law in statistical mechanics.

Despite the worthiness of all of these issues, this article focuses on two distinct problems associated with the direction of time. First, however, we’ll try to identify the source of the temporal asymmetry, which is itself a topic of investigation.

## 2. Where is the Time Asymmetry?

It is almost universally acknowledged that the temporally asymmetric aspects of the pheneomena with which we began are captured by the Second Law. Loosely put, the Second Law is understood as the claim that entropy spontaneously increases with time. A system of two iron bars at the same temperature has a higher entropy than a system composed of a hot bar touching a cold bar. So it seems that the Second Law tracks the temporal process of heat flowing from the hot bar to the cold bar until equilibrium is achieved and rules out the temporal reverse from happening.

It does, but only in a *conditional* sense. The Second Law relates equilibrium states. To capture what happens to the iron bars, it assumes facts about non-equilibrium states too. When we place a bar at one temperature against a bar at another temperature, we have created a non-equilibrium system. Will this non-equilibrium system later evolve to another equilibrium system? That is not guaranteed by the Second Law. The Second Law only says that if the system evolves to another equilibrium state, that final state’s entropy will not be lower than the initial state’s entropy. That is compatible with the system evolving to equilibrium states of the same entropy, of course, but also, and crucially, with the system never evolving to equilibrium again. The Second Law doesn’t force the two irons bars to go to equilibrium; it only says, *if* they do, their entropy is not lower than before.

Indeed, this point is connected to a related one, which is often asked as a question: why isn’t thermodynamics called “thermostatics”? The science of transformations lacks any explicit time variable. Even the “before” two sentences up is implicit.

Recognizing the importance of this lacuna, physicists Uhlenbeck and Ford (1963) and Lebowitz (1993a, 1993b)[^lebowitz-1993a][^lebowitz-1993b] propose adding a new zeroth law to capture the assumed temporal asymmetry. However, because the Zeroth Law is already named, Brown and Uffink (2001)[^uffink-2001] propose calling it the Minus First Law. As a formulation, they propose: “An isolated system in an arbitrary initial state within a finite fixed volume will spontaneously attain a unique state of equilibrium.” This Law would establish the existence and uniqueness of equilibrium states and the spontaneous approach to equilibrium from non-equilibrium. See also Roberts (2022)[^roberts-2022]. Brown and Uffink ground the time asymmetry in the notion of equilibrium. Its defining property, they hold, is “that once they are attained, they remain thereafter constant in time, unless the external conditions are changed” (Brown and Uffink 2001, p.528)[^brown-2001][^uffink-2001].

As we dig through thermodynamics to find its time asymmetric heart, however, there is still another step. Roberts (2026)[^roberts-2026] notes that, strictly speaking, one could understand “thereafter constant in time” in either temporal direction. Non-equilibrium states could approach equilibrium states in both temporal directions compatible with the Minus First Law. Do we then need a “Minus Second Law”? Perhaps. We need the assumption that some of these non-equilibrium states were in the past. Later (Section 3.1) we will encounter the Past Hypothesis as an explanation for time asymmetry in statistical mechanics. Roberts argues that we need something like this special temporally asymmetric “initial” condition even in thermodynamics.

If this is right, then the time asymmetry of thermodynamics is buried very deeply, at least concering the Second Law. (Many other principles of thermodynamics are explicitly time-asymmetric, e.g., the classical heat equation.) Depending on what one counts as thermodynamics, the time asymmetry may not even be part of thermodynamics. As Myrvold (2021)[^myrvold-2021] notes, it is unique among core principles in not making a distinction between energy transfer as heat and as work. If we regard that distinction as central to thermodynamics proper, then perhaps it’s better to say, with Myrvold, that the time asymmetry in the Minus First Law is more a presupposition than a part of thermodynamics. For further discussion relevant to this discussion, see Wallace (2025b)[^wallace-2025b].

## 3. The Problem of the Direction of Time I

The first “problem of the direction of time” is: what accounts for the time asymmetry of thermodynamics (wherever located)? Thermodynamics is not a fundamental physical science. Hence it must inherit its massive time asymmetry from the microworld. But from where? What, fundamnetally, makes thermodynamics time asymmetric? The puzzle is usually said to arise due to fundamental physics being time symmetric, or more precisely, time reversal invariant. (A theory is time reversal invariant, loosely speaking, if its laws don’t care about the direction of time.) The intuition behind the question is: no asymmetry in, no asymmetry out. Hence there is a puzzle over where the asymmetry enters.

However, even if fundamental physics is time asymmetric, one can and should still demand an answer to the question of what accounts for thermodynamics’ time asymmetry. The possible time asymmetry of fundamental physics may have nothing to do with the time asymmetry of thermodynamics. This situation actually appears to be the case, as weak interactions between quarks and leptons can violate time symmetry yet these violations don’t appear to be responsible for thermodynamic behavior. But see Roberts (2022)[^roberts-2022].

Historically the problem arose in a wonderful series of debates and arguments between the great physicist Ludwig Boltzmann and some of his contemporaries, notably, Johann Loschmidt, Ernst Zermelo and Edward Culverwell. Boltzmann was one of the founders and most influential developers of the field of statistical mechanics, as well as (later in life) a philosopher. While seeking a mechanical underpinning of the Second Law, he discovered a particularly ingenious explanation for why systems tend toward equilibrium.

Ignoring historical details (see Brush 1976, Frigg & Werndl 2011, Sklar 1993, Uffink 2006)[^brush-1976][^frigg-2011][^sklar-1993][^uffink-2006], here is the core idea loosely reconstructed from Boltzmann’s later writings. Consider an isolated gas of $N$ particles in a box, where $N$ is large enough to make the system macroscopic $(N \approx 10^{23}+)$. For the sake of familiarity we will work with classical mechanics. We can characterize the gas by the coordinates and momenta $x_{in}, p_{in}$ of each of its particles and represent the whole system by a point $X = (q,p)$ in a $6N$-dimensional phase space known as *Γ*, where $q = (q_1 \ldots q_{3N})$ and $p = (p_1 \ldots p_{3N})$. Boltzmann’s great insight was to see that the thermodynamic entropy arguably “reduced” to the volume in *Γ* picked out by the macroscopic parameters of the system. The key ingredient is partitioning *Γ* into compartments, such that all of the microstates $X$ in a compartment are macroscopically (and thus thermodynamically) indistinguishable. To each macrostate $M$, there corresponds a volume of *Γ*, $\lvert\Gamma_M\rvert$, whose size will depend on the macrostate in question. For combinatorial reasons, almost all of *Γ* corresponds to a state of thermal equilibrium. There are simply many more ways to be distributed with uniform temperature and pressure than ways to be distributed with nonuniform temperature and pressure. There is a vast numerical imbalance in *Γ* between the states in thermal equilibrium and the states in thermal nonequilibrium.

We now introduce Boltzmann’s famous formula (up to an additive constant) for what we might call the “Boltzmann entropy” $S_B$: $$ S_B (M(X)) = k \log \lvert\Gamma_M\rvert $$ where $\lvert\Gamma_M\rvert$ is the volume in *Γ* associated with the macrostate $M$, $X$ is the microstate of the system, and $k$ is Boltzmann’s constant. $S_B$ provides a relative measure of the amount of *Γ* corresponding to each $M$.

Given the mentioned asymmetry in *Γ*, almost all microstates *realizing non-equilibrium macrostates* are such that their entropy value is overwhelmingly likely to increase with time. When the constraints are released on systems initially confined to small sections of *Γ*, *typical* systems will evolve into larger compartments. Since the new equilibrium distribution occupies *almost all* of the newly available phase space, nearly all of the microstates originating in the smaller volume will tend toward equilibrium. Except for those incredibly rare microstates conspiring to stay in small compartments, microstates will evolve in such a way as to have $S_B$ increase. Substantial questions can be raised about the details of this approach. What justifies, for instance, the standard probability measure on *Γ*? Nonetheless, the Boltzmannian explanation seems to offer a plausible and powerful *framework* for understanding why the entropy of systems tends to increase with time. (For further explanation and discussion see Bricmont 1995; Callender 1999; Frigg 2008, 2009; Goldstein 2001; Hemmo & Shenker 2012; Klein 1973; Lavis 2005; Lebowitz 1993a, 1993b; Uffink 2006.)[^bricmont-1995][^callender-1999][^frigg-2008][^frigg-2009][^goldstein-2001][^hemmo-2012][^klein-1973][^lavis-2005][^lebowitz-1993a][^lebowitz-1993b][^uffink-2006]

Trouble looms over this explanation of time asymmetry (see Brown, Myrvold, & Uffink 2009)[^brown-2009]. Before Boltzmann explained entropy increase as described above, he proposed a now notorious “proof” known as the “$H$-theorem” to the effect that entropy must always increase. Loschmidt 1876/1877 and Zermelo 1896 launched objections to the $H$-theorem. If we take as premises the central laws of conservative classical mechanical dynamics, they pointed out, it’s impossible to get any function of the classical state to monotonically increase. Loschmidt focused on the time reversal invariance of the classical dynamics and Zermelo on its recurrence property (roughly, that a bounded system, left to itself, will eventually return arbitrarily close to its initial state, for any given initial state). They were right: time reversal means that for every entropy-increasing solution to the classical equations there is a mirror entropy-decreasing solution; and recurrence means that every solution will at some point have its entropy decrease if we wait long enough. Some time asymmetric ingredient that had not been properly announced had been smuggled into the theorem.

The reader can find this story in many textbooks and in many references cited above. An objection in their spirit (specifically, Loschmidt’s) can also be advanced against Boltzmann’s later view sketched above. Loosely put, because the classical equations of motion are time reversal invariant, nothing in the original explanation necessarily referred to the direction of time (see Hurley 1986)[^hurley-1986]. Although we just stated the Boltzmannian account of entropy increase in terms of entropy increasing into the future, the explanation can be turned around and made for the *past* temporal direction as well. Given a gas in a box that is in a nonequilibrium state, the vast majority of microstates that are *antecedents* of the dynamical evolution leading to the present macrostate correspond to a macrostate with *higher entropy* than the present one. Therefore, not only is it highly likely that typical microstates corresponding to a nonequilibrium state *will evolve to* higher entropy states, but it is also highly likely that they *evolved from* higher entropy states.

Concisely put, the problem is that given a nonequilibrium state at time $t_2$, it is overwhelmingly likely that

**(1)**

the nonequilibrium state at $t_2$ will evolve to one closer to equilibrium at $t_3$

but that due to the reversibility of the dynamics it is also overwhelmingly likely that

**(2)**

the nonequilibrium state at $t_2$ has evolved from one closer to equilibrium at $t_1$

where $t_1 \lt t_2 \lt t_3$. However, transitions described by (2) do not seem to occur; or phrased more carefully, not both (1) and (2) occur. However we choose referents for the terms “earlier” and “later”, clearly entropy doesn’t increase in both temporal directions. For ease of exposition let us dub (2) the culprit.

The traditional problem is not merely that nomologically possible (anti-thermodynamic) behavior does not occur when it could. That is not straightforwardly a problem: *all sorts* of nomologically allowed processes do not occur. Rather, the problem is that statistical mechanics seems to make a prediction that is falsified, and that is a problem according to anyone’s theory of confirmation.

Many solutions to this problem have been proposed. Generally speaking, there are two ways to solve the problem: eliminate transitions of type (2) either with special boundary conditions or with laws of nature. The former method works if we assume that *earlier* states of the universe are of comparatively low-entropy *and* that (relatively) *later* states are not also low-entropy states. There are no high-to-low-entropy processes simply because earlier entropy was very low. Alternatively, the latter method works if we can somehow restrict the domain of physically possible worlds to those admitting only low-to-high transitions. The laws of nature are the straightjacket on what we deem physically possible. Since we need to eliminate transitions of type (2) while keeping those of type (1) (or vice versa), a necessary condition of the laws doing this job is that they be time reversal noninvariant. Our choice of strategy boils down to either assuming temporally asymmetric boundary conditions or of adding (or changing to or restricting to) time reversal noninvariant laws of nature that make entropy increase likely. Many approaches to this problem have thought to avoid this dilemma, but a little analysis of any proposed “third way” arguably proves this to be false.

Motivations for restrictions of type (2) transitions originate in both philosophy and in particular physical theories. The rest of this section describes some of the wide range of views found on the issue.

### 3.1 Past Hypothesis

Without proclaiming the laws of nature time asymmetric, there is no way to eliminate as impossible transitions (2) in favor of (1). Nevertheless, appealing to temporally asymmetric boundary conditions allows us to describe a world wherein (1) but not (2) occur. A cosmological hypothesis claiming that in the very distant past entropy was much lower will work. Boltzmann, as well as many of the twentieth century’s greatest scientists, e.g., Einstein, Richard Feynman, and Erwin Schroedinger, saw that this hypothesis is necessary given our (mostly) time asymmetric laws. (Boltzmann, however, explained this low-entropy condition by treating the observable universe as a natural statistical fluctuation away from equilibrium in a vastly larger universe.) Earlier states do not have higher entropy than present states because we make the cosmological posit that the universe began in an extremely tiny section of its available phase space. Albert (2000)[^albert-2000] calls this the “Past Hypothesis” and argues that it solves both this problem of the direction of time and also the one to be discussed below. Note that classical mechanics is also compatible with a “Future Hypothesis”: the claim that entropy is very low in the distant future. The restriction to “distant” is needed, for if the near future were of low-entropy, we would not expect the thermodynamic behavior that we see – see Cocke 1967, Price 1996, and Schulman 1997 for discussion of two-time boundary conditions.

The Past Hypothesis offers an elegant solution to the problem of the direction of time. However, there are some concerns.

First, some find it incredible that systems everywhere for all time should display thermodynamic behavior due to special initial conditions. The common cause of these events is viewed as itself monstrously unlikely. Expressing this feeling, R. Penrose (1989)[^penrose-1989] estimates that the probability, given the standard measure on phase space, of the universe starting in the requisite state is astronomically small. In response, one may hold that the Past Hypothesis is lawlike. If so, then the probability for this state, if such exists, is one! Even if one doesn’t go down this path, there is the question of whether the Past Hypothesis itself demands explanation. In physics it is often claimed that explaining the Past Hypothesis is a central problem. But why? And what would an explanation look like? See Callender 2004a,b for some skepticism that explaining the Past Hypothesis is demanded and Price 1996, 2004 for the contrary position (and Baras and Shenker 2020 for diagnosis)[^baras-2020].

Second, another persistent line of criticism might be labeled the “subsystem” worry. It’s consistent with the Past Hypothesis, after all, that none of the subsystems on Earth ever display thermodynamically asymmetric behavior. How exactly does the *global* entropy increase of the universe imply *local* entropy increase among the subsystems (which, after all, is what causes us to posit the Second Law in the first place)? This objection is often motivated by a Reichenbachian “branch systems” picture of entropy increase (see Reichenbach 1956)[^reichenbach-1956]. See Winsberg 2004 for the subsystems objection and Albert 2025, Callender 2011b, Frisch 2010, and North 2011 for discussion.

Third, what exactly does the Past Hypothesis say in the context of our best and most recent physics? While not denying that temporally asymmetric boundary conditions are needed to solve the problem, Earman (2006)[^earman-2006] is very critical of the Past Hypothesis, concluding that it isn’t even coherent enough to be false. The main problem Earman sees is that we cannot state the Past Hypothesis in the language of general relativity. Callender (2010, 2011a)[^callender-2010][^callender-2011a] and Wallace (2010)[^wallace-2010] discuss the related question of stating the Past Hypothesis when self-gravitation is included. One may also consider the question in the context of quantum theory (see Wallace 2013, 2023, Chen 2023, 2024)[^chen-2023][^chen-2024][^wallace-2013][^wallace-2023].

### 3.2 Electromagnetism

If we place an isolated concentrated homogeneous gas in the middle of a large empty volume, we would expect the particles to spread out in an expanding sphere about the center of the gas, much as waves of radiation spread out from concentrated charge sources. It is therefore tempting to think that there is a relationship between the thermodynamic and electromagnetic arrows of time. In a debate in 1909, Albert Einstein and Walther Ritz apparently disagreed about the nature of this relationship, although the exact points of dispute remain a bit unclear. The common story told is that Ritz took the position that the asymmetry of radiation had to be judged lawlike and that the thermodynamic asymmetry could be derived from this law. Einstein’s position is instead that “irreversibility is exclusively based on reasons of probability” (Ritz and Einstein 1909, English translation from Zeh 1989: 13)[^ritz-1909][^zeh-1989]. It is unclear whether Einstein meant probability plus the right boundary conditions, or simply probability alone. In any case, Ritz is said to believe that the radiation arrow causes the thermodynamic one, whereas Einstein is said to hold something closer to the opposite position. The real story is far more complicated, as Ritz had a particle-based ontology in mind as well as many additional considerations (see Frisch and Pietsch 2016 for subtleties of the actual historical debate)[^frisch-2016].

*If* this common tale is correct – and there is reason to think it isn’t the full story – then it seems that Einstein must be closer to being correct than Ritz. Ritz’ position appears implausible if only because it implies gases composed of neutral particles will not tend to spread out. That aside, Einstein’s position is attractive if we concentrate on the wave asymmetry mentioned above. Using Popper 1956’s famous mechanical wave example as an analogy, throwing a rock into a pond so that waves on the surface spread out into the future requires every bit the conspiracy that is needed for waves to converge on a point in order to eject a rock from the bottom. However, here it does seem clear that one process is favored thermodynamically and the other disfavored once we have a thermodynamic arrow in hand. Given a solution to the thermodynamic arrow, impulses directed toward the center of a pond such as to eject a rock are unlikely, whereas a rock triggering spherical waves diverging from the point of impact are likely. Here the radiation arrow seems plausibly connected to and perhaps even derivable from the thermodynamic arrow. The main interesting difference is that Popper’s time-reversed pond seems approximately attainable whereas anti-thermodynamic processes seem more absolutely forbidden (or at least dramatically harder to engine, requiring a so-called Maxwell Demon).

If the wave asymmetry were the only electromagnetic arrow, then the above sketch would plausibly capture the core connection between the thermodynamic and electromagnetic arrows of time. We would have reason to think that whatever causes the thermodynamic arrow also is responsible for the electromagnetic arrow. That may ultimately be correct. However, it’s too early to conclude that, for electromagnetism is chock full of arrows of time besides the wave asymmetry.

Maxwell’s equations are well-known to include both “advanced” and “retarded” solutions. The retarded solution $$ \phi_{\text{ret}}(r,t) = \int dr' \rho\frac{(r', t- \frac{\lvert r'-r\rvert}{c})}{\lvert r'-r\rvert} $$ gives the field amplitude $\phi_{\text{ret}}$ at $r,t$ by finding the source density $r$ at $r'$ at earlier times. The advanced solution $$ \phi_{\text{adv}}(r,t) = \int dr' \rho\frac{(r', t+ \frac{\lvert r'-r\rvert}{c})}{\lvert r'-r\rvert} $$ gives the field amplitude in terms of the source density at $r'$ at later times. Physicists routinely discard the advanced solutions for reasons of “causality”. It is not so clear thermodynamic considerations are behind this rejection of solutions, an asymmetry made all the harder to see given the freedom electromagnetism has to rewrite retarded fields in terms of advanced fields and outgoing sourceless radiation (and vice versa). Electromagnetism is also said to allow emissions and not absorptions. Accelerating charges are also damped and not anti-damped by the field. With so many arrows besides the wave asymmetry – emission/absorption, in/out, retarded/advanced, damped/anti-damped – it’s premature to say that the thermodynamic arrow is the one arrow to rule them all. Most agree that the wave asymmetry is ultimately “thermodynamic” but after that matters are contested.

For further discussion of these controversial points, see Allori 2015; Arntzenius 1994; Atkinson 2006; Earman 2011; Frisch 2000, 2006; Frisch and Pietsch 2016; Hubert and Sebens 2023; North 2003; Price 1996, 2006; Rohrlich 2006; and Zeh 1989.

### 3.3 Cosmology

Cosmology presents us with a number of apparently temporally asymmetric mechanisms. The most obvious one is the inexorable expansion of the universe. The spatial scale factor $a(t)$, which we might conceive roughly as the radius of the universe (it gives the distance between co-moving “fundamental” observers), is increasing. The universe seems to be uniformly expanding relative to our local frame. Since this temporal asymmetry occupies a rather unique status it is natural to wonder whether it might be the “master” arrow.

The cosmologist Thomas Gold 1962 proposed just this. Believing that entropy values covary with the size of the universe, Gold asserts that at the maximum radius the thermodynamic arrow will “flip” due to the re-contraction. However, as Richard Tolman 1934 has shown in some detail, a universe filled with non-relativistic particles will not suffer entropy increase due to expansion, nor will an expanding universe uniformly filled with blackbody radiation increase its entropy either. Interestingly, Tolman demonstrated that more realistic universes containing both matter and radiation *will* change their entropy contents. Coupled with expansion, various processes will contribute to entropy increase, e.g., energy will flow from the “hot” radiation to the “cool” matter. So long as the relaxation time of these processes is larger than the expansion time scale, they should generate entropy. We thus have a purely cosmological method of entropy generation.

Others (e.g., Davies 1994)[^davies-1994] have thought inflation provides a kind of entropy-increasing behavior – again, given the sort of matter content we have in our universe. The inflationary model is an alternative of sorts to the standard big bang model, although by now it is so well entrenched in the cosmology community that it really deserves the tag “standard”. In this scenario, the universe is very early in a quantum state called a “false vacuum”, a state with a very high energy density and negative pressure. Gravity acts like Einstein’s cosmological constant, so that it is repulsive rather than attractive. Under this force the universe enters a period of exponential inflation, with geometry resembling de Sitter space. When this period ends any initial inhomogeneities will have been smoothed to insignificance. At this point ordinary stellar evolution begins. Loosely associating gravitational homogeneity with low-entropy and inhomogeneity with higher entropy, inflation is arguably a source of a low entropy “initial” condition.

There are other proposed sources of cosmological entropy generation, but these should suffice to give the reader a flavor of the idea. We shall not be concerned with evaluating these scenarios in any detail. Rather, our concern is about how these proposals explain time’s arrow. In particular, how do they square with our earlier claim that the issue boils down to either assuming temporally asymmetric boundary conditions or of adding time reversal non-invariant laws of nature?

The answer is not always clear, owing in part to the fact that the separation between laws of nature and boundary conditions is especially slippery in the science of cosmology. Advocates of the cosmological explanation of time’s arrow typically see themselves as explaining the origin of the needed low-entropy cosmological condition. Some explicitly state that special initial conditions are needed for the thermodynamic arrow, but differ with the conventional “statistical” school in deducing the origin of these initial conditions. Earlier low-entropy conditions are not viewed as the boundary conditions of the spacetime. They came about, according to the cosmological schools, about a second or more after the big bang. But when the universe is the size of a small particle, a second or more is enough time for some kind of cosmological mechanism to bring about our low-entropy “initial” condition. What cosmologists (primarily) differ about is the precise nature of this mechanism. Once the mechanism creates the “initial” low-entropy we have the same sort of explanation of the thermodynamic asymmetry as discussed in the previous section. Because the proposed mechanisms are supposed to make the special initial conditions inevitable or at least highly probable, this maneuver seems like the alleged “third way” mentioned above.

The central question about this type of explanation, as far as we’re concerned, is this: Is the existence of the low “initial” state a consequence of the laws of nature alone or the laws plus boundary conditions? In other words, first, does the proposed mechanism produce low-entropy states given *any* initial condition, and second, is it a *consequence* of the laws *alone* or a consequence of the laws *plus initial conditions*? We want to know whether our question has merely been shifted back a step, whether the explanation is a disguised appeal to special initial conditions. Though we cannot here answer the question in general, we can say that the two mechanisms mentioned are not lawlike in nature. Expansion fails on two counts. There are boundary conditions in expanding universes that do not lead to an entropy gradient, i.e., conditions without the right matter-radiation content, and there are boundary conditions that do not lead to expansion in which entropy nonetheless increases, e.g., matter-filled Friedmann models that do not expand. Inflation fails at least on the second count. Despite advertising, arbitrary initial conditions will not give rise to an inflationary period. Furthermore, it’s not clear that inflationary periods will give rise to thermodynamic asymmetries (Price 1996: ch. 2)[^price-1996]. The cosmological scenarios do not seem to make the thermodynamic asymmetries a result of nomic necessity. The cosmological hypotheses may be true, and in some sense, they may even explain the low-entropy initial state. But they do not appear to provide an explanation of the thermodynamic asymmetry that makes it nomologically necessary or even likely.

Another way to see the point is to consider the question of whether the thermodynamic arrow would “flip” if (say) the universe started to contract. Gold, as we said above, asserts that at the maximum radius the thermodynamic arrow must “flip” due to the re-contraction. Not positing a thermodynamic flip while maintaining that entropy values covary with the radius of the universe is clearly inconsistent – it is what Price (1996)[^price-1996] calls the fallacy of a “temporal double standard”. Gold does not commit this fallacy, and so he claims that the entropy must decrease if ever the universe started to re-contract. However, as Albert writes,

> there are plainly locations in the phase space of the world from which … the world’s radius will inexorably head up and the world’s entropy will inexorably head down. (2000: 90)

Since that is the case, it doesn’t follow from law that the thermodynamic arrow will flip during re-contraction; therefore, without changing the fundamental laws, the Gold mechanism cannot explain the thermodynamic arrow in the sense we want.

From these considerations we can understand the *basic dilemma* that runs throughout Price (1995, 1996)[^price-1995][^price-1996]: either we explain the earlier low-entropy condition Gold-style or it is inexplicable by time-symmetric physics. Because there is no net asymmetry in a Gold universe, we might paraphrase Price’s conclusion in a more disturbing manner as the claim that the (local) thermodynamic arrow is explicable just in case (globally) there isn’t one. However, notice that this remark leaves open the idea that the laws governing expansion or inflation are not time reversal invariant. (For more on Price’s basic dilemma, see Callender 1998 and Price 1995.)[^callender-1998][^price-1995]

Finally, it’s important to remember that this dilemma and the need for a Past Hypothesis are dependent upon a particular physical set-up. Can we explain the thermodynamic arrow without invoking a Past Hypothesis? Inspired by the idea of eternal spontaneous inflation, Carroll and Chen (2004, Other Internet Resources) describe a model in which new baby universes (or “pocket universes”) are repeatedly born from existing universes. Each birth increases the overall entropy of the multiverse although within each baby universe we have our familiar thermodynamic asymmetry. The crucial assumption in this model – one also found in the gravitational theory of Barbour, Koslowski, and Mercati (2014) – is that entropy is unbound. It can be arbitrarily high. With this assumption and in these models, one can do without a past Hypothesis. For discussion, see Goldstein, Tumulka, & Zanghi 2016 and Lazarovici and Reichert 2020.

### 3.4 Quantum Cosmology

Quantum cosmology, it is often said, is the *theory* of the universe’s initial conditions. Presumably this entails that its posits are to be regarded as lawlike. Because theories are typically understood as containing a set of laws, quantum cosmologists apparently assume that the distinction between laws and initial conditions is fluid. Particular initial conditions will be said to obtain as a matter of law. Hawking writes, for example,

> we shall not have a complete model of the universe until we can say more about the boundary conditions than that they must be whatever would produce what we observe, (1987: 163).

Combining such aspirations with the observation that thermodynamics requires special boundary conditions leads quite naturally to the thought that “the second law becomes a selection principle for the boundary conditions of the universe [for quantum cosmology]” (Laflamme 1994: 358)[^laflamme-1994]. In other words, if one is to have a theory of initial conditions, it would certainly be desirable to deduce initial conditions that will lead to the thermodynamic arrow. This is precisely what many quantum cosmologists have sought. For example, Hawking 1985 posits and quantum state of the universe that begins in a very smooth and homogeneous state and evolves to a less symmetric and more complicated later state. (This should be contrasted with the arrows of time discussed in semiclassical quantum gravity, for example, the idea that quantum scattering processes in systems with black holes violate the CPT theorem.) Although quantum cosmology is currently very speculative, there has been a substantial amount of debate on this issue (see Haliwell *et al*. 1994)[^haliwell-1994].

### 3.5 Causation

Penrose and Percival (1962) propose a general causal principle to handle our problem. The principle states that the effects of interactions happen *after* those interactions but not *before*. Similar to Reichenbach’s principle of the common cause, they suggest what they dub the Law of Conditional Independence, namely, that “If $A$ and $B$ are two disjoint 4-regions, and $C$ is any 4-region which divides the union of the pasts of $A$ and $B$ into two parts, one containing $A$ and the other containing $B$, then $A$ and $B$ are conditionally independent given $c$. That is, $\text{Pr}(a \mathbin{\&} b \mid c) = \text{Pr}(a\mid c) \times \text{Pr}(b\mid c)$, for all $a$,$b$.” (Penrose and Percival 1962, p. 611)[^penrose-1962]. Here $c$ is an event that is a common cause that screens off the correlation between events in $A$ and $B$.

In terms of statistical mechanics, this law would have the effect of making the phase space density associated with a system at a time determined by earlier events but not later events. This would more or less directly preclude the temporal “parity of reasoning” motivated transitions assumed in the problem of the direction of time, transition of type (2). To achieve this, the Law of Conditional Independence must be time asymmetric, which it is, and it must be a kind of fundamental principle that restricts the lawlike correlation otherwise allowed. After all, if we assume that the laws of nature are time reversal invariant, then there is no asymmetry between pre- and post-interaction correlations.

Price 1996 (chapter 5) and Sklar 1993 hold that this nomic restriction is unwarranted or unexplanatory. There is the sense that the causal asymmetry should come out of more basic physics, not be baked into this physics. Horwich 1987 is an example of someone trying to derive what he calls the fork asymmetry, which is similar to the Law of Conditional Independence, from more basic assumptions.

A recent contribution that has some affinities with the Penrose and Percival move can be found in Myrvold 2020.

### 3.6 Time Itself

Some philosophers have proposed solving the problem of time’s arrow by claiming that time *itself* is directed. The philosophers of interest do not adopt a so-called tensed or “A-theoretic” conception of time. These theories of time, such as presentism, becoming, and moving spotlight, all posit a distinguished present or now, one that is irreducible to the temporal or staiotemporal relations connecting events, e.g., earlier than (see Bardon 2024, Baron and Miller 2018, Callender 2011c, 2017)[^bardon-2024][^baron-2018][^callender-2011c][^callender-2017]. According to the tensed theory of time, time itself is truly temporally directed: the distinguished now updates itself in one direction and not the other. However, perhaps because the now doesn’t alter the qualitative properties of events, few if any have tried to extract an entropic gradient from the passage of the now. However, there have been some proposals firmly rooted in the idea that time and space are properly represented on a four-dimensional manifold. The main idea is that the various asymmetries in time indicate something about the nature of time itself. Christensen (1993)[^christensen-1993] argues that this is the most economical response to our problem since it posits nothing besides time as the common cause of the asymmetries, and we already believe in time.

A proposal similar to Christensen’s is Robert Weingard’s “time-ordering field” (1977). Earman (1974)[^earman-1974] discusses the heterodox idea that temporal orientability is important to explain the direction of time. A spacetime is time orientable, loosely put, if one can consistently “color” future lightcones (say) red and past lightcones (say) black. Weingard’s speculative thesis goes a step further than Earman by proposing the existence of a “time potential”, a timelike vector field that at every spacetime point directs a vector into its future light cone. In other words, supposing our spacetime is temporally orientable, Weingard wants to actually orient it. The main virtue of this is that it provides a time sense everywhere, even in spacetimes containing closed timelike curves (so long as they’re temporally orientable). One virtue of the idea is that it is in principle capable of explaining *all* the temporal asymmetries. If coupled to the various asymmetries in time, it would be the “master arrow” responsible for the arrows of interest. As Sklar (1985)[^sklar-1985] notes, Weingard’s proposal makes the past-future asymmetry very much like the up-down asymmetry. As the up-down asymmetry was reduced to the existence of a gravitational potential – and not an asymmetry of space itself – so the past-future asymmetry would reduce to the time potential – and not an asymmetry of time itself. Of course, if one thinks of the gravitational metric field as part of spacetime, there is a sense in which the reduction of the up-down asymmetry really was a reduction to a spacetime asymmetry. And if the metric field is conceived as part of spacetime – which is itself a huge source of contention in philosophy of physics – it is natural to regard Weingard’s time-ordering field as also part of spacetime. Thus his proposal shares a lot in common with Christensen’s suggestion.

Sklar criticizes this proposal on methodological grounds. He claims that scientists would not accept such an explanation (1985: 111–2). One might point out, however, that many scientists did believe in analogues of the time-ordering field as possible causes of the CP violations. Both the ‘super-weak’ and ‘milli-weak’ fields originally postulated to account for CP-violations are quite analogous in method to the postulation of the time-ordering field. See Sachs 1987: 236, and references therein. The time-ordering field, if it exists, would be an unseen (except through its effects) common cause of strikingly ubiquitous phenomena. Scientists routinely accept such explanations. To find a problem with the time-ordering field we need not invoke methodological scruples; instead we can simply ask whether it does the job asked of it. Is there a mechanism that will couple the time-ordering field to thermodynamic phenomena? Weingard says the time potential field needs to be suitably coupled (1977: 130) to the non-accidental asymmetric processes, but neither he nor Christensen elaborate on how this is to be accomplished. Until this is addressed satisfactorily, this speculative idea must be considered interesting yet embryonic. For more recent work in this vein, see Maudlin 2002.

### 3.7 Interventionism

When explaining time’s arrow many philosophers and physicists have focused their attention upon the unimpeachable fact that real systems are open systems that are subjected to interactions of various sorts. Thermodynamic systems cannot be truly isolated. To take the most obvious example, we can not shield a system from the influence of gravity. At best, we can move systems to locations feeling less and less gravitational force, but we can never completely decouple a system from the gravitational field. Not only do we ignore the gravitational force when doing classical thermodynamics, but we also ignore less exotic matters, such as the walls in the standard gas-in-a-box scenario. This idealization is usually justfied because the time it takes for a gas to reach equilibrium with itself is vastly shorter than the time it takes the gas+walls system to reach equilibrium. For this reason we typically discount the effects of the box walls on the gas.

Many have felt that the solution to the problem of the direction of time is buried in this idealization. Indeed, many have thought herein lies a solution that *does not* change the laws of classical mechanics and *does not* allow for the nomological possibility of anti-thermodynamic behavior. In other words, advocates of this view seem to believe it embodies a third way. Blatt 1959; Reichenbach 1956; Redhead and Ridderbos 1998, and to some extent, Horwich 1987 are a few works charmed by this idea.

The thoiught is to take advantage of what a random perturbation of the representative phase point would do to the evolution of a system. Given our Boltzmannian setup, there is a tremendous asymmetry in phase space between the volumes of points leading to equilibrium and of points leading away from equilibrium. If the representative point of a system were knocked about randomly, then due to this asymmetry, it would be very probable that the system at any given time be on a trajectory leading toward equilibrium. Thus, if it could be argued that the earlier treatment of the statistical mechanics of ideal systems ignored a random perturber in the environment of the system, then one would seem to have a solution to our problems. Even if the perturbation were weak it would still have the desired effect. The weak “random” previously ignored knocking of the environment is claimed to be the cause of the approach to equilibrium. *Prima facie*, this answer to the problem escapes the appeal to special initial conditions and the appeal to new laws.

But only *prima facie*. A number of criticisms have been leveled against this maneuver. One that seems on the mark is the observation that if classical mechanics is to be a universal theory, then the environment must be governed by the laws of classical mechanics as well. The environment is not some mechanism outside the governance of physical law, after all, and when we treat it too, the “deus ex machina” – the random perturber – disappears. If we treat the gas-plus-the-container walls as a classical system, it is still governed by time-reversible laws that will cause the same problem as we met with the gas alone. At this point one sometimes sees the response that this combined system of gas plus walls has a neglected environment too, and so on, and so on, until we get to the entire universe. It is then questioned whether we have a right to expect laws to apply universally (Reichenbach 1956: 81ff)[^reichenbach-1956]. Or the point is made that we cannot write down the Hamiltonian for all the interactions a real system suffers, and so there will always be something “outside” what is governed by the time-reversible Hamiltonian. Both of these points rely, one suspects, on an underlying instrumentalism about the laws of nature. Our problem only arises if we assume or pretend that the world literally is the way the theory says; dropping this assumption naturally “solves” the problem. Rather than further address these responses, let us turn to the claim that this maneuver need not modify the laws of classical mechanics.

If one does not make the radical proclamation that physical law does not govern the environment, then it is easy to see that whatever law describes the perturber’s behavior, it cannot be the laws of classical mechanics $if$ the environment is to do the job required of it. A time-reversal noninvariant law, in contrast to the time symmetric laws of classical mechanics, must govern the external perturber. Otherwise we can in principle subject the whole system, environment plus system of interest, to a Loschmidt reversal. The system’s velocities will reverse, as will the velocities of the millions of tiny perturbers. “Miraculously”, as if there were a conspiracy between the reversed system and the millions of “anti-perturbers”, the whole system will return to a time reverse of its original state. What is more, this reversal will be just as likely as the original process if the laws are time reversal invariant. A minimal criterion of adequacy, therefore, is that the random perturbers be time reversal *noninvariant*. But the laws of classical mechanics are time reversal invariant. Consequently, if this “solution” is to succeed, it must exercise new laws and modify or supplement classical mechanics. (Since the perturbations need to be genuinely random and not merely unpredictable, and since classical mechanics is deterministic, the same sort of argument could be run with indeterminism instead of irreversibility. See Price 2002 for a diagnosis of why people have made this mistake, and also for an argument objecting to interventionism for offering a “redundant” physical mechanism responsible for entropy increase.)

### 3.8 Quantum Mechanics

To the best of our knowledge our world is fundamentally quantum mechanical, not classical mechanical. Does this change the situation? “Maybe” is perhaps the best answer. Not surprisingly, answers to the question are affected by one’s interpretation of quantum mechanics. Quantum mechanics suffers from the notorious measurement problem, a problem demanding an interpretation of the quantum formalism. These interpretations either violate the unitary evolution of the quantum state (e.g., evolution according to the Schroedinger equation) or they do not. The former are dubbed “collapse” interpretations whereas the latter are known as “no-collapse” interpretations. Everettian “many worlds” and Bohmian mechnaics are examples of no-collapse theories, whereas the conventional Bohrian interpretation and Ghirardi, Rimini, and Weber (GRW) class of models are examples of collapse theories. This is not the place to go into the details of these interpretations, but we can still sketch the outlines of the picture painted by quantum mechanics (for more see Albert 1992, Barrett 2019)[^albert-1992][^barrett-2019].

Modulo some philosophical concerns about the meaning of time reversal (Albert 2000; Callender 2000; Earman 2002; Roberts 2022, Struyve 2022)[^albert-2000][^callender-2000][^earman-2002][^roberts-2022], the equation governing the unitary evolution of the quantum state is time reversal invariant. For interpretations that add something to quantum mechanics, such as Bohmian mechanics, this typically means that the resulting theory is time reversal invariant too (since it would be odd or even inconsistent to have one part of the theory invariant and the other part not). For other interpretations that leave the unitary evolution untouched, such as Everett, the theory is time reversal invariant. Since the resulting theory is time reversal invariant in either case, it is possible to generate the problem of the direction of time just as we did with classical mechanics. While many details are altered in the change from classical to no-collapse quantum mechanics, the logical geography remains the same (Chen 2018, 2020)[^chen-2018][^chen-2020].

Collapse interpretations are potentially more interesting with respect to our topic. Collapses interrupt or outright replace the unitary evolution of the quantum state. To date, they have always done so in a time reversal *non*invariant manner: there are collapses but no “uncollapses”. The resulting theory, therefore, is not time reversal invariant. This fact offers a potential escape from our problem: transitions of type (2) in our above statement of the problem may not be lawful. And this has led many thinkers throughout the century to believe that collapses somehow explain the thermodynamic time asymmetry.

Mostly these postulated methods fail to provide what we want. We think gases relax to equilibrium even when they’re not measured by Bohrian observers or Wignerian conscious beings. This complaint is, admittedly, not independent of more general complaints about the adequacy of these interpretations. But perhaps because of these controversial features they have not been pushed very far in explaining thermodynamics.

More satisfactory collapse theories exist, however. GRW, for example, can describe collapses in a closed system – no dubious appeal to observers outside the quantum system is required. Albert (1992, 2000)[^albert-1992][^albert-2000] has extensively investigated the impact GRW would have on statistical mechanics and thermodynamics. GRW would ground a temporally asymmetric probabilistic tendency for systems to evolve toward equilibrium. Anti-thermodynamic behavior is not impossible according to this theory. Instead it is tremendously unlikely. The innovation of the theory lies in the fact that although entropy is overwhelmingly likely to increase toward the future, it is not also overwhelmingly likely to increase toward the past (because there are no dynamic backwards transition probabilities provided by the theory). So the theory does not suffer from a problem of the direction of time as stated above.

This does not mean, however, that it removes the need for something like the Past Hypothesis. GRW is capable of explaining why, given a present nonequilibrium state, later states should have higher entropy; and it can do this without also implying that earlier states have higher entropy too. But it does not explain how the universe ever got into a nonequilibrium state in the first place. As indicated before, some are not sure *what* would explain this fact, if anything, or whether it’s something we should even aspire to explain. The principal virtue GRW would bring to the situation, Albert thinks, is that it would solve or bypass various troubles involving the nature of probabilities in statistical mechanics.

The same type of benefit, plus arguably others, come from a recent proposal by Chen (2020, 2024)[^chen-2020][^chen-2024]. Chen suggests that we adopt a position known as density matrix realism to help understand time’s arrow. Instead of regarding the wavefunction as the basic ontology of quantum theory, we take the quantum state to be represented by an impure density matrix. When we express the Past Hypothesis in terms of a density matrix, a number of virtues appear, including greater harmony between the probabilities of statistical mechanics and quantum mechanics. It may be that interpretations of quantum mechanics that are not like GRW can possess some of the same benefits that GRW brings.

More detailed discussion of the impact quantum mechanics has on our problem can be found in Albert 2000, 2015, North 2002, Price 2002. But if our superficial review is correct, we can say that quantum mechanics will not obviate our need for a Past Hypothesis though it may well solve at least one problem related to the direction of time.

### 3.9 Lawlike Initial Conditions?

Finally, let’s return to a point made in passing about the status of the Past Hypothesis. Without some new physics that eliminates or explains the Past Hypothesis, or some satisfactory “third way”, it seems we are left with a bald posit of special initial conditions. One can question whether there really is anything unsatisfactory about this (Sklar 1993; Callender 2004b)[^callender-2004b][^sklar-1993]. But perhaps we were wrong in the first place to think of the Past Hypothesis as a contingent boundary condition. The question “why these special initial conditions?” would be answered with “it’s physically impossible for them to be otherwise”, which is always a conversation stopper. Indeed, Feynman (1965: 116)[^feynman-1965] speaks this way when explaining the statistical version of the second law.

Absent a particular understanding of laws of nature, there is perhaps not much to say about the issue. But given particular conceptions of lawhood, it is clear that various judgments about this issue follow naturally – as we will see momentarily. However, let’s acknowledge that this may be to get matters backwards. It might be said that we *first* ought to find out whether the boundary conditions *are* lawlike, and *then* devise a theory of law appropriate to the answer. To decide whether or not the boundary conditions are lawlike based merely on current philosophical theories of law is to prejudge the issue. Perhaps this objection is really evidence of the feeling that settling the issue based on one’s conception of lawhood seems a bit unsatisfying. It is hard to deny this. Even so, it is illuminating to have a brief look at the relationships between some conceptions of lawhood and the topic of special initial conditions. For discussion and references on laws of nature, please refer to the entry on that topic.

For instance, if one agrees with John Stuart Mill that from the laws one should be able to deduce everything and one considers the thermodynamic part of that “everything”, then the special initial condition will be needed for such a deduction. The modern heir of this conception of lawhood, the one associated with Frank Ramsey and David Lewis (see Loewer 1996)[^loewer-1996], sees laws as the axioms of the simplest, most powerful, consistent deductive system possible. It is likely that the specification of a special initial condition would emerge as an axiom in such a system, for such a constraint may well make the laws much more powerful than they otherwise would be.

We should not expect the naïve regularity view of laws to follow suit, however. On this sort of account, roughly, if $B$s always follow $A$s, then it is a law of nature that $A$ causes $B$. To avoid finding laws everywhere, however, this account needs to assume that $A$s and $B$s are instantiated plenty of times. But the initial conditions occur only once.

For more robust realist conceptions of law, it’s difficult to predict whether the special initial conditions will emerge as lawlike. Necessitarian accounts like Pargetter’s (1984)[^pargetter-1984] maintain that it is a law that $P$ in our world iff $P$ obtains at every possible world joined to ours by a nomic accessibility relation. Without more specific information about the nature of the accessibility relations and the worlds to which we’re related, one can only guess whether all of the worlds relative to ours have the same special initial conditions. Nevertheless some realist theories offer apparently prohibitive criteria, so they are able to make negative judgments. For instance, “universalist” theories associated with David Armstrong say that laws are relations between universals. Yet a constraint on initial conditions isn’t in any natural way put in this form; hence it would seem the universalist theory would not consider this constraint lawlike.

Philosophical opinion is certainly divided. The problem is that a lawlike boundary condition lacks many of the features we ordinarily attribute to laws, e.g., multiple instances, governing temporal evolution, etc., yet different accounts of laws focus on different subsets of these features. See Chen 2023. When we turn to the issue at hand, what we find is the disagreement we expect.

## 4. The Problem of the Direction of Time II

Life is filled with temporal asymmetries. This directedness is one of the most general features of the world we inhabit. We can break this general tendency down into a few more specific temporal arrows.

1. The epistemological arrow. Roughly put, we know more about the past than the future. I know that yesterday’s broken egg on the floor had a similar outline to Chile’s boundaries, but I have no idea what country tomorrow’s broken egg will look like. Albert (2000)[^albert-2000] provides a much better characterization, for no one really counts and compares known propositions between past and future. It’s better to say, as he does, that our *way of knowing* the past is different than our way of knowing the future. There also seem to be more traces of events in the future than in the past. When I say something embarrassing, information representing that event is encoded on sound and light waves that form a continually increasing spherical shell in my future light-cone. I am potentially further embarrassed throughout my whole future lightcone. Yet there is no indication of the unfortunate event in its backward lightcone.
2. The mutability arrow. We feel the future is “open” or indeterminate in a way the past is not. The past is closed, fixed for all eternity. Related to this, no doubt, is the feeling that our actions are essentially tied to the future and not the past. The future is mutable whereas the past is not.
3. The psychological arrow. We have very different attitudes toward the past than toward the future. We dread future but not past headaches and prison sentences. This controversial arrow is actually many different asymmetries. Another, much disputed, is that we seem to share a psychological sense of passage through time. Allegedly, we sense a moving “now”, the motion of the present as events are transformed from future to past.
4. The explanation-causation-counterfactual arrow. This arrow is actually three, yet it seems plausible that there are connections among them. Causes typically occur *before* their effects. Related to the causal asymmetry in some fashion or other is the asymmetry of explanation. Usually good explanations appeal to events in the past of the event to be explained, not to events in the future. It may be that this is just a prejudice that we ought to dispense with, but it is an intuition that we frequently have. Finally, and no doubt this is again related to the other two arrows as well as the mutability arrow, we – at least naively – believe the future depends counterfactually on the present in a way that we do not believe the past depends counterfactually on the present.

The above list is not meant to be exhaustive or especially clean. Temporal asymmetries are everywhere. We age and die. Punchlines are at the ends of jokes. Propensities and dispositions and reproductive fitness are all future-directed. We prefer rags-to-riches stories to riches-to-rags stories. Obviously there are connections amongst many of these arrows. Some authors have explicitly or implicitly proposed various “dependency charts” that are supposed to explain which of the above arrows depend on which for their existence. Horwich (1987)[^horwich-1987] argues for an explanatory relationship wherein the counterfactual arrow depends on the causal arrow, which depends on the arrow of explanation, which depends on the epistemological arrow. Lewis (1979)[^lewis-1979], by contrast, thinks an alleged over-determination of traces grounds the asymmetry of counterfactuals and that this in turn grounds the rest. Suhler and Callender (2011) ground the psychological arrow on the causal and knowledge asymmetries. The chart one judges most appropriate will depend, to a large degree, upon one’s general philosophical stance on many large topics.

Which dependency chart is the correct one is not our concern here. Rather, the second “problem of the direction of time” asks: do any (all?) of these arrows ultimately hold in virtue of the thermodynamic arrow of time (or what grounds it)?

Sklar (1985)[^sklar-1985] provides useful examples to have in mind. Consider the up-down asymmetry. It plausibly reduces to the local gravitational gradient. Astronauts on the moon think down is the direction toward the center of the moon, not wherever it was when they left Earth. By contrast, there is (probably) merely a correlation between the left-right asymmetry (say, in snail shells) and parity violations in high-energy particle physics. The second problem asks whether any of the above temporal asymmetries are to the thermodynamic arrow as the up-down asymmetry is to the local gravitational gradient. Of course, we don’t expect anything quite so straightforward. Sklar describes an experiment where iron dust inserted in the ear sacs of fish cause the fish to swim upside down when a magnet is held over the tank, presumably altering their sense of up and down. But as Jos Uffink remarked to me, going inside a refrigerator doesn’t cause us to remember the future. The connections, if any, are bound to be subtle.

### 4.1 The Thermodynamic Reduction

Inspired by Boltzmann’s attempts in this regard, many philosophers have sought such reductions, either partial or total. Grünbaum (1973)[^grünbaum-1973] and Smart (1967)[^smart-1967] develop entropic accounts of the knowledge asymmetry. Lewis (1979)[^lewis-1979] suspects the asymmetry of traces is linked to the thermodynamic arrow but provides no specifics. Dowe (1992)[^dowe-1992], like a few others, ties the direction of causation to the entropy gradient. And some have also tied the psychological arrow to this gradient (for a discussion see Kroes 1985)[^kroes-1985]. Perhaps the most ambitious attempts at grounding many arrows all at once can be found in Reichenbach 1956, Horwich 1987, and Albert 2000, 2015. Each of these books offers possible thermodynamic explanations for the causal and epistemic arrows, as well as many subsidiary arrows.

A straightforward reduction of these arrows to entropy is probably not in the cards (Earman 1974; Horwich 1987)[^earman-1974][^horwich-1987]. Consider the epistemic arrow of time. The traditional entropic account claimed that because we know there are many more entropy-increasing rather than entropy-decreasing systems in the world (or our part of it), we can infer when we see a low-entropy system that it was preceded and caused by an interaction with something outside the system. To take the canonical example, imagine you are walking on the beach and come across a footprint in the sand. You can infer that earlier someone walked by (in contrast to it arising as a random fluctuation). In other words, you infer, due to its high order, that it was caused by something previously also of high (or higher) order, i.e, someone walking.

However, the entropic account faces some very severe challenges. First, do footprints on beaches have well-defined thermodynamic entropies? To describe the example we switched from low-entropy to high order, but the association between entropy and our ordinary concept of order is tenuous at best and usually completely misleading. (To appreciate this, just consider what happens to your salad dressing after it is left undisturbed. Order increases when the oil and vinegar separate, yet entropy has increased.) To describe the range of systems about which we have knowledge, the account needs something broader than the thermodynamic entropy. But what? Reichenbach is forced to move to a notion of quasi-entropy, losing the reduction in the process. Second, the entropic account doesn’t license the inference to a human being walking on the beach. All it tells you is that the grains of sand in the footprint interacted with its environment previously, which barely scratches the surface of our ability to tell detailed stories about what happened in the past. Third, even if we entertain a broader understanding of entropy, it still doesn’t always work. Consider Earman’s (1974)[^earman-1974] example of a bomb destroying a city. From the destruction we may infer that a bomb went off; yet the bombed city does not have lower entropy than its surroundings or even any type of intuitively higher order than its surroundings.

### 4.2 The Statistical Mechanical Reduction

Presumably for these reasons, contemporary theories abandon the attempt to ground the arrows of time on thermodynamic entropy. Instead, they turn to statistical mechanics, that which grounds the thermodynamic arrow. This more general basis is regarded as more fertile ground for the other arrows. In effect, the thermodynamic arrow is just regarded as another non-basic arrow like those four mention above. Horwich (1987)[^horwich-1987] traces the arrows back to initial micro-chaos. Albert (2000, 2015)[^albert-2000][^albert-2015] and Loewer (2012)[^loewer-2012] instead trace them to a package dubbed the *Mentaculus* (after the Coen brothers’ film, *A Serious Man*, 2009). Let’s briefly consider how Albert and Loewer propose to derive the thermodynamic arrow, the epistemic arrow, and the causal arrow all from the Mentaculus.

In the Coen brothers’ film, the character Arthur Gopnik, a mathematician, spends his days on a couch filling a notebook with a probability map of the universe, the Mentaculus. It is an apt name for what statistical mechanics provides us according to Albert and Loewer. In effect, it is a probability map for every macroscopic generalization. It assigns probabilities over all the microstates realizing any macrostate. The package is composed of the following elements: the past hypothesis (that the entropy of initial macrostate $M(0)$ is extremely low), a uniform probability distribution over the microstates that realize $M(0)$, the present macrostate $M(t)$, and the dynamical laws of the microlevel.

This package, they say, implies the thermodynamic arrow. We “derive” entropy (*S*) increase from basic physics by making a case at time $t$ that

$$\begin{align} P(S \text{ increases } &\mid M(t) \amp M(0) \amp \text{uniform-probability-over-}M(0)) \\ &= \text{high} \end{align}$$

Boltzmann, Gibbs and many others make the case, although it’s worth bearing in mind that they do so rigorously only in ideal cases and much remains controversial. Still, it strikes many as physically plausible. One could say a lot more, but let’s grant this. Then he first problem of the direction of time is blocked by the Past Hypothesis. One conditionalizes on the uniform distribution given $M(0)$ and $M(t)$, not merely $M(t)$. The constraint at one end of the universe makes the claim that ‘earlier entropy was higher’ unlikely. If correct, we have an honest-to-goodness reduction of a special science law “the second law of thermodynamics” from the bottom.

But this package also implies much more. The statistical mechanical probabilities cover *all* physical microstates, and therefore, they apply to all macrostates as well – so long as the macroscopic supervenes upon the microscopic – whether they are classical thermodynamic variables like pressure, temperature, and volume or not. One can replace “S increases” with any macroscopic generalization at all and the Mentaculus will yield a conditional probability. Not only is equilibrium thermodynamics “reduced” to statistical mechanics, but so – in principle – are all the special sciences, e.g., economics, biology, sociology. And amongst the generalizations reduced are a number of temporal asymmetries.

First, the explanation-causation-counterfactual arrow. As a very rough first approximation, causation can be analyzed probabilistically. Cause $C$ causes effect $E$ just in case $C$ is prior to $E$ and the probability of $E$ given $C$ and background $B$ is greater than the probability of $E$ given $B$ alone. Of course, there are serious problems with this account (see the entry on Probabilistic Causation). Yet the core intuition appears to come from the package, as one gets the temporal priority of causes from the Past Hypothesis and the probabilities from statistical mechanics. Together, they are claimed to explain why we can manipulate causes to produce effects but not vice versa. Loewer 2007 instead begins with counterfactuals and then gets causation from a counterfactual analysis and then explanation. Others, such as Ismael 2023, derive the causal asymmetry differently yet still connect it crucially to the statistical mechanical arrow.

Second, the epistemic arrow. Reflect on the nature of records. When you weigh yourself on a scale, it produces a record of one’s weight. This record is based on an inference comparing the states of the scale at two different times. I’m (say) 180 lbs if the scale was in its functioning ready state at 0 lbs before I stepped on it. The idea, very loosely (see Albert 2000, 2015 and Loewer 2012 for the details)[^albert-2000][^albert-2015][^loewer-2012] is that the Past Hypothesis effectively is the world’s Ready State. This very special state is what causes there to be macroscopic traces of the past in the present but not macroscopic traces of the future in the present.

The other two arrows mentioned above, mutability and the psychological, have not been discussed as extensively in this program. Some may regard the mutability arrow as connected to the explanation-causation-counterfactual arrow. Hemmo and Shenker (2022) argue that this program will not succeeed with the psychological arrow.

Naturally for a program this ambitious, its many claims have met with vigorous scrutiny. The idea that statistical mechanics implies (probabilistically) the truth or falsity of virtually every counterfactual-supporting generalization in all of science and everyday life strikes many as going too far. See Albert 2025, Callender and Cohen 2010, Earman 2006, Frisch 2010, Leeds 2003, North 2011, Westlake 2014, Winsberg 2004, Wilson 2014, and especially Loewer, Weslake, and Winsberg 2023.

Long ago Boltzmann (e.g., 1895) suggested that the temporal asymmetries discussed above are explained by the direction of increasing entropy. A lot of progress has been made developing this tantalizing thesis. Nevertheless, just as work on the first problem of the origins of the thermodynamic arrow remains active, so too does research on the second.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=time-thermo). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/time-thermo/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=time-thermo&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/time-thermo/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- Carroll, Sean M. and Jennifer Chen, 2004. “[Spontaneous Inflation and the Origin of the Arrow of Time](http://arxiv.org/abs/hep-th/0410270)”, manuscript at arVix.org. ArXiv: 0410270 [hep-th].
- Prunkl, Carina E. A., and Christopher G. Timpson, 2019, “[Black hole Entropy is Thermodynamic Entropy](https://arxiv.org/abs/1903.06276)”, arXiv preprint arXiv:1903.06276.
- [PhilSci Archive](http://philsci-archive.pitt.edu/) (University of Pittsburgh); contains a section containing papers in the foundations of thermodynamics and statistical mechanics. Many papers relevant to this entry are available.

## Related Entries

causation: probabilistic | consciousness: temporal | laws of nature | physics: intertheory relations in | probability, interpretations of | Reichenbach, Hans: common cause principle | statistical physics: Boltzmann’s work in | statistical physics: philosophy of statistical mechanics

[^albert-1992]: Albert, David Z., 1992, *Quantum Mechanics and Experience*, Cambridge, MA: Harvard University Press.

[^albert-2000]: –––, 2000, *Time and Chance*, Cambridge, MA: Harvard University Press.

[^albert-2015]: –––, 2015, *After Physics*, Cambridge, MA: Harvard University Press.

[^albert-2025]: –––, 2025, “The Direction of Time: From the Cosmos to Local Systems” in C. López and O. Lombardi (eds.), *The Arrow of Time: From Local Systems to the Whole Universe*, Cambridge: Cambridge University Press, 3–11

[^allori-2015]: Allori, Valia, 2015, “Maxwell’s Paradox: Classical Electrodynamics and its Time Reversal Invariance”, *Analytica*, 1: 1–19.

[^allori-2020]: –––, 2020, *Statistical Mechanics and Scientific Explanation: Determinism, Indeterminism and Laws of Nature*, Singapore: World Scientific. doi:10.1142/11591

[^allori-2025]: –––, 2025, “Time for Pancakes”, in O. Lombardi and C. Lopez (eds), *The Arrow of Time: From Closed Systems to the Whole Universe*. Cambridge: Cambridge University Press.

[^arntzenius-1994]: Arntzenius, Frank, 1994, “The Classical Failure to Account for Electromagnetic Arrows of Time”, in Tamara Horowitz & Alan Ira Janis (eds.), *Scientific Failure*, Lanham: Rowman & Littlefield, pp. 29–48.

[^atkinson-2006]: Atkinson, David, 2006, “Does Quantum Electrodynamics Have an Arrow of Time?”, *Studies in the History and Philosophy of Modern Physics*, 37(3): 528–541. doi:10.1016/j.shpsb.2005.03.003

[^barbour-2014]: Barbour, J., Koslowski, T. and Mercati, F., 2014, “Identification of a Gravitational Arrow of Time”, *Physical Review Letters*, 113: 181101.

[^baras-2020]: Baras, Dan and Shenker, Orly, 2020, “Calling for Explanation: the Case of the Thermodynamic Past State”, *European Journal for the Philosophy of Science*, 10: article 36. doi:10.1007/s13194-020-00297-7

[^bardon-2024]: Bardon, Adrian, 2024, *A Brief History of the Philosophy of Time*, second edition, Oxford: Oxford University Press.

[^baron-2018]: Baron, Sam, and Miller, Kristie, 2018, *An Introduction to the Philosophy of Time*, Cambridge: Polity Press.

[^barrett-2019]: Barrett, Jeffrey, 2019, *The Conceptual Foundations of Quantum Mechanics*, Oxford: Oxford University Press.

[^besson-2012]: Besson, Ugo, 2012, “The History of the Cooling Law: When the Search for Simplicity can be an Obstacle”, *Science & Education* 21, 1085–1110. doi:10.1007/s11191-010-9324-1

[^blatt-1959]: Blatt, J.M., 1959, “An Alternative Approach to the Ergodic Problem”, *Progress in Theoretical Physics*, 22(6): 745. doi:10.1143/PTP.22.745

[^boltzmann-1895]: Boltzmann, Ludwig, 1895, “On Certain Questions of the Theory of Gases”, *Nature*, 51: 413–15.

[^bricmont-1995]: Bricmont, Jean, 1995, “Science of Chaos or Chaos in Science?”, *Physicalia Magazine*, 17(3–4): 159–208.

[^brown-2009]: Brown, Harvey R., Wayne Myrvold, and Jos Uffink, 2009, “Boltzmann’s $H$-Theorem, Its Discontents, and the Birth of Statistical Mechanics”, *Studies in the History and Philosophy of Science*, 40(2): 174–191. doi:10.1016/j.shpsb.2009.03.003

[^brown-2001]: Brown, Harvey R. and Jos Uffink, 2001, “The Origins of Time-Asymmetry in Thermodynamics: The Minus First Law”, *Studies in the History and Philosophy of Modern Physics*, 32(4): 525–538. doi:10.1016/S1355-2198(01)00021-1

[^brush-1976]: Brush, S.G., 1976, *The Kind of Motion We Call Heat*, Amsterdam: North Holland.

[^callender-1997]: Callender, Craig, 1997, “What is ‘The Problem of the Direction of Time’?”, *Philosophy of Science*, 64: S223–34. doi:10.1086/392602

[^callender-1998]: –––, 1998, “The View From No-when”, *British Journal for the Philosophy of Science*, 49(135): 135–159. doi:10.1093/bjps/49.1.135

[^callender-1999]: –––, 1999, “Reducing Thermodynamics to Statistical Mechanics: The Case of Entropy”, *Journal of Philosophy*, 96(7): 348–373. doi:10.5840/jphil199996733

[^callender-2000]: –––, 2000, “Is Time ‘Handed’in a Quantum World?” *Proceedings of the Aristotelian Society*, 100(1): 247–269. Oxford, UK and Boston, USA: Blackwell Science Ltd.

[^callender-2004a]: –––, 2004a, “There is No Puzzle about the Low Entropy Past”, in Christopher Hitchcock (ed.), *Contemporary Debates in the Philosophy of Science*, Oxford: Blackwell, 240–256.

[^callender-2004b]: –––, 2004b, “Measures, Explanation and the Past: Should ‘Special’ Initial Conditions Be Explained?”, *British Journal for the Philosophy of Science*, 55(2): 195–217. doi:10.1093/bjps/55.2.195

[^callender-2010]: –––, 2010, “The Past Hypothesis Meets Gravity”, in Gerhard Ernst and Andreas Hüttemann (eds), *Time, Chance and Reduction*, Cambridge: Cambridge University Press, pp. 34–58.

[^callender-2011a]: –––, 2011a, “Hot and Heavy Matters in the Foundations of Statistical Mechanics”, *Foundations of Physics*, 41(6): 960–981. doi:10.1007/s10701-010-9518-z

[^callender-2011b]: –––, 2011b, “The Past Histories of Molecules”, in Claus Beisbart & Stephan Hartmann (eds.), *Probabilities in Physics*, Oxford: Oxford University Press, pp. 83–113. doi:10.1093/acprof:oso/9780199577439.003.0004

[^callender-2011c]: –––, 2011c, *The Oxford Handbook of Philosophy of Time*, Oxford: Oxford University Press.

[^callender-2017]: –––, 2017, *What Makes Time Special?* Oxford University Press.

[^callender-2025]: –––, 2025, “Insights into Quantum Time Reversal from the Classical Schrödinger Equation”, in C. López, O. Lombardi (eds.), *The Arrow of Time: From Local Systems to the Whole Universe*. Cambridge University Press, 184–197.

[^carathéodory-1909]: Carathéodory, Constantin, 1909, “Untersuchungen über die Grundlagen der Thermodynamik”, *Mathematische Annalen*, 67(3): 355–386 doi:10.1007/BF01450409

[^cardwell-1971]: Cardwell D.S.L. 1971, *From Watt to Clausius: The Rise of Thermodynamics in the Early Industrial Age*, Ithaca, NY: Cornell University Press.

[^carnot-1824]: Carnot, Sadi, 1824, *Réflexions sur la puissance motrice du feu et sur les machines propres à développer cette puissance*, Paris: Chez Bachelier, Libraire; translated as *Reflections on the Motive Power of Heat*, R.H. Thurston (trans.), New York: Wiley & Sons, 1897.

[^chang-2004]: Chang, Hasok, 2004, *Inventing Temperature*. Oxford: Oxford University Press.

[^chen-2018]: Chen, Eddy Keming, “Quantum Mechanics in a Time-Asymmetric Universe: On the Nature of the Initial Quantum State”, *The British Journal for the Philosophy of Science*, first online 13 October 2018. doi:10.1093/bjps/axy068

[^chen-2020]: –––, 2020, “Time’s Arrow in a Quantum Universe: On the Status of Statistical Mechanical Probabilities”, in Valia Allori (ed.), *Statistical Mechanics and Scientific Explanation: Determinism, Indeterminism and Laws of Nature*, World Scientific.

[^chen-2023]: –––, 2023, “The Past Hypothesis and the Nature of Physical Laws”, in Barry Loewer, Eric Winsberg, and Brad Weslake (eds.), The Probability Map of the Universe: Essays on David Albert’s Time and Chance, Harvard University Press.

[^chen-2024]: –––, 2024, “The Wentaculus: Density Matrix Realism Meets the Arrow of Time”, in A. Bassi, S. Goldstein, R. Tumulka, N. Zanghì (eds), *Physics and the Nature of Reality*, Fundamental Theories of Physics 215, Berlin: Springer, pp. 87–104. doi:10.1007/978-3-031-45434-9_8

[^christensen-1993]: Christensen, F.M., 1993, *Space-like Time: Consequences Of, Alternatives To, and Arguments Regarding the Theory That Time Is Like Space*, Toronto: University of Toronto Press.

[^chua-2023]: Chua, Eugene Y.S., 2023, “T Falls Apart: On the Status of Classical Temperature in Relativity”, *Philosophy of Science*, 90(5): 1307–19. doi:10.1017/psa.2023.27

[^chua-2026]: –––, 2026, “Looking for Work in Quantum Thermodynamics”, *British Journal for the Philosophy of Science*, forthcoming. doi:10.1086/740608

[^chua-2026-2]: Chua, Eugene Y.S. and Callender, Craig, 2026, “The Toll of the Tolman Effect: On the Status of Classical Temperature in General Relativity”, *British Journal for the Philosophy of Science*, forthcoming.

[^clausius-1851]: Clausius, Rudolf, “On the moving force of heat and the laws of heat which may be deduced there from”, *Poggendorf’s Annalen*, 185(79): 368–369. Translated in 1851, *Phil. Mag.*, Series 4, Vol. 2(8): 1–21.

[^time-thermo-1854]: 1854, “Ueber eine veränderte Form des zweiten Hauptsatzes der mechanischen Wärmetheorie”, *Annalen der Physik und Chemie*, 93(12): 481–506. doi:10.1002/andp.18541691202

[^time-thermo-1865]: –––, 1865, “Ueber verschiedene für die Anwendung bequeme Formen der Hauptgleichungen der mechanischen Wärmetheorie”, *Annalen der Physik und Chemie*, 201(7): 353–400. doi:10.1002/andp.18652010702

[^cocke-1967]: Cocke, W.J., 1967, “Statistical Time Symmetry and Two-Time Boundary Conditions in Physics and Cosmology”, *Physical Review*, 160(5): 1165–70. doi:10.1103/PhysRev.160.1165

[^cohen-2010]: Cohen, Jonathan and Craig Callender, 2010, “Special Sciences, Conspiracy and the Better Best System Account of Lawhood”, *Erkenntnis*, 73(3): 427–447. doi:10.1007/s10670-010-9241-3

[^davies-1994]: Davies, P.C.W., 1994, “Stirring Up Trouble”, in Haliwell *et al.* 1994: 119–30.

[^da-1906]: Da Vinci, Leonardo, 1496, South Kensington Museum MS ii p. 92 McCurdy, Edward (1906). *Leonardo da Vinci’s Note-books*. US: Charles Scribner’s Sons. p. 64.

[^dougherty-2026]: Dougherty, John and Callender, Craig, 2026, “Black Hole Thermodynamics: More Than an Analogy?”, forthcoming in Baptiste Le Bihan and Christian Wüthrich (eds.), *Metaphysics Beyond Spacetime: Essays on the Metaphysics of Quantum Gravity*, New York: Routledge. [[Dougherty and Callender 2026 available online](https://philsci-archive.pitt.edu/13195/1/bht.pdf)]

[^dowe-1992]: Dowe, Phil, 1992, “Process Causality and Asymmetry”, *Erkenntnis*, 37(2): 179–196. doi:10.1007/BF00209321

[^earman-1969]: Earman, John, 1969, “The Anisotropy of Time”, *Australasian Journal of Philosophy*, 47(3): 273–295. doi:10.1080/00048406912341281

[^earman-1974]: –––, 1974, “An Attempt to Add a Little Direction to ‘The Problem of the Direction of Time’”, *Philosophy of Science*, 41(1): 15–47. doi:10.1086/288568

[^earman-1978]: –––, 1978, “Combining Statistical-Thermodynamics and Relativity Theory: Methodological and Foundations Problems”, in Peter D. Asquith and Ian Hacking (eds), *Proceedings of the 1978 Biennial Meeting of the Philosophy of Science Association*, 2: 157–185

[^earman-2002]: –––, 2002, “What Time Reversal Invariance Is and Why It Matters”, *International Journal for the Philosophy of Science*, 16: 245–264.

[^earman-2006]: –––, 2006, “The ‘Past Hypothesis’: Not Even False”, *Studies in History and Philosophy of Modern Physics*, 37(3): 399–430. doi:10.1016/j.shpsb.2006.03.002

[^earman-2011]: –––, 2011, “Sharpening the Electromagnetic Arrow(s) of Time”, in Callender 2011c: 485–527. doi:10.1093/oxfordhb/9780199298204.003.0017

[^fermi-1936]: Fermi, Enrico, 1936, *Thermodynamics*, New York: Dover.

[^feynman-1965]: Feynman, Richard, 1965, *The Character of Physical Law*, Cambridge, MA: MIT Press.

[^frigg-2008]: Frigg, Roman, 2008, “A Field Guide to Recent Work on the Foundations of Statistical Mechanics”, in Dean Rickles, ed., *The Ashgate Companion to Contemporary Philosophy of Physics*, London: Ashgate, pp. 99–196.

[^frigg-2009]: –––, 2009, “Typicality and the Approach to Equilibrium in Boltzmannian Statistical Mechanics”, *Philosophy of Science*, 76(5): 997–1008. doi:10.1086/605800

[^frigg-2011]: Frigg, Roman and Charlotte Werndl, 2011, “Entropy: A Guide for the Perplexed”, in Claus Beisbart and Stephan Hartmann (eds.), *Probability in Physics*, Oxford: Oxford University Press, 115–142.

[^frisch-2000]: Frisch, Mathias, 2000, “(Dis-)solving the Puzzle of the Arrow of Radiation” *British Journal for the Philosophy of Science*, 51(3): 381–410. doi:10.1093/bjps/51.3.381

[^frisch-2006]: –––, 2006, “A Tale of Two Arrows”, *Studies in History and Philosophy of Modern Physics*, 37(3): 542–558. doi:10.1016/j.shpsb.2005.03.004

[^frisch-2010]: –––, 2010, “Does a Low-Entropy Constraint Prevent Us from Influencing the Past?” in Andreas Hüttemann and Gerhard Ernst (eds.), *Time, Chance, and Reduction: Philosophical Aspects of Statistical Mechanics*, Cambridge: Cambridge University Press, 13–33.

[^frisch-2016]: Frisch, Mathias and Wolfgang Pietsch, 2016, “Reassessing the Ritz–Einstein Debate on the Radiation Asymmetry in Classical Electrodynamics”, *Studies in History and Philosophy of Modern Physics*, 55: 13–23. doi:10.1016/j.shpsb.2016.05.001

[^gold-1962]: Gold, T., 1962, “The Arrow of Time”, *American Journal of Physics*, 30: 403–10. doi:10.1119/1.1942052

[^goldstein-2001]: Goldstein, Sheldon, 2001, “Boltzmann’s Approach to Statistical Mechanics”, in J. Bricmont, D. Dürr, M.C. Galavotti, G. Ghirardi, F. Petruccione, and N. Zanghi (eds), *Chance in Physics: Foundations and Perspectives* (Lecture Notes in Physics 574), Berlin: Springer-Verlag.

[^goldstein-2016]: Goldstein, Sheldon, Roderick Tumulka, and Nino Zanghì, 2016, “Is the Hypothesis About a Low Entropy Initial State of the Universe Necessary for Explaining the Arrow of Time?” *Physical Review D*, 94(2): 023520. doi:10.1103/PhysRevD.94.023520

[^goldstein-2020]: Goldstein, Sheldon, Lebowitz, Joel, Roderick Tumulka, and Nino Zanghì, 2020, “Gibbs and Boltzmann Entropy in Classical and Quantum Mechanics” in Allori, Valia (ed.), *Statistical Mechanics and Scientific Explanation: Determinism, Indeterminism and Laws of Nature*, Singapore: World Scientific.

[^grünbaum-1973]: Grünbaum, Adolf, 1973, *Philosophical Problems of Space and Time*, New York: Knopf.

[^haliwell-1994]: Haliwell, J.J., J. Pérez-Mercader, and W.H. Zurek (eds.), 1994, *Physical Origins of Time Asymmetry*, Cambridge: Cambridge University Press.

[^hawking-1985]: Hawking, Stephen, 1985, “Arrow of Time in Cosmology” *Physical Review D*, 32, 2489. doi:10.1103/PhysRevD.32.2489

[^hawking-1987]: Hawking, Stephen, 1987, “The Boundary Conditions of the Universe” in L.-Z. Fang and R. Ruffini (eds.), *Quantum Cosmology*, Teaneck, NJ: World Scientific, pp. 162–174.

[^healey-1981]: Healey, Richard, 1981, “Statistical Theories, QM and the Directedness of Time”, in Richard Healey (ed.), *Reduction, Time and Reality: Studies in the Philosophy of the Natural Sciences*, Cambridge: Cambridge University Press.

[^hemmo-2012]: Hemmo, Meir and Orly R. Shenker, 2012, *The Road to Maxwell’s Demon: Conceptual Foundations of Statistical Mechanics*, New York: Cambridge University Press.

[^hemmo-2022]: –––, 2022, “The Second Law of Thermodynamics and the Psychological Arrow of Time”, *The British Journal for the Philosophy of Science* 73(1),

[^horwich-1987]: Horwich, Paul, 1987, *Asymmetries in Time: Problems in the Philosophy of Science*, Cambridge, MA: MIT Press.

[^hubert-2023]: Hubert, Mario and Sebens, Charles, 2023, “Absorbing the Arrow of Electromagnetic Radiation”, *Studies in the History and Philosophy of Science*, 99: 10–27.

[^hurley-1986]: Hurley, James, 1986, “The Time-asymmetry Paradox”, *American Journal of Physics*, 54(1): 25–28. doi:10.1119/1.14764

[^ismael-2023]: Ismael, Jenann, 2023, “Reflections on the Asymmetry of Causation”, *Interface* *Focus* 13 (3): 20220081. doi:10.1098/rsfs.2022.0081

[^klein-1973]: Klein, M.J., 1973, “The Development of Boltzmann’s Statistical Ideas” in E.G.D. Cohen and W. Thirring (eds.), *The Boltzmann Equation: Theory and Applications*, Vienna: Springer, pp. 53–106.

[^kroes-1985]: Kroes, Peter, 1985, *Time: Its Structure and Role in Physical Theories*, Boston: D. Reidel.

[^laflamme-1994]: Laflamme, R., 1994, “The Arrow of Time and the No-boundary Proposal” in Haliwell *et al.* 1994: 358–68.

[^lavis-2005]: Lavis, D.A., 2005, “Boltzmann and Gibbs: An Attempted Reconciliation”, *Studies in the History and Philosophy of Modern Physics*, 36(2): 245–273. doi:10.1016/j.shpsb.2004.11.007

[^lazarovici-2020]: Lazarovici, Dustin and Reichert, Paula, 2020, “Arrow(s) of Time without a Past Hypothesis”, in Valia Allori (ed.), *Statistical Mechanics and Scientific Explanation: Determinism, Indeterminism and Laws of Nature*, Singapore: World Scientific, pp. 343–386. doi:10.1142/9789811211720_0010

[^lebowitz-1993a]: Lebowitz, Joel L., 1993a, “Boltzmann’s Entropy and Time’s Arrow”, *Physics Today*, 46(9): 32–38. doi:10.1063/1.881363

[^lebowitz-1993b]: Lebowitz, J. 1993b. “Macroscopic Laws, Microscopic Dynamics, Time’s Arrow and Boltzmann’s Entropy.” *Physica A* 194. 1-27.

[^leeds-2003]: Leeds, Stephen, 2003, “Foundations of Statistical Mechanics: Two Approaches”, *Philosophy of Science*, 70(1): 126–144. doi:10.1086/367873

[^lewis-1979]: Lewis, David, 1979, “Counterfactual Dependence and Time’s Arrow”, *Noûs*, 13(4): 455–76. doi:10.2307/2215339

[^lieb-2000]: Lieb, Elliot H. and Jakob Yngvason, 2000, “A Fresh Look at Entropy and the Second Law of Thermodynamics”, *Physics Today*, 53(4): 32–37. doi:10.1063/1.883034

[^liu-1994]: Liu, Chuang, 1994, “Is There a Relativistic Thermodynamics? A Case Study of the Meaning of Special Relativity”, *Studies in the History and Philosophy of Modern Physics*, 25: 983–1004. doi:10.1016/0039-3681(94)90073-6

[^loewer-1996]: Loewer, Barry, 1996, “Humean Supervenience” *Philosophical Topics*, 24(1): 101–127. doi:10.5840/philtopics199624112

[^loewer-2007]: –––, 2007. “Counterfactuals and the Second Law”, in Price, H. and Corry, R. (eds.) Causation, Physics, and the Constitution of Reality. Russell’s Republic Revisited Oxford: Oxford University Press.

[^loewer-2012]: –––, 2012, “The Emergence of Time’s Arrows and Special Science Laws from Physics”, *Interface Focus*, 2(1): 13–19. doi:10.1098/rsfs.2011.0072

[^loewer-2023]: Loewer, Barry, Weslake, Brad, and Winsberg, Eric, 2023, *The Probability Map of the Universe: Essays on David Albert’s Time and Chance*, Cambridge: Harvard University Press.

[^lópez-2025]: López C., and O. Lombardi (eds.), 2025, *The Arrow of Time: From Local Systems to the Whole Universe*, Cambridge: Cambridge University Press.

[^lorenzetti-2025]: Lorenzetti, Lorenzo, 2025, “Making Sense of Gravitational Thermodynamics”, *Philosophy of Physics*, 3(1): 5, 1–29. doi:10.31389/pop.120

[^loschmidt-1876]: Loschmidt, J., 1876/1877, “Über die Zustand des Wärmegleichgewichtes eines Systems von Körpern mit Rücksicht auf die Schwerkraft”, *Wiener Berichte*, 73: 128, 366 (1876); 75: 287; 76: 209 (1877).

[^maudlin-2002]: Maudlin, Tim, 2002, “Remarks on the Passing of Time”, *Proceedings of the Aristotelian Society*, 102(1): 259–274. doi:10.1111/j.0066-7372.2003.00053.x

[^mendoza-1961]: Mendoza, E., 1961, “A Sketch for a History of Early Thermodynamics”, *Physics Today*, 2: 32–42.

[^müller-2006]: Müller I., 2006, *A History of Thermodynamics.* Springer; Berlin, Germany.

[^myrvold-2020]: Myrvold, Wayne, 2020, “Explaining Thermodynamics: What Remains to be Done?” in Valia Allori (ed.), *Statistical Mechanics and Scientific Explanation: Determinism, Indeterminism and Laws of Nature*, Singapore: World Scientific, pp. 113–143. doi:10.1142/9789811211720_0004

[^myrvold-2021]: –––, 2021, *Beyond Chance and Credence: A Theory of Hybrid Probabilities*, Oxford: Oxford University Press.

[^nernst-1966]: Nernst, Werner, 1966, “Nobel Lecture,” in *Nobel Lectures, Chemistry 1901–1921*, Elsevier, Amsterdam.

[^newton-1701]: Newton, Isaac, 1701, “Scala graduum caloris, Calorum descriptiones & signa (Scale of the degrees of heat)”, *Philosophical Transactions*, 22(270): 824–829. English translation in: Newton, I. (1809). *Philosophical Transactions Royal Society of London, Abridged*, 4: 572–575.

[^north-2002]: North, Jill, 2002, “What is the Problem about the Time-Asymmetry of Thermodynamics? A Reply to Price”, *British Journal for the Philosophy of Science*, 53(1): 121–136. doi:10.1093/bjps/53.1.121

[^north-2003]: –––, 2003, “Understanding the Time-Asymmetry of Radiation”, *Philosophy of Science* 70(5, proceedings): 1086–1097.doi:10.1086/377391

[^north-2011]: –––, 2011, “Time in Thermodynamics”, in Callender 2011c: 312–352. doi:10.1093/oxfordhb/9780199298204.003.0011

[^norton-2016]: Norton, John D, 2016, The Impossible Process: Thermodynamic Reversibility, *Studies in History and Philosophy of Modern Physics*, 55: 43–61.

[^pargetter-1984]: Pargetter, R., 1984, “Laws and Modal Realism”, *Philosophical Studies*, 46: 335–347.

[^penrose-1970]: Penrose, Oliver, 1970, *Foundations of Statistical Mechanics*, New York: Pergamon Press.

[^penrose-1962]: Penrose, Oliver and I.C. Percival, 1962, “The Direction of Time”, *Proceedings of the Physical Society*, 79(3): 605–615. doi:10.1088/0370-1328/79/3/318

[^penrose-1989]: Penrose, Roger, 1989, *The Emperor’s New Mind: Concerning Computers, Minds and The Laws of Physics*, Oxford: Oxford University Press.

[^pippard-1964]: Pippard, A.B., 1964, *The Elements of Classical Thermodynamics*, Cambridge: Cambridge University Press.

[^popper-1956]: Popper, Karl R., 1956, “The Arrow of Time”, *Nature*, 177 (March 17): 538. doi:10.1038/177538a0

[^price-1995]: Price, Huw, 1995, “Cosmology, Time’s Arrow, and That Old Double Standard”, in Savitt 1995: 66–94.

[^price-1996]: –––, 1996, *Time’s Arrow and Archimedes’ Point: New Directions for the Physics of Time*, New York: Oxford University Press. [[Price 1996 table of contents and chapter 1 available online](http://www.usyd.edu.au/time/price/TAAP.html)]

[^price-2002]: –––, 2002, “Burbury’s Last Case: The Mystery of the Entropic Arrow”, in Craig Callender (ed.), *Time, Reality and Experience*, Royal Institute of Philosophy Supplements, 50: 19–56, Cambridge: Cambridge University Press. doi:10.1017/S1358246100010493

[^price-2004]: –––, 2004, “On the Origins of the Arrow of Time: Why There is Still a Puzzle about the Low-Entropy Past”, in Christopher Hitchcock (ed.), *Contemporary Debates in the Philosophy of Science*, Oxford: Blackwell, 219–232.

[^price-2006]: –––, 2006, “Recent Work on the Arrow of Radiation”, *Studies in History and Philosophy of Science Part B: Studies in History and Philosophy of Modern Physics*, 37(3): 498–527. doi:10.1016/j.shpsb.2006.03.004

[^psillos-1994]: Psillos, Stathis, 1994, “A Philosophical Study of the Transition from the Caloric Theory of Heat to Thermodynamics”, *Studies in the History and Philosophy of Science*, 25(2): 159–90. doi:10.1016/0039-3681(94)90026-4

[^reichenbach-1956]: Reichenbach, Hans, 1956, *The Direction of Time*, Maria Reichenbach (ed.), Berkeley: University of California Press.

[^redhead-1998]: Redhead, Michael L.G. and Ridderbos, T.M., 1998, “The Spin-Echo Experiments and the Second Law of Thermodynamics”, *Foundations of Physics*, 28(8): 1237–1270. doi:10.1023/A:1018870725369

[^ritz-1909]: Ritz, Walter and Albert Einstein, 1909, “Zum gegenwärtigen Stand des Strahlungsproblems (On the Current State of the Radiation Problem)”, *Physikalische Zeitschrift*, 10: 323–324.

[^roberts-2022]: Roberts, Bryan, 2022, *Reversing the Arrow of Time*, Cambridge: Cambridge University Press.

[^roberts-2026]: –––, 2026, “Does Thermodynamics Have a Reversibility Problem?” *Mind*, fzag008. doi:10.1093/mind/fzag008 [[Roberts 2026 available online](https://philsci-archive.pitt.edu/22288/1/2023-07-04-reversibilityproblem.pdf)]

[^robertson-2019]: Robertson, Katie, 2019, “Stars and Steam Engines: To What Extent Do Thermodynamics and Statistical Mechanics Apply to Self-gravitating Systems?”, *Synthese*, 196: 1783–1808.

[^robertson-2022]: –––, 2022, “In Search of the Holy Grail: How to Reduce the Second Law of Thermodynamics”, *British Journal for the Philosophy of Science*, 73(4): 987–1020.

[^rohrlich-2006]: Rohrlich, Fritz, 2006, “Time in Classical Electrodynamics”, *American Journal of Physics*, 74(4): 313–315. doi:10.1119/1.2178847

[^sachs-1987]: Sachs, Robert G., 1987, *The Physics of Time Reversal*, Chicago: University of Chicago Press.

[^saha-1935]: Saha, M.N. and Srivastava, B.N., 1935, *A Treatise on Heat*, Allahabad and Calcutta: The Indian Press. (Including Kinetic Theory of Gases, Thermodynamics and Recent Advances in Statistical Thermodynamics) (The second and revised edition of *A Text Book of Heat*.)

[^sanford-1984]: Sanford, David H., 1984, “The Direction of Causation and the Direction of Time”, in P. French, *et al*. (eds.), *Midwest Studies in Philosophy IX*, Minneapolis: University of Minnesota Press, 53–75. doi:10.1111/j.1475-4975.1984.tb00052.x

[^santiago-2019]: Santiago, Jessica. and Visser, Matthew, 2019, “Tolman Temperature Gradients in a Gravitational Field”, *European Journal of Physics*, 40, 025604. doi:10.1088/1361-6404/aaff1c

[^saslow-2020]: Saslow, W.M, 2020, “A History of Thermodynamics: The Missing Manual”, *Entropy* (Basel), 22(1), 77. doi:10.3390/e22010077

[^savitt-1995]: Savitt, Steven F. (ed.), 1995, *Time’s Arrow Today: Recent Physical and Philosophical Work on the Direction of Time*, Cambridge: Cambridge University Press.

[^savitt-1996]: –––, 1996, “Survey Article: The Direction of Time”, *British Journal for the Philosophy of Science*, 47(3): 347–370. doi:10.1093/bjps/47.3.347

[^schulman-1997]: Schulman, L.S., 1997, *Time’s Arrows and Quantum Measurement*, New York: Cambridge University Press.

[^sklar-1985]: Sklar, Lawrence, 1985, *Philosophy and Spacetime Physics*, Berkeley: University of California Press.

[^sklar-1993]: –––, 1993, *Physics and Chance: Philosophical Issues in the Foundations of Statistical Mechanics*, Cambridge: Cambridge University Press.

[^smart-1967]: Smart, J.J.C., 1967, “Time” in *Encyclopedia of Philosophy*, Paul Edwards (ed.), New York: Macmillan.

[^sommerfeld-1951]: Sommerfeld, A. 1951/1955. “Thermodynamics and Statistical Mechanics”, vol. 5 of *Lectures on Theoretical Physics*, edited by F. Bopp, J. Meixner, translated by J. Kestin, Academic Press, New York.

[^struyve-2025]: Struyve, Ward, 2025, “Time-reversal Invariance and Ontology”, *British Journal for the Philosophy of Science* 76(3). doi:10.1086/721089

[^suhler-2012]: Suhler, Christopher and Craig Callender, 2012, “Thank Goodness that Argument is Over: Explaining the Temporal Value Asymmetry”, *Philosophers’ Imprints*, 12(15): 1–16.

[^thomson-1849]: Thomson, William, 1849, “An Account of Carnot’s Theory of the Motive Power of Heat, with numerical results deduced from Regnault’s Experiments on Steam”, Translated in *Edinb. R. Soc.*, 16, 541. doi:10.1017/S0080456800022481

[^tolman-1934]: Tolman, Richard C., 1934, *Relativity, Thermodynamics and Cosmology*, Oxford: Oxford University Press.

[^uffink-2001]: Uffink, Jos, 2001, “Bluff Your Way in the Second Law of Thermodynamics”, *Studies in the History and Philosophy of Modern Physics*, 32(3): 305–394. doi:10.1016/S1355-2198(01)00016-8

[^uffink-2006]: –––, 2006, “Compendium to the Foundations of Classical Statistical Physics”, in Jeremy Butterfield & John Earman (eds), *Philosophy of Physics* (Handbook of Philosophy), Amsterdam: North-Holland, pp. 923–1074.

[^uhlenbeck-1963]: Uhlenbeck, G.E., and Ford, G.W., 1963, *Lectures in Statistical Mechanics*, Providence: American Mathematical Society.

[^wallace-2010]: Wallace, David, 2010, “Gravity, Entropy, and Cosmology: In Search of Clarity”, *British Journal for the Philosophy of Science*, 61(3): 513–540. doi:10.1093/bjps/axp048

[^wallace-2013]: –––, 2013, “The Arrow of Time in Physics”, in Heather Dyke and Adrian Bardon (ed.), in *A Companion to Philosophy of Time*, Chichester, U.K.: John Wiley & Sons. doi:10.1002/9781118522097.ch16

[^wallace-2018]: –––, 2018. “The Case for Black Hole Thermodynamics Part I: Phenomenological Thermodynamics.” *Studies in History and Philosophy of Modern Physics*, 64: 52–67. doi:10.1016/j.shpsb.2018.05.002

[^wallace-2023]: –––, 2023, “The Logic of the Past Hypothesis.” In Loewer, Barry, W. E. and Weslake, B., editors, *The Probability Map of the Universe: Essays on David Albert’s Time and Chance*, Cambridge: Harvard University Press.

[^wallace-2025a]: –––, 2025a, “On Relativistic Thermodynamics”, *Philosophy of Science*, 92(3): 688–707. doi:10.1017/psa.2025.9

[^wallace-2025b]: –––, 2025b, “Thermodynamics With and Without Irreversibility”, in C. López and O. Lombardi (eds.), *The Arrow of Time: From Local Systems to the Whole Universe*, Cambridge: Cambridge University Press, 12–55.

[^weingard-1977]: Weingard, Robert, 1977, “Space-Time and the Direction of Time”, *Noûs*, 11(2): 119–131. doi:10.2307/2214540

[^westlake-2014]: Westlake, Brad, 2014, “Statistical Mechanical Imperialism”, in Wilson 2014: 241–257. doi:10.1093/acprof:oso/9780199673421.003.0012

[^wilson-2014]: Wilson, Alastair (ed.), 2014, *Chance and Temporal Asymmetry*, Oxford: Oxford University Press. doi:10.1093/acprof:oso/9780199673421.001.0001

[^winsberg-2004]: Winsberg, Eric, 2004, “Can Conditioning on the ‘Past Hypothesis’ Militate Against the Reversibility Objections?”, *Philosophy of Science*, 71(4): 489–504. doi:10.1086/423749

[^zeh-1989]: Zeh, H.-Dieter, 1989, *The Physical Basis of the Direction of Time*, Berlin: Springer-Verlag.

[^zermelo-1896]: Zermelo, E. 1896, “Über einen Satz der Dynamik und die mechanische Wärmetheorie”, *Annalen der Physik*, 57: 485–494.
